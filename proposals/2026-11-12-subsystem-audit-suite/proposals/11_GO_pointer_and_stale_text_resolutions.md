# GO — pointer and stale-text resolutions at the owners a porter reads first

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `R1_READ.md` §1.4 row 160 (AMBIGUOUS; items 4–6 are owed Layer 1 text, applied only by Jordan's merge, and **item 4 and item 5 are merged with A-30's row text into one hunk, not two**: the RNG row and rejection 4 now say the keyed draw with an owned mix and no recorded uniforms), §2 row A-30 (item 12's marker no longer names recorded-draw replay; item 4's evidence names `draw.seeded`, the one constructor after B06); `U3_DEPENDENCY_ORDER.md` split row 1 (item 5 lands in B06 with the draw owner; the rest in B03) and B03; `U3_CONFLICT_LEDGER.md` C3-N15 (item 6 is the command that replaces every quoted `raise` count; `11_GO_port_gate_order_and_coverage.md` §4 points here). Checked at the tree: `seam/contest.py::ContestError` is returned, not raised (`:25-35`, `:238`), so item 6's sentence stands. Test 9: gates kept, lands-it and tier added.

**Depends on:** `09_WR_B_pointer_text_for_the_orchestrator.md` (B03, before this file in U3's chain); nothing for items 4 and 5, which are applied (A-97, `L1-A30`).
Reconciled: 2026-11-12, A-97 (`unified/work/L1_APPLIED.md` §`L1-A30`, `unified/work/L1_PROPAGATION.md`): items 4 and 5 (`04:927`, rejection 4) are APPLIED by Jordan's amendment, in the U3 draft's wording (`unified/U3_LAYER1_AMENDMENTS.md` node `L1-A30`), not in this file's wording; both rows say so and carry no batch. Item 6 (rejection 5's measurement paragraph, `04:985-1002`, still quoting 167 / 128 / 18 / 4) was not an A-n node and is NOT applied; it stays owed text for Jordan's merge.

**Lands in batch:** B03 (`B03-hygiene`) for items 1–3, 6–13; items 4–5 are applied and land in no batch (B06 carries the keyed draw's code, `11_GO_one_draw_owner.md`).

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
| 4 | `architecture/meta/04_CODE_ARCHITECTURE.md:927` | *(was "the RNG (unbuilt)" \| "a seeded `RandomNumberGenerator` **threaded like `World`**")* | **APPLIED 2026-11-12 (A-97, node `L1-A30`), in the U3 draft's wording and not this row's:** §C.12 reads "the draw" \| "a function of its key, `H(seed, tick, subject, purpose)`, the index `n` part of the key; no generator object, nothing global" (`04:927`). This row's own wording ("**threaded like `World`**", "implemented in GDScript") is not carried: Layer 1 now says *threaded* does not stand (`04:953`). Not an edit of any batch | superseded by the applied Layer 1 text (`unified/work/L1_APPLIED.md` §`L1-A30`) and A-30; B06 carries the code (`engine/dice_engine/draw.py::seeded`, the one constructor) and no Layer 1 hunk |
| 5 | `04:955-959` (rejection 4) | *(was "When R-09's producer is built … This is the one rejection that is **not yet load-bearing**, because no roll exists yet …")* | **APPLIED 2026-11-12 (A-97, node `L1-A30`), in the U3 draft's wording:** rejection 4 (`04:953`, `:959`) now says the draw is a function of its key, the driver constructs no generator and passes none down, and that the rejection is load-bearing (the oracle rolls today), without a census figure. This row's sentence about the port ("implements the same mix and is threaded the same way") is not carried. Not an edit of any batch | as item 4 |
| 6 | `04:985-1002` (rejection 5's measurement paragraph) | the counts in `shape.py` and `seam.py` (167 / 128 / 18 / 4) | one sentence: "Measured with `grep -rE '^\s*raise ' engine/season` outside `tests/`, `harness/`, `data/` and `manifest/`; re-run it rather than quoting a figure. One site returns a typed value (`seam/contest.py::ContestError`)." | 2: the files it counts do not exist; a pointer to a command replaces a stale figure (`CLAUDE.md` §1's pointer rule, by analogy) |
| 7 | `references/module_contracts.yaml` `golden_path:` note (`:1036-1037`) | "BaseEngine / EngineModule / KeyBus / Resolver / GameState are referenced by the skeleton but class_name def = NONE anywhere. Gate-0; the skeleton is non-compilable. …" | delete the note | 2: its subject, `godot/skeleton/`, was deleted by GO-14. This is GO-11's own edit; listed so GO-11's re-base names it |
| 8 | `references/module_contracts.yaml`, 20 `parity:` values | `key-log`, `key-log + typed-export round-trip` | `state-hash` (a module whose effect is read in `World.content_hash`) or `seam-io` (a module pinned at its entry by a module-scene pin) | 1 and 3: ED-IN-0232; GO-11 as planned. The second value's meaning is supplied by `11_GO_port_gate_order_and_coverage.md` §3 |
| 9 | `workplans/valoria_master_workplan_v11_part5.md:196` (GO-01) | "CONTROL: the six existing constants are unchanged." | "CONTROL: the existing constants (count them: `len(json.load(...)['constants'])`) are unchanged." | 3: `engine/engine_params/game_constants.json` holds five; a pointer to a command, not a count |
| 10 | `references/descriptor_registry.yaml:24`, `:31-32` | "Roster IN FLUX …"; "\"IN FLUX\" STAYS and Godot fields stay unbound (CLAUDE.md §5) until Jordan confirms the ten." | **no edit.** The sentence records Jordan's own hedge (ED-IN-0328: "I think") and stays his. The port's rule makes it moot: it binds no resource field, enum or constant to an attribute or skill name and loads the roster from `descriptors.json` as data (audit §14), so nothing waits on the confirmation | 5: the data-driven binding is what the capability-authoring charge needs anyway, and it satisfies `CLAUDE.md` §5 whether or not the roster is in flux |
| 11 | `engine/season/tests/test_go07_canonical_digest.py` | `_old_entity_digest`, `_old_content_hash` (`:282-311`), every `old` pin, the `assert got["old"] != got["new"]` line, and the RE-RECORDED / RE-PINNED notes (72) | deleted. Kept: the vector half (`:49-277`) unchanged; one `new` hash, act count, census digest and counts per seed; the build-world pin | 2: the control compared two digests across one commit (`b9beec9d` → GO-07); both are now re-read from the same run at each mover, so their agreement observes nothing. The notes are dated narrative whose home is the commits that made them |
| 12 | `godot/godot_conversion_strategy_v1.md:167-169` (V.2 items 2–3) | no marker | a `[LAYER 1 ANSWERS — marker only …]` line, in the document's own convention: *(W3-1, A-30)* "The port implements the oracle's keyed draw (B10-20); parity is exact, by `(key, n) → u` vectors and `content_hash` at any seed. 'Statistical parity (second tier)' has no instrument in either repository and needs none." | 4: the document's own marker precedent (`:121`, `:166`, `:220`, `:222`). The document stays PROPOSED |
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

## Lands it (W3-1, test 9)

Order: items 1–3, then 7–8 (with GO-11), 9, 11, 12, 13 in one `[cleanup]` commit in B03; item 6's Layer 1
sentence in the same B03 PR, held for Jordan's merge; items 4–5 are applied (A-97, `L1-A30`). Gates as above; item 11's gate is its named test file, red before the edit only if the
spent control is reintroduced (control: the mutation its head records). Hash movers: none. Lands it: the
IN-lane B03 hygiene session (GO reviews); `haiku` for items 1–3 and 7–13 (transcription), `sonnet` for
the Layer 1 hunks' wording.

## Cost class

Edit, throughout. Item 6 is a Layer 1 hunk, **owed text for Jordan's merge**, independently revertible (items 4
and 5, formerly with it, are applied); item 10 is a decision with no edit.
