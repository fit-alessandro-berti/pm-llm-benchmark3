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
- Correlation: -0.292 **
- Linear fit: y = -0.186x + 8.7
- P-value: 0.0056
- N samples: 89

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.162 
- Linear fit: y = 1.348x + 1.8
- P-value: 0.1305
- N samples: 89

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.019 
- Linear fit: y = -0.196x + 2.5
- P-value: 0.8626
- N samples: 89

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.103 
- Linear fit: y = -1.238x + 7.5
- P-value: 0.3387
- N samples: 89

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
- Correlation: 0.022 
- Linear fit: y = 0.336x + 6.7
- P-value: 0.8375
- N samples: 89

**Benchmark Score:**
- Correlation: -0.006 
- Linear fit: y = -0.005x + 7.2
- P-value: 0.9557
- N samples: 89

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.221 *
- Linear fit: y = -0.287x + 29.1
- P-value: 0.0373
- N samples: 89

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Is Open Source:**
- Correlation: -0.182 
- Linear fit: y = -3.096x + 20.7
- P-value: 0.0879
- N samples: 89

**Is Reasoning Model:**
- Correlation: -0.108 
- Linear fit: y = -2.315x + 21.2
- P-value: 0.3147
- N samples: 89

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.170 
- Linear fit: y = -1.130x + 2.7
- P-value: 0.1122
- N samples: 89

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.094 
- Linear fit: y = 0.787x + 1.6
- P-value: 0.3834
- N samples: 89

**Days Since 2024-01-01:**
- Correlation: 0.063 
- Linear fit: y = 0.002x + 1.1
- P-value: 0.6402
- N samples: 57

**Benchmark Score:**
- Correlation: 0.041 
- Linear fit: y = 0.021x + 1.5
- P-value: 0.7046
- N samples: 89

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.173 
- Linear fit: y = -0.462x + 46.8
- P-value: 0.1057
- N samples: 89

**Days Since 2024-01-01:**
- Correlation: -0.139 
- Linear fit: y = -0.021x + 51.2
- P-value: 0.3022
- N samples: 57

**Is Open Source:**
- Correlation: -0.116 
- Linear fit: y = -4.082x + 32.8
- P-value: 0.2777
- N samples: 89

**Model Size (B):**
- Correlation: -0.066 
- Linear fit: y = -0.001x + 34.3
- P-value: 0.6271
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.028 
- Linear fit: y = -1.222x + 32.0
- P-value: 0.7974
- N samples: 89

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.292 **
- Linear fit: y = -0.186x + 8.7
- P-value: 0.0056
- N samples: 89

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.162 
- Linear fit: y = 1.348x + 1.8
- P-value: 0.1305
- N samples: 89

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.019 
- Linear fit: y = -0.196x + 2.5
- P-value: 0.8626
- N samples: 89

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.103 
- Linear fit: y = -1.238x + 7.5
- P-value: 0.3387
- N samples: 89

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
- Correlation: 0.022 
- Linear fit: y = 0.336x + 6.7
- P-value: 0.8375
- N samples: 89

**Benchmark Score:**
- Correlation: -0.006 
- Linear fit: y = -0.005x + 7.2
- P-value: 0.9557
- N samples: 89

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.221 *
- Linear fit: y = -0.287x + 29.1
- P-value: 0.0373
- N samples: 89

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Is Open Source:**
- Correlation: -0.182 
- Linear fit: y = -3.096x + 20.7
- P-value: 0.0879
- N samples: 89

**Is Reasoning Model:**
- Correlation: -0.108 
- Linear fit: y = -2.315x + 21.2
- P-value: 0.3147
- N samples: 89

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.170 
- Linear fit: y = -1.130x + 2.7
- P-value: 0.1122
- N samples: 89

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.094 
- Linear fit: y = 0.787x + 1.6
- P-value: 0.3834
- N samples: 89

**Days Since 2024-01-01:**
- Correlation: 0.063 
- Linear fit: y = 0.002x + 1.1
- P-value: 0.6402
- N samples: 57

**Benchmark Score:**
- Correlation: 0.041 
- Linear fit: y = 0.021x + 1.5
- P-value: 0.7046
- N samples: 89

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.214 *
- Linear fit: y = -0.041x + 1.9
- P-value: 0.0444
- N samples: 89

**Model Size (B):**
- Correlation: -0.185 
- Linear fit: y = -0.000x + 0.9
- P-value: 0.1684
- N samples: 57

**Is Open Source:**
- Correlation: 0.137 
- Linear fit: y = 0.344x + 0.4
- P-value: 0.2008
- N samples: 89

**Days Since 2024-01-01:**
- Correlation: -0.128 
- Linear fit: y = -0.001x + 1.9
- P-value: 0.3415
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.038 
- Linear fit: y = -0.119x + 0.6
- P-value: 0.7261
- N samples: 89

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.221 *
- Linear fit: y = -0.089x + 4.3
- P-value: 0.0375
- N samples: 89

**Is Open Source:**
- Correlation: 0.158 
- Linear fit: y = 0.829x + 0.9
- P-value: 0.1403
- N samples: 89

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
- Correlation: 0.035 
- Linear fit: y = 0.230x + 1.1
- P-value: 0.7478
- N samples: 89

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.229 *
- Linear fit: y = -0.056x + 2.4
- P-value: 0.0310
- N samples: 89

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
- Correlation: -0.076 
- Linear fit: y = -0.306x + 0.8
- P-value: 0.4817
- N samples: 89

**Is Open Source:**
- Correlation: 0.055 
- Linear fit: y = 0.175x + 0.4
- P-value: 0.6114
- N samples: 89

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.094 
- Linear fit: y = -0.000x + 1.3
- P-value: 0.4845
- N samples: 57

**Benchmark Score:**
- Correlation: 0.063 
- Linear fit: y = 0.017x + 0.7
- P-value: 0.5586
- N samples: 89

**Is Reasoning Model:**
- Correlation: 0.046 
- Linear fit: y = 0.202x + 1.1
- P-value: 0.6682
- N samples: 89

**Is Open Source:**
- Correlation: 0.014 
- Linear fit: y = 0.048x + 1.3
- P-value: 0.8983
- N samples: 89

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
- Linear fit: y = -0.953x + 5.6
- P-value: 0.4215
- N samples: 89

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
- Correlation: -0.064 
- Linear fit: y = -0.054x + 7.0
- P-value: 0.5530
- N samples: 89

**Is Reasoning Model:**
- Correlation: -0.019 
- Linear fit: y = -0.259x + 5.4
- P-value: 0.8629
- N samples: 89

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: 0.273 **
- Linear fit: y = 0.032x + -0.6
- P-value: 0.0095
- N samples: 89

**Model Size (B):**
- Correlation: 0.249 
- Linear fit: y = 0.000x + 0.3
- P-value: 0.0617
- N samples: 57

**Is Open Source:**
- Correlation: -0.219 *
- Linear fit: y = -0.332x + 0.6
- P-value: 0.0388
- N samples: 89

**Is Reasoning Model:**
- Correlation: 0.206 
- Linear fit: y = 0.393x + 0.2
- P-value: 0.0533
- N samples: 89

**Days Since 2024-01-01:**
- Correlation: 0.131 
- Linear fit: y = 0.001x + -0.2
- P-value: 0.3322
- N samples: 57

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.219 *
- Linear fit: y = -0.242x + 23.4
- P-value: 0.0389
- N samples: 89

**Days Since 2024-01-01:**
- Correlation: -0.176 
- Linear fit: y = -0.011x + 25.5
- P-value: 0.1905
- N samples: 57

**Is Open Source:**
- Correlation: -0.163 
- Linear fit: y = -2.359x + 16.2
- P-value: 0.1273
- N samples: 89

**Is Reasoning Model:**
- Correlation: -0.074 
- Linear fit: y = -1.346x + 16.2
- P-value: 0.4929
- N samples: 89

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
- Correlation: -0.165 
- Linear fit: y = -0.983x + 4.9
- P-value: 0.1212
- N samples: 89

**Is Open Source:**
- Correlation: -0.162 
- Linear fit: y = -0.762x + 4.5
- P-value: 0.1294
- N samples: 89

**Benchmark Score:**
- Correlation: -0.119 
- Linear fit: y = -0.043x + 5.6
- P-value: 0.2655
- N samples: 89

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
- P-value: 0.2599
- N samples: 89

**Benchmark Score:**
- Correlation: -0.108 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.3133
- N samples: 89

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
- P-value: 0.6297
- N samples: 89

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: 0.126 
- Linear fit: y = 0.618x + 0.1
- P-value: 0.2377
- N samples: 89

**Is Open Source:**
- Correlation: -0.095 
- Linear fit: y = -0.370x + 0.8
- P-value: 0.3738
- N samples: 89

**Model Size (B):**
- Correlation: 0.065 
- Linear fit: y = 0.000x + 0.5
- P-value: 0.6318
- N samples: 57

**Benchmark Score:**
- Correlation: 0.053 
- Linear fit: y = 0.016x + 0.1
- P-value: 0.6235
- N samples: 89

**Days Since 2024-01-01:**
- Correlation: 0.045 
- Linear fit: y = 0.001x + 0.1
- P-value: 0.7393
- N samples: 57

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.163 
- Linear fit: y = -0.712x + 1.8
- P-value: 0.1271
- N samples: 89

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
- Correlation: 0.039 
- Linear fit: y = 0.217x + 1.4
- P-value: 0.7149
- N samples: 89

**Benchmark Score:**
- Correlation: 0.031 
- Linear fit: y = 0.010x + 1.2
- P-value: 0.7759
- N samples: 89

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.096 
- Linear fit: y = -0.005x + 0.3
- P-value: 0.3699
- N samples: 89

**Is Open Source:**
- Correlation: -0.071 
- Linear fit: y = -0.049x + 0.1
- P-value: 0.5112
- N samples: 89

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
- Correlation: -0.055 
- Linear fit: y = -0.048x + 0.1
- P-value: 0.6068
- N samples: 89

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
- Correlation: 0.396 ***
- Linear fit: y = 0.572x + 5.6

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.436 ***
- Linear fit: y = 0.889x + 17.2

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.397 ***
- Linear fit: y = 0.317x + 1.5

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.466 ***
- Linear fit: y = 0.657x + 14.7

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.598 ***
- Linear fit: y = 0.331x + -0.1

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.536 ***
- Linear fit: y = 0.210x + -1.8

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.968 ***, y = 0.824x + -0.8

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.954 ***, y = 0.874x + -0.9

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.838 ***, y = 0.529x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.814 ***, y = 0.534x + 0.3

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.729 ***, y = 0.424x + -0.3

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.714 ***, y = 0.215x + 0.0

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.667 ***, y = 0.257x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.626 ***, y = 0.173x + 0.8

**Category 2: Factual Errors vs 4b: Model Semantics Breach:**
  r = 0.617 ***, y = 0.223x + -0.0

**Category 2: Factual Errors vs Category 4: Technical Errors:**
  r = 0.598 ***, y = 0.331x + -0.1

**2b: Spurious Numeric vs 4b: Model Semantics Breach:**
  r = 0.589 ***, y = 0.233x + 0.3

**Category 4: Technical Errors vs 2b: Spurious Numeric:**
  r = 0.584 ***, y = 0.968x + 3.0

**Category 3: Logical Errors vs 4b: Model Semantics Breach:**
  r = 0.578 ***, y = 0.148x + -1.3

**Category 2: Factual Errors vs 4c: Visual Descr Mismatch:**
  r = 0.570 ***, y = 0.033x + -0.1

**3a: Unsupported Leap vs 4b: Model Semantics Breach:**
  r = 0.567 ***, y = 0.171x + -1.1

**Category 3: Logical Errors vs Category 4: Technical Errors:**
  r = 0.536 ***, y = 0.210x + -1.8

**2b: Spurious Numeric vs 4c: Visual Descr Mismatch:**
  r = 0.536 ***, y = 0.033x + -0.1

**Category 4: Technical Errors vs 3a: Unsupported Leap:**
  r = 0.506 ***, y = 1.100x + 12.7

**1b: Context Omission vs 3c: Circular Reasoning:**
  r = 0.478 ***, y = 0.019x + -0.0

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.468 ***, y = 0.562x + 11.2

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
