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

SECTION-2-ONWARD
