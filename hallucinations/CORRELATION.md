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
- Correlation: -0.292 *
- Linear fit: y = -0.010x + 11.2
- P-value: 0.0277
- N samples: 57

**Benchmark Score:**
- Correlation: -0.270 *
- Linear fit: y = -0.177x + 8.1
- P-value: 0.0281
- N samples: 66

**Model Size (B):**
- Correlation: -0.216 
- Linear fit: y = -0.001x + 3.2
- P-value: 0.1061
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.200 
- Linear fit: y = -2.063x + 3.9
- P-value: 0.1071
- N samples: 66

**Is Open Source:**
- Correlation: 0.064 
- Linear fit: y = 0.544x + 2.1
- P-value: 0.6078
- N samples: 66

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.214 
- Linear fit: y = -2.700x + 8.8
- P-value: 0.0851
- N samples: 66

**Model Size (B):**
- Correlation: -0.132 
- Linear fit: y = -0.001x + 8.2
- P-value: 0.3287
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.097 
- Linear fit: y = 1.495x + 6.4
- P-value: 0.4382
- N samples: 66

**Days Since 2024-01-01:**
- Correlation: -0.059 
- Linear fit: y = -0.003x + 10.2
- P-value: 0.6608
- N samples: 57

**Benchmark Score:**
- Correlation: 0.011 
- Linear fit: y = 0.011x + 7.2
- P-value: 0.9290
- N samples: 66

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.335 **
- Linear fit: y = -6.750x + 27.1
- P-value: 0.0059
- N samples: 66

**Days Since 2024-01-01:**
- Correlation: -0.314 *
- Linear fit: y = -0.024x + 44.4
- P-value: 0.0172
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.210 
- Linear fit: y = -5.148x + 28.1
- P-value: 0.0908
- N samples: 66

**Benchmark Score:**
- Correlation: -0.091 
- Linear fit: y = -0.142x + 28.7
- P-value: 0.4664
- N samples: 66

**Model Size (B):**
- Correlation: 0.055 
- Linear fit: y = 0.000x + 23.1
- P-value: 0.6822
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.355 **
- Linear fit: y = -0.008x + 8.9
- P-value: 0.0068
- N samples: 57

**Benchmark Score:**
- Correlation: -0.308 *
- Linear fit: y = -0.143x + 6.3
- P-value: 0.0119
- N samples: 66

**Model Size (B):**
- Correlation: -0.211 
- Linear fit: y = -0.000x + 2.1
- P-value: 0.1156
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.120 
- Linear fit: y = -0.876x + 2.4
- P-value: 0.3390
- N samples: 66

**Is Open Source:**
- Correlation: 0.030 
- Linear fit: y = 0.183x + 1.6
- P-value: 0.8082
- N samples: 66

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.289 *
- Linear fit: y = -0.046x + 74.4
- P-value: 0.0294
- N samples: 57

**Is Open Source:**
- Correlation: -0.228 
- Linear fit: y = -8.844x + 39.6
- P-value: 0.0659
- N samples: 66

**Benchmark Score:**
- Correlation: -0.146 
- Linear fit: y = -0.439x + 49.9
- P-value: 0.2418
- N samples: 66

**Is Reasoning Model:**
- Correlation: -0.137 
- Linear fit: y = -6.503x + 40.7
- P-value: 0.2711
- N samples: 66

**Model Size (B):**
- Correlation: -0.090 
- Linear fit: y = -0.001x + 36.6
- P-value: 0.5033
- N samples: 57

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.292 *
- Linear fit: y = -0.010x + 11.2
- P-value: 0.0277
- N samples: 57

**Benchmark Score:**
- Correlation: -0.270 *
- Linear fit: y = -0.177x + 8.1
- P-value: 0.0281
- N samples: 66

**Model Size (B):**
- Correlation: -0.216 
- Linear fit: y = -0.001x + 3.2
- P-value: 0.1061
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.200 
- Linear fit: y = -2.063x + 3.9
- P-value: 0.1071
- N samples: 66

**Is Open Source:**
- Correlation: 0.064 
- Linear fit: y = 0.544x + 2.1
- P-value: 0.6078
- N samples: 66

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.214 
- Linear fit: y = -2.700x + 8.8
- P-value: 0.0851
- N samples: 66

**Model Size (B):**
- Correlation: -0.132 
- Linear fit: y = -0.001x + 8.2
- P-value: 0.3287
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.097 
- Linear fit: y = 1.495x + 6.4
- P-value: 0.4382
- N samples: 66

**Days Since 2024-01-01:**
- Correlation: -0.059 
- Linear fit: y = -0.003x + 10.2
- P-value: 0.6608
- N samples: 57

**Benchmark Score:**
- Correlation: 0.011 
- Linear fit: y = 0.011x + 7.2
- P-value: 0.9290
- N samples: 66

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.335 **
- Linear fit: y = -6.750x + 27.1
- P-value: 0.0059
- N samples: 66

**Days Since 2024-01-01:**
- Correlation: -0.314 *
- Linear fit: y = -0.024x + 44.4
- P-value: 0.0172
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.210 
- Linear fit: y = -5.148x + 28.1
- P-value: 0.0908
- N samples: 66

**Benchmark Score:**
- Correlation: -0.091 
- Linear fit: y = -0.142x + 28.7
- P-value: 0.4664
- N samples: 66

**Model Size (B):**
- Correlation: 0.055 
- Linear fit: y = 0.000x + 23.1
- P-value: 0.6822
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.355 **
- Linear fit: y = -0.008x + 8.9
- P-value: 0.0068
- N samples: 57

**Benchmark Score:**
- Correlation: -0.308 *
- Linear fit: y = -0.143x + 6.3
- P-value: 0.0119
- N samples: 66

**Model Size (B):**
- Correlation: -0.211 
- Linear fit: y = -0.000x + 2.1
- P-value: 0.1156
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.120 
- Linear fit: y = -0.876x + 2.4
- P-value: 0.3390
- N samples: 66

**Is Open Source:**
- Correlation: 0.030 
- Linear fit: y = 0.183x + 1.6
- P-value: 0.8082
- N samples: 66

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.247 *
- Linear fit: y = -1.157x + 1.7
- P-value: 0.0458
- N samples: 66

**Days Since 2024-01-01:**
- Correlation: -0.246 
- Linear fit: y = -0.004x + 4.2
- P-value: 0.0650
- N samples: 57

**Benchmark Score:**
- Correlation: -0.227 
- Linear fit: y = -0.068x + 3.0
- P-value: 0.0666
- N samples: 66

**Model Size (B):**
- Correlation: -0.210 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.1162
- N samples: 57

**Is Open Source:**
- Correlation: 0.078 
- Linear fit: y = 0.300x + 0.7
- P-value: 0.5339
- N samples: 66

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.230 
- Linear fit: y = -0.004x + 4.7
- P-value: 0.0854
- N samples: 57

**Benchmark Score:**
- Correlation: -0.224 
- Linear fit: y = -0.074x + 3.5
- P-value: 0.0700
- N samples: 66

**Model Size (B):**
- Correlation: -0.215 
- Linear fit: y = -0.000x + 1.6
- P-value: 0.1075
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.107 
- Linear fit: y = -0.552x + 1.6
- P-value: 0.3941
- N samples: 66

**Is Open Source:**
- Correlation: 0.027 
- Linear fit: y = 0.117x + 1.1
- P-value: 0.8269
- N samples: 66

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.321 *
- Linear fit: y = -0.002x + 2.3
- P-value: 0.0149
- N samples: 57

**Benchmark Score:**
- Correlation: -0.276 *
- Linear fit: y = -0.036x + 1.5
- P-value: 0.0248
- N samples: 66

**Is Reasoning Model:**
- Correlation: -0.175 
- Linear fit: y = -0.354x + 0.6
- P-value: 0.1601
- N samples: 66

**Is Open Source:**
- Correlation: 0.077 
- Linear fit: y = 0.128x + 0.3
- P-value: 0.5398
- N samples: 66

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 0.4
- P-value: 0.6583
- N samples: 57

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.252 
- Linear fit: y = -0.000x + 1.7
- P-value: 0.0589
- N samples: 57

**Is Open Source:**
- Correlation: 0.205 
- Linear fit: y = 0.656x + 1.1
- P-value: 0.0993
- N samples: 66

**Benchmark Score:**
- Correlation: -0.161 
- Linear fit: y = -0.040x + 2.7
- P-value: 0.1968
- N samples: 66

**Is Reasoning Model:**
- Correlation: 0.133 
- Linear fit: y = 0.519x + 1.0
- P-value: 0.2868
- N samples: 66

**Days Since 2024-01-01:**
- Correlation: -0.022 
- Linear fit: y = -0.000x + 1.6
- P-value: 0.8698
- N samples: 57

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.271 *
- Linear fit: y = -3.233x + 7.3
- P-value: 0.0280
- N samples: 66

**Model Size (B):**
- Correlation: -0.090 
- Linear fit: y = -0.000x + 6.4
- P-value: 0.5062
- N samples: 57

**Days Since 2024-01-01:**
- Correlation: -0.069 
- Linear fit: y = -0.003x + 8.8
- P-value: 0.6086
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.057 
- Linear fit: y = 0.824x + 5.2
- P-value: 0.6515
- N samples: 66

**Benchmark Score:**
- Correlation: 0.028 
- Linear fit: y = 0.026x + 5.0
- P-value: 0.8209
- N samples: 66

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: 0.259 *
- Linear fit: y = 0.025x + -0.5
- P-value: 0.0360
- N samples: 66

**Model Size (B):**
- Correlation: 0.188 
- Linear fit: y = 0.000x + 0.2
- P-value: 0.1618
- N samples: 57

**Days Since 2024-01-01:**
- Correlation: 0.149 
- Linear fit: y = 0.001x + -0.2
- P-value: 0.2682
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.101 
- Linear fit: y = 0.151x + 0.2
- P-value: 0.4195
- N samples: 66

**Is Open Source:**
- Correlation: -0.100 
- Linear fit: y = -0.122x + 0.4
- P-value: 0.4265
- N samples: 66

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.389 **
- Linear fit: y = -6.144x + 22.6
- P-value: 0.0012
- N samples: 66

**Days Since 2024-01-01:**
- Correlation: -0.323 *
- Linear fit: y = -0.020x + 36.1
- P-value: 0.0143
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.144 
- Linear fit: y = -2.769x + 22.0
- P-value: 0.2490
- N samples: 66

**Model Size (B):**
- Correlation: 0.099 
- Linear fit: y = 0.001x + 18.7
- P-value: 0.4641
- N samples: 57

**Benchmark Score:**
- Correlation: -0.046 
- Linear fit: y = -0.056x + 21.7
- P-value: 0.7131
- N samples: 66

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.302 *
- Linear fit: y = -2.255x + 5.9
- P-value: 0.0138
- N samples: 66

**Days Since 2024-01-01:**
- Correlation: -0.203 
- Linear fit: y = -0.005x + 8.4
- P-value: 0.1302
- N samples: 57

**Benchmark Score:**
- Correlation: -0.166 
- Linear fit: y = -0.079x + 6.7
- P-value: 0.1825
- N samples: 66

**Is Open Source:**
- Correlation: -0.105 
- Linear fit: y = -0.644x + 4.4
- P-value: 0.4015
- N samples: 66

**Model Size (B):**
- Correlation: -0.061 
- Linear fit: y = -0.000x + 4.3
- P-value: 0.6520
- N samples: 57

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.243 *
- Linear fit: y = -0.124x + 0.1
- P-value: 0.0497
- N samples: 66

**Benchmark Score:**
- Correlation: -0.212 
- Linear fit: y = -0.007x + 0.3
- P-value: 0.0875
- N samples: 66

**Model Size (B):**
- Correlation: -0.133 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.3229
- N samples: 57

**Is Open Source:**
- Correlation: 0.093 
- Linear fit: y = 0.039x + 0.0
- P-value: 0.4578
- N samples: 66

**Days Since 2024-01-01:**
- Correlation: 0.070 
- Linear fit: y = 0.000x + -0.1
- P-value: 0.6024
- N samples: 57

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.420 **
- Linear fit: y = -0.005x + 4.5
- P-value: 0.0012
- N samples: 57

**Benchmark Score:**
- Correlation: -0.189 
- Linear fit: y = -0.041x + 1.8
- P-value: 0.1281
- N samples: 66

**Model Size (B):**
- Correlation: -0.138 
- Linear fit: y = -0.000x + 0.6
- P-value: 0.3047
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.081 
- Linear fit: y = -0.277x + 0.6
- P-value: 0.5158
- N samples: 66

**Is Open Source:**
- Correlation: -0.038 
- Linear fit: y = -0.106x + 0.5
- P-value: 0.7636
- N samples: 66

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.305 *
- Linear fit: y = -0.100x + 4.5
- P-value: 0.0127
- N samples: 66

**Days Since 2024-01-01:**
- Correlation: -0.207 
- Linear fit: y = -0.004x + 4.2
- P-value: 0.1232
- N samples: 57

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.000x + 1.5
- P-value: 0.1298
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.106 
- Linear fit: y = -0.547x + 1.6
- P-value: 0.3983
- N samples: 66

**Is Open Source:**
- Correlation: 0.052 
- Linear fit: y = 0.222x + 1.1
- P-value: 0.6764
- N samples: 66

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.194 
- Linear fit: y = 0.067x + 0.0
- P-value: 0.1192
- N samples: 66

**Days Since 2024-01-01:**
- Correlation: -0.127 
- Linear fit: y = -0.000x + 0.2
- P-value: 0.3467
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.124 
- Linear fit: y = -0.052x + 0.1
- P-value: 0.3193
- N samples: 66

**Benchmark Score:**
- Correlation: -0.082 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.5102
- N samples: 66

**Model Size (B):**
- Correlation: 0.006 
- Linear fit: y = 0.000x + 0.0
- P-value: 0.9643
- N samples: 57

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**4a_syntax_error vs Days Since 2024-01-01:**
  r = -0.420, y = -0.005x + 4.5

**3a_unsupported_leap vs Is Open Source:**
  r = -0.389, y = -6.144x + 22.6

**category4_technical_errors vs Days Since 2024-01-01:**
  r = -0.355, y = -0.008x + 8.9

**category3_logical_errors vs Is Open Source:**
  r = -0.335, y = -6.750x + 27.1

**3a_unsupported_leap vs Days Since 2024-01-01:**
  r = -0.323, y = -0.020x + 36.1

**1c_prompt_contradiction vs Days Since 2024-01-01:**
  r = -0.321, y = -0.002x + 2.3

**category3_logical_errors vs Days Since 2024-01-01:**
  r = -0.314, y = -0.024x + 44.4

**category4_technical_errors vs Benchmark Score:**
  r = -0.308, y = -0.143x + 6.3

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.305, y = -0.100x + 4.5

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.302, y = -2.255x + 5.9


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
- Correlation: 0.610 ***
- Linear fit: y = 0.912x + 5.5

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.551 ***
- Linear fit: y = 1.311x + 21.0

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.505 ***
- Linear fit: y = 0.359x + 0.8

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.581 ***
- Linear fit: y = 0.926x + 17.0

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.403 ***
- Linear fit: y = 0.192x + 0.2

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.416 ***
- Linear fit: y = 0.124x + -1.3

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.968 ***, y = 0.760x + 1.6

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.960 ***, y = 0.907x + -1.0

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.926 ***, y = 0.465x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.903 ***, y = 0.637x + 0.2

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.865 ***, y = 0.393x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.782 ***, y = 0.238x + -1.6

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.778 ***, y = 0.362x + -0.2

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.719 ***, y = 0.141x + 0.0

**1a: Instruction Override vs 3b: Self Contradiction:**
  r = 0.688 ***, y = 1.097x + 3.3

**1b: Context Omission vs 1c: Prompt Contradiction:**
  r = 0.654 ***, y = 0.256x + 0.1

**1a: Instruction Override vs 1b: Context Omission:**
  r = 0.649 ***, y = 0.717x + 0.6

**Category 1: Input Misalignment vs 3b: Self Contradiction:**
  r = 0.648 ***, y = 0.470x + 3.1

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = 0.610 ***, y = 0.912x + 5.5

**Category 1: Input Misalignment vs 2b: Spurious Numeric:**
  r = 0.610 ***, y = 0.861x + 3.9

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.606 ***, y = 0.360x + -2.8

**3a: Unsupported Leap vs 3b: Self Contradiction:**
  r = 0.602 ***, y = 0.234x + -0.5

**Category 2: Factual Errors vs 1a: Instruction Override:**
  r = 0.600 ***, y = 0.183x + -0.6

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = 0.597 ***, y = 0.201x + -0.4

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = 0.596 ***, y = 1.674x + 4.0

**1a: Instruction Override vs 2b: Spurious Numeric:**
  r = 0.585 ***, y = 1.816x + 4.4

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
