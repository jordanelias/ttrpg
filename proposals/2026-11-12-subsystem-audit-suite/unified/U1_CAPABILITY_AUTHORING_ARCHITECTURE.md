# U1 — the capability authoring architecture: one home, one schema, one reader interface

## Status: REFERENCE (the suite's one decision on how a capability is authored; a plan, not canon; resolves nothing at runtime, CLAUDE.md §0.05)

## Read at: 601e715 (working tree), 2026-11-12. Written by the U5a closure lane (CORE, CHAR, DICE), which was charged with deciding the home. Other closure lanes cite this file; they do not restate it.

Reconciled: 2026-11-12, unification lane U1 (wave 2; `unified/U1_OWNERS_AND_VOCABULARY.md`, decisions `D-U1-nn`). Changed: §4's opposition operand is the defender's **trained score**, never his pool, with the even line a term of the social composer only (A-79; D-U1-02; lane 29's one-word amendment, OWED §B); §3 item 6 is rewritten — a seat's modifier is the `office` leverage source read off the seat row's `modifier:`, never dice, and a seat above the actor's stands against an act only as `rank_gap` (D-U1-01, which also strikes OBS §3's defender column); `rhetoric` is not created (D-U1-03); the pool rule gets one pure owner and the fight carries `scores` and `addends` in place of `faculties` (D-U1-08); `rate` reads the score and yields to the `task` site on a drawn row (D-U1-09); `capability_use_sites` names each site's one reader, so a module-applied row needs no `applied_by` column; the site rows of FI, SE, WR and MB are written out (§3); implementation lane A's unmerged branch (`e5d6ab9`, `c5bf18a`) is placed: its `verb_capability` rows, `unauthored_attributes` and `task_difficulty` are interim and retire at named batches (D-U1-04, D-U1-07); §11 adds the coding instructions (files, symbols, order, schema, call sites, tests, check, falsifier, movers, tier). Re-verified against the tree: the registry has no `capabilities` block today; `tools/export_descriptors.py --check` exists and is blocking in CI (`valoria-ci.yml:140`); `engine/substrate/descriptors.py` exposes `ATTRIBUTE_FLOOR`, `ATTRIBUTE_CEILING`; `pool.py::faculty` (`:78`) still folds `max(attr, have)`.

**What this settles.** Ten proposals describe pieces of one surface
(`01_CORE_capability_authoring_surface.md`, `10_DICE_capability_axiom_map.md`,
`02_CHAR_capability_uses_table.md`, `02_CHAR_capability_definitions.md`, `05_SC_capability_surface.md`,
`05_SC_hearing_capabilities.md`, `06_FA_office_capabilities.md`, `07_SE_capability_rate_B.md`,
`03_PC_person_inputs_content.md`, `27_MB_A_command_and_the_obedience_draw.md`), with FI's and WR's needs stated as
sites (`18_DETERMINISM_notice_is_a_draw.md`, `09_WR_threadwork_module.md`). They agreed on the rows and disagreed on
the file, on four verbs' values, on the seat's channel and on what the opponent contributes. This file decides each
once. The executable plan is `proposals/U5a_capability_home_and_two_inputs.md` (**CAP**), as amended by §11.

**Jordan's answers this is written to** (`unified/DECISIONS_ANSWERED.md`): A-5 the bell curve everywhere;
A-6 score plus a base, floor five, one rule for combat and everything else; A-7 talent and training are two
inputs; A-8 a wound is a level against the roll; A-11 a capability never gates an act (Thread Sensitivity
excepted); A-12 a seat may carry a modifier; A-25 favourable circumstances raise the speaker, hostile ones
raise the obstacle; A-26 an equal opponent costs 0.4 per point; A-54 a steward's skill bears on the harvest draw;
A-59 command from a learned skill and social/mental attributes; A-71/A-79 one opposition rule for fight and argument,
on the trained score.

---

## §1 · The home (decided)

One fact, one owner (UNIFICATION_BRIEF test 2). Kinds of fact and their owners:

| fact | owner (authored head) | read through | why here |
|---|---|---|---|
| **what a capability is**: id, kind, gloss, governing attribute, what opposes it, scale, how it grows | `references/descriptor_registry.yaml: capabilities` | `tools/export_descriptors.py` (blocking `--check`) → `engine/engine_params/descriptors.json` → `engine/substrate/descriptors.py` (`CAPABILITIES`, `capability(id)`) | it is vocabulary, like the ten attributes, the pursuits, the axes, the affiliations and the heritage roster, which already live there |
| **which capability a verb tests** | a `capability:` column on the verb's own row, `engine/season/verb_table.yaml` | `engine/season/data/verbs.py` (derives `VERB_CAPABILITY`, the map every reader already imports) | it is a property of the verb; a roster keyed by verb beside the table is a second place for a verb's facts (F-CORE-18) |
| **how hard the verb's task is** | a `difficulty:` column on the verb's own row (a member of `rosters.yaml: difficulty_levels`); level sizes `Fixtures.difficulty_ob` | `data/verbs.py`; `roll.py::obstacle` | the same reason (D-U1-04); lane A's `rosters.yaml: task_difficulty` retires into it |
| **where a capability changes an outcome**: the roles, the sites and their readers, the uses | `engine/season/rosters.yaml`: rosters `capability_roles`, `capability_use_sites`; `tables.capability_uses` | `engine/season/data/rosters.py` | each row binds a season reader and names a `Fixtures` gain: season facts, loaded by the season's one loader |
| **who holds what** | `references/npc_registry.yaml` cast rows (`stats:`, `capabilities:`, `lifepath:`); bundles in `rosters.yaml: tables.lifepath_templates` | `engine/season/data/cast.py` | unchanged. An unauthored attribute is **not stored**: the roll reads the scale's mid-point (§4) |
| **magnitudes** (the pool's base and floor, the untrained score, level sizes, gains, the opposition rate) | `engine/season/data/fixtures.py` with register rows; `LEVEL_SIGMA` in `engine/dice_engine/sigma_leverage.py` | `Fixtures`; `tools/export_sim_params.py` | unchanged owners |
| **the rules** (the pool rule, the opposition, the even line) | pure functions in `engine/dice_engine/sigma_leverage.py`: `pool_of`, `opposed_ob`, `even_line` | imported by the host's `pool.py` and by the modules | one rule, two callers (D-U1-08); a module may import the dice engine (`04` §A.2 provider row) |
| **a seat's modifier** | `engine/season/offices.yaml` row `modifier:` (a `LEVEL_SIGMA` name) | the `office` leverage source | a property of the seat (D-U1-01a); not a capability |

`rosters.yaml` names the capability ids by the pointer it already has for registry-owned rosters
(`capabilities: {from_descriptor: capabilities}`, the `pursuit_axes` precedent), so `lifepath_templates.holds`
and `capability_uses.key` are validated against one roster. `rosters.yaml: verb_capability` and
`vocation_attribute` are deleted in the commit that lands the block and the column; implementation lane A's three
added `verb_capability` rows (`interrogate: inquiry`, `arrest: arms`, `determine: argue`) move to the column with
`determine: law` once `law` has a definition row.

**The decision, by the ladder.** Step 4 (precedent): the tree already splits exactly this way for every
other trait of a person. The five rosters whose members are *what a thing is* are in the descriptor
registry; the tables that say *how the season uses them* (`tables.pursuit_projection`, `tables.alignment`,
`tables.affiliation_engagement`) are in `rosters.yaml` and point back with `from_descriptor:`. Step 5
(architecture): a registered module and the port may read the substrate leaf and its exported artifact and
may not read `engine/season/data` (`04` §A.2: a module reaches the season only through its typed input;
CLAUDE.md §5: a value crossing to the port sits behind an exporter's `--check`); `modules/combat/attributes.py`
already points at the registry by `registry_key`. The DICE map's reason for `rosters.yaml` ("the loader and
the closure checks are already there, and nothing is moved") is a cost argument and is met: the loaders stay,
and derive the same maps from the registry leaf.

**Layer 1, graded** (`skills/layer-conformance` Lens B). The definition block and the uses table are data a
loader validates (`04` §G.3.1, first row): conformant. The verb-row column meets two rows of `04` that pull
apart: §B.13 (*"a number that is a property of a roster member travels with the roster"*) and §C.4 (*"a verb
needing more columns is one the design has not finished thinking about"*). B4's third disposition applies:
the ambiguity is named here and the row is picked, because a required column makes a missing value a load
refusal (MECHANICAL at load) where a side roster makes it a silent default (the five undeclared rows are the
corpse). Grade of the column rule: MECHANICAL. Nothing in `04` is edited. The seat's `modifier:` departs from
`04` §B.7's STRUCTURAL *"a seat adds no verb and no modifier"* under A-12; the amendment text is drafted in
`U1_OWNERS_AND_VOCABULARY.md` D-U1-01 and applied only by Jordan.

**Losing texts, reconciled.** `10_DICE_capability_axiom_map.md` §B and §G edit 1 (definition rows in
`rosters.yaml: tables.capabilities`; `verb_capability` kept as a roster) carry a `Reconciled:` line pointing
here; its roles, uses table, typed-record table and reason trail are adopted with §3's amendments.
`06_FA_office_capabilities.md`'s body (`rosters.yaml: verb_capability`, `vocation_attribute`) and
`07_SE_capability_and_chooser_surface.md` §3–§4 are superseded by this section.

## §2 · The definition row

```yaml
# references/descriptor_registry.yaml
capabilities:
  source: "U1; A-6, A-7, A-11 (2026-11-12)"
  kinds:   [skill, aptitude, trait]           # closed. The ten attributes are defined in `attributes:` and are not re-defined
  grows_by: [train, practice, use, fixed]      # closed; each names a rule the engine implements
  untrained: [default, none]                   # closed; what a non-holder brings (§4)
  rows:
    argue:
      kind: skill
      gloss: "Makes a case to someone's face and moves them by it."    # required; refused if empty
      base: attr.social.charisma               # the governing attribute: the TALENT input of §4
      opposed_by: attr.mind.will               # optional; the attribute a person subject resists with, else `base`; `none` = nobody's rating opposes it
      scale: [0, 7]                            # floor and ceiling of the held rank
      untrained: default
      grows_by: [train, practice]
      source: "<ruling or design reference>"
```

| field | owner lane's proposal it comes from | reader |
|---|---|---|
| `kind` | MAP §B; CORE Edit 1 | the exporter's `--check` (refuses a `dice` use of a trait) |
| `gloss` | `02_CHAR_capability_definitions.md` Edit 1 | `decision/sheet.py::describe`; the reason trail |
| `base`, `opposed_by` | CORE Edit 1; MAP §B; `copying.opposed_by: none` (OBS §2) | the two inputs of §4 |
| `scale` | MAP §B; F-DICE-23 | `data/cast.py`; `loop/effects_combat.py::raised_capability` (a rank never passes its ceiling) |
| `untrained` | CORE Edit 9; MAP §B, narrowed by A-7 (§4) | the pool reader |
| `grows_by` | CORE Edit 1; MAP §B | `_eff_train`, `world_q.practice`, `_grown` |

Kinds, in the tradition's words: a **skill** is a learned rating that gives dice; an **aptitude** is a rated
knack that gives no dice of its own and acts through use rows; a **trait** is held or not (scale `[0, 1]`)
and acts through use rows. An **ability** is not a fourth kind: it is a trait or aptitude whose use row names
its scene's site (`02_CHAR_audit_addendum_B.md` §B4 (c)). A capability is never lost (no loss rule exists;
adding one is a new growth rule, which is code and a decision). A new capability is a row.

**The rows, all lanes (each lands in its own lane's commit, definition row before any verb cell or use row names it).**

| id | kind | base | opposed_by | untrained | grows_by | lane, proposal |
|---|---|---|---|---|---|---|
| `copying` | skill | `attr.mind.focus` | `none` | default | train, practice | CORE (existing vocation) |
| `argue` | skill | `attr.social.charisma` | `attr.mind.will` | default | train, practice | CORE (existing; ED-IN-0350) |
| `inquiry` | skill | `attr.mind.acuity` | `attr.mind.will` | default | train, practice | CORE (existing) |
| `arms` | skill | `attr.body.agility` | — | default | train, practice, use | CORE (existing; `vocation_attribute` row) |
| `deception` | skill | `attr.social.grace` | `attr.mind.perception` | default | train, practice | SC (`05_SC_hearing_capabilities.md`) |
| `law` | skill | `attr.mind.acuity` | — | default | train, practice | SC; FA (the judge's; `judgment` withdrawn) |
| `insight` | aptitude | `attr.social.attunement` | — | none | train, practice | SC (never rolled; `bench_reading`) |
| `command` | skill | `attr.social.charisma` | `none` | default | train, practice | MB (`27_MB_A` §1; A-59) |
| `healing` | skill | `[ASSUMPTION: attr.mind.focus; PC's tend lane names it]` | `none` | default | train, practice | PC (`tend`) |
| `moved_by_evidence`, `moved_by_consequence`, `moved_by_authority`, `moved_by_solidarity` | trait | — | — | none | fixed | CHAR (`02_CHAR_which_ground_moves_whom.md`); seated from `npc_registry.yaml: resonant_style` |

`rhetoric` is not a row (D-U1-03): the hearing's `argue` and `impugn` moves draw on `argue`, its `procedure` and
`definition` rungs on `law`. The governance capability FA proposed as `judgment` is `law`.

## §3 · The roles, the sites and the uses table

Adopted from `10_DICE_capability_axiom_map.md` §A and §C: ten roles (`dice`, `addend`, `opposes`, `edge`,
`circumstance`, `resource`, `threshold`, `rate`, `judgement`, `gate`), each one RPG axiom feeding one typed resolver
input in one unit through one reader; one table, `rosters.yaml: tables.capability_uses`, in which every place a
capability changes an outcome is a row (`use`, `role`, `key`, `side`, `when`, `level`, `per`, `against`, `gain`,
`add`, `floor`); closed both ways. The CHAR table (`02_CHAR_capability_uses_table.md`) is this table; its `form` is
implied by `role` (`judgement` is `about_mid`, `gate` is `at_least`). Seven amendments, each forced by an answer or
by a contradiction between lanes:

1. **`key` gains two selectors** beside a capability id and a registry key: `verb` means the *trained rank* of
   the capability the verb's row names, and `verb.base` means that capability's *governing attribute* (the
   talent). A-7 needs both addressable. A row may still name an attribute key outright (the `notice` and `field`
   rows below do).
2. **`per` gains `mid`** beside `held` and `rank`: signed steps of the held value from its scale's mid-point
   (above counts for the side named, below counts against). It is how an attribute acts as levels (§4). One
   comparison in the `edge` reader. An unauthored value reads as the mid-point (zero steps).
3. **`against: true` has one meaning**: the row's levels count against the **roller** (the act's actor).
   `against: false` (the default) counts for him. `side` says whose sheet is read, not who benefits. So a trait
   that hardens a hearer is `{side: subject, against: true}` and a susceptibility that opens him is
   `{side: subject, against: false}`; the four `moved_by_*` rows are the second form.
4. **`circumstance` carries hostile terms only** (A-25). A favourable circumstance is an `edge` row for the
   roller. A row with a negative `gain` at role `circumstance` is refused at load. Its sum is the obstacle roster's
   member `capability` (OBS §2 member 9).
5. **`gate` stays closed to its one capability** (A-11): Thread Sensitivity (`prac.thread_sensitivity`), at two
   sites, each the same comparison against the one `thread_sensitivity_gate` fixture: `own_state_gate` (may he
   attempt the gated act) and `told_retain` (may he hold a told claim of a thread-substrate term; also the reader
   by which a ground crossing reaches only sensitive witnesses, `12_ARCS_substrate_as_ground.md` item 4). No
   `when` key, `requires` stem or use row may make another capability a condition of attempting an act or of
   holding a claim; a `gate` row keyed on any other capability, or at any other site, is refused at load.
   `01_CORE_capability_authoring_surface.md` Part three is withdrawn (Reconciled).
6. **A seat is not a capability and has no use row** (A-12; D-U1-01, superseding this item's earlier
   "a seat's modifier is an `addend`"). The seat the actor exercises (`Act.via`) helps him through the leverage
   source `office` (`rosters.yaml: advantage_sources`), whose host function reads that seat row's `modifier:` (a
   `LEVEL_SIGMA` name) and returns it as one level for the actor where the act is heard by a bench or body he sits
   on or presides over (OBS §3's condition). A seat held above the actor's by the person acted on stands against
   the act as the obstacle term `rank_gap` (OBS §2 member 6). Nothing else: no dice, no defender-side `office`
   level, no `edge` row reading a seat; regard for an office-holder stays in `regard` (stance rows) and in the
   chooser's stance term. One seat, one channel per side, so it cannot be counted twice.
7. **`capability_use_sites` is a map from a site to its one reader** (a host function, or a typed-input field the
   module applies), replacing the list form and `03_PC_*`/UPR §2 edit 5's `applied_by: module` column: a row is
   read by the site's reader and by nothing else, so who applies it is a fact of the site, said once.

**The sites** (`capability_use_sites`, closed; each one reader):

| site | reader | rows (role · key · side) | lane |
|---|---|---|---|
| `social_roll` | `seam/wrappers/sigma.py::contest_input` | `dice · verb · actor` (`add: pool_add, floor: pool_floor`); `opposes · verb · subject`; `edge · verb.base · actor · per: mid · level: talent_level`; `edge · verb.base · subject · per: mid · against` (reads `opposed_by` where named); `circumstance` rows by `when` | SC, IN |
| `task` | the task route's input builder (`18_DETERMINISM_task_draw_for_uncontested_verbs.md`) | as `social_roll`, with `opposes` reading the stand-in (nobody opposite) | IN, verb lanes |
| `fight` | `seam/wrappers/combat.py::combat_input` → `PersonalCombatInput` (applied by the module) | `dice · verb · each`; `opposes · verb · each`; `resource · attr.body.endurance · each`; `threshold · attr.body.strength · each` (the carry shortfall, D-U1-11d); `edge · attributes · each` carried raw on `.attributes` and applied by the module's own sigma (`wrapper.py:316-320`) | PC |
| `field` | `seam/wrappers/mass_battle.py::command_record` → `CommandRecord` | `dice · command · each`; `edge · attr.social.charisma · each · per: mid`; `edge · attr.mind.acuity · each · per: mid` (`27_MB_A` §1, each `level: talent_level`); `threshold` for a troop kind's `strength` is the troop table's, not a person's | MB |
| `notice` | WITNESS's per-holder projection built at the barrier (`18_DETERMINISM_notice_is_a_draw.md`, C-U5a-14) | `dice · inquiry · actor`; `edge · attr.mind.perception · actor · per: mid` `[ASSUMPTION; medium; the FI lane confirms: noticing in passing is the fieldwork skill with Perception as its talent, AR-24]` | FI |
| `kit` | `combat_systems.act_cost`'s caller (host-side shortfall) | `threshold · attr.body.strength · each` | PC |
| `settlement_effect` | the place's seasonal draw (`09_WR_world_motion` / A-54) | `edge · <the work's capability> · steward · per: mid` — the steward (holder of the seat whose rung is the place's treasury rung) adds levels to the **place's** draw; the place, not the steward, is the roller (D-U1-09) | SE |
| `rate` sites (`labour`) | `pool.py::rate` | `rate · verb · actor · gain: effect_rate_gain`, only on a row with `magnitude: rate` that is **not** a task row (D-U1-09) | SE |
| `thread` | the threadwork host builder → `WorkingInput`/`Practitioner` (applied by the module) | `edge · attr.mind.focus · actor`; `resource · attr.mind.will · actor` (thread fatigue's scale, `fatigue_scale_per_will`) `[ASSUMPTION; medium; the WR lane confirms against `09_WR_B_threadwork_session_and_practitioner.md`]` | WR |
| `told_claim_credit` | `decision/` credit reader | `judgement · attr.social.attunement · actor · gain: competence_gain` | CHAR |
| `choice_temper` | `decision/choose.py` | `judgement · attr.mind.focus · actor · gain: temper_gain` | CHAR |
| `choice_exposure` | `02_CHAR_what_an_act_risks.md`'s reader | per that proposal | CHAR |
| `bench_reading` | `sigma.py::hearing_input` | `judgement · insight · actor · gain: insight_bench_threshold` (the threshold form) | SC |
| `own_state_gate`, `told_retain` | `capability_admits` | `gate · prac.thread_sensitivity · actor · gain: thread_sensitivity_gate` | CHAR, FI, WR |

A new site is a new reader and a new map member.

## §4 · The roll: two inputs, one pool rule, one sampler

Every `static` contest and every task draw, at every site, is composed the same way. The numbers named are
fixtures; their values are set by the joint calibration A-5, A-6, A-7 and A-26 call for (SC's
`13_SC_calibration.md` is the instrument; U5c; lane 29's tuning is the live arm), not here.

| part | rule | input (who, what) | owner of the rule | answer |
|---|---|---|---|---|
| **dice** | `pool = pool_of(score, addends, pool_add, pool_floor) = max(pool_floor, score + addends + pool_add)` | the roller's **training**: the trained rank of the verb's capability, else the untrained score; `addends` = the registered pool addends (practice; helpers) | `sigma_leverage.pool_of`, called by `seam/wrappers/pool.py::faculty` and by `modules/combat/core.py` | A-6. `pool_add` and `pool_floor` live at 6 and 5 (`modules/combat/core.py:51-52`, the only regime ever calibrated; lane 29's tuning) |
| **talent** | named levels by `per: mid` on the governing attribute: for the roller above the mid-point, against below | the roller's **attribute** (`verb.base`) | `seam/wrappers/sigma.py::advantage_sigma` (the `edge` reader) | A-7. Size per step: fixture `talent_level`, live `minor` |
| **the opponent** | `opposed_ob(score, opposition_rate) = opposition_rate × max(0, score)`, on the opponent's **trained score** (his rank in the capability the verb's row names as opposed, else the same one), never his pool: no base dice, no practice addend, no seat | the subject's **training** | `sigma_leverage.opposed_ob`, one function for both modules | A-26, A-79. `opposition_rate`: control 0.5, live `MU_PER_DIE` |
| **the even line** | the social and task composer's first term: `even_line(pool_add) = MU_PER_DIE × pool_add`; absent from the fight, whose defence layer spends the defender's base | — | `sigma_leverage.even_line` | A-79 (the base dice are never part of the opposition) |
| **the difficulty** | the verb row's `difficulty:` level, sized by `difficulty_ob` (live 0 / 0.5 / 1 / 1.5 above the even line) | — | `roll.py::obstacle` | `13_SC_tuning_tables.md` T1; OBS §4 |
| **the opponent's talent** | levels against the roller, `per: mid` on the subject's `opposed_by` attribute (else `base`) | the subject's **attribute** | the same `edge` reader | A-7 |
| **nobody opposite** | the stand-in: `opposed_ob(pool_default, opposition_rate)` on the even line; a capability whose `opposed_by` is `none` takes it too | — | `roll.py::obstacle` | C-04; `obstacle_default` is deleted |
| **the situation** | hostile terms add to the obstacle (OBS's roster); favourable ones are levels for the roller | `circumstance` and `edge` rows; OBS §2–§3 | `roll.py::obstacle`; `advantage_sigma` | A-25 |
| **a seat** | the exercised seat's `modifier:` as one `office` level for the actor; a seat above his as `rank_gap` | `Act.via`; the subject's seats | the `office` source; OBS member 6 | A-12 (§3 item 6) |
| **a wound** | a level against the wounded roller, and for the roller when the bearer defends (combat's bilateral precedent) | `Person.body` against its ceiling | `advantage_sources: wounds` (`10_DICE_advantage_sources_for_the_arcs.md` Edits A–D; 29 item 29-4 step 5) | A-8. The obstacle-term form (`10_DICE_audit_addendum_B.md` §5.4) is withdrawn |
| **the draw** | `roll_net_continuous(pool) + net_boost(leverage, pool)` against the obstacle; `degree_from_net` on the real-valued margin | — | `engine/dice_engine/` | A-5. No whole dice, no settled margin, no fraction rule |
| **the odds shown and believed** | the closed form of the same sampler (`band_odds` keeps its name and signature and stops enumerating faces) | — | `sigma_leverage.band_odds` | A-5 |

**What A-7 retires.** The fold of the two by `max` (CR-20's "the larger of the attribute and the held
key", `pool.py::faculty:96-99` today). Training gives dice; talent gives levels; they are never added into one
number and never substituted for one another. `untrained: attribute` is therefore removed from the closed set.
Precedent for this assignment (ladder step 4): ED-901, the one two-input regime the tree has ratified (the pool
from learned skill plus six, floor five; attributes acting through sigma), and A-6's own wording (*a skill
score* plus a base). The register's illustration of A-7 (the attribute sets the dice and the skill sets the
obstacle one is attacked against) is the other assignment; under this architecture it is a two-row edit of
`capability_uses` (swap the `key` of the `dice` and `edge` rows), with no code. It is listed for Jordan as
decided-and-reversible in `unified/U5_CONFLICTS_U5a.md` §2.

**Untrained, and acquiring a skill.** A non-holder's score is the fixture `pool_default` (H-126, Jordan's
magnitude) under `untrained: default`, and nothing under `none`. A holder's score is
`max(untrained score, rank)`, so a first rank is never a loss and `raised_capability` may mint a key
(`01_CORE_capability_authoring_surface.md` Edit 9, kept). `[ASSUMPTION; medium; revert: the never-minted rule]`.

**Unauthored talent.** A person with no authored attribute reads the scale's mid-point,
`(descriptors.ATTRIBUTE_FLOOR + ATTRIBUTE_CEILING) / 2` (4 on 1–7): zero levels either way. The mid-point is
derived, never stored (the precedent: `decision/options.py:1631`, `COMPETENCE_MID`, the same expression for the
told-claim credit's `about_mid`; `per: mid` reads that one constant, moved to the substrate leaf beside the bounds). The registry's `default: 1` is
the sheet's floor for display and is not the roll's neutral. Implementation lane A's `rosters.yaml:
unauthored_attributes` (2 on every key, seated by `build_realm(cast_attributes=True)`) is the interim that lets
CR-20's attribute-as-pool code read a score for everybody; it retires at §11 batch U1-B, when the attribute leaves
the pool (D-U1-04).

## §5 · Which capability each rolled verb tests (decided across lanes)

One value per verb row. Where lanes disagreed the verb's owning lane's later proposal wins (ladder step 4),
and a new capability must have a definition row before the verb row may name it.

| verb | CORE Edit 8 | DICE edit C | SC | FA | lane A (B) | **decided** | ground |
|---|---|---|---|---|---|---|---|
| `interrogate` | `inquiry` | `inquiry` | `inquiry` | `inquiry` | `inquiry` | **`inquiry`** | unanimous |
| `lie` | `copying` | `copying` | `deception` | — | (no verb row: a lie is a `tell`, `lie_verbs`) | **`deception`** on whichever row resolves a lie | the verb is SC's; a lie is not a faithful copy. Until the `deception` row is defined the row carries `capability: none` with a note |
| `determine` | `argue` | `argue` | `law` | `judgment` | `argue` | **`law`** (interim `argue` until `law`'s row lands) | one thing gets one name; `judgment` collides with the role `judgement` |
| `arrest` | `argue` | `arms` | CR-92's | `arms` | `arms` | **`arms`** | FA (the verb's lane), DICE and lane A agree; `capture`'s precedent |
| `march` | `none`, noted | (mass battle's) | — | — | — | **`none`**, noted | the field's capability enters at the `field` site, on the commander's record (`27_MB_A`) |
| `recruit`, `discharge_troops`, the army verbs | — | — | — | — | — | **`command`** | `14_VERBS_MILITARY_D` Edit 4; `27_MB_A` §1 (one rating for drilling and being obeyed) |
| `tend` | — | — | — | — | — | **`healing`** | PC; the row's owner is `14_VERBS_MATERIAL_A` §6 (C-32) |
| `restore`, `work`, `build`, `craft` | — | — | — | — | — | Jordan's content, when authored; as **task rows** they take the capability at the `task` site, not a `rate` row (D-U1-09) | SE |

The nine rows that have a value today keep it.

## §6 · Who holds what: content and the switch

- A cast row authors `stats:` (the ten, 1–7) and `capabilities: {<id>: <rank>}`
  (`01_CORE_capability_authoring_surface.md` Edit 5); a lifepath or a tradition is a bundle that may grant
  an id at a rank (`02_CHAR_capability_definitions.md` Edit 3). `data/cast.py` validates every id against
  `CAPABILITIES` and every rank against the row's `scale`, and refuses a cast-row key it does not read
  (`UNREAD_KEYS`, same proposal Edit 4).
- With two inputs, talent must be live for the roll to mean what A-7 says. `build_realm(cast_attributes=…)` ships
  **on** (lane A already flips it, B). With CAP Part B the seating of unauthored values stops (the mid-point is
  read), so the switch then gates only the authored `stats:` (the content is Jordan's and the CHAR content pass's,
  CAP Part C; a declared mover).
- An unauthored person is ordinary by construction (§4), so authoring one character never makes him
  easier to oppose (F-DICE-03) and never makes his first rank a loss. Charge 3 of implementation lane A ("Ob always
  2 is wrong") is **not met in the shipped realm** until Part C authors scores and difficulty levels (OWED §E).

## §7 · One owner for each default that was written twice

| fact | today | owner after |
|---|---|---|
| Endurance's value in a fight for an unauthored person | registry `default: 1`; combat spec `end` 4; a literal `4` at `seam/wrappers/combat.py:151` | the combat module's typed export (`engine/engine_params`, section `attributes`), read by `party_end` (CORE Edit 7) |
| the opposed divisor | `roll.py:141` and `core.py:124` | `sigma_leverage.opposed_ob` with the fixture `opposition_rate` (§4) |
| the pool rule, its base and floor | literals in `modules/combat/core.py`; `pool.py::faculty`'s own sum; absent in the social roll | `sigma_leverage.pool_of` with fixtures `pool_add`, `pool_floor`, carried raw on the typed inputs |
| the untrained score | `Fixtures.pool_default`; lane A's `unauthored_attributes` values (B) equal it | `pool_default` alone (D-U1-04) |
| a task's difficulty | lane A's `rosters.yaml: task_difficulty` (B); T13 T1 per-verb values; SC-B values | the verb row's `difficulty:` level and `difficulty_ob` (D-U1-04; OBS §4) |
| the level table | `LEVEL_SIGMA`, unexported | the same literal, exported (`10_DICE_exported_face_rule_and_band_edges.md` Edit D) |
| which attribute judges a told claim; the Thread-Sensitivity gate | literals under `decision/` and a dedicated stem | rows of `capability_uses` (`02_CHAR_capability_uses_table.md`) |
| a seat's help on a roll | U1 §3 item 6's addend; T13 T4's `standing_dice`; OBS's `office_level` | the seat row's `modifier:` read by `office` (D-U1-01) |

## §8 · The reader interface

What code outside the loaders may call. Nothing under `decision/` or a module names an attribute, a scale
constant or pool arithmetic.

```
# engine/substrate/descriptors.py (leaf; modules, the season and the port's exporter read it)
CAPABILITIES: Mapping[str, CapabilityRow]          # id -> (kind, gloss, base, opposed_by, floor, ceiling, untrained, grows_by)
capability(id) -> CapabilityRow                    # raises naming the roster
ATTRIBUTE_FLOOR, ATTRIBUTE_CEILING                 # existing; the talent mid-point is derived from them

# engine/dice_engine/sigma_leverage.py (pure; host and modules import it)
pool_of(score, addends, pool_add, pool_floor) -> int
opposed_ob(score, rate) -> float                   # the operand is a trained score, never a pool
even_line(pool_add) -> float

# engine/season/seam/wrappers/pool.py (host; the one pool reader)
score(w, p, verb) -> int                           # training: max(untrained score, held rank); no addend, no attribute
talent(p, verb) -> int | None                      # the governing attribute as held; None = unauthored (reads as the mid-point)
faculty(w, p, verb) -> int                         # pool_of(score, Σ addends, pool_add, pool_floor)
rate(w, p, verb) -> Fraction                       # about_mid on score; 1 unless the row declares magnitude: rate (D-U1-09)

# engine/season/seam/wrappers/sigma.py (host)
advantage_sigma(fx, operands) -> float             # signed named levels: effort, wounds, office, proofs, favour, …, and the `edge` rows (talent among them)
obstacle_operands(w, act, row) -> tuple            # (name, raw, step) per obstacle_terms member (OBS §1); the `capability` member sums hostile `circumstance` rows
# the returned record gains `fed_by`: (use, role, key, side, value, contributed) per contributing row

# decision side (person-side; no World)
capability_factor(p, use, fx) -> float | None      # `judgement` rows; 1 at the scale's mid-point
capability_admits(p, use, fx) -> bool | UNKNOWN    # the one `gate` capability, two sites
View.odds(act, bands) -> float | None              # pools and opposition are never read directly
describe(key) -> str                               # the gloss
```

Typed inputs carry the composed values and no module reads a table (`04` §A.2): `SocialContestInput.pool`,
`.opposition` (the opponent's trained score, or `None`), `.pool_default`, `.pool_add`, `.opposition_rate`,
`.difficulty`, `.obstacle_operands`, `.leverage`; `PersonalCombatInput.scores` and `.addends` (replacing
`.faculties`, D-U1-08), `.pool_add`, `.pool_floor`, `.opposition_rate`, `.attributes`; `DuelRoundInput` the same five
(29 item 29-5); `MassBattleInput.commanders: (CommandRecord | None, CommandRecord | None)` with
`CommandRecord(person, score, addends, levels, post, fed_by)` (`27_MB_A` §2; `levels` includes the march seat's
`office` level).

**Check of the surface (CAP carries it).** Delete the `capabilities:` block and the load refuses; delete a
contested row's `capability:` and the load refuses naming the row; re-point `argue`'s `base` and the
talent levels of an `argue` follow the new attribute with no edit to code; plant a trait row and one
hearer's odds move and nobody else's; give a seat row `modifier: minor` and only acts made through that seat
before its own body move. If any of these needs a Python edit to take effect, the surface is not the owner.

## §9 · What each lane cites this file for

| lane | its edge on the surface |
|---|---|
| CORE | the block, the two verb-row columns (`capability:`, `difficulty:`), the derived maps, the deletions (CORE Edits 1–7 as reconciled) |
| DICE | the roles, the uses table, the typed records, `fed_by` (MAP §A, §C, §D, §G), with §3's seven amendments; `pool_of`, `opposed_ob`, `even_line` (§4) |
| CHAR | `gloss`, `rank_at_least`, bundles at a rank, the cast row; the choice-side rows (`told_claim_credit`, `choice_temper`, `choice_exposure`); the susceptibility traits |
| SC | the rows `deception`, `law`, `insight`; `bench_reading`; the composer that reads `obstacle_operands`, `opposition_rate` and the even line; the calibration of §4's fixtures |
| FA, institutions | the seat row's `modifier:` read by `office`, and `rank_gap` (§3 item 6); `determine: law`; a seat's `vocation:` is spelled `capability:` (glossary) |
| SE | `rate` on non-task magnitudes; the steward's `edge` rows at `settlement_effect` (D-U1-09) |
| PC | `fight`'s rows; `scores`, `addends`, `pool_add`, `pool_floor`, `opposition_rate` carried raw; `healing`; abilities as rows once the lever roster is exported; an approach is an `edge` row, never a pool rule |
| MB | the `field` site: `command`'s definition and its three use rows, `CommandRecord`; a troop kind's `strength` is the troop table's |
| FI, WR | `notice` and `task` as sites; `thread`; a finding names the capability that surfaced it through `fed_by` |
| GO | the sheet shows `gloss`, rank, talent and the terms of `fed_by`; R-09's by-person conjunct is this surface's execution check: *two actors at different pools: yes* on a non-combat verb in `aperture`, with no monkeypatched addend |

## §10 · What this does not decide

The values of `pool_add`, `pool_floor`, `talent_level`, `opposition_rate`, `difficulty_ob` at ship (lane 29's tuning
and the joint calibration); the per-seat `modifier:` values (the institutions and FA lanes' content); Health's form
and the other derived resources (Jordan's AR-58, open); the content of any cast row; the base attribute of `healing`;
whether the in-fight wound sizes (`CFG WOUND_ATK_OB`, `WOUND_DEF_OB`) and the season's `wound_step` are set by one
calibration (PC's batch; `U1_OWNERS_AND_VOCABULARY.md` R-27).

---

## §11 · Coding instructions (workplan v12; each batch executable without re-deriving)

**Base.** Every batch takes implementation lane A's branch (`worktree-agent-a737f996de1fa4752`, `c5bf18a`) as its base
once Jordan merges it, or re-does its edits (OWED §E); the instructions below are written against that branch's
state and say where `main` differs. Run only the test files named (CLAUDE.md §0.4); the full suite once at the
batch close. Tier per CLAUDE.md §10.

### Batch U1-A · the surface in its home (hash EQUAL) — CAP Part A, as amended · IN lane · `valoria-author` on `sonnet`, `high` · cost: edit plus a small build

Order (one commit each, or one commit with each step's revert separable):

1. `references/descriptor_registry.yaml`: add the `capabilities:` block of §2 with the four existing rows
   (`copying`, `argue`, `inquiry`, `arms`) only; each `gloss` from `02_CHAR_capability_definitions.md` Edit 1.
   `tools/export_descriptors.py`: a `_capability_roster(reg)` validator beside `_heritage_roster` (refuses a kind,
   growth rule or untrained rule outside the closed sets, an empty `gloss`, a `base`/`opposed_by` outside the ten
   attribute keys or `none`, a `scale` that is not `[int, int]` with floor ≤ ceiling), added to the export dict.
   Re-derive `engine/engine_params/descriptors.json` with the tool, never by hand. `engine/substrate/descriptors.py`:
   `CapabilityRow` (a frozen dataclass), `CAPABILITIES`, `capability(id)`.
2. `engine/season/verb_table.yaml`: the `capability:` column on every row that contests or is graded, with the
   values `verb_capability` holds on the base branch (12 rows: `tell`, `speak`, `argue`, `research`, `examine`,
   `surveil`, `fight`, `accept`, `capture`, `interrogate`, `arrest`, `determine`), each `[ASSUMPTION]` note carried
   over. `engine/season/data/verbs.py`: `VerbRow.capability`; `VERB_CAPABILITY`, `VOCATIONS`, `VOCATION_ATTRIBUTE`,
   `VOCATION_OPPOSED_BY` derived from the column and `descriptors.CAPABILITIES`; the loader refuses a `capability:`
   naming no definition row, a contested or graded row with none (no default by omission; `none` is spelled), and a
   `capability:` on any other row unless it declares `magnitude: rate`.
3. Delete `rosters.yaml: verb_capability`, `vocation_attribute` and `data/rosters.py::_load_vocation_attribute`,
   `_load_vocation_opposed_by`; add `capabilities: {from_descriptor: capabilities}`.
4. `engine/season/rosters.yaml`: `capability_roles` (the ten), `capability_use_sites` (the map of §3, only the sites
   with a reader on this tree: `social_roll`, `fight`, `kit`, `told_claim_credit`, `choice_temper`, `own_state_gate`),
   `tables.capability_uses` restating today's rules as rows; `data/rosters.py::_load_capability_uses` refusing:
   an unknown site, role or key; a field the role does not take; a negative-gain `circumstance`; a `dice` use of a
   trait; a `gate` row other than `prac.thread_sensitivity` at `own_state_gate`/`told_retain`.
5. `02_CHAR_capability_uses_table.md` edits 3–5 (the two `decision/` literals become rows; `capability_factor`,
   `capability_admits`).
6. `engine/dice_engine/sigma_leverage.py`: `pool_of`, `opposed_ob`, `even_line` (29 item 29-1's two plus `pool_of`),
   no caller yet.

**Tests (new, `engine/season/tests/test_u1_capability_surface.py`).** `test_deleting_the_block_refuses_the_load`;
`test_a_contested_row_with_no_capability_is_refused_naming_it`; `test_a_capability_naming_no_definition_is_refused`;
`test_a_gate_row_on_another_capability_is_refused`; `test_negative_circumstance_gain_is_refused`;
`test_derived_vocation_maps_equal_the_retired_rosters` (the derived `VERB_CAPABILITY`/`VOCATION_ATTRIBUTE` equal the
base branch's roster values, captured as literals in the test, `==` not `approx`). `engine/tests/test_opposed_ob.py`
(29 item 29-1) plus `test_pool_of_is_the_max_of_floor_and_sum`.
**Check.** `python tools/export_descriptors.py --check` green; the two test files green;
`python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` prints the base branch's hash
(on `main`: `5405522c36b0399247f83fd9f6d29494`; on lane A's branch: re-read it before the batch and quote it).
**Falsifier.** Any of the five refusals loading; a hash that moves. **Control.** The base branch. **Hash movers.**
None. **Depends on.** `01_CORE_tests_one_golden_owner.md` (one pin file).

### Batch U1-B · the roll with two inputs (one calibrated landing; every seeded result re-pinned once) — CAP Part B, 29 items 29-2 to 29-4, OBS §4 steps 0 to 5 · IN, SC, PC lanes · `sonnet` for the edits, `opus` for reading the calibration · cost: small build and a calibration

Lands with `U5a_DICE_owed_edits.md` §1 (the one sampler). Order:

1. `seam/wrappers/pool.py`: `score(w, p, verb)` = `max(pool_default, held rank)` (the base branch's `score` with the
   attribute branch removed); `talent(p, verb)`; `faculty` = `pool_of(score, Σ addends, fx.pool_add, fx.pool_floor)`;
   delete `_authored_attribute`'s use in `faculty`.
2. `data/fixtures.py` + `hole_register.yaml` NUMBER rows: `pool_add` (0 / 6), `pool_floor` (0 / 5), `talent_level`
   (`None` / `minor`), `opposition_rate` (0.5 / `MU_PER_DIE` read from the owner), `difficulty_ob` (0/1/2/3 →
   0/0.5/1/1.5), each with a three-point sweep. Control arm = batch U1-A's bytes.
3. `rosters.yaml: tables.capability_uses`: the `dice` rows of `social_roll`, `fight`, `task` name `add: pool_add,
   floor: pool_floor`; the two `edge` talent rows per site (§3).
4. `sigma.py::_opposition_of` returns `pool.score(w, person, opposing verb)` — the trained score — for every person
   subject (29 item 29-4 step 1); `advantage_sigma` reads the `edge` rows through the signed two-list form (ADV
   Edit A); `advantage_sources` gains `capability`, `wounds` (ADV Edits B–D).
5. `verb_table.yaml`: the `difficulty:` column (every rolled row `routine`); `rosters.yaml: difficulty_levels`;
   delete lane A's `rosters.yaml: task_difficulty`, `data/verbs.py::_load_task_difficulty` and the `task` arm of
   `Fixtures obstacle_model` (OBS's control is the `stand_in`-equivalent composition). `obstacle_default` and H-127
   deleted (C-04).
6. `modules/social_contest/roll.py::obstacle`: `even_line(pool_add) + difficulty + opposed_ob(opposition or
   pool_default, opposition_rate) + Σ raw_i × step_i` (OBS §2 as folded); `terms` leads with `("even", …)`.
   `modules/combat/core.py`: `ob_from_defender(defender, cfg)` → `opposed_ob(defender.score, …)`; `resolution_pool`
   → `pool_of`. `queries/inputs.py`: `PersonalCombatInput.scores`, `.addends`, `.pool_add`, `.pool_floor`,
   `.opposition_rate` (`.faculties` deleted); `SocialContestInput.pool_add`, `.opposition_rate`, `.difficulty`.
   `seam/wrappers/combat.py::combat_input` fills them.
7. Delete lane A's `rosters.yaml: unauthored_attributes`, its loader and the seating in `build_realm`; `talent`
   returns `None` for an unauthored key.
8. Flip the live arms in the order lane 29 gives (the fight's rate first inside U5b §5 row 5; the social roll at
   OBS §4 step 5); re-pin every golden once.

**Tests.** `engine/season/tests/test_u1_two_inputs.py`: `test_training_gives_dice_and_talent_gives_levels`
(two hand-built persons, rank 5 / talent 2 and rank 2 / talent 5, read different band shares; swapping the two
`edge`/`dice` rows' keys swaps them with no code edit); `test_an_unauthored_person_reads_zero_talent_levels`;
`test_a_first_rank_never_lowers_a_pool`; `test_the_opposition_reads_the_trained_score_not_the_pool` (a subject with
practice addends and a seat: his `opposition` equals his rank). `engine/season/tests/test_cr85_faculty_replaces_history.py`
and `test_cr20_attributes.py` re-pinned (named in the commit). 29's `test_sc_calibration_targets.py` and
`tests/valoria/test_combat_opposed_rule_shape.py`.
**Check.** (1) Control: every fixture at control reproduces batch U1-A's hashes at `build_realm(0..2)`, one season.
(2) Equal trained ranks 0, 2, 4, 7 at `plain`: P(margin ≥ 0) within 0.005 of 0.5 (29 gate 6). (3) `python -m
engine.season.harness.aperture 4 0` prints *two actors at different pools: yes* on a non-combat verb only after
batch U1-C (expected **no** at this batch: every person holds the default). **Falsifier.** A first trained rank
lowering a pool; an authored character easier to oppose than an unauthored one; an attribute or a seat found in
the opposition; a favourable circumstance lowering an obstacle; a hash moving at the control arm.
**Hash movers.** Every world in which a graded act resolves; all goldens, once. **Depends on.** U1-A; lane 29 item
29-1; `U5a_DICE_owed_edits.md` §1; OBS steps 0–4.

### Batch U1-C · content and the switch — CAP Part C · CHAR content pass with Jordan · content

1. `references/npc_registry.yaml`: `stats:` and `capabilities:` for the cast (Jordan's and the CHAR pass's values).
2. `verb_table.yaml`: per-verb `difficulty:` levels beyond `routine` (Jordan's), starting with OBS §4 step 5's
   `interrogate: demanding`.
3. The new definition rows, each in its lane's commit with its first use: SC's `deception`, `law`, `insight`
   (then `determine: law`, the lie row's `deception`, `bench_reading`); MB's `command` (then `27_MB_A`'s `field`
   rows); PC's `healing`; CHAR's four `moved_by_*`.

**Check.** `decision_spread --persons` shows the cast's pools differing; `aperture 4 0` prints *two actors at
different pools: yes* on a non-combat verb; lane A's realm roll census (1,106 rolls at four seasons, 998 at
obstacle 2.0) no longer reads one obstacle in nine of ten. **Falsifier.** Authoring a `stats:` row moves no roll.
**Hash movers.** The build hash and every season hash (declared).

### Batch U1-D · the seat's modifier — FA and institutions lanes · `sonnet` · cost: edit

1. `engine/season/offices.yaml`: the optional row key `modifier:`; `state/carriers.py::Office.modifier:
   Optional[str] = None`; the offices loader refuses a value outside `sigma_leverage.LEVEL_SIGMA`.
2. `sigma.py::ADVANTAGE_SOURCES` gains `office` (its roster member in `advantage_sources`), reading `Act.via`'s
   `modifier` where the act's prize row's `heard_by` names a bench or body the actor sits on or presides over.
3. No row authors a value at landing (control: hash EQUAL). The bench seats' first values (T13 T4's) land with
   OBS §4 step 5 as a declared mover.

**Tests.** `engine/season/tests/test_u1_seat_modifier.py`: `test_a_seat_modifier_reaches_only_acts_through_that_seat`;
`test_a_seat_is_never_in_the_pool_or_the_opposition`; `test_an_unknown_level_name_is_refused`. **Check.** Hash EQUAL
at landing; a planted `modifier: minor` on one bench seat moves only that bench's rolls. **Falsifier.** A pool or an
`opposition` value that moves with a seat. **Depends on.** U1-B steps 4 and 6 (the leverage two-list form).
**Layer 1.** `04` §B.7's amendment text (D-U1-01) must be applied by Jordan before or with this batch; until then the
batch ships behind its revert (drop the column) and names the departure at `Office`'s docstring.

### Batch U1-E · the other sites — FI, SE, WR, MB lanes, each in its own proposal's batch · `sonnet` · cost: edit

Each lane adds its site to `capability_use_sites` with its reader and its rows (§3), in the commit that builds the
reader: `notice` with `18_DETERMINISM_notice_is_a_draw.md`; `task` with 18-A; `field` with `27_MB_A`; `thread` with
`09_WR_threadwork_module.md` edit 3; `settlement_effect` with the A-54 weather/harvest draw; `rate` with CP-T08-01's
`labour`; `bench_reading` with `05_SC_playable_hearing_B.md`. **Check per site.** The site's rows load; a planted
holder moves only that site's reader's output; the loader refuses the site's rows before its reader is registered.
