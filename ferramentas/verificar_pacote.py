#!/usr/bin/env python3
"""Confere os arquivos originais V7, sem executar os scripts do pacote."""
from pathlib import Path
import hashlib
import json
import sys


def main():
    root = Path(__file__).resolve().parents[1] / 'modelos-3d'
    manifest = json.loads((root / 'MANIFESTO_ARQUIVOS.json').read_text(encoding='utf-8'))
    failures = []
    for entry in manifest['arquivos']:
        path = (root / entry['arquivo']).resolve()
        if not path.is_relative_to(root.resolve()):
            failures.append(f"Caminho inválido: {entry['arquivo']}")
            continue
        if not path.is_file():
            failures.append(f"Ausente: {entry['arquivo']}")
            continue
        data = path.read_bytes()
        if len(data) != entry['bytes']:
            failures.append(f"Tamanho divergente: {entry['arquivo']}")
        if hashlib.sha256(data).hexdigest() != entry['sha256']:
            failures.append(f"SHA-256 divergente: {entry['arquivo']}")
    for failure in failures:
        print(failure, file=sys.stderr)
    print(f"{len(manifest['arquivos'])} arquivos verificados; {len(failures)} divergências.")
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
