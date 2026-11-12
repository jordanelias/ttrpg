# U1 — the capability authoring architecture: one home, one schema, one reader interface

## Status: REFERENCE (the suite's one decision on how a capability is authored; a plan, not canon; resolves nothing at runtime, CLAUDE.md §0.05)

## Read at: 601e715 (working tree), 2026-11-12. Written by the U5a closure lane (CORE, CHAR, DICE), which was charged with deciding the home. Other closure lanes cite this file; they do not restate it.

**What this settles.** Nine proposals describe pieces of one surface
(`01_CORE_capability_authoring_surface.md`, `10_DICE_capability_axiom_map.md`,
`02_CHAR_capability_uses_table.md`, `02_CHAR_capability_definitions.md`, `05_SC_capability_surface.md`,
`05_SC_hearing_capabilities.md`, `06_FA_office_capabilities.md`, `07_SE_capability_and_chooser_surface.md`,
`03_PC_person_inputs_content.md`). They agreed on the rows and disagreed on the file, on four verbs'
values, and (before Jordan's answers of 2026-11-12) on what a score is worth. This file decides each once.
The executable plan is `proposals/U5a_capability_home_and_two_inputs.md` (**CAP**); nothing here is executed.

**Jordan's answers this is written to** (`unified/DECISIONS_ANSWERED.md`): A-5 the bell curve everywhere;
A-6 score plus a base, floor five, one rule for combat and everything else; A-7 talent and training are two
inputs; A-8 a wound is a level against the roll; A-11 a capability never gates an act (Thread Sensitivity
excepted); A-12 a seat may carry a modifier; A-25 favourable circumstances raise the speaker, hostile ones
raise the obstacle; A-26 an equal opponent costs 0.4 per point.

---

## §1 · The home (decided)

One fact, one owner (UNIFICATION_BRIEF test 2). Three kinds of fact, three owners, all existing:

| fact | owner (authored head) | read through | why here |
|---|---|---|---|
| **what a capability is**: id, kind, gloss, governing attribute, what opposes it, scale, how it grows | `references/descriptor_registry.yaml: capabilities` | `tools/export_descriptors.py` (blocking `--check`) → `engine/substrate/descriptors.py` (`CAPABILITIES`, `capability(id)`) | it is vocabulary, like the ten attributes, the pursuits, the axes, the affiliations and the heritage roster, which already live there |
| **which capability a verb tests** | a `capability:` column on the verb's own row, `engine/season/verb_table.yaml` | `engine/season/data/verbs.py` (derives `VERB_CAPABILITY`, the map every reader already imports) | it is a property of the verb; a roster keyed by verb beside the table is a second place for a verb's facts (F-CORE-18) |
| **where a capability changes an outcome**: the roles and the uses | `engine/season/rosters.yaml`: rosters `capability_roles`, `capability_use_sites`; `tables.capability_uses` | `engine/season/data/rosters.py` | each row binds a season reader (a site in `engine/season/` code) and names a `Fixtures` gain: season facts, loaded by the season's one loader |
| **who holds what** | `references/npc_registry.yaml` cast rows (`stats:`, `capabilities:`, `lifepath:`); bundles in `rosters.yaml: tables.lifepath_templates` | `engine/season/data/cast.py` | unchanged |
| **magnitudes** (the pool's base and floor, the untrained score, level sizes, gains) | `engine/season/data/fixtures.py` with register rows; `LEVEL_SIGMA` in `engine/dice_engine/sigma_leverage.py` | `Fixtures`; `tools/export_sim_params.py` | unchanged owners |

`rosters.yaml` names the capability ids by the pointer it already has for registry-owned rosters
(`capabilities: {from_descriptor: capabilities}`, the `pursuit_axes` precedent), so `lifepath_templates.holds`
and `capability_uses.key` are validated against one roster. `rosters.yaml: verb_capability` and
`vocation_attribute` are deleted in the commit that lands the block and the column.

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
corpse). Grade of the column rule: MECHANICAL. Nothing in `04` is edited.

**Losing texts, reconciled.** `10_DICE_capability_axiom_map.md` §B and §G edit 1 (definition rows in
`rosters.yaml: tables.capabilities`; `verb_capability` kept as a roster) carry a `Reconciled:` line pointing
here; its roles, uses table, typed-record table and reason trail are adopted unchanged below.

## §2 · The definition row

```yaml
# references/descriptor_registry.yaml
capabilities:
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
| `base`, `opposed_by` | CORE Edit 1; MAP §B; SC's `opposed_by: none` (the stand-in) | the two inputs of §4 |
| `scale` | MAP §B; F-DICE-23 | `data/cast.py`; `loop/effects_combat.py::raised_capability` (a rank never passes its ceiling) |
| `untrained` | CORE Edit 9; MAP §B, narrowed by A-7 (§4) | the pool reader |
| `grows_by` | CORE Edit 1; MAP §B | `_eff_train`, `world_q.practice`, `_grown` |

Kinds, in the tradition's words: a **skill** is a learned rating that gives dice; an **aptitude** is a rated
knack that gives no dice of its own and acts through use rows; a **trait** is held or not (scale `[0, 1]`)
and acts through use rows. An **ability** is not a fourth kind: it is a trait or aptitude whose use row names
its scene's site (`02_CHAR_audit_addendum_B.md` §B4 (c)). A capability is never lost (no loss rule exists;
adding one is a new growth rule, which is code and a decision). A new capability is a row. The first new
rows other lanes author on this surface: `deception`, `law`, `insight` (SC, `05_SC_hearing_capabilities.md`),
`healing` (PC's `tend`), the four `moved_by_*` traits (CHAR).

## §3 · The roles and the uses table

Adopted from `10_DICE_capability_axiom_map.md` §A and §C without restating them: ten roles (`dice`,
`addend`, `opposes`, `edge`, `circumstance`, `resource`, `threshold`, `rate`, `judgement`, `gate`), each one
RPG axiom feeding one typed resolver input in one unit through one reader; one table,
`rosters.yaml: tables.capability_uses`, in which every place a capability changes an outcome is a row
(`use`, `role`, `key`, `side`, `when`, `level`, `per`, `against`, `gain`); closed both ways. The CHAR
table (`02_CHAR_capability_uses_table.md`) is this table; its `form` is implied by `role` (`judgement` is
`about_mid`, `gate` is `at_least`). Six amendments, each forced by an answer or by a contradiction between
lanes:

1. **`key` gains two selectors** beside a capability id, a registry key and `verb`: `verb` now means the
   *trained rank* of the capability the verb's row names, and `verb.base` means that capability's
   *governing attribute* (the talent). A-7 needs both addressable.
2. **`per` gains `mid`** beside `held` and `rank`: signed steps of the held value from its scale's
   mid-point (above counts for the side named, below counts against). It is how an attribute acts as
   levels (§4). One comparison in the `edge` reader.
3. **`against: true` has one meaning**, which `02_CHAR_which_ground_moves_whom.md` left to the builder: the
   row's levels count against the **roller** (the act's actor). `against: false` (the default) counts for
   him. `side` says whose sheet is read, not who benefits. So a trait that hardens a hearer is
   `{side: subject, against: true}` and a susceptibility that opens him is `{side: subject, against: false}`;
   the four `moved_by_*` rows are the second form (Reconciled in that file).
4. **`circumstance` carries hostile terms only** (A-25). A favourable circumstance is an `edge` row for
   the roller. A row with a negative `gain` at role `circumstance` is refused at load. The room's
   favourable half follows SC's composer (U5c).
5. **`gate` stays closed to its one capability** (A-11): Thread Sensitivity, at two sites, each the same
   comparison against the one `thread_sensitivity_gate` fixture: `own_state_gate` (may he attempt the
   gated act) and `told_retain` (may he hold a told claim of a thread-substrate term;
   `17_CENSUS_REST_2_wiring.md` W3, Reconciled to read through `capability_admits`). No `when` key,
   `requires` stem or use row may make another capability a condition of attempting an act or of holding
   a claim; a `gate` row keyed on any other capability, or at any other site, is refused at load.
   `01_CORE_capability_authoring_surface.md` Part three is withdrawn (Reconciled).
6. **A seat's modifier is an `addend`** (A-12). Where a seat declares one (the fact on the seat is the
   institutions and FA lanes'; the Layer-1 amendment text is owed by the unification stage, not applied
   here), it reaches a roll as whole dice through `POOL_ADDENDS`, read off `Act.via`, never as a level and
   never on the obstacle. One channel per fact, so it cannot be counted twice: regard for an office-holder
   stays in the chooser's stance term and in the room's reception, and no `edge` row may read a seat.

Sites (`capability_use_sites`, closed; each is one reader): `social_roll`, `fight`, `field`, `kit`,
`settlement_effect`, `told_claim_credit`, `choice_temper`, `own_state_gate` (MAP §C), plus the sites other
lanes' proposals add on this surface: `choice_exposure` (`02_CHAR_what_an_act_risks.md`), `bench_reading`
(`05_SC_hearing_capabilities.md`), `notice` (`18_DETERMINISM_notice_is_a_draw.md`), `task`
(`18_DETERMINISM_task_draw_for_uncontested_verbs.md`), `told_retain` (`17_CENSUS_REST_2_wiring.md` W3). A
new site is a new reader and a new roster member.

## §4 · The roll: two inputs, one pool rule, one sampler

Every `static` contest and every task draw, at every site, is composed the same way. The numbers named are
fixtures; their values are set by the joint calibration A-5, A-6, A-7 and A-26 call for (SC's
`13_SC_calibration.md` is the instrument; U5c), not here.

| part | rule | input (who, what) | owner of the rule | answer |
|---|---|---|---|---|
| **dice** | `pool = max(pool_floor, score + addends + pool_add)` | the roller's **training**: the trained rank of the verb's capability, else the untrained score | `seam/wrappers/pool.py` (one function; the `dice` row of every site names the same two fixtures) | A-6. `pool_add` and `pool_floor` start at combat's 6 and 5 (`modules/combat/core.py:51-52`, the only regime ever calibrated) `[ASSUMPTION; medium; set by the calibration]`. MAP §C's four per-site fixtures become these two |
| **talent** | named levels by `per: mid` on the governing attribute: for the roller above the mid-point, against below | the roller's **attribute** (`verb.base`) | `seam/wrappers/sigma.py::advantage_sigma` (the `edge` reader) | A-7. Size per step: fixture `talent_level`, starting `minor` `[ASSUMPTION; medium]` |
| **the opponent** | `obstacle = opposition_rate × opponent's pool + hostile terms`, the opponent's pool by the same pool rule on his own training (no practice addend) | the subject's **training** | `sigma_leverage.opposed_ob`, one function | A-26: `opposition_rate` is `MU_PER_DIE` (0.4), applied to the pool so that an even contest is even under A-6. `05_SC_opposed_obstacle_parity.md` is the carrier (U5c) |
| **the opponent's talent** | levels against the roller, `per: mid` on the subject's `opposed_by` attribute (else `base`) | the subject's **attribute** | the same `edge` reader | A-7 |
| **nobody opposite** | the same rule against an ordinary person's pool (`16_PESSIMIST_DICE_task_difficulty_and_throughput.md` (a)); a capability whose `opposed_by` is `none` takes it too | — | `roll.py::obstacle` | — |
| **the situation** | hostile terms add to the obstacle; favourable ones are levels for the roller | `circumstance` and `edge` rows | `roll.py::obstacle`; `advantage_sigma` | A-25 |
| **a wound** | a level against the wounded roller, in the signed channel | `Person.body` against its ceiling | `advantage_sources: wounds` (`10_DICE_advantage_sources_for_the_arcs.md` Edits A–D) | A-8. The obstacle-term form (`10_DICE_audit_addendum_B.md` §5.4) is withdrawn |
| **the draw** | `roll_net_continuous(pool) + net_boost(leverage, pool)` against the obstacle; `degree_from_net` on the margin | — | `engine/dice_engine/` | A-5. No whole dice, no settled margin, no fraction rule |
| **the odds shown and believed** | the closed form of the same sampler (`band_odds` keeps its name and signature and stops enumerating faces) | — | `sigma_leverage.band_odds` | A-5 |

**What A-7 retires.** The fold of the two by `max` (CR-20's "the larger of the attribute and the held
key"). Training gives dice; talent gives levels; they are never added into one number and never
substituted for one another. `untrained: attribute` is therefore removed from the closed set. Precedent for
this assignment (ladder step 4): ED-901, the one two-input regime the tree has ratified (the pool from
learned skill plus six, floor five; attributes acting through sigma), and A-6's own wording (*a skill score*
plus a base). The register's illustration of A-7 (the attribute sets the dice and the skill sets the
obstacle one is attacked against) is the other assignment; under this architecture it is a two-row edit of
`capability_uses` (swap the `key` of the `dice` and `edge` rows), with no code. It is listed for Jordan as
decided-and-reversible in `unified/U5_CONFLICTS_U5a.md` §2.

**Untrained, and acquiring a skill.** A non-holder's score is the fixture `pool_default` (H-126, Jordan's
magnitude) under `untrained: default`, and nothing under `none`. A holder's score is
`max(untrained score, rank)`, so a first rank is never a loss and `raised_capability` may mint a key
(`01_CORE_capability_authoring_surface.md` Edit 9, kept). `[ASSUMPTION; medium; revert: the never-minted rule]`.

**Unauthored talent.** A person with no authored attribute reads the scale's mid-point: zero levels
either way. The registry's `default: 1` is the sheet's floor for display and is not the roll's neutral; the
combat spec's own neutral column is the precedent (`modules/combat/attributes.py`).

## §5 · Which capability each rolled verb tests (decided across lanes)

One value per verb row. Where lanes disagreed the verb's owning lane's later proposal wins (ladder step 4),
and a new capability must have a definition row before the verb row may name it.

| verb | CORE Edit 8 | DICE edit C | SC | FA | **decided** | ground |
|---|---|---|---|---|---|---|
| `interrogate` | `inquiry` | `inquiry` | `inquiry` | `inquiry` | **`inquiry`** | unanimous |
| `lie` | `copying` | `copying` | `deception` (`05_SC_hearing_capabilities.md`, which withdraws SC's own earlier `copying`) | — | **`deception`** | the verb is SC's; a lie is not a faithful copy. Until the `deception` row is defined the row carries `capability: none` with a note (never the default by omission) |
| `determine` | `argue` | `argue` | `law` | `judgment` | **`law`** | SC and FA both author a new capability for the judge's learning under two names; one thing gets one name (UNIFICATION_BRIEF test 1). `law` is the plain word for a learned body, and `judgment` collides with the role `judgement`. `06_FA_office_capabilities.md` is Reconciled to `law` |
| `arrest` | `argue` | `arms` | CR-92's | `arms` | **`arms`** | FA (the verb's lane) and DICE agree; `capture`'s precedent |
| `march` | `none`, noted | (mass battle's) | — | — | **`none`**, noted | the field reads no person's training today; a commander's capability enters as an `edge` row at site `field` (MB's, U5b) |

The nine rows that have a value today keep it.

## §6 · Who holds what: content and the switch

- A cast row authors `stats:` (the ten, 1–7) and `capabilities: {<id>: <rank>}`
  (`01_CORE_capability_authoring_surface.md` Edit 5); a lifepath or a tradition is a bundle that may grant
  an id at a rank (`02_CHAR_capability_definitions.md` Edit 3). `data/cast.py` validates every id against
  `CAPABILITIES` and every rank against the row's `scale`, and refuses a cast-row key it does not read
  (`UNREAD_KEYS`, same proposal Edit 4).
- With two inputs, talent must be live for the roll to mean what A-7 says. `build_realm(cast_attributes=…)`
  ships **on** in the commit that authors `stats:` for the cast (today one of 46 rows authors them). The
  content is Jordan's and the CHAR content pass's; the flip is a declared hash mover (CAP Part C).
- An unauthored person is ordinary by construction (§4), so authoring one character never makes him
  easier to oppose (F-DICE-03) and never makes his first rank a loss.

## §7 · One owner for each default that was written twice

| fact | today | owner after |
|---|---|---|
| Endurance's value in a fight for an unauthored person | registry `default: 1`; combat spec `end` 4; a literal `4` at `seam/wrappers/combat.py:151` | the combat module's typed export (`engine/engine_params`, section `attributes`), read by `party_end` (CORE Edit 7) |
| the opposed divisor | `roll.py:141` and `core.py:124` | `sigma_leverage.opposed_ob` with the fixture `opposition_rate` (§4) |
| the pool's base and floor | literals in `modules/combat/core.py`; absent in the social roll | fixtures `pool_add`, `pool_floor`, carried raw on the typed inputs (MAP §G edits 4 and 8, with one pair of fixtures) |
| the level table | `LEVEL_SIGMA`, unexported | the same literal, exported (`10_DICE_exported_face_rule_and_band_edges.md` Edit D) |
| which attribute judges a told claim; the Thread-Sensitivity gate | literals under `decision/` and a dedicated stem | rows of `capability_uses` (`02_CHAR_capability_uses_table.md`) |

## §8 · The reader interface

What code outside the loaders may call. Nothing under `decision/` or a module names an attribute, a scale
constant or pool arithmetic.

```
# engine/substrate/descriptors.py (leaf; modules, the season and the port's exporter read it)
CAPABILITIES: Mapping[str, CapabilityRow]          # id -> (kind, gloss, base, opposed_by, floor, ceiling, untrained, grows_by)
capability(id) -> CapabilityRow                    # raises naming the roster

# engine/season/seam/wrappers/pool.py (host; the one pool reader)
score(w, p, verb) -> int                           # training: max(untrained score, held rank); no addend, no attribute
talent(p, verb) -> int | None                      # the governing attribute as held; None = unauthored (reads as the mid-point)
faculty(w, p, verb) -> int                         # max(pool_floor, score + addends + pool_add)

# engine/season/seam/wrappers/sigma.py (host)
advantage_sigma(fx, operands) -> float             # signed named levels: effort, wounds, and the `edge` rows (talent among them)
obstacle_term_sum(fx, operands) -> float           # hostile `circumstance` rows, in successes
# the returned record gains `fed_by`: (use, role, key, side, value, contributed) per contributing row

# engine/dice_engine/sigma_leverage.py
opposed_ob(opponent_pool, rate) -> float

# decision side (person-side; no World)
capability_factor(p, use, fx) -> float | None      # `judgement` rows; 1 at the scale's mid-point
capability_admits(p, use, fx) -> bool | UNKNOWN    # the one `gate` row
View.odds(act, bands) -> float | None              # pools and opposition are never read directly
describe(key) -> str                               # the gloss
```

Typed inputs carry the composed values and no module reads a table (`04` §A.2): `SocialContestInput.pool`,
`.opposition` (the opponent's pool), `.opposition_rate`, `.leverage`, `.obstacle_terms`;
`PersonalCombatInput.faculties`, `.pool_add`, `.pool_floor`, `.attributes`; `MassBattleInput` has no
capability row until MB authors one (the `field` site is declared and empty, so the absence is in data).

**Gate of the surface (CAP carries it).** Delete the `capabilities:` block and the load refuses; delete a
contested row's `capability:` and the load refuses naming the row; re-point `argue`'s `base` and the
talent levels of an `argue` follow the new attribute with no edit to code; plant a trait row and one
hearer's odds move and nobody else's. If any of these needs a Python edit to take effect, the surface is
not the owner.

## §9 · What each lane cites this file for

| lane | its edge on the surface |
|---|---|
| CORE | the block, the column, the derived maps, the deletions (CORE Edits 1–7 as reconciled) |
| DICE | the roles, the uses table, the typed records, `fed_by` (MAP §A, §C, §D, §G), with §3's six amendments and §4's roll |
| CHAR | `gloss`, `rank_at_least`, bundles at a rank, the cast row; the choice-side rows (`told_claim_credit`, `choice_temper`, `choice_exposure`); the susceptibility traits |
| SC | the new rows `deception`, `law`, `insight`; `bench_reading`; the composer that reads `obstacle_terms` and `opposition_rate`; the calibration of §4's fixtures |
| FA, institutions | the seat's modifier as an `addend` (§3 item 6); `determine: law` |
| SE | the `rate` role (`07_SE_capability_and_chooser_surface.md`, `07_SE_capability_rate_B.md`) |
| PC | `fight`'s rows; `pool_add` / `pool_floor` carried raw; abilities as rows once the lever roster is exported; an approach is an `edge` row, never a pool rule |
| MB | the first rows of the `field` site: a commander's capability as an `edge` row; a troop type's `strength` as the `threshold` row's second holder |
| FI, WR | `notice` and `task` as sites; a finding names the faculty that surfaced it through `fed_by` |
| GO | the sheet shows `gloss`, rank, talent and the terms of `fed_by`; R-09's by-person conjunct is this surface's execution gate: *two actors at different pools: yes* on a non-combat verb in `aperture`, with no monkeypatched addend |

## §10 · What this does not decide

The values of `pool_add`, `pool_floor`, `talent_level`, `opposition_rate` at ship (the calibration's);
Health's form and the other derived resources (Jordan's AR-58, open); the form of fortune in a field (D-34);
the content of any cast row; the Layer-1 amendment text for A-12 (owed by the unification stage).
