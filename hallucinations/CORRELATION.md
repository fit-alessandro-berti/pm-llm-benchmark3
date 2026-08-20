# Correlation Analysis Report

================================================================================
## VARIABLE EXPLANATIONS
================================================================================

### HALLUCINATION CATEGORIES:
----------------------------------------
**Category 1 - Input Misalignment:**
- 1a_instruction_override: Model ignores explicit instructions
- 1b_context_omission: Model omits provided context
- 1c_prompt_contradiction: Model contradicts the prompt

**Category 2 - Factual Errors:**
- 2a_concept_fabrication: Model invents concepts/facts
- 2b_spurious_numeric: Model generates incorrect numbers
- 2c_false_citation: Model creates false references

**Category 3 - Logical Errors:**
- 3a_unsupported_leap: Model makes unsupported logical jumps
- 3b_self_contradiction: Model contradicts itself
- 3c_circular_reasoning: Model uses circular logic

**Category 4 - Technical Errors:**
- 4a_syntax_error: Model produces syntactically incorrect output
- 4b_model_semantics_breach: Model violates semantic rules
- 4c_visual_descr_mismatch: Model misinterprets visual descriptions

### MODEL FEATURES:
----------------------------------------
- **model_size**: Total model parameters in billions (B)
- **is_opensource**: Binary (1=open source, 0=proprietary)
- **is_reasoning**: Binary (1=reasoning model, 0=standard model)
- **benchmark_score**: Performance score from PM-LLM benchmark
- **days_since_2024**: Days since Jan 1, 2024 (model age indicator)

================================================================================
## CORRELATION ANALYSIS: Hallucinations vs Model Features
================================================================================

================================================================================
## CATEGORY-LEVEL CORRELATIONS (Summed Categories)
================================================================================

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.230 
- Linear fit: y = -0.162x + 7.7
- P-value: 0.0982
- N samples: 53

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.121 
- Linear fit: y = -1.216x + 3.4
- P-value: 0.3866
- N samples: 53

**Days Since 2024-01-01:**
- Correlation: -0.046 
- Linear fit: y = -0.001x + 3.6
- P-value: 0.8464
- N samples: 20

**Is Open Source:**
- Correlation: 0.027 
- Linear fit: y = 0.246x + 2.4
- P-value: 0.8461
- N samples: 53

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.205 
- Linear fit: y = -0.002x + 8.5
- P-value: 0.4306
- N samples: 17

**Is Open Source:**
- Correlation: -0.198 
- Linear fit: y = -2.620x + 8.9
- P-value: 0.1549
- N samples: 53

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Is Reasoning Model:**
- Correlation: 0.038 
- Linear fit: y = 0.563x + 7.2
- P-value: 0.7849
- N samples: 53

**Benchmark Score:**
- Correlation: -0.002 
- Linear fit: y = -0.002x + 7.7
- P-value: 0.9864
- N samples: 53

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.411 
- Linear fit: y = -0.004x + 26.1
- P-value: 0.1010
- N samples: 17

**Is Open Source:**
- Correlation: -0.346 *
- Linear fit: y = -6.776x + 26.8
- P-value: 0.0111
- N samples: 53

**Days Since 2024-01-01:**
- Correlation: -0.309 
- Linear fit: y = -0.012x + 33.8
- P-value: 0.1849
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.298 *
- Linear fit: y = -6.475x + 28.1
- P-value: 0.0301
- N samples: 53

**Benchmark Score:**
- Correlation: -0.155 
- Linear fit: y = -0.236x + 31.1
- P-value: 0.2682
- N samples: 53

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.276 *
- Linear fit: y = -0.132x + 5.9
- P-value: 0.0458
- N samples: 53

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.035 
- Linear fit: y = -0.235x + 1.9
- P-value: 0.8058
- N samples: 53

**Is Open Source:**
- Correlation: -0.014 
- Linear fit: y = -0.087x + 1.7
- P-value: 0.9197
- N samples: 53

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.287 
- Linear fit: y = -0.007x + 40.3
- P-value: 0.2647
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: -0.259 
- Linear fit: y = -0.028x + 57.2
- P-value: 0.2707
- N samples: 20

**Is Open Source:**
- Correlation: -0.232 
- Linear fit: y = -9.386x + 40.0
- P-value: 0.0940
- N samples: 53

**Benchmark Score:**
- Correlation: -0.164 
- Linear fit: y = -0.518x + 51.9
- P-value: 0.2392
- N samples: 53

**Is Reasoning Model:**
- Correlation: -0.163 
- Linear fit: y = -7.311x + 40.6
- P-value: 0.2432
- N samples: 53

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.230 
- Linear fit: y = -0.162x + 7.7
- P-value: 0.0982
- N samples: 53

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.121 
- Linear fit: y = -1.216x + 3.4
- P-value: 0.3866
- N samples: 53

**Days Since 2024-01-01:**
- Correlation: -0.046 
- Linear fit: y = -0.001x + 3.6
- P-value: 0.8464
- N samples: 20

**Is Open Source:**
- Correlation: 0.027 
- Linear fit: y = 0.246x + 2.4
- P-value: 0.8461
- N samples: 53

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.205 
- Linear fit: y = -0.002x + 8.5
- P-value: 0.4306
- N samples: 17

**Is Open Source:**
- Correlation: -0.198 
- Linear fit: y = -2.620x + 8.9
- P-value: 0.1549
- N samples: 53

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Is Reasoning Model:**
- Correlation: 0.038 
- Linear fit: y = 0.563x + 7.2
- P-value: 0.7849
- N samples: 53

**Benchmark Score:**
- Correlation: -0.002 
- Linear fit: y = -0.002x + 7.7
- P-value: 0.9864
- N samples: 53

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.411 
- Linear fit: y = -0.004x + 26.1
- P-value: 0.1010
- N samples: 17

**Is Open Source:**
- Correlation: -0.346 *
- Linear fit: y = -6.776x + 26.8
- P-value: 0.0111
- N samples: 53

**Days Since 2024-01-01:**
- Correlation: -0.309 
- Linear fit: y = -0.012x + 33.8
- P-value: 0.1849
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.298 *
- Linear fit: y = -6.475x + 28.1
- P-value: 0.0301
- N samples: 53

**Benchmark Score:**
- Correlation: -0.155 
- Linear fit: y = -0.236x + 31.1
- P-value: 0.2682
- N samples: 53

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.276 *
- Linear fit: y = -0.132x + 5.9
- P-value: 0.0458
- N samples: 53

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.035 
- Linear fit: y = -0.235x + 1.9
- P-value: 0.8058
- N samples: 53

**Is Open Source:**
- Correlation: -0.014 
- Linear fit: y = -0.087x + 1.7
- P-value: 0.9197
- N samples: 53

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.183 
- Linear fit: y = -0.058x + 2.7
- P-value: 0.1888
- N samples: 53

**Is Reasoning Model:**
- Correlation: -0.170 
- Linear fit: y = -0.768x + 1.4
- P-value: 0.2247
- N samples: 53

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.8198
- N samples: 17

**Is Open Source:**
- Correlation: 0.054 
- Linear fit: y = 0.221x + 0.7
- P-value: 0.7005
- N samples: 53

**Days Since 2024-01-01:**
- Correlation: 0.049 
- Linear fit: y = 0.001x + 0.5
- P-value: 0.8384
- N samples: 20

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.211 
- Linear fit: y = -0.001x + 1.9
- P-value: 0.4158
- N samples: 17

**Benchmark Score:**
- Correlation: -0.184 
- Linear fit: y = -0.065x + 3.4
- P-value: 0.1867
- N samples: 53

**Days Since 2024-01-01:**
- Correlation: -0.080 
- Linear fit: y = -0.001x + 2.3
- P-value: 0.7365
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.032 
- Linear fit: y = -0.163x + 1.4
- P-value: 0.8179
- N samples: 53

**Is Open Source:**
- Correlation: -0.023 
- Linear fit: y = -0.103x + 1.3
- P-value: 0.8724
- N samples: 53

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.272 *
- Linear fit: y = -0.038x + 1.6
- P-value: 0.0489
- N samples: 53

**Is Reasoning Model:**
- Correlation: -0.143 
- Linear fit: y = -0.284x + 0.6
- P-value: 0.3082
- N samples: 53

**Days Since 2024-01-01:**
- Correlation: -0.099 
- Linear fit: y = -0.000x + 0.7
- P-value: 0.6765
- N samples: 20

**Is Open Source:**
- Correlation: 0.071 
- Linear fit: y = 0.128x + 0.3
- P-value: 0.6113
- N samples: 53

**Model Size (B):**
- Correlation: 0.035 
- Linear fit: y = 0.000x + 0.4
- P-value: 0.8934
- N samples: 17

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.323 
- Linear fit: y = -0.001x + 1.8
- P-value: 0.2066
- N samples: 17

**Is Open Source:**
- Correlation: 0.226 
- Linear fit: y = 0.729x + 1.0
- P-value: 0.1032
- N samples: 53

**Benchmark Score:**
- Correlation: -0.146 
- Linear fit: y = -0.037x + 2.5
- P-value: 0.2955
- N samples: 53

**Is Reasoning Model:**
- Correlation: 0.099 
- Linear fit: y = 0.354x + 1.1
- P-value: 0.4802
- N samples: 53

**Days Since 2024-01-01:**
- Correlation: 0.021 
- Linear fit: y = 0.000x + 1.1
- P-value: 0.9297
- N samples: 20

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.272 *
- Linear fit: y = -3.397x + 7.7
- P-value: 0.0489
- N samples: 53

**Model Size (B):**
- Correlation: -0.162 
- Linear fit: y = -0.001x + 6.5
- P-value: 0.5338
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: -0.121 
- Linear fit: y = -0.004x + 8.8
- P-value: 0.6113
- N samples: 20

**Benchmark Score:**
- Correlation: 0.019 
- Linear fit: y = 0.019x + 5.4
- P-value: 0.8903
- N samples: 53

**Is Reasoning Model:**
- Correlation: 0.007 
- Linear fit: y = 0.093x + 5.9
- P-value: 0.9620
- N samples: 53

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: 0.360 
- Linear fit: y = 0.001x + -0.6
- P-value: 0.1188
- N samples: 20

**Model Size (B):**
- Correlation: 0.228 
- Linear fit: y = 0.000x + 0.2
- P-value: 0.3787
- N samples: 17

**Benchmark Score:**
- Correlation: 0.201 
- Linear fit: y = 0.015x + -0.2
- P-value: 0.1482
- N samples: 53

**Is Reasoning Model:**
- Correlation: 0.106 
- Linear fit: y = 0.116x + 0.2
- P-value: 0.4486
- N samples: 53

**Is Open Source:**
- Correlation: 0.049 
- Linear fit: y = 0.048x + 0.3
- P-value: 0.7256
- N samples: 53

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.378 **
- Linear fit: y = -5.799x + 22.2
- P-value: 0.0052
- N samples: 53

**Model Size (B):**
- Correlation: -0.322 
- Linear fit: y = -0.002x + 21.7
- P-value: 0.2069
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: -0.299 
- Linear fit: y = -0.010x + 28.0
- P-value: 0.2000
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.270 
- Linear fit: y = -4.588x + 22.7
- P-value: 0.0508
- N samples: 53

**Benchmark Score:**
- Correlation: -0.140 
- Linear fit: y = -0.167x + 24.7
- P-value: 0.3183
- N samples: 53

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.379 
- Linear fit: y = -0.001x + 4.4
- P-value: 0.1339
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.274 *
- Linear fit: y = -1.847x + 5.4
- P-value: 0.0473
- N samples: 53

**Days Since 2024-01-01:**
- Correlation: -0.187 
- Linear fit: y = -0.003x + 5.8
- P-value: 0.4300
- N samples: 20

**Is Open Source:**
- Correlation: -0.161 
- Linear fit: y = -0.979x + 4.6
- P-value: 0.2496
- N samples: 53

**Benchmark Score:**
- Correlation: -0.138 
- Linear fit: y = -0.065x + 6.2
- P-value: 0.3244
- N samples: 53

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.170 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.5133
- N samples: 17

**Benchmark Score:**
- Correlation: -0.132 
- Linear fit: y = -0.004x + 0.2
- P-value: 0.3472
- N samples: 53

**Days Since 2024-01-01:**
- Correlation: 0.100 
- Linear fit: y = 0.000x + -0.1
- P-value: 0.6745
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.095 
- Linear fit: y = -0.040x + 0.1
- P-value: 0.4969
- N samples: 53

**Is Open Source:**
- Correlation: 0.004 
- Linear fit: y = 0.001x + 0.0
- P-value: 0.9788
- N samples: 53

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.487 *
- Linear fit: y = -0.007x + 6.3
- P-value: 0.0296
- N samples: 20

**Benchmark Score:**
- Correlation: -0.140 
- Linear fit: y = -0.032x + 1.5
- P-value: 0.3190
- N samples: 53

**Is Open Source:**
- Correlation: -0.111 
- Linear fit: y = -0.323x + 0.6
- P-value: 0.4300
- N samples: 53

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.8201
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.043 
- Linear fit: y = -0.139x + 0.5
- P-value: 0.7612
- N samples: 53

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.352 
- Linear fit: y = -0.004x + 4.0
- P-value: 0.1282
- N samples: 20

**Benchmark Score:**
- Correlation: -0.287 *
- Linear fit: y = -0.098x + 4.4
- P-value: 0.0375
- N samples: 53

**Model Size (B):**
- Correlation: -0.134 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.6083
- N samples: 17

**Is Open Source:**
- Correlation: 0.036 
- Linear fit: y = 0.160x + 1.1
- P-value: 0.7954
- N samples: 53

**Is Reasoning Model:**
- Correlation: -0.012 
- Linear fit: y = -0.056x + 1.3
- P-value: 0.9345
- N samples: 53

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.357 
- Linear fit: y = 0.000x + 0.0
- P-value: 0.1590
- N samples: 17

**Is Open Source:**
- Correlation: 0.202 
- Linear fit: y = 0.077x + -0.0
- P-value: 0.1473
- N samples: 53

**Is Reasoning Model:**
- Correlation: -0.095 
- Linear fit: y = -0.040x + 0.1
- P-value: 0.4969
- N samples: 53

**Benchmark Score:**
- Correlation: -0.073 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.6032
- N samples: 53

**Days Since 2024-01-01:**
- Correlation: -0.024 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.9216
- N samples: 20

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**4a_syntax_error vs Days Since 2024-01-01:**
  r = -0.487, y = -0.007x + 6.3

**category4_technical_errors vs Days Since 2024-01-01:**
  r = -0.458, y = -0.011x + 10.5

**3a_unsupported_leap vs Is Open Source:**
  r = -0.378, y = -5.799x + 22.2

**category3_logical_errors vs Is Open Source:**
  r = -0.346, y = -6.776x + 26.8


================================================================================
## Legend:
- \* p < 0.05
- \*\* p < 0.01
- \*\*\* p < 0.001
================================================================================

================================================================================
## INTER-CATEGORY CORRELATIONS
================================================================================

How different hallucination categories correlate with each other:
(Shows if models prone to one type also tend to have others)
------------------------------------------------------------

### CATEGORY-LEVEL CORRELATIONS
----------------------------------------

**Category 1: Input Misalignment**
  vs **Category 2: Factual Errors:**
- Correlation: 0.663 ***
- Linear fit: y = 0.970x + 5.2

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.603 ***
- Linear fit: y = 1.308x + 20.2

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.461 ***
- Linear fit: y = 0.313x + 0.9

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.650 ***
- Linear fit: y = 0.963x + 16.2

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.475 ***
- Linear fit: y = 0.220x + 0.0

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.438 **
- Linear fit: y = 0.137x + -1.5

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.967 ***, y = 0.757x + 1.6

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.967 ***, y = 0.914x + -0.9

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.927 ***, y = 0.466x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.892 ***, y = 0.637x + 0.1

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.863 ***, y = 0.390x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.778 ***, y = 0.242x + -1.6

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.759 ***, y = 0.362x + -0.2

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.722 ***, y = 0.144x + 0.0

**1a: Instruction Override vs 3b: Self Contradiction:**
  r = 0.704 ***, y = 1.049x + 3.2

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.677 ***, y = 0.432x + -4.2

**Category 1: Input Misalignment vs 3b: Self Contradiction:**
  r = 0.672 ***, y = 0.453x + 2.9

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = 0.663 ***, y = 0.970x + 5.2

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = 0.659 ***, y = 0.226x + -0.4

**1b: Context Omission vs 1c: Prompt Contradiction:**
  r = 0.659 ***, y = 0.261x + 0.1

**Category 2: Factual Errors vs 1a: Instruction Override:**
  r = 0.656 ***, y = 0.203x + -0.7

**Category 1: Input Misalignment vs 2b: Spurious Numeric:**
  r = 0.654 ***, y = 0.905x + 3.7

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.650 ***, y = 0.963x + 16.2

**1a: Instruction Override vs 1b: Context Omission:**
  r = 0.649 ***, y = 0.721x + 0.7

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = 0.644 ***, y = 1.774x + 3.7

**1a: Instruction Override vs 2b: Spurious Numeric:**
  r = 0.639 ***, y = 1.957x + 4.3

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
