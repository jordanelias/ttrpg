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

### 5.1 The NPC and chooser surface, as the port meets it

The statement of the NPC and AI-chooser intent is the CHAR lane's (`audits/02_CHAR_audit.md`; its
section on the intent was not yet written when this was read, so nothing here depends on its wording).
What the port needs follows from the code:

- *(a) Who decides, on what.* Each person, once per round, through `choose(p, v, s, ask_budget)` inside
  DELIBERATE's per-person map (`loop/deliberate.py:202`). The information is the `View` (slots `holder`,
  `claim_ids`, `question`, `questions`, `odds`: E6) and the person's own fields (`pursuits`, `stance`,
  `conviction`, `scar`, `capability`, `body`); the budget is `ask_budget()` (5 and 4 in E6). Visible
  reasons: none typed (F-GO-07).
- *(b) One interface for player and NPC.* Yes, executed: `dispatching_chooser` hands one person to a
  callback of the same signature, and `development_space` packs the player's picks through the automated
  chooser's `release`. Both controls reproduce the automated hash (E6, E7).
- *(c) Hard-coded NPC rules.* None in GO's surface. Three risks for the port, named so they are not
  built: `videogame_mode_spec.md` §1.8 keeps "BG Faction Priority Trees … every season" as the NPC
  faction AI, which the season loop replaced (a faction is a view and does not act); mass battle's
  AUTOMATED mode runs default orders (`massbattle.py:170-178`, cited in `requirements.yaml`), a commander
  rule outside the chooser (MB's finding); and two case needs (ARC-14, ARC-17) ask for a response "fully
  determined … via a fixed lookup … when not player-controlled", which would fork player from NPC (§13).
- *(d) Characterful and legible afterwards.* Distinguishable choices are CHAR's subject. Legible
  afterwards, for a player, means his own ledger: another person's reasons may be shown only as far as he
  holds claims about them (`source`, `doer`, `chain` on `Claim`). `harness/chronicle.py` reads the whole
  log and must stay a developer's instrument; shipped as a player view it breaches AX-2.
- *(e) Missing.* `11_GO_player_surface_contract.md`. The chooser runs in the port's core, never in
  `game/`; what is data and what is code is that proposal's table.

### 5.2 A managed battle (Jordan's stated intent, 2026-11-12: Football Manager and Total War)

The doctrine the tree already holds is ED-SC-0013 (ruled 2026-07-08; text in the quarantined
`auto_manual_resolution_duality_v1.md`, read for intent): one engine at two fidelities, "auto = the
kernel run headless, played = the same kernel run interactively", with a middle "witnessed" fidelity,
and consistency between them "by construction". The code agrees in shape: the loop calls one field
engine (`mass_battle.resolve_field`) and has no second, simplified formula. It disagrees with the older
`videogame_mode_spec.md` §1.5, which keeps a separate "Part B" auto-resolve formula; the doctrine is
later and ruled, the code follows it, and the spec's row is superseded.

What a manager-style battle needs the oracle to export and the player layer to show, against what
exists:

| the player | needs from the oracle | today |
|---|---|---|
| sets roles and instructions before the battle | the orders vocabulary as data; the typed order on the input | built: `battle_orders.json`; `queries/inputs.py::FieldOrder(role, retreat_at)` |
| watches the battle | a per-tick record on the typed outcome | not on the outcome. The engine keeps per-tick logs (`_person_report(units, members, logs)`); the only renderer in the tree is the quarantined audit's (`.audit/2026-07-29-scenario-visualization/render_scenarios.py`). That audit's finding, re-verified as far as the constants (`BATTLEFIELD_SIZE` 51, `SUBUNIT_CAP` 11, `MAX_TROOPS_PER_UNIT` 10,000 hold): a single-subunit body of 25 cells has "no geometry to compare"; a field built from person weights alone will have nothing to watch |
| intervenes during it | a decider on the module entry | absent (F-GO-08) |
| auto-resolves it, consistently | the same call with no decider | built, and it is the only path |
| reads why it went as it did | an after-action reading | partial: who broke first, each person's survivors (`_person_report`) |

What the port gate lacks for it: any pin that enters the field engine more than once (F-GO-01); the 91
tunables (F-GO-04); a trace format, so that a port wrong in 11,600 lines is wrong visibly; and a port
form for `rngsource`'s scoped source, which is a Python context variable (`rngsource.py:45`) with no
GDScript equivalent, and which the one-draw-owner proposal replaces with a threaded value.

## 6. Hole-register and workplan disposition, and resolutions

### 6.1 Positions, entries and ledger rows

`grep -n -i "godot\|gdscript" engine/season/hole_register.yaml` → 0: the register holds no GO row, and
the dossier lists none.

| item | listed | verified | evidence | action |
|---|---|---|---|---|
| GO-07 portable digest | CLOSED (B10-03b) | closed | encoder at `world.py:210-340`; build pin reproduced under 3 hash seeds and 3 interpreters (E3, E5) | none; trim its test's control half (R32) |
| GO-13 version strings | landed (B10-01) | closed | `git grep -nE "Godot 4\.[0-9]" -- README.md references/glossary.md CURRENT.md CLAUDE.md` prints nothing (E8) | none |
| GO-14 skeleton deletion | landed (B10-03) | closed | `godot/` holds seven `.md` and nothing else | none |
| GO-09 registries export | BUILD | open, unbuilt | exporter and JSON absent | early landing (R14) |
| GO-10 typed refusals | BUILD | open; under-scoped | four `except` sites; 172 in-loop raises | add the defect shape and the halt roster (R11) |
| GO-11 contracts re-derived | EDIT | open | 20 `key-log`; stale `golden_path` note | early landing (R14); R28, R29 |
| GO-12 seam port items | BUILD | open; under-scoped | 91 environment reads, not 2; five fallbacks, not 1 | R8, R10 |
| GO-16 draw recorder | BUILD | open; premise false | generators at `combat.py:397` outside the factory (E4) | re-specify on `Draw.u` (R9) |
| GO-01 version owner | BUILD | open; its one need is met | ED-GO-0002 on `main`; `engine_series.yaml` absent | early landing (R14); R30 |
| GO-05 manifest | BUILD | open; one spurious need | reads `composition.json` only | drop the GO-01 edge (R13); early landing |
| GO-08 pins | BUILD | open; two needs unnamed | "slice 3" undefined; slice 2's coverage (E4) | R1, R3, R4 |
| GO-15 FREEZE | MEASURE | open; mis-shaped | F-GO-06 | split (R12) |
| GO-06 cross-repo reader | HELD · BLK | correctly held | another repository; not checkable here | none; it gains the module-scene and float-log readers when those land |
| ED-GO-0001, ED-GO-0002 | resolved | accepted as binding | ledger rows read | none |
| ED-1054 stale navigation | open since 2026-06-30 | superseded | each of the five documents carries its banner; `CLAUDE.md` §6 says implement from none | close at step 1 (R35) |
| Strategy Part VIII, items 1–8 | `[OPEN — Jordan]` | none survives the ladder | R36–R43 | close in the handoff; nothing to Jordan |

### 6.2 Every inconsistency, gap and unclear passage, with its decided resolution

Ladder steps: 1 superseded · 2 irrelevant · 3 answered by a design document or ruling · 4 precedent ·
5 what makes sense for the architecture. Proposal files are under `proposals/` beside this audit:
**DRAW** = `11_GO_one_draw_owner.md`, **FLOAT** = `11_GO_float_contract.md`, **GATE** =
`11_GO_port_gate_order_and_coverage.md`, **SURF** = `11_GO_player_surface_contract.md`, **TEXT** =
`11_GO_pointer_and_stale_text_resolutions.md`.

| # | kind | what | resolution | step | carried by |
|---|---|---|---|---|---|
| R1 | gap | the pinned slices enter combat 0/2/4 times and a fought field 0/0/1 | pin each drawing module at its entry, input built by the seam | 3, 4 | GATE §3 |
| R2 | inconsistency | two float accumulation conventions (`_ltr_sum`; builtin `sum`) | one `ltr_sum`, every float sum on the game path through it | 4 | FLOAT A |
| R3 | gap | transcendentals decide outcomes and are pinned nowhere | one owner per function; operand and result bits recorded with the draws | 4 | FLOAT B |
| R4 | unclear | "slice 3's float pin" names a slice defined nowhere | the name is struck; the `fmath` log is that pin | 5 | FLOAT B |
| R5 | inconsistency | step 13 "in the integer domain" (ratified) against "slice 1 is not integer-domain" (adopted plan) | proposed reading: declared float state; overwrites ratified text | — | FLOAT C and §11 |
| R6 | inconsistency | generators built in two places | one constructor, `draw.seeded` | 5 | DRAW |
| R7 | gap | replay never runs the port's samplers | the oracle owns its samplers as functions of one uniform | 5 | DRAW |
| R8 | gap | four unseeded fallbacks beside the one GO-12 names | all refuse | 4 | DRAW |
| R9 | unclear | GO-16 records "every method the oracle calls" | it records the one primitive | 5 | DRAW |
| R10 | gap | 91 tunables read from the environment, exported nowhere | literals at their defaults, exported behind `--check` | 4 | GATE §5 |
| R11 | gap | a defect halt has no portable form | defect as a returned record; a pinned halt roster | 3, 5 | GATE §4 |
| R12 | inconsistency | a freeze of behaviour while the game moves; a ledger row per re-record | contract freeze with `ED-GO-` rows; behaviour pins recorded by their commit | 5, 4 | GATE §1 |
| R13 | inconsistency | GO-05 "needs" GO-01 | edge dropped | 5 | GATE §2 |
| R14 | gap | four hash-EQUAL positions held by batch membership | early landings | 4 | GATE §2 |
| R15 | gap | the offer shows no terms, odds or cost | `OfferRow`, computed once by the ranker | 3, 4 | SURF §1 |
| R16 | gap | `explain` is ratified and unbuilt | built as §C.11 states it | 3 | SURF §2 |
| R17 | gap | nothing relates an act to what the actor learned | `aftermath(p, since)` over his own ledger | 4 | SURF §3 |
| R18 | gap | scars and crises write without an Event | their rows emit one | 5 | SURF §4 (IN's edit) |
| R19 | unclear | "a player must be able to X" in 53 needs; `WAITS-ON-PLAYER` in 16 cases | read as "X is in the offer of a person so placed" | 3 | SURF §5 |
| R20 | gap | PLAYABLE at one seam | scenes hosted only through a typed decider; auto is the same call without one | 1, 4 | SURF §6; GATE §3 |
| R21 | inconsistency | `videogame_mode_spec` §1.5's second auto-resolve formula against ED-SC-0013's one engine | superseded; the code follows the doctrine; no edit (the tree is quarantined) | 1 | — |
| R22 | inconsistency | `CURRENT.md`'s GO head | names §C.12 and the B10-20 card first | 3 | TEXT 1 |
| R23 | inconsistency | "`godot/` is the eventual `res://` root" | the project is the other repository | 1 | TEXT 2 |
| R24 | inconsistency | README lists the stale spec unflagged | flagged | 3 | TEXT 3 |
| R25 | inconsistency | "the RNG (unbuilt)" | "the RNG" | 1 | TEXT 4 |
| R26 | inconsistency | rejection 4 "no roll exists yet" | restated to the built draw | 1 | TEXT 5 |
| R27 | inconsistency | rejection 5 counts files that do not exist | a command in place of a figure | 2 | TEXT 6 |
| R28 | gap | `golden_path` note about a deleted skeleton | deleted | 2 | TEXT 7 |
| R29 | unclear | what replaces `parity: key-log` | `state-hash` or `seam-io`, the second defined by the module-scene pin | 1, 3 | TEXT 8 |
| R30 | inconsistency | "the six existing constants" (five) | a command in place of a count | 3 | TEXT 9 |
| R31 | unclear | may a Godot field bind to an attribute while the registry says IN FLUX | the port binds no field or enum to an attribute name; it reads the roster from `descriptors.json` as data (§14), so the question does not arise | 5 | TEXT 10 |
| R32 | gap | a control that observes nothing | deleted, vectors kept | 2 | TEXT 11 |
| R33 | unclear | "statistical parity (second tier)" with no instrument | marker: owned samplers under replay take its place | 4 | TEXT 12 |
| R34 | unclear | "parity" means two things | *fidelity parity* and *port parity* in new text | — (word choice) | TEXT 13 |
| R35 | gap | ED-1054 open | closed: the banners are its resolution | 1 | TEXT |
| R36 | open item | strategy VIII.1 downward Key delivery | closed: the Key substrate is retired | 2 | — |
| R37 | open item | VIII.2 the Python corpus's role | closed: it is the oracle, by ED-1050 and the port gate | 3 | — |
| R38 | open item | VIII.3 faction-stat inversion | closed: a faction is a resolved view; the stat vector was deleted at `29b` (`requirements.yaml`) | 2 | — |
| R39 | open item | VIII.4 Key runtime form | already struck in the document | 1 | — |
| R40 | open item | VIII.5 autoloads | closed for the state owner by §C.12 rejection 1; which thin services exist is the other repository's choice inside "`game/` is the only place Nodes and signals appear" | 3 | — |
| R41 | open item | VIII.6 first module target | closed: Layer 1 PART E's order, and slice 1's owner list is the first port slice | 1 | — |
| R42 | open item | VIII.7 Church L+PS 4/4 against 5/5 | closed: no stat vector carries it `[UNVERIFIED that no settlement datum does]` | 2 | — |
| R43 | open item | VIII.8 standing dockets | not GO's; each sits in its own lane | 2 | — |
| R44 | gap | no save | design-first: a snapshot at a barrier boundary in the GO-07 encoding plus seed, tick, act store and fixtures digest; the UI set's "no saves mid-resolution" is the same boundary | 5 | §8 step 11; no proposal |
| R45 | gap | the UI design set is written against retired phases and clocks, and `ui` has no code, contract or `CURRENT.md` row | the typed readings of SURF are the oracle-side owner; the UI documents stay reference; a new UI design is a proposal when a client exists | 5 | SURF |
| R46 | gap | the doctrine's "witnessed" fidelity is not in code | no new mechanism: it is the automated call plus the aftermath reading | 5 | SURF §3, §6 |
| R47 | inconsistency | the plan's line numbers have drifted at five sites | none: the plan says re-derive by symbol | 3 | — |

Forty-seven resolutions; one (R5) is also a survivor for Jordan.

## 7. Research transfer

**Used, and what each changed.**

- `research/by_lane/GO_godot_port.md` (2026-10-16). Its missing-area register was the starting list, and
  each row was re-verified: M-GO-1 (a language-neutral serialization) is **closed** by GO-07, so its
  T-GO-3 "the hash is blake2b over `repr()`" is now false; M-GO-2 (a portable generator) was answered by
  replay, not by a portable algorithm, which is what leaves F-GO-03's sampler gap; M-GO-3 is GO-09;
  M-GO-8 is GO-10 in part; **M-GO-10 (resolution arithmetic) was carried into no position** and is
  F-GO-02; M-GO-4, 5, 6, 9 remain and are F-GO-07 to F-GO-09.
- `research/emergent_narrative_literature/07_apparatus.md`, Gates D and E. D5 (can the engine name the
  conditions that enabled an outcome, as a stored record), D6 (does the system retell faithfully, with a
  nameable viewpoint), E1 (what fraction of internal events reach the player), E3 (does a visible
  failure reveal a systems cause), E6 (can the player tell what hidden state his act changed). These are
  the tests behind F-GO-07; `aftermath` is D6 and E6 answered from the person's own ledger.
- `proposals/2026-09-05-proceedings-subsystem/relay/G_EMERGENCE_PRECEDENT.md`, the memory question: a
  retained memory matters when its read is coupled to a decision point, and CK3 shows about ten opinion
  terms over an uncapped calculation. Transfer: terms belong on the offer row, at the decision; and a
  display cap is a presentation rule over an uncapped reading (the UI set's Slate dock caps at 12).
- `research/game_precedent_suite/THROUGHLINES.md`, "One resolver or two?" (Total War: played or
  auto-resolved per contact; Football Manager: a fidelity ladder), with ED-SC-0013. Transfer: one call,
  with and without a decider; a pin for both.
- `.audit/2026-07-29-scenario-visualization/00_findings.md` (lesser weight; constants re-verified). Its
  method (render the engine's per-tick state and compare with a diagram) is the only instance in the
  tree of a battle made watchable, and its first finding bounds §5.2.
- `.designs/…/videogame_mode_spec.md` §3 for vocabulary only: the five ways a "GM decides" is resolved
  (authored, deterministic, AI-driven, player choice, default), used in §9. `.designs/…/valoria_ui_ux_v4_1.md`
  Part 0 (Oath II's third violation test: the UI shows nothing the character's perception cannot
  render), §1.2 (no saves mid-resolution), §2.5 (the Slate dock).

**Nulls.** `research/00_INDEX.md` §3 and §7: no game precedent or historical source for a port, "None
located"; confirmed, none found beyond the lists. `PRECEDENT.md` N-6: "No shipped game in this domain
has found a formula-legible system that critics also called deep". SURF therefore claims a typed owner
for reasons, not that legibility is solved.

**Tried, did not transfer.** The strategy's "standard deterministic-replay porting practice"
(`godot_conversion_strategy_v1.md:167`) is uncited, and the corpus holds nothing on deterministic
simulation across platforms; my recollection of that practice in other engines was not used as a
premise `[UNVERIFIED]`. The UI set's interface precedents (the dialogue-as-conviction interface, the
hex battle map) are decorative for GO until a client exists. Tactics Ogre: surveyed by the corpus with
no surviving finding.

## 8. Best path forward

*Alone* means: needed for the oracle side of the port contract to run, be observed and be exercised by
itself. *Compose* means: needed for the port to carry a game a player can read.

| # | change | where | gate (execution artifact) | unblocks | cost |
|---|---|---|---|---|---|
| 1 | Early landings: GO-01, GO-11, GO-05, GO-09 | `references/engine_series.yaml`, `references/module_contracts.yaml`, the manifest, `tools/export_season_registries.py` | each `--check` prints OK on `main` before B10-18b merges | alone | edit / small build |
| 2 | One draw owner | `engine/dice_engine/draw.py`, `state/ids.py`, the combat seam, nine sampler sites | the shim prints one site and one method; a second implementation reproduces the samplers | alone; R-09 in the port | small build, one declared re-pin |
| 3 | Float contract A and B | `engine/dice_engine/fmath.py`, about sixty call sites | equal hashes on CPython 3.11 and 3.13; the grep for `math.<fn>(` is empty | alone | small build |
| 4 | GO-12 at its real scope | `modules/mass_battle/` (91 reads), `tools/export_engine_params.py` | the grep for `os.environ` under `modules/` is empty; hashes equal | alone | small build |
| 5 | GO-10 with the defect shape and halt roster | `loop/resolve.py`, `loop/predicates.py`, `04` §C.12 (the hunk), `oracle_pins.json` | a planted defect halts at its pinned tag | alone | small build |
| 6 | Module-scene pins | `tools/export_oracle_pins.py`; scenario fixtures built by the harness builders | `--check` OK with twelve or more scenes; a changed module entry reds its scene while slices 1–2 stay green | alone; R-04's duel and field scales in the port | small build per module |
| 7 | GO-16 on `Draw.u`, GO-08, the contract freeze, the first behaviour pin | the card's files | the card's exit lines | alone | small build |
| 8 | The offer's terms, `aftermath`, `OFFER-CONTAINS` | `decision/sheet.py`, `decision/choose.py::make_ranker`, `harness/corpus_run.py` | `take_ranked` reproduces the hash at seeds 0–2; `corpus_run` prints `OFFER-CONTAINS n of 16` | compose; the player's reading of R-06, R-07, R-08 | small build |
| 9 | `explain` | `queries/person_q.py` | no `World` in its signature; a fact held by no claim appears in no derivation | compose | small build after `PersonInterior` |
| 10 | Deciders and turn views for the field, the contest and the inquiry | each module and its seam wrapper (MB, SC, FI lanes) | a played run whose decider returns the default reproduces the automated outcome | compose; R-04 conjunct 3; the standing requirement | design-first |
| 11 | A snapshot save | `state/world.py` (a decoder beside the encoder) | `decode(encode(w)).content_hash() == w.content_hash()` at a barrier boundary | compose | design-first |
| 12 | The pointer and stale-text edits | TEXT's thirteen owners | the listed checks | — | edit |

Steps 2 and 3 share one re-pin window with any other declared mover. Step 6 depends on step 2. Steps
8–11 do not wait on the freeze and none of them is a port-gate member.

## 9. Playable standalone and integrated

GO is not a registered module and has no scenario of its own. It is where every other subsystem's
playable form is hosted, so the standing requirement is read here as: **what exists, in the oracle,
for a player (or the harness's player-proxy) to play at all, and what a port would have to invent.**

| point | exists today | missing |
|---|---|---|
| Entry point | `python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0`; `populated.run`; for a seat, `play_surface.dispatching_chooser` composed by hand (probes E6, E7) | a runner that seats a person and plays: `port_oracle.py` is unbuilt and is specified as a hash printer only |
| Scenario seed | `build_realm(seed)` (83 persons); the 143 corpus cases; `creation_sheet` lists the seated persons to pick from | a scenario scoped to one subsystem (the module-scene fixtures of §8 step 6 are these) |
| Choice surface | `DevelopmentSheet`: 22 and 32 candidates, budget 5 (E7); the duel's per-turn decider (`PlayHost.decide`) | deciders for the field, the contest and the inquiry (F-GO-08); creation makes no person (IN-47's ruled shape) |
| Outcome legibility | `chronicle(p)`: ledger, beliefs, conviction and scar as present values | terms, believed odds, `explain`, the aftermath; scars and crises as events (F-GO-07) |
| Stakes | the person's `body`, holdings, tenures and standing exist in the world and move with his acts (E6: idling him removed 15 acts and changed nine Event kinds) | shown nowhere as stakes: no reading says what he stands to lose by a candidate |
| End condition | death, then `carry_on` offers the living continuation ties (`play_surface.py:61-95`); an ending classification exists as data (`ENDINGS_CLASSIFIED.yaml`) | no end state reaches a client; no save; the plan warns that `victory: true` is not the game's end (`…build-B10-20.md:185`) |
| Instrument | `test_rem30_character_sheet.py`, `test_rem31_grid_suspension.py`, `test_g2_token.py` (named by `play_surface.py:29`; not run, pytest is a close step); the probes in §12 | an instrument that plays a season through the sheet and prints what the player would have seen |
| One code path | yes at the chooser slot and at the duel: the played and automated runs are one driver, one ranker, one `release`, one module entry (controls E6, E7) | the field: one engine, but no played path to compare with |
| Layer 1 conformance | `decision/sheet.py` is person-side under the AX-2 path scan; `PlayHost` is a typed input; the one suspension is a call-out with no re-entry | `harness/play_surface.py` is the seam and lives in `harness/`, which is not game code; `View.odds` closes over `World` by CONVENTION |
| No GM | every act is resolved by the engine; using `videogame_mode_spec.md` §3's vocabulary, NPC reactions are AI-driven (the chooser) and depth and thresholds are authored or deterministic | "the player is offered options with visible consequences" has the options and not the consequences |

**Ordered work to close it:** §8 steps 8, 6, 10, 9, 11, in that order; step 8 alone makes a headless
season through the sheet a readable play session.

## 10. Interfaces

| with | GO consumes | GO emits | real or designed |
|---|---|---|---|
| CORE / IN (season loop) | `World.content_hash`, `H`, `draw_factory`, the registries, the fold's refusals | nothing into the loop; the gate's exporters read it | hash, `H`, draws: executed. Registries export, pins, draw log: designed |
| CHAR (decision) | `make_ranker`, `release`, `score_terms`, `View`, `sheet.py` | the requirement that reasons be typed readings | sheet and ranker: executed. Terms, `explain`, aftermath: designed |
| PC (combat) | `combat.fight` and its decider; `combat_engine_v1.json` | a module-scene pin; the draw type | entry, decider, export: executed (2 and 4 fights at seeds 1, 2). Pin: designed |
| MB (mass battle) | `mass_battle.resolve_field`; `battle_orders.json`; `FieldOrder` | the 91-tunable export; a module-scene pin; the need for a decider and a trace | entry and orders export: executed (one fought field at seed 2). The rest: designed |
| SC, FI | the social-contest role; `fieldwork.find` | module-scene pins; the need for deciders | entries executed in computed play (`roll:a standing`, `roll:research`, `roll:surveil`: E4). Pins and deciders: designed |
| SE (settlements) | `settlements.produce` and the larder draw, inside slice 1 | the float yield vectors (GO-08) | entry: executed every season. Vectors: designed |
| DICE | `engine/dice_engine` (`roll_pool`, the continuous roll, `sigma_leverage`) | `draw.py` and `fmath.py` as leaves beside it | dice: executed. Leaves: designed |
| WR, FA | nothing directly; their content reaches GO as registry rows and initial worlds | — | by GO-09 and GO-08, designed |
| `valoria-game` | — | every artifact under `engine/engine_params/` | `game_constants.json`'s reader is the only executed edge, and it is not checkable here |

## 11. Survivors for Jordan

One.

**Step 13's "integer domain".** Ratified Layer 1 says the Godot shell is done when "a headless run prints
the Python oracle's hash in the integer domain" (`04:1130`). The adopted plan says slice 1 is not
integer-domain, and the hash folds 1,245 floats a season. Ladder: not superseded (both texts are live);
not irrelevant; the two design documents are the two sides; no precedent decides between a ratified
architecture line and a ratified plan; and the architecture alone does not choose, because the options
buy different things.

- **C1, integer state.** `pursuits` and `stance` become fixed-point integers, the encoder refuses a
  float, and step 13 holds as written. A run is then reproducible from seed and acts on any machine,
  which makes replay saves and shareable seeds safe. Cost: a design-first rework and one re-pin with
  marginal changes of choice.
- **C2, declared float state.** Step 13 is amended to name the float contract. Nothing in the game
  moves. Reproducibility across machines is not promised, so a save is a state snapshot and a seed is
  not a shareable artefact.

They differ as games in whether "the same seed is the same world, everywhere" is a property of Valoria.
FLOAT recommends C2 now. It is Jordan's because either option rewrites a ratified sentence or a
ratified plan line.

## 12. Evidence log

All seeded runs under `PYTHONHASHSEED=0` unless a row says otherwise; `PYTHONDONTWRITEBYTECODE=1`; outputs
under `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/GO/`.

| id | command or probe | seed · seasons | outcome |
|---|---|---|---|
| E1 | `python tools/m1_acceptance.py --summary` | 20260819 · 1 (its own) | stubs 0 PASS; same-seed hash `bbf88d55e218…` PASS; THE NINE 3/9 FAIL (met 3, not met 1, partial 5; doc-derived); 24 headless seeds × 4 + 2 populated, 0 invariant violations PASS; verdict NOT MET |
| E2 | `ls` of the six unbuilt artifacts and `references/engine_series.yaml` | — | all absent |
| E3 | `go_probe.py 0 1` under `PYTHONHASHSEED` 0, 1, 2 | 0 · 1 | build `600d8b27147478e158553552cc1409a5` (equals the test pin); after one season `5ab73af282d0779646c38839fbab85d8`, 13,379 Events, 749 acts, three times; 1,245 hashed floats, all `Person.pursuits`; no NaN, no −0.0 |
| E4 | `go_probe.py <seed> 2 census` (a counting subclass in place of `random.Random`, wrappers on the module-level functions, a wrapper on `draw_factory`) | 0, 1, 2 · 2 | seed 0: `bacd687f…`, 45,603 generators all at `ids.py:90`, `random` 45,486, `randint` 236; purposes `choice` 45,482, `roll:research` 71, `roll:surveil` 22, `roll:a standing` 13, `roll:a proposition` 10, `roll:a field` 3, `roll:a matter` 2; `field.unopposed` 3. Seed 1: `8aae8412…`; 2 generators at `combat.py:397` (37 `random`, 7 `betavariate`, 7 `gauss`, 2 `randrange`); `roll:the body` 2; `field.unopposed` 3. Seed 2: `89109213…`; 4 generators at `combat.py:397` (57 draws); `roll:the body` 4; `field.lost` 1, `field.unopposed` 4; 2 `gauss` through `ids.py:90`; floats 1,230 `pursuits` + 4 `stance`. No unseeded generator and no global draw at any seed |
| E5 | `go_probe.py 0 1` under `/usr/bin/python3.11` (3.11.18) and `python3.12` (3.12.3) | 0 · 1 | build and season hashes identical to E3's (3.13.18) |
| E6 | `go_play_probe.py 0 1` (`dispatching_chooser`, `p_npc_001`) | 0 · 1 | plain `5ab73af2…`; echo equal; idle `6e3697b1…`, 13,324 Events, 734 acts, nine Event kinds differ; five callback calls; `View` slots as listed. A first version that called `vars(view)` was refused by `View.__getattr__` with `Forbidden` |
| E7 | `go_sheet_probe.py 0 1 p_npc_001` (`creation_sheet`, `seat`, `development_space`, `chronicle`) | 0 · 1 | plain and `take_ranked` `5ab73af2…`; reversed pick `0cddf258…`, 739 acts; sheets of 22 and 32 candidates, budget 5; `Candidate` fields `verb`, `subject`, `operands`; chronicle 119 claims, 49 beliefs; his acts caused 15 Events of eight kinds |
| E8 | greps and one-liners: version strings; `key-log` count; `game_constants.json` keys; `descriptors.json`; `raise` and `os.environ` censuses; the `random` and `math` censuses | — | as cited in §3 and §6 |
| E9 | `MB_FRICTION=0 python -c "import modules.mass_battle.config as c; print(c.MB_FRICTION)"`; `CASUALTY_SCALE=9 MB_FRICTION=0 python tools/export_sim_params.py --check`; a scan of the 91 names against `sim_params.json` | — | `False` (unset: `True`); `[SIM-PARAMS] current`; 0 of 91 present |
| E10 | `python -m engine.season.harness.corpus_run` | 0 · per case | 143 cases; verbs executed 23 of 67, only refused 13, never attempted 30, one with no predicate or effect; R1, R3, R4, R5 pass on all 143; the planted control flips R3; `WAITS-ON-PLAYER` 16 cases; RUNS and ENDS not computable |

**Read in full:** the brief; both dossiers; `CLAUDE.md`; `HANDOFF_GO.md` and its history; the B10-20 card
(`part3:355-378`) and the ten GO entries (`part5:6-95`, `:191-226`); the build file for B10-20;
`godot/README.md`, `godot_conversion_strategy_v1.md` and the four ED-1054 documents; `04` §C.11 and
§C.12; `state/ids.py`; `modules/mass_battle/rngsource.py`; `harness/play_surface.py`; `decision/sheet.py`;
`world.py:205-360`, `:1630-1742`; `research/00_INDEX.md`, `research/by_lane/README.md`,
`research/by_lane/GO_godot_port.md`; `chain/CASE_BRIEF.md`;
`.designs/…/auto_manual_resolution_duality_v1.md`; `.designs/…/videogame_mode_spec.md`;
`.designs/systems/ui/reference/ui_flow_skeleton_v1.md`.

**Read in part, and what was not read.**
`[SKIPPED: engine/season/tests/test_go07_canonical_digest.py:487-656 — the re-record notes; the tests and pins either side were read]`.
`[SKIPPED: godot/godot_architecture_specification.md — body beyond its head and heading list; STALE by its own status, 998 lines]`.
`[SKIPPED: .designs/systems/ui/reference/valoria_ui_ux_v4.md, _v4_1_max_audit.md, _v4_2_workplan.md and the supplement — about 300 KB; of the UI set I read the flow skeleton in full, the v4.1 index, and v4.1 Part 0, §1.2, §1.5, §2.1, §2.5, Part 8 and §12.1]`.
`[SKIPPED: the other cross-cutting .designs documents (engine_atlas, throughlines_complete, integration_proposal, campaign_architecture, campaign_modes, cogload, complete_systems_reference, conflict_architecture_proposal, early_game_ignition, companion_app) — about 300 KB; the cogload index only]`.
`[SKIPPED: .audit/ beyond 2026-07-29-scenario-visualization/00_findings.md lines 1-60 and a file listing of 2026-07-05-emergent-narrative-engine]`.
`[SKIPPED: the case files' bodies — read for the 53 needs that name a player and the brief, not case by case]`.
`[SKIPPED: research/ beyond the index, the lane file, LIT 07 Gates D–E, THROUGHLINES' resolver row, PRECEDENT N-6 and the EMG memory question]`.
The reason in each case is the reading budget of one lane after six added charges; none of the skipped
material is cited.

## 13. Provided arcs and characters — adjudication

No case need turns on a mechanism GO owns, because GO owns no mechanism in the loop. The needs nearest
it are the 53 (26 core, 25 important, 1 flavour, 1 untagged) that name a player, and the 16 cases
`corpus_run` reports as `WAITS-ON-PLAYER … a player the engine does not supply` (E10). GO adjudicates
what "a player" means in them and cross-lists the rest by the mechanism each turns on.

**The ruling reading** (`04` §C.11, ratified): the player controls a person and is that person's
decision procedure. So the engine *does* supply the player's seat (E6, E7); what `corpus_run` lacks is
only a client in it.

| cases | need (short) | hardness | represented today? | evidence | change required | owner | proposal | gate |
|---|---|---|---|---|---|---|---|---|
| ARC-R16 (×2 core), ARC-25, ARC-36, ARC-38, NPC-012, NPC-033, NPC-007 | the world acts, and arcs feed each other, with no player present or attending | core / important | **yes** | every run in §12 has no player; 749 acts and 13,379 Events in a season (E3) | none | IN | — | exists |
| ARC-R16 | unattended seasons "legible together as a single readable summary when a player finally looks" | core | **partly** | `chronicle(p)` gives the person's ledger (E7); `harness/chronicle.py` gives one chain to an outside reader | `aftermath(p, since)` | GO states, IN builds | SURF §3 | SURF gate 4 |
| ARC-47 (×2 core), ARC-R19 (core), EMG-C2 (core), ARC-25, ARC-33 | a quantity hidden from the player by default; an effect he "did not choose and may not notice" | core | **yes, as epistemics** | the `View` is claim ids; reaching past it is refused (E6); a person knows what his ledger holds | none in the loop. **Wrongly stated** where it says "counter": a stored aggregate is ruled out (PART D row 8); the hidden quantity is a Query nobody holds a claim about | IN | — | exists |
| ARC-46 | a rising quantity "observable to players as a trackable number across several periods" | important | **no** | no reading gives a person the history of a value he holds claims about | a history reading over his own claims on one `(subject, predicate)`; part of `explain`'s `Derivation.terms` | GO states, CHAR builds | SURF §2 | SURF gate 3 |
| ARC-09 | players "notice an absence" | important | **no** | no carrier for an expected event that did not occur | cross-listed; not GO's | IN | — | — |
| ARC-14, ARC-17 | a non-player's response "entirely determined by a single threshold stat" or "a fixed lookup", "when not player-controlled" | core | **no, and should not be** | one chooser serves both (E6, E7) | **wrongly stated**: it asks for a player/NPC fork in the decision. Restate as "a person whose pursuit or conviction on that axis is extreme decides predictably", which is CHAR's temperament question | CHAR | — | CHAR's |
| ARC-01, ARC-03, ARC-05 (core), ARC-47, ARC-53 (core), NSC-08, SCN-03, SCN-07 (core), EMG-C3 (core), ARC-51, NPC-013 | "players must be able to" take a named act (remove a cost, supply a pretext, force a public contest, recover, defuse, decline to investigate) | core / important | **per verb** | 23 of 67 verbs execute in the corpus run (E10) | **restated**: "a person so placed is offered X". The act is its verb's lane's | the verb's lane | SURF §5 | `OFFER-CONTAINS` |
| NPC-088 (×2 core), NPC-086, NPC-075, NPC-010, NPC-012 (core) | a person with no rank generates "a scene opportunity that brings a player into contact"; access gated by competence; an offer that is not a bribe or a threat | core / important | **partly** | a seated person's offer names other persons as subjects (E7: `p_npc_032`) | whose question names whom is `questions_for`'s; cross-listed | IN, CHAR | — | `OFFER-CONTAINS` for the pair |
| ARC-24 | a grace window "missed if the players are not present" | important | **no** | no attendance or witnessed fidelity in code (R46) | none new: the automated call plus the aftermath | IN | SURF §3 | — |
| the 16 `WAITS-ON-PLAYER` cases (NPC-001, 002, 003, 008, 011, 013, 030, 031, 032, 035, 041, 050, 070, 072, 075, 086) | the case's `who_acts` names a player | — | **the seat, yes; the client, no** | E6, E7 | re-read the class as `OFFER-CONTAINS` | GO states, IN edits `corpus_run` | SURF §5 | `corpus_run` prints n of 16 |

**What GO's changes bring up, soonest first.**

1. *Any arc, as something a player could follow*: once the offer carries terms and `aftermath` exists,
   a headless season through the sheet prints what the seated person was offered, chose and learned.
   That is the execution artifact for "legible", and it scripts nothing.
2. *The 16 `WAITS-ON-PLAYER` cases* become measurable (offered or not), not simulable end to end: their
   verbs must execute, which is their lanes' work.
3. *ARC-R16* is the one arc whose remaining need (the readable summary) is the player surface's.

**Dependency edges.** SURF §1 and §3 → CHAR (the ranker and the ledger are its files). SURF §4 → CHAR
(F-CHAR-03, F-CHAR-04: the same two writers). `OFFER-CONTAINS` → IN (`corpus_run`) and, per case, the
verb's lane. Nothing in §13 depends on the port gate, and the port gate depends on none of it.

## 14. Capability authoring surface

**(a) Where GO takes a capability as input.** Nowhere in a resolver. GO touches capabilities at two
points: the *export* a port loads, and the *sheet* a player reads.

| point | reads | from | data or code |
|---|---|---|---|
| attribute roster export | the ten `attr.*` keys, names, aliases, scale `1-7`, default | `references/descriptor_registry.yaml` → `tools/export_descriptors.py --check` → `engine/engine_params/descriptors.json` (`attributes.count` 10, `pending_tenth` None) | data, behind a blocking `--check` |
| verb → capability → attribute | `verb_capability`, `vocation_attribute`, `vocation_opposed_by` | `engine/season/rosters.yaml`, loaded by `data/rosters.py`, read once by `seam/wrappers/pool.py::faculty` | data, one reader; **not exported** until GO-09 |
| a person's capabilities | `Person.capability`, `Person.attributes` | the cast (`npcs.yaml`, `data/cast.py`), lifepath templates in `rosters.yaml` | data; reaches a port inside the initial worlds (GO-08) |
| the sheets | `CreationRow.capability`, `.attributes`; `DevelopmentSheet.capability` | copies of the person's own fields (`decision/sheet.py:74-94`, `:127`) | code that copies data; carries keys and numbers, no definition |
| combat's use of them | attributes and thresholds | `modules/combat/attributes.py`, `fight.py`, `combat_engine_v1.json` | PC's to state; exported for combat |

**(b) Data-driven or hard-coded.** For GO: the roster and the mapping are data with one owner each. The
gap is that a capability has **no definition a client can render**: the sheet shows `{"inquiry": 3}`,
and what `inquiry` is, which verbs it feeds, which attribute it starts from and how it is trained live
in three places (`rosters.yaml`'s three tables, the descriptor registry, and the `train` verb's row),
none exported together.

**(c) The target shape, as GO needs it.** One capability registry, extending the existing owner
(`engine/season/rosters.yaml`'s `verb_capability` family; the holistic stage decides whether it stays
there or moves beside `descriptor_registry.yaml`), exported whole by GO-09. For the port and the sheet
a definition must say, per capability key:

```
key            stable id, never a display name (the port binds to nothing else)
name, text     display name and one line of description (authored; the port authors none)
kind           skill | attribute | aptitude | trait        (a closed roster)
scale          range and default
feeds          the verbs or composition roles whose pool, obstacle or ceiling it enters, each with the rule's name
starts_from    the attribute key its pool starts from, if any          (today: vocation_attribute)
opposed_by     the capability the other side brings, if any            (today: vocation_opposed_by)
grows_by       the act and rule that raise it                           (today: `train`: +1 on a held key)
```

The port's rule, which is R31's resolution: **it binds no resource field, enum or script constant to a
capability or attribute name**; it loads the registry and renders whatever is there. A capability added
as data then appears on the sheet, in an offer row's terms and in `explain` with no port change.

**(d) Axioms, in the tradition's vocabulary.** GO implements none; it must be able to *show* the ones
the engine implements. From the code: *a skill supplies dice and gates nothing* (`rosters.yaml:1498-1502`:
"`capability` supplies dice and GATES NOTHING"); *an untrained attempt rolls a default pool*
(`pool_default`); *opposed rolls take the obstacle from the other side's skill* (`vocation_opposed_by`);
*advancement by training* (`train`). Lacking, as a designer would expect them on a character sheet:
*advancement by use*; *a visible difficulty before the roll* (the believed odds, SURF §1); *specialities
or tags*; *a cap or ceiling per skill shown to the player*. Whether any is wanted is CHAR's and
Jordan's; GO's part is that each, if added, arrives as a registry field and not as port code.

**(e) Proposals, ordered.** (1) GO-09 exports the capability tables whole (already its scope: every file
the loader reads). (2) SURF §1–§2: an offer row's terms and `explain`'s derivation name the capability
key that fed a pool, so "which capabilities fed this roll, by which rule" is a reading. (3) The registry
gains `name`, `text` and `kind` per key: the owning lane's proposal (CHAR), whose interface GO needs is
the block in (c).

**The interface GO needs from the merged architecture:** one exported registry keyed by stable ids,
carrying display text and the `feeds` relation; every person's capabilities as `{key: value}` in the
initial world; and every reason the engine gives for a roll or a choice expressed in those keys.
