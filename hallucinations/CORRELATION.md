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
- Correlation: -0.266 *
- Linear fit: y = -0.174x + 8.4
- P-value: 0.0185
- N samples: 78

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.184 
- Linear fit: y = 1.614x + 1.9
- P-value: 0.1068
- N samples: 78

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.004 
- Linear fit: y = -0.044x + 2.6
- P-value: 0.9715
- N samples: 78

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.124 
- Linear fit: y = -1.525x + 7.6
- P-value: 0.2792
- N samples: 78

**Is Reasoning Model:**
- Correlation: 0.063 
- Linear fit: y = 0.958x + 6.2
- P-value: 0.5812
- N samples: 78

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
- Correlation: 0.003 
- Linear fit: y = 0.003x + 6.9
- P-value: 0.9785
- N samples: 78

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Benchmark Score:**
- Correlation: -0.198 
- Linear fit: y = -0.257x + 28.2
- P-value: 0.0825
- N samples: 78

**Is Open Source:**
- Correlation: -0.159 
- Linear fit: y = -2.759x + 20.8
- P-value: 0.1657
- N samples: 78

**Is Reasoning Model:**
- Correlation: -0.085 
- Linear fit: y = -1.821x + 21.1
- P-value: 0.4585
- N samples: 78

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.181 
- Linear fit: y = -1.262x + 2.9
- P-value: 0.1135
- N samples: 78

**Is Reasoning Model:**
- Correlation: 0.126 
- Linear fit: y = 1.081x + 1.5
- P-value: 0.2718
- N samples: 78

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Benchmark Score:**
- Correlation: 0.084 
- Linear fit: y = 0.044x + 0.9
- P-value: 0.4628
- N samples: 78

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
- Correlation: -0.143 
- Linear fit: y = -0.387x + 44.7
- P-value: 0.2116
- N samples: 78

**Days Since 2024-01-01:**
- Correlation: -0.139 
- Linear fit: y = -0.021x + 51.2
- P-value: 0.3022
- N samples: 57

**Is Open Source:**
- Correlation: -0.107 
- Linear fit: y = -3.893x + 33.4
- P-value: 0.3496
- N samples: 78

**Model Size (B):**
- Correlation: -0.066 
- Linear fit: y = -0.001x + 34.3
- P-value: 0.6271
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.008 
- Linear fit: y = 0.367x + 31.4
- P-value: 0.9429
- N samples: 78

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.266 *
- Linear fit: y = -0.174x + 8.4
- P-value: 0.0185
- N samples: 78

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.184 
- Linear fit: y = 1.614x + 1.9
- P-value: 0.1068
- N samples: 78

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.004 
- Linear fit: y = -0.044x + 2.6
- P-value: 0.9715
- N samples: 78

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.124 
- Linear fit: y = -1.525x + 7.6
- P-value: 0.2792
- N samples: 78

**Is Reasoning Model:**
- Correlation: 0.063 
- Linear fit: y = 0.958x + 6.2
- P-value: 0.5812
- N samples: 78

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
- Correlation: 0.003 
- Linear fit: y = 0.003x + 6.9
- P-value: 0.9785
- N samples: 78

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Benchmark Score:**
- Correlation: -0.198 
- Linear fit: y = -0.257x + 28.2
- P-value: 0.0825
- N samples: 78

**Is Open Source:**
- Correlation: -0.159 
- Linear fit: y = -2.759x + 20.8
- P-value: 0.1657
- N samples: 78

**Is Reasoning Model:**
- Correlation: -0.085 
- Linear fit: y = -1.821x + 21.1
- P-value: 0.4585
- N samples: 78

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.181 
- Linear fit: y = -1.262x + 2.9
- P-value: 0.1135
- N samples: 78

**Is Reasoning Model:**
- Correlation: 0.126 
- Linear fit: y = 1.081x + 1.5
- P-value: 0.2718
- N samples: 78

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Benchmark Score:**
- Correlation: 0.084 
- Linear fit: y = 0.044x + 0.9
- P-value: 0.4628
- N samples: 78

**Days Since 2024-01-01:**
- Correlation: 0.063 
- Linear fit: y = 0.002x + 1.1
- P-value: 0.6402
- N samples: 57

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.220 
- Linear fit: y = -0.042x + 2.0
- P-value: 0.0531
- N samples: 78

**Model Size (B):**
- Correlation: -0.185 
- Linear fit: y = -0.000x + 0.9
- P-value: 0.1684
- N samples: 57

**Is Open Source:**
- Correlation: 0.158 
- Linear fit: y = 0.408x + 0.4
- P-value: 0.1662
- N samples: 78

**Days Since 2024-01-01:**
- Correlation: -0.128 
- Linear fit: y = -0.001x + 1.9
- P-value: 0.3415
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.049 
- Linear fit: y = -0.155x + 0.7
- P-value: 0.6695
- N samples: 78

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.192 
- Linear fit: y = -0.080x + 4.1
- P-value: 0.0922
- N samples: 78

**Is Open Source:**
- Correlation: 0.180 
- Linear fit: y = 1.000x + 1.0
- P-value: 0.1146
- N samples: 78

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
- Correlation: 0.057 
- Linear fit: y = 0.391x + 1.1
- P-value: 0.6179
- N samples: 78

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.206 
- Linear fit: y = -0.052x + 2.3
- P-value: 0.0708
- N samples: 78

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
- Correlation: -0.067 
- Linear fit: y = -0.280x + 0.8
- P-value: 0.5603
- N samples: 78

**Is Open Source:**
- Correlation: 0.060 
- Linear fit: y = 0.206x + 0.5
- P-value: 0.5994
- N samples: 78

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: 0.099 
- Linear fit: y = 0.321x + 0.9
- P-value: 0.3899
- N samples: 78

**Model Size (B):**
- Correlation: -0.094 
- Linear fit: y = -0.000x + 1.3
- P-value: 0.4845
- N samples: 57

**Benchmark Score:**
- Correlation: 0.056 
- Linear fit: y = 0.011x + 0.8
- P-value: 0.6289
- N samples: 78

**Is Open Source:**
- Correlation: -0.030 
- Linear fit: y = -0.080x + 1.2
- P-value: 0.7921
- N samples: 78

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
- Linear fit: y = -0.983x + 5.7
- P-value: 0.4515
- N samples: 78

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
- Correlation: -0.055 
- Linear fit: y = -0.047x + 6.8
- P-value: 0.6302
- N samples: 78

**Is Reasoning Model:**
- Correlation: 0.021 
- Linear fit: y = 0.290x + 5.0
- P-value: 0.8565
- N samples: 78

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: 0.338 **
- Linear fit: y = 0.039x + -0.8
- P-value: 0.0025
- N samples: 78

**Is Open Source:**
- Correlation: -0.300 **
- Linear fit: y = -0.463x + 0.7
- P-value: 0.0075
- N samples: 78

**Model Size (B):**
- Correlation: 0.249 
- Linear fit: y = 0.000x + 0.3
- P-value: 0.0617
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.183 
- Linear fit: y = 0.347x + 0.3
- P-value: 0.1079
- N samples: 78

**Days Since 2024-01-01:**
- Correlation: 0.131 
- Linear fit: y = 0.001x + -0.2
- P-value: 0.3322
- N samples: 57

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.182 
- Linear fit: y = -0.200x + 22.3
- P-value: 0.1107
- N samples: 78

**Days Since 2024-01-01:**
- Correlation: -0.176 
- Linear fit: y = -0.011x + 25.5
- P-value: 0.1905
- N samples: 57

**Is Open Source:**
- Correlation: -0.153 
- Linear fit: y = -2.258x + 16.5
- P-value: 0.1806
- N samples: 78

**Is Reasoning Model:**
- Correlation: -0.045 
- Linear fit: y = -0.817x + 16.2
- P-value: 0.6949
- N samples: 78

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
- Correlation: -0.177 
- Linear fit: y = -1.020x + 4.9
- P-value: 0.1203
- N samples: 78

**Benchmark Score:**
- Correlation: -0.158 
- Linear fit: y = -0.055x + 5.9
- P-value: 0.1680
- N samples: 78

**Is Open Source:**
- Correlation: -0.113 
- Linear fit: y = -0.531x + 4.3
- P-value: 0.3232
- N samples: 78

**Model Size (B):**
- Correlation: -0.026 
- Linear fit: y = -0.000x + 4.3
- P-value: 0.8462
- N samples: 57

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.130 
- Linear fit: y = 0.029x + 0.0
- P-value: 0.2579
- N samples: 78

**Benchmark Score:**
- Correlation: -0.102 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.3761
- N samples: 78

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
- Correlation: 0.058 
- Linear fit: y = 0.016x + 0.0
- P-value: 0.6146
- N samples: 78

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: 0.141 
- Linear fit: y = 0.714x + 0.1
- P-value: 0.2173
- N samples: 78

**Is Open Source:**
- Correlation: -0.096 
- Linear fit: y = -0.393x + 0.9
- P-value: 0.4054
- N samples: 78

**Benchmark Score:**
- Correlation: 0.087 
- Linear fit: y = 0.027x + -0.2
- P-value: 0.4496
- N samples: 78

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
- Correlation: -0.181 
- Linear fit: y = -0.814x + 1.9
- P-value: 0.1132
- N samples: 78

**Model Size (B):**
- Correlation: 0.116 
- Linear fit: y = 0.000x + 1.5
- P-value: 0.3908
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.074 
- Linear fit: y = 0.411x + 1.3
- P-value: 0.5176
- N samples: 78

**Days Since 2024-01-01:**
- Correlation: 0.068 
- Linear fit: y = 0.001x + 0.6
- P-value: 0.6164
- N samples: 57

**Benchmark Score:**
- Correlation: 0.064 
- Linear fit: y = 0.021x + 0.9
- P-value: 0.5783
- N samples: 78

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.076 
- Linear fit: y = -0.004x + 0.2
- P-value: 0.5091
- N samples: 78

**Is Open Source:**
- Correlation: -0.075 
- Linear fit: y = -0.055x + 0.1
- P-value: 0.5166
- N samples: 78

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
- Correlation: -0.049 
- Linear fit: y = -0.044x + 0.1
- P-value: 0.6694
- N samples: 78

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**2c_false_citation vs Benchmark Score:**
  r = 0.338, y = 0.039x + -0.8

**2c_false_citation vs Is Open Source:**
  r = -0.300, y = -0.463x + 0.7


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
- Correlation: 0.414 ***
- Linear fit: y = 0.580x + 5.4

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.440 ***
- Linear fit: y = 0.874x + 17.4

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.394 ***
- Linear fit: y = 0.314x + 1.5

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.465 ***
- Linear fit: y = 0.659x + 15.0

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.618 ***
- Linear fit: y = 0.351x + -0.1

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.534 ***
- Linear fit: y = 0.214x + -1.8

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.971 ***, y = 0.823x + -0.6

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.971 ***, y = 0.897x + -1.0

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.836 ***, y = 0.530x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.810 ***, y = 0.522x + 0.3

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.738 ***, y = 0.434x + -0.3

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.721 ***, y = 0.212x + 0.0

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.666 ***, y = 0.259x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.650 ***, y = 0.175x + 0.6

**Category 2: Factual Errors vs 4b: Model Semantics Breach:**
  r = 0.635 ***, y = 0.233x + -0.0

**Category 2: Factual Errors vs Category 4: Technical Errors:**
  r = 0.618 ***, y = 0.351x + -0.1

**Category 2: Factual Errors vs 4c: Visual Descr Mismatch:**
  r = 0.602 ***, y = 0.036x + -0.2

**Category 3: Logical Errors vs 4b: Model Semantics Breach:**
  r = 0.584 ***, y = 0.151x + -1.4

**Category 4: Technical Errors vs 2b: Spurious Numeric:**
  r = 0.584 ***, y = 0.949x + 3.0

**2b: Spurious Numeric vs 4b: Model Semantics Breach:**
  r = 0.583 ***, y = 0.231x + 0.4

**3a: Unsupported Leap vs 4b: Model Semantics Breach:**
  r = 0.562 ***, y = 0.172x + -1.1

**2b: Spurious Numeric vs 4c: Visual Descr Mismatch:**
  r = 0.558 ***, y = 0.036x + -0.1

**Category 3: Logical Errors vs Category 4: Technical Errors:**
  r = 0.534 ***, y = 0.214x + -1.8

**Category 4: Technical Errors vs 3a: Unsupported Leap:**
  r = 0.494 ***, y = 1.042x + 13.1

**1b: Context Omission vs 3c: Circular Reasoning:**
  r = 0.479 ***, y = 0.020x + -0.0

**Category 2: Factual Errors vs 1a: Instruction Override:**
  r = 0.471 ***, y = 0.099x + -0.1

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
