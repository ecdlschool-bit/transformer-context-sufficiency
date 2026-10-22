# Experimental reruns

## Working directory and order

Start every notebook with its kernel working directory at the repository root,
even when the notebook itself lives in `notebooks/`. For example, start Jupyter
at the root and change the kernel directory to the root before executing cells.
The notebooks create `Markov_Context_Paper/` relative to that working directory.
Use new directories for diagnostic runs; resume files from reduced runs must not
be mixed with publication runs.

1. Run `Part1_Markov_Context_Sufficiency_A100.ipynb` for scratch training.
   The default main sweep uses five seeds and 3,000 steps. The later k=4
   refinement cell runs a separate five-seed, 12,000-step sweep.
   Capacity, sparse, and larger-vocabulary sections have separate switches.
2. Run `Part1_Causal_Intervention_A100.ipynb` after scratch training. It requires
   the exact saved kernels and best/last checkpoints in `Part1/runs/`, including
   k=4 refinement. Lightweight CSV archives do not contain these checkpoints.
3. Run the Qwen representation, input/state, true-state, and Pythia notebooks
   for their respective datasets and probes. Qwen and Pythia weights are fetched
   from Hugging Face on first use; those weights are not distributed here.
4. Run `Robustness_Checks_A100.ipynb` after scratch training for A1-A4;
   its intervention stages require scratch kernels/checkpoints.
   Run `True_State_Coverage_A100.ipynb` for A3b independently.
5. Run the HMM extension, then the HMM information-gap correction. The
   corrected same-history KL archive is the authoritative information gap.

The repository's unified analysis notebook reads completed archives. It does
not automatically rebuild all publication archives from raw training runs.
Full reruns require the experiment-specific export/aggregation cells. Existing
archives remain the reference for the submitted analyses.

## Diagnostics versus full runs

`python scripts/verify_inputs.py` is the lightweight package smoke check. It
checks checksums, ZIP CRCs, notebook syntax, and stored errors without a GPU or
training. It is not a numerical training test.

| Notebook | Reduced diagnostic setting | Full configuration |
| --- | --- | --- |
| Scratch Markov | `QUICK_TEST=True`; run only main cells through the main sweep; skip the later refinement and optional sections | `QUICK_TEST=False`; five seeds; enable the desired optional controls explicitly |
| Scratch causal | `QUICK_TEST=True` reduces evaluation contexts, but still requires canonical full-training checkpoints | `QUICK_TEST=False`; five seeds |
| Qwen representation | `SMOKE_TEST=True` | `SMOKE_TEST=False`; two checkpoints, ten seeds |
| Input/state | No built-in reduced mode; use the package smoke check | Two Qwen checkpoints, ten seeds |
| True-state readout | `SMOKE_TEST=True` | `SMOKE_TEST=False`; ten seeds |
| Pythia | `SMOKE_TEST=True` | `SMOKE_TEST=False`; ten seeds |
| Robustness | `QUICK_TEST=True` reduces selected budgets; A1 still needs canonical checkpoints | `QUICK_TEST=False`; settings in the configuration cell |
| A3b | No built-in reduced mode; use the package smoke check | Five seeds; 12k, 24k, 48k, 96k examples |
| HMM extension | No built-in reduced mode; use the package smoke check | Three seeds; L=2,4,8,16,32 |
| HMM correction | No built-in reduced mode; use the package smoke check | CUDA required; three seeds; 100k histories per seed |

Do not Run All on the scratch notebook expecting QUICK_TEST to reduce the
separately configured k=4 refinement. Reduced runs do not satisfy the paper's
sample sizes, uncertainty estimates, or numerical reference checks.

## Environment and checkpoint provenance

The archived robustness environment records Python 3.11.0rc1, PyTorch
2.5.1+cu124, CUDA 12.4, and NVIDIA A100-SXM4-40GB MIG 3g.20gb (BF16).
This is historical provenance, not a claim that every experiment used identical
package versions. Complete historical NumPy/pandas/Transformers/Accelerate
versions and immutable Hugging Face revisions were not recorded in that file.
They cannot be recovered reliably by choosing the latest revision today.

`requirements-analysis.txt` pins the separately validated CPU analysis stack.
`requirements-experiments.txt` retains compatibility ranges for GPU reruns;
it is not a historical training lockfile. Select the PyTorch CUDA build for
the host. For future full runs, record `pip freeze`, CUDA/driver versions,
hardware, seeds, and the actual immutable model revision with the outputs:

```bash
python scripts/record_environment.py --output run-environment.json
```

For pretrained reruns, resolve a model's immutable Hugging Face commit, pass it
as `revision="<40-character SHA>"` to each relevant `from_pretrained` call,
and record `--model MODEL_ID@COMMIT_SHA` with the command above. The notebooks
currently specify model IDs without historical revision pins; a new run must
not be described as a bitwise replication of the old checkpoint extraction.
These experiments map symbols directly to vocabulary IDs; they do not tokenize
natural-language text. Third-party model weights retain their own licenses.

## Resources and timing

Analysis reproduction needs a CPU and no model downloads. Experiment reruns
were designed for an A100-class CUDA environment; VRAM requirements depend on
the checkpoint, extraction batch, and probe configuration. Lower extraction
batches if required, while keeping the scientific settings fixed. Full scratch
sweeps and pretrained extraction are substantially more expensive than analysis.
No portable end-to-end GPU runtime has been measured for this package; do not
interpret an analysis runtime as an experimental-rerun estimate. Record actual
timing on the target machine. GPU kernels and Monte Carlo estimators can produce
cross-platform differences even with fixed seeds.
