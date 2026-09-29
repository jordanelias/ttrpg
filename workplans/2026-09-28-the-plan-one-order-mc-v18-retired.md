# THE PLAN — every live item, one order, across every lane, with `mc_v18` and its spine retired in full

## Status: **ADOPTED 2026-09-28 (`ED-IN-0281`) AS THE SINGLE PLAN, ON JORDAN'S INSTRUCTION** — *"Resume on the master plan (task #3). Ensure that we comprehensively supersede all calls for mc_v18."* It supersedes `workplans/2026-09-18-governance-settlement-behaviour-plan.md` (+ `_part2`) as the ORDER, by the precedent that document set when it was itself amended into the single plan (its `:12`, `ED-IN-0253`: *"I need one single clearly defined plan"*). **What is adopted on the instruction, and what a merge carrying it ratifies (ED-1094):** §3's four-phase ORDER and §2's supersession verdict — the same scope the 2026-09-18 plan's own merge ratified (its §3 order and its §1 verdict, and nothing else). ⚠ **HELD BACK, LOUDLY (§7): the thirteen Jordan items of §5.1 are OPEN. Each is his to answer individually, and nothing about this document landing answers any of them.** §5.2's demotions ratify only as *which ladder step answers each question, and which candidate gets attacked* — never as the answer, which is decided at its position with the code in front of it (the 2026-09-25 amendment's own discipline, `ED-IN-0270`). **No existing position number changes meaning.**
## Owner: infrastructure / cross-cutting (IN lane)
## Supersedes: `workplans/2026-09-18-governance-settlement-behaviour-plan.md` + `_part2` **as the ORDER, in full.** That file's `_part2` stays the **CONTENT OWNER** for every position it details; its §1, §2, §3.4, §3.9, §5 and §7 stay as historical record, cited here by reference; its **§3.0 per-step cadence is not superseded** (§0 below). Also absorbed **as CONTENT, not as parallel orders**: `proposals/2026-09-27-mc-v18-retirement-plan/PROPOSAL.md` §3 (M5, M6, ADJACENT) and its Step B; `proposals/2026-09-26-decision-layer-execution-plan/PROPOSAL.md` §3 (H3–H13); `proposals/2026-09-25-squad-engagement-synthesis.md` (Part A remainder, the Sequenced rows, Part D); `proposals/2026-09-05-proceedings-subsystem/21_RECONCILIATION.md` PHASE 1–4. Unit content owners are unchanged: `workplans/2026-09-13-work-order.md`, `2026-09-09-r-execution-plan.md` (U5–U10), `2026-09-09-layer1-conformance-plan.md`, `proposals/2026-09-05-proceedings-subsystem/`. The per-item mapping is `_part2` §3.
## Produced by: a Fable → Opus relay (`CLAUDE.md` §10), the same division as `workplans/2026-09-18-governance-settlement-behaviour-plan.md:29-34` and `proposals/2026-09-28-repository-armature/ARMATURE.md:5`. A read-only **Fable 5.1** node resolved every contradiction, built the phased sequence, dispositioned every file, role and importer on the `mc_v18` spine, ran the Layer-1 nodes through the five-step test and produced the Jordan roster, reading every file it cites; this write-up is **Opus's**, from that pass. Working tree **HEAD `6f6ef84`** (the armature commit) over `ecacb57`'s code, 2026-09-28; no code changed between them.
## Grade under CLAUDE.md §0.2: `paper` throughout — a plan, not an execution artifact. Where a row says DONE it is repeating the cited evidence; the execution artifact is the thing cited, never this file.

**Why this exists, in Jordan's words.** Three requests across one session, in order: pull in the
recent workplans (done — the armature's §1); a structural armature (done —
`proposals/2026-09-28-repository-armature/ARMATURE.md`); and a new master plan, first held (*"Our task
is just #1 and #2 right now with #3 on hold"*, armature `:37-38`) and then resumed: *"Resume on the
master plan (task #3). Ensure that we comprehensively supersede all calls for mc_v18."* The second
sentence is why the retirement of `engine/mc_v18.py` is not a side-plan here. It is Phase 4, and every
file, composition role and importer on its spine has a disposition (`_part2` §1).

**How it was produced, and what the author re-checked.** Fable's claims are carried as verified by
that pass; its `(ARMATURE)` claims are carried from the armature. The author re-ran these against the
tree rather than trusting them, and all held:

- the `ast` importer scan: **12 production files** import a spine module (4 of them the spine
  itself), and **17 test/tool files** do;
- `references/module_contracts.yaml` loaded with PyYAML: **27** `composition_roles:` keys;
- `engine/season/verb_table.yaml`: **39** verbs, **3** declaring `contests:` — `kill / wound` (the
  body), `march` (a field), `tell` (a standing);
- `architecture/meta/04_CODE_ARCHITECTURE.md:311-314`: `upkeep` is in the ratified `Seat :=`;
- r2 `05_LEDGER_AND_BUILD.md:1659`: *"Deleting `Office.upkeep` removes the carrier, not the gap"*;
- `engine/season/data/verbs.py:685-692`: `_load_alignment` keys its column check on `set(VERB_TABLE)`;
- `tools/m1_acceptance.py:129-164`: rows 1–2 probe `engine/season/`, not `mc_v18`.

**One Fable claim is corrected, and the correction does not move its conclusion.**
`tests/valoria/test_forked_status.py:118` `UNRESOLVABLE_CEILING = 78` is a **ceiling** (`:120` asserts
`<=`), not an equality. Fable's point stands: a new `FORK:` row that resolves does not trip it.

---

## 0. WHAT THIS DOCUMENT IS, AND THE TWO THINGS IT IS NOT

It is an **order**, with an instruction per position and the Layer-0/1/2 clause each position must
satisfy. For a position the 2026-09-18 plan already carried, the instruction and the clause stay in
that plan's `_part2` §8, which remains the content owner. For a position this document adds, the
instruction is written here and its disposition detail is in this file's `_part2`. It executes
nothing. Under `CLAUDE.md` §0.05 it is **reference**: delete it and the game behaves identically, which
is the correct standing for a plan.

**It is NOT the queue closure.** The closures are position 1, exactly as before. Landing a batch of
status flips inside a planning commit is what `CLAUDE.md` §2 forbids — *"Never bundle a hard design
call into a routine PR"* — and each closure asserts a question is dead. Two ledger rows land with this
document, and neither is a closure. One is the adoption record (`ED-IN-0281`). The other is an
**escalation** under `ED-IN-0261`: it adds a `needs_jordan: true` flag the ledger was missing (§3.1
item 1). The record edits in §8.1 are corrections of stale facts, not design calls.

**It is NOT the retirement.** Every deletion named below is a future position's commit. This
document deletes no game code, renames no verb row and touches neither `engine/` nor `systems/`.

**Numbering.** No existing position number changes meaning. New work takes one of three forms:

- **lettered sub-positions** on the position it belongs to — `2-i`/`2-ii`, `12e`, `15d`, `17b`,
  `19d`, `20-i`…`20-iv`, `22a`, `22b`, `24g`, `24h`;
- **new numbers ≥ 28**, which change no existing meaning — `28-0`, `28-i`, `28-ii`, `28-iii` (the
  `mc_v18` retirement) and `29a`–`29f` (Step B, per tree);
- **three named Phase-1 steps with no number** — `FIGHT-RENAME`, `OPENERS-DERIVE` and
  `GATE-REMOVE-PERSON`. There is no prior position to letter them onto.

**None of these handles allocates a ledger id.** An id is allocated when the position is built.

**Three columns decide how you read a row**, as before. `STATE` is execution-bound per `CLAUDE.md`
§0.2. `GATE` names what the row waits on — a position, Jordan, or nothing. **A row whose `GATE` is `—`
is buildable today.**

| `STATE` | meaning |
|---|---|
| **DONE** | it runs, and the evidence is named in §2.2 |
| **DONE·INERT** | the code landed and does not yet affect the game. **§0.2 does not count this as done** |
| **OPEN** | buildable; `GATE` says what, if anything, it waits on |
| **BLOCKED** | a named position must land first |
| **JORDAN** | a decision or authored content is owed, named exactly in §5.1 |

**THE PER-STEP CADENCE IS NOT SUPERSEDED.** `workplans/2026-09-18-governance-settlement-behaviour-plan.md`
§3.0 — *"at end of each step i expect a /code-review and /simplify to run followed by fixes then a
forward sweep to see how it impacts stuff"* (RULED by Jordan, 2026-09-18) — binds **every** step in
this document unchanged. That section is the cadence's home. It is not restated here, because a
second copy of a ruled procedure would be a second owner (`CLAUDE.md` §8). In brief: one step is one
position and one commit. Each step runs five phases: BUILD, `/code-review`, `/simplify`, FORWARD SWEEP
(the five checks defined there), CLOSE. The full suite runs once, at CLOSE (`CLAUDE.md` §0.4).

---

## 1. CORRECTIONS TO THE BRIEF — measured before planning (read first)

Each row is a figure or claim on a live surface that the tree contradicts. The plan below is built
on the right-hand column. Several of these surfaces are corrected in this commit (§8.1); the rest are
named as owed (§8.2).

| the brief / a live surface says | the tree says | how measured |
|---|---|---|
| Step B has **"39 production importers outside tests/tools"** (retirement plan §1 `:31`; ARMATURE §2.5) | **12 production files import a spine module, and 4 of them ARE the spine**: `engine/mc_v18.py`, `engine/autoload/engine_clock.py` (→ `season_manager`), `engine/autoload/victory.py` (→ `game_state`), `engine/cross_scale/scene_dispatch.py` (→ `scene_slate` + three siblings). **The other 8 are all `systems/` modules, and all 8 import `engine.autoload.game_state`**: `systems/factions/sim/{faction_action:54, mass_seizure:51, parliamentary_action:40, parliamentary_transfer:81}.py`, `systems/overview/sim/{accounting:42, ci_track:128 (lazy), season:37-38}.py`, `systems/social_contest/sim/parliamentary_vote.py:42`. Plus **17 test/tool importers** (`_part2` §1.4). **The 39 is not reproducible by AST; do not carry it forward** | an `ast` walk over every tracked `.py` (`ImportFrom`/`Import` against the spine module names), run by Fable and re-run by the author. **`game_state.py` is the hub; every other spine file has at most two importers** |
| **"the 16 composition roles whose ONLY consumer is this spine"** (the brief; ARMATURE §2.5 "16 of 17") | **27 `composition_roles:` keys** (`references/module_contracts.yaml:71-207`, loaded with PyYAML). **20 are spine-only**: the brief's own list names 20 (4 + ten `snapshot_state.*` + 6). **3 are orphaned**: `rs_track_delta`, `territory_transfer_candidate` and `territory_transfer_proposal` — `needed_by: NOBODY since 2026-09-16`. **3 are FA-lane**: `parliamentary_vote`, `parliamentary_motion` and `parliamentary_vote_declaration`. **1 is consumed by the season**: `mass_battle.resolve_field`. The "16" is a miscount on both surfaces | `grep -rn "composition.require(" engine systems`. The consumers are `mc_v18.py:141,249`; `engine_clock.py:80`; `game_state.py:351,458-510`; `scene_dispatch.py:288-356`; `seam/wrappers/mass_battle.py:80`; `parliamentary_transfer.py:263-270` |
| the FA-lane distinction — *"`parliamentary_*` roles are consumed by retained `systems/factions/sim/parliamentary_*.py`, NOT by the spine"* | **It holds for the ROLES, but the consumers are themselves spine-dead.** The three roles' only `composition.require` caller is `systems/factions/sim/parliamentary_transfer.py:263-270`; `parliamentary_action.py:41` imports `parliamentary_vote` directly. `parliamentary_transfer.py` has **no production importer**: `faction_action.py:55-60` imports `crown_initiative, excommunication, absolution, council_solmund, parliamentary_action`, not `parliamentary_transfer`. Its `territory_transfer_*` roles have been NOBODY since ED-IN-0232, and `test_f7_smoke_oracle.py`'s header reads *"the only restoration path, parliamentary_transfer, is never called"*. `parliamentary_action.py` is reached only via `faction_action` ← `mc_v18`. **So when Step B retires `systems/factions/`, the three `parliamentary_*` roles and `systems/social_contest/sim/parliamentary_{vote,stay}.py` become orphans. `HANDOFF_SC.md`'s carve-out** (*"NOT in scope — live FA-lane callers … re-measure inbound references before executing"*) **expires by its own condition at that moment. `systems/factions/sim/` is NOT "retained": it is in the retire set** (`requirements.yaml:75-78`) | a grep of `from systems.` across `systems/factions/sim/*.py`. `parliamentary_stay` has zero importers outside a docstring (`parliamentary_transfer.py:35`) |
| ARMATURE §2.5's importer table gives `engine/tests/test_combat_bridge_seam.py` the stage "—" | it is **M6-class with NO successor needed** (`_part2` §1.4) | its own docstring, `:11-27` |
| `HANDOFF_IN.md` — *"step 11 (garrison Sites) not started; no review pass has run on M4"* | stale on both counts. `ecacb57` seeds garrisons (`harness/populated.py:396-414`), and its message records all four review passes (ARMATURE §1.2 item 5) | record edit, **made in this commit** (§8.1) |
| — | **Two spine modules are ALREADY orphaned, with zero importers anywhere.** `engine/autoload/npc_ai.py`: only its package docstring names it, and its header reads *"may contain contamination per Jordan diagnosis 2026-05-17 — audit pending"*. `engine/cross_scale/domain_echo.py`: *"the §5 Domain Echo COMPUTATION survives"* (`cross_scale/__init__.py`), and its transport was retired by ED-IN-0232 | the AST scan above. **Deletable today with a `FORK:` row and no gate** → position `28-0` ⚠ **CORRECTED at position `28-0`'s execution (§8.4): `npc_ai.py` is NOT zero-caller.** The `ast` scan is blind to `engine/tests/test_pipeline_reach.py`'s dynamic, string-keyed `_OI17_FULL_MODULE_ENTRYPOINTS` probe, which names `engine.autoload.npc_ai` by dotted path and calls it every run. Only `domain_echo.py` of this row's two was actually deletable today; `npc_ai.py` waits on `28-iii` with the other eleven OI-17 targets |
| — | `tests/valoria/test_engine_does_not_import_systems.py` also carries a snapshot-role guard (`:523 test_every_snapshot_state_role_resolves_to_something_restore_world_can_call`), and it uses `systems.factions.sim.treaty` / `faction_action` as planted fixtures (`:183-196`, `:462`) | both are Step-B ride-alongs: the guard dies at `28-iii`, and the fixtures are re-pointed at `29b` |

---

## 2. THE SUPERSESSION VERDICT

### 2.1 What is superseded, and what is not

**This document supersedes `workplans/2026-09-18-governance-settlement-behaviour-plan.md` (+ `_part2`)
in full, as the single ORDER.** The authority for the move is that document's own precedent. When
Jordan asked for *"one single clearly defined plan"*, it absorbed the spine, the governance build order
and the gather's amendment (`:12-22`, `ED-IN-0253`) under three rules. No existing position number
changed meaning. New work took lettered sub-positions. A mapping table recorded where everything
went. This document applies the same three rules to that plan: §0's numbering, §2.3's state index and
`_part2` §3's mapping table.

**What is superseded is the ORDER surface, and only that.** The 2026-09-18 plan's `_part2` is **not**
superseded. For every position it details — the `INSTRUCTION` / `WHERE` / `FALSIFIER` / `GATE` entries
and the Layer-0/1/2 clauses — it stays the **content owner**. A builder at position `15`, say, reads
this document for *when* and that file's `_part2` §8 for *what*. The 2026-09-18 plan's §1 (its own
supersession verdict), §2 (the closures, by test), §3.4 (the build-order item → position map), §3.9
(the file census and hard serial edges), §5 (the ruling batch, items 0–13 with the NOT-JORDAN table)
and §7 (its held-back list) are carried **by reference** as the historical record. Where this document
cites *"§5 item 11"* or *"`§3.9` edge 10"*, it means that file's section. Its §3.0 cadence stays
binding, as §0 says.

**Four other planning surfaces are absorbed as CONTENT.** None of them survives as a parallel order.

- **The `mc_v18` retirement plan** (`proposals/2026-09-27-mc-v18-retirement-plan/PROPOSAL.md`).
  - M0–M4 are DONE (§2.2).
  - M5 becomes `28-i`, M6 becomes `28-ii`, and M6's terminal clause (delete the spine) becomes `28-iii`.
  - Its ADJACENT rows land at `17b` (G2), `19d` (G3), `24d-ii` (S2), `24e` (S3), `24g` (S4) and `24h` (S5).
  - Its Step B becomes `29a`–`29f`, one per retire-set tree, each with its own scale gate.
  - Its header reads PROPOSED / HELD BACK IN FULL. The reason it gave was that its critical-path clause
    was `needs_jordan` (`ED-IN-0279`), and that row's last line is now `resolved` (2026-09-28), so the
    reason for the hold is spent. Its header is not edited here (§8.2).
- **The decision-layer execution plan** (`proposals/2026-09-26-decision-layer-execution-plan/PROPOSAL.md`).
  - H1 and H2 are DONE.
  - H3–H13 land at `12`, `12b`–`12d` (the cells commit) and `12e`. There is no H4 or H5; that plan's
    own `:324` says so.
  - That file self-deletes when its H-items have landed or been dropped (its `:10-12`).
- **The squad-engagement synthesis** (`proposals/2026-09-25-squad-engagement-synthesis.md`). Its build
  remainder, its Sequenced rows and Part D (ED-MB-0075) are MB-lane work in Phase 1. They are not
  positions, which follows the 2026-09-18 plan's *"parked, with reasons"* convention for a lane hand
  pass.
- **The proceedings reconciliation** (`21_RECONCILIATION.md` PHASE 1–4).
  - PHASE 1 step 1 goes to `16`. Steps 4(a)/(b) go to the new `15d`. Step 5 rides `11`/`21`.
  - PHASE 2 goes to `18`.
  - Steps 11–16 go to `22`.
  - PHASE 3 goes to the new `22a`.
  - PHASE 4 goes to the new `22b`, except step 22 (`Tenure.term`), which goes to `17b`.

### 2.2 DONE — left out of the sequence, noted so that it is not re-done

Re-read for this pass against the 2026-09-18 plan's §3.2; nothing has moved since.

| position | what landed | evidence |
|---|---|---|
| **3** G1a | the act store, `Receipt`, `state/gate`, `log.append` | `ED-IN-0258` |
| **4** G1b | `Event.subject` deleted | `ED-IN-0275` (hash `546fafa1…` → `52cfd9f0…`, declared) |
| **5** G2 | one `Token`, 36 gate sites | `ED-IN-0276` |
| **6** G3 | `NotYours`, `Act.via`, five bases (T-n unbuildable) | `ED-IN-0277`. **It absorbs `13d-ii` (purview), so `13d-ii` is DONE by 6** — even though that row still read `BLOCKED 6` in the old §3.2 |
| **7** G4 | `NoOpReceipt`, the effect contract, 12 effects rewritten | `ED-IN-0278` (H-135..H-141 filed) |
| **13b** H-71 | both halves | `ED-IN-0255` / `ED-IN-0267` |
| **13e** | one reading of the remit | `ED-IN-0272` |
| **13f** | `establish` has an effect | `ED-IN-0271` |
| **13d-i** items (1)–(4) | offices as data | `ED-IN-0273` — **item (5), `offices.yaml`, is still OPEN** |
| **24d-i** | the dwelling substrate | `ED-IN-0274` — **DONE, not DONE·INERT** |
| the old §3.1 **phases α and β** | entirely spent | ARMATURE §1.1, document 1 (a) |
| **H1, H2** (decision-layer plan) | record hygiene; the deontology gate | 2026-09-27. H2 is **inert** at `refusal_axis=None` (H-146) |
| **M0–M4** (retirement plan) | `test_j2` forked; roster 9 → 6; `faction_q.resolve`; `seam/wrappers/mass_battle.py`; `massbattle.py::resolve_field`; `march` + ENCOUNTER + garrison Sites | `ecacb57`; `ED-IN-0279` resolved. **Position 20 had no row for this. It is recorded here as `20-i` DONE** — the retirement plan's own proposed split, which was never applied |
| **MB**: A1, A2, A3+C5, A4, A6, A7, A8, C4, d.1 | the squad-engagement Tier-1/Tier-2 slate | `ED-MB-0068`..`0074` (`HANDOFF_MB.md`) |
| **SC**: PHASE 0; PHASE 1 steps 2, 3, 4(c); PHASE 2 step 8; the gate half of step 11 | proceedings foundations | `21:411-472`; `ED-IN-0205`; PR #432; `witness.py:369-371`; the `release` row; `state/gate.py::tenure_write_basis`'s conferral clause |
| **§5 items 1, 3(i), 3(ii), 6** of the 2026-09-18 plan | struck or ruled | `ED-IN-0261`, `ED-SE-0051` / `ED-SE-0054`, `ED-WR-0010` |

### 2.3 The state index — every carried and new position, where it sits in §3

This is the state at adoption. It replaces the 2026-09-18 plan's §3.2 **as the state surface**. The
four rows of that table found stale in this pass are corrected here, not there: `13d-ii` (DONE by 6),
`18a` (eleven fields), `20` (split) and `24f` (its gate, 5, is DONE). New positions are marked ✦.

| # | handle | lane | `STATE` | `GATE` | placed at |
|---|---|---|---|---|---|
| 1 | **CLOSE-PASS** | IN | OPEN · partial | — | Phase 1 · 1 |
| 2-i ✦ | **RET-SC (stub)** | IN/SC | OPEN | — | Phase 1 · 3 |
| 2-ii ✦ | **RET-SC (kernel)** | IN/SC | BLOCKED | `28-iii`, `29b`, `22` | Phase 4 · k |
| 3–7 | G1a · G1b · G2 · G3 · G4 | IN | **DONE** | — | §2.2 |
| 7a | **COMMIT-EFFECT** | IN | OPEN | `15`, `15c`, `15b` | Phase 2 |
| 8 | **H-98 (b)** | IN/PC | OPEN | `FIGHT-RENAME` (serial edge, §3.5); 7 ✓ | Phase 3 |
| 9 | **PC-SURRENDER** | PC | **JORDAN** | §5.1 item 7 | Phase 3 |
| 10 | **U5 / R-07** | IN | OPEN | 7 ✓ | Phase 3 (head) |
| 11 | **U6** | IN | OPEN | `10` | Phase 3 |
| 11a | **REACH** | IN | OPEN | S4 ✓ (closed, old `_part2:750`) · 4 ✓ | Phase 2 (head) |
| 11b | **CALENDAR-EMIT** | IN | OPEN | `11a` | Phase 2 |
| 12 | **H-62-rest** | IN | BLOCKED | the cells commit (`12b`/`12c`) | Phase 3 |
| 12b | **AFFILIATIONS** | IN | **JORDAN** | §5.1 items 1, 3 | Phase 3 (cells commit) |
| 12c | **THE FIFTEEN** | IN | **JORDAN** | §5.1 items 1, 2 | Phase 3 (cells commit) |
| 12d | **THE RENAME** | IN | OPEN · partial | its substrate half rides the cells commit | Phase 3 (cells commit) |
| 12e ✦ | **H12 / H13, held** | IN | BLOCKED | H12: a post-H6 re-measure (not Jordan, §5.2); H13: §5.1 item 5 | Phase 3 |
| 13 | **W28-cast** | IN | OPEN | — | Phase 1 · 8 |
| 13b · 13e · 13f | | IN | **DONE** | — | §2.2 |
| 13d-i | **OFFICES AS DATA** | IN | items (1)–(4) DONE · **item (5) OPEN** | — | Phase 1 · 8a |
| 13d-ii | **PURVIEW** | IN | **DONE (by 6)** | — | §2.2 |
| 14 | **U7-own** | IN | BLOCKED | `12`, `13` | Phase 3 |
| 15 | **Record-kind fold** | IN | OPEN | `11a` | Phase 2 |
| 15a | ≡ `16` | IN | — | — | merged 2026-09-25 |
| 15b | **LOSSY TELL** | IN | BLOCKED | `15` | Phase 2 |
| 15c | **CONTENT OPERANDS** | IN | BLOCKED | `15`, `16` | Phase 2 |
| 15d ✦ | **`told_by` (a)/(b)** | IN/SC | BLOCKED | `15b` | Phase 2 |
| 16 | **H-84 · GIVE** | IN | OPEN | `15` | Phase 2 |
| 17 | **U8 / R-06b** | IN | OPEN | `13` | Phase 3 |
| 17a | **OBLIGEES** | IN | OPEN | `7a`, 13e ✓ | Phase 2 |
| 17b ✦ | **TERM · UPKEEP** | IN/SE | BLOCKED | `17a` | Phase 2 |
| 18 | **PROC-A** | SC | OPEN | — | Phase 1 · 9 |
| 18a | **FIELD DELETIONS — eleven** | IN | OPEN | `17a`, `13d-i` (incl. item 5), 13d-ii ✓, `18` | Phase 2 |
| ★ | **APERTURE RE-MEASUREMENT** | IN | OPEN | `18a` | Phase 2 |
| 19 | **U7-remit** | IN | OPEN | `★`, 6 ✓, `15`/`15c`, `18` | Phase 2 |
| 19b | **U7-disp** | IN | OPEN | **JORDAN** (`ED-IN-0210`, §5.1 item 6) + `15`/`15c` | Phase 2 |
| 19c | **MIGRATE** (+ `24d-ii`) | IN/SE | OPEN | 24d-i ✓ | Phase 2 |
| 19d ✦ | **DEMAND · DELIVERY** | SE/IN | BLOCKED | `15c` | Phase 2 |
| 20-i ✦ | **faction scale, first cut** | IN | **DONE** | — | §2.2 (`ecacb57`) |
| 20-ii ✦ | **U9 / R-04 — faction queries** | IN | BLOCKED | `★` | Phase 4 · a |
| 20-iii ✦ | **the information cluster** | IN/FI | BLOCKED | `15` (20-i ✓) | Phase 2 |
| 20-iv ✦ | **d.1 + terrain on the season path** | MB/IN | BLOCKED | `20-ii`, `28-iii` | Phase 4 · e |
| 21 | **U10** | IN | BLOCKED | `20-ii` | Phase 4 · b |
| 22 | **PROC-B** | SC | BLOCKED | `18`, `★` | Phase 4 · l |
| 22a ✦ | **proceedings PHASE 3** | SC | BLOCKED | `22`, `15d` | Phase 4 · m |
| 22b ✦ | **proceedings PHASE 4** | SC | BLOCKED | `22` (+ `17b` for `term`) | Phase 4 · m |
| 23 | **PART-E-0/2** | IN | OPEN | `22` | Phase 4 · m |
| 24 | **SE-BUILD** | SE | OPEN · partial | re-scoped across `24d`–`24h` | — |
| 24d-ii | **CAPACITY** | SE | BLOCKED | 24d-i ✓; lands inside `19c` | Phase 2 |
| 24e | **WORKS · FOUNDING** | SE/IN | BLOCKED | `15`, `15c`, 24d-i ✓ | Phase 2 |
| 24f | **SUBSISTENCE IS TERRITORIAL** | SE | OPEN — **ungated: its gate, 5 = G2, is DONE** | design before code | design Phase 1 · 10; build Phase 2 (tail) |
| 24g ✦ | **bodies clock + P3 individuation** | SE | BLOCKED | `24d-ii`, `24f`'s cohort producer, `ED-IN-0247` (**JORDAN**, §5.1 item 8) | Phase 4 · n |
| 24h ✦ | **S5 — revolt (P5), forswearing (P6)** | SE/IN | BLOCKED | `20-ii`; P7 **JORDAN** (§5.1 item 11) | Phase 4 · o |
| 25 | **MB-GOLDEN** | MB | OPEN | — (`ED-MB-0016` is `needs_jordan: false`) | Phase 1 · 11 |
| 26 | **GO-VERSION** | GO | **JORDAN** | §5.1 item 9 | Phase 4 · p |
| 27 | **WR-SCOPE** | WR | OPEN | — (`ED-WR-0010` ruled IN SCOPE) | Phase 3 (parallel) |
| 28-0 ✦ | **ORPHAN-DELETE** | IN | OPEN | — | Phase 1 · 2 |
| 28-i ✦ | **M5 — tools** | IN | OPEN | — | Phase 1 · 4 |
| 28-ii ✦ | **M6 — successor goldens** | IN | BLOCKED | `28-i` | Phase 4 · c |
| 28-iii ✦ | **SPINE-DELETE** | IN | BLOCKED | `28-ii` | Phase 4 · d |
| 29a–29f ✦ | **Step B, per tree** | IN | BLOCKED | per tree (§3.4 f–j) | Phase 4 · f–j |
| — | **FIGHT-RENAME** | IN | OPEN | — | Phase 1 · 5 |
| — | **OPENERS-DERIVE** | IN | OPEN | — | Phase 1 · 6 |
| — | **GATE-REMOVE-PERSON** | IN | OPEN | — | Phase 1 · 7 |

⚠ **ONE PLACEMENT IS THE AUTHOR'S, NOT FABLE'S, AND IS MARKED SO.** Fable's state list carries
`13d-i` item (5) as OPEN, and `18a`'s gate names `13d-i` whole (r2 item 14 depends on item 10 whole,
`05:1254`). But no phase table in the Fable pass lists item (5). It has no gate, which is Phase 1's
definition, so it is placed there as `8a` beside `13`. If a later pass places it elsewhere, the one
constraint is that it lands before `18a`.

---

## 3. THE SEQUENCE — THE SINGLE PLAN

**This section is the only ORDER in the repository.** It has four phases, and they are the phases the
dependency graph actually demands. The `STATE` legend is §0's. `GATE` names what blocks. The
2026-09-18 plan's `§3.9` hard serial edges still bind, because they are facts about shared files.
§3.5 adds the edges this pass found.

**How the phases relate.** Phase 1 is a **set**: every item in it has `GATE —` at HEAD, and its items
are parallel-safe unless they share a file (noted per item). Phases 2 and 3 are **serial chains** on
shared files. Phase 4 is the scales and the retirement, each row gated by name. A phase boundary is
an ORDER, not a gate. Where a later phase's head has no unmet gate — `11a` today — the §3.9 file
census, not the phase number, decides whether it may run beside a Phase-1 item.

### 3.1 · ⭐ START HERE — PHASE 1: gate-free, now

| # | handle | what runs | `STATE` | `GATE` / notes |
|---|---|---|---|---|
| 1 | **CLOSE-PASS** (position `1`) | flip the 2026-09-18 plan's §2.1 rows with their citations; write §5.2's closures with theirs; ship the **fold-to-latest script** as the instrument (old §8.3) | **DONE** (`ec1a9d0`, §8.3) | — |
| 2 | **`28-0` ORPHAN-DELETE** | `FORK:` rows + `git rm` for code with no live caller (list below, narrowed — §8.4) | **DONE**, narrowed scope (§8.4) | — ; precedent `ED-IN-0232` |
| 3 | **`2-i` RET-SC (stub)** | `contest_legacy_stub.py` + its export ripple; the seam-import detector's one-hop falsifier | OPEN | — |
| 4 | **`28-i` (M5)** | port `tools/balance_oracle.py` onto the season harness; retire `campaign_output_probe.py`, `trace_execution_phases.py` and the execution-map cluster | OPEN | — |
| 5 | **FIGHT-RENAME** | `kill / wound` → `fight`: one row key + one alignment key + re-pins; a declared hash move | OPEN | — ; **before `8`**; never interleaved with `8`, `9` or the cells commit (`§3.9` edge 10) |
| 6 | **OPENERS-DERIVE** `[L1]` | derive the `openers:` roster from the `@effect_for` registry, or guard their equality | OPEN | — ; before any Phase-2 effect lands |
| 7 | **GATE-REMOVE-PERSON** `[L1]` | route `World.remove_person` through `World.write`; a declared hash move | OPEN | — ; shares `loop/matter.py` with `24f`'s build — serial |
| 8 | **`13` W28-cast** | the `cast:` blocks and their reader in `build_at`; the harness loader's count | OPEN | — ; precondition of `17` and of `ED-FI-0009` |
| 8a | **`13d-i` item (5)** | `offices.yaml` + its `harness/populated.py` wiring; the `titles` fold | OPEN | — ; before `18a` (placed by the author, §2.3) |
| 9 | **`18` PROC-A** | re-host the 28 stress tests; `world_q.judging_set`; `convene` + the `rank` stem; `arrangements.yaml` through the one loader; D-6/D-7 as swept fixtures | OPEN | — (SC lane); a hard dependency of `18a` and `19` |
| 10 | **`24f` — the design step** | specify who eats; **NAME the cohort producer** before any code | OPEN | — ; its code shares `matter.py` with item 7 |
| 11 | **`25` MB-GOLDEN** + the MB hand pass | the golden-mode ruling; `ED-MB-0057`, `ED-MB-0044`, `config.py:315-317`; A5; A9; the unblocked Sequenced rows; `ED-MB-0075`'s option (2) after its superseding row | OPEN | — (MB lane, parallel) |
| 12 | **PC lane** | the `partisan` deletion; Ob-from-defender (`core.py:79-83`) | OPEN | — (PC lane, parallel) |

**Each item — why here, and what it must satisfy.**

**1 · CLOSE-PASS.** It flips the 2026-09-18 plan's §2.1 rows with their citations, writes §5.2's
closures below with theirs, and ships the fold-to-latest script. Without that script the acceptance
line cannot be checked (old §8.3: *"37 after folding append-only rows to the latest per id"* against
three other figures). Its instruction and falsifier are the old `_part2` position 1. Two things
changed since that entry was written:

- **`ED-IN-0210` keeps `needs_jordan` deliberately.** Its one live fork survives the five tests
  (`ED-IN-0211`), so the pass must **skip it by name** (old §8.3).
- **The escalation the ledger was missing is already filed, with this document.** This is
  contradiction 8 of the armature's nine (§4), resolved as follows.

> **Contradiction 8 · `ED-IN-0251` row 2's field against its own text — RESOLVED by §0 test 5, with a
> new row rather than a correction.** The governing row (`registers/editorial_ledger_in_archive.jsonl:168`,
> 2026-09-19, `supersedes_row: true`) has the field `needs_jordan: false`. Its own text says R3 is
> *"still needs_jordan and still Jordan's to author"*. The decision-layer plan declined to settle which
> half was right (its §1.1), and then found that *"under any of these counts, zero `needs_jordan: true`
> rows is an under-report"* (its §1.2). Four content items survived its five-step gate, and none had a
> row saying so. The flag belongs on **`ED-IN-0261`** — the ruling under which the cells are now
> authored (fifteen pursuits over seven axes, the verb split) — not on a rewrite of `ED-IN-0251`, whose
> thirteen-over-four basis no longer exists. **Landed with this document (§8.1):** a new `ED-IN-0261`
> row, `needs_jordan: true`, covering C1 + C2, with C3/C4 as its siblings. Close-pass inherits it and
> writes nothing further for it.

**2 · `28-0` ORPHAN-DELETE.** ⚠ **NARROWED AT EXECUTION — see §8.4.** "Zero importers by the `ast`
scan" is true of every item below and was taken as license to delete all of them; it does not mean
zero *callers*, and for most of this list it isn't one. Executed now, each a `FORK:` row plus `git
rm`, then one `tools/export_composition.py` regeneration:

- `engine/cross_scale/domain_echo.py` (§1) — confirmed zero callers anywhere, including
  dynamically;
- `systems/fieldwork/sim/{fieldwork,investigation}.py`, with the roles
  `scene_resolver.fieldwork/investigation` and `scene_dispatch.py:354-356`'s stub branch. The branch
  removal is a deletion edit only, falling the two scene_types through to the existing total-mapping
  stub fallback (same `stub=True` shape). `ED-916` closes under this — this is its subject.

**DEFERRED to `28-iii`, when `engine/tests/test_pipeline_reach.py` itself retires (§3.4) — not
gate-free today, §8.4:** `engine/autoload/npc_ai.py`; `systems/overview/sim/{rs_track,ip_track}.py`
with the role `rs_track_delta`; the six FA stubs
`systems/factions/sim/{charter_liberties,hafenmark_equipment,home_sanctuary,infrastructure_reclamation,varfell_mandate_action,varfell_territorial_acquisition}.py`;
`systems/world/sim/{miraculous_event,restoration_movement}.py`; `systems/characters/sim/companion.py`
— all thirteen are `_OI17_FULL_MODULE_ENTRYPOINTS` targets, dynamically probed every run by a
currently-passing test this plan's own §3.4 schedules for later retirement. Deleting any of them now
would fail that test today for no gain.

**REMOVED FROM THIS POSITION'S SCOPE, not merely deferred — `references/module_contracts.yaml`
already ruled it, §8.4:** the roles `territory_transfer_candidate` and `territory_transfer_proposal`.
Their own registry rows (`:116-122`) already say why they stay: the targets
(`systems/factions/sim/parliamentary_transfer.py`, a permanent, non-orphaned module) resolve,
`tools/export_composition.py` imports them at export time, and deleting the rows would hide a real,
working mechanic with no driver behind a tidy registry rather than leave the gap named. No position
in this plan gates that ruling; it stands until someone builds the driver, which is out of this
position's scope.

`beliefs.py` joins this list after `28-iii`, when it becomes orphaned. The precedent is
`ED-IN-0232`, which retired six files with the substrate and recorded the roster shrink in
`test_mc_v18_is_deprecated.py:84-107`. `test_forked_status.py`'s `UNRESOLVABLE_CEILING` is a `<=`
ceiling on rows that cannot be followed, so new resolvable `FORK:` rows do not trip it. **Why first
among the deletions:** it shrinks every later disposition table in `_part2` §1 and costs no gate.

**3 · `2-i` RET-SC (stub).** Position `2` is split, because only half of it is gate-free.

- **`2-i`, now:** `contest_legacy_stub.py`, plus its export ripple (`engine/engine_params/sim_params.json:3851`,
  `value_pointer_links.json`), plus the seam-import detector's one-hop falsifier. That falsifier is a
  Layer-1 ride-along (the old `_part2` position 2 (f)): `_relative_module_files` has had no planted
  falsifier since the combat-loader consolidation.
- **`2-ii`**, the 14-module kernel and the veto relocation, waits on `28-iii`, `29b` and `22`
  (§3.4 k).

The old `_part2` position 2 remains the content owner. **Relocate the demote-only rule first**, as it
says.

**4 · `28-i` (M5).**

- **Port `tools/balance_oracle.py` → `engine/season/harness/arms.py`**, as an n-seed two-arm comparison
  over `build_realm` outputs. There is no win-share on the season side; the quantities are
  `harness/report.py`'s and `delta.py`'s, and `corpus_run`'s. Re-point
  `tests/valoria/test_balance_oracle_arms.py`, and update the `references/ci_checks_registry.yaml:454`
  row.
- **Retire `tools/campaign_output_probe.py`**, which `harness.report`/`delta` + `content_hash`
  supersede.
- **Retire `tools/trace_execution_phases.py`, and with it the execution-map cluster it feeds:**
  `tools/build_execution_map.py`, `references/execution_map.json`, `references/EXECUTION_MAP.md` and
  `tests/valoria/test_execution_map.py`. That cluster's ED, `ED-IN-0123`, was closed in the old §2.1
  under test 1; its "spine" is hand-transcribed from `mc_v18.py`/`engine_clock.py`.
- **Check `tests/valoria/conftest.py` and `test_flow_skeletons.py`'s reads of `execution_map.json`
  first** — not verified in this pass (§9).

**Why here:** it is gate-free, and `28-ii` depends on it. It also closes MOD 8 (the balance
instrument sitting on the spine).

**5 · FIGHT-RENAME.** This is contradiction 4 of the armature's nine (ARMATURE §1.2).

> **Contradiction 4 · the `kill / wound` rename — RESOLVED: rename the row STANDALONE NOW to `fight`;
> the SPLIT (`kill`, `wound`, `challenge` → `accept`) still rides the cells commit (H6 + H8). Both
> signals are honoured.** It is answered by §0 test 1 — Jordan's 2026-09-27 instruction is later than
> the 2026-09-20 ruling and PR #434's standing order, on the one point it addresses — plus test 3 for
> the name. Not Jordan.
>
> - **What "unbuildable" actually covers.** The technical claim (`HANDOFF_IN.md`'s verb-split row; the
>   decision-layer plan §3.1) is about a two-step **split**. `data/verbs.py:685-692` `_load_alignment`
>   raises on any alignment key not in `VERB_TABLE`, so five new rows cannot land without five
>   alignment rows of cells. It does **not** forbid renaming **one** row's key together with its **one**
>   alignment key in the same commit.
> - **What the rename touches.** It is an atomic two-key rename: `verb_table.yaml:289`, plus the
>   `kill / wound` block in `rosters.yaml`'s `alignment` table. It needs re-pins — the never-attempted
>   set at `test_season_shape.py:6996`, and `WHERE THE 39 GO` — and a **declared content-hash move**,
>   because Acts carry the verb name.
> - **Why the renamed row IS H6's `fight`.** Jordan's instruction (`HANDOFF_IN.md`, recorded
>   2026-09-27) is a rename/reframe: *"a character can only attempt to kill or wound, never choose the
>   outcome directly"*. That is precisely the attempt-verb semantics `ED-IN-0261` ruled — *"`fight`
>   (opponent is `subject`, needs a typed precondition …)"* (the ledger row text;
>   `verb_table.yaml:298` `requires_typed_note`). The decision-layer plan's own H6 deliverable says
>   `fight` takes *"the `kill / wound` clause, `verb_table.yaml:293-296`"*. H6 later **adds** `kill`,
>   `wound`, `challenge` and `accept` beside it. Those express the actor's **intent** (to the death
>   against first blood), never the outcome, which stays degree-keyed: Felled / Wounded / Untouched.
> - **Sequence.** It is its own small step in Phase 1, **before** position `8` (H-98b), and never
>   interleaved with `8`, `9` or the cells commit (`§3.9` edge 10).
> - **Name.** `fight` is the ruled name (§0 test 3); there is no question to put to Jordan.
> - **Record edits, made in this commit (§8.1).** `HANDOFF_IN.md`'s "same-day conflict" row is struck
>   as resolved. The standing order is narrowed to *"the SPLIT rides the cells commit"*.

**6 · OPENERS-DERIVE** `[L1]`. The `openers:` roster is a hand-copied second copy of
`loop/effects.py`'s `_eff_*` opener bodies. It is correct today, and silently wrong the day an opener
is added without updating it: the `CLAUDE.md` §8 "every rule lives once" hazard, recorded open at
`HANDOFF_IN.md`'s Layer-1 backlog row. Either derive the roster from the `@effect_for` registry, or
guard their equality. **Why here:** Phase 2 adds effect bodies (`7a`, `15`, `16`, `17a`, `17b`, `19`,
`24e`), and each of them risks the hand copy. Fixing it first means every later effect is written
against one owner.

**7 · GATE-REMOVE-PERSON** `[L1]`. `World.remove_person` bypasses the gate. Route it through
`World.write` at all three callers: `_eff_kill`, `_eff_march`, and `loop/matter.py:298-326`. It needs a
declared hash move. This is the one live violation of the AX-4 *property*. The property is
MECHANICAL via `World.write` + tokens (G2/G4), which makes the abandoned AX-4 setter scan a CONVENTION
duplicate (`_part2` §2). The fix closes the gate-bypass half of H-152 and MOD 7. **Serial with
`24f`'s build**, since both edit `matter.py`.

**8 · `13` W28-cast.** Author the `cast:` blocks and their reader in `build_at`, in the same commit;
use the harness loader's count, never a grep (old §6's GAP). **Why here:** it has no gate, and it is
the precondition of two later items. `17` builds ambitions from the cast. `ED-FI-0009` needs
`capability` to carry its world-gen value, which is F.6's *"world-gen writes it once"* — today
`capability` is zeroed on every corpus person. The old plan's §7 item 6 still governs the reader's
placement (it moved from U8 to here and was held back as a content move).

**8a · `13d-i` item (5).** `offices.yaml` and its `harness/populated.py` wiring. Two things fold in
here, and neither is Jordan's:

- **The fate of `title_domain` and the `titles` roster** (MOD 5), answered by Layer 1 (§0 test 3).
  `04 §B.7:308` says there is *"no `Title` type"*, and `04 §E.1:1067` calls `titles.domains`
  *"world-generation content read at step 9"*. So `titles` is world-gen DATA, and it folds into
  `offices.yaml` — r2 `05`'s RULED (c).
- **`proposals/2026-09-16-term-ownership/offices_draft.yaml`** (570 rows), which is verified against
  canon first. r2 `03:1043-1056`'s roster VALUES are superseded by `ED-IN-0256` rulings (2) and (3);
  r2 supplies the structure.

**9 · `18` PROC-A.**

- Re-host the 28 stress tests, whose tracer is gone.
- Build `world_q.judging_set(w, venue, matter)`.
- Add `convene` and the `rank` stem.
- Load `arrangements.yaml` through the one loader.
- Implement **D-6/D-7 (the `speech_kinds` roster defaults) as swept fixtures**, in the `H-128` shape
  (§0 test 5; §5.2). They are not Jordan's.
- Fold in proceedings PHASE 2 steps 6, 7, 9 and 10.

**Why here:** it is gate-free and in the SC lane. It is a hard dependency of `18a` (which deletes only
the stub `18` replaced, `§3.9` edge 5) and of `19` (whose `determine` consumes `judging_set`). Its
content owner is the old `_part2` position 18 plus `21_RECONCILIATION.md` PHASE 2.

**10 · `24f`, the design step.** Its old gate was `5` (G2, because `24f` touches `matter.py`'s
subsistence pass), and G2 is DONE, so it is ungated. Its old row says *"design before code"*. The
design step comes first because its candidate (`weight > 1` eats) is **dead on arrival** until
something mints cohorts (old §5 NOT-JORDAN table, attacked 2026-09-25). The step has three parts:

- specify who eats;
- **name the cohort producer and what it mints from** — this *is* narrative #13, *"populace as a
  weighted person"*, the synecdoche Jordan's ruling asks for (`ED-IN-0255`);
- do both before any code.

The build is the tail of Phase 2. It is serial with item 7 on `matter.py`. It must precede any
`body_step` pick (`§3.9` edge 8; §5.1 item 8).

**11 · MB lane.**

- `25` MB-GOLDEN applies the golden-mode ruling. `ED-MB-0016`'s governing row is `needs_jordan: false`
  (2026-09-15), so the position is OPEN, not Jordan's.
- The **MB hand pass**: `ED-MB-0057`'s dead-primitive dispositions (`resolve_internal_collisions`
  re-adjudicated to DELETE), `ED-MB-0044`'s gauge fix (`tests/sim/gauge_mb.py:330-331`), and the
  `config.py:315-317` comment.
- A5 and A9.
- The **Sequenced rows the MB work has now unblocked**: headless duels (the provider exists), the
  generated map (A1 is done), and AI generals (A1–A4 are done).
- **`ED-MB-0075`'s option (2)**, built after its superseding row (§5.2).

Per-cell Q and army-scale envelopment (the multiunit Phase 0 spike) keep their existing gates. These
are lane items, not positions — the old plan's *"parked, with reasons"* convention for a hand pass.

**12 · PC lane.** The `partisan` deletion (`weapons.py:322,852`) and Ob-from-defender
(`combat_engine_v1/core.py:79-83`). Both are ruled and ungated. Beside them is one administrative item,
not a design call: the PC `ED-` id block is exhausted (`references/id_reservations.yaml:124`), so a
reservation comes first, under the file's own Lane-B procedure.

### 3.2 · PHASE 2 — governance and settlement content, serial on shared files

This is the old plan's phase γ, carried with its 2026-09-25 corrections, plus four new lettered rows
(`15d`, `17b`, `19d`, `20-iii`) and one re-count (`18a`: eleven fields, not twelve). Every effect body
added here is written once, to the G4 contract: build the object locally and return
`Change((Subject…), lambda: …)`, never mutate eagerly in the effect's own body (`H-137`). Every
`STATE` is as §2.3 reads.

**The chain:** `11a` → `11b` → `15` → `16` → `15c` → `15b` → **`15d`** → `7a` → `17a` → **`17b`** →
**`19d`** → `18a` → `★` → `19` → `19b` → `24e` → `19c` + `24d-ii` → **`20-iii`** → `24f` (build).

| # | position | what runs | why here |
|---|---|---|---|
| 1 | **`11a`** REACH | `reach` · `place_of` · two question sources deleted · `w.crossings` deleted · `occasioned_by` → one route | Both recorded gates are met: S4 closed, and G1b's deletion (`§3.9` edge 1) landed. It heads the chain because `15` waits on it. Detail: old `_part2` 11a |
| 2 | **`11b`** CALENDAR-EMIT | CALENDAR `emits="date.fired"`, `subject=venue` | Observable on the corpus's planted `d_forced` dates (`harness/corpus_run.py:320-325`), so no ad-hoc plant is needed. Old `_part2` 11b |
| 3 | **`15`** Record-kind fold | Petition/Dispensation become kinds of `Record`; `record_kinds` + its refusal; `issue`/`petition` bodies; the deposit rule; then `petition` + `carry`. **≡ build-order item 5** | The largest item: `16`, `15c`, `15b`, `7a`, `19b` and `24e` hang off it. G4 is DONE, so its effects are written once. `record_kinds` is also where narrative #10's casus belli becomes a Record (then `20-ii`/H-151). Old `_part2` 15 |
| 4 | **`16`** ≡ `15a` GIVE (H-84) | one verb that moves a Record to another person — and proceedings PHASE 1 step 1's record-moving route | r2 dependency 5 → 6. Narrative #11 (the writ) follows it — *"there is no player"* (v7 §8.5). Old `_part2` 15/16 |
| 5 | **`15c`** CONTENT OPERANDS | content-claim operands; Q2's third clause; the invariant statement | r2 dependency 5, 6 → 7. **It widens `requires_operands`**, which `19`, `19b`, `24e`'s `found` and a computed `establish` all need before a computed act can form. Old `_part2` 15c |
| 6 | **`15b`** LOSSY TELL | `tell` at `Partial` deposits a lossy copy, and the teller's identity | r2 dependency 5 → 8. Narrative #12 (telling renews belief) is this item. Old `_part2` 15b |
| 7 | **`15d`** ✦ `told_by` (a)/(b) | proceedings PHASE 1 step 4 parts (a) and (b): the (person, channel) precedence walk, and the document/remit → `told_by` source map | WITNESS-side, on the same file as `15b` (`loop/witness.py`), so it comes right after. Part (c) is built (`witness.py:369-371`), but `witness.py:182` still returns only `firsthand`/`firsthand_via_knot`. **R-07 rests on it, and no position carried it.** `22a` waits on it |
| 8 | **`7a`** COMMIT-EFFECT | `@effect_for("commit")` — mint the Tenure the `commit` row already declares | Its aperture opens only now: BO-10 names build-order items 5 / 7 / 8, which are `15` / `15c` / `15b`. Built earlier, its first run re-measures `commitment.made 0 / refused 42`. Old `_part2` 7a |
| 9 | **`17a`** OBLIGEES | obligees co-located mint `inferred` · `oblige` body · `establishment_of` rewritten with a caller · `Office.establishment` deleted | After `7a`; after `13e` ✓ (same function, `§3.9` edge 4). Old `_part2` 17a |
| 10 | **`17b`** ✦ TERM · UPKEEP | `Tenure.term`, the T-n basis at the gate, **`Office.upkeep`'s reader**, and payment by `transfer` renewing `oblige` terms | Gate `17a`: `_eff_oblige` is what mints the term-bearing Tenure. The full reasoning is contradiction 1, below |
| 11 | **`19d`** ✦ DEMAND · DELIVERY | the retirement plan's ADJACENT G3: `demanded` / `delivered`, plus the scarce test world | Gate `15c` (its operands). Beside `24f`, whose territorial quantity it feeds |
| 12 | **`18a`** FIELD DELETIONS | **eleven** fields; `conferral_path` re-pointed at `ancestry`; only the `judging_set` **stub** | Gates `17a`, `13d-i` whole (incl. item 5), 13d-ii ✓ and `18` (which built the real `judging_set`, `§3.9` edge 5). **Not `Tenure.payload`**, which is live (`§3.9` edge 11). **Not `Office.upkeep`** — contradiction 1. Old `_part2` 18a |
| 13 | **`★`** APERTURE RE-MEASUREMENT | **build the populated-realm formability instrument as its first step**; then re-take, per holder: verbs resolvable, verbs unformable person-side, claims by source, questions by source; then re-take `CAT-6`'s evidence block and `STR-4`'s conclusion | Fires once, after `18a`. **Nothing below may be scored before it passes.** The instrument does not exist (old §6's GAP), and it is this gate's first step, not a separate position. Old `_part2` ★ |
| 14 | **`19`** U7-remit | `levy`'s typed cell · `open_case` · `determine` over `judging_set` · `issue` via `15` — predicates, effects and operands | After `★`, 6 ✓, `15`/`15c` and `18`. **Layer-1 ride-along: invariant 4's per-conjunct half**, a keyed `emits_on_refusal` schema. Three live verbs have two conjuncts and `19` adds more, so the schema — `23`'s invariant work — is brought forward to its first consumer. Old `_part2` 19 |
| 15 | **`19b`** U7-disp | build the three response verbs — `comply`, `evade \| defy`, `construe` | **JORDAN**: `ED-IN-0210`'s fork (§5.1 item 6). Also waits on `15`/`15c`: the operand is a dispensation, which is a `Record` kind only after the fold. It stays conditional on the ruling, as the old §7 item 5 held. Old `_part2` 19b |
| 16 | **`24e`** WORKS · FOUNDING | the `works` kind · `work` advances `stage` · `restore` body · `found` + body · `(Rung\|Site, exists)` get a producer | After `15`, `15c` and 24d-i ✓. Answers `ARCH F.20` (*"the world only decays"*) and is the R-half with no player in it (§0.06). Narrative #9 is this item. `ED-SE-0052`/`0053` ride it. Old `_part2` 24e |
| 17 | **`19c`** MIGRATE, **carrying `24d-ii`** | a migration verb; the presence/residence split; `capacity(w, rung)` lands here as its only in-scope caller; the `travel_leg` fix | After 24d-i ✓. A Query nobody calls is `ID-13`'s shape, so `capacity` lands with `migrate`. Old `_part2` 19c / 24d-ii |
| 18 | **`20-iii`** ✦ the information cluster | narrative #14 §F (D1-a) and the chain half of #7 (*intelligence before action*); #7's FI-lane half is `ED-FI-0009` (Phase 3) | After `15` (Records to carry intelligence) and 20-i ✓ |
| 19 | **`24f`** — the build | the territorial subsistence quantity with population synecdoches, on the cohort producer Phase-1 item 10 named | Only after item 10 has named the producer. Serial with GATE-REMOVE-PERSON on `matter.py`. Precedes any `body_step` pick. Old `_part2` 24f |

> **Contradiction 1 · `Office.upkeep` — RESOLVED: it comes OFF `18a`'s deletion list and gets its
> reader at the new position `17b`.** This is answered by a design document (§0 test 3), not by Jordan.
>
> - **Layer 1 has the field.** `architecture/meta/04_CODE_ARCHITECTURE.md:311-314`:
>   `Seat := ( …, upkeep, dates[], exists )`. `upkeep` is in the RATIFIED Seat.
> - **r2's own ledger already refused the deletion.**
>   `proposals/2026-09-17-governance-and-holdings-r2/05_LEDGER_AND_BUILD.md:1659`: *"Deleting
>   `Office.upkeep` **removes the carrier, not the gap.** F.18's own resolution is 'the repair is a verb'
>   and no verb is proposed … ⚠ **And `upkeep` is in the ratified `Seat :=`**"* (RR-B limb B-1). So
>   `18a`'s list — old `_part2:1294-1297`, inherited from r2 `05:223-256` — contradicts r2's own
>   "Explicitly NOT closed" section.
> - **Layer 1 names the repair's shape.** `04:1099`, F.18: *"A MATTER payment would be a fourth clock,
>   so the repair is a **verb**"*. That is exactly the retirement plan's G2 shape. Payment is the
>   existing `transfer`. `oblige` Tenures carry a T-n term that the paying act renews. `Office.upkeep`
>   is the per-obligee amount, typed, with a fixture default and a 3-point sweep.
> - **Consequence: `18a` deletes eleven fields, not twelve.** The other two Layer-1 collisions on that
>   list were checked. `Office.scope_rung` has NO reader (`state/carriers.py:707`: *"`scope_rung` has NO
>   READER"*; `state/gate.py:177-179`: *"`Office.rung` IS `via.scope` … `18a` deletes"*), so it is safe
>   to delete. `Office.dates` has no reader in `engine/season` non-test code, so it is safe too. Only
>   `upkeep` collides.
> - **What `17b` is.** It is the retirement plan's own proposed handle. It carries `Tenure.term` — F.3,
>   work-order item 6, and the edge half of `21` C-10: the field T-n needs, which G3 left "unbuildable".
>   It also carries the T-n basis at the gate, `upkeep`'s reader, and payment by `transfer` renewing
>   `oblige` terms. The same field is proceedings PHASE 4 step 22 and narrative #4.
> - **Gate: `17a`.** `_eff_oblige` is what mints the term-bearing Tenure.
> - **Until `17b` lands**, `upkeep` stays declared-but-unread, the way `Tenure.degree` (F.4) does. That
>   is a Layer-1 field awaiting its reader, not `ID-13`.
> - **Narrative #3** (*embezzlement "already runs"*) becomes observable here.

### 3.3 · PHASE 3 — the behaviour layer and the decision layer

This is the old plan's phase δ, carried, with the decision-layer plan's H-steps folded onto the
positions they belong to. `21` (U10) has moved to Phase 4, because its gate is `20-ii`.

**The chain:** `10` (+ AX-7 wiring) → `11` → `8` → `9` → **the cells commit** (`12b`/`12c`/`12d` +
H6/H8) → H7, H3, H9 → `12` remainder → `14` → `17` → H10 → H11 → **`12e`** → `ED-FI-0009` → `27`
(parallel).

| # | position | what runs | `GATE` | why here |
|---|---|---|---|---|
| 1 | **`10`** U5 / R-07 | `stance_delta`; `Person.stance` written; `stance.moved`; `tell` only; a `names_index` entry for `stance`. **+ the AX-7 wiring** — `agreement` / `standing_of` / `belief_contradicts` into the Claim producers (`ED-IN-0244`/`0245` `RR-P`; `loop/witness.py:191,271,361`) | 7 ✓ | After G4, so its effect is written once. The AX-7 wiring's proposed home is here, because this is where the Claim producers are next opened. **Verify RR-P's text first:** `Person.beliefs` is deleted, so `belief_contradicts` may be moot (§9). The field is NOT unwritten — `harness/populated.py` writes `stance` rows at build — so a falsifier must look for a row that moved. Old `_part2` 10 |
| 2 | **`11`** U6 | the first R-01/R-02 measurement. **Pre-flight:** name the R3 owner and denominator (old position `21`'s instruction on `requirements.yaml`'s mutually inconsistent R3 figures, brought forward to the first measurement). **+ the `test_n3` re-pin** | `10` | Prior 100 % at `2x3`. `test_n3` is `HANDOFF_IN.md`'s reverted build-order item 4 (`budget()` should count `t.granted_acts`): the re-pin is declared per `CLAUDE.md` §7 **unless** U6 shows the floor is an R-01/R-02 property (§0 test 5; §5.2). Old `_part2` 11 |
| 3 | **`8`** H-98 (b) | the wound-count band edge at `seam/ladder.py:133-135` → data. (a) has no subject today | `FIGHT-RENAME` | After the rename, so it edits the `fight` row once. Never interleaved with the cells commit (`§3.9` edge 10). Old `_part2` 8 |
| 4 | **`9`** PC-SURRENDER | promote §11.4 Yield/Disengage into `combat_engine_v1/` — **or strike it** | **JORDAN** (§5.1 item 7) | If struck, position `9` leaves the order and nothing else moves. Old `_part2` 9 |
| 5 | **the cells commit** = `12b` / `12c` / `12d` + H6 + H8 | Jordan's cells land; the `(Person, conviction)` carrier + the confliction Query (with a reader); the substrate rename (`descriptor_registry.yaml`'s `conviction_roster`); **the verb split — adds `kill`, `wound`, `challenge` and `accept` beside `fight`**; `role_template_pursuits` validation; the `npe.py` / `conviction.py` audit | **JORDAN** — C1 + C2 (§5.1 items 1, 2) | ONE R6-atomic landing: `_load_projection` / `_load_alignment` raise at module scope, so every table must exist before first import. **If Step B's `29d`/`29e` land first, the `npe.py`/`conviction.py` audit item drops** (both modules are gone). See contradiction 2, below. Old `_part2` 12b–12d |
| 6 | **H7** faith-pair falsifier | Jordan's own falsifier — the devout-Solmund / anti-Solmund `faith` pair must land far apart | cells commit; C2's placement | It is `12c`'s falsifier. The draft cells fail it at the registry's actual clergy weight (.60) and pass only at .45 (`HANDOFF_IN.md`) |
| 7 | **H3** scar counts, pursuits track | per-element counts, thresholds 1/2/3, written at RESOLVE over `observers_for` | cells commit | This **is** `12`'s scar rebuild (`ED-IN-0261` item 4). The float-per-axis code (`loop/effects.py` `_scar`, shipped at `scar_step=0`) is live against the OLD tables once touched, so it lands with or after the content, never before |
| 8 | **H9** crisis reader, threshold 2 | threshold 2 only | H3 | `12`'s remainder |
| 9 | **`12`** remainder | `axis_count` against the count-scar (the count-scar IS the counter — retire the row or give it the field, never both); a `pursuits` trigger | H3, H9 | Old §5 NOT-JORDAN table (step 4/5). Old `_part2` 12 |
| 10 | **`14`** U7-own | the eight `own`-eligibility verbs in antonym pairs; distinct operands; `Candidate.why`; **the `tie / knot` effect** | `12`, `13` | `12 → 14` because 14's contested closers reuse 12's degree-keyed rows. `29f` (knots) waits on the `tie / knot` effect. CANDIDATE-WHY rides here. Old `_part2` 14 |
| 11 | **`17`** U8 / R-06b | `ambitions(p)`; narrative #2, *the patron as a person*, as a `cast:` entry read here | `13` | The cast exists after Phase 1 item 8. It inherits `governance_spine`'s argument for why a third builder is not a flag on `build_realm` (old §3.8b). Old `_part2` 17 |
| 12 | **H10** affiliation plumbing | `12b`'s carrier, `incompatible`, `confliction` | **JORDAN** — C3 (§5.1 item 3) | After the cells commit |
| 13 | **H11** conviction-track scars | the second scar track | **JORDAN** — C4 (§5.1 item 4); H3; H10 | |
| 14 | **`12e`** ✦ held | **H12** (`Person.precedence` / excluders / loop-to-order) is held on a **post-H6 re-measure**, not on Jordan (§5.2). **H13** (crisis threshold 3 + threshold 1's mechanism) is held on G-Q6 | H12: a measurement · H13: **JORDAN** (§5.1 item 5) | Both are the decision-layer plan's tail. Neither blocks a position here |
| 15 | **`ED-FI-0009`** (FI lane) | the six investigation acts' degree producer | `13` | `capability` has its world-gen value only after the cast (F.6). `ED-FI-0002` and `ED-914` are unchanged |
| 16 | **`27`** WR-SCOPE (parallel) | build threadwork: reshape `systems/threadwork/sim/coherence.py` to the model `RULINGS.md` replaced it with; the two `rendering.py` stubs; `ED-WR-0003` | — (`ED-WR-0010` ruled IN SCOPE) | Parallel to the whole chain. **Two Step-B deletions wait on it**: `29a`'s `ms_track.py` (threadwork lazily imports `apply_ms_delta`) and `29f`'s `knots.py` (`opposing.py:239` `sustain_knot`) |

> **Contradiction 2 · C1–C4 "derive automatically, no code change" — RESOLVED to the 2026-09-18
> plan's §3.5 (as narrowed 2026-09-25) and the decision-layer plan's H6.** Answered by §0 test 1:
> measured, and later. Not Jordan.
>
> - **What the retirement plan said.** Its line repeated `01_THE_BUILD_ORDER.md:1028`'s claim that
>   the cells "derive".
> - **What §3.5 of the 2026-09-18 plan had already falsified.** `tools/valoria_rename.py` is retired
>   (`FORK:1e4c6f4`). `names_index.yaml` does not own the roster. The real chain is
>   `descriptor_registry.yaml` → `rosters.yaml` (`from_descriptor:`) → `descriptors.json`.
> - **What still owes code.** §3.5's narrowing: "no `.py` change" holds for `12c`'s tables and NOT for
>   `12b`. `Person` carries no `conviction` field, and confliction is a derived Query, so `12b` owes a
>   carrier and a Query. They land IN the cells commit, with a reader.
> - **What that commit looks like.** The decision-layer plan's H6 (corrected 2026-09-27) makes it ONE
>   R6-atomic commit across five owners, plus the verb split.

### 3.4 · PHASE 4 — the scales, and the retirement of `mc_v18` and its spine

**What this phase does to `mc_v18`.** Every call into the deprecated spine is superseded here: the
spine's modules, its 26 non-survivor composition roles, its 12 production importers and its 17
test/tool importers. The per-file, per-role and per-importer dispositions, each with its reasoning,
are `_part2` §1. The one rule that makes the order below correct is **`requirements.yaml:27-31`'s
gate: a retire-set tree may go only when the loop expresses its scale.** That gate is honoured **per
tree** (`29a`–`29f`), never as one wave. Jordan's 2026-09-28 instruction is consistent with it:
superseding the CALLS means the loop subsumes the SCALES.

| # | handle | what runs | `STATE` | `GATE` |
|---|---|---|---|---|
| a | **`20-ii`** faction queries (U9 / R-04) | `faction_q.{holdings,purview,superiors,subordinates,at_war}`; `head` via `Tenure.degree` (F.4's first reader); `scale_of_rung`; the 44 faction-scale re-scales and the 10 world cases; **edit `04 §A.2:132`** to name the fourth `queries/` module | BLOCKED | `★` |
| b | **`21`** U10 | the second measurement; `measured:` from instrument output only | BLOCKED | `20-ii` |
| c | **`28-ii`** (M6) — successor goldens | (1) a **named** same-seed hash pin on `build_realm(0)` × N; (2) a battle executing from a real, chooser-formed decision | BLOCKED | `28-i`. `15c` helps the operand arm, but the per-verb cell does not need it |
| d | **`28-iii`** SPINE-DELETE | delete `engine/mc_v18.py` and the engine spine (list below) | BLOCKED | `28-ii` — nothing else. Every engine-spine module already has its season replacement (`_part2` §1.1) |
| e | **`20-iv`** d.1 + terrain/garrison on the season path | `resolve_field`'s units get `morale_start` from season-native faction state; terrain and garrison from `scale_of_rung`; re-pin `test_mass_battle_d1_morale_baseline.py` against `resolve_field` | BLOCKED | `20-ii`, `28-iii` |
| f | **`29a`** overview | `systems/overview/sim/{accounting,ci_track,ms_track}.py` (+ the `test_accounting_accord_drift_probe.py` `FORK:`) | BLOCKED | `28-iii` (+ `27` for `ms_track`) |
| g | **`29b`** factions + **`game_state.py`** | `systems/factions/sim/*` remainder; `engine/autoload/game_state.py`; the `parliamentary_*` roles and modules; the descriptor faction block (list below) | BLOCKED | `20-ii`, `28-iii`, `29a` |
| h | **`29d`** world | `systems/world/sim/{npe,insurgency_pipeline}.py` | BLOCKED | `29b`, `10`; `24h` recommended before it (a choice, not a gate) |
| i | **`29c`** settlements | `systems/settlements/sim/*.py` only — **the geography YAML stays** | BLOCKED | `29b`, `29d`, `24e`, `24d-ii` |
| j | **`29f`** fieldwork/knots, then **`29e`** characters | `systems/fieldwork/sim/knots.py`; then `systems/characters/sim/{conviction,beliefs}.py` | BLOCKED | `14` (the `tie / knot` effect), `27` (`opposing.py:239` `sustain_knot`) |
| k | **`2-ii`** RET-SC (kernel) | the 14-module kernel + `parliamentary_*` + the veto relocated as a forwarded `extension=` at `seam/ladder.py:164` (old `_part2:89-181`); `engine/tests/test_contest_kernel.py` retires; the prize rows repoint | BLOCKED | `28-iii` (`scene_dispatch` gone), `29b`, **`22`** (the prize-row repoint is `22`'s row change; Lens B on the veto only) |
| l | **`22`** PROC-B | the provider, by string; the composed obstacle + **ceiling** (the M-7 candidate, swept); `speak`'s four bands; the rows drop `interim: true`; the seam obstacle site deleted (`ED-SC-0033` cl. 3); proceedings steps 11–16 | BLOCKED | `18`, `★` |
| m | **`22a`** (proceedings PHASE 3, steps 17–21) → **`23`** PART-E-0/2 → **`22b`** (proceedings PHASE 4, steps 23–27) | `23`: typed ids with an owned `H`; the ONE loader's remaining invariants — invariant 4 (widened) and invariant 7, including F.20b's three body-literal Event kinds as declared columns | OPEN / BLOCKED | `22` (+ `15d` for `22a`; `17b` for `22b`'s `term`) |
| n | **`24g`** the bodies clock + P3 individuation | the retirement plan's ADJACENT S4 (narrative #5; `24` P2/P3) | BLOCKED | `24d-ii`, `24f`'s cohort producer, `ED-IN-0247`'s number (**JORDAN**, §5.1 item 8) |
| o | **`24h`** S5 — revolt (P5), forswearing (P6) | the revolt Query; the costs of forswearing | BLOCKED | `20-ii`; P7 (dispensation-as-document) is **JORDAN** (§5.1 item 11) |
| p | **`26`** GO-VERSION | record the ruled version; ED-1050's deferred re-export; then held H6 | **JORDAN** | the Godot version (§5.1 item 9) |

**a · `20-ii`, and contradiction 9.** This is where the season loop expresses the grand-strategy
scale, and so it is the gate every Step-B tree for that scale waits on. `faction_q` answers
`(proposition, members, holdings, seats)` per `04 §B.6.1:286-292`. It never makes a faction stat
vector a field of its own (`04:292`), and a seat *"adds no verb and no modifier"* (`04:334`).
`head` is `Tenure.degree`'s first reader, F.4. `scale_of_rung` is what `20-iv` consumes.

> **Contradiction 9 · `queries/` has three modules or four — RESOLVED: stale by design, until
> `20-ii`.** `04 §A.2:132` names three `queries/` modules. `faction_q.py` is a fourth, deliberately
> not written into `04` while it is partial (its docstring `:4-26`; layer-conformance B4, third
> disposition). **Edit `04 §A.2:132` at `20-ii`, when the fourth module is complete — not before.**
> Lens B reads that edit (§3.6).

**c · `28-ii` (M6).**

- **(1) The hash pin.** It succeeds `test_mc_v18_regression.py`'s seed-0 golden.
  `tests/valoria/test_m1_acceptance_probe.py` and `test_season_shape.py` already pin `content_hash`.
  Name whichever is the successor, or add one; which it is was not verified (§9).
- **(2) The battle.** A battle executing from a chooser-formed decision needs an `operands_for` `march`
  arm (H-151's citation). The precedent is the `kill / wound` per-verb typed-cell workaround
  (decision-layer plan §4.2); H-80's general fix stays unscheduled. `march` then leaves
  `test_season_shape.py:6996`'s never-attempted set. This succeeds `test_f7_smoke_oracle.py`'s
  `battles_mean`. That file's `VICTORY_THRESHOLD` dead-param tripwire dies with `DEFAULT_PARAMS`, and
  its Hafenmark-lockout claim closes under test 2.
- **`test_combat_bridge_seam.py` needs NO successor.** Its remaining `mc_v18` test asserts a flag-ON
  no-op on the OLD loop, and the flag dies with the file. Its shape tests are already carried by
  `seam/wrappers/combat.py:203-208`, `test_degree_ladder_single_owner.py` and
  `test_season_providers_are_registered.py`.
- **The retirement plan's own §6 gate binds here.** The successor artifacts must have RUN in the same
  PRs: a named same-seed hash pin, a two-arm balance comparison on the season harness (`28-i`), and a
  battle from a chooser-formed decision.

**d · `28-iii` SPINE-DELETE — what goes, in one commit (or a short serial run of them).**

1. **`engine/mc_v18.py` and `tests/valoria/test_mc_v18_is_deprecated.py`, together.** First reach
   `ALLOWED_IMPORTERS == set()` — that is the intermediate, falsifiable state.
2. **`engine/autoload/{engine_clock,season_manager,scene_slate,victory}.py`.**
3. **`engine/cross_scale/`, whole:** `scene_dispatch`, `combat_bridge`, `handoff_rules`,
   `zoom_in_out`, `__init__`.
4. **`systems/overview/sim/season.py`**, together with its `season_driver` role row.
   `export_composition --check` imports every target, so the row and the module go together.
5. **`game_state.py::{serialize_world,restore_world}`**, plus the ten `snapshot_state.*` roles, plus
   `test_engine_does_not_import_systems.py:523`'s guard.
6. **The role rows** `season_driver`, `faction_action`, `accounting`, `scene_builder.contest`,
   `scene_resolver.contest`, `contest_side.a/.b`.
7. **`module_contracts.yaml:1264-1298`'s `adapters:` block**, together with `test_wiring_validation.py`'s
   rule that *"adapters resolve to `engine/cross_scale/<name>.py`, 8/8"*. The rule retires with the
   block.
8. **`FORK:` rows for the test files** `engine/tests/{test_combat_bridge_seam,test_f7_smoke_oracle,test_mc_v18_regression,test_pipeline_reach,test_world_population}.py`
   and `tests/valoria/test_engine_clock_phases.py`. (`engine/tests/test_accounting_accord_drift_probe.py`
   survives to `29a`.)
9. **The `sim-regression` CI job re-scoped** (`valoria-ci.yml:361-397`).
10. **The text that names the spine:** `ci_checks_registry.yaml:374,388,390,396,398,480`,
    `tools/valoria_local.py:85-86` and `tools/m1_acceptance.py:13,64,138-198`.
11. **`/layer-conformance`, both lenses, at CLOSE** (§3.6).

⚠ **`game_state.py` itself STAYS until `29b`.** Its eight `systems/` importers would fail at import.

**The requirement behind `victory.py` does not die with it.** GD-1's sole-victory requirement needs a
registered hole: *"no season-side ending/victory condition; `ENDINGS_CLASSIFIED.yaml` +
`forced_by_threshold` are the ending vocabulary; `20-ii`'s observable '≥1 faction-scale ARC ends' is
its precondition"*. It is a gap to register, not a build item and not a question (§8.2).

**e · `20-iv`.**

- **d.1 on the season path.** `resolve_field`'s units take `morale_start` from season-native faction
  state. The candidate is §0 test 5: members' `commit`-Tenure `degree`, which is F.4's own reading and
  the same input `Faction.head` needs. It is attacked at the build, and if the attack lands it becomes
  the MB lane's Jordan item.
- **Terrain and garrison on the season path (H-150).** Build a rung→province map off `scale_of_rung`,
  plus `populated.py:287,330`'s settlement ids ↔ `valoria_geography_v30.yaml`. Then call
  `terrain_row_for_territory(tid, fort_level)` with `fortification_of`. H-150 closes here.
- **Nothing waits on `20-iv`.**

**f–j · Step B, per tree.** These are the hard serial edges, in import direction: overview → settlements
and world; factions → settlements; world → settlements. Each tree's contents and disposition are in
`_part2` §1.3; the points a builder must not miss are these.

- **`29a` overview.** `ms_track.py` waits on `27`, because `threadwork/sim/{co_movement:142, opposing:232}.py`
  lazily import `apply_ms_delta` and threadwork is retained by `ED-WR-0010`. The Accord / CI / MS /
  PT / insurgency CLOCKS have no season analogue, and by architecture none is wanted:
  `loop/census.py:33` says *"NO CLOCK GENERATES ANYTHING"* (ED-WR-0011 option A).
- **`29b` factions + `game_state.py`.**
  - The modules: the `systems/factions/sim/*` remainder — `faction_action`, `crown_initiative`,
    `tribunal`, `treaty`, `absolution`, `council_solmund`, `excommunication`, `mass_seizure`,
    `parliamentary_action`, `parliamentary_transfer` — plus `engine/autoload/game_state.py` (its last
    importers go here) and `MULTS/ACCORD_MAP/PT_MAP`.
  - The roles: `parliamentary_vote/motion/vote_declaration` and `world_gen_settlements` (a row;
    `create_world` dies).
  - `systems/social_contest/sim/parliamentary_{vote,stay}.py` — orphaned at this instant, they join
    `2-ii`'s set.
  - The descriptor faction block: `descriptor_registry.yaml`'s faction-stat block,
    `descriptors.FACTION_STATS/faction_bounds/assert_faction_roster_is_covered`, and
    `export_descriptors.py:245`'s faction validation. Once `Faction` is gone this is `ID-13`.
  - The tests go to `FORK:`, with their EDs closing under test 2: `test_parliamentary_action.py`,
    `test_faction_write_sweep.py` (`ED-FA-0038` — on the season side the one write mechanism is
    `World.write`), `test_faction_stat_bounds.py` (`ED-IN-0029`'s floors), `test_mass_seizure_accord_write.py`
    and `test_faction_obstacle_conventions.py`. `HANDOFF_FA`'s `score/2` row also closes; the ruling's
    live home is the season seam, H-127/`22` and PC Ob-from-defender.
  - `test_descriptors_runtime.py:100-110` and `test_world_initial_state.py:80-90` lose one test each.
  - `test_engine_does_not_import_systems.py:183-196,462`'s fixtures are re-pointed.
- **`29d` world.** `npe.py` → `decision/` + position `10`'s stance. `insurgency_pipeline.py` → `24h`'s
  P5 revolt Query. `test_conviction_roster_single_owner.py:52-55` is re-pointed, and MOD 4 closes.
- **`29c` settlements.** `.py` only. **`systems/settlements/valoria_geography_v30.yaml` STAYS** — it is
  A7's terrain source, read by the retained `systems/mass_battle/sim/terrain.py`. Moving it to
  `references/` is a consideration, per the `world_initial_state.yaml` precedent.
  `test_settlement_temperament_drift.py` goes to `FORK:`. `ED-SE-0052`'s `fort_level`/`facility_tier`
  readers move to `Site.condition` and `fortification_of`.
- **`29f` then `29e`.** On the season side a `knot` Tenure kind exists (`epistemic.py:204`
  `firsthand_via_knot`). ED-912's ±5 gauge has no carrier, so it maps to `Tenure.degree`; that is
  recorded on `14`, not invented. `test_knots_ed912.py` goes to `FORK:`. Then `conviction.py`
  (← `knots.py:349`) and `beliefs.py`, which is orphaned after `28-iii` and may go at a `28-0`
  follow-up.

**l · `22` PROC-B, and contradiction 3.**

> **Contradiction 3 · the M-7 obstacle remedy — RESOLVED to the ratified plan's side (old
> `_part2:1492-1501`): the candidate is the CEILING, its value injected and swept, attacked at `22`'s
> build.** Not Jordan.
>
> - **The disposition is already on record.** Old `_part2` position 22 disposes of it under §0 test 5,
>   with reasoning: *"a ceiling caps how hard a matter can get; a pool floor raises every participant's
>   competence — a statement about people rather than matters."*
> - **That disposition was ratified.** The 2026-09-25 amendment (`ED-IN-0270`) ratified the old §5's
>   discipline: candidates ratify *"only as which ladder step answers each question, and which
>   candidate gets attacked — never as the answer"* (old plan `:12`). The same entry names what a
>   different preference would displace: *"If Jordan prefers the floor, that is a §5 item and it
>   displaces this clause only."*
> - **Why `HANDOFF_SC.md`'s "genuine open call" does not reopen it.** That handoff row is a pointer
>   index that predates the ratified disposition. The evidence it cites —
>   `13_PARLIAMENT_FOLD_AND_RECALIBRATION.md`'s bounded-δσ evidence *"for moving bench reception out of
>   the obstacle"* — is an **input to the attack** at `22`. It argues for a composition change that is
>   compatible with a ceiling, not for a pool floor.
> - **`21_RECONCILIATION.md` step 14's "remedy undecided" is superseded** by `ED-IN-0270` (§0 test 1:
>   later, and ratified).
> - **Record edit, made in this commit (§8.1):** `HANDOFF_SC.md`'s row is re-pointed to old `_part2`
>   position 22. The M-7 falsifier stays as written there: *"M-7 re-run at the floor must clear Ob ≥ 4
>   after the ceiling."*

`ED-SC-0038` (two of Jordan's 2026-09-04 rulings binding all twelve proceeding rows) is RULED
(`needs_jordan: false`, 2026-09-26). Its per-matter / single-margin pick is `22`'s **build decision**,
not a question.

**m · `23`.** `valoria-ci.yml` runs no type-checker (no mypy or pyright; verified), so the runtime
grade is the real one (old `_part2:1519-1521`). The old §7 item 4 still governs the scheduling of PART E
steps 0 and 2: a departure from the spine, held back.

### 3.5 · HARD SERIAL EDGES ADDED BY THIS PASS — beyond the 2026-09-18 plan's `§3.9`

Each edge is a shared file, a shared row, or a produced-then-consumed symbol. `isolation: worktree`
defers these to the merge; it does not remove them.

1. **`28-iii` → `29a` → `29b` → `29d` → `29c`.** This is the import direction: overview imports
   settlements and world; factions imports settlements; world imports settlements.
2. **`27` → `ms_track` (`29a`)**, and **`27` → `knots` (`29f`)**.
3. **`14` → `29f` → `29e`.** The `tie / knot` effect comes first; then `conviction.py` ← `knots.py:349`.
4. **`29b` → `2-ii`** (the `parliamentary_*` modules), and **`22` → `2-ii`** (the prize-row repoint).
5. **`FIGHT-RENAME` → `8`.** One row, one wrapper.
6. **GATE-REMOVE-PERSON ↔ `24f`.** Both edit `loop/matter.py`, so they run serially, in either order.
7. **`20-ii` → `20-iv`.** Nothing waits on `20-iv`; H-150 closes there.
8. **`13d-i` item (5) → `18a`** (§2.3's author placement).

### 3.6 · Where `/layer-conformance` has NEW subject matter

The skill's own description says it is *"Run by /close step 4"*, so it already runs at every CLOSE of
the §3.0 cadence. At these positions Lens B has new subject matter, so its output must be **read**, not
just passed:

| position | Lens B's new subject |
|---|---|
| `28-iii` | `04 §A.2`'s module table, §C.5's routes, `04:679-684`; `ID-13` over the deleted registry rows |
| each `29x` | `ID-13`'s consequences: the descriptor faction block, the re-pointed fixtures |
| `20-ii` | §B.6.1's NEVER list; the `04 §A.2:132` edit (contradiction 9) |
| `2-ii` | the veto relocation only (old `_part2:171-172`) |
| `22` | the provider returns a Margin, never a winner; the obstacle has a single owner |
| `23` | the invariants |

**Lens A (placement) matters most at `28-0` and `28-iii`**, for their `FORK:` rows and registry edits.
The full Layer-1 mapping — every open ARMATURE §2.3 node through the five-step test — is `_part2` §2.

### 3.7 · The 2026-09-18 plan's §6 gaps — what each became

| its §6 gap | now |
|---|---|
| PART E step 12 (parallel DELIBERATE map) and D-41a's permutation falsifier | **unchanged** — beside the critical path; no R-row moves on them |
| the FA lane beyond OLD-DRIVER | **positioned**: `20-ii` expresses the scale; `29b` retires `systems/factions/` |
| proceedings PHASE 1/3/4 | **positioned**: step 1 → `16`; steps 4(a)/(b) → `15d`; PHASE 3 → `22a`; PHASE 4 → `22b` (step 22 → `17b`) |
| any GDScript grade | **unchanged** — no position targets GDScript before `26` |
| the 143-case count has no single owner | **unchanged** — position `13` uses the harness loader's count |
| `tools/m1_acceptance.py` rows 1 and 4 | **unchanged** as a gap; the registry's stale description of rows 1–2 is corrected in this commit (§8.1) |
| `2026-08-15-character-and-faction-stats-and-progression.md`, ownership unresolved | **unchanged**; §5.1 item 10 is its one live question |
| no content owner for `13e`, `13f` or `24f` beyond the plan | `13e`/`13f` are DONE; `24f` still has only the old `_part2` entry — and Phase 1 item 10 is its design step |
| no instrument runs the populated realm for `★` | **positioned** as `★`'s first step |
| `19`'s `determine` has no `judging_set` until `18` | `18` is Phase 1 item 9 |
| `★`'s claims/questions figures are 2026-09-17 values | **unchanged** — re-run them, do not re-cite them |
| the birth-side consumer of `capacity` | **unchanged** — no position here builds one |
| a producer of synecdoche cohorts | **positioned**: naming it is Phase 1 item 10's deliverable |

---

## 4. THE NINE CONTRADICTIONS — where each is resolved

ARMATURE §1.2 lists nine places where two live surfaces disagreed. Each is resolved to ONE side. Where
the resolution bears on a position, its full reasoning is written at that position; this table is
only the index. None of the nine went to Jordan.

| # | subject | resolved to | ladder step | full reasoning at |
|---|---|---|---|---|
| 1 | `Office.upkeep` | off `18a`'s list; its reader at the new `17b` | 3 (Layer 1 `Seat :=`; r2 `05:1659`; F.18) | §3.2, after the table |
| 2 | C1–C4 "derive, no code change" | the 2026-09-18 plan's §3.5 (narrowed) + the decision-layer plan's H6 | 1 (measured, later) | §3.3, after the table |
| 3 | the M-7 remedy | the obstacle CEILING, swept, attacked at `22` | 5, as ratified by `ED-IN-0270` | §3.4 l |
| 4 | the `kill / wound` rename | rename standalone NOW to `fight`; the SPLIT rides the cells commit | 1 (Jordan 09-27 is later) + 3 (the ruled name) | §3.1 item 5 |
| 5 | `HANDOFF_IN.md`'s M4 row | a record edit — `ecacb57` seeded the garrisons and ran all four reviews | — (a stale fact) | §1; edited in §8.1 |
| 6 | the count of contested verbs | a record edit — 3 of 39; the mass-battle seam exists | — (a stale fact) | edited in §8.1 |
| 7 | proceedings step numbering | a record edit — `21_RECONCILIATION.md` PHASE 1's numbering | — (a stale fact) | edited in §8.1 |
| 8 | `ED-IN-0251` row 2's field against its text | a NEW `ED-IN-0261` row carrying `needs_jordan: true` | 5 | §3.1 item 1; landed in §8.1 |
| 9 | `queries/` — three modules or four | stale by design; `04 §A.2:132` is edited at `20-ii` | 3 (`faction_q.py:4-26`) | §3.4 a |

---

## 5. THE JORDAN ROSTER — ⚠ OPEN, EACH ONE HIS; NOTHING HERE IS RATIFIED BY THIS DOCUMENT LANDING

**Read this section as the open questions it is.** The ORDER above is adopted on Jordan's
instruction. **None of the thirteen items below is**: each survived all five of `CLAUDE.md` §0's tests
and waits on his individual answer. A merge of this document ratifies none of them (§7). Where a
position waits on one, its `GATE` column says **JORDAN** and names the item number here.

### 5.1 · Survives all five tests — put to Jordan

Each item gives the question, why the ladder does not answer it, what it blocks, and where its ledger
record is.

1. **C1 · the 105 cells, plus the alignment re-cell over 43 verbs** (G-Q1; the 2026-09-18 plan's §5
   item 11). ⚠ **The count is corrected by the author.** The decision-layer plan's *"42"* (its `:697`)
   is 38 − `kill / wound` + `kill`, `wound`, `fight`, `challenge`, `accept`, computed before `march`
   became the 39th verb (`ecacb57`). On today's table the same arithmetic gives 43.
   - *Why it is his:* it is content nobody can derive. R3 already says *"the cells are yours"*.
   - *Include the faith-pair placement* (decision-layer plan §5, Q1 note; `HANDOFF_IN.md`'s cells row).
     The draft fails Jordan's own falsifier at the registry's .60 clergy weight.
   - *Blocks:* `12b`/`12c`/`12d`, `12`, `14`, H3–H11, and arming H-146.
   - *Ledger:* **`ED-IN-0261`'s new row (2026-09-28, this commit).**
2. **C2 · the per-character and role-template migration to the fifteen** (G-Q2).
   - *Why it is his, and why it must arrive WITH C1:* `cast.py:203-211` raises, and `to_axes` fails
     silently. Four true orphans remain — `Utility`, `Equity`, `Identity`, `Precedent`.
   - *Blocks:* the cells commit, jointly with C1.
   - *Ledger:* `ED-IN-0261` (same row).
3. **C3 · the affiliation roster, the ten `incompatible:` cells, and intensity** (G-Q3).
   - *Why it is his:* it is content.
   - *Blocks:* H10 (`12b`'s plumbing).
   - *Ledger:* `ED-IN-0261` (same row, as a sibling).
4. **C4 · verb × affiliation engagement** (G-Q4).
   - *Why it is his:* no table exists; it is content.
   - *Blocks:* H11.
   - *Ledger:* `ED-IN-0261` (same row, as a sibling).
5. **G-Q6 · crisis threshold 3's terminal branch** — restabilise, fold or destroyed; per case, or
   fixed?
   - *Why it is his:* the only non-quarantined source is silent. `.designs/conviction_track_v1.md` may
     answer it, but only by Jordan's own reading — quarantined prose is not authority.
   - *Blocks:* H13 (`12e`) only.
   - *Ledger:* named as a narrower sibling on `ED-IN-0261`'s new row.
6. **`ED-IN-0210` · is `comply` one verb or two** (the 2026-09-18 plan's §5 item 2).
   - *Why it is his:* two defensible verb grammars lead to materially different games, and the old
     plan's §7 item 5 affirms the question is genuinely his.
   - *Blocks:* `19b`.
   - *Ledger:* `ED-IN-0210` (keeps `needs_jordan` deliberately; close-pass skips it by name).
7. **Position `9` · build or strike §11.4 Surrender / Disengage** (the old §5 item 12; `ED-PC-0056`).
   - *Why it is his:* a surrender mechanic, or none, changes what a duel can end in (F.12).
   - *Blocks:* `9` only.
   - The PC id-block reservation is administrative (Lane B's file procedure), not part of the question.
8. **`ED-IN-0247` · the `body_step` value** (the old §5 item 13).
   - *Why it is his:* it is a balance number, and it is asked only after `24f` has settled the carrier.
     A value chosen for the wrong carrier is worse than none.
   - *Blocks:* `24g`'s live arm.
   - *Ledger:* `ED-IN-0247` (`needs_jordan: true`).
9. **The Godot version** (the old §5 item 5).
   - *Why it is his:* `CLAUDE.md` forbids settling it by editing a document.
   - *Blocks:* `26`.
10. **D2 · the tenth attribute** (the old §5 item 7).
    - *Why it is his:* it is registry content for Godot binding. It is inert for `engine/season`.
    - *Rides:* `26`.
11. **S5-P7 · overturn the written refusal of dispensation-as-document** (`verb_table.yaml`'s `comply`
    typed cell; the-gather `02_SETTLEMENTS.md:20`).
    - *Why it is his:* *"the answer would overwrite ratified canon"* — §0's own escalation clause.
    - *Blocks:* `24h`'s third item only. Not urgent.
12. **Narrative #6 · complication as the modal outcome.**
    - *Why it is his:* it re-bands the ONE degree ladder (`dice_engine.degree_from_net`; `CLAUDE.md`
      §5; T-k). That moves every scale and overwrites a ratified shape.
    - *Blocks:* nothing.
13. **MB-lane rows the lane flagged, NOT re-tested in this pass.**
    - The rows: `ED-MB-0039` (A)/(B) geometry; `ED-MB-0041`'s depth cap / graded cavalry refusal /
      Command σ-ceiling / yield split; `ED-MB-0045`'s CEV naming and 2:1 targets; `ED-PC-0016`;
      `ED-PC-0047`/`0049`–`0055`.
    - Fable did not open them. **The lane owner runs the five-step test before they reach Jordan** —
      the old §5's discipline.
    - *Blocks:* no position in this sequence.

### 5.2 · DEMOTED — answered, with the closing citation close-pass writes. Do NOT let these ride back into §5.1

**Why this list matters as much as the one above.** The 2026-09-18 plan's §2.2 named the queue's
pathology: *"it is large because closures were never written down, not because the questions are
hard."* Each row below was answered in this pass. Recording the answer is what stops a later session
from re-litigating it. Each row ratifies only as *which ladder step answers it, and which candidate
gets attacked* — the answer itself is decided at its position (§7).

| question | answered by | the answer, or where it is decided |
|---|---|---|
| the old §5 item 0 — the undeclared content-hash tiebreak | test 4 | precedent `H-54`/`H-122`; positions 3–7 landed on hash controls. The plan itself posed it conditionally |
| the old §5 item 4 — the MB golden (A/B) | test 1 | `ED-MB-0016`'s governing row is `needs_jordan: false` (2026-09-15); position `25` is OPEN |
| the old §5 item 8 — held H5, the ladder divergence | test 1 | the hold IS Jordan's 2026-08-14 ruling, and the owner is named (T-k; `dice_engine.degree_from_net`). Nothing to ask until a PC position touches it |
| the old §5 item 9 — `H-111`, refusal as news | test 5 (candidate) | Already mechanism: refusals EMIT (`emits_on_refusal`) and WITNESS fans out Events. **One probe** confirms whether any channel predicate filters refusal kinds; if one does, that filter is the recorded prior answer (§9) |
| **`ED-MB-0075`** — C2/C3 check-form (`needs_jordan: true`, 2026-09-27) | tests 4 + 5 | Part D eliminates option (1) on Jordan's own wording (*"checked against Discipline"* is a check), and option (3) on sibling consistency (every check in the module is binary). That leaves **(2), roll-gated via `discipline_check_cascade`, unmodified**. Write the superseding row, build (2) in the MB pass, and have an antagonist attack the "passive denominator" reading |
| `mass_battle`'s `state: []` (`HANDOFF_MB.md`) | test 3 | `04 §C.5.1`: a provider returns a Margin and owns no world state, so `[]` is correct. **Closed** — handoff row edited in §8.1 |
| **G-Q5** — `Person.precedence` | test 5 | The decision-layer plan §2.1 measured the precedence band as a no-op: 28/28/1, and three of six tests fire zero times. A fork whose arms are indistinguishable on the measured world is not a live choice (the old §5 item 0's logic). Candidate: *"neither"* (the shipped state). H12 is held on a **post-H6 re-measure**, not on Jordan; if the re-measure shows the tests would fire, the question comes back through the ladder |
| M-7; `Office.upkeep`; `kill / wound` | tests 5 / 3 / 1+3 | contradictions 3, 1 and 4 (§4) |
| `13d-i` item (5) — the fate of `titles` | test 3 | Layer 1 §B.7 (`04:308`, *"no `Title` type"*) + §E.1 (`04:1067`, world-gen content) → it folds into `offices.yaml` (`_part2` §2, MOD 5) |
| d.1 on the season path | test 5 (candidate) | members' `commit`-Tenure `degree`, attacked at `20-iv` |
| `HANDOFF_IN.md`'s `test_n3` floors | test 5 | a declared re-pin per `CLAUDE.md` §7, unless U6 (`11`) shows the floor is an R-01/R-02 property |
| D-6/D-7 — the `speech_kinds` defaults | test 5 | swept fixtures in the `H-128` shape, at `18`. **`ED-SC-0038` is RULED** (`needs_jordan: false`, 2026-09-26); the per-matter / single-margin pick is `22`'s build decision |
| deleting the retire set | not a question | `requirements.yaml:27-31`'s gate is honoured per tree (§3.4; `_part2` §1.3). Jordan's 2026-09-28 instruction is consistent with it: supersede the CALLS, meaning subsume the scales |
| `docket` / `victory` GD-1 | not a question | a registered gap (§3.4 d; §8.2) |

---

## 6. THE END-STATE — what is true when `28`, `29` and `2-ii` complete

- **`engine/mc_v18.py` is deleted, with a `FORK:` row.** `tests/valoria/test_mc_v18_is_deprecated.py`
  is deleted in the same commit, after passing `ALLOWED_IMPORTERS == set()` as the intermediate,
  falsifiable state.
- **`references/module_contracts.yaml` `composition_roles:` holds exactly ONE row,
  `mass_battle.resolve_field`**, consumed by `engine/season/seam/wrappers/mass_battle.py`. The other 26
  are deleted: 20 spine-only, 3 orphaned, 3 `parliamentary_*`. `engine/engine_params/composition.json`
  is regenerated behind `export_composition --check`. The `adapters:` block and its wiring rule are
  retired.
- **`engine/autoload/` is `{__init__, dice_engine, sigma_leverage}`** — the substrate.
  `engine/cross_scale/` is gone. `engine/substrate/` is unchanged: `canon_buckets`,
  `world_initial_state`, `pc_engine`, `composition`, `descriptors` (minus the faction-stat roster),
  `stubwire`, `names`.
- **`systems/{overview, factions, world, characters, fieldwork}/` are gone, with `FORK:` rows.**
  - `systems/settlements/` is reduced to `valoria_geography_v30.yaml`, or that file moves to
    `references/`.
  - `systems/social_contest/` is gone (`2-ii`), and its prize rows are repointed to the proceedings
    provider.
  - `systems/threadwork/` is retained (`27`).
  - `systems/mass_battle/` and `systems/combat/` are retained. `massbattle.py`'s
    `resolve_mass_battle`/`_faction_to_unit` are deleted, and d.1 lives on `resolve_field`.
- **Zero production imports of any spine module** — §1's AST scan returns the empty set.
  `test_engine_does_not_import_systems.py` is still green at `BASELINE_TOTAL = 0`, with
  `PATH_SEAM_ALLOWED = {'substrate/pc_engine.py'}` and its fixtures re-pointed.
- **Zero mentions of `mc_v18`** outside the fork ledger, `CLAUDE_RATIONALE.md` and `registers/archive/`.
  The text of `tools/m1_acceptance.py`, `ci_checks_registry.yaml` and `tools/valoria_local.py` is
  updated, and `references/execution_map.json` / `EXECUTION_MAP.md` are gone.
- **`engine/tests/` is reduced to `test_sigma_leverage_parity.py` + `test_thread_mending_ed871.py`**
  (plus `test_contest_kernel.py` until `2-ii`, and `test_knots_ed912.py` until `29f`). The
  `sim-regression` CI job is folded into `unit-tests`. `test_sigma_leverage_parity.py` is substrate;
  it moves out of `engine/tests` when the job folds.
- **`requirements.yaml:27-31,60-63` are rewritten:** Step B executed. Every scale row reads either
  `in_loop: true`, with its position, or (grid combat) *"unbuilt design, no work item"* as today.
- **The successor artifacts have RUN, in the same PRs** (the retirement plan's §6 gate): a named
  same-seed hash pin, a two-arm balance comparison on the season harness, and a battle from a
  chooser-formed decision.

---

## 7. HELD BACK FROM RATIFICATION-ON-MERGE (`CLAUDE.md` §2, ED-1094)

A merge of this document ratifies **§3's ORDER and §2's supersession verdict**, and nothing else.
These are explicitly held back:

1. ⚠ **§5.1's thirteen items are OPEN.** Each is Jordan's to answer individually. No position that
   waits on one becomes buildable because this document merged. Where a row's `GATE` reads
   **JORDAN**, it stays so until he answers.
2. **The queue closures are NOT applied.** The 2026-09-18 plan's §2.1 closures and §5.2's are position
   1's commit, because each asserts a question is dead. The two ledger rows that land with this
   document are the adoption record (`ED-IN-0281`) and an escalation (`ED-IN-0261`'s new row). Neither
   is a closure.
3. **§5.2's demotions ratify only as *which ladder step answers the question, and which candidate gets
   attacked*.** Each answer is decided at its position, with the code in front of it. An attack that
   lands sends the question back through the ladder, not to Jordan by default.
4. **Two CONTENT placements are made by a document that owns only ORDER**, the shape the 2026-09-18
   plan's §7 item 6 held back for itself.
   - **`15d`** takes proceedings PHASE 1 step 4 (a)/(b) out of `21_RECONCILIATION.md`'s sequence and
     into the IN chain after `15b`.
   - **`17b`** composes `Office.upkeep`'s reader with `Tenure.term`. Those come from the retirement
     plan's ADJACENT G2 and proceedings PHASE 4 step 22.

   If either content owner disputes its placement, that position reverts and nothing else in the order
   moves.
5. **The 2026-09-18 plan's §7 items 4–6 still stand**: PART E steps 0 and 2 scheduled at `23`; `19b`
   conditional on `ED-IN-0210`; the `cast:` reader at `13`. Its item 3, the Arc-2 re-cut, is spent,
   because G1a–G4 are DONE.
6. **No `## Status:` line moves on an absorbed document.** The retirement plan, the decision-layer plan,
   the squad-engagement synthesis and `21_RECONCILIATION.md` keep their headers. This document
   supersedes their ORDER claims, and their content stays theirs. The one header edited is the
   2026-09-18 plan's: a forwarding note under its status line, which is left in place.

---

## 8. RECORD EDITS

### 8.1 · Made in this commit — stale facts, not design calls

| file | what changed |
|---|---|
| `references/id_reservations.yaml` | IN `next_free` 280 → 281 (`ED-IN-0281` allocated to this document's adoption) |
| `registers/editorial_ledger_in.jsonl` | `ED-IN-0281` (the adoption record); `ED-IN-0261`'s new row (`needs_jordan: true`, C1 + C2 with C3/C4 and G-Q6 as siblings). ⚠ **`ED-IN-0261`'s one earlier row was moved from `editorial_ledger_in_archive.jsonl` to the live ledger, byte-identical, ahead of the new row.** `tests/valoria/test_ledger_hygiene.py::test_no_ed_has_rows_split_between_a_live_ledger_and_its_archive` forbids an id split across the pair, and an id whose last row is non-terminal belongs in the live ledger |
| `CURRENT.md` | "The plan" row → this document, `ED-IN-0281`; it notes that this supersedes the 2026-09-18 plan, whose `_part2` stays the content owner |
| `workplans/2026-09-18-governance-settlement-behaviour-plan.md` | a forwarding note under its `## Status:` line (the line itself is untouched), in the shape of `workplans/2026-09-11-arc-sequence-spine.md`'s *"SUPERSEDED AS AN ORDER"* header |
| `registers/handoffs/HANDOFF_IN.md` | the relocation row: `site_kinds` has carried `dwelling` since `ED-IN-0274`. The M4 row: garrisons seeded and all four reviews run (`ecacb57`; contradiction 5). The kill/wound "same-day conflict" row: **struck as resolved** (contradiction 4). The standing order: narrowed to *"the SPLIT rides the cells commit"* |
| `registers/handoffs/HANDOFF_SC.md` | the proceedings row: re-numbered to `21_RECONCILIATION.md` PHASE 1 (contradiction 7). The retirement row: the carve-out expires at `29b`. The M-7 row: re-pointed to old `_part2` position 22 (contradiction 3). The `ED-SC-0038` row: RULED; the pick is `22`'s |
| `registers/handoffs/HANDOFF_MB.md` | the `state: []` row: closed by `04 §C.5.1` |
| `engine/season/requirements.yaml` | the social-contest scale note: 3 of 39 verbs declare `contests:`, and none reaches this kernel. The mass-battle scale row: the seam exists (`ecacb57`) and no chosen act reaches it yet (contradiction 6). **Its `in_loop:` value was edited too**, because it read *"seam unbuilt"* beside a note saying the seam exists. No tool reads `in_loop` |
| `references/ci_checks_registry.yaml` | `tools/m1_acceptance.py`'s `role:`: rows 1–2 probe `engine/season/`, not `mc_v18` (false since `ED-IN-0226`) |

### 8.2 · Owed, and NOT made here — outside this commit's declared scope

- **`HANDOFF.md:18`** — *"the ordered work — start here"* still points at the 2026-09-18 plan's §3.1.
  It should point here, at §3.1.
- **`proposals/2026-09-27-mc-v18-retirement-plan/PROPOSAL.md` §1 `:31`** — *"39 production files"*
  should read 12 by AST (§1).
- **`proposals/2026-09-28-repository-armature/ARMATURE.md` §2.5** — *"16 of 17"* should read 20 of 27.
  The armature's own rule is to delete it rather than update it piecemeal once it misleads (its
  `:9-11`).
- **`engine/season/hole_register.yaml`** — an `ABSENT_RULE` hole for GD-1's season-side ending
  condition (§3.4 d).
- **The documents that name the 2026-09-18 plan as *"the ORDER"***: `workplans/valoria_master_workplan_v7.md:18,53`,
  `workplans/2026-09-11-arc-sequence-spine.md:4`, `workplans/2026-09-13-work-order.md:3`,
  `registers/handoffs/HANDOFF_WR.md:8` and `HANDOFF_SE.md:8-9`. The forwarding note catches a reader
  who follows them.
- **`proposals/2026-09-26-decision-layer-execution-plan/candidate_pursuit_cells.md:46`** cites
  `registers/editorial_ledger_in_archive.jsonl:177` for `ED-IN-0261`. Moving that row (§8.1) makes the
  line number stale; the id still resolves.

### 8.3 · Made at position `1`'s execution — a later commit than §8.1's, same day

Position `1` (CLOSE-PASS) shipped its instrument (`tools/fold_ledger_to_latest.py`,
`ci_common.fold_ledger_to_latest`) and used it before touching any row — §0.1 pt 3's discipline,
not trusting the ten-day-old §2.1 table by eye. **The measurement corrects §2.1 itself, and the
correction belongs here, not there:** the old plan's `_part2` §8 position 1 stays its content
owner, and this table records what changed the facts underneath it since it was written.

- **§2.1's own table was stale the day it was compiled.** Its ~97 "closable" rows were measured
  2026-09-11. An internal pass the ledger itself labels **`ED-IN-0215 position 1`**, dated the same
  day, had already closed the overwhelming majority of them — the same document's own earlier
  execution of its own position 1, a day before that document's stated ratification
  (`workplans/2026-09-13-work-order.md:176`, `## Status: RATIFIED 2026-09-12`), not a separate plan
  generation. §2.1's compiler never reconciled against it. A second, independent instance of the
  same pattern: the old plan's own §5 item 1 cites `ED-IN-0214`'s row as "still reads `status: open`
  / `needs_jordan: true`" — true of the row at
  `registers/archive/editorial_ledger_in_archive_pre-2026-09.yaml:2504`, but that file holds a
  SECOND, later `ED-IN-0214` row at `:3678` (dated 2026-09-15, `status: ruled`,
  `needs_jordan: false`) the old plan's own citation never checked for. By the append-only
  convention both plans state (`CLAUDE.md` §1: "an id's LAST row is its current state"), `:3678`
  governs: `ED-IN-0214` was already closed before either plan's §5 was written.
- **§2.1's "13 not found" ids are not 13 unresolved citations.** All 13 resolve. Twelve
  (`ED-IN-0030/0042/0049/0050/0086/0092/0123/0124/0148/0158/0159/0195`) are already terminal in
  `registers/archive/editorial_ledger_in_archive_pre-2026-09.yaml` — the frozen, pre-migration
  corpus `ci_common.editorial_ledger_paths()` does not scan, so they read as "not found," not as
  "still open," to the new instrument (nine via a 2026-09-15 superseding row; three were already
  `status: closed` at their original 2026-07/08 row, predating §2.1 entirely). The thirteenth,
  cited as `ED-FA-0013c`, is a citation typo for **`ED-FA-0013`** (`registers/editorial_ledger_fa_archive.jsonl:12`)
  — a live, in-scope, already-`status: superseded` row (2026-09-11, the same `ED-IN-0215 position 1`
  pass). ⚠ **Corrected by a Phase-3 terminal critique:** it is NOT "findable by the same fragment
  search this position's own instrument supports" — the shipped `--id` flag is an exact-id lookup
  only and does not accept a fragment. The typo was caught by a manual, ad-hoc search run during
  this session's own investigation, not by a feature of the instrument as shipped.
- **The instrument's OWN first cut manufactured a fifth disagreeing figure, and a Phase-3 terminal
  critique caught it before this landed.** `needs_jordan: true ∧ status: open`, old plan position
  1's literal OBSERVABLE predicate, folds to **0** — the ≤ 12 acceptance line is met. But reporting
  that alone as "the queue" is false: `ED-IN-0210` (`status: ruled`), `ED-IN-0261` (`status:
  partial`) and `ED-IN-0247` (`status: resolved`) all carry `needs_jordan: true` in their current
  row and are all independently named, elsewhere in THIS document, as still Jordan's to answer —
  §5.1 items 6, 1–5 and 8 respectively. `needs_jordan: true` at ANY status, folded, is **41** —
  overwhelmingly historical rows where the flag was never cleared after the row's own resolution
  (a `resolved`/`ratified`/`executed` status with a lingering `needs_jordan: true` is bookkeeping
  noise, not a live question; §5.1's own thirteen-item roster is the curated, ratified list of what
  is actually still open). Neither raw count IS "the queue" on its own; `tools/fold_ledger_to_latest.py
  --queue` now prints both, and §5.1 is the answer to "what does Jordan still owe."
- **Net: this position's only ledger edit is the one row §5.2 already named**, `ED-MB-0075`
  (appended to `registers/editorial_ledger_mb.jsonl`, `needs_jordan: false`, `status` stays `open`
  — the design fork is settled, the build is `25`'s). The narrow OBSERVABLE predicate goes
  **1 → 0**, meeting the ≤ 12 line old plan position 1 set; §5.1's roster is untouched by this
  commit and remains open, exactly as its own header says it must.
- **Ride-along, confirmed moot rather than silently skipped:** old plan `_part2` §8 position 1's
  second ride-along, "strike `HANDOFF.md:463-469`'s 'THE STEP TO TAKE: S7'", has no live target —
  root `HANDOFF.md` is 61 lines today, a pure pointer index with no such text anywhere (grepped).
  An earlier, unrelated rewrite already removed it. Nothing to strike.

### 8.4 · Made at position `2`'s execution — narrowing `28-0` before deleting anything

Before running any `git rm`, §0.1 pt 3's discipline again: verify "zero importers" rather than trust
it, this time by grepping each of the thirteen-plus targets for every caller, not only literal
`import` statements. **The `ast` scan the brief cites cannot see a dynamic, string-keyed caller**,
and `engine/tests/test_pipeline_reach.py` (kept live and in scope until `28-iii`, §3.4) is exactly
that: its `_OI17_FULL_MODULE_ENTRYPOINTS` list (`:276-290`) holds
`(module_path, func_name, args_fn)` tuples that `test_oi17_full_module_conversions_are_stub_wired`
(`:293-305`) probes at runtime via `importlib`, never a source-level `import`.

- **Twelve of this position's fourteen module targets are OI-17 entrypoints, invisible to the
  brief's own justification for calling them zero-importer.** `engine/autoload/npc_ai.py`,
  `systems/overview/sim/{rs_track,ip_track}.py`, all six FA stubs,
  `systems/world/sim/{miraculous_event,restoration_movement}.py` and
  `systems/characters/sim/companion.py` are named, by full dotted path, in that list today.
  Deleting any of them before `28-iii` retires that test would turn a currently-green
  `sim-regression` job red for a deletion this plan's own §3.4 already schedules later, for no
  reason to do it sooner. Only `engine/cross_scale/domain_echo.py` and
  `systems/fieldwork/sim/{fieldwork,investigation}.py` are absent from that list — confirmed by
  grep, not assumed — and only those three modules are executed in this commit.
- **The two `scene_resolver.*` roles and their stub branch are a self-contained unit, checked
  independently.** `references/module_contracts.yaml:194-199`'s `needed_by:` field for both named
  only `engine/cross_scale/scene_dispatch.py`'s `st in ("fieldwork", "investigation")` branch,
  and a grep of `run_fieldwork_scene`/`resolve_npe_response` tree-wide turned up only their own
  definition sites — no second caller. Deleting the branch drops those two scene_types into the
  same file's existing total-mapping `else` (`:361-372`), which sets `out["stub"] = True` the same
  way the deleted branch did, so `test_scene_type_total_mapping_resolves_or_stub_flags`
  (`engine/tests/test_pipeline_reach.py:168-201`) is unaffected — verified by running it, not
  inferred. `ED-916` ("Zero continuous-engine validation at fieldwork parameters") is superseded
  in `registers/editorial_ledger.jsonl` on that basis (§0 test 2: its subject is gone).
- **`territory_transfer_candidate`/`territory_transfer_proposal` were never orphaned in the sense
  this position's list implies, and the registry says so in the same file the brief read.**
  `references/module_contracts.yaml:110-115` (immediately above the `territory_transfer_candidate`
  row) already carries a reasoned ruling to KEEP both rows — the target module
  (`systems/factions/sim/parliamentary_transfer.py`) is permanent, its functions resolve,
  `tools/export_composition.py` imports them at export time, and "giving it a driver is a design
  call nobody has taken." Nothing in this session's execution, or in `28-iii`, changes that
  reasoning. §0's five-step test resolves this at step 3 (answered by a design document — the
  registry entry itself) without going to Jordan: the rows are removed from this position's scope
  entirely, not deferred.
- **`rs_track_delta` carries the identical "kept, not orphaned" ruling** at
  `references/module_contracts.yaml:200-203`, *and* its target module (`rs_track.py`) is itself an
  OI-17 entrypoint. Both reasons block it today; only the second is time-gated (`28-iii`), so this
  role's fate is coupled to its module's, not to the other two roles' — noted so a future session
  does not delete it the moment `rs_track.py` goes without re-checking whether the standing "kept"
  ruling still applies at that point.
- **Verified, not asserted:** `python -m pytest tests/valoria/test_engine_does_not_import_systems.py
  engine/tests/test_pipeline_reach.py -q` — 24 passed, after the three deletions, the
  `scene_dispatch.py` branch removal, the two registry role rows removed, the now-orphaned
  `domain_echo` adapter/wiring rows removed from `references/module_contracts.yaml`, and
  `tools/export_composition.py` re-run clean.
- **Net: this position ships 3 of its originally-listed ~15 targets.** Twelve wait on `28-iii`
  (a scheduling correction, not a design one); two (`territory_transfer_*`) are removed from this
  position's scope on a standing ruling already on record. Nothing here needed Jordan.

---

## 9. NOT VERIFIED IN THIS PASS

Carried forward honestly, not resolved here.

- The MB/PC `needs_jordan` rows in §5.1 item 13 — not opened.
- Whether any WITNESS channel predicate filters refusal kinds (§5.2, `H-111`) — one probe.
- Which existing test is the named same-seed hash pin (`28-ii` (1)).
- `tests/valoria/conftest.py`'s and `test_flow_skeletons.py`'s exact dependence on
  `execution_map.json` (`28-i`).
- RR-P's text for the AX-7 wiring's third function (`belief_contradicts`), given that `Person.beliefs`
  is deleted (`10`).
- `ED-916`'s full row — only its head was read (*"fieldwork.py + investigation.py are
  NotImplemented"*), which is consistent with `28-0`.
- ARMATURE's code-level citations were carried, not re-derived, except where a §1 correction required
  opening the file.
- **Added by the author:** the author re-ran only the checks named in this file's header. Every other
  line number is as Fable read it at `6f6ef84`, and **will drift** — re-derive a site by its symbol,
  never by its number.
