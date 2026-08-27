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
- Correlation: -0.264 *
- Linear fit: y = -0.009x + 10.3
- P-value: 0.0490
- N samples: 56

**Benchmark Score:**
- Correlation: -0.243 
- Linear fit: y = -0.170x + 7.8
- P-value: 0.0664
- N samples: 58

**Model Size (B):**
- Correlation: -0.227 
- Linear fit: y = -0.001x + 3.3
- P-value: 0.0923
- N samples: 56

**Is Reasoning Model:**
- Correlation: -0.143 
- Linear fit: y = -1.399x + 3.4
- P-value: 0.2831
- N samples: 58

**Is Open Source:**
- Correlation: 0.023 
- Linear fit: y = 0.198x + 2.3
- P-value: 0.8660
- N samples: 58

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.193 
- Linear fit: y = -2.490x + 8.6
- P-value: 0.1470
- N samples: 58

**Model Size (B):**
- Correlation: -0.135 
- Linear fit: y = -0.001x + 8.3
- P-value: 0.3201
- N samples: 56

**Days Since 2024-01-01:**
- Correlation: -0.024 
- Linear fit: y = -0.001x + 8.6
- P-value: 0.8614
- N samples: 56

**Benchmark Score:**
- Correlation: -0.018 
- Linear fit: y = -0.018x + 8.0
- P-value: 0.8952
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.013 
- Linear fit: y = -0.182x + 7.6
- P-value: 0.9254
- N samples: 58

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.383 **
- Linear fit: y = -7.479x + 27.3
- P-value: 0.0030
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.320 *
- Linear fit: y = -6.988x + 28.8
- P-value: 0.0144
- N samples: 58

**Days Since 2024-01-01:**
- Correlation: -0.316 *
- Linear fit: y = -0.025x + 44.9
- P-value: 0.0175
- N samples: 56

**Benchmark Score:**
- Correlation: -0.122 
- Linear fit: y = -0.191x + 29.9
- P-value: 0.3616
- N samples: 58

**Model Size (B):**
- Correlation: 0.031 
- Linear fit: y = 0.000x + 23.7
- P-value: 0.8197
- N samples: 56

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.328 *
- Linear fit: y = -0.008x + 8.3
- P-value: 0.0136
- N samples: 56

**Benchmark Score:**
- Correlation: -0.284 *
- Linear fit: y = -0.135x + 6.0
- P-value: 0.0310
- N samples: 58

**Model Size (B):**
- Correlation: -0.221 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.1009
- N samples: 56

**Is Reasoning Model:**
- Correlation: -0.070 
- Linear fit: y = -0.461x + 1.9
- P-value: 0.6040
- N samples: 58

**Is Open Source:**
- Correlation: -0.022 
- Linear fit: y = -0.131x + 1.7
- P-value: 0.8694
- N samples: 58

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.270 *
- Linear fit: y = -0.043x + 71.9
- P-value: 0.0441
- N samples: 56

**Is Open Source:**
- Correlation: -0.254 
- Linear fit: y = -10.038x + 40.0
- P-value: 0.0539
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.204 
- Linear fit: y = -8.982x + 41.6
- P-value: 0.1252
- N samples: 58

**Benchmark Score:**
- Correlation: -0.158 
- Linear fit: y = -0.501x + 51.3
- P-value: 0.2351
- N samples: 58

**Model Size (B):**
- Correlation: -0.108 
- Linear fit: y = -0.002x + 37.4
- P-value: 0.4263
- N samples: 56

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.264 *
- Linear fit: y = -0.009x + 10.3
- P-value: 0.0490
- N samples: 56

**Benchmark Score:**
- Correlation: -0.243 
- Linear fit: y = -0.170x + 7.8
- P-value: 0.0664
- N samples: 58

**Model Size (B):**
- Correlation: -0.227 
- Linear fit: y = -0.001x + 3.3
- P-value: 0.0923
- N samples: 56

**Is Reasoning Model:**
- Correlation: -0.143 
- Linear fit: y = -1.399x + 3.4
- P-value: 0.2831
- N samples: 58

**Is Open Source:**
- Correlation: 0.023 
- Linear fit: y = 0.198x + 2.3
- P-value: 0.8660
- N samples: 58

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.193 
- Linear fit: y = -2.490x + 8.6
- P-value: 0.1470
- N samples: 58

**Model Size (B):**
- Correlation: -0.135 
- Linear fit: y = -0.001x + 8.3
- P-value: 0.3201
- N samples: 56

**Days Since 2024-01-01:**
- Correlation: -0.024 
- Linear fit: y = -0.001x + 8.6
- P-value: 0.8614
- N samples: 56

**Benchmark Score:**
- Correlation: -0.018 
- Linear fit: y = -0.018x + 8.0
- P-value: 0.8952
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.013 
- Linear fit: y = -0.182x + 7.6
- P-value: 0.9254
- N samples: 58

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.383 **
- Linear fit: y = -7.479x + 27.3
- P-value: 0.0030
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.320 *
- Linear fit: y = -6.988x + 28.8
- P-value: 0.0144
- N samples: 58

**Days Since 2024-01-01:**
- Correlation: -0.316 *
- Linear fit: y = -0.025x + 44.9
- P-value: 0.0175
- N samples: 56

**Benchmark Score:**
- Correlation: -0.122 
- Linear fit: y = -0.191x + 29.9
- P-value: 0.3616
- N samples: 58

**Model Size (B):**
- Correlation: 0.031 
- Linear fit: y = 0.000x + 23.7
- P-value: 0.8197
- N samples: 56

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.328 *
- Linear fit: y = -0.008x + 8.3
- P-value: 0.0136
- N samples: 56

**Benchmark Score:**
- Correlation: -0.284 *
- Linear fit: y = -0.135x + 6.0
- P-value: 0.0310
- N samples: 58

**Model Size (B):**
- Correlation: -0.221 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.1009
- N samples: 56

**Is Reasoning Model:**
- Correlation: -0.070 
- Linear fit: y = -0.461x + 1.9
- P-value: 0.6040
- N samples: 58

**Is Open Source:**
- Correlation: -0.022 
- Linear fit: y = -0.131x + 1.7
- P-value: 0.8694
- N samples: 58

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.225 
- Linear fit: y = -0.004x + 3.9
- P-value: 0.0955
- N samples: 56

**Model Size (B):**
- Correlation: -0.219 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.1051
- N samples: 56

**Is Reasoning Model:**
- Correlation: -0.209 
- Linear fit: y = -0.929x + 1.5
- P-value: 0.1150
- N samples: 58

**Benchmark Score:**
- Correlation: -0.182 
- Linear fit: y = -0.058x + 2.7
- P-value: 0.1716
- N samples: 58

**Is Open Source:**
- Correlation: 0.032 
- Linear fit: y = 0.126x + 0.8
- P-value: 0.8128
- N samples: 58

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.226 
- Linear fit: y = -0.000x + 1.6
- P-value: 0.0938
- N samples: 56

**Benchmark Score:**
- Correlation: -0.205 
- Linear fit: y = -0.072x + 3.5
- P-value: 0.1229
- N samples: 58

**Days Since 2024-01-01:**
- Correlation: -0.203 
- Linear fit: y = -0.004x + 4.3
- P-value: 0.1342
- N samples: 56

**Is Reasoning Model:**
- Correlation: -0.039 
- Linear fit: y = -0.193x + 1.3
- P-value: 0.7694
- N samples: 58

**Is Open Source:**
- Correlation: -0.013 
- Linear fit: y = -0.057x + 1.2
- P-value: 0.9229
- N samples: 58

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.300 *
- Linear fit: y = -0.002x + 2.2
- P-value: 0.0246
- N samples: 56

**Benchmark Score:**
- Correlation: -0.286 *
- Linear fit: y = -0.040x + 1.6
- P-value: 0.0297
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.143 
- Linear fit: y = -0.277x + 0.6
- P-value: 0.2842
- N samples: 58

**Is Open Source:**
- Correlation: 0.074 
- Linear fit: y = 0.129x + 0.3
- P-value: 0.5795
- N samples: 58

**Model Size (B):**
- Correlation: -0.067 
- Linear fit: y = -0.000x + 0.4
- P-value: 0.6228
- N samples: 56

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.257 
- Linear fit: y = -0.000x + 1.7
- P-value: 0.0558
- N samples: 56

**Is Open Source:**
- Correlation: 0.196 
- Linear fit: y = 0.610x + 1.0
- P-value: 0.1414
- N samples: 58

**Benchmark Score:**
- Correlation: -0.133 
- Linear fit: y = -0.033x + 2.4
- P-value: 0.3178
- N samples: 58

**Is Reasoning Model:**
- Correlation: 0.080 
- Linear fit: y = 0.280x + 1.1
- P-value: 0.5492
- N samples: 58

**Days Since 2024-01-01:**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 1.5
- P-value: 0.9352
- N samples: 56

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.257 
- Linear fit: y = -3.119x + 7.3
- P-value: 0.0519
- N samples: 58

**Model Size (B):**
- Correlation: -0.092 
- Linear fit: y = -0.000x + 6.4
- P-value: 0.4991
- N samples: 56

**Days Since 2024-01-01:**
- Correlation: -0.037 
- Linear fit: y = -0.002x + 7.4
- P-value: 0.7875
- N samples: 56

**Is Reasoning Model:**
- Correlation: -0.037 
- Linear fit: y = -0.497x + 6.2
- P-value: 0.7852
- N samples: 58

**Benchmark Score:**
- Correlation: 0.001 
- Linear fit: y = 0.001x + 5.8
- P-value: 0.9959
- N samples: 58

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: 0.185 
- Linear fit: y = 0.014x + -0.2
- P-value: 0.1637
- N samples: 58

**Days Since 2024-01-01:**
- Correlation: 0.181 
- Linear fit: y = 0.001x + -0.3
- P-value: 0.1824
- N samples: 56

**Model Size (B):**
- Correlation: 0.180 
- Linear fit: y = 0.000x + 0.2
- P-value: 0.1839
- N samples: 56

**Is Reasoning Model:**
- Correlation: 0.033 
- Linear fit: y = 0.036x + 0.3
- P-value: 0.8059
- N samples: 58

**Is Open Source:**
- Correlation: 0.020 
- Linear fit: y = 0.019x + 0.3
- P-value: 0.8835
- N samples: 58

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.420 **
- Linear fit: y = -6.421x + 22.6
- P-value: 0.0010
- N samples: 58

**Days Since 2024-01-01:**
- Correlation: -0.321 *
- Linear fit: y = -0.020x + 36.3
- P-value: 0.0159
- N samples: 56

**Is Reasoning Model:**
- Correlation: -0.288 *
- Linear fit: y = -4.920x + 23.1
- P-value: 0.0283
- N samples: 58

**Benchmark Score:**
- Correlation: -0.105 
- Linear fit: y = -0.129x + 23.7
- P-value: 0.4306
- N samples: 58

**Model Size (B):**
- Correlation: 0.071 
- Linear fit: y = 0.000x + 19.3
- P-value: 0.6023
- N samples: 56

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.297 *
- Linear fit: y = -2.030x + 5.6
- P-value: 0.0234
- N samples: 58

**Days Since 2024-01-01:**
- Correlation: -0.217 
- Linear fit: y = -0.005x + 8.6
- P-value: 0.1079
- N samples: 56

**Is Open Source:**
- Correlation: -0.174 
- Linear fit: y = -1.060x + 4.7
- P-value: 0.1925
- N samples: 58

**Benchmark Score:**
- Correlation: -0.118 
- Linear fit: y = -0.058x + 6.0
- P-value: 0.3765
- N samples: 58

**Model Size (B):**
- Correlation: -0.070 
- Linear fit: y = -0.000x + 4.3
- P-value: 0.6080
- N samples: 56

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.139 
- Linear fit: y = -0.004x + 0.2
- P-value: 0.2996
- N samples: 58

**Model Size (B):**
- Correlation: -0.137 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.3131
- N samples: 56

**Is Reasoning Model:**
- Correlation: -0.095 
- Linear fit: y = -0.039x + 0.1
- P-value: 0.4792
- N samples: 58

**Days Since 2024-01-01:**
- Correlation: 0.081 
- Linear fit: y = 0.000x + -0.1
- P-value: 0.5535
- N samples: 56

**Is Open Source:**
- Correlation: 0.007 
- Linear fit: y = 0.002x + 0.0
- P-value: 0.9613
- N samples: 58

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.406 **
- Linear fit: y = -0.005x + 4.3
- P-value: 0.0019
- N samples: 56

**Benchmark Score:**
- Correlation: -0.151 
- Linear fit: y = -0.034x + 1.5
- P-value: 0.2592
- N samples: 58

**Model Size (B):**
- Correlation: -0.144 
- Linear fit: y = -0.000x + 0.6
- P-value: 0.2899
- N samples: 56

**Is Open Source:**
- Correlation: -0.101 
- Linear fit: y = -0.283x + 0.5
- P-value: 0.4504
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.046 
- Linear fit: y = -0.143x + 0.5
- P-value: 0.7341
- N samples: 58

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.289 *
- Linear fit: y = -0.099x + 4.4
- P-value: 0.0277
- N samples: 58

**Model Size (B):**
- Correlation: -0.214 
- Linear fit: y = -0.000x + 1.6
- P-value: 0.1134
- N samples: 56

**Days Since 2024-01-01:**
- Correlation: -0.178 
- Linear fit: y = -0.003x + 3.8
- P-value: 0.1888
- N samples: 56

**Is Reasoning Model:**
- Correlation: -0.059 
- Linear fit: y = -0.280x + 1.4
- P-value: 0.6611
- N samples: 58

**Is Open Source:**
- Correlation: 0.019 
- Linear fit: y = 0.081x + 1.1
- P-value: 0.8873
- N samples: 58

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.196 
- Linear fit: y = 0.071x + 0.0
- P-value: 0.1411
- N samples: 58

**Days Since 2024-01-01:**
- Correlation: -0.117 
- Linear fit: y = -0.000x + 0.2
- P-value: 0.3891
- N samples: 56

**Is Reasoning Model:**
- Correlation: -0.095 
- Linear fit: y = -0.039x + 0.1
- P-value: 0.4792
- N samples: 58

**Benchmark Score:**
- Correlation: -0.081 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.5456
- N samples: 58

**Model Size (B):**
- Correlation: 0.003 
- Linear fit: y = 0.000x + 0.0
- P-value: 0.9824
- N samples: 56

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**3a_unsupported_leap vs Is Open Source:**
  r = -0.420, y = -6.421x + 22.6

**4a_syntax_error vs Days Since 2024-01-01:**
  r = -0.406, y = -0.005x + 4.3

**category3_logical_errors vs Is Open Source:**
  r = -0.383, y = -7.479x + 27.3

**category4_technical_errors vs Days Since 2024-01-01:**
  r = -0.328, y = -0.008x + 8.3

**3a_unsupported_leap vs Days Since 2024-01-01:**
  r = -0.321, y = -0.020x + 36.3

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.320, y = -6.988x + 28.8

**category3_logical_errors vs Days Since 2024-01-01:**
  r = -0.316, y = -0.025x + 44.9

**1c_prompt_contradiction vs Days Since 2024-01-01:**
  r = -0.300, y = -0.002x + 2.2


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
- Correlation: 0.666 ***
- Linear fit: y = 0.985x + 5.1

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.578 ***
- Linear fit: y = 1.294x + 20.6

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.472 ***
- Linear fit: y = 0.321x + 0.8

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.620 ***
- Linear fit: y = 0.937x + 16.7

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.488 ***
- Linear fit: y = 0.224x + -0.1

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.429 ***
- Linear fit: y = 0.130x + -1.5

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.967 ***, y = 0.910x + -0.9

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.967 ***, y = 0.756x + 1.6

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.925 ***, y = 0.466x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.894 ***, y = 0.641x + 0.1

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.858 ***, y = 0.390x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.780 ***, y = 0.244x + -1.6

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.756 ***, y = 0.357x + -0.2

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.724 ***, y = 0.144x + 0.0

**1a: Instruction Override vs 3b: Self Contradiction:**
  r = 0.691 ***, y = 1.063x + 3.3

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = 0.666 ***, y = 0.985x + 5.1

**1b: Context Omission vs 1c: Prompt Contradiction:**
  r = 0.665 ***, y = 0.262x + 0.1

**Category 2: Factual Errors vs 1a: Instruction Override:**
  r = 0.664 ***, y = 0.204x + -0.7

**Category 1: Input Misalignment vs 2b: Spurious Numeric:**
  r = 0.659 ***, y = 0.918x + 3.7

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = 0.651 ***, y = 0.222x + -0.5

**1a: Instruction Override vs 2b: Spurious Numeric:**
  r = 0.647 ***, y = 1.981x + 4.2

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.644 ***, y = 0.401x + -3.7

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = 0.640 ***, y = 1.769x + 3.8

**Category 1: Input Misalignment vs 3b: Self Contradiction:**
  r = 0.639 ***, y = 0.447x + 3.1

**1a: Instruction Override vs 1b: Context Omission:**
  r = 0.635 ***, y = 0.704x + 0.6

**Category 3: Logical Errors vs 1a: Instruction Override:**
  r = 0.625 ***, y = 0.127x + -2.2

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
