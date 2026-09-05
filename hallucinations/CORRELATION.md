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

**Days Since 2024-01-01:**
- Correlation: -0.292 *
- Linear fit: y = -0.010x + 11.2
- P-value: 0.0277
- N samples: 57

**Benchmark Score:**
- Correlation: -0.263 *
- Linear fit: y = -0.175x + 8.0
- P-value: 0.0343
- N samples: 65

**Model Size (B):**
- Correlation: -0.216 
- Linear fit: y = -0.001x + 3.2
- P-value: 0.1061
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.197 
- Linear fit: y = -2.027x + 3.9
- P-value: 0.1164
- N samples: 65

**Is Open Source:**
- Correlation: 0.040 
- Linear fit: y = 0.340x + 2.2
- P-value: 0.7515
- N samples: 65

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.234 
- Linear fit: y = -2.971x + 9.0
- P-value: 0.0602
- N samples: 65

**Model Size (B):**
- Correlation: -0.132 
- Linear fit: y = -0.001x + 8.2
- P-value: 0.3287
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.093 
- Linear fit: y = 1.434x + 6.4
- P-value: 0.4605
- N samples: 65

**Days Since 2024-01-01:**
- Correlation: -0.059 
- Linear fit: y = -0.003x + 10.2
- P-value: 0.6608
- N samples: 57

**Benchmark Score:**
- Correlation: -0.001 
- Linear fit: y = -0.001x + 7.6
- P-value: 0.9945
- N samples: 65

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.350 **
- Linear fit: y = -7.068x + 27.3
- P-value: 0.0042
- N samples: 65

**Days Since 2024-01-01:**
- Correlation: -0.314 *
- Linear fit: y = -0.024x + 44.4
- P-value: 0.0172
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.216 
- Linear fit: y = -5.287x + 28.1
- P-value: 0.0844
- N samples: 65

**Benchmark Score:**
- Correlation: -0.107 
- Linear fit: y = -0.168x + 29.4
- P-value: 0.3982
- N samples: 65

**Model Size (B):**
- Correlation: 0.055 
- Linear fit: y = 0.000x + 23.1
- P-value: 0.6822
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.355 **
- Linear fit: y = -0.008x + 8.9
- P-value: 0.0068
- N samples: 57

**Benchmark Score:**
- Correlation: -0.301 *
- Linear fit: y = -0.142x + 6.3
- P-value: 0.0147
- N samples: 65

**Model Size (B):**
- Correlation: -0.211 
- Linear fit: y = -0.000x + 2.1
- P-value: 0.1156
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.116 
- Linear fit: y = -0.847x + 2.4
- P-value: 0.3590
- N samples: 65

**Is Open Source:**
- Correlation: 0.006 
- Linear fit: y = 0.033x + 1.7
- P-value: 0.9653
- N samples: 65

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.289 *
- Linear fit: y = -0.046x + 74.4
- P-value: 0.0294
- N samples: 57

**Is Open Source:**
- Correlation: -0.251 *
- Linear fit: y = -9.789x + 40.2
- P-value: 0.0437
- N samples: 65

**Benchmark Score:**
- Correlation: -0.155 
- Linear fit: y = -0.473x + 50.9
- P-value: 0.2177
- N samples: 65

**Is Reasoning Model:**
- Correlation: -0.140 
- Linear fit: y = -6.636x + 40.7
- P-value: 0.2658
- N samples: 65

**Model Size (B):**
- Correlation: -0.090 
- Linear fit: y = -0.001x + 36.6
- P-value: 0.5033
- N samples: 57

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.292 *
- Linear fit: y = -0.010x + 11.2
- P-value: 0.0277
- N samples: 57

**Benchmark Score:**
- Correlation: -0.263 *
- Linear fit: y = -0.175x + 8.0
- P-value: 0.0343
- N samples: 65

**Model Size (B):**
- Correlation: -0.216 
- Linear fit: y = -0.001x + 3.2
- P-value: 0.1061
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.197 
- Linear fit: y = -2.027x + 3.9
- P-value: 0.1164
- N samples: 65

**Is Open Source:**
- Correlation: 0.040 
- Linear fit: y = 0.340x + 2.2
- P-value: 0.7515
- N samples: 65

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.234 
- Linear fit: y = -2.971x + 9.0
- P-value: 0.0602
- N samples: 65

**Model Size (B):**
- Correlation: -0.132 
- Linear fit: y = -0.001x + 8.2
- P-value: 0.3287
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.093 
- Linear fit: y = 1.434x + 6.4
- P-value: 0.4605
- N samples: 65

**Days Since 2024-01-01:**
- Correlation: -0.059 
- Linear fit: y = -0.003x + 10.2
- P-value: 0.6608
- N samples: 57

**Benchmark Score:**
- Correlation: -0.001 
- Linear fit: y = -0.001x + 7.6
- P-value: 0.9945
- N samples: 65

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.350 **
- Linear fit: y = -7.068x + 27.3
- P-value: 0.0042
- N samples: 65

**Days Since 2024-01-01:**
- Correlation: -0.314 *
- Linear fit: y = -0.024x + 44.4
- P-value: 0.0172
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.216 
- Linear fit: y = -5.287x + 28.1
- P-value: 0.0844
- N samples: 65

**Benchmark Score:**
- Correlation: -0.107 
- Linear fit: y = -0.168x + 29.4
- P-value: 0.3982
- N samples: 65

**Model Size (B):**
- Correlation: 0.055 
- Linear fit: y = 0.000x + 23.1
- P-value: 0.6822
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.355 **
- Linear fit: y = -0.008x + 8.9
- P-value: 0.0068
- N samples: 57

**Benchmark Score:**
- Correlation: -0.301 *
- Linear fit: y = -0.142x + 6.3
- P-value: 0.0147
- N samples: 65

**Model Size (B):**
- Correlation: -0.211 
- Linear fit: y = -0.000x + 2.1
- P-value: 0.1156
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.116 
- Linear fit: y = -0.847x + 2.4
- P-value: 0.3590
- N samples: 65

**Is Open Source:**
- Correlation: 0.006 
- Linear fit: y = 0.033x + 1.7
- P-value: 0.9653
- N samples: 65

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.246 
- Linear fit: y = -0.004x + 4.2
- P-value: 0.0650
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.244 *
- Linear fit: y = -1.146x + 1.7
- P-value: 0.0500
- N samples: 65

**Benchmark Score:**
- Correlation: -0.222 
- Linear fit: y = -0.067x + 3.0
- P-value: 0.0759
- N samples: 65

**Model Size (B):**
- Correlation: -0.210 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.1162
- N samples: 57

**Is Open Source:**
- Correlation: 0.059 
- Linear fit: y = 0.230x + 0.7
- P-value: 0.6380
- N samples: 65

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.230 
- Linear fit: y = -0.004x + 4.7
- P-value: 0.0854
- N samples: 57

**Benchmark Score:**
- Correlation: -0.216 
- Linear fit: y = -0.072x + 3.5
- P-value: 0.0833
- N samples: 65

**Model Size (B):**
- Correlation: -0.215 
- Linear fit: y = -0.000x + 1.6
- P-value: 0.1075
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.103 
- Linear fit: y = -0.532x + 1.6
- P-value: 0.4152
- N samples: 65

**Is Open Source:**
- Correlation: 0.003 
- Linear fit: y = 0.014x + 1.1
- P-value: 0.9789
- N samples: 65

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.321 *
- Linear fit: y = -0.002x + 2.3
- P-value: 0.0149
- N samples: 57

**Benchmark Score:**
- Correlation: -0.271 *
- Linear fit: y = -0.035x + 1.5
- P-value: 0.0289
- N samples: 65

**Is Reasoning Model:**
- Correlation: -0.172 
- Linear fit: y = -0.349x + 0.6
- P-value: 0.1706
- N samples: 65

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 0.4
- P-value: 0.6583
- N samples: 57

**Is Open Source:**
- Correlation: 0.057 
- Linear fit: y = 0.096x + 0.3
- P-value: 0.6495
- N samples: 65

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.252 
- Linear fit: y = -0.000x + 1.7
- P-value: 0.0589
- N samples: 57

**Is Open Source:**
- Correlation: 0.226 
- Linear fit: y = 0.713x + 1.0
- P-value: 0.0702
- N samples: 65

**Benchmark Score:**
- Correlation: -0.205 
- Linear fit: y = -0.050x + 3.0
- P-value: 0.1020
- N samples: 65

**Is Reasoning Model:**
- Correlation: 0.123 
- Linear fit: y = 0.471x + 1.0
- P-value: 0.3295
- N samples: 65

**Days Since 2024-01-01:**
- Correlation: -0.022 
- Linear fit: y = -0.000x + 1.6
- P-value: 0.8698
- N samples: 57

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.302 *
- Linear fit: y = -3.618x + 7.6
- P-value: 0.0146
- N samples: 65

**Model Size (B):**
- Correlation: -0.090 
- Linear fit: y = -0.000x + 6.4
- P-value: 0.5062
- N samples: 57

**Days Since 2024-01-01:**
- Correlation: -0.069 
- Linear fit: y = -0.003x + 8.8
- P-value: 0.6086
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.059 
- Linear fit: y = 0.864x + 5.2
- P-value: 0.6389
- N samples: 65

**Benchmark Score:**
- Correlation: 0.036 
- Linear fit: y = 0.034x + 4.8
- P-value: 0.7758
- N samples: 65

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: 0.195 
- Linear fit: y = 0.016x + -0.2
- P-value: 0.1197
- N samples: 65

**Model Size (B):**
- Correlation: 0.188 
- Linear fit: y = 0.000x + 0.2
- P-value: 0.1618
- N samples: 57

**Days Since 2024-01-01:**
- Correlation: 0.149 
- Linear fit: y = 0.001x + -0.2
- P-value: 0.2682
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.079 
- Linear fit: y = 0.099x + 0.2
- P-value: 0.5321
- N samples: 65

**Is Open Source:**
- Correlation: -0.063 
- Linear fit: y = -0.065x + 0.3
- P-value: 0.6175
- N samples: 65

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.392 **
- Linear fit: y = -6.193x + 22.7
- P-value: 0.0012
- N samples: 65

**Days Since 2024-01-01:**
- Correlation: -0.323 *
- Linear fit: y = -0.020x + 36.1
- P-value: 0.0143
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.151 
- Linear fit: y = -2.902x + 22.0
- P-value: 0.2292
- N samples: 65

**Model Size (B):**
- Correlation: 0.099 
- Linear fit: y = 0.001x + 18.7
- P-value: 0.4641
- N samples: 57

**Benchmark Score:**
- Correlation: -0.065 
- Linear fit: y = -0.080x + 22.3
- P-value: 0.6068
- N samples: 65

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.302 *
- Linear fit: y = -2.262x + 5.9
- P-value: 0.0145
- N samples: 65

**Days Since 2024-01-01:**
- Correlation: -0.203 
- Linear fit: y = -0.005x + 8.4
- P-value: 0.1302
- N samples: 57

**Benchmark Score:**
- Correlation: -0.168 
- Linear fit: y = -0.081x + 6.8
- P-value: 0.1816
- N samples: 65

**Is Open Source:**
- Correlation: -0.148 
- Linear fit: y = -0.911x + 4.6
- P-value: 0.2403
- N samples: 65

**Model Size (B):**
- Correlation: -0.061 
- Linear fit: y = -0.000x + 4.3
- P-value: 0.6520
- N samples: 57

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.241 
- Linear fit: y = -0.123x + 0.1
- P-value: 0.0526
- N samples: 65

**Benchmark Score:**
- Correlation: -0.211 
- Linear fit: y = -0.007x + 0.3
- P-value: 0.0922
- N samples: 65

**Model Size (B):**
- Correlation: -0.133 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.3229
- N samples: 57

**Is Open Source:**
- Correlation: 0.084 
- Linear fit: y = 0.035x + 0.0
- P-value: 0.5081
- N samples: 65

**Days Since 2024-01-01:**
- Correlation: 0.070 
- Linear fit: y = 0.000x + -0.1
- P-value: 0.6024
- N samples: 57

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.420 **
- Linear fit: y = -0.005x + 4.5
- P-value: 0.0012
- N samples: 57

**Benchmark Score:**
- Correlation: -0.186 
- Linear fit: y = -0.041x + 1.8
- P-value: 0.1389
- N samples: 65

**Model Size (B):**
- Correlation: -0.138 
- Linear fit: y = -0.000x + 0.6
- P-value: 0.3047
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.079 
- Linear fit: y = -0.270x + 0.6
- P-value: 0.5306
- N samples: 65

**Is Open Source:**
- Correlation: -0.052 
- Linear fit: y = -0.145x + 0.5
- P-value: 0.6827
- N samples: 65

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.298 *
- Linear fit: y = -0.099x + 4.5
- P-value: 0.0159
- N samples: 65

**Days Since 2024-01-01:**
- Correlation: -0.207 
- Linear fit: y = -0.004x + 4.2
- P-value: 0.1232
- N samples: 57

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.000x + 1.5
- P-value: 0.1298
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.102 
- Linear fit: y = -0.525x + 1.6
- P-value: 0.4206
- N samples: 65

**Is Open Source:**
- Correlation: 0.027 
- Linear fit: y = 0.114x + 1.2
- P-value: 0.8324
- N samples: 65

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.187 
- Linear fit: y = 0.065x + 0.0
- P-value: 0.1367
- N samples: 65

**Days Since 2024-01-01:**
- Correlation: -0.127 
- Linear fit: y = -0.000x + 0.2
- P-value: 0.3467
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.123 
- Linear fit: y = -0.052x + 0.1
- P-value: 0.3276
- N samples: 65

**Benchmark Score:**
- Correlation: -0.080 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.5271
- N samples: 65

**Model Size (B):**
- Correlation: 0.006 
- Linear fit: y = 0.000x + 0.0
- P-value: 0.9643
- N samples: 57

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**4a_syntax_error vs Days Since 2024-01-01:**
  r = -0.420, y = -0.005x + 4.5

**3a_unsupported_leap vs Is Open Source:**
  r = -0.392, y = -6.193x + 22.7

**category4_technical_errors vs Days Since 2024-01-01:**
  r = -0.355, y = -0.008x + 8.9

**category3_logical_errors vs Is Open Source:**
  r = -0.350, y = -7.068x + 27.3

**3a_unsupported_leap vs Days Since 2024-01-01:**
  r = -0.323, y = -0.020x + 36.1

**1c_prompt_contradiction vs Days Since 2024-01-01:**
  r = -0.321, y = -0.002x + 2.3

**category3_logical_errors vs Days Since 2024-01-01:**
  r = -0.314, y = -0.024x + 44.4

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.302, y = -2.262x + 5.9

**2b_spurious_numeric vs Is Open Source:**
  r = -0.302, y = -3.618x + 7.6

**category4_technical_errors vs Benchmark Score:**
  r = -0.301, y = -0.142x + 6.3


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
- Correlation: 0.618 ***
- Linear fit: y = 0.923x + 5.4

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.559 ***
- Linear fit: y = 1.329x + 20.8

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.502 ***
- Linear fit: y = 0.357x + 0.9

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.579 ***
- Linear fit: y = 0.922x + 17.0

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.410 ***
- Linear fit: y = 0.195x + 0.2

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.423 ***
- Linear fit: y = 0.127x + -1.3

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.968 ***, y = 0.758x + 1.6

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.965 ***, y = 0.914x + -1.0

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.926 ***, y = 0.465x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.903 ***, y = 0.637x + 0.2

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.864 ***, y = 0.394x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.785 ***, y = 0.240x + -1.6

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.778 ***, y = 0.362x + -0.2

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.719 ***, y = 0.141x + 0.0

**1a: Instruction Override vs 3b: Self Contradiction:**
  r = 0.689 ***, y = 1.100x + 3.3

**1b: Context Omission vs 1c: Prompt Contradiction:**
  r = 0.653 ***, y = 0.256x + 0.1

**Category 1: Input Misalignment vs 3b: Self Contradiction:**
  r = 0.649 ***, y = 0.472x + 3.1

**1a: Instruction Override vs 1b: Context Omission:**
  r = 0.648 ***, y = 0.715x + 0.6

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = 0.618 ***, y = 0.923x + 5.4

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.611 ***, y = 0.363x + -2.8

**Category 1: Input Misalignment vs 2b: Spurious Numeric:**
  r = 0.609 ***, y = 0.861x + 3.9

**3a: Unsupported Leap vs 3b: Self Contradiction:**
  r = 0.606 ***, y = 0.237x + -0.5

**Category 2: Factual Errors vs 1a: Instruction Override:**
  r = 0.606 ***, y = 0.185x + -0.6

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = 0.605 ***, y = 0.203x + -0.4

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = 0.595 ***, y = 1.675x + 4.0

**2b: Spurious Numeric vs 3a: Unsupported Leap:**
  r = 0.585 ***, y = 0.771x + 15.2

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
