# GO — adversarial steelman audit

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: b1e5a08 (working tree; begun at 601e715, the two differ only in this suite's own files)

## 0. Verdict

VERDICT-PLACEHOLDER

## 1. What it is, as coded

**GO has no game code in this repository.** `godot/` holds seven Markdown documents and no `.gd`, `.tscn`,
`.tres` or `project.godot` (`git ls-files godot`; `godot/skeleton/` was deleted by GO-14 in B10-03). The
Godot project is `jordanelias/valoria-game`, a separate clone that is not attached to this session and
was not read. What this repository owns of the port is the **oracle side of a parity contract**, and that
is what this audit judges. **Where this repository ends:** at the files under `engine/engine_params/`
(the exports), the committed vectors in `engine/season/tests/test_go07_canonical_digest.py`, and Layer 1
§C.12. **Where `valoria-game` begins:** every `.gd` file, `project.godot`, its CI's engine pin, its parity
reader (`tools/check_constants_parity.py` or equivalent, GO-06), its `docs/architecture.md`, and the
`game/` scene tree. Nothing below asserts a fact about that repository or about an engine version; the
version is ED-GO-0002's.

### 1.1 What exists (built, executed this session)

| object | where | state | evidence |
|---|---|---|---|
| The portable digest (GO-07) | `engine/season/state/world.py:210-340` (the encoding table and `_encode_into`), `:1667-1726` (`content_hash`) | built; the only landed port-gate position | `build_realm(0).content_hash()` = `600d8b27147478e158553552cc1409a5`, equal to the pin at `test_go07_canonical_digest.py:681`, under `PYTHONHASHSEED` 0, 1, 2 and on CPython 3.11.18, 3.12.3, 3.13.18 (§12 E3, E5) |
| The keyed draw | `engine/season/state/ids.py:16-21` (`H`, blake2b-64 over `v1\|seed\|tick\|subject\|purpose`), `:49-92` (`draw_factory`, a `random.Random` per `(subject, purpose)`) | built; every draw of a two-season realm run at seed 0 is constructed here | 45,603 generators, 45,486 `random()` and 236 `randint`, none elsewhere, none through the process-global module (§12 E4) |
| Same-seed determinism | `tools/m1_acceptance.py` row 2 | PASS | `bbf88d55e218…` twice, seed 20260819, one headless season (§12 E1) |
| Typed exports with a round-trip `--check` | `engine/engine_params/{combat_engine_v1,game_constants,descriptors,composition,names,sim_params,battle_orders}.json` | built; six of the seven `--check`s are wired in CI (`valoria-ci.yml:130-157`; `export_sim_params` is not) | `game_constants.json` carries five constants, two collisions, three divergences, `schema_version` 1, no `engine_series` (§12 E8) |
| The play surface (the player-proxy) | `engine/season/harness/play_surface.py:47-58` (`dispatching_chooser`), `engine/season/decision/sheet.py` (`creation_sheet`, `development_space`, `chronicle`), `queries/inputs.py::PlayHost` and `loop/driver.py:434-445` (the one suspension, at ENCOUNTER, for a duel) | built; reached only by tests and harnesses | seed 0, one season: a callback returning the shipped pick leaves the hash at `5ab73af2…` (control); returning `[]` for `p_npc_001` moves it to `6e3697b1…`, 749 → 734 acts, nine Event kinds differ (§12 E6) |
| Layer 1 §C.12 | `architecture/meta/04_CODE_ARCHITECTURE.md:906-1015` | RATIFIED (ED-IN-0204): the shape→construct table and five rejected idioms | read in full |

### 1.2 What does not exist (each absence run)

`ls tools/export_season_registries.py tools/export_oracle_pins.py tools/export_oracle_draws.py
references/engine_series.yaml engine/season/harness/port_oracle.py engine/engine_params/{season_registries,oracle_pins,oracle_draws}.json`
→ every path absent. So GO-09, GO-08, GO-16, GO-01 and the `port_oracle` runner are unbuilt, as the batch
card says (B10-20 has not opened: its entry gate is B10-18b merged). `grep -c "key-log"
references/module_contracts.yaml` → 20 (GO-11 unbuilt). `grep -rnE "def explain|Derivation" engine modules`
→ 0 (§C.11's `explain` unbuilt). `registers/editorial_ledger_go.jsonl` holds one row, ED-GO-0002; no freeze
row.

### 1.3 How the season loop reaches it

It does not, and should not: the loop imports nothing of GO. The relation runs the other way. The port
re-implements `engine/season/` (state, loop, decision, queries, data, seam, manifest: 39,895 lines of
Python outside `harness/` and `tests/`, by `wc -l`), `engine/dice_engine/` (796), and the five registered
modules (`modules/`: combat 6,009, mass_battle 11,624, settlements 371, social_contest 168, fieldwork 36),
and consumes as data the registries under `engine/season/*.yaml` (18,047 lines) and the JSON exports.
The contract between the two is the content hash over a recorded-draw replay.

## 2. Steelman

Ranked by the weight each bears. Each was attacked; what survived is stated.

1. **One contract, one artifact: the content hash over a canonical encoding.** The defender's case: a port
   can only be shown to run the oracle's game by comparing complete state, and GO-07 made that comparison
   expressible in any language (tag byte, self-delimiting payload, three declared orders, floats as IEEE
   bits, an unknown type raises: `world.py:210-250`, `:330-333`). The committed vector
   (`test_go07_canonical_digest.py:85-100`) is built so a port that sorts everything by encoded bytes
   fails it. *Attack:* a `set` or `hash()`-ordered field, or an interpreter-version dependence, would break
   it; I ran the one-season realm at seed 0 under `PYTHONHASHSEED` 0, 1, 2 and under CPython 3.11, 3.12,
   3.13. *Outcome:* one hash, `5ab73af282d0779646c38839fbab85d8`, in all five runs. **Holds.**
2. **Recorded-draw replay, not generator emulation.** Layer 1 names a seeded Godot generator threaded
   like `World` (`04:927`); the plan resolves parity by the oracle exporting its draw log and the port
   replaying it. The defender's case: every draw is already addressed by `(seed, tick, subject, purpose)`,
   so replay is a lookup, logic parity is separated from generator parity, and no Mersenne Twister is
   written in GDScript. *Attack:* replay proves the port on the recorded runs and nothing else. *Outcome:*
   **holds as the mechanism for logic parity; fails as the whole contract** (F-GO-01, F-GO-03).
3. **Freeze at one recorded commit, with a declared-mover rule.** The defender's case: a port chasing a
   moving oracle never converges; every member is hash-EQUAL so the gate costs the game nothing; the
   freeze row lists what may still move. *Attack:* count how often the pinned realm moved:
   `grep -c "RE-RECORDED\|RE-PINNED" engine/season/tests/test_go07_canonical_digest.py` → 72, since
   2026-10-28. *Outcome:* **holds for formats and primitives, fails for behaviour** (F-GO-06).
4. **A port never corrects its oracle (ED-1050), and a value crosses only behind an exporter.** The
   defender's case: the one bridge that survived every architecture retirement is the generated one.
   *Attack:* find a value the port would have to hand-carry. *Outcome:* 91 mass-battle tunables are in no
   export (F-GO-04). **The rule holds; its coverage does not.**
5. **The player is the decision procedure for one person; PLAYABLE and AUTOMATED are one code path.**
   `SeasonDriver.season` receives its chooser; `dispatching_chooser` routes one person to a callback;
   `development_space` packs the player's picks through the automated chooser's own `release`. *Attack:*
   the two controls and two movers (E6, E7). *Outcome:* echo and `take_ranked` reproduce the plain hash;
   idle and a reversed pick move it. **Holds.**
6. **Layer 1's five rejected idioms.** Sound as doctrine, and the one I could exercise fired: my first
   probe reached for `vars(view)` and `View.__getattr__` raised `Forbidden … choose() reached for world
   state '__dict__' through its View` (`state/carriers.py:505`). Two of the five carry stale premises
   (F-GO-10); the rules stand without them.
7. **The stale `godot/` documents are bannered, and `CLAUDE.md` §6 forbids implementing from them.**
   Holds: all five carry a banner at their head. Weakly, because `godot/README.md` contradicts itself
   about them (F-GO-10).

## 3. Adversarial findings

Ranked worst first. "Port validity" is used where a finding blocks no row of THE NINE directly but blocks
the claim that a port runs the game the oracle runs; the batch card says the gate "moves no row of THE
NINE", and that is accurate.

### F-GO-01 · blocks port validity · the pinned slices barely enter the two largest modules

**Claim.** GO-08 pins slice 1 (two no-act seasons) and slice 2 (two computed seasons), seeds 0–2. Slice 1
excludes `decision/`, `loop/resolve.py`, `seam/` and every module but `settlements` by construction
(build file §3). Slice 2, measured, enters the combat engine for 0, 2 and 4 fights and fights 0, 0 and 1
field battle at seeds 0, 1, 2. `modules/combat` (6,009 lines) and `modules/mass_battle` (11,624 lines) are
30% of the code the port re-implements.

**Evidence.** Two computed seasons of `populated.build_realm(seed)`, `PYTHONHASHSEED=0` (E4): seed 0 builds
no generator outside `ids.py:90` and draws only `random()` and `randint`; its `roll:a field` purposes
number 3 and its Events are `field.unopposed` ×3; no `roll:the body`. Seed 1: `roll:the body` ×2, two
generators at `seam/wrappers/combat.py:397` (37 `random`, 7 `betavariate`, 7 `gauss`, 2 `randrange`);
fields `unopposed` ×3. Seed 2: `roll:the body` ×4, four generators at `combat.py:397`; one `field.lost`
(2 `gauss` draws through `ids.py:90`).

**Falsifier.** A two-season run at any of seeds 0–2 that constructs a generator at `combat.py:395/397` or
draws `gauss` through the mass-battle source would show presence. Run; outcome as above: seed 0 none,
seeds 1–2 six fights and one fought field between them.

**Touches.** R-04 (the duel and field scales), R-09. **Narrative consequence.** The two scales where a
player zooms in are the ones a port could get wrong with a green parity job. **Minimal fix.** Pin each
registered module at its own entry: a seeded scenario per composition role (`combat.fight`,
`mass_battle.resolve_field`, `fieldwork.find`, the social-contest role) called with the typed input the
seam builds, its typed outcome and draw log recorded. That is the conversion strategy's own unit ("one
module contract = one parity target", `godot_conversion_strategy_v1.md:139`) and the standing
requirement's standalone scene on the loop's code path. Proposal `11_GO_port_gate_order_and_coverage.md`.

### F-GO-02 · blocks port validity · the float contract is unstated, and Layer 1 and the plan disagree about it

**Claim.** The hash folds floats as IEEE bits, and the arithmetic that produces state and decides acts
uses functions that are not correctly rounded and one builtin whose result changed between CPython
versions. Nothing in GO-08's `primitives` pins them.

**Evidence.** (a) Hashed floats: 1,245 values after one season at seed 0, all `Person.pursuits`; at seed 2
after two seasons, 1,230 `Person.pursuits` and 4 `Person.stance` (E3, E4). `pursuits` is written by float
arithmetic (`loop/effects_information.py:643`, `:673`). (b) Transcendentals on the game path:
`decision/choose.py:466` (`-log(-log(u))`, the chooser's noise); `engine/dice_engine/sigma_leverage.py:154`
(`tanh`), `:249` (`erf`); `modules/combat/weapon_physics.py:502`, `:563` (`** PERC_EXP`), `:663` (`exp`),
`:672-723` (`tanh` ×5); `modules/mass_battle/` 44 calls (`hierarchy/units.py` 25, `core/contact.py` 6,
`perimeter.py` 5, `geometry.py` 4, `orchestration.py` 2, one each in `battle_loop.py`, `resolution.py`).
(c) Float `sum()` on the decision path: `decision/choose.py:215`; `queries/person_q.py:421`, `:502`,
`:619`, `:621`, `:696`, `:697`; `data/pursuits.py:145-147`. CPython 3.12 changed float `sum()` to
compensated summation; the tree has met this once (CR-01: `modules/combat/weapon_physics.py:42-53`,
`_ltr_sum`, "16 of 52 roster binds … measured on 3.13") and `person_q.py:630` names it. CI pins 3.11
(`valoria-ci.yml:32`); this container runs 3.13.18. (d) The build file says "the chooser's `math.log` over
them is slice 3's float pin" (`…-v10-09-build-B10-20.md:177`); `grep -rn "slice 3"` over the plan and
build files returns that line alone. Slice 3 is defined nowhere. (e) Layer 1 PART E step 13 is done when
"a headless run prints the Python oracle's hash in the integer domain" (`04:1130`); the build file says
"Slice 1 is **not integer-domain**" (`:175`, `:217`).

**Falsifier.** A hash that differs between CPython 3.11 and 3.13 would show the `sum()` hazard live. Run
(E5): seed 0, one season, identical on 3.11.18, 3.12.3 and 3.13.18. **The attack did not break it at this
seed.** The finding stands on (b), (d) and (e), which do not depend on it, and on (c) as a latent
knife-edge: a last-bit difference moves a hash only when it changes an order or a threshold.

**Touches.** R-09; every pinned hash. **Narrative consequence.** None in Python. In a port, one flipped
choice early in a season is a different history, and the hash reports only that it differs.
**Minimal fix.** One owner for float accumulation and for each transcendental the game path calls, with
the pinned runs recording each call's operand and result bits beside the draws, so a port's divergence
names a site. Proposal `11_GO_float_contract.md`. The step-13 wording is ratified text: §11.

### F-GO-03 · blocks port validity · draws are built in two places, and replay never tests the port's samplers

**Claim.** GO-16 puts the recorder on the factory in `state/ids.py` on the premise that after GO-12
"every draw goes through a keyed generator". The combat seam builds its own generator; and a port
validated by replay has unvalidated `gauss`, `betavariate`, `randrange`, `randint` and `choice`.

**Evidence.** `seam/wrappers/combat.py:386` computes `seed = int(H(...), 16)` and `:395`, `:397` call
`random.Random(seed)` directly; E4 counts 2 and 4 such generators (53 and 57 draws) at seeds 1 and 2,
none through `draw_factory`. Unseeded fallbacks remain at `seam/wrappers/sigma.py:533`,
`engine/dice_engine/dice_engine.py:210`, `:227` and `modules/combat/wrapper.py:565`
(`rng=rng or random.Random()`); GO-12 names only `modules/mass_battle/rngsource.py:45`, `:60`.
Non-uniform draw sites on the game path number nine: `queries/world_q.py:1205` (`choice`);
`dice_engine.py:212` (`randint`), `:233` (`gauss`); `modules/combat/wrapper.py:267`,
`combat_systems.py:1149` (`randrange`), `:1127` (`betavariate`); `modules/mass_battle/orchestration.py:1734`
(`gauss`), `resolution.py:50` (`randint`). CPython's `randint`, `gauss` and `betavariate` are not
functions of a fixed number of uniforms, so a port cannot reproduce them from a uniform stream; it
writes its own, and replay feeds it the oracle's returned values instead of exercising them.

**Falsifier.** The plan's own completeness test (a counting shim on `random.Random` against the recorder)
would redden on `combat.py:397`; E4 is that shim, run early. No fallback fired in E4 (zero unseeded
generators, zero global draws), so the fallbacks are unreached in computed play, not absent.

**Touches.** R-09. **Narrative consequence.** The shipped game's dice are the one component no test in
either repository would compare with the oracle's. **Minimal fix.** One draw owner whose only primitive
is a uniform and whose other samplers are its own functions of that uniform; every generator, including
the combat seam's, built by it; the recorder on the one primitive. Proposal `11_GO_one_draw_owner.md`.
It is a declared re-pin (the integer draws change stream) and must precede GO-16, GO-08 and GO-15.

### F-GO-04 · blocks port validity · 91 mass-battle tunables are read from the process environment and exported nowhere

**Claim.** The plan's GO-12 names two environment reads. There are 91, they are read at import, and the
values they default to reach no artifact a port can load.

**Evidence.** `grep -rn "os.environ" modules --include=*.py` (tests excluded): `mass_battle/config.py` 66,
`hierarchy/units.py` 12, `orchestration.py` 11, `core/exchange.py` 2. `MB_FRICTION=0 python -c "import
modules.mass_battle.config as c; print(c.MB_FRICTION)"` prints `False`; unset, `True` (E9). A scan of the
91 assigned names against `engine/engine_params/sim_params.json` finds 0 (`CASUALTY_SCALE`, `K_LINEAR`,
`ROUT_CASCADE_FRAC`, `MB_FRICTION_SIGMA` among them): `tools/export_sim_params.py` takes literals by
`ast.literal_eval` and skips a call expression (`:56-58`), and its `--check` reads "current" with
`CASUALTY_SCALE=9 MB_FRICTION=0` in the environment (E9). No other exporter reads `config.py`
(`grep -ln mass_battle tools/export_*.py` → `export_battle_orders`, `export_composition`,
`export_game_constants`).

**Falsifier.** A realm hash that moves under a flipped flag needs a fought field in the run; seed 2, two
seasons, has one. Not run (a third seven-minute run for a consequence the import-time read already
establishes). The import-time read and the export scan were run.

**Touches.** R-04 (field scale), R-09. **Narrative consequence.** Two processes with the same seed are
the same oracle only if their environments agree; the port would carry the tunables by hand, the defect
ED-1050 records. The conversion strategy named it in June ("N1: no canonical gate-vector/config manifest
— create one as the generated param export before porting", `:80`); no GO position carries it.
**Minimal fix.** GO-12's scope is all 91: each becomes a literal in `config.py` (or its owner file), a
harness that wants an A/B arm passes the value, and the mass-battle parameters join an exporter with a
`--check`. Proposal `11_GO_port_gate_order_and_coverage.md`.

### F-GO-05 · degrades the port · halts have no portable form, and GO-10 covers four sites

**Claim.** Layer 1 calls refusal-by-`raise` "the largest unpaid port cost in the tree" (`04:985`). GO-10
retypes the `except` sites that turn an exception into a game outcome and says "defect raises stay
halts". GDScript has no halt that survives a release build (`04:966-972`, Layer 1's own reading).

**Evidence.** The four sites, by symbol, now sit at `loop/resolve.py:267`, `:498`, `:1189` and
`loop/predicates.py:368` (the plan cites `:276`, `:502`, `:1137`, `:267`). `grep -rE "^\s*raise "
engine/season` outside `tests/` and `harness/`: 433; outside `data/` and `manifest/` (the boot loaders,
which Layer 1 wants to abort): **172**. The same instrument read 167 on 2026-09-05 at one directory level
and 289 on 2026-10-16 (`research/by_lane/GO_godot_port.md` T-GO-7). One typed result class exists
(`seam/contest.py:27`, `ContestError`). The Result shape is "PROPOSED, not ruled" (`04:1004`).

**Falsifier.** A typed return on the in-loop path other than `ContestError` would show presence:
`grep -rn "class .*Error\b\|class Refusal\|class .*Result\b" engine/season` (tests excluded) → `ContestError`
and a harness `ValueError` subclass only.

**Touches.** R-05's completeness (a mechanism that breaks at its extremes fails). **Narrative
consequence.** A world the oracle refuses to continue, the port continues with a fabricated absence.
**Minimal fix.** The oracle keeps raising. The contract gains what a port needs to be checked against:
the closed roster of `where` tags `ShapeGap` already carries, and a small set of planted worlds each
pinned to the tag it halts on, so the port's parity job asserts it stops at the same place. The §C.12
hunk GO-10 lands should say that a defect is a `Result` the driver returns to `game/`, which stops the
run. Proposal `11_GO_port_gate_order_and_coverage.md` §4.

### F-GO-06 · degrades the port · the gate freezes behaviour while the game is still being invented, and two of its edges are wrong

**Claim.** The freeze is right for formats and primitives and premature for behaviour; the order inside
B10-20 carries one spurious edge and misses two real ones.

**Evidence.** (a) `python -m engine.season.harness.register --requirements` is what the gate declines to
wait on: `m1_acceptance` reads 3 of 9 met, 1 not met, 5 partial (E1). The freeze row's own list of open
movers runs to some forty handles (`part3:361`). The pinned realm has been re-recorded 72 times in two
weeks. After the freeze each mover "writes an `ED-GO-` row naming old and new values" (`part5:83`): a
ledger row per golden re-record. (b) GO-05 "NEEDS: GO-01, GO-12" (`part5:208`): a manifest derived from
`composition.json` reads nothing GO-01 writes; the only link is that GO-05's exit re-runs
`export_game_constants.py --check`. (c) GO-16 needs the single draw owner (F-GO-03), which GO-12 as
scoped does not deliver. (d) GO-08 needs the float contract and a definition of slice 3 (F-GO-02).
(e) GO-01, GO-11, GO-05 and GO-09 read no game behaviour that B10-11 to B10-18b change, yet wait on
B10-18b's merge by batch membership alone; GO-01's one need, ED-GO-0002 on `main`, is met
(`registers/editorial_ledger_go.jsonl:1`).

**Falsifier.** For (b): a field of `engine_series.yaml` or `game_constants.json` read by the manifest
builder. None can exist; neither file does yet, and the entry names `composition.json` as the sole source.

**Touches.** None directly. **Narrative consequence.** Indirect and large: every design-first row
released after the freeze (`CL-SLICE`, `CL-PERSON`, `CL-OPEN`, the narration rows) is the work that makes
the game an emergent-narrative game, and each becomes a re-port. **Minimal fix.** Split the freeze: a
**contract freeze** now-or-early (encoder, `H`, the integer and float contracts, the draw-log and
registry formats, the Result shape, the module-scene pins' format) and a **behaviour pin** that is simply
the `--build` output at whatever commit the port syncs to, recorded by its own commit. `ED-GO-` rows are
for contract changes only. Proposal `11_GO_port_gate_order_and_coverage.md` §1–§2.

### F-GO-07 · degrades narrative · what the player is shown has an owner for the choice and none for the reason or the result

**Claim.** The oracle already types the player's surface (`decision/sheet.py`): a creation sheet, a
development sheet with the ranked candidate set, a chronicle of the person's own ledger. It shows what
may be done and what is held. It does not show why a candidate ranks where it does, what the person
believes the odds are, or what an act did.

**Evidence.** E7: `DevelopmentSheet` showed 22 and 32 candidates; a `Candidate` carries `verb`, `subject`,
`operands` and nothing else. `score_terms` (`decision/choose.py:193`) returns the two terms the chooser
sums and no sheet exposes them. `View.odds` exists (`view_slots` in E6) and closes over the World by
CONVENTION (`sheet.py:40-41`). `explain` and `Derivation` are absent (grep 0), though §C.11 is ratified.
The seated person's 15 Events (E7) reach him only as `claim.deposited` rows in a 119-claim ledger; nothing
relates "my act" to "what I then learned". `chronicle()` shows scars and convictions as present values
because their writers emit no Event (`sheet.py:27-33`). `harness/chronicle.py` renders the deepest causal
chain for an omniscient reader outside the simulation.

**Falsifier.** A field on `Candidate` or `DevelopmentSheet` carrying a score term, odds or cost: read the
dataclasses (`state/carriers.py`, `sheet.py:115-132`); none.

**Touches.** R-06, R-07, R-08 as the player meets them. **Narrative consequence.** Emergence the player
cannot read is noise (the literature's Tale-Spin effect, §7). A port left to invent this would re-derive
the chooser's arithmetic in GDScript, a second owner. **Minimal fix.** Three person-side readers beside
the sheet, each taking no `World`: the candidate's terms and believed odds; `explain` per §C.11; and an
aftermath reading (the claims deposited to this person since a tick whose `chain` or `doer` names his own
act). Proposal `11_GO_player_surface_contract.md`.

### F-GO-08 · blocks the standing requirement · PLAYABLE exists at one seam

**Claim.** A subsystem is playable alone only if a player can decide inside it. The driver suspends at
one step for one provider (`loop/driver.py:434-441`: `host` reaches ENCOUNTER alone, and
`seam/wrappers/combat.py:395` forwards `host.decide` to `combat.fight`). `mass_battle.resolve_field`,
the social-contest role and `fieldwork.find` take no decider.

**Evidence.** `grep -rn "decide" engine/season/seam modules` (tests excluded): the only call that passes a
decider is `combat.py:395`. The mass-battle wrapper "decides none of what they do" and hands orders from
`mass_battle.army_order` (`seam/wrappers/mass_battle.py:49`, `:205`).

**Falsifier.** A second `decide=` keyword on a module entry. None.

**Touches.** R-04 (decisions at differing scales). **Narrative consequence.** In a port, a battle, a
debate and an investigation are watched, not played. **Minimal fix.** Not GO's to build: each module
lane types its own decision points (MB: the `Orders` record MB-08 names; SC and FI: their turn). GO's
part is the rule that the port hosts a module's scene only through that typed decider, the same call-out
REM-31 built. Cross-listed in §10.

### F-GO-09 · degrades the port · no save, and the canonical encoding cannot rebuild a world

**Claim.** `World` does not serialize ("a World does not pickle", `state/world.py:390`), and GO-07's
encoding is a digest input: it omits the act store, `tick`, `world_seed` and fixtures. GO-08 ships "the
initial world in GO-07's encoding", which is enough only because an initial world has an empty act store
at tick 0.

**Evidence.** `_STATE_COLLECTIONS`, `_STATE_SEQUENCES` (`world.py:1660-1665`) and the fold (`:1700-1725`).
**Falsifier.** A decoder: `grep -rn "def _decode\|def decode" engine/season` → none.
**Touches.** None of the nine. **Narrative consequence.** A session cannot be resumed, on either side.
**Minimal fix.** Design-first, and the port's to lead: one snapshot format = the GO-07 encoding of the
hashed frames plus four named extras (seed, tick, the act store, the fixtures digest), with a decoder
tested by round trip (`decode(encode(w)).content_hash() == w.content_hash()`). Listed in §8; no proposal
this pass (weak demand, per the lane research's M-GO-9).

### F-GO-10 · hygiene · stale and contradictory text at the pointers a porter reads first

| where | says | is |
|---|---|---|
| `CURRENT.md:39` | the GO head is `godot_conversion_strategy_v1.md` (PROPOSED) | the ratified mapping is `04` §C.12; the live work is the B10-20 card; the strategy's own body marks a third of itself retired |
| `godot/README.md:5` | `godot/` "**is** the eventual `res://` project root" | the project is `valoria-game`; Layer 1 puts the scene tree in `game/` |
| `godot/README.md:13` | lists `godot_architecture_specification.md` with no flag | its own line 5 reads STALE REFERENCE |
| `04:927`, `:958` | "the RNG (unbuilt)"; rejection 4 is "not yet load-bearing, because no roll exists yet" | 45,000 draws a two-season run (E4) |
| `04:986-1000` | counts in `shape.py` and `seam.py` | neither file exists; the count is 433 / 172 today |
| `references/module_contracts.yaml` | 20 `key-log` parity values; `:1036-1037` a `golden_path` note about "the skeleton" | the Key log is retired (ED-IN-0232); the skeleton is deleted (GO-14) |
| `part5:196` (GO-01) | "the six existing constants" | `game_constants.json` holds five; `weapon_tn_modifiers` is a divergence (E8) |
| build file `:29`, `:53`, `:81` | `ids.py:87-89`; `resolve.py:276/502/1137`; `config.py:113` | `:88-90`; `:267/498/1189`; `:112`, `:114` (the plan says re-derive by symbol, so this costs nothing) |
| `references/descriptor_registry.yaml:24`, `:32` | the attribute roster is "IN FLUX … until Jordan confirms the ten" | ED-IN-0328 is `ratified`; `descriptors.json` reads `pending_tenth: None`. See §14 |

**Minimal fix.** Edits at each owner; proposal `11_GO_pointer_and_stale_text_resolutions.md`.

### F-GO-11 · hygiene · the digest test's control half is spent

`test_go07_canonical_digest.py` keeps `_old_content_hash` (`:282-311`), the `repr` digest GO-07 replaced,
and re-records its value at every mover (72 notes, about 370 of the file's 699 lines). The control meant
"the world did not move, only its digest" across one commit, `b9beec9d` → GO-07. Since then both digests
are re-read from the same run at each mover, so their agreement observes nothing (§0.1 pt 2: the
assertion can no longer see the failure it excluded). The vector half (`:49-277`) is the port's contract
and is sound; its mutation note (`:9-11`) says the vectors redden when a field is dropped.
**Minimal fix.** Delete `_old_entity_digest`, `_old_content_hash`, the `old` pins and the dated notes (they
are in `git log`); keep the vectors and one pinned `new` hash per seed. In the pointer proposal.

### F-GO-12 · hygiene · the determinism controls vary the hash seed, not the interpreter

`m1_acceptance` row 2 and exit line 3 compare runs within one interpreter. Local sessions run 3.13; CI
pins 3.11; the tree has one recorded cross-version drift (CR-01). My cross-version run did not reproduce
a drift at seed 0 (E5), so this is a latent hazard, not a live defect. **No guard is proposed** (§0.1
pt 5 would allow one, since the pins cross into the port, but the float-contract proposal removes the
cause at its owner instead).

## 4. Code matters

**Ownership and duplication.** `H` has one owner (`ids.py`; `grep -rln "def H(" engine/season` prints one
file). Generator construction has two (`ids.py:90`, `combat.py:395/397`) and four unseeded fallbacks
(F-GO-03). Float accumulation has two conventions: `_ltr_sum` in combat, builtin `sum()` in the season
(F-GO-02); by §0.06's S test (calculations consistent in methodology) that is a defect even where each
is correct. `faculty`, the pool reader, has one owner (`seam/wrappers/pool.py`).

**Dead or unreached.** In computed play at seeds 0–2 the unseeded fallbacks and the global-`random`
fallback are unreached (E4). `View.odds` is reached; `explain` does not exist. `harness/play_surface.py`
and `decision/sheet.py` are reached only by tests and probes: there is no client.

**Contract and seam fidelity.** `references/module_contracts.yaml` still describes a port that no longer
exists in this tree: `godot:` reads `no-oracle` on 19 rows, `python-oracle` on 6, `retire` on 2,
`typed-exported` on 1; `parity:` reads `key-log` on 20. `tools/export_composition.py --check` validates
vocabulary membership, so it cannot see a stale value (the plan says so, `part5:52`). `composition.json`
exports 16 roles; `registry.resolve` falls back to `resolver="unknown"` when the contracts file is
missing (`manifest/registry.py:180`), the silent default GO-12 item F8 removes. Against Layer 1 §C.12:
`World` is threaded, never global (the View refusal fired, §2 item 6); the log is an append-only list;
refusals as values exist at one site.

**Determinism.** Established within Python across processes and across three CPython minors at seed 0
(E3, E5); `m1_acceptance` row 2 PASS (E1). The environment is the one input outside the seed (F-GO-04).

**Test strength.** The GO-07 vectors can observe what they exclude (a wrong order, a dropped field, a
`repr` leak, a guessed type) and include a subprocess leg that asserts the two processes iterated the
set differently before asserting equal encodings (`:179-189`): an assertion that asserts it observed.
The control half cannot (F-GO-11). No test compares interpreters (F-GO-12).

**Performance.** One computed season of the 83-person realm took 18 s alone and about 150 s with four
probes sharing the machine (E3, E4): roughly 23,000 keyed generators a season, each a blake2b and a
Mersenne Twister seeding. That is a cost the port inherits by design (one generator per draw key) and
should measure in GDScript before it builds on it; it is not a defect here.

## 5. Design matters

**Ruled, and accepted as binding.** The engine version is ED-GO-0002's and this file asserts none. A
port never corrects its oracle (ED-1050). The Key substrate is retired (ED-IN-0232). `World` is not an
autoload, carriers are not Nodes, the log is not signals, the RNG is threaded, a refusal is a value
(§C.12, ED-IN-0204). The port does not implement the Mersenne Twister (the batch card). The conversion
strategy is PROPOSED and held; nothing here ratifies it.

**Where ruling, plan and code disagree.**

- *Step 13's "integer domain"* (ratified) against a hash that folds floats and a plan that says slice 1
  is not integer-domain. The code follows the plan. §11.
- *§C.12's Result shape* (PROPOSED inside ratified text) against 172 in-loop raises. The code raises.
- *The strategy's "Meta as single state owner"* against rejection 1. Layer 1 governs; the strategy
  carries a marker saying so (`:121`). No action.
- *"`godot/` is the eventual `res://` root"* against a separate implementation repository. The
  repository split is the fact; the sentence is stale.

**The split between oracle and runtime** (the special charge). Three kinds of thing cross, and the tree
already has the right owner for each:

| what | crosses as | owner here | state |
|---|---|---|---|
| **Rules that are data** — verbs, write matrix, rosters, offices, arrangements, venues, cohorts, goals, the governance spine, the cast, fixtures | consumed by one loader with Layer 1's boot invariants | the YAML under `engine/season/` and `DEFAULT_FIXTURES` | authored; export unbuilt (GO-09) |
| **Parameters** — combat tables, mass-battle tunables, dice constants, descriptors, names | consumed | `engine/engine_params/*.json` behind `--check` | combat, descriptors, names built; mass-battle tunables not (F-GO-04) |
| **Mechanism** — the gate, the fold, the effects, the chooser, the queries, the five modules | **re-implemented**, and proved by replay | the Python oracle | 58,000 lines, moving |
| **Evidence** — initial worlds, traces, hashes, draw and float logs, halt vectors, module-scene pins | consumed by the port's parity job only, never by the shipped game | `oracle_pins.json`, `oracle_draws.json` | unbuilt (GO-08, GO-16) |
| **The player's surface** — sheets, the chronicle, terms, odds, derivations, aftermath | **re-implemented as person-side functions; rendered by `game/`** | `decision/sheet.py`, `queries/person_q.py` | choice built; reason and result not (F-GO-07) |

Two consequences. First, the cost of the port is the third row, so every rule moved from Python into a
registry row is a rule the port never re-implements and never re-ports; the season loop's direction of
travel (typed `requires_typed` cells, `referent_class` columns, `verb_capability`) is already the port's
cheapest path, and "can this be a row?" is the question to ask of each new mechanism before the freeze.
Second, the shipped game does not run the oracle and cannot be checked against it in play: parity is a
property of pinned runs. What protects the unpinned game is that the port's samplers and arithmetic are
themselves exercised by replay (F-GO-02, F-GO-03), which is why those two findings rank above the rest.

**What the player-facing layer must show for emergence to be legible.** From §C.11 and the code, five
things, all from the played person's own holdings and never from `World`: (1) *the offer*: the candidates
his opening set formed, each with its terms (pursuit, stance) and his believed odds; (2) *the reason*: the
derivation of any value shown, from his own claims' `source`, `confidence` and `when`; (3) *the result*:
what his act did as he came to know it, and that an effect is unattributed where it is; (4) *the record*:
his ledger as held, false beliefs included (`chronicle`, built); (5) *the absence*: that something he
expected did not happen. (1)–(3) are F-GO-07; (5) has no carrier anywhere and is cross-listed to IN.

**NERS readings.**

- *The content hash as the port's contract.* N holds, narrowed (it carries oracle-to-port equality only
  on pinned runs; horizontally, PLAYABLE against AUTOMATED, it holds outright: E6, E7). Cut it and no
  object says two executions are one game. R-complete: fails at the extremes named in F-GO-02 and F-GO-05.
  S: two accumulation conventions and two generator constructors are methodology defects. E, last: one
  number for "same game" is as legible as a parity contract gets; the overhead is the encoder, which is
  earned.
- *The freeze list.* N fails as built: cut the per-mover `ED-GO-` row and nothing is lost that the pins
  file's own commit does not carry. What a cut would lose is the *contract* change record, which stays.
- *The five stale `godot/` documents.* N fails for the game (deleted, nothing behaves differently). They
  are reference, bannered, and §0.05 does not license deleting design documents; they stay.
- *`decision/sheet.py`.* N holds (cut it and a client must re-form candidates, a second generator).
  R: creation picks a seated person and cannot make one; that is IN-47's ruled shape and CL-SLICE's work.
  E: the sheet is legible about *what*; F-GO-07 is its E-defect.

**Design that exists only as prose and is therefore not yet game.** Everything under `godot/`; the
strategy's waves, ritual and dictionary; §C.11's `explain`; §C.12's Result shape; the batch card's
slices, pins and freeze. The port itself, as far as this repository can show.

SECTION-6-ONWARD
