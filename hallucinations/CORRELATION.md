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
- Correlation: -0.222 
- Linear fit: y = -0.156x + 7.6
- P-value: 0.1220
- N samples: 50

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.123 
- Linear fit: y = -1.266x + 3.6
- P-value: 0.3938
- N samples: 50

**Days Since 2024-01-01:**
- Correlation: -0.046 
- Linear fit: y = -0.001x + 3.6
- P-value: 0.8464
- N samples: 20

**Is Open Source:**
- Correlation: 0.045 
- Linear fit: y = 0.413x + 2.5
- P-value: 0.7574
- N samples: 50

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.205 
- Linear fit: y = -0.002x + 8.5
- P-value: 0.4306
- N samples: 17

**Is Open Source:**
- Correlation: -0.203 
- Linear fit: y = -2.740x + 9.1
- P-value: 0.1577
- N samples: 50

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Is Reasoning Model:**
- Correlation: 0.028 
- Linear fit: y = 0.417x + 7.5
- P-value: 0.8485
- N samples: 50

**Benchmark Score:**
- Correlation: 0.010 
- Linear fit: y = 0.011x + 7.5
- P-value: 0.9432
- N samples: 50

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.411 
- Linear fit: y = -0.004x + 26.1
- P-value: 0.1010
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: -0.309 
- Linear fit: y = -0.012x + 33.8
- P-value: 0.1849
- N samples: 20

**Is Open Source:**
- Correlation: -0.305 *
- Linear fit: y = -5.926x + 26.4
- P-value: 0.0313
- N samples: 50

**Is Reasoning Model:**
- Correlation: -0.254 
- Linear fit: y = -5.500x + 27.5
- P-value: 0.0747
- N samples: 50

**Benchmark Score:**
- Correlation: -0.175 
- Linear fit: y = -0.260x + 31.8
- P-value: 0.2228
- N samples: 50

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.271 
- Linear fit: y = -0.130x + 5.9
- P-value: 0.0567
- N samples: 50

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.030 
- Linear fit: y = -0.206x + 1.9
- P-value: 0.8384
- N samples: 50

**Is Open Source:**
- Correlation: 0.004 
- Linear fit: y = 0.022x + 1.8
- P-value: 0.9803
- N samples: 50

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
- Correlation: -0.204 
- Linear fit: y = -8.388x + 39.8
- P-value: 0.1549
- N samples: 50

**Benchmark Score:**
- Correlation: -0.166 
- Linear fit: y = -0.522x + 52.4
- P-value: 0.2479
- N samples: 50

**Is Reasoning Model:**
- Correlation: -0.142 
- Linear fit: y = -6.500x + 40.5
- P-value: 0.3246
- N samples: 50

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.222 
- Linear fit: y = -0.156x + 7.6
- P-value: 0.1220
- N samples: 50

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.123 
- Linear fit: y = -1.266x + 3.6
- P-value: 0.3938
- N samples: 50

**Days Since 2024-01-01:**
- Correlation: -0.046 
- Linear fit: y = -0.001x + 3.6
- P-value: 0.8464
- N samples: 20

**Is Open Source:**
- Correlation: 0.045 
- Linear fit: y = 0.413x + 2.5
- P-value: 0.7574
- N samples: 50

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.205 
- Linear fit: y = -0.002x + 8.5
- P-value: 0.4306
- N samples: 17

**Is Open Source:**
- Correlation: -0.203 
- Linear fit: y = -2.740x + 9.1
- P-value: 0.1577
- N samples: 50

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Is Reasoning Model:**
- Correlation: 0.028 
- Linear fit: y = 0.417x + 7.5
- P-value: 0.8485
- N samples: 50

**Benchmark Score:**
- Correlation: 0.010 
- Linear fit: y = 0.011x + 7.5
- P-value: 0.9432
- N samples: 50

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.411 
- Linear fit: y = -0.004x + 26.1
- P-value: 0.1010
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: -0.309 
- Linear fit: y = -0.012x + 33.8
- P-value: 0.1849
- N samples: 20

**Is Open Source:**
- Correlation: -0.305 *
- Linear fit: y = -5.926x + 26.4
- P-value: 0.0313
- N samples: 50

**Is Reasoning Model:**
- Correlation: -0.254 
- Linear fit: y = -5.500x + 27.5
- P-value: 0.0747
- N samples: 50

**Benchmark Score:**
- Correlation: -0.175 
- Linear fit: y = -0.260x + 31.8
- P-value: 0.2228
- N samples: 50

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.271 
- Linear fit: y = -0.130x + 5.9
- P-value: 0.0567
- N samples: 50

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.030 
- Linear fit: y = -0.206x + 1.9
- P-value: 0.8384
- N samples: 50

**Is Open Source:**
- Correlation: 0.004 
- Linear fit: y = 0.022x + 1.8
- P-value: 0.9803
- N samples: 50

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.179 
- Linear fit: y = -0.833x + 1.5
- P-value: 0.2136
- N samples: 50

**Benchmark Score:**
- Correlation: -0.175 
- Linear fit: y = -0.056x + 2.7
- P-value: 0.2240
- N samples: 50

**Is Open Source:**
- Correlation: 0.065 
- Linear fit: y = 0.272x + 0.8
- P-value: 0.6533
- N samples: 50

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.8198
- N samples: 17

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
- Correlation: -0.173 
- Linear fit: y = -0.061x + 3.3
- P-value: 0.2301
- N samples: 50

**Days Since 2024-01-01:**
- Correlation: -0.080 
- Linear fit: y = -0.001x + 2.3
- P-value: 0.7365
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.038 
- Linear fit: y = -0.194x + 1.5
- P-value: 0.7947
- N samples: 50

**Is Open Source:**
- Correlation: -0.011 
- Linear fit: y = -0.051x + 1.4
- P-value: 0.9391
- N samples: 50

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.279 *
- Linear fit: y = -0.039x + 1.6
- P-value: 0.0495
- N samples: 50

**Is Reasoning Model:**
- Correlation: -0.117 
- Linear fit: y = -0.238x + 0.6
- P-value: 0.4198
- N samples: 50

**Is Open Source:**
- Correlation: 0.105 
- Linear fit: y = 0.192x + 0.3
- P-value: 0.4688
- N samples: 50

**Days Since 2024-01-01:**
- Correlation: -0.099 
- Linear fit: y = -0.000x + 0.7
- P-value: 0.6765
- N samples: 20

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
- Correlation: 0.206 
- Linear fit: y = 0.663x + 1.0
- P-value: 0.1522
- N samples: 50

**Benchmark Score:**
- Correlation: -0.159 
- Linear fit: y = -0.039x + 2.5
- P-value: 0.2712
- N samples: 50

**Is Reasoning Model:**
- Correlation: 0.081 
- Linear fit: y = 0.290x + 1.1
- P-value: 0.5777
- N samples: 50

**Days Since 2024-01-01:**
- Correlation: 0.021 
- Linear fit: y = 0.000x + 1.1
- P-value: 0.9297
- N samples: 20

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.267 
- Linear fit: y = -3.385x + 7.9
- P-value: 0.0610
- N samples: 50

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
- Correlation: 0.036 
- Linear fit: y = 0.035x + 5.2
- P-value: 0.8055
- N samples: 50

**Is Reasoning Model:**
- Correlation: 0.004 
- Linear fit: y = 0.063x + 6.2
- P-value: 0.9753
- N samples: 50

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
- Correlation: 0.226 
- Linear fit: y = 0.015x + -0.2
- P-value: 0.1140
- N samples: 50

**Is Reasoning Model:**
- Correlation: 0.065 
- Linear fit: y = 0.063x + 0.2
- P-value: 0.6539
- N samples: 50

**Is Open Source:**
- Correlation: -0.022 
- Linear fit: y = -0.019x + 0.3
- P-value: 0.8800
- N samples: 50

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.337 *
- Linear fit: y = -5.058x + 21.8
- P-value: 0.0168
- N samples: 50

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
- Correlation: -0.212 
- Linear fit: y = -3.540x + 21.9
- P-value: 0.1400
- N samples: 50

**Benchmark Score:**
- Correlation: -0.168 
- Linear fit: y = -0.192x + 25.5
- P-value: 0.2440
- N samples: 50

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.379 
- Linear fit: y = -0.001x + 4.4
- P-value: 0.1339
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.279 
- Linear fit: y = -1.917x + 5.5
- P-value: 0.0501
- N samples: 50

**Days Since 2024-01-01:**
- Correlation: -0.187 
- Linear fit: y = -0.003x + 5.8
- P-value: 0.4300
- N samples: 20

**Is Open Source:**
- Correlation: -0.141 
- Linear fit: y = -0.872x + 4.5
- P-value: 0.3288
- N samples: 50

**Benchmark Score:**
- Correlation: -0.136 
- Linear fit: y = -0.064x + 6.2
- P-value: 0.3473
- N samples: 50

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.170 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.5133
- N samples: 17

**Benchmark Score:**
- Correlation: -0.127 
- Linear fit: y = -0.004x + 0.2
- P-value: 0.3793
- N samples: 50

**Days Since 2024-01-01:**
- Correlation: 0.100 
- Linear fit: y = 0.000x + -0.1
- P-value: 0.6745
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.100 
- Linear fit: y = -0.044x + 0.1
- P-value: 0.4895
- N samples: 50

**Is Open Source:**
- Correlation: 0.008 
- Linear fit: y = 0.003x + 0.0
- P-value: 0.9551
- N samples: 50

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.487 *
- Linear fit: y = -0.007x + 6.3
- P-value: 0.0296
- N samples: 20

**Benchmark Score:**
- Correlation: -0.133 
- Linear fit: y = -0.031x + 1.4
- P-value: 0.3558
- N samples: 50

**Is Open Source:**
- Correlation: -0.108 
- Linear fit: y = -0.324x + 0.6
- P-value: 0.4559
- N samples: 50

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.8201
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.046 
- Linear fit: y = -0.155x + 0.6
- P-value: 0.7493
- N samples: 50

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.352 
- Linear fit: y = -0.004x + 4.0
- P-value: 0.1282
- N samples: 20

**Benchmark Score:**
- Correlation: -0.285 *
- Linear fit: y = -0.097x + 4.4
- P-value: 0.0451
- N samples: 50

**Model Size (B):**
- Correlation: -0.134 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.6083
- N samples: 17

**Is Open Source:**
- Correlation: 0.059 
- Linear fit: y = 0.263x + 1.2
- P-value: 0.6855
- N samples: 50

**Is Reasoning Model:**
- Correlation: -0.002 
- Linear fit: y = -0.008x + 1.3
- P-value: 0.9912
- N samples: 50

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.357 
- Linear fit: y = 0.000x + 0.0
- P-value: 0.1590
- N samples: 17

**Is Open Source:**
- Correlation: 0.212 
- Linear fit: y = 0.083x + 0.0
- P-value: 0.1385
- N samples: 50

**Is Reasoning Model:**
- Correlation: -0.100 
- Linear fit: y = -0.044x + 0.1
- P-value: 0.4895
- N samples: 50

**Benchmark Score:**
- Correlation: -0.068 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.6399
- N samples: 50

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
  r = -0.337, y = -5.058x + 21.8

**category3_logical_errors vs Is Open Source:**
  r = -0.305, y = -5.926x + 26.4


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
- Correlation: 0.659 ***
- Linear fit: y = 0.965x + 5.2

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.621 ***
- Linear fit: y = 1.308x + 20.1

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.453 ***
- Linear fit: y = 0.308x + 1.0

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.686 ***
- Linear fit: y = 0.987x + 15.8

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.470 ***
- Linear fit: y = 0.218x + 0.1

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.446 **
- Linear fit: y = 0.144x + -1.6

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.968 ***, y = 0.909x + -0.8

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.967 ***, y = 0.747x + 1.8

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.926 ***, y = 0.465x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.891 ***, y = 0.636x + 0.1

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.862 ***, y = 0.391x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.792 ***, y = 0.252x + -1.8

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.758 ***, y = 0.363x + -0.2

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.728 ***, y = 0.145x + 0.0

**1a: Instruction Override vs 3b: Self Contradiction:**
  r = 0.711 ***, y = 1.051x + 3.2

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.706 ***, y = 0.460x + -4.6

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.686 ***, y = 0.987x + 15.8

**Category 1: Input Misalignment vs 3b: Self Contradiction:**
  r = 0.678 ***, y = 0.454x + 2.9

**2b: Spurious Numeric vs 3a: Unsupported Leap:**
  r = 0.675 ***, y = 0.799x + 14.4

**1b: Context Omission vs 1c: Prompt Contradiction:**
  r = 0.668 ***, y = 0.265x + 0.0

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = 0.659 ***, y = 0.965x + 5.2

**Category 3: Logical Errors vs 1a: Instruction Override:**
  r = 0.656 ***, y = 0.141x + -2.4

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.656 ***, y = 0.729x + 13.7

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = 0.654 ***, y = 0.224x + -0.4

**Category 2: Factual Errors vs 1a: Instruction Override:**
  r = 0.652 ***, y = 0.202x + -0.7

**Category 1: Input Misalignment vs 2b: Spurious Numeric:**
  r = 0.648 ***, y = 0.890x + 3.9

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
