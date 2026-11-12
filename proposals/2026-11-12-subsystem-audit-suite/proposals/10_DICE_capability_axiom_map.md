# DICE — the capability → axiom → resolver input map, and the one surface that authors it

## Status: PROPOSED

Carries §4 of `../audits/10_DICE_audit_addendum_B.md` (findings F-DICE-15, F-DICE-17, F-DICE-18,
F-DICE-20, F-DICE-21) and the brief's §14 charge, from the resolution side. It is the interface the
holistic stage is asked to adopt, so every field has a unit and one reader. It extends the existing
owner (`engine/season/rosters.yaml`: `verb_capability`, `vocation_attribute`, `advantage_sources`; the
dice engine's inputs) and adds no second capability system. Lanes that own the edited files: IN (the
rosters, the seam's wrappers, the dice engine); CHAR (content and the choice-side rows); SC, PC, MB, SE
for the rows of their own sites. Not ratified by being written (`CLAUDE.md` §2).

## What it changes in `engine/season/` at runtime

**Part one changes nothing a season computes.** Three tables restate, as rows, rules that are code
today; the loaders derive the same maps every reader already imports; two generic door members read a
table that ships with no row for them. Same pools, same obstacles, same `World.content_hash()`.
**Part two is not in this file:** the movers it makes possible are other proposals, each with its own
control arm (§G). What part one buys is that, afterwards, a new skill, aptitude or trait and what it
does to a roll are data edits, and the question *which capabilities fed this roll, by which rule* has
an answer the engine returns.

## The problem, with evidence

1. **One score is three pools** (F-DICE-17). A person's score is read once
   (`seam/wrappers/pool.py::faculty`) and then is the pool in a social roll, itself plus six with a
   floor of five in a fight (`modules/combat/core.py:54-58`), and nothing on a field. Equal scores of
   3: Success-or-better 28.6 % in the social roll, 67.7 % in a fight (addendum E-B03). The rule that
   makes the difference is two literals inside a module. Jordan's Ruling C (2026-08-23): *"All pools
   are contained within one single document, which all subsystems call to get the appropriate pool."*
2. **One ruling on the obstacle is three obstacles** (F-DICE-15): half the held score with a stand-in;
   half of `faculty`; the opponent's rolled net.
3. **A modifier has three vocabularies** (F-DICE-21): named levels through a roster (social); bare
   sigma summed in a module (combat); die-equivalents at 0.2 sigma (field).
4. **A field reads no person** (F-DICE-18): `MassBattleInput` is equal before and after a whole side
   is raised to 7 on every attribute and key (E-B04).
5. **A capability can do one thing by data today: give dice to a verb.** Everything else a designer
   would attach to a character (a knack that helps under a condition, a trait that hardens a hearer, a
   bearing a venue rewards, strength that carries a kit) needs a Python function or a module constant.
   The doors exist (`advantage_sources`, `POOL_ADDENDS`, the room's terms) and each admits only code.
6. **Nowhere does a row say what a capability is.** `vocation_attribute` says which attribute a
   vocation starts from; kind, scale, what a non-holder rolls and how it grows are in loaders, fixtures
   and effects (`01_CORE_capability_authoring_surface.md` lists seven files).

## The resolution, decided

Ladder step 3 (Ruling C; the mean-shift, score/2 and wound rulings; ED-IN-0330's *"bundles of
skills/aptitudes … that complement character attributes"*) for what must be expressible; step 4 for
the form (`vocation_attribute` is a closed table, both ways, refused at import; `advantage_sources` is
a closed roster bound to functions; the room's operands are carried raw to the module, which composes
them). Three decisions:

- **A capability changes an outcome only by playing a role, and the roles are a closed set of ten.**
  Each role is one RPG axiom, feeds one named resolver input in one unit, and has one reader. A new
  role is a code change and a design decision; a new capability, or a new use of one in an existing
  role, is a row.
- **Every use is a row of one table** (`capability_uses`), the roll's and the choice's alike.
- **A rule's magnitude is a fixture; a rule's shape is the role.** Nothing numeric is authored in a
  module for a quantity a character's sheet feeds.

## A. The ten roles (the axioms)

`engine/season/rosters.yaml: capability_roles`, closed and ordered.

| role | the axiom, in the tradition's words | what the held value becomes | unit | resolver input it feeds | the one reader | executed today |
|---|---|---|---|---|---|---|
| `dice` | a rating gives the pool: attribute or skill, whichever is higher | the pool's base, then the site's rule (`add`, `floor`) | whole dice | `SocialContestInput.pool`; `PersonalCombatInput.faculties[i]` | `pool.py::faculty` | social, fight |
| `addend` | bonus dice from a named source (practice, help, a seat's resources) | dice added to the base | whole dice | the same fields | `pool.py::POOL_ADDENDS` | social, fight (practice only) |
| `opposes` | a static difficulty from the opponent's rating: half his score | the score the module halves | a score (dice); the obstacle is score ÷ 2, fractional | `SocialContestInput.opposition`; the defender's `faculties[i]` | `sigma.py::_opposition_of` → `roll.py::obstacle`; `core.ob_from_defender` | social, fight |
| `edge` | advantage and disadvantage in named steps, with diminishing returns | named levels, for or against | level names (`minor` 0.25, `moderate` 0.50, `strong` 0.75, `major` 1.00 sigma), summed, soft-capped at 1.5 | `SocialContestInput.leverage`; a fight's `net_sigma`; a field side's sigma | `sigma.py::advantage_sigma` → `sigma_leverage.levels_to_net_sigma` → `net_boost` | social (effort only); fight and field in their own units |
| `circumstance` | the situation moves the difficulty | a signed term on the obstacle | successes, fractional; positive is harder | `SocialContestInput.obstacle_terms` (new; today three named fields) | `roll.py::obstacle` | social (room, forgery) |
| `resource` | an attribute sizes a pool that drains (health, stamina, composure) | the size of a resource | resource points | `Person.body_ceiling`; `PersonalCombatInput.ends`; the fight's stamina, concentration, wound tracker | `seam/wrappers/combat.py::party_end`; `modules/combat/combatant.py::rederive` | fight, per scene |
| `threshold` | a requirement that prices use, never forbids it (the strength a kit demands) | a shortfall, `max(0, demand − value)` | attribute points | stamina per action and closing rate (a person); drain, recovery and step (a unit) | `carry_demand`'s caller: `combat_systems.act_cost`; the host, for a unit | fight (wielded and worn only) |
| `rate` | competence scales an uncontested effect | a multiplier on the effect's magnitude | per mille | the effect's written amount | the effect's reader of `capability_rate` (`07_SE_capability_and_chooser_surface.md`) | none |
| `judgement` | competence weighs a choice | a factor about the scale's mid-point | a factor, 1 at mid | a candidate's score | `capability_factor` (`02_CHAR_capability_uses_table.md`) | one site (told-claim credit) |
| `gate` | a minimum to attempt | admits, refuses, or unknown | attribute or practitioner points | a precondition stem | `queries/person_q.py::OwnStateReader` | one site (Thread Sensitivity); closed to it by ruling |

Three things that are **not** roles, so that nobody adds them as one:

- *The target number* is 7 and no capability touches it (ED-IN-0196). *The band edges* (0, 1, 3) are
  the ladder's.
- *The contest form* is the provider's, not the character's: `static` (the obstacle is composed from
  scores and terms) or `opposed_roll` (each side's obstacle is the other's net, floored at `OB_MIN`).
  It is one more key on the provider's row in `references/module_contracts.yaml`, beside the resolver
  vocabulary the first audit's export proposal sets: social `static`, combat `static`, field
  `opposed_roll`.
- *Bounds* are per role and are fixtures or the dice engine's constants, never a capability's:

| bound | value shipped | owner |
|---|---|---|
| attribute scale | 1 to 7 (floor 1: AR-05) | `references/descriptor_registry.yaml: attributes.scale` |
| a skill's scale | 0 to 7 (today a rank has **no** ceiling: `raised_capability` adds one without a bound, `loop/effects_combat.py:262-268`) | the capability's own row (§B) |
| the least a person brings | 0 in the social roll (a pool of zero is refused by S27.4 on the returned pair, `sigma.py:544-546`, as pinned for a held 0); 5 dice in a fight | the `dice` row's `floor` fixture (§C) |
| the least the roller deals | 1 die (`sigma_leverage._dice_dealt`); for a person it decides no outcome (a zero pool's one die is rolled and the act refused; a fight's pool is at least 5) | the dice engine; the addendum's §5.1 removes it for aggregates |
| the opposed divisor | 2 (ruled) | `sigma_leverage.opposed_ob`, one function (§G edit 5) |
| the obstacle's floor against a favourable term | `OB_MIN` (1) | `sigma_leverage.OB_MIN` |
| the obstacle's ceiling | solved per pool from `obstacle_ceiling` (2) | `roll.py::_chance_floor_cap`, fixtures |
| the impossible attempt | `Ob > obstacle_refusal_multiple × pool` (2) is refused | `sigma.py::resolve`, fixture |
| advantage's ceiling | 1.5 sigma (soft cap) | `sigma_leverage.M_MAX` |
| effort, practice | 2 levels; 2 dice | `Fixtures`: `effort` operand, `practice_cap` |

## B. What a capability is (the definition row)

`engine/season/rosters.yaml: tables.capabilities`, which `vocation_attribute` becomes (its `values:`
and `opposed_by:` are this table's `base` and `opposed_by` columns; its loader's closure checks carry
over). The row is field for field the one `01_CORE_capability_authoring_surface.md` proposes, so the
two proposals differ only in the file (§F).

```yaml
tables:
  capabilities:
    kinds: [attribute, skill, aptitude, trait]     # closed
    grows_by: [train, practice, use, fixed]        # closed; each names a rule the engine implements
    untrained: [default, attribute, none]          # closed; what a non-holder brings
    rows:
      copying: {kind: skill, base: attr.mind.focus,      scale: [0, 7], untrained: default, grows_by: [train, practice]}
      argue:   {kind: skill, base: attr.social.charisma, scale: [0, 7], untrained: default, grows_by: [train, practice]}
      inquiry: {kind: skill, base: attr.mind.acuity,     scale: [0, 7], untrained: default, grows_by: [train, practice]}
      arms:    {kind: skill, base: attr.body.agility,    scale: [0, 7], untrained: default, grows_by: [train, practice, use]}
```

| field | meaning | unit | read by |
|---|---|---|---|
| the row's key | the capability's id; the key of `Person.capability` | — | every reader below |
| `kind` | `skill`: a learned rating that gives dice, started from an attribute. `aptitude`: a rated knack that gives no dice of its own and acts through `edge`, `addend`, `rate` or `judgement` rows. `trait`: unrated (held or not; scale `[0, 1]`), acting through `edge`, `circumstance` or `judgement` rows. `attribute`: one of the ten, defined in `descriptor_registry.yaml` and **not** re-defined here; the kind exists so a uses row may name an attribute key | — | `data/rosters.py::_load_capabilities` (refuses a `dice` use of a trait, a rank above `scale`, a `base` outside the ten) |
| `base` | the attribute a skill's pool starts from | a registry key | `pool.py::_authored_attribute` (through the derived `VOCATION_ATTRIBUTE`) |
| `opposed_by` (optional) | the attribute a person subject opposes it with, when not `base` | a registry key | `pool.py::_opposing_attribute` (through `VOCATION_OPPOSED_BY`) |
| `scale` | floor and ceiling of the held rank | whole numbers | `data/cast.py` at world build (part one); `loop/effects_combat.py::raised_capability`, which today raises a rank without any ceiling (part two: a mover only for a rank that would pass the ceiling) |
| `untrained` | what a non-holder brings: `default` (`pool_default`), `attribute` (the base attribute, else `pool_default`), `none` (nothing: traits and aptitudes) | — | `pool.py::score` |
| `grows_by` | `train` (`_eff_train`), `practice` (the practice addend, from the act log), `use` (a fight that drew blood raises it), `fixed` | — | `loop/effects_combat.py` (`_eff_train`, `_grown`); `queries/world_q.py::practice` |

**Who holds what** is unchanged and has two carriers, both existing: `Person.attributes`
(`{registry key: 1..7}`, the ten) and `Person.capability` (`{capability id: rank}`: skills, aptitudes,
and a trait as rank 1). No new `Person` field and so no new `write_matrix.yaml` row. **A bundle**
(a lifepath, a martial tradition: AR-43a) is a named set of capability ids granted together; the
existing `tables.lifepath_templates` is the bundle table and its `holds:` check reads this table's keys.

## C. Where a capability is used (the uses table)

`engine/season/rosters.yaml: tables.capability_uses`. It is the table `02_CHAR_capability_uses_table.md`
proposes, with a `role` column; that proposal's three rows are rows of it unchanged.

```yaml
rosters:
  capability_use_sites: [social_roll, fight, field, kit, settlement_effect,
                         told_claim_credit, choice_temper, own_state_gate]   # closed: each is one reader
tables:
  capability_uses:
    rows:
      # -- today's rules, restated (part one: hash equal) -----------------------------------------
      - {use: social_roll, role: dice,      key: verb, side: actor,   add: social_pool_add, floor: social_pool_floor}
      - {use: social_roll, role: opposes,   key: verb, side: subject}
      - {use: fight,       role: dice,      key: verb, side: each,    add: combat_pool_add, floor: combat_pool_floor}
      - {use: fight,       role: opposes,   key: verb, side: each}
      - {use: fight,       role: resource,  key: attr.body.endurance, side: each}
      - {use: kit,         role: threshold, key: attr.body.strength,  side: each}
      - {use: told_claim_credit, role: judgement, key: attr.social.attunement,  gain: competence_gain}
      - {use: choice_temper,     role: judgement, key: attr.mind.focus,         gain: temper_gain}
      - {use: own_state_gate,    role: gate,      key: prac.thread_sensitivity, gain: thread_sensitivity_gate}
      # -- no row ships for: edge, circumstance, addend, rate; `field` has no row at all -----------
```

| field | meaning | unit or closed set | which roles take it |
|---|---|---|---|
| `use` | the site: the one place in code that reads this row | `capability_use_sites` | all |
| `role` | the axiom (§A) | `capability_roles` | all |
| `key` | whose rating: a capability id, an attribute or practitioner key, or `verb` (the capability `verb_capability` names for the act's verb) | — | all |
| `side` | whose sheet: `actor`, `subject`, or `each` (both parties of a two-sided scene) | closed | `dice`, `opposes`, `edge`, `circumstance`, `resource`, `threshold` |
| `when` (optional) | the condition under which the row applies; keys closed against the verb table's verbs and prizes, a venue's kind and the arrangement's speech kinds (the set `05_SC_capability_surface.md` names) | closed keys | `edge`, `circumstance`, `addend`, `rate` |
| `level`, `per` | the named level, and whether it counts once when held (`held`) or once per rank (`rank`) | a `LEVEL_SIGMA` name; `held` or `rank` | `edge` |
| `against` | `true`: the levels count against the side named | boolean | `edge` |
| `gain` | the fixture that scales the value | a registered `Fixtures` name | `circumstance` (successes per rank), `judgement`, `gate`, `rate` |
| `add`, `floor` | the site's pool rule: dice added to the base, and the least a person brings | registered `Fixtures` names, whole dice | `dice` |

Closed both ways, as `vocation_attribute` is: a site that no reader registers is refused at import; a
field its role does not take is refused; a reader whose site has no row for a role reads *no
capability* (zero dice added, zero sigma, zero term, a factor of 1, unknown for a gate), never a
default. Four new fixtures carry values that are literals today, each with a hole-register row graded
`assumption` under H-126 and a three-point sweep: `social_pool_add` (0), `social_pool_floor` (0),
`combat_pool_add` (6), `combat_pool_floor` (5). The rule they parameterise is one line, the same at
every site: `pool = max(floor, score + addends + add)`.

`verb_capability` stays as it is (verb → capability id). Whether it is a roster or a column on the
verb's row (CORE's edit 3) is the same fact in either place; `VERB_CAPABILITY` is the interface.

## D. The resolver inputs, exactly

What each typed record carries after part one, and which rows fill it. Records are in
`engine/season/queries/inputs.py`; the host fills them, the module composes, and no module reads the
tables (a module reaches the surface only through its typed input, `04` §A.2).

| record · field | type · unit | filled from | by (host) | composed by (module) |
|---|---|---|---|---|
| `SocialContestInput.pool` | `int`, dice | `dice` + `addend` rows of `social_roll` | `pool.py::faculty` | `roll.py::roll` (`roll_net`) |
| `.opposition` | `float` or `None`, a score | the `opposes` row | `sigma.py::_opposition_of` | `roll.py::obstacle` (`opposed_ob`) |
| `.leverage` | `float`, sigma | `advantage_sources` members: `effort`, and `capability` (the `edge` rows) | `sigma.py::advantage_sigma` | `roll.py::roll` (`net_boost`) |
| `.obstacle_terms` (new) | `float`, successes, signed | `obstacle_terms` members: `capability` (the `circumstance` rows); `wounds` when the addendum's §5.4 lands | `sigma.py::obstacle_term_sum` (new, `advantage_sigma`'s twin) | `roll.py::obstacle`, added before the ceiling |
| `.reception`, `.proofs`, `.forgery_quality` and their gains | as today | the room and the examined Record (not capabilities) | `sigma.py::contest_input` | `roll.py::obstacle` |
| `.obstacle_default`, `.obstacle_ceiling`, `.ceiling_per_pool`, `.obstacle_refusal_multiple` | as today | fixtures | `sigma.py::_frame` | `roll.py::obstacle`; the refusal in `sigma.py::resolve` |
| `PersonalCombatInput.faculties` | `(int, int)`, a score with addends | the `dice` row of `fight` | `combat.py::combat_input` | `core.resolution_pool`, `core.ob_from_defender` |
| `.pool_add`, `.pool_floor` (new, carried raw) | `int`, dice | the `dice` row's two fixtures | `combat.py::combat_input` | `core.resolution_pool(faculty, add, floor)`; `BASE_POOL` and `POOL_FLOOR` become the workbench's defaults of the same two arguments |
| `.ends` | `(int, int)`, Endurance less body bands | the `resource` row | `combat.py::party_end` | `combatant.rederive` |
| `.attributes` | per party `{registry key: 1..7}` | `Person.attributes`, whole | `combat.py::combat_input` | the module's own sigma terms, by `modules/combat/attributes.py::SPEC` (its `registry_key` column is the map's row for each) |
| `.kits` | `(weapon, armour)` per party | the rungs' stores (`world_q.kit_of`) | `combat.py::combat_input` | `combat_systems.act_cost`, with the `threshold` row's Strength |
| `MassBattleInput` | — | **no capability row**; `field` is a declared site with no rows | — | — |

The field's absence is thereby stated in data and not only discoverable by reading a wrapper. The
first rows it would take, each the MB lane's to author and build, are an `edge` row (a commander's
capability as levels on his side's exchanges: the mean shift, never the pool, so the directive of
2026-07-08 stands) and the `threshold` row for a troop type's `strength`.

**The reason trail.** `seam/wrappers/sigma.py::resolve` already returns a record (pool, obstacle,
leverage, net, settled margin). It gains one field, `fed_by`: a tuple of
`(use, role, key, side, value, contributed)` for every row that contributed, in table order, built by
the same three functions that read the rows (so it cannot disagree with what was rolled). That is the
end-to-end legibility the brief asks for, and it is the payload of the first audit's *roll's record on
its Event* (`10_DICE_believed_odds_have_a_prior.md`, edit D), not a new instrument.

## E. What a designer does, and what needs code

Each of these is rows only (no Python), once part one has landed:

| to do this | add |
|---|---|
| a new skill, say `oratory`, on Presence | one `capabilities` row; `verb_capability` rows for the verbs that test it. The `dice` and `opposes` rows of each site already cover it (`key: verb`) |
| a skill a person resists with something other than its own attribute (a plea resisted by Spirit: AR-44) | `opposed_by: attr.mind.will` on the row |
| an aptitude that helps under a condition (a trained eye on documents) | a `capabilities` row (`kind: aptitude`); `{use: social_roll, role: edge, key: keen_eye, side: actor, when: {verb: examine}, level: minor, per: rank}` |
| a trait that hardens a hearer (unmoved by rhetoric: NPC-001) | a `capabilities` row (`kind: trait`); `{use: social_roll, role: edge, key: unmoved, side: subject, against: true, when: {verb: argue}, level: moderate, per: held}` |
| an attribute a venue rewards (a parliament penalises want of Grace: AR-36a) | `{use: social_roll, role: circumstance, key: attr.social.grace, side: actor, when: {venue: parliament}, gain: grace_venue_gain}` and the fixture |
| Spirit *"ignoring obstacle modifiers"* in one context and *"adding … to dice pool"* in another (AR-44) | two rows on `attr.mind.will`: a `circumstance` row with a negative gain, and an `edge` row; each under its own `when` |
| who has it | `capabilities: {oratory: 3}` on the cast row (`references/npc_registry.yaml`), or the id in a lifepath's `holds:` |
| how much it is worth | the fixture the row names |

What needs code, and should: a new **role** (a new axiom), a new **site** (a new reader), a new
**`when` key**, a new **growth rule**. Each is one function at one owner and a new member of a closed
roster. A flat bonus to a net, a changed target number, an actor lowering his own obstacle, and a
capability required to attempt are not expressible at all, which is the rulings' intent.

## F. Reconciliation with the other lanes' proposals

| proposal | what it proposes | in this map |
|---|---|---|
| `01_CORE_capability_authoring_surface.md` | a `capabilities:` block (the definition row) in `references/descriptor_registry.yaml`; a `capability:` column on the verb row; `verb_capability` and `vocation_attribute` deleted | **the same row** (§B). The one open difference is the file. This proposal keeps it in `rosters.yaml`, as the work order directs: the loader, the closure checks and the three tables that validate against it are already there, and nothing is moved. CORE's home buys the descriptor chain's exporter and `--check` and a leaf modules can reach. The holistic stage picks; the row, the derived maps and every reader are identical under either. CORE's edits 7, 9 and 10 are adopted as written |
| `02_CHAR_capability_uses_table.md` | `capability_uses` with `use`, `key`, `form`, `gain`; forms `about_mid`, `at_least` | **the same table** (§C). `form` is implied by `role` (`judgement` is `about_mid`, `gate` is `at_least`); its three rows ship unchanged; its two substrate functions are the two roles' readers |
| `05_SC_capability_surface.md` | `trait_advantages` roster and one generic `trait` member of `advantage_sources` | its rows are `edge` rows of `capability_uses`; its generic member is the `capability` member here (one function for every kind, not only traits). Its two verb rows stand |
| `06_FA_office_capabilities.md` | verb rows for `determine`, `interrogate`, `arrest`; a seat's vocation as a reason a conferrer may weigh | verb rows are `verb_capability`'s; a seat's vocation weighed in a `confer` is a `judgement` row with a new site, the FA lane's |
| `07_SE_capability_and_chooser_surface.md` | `capability_rate`: a per-mille multiplier on an uncontested effect | the `rate` role; its table is the role's gain |
| `03_PC_person_inputs_content.md`, `03_PC_loadout_and_carry.md` | slot values composed by the host from the surface; `carry_demand` | the `fight` rows of §C and §D; `threshold` |
| `04_MB_unit_loadout_and_weapon_in_hand.md` | a troop table as data with a `strength` cell | the `threshold` row's second holder; the `field` site's first rows |
| `10_DICE_one_score_two_roles.md` (first audit) | `score` split from `faculty`; a person subject always has a score; four verb rows | `score` is the `dice` row's base and the `opposes` row's value: the proposal is what makes one row serve both roles |
| `10_DICE_advantage_sources_for_the_arcs.md` (first audit) | a signed channel; `wounds` | the signed channel is the `edge` role's `against`; `wounds` moves to `obstacle_terms` (addendum §5.4, F-DICE-16) |

## G. The exact edits, by file and owner

**Part one (hash equal).**

1. `engine/season/rosters.yaml` (IN). `tables.capabilities` (§B), absorbing `vocation_attribute`;
   rosters `capability_roles` and `capability_use_sites`; `tables.capability_uses` (§C);
   `advantage_sources.values: [effort, capability]`; a new closed, ordered roster
   `obstacle_terms: [capability]`.
2. `engine/season/data/rosters.py` (IN). `_load_capabilities` replaces `_load_vocation_attribute` and
   `_load_vocation_opposed_by` and exports the same `VOCATION_ATTRIBUTE` and `VOCATION_OPPOSED_BY`;
   `_load_capability_uses` (every `key` resolved through `engine.substrate.descriptors` or the
   capabilities table; every fixture name registered; every `level` a `LEVEL_SIGMA` name; role-field
   agreement).
3. `engine/season/data/fixtures.py` (IN). The four pool fixtures of §C at today's values, with their
   hole-register rows.
4. `engine/season/seam/wrappers/pool.py` (IN). `faculty` reads `add` and `floor` from the `social_roll`
   site's `dice` row and returns `max(floor, score + addends + add)`; at 0 and 0 that is today's
   `base + addends`, so a held 0 stays under one die and is refused by S27.4 as
   `engine/season/tests/test_odds_of.py` pins. Combat keeps receiving `score + addends` and applies its
   own row's two operands (edit 8), which is today's `max(5, faculty + 6)`. One registered addend,
   `capability_addend`, reads the `addend` rows (none ship).
5. `engine/dice_engine/sigma_leverage.py` (IN). `opposed_ob(score) -> float`, the ruled divisor once;
   `modules/social_contest/roll.py:141` and `modules/combat/core.py:124` call it.
6. `engine/season/seam/wrappers/sigma.py` (IN). `ADVANTAGE_SOURCES["capability"]` and
   `OBSTACLE_TERMS["capability"]`, each one function over the table's rows for the act's operands
   (the actor's and the subject's held capabilities, filled by `contest_input`; a believer's own are
   his to know, a subject's are `None` without a claim, the existing `CAPABILITY_CLAIM` rule);
   `obstacle_term_sum`; `SocialContestInput.obstacle_terms`; `fed_by` on the returned record.
7. `modules/social_contest/roll.py` (SC). `obstacle` adds `inp.obstacle_terms` where it adds
   `forgery_quality`; a favourable sum is clipped at `OB_MIN` as the room is.
8. `engine/season/seam/wrappers/combat.py`, `modules/combat/core.py` (PC). `pool_add` and `pool_floor`
   carried raw on `PersonalCombatInput`; `resolution_pool(faculty, add, floor)`.
9. `references/module_contracts.yaml` (IN). `obstacle: static | opposed_roll` on the three provider
   rows.

**Part two (movers; other proposals, in order).** `10_DICE_one_score_two_roles.md`; the signed channel
of `10_DICE_advantage_sources_for_the_arcs.md` and the addendum's §5.4 wound term; CORE's edit 9 (a
first rank is never a loss); `raised_capability` reading the row's ceiling (control: no ceiling,
today's bytes); the verb rows of SC and FA; content (CHAR, PC, MB).

## The gate (execution artifacts)

1. `PYTHONHASHSEED=0 python -m engine.season.harness.headless --seasons 2 --seed 0`: the same
   `CONTENT HASH` before and after part one; `corpus_run` seed 0 reproduces its `DEGREES RESOLVED`
   tallies.
2. The addendum's probe E-B04, re-run: the three host records are byte-equal to today's at shipped
   data, and `fed_by` on a graded `argue` lists exactly the `dice` and `opposes` rows.
3. `python -m engine.season.harness.aperture 1 0`: `POOLS ROLLED` unchanged.
4. Combat's goldens byte-equal (`combat_pool_add` 6 and `combat_pool_floor` 5 are the literals moved).

## The falsifier

Each is a row edit in a test's rebound table, with no edit to code, and each must move the stated
figure and nothing else:

- Re-point `argue`'s `base` to `attr.mind.perception`: `odds_of` for an `argue` follows the actor's
  Perception and ignores his Presence.
- Set `combat_pool_add` and `combat_pool_floor` to 0: a fight's pool equals the social pool for the
  same person and verb (the F-DICE-17 table's third column becomes its first, under combat's
  sampler).
- Plant the trait row of §E and give a hearer the trait: `odds_of` for an `argue` at him equals
  `record_odds(pool, ob, -0.5)`; for a `tell` at him it is unchanged; with the row removed both are
  unchanged.
- Plant a `circumstance` row with a gain of 0.25 on an attribute the actor holds at 4, on the uncapped
  arm (`obstacle_ceiling` `None`): the composed obstacle rises by exactly 1.0, and `fed_by` names the
  row. On the shipped arm the rise is clipped at the pool's cap, as a hostile room's is.
- A row naming a level outside `LEVEL_SIGMA`, a fixture that is not registered, a `dice` use of a
  trait, or a site no reader registers refuses at import.

If any of the first four requires a Python edit to take effect, the surface is not the owner and the
proposal has failed.

## NERS reading (`CLAUDE.md` §0.06; E last)

- **N.** Cut it and a capability can give dice to a verb and nothing else by data; every other thing a
  character is good at is a constant in a module or does not exist. Tested top-down (a designer adds a
  trait and a hearer hardens), bottom-up (the three door functions read one table), lateral (a fight
  and a debate take their pool rule from the same row shape), vertical (a commander's row is the same
  kind of row as an advocate's), diagonal (a person's Strength and a troop type's are one key with two
  holders), horizontal (the choice-side and roll-side uses are one table). It holds in each; it is
  *narrowed* on the field, where it only declares an absence until MB authors rows.
- **R.** Customisation of characters is the direct yield. Variety in approach: the same capability can
  act as dice in one context and as a circumstance in another (AR-44) without a new mechanism. With no
  player present, differences between people reach rolls by declaration, which is what lets the world
  produce *she was the better speaker*. Complete at the extremes: a use with no row reads nothing; an
  unknown level, site or fixture is refused; the soft cap bounds any stack of `edge` rows.
- **S.** One unit per channel (dice, sigma in named levels, successes on the obstacle), the same in a
  debate and a fight; the pool rule differs by site only where a row says so; the contest form is
  named. *Zooms in and out*: the field's site and the person's are one table.
- **E, as a ratio against N and R.** Ten roles, two tables and four fixtures replace two rosters, two
  loader functions, two module literals, three planned per-lane rosters and one function per future
  modifier. A reader can say what any capability does from one file, and what fed any roll from one
  field.

## Cost class

Part one: an edit plus a small build (two loaders, two door members, one record field), hash equal.
Part two: the movers named, each in its own proposal with its control arm.
