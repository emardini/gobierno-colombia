# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not a software application**. It is a book-length government plan for Colombia ("Estado en el Territorio"), written in **Spanish**, published as versioned Markdown. The content is the product. Almost all work here is editing prose, tables, and figures in Markdown — the only code is a single Python build script.

All contributor-facing docs, commit messages, and prose are in Spanish; match that language when editing content.

## Source of truth and generated artifacts

- **`docs/**/*.md` are the source of truth.** Everything else derives from them.
- Two consolidated artifacts are **generated, never edited by hand, and gitignored**: `plan-completo.md` (single-file Markdown) and `completo.html` (single-page static HTML). Do not commit them; they carry a "No editar a mano" banner and are rebuilt by CI.
- `_sidebar.md` defines both the navigation order of the live site **and** the section order the build script uses. Adding a new `docs/` section means adding it to `_sidebar.md` — otherwise it appears in neither the site nor the consolidated files.
- `docs/resumen-ejecutivo.md` is a curated executive summary (max ~20 pages). Unlike the two consolidated artifacts, it **is versioned**. It is regenerated **on demand** (by re-reading the current sections and re-synthesizing), not auto-built by CI, so it can drift; refresh it after large content changes.

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
- Docsify runs with `relativePath: true` plus an `alias` mapping every `_sidebar.md` request to `/_sidebar.md`. That is what makes relative cross-links (`../transversal/x.md`) resolve from nested pages. Consequence: links to the standalone **static** pages (`presentacion.html`, `completo.html`) must be **full absolute URLs** (`https://emardini.github.io/gobierno-colombia/...`). If left relative, Docsify hash-routes them (`#/docs/completo.html`) and they 404 from any page under `docs/`.

## Content structure

`docs/` is organized as: numbered foundation sections (`01-`…`06-`), `frentes/` (the fifteen policy fronts, `frente-01`…`frente-15`), `transversal/` (cross-cutting sections), `cierre/` (closing sections), `anexos/`, and `img/` (each figure kept as both `.svg` and `.png`). `BITACORA.md` narrates why the plan changed over time; `CHANGELOG.md` is the technical change log.

## Writing style (how the prose is written here)

All content is written the way a thoughtful, educated Colombian would write, not like a consulting report or AI-generated text. The content is in Spanish; the rules below govern that Spanish, and the quoted terms are the exact words to use.

- **Never em or en dashes (— –).** Use commas, periods, or parentheses. This is the most-broken rule; always check it.
- **No anglicisms.** Use the Spanish term. Settled conventions: **"mil millones" by default**, and "billones" only when genuinely justified (this was a real source of 1000x errors when "B" meant different things across documents); decimals with a comma; "caducidad" not "sunset"; "prueba de resistencia" not "stress test"; "compensación industrial (offset)" glossed; "poder blando", "encuadre", "marca país". Gloss acronyms on first use.
- **Varied rhythm.** Sentences of different lengths, neither all short nor all long.
- **No AI filler.** No "es importante notar", no "not only X but Y" constructions, no parallel triplets of adjectives, no flourish endings, no buzzwords.
- **Minimal formatting in the plan's content.** Prose and paragraphs, not bullets or excess bold. Tables are reserved for where they genuinely clarify (the ley/decreto/ejecución classification, cost breakdowns, risk matrices). This guide file does use lists because it is reference, not plan content.
- **Honesty in tone.** Every section names its limits and failures, not only its strengths; many close with an honesty note ("La honestidad de siempre" or equivalent). Mark estimates as order-of-magnitude estimates. Do not promise what no government can deliver.

## Working methodology

- **Research first, write second.** Nothing is written about figures or facts without grounding them.
- **Verify present-day facts with web search before asserting**: fiscal figures, credit rating, laws in force, who holds an office. Do not trust memory for what changes.
- **Show drafts before committing.** The author reviews and commits; the assistant does not commit on its own.
- **Respect the layer banners** (NÚCLEO / EJECUCIÓN / MIXTO) and do not rewrite the núcleo.
- **Whole-plan coherence.** A new section is added to `_sidebar.md`, cross-linked from related sections (with the specific point it connects to, not a generic "see also"), and its sources go into `fundamentos-investigacion.md`.
- **Reconcile figures across documents.** The same figure cannot say different things in two places.
- **The Linux sandbox may be down.** Work with the file and search tools; the local `build` is not essential because CI regenerates the artifacts on every push.

## Research principles

- **Ground claims in recent evidence**, cited inline with author and year, as the plan already does (Acemoglu and Robinson, Ostrom, North, Fergusson, Patashnik, Tyler, Kahan, Mockus, among others).
- **`docs/transversal/fundamentos-investigacion.md` is the sources index.** Every new finding enters as a row: the frontier finding, the concrete adjustment in the program, and where it applies.
- **Always present what works and its limit.** External validity (that what worked in another country works in Colombia) is an open question, not a guarantee. Distinguish strong causal evidence from informed analogy.
- **Prefer proven cases.** When the data does not exist, say so; do not invent it.

## Content principles (the spine of the plan)

- **Two roots, not twenty problems:** a State absent from the territory, and weak institutions with a fragile fiscal position.
- **One method: the node.** The State arrives complete and coordinated in a municipality, in phases, and expands only on verifiable results.
- **Honesty as strategy.** Every promise with its source; tell the failures too.
- **The burden (security, taxes, adjustment) never falls on the poorest.**
- **Counterweights before trust in any actor.** Govern with Congress, the Banco de la República and the courts, with respect and often subordinate to them, not against them.
- **Political realism:** govern in the minority (around 30% of Congress), executing what the Executive controls and leaving reforms that require legislation drafted and ready for when a window opens.
- **Data is the foundation; the story and the symbol are the vehicle.** Avoid cold technocracy.
- **Every major reform is designed to create the coalition that will defend it.**
- **Social ends through state capacity, mechanism design and fiscal honesty**, not through promised spending or confrontation.
- **Horizon 2042, beyond a single government.** No government will see a node graduate within its term, and the plan says so plainly.
