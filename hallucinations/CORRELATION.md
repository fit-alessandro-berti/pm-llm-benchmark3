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
- P-value: 0.0764
- N samples: 47

**Is Reasoning Model:**
- Correlation: -0.147 
- Linear fit: y = -1.511x + 3.6
- P-value: 0.3240
- N samples: 47

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Open Source:**
- Correlation: 0.079 
- Linear fit: y = 0.745x + 2.1
- P-value: 0.5966
- N samples: 47

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
- Correlation: -0.159 
- Linear fit: y = -2.060x + 8.4
- P-value: 0.2870
- N samples: 47

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Benchmark Score:**
- Correlation: -0.037 
- Linear fit: y = -0.036x + 8.5
- P-value: 0.8053
- N samples: 47

**Is Reasoning Model:**
- Correlation: -0.012 
- Linear fit: y = -0.167x + 7.5
- P-value: 0.9376
- N samples: 47

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.411 
- Linear fit: y = -0.004x + 26.1
- P-value: 0.1010
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.319 *
- Linear fit: y = -6.682x + 27.5
- P-value: 0.0291
- N samples: 47

**Days Since 2024-01-01:**
- Correlation: -0.309 
- Linear fit: y = -0.012x + 33.8
- P-value: 0.1849
- N samples: 20

**Is Open Source:**
- Correlation: -0.250 
- Linear fit: y = -4.803x + 25.3
- P-value: 0.0897
- N samples: 47

**Benchmark Score:**
- Correlation: -0.215 
- Linear fit: y = -0.307x + 32.5
- P-value: 0.1475
- N samples: 47

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
- Linear fit: y = -0.150x + 6.5
- P-value: 0.0298
- N samples: 47

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.047 
- Linear fit: y = -0.323x + 1.9
- P-value: 0.7560
- N samples: 47

**Is Open Source:**
- Correlation: 0.029 
- Linear fit: y = 0.183x + 1.6
- P-value: 0.8473
- N samples: 47

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
- Correlation: -0.222 
- Linear fit: y = -0.670x + 55.6
- P-value: 0.1340
- N samples: 47

**Is Reasoning Model:**
- Correlation: -0.197 
- Linear fit: y = -8.712x + 40.5
- P-value: 0.1854
- N samples: 47

**Is Open Source:**
- Correlation: -0.147 
- Linear fit: y = -5.976x + 37.4
- P-value: 0.3228
- N samples: 47

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.261 
- Linear fit: y = -0.183x + 8.3
- P-value: 0.0764
- N samples: 47

**Is Reasoning Model:**
- Correlation: -0.147 
- Linear fit: y = -1.511x + 3.6
- P-value: 0.3240
- N samples: 47

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Open Source:**
- Correlation: 0.079 
- Linear fit: y = 0.745x + 2.1
- P-value: 0.5966
- N samples: 47

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
- Correlation: -0.159 
- Linear fit: y = -2.060x + 8.4
- P-value: 0.2870
- N samples: 47

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Benchmark Score:**
- Correlation: -0.037 
- Linear fit: y = -0.036x + 8.5
- P-value: 0.8053
- N samples: 47

**Is Reasoning Model:**
- Correlation: -0.012 
- Linear fit: y = -0.167x + 7.5
- P-value: 0.9376
- N samples: 47

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.411 
- Linear fit: y = -0.004x + 26.1
- P-value: 0.1010
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.319 *
- Linear fit: y = -6.682x + 27.5
- P-value: 0.0291
- N samples: 47

**Days Since 2024-01-01:**
- Correlation: -0.309 
- Linear fit: y = -0.012x + 33.8
- P-value: 0.1849
- N samples: 20

**Is Open Source:**
- Correlation: -0.250 
- Linear fit: y = -4.803x + 25.3
- P-value: 0.0897
- N samples: 47

**Benchmark Score:**
- Correlation: -0.215 
- Linear fit: y = -0.307x + 32.5
- P-value: 0.1475
- N samples: 47

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
- Linear fit: y = -0.150x + 6.5
- P-value: 0.0298
- N samples: 47

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.047 
- Linear fit: y = -0.323x + 1.9
- P-value: 0.7560
- N samples: 47

**Is Open Source:**
- Correlation: 0.029 
- Linear fit: y = 0.183x + 1.6
- P-value: 0.8473
- N samples: 47

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.196 
- Linear fit: y = -0.062x + 2.9
- P-value: 0.1874
- N samples: 47

**Is Reasoning Model:**
- Correlation: -0.191 
- Linear fit: y = -0.894x + 1.5
- P-value: 0.1983
- N samples: 47

**Is Open Source:**
- Correlation: 0.081 
- Linear fit: y = 0.346x + 0.7
- P-value: 0.5891
- N samples: 47

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
- P-value: 0.1372
- N samples: 47

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
- Correlation: -0.069 
- Linear fit: y = -0.348x + 1.5
- P-value: 0.6450
- N samples: 47

**Is Open Source:**
- Correlation: 0.034 
- Linear fit: y = 0.159x + 1.2
- P-value: 0.8180
- N samples: 47

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.328 *
- Linear fit: y = -0.045x + 1.8
- P-value: 0.0245
- N samples: 47

**Is Reasoning Model:**
- Correlation: -0.135 
- Linear fit: y = -0.268x + 0.6
- P-value: 0.3672
- N samples: 47

**Is Open Source:**
- Correlation: 0.131 
- Linear fit: y = 0.239x + 0.3
- P-value: 0.3799
- N samples: 47

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
- Correlation: 0.165 
- Linear fit: y = 0.538x + 1.1
- P-value: 0.2677
- N samples: 47

**Benchmark Score:**
- Correlation: -0.131 
- Linear fit: y = -0.032x + 2.4
- P-value: 0.3818
- N samples: 47

**Is Reasoning Model:**
- Correlation: 0.116 
- Linear fit: y = 0.413x + 1.1
- P-value: 0.4375
- N samples: 47

**Days Since 2024-01-01:**
- Correlation: 0.021 
- Linear fit: y = 0.000x + 1.1
- P-value: 0.9297
- N samples: 20

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.221 
- Linear fit: y = -2.630x + 7.1
- P-value: 0.1350
- N samples: 47

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
- Correlation: -0.047 
- Linear fit: y = -0.608x + 6.2
- P-value: 0.7547
- N samples: 47

**Benchmark Score:**
- Correlation: -0.016 
- Linear fit: y = -0.014x + 6.2
- P-value: 0.9155
- N samples: 47

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
- P-value: 0.2844
- N samples: 47

**Is Open Source:**
- Correlation: 0.038 
- Linear fit: y = 0.033x + 0.2
- P-value: 0.7972
- N samples: 47

**Is Reasoning Model:**
- Correlation: 0.030 
- Linear fit: y = 0.028x + 0.2
- P-value: 0.8393
- N samples: 47

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
- Linear fit: y = -4.250x + 21.0
- P-value: 0.0487
- N samples: 47

**Is Reasoning Model:**
- Correlation: -0.275 
- Linear fit: y = -4.413x + 21.9
- P-value: 0.0616
- N samples: 47

**Benchmark Score:**
- Correlation: -0.206 
- Linear fit: y = -0.225x + 26.0
- P-value: 0.1654
- N samples: 47

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.379 
- Linear fit: y = -0.001x + 4.4
- P-value: 0.1339
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.323 *
- Linear fit: y = -2.197x + 5.5
- P-value: 0.0266
- N samples: 47

**Days Since 2024-01-01:**
- Correlation: -0.187 
- Linear fit: y = -0.003x + 5.8
- P-value: 0.4300
- N samples: 20

**Benchmark Score:**
- Correlation: -0.165 
- Linear fit: y = -0.077x + 6.4
- P-value: 0.2665
- N samples: 47

**Is Open Source:**
- Correlation: -0.096 
- Linear fit: y = -0.594x + 4.3
- P-value: 0.5228
- N samples: 47

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.227 
- Linear fit: y = -0.005x + 0.2
- P-value: 0.1256
- N samples: 47

**Is Reasoning Model:**
- Correlation: -0.226 
- Linear fit: y = -0.071x + 0.1
- P-value: 0.1260
- N samples: 47

**Model Size (B):**
- Correlation: -0.170 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.5133
- N samples: 17

**Is Open Source:**
- Correlation: 0.144 
- Linear fit: y = 0.042x + 0.0
- P-value: 0.3331
- N samples: 47

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
- Correlation: -0.142 
- Linear fit: y = -0.033x + 1.5
- P-value: 0.3402
- N samples: 47

**Is Open Source:**
- Correlation: -0.117 
- Linear fit: y = -0.361x + 0.7
- P-value: 0.4339
- N samples: 47

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.8201
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.044 
- Linear fit: y = -0.147x + 0.6
- P-value: 0.7707
- N samples: 47

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
- P-value: 0.0174
- N samples: 47

**Model Size (B):**
- Correlation: -0.134 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.6083
- N samples: 17

**Is Open Source:**
- Correlation: 0.103 
- Linear fit: y = 0.460x + 1.0
- P-value: 0.4917
- N samples: 47

**Is Reasoning Model:**
- Correlation: -0.027 
- Linear fit: y = -0.134x + 1.3
- P-value: 0.8548
- N samples: 47

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.357 
- Linear fit: y = 0.000x + 0.0
- P-value: 0.1590
- N samples: 17

**Is Open Source:**
- Correlation: 0.206 
- Linear fit: y = 0.083x + 0.0
- P-value: 0.1640
- N samples: 47

**Is Reasoning Model:**
- Correlation: -0.093 
- Linear fit: y = -0.041x + 0.1
- P-value: 0.5333
- N samples: 47

**Benchmark Score:**
- Correlation: -0.065 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.6654
- N samples: 47

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
  r = -0.328, y = -0.045x + 1.8

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.323, y = -2.197x + 5.5

**category3_logical_errors vs Is Reasoning Model:**
  r = -0.319, y = -6.682x + 27.5

**category4_technical_errors vs Benchmark Score:**
  r = -0.317, y = -0.150x + 6.5


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
- Correlation: 0.640 ***
- Linear fit: y = 0.884x + 5.2

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.648 ***
- Linear fit: y = 1.323x + 19.5

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.452 **
- Linear fit: y = 0.305x + 0.9

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.705 ***
- Linear fit: y = 1.042x + 15.1

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.448 **
- Linear fit: y = 0.219x + 0.1

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.455 **
- Linear fit: y = 0.150x + -1.7

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.967 ***, y = 0.741x + 1.9

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.965 ***, y = 0.883x + -0.7

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.929 ***, y = 0.457x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.887 ***, y = 0.627x + 0.1

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.863 ***, y = 0.393x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.801 ***, y = 0.259x + -2.0

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.773 ***, y = 0.150x + 0.0

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.765 ***, y = 0.372x + -0.2

**1b: Context Omission vs 1c: Prompt Contradiction:**
  r = 0.741 ***, y = 0.293x + 0.0

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.732 ***, y = 0.453x + -4.6

**2b: Spurious Numeric vs 3a: Unsupported Leap:**
  r = 0.726 ***, y = 0.897x + 13.6

**1a: Instruction Override vs 3b: Self Contradiction:**
  r = 0.719 ***, y = 1.044x + 3.0

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.705 ***, y = 1.042x + 15.1

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.696 ***, y = 0.788x + 13.0

**Category 3: Logical Errors vs 1a: Instruction Override:**
  r = 0.684 ***, y = 0.153x + -2.6

**Category 1: Input Misalignment vs 3b: Self Contradiction:**
  r = 0.670 ***, y = 0.443x + 2.8

**Category 2: Factual Errors vs 1a: Instruction Override:**
  r = 0.659 ***, y = 0.217x + -0.7

**1a: Instruction Override vs 2b: Spurious Numeric:**
  r = 0.650 ***, y = 1.806x + 4.2

**Category 1: Input Misalignment vs Category 3: Logical Errors:**
  r = 0.648 ***, y = 1.323x + 19.5

**1a: Instruction Override vs 1b: Context Omission:**
  r = 0.643 ***, y = 0.695x + 0.6

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
