# Valoria — System Transparency Console

A **data-management & observability layer** that makes the *shaping of the shape* visible:
pick any Key, score, scalar, or engine and watch how it ripples through the whole system —
upstream (what causes it) and downstream (what it affects), across every scale.

It exists because the engine's wiring lives scattered across 1,200+ design files. This tool
**assembles the canonical machine-readable sources into one navigable graph** so you can *see*
how attributes / scores / statistics / Keys propagate, instead of reading it file by file.

## What it shows

- **Systems (engines)** — every mechanical engine as its `IN(consumed Keys) → resolver → OUT(emitted Keys)`
  wrapper contract, plus the scalars it owns, its gates, its cross-scale transitions, and its GD-constraints.
- **Keys** — all 44 vectorized Key types: who emits each, who consumes it, its family/scale/permanence,
  and whether it is registered / broadcast / unregistered.
- **Scalars** — every owned quantity, its **bucket** (pool / derived_value / track / clock), its
  **write-legality** (writable vs derived/write-protected — the F1 guard), its derivation, and the
  gates that fire on it.
- **Ripple Explorer** — select any node; the console traces multi-hop propagation both directions
  (cause chain ↑ and consequence cascade ↓) with an adjustable depth.
- **Atlas** — all engines banded by scale with the aggregate emit→consume flow between them.
- **Lexicon** (the terminology layer) — every definition, abbreviation, name / alias / synonym /
  legacy name, plus **abbreviation collisions** (PT, CI, PC, IP…), **deprecated** renames
  (RS→MS, EventImpact→Key…), **censured** and **placeholder** terms. Search resolves any alias or
  abbreviation to its canonical term; terms link to their graph node where one exists.
- **Handshakes** — the named cross-scale handoffs (`scale_transitions §3` + Domain Echo §5): the
  inter-container ripples drawn as a scale-to-scale diagram. These are *authored sugar* over the
  all-directions Key substrate beneath.
- **Health panel (chips)** — emit/route closure %, orphan emits, broadcast keys, **naming alerts**
  (the canonical registry-system ↔ module-name drift, surfaced and reconciled, never hidden), and
  term / abbreviation / collision / handshake counts.
- **Governance layer (the unified dashboard)** — three cross-linked feeds fold the project's
  *open work* into the same console as its *structure*, joined on **lane**, **file**, and
  **declared system**:
  - **Health** (left tab + canvas **Health** mode) — the `review_core` CI signals (blocking vs
    report-only, verdict, regression-vs-baseline) with the repo-state **grade** (GREEN / AMBER /
    RED), presented as a **lane × {CI signals · proposals · needs-Jordan · open decisions · P1}**
    matrix plus the signal roster and the decision-debt file hotspots. Every cell click-throughs
    into the filtered list.
  - **Proposals** — the unified unratified-work register (`build_proposals`): every provisional
    doc / proposal / actionable ledger item, lane-partitioned, **needs-Jordan** flagged.
  - **Decisions** — the marker-level decision debt (`build_decisions`): 900+ open
    ratification / ruling / naming / gap / assumption / stub markers, priority-sorted, each with
    its source locations and any `systems[]` it touches.
  - **Cross-links both ways:** a governance item's detail lists its file locations (click to copy)
    and jumps to the graph node whose home doc it targets; a graph node's detail gains a
    **governance — open work** section listing the decisions/proposals attached to it; and the
    **lane lens** (a chip on every governance detail + the Health matrix) focuses one lane across
    *all* panels at once.

## Use it

**Fastest:** double-click **`console.html`** — it is fully self-contained (data inlined) and works
offline with no server.

**Dev pair (regenerable):** `index.html` + `graph_data.js`. If your browser blocks the local data
file on `file://`, serve the folder:

```bash
python tools/observability/build_graph.py     # (re)build the graph from canon
python -m http.server 8000                     # then open http://localhost:8000/tools/observability/
```

## Regenerate after canon changes

```bash
python tools/observability/build_graph.py
```

This one command rebuilds the graph + lexicon (it calls `build_lexicon.py` for you) and
re-inlines **all present feeds** into the self-contained `console.html`. The three governance
feeds are built by their own generators on the audit-refresh cadence — to refresh them too:

```bash
python tools/observability/build_decisions.py    # decisions_data.js
python tools/observability/build_proposals.py     # proposals_data.js
python tools/review_core.py --json                # review_state_data.js (git-ignored, live)
python tools/observability/build_graph.py         # rebuilds console.html inlining all five
```

## Data sources (single source of truth — nothing is invented)

| Source | Provides |
|---|---|
| `references/module_contracts.yaml` | the `IN → resolver → OUT` wrapper contracts + owned scalars + gates + derivations + transitions |
| `designs/architecture/key_type_registry_v30.md` | authoritative Key metadata + emit/consume routing (the vectorized routing) |
| `registers/mechanics_index.yaml` | scale / GD-constraint / sim-module enrichment per mechanic |
| `references/alias_registry.yaml` + `name_collision_database.yaml` + `synonym_registry.yaml` | canonical names, abbreviations, aliases, silos, collisions |
| `references/deprecated_terms_registry.yaml` + `censured_vocabulary.yaml` + `registers/placeholder_names.yaml` | retired / do-not-use / placeholder names |
| `references/glossary.md` + `descriptor_registry.yaml` + `proper_noun_registry.yaml` | definitions, ranges, attributes/stats/axes, world entities |
| `designs/architecture/scale_transitions_v30.md` | the cross-scale handshakes (§3 / §5 / §12) |

Every node and edge traces back to one of these files. The extractor (`build_graph.py`) reconciles the
known registry-system ↔ module-name vocabulary drift to a single canonical id for accurate ripple
tracing, and records every substitution in `graph.json → meta.naming_alerts`.

## Output files

| File | Purpose |
|---|---|
| `console.html` | self-contained unified viewer (**all five feeds** inlined) — **double-click to open** |
| `index.html` | viewer that loads the five `*_data.js` feeds (edit this to change the UI; rebuild to refresh `console.html`) |
| `graph_data.js` / `graph.json` | `window.VALORIA_GRAPH = {…}` — the propagation graph |
| `lexicon_data.js` / `lexicon.json` | `window.VALORIA_LEXICON = {…}` — terms, abbreviations, collisions, deprecated, handshakes |
| `decisions_data.js` / `decisions.json` | `window.VALORIA_DECISIONS = {…}` — marker-level decision debt (`build_decisions.py`) |
| `proposals_data.js` / `proposals.json` | `window.VALORIA_PROPOSALS = {…}` — the unratified-work register (`build_proposals.py`) |
| `review_state_data.js` / `review_state.json` | `window.VALORIA_REVIEW = {…}` — the `review_core.py` CI-health snapshot. **git-ignored** (live state): absent on a fresh clone; the viewer degrades gracefully and `build_graph` inlines it only when present |
| `build_graph.py` | the graph extractor (also drives the lexicon build + inlines all five feeds into the `console.html` bundle) |
| `build_lexicon.py` | the lexicon extractor |

## Relationship to the other two deliverables

This is the **observability** layer of a three-part shape:

1. **Architecture** — the consolidated Godot 4 structure (kernel wrapper → KeyBus → BaseEngine + EngineModule).
2. **Engine-Shape Conformance methodology (ESCP)** — how to evaluate each engine's shape.
3. **This console** — how to *see* the shape and its dynamics.

`graph.json` is the shared, machine-readable substrate for all three: the same Key-system shape the
architecture implements and the methodology evaluates. It can feed CI checks (closure %, orphan emits,
naming-alert count) and is the natural backing store for an in-engine debug overlay later.
