#!/usr/bin/env bash
# Build local del proyecto: genera programa-completo.md y el Word desde docs/.
# Requiere python3 y, para el Word, pandoc.
set -euo pipefail
cd "$(dirname "$0")"
python3 build/build.py
