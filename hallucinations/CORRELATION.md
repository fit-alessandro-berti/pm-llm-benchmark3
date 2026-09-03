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

**Days Since 2024-01-01:**
- Correlation: -0.277 *
- Linear fit: y = -0.010x + 10.6
- P-value: 0.0355
- N samples: 58

**Benchmark Score:**
- Correlation: -0.249 *
- Linear fit: y = -0.169x + 7.9
- P-value: 0.0486
- N samples: 63

**Model Size (B):**
- Correlation: -0.212 
- Linear fit: y = -0.001x + 3.1
- P-value: 0.1102
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.189 
- Linear fit: y = -1.949x + 3.9
- P-value: 0.1375
- N samples: 63

**Is Open Source:**
- Correlation: 0.042 
- Linear fit: y = 0.358x + 2.2
- P-value: 0.7455
- N samples: 63

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.234 
- Linear fit: y = -2.988x + 9.1
- P-value: 0.0648
- N samples: 63

**Model Size (B):**
- Correlation: -0.124 
- Linear fit: y = -0.001x + 8.1
- P-value: 0.3539
- N samples: 58

**Is Reasoning Model:**
- Correlation: 0.106 
- Linear fit: y = 1.633x + 6.4
- P-value: 0.4061
- N samples: 63

**Days Since 2024-01-01:**
- Correlation: -0.038 
- Linear fit: y = -0.002x + 9.1
- P-value: 0.7757
- N samples: 58

**Benchmark Score:**
- Correlation: 0.029 
- Linear fit: y = 0.030x + 6.7
- P-value: 0.8186
- N samples: 63

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.366 **
- Linear fit: y = -7.394x + 27.7
- P-value: 0.0032
- N samples: 63

**Days Since 2024-01-01:**
- Correlation: -0.330 *
- Linear fit: y = -0.026x + 45.6
- P-value: 0.0113
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.205 
- Linear fit: y = -4.969x + 28.1
- P-value: 0.1079
- N samples: 63

**Benchmark Score:**
- Correlation: -0.078 
- Linear fit: y = -0.125x + 28.2
- P-value: 0.5435
- N samples: 63

**Model Size (B):**
- Correlation: 0.047 
- Linear fit: y = 0.000x + 23.3
- P-value: 0.7251
- N samples: 58

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.339 **
- Linear fit: y = -0.008x + 8.4
- P-value: 0.0093
- N samples: 58

**Benchmark Score:**
- Correlation: -0.302 *
- Linear fit: y = -0.146x + 6.4
- P-value: 0.0162
- N samples: 63

**Model Size (B):**
- Correlation: -0.206 
- Linear fit: y = -0.000x + 2.1
- P-value: 0.1200
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.116 
- Linear fit: y = -0.847x + 2.4
- P-value: 0.3673
- N samples: 63

**Is Open Source:**
- Correlation: 0.021 
- Linear fit: y = 0.130x + 1.6
- P-value: 0.8681
- N samples: 63

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.286 *
- Linear fit: y = -0.045x + 73.5
- P-value: 0.0294
- N samples: 58

**Is Open Source:**
- Correlation: -0.256 *
- Linear fit: y = -10.021x + 40.8
- P-value: 0.0431
- N samples: 63

**Is Reasoning Model:**
- Correlation: -0.128 
- Linear fit: y = -6.041x + 40.7
- P-value: 0.3162
- N samples: 63

**Benchmark Score:**
- Correlation: -0.128 
- Linear fit: y = -0.396x + 48.8
- P-value: 0.3180
- N samples: 63

**Model Size (B):**
- Correlation: -0.091 
- Linear fit: y = -0.001x + 36.6
- P-value: 0.4985
- N samples: 58

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.277 *
- Linear fit: y = -0.010x + 10.6
- P-value: 0.0355
- N samples: 58

**Benchmark Score:**
- Correlation: -0.249 *
- Linear fit: y = -0.169x + 7.9
- P-value: 0.0486
- N samples: 63

**Model Size (B):**
- Correlation: -0.212 
- Linear fit: y = -0.001x + 3.1
- P-value: 0.1102
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.189 
- Linear fit: y = -1.949x + 3.9
- P-value: 0.1375
- N samples: 63

**Is Open Source:**
- Correlation: 0.042 
- Linear fit: y = 0.358x + 2.2
- P-value: 0.7455
- N samples: 63

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.234 
- Linear fit: y = -2.988x + 9.1
- P-value: 0.0648
- N samples: 63

**Model Size (B):**
- Correlation: -0.124 
- Linear fit: y = -0.001x + 8.1
- P-value: 0.3539
- N samples: 58

**Is Reasoning Model:**
- Correlation: 0.106 
- Linear fit: y = 1.633x + 6.4
- P-value: 0.4061
- N samples: 63

**Days Since 2024-01-01:**
- Correlation: -0.038 
- Linear fit: y = -0.002x + 9.1
- P-value: 0.7757
- N samples: 58

**Benchmark Score:**
- Correlation: 0.029 
- Linear fit: y = 0.030x + 6.7
- P-value: 0.8186
- N samples: 63

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.366 **
- Linear fit: y = -7.394x + 27.7
- P-value: 0.0032
- N samples: 63

**Days Since 2024-01-01:**
- Correlation: -0.330 *
- Linear fit: y = -0.026x + 45.6
- P-value: 0.0113
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.205 
- Linear fit: y = -4.969x + 28.1
- P-value: 0.1079
- N samples: 63

**Benchmark Score:**
- Correlation: -0.078 
- Linear fit: y = -0.125x + 28.2
- P-value: 0.5435
- N samples: 63

**Model Size (B):**
- Correlation: 0.047 
- Linear fit: y = 0.000x + 23.3
- P-value: 0.7251
- N samples: 58

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.339 **
- Linear fit: y = -0.008x + 8.4
- P-value: 0.0093
- N samples: 58

**Benchmark Score:**
- Correlation: -0.302 *
- Linear fit: y = -0.146x + 6.4
- P-value: 0.0162
- N samples: 63

**Model Size (B):**
- Correlation: -0.206 
- Linear fit: y = -0.000x + 2.1
- P-value: 0.1200
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.116 
- Linear fit: y = -0.847x + 2.4
- P-value: 0.3673
- N samples: 63

**Is Open Source:**
- Correlation: 0.021 
- Linear fit: y = 0.130x + 1.6
- P-value: 0.8681
- N samples: 63

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.239 
- Linear fit: y = -1.122x + 1.7
- P-value: 0.0594
- N samples: 63

**Days Since 2024-01-01:**
- Correlation: -0.235 
- Linear fit: y = -0.004x + 4.0
- P-value: 0.0764
- N samples: 58

**Benchmark Score:**
- Correlation: -0.212 
- Linear fit: y = -0.065x + 3.0
- P-value: 0.0961
- N samples: 63

**Model Size (B):**
- Correlation: -0.207 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.1188
- N samples: 58

**Is Open Source:**
- Correlation: 0.061 
- Linear fit: y = 0.239x + 0.7
- P-value: 0.6337
- N samples: 63

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.216 
- Linear fit: y = -0.004x + 4.4
- P-value: 0.1034
- N samples: 58

**Model Size (B):**
- Correlation: -0.211 
- Linear fit: y = -0.000x + 1.5
- P-value: 0.1115
- N samples: 58

**Benchmark Score:**
- Correlation: -0.202 
- Linear fit: y = -0.069x + 3.4
- P-value: 0.1127
- N samples: 63

**Is Reasoning Model:**
- Correlation: -0.095 
- Linear fit: y = -0.490x + 1.6
- P-value: 0.4607
- N samples: 63

**Is Open Source:**
- Correlation: 0.004 
- Linear fit: y = 0.018x + 1.2
- P-value: 0.9738
- N samples: 63

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.308 *
- Linear fit: y = -0.002x + 2.2
- P-value: 0.0185
- N samples: 58

**Benchmark Score:**
- Correlation: -0.262 *
- Linear fit: y = -0.035x + 1.5
- P-value: 0.0382
- N samples: 63

**Is Reasoning Model:**
- Correlation: -0.166 
- Linear fit: y = -0.337x + 0.6
- P-value: 0.1938
- N samples: 63

**Is Open Source:**
- Correlation: 0.059 
- Linear fit: y = 0.100x + 0.3
- P-value: 0.6450
- N samples: 63

**Model Size (B):**
- Correlation: -0.057 
- Linear fit: y = -0.000x + 0.4
- P-value: 0.6711
- N samples: 58

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.250 
- Linear fit: y = -0.000x + 1.6
- P-value: 0.0584
- N samples: 58

**Is Open Source:**
- Correlation: 0.222 
- Linear fit: y = 0.706x + 1.1
- P-value: 0.0805
- N samples: 63

**Benchmark Score:**
- Correlation: -0.193 
- Linear fit: y = -0.049x + 3.0
- P-value: 0.1289
- N samples: 63

**Is Reasoning Model:**
- Correlation: 0.133 
- Linear fit: y = 0.510x + 1.0
- P-value: 0.2970
- N samples: 63

**Days Since 2024-01-01:**
- Correlation: -0.018 
- Linear fit: y = -0.000x + 1.5
- P-value: 0.8949
- N samples: 58

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.305 *
- Linear fit: y = -3.688x + 7.8
- P-value: 0.0149
- N samples: 63

**Model Size (B):**
- Correlation: -0.083 
- Linear fit: y = -0.000x + 6.2
- P-value: 0.5367
- N samples: 58

**Is Reasoning Model:**
- Correlation: 0.072 
- Linear fit: y = 1.051x + 5.2
- P-value: 0.5726
- N samples: 63

**Benchmark Score:**
- Correlation: 0.067 
- Linear fit: y = 0.064x + 4.0
- P-value: 0.6002
- N samples: 63

**Days Since 2024-01-01:**
- Correlation: -0.049 
- Linear fit: y = -0.002x + 7.8
- P-value: 0.7166
- N samples: 58

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.191 
- Linear fit: y = 0.000x + 0.2
- P-value: 0.1515
- N samples: 58

**Benchmark Score:**
- Correlation: 0.186 
- Linear fit: y = 0.014x + -0.2
- P-value: 0.1437
- N samples: 63

**Days Since 2024-01-01:**
- Correlation: 0.158 
- Linear fit: y = 0.001x + -0.2
- P-value: 0.2349
- N samples: 58

**Is Reasoning Model:**
- Correlation: 0.062 
- Linear fit: y = 0.071x + 0.2
- P-value: 0.6288
- N samples: 63

**Is Open Source:**
- Correlation: -0.006 
- Linear fit: y = -0.006x + 0.3
- P-value: 0.9607
- N samples: 63

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.414 ***
- Linear fit: y = -6.564x + 23.0
- P-value: 0.0008
- N samples: 63

**Days Since 2024-01-01:**
- Correlation: -0.340 **
- Linear fit: y = -0.021x + 37.1
- P-value: 0.0091
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.141 
- Linear fit: y = -2.694x + 22.0
- P-value: 0.2694
- N samples: 63

**Model Size (B):**
- Correlation: 0.089 
- Linear fit: y = 0.000x + 19.0
- P-value: 0.5047
- N samples: 58

**Benchmark Score:**
- Correlation: -0.043 
- Linear fit: y = -0.054x + 21.7
- P-value: 0.7365
- N samples: 63

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.292 *
- Linear fit: y = -2.153x + 5.9
- P-value: 0.0204
- N samples: 63

**Days Since 2024-01-01:**
- Correlation: -0.212 
- Linear fit: y = -0.005x + 8.6
- P-value: 0.1102
- N samples: 58

**Is Open Source:**
- Correlation: -0.141 
- Linear fit: y = -0.867x + 4.7
- P-value: 0.2704
- N samples: 63

**Benchmark Score:**
- Correlation: -0.131 
- Linear fit: y = -0.063x + 6.3
- P-value: 0.3080
- N samples: 63

**Model Size (B):**
- Correlation: -0.065 
- Linear fit: y = -0.000x + 4.3
- P-value: 0.6295
- N samples: 58

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.239 
- Linear fit: y = -0.122x + 0.1
- P-value: 0.0592
- N samples: 63

**Benchmark Score:**
- Correlation: -0.208 
- Linear fit: y = -0.007x + 0.3
- P-value: 0.1024
- N samples: 63

**Model Size (B):**
- Correlation: -0.132 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.3238
- N samples: 58

**Is Open Source:**
- Correlation: 0.085 
- Linear fit: y = 0.036x + 0.0
- P-value: 0.5063
- N samples: 63

**Days Since 2024-01-01:**
- Correlation: 0.073 
- Linear fit: y = 0.000x + -0.1
- P-value: 0.5838
- N samples: 58

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.409 **
- Linear fit: y = -0.005x + 4.3
- P-value: 0.0014
- N samples: 58

**Benchmark Score:**
- Correlation: -0.179 
- Linear fit: y = -0.040x + 1.7
- P-value: 0.1612
- N samples: 63

**Model Size (B):**
- Correlation: -0.136 
- Linear fit: y = -0.000x + 0.5
- P-value: 0.3078
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.075 
- Linear fit: y = -0.255x + 0.6
- P-value: 0.5615
- N samples: 63

**Is Open Source:**
- Correlation: -0.052 
- Linear fit: y = -0.148x + 0.5
- P-value: 0.6850
- N samples: 63

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.305 *
- Linear fit: y = -0.103x + 4.6
- P-value: 0.0151
- N samples: 63

**Model Size (B):**
- Correlation: -0.199 
- Linear fit: y = -0.000x + 1.5
- P-value: 0.1349
- N samples: 58

**Days Since 2024-01-01:**
- Correlation: -0.193 
- Linear fit: y = -0.003x + 4.0
- P-value: 0.1475
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.105 
- Linear fit: y = -0.541x + 1.6
- P-value: 0.4128
- N samples: 63

**Is Open Source:**
- Correlation: 0.049 
- Linear fit: y = 0.212x + 1.1
- P-value: 0.7002
- N samples: 63

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.190 
- Linear fit: y = 0.067x + 0.0
- P-value: 0.1360
- N samples: 63

**Days Since 2024-01-01:**
- Correlation: -0.122 
- Linear fit: y = -0.000x + 0.2
- P-value: 0.3629
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.121 
- Linear fit: y = -0.051x + 0.1
- P-value: 0.3449
- N samples: 63

**Benchmark Score:**
- Correlation: -0.075 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.5590
- N samples: 63

**Model Size (B):**
- Correlation: 0.007 
- Linear fit: y = 0.000x + 0.0
- P-value: 0.9567
- N samples: 58

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**3a_unsupported_leap vs Is Open Source:**
  r = -0.414, y = -6.564x + 23.0

**4a_syntax_error vs Days Since 2024-01-01:**
  r = -0.409, y = -0.005x + 4.3

**category3_logical_errors vs Is Open Source:**
  r = -0.366, y = -7.394x + 27.7

**3a_unsupported_leap vs Days Since 2024-01-01:**
  r = -0.340, y = -0.021x + 37.1

**category4_technical_errors vs Days Since 2024-01-01:**
  r = -0.339, y = -0.008x + 8.4

**category3_logical_errors vs Days Since 2024-01-01:**
  r = -0.330, y = -0.026x + 45.6

**1c_prompt_contradiction vs Days Since 2024-01-01:**
  r = -0.308, y = -0.002x + 2.2

**2b_spurious_numeric vs Is Open Source:**
  r = -0.305, y = -3.688x + 7.8

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.305, y = -0.103x + 4.6

**category4_technical_errors vs Benchmark Score:**
  r = -0.302, y = -0.146x + 6.4


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
- Correlation: 0.613 ***
- Linear fit: y = 0.913x + 5.5

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.553 ***
- Linear fit: y = 1.305x + 21.1

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.506 ***
- Linear fit: y = 0.360x + 0.8

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.572 ***
- Linear fit: y = 0.907x + 17.2

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.411 ***
- Linear fit: y = 0.197x + 0.2

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.432 ***
- Linear fit: y = 0.130x + -1.5

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.969 ***, y = 0.760x + 1.5

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.965 ***, y = 0.913x + -1.0

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.925 ***, y = 0.465x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.903 ***, y = 0.634x + 0.1

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.864 ***, y = 0.394x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.782 ***, y = 0.238x + -1.5

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.781 ***, y = 0.365x + -0.2

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.716 ***, y = 0.141x + 0.0

**1a: Instruction Override vs 3b: Self Contradiction:**
  r = 0.689 ***, y = 1.084x + 3.3

**1b: Context Omission vs 1c: Prompt Contradiction:**
  r = 0.651 ***, y = 0.255x + 0.1

**Category 1: Input Misalignment vs 3b: Self Contradiction:**
  r = 0.646 ***, y = 0.463x + 3.1

**1a: Instruction Override vs 1b: Context Omission:**
  r = 0.645 ***, y = 0.711x + 0.6

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = 0.613 ***, y = 0.913x + 5.5

**Category 1: Input Misalignment vs 2b: Spurious Numeric:**
  r = 0.604 ***, y = 0.851x + 4.0

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.604 ***, y = 0.361x + -2.7

**3a: Unsupported Leap vs 3b: Self Contradiction:**
  r = 0.604 ***, y = 0.234x + -0.4

**Category 2: Factual Errors vs 1a: Instruction Override:**
  r = 0.603 ***, y = 0.185x + -0.6

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = 0.600 ***, y = 0.203x + -0.4

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = 0.590 ***, y = 1.654x + 4.1

**1a: Instruction Override vs 2b: Spurious Numeric:**
  r = 0.581 ***, y = 1.794x + 4.5

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
