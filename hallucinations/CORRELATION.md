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
- Correlation: -0.235 
- Linear fit: y = -0.165x + 7.8
- P-value: 0.0873
- N samples: 54

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.127 
- Linear fit: y = -1.272x + 3.4
- P-value: 0.3599
- N samples: 54

**Days Since 2024-01-01:**
- Correlation: -0.046 
- Linear fit: y = -0.001x + 3.6
- P-value: 0.8464
- N samples: 20

**Is Open Source:**
- Correlation: 0.037 
- Linear fit: y = 0.332x + 2.3
- P-value: 0.7903
- N samples: 54

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.205 
- Linear fit: y = -0.002x + 8.5
- P-value: 0.4306
- N samples: 17

**Is Open Source:**
- Correlation: -0.189 
- Linear fit: y = -2.481x + 8.8
- P-value: 0.1710
- N samples: 54

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Is Reasoning Model:**
- Correlation: 0.034 
- Linear fit: y = 0.492x + 7.2
- P-value: 0.8092
- N samples: 54

**Benchmark Score:**
- Correlation: -0.007 
- Linear fit: y = -0.007x + 7.8
- P-value: 0.9586
- N samples: 54

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.411 
- Linear fit: y = -0.004x + 26.1
- P-value: 0.1010
- N samples: 17

**Is Open Source:**
- Correlation: -0.340 *
- Linear fit: y = -6.604x + 26.6
- P-value: 0.0118
- N samples: 54

**Days Since 2024-01-01:**
- Correlation: -0.309 
- Linear fit: y = -0.012x + 33.8
- P-value: 0.1849
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.299 *
- Linear fit: y = -6.467x + 28.1
- P-value: 0.0282
- N samples: 54

**Benchmark Score:**
- Correlation: -0.156 
- Linear fit: y = -0.237x + 31.1
- P-value: 0.2597
- N samples: 54

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.280 *
- Linear fit: y = -0.134x + 6.0
- P-value: 0.0399
- N samples: 54

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.041 
- Linear fit: y = -0.277x + 1.9
- P-value: 0.7698
- N samples: 54

**Is Open Source:**
- Correlation: -0.004 
- Linear fit: y = -0.025x + 1.7
- P-value: 0.9768
- N samples: 54

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

**Is Open Source:**
- Correlation: -0.223 
- Linear fit: y = -8.923x + 39.5
- P-value: 0.1058
- N samples: 54

**Benchmark Score:**
- Correlation: -0.169 
- Linear fit: y = -0.530x + 52.2
- P-value: 0.2228
- N samples: 54

**Is Reasoning Model:**
- Correlation: -0.167 
- Linear fit: y = -7.472x + 40.6
- P-value: 0.2273
- N samples: 54

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.235 
- Linear fit: y = -0.165x + 7.8
- P-value: 0.0873
- N samples: 54

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.127 
- Linear fit: y = -1.272x + 3.4
- P-value: 0.3599
- N samples: 54

**Days Since 2024-01-01:**
- Correlation: -0.046 
- Linear fit: y = -0.001x + 3.6
- P-value: 0.8464
- N samples: 20

**Is Open Source:**
- Correlation: 0.037 
- Linear fit: y = 0.332x + 2.3
- P-value: 0.7903
- N samples: 54

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.205 
- Linear fit: y = -0.002x + 8.5
- P-value: 0.4306
- N samples: 17

**Is Open Source:**
- Correlation: -0.189 
- Linear fit: y = -2.481x + 8.8
- P-value: 0.1710
- N samples: 54

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Is Reasoning Model:**
- Correlation: 0.034 
- Linear fit: y = 0.492x + 7.2
- P-value: 0.8092
- N samples: 54

**Benchmark Score:**
- Correlation: -0.007 
- Linear fit: y = -0.007x + 7.8
- P-value: 0.9586
- N samples: 54

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.411 
- Linear fit: y = -0.004x + 26.1
- P-value: 0.1010
- N samples: 17

**Is Open Source:**
- Correlation: -0.340 *
- Linear fit: y = -6.604x + 26.6
- P-value: 0.0118
- N samples: 54

**Days Since 2024-01-01:**
- Correlation: -0.309 
- Linear fit: y = -0.012x + 33.8
- P-value: 0.1849
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.299 *
- Linear fit: y = -6.467x + 28.1
- P-value: 0.0282
- N samples: 54

**Benchmark Score:**
- Correlation: -0.156 
- Linear fit: y = -0.237x + 31.1
- P-value: 0.2597
- N samples: 54

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.280 *
- Linear fit: y = -0.134x + 6.0
- P-value: 0.0399
- N samples: 54

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.041 
- Linear fit: y = -0.277x + 1.9
- P-value: 0.7698
- N samples: 54

**Is Open Source:**
- Correlation: -0.004 
- Linear fit: y = -0.025x + 1.7
- P-value: 0.9768
- N samples: 54

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.187 
- Linear fit: y = -0.060x + 2.7
- P-value: 0.1748
- N samples: 54

**Is Reasoning Model:**
- Correlation: -0.174 
- Linear fit: y = -0.785x + 1.4
- P-value: 0.2095
- N samples: 54

**Is Open Source:**
- Correlation: 0.061 
- Linear fit: y = 0.247x + 0.7
- P-value: 0.6613
- N samples: 54

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
- Correlation: -0.190 
- Linear fit: y = -0.067x + 3.4
- P-value: 0.1691
- N samples: 54

**Days Since 2024-01-01:**
- Correlation: -0.080 
- Linear fit: y = -0.001x + 2.3
- P-value: 0.7365
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.039 
- Linear fit: y = -0.195x + 1.4
- P-value: 0.7810
- N samples: 54

**Is Open Source:**
- Correlation: -0.012 
- Linear fit: y = -0.055x + 1.3
- P-value: 0.9303
- N samples: 54

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.276 *
- Linear fit: y = -0.038x + 1.6
- P-value: 0.0436
- N samples: 54

**Is Reasoning Model:**
- Correlation: -0.147 
- Linear fit: y = -0.292x + 0.6
- P-value: 0.2888
- N samples: 54

**Days Since 2024-01-01:**
- Correlation: -0.099 
- Linear fit: y = -0.000x + 0.7
- P-value: 0.6765
- N samples: 20

**Is Open Source:**
- Correlation: 0.079 
- Linear fit: y = 0.140x + 0.3
- P-value: 0.5721
- N samples: 54

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
- Correlation: 0.216 
- Linear fit: y = 0.692x + 1.0
- P-value: 0.1160
- N samples: 54

**Benchmark Score:**
- Correlation: -0.140 
- Linear fit: y = -0.035x + 2.5
- P-value: 0.3113
- N samples: 54

**Is Reasoning Model:**
- Correlation: 0.103 
- Linear fit: y = 0.369x + 1.1
- P-value: 0.4566
- N samples: 54

**Days Since 2024-01-01:**
- Correlation: 0.021 
- Linear fit: y = 0.000x + 1.1
- P-value: 0.9297
- N samples: 20

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.260 
- Linear fit: y = -3.231x + 7.5
- P-value: 0.0573
- N samples: 54

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

**Benchmark Score:**
- Correlation: 0.013 
- Linear fit: y = 0.013x + 5.5
- P-value: 0.9235
- N samples: 54

**Is Reasoning Model:**
- Correlation: 0.001 
- Linear fit: y = 0.015x + 5.9
- P-value: 0.9936
- N samples: 54

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
- Correlation: 0.193 
- Linear fit: y = 0.015x + -0.2
- P-value: 0.1624
- N samples: 54

**Is Reasoning Model:**
- Correlation: 0.099 
- Linear fit: y = 0.108x + 0.2
- P-value: 0.4766
- N samples: 54

**Is Open Source:**
- Correlation: 0.059 
- Linear fit: y = 0.058x + 0.2
- P-value: 0.6710
- N samples: 54

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.377 **
- Linear fit: y = -5.720x + 22.1
- P-value: 0.0050
- N samples: 54

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

**Is Reasoning Model:**
- Correlation: -0.268 
- Linear fit: y = -4.538x + 22.7
- P-value: 0.0502
- N samples: 54

**Benchmark Score:**
- Correlation: -0.138 
- Linear fit: y = -0.164x + 24.7
- P-value: 0.3192
- N samples: 54

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.379 
- Linear fit: y = -0.001x + 4.4
- P-value: 0.1339
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.279 *
- Linear fit: y = -1.887x + 5.4
- P-value: 0.0407
- N samples: 54

**Days Since 2024-01-01:**
- Correlation: -0.187 
- Linear fit: y = -0.003x + 5.8
- P-value: 0.4300
- N samples: 20

**Is Open Source:**
- Correlation: -0.147 
- Linear fit: y = -0.887x + 4.5
- P-value: 0.2901
- N samples: 54

**Benchmark Score:**
- Correlation: -0.145 
- Linear fit: y = -0.069x + 6.2
- P-value: 0.2948
- N samples: 54

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.170 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.5133
- N samples: 17

**Benchmark Score:**
- Correlation: -0.134 
- Linear fit: y = -0.004x + 0.2
- P-value: 0.3356
- N samples: 54

**Days Since 2024-01-01:**
- Correlation: 0.100 
- Linear fit: y = 0.000x + -0.1
- P-value: 0.6745
- N samples: 20

**Is Reasoning Model:**
- Correlation: -0.097 
- Linear fit: y = -0.041x + 0.1
- P-value: 0.4840
- N samples: 54

**Is Open Source:**
- Correlation: 0.007 
- Linear fit: y = 0.003x + 0.0
- P-value: 0.9584
- N samples: 54

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.487 *
- Linear fit: y = -0.007x + 6.3
- P-value: 0.0296
- N samples: 20

**Benchmark Score:**
- Correlation: -0.142 
- Linear fit: y = -0.032x + 1.5
- P-value: 0.3040
- N samples: 54

**Is Open Source:**
- Correlation: -0.104 
- Linear fit: y = -0.302x + 0.6
- P-value: 0.4530
- N samples: 54

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.8201
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.046 
- Linear fit: y = -0.149x + 0.5
- P-value: 0.7411
- N samples: 54

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.352 
- Linear fit: y = -0.004x + 4.0
- P-value: 0.1282
- N samples: 20

**Benchmark Score:**
- Correlation: -0.291 *
- Linear fit: y = -0.099x + 4.4
- P-value: 0.0325
- N samples: 54

**Model Size (B):**
- Correlation: -0.134 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.6083
- N samples: 17

**Is Open Source:**
- Correlation: 0.046 
- Linear fit: y = 0.201x + 1.1
- P-value: 0.7404
- N samples: 54

**Is Reasoning Model:**
- Correlation: -0.018 
- Linear fit: y = -0.087x + 1.3
- P-value: 0.8973
- N samples: 54

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.357 
- Linear fit: y = 0.000x + 0.0
- P-value: 0.1590
- N samples: 17

**Is Open Source:**
- Correlation: 0.204 
- Linear fit: y = 0.077x + -0.0
- P-value: 0.1399
- N samples: 54

**Is Reasoning Model:**
- Correlation: -0.097 
- Linear fit: y = -0.041x + 0.1
- P-value: 0.4840
- N samples: 54

**Benchmark Score:**
- Correlation: -0.075 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.5891
- N samples: 54

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

**3a_unsupported_leap vs Is Open Source:**
  r = -0.377, y = -5.720x + 22.1

**category3_logical_errors vs Is Open Source:**
  r = -0.340, y = -6.604x + 26.6


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
- Correlation: 0.664 ***
- Linear fit: y = 0.971x + 5.1

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.603 ***
- Linear fit: y = 1.304x + 20.2

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.464 ***
- Linear fit: y = 0.315x + 0.9

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.650 ***
- Linear fit: y = 0.962x + 16.2

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.477 ***
- Linear fit: y = 0.221x + -0.0

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.438 ***
- Linear fit: y = 0.138x + -1.6

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.967 ***, y = 0.914x + -1.0

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.967 ***, y = 0.757x + 1.6

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.928 ***, y = 0.466x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.893 ***, y = 0.637x + 0.1

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.863 ***, y = 0.390x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.776 ***, y = 0.242x + -1.6

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.759 ***, y = 0.361x + -0.2

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.723 ***, y = 0.144x + 0.0

**1a: Instruction Override vs 3b: Self Contradiction:**
  r = 0.705 ***, y = 1.053x + 3.2

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.677 ***, y = 0.433x + -4.2

**Category 1: Input Misalignment vs 3b: Self Contradiction:**
  r = 0.675 ***, y = 0.455x + 2.9

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = 0.664 ***, y = 0.971x + 5.1

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = 0.661 ***, y = 0.227x + -0.5

**1b: Context Omission vs 1c: Prompt Contradiction:**
  r = 0.660 ***, y = 0.261x + 0.1

**Category 2: Factual Errors vs 1a: Instruction Override:**
  r = 0.657 ***, y = 0.203x + -0.7

**Category 1: Input Misalignment vs 2b: Spurious Numeric:**
  r = 0.656 ***, y = 0.907x + 3.7

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.650 ***, y = 0.962x + 16.2

**1a: Instruction Override vs 1b: Context Omission:**
  r = 0.650 ***, y = 0.724x + 0.7

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = 0.646 ***, y = 1.778x + 3.7

**1a: Instruction Override vs 2b: Spurious Numeric:**
  r = 0.641 ***, y = 1.962x + 4.3

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
