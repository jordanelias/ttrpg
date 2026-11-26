# Defer the stored goldens to the end of the workplan; keep the readings

## Status: PROPOSED, amended after an Opus audit (2026-11-26). Rulings below were delegated to that audit by Jordan; nothing is applied.
## Lane: IN (cross-cutting).

Jordan, 2026-11-26: *"I am okay with reusing pins or literally just ignoring them until the workplan itself is built out entirely"*; *"we are currently wasting so much time trying to keep same balance bottom-up when we haven't even built all the slices"*; *"P10 has exceptions if testing specifically for narrative/stories/arcs"*; the goal is the least time per batch **without losing the ability to tell whether a batch worked**, with a targeted post-workplan run (B99) once everything is built. Figures marked `[MEASURE]` are not measured.

## 1. How a batch's efficacy is decided, and what a pin adds

A batch works if (a) each item's falsifier and control pass on a hand-built world (P9), (b) the batch gate's readings hold (`aperture 2 s` executed counts, `register --check`, `--requirements`, `m1_acceptance`, BUILT OUT), and (c) the batch's recorded per-batch hash readings show the realm hash moved only where the batch declared a mover, and not at all for an EQUAL item (v12 part 29:26, 117; P17(3)). All three need **no stored file**: each is a base-against-head reading taken inside the batch.

A stored golden adds exactly two things: whole-realm determinism across processes and machines (CI sets no `PYTHONHASHSEED`, so a match with a literal proves seed independence), and drift between batches, which every batch's entry reading already covers (P16(2)). The rest of the pin machinery (the `.99` re-record edit, the ~15 "RE-PIN" paragraphs in `_realm_goldens.py`, the "re-pin" comments in about 60 test files) says nothing about whether a batch worked.

## 2. Defer, keep, replace

**Defer to B99** (stored literals, no per-batch reading): the `SHIPPED`, `BUILD` and `CENSUS` edits in `_realm_goldens.py`; inline realm-hash literals (in `endowment`, `rival_precedence`, `scene_sequence`, `task_draw`, and the count pins such as `BEFORE_SEASON_ONE_ENTRIES` in `claim_fade_as_read`); `engine/season/runs/results.json` regeneration (asserted by `test_w15`, `test_season_shape.py:1153`); the go07 control tests; B41's `oracle_pins --build`.

**Keep:** P14 sentences 1 and 2 (hash movers declared; a mover's before-reading is the previous item's after-reading); P16(2) (carry-forward readings, a speed rule); P17(3) first half (EQUAL items record no hash, one seed-0 reading per EQUAL run, bisect only on inequality, seeds 1 and 2 only for movers); the batch table's hash column; each `.99`, renamed in effect "close readings": seeds 0 to 2 base and close hash recorded in the commit body, plus aperture, register and requirements, with **no golden edit**; `## Readings` minus its re-pin lines; the `field-goldens` job (see §4(b)).

**Replace:** (i) one blocking test: the realm hash at seed 0 after one season, equal in two subprocesses under `PYTHONHASHSEED` 0 and 1 (class B, in-process; it recovers the one signal only a stored literal gave); (ii) the arm-off pins that compare to a stored literal (`test_task_draw.py:96`, `test_notice_draw.py:40`) re-expressed as arm off against arm absent in one process.

## 3. Structural conditions

1. **Stale goldens must be deselected, not skipped** (P8 forbids skip, xfail, quarantine). That is a marker deselection, which `pytest.ini`'s ONE RULE reserves to Jordan; ruled in §4(a). Without it CI is red until B99.
2. **The marker is broken today** and must be rebuilt before anything relies on it. Measured: `-m shipped_pin` marks 14 tests, of which 8 are false positives (`co_names` matches local and attribute names: the 5 tests of `test_b01a_generated_attributes`, a local `SHIPPED=(1,6)`; `Step.CENSUS` in `test_season_shape` w2 and in 2 `test_territorial_subsistence` falsifiers), 6 are true pins, and it misses the aliases (`ARM_OFF_PINS`, `REALM_PIN_SEED_0_TWO_SEASONS`), the inline literals and `test_w15`. Only 7 files import `_realm_goldens` (an earlier figure of 21 counted comment mentions).
3. **B41-go-port-gate as scheduled is unsafe.** Its gate runs `test_go07_canonical_digest.py` (reads `SHIPPED`) and it writes `oracle_pins.json` at W17, which B98's 38 behaviour movers then stale. Under deferral its go07 gate line is dropped and `oracle_pins --build` moves to B99.

## 4. Rulings (delegated by Jordan to the audit; none is his alone: process text, no change to the game or canon)

- **(a) Marker deselection in blocking jobs: YES WITH CHANGES.** Rebuild the marker **by identity** (a global the test reads that is, or holds a value of, the `_realm_goldens` object). Derive the member set once with a perturbation run: change one golden and one trivial world-move; each red is either moved to read its literal from `_realm_goldens` (so it is marked) or rewritten as a control. Add `test_w15` by its owner, `files.RESULTS_JSON`. Amend P8 to read "except the `shipped_pin` deselection until B99 (Jordan, 2026-11-26)". Deselects pins and nothing else.
- **(b) Take `field-goldens` out of the KEPT list and out of `ci-summary`: NO.** It is the mass-battle sim's byte-exact oracle and the only behaviour-preservation proof for MB refactors (the B12b gate uses it as the EQUAL proof). It runs as a parallel CI job and batches never wait on CI (§11), so it costs a batch about nothing. No `CLAUDE.md` edit. An MB batch that moves it re-records it in that batch.
- **(c) Delete P14, P15, P16(2), P17(3), the `.99` re-records: YES WITH CHANGES.** Delete only: P15 whole; P14's last sentence; P17(3)'s go07 sentence and P17(5); the re-record INSTRUCTION, WHERE and golden-file TESTS lines of each `.99` (36 items); the pin clause of each `EXPECTED RED UNTIL`; B41's go07 gate line. Keep the rest (§2). The kept parts cost about one 15 s hash reading per tree and are what shows a batch moved only what it declared.

## 5. B99, the targeted post-workplan run

1. `pytest -m shipped_pin`; re-record every red in one commit that says plainly it re-recorded goldens.
2. Regenerate `runs/results.json` with `harness/report`.
3. `oracle_pins --build`, then `--check` under `PYTHONHASHSEED` 0 and 1.
4. `tools/freshness_gate.py --update`, only for pins whose covered code moved.
5. THE NINE re-take on that tree.

Attribution of a late drift comes from the chain of close readings in the commit bodies; a bisect has little to test against, since all 30 mover batches change the hash on purpose.

## 6. Order of work

1. Rebuild the marker by identity; run the perturbation once; list what it finds. (No CI or plan change yet.)
2. Add the subprocess determinism test and re-express the two arm-off pins.
3. Add `-m "not shipped_pin"` to `unit-tests`, the `season-tests` legs and the P18 lane commands; check that marked plus unmarked equal the full collection with no duplicates.
4. Edit the plan and `methodology-execute` per §4(c); amend P8 per §4(a); drop B41's go07 gate line.
5. B99 as in §5.

## 7. Not verified, and not covered

Timings (`[MEASURE]`); whether any batch moves the `bat.py` field digests; how many of the 60 "re-pin" files hold realm-output literals rather than combat tables. It does not remove the carried reds on `main` (combat (7, 5) cell, `test_shortest_case`, two `test_playable_inquiry`, `test_rumour`), or change THE NINE, class B equalities, or the narrative exception to P10.

Corrections from the audit to the first draft: 36 `.99` items, not 44; about 5,100 tests, not 4,100; 7 files import `_realm_goldens`, not 21; 4 inline-hex files besides go07, not 5; `field-goldens` is not a class-A pin.
