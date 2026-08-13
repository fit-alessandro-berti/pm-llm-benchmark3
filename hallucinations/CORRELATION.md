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
- Correlation: -0.274 
- Linear fit: y = -0.192x + 8.7
- P-value: 0.0723
- N samples: 44

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.136 
- Linear fit: y = -1.405x + 3.6
- P-value: 0.3801
- N samples: 44

**Is Open Source:**
- Correlation: 0.105 
- Linear fit: y = 1.012x + 2.1
- P-value: 0.4984
- N samples: 44

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
- Correlation: -0.113 
- Linear fit: y = -1.482x + 8.4
- P-value: 0.4661
- N samples: 44

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Benchmark Score:**
- Correlation: -0.057 
- Linear fit: y = -0.055x + 9.5
- P-value: 0.7111
- N samples: 44

**Is Reasoning Model:**
- Correlation: 0.024 
- Linear fit: y = 0.333x + 7.5
- P-value: 0.8789
- N samples: 44

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
- Correlation: -0.280 
- Linear fit: y = -5.567x + 27.5
- P-value: 0.0655
- N samples: 44

**Benchmark Score:**
- Correlation: -0.260 
- Linear fit: y = -0.350x + 34.8
- P-value: 0.0883
- N samples: 44

**Is Open Source:**
- Correlation: -0.176 
- Linear fit: y = -3.261x + 25.3
- P-value: 0.2532
- N samples: 44

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.324 *
- Linear fit: y = -0.154x + 6.6
- P-value: 0.0320
- N samples: 44

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.042 
- Linear fit: y = -0.295x + 1.9
- P-value: 0.7864
- N samples: 44

**Is Open Source:**
- Correlation: 0.038 
- Linear fit: y = 0.248x + 1.6
- P-value: 0.8068
- N samples: 44

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
- Correlation: -0.253 
- Linear fit: y = -0.746x + 59.5
- P-value: 0.0969
- N samples: 44

**Is Reasoning Model:**
- Correlation: -0.160 
- Linear fit: y = -6.967x + 40.5
- P-value: 0.2983
- N samples: 44

**Is Open Source:**
- Correlation: -0.087 
- Linear fit: y = -3.530x + 37.4
- P-value: 0.5737
- N samples: 44

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.274 
- Linear fit: y = -0.192x + 8.7
- P-value: 0.0723
- N samples: 44

**Model Size (B):**
- Correlation: -0.145 
- Linear fit: y = -0.001x + 3.4
- P-value: 0.5793
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.136 
- Linear fit: y = -1.405x + 3.6
- P-value: 0.3801
- N samples: 44

**Is Open Source:**
- Correlation: 0.105 
- Linear fit: y = 1.012x + 2.1
- P-value: 0.4984
- N samples: 44

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
- Correlation: -0.113 
- Linear fit: y = -1.482x + 8.4
- P-value: 0.4661
- N samples: 44

**Days Since 2024-01-01:**
- Correlation: -0.073 
- Linear fit: y = -0.003x + 9.4
- P-value: 0.7589
- N samples: 20

**Benchmark Score:**
- Correlation: -0.057 
- Linear fit: y = -0.055x + 9.5
- P-value: 0.7111
- N samples: 44

**Is Reasoning Model:**
- Correlation: 0.024 
- Linear fit: y = 0.333x + 7.5
- P-value: 0.8789
- N samples: 44

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
- Correlation: -0.280 
- Linear fit: y = -5.567x + 27.5
- P-value: 0.0655
- N samples: 44

**Benchmark Score:**
- Correlation: -0.260 
- Linear fit: y = -0.350x + 34.8
- P-value: 0.0883
- N samples: 44

**Is Open Source:**
- Correlation: -0.176 
- Linear fit: y = -3.261x + 25.3
- P-value: 0.2532
- N samples: 44

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.458 *
- Linear fit: y = -0.011x + 10.5
- P-value: 0.0424
- N samples: 20

**Benchmark Score:**
- Correlation: -0.324 *
- Linear fit: y = -0.154x + 6.6
- P-value: 0.0320
- N samples: 44

**Model Size (B):**
- Correlation: -0.069 
- Linear fit: y = -0.000x + 2.2
- P-value: 0.7910
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.042 
- Linear fit: y = -0.295x + 1.9
- P-value: 0.7864
- N samples: 44

**Is Open Source:**
- Correlation: 0.038 
- Linear fit: y = 0.248x + 1.6
- P-value: 0.8068
- N samples: 44

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.205 
- Linear fit: y = -0.066x + 3.0
- P-value: 0.1824
- N samples: 44

**Is Reasoning Model:**
- Correlation: -0.183 
- Linear fit: y = -0.867x + 1.5
- P-value: 0.2339
- N samples: 44

**Is Open Source:**
- Correlation: 0.101 
- Linear fit: y = 0.447x + 0.7
- P-value: 0.5126
- N samples: 44

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
- Correlation: -0.233 
- Linear fit: y = -0.080x + 3.9
- P-value: 0.1281
- N samples: 44

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

**Is Open Source:**
- Correlation: 0.064 
- Linear fit: y = 0.302x + 1.2
- P-value: 0.6814
- N samples: 44

**Is Reasoning Model:**
- Correlation: -0.052 
- Linear fit: y = -0.267x + 1.5
- P-value: 0.7357
- N samples: 44

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.339 *
- Linear fit: y = -0.046x + 1.9
- P-value: 0.0245
- N samples: 44

**Is Open Source:**
- Correlation: 0.141 
- Linear fit: y = 0.263x + 0.3
- P-value: 0.3629
- N samples: 44

**Is Reasoning Model:**
- Correlation: -0.135 
- Linear fit: y = -0.271x + 0.6
- P-value: 0.3813
- N samples: 44

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
- Correlation: 0.234 
- Linear fit: y = 0.770x + 1.1
- P-value: 0.1263
- N samples: 44

**Is Reasoning Model:**
- Correlation: 0.159 
- Linear fit: y = 0.562x + 1.1
- P-value: 0.3020
- N samples: 44

**Benchmark Score:**
- Correlation: -0.152 
- Linear fit: y = -0.036x + 2.6
- P-value: 0.3259
- N samples: 44

**Days Since 2024-01-01:**
- Correlation: 0.021 
- Linear fit: y = 0.000x + 1.1
- P-value: 0.9297
- N samples: 20

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.191 
- Linear fit: y = -2.321x + 7.1
- P-value: 0.2140
- N samples: 44

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
- Correlation: -0.032 
- Linear fit: y = -0.028x + 6.9
- P-value: 0.8372
- N samples: 44

**Is Reasoning Model:**
- Correlation: -0.022 
- Linear fit: y = -0.281x + 6.2
- P-value: 0.8895
- N samples: 44

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
- Correlation: 0.152 
- Linear fit: y = 0.010x + -0.1
- P-value: 0.3262
- N samples: 44

**Is Open Source:**
- Correlation: 0.079 
- Linear fit: y = 0.068x + 0.2
- P-value: 0.6111
- N samples: 44

**Is Reasoning Model:**
- Correlation: 0.056 
- Linear fit: y = 0.052x + 0.2
- P-value: 0.7164
- N samples: 44

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

**Benchmark Score:**
- Correlation: -0.253 
- Linear fit: y = -0.258x + 27.8
- P-value: 0.0974
- N samples: 44

**Is Reasoning Model:**
- Correlation: -0.230 
- Linear fit: y = -3.462x + 21.9
- P-value: 0.1328
- N samples: 44

**Is Open Source:**
- Correlation: -0.214 
- Linear fit: y = -3.000x + 21.0
- P-value: 0.1632
- N samples: 44

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.379 
- Linear fit: y = -0.001x + 4.4
- P-value: 0.1339
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.301 *
- Linear fit: y = -2.033x + 5.5
- P-value: 0.0468
- N samples: 44

**Benchmark Score:**
- Correlation: -0.191 
- Linear fit: y = -0.087x + 6.9
- P-value: 0.2150
- N samples: 44

**Days Since 2024-01-01:**
- Correlation: -0.187 
- Linear fit: y = -0.003x + 5.8
- P-value: 0.4300
- N samples: 20

**Is Open Source:**
- Correlation: -0.049 
- Linear fit: y = -0.308x + 4.3
- P-value: 0.7519
- N samples: 44

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.232 
- Linear fit: y = -0.005x + 0.2
- P-value: 0.1305
- N samples: 44

**Is Reasoning Model:**
- Correlation: -0.223 
- Linear fit: y = -0.071x + 0.1
- P-value: 0.1452
- N samples: 44

**Model Size (B):**
- Correlation: -0.170 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.5133
- N samples: 17

**Is Open Source:**
- Correlation: 0.160 
- Linear fit: y = 0.048x + -0.0
- P-value: 0.3008
- N samples: 44

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
- Correlation: -0.138 
- Linear fit: y = -0.032x + 1.5
- P-value: 0.3728
- N samples: 44

**Is Open Source:**
- Correlation: -0.115 
- Linear fit: y = -0.366x + 0.7
- P-value: 0.4563
- N samples: 44

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.8201
- N samples: 17

**Is Reasoning Model:**
- Correlation: -0.041 
- Linear fit: y = -0.138x + 0.6
- P-value: 0.7941
- N samples: 44

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.359 *
- Linear fit: y = -0.120x + 5.0
- P-value: 0.0168
- N samples: 44

**Days Since 2024-01-01:**
- Correlation: -0.352 
- Linear fit: y = -0.004x + 4.0
- P-value: 0.1282
- N samples: 20

**Model Size (B):**
- Correlation: -0.134 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.6083
- N samples: 17

**Is Open Source:**
- Correlation: 0.113 
- Linear fit: y = 0.520x + 1.0
- P-value: 0.4662
- N samples: 44

**Is Reasoning Model:**
- Correlation: -0.024 
- Linear fit: y = -0.119x + 1.3
- P-value: 0.8767
- N samples: 44

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Model Size (B):**
- Correlation: 0.357 
- Linear fit: y = 0.000x + 0.0
- P-value: 0.1590
- N samples: 17

**Is Open Source:**
- Correlation: 0.228 
- Linear fit: y = 0.095x + -0.0
- P-value: 0.1360
- N samples: 44

**Is Reasoning Model:**
- Correlation: -0.085 
- Linear fit: y = -0.038x + 0.1
- P-value: 0.5825
- N samples: 44

**Benchmark Score:**
- Correlation: -0.070 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.6538
- N samples: 44

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
  r = -0.359, y = -0.120x + 5.0

**1c_prompt_contradiction vs Benchmark Score:**
  r = -0.339, y = -0.046x + 1.9

**category4_technical_errors vs Benchmark Score:**
  r = -0.324, y = -0.154x + 6.6

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.301, y = -2.033x + 5.5


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
- Correlation: 0.639 ***
- Linear fit: y = 0.870x + 5.5

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.667 ***
- Linear fit: y = 1.280x + 20.4

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.450 **
- Linear fit: y = 0.305x + 0.9

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.693 ***
- Linear fit: y = 0.977x + 16.2

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.452 **
- Linear fit: y = 0.225x + -0.0

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.476 **
- Linear fit: y = 0.168x + -2.3

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.965 ***, y = 0.892x + -0.9

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.963 ***, y = 0.729x + 2.3

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.928 ***, y = 0.456x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.889 ***, y = 0.626x + 0.1

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.862 ***, y = 0.394x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.801 ***, y = 0.272x + -2.3

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.774 ***, y = 0.150x + -0.0

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.769 ***, y = 0.373x + -0.2

**1b: Context Omission vs 1c: Prompt Contradiction:**
  r = 0.744 ***, y = 0.293x + -0.0

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.735 ***, y = 0.482x + -5.4

**2b: Spurious Numeric vs 3a: Unsupported Leap:**
  r = 0.734 ***, y = 0.847x + 14.5

**1a: Instruction Override vs 3b: Self Contradiction:**
  r = 0.727 ***, y = 1.037x + 3.2

**Category 3: Logical Errors vs 1a: Instruction Override:**
  r = 0.711 ***, y = 0.169x + -3.1

**Category 2: Factual Errors vs Category 3: Logical Errors:**
  r = 0.693 ***, y = 0.977x + 16.2

**Category 2: Factual Errors vs 3a: Unsupported Leap:**
  r = 0.686 ***, y = 0.732x + 13.9

**Category 1: Input Misalignment vs 3b: Self Contradiction:**
  r = 0.676 ***, y = 0.440x + 3.0

**Category 1: Input Misalignment vs Category 3: Logical Errors:**
  r = 0.667 ***, y = 1.280x + 20.4

**Category 2: Factual Errors vs 1a: Instruction Override:**
  r = 0.661 ***, y = 0.222x + -0.8

**1a: Instruction Override vs 2b: Spurious Numeric:**
  r = 0.650 ***, y = 1.789x + 4.4

**1a: Instruction Override vs 1b: Context Omission:**
  r = 0.640 ***, y = 0.689x + 0.7

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
