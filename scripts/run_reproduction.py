"""Execute analysis in a fresh directory containing only the declared inputs."""
import argparse
import importlib.metadata
import json
from pathlib import Path
import shutil
import sys
import tempfile
import time

from verify_inputs import ROOT, verify


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'validation-run')
    parser.add_argument('--timeout', type=int, default=1800, help='Seconds per cell')
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(f'Choose a new output directory: {output}')
    manifest = verify()
    import nbformat
    from nbclient import NotebookClient
    from jupyter_client import KernelManager
    from jupyter_client.kernelspec import KernelSpec

    class CurrentPythonKernel(KernelManager):
        @property
        def kernel_spec(self):
            return KernelSpec(argv=[sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}'],
                              display_name='Reproduction Python', language='python')

    output.mkdir(parents=True)
    start = time.monotonic()
    report = {'status': 'FAIL', 'python': sys.version.split()[0],
              'platform': sys.platform, 'input_source_commit': manifest['source_commit'],
              'packages': {p: importlib.metadata.version(p) for p in
                           ['numpy', 'pandas', 'matplotlib', 'nbformat', 'nbclient', 'ipykernel']}}
    notebook = nbformat.read(ROOT / 'reproduce_paper.ipynb', as_version=4)
    try:
        with tempfile.TemporaryDirectory(prefix='paper-reproduction-') as directory:
            work = Path(directory)
            for name in manifest['files']:
                target = work / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / name, target)
            client = NotebookClient(notebook, timeout=args.timeout, allow_errors=False,
                                    resources={'metadata': {'path': str(work)}},
                                    kernel_manager_class=CurrentPythonKernel)
            client.execute()
            products = work / 'Reproduced_Paper_Outputs'
            audit = json.loads((products / 'audit/reproduction_audit.json').read_text())
            if audit['status'] != 'PASS' or any(c['status'] != 'PASS' for c in audit['checks']):
                raise RuntimeError('Numerical reproduction audit failed')
            shutil.copytree(products, output / 'Reproduced_Paper_Outputs')
            report.update(status='PASS', checks=len(audit['checks']),
                          figures=len(list((products / 'figures').glob('*.png'))))
    except Exception as error:
        report['error'] = f'{type(error).__name__}: {error}'
        raise
    finally:
        report['elapsed_seconds'] = round(time.monotonic() - start, 2)
        # Keep a diagnostics notebook locally. Do not upload machine paths or tracebacks.
        nbformat.write(notebook, output / 'reproduction_executed.ipynb')
        (output / 'validation.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
