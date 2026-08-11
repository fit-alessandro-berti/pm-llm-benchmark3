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
- Correlation: -0.405 **
- Linear fit: y = -0.112x + 4.8
- P-value: 0.0096
- N samples: 40

**Is Reasoning Model:**
- Correlation: -0.338 *
- Linear fit: y = -1.615x + 2.0
- P-value: 0.0329
- N samples: 40

**Is Open Source:**
- Correlation: 0.262 
- Linear fit: y = 1.202x + 0.4
- P-value: 0.1020
- N samples: 40

**Days Since 2024-01-01:**
- Correlation: -0.170 
- Linear fit: y = -0.003x + 4.0
- P-value: 0.4739
- N samples: 20

**Model Size (B):**
- Correlation: -0.116 
- Linear fit: y = -0.001x + 2.0
- P-value: 0.6572
- N samples: 17

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.369 *
- Linear fit: y = -4.654x + 12.5
- P-value: 0.0191
- N samples: 40

**Is Open Source:**
- Correlation: 0.329 *
- Linear fit: y = 3.985x + 7.7
- P-value: 0.0379
- N samples: 40

**Benchmark Score:**
- Correlation: -0.283 
- Linear fit: y = -0.207x + 16.6
- P-value: 0.0766
- N samples: 40

**Model Size (B):**
- Correlation: 0.282 
- Linear fit: y = 0.002x + 9.0
- P-value: 0.2731
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: -0.039 
- Linear fit: y = -0.001x + 11.4
- P-value: 0.8699
- N samples: 20

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.702 ***
- Linear fit: y = -0.827x + 42.4
- P-value: 0.0000
- N samples: 40

**Is Reasoning Model:**
- Correlation: -0.642 ***
- Linear fit: y = -13.038x + 22.5
- P-value: 0.0000
- N samples: 40

**Is Open Source:**
- Correlation: 0.392 *
- Linear fit: y = 7.631x + 10.6
- P-value: 0.0124
- N samples: 40

**Model Size (B):**
- Correlation: -0.310 
- Linear fit: y = -0.004x + 18.6
- P-value: 0.2254
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: -0.248 
- Linear fit: y = -0.016x + 27.6
- P-value: 0.2921
- N samples: 20

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.434 **
- Linear fit: y = -1.445x + 1.7
- P-value: 0.0052
- N samples: 40

**Days Since 2024-01-01:**
- Correlation: -0.223 
- Linear fit: y = -0.002x + 2.5
- P-value: 0.3442
- N samples: 20

**Benchmark Score:**
- Correlation: -0.129 
- Linear fit: y = -0.025x + 1.6
- P-value: 0.4263
- N samples: 40

**Model Size (B):**
- Correlation: 0.056 
- Linear fit: y = 0.000x + 0.8
- P-value: 0.8301
- N samples: 17

**Is Open Source:**
- Correlation: -0.030 
- Linear fit: y = -0.096x + 0.8
- P-value: 0.8540
- N samples: 40

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.655 ***
- Linear fit: y = -20.967x + 38.9
- P-value: 0.0000
- N samples: 40

**Benchmark Score:**
- Correlation: -0.632 ***
- Linear fit: y = -1.174x + 65.6
- P-value: 0.0000
- N samples: 40

**Is Open Source:**
- Correlation: 0.410 **
- Linear fit: y = 12.586x + 19.6
- P-value: 0.0086
- N samples: 40

**Days Since 2024-01-01:**
- Correlation: -0.235 
- Linear fit: y = -0.023x + 45.4
- P-value: 0.3189
- N samples: 20

**Model Size (B):**
- Correlation: -0.121 
- Linear fit: y = -0.003x + 30.4
- P-value: 0.6430
- N samples: 17

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.405 **
- Linear fit: y = -0.112x + 4.8
- P-value: 0.0096
- N samples: 40

**Is Reasoning Model:**
- Correlation: -0.338 *
- Linear fit: y = -1.615x + 2.0
- P-value: 0.0329
- N samples: 40

**Is Open Source:**
- Correlation: 0.262 
- Linear fit: y = 1.202x + 0.4
- P-value: 0.1020
- N samples: 40

**Days Since 2024-01-01:**
- Correlation: -0.170 
- Linear fit: y = -0.003x + 4.0
- P-value: 0.4739
- N samples: 20

**Model Size (B):**
- Correlation: -0.116 
- Linear fit: y = -0.001x + 2.0
- P-value: 0.6572
- N samples: 17

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.369 *
- Linear fit: y = -4.654x + 12.5
- P-value: 0.0191
- N samples: 40

**Is Open Source:**
- Correlation: 0.329 *
- Linear fit: y = 3.985x + 7.7
- P-value: 0.0379
- N samples: 40

**Benchmark Score:**
- Correlation: -0.283 
- Linear fit: y = -0.207x + 16.6
- P-value: 0.0766
- N samples: 40

**Model Size (B):**
- Correlation: 0.282 
- Linear fit: y = 0.002x + 9.0
- P-value: 0.2731
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: -0.039 
- Linear fit: y = -0.001x + 11.4
- P-value: 0.8699
- N samples: 20

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.702 ***
- Linear fit: y = -0.827x + 42.4
- P-value: 0.0000
- N samples: 40

**Is Reasoning Model:**
- Correlation: -0.642 ***
- Linear fit: y = -13.038x + 22.5
- P-value: 0.0000
- N samples: 40

**Is Open Source:**
- Correlation: 0.392 *
- Linear fit: y = 7.631x + 10.6
- P-value: 0.0124
- N samples: 40

**Model Size (B):**
- Correlation: -0.310 
- Linear fit: y = -0.004x + 18.6
- P-value: 0.2254
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: -0.248 
- Linear fit: y = -0.016x + 27.6
- P-value: 0.2921
- N samples: 20

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.434 **
- Linear fit: y = -1.445x + 1.7
- P-value: 0.0052
- N samples: 40

**Days Since 2024-01-01:**
- Correlation: -0.223 
- Linear fit: y = -0.002x + 2.5
- P-value: 0.3442
- N samples: 20

**Benchmark Score:**
- Correlation: -0.129 
- Linear fit: y = -0.025x + 1.6
- P-value: 0.4263
- N samples: 40

**Model Size (B):**
- Correlation: 0.056 
- Linear fit: y = 0.000x + 0.8
- P-value: 0.8301
- N samples: 17

**Is Open Source:**
- Correlation: -0.030 
- Linear fit: y = -0.096x + 0.8
- P-value: 0.8540
- N samples: 40

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.335 *
- Linear fit: y = -0.566x + 0.6
- P-value: 0.0346
- N samples: 40

**Benchmark Score:**
- Correlation: -0.235 
- Linear fit: y = -0.023x + 1.1
- P-value: 0.1449
- N samples: 40

**Days Since 2024-01-01:**
- Correlation: -0.204 
- Linear fit: y = -0.001x + 1.6
- P-value: 0.3877
- N samples: 20

**Is Open Source:**
- Correlation: 0.190 
- Linear fit: y = 0.308x + 0.1
- P-value: 0.2398
- N samples: 40

**Model Size (B):**
- Correlation: -0.068 
- Linear fit: y = -0.000x + 0.6
- P-value: 0.7965
- N samples: 17

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.426 **
- Linear fit: y = -0.054x + 2.4
- P-value: 0.0061
- N samples: 40

**Is Reasoning Model:**
- Correlation: -0.250 
- Linear fit: y = -0.549x + 0.9
- P-value: 0.1199
- N samples: 40

**Days Since 2024-01-01:**
- Correlation: -0.248 
- Linear fit: y = -0.002x + 2.4
- P-value: 0.2917
- N samples: 20

**Is Open Source:**
- Correlation: 0.240 
- Linear fit: y = 0.505x + 0.3
- P-value: 0.1365
- N samples: 40

**Model Size (B):**
- Correlation: -0.099 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.7049
- N samples: 17

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.344 *
- Linear fit: y = -0.035x + 1.4
- P-value: 0.0297
- N samples: 40

**Is Reasoning Model:**
- Correlation: -0.286 
- Linear fit: y = -0.500x + 0.5
- P-value: 0.0734
- N samples: 40

**Is Open Source:**
- Correlation: 0.232 
- Linear fit: y = 0.389x + -0.0
- P-value: 0.1494
- N samples: 40

**Model Size (B):**
- Correlation: -0.129 
- Linear fit: y = -0.000x + 0.4
- P-value: 0.6221
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: 0.032 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.8945
- N samples: 20

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.377 *
- Linear fit: y = -2.176x + 2.7
- P-value: 0.0163
- N samples: 40

**Benchmark Score:**
- Correlation: -0.172 
- Linear fit: y = -0.058x + 3.3
- P-value: 0.2873
- N samples: 40

**Is Open Source:**
- Correlation: 0.157 
- Linear fit: y = 0.869x + 0.9
- P-value: 0.3327
- N samples: 40

**Days Since 2024-01-01:**
- Correlation: -0.118 
- Linear fit: y = -0.003x + 4.2
- P-value: 0.6206
- N samples: 20

**Model Size (B):**
- Correlation: 0.006 
- Linear fit: y = 0.000x + 2.0
- P-value: 0.9820
- N samples: 17

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.365 
- Linear fit: y = 0.002x + 6.8
- P-value: 0.1501
- N samples: 17

**Is Open Source:**
- Correlation: 0.285 
- Linear fit: y = 3.076x + 6.6
- P-value: 0.0744
- N samples: 40

**Benchmark Score:**
- Correlation: -0.250 
- Linear fit: y = -0.163x + 13.6
- P-value: 0.1196
- N samples: 40

**Is Reasoning Model:**
- Correlation: -0.238 
- Linear fit: y = -2.676x + 9.7
- P-value: 0.1393
- N samples: 40

**Days Since 2024-01-01:**
- Correlation: 0.018 
- Linear fit: y = 0.001x + 7.6
- P-value: 0.9406
- N samples: 20

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.360 
- Linear fit: y = 0.000x + 0.1
- P-value: 0.1558
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: 0.287 
- Linear fit: y = 0.001x + -0.4
- P-value: 0.2197
- N samples: 20

**Benchmark Score:**
- Correlation: 0.279 
- Linear fit: y = 0.014x + -0.3
- P-value: 0.0816
- N samples: 40

**Is Reasoning Model:**
- Correlation: 0.236 
- Linear fit: y = 0.198x + 0.1
- P-value: 0.1429
- N samples: 40

**Is Open Source:**
- Correlation: 0.050 
- Linear fit: y = 0.040x + 0.2
- P-value: 0.7581
- N samples: 40

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.702 ***
- Linear fit: y = -0.791x + 38.5
- P-value: 0.0000
- N samples: 40

**Is Reasoning Model:**
- Correlation: -0.617 ***
- Linear fit: y = -11.989x + 19.1
- P-value: 0.0000
- N samples: 40

**Is Open Source:**
- Correlation: 0.421 **
- Linear fit: y = 7.848x + 7.8
- P-value: 0.0068
- N samples: 40

**Model Size (B):**
- Correlation: -0.234 
- Linear fit: y = -0.003x + 15.2
- P-value: 0.3670
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: -0.191 
- Linear fit: y = -0.012x + 21.7
- P-value: 0.4188
- N samples: 20

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.410 
- Linear fit: y = -0.001x + 3.2
- P-value: 0.1022
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: -0.309 
- Linear fit: y = -0.004x + 5.5
- P-value: 0.1847
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.230 
- Linear fit: y = -0.907x + 3.2
- P-value: 0.1533
- N samples: 40

**Benchmark Score:**
- Correlation: -0.128 
- Linear fit: y = -0.029x + 3.6
- P-value: 0.4315
- N samples: 40

**Is Open Source:**
- Correlation: -0.087 
- Linear fit: y = -0.328x + 2.8
- P-value: 0.5940
- N samples: 40

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.313 *
- Linear fit: y = -0.143x + 0.1
- P-value: 0.0495
- N samples: 40

**Is Open Source:**
- Correlation: 0.254 
- Linear fit: y = 0.111x + 0.0
- P-value: 0.1143
- N samples: 40

**Benchmark Score:**
- Correlation: -0.244 
- Linear fit: y = -0.006x + 0.3
- P-value: 0.1284
- N samples: 40

**Days Since 2024-01-01:**
- Correlation: -0.181 
- Linear fit: y = -0.000x + 0.4
- P-value: 0.4439
- N samples: 20

**Model Size (B):**
- Correlation: -0.065 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.8055
- N samples: 17

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.307 
- Linear fit: y = -0.676x + 0.7
- P-value: 0.0536
- N samples: 40

**Is Open Source:**
- Correlation: -0.141 
- Linear fit: y = -0.298x + 0.4
- P-value: 0.3842
- N samples: 40

**Model Size (B):**
- Correlation: -0.061 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.8155
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: -0.026 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.9142
- N samples: 20

**Benchmark Score:**
- Correlation: 0.016 
- Linear fit: y = 0.002x + 0.2
- P-value: 0.9224
- N samples: 40

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.326 *
- Linear fit: y = -0.808x + 1.0
- P-value: 0.0403
- N samples: 40

**Benchmark Score:**
- Correlation: -0.173 
- Linear fit: y = -0.025x + 1.3
- P-value: 0.2849
- N samples: 40

**Days Since 2024-01-01:**
- Correlation: -0.157 
- Linear fit: y = -0.001x + 1.7
- P-value: 0.5081
- N samples: 20

**Is Open Source:**
- Correlation: 0.104 
- Linear fit: y = 0.247x + 0.4
- P-value: 0.5228
- N samples: 40

**Model Size (B):**
- Correlation: 0.087 
- Linear fit: y = 0.000x + 0.6
- P-value: 0.7396
- N samples: 17

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.475 *
- Linear fit: y = -0.001x + 0.6
- P-value: 0.0345
- N samples: 20

**Is Open Source:**
- Correlation: -0.145 
- Linear fit: y = -0.045x + 0.0
- P-value: 0.3725
- N samples: 40

**Is Reasoning Model:**
- Correlation: 0.118 
- Linear fit: y = 0.038x + 0.0
- P-value: 0.4702
- N samples: 40

**Benchmark Score:**
- Correlation: -0.110 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.4981
- N samples: 40

**Model Size (B):**
- Correlation: -0.091 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.7277
- N samples: 17

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**category3_logical_errors vs Benchmark Score:**
  r = -0.702, y = -0.827x + 42.4

**3a_unsupported_leap vs Benchmark Score:**
  r = -0.702, y = -0.791x + 38.5

**total_hallucinations vs Is Reasoning Model:**
  r = -0.655, y = -20.967x + 38.9

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.642, y = -13.038x + 22.5

**total_hallucinations vs Benchmark Score:**
  r = -0.632, y = -1.174x + 65.6

**3a_unsupported_leap vs Is Reasoning Model:**
  r = -0.617, y = -11.989x + 19.1

**4c_visual_descr_mismatch vs Days Since 2024-01-01:**
  r = -0.475, y = -0.001x + 0.6

**category4_technical_errors vs Is Reasoning Model:**
  r = -0.434, y = -1.445x + 1.7

**1b_context_omission vs Benchmark Score:**
  r = -0.426, y = -0.054x + 2.4

**3a_unsupported_leap vs Is Open Source:**
  r = 0.421, y = 7.848x + 7.8

**total_hallucinations vs Is Open Source:**
  r = 0.410, y = 12.586x + 19.6

**category1_input_misalignment vs Benchmark Score:**
  r = -0.405, y = -0.112x + 4.8

**category3_logical_errors vs Is Open Source:**
  r = 0.392, y = 7.631x + 10.6

**2a_concept_fabrication vs Is Reasoning Model:**
  r = -0.377, y = -2.176x + 2.7

**category2_factual_errors vs Is Reasoning Model:**
  r = -0.369, y = -4.654x + 12.5

**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.344, y = -0.035x + 1.4

**category1_input_misalignment vs Is Reasoning Model:**
  r = -0.338, y = -1.615x + 2.0

**1a_instruction_override vs Is Reasoning Model:**
  r = -0.335, y = -0.566x + 0.6

**category2_factual_errors vs Is Open Source:**
  r = 0.329, y = 3.985x + 7.7

**4b_model_semantics_breach vs Is Reasoning Model:**
  r = -0.326, y = -0.808x + 1.0

**3c_circular_reasoning vs Is Reasoning Model:**
  r = -0.313, y = -0.143x + 0.1


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
- Correlation: 0.408 **
- Linear fit: y = 1.077x + 8.5

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.428 **
- Linear fit: y = 1.818x + 12.3

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.245 
- Linear fit: y = 0.171x + 0.6

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.441 **
- Linear fit: y = 0.710x + 7.3

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.145 
- Linear fit: y = 0.038x + 0.4

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.273 
- Linear fit: y = 0.045x + 0.1

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.982 ***, y = 0.939x + -1.8

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.899 ***, y = 0.414x + 0.1

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.890 ***, y = 0.794x + 0.5

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.834 ***, y = 0.305x + -0.1

**1a: Instruction Override vs 2a: Concept Fabrication:**
  r = 0.798 ***, y = 2.722x + 0.6

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.797 ***, y = 0.282x + 0.0

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.749 ***, y = 0.557x + 0.0

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.652 ***, y = 0.431x + -0.1

**1b: Context Omission vs 1c: Prompt Contradiction:**
  r = 0.644 ***, y = 0.511x + -0.1

**2a: Concept Fabrication vs 3c: Circular Reasoning:**
  r = 0.642 ***, y = 0.051x + -0.0

**1a: Instruction Override vs 1b: Context Omission:**
  r = 0.577 ***, y = 0.751x + 0.3

**1b: Context Omission vs 4c: Visual Descr Mismatch:**
  r = 0.534 ***, y = 0.080x + -0.0

**Category 1: Input Misalignment vs 2a: Concept Fabrication:**
  r = 0.525 ***, y = 0.633x + 0.7

**1a: Instruction Override vs 3c: Circular Reasoning:**
  r = 0.491 **, y = 0.133x + 0.0

**1a: Instruction Override vs 1c: Prompt Contradiction:**
  r = 0.487 **, y = 0.503x + 0.0

**Category 2: Factual Errors vs 2a: Concept Fabrication:**
  r = 0.451 **, y = 0.206x + -0.7

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = 0.446 **, y = 0.078x + -0.2

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.441 **, y = 0.710x + 7.3

**Category 3: Logical Errors vs 1b: Context Omission:**
  r = 0.439 **, y = 0.048x + -0.2

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.432 **, y = 0.666x + 5.0

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

**Category 3: Logical Errors vs 2c: False Citation:**
  r = -0.356 *, y = -0.015x + 0.4
  (Models good at one tend to be worse at the other)

**2c: False Citation vs 3b: Self Contradiction:**
  r = -0.332 *, y = -1.562x + 2.9
  (Models good at one tend to be worse at the other)

================================================================================
## END OF ANALYSIS
================================================================================
