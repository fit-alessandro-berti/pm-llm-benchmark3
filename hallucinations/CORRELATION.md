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
- Correlation: -0.253 *
- Linear fit: y = -0.167x + 8.3
- P-value: 0.0310
- N samples: 73

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.174 
- Linear fit: y = 1.556x + 2.1
- P-value: 0.1406
- N samples: 73

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.019 
- Linear fit: y = -0.217x + 2.9
- P-value: 0.8720
- N samples: 73

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.149 
- Linear fit: y = -1.859x + 8.0
- P-value: 0.2090
- N samples: 73

**Model Size (B):**
- Correlation: -0.059 
- Linear fit: y = -0.000x + 7.5
- P-value: 0.6606
- N samples: 57

**Days Since 2024-01-01:**
- Correlation: -0.058 
- Linear fit: y = -0.003x + 9.7
- P-value: 0.6706
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.031 
- Linear fit: y = 0.489x + 6.7
- P-value: 0.7948
- N samples: 73

**Benchmark Score:**
- Correlation: 0.007 
- Linear fit: y = 0.007x + 6.9
- P-value: 0.9522
- N samples: 73

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.215 
- Linear fit: y = -3.757x + 21.6
- P-value: 0.0674
- N samples: 73

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Benchmark Score:**
- Correlation: -0.171 
- Linear fit: y = -0.221x + 27.2
- P-value: 0.1485
- N samples: 73

**Is Reasoning Model:**
- Correlation: -0.099 
- Linear fit: y = -2.185x + 21.6
- P-value: 0.4045
- N samples: 73

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.212 
- Linear fit: y = -1.503x + 3.2
- P-value: 0.0713
- N samples: 73

**Benchmark Score:**
- Correlation: 0.116 
- Linear fit: y = 0.061x + 0.5
- P-value: 0.3295
- N samples: 73

**Is Reasoning Model:**
- Correlation: 0.111 
- Linear fit: y = 0.998x + 1.7
- P-value: 0.3478
- N samples: 73

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Days Since 2024-01-01:**
- Correlation: 0.063 
- Linear fit: y = 0.002x + 1.1
- P-value: 0.6402
- N samples: 57

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.151 
- Linear fit: y = -5.531x + 34.9
- P-value: 0.2035
- N samples: 73

**Days Since 2024-01-01:**
- Correlation: -0.139 
- Linear fit: y = -0.021x + 51.2
- P-value: 0.3022
- N samples: 57

**Benchmark Score:**
- Correlation: -0.119 
- Linear fit: y = -0.322x + 43.1
- P-value: 0.3176
- N samples: 73

**Model Size (B):**
- Correlation: -0.066 
- Linear fit: y = -0.001x + 34.3
- P-value: 0.6271
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.015 
- Linear fit: y = -0.712x + 33.0
- P-value: 0.8976
- N samples: 73

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.253 *
- Linear fit: y = -0.167x + 8.3
- P-value: 0.0310
- N samples: 73

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.174 
- Linear fit: y = 1.556x + 2.1
- P-value: 0.1406
- N samples: 73

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.019 
- Linear fit: y = -0.217x + 2.9
- P-value: 0.8720
- N samples: 73

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.149 
- Linear fit: y = -1.859x + 8.0
- P-value: 0.2090
- N samples: 73

**Model Size (B):**
- Correlation: -0.059 
- Linear fit: y = -0.000x + 7.5
- P-value: 0.6606
- N samples: 57

**Days Since 2024-01-01:**
- Correlation: -0.058 
- Linear fit: y = -0.003x + 9.7
- P-value: 0.6706
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.031 
- Linear fit: y = 0.489x + 6.7
- P-value: 0.7948
- N samples: 73

**Benchmark Score:**
- Correlation: 0.007 
- Linear fit: y = 0.007x + 6.9
- P-value: 0.9522
- N samples: 73

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.215 
- Linear fit: y = -3.757x + 21.6
- P-value: 0.0674
- N samples: 73

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Benchmark Score:**
- Correlation: -0.171 
- Linear fit: y = -0.221x + 27.2
- P-value: 0.1485
- N samples: 73

**Is Reasoning Model:**
- Correlation: -0.099 
- Linear fit: y = -2.185x + 21.6
- P-value: 0.4045
- N samples: 73

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.212 
- Linear fit: y = -1.503x + 3.2
- P-value: 0.0713
- N samples: 73

**Benchmark Score:**
- Correlation: 0.116 
- Linear fit: y = 0.061x + 0.5
- P-value: 0.3295
- N samples: 73

**Is Reasoning Model:**
- Correlation: 0.111 
- Linear fit: y = 0.998x + 1.7
- P-value: 0.3478
- N samples: 73

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Days Since 2024-01-01:**
- Correlation: 0.063 
- Linear fit: y = 0.002x + 1.1
- P-value: 0.6402
- N samples: 57

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.208 
- Linear fit: y = -0.040x + 1.9
- P-value: 0.0779
- N samples: 73

**Model Size (B):**
- Correlation: -0.185 
- Linear fit: y = -0.000x + 0.9
- P-value: 0.1684
- N samples: 57

**Is Open Source:**
- Correlation: 0.149 
- Linear fit: y = 0.393x + 0.4
- P-value: 0.2076
- N samples: 73

**Days Since 2024-01-01:**
- Correlation: -0.128 
- Linear fit: y = -0.001x + 1.9
- P-value: 0.3415
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.068 
- Linear fit: y = -0.226x + 0.8
- P-value: 0.5677
- N samples: 73

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.181 
- Linear fit: y = -0.076x + 4.0
- P-value: 0.1263
- N samples: 73

**Is Open Source:**
- Correlation: 0.174 
- Linear fit: y = 0.986x + 1.1
- P-value: 0.1417
- N samples: 73

**Model Size (B):**
- Correlation: -0.119 
- Linear fit: y = -0.000x + 1.9
- P-value: 0.3798
- N samples: 57

**Days Since 2024-01-01:**
- Correlation: -0.067 
- Linear fit: y = -0.002x + 3.1
- P-value: 0.6189
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.053 
- Linear fit: y = 0.379x + 1.2
- P-value: 0.6571
- N samples: 73

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.196 
- Linear fit: y = -0.051x + 2.3
- P-value: 0.0958
- N samples: 73

**Model Size (B):**
- Correlation: -0.193 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.1506
- N samples: 57

**Days Since 2024-01-01:**
- Correlation: -0.128 
- Linear fit: y = -0.002x + 2.3
- P-value: 0.3438
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.084 
- Linear fit: y = -0.369x + 0.9
- P-value: 0.4822
- N samples: 73

**Is Open Source:**
- Correlation: 0.051 
- Linear fit: y = 0.177x + 0.6
- P-value: 0.6701
- N samples: 73

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.094 
- Linear fit: y = -0.000x + 1.3
- P-value: 0.4845
- N samples: 57

**Is Open Source:**
- Correlation: -0.089 
- Linear fit: y = -0.234x + 1.3
- P-value: 0.4565
- N samples: 73

**Benchmark Score:**
- Correlation: 0.073 
- Linear fit: y = 0.014x + 0.7
- P-value: 0.5403
- N samples: 73

**Is Reasoning Model:**
- Correlation: 0.055 
- Linear fit: y = 0.183x + 1.1
- P-value: 0.6459
- N samples: 73

**Days Since 2024-01-01:**
- Correlation: 0.001 
- Linear fit: y = 0.000x + 1.2
- P-value: 0.9964
- N samples: 57

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.097 
- Linear fit: y = -1.117x + 5.9
- P-value: 0.4154
- N samples: 73

**Days Since 2024-01-01:**
- Correlation: -0.081 
- Linear fit: y = -0.004x + 8.7
- P-value: 0.5498
- N samples: 57

**Model Size (B):**
- Correlation: -0.079 
- Linear fit: y = -0.000x + 5.8
- P-value: 0.5604
- N samples: 57

**Benchmark Score:**
- Correlation: -0.057 
- Linear fit: y = -0.048x + 7.0
- P-value: 0.6335
- N samples: 73

**Is Reasoning Model:**
- Correlation: -0.011 
- Linear fit: y = -0.161x + 5.5
- P-value: 0.9262
- N samples: 73

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: 0.353 **
- Linear fit: y = 0.041x + -0.8
- P-value: 0.0022
- N samples: 73

**Is Open Source:**
- Correlation: -0.325 **
- Linear fit: y = -0.508x + 0.8
- P-value: 0.0051
- N samples: 73

**Model Size (B):**
- Correlation: 0.249 
- Linear fit: y = 0.000x + 0.3
- P-value: 0.0617
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.236 *
- Linear fit: y = 0.467x + 0.1
- P-value: 0.0441
- N samples: 73

**Days Since 2024-01-01:**
- Correlation: 0.131 
- Linear fit: y = 0.001x + -0.2
- P-value: 0.3322
- N samples: 57

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.212 
- Linear fit: y = -3.130x + 17.1
- P-value: 0.0722
- N samples: 73

**Days Since 2024-01-01:**
- Correlation: -0.176 
- Linear fit: y = -0.011x + 25.5
- P-value: 0.1905
- N samples: 57

**Benchmark Score:**
- Correlation: -0.162 
- Linear fit: y = -0.177x + 21.6
- P-value: 0.1715
- N samples: 73

**Is Reasoning Model:**
- Correlation: -0.059 
- Linear fit: y = -1.097x + 16.6
- P-value: 0.6219
- N samples: 73

**Model Size (B):**
- Correlation: -0.004 
- Linear fit: y = -0.000x + 16.2
- P-value: 0.9788
- N samples: 57

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.227 
- Linear fit: y = -0.004x + 8.0
- P-value: 0.0900
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.187 
- Linear fit: y = -1.105x + 5.1
- P-value: 0.1138
- N samples: 73

**Is Open Source:**
- Correlation: -0.140 
- Linear fit: y = -0.657x + 4.5
- P-value: 0.2367
- N samples: 73

**Benchmark Score:**
- Correlation: -0.121 
- Linear fit: y = -0.042x + 5.6
- P-value: 0.3090
- N samples: 73

**Model Size (B):**
- Correlation: -0.026 
- Linear fit: y = -0.000x + 4.3
- P-value: 0.8462
- N samples: 57

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.130 
- Linear fit: y = 0.030x + 0.0
- P-value: 0.2739
- N samples: 73

**Benchmark Score:**
- Correlation: -0.099 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.4045
- N samples: 73

**Days Since 2024-01-01:**
- Correlation: -0.084 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.5337
- N samples: 57

**Model Size (B):**
- Correlation: -0.068 
- Linear fit: y = -0.000x + 0.0
- P-value: 0.6137
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.057 
- Linear fit: y = 0.017x + -0.0
- P-value: 0.6295
- N samples: 73

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: 0.138 
- Linear fit: y = 0.738x + 0.1
- P-value: 0.2428
- N samples: 73

**Is Open Source:**
- Correlation: -0.110 
- Linear fit: y = -0.465x + 0.9
- P-value: 0.3533
- N samples: 73

**Benchmark Score:**
- Correlation: 0.103 
- Linear fit: y = 0.032x + -0.3
- P-value: 0.3865
- N samples: 73

**Model Size (B):**
- Correlation: 0.065 
- Linear fit: y = 0.000x + 0.5
- P-value: 0.6318
- N samples: 57

**Days Since 2024-01-01:**
- Correlation: 0.045 
- Linear fit: y = 0.001x + 0.1
- P-value: 0.7393
- N samples: 57

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.214 
- Linear fit: y = -0.973x + 2.1
- P-value: 0.0697
- N samples: 73

**Model Size (B):**
- Correlation: 0.116 
- Linear fit: y = 0.000x + 1.5
- P-value: 0.3908
- N samples: 57

**Benchmark Score:**
- Correlation: 0.096 
- Linear fit: y = 0.032x + 0.6
- P-value: 0.4206
- N samples: 73

**Days Since 2024-01-01:**
- Correlation: 0.068 
- Linear fit: y = 0.001x + 0.6
- P-value: 0.6164
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.055 
- Linear fit: y = 0.317x + 1.4
- P-value: 0.6437
- N samples: 73

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.085 
- Linear fit: y = -0.064x + 0.1
- P-value: 0.4736
- N samples: 73

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.6113
- N samples: 57

**Benchmark Score:**
- Correlation: -0.067 
- Linear fit: y = -0.004x + 0.2
- P-value: 0.5705
- N samples: 73

**Days Since 2024-01-01:**
- Correlation: -0.066 
- Linear fit: y = -0.000x + 0.3
- P-value: 0.6241
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.061 
- Linear fit: y = -0.058x + 0.1
- P-value: 0.6092
- N samples: 73

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**2c_false_citation vs Benchmark Score:**
  r = 0.353, y = 0.041x + -0.8

**2c_false_citation vs Is Open Source:**
  r = -0.325, y = -0.508x + 0.8


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
- Correlation: 0.410 ***
- Linear fit: y = 0.573x + 5.5

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.440 ***
- Linear fit: y = 0.859x + 17.5

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.378 ***
- Linear fit: y = 0.300x + 1.7

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.484 ***
- Linear fit: y = 0.675x + 15.1

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.618 ***
- Linear fit: y = 0.350x + 0.0

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.536 ***
- Linear fit: y = 0.217x + -1.8

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.972 ***, y = 0.898x + -1.0

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.972 ***, y = 0.823x + -0.7

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.834 ***, y = 0.530x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.804 ***, y = 0.518x + 0.4

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.737 ***, y = 0.439x + -0.4

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.716 ***, y = 0.211x + 0.0

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.663 ***, y = 0.259x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.649 ***, y = 0.174x + 0.7

**Category 2: Factual Errors vs 4b: Model Semantics Breach:**
  r = 0.635 ***, y = 0.232x + 0.0

**Category 2: Factual Errors vs Category 4: Technical Errors:**
  r = 0.618 ***, y = 0.350x + 0.0

**Category 2: Factual Errors vs 4c: Visual Descr Mismatch:**
  r = 0.605 ***, y = 0.037x + -0.2

**Category 3: Logical Errors vs 4b: Model Semantics Breach:**
  r = 0.588 ***, y = 0.154x + -1.4

**Category 4: Technical Errors vs 2b: Spurious Numeric:**
  r = 0.584 ***, y = 0.952x + 3.0

**2b: Spurious Numeric vs 4b: Model Semantics Breach:**
  r = 0.584 ***, y = 0.230x + 0.4

**3a: Unsupported Leap vs 4b: Model Semantics Breach:**
  r = 0.572 ***, y = 0.176x + -1.1

**2b: Spurious Numeric vs 4c: Visual Descr Mismatch:**
  r = 0.560 ***, y = 0.037x + -0.1

**Category 3: Logical Errors vs Category 4: Technical Errors:**
  r = 0.536 ***, y = 0.217x + -1.8

**Category 4: Technical Errors vs 3a: Unsupported Leap:**
  r = 0.501 ***, y = 1.046x + 13.0

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.485 ***, y = 0.574x + 11.6

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.484 ***, y = 0.675x + 15.1

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
