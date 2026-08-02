# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not a software application**. It is a book-length government plan for Colombia ("Estado en el Territorio"), written in **Spanish**, published as versioned Markdown. The content is the product. Almost all work here is editing prose, tables, and figures in Markdown — the only code is a single Python build script.

All contributor-facing docs, commit messages, and prose are in Spanish; match that language when editing content.

## Source of truth and generated artifacts

- **`docs/**/*.md` are the source of truth.** Everything else derives from them.
- Two consolidated artifacts are **generated, never edited by hand, and gitignored**: `plan-completo.md` (single-file Markdown) and `completo.html` (single-page static HTML). Do not commit them; they carry a "No editar a mano" banner and are rebuilt by CI.
- `_sidebar.md` defines both the navigation order of the live site **and** the section order the build script uses. Adding a new `docs/` section means adding it to `_sidebar.md` — otherwise it appears in neither the site nor the consolidated files.

## Build & publish

```bash
pip install markdown                    # only dependency; requirements.txt is intentionally empty
python3 scripts/build-completo.py       # regenerates plan-completo.md + completo.html locally
```

The script (`scripts/build-completo.py`) parses `_sidebar.md`, skips the `Proyecto` group (`EXCLUDE_GROUPS`), reads each linked `.md`, strips its layer banner (the leading `> **…**` line), rewrites links so the consolidated files have no broken references (internal `.md` links → anchors, everything pointing outside the doc → plain text), and exits non-zero if any linked file is missing.

Publishing is automatic: `.github/workflows/pages.yml` runs the script and deploys to GitHub Pages on every push to **`master`** (note: the branch is `master`, not `main`). There is no other build/test/lint step.

The live navigable site is served by **Docsify** loaded from CDN in `index.html` — it renders the `.md` files directly in the browser with no compilation. `.nojekyll` is required so Pages serves `_sidebar.md` (leading-underscore files) and the raw `.md` untouched.

## Core vs. execution — the rule that governs all content edits

This is the single most important convention. The plan has two layers, and **every file in `docs/` opens with a banner blockquote declaring its layer**:

- **NÚCLEO** (`> **NÚCLEO, no se modifica por propuesta.**`) — the authored thesis: the "two roots" diagnosis, the nodes model, the guiding principles, the mechanism-design philosophy. **Do not rewrite the substance of these.** They are not open to change by proposal.
- **EJECUCIÓN** (`> **EJECUCIÓN, abierto a corrección con evidencia.**`) — figures, legal paths, timelines, thresholds, indicators, per-front detail. This is where edits and corrections belong.
- **MIXTO** — the principle is núcleo (fixed); the parameters are execution (editable).

When editing, respect the banner. Preserve it and its relative link back to `CONTRIBUTING.md`. `MAPA-NUCLEO-EJECUCION.md` is the at-a-glance map of which sections fall in which layer; `CONTRIBUTING.md` and `GOVERNANCE.md` explain the maintainer/authored-plan governance model.

## Link conventions

- `_sidebar.md` uses **absolute** site paths (e.g. `/docs/frentes/frente-01-empleo.md`); the build script strips the leading `/` to resolve them against the filesystem.
- Links **inside** `docs/` files are **relative** and point to `.md` files (not `.html`) — Docsify serves `.md` directly, so keeping the `.md` extension is what keeps links working. Broken internal links are a recurring maintenance theme (see recent commits), so verify relative paths when moving or adding sections.

## Content structure

`docs/` is organized as: numbered foundation sections (`01-`…`06-`), `frentes/` (the fifteen policy fronts, `frente-01`…`frente-15`), `transversal/` (cross-cutting sections), `cierre/` (closing sections), `anexos/`, and `img/` (each figure kept as both `.svg` and `.png`). `BITACORA.md` narrates why the plan changed over time; `CHANGELOG.md` is the technical change log.
