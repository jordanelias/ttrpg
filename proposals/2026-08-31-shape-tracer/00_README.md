# Shape tracer — two executed tests of PR #350's idealized code shape, and what they demand

## Status: **PROPOSED (2026-08-31). HELD BACK. Nothing ratifies on merge.**

**Read `04_UNIFIED_SHAPE.md` first.** It is the deliverable; everything else is its evidence.

| file | what it is |
|---|---|
| **`04_UNIFIED_SHAPE.md`** | **the unified proposal** — five laws, the carriers, what is refused, what is still Jordan's |
| `01_TEST_A_NPC.md` | **test a:NPC** — a season for 27 named NPCs, copyist to King. 22 BLOCKED · 4 NOT-ASSESSED · 1 DEGRADED |
| `02_TEST_B_ARCS.md` | **test b:ARCS** — 50 arcs from `designs/arcs` played out. 39 BLOCKED · 10 NOT-ASSESSED · 1 PLAYABLE |
| `03_THROUGHLINES_AND_CHANGES.md` | the throughlines and the **first** change list, kept unrewritten so what it said before the evidence arrived stays legible. §6 records what arrived after |
| `tracer/` | **the instrument** — PR #350's shape, executable |
| `TRACE.txt` · `gaps.json` · `results.json` | the run: the sequence, the gap register, the data |

## The instrument

`tracer/shape.py` implements the shape faithfully enough to execute: the six steps, the four write
classes, the Partition asymmetry, and a `View` that raises on any world collection so Law 2 holds by
type rather than by discipline. `tracer/probes.py` is 65 probes, each a real execution that either
completes or raises a typed `ShapeGap` — `UNSPECIFIED`, `FORBIDDEN`, `NO-PRODUCER`, `COLLISION`.
`tracer/run_cases.py` routes 527 `season_requires` rows, written by lanes blind to the shape, onto
those probes.

```
cd tracer && python3 run_cases.py                 # the run
cd tracer && python3 -m pytest test_tracer_is_honest.py -q   # 20 self-tests
```

## The instrument's own honesty

`tracer/test_tracer_is_honest.py` exists because the tracer gates every finding downstream. **Five
defects were found during the run and every one flattered the shape**, which is the dangerous
direction; each is regression-tested so a sixth is caught by a machine rather than by luck. Two were
found by audits that never saw the reasoning that produced the reports.

**226 of 527 needs did not route and are reported `UNMAPPED` rather than passed.** Fourteen cases
are `NOT-ASSESSED` — more than half their `core` needs failed to route, so the test did not aim at
them, and grading such a case PLAYABLE would be the instrument flattering the shape by failing to
point at it. **Probe verdicts are hard; case verdicts are advisory.** `01_TEST_A_NPC.md` §5 is the
catalogue.
