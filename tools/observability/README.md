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

This one command rebuilds **both** datasets (it calls `build_lexicon.py` for you) and rewrites
`graph.json`, `graph_data.js`, `lexicon.json`, `lexicon_data.js`, and the self-contained
`console.html`. Run it whenever the inputs change. (`build_lexicon.py` can also be run standalone.)

## Data sources (single source of truth — nothing is invented)

| Source | Provides |
|---|---|
| `references/module_contracts.yaml` | the `IN → resolver → OUT` wrapper contracts + owned scalars + gates + derivations + transitions |
| `designs/architecture/key_type_registry_v30.md` | authoritative Key metadata + emit/consume routing (the vectorized routing) |
| `canon/mechanics_index.yaml` | scale / GD-constraint / sim-module enrichment per mechanic |
| `references/alias_registry.yaml` + `name_collision_database.yaml` + `synonym_registry.yaml` | canonical names, abbreviations, aliases, silos, collisions |
| `references/deprecated_terms_registry.yaml` + `censured_vocabulary.yaml` + `canon/placeholder_names.yaml` | retired / do-not-use / placeholder names |
| `references/glossary.md` + `descriptor_registry.yaml` + `proper_noun_registry.yaml` | definitions, ranges, attributes/stats/axes, world entities |
| `designs/architecture/scale_transitions_v30.md` | the cross-scale handshakes (§3 / §5 / §12) |

Every node and edge traces back to one of these files. The extractor (`build_graph.py`) reconciles the
known registry-system ↔ module-name vocabulary drift to a single canonical id for accurate ripple
tracing, and records every substitution in `graph.json → meta.naming_alerts`.

## Output files

| File | Purpose |
|---|---|
| `console.html` | self-contained viewer (graph + lexicon inlined) — **double-click to open** |
| `index.html` | viewer that loads `graph_data.js` + `lexicon_data.js` (edit this to change the UI; rebuild to refresh `console.html`) |
| `graph_data.js` / `graph.json` | `window.VALORIA_GRAPH = {…}` — the propagation graph |
| `lexicon_data.js` / `lexicon.json` | `window.VALORIA_LEXICON = {…}` — terms, abbreviations, collisions, deprecated, handshakes |
| `build_graph.py` | the graph extractor (also drives the lexicon build + the bundle) |
| `build_lexicon.py` | the lexicon extractor |

## Relationship to the other two deliverables

This is the **observability** layer of a three-part shape:

1. **Architecture** — the consolidated Godot 4 structure (kernel wrapper → KeyBus → BaseEngine + EngineModule).
2. **Engine-Shape Conformance methodology (ESCP)** — how to evaluate each engine's shape.
3. **This console** — how to *see* the shape and its dynamics.

`graph.json` is the shared, machine-readable substrate for all three: the same Key-system shape the
architecture implements and the methodology evaluates. It can feed CI checks (closure %, orphan emits,
naming-alert count) and is the natural backing store for an in-engine debug overlay later.
