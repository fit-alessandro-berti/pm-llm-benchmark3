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
- Correlation: -0.265 *
- Linear fit: y = -0.173x + 8.4
- P-value: 0.0173
- N samples: 80

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.185 
- Linear fit: y = 1.609x + 1.9
- P-value: 0.1010
- N samples: 80

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.002 
- Linear fit: y = 0.025x + 2.6
- P-value: 0.9829
- N samples: 80

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.116 
- Linear fit: y = -1.412x + 7.5
- P-value: 0.3072
- N samples: 80

**Is Reasoning Model:**
- Correlation: 0.075 
- Linear fit: y = 1.090x + 6.1
- P-value: 0.5064
- N samples: 80

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

**Benchmark Score:**
- Correlation: -0.003 
- Linear fit: y = -0.003x + 7.0
- P-value: 0.9788
- N samples: 80

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Benchmark Score:**
- Correlation: -0.193 
- Linear fit: y = -0.250x + 28.1
- P-value: 0.0867
- N samples: 80

**Is Open Source:**
- Correlation: -0.161 
- Linear fit: y = -2.789x + 20.8
- P-value: 0.1529
- N samples: 80

**Is Reasoning Model:**
- Correlation: -0.091 
- Linear fit: y = -1.869x + 21.1
- P-value: 0.4204
- N samples: 80

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.173 
- Linear fit: y = -1.201x + 2.8
- P-value: 0.1241
- N samples: 80

**Is Reasoning Model:**
- Correlation: 0.132 
- Linear fit: y = 1.081x + 1.5
- P-value: 0.2439
- N samples: 80

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Benchmark Score:**
- Correlation: 0.080 
- Linear fit: y = 0.041x + 0.9
- P-value: 0.4831
- N samples: 80

**Days Since 2024-01-01:**
- Correlation: 0.063 
- Linear fit: y = 0.002x + 1.1
- P-value: 0.6402
- N samples: 57

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.144 
- Linear fit: y = -0.388x + 44.7
- P-value: 0.2028
- N samples: 80

**Days Since 2024-01-01:**
- Correlation: -0.139 
- Linear fit: y = -0.021x + 51.2
- P-value: 0.3022
- N samples: 57

**Is Open Source:**
- Correlation: -0.104 
- Linear fit: y = -3.747x + 33.2
- P-value: 0.3574
- N samples: 80

**Model Size (B):**
- Correlation: -0.066 
- Linear fit: y = -0.001x + 34.3
- P-value: 0.6271
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.012 
- Linear fit: y = 0.520x + 31.2
- P-value: 0.9144
- N samples: 80

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.265 *
- Linear fit: y = -0.173x + 8.4
- P-value: 0.0173
- N samples: 80

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.185 
- Linear fit: y = 1.609x + 1.9
- P-value: 0.1010
- N samples: 80

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.002 
- Linear fit: y = 0.025x + 2.6
- P-value: 0.9829
- N samples: 80

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.116 
- Linear fit: y = -1.412x + 7.5
- P-value: 0.3072
- N samples: 80

**Is Reasoning Model:**
- Correlation: 0.075 
- Linear fit: y = 1.090x + 6.1
- P-value: 0.5064
- N samples: 80

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

**Benchmark Score:**
- Correlation: -0.003 
- Linear fit: y = -0.003x + 7.0
- P-value: 0.9788
- N samples: 80

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Benchmark Score:**
- Correlation: -0.193 
- Linear fit: y = -0.250x + 28.1
- P-value: 0.0867
- N samples: 80

**Is Open Source:**
- Correlation: -0.161 
- Linear fit: y = -2.789x + 20.8
- P-value: 0.1529
- N samples: 80

**Is Reasoning Model:**
- Correlation: -0.091 
- Linear fit: y = -1.869x + 21.1
- P-value: 0.4204
- N samples: 80

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.173 
- Linear fit: y = -1.201x + 2.8
- P-value: 0.1241
- N samples: 80

**Is Reasoning Model:**
- Correlation: 0.132 
- Linear fit: y = 1.081x + 1.5
- P-value: 0.2439
- N samples: 80

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Benchmark Score:**
- Correlation: 0.080 
- Linear fit: y = 0.041x + 0.9
- P-value: 0.4831
- N samples: 80

**Days Since 2024-01-01:**
- Correlation: 0.063 
- Linear fit: y = 0.002x + 1.1
- P-value: 0.6402
- N samples: 57

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.199 
- Linear fit: y = -0.039x + 1.9
- P-value: 0.0766
- N samples: 80

**Model Size (B):**
- Correlation: -0.185 
- Linear fit: y = -0.000x + 0.9
- P-value: 0.1684
- N samples: 57

**Is Open Source:**
- Correlation: 0.138 
- Linear fit: y = 0.359x + 0.4
- P-value: 0.2237
- N samples: 80

**Days Since 2024-01-01:**
- Correlation: -0.128 
- Linear fit: y = -0.001x + 1.9
- P-value: 0.3415
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.079 
- Linear fit: y = -0.246x + 0.8
- P-value: 0.4839
- N samples: 80

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.196 
- Linear fit: y = -0.081x + 4.1
- P-value: 0.0811
- N samples: 80

**Is Open Source:**
- Correlation: 0.185 
- Linear fit: y = 1.022x + 1.0
- P-value: 0.0996
- N samples: 80

**Model Size (B):**
- Correlation: -0.119 
- Linear fit: y = -0.000x + 1.9
- P-value: 0.3798
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.071 
- Linear fit: y = 0.461x + 1.1
- P-value: 0.5336
- N samples: 80

**Days Since 2024-01-01:**
- Correlation: -0.067 
- Linear fit: y = -0.002x + 3.1
- P-value: 0.6189
- N samples: 57

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.210 
- Linear fit: y = -0.053x + 2.4
- P-value: 0.0612
- N samples: 80

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

**Is Open Source:**
- Correlation: 0.067 
- Linear fit: y = 0.228x + 0.5
- P-value: 0.5530
- N samples: 80

**Is Reasoning Model:**
- Correlation: -0.047 
- Linear fit: y = -0.190x + 0.7
- P-value: 0.6760
- N samples: 80

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.094 
- Linear fit: y = -0.000x + 1.3
- P-value: 0.4845
- N samples: 57

**Benchmark Score:**
- Correlation: 0.066 
- Linear fit: y = 0.013x + 0.8
- P-value: 0.5587
- N samples: 80

**Is Reasoning Model:**
- Correlation: 0.065 
- Linear fit: y = 0.203x + 1.1
- P-value: 0.5696
- N samples: 80

**Is Open Source:**
- Correlation: -0.043 
- Linear fit: y = -0.114x + 1.3
- P-value: 0.7053
- N samples: 80

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
- Correlation: -0.077 
- Linear fit: y = -0.867x + 5.5
- P-value: 0.4994
- N samples: 80

**Benchmark Score:**
- Correlation: -0.062 
- Linear fit: y = -0.053x + 7.0
- P-value: 0.5824
- N samples: 80

**Is Reasoning Model:**
- Correlation: 0.038 
- Linear fit: y = 0.513x + 4.8
- P-value: 0.7362
- N samples: 80

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: 0.322 **
- Linear fit: y = 0.037x + -0.7
- P-value: 0.0036
- N samples: 80

**Is Open Source:**
- Correlation: -0.281 *
- Linear fit: y = -0.431x + 0.7
- P-value: 0.0116
- N samples: 80

**Model Size (B):**
- Correlation: 0.249 
- Linear fit: y = 0.000x + 0.3
- P-value: 0.0617
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.206 
- Linear fit: y = 0.375x + 0.2
- P-value: 0.0664
- N samples: 80

**Days Since 2024-01-01:**
- Correlation: 0.131 
- Linear fit: y = 0.001x + -0.2
- P-value: 0.3322
- N samples: 57

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.187 
- Linear fit: y = -0.205x + 22.4
- P-value: 0.0972
- N samples: 80

**Days Since 2024-01-01:**
- Correlation: -0.176 
- Linear fit: y = -0.011x + 25.5
- P-value: 0.1905
- N samples: 57

**Is Open Source:**
- Correlation: -0.143 
- Linear fit: y = -2.105x + 16.4
- P-value: 0.2044
- N samples: 80

**Is Reasoning Model:**
- Correlation: -0.027 
- Linear fit: y = -0.462x + 15.8
- P-value: 0.8148
- N samples: 80

**Model Size (B):**
- Correlation: -0.004 
- Linear fit: y = -0.000x + 16.2
- P-value: 0.9788
- N samples: 57

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.248 *
- Linear fit: y = -1.423x + 5.3
- P-value: 0.0266
- N samples: 80

**Days Since 2024-01-01:**
- Correlation: -0.227 
- Linear fit: y = -0.004x + 8.0
- P-value: 0.0900
- N samples: 57

**Is Open Source:**
- Correlation: -0.147 
- Linear fit: y = -0.714x + 4.5
- P-value: 0.1927
- N samples: 80

**Benchmark Score:**
- Correlation: -0.117 
- Linear fit: y = -0.043x + 5.6
- P-value: 0.3003
- N samples: 80

**Model Size (B):**
- Correlation: -0.026 
- Linear fit: y = -0.000x + 4.3
- P-value: 0.8462
- N samples: 57

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.131 
- Linear fit: y = 0.029x + 0.0
- P-value: 0.2472
- N samples: 80

**Benchmark Score:**
- Correlation: -0.103 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.3635
- N samples: 80

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
- Correlation: 0.061 
- Linear fit: y = 0.016x + 0.0
- P-value: 0.5932
- N samples: 80

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: 0.139 
- Linear fit: y = 0.672x + 0.2
- P-value: 0.2182
- N samples: 80

**Is Open Source:**
- Correlation: -0.092 
- Linear fit: y = -0.377x + 0.8
- P-value: 0.4145
- N samples: 80

**Benchmark Score:**
- Correlation: 0.084 
- Linear fit: y = 0.026x + -0.2
- P-value: 0.4576
- N samples: 80

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

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.173 
- Linear fit: y = -0.774x + 1.9
- P-value: 0.1252
- N samples: 80

**Model Size (B):**
- Correlation: 0.116 
- Linear fit: y = 0.000x + 1.5
- P-value: 0.3908
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.083 
- Linear fit: y = 0.439x + 1.2
- P-value: 0.4649
- N samples: 80

**Days Since 2024-01-01:**
- Correlation: 0.068 
- Linear fit: y = 0.001x + 0.6
- P-value: 0.6164
- N samples: 57

**Benchmark Score:**
- Correlation: 0.059 
- Linear fit: y = 0.020x + 0.9
- P-value: 0.6012
- N samples: 80

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.080 
- Linear fit: y = -0.004x + 0.2
- P-value: 0.4823
- N samples: 80

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.6113
- N samples: 57

**Is Open Source:**
- Correlation: -0.068 
- Linear fit: y = -0.050x + 0.1
- P-value: 0.5465
- N samples: 80

**Days Since 2024-01-01:**
- Correlation: -0.066 
- Linear fit: y = -0.000x + 0.3
- P-value: 0.6241
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.035 
- Linear fit: y = -0.030x + 0.1
- P-value: 0.7559
- N samples: 80

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**2c_false_citation vs Benchmark Score:**
  r = 0.322, y = 0.037x + -0.7


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
- Correlation: 0.409 ***
- Linear fit: y = 0.573x + 5.4

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.433 ***
- Linear fit: y = 0.858x + 17.5

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.395 ***
- Linear fit: y = 0.314x + 1.5

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.465 ***
- Linear fit: y = 0.658x + 15.1

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.617 ***
- Linear fit: y = 0.350x + -0.1

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.529 ***
- Linear fit: y = 0.212x + -1.8

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.971 ***, y = 0.900x + -1.0

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.967 ***, y = 0.821x + -0.7

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.836 ***, y = 0.528x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.810 ***, y = 0.523x + 0.3

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.736 ***, y = 0.433x + -0.3

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.713 ***, y = 0.214x + 0.0

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.664 ***, y = 0.258x + -0.1

**Category 2: Factual Errors vs 4b: Model Semantics Breach:**
  r = 0.629 ***, y = 0.231x + -0.0

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.628 ***, y = 0.176x + 0.7

**Category 2: Factual Errors vs Category 4: Technical Errors:**
  r = 0.617 ***, y = 0.350x + -0.1

**Category 2: Factual Errors vs 4c: Visual Descr Mismatch:**
  r = 0.602 ***, y = 0.036x + -0.2

**Category 4: Technical Errors vs 2b: Spurious Numeric:**
  r = 0.580 ***, y = 0.948x + 3.0

**2b: Spurious Numeric vs 4b: Model Semantics Breach:**
  r = 0.575 ***, y = 0.227x + 0.4

**Category 3: Logical Errors vs 4b: Model Semantics Breach:**
  r = 0.575 ***, y = 0.149x + -1.4

**2b: Spurious Numeric vs 4c: Visual Descr Mismatch:**
  r = 0.557 ***, y = 0.036x + -0.1

**3a: Unsupported Leap vs 4b: Model Semantics Breach:**
  r = 0.553 ***, y = 0.169x + -1.0

**Category 3: Logical Errors vs Category 4: Technical Errors:**
  r = 0.529 ***, y = 0.212x + -1.8

**Category 4: Technical Errors vs 3a: Unsupported Leap:**
  r = 0.491 ***, y = 1.040x + 13.0

**1b: Context Omission vs 3c: Circular Reasoning:**
  r = 0.479 ***, y = 0.020x + -0.0

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.471 ***, y = 0.566x + 11.6

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
