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
- Correlation: -0.308 **
- Linear fit: y = -0.193x + 8.9
- P-value: 0.0025
- N samples: 94

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.158 
- Linear fit: y = 1.296x + 1.7
- P-value: 0.1279
- N samples: 94

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.017 
- Linear fit: y = -0.178x + 2.4
- P-value: 0.8688
- N samples: 94

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.091 
- Linear fit: y = -1.090x + 7.4
- P-value: 0.3810
- N samples: 94

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
- Correlation: 0.027 
- Linear fit: y = 0.405x + 6.6
- P-value: 0.7966
- N samples: 94

**Benchmark Score:**
- Correlation: -0.018 
- Linear fit: y = -0.017x + 7.5
- P-value: 0.8607
- N samples: 94

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.239 *
- Linear fit: y = -0.309x + 29.6
- P-value: 0.0203
- N samples: 94

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Is Open Source:**
- Correlation: -0.187 
- Linear fit: y = -3.163x + 20.4
- P-value: 0.0707
- N samples: 94

**Is Reasoning Model:**
- Correlation: -0.124 
- Linear fit: y = -2.637x + 21.1
- P-value: 0.2343
- N samples: 94

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.171 
- Linear fit: y = -1.124x + 2.7
- P-value: 0.0992
- N samples: 94

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

**Is Reasoning Model:**
- Correlation: 0.059 
- Linear fit: y = 0.485x + 1.8
- P-value: 0.5746
- N samples: 94

**Benchmark Score:**
- Correlation: 0.026 
- Linear fit: y = 0.013x + 1.7
- P-value: 0.8061
- N samples: 94

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.193 
- Linear fit: y = -0.511x + 48.0
- P-value: 0.0629
- N samples: 94

**Days Since 2024-01-01:**
- Correlation: -0.139 
- Linear fit: y = -0.021x + 51.2
- P-value: 0.3022
- N samples: 57

**Is Open Source:**
- Correlation: -0.117 
- Linear fit: y = -4.048x + 32.2
- P-value: 0.2629
- N samples: 94

**Model Size (B):**
- Correlation: -0.066 
- Linear fit: y = -0.001x + 34.3
- P-value: 0.6271
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.040 
- Linear fit: y = -1.768x + 31.8
- P-value: 0.6990
- N samples: 94

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.308 **
- Linear fit: y = -0.193x + 8.9
- P-value: 0.0025
- N samples: 94

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.158 
- Linear fit: y = 1.296x + 1.7
- P-value: 0.1279
- N samples: 94

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.017 
- Linear fit: y = -0.178x + 2.4
- P-value: 0.8688
- N samples: 94

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.091 
- Linear fit: y = -1.090x + 7.4
- P-value: 0.3810
- N samples: 94

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
- Correlation: 0.027 
- Linear fit: y = 0.405x + 6.6
- P-value: 0.7966
- N samples: 94

**Benchmark Score:**
- Correlation: -0.018 
- Linear fit: y = -0.017x + 7.5
- P-value: 0.8607
- N samples: 94

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.239 *
- Linear fit: y = -0.309x + 29.6
- P-value: 0.0203
- N samples: 94

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Is Open Source:**
- Correlation: -0.187 
- Linear fit: y = -3.163x + 20.4
- P-value: 0.0707
- N samples: 94

**Is Reasoning Model:**
- Correlation: -0.124 
- Linear fit: y = -2.637x + 21.1
- P-value: 0.2343
- N samples: 94

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.171 
- Linear fit: y = -1.124x + 2.7
- P-value: 0.0992
- N samples: 94

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

**Is Reasoning Model:**
- Correlation: 0.059 
- Linear fit: y = 0.485x + 1.8
- P-value: 0.5746
- N samples: 94

**Benchmark Score:**
- Correlation: 0.026 
- Linear fit: y = 0.013x + 1.7
- P-value: 0.8061
- N samples: 94

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.227 *
- Linear fit: y = -0.043x + 2.0
- P-value: 0.0275
- N samples: 94

**Model Size (B):**
- Correlation: -0.185 
- Linear fit: y = -0.000x + 0.9
- P-value: 0.1684
- N samples: 57

**Is Open Source:**
- Correlation: 0.134 
- Linear fit: y = 0.330x + 0.4
- P-value: 0.1967
- N samples: 94

**Days Since 2024-01-01:**
- Correlation: -0.128 
- Linear fit: y = -0.001x + 1.9
- P-value: 0.3415
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.036 
- Linear fit: y = -0.111x + 0.6
- P-value: 0.7313
- N samples: 94

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.237 *
- Linear fit: y = -0.093x + 4.5
- P-value: 0.0216
- N samples: 94

**Is Open Source:**
- Correlation: 0.154 
- Linear fit: y = 0.796x + 0.9
- P-value: 0.1374
- N samples: 94

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
- Correlation: 0.034 
- Linear fit: y = 0.221x + 1.1
- P-value: 0.7452
- N samples: 94

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.237 *
- Linear fit: y = -0.057x + 2.5
- P-value: 0.0212
- N samples: 94

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
- Correlation: -0.073 
- Linear fit: y = -0.288x + 0.7
- P-value: 0.4853
- N samples: 94

**Is Open Source:**
- Correlation: 0.054 
- Linear fit: y = 0.170x + 0.4
- P-value: 0.6033
- N samples: 94

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.094 
- Linear fit: y = -0.000x + 1.3
- P-value: 0.4845
- N samples: 57

**Benchmark Score:**
- Correlation: 0.056 
- Linear fit: y = 0.015x + 0.8
- P-value: 0.5952
- N samples: 94

**Is Reasoning Model:**
- Correlation: 0.041 
- Linear fit: y = 0.178x + 1.1
- P-value: 0.6929
- N samples: 94

**Is Open Source:**
- Correlation: -0.006 
- Linear fit: y = -0.020x + 1.3
- P-value: 0.9550
- N samples: 94

**Days Since 2024-01-01:**
- Correlation: 0.001 
- Linear fit: y = 0.000x + 1.2
- P-value: 0.9964
- N samples: 57

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

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

**Is Open Source:**
- Correlation: -0.072 
- Linear fit: y = -0.783x + 5.5
- P-value: 0.4908
- N samples: 94

**Benchmark Score:**
- Correlation: -0.071 
- Linear fit: y = -0.059x + 7.2
- P-value: 0.4978
- N samples: 94

**Is Reasoning Model:**
- Correlation: -0.012 
- Linear fit: y = -0.159x + 5.3
- P-value: 0.9115
- N samples: 94

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.249 
- Linear fit: y = 0.000x + 0.3
- P-value: 0.0617
- N samples: 57

**Benchmark Score:**
- Correlation: 0.242 *
- Linear fit: y = 0.028x + -0.5
- P-value: 0.0186
- N samples: 94

**Is Reasoning Model:**
- Correlation: 0.205 *
- Linear fit: y = 0.386x + 0.2
- P-value: 0.0472
- N samples: 94

**Is Open Source:**
- Correlation: -0.192 
- Linear fit: y = -0.287x + 0.6
- P-value: 0.0635
- N samples: 94

**Days Since 2024-01-01:**
- Correlation: 0.131 
- Linear fit: y = 0.001x + -0.2
- P-value: 0.3322
- N samples: 57

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.236 *
- Linear fit: y = -0.261x + 23.8
- P-value: 0.0220
- N samples: 94

**Days Since 2024-01-01:**
- Correlation: -0.176 
- Linear fit: y = -0.011x + 25.5
- P-value: 0.1905
- N samples: 57

**Is Open Source:**
- Correlation: -0.174 
- Linear fit: y = -2.504x + 15.9
- P-value: 0.0944
- N samples: 94

**Is Reasoning Model:**
- Correlation: -0.086 
- Linear fit: y = -1.558x + 16.1
- P-value: 0.4115
- N samples: 94

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
- Correlation: -0.185 
- Linear fit: y = -1.092x + 5.0
- P-value: 0.0744
- N samples: 94

**Is Open Source:**
- Correlation: -0.146 
- Linear fit: y = -0.683x + 4.4
- P-value: 0.1608
- N samples: 94

**Benchmark Score:**
- Correlation: -0.130 
- Linear fit: y = -0.047x + 5.7
- P-value: 0.2118
- N samples: 94

**Model Size (B):**
- Correlation: -0.026 
- Linear fit: y = -0.000x + 4.3
- P-value: 0.8462
- N samples: 57

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.118 
- Linear fit: y = 0.024x + -0.0
- P-value: 0.2578
- N samples: 94

**Benchmark Score:**
- Correlation: -0.110 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.2897
- N samples: 94

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
- Correlation: 0.050 
- Linear fit: y = 0.013x + 0.0
- P-value: 0.6291
- N samples: 94

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: 0.123 
- Linear fit: y = 0.586x + 0.1
- P-value: 0.2377
- N samples: 94

**Is Open Source:**
- Correlation: -0.091 
- Linear fit: y = -0.346x + 0.7
- P-value: 0.3812
- N samples: 94

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

**Benchmark Score:**
- Correlation: 0.037 
- Linear fit: y = 0.011x + 0.2
- P-value: 0.7242
- N samples: 94

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.168 
- Linear fit: y = -0.733x + 1.8
- P-value: 0.1047
- N samples: 94

**Model Size (B):**
- Correlation: 0.116 
- Linear fit: y = 0.000x + 1.5
- P-value: 0.3908
- N samples: 57

**Days Since 2024-01-01:**
- Correlation: 0.068 
- Linear fit: y = 0.001x + 0.6
- P-value: 0.6164
- N samples: 57

**Benchmark Score:**
- Correlation: 0.023 
- Linear fit: y = 0.008x + 1.2
- P-value: 0.8275
- N samples: 94

**Is Reasoning Model:**
- Correlation: -0.010 
- Linear fit: y = -0.056x + 1.6
- P-value: 0.9228
- N samples: 94

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.104 
- Linear fit: y = -0.005x + 0.3
- P-value: 0.3178
- N samples: 94

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.6113
- N samples: 57

**Is Open Source:**
- Correlation: -0.068 
- Linear fit: y = -0.046x + 0.1
- P-value: 0.5170
- N samples: 94

**Days Since 2024-01-01:**
- Correlation: -0.066 
- Linear fit: y = -0.000x + 0.3
- P-value: 0.6241
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.053 
- Linear fit: y = -0.045x + 0.1
- P-value: 0.6092
- N samples: 94

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**category1_input_misalignment vs Benchmark Score:**
  r = -0.308, y = -0.193x + 8.9


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
- Correlation: 0.395 ***
- Linear fit: y = 0.575x + 5.6

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.445 ***
- Linear fit: y = 0.918x + 16.9

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.398 ***
- Linear fit: y = 0.319x + 1.5

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.460 ***
- Linear fit: y = 0.652x + 14.5

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.587 ***
- Linear fit: y = 0.323x + -0.1

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.544 ***
- Linear fit: y = 0.211x + -1.8

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.968 ***, y = 0.827x + -0.8

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.954 ***, y = 0.871x + -0.8

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.841 ***, y = 0.529x + 0.0

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.817 ***, y = 0.541x + 0.3

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.724 ***, y = 0.417x + -0.3

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.718 ***, y = 0.215x + 0.0

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.669 ***, y = 0.256x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.617 ***, y = 0.171x + 0.9

**Category 2: Factual Errors vs 4b: Model Semantics Breach:**
  r = 0.596 ***, y = 0.217x + 0.0

**Category 2: Factual Errors vs Category 4: Technical Errors:**
  r = 0.587 ***, y = 0.323x + -0.1

**Category 3: Logical Errors vs 4b: Model Semantics Breach:**
  r = 0.579 ***, y = 0.149x + -1.3

**Category 4: Technical Errors vs 2b: Spurious Numeric:**
  r = 0.573 ***, y = 0.949x + 3.1

**2b: Spurious Numeric vs 4b: Model Semantics Breach:**
  r = 0.571 ***, y = 0.228x + 0.3

**Category 2: Factual Errors vs 4c: Visual Descr Mismatch:**
  r = 0.565 ***, y = 0.032x + -0.1

**3a: Unsupported Leap vs 4b: Model Semantics Breach:**
  r = 0.561 ***, y = 0.169x + -1.0

**Category 3: Logical Errors vs Category 4: Technical Errors:**
  r = 0.544 ***, y = 0.211x + -1.8

**2b: Spurious Numeric vs 4c: Visual Descr Mismatch:**
  r = 0.531 ***, y = 0.033x + -0.1

**Category 4: Technical Errors vs 3a: Unsupported Leap:**
  r = 0.510 ***, y = 1.120x + 12.4

**1b: Context Omission vs 3c: Circular Reasoning:**
  r = 0.477 ***, y = 0.019x + -0.0

**1b: Context Omission vs 3a: Unsupported Leap:**
  r = 0.463 ***, y = 1.295x + 13.3

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
