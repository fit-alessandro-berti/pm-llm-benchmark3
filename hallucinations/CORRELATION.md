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
- Correlation: -0.264 
- Linear fit: y = -0.187x + 8.7
- P-value: 0.0913
- N samples: 42

**Is Open Source:**
- Correlation: 0.164 
- Linear fit: y = 1.625x + 2.0
- P-value: 0.2994
- N samples: 42

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.120 
- Linear fit: y = -1.250x + 3.6
- P-value: 0.4485
- N samples: 42

**Days Since 2024-01-01:**
- Correlation: -0.046 
- Linear fit: y = -0.001x + 3.6
- P-value: 0.8464
- N samples: 20

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.205 
- Linear fit: y = -0.002x + 8.5
- P-value: 0.4306
- N samples: 17

**Is Open Source:**
- Correlation: -0.076 
- Linear fit: y = -1.028x + 8.2
- P-value: 0.6303
- N samples: 42

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Benchmark Score:**
- Correlation: -0.054 
- Linear fit: y = -0.052x + 9.4
- P-value: 0.7348
- N samples: 42

**Is Reasoning Model:**
- Correlation: 0.033 
- Linear fit: y = 0.464x + 7.5
- P-value: 0.8361
- N samples: 42

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

**Is Reasoning Model:**
- Correlation: -0.257 
- Linear fit: y = -5.036x + 27.5
- P-value: 0.1006
- N samples: 42

**Benchmark Score:**
- Correlation: -0.240 
- Linear fit: y = -0.321x + 34.3
- P-value: 0.1255
- N samples: 42

**Is Open Source:**
- Correlation: -0.065 
- Linear fit: y = -1.222x + 24.7
- P-value: 0.6805
- N samples: 42

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.318 *
- Linear fit: y = -0.153x + 6.6
- P-value: 0.0402
- N samples: 42

**Is Open Source:**
- Correlation: 0.093 
- Linear fit: y = 0.625x + 1.5
- P-value: 0.5580
- N samples: 42

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.025 
- Linear fit: y = -0.179x + 1.9
- P-value: 0.8736
- N samples: 42

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

**Benchmark Score:**
- Correlation: -0.240 
- Linear fit: y = -0.707x + 58.9
- P-value: 0.1264
- N samples: 42

**Is Reasoning Model:**
- Correlation: -0.139 
- Linear fit: y = -6.036x + 40.5
- P-value: 0.3787
- N samples: 42

**Is Open Source:**
- Correlation: -0.001 
- Linear fit: y = -0.056x + 36.5
- P-value: 0.9932
- N samples: 42

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.264 
- Linear fit: y = -0.187x + 8.7
- P-value: 0.0913
- N samples: 42

**Is Open Source:**
- Correlation: 0.164 
- Linear fit: y = 1.625x + 2.0
- P-value: 0.2994
- N samples: 42

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.120 
- Linear fit: y = -1.250x + 3.6
- P-value: 0.4485
- N samples: 42

**Days Since 2024-01-01:**
- Correlation: -0.046 
- Linear fit: y = -0.001x + 3.6
- P-value: 0.8464
- N samples: 20

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.205 
- Linear fit: y = -0.002x + 8.5
- P-value: 0.4306
- N samples: 17

**Is Open Source:**
- Correlation: -0.076 
- Linear fit: y = -1.028x + 8.2
- P-value: 0.6303
- N samples: 42

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Benchmark Score:**
- Correlation: -0.054 
- Linear fit: y = -0.052x + 9.4
- P-value: 0.7348
- N samples: 42

**Is Reasoning Model:**
- Correlation: 0.033 
- Linear fit: y = 0.464x + 7.5
- P-value: 0.8361
- N samples: 42

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

**Is Reasoning Model:**
- Correlation: -0.257 
- Linear fit: y = -5.036x + 27.5
- P-value: 0.1006
- N samples: 42

**Benchmark Score:**
- Correlation: -0.240 
- Linear fit: y = -0.321x + 34.3
- P-value: 0.1255
- N samples: 42

**Is Open Source:**
- Correlation: -0.065 
- Linear fit: y = -1.222x + 24.7
- P-value: 0.6805
- N samples: 42

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.318 *
- Linear fit: y = -0.153x + 6.6
- P-value: 0.0402
- N samples: 42

**Is Open Source:**
- Correlation: 0.093 
- Linear fit: y = 0.625x + 1.5
- P-value: 0.5580
- N samples: 42

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.025 
- Linear fit: y = -0.179x + 1.9
- P-value: 0.8736
- N samples: 42

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.198 
- Linear fit: y = -0.064x + 3.0
- P-value: 0.2096
- N samples: 42

**Is Reasoning Model:**
- Correlation: -0.172 
- Linear fit: y = -0.821x + 1.5
- P-value: 0.2750
- N samples: 42

**Is Open Source:**
- Correlation: 0.147 
- Linear fit: y = 0.667x + 0.7
- P-value: 0.3533
- N samples: 42

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

**Benchmark Score:**
- Correlation: -0.221 
- Linear fit: y = -0.077x + 3.8
- P-value: 0.1597
- N samples: 42

**Model Size (B):**
- Correlation: -0.211 
- Linear fit: y = -0.001x + 1.9
- P-value: 0.4158
- N samples: 17

**Is Open Source:**
- Correlation: 0.123 
- Linear fit: y = 0.597x + 1.1
- P-value: 0.4391
- N samples: 42

**Days Since 2024-01-01:**
- Correlation: -0.080 
- Linear fit: y = -0.001x + 2.3
- P-value: 0.7365
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.035 
- Linear fit: y = -0.179x + 1.5
- P-value: 0.8262
- N samples: 42

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.333 *
- Linear fit: y = -0.046x + 1.9
- P-value: 0.0310
- N samples: 42

**Is Open Source:**
- Correlation: 0.188 
- Linear fit: y = 0.361x + 0.3
- P-value: 0.2342
- N samples: 42

**Is Reasoning Model:**
- Correlation: -0.124 
- Linear fit: y = -0.250x + 0.6
- P-value: 0.4351
- N samples: 42

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
- Correlation: 0.196 
- Linear fit: y = 0.667x + 1.2
- P-value: 0.2123
- N samples: 42

**Is Reasoning Model:**
- Correlation: 0.160 
- Linear fit: y = 0.571x + 1.1
- P-value: 0.3101
- N samples: 42

**Benchmark Score:**
- Correlation: -0.159 
- Linear fit: y = -0.039x + 2.7
- P-value: 0.3157
- N samples: 42

**Days Since 2024-01-01:**
- Correlation: 0.021 
- Linear fit: y = 0.000x + 1.1
- P-value: 0.9297
- N samples: 20

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.162 
- Linear fit: y = -0.001x + 6.5
- P-value: 0.5338
- N samples: 17

**Is Open Source:**
- Correlation: -0.142 
- Linear fit: y = -1.764x + 6.9
- P-value: 0.3705
- N samples: 42

**Days Since 2024-01-01:**
- Correlation: -0.121 
- Linear fit: y = -0.004x + 8.8
- P-value: 0.6113
- N samples: 20

**Benchmark Score:**
- Correlation: -0.025 
- Linear fit: y = -0.022x + 6.8
- P-value: 0.8776
- N samples: 42

**Is Reasoning Model:**
- Correlation: -0.011 
- Linear fit: y = -0.143x + 6.2
- P-value: 0.9452
- N samples: 42

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
- Correlation: 0.138 
- Linear fit: y = 0.009x + -0.0
- P-value: 0.3818
- N samples: 42

**Is Open Source:**
- Correlation: 0.081 
- Linear fit: y = 0.069x + 0.2
- P-value: 0.6115
- N samples: 42

**Is Reasoning Model:**
- Correlation: 0.040 
- Linear fit: y = 0.036x + 0.2
- P-value: 0.8037
- N samples: 42

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

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

**Benchmark Score:**
- Correlation: -0.229 
- Linear fit: y = -0.230x + 27.2
- P-value: 0.1446
- N samples: 42

**Is Reasoning Model:**
- Correlation: -0.201 
- Linear fit: y = -2.964x + 21.9
- P-value: 0.2009
- N samples: 42

**Is Open Source:**
- Correlation: -0.098 
- Linear fit: y = -1.375x + 20.5
- P-value: 0.5367
- N samples: 42

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.379 
- Linear fit: y = -0.001x + 4.4
- P-value: 0.1339
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.297 
- Linear fit: y = -2.000x + 5.5
- P-value: 0.0563
- N samples: 42

**Benchmark Score:**
- Correlation: -0.187 
- Linear fit: y = -0.086x + 6.9
- P-value: 0.2348
- N samples: 42

**Days Since 2024-01-01:**
- Correlation: -0.187 
- Linear fit: y = -0.003x + 5.8
- P-value: 0.4300
- N samples: 20

**Is Open Source:**
- Correlation: 0.015 
- Linear fit: y = 0.097x + 4.1
- P-value: 0.9242
- N samples: 42

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.232 
- Linear fit: y = -0.005x + 0.2
- P-value: 0.1396
- N samples: 42

**Is Reasoning Model:**
- Correlation: -0.221 
- Linear fit: y = -0.071x + 0.1
- P-value: 0.1598
- N samples: 42

**Is Open Source:**
- Correlation: 0.180 
- Linear fit: y = 0.056x + 0.0
- P-value: 0.2531
- N samples: 42

**Model Size (B):**
- Correlation: -0.170 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.5133
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: 0.100 
- Linear fit: y = 0.000x + -0.1
- P-value: 0.6745
- N samples: 20

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.487 *
- Linear fit: y = -0.007x + 6.3
- P-value: 0.0296
- N samples: 20

**Benchmark Score:**
- Correlation: -0.132 
- Linear fit: y = -0.031x + 1.5
- P-value: 0.4054
- N samples: 42

**Is Open Source:**
- Correlation: -0.089 
- Linear fit: y = -0.292x + 0.6
- P-value: 0.5752
- N samples: 42

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.8201
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.031 
- Linear fit: y = -0.107x + 0.6
- P-value: 0.8448
- N samples: 42

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.354 *
- Linear fit: y = -0.120x + 5.1
- P-value: 0.0213
- N samples: 42

**Days Since 2024-01-01:**
- Correlation: -0.352 
- Linear fit: y = -0.004x + 4.0
- P-value: 0.1282
- N samples: 20

**Is Open Source:**
- Correlation: 0.170 
- Linear fit: y = 0.806x + 0.9
- P-value: 0.2809
- N samples: 42

**Model Size (B):**
- Correlation: -0.134 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.6083
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.007 
- Linear fit: y = -0.036x + 1.3
- P-value: 0.9639
- N samples: 42

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.357 
- Linear fit: y = 0.000x + 0.0
- P-value: 0.1590
- N samples: 17

**Is Open Source:**
- Correlation: 0.258 
- Linear fit: y = 0.111x + 0.0
- P-value: 0.0987
- N samples: 42

**Is Reasoning Model:**
- Correlation: -0.079 
- Linear fit: y = -0.036x + 0.1
- P-value: 0.6187
- N samples: 42

**Benchmark Score:**
- Correlation: -0.065 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.6816
- N samples: 42

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

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.354, y = -0.120x + 5.1

**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.333, y = -0.046x + 1.9

**category4_technical_errors vs Benchmark Score:**
  r = -0.318, y = -0.153x + 6.6


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
- Correlation: 0.644 ***
- Linear fit: y = 0.873x + 5.4

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.662 ***
- Linear fit: y = 1.248x + 20.7

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.442 **
- Linear fit: y = 0.300x + 1.0

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.709 ***
- Linear fit: y = 0.985x + 16.4

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.453 **
- Linear fit: y = 0.226x + 0.0

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.466 **
- Linear fit: y = 0.168x + -2.2

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.965 ***, y = 0.893x + -0.9

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.963 ***, y = 0.723x + 2.5

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.927 ***, y = 0.456x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.887 ***, y = 0.625x + 0.1

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.861 ***, y = 0.394x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.809 ***, y = 0.278x + -2.5

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.772 ***, y = 0.150x + -0.0

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.768 ***, y = 0.375x + -0.2

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.747 ***, y = 0.498x + -5.9

**2b: Spurious Numeric vs 3a: Unsupported Leap:**
  r = 0.744 ***, y = 0.838x + 14.8

**1b: Context Omission vs 1c: Prompt Contradiction:**
  r = 0.742 ***, y = 0.293x + -0.0

**1a: Instruction Override vs 3b: Self Contradiction:**
  r = 0.732 ***, y = 1.035x + 3.2

**Category 3: Logical Errors vs 1a: Instruction Override:**
  r = 0.711 ***, y = 0.173x + -3.2

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.709 ***, y = 0.985x + 16.4

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.699 ***, y = 0.729x + 14.3

**Category 1: Input Misalignment vs 3b: Self Contradiction:**
  r = 0.680 ***, y = 0.440x + 3.0

**Category 2: Factual Errors vs 1a: Instruction Override:**
  r = 0.665 ***, y = 0.225x + -0.8

**Category 1: Input Misalignment vs Category 3: Logical Errors:**
  r = 0.662 ***, y = 1.248x + 20.7

**1a: Instruction Override vs 2b: Spurious Numeric:**
  r = 0.651 ***, y = 1.785x + 4.4

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = 0.644 ***, y = 0.873x + 5.4

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
