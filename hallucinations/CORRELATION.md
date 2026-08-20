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
- Correlation: -0.242 
- Linear fit: y = -0.169x + 7.9
- P-value: 0.0752
- N samples: 55

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.132 
- Linear fit: y = -1.325x + 3.4
- P-value: 0.3350
- N samples: 55

**Days Since 2024-01-01:**
- Correlation: -0.046 
- Linear fit: y = -0.001x + 3.6
- P-value: 0.8464
- N samples: 20

**Is Open Source:**
- Correlation: 0.046 
- Linear fit: y = 0.412x + 2.2
- P-value: 0.7375
- N samples: 55

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.205 
- Linear fit: y = -0.002x + 8.5
- P-value: 0.4306
- N samples: 17

**Is Open Source:**
- Correlation: -0.169 
- Linear fit: y = -2.214x + 8.5
- P-value: 0.2186
- N samples: 55

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Benchmark Score:**
- Correlation: -0.024 
- Linear fit: y = -0.025x + 8.2
- P-value: 0.8592
- N samples: 55

**Is Reasoning Model:**
- Correlation: 0.022 
- Linear fit: y = 0.325x + 7.2
- P-value: 0.8729
- N samples: 55

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.411 
- Linear fit: y = -0.004x + 26.1
- P-value: 0.1010
- N samples: 17

**Is Open Source:**
- Correlation: -0.354 **
- Linear fit: y = -6.893x + 26.9
- P-value: 0.0081
- N samples: 55

**Days Since 2024-01-01:**
- Correlation: -0.309 
- Linear fit: y = -0.012x + 33.8
- P-value: 0.1849
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.281 *
- Linear fit: y = -6.133x + 28.1
- P-value: 0.0378
- N samples: 55

**Benchmark Score:**
- Correlation: -0.132 
- Linear fit: y = -0.202x + 30.2
- P-value: 0.3360
- N samples: 55

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.287 *
- Linear fit: y = -0.136x + 6.0
- P-value: 0.0337
- N samples: 55

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.047 
- Linear fit: y = -0.317x + 1.9
- P-value: 0.7352
- N samples: 55

**Is Open Source:**
- Correlation: 0.005 
- Linear fit: y = 0.033x + 1.6
- P-value: 0.9684
- N samples: 55

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
- Correlation: -0.221 
- Linear fit: y = -8.802x + 39.4
- P-value: 0.1043
- N samples: 55

**Benchmark Score:**
- Correlation: -0.167 
- Linear fit: y = -0.518x + 51.9
- P-value: 0.2244
- N samples: 55

**Is Reasoning Model:**
- Correlation: -0.166 
- Linear fit: y = -7.400x + 40.6
- P-value: 0.2257
- N samples: 55

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.242 
- Linear fit: y = -0.169x + 7.9
- P-value: 0.0752
- N samples: 55

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.132 
- Linear fit: y = -1.325x + 3.4
- P-value: 0.3350
- N samples: 55

**Days Since 2024-01-01:**
- Correlation: -0.046 
- Linear fit: y = -0.001x + 3.6
- P-value: 0.8464
- N samples: 20

**Is Open Source:**
- Correlation: 0.046 
- Linear fit: y = 0.412x + 2.2
- P-value: 0.7375
- N samples: 55

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.205 
- Linear fit: y = -0.002x + 8.5
- P-value: 0.4306
- N samples: 17

**Is Open Source:**
- Correlation: -0.169 
- Linear fit: y = -2.214x + 8.5
- P-value: 0.2186
- N samples: 55

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Benchmark Score:**
- Correlation: -0.024 
- Linear fit: y = -0.025x + 8.2
- P-value: 0.8592
- N samples: 55

**Is Reasoning Model:**
- Correlation: 0.022 
- Linear fit: y = 0.325x + 7.2
- P-value: 0.8729
- N samples: 55

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.411 
- Linear fit: y = -0.004x + 26.1
- P-value: 0.1010
- N samples: 17

**Is Open Source:**
- Correlation: -0.354 **
- Linear fit: y = -6.893x + 26.9
- P-value: 0.0081
- N samples: 55

**Days Since 2024-01-01:**
- Correlation: -0.309 
- Linear fit: y = -0.012x + 33.8
- P-value: 0.1849
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.281 *
- Linear fit: y = -6.133x + 28.1
- P-value: 0.0378
- N samples: 55

**Benchmark Score:**
- Correlation: -0.132 
- Linear fit: y = -0.202x + 30.2
- P-value: 0.3360
- N samples: 55

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.287 *
- Linear fit: y = -0.136x + 6.0
- P-value: 0.0337
- N samples: 55

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.047 
- Linear fit: y = -0.317x + 1.9
- P-value: 0.7352
- N samples: 55

**Is Open Source:**
- Correlation: 0.005 
- Linear fit: y = 0.033x + 1.6
- P-value: 0.9684
- N samples: 55

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.193 
- Linear fit: y = -0.061x + 2.8
- P-value: 0.1586
- N samples: 55

**Is Reasoning Model:**
- Correlation: -0.177 
- Linear fit: y = -0.800x + 1.4
- P-value: 0.1954
- N samples: 55

**Is Open Source:**
- Correlation: 0.068 
- Linear fit: y = 0.272x + 0.7
- P-value: 0.6242
- N samples: 55

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
- Correlation: -0.197 
- Linear fit: y = -0.069x + 3.5
- P-value: 0.1484
- N samples: 55

**Days Since 2024-01-01:**
- Correlation: -0.080 
- Linear fit: y = -0.001x + 2.3
- P-value: 0.7365
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.045 
- Linear fit: y = -0.225x + 1.4
- P-value: 0.7457
- N samples: 55

**Is Open Source:**
- Correlation: -0.002 
- Linear fit: y = -0.011x + 1.2
- P-value: 0.9863
- N samples: 55

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.281 *
- Linear fit: y = -0.039x + 1.6
- P-value: 0.0380
- N samples: 55

**Is Reasoning Model:**
- Correlation: -0.151 
- Linear fit: y = -0.300x + 0.6
- P-value: 0.2707
- N samples: 55

**Days Since 2024-01-01:**
- Correlation: -0.099 
- Linear fit: y = -0.000x + 0.7
- P-value: 0.6765
- N samples: 20

**Is Open Source:**
- Correlation: 0.085 
- Linear fit: y = 0.151x + 0.3
- P-value: 0.5354
- N samples: 55

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
- Correlation: 0.218 
- Linear fit: y = 0.692x + 1.0
- P-value: 0.1096
- N samples: 55

**Benchmark Score:**
- Correlation: -0.143 
- Linear fit: y = -0.035x + 2.5
- P-value: 0.2984
- N samples: 55

**Is Reasoning Model:**
- Correlation: 0.101 
- Linear fit: y = 0.358x + 1.1
- P-value: 0.4644
- N samples: 55

**Days Since 2024-01-01:**
- Correlation: 0.021 
- Linear fit: y = 0.000x + 1.1
- P-value: 0.9297
- N samples: 20

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.239 
- Linear fit: y = -2.972x + 7.2
- P-value: 0.0782
- N samples: 55

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
- Correlation: -0.010 
- Linear fit: y = -0.133x + 5.9
- P-value: 0.9446
- N samples: 55

**Benchmark Score:**
- Correlation: -0.004 
- Linear fit: y = -0.003x + 5.9
- P-value: 0.9797
- N samples: 55

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
- Correlation: 0.181 
- Linear fit: y = 0.014x + -0.2
- P-value: 0.1868
- N samples: 55

**Is Reasoning Model:**
- Correlation: 0.092 
- Linear fit: y = 0.100x + 0.2
- P-value: 0.5044
- N samples: 55

**Is Open Source:**
- Correlation: 0.068 
- Linear fit: y = 0.066x + 0.2
- P-value: 0.6201
- N samples: 55

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.390 **
- Linear fit: y = -5.956x + 22.4
- P-value: 0.0033
- N samples: 55

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
- Correlation: -0.249 
- Linear fit: y = -4.267x + 22.7
- P-value: 0.0667
- N samples: 55

**Benchmark Score:**
- Correlation: -0.113 
- Linear fit: y = -0.135x + 23.9
- P-value: 0.4109
- N samples: 55

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.379 
- Linear fit: y = -0.001x + 4.4
- P-value: 0.1339
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.270 *
- Linear fit: y = -1.825x + 5.4
- P-value: 0.0460
- N samples: 55

**Days Since 2024-01-01:**
- Correlation: -0.187 
- Linear fit: y = -0.003x + 5.8
- P-value: 0.4300
- N samples: 20

**Is Open Source:**
- Correlation: -0.156 
- Linear fit: y = -0.940x + 4.5
- P-value: 0.2552
- N samples: 55

**Benchmark Score:**
- Correlation: -0.132 
- Linear fit: y = -0.062x + 6.1
- P-value: 0.3364
- N samples: 55

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.170 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.5133
- N samples: 17

**Benchmark Score:**
- Correlation: -0.136 
- Linear fit: y = -0.004x + 0.2
- P-value: 0.3228
- N samples: 55

**Days Since 2024-01-01:**
- Correlation: 0.100 
- Linear fit: y = 0.000x + -0.1
- P-value: 0.6745
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.099 
- Linear fit: y = -0.042x + 0.1
- P-value: 0.4715
- N samples: 55

**Is Open Source:**
- Correlation: 0.011 
- Linear fit: y = 0.004x + 0.0
- P-value: 0.9387
- N samples: 55

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.487 *
- Linear fit: y = -0.007x + 6.3
- P-value: 0.0296
- N samples: 20

**Benchmark Score:**
- Correlation: -0.146 
- Linear fit: y = -0.033x + 1.5
- P-value: 0.2864
- N samples: 55

**Is Open Source:**
- Correlation: -0.098 
- Linear fit: y = -0.282x + 0.6
- P-value: 0.4755
- N samples: 55

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.8201
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.049 
- Linear fit: y = -0.158x + 0.5
- P-value: 0.7218
- N samples: 55

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.352 
- Linear fit: y = -0.004x + 4.0
- P-value: 0.1282
- N samples: 20

**Benchmark Score:**
- Correlation: -0.298 *
- Linear fit: y = -0.101x + 4.4
- P-value: 0.0272
- N samples: 55

**Model Size (B):**
- Correlation: -0.134 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.6083
- N samples: 17

**Is Open Source:**
- Correlation: 0.055 
- Linear fit: y = 0.239x + 1.1
- P-value: 0.6888
- N samples: 55

**Is Reasoning Model:**
- Correlation: -0.024 
- Linear fit: y = -0.117x + 1.3
- P-value: 0.8615
- N samples: 55

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.357 
- Linear fit: y = 0.000x + 0.0
- P-value: 0.1590
- N samples: 17

**Is Open Source:**
- Correlation: 0.205 
- Linear fit: y = 0.077x + 0.0
- P-value: 0.1329
- N samples: 55

**Is Reasoning Model:**
- Correlation: -0.099 
- Linear fit: y = -0.042x + 0.1
- P-value: 0.4715
- N samples: 55

**Benchmark Score:**
- Correlation: -0.078 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.5717
- N samples: 55

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
  r = -0.390, y = -5.956x + 22.4

**category3_logical_errors vs Is Open Source:**
  r = -0.354, y = -6.893x + 26.9


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
- Correlation: 0.666 ***
- Linear fit: y = 0.980x + 5.0

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.582 ***
- Linear fit: y = 1.271x + 20.6

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.467 ***
- Linear fit: y = 0.317x + 0.9

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.615 ***
- Linear fit: y = 0.913x + 16.9

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.481 ***
- Linear fit: y = 0.222x + -0.0

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.420 **
- Linear fit: y = 0.131x + -1.5

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.968 ***, y = 0.759x + 1.6

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.967 ***, y = 0.914x + -1.0

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.928 ***, y = 0.467x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.893 ***, y = 0.638x + 0.1

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.864 ***, y = 0.390x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.778 ***, y = 0.240x + -1.6

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.760 ***, y = 0.361x + -0.2

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.724 ***, y = 0.144x + 0.0

**1a: Instruction Override vs 3b: Self Contradiction:**
  r = 0.697 ***, y = 1.043x + 3.2

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = 0.666 ***, y = 0.980x + 5.0

**Category 1: Input Misalignment vs 3b: Self Contradiction:**
  r = 0.664 ***, y = 0.448x + 3.0

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = 0.663 ***, y = 0.226x + -0.4

**1b: Context Omission vs 1c: Prompt Contradiction:**
  r = 0.661 ***, y = 0.261x + 0.1

**Category 1: Input Misalignment vs 2b: Spurious Numeric:**
  r = 0.658 ***, y = 0.915x + 3.6

**Category 2: Factual Errors vs 1a: Instruction Override:**
  r = 0.657 ***, y = 0.202x + -0.7

**1a: Instruction Override vs 1b: Context Omission:**
  r = 0.652 ***, y = 0.726x + 0.6

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = 0.649 ***, y = 1.794x + 3.6

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.642 ***, y = 0.409x + -3.8

**1a: Instruction Override vs 2b: Spurious Numeric:**
  r = 0.641 ***, y = 1.977x + 4.2

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.615 ***, y = 0.913x + 16.9

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
