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
- Correlation: -0.237 
- Linear fit: y = -0.162x + 8.2
- P-value: 0.0538
- N samples: 67

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.164 
- Linear fit: y = 1.511x + 2.2
- P-value: 0.1848
- N samples: 67

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.007 
- Linear fit: y = -0.080x + 2.9
- P-value: 0.9549
- N samples: 67

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.190 
- Linear fit: y = -2.453x + 8.4
- P-value: 0.1228
- N samples: 67

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
- Correlation: 0.047 
- Linear fit: y = 0.045x + 5.8
- P-value: 0.7082
- N samples: 67

**Is Reasoning Model:**
- Correlation: 0.043 
- Linear fit: y = 0.682x + 6.7
- P-value: 0.7288
- N samples: 67

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.239 
- Linear fit: y = -4.259x + 22.2
- P-value: 0.0517
- N samples: 67

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Benchmark Score:**
- Correlation: -0.148 
- Linear fit: y = -0.196x + 26.6
- P-value: 0.2322
- N samples: 67

**Is Reasoning Model:**
- Correlation: -0.082 
- Linear fit: y = -1.794x + 21.6
- P-value: 0.5095
- N samples: 67

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.295 *
- Linear fit: y = -2.085x + 3.5
- P-value: 0.0155
- N samples: 67

**Benchmark Score:**
- Correlation: 0.162 
- Linear fit: y = 0.085x + -0.3
- P-value: 0.1905
- N samples: 67

**Is Reasoning Model:**
- Correlation: 0.115 
- Linear fit: y = 1.003x + 1.7
- P-value: 0.3520
- N samples: 67

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

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.193 
- Linear fit: y = -7.260x + 36.4
- P-value: 0.1184
- N samples: 67

**Days Since 2024-01-01:**
- Correlation: -0.139 
- Linear fit: y = -0.021x + 51.2
- P-value: 0.3022
- N samples: 57

**Benchmark Score:**
- Correlation: -0.082 
- Linear fit: y = -0.228x + 40.5
- P-value: 0.5113
- N samples: 67

**Model Size (B):**
- Correlation: -0.066 
- Linear fit: y = -0.001x + 34.3
- P-value: 0.6271
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.001 
- Linear fit: y = 0.038x + 33.0
- P-value: 0.9948
- N samples: 67

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.237 
- Linear fit: y = -0.162x + 8.2
- P-value: 0.0538
- N samples: 67

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.164 
- Linear fit: y = 1.511x + 2.2
- P-value: 0.1848
- N samples: 67

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.007 
- Linear fit: y = -0.080x + 2.9
- P-value: 0.9549
- N samples: 67

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.190 
- Linear fit: y = -2.453x + 8.4
- P-value: 0.1228
- N samples: 67

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
- Correlation: 0.047 
- Linear fit: y = 0.045x + 5.8
- P-value: 0.7082
- N samples: 67

**Is Reasoning Model:**
- Correlation: 0.043 
- Linear fit: y = 0.682x + 6.7
- P-value: 0.7288
- N samples: 67

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.239 
- Linear fit: y = -4.259x + 22.2
- P-value: 0.0517
- N samples: 67

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Benchmark Score:**
- Correlation: -0.148 
- Linear fit: y = -0.196x + 26.6
- P-value: 0.2322
- N samples: 67

**Is Reasoning Model:**
- Correlation: -0.082 
- Linear fit: y = -1.794x + 21.6
- P-value: 0.5095
- N samples: 67

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.295 *
- Linear fit: y = -2.085x + 3.5
- P-value: 0.0155
- N samples: 67

**Benchmark Score:**
- Correlation: 0.162 
- Linear fit: y = 0.085x + -0.3
- P-value: 0.1905
- N samples: 67

**Is Reasoning Model:**
- Correlation: 0.115 
- Linear fit: y = 1.003x + 1.7
- P-value: 0.3520
- N samples: 67

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

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.197 
- Linear fit: y = -0.040x + 1.9
- P-value: 0.1093
- N samples: 67

**Model Size (B):**
- Correlation: -0.185 
- Linear fit: y = -0.000x + 0.9
- P-value: 0.1684
- N samples: 57

**Is Open Source:**
- Correlation: 0.145 
- Linear fit: y = 0.394x + 0.4
- P-value: 0.2427
- N samples: 67

**Days Since 2024-01-01:**
- Correlation: -0.128 
- Linear fit: y = -0.001x + 1.9
- P-value: 0.3415
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.060 
- Linear fit: y = -0.201x + 0.8
- P-value: 0.6291
- N samples: 67

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.174 
- Linear fit: y = 1.018x + 1.1
- P-value: 0.1599
- N samples: 67

**Benchmark Score:**
- Correlation: -0.171 
- Linear fit: y = -0.074x + 4.0
- P-value: 0.1664
- N samples: 67

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
- Linear fit: y = 0.465x + 1.2
- P-value: 0.6031
- N samples: 67

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.193 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.1506
- N samples: 57

**Benchmark Score:**
- Correlation: -0.177 
- Linear fit: y = -0.047x + 2.2
- P-value: 0.1511
- N samples: 67

**Days Since 2024-01-01:**
- Correlation: -0.128 
- Linear fit: y = -0.002x + 2.3
- P-value: 0.3438
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.078 
- Linear fit: y = -0.344x + 0.9
- P-value: 0.5324
- N samples: 67

**Is Open Source:**
- Correlation: 0.027 
- Linear fit: y = 0.099x + 0.6
- P-value: 0.8264
- N samples: 67

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.094 
- Linear fit: y = -0.000x + 1.3
- P-value: 0.4845
- N samples: 57

**Is Open Source:**
- Correlation: -0.070 
- Linear fit: y = -0.162x + 1.2
- P-value: 0.5727
- N samples: 67

**Benchmark Score:**
- Correlation: 0.028 
- Linear fit: y = 0.005x + 1.0
- P-value: 0.8239
- N samples: 67

**Is Reasoning Model:**
- Correlation: 0.021 
- Linear fit: y = 0.061x + 1.1
- P-value: 0.8636
- N samples: 67

**Days Since 2024-01-01:**
- Correlation: 0.001 
- Linear fit: y = 0.000x + 1.2
- P-value: 0.9964
- N samples: 57

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.150 
- Linear fit: y = -1.772x + 6.4
- P-value: 0.2256
- N samples: 67

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

**Is Reasoning Model:**
- Correlation: 0.008 
- Linear fit: y = 0.123x + 5.5
- P-value: 0.9458
- N samples: 67

**Benchmark Score:**
- Correlation: -0.005 
- Linear fit: y = -0.005x + 5.7
- P-value: 0.9668
- N samples: 67

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: 0.373 **
- Linear fit: y = 0.044x + -0.9
- P-value: 0.0019
- N samples: 67

**Is Open Source:**
- Correlation: -0.325 **
- Linear fit: y = -0.520x + 0.8
- P-value: 0.0073
- N samples: 67

**Is Reasoning Model:**
- Correlation: 0.254 *
- Linear fit: y = 0.499x + 0.1
- P-value: 0.0380
- N samples: 67

**Model Size (B):**
- Correlation: 0.249 
- Linear fit: y = 0.000x + 0.3
- P-value: 0.0617
- N samples: 57

**Days Since 2024-01-01:**
- Correlation: 0.131 
- Linear fit: y = 0.001x + -0.2
- P-value: 0.3322
- N samples: 57

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.229 
- Linear fit: y = -3.468x + 17.5
- P-value: 0.0629
- N samples: 67

**Days Since 2024-01-01:**
- Correlation: -0.176 
- Linear fit: y = -0.011x + 25.5
- P-value: 0.1905
- N samples: 57

**Benchmark Score:**
- Correlation: -0.148 
- Linear fit: y = -0.167x + 21.4
- P-value: 0.2306
- N samples: 67

**Is Reasoning Model:**
- Correlation: -0.046 
- Linear fit: y = -0.854x + 16.6
- P-value: 0.7122
- N samples: 67

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

**Is Open Source:**
- Correlation: -0.173 
- Linear fit: y = -0.823x + 4.7
- P-value: 0.1610
- N samples: 67

**Is Reasoning Model:**
- Correlation: -0.164 
- Linear fit: y = -0.958x + 5.1
- P-value: 0.1838
- N samples: 67

**Benchmark Score:**
- Correlation: -0.076 
- Linear fit: y = -0.027x + 5.2
- P-value: 0.5387
- N samples: 67

**Model Size (B):**
- Correlation: -0.026 
- Linear fit: y = -0.000x + 4.3
- P-value: 0.8462
- N samples: 57

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.133 
- Linear fit: y = 0.032x + -0.0
- P-value: 0.2846
- N samples: 67

**Benchmark Score:**
- Correlation: -0.095 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.4435
- N samples: 67

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
- Correlation: 0.063 
- Linear fit: y = 0.019x + -0.0
- P-value: 0.6110
- N samples: 67

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.214 
- Linear fit: y = -0.830x + 1.1
- P-value: 0.0823
- N samples: 67

**Benchmark Score:**
- Correlation: 0.142 
- Linear fit: y = 0.041x + -0.7
- P-value: 0.2504
- N samples: 67

**Is Reasoning Model:**
- Correlation: 0.140 
- Linear fit: y = 0.668x + 0.1
- P-value: 0.2569
- N samples: 67

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
- Correlation: -0.252 *
- Linear fit: y = -1.181x + 2.3
- P-value: 0.0400
- N samples: 67

**Benchmark Score:**
- Correlation: 0.135 
- Linear fit: y = 0.047x + 0.2
- P-value: 0.2750
- N samples: 67

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
- Correlation: 0.066 
- Linear fit: y = 0.383x + 1.4
- P-value: 0.5930
- N samples: 67

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.095 
- Linear fit: y = -0.074x + 0.1
- P-value: 0.4458
- N samples: 67

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

**Benchmark Score:**
- Correlation: -0.053 
- Linear fit: y = -0.003x + 0.2
- P-value: 0.6715
- N samples: 67

**Is Reasoning Model:**
- Correlation: -0.050 
- Linear fit: y = -0.049x + 0.1
- P-value: 0.6855
- N samples: 67

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**2c_false_citation vs Benchmark Score:**
  r = 0.373, y = 0.044x + -0.9

**2c_false_citation vs Is Open Source:**
  r = -0.325, y = -0.520x + 0.8


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
- Correlation: 0.405 ***
- Linear fit: y = 0.566x + 5.6

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.429 ***
- Linear fit: y = 0.830x + 17.8

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.397 ***
- Linear fit: y = 0.305x + 1.6

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.482 ***
- Linear fit: y = 0.667x + 15.4

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.633 ***
- Linear fit: y = 0.348x + -0.0

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.573 ***
- Linear fit: y = 0.228x + -2.1

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.978 ***, y = 0.896x + -0.9

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.972 ***, y = 0.827x + -0.8

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.838 ***, y = 0.556x + 0.3

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.833 ***, y = 0.530x + 0.1

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.724 ***, y = 0.397x + -0.3

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.712 ***, y = 0.211x + 0.0

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.662 ***, y = 0.260x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.641 ***, y = 0.171x + 0.9

**Category 2: Factual Errors vs Category 4: Technical Errors:**
  r = 0.633 ***, y = 0.348x + -0.0

**Category 2: Factual Errors vs 4b: Model Semantics Breach:**
  r = 0.630 ***, y = 0.229x + 0.1

**Category 2: Factual Errors vs 4c: Visual Descr Mismatch:**
  r = 0.606 ***, y = 0.037x + -0.2

**Category 4: Technical Errors vs 2b: Spurious Numeric:**
  r = 0.590 ***, y = 0.984x + 3.1

**Category 3: Logical Errors vs 4b: Model Semantics Breach:**
  r = 0.588 ***, y = 0.155x + -1.4

**2b: Spurious Numeric vs 4b: Model Semantics Breach:**
  r = 0.586 ***, y = 0.233x + 0.4

**Category 3: Logical Errors vs Category 4: Technical Errors:**
  r = 0.573 ***, y = 0.228x + -2.1

**3a: Unsupported Leap vs 4b: Model Semantics Breach:**
  r = 0.573 ***, y = 0.177x + -1.1

**2b: Spurious Numeric vs 4c: Visual Descr Mismatch:**
  r = 0.562 ***, y = 0.037x + -0.1

**Category 4: Technical Errors vs 3a: Unsupported Leap:**
  r = 0.537 ***, y = 1.152x + 13.0

**2a: Concept Fabrication vs 4c: Visual Descr Mismatch:**
  r = 0.535 ***, y = 0.182x + -0.1

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.485 ***, y = 0.571x + 11.8

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
