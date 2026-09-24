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
- Correlation: -0.254 *
- Linear fit: y = -0.168x + 8.3
- P-value: 0.0292
- N samples: 74

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.163 
- Linear fit: y = 1.450x + 2.0
- P-value: 0.1648
- N samples: 74

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.002 
- Linear fit: y = -0.021x + 2.7
- P-value: 0.9869
- N samples: 74

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.159 
- Linear fit: y = -1.979x + 7.9
- P-value: 0.1761
- N samples: 74

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
- Correlation: 0.052 
- Linear fit: y = 0.803x + 6.4
- P-value: 0.6596
- N samples: 74

**Benchmark Score:**
- Correlation: 0.005 
- Linear fit: y = 0.005x + 6.9
- P-value: 0.9659
- N samples: 74

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.218 
- Linear fit: y = -3.781x + 21.6
- P-value: 0.0618
- N samples: 74

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Benchmark Score:**
- Correlation: -0.171 
- Linear fit: y = -0.222x + 27.2
- P-value: 0.1441
- N samples: 74

**Is Reasoning Model:**
- Correlation: -0.087 
- Linear fit: y = -1.876x + 21.3
- P-value: 0.4593
- N samples: 74

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.220 
- Linear fit: y = -1.553x + 3.2
- P-value: 0.0592
- N samples: 74

**Is Reasoning Model:**
- Correlation: 0.127 
- Linear fit: y = 1.112x + 1.6
- P-value: 0.2798
- N samples: 74

**Benchmark Score:**
- Correlation: 0.114 
- Linear fit: y = 0.060x + 0.5
- P-value: 0.3355
- N samples: 74

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
- Correlation: -0.160 
- Linear fit: y = -5.837x + 34.9
- P-value: 0.1743
- N samples: 74

**Days Since 2024-01-01:**
- Correlation: -0.139 
- Linear fit: y = -0.021x + 51.2
- P-value: 0.3022
- N samples: 57

**Benchmark Score:**
- Correlation: -0.120 
- Linear fit: y = -0.327x + 43.1
- P-value: 0.3085
- N samples: 74

**Model Size (B):**
- Correlation: -0.066 
- Linear fit: y = -0.001x + 34.3
- P-value: 0.6271
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.005 
- Linear fit: y = 0.221x + 32.1
- P-value: 0.9670
- N samples: 74

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.254 *
- Linear fit: y = -0.168x + 8.3
- P-value: 0.0292
- N samples: 74

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.163 
- Linear fit: y = 1.450x + 2.0
- P-value: 0.1648
- N samples: 74

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.002 
- Linear fit: y = -0.021x + 2.7
- P-value: 0.9869
- N samples: 74

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.159 
- Linear fit: y = -1.979x + 7.9
- P-value: 0.1761
- N samples: 74

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
- Correlation: 0.052 
- Linear fit: y = 0.803x + 6.4
- P-value: 0.6596
- N samples: 74

**Benchmark Score:**
- Correlation: 0.005 
- Linear fit: y = 0.005x + 6.9
- P-value: 0.9659
- N samples: 74

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.218 
- Linear fit: y = -3.781x + 21.6
- P-value: 0.0618
- N samples: 74

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Benchmark Score:**
- Correlation: -0.171 
- Linear fit: y = -0.222x + 27.2
- P-value: 0.1441
- N samples: 74

**Is Reasoning Model:**
- Correlation: -0.087 
- Linear fit: y = -1.876x + 21.3
- P-value: 0.4593
- N samples: 74

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.220 
- Linear fit: y = -1.553x + 3.2
- P-value: 0.0592
- N samples: 74

**Is Reasoning Model:**
- Correlation: 0.127 
- Linear fit: y = 1.112x + 1.6
- P-value: 0.2798
- N samples: 74

**Benchmark Score:**
- Correlation: 0.114 
- Linear fit: y = 0.060x + 0.5
- P-value: 0.3355
- N samples: 74

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
- Correlation: -0.208 
- Linear fit: y = -0.041x + 1.9
- P-value: 0.0746
- N samples: 74

**Model Size (B):**
- Correlation: -0.185 
- Linear fit: y = -0.000x + 0.9
- P-value: 0.1684
- N samples: 57

**Is Open Source:**
- Correlation: 0.141 
- Linear fit: y = 0.369x + 0.4
- P-value: 0.2306
- N samples: 74

**Days Since 2024-01-01:**
- Correlation: -0.128 
- Linear fit: y = -0.001x + 1.9
- P-value: 0.3415
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.054 
- Linear fit: y = -0.174x + 0.7
- P-value: 0.6499
- N samples: 74

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.182 
- Linear fit: y = -0.076x + 4.0
- P-value: 0.1217
- N samples: 74

**Is Open Source:**
- Correlation: 0.164 
- Linear fit: y = 0.925x + 1.1
- P-value: 0.1626
- N samples: 74

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
- Correlation: 0.066 
- Linear fit: y = 0.460x + 1.1
- P-value: 0.5776
- N samples: 74

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.197 
- Linear fit: y = -0.051x + 2.3
- P-value: 0.0923
- N samples: 74

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
- Correlation: -0.071 
- Linear fit: y = -0.307x + 0.9
- P-value: 0.5453
- N samples: 74

**Is Open Source:**
- Correlation: 0.045 
- Linear fit: y = 0.156x + 0.6
- P-value: 0.7040
- N samples: 74

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.101 
- Linear fit: y = -0.266x + 1.3
- P-value: 0.3925
- N samples: 74

**Model Size (B):**
- Correlation: -0.094 
- Linear fit: y = -0.000x + 1.3
- P-value: 0.4845
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.078 
- Linear fit: y = 0.254x + 1.0
- P-value: 0.5104
- N samples: 74

**Benchmark Score:**
- Correlation: 0.070 
- Linear fit: y = 0.014x + 0.7
- P-value: 0.5530
- N samples: 74

**Days Since 2024-01-01:**
- Correlation: 0.001 
- Linear fit: y = 0.000x + 1.2
- P-value: 0.9964
- N samples: 57

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.107 
- Linear fit: y = -1.228x + 5.9
- P-value: 0.3651
- N samples: 74

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
- Correlation: -0.058 
- Linear fit: y = -0.050x + 7.0
- P-value: 0.6211
- N samples: 74

**Is Reasoning Model:**
- Correlation: 0.010 
- Linear fit: y = 0.139x + 5.2
- P-value: 0.9343
- N samples: 74

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: 0.353 **
- Linear fit: y = 0.041x + -0.8
- P-value: 0.0020
- N samples: 74

**Is Open Source:**
- Correlation: -0.312 **
- Linear fit: y = -0.485x + 0.7
- P-value: 0.0068
- N samples: 74

**Model Size (B):**
- Correlation: 0.249 
- Linear fit: y = 0.000x + 0.3
- P-value: 0.0617
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.213 
- Linear fit: y = 0.410x + 0.2
- P-value: 0.0688
- N samples: 74

**Days Since 2024-01-01:**
- Correlation: 0.131 
- Linear fit: y = 0.001x + -0.2
- P-value: 0.3322
- N samples: 57

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.215 
- Linear fit: y = -3.159x + 17.1
- P-value: 0.0656
- N samples: 74

**Days Since 2024-01-01:**
- Correlation: -0.176 
- Linear fit: y = -0.011x + 25.5
- P-value: 0.1905
- N samples: 57

**Benchmark Score:**
- Correlation: -0.163 
- Linear fit: y = -0.178x + 21.6
- P-value: 0.1665
- N samples: 74

**Is Reasoning Model:**
- Correlation: -0.047 
- Linear fit: y = -0.859x + 16.3
- P-value: 0.6897
- N samples: 74

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
- Correlation: -0.180 
- Linear fit: y = -1.034x + 5.0
- P-value: 0.1259
- N samples: 74

**Is Open Source:**
- Correlation: -0.140 
- Linear fit: y = -0.651x + 4.5
- P-value: 0.2334
- N samples: 74

**Benchmark Score:**
- Correlation: -0.121 
- Linear fit: y = -0.042x + 5.6
- P-value: 0.3049
- N samples: 74

**Model Size (B):**
- Correlation: -0.026 
- Linear fit: y = -0.000x + 4.3
- P-value: 0.8462
- N samples: 57

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.127 
- Linear fit: y = 0.029x + 0.0
- P-value: 0.2811
- N samples: 74

**Benchmark Score:**
- Correlation: -0.099 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.3999
- N samples: 74

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
- Correlation: 0.059 
- Linear fit: y = 0.017x + 0.0
- P-value: 0.6175
- N samples: 74

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: 0.144 
- Linear fit: y = 0.748x + 0.1
- P-value: 0.2209
- N samples: 74

**Is Open Source:**
- Correlation: -0.114 
- Linear fit: y = -0.479x + 0.9
- P-value: 0.3317
- N samples: 74

**Benchmark Score:**
- Correlation: 0.102 
- Linear fit: y = 0.032x + -0.3
- P-value: 0.3877
- N samples: 74

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
- Correlation: -0.222 
- Linear fit: y = -1.007x + 2.1
- P-value: 0.0574
- N samples: 74

**Model Size (B):**
- Correlation: 0.116 
- Linear fit: y = 0.000x + 1.5
- P-value: 0.3908
- N samples: 57

**Benchmark Score:**
- Correlation: 0.093 
- Linear fit: y = 0.032x + 0.6
- P-value: 0.4283
- N samples: 74

**Is Reasoning Model:**
- Correlation: 0.073 
- Linear fit: y = 0.412x + 1.3
- P-value: 0.5348
- N samples: 74

**Days Since 2024-01-01:**
- Correlation: 0.068 
- Linear fit: y = 0.001x + 0.6
- P-value: 0.6164
- N samples: 57

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.088 
- Linear fit: y = -0.066x + 0.1
- P-value: 0.4547
- N samples: 74

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.6113
- N samples: 57

**Benchmark Score:**
- Correlation: -0.068 
- Linear fit: y = -0.004x + 0.2
- P-value: 0.5644
- N samples: 74

**Days Since 2024-01-01:**
- Correlation: -0.066 
- Linear fit: y = -0.000x + 0.3
- P-value: 0.6241
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.052 
- Linear fit: y = -0.049x + 0.1
- P-value: 0.6583
- N samples: 74

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**2c_false_citation vs Benchmark Score:**
  r = 0.353, y = 0.041x + -0.8

**2c_false_citation vs Is Open Source:**
  r = -0.312, y = -0.485x + 0.7


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
- Linear fit: y = 0.579x + 5.5

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.441 ***
- Linear fit: y = 0.860x + 17.5

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.382 ***
- Linear fit: y = 0.303x + 1.7

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.485 ***
- Linear fit: y = 0.674x + 15.1

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.621 ***
- Linear fit: y = 0.352x + 0.0

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.537 ***
- Linear fit: y = 0.218x + -1.8

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.972 ***, y = 0.898x + -1.0

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.972 ***, y = 0.823x + -0.7

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.834 ***, y = 0.530x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.805 ***, y = 0.519x + 0.4

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.737 ***, y = 0.438x + -0.4

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.717 ***, y = 0.211x + 0.0

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.663 ***, y = 0.259x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.649 ***, y = 0.174x + 0.7

**Category 2: Factual Errors vs 4b: Model Semantics Breach:**
  r = 0.638 ***, y = 0.233x + 0.0

**Category 2: Factual Errors vs Category 4: Technical Errors:**
  r = 0.621 ***, y = 0.352x + 0.0

**Category 2: Factual Errors vs 4c: Visual Descr Mismatch:**
  r = 0.604 ***, y = 0.036x + -0.2

**Category 3: Logical Errors vs 4b: Model Semantics Breach:**
  r = 0.589 ***, y = 0.154x + -1.4

**Category 4: Technical Errors vs 2b: Spurious Numeric:**
  r = 0.587 ***, y = 0.958x + 2.9

**2b: Spurious Numeric vs 4b: Model Semantics Breach:**
  r = 0.587 ***, y = 0.232x + 0.4

**3a: Unsupported Leap vs 4b: Model Semantics Breach:**
  r = 0.573 ***, y = 0.177x + -1.1

**2b: Spurious Numeric vs 4c: Visual Descr Mismatch:**
  r = 0.560 ***, y = 0.037x + -0.1

**Category 3: Logical Errors vs Category 4: Technical Errors:**
  r = 0.537 ***, y = 0.218x + -1.8

**Category 4: Technical Errors vs 3a: Unsupported Leap:**
  r = 0.502 ***, y = 1.046x + 13.0

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.487 ***, y = 0.574x + 11.6

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.485 ***, y = 0.674x + 15.1

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
