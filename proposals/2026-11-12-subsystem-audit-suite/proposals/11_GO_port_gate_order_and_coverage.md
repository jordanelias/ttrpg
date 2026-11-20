# GO — the port gate: what it freezes, in what order, and what it must cover

Reconciled: 2026-11-12, U4 fact check (`unified/U4_FACT_CHECK.md` F-07) — "ED-SC-0013, ruled 2026-07-08" is corrected where it is quoted in §3: the ledger row (`registers/editorial_ledger_sc_archive.jsonl`, 2026-07-08) calls the doctrine "(PROPOSED) — drafted"; the binding rulings are `ED-IN-0285` and Jordan's A-1 (`audits/25_GROUNDING_ENGINE.md` G-12, opened again at the row).

Reconciled: 2026-11-12, U5d closure — folded **A-30**, **A-29** and **A-5**. GO-16 (the draw recorder) is not built: §2's order drops it and GO-08 loses the draw-log digest and gains draw vectors (`16_PESSIMIST_GO_keyed_draw_no_recorder.md`); the pins gain the surface block of `16_PESSIMIST_GO_surface_pins.md`. The freeze of §1 is of contracts; the behaviour pins are re-recorded once for the keyed draw and once for the one sampler (A-5 moves every season hash), each a declared mover named in the card. §3's module pins take inputs built by the seam, with the mass battle returning an end state (A-3).

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `R1_READ.md` §2 row A-30 and `U3_CONFLICT_LEDGER.md` C3-L3 item 3 (§1 strikes "the draw and float logs" from the behaviour pins and the plan text; parity is by vectors; §2's order drops GO-16, the head's own fold now carried into the body), §2 row A-4 (§3's decider row cites `04_MB_manager_battle_one_resolver.md` §4, PROPOSED, the general's action at each window), C3-N15 (§4's figure replaced by the command, `11_GO_pointer_and_stale_text_resolutions.md` item 6), 7b-8 and `U1_OWNERS_AND_VOCABULARY.md` D-U1-11c (§5: the 91 reads are partitioned by the one-owner rule, and **the build is `04_MB_typed_outcome_and_one_path.md` §3's, landing in B17**; this file keeps the plan-text edit and the check, so no constant has two builders); §1.4 row 151 (§4's halt shape stands; a new `raise` on a port-reached path needs a `where` tag, `U5b_PC_residue.md` §4 as reconciled); test 9 (`module_scenes` scenario names, tests, order, lands-it, tier; `Depends on:` / `Lands in batch:`).

**Depends on:** `16_PESSIMIST_GO_surface_pins.md` (B41, first in the batch); `11_GO_one_draw_owner.md`, `11_GO_float_contract.md`, `U5d_GO_owed_edits.md` (B06: the draw type, `fmath`, the vectors); `04_MB_typed_outcome_and_one_path.md` §3 (B17: the 91 reads); `04_MB_manager_battle_one_resolver.md` §4 (B20: the decider); `11_GO_player_surface_contract_B.md` (B34).
**Lands in batch:** B41 (`B41-go-port-gate`, GO), after `16_PESSIMIST_GO_surface_pins.md`.

## Status: PROPOSED

Carries audit findings F-GO-01, F-GO-04, F-GO-05, F-GO-06 and the mass-battle part of F-GO-08
(`audits/11_GO_audit.md`). Lane: GO, IN. It edits the one active plan (`workplans/valoria_master_workplan_v11_part3.md`
§1, the B10-20 card; `_part5.md`'s GO entries; the build file
`proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-20.md`). It asserts no engine
version and edits nothing in `valoria-game`.

## What it changes in `engine/season/` at runtime

Nothing in the loop. *(W3-1.)* The 91 tunables of `modules/mass_battle/`
stop being read from the process environment in B17, by `04_MB_typed_outcome_and_one_path.md` §3 (hash
EQUAL in an unset environment, which is every pinned run); this file checks it. The rest is exporters,
pins and plan text.

## 1. Split the freeze: contract now, behaviour by sync

**Problem.** B10-20 freezes pins at one commit while `register --requirements` reads three met, one not
met, five partial; the freeze row lists about forty open movers; the pinned realm was re-recorded 72
times between 2026-10-28 and this reading (`grep -c "RE-RECORDED\|RE-PINNED"
engine/season/tests/test_go07_canonical_digest.py`). After the freeze each mover "writes an `ED-GO-` row
naming old and new values" (`_part5.md:83`).

**Resolution** (ladder step 5; step 4's precedent is that a golden re-record is recorded by its commit,
`CLAUDE.md` §7).

- **The contract** is what a port is *built against* and it rarely moves: the GO-07 encoding and its
  vectors; `H`; the integer contract; the draw type and its samplers (`11_GO_one_draw_owner.md`); the
  float contract (`11_GO_float_contract.md`); the registry JSON's schema; the refusal record's roster
  and the halt roster (§4); the format of every pin. **A change to any of these writes an `ED-GO-` row.**
- **The behaviour pins** are what a port is *checked against* and they move with the game: initial
  worlds, traces, hashes, the module-scene pins (§3). *(W3-1, A-30, C3-L3: no draw or float log exists;
  the draw and `fmath` vectors are contract, in GO-08's `primitives` block.)* They are whatever
  `--build` writes at the commit the port syncs to. **A mover re-runs `--build` in its own commit and
  says so in that commit; no ledger row.** The port records the oracle SHA it synced to, on its side.

Edits. `_part3.md` B10-20 **Hash** line and `_part5.md:83` (GO-15 SOURCE) — old: "A later mover after
the freeze re-builds the pins and the draw log in the same commit and writes an `ED-GO-` row naming old
and new values and the slice it moves." New: "A later mover re-builds the pins in the same commit and
states the move in that commit (a golden re-record, said plainly). A change to the *contract*
(the encoding, `H`, the integer or float contract, the draw type, a pin's format, the refusal or halt
roster) writes an `ED-GO-` row." The freeze row keeps the oracle SHA and the digests and **drops the
freeze list**: a list of everything that might still move the game is the plan's own held rows, read
there.

**GO-15 becomes two acts**: `GO-15a` CONTRACT FREEZE (the `ED-GO-` row; needs every contract item) and
`GO-15b` FIRST BEHAVIOUR PIN (a `--build` and the card's exit lines; repeatable, no row).

## 2. The order inside B10-20

| edge | today | decided | why |
|---|---|---|---|
| GO-05 → GO-01 | "NEEDS: GO-01, GO-12" (`_part5.md:208`) | drop GO-01 | the manifest is derived from `composition.json`; it reads nothing GO-01 writes |
| GO-16 | "NEEDS: GO-12" | *(W3-1, A-30)* **not built**; the plan entry is replaced by "not built" (`11_GO_one_draw_owner.md`'s GO-16 row) | the port implements the keyed draw; there is nothing to record |
| GO-08 → the float contract | not named | NEEDS it | "slice 3's float pin" names nothing; the `fmath` stream is that pin |
| GO-08 → module-scene pins (§3) | not named | NEEDS them | slice 2 reaches the combat engine 0 / 2 / 4 times and a fought field 0 / 0 / 1 times at seeds 0 / 1 / 2 |
| GO-01, GO-11, GO-05 → B10-18b merged | held by batch membership | **early landings**, as GO-13, GO-14 and GO-07 were | each is hash-EQUAL and reads no behaviour B10-11 to B10-18b change; GO-01's one need (ED-GO-0002 on `main`) is met |
| GO-09 → B10-18b merged | held by batch membership | early landing | its `--check` then catches a registry edited without a re-export *during* the batches that edit registries, which is when it can fail |

Decided order: **early** GO-01 · GO-11 · GO-05 · GO-09; **then, in one re-pin window** the draw owner →
the float contract → GO-12 (the rest of it, §5) → GO-10 (§4) → module-scene pins (§3) → GO-08 →
GO-15a → GO-15b. GO-06 stays listed and held on the other repository.

## 3. Module-scene pins: each registered module pinned at its own entry

**Problem.** Slices 1 and 2 are season-shaped. Slice 1 excludes every module but `settlements`. Slice 2,
measured over two computed seasons, enters `combat.fight` for 0, 2 and 4 fights and resolves 0, 0 and 1
fought field at seeds 0, 1, 2. `modules/combat` and `modules/mass_battle` are 17,600 of the 58,000 lines
the port re-implements.

**Resolution** (step 3: the conversion strategy's own unit, "one module contract = one conversion unit =
one parity target", read for intent; step 4: `engine/season/harness/exercises.py` and the composition
rows are the existing owners). For each `composition_roles:` row of `references/module_contracts.yaml`
that resolves by a draw (`combat.fight`, `mass_battle.resolve_field`, the social-contest role,
`fieldwork.find`), `tools/export_oracle_pins.py` adds a `module_scenes` block:

```
module_scenes:
  - role: combat.fight
    scenario: <name>                 # a fixture world from which the SEAM builds the input (never a hand-built input)
    input:  <the typed input the seam built, in the GO-07 encoding>
    key:    <the Draw key>
    outcome: <the typed outcome, GO-07 encoding>
    trace_digest: <blake2b of the module's own per-step trace, where it returns one>
```

At least: three duels (an even match, a mismatch, one that ends by yield), three fields (line against
line; an envelopment; a rout cascade), three contested speech acts, three graded findings. *(W3-1, test 9.)*
Scenario names, one per entry, in the block's `scenario:` field: `duel_even`, `duel_mismatch`,
`duel_yield`; `field_line`, `field_envelop`, `field_rout_cascade` (the one with subunits, below);
`speech_even`, `speech_mismatch`, `speech_refused`; `finding_none`, `finding_partial`, `finding_full`
`[ASSUMPTION: names chosen here; the fixture worlds are built by the builders named below — basis: the
block needs a stable key per entry]`. The scenario
worlds are built by the same builders the corpus uses (`harness/populated.py`, `headless.py`), and the
input is produced by the seam wrapper (`seam/wrappers/combat.py::combat_input`, `mass_battle.py`'s
input builder), so the pin tests **the loop's code path**, not a parallel one.

**Mass battle, for a manager-style game** (Jordan's stated intent, 2026-11-12: Football Manager and
Total War). The port needs four things from the oracle for a battle a player manages, and has one:

| the port needs | exists | missing |
|---|---|---|
| the orders vocabulary as data | `engine/engine_params/battle_orders.json` (roles `ShieldWall`, `Hold`, `Anvil`, `Push`, `Skirmish`, `Screen`; `retreat_at`), behind `tools/export_battle_orders.py` | nothing for the vocabulary; its `--check` is wired locally and through a season test (`references/ci_checks_registry.yaml:312-318`), not as a line of CI's validators job, and exit line 4 of the card does not list it |
| the engine's tunables | — | all 91 (§5) |
| a per-tick record to watch and to explain | `massbattle.py::_person_report` (per-person survivor ratio, rout, who broke first) on the outcome | a per-tick trace on the typed outcome (positions, morale, casualties, orders in force), pinned by `trace_digest`; without it a port's divergence in 11,600 lines shows only in the final result |
| a point to intervene | — | *(W3-1, A-4)* designed: `04_MB_manager_battle_one_resolver.md` §4 (PROPOSED; B20), a general's action at each window through a decider on `mass_battle.resolve_field`, as `combat.fight` has (`seam/wrappers/combat.py:395`); GO hosts it |

Auto-resolve and the played battle are then one call with and without the decider, which is what keeps
them consistent, and the module-scene pin covers both: the automated outcome, and a played run whose
decider returns the default orders reproducing it. That is the doctrine the tree already holds
(ED-SC-0013, drafted 2026-07-08 and PROPOSED, not ruled — `audits/25_GROUNDING_ENGINE.md` G-12; the ruling is Jordan's A-1 and `ED-IN-0285`: "one engine, event-parameterized … auto = the kernel run headless, played
= the same kernel run interactively"; the text is in the quarantined
`auto_manual_resolution_duality_v1.md`, read for intent and loaded by nothing). Its one open fork, the
calibration tolerance between fidelities, needs no number under this shape: the two fidelities are equal
on matched inputs by construction, and the pin is the check. A "witnessed" battle is the automated call
with the after-action reading shown; it adds no mechanism.

The quarantined scenario-visualization audit (2026-07-29, lesser weight; its constants re-verified:
field 51, 11 subunits, 10,000 troops a unit) found that a single-subunit body of 25 cells has no
geometry to watch. A field the seam builds from person weights alone will be such a body. Whether the
order of battle carries subunits is MB's; the pin's three field scenarios must include one that does,
or the trace has nothing in it for a port to get wrong.

## 4. Halts and refusals

**Problem.** GO-10 retypes four `except` sites (by symbol today: `loop/resolve.py:267`, `:498`, `:1189`;
`loop/predicates.py:368`) and leaves "defect raises" as halts. *(W3-1, C3-N15.)* The `raise` sites are
counted by `grep -rE '^\s*raise ' engine/season` outside `tests/`, `harness/`, `data/` and `manifest/`;
re-run it rather than quoting a figure. Layer 1 reads the engine reference as
giving GDScript no release-build halt (`04:966-972`).

**Resolution** (step 3: §C.12 rejection 5, "the refusal must ride in the value"; step 5 for the halt).
The oracle keeps raising. Two additions to the contract:

- GO-10's §C.12 hunk states both shapes: a **refusal** is `{code, needs, law}` and becomes an Event; a
  **defect** is `{where, needs, law}` (the fields `ShapeGap` already carries, `engine/season/gaps.py`),
  is returned up to the driver, and ends the run in `game/`. Neither is a sentinel beside a last error.
- `oracle_pins.json` gains `halts`: the closed roster of `where` tags reachable in the loop (derived by
  the exporter from the `raise` sites, never typed by hand), and a handful of planted worlds each pinned
  to the tag it halts on. The port's parity job asserts it stops at the same tag.

## 5. GO-12's environment reads are 91, not two

**Problem.** `grep -rn "os.environ" modules --include=*.py` (tests excluded): `mass_battle/config.py` 66,
`hierarchy/units.py` 12, `orchestration.py` 11, `core/exchange.py` 2. Read at import (`MB_FRICTION=0`
flips `config.MB_FRICTION`). None of the 91 names appears in `engine/engine_params/sim_params.json`
(`tools/export_sim_params.py:56-58` skips a non-literal), and no other exporter reads `config.py`.

**Resolution** (step 4: `modules/combat/config.py` → `combat_engine_v1.json` behind
`tools/export_engine_params.py --check` is the precedent). *(W3-1, 7b-8, D-U1-11c.)* The 91 reads are
partitioned by the one-owner rule: those that are columns of a row a designer edits move to
`references/troops.yaml`, exported to `engine/engine_params/troops.json` by `tools/export_troops.py --check`
(e.g. `MB_STAMINA_DRAIN`, `MB_STAMINA_REST`, `MB_CAVALRY_SPEED_MULT`, `MB_ENVELOP_SPEED_MULT` per
`26_MASS_BATTLE_movement…`); the rest are literals at their present default, exported by a mass-battle
section of `tools/export_engine_params.py` to `engine/engine_params/mass_battle_v1.json` behind
`--check`; the loader refuses a name present in both; an A/B harness passes a variant `cfg` explicitly.
**The build is `04_MB_typed_outcome_and_one_path.md` §3's (B17, MB)**; this file adds none of it and, in
B41, only checks it (gate 1). The dead arm of a toggle that has shipped ON is deleted with its toggle
where the module's lane agrees (MB's call, not GO's).

Edit, `_part5.md:63` (GO-12 REMAINING UNBUILT) — old: "`os.environ`-read module flags
(`modules/mass_battle/config.py:113`, `hierarchy/units.py:33`) frozen into exported values". New: "every
`os.environ` read under `modules/` (91 at this reading: re-count by grep) replaced by a literal at its
default, partitioned between `references/troops.yaml` (`troops.json`) and `mass_battle_v1.json` by the
one-owner rule, each behind `--check` (done in B17 by `04_MB_typed_outcome_and_one_path.md` §3); no module
reads the process environment".

## The gate (execution artifacts)

1. `grep -rn "os.environ" modules --include=*.py` (tests excluded) prints nothing; the realm hash at
   seeds 0–2, two seasons, is equal before and after; `CASUALTY_SCALE=9 python -m … port_oracle` prints
   the same line as with the variable unset.
2. `python tools/export_oracle_pins.py --check` OK with a `module_scenes` block of the twelve named
   entries; each scene's `key` re-seeds `draw.seeded(key)` and reproduces its `outcome` (written as
   `tests/valoria/test_oracle_pins.py::test_each_module_scene_reproduces_from_its_key`, red before the
   block exists).
3. A planted defect world halts with the pinned `where` tag; a planted no-op write still yields its
   refusal Event (GO-10's own falsifier).
4. The early landings each print their `--check` OK on `main` before B10-18b merges.

## The falsifier

Editing one tunable's literal without a re-export reds the new `--check`. Changing a module's entry so
that the seam builds a different input reds that scene's pin while slices 1 and 2 stay green, which is
the case the season-shaped slices cannot see. A `raise` added on the loop path with a new `where` tag
reds `--check` until the roster is rebuilt.

## NERS reading (§0.06; E last)

- **N.** The module-scene pins carry a possibility nothing else carries: a port wrong about a duel or a
  battle is shown wrong. Holds vertically (oracle to port) and diagonally (a scene entered from the
  season and a scene run alone are one pin). The per-mover ledger row fails N: cut it and the commit
  carries the same fact.
- **R.** Completeness: the halt roster is the mechanism at its extreme; the environment reads are a
  second, unseeded input to a seeded oracle.
- **S.** *Zooms in and out across scales* and *pauses correctly* are what a scene pin with and without a
  decider tests. Two parameter-export conventions (combat exported, mass battle not) become one.
- **E.** The card gets shorter: no freeze list, one spurious edge gone. The contract/behaviour split is
  one distinction a porter must hold, and it replaces a forty-item list.

## Build order and lands-it (W3-1, test 9)

Order inside B41, after `16_PESSIMIST_GO_surface_pins.md`: (1) §1 and §2's plan-text edits (`_part3.md`,
`_part5.md`, the B10-20 build file), hash-EQUAL; (2) write gate 2's and gate 3's tests red; (3) §3's
`module_scenes` block and §4's `halts` block in `tools/export_oracle_pins.py` (GO-08); (4) gates 1–4. Hash
movers: none (the pins re-read the run; B06 and B05 moved the hash earlier, each declared there). Control:
gate 1's `CASUALTY_SCALE=9` line equals the unset line. Lands it: the GO lane's B41 session (MB reviews the
field scenes, PC the duels); `sonnet` for the exporter, `opus` for the halt roster's derivation.

## Cost class

§1, §2: edit. §3: small build per module (the decider is MB's, B20). §4: small build. §5: a check here;
the build is MB's in B17.
