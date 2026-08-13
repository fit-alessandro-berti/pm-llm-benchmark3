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
- Correlation: -0.261 
- Linear fit: y = -0.183x + 8.3
- P-value: 0.0800
- N samples: 46

**Is Reasoning Model:**
- Correlation: -0.149 
- Linear fit: y = -1.540x + 3.6
- P-value: 0.3223
- N samples: 46

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Open Source:**
- Correlation: 0.078 
- Linear fit: y = 0.739x + 2.1
- P-value: 0.6072
- N samples: 46

**Days Since 2024-01-01:**
- Correlation: -0.046 
- Linear fit: y = -0.001x + 3.6
- P-value: 0.8464
- N samples: 20

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.205 
- Linear fit: y = -0.002x + 8.5
- P-value: 0.4306
- N samples: 17

**Is Open Source:**
- Correlation: -0.146 
- Linear fit: y = -1.913x + 8.4
- P-value: 0.3314
- N samples: 46

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Benchmark Score:**
- Correlation: -0.039 
- Linear fit: y = -0.037x + 8.7
- P-value: 0.7986
- N samples: 46

**Is Reasoning Model:**
- Correlation: -0.002 
- Linear fit: y = -0.031x + 7.5
- P-value: 0.9884
- N samples: 46

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.411 
- Linear fit: y = -0.004x + 26.1
- P-value: 0.1010
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: -0.309 
- Linear fit: y = -0.012x + 33.8
- P-value: 0.1849
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.307 *
- Linear fit: y = -6.312x + 27.5
- P-value: 0.0382
- N samples: 46

**Is Open Source:**
- Correlation: -0.227 
- Linear fit: y = -4.304x + 25.3
- P-value: 0.1289
- N samples: 46

**Benchmark Score:**
- Correlation: -0.223 
- Linear fit: y = -0.312x + 33.0
- P-value: 0.1363
- N samples: 46

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.317 *
- Linear fit: y = -0.150x + 6.4
- P-value: 0.0318
- N samples: 46

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.048 
- Linear fit: y = -0.335x + 1.9
- P-value: 0.7509
- N samples: 46

**Is Open Source:**
- Correlation: 0.027 
- Linear fit: y = 0.174x + 1.6
- P-value: 0.8578
- N samples: 46

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.287 
- Linear fit: y = -0.007x + 40.3
- P-value: 0.2647
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: -0.259 
- Linear fit: y = -0.028x + 57.2
- P-value: 0.2707
- N samples: 20

**Benchmark Score:**
- Correlation: -0.226 
- Linear fit: y = -0.676x + 56.2
- P-value: 0.1316
- N samples: 46

**Is Reasoning Model:**
- Correlation: -0.187 
- Linear fit: y = -8.250x + 40.5
- P-value: 0.2139
- N samples: 46

**Is Open Source:**
- Correlation: -0.132 
- Linear fit: y = -5.348x + 37.4
- P-value: 0.3834
- N samples: 46

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.261 
- Linear fit: y = -0.183x + 8.3
- P-value: 0.0800
- N samples: 46

**Is Reasoning Model:**
- Correlation: -0.149 
- Linear fit: y = -1.540x + 3.6
- P-value: 0.3223
- N samples: 46

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Open Source:**
- Correlation: 0.078 
- Linear fit: y = 0.739x + 2.1
- P-value: 0.6072
- N samples: 46

**Days Since 2024-01-01:**
- Correlation: -0.046 
- Linear fit: y = -0.001x + 3.6
- P-value: 0.8464
- N samples: 20

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.205 
- Linear fit: y = -0.002x + 8.5
- P-value: 0.4306
- N samples: 17

**Is Open Source:**
- Correlation: -0.146 
- Linear fit: y = -1.913x + 8.4
- P-value: 0.3314
- N samples: 46

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Benchmark Score:**
- Correlation: -0.039 
- Linear fit: y = -0.037x + 8.7
- P-value: 0.7986
- N samples: 46

**Is Reasoning Model:**
- Correlation: -0.002 
- Linear fit: y = -0.031x + 7.5
- P-value: 0.9884
- N samples: 46

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.411 
- Linear fit: y = -0.004x + 26.1
- P-value: 0.1010
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: -0.309 
- Linear fit: y = -0.012x + 33.8
- P-value: 0.1849
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.307 *
- Linear fit: y = -6.312x + 27.5
- P-value: 0.0382
- N samples: 46

**Is Open Source:**
- Correlation: -0.227 
- Linear fit: y = -4.304x + 25.3
- P-value: 0.1289
- N samples: 46

**Benchmark Score:**
- Correlation: -0.223 
- Linear fit: y = -0.312x + 33.0
- P-value: 0.1363
- N samples: 46

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.317 *
- Linear fit: y = -0.150x + 6.4
- P-value: 0.0318
- N samples: 46

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.048 
- Linear fit: y = -0.335x + 1.9
- P-value: 0.7509
- N samples: 46

**Is Open Source:**
- Correlation: 0.027 
- Linear fit: y = 0.174x + 1.6
- P-value: 0.8578
- N samples: 46

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.196 
- Linear fit: y = -0.062x + 2.8
- P-value: 0.1927
- N samples: 46

**Is Reasoning Model:**
- Correlation: -0.193 
- Linear fit: y = -0.906x + 1.5
- P-value: 0.1993
- N samples: 46

**Is Open Source:**
- Correlation: 0.080 
- Linear fit: y = 0.348x + 0.7
- P-value: 0.5953
- N samples: 46

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.8198
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: 0.049 
- Linear fit: y = 0.001x + 0.5
- P-value: 0.8384
- N samples: 20

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.220 
- Linear fit: y = -0.076x + 3.7
- P-value: 0.1411
- N samples: 46

**Model Size (B):**
- Correlation: -0.211 
- Linear fit: y = -0.001x + 1.9
- P-value: 0.4158
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: -0.080 
- Linear fit: y = -0.001x + 2.3
- P-value: 0.7365
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.068 
- Linear fit: y = -0.344x + 1.5
- P-value: 0.6547
- N samples: 46

**Is Open Source:**
- Correlation: 0.037 
- Linear fit: y = 0.174x + 1.2
- P-value: 0.8059
- N samples: 46

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.328 *
- Linear fit: y = -0.044x + 1.8
- P-value: 0.0261
- N samples: 46

**Is Reasoning Model:**
- Correlation: -0.146 
- Linear fit: y = -0.290x + 0.6
- P-value: 0.3345
- N samples: 46

**Is Open Source:**
- Correlation: 0.118 
- Linear fit: y = 0.217x + 0.3
- P-value: 0.4329
- N samples: 46

**Days Since 2024-01-01:**
- Correlation: -0.099 
- Linear fit: y = -0.000x + 0.7
- P-value: 0.6765
- N samples: 20

**Model Size (B):**
- Correlation: 0.035 
- Linear fit: y = 0.000x + 0.4
- P-value: 0.8934
- N samples: 17

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.323 
- Linear fit: y = -0.001x + 1.8
- P-value: 0.2066
- N samples: 17

**Is Open Source:**
- Correlation: 0.186 
- Linear fit: y = 0.609x + 1.1
- P-value: 0.2155
- N samples: 46

**Benchmark Score:**
- Correlation: -0.133 
- Linear fit: y = -0.032x + 2.4
- P-value: 0.3764
- N samples: 46

**Is Reasoning Model:**
- Correlation: 0.129 
- Linear fit: y = 0.460x + 1.1
- P-value: 0.3914
- N samples: 46

**Days Since 2024-01-01:**
- Correlation: 0.021 
- Linear fit: y = 0.000x + 1.1
- P-value: 0.9297
- N samples: 20

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.214 
- Linear fit: y = -2.565x + 7.1
- P-value: 0.1532
- N samples: 46

**Model Size (B):**
- Correlation: -0.162 
- Linear fit: y = -0.001x + 6.5
- P-value: 0.5338
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: -0.121 
- Linear fit: y = -0.004x + 8.8
- P-value: 0.6113
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.040 
- Linear fit: y = -0.527x + 6.2
- P-value: 0.7896
- N samples: 46

**Benchmark Score:**
- Correlation: -0.017 
- Linear fit: y = -0.015x + 6.3
- P-value: 0.9106
- N samples: 46

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: 0.360 
- Linear fit: y = 0.001x + -0.6
- P-value: 0.1188
- N samples: 20

**Model Size (B):**
- Correlation: 0.228 
- Linear fit: y = 0.000x + 0.2
- P-value: 0.3787
- N samples: 17

**Benchmark Score:**
- Correlation: 0.159 
- Linear fit: y = 0.010x + -0.1
- P-value: 0.2921
- N samples: 46

**Is Open Source:**
- Correlation: 0.051 
- Linear fit: y = 0.043x + 0.2
- P-value: 0.7366
- N samples: 46

**Is Reasoning Model:**
- Correlation: 0.039 
- Linear fit: y = 0.036x + 0.2
- P-value: 0.7993
- N samples: 46

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.322 
- Linear fit: y = -0.002x + 21.7
- P-value: 0.2069
- N samples: 17

**Days Since 2024-01-01:**
- Correlation: -0.299 
- Linear fit: y = -0.010x + 28.0
- P-value: 0.2000
- N samples: 20

**Is Open Source:**
- Correlation: -0.267 
- Linear fit: y = -3.870x + 21.0
- P-value: 0.0729
- N samples: 46

**Is Reasoning Model:**
- Correlation: -0.261 
- Linear fit: y = -4.116x + 21.9
- P-value: 0.0794
- N samples: 46

**Benchmark Score:**
- Correlation: -0.214 
- Linear fit: y = -0.229x + 26.3
- P-value: 0.1528
- N samples: 46

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.379 
- Linear fit: y = -0.001x + 4.4
- P-value: 0.1339
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.314 *
- Linear fit: y = -2.125x + 5.5
- P-value: 0.0334
- N samples: 46

**Days Since 2024-01-01:**
- Correlation: -0.187 
- Linear fit: y = -0.003x + 5.8
- P-value: 0.4300
- N samples: 20

**Benchmark Score:**
- Correlation: -0.169 
- Linear fit: y = -0.078x + 6.5
- P-value: 0.2607
- N samples: 46

**Is Open Source:**
- Correlation: -0.077 
- Linear fit: y = -0.478x + 4.3
- P-value: 0.6115
- N samples: 46

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.227 
- Linear fit: y = -0.005x + 0.2
- P-value: 0.1292
- N samples: 46

**Is Reasoning Model:**
- Correlation: -0.225 
- Linear fit: y = -0.071x + 0.1
- P-value: 0.1321
- N samples: 46

**Model Size (B):**
- Correlation: -0.170 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.5133
- N samples: 17

**Is Open Source:**
- Correlation: 0.149 
- Linear fit: y = 0.043x + 0.0
- P-value: 0.3228
- N samples: 46

**Days Since 2024-01-01:**
- Correlation: 0.100 
- Linear fit: y = 0.000x + -0.1
- P-value: 0.6745
- N samples: 20

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.487 *
- Linear fit: y = -0.007x + 6.3
- P-value: 0.0296
- N samples: 20

**Benchmark Score:**
- Correlation: -0.143 
- Linear fit: y = -0.033x + 1.5
- P-value: 0.3428
- N samples: 46

**Is Open Source:**
- Correlation: -0.112 
- Linear fit: y = -0.348x + 0.7
- P-value: 0.4598
- N samples: 46

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.8201
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.040 
- Linear fit: y = -0.134x + 0.6
- P-value: 0.7939
- N samples: 46

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.352 
- Linear fit: y = -0.004x + 4.0
- P-value: 0.1282
- N samples: 20

**Benchmark Score:**
- Correlation: -0.345 *
- Linear fit: y = -0.115x + 4.8
- P-value: 0.0188
- N samples: 46

**Model Size (B):**
- Correlation: -0.134 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.6083
- N samples: 17

**Is Open Source:**
- Correlation: 0.096 
- Linear fit: y = 0.435x + 1.0
- P-value: 0.5245
- N samples: 46

**Is Reasoning Model:**
- Correlation: -0.033 
- Linear fit: y = -0.161x + 1.3
- P-value: 0.8290
- N samples: 46

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.357 
- Linear fit: y = 0.000x + 0.0
- P-value: 0.1590
- N samples: 17

**Is Open Source:**
- Correlation: 0.213 
- Linear fit: y = 0.087x + 0.0
- P-value: 0.1548
- N samples: 46

**Is Reasoning Model:**
- Correlation: -0.091 
- Linear fit: y = -0.040x + 0.1
- P-value: 0.5491
- N samples: 46

**Benchmark Score:**
- Correlation: -0.065 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.6664
- N samples: 46

**Days Since 2024-01-01:**
- Correlation: -0.024 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.9216
- N samples: 20

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**4a_syntax_error vs Days Since 2024-01-01:**
  r = -0.487, y = -0.007x + 6.3

**category4_technical_errors vs Days Since 2024-01-01:**
  r = -0.458, y = -0.011x + 10.5

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.345, y = -0.115x + 4.8

**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.328, y = -0.044x + 1.8

**category4_technical_errors vs Benchmark Score:**
  r = -0.317, y = -0.150x + 6.4

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.314, y = -2.125x + 5.5

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.307, y = -6.312x + 27.5


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
- Correlation: 0.645 ***
- Linear fit: y = 0.887x + 5.3

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.667 ***
- Linear fit: y = 1.330x + 19.8

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.452 **
- Linear fit: y = 0.305x + 0.9

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.704 ***
- Linear fit: y = 1.021x + 15.5

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.452 **
- Linear fit: y = 0.222x + 0.0

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.468 **
- Linear fit: y = 0.158x + -2.0

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.965 ***, y = 0.739x + 2.0

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.965 ***, y = 0.886x + -0.8

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.929 ***, y = 0.457x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.888 ***, y = 0.626x + 0.1

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.863 ***, y = 0.393x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.797 ***, y = 0.262x + -2.0

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.776 ***, y = 0.150x + -0.0

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.766 ***, y = 0.372x + -0.2

**1b: Context Omission vs 1c: Prompt Contradiction:**
  r = 0.746 ***, y = 0.293x + -0.0

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.736 ***, y = 0.465x + -4.9

**2b: Spurious Numeric vs 3a: Unsupported Leap:**
  r = 0.730 ***, y = 0.883x + 13.9

**1a: Instruction Override vs 3b: Self Contradiction:**
  r = 0.727 ***, y = 1.046x + 3.1

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.704 ***, y = 1.021x + 15.5

**Category 3: Logical Errors vs 1a: Instruction Override:**
  r = 0.702 ***, y = 0.160x + -2.8

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.695 ***, y = 0.771x + 13.3

**Category 1: Input Misalignment vs 3b: Self Contradiction:**
  r = 0.679 ***, y = 0.445x + 2.9

**Category 1: Input Misalignment vs Category 3: Logical Errors:**
  r = 0.667 ***, y = 1.330x + 19.8

**Category 2: Factual Errors vs 1a: Instruction Override:**
  r = 0.663 ***, y = 0.220x + -0.8

**1a: Instruction Override vs 2b: Spurious Numeric:**
  r = 0.653 ***, y = 1.808x + 4.3

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = 0.645 ***, y = 0.887x + 5.3

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
