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
- Correlation: -0.299 **
- Linear fit: y = -0.190x + 8.8
- P-value: 0.0038
- N samples: 92

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.149 
- Linear fit: y = 1.231x + 1.7
- P-value: 0.1554
- N samples: 92

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.011 
- Linear fit: y = -0.119x + 2.4
- P-value: 0.9134
- N samples: 92

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.099 
- Linear fit: y = -1.183x + 7.5
- P-value: 0.3483
- N samples: 92

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
- Correlation: 0.031 
- Linear fit: y = 0.458x + 6.6
- P-value: 0.7724
- N samples: 92

**Benchmark Score:**
- Correlation: -0.010 
- Linear fit: y = -0.009x + 7.2
- P-value: 0.9266
- N samples: 92

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.225 *
- Linear fit: y = -0.294x + 29.2
- P-value: 0.0310
- N samples: 92

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Is Open Source:**
- Correlation: -0.204 
- Linear fit: y = -3.452x + 20.6
- P-value: 0.0514
- N samples: 92

**Is Reasoning Model:**
- Correlation: -0.117 
- Linear fit: y = -2.489x + 21.1
- P-value: 0.2655
- N samples: 92

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.186 
- Linear fit: y = -1.228x + 2.8
- P-value: 0.0754
- N samples: 92

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.066 
- Linear fit: y = 0.547x + 1.8
- P-value: 0.5308
- N samples: 92

**Days Since 2024-01-01:**
- Correlation: 0.063 
- Linear fit: y = 0.002x + 1.1
- P-value: 0.6402
- N samples: 57

**Benchmark Score:**
- Correlation: 0.044 
- Linear fit: y = 0.023x + 1.4
- P-value: 0.6746
- N samples: 92

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.177 
- Linear fit: y = -0.476x + 47.0
- P-value: 0.0910
- N samples: 92

**Days Since 2024-01-01:**
- Correlation: -0.139 
- Linear fit: y = -0.021x + 51.2
- P-value: 0.3022
- N samples: 57

**Is Open Source:**
- Correlation: -0.132 
- Linear fit: y = -4.604x + 32.7
- P-value: 0.2087
- N samples: 92

**Model Size (B):**
- Correlation: -0.066 
- Linear fit: y = -0.001x + 34.3
- P-value: 0.6271
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.033 
- Linear fit: y = -1.441x + 31.8
- P-value: 0.7544
- N samples: 92

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.299 **
- Linear fit: y = -0.190x + 8.8
- P-value: 0.0038
- N samples: 92

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.149 
- Linear fit: y = 1.231x + 1.7
- P-value: 0.1554
- N samples: 92

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.011 
- Linear fit: y = -0.119x + 2.4
- P-value: 0.9134
- N samples: 92

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.099 
- Linear fit: y = -1.183x + 7.5
- P-value: 0.3483
- N samples: 92

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
- Correlation: 0.031 
- Linear fit: y = 0.458x + 6.6
- P-value: 0.7724
- N samples: 92

**Benchmark Score:**
- Correlation: -0.010 
- Linear fit: y = -0.009x + 7.2
- P-value: 0.9266
- N samples: 92

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.225 *
- Linear fit: y = -0.294x + 29.2
- P-value: 0.0310
- N samples: 92

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Is Open Source:**
- Correlation: -0.204 
- Linear fit: y = -3.452x + 20.6
- P-value: 0.0514
- N samples: 92

**Is Reasoning Model:**
- Correlation: -0.117 
- Linear fit: y = -2.489x + 21.1
- P-value: 0.2655
- N samples: 92

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.186 
- Linear fit: y = -1.228x + 2.8
- P-value: 0.0754
- N samples: 92

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.066 
- Linear fit: y = 0.547x + 1.8
- P-value: 0.5308
- N samples: 92

**Days Since 2024-01-01:**
- Correlation: 0.063 
- Linear fit: y = 0.002x + 1.1
- P-value: 0.6402
- N samples: 57

**Benchmark Score:**
- Correlation: 0.044 
- Linear fit: y = 0.023x + 1.4
- P-value: 0.6746
- N samples: 92

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.220 *
- Linear fit: y = -0.042x + 2.0
- P-value: 0.0350
- N samples: 92

**Model Size (B):**
- Correlation: -0.185 
- Linear fit: y = -0.000x + 0.9
- P-value: 0.1684
- N samples: 57

**Days Since 2024-01-01:**
- Correlation: -0.128 
- Linear fit: y = -0.001x + 1.9
- P-value: 0.3415
- N samples: 57

**Is Open Source:**
- Correlation: 0.127 
- Linear fit: y = 0.315x + 0.4
- P-value: 0.2259
- N samples: 92

**Is Reasoning Model:**
- Correlation: -0.032 
- Linear fit: y = -0.098x + 0.6
- P-value: 0.7656
- N samples: 92

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.228 *
- Linear fit: y = -0.091x + 4.4
- P-value: 0.0287
- N samples: 92

**Is Open Source:**
- Correlation: 0.147 
- Linear fit: y = 0.761x + 0.9
- P-value: 0.1627
- N samples: 92

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
- Correlation: 0.039 
- Linear fit: y = 0.255x + 1.1
- P-value: 0.7102
- N samples: 92

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.233 *
- Linear fit: y = -0.057x + 2.5
- P-value: 0.0253
- N samples: 92

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
- Correlation: -0.070 
- Linear fit: y = -0.276x + 0.7
- P-value: 0.5087
- N samples: 92

**Is Open Source:**
- Correlation: 0.049 
- Linear fit: y = 0.154x + 0.4
- P-value: 0.6446
- N samples: 92

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.094 
- Linear fit: y = -0.000x + 1.3
- P-value: 0.4845
- N samples: 57

**Benchmark Score:**
- Correlation: 0.053 
- Linear fit: y = 0.014x + 0.8
- P-value: 0.6129
- N samples: 92

**Is Reasoning Model:**
- Correlation: 0.040 
- Linear fit: y = 0.173x + 1.1
- P-value: 0.7037
- N samples: 92

**Is Open Source:**
- Correlation: -0.003 
- Linear fit: y = -0.011x + 1.3
- P-value: 0.9758
- N samples: 92

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
- Correlation: -0.079 
- Linear fit: y = -0.861x + 5.6
- P-value: 0.4558
- N samples: 92

**Benchmark Score:**
- Correlation: -0.064 
- Linear fit: y = -0.054x + 7.0
- P-value: 0.5465
- N samples: 92

**Is Reasoning Model:**
- Correlation: -0.008 
- Linear fit: y = -0.116x + 5.3
- P-value: 0.9364
- N samples: 92

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: 0.265 *
- Linear fit: y = 0.031x + -0.6
- P-value: 0.0106
- N samples: 92

**Model Size (B):**
- Correlation: 0.249 
- Linear fit: y = 0.000x + 0.3
- P-value: 0.0617
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.214 *
- Linear fit: y = 0.401x + 0.2
- P-value: 0.0409
- N samples: 92

**Is Open Source:**
- Correlation: -0.207 *
- Linear fit: y = -0.310x + 0.6
- P-value: 0.0475
- N samples: 92

**Days Since 2024-01-01:**
- Correlation: 0.131 
- Linear fit: y = 0.001x + -0.2
- P-value: 0.3322
- N samples: 57

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.227 *
- Linear fit: y = -0.253x + 23.6
- P-value: 0.0297
- N samples: 92

**Is Open Source:**
- Correlation: -0.186 
- Linear fit: y = -2.698x + 16.1
- P-value: 0.0753
- N samples: 92

**Days Since 2024-01-01:**
- Correlation: -0.176 
- Linear fit: y = -0.011x + 25.5
- P-value: 0.1905
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.081 
- Linear fit: y = -1.462x + 16.1
- P-value: 0.4450
- N samples: 92

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
- Correlation: -0.179 
- Linear fit: y = -1.041x + 5.0
- P-value: 0.0882
- N samples: 92

**Is Open Source:**
- Correlation: -0.167 
- Linear fit: y = -0.778x + 4.5
- P-value: 0.1105
- N samples: 92

**Benchmark Score:**
- Correlation: -0.109 
- Linear fit: y = -0.039x + 5.5
- P-value: 0.3015
- N samples: 92

**Model Size (B):**
- Correlation: -0.026 
- Linear fit: y = -0.000x + 4.3
- P-value: 0.8462
- N samples: 57

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.117 
- Linear fit: y = 0.024x + 0.0
- P-value: 0.2670
- N samples: 92

**Benchmark Score:**
- Correlation: -0.109 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.2992
- N samples: 92

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
- Correlation: 0.052 
- Linear fit: y = 0.014x + 0.0
- P-value: 0.6245
- N samples: 92

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: 0.127 
- Linear fit: y = 0.605x + 0.1
- P-value: 0.2287
- N samples: 92

**Is Open Source:**
- Correlation: -0.098 
- Linear fit: y = -0.374x + 0.8
- P-value: 0.3514
- N samples: 92

**Model Size (B):**
- Correlation: 0.065 
- Linear fit: y = 0.000x + 0.5
- P-value: 0.6318
- N samples: 57

**Benchmark Score:**
- Correlation: 0.046 
- Linear fit: y = 0.014x + 0.1
- P-value: 0.6633
- N samples: 92

**Days Since 2024-01-01:**
- Correlation: 0.045 
- Linear fit: y = 0.001x + 0.1
- P-value: 0.7393
- N samples: 57

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.184 
- Linear fit: y = -0.804x + 1.9
- P-value: 0.0786
- N samples: 92

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
- Correlation: 0.042 
- Linear fit: y = 0.014x + 1.1
- P-value: 0.6884
- N samples: 92

**Is Reasoning Model:**
- Correlation: -0.003 
- Linear fit: y = -0.015x + 1.6
- P-value: 0.9793
- N samples: 92

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.100 
- Linear fit: y = -0.005x + 0.3
- P-value: 0.3433
- N samples: 92

**Is Open Source:**
- Correlation: -0.073 
- Linear fit: y = -0.049x + 0.1
- P-value: 0.4917
- N samples: 92

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

**Is Reasoning Model:**
- Correlation: -0.051 
- Linear fit: y = -0.044x + 0.1
- P-value: 0.6278
- N samples: 92

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------

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
- Linear fit: y = 0.574x + 5.6

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.441 ***
- Linear fit: y = 0.906x + 17.0

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.393 ***
- Linear fit: y = 0.314x + 1.5

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.463 ***
- Linear fit: y = 0.655x + 14.6

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.589 ***
- Linear fit: y = 0.324x + -0.0

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.539 ***
- Linear fit: y = 0.210x + -1.8

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.969 ***, y = 0.828x + -0.9

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.954 ***, y = 0.873x + -0.9

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.840 ***, y = 0.529x + 0.0

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.815 ***, y = 0.540x + 0.3

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.723 ***, y = 0.418x + -0.3

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.716 ***, y = 0.215x + 0.0

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.668 ***, y = 0.256x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.619 ***, y = 0.170x + 0.9

**Category 2: Factual Errors vs 4b: Model Semantics Breach:**
  r = 0.598 ***, y = 0.218x + 0.0

**Category 2: Factual Errors vs Category 4: Technical Errors:**
  r = 0.589 ***, y = 0.324x + -0.0

**Category 3: Logical Errors vs 4b: Model Semantics Breach:**
  r = 0.574 ***, y = 0.148x + -1.3

**Category 4: Technical Errors vs 2b: Spurious Numeric:**
  r = 0.573 ***, y = 0.951x + 3.1

**2b: Spurious Numeric vs 4b: Model Semantics Breach:**
  r = 0.571 ***, y = 0.228x + 0.4

**Category 2: Factual Errors vs 4c: Visual Descr Mismatch:**
  r = 0.567 ***, y = 0.032x + -0.1

**3a: Unsupported Leap vs 4b: Model Semantics Breach:**
  r = 0.559 ***, y = 0.168x + -1.0

**Category 3: Logical Errors vs Category 4: Technical Errors:**
  r = 0.539 ***, y = 0.210x + -1.8

**2b: Spurious Numeric vs 4c: Visual Descr Mismatch:**
  r = 0.531 ***, y = 0.033x + -0.1

**Category 4: Technical Errors vs 3a: Unsupported Leap:**
  r = 0.507 ***, y = 1.114x + 12.5

**1b: Context Omission vs 3c: Circular Reasoning:**
  r = 0.477 ***, y = 0.019x + -0.0

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.463 ***, y = 0.560x + 11.1

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
