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
- Correlation: -0.230 
- Linear fit: y = -0.156x + 8.0
- P-value: 0.0553
- N samples: 70

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.160 
- Linear fit: y = 1.447x + 2.2
- P-value: 0.1870
- N samples: 70

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.006 
- Linear fit: y = -0.071x + 2.9
- P-value: 0.9584
- N samples: 70

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.185 
- Linear fit: y = -2.347x + 8.3
- P-value: 0.1256
- N samples: 70

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
- Correlation: 0.042 
- Linear fit: y = 0.661x + 6.7
- P-value: 0.7305
- N samples: 70

**Benchmark Score:**
- Correlation: 0.035 
- Linear fit: y = 0.033x + 6.2
- P-value: 0.7748
- N samples: 70

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.225 
- Linear fit: y = -3.962x + 21.9
- P-value: 0.0610
- N samples: 70

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Benchmark Score:**
- Correlation: -0.140 
- Linear fit: y = -0.183x + 26.2
- P-value: 0.2491
- N samples: 70

**Is Reasoning Model:**
- Correlation: -0.086 
- Linear fit: y = -1.875x + 21.6
- P-value: 0.4802
- N samples: 70

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.303 *
- Linear fit: y = -2.177x + 3.6
- P-value: 0.0108
- N samples: 70

**Benchmark Score:**
- Correlation: 0.149 
- Linear fit: y = 0.080x + -0.0
- P-value: 0.2180
- N samples: 70

**Is Reasoning Model:**
- Correlation: 0.124 
- Linear fit: y = 1.107x + 1.7
- P-value: 0.3064
- N samples: 70

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

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

**Is Open Source:**
- Correlation: -0.189 
- Linear fit: y = -6.999x + 36.1
- P-value: 0.1170
- N samples: 70

**Days Since 2024-01-01:**
- Correlation: -0.139 
- Linear fit: y = -0.021x + 51.2
- P-value: 0.3022
- N samples: 57

**Benchmark Score:**
- Correlation: -0.082 
- Linear fit: y = -0.227x + 40.5
- P-value: 0.4992
- N samples: 70

**Model Size (B):**
- Correlation: -0.066 
- Linear fit: y = -0.001x + 34.3
- P-value: 0.6271
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.001 
- Linear fit: y = 0.036x + 33.0
- P-value: 0.9949
- N samples: 70

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.230 
- Linear fit: y = -0.156x + 8.0
- P-value: 0.0553
- N samples: 70

**Model Size (B):**
- Correlation: -0.203 
- Linear fit: y = -0.001x + 3.8
- P-value: 0.1292
- N samples: 57

**Is Open Source:**
- Correlation: 0.160 
- Linear fit: y = 1.447x + 2.2
- P-value: 0.1870
- N samples: 70

**Days Since 2024-01-01:**
- Correlation: -0.129 
- Linear fit: y = -0.005x + 7.3
- P-value: 0.3379
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.006 
- Linear fit: y = -0.071x + 2.9
- P-value: 0.9584
- N samples: 70

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.185 
- Linear fit: y = -2.347x + 8.3
- P-value: 0.1256
- N samples: 70

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
- Correlation: 0.042 
- Linear fit: y = 0.661x + 6.7
- P-value: 0.7305
- N samples: 70

**Benchmark Score:**
- Correlation: 0.035 
- Linear fit: y = 0.033x + 6.2
- P-value: 0.7748
- N samples: 70

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.225 
- Linear fit: y = -3.962x + 21.9
- P-value: 0.0610
- N samples: 70

**Days Since 2024-01-01:**
- Correlation: -0.211 
- Linear fit: y = -0.015x + 33.6
- P-value: 0.1152
- N samples: 57

**Benchmark Score:**
- Correlation: -0.140 
- Linear fit: y = -0.183x + 26.2
- P-value: 0.2491
- N samples: 70

**Is Reasoning Model:**
- Correlation: -0.086 
- Linear fit: y = -1.875x + 21.6
- P-value: 0.4802
- N samples: 70

**Model Size (B):**
- Correlation: -0.011 
- Linear fit: y = -0.000x + 20.6
- P-value: 0.9350
- N samples: 57

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.303 *
- Linear fit: y = -2.177x + 3.6
- P-value: 0.0108
- N samples: 70

**Benchmark Score:**
- Correlation: 0.149 
- Linear fit: y = 0.080x + -0.0
- P-value: 0.2180
- N samples: 70

**Is Reasoning Model:**
- Correlation: 0.124 
- Linear fit: y = 1.107x + 1.7
- P-value: 0.3064
- N samples: 70

**Model Size (B):**
- Correlation: 0.109 
- Linear fit: y = 0.000x + 2.1
- P-value: 0.4215
- N samples: 57

**Days Since 2024-01-01:**
- Correlation: 0.063 
- Linear fit: y = 0.002x + 1.1
- P-value: 0.6402
- N samples: 57

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.191 
- Linear fit: y = -0.038x + 1.9
- P-value: 0.1133
- N samples: 70

**Model Size (B):**
- Correlation: -0.185 
- Linear fit: y = -0.000x + 0.9
- P-value: 0.1684
- N samples: 57

**Is Open Source:**
- Correlation: 0.141 
- Linear fit: y = 0.377x + 0.5
- P-value: 0.2458
- N samples: 70

**Days Since 2024-01-01:**
- Correlation: -0.128 
- Linear fit: y = -0.001x + 1.9
- P-value: 0.3415
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.059 
- Linear fit: y = -0.196x + 0.8
- P-value: 0.6278
- N samples: 70

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.169 
- Linear fit: y = 0.975x + 1.2
- P-value: 0.1619
- N samples: 70

**Benchmark Score:**
- Correlation: -0.159 
- Linear fit: y = -0.068x + 3.8
- P-value: 0.1885
- N samples: 70

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
- Correlation: 0.065 
- Linear fit: y = 0.464x + 1.2
- P-value: 0.5941
- N samples: 70

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.193 
- Linear fit: y = -0.000x + 1.0
- P-value: 0.1506
- N samples: 57

**Benchmark Score:**
- Correlation: -0.184 
- Linear fit: y = -0.049x + 2.3
- P-value: 0.1271
- N samples: 70

**Days Since 2024-01-01:**
- Correlation: -0.128 
- Linear fit: y = -0.002x + 2.3
- P-value: 0.3438
- N samples: 57

**Is Reasoning Model:**
- Correlation: -0.077 
- Linear fit: y = -0.339x + 0.9
- P-value: 0.5286
- N samples: 70

**Is Open Source:**
- Correlation: 0.026 
- Linear fit: y = 0.094x + 0.6
- P-value: 0.8280
- N samples: 70

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.103 
- Linear fit: y = -0.250x + 1.3
- P-value: 0.3970
- N samples: 70

**Model Size (B):**
- Correlation: -0.094 
- Linear fit: y = -0.000x + 1.3
- P-value: 0.4845
- N samples: 57

**Benchmark Score:**
- Correlation: 0.044 
- Linear fit: y = 0.008x + 0.9
- P-value: 0.7176
- N samples: 70

**Is Reasoning Model:**
- Correlation: 0.041 
- Linear fit: y = 0.125x + 1.1
- P-value: 0.7334
- N samples: 70

**Days Since 2024-01-01:**
- Correlation: 0.001 
- Linear fit: y = 0.000x + 1.2
- P-value: 0.9964
- N samples: 57

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.140 
- Linear fit: y = -1.637x + 6.3
- P-value: 0.2461
- N samples: 70

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
- Correlation: -0.020 
- Linear fit: y = -0.017x + 6.1
- P-value: 0.8727
- N samples: 70

**Is Reasoning Model:**
- Correlation: 0.005 
- Linear fit: y = 0.071x + 5.5
- P-value: 0.9677
- N samples: 70

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: 0.354 **
- Linear fit: y = 0.042x + -0.9
- P-value: 0.0026
- N samples: 70

**Is Open Source:**
- Correlation: -0.290 *
- Linear fit: y = -0.460x + 0.7
- P-value: 0.0149
- N samples: 70

**Model Size (B):**
- Correlation: 0.249 
- Linear fit: y = 0.000x + 0.3
- P-value: 0.0617
- N samples: 57

**Is Reasoning Model:**
- Correlation: 0.236 *
- Linear fit: y = 0.464x + 0.1
- P-value: 0.0496
- N samples: 70

**Days Since 2024-01-01:**
- Correlation: 0.131 
- Linear fit: y = 0.001x + -0.2
- P-value: 0.3322
- N samples: 57

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.219 
- Linear fit: y = -3.275x + 17.3
- P-value: 0.0688
- N samples: 70

**Days Since 2024-01-01:**
- Correlation: -0.176 
- Linear fit: y = -0.011x + 25.5
- P-value: 0.1905
- N samples: 57

**Benchmark Score:**
- Correlation: -0.139 
- Linear fit: y = -0.155x + 21.0
- P-value: 0.2520
- N samples: 70

**Is Reasoning Model:**
- Correlation: -0.048 
- Linear fit: y = -0.893x + 16.6
- P-value: 0.6930
- N samples: 70

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
- Correlation: -0.172 
- Linear fit: y = -1.000x + 5.1
- P-value: 0.1552
- N samples: 70

**Is Open Source:**
- Correlation: -0.153 
- Linear fit: y = -0.719x + 4.6
- P-value: 0.2052
- N samples: 70

**Benchmark Score:**
- Correlation: -0.076 
- Linear fit: y = -0.027x + 5.1
- P-value: 0.5305
- N samples: 70

**Model Size (B):**
- Correlation: -0.026 
- Linear fit: y = -0.000x + 4.3
- P-value: 0.8462
- N samples: 57

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.135 
- Linear fit: y = 0.032x + -0.0
- P-value: 0.2651
- N samples: 70

**Benchmark Score:**
- Correlation: -0.096 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.4293
- N samples: 70

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
- Correlation: 0.060 
- Linear fit: y = 0.018x + 0.0
- P-value: 0.6206
- N samples: 70

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.227 
- Linear fit: y = -0.979x + 1.2
- P-value: 0.0583
- N samples: 70

**Is Reasoning Model:**
- Correlation: 0.147 
- Linear fit: y = 0.786x + 0.1
- P-value: 0.2249
- N samples: 70

**Benchmark Score:**
- Correlation: 0.125 
- Linear fit: y = 0.040x + -0.5
- P-value: 0.3034
- N samples: 70

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
- Correlation: -0.245 *
- Linear fit: y = -1.134x + 2.2
- P-value: 0.0409
- N samples: 70

**Benchmark Score:**
- Correlation: 0.125 
- Linear fit: y = 0.043x + 0.3
- P-value: 0.3028
- N samples: 70

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
- Correlation: 0.065 
- Linear fit: y = 0.375x + 1.4
- P-value: 0.5915
- N samples: 70

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.082 
- Linear fit: y = -0.064x + 0.1
- P-value: 0.4973
- N samples: 70

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

**Benchmark Score:**
- Correlation: -0.056 
- Linear fit: y = -0.003x + 0.2
- P-value: 0.6431
- N samples: 70

**Is Reasoning Model:**
- Correlation: -0.056 
- Linear fit: y = -0.054x + 0.1
- P-value: 0.6460
- N samples: 70

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**2c_false_citation vs Benchmark Score:**
  r = 0.354, y = 0.042x + -0.9

**category4_technical_errors vs Is Open Source:**
  r = -0.303, y = -2.177x + 3.6


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
- Correlation: 0.402 ***
- Linear fit: y = 0.564x + 5.6

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.430 ***
- Linear fit: y = 0.836x + 17.7

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.370 **
- Linear fit: y = 0.293x + 1.8

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.474 ***
- Linear fit: y = 0.657x + 15.4

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.613 ***
- Linear fit: y = 0.347x + 0.1

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.528 ***
- Linear fit: y = 0.216x + -1.7

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.976 ***, y = 0.895x + -0.9

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.972 ***, y = 0.826x + -0.8

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.831 ***, y = 0.529x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.801 ***, y = 0.516x + 0.4

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.736 ***, y = 0.441x + -0.4

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.713 ***, y = 0.211x + 0.0

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.660 ***, y = 0.260x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.642 ***, y = 0.171x + 0.8

**Category 2: Factual Errors vs 4b: Model Semantics Breach:**
  r = 0.631 ***, y = 0.230x + 0.1

**Category 2: Factual Errors vs Category 4: Technical Errors:**
  r = 0.613 ***, y = 0.347x + 0.1

**Category 2: Factual Errors vs 4c: Visual Descr Mismatch:**
  r = 0.604 ***, y = 0.037x + -0.2

**2b: Spurious Numeric vs 4b: Model Semantics Breach:**
  r = 0.584 ***, y = 0.232x + 0.4

**Category 3: Logical Errors vs 4b: Model Semantics Breach:**
  r = 0.583 ***, y = 0.153x + -1.4

**Category 4: Technical Errors vs 2b: Spurious Numeric:**
  r = 0.580 ***, y = 0.940x + 3.1

**3a: Unsupported Leap vs 4b: Model Semantics Breach:**
  r = 0.569 ***, y = 0.176x + -1.1

**2b: Spurious Numeric vs 4c: Visual Descr Mismatch:**
  r = 0.560 ***, y = 0.037x + -0.1

**Category 3: Logical Errors vs Category 4: Technical Errors:**
  r = 0.528 ***, y = 0.216x + -1.7

**Category 4: Technical Errors vs 3a: Unsupported Leap:**
  r = 0.495 ***, y = 1.030x + 13.2

**2a: Concept Fabrication vs 4c: Visual Descr Mismatch:**
  r = 0.488 ***, y = 0.155x + -0.1

**1b: Context Omission vs 3c: Circular Reasoning:**
  r = 0.479 ***, y = 0.020x + -0.0

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
