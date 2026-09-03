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
- Correlation: -0.247 
- Linear fit: y = -0.168x + 7.8
- P-value: 0.0530
- N samples: 62

**Model Size (B):**
- Correlation: -0.212 
- Linear fit: y = -0.001x + 3.1
- P-value: 0.1102
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.196 
- Linear fit: y = -1.976x + 3.9
- P-value: 0.1264
- N samples: 62

**Is Open Source:**
- Correlation: 0.037 
- Linear fit: y = 0.319x + 2.3
- P-value: 0.7756
- N samples: 62

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.220 
- Linear fit: y = -2.804x + 8.9
- P-value: 0.0851
- N samples: 62

**Model Size (B):**
- Correlation: -0.124 
- Linear fit: y = -0.001x + 8.1
- P-value: 0.3539
- N samples: 58

**Days Since 2024-01-01:**
- Correlation: -0.038 
- Linear fit: y = -0.002x + 9.1
- P-value: 0.7757
- N samples: 58

**Is Reasoning Model:**
- Correlation: 0.028 
- Linear fit: y = 0.414x + 7.3
- P-value: 0.8295
- N samples: 62

**Benchmark Score:**
- Correlation: 0.016 
- Linear fit: y = 0.016x + 7.0
- P-value: 0.8990
- N samples: 62

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.377 **
- Linear fit: y = -7.667x + 28.0
- P-value: 0.0025
- N samples: 62

**Days Since 2024-01-01:**
- Correlation: -0.330 *
- Linear fit: y = -0.026x + 45.6
- P-value: 0.0113
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.206 
- Linear fit: y = -4.894x + 28.0
- P-value: 0.1078
- N samples: 62

**Benchmark Score:**
- Correlation: -0.072 
- Linear fit: y = -0.116x + 28.0
- P-value: 0.5756
- N samples: 62

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
- Correlation: -0.297 *
- Linear fit: y = -0.144x + 6.4
- P-value: 0.0189
- N samples: 62

**Model Size (B):**
- Correlation: -0.206 
- Linear fit: y = -0.000x + 2.1
- P-value: 0.1200
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.137 
- Linear fit: y = -0.977x + 2.5
- P-value: 0.2899
- N samples: 62

**Is Open Source:**
- Correlation: 0.013 
- Linear fit: y = 0.079x + 1.7
- P-value: 0.9207
- N samples: 62

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
- Correlation: -0.258 *
- Linear fit: y = -10.202x + 41.0
- P-value: 0.0425
- N samples: 62

**Is Reasoning Model:**
- Correlation: -0.159 
- Linear fit: y = -7.345x + 41.6
- P-value: 0.2157
- N samples: 62

**Benchmark Score:**
- Correlation: -0.128 
- Linear fit: y = -0.398x + 48.8
- P-value: 0.3223
- N samples: 62

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
- Correlation: -0.247 
- Linear fit: y = -0.168x + 7.8
- P-value: 0.0530
- N samples: 62

**Model Size (B):**
- Correlation: -0.212 
- Linear fit: y = -0.001x + 3.1
- P-value: 0.1102
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.196 
- Linear fit: y = -1.976x + 3.9
- P-value: 0.1264
- N samples: 62

**Is Open Source:**
- Correlation: 0.037 
- Linear fit: y = 0.319x + 2.3
- P-value: 0.7756
- N samples: 62

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.220 
- Linear fit: y = -2.804x + 8.9
- P-value: 0.0851
- N samples: 62

**Model Size (B):**
- Correlation: -0.124 
- Linear fit: y = -0.001x + 8.1
- P-value: 0.3539
- N samples: 58

**Days Since 2024-01-01:**
- Correlation: -0.038 
- Linear fit: y = -0.002x + 9.1
- P-value: 0.7757
- N samples: 58

**Is Reasoning Model:**
- Correlation: 0.028 
- Linear fit: y = 0.414x + 7.3
- P-value: 0.8295
- N samples: 62

**Benchmark Score:**
- Correlation: 0.016 
- Linear fit: y = 0.016x + 7.0
- P-value: 0.8990
- N samples: 62

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.377 **
- Linear fit: y = -7.667x + 28.0
- P-value: 0.0025
- N samples: 62

**Days Since 2024-01-01:**
- Correlation: -0.330 *
- Linear fit: y = -0.026x + 45.6
- P-value: 0.0113
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.206 
- Linear fit: y = -4.894x + 28.0
- P-value: 0.1078
- N samples: 62

**Benchmark Score:**
- Correlation: -0.072 
- Linear fit: y = -0.116x + 28.0
- P-value: 0.5756
- N samples: 62

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
- Correlation: -0.297 *
- Linear fit: y = -0.144x + 6.4
- P-value: 0.0189
- N samples: 62

**Model Size (B):**
- Correlation: -0.206 
- Linear fit: y = -0.000x + 2.1
- P-value: 0.1200
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.137 
- Linear fit: y = -0.977x + 2.5
- P-value: 0.2899
- N samples: 62

**Is Open Source:**
- Correlation: 0.013 
- Linear fit: y = 0.079x + 1.7
- P-value: 0.9207
- N samples: 62

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.235 
- Linear fit: y = -0.004x + 4.0
- P-value: 0.0764
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.233 
- Linear fit: y = -1.071x + 1.7
- P-value: 0.0681
- N samples: 62

**Benchmark Score:**
- Correlation: -0.208 
- Linear fit: y = -0.064x + 2.9
- P-value: 0.1052
- N samples: 62

**Model Size (B):**
- Correlation: -0.207 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.1188
- N samples: 58

**Is Open Source:**
- Correlation: 0.055 
- Linear fit: y = 0.217x + 0.8
- P-value: 0.6708
- N samples: 62

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
- Correlation: -0.197 
- Linear fit: y = -0.067x + 3.4
- P-value: 0.1255
- N samples: 62

**Is Reasoning Model:**
- Correlation: -0.119 
- Linear fit: y = -0.603x + 1.7
- P-value: 0.3557
- N samples: 62

**Is Open Source:**
- Correlation: -0.004 
- Linear fit: y = -0.019x + 1.2
- P-value: 0.9734
- N samples: 62

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.308 *
- Linear fit: y = -0.002x + 2.2
- P-value: 0.0185
- N samples: 58

**Benchmark Score:**
- Correlation: -0.273 *
- Linear fit: y = -0.036x + 1.5
- P-value: 0.0321
- N samples: 62

**Is Reasoning Model:**
- Correlation: -0.153 
- Linear fit: y = -0.302x + 0.6
- P-value: 0.2358
- N samples: 62

**Is Open Source:**
- Correlation: 0.071 
- Linear fit: y = 0.121x + 0.3
- P-value: 0.5818
- N samples: 62

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
- Correlation: 0.220 
- Linear fit: y = 0.704x + 1.1
- P-value: 0.0861
- N samples: 62

**Benchmark Score:**
- Correlation: -0.191 
- Linear fit: y = -0.048x + 3.0
- P-value: 0.1363
- N samples: 62

**Is Reasoning Model:**
- Correlation: 0.095 
- Linear fit: y = 0.356x + 1.1
- P-value: 0.4616
- N samples: 62

**Days Since 2024-01-01:**
- Correlation: -0.018 
- Linear fit: y = -0.000x + 1.5
- P-value: 0.8949
- N samples: 58

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.291 *
- Linear fit: y = -3.494x + 7.6
- P-value: 0.0216
- N samples: 62

**Model Size (B):**
- Correlation: -0.083 
- Linear fit: y = -0.000x + 6.2
- P-value: 0.5367
- N samples: 58

**Benchmark Score:**
- Correlation: 0.053 
- Linear fit: y = 0.050x + 4.3
- P-value: 0.6825
- N samples: 62

**Days Since 2024-01-01:**
- Correlation: -0.049 
- Linear fit: y = -0.002x + 7.8
- P-value: 0.7166
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.003 
- Linear fit: y = -0.040x + 5.9
- P-value: 0.9825
- N samples: 62

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: 0.194 
- Linear fit: y = 0.015x + -0.2
- P-value: 0.1305
- N samples: 62

**Model Size (B):**
- Correlation: 0.191 
- Linear fit: y = 0.000x + 0.2
- P-value: 0.1515
- N samples: 58

**Days Since 2024-01-01:**
- Correlation: 0.158 
- Linear fit: y = 0.001x + -0.2
- P-value: 0.2349
- N samples: 58

**Is Reasoning Model:**
- Correlation: 0.087 
- Linear fit: y = 0.098x + 0.2
- P-value: 0.5006
- N samples: 62

**Is Open Source:**
- Correlation: -0.015 
- Linear fit: y = -0.015x + 0.3
- P-value: 0.9069
- N samples: 62

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.423 ***
- Linear fit: y = -6.752x + 23.2
- P-value: 0.0006
- N samples: 62

**Days Since 2024-01-01:**
- Correlation: -0.340 **
- Linear fit: y = -0.021x + 37.1
- P-value: 0.0091
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.150 
- Linear fit: y = -2.790x + 22.1
- P-value: 0.2456
- N samples: 62

**Model Size (B):**
- Correlation: 0.089 
- Linear fit: y = 0.000x + 19.0
- P-value: 0.5047
- N samples: 58

**Benchmark Score:**
- Correlation: -0.039 
- Linear fit: y = -0.049x + 21.5
- P-value: 0.7623
- N samples: 62

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.277 *
- Linear fit: y = -1.991x + 5.8
- P-value: 0.0294
- N samples: 62

**Days Since 2024-01-01:**
- Correlation: -0.212 
- Linear fit: y = -0.005x + 8.6
- P-value: 0.1102
- N samples: 58

**Is Open Source:**
- Correlation: -0.154 
- Linear fit: y = -0.950x + 4.8
- P-value: 0.2319
- N samples: 62

**Benchmark Score:**
- Correlation: -0.123 
- Linear fit: y = -0.060x + 6.2
- P-value: 0.3407
- N samples: 62

**Model Size (B):**
- Correlation: -0.065 
- Linear fit: y = -0.000x + 4.3
- P-value: 0.6295
- N samples: 58

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.224 
- Linear fit: y = -0.112x + 0.1
- P-value: 0.0806
- N samples: 62

**Benchmark Score:**
- Correlation: -0.206 
- Linear fit: y = -0.007x + 0.3
- P-value: 0.1082
- N samples: 62

**Model Size (B):**
- Correlation: -0.132 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.3238
- N samples: 58

**Is Open Source:**
- Correlation: 0.082 
- Linear fit: y = 0.035x + 0.0
- P-value: 0.5239
- N samples: 62

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
- Correlation: -0.176 
- Linear fit: y = -0.040x + 1.7
- P-value: 0.1714
- N samples: 62

**Is Reasoning Model:**
- Correlation: -0.137 
- Linear fit: y = -0.460x + 0.8
- P-value: 0.2872
- N samples: 62

**Model Size (B):**
- Correlation: -0.136 
- Linear fit: y = -0.000x + 0.5
- P-value: 0.3078
- N samples: 58

**Is Open Source:**
- Correlation: -0.057 
- Linear fit: y = -0.165x + 0.5
- P-value: 0.6577
- N samples: 62

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.300 *
- Linear fit: y = -0.102x + 4.5
- P-value: 0.0177
- N samples: 62

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
- Correlation: -0.094 
- Linear fit: y = -0.472x + 1.6
- P-value: 0.4676
- N samples: 62

**Is Open Source:**
- Correlation: 0.041 
- Linear fit: y = 0.177x + 1.2
- P-value: 0.7511
- N samples: 62

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.189 
- Linear fit: y = 0.067x + 0.0
- P-value: 0.1422
- N samples: 62

**Days Since 2024-01-01:**
- Correlation: -0.122 
- Linear fit: y = -0.000x + 0.2
- P-value: 0.3629
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.110 
- Linear fit: y = -0.045x + 0.1
- P-value: 0.3946
- N samples: 62

**Benchmark Score:**
- Correlation: -0.073 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.5716
- N samples: 62

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
  r = -0.423, y = -6.752x + 23.2

**4a_syntax_error vs Days Since 2024-01-01:**
  r = -0.409, y = -0.005x + 4.3

**category3_logical_errors vs Is Open Source:**
  r = -0.377, y = -7.667x + 28.0

**3a_unsupported_leap vs Days Since 2024-01-01:**
  r = -0.340, y = -0.021x + 37.1

**category4_technical_errors vs Days Since 2024-01-01:**
  r = -0.339, y = -0.008x + 8.4

**category3_logical_errors vs Days Since 2024-01-01:**
  r = -0.330, y = -0.026x + 45.6

**1c_prompt_contradiction vs Days Since 2024-01-01:**
  r = -0.308, y = -0.002x + 2.2

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.300, y = -0.102x + 4.5


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
- Correlation: 0.627 ***
- Linear fit: y = 0.924x + 5.3

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.552 ***
- Linear fit: y = 1.301x + 21.1

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.504 ***
- Linear fit: y = 0.358x + 0.9

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.590 ***
- Linear fit: y = 0.942x + 17.1

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.427 ***
- Linear fit: y = 0.206x + 0.2

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.429 ***
- Linear fit: y = 0.130x + -1.4

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.969 ***, y = 0.761x + 1.5

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.964 ***, y = 0.909x + -1.0

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.925 ***, y = 0.464x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.902 ***, y = 0.634x + 0.1

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.863 ***, y = 0.394x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.781 ***, y = 0.237x + -1.5

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.781 ***, y = 0.365x + -0.2

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.724 ***, y = 0.142x + 0.0

**1a: Instruction Override vs 3b: Self Contradiction:**
  r = 0.688 ***, y = 1.079x + 3.4

**1b: Context Omission vs 1c: Prompt Contradiction:**
  r = 0.662 ***, y = 0.259x + 0.1

**Category 1: Input Misalignment vs 3b: Self Contradiction:**
  r = 0.646 ***, y = 0.461x + 3.2

**1a: Instruction Override vs 1b: Context Omission:**
  r = 0.644 ***, y = 0.709x + 0.6

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = 0.627 ***, y = 0.924x + 5.3

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.625 ***, y = 0.369x + -3.1

**Category 1: Input Misalignment vs 2b: Spurious Numeric:**
  r = 0.621 ***, y = 0.862x + 3.8

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = 0.619 ***, y = 0.211x + -0.4

**Category 2: Factual Errors vs 1a: Instruction Override:**
  r = 0.618 ***, y = 0.191x + -0.6

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = 0.612 ***, y = 1.696x + 3.9

**3a: Unsupported Leap vs 3b: Self Contradiction:**
  r = 0.602 ***, y = 0.233x + -0.3

**1a: Instruction Override vs 2b: Spurious Numeric:**
  r = 0.600 ***, y = 1.828x + 4.3

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
