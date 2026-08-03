# PM-LLM-Benchmark 3.0

**This repository contains PM-LLM-Benchmark 3.0**, a new generation of the benchmark with a harder, more open-ended set of prompts than [PM-LLM-Benchmark v 2.2](https://github.com/fit-alessandro-berti/pm-llm-benchmark) and v 1.0.
The paper describing PM-LLM-Benchmark v 1.0 is available [here](https://arxiv.org/pdf/2407.13244).

Process mining benefits significantly from the domain knowledge provided by LLMs. *PM-LLM-Benchmark* is a qualitative benchmark for PM-on-LLM: model answers are graded by another expert LLM (**LLM-as-a-Judge**). Version 3.0 keeps that design but replaces the older category mix with eight process-mining reasoning themes, each identified by a stable three-letter code.

The prompts are reported in the *questions/* folder (56 textual tasks: 7 prompts × 8 categories). There is deliberately **no single hidden reference answer** for most tasks; judges reward process-mining competence, use of evidence, treatment of uncertainty, and argument quality.

## Categories (three-letter codes)

| Code | Category | Focus |
| --- | --- | --- |
| **CCR** | Causal and Counterfactual Process Reasoning | Attribution, mediation, transportability, and case-level counterfactuals under process constraints |
| **SQT** | Stochastic Performance, Queue Mining, and Temporal Statistics | Queues, delay decomposition, non-stationarity, censoring, and staffing under imperfect timing data |
| **OCR** | Object-Centric and Cross-Instance Process Reasoning | Case notions, OCEL relations, cross-instance bottlenecks, and object-centric conformance |
| **FMS** | Formal Process-Model Synthesis, Equivalence, and Repair | Process trees, Petri nets, POWL/BPMN conversions, soundness repair, and model critique |
| **MCA** | Multi-Perspective Conformance and Compliance Argumentation | Conflicting norms, data-aware and temporal conformance, severity, and dialectical defense of norms |
| **PPM** | Predictive Process Monitoring under Uncertainty | Next-state and remaining-time prediction, censoring, early warning, explanations, and drift |
| **ORF** | Organizational Mining, Resource Reasoning, and Procedural Fairness | Org networks, shadow roles, collusion vs necessity, fairness, and restructuring impact |
| **RPR** | Robust Process Redesign, Optimization, and Strategic Reasoning | Multi-objective redesign, shocks, automation portfolios, sustainability, resilience, and decision memos |

## Textual Question Index

| Question | First 50 chars | Last 50 chars |
| --- | --- | --- |
| `cat01_01` | ROLE You are a senior process-mining and causal-in | ntion that learns while limiting operational risk. |
| `cat01_02` | ROLE You are the lead process-mining scientist for | entifiability, not merely name a causal estimator. |
| `cat01_03` | ROLE You are a process-mining researcher asked to  | t that can improve both performance and knowledge. |
| `cat01_04` | ROLE You are investigating a sudden deterioration  | itness can be obtained by an overpermissive model. |
| `cat01_05` | ROLE You are responsible for drift diagnosis in a  | ng that can distinguish recurrence from new drift. |
| `cat01_06` | ROLE You are advising two organizations that execu | ts both causal effect and implementation fidelity. |
| `cat01_07` | ROLE You are a process-mining and operations exper | tions can shift congestion or risk to other cases. |
| `cat02_01` | BENCHMARK CONTEXT This is an open-ended process-mi | urvive plausible timestamp and imputation choices. |
| `cat02_02` | BENCHMARK CONTEXT This is an open-ended process-mi | ts, appointments, urgency, and shortest-job rules. |
| `cat02_03` | BENCHMARK CONTEXT This is an open-ended process-mi |  noncritical branch may have no case-level effect. |
| `cat02_04` | BENCHMARK CONTEXT This is an open-ended process-mi |  discovery with independent data-quality evidence. |
| `cat02_05` | BENCHMARK CONTEXT This is an open-ended process-mi | regates are insufficient for a queueing-law claim. |
| `cat02_06` | BENCHMARK CONTEXT This is an open-ended process-mi | ocess events as leakage-prone baseline predictors. |
| `cat02_07` | BENCHMARK CONTEXT This is an open-ended process-mi | e it minimizes average delay in the base scenario. |
| `cat03_01` | You are given a synthetic OCEL 2.0-style snapshot  |  not. - Aim for 1,800–2,800 words, excluding code. |
| `cat03_02` | You are given an incomplete OCEL 2.0-style dataset | im for 1,700–2,700 words, excluding code and JSON. |
| `cat03_03` | A manufacturer has six jobs. Traditional flattenin | fied. - Aim for 1,800–2,800 words, excluding code. |
| `cat03_04` | You must interpret object-centric deviations again | fied. - Aim for 1,700–2,600 words, excluding code. |
| `cat03_05` | You are given eight compact object-centric executi | tent. - Aim for 1,700–2,600 words, excluding code. |
| `cat03_06` | Construct an OCEL 2.0-style in-memory dataset from | ity and semantic clarity matter more than brevity. |
| `cat03_07` | An OCEL has been assembled from ERP, WMS, handheld | icit. - Aim for 1,900–2,900 words, excluding code. |
| `cat04_01` | TASK TYPE Deductive modeling, representational rea | evidence to inspect rather than proof of fidelity. |
| `cat04_02` | TASK TYPE Formal diagnosis, marking-based reasonin | e repaired net matches every business expectation. |
| `cat04_03` | TASK TYPE Model selection, compositional reasoning | cannot be recovered from activity sequences alone. |
| `cat04_04` | TASK TYPE Inductive and abductive model discovery, | validation that could actually reduce uncertainty. |
| `cat04_05` | TASK TYPE Formal comparison, equivalence-notion se | ion preserves the semantics it claims to preserve. |
| `cat04_06` | TASK TYPE Transformation reasoning, semantic-invar | tion or visualization with behavioral equivalence. |
| `cat04_07` | TASK TYPE Critical multi-criteria reasoning, metri | dissenting argument rather than a token objection. |
| `cat05_01` | You are an independent process-compliance analyst. | identify evidence that would reverse a conclusion. |
| `cat05_02` | You are reviewing payment-process conformance for  | 4Py behavior you cannot guarantee across versions. |
| `cat05_03` | You are assessing transaction-review compliance fr | ope, change provenance, and stable event ordering. |
| `cat05_04` | You are evaluating incident-response timing across | er interval overlap is sufficient for enforcement. |
| `cat05_05` | You are investigating change-control cases at a ph | nd name the three highest-priority investigations. |
| `cat05_06` | You are given process alignments and business cont |  business-severity assessment in separate columns. |
| `cat05_07` | You are an independent reviewer of supplier-onboar | st defensible approximation rather than hiding it. |
| `cat06_01` | ROLE You are an expert in predictive process monit | sk, or attach unjustifiably precise probabilities. |
| `cat06_02` | ROLE You are an expert in predictive process monit | sion, or present a single precise completion time. |
| `cat06_03` | ROLE You are designing an uncertainty-aware predic |  random split across policy and migration periods. |
| `cat06_04` | ROLE You are designing a portfolio-level early-war | nore segment-level uncertainty and feedback loops. |
| `cat06_05` | ROLE You are auditing explanations from a predicti | ations or declare every correlated feature causal. |
| `cat06_06` | ROLE You are an expert in predictive process monit |  as a substitute for mandatory independent review. |
| `cat06_07` | ROLE You are auditing a predictive process monitor |  breach rate as fully comparable to mature months. |
| `cat07_01` | You are analyzing the organizational dimension of  | - Do not assume a ground truth label for her role. |
| `cat07_02` | You are given summarized event-log evidence for an | les are improper; discuss both benefits and risks. |
| `cat07_03` | You are assisting an internal audit team reviewing | ollapse all resource pairs into one risk category. |
| `cat07_04` | You are assessing a public-benefits case-managemen | moving support steps merely to improve cycle time. |
| `cat07_05` | You are analyzing event-level performance in a cla | oving quality checks simply to improve throughput. |
| `cat07_06` | You are asked to design a dynamic resource-assignm | socio-technical and explainability considerations. |
| `cat07_07` | You are asked to forecast the process-mining impac | end full rollout without a monitoring/pilot logic. |
| `cat08_01` | You are advising the executive sponsor of a consum | tics, customer outcomes, and resource information. |
| `cat08_02` | You are advising the operations team of a regional |  resources, variants, and candidate interventions. |
| `cat08_03` | You are advising a bank that wants to automate par | rtifacts, resource networks, and control findings. |
| `cat08_04` | You are advising an industrial spare-parts distrib | evidence, transport evidence, and policy findings. |
| `cat08_05` | You are advising a pharmaceutical wholesaler after | s, adaptation patterns, and segment/product risks. |
| `cat08_06` | You are advising a municipality that wants to buil | lation that has not been calibrated and validated. |
| `cat08_07` | You are preparing an executive decision memo for a | s, social/resource networks, and segment outcomes. |

## Evaluation procedure

For every prompt:

* Provide the prompt to an LLM (content of the corresponding file under `questions/` as-is).
* Collect the model output under `answers/`.
* Use an expert LLM (LLM-as-a-Judge) to grade the output. The evaluation template asks the judge to score the answer from **1.0 (minimum) to 10.0 (maximum)** given the original question and the candidate answer.

The overall score of the benchmark is obtained by summing the per-question scores and dividing by **10.0**. Leaderboard tables also report per-category averages using the codes above (**CCR** … **RPR**).

## Running the scripts

Scripts to answer and evaluate questions against OpenAI-compatible APIs (including xAI Grok) are available in **`answer.py`** and **`evalscript.py`**. Shared configuration lives in **`common.py`** and **`models_config.json`**.

* Default **answering** model / API key: configure via CLI args, `models_config.json`, and `answering_api_key.txt` (or provider env vars such as `OPENAI_API_KEY`, `GROK_API_KEY`).
* Default **judge** model: `grok-4.5` at `https://api.x.ai/v1/` (override with CLI; key via `GROK_API_KEY`).
* Aggregated leaderboards are produced with `utils/overall_table.py` and `utils/table_per_model.py`.

Example flow:

```bash
# Generate answers for configured models
python answer.py

# Judge answers with the default evaluating model
python evalscript.py

# Build leaderboard markdown from evaluation-* folders
python -m utils.overall_table
```

## Leaderboards

Leaderboards will list model results as evaluated by the configured judge LLM (default: **grok-4.5**). Generated files follow the pattern `leaderboard_<judge>.md`.
