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
- Correlation: -0.277 *
- Linear fit: y = -0.010x + 10.6
- P-value: 0.0355
- N samples: 58

**Benchmark Score:**
- Correlation: -0.255 *
- Linear fit: y = -0.172x + 7.9
- P-value: 0.0420
- N samples: 64

**Model Size (B):**
- Correlation: -0.212 
- Linear fit: y = -0.001x + 3.1
- P-value: 0.1102
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.193 
- Linear fit: y = -1.989x + 3.9
- P-value: 0.1265
- N samples: 64

**Is Open Source:**
- Correlation: 0.050 
- Linear fit: y = 0.424x + 2.2
- P-value: 0.6970
- N samples: 64

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.223 
- Linear fit: y = -2.837x + 9.0
- P-value: 0.0761
- N samples: 64

**Model Size (B):**
- Correlation: -0.124 
- Linear fit: y = -0.001x + 8.1
- P-value: 0.3539
- N samples: 58

**Is Reasoning Model:**
- Correlation: 0.101 
- Linear fit: y = 1.551x + 6.4
- P-value: 0.4264
- N samples: 64

**Days Since 2024-01-01:**
- Correlation: -0.038 
- Linear fit: y = -0.002x + 9.1
- P-value: 0.7757
- N samples: 58

**Benchmark Score:**
- Correlation: 0.021 
- Linear fit: y = 0.021x + 6.9
- P-value: 0.8670
- N samples: 64

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.343 **
- Linear fit: y = -6.961x + 27.3
- P-value: 0.0055
- N samples: 64

**Days Since 2024-01-01:**
- Correlation: -0.330 *
- Linear fit: y = -0.026x + 45.6
- P-value: 0.0113
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.211 
- Linear fit: y = -5.171x + 28.1
- P-value: 0.0937
- N samples: 64

**Benchmark Score:**
- Correlation: -0.092 
- Linear fit: y = -0.147x + 28.8
- P-value: 0.4710
- N samples: 64

**Model Size (B):**
- Correlation: 0.047 
- Linear fit: y = 0.000x + 23.3
- P-value: 0.7251
- N samples: 58

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.339 **
- Linear fit: y = -0.008x + 8.4
- P-value: 0.0093
- N samples: 58

**Benchmark Score:**
- Correlation: -0.294 *
- Linear fit: y = -0.141x + 6.3
- P-value: 0.0184
- N samples: 64

**Model Size (B):**
- Correlation: -0.206 
- Linear fit: y = -0.000x + 2.1
- P-value: 0.1200
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.112 
- Linear fit: y = -0.817x + 2.4
- P-value: 0.3802
- N samples: 64

**Is Open Source:**
- Correlation: 0.015 
- Linear fit: y = 0.090x + 1.7
- P-value: 0.9072
- N samples: 64

================================================================================
## INDIVIDUAL HALLUCINATION TYPE CORRELATIONS
================================================================================

------------------------------------------------------------
### Correlations with: total_hallucinations
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.286 *
- Linear fit: y = -0.045x + 73.5
- P-value: 0.0294
- N samples: 58

**Is Open Source:**
- Correlation: -0.241 
- Linear fit: y = -9.410x + 40.2
- P-value: 0.0555
- N samples: 64

**Benchmark Score:**
- Correlation: -0.138 
- Linear fit: y = -0.426x + 49.5
- P-value: 0.2786
- N samples: 64

**Is Reasoning Model:**
- Correlation: -0.134 
- Linear fit: y = -6.334x + 40.7
- P-value: 0.2905
- N samples: 64

**Model Size (B):**
- Correlation: -0.091 
- Linear fit: y = -0.001x + 36.6
- P-value: 0.4985
- N samples: 58

------------------------------------------------------------
### Correlations with: category1_input_misalignment
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.277 *
- Linear fit: y = -0.010x + 10.6
- P-value: 0.0355
- N samples: 58

**Benchmark Score:**
- Correlation: -0.255 *
- Linear fit: y = -0.172x + 7.9
- P-value: 0.0420
- N samples: 64

**Model Size (B):**
- Correlation: -0.212 
- Linear fit: y = -0.001x + 3.1
- P-value: 0.1102
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.193 
- Linear fit: y = -1.989x + 3.9
- P-value: 0.1265
- N samples: 64

**Is Open Source:**
- Correlation: 0.050 
- Linear fit: y = 0.424x + 2.2
- P-value: 0.6970
- N samples: 64

------------------------------------------------------------
### Correlations with: category2_factual_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.223 
- Linear fit: y = -2.837x + 9.0
- P-value: 0.0761
- N samples: 64

**Model Size (B):**
- Correlation: -0.124 
- Linear fit: y = -0.001x + 8.1
- P-value: 0.3539
- N samples: 58

**Is Reasoning Model:**
- Correlation: 0.101 
- Linear fit: y = 1.551x + 6.4
- P-value: 0.4264
- N samples: 64

**Days Since 2024-01-01:**
- Correlation: -0.038 
- Linear fit: y = -0.002x + 9.1
- P-value: 0.7757
- N samples: 58

**Benchmark Score:**
- Correlation: 0.021 
- Linear fit: y = 0.021x + 6.9
- P-value: 0.8670
- N samples: 64

------------------------------------------------------------
### Correlations with: category3_logical_errors
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.343 **
- Linear fit: y = -6.961x + 27.3
- P-value: 0.0055
- N samples: 64

**Days Since 2024-01-01:**
- Correlation: -0.330 *
- Linear fit: y = -0.026x + 45.6
- P-value: 0.0113
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.211 
- Linear fit: y = -5.171x + 28.1
- P-value: 0.0937
- N samples: 64

**Benchmark Score:**
- Correlation: -0.092 
- Linear fit: y = -0.147x + 28.8
- P-value: 0.4710
- N samples: 64

**Model Size (B):**
- Correlation: 0.047 
- Linear fit: y = 0.000x + 23.3
- P-value: 0.7251
- N samples: 58

------------------------------------------------------------
### Correlations with: category4_technical_errors
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.339 **
- Linear fit: y = -0.008x + 8.4
- P-value: 0.0093
- N samples: 58

**Benchmark Score:**
- Correlation: -0.294 *
- Linear fit: y = -0.141x + 6.3
- P-value: 0.0184
- N samples: 64

**Model Size (B):**
- Correlation: -0.206 
- Linear fit: y = -0.000x + 2.1
- P-value: 0.1200
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.112 
- Linear fit: y = -0.817x + 2.4
- P-value: 0.3802
- N samples: 64

**Is Open Source:**
- Correlation: 0.015 
- Linear fit: y = 0.090x + 1.7
- P-value: 0.9072
- N samples: 64

------------------------------------------------------------
### Correlations with: 1a_instruction_override
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.242 
- Linear fit: y = -1.134x + 1.7
- P-value: 0.0545
- N samples: 64

**Days Since 2024-01-01:**
- Correlation: -0.235 
- Linear fit: y = -0.004x + 4.0
- P-value: 0.0764
- N samples: 58

**Benchmark Score:**
- Correlation: -0.216 
- Linear fit: y = -0.066x + 3.0
- P-value: 0.0868
- N samples: 64

**Model Size (B):**
- Correlation: -0.207 
- Linear fit: y = -0.000x + 1.2
- P-value: 0.1188
- N samples: 58

**Is Open Source:**
- Correlation: 0.067 
- Linear fit: y = 0.261x + 0.7
- P-value: 0.5986
- N samples: 64

------------------------------------------------------------
### Correlations with: 1b_context_omission
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.216 
- Linear fit: y = -0.004x + 4.4
- P-value: 0.1034
- N samples: 58

**Model Size (B):**
- Correlation: -0.211 
- Linear fit: y = -0.000x + 1.5
- P-value: 0.1115
- N samples: 58

**Benchmark Score:**
- Correlation: -0.208 
- Linear fit: y = -0.070x + 3.5
- P-value: 0.0997
- N samples: 64

**Is Reasoning Model:**
- Correlation: -0.099 
- Linear fit: y = -0.511x + 1.6
- P-value: 0.4374
- N samples: 64

**Is Open Source:**
- Correlation: 0.012 
- Linear fit: y = 0.053x + 1.1
- P-value: 0.9229
- N samples: 64

------------------------------------------------------------
### Correlations with: 1c_prompt_contradiction
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.308 *
- Linear fit: y = -0.002x + 2.2
- P-value: 0.0185
- N samples: 58

**Benchmark Score:**
- Correlation: -0.266 *
- Linear fit: y = -0.035x + 1.5
- P-value: 0.0337
- N samples: 64

**Is Reasoning Model:**
- Correlation: -0.169 
- Linear fit: y = -0.343x + 0.6
- P-value: 0.1818
- N samples: 64

**Is Open Source:**
- Correlation: 0.065 
- Linear fit: y = 0.110x + 0.3
- P-value: 0.6079
- N samples: 64

**Model Size (B):**
- Correlation: -0.057 
- Linear fit: y = -0.000x + 0.4
- P-value: 0.6711
- N samples: 58

------------------------------------------------------------
### Correlations with: 2a_concept_fabrication
------------------------------------------------------------

**Model Size (B):**
- Correlation: -0.250 
- Linear fit: y = -0.000x + 1.6
- P-value: 0.0584
- N samples: 58

**Is Open Source:**
- Correlation: 0.232 
- Linear fit: y = 0.737x + 1.0
- P-value: 0.0651
- N samples: 64

**Benchmark Score:**
- Correlation: -0.203 
- Linear fit: y = -0.051x + 3.0
- P-value: 0.1078
- N samples: 64

**Is Reasoning Model:**
- Correlation: 0.125 
- Linear fit: y = 0.480x + 1.0
- P-value: 0.3246
- N samples: 64

**Days Since 2024-01-01:**
- Correlation: -0.018 
- Linear fit: y = -0.000x + 1.5
- P-value: 0.8949
- N samples: 58

------------------------------------------------------------
### Correlations with: 2b_spurious_numeric
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.292 *
- Linear fit: y = -3.518x + 7.6
- P-value: 0.0191
- N samples: 64

**Model Size (B):**
- Correlation: -0.083 
- Linear fit: y = -0.000x + 6.2
- P-value: 0.5367
- N samples: 58

**Is Reasoning Model:**
- Correlation: 0.066 
- Linear fit: y = 0.966x + 5.2
- P-value: 0.6017
- N samples: 64

**Benchmark Score:**
- Correlation: 0.058 
- Linear fit: y = 0.055x + 4.2
- P-value: 0.6511
- N samples: 64

**Days Since 2024-01-01:**
- Correlation: -0.049 
- Linear fit: y = -0.002x + 7.8
- P-value: 0.7166
- N samples: 58

------------------------------------------------------------
### Correlations with: 2c_false_citation
------------------------------------------------------------

**Benchmark Score:**
- Correlation: 0.214 
- Linear fit: y = 0.018x + -0.3
- P-value: 0.0901
- N samples: 64

**Model Size (B):**
- Correlation: 0.191 
- Linear fit: y = 0.000x + 0.2
- P-value: 0.1515
- N samples: 58

**Days Since 2024-01-01:**
- Correlation: 0.158 
- Linear fit: y = 0.001x + -0.2
- P-value: 0.2349
- N samples: 58

**Is Reasoning Model:**
- Correlation: 0.084 
- Linear fit: y = 0.106x + 0.2
- P-value: 0.5097
- N samples: 64

**Is Open Source:**
- Correlation: -0.054 
- Linear fit: y = -0.057x + 0.3
- P-value: 0.6689
- N samples: 64

------------------------------------------------------------
### Correlations with: 3a_unsupported_leap
------------------------------------------------------------

**Is Open Source:**
- Correlation: -0.390 **
- Linear fit: y = -6.210x + 22.7
- P-value: 0.0014
- N samples: 64

**Days Since 2024-01-01:**
- Correlation: -0.340 **
- Linear fit: y = -0.021x + 37.1
- P-value: 0.0091
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.149 
- Linear fit: y = -2.860x + 22.0
- P-value: 0.2404
- N samples: 64

**Model Size (B):**
- Correlation: 0.089 
- Linear fit: y = 0.000x + 19.0
- P-value: 0.5047
- N samples: 58

**Benchmark Score:**
- Correlation: -0.058 
- Linear fit: y = -0.073x + 22.1
- P-value: 0.6507
- N samples: 64

------------------------------------------------------------
### Correlations with: 3b_self_contradiction
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.296 *
- Linear fit: y = -2.189x + 5.9
- P-value: 0.0177
- N samples: 64

**Days Since 2024-01-01:**
- Correlation: -0.212 
- Linear fit: y = -0.005x + 8.6
- P-value: 0.1102
- N samples: 58

**Benchmark Score:**
- Correlation: -0.139 
- Linear fit: y = -0.068x + 6.4
- P-value: 0.2729
- N samples: 64

**Is Open Source:**
- Correlation: -0.129 
- Linear fit: y = -0.788x + 4.6
- P-value: 0.3113
- N samples: 64

**Model Size (B):**
- Correlation: -0.065 
- Linear fit: y = -0.000x + 4.3
- P-value: 0.6295
- N samples: 58

------------------------------------------------------------
### Correlations with: 3c_circular_reasoning
------------------------------------------------------------

**Is Reasoning Model:**
- Correlation: -0.240 
- Linear fit: y = -0.123x + 0.1
- P-value: 0.0558
- N samples: 64

**Benchmark Score:**
- Correlation: -0.209 
- Linear fit: y = -0.007x + 0.3
- P-value: 0.0968
- N samples: 64

**Model Size (B):**
- Correlation: -0.132 
- Linear fit: y = -0.000x + 0.1
- P-value: 0.3238
- N samples: 58

**Is Open Source:**
- Correlation: 0.088 
- Linear fit: y = 0.037x + 0.0
- P-value: 0.4895
- N samples: 64

**Days Since 2024-01-01:**
- Correlation: 0.073 
- Linear fit: y = 0.000x + -0.1
- P-value: 0.5838
- N samples: 58

------------------------------------------------------------
### Correlations with: 4a_syntax_error
------------------------------------------------------------

**Days Since 2024-01-01:**
- Correlation: -0.409 **
- Linear fit: y = -0.005x + 4.3
- P-value: 0.0014
- N samples: 58

**Benchmark Score:**
- Correlation: -0.182 
- Linear fit: y = -0.041x + 1.8
- P-value: 0.1507
- N samples: 64

**Model Size (B):**
- Correlation: -0.136 
- Linear fit: y = -0.000x + 0.5
- P-value: 0.3078
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.077 
- Linear fit: y = -0.263x + 0.6
- P-value: 0.5458
- N samples: 64

**Is Open Source:**
- Correlation: -0.047 
- Linear fit: y = -0.133x + 0.5
- P-value: 0.7117
- N samples: 64

------------------------------------------------------------
### Correlations with: 4b_model_semantics_breach
------------------------------------------------------------

**Benchmark Score:**
- Correlation: -0.290 *
- Linear fit: y = -0.098x + 4.4
- P-value: 0.0200
- N samples: 64

**Model Size (B):**
- Correlation: -0.199 
- Linear fit: y = -0.000x + 1.5
- P-value: 0.1349
- N samples: 58

**Days Since 2024-01-01:**
- Correlation: -0.193 
- Linear fit: y = -0.003x + 4.0
- P-value: 0.1475
- N samples: 58

**Is Reasoning Model:**
- Correlation: -0.097 
- Linear fit: y = -0.503x + 1.6
- P-value: 0.4442
- N samples: 64

**Is Open Source:**
- Correlation: 0.037 
- Linear fit: y = 0.157x + 1.2
- P-value: 0.7737
- N samples: 64

------------------------------------------------------------
### Correlations with: 4c_visual_descr_mismatch
------------------------------------------------------------

**Is Open Source:**
- Correlation: 0.191 
- Linear fit: y = 0.067x + 0.0
- P-value: 0.1302
- N samples: 64

**Is Reasoning Model:**
- Correlation: -0.122 
- Linear fit: y = -0.051x + 0.1
- P-value: 0.3361
- N samples: 64

**Days Since 2024-01-01:**
- Correlation: -0.122 
- Linear fit: y = -0.000x + 0.2
- P-value: 0.3629
- N samples: 58

**Benchmark Score:**
- Correlation: -0.077 
- Linear fit: y = -0.002x + 0.1
- P-value: 0.5453
- N samples: 64

**Model Size (B):**
- Correlation: 0.007 
- Linear fit: y = 0.000x + 0.0
- P-value: 0.9567
- N samples: 58

================================================================================
## SUMMARY STATISTICS
================================================================================

### Strongest Correlations (|r| > 0.3):
----------------------------------------
**4a_syntax_error vs Days Since 2024-01-01:**
  r = -0.409, y = -0.005x + 4.3

**3a_unsupported_leap vs Is Open Source:**
  r = -0.390, y = -6.210x + 22.7

**category3_logical_errors vs Is Open Source:**
  r = -0.343, y = -6.961x + 27.3

**3a_unsupported_leap vs Days Since 2024-01-01:**
  r = -0.340, y = -0.021x + 37.1

**category4_technical_errors vs Days Since 2024-01-01:**
  r = -0.339, y = -0.008x + 8.4

**category3_logical_errors vs Days Since 2024-01-01:**
  r = -0.330, y = -0.026x + 45.6

**1c_prompt_contradiction vs Days Since 2024-01-01:**
  r = -0.308, y = -0.002x + 2.2


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
- Correlation: 0.615 ***
- Linear fit: y = 0.916x + 5.5

**Category 1: Input Misalignment**
  vs **Category 3: Logical Errors:**
- Correlation: 0.556 ***
- Linear fit: y = 1.321x + 20.9

**Category 1: Input Misalignment**
  vs **Category 4: Technical Errors:**
- Correlation: 0.500 ***
- Linear fit: y = 0.356x + 0.9

**Category 2: Factual Errors**
  vs **Category 3: Logical Errors:**
- Correlation: 0.575 ***
- Linear fit: y = 0.918x + 17.0

**Category 2: Factual Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.406 ***
- Linear fit: y = 0.194x + 0.2

**Category 3: Logical Errors**
  vs **Category 4: Technical Errors:**
- Correlation: 0.420 ***
- Linear fit: y = 0.126x + -1.3

### TOP 20 STRONGEST INTER-HALLUCINATION CORRELATIONS
----------------------------------------

**Category 3: Logical Errors vs 3a: Unsupported Leap:**
  r = 0.969 ***, y = 0.761x + 1.5

**Category 2: Factual Errors vs 2b: Spurious Numeric:**
  r = 0.965 ***, y = 0.914x + -1.0

**Category 1: Input Misalignment vs 1b: Context Omission:**
  r = 0.925 ***, y = 0.465x + 0.1

**Category 4: Technical Errors vs 4b: Model Semantics Breach:**
  r = 0.902 ***, y = 0.636x + 0.2

**Category 1: Input Misalignment vs 1a: Instruction Override:**
  r = 0.864 ***, y = 0.394x + -0.1

**Category 3: Logical Errors vs 3b: Self Contradiction:**
  r = 0.784 ***, y = 0.237x + -1.5

**Category 4: Technical Errors vs 4a: Syntax Error:**
  r = 0.777 ***, y = 0.363x + -0.2

**Category 1: Input Misalignment vs 1c: Prompt Contradiction:**
  r = 0.717 ***, y = 0.141x + 0.0

**1a: Instruction Override vs 3b: Self Contradiction:**
  r = 0.691 ***, y = 1.088x + 3.3

**1b: Context Omission vs 1c: Prompt Contradiction:**
  r = 0.652 ***, y = 0.255x + 0.1

**Category 1: Input Misalignment vs 3b: Self Contradiction:**
  r = 0.648 ***, y = 0.466x + 3.1

**1a: Instruction Override vs 1b: Context Omission:**
  r = 0.647 ***, y = 0.713x + 0.6

**Category 1: Input Misalignment vs Category 2: Factual Errors:**
  r = 0.615 ***, y = 0.916x + 5.5

**3a: Unsupported Leap vs 3b: Self Contradiction:**
  r = 0.608 ***, y = 0.234x + -0.4

**Category 3: Logical Errors vs 2b: Spurious Numeric:**
  r = 0.608 ***, y = 0.361x + -2.7

**Category 1: Input Misalignment vs 2b: Spurious Numeric:**
  r = 0.606 ***, y = 0.855x + 3.9

**Category 2: Factual Errors vs 1a: Instruction Override:**
  r = 0.604 ***, y = 0.185x + -0.6

**Category 2: Factual Errors vs 1b: Context Omission:**
  r = 0.602 ***, y = 0.203x + -0.4

**1b: Context Omission vs 2b: Spurious Numeric:**
  r = 0.593 ***, y = 1.663x + 4.0

**2b: Spurious Numeric vs 3a: Unsupported Leap:**
  r = 0.584 ***, y = 0.773x + 15.2

### NOTABLE NEGATIVE CORRELATIONS (Trade-offs)
----------------------------------------

No significant negative correlations found between hallucination types.

================================================================================
## END OF ANALYSIS
================================================================================
