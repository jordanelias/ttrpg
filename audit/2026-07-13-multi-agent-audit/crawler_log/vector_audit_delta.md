# Crawler-log delta — vector_audit (2026-07-13 multi-agent audit)

**Instrument just completed:** vector_audit — BLOCKED (stub, no run produced; see
`designs/audit/2026-07-13-multi-agent-audit/vector_audit/00_status.md`).

**What existed at cross-reference time** (`find designs/audit/2026-07-13-multi-agent-audit -type f`):
- `vector_audit/00_status.md` — this instrument's own status-only output.
- `module_adjudicator/` — 4 files, complete (`module_flowchart.mermaid`, `state_graph.mermaid`,
  `module_map_flat.md`, `verdict_full_graph.md`). **Read in full.**
- `compliance_check/raw_output.txt` — complete, 3 lines: `[COMPLIANCE] CI mode`, `[COMPLIANCE ✓] All
  files within thresholds`, done. **Read in full.** No violations were reported, so there is nothing
  to cross-reference against a size/atomization finding this round — noted explicitly per the brief's
  instruction to say so plainly rather than invent a connection.
- `mechanic_audit/` — 6 subsystem folders each with 5 files (`formula_audit.md`,
  `mechanic_dependency_graph.md`, `core_principles_audit.md`, `number_systems_audit.md`,
  `gap_register_update.md`) for `settlement_territory`, `personal_combat`, `mass_battle`,
  `social_contest`, `faction_political`, `fieldwork_investigation`. **Read all 6 `gap_register_update.md`
  files in full**; spot-checked `formula_audit.md`/`core_principles_audit.md` via grep for direct
  cross-hits (`conviction_track`, `scene_outcome.battle_concluded`, `Fort Level`, `domain_actions`).

Since vector_audit itself produced no analytic content (confirmed stub, per its own report), there is
nothing from vector_audit's *output* to cross-reference — no cite-graph findings, no vocabulary-drift
list, no P1/P2/P3 structural-property results exist this run. What follows is (a) what vector_audit's
absence leaves uncovered that the other two finished instruments' actual output reveals as gaps of
exactly the kind vector_audit exists to catch, and (b) one genuine convergent/contradictory finding
pair between module_adjudicator and mechanic_audit that a working vector_audit pass would likely have
surfaced as a cite-graph inconsistency on its own.

---

## 1. Convergent evidence: settlement_layer Fort Level — module_adjudicator's derivation graph
silently encodes a variable mechanic_audit proved undefined

- **module_adjudicator** (`module_adjudicator/verdict_full_graph.md` §4.4 Derivations, row
  "Defense, Fort Level → Garrison Strength") and `module_map_flat.md` §2 (node `d2_s`/`d2_t`) both
  cite the formula `Garrison Strength = Defense × 20 + Fort × 30` from `settlement_layer_v30 §1.3`,
  and the graph verdict reports **A10/A11 gate/derivation integrity at 100%, zero violations** for
  this derivation.
- **mechanic_audit** (`mechanic_audit/settlement_territory/gap_register_update.md`, GAP-02, filed
  **P1**) independently read the same section and found that "Fort Level" as used in this exact
  formula is a **province-granularity value (one per T1–T17)** with **no rule mapping it onto a
  province's 1–3 constituent settlements** post the PP-726 two-tier split — i.e. the input variable
  the formula consumes is not actually defined at the granularity the formula operates at.
- **Cross-reference:** module_adjudicator's contract-level A10/A11 check is necessarily syntactic
  (does a derivation cite a source field that exists?) and cannot detect a granularity mismatch
  between a province-scoped field and a settlement-scoped formula — so it correctly reports "zero
  violations" while mechanic_audit's prose-level read catches a real P1 defect in the same formula.
  This is exactly the kind of gap a working `vector_audit` topographic pass (which builds a term/
  cite graph across granularity boundaries, per its `PILOT_TOKENS`/`SEED_TOKENS` design intent) would
  be positioned to flag structurally rather than requiring a subsystem-scoped mechanic audit to catch
  it by hand. **Action implied:** module_adjudicator's derivation-graph verdict for this row should
  not be read as "formula sound" — it only certifies citation existence, not granularity fitness;
  GAP-02 (P1, lane=SE) is the substantive finding.

## 2. Possible contradiction: settlement Prosperity → Treasury/Local-Economy multiplier

- **mechanic_audit** GAP-01 (P1, `settlement_territory/gap_register_update.md`) asserts that
  `settlement_layer_v30.md` states Settlement Prosperity's contribution to **faction Treasury income**
  as **both ×50** (§1.3, "Local Economy") **and ×10** (§1.8, citing `derived_stats §8.1`) "for what
  both passages describe as the same edge" — flagged as an internal formula conflict.
- **module_adjudicator**'s derivation table (`verdict_full_graph.md` §4.4) lists these as **two
  distinct, non-conflicting derivations**: `d1` Prosperity → Local Economy (`×50`, settlement-internal
  stat) and `d6` settlement Prosperity → faction Treasury income (`Σ settlement Prosperity × 10`,
  cross-module to `faction_state`) — and reports the derivation layer as A10/A11-clean with **zero
  violations**.
- **Cross-reference (flag, not resolved here):** either mechanic_audit is right that the doc conflates
  these as one edge (in which case module_adjudicator's clean derivation-graph read is masking the
  defect by treating the doc's two multiplier statements as if they were always cleanly separated
  targets), or module_adjudicator's reading of §1.3/§1.8 as genuinely distinct derivations is correct
  and GAP-01 is a false-positive born of the doc's own ambiguous prose rather than a true formula
  conflict. This is a live tension between the two just-completed instruments' verdicts on the same
  source text (`settlement_layer_v30.md §1.3` vs `§1.8`) that neither instrument itself flags as a
  disagreement with the other — worth the synthesis pass resolving by re-reading §1.3/§1.8 with both
  framings in hand before GAP-01 is filed as lane=SE.

## 3. mass_battle: independently flagged as a hotspot by both finished instruments, different defects

- **module_adjudicator** flags `mass_battle` **NON-CONFORMANT** (P1-A): a fabricated/mislabeled emit
  type `scene_outcome.battle_concluded` that conflates a family name with a type_id (contract defect,
  proposed lane=MB).
- **mechanic_audit** (`mass_battle/gap_register_update.md`) independently flags `mass_battle_v30.md`
  with **two separate P1s**: G1 (contradictory Ranged DR tables, PP-104 vs PP-188) and G2 (an
  orphaned "Woven units — brittleness" fragment citing a nonexistent `stage5_clocks.md`).
- **Cross-reference:** these are three distinct P1 defects (contract-schema, formula-table,
  dangling-reference) converging on the same subsystem doc-set from two structurally different audit
  angles in the same run — none is a duplicate of another, but the subsystem is carrying disproportionate
  P1 volume across instrument types and is a strong candidate for the synthesis pass to treat as one
  consolidated MB-lane remediation batch rather than three independent ED filings landing separately.

## 4. What vector_audit's blocked status leaves uncovered (blind-spot note)

The two finished instruments each independently caught **stale/dead cross-reference** defects of
exactly the kind a corpus-wide citation/vocabulary graph (vector_audit's actual job) would catch
systematically instead of piecemeal, per-subsystem:
- `settlement_territory/gap_register_update.md` GAP-05: `settlement_adjacency_v30.md` still cites
  pre-PP-726 S-IDs (S-011/S-034 now refer to different settlements) — a co-file drift between prose
  and the already-rebuilt `valoria_geography_v30.yaml`.
- `fieldwork_investigation/gap_register_update.md` GAP-4: four citations to a nonexistent
  `stage11 §11.x`, with the live target renumbered under `scale_transitions_v30.md`.
- `mass_battle/gap_register_update.md` G6: ~5 stale `derived_stats_v1` citations (file no longer
  exists; current file is `derived_stats_v30.md`).
- `module_adjudicator/verdict_full_graph.md` P1-B: `piety_track`'s real home doc
  (`designs/personal/conviction_track_v1.md`) is absent from `canonical_sources.yaml` entirely (a
  registry/vocabulary gap, not just a stale pointer).

Each of these was found only because a subsystem-scoped instrument happened to read the specific
section containing the dangling citation. **No subsystem in this run's mechanic_audit slate covers
piety_track/conviction_track_v1, threadwork, npc_behavior, or victory** — exactly the modules
module_adjudicator flags with A6/A8 issues — so the same class of stale-citation or missing-registry-
entry defect plausibly exists uncaught in those modules this run, and only a working vector_audit pass
(or a future mechanic_audit lane on those subsystems) would surface it. This is the concrete,
citable form of "vector_audit's blocked status is a blind spot": it is not hypothetical — the pattern
it would generalize over is already showing up independently, four separate times, in the instruments
that did run.

## 5. No compliance_check cross-reference available

`compliance_check/raw_output.txt` reported a clean pass (`All files within thresholds`) with no
per-file findings, so there is no size/atomization violation to cross-reference against any
mechanic_audit "hard to reason about" or module_adjudicator decomposition flag this round. Stating
this plainly per the task brief rather than manufacturing a connection.

---

**Governance-file discipline:** this delta note is analysis-only, written solely to
`designs/audit/2026-07-13-multi-agent-audit/crawler_log/vector_audit_delta.md`. No writes were made to
`audit_registry.jsonl`, `editorial_ledger*.jsonl`, or `id_reservations.yaml` — those remain reserved
for this run's dedicated sequential registry step, consistent with every instrument's own stated
constraint above.
