# Transformer Context Sufficiency

Reproducibility package for the published article:

**Context Sufficiency in Transformers: Information-Theoretic Limits, Native Functional Dependence, Representational Accessibility, and Predictive Readout**

Dimitris Karydas, Dimosthenis Margaritis and Helen C. Leligou. *Computers* **2026**, 15(11), 769.

[Published article](https://www.mdpi.com/2073-431X/15/11/769)

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

The small final HMM CSV/JSON outputs needed by the unified reproduction notebook are mirrored in `results/`. The complete HMM archive is maintained separately from the lightweight GitHub inputs. The archival deposit designated in the article is [Zenodo 10.5281/zenodo.23528707](https://doi.org/10.5281/zenodo.23528707); the deposit must be published before that reserved DOI provides public access. The full HMM archive is not required for analysis-only reproduction.

## Automated verification

For CPU-only verification from the frozen archives:

```bash
python -m pip install -r requirements-analysis.txt
python scripts/verify_inputs.py
python scripts/run_reproduction.py
```

The runner uses a fresh temporary directory and writes to a new
`validation-run/` directory. It verifies input checksums, runs every analysis
cell, requires all 15 figures, and fails on numerical-audit errors. See
`REPRODUCIBILITY.md` for tolerances and `reproducibility/EXPERIMENTS.md` for
GPU rerun prerequisites and diagnostics. This verifies analysis from archived
outputs; it does not establish a new full-training replication.

## Documentation

- `REPRODUCIBILITY.md` maps each analysis component to its experiment notebook, archived outputs, and reproduced figures.
- `CITATION.cff` provides repository citation metadata.

## Figures


The `figures/` directory contains the 15 reproduced figures generated from the archived outputs, including the corrected HMM gap-decomposition figure.

## Reproducibility scope

The unified notebook reproduces the reported analyses from completed outputs. It is intentionally not described as end-to-end retraining reproduction.

The experiment notebooks under `notebooks/` are provided for provenance and full reruns, including the scratch Markov experiments, Qwen representation studies, causal intervention, robustness and coverage analyses, Pythia cross-family validation, true-state predictive-readout control, and the latent-state HMM extension.

## Publication and frozen snapshot

The article is published in *Computers*; the publication-facing metadata is maintained on the default branch.

The exact reproducibility snapshot cited in the article is commit [`ad6cdf33e91a767634b5cbfd06e85b8cbe0fd14d`](https://github.com/ecdlschool-bit/transformer-context-sufficiency/tree/ad6cdf33e91a767634b5cbfd06e85b8cbe0fd14d). Later documentation updates do not replace this frozen snapshot or change its experiment data. The separately prepared snapshot ZIP and full HMM ZIP retain their original checksums for the archival deposit.

Analysis reproduction uses the archived outputs and requires no GPU training rerun. Complete historical GPU environment details were not recorded for every experiment; see `reproducibility/EXPERIMENTS.md` for the documented provenance and limitations.

## License

The project-authored code and documentation are distributed under the MIT license; see `LICENSE`. Third-party model weights and dependencies retain their own licenses.
