"""Record package/GPU versions and explicitly supplied model revisions."""
import argparse
import importlib.metadata
import json
from pathlib import Path
import platform


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--model', action='append', default=[], metavar='MODEL_ID@COMMIT_SHA',
                        help='Record the immutable revision actually passed to from_pretrained')
    args = parser.parse_args()
    packages = {}
    for name in ['numpy', 'pandas', 'matplotlib', 'torch', 'transformers', 'accelerate', 'safetensors']:
        try:
            packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            packages[name] = None
    models = {}
    for value in args.model:
        model, sep, revision = value.rpartition('@')
        if not sep or len(revision) != 40 or any(c not in '0123456789abcdef' for c in revision):
            parser.error('--model requires MODEL_ID@40_CHARACTER_COMMIT_SHA')
        models[model] = revision
    report = {'python': platform.python_version(), 'system': platform.system(),
              'packages': packages, 'model_revisions': models}
    if packages['torch']:
        import torch
        report['cuda_build'] = torch.version.cuda
        report['cuda_available'] = torch.cuda.is_available()
        report['gpus'] = [torch.cuda.get_device_name(i) for i in range(torch.cuda.device_count())]
    # Exclusive creation avoids overwriting the provenance of an earlier run.
    with args.output.open('x', encoding='utf-8') as stream:
        json.dump(report, stream, indent=2)
        stream.write('\n')
    print('Environment recorded; keep this file with the corresponding run outputs.')


if __name__ == '__main__':
    main()
