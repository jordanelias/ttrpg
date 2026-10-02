# Valoria — Master Workplan v8, part 5: Batch 4 (opens per ruling) · the Jordan queue · what the ladder already answered

## Status: PROPOSED 2026-10-01 — directed by Jordan; adoption on merge (ED-1094). ⚠ HELD BACK, LOUDLY: every item in §J is OPEN and is Jordan's to answer individually. A merge of this plan answers none of them, and no position gated on one becomes buildable because this file merged.
## Reads after `workplans/valoria_master_workplan_v8_part4.md`.
## Grade under `CLAUDE.md` §0.2: `paper`.

---

## B4. BATCH 4 — JORDAN-GATED; ONE SUB-BATCH PER RULING, AS EACH LANDS

**Reading list:** `proposals/2026-09-26-decision-layer-execution-plan/PROPOSAL.md` §3.3–§3.5 (the H-item
deliverables, carried below so that file can be deleted once they land — its own header asks for that);
`proposals/2026-09-20-pursuit-basis-worksheet.yaml`; the DRAFT candidates `candidate_pursuit_cells.md`
and `candidate_affiliation_content.md` in the decision-layer proposal (they ratify nothing);
`engine/season/hole_register.yaml` H-146; `ED-IN-0261`'s 2026-09-28 row.

### The cells commit — `12b` · `12c` · `12d` + H6 + H8 · IN · gate J-1 · `opus`/`opus` · one R6-atomic commit · `[design]`

**Atomic because** `data/verbs.py`'s `_load_projection`/`_load_alignment` bind at module scope and refuse
an unrostered key or an all-zero matrix — a partial landing is an `ImportError`. **In one commit:**
`references/descriptor_registry.yaml` (`conviction_roster` → `pursuit_roster`, 15; `axis_roster`, 7;
each with `count`) behind `tools/export_descriptors.py --check`; `engine/substrate/descriptors.py` and
`data/pursuits.py` names; `rosters.yaml` `pursuit_projection` (15 × 7), `alignment` (every verb × 7),
`role_template_pursuits` **plus an explicit validation step** (its read path does not raise on an
unknown name); `references/npc_registry.yaml` values; `references/names_index.yaml`; **the verb split** —
`FIGHT-RENAME` already landed `fight`, so the split adds `kill`, `wound`, `challenge` → `accept` (`accept`
carries `contests: "the body"`), with `loop/effects_combat.py` registrations; `12b`'s schema half — a
`(Person, conviction)` carrier, its `write_matrix.yaml` row, a `queries/person_q.py` confliction Query
derived and never stored, **with a caller** (if nothing reads confliction yet — build-order 6f, `score`
dotting against the basis — the Query waits for 6f, `ID-13`); `refusal_axis` set only if the ruling says
arm H-146, reading the refusing pole from roster data. Audit the direct readers of
`descriptors.CONVICTIONS` that survive Batch 1 (`npe.py`'s died at `29d`; `conviction.py`'s dies at `29e`). Re-pin
`test_conviction_roster_single_owner.py` and `test_conviction_spread_solver.py` (declared, §7).
**FALSIFIER:** Jordan's faith pair (the devout-Solmund builder and the Einhir dismantler, both high
`faith` — his own worked example in the worksheet) sits outside the 60° bar (`cos ≤ 0.5`) —
`python -m engine.season.harness.conviction_spread` prints `within_60deg`; the loaders raise on a
partial landing; **`resolvable_verbs()`'s new count is derived from `loop/driver.py`'s definition at the
build, never asserted in advance**; the headless hash moves (declared); the three-arm corpus readout
`ED-IN-0261` used is re-run. **E5:** never interleaved with `8`, `9`. **R:** R-05 (+4 rows),
R-06 reason 2, R-08.

**Then, in order (each its own step):**
- **H7** — the faith-pair test as a standing test; if red, the placement is wrong and the fix goes back to
  J-1, not to the code.
- **H3 = `12`'s scar rebuild** — `Person.scar` becomes `{element: count}`; `_scar` and `scar_step` retire;
  at RESOLVE the act calls `observers_for(w, e, mode, everyone)` and increments one count per observer
  per violated pursuit. The violation predicate (`Σ_axis projection·align < 0`, a sign test) is a
  candidate reading recorded for review, not a ruling; whether the actor counts as an observer is a swept
  arm. Retire the `(Person, axis_count)` row or give it the field — **never both**. **FALSIFIER:** counts
  differ between `fan_out_mode` `presence_only` and `all_five`; a scar on a person who did not observe the
  act → fail; a conviction write reachable from a `Failure` band or from WITNESS's token → fail.
  ⚠ `(Person, pursuits)` movement has **no specified trigger anywhere** (H-62) — describe it; do not build
  around it.
- **H9** — crisis reader, threshold 2 only: the weight shift as a `Fixtures` arm, control `0`, swept.
  **FALSIFIER:** fork divergence at the `total` arm rises above the ED-IN-0261 baseline while the control
  arm is unmoved.
- **H10** (gate J-5's C3) — `affiliation_roster` with exporter validation; `Person.conviction: dict`; the
  `incompatible` half-matrix with a loader refusing an unrostered pair; `confliction(p)` derived.
  **FALSIFIER:** two incompatible affiliations at full intensity load, and `confliction` is non-zero.
- **H11** (gate H3, H10, J-5's C4) — H3's mechanism over the affiliation table.
- **`12e`** — H12 (`Person.precedence`) **held on a post-H6 re-measure, not on Jordan** (A-1: the
  precedence band measured a no-op); H13 (crisis threshold 3 on J-5's G-Q6; threshold 1 has **no
  mechanism** anywhere — it stays open, no precedent is forced onto it).
- **6f** — `score` dotting against the new basis (the confliction Query's caller) and 6d's
  `beneficiary:` column, `DONE·UNWIRED` until something produces `orient`. Sequence after H3; no
  separate gate beyond J-1.

### `19b` · U7-disp: `comply` · `evade / defy` · `construe` · IN · gate J-2 · `sonnet`/`opus`

Rows exist, `eligibility: own`, untyped, no predicate; `construe` is `grade: absent`. After `15`/`15c`
(DONE) the cell is `form: own_ledger, of: subject` over a `content:dispensation` claim — `tell`'s form.
Compliance is `writes: []` per the term's own row, so `_eff_comply` may be emission-only and the fold's
write-nothing refusal does not reach it. **Under arm (A)** the three key on the actor's ledger claim and
answer both an `issue`d dispensation and a `dispatch`ed order; **under (B)** `dispatch` gets its own
obey/disobey pair. **COMPLIANCE:** the fold may ask the actor's own ledger through the `PersonInterior`
snapshot the act carries, and no other (`04`'s carve-out). **FALSIFIER:** `comply` evaluable for a
person whose ledger holds no claim of the terms → fail. **R:** R-05 (+3, or +4 with V-1).

### J-3's verbs — `confer` · `establish` · `revoke` reachable from computed play · IN · gate J-3

Built per the option ruled: (i) an `office` operand bound from a question referent of kind Office (needs
a question source about seats — none exists; it would be built here); (ii) read off a held writ/commission
Record (`15c`'s `_from_content_claim` precedent, no new operand name); (iii) withheld from formation.
**FALSIFIER (i)/(ii):** `aperture 4 0` shows each executing ≥ 1 with `Act.via`; a `confer` onto an
already-held office does not deposit a claim about the outgoing holder's Tenure (the re-seating leak
H-71's record names). **R:** R-04, R-05.

### `9` · PC-SURRENDER · PC · gate J-7

If built: Yield (declared in Phase 1; accepted ends the combat, refused leaves the yielder unresisting)
maps onto the seam as a `Margin`/`wound_state` with the loser's outcome — **no fourth band, no fourth
resolver**; say whether a yield maps onto `Untouched`/`Wounded` with the surrender on the result, or the
band roster gains a value, and why. Disengage already exists as emergent behaviour in
`combat_engine_v1/wrapper.py`. Constants go to `config.py`, cited. A PC id-block release precedes any
filing (the PC block is exhausted — administrative). **FALSIFIER:** a planted yield ends the exchange
with zero further rolls (assert the bout count); a yield accepted while the yielder's objective is still
contested in the zone is refused. **E5.** If struck: one ledger row and `ED-PC-0056`'s carry-forward
closed.

### `24g` · the bodies clock + P3 individuation · SE · gate J-6

The live arm of `body_step` (shipped at the control arm `0`; `H-125` swept 0 / 10 / 67). The carrier is
settled (`24f`: cohorts eat, `Person.weight`). P3: CENSUS individuates on a demand kind — a `dispatch` to
a non-existent clerk emits `person.demanded`, and next season a Person exists whose `person.individuated`
cites it. P1's other half — a PERSON-keyed crossing cannot fire the `presence` branch because
`world_q` derives `at` from `w.sites.get(who)`; the repair is `at = parent_of(w, who)` when `who` names a
person. **FALSIFIER:** `Person.weight` or the envelope written by anything but CENSUS/MATTER → fail; a
stored aggregate where a Query is required → fail. **`/code-review` + `/simplify` only** (one number,
with its control arm).

### `24h` P7 · dispensation-as-document · SE/IN · gate J-10

Only if Jordan overturns the written refusal in `verb_table.yaml`'s `comply` typed cell.

### `26` · GO-VERSION · GO · gate J-9

Record the ruled version where code reads it; then ED-1050's deferred module re-export (*"a port never
corrects its oracle in place"*). **Nothing in this repository asserts a version before then.**
**FALSIFIER:** any `.gd` value differing from its `.py` oracle.

---

## J. THE JORDAN QUEUE — survives all five ladder steps; ranked by what each unblocks

Each item went through `CLAUDE.md` §0's ladder (superseded · irrelevant · answered by a design document ·
answered by precedent · answered by what makes sense for the architecture) and survived: two defensible
options lead to materially different games, or the answer would overwrite ratified canon, or it is a
number or content nobody can derive. **Rank = what it unblocks**, most first.

| # | question | options | consequence | unblocks |
|---|---|---|---|---|
| **J-1** | **C1 + C2** — the 105 projection cells (15 pursuits × 7 axes) and the alignment re-cell over every verb (incl. `kill`, `wound`, `fight`, `challenge`, `accept`), **including the faith-pair placement**; and the per-character / role-template migration to the fifteen (four orphans: `Utility`, `Equity`, `Identity`, `Precedent`). Ledger: `ED-IN-0261` (2026-09-28 row, `needs_jordan: true`) | approve/vet the DRAFT `candidate_pursuit_cells.md` (it **fails** the faith pair at the registry's `.60` clergy weight and passes only at `.45`), or supply your own | the cells commit, H3–H11, `12`, `12e`, 6f, H-146 arming, the verb split | **R-05 (+4 rows), R-06 reason 2, R-08** — the only path to R-08 at all |
| **J-3** | **The `office` operand (H-94)** — the realm attempts `confer` 213, `establish` 74, `revoke` 45 times in four seasons and refuses every one, because no computed act names an office and `office` is not one of the closed eight `requires_operands`. Does the vocabulary gain a seat/office operand, and from what source? | (i) a new `office` operand from a question referent of kind Office (needs a question source about seats); (ii) read it off a held writ/commission Record (`15c`'s precedent; no new name); (iii) withhold the three from formation and keep them hand-built only | (i)/(ii): realm governance verbs become reachable — the R-04 strategic layer; (iii): 332 fewer refusals and no realm governance | **R-04, R-05 (3 rows)**; shapes `22`'s `determine` referent (H-163 limit 2 shares the shape) |
| **J-2** | **`ED-IN-0210`** — is `comply` one verb or two? With **V-1** (held back from #445): split `evade / defy` into two rows on the `ED-FI-0009` precedent? | (A) one `comply` keyed on the actor's ledger claim answers both an `issue`d dispensation and a `dispatch`ed order (evidence leans A); (B) `dispatch` gets its own obey/disobey pair; V-1 yes/no | A: one row, one falsifier; B: two more rows; V-1: a witness's claim distinguishes evasion from defiance | **R-05 (+3 or +4)** via `19b` |
| **J-4** | **H-156** — verbs that are always refused still form and win scene slots (`commit`, `found`, `build`, `survey`; same shape `migrate`, `levy`; and `confer`/`establish`/`revoke` in the realm) — 34% of realm acts. ⚠ The realm figure is sized under `remit_default`, a testing fixture | (a) decline person-side until each verb's own gap closes (the `give`/`petition` precedent); (b) accept the cost as shipped; (c) widen preconditions or grade the verbs so the chooser has a reason | (a) restores `release`'s share and empties the realm of failing attempts; (b) R-01/R-02 measure with the tax in; (c) new typed cells per verb | shapes **R-05**'s counts and **R-01**'s scene share; `22` step 11 (`commit` never executes) |
| **J-22** | **`ED-FI-0009` — how does a degree reach the six inquiries, and does a refused inquiry's `finding.none` deposit?** Step 3 ALREADY CLOSED that they are graded ("Claims graded by degree; Failure emits `finding.none` and deposits nothing", RESOLVE → WITNESS, work item 4.5: `workplans/2026-09-06-season-loop-execution-plan.md:647`, a retired plan at fork ref `0671283`; carried at `engine/season/verb_table.yaml:962-969` and `engine/season/requirements.yaml:687-691`). The position hit its own stop condition on the two parts still open: (i) a degree reaches a verb only through `contests:` — the `emits` arm of the loader check (`engine/season/data/verbs.py:589-604`, a check `ED-FI-0009`'s own 2026-09-10 commit added, not ratified Layer 1 text: `04 §B.13 #12` rules on `writes`) refuses a degree-keyed `emits:` with no `contests:`, and `test_season_shape.py::test_we_only_a_verb_that_declares_contests_can_be_graded_today` pins one roll owner — while `engine/season/rosters.yaml:1031-1034` rules that investigation must not be made a contest to become gradeable; (ii) "Failure deposits nothing" is false today of `finding.none` (WITNESS deposits every Event kind, `engine/season/loop/witness.py:380`) — the same unruled question as `H-111` (`engine/season/hole_register.yaml:1608-1618`, "nobody has ruled"). Figures, the producer's scratch probes and NOT committed: at the shipped fixtures (pool 2, obstacle 2) a graded inquiry fails about 73% of draws (the 73% reproduces analytically, P(net < 2) about .74 on the ED-MB-0066 face map) and `finding.made` falls about 80% (headless, three seasons, three seeds; 76% pooled, 62-86% per seed) | (A) graded, as step 3 answered: a declared routing column that is not a prize, the `emits` arm of the loader check accepting it, a WITNESS rule that skips `finding.none` (which also answers H-111), and either `verb_capability` rows first or an accepted ~80% finding cut; (B) ungraded: the six stay flat and R-05 / R-09 say so — this REVERSES the step-3 answer rather than being a neutral default; (C) a prize, which `rosters.yaml:1031-1034` forbids | A: investigation outcomes vary by skill and a season carries far fewer findings; B: step 3's "graded by degree" is struck, findings stay near-certain, a refused inquiry still deposits as news (H-111's running reading), and R-05 "graded, not only executed" stays unmet for six verbs | `ED-FI-0009`; R-05 (graded), R-09 (a third graded chain) |
| **J-13** | **`capability`'s scale and source (H-126/H-127, `assumption`)** — R-09's roll varies by person only where a person has a `capability`; the one authored value (`NPC-088`'s `3`) was a named judgment call. Where do per-person magnitudes come from? | (i) the authored attribute `stats:` in `references/npc_registry.yaml`, through `verb_capability`'s key mapping; (ii) a rank scale you rule; (iii) leave `pool_default` everywhere a case does not name a vocation | (i)/(ii): R-09 varies by person across the corpus; (iii): R-09 varies by person in a handful of cases | **R-09**; `13`-rest's quality; `ED-FI-0009` |
| **J-23** | **`Proposition.predicate` for an authored ought (`H-185`)** — `17b`'s eight-overlay pilot did not raise DISTINCT EXECUTED SETS (41 → 41; control C reproduced `17`'s 41 → 26) because Q4 reads an ought's `subject` only (`queries/world_q.py:1362`); the `predicate` the schema carries is read by no live path. Does an ought's predicate get a reader, or does the schema drop it? | (A) drop `predicate` from `ought:` so it carries only `about`, what Q4 reads; (B) build a reader — a verb × predicate score, a formula and magnitudes you would have to rule; (C) leave it and stop `13`-rest at the pilot | A: one fewer dead field, oughts differ only by referent; B: oughts could differentiate decisions (R-06, R-09) at the cost of a ruled table; C: the corpus stays at eight overlays | **R-06**, **R-09**; `13`-rest at scale |
| **J-11** | **Two of your six scales have no mechanism spec anywhere in code**: grid-based map combat with units (no grid, hex or tile module exists; only quarantined UI documents mention a grid) and character creation / development (nothing creates or develops a person). Are they in scope for the season loop, a separate mode, or later? | in the loop (then a spec is owed); a separate tactical/creation mode outside the season loop; deferred past M1 | decides whether R-04 can ever be `met` on its scale roster | **R-04** conjunct (3); R-05's second clause |
| **J-5** | **C3** the affiliation roster, the ten `incompatible:` cells and intensity; **C4** verb × affiliation engagement; **G-Q6** crisis threshold 3's terminal branch (restabilize, fold or destroyed; per case or fixed) | content; content; per case or fixed | — | H10, H11, H13 (R-06 texture) |
| **J-6** | **`ED-IN-0247` — the `body_step` value** (carrier settled at `24f`) | `0` (control) / `10` / `67` (the H-125 sweep), or another | a realm where dearth kills vs one where it never does | `24g`'s live arm |
| **J-7** | **Position `9`** — build §11.4 Yield/Disengage, or strike it (`ED-PC-0056`) | build (yield as a Margin, no fourth band) / strike | what a duel can end in | `9` |
| **J-8** | **`dispatch` as a remit act** — `offices.yaml`'s remit column (r2 `03`) excludes it; the tree carries it and the realm executes it 2 of 27; `ED-IN-0256` is silent; `remit_default` is "for testing purposes for now" (you, 2026-09-18) | keep it in the per-post remit / delete it per r2 `02` | which seats can `dispatch`; sizes J-4's tax under a real remit | `13d-iii`'s remit half → R-04 |
| **J-9** | **The Godot version**; and **D2**, the tenth attribute (count ruled ten, `ED-IN-0193`) | — | — | `26` → M3 |
| **J-10** | **S5-P7** — overturn the written refusal of dispensation-as-document (`verb_table.yaml`'s `comply` cell) | overturn / keep | overwrites ratified canon either way it is asked | `24h` P7 |
| **J-20** | **The off-hand slot** (`ED-PC-0055`; the retired combat plan v4.1's `⚖6`; the PC proposal's Q9) — `core.COVERAGE_GAP['partial']` is plumbed through `_transmit` and no caller passes it (`systems/combat/combat_engine_v1/core.py:208,401,431`); the roster has no shield, buckler or targe and no slot to hold one, so `main_gauche`, `paired_short` and `hook_sword` are measured in a configuration they were never used in. Is an off-hand in scope for personal combat? | (A) in scope — the proposal's minimum increment: an `offhand` field (default `None`, byte-identical), a buckler through the dead `coverage='partial'` path, a parrying dagger, a paired weapon; (B) out of scope — delete `COVERAGE_GAP['partial']` and the `coverage` parameters, duels stay single-weapon | A: sword-and-buckler and rapier-and-dagger exist and the dead key gets its caller; B: the roster stays single-weapon and the dead branch goes | the off-hand build — `proposals/2026-07-26-personal-combat-player-agency-and-tradition-curriculum.md` §13 (I-3, I-4) |
| **J-21** | **The katana anchor** (`ED-PC-0051`, the 2026-07-29 row, still `needs_jordan: true`; the retired combat plan v4.1's `⚖1b`) — a native cut edge is graded `rel = eff / CUT_REF_NATIVE` (`systems/combat/combat_engine_v1/core.py:480-481`), anchored on the katana at 1.00 (`core.py:344`): above 1.0 a benefit gated on how much the target yields to an edge, below 1.0 a penalty gated on nothing. That asymmetry is the batch's own choice (`core.py:349`); your 2026-07-29 ruling, *"cutters need to be excellent in contexts where they can CUT"* (`core.py:345-346`), does not name it. The two lowest native edges, greatsword (0.80) and hook_sword (0.71), therefore now prefer their point unarmoured (`tests/valoria/golden_element_parity.json`, `select_mode['none']`), which the row itself calls *"questionable feel"* and says *"the anchor choice is Jordan's to confirm or move"*. The v4.1 adversarial pass returned it to you (`registers/handoffs/HANDOFF_PC_history.md:146-147`); retiring that plan did not answer it, and your *"that looks like fiat"* (`registers/editorial_ledger_pc_archive.jsonl:59`) was about replacing a gate with a derivation, not about an anchor's consequence. The module's other anchors sit on the WEAKEST member of a population (`CUT_AUTH_REF`←hook_sword, `THRUST_AUTH_REF`←bear_spear, `PERC_AUTH_REF_SOFT`←the weakest hammer; `core.py:335`, `:378-380`); the katana is not the weakest native cutter (hook_sword, 0.71, is), so it follows that precedent's form and not its rule. | (A) keep the flip as a guarded asymmetry exactly as batched — the katana stays the anchor, greatsword and hook_sword pick their point unarmoured, and `test_a_poor_edge_is_poor_everywhere` (`tests/valoria/test_combat_cut_grading.py:138`) stays the guard; (B) re-anchor — move `CUT_REF_NATIVE` off one weapon onto a reference taken from the native population (its weakest member, as the module's other anchors do, or a mid-population value), so the grade is relative to the field of sixteen; the direction decides what moves (a lower reference ends the flips and lifts every native cutter above it, a higher one adds penalties), and no value has an external criterion | A: no code change; a greatsword that prefers its point unarmoured is the disclosed cost of grading the edges, and no weapon is exempted by name (scripting drift); B: a re-fit of one exported constant (`engine/engine_params/combat_engine_v1.json`) that moves every native cutter's balance — measured as the build, not asserted here | the PC calibration batch: `CUT_REF_NATIVE`'s value, and re-pinning `golden_element_parity.json` and `combat_armour_reference.json` if it moves |
| **J-18** | **The depth support stack** (`ED-MB-0041`, narrowed 2026-10-01) — your 2026-07-24 per-cell directive includes *"damage only being emitted by cells in direct contact"*, but the pool also counts support from the ranks behind the contact row, weighted by depth behind contact: the first rank behind at **1.0, full weight**, then 0.7 and 0.5, and the fourth and **every rank beyond at 0.3, with no cutoff** (`systems/mass_battle/sim/config.py:139-140`; `core/exchange.py:218-219`; `geometry.py:327-328`). Two of your own statements bear on it and neither settles it: the stack is tagged `[canonical: Jordan handoff §(1)]` (`geometry.py:307`), and your 2026-07-23 closing-ranks directive (`MB_CLOSE_RANKS`, `config.py:357`) is how rear troops become contact troops; depth also already earns relief elsewhere (`MB_DEPTH_ROTATE`, `MB_SHOCK_DEPTH_*`, `MB_ENVELOP_DEPTH_RESIST`). It reaches play: a season field is one troops-sized subunit (`massbattle._weighted_unit`, `massbattle.py:202`), so its depth varies with force size (rank counts per size were not measured). Does the directive reach the support stack? | (A) yes — cap support at the ranks a troop type's weapon reaches; depth's value then lives in the relief terms and the refill; (B) no — the stack stays as built (`[canonical: Jordan handoff §(1)]`), and the directive governs where casualties land (`MB_CELL_DAMAGE`), not what counts toward the pool | A: pool from rear ranks past the cap is removed, which changes how a larger season force scales; B: depth keeps adding pool at every size, down to the 0.3 floor | no plan position; it sets how a larger season force scales in `resolve_field`, and it is a prerequisite the squad-engagement synthesis names for per-cell quality (`proposals/2026-09-25-squad-engagement-synthesis.md:141`) |
| **J-16** | **H-173** — should a determination-opened `oblige` (a sentence) read differently from a service `oblige` to renewal, the witness channel, the one-edge rule and the term fixture? | one carrier read the same everywhere / a per-reader distinction (the opening act's verb is already recoverable) | how disposal is felt in play | nothing until `22` makes `determine` execute in a shipped world — **ask then** |
| **J-17** | **H-174** — does a bench's jurisdiction follow where a person IS (`home_of`) or where he LIVES (`residence_of`)? (The upkeep-target half is answered, A-2.) | presence / residence | whose bench binds a traveller | nothing until a `move` crosses two benches' grounds — **ask then** |
| **J-19** | **The cavalry charge recoil — graded by steadiness, or brace-gated?** (`ED-MB-0041`, narrowed 2026-10-01) — a charge is already resisted by steadiness without any brace: its moral shock is graded always-on by discipline and depth, with hold-or-brace as one multiplier of three (`_charge_shock_sigma`, `systems/mass_battle/sim/resolution.py:194-201`), and its puncture is absorbed by the defender's depth (`orchestration.py:1147-1148`). Only the charger's reciprocal recoil (`MB_CHARGE_RECOIL`) fires solely against a defender carrying the literal `brace` instruction, facing the charge, against a cavalry charger whose reach the defender matches or exceeds (`orchestration.py:1234-1242`; `config.py:385-388`). That gate is yours — bracing is prepared, never instantaneous (ED-1095, `config.py:387`), and only a wall that faces the charge repels it (ED-1091, `config.py:385`) — and the code's stated cause is *"a mounted body being pressed onto a hedge of set poles"* (`orchestration.py:1213-1215`). The recoil's size is already steadiness-graded (`_wall_prep`, discipline × depth, `resolution.py:170-174`); only its gate is brace. Should steadiness also grade the recoil, with `brace` a multiplier instead of a gate? The squad-engagement synthesis queued exactly this, unanswered (`proposals/2026-09-25-squad-engagement-synthesis.md:203-204`). | (A) yes — the recoil is graded by steadiness always-on and `brace` multiplies it, as it already does for the shock; (B) no — the recoil stays brace-gated: its cause is set poles, and steadiness already protects through the shock and the puncture | A: an unbraced, disciplined, deep body repels a charge in part, which moves cavalry-versus-infantry outcomes and recasts the cause from set poles to steadiness; B: only a prepared wall costs a charger anything beyond the existing shock and puncture grading | nothing until a season field can field cavalry (`massbattle._weighted_unit` builds one infantry Line subunit, `massbattle.py:159-161`, `:202`) — **ask then** |
| **J-14** | **Narrative #6** — complication as the modal outcome (re-bands the one degree ladder, `degree_from_net`) | — | moves every scale; overwrites a ratified shape | nothing |
| **J-15** | **Held back from #445:** `05 §4.1` (do unwatched fights resolve in one act or span scenes?) and `05 §4.2` (does duel mode open any closed moment? recommended no) | — | — | nothing in this order |

**Not on the queue, and why:**
- **The MB/PC lane rows** the 2026-09-28 roster listed have been through the ladder (`LADDER-MBPC`,
  2026-10-01: a Haiku extract, a Sonnet ladder pass, an Opus check, then a revision on that check). The pass
  is done. Its rows are appended to the lane **`_archive`** ledgers
  (`registers/editorial_ledger_{mb,pc}_archive.jsonl`), not the live ones: an id lives entirely in one file or
  the other (`tests/valoria/test_ledger_hygiene.py::test_no_ed_has_rows_split_between_a_live_ledger_and_its_archive`)
  and these ids' earlier rows are archived. **Closed at a step:** `ED-MB-0039` (step 1, premise overtaken —
  Jordan's C2 ruling left its (A)/(B) fork untouched and is not the ground), `ED-MB-0041`'s envelopment payoff
  and rout band (1), Command σ-ceiling (4, a prior ruling) and yield split (5), `ED-PC-0047` (5),
  `ED-PC-0052` and `0054` (4), `ED-PC-0053` (5). **Decided, build still owed — the row stays `open`,
  `needs_jordan: false`:** `ED-PC-0016` (1), `ED-PC-0049` (5), `ED-PC-0050` (4), `ED-MB-0045`'s 2:1 band, label
  and rename (5 / 4; its emergence verdict is not ruled). **Survived, now §J rows:** `ED-MB-0041`'s depth
  stack (J-18) and charge recoil (J-19), `ED-PC-0055` (J-20), `ED-PC-0051` (J-21).
- **The naming confirmation** Fable proposed (is the new document THE PLAN or the master) is withdrawn:
  Jordan's retire-all ruling removed the reason they were two documents.

---

## A. ANSWERED BY THE LADDER — closed; do not let any ride back onto §J

Each row names the ladder step and the closing citation. Each ratifies only as *which step answers it,
and which candidate gets attacked* — the answer is decided at its position with the code in front of it,
and an attack that lands sends the question back through the ladder, not to Jordan by default.

| # | question | step | answer / where decided |
|---|---|---|---|
| A-1 | the 2026-09-28 plan's §5.2 thirteen demotions | 1–5 | each with its step (content-hash tiebreak → H-54/H-122, step 4; MB golden → `ED-MB-0016`, step 1; held H5 → step 1; H-111 → one probe, step 5; `ED-MB-0075` → option (2), built; `mass_battle` `state: []` → `04 §C.5.1`, step 3; G-Q5 → post-H6 re-measure, step 5; M-7 / `upkeep` / `kill / wound` → contradictions 3 / 1 / 4; `titles` → `04 §B.7/§E.1`, step 3; d.1 → members' `commit` degree, attacked at `20-iv` and dropped (nothing writes a commit Tenure's `degree`, H-162; the morale source landed from stance instead, PR #450), step 5; `test_n3` floors → declared re-pin unless `11` shows a property, step 5; D-6/D-7 → swept fixtures at `18`; deleting the retire set → `requirements.yaml`'s own gate, not a question; GD-1 → a registered gap) |
| A-2 | H-174 item 2 — the upkeep payment's target | 5 | `home_of` is the architecture's own definition of where a person is |
| A-3 | `24f`'s cohort producer | 3 | `engine/season/cohorts.yaml` — built (ED-WR-0011, `npcs.yaml` header, ED-SE-0051) |
| A-4 | R-04 reason 2's "no Faction-as-actor" | 3 | `04_CODE_ARCHITECTURE.md`: `Faction` is a resolved view with **no verbs**, never `Act.actor`; faction acts are person acts `via` seats |
| A-5 | H-163 limit 1 (rungless seats) | 3 | r2 `03`'s four anchor forms → build item `13d-iii` |
| A-6 | `29d`'s gate on `10` | 5 | the retire gate is "the loop expresses the scale"; `npe.py` has no season reader → re-gated on `29b`; the premise was verified and `29d` landed on it (PR #450) |
| A-7 | `thread_read`'s operand (H-85) | 4 | the row's own default, a two-valued `knowledge_kinds` roster (H-128's swept-fixture shape) — `14` ride-along (`R05-THREAD`) |
| A-8 | the "double `@effect_for('oblige')`" in `effects_governance.py` | — | false alarm: the second is docstring text |
| A-9 | `return_to_game_queue.yaml` | 1 | superseded by its own header (2026-08-19); retired at `ebb43bf0` |
| A-10 | GD-1, the victory requirement | 5 | registered as an `ABSENT_RULE` hole, `H-176`, at `28-iii` (PR #450) |
| A-11 | `ms_track` / `knots` deletions | 4 | wait on `27` (the retired plan's §1.3 disposition) |
| A-12 | **former J-12** (does being told something move the hearer's stance?) **and position `10`'s write target** | 1 | superseded by the telling workplan, RATIFIED 2026-10-01 (main §0.6): `tell` writes no stance; told valence enters regard at read (G1); a judged deed counts there too, so this plan's stored `fight`-write rewrite of `10` is withdrawn |
| A-13 | `destroy_record` unformable for everyone | 4 | needs a record-holding question referent — `give`'s shape, at `14` |
| A-14 | v7's ruling R-7 — does the Churn Engine workstream survive `ED-IN-0204`? | 2 | its head lived under the dissolved `designs/` tree; nothing builds on it |
| A-15 | `21` item 3 — reconcile the M1 progress board | 2 | the board was retired at `ebb43bf0`; m1 row 3 now reads THE NINE |
| A-16 | `14`'s antonym rows `waive`, `deposed`, `fray / loosen` | 3 | `04 §A.3` row 14: the closing half is ONE `release` verb, generic over kind; `revoke` takes away. No new closer rows |
| A-17 | what "built out" means for R-05 | 4 | executes in computed play — U7's own acceptance (*"≥ 1 world — in the corpus, not merely in a hand-built `Act`"*) |
| A-18 | must R-01's `met` include a realm reading? | 5 | no — a row is measured where its `measure:` says; the realm is context |
| A-19 | is U6's `probed` divergence a defect or a property? | 5 | a property (a deposit raises a later-round question — R-03's channel), **conditional on P-4**: same-arm divergence makes it a determinism defect |
| A-20 | where `27`'s `rendering.py` stubs write | 5 | not into the overview clocks (no season analogue, ED-WR-0011 option A); a retained or season-native carrier, or struck |
| A-21 | `ED-FI-0009`'s obstacle source | 4 | `sigma.py::_obstacle_of`'s existing non-person default; one roll owner (S27.2) — stop if that needs a `contests:` shape |
| A-22 | who seats `p_b`/`p_c` from the `cast:` — `13` or `17`? | 1 | `13`'s execution record (2026-09-28 plan §8.7) assigned the remainder to `17` |
| A-23 | Fable's proposal to run FI `ED-FI-0009` as a parallel lane | 5 | serial — it shares `verb_table.yaml` and `effects_information.py` with `14` (`_part3` O.3) |
