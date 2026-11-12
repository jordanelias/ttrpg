# GO — the port gate: what it freezes, in what order, and what it must cover

## Status: PROPOSED

Carries audit findings F-GO-01, F-GO-04, F-GO-05, F-GO-06 and the mass-battle part of F-GO-08
(`audits/11_GO_audit.md`). Lane: GO, IN. It edits the one active plan (`workplans/valoria_master_workplan_v11_part3.md`
§1, the B10-20 card; `_part5.md`'s GO entries; the build file
`proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-20.md`). It asserts no engine
version and edits nothing in `valoria-game`.

## What it changes in `engine/season/` at runtime

Nothing in the loop. In `modules/mass_battle/`, 91 tunables stop being read from the process
environment (their defaults become the values; hash EQUAL in an unset environment, which is every pinned
run). The rest is exporters, pins and plan text.

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
  worlds, traces, hashes, the draw and float logs, the module-scene pins (§3). They are whatever
  `--build` writes at the commit the port syncs to. **A mover re-runs `--build` in its own commit and
  says so in that commit; no ledger row.** The port records the oracle SHA it synced to, on its side.

Edits. `_part3.md` B10-20 **Hash** line and `_part5.md:83` (GO-15 SOURCE) — old: "A later mover after
the freeze re-builds the pins and the draw log in the same commit and writes an `ED-GO-` row naming old
and new values and the slice it moves." New: "A later mover re-builds the pins and the logs in the same
commit and states the move in that commit (a golden re-record, said plainly). A change to the *contract*
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
| GO-16 → the draw owner | "NEEDS: GO-12" | NEEDS the one draw owner (which absorbs GO-12's generator item) | two of three seeds build generators outside the factory the recorder is planned on |
| GO-08 → the float contract | not named | NEEDS it | "slice 3's float pin" names nothing; the `fmath` stream is that pin |
| GO-08 → module-scene pins (§3) | not named | NEEDS them | slice 2 reaches the combat engine 0 / 2 / 4 times and a fought field 0 / 0 / 1 times at seeds 0 / 1 / 2 |
| GO-01, GO-11, GO-05 → B10-18b merged | held by batch membership | **early landings**, as GO-13, GO-14 and GO-07 were | each is hash-EQUAL and reads no behaviour B10-11 to B10-18b change; GO-01's one need (ED-GO-0002 on `main`) is met |
| GO-09 → B10-18b merged | held by batch membership | early landing | its `--check` then catches a registry edited without a re-export *during* the batches that edit registries, which is when it can fail |

Decided order: **early** GO-01 · GO-11 · GO-05 · GO-09; **then, in one re-pin window** the draw owner →
the float contract → GO-12 (the rest of it, §5) → GO-10 (§4) → GO-16 → module-scene pins (§3) → GO-08 →
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
line; an envelopment; a rout cascade), three contested speech acts, three graded findings. The scenario
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
| a point to intervene | — | a decider on `mass_battle.resolve_field`, as `combat.fight` has (`seam/wrappers/combat.py:395`); MB's to design (the typed `Orders` record MB-08 names), GO's to host |

Auto-resolve and the played battle are then one call with and without the decider, which is what keeps
them consistent, and the module-scene pin covers both: the automated outcome, and a played run whose
decider returns the default orders reproducing it.

## 4. Halts and refusals

**Problem.** GO-10 retypes four `except` sites (by symbol today: `loop/resolve.py:267`, `:498`, `:1189`;
`loop/predicates.py:368`) and leaves "defect raises" as halts. `engine/season` holds 172 `raise`
statements outside `data/`, `manifest/`, `harness/` and `tests/`; Layer 1 reads the engine reference as
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
`tools/export_engine_params.py --check` is the precedent). Each of the 91 becomes a literal assignment
at its present default; an A/B harness passes the value as an argument or a fixture instead of setting
the environment; `tools/export_engine_params.py` gains a mass-battle section writing
`engine/engine_params/mass_battle_v1.json` with the same `--check`. The dead arm of a toggle that has
shipped ON is deleted with its toggle where the module's lane agrees (MB's call, not GO's).

Edit, `_part5.md:63` (GO-12 REMAINING UNBUILT) — old: "`os.environ`-read module flags
(`modules/mass_battle/config.py:113`, `hierarchy/units.py:33`) frozen into exported values". New: "every
`os.environ` read under `modules/` (91 at this reading: re-count by grep) replaced by a literal at its
default and exported by `tools/export_engine_params.py` to `engine/engine_params/mass_battle_v1.json`
behind `--check`; no module reads the process environment".

## The gate (execution artifacts)

1. `grep -rn "os.environ" modules --include=*.py` (tests excluded) prints nothing; the realm hash at
   seeds 0–2, two seasons, is equal before and after; `CASUALTY_SCALE=9 python -m … port_oracle` prints
   the same line as with the variable unset.
2. `python tools/export_oracle_pins.py --check` OK with a `module_scenes` block of at least twelve
   entries; a counting shim shows each scene's draws came from one `Draw` key.
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

## Cost class

§1, §2: edit. §3: small build per module, plus MB's design-first decider and trace. §4: small build.
§5: small build (mechanical; 91 lines and one exporter section).
