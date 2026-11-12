# VERBS · PHYSICAL · B — the field and the ruin: `march`, `raze`

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Parts 3–4; `U5b_VERBS_military_physical_residue.md`) — **the land ruling (A-57, A-58) and Layer 1 folded.** (1) B1's `march_defender` answered `None` without a war, and B1 had `sides_of` read it; under A-58 a casus belli is not a precondition and a march in force onto land another holds is itself the aggression. The reader is split (residue §2): `field_defender` (who defends this ground against this seat: the holder, unless he is the marcher's own or has given leave; no war test), which `sides_of` and the title tail both read, and the stamp `fields_in_reach`, which keeps "a war he knows of" as the occasion on which a person thinks of marching. (2) "What it does not do: … title on a won field" is decided: an aggressor's `Won` on land another holds passes the land and its seats (`U5d_FA_land_and_seats_pass_on_a_won_march.md`; which end state that is: `26_MASS_BATTLE_aggression_and_land.md`); a draw or a defender's win passes nothing. (3) B2's licence (`occupying_faction`) is false for a town the victor now holds, so `raze` gains one arm, the taker's (residue §3, an ASSUMPTION with its two options); `seize` keeps its Record half, unheld land and a held place entered unopposed. (4) **Layer 1**: `raze` writes different cells by band, so it declares `contests: "a task"`; the roster keeps one name, `graded_tasks` (the `graded_routes` rename is dropped); the pool is the one pool rule on the commander's `command` score, with the army's size as levels and the town's fabric as an obstacle term, never `pool_from: mustered_headcount` (residue §1). (5) Consent, relief and pursuit are classed in residue §2's table, from U5d's decisions 5 and 6.

## Status: PROPOSED

Folded: 2026-11-12 by `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` (row R-10), on Jordan's rulings A-57 and A-58 (`unified/DECISIONS_ANSWERED.md:69`, `:71`). Nothing here is deleted. (1) **"It does not decide title on a won field" is overtaken**: on a march in force onto land another faction holds, an aggressor's win passes the land and its seats in the field's own fold; a draw or a defender's win leaves the defender holding; ground nobody holds is outside the rule. The write is `U5d_FA_land_and_seats_pass_on_a_won_march.md`'s; which end states count as the win is `26_MASS_BATTLE_aggression_and_land.md` §2. (2) **B1 and "not a precondition"**: A-58 reads the aggression from the act, and a casus belli is context, not a precondition. B1's `fields_in_reach` (a person forms `march` on places of those he knows he is at war with) is a rule of formation and keeps it bounded; it is not a precondition of the act (`requires_typed` is unchanged, as this file says), so it stands. What is owed beside it is FA's: `sides_of` fielding the holder when the two are not yet at war, and the fold leaving them at war (`26_MASS_BATTLE_aggression_and_land.md` §5). (3) **`march_defender` and a third party's land**: B1 forms a field against a non-holder only on the marcher's own land. Under A-58 a win after an unasked march onto a third party's land would pass that land; no such field can form today, and the case is recorded, not built (same file §3). (4) The payload fan of `posture` is unchanged: A-58 withdrew the declared purpose, so no `purpose` key joins it. (5) Deployment: an army facing missile troops starts a missile range apart (`26_MASS_BATTLE_cell_scale_and_time.md` §2); nothing in B1 moves.

Batch P-B of `audits/14_VERBS_PHYSICAL.md` §10.3. Carries that file's §5, §6 and §0.6. Lands after
CR-91 (a WAR Proposition exists), FA-B1 (`06_FA_war_lives_in_seats_B.md`), FA-P2
(`06_FA_remit_grant_by_row.md`) and MB's `04_MB_headcount_grade_and_scale.md` (gate 2: a field verdict
varies by seed). B1's formation half may land before CR-91 as a declared honest zero. Reference only
(CLAUDE.md §0.05). Authored by Opus completing a Fable lane cut off by the usage limit (2026-11-12).

## What it changes in `engine/season/` at runtime

1. `march` forms only on a `Field`: a settlement or territory the commander knows of, held by a faction
   at war with his seat's faction, or his own faction's place where an enemy is mustered (B1). In every
   war-less world `march` stops forming (realm: 26 formations to 0). This is declared.
2. `sides_of`'s inline kind and holder read moves to one `world_q` owner.
3. `raze` forms only on a town its seat's faction occupies. It is resolved by a draw over four
   graded outcomes, sacks stores and ends the town's Sites on its better bands (B2).

Declared movers: every realm pin with a `march` or `raze` formation (all of them at seed 0), and
`test_in12_raze.py`'s H-228 pin (it reddens by design).

## The problem (evidence)

`aperture 2 0`: `march` formed 26, attempted 13, 3 unopposed arrivals, 10 refused at ENCOUNTER on the
target's kind, 0 fields. `raze` formed 26, attempted 14, refused 14 of 14 post-admission (no
occupation). The row's own REM-27 note: at `troops=weight` the stronger force routs on contact (a
deterministic field).

## The resolution, decided

Audit §5.3 and §6.3.

## Exact edits, by owner

### B1 — `march`

| file (owner) | edit |
|---|---|
| `engine/season/queries/world_q.py` | *(Reconciled, A-58: this reader is split. `field_defender(w, via, rung)` drops the two `at_war` tests on the holder and adds the leave test, and is what `sides_of` reads; the war test moves to the stamp in the next row. `U5b_VERBS_military_physical_residue.md` §2 has the exact text. The author's row follows.)* add `march_defender(w, via, rung) -> Optional[str]`: `None` unless `w.rungs[rung].kind in MARCH_TARGET_KINDS`. Let `mine = faction of via` (`seat_faction`). If `holder_faction_of(w, rung)` is a faction `f != mine` with `at_war(w, mine, f)`, return `f`. If the holder is `mine` and an enemy faction `e` (`at_war`) is `mustered` there, return `e`. Otherwise `None`. **The one owner of "is this a field for this seat, and against whom."** |
| same | add stamp term `fields_in_reach(w, p)`: Rungs among `p`'s ledger names (`ledger_names`, `places_named`' knowledge rule) for which some live `hold` of `p` on a seat granting `MUSTER_ACT` gets a non-`None` `march_defender`, and the war is one `p` knows of (the knowledge test of `enemies_heard`, factored out into `_wars_known(w, p)` and shared by both). Stamped under `Field`. |
| `engine/season/rosters.yaml: referent_classes` | `values` gains `Field`. `occasion_only_classes` gains `Field`. Note: *"a Rung on which a seat of the asker may march (`world_q.march_defender`); occasion-only, so `places_named` never reaches `march`"*. |
| `engine/season/data/verbs.py` | `FIELD_CLASS = "Field"` beside `DETAINEE_CLASS` and `ENEMY_CLASS` (`:1937-1949`). `RUNG_REMIT_ACTS` loses `dispatch` (derived; `march` no longer declares `Rung`). That reverses REM-27's derived widening of `larders_in_purview`, and it is declared. |
| `engine/season/verb_table.yaml`, row `march` | `referent_class: Field`. `referent_class_note`: replace with *"14_VERBS_PHYSICAL_B B1: FORMED ONLY ON A `Field` (`world_q.fields_in_reach`, the same `march_defender` `sides_of` reads). A war-less world forms none (ED-IN-0337). REM-27's measured `fields_named` was unearned because `places_named` stamped the same Rungs under `Rung`; an occasion-only class removes that route. [ASSUMPTION; medium; revert: `referent_class: Rung` and REM-27's note]."* `requires_typed` is unchanged (a hand-built act still needs a Rung). |
| `engine/season/loop/sides.py::sides_of` (`:97-115`) | the `mass_battle` branch: `subject = march_defender(w, a.via, target)`. The army is mustered as today, and `claimants = []` when `w.rungs[target].kind` is outside the roster, through `march_defender`'s own first test (exposed as `is_field_kind(w, rung)` in `world_q`). Delete the inline kind check and its disclosure comment, replaced by one line citing the owner. |
| `engine/season/decision/options.py` | `march` forms one Candidate per `march_postures` value carrying `posture`, on `vocation_sourced`'s shape (`rosters.yaml: payload_sourced: {march: posture}` is a new roster line, read where `VOCATION_SOURCED` is). A withheld posture is not formed. |

### B2 — `raze`

| file | edit |
|---|---|
| `loop/effects_shared.py:149` -> `queries/world_q.py` | move `occupying_faction` verbatim. `effects_shared` imports and re-exports it (`_seize_rung` unchanged). |
| `queries/world_q.py` | stamp term `towns_occupied(w, p)`: `RAZE_TARGET_KINDS` Rungs for which some seat `s` of `p` granting `MUSTER_ACT` has `occupying_faction(w, s, rid)` not `None` and `mustered(w, rid, that faction)`. Stamped under the new occasion-only class `Occupied` (roster and `data/verbs.py` as for `Field`). |
| `rosters.yaml: graded_inquiries` | rename the key to `graded_routes` (the loader `data/rosters.py`, `manifest/registry.py::check_graded_inquiries` renamed `check_graded_routes`; existing rows byte-identical). Add the row `raze`, routed to the same provider and role as the inquiries. Pool: `seam/wrappers/sigma.py::faculty`'s fallback replaced, for this row only through the row's declared `pool_from: mustered_headcount` key `[a new route-row key; the alternative is the swept `pool_default`, which would make the army's size irrelevant to the draw, rejected]`. Obstacle: `obstacle_default` plus the town's Site count, a modifier named in SC's modifier list. |
| `verb_table.yaml`, row `raze` | `referent_class: Occupied` with a note. `writes:` becomes degree-keyed: `Overwhelming` and `Success`: `["Rung.stores", "Rung.stores", "Site.exists", "Rung.exists"]`. `Partial`: `["Rung.stores", "Rung.stores", "Site.condition"]`. `Failure`: `[]`. `emits:` `Overwhelming`/`Success`: `["rung.razed", "site.razed"]`; `Partial`: `["site.damaged"]`; `Failure`: `["raze.resisted"]`. `emits_on_refusal: ["raze.refused"]`. `writes_note`: the cascade on `Rung.exists` is Layer 1 §B.8's, unchanged. `Site.exists` is the act's own declared write on Sites whose `rung` is the subject, not the cascade. `[UNVERIFIED: the `(Site, exists)` matrix row's step and admitting stratum were not read; the loader refuses the row at load if they do not admit it, and then a `write_matrix.yaml` cell is a named prerequisite]`. |
| `loop/effects_founding.py::_eff_raze` | the licence is `towns_occupied`' pair (one owner). By band: move `raze_sack_share[band]` of the Rung's `stores` to the exercised seat's rung (`_shift`, `requisition`'s two-sided shape). On Success and better, end each Site naming the Rung, then delete the Rung as today. On Partial, lower each Site's `condition` by `loop/effects_economy.py::_fall` (`sabotage`'s formula). `raze.resisted` is earned by the Rung on Failure (written nothing; `contest.undecided`'s shape, an emitted kind with no write). |
| `data/fixtures.py` | `raze_sack_share: {Overwhelming: 1.0, Success: 0.5, Partial: 0.25}`, swept, `[ASSUMPTION; medium]`. |
| `data/verbs.py::KIND_VERB` | `raze.resisted` and `site.razed` map to `raze` (one emitter each). `site.damaged` already maps to `sabotage`; a second emitter makes it unmapped, which is lawful (it is the kind, not the verb, that witnesses read) `[verify the map's rule at landing]`. |

### Order of landing

B2's move of `occupying_faction` first (no behaviour). Then B1 (formation, `sides_of`). Then B2's
class, then B2's grading. MB's gate 2 must be green before B1's war-world gate is quoted as a field.

## Gate (execution artifacts)

Audit §5.7 and §6.7, including both draw assertions (a field verdict that varies by seed; at least two
raze bands over seeds 0-29). `aperture 2 0` before and after: `march` and `raze` formations 26 to 0 in
the war-less realm. Every remaining refusal reason is named.

## Falsifier

Restore `referent_class: Rung` on `march` (wrong-kind formations return). Drop `Occupied` on `raze`
(unoccupied formations return). A field that holds one verdict for one pair over 30 seeds means the
field is still deterministic, and B is not done.

## What it does not do

*(Reconciled: decided by A-57 and A-58; carried by `U5d_FA_land_and_seats_pass_on_a_won_march.md`.)* ~~It does not decide title on a won field (audit §10.4 D-2, carried by FA-B1).~~ It does not re-home the
displaced (Layer 1 §B.8, H-228's ladder). It does not build armies (MB, MILITARY) or the war
Proposition (CR-91).

## NERS reading

- **N.** Force changes the map only through these two. Audit §5.9 and §6.9.
- **R.** Targets, postures and the choice to ruin are strategic. Fields and ruins go either way.
- **S.** One owner per licence for formation and fold. One graded route for inquiries and razing.
  `sides_of` stops carrying a verb rule.
- **E (last).** Two readers, two classes, one renamed key, one graded row, against two verbs that
  today only waste formations. High.

## Cost class

Build: two readers, two stamps, two classes, a route row, an effect rewrite of `_eff_raze`'s tail, one
fixture. Declared re-records.
