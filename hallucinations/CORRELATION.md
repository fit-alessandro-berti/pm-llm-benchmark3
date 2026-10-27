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
- Correlation: -0.281 **
- Linear fit: y = -0.180x + 8.6
- P-value: 0.0092
- N samples: 85

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.160 
- Linear fit: y = 1.359x + 1.9
- P-value: 0.1425
- N samples: 85

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.030 
- Linear fit: y = -0.333x + 2.7
- P-value: 0.7841
- N samples: 85

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.088 
- Linear fit: y = -1.072x + 7.4
- P-value: 0.4245
- N samples: 85

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
- Correlation: 0.037 
- Linear fit: y = 0.586x + 6.4
- P-value: 0.7384
- N samples: 85

**Benchmark Score:**
- Correlation: -0.021 
- Linear fit: y = -0.020x + 7.6
- P-value: 0.8460
- N samples: 85

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.230 *
- Linear fit: y = -0.298x + 29.4
- P-value: 0.0345
- N samples: 85

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Is Open Source:**
- Correlation: -0.190 
- Linear fit: y = -3.255x + 20.7
- P-value: 0.0818
- N samples: 85

**Is Reasoning Model:**
- Correlation: -0.113 
- Linear fit: y = -2.533x + 21.3
- P-value: 0.3018
- N samples: 85

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.174 
- Linear fit: y = -1.182x + 2.8
- P-value: 0.1106
- N samples: 85

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.090 
- Linear fit: y = 0.800x + 1.6
- P-value: 0.4104
- N samples: 85

**Days Since 2024-01-01:**
- Correlation: 0.063 
- Linear fit: y = 0.002x + 1.1
- P-value: 0.6402
- N samples: 57

**Benchmark Score:**
- Correlation: 0.049 
- Linear fit: y = 0.025x + 1.4
- P-value: 0.6586
- N samples: 85

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.177 
- Linear fit: y = -0.478x + 47.2
- P-value: 0.1045
- N samples: 85

**Days Since 2024-01-01:**
- Correlation: -0.139 
- Linear fit: y = -0.021x + 51.2
- P-value: 0.3022
- N samples: 57

**Is Open Source:**
- Correlation: -0.116 
- Linear fit: y = -4.119x + 32.8
- P-value: 0.2909
- N samples: 85

**Model Size (B):**
- Correlation: -0.066 
- Linear fit: y = -0.001x + 34.3
- P-value: 0.6271
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.028 
- Linear fit: y = -1.310x + 32.1
- P-value: 0.7975
- N samples: 85

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.281 **
- Linear fit: y = -0.180x + 8.6
- P-value: 0.0092
- N samples: 85

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.160 
- Linear fit: y = 1.359x + 1.9
- P-value: 0.1425
- N samples: 85

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.030 
- Linear fit: y = -0.333x + 2.7
- P-value: 0.7841
- N samples: 85

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.088 
- Linear fit: y = -1.072x + 7.4
- P-value: 0.4245
- N samples: 85

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
- Correlation: 0.037 
- Linear fit: y = 0.586x + 6.4
- P-value: 0.7384
- N samples: 85

**Benchmark Score:**
- Correlation: -0.021 
- Linear fit: y = -0.020x + 7.6
- P-value: 0.8460
- N samples: 85

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.230 *
- Linear fit: y = -0.298x + 29.4
- P-value: 0.0345
- N samples: 85

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Is Open Source:**
- Correlation: -0.190 
- Linear fit: y = -3.255x + 20.7
- P-value: 0.0818
- N samples: 85

**Is Reasoning Model:**
- Correlation: -0.113 
- Linear fit: y = -2.533x + 21.3
- P-value: 0.3018
- N samples: 85

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.174 
- Linear fit: y = -1.182x + 2.8
- P-value: 0.1106
- N samples: 85

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.090 
- Linear fit: y = 0.800x + 1.6
- P-value: 0.4104
- N samples: 85

**Days Since 2024-01-01:**
- Correlation: 0.063 
- Linear fit: y = 0.002x + 1.1
- P-value: 0.6402
- N samples: 57

**Benchmark Score:**
- Correlation: 0.049 
- Linear fit: y = 0.025x + 1.4
- P-value: 0.6586
- N samples: 85

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.202 
- Linear fit: y = -0.039x + 1.9
- P-value: 0.0632
- N samples: 85

**Model Size (B):**
- Correlation: -0.185 
- Linear fit: y = -0.000x + 0.9
- P-value: 0.1684
- N samples: 57

**Is Open Source:**
- Correlation: 0.132 
- Linear fit: y = 0.338x + 0.4
- P-value: 0.2273
- N samples: 85

**Days Since 2024-01-01:**
- Correlation: -0.128 
- Linear fit: y = -0.001x + 1.9
- P-value: 0.3415
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.057 
- Linear fit: y = -0.190x + 0.7
- P-value: 0.6028
- N samples: 85

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.213 
- Linear fit: y = -0.086x + 4.3
- P-value: 0.0502
- N samples: 85

**Is Open Source:**
- Correlation: 0.160 
- Linear fit: y = 0.858x + 1.0
- P-value: 0.1423
- N samples: 85

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
- Correlation: 0.036 
- Linear fit: y = 0.252x + 1.1
- P-value: 0.7424
- N samples: 85

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.222 *
- Linear fit: y = -0.055x + 2.4
- P-value: 0.0416
- N samples: 85

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
- Correlation: -0.093 
- Linear fit: y = -0.395x + 0.9
- P-value: 0.3993
- N samples: 85

**Is Open Source:**
- Correlation: 0.050 
- Linear fit: y = 0.163x + 0.5
- P-value: 0.6498
- N samples: 85

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.094 
- Linear fit: y = -0.000x + 1.3
- P-value: 0.4845
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.078 
- Linear fit: y = 0.357x + 1.0
- P-value: 0.4768
- N samples: 85

**Benchmark Score:**
- Correlation: 0.073 
- Linear fit: y = 0.019x + 0.6
- P-value: 0.5042
- N samples: 85

**Is Open Source:**
- Correlation: 0.025 
- Linear fit: y = 0.087x + 1.3
- P-value: 0.8219
- N samples: 85

**Days Since 2024-01-01:**
- Correlation: 0.001 
- Linear fit: y = 0.000x + 1.2
- P-value: 0.9964
- N samples: 57

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.086 
- Linear fit: y = -0.073x + 7.6
- P-value: 0.4330
- N samples: 85

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
- Correlation: -0.066 
- Linear fit: y = -0.741x + 5.4
- P-value: 0.5455
- N samples: 85

**Is Reasoning Model:**
- Correlation: -0.009 
- Linear fit: y = -0.129x + 5.2
- P-value: 0.9360
- N samples: 85

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: 0.295 **
- Linear fit: y = 0.034x + -0.6
- P-value: 0.0061
- N samples: 85

**Is Open Source:**
- Correlation: -0.279 **
- Linear fit: y = -0.418x + 0.7
- P-value: 0.0098
- N samples: 85

**Model Size (B):**
- Correlation: 0.249 
- Linear fit: y = 0.000x + 0.3
- P-value: 0.0617
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.183 
- Linear fit: y = 0.357x + 0.2
- P-value: 0.0944
- N samples: 85

**Days Since 2024-01-01:**
- Correlation: 0.131 
- Linear fit: y = 0.001x + -0.2
- P-value: 0.3322
- N samples: 57

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.225 *
- Linear fit: y = -0.249x + 23.6
- P-value: 0.0380
- N samples: 85

**Days Since 2024-01-01:**
- Correlation: -0.176 
- Linear fit: y = -0.011x + 25.5
- P-value: 0.1905
- N samples: 57

**Is Open Source:**
- Correlation: -0.171 
- Linear fit: y = -2.497x + 16.2
- P-value: 0.1177
- N samples: 85

**Is Reasoning Model:**
- Correlation: -0.077 
- Linear fit: y = -1.476x + 16.3
- P-value: 0.4809
- N samples: 85

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
- Correlation: -0.172 
- Linear fit: y = -1.071x + 5.0
- P-value: 0.1153
- N samples: 85

**Is Open Source:**
- Correlation: -0.164 
- Linear fit: y = -0.784x + 4.5
- P-value: 0.1332
- N samples: 85

**Benchmark Score:**
- Correlation: -0.130 
- Linear fit: y = -0.047x + 5.7
- P-value: 0.2353
- N samples: 85

**Model Size (B):**
- Correlation: -0.026 
- Linear fit: y = -0.000x + 4.3
- P-value: 0.8462
- N samples: 57

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.121 
- Linear fit: y = 0.026x + -0.0
- P-value: 0.2686
- N samples: 85

**Benchmark Score:**
- Correlation: -0.106 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.3343
- N samples: 85

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
- Correlation: 0.051 
- Linear fit: y = 0.014x + 0.0
- P-value: 0.6462
- N samples: 85

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: 0.121 
- Linear fit: y = 0.624x + 0.1
- P-value: 0.2693
- N samples: 85

**Is Open Source:**
- Correlation: -0.104 
- Linear fit: y = -0.409x + 0.8
- P-value: 0.3457
- N samples: 85

**Model Size (B):**
- Correlation: 0.065 
- Linear fit: y = 0.000x + 0.5
- P-value: 0.6318
- N samples: 57

**Benchmark Score:**
- Correlation: 0.065 
- Linear fit: y = 0.019x + -0.0
- P-value: 0.5556
- N samples: 85

**Days Since 2024-01-01:**
- Correlation: 0.045 
- Linear fit: y = 0.001x + 0.1
- P-value: 0.7393
- N samples: 57

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.162 
- Linear fit: y = -0.719x + 1.9
- P-value: 0.1379
- N samples: 85

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
- Correlation: 0.041 
- Linear fit: y = 0.238x + 1.3
- P-value: 0.7083
- N samples: 85

**Benchmark Score:**
- Correlation: 0.031 
- Linear fit: y = 0.010x + 1.2
- P-value: 0.7789
- N samples: 85

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.090 
- Linear fit: y = -0.005x + 0.2
- P-value: 0.4141
- N samples: 85

**Is Open Source:**
- Correlation: -0.076 
- Linear fit: y = -0.054x + 0.1
- P-value: 0.4876
- N samples: 85

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.6113
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.067 
- Linear fit: y = -0.062x + 0.1
- P-value: 0.5400
- N samples: 85

**Days Since 2024-01-01:**
- Correlation: -0.066 
- Linear fit: y = -0.000x + 0.3
- P-value: 0.6241
- N samples: 57

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
- Correlation: 0.406 ***
- Linear fit: y = 0.586x + 5.4

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.442 ***
- Linear fit: y = 0.894x + 17.0

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.393 ***
- Linear fit: y = 0.315x + 1.5

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.463 ***
- Linear fit: y = 0.649x + 14.8

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.602 ***
- Linear fit: y = 0.334x + -0.0

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.537 ***
- Linear fit: y = 0.212x + -1.8

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.968 ***, y = 0.825x + -0.8

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.954 ***, y = 0.871x + -0.9

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.838 ***, y = 0.529x + 0.0

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.814 ***, y = 0.532x + 0.3

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.730 ***, y = 0.425x + -0.3

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.712 ***, y = 0.214x + 0.0

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.666 ***, y = 0.257x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.621 ***, y = 0.173x + 0.8

**Category 2: Factual Errors vs 4b: Model Semantics Breach:**
  r = 0.615 ***, y = 0.223x + -0.0

**Category 2: Factual Errors vs Category 4: Technical Errors:**
  r = 0.602 ***, y = 0.334x + -0.0

**Category 4: Technical Errors vs 2b: Spurious Numeric:**
  r = 0.591 ***, y = 0.972x + 2.9

**2b: Spurious Numeric vs 4b: Model Semantics Breach:**
  r = 0.591 ***, y = 0.235x + 0.3

**Category 2: Factual Errors vs 4c: Visual Descr Mismatch:**
  r = 0.580 ***, y = 0.033x + -0.1

**Category 3: Logical Errors vs 4b: Model Semantics Breach:**
  r = 0.573 ***, y = 0.148x + -1.3

**3a: Unsupported Leap vs 4b: Model Semantics Breach:**
  r = 0.562 ***, y = 0.171x + -1.0

**2b: Spurious Numeric vs 4c: Visual Descr Mismatch:**
  r = 0.547 ***, y = 0.035x + -0.1

**Category 3: Logical Errors vs Category 4: Technical Errors:**
  r = 0.537 ***, y = 0.212x + -1.8

**Category 4: Technical Errors vs 3a: Unsupported Leap:**
  r = 0.505 ***, y = 1.088x + 12.7

**1b: Context Omission vs 3c: Circular Reasoning:**
  r = 0.478 ***, y = 0.019x + -0.0

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.466 ***, y = 0.557x + 11.3

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
