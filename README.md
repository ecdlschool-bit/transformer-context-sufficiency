# Transformer Context Sufficiency

Reproducibility package for the manuscript:

**Context Sufficiency in Transformers: Information-Theoretic Limits, Native Functional Dependence, Representational Accessibility, and Predictive Readout**

## Repository purpose

This repository provides two complementary levels of reproducibility:

1. **Analysis reproduction from archived outputs** — reproduces the reported tables, figures, and summary statistics without retraining models.
2. **Full experimental provenance** — retains the original experiment notebooks used to generate the archived outputs.

## Quick reproduction

For the fastest verification, open and run:

`reproduce_paper.ipynb`

The notebook automatically searches the repository root and `results/` for the archived experiment outputs.

A successful run ends with:

`PAPER REPRODUCTION FROM EXISTING RESULTS: PASS`

For immediate visual inspection without rerunning, see:

`reproduce_paper_executed.ipynb`

The executed notebook contains the reproduced tables, figures, audit outputs, and final PASS result.

## Repository structure

```text
.
├── README.md
├── requirements.txt
├── requirements-experiments.txt
├── reproduce_paper.ipynb
├── reproduce_paper_executed.ipynb
├── notebooks/      # original experiment notebooks
├── results/        # archived completed experiment outputs
└── figures/        # reproduced publication and supplementary figures
```

## Installation

For analysis-only reproduction:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook reproduce_paper.ipynb
```

For full experimental reruns, additionally install:

```bash
pip install -r requirements-experiments.txt
```

GPU-enabled PyTorch installation may depend on the local CUDA environment; use the appropriate PyTorch build for the target system.

## Important methodological note

For the latent-state HMM extension, the final information-gap calculation uses matched/same-history quantities. Older negative-gap intermediate outputs are obsolete and are not part of the final analysis.

The small final HMM CSV/JSON outputs needed by the unified reproduction notebook are mirrored in `results/`. The larger complete HMM archive will be provided separately as an archival research object.

## Documentation

- `REPRODUCIBILITY.md` maps each analysis component to its experiment notebook, archived outputs, and reproduced figures.
- `CITATION.cff` provides repository citation metadata.

## Figures


The `figures/` directory contains the 15 reproduced figures generated from the archived outputs, including the corrected HMM gap-decomposition figure.

## Reproducibility scope

The unified notebook reproduces the reported analyses from completed outputs. It is intentionally not described as end-to-end retraining reproduction.

The experiment notebooks under `notebooks/` are provided for provenance and full reruns, including the scratch Markov experiments, Qwen representation studies, causal intervention, robustness and coverage analyses, Pythia cross-family validation, true-state predictive-readout control, and the latent-state HMM extension.

## Release status

This repository is currently **private and under final preparation** for the manuscript revision. Before public release, it will receive a final audit for credentials, local paths, obsolete outputs, licensing, and consistency with the submitted manuscript.

## License

No license has been selected yet. Until a license is explicitly added, normal copyright rules apply.
