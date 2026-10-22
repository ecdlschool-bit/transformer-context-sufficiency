"""Check the frozen analysis inputs without downloading or training anything."""
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def verify(root=ROOT):
    manifest = json.loads((root / 'reproducibility/inputs.sha256.json').read_text())
    for name, expected in manifest['files'].items():
        path = root / name
        if not path.is_file():
            raise FileNotFoundError(f'Missing frozen input: {name}')
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError(f'SHA-256 mismatch: {name}')
        if path.suffix == '.zip':
            with zipfile.ZipFile(path) as archive:
                bad = archive.testzip()
                if bad:
                    raise ValueError(f'Corrupt archive member: {name}: {bad}')
    for path in [root / 'reproduce_paper.ipynb', *sorted((root / 'notebooks').glob('*.ipynb'))]:
        notebook = json.loads(path.read_text(encoding='utf-8'))
        for index, cell in enumerate(notebook['cells']):
            if cell['cell_type'] == 'code':
                compile(''.join(cell['source']), f'{path.name}:cell{index}', 'exec')
                if any(output.get('output_type') == 'error' for output in cell.get('outputs', [])):
                    raise ValueError(f'Stored error in {path.name}:cell{index}')
    print(f"INPUT VERIFICATION: PASS ({len(manifest['files'])} frozen inputs; notebook syntax checked)")
    return manifest


if __name__ == '__main__':
    verify()
