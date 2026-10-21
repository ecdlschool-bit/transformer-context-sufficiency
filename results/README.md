# Archived experiment outputs

This directory contains the completed experiment outputs used by the unified reproduction notebook.

## Required archives

- `Markov_Context_FINAL_ANALYSIS.zip`
- `Part2_Sufficiency_Representation_RESULTS.zip`
- `Part1_CAUSAL_INTERVENTION_RESULTS.zip`
- `Part2_Pythia_CrossFamily_Validation_RESULTS.zip`
- `Part2_TrueState_PredictiveReadout_Control_RESULTS.zip`
- `Reviewer_Robustness_Checks_RESULTS.zip`
- `Reviewer_A3b_TrueState_Coverage_RESULTS.zip`
- `HMM_Oracle_Gap_Fix_GPU_RESULTS.zip`

## Latent-state HMM extension

For lightweight analysis reproduction, the repository includes:

- `HMM_native_oracle_summary.csv`
- `HMM_probe_summary.csv`

These curated summaries contain the final predictive/oracle and probe/readout quantities used by the paper analysis.

The complete `HMM_Latent_State_Extension_RESULTS.zip` is larger than the normal GitHub web-upload limit and will be deposited as a separate archival research object.

### Corrected HMM information gap

The authoritative finite-context HMM information gap is **not** taken from the earlier independently estimated cross-entropy difference. The final paper uses the matched/same-history calculation stored in:

`HMM_Oracle_Gap_Fix_GPU_RESULTS.zip`

The obsolete negative-gap intermediate columns were intentionally omitted from the lightweight HMM summary mirrored here.

## Naming

The unified notebook accepts duplicate-download suffixes such as `(1)`, `(2)`, etc., for local use, while the repository uses canonical filenames.

## Reproducibility scope

These are completed experimental outputs. The unified notebook reproduces the paper analyses from them without retraining the underlying models.


## Archive naming

Some result archives retain their original internal experiment labels. These filenames are preserved for provenance and compatibility with the unified reproduction notebook; the publication-facing notebook names are listed in `../notebooks/README.md`.
