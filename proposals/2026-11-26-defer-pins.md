# Defer the shipped-output pins to the end of the workplan

## Status: PROPOSED
## Lane: IN (cross-cutting). Owner of the decision: Jordan.

Jordan, 2026-11-26: *"I am okay with reusing pins or literally just ignoring them until the workplan itself is built out entirely"*; *"the game needs to be balanced topdown and bottom-up, and we are currently wasting so much time trying to keep same balance bottom-up when we haven't even built all the slices"*; *"P10 has exceptions if testing specifically for narrative/stories/arcs"*.

This document proposes how to stop paying for pins during the build without losing what they were protecting. It is a plan, not a ruling; nothing in it is applied. Figures marked `[MEASURE]` are not measured.

## 1. What "a pin" is here, and what is not one

Three different things share the word. Only the first is deferred.

| Class | What it is | Where | Deferred? |
|---|---|---|---|
| **A. Stored shipped-output goldens** | A literal (hash, count, set) of the shipped realm after one or two seasons, compared by a test | `engine/season/tests/_realm_goldens.py` (`SHIPPED`, `BUILD`, `CENSUS`), read by 21 season test files and `test_go07_canonical_digest.py`; 5 more season test files hold inline 32-hex literals; `engine/season/runs/results.json` (byte-check, see §6); CI job `field-goldens` (`tools/ci_golden_modes_check.py` `FIELD_PINS`, about 7 minutes) and its drift guard `tests/valoria/test_field_golden_pins.py` | **Yes** |
| **B. In-process equalities** | Two worlds built in one process and compared to each other: same seed twice, an arm `off` against absent, a control arm | the acceptance probe (`tools/m1_acceptance.py`), `requirements.yaml` rows reading "the same content hash twice", control-arm falsifiers | **No.** They need no stored file and cost nothing to keep valid |
| **C. Plan machinery for pins** | The process that keeps A current: hash movers named per item and batch (P14), re-record in the batch's `.99` commit (P15), carry-forward readings (P16(2)), `## Readings` blocks, the batch table's hash column (30 MOVER, 4 EQUAL), the BATCH-CLOSE go07 blocking pin (P17(3)) | `workplans/valoria_master_workplan_v12*.md`, `skills/methodology-execute/SKILL.md` | **Yes** |

Also not pins, and kept: the exporter round-trip `--check` for `engine/engine_params/`, `test_morale_write_sweep.py`, the compile gate, the test-lane ratchet, the `canonical_sha__*` freshness gate (it covers documents, not game output).

## 2. What must stay (the required exceptions)

1. **Determinism:** the same seed twice gives the same hash (class B). Observed by `engine/season/tests/test_season_shape.py` and the acceptance probe. Nothing changes.
2. **EQUAL batches** (behaviour-preserving, 4 in the batch table): each keeps one in-process before/after comparison, base SHA against head, with no stored file. This is the only proof a refactor moved nothing.
3. **THE NINE at B99:** the longer re-take stays the plan's last item (P10 exception 1).
4. **Narrative, story and arc tests** run the seasons the arc needs (P10 exception 2, written 2026-11-26, `dc5777a4a`); they are tests, not pins, and are unaffected by this proposal.
5. **Pins return at B99, once.** Deferral means "re-record all at the end", not "never": B99 runs the pin tests, records every golden in one commit that says plainly it re-recorded them, and re-takes THE NINE.

## 3. The structural condition: stale pins must be excluded, not skipped

Stored goldens go stale at the first batch that moves the world. A stale golden test fails. P8 forbids skipping, xfailing or quarantining a test, so the exclusion has to be a **marker deselection**, which `pytest.ini`'s "ONE RULE" reserves to Jordan as a coverage cut. This proposal asks for that ruling for the `shipped_pin` marker only. Without the exclusion CI stays red for the rest of the plan.

## 4. The change, in order

Each step is independently shippable and leaves CI no worse.

**Step 1: make the marker complete.** `conftest.py` marks `shipped_pin` today for a test that names `SHIPPED`, `BUILD` or `CENSUS`; it marks 14 of about 4,100 tests because most pin tests read the goldens through module-level aliases (for example `ARM_OFF_PINS = SHIPPED[...]`). Change it to follow aliases: in a file that imports from `_realm_goldens`, mark a test whose function reads a module global that is, or was built from, a golden value. Add the 5 files with inline hash literals. Derive it from the owner (the golden module's names); list no test by hand. *Falsifier, run once and not kept:* change one golden value; exactly the marked tests that read it must fail, and no unmarked test.

**Step 2: exclude in the blocking jobs.** Add `-m "not shipped_pin"` to the `unit-tests` job and the `season-tests` legs, and to every batch lane command (P18). *Check:* `pytest --collect-only` ids for (marked) plus (unmarked) equal the unfiltered collection, with no duplicates, as for the earlier shard split.

**Step 3: take the field goldens out of the blocking tier.** Remove `field-goldens` from `ci-summary`'s `needs`, as `lanchester-signature` already is; run it only on demand (`workflow_dispatch`). This needs Jordan's ruling because `CLAUDE.md` §0.1 pt 5 names the golden-modes check in its KEPT list.

**Step 4: delete the machinery (class C).** In the workplan head replace P14, P15, P16(2) and P17(3) with one rule: *pins are not re-recorded during the build; a batch's close reads no golden; B99 re-records them once.* Delete the `.99` re-record items and the `## Readings` blocks that serve only pins, and drop the batch table's hash column except the EQUAL flag. In `methodology-execute` remove the readings and re-record steps from BATCH OPEN, the item gate and BATCH-CLOSE; the EQUAL in-process comparison replaces them for those 4 batches. In `CLAUDE.md`, edit §0.1 pt 5 (drop the golden-modes check from KEPT) and §7 (the pin paragraph) in place; the file is at its 645-line cap, so no line is added.

**Step 5: the rule that keeps it from regrowing.** A new pin test must import from `_realm_goldens` so the marker catches it, or it observes behaviour and is not a pin. This is a reader's discipline; no guard is built (§0.1 pt 5).

**Step 6: B99.** Run `pytest -m shipped_pin` and the field goldens, record every moved golden in one commit that says it re-recorded them, run `tools/freshness_gate.py --update`, and re-take THE NINE.

## 5. What it saves `[MEASURE]`

Known: `field-goldens` took 6m56s per run (run 45737148512); `test_go07_canonical_digest` reads seeds 0 to 2 at one and two seasons, about nine realm seasons at about 15 s each; the marked tests are a small share of a leg. Larger and unmeasured: the per-batch `.99` re-record item (44 in the plan), the `## Readings` blocks, and the before/after runs every mover item takes. Measure first: record `--durations` for the 14 marked tests plus the aliased ones, and count the `.99` and readings positions in `workplans/valoria_master_workplan_v12_part*.md`, before claiming a figure.

## 6. Risks and open questions

1. **Attribution is late.** A drift from an early batch surfaces at B99. `git bisect` over the batch commits on one realm-hash test is about 7 runs for 69 batches; each batch's recorded mover declarations narrow the suspects.
2. **B41-go-port-gate** (EQUAL, wave W17) precedes B98 and B99 (W23, W24). If it validates a port against pinned oracle values, those will be stale. Not read; check before ruling.
3. **`engine/season/runs/results.json`** is a derived artifact a byte-check compares (P15). Which test or tool asserts it, and whether the marker catches it, is unconfirmed.
4. **A pin test that also asserts behaviour** (a count that doubles as a design claim) would be excluded with the pins. Step 1's falsifier will list these; split them or leave them marked.
5. **Rulings needed:** (a) the `shipped_pin` marker deselection in blocking jobs (§3); (b) removing `field-goldens` from the KEPT list (§4 step 3); (c) deleting P14, P15, P16(2), P17(3) and the `.99` re-record items.

## 7. What this does not do

It does not remove the carried reds on `main` (the combat (7, 5) cell, `test_shortest_case`, two `test_playable_inquiry` tests, `test_rumour`), which are separate failures. It does not change THE NINE's definition or the narrative exception. It does not touch class B.
