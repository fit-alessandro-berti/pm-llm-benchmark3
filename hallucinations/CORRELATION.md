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
- Correlation: -0.287 **
- Linear fit: y = -0.184x + 8.7
- P-value: 0.0071
- N samples: 87

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.156 
- Linear fit: y = 1.316x + 1.8
- P-value: 0.1478
- N samples: 87

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.018 
- Linear fit: y = -0.196x + 2.6
- P-value: 0.8672
- N samples: 87

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.087 
- Linear fit: y = -1.051x + 7.3
- P-value: 0.4227
- N samples: 87

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
- Correlation: 0.038 
- Linear fit: y = 0.597x + 6.4
- P-value: 0.7233
- N samples: 87

**Benchmark Score:**
- Correlation: -0.023 
- Linear fit: y = -0.021x + 7.6
- P-value: 0.8304
- N samples: 87

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.234 *
- Linear fit: y = -0.304x + 29.5
- P-value: 0.0292
- N samples: 87

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Is Open Source:**
- Correlation: -0.172 
- Linear fit: y = -2.936x + 20.5
- P-value: 0.1106
- N samples: 87

**Is Reasoning Model:**
- Correlation: -0.084 
- Linear fit: y = -1.842x + 20.7
- P-value: 0.4380
- N samples: 87

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.169 
- Linear fit: y = -1.139x + 2.7
- P-value: 0.1166
- N samples: 87

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.102 
- Linear fit: y = 0.880x + 1.5
- P-value: 0.3473
- N samples: 87

**Days Since 2024-01-01:**
- Correlation: 0.063 
- Linear fit: y = 0.002x + 1.1
- P-value: 0.6402
- N samples: 57

**Benchmark Score:**
- Correlation: 0.041 
- Linear fit: y = 0.021x + 1.5
- P-value: 0.7093
- N samples: 87

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.183 
- Linear fit: y = -0.493x + 47.6
- P-value: 0.0893
- N samples: 87

**Days Since 2024-01-01:**
- Correlation: -0.139 
- Linear fit: y = -0.021x + 51.2
- P-value: 0.3022
- N samples: 57

**Is Open Source:**
- Correlation: -0.107 
- Linear fit: y = -3.782x + 32.5
- P-value: 0.3227
- N samples: 87

**Model Size (B):**
- Correlation: -0.066 
- Linear fit: y = -0.001x + 34.3
- P-value: 0.6271
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.009 
- Linear fit: y = -0.393x + 31.1
- P-value: 0.9364
- N samples: 87

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.287 **
- Linear fit: y = -0.184x + 8.7
- P-value: 0.0071
- N samples: 87

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.156 
- Linear fit: y = 1.316x + 1.8
- P-value: 0.1478
- N samples: 87

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.018 
- Linear fit: y = -0.196x + 2.6
- P-value: 0.8672
- N samples: 87

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.087 
- Linear fit: y = -1.051x + 7.3
- P-value: 0.4227
- N samples: 87

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
- Correlation: 0.038 
- Linear fit: y = 0.597x + 6.4
- P-value: 0.7233
- N samples: 87

**Benchmark Score:**
- Correlation: -0.023 
- Linear fit: y = -0.021x + 7.6
- P-value: 0.8304
- N samples: 87

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.234 *
- Linear fit: y = -0.304x + 29.5
- P-value: 0.0292
- N samples: 87

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Is Open Source:**
- Correlation: -0.172 
- Linear fit: y = -2.936x + 20.5
- P-value: 0.1106
- N samples: 87

**Is Reasoning Model:**
- Correlation: -0.084 
- Linear fit: y = -1.842x + 20.7
- P-value: 0.4380
- N samples: 87

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.169 
- Linear fit: y = -1.139x + 2.7
- P-value: 0.1166
- N samples: 87

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.102 
- Linear fit: y = 0.880x + 1.5
- P-value: 0.3473
- N samples: 87

**Days Since 2024-01-01:**
- Correlation: 0.063 
- Linear fit: y = 0.002x + 1.1
- P-value: 0.6402
- N samples: 57

**Benchmark Score:**
- Correlation: 0.041 
- Linear fit: y = 0.021x + 1.5
- P-value: 0.7093
- N samples: 87

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.207 
- Linear fit: y = -0.040x + 1.9
- P-value: 0.0540
- N samples: 87

**Model Size (B):**
- Correlation: -0.185 
- Linear fit: y = -0.000x + 0.9
- P-value: 0.1684
- N samples: 57

**Is Open Source:**
- Correlation: 0.129 
- Linear fit: y = 0.327x + 0.4
- P-value: 0.2324
- N samples: 87

**Days Since 2024-01-01:**
- Correlation: -0.128 
- Linear fit: y = -0.001x + 1.9
- P-value: 0.3415
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.047 
- Linear fit: y = -0.152x + 0.7
- P-value: 0.6659
- N samples: 87

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.218 *
- Linear fit: y = -0.088x + 4.3
- P-value: 0.0420
- N samples: 87

**Is Open Source:**
- Correlation: 0.157 
- Linear fit: y = 0.832x + 0.9
- P-value: 0.1467
- N samples: 87

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
- Correlation: 0.045 
- Linear fit: y = 0.304x + 1.1
- P-value: 0.6815
- N samples: 87

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.225 *
- Linear fit: y = -0.056x + 2.4
- P-value: 0.0363
- N samples: 87

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
- Correlation: -0.084 
- Linear fit: y = -0.348x + 0.8
- P-value: 0.4412
- N samples: 87

**Is Open Source:**
- Correlation: 0.048 
- Linear fit: y = 0.157x + 0.5
- P-value: 0.6556
- N samples: 87

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.094 
- Linear fit: y = -0.000x + 1.3
- P-value: 0.4845
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.076 
- Linear fit: y = 0.338x + 1.0
- P-value: 0.4851
- N samples: 87

**Benchmark Score:**
- Correlation: 0.068 
- Linear fit: y = 0.018x + 0.7
- P-value: 0.5342
- N samples: 87

**Is Open Source:**
- Correlation: 0.017 
- Linear fit: y = 0.058x + 1.3
- P-value: 0.8786
- N samples: 87

**Days Since 2024-01-01:**
- Correlation: 0.001 
- Linear fit: y = 0.000x + 1.2
- P-value: 0.9964
- N samples: 57

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.087 
- Linear fit: y = -0.073x + 7.6
- P-value: 0.4233
- N samples: 87

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
- Correlation: -0.068 
- Linear fit: y = -0.750x + 5.4
- P-value: 0.5312
- N samples: 87

**Is Reasoning Model:**
- Correlation: -0.009 
- Linear fit: y = -0.131x + 5.2
- P-value: 0.9321
- N samples: 87

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: 0.291 **
- Linear fit: y = 0.034x + -0.6
- P-value: 0.0062
- N samples: 87

**Model Size (B):**
- Correlation: 0.249 
- Linear fit: y = 0.000x + 0.3
- P-value: 0.0617
- N samples: 57

**Is Open Source:**
- Correlation: -0.236 *
- Linear fit: y = -0.359x + 0.7
- P-value: 0.0277
- N samples: 87

**Is Reasoning Model:**
- Correlation: 0.200 
- Linear fit: y = 0.390x + 0.2
- P-value: 0.0636
- N samples: 87

**Days Since 2024-01-01:**
- Correlation: 0.131 
- Linear fit: y = 0.001x + -0.2
- P-value: 0.3322
- N samples: 57

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.230 *
- Linear fit: y = -0.255x + 23.7
- P-value: 0.0320
- N samples: 87

**Days Since 2024-01-01:**
- Correlation: -0.176 
- Linear fit: y = -0.011x + 25.5
- P-value: 0.1905
- N samples: 57

**Is Open Source:**
- Correlation: -0.154 
- Linear fit: y = -2.242x + 16.1
- P-value: 0.1533
- N samples: 87

**Is Reasoning Model:**
- Correlation: -0.050 
- Linear fit: y = -0.925x + 15.8
- P-value: 0.6480
- N samples: 87

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
- Correlation: -0.153 
- Linear fit: y = -0.931x + 4.9
- P-value: 0.1558
- N samples: 87

**Is Open Source:**
- Correlation: -0.152 
- Linear fit: y = -0.720x + 4.4
- P-value: 0.1593
- N samples: 87

**Benchmark Score:**
- Correlation: -0.131 
- Linear fit: y = -0.047x + 5.7
- P-value: 0.2252
- N samples: 87

**Model Size (B):**
- Correlation: -0.026 
- Linear fit: y = -0.000x + 4.3
- P-value: 0.8462
- N samples: 57

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.120 
- Linear fit: y = 0.026x + -0.0
- P-value: 0.2697
- N samples: 87

**Benchmark Score:**
- Correlation: -0.107 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.3238
- N samples: 87

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
- Linear fit: y = 0.014x + -0.0
- P-value: 0.6377
- N samples: 87

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: 0.124 
- Linear fit: y = 0.621x + 0.1
- P-value: 0.2527
- N samples: 87

**Is Open Source:**
- Correlation: -0.103 
- Linear fit: y = -0.402x + 0.8
- P-value: 0.3425
- N samples: 87

**Model Size (B):**
- Correlation: 0.065 
- Linear fit: y = 0.000x + 0.5
- P-value: 0.6318
- N samples: 57

**Benchmark Score:**
- Correlation: 0.060 
- Linear fit: y = 0.018x + 0.0
- P-value: 0.5816
- N samples: 87

**Days Since 2024-01-01:**
- Correlation: 0.045 
- Linear fit: y = 0.001x + 0.1
- P-value: 0.7393
- N samples: 57

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.156 
- Linear fit: y = -0.684x + 1.8
- P-value: 0.1499
- N samples: 87

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
- Correlation: 0.056 
- Linear fit: y = 0.313x + 1.2
- P-value: 0.6094
- N samples: 87

**Benchmark Score:**
- Correlation: 0.023 
- Linear fit: y = 0.008x + 1.2
- P-value: 0.8292
- N samples: 87

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.093 
- Linear fit: y = -0.005x + 0.2
- P-value: 0.3940
- N samples: 87

**Is Open Source:**
- Correlation: -0.076 
- Linear fit: y = -0.053x + 0.1
- P-value: 0.4845
- N samples: 87

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
- Correlation: -0.061 
- Linear fit: y = -0.055x + 0.1
- P-value: 0.5743
- N samples: 87

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
- Linear fit: y = 0.584x + 5.5

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.442 ***
- Linear fit: y = 0.896x + 17.0

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.397 ***
- Linear fit: y = 0.318x + 1.5

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.461 ***
- Linear fit: y = 0.650x + 14.7

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.602 ***
- Linear fit: y = 0.335x + -0.1

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.538 ***
- Linear fit: y = 0.212x + -1.9

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.968 ***, y = 0.825x + -0.8

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.954 ***, y = 0.871x + -0.9

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.839 ***, y = 0.529x + 0.0

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.815 ***, y = 0.533x + 0.3

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.731 ***, y = 0.425x + -0.3

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.714 ***, y = 0.215x + 0.0

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.667 ***, y = 0.257x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.623 ***, y = 0.173x + 0.8

**Category 2: Factual Errors vs 4b: Model Semantics Breach:**
  r = 0.615 ***, y = 0.224x + -0.0

**Category 2: Factual Errors vs Category 4: Technical Errors:**
  r = 0.602 ***, y = 0.335x + -0.1

**Category 4: Technical Errors vs 2b: Spurious Numeric:**
  r = 0.590 ***, y = 0.967x + 2.9

**2b: Spurious Numeric vs 4b: Model Semantics Breach:**
  r = 0.589 ***, y = 0.235x + 0.3

**Category 2: Factual Errors vs 4c: Visual Descr Mismatch:**
  r = 0.580 ***, y = 0.033x + -0.1

**Category 3: Logical Errors vs 4b: Model Semantics Breach:**
  r = 0.574 ***, y = 0.148x + -1.3

**3a: Unsupported Leap vs 4b: Model Semantics Breach:**
  r = 0.564 ***, y = 0.171x + -1.1

**2b: Spurious Numeric vs 4c: Visual Descr Mismatch:**
  r = 0.547 ***, y = 0.035x + -0.1

**Category 3: Logical Errors vs Category 4: Technical Errors:**
  r = 0.538 ***, y = 0.212x + -1.9

**Category 4: Technical Errors vs 3a: Unsupported Leap:**
  r = 0.507 ***, y = 1.095x + 12.6

**1b: Context Omission vs 3c: Circular Reasoning:**
  r = 0.478 ***, y = 0.019x + -0.0

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.464 ***, y = 0.558x + 11.2

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
