# L1_A104_AND_WAVES — running record: Layer 1 node `L1-A104` applied, and U3's waves recomputed

## Status: WORK RECORD (the A-104/A-97 follow-up lane, 2026-11-12; reference, resolves nothing at runtime, CLAUDE.md §0.05; deleted with `unified/work/` when v12 is adopted)

Reconciled: 2026-11-12, A-104/A-97 follow-up.

Authority: Jordan, `unified/DECISIONS_ANSWERED.md` A-97 (*"Layer 1: make amendments as required"*) and A-104
(*"menu orders … do not cost scene budget because they are not scenes. however, these CAN prompt scenes after being
performed"*); for the further nodes, A-105, A-107, A-108. Convention followed: `unified/work/L1_APPLIED.md` (in-place
`⚠ AMENDED 2026-11-12 (Jordan, A-n; A-97, node L1-An)` quoting the old text; both halves; one Status-banner clause;
`hol` and the other `architecture/` files append-only; one new ledger id for the amendment record). Nothing here is
committed by this lane (the orchestrator's in-progress commits `bc2152f`, `09da06e` took part of it).

## Job 1 — `L1-A104`, and the further Layer 1 check

**Draft confirmed against the text.** `04:449` read *"**`Scene` is what the budget counts**, not the Act. `choose`
returns `Scene[]` of length ≤ `budget`."*; row 51 (`04:1081`) read *"… because the count is of Scenes chosen, not of acts
made"*. Both as the draft quoted. Code as read (not the reason for the text, CLAUDE.md §0.05): `loop/deliberate.py:230`
already checks the summed `Scene.cost(ext)` against the budget (`state/carriers.py:650`, an extended scene costs
`extended_scene_cost`), so "length" was already narrower than the check.

| file:line | what changed (old text quoted in place) |
|---|---|
| `architecture/meta/04_CODE_ARCHITECTURE.md:449` §B.9 | `choose` returns `Scene[]` whose summed `Scene.cost` ≤ `budget`; a `Scene` carrying only management orders costs 0 (A-104: an order is not a scene) and may open scenes after, each priced as any. `[CHANGED FROM DRAFT: "a scene of management orders" → "a `Scene` carrying only management orders", so the sentence does not call an order a scene beside A-104's "an order is not a scene"]` |
| `04:1081` row 51 (PART D twin) | "the count is of the cost of Scenes chosen …; a Scene carrying only management orders costs 0, refused or made (A-104)"; grade and falsifier unchanged |
| `04:3` Status | two clauses: L1-A104; L1-A105, L1-A107, L1-A108 (`ED-IN-0360`) |
| `holonic_ARCHITECTURE.md:882` §26 | pointer appended to `choose`'s signature ("bounded by budget"): the bound is the summed cost; an order scene costs 0 |
| `hol:939` §26.3 | pointer appended after the "No cost clause … A petition consumes budget like any act" bullet: "like any act" no longer holds of a management order; a petition is priced as before |
| `hol:3` Status | one clause |
| `architecture/PLAN.md:908` (W5), `:1204` (W17 item 1), `:1233` (W17 Proof), `:3` Status | pointers: "at most `budget` scenes" now reads the summed cost; the Proof's "6 scenes" means scenes costing 6 |
| `04:605` §C.2, row 10a `:1036` | `L1-A105` (see `L1_FURTHER.md`) |
| `04:235`, `:241` §B.2 | `L1-A107`, `L1-A108` (see `L1_FURTHER.md`) |

No line was added to any `architecture/` file (`wc -l`: `04` 1658, `hol` 2077, `PLAN.md` 2097, unchanged), so every
`04:NNN`/`hol:NNN` citation in the suite and `hole_register.yaml` stays valid.

**Restatements checked and left** (grep `budget|Scene\[\]|length ≤` over `architecture/`): `04:142`, `:171` (the module
lists name `budget` and `Scene[]`, no count); `04:202` row 15 (`office_bonus`, unrelated); F.12, F.29 ("the budget is the
whole price": still true, an order is priced at 0 by A-104, not beyond the budget); `hol:797` (the §24 diagram of the
same signature as `:882`, covered by its pointer); `hol:918` (budget a Query: holds); `hol:1256` (`carry` costs budget:
a petition, not an order); `03_VERBS_AND_LOOPS.md:119`, `:127`, `:301`, `07_DYNAMICS.md:14` ("the budget counts
scenes": holds, an order is not a scene); `01_AXIOMS.md:1211` (an oath paying budget); `ARCHITECTURE_V2.md:265` D19,
`:419`, `:514-531`, `01_NPC_VS_ARC.md:74`, `PLAN.md:83`, `:364` (quotations of #353's "no cost clause" for petitions and
the size-priced act P33, which A-104 leaves standing: it prices by kind, not size); `PLAN.md:1893` (a MET record of a past
gate). Falsifier grep after the edits (`length ≤|count is of Scenes chosen|at most \`budget\` scenes|at most that many
\*\*scenes`, excluding lines carrying the A-104 mark): one hit, `PLAN.md:906`, the sentence whose pointer sits on `:908`.

**Ledger.** `ED-IN-0360` (new; `registers/editorial_ledger_in.jsonl`, appended with `Edit`, keys and key order as the
existing rows, checked by `json.loads` over every line): the record of `L1-A104`, `L1-A105`, `L1-A107`, `L1-A108`.
`references/id_reservations.yaml` IN `next_free` 360 → 361.

**Checks (actual output).**
- `python tools/ci_naming_check.py` → exit 0, "Naming check: no new use of a deprecated name." (run after the ledger
  append and again at the end).
- `python tools/validate_ed_citations.py` → exit 0, "0 citation-integrity violation(s); 9 deferred; 318 open-reference info."
- `python -m engine.season.harness.register --verify-citations` → before any edit "CITATIONS: all resolve"; after, the same, exit 0.
- `python tools/tests_for_diff.py` → "changed files: 771 … no narrowing" (the branch diff against `main`), so, as
  `L1_APPLIED.md` did, only the tests that read `architecture/` were run: `pytest engine/season/tests/test_season_shape.py -q
  -k "w1_ or cr45 or citation or register or architecture_v2 or discharge"` → **9 passed**, 219 deselected (twice: after
  `L1-A104`, and after `L1-A105`/`A107`/`A108`). The file is `engine/season/tests/test_season_shape.py`; there is no
  `tests/valoria/test_season_shape.py`.

**Further contradictions** (A-100, A-101, A-105, A-107, A-108, A-112): `unified/work/L1_FURTHER.md`. Applied: `L1-A105`,
`L1-A107`, `L1-A108`. For Jordan, not applied: the season's "round" at `04:1065` row 36 and `hol:1166` (A-101's word;
the glossary's *lap*), and "exchange" at `03:126`. None found for A-100 or A-112.

**Suite files updated.** `unified/U3_LAYER1_AMENDMENTS.md` (node `L1-A104` APPLIED with its lines; three new rows;
Reconciled line); `unified/U3_DEPENDENCY_ORDER.md` §1.4 (four rows); `unified/OWED_TO_UNIFICATION.md` §A (four rows,
Reconciled line); `master/instructions/IS_B3_FA_SE_WR_GO_part2.md` `IS-B3-GO-07` (INSTRUCTION (6), Hash movers, Depends
on, §7.2 row: APPLIED; "round" in the season sense → *lap* in the clauses edited; Reconciled line). Grep `L1-A104` over the
suite found no proposal under `proposals/` citing the node. `unified/work/A102_112_APPLIED.md:18` still says "drafted,
not applied": another lane's record, left as written.

**Found, for the orchestrator.** `IS-B3-FA-07` places H-132's build in B21 (`IS_B3_FA_SE_WR_GO.md`, its Lane line);
`master/eval/V12_INTAKE.md` §3 and §4 carry H-132 in B21b. One of the two placements is v12's to keep; this lane edited
neither (B21b follows B21, so either order is acyclic).

## Job 2 — the waves

**Inputs.** §2.1 as written (with B03c and B19a); the nine batches the settle lane reconciled
(`master/eval/V12_INTAKE.md` §3: B03d, B11F1, B11F2, B21b, B21c, B21d, B21s, B24a, B37p; the task's B42 is B21d and
B10b-loops is B11F2 there; E4's B11b-verbs-r05, E5's B35a and E6's B03e are "Not taken" there); the new instruction items'
`Depends on` lines. Every edge, with its source, is the `edges` block of `U3_DEPENDENCY_ORDER.md` §8; the script's text
is there too (scratch copy at the session scratchpad, `waves/waves.py`, identical by `diff`).

**Runs.** (1) Old file, B03c excluded: reproduces the old §2.2, critical path and §2.3 exactly (20 waves, chain 20,
22 steps). (2) With B03c: W0–W21, chain 22, 23 steps (as the old note said). (3) Final: 52 batches, 339 edges, acyclic,
W0–W21, three tied chains of 22, 23 steps critical path first (24 in handle order); no `edges` row missing from §2.1; no
§2.1 wave cell differing; the §2.2 and §2.3 tables in the file equal the script's output line for line (45 of 45).
Sensitivity: E2's unconfirmed B23, B36 → B21d and the intake's `[ASSUMPTION]` B21 → B12 change nothing but B21d's wave
(W19).

| | before | after |
|---|---|---|
| batches | 42 (B03c listed but not computed) | 52 |
| waves | 20 (W0–W19) | 22 (W0–W21) |
| critical path | 20: B00 → B01 → B02 → B04 → B05 → B06 → B07 → B09 → B10 → B15 → B16 → B19a → B19 → B20 → B32 → B35 → B36 → B38 → B39 → B40 | 22, three ties: head B00 → B01 → B02 → B03 → B03c → B04 → B05 → B06 → B07 → B09 → B10; then (a) B15 → B16 → B19a → B19 → B20, (b) B11 → B21b → B21c → B24a → B27, or (c) B21 → B21b → B21c → B24a → B27; tail B32 → B35 → B36 → B38 → B39 → B40 |
| schedule | 22 steps (handle order) | 23 steps (critical path first, STAGES.md efficiency rule 5; 24 in handle order); 23 is the floor under the lane rule (§2.3's note) |

**Changes to `U3_DEPENDENCY_ORDER.md`.** Head: one Reconciled line. §0 handles: the ten new handles. §1.1: the IN lane's
new batches and the one-step cost. §1.4: four rows. §2.1: nine rows added (3d, 11F1, 11F2, 20b, 20c, 20d, 20s, 23a, 36p);
`after` cells gain B03d, B05 (B11), B15 (B18), B21b (B22, B23), B24a (B27), B21b, B21c, B24a (B32), B21 (B34), B11F1,
B11F2 (B38), B11F1, B37p (B39), B21b, B21c (B40); every wave cell that moved (B03c, and B04 on, B08 excepted)
rewritten with its old value kept. §2.2:
the table, a Reconciled note, a new critical-path paragraph (the A-100 one kept, marked superseded). §2.3: the table and
a Reconciled note (the A-100 makespan sentence kept, marked superseded). §5.1: eight rows gain an instruction item's batch
(`rosters.yaml`, `rosters.py`, `choose.py`, `carriers.py`, `deliberate.py` +B34; `hole_register.yaml` +B21; `sigma.py`,
`modules/combat/fight.py` +B15) and a Reconciled note. New §8: the method, the runs, the `edges` block, the script.

**Assumptions.** `[ASSUMPTION: the intake's §3 after/before columns carry every inter-batch edge its entries need; basis:
§3's own cycle check runs over those columns; not re-extracted per entry]`. `[ASSUMPTION: a two-lane batch (B12, SE+WR)
holds both lanes in the schedule; basis: the old §2.3 is reproduced under it]`. `[ASSUMPTION: unit time per batch, as
§2.3 already states]`. **Not done:** the nine intake batches have no §1 item and no §5.1 census rows (their edit sets are
in the evaluation lanes' carry-forward blocks, not in `V12_INTAKE.md` in a readable form); listed in §2.1's Reconciled
note and §5.1's for v12's author.
