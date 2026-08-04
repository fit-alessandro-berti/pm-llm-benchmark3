import os
import traceback
import time
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from common import (
    query_text_simple,
    query_image_simple,
    callback_write,
    set_api_key,
    is_visual_model,
    MODELS_DICT,
    query_text_simple_with_rate_limit,
    query_image_simple_with_rate_limit,
    RATE_LIMITER,
    configure_rate_limiter,
    create_rate_limiter,
    model_session,
    submit_with_context,
)
import common

WAITING_TIME_RETRY = 15
USE_MULTITHREADING = True
# Concurrent questions per model (size of each model's limited response-pool).
MAX_WORKERS = 100
# Concurrent models, each with its own response-pool / Shared session.
MAX_MODEL_WORKERS = 6
TIME_BETWEEN_ANSWERS = 0
MAX_VISUAL_FAILURES = 5
VISUAL_FAILURE_ANSWER = "."

# Default limits applied when creating a per-model response-pool.
DEFAULT_POOL_REQUESTS_PER_MINUTE = 50
DEFAULT_POOL_REQUESTS_PER_HOUR = 1000
DEFAULT_POOL_TOKENS_PER_MINUTE = 90000
DEFAULT_POOL_TOKENS_PER_HOUR = 2000000


def get_answer_path(q, alias_model_name):
    return os.path.join("answers", common.clean_model_name(alias_model_name) + "_" + q).replace(
        ".png", ".txt")


def is_retry_limited_visual_question(q, model_name):
    return q.endswith(".png") and is_visual_model(model_name)


def write_visual_failure_answer(answer_path):
    callback_write(VISUAL_FAILURE_ANSWER, answer_path)


def should_stop_visual_retries(q, model_name, failed_attempts):
    return is_retry_limited_visual_question(q, model_name) and failed_attempts >= MAX_VISUAL_FAILURES


def process_single_question(q, model_name, alias_model_name, use_rate_limit=False, failed_attempts=0):
    """Process a single question."""
    question_path = os.path.join("questions", q)
    answer_path = get_answer_path(q, alias_model_name)

    if not common.is_completed_output(answer_path):
        # Check if file is already being processed (this model's pool).
        if use_rate_limit and RATE_LIMITER.is_file_processing(answer_path):
            print(f"File {answer_path} already being processed, skipping")
            return None

        try:
            if question_path.endswith(".txt"):
                print("Executing", question_path, "for", alias_model_name)
                if use_rate_limit:
                    query_text_simple_with_rate_limit(question_path, answer_path, callback_write,
                                                     use_rate_limit=True)
                    time.sleep(TIME_BETWEEN_ANSWERS)
                else:
                    query_text_simple(question_path, answer_path, callback_write)
                    time.sleep(TIME_BETWEEN_ANSWERS)
            elif is_visual_model(model_name):
                print("Executing", question_path, "for", alias_model_name)
                if use_rate_limit:
                    query_image_simple_with_rate_limit(question_path, answer_path, callback_write,
                                                      use_rate_limit=True)
                else:
                    query_image_simple(question_path, answer_path, callback_write)
            else:
                return False

            if common.is_completed_output(answer_path):
                return True

            failed_attempts += 1
            if should_stop_visual_retries(q, model_name, failed_attempts):
                print(f"Visual question {question_path} failed {failed_attempts} time(s); writing fallback answer")
                write_visual_failure_answer(answer_path)
                return True

            print(f"No completed answer was written for {question_path}; retrying")
            time.sleep(WAITING_TIME_RETRY)
            return None
        except SystemExit as e:
            sys.exit(0)
        except Exception as e:
            if "context length" in str(e):
                return False

            traceback.print_exc()

            failed_attempts += 1
            if should_stop_visual_retries(q, model_name, failed_attempts):
                print(f"Visual question {question_path} failed {failed_attempts} time(s); writing fallback answer")
                write_visual_failure_answer(answer_path)
                return True

            print("sleeping %d seconds ..." % (WAITING_TIME_RETRY))
            time.sleep(WAITING_TIME_RETRY)
            return None  # Indicates retry needed
    return False


def mark_failed_attempt(q, model_name, alias_model_name, failure_counts):
    failed_attempts = failure_counts.get(q, 0) + 1
    failure_counts[q] = failed_attempts

    if should_stop_visual_retries(q, model_name, failed_attempts):
        question_path = os.path.join("questions", q)
        answer_path = get_answer_path(q, alias_model_name)
        print(f"Visual question {question_path} failed {failed_attempts} time(s); writing fallback answer")
        write_visual_failure_answer(answer_path)
        return False

    return True


def _collect_retry_questions(futures, model_name, alias_model_name, failure_counts):
    """Drain futures and return questions that need another attempt."""
    retry_questions = []
    for q, future in futures:
        try:
            result = future.result(timeout=1200)  # 20 minute timeout per question
            if result:
                print(f"Successfully processed {q} for {alias_model_name}")
            elif result is None:
                if mark_failed_attempt(q, model_name, alias_model_name, failure_counts):
                    retry_questions.append(q)
        except Exception as e:
            print(f"Failed to process {q} for {alias_model_name}: {e}")
            traceback.print_exc()
            if mark_failed_attempt(q, model_name, alias_model_name, failure_counts):
                retry_questions.append(q)
    return retry_questions


def _submit_question_batch(executor, questions, model_name, alias_model_name, failure_counts):
    """Submit a batch of questions on the current model session's pool."""
    futures = []
    for q in questions:
        answer_path = get_answer_path(q, alias_model_name)
        if not common.is_completed_output(answer_path):
            future = submit_with_context(
                executor,
                process_single_question,
                q,
                model_name,
                alias_model_name,
                use_rate_limit=True,
                failed_attempts=failure_counts.get(q, 0),
            )
            futures.append((q, future))
    return futures


def _answer_question_body(model_name, alias_model_name, use_multithreading):
    """Core per-model answering loop; expects an active model_session."""
    # Keep module global for single-model scripts; concurrent model threads
    # rely on Shared.MODEL_NAME / session isolation instead.
    common.ANSWERING_MODEL_NAME = model_name

    print("=====", common.Shared.ALIAS_MODEL_NAME,
          f"(pool max_concurrent={RATE_LIMITER.max_concurrent})")

    if use_multithreading is None:
        use_multithreading = USE_MULTITHREADING

    questions = [x for x in os.listdir("questions") if x.endswith(".txt") or x.endswith(".png")]
    failure_counts = {}

    if use_multithreading:
        # Multi-threaded processing within this model's limited response-pool.
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = _submit_question_batch(
                executor, questions, model_name, alias_model_name, failure_counts
            )
            retry_questions = _collect_retry_questions(
                futures, model_name, alias_model_name, failure_counts
            )

            while retry_questions:
                retry_questions = [
                    q for q in retry_questions
                    if not common.is_completed_output(
                        get_answer_path(q, alias_model_name)
                    )
                ]
                if not retry_questions:
                    break

                print(
                    f"Retrying {len(retry_questions)} question(s) for "
                    f"{alias_model_name} after transient failures"
                )
                time.sleep(WAITING_TIME_RETRY)

                with ThreadPoolExecutor(max_workers=MAX_WORKERS) as retry_executor:
                    retry_futures = _submit_question_batch(
                        retry_executor, retry_questions, model_name, alias_model_name,
                        failure_counts
                    )
                    retry_questions = _collect_retry_questions(
                        retry_futures, model_name, alias_model_name, failure_counts
                    )
    else:
        # Single-threaded processing (original behavior)
        for q in questions:
            answer_path = get_answer_path(q, alias_model_name)

            if not common.is_completed_output(answer_path):
                while not common.is_completed_output(answer_path):
                    result = process_single_question(
                        q, model_name, alias_model_name, use_rate_limit=False,
                        failed_attempts=failure_counts.get(q, 0),
                    )
                    if result is None:
                        if mark_failed_attempt(q, model_name, alias_model_name, failure_counts):
                            continue
                        break
                    else:
                        break


def answer_question(model_name, api_url=None, api_key=None, alias_model_name=None, use_multithreading=None,
                    rate_limiter=None):
    """
    Answer all questions for one model.

    Installs an isolated Shared session and limited response-pool when needed so
    several models can run concurrently without clobbering each other's config.
    """
    if alias_model_name is None:
        alias_model_name = model_name

    session_kwargs = {}
    if api_url is not None:
        session_kwargs["API_URL"] = api_url
    if api_key is not None:
        session_kwargs["API_KEY"] = api_key
        session_kwargs["MODEL_NAME"] = model_name
        session_kwargs["ALIAS_MODEL_NAME"] = alias_model_name

    active = common.get_current_session()
    if rate_limiter is None and (active is None or active.rate_limiter is None):
        rate_limiter = create_rate_limiter(
            requests_per_minute=DEFAULT_POOL_REQUESTS_PER_MINUTE,
            requests_per_hour=DEFAULT_POOL_REQUESTS_PER_HOUR,
            tokens_per_minute=DEFAULT_POOL_TOKENS_PER_MINUTE,
            tokens_per_hour=DEFAULT_POOL_TOKENS_PER_HOUR,
            max_concurrent=MAX_WORKERS,
        )

    with model_session(rate_limiter=rate_limiter, **session_kwargs):
        if api_key is None and common.Shared.API_KEY is None:
            set_api_key("answer")
        if common.Shared.MODEL_NAME is None:
            common.Shared.MODEL_NAME = model_name
        if common.Shared.ALIAS_MODEL_NAME is None:
            common.Shared.ALIAS_MODEL_NAME = alias_model_name
        _answer_question_body(model_name, alias_model_name, use_multithreading)


def _build_model_job(llm):
    """Resolve provider config for a cleaned model name. Returns a job dict or None."""
    for provider in MODELS_DICT:
        info = MODELS_DICT[provider]
        cleaned_models = {common.clean_model_name(x): x for x in info["models"]}
        if llm not in cleaned_models:
            continue

        job = {
            "llm": llm,
            "provider": provider,
            "this_provider": provider,
            "api_url": None,
            "api_key": None,
            "model_name": None,
            "alias_model_name": None,
            "system_prompt": None,
            "thinking_tokens": None,
            "reasoning_effort": None,
            "temperature": None,
            "max_tokens": 32000,
            "added_to_prompt": None,
            "tools": None,
            "added_to_payload": None,
        }

        if provider == "manual":
            ref = MODELS_DICT[provider]["models"][cleaned_models[llm]]
            if "provider" in ref and ref["provider"] in MODELS_DICT:
                job["api_url"] = MODELS_DICT[ref["provider"]]["api_url"]
                job["api_key"] = MODELS_DICT[ref["provider"]]["api_key"]
                job["model_name"] = ref["base_model"]
                job["alias_model_name"] = cleaned_models[llm]
                job["system_prompt"] = ref.get("system_prompt")
                job["thinking_tokens"] = ref.get("thinking_tokens")
                job["reasoning_effort"] = ref.get("reasoning_effort")
                job["temperature"] = ref.get("temperature")
                job["max_tokens"] = ref["max_tokens"] if "max_tokens" in ref else 32000
                job["added_to_prompt"] = ref.get("added_to_prompt")
                job["tools"] = ref.get("tools")
                job["added_to_payload"] = ref.get("added_to_payload")
                job["this_provider"] = ref["provider"]
            else:
                job["api_key"] = None
        else:
            job["api_url"] = info["api_url"]
            job["api_key"] = info["api_key"]
            job["model_name"] = cleaned_models[llm]
            job["alias_model_name"] = cleaned_models[llm]
            job["this_provider"] = provider

        return job

    return None


def _run_model_job(job, excluded_providers=None, use_multithreading=None):
    """Run one model end-to-end on its own thread with a private response-pool."""
    if excluded_providers is None:
        excluded_providers = set()

    provider = job["provider"]
    this_provider = job["this_provider"]
    api_key = job["api_key"]
    model_name = job["model_name"]
    alias_model_name = job["alias_model_name"]

    if api_key is None:
        return

    if provider in excluded_providers or this_provider in excluded_providers:
        print(model_name, provider, "excluded")
        return

    # Fresh limited response-pool for this model only.
    pool = create_rate_limiter(
        requests_per_minute=DEFAULT_POOL_REQUESTS_PER_MINUTE,
        requests_per_hour=DEFAULT_POOL_REQUESTS_PER_HOUR,
        tokens_per_minute=DEFAULT_POOL_TOKENS_PER_MINUTE,
        tokens_per_hour=DEFAULT_POOL_TOKENS_PER_HOUR,
        max_concurrent=MAX_WORKERS,
    )

    try:
        with model_session(
            rate_limiter=pool,
            API_URL=job["api_url"],
            API_KEY=api_key,
            MODEL_NAME=model_name,
            ALIAS_MODEL_NAME=alias_model_name,
            SYSTEM_PROMPT=job["system_prompt"],
            ANTHROPIC_THINKING_TOKENS=job["thinking_tokens"],
            PAYLOAD_REASONING_EFFORT=job["reasoning_effort"],
            CUSTOM_TEMPERATURE=job["temperature"],
            MAX_REQUESTED_TOKENS=job["max_tokens"],
            ADDED_TO_PROMPT=job["added_to_prompt"],
            TOOLS_PAYLOAD=job["tools"],
            ADDED_TO_PAYLOAD=job["added_to_payload"],
        ):
            answer_question(
                model_name,
                api_url=job["api_url"],
                api_key=api_key,
                alias_model_name=alias_model_name,
                use_multithreading=use_multithreading,
                rate_limiter=pool,
            )
    except Exception:
        print(f"Model job failed for {alias_model_name}:")
        traceback.print_exc()


def answer_models_concurrently(ordered_llms, excluded_providers=None, max_model_workers=None,
                               use_multithreading=None):
    """
    Process several models concurrently. Each model thread installs its own
    Shared settings and limited response-pool (RateLimiter).
    """
    if excluded_providers is None:
        excluded_providers = set()
    if max_model_workers is None:
        max_model_workers = MAX_MODEL_WORKERS
    if use_multithreading is None:
        use_multithreading = USE_MULTITHREADING

    jobs = []
    for llm in ordered_llms:
        job = _build_model_job(llm)
        if job is None:
            print("problem with " + str(llm) + " not found!")
            continue
        jobs.append(job)

    if not jobs:
        print("No models to process")
        return

    workers = max(1, min(max_model_workers, len(jobs)))
    print(
        f"Processing {len(jobs)} model(s) with up to {workers} concurrent model thread(s); "
        f"each uses a response-pool of max_concurrent={MAX_WORKERS}"
    )

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [
            executor.submit(_run_model_job, job, excluded_providers, use_multithreading)
            for job in jobs
        ]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception:
                traceback.print_exc()


if __name__ == "__main__":
    # Process-wide default pool (used only when a model run does not install its own).
    configure_rate_limiter(
        requests_per_minute=DEFAULT_POOL_REQUESTS_PER_MINUTE,
        requests_per_hour=DEFAULT_POOL_REQUESTS_PER_HOUR,
        tokens_per_minute=DEFAULT_POOL_TOKENS_PER_MINUTE,
        tokens_per_hour=DEFAULT_POOL_TOKENS_PER_HOUR,
        max_concurrent=MAX_WORKERS,
    )

    if True:
        e_m_name = common.clean_model_name(common.EVALUATING_MODEL_NAME)
        common.insert_api_keys()

        ordered_llms, referenced_llms = common.get_ordered_references_llms(".")
        ordered_llms = ordered_llms + referenced_llms

        #ordered_llms = ordered_llms[::-1]

        answer_models_concurrently(
            ordered_llms,
            excluded_providers={},
            max_model_workers=MAX_MODEL_WORKERS,
            use_multithreading=USE_MULTITHREADING,
        )
    else:
        models = [common.ANSWERING_MODEL_NAME]
        for model in models:
            answer_question(model, use_multithreading=USE_MULTITHREADING)
