# Crawler Delta — mechanic_audit vs. other instruments (2026-07-13 multi-agent run)

**Logged after:** mechanic_audit (just completed, 7 subsystems: architecture, faction_political,
fieldwork_investigation, mass_battle, personal_combat, settlement_territory, social_contest).

**`find` at time of writing** showed content already present under:
- `mechanic_audit/` (all 7 subsystem folders, 5 files each — the audit whose delta this is)
- `module_adjudicator/` — `verdict_full_graph.md`, `module_map_flat.md`, `module_flowchart.mermaid`,
  `state_graph.mermaid` (full-graph pass, already finished)
- `vector_audit/00_status.md` (a status/blocked report, no findings — already finished)
- `compliance_check/raw_output.txt` (two-line CI-mode pass, no per-file detail — already finished)

All four instrument directories had content, so all three other instruments were checked. Below are
concrete cross-references, not vague correlation claims; each cites file+section on both sides.

---

## 1. Convergent evidence: mass_battle has a cluster of independent P1 provenance defects

Two mechanic_audit P1s and one module_adjudicator P1 all land on **mass_battle**, in the same run,
each discovered via a different check angle. None cite the same file, but all three are the same
*class* of defect — a false or broken provenance claim inside mass_battle's canon surface:

- **mechanic_audit G1** (`mechanic_audit/mass_battle/gap_register_update.md` row G1): two
  contradictory Ranged/Volley DR tables in `params/mass_combat.md` (PP-104 vs PP-188), ~2x apart at
  Heavy armor, neither marked superseded.
- **mechanic_audit G2** (same file, row G2): `mass_battle_v30.md` §A.14 "Woven units — brittleness"
  cites a compilation pass on `stage5_clocks.md` — a file that does not exist anywhere in the repo.
  Self-flagged in-doc `[EDGE-06 — P1]` but never filed as an ED.
- **module_adjudicator P1-A** (`module_adjudicator/verdict_full_graph.md` lines 24-27): `mass_battle`'s
  contract emits `scene_outcome.battle_concluded`, mislabeled "substrate §8.5 verbatim" — canon §8.5
  actually writes `scene.battle_concluded`; `scene_outcome` is only the *family name*. A fabricated
  type-string with a false provenance citation.

Read together: in this single run, mass_battle independently accumulated three separate P1-grade
"claims a source/reference that isn't real" defects — one in the params table, one in the design-doc
prose (dead file pointer), one in the module contract (mislabeled canon citation). No other subsystem
in mechanic_audit's output shows this density of provenance-integrity failures. This is worth flagging
to the synthesis pass as a pattern, not three unrelated one-offs: mass_battle's canon surface has a
recurring habit of asserting false pedigree for its own claims.

---

## 2. Convergent evidence: personal_combat Health formula — mechanic_audit's stale-doc finding is
   independently confirmed by module_adjudicator's citation

- **mechanic_audit GAP-PC-4** (`mechanic_audit/personal_combat/gap_register_update.md` row GAP-PC-4,
  detailed in `formula_audit.md` A3.1): `params/core.md:158`'s Health row uses the pre-D-A formula and
  is ~7% numerically drifted from both `designs/scene/derived_stats_v30.md:55-72` **§4.1** and the live
  `combatant.py:35-42`.
- **module_adjudicator** (`module_adjudicator/module_map_flat.md` line 247, derivations table row 7 /
  `verdict_full_graph.md` line 93 personal_combat CONFORMANT note): independently, and for an unrelated
  purpose (F1 write-legality check on the `Health` derived_value), cites the *exact same* authority —
  `r2_consequence_wounds.health_full = WI*(MaxWounds+1)+0.25*Str*End, minus accrued damage (ED-1041 /
  derived_stats_v30 §4.1)` — as the correct, canon-current Health formula.

This is genuine convergent evidence, not coincidence: two instruments, working from different corpora
(mechanic_audit read `params/core.md` + `derived_stats_v30.md` + `combatant.py`; module_adjudicator read
only `references/module_contracts.yaml`'s citation trail) independently anchor on `derived_stats_v30
§4.1` / ED-1041 as *the* authoritative Health formula. That strengthens mechanic_audit's GAP-PC-4 call
that `params/core.md` is the drifted outlier, not derived_stats_v30 — worth citing both sources together
if GAP-PC-4 is escalated past its current P2/no-ED disposition.

---

## 3. Convergent pattern: personal_combat's recurring "declared-but-dead" defect class

mechanic_audit found two internal-doc instances and module_adjudicator independently found a third,
structurally different instance, all within personal_combat:

- **GAP-PC-1** (`ability_armature.md` §2c/§7, `REARCHITECTURE_v1.md`): `reopen`/`disengage` lever named
  across 3 docs, never built.
- **GAP-PC-2** (`ability_armature.md` lines 47/53/169): `seize` lever is dead (cut 2026-06-05, verified
  ablation ~0), but §7 "Current state" still lists `vorschlag`/`sen_no_sen` as live abilities with "a
  positive, bounded edge" — an internal doc self-contradiction.
- **module_adjudicator A4** (`verdict_full_graph.md` line 93 / `module_map_flat.md` lines 449, 451, and
  §5 "orphan emissions"): `scene.combat_felled` and `scene.combat_resolved` are registry-declared
  personal_combat emits with **zero consumers** wired anywhere in the module graph ("registry-declared-
  but-unwired, tracked gap_note").

Three independent findings, two from the doc-prose side (mechanic_audit Mode D) and one from the
Key-contract wiring side (module_adjudicator's A4 orphan check), converge on the same subsystem-level
theme: personal_combat has multiple named-but-functionally-inert surfaces (an ability lever, two named
abilities that no-op, and two emitted-but-unconsumed outcome types). None of these individually rise to
P1 in either instrument's severity scheme, but the volume and cross-angle agreement suggests
personal_combat's "declared capability" surface has drifted further from its "actually live" surface
than either audit alone would suggest. Worth flagging to synthesis as a subsystem-level trend, since a
reader of `ability_armature.md §7` ("Current state") or `module_contracts.yaml`'s personal_combat entry
in isolation would not see the other instrument's half of the picture.

---

## 4. No cross-reference found: architecture Mode D findings (GAP-D1..D7) vs. module_adjudicator

Checked whether mechanic_audit's architecture-subsystem gap findings
(`mechanic_audit/architecture/gap_register_update.md`) line up with module_adjudicator's per-module
transition checks (J2 pass). They do not overlap in a checkable way, and that absence is itself worth
noting:

- **GAP-D3** (P1): `scale_transitions_v30.md` §3.3 "Personal → Scene (Contest)" is an empty Handoff
  Rule — no trigger, no effect, no editorial stub marker (unlike sibling §3.4/§3.6, fixed via ED-748).
- module_adjudicator's J2 transition-semantics pass (`verdict_full_graph.md` line 129) confirms every
  module that *does* declare a `transitions[]` citation points to real payload-carrying content (§3.4,
  §3.5/3.6, §3.1, §3.9, §12.3 — social_contest cites §3.4, not §3.3; personal_combat cites §3.4/§12.3,
  not §3.3). **No module contract currently cites §3.3 at all**, so J2's citation-fitness check never
  touches the empty section — it has nothing to check.

This means GAP-D3's hole is invisible to module_adjudicator's method by construction: J2 only validates
citations that exist, not the completeness of the promised-but-uncited Eight-Handoff-Rules taxonomy
itself. Flag for synthesis: this is a genuine blind spot at the seam between the two instruments, not
a disagreement — mechanic_audit is the only one of the two capable of catching an empty, never-cited
canonical section.

**GAP-D4/GAP-D5** (P1/P2, the residual "GM adjudication"/"GM recognises"/"GM use" language in
`scale_transitions_v30.md` §1/§3.2 and `player_agency_v30.md` §7.1) has no module_adjudicator
counterpart — that instrument checks Key-flow wiring, not prose-level no-GM-invariant compliance — so
no cross-reference exists here either. Noting the absence rather than inventing one.

---

## 5. vector_audit is BLOCKED — a real, named blind spot for exactly the defect class mechanic_audit
   is finding manually

`vector_audit/00_status.md` confirms (verified directly, not taken on faith) that
`scripts/vector_audit.py`'s Stage 1-7 dispatcher is unimplemented and the last real run
(`archives/audit/2026-04-29-topographic-analysis/`) is 304 files stale as of today. No vector-audit
findings exist to cross-reference. But the *kind* of defect mechanic_audit is catching by hand this run
is exactly what a working citation-graph/TF-IDF pipeline (vector_audit Stage 6 diagnostic modes) exists
to catch systematically across the whole corpus:

- **mechanic_audit G6** (`mechanic_audit/mass_battle/gap_register_update.md` row G6): `mass_battle_v30.md`
  cites a nonexistent `derived_stats_v1` at ~5 sites (current file is `derived_stats_v30.md`) — a stale
  cross-doc citation string, already independently caught once before by the 2026-07-08 batch_09 term
  sweep and now re-confirmed.
- **mechanic_audit GAP-D4/D5**: the "GM adjudication" language pattern was fixed once in
  `player_agency_v30.md` §4.2 (ED-WR-0007) but survives in two more locations across two files
  (`scale_transitions_v30.md` §1/§3.2, `player_agency_v30.md` §7.1) — a corpus-wide terminology-drift
  pattern that a citation/vocabulary graph is precisely built to surface exhaustively rather than by
  spot-check.

Both are hand-found, one-subsystem-at-a-time hits of a defect class (stale citation strings, drifted
terminology) that vector_audit's blocked pipeline would otherwise sweep corpus-wide. Flag for synthesis:
until the Stage 1-7 dispatcher is implemented, mechanic_audit's per-subsystem Mode D pass is the *only*
detector for this class running in this multi-agent audit, and it only covers the 7 subsystems in scope
this run — there is no corpus-wide backstop.

---

## 6. compliance_check produced no per-file output to cross-reference

`compliance_check/raw_output.txt` is two lines: `[COMPLIANCE] CI mode — checking local repo state` /
`[COMPLIANCE ✓] All files within thresholds`. No file-level size/atomization detail was written, so
there is nothing to check mechanic_audit's flagged docs against (e.g., whether `ability_armature.md` —
which mechanic_audit found carries two different stale/self-contradicting status banners, GAP-PC-2 and
GAP-PC-3 — is also large/atomization-flagged). If compliance_check's synthesis-facing output later gains
per-file detail, `ability_armature.md`, `scale_transitions_v30.md`, and `mass_battle_v30.md` (each
carrying multiple independently-confirmed structural defects this run) are the three worth checking
first.

---

## Summary for synthesis

- **Strongest cross-instrument signal:** mass_battle (§1) — 3 independent P1s, same defect class, same
  module, different files/layers.
- **Strongest confirming signal:** personal_combat Health formula (§2) — module_adjudicator's citation
  trail independently corroborates which formula is canonical, backing mechanic_audit's stale-doc call.
- **Strongest pattern signal:** personal_combat "declared but dead" (§3) — 3 separate instances across
  2 instruments in 1 subsystem.
- **Coverage gaps to carry forward:** GAP-D3 is invisible to module_adjudicator's J2 method by
  construction (§4); vector_audit's blocked pipeline leaves stale-citation/terminology-drift detection
  entirely to mechanic_audit's manual per-subsystem sweep, uncovered corpus-wide (§5); compliance_check
  gives synthesis nothing to check file-size claims against yet (§6).
