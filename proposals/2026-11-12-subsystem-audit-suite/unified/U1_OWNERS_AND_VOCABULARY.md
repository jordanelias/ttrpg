# U1 — owners, units and interfaces: the fact-to-owner ledger and the decisions the read lanes passed across

## Status: REFERENCE (a unification-lane ledger; a plan of ordered edits for the wave-3 rewrite lanes and the v12 batches; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: the working tree of `main`, 2026-11-12, plus implementation lane A's two unmerged commits (`e5d6ab9`, `c5bf18a`, read with `git show`). Lane: U1 (Opus), wave 2 of `unified/UNIFICATION_RUN.md`.

Reconciled: 2026-11-12, U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "Ob" → "obstacle" in prose (glossary *obstacle*).

**Inputs read.** `CLAUDE.md`; `UNIFICATION_BRIEF.md`; `unified/UNIFICATION_RUN.md`; `unified/DECISIONS_ANSWERED.md`
(A-1 to A-91, governing); `unified/OWED_TO_UNIFICATION.md`; `unified/U5_CONFLICTS_U5a.md`, `unified/U5_CONFLICTS_U5c.md`;
sections 3 and 4 of `unified/work/R1_READ.md` to `R5_READ.md` in full and their owner, vocabulary and capability rows
by search; the proposals needed to decide an item, opened: `29_DICE_one_opposed_rule_form_and_tuning.md`,
`U5a_capability_home_and_two_inputs.md` (CAP), `U5c_SC_one_obstacle_form.md` (OBS), `05_SC_hearing_capabilities.md`,
`06_FA_decree_binds.md` (edits 1–2), `20_NARRATIVE_E_the_year_and_the_reason.md`, `27_MB_A_command_and_the_obedience_draw.md`
(§1, §2, §5), `07_SE_capability_rate_B.md`, `10_DICE_capability_axiom_map.md` §A–§D, `02_CHAR_scar_cap_and_regard_unit.md`
(head), and the heads of the nine capability proposals. **Tree owners opened** (the read lanes did not):
`references/descriptor_registry.yaml` (whole), `references/names_index.yaml` (whole), `architecture/VOCABULARY.md` (whole),
`engine/season/rosters.yaml` (key list; `verb_capability`, `vocation_attribute`, `endings`, `advantage_sources`,
`combat_degree_bands`, `fight_endings`, `field_degree_bands`, `record_kinds`), `engine/season/verb_table.yaml` (head and the
`argue` row), `engine/season/data/fixtures.py` (by name), `engine/season/state/carriers.py` (`Event`, `Sensation`, `Office`),
`engine/season/seam/wrappers/pool.py`, `engine/season/loop/effects_combat.py::broke_observed`, `engine/substrate/descriptors.py`
(public names), `engine/dice_engine/` (public names), `engine/engine_params/` (file list; `game_constants.json`),
`architecture/meta/04_CODE_ARCHITECTURE.md` §B.7, `architecture/holonic_ARCHITECTURE.md` §9 row, `registers/editorial_ledger_in.jsonl`
row ED-IN-0332, `tools/export_descriptors.py` (validators), `systems/settlements/valoria_geography_v30.yaml` (province keys).

**Division with U3.** This file decides owner, vocabulary, schema, unit and capability items. Where an item is
also a contradiction of fact or an order question, it is decided here and marked **(U3 defers)**. Counts that
disagree (territories 15/16/17, verb rows 67/68, instruments 16/17) are U3's unless a unit decision below settles them.

**Marks used in the ledger.** `T` the owner file and key exist on `main` (opened by this lane); `B` exists only on
lane A's unmerged branch; `P` the file exists and the key is proposed; `P*` the file itself is proposed. Ladder steps
are CLAUDE.md §0's: 1 superseded, 2 irrelevant, 3 a design document or Layer 1, 4 precedent, 5 architecture.
Nothing here edits a proposal, audit, code, canon, registry or ruling; every edit below is an **instruction** for
the wave-3 rewrite lane of the named family or the v12 batch named.

---

## §1 · The decisions passed to U1 (each: the question, the decision, the ladder step, the edits it orders)

### D-U1-01 · The seat's modifier: dice (U1 §3 item 6, `27_MB_A` §5) or obstacle plus levels (OBS §2–§3, U5c C-35)

**Decided: obstacle plus levels, with one channel per side.** A seat reaches a roll in exactly two ways:

1. **The seat the actor exercises (`Act.via`) helps him** as named levels from the leverage source `office`
   (`rosters.yaml: advantage_sources`, OBS §3), never as dice. The size is a per-seat datum (D-U1-01a).
2. **A seat held above the actor's exercised seat by the person acted on stands against the act** as the
   obstacle term `rank_gap` (OBS §2 member 6), never as levels.

OBS §3's defender column for `office` ("the same for a seated counterparty acting through his seat") is
**struck**: the counterparty's seat already enters once, as `rank_gap`; a second entry as levels against the roller
would count one seat twice. In a two-sided proceeding each party's own move is his own roll, so his seat enters on
his roll's actor side and nowhere else. No `edge` row may read a seat; `regard` reads stance rows only (OBS §2
member 7); the chooser's stance toward an office-holder stays a choice-side term.

**Ladder.** Step 1: A-79 accepts lane 29's tuning as A-71's answer, and that tuning's input table names the seat as
"the `office` level source" (`29_DICE…` table row *seat*); A-25 puts what helps in levels and what stands against in
the obstacle. Step 5: under A-6/A-7 the pool is **training only** (score plus base); everything that is not the
roller's training reaches the roll as a soft-capped level (29's S line: "one channel for everything that is not
training"). A dice addend would be an uncapped second door into the pool and would not oppose (29 item 29-4: the
opposing operand excludes addends), so a seat would attack and never defend; levels are symmetric and capped at
`M_MAX`. **U1 §3 item 6 and `27_MB_A` §5 lose.** A-12's own consequence line ("the bench die in T13 T4 stands") is
honoured: the bench die is OBS §3's first `office` member, restated once in the level unit at OBS §4 step 5.

**D-U1-01a · Where a seat's modifier is authored.** One column on the seat's own row: `engine/season/offices.yaml`
row key `modifier: <a LEVEL_SIGMA name> | null` (absent = none; "a seat declaring none behaves as today", A-13's
pattern), carried on `state/carriers.py::Office` as `modifier: Optional[str] = None`, refused at load unless a member
of `sigma_leverage.LEVEL_SIGMA`. Read by one host function, the `office` member of `sigma.py::ADVANTAGE_SOURCES`,
off `Act.via`. Ladder step 4 (`04` §B.13: a property of a roster member travels with the roster; the `term:` and
`vocation:` seat-row keys already proposed). No global `office_level` fixture is created; OBS §3's `office_level`
becomes the seat row's value. T13 T4's `standing_dice` is not created as a fixture: its first value is authored as
`modifier:` on the bench seats.

**Edits ordered (rewrite lanes).**
- `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §3 item 6: rewritten here (this lane's own file).
- `27_MB_A_command_and_the_obedience_draw.md` (MB rewrite lane): §2 `CommandRecord.addends` comment becomes
  "whole dice from the registered pool addends (practice)"; `CommandRecord.levels` gains "and the `office` level of
  the seat the march is made through"; §5 is rewritten to the two halves above (the commander's march seat as an
  `office` level; no officer has one); gate 7 and test `test_a_seat_addend_reaches_the_commander_only` become
  `test_a_seat_modifier_reaches_the_commander_as_a_level`.
- `U5c_SC_one_obstacle_form.md` (SC rewrite lane): §3 `office` row, defender column → "—"; `office_level`
  → "the exercised seat's `modifier:` (`offices.yaml`)"; the T4 sentence keeps its "restated once" clause.
- `10_DICE_capability_axiom_map.md` head and §A `addend` row (DICE rewrite lane): strike "a seat's resources" and
  "a seat's modifier is an `addend` (A-12)"; the `addend` role keeps practice and helpers.
- `U5a_capability_home_and_two_inputs.md` row A4 (CORE/DICE rewrite lane): "a seat's modifier is an `addend`" →
  "a seat's modifier is the `office` leverage source (U1 §3 item 6)".
- `13_SC_tuning_tables.md` T4, `14_VERBS_BINDING_C_turnover.md` (standing term), `06_FA_office_capabilities.md`
  head, `07_SE_capability_rate_B.md` head, the institutions synthesis files that add an office modifier: each
  cites D-U1-01 (the term is `rank_gap`; the help is the seat row's `modifier:` read by `office`).
- **Layer 1 text owed (A-12, OWED §A row 2), drafted here and applied only by Jordan's amendment.** `04` §B.7, the
  `Seat :=` block's `NEVER:` line becomes *"NEVER: who holds it · who serves it"*; the block gains
  *"`modifier?` — a named level (A-12, 2026-11-12) on rolls made through this seat; the help half only"*; the
  invariant row *"a seat adds no verb and no modifier | STRUCTURAL"* becomes *"a seat adds no verb; its only
  modifier is `modifier?`, a level read off `Act.via` by the `office` leverage source, and a seat above the
  actor's stands against an act only as the obstacle term `rank_gap` | STRUCTURAL | one column; one reader;
  `eligibility_kinds` has no `capability` member and the loader raises on one"*. `holonic_ARCHITECTURE.md` §9.2
  ("`capability` supplies dice and gates nothing") is about a **capability's** rank and is **not** amended:
  the register's citation of it as the seat rule (D-12 text) conflates two ranks (see glossary *rank*).

### D-U1-02 · The opposition operand (A-79): the opponent's pool or his trained score

**Decided: the trained score, never the pool, in both modules.** `opposed_ob(score, rate) = rate × max(0, score)`
with `rate = opposition_rate` (one fixture, control 0.5, live `MU_PER_DIE`). The social composer adds the base
dice's mean as its own leading term, the even line `MU_PER_DIE × pool_add`; the fight adds nothing (its defence
layer spends the defender's base). Ladder step 1: A-79 ("same rule only"; "the defender's trained score at 0.4
per point … the six base dice never part of the opposition"). Numerically the social obstacle is unchanged
(0.4 × pool = even line + 0.4 × score when the floor does not bind).

- The operand's one reader: `seam/wrappers/pool.py::score(w, p, verb)` for the capability the verb's row names as
  `opposed_by`'s capability (else the verb's own). A person always has one (the untrained score). No practice
  addend, no seat, no attribute.
- **Edits ordered.** U1 §4 row *the opponent* (this file's sibling, done here); `10_DICE_capability_axiom_map.md`
  head and §A `opposes` row; `10_DICE_one_score_two_roles.md` head ("his **pool** under the same pool rule");
  CAP row B4/B5 bodies (already `Folded:`, the body sentence is stale); `U5c_SC_one_obstacle_form.md` §1 row
  *the score a person rolls and opposes with* (add "the trained score"). Each replaces "pool" by "trained score"
  and cites A-79.

### D-U1-03 · `rhetoric` as a fourth social skill

**Decided: not created.** The hearing moves `argue` (rungs `fact`, `justification`) and `impugn` draw on the
existing capability `argue`; rungs `procedure` and `definition` draw on `law`. Three new social rows stand:
`deception`, `law`, `insight`.

Ladder step 4: ED-IN-0350 (Jordan, 2026-11-05, quoted at `rosters.yaml: vocation_attribute`) rules what argument is
("argue main component is presence, attunement informs how character thinks the other character is receiving it");
it does not split argument by the size of the audience. Step 5: `rhetoric` and `argue` share a base (Presence), an
untrained rule and growth rules, and differ only in audience; the audience already reaches the roll as the
obstacle term `reception` (OBS §2 member 8) and the `favour` level, so a second skill for the same act would split
one person's training in two and let a skilled pleader be a novice in court. Reading a room is `insight`
(Attunement), which ED-IN-0350 names. Reversible on a word: re-adding is one definition row and two cells of the
`hearing_moves` column.

**Edits ordered.** `05_SC_hearing_capabilities.md` (SC rewrite lane): the `rhetoric` definition row is struck with a
`Reconciled:` line citing D-U1-03; the `hearing_moves` table cells become `argue` (by rung: `procedure`,
`definition` → `law`; `fact`, `justification` → `argue`), `impugn` → `argue`, `answer` → as `argue`; edit 1 reads
"three rows". R2 §3's conflict row closes.

### D-U1-04 · Who owns a person's scores and a task's difficulty (lane A, OWED §E (2))

Three facts, three owners (one each); lane A's interim rosters retire into them at named batches.

| fact | one owner | lane A's interim (branch) | what happens to it |
|---|---|---|---|
| a person's **training** (rank per capability) | the cast row's `capabilities: {<id>: <rank>}` in `references/npc_registry.yaml` (CORE Edit 5, P), bundles in `rosters.yaml: tables.lifepath_templates` (T); read by `data/cast.py::capability_of` (T) | none | — |
| a non-holder's **untrained score** | `Fixtures.pool_default` (T, H-126) | `rosters.yaml: unauthored_attributes` values 2 (B) equal it by construction | see next row |
| a person's **talent** (attribute, 1–7) | the cast row's `stats:` (`npc_registry.yaml`, T), held on `Person.attributes`; an unauthored attribute is **not stored**: the roll reads the scale's mid-point, derived from `descriptors.ATTRIBUTE_FLOOR`/`ATTRIBUTE_CEILING` (T), zero levels either way | `unauthored_attributes` (B) seats 2 on every key under every person (`build_realm(cast_attributes=True)`) | **retired at CAP Part B**, when the attribute leaves the pool (A-7). Until then it is the interim that lets the attribute-as-pool code (CR-20) read a score for everybody; its values must equal `pool_default` and say so |
| a task's **difficulty** | a `difficulty:` cell on the verb's own row (`engine/season/verb_table.yaml`, P), naming a member of the closed roster `rosters.yaml: difficulty_levels` (`plain routine demanding hard`, P); the size of each level is the fixture table `Fixtures.difficulty_ob` (P, NUMBER row); required on every rolled row, refused at load where absent | `rosters.yaml: task_difficulty` (B), `verb: number`, closed over the social roll's verbs | **retired at OBS §4 step 1a**: each of its nine rows becomes `difficulty: routine` (the control arm C-04 orders: routine 1 + the stand-in 1.0 = today's 2.0 for an inquiry; routine 1 + 2/2 = 2.0 against an ordinary person) |
| the **content** (who is how good; which task is harder) | Jordan's and the CHAR content pass (CAP Part C) | lane A ships every person at 2 and every task at a calibration | the suite assumes the defaults until authored; charge 3 ("Ob always 2 is wrong") stays **not met in the shipped realm** until Part C (OWED §E) |

Ladder: step 4 for the mid-point (the tree already derives the attribute mid-point this way for the told-claim
credit: `engine/season/decision/options.py:1631`, `COMPETENCE_MID = (ATTRIBUTE_FLOOR + ATTRIBUTE_CEILING) / 2`, T); step 4 for the difficulty home (the verb's facts live on its row:
F-CORE-18, U1 §1's `capability:` column; a side roster keyed by verb is the shape U1 already refused); step 5 for
one level ladder (the four named levels are what `13_SC_calibration.md` C1 is stated on; a per-verb float would be a
second ladder for the same quantity). Hash: retiring `task_difficulty` into `routine` rows is hash-equal at the
control arm (the composed obstacle is the same number); retiring `unauthored_attributes` is inside CAP Part B's one
re-pin. **(U3 defers)** on the order: lane A's branch is the base of any v12 batch touching these files (OWED §E).

**Edits ordered.** (1) The batch that lands OBS §4 step 1a takes lane A's branch as base, deletes
`rosters.yaml: task_difficulty`, `data/verbs.py::_load_task_difficulty` and `Fixtures obstacle_model`'s `task` arm
(the `stand_in` arm is OBS's control), and adds the `difficulty:` column; gate: the 72-record grid of
`engine/season/tests/test_b11a_scores_and_obstacle.py` (B) composes the same obstacles before and after. (2) CAP
Part B deletes `rosters.yaml: unauthored_attributes`, `data/rosters.py::_load_unauthored_attributes` and the
`cast_attributes` seating, and adds `pool.py::talent` returning `None` for an unauthored key (read as mid-point);
falsifier: an unauthored person's talent levels are non-zero.

### D-U1-05 · The `read_to_addressee` witness roster: its home and its closed-set refusal (OWED §E (3))

**Decided: it is the one owner of "which Records' content reaches their addressee without his holding the
paper", and FA's `public_terms` column is folded into it.** Owner: `engine/season/rosters.yaml: read_to_addressee`
(B), read by `loop/witness.py::addressee_reads` (B). **Its shape changes from a list of kinds to a map from a
`record_kinds` member to the verbs whose mint of that kind is put to the addressee:**
`{challenge: [challenge], dispensation: [issue]}`. The qualifier is needed because a kind is not enough: `covenant`
also mints a `dispensation` (`verb_table.yaml:319`, `_eff_covenant` through `_mint_document`), and its counterparty
"learns the terms only by holding the Record" (#453 K-54, quoted at the same row), which A-21 keeps ("covenants and
challenges stay in person"). The verb list is FA edit 2's `WRIT_MINTING_VERB` filter (`world_q.py:1604`, T) moved
into data. `06_FA_decree_binds.md` edit 1 (`record_kinds.dispensation.public_terms: true`) is **not** made, and its
edit 2's deposit loop is the existing `addressee_reads` path, not a second loop.

- **Why one roster, not a column.** `record_kinds`' values are lists of content keys (`dispensation: [terms, to, at]`,
  T); a `public_terms: true` cell would turn one member into a map and the rest into lists: a second shape in one
  roster (shape divergence). The sibling-list form is this file's precedent for a property of record kinds
  (`covert_kinds`, `forgeable_kinds` proposed, `lie_verbs`). Ladder steps 4 and 5. The two proposals carry one
  rule (deposit the content to the witnessing addressee), so two carriers would be a second copy.
- **Closed-set refusal (CLAUDE.md §0.05, the loader's refusal per data family).** `data/rosters.py` refuses at
  import (a) a key that is not a `record_kinds` member (B, built), (b) a key whose content keys hold no addressee key
  (`record_kinds`' `addressee: to` map, T) — FA edit 1's refusal, moved here — and (c) a verb that is not a
  `verb_table.yaml` row or whose effect does not mint that kind. Falsifiers: plant `works: [found]` (no `to` key):
  the import refuses naming the key; a covenant's counterparty, witnessing the covenant, holds no `content:dispensation`
  claim (test beside `test_b11a_duel_reach.py`); an `issue`d writ's addressee does. Control: `{}` reproduces the
  parent hashes (lane A's own control, `[]`).
- **Name.** Kept (the built name; no retrofit, CLAUDE.md §4). Its note gains the definition sentence: "a Record, by its
  kind and the verb that minted it, whose content WITNESS deposits to its addressee when he witnesses its making,
  the Record staying in its maker's hand (ED-IN-0292 (1))".
- **Edits ordered.** (1) The batch that lands `06_FA_decree_binds.md` takes lane A's branch as base and changes the
  roster's shape to the map (lane A's loader and `addressee_reads` read `kind in ROSTER and verb in ROSTER[kind]`;
  hash-equal at `{challenge: [challenge]}`). (2) `06_FA_decree_binds.md` (FA rewrite lane): edit 1 rewritten to "add
  `dispensation: [issue]` to `rosters.yaml: read_to_addressee`"; edit 2 rewritten to "no new loop:
  `addressee_reads` deposits it"; the control (the entry absent) and the gate stand. U2 grades the roster against
  `04` (OWED §E (3) names U2 for the grade; this decides home, shape and refusal only).

### D-U1-06 · `Event.observed` versus a new `draws` field or `fell_to` elsewhere

**Decided: `observed` is the one channel for every per-Event fact that WITNESS may deposit and that is neither a
change (`changes[]`), the band (`degree`) nor a per-party fight ending (`ending`).** That covers what the fold read
(today's sense), the derived outcomes `fell_to` (`03_PC_typed_outcome_one_door.md`), the scene-shape Observations
(`16_PESSIMIST_PC_C…`), the field's named draws (`_eff_march`'s Observations of `FieldOutcome.report.draws`,
`27_MB_C`) and the roll's terms where a proposal wants them witnessed. No `Event.draws`, no `Event.roll` field is
added. Ladder step 4: the tree already does exactly this, with an `[ASSUMPTION]` tag, in `body_observed` and
`broke_observed` (`engine/season/loop/effects_combat.py:301-315`, T): *"An Event carries no payload (`Event.ending`'s
note), so the cause rides `Event.observed`, deposited by WITNESS"*. Step 5: a fourth Event field would be a schema
mover on every Event and a second channel WITNESS must learn.

- **The docstring is out of step with its use, and is amended at the code, not in Layer 1:**
  `state/carriers.py::Event.observed`'s comment (`:276-293`) gains: *"and the outcomes an effect derives from the
  scene it wrote (a felling's source, a body that broke first, a named draw), as Observations WITNESS deposits;
  never an actor, a target or a recipient (S19.3)"*. `04` §B.9 is not edited (the field already departs from it,
  named at the site, H-266; U2 grades).
- **Constraints carried.** (a) An Observation that names a person as a doer (`fell_to_hand`, `first_blood`) is
  deposited only through channels whose `observation_terms.supplied_by` includes `who` (R5 §1's rewrite of
  `16_PESSIMIST_PC_C`, `04` §C.6) — this decision does not widen attribution. (b) Every predicate a proposal puts on
  `observed` is a member of the closed roster `rosters.yaml: observation_terms` (T) — the roster the PC proposal left
  `[name it at landing]`. (c) `Event.ending` stays the per-party fight ending (`fight_endings`, T); a field's end
  state is the band (`field_degree_bands`, T), not an `ending`.
- **The roll's record** (`10_DICE_believed_odds_have_a_prior.md` Edit D's `roll:` field; `05_SC_contest_record_on_event.md`)
  rides the act's Resolution and the reason trail (`fed_by`, `terms`, `levels`), not a new Event field; where a
  proposal needs it witnessed, its parts go on `observed` under `observation_terms` members. **(U3 defers)** on
  whether F-SC-04's persistence of `ob_terms` (lane A's residue) lands with SC-P1 or the GO receipt.
- **Edits ordered.** PC rewrite lane: `03_PC_typed_outcome_one_door.md` names `observation_terms` as `fell_to`'s
  roster and cites D-U1-06; `16_PESSIMIST_PC_C…` the same for its five predicates. MB rewrite lane: `27_MB_C…` and
  `04_MB_typed_outcome_and_one_path.md`: "the draws ride `Event.observed` as `observation_terms` members
  (`draw:<name>`)". DICE rewrite lane: `10_DICE_believed_odds_have_a_prior.md` Edit D withdrawn in favour of
  `fed_by` (already merged, `U5_CONFLICTS_U5a.md` §4 row 5).

### D-U1-07 · Where a capability is defined: `rosters.yaml` or `descriptor_registry.yaml`

**Decided (U1 of U5a confirmed, re-verified against the tree): `references/descriptor_registry.yaml: capabilities`.**
Verified: the registry exists, has no `capabilities` block today, is exported by `tools/export_descriptors.py`
(validators per roster block, `--check` mode at `:45`, blocking in CI at `.github/workflows/valoria-ci.yml:140`) to
`engine/engine_params/descriptors.json`, and read by `engine/substrate/descriptors.py` (`ATTRIBUTES`, `PURSUITS`,
`HERITAGES` the precedents). `rosters.yaml` keeps what the **season** does with a capability (roles, sites, uses),
pointing back with `capabilities: {from_descriptor: capabilities}` (the `pursuit_axes` precedent). Ladder step 4
(every other person-trait roster is split this way) and step 5 (a registered module and the port may read the
substrate leaf and the exported JSON, and may not read `engine/season/data`, `04` §A.2; CLAUDE.md §5). Losing
homes: `10_DICE_capability_axiom_map.md` §B (`rosters.yaml: tables.capabilities`), `06_FA_office_capabilities.md`
body (`rosters.yaml: verb_capability`, `vocation_attribute`), `07_SE_capability_and_chooser_surface.md` §3–§4
(superseded already), lane A's three new `verb_capability` rows (B). Lane A's rows are **values** that move to the
verb-row column at CAP A2/A3: `interrogate: inquiry` and `arrest: arms` stand; `determine: argue` (B) is the
interim until `law` has a definition row, then `law` (U1 §5).

### D-U1-08 · One owner of the pool rule, and the fight's `faculties` field

**Decided.** The pool rule `max(pool_floor, score + addends + pool_add)` is one pure function,
`engine/dice_engine/sigma_leverage.py::pool_of(score, addends, pool_add, pool_floor) -> int` (P), beside `opposed_ob`
and `even_line` (29 item 29-1). The host's `pool.py::faculty` calls it; the combat module calls it in place of
`core.resolution_pool`'s own arithmetic. `PersonalCombatInput.faculties` (today the score with addends, R1 7b-3) is
replaced by `scores: (int, int)` (the trained score: what `ob_from_defender` opposes with, 29 item 29-2) and
`addends: (int, int)`, beside `pool_add`, `pool_floor`, `opposition_rate` carried raw. Ladder step 5 (one rule,
two callers; the module may import the dice engine, `04` §A.2 provider row as OBS reads it); step 1 for the operand
(A-79). The rename also clears a collision: `faculty` names the pool in `pool.py`, the attribute Reason in the
registry's aliases, and "learned skill" in A-59 (glossary).

**Edits ordered.** PC rewrite lane: `U5b_PC_rulings_in_the_fight.md` §2, `03_PC_person_inputs_content.md` Part A
(`pool` slot = `scores`), `29_DICE…` item 29-2 step 2 (`defender.faculty` → `defender.score`). DICE rewrite lane:
`10_DICE_capability_axiom_map.md` §D rows for `PersonalCombatInput`. MB: `27_MB_A` `CommandRecord` already carries
`score` and `addends` (conforms).

### D-U1-09 · The `rate` role and the settlement's untested effects

**Decided.** `rate(w, p, verb)` (`07_SE_capability_rate_B.md` §4 (c)) reads `pool.py::score` (the trained rank, on the
capability's own 0–7 scale), **not** `faculty`: about_mid over the capability row's floor and ceiling is only
meaningful on the rank, and `faculty` carries `pool_add` (6) at the live arm. A verb row that becomes a **task row**
under `18_DETERMINISM_task_draw_for_uncontested_verbs.md` (a drawn act) takes its capability through the `task`
site's `dice` row and **no** `rate` row: one capability, one channel per act. `rate` remains for magnitudes no draw
decides (CP-T08-01's `labour` hand weights). A steward's skill on the harvest draw (A-54) is an `edge` row at site
`settlement_effect`, `side: steward`, for the place's draw: the place rolls, the steward is not the roller.
Ladder step 5 (one channel per act; levels for what is not the roller's training, D-U1-01's rule).

**Edits ordered.** SE rewrite lane: `07_SE_capability_rate_B.md` §3 item 2 and §4 (c) `faculty` → `score`; the head's
A-54 sentence "contributes to the **pool** of the place's seasonal draw" → "contributes named levels (`edge`,
`settlement_effect`) to the place's seasonal draw"; a `magnitude: rate` row that is also a task row is refused at load.

### D-U1-10 · The year: one owner, one unit (test 3)

**Decided: one season is one tick; a year is four seasons (ED-IN-0332, RULED, verified at
`registers/editorial_ledger_in.jsonl` row ED-IN-0332); the season loop's one owner of the year is
`engine/season/rosters.yaml: seasons_of_year` (P), ordered `[spring, summer, autumn, winter]`** (`20_NARRATIVE_E`
edit 1). `world_q.season_of_year` reads its length and never returns `None`; `season_factor_draw` (T) keeps its
`()` control and, when non-empty, is refused unless its length equals the roster's. Losing readings:
`09_WR_B_weather_with_memory_and_the_year.md` (`year = tick // len(season_factor_draw)`), CP-T10-03's planned
`year_length` fixture (design only, not in `fixtures.py`), and every restatement of "four" as a literal
(`06_FA_seat_terms_by_body_B.md`; `16_PESSIMIST_WR_C` `born = -4 × age`; `worldgen.yaml` ages; A-51's twenty
seasons). Each reads `len(SEASONS_OF_YEAR)`. Ladder step 1 (ED-IN-0332 fixes the value), step 5 (CLAUDE.md §0.05
clause 3: one owner, re-derive). **The oracle's copy.** `systems/overview/sim/ms_track.py:49 SEASONS_PER_YEAR = 4`,
exported to `engine/engine_params/game_constants.json` (`tools/export_game_constants.py:75`), is read by nothing in
`engine/season` or `modules/` (grep: its own file and its exporter only). It is left to the overview oracle's own
retirement, not edited by the suite; the two agree today and no game path reads the second.

### D-U1-11 · Smaller owner and vocabulary decisions the extracts raised

| id | item | decision | step |
|---|---|---|---|
| D-U1-11a | `fight_endings`' victor value (`03_PC_typed_outcome_one_door.md` adds `standing`) | the member is `prevailed`; `standing` already names S18.2's gap (`Sensation.standing`, `decision/options.py::standing_of`, T), a prize (`a standing`, T) and the MB standing order | 5 (CLAUDE.md §4) |
| D-U1-11b | the nesting-cap refusal (`dict(status="NESTING-CAP")` vs `04` §C.5 `Refusal(depth_cap)`) | the typed `Refusal(depth_cap)` | 3 (Layer 1 type) |
| D-U1-11c | MB tunables: `config.py` exported (`mass_battle_v1.json`), `references/troops.yaml`, or a frozen `EngineConfig` (R1 7b-8) | two kinds of fact, two owners, no fact in both: table-shaped content keyed by troop kind, arm, formation, stand case, armour tier and fatigue row → `references/troops.yaml` (P*), exported to `engine/engine_params/troops.json` by a new exporter with `--check` (P*); scalar engine constants → literals in `modules/mass_battle/config.py` exported to `mass_battle_v1.json` by `tools/export_engine_params.py` (the combat precedent: `CFG` → `combat_engine_v1.json`, T). `EngineConfig` is the typed in-memory reader of those two, not a home. A constant that moves to the table is deleted from `config.py` in the same commit (26's `MB_STAMINA_*`, `MB_CAVALRY_SPEED_MULT`) | 4, 5 |
| D-U1-11d | the carry rule (`carry_demand_of`) placement | one pure function in `engine/substrate/combat_kit.py` (T file; the kit data's owner); the host computes each party's shortfall for each kit it may wield and carries them raw on `PersonalCombatInput` and the unit row; the modules hold no copy | 5 (`04` §A.2: a module reads its typed input) |
| D-U1-11e | the field's end-state record `FieldOutcome` (eleven additions across seven files) | one field list, owner `engine/season/queries/inputs.py::FieldOutcome` (T): `ended, turns, attacker, defender` (T) + `parts, report, interventions` (`04_MB_manager_battle_one_resolver.md`) + `rallied, pursuit_loss, taken, gave_ground` (`26_MASS_BATTLE_rout_pursuit_and_giving_ground.md`) + `stamina_left` (`26_…movement_and_fatigue_as_data.md`) + `fight_loss`, `bouts` (`26_…cell_scale_and_time.md`) + `report.draws` (`27_MB_C`); each lands with its proposal and no other proposal re-declares it | 5 |
| D-U1-11f | the standing-order cap (literal "at most 4") | a key of the exported orders file: `engine/engine_params/battle_orders.json` (T) via `engine/substrate/battle_orders.py` (T), named `standing_order_cap` | 4 (D-38's own pointer) |
| D-U1-11g | `MassBattleInput.command` (1..7 integer) vs the capability `command` | the capability is `command` (27_MB_A); the old integer is retired with `derive_command`; `command_span` (the 1..7 span read off the score) keeps its name and is not called "command" in prose | 5 |
| D-U1-11h | the writ's Record kind (`dispensation` in the roster, `writ` in code and `06_FA_hygiene.md` e4, `decree` in A-21) | the roster key stays `dispensation` (T, the cited key of `read_to_addressee`, D-U1-05); prose says "writ" for any dispensation and "decree" for one proclaimed; `06_FA_hygiene.md` e4's rename is withdrawn (it would move every hash for a word) **(U3 defers on order)** | 4, 5 |
| D-U1-11i | the route roster name (`graded_inquiries` T, `graded_tasks`, `graded_acts`, `graded_routes`) | `graded_tasks` (18-A; C-22/C-23 already chose it); `graded_inquiries` is renamed once, in 18-A's commit | 4 |
| D-U1-11j | one stand-in family (`pool_default`, `obstacle_default`, "ordinary score") | `pool_default` alone (the untrained score); `obstacle_default` is deleted (C-04) | 1 (C-04) |
| D-U1-11k | `remove` (institutions) and `distance` (OBS member 20), `carriage` (MAT_B) | one member `distance`, one fixture `distance_step` | 4 (OBS refusals list) |
| D-U1-11l | `effect_share` (MAT_A), `band_entry` (S2_C), `task_fraction` | `task_fraction` (C-23) | 1 |
| D-U1-11m | `person_q.resolve` (CHAR, proposed) vs ratified `faction_q.resolve` | the person reader is `person_q.decisiveness` | 5 (R2 §4) |
| D-U1-11n | the GO host-side reading `receipt(w, act_of, pid, since)` / `ReceiptRow` vs Layer 1 `Receipt` | renamed `act_result` / `ResultRow` | 5 (Layer 1 owns `Receipt`, `04` §B.9) |
| D-U1-11o | `subformation`: A-59's "each unit within subformation" vs the MB designer surface (a subformation is a unit's arrangement) vs code `Subformation` (the unit spec) | the code meaning stands (a row of `subformations` is a unit, A-2); a unit's cell arrangement is its `formation` (`ranks, files, shape`); A-59's grouping above units is a **formation post group** (`front, rear, left, right, reserve`); prose never says "subformation" for a grouping | 4 (the Record key `subformations`, T in `armyrecord.KEYS`) |
| D-U1-11p | `prowess`: a unit's quality (A-59, `27_MB_B`) vs a person's training (29) | a **unit's** quality only; a person's is "training" | 5 |
| D-U1-11q | `aptitude`: a capability kind (U1 §2) vs the attribute (29) | the capability kind only; the attribute is "talent" | 5 |
| D-U1-11r | the seat-row key list (A-12, A-13, `term`, `vocation`, dignity, …) | one schema, owned by `engine/season/offices.yaml` rows and `state/carriers.py::Office`, one loader; keys as listed in §2 row S-24; each key lands with its proposal; a key no reader reads is not added (ID-13) | 4 |

---

## §2 · One interface per edge (test 4)

| edge | the one typed interface (owner) | each side cites it as |
|---|---|---|
| evidence: fieldwork → social contest | the citing act's `cites` operand (FI, `08_FI_05_evidence-interface_B.md`); the case file's entries are **exhibits** (`Exhibit`, the module's record) entered by the citing speech's band (`19_LACUNA_admission_rides_the_citing_draw.md`, C-05); their weight reaches the roll only as the `proofs` leverage source (OBS §3); `rosters.yaml: proofs` (T) the closed set of kinds | FI: "an item is cited"; SC: "an exhibit is entered"; both cite ADM for entry and OBS §3 for weight |
| the duel round inside a field | `nested_entry("combat.round", depth, fx)` (U5b §1) taking `DuelRoundInput` (P) and returning `DuelContactResult(pair, felled, wounded, yielded)` (P); depth cap 1 (A-72); refusal `Refusal(depth_cap)` (D-U1-11b); the round carries `scores`, `addends`, `pool_add`, `pool_floor`, `opposition_rate` raw (D-U1-08, 29 item 29-5) | PC and MB cite U5b §1 and this row |
| the player view (lanes → port) | person-side: one `state/carriers.py::View` (T, `:456`) whose slots are the one closed list (`odds`, `questions` T; `strands`, `calendar`, `head_seats`, `circle` P by `11_GO_player_surface_contract_B` and `30_GO_F`), filled by the GO readings `situation`, `offer`, `account`, `dossier` (`decision/sheet.py`, `queries/person_q.py`); host-side: `act_result` (D-U1-11n). No lane adds a reading outside this list; a new slot is a member of `View`'s list with its reader (ID-13) | GO owns the list; every lane that wants a player-visible fact names the slot |
| capability: dice, character, every consumer | `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §8 (the reader interface) | all lanes |
| the campaign layer: governance, settlements, mass battle | the field returns an end state (`field_degree_bands`, T; A-3); title moves only by the one title owner's act (seize/occupy, A-57–A-66) reading the band and the march's context; losses return as `FieldOutcome` fields (D-U1-11e) written to the army Record (A-2, A-69); seats pass with holdings by the `conquest` gate basis (`U5d_FA_land…`) | FA, SE and MB cite this row and their own proposals; no lane writes title by a second path |

---

## §3 · One ladder, one unit, one clock per quantity (test 3)

| quantity | measured twice as | the one unit and owner (decided) | step |
|---|---|---|---|
| **degree** | the four-band ladder; combat's `Felled/Wounded/Untouched`; the field's `Won/Lost/Drawn/Unopposed/Invested`; "band" in six senses | a **degree** is one of four bands of one ladder, `engine/dice_engine/dice_engine.py::degree_from_net` (T, `:236`; `Degree`, `:27`), band edges in that function (exported `BAND_FLOORS`, P, `10_DICE_exported_face_rule…`). Combat's three and the field's five are **end states** read off their module (`combat_degree_bands`, `field_degree_bands`, T; A-3), never called degrees in new text. `compute_degree`/`degree_label` survive only as callers of `degree_from_net` | 1 (A-3), 4 (`rosters.yaml` notes) |
| **margin** | an integer (`04:903`, D-29) and a real (A-5) | a **real number** (the continuous sampler's net minus the obstacle) under A-29's declared-float contract; band edges compare it; nothing rounds it to an integer before the ladder. `04:903`'s integer wording is covered by A-29's owed step-13 text (OWED §A row 6) | 1 (A-5, A-29) |
| **leverage** | "levels", "advantage", "leverage", "edge" | **named levels** of `sigma_leverage.LEVEL_SIGMA` (T, `:103`), summed and soft-capped at `M_MAX` 1.5σ (T, `:110`); the roster is `advantage_sources` (T); prose calls the quantity "leverage", a unit of it "a level" | 4 |
| **obstacle** | per-verb tables; two `obstacle_terms` rosters | **successes**, composed once by `modules/social_contest/roll.py::obstacle` (OBS §1) and `modules/combat/core.py::ob_from_defender` (29), both through `opposed_ob`; difficulty in named levels (D-U1-04) | 1 (C-02), 5 |
| **fatigue / stamina** | MB column ledger 0–100 (`modules/mass_battle/percell.py`); `entry_stamina` share; PC `DuelState.stamina`; threadwork session `fatigue`; A-69 "fatigue" | **stamina** is the reserve and **fatigue** its loss; at every typed boundary (field in, field out, round in, round out) stamina is a **share of full in [0, 1]** (`MassBattleInput.entry_stamina` P, `FieldOutcome.stamina_left` P); a module's internal scale (MB 0–100) never crosses a boundary. A-69's carried fatigue is the one stamina share on the army Record's unit row. **Thread Fatigue** (`names_index.yaml: thread.thread_fatigue`, T) is a different quantity (a practitioner's), never "stamina" | 5 |
| **speed** | `pace` per troop; `MB_CAVALRY_SPEED_MULT`; the season's march | inside a field: **cells per tick** (`cell_m` 4, `tick_s` 4: `troops.yaml: deployment.scale`, P*), each troop kind's `pace` its one owner (the multiplier is deleted, 26); between fields: **adjacency steps per season** (`march_budget`, `valoria_geography_v30.yaml`, T). Two quantities with two names; neither converts to the other | 5 |
| **regard** | `regard_unit: raw` vs `stance`; four fixtures (`regard_sign`, `regard_unit`, `regard_step`, `waiting_valence`) | the **stance row's unit**, `Σ valence × weight`, clamped at `±STANCE_MAX` (25, `data/cast.py`, T) — `02_CHAR_scar_cap_and_regard_unit.md` item 2's live arm. `regard_step` (obstacle per full clamp) and `favour_level` are **conversions at the roll's boundary**, not second units; `waiting_valence` is a valence in the same row unit; `regard_sign` is a sign, not a unit | 5 |
| **standing** | S18.2's gap; the prize `a standing`; rank against an act; a document's band; the bench die; the fight's victor; a standing order | **standing** is S18.2's scalar, the gap between what others say of a person and what he holds of himself, an integer on `condition_scale` (`decision/options.py::standing_of`, T, `:1524`), and the prize `a standing` (T) is the contest that moves it. Rank against an act is `rank_gap`; a document's band is `force` (VRES); the bench die is `office` (D-U1-01); the victor is `prevailed` (D-U1-11a); "standing order" is a fixed two-word MB phrase and is never shortened | 5 |
| **year** | 4 seasons; twenty seasons (A-51); `()` (unshipped) | D-U1-10 | 1, 5 |
| **territory count** | 15 (GD-1 canon), 16 (realm), 17 (provinces in the geography file: `T1`–`T17`, T15 with no settlement, T16 the foreign root) | the unit is **a rung of kind `territory` under a `realm` rung**, counted at read by `world_q.endings_reached` (T, `rosters.yaml: endings` note: "every territory under a `realm` rung counts, not a fixed 15"); no proposal writes a territory count as a constant. Which number is right is a contradiction of fact: **U3's** | 4 (`endings`) |
| **cost / price** | `task_fraction`, `effect_share`, `delivery_share`, `exchange_terms`, `works_outlay` | per-mille of the act's stated amount for every band table (MAT_A–C's convention, `amount_shares` T per-mille); `task_fraction` keeps its fraction form `{1, 1, 0.5, 0}` as the one default (C-23) and a row that departs names its own per-mille table | 4 |
| **round / turn / tick** | the season round; the duel round; a turn; `Claim.round` | **tick** = one season (the loop); **round** = one of `scene_budget` slots in a season (`Claim.round`, T); the duel's unit is the **exchange** (one of the duel's twelve turns is a "turn"); the PC "round" of `DuelRoundInput` is a **duel round** in full every time | 5 |
| **scale of play** | person, settlement, faction, realm; "army scale" | the four of `UNIFICATION_BRIEF.md` test 3; a field is fought at the person and army scales (A-4's nesting), not a fifth scale | 3 |

---

## §4 · The fact-to-owner ledger (test 2)

One row per fact, number, roster, closed set and schema the suite proposes or relies on. Probe readings (counts and
hashes printed by a scratch script and owned by no file) are **claims**, U4's fact check, not owned facts: they are
left out of this ledger. Columns: **owner** (file : key, mark); **consumers** (readers named by the proposals);
**competing home → decision (step)**; **removal edit** (the ordered instruction for a later lane; "—" where no second
copy exists).

### 4.1 · Dice, the roll and the obstacle

| # | fact | owner | consumers | competing home → decision (step) | removal edit |
|---|---|---|---|---|---|
| R-01 | the sampler | `dice_engine.py`/`sigma_leverage.py::roll_net_continuous` (T, `:417`) | `roll.py`, `core.py`, MB sampler | whole-dice social roll and MB whole-dice sampler → the bell curve (1, A-5) | `U5a_DICE_owed_edits.md` §1 deletes the second sampler; `10_DICE_exported_face_rule…` and `10_DICE_one_roller…` in part rewritten (A-5) |
| R-02 | per-die mean and spread | `dice_engine.py::MU_PER_DIE` 0.40, `SIGMA_PER_DIE` 0.800 (T, `:181-182`); `sigma_leverage.MU_PER_DIE` is an alias (T, `:118`) | `opposed_ob`, `even_line`, `net_boost` | `10_DICE_one_roller` C's `PER_DIE_NET_EV` → import the owner (4) | the alias stays an import; no literal 0.4 anywhere (29 gate 8) |
| R-03 | the face rule | `dice_engine.py` (`FACE_NET`, P: exported by `10_DICE_exported_face_rule…` A) | `band_odds` derivation only | after A-5 no play path deals a face (1) | `U5a_DICE_owed_edits.md` row 6 |
| R-04 | the ladder and its band edges | `dice_engine.py::degree_from_net` (T, `:236`); `BAND_FLOORS {partial 0, success 1, overwhelming 3}` (P) | every rolled act | `compute_degree`, `degree_label` (T) → callers of the owner (4) | DICE lane deletes the second entry point named in `U5a_DICE_owed_edits.md` |
| R-05 | level table, soft cap | `sigma_leverage.LEVEL_SIGMA` (T, `:103`), `M_MAX` 1.5 (T, `:110`) | `levels_to_net_sigma`, every leverage source, talent, wounds, office | — | exported once (`10_DICE_exported_face_rule…` Edit D) |
| R-06 | `OB_MIN` | `sigma_leverage.OB_MIN` 1 (T, `:114`) | `roll.py::obstacle` floor | — | — |
| R-07 | the opposition function | `sigma_leverage.opposed_ob(score, rate)` (P, 29 item 29-1) | `roll.py::obstacle`, `core.ob_from_defender` | `roll.py:141`, `core.py:124` divisors (5) | 29 items 29-2, 29-4 replace both |
| R-08 | the opposition operand | `pool.py::score` (P; `B` on lane A as a split of `faculty`) | `_opposition_of`, `ob_from_defender` | the opponent's pool (U1 §4, CAP B4, DICE map head) → trained score (1, A-79; D-U1-02) | edits in D-U1-02 |
| R-09 | the opposition rate | `Fixtures.opposition_rate` (P), control 0.5, live `MU_PER_DIE`; NUMBER row graded `ruled` | both modules via typed inputs | `U5b_PC_rulings` §2 edit 4 `fight_opposition_rate` → not created (1, A-71) | already folded in U5b |
| R-10 | the even line | `sigma_leverage.even_line(pool_add)` (P, derived, never typed) | `roll.py::obstacle` (leading term `even`) | U1 §4 wrote it as "rate × an ordinary person's pool" (equal while the floor does not bind) → `even_line` (1, A-79) | U1 §4 rewritten here |
| R-11 | the pool rule | `sigma_leverage.pool_of` (P, D-U1-08) | `pool.py::faculty`, `modules/combat/core.py` | `core.resolution_pool`'s own arithmetic; `BASE_POOL`/`POOL_FLOOR` literals (5) | PC lane: `core.py` calls `pool_of`; `BASE_POOL`, `POOL_FLOOR` become workbench defaults |
| R-12 | the pool's base and floor | `Fixtures.pool_add` (control 0, live 6), `pool_floor` (control 0, live 5) (P) | every site's `dice` row | DICE map's `social_pool_*`, `combat_pool_*` → one pair (1, A-6) | already folded |
| R-13 | the untrained score | `Fixtures.pool_default` 2 (T, `:449`, H-126) | `score`, the stand-in | `unauthored_attributes` (B) equal by construction → retired at CAP B (D-U1-04) | D-U1-04 edit (2) |
| R-14 | talent level size | `Fixtures.talent_level` (P), control `None`, live `minor` | the `edge` reader | `27_MB_A`'s `level: minor` per row → reads the fixture (4) | MB rewrite lane: `level: talent_level` |
| R-15 | the attribute scale | `descriptor_registry.yaml: attributes.scale` "1-7" (T) → `descriptors.ATTRIBUTE_FLOOR/CEILING` (T) | `per: mid`, the sheet | registry `default: 1` read as the roll's neutral → display floor only; neutral = derived mid-point (4) | CAP B1: `talent` returns `None`; nothing reads `default` for a roll |
| R-16 | the stand-in | `opposed_ob(pool_default, rate)` | every roll with nobody opposite | `obstacle_default` (T, `:451`) → deleted; `opposition_fallback` → not added (1, C-04) | OBS §4 step 1a deletes the fixture and H-127's row |
| R-17 | difficulty levels | `rosters.yaml: difficulty_levels` (P) `[plain, routine, demanding, hard]`; sizes `Fixtures.difficulty_ob` (P) control 0/1/2/3, live 0/0.5/1/1.5 above the even line | `roll.py::obstacle` | `task_difficulty` (B) → retired (D-U1-04) | D-U1-04 edit (1) |
| R-18 | a verb's difficulty | `verb_table.yaml` row `difficulty:` (P) | the composer | `task_difficulty` (B); T13 T1 per-verb values; SC-B values → OBS §4 (control: all `routine`; step 5: `interrogate` `demanding`) (1, C-04) | SC rewrite lane: SC-B and T13 bodies cite OBS §4 |
| R-19 | the obstacle roster | `rosters.yaml: obstacle_terms` (P), 29 members: `even` first, then OBS §2's 28 | `sigma.py::OBSTACLE_TERMS` (P) | SC-B's 10; DICE map's `[capability]`; seven per-verb tables (1, C-02); count 28 vs 29 is U3's (the `even` member is A-79's) | already folded; U4 counts |
| R-20 | each term's size | one fixture per term, control 0, NUMBER row (OBS §1) | the composer | per-verb tables (`tell_obstacle`, …) → members (1, C-21) | — |
| R-21 | rank term name | `rank_gap` + `rank_step` (P, OBS member 6) | the composer | `standing`, `standing_step` (BIND_C), `rank_gap_per_rung` (S2_C/S2_D) (5) | VERBS rewrite lane: BIND_C, S1_D, S2_C, S2_D cite OBS |
| R-22 | distance term | `distance` + `distance_step` (P, OBS member 20) | `comply`, `transfer` | `carriage_step` (MAT_B), `remove_step` (COL_B), `distance_ob` (S1_B) (4, D-U1-11k) | VERBS and institutions rewrite lanes |
| R-23 | watch term | `watch` + `watch_step` (P, OBS member 22) | `conceal`, `evade / defy`, … | `witness_step` (S1_B), `notoriety_step` (S1_C), MAT_D's (4) | VERBS rewrite lane |
| R-24 | the leverage roster | `rosters.yaml: advantage_sources` (T, `values: [effort]`), growing to `effort, capability, proofs, favour, approach, custody, office, lean, wounds` (P) | `sigma.py::ADVANTAGE_SOURCES` (T) | `28C`'s `waiting` inserted after `custody` (agree); `wounds` (A-8) | — |
| R-25 | proof, favour, press levels | `Fixtures.proof_level` (`minor`), `favour_level` (`major`), `press_level` (`minor`) (P) | leverage sources | `proof_step` → deleted (OBS §3) | SC rewrite lane |
| R-26 | the seat's help | `offices.yaml` row `modifier:` (P, D-U1-01a) | `office` leverage source | U1 §3.6 addend; T13 `standing_dice`; OBS `office_level` (1, 5; D-U1-01) | D-U1-01 edits |
| R-27 | wounds on a roll | `advantage_sources: wounds` (P); `Fixtures.wound_level`, `wound_step`, `wound_levels_max` (P — **not** shipped: R1's "shipped" is wrong, `fixtures.py` has none) | social, task, fight | ED-PC-0005/0006 0.15 obstacle; `10_DICE_audit_addendum_B` §5.4 term (1, A-8). The in-fight size (`CFG WOUND_ATK_OB`/`WOUND_DEF_OB`) vs the season's `wound_step`: **one ladder** — the combat module keeps its `CFG` values as the in-fight owner (a module's own rule, the scene's state), and the season level reads none of them; they are two sites of one rule, sized by one calibration (PC lane's batch) | PC rewrite lane: `U5b_PC_residue` names the calibration that sets both together |
| R-28 | the ceiling | `Fixtures.obstacle_ceiling` 2, `ceiling_per_pool` (T, `:454`, `:460`); `ceiling_form` (P) | `roll.py::_chance_floor_cap` | — | — |
| R-29 | the roll's record | `margin_endings` (P) `[pool, ob, net, margin, terms, levels, leverage]`; `Margin.terms` | chronicle, GO | `room` (SC-P1 body) → `terms`, `levels` (1, C-06) | SC rewrite lane: body |
| R-30 | the reason trail | `fed_by` on `sigma.resolve`'s record (P) | GO sheet, chronicle | `10_DICE_believed_odds…` Edit D's `roll:` field (merged) | DICE rewrite lane |
| R-31 | `band_odds` | `sigma_leverage.band_odds` (T, `:345`), the closed form of the one sampler | odds shown and believed | whole-dice figures `(0.74, 0.19, 0.07, 0)` void (1, A-5) | U4 marks the figures |
| R-32 | `task_fraction` | `rosters.yaml: task_fraction` (P) `{Failure 0, Partial 0.5, Success 1, Overwhelming 1}` | `effects_shared.graded_amount` | `effect_share`, `band_entry` (1, C-23) | VERBS rewrite lane |
| R-33 | resolution classes | `rosters.yaml: graded_tasks` (P, renamed from `graded_inquiries` T), `bookkeeping_verbs` (P); verb rows' `contests:` (T) | the fold | `graded_acts`, `graded_routes` (4, D-U1-11i) | 18-A renames once |
| R-34 | the scene budget | `Fixtures.scene_budget` 5 (T, `:228`) | the fold, GO | — | — |
| R-35 | the one sampler's key | `H(seed, tick, subject, purpose)` (`04` D-35); `engine/dice_engine/draw.py` (P*) | every draw | per-round `random.Random` streams (PB); a recorder (1, A-30) | GO and PC rewrite lanes |
| R-36 | the float functions | `engine/dice_engine/fmath.py` (P*) | every transcendental site | `weapon_physics._ltr_sum` (5) | GO lane |

### 4.2 · Capability (schema and content; the architecture file is the plan)

| # | fact | owner | consumers | competing home → decision (step) | removal edit |
|---|---|---|---|---|---|
| C-01 | what a capability is | `references/descriptor_registry.yaml: capabilities` (P; file T) → `descriptors.json` → `descriptors.CAPABILITIES` (P) | `data/cast.py`, `pool.py`, the port | `rosters.yaml: tables.capabilities` (DICE map §B); `verb_capability`/`vocation_attribute` (FA body, SE) (4, 5; D-U1-07) | CAP A1/A3 |
| C-02 | closed sets of the definition | `capabilities.kinds [skill, aptitude, trait]`, `grows_by [train, practice, use, fixed]`, `untrained [default, none]` (P) | the exporter's validator | CORE Edit 1 body (`attribute` kind; `growth_rules`; `untrained_rules` with `attribute`) stale (1, A-7) | CORE rewrite lane: body to the head |
| C-03 | the held-rank scale key | `scale: [floor, ceiling]` (P) | `data/cast.py`, `raised_capability` | CORE's `{floor:, ceiling:}` shape (5: one shape) | CORE rewrite lane |
| C-04 | which capability a verb tests | `verb_table.yaml` row `capability:` (P) | derived `VERB_CAPABILITY` (`data/verbs.py`) | `rosters.yaml: verb_capability` (T; B adds three) (4, D-U1-07) | CAP A2/A3 deletes the roster and moves lane A's values |
| C-05 | the attribute a capability starts from / is opposed by | definition row `base`, `opposed_by` (P) | the `edge` reader (talent) | `rosters.yaml: vocation_attribute` (T) incl. `opposed_by: {}` (4) | CAP A3 deletes it |
| C-06 | roles | `rosters.yaml: capability_roles` (P), ten | the loader | — | — |
| C-07 | sites | `rosters.yaml: capability_use_sites` (P), a map site → its one reader (architecture §3) | the loader | DICE map list; `applied_by: module` column (UPR §2 edit 5) → the site's `reader:` cell (5) | PC rewrite lane: UPR §2 edit 5 uses the site row |
| C-08 | the uses | `rosters.yaml: tables.capability_uses` (P) | every site reader | CHAR's `use, key, form, gain` table (1, C-U5a-08) | CHAR rewrite lane: body |
| C-09 | the verb → capability values | `interrogate: inquiry`, `lie: deception`, `determine: law`, `arrest: arms`, `march: none` (U1 §5) | — | lane A `determine: argue` (B) is the interim until `law`'s row exists | CAP A2 |
| C-10 | social rows | `deception`, `law`, `insight` | SC | `rhetoric` (D-U1-03) | SC rewrite lane |
| C-11 | `command` | definition row (P, `27_MB_A` §1) | the `field` site, MILITARY_D's army verbs | `MassBattleInput.command` literal 4; `derive_command` (5, D-U1-11g) | MB lane |
| C-12 | CHAR traits | `moved_by_evidence`, `moved_by_consequence`, `moved_by_authority`, `moved_by_solidarity` (P), seated from `npc_registry.yaml: resonant_style` (T) | `told_claim_credit`'s `edge` rows | — | — |
| C-13 | `healing` | definition row (P, PC's `tend`) | `tend`'s task site | — | — |
| C-14 | the Thread gate | `practitioner_stats: prac.thread_sensitivity` (T); fixture `thread_sensitivity_gate` (T) | `own_state_gate`, `told_retain` via `capability_admits` | a second literal read (W3) (1, A-11; C-U5a-20) | — |
| C-15 | who holds what | cast rows `stats:` (T), `capabilities:` (P), `lifepath:` (T); `tables.lifepath_templates` (T) | `data/cast.py` | `unauthored_attributes` (B) (D-U1-04) | D-U1-04 |
| C-16 | a seat's vocation | `offices.yaml` row `vocation: <capability id> | null` (P, `06_FA_office_capabilities.md` e3) | the conferee ranking (`confer_fit_weight`) | "vocation" as a word → "capability" (glossary); the key keeps its name only if it lands before the glossary edit; otherwise `capability:` | FA rewrite lane: name it `capability:` |
| C-17 | the rate role's licence | `verb_table.yaml` row `magnitude: rate` (P) | `pool.py::rate` | — (D-U1-09 narrows it) | SE rewrite lane |
| C-18 | `effect_rate_gain` | `Fixtures` (P), shipped 0 | `rate` | — | — |
| C-19 | talent's two inputs | `capability_uses` rows `edge, key: verb.base, per: mid` (P) | `advantage_sigma` | the `max(attr, have)` fold (T in `pool.py::faculty`) (1, A-7) | CAP B1 |
| C-20 | a skill grows | `grows_by` (P): `_eff_train`, `world_q.practice` (T), `_grown` (T) | — | — | — |
| C-21 | a rank's ceiling | the row's `scale` (P) | `raised_capability` | none today (no ceiling) (5) | CAP A10 |
| C-22 | `insight_bench_threshold` | `Fixtures` (P) 3 | `bench_reading` | — | — |
| C-23 | `told_claim_credit`, `choice_temper` gains | `Fixtures.competence_gain`, `temper_gain` (P) | `capability_factor` | literals under `decision/` (5) | CAP A5 |

### 4.3 · Personal combat

| # | fact | owner | consumers | competing home → decision (step) | removal edit |
|---|---|---|---|---|---|
| P-01 | nesting cap | `Fixtures.contest_nesting_cap` 1 (P; A-72) | `nested_entry` | `hol` §39.3 "no default" (Layer 1 text owed, OWED §A) | — |
| P-02 | damage scale | `modules/combat/core.py:168 DMG_SCALE` 1.07 (T file), exported | the fight | UPR §4 "a sweep reads it" → decided 1.07 (1, A-79 accepting 29) | PC rewrite lane: UPR §4 |
| P-03 | approach set | `modules/combat/vocabulary.py: APPROACHES` (P) `('defensive','normal','aggressive')`, phases `('measure','exchange','bind')` | the fight, `choice_sourced` | PA's order (superseded); LACUNA's `calm/press` under the same `choice_sourced` key → LACUNA's key is `questioning` (5) | FI/LACUNA rewrite lane: rename the key |
| P-04 | approach coefficients | `modules/combat/config.py CFG` (T file) | — | — | — |
| P-05 | `fight_endings` | `rosters.yaml: fight_endings` (T) `[felled, yielded, undecided]` + `prevailed` (P, D-U1-11a) | `Event.ending` | `standing` (5) | PC rewrite lane |
| P-06 | combat outcome record | `queries/inputs.py::CombatOutcome` (P) | effects | PB's `DuelRoundOutcome` (merged) | — |
| P-07 | round state | `queries/inputs.py::DuelState` (P) `{cumulative_damage, stamina, conc, poise, form}` | the round | `form` survives or not (PF vs PL) → **U3** (an order/contradiction) | — |
| P-08 | the round's typed input | `DuelRoundInput` (P) carries `scores, addends, pool_add, pool_floor, opposition_rate` | `nested_entry` | `faculties` (D-U1-08) | PC rewrite lane |
| P-09 | weapon records | `modules/combat/weapons.py` (T) + `combat_engine_v1.json` (T); `troops.yaml: arms.<k>.mass_kg` (P*) when not in the roster; both is refused | PC, MB | — | — |
| P-10 | ARSENAL classes missing from the personal roster | (a count) | — | 5 vs 6 → **U3** | — |
| P-11 | the carry rule | `engine/substrate/combat_kit.py::carry_demand_of` (P; file T) | host input builders | inside `act_cost` (5, D-U1-11d) | PC rewrite lane |
| P-12 | `tend` | `verb_table.yaml` row owned by `14_VERBS_MATERIAL_A` §6 (C-32); `Fixtures.tend_fraction`, `tend_ob` (P) | — | PC exits Part C (1, C-32) | — |
| P-13 | mortal-wound draw | `Fixtures.mortal_wound_ob` (P, PHY_A A3) | `_eff_kill` | `mortal_ob` (HAP_A), `mortal_terms` → one name `mortal_terms` (the pool/obstacle pair), whose `mortal_wound_ob` is its obstacle member (5); its legal home is **U2/U3**'s (`25_GROUNDING`: no legal home found) | HAPPENINGS and PHYSICAL rewrite lanes |
| P-14 | lasting mark | `Fixtures.body_mark_model` (T) | — | — | — |
| P-15 | violence contexts | `rosters.yaml: violence_contexts` (T) | `fight`, `capture` | `duel` dropped (B, lane A; PHY_A A3); `enmity` added (P) | — |
| P-16 | yield thresholds | `modules/combat/config.py YIELD_OB` (T file) | the fight | — (open sweep) | — |
| P-17 | estimate samples | `Fixtures` display 400, `believed_fight_samples` 60, `believed_field_samples` 40 (P) | `fight_estimate` | — | — |
| P-18 | `arms_kinds` seeds | `rosters.yaml: arms_kinds` (T) | kits | `harness_mail → medium` (glossary: armour tier is `medium`) | — |

### 4.4 · Mass battle

| # | fact | owner | consumers | competing home → decision (step) | removal edit |
|---|---|---|---|---|---|
| M-01 | troop table | `references/troops.yaml: troops.<kind>` (P*) columns `power, discipline, morale, strength, mounted, charge, wheel, default_role, cell_cap, ranks, primary, secondary, armour, roles, training_site, min_site_condition, upkeep, pace` | the field, recruitment | `config.py` literals; `EngineConfig` (D-U1-11c) | MB rewrite lane names one exporter |
| M-02 | arms classes, ranges | `troops.yaml: classes`, `arms.<k>.range` (P*) | the field | — | — |
| M-03 | cell size, tick, bout | `troops.yaml: deployment.scale` `cell_m` 4, `tick_s` 4, `bout_ticks` 18, `max_bouts` (P*) | the field | — | — |
| M-04 | `cell_troops` | `troops.yaml: deployment.cell_troops` 16 (P*) | — | `ranks` seeds 4/3/2 vs 2/4/2 inside `04_MB_cell_hierarchy` → **U3** | — |
| M-05 | formations and posts | `troops.yaml: formations` (P*) | the field, `commander_post` | — | — |
| M-06 | standing-order cap | `battle_orders.json: standing_order_cap` (P; file T) | the manager | literal 4 (4, D-U1-11f) | MB lane |
| M-07 | order triggers, behaviours | `hierarchy/units.py::_ORDER_TRIGGER_KINDS`, `_ORDER_SAFE_FIELDS` (T) exported to `battle_orders.json` (T) | the field | — | — |
| M-08 | obedience | `troops.yaml: orders.obey` (P*) | `27_MB_A` | `26_maneuver_orders` `obey_ob` absolute (1, 27A `Folded:`) | — |
| M-09 | stand draw table | `troops.yaml: stand` (P*) | rout | — | — |
| M-10 | rally step | `troops.yaml: armour.<tier>.rally_step` (P*) | rout | — | — |
| M-11 | casualty breakpoint | `modules/mass_battle/config.py:160-183` (T file) 0.15–0.30 | rout | — (A-61 keeps it) | — |
| M-12 | side-wide friction | `MB_FRICTION_SIGMA` (T) → 0 (A-77) | — | — | `27_MB_C` deletes it when the arm passes |
| M-13 | linear band | `systems/mass_battle/sim/lanchester_signature.py:43 LINEAR_BIG_WIN_BAND` (T) | CR-12 gate, multiplier calibration | edited by two proposals → edited once, in the v12 batch that ships the multiplier at zero (OWED §B; **U3** orders) | — |
| M-14 | veterancy | `troops.yaml: veterancy` (P*) | `_eff_march` | — | — |
| M-15 | aftermath tables | `troops.yaml: aftermath` (P*), all NOT ESTABLISHED, `recuperation: off` | A-69/A-78 | — | — |
| M-16 | fatigue rows | `troops.yaml: fatigue` (P*) | the field | `MB_STAMINA_*` env (deleted by 26) | — |
| M-17 | `FieldOutcome` | `queries/inputs.py` (T) | effects, GO | D-U1-11e | — |
| M-18 | field end states | `rosters.yaml: field_degree_bands` (T) | `_eff_march` | Won/Lost/Drawn (A-3) — `Drawn` not yet a member: **U3** checks against `field_degree_bands` | — |
| M-19 | `field_walls_dr` | `Fixtures` (P) 3 | the field | — | — |
| M-20 | armies at build | `Fixtures.armies_at_build` (P) `off/empty/mustered` | `build_realm` | `army_presets` (`04_MB_playable_field_scenario` §E) (1, MIL-C) | — |
| M-21 | army record keys | `armyrecord.KEYS` (T) + `doctrine`, `footing` (P) | MILITARY verbs | — | — |
| M-22 | footing shares | `armyrecord.FOOTING_SHARE` (P) | recruitment | — | — |
| M-23 | `CommandRecord` | `queries/inputs.py` (P) | the field | `command: tuple = (4, 4)` (`04_MB_typed_outcome` §4) | — |
| M-24 | `command_span` | `troops.yaml` header (P*) | morale divisor, span check | `clamp_command` seed | — |
| M-25 | squad grid | `troops.yaml: deployment.field_exchanges, rows, files` (P*) | the squad grid | — | — |

### 4.5 · Social contest, fieldwork, scene access

| # | fact | owner | consumers | competing home → decision (step) | removal edit |
|---|---|---|---|---|---|
| S-01 | proofs | `rosters.yaml: proofs` (T) `[record, testimony, oath, confession]` | `proofs` source | precedent not added | — |
| S-02 | entry by band | `19_LACUNA_admission…` (ADM) | the case file | "any band" (EVID body), "Success or better" (FI body) (1, C-05) | SC/FI rewrite lanes: bodies |
| S-03 | ballots | `arrangements.yaml` row key `ballots` (P) default 1 | the hearing's close | G-55's 3 is an authored value | — |
| S-04 | sitting vocabulary | `rosters.yaml: issue_rungs, hearing_moves, hearing_faults` (P) | the hearing | — | — |
| S-05 | `hearing_moves.capability` | column (P), single id or map by rung | the hearing | `rhetoric` cells (D-U1-03) | — |
| S-06 | hearing fixtures | `Fixtures.sitting_exchanges`, `argument_step`, `fault_step`, `answer_ob`, `evidence_cap`, `first_heard_ob` (P) | the hearing | — | — |
| S-07 | said slants | `rosters.yaml: said_slants` (T) `[newest, valence, unshared, unshared_first]` | `tell` | FI_02 tiers `cell` (1, C-14) | — |
| S-08 | `choice_sourced` additions | `rosters.yaml: choice_sourced` (T) | `decision/options.py` | `approach` key with two value sets → `approach` (PC) and `questioning` (LACUNA) (5) | P-03's edit |
| S-09 | termed promises | `rosters.yaml: termed_promises` (P); `Fixtures.appointment_term` 2 | 28B | — | — |
| S-10 | occupying rows | derived `VerbRow.occupies` (P) | 28A | — | — |
| S-11 | rebuff kinds | `rosters.yaml: rebuff_kinds` (P) | 28C | — | — |
| S-12 | relation grounds | `rosters.yaml: relation_grounds` (P) `[kin, oath, service, patronage, rivalry, feud]` | `_bond` | — | — |
| S-13 | scar fixtures | `Fixtures.scar_season_cap` (P) domain `None/element/person`, `scar_hold`, `scar_lean_floor`, `scar_primary_mass`, `scar_vindication` | the scar | `scar_season_cap` per element only (1, C-U5a-06) | — |
| S-14 | `STANCE_MAX` | `data/cast.py` 25 (T) | regard, `stance_toward` | — | — |
| S-15 | the score terms | `decision/choose.py::score_terms` `(pursuit, stance, aim, risk)` (T) | voices | `ATTRIBUTED_TERMS` names two (CHAR rewrite lane adds `aim`, `risk`) | CHAR rewrite lane |
| S-16 | decider API | `queries/inputs.py::PlayHost(persons, deciders)` (P) | hearing, negotiation, scene | one `decide` (1, C-U5a-04) | — |
| S-17 | who is present to me | `person_q.present_persons` (P) | SOCIAL1_A, FI_02, SOCIAL2_A | (1, C-19) | — |
| S-18 | who holds that seat as I know it | `person_q.holders_named`; `seed_seat_news` (P) | SOCIAL2_B, FI_01 | (1, C-20) | — |
| S-19 | covert kinds | `rosters.yaml: covert_kinds` (T, `[record.forged]`) | trails | `person.died`, `body.changed`, `person.captured` (FI_C) vs `store.sabotaged`, `holding.seized`, `rung.seized` (PROC_C, GAME) → one list, Event-kind names checked against `data/verbs.py::EVENT_KINDS` at load (5); which members: **U3** | the loader refuses a non-Event-kind member |
| S-20 | knowledge kinds | `rosters.yaml: knowledge_kinds` (T) | `told_retain` | — | — |
| S-21 | conclusions | `reconstruct` is an inquiry; the committed conclusion is the maker's `utter` (1, C-22) | — | MAT_E's minted Proposition | VERBS rewrite lane |
| S-22 | `finding_terms` | `rosters.yaml: finding_terms` (T) owns what a look teaches by band | inquiries | three rules (1, C-24) | — |
| S-23 | prize roster | `rosters.yaml: contest_subsystems.prizes` (T) + `a verdict, a seat, a holding, a task` (P) | the seam | `an order`, `a cover` not added (1, C-25) | — |
| S-24 | seat-row keys | `offices.yaml` rows / `Office` (T): `id, post, rung, remit_acts, scope_rung, binds, conferral, revocation, upkeep` (T) + `term` (P, `06_FA_seat_terms…`), `vocation` (P, C-16), `modifier` (P, D-U1-01a), A-13's `passes_through`, `hand_term`, `audit_at_exit` (P, institutions), `dignity`, `patronage`, `eligible_from`, `cooling_off` (P, institutions) | the gate, `confer`, the composer | `Office.term` field vs `Tenure.term?` (`04` §B.8): the seat row's `term:` is the **default** a conferral writes onto the Tenure's `term?`, not a second store (3) | FA rewrite lane |
| S-25 | `read_to_addressee` | `rosters.yaml` (B) `{challenge: [challenge], dispensation: [issue]}` | `witness.addressee_reads` (B) | `record_kinds.dispensation.public_terms` (4, 5; D-U1-05) | D-U1-05 edits |
| S-26 | `observation_terms` | `rosters.yaml: observation_terms` (T) | WITNESS | `fell_to`, scene-shape predicates, `draw:<name>` join it (D-U1-06) | PC/MB rewrite lanes |

### 4.6 · Faction actions, settlements, world, institutions

| # | fact | owner | consumers | competing home → decision (step) | removal edit |
|---|---|---|---|---|---|
| F-01 | seat terms | `offices.yaml` row `term:` (P) | `confer`, `succeed` | 8 (first authoring, withdrawn) vs 4 (`_B`) → `_B`'s rows (1, its head) | FA rewrite lane: body of the first |
| F-02 | head seats | `rosters.yaml: factions.<f>.head_seat` (P; `factions` T) | `30_WR_A`, `31_WR_A`, revocation | — | — |
| F-03 | remit acts | `offices.yaml` `remit_acts` (T) | the gate | — | — |
| F-04 | founded-seat defaults | `offices.yaml: founding:` (P) | `found` | — | — |
| F-05 | `confer_fit_weight` | `Fixtures` (P) | `confer` | — | — |
| F-06 | `recall_suspicion` | `Fixtures` (P) 3 | `revoke` | — | — |
| F-07 | the writ's kind | `record_kinds.dispensation` (T) | `issue`, `comply` | `writ` rename (D-U1-11h) | FA rewrite lane |
| F-08 | a war is live | `state/gate.py::may_wage` + `world_q.at_war` (P) | land, strife | — (A-20) | — |
| F-09 | seats pass with land | gate basis `conquest` (P) + `_take_hold` (T file) | land | — (A-58) | — |
| F-10 | the entry draw | `_eff_march` + `world_q.parliament_sits` (P); `Fixtures.entry_draw`, `parliament_reading` (P) | land | `30_WR_A` "pairwise only" vs A-85's strife level → A-85 (1) | WR rewrite lane |
| F-11 | revocation by the head | `rosters.yaml: revocation_bases` (T) + `head_of_faction` (P); `state/gate.py::REVOCATION_RULES` (T) | `revoke` | — (A-35) | — |
| F-12 | political weight of a territory | **a table keyed by territory id** in `rosters.yaml: tables.territory_weight` (P) (`Rung` field forbidden, R3 §1) | `faction_q.weight`, `31_WR_C`, cohorts | "a `weight:` key on territory rungs' authoring rows" (5) | FA/WR rewrite lanes |
| F-13 | store-move shares | `rosters.yaml: amount_shares` (T, `[1000]`) per-mille | `transfer` | — | — |
| F-14 | endowment by territory | `rosters.yaml: site_endowment` (P) | the economy | — | — |
| F-15 | granary location | `world_q.treasury_above` (P) | relief | every territory rung (superseded) | SE rewrite lane |
| F-16 | settlement arms | `Fixtures.endowment_mode`, `granary_seasons`, `larder_walk`, `famine_loss`, `hunger_loss`, `regrow_seasons`, `standing_ration`, `arrival_report` (P) | settlements | — | — |
| F-17 | cohort heavy moves | `rosters.yaml: cohort_moves` (P) `[petition, migrate, work, tend, comply, "evade / defy", riot]` | cohorts | — (A-56) | — |
| F-18 | verb roster | `verb_table.yaml` (T) | the fold | 67/68/69 → **U3** | — |
| F-19 | thread operations | `rosters.yaml: thread_operations` (P) | threadwork | — | — |
| F-20 | thread session parameters | `engine/engine_params/` typed file behind `export_engine_params.py --check` (P) | threadwork | — | — |
| F-21 | weather spell | `Fixtures.season_spell_draw` (P) | weather | body vs head (A-54) → head | WR rewrite lane |
| F-22 | era vocabulary | `rosters.yaml: era_rule_standings`, `era_conditions` (P) | eras | — | — |
| F-23 | strand link rule | `Fixtures.strand_links`; `world_q.STRAND_RECENT` (P) | strands | `harness/strife.py::LINK_WINDOW` rebinds → reads the owner | WR lane |
| F-24 | terminal degrees | `world_q.CONCLUDING_DEGREES` (P) | strands | — | — |
| F-25 | opinion axes | `descriptor_registry.yaml: affiliation_roster` (T) + `31_WR_A`'s five (P) | regimes | `30_WR_G`'s three (1, its head) | WR rewrite lane: bodies |
| F-26 | regime cores and links | `rosters.yaml: regime_cores`, `tables.opinion_links` (P) | regimes | — (A-87–A-91) | — |
| F-27 | sway/custom parameters | `Fixtures` (P) | regimes | — | — |
| F-28 | thrust poles | `rosters.yaml: thrust_axes.bears` (P; `thrust_axes` T) | thrusts | — | — |
| F-29 | the year | `rosters.yaml: seasons_of_year` (P) | D-U1-10 | D-U1-10 | D-U1-10 |
| F-30 | legibility | `person_q.legibility`; `Fixtures.legibility_curve` (P) | A-43 | — | — |
| F-31 | LOOP rows | `hole_register.yaml` (T) | — | ids: **U3** (H-275 collision) | — |
| F-32 | durable write | `30_WR_D` §3's definition, carried by `write_matrix.yaml` (T) cells | `null_scenes` | — (A-81 `[ASSUMPTION]`) | — |
| F-33 | `provisional_term` | `Fixtures` (P) | regency, BIND_C | 2 (BIND_C) vs 4 (BYZ_A): **U3** (a value, not a home) | — |
| F-34 | `presumption_gain` | `Fixtures` (P) | legitimacy | ships 0 (SYN_B) vs 0.5 (BYZ_A): **U3** | — |
| F-35 | instrument forms | `engine/season/instruments.yaml: forms` (P*) | instruments | count 16/17: **U3** | — |
| F-36 | arrangement keys | `data/arrangements.py::_ARRANGEMENT_KEYS` (T file) + `quorum_share` (P) | arrangements | exclusive vs combinable with `quorum` → PAP_G (1) | — |
| F-37 | Church electorate | two electors (A-36's consequence; plan row `v11_part12.md:366`) | conclave | four (PAP_B gate) (1) | institutions rewrite lane |
| F-38 | successions | `rosters.yaml: successions` (T) | eight readers (25 G-28) | set shape (A-19) | FA rewrite lane |
| F-39 | obligation term | `obligation` member (institutions to place) or `oath_step`/`pledge_step` (withdrawn) | the composer | one member (OBS refusals; institutions place it) | institutions rewrite lane |
| F-40 | stakes | `rosters.yaml: stakes` (P) `body, stores, standing` | task failures | the member `standing` here means a stance row cell `(Person, stance)` → rename `regard` (5; standing reserved, §3) | DETERMINISM rewrite lane |
| F-41 | `cast_quota`, `cast_cap`, ages | `engine/season/worldgen.yaml` (P*) | world generation | ages counted in seasons read `len(SEASONS_OF_YEAR)` (D-U1-10) | PROCEDURAL rewrite lane |
| F-42 | birth and age | `Fixtures.birth_rate`, `majority_age`, `illness_rate` (T), `age_step` (T) | A-15, A-75 | `16_PESSIMIST_WR_C`'s `illness_step`, `illness_pool_base`, `age_band` vs HAP_A's bout fixtures: **one set**, HAP_A's (22_HAPPENINGS_A is the later, carrying proposal of A-15) (4) — the two writers of `Person.born` (WR_C, HAP_A) → HAP_A's (4) | WR rewrite lane withdraws WR_C's fixtures and its `born` write |
| F-43 | crisis switch | `Fixtures.crisis_arm` `rule/drawn` (P) | `_conviction_crisis` | `crisis_draw: off/on` (CHAR_A) → `crisis_arm` (20_NARR_E names it; one switch) (5) | CHAR rewrite lane |
| F-44 | crisis bands | `rosters.yaml: tables.crisis_bands` (P) | the crisis | — | — |
| F-45 | `occasion_grounds` | `rosters.yaml` (P) | `Question.grounds` | count 11/15/16 → **U3** | — |
| F-46 | world cards | `engine/season/world_cards.yaml` (P*) | build | "deck", "template", "set piece", "tension" → `card` (glossary) | PROCEDURAL lane |

---

## §5 · What this lane could not verify

- Consumers in the ledger are the proposals' own statements, not re-read call sites, except where a `T` owner was
  opened. Every `P`/`P*` owner is a proposed name the landing lane creates; this lane checked only that the
  file exists (`P`) or does not (`P*`).
- `R-27`'s in-fight wound sizes were not opened in `modules/combat/` (`CFG WOUND_ATK_OB`, `WOUND_DEF_OB` are cited
  from R1).
- D-U1-05 was first drafted on the assumption that only `issue` mints a `dispensation`; checked against
  `verb_table.yaml:319` it is false (`covenant` mints one too), and the decision was changed to the kind-to-verbs map
  before this file closed.
- The "Faculty" alias (glossary *faculty*): a grep of `tools/`, `engine/`, `modules/` for the quoted string `Faculty`
  found no caller; prose matching by `tools/names.py` readers (the vector audit) was not traced.
