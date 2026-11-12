# GO — pointer and stale-text resolutions at the owners a porter reads first

## Status: PROPOSED

Carries audit findings F-GO-10 and F-GO-11 (`audits/11_GO_audit.md`). Lane: GO, IN. Every item is an
edit or a deletion at the single owner of the sentence; none adds a file, a guard or a ledger corpus.

## What it changes in `engine/season/` at runtime

Nothing. One test file loses a spent control and its dated notes; its vectors and current pins stay.

## Resolutions, each decided by the five-step ladder

| # | owner | old | new | ladder |
|---|---|---|---|---|
| 1 | `CURRENT.md:39` (the GO row) | head: `godot/godot_conversion_strategy_v1.md` — PROPOSED | head: `architecture/meta/04_CODE_ARCHITECTURE.md` §C.12 (RATIFIED, the Godot mapping); the port gate: the B10-20 card in `workplans/valoria_master_workplan_v11_part3.md`; `godot/godot_conversion_strategy_v1.md` — PROPOSED, intent only. Pointers unchanged: ED-GO-0001, ED-GO-0002, `HANDOFF_GO.md` | 3: `CLAUDE.md` §6 already says the season loop's ratified Godot mapping is `04` §C.12 |
| 2 | `godot/README.md:5` | "It **is** the eventual `res://` project root." | "The Godot project is `jordanelias/valoria-game`, a separate repository; this directory holds design reference for the port and no project files." | 1: `CLAUDE.md`'s preamble (the implementation repo is a separate clone) |
| 3 | `godot/README.md:13-14` | "`godot_architecture_specification.md` — the Godot architecture specification (formerly under `designs/videogame/`)." | "`godot_architecture_specification.md` — STALE REFERENCE by its own Status line (pre-d+σ). Do not implement from it." | 3: the document's own line 5 |
| 4 | `architecture/meta/04_CODE_ARCHITECTURE.md:927` | "the RNG (unbuilt)" | "the RNG" | Layer 1 text. 1: superseded by the code (`state/ids.py::draw_factory`; 45,000 draws in a two-season run). Lands with GO-10's §C.12 hunk, listed under "Layer 0/1 hunks"; a (RULED) mark at the anchor stops it |
| 5 | `04:955-959` (rejection 4) | "When R-09's producer is built … This is the one rejection that is **not yet load-bearing**, because no roll exists yet; it is stated now so the roll is not built the idiomatic way first and retrofitted after." | "R-09's producer is built: every draw is keyed by `H(seed, tick, subject, purpose)` (`engine/season/state/ids.py`), constructed by the driver's factory and passed down. The port's generator is threaded the same way and, in a parity run, replays the oracle's recorded uniforms." | as item 4 |
| 6 | `04:985-1002` (rejection 5's measurement paragraph) | the counts in `shape.py` and `seam.py` (167 / 128 / 18 / 4) | one sentence: "Measured with `grep -rE '^\s*raise ' engine/season` outside `tests/`, `harness/`, `data/` and `manifest/`; re-run it rather than quoting a figure. One site returns a typed value (`seam/contest.py::ContestError`)." | 2: the files it counts do not exist; a pointer to a command replaces a stale figure (`CLAUDE.md` §1's pointer rule, by analogy) |
| 7 | `references/module_contracts.yaml` `golden_path:` note (`:1036-1037`) | "BaseEngine / EngineModule / KeyBus / Resolver / GameState are referenced by the skeleton but class_name def = NONE anywhere. Gate-0; the skeleton is non-compilable. …" | delete the note | 2: its subject, `godot/skeleton/`, was deleted by GO-14. This is GO-11's own edit; listed so GO-11's re-base names it |
| 8 | `references/module_contracts.yaml`, 20 `parity:` values | `key-log`, `key-log + typed-export round-trip` | `state-hash` (a module whose effect is read in `World.content_hash`) or `seam-io` (a module pinned at its entry by a module-scene pin) | 1 and 3: ED-IN-0232; GO-11 as planned. The second value's meaning is supplied by `11_GO_port_gate_order_and_coverage.md` §3 |
| 9 | `workplans/valoria_master_workplan_v11_part5.md:196` (GO-01) | "CONTROL: the six existing constants are unchanged." | "CONTROL: the existing constants (count them: `len(json.load(...)['constants'])`) are unchanged." | 3: `engine/engine_params/game_constants.json` holds five; a pointer to a command, not a count |
| 10 | `references/descriptor_registry.yaml:24`, `:31-32` | "Roster IN FLUX …"; "\"IN FLUX\" STAYS and Godot fields stay unbound (CLAUDE.md §5) until Jordan confirms the ten." | "The ten are ratified (ED-IN-0328); keys are stable. A Godot field may bind to an attribute **key** (`attr.*`), never to a display name or alias." | 3: ED-IN-0328 reads `status: ratified`; `descriptors.json` reads `pending_tenth: None`. **Held back for Jordan** (audit §11): the row's own description says "I think", and `CLAUDE.md` §5 forbids binding to a key the registry marks IN FLUX |
| 11 | `engine/season/tests/test_go07_canonical_digest.py` | `_old_entity_digest`, `_old_content_hash` (`:282-311`), every `old` pin, the `assert got["old"] != got["new"]` line, and the RE-RECORDED / RE-PINNED notes (72) | deleted. Kept: the vector half (`:49-277`) unchanged; one `new` hash, act count, census digest and counts per seed; the build-world pin | 2: the control compared two digests across one commit (`b9beec9d` → GO-07); both are now re-read from the same run at each mover, so their agreement observes nothing. The notes are dated narrative whose home is the commits that made them |
| 12 | `godot/godot_conversion_strategy_v1.md:167-169` (V.2 items 2–3) | no marker | a `[LAYER 1 ANSWERS — marker only …]` line, in the document's own convention: "Recorded-draw replay is the port gate's mechanism (B10-20). 'Statistical parity (second tier)' has no instrument in either repository; the oracle's owned samplers, exercised by replay, take its place." | 4: the document's own marker precedent (`:121`, `:166`, `:220`, `:222`). The document stays PROPOSED |
| 13 | "parity" used for two things | the auto/manual doctrine's "parity harness" (played against auto-resolved, ED-SC-0013) and the port gate's "parity" (oracle against port) | in new text, **fidelity parity** for the first and **port parity** for the second; no retrofit of existing text | `CLAUDE.md` §4, word choice: one word with two meanings a reader cannot tell apart |

## Not edited, and why

The five stale `godot/` documents keep their banners and stay. `CLAUDE.md` §0.05 does not license
deleting design documents, each is bannered at its head, and `CLAUDE.md` §6 already says to implement
from none of them. ED-1054 (open since 2026-06-30) is answered by that state: the banners are the
resolution it asked for, and it closes at ladder step 1 with a row citing them.

## The gate (execution artifacts)

- `python tools/currency_consistency_check.py` and `python tools/freshness_gate.py` clean after items 1–3.
- `python tools/export_composition.py --check` OK and `grep -c "key-log" references/module_contracts.yaml`
  prints 0 after items 7–8 (GO-11's exit).
- `python -m pytest engine/season/tests/test_go07_canonical_digest.py -q` green after item 11, and the
  mutation its head records (drop a dataclass's last field in `_object_head`) still reddens it.

## The falsifier

For item 11: if deleting the `old` digest removed the test's ability to see a world move, a planted
one-field change in a built realm would pass; it does not, because the `new` hash, the act count and the
counts are still pinned.

## NERS reading (§0.06; E last)

Process text, so only N and E apply. **N:** each sentence removed or replaced is one a porter would act
on wrongly; none carries a behaviour. **E:** the pointer row names the ratified owner first; the test
file falls from 699 lines to about 330.

## Cost class

Edit, throughout. Items 4–6 are Layer 1 hunks and ride GO-10's PR; item 10 is held back.
