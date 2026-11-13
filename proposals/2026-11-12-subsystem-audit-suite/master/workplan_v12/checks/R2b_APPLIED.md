# R2b_APPLIED — repair lane R2b (Opus): the open findings of CHK_K3 and CHK_K4 (parts 12 to 20)

## Status: WORK RECORD (one round; a record of edits to `master/workplan_v12/` parts 12 to 20; resolves nothing at runtime, CLAUDE.md §0.05; deleted with the suite when v12 is adopted)

Appended finding by finding as each is applied (a restart resumes from the last row written). Ladder steps are CLAUDE.md §0's: 1 superseded, 2 irrelevant, 3 design document, 4 precedent, 5 architecture.

## Already resolved by R1 (re-checked against the current text)

- K3 F2 (`corpus_run` past two seasons): R1 repair 2 — B10.74 Reading 1 and B10.99 step 1 (`workplan_v12_part13_cont.md`) carry `--seasons 2` and the bracketed D-17 note; B21's BATCH GATE and B21.10 likewise (R1's list). Re-checked in part 13_cont: present.
- K3 F3 (the hash reading names no command): R1 repair 3 — B10's block carries the `HASH READING:` line (`workplan_v12_part12.md`, under the last `GATE:` line); item gates cite it. A mover's "moved" is falsifiable against the seed-0 command (an EQUAL reading falsifies it). No further edit.
- K4 F1 (`register --check` → exit 0): R1 repair 1 — the 15 lines read "violation count … does not rise" (re-checked at B10.58, B10.99, B21 lines in parts 12–15).
- K4 F16: fixed by K4 itself.

## Applied

- K3 F4 (B10.55, `PersonInterior`): edit — DEPENDS ON now names V12 `B03.58` (`workplan_v12_part5.md`: NEW class `PersonInterior`, `interior_of`) and keeps the copied signature `room_as_held(p: PersonInterior, …)`, as B10.27/.28; `[ASSUMPTION]` on `regard`'s own type. `workplan_v12_part13.md` B10.55.
- K3 F14 (B10.58 WHERE): edit — `references/npc_registry.yaml` added (the `manner:` schema note). `workplan_v12_part13.md` B10.58.
- K3 F6 (B10.66): edit, ladder 4 (precedent from the tree). Stem renamed `skill_shown` (A-98), test renamed `test_a_shown_skill_is_deposited_to_the_actor_alone` (also in B10.64's TESTS line). Not BLOCKED: `observation_terms` is `Seen`'s struct, and an `observed` predicate is a stem constant beside its emitter (`loop/effects_combat.py::BROKE_STEM`/`broke_observed`, `world_q.BODY_STEM`); WHERE now `loop/resolve.py::_act_events` plus the stem beside its emitter; "to him alone" is `observation_deposit_mode: actor` (H-122, shipped, `loop/witness.py` `pid == actor`). Old STOPS IF replaced by one on that fixture; control test added `[ASSUMPTION — E-3]`. `workplan_v12_part13.md` B10.66.
- K3 F5 (B10.24 `Scene.forgone`): edit — the Layer-1 departure sentence copied from B10.05 for `forgone` (reader: the fold's `scruple.overridden`); WHERE names the docstring. `workplan_v12_part12_cont.md` B10.24.
- K3 F10 (B10.56 DEPENDS ON B08): edit — B08 removed from DEPENDS ON, kept as a "Not a dependency" sentence citing UNDECIDED 11. B21.76/.77/.70: recorded, no edit (K3: "none needed"). `workplan_v12_part13.md` B10.56.
- K3 F11 (B10.65 `boot/realm.py` EXISTS-IN-TREE): edit — now `V12 Batch B03c`. `workplan_v12_part13.md` B10.65.
- K3 F13 (B10.71 test green before the edit): edit — step 1 says `_stages` already refuses stage keys (kept as a pin, green before); the real edit is admitting `opens` in `_goal_stages` (`{id, for, stages}` today); new red test `test_an_opens_value_outside_the_two_is_refused` `[ASSUMPTION — E-3]`. `workplan_v12_part13_cont.md` B10.71.
- K3 F9 (B10.75, B10.76 owners): edit, ladder 3 (`V12_STRUCTURE_part3.md` §8.2, "nine blocked entries … outside the tree's reach"): an "Owner who can act" line each — no batch of v12; blocked by a design no proposal writes (B10.76: B11's source leaves the false-deed deposit out as design-first, `workplan_v12_part16_cont.md:98`). `workplan_v12_part13_cont.md`.
- K3 F15 (B10.78 POINTER body 2 lines): edit — target files/symbols and a close reading (`grade:` lines of H-185/H-191) added (E-5). Heading `· HASH` segment on non-BUILD rows: no edit, ladder 4 (K4 F12's same finding: H2 §1.3 parses them; the table carries `—`).
- K3 F12 (B10 head EXPECTED RED): edit — the "none in this half" line rewritten in R1 repair 4's form (first mover B10.32; `_realm_goldens.py`, `test_go07_canonical_digest.py`, the NPC-088 headless hash). B21's line was added by R1. `workplan_v12_part12.md` B10 head.
- K3 F8 (B10 UNDECIDED 3, A-24 against D-22): edit, ladder 4 — one sentence: D-22 governs the order; A-24 lands at `B98.12` (BUILD flip to `drawn`, `workplan_v12_part44.md`), not a BLOCKED row. `workplan_v12_part12.md` UNDECIDED 3.
- K3 F17 (B21 EST stale "19 h"): edit — EST reads part 2 §1.3's 25.3 h, the two halves' formula figures kept in the bracket. `workplan_v12_part14.md`.
- K3 F7 (B21.81–.83 compressed by reference): items rewritten whole (each under 6 KB). Clause names copied from B09.18's table (`workplan_v12_part11_cont.md`) for `establish` and `oblige`; `revoke` is not in B09.18's table nor B09.19's four, so its four names are short forms of the four `_refuse` phrases on the tree (`loop/predicates.py`, `_req_revoke`) `[ASSUMPTION]`; the keyed `emits_on_refusal:` form cited from the `arrest` row (`verb_table.yaml`); B21.83's "if `oblige` is a typed row" resolved from the tree (`loop/predicates.py:466`, a predicate row). E-3 marks on the test arms. B21.80's GATE hash reading made falsifiable (`HASH READING`, "moved …, else equal"). `workplan_v12_part15_cont.md`.
- Size note: three items edited here sit at 6.0–6.2 KB after the edits (B10.24, B10.58, B10.71); additions were cut to the minimum; each was already at or near 6 KB before.

## For Jordan
