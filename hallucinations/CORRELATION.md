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
- Correlation: -0.240 
- Linear fit: y = -0.167x + 7.8
- P-value: 0.0747
- N samples: 56

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.133 
- Linear fit: y = -1.300x + 3.4
- P-value: 0.3285
- N samples: 56

**Days Since 2024-01-01:**
- Correlation: -0.046 
- Linear fit: y = -0.001x + 3.6
- P-value: 0.8464
- N samples: 20

**Is Open Source:**
- Correlation: 0.044 
- Linear fit: y = 0.387x + 2.3
- P-value: 0.7490
- N samples: 56

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.205 
- Linear fit: y = -0.002x + 8.5
- P-value: 0.4306
- N samples: 17

**Is Open Source:**
- Correlation: -0.180 
- Linear fit: y = -2.364x + 8.6
- P-value: 0.1835
- N samples: 56

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Benchmark Score:**
- Correlation: -0.016 
- Linear fit: y = -0.017x + 8.1
- P-value: 0.9053
- N samples: 56

**Is Reasoning Model:**
- Correlation: -0.003 
- Linear fit: y = -0.038x + 7.6
- P-value: 0.9849
- N samples: 56

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.411 
- Linear fit: y = -0.004x + 26.1
- P-value: 0.1010
- N samples: 17

**Is Open Source:**
- Correlation: -0.369 **
- Linear fit: y = -7.262x + 27.3
- P-value: 0.0052
- N samples: 56

**Is Reasoning Model:**
- Correlation: -0.310 *
- Linear fit: y = -6.750x + 28.8
- P-value: 0.0199
- N samples: 56

**Days Since 2024-01-01:**
- Correlation: -0.309 
- Linear fit: y = -0.012x + 33.8
- P-value: 0.1849
- N samples: 20

**Benchmark Score:**
- Correlation: -0.116 
- Linear fit: y = -0.179x + 29.7
- P-value: 0.3959
- N samples: 56

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.281 *
- Linear fit: y = -0.133x + 6.0
- P-value: 0.0356
- N samples: 56

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.058 
- Linear fit: y = -0.388x + 1.9
- P-value: 0.6694
- N samples: 56

**Is Open Source:**
- Correlation: -0.002 
- Linear fit: y = -0.013x + 1.7
- P-value: 0.9876
- N samples: 56

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
- Correlation: -0.236 
- Linear fit: y = -9.390x + 40.0
- P-value: 0.0806
- N samples: 56

**Is Reasoning Model:**
- Correlation: -0.191 
- Linear fit: y = -8.425x + 41.6
- P-value: 0.1576
- N samples: 56

**Benchmark Score:**
- Correlation: -0.154 
- Linear fit: y = -0.484x + 51.2
- P-value: 0.2570
- N samples: 56

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.240 
- Linear fit: y = -0.167x + 7.8
- P-value: 0.0747
- N samples: 56

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.133 
- Linear fit: y = -1.300x + 3.4
- P-value: 0.3285
- N samples: 56

**Days Since 2024-01-01:**
- Correlation: -0.046 
- Linear fit: y = -0.001x + 3.6
- P-value: 0.8464
- N samples: 20

**Is Open Source:**
- Correlation: 0.044 
- Linear fit: y = 0.387x + 2.3
- P-value: 0.7490
- N samples: 56

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.205 
- Linear fit: y = -0.002x + 8.5
- P-value: 0.4306
- N samples: 17

**Is Open Source:**
- Correlation: -0.180 
- Linear fit: y = -2.364x + 8.6
- P-value: 0.1835
- N samples: 56

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Benchmark Score:**
- Correlation: -0.016 
- Linear fit: y = -0.017x + 8.1
- P-value: 0.9053
- N samples: 56

**Is Reasoning Model:**
- Correlation: -0.003 
- Linear fit: y = -0.038x + 7.6
- P-value: 0.9849
- N samples: 56

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.411 
- Linear fit: y = -0.004x + 26.1
- P-value: 0.1010
- N samples: 17

**Is Open Source:**
- Correlation: -0.369 **
- Linear fit: y = -7.262x + 27.3
- P-value: 0.0052
- N samples: 56

**Is Reasoning Model:**
- Correlation: -0.310 *
- Linear fit: y = -6.750x + 28.8
- P-value: 0.0199
- N samples: 56

**Days Since 2024-01-01:**
- Correlation: -0.309 
- Linear fit: y = -0.012x + 33.8
- P-value: 0.1849
- N samples: 20

**Benchmark Score:**
- Correlation: -0.116 
- Linear fit: y = -0.179x + 29.7
- P-value: 0.3959
- N samples: 56

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.281 *
- Linear fit: y = -0.133x + 6.0
- P-value: 0.0356
- N samples: 56

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.058 
- Linear fit: y = -0.388x + 1.9
- P-value: 0.6694
- N samples: 56

**Is Open Source:**
- Correlation: -0.002 
- Linear fit: y = -0.013x + 1.7
- P-value: 0.9876
- N samples: 56

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.202 
- Linear fit: y = -0.900x + 1.5
- P-value: 0.1354
- N samples: 56

**Benchmark Score:**
- Correlation: -0.180 
- Linear fit: y = -0.057x + 2.7
- P-value: 0.1842
- N samples: 56

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

**Is Open Source:**
- Correlation: 0.048 
- Linear fit: y = 0.195x + 0.8
- P-value: 0.7238
- N samples: 56

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.211 
- Linear fit: y = -0.001x + 1.9
- P-value: 0.4158
- N samples: 17

**Benchmark Score:**
- Correlation: -0.202 
- Linear fit: y = -0.071x + 3.5
- P-value: 0.1361
- N samples: 56

**Days Since 2024-01-01:**
- Correlation: -0.080 
- Linear fit: y = -0.001x + 2.3
- P-value: 0.7365
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.028 
- Linear fit: y = -0.138x + 1.3
- P-value: 0.8382
- N samples: 56

**Is Open Source:**
- Correlation: 0.007 
- Linear fit: y = 0.031x + 1.2
- P-value: 0.9598
- N samples: 56

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.283 *
- Linear fit: y = -0.039x + 1.6
- P-value: 0.0343
- N samples: 56

**Is Reasoning Model:**
- Correlation: -0.135 
- Linear fit: y = -0.263x + 0.6
- P-value: 0.3207
- N samples: 56

**Days Since 2024-01-01:**
- Correlation: -0.099 
- Linear fit: y = -0.000x + 0.7
- P-value: 0.6765
- N samples: 20

**Is Open Source:**
- Correlation: 0.092 
- Linear fit: y = 0.162x + 0.3
- P-value: 0.5010
- N samples: 56

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
- Correlation: 0.209 
- Linear fit: y = 0.659x + 1.0
- P-value: 0.1223
- N samples: 56

**Benchmark Score:**
- Correlation: -0.138 
- Linear fit: y = -0.034x + 2.4
- P-value: 0.3098
- N samples: 56

**Is Reasoning Model:**
- Correlation: 0.086 
- Linear fit: y = 0.300x + 1.1
- P-value: 0.5278
- N samples: 56

**Days Since 2024-01-01:**
- Correlation: 0.021 
- Linear fit: y = 0.000x + 1.1
- P-value: 0.9297
- N samples: 20

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.248 
- Linear fit: y = -3.064x + 7.3
- P-value: 0.0655
- N samples: 56

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

**Is Reasoning Model:**
- Correlation: -0.028 
- Linear fit: y = -0.388x + 6.2
- P-value: 0.8354
- N samples: 56

**Benchmark Score:**
- Correlation: 0.003 
- Linear fit: y = 0.003x + 5.8
- P-value: 0.9833
- N samples: 56

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
- Correlation: 0.191 
- Linear fit: y = 0.015x + -0.2
- P-value: 0.1593
- N samples: 56

**Is Reasoning Model:**
- Correlation: 0.046 
- Linear fit: y = 0.050x + 0.2
- P-value: 0.7357
- N samples: 56

**Is Open Source:**
- Correlation: 0.042 
- Linear fit: y = 0.041x + 0.3
- P-value: 0.7598
- N samples: 56

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.402 **
- Linear fit: y = -6.177x + 22.6
- P-value: 0.0021
- N samples: 56

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
- Correlation: -0.275 *
- Linear fit: y = -4.663x + 23.1
- P-value: 0.0404
- N samples: 56

**Benchmark Score:**
- Correlation: -0.100 
- Linear fit: y = -0.121x + 23.6
- P-value: 0.4644
- N samples: 56

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.379 
- Linear fit: y = -0.001x + 4.4
- P-value: 0.1339
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.303 *
- Linear fit: y = -2.050x + 5.6
- P-value: 0.0230
- N samples: 56

**Days Since 2024-01-01:**
- Correlation: -0.187 
- Linear fit: y = -0.003x + 5.8
- P-value: 0.4300
- N samples: 20

**Is Open Source:**
- Correlation: -0.178 
- Linear fit: y = -1.090x + 4.7
- P-value: 0.1891
- N samples: 56

**Benchmark Score:**
- Correlation: -0.114 
- Linear fit: y = -0.055x + 5.9
- P-value: 0.4047
- N samples: 56

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.170 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.5133
- N samples: 17

**Benchmark Score:**
- Correlation: -0.137 
- Linear fit: y = -0.004x + 0.2
- P-value: 0.3130
- N samples: 56

**Days Since 2024-01-01:**
- Correlation: 0.100 
- Linear fit: y = 0.000x + -0.1
- P-value: 0.6745
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.091 
- Linear fit: y = -0.038x + 0.1
- P-value: 0.5034
- N samples: 56

**Is Open Source:**
- Correlation: 0.014 
- Linear fit: y = 0.005x + 0.0
- P-value: 0.9197
- N samples: 56

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.487 *
- Linear fit: y = -0.007x + 6.3
- P-value: 0.0296
- N samples: 20

**Benchmark Score:**
- Correlation: -0.149 
- Linear fit: y = -0.033x + 1.5
- P-value: 0.2743
- N samples: 56

**Is Open Source:**
- Correlation: -0.092 
- Linear fit: y = -0.264x + 0.5
- P-value: 0.4978
- N samples: 56

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.8201
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.040 
- Linear fit: y = -0.125x + 0.5
- P-value: 0.7717
- N samples: 56

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
- P-value: 0.0318
- N samples: 56

**Model Size (B):**
- Correlation: -0.134 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.6083
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.047 
- Linear fit: y = -0.225x + 1.4
- P-value: 0.7296
- N samples: 56

**Is Open Source:**
- Correlation: 0.040 
- Linear fit: y = 0.174x + 1.1
- P-value: 0.7675
- N samples: 56

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.357 
- Linear fit: y = 0.000x + 0.0
- P-value: 0.1590
- N samples: 17

**Is Open Source:**
- Correlation: 0.207 
- Linear fit: y = 0.077x + 0.0
- P-value: 0.1263
- N samples: 56

**Is Reasoning Model:**
- Correlation: -0.091 
- Linear fit: y = -0.038x + 0.1
- P-value: 0.5034
- N samples: 56

**Benchmark Score:**
- Correlation: -0.080 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.5601
- N samples: 56

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
  r = -0.402, y = -6.177x + 22.6

**category3_logical_errors vs Is Open Source:**
  r = -0.369, y = -7.262x + 27.3

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.310, y = -6.750x + 28.8

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.303, y = -2.050x + 5.6


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
- Linear fit: y = 0.982x + 5.1

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.574 ***
- Linear fit: y = 1.277x + 20.8

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.467 ***
- Linear fit: y = 0.317x + 0.9

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.622 ***
- Linear fit: y = 0.934x + 16.9

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.484 ***
- Linear fit: y = 0.222x + -0.0

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.423 **
- Linear fit: y = 0.129x + -1.4

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.968 ***, y = 0.755x + 1.7

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.967 ***, y = 0.912x + -1.0

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.924 ***, y = 0.466x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.893 ***, y = 0.640x + 0.2

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.857 ***, y = 0.391x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.787 ***, y = 0.244x + -1.7

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.755 ***, y = 0.358x + -0.2

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.722 ***, y = 0.143x + 0.0

**1a: Instruction Override vs 3b: Self Contradiction:**
  r = 0.704 ***, y = 1.068x + 3.2

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = 0.663 ***, y = 0.982x + 5.1

**1b: Context Omission vs 1c: Prompt Contradiction:**
  r = 0.663 ***, y = 0.261x + 0.1

**Category 2: Factual Errors vs 1a: Instruction Override:**
  r = 0.663 ***, y = 0.204x + -0.7

**Category 1: Input Misalignment vs 2b: Spurious Numeric:**
  r = 0.657 ***, y = 0.917x + 3.7

**Category 1: Input Misalignment vs 3b: Self Contradiction:**
  r = 0.652 ***, y = 0.451x + 3.1

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = 0.649 ***, y = 0.221x + -0.4

**1a: Instruction Override vs 2b: Spurious Numeric:**
  r = 0.645 ***, y = 1.976x + 4.2

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.645 ***, y = 0.405x + -3.8

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = 0.638 ***, y = 1.766x + 3.8

**1a: Instruction Override vs 1b: Context Omission:**
  r = 0.633 ***, y = 0.700x + 0.6

**Category 3: Logical Errors vs 1a: Instruction Override:**
  r = 0.623 ***, y = 0.128x + -2.2

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
