# Experiment notebooks

This directory contains the experiment notebooks used for the manuscript.

- `Part1_Markov_Context_Sufficiency_A100.ipynb`: finite-order Markov experiments and information-theoretic baselines
- `Part1_Causal_Intervention_A100.ipynb`: input interventions and activation patching
- `Part2_Sufficiency_Representation_A100.ipynb`: frozen Qwen representation and predictive readout
- `Part2_InputVsState_Control_A100.ipynb`: visible-input versus full-state control
- `Part2_TrueState_PredictiveReadout_Control.ipynb`: predictive readout from the exact Markov state
- `Part2_Pythia_CrossFamily_Validation_A100.ipynb`: Pythia-410M cross-family validation
- `Robustness_Checks_A100.ipynb`: robustness analyses
- `True_State_Coverage_A100.ipynb`: state-space coverage analysis
- `HMM_Latent_State_Extension_A100.ipynb`: latent-state HMM extension
- `HMM_Information_Gap_Correction_GPU.ipynb`: corrected same-history HMM information-gap calculation

The `A100` suffix records the original GPU-oriented execution environment. Compatible hardware may also be used.

Some archived output filenames retain their original internal labels for compatibility with the unified reproduction notebook.

For paper-level verification, use the root-level `reproduce_paper.ipynb`.
