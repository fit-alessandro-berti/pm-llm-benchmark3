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
- Correlation: -0.226 
- Linear fit: y = -0.158x + 7.8
- P-value: 0.1191
- N samples: 49

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.117 
- Linear fit: y = -1.200x + 3.6
- P-value: 0.4243
- N samples: 49

**Days Since 2024-01-01:**
- Correlation: -0.046 
- Linear fit: y = -0.001x + 3.6
- P-value: 0.8464
- N samples: 20

**Is Open Source:**
- Correlation: 0.034 
- Linear fit: y = 0.315x + 2.6
- P-value: 0.8170
- N samples: 49

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.217 
- Linear fit: y = -2.945x + 9.3
- P-value: 0.1349
- N samples: 49

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
- Correlation: 0.035 
- Linear fit: y = 0.529x + 7.5
- P-value: 0.8106
- N samples: 49

**Benchmark Score:**
- Correlation: 0.007 
- Linear fit: y = 0.008x + 7.6
- P-value: 0.9601
- N samples: 49

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
- Correlation: -0.286 *
- Linear fit: y = -5.502x + 26.0
- P-value: 0.0463
- N samples: 49

**Is Reasoning Model:**
- Correlation: -0.279 
- Linear fit: y = -5.929x + 27.5
- P-value: 0.0526
- N samples: 49

**Benchmark Score:**
- Correlation: -0.172 
- Linear fit: y = -0.250x + 31.2
- P-value: 0.2385
- N samples: 49

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.275 
- Linear fit: y = -0.131x + 6.0
- P-value: 0.0554
- N samples: 49

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.023 
- Linear fit: y = -0.157x + 1.9
- P-value: 0.8780
- N samples: 49

**Is Open Source:**
- Correlation: -0.008 
- Linear fit: y = -0.048x + 1.8
- P-value: 0.9583
- N samples: 49

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
- Correlation: -0.201 
- Linear fit: y = -8.342x + 39.8
- P-value: 0.1655
- N samples: 49

**Benchmark Score:**
- Correlation: -0.165 
- Linear fit: y = -0.518x + 52.2
- P-value: 0.2563
- N samples: 49

**Is Reasoning Model:**
- Correlation: -0.146 
- Linear fit: y = -6.700x + 40.5
- P-value: 0.3165
- N samples: 49

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.226 
- Linear fit: y = -0.158x + 7.8
- P-value: 0.1191
- N samples: 49

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.117 
- Linear fit: y = -1.200x + 3.6
- P-value: 0.4243
- N samples: 49

**Days Since 2024-01-01:**
- Correlation: -0.046 
- Linear fit: y = -0.001x + 3.6
- P-value: 0.8464
- N samples: 20

**Is Open Source:**
- Correlation: 0.034 
- Linear fit: y = 0.315x + 2.6
- P-value: 0.8170
- N samples: 49

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.217 
- Linear fit: y = -2.945x + 9.3
- P-value: 0.1349
- N samples: 49

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
- Correlation: 0.035 
- Linear fit: y = 0.529x + 7.5
- P-value: 0.8106
- N samples: 49

**Benchmark Score:**
- Correlation: 0.007 
- Linear fit: y = 0.008x + 7.6
- P-value: 0.9601
- N samples: 49

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
- Correlation: -0.286 *
- Linear fit: y = -5.502x + 26.0
- P-value: 0.0463
- N samples: 49

**Is Reasoning Model:**
- Correlation: -0.279 
- Linear fit: y = -5.929x + 27.5
- P-value: 0.0526
- N samples: 49

**Benchmark Score:**
- Correlation: -0.172 
- Linear fit: y = -0.250x + 31.2
- P-value: 0.2385
- N samples: 49

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.275 
- Linear fit: y = -0.131x + 6.0
- P-value: 0.0554
- N samples: 49

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.023 
- Linear fit: y = -0.157x + 1.9
- P-value: 0.8780
- N samples: 49

**Is Open Source:**
- Correlation: -0.008 
- Linear fit: y = -0.048x + 1.8
- P-value: 0.9583
- N samples: 49

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.178 
- Linear fit: y = -0.057x + 2.7
- P-value: 0.2215
- N samples: 49

**Is Reasoning Model:**
- Correlation: -0.175 
- Linear fit: y = -0.814x + 1.5
- P-value: 0.2304
- N samples: 49

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.8198
- N samples: 17

**Is Open Source:**
- Correlation: 0.057 
- Linear fit: y = 0.242x + 0.8
- P-value: 0.6957
- N samples: 49

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
- Correlation: -0.177 
- Linear fit: y = -0.062x + 3.4
- P-value: 0.2245
- N samples: 49

**Days Since 2024-01-01:**
- Correlation: -0.080 
- Linear fit: y = -0.001x + 2.3
- P-value: 0.7365
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.030 
- Linear fit: y = -0.157x + 1.5
- P-value: 0.8353
- N samples: 49

**Is Open Source:**
- Correlation: -0.023 
- Linear fit: y = -0.107x + 1.4
- P-value: 0.8759
- N samples: 49

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.282 *
- Linear fit: y = -0.039x + 1.7
- P-value: 0.0493
- N samples: 49

**Is Reasoning Model:**
- Correlation: -0.112 
- Linear fit: y = -0.229x + 0.6
- P-value: 0.4446
- N samples: 49

**Days Since 2024-01-01:**
- Correlation: -0.099 
- Linear fit: y = -0.000x + 0.7
- P-value: 0.6765
- N samples: 20

**Is Open Source:**
- Correlation: 0.097 
- Linear fit: y = 0.180x + 0.3
- P-value: 0.5056
- N samples: 49

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
- Correlation: 0.204 
- Linear fit: y = 0.665x + 1.0
- P-value: 0.1595
- N samples: 49

**Benchmark Score:**
- Correlation: -0.160 
- Linear fit: y = -0.039x + 2.5
- P-value: 0.2730
- N samples: 49

**Is Reasoning Model:**
- Correlation: 0.083 
- Linear fit: y = 0.300x + 1.1
- P-value: 0.5698
- N samples: 49

**Days Since 2024-01-01:**
- Correlation: 0.021 
- Linear fit: y = 0.000x + 1.1
- P-value: 0.9297
- N samples: 20

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.280 
- Linear fit: y = -3.580x + 8.1
- P-value: 0.0510
- N samples: 49

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
- Correlation: 0.033 
- Linear fit: y = 0.032x + 5.3
- P-value: 0.8215
- N samples: 49

**Is Reasoning Model:**
- Correlation: 0.011 
- Linear fit: y = 0.157x + 6.2
- P-value: 0.9395
- N samples: 49

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
- Correlation: 0.224 
- Linear fit: y = 0.015x + -0.2
- P-value: 0.1217
- N samples: 49

**Is Reasoning Model:**
- Correlation: 0.073 
- Linear fit: y = 0.071x + 0.2
- P-value: 0.6177
- N samples: 49

**Is Open Source:**
- Correlation: -0.034 
- Linear fit: y = -0.030x + 0.3
- P-value: 0.8168
- N samples: 49

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.322 
- Linear fit: y = -0.002x + 21.7
- P-value: 0.2069
- N samples: 17

**Is Open Source:**
- Correlation: -0.316 *
- Linear fit: y = -4.650x + 21.4
- P-value: 0.0271
- N samples: 49

**Days Since 2024-01-01:**
- Correlation: -0.299 
- Linear fit: y = -0.010x + 28.0
- P-value: 0.2000
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.241 
- Linear fit: y = -3.929x + 21.9
- P-value: 0.0952
- N samples: 49

**Benchmark Score:**
- Correlation: -0.164 
- Linear fit: y = -0.182x + 24.9
- P-value: 0.2611
- N samples: 49

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.379 
- Linear fit: y = -0.001x + 4.4
- P-value: 0.1339
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.284 *
- Linear fit: y = -1.957x + 5.5
- P-value: 0.0484
- N samples: 49

**Days Since 2024-01-01:**
- Correlation: -0.187 
- Linear fit: y = -0.003x + 5.8
- P-value: 0.4300
- N samples: 20

**Is Open Source:**
- Correlation: -0.137 
- Linear fit: y = -0.853x + 4.5
- P-value: 0.3486
- N samples: 49

**Benchmark Score:**
- Correlation: -0.134 
- Linear fit: y = -0.063x + 6.1
- P-value: 0.3572
- N samples: 49

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.170 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.5133
- N samples: 17

**Benchmark Score:**
- Correlation: -0.128 
- Linear fit: y = -0.004x + 0.2
- P-value: 0.3797
- N samples: 49

**Days Since 2024-01-01:**
- Correlation: 0.100 
- Linear fit: y = 0.000x + -0.1
- P-value: 0.6745
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.098 
- Linear fit: y = -0.043x + 0.1
- P-value: 0.5036
- N samples: 49

**Is Open Source:**
- Correlation: 0.004 
- Linear fit: y = 0.002x + 0.0
- P-value: 0.9771
- N samples: 49

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
- Linear fit: y = -0.031x + 1.5
- P-value: 0.3542
- N samples: 49

**Is Open Source:**
- Correlation: -0.115 
- Linear fit: y = -0.348x + 0.6
- P-value: 0.4311
- N samples: 49

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.8201
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.043 
- Linear fit: y = -0.143x + 0.6
- P-value: 0.7711
- N samples: 49

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.352 
- Linear fit: y = -0.004x + 4.0
- P-value: 0.1282
- N samples: 20

**Benchmark Score:**
- Correlation: -0.289 *
- Linear fit: y = -0.098x + 4.4
- P-value: 0.0441
- N samples: 49

**Model Size (B):**
- Correlation: -0.134 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.6083
- N samples: 17

**Is Open Source:**
- Correlation: 0.048 
- Linear fit: y = 0.217x + 1.2
- P-value: 0.7427
- N samples: 49

**Is Reasoning Model:**
- Correlation: 0.006 
- Linear fit: y = 0.029x + 1.3
- P-value: 0.9688
- N samples: 49

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.357 
- Linear fit: y = 0.000x + 0.0
- P-value: 0.1590
- N samples: 17

**Is Open Source:**
- Correlation: 0.211 
- Linear fit: y = 0.083x + -0.0
- P-value: 0.1465
- N samples: 49

**Is Reasoning Model:**
- Correlation: -0.098 
- Linear fit: y = -0.043x + 0.1
- P-value: 0.5036
- N samples: 49

**Benchmark Score:**
- Correlation: -0.069 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.6377
- N samples: 49

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
  r = -0.316, y = -4.650x + 21.4


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
- Correlation: 0.657 ***
- Linear fit: y = 0.961x + 5.3

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.653 ***
- Linear fit: y = 1.352x + 19.6

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.449 **
- Linear fit: y = 0.305x + 1.0

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.719 ***
- Linear fit: y = 1.017x + 15.3

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.466 ***
- Linear fit: y = 0.216x + 0.1

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.473 ***
- Linear fit: y = 0.155x + -1.8

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.968 ***, y = 0.909x + -0.8

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.966 ***, y = 0.739x + 1.9

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.926 ***, y = 0.464x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.890 ***, y = 0.636x + 0.2

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.861 ***, y = 0.391x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.800 ***, y = 0.260x + -1.9

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.758 ***, y = 0.364x + -0.2

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.737 ***, y = 0.489x + -5.1

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.727 ***, y = 0.145x + 0.0

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.719 ***, y = 1.017x + 15.3

**1a: Instruction Override vs 3b: Self Contradiction:**
  r = 0.715 ***, y = 1.059x + 3.1

**2b: Spurious Numeric vs 3a: Unsupported Leap:**
  r = 0.715 ***, y = 0.825x + 13.9

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.697 ***, y = 0.755x + 13.2

**Category 1: Input Misalignment vs 3b: Self Contradiction:**
  r = 0.684 ***, y = 0.460x + 2.9

**Category 3: Logical Errors vs 1a: Instruction Override:**
  r = 0.683 ***, y = 0.150x + -2.6

**1b: Context Omission vs 1c: Prompt Contradiction:**
  r = 0.666 ***, y = 0.264x + 0.0

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = 0.657 ***, y = 0.961x + 5.3

**Category 1: Input Misalignment vs Category 3: Logical Errors:**
  r = 0.653 ***, y = 1.352x + 19.6

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = 0.652 ***, y = 0.223x + -0.4

**Category 2: Factual Errors vs 1a: Instruction Override:**
  r = 0.650 ***, y = 0.202x + -0.7

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
