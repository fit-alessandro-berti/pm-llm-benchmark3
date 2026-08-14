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
- Correlation: -0.251 
- Linear fit: y = -0.177x + 8.2
- P-value: 0.0850
- N samples: 48

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.132 
- Linear fit: y = -1.366x + 3.6
- P-value: 0.3703
- N samples: 48

**Is Open Source:**
- Correlation: 0.058 
- Linear fit: y = 0.542x + 2.3
- P-value: 0.6969
- N samples: 48

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
- Correlation: -0.190 
- Linear fit: y = -2.542x + 8.9
- P-value: 0.1947
- N samples: 48

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Benchmark Score:**
- Correlation: -0.022 
- Linear fit: y = -0.022x + 8.3
- P-value: 0.8839
- N samples: 48

**Is Reasoning Model:**
- Correlation: 0.014 
- Linear fit: y = 0.206x + 7.5
- P-value: 0.9246
- N samples: 48

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
- Linear fit: y = -6.441x + 27.5
- P-value: 0.0337
- N samples: 48

**Is Open Source:**
- Correlation: -0.260 
- Linear fit: y = -4.958x + 25.4
- P-value: 0.0742
- N samples: 48

**Benchmark Score:**
- Correlation: -0.209 
- Linear fit: y = -0.299x + 32.4
- P-value: 0.1548
- N samples: 48

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.316 *
- Linear fit: y = -0.149x + 6.4
- P-value: 0.0286
- N samples: 48

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.045 
- Linear fit: y = -0.311x + 1.9
- P-value: 0.7610
- N samples: 48

**Is Open Source:**
- Correlation: 0.027 
- Linear fit: y = 0.167x + 1.6
- P-value: 0.8577
- N samples: 48

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
- Correlation: -0.210 
- Linear fit: y = -0.642x + 55.3
- P-value: 0.1521
- N samples: 48

**Is Reasoning Model:**
- Correlation: -0.177 
- Linear fit: y = -7.941x + 40.5
- P-value: 0.2275
- N samples: 48

**Is Open Source:**
- Correlation: -0.168 
- Linear fit: y = -6.833x + 38.3
- P-value: 0.2537
- N samples: 48

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.251 
- Linear fit: y = -0.177x + 8.2
- P-value: 0.0850
- N samples: 48

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.132 
- Linear fit: y = -1.366x + 3.6
- P-value: 0.3703
- N samples: 48

**Is Open Source:**
- Correlation: 0.058 
- Linear fit: y = 0.542x + 2.3
- P-value: 0.6969
- N samples: 48

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
- Correlation: -0.190 
- Linear fit: y = -2.542x + 8.9
- P-value: 0.1947
- N samples: 48

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Benchmark Score:**
- Correlation: -0.022 
- Linear fit: y = -0.022x + 8.3
- P-value: 0.8839
- N samples: 48

**Is Reasoning Model:**
- Correlation: 0.014 
- Linear fit: y = 0.206x + 7.5
- P-value: 0.9246
- N samples: 48

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
- Linear fit: y = -6.441x + 27.5
- P-value: 0.0337
- N samples: 48

**Is Open Source:**
- Correlation: -0.260 
- Linear fit: y = -4.958x + 25.4
- P-value: 0.0742
- N samples: 48

**Benchmark Score:**
- Correlation: -0.209 
- Linear fit: y = -0.299x + 32.4
- P-value: 0.1548
- N samples: 48

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.316 *
- Linear fit: y = -0.149x + 6.4
- P-value: 0.0286
- N samples: 48

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.045 
- Linear fit: y = -0.311x + 1.9
- P-value: 0.7610
- N samples: 48

**Is Open Source:**
- Correlation: 0.027 
- Linear fit: y = 0.167x + 1.6
- P-value: 0.8577
- N samples: 48

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.191 
- Linear fit: y = -0.061x + 2.8
- P-value: 0.1935
- N samples: 48

**Is Reasoning Model:**
- Correlation: -0.183 
- Linear fit: y = -0.853x + 1.5
- P-value: 0.2143
- N samples: 48

**Is Open Source:**
- Correlation: 0.069 
- Linear fit: y = 0.292x + 0.8
- P-value: 0.6428
- N samples: 48

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

**Model Size (B):**
- Correlation: -0.211 
- Linear fit: y = -0.001x + 1.9
- P-value: 0.4158
- N samples: 17

**Benchmark Score:**
- Correlation: -0.202 
- Linear fit: y = -0.071x + 3.6
- P-value: 0.1679
- N samples: 48

**Days Since 2024-01-01:**
- Correlation: -0.080 
- Linear fit: y = -0.001x + 2.3
- P-value: 0.7365
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.046 
- Linear fit: y = -0.235x + 1.5
- P-value: 0.7585
- N samples: 48

**Is Open Source:**
- Correlation: 0.000 
- Linear fit: y = 0.000x + 1.3
- P-value: 1.0000
- N samples: 48

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.330 *
- Linear fit: y = -0.045x + 1.8
- P-value: 0.0220
- N samples: 48

**Is Reasoning Model:**
- Correlation: -0.139 
- Linear fit: y = -0.277x + 0.6
- P-value: 0.3447
- N samples: 48

**Is Open Source:**
- Correlation: 0.138 
- Linear fit: y = 0.250x + 0.2
- P-value: 0.3488
- N samples: 48

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
- Correlation: 0.180 
- Linear fit: y = 0.583x + 1.0
- P-value: 0.2220
- N samples: 48

**Benchmark Score:**
- Correlation: -0.136 
- Linear fit: y = -0.033x + 2.4
- P-value: 0.3582
- N samples: 48

**Is Reasoning Model:**
- Correlation: 0.103 
- Linear fit: y = 0.370x + 1.1
- P-value: 0.4841
- N samples: 48

**Days Since 2024-01-01:**
- Correlation: 0.021 
- Linear fit: y = 0.000x + 1.1
- P-value: 0.9297
- N samples: 20

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.255 
- Linear fit: y = -3.167x + 7.7
- P-value: 0.0809
- N samples: 48

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
- Correlation: -0.014 
- Linear fit: y = -0.185x + 6.2
- P-value: 0.9274
- N samples: 48

**Benchmark Score:**
- Correlation: 0.002 
- Linear fit: y = 0.002x + 6.0
- P-value: 0.9906
- N samples: 48

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
- Correlation: 0.155 
- Linear fit: y = 0.010x + -0.1
- P-value: 0.2940
- N samples: 48

**Is Open Source:**
- Correlation: 0.050 
- Linear fit: y = 0.042x + 0.2
- P-value: 0.7379
- N samples: 48

**Is Reasoning Model:**
- Correlation: 0.023 
- Linear fit: y = 0.021x + 0.2
- P-value: 0.8782
- N samples: 48

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
- Correlation: -0.289 *
- Linear fit: y = -4.208x + 21.0
- P-value: 0.0461
- N samples: 48

**Is Reasoning Model:**
- Correlation: -0.271 
- Linear fit: y = -4.340x + 21.9
- P-value: 0.0621
- N samples: 48

**Benchmark Score:**
- Correlation: -0.204 
- Linear fit: y = -0.223x + 25.9
- P-value: 0.1639
- N samples: 48

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.379 
- Linear fit: y = -0.001x + 4.4
- P-value: 0.1339
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.299 *
- Linear fit: y = -2.059x + 5.5
- P-value: 0.0389
- N samples: 48

**Days Since 2024-01-01:**
- Correlation: -0.187 
- Linear fit: y = -0.003x + 5.8
- P-value: 0.4300
- N samples: 20

**Benchmark Score:**
- Correlation: -0.153 
- Linear fit: y = -0.072x + 6.3
- P-value: 0.2995
- N samples: 48

**Is Open Source:**
- Correlation: -0.120 
- Linear fit: y = -0.750x + 4.4
- P-value: 0.4171
- N samples: 48

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.170 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.5133
- N samples: 17

**Benchmark Score:**
- Correlation: -0.126 
- Linear fit: y = -0.004x + 0.2
- P-value: 0.3942
- N samples: 48

**Days Since 2024-01-01:**
- Correlation: 0.100 
- Linear fit: y = 0.000x + -0.1
- P-value: 0.6745
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.096 
- Linear fit: y = -0.042x + 0.1
- P-value: 0.5182
- N samples: 48

**Is Open Source:**
- Correlation: 0.000 
- Linear fit: y = 0.000x + 0.0
- P-value: 1.0000
- N samples: 48

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.487 *
- Linear fit: y = -0.007x + 6.3
- P-value: 0.0296
- N samples: 20

**Benchmark Score:**
- Correlation: -0.144 
- Linear fit: y = -0.033x + 1.5
- P-value: 0.3283
- N samples: 48

**Is Open Source:**
- Correlation: -0.109 
- Linear fit: y = -0.333x + 0.6
- P-value: 0.4602
- N samples: 48

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.8201
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.048 
- Linear fit: y = -0.160x + 0.6
- P-value: 0.7484
- N samples: 48

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.352 
- Linear fit: y = -0.004x + 4.0
- P-value: 0.1282
- N samples: 20

**Benchmark Score:**
- Correlation: -0.342 *
- Linear fit: y = -0.114x + 4.8
- P-value: 0.0174
- N samples: 48

**Model Size (B):**
- Correlation: -0.134 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.6083
- N samples: 17

**Is Open Source:**
- Correlation: 0.094 
- Linear fit: y = 0.417x + 1.0
- P-value: 0.5252
- N samples: 48

**Is Reasoning Model:**
- Correlation: -0.022 
- Linear fit: y = -0.109x + 1.3
- P-value: 0.8799
- N samples: 48

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.357 
- Linear fit: y = 0.000x + 0.0
- P-value: 0.1590
- N samples: 17

**Is Open Source:**
- Correlation: 0.209 
- Linear fit: y = 0.083x + 0.0
- P-value: 0.1550
- N samples: 48

**Is Reasoning Model:**
- Correlation: -0.096 
- Linear fit: y = -0.042x + 0.1
- P-value: 0.5182
- N samples: 48

**Benchmark Score:**
- Correlation: -0.066 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.6548
- N samples: 48

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
  r = -0.342, y = -0.114x + 4.8

**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.330, y = -0.045x + 1.8

**category4_technical_errors vs Benchmark Score:**
  r = -0.316, y = -0.149x + 6.4

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.307, y = -6.441x + 27.5


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
- Correlation: 0.647 ***
- Linear fit: y = 0.920x + 5.2

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.652 ***
- Linear fit: y = 1.324x + 19.5

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.449 **
- Linear fit: y = 0.300x + 0.9

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.701 ***
- Linear fit: y = 1.002x + 15.3

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.435 **
- Linear fit: y = 0.205x + 0.1

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.454 **
- Linear fit: y = 0.149x + -1.7

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.966 ***, y = 0.901x + -0.8

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.965 ***, y = 0.736x + 2.0

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.927 ***, y = 0.464x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.887 ***, y = 0.627x + 0.1

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.863 ***, y = 0.391x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.801 ***, y = 0.263x + -2.0

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.763 ***, y = 0.372x + -0.2

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.757 ***, y = 0.146x + -0.0

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.719 ***, y = 0.469x + -4.7

**1a: Instruction Override vs 3b: Self Contradiction:**
  r = 0.719 ***, y = 1.059x + 3.1

**1b: Context Omission vs 1c: Prompt Contradiction:**
  r = 0.706 ***, y = 0.272x + 0.0

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.701 ***, y = 1.002x + 15.3

**2b: Spurious Numeric vs 3a: Unsupported Leap:**
  r = 0.693 ***, y = 0.810x + 13.9

**Category 3: Logical Errors vs 1a: Instruction Override:**
  r = 0.686 ***, y = 0.153x + -2.6

**Category 1: Input Misalignment vs 3b: Self Contradiction:**
  r = 0.678 ***, y = 0.452x + 2.9

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.677 ***, y = 0.737x + 13.2

**Category 2: Factual Errors vs 1a: Instruction Override:**
  r = 0.653 ***, y = 0.208x + -0.7

**Category 1: Input Misalignment vs Category 3: Logical Errors:**
  r = 0.652 ***, y = 1.324x + 19.5

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = 0.647 ***, y = 0.920x + 5.2

**1a: Instruction Override vs 1b: Context Omission:**
  r = 0.642 ***, y = 0.710x + 0.7

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
