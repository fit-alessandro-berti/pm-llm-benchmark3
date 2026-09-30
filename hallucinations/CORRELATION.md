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
- Correlation: -0.264 *
- Linear fit: y = -0.172x + 8.4
- P-value: 0.0212
- N samples: 76

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.189 
- Linear fit: y = 1.676x + 1.9
- P-value: 0.1012
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.004 
- Linear fit: y = 0.042x + 2.6
- P-value: 0.9735
- N samples: 76

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.133 
- Linear fit: y = -1.653x + 7.7
- P-value: 0.2511
- N samples: 76

**Is Reasoning Model:**
- Correlation: 0.070 
- Linear fit: y = 1.062x + 6.2
- P-value: 0.5454
- N samples: 76

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
- Correlation: 0.006 
- Linear fit: y = 0.005x + 6.9
- P-value: 0.9609
- N samples: 76

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Benchmark Score:**
- Correlation: -0.200 
- Linear fit: y = -0.259x + 28.3
- P-value: 0.0832
- N samples: 76

**Is Open Source:**
- Correlation: -0.180 
- Linear fit: y = -3.159x + 21.0
- P-value: 0.1194
- N samples: 76

**Is Reasoning Model:**
- Correlation: -0.087 
- Linear fit: y = -1.846x + 21.1
- P-value: 0.4570
- N samples: 76

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.182 
- Linear fit: y = -1.280x + 3.0
- P-value: 0.1159
- N samples: 76

**Is Reasoning Model:**
- Correlation: 0.136 
- Linear fit: y = 1.167x + 1.5
- P-value: 0.2401
- N samples: 76

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Benchmark Score:**
- Correlation: 0.089 
- Linear fit: y = 0.046x + 0.9
- P-value: 0.4448
- N samples: 76

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
- Correlation: -0.142 
- Linear fit: y = -0.382x + 44.7
- P-value: 0.2223
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: -0.139 
- Linear fit: y = -0.021x + 51.2
- P-value: 0.3022
- N samples: 57

**Is Open Source:**
- Correlation: -0.120 
- Linear fit: y = -4.374x + 33.8
- P-value: 0.3036
- N samples: 76

**Model Size (B):**
- Correlation: -0.066 
- Linear fit: y = -0.001x + 34.3
- P-value: 0.6271
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.014 
- Linear fit: y = 0.625x + 31.4
- P-value: 0.9041
- N samples: 76

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.264 *
- Linear fit: y = -0.172x + 8.4
- P-value: 0.0212
- N samples: 76

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.189 
- Linear fit: y = 1.676x + 1.9
- P-value: 0.1012
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.004 
- Linear fit: y = 0.042x + 2.6
- P-value: 0.9735
- N samples: 76

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.133 
- Linear fit: y = -1.653x + 7.7
- P-value: 0.2511
- N samples: 76

**Is Reasoning Model:**
- Correlation: 0.070 
- Linear fit: y = 1.062x + 6.2
- P-value: 0.5454
- N samples: 76

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
- Correlation: 0.006 
- Linear fit: y = 0.005x + 6.9
- P-value: 0.9609
- N samples: 76

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Benchmark Score:**
- Correlation: -0.200 
- Linear fit: y = -0.259x + 28.3
- P-value: 0.0832
- N samples: 76

**Is Open Source:**
- Correlation: -0.180 
- Linear fit: y = -3.159x + 21.0
- P-value: 0.1194
- N samples: 76

**Is Reasoning Model:**
- Correlation: -0.087 
- Linear fit: y = -1.846x + 21.1
- P-value: 0.4570
- N samples: 76

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.182 
- Linear fit: y = -1.280x + 3.0
- P-value: 0.1159
- N samples: 76

**Is Reasoning Model:**
- Correlation: 0.136 
- Linear fit: y = 1.167x + 1.5
- P-value: 0.2401
- N samples: 76

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Benchmark Score:**
- Correlation: 0.089 
- Linear fit: y = 0.046x + 0.9
- P-value: 0.4448
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: 0.063 
- Linear fit: y = 0.002x + 1.1
- P-value: 0.6402
- N samples: 57

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.218 
- Linear fit: y = -0.042x + 2.0
- P-value: 0.0585
- N samples: 76

**Model Size (B):**
- Correlation: -0.185 
- Linear fit: y = -0.000x + 0.9
- P-value: 0.1684
- N samples: 57

**Is Open Source:**
- Correlation: 0.162 
- Linear fit: y = 0.423x + 0.4
- P-value: 0.1610
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: -0.128 
- Linear fit: y = -0.001x + 1.9
- P-value: 0.3415
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.043 
- Linear fit: y = -0.138x + 0.7
- P-value: 0.7094
- N samples: 76

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.190 
- Linear fit: y = -0.078x + 4.1
- P-value: 0.1006
- N samples: 76

**Is Open Source:**
- Correlation: 0.185 
- Linear fit: y = 1.037x + 1.0
- P-value: 0.1096
- N samples: 76

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
- Correlation: 0.065 
- Linear fit: y = 0.442x + 1.1
- P-value: 0.5782
- N samples: 76

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.204 
- Linear fit: y = -0.052x + 2.3
- P-value: 0.0770
- N samples: 76

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
- Correlation: -0.063 
- Linear fit: y = -0.263x + 0.8
- P-value: 0.5912
- N samples: 76

**Is Open Source:**
- Correlation: 0.063 
- Linear fit: y = 0.216x + 0.5
- P-value: 0.5916
- N samples: 76

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: 0.098 
- Linear fit: y = 0.313x + 0.9
- P-value: 0.4015
- N samples: 76

**Model Size (B):**
- Correlation: -0.094 
- Linear fit: y = -0.000x + 1.3
- P-value: 0.4845
- N samples: 57

**Is Open Source:**
- Correlation: -0.063 
- Linear fit: y = -0.165x + 1.3
- P-value: 0.5909
- N samples: 76

**Benchmark Score:**
- Correlation: 0.054 
- Linear fit: y = 0.011x + 0.8
- P-value: 0.6413
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: 0.001 
- Linear fit: y = 0.000x + 1.2
- P-value: 0.9964
- N samples: 57

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.086 
- Linear fit: y = -0.987x + 5.7
- P-value: 0.4598
- N samples: 76

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

**Benchmark Score:**
- Correlation: -0.052 
- Linear fit: y = -0.044x + 6.8
- P-value: 0.6539
- N samples: 76

**Is Reasoning Model:**
- Correlation: 0.029 
- Linear fit: y = 0.400x + 5.0
- P-value: 0.8056
- N samples: 76

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: 0.340 **
- Linear fit: y = 0.039x + -0.8
- P-value: 0.0027
- N samples: 76

**Is Open Source:**
- Correlation: -0.323 **
- Linear fit: y = -0.502x + 0.7
- P-value: 0.0044
- N samples: 76

**Model Size (B):**
- Correlation: 0.249 
- Linear fit: y = 0.000x + 0.3
- P-value: 0.0617
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.186 
- Linear fit: y = 0.350x + 0.2
- P-value: 0.1086
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: 0.131 
- Linear fit: y = 0.001x + -0.2
- P-value: 0.3322
- N samples: 57

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.186 
- Linear fit: y = -0.203x + 22.3
- P-value: 0.1068
- N samples: 76

**Is Open Source:**
- Correlation: -0.182 
- Linear fit: y = -2.681x + 16.7
- P-value: 0.1166
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: -0.176 
- Linear fit: y = -0.011x + 25.5
- P-value: 0.1905
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.049 
- Linear fit: y = -0.888x + 16.2
- P-value: 0.6716
- N samples: 76

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
- Correlation: -0.170 
- Linear fit: y = -0.975x + 4.9
- P-value: 0.1419
- N samples: 76

**Benchmark Score:**
- Correlation: -0.155 
- Linear fit: y = -0.054x + 5.9
- P-value: 0.1822
- N samples: 76

**Is Open Source:**
- Correlation: -0.108 
- Linear fit: y = -0.507x + 4.3
- P-value: 0.3549
- N samples: 76

**Model Size (B):**
- Correlation: -0.026 
- Linear fit: y = -0.000x + 4.3
- P-value: 0.8462
- N samples: 57

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.132 
- Linear fit: y = 0.030x + -0.0
- P-value: 0.2564
- N samples: 76

**Benchmark Score:**
- Correlation: -0.101 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.3853
- N samples: 76

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
- Correlation: 0.060 
- Linear fit: y = 0.017x + -0.0
- P-value: 0.6089
- N samples: 76

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: 0.147 
- Linear fit: y = 0.742x + 0.1
- P-value: 0.2066
- N samples: 76

**Is Open Source:**
- Correlation: -0.096 
- Linear fit: y = -0.399x + 0.9
- P-value: 0.4104
- N samples: 76

**Benchmark Score:**
- Correlation: 0.089 
- Linear fit: y = 0.027x + -0.2
- P-value: 0.4444
- N samples: 76

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
- Correlation: -0.182 
- Linear fit: y = -0.825x + 2.0
- P-value: 0.1156
- N samples: 76

**Model Size (B):**
- Correlation: 0.116 
- Linear fit: y = 0.000x + 1.5
- P-value: 0.3908
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.085 
- Linear fit: y = 0.467x + 1.2
- P-value: 0.4672
- N samples: 76

**Benchmark Score:**
- Correlation: 0.069 
- Linear fit: y = 0.023x + 0.9
- P-value: 0.5563
- N samples: 76

**Days Since 2024-01-01:**
- Correlation: 0.068 
- Linear fit: y = 0.001x + 0.6
- P-value: 0.6164
- N samples: 57

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.075 
- Linear fit: y = -0.056x + 0.1
- P-value: 0.5210
- N samples: 76

**Benchmark Score:**
- Correlation: -0.075 
- Linear fit: y = -0.004x + 0.2
- P-value: 0.5222
- N samples: 76

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
- Correlation: -0.046 
- Linear fit: y = -0.042x + 0.1
- P-value: 0.6930
- N samples: 76

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**2c_false_citation vs Benchmark Score:**
  r = 0.340, y = 0.039x + -0.8

**2c_false_citation vs Is Open Source:**
  r = -0.323, y = -0.502x + 0.7


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
- Correlation: 0.410 ***
- Linear fit: y = 0.575x + 5.5

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.446 ***
- Linear fit: y = 0.884x + 17.3

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.387 ***
- Linear fit: y = 0.308x + 1.6

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.465 ***
- Linear fit: y = 0.657x + 15.0

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.616 ***
- Linear fit: y = 0.349x + -0.0

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.542 ***
- Linear fit: y = 0.217x + -1.8

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.972 ***, y = 0.899x + -1.0

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.972 ***, y = 0.819x + -0.6

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.835 ***, y = 0.529x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.808 ***, y = 0.520x + 0.4

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.737 ***, y = 0.436x + -0.3

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.719 ***, y = 0.212x + 0.0

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.665 ***, y = 0.259x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.663 ***, y = 0.178x + 0.6

**Category 2: Factual Errors vs 4b: Model Semantics Breach:**
  r = 0.633 ***, y = 0.231x + -0.0

**Category 2: Factual Errors vs Category 4: Technical Errors:**
  r = 0.616 ***, y = 0.349x + -0.0

**Category 2: Factual Errors vs 4c: Visual Descr Mismatch:**
  r = 0.602 ***, y = 0.036x + -0.2

**Category 3: Logical Errors vs 4b: Model Semantics Breach:**
  r = 0.592 ***, y = 0.153x + -1.4

**Category 4: Technical Errors vs 2b: Spurious Numeric:**
  r = 0.579 ***, y = 0.944x + 3.0

**2b: Spurious Numeric vs 4b: Model Semantics Breach:**
  r = 0.579 ***, y = 0.229x + 0.4

**3a: Unsupported Leap vs 4b: Model Semantics Breach:**
  r = 0.577 ***, y = 0.177x + -1.1

**2b: Spurious Numeric vs 4c: Visual Descr Mismatch:**
  r = 0.557 ***, y = 0.036x + -0.1

**Category 3: Logical Errors vs Category 4: Technical Errors:**
  r = 0.542 ***, y = 0.217x + -1.8

**Category 4: Technical Errors vs 3a: Unsupported Leap:**
  r = 0.507 ***, y = 1.065x + 12.9

**1b: Context Omission vs 3c: Circular Reasoning:**
  r = 0.479 ***, y = 0.020x + -0.0

**Category 1: Input Misalignment vs 3a: Unsupported Leap:**
  r = 0.472 ***, y = 0.788x + 13.4

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
