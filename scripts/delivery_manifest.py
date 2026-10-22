"""Hash the two final delivery archives without uploading or publishing them."""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--commit', required=True, help='Exact commit downloaded as the snapshot')
    parser.add_argument('--snapshot', required=True, type=Path)
    parser.add_argument('--hmm', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    if len(args.commit) != 40 or any(c not in '0123456789abcdef' for c in args.commit):
        parser.error('--commit must be the full 40-character Git SHA')
    files = []
    for path in [args.snapshot, args.hmm]:
        digest = hashlib.sha256()
        with path.open('rb') as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b''):
                digest.update(block)
        files.append({'name': path.name, 'bytes': path.stat().st_size, 'sha256': digest.hexdigest()})
    report = {'repository': 'ecdlschool-bit/transformer-context-sufficiency',
              'snapshot_commit': args.commit, 'files': files,
              'access': 'Private review delivery; no publication performed by this script'}
    with args.output.open('x', encoding='utf-8') as stream:
        json.dump(report, stream, indent=2)
        stream.write('\n')
    print('Delivery manifest written. The commit is supplied by the depositor; verify it before delivery.')


if __name__ == '__main__':
    main()
