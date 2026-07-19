# Crawler-log delta — module_adjudicator (2026-07-13 multi-agent audit)

**Instrument just completed:** module_adjudicator — graph verdict OPEN (22 violations / 61 warnings,
exit 1), three root causes (1 A2 fabricated emit on `mass_battle`, 1 A8 registry gap on `piety_track`,
20 A6 down-seam-cluster violations across 9 modules). Full detail:
`designs/audit/2026-07-13-multi-agent-audit/module_adjudicator/verdict_full_graph.md`.

**What existed at cross-reference time** (`find designs/audit/2026-07-13-multi-agent-audit -type f`):
- `module_adjudicator/` — this instrument's own 4 output files. Read `verdict_full_graph.md` and
  `module_map_flat.md` in full.
- `mechanic_audit/` — 6 subsystem folders (`settlement_territory`, `personal_combat`, `mass_battle`,
  `social_contest`, `faction_political`, `fieldwork_investigation`), 5 files each, all complete. Read
  all 6 `gap_register_update.md` in full; grepped the other 4 file-types per subsystem for
  `outcome`/`conclude`/`emit`/`piety`/`conviction`/`transitions`/`down-seam`/`scale_transitions`/
  `settlement_layer`/`settlement_economy`/`faction_politics`.
- `compliance_check/raw_output.txt` — complete (3 lines, clean PASS, no per-file findings).
- `vector_audit/00_status.md` — complete (BLOCKED/stub, confirmed by direct read).
- `crawler_log/compliance_check_delta.md` and `crawler_log/vector_audit_delta.md` — both already
  written by earlier crawler passes in this run. Read both in full to avoid re-deriving the same
  cross-references; noted below where I defer to them rather than repeating, and where I add something
  neither caught.

Two prior crawler passes already did substantial module_adjudicator↔mechanic_audit cross-referencing
(Fort Level granularity mismatch, the Prosperity ×50/×10 possible contradiction, mass_battle as a
multi-instrument hotspot, and the piety_track/canonical_sources blind-spot note). Rather than repeat
those, this pass focuses on what's new since: (1) an uncaught cross-lane duplication risk on the
piety_track finding specifically, and (2) mechanic_audit evidence that directly corroborates
module_adjudicator's own "intent gate PASSES" read of the P2-A down-seam cluster — neither prior note
surfaced either of these.

---

## 1. NEW — piety_track A8 finding likely overlaps an already-open ticket in a different lane (ED-SC-0003)

- **module_adjudicator** P1-B (`verdict_full_graph.md`): `piety_track`'s real home doc
  (`designs/personal/conviction_track_v1.md`, the personal-scale Conviction-scar canon) is absent from
  `references/canonical_sources.yaml` — only the unrelated territorial `conviction_track_v30.md` is
  registered. Proposed lane: **IN**.
- **mechanic_audit** (`mechanic_audit/social_contest/number_systems_audit.md:22` and
  `mechanic_audit/social_contest/gap_register_update.md:20`, G-6) independently documents "Piety Track"
  as a **name collision between two referents**: the 0–10 debate tracker (sourced to
  `conviction_track_v1.md`, the *same file* module_adjudicator flags as unregistered) and the
  per-territory BG stat (`params/bg/core.md`). This is **already tracked**: `ED-SC-0003`, P0 docket,
  P2 severity, `needs_jordan`, status **open** — filed in the **SC** lane, transitively referenced via
  `scale_transitions_v30.md` §5.4.
- **Cross-reference:** both findings center on the exact same file, `conviction_track_v1.md`, and the
  exact same underlying confusion (two things both called "Piety Track" at different scales, one of
  which has no clean registry footing). module_adjudicator's A8 finding reads as the *contract-registry
  symptom* of the *naming-collision root cause* mechanic_audit already has open under ED-SC-0003. These
  are not verified to be the identical fix (ED-SC-0003 may resolve via renaming one of the two tracks
  rather than registering `conviction_track_v1.md` as-is; module_adjudicator's fix is purely additive
  registration), but they are close enough that filing module_adjudicator's proposed new **IN**-lane ED
  without first checking ED-SC-0003's actual scope risks two lanes (SC and IN) independently resolving
  overlapping halves of one problem, or worse, resolving it in incompatible ways (e.g. ED-SC-0003
  renames/retires `conviction_track_v1.md`'s "Piety Track" label while an IN-lane ED simultaneously
  registers it under that same name). **Recommended action for the synthesis pass:** read ED-SC-0003's
  full ledger entry before filing module_adjudicator's A8 fix; either fold the canonical_sources.yaml
  registration into ED-SC-0003's remediation, or explicitly cross-cite ED-SC-0003 in the new IN-lane
  entry so both stay coordinated rather than colliding.

## 2. NEW — mechanic_audit's doc-consistency reads corroborate module_adjudicator's own "intent gate PASSES" verdict on the P2-A down-seam cluster

module_adjudicator's summary explicitly argues the 20 A6 violations are *not* a missing-mechanism hole
— the couplings are "deliberate/registry-canonical," and the real residual is unpopulated
`transitions[]`/`targets[]` entries (a contract/script gap), not absent design. Two independent
mechanic_audit passes, reading the prose side with no visibility into the contract graph, land on the
same read for two of the nine flagged down-seam modules:

- **`mass_battle` → `scene_slate`:** `mechanic_audit/mass_battle/core_principles_audit.md:9` (Mode B,
  Fail-Forward check) confirms Part D of `mass_battle_v30.md` "mandatory[ly guarantees] every battle
  produces mandatory downstream state change... Part D's mandatory post-battle Scene Slate similarly
  guarantees narrative continuation." That is an independent, doc-only confirmation that the
  `mass_battle → scene_slate` edge is a real, deliberately-authored coupling — one of the exact 9
  modules in module_adjudicator's down-seam cluster (`scene_slate` and `mass_battle` are both
  NON-CONFORMANT in this run).
- **`faction_political` ↔ `settlement_layer`:** `mechanic_audit/faction_political/
  mechanic_dependency_graph.md:5` rates the Legitimacy/Popular-Support coupling from `settlement_layer
  §1.8` into faction Mandate/Strictness as "well-connected, single source of truth... explicitly cited
  everywhere it's consumed," with **no gap flagged**. `settlement_layer` and `faction_politics` are
  both in module_adjudicator's own `nonConformantModules` list for this run.
- **Cross-reference:** neither mechanic_audit pass was looking for contract-graph transitions[] entries
  — they were independently assessing doc-level design coherence — yet both confirm the underlying
  mechanic is real, intentional, and correctly specified in prose for two of the nine flagged modules.
  This strengthens module_adjudicator's own conclusion that the P2-A cluster's fix belongs in the
  contract/script layer (populate `transitions[]` per scale_transitions §12.3, fix the A6 assessor's
  §12.2 exemption blindness) rather than in design authoring — there is no design gap here for the
  synthesis pass to worry about re-opening on these two edges specifically.

## 3. mass_battle's A2 fabricated-emit finding is orthogonal to, and not contradicted by, mechanic_audit's clean GD-1 read

- **module_adjudicator** flags `mass_battle` for a fabricated `scene_outcome.battle_concluded` emit
  (mislabeling canon's actual `scene.battle_concluded`) — a contract-transcription defect.
- **mechanic_audit** (`mass_battle/gap_register_update.md:43`) separately confirms "GD-1 compliance
  (no mass-battle-outcome → game-victory path): confirmed intact, both docs. No action."
- **Cross-reference:** these are compatible, not contradictory — a mislabeled/duplicated emit type name
  does not by itself create a victory-condition leak, and mechanic_audit's GD-1 check was scoped to
  outcome→game_victory paths specifically, not emit-type naming fidelity. Noting this explicitly so the
  synthesis pass doesn't need to re-verify that the A2 fix is safe with respect to GD-1 — it already is,
  independently confirmed.

## 4. settlement_layer — deferring to the prior vector_audit_delta note, flagging only the aggregate count

`crawler_log/vector_audit_delta.md` §§1–2 already did detailed work on `settlement_layer_v30.md`'s
Fort-Level granularity mismatch (GAP-02) and the possible ×50/×10 Prosperity-formula contradiction
(GAP-01) against module_adjudicator's derivation-graph verdict. Not re-derived here. Adding only the
aggregate count from this pass: `settlement_layer` (module) / `settlement_layer_v30.md` (doc) is now
independently flagged by **two** of the three finished instruments — mechanic_audit (4 separate P1
content gaps: GAP-01 through GAP-04, all lane=SE) and module_adjudicator (A6 down-seam
`transitions[]` gap, part of the P2-A cluster, proposed lane=IN) — plus `settlement_economy` also
sitting in module_adjudicator's NON-CONFORMANT list. compliance_check's clean pass means none of this
is a file-size problem; it's a content-and-wiring problem concentrated on one subsystem across two
different audit angles. Worth the synthesis pass treating settlement_layer as a priority remediation
target on volume alone, independent of any single finding's severity.

## 5. compliance_check — nothing new beyond the prior pass

`crawler_log/compliance_check_delta.md` already covers the highest-value compliance cross-reference
available this run: `module_contracts.yaml` sitting at 80% of its token cap while module_adjudicator's
own remediation queue (P1-A/P2-A/P3-A/P3-B, `verdict_full_graph.md` lines 149-153 — the same fixes
referenced in §§1-2 above) stages at least 4-5 more edits into that exact file, compounded by a
severity-classification bug in compliance_check's own CI-mode logic. Confirmed still accurate this
pass; no new compliance-side finding to add.

## 6. vector_audit — still blocked, no new blind-spot beyond the prior note plus one addition

`crawler_log/vector_audit_delta.md` §4 already lists the stale-citation/registry-gap pattern
(`piety_track`'s missing canonical_sources.yaml entry among them) that a working corpus-wide
vector_audit pass would normally catch systematically. One addition from this pass: §1 above (the
Piety Track cross-lane duplication risk between module_adjudicator's A8 finding and mechanic_audit's
open ED-SC-0003) is itself a textbook case of exactly what a vocabulary-collision detector
(vector_audit's Stage 6 diagnostic modes, per its own SKILL.md) exists to catch in one place instead of
two separate instruments each independently finding half the picture from different angles. Concrete,
not hypothetical — it just happened, in this run, between the two instruments that did finish.

---

**Governance-file discipline:** this delta note is analysis-only, written solely to
`designs/audit/2026-07-13-multi-agent-audit/crawler_log/module_adjudicator_delta.md`. No writes were
made to `references/audit_registry.jsonl`, `canon/editorial_ledger*.jsonl`, or
`references/id_reservations.yaml` — those remain reserved for this run's dedicated sequential registry
step, consistent with every instrument's own stated constraint this run.
