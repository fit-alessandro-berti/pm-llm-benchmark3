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
- Correlation: -0.274 *
- Linear fit: y = -0.179x + 8.1
- P-value: 0.0249
- N samples: 67

**Model Size (B):**
- Correlation: -0.216 
- Linear fit: y = -0.001x + 3.2
- P-value: 0.1061
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.204 
- Linear fit: y = -2.098x + 3.9
- P-value: 0.0985
- N samples: 67

**Is Open Source:**
- Correlation: 0.055 
- Linear fit: y = 0.461x + 2.1
- P-value: 0.6597
- N samples: 67

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.194 
- Linear fit: y = -2.446x + 8.8
- P-value: 0.1162
- N samples: 67

**Model Size (B):**
- Correlation: -0.132 
- Linear fit: y = -0.001x + 8.2
- P-value: 0.3287
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.104 
- Linear fit: y = 1.609x + 6.4
- P-value: 0.4027
- N samples: 67

**Days Since 2024-01-01:**
- Correlation: -0.059 
- Linear fit: y = -0.003x + 10.2
- P-value: 0.6608
- N samples: 57

**Benchmark Score:**
- Correlation: 0.020 
- Linear fit: y = 0.020x + 7.1
- P-value: 0.8707
- N samples: 67

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.347 **
- Linear fit: y = -6.987x + 27.1
- P-value: 0.0040
- N samples: 67

**Days Since 2024-01-01:**
- Correlation: -0.314 *
- Linear fit: y = -0.024x + 44.4
- P-value: 0.0172
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.216 
- Linear fit: y = -5.336x + 28.1
- P-value: 0.0791
- N samples: 67

**Benchmark Score:**
- Correlation: -0.100 
- Linear fit: y = -0.157x + 29.0
- P-value: 0.4204
- N samples: 67

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
- Correlation: -0.312 *
- Linear fit: y = -0.145x + 6.4
- P-value: 0.0103
- N samples: 67

**Model Size (B):**
- Correlation: -0.211 
- Linear fit: y = -0.000x + 2.1
- P-value: 0.1156
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.123 
- Linear fit: y = -0.904x + 2.4
- P-value: 0.3201
- N samples: 67

**Is Open Source:**
- Correlation: 0.021 
- Linear fit: y = 0.126x + 1.6
- P-value: 0.8652
- N samples: 67

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
- Correlation: -0.233 
- Linear fit: y = -8.966x + 39.6
- P-value: 0.0583
- N samples: 67

**Benchmark Score:**
- Correlation: -0.150 
- Linear fit: y = -0.449x + 50.1
- P-value: 0.2272
- N samples: 67

**Is Reasoning Model:**
- Correlation: -0.140 
- Linear fit: y = -6.639x + 40.7
- P-value: 0.2571
- N samples: 67

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
- Correlation: -0.274 *
- Linear fit: y = -0.179x + 8.1
- P-value: 0.0249
- N samples: 67

**Model Size (B):**
- Correlation: -0.216 
- Linear fit: y = -0.001x + 3.2
- P-value: 0.1061
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.204 
- Linear fit: y = -2.098x + 3.9
- P-value: 0.0985
- N samples: 67

**Is Open Source:**
- Correlation: 0.055 
- Linear fit: y = 0.461x + 2.1
- P-value: 0.6597
- N samples: 67

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.194 
- Linear fit: y = -2.446x + 8.8
- P-value: 0.1162
- N samples: 67

**Model Size (B):**
- Correlation: -0.132 
- Linear fit: y = -0.001x + 8.2
- P-value: 0.3287
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.104 
- Linear fit: y = 1.609x + 6.4
- P-value: 0.4027
- N samples: 67

**Days Since 2024-01-01:**
- Correlation: -0.059 
- Linear fit: y = -0.003x + 10.2
- P-value: 0.6608
- N samples: 57

**Benchmark Score:**
- Correlation: 0.020 
- Linear fit: y = 0.020x + 7.1
- P-value: 0.8707
- N samples: 67

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.347 **
- Linear fit: y = -6.987x + 27.1
- P-value: 0.0040
- N samples: 67

**Days Since 2024-01-01:**
- Correlation: -0.314 *
- Linear fit: y = -0.024x + 44.4
- P-value: 0.0172
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.216 
- Linear fit: y = -5.336x + 28.1
- P-value: 0.0791
- N samples: 67

**Benchmark Score:**
- Correlation: -0.100 
- Linear fit: y = -0.157x + 29.0
- P-value: 0.4204
- N samples: 67

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
- Correlation: -0.312 *
- Linear fit: y = -0.145x + 6.4
- P-value: 0.0103
- N samples: 67

**Model Size (B):**
- Correlation: -0.211 
- Linear fit: y = -0.000x + 2.1
- P-value: 0.1156
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.123 
- Linear fit: y = -0.904x + 2.4
- P-value: 0.3201
- N samples: 67

**Is Open Source:**
- Correlation: 0.021 
- Linear fit: y = 0.126x + 1.6
- P-value: 0.8652
- N samples: 67

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.249 *
- Linear fit: y = -1.167x + 1.7
- P-value: 0.0421
- N samples: 67

**Days Since 2024-01-01:**
- Correlation: -0.246 
- Linear fit: y = -0.004x + 4.2
- P-value: 0.0650
- N samples: 57

**Benchmark Score:**
- Correlation: -0.230 
- Linear fit: y = -0.068x + 3.0
- P-value: 0.0611
- N samples: 67

**Model Size (B):**
- Correlation: -0.210 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.1162
- N samples: 57

**Is Open Source:**
- Correlation: 0.070 
- Linear fit: y = 0.269x + 0.7
- P-value: 0.5715
- N samples: 67

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.230 
- Linear fit: y = -0.004x + 4.7
- P-value: 0.0854
- N samples: 57

**Benchmark Score:**
- Correlation: -0.228 
- Linear fit: y = -0.075x + 3.6
- P-value: 0.0633
- N samples: 67

**Model Size (B):**
- Correlation: -0.215 
- Linear fit: y = -0.000x + 1.6
- P-value: 0.1075
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.110 
- Linear fit: y = -0.571x + 1.6
- P-value: 0.3741
- N samples: 67

**Is Open Source:**
- Correlation: 0.018 
- Linear fit: y = 0.078x + 1.1
- P-value: 0.8821
- N samples: 67

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.321 *
- Linear fit: y = -0.002x + 2.3
- P-value: 0.0149
- N samples: 57

**Benchmark Score:**
- Correlation: -0.279 *
- Linear fit: y = -0.036x + 1.5
- P-value: 0.0222
- N samples: 67

**Is Reasoning Model:**
- Correlation: -0.178 
- Linear fit: y = -0.360x + 0.6
- P-value: 0.1502
- N samples: 67

**Is Open Source:**
- Correlation: 0.069 
- Linear fit: y = 0.114x + 0.3
- P-value: 0.5794
- N samples: 67

**Model Size (B):**
- Correlation: -0.060 
- Linear fit: y = -0.000x + 0.4
- P-value: 0.6583
- N samples: 57

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.252 
- Linear fit: y = -0.000x + 1.7
- P-value: 0.0589
- N samples: 57

**Is Open Source:**
- Correlation: 0.199 
- Linear fit: y = 0.631x + 1.1
- P-value: 0.1072
- N samples: 67

**Benchmark Score:**
- Correlation: -0.163 
- Linear fit: y = -0.040x + 2.7
- P-value: 0.1883
- N samples: 67

**Is Reasoning Model:**
- Correlation: 0.131 
- Linear fit: y = 0.509x + 1.0
- P-value: 0.2916
- N samples: 67

**Days Since 2024-01-01:**
- Correlation: -0.022 
- Linear fit: y = -0.000x + 1.6
- P-value: 0.8698
- N samples: 57

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.250 *
- Linear fit: y = -2.978x + 7.3
- P-value: 0.0417
- N samples: 67

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
- Correlation: 0.064 
- Linear fit: y = 0.937x + 5.2
- P-value: 0.6069
- N samples: 67

**Benchmark Score:**
- Correlation: 0.037 
- Linear fit: y = 0.035x + 4.8
- P-value: 0.7636
- N samples: 67

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: 0.266 *
- Linear fit: y = 0.025x + -0.5
- P-value: 0.0299
- N samples: 67

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
- Correlation: 0.108 
- Linear fit: y = 0.163x + 0.2
- P-value: 0.3830
- N samples: 67

**Is Open Source:**
- Correlation: -0.080 
- Linear fit: y = -0.099x + 0.4
- P-value: 0.5184
- N samples: 67

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.399 ***
- Linear fit: y = -6.289x + 22.6
- P-value: 0.0008
- N samples: 67

**Days Since 2024-01-01:**
- Correlation: -0.323 *
- Linear fit: y = -0.020x + 36.1
- P-value: 0.0143
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.150 
- Linear fit: y = -2.906x + 22.0
- P-value: 0.2250
- N samples: 67

**Model Size (B):**
- Correlation: 0.099 
- Linear fit: y = 0.001x + 18.7
- P-value: 0.4641
- N samples: 57

**Benchmark Score:**
- Correlation: -0.055 
- Linear fit: y = -0.067x + 21.9
- P-value: 0.6605
- N samples: 67

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.307 *
- Linear fit: y = -2.306x + 5.9
- P-value: 0.0116
- N samples: 67

**Days Since 2024-01-01:**
- Correlation: -0.203 
- Linear fit: y = -0.005x + 8.4
- P-value: 0.1302
- N samples: 57

**Benchmark Score:**
- Correlation: -0.174 
- Linear fit: y = -0.083x + 6.8
- P-value: 0.1598
- N samples: 67

**Is Open Source:**
- Correlation: -0.120 
- Linear fit: y = -0.735x + 4.4
- P-value: 0.3341
- N samples: 67

**Model Size (B):**
- Correlation: -0.061 
- Linear fit: y = -0.000x + 4.3
- P-value: 0.6520
- N samples: 57

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.244 *
- Linear fit: y = -0.124x + 0.1
- P-value: 0.0468
- N samples: 67

**Benchmark Score:**
- Correlation: -0.213 
- Linear fit: y = -0.007x + 0.3
- P-value: 0.0831
- N samples: 67

**Model Size (B):**
- Correlation: -0.133 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.3229
- N samples: 57

**Is Open Source:**
- Correlation: 0.089 
- Linear fit: y = 0.037x + 0.0
- P-value: 0.4760
- N samples: 67

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
- Correlation: -0.191 
- Linear fit: y = -0.041x + 1.8
- P-value: 0.1209
- N samples: 67

**Model Size (B):**
- Correlation: -0.138 
- Linear fit: y = -0.000x + 0.6
- P-value: 0.3047
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.084 
- Linear fit: y = -0.284x + 0.6
- P-value: 0.5015
- N samples: 67

**Is Open Source:**
- Correlation: -0.042 
- Linear fit: y = -0.117x + 0.5
- P-value: 0.7340
- N samples: 67

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.309 *
- Linear fit: y = -0.101x + 4.5
- P-value: 0.0110
- N samples: 67

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
- Correlation: -0.110 
- Linear fit: y = -0.567x + 1.6
- P-value: 0.3770
- N samples: 67

**Is Open Source:**
- Correlation: 0.042 
- Linear fit: y = 0.179x + 1.1
- P-value: 0.7329
- N samples: 67

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.189 
- Linear fit: y = 0.065x + -0.0
- P-value: 0.1255
- N samples: 67

**Days Since 2024-01-01:**
- Correlation: -0.127 
- Linear fit: y = -0.000x + 0.2
- P-value: 0.3467
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.126 
- Linear fit: y = -0.053x + 0.1
- P-value: 0.3113
- N samples: 67

**Benchmark Score:**
- Correlation: -0.084 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.4999
- N samples: 67

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
  r = -0.399, y = -6.289x + 22.6

**category4_technical_errors vs Days Since 2024-01-01:**
  r = -0.355, y = -0.008x + 8.9

**category3_logical_errors vs Is Open Source:**
  r = -0.347, y = -6.987x + 27.1

**3a_unsupported_leap vs Days Since 2024-01-01:**
  r = -0.323, y = -0.020x + 36.1

**1c_prompt_contradiction vs Days Since 2024-01-01:**
  r = -0.321, y = -0.002x + 2.3

**category3_logical_errors vs Days Since 2024-01-01:**
  r = -0.314, y = -0.024x + 44.4

**category4_technical_errors vs Benchmark Score:**
  r = -0.312, y = -0.145x + 6.4

**4b_model_semantics_breach vs Benchmark Score:**
  r = -0.309, y = -0.101x + 4.5

**3b_self_contradiction vs Is Reasoning Model:**
  r = -0.307, y = -2.306x + 5.9


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
- Correlation: 0.596 ***
- Linear fit: y = 0.896x + 5.7

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.554 ***
- Linear fit: y = 1.327x + 20.8

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.507 ***
- Linear fit: y = 0.361x + 0.8

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.555 ***
- Linear fit: y = 0.886x + 17.0

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.391 **
- Linear fit: y = 0.185x + 0.2

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.421 ***
- Linear fit: y = 0.125x + -1.3

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.969 ***, y = 0.759x + 1.6

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.960 ***, y = 0.908x + -1.0

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.926 ***, y = 0.465x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.904 ***, y = 0.638x + 0.1

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.865 ***, y = 0.393x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.786 ***, y = 0.239x + -1.6

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.778 ***, y = 0.361x + -0.2

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.720 ***, y = 0.141x + 0.0

**1a: Instruction Override vs 3b: Self Contradiction:**
  r = 0.688 ***, y = 1.104x + 3.2

**1b: Context Omission vs 1c: Prompt Contradiction:**
  r = 0.656 ***, y = 0.256x + 0.1

**1a: Instruction Override vs 1b: Context Omission:**
  r = 0.650 ***, y = 0.719x + 0.6

**Category 1: Input Misalignment vs 3b: Self Contradiction:**
  r = 0.650 ***, y = 0.474x + 3.0

**3a: Unsupported Leap vs 3b: Self Contradiction:**
  r = 0.608 ***, y = 0.237x + -0.6

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = 0.596 ***, y = 0.896x + 5.7

**Category 1: Input Misalignment vs 2b: Spurious Numeric:**
  r = 0.595 ***, y = 0.845x + 4.0

**Category 2: Factual Errors vs 1a: Instruction Override:**
  r = 0.588 ***, y = 0.178x + -0.6

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = 0.584 ***, y = 0.195x + -0.4

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = 0.582 ***, y = 1.644x + 4.1

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.579 ***, y = 0.343x + -2.2

**Category 3: Logical Errors vs 1a: Instruction Override:**
  r = 0.578 ***, y = 0.110x + -1.8

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
