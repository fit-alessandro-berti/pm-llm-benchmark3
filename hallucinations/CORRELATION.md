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
- Correlation: -0.271 *
- Linear fit: y = -0.177x + 8.5
- P-value: 0.0138
- N samples: 82

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.164 
- Linear fit: y = 1.414x + 1.9
- P-value: 0.1402
- N samples: 82

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.024 
- Linear fit: y = -0.271x + 2.7
- P-value: 0.8271
- N samples: 82

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.112 
- Linear fit: y = -1.361x + 7.5
- P-value: 0.3150
- N samples: 82

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
- Correlation: 0.040 
- Linear fit: y = 0.615x + 6.4
- P-value: 0.7244
- N samples: 82

**Benchmark Score:**
- Correlation: -0.007 
- Linear fit: y = -0.006x + 7.1
- P-value: 0.9515
- N samples: 82

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Benchmark Score:**
- Correlation: -0.204 
- Linear fit: y = -0.266x + 28.5
- P-value: 0.0662
- N samples: 82

**Is Open Source:**
- Correlation: -0.178 
- Linear fit: y = -3.070x + 20.8
- P-value: 0.1088
- N samples: 82

**Is Reasoning Model:**
- Correlation: -0.102 
- Linear fit: y = -2.244x + 21.3
- P-value: 0.3639
- N samples: 82

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.168 
- Linear fit: y = -1.153x + 2.8
- P-value: 0.1311
- N samples: 82

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.103 
- Linear fit: y = 0.907x + 1.6
- P-value: 0.3569
- N samples: 82

**Benchmark Score:**
- Correlation: 0.075 
- Linear fit: y = 0.039x + 1.0
- P-value: 0.5006
- N samples: 82

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
- Correlation: -0.153 
- Linear fit: y = -0.413x + 45.3
- P-value: 0.1708
- N samples: 82

**Days Since 2024-01-01:**
- Correlation: -0.139 
- Linear fit: y = -0.021x + 51.2
- P-value: 0.3022
- N samples: 57

**Is Open Source:**
- Correlation: -0.116 
- Linear fit: y = -4.134x + 33.2
- P-value: 0.3001
- N samples: 82

**Model Size (B):**
- Correlation: -0.066 
- Linear fit: y = -0.001x + 34.3
- P-value: 0.6271
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.018 
- Linear fit: y = -0.813x + 32.1
- P-value: 0.8743
- N samples: 82

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.271 *
- Linear fit: y = -0.177x + 8.5
- P-value: 0.0138
- N samples: 82

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.164 
- Linear fit: y = 1.414x + 1.9
- P-value: 0.1402
- N samples: 82

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.024 
- Linear fit: y = -0.271x + 2.7
- P-value: 0.8271
- N samples: 82

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.112 
- Linear fit: y = -1.361x + 7.5
- P-value: 0.3150
- N samples: 82

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
- Correlation: 0.040 
- Linear fit: y = 0.615x + 6.4
- P-value: 0.7244
- N samples: 82

**Benchmark Score:**
- Correlation: -0.007 
- Linear fit: y = -0.006x + 7.1
- P-value: 0.9515
- N samples: 82

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Benchmark Score:**
- Correlation: -0.204 
- Linear fit: y = -0.266x + 28.5
- P-value: 0.0662
- N samples: 82

**Is Open Source:**
- Correlation: -0.178 
- Linear fit: y = -3.070x + 20.8
- P-value: 0.1088
- N samples: 82

**Is Reasoning Model:**
- Correlation: -0.102 
- Linear fit: y = -2.244x + 21.3
- P-value: 0.3639
- N samples: 82

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.168 
- Linear fit: y = -1.153x + 2.8
- P-value: 0.1311
- N samples: 82

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.103 
- Linear fit: y = 0.907x + 1.6
- P-value: 0.3569
- N samples: 82

**Benchmark Score:**
- Correlation: 0.075 
- Linear fit: y = 0.039x + 1.0
- P-value: 0.5006
- N samples: 82

**Days Since 2024-01-01:**
- Correlation: 0.063 
- Linear fit: y = 0.002x + 1.1
- P-value: 0.6402
- N samples: 57

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.204 
- Linear fit: y = -0.040x + 1.9
- P-value: 0.0658
- N samples: 82

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
- Correlation: 0.122 
- Linear fit: y = 0.315x + 0.4
- P-value: 0.2735
- N samples: 82

**Is Reasoning Model:**
- Correlation: -0.059 
- Linear fit: y = -0.196x + 0.7
- P-value: 0.5969
- N samples: 82

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.201 
- Linear fit: y = -0.083x + 4.2
- P-value: 0.0698
- N samples: 82

**Is Open Source:**
- Correlation: 0.167 
- Linear fit: y = 0.911x + 1.0
- P-value: 0.1327
- N samples: 82

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
- Correlation: 0.043 
- Linear fit: y = 0.300x + 1.1
- P-value: 0.7019
- N samples: 82

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.214 
- Linear fit: y = -0.054x + 2.4
- P-value: 0.0539
- N samples: 82

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
- Correlation: -0.087 
- Linear fit: y = -0.374x + 0.9
- P-value: 0.4345
- N samples: 82

**Is Open Source:**
- Correlation: 0.057 
- Linear fit: y = 0.188x + 0.5
- P-value: 0.6138
- N samples: 82

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.094 
- Linear fit: y = -0.000x + 1.3
- P-value: 0.4845
- N samples: 57

**Is Open Source:**
- Correlation: -0.067 
- Linear fit: y = -0.178x + 1.3
- P-value: 0.5476
- N samples: 82

**Is Reasoning Model:**
- Correlation: 0.066 
- Linear fit: y = 0.224x + 1.0
- P-value: 0.5547
- N samples: 82

**Benchmark Score:**
- Correlation: 0.052 
- Linear fit: y = 0.010x + 0.8
- P-value: 0.6412
- N samples: 82

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
- Correlation: -0.066 
- Linear fit: y = -0.738x + 5.5
- P-value: 0.5585
- N samples: 82

**Benchmark Score:**
- Correlation: -0.061 
- Linear fit: y = -0.052x + 7.0
- P-value: 0.5852
- N samples: 82

**Is Reasoning Model:**
- Correlation: 0.002 
- Linear fit: y = 0.024x + 5.2
- P-value: 0.9882
- N samples: 82

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: 0.309 **
- Linear fit: y = 0.035x + -0.7
- P-value: 0.0048
- N samples: 82

**Is Open Source:**
- Correlation: -0.294 **
- Linear fit: y = -0.446x + 0.7
- P-value: 0.0074
- N samples: 82

**Model Size (B):**
- Correlation: 0.249 
- Linear fit: y = 0.000x + 0.3
- P-value: 0.0617
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.188 
- Linear fit: y = 0.367x + 0.2
- P-value: 0.0899
- N samples: 82

**Days Since 2024-01-01:**
- Correlation: 0.131 
- Linear fit: y = 0.001x + -0.2
- P-value: 0.3322
- N samples: 57

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.197 
- Linear fit: y = -0.218x + 22.7
- P-value: 0.0767
- N samples: 82

**Days Since 2024-01-01:**
- Correlation: -0.176 
- Linear fit: y = -0.011x + 25.5
- P-value: 0.1905
- N samples: 57

**Is Open Source:**
- Correlation: -0.156 
- Linear fit: y = -2.286x + 16.4
- P-value: 0.1609
- N samples: 82

**Is Reasoning Model:**
- Correlation: -0.063 
- Linear fit: y = -1.184x + 16.3
- P-value: 0.5736
- N samples: 82

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
- Correlation: -0.173 
- Linear fit: y = -1.075x + 5.0
- P-value: 0.1193
- N samples: 82

**Is Open Source:**
- Correlation: -0.168 
- Linear fit: y = -0.812x + 4.5
- P-value: 0.1312
- N samples: 82

**Benchmark Score:**
- Correlation: -0.126 
- Linear fit: y = -0.046x + 5.7
- P-value: 0.2582
- N samples: 82

**Model Size (B):**
- Correlation: -0.026 
- Linear fit: y = -0.000x + 4.3
- P-value: 0.8462
- N samples: 57

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.126 
- Linear fit: y = 0.028x + 0.0
- P-value: 0.2609
- N samples: 82

**Benchmark Score:**
- Correlation: -0.102 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.3601
- N samples: 82

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
- Correlation: 0.053 
- Linear fit: y = 0.015x + 0.0
- P-value: 0.6390
- N samples: 82

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: 0.128 
- Linear fit: y = 0.658x + 0.1
- P-value: 0.2536
- N samples: 82

**Is Open Source:**
- Correlation: -0.100 
- Linear fit: y = -0.403x + 0.8
- P-value: 0.3696
- N samples: 82

**Benchmark Score:**
- Correlation: 0.079 
- Linear fit: y = 0.024x + -0.1
- P-value: 0.4825
- N samples: 82

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
- Correlation: -0.155 
- Linear fit: y = -0.697x + 1.9
- P-value: 0.1632
- N samples: 82

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
- Correlation: 0.058 
- Linear fit: y = 0.020x + 0.9
- P-value: 0.6034
- N samples: 82

**Is Reasoning Model:**
- Correlation: 0.054 
- Linear fit: y = 0.308x + 1.3
- P-value: 0.6325
- N samples: 82

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.083 
- Linear fit: y = -0.005x + 0.2
- P-value: 0.4596
- N samples: 82

**Is Open Source:**
- Correlation: -0.074 
- Linear fit: y = -0.053x + 0.1
- P-value: 0.5086
- N samples: 82

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
- Correlation: -0.064 
- Linear fit: y = -0.059x + 0.1
- P-value: 0.5695
- N samples: 82

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**2c_false_citation vs Benchmark Score:**
  r = 0.309, y = 0.035x + -0.7


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
- Correlation: 0.403 ***
- Linear fit: y = 0.567x + 5.5

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.437 ***
- Linear fit: y = 0.873x + 17.3

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.390 ***
- Linear fit: y = 0.310x + 1.6

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.467 ***
- Linear fit: y = 0.663x + 14.9

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.622 ***
- Linear fit: y = 0.352x + -0.1

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.529 ***
- Linear fit: y = 0.211x + -1.8

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.970 ***, y = 0.901x + -1.0

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.967 ***, y = 0.822x + -0.7

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.837 ***, y = 0.529x + 0.0

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.811 ***, y = 0.530x + 0.3

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.730 ***, y = 0.427x + -0.3

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.714 ***, y = 0.214x + 0.0

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.665 ***, y = 0.258x + -0.1

**Category 2: Factual Errors vs 4b: Model Semantics Breach:**
  r = 0.636 ***, y = 0.235x + -0.0

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.625 ***, y = 0.175x + 0.7

**Category 2: Factual Errors vs Category 4: Technical Errors:**
  r = 0.622 ***, y = 0.352x + -0.1

**Category 2: Factual Errors vs 4c: Visual Descr Mismatch:**
  r = 0.596 ***, y = 0.035x + -0.2

**Category 4: Technical Errors vs 2b: Spurious Numeric:**
  r = 0.586 ***, y = 0.963x + 3.0

**2b: Spurious Numeric vs 4b: Model Semantics Breach:**
  r = 0.586 ***, y = 0.233x + 0.4

**Category 3: Logical Errors vs 4b: Model Semantics Breach:**
  r = 0.566 ***, y = 0.147x + -1.3

**3a: Unsupported Leap vs 4b: Model Semantics Breach:**
  r = 0.553 ***, y = 0.169x + -1.0

**2b: Spurious Numeric vs 4c: Visual Descr Mismatch:**
  r = 0.548 ***, y = 0.035x + -0.1

**Category 3: Logical Errors vs Category 4: Technical Errors:**
  r = 0.529 ***, y = 0.211x + -1.8

**Category 4: Technical Errors vs 3a: Unsupported Leap:**
  r = 0.495 ***, y = 1.056x + 12.9

**1b: Context Omission vs 3c: Circular Reasoning:**
  r = 0.478 ***, y = 0.019x + -0.0

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.477 ***, y = 0.576x + 11.4

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
