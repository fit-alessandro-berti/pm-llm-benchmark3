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
- Correlation: -0.224 
- Linear fit: y = -0.158x + 7.7
- P-value: 0.1134
- N samples: 51

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.129 
- Linear fit: y = -1.328x + 3.6
- P-value: 0.3655
- N samples: 51

**Days Since 2024-01-01:**
- Correlation: -0.046 
- Linear fit: y = -0.001x + 3.6
- P-value: 0.8464
- N samples: 20

**Is Open Source:**
- Correlation: 0.033 
- Linear fit: y = 0.298x + 2.5
- P-value: 0.8205
- N samples: 51

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.209 
- Linear fit: y = -2.795x + 9.1
- P-value: 0.1416
- N samples: 51

**Model Size (B):**
- Correlation: -0.205 
- Linear fit: y = -0.002x + 8.5
- P-value: 0.4306
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Is Reasoning Model:**
- Correlation: 0.023 
- Linear fit: y = 0.338x + 7.5
- P-value: 0.8754
- N samples: 51

**Benchmark Score:**
- Correlation: 0.009 
- Linear fit: y = 0.010x + 7.4
- P-value: 0.9476
- N samples: 51

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.411 
- Linear fit: y = -0.004x + 26.1
- P-value: 0.1010
- N samples: 17

**Is Open Source:**
- Correlation: -0.320 *
- Linear fit: y = -6.223x + 26.4
- P-value: 0.0222
- N samples: 51

**Days Since 2024-01-01:**
- Correlation: -0.309 
- Linear fit: y = -0.012x + 33.8
- P-value: 0.1849
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.261 
- Linear fit: y = -5.689x + 27.5
- P-value: 0.0645
- N samples: 51

**Benchmark Score:**
- Correlation: -0.176 
- Linear fit: y = -0.264x + 31.8
- P-value: 0.2168
- N samples: 51

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.272 
- Linear fit: y = -0.130x + 5.9
- P-value: 0.0533
- N samples: 51

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.036 
- Linear fit: y = -0.253x + 1.9
- P-value: 0.8005
- N samples: 51

**Is Open Source:**
- Correlation: -0.008 
- Linear fit: y = -0.049x + 1.8
- P-value: 0.9561
- N samples: 51

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
- Correlation: -0.218 
- Linear fit: y = -8.925x + 39.9
- P-value: 0.1243
- N samples: 51

**Benchmark Score:**
- Correlation: -0.168 
- Linear fit: y = -0.528x + 52.3
- P-value: 0.2395
- N samples: 51

**Is Reasoning Model:**
- Correlation: -0.150 
- Linear fit: y = -6.878x + 40.5
- P-value: 0.2934
- N samples: 51

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.224 
- Linear fit: y = -0.158x + 7.7
- P-value: 0.1134
- N samples: 51

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.129 
- Linear fit: y = -1.328x + 3.6
- P-value: 0.3655
- N samples: 51

**Days Since 2024-01-01:**
- Correlation: -0.046 
- Linear fit: y = -0.001x + 3.6
- P-value: 0.8464
- N samples: 20

**Is Open Source:**
- Correlation: 0.033 
- Linear fit: y = 0.298x + 2.5
- P-value: 0.8205
- N samples: 51

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.209 
- Linear fit: y = -2.795x + 9.1
- P-value: 0.1416
- N samples: 51

**Model Size (B):**
- Correlation: -0.205 
- Linear fit: y = -0.002x + 8.5
- P-value: 0.4306
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Is Reasoning Model:**
- Correlation: 0.023 
- Linear fit: y = 0.338x + 7.5
- P-value: 0.8754
- N samples: 51

**Benchmark Score:**
- Correlation: 0.009 
- Linear fit: y = 0.010x + 7.4
- P-value: 0.9476
- N samples: 51

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.411 
- Linear fit: y = -0.004x + 26.1
- P-value: 0.1010
- N samples: 17

**Is Open Source:**
- Correlation: -0.320 *
- Linear fit: y = -6.223x + 26.4
- P-value: 0.0222
- N samples: 51

**Days Since 2024-01-01:**
- Correlation: -0.309 
- Linear fit: y = -0.012x + 33.8
- P-value: 0.1849
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.261 
- Linear fit: y = -5.689x + 27.5
- P-value: 0.0645
- N samples: 51

**Benchmark Score:**
- Correlation: -0.176 
- Linear fit: y = -0.264x + 31.8
- P-value: 0.2168
- N samples: 51

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.272 
- Linear fit: y = -0.130x + 5.9
- P-value: 0.0533
- N samples: 51

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.036 
- Linear fit: y = -0.253x + 1.9
- P-value: 0.8005
- N samples: 51

**Is Open Source:**
- Correlation: -0.008 
- Linear fit: y = -0.049x + 1.8
- P-value: 0.9561
- N samples: 51

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.183 
- Linear fit: y = -0.851x + 1.5
- P-value: 0.1981
- N samples: 51

**Benchmark Score:**
- Correlation: -0.177 
- Linear fit: y = -0.057x + 2.7
- P-value: 0.2138
- N samples: 51

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.8198
- N samples: 17

**Is Open Source:**
- Correlation: 0.056 
- Linear fit: y = 0.231x + 0.8
- P-value: 0.6982
- N samples: 51

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
- Correlation: -0.176 
- Linear fit: y = -0.062x + 3.3
- P-value: 0.2176
- N samples: 51

**Days Since 2024-01-01:**
- Correlation: -0.080 
- Linear fit: y = -0.001x + 2.3
- P-value: 0.7365
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.045 
- Linear fit: y = -0.230x + 1.5
- P-value: 0.7559
- N samples: 51

**Is Open Source:**
- Correlation: -0.023 
- Linear fit: y = -0.105x + 1.4
- P-value: 0.8741
- N samples: 51

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.283 *
- Linear fit: y = -0.040x + 1.7
- P-value: 0.0445
- N samples: 51

**Is Reasoning Model:**
- Correlation: -0.121 
- Linear fit: y = -0.247x + 0.6
- P-value: 0.3965
- N samples: 51

**Days Since 2024-01-01:**
- Correlation: -0.099 
- Linear fit: y = -0.000x + 0.7
- P-value: 0.6765
- N samples: 20

**Is Open Source:**
- Correlation: 0.095 
- Linear fit: y = 0.172x + 0.3
- P-value: 0.5084
- N samples: 51

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
- Correlation: 0.231 
- Linear fit: y = 0.758x + 1.0
- P-value: 0.1028
- N samples: 51

**Benchmark Score:**
- Correlation: -0.144 
- Linear fit: y = -0.036x + 2.5
- P-value: 0.3148
- N samples: 51

**Is Reasoning Model:**
- Correlation: 0.098 
- Linear fit: y = 0.361x + 1.1
- P-value: 0.4931
- N samples: 51

**Days Since 2024-01-01:**
- Correlation: 0.021 
- Linear fit: y = 0.000x + 1.1
- P-value: 0.9297
- N samples: 20

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.279 *
- Linear fit: y = -3.525x + 7.9
- P-value: 0.0474
- N samples: 51

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
- Correlation: 0.032 
- Linear fit: y = 0.031x + 5.2
- P-value: 0.8240
- N samples: 51

**Is Reasoning Model:**
- Correlation: -0.006 
- Linear fit: y = -0.079x + 6.2
- P-value: 0.9689
- N samples: 51

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
- Correlation: 0.223 
- Linear fit: y = 0.015x + -0.2
- P-value: 0.1162
- N samples: 51

**Is Reasoning Model:**
- Correlation: 0.057 
- Linear fit: y = 0.056x + 0.2
- P-value: 0.6895
- N samples: 51

**Is Open Source:**
- Correlation: -0.034 
- Linear fit: y = -0.029x + 0.3
- P-value: 0.8153
- N samples: 51

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.353 *
- Linear fit: y = -5.328x + 21.8
- P-value: 0.0111
- N samples: 51

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
- Correlation: -0.223 
- Linear fit: y = -3.766x + 21.9
- P-value: 0.1162
- N samples: 51

**Benchmark Score:**
- Correlation: -0.169 
- Linear fit: y = -0.196x + 25.4
- P-value: 0.2364
- N samples: 51

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.379 
- Linear fit: y = -0.001x + 4.4
- P-value: 0.1339
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.273 
- Linear fit: y = -1.878x + 5.5
- P-value: 0.0524
- N samples: 51

**Days Since 2024-01-01:**
- Correlation: -0.187 
- Linear fit: y = -0.003x + 5.8
- P-value: 0.4300
- N samples: 20

**Is Open Source:**
- Correlation: -0.146 
- Linear fit: y = -0.897x + 4.6
- P-value: 0.3062
- N samples: 51

**Benchmark Score:**
- Correlation: -0.135 
- Linear fit: y = -0.064x + 6.2
- P-value: 0.3450
- N samples: 51

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.170 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.5133
- N samples: 17

**Benchmark Score:**
- Correlation: -0.129 
- Linear fit: y = -0.004x + 0.2
- P-value: 0.3677
- N samples: 51

**Is Reasoning Model:**
- Correlation: -0.102 
- Linear fit: y = -0.044x + 0.1
- P-value: 0.4760
- N samples: 51

**Days Since 2024-01-01:**
- Correlation: 0.100 
- Linear fit: y = 0.000x + -0.1
- P-value: 0.6745
- N samples: 20

**Is Open Source:**
- Correlation: 0.004 
- Linear fit: y = 0.002x + 0.0
- P-value: 0.9780
- N samples: 51

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.487 *
- Linear fit: y = -0.007x + 6.3
- P-value: 0.0296
- N samples: 20

**Benchmark Score:**
- Correlation: -0.135 
- Linear fit: y = -0.031x + 1.4
- P-value: 0.3452
- N samples: 51

**Is Open Source:**
- Correlation: -0.113 
- Linear fit: y = -0.335x + 0.6
- P-value: 0.4305
- N samples: 51

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.8201
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.050 
- Linear fit: y = -0.166x + 0.6
- P-value: 0.7283
- N samples: 51

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
- P-value: 0.0427
- N samples: 51

**Model Size (B):**
- Correlation: -0.134 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.6083
- N samples: 17

**Is Open Source:**
- Correlation: 0.046 
- Linear fit: y = 0.206x + 1.2
- P-value: 0.7465
- N samples: 51

**Is Reasoning Model:**
- Correlation: -0.009 
- Linear fit: y = -0.042x + 1.3
- P-value: 0.9526
- N samples: 51

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.357 
- Linear fit: y = 0.000x + 0.0
- P-value: 0.1590
- N samples: 17

**Is Open Source:**
- Correlation: 0.206 
- Linear fit: y = 0.080x + 0.0
- P-value: 0.1469
- N samples: 51

**Is Reasoning Model:**
- Correlation: -0.102 
- Linear fit: y = -0.044x + 0.1
- P-value: 0.4760
- N samples: 51

**Benchmark Score:**
- Correlation: -0.070 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.6267
- N samples: 51

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
  r = -0.353, y = -5.328x + 21.8

**category3_logical_errors vs Is Open Source:**
  r = -0.320, y = -6.223x + 26.4


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
- Correlation: 0.660 ***
- Linear fit: y = 0.965x + 5.2

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.622 ***
- Linear fit: y = 1.321x + 19.9

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.457 ***
- Linear fit: y = 0.310x + 0.9

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.684 ***
- Linear fit: y = 0.994x + 15.7

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.472 ***
- Linear fit: y = 0.219x + 0.0

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.449 ***
- Linear fit: y = 0.143x + -1.6

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.967 ***, y = 0.750x + 1.7

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.967 ***, y = 0.912x + -0.9

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.927 ***, y = 0.465x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.892 ***, y = 0.637x + 0.1

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.862 ***, y = 0.390x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.791 ***, y = 0.249x + -1.7

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.759 ***, y = 0.362x + -0.2

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.729 ***, y = 0.145x + 0.0

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.707 ***, y = 0.459x + -4.6

**1a: Instruction Override vs 3b: Self Contradiction:**
  r = 0.705 ***, y = 1.043x + 3.2

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.684 ***, y = 0.994x + 15.7

**2b: Spurious Numeric vs 3a: Unsupported Leap:**
  r = 0.680 ***, y = 0.813x + 14.2

**Category 1: Input Misalignment vs 3b: Self Contradiction:**
  r = 0.671 ***, y = 0.449x + 3.0

**1b: Context Omission vs 1c: Prompt Contradiction:**
  r = 0.669 ***, y = 0.265x + 0.0

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = 0.660 ***, y = 0.965x + 5.2

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = 0.656 ***, y = 0.225x + -0.4

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.655 ***, y = 0.738x + 13.5

**Category 3: Logical Errors vs 1a: Instruction Override:**
  r = 0.654 ***, y = 0.139x + -2.4

**Category 2: Factual Errors vs 1a: Instruction Override:**
  r = 0.653 ***, y = 0.202x + -0.7

**Category 1: Input Misalignment vs 2b: Spurious Numeric:**
  r = 0.651 ***, y = 0.897x + 3.8

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
