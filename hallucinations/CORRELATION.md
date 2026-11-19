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
- Correlation: -0.312 **
- Linear fit: y = -0.195x + 9.0
- P-value: 0.0021
- N samples: 95

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.162 
- Linear fit: y = 1.327x + 1.6
- P-value: 0.1160
- N samples: 95

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.038 
- Linear fit: y = -0.411x + 2.6
- P-value: 0.7151
- N samples: 95

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.081 
- Linear fit: y = -0.972x + 7.2
- P-value: 0.4328
- N samples: 95

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
- Correlation: 0.034 
- Linear fit: y = 0.536x + 6.4
- P-value: 0.7441
- N samples: 95

**Benchmark Score:**
- Correlation: -0.029 
- Linear fit: y = -0.027x + 7.7
- P-value: 0.7791
- N samples: 95

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.248 *
- Linear fit: y = -0.321x + 30.0
- P-value: 0.0153
- N samples: 95

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Is Open Source:**
- Correlation: -0.176 
- Linear fit: y = -2.972x + 20.2
- P-value: 0.0888
- N samples: 95

**Is Reasoning Model:**
- Correlation: -0.097 
- Linear fit: y = -2.169x + 20.7
- P-value: 0.3507
- N samples: 95

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.164 
- Linear fit: y = -1.075x + 2.6
- P-value: 0.1125
- N samples: 95

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.090 
- Linear fit: y = 0.778x + 1.5
- P-value: 0.3873
- N samples: 95

**Days Since 2024-01-01:**
- Correlation: 0.063 
- Linear fit: y = 0.002x + 1.1
- P-value: 0.6402
- N samples: 57

**Benchmark Score:**
- Correlation: 0.018 
- Linear fit: y = 0.009x + 1.8
- P-value: 0.8623
- N samples: 95

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.203 *
- Linear fit: y = -0.538x + 48.8
- P-value: 0.0489
- N samples: 95

**Days Since 2024-01-01:**
- Correlation: -0.139 
- Linear fit: y = -0.021x + 51.2
- P-value: 0.3022
- N samples: 57

**Is Open Source:**
- Correlation: -0.105 
- Linear fit: y = -3.656x + 31.8
- P-value: 0.3109
- N samples: 95

**Model Size (B):**
- Correlation: -0.066 
- Linear fit: y = -0.001x + 34.3
- P-value: 0.6271
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.024 
- Linear fit: y = -1.112x + 31.1
- P-value: 0.8163
- N samples: 95

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.312 **
- Linear fit: y = -0.195x + 9.0
- P-value: 0.0021
- N samples: 95

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.162 
- Linear fit: y = 1.327x + 1.6
- P-value: 0.1160
- N samples: 95

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.038 
- Linear fit: y = -0.411x + 2.6
- P-value: 0.7151
- N samples: 95

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.081 
- Linear fit: y = -0.972x + 7.2
- P-value: 0.4328
- N samples: 95

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
- Correlation: 0.034 
- Linear fit: y = 0.536x + 6.4
- P-value: 0.7441
- N samples: 95

**Benchmark Score:**
- Correlation: -0.029 
- Linear fit: y = -0.027x + 7.7
- P-value: 0.7791
- N samples: 95

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.248 *
- Linear fit: y = -0.321x + 30.0
- P-value: 0.0153
- N samples: 95

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Is Open Source:**
- Correlation: -0.176 
- Linear fit: y = -2.972x + 20.2
- P-value: 0.0888
- N samples: 95

**Is Reasoning Model:**
- Correlation: -0.097 
- Linear fit: y = -2.169x + 20.7
- P-value: 0.3507
- N samples: 95

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.164 
- Linear fit: y = -1.075x + 2.6
- P-value: 0.1125
- N samples: 95

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.090 
- Linear fit: y = 0.778x + 1.5
- P-value: 0.3873
- N samples: 95

**Days Since 2024-01-01:**
- Correlation: 0.063 
- Linear fit: y = 0.002x + 1.1
- P-value: 0.6402
- N samples: 57

**Benchmark Score:**
- Correlation: 0.018 
- Linear fit: y = 0.009x + 1.8
- P-value: 0.8623
- N samples: 95

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.231 *
- Linear fit: y = -0.043x + 2.0
- P-value: 0.0245
- N samples: 95

**Model Size (B):**
- Correlation: -0.185 
- Linear fit: y = -0.000x + 0.9
- P-value: 0.1684
- N samples: 57

**Is Open Source:**
- Correlation: 0.138 
- Linear fit: y = 0.337x + 0.4
- P-value: 0.1836
- N samples: 95

**Days Since 2024-01-01:**
- Correlation: -0.128 
- Linear fit: y = -0.001x + 1.9
- P-value: 0.3415
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.064 
- Linear fit: y = -0.206x + 0.7
- P-value: 0.5396
- N samples: 95

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.240 *
- Linear fit: y = -0.094x + 4.5
- P-value: 0.0189
- N samples: 95

**Is Open Source:**
- Correlation: 0.158 
- Linear fit: y = 0.813x + 0.9
- P-value: 0.1262
- N samples: 95

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
- Correlation: 0.028 
- Linear fit: y = 0.191x + 1.1
- P-value: 0.7876
- N samples: 95

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.239 *
- Linear fit: y = -0.057x + 2.5
- P-value: 0.0194
- N samples: 95

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
- Correlation: -0.095 
- Linear fit: y = -0.395x + 0.8
- P-value: 0.3576
- N samples: 95

**Is Open Source:**
- Correlation: 0.057 
- Linear fit: y = 0.178x + 0.4
- P-value: 0.5837
- N samples: 95

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.094 
- Linear fit: y = -0.000x + 1.3
- P-value: 0.4845
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.064 
- Linear fit: y = 0.291x + 1.0
- P-value: 0.5364
- N samples: 95

**Benchmark Score:**
- Correlation: 0.047 
- Linear fit: y = 0.012x + 0.8
- P-value: 0.6523
- N samples: 95

**Is Open Source:**
- Correlation: 0.001 
- Linear fit: y = 0.003x + 1.2
- P-value: 0.9929
- N samples: 95

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

**Benchmark Score:**
- Correlation: -0.081 
- Linear fit: y = -0.067x + 7.4
- P-value: 0.4375
- N samples: 95

**Model Size (B):**
- Correlation: -0.079 
- Linear fit: y = -0.000x + 5.8
- P-value: 0.5604
- N samples: 57

**Is Open Source:**
- Correlation: -0.063 
- Linear fit: y = -0.682x + 5.4
- P-value: 0.5470
- N samples: 95

**Is Reasoning Model:**
- Correlation: -0.008 
- Linear fit: y = -0.112x + 5.2
- P-value: 0.9407
- N samples: 95

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.249 
- Linear fit: y = 0.000x + 0.3
- P-value: 0.0617
- N samples: 57

**Benchmark Score:**
- Correlation: 0.248 *
- Linear fit: y = 0.028x + -0.5
- P-value: 0.0154
- N samples: 95

**Is Open Source:**
- Correlation: -0.197 
- Linear fit: y = -0.294x + 0.6
- P-value: 0.0552
- N samples: 95

**Is Reasoning Model:**
- Correlation: 0.181 
- Linear fit: y = 0.357x + 0.2
- P-value: 0.0793
- N samples: 95

**Days Since 2024-01-01:**
- Correlation: 0.131 
- Linear fit: y = 0.001x + -0.2
- P-value: 0.3322
- N samples: 57

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.245 *
- Linear fit: y = -0.271x + 24.1
- P-value: 0.0165
- N samples: 95

**Days Since 2024-01-01:**
- Correlation: -0.176 
- Linear fit: y = -0.011x + 25.5
- P-value: 0.1905
- N samples: 57

**Is Open Source:**
- Correlation: -0.162 
- Linear fit: y = -2.339x + 15.8
- P-value: 0.1174
- N samples: 95

**Is Reasoning Model:**
- Correlation: -0.066 
- Linear fit: y = -1.256x + 15.8
- P-value: 0.5277
- N samples: 95

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
- Correlation: -0.150 
- Linear fit: y = -0.926x + 4.9
- P-value: 0.1477
- N samples: 95

**Is Open Source:**
- Correlation: -0.141 
- Linear fit: y = -0.657x + 4.4
- P-value: 0.1740
- N samples: 95

**Benchmark Score:**
- Correlation: -0.134 
- Linear fit: y = -0.048x + 5.8
- P-value: 0.1941
- N samples: 95

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
- Linear fit: y = 0.024x + 0.0
- P-value: 0.2533
- N samples: 95

**Benchmark Score:**
- Correlation: -0.111 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.2849
- N samples: 95

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
- Correlation: 0.046 
- Linear fit: y = 0.013x + 0.0
- P-value: 0.6551
- N samples: 95

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: 0.109 
- Linear fit: y = 0.546x + 0.1
- P-value: 0.2912
- N samples: 95

**Is Open Source:**
- Correlation: -0.088 
- Linear fit: y = -0.332x + 0.7
- P-value: 0.3961
- N samples: 95

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
- Correlation: 0.033 
- Linear fit: y = 0.010x + 0.2
- P-value: 0.7497
- N samples: 95

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.161 
- Linear fit: y = -0.699x + 1.8
- P-value: 0.1194
- N samples: 95

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

**Is Reasoning Model:**
- Correlation: 0.051 
- Linear fit: y = 0.294x + 1.3
- P-value: 0.6222
- N samples: 95

**Benchmark Score:**
- Correlation: 0.015 
- Linear fit: y = 0.005x + 1.3
- P-value: 0.8867
- N samples: 95

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.106 
- Linear fit: y = -0.005x + 0.3
- P-value: 0.3066
- N samples: 95

**Is Reasoning Model:**
- Correlation: -0.070 
- Linear fit: y = -0.062x + 0.1
- P-value: 0.5032
- N samples: 95

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.6113
- N samples: 57

**Days Since 2024-01-01:**
- Correlation: -0.066 
- Linear fit: y = -0.000x + 0.3
- P-value: 0.6241
- N samples: 57

**Is Open Source:**
- Correlation: -0.065 
- Linear fit: y = -0.044x + 0.1
- P-value: 0.5294
- N samples: 95

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**category1_input_misalignment vs Benchmark Score:**
  r = -0.312, y = -0.195x + 9.0


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
- Correlation: 0.398 ***
- Linear fit: y = 0.582x + 5.5

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.448 ***
- Linear fit: y = 0.928x + 16.8

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.400 ***
- Linear fit: y = 0.321x + 1.4

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.466 ***
- Linear fit: y = 0.661x + 14.4

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.589 ***
- Linear fit: y = 0.324x + -0.1

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.547 ***
- Linear fit: y = 0.212x + -1.9

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.968 ***, y = 0.827x + -0.9

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.955 ***, y = 0.871x + -0.8

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.841 ***, y = 0.529x + 0.0

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.818 ***, y = 0.542x + 0.3

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.724 ***, y = 0.416x + -0.3

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.718 ***, y = 0.215x + 0.0

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.669 ***, y = 0.256x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.618 ***, y = 0.171x + 0.9

**Category 2: Factual Errors vs 4b: Model Semantics Breach:**
  r = 0.598 ***, y = 0.218x + 0.0

**Category 2: Factual Errors vs Category 4: Technical Errors:**
  r = 0.589 ***, y = 0.324x + -0.1

**Category 3: Logical Errors vs 4b: Model Semantics Breach:**
  r = 0.581 ***, y = 0.149x + -1.3

**Category 4: Technical Errors vs 2b: Spurious Numeric:**
  r = 0.575 ***, y = 0.956x + 3.0

**2b: Spurious Numeric vs 4b: Model Semantics Breach:**
  r = 0.574 ***, y = 0.229x + 0.3

**3a: Unsupported Leap vs 4b: Model Semantics Breach:**
  r = 0.564 ***, y = 0.169x + -1.0

**Category 2: Factual Errors vs 4c: Visual Descr Mismatch:**
  r = 0.564 ***, y = 0.032x + -0.1

**Category 3: Logical Errors vs Category 4: Technical Errors:**
  r = 0.547 ***, y = 0.212x + -1.9

**2b: Spurious Numeric vs 4c: Visual Descr Mismatch:**
  r = 0.530 ***, y = 0.033x + -0.1

**Category 4: Technical Errors vs 3a: Unsupported Leap:**
  r = 0.513 ***, y = 1.132x + 12.3

**1b: Context Omission vs 3c: Circular Reasoning:**
  r = 0.477 ***, y = 0.019x + -0.0

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.466 ***, y = 0.661x + 14.4

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
