# PC — adversarial steelman audit

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 601e715 (working tree)

Subject: personal combat. `modules/combat/` (the engine), `systems/combat/` (oracle-side data and the
workbench), `engine/season/seam/wrappers/combat.py` (the host adapter), `engine/season/seam/ladder.py`
(the band read), `engine/season/loop/effects_combat.py` (the fold's writes), the typed export
`engine/engine_params/combat_engine_v1.json`, positions B10-11 / PC-nn / CP-T03-nn, and the
player-agency, tradition-curriculum and sparring proposals. Every figure is a reading taken at this
SHA with `PYTHONHASHSEED=0`; §12 gives the command, seed and count behind each. Probe scripts and their
outputs are in the scratchpad named in §12, not in the tree.

## 0. Verdict

**Not yet: the engine is a sound resolver and a clean registered module, but as coded it is not a basis
for emergent narrative, because computed play never reaches it and, when a hand-built act does, every
fighter is the same fighter.** At seed 0 over two seasons, in the realm and in the spine, the personal
combat seam was called zero times: `fight` formed no Candidate, 84 of 84 `challenge` acts, 27 of 27
`accept` acts and 12 of 12 `capture` acts were refused, and the death census read 0 (§3 F-PC-01). All
83 persons of `build_realm(0)` carry no attribute, the default kit, faculty 2 and Endurance 4, so a
fight's outcome varies by seed and never by person (F-PC-02). At seed 1 the same instrument shows two
`capture` scenes fought out of 150 attempts on combat verbs and again no death. What the fold does with a fight is
correct and graded on the survivor's side (wounds as a body fraction, a lasting ceiling mark, custody
under `capture`, a death that names the seats it empties), but a plain `fight` ends in a death 200
times in 200, the winner gains nothing, and no witness's regard moves (F-PC-03, F-PC-04). The single
largest obstacle is therefore not in `modules/combat/`: it is the absence of occasions and of
per-person inputs on the host side. The engine's 6,000 lines are a module with almost no customers.

## 1. What it is, as coded

### 1.1 The path a fight takes (each step opened at its call site)

1. An act with verb `fight`, `accept` or `capture` declares `contests: the body`
   (`engine/season/verb_table.yaml:733`, `:951`, `:866`). The fold reaches the provider registered
   `@provider("contest", "personal_combat")`: `engine/season/seam/wrappers/combat.py:324` (`resolve`).
2. `resolve` builds one frozen `PersonalCombatInput` (`combat_input`, `combat.py:197-232`;
   `engine/season/queries/inputs.py:113-157`): the two claimants, each one's `end` (`party_end`,
   `combat.py:143-152`: authored Endurance or 4, less one per body band, floored at 1), the wound
   quantities to lift, each kit (`queries/world_q.py:3484-3509`), each `faculty`
   (`seam/wrappers/pool.py:78-100`), the duel `terms`, and the authored attributes.
3. It seeds `random.Random(int(H(world_seed, tick, a_id, "contest:<prize>:<cause>"), 16))`
   (`combat.py:388`) and calls the module entry found by composition row (`entry_for`, `:389`;
   `references/module_contracts.yaml:58-62`), never by import.
4. `modules/combat/fight.py:55-117` builds two fresh `Combatant`s (`:84-85`), binds `wrapper._TRACE`
   for the call (`:110-113`), runs `wrapper.fight(A, B, rng, terms, decide)` and returns a dict
   `{status, result, trace, ends, wound_state}`. It reads no `World`.
5. `wrapper.fight` (`modules/combat/wrapper.py:555-625`) runs up to twelve engagements. Each
   `engagement` (`:76-481`) is an approach phase (stop-hits, arrest) then a tempo-gated closed exchange:
   a Beta-drawn commit depth, a read contest, a defence mode, one `core.resolve` roll
   (`modules/combat/core.py:127-136`: continuous Normal net plus a soft-capped σ shift, banded by the
   owner ladder `degree_from_net`), damage through `core.strike`, a bind loop and a contact branch. Every
   wound passes one site (`wrapper.py:24-34`).
6. Back in the host, `seam/ladder.py:121-171` (`party_degree`) reads each party's band off his lifted
   tracker (`Felled` / `Wounded` / `Untouched`); the act's band is the worst over both (`:174-195`).
7. `loop/effects_combat.py:61-254` (`_eff_kill`) writes each party by his own band: `Felled` → body 0
   and `World.remove_person` (tenures closed, each emptied seat named); `Wounded` →
   `body × health_remaining // health_full`, floored at 1 (`:427-447`), a lasting ceiling mark at the
   deepest gate (`:394-424`), and one point of the `arms` capability where he already holds the key
   (`:271-296`). `_eff_capture` (`:333-381`) adds one `detain` edge when the subject yielded.

### 1.2 State it owns

None between calls, by design: Combatants are rebuilt per scene and the tracker's damage is zeroed at
the fight's start (`wrapper.py:570-571`). Health between scenes is `Person.body`, written by the fold.
Three process-level caches exist and are benign: `pc_engine._LOADED`, `core.band_floor`'s `lru_cache`
(`core.py:79`) and the module global `wrapper._TRACE` (`wrapper.py:19`), which is rebound for the call
and restored (see F-PC-07).

### 1.3 Execution evidence

| reading | result | source |
|---|---|---|
| plain `fight`, hand-built act through RESOLVE + ENCOUNTER + WITNESS, tiny_world, 200 world seeds | a death in 200 of 200; survivor wounded in 110, untouched in 90; survivor body 25 to 675 of 1000 (17 and 15 distinct values); ceiling marks 32; stance rows changed 0; capability grown 0 | E3 |
| `capture`, same route, 200 seeds | captive taken 97; captor yielded 88; a death 15 (10 naming a seat, `tenure.closed`); ceiling marks 84 | E4 |
| the module at its own scale, season-default mirror (faculty 2, arming, light), 1,000 fights per cell | death terms: decided 99.8%, exchange rolls Overwhelming 36% / Success 33% / Partial 13% / Fail 18%; first-wounded fighter survives 24.4% (disjoint-seed control 21.9%); at least one lead change in 35%; blood terms: 0 deaths; yield terms: 3% a felling | E5 |
| lever sizes at module scale (A's share felled; mirror 49.3%, control 46.1%) | faculty 3 v 2: 34.8%; faculty 5 v 2: 12.5%; Endurance 3 v 4: 58.8%; Endurance 1 v 4: 80.9%; dagger v arming: 95.3%; longsword v arming: 19.2%; heavy v light armour: 0.0%; both heavy: 99.7% unresolved | E5 |
| a played person's per-turn choice, 300 seeds | engage every turn = AUTOMATED exactly (52.0% / 47.7%); withdraw at the first wound: own death 14.3%, foe's 35.0%, both standing 50.7% | E6 |
| computed play, `aperture 2 0` (realm 83 persons, spine 13) | `fight` formed 0; `challenge` 84 attempted, 84 refused; `accept` 27, 27; `capture` 12, 12; `train` 85, 85; `tend` executed 37; deaths 0 | E7 |
| per-person inputs in `build_realm(0)` | 83 of 83: no attributes, kit `(arming, light)`, `faculty(fight)` 2, `party_end` 4; `arms` holders 0 | E8 |
| the typed export | `python tools/export_engine_params.py --check`: the committed JSON matches the oracle | E9 |

## 2. Steelman

Ranked by the weight each bears.

1. **One resolver, one damage site, one ladder, a reproducible draw.** Every exchange grades through
   `engine/dice_engine/dice_engine.py::degree_from_net` (`core.py:67-76`); the seed is a function of
   world seed, tick, actor and causing act; the module reads no `World` and is reached by a composition
   row. *Attack:* run the entry on a hand-built record in a fresh process and compare with the engine
   called directly (`engine/season/tests/test_combat_module.py`, read in full: three seeds, `checked ==
   3`, a non-vacuity assert). Not run here (no pytest); the probe E5/E6 reproduces determinism: engage
   every turn equals AUTOMATED to the third decimal. **Holds.**
2. **The degree is read off the scene, per party (ruled 2026-09-03/04).** No winner is mapped to a band;
   each party is written by his own tracker, so an attacker his target fells dies. *Attack:* E3's 200
   fights: actor dead 104, subject dead 96, never both standing with a death reported, `Event.ending`
   agrees with the removals. **Holds.**
3. **Outcomes are graded and recoverable where the engine is allowed to grade.** A wound is a body
   fraction, a deep wound leaves a ceiling, the body sets next season's budget and the next fight's
   Endurance, `tend` raises it, and inside a fight the first man hurt still wins a quarter of the time.
   *Attack:* E3, E5. **Holds for the survivor; fails for the loser of a plain `fight`** (F-PC-04).
4. **A death is consequential.** `remove_person` closes every edge naming the dead, each emptied seat
   earns `tenure.closed`, and witnesses hold `person.died` with the doer paired (IN-58). *Attack:* E4:
   10 of the 15 deaths were of a seat-holder and each emitted `tenure.closed`; E3's ledgers hold 296
   bystander `person.died` claims over the 200 fights. **Holds.**
5. **Violence is exceptional by ruling (ED-IN-0337), so zero fights at seed 0 is the ruling working.**
   *Attack:* the ruling says rare and belonging to war, crime and duels; E7 shows 123 attempts on combat
   verbs, every one refused, 92 of them on a kind or carrier error rather than on rarity. **Fails as a
   defence of F-PC-01; the ruling itself is accepted.**
6. **Empty content rosters are honesty, not omission.** `arms_kinds` is empty because the inventory is
   Jordan's (`engine/season/rosters.yaml:1848-1851`). *Attack:* E8. **Holds as discipline; fails as a
   game**: R-09's by-person conjunct cannot read while every input is a default.
7. **AUTOMATED and PLAYABLE are one loop.** The decider crosses the boundary as a typed view and draws
   nothing (`fight.py:103-106`, `wrapper.py:586-592`). *Attack:* E6. **Holds.**

## 3. Adversarial findings

Ranked worst first.

**F-PC-01 · blocks a requirement (R-09, R-05) · Computed play never reaches personal combat.**
Evidence: E7, `aperture_2_0.txt` lines 91, 96, 98, 116, 154, 169, 172, 174, 362 (realm) and 422, 427,
429, 447 (spine). `fight`: formed 0. `challenge`: 84 refused, last read `exists:Person=0` 65,
`with=False` 13, `dispute=False` 6. `accept`: 27 refused, all `exists:challenge=0`. `capture`: 12
refused (`with=False` 7, `exists:Person=0` 3, `individual=False` 2). Death census: 0. Causes at the
owners: `challenge` declares no `referent_class` (`verb_table.yaml:923-940`), so it forms on referents
that are not persons; its `dispute` conjunct is evaluated only in the fold although
`queries/person_q.py:148-156` reads nothing but the actor's own ledger; `accept` shares the `Record`
class with other record kinds (`verb_table.yaml:956-958`) and forms on Records that are not challenges;
`fight` forms only under `rosters.yaml:2743-2762`'s four contexts, of which `war` is empty in every
buildable world (`rosters.yaml:739-744`), `duel` needs the `challenge` Record that never mints, and
`defence` needs a prior attack. Falsifier: any `ex > 0` on these rows. Outcome: 0 at seed 0; at seed 1
(E7b) `capture` executed 2 of 18 in the realm, `challenge` was refused 105 of 105 (`exists:Person=0`
75), `accept` 27 of 27, `fight` formed 0, deaths 0. The B10-11 card records the same shape at
`eb34324f`: 0, 2 and 2 fought scenes at seeds 0 to 2, all `capture`
(`workplans/valoria_master_workplan_v11_part3.md:86`). So over two seeds and four world-seasons the
engine ran twice, and never from a duel or an assault.
Consequence: almost no chain of events inside a combat scene occurs for R-09 to grade, more than 120
scene acts per two seasons are spent on acts that cannot succeed, and a duel or an assassination
cannot arise from persons' own acts. Minimal fix: `proposals/03_PC_duel_chain_reach.md`.

**F-PC-02 · blocks a requirement (R-09 by person, R-06) · Every person is the same fighter.**
Evidence: E8. The mechanisms have landed (authored attributes `fight.py:44-52`; kits
`world_q.py:3484`; faculty `combat.py:229`; growth `effects_combat.py:271`), and each reads an empty
source: no realm person has an attribute, `arms_kinds` and `arms_at_build` are `{}`
(`rosters.yaml:1851`, `:1862`), nobody holds `arms`. Tradition, technique investment, skill axes and
disposition have no host carrier at all: `fight.py:84-85` passes none, so `tradition='none'`,
`equipped=[]`, `skills={}`, `disp=4` in every season fight. Falsifier: a count of distinct combat
inputs over the realm above 1; outcome 1. The module shows what is being withheld (E5): one point of
faculty moves a mirror's win share from about 50 to 64, a longsword to 77, heavy armour to 93 with no
deaths of its wearer. Consequence:
who fights does not matter, so a feud between a veteran and a clerk reads as a coin. Fix:
`proposals/03_PC_person_inputs_content.md` (content flagged as Jordan's).

**F-PC-03 · degrades narrative (R-01, R-07) · A fight's consequences reach other subsystems only as a
death and a body.** Read by others: `Person.body` (budget and the next fight's Endurance),
`body_ceiling` (`tend`'s bound), the tenure cascade and its named seats, the `detain` edge, and the
witnesses' deed claims. Not produced: any stance or regard change (E3: 0 stance rows in 400 fights; E6:
87 of 87 bystander regards toward a killer unmoved, on a fixture whose persons hold no pursuits, so
this is a floor reading, and the B10-11 card's realm reading is 0 of 4 survivors' regard reaching a
Candidate); anything for the winner; any sanction for a killing before witnesses; any use of the scene's
trace, which is returned (`combat.py:422`) and read by nothing but `surrender_of` (grep, non-test
readers of `"trace"`, `"winner"`, `"bouts"`, `"unresolved"`, `"parties"`: zero). `_grown` fired 0 times
because a key is never minted. Consequence: the survivor's grudge, the vendetta, the reputation of a
killer and the tale of the fight are all absent; a duel changes the roster and nothing else.
Fix: CP-T03-06 stays design-first with CHAR (dependency edge); the decisive beat is carried by
`proposals/03_PC_typed_outcome_one_door.md`.

**F-PC-04 · degrades narrative (R-09: graded, recoverable) · A plain `fight` is binary for its loser
and its roll is top-heavy.** E3: a death in 200 of 200, never both standing. E5: under death terms
99.8% decided; the exchange roll at the season default (pool 8 against Ob 1.0, base success 83.5% at
σ 0, E10) lands Overwhelming more often than any other band and Partial 13%. Graded endings exist only
under `blood` and `yield` terms, which reach the fight for `accept` and `capture` alone
(`rosters.yaml:996-1017`). H-263 stands as measured. Consequence: violence, when it comes, removes a
character every time; there are no beaten survivors to resent, ransom, pardon or return. Fix: §11
item 1 (Jordan's) and `proposals/03_PC_exits_withdrawal_recovery.md`.

**F-PC-05 · degrades narrative and playability · The one in-fight choice is free, and only a played
person has it.** E6: withdrawing at the first wound cuts a played fighter's death from 52.0% to 14.3%
with no contest, no pursuit and no world consequence (`wrapper.py:586-592`: `break`, result 0). NPCs
never withdraw (`decide=None`). The engine already owns a contested withdrawal one level down
(`combat_systems.py:979-1004`, the pursuit strike `wrapper.py:206-219`); the turn-level exit does not
use it: two exits for one act, one of them unpriced (NERS S: calculations consistent in methodology).
Falsifier: a withdraw that costs the withdrawer something in some seed; outcome none in 300. Fix:
`proposals/03_PC_exits_withdrawal_recovery.md` (the contested withdrawal is takeable; NPC concession is
§11 item 1).

**F-PC-06 · hygiene with a contract cost · The module returns an untyped dict and the seam returns
twelve keys of which the fold reads two.** `fight.py:115-117`; `combat.py:403-423`. `winner` names the
felled fighter in 11 of 200 (E3; H-119 measured 6.06%), because `wrapper.py:621-624` flips `result`
after the fell and leaves the trackers. The flip costs one draw per decided fight and changes nothing
the world reads. Every other registered module returns a typed record
(`modules/social_contest/roll.py:157` `Margin`; `modules/settlements/subsist.py:40` `SubsistOutcome`).
Fix: `proposals/03_PC_typed_outcome_one_door.md`.

**F-PC-07 · standing requirement (one code path) · One engine, two doors, and the registered door is
the narrower.** The workbench builds `Combatant`s and calls `wrapper.fight` directly
(`systems/combat/combat_engine_v1/workbench/server.py:15-37`, `trace.py:14-27`, `balance.py:16-29`),
with tradition, skills, techniques, disposition, a config overlay and `yield_decl`; the module entry
can express none of those (`fight.py:55-56`). A standalone scene built on the workbench would run
engine paths the loop cannot reach (the tradition layer, a declared `Yield`), and the loop's `terms`
and typed record are not what the workbench exercises. The workbench's server is threaded
(`server.py:18`) over a module-global trace hook, so two requests can cross traces; `trace.py:17`'s
"concurrent callers are unaffected" is false under threads. Fix: same proposal (widen the record, route
the workbench through the entry, make the trace sink a parameter as `decide` is).

**F-PC-08 · hygiene (S: one method per quantity) · The draw has second owners.** (a) `core.py:135`
inlines `soft_cap(net_sigma) * sigma_n(pool)`, the body of `sigma_leverage.net_boost`; E10 shows the
two agree to one unit in the last place, so it is a second owner, not a second answer. (b) At least
nine outcome gates are bespoke Bernoulli or logistic draws beside the ladder (read contest
`combat_systems.py:1145-1146`, neutralise and riposte `wrapper.py:344-357`, bind dominance `:434`,
counter `:361`, grab `contact.py:66-77`, displace `wrapper.py:388`, stop-hit chance `:239-240`, the
upset flip `:622`); `resolution-diagnostic` P-v. Ruled exempt for the bands; not ruled for the
substrate. (c) The Ob a person is attacked against reads `pool_default` and the practice addend; the
social contest's opposition reader excludes both, as `core.py:113-116` says of itself: two ladders for
one quantity. (d) `core.py:58` rounds the pool to an integer although fractional pools are canonical.
Fix: (a) in the typed-outcome proposal's appendix; (b) to (d) are part of §11 item 2.

**F-PC-09 · design (NERS N) · The tradition, ability and morphology-lever layer is unreachable from the
season and near-silent in the module.** Seven traditions, 30 abilities of which 21 are generic
calibration instruments (`modules/combat/ability_primitives.py:78-132`), five lever channels and
familiarity. E5: a German fighter with two techniques at level 1 reads 47.8% felled against a mirror
band of 46.1 to 49.3. The code says the same of its own anticipation term (`combat_systems.py:1343-1352`:
"OUTCOME-INVISIBLE"). Research names the shape: a deep layer the campaign does not consume becomes
decoration (T-PC-7). Fix: none in code; §5 gives the cut reading and PC-21 carries the decision.

**F-PC-10 · hygiene · Engine constants sit outside the one place the header says holds them, and
outside the export.** `config.py:1` says all tunable coefficients are in one place; 18 module-level
numeric constants in `combat_systems.py` (`:121`, `:124`, `:411-420`, `:426-428`, `:500`, `:510`,
`:517`, `:520`, `:528`, `:535`, `:1289`, `:1389`) are in no section of
`engine/engine_params/combat_engine_v1.json` (E10: 0 of 18 present). A port regenerating from the export
would hand-transcribe them (CLAUDE.md §5). Fix: move them into `CFG`; the exporter collects `CFG`
whole; values unchanged.

**F-PC-11 · hygiene · Flat-module and prose debt.** Four engine files insert their directory on
`sys.path` at import (`wrapper.py:7`, `core.py:14-17`, `combat_systems.py:4`, `contact.py`), exposing
bare names `config`, `core`, `attributes`; the workbench adds `trace.py`, which shadows the standard
library's `trace` once its directory is on the path. Sixteen lines in `modules/combat/*.py` cite
`designs/audit/` paths that no longer exist (E10). `registers/handoffs/HANDOFF_PC.md` points into
`.designs/` twice, which CLAUDE.md §1 forbids. The CR-85 proposal's Status line says nothing was built
on it; the build is in the tree (`modules/combat/attributes.py:29-37`). `combat_systems.py:107-113`
carries a `KNOWN BROKEN-LOGIC` note (38 of 53 weapons flat-topped to one tempo penalty) deferred since
ED-PC-0023 with no position.

**F-PC-12 · degrades narrative (completeness at an extreme) · There is no unarmed fighter, and "holds
no arms" means "holds an arming sword".** `modules/combat/weapons.py` has 54 records and none for an
unarmed hand (E2); `kit_of` falls back to the Combatant default. Once an inventory exists, owning no
weapon will still arm a person. H-265 stands. Fix: in the person-inputs proposal.

## 4. Code matters

- **Ownership.** Good: one wound site, one vocabulary leaf with import-time table checks
  (`core.py:240-252`), one attribute spec (`attributes.py`), one export with a round-trip. Second
  owners: F-PC-08 (a); `_wilson` in both `workbench/server.py:40` and `workbench/balance.py:46`;
  `systems/combat/combat_engine_v1/state_graph.py` restates the engagement's control flow as data that
  `wrapper.engagement` does not read (tests and the workbench read it), so the code and the graph can
  disagree with nothing to notice.
- **Dead or unreached from the game path.** `Yield` and `yield_decl` (`wrapper.py:483-501`, never
  passed by `fight.py`); the tradition layer (F-PC-09); `capabilities.py` and `state_graph.py`
  (oracle-side); the seam's `engine()` and `load_error()` probes (tests only); ten of the seam's twelve
  return keys (F-PC-06).
- **Contract and seam fidelity.** Against `architecture/meta/04_CODE_ARCHITECTURE.md:147-152` and
  `architecture/holonic_ARCHITECTURE.md` §43: typed input yes; reached by composition row yes; reads no
  `World`, holds no token, writes nothing yes; typed output **no** (F-PC-06); no state between calls yes,
  with the `_TRACE` rebinding as the one module attribute a call touches; loaded by bare name off a path
  **yes, as a declared, shrink-only departure** (`engine/substrate/pc_engine.py:1-20`), which is §43's
  named anti-pattern. `references/module_contracts.yaml:912-922` still lists eleven sub-rows as
  `PENDING` port slices under a retired vocabulary; reference only.
- **Determinism.** Sound. The seed string is unique per act; the estimate uses a private stream and
  moves no hash (`combat.py:249-254`). The order of `DEFENCE_MODES` is part of the draw contract,
  stated at its owner (`modules/combat/vocabulary.py`).
- **Test strength.** The module test can observe the failure it excludes (subprocess, oracle, counted).
  The fold tests (`test_cp_t03_00…`, read in full) drive pinned bands through the real fold and gate and
  record a hand-run mutation; they do not drive the real draw, which the capture tests do by scanning
  act ids. No test or instrument row asserts that computed play reaches a fight, and none should be
  added as a guard (CLAUDE.md §0.1 pt 5); the aperture's per-verb row is the execution artifact (§8).
  Tests were sampled, not read in full: two of fifty-seven.
- **Performance.** 200 fights in about 0.4 s; a 400-sample odds display about 0.7 s per call
  (H-251's figure, consistent with E5's wall time). Not a constraint.

## 5. Design matters

**Rulings accepted as binding and not re-raised:** the degree is read off the scene and the fold accepts
the result (2026-09-03/04); an undecided fight is legitimate and gets no tiebreak (2026-06-02); a duel
need not be lethal (RS-25); fighting is exceptional (ED-IN-0337); cohorts never fight a personal fight
(CP-T03-01); wounds never cut pools (ED-PC-0005); facing reads weapon class (the Jordan-resolved
reversal); the upset floor is a deliberate designer rule (`config.py:305-315`); the CR-85 ratification
is withdrawn (ED-IN-0351).

**Where intent, ruling and code disagree.**

| subject | intent or ruling | code | what the game follows | cost |
|---|---|---|---|---|
| "no matchup is ever certain" (the 95% cap) | `config.py:304-315` | the flip moves `result`; the fold reads trackers | the trackers | at season scale heavy against light is certain (E5: 0 deaths in 1,000); the cap is a workbench scoreboard rule only |
| a wound's persistence | CR-85 §4 step 2 (PROPOSED, held): condition arrives as seeded damage once Endurance is authored | `party_end` still cuts Endurance by band; the tracker starts clean (`combat.py:143-152`, `wrapper.py:570`) | the code | body 799 and body 501 are one fighter; a marked veteran is permanently one Endurance lower |
| the beaten yield, flee or die (the premise H-263 tests) | RS-25 covers duels | plain `fight` is lethal | the code | F-PC-04 |
| every fighter differs by attribute, kit, tradition | PC-06 K-1/K-5, CP-T03-03, PC-21 | mechanisms present, sources empty or absent | the defaults | F-PC-02 |
| the player decides once per engagement over six intents | `proposals/2026-07-26-personal-combat-player-agency-and-tradition-curriculum.md` §2 to §3 (PROPOSED, held) | one binary choice per turn, played persons only | the code | F-PC-05 |

**NERS cuts** (definitions CLAUDE.md §0.06; E scored last, as a ratio).

- *The exchange engine* (approach, commit, read, mode, roll, bind, contact). N: survives from below and
  laterally (cut it and wounds, bands and marks have no source); narrowed from above, since nothing in a
  season selects among its behaviours. R: complete at its extremes except the unarmed fighter and the
  plate stalemate, which ends unresolved by ruling. S: fails "calculations consistent" on F-PC-08. E:
  low for what N and R found; about 220 exported coefficients buy outcomes a season reads as three
  bands and a fraction. The cut would lose the graded wound, which is the part the season uses.
- *The tradition and ability layer.* N fails from above and vertically: with it removed the season is
  byte-identical and the module moves inside its noise band. It survives only as a calibration surface.
  What dies if cut: 21 generics, 9 authored abilities, five lever channels, familiarity, wariness.
  What the cut would lose: the only place a fighter's training could become visible, which PC-21 is
  designed to supply. Verdict: not game until a carrier exists; do not extend it before then.
- *Duel terms.* N survives in every direction: they are the only source of a non-lethal ending.
- *The upset flip.* N fails at season scale (nothing reads it); survives at workbench scale as a stated
  compression of reported win-rates.
- *The contact branch* (`contact.py`). Six outcomes that move only poise and initiative; R's "fully
  formed" is not met (no hold, no disarmed state persists past the beat). Hold as it stands; ED-PC-0007
  is its position.

**Design that is only prose, and so not yet game:** the six-intent Plan layer; tradition curricula; the
off-hand slot and carry context (same proposal, §12 to §13); the opponent model (PC-21); sparring
(PC-22); Spirit against circumstance (CR-95); the survivor's grudge (CP-T03-06); rescue (CP-T03-10);
multi-combatant scenes (WS-7).

## 6. Hole-register and workplan disposition, and resolutions

### 6.1 Disposition

| item | listed | verified | evidence | action |
|---|---|---|---|---|
| H-97 body lands on `end` | assumption | open, as coded | `combat.py:143-152`; E5 Endurance cells | closes when CR-85 §4 step 2 is decided (§11 item 2) |
| H-98 the fourth band | absent | **superseded** | per-party bands since CP-T03-00 give decisive against narrow as the winner's own band (E3: 90 untouched, 110 wounded) | R-PC-01 |
| H-119 two degree surfaces | measured | open | E3: 11 of 200 | R-PC-02 |
| H-123 wound magnitude | assumption | closed as an assumption | E3 body spread | re-point its `site:` from `loop/effects.py` to `loop/effects_combat.py` (R-PC-15) |
| H-184 the Wounded edge | assumption | closed as an assumption | `ladder.py:153-170` | none |
| H-251 odds sample size | assumption | closed as an assumption; no shipped caller found beyond the `estimate` provider `[UNVERIFIED: clients of sigma.odds_of not opened]` | `combat.py:235-296` | none |
| H-258 lasting mark | assumption | closed as an assumption | E3: 32 marks; E4: 84 | none |
| H-263 no exit but death | measured | open | E3 | R-PC-11, §11 item 1 |
| H-265 no unarmed fighter | measured | open | E2 | R-PC-13 |
| H-266 the log's gaps | measured | closed in part | `Event.ending` carries `(yielded, undecided)` for a failed capture in 88 of 200 (E4); weapon, armour and turns are still not carried | R-PC-05 |
| H-348 the victor reads `undecided` | measured | open | E3: every decided fight | R-PC-04 |
| H-349 none against light armour | measured | not re-measured | no campaign-level instrument (CLAUDE.md §7) | re-read with the workbench when an inventory exists |
| H-350 one kit for all | measured | open | E8 | R-PC-12 |
| H-240 `accept` binds a challenge | closed? | closed in mechanism, unreached | `verb_table.yaml:956-975`; E7: `accept` 27 of 27 refused | R-PC-08 |
| H-64 the probe corpus invented `fight` | measured | superseded | `fight` is a table row since ED-IN-0261 | close; its own text marks the stale symbol |
| H-147, H-212, H-342, H-355, H-360 | various | wrongly filed here by path | their subject is `_eff_march` | owner MB |
| H-304, H-338, H-340 | measured | wrongly filed here by path | `_eff_tend`, `_eff_forgive` | owners SE and CHAR; H-304 bears on R-PC-14 |
| CP-T03-06 survivor's grudge | design-first | open | E3, E6 | stays design-first; CHAR owns the regard side |
| CP-T03-10 rescue, CP-T03-11 guards | parked, cut | accepted | card | none |
| CL-SLICE | ratified design, build held | open; no client exists | `PlayHost(` is constructed only at `engine/season/tests/test_rem31_grid_suspension.py:80` | §9 |
| PC-21, PC-22, CR-95 | design-first | open | part17:52-90 | PC-22 moves ahead of PC-21 in §8 |
| PC-06 K-1 | landed | closed in mechanism, unreached | `fight.py:44-52`; E8: 0 persons with attributes | R-PC-12 |
| PC-06 K-5, PC-08 | leave | accepted | part5:241-264 | none |
| CR-85 build | built on an unratified design | built | `attributes.py:29-37`, `core.py:102-124` | R-PC-16; §11 item 2 |

### 6.2 Resolutions

Each is decided by the first rung of CLAUDE.md §0's ladder that answers it. `P1` to `P4` are the
proposal files of this lane under `proposals/2026-11-12-subsystem-audit-suite/proposals/`:
`P1 = 03_PC_duel_chain_reach.md`, `P2 = 03_PC_typed_outcome_one_door.md`,
`P3 = 03_PC_exits_withdrawal_recovery.md`, `P4 = 03_PC_person_inputs_content.md`.

| id | inconsistency, gap or unclear passage | decided resolution | rung | carried by |
|---|---|---|---|---|
| R-PC-01 | H-98 says a fourth band has no source; R-09 is blocked on it | close H-98: the winner's own band is the decisive-against-narrow split and is written per party; re-point R-09's `blocks:` to F-PC-01 and F-PC-02 | 1 superseded (CP-T03-00) | P2 app. |
| R-PC-02 | the seam returns `winner` and `wound_state`, which disagree in about 5% | delete `winner`, `result`, `unresolved` from what crosses to the fold; the scene is the one surface | 2 irrelevant (no reader) | P2 |
| R-PC-03 | the upset flip changes nothing the world reads | keep it as the workbench's rule; state at `config.py` that it has no season effect; whether upsets become diegetic is §11 item 3 | 1 (the 2026-09-04 ruling governs what the season reads) | P2 app. |
| R-PC-04 | the fighter left standing is recorded `undecided` | add `standing` to `fight_endings`; `undecided` only when nobody is felled or yielded; a declared hash mover | 5 architecture | P2 |
| R-PC-05 | "no event says the capture failed" (H-266) | already said: `Event.ending` carries `(actor, yielded)`; correct the row; carry weapon, armour and turns as the decisive beat | 1 superseded (CP-T03-02) | P2 |
| R-PC-06 | `challenge` forms on referents that are not persons | `referent_class: Person` on the row | 4 precedent (REM-28's class on `convene`) | P1 |
| R-PC-07 | `dispute` is tested in the fold though it reads only the actor's own ledger | make it a person-side decline, so no Candidate forms without a dispute | 5 architecture (AX-2 allows it; it is his own knowledge) | P1 |
| R-PC-08 | `accept` forms on Records that are not challenges | narrow its formation to Records of kind `challenge` | 4 precedent (`comply`'s kind-keyed class) | P1 |
| R-PC-09 | the module returns a dict; siblings return typed records | a frozen `CombatOutcome` in `queries/inputs.py` | 4 precedent (`Margin`, `SubsistOutcome`) | P2 |
| R-PC-10 | two doors onto one engine; `_TRACE` is a rebound module attribute | widen `PersonalCombatInput` by the fields the engine already reads; route the workbench through the entry; pass the trace sink as a parameter | 5 architecture (`decide`'s own note names the precedent not to follow) | P2 |
| R-PC-11 | withdrawal is a free exit beside a contested one | the turn-level `withdraw` resolves through `disengage_clean_p` and the pursuit strike | 5 architecture (CLAUDE.md §0: compose on the owner) | P3 |
| R-PC-12 | per-person inputs are mechanisms with empty sources | a starter inventory and seeding, proposed as `[ASSUMPTION]` content for Jordan's correction | 5, with the content itself Jordan's | P4 |
| R-PC-13 | no unarmed fighter; no arms means an arming sword | an `unarmed` record in `weapons.py` and `kit_of`'s fallback reads it once `arms_kinds` is non-empty | 5 architecture | P4 |
| R-PC-14 | one `tend` restores a body whole (C-48), against the fast-partial and slow-full recovery the design names | a swept fixture fraction of the headroom, as `_eff_tend`'s own revert states | 3 design document (#453's phrase, quoted at `effects_combat.py:774-775`) | P3 |
| R-PC-15 | stale locators and forbidden pointers (H-123's `site:`, HANDOFF_PC into `.designs/`, 16 dead `designs/audit/` citations) | re-point or delete | 3 (CLAUDE.md §1) | P2 app. |
| R-PC-16 | CR-85's Status says nothing was built; the build is in the tree | edit the Status line to "built; design unratified (ED-IN-0351)" | 1 (the commit decided it; a plan defect, §0.2) | P2 app. |
| R-PC-17 | `core.resolve` re-derives `net_boost` | call the owner; declare a possible one-unit-in-the-last-place mover | 4 precedent (CLAUDE.md §8) | P2 app. |
| R-PC-18 | 18 constants outside `CFG` and the export | move into `CFG` | 3 (`config.py:1`) | P2 app. |
| R-PC-19 | the tradition layer is presented as game | record it as oracle-side until PC-21 names a carrier; add no ability before then | 3 (PC-21 is the scheduled design) | none (no edit) |
| R-PC-20 | `state_graph.py` restates control flow nothing executes | keep as reference for the Plan-layer proposal; say so in its docstring; delete if PC-21 does not adopt it | 2 or 3 | P2 app. |
| R-PC-21 | `combat_systems.py:107-113` flat-tops 38 weapons' tempo, deferred with no position | fold into PC-08's Phase-C recalibration row by name; no fix here (a golden regeneration with no generator) | 3 (the note's own deferral) | none |

Twenty-one resolutions decided. Three questions survive the ladder and are in §11.

## 7. Research transfer

Read: `research/00_INDEX.md` (§1 and the PC rows), `research/by_lane/README.md`,
`research/by_lane/PC_personal_combat.md` (§0, §2.2 to §2.3, §7, §8.1 to §8.3, §10),
`research/game_precedent_suite/dispositions/D_T03.md` (all 50 rows). Not read in full: the rest of the
lane file, the precedent companion, `THROUGHLINES.md`, `tables/R4`, `tutorials/T05`.

**Precedents that change what to build.**

- *Griftlands: enemies surrender at a threshold; the victor spares or kills, and a public killing makes
  enemies* (D_T03 row 27; convergent with Kenshi and Jagged Alliance 2 capture, rows 17 and 36, and
  Wildermyth's mortal choice, row 33). Four independent games put a state between standing and dead and
  make the victor's disposition the story. Valoria's engine has the surrender (`wrapper.Yield`) and the
  fold has custody; the plain fight uses neither. This is the evidence behind §11 item 1 and P3.
- *Every surveyed game harms the loser whoever attacked* (row 25, seven titles). Already built
  (CP-T03-00); the research predates it. Transfer complete.
- *A deep character layer the campaign does not consume becomes decoration* (lane file T-PC-7:
  Bannerlord, The Guild 3). Applies directly to F-PC-09 and argues against extending the ability layer.
- *Total War's auto-resolve: never a second resolver; test the failure mode, not the mean* (T-PC-8).
  Honoured by the scene read; it is also the argument for R-PC-10 (one door).
- *Emergent-narrative heuristic: a complication band near 40%* (D_T03 row 39). The exchange's Partial
  is 13% and the season's middle band records the winner's cost. A lead on shape, not a number to tune
  to; it supports widening graded endings rather than re-banding the roll.
- *Kingdom Come: improvement by doing* (row 8). Built as `_grown`, which never fires because no one
  holds the key (E3); P4 seeds it.
- *XCOM, Battle Brothers, Baldur's Gate 3: show the chance* (rows 5, 22, 29). `fight_estimate` exists;
  the workplan records a Jordan no-forecast directive for the fight window `[UNVERIFIED: the directive
  itself was not opened; cited from part4:321-334]`, so this transfers only to the pre-fight card.

**Tried, did not transfer.**

- *Final Fantasy Tactics jobs as traditions; Burning Wheel test-marking; SaGa sparking.* Named, never
  surveyed, and they presuppose a progression layer the season does not have.
- *Fire Emblem and FFT "depth lives on the grid".* Supports a grid mode that does not exist; the
  mass-battle cell field is the only grid.
- *Dominions and Mount & Blade on a hero's leverage in a battle.* A null in the genre (T-PC-15) and
  nothing to bind to: no duel feeds a field.
- *The HEMA fact files.* They ground constants in the module; nothing in them bears on whether a season
  produces fights. The lane file's own verdict is that they are one unverified run.

**Nulls that are findings.** No surveyed game precedent exists for the bout itself (T-PC-6); no
research on duelling custom, terms or the yield (T-PC-5), so the three terms rest on one ruling; no
treatise or game gives a win ratio for reach (T-PC-4). None of these may be cited as support.

## 8. Best path forward

Ordered. "Alone" marks what the subsystem needs to run well by itself; "compose" what it needs to feed
the season.

| # | change | file (owner) | gate (execution artifact) | unblocks | cost | kind |
|---|---|---|---|---|---|---|
| 1 | make the duel chain formable: `challenge` on persons with a dispute, `accept` on challenge Records | `engine/season/verb_table.yaml`, `rosters.yaml`, `decision/options.py` (P1) | `aperture 2 s`, s = 0, 1, 2: `challenge` refused on `exists:Person=0` = 0; `challenge` and `accept` `ex` reported | R-05, R-09 | edit | compose |
| 2 | type the outcome, cut the unread keys, rename `standing`, carry the decisive beat | `queries/inputs.py`, `modules/combat/fight.py`, `seam/wrappers/combat.py`, `loop/effects_combat.py` (P2) | the module test's oracle comparison on the record; `content_hash` equal except the declared `standing` rename | R-01 (the tale), H-119, H-348 | small build | both |
| 3 | one door: widen the record; workbench through the entry; trace sink as a parameter | `queries/inputs.py`, `fight.py`, `workbench/server.py`, `trace.py` (P2) | a workbench trace and an entry call at one seed give identical events | standing requirement | small build | alone |
| 4 | a standalone duel scenario over the entry (§9) | a client under `engine/season/harness/`, composing `play_surface`, `PlayHost`, `fight_estimate`, `workbench/commentary.py` | a scripted run whose choices equal the chooser's ends at the AUTOMATED `content_hash`; a differing script moves it (REM-31's control) | R-04 conjunct 3, CL-SLICE | small build | alone |
| 5 | contested withdrawal | `modules/combat/wrapper.py` (P3) | E6 re-run: withdraw-at-first-wound no longer ends every scene it is called in; a pursued withdrawal draws a wound in some seeds; `decide=None` byte-identical | R-09 (recoverable, priced) | small build | alone |
| 6 | per-person inputs: starter inventory, `unarmed`, seeded `arms`, authored attributes in the realm builder | `rosters.yaml`, `modules/combat/weapons.py`, `harness/populated.py`, `data/cast.py` (P4) | E8 re-run: distinct `(kit, faculty, end)` over the realm above 1; `export_engine_params.py --check` green | R-09 by person, R-06 | small build (content Jordan's) | compose |
| 7 | sparring (PC-22) ahead of PC-21 | design file, then `verb_table.yaml`, `effects_combat.py` | `aperture`: `spar` `ex > 0` in every season; bodies unchanged | R-05, R-09: the one occasion for a fight that ED-IN-0337 does not make rare | design-first | compose |
| 8 | the beaten fighter's exit (after §11 item 1) | `rosters.yaml: duel_terms` or the module's concession rule (P3) | E3 re-run: deaths below 200 of 200 by the ruled amount | R-09, F-PC-04 | edit or small build | compose |
| 9 | the survivor's grudge (CP-T03-06) with CHAR | CHAR's regard owner; PC supplies the doer on the wound claim | the card's own reading, repeated: a survivor's regard reaches a Candidate | R-07 | design-first | compose |
| 10 | the opponent model and a tradition carrier (PC-21), or the cut of the ability layer | design file | per PC-21's falsifiers | R-06 | design-first | alone |
| 11 | hygiene: `net_boost`, constants into `CFG`, dead citations | P2 appendix | `--check` green; goldens unchanged or one declared re-record | port readiness | edit | alone |

Deletions recommended: the seam's unread return keys (step 2); the `Yield` declaration path if step 8
does not adopt it; `state_graph.py` if PC-21 does not; the 21 generic abilities if PC-21 does not adopt
them (their own revert note says how).

## 9. Playable standalone and integrated

**What exists today.**

| element | state | evidence |
|---|---|---|
| entry point | the registered entry `modules.combat.fight:fight(inp, rng, decide)`, callable on a hand-built record with no `World`; and the workbench HTTP server (trace, commentary, branch odds, Monte Carlo) | `fight.py:55`; `workbench/server.py:1-13` |
| scenario seed | none. No shipped fixture states two named persons, their kits, a cause and stakes | `tiny_world` is a probe fixture with five attribute-less persons |
| choice surface, before | which verb (`fight`, `capture`, `challenge`, `accept`), offered through `opening_set`; a four-share odds reading | `combat.py:235-296` |
| choice surface, during | `engage` or `withdraw`, once per turn, for a played person | `wrapper.py:552-553`; E6 |
| choice surface, build | none: no kit, tradition, technique or disposition can be chosen | F-PC-02 |
| outcome legibility | eighteen trace event kinds with the inputs of each decision; a commentary and a narration renderer in the workbench; `Event.ending`; the body Observation to the actor | `wrapper.py:20-40`; `workbench/commentary.py`, `narrate.py` (heads read) |
| stakes | death with its cascade, body, ceiling, custody; nothing for the winner | §3 F-PC-03 |
| end condition | of a fight: felling, terms met, yield, withdrawal, twelve turns; of a scenario: none | `wrapper.py:576-625` |
| instrument | `workbench/balance.py` (win-rate tables with Wilson intervals); this audit's probes | — |
| client | none. `PlayHost` is constructed in one test; `dispatching_chooser` has no shipped caller | `test_rem31_grid_suspension.py:80` |

**One code path?** One resolver, yes. One entry, no (F-PC-07): the workbench calls `wrapper.fight`;
the loop calls `fight.py`. A playable scene built on the workbench would not be the loop's scene.

**Layer-1 conformance as a registered module.** Conforms on: composition row, typed input, no `World`,
no token, no write, no game state between calls. Departs on: typed output (a dict); the path seam
(declared, shrink-only); a module attribute rebound per call (`_TRACE`).

**Integration, executed edges.** In: `Person.body`, `Person.attributes`, `Person.capability` (through
`faculty`), rung stores (through `kit_of`), a `challenge` Record's `stakes`, fixtures. Out: `(Person,
body)`, `(Person, exists)`, `(Person, body_ceiling)`, `(Person, capability)`, `(Tenure, until)`,
a `detain` Tenure; kinds `person.died`, `body.changed`, `tenure.closed`, `person.captured`,
`duel.yielded`, `contest.undecided`. Zoom: the fight runs inside the provider's frame at ENCOUNTER with
the driver suspended beneath it, so the other scales pause correctly by construction.

**No GM.** The engine resolves everything it reaches. What a GM would otherwise supply and nothing
does: what the victor does with a man who yields in a plain fight; what happens to a captor who yields
to his quarry (E4: 88 of 200, wounded and left); whether bystanders intervene (CP-T03-11 is cut).

**Ordered work to close each gap.**

1. One door (§8 step 3). Without it a standalone scene is a fork.
2. A scenario seed: a fixture of two authored persons (attributes, kit, an `arms` key, a cause that
   satisfies a `violence_contexts` reader, a seat for the captor), built by the same builders the realm
   uses. It needs §8 step 6's owners to exist, not their realm-wide content.
3. The client (§8 step 4): present the offered verbs with the odds reading; on a fight, call the
   provider with a `PlayHost`; render each turn from the trace with the existing commentary; end the
   scenario at death, custody, yield or disengagement and print what the world now holds (body,
   ceiling, tenures closed, claims witnesses hold). Its control is REM-31's: equal scripted choices give
   the AUTOMATED hash.
4. A priced choice inside the fight (§8 step 5), then the wider decision set, which is J-15's and the
   Plan-layer proposal's and is not decided here.
5. Stakes for the winner and a tale of the fight: the decisive beat on the band's Event (§8 step 2),
   then CP-T03-06.

A played duel that resolves correctly is available today by hand (E6). It does not yet play: there is
no seed, one binary and unpriced choice, no rendered legibility on the loop's path, and no ending
beyond the fight's.

## 10. Interfaces

| with | consumes | emits | real or designed |
|---|---|---|---|
| CORE (loop, seam, gate) | the fold's act, the ENCOUNTER token, fixtures, `H` | a `Change` with named Subjects; `Event.ending` | executed (E3, E4) |
| CHAR (persons, decision) | `body`, `attributes`, `capability`, the ledger's dispute | `body`, `body_ceiling`, `capability +1`, deed claims with a paired doer, the body Observation | executed for body and claims; attributes and capability are executed paths over empty data (E8); regard and grudge designed (CP-T03-06) |
| DICE | `degree_from_net`, `roll_net_continuous`, `soft_cap`, `sigma_n` | nothing | executed; `net_boost` re-derived (F-PC-08) |
| SC (social contest, proceedings) | a `challenge` Record and its `stakes` | `duel.yielded` | mechanism executed by hand; 0 in computed play (E7) |
| FA (factions, seats, war) | the seat a `capture` is exercised through; `Enemy` stamps for the war context | `tenure.closed` naming each emptied seat; a `detain` edge | seats and custody executed (E4); the war context is empty until CR-91 (designed) |
| SE (settlements, stores) | rung stores as arms | none (a kit is read, not consumed) | executed path over an empty roster |
| MB (mass battle) | nothing | nothing | none: no duel inside a field, no champion; `effects_combat.py` merely houses `_eff_march` |
| FI (fieldwork) | nothing | a captive for `interrogate` | designed; `interrogate` formed 0 (E7) |
| WR (world, canon) | nothing | deaths for the chronicle | the death is logged; the fight's content is not |
| GO (port) | — | `combat_engine_v1.json` | export executed and round-trip green; 18 constants outside it (F-PC-10) |

## 11. Survivors for Jordan

Three. Each was taken through the five rungs; none is superseded, irrelevant, settled by a design
document or by precedent, and in each the two options are different games.

1. **Does a beaten fighter in a plain `fight` have an exit?** (H-263.) Not settled: RS-25 speaks of
   duels; ED-IN-0337 makes violence exceptional without saying it is lethal; precedent in the tree
   points both ways (`capture: yield`, `accept: blood`, `fight` unnamed).
   *Option A, as coded:* outside a duel or an arrest a fight is to the death. Violence is rare and
   final; every fight removes a character; there are no beaten enemies to carry a story on.
   *Option B:* every fight carries a concession rule (a fighter yields at a threshold set by his own
   state, the engine's `yield` term or a Spirit-keyed variant), and what the victor does with him is the
   victor's next act (kill, hold, release). Violence is rare and consequential in more ways; death
   becomes a choice someone made. Four surveyed games converge on B (§7). P3 specifies B's mechanism so
   it can be built the day it is ruled; it changes nothing until then.
2. **What is the one input to a combat pool and its obstacle?** (ED-IN-0351, the withdrawn CR-85
   ratification; includes §4 step 2's seeded damage and F-PC-08 (c).) Already Jordan's open question;
   listed because the build runs on it today. *Option A, as built:* one `faculty` (the larger of the
   attribute and the trained key, plus practice) feeds the pool and the Ob. A trained person and a
   gifted one are the same number. *Option B:* attribute and trained skill enter separately (for
   example the attribute sets dice and the skill sets the obstacle one is attacked against). Talent and
   schooling become different kinds of fighter, at the cost of a second input on every contest.
3. **Is any matchup certain?** The 95% cap is a deliberate designer rule; the scene read is a ruling;
   together they leave the cap with no effect in the world. *Option A:* accept it; the cap stays a
   workbench convention and a plated knight cannot lose to a clerk. *Option B:* make the upset diegetic,
   as `config.py:314-315` itself suggests (a critical opening inside the exchange), so the trackers
   carry it and the world sees it. B makes every fight a risk for the favourite and changes every
   balance figure.

## 12. Evidence log

Scratchpad: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PC/`.
All runs `PYTHONHASHSEED=0`. No pytest was run. No tracked file was written by any run.

| id | command or probe | seeds, counts | outcome |
|---|---|---|---|
| E1 | `python -m engine.season.harness.register --requirements` → `requirements.txt` | — | R-01 to R-03 met; R-04, R-06 to R-09 partial; R-05 not met |
| E2 | structural scan of `weapon_physics.py` and `weapons.py` (AST, loaded dictionary) | — | 54 weapon records; no `unarmed`, `none` or `fist` key; heads: cut_thrust 18, point 14, curved_cut 12, blunt 6, straight_cut 4 |
| E3 | `probe_season_fights.py fight 200` → `season_fight_200.txt` | tiny_world, world_seed 1000 to 1199, one hand-built `fight` each, through `SeasonDriver.resolve`, `encounter`, `witness` | as §1.3 row 1; seam sign against the felled party mismatched in 11; bouts median 3 |
| E4 | `probe_season_fights.py capture 200` → `season_capture_200.txt` | same, actor holds a `dispatch` seat | as §1.3 row 2; no sign mismatch |
| E5 | `probe_module_fights.py 1000` → `module_fights_1000.txt` | `wrapper.fight` with the trace seam, seeds 0 to 999 per cell; one control cell at seeds 100000 to 100999 | as §1.3 rows 3 and 4 |
| E6 | `probe_playable.py 300` → `playable_300.txt` | provider-level, world_seed 5000 to 5299, four policies; then 60 lethal fights through the fold for bystander regard (world_seed 7000 to 7059) | as §1.3 row 5; regard unmoved 87 of 87 (the fixture's persons hold no pursuits) |
| E7 | `python -m engine.season.harness.aperture 2 0` → `aperture_2_0.txt` | seed 0, two seasons, realm and spine | as §1.3 row 6 |
| E7b | `python -m engine.season.harness.aperture 2 1` → `aperture_2_1.txt` | seed 1, two seasons, realm and spine | realm: `capture` attempted 18, executed 2; `challenge` 105 refused of 105; `accept` 27 of 27; `fight` formed 0; deaths 0. Spine: all refused, deaths 0 |
| E8 | a `python -c` reading of `build_realm(0)` | seed 0 | as §1.3 row 7; 37 of the 83 are cohorts |
| E9 | `python tools/export_engine_params.py --check` | — | round-trip verified |
| E10 | `python -c`: `soft_cap·sigma_n` against `net_boost` at four points; `p_success`; the export's sections; a regex over `combat_systems.py`; `grep -c designs/audit/` | — | equal to one unit in the last place; `p_success(1.0, 8, 0)` = 0.835; sections attributes 8, cfg 214, core 26, kit 3; 0 of 18 module constants exported; 16 dead citations |
| E11 | greps for non-test readers of the seam's return keys | — | `trace` read only by `surrender_of`; no reader of `winner`, `bouts`, `unresolved`, `seed`, `parties` |
| E12 | `python -m engine.season.harness.corpus_run` → `corpus_run.txt` | the 143-case corpus | see §13 |

Not read, or read in part: `modules/combat/weapon_physics.py` and `weapons.py` (structure and
docstring heads only, E2); the workbench files other than `server.py`, `trace.py`, `presets.py` heads
and `balance.py`'s definitions; `capabilities.py` and `state_graph.py` (imports and readers only);
`combat_armour_reference.json`; fifty-five of fifty-seven test files; the research files named in §7.

PENDING-SECTION-13
