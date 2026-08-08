# Vector audit — corpus-wide, 2026-08-06

## Status: PROPOSED (ED-IN-0148)

First vector audit since the 2026-08-05 evacuation (ED-IN-0145). The prior refresh was `c492de9`
(2026-07-22) — it predates the fork-direction inversion, the evacuation, and the CLAUDE.md §4/§8
restoration, with **1,322 in-scope files changed since**. Effectively every input had moved.

**Lane:** IN (infrastructure / cross-cutting). Corpus-wide, not subsystem-scoped.

## What ran

| Layer | Instrument | Output |
|---|---|---|
| Vector (multi-graph, L1) | `skills/valoria-vector-audit/scripts/vector_audit.py --layer L1` | `02_weakness_register.md`, `03_validation_report.md`, `data/` |
| Architecture (G_code + L2) | `skills/valoria-vector-audit/scripts/structure_audit.py` | `structure_audit/` |
| Vocabulary-debt triage | hand-authored from Mode G | `05_gm_resolution_register.md` |

Not run this pass: `formula_audit`, `pointer_audit`, `ripple_audit`, `gen_audit`, `workbench`.
**Coverage is therefore partial against the skill's full pipeline** — stated here rather than
implied by the folder's presence.

## Verdict

**PARTIAL.** Vector layer VALIDATED (2/3). P1 FAILED and that is itself a finding.

- **P1 foundation-periphery: FAIL** — foundation cite-mean **59.75 vs corpus median 76.5**. The
  canon philosophical foundations are *less* connected than the average document, in a repo where
  P-01..P-14 are the adjudication substrate.
- P2 conviction-symmetry: PASS (CV 0.39, ≤0.5 required)
- P3 citation-density: PASS (mean cite-degree 52.47, floor 6.0)

Scorecard: 199 design docs · 268 tokens · 14,062 cite-edges · 15 hubs · 28 implied-missing ·
13,707 notional · 235 cascade-sinks · 12 sparse · 4 isolates · 3 vocab-debt terms.

## Findings that survived scrutiny

1. **84 live "Game Master" delegations across 22 files** (67 after excluding the superseded
   `threadwork_v25_historical.md`), in a project whose first principle is *"There is no GM."*
   Fully dispositioned in `05_gm_resolution_register.md`: **30 open decisions, 6 mechanical
   rewrites, 12 already-ruled, 16 discarded, 3 non-defects.**
2. **4 canonical tokens are total isolates** — zero degree in all four graphs: `Active Inquisition`,
   `Counter-Intelligence`, `faction Mandate`, `faction Treasury income`. The last two are
   contract-declared faction state with no design prose anywhere.
3. **6 sparse tokens carry 0 paragraphs and 0 cite-degree**, including the registered Key types
   `mechanical.scene_exited` and `mechanical.scene_skipped`.
4. **`mass_battle` is the only one of 27 module contracts without a `sim_module:` field** — and it
   never had one. `structure_register.md` asserts inline that a nonzero UNDECLARED count "is itself a
   regression, **not a pre-existing gap**." Verified against `f03357d` (ED-IN-0097, the commit that
   introduced the field): 26 of 27 modules got it, `mass_battle` was missed. **The register's own
   regression-vs-pre-existing classification is wrong for this row.**
5. **J2 (2026-08-03) is registered but not executed.** J2 ruled `systems/mass_battle/sim/` "retired,
   not kept alongside." All five modules are still present and still structurally load-bearing —
   `massbattle ↔ units` is one of the three import cycles and both are cut-vertices.

## Measurement defects found in the instruments

Recorded because §0.1 point 5 asks for pattern defects to be named, not just worked around.

- **Mode C ("notional edges") is uninformative at L1.** It reports 13,707 of 14,062 cite-edges —
  **97.5%** — as notional. The cause is disclosed in the register's own Direction disclosure: L1
  widens the *cite* graph only and leaves the throughline/mu/key metadata graphs at L0 scope, so a
  near-total "notional" reading is guaranteed by construction. The top targets are ubiquitous common
  nouns (`Crown`, `Standing`, `Hafenmark`, `Church`) all at identical cite weight 183. **The register
  discloses the cause and does not connect it to the number.**
- **The VALIDATED (2/3) verdict does not strictly apply at L1.** The register states it: thresholds
  were calibrated on L0 and are "NOT re-validated for the L1 corpus."
- **Mode D hit its traversal cap on 58,860 calls** — self-flagged; cascade-sinks are leads, not
  findings.
- **The TF-IDF supporting graph is inert.** Run once without `scikit-learn` and once with it: the
  weakness register, all 8 diagnostic modes, and the P1/P2/P3 verdict are **byte-identical**. The
  only difference is a `tfidf` block in `data/degrees.json` (261 tokens move from 0 to real values)
  that nothing downstream consumes. Two consequences: (a) "multi-graph triangulation" is cite +
  metadata in practice, not three-graph; (b) **without sklearn the run records tfidf degrees as
  all-zero rather than absent**, so a reader of `degrees.json` cannot distinguish "not computed" from
  "genuinely zero." The committed `data/` here is from the sklearn-present run.
- **`stubs.count` 24/25 is red by construction.** `registers/review_baseline.yaml` seeds the baseline
  at a *ceiling* (24 measured + 1 for an unconverted MB file) and documents that intent, but
  `review_core` compares for equality. The signal cannot go green through any IN action.

## Coverage disclosure

L1 traces **199 design docs = 42.8% of the repo's 465 `.md`** — `systems/ engine/ canon/ godot/
proposals/`. Excludes `workplans/`, `tests/`, audit prose, and all non-`.md` (so no sim `.py`,
no engine params). A green result here is not whole-repo coverage.

## Files

| File | Contents |
|---|---|
| `02_weakness_register.md` | Tool output — 8 diagnostic modes |
| `03_validation_report.md` | Tool output — P1/P2/P3 |
| `05_gm_resolution_register.md` | **The deliverable.** Populates `videogame_mode_spec.md` §3 |
| `data/` | Vector-audit graphs + `gm_occurrences_raw.txt` (the 84-row grep capture) |
| `structure_audit/` | G_code + L2 architecture layers |

**No source design doc was edited by this audit.** Every disposition in
`05_gm_resolution_register.md` is PROPOSED.
