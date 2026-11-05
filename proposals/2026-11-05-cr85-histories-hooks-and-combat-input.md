# CR-85: histories, hooks and combat's input. What replaces the `history` summed into rolls

## Status: RATIFIED on the merge of the PR that lands it (ED-1094), EXCEPT what §10 lists as HELD BACK (§4 step 2, the seeded-damage crossing), which stays PROPOSED until Jordan signs it off separately. Combat's `history` replacement (§1) is a ladder take, `[ASSUMPTION; medium; Jordan to correct; revert: delete this file; history stays]`.
## Version: v1.0 · Lane: PC (with IN, WR) · Position: `workplans/valoria_master_workplan_v11_part4.md` `### CR-85` (DESIGN-FIRST, B10-10; build B10-11)
## Grade under `CLAUDE.md` §0.2: `paper`. This is a design. It changes nothing in `engine/` or `modules/`, and whether its build executes is decided by the tests named in §8, not by this file.
## Citation rule: every `file:line` was opened by this author on the tree at `3ce1f08e` unless tagged `[UNVERIFIED]`. A drifted line from the plan is cited at its current line, and §9 lists the drift. Design documents are cited for intent only (`CLAUDE.md` §0.05). No formula below is correct because this file states it; the code that will hold each fact is named beside it.

**The rulings.** `ED-IN-0330` (Jordan, 2026-11-04): histories stop being *"something that can be added to rolls"*. In their place come *"bundles of skills/aptitudes that are learned abilities that complement character attributes"*. `ED-IN-0331` (the next message): *"histories also grant narrative hooks when building out character life paths"*. Neither ruling says what the mechanism is. This file answers that with the `CLAUDE.md` §0 ladder, as the position asks.

**What is eliminated, exactly.** The integer `history` that the code adds to a roll:

| owner | read | today |
|---|---|---|
| combat pool | `modules/combat/core.py:54-56` `resolution_pool(history) = max(POOL_FLOOR, int(round(history)) + BASE_POOL)`, called at `modules/combat/wrapper.py:189`, `:218`, `:313` | pool |
| combat Ob | `modules/combat/core.py:115` (`ob_from_defender`, def at `:100`) `defender.history / 2.0` | Ob |
| combat σ terms | `modules/combat/combat_systems.py:171` (`reading`: `READ_HISTORY_K*(c.history-3)`), `:332` (`tech = defender.history + skill('technique')`, used as `tech-3` at `:337` and `:349`), `:1053` (bind: `(aggressor.history+skill) - (defender.history+skill)`), `:1421` (`INIT_HISTORY_K*(aggressor.history-defender.history)`), `:1441` (`COUNTER_TRAIN_K*(defender.history-3)`) | five σ terms |
| threadwork pool | `systems/threadwork/sim/operations.py:243-247` `min(3, history + 3)` | a constant 3 for every history ≥ 0 |
| knot formation pool | `systems/fieldwork/sim/knots.py:215-216` `(spirit * 2) + history_relationships` | 0 by default |

`ED-IN-0330` also names "the fieldwork pool's History term". `git grep -i history -- modules/fieldwork systems/fieldwork/sim` finds no such read except the knot term above, so it has nothing to eliminate.

---

## 1. What replaces combat's `history` in the pool and the Ob

### 1.1 The recommendation

**Combat's pool and Ob read `faculty`**, the same reader the social contest uses (`engine/season/seam/wrappers/sigma.py:146-160`, *"THE ONE POOL READER"*). It returns the person's held capability key for the verb (`VERB_CAPABILITY`), or the fallback when he holds none, plus the registered pool addends. The season computes it for each party with the verb that opened the fight. It crosses the seam as a typed field. Inside the module it takes `history`'s place in exactly two reads, the pool and the Ob, with their formulas unchanged. **The five σ reads of `history` are deleted, not re-pointed.** There is no combat-specific bundle.

`[ASSUMPTION; medium; Jordan to correct; revert: delete the design file; history stays]`

The concrete shape, for the build (§8):

- `engine/season/queries/inputs.py::PersonalCombatInput` gets `faculties: tuple`, in `claimants` order, beside `ends`.
- `engine/season/seam/wrappers/combat.py::combat_input(w, claimants, *, verb)` fills that field with `faculty(w, p, verb)` for each party. It imports `faculty` from its owner and does not copy it. `resolve` already receives `verb` (`:181`); today it calls `combat_input(w, claimants)` without it at `:234`, and the build passes it there.
- `modules/combat/fight.py:52` constructs each `Combatant` with its party's faculty value.
- The `Combatant` input that was `history` is renamed `faculty`. It is the tree's existing word for exactly this number (§4: coin nothing). It sits in PC-14's attribute spec (B10-10b) with default 3, no `neutral`, and `registry_key` null, because it is not a registry attribute.
- `core.resolution_pool(faculty)` and `core.ob_from_defender` (`defender.faculty / 2.0`) keep their formulas. `BASE_POOL` 6 and `POOL_FLOOR` 5 are unchanged.

### 1.2 The ladder

1. **Superseded.** `-06` M2's DECISION (`workplans/valoria_master_workplan_v11_part6.md:33`, NARROWED and taken) already ruled: *"A person's input is `faculty`, derived at read and entering through the pool only, at all three scales (JQ-2 (1) yes)"*. CR-20 (`-04`, line 129) repeats it. The question "faculty or a combat bundle" was decided before `ED-IN-0330`, and nothing in `ED-IN-0330` reverses it: a held capability key, with `CR-20`'s attribute base under it, *is* a learned skill or aptitude that complements the attributes.
2. **Irrelevant.** Not applicable.
3. **Design document.** CP-T03-04's home (`proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-03-personal-combat.md:163`) already routes a combat skill through `Person.capability` (a vocation `arms` in `verb_capability`'s range, derived at the seam).
4. **Precedent.** The social contest reads the actor's pool from `faculty` and the opponent's Ob from his score halved (`sigma.py:163-175` `_opposition_of`, composed by `modules/social_contest/roll.py::obstacle`). Combat's Ob ruling, Jordan 2026-08-15 (quoted at `core.py:101-104`), names *"the SAME reading `modules/social_contest/roll.py::obstacle` applies"*. The docstring at `core.py:105-107` says history was used only because *"combat_engine_v1 has no separate 'capability' surface"*. The season now has one.
5. **Architecture.** A combat-specific bundle would be a second pool rule at a second scale. `CLAUDE.md` §10 calls that *shape divergence*. It would also be a second store of learned skill beside `Person.capability`, so CR-33's lifepath templates would have to write two carriers. One reader, one store.

**Why the σ terms go rather than read `faculty`.** M2 says "through the pool only", and its own two facts gloss that as *"`leverage` (σ-leverage) stays 0.0 … person latitude enters through the pool only … so (a) and (c) add no leverage producer"* (`-06:39`). The five reads are person latitude entering the net σ. `ED-IN-0330` eliminates exactly that: history added to the roll. PC-03's strict xfail already records them as a second channel: `tests/valoria/test_combat_ob_from_defender_consumers.py:194-213`, `test_history_enters_the_roll_through_exactly_one_channel` (*"Whether that is a double-count is a design question"*). This design answers it: **one channel, the Ob.**

**Reading of "pool only" taken here.** The Ob from the opponent's score is not "latitude through σ". It is the 2026-08-15 ruling, and the social contest applies it under the same M2. `[ASSUMPTION; medium; Jordan to correct; revert: the faculty value feeds the pool only and the Ob reads the class default 3, a `modules/combat` split (CP-T03-04's home note at :174-175)]`.

**One field, read by both pool and Ob.** Social splits the actor's pool (`faculty`, practice included) from the opponent's Ob (the held key, never practice, `world_q.py:4112-4113`) because only the actor rolls. In a fight both parties roll in turn (`wrapper.py:313-315`: pool from the aggressor, Ob from the defender). Combat's two rulings read one score (`core.py:105-107`), so one value per party is kept. `[ASSUMPTION; low; revert: a second per-party field from `_opposition_of` for the Ob]`. At the build this choice is inert: the practice addend counts no fight (§6, finding P), and no person holds a combat key.

**The rejected alternative.** A combat bundle in `Combatant.skills` / `equipped`, filled by the season, with the pool read from it. Rejected at steps 1, 4 and 5. `Combatant.skills` (`combatant.py:115`) and `equipped` (`:116`) stay as the module's own per-axis biases. They are not the pool's input (see §6).

### 1.3 The season-loop hash cost, measured

**Today.** The season constructs fighters at `modules/combat/fight.py:52` as `Combatant(a_id, end=a_end)`. `history` is left at the class default 3 (`combatant.py:94`). The plan's citation `seam/wrappers/combat.py:36-39` is the docstring that lists the defaults, and that list omits `history` (§9). So the pool is `max(5, 3+6) = 9` and the Ob is `3/2 = 1.5`.

- **Executed:** `core.resolution_pool(Combatant('a', end=4).history)` → 9 and `core.ob_from_defender(...)` → 1.5.
- **Run:** a probe that wraps `core.resolve` over `build_realm(0)` for two automated seasons recorded `{(pool 9, Ob 1.5): 28}`. Every roll the season made was at 9 against 1.5. The probe is not committed. It loads `pc_engine`, wraps `core.resolve` to count `(pool, ob)`, and runs `SeasonDriver(build_realm(0)).season(make_chooser(...))` twice, as `engine/season/tests/test_rem31_grid_suspension.py:47-74` drives one season.

**Under the recommendation.** No verb names a combat key yet: `verb_capability` has rows for `tell`, `speak`, `argue`, `research`, `examine` and `surveil` only (`engine/season/rosters.yaml:1381-1387`). So `faculty(w, p, "fight")` is `pool_default`, which is 2 (`engine/season/data/fixtures.py:449`), plus a practice addend of 0. CR-20's attribute base applies only to a verb that has a vocation. **Every season fight moves from pool 9 against Ob 1.5 to pool 8 (`max(5, 2+6)`, executed) against Ob 1.0.** That makes the build a declared MOVER of every seeded season that fights, as the plan states.

**Why the build takes the move rather than reproduce 3.** Two facts, each checkable, decide it.

- **(a) The plan's own falsifier needs it.** The plan's planted failure is that dropping the replacement read *"reproduces pool 9 against Ob 1.5 and reddens"* (`-04` CR-85 EXIT). If the season's no-key value were the class default 3, dropping the read would reproduce exactly the shipped state, and that assertion could never redden. It would be an absent test (`CLAUDE.md` §0.1 pt 2).
- **(b) CR-33 needs it.** CR-33 grants lifepath keys at `pool_default` because *"the grant changes no pool"* (`-04` CR-33, line 311). That holds for combat only if combat's no-key value is also `pool_default`. Otherwise a martial lifepath granting the combat key at 2 would fight **worse** than a person with no lifepath (pool 8 against 9).

One fallback for "holds no key", swept by H-126 at every scale, is the consistent methodology (`CLAUDE.md` §0.06 S).

**What stays EQUAL. This is the build's CONTROL.** A test-time arm replaces the seam's faculty value with the constant 3 for every party. That arm must reproduce the pre-item season `content_hash` bit for bit, because nothing else in the fight differs:

- the pool and Ob are 9 and 1.5 again;
- the five deleted σ terms were exactly `0.0` in every season fight. Both parties sat at history 3. Each term is centred at 3 (`:171`, `:332`→`:337/:349`, `:1441`) or is a difference of the two parties' values (`:1053`, `:1421`). `Combatant.skills` is empty in the season (`fight.py:52` passes none; `combatant.py:115`), so `skill('technique')` and `skill('bind')` are 0.0. `x + 0.0 == x` in IEEE arithmetic, so deleting a zero addend is exact.

The exported constants differ only by the deleted keys. The same arm on the module, `Combatant(…, faculty=3)` in the workbench, reproduces every default-build workbench outcome.

**What a differing input moves.** Only that party's own pool (`faculty + 6`, floor 5) and the Ob his opponent rolls against (`faculty / 2`). No σ term reads it, and no other party's number changes.

**FALSIFIER (1).** These four checks would show the section wrong. What each reads today is in brackets.

- A season fight's rolls, spied as above, read (8, 1.0) on `build_realm(0)`. [Today: (9, 1.5), 28 of 28.]
- A planted party holding the combat key at 5 rolls pool 11, and his opponent rolls against Ob 2.5. [Today impossible: the seam passes nothing.]
- Planted failure: the seam's read dropped (the class default) reproduces (9, 1.5) and the first assertion reddens.
- CONTROL: the constant-3 arm reproduces the pre-item season hash.

The strict xfail at `test_combat_ob_from_defender_consumers.py:194` XPASSes, and the build converts it into a plain passing assertion of one channel.

---

## 2. What a hook is, where a lifepath writes it, how it reaches play

**A hook is not a new kind of thing, and no noun is coined for it.** In code, a hook is one of three writes made **at world build** onto a carrier that already exists and already has a reader in play. `Person.marks` is deleted (`engine/season/state/carriers.py:724`), and `git grep -i 'lifepath\|life_path' -- engine modules` returns nothing. Nothing named `hook` is introduced.

| a hook is… | written by | at | reaches play through |
|---|---|---|---|
| **a capability key** (the skill half; `ED-IN-0330`'s bundle) | CR-33's `lifepath_templates` expansion of a cast row's `lifepath:` key, in `engine/season/data/cast.py` | world build | `faculty` (`sigma.py:146-160`) → every contested verb's pool, combat's included (§1); `train` raises only a held key; `_opposition_of` → the Ob against him |
| **a goal row's commit** (an obligation, a vow, an enemy: an OUGHT the person commits to, and the goal row's `stance` rows) | `harness/populated.py::seed_goals` (`:823`), which already mints each goal's Proposition and writes its org persons' `commit`s and stance rows. It reaches the cast row through its existing `cid_of` argument (person id → case id), then the row's `lifepath:` key, then the template's goal ids | world build, after the goal Propositions are minted | the ambition's question: `world_q.goal_referents` (`:2585`, *"WHO OR WHAT AN AMBITION IS ABOUT, read when the question forms"*); `goals.expected` in the opinion reading (`world_q.py:2811`); CR-34's tally where a matter is declared |
| **a heritage value** (descent) | CR-30's `data/cast.py::heritage_of`, reading the cast row's `heritage:` key, **not the lifepath** (descent is not a profession) | world build | `epistemic.py::_term_marks` (`:918-924`) → a co-located witness's `seen` claim → CR-31's `heritage_regard` → `teller_weight` |

**Where CR-33 stores the lifepath id: on the cast row only, never on `Person`.** CR-33 stands as written (`-04:309`, `:311`; its exit asserts that `repr(Person)` contains no lifepath id). Every hook is written at build, and at build the cast row is readable (`cast.row(case_id)`, `data/cast.py:117`). So no reader in play needs the id, and storing it would add a field that nothing reads. The hook writers go where the id already is: the template expansion in `data/cast.py` for capability keys, and `seed_goals` through `cid_of` for goal commits. A person built from no cast row (a generated cohort) has no lifepath and no lifepath hook.

**Two kinds of hook are written now.**

- **Capability keys** are CR-33's rows. A martial lifepath can map to a combat key only once CP-T03-04 adds that key to `verb_capability`'s values, because CR-33 refuses at import a template key outside them (`-04:313`). Until then martial lifepaths map to none and are recorded, which is CR-33's own rule (`-04:318`).
- **The goal-commit column** of `lifepath_templates` (goal ids from `goals.yaml`, each refused at build if this world minted no Proposition for it) is **built only with its first authored value**. A column that nothing writes is the defect PC-14 item (8) names (*"a field read that nothing writes is I1's own defect class"*). Which lifepath carries which obligation is content, as CL-OPEN's pool rows are Jordan's (`-04:459`).

**Not taken.** A Record held from build (CL-OPEN's "lawful seed", `-04:456`) is the precedent if a lifepath ever needs to grant a document. No template needs one today.

**FALSIFIER (2), for the first build that authors a hook value.**

- A cast row whose lifepath template names goal `g` builds a person holding a live `commit` to Proposition `g`.
- That person's question list on the next deliberation includes `goal_referents(g)`.
- The same row with the `lifepath:` key deleted builds without the commit.
- Planted failure: the `seed_goals` branch skipped reddens the first assertion.
- CONTROL: no template carrying a goal id reproduces the pre-commit hash.

Today the first assertion cannot run: no `lifepath:` key, template or column exists, which is the expected reading at this design's base.

---

## 3. The oracles' fate

`CLAUDE.md` §6 governs this section. A change is made at the owner in Python and re-exported by its exporter. The port is never hand-edited.

| oracle | owner of the `history` read | becomes | exporter and `--check` |
|---|---|---|---|
| **combat** `modules/combat/` (the live oracle, ED-900/904) | `core.py:54-56` (pool), `core.py:115` (Ob), `combat_systems.py:171`, `:332`, `:1053`, `:1421`, `:1441` (σ), and the three pool callers at `wrapper.py:189`, `:218`, `:313` | **Pool and Ob:** the renamed input `faculty`, same formulas (§1). **σ:** the five terms deleted (`reading` loses its experience term; `tech` becomes `skill('technique')` AND its `-3` centre at `:337` and `:349` goes with the history term (left in, `skill - 3` is a constant -3 on every parry and wind sigma and breaks the constant-3 control); bind reads the two `skill('bind')` alone; `init_emphasis_sigma` loses its third addend; the counter probability loses its training term). `config.py`'s `READ_HISTORY_K`, `INIT_HISTORY_K` (`config.py:124`) and `COUNTER_TRAIN_K` (`:267`) are deleted with their only readers. `BIND_TECH_K` (`:217`) stays, because bind still reads the skill differential. PC-14's attribute spec renames its `history` entry `faculty`. | `python tools/export_engine_params.py` re-derives `engine/engine_params/combat_engine_v1.json`, losing the three keys (today at `:113`, `:194`, `:66`; `BASE_POOL` `:238` and `POOL_FLOOR` `:278` unchanged) and carrying `faculty` in PC-14's `attributes` section. `SCHEMA_VERSION` (`tools/export_engine_params.py:56`) is bumped, as v3 did for a removed key. `--check` is blocking in CI (`.github/workflows/valoria-ci.yml:130`) and green at base (run by this author: *"committed JSON matches config.py"*). `tests/valoria/test_combat_invariants.py:526` (`test_no_dead_exported_engine_params`) would redden if a key were kept with no reader. |
| **combat collision note** | `tools/export_game_constants.py:89-91`, a reason string reading *"max(POOL_FLOOR, history + BASE_POOL)"* | the same string with `faculty` | `python tools/export_game_constants.py --check` (green at base) |
| **combat workbench** `systems/combat/combat_engine_v1/workbench/` | `balance.py:44`, `catalogue.py:47`, `server.py:29`, `static/index.html:132` name `history` | renamed `faculty`, through PC-14's spec where PC-14 (6) already routes these factories | none: the workbench is not exported |
| **threadwork** `systems/threadwork/sim/operations.py` (the oracle CP-T07-02's host rolls) | `_actor_pool`, `:241-247` | `history_contrib = min(3, history + 3)` becomes the constant it already yields, 3, which is PP-624's *"constant +3"* (`:245`). The `.history` attribute is no longer read. This is EQUAL for every caller in the tree: every practitioner the tests build carries `history` 0 (`tests/valoria/test_threadwork_mending_parity.py:50-51`, `test_threadwork_resilience.py:37`, `test_coherence_elastic_plastic.py:229`, `engine/tests/test_thread_mending_ed871.py:32-36`). The docstrings at `:17`, `:236-239` and `opposing.py:107` drop `.history`. | `python tools/export_sim_params.py --check` (reads `[SIM-PARAMS] current` at base). No named constant changes, so it is expected to stay current. `[UNVERIFIED until the build runs it]` |
| **knots** `systems/fieldwork/sim/knots.py` (unplugged: `references/module_contracts.yaml` row `fieldwork`, `sim_module: modules/fieldwork/`; no game caller of `form_knot`) | `:215-216` | `pool = spirit * 2`. The `:57` canonical tag and the `:179` duck-type list drop History. `engine/tests/test_knots_ed912.py:35-38`'s `_FormActor.history_relationships = 6` goes. Its one assertion is that some knot forms over 80 seeds, now at pool 10 against Ob 2 (`:58-59`), and it is re-run. | the same `export_sim_params.py --check` |
| **v30 combat** `systems/combat/sim/combat.py` (DEPRECATED 2026-06-23, *"Retained for reference/history only"*, `:3-11`) | `:134-138` (`agi*2 + history + 3`) | **not touched by CR-85.** It is no roll the game or the port makes (ED-1050's port reads `combat_engine_v1.json`). Its retirement (delete it and write a `FORK:` row; `tests/valoria/test_degree_ladder_single_owner.py` and `test_tn7_always.py` import it) is outside this position, and the orchestrator decides whether to take it (§10). | none |

**FALSIFIER (3).** After the build, `git grep -c -E '\.history\b|history_relationships' -- modules/combat/*.py systems/threadwork/sim/*.py systems/fieldwork/sim/*.py` finds no line that is code. [Today, per file, docstring lines included: `combat_systems.py` 5, `wrapper.py` 3, `core.py` 1, `combatant.py` 1, `operations.py` 2, `opposing.py` 1, `knots.py` 2. The bare parameter `history` at `core.py:54` and `combatant.py:94` is not matched by that pattern and is renamed with it.] All three `--check`s pass after re-export. Planted failure: re-adding `READ_HISTORY_K` to `CFG` with no reader reddens `test_no_dead_exported_engine_params`.

---

## 4. The Health round trip: what is stored, where, once

**What is stored.**

- **Between scenes, health is stored once:** `Person.body`, an int on `condition_scale` 1000 (`state/carriers.py:743`, `data/fixtures.py:217`). Its writers are the fight (`loop/effects_combat.py:163` through `_harm`, `:204-224`), the field's casualties (`:363-370`), `tend` (`:481-485`) and MATTER's dearth fall (`loop/matter.py:666-668`, a `setattr` form a `.body =` grep misses), so step 2's seeded damage reads a body MATTER may have lowered.
- **Inside a scene,** the module's `WoundTracker` (`modules/combat/combatant.py:50-89`) is working state. It holds `cumulative_damage` and derives `health_full`, `wi` and `max_wounds` from the attributes. PC-14's storage puts it under one owner: `rederive()` rebuilds the maxima and **preserves `cumulative_damage`** (`-04:930`, item (3)). The tracker is never stored. `fight.py:52` constructs fresh `Combatant`s for every scene, and `wrapper.fight` re-initialises both trackers at its start (`modules/combat/wrapper.py:561`). A registered module keeps no game state (`04` §A.2).
- **Not stored anywhere:** `health_full`, `wi`, `max_wounds`, `stamina_max`. Each is derived from attributes.

**So health is not stored twice. It is mapped twice, and the two maps differ.**

- **In,** `party_end` turns body bands into a lower `end`, one point per band (`seam/wrappers/combat.py:130-138`, H-97, `hole_register.yaml:1350-1358`). A wound reaches the fight as a lower *attribute*. That shrinks `wi`, `max_wounds` and `stamina_max`, and the tracker then starts clean.
- **Out,** `_harm` writes `max(1, body × left // full)` (`loop/effects_combat.py:224`), the fraction of the scene's health the fight left.

The tracker's own sentence *"Persists between encounters (cleared only at session end, per canon)"* (`combatant.py:56-57`) is the archived tabletop rule. It is false in the module (`wrapper.py:561`) and false in the season.

**The design.**

1. **CR-85's build corrects the record and changes no behaviour.**
   - The `WoundTracker` docstring says the tracker is per-scene working state, and that persistence is the host's `Person.body`.
   - The comment at `wrapper.py:558-560` is reconciled with PC-14's `rederive`.
   - This is hash EQUAL.
2. **The in-map changes when its premise ends** `[ASSUMPTION; medium; Jordan to correct; revert: H-97's `party_end` and `_harm` as they stand]`.
   - **The premise.** H-97 derives `end` from `body` only because *"a tracer `Person` carries nothing combat-shaped except `body`"* (`hole_register.yaml:1352`).
   - **When it ends.** That premise ends at the first commit that passes a party's Endurance from CR-20's `Person.attributes` through the seam. That is PC-14 item (8)'s trigger, *"the host passes attributes when K-1/K-5 lands"*. From then on `end` has one source, the attribute, and body must stop landing on it.
   - **The seed.** In that same commit `PersonalCombatInput` carries each party's condition (`body / condition_scale`). The module entry then seeds `cumulative_damage = floor(health_full × (1 − condition))` after construction.
   - **What it composes on.** PC-14's `rederive`, which replaces `wrapper.py:561`'s re-init and preserves damage, is what lets the seed survive into the fight. That is the "one design with PC-14's storage".
   - **The out-map.** It becomes `body × left // left_at_start`, where `left_at_start` is the health the party entered with, lifted once before the fight. Today's formula is the case `left_at_start == full`.
   - **The bands.** The lifted `wounds`, which `combat_band_edges` reads (`rosters.yaml:934`, `wound_quantities`), is measured from the scene's start. That way a person who enters wounded and takes no hit still reads `Untouched`.
   - **H-97.** It closes by supersession, not by its own sweep's third arm (`hole_register.yaml:1358`: *"condition cannot reach the engine"*): step 2 makes condition reach the engine through seeded damage.

**FALSIFIER (4), for step 2's commit.**

- A party entering at body 500 with no hit taken leaves at body 500 and reads `Untouched`.
- A party entering at body 500 and losing half the health he entered with leaves at 250 and reads `Wounded`.
- A party felled is written 0.
- Planted failure: a seed of 0 with `end` read from the attribute gives the wounded party full health, and the first fight's `health_remaining` assertion reddens.
- CONTROL: the condition passed as 1.0 for every party, with `party_end` restored, reproduces the pre-commit hash.

[Today: `body × left // full` with a clean tracker, and `end` cut by bands. Step 1 has no falsifier beyond the docstring diff, because it executes nothing.]

**A consumer this re-base touches that the position did not list.** CP-T03-07's home says *"a maimed veteran fights at `end` 3"* (`proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-03-personal-combat.md:210`). Under step 2, a body ceiling reaches the fight as seeded damage, not as `end`. CP-T03-07's re-base reads this section.

---

## 5. Its consumers' re-bases

| consumer | the exact change |
|---|---|
| **CP-T03-04** (B10-11, after CR-85's build) | **(i)** The vocation stays: `verb_capability` gains `fight` and `accept` rows naming the combat key, because both verbs contest *"the body"* (`rosters.yaml:1432`). It is still a formation mover even at control, since `VOCATIONS = frozenset(VERB_CAPABILITY.values())` (`data/verbs.py:1608`) forms one `train` Candidate per vocation (`decision/options.py:224-235`). The key's name is the item's, see §10. **(ii) Deleted:** *"the seam derives the Combatant's skill term from `capability["arms"]` by one formula beside `party_end`"*. CR-85's build already routes `faculty` into the pool and Ob, so CP-T03-04 writes no formula. **(iii)** Stays: the authored overlay values, which are content. **(iv) Build-by-doing is NOT absorbed by the practice addend:** `practice` counts an act only at `DEGREE_STEP["Success"]` or better (`queries/world_q.py:4128-4131`), and `DEGREE_STEP` is keyed by the ladder's four labels (`data/rosters.py:914-915`). A fight's Event carries combat's own bands, `Felled`, `Wounded` or `Untouched` (`rosters.yaml:900-912`), which `DEGREE_STEP.get(…, 0)` reads below Success, so practice counts no fight. CP-T03-04 keeps (iv) as its home wrote it, or teaches `practice` to read combat's bands. That choice is CP-T03-04's at its re-base. **Falsifier re-base:** *"the history-5 row (87.8 %)"* is a **conflict, not a host**. That figure was measured with the five σ terms live and against a default of 3. After CR-85 a faculty-5 party against the season default (2) differs by pool and Ob only. CP-T03-04's falsifier re-measures its own row on the post-CR-85 workbench (faculty 5 against 2, n stated) and asserts the seam reproduces that row. The 87.8 % is not reused. |
| **CP-T03-05** (B10-11, after CR-85's build) | The repair (AM-C-02, `workplans/valoria_master_workplan_v11_part13.md:343-347`) already deleted the matchup table. `tools/export_pc_matchup.py` and `engine/engine_params/pc_matchup.json` do not exist at base. So "the table would stale" is moot. **Change:** `fight_estimate` builds its record by calling `combat_input(w, claimants, verb=verb)`, the one builder, and never assembles a `PersonalCombatInput` by hand. That way the faculty field is sampled live. Its falsifier (display = realised shares; no season draw consumed) holds across CR-85 unchanged. |
| **PC-14** (B10-10b, before CR-85's build) | **Builds as written, `history` included** (its own re-base (b) says so). CR-85's build then edits PC-14's storage. **Item (1):** the spec entry `history` (default 3, `neutral` 3) is renamed `faculty` (default 3, **no `neutral`**: after the σ deletion nothing centres on it). `registry_key` stays null, because it is not a registry attribute. **Item (4):** the centring sites at `combat_systems.py:171` and `:1441` are deleted by CR-85, so `NEUTRAL['history']` loses its readers. **Item (5):** the typed `attributes` export carries `faculty` after CR-85's re-export, with `SCHEMA_VERSION` bumped again. **Item (7):** its list of history's other uses (reading experience, parry and wind technique, bind, counter training, initiative emphasis) is exactly CR-85's deletion list. The strict xfail it keeps *"as the record"* is converted by CR-85 into a passing one-channel assertion. **Exit:** `set_attr('history', 7)` → "pool 13, Ob 3.5 and History-fed sigma terms following" is run at PC-14 as written. CR-85's build runs `set_attr('faculty', 7)` → pool 13, Ob 3.5, **and no σ term moves**. **Asks:** History's "interim home" in the spec ends at CR-85's build. |
| **PC-17** (B10-10b, before CR-85's build) | Item (2) sizes `INIT_TEMPO_LEVER_K` against `INIT_READING_K` 0.03 **and `INIT_HISTORY_K` 0.02**. CR-85 deletes the second, so the comparison keeps `INIT_READING_K` alone. **The calibration table is not moved by the deletion** if every calibration subject carries history 3 on both sides: the term is then `0.02 × 0` in every fight. CR-85's build checks that against PC-17's recorded subjects and re-runs the table only if one differed. `[UNVERIFIED: PC-17 is unbuilt; read its commit]` |
| **CP-T07-02** (B10-15) | Its revived override (`workplans/valoria_master_workplan_v11_part14.md:43`, HR-7 "REVIVED") reads `_actor_pool`'s `min(3, history + 3)` and leaves *"the term's fate"* to CR-85. **The fate:** CR-85's build replaces it with the constant 3 (§3). This is EQUAL for every history ≥ 0, so the actor adapter supplies `.spirit`, `.ts` and `.resilience` and **no `.history`**. A learned thread skill, if any, enters as `faculty` when a thread verb gains a `verb_capability` row. CR-85 schedules no such row. |
| **CR-33** (B10-10, after this design) | **Where the lifepath id is stored:** on the cast row's `lifepath:` key only, never on `Person` (§2). Its exit line *"`repr(Person)` contains no lifepath id"* stands. **Changes:** (a) its `GATE` clause is met by this design and no re-pin is owed. (b) Martial lifepaths map to no key until CP-T03-04's vocation row exists, which is CR-33's own "maps to none, recorded" rule. When CP-T03-04 lands its vocation, those rows gain the key in the same commit, which is already a formation mover. (c) The goal-commit column (§2) is not built until a value is authored. (d) Its `pool_default` grant is confirmed to change no pool at **every** scale, combat included, once CR-85's build lands (§1.3 (b)). |

**FALSIFIER (5).** Each consumer's own falsifier, run on CR-85's landed tree, is the test of its re-base:

- **CP-T03-04:** its re-measured faculty-5 row is reproduced through the seam.
- **CP-T03-05:** display equals realised shares, with `fight_estimate` calling `combat_input`. Planted failure: a hand-built record without `faculties` changes the shares.
- **PC-14:** `set_attr('faculty', 7)` reads pool 13, Ob 3.5 and an unchanged net σ.
- **PC-17:** its table re-run on default subjects equals the recorded one.
- **CP-T07-02:** the threadwork parity tests listed in §3 are unchanged.
- **CR-33:** `repr(Person)` carries no lifepath id.

[Today none can run: every consumer is unbuilt at `3ce1f08e`.]

---

## 6. What is not eliminated

The skill-shaped half already runs, and `ED-IN-0330`'s "bundles of skills/aptitudes" are these, with nothing new:

- **`Person.capability`**, keyed by `verb_capability`'s values (`rosters.yaml:1352-1387`), the person's held skills.
- **`faculty`** (`sigma.py:146-160`), the one pool reader: held key, else the fallback, plus addends. CR-20 adds the vocation's attribute as the base (`-04:131`).
- **`train`**, which raises a key the subject already holds (`rosters.yaml:2280-2288`, `vocation_sourced`).
- **The `practice` addend** (`queries/world_q.py:4095-4136`), dice from one's own recent good results. It does not see a fight (§5, finding P).
- **`tradition`**, combat's cognitive-mode profile (`combatant.py:101`), and with it `Combatant.skills` and `equipped` (`:115-116`), the module's own learned per-axis biases and techniques. The season does not fill them (`fight.py:52`), PC-17 populates generics in the workbench, and they are not the pool's input.
- **CR-33's `lifepath_templates`**, a lifepath expanded into capability keys at build: literally "bundles of skills".

**Finding P (recorded, not fixed here).** `practice` cannot count a fight. Its gate is the ladder's Success band, and a fight's Event carries combat's three bands (§5, CP-T03-04 (iv)). It needs no ruling and moves no hash at CR-85, because no verb maps `fight` to a key. It belongs to CP-T03-04's re-base.

---

## 7. Two things this design deliberately does not decide

- **The combat key's name.** CP-T03-04's home names it `arms`. The same subsystem's kit item names arms *matter kinds* `arms_kinds` and `arms_at_build` (`…-03-personal-combat.md:144`). A reader with no memory of the tree would take `capability["arms"]` for equipment (`CLAUDE.md` §4). Both are CP-T03-04's and CP-T03-03's. This design needs no key name, because at its build `fight` has no row (§10).
- **Aligning the module's own default (3) with the season's (`pool_default` 2).** The season always passes a value, so the module default is reached only by the workbench and by the control arm. Moving it to 2 would re-baseline every workbench calibration (T03 §3's rows, PC-17's table) for no season effect. `[ASSUMPTION; low; revert: Combatant's faculty default 2]`

---

## 8. Build contract for B10-11

- **Position:** B10-11, after CP-T03-02 and before CP-T03-05 and CP-T03-04 (`-03`, B10-11 order, line 105). It is serialised with the batch's other movers of every season fight (P13, P14), and it re-bases on CP-T03-02's landed band Event, PC-14's storage and PC-17's tempo site.
- **Commit 1 (the replacement): a declared MOVER of every seeded season that fights.** Files: `modules/combat/{core,combatant,combat_systems,wrapper,config,fight}.py` and PC-14's `modules/combat/attributes.py`; `engine/season/queries/inputs.py`; `engine/season/seam/wrappers/combat.py`; `systems/threadwork/sim/operations.py`; `systems/fieldwork/sim/knots.py`; the workbench factories; the exporters' outputs. `faculty` is imported from `seam/wrappers/sigma.py`. If a shape test refuses a wrapper-to-wrapper import, `faculty` moves to `queries/` in the same commit with both callers re-pointed: one owner, never a copy. `[UNVERIFIED: whether such a test exists]`
- **Commit 2 (§4 step 1): EQUAL.** Docstrings only. §4 step 2 is not in B10-11. It rides the first commit that passes Endurance from `Person.attributes`.
- **FALSIFIER (the plan's EXIT, made executable):**
  - A spy on `core.resolve` over a seeded season reads every roll at (8, 1.0).
  - A planted party holding the combat key at 5 rolls pool 11, and his opponent rolls against Ob 2.5. The key is planted in a test-local `VERB_CAPABILITY`, so no roster row is added.
  - **Planted failure:** the seam's read dropped reproduces (9, 1.5) and reddens.
  - **CONTROL:** the seam's value replaced by 3 for every party reproduces the pre-item season `content_hash` (§1.3).
  - The PC-03 strict xfail becomes a passing assertion of one channel.
  - `tests/valoria/test_combat_invariants.py`'s owner scan, keyed on the name `history` (`:143-147`), is re-keyed to `faculty` in the same commit. Left as it is, it would pass while observing nothing (`CLAUDE.md` §0.1 pt 2).
  - `test_resolution_pool_rounds_fractional_history` is renamed with the field.
- **Goldens:** every seeded season pin that fights is re-recorded, old to new in the commit body, stated as an intended re-pin (`CLAUDE.md` §7).
- **Exporters:** `tools/export_engine_params.py`, `tools/export_game_constants.py` and `tools/export_sim_params.py` are re-derived and each passes `--check`. This is not a hand edit (`CLAUDE.md` §6).
- **Test files the build runs mid-session** (§0.4 cl. 2): `tests/valoria/test_combat_ob_from_defender_consumers.py`, `test_combat_invariants.py`, `test_threadwork_mending_parity.py`, `test_threadwork_resilience.py`, `test_coherence_elastic_plastic.py`, `engine/tests/test_knots_ed912.py`, `engine/tests/test_thread_mending_ed871.py`, the season tests that construct a fight, and `python tools/tests_for_diff.py` at the close.

---

## 9. Where I could not verify

- **Line citations that drifted** (all opened at `3ce1f08e`):
  - `sigma.py:145-159` is now `:146-160` (`faculty`).
  - `world_q.py:4093-4113` is now `:4095-4136` (`practice`).
  - `harness/populated.py:818` is inside `goals_missing`; `seed_goals` is `:823`.
  - `core.py:115` is the `return`; `ob_from_defender` is defined at `:100`.
  - `combatant.py:93` is `def __init__`; the `history=3` default is `:94`.
  - `effects_combat.py:224` is `engine/season/loop/effects_combat.py:224`. There is no `modules/combat/effects_combat.py`.
- **A citation that is false as stated:** `seam/wrappers/combat.py:36-39` "leaves the class default 3". Those lines are a docstring, and its list of defaults omits `history`. The default is left by `modules/combat/fight.py:52` constructing `Combatant(a_id, end=a_end)` (`combatant.py:94`).
- **Lines in a design document that drifted:** CP-T03-04's home cites `decision/options.py:182-193`, `:279-280` for `train` formation; the vocation formation is now `:224-235` (`:279-280` not opened). It cites `sigma.py::_pool_of`; the function is now `_capability`/`faculty`.
- **Not opened:**
  - T03 §3's history-5 figure (87.8 %).
  - PC-14 item (4)'s other centring sites (`combat_systems.py` "about `:113,183,1436`").
  - Whether a shape test forbids a wrapper-to-wrapper import (§8).
  - `export_sim_params --check` after the build (§3).
  - PC-17's calibration subjects (§5).
- **Not run:** the post-change season. The (8, 1.0) reading is computed from the formula (`core.resolution_pool(2)` → 8, executed), not observed in a season.
- **ED-IN-0330's "the fieldwork pool's History term":** no code read was found (§ head).

---

## 10. Held back from ED-1094's merge default, and the orchestrator's decisions

**HELD BACK** (needs separate sign-off; the merge does not ratify it):

- §4 step 2, the seeded-damage crossing. It changes what a wounded person's fight means, and it schedules itself on a trigger outside this position.
- Everything else here is a ladder take, ratified on merge. The one Jordan was told is *"worth his glance"* (`-04` CR-85 ASKS) is §1's recommendation, `[ASSUMPTION; medium; Jordan to correct; revert: delete the design file; history stays]`.

**For the orchestrator:**

- (a) Whether to retire `systems/combat/sim/combat.py`, the deprecated v30 combat (§3), in a separate cleanup.
- (b) Whether CP-T03-07's entry gets the re-base line §4 names. It was not in the position's consumer list.
- (c) Writing the re-base lines of §5 into each consumer's `-04`/`-08` entry, and CR-33's GATE as met.
- (d) The combat key's name (§7) is left to CP-T03-04 and CP-T03-03. If it should be settled before CR-33's martial rows are written, it is a one-line decision.
