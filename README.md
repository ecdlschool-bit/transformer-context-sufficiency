# Transformer Context Sufficiency

Reproducibility package for the manuscript:

**Context Sufficiency in Transformers: From Information-Theoretic Limits to Representational Accessibility, Predictive Readout, and Native Functional Dependence**

## Status

This repository is currently **private and under preparation** for the manuscript revision.  
Do not treat the repository contents as a final archival release until a versioned release is created.

## Reproducibility design

The repository separates two levels of reproducibility:

1. **Analysis reproduction from archived experiment outputs**  
   A unified notebook reproduces the reported tables, figures, and summary statistics from the archived outputs, without retraining models.

2. **Full experimental provenance**  
   The original experiment notebooks and configurations are retained for rerunning the underlying experiments.

The unified analysis notebook is:

`Reproduce_Paper_From_Existing_Results_FOLDER_AWARE.ipynb`

A successful run ends with:

`PAPER REPRODUCTION FROM EXISTING RESULTS: PASS`

## Planned repository structure

```text
.
├── README.md
├── requirements.txt
├── .gitignore
├── Reproduce_Paper_From_Existing_Results_FOLDER_AWARE.ipynb
├── notebooks/
├── results/
└── figures/
```

## Important methodological note

For the latent-state HMM extension, the corrected information-gap calculation uses matched/same-history quantities. Older negative-gap intermediate outputs are not part of the final analysis and must not be used.

## Release policy

Before this repository is made public, it will receive a final audit for:
- credentials and tokens,
- personal/local paths,
- obsolete intermediate results,
- reviewer/editor correspondence,
- licensing and third-party model constraints,
- consistency between manuscript figures/tables and archived outputs.

## License

No license has been selected yet. Until a license is explicitly added, normal copyright rules apply.
