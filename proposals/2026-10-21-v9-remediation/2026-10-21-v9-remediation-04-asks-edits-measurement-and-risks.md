# v9 remediation proposal, part 4: Jordan asks, edits to existing parts, measurement, risks, self-check

## Status: PROPOSED. Merging this file ratifies nothing: every item, ask and edit below is HELD BACK (ED-1094's loud exception). Jordan ratifies or adopts item by item, as edits to the v9 parts it names.
## Lane: IN (cross-cutting). A proposal for edits to `workplans/valoria_master_workplan_v9*.md`, not a second plan (`CLAUDE.md` §2: one active plan per lane). On adoption its items become v9 positions and these files are deleted with a `FORK:` row. **Home of v10 positions** since the v10 adoption (`ED-IN-0299`): this file holds the full spec of the v10 positions whose plan row names it (rows: `workplans/valoria_master_workplan_v10_part3.md` §1; handles: `workplans/valoria_master_workplan_v10_part12.md` §1; where `workplans/valoria_master_workplan_v10_part13.md` amends a home, the amendment governs), and is deleted with a `FORK:` row when its last position lands (v10 head §9 step 6).
## Grade under `CLAUDE.md` §0.2: `paper`. Nothing here executes. It moves no row of THE NINE; a row moves only on its own `measured:` block.
## Parts, in reading order: `2026-10-21-v9-remediation-01-verdict-and-coverage.md` → `2026-10-21-v9-remediation-02-items-rb0-to-rb3.md` → `2026-10-21-v9-remediation-03-items-rb4-rb5-and-index.md` → `2026-10-21-v9-remediation-04-asks-edits-measurement-and-risks.md`.

## 3. The Jordan asks — only what survives all five steps; home: `_part5` §J.2 (no new document, no new ledger row)

Each is drafted as v9 §J.2 drafts a row: question, options, consequence, recommendation (or none), what it unblocks.
**No `needs_jordan` ledger row is written by this plan.** Each ask rides an existing row or the §J.2 table (P5:402-438).
The batch whose instrument produces its evidence asks it, at that batch's close.

### JQ-1 · NEW ranked row (proposed rank 2): how much of a person is the draw?

- **Question.** Among the 46 realm persons who carry a pursuit vector, the sampler overrules a strict score top in 72 %
  of `--decisions` choices (198 of 276 at seed 0; 202 and 196 at seeds 1 and 2). The outvoted margins' median is
  0.030 against `choice_temperature` 0.1 (`data/fixtures.py:286`), and 89-93 % of them lie below τ. Pursuit decides
  28 %. Do the persons' goals decide their acts often enough?
- **Options.** (a) Keep τ = 0.1 and read the share as R-08's "may not make the optimal decision". R-06's fourth conjunct
  is then recorded and never thresholded. (b) Re-scale: lower τ, or scale the score terms. Either is one fixture; every
  world moves. (c) Name a share that pursuit must reach among vectored persons; R-06's fourth conjunct reads it as its
  threshold.
- **Consequence.** (a) Two persons with different goals often act alike, and R-06 holds by statement only. (b)/(c) Goals
  order more acts, and R-08's non-optimality then rests on ties and on the smaller outvoted share.
- **Ladder.** 1: not superseded. 2: not irrelevant (R-06, R-08). 3: no document states a share. 4: H-96 is precedent for
  the sweep, not for a value (P2:367). 5: the architecture cannot choose how much of a person is noise.
- **Recommendation.** None. Evidence attached at RB-1's close: REM-12's split at H-96's grid (τ ∈ {0, 0.1, 0.25, 0.5,
  1.0}) at seeds 0-2 [the grid's values are H-96's, carried; not re-checked here].
- **Unblocks.** R-06's fourth conjunct (REM-05); nothing else waits.

### JQ-2 · AMEND rank 1 (J-13's remainder): does your "pool only" constraint reach combat and mass battle? (rev. 2, C-05)

- **Your standing constraints, quoted from rank 1's own row (P5:400, :410).** "pool only it is, but ensure you don't go
  so far as to deprive player of a chance at winning". "It's a derived score that is used for the subsystem for a
  character, but it is not a character attribute in and of itself". P5:410: "Your 2026-09-06 constraints … bind any
  answer". They were said of the proceeding's pool, so whether they also bind the other two resolutions is itself the
  first question.
- **Today.** `Combatant(a_id, end=a_end)` (`modules/combat/fight.py:45`) takes `end` from the body band alone
  (`seam/wrappers/combat.py:130-138`). Mass battle builds one Unit at `_SEASON_FORCE_POWER = 4` (`massbattle.py:196`)
  and `command = 4` (`:183`).
- **Question.** (1) Do the two constraints bind combat and mass battle as well as proceedings? (2) If they do, which of
  the options below?
- **Options, each checked against the constraints.**
  - (a) A per-person term DERIVED per subsystem from the source J-13 rules, entering combat and mass battle **through
    the pool only**. `end` stays body-band, and no stored attribute is read directly. This survives both constraints.
  - (b) Identical fighters are intended at those two scales (NERS G1's second arm). The claim of person-varying
    resolution is then dropped for them. This survives trivially.
  - **Dropped as written:** NERS G1's first arm, "`Person.attributes` (#445 K-2) with its first reader `party_end`".
    A stored attribute read directly into `end` fails "not a character attribute in and of itself", and `end` is not
    the pool, so it also fails "pool only". It returns only if you say the constraints were scoped to proceedings
    (answer "no" to (1)). It is then offered as (c), with K-2 still "not ratified" (P7:44).
- **Ladder.** NERS G1 survived all five (`references/ners_audit_2026-10-14.md:427`). J-13 (iii) covers the contest only
  (P5:410). Step 5 cannot choose between (a) and (b), because the two lead to materially different games.
- **Recommendation.** None. **Unblocks:** R-09's by-person conjunct across all three resolutions; M1.

### JQ-3 · ASK-THEN annex to the CELL-VALUE AND COSINE PASS row (P5:427): four magnitudes no v9 part names

- **Question.** In the same pass, set or confirm: H-187, how far a weight shifts at scar threshold 2 (shipped
  `scar_weight_shift = 0`, `data/fixtures.py:680`); H-188, how religious confliction enters the score (`confliction_weight
  = 0`, `:688`); H-200, the competence factor in refraction (1; `hole_register.yaml:4398`, kind RULING); H-208, IN-34's
  rates and starting age (`age_step`, `illness_rate`, `:579-580`).
- **Ladder.** 1-4 silent: each is a NUMBER hole with no source, and grep finds each in 0 v9 parts. 5: no value can be
  derived. **Not ranked:** no row's `met` waits on them. They decide whether characters change (R-06, R-07 substance).
- **Ask when.** With the CELL-VALUE pass, as that row already holds NPC-089's and `restore`'s numbers (step 4 precedent
  for bundling).

### JQ-4 · ASK-THEN at REM-32: G3's weight→troop value

- **Question.** REM-32 lands the conversion at `massbattle._weighted_unit` with the value that reproduces today's force
  (a season force "routs on contact regardless of who wins", `massbattle.py:198-207`; the constant is `:196`). What value makes a season field
  contestable?
- **Ladder.** NERS G3: "Form: agent, MB lane. Value: `[OPEN — Jordan tuning]`". **It gates no `met`:** R-07 conjunct 3
  is reached by a `Lost` field too (C9).
- **Ask when.** REM-32 merged (B-T's tail).

### JQ-5 · OPTIONAL ASK-THEN (rev. 4): ratify the IN-46 and IN-47 designs?

- **Question.** Your 2026-10-21 ruling lets RB-3 build. The plan keeps both designs PROPOSED and held under ED-1094
  until you ratify them [ASSUMPTION; medium]. Do you ratify either now, or leave both held?
- **Ladder.** Steps 1-5 cannot ratify a design whose hold names you as its releaser (P4:34, :41).
- **Nothing waits on it.** The builds proceed either way.
- **Ask when:** RB-3 opens, or never.

### JQ-6 · NEW ranked row (proposed rank 3, after JQ-1): what makes a settlement go hungry? (rev. 4, hunger)

- **Question.** Hunger is now a settlement attribute (REM-50) that rises as population grows against the food on hand.
  At today's magnitudes it cannot bind after the first yield. Measured this session (`SP/hunger/cover.py`, realm, seed 0,
  PYTHONHASHSEED=0):
  - every settlement holds **21.7 seasons of food after season 0, and 41.7 after season 1**;
  - all 37 cohorts are short only in season 0, before the first yield;
  - capacity caps each settlement's population at 4-9 (median 6), so even a cohort at capacity eats far less than the
    yield (`SP/hunger/sweep_weight.py`: weight ×10 still records 0 shortfall after season 0).
  Which magnitude should make hunger bind?
- **Options, each an existing knob with an owner.**
  - (a) Per-head subsistence: `rosters.yaml: subsistence_weight` (grain 2, salt 1; H-11's "invented" weights).
  - (b) Yield per Site: `SITE_YIELD` (`data/fixtures.py`).
  - (c) Population: the authored cohort weights (all 2, `cohorts.yaml`; ED-WR-0011 calls the count a sweepable fixture)
    together with `capacity`'s floor (ED-SE-0051, RULED as a Query with a floor).
  - (d) Leave it: hunger binds only in scarce worlds, before the first yield, and under shocks.
  - Also: the band thresholds (`band_floors["hunger"]`, REM-50) and the body cost (H-125, shipped at 10 by REM-52).
- **Consequence.** (a)-(c) make hunger a standing pressure that drives bodies, deaths, governors' transfers and
  `requisition` politics. (d) keeps it a rare event.
- **Ladder.**
  1. Not superseded.
  2. Not irrelevant: it is Jordan's requirement.
  3. No document sets the ratio. H-11 calls the weights invented, and ED-WR-0011 calls the count a fixture.
  4. No precedent sets a ratio.
  5. The architecture cannot choose how scarce the world is.
- **Recommendation.** None. The evidence comes at RB-5's close: M-H2's sweep, showing hunger and cohort survival at
  each knob.
- **Unblocks.** Hunger binding in the shipped realm; the settlement row's substance (R-04).

### Answered by the ladder, so not asked (recorded so none rides back onto §J)

| would-be ask | step | answer |
|---|---|---|
| do the 37 cohorts break R-08? (rev. 2, C-11) | 4 | no. G-1's precedent (P2:385): a zero with no reason is not a tie the person has a reason to break, so an all-zero field is true indifference (P2:381's gloss). The cohorts are R-06's: a visibility conjunct gated by ED-IN-0296 (2), already asked. The draft's "yes, by T-l" is withdrawn |
| may RB-3 build IN-46/IN-47 on held designs? | — | **answered by Jordan's ruling of 2026-10-21 (D-2 yes)**; the designs stay held [ASSUMPTION]; JQ-5 is the optional ratification |
| is the verb roster 46 or 92? | 1 | already held as the suite's D-V decisions (DEF-1) |
| does `chronicle`'s deletion need a gate? | 1 | H-214 holds it (C2) |
| ED-IN-0261's self/other weighting (G5's condition) | 5 survives, nothing waits | not asked (DEC-8) |

---

## 4. Edits to existing parts — proposed text, with anchors

### 4.1 v9 and data-file edits (agent-landed; v9 was ratified on merge, ED-1094, so these merge by PR review)

Anchors are HEAD `b70b5af` line numbers; re-derive each by its quoted words before editing (P3:5).

- **E-1 · P1:191** — replace the paragraph's first sentence with: "⚠ **Three rows cannot read `met` under v9 as it
  stands, a fourth is conditional, and so M1 cannot** (`m1_acceptance.py:320` passes only when every row is met): R-04's
  conjunct (3) waits on IN-46's and IN-47's builds (RB-3, scheduled by REM-03; the builds proceed by Jordan's
  2026-10-21 ruling, with the designs held back under ED-1094); R-07's conjunct (3) waits on a fought
  field, which no v9 position reached until REM-27 (P2:30, :354); R-09's by-person pool waits on a ruled SOURCE for
  `capability` (J-13's remainder, widened by JQ-2). R-05's earliest `met` is conditional: every owner's EXIT records an
  execution, and ED-IN-0297 is answered (P2:265)."
- **E-2 · P2:38** — "R-04's conjunct (3) waits on build batches for IN-46 and IN-47, which only their design review can
  create, R-09's by-person conjunct waits on a ruled `capability` source, and R-05's earliest `met` holds only if…
  **Both are stated**" → "…**R-07's conjunct (3) waits on a fought field (REM-27), and R-05's earliest `met` holds only
  if every owner's EXIT observed its verbs executing and ED-IN-0297 is answered. All four are stated in their
  sections.**"
- **E-3 · P2:227-231** — after "Re-read at B-I: 21 of 45 executed" add: "The executed set fell 21 → 17 (B-W, IN-57) → 16
  (B-N) (`requirements.yaml:977-991`). **The table holds 46 rows at HEAD `b70b5af`** (`len(VERB_TABLE)`; `speak` returned
  at B-N; `requirements.yaml:985`'s 45 is a dated reading). **Scope:** R-05's `met` counts the code table. The 33 verbs
  of `proposals/2026-10-16-verbs/` with no row here are outside it until Jordan's D-V decisions (the suite holds itself
  back, `…verbs-01-thesis-and-persons.md:3`). **Instrument caveat until RB-1:** `aperture`/`corpus_run.attribute` count
  "attempted" over `SeasonDriver.resolved`, which a contested act refused at admission never enters
  (`requirements.yaml:991-995`). Read a 'never attempted' contested row as 'unknown' until REM-10 lands."
- **E-4 · P2's R-05 table, after the `forge`, `carry` row (:243)** — two rows:
  `| restore | executed (B-I); left the set under IN-57 | 0/27 realm, 0/8 spine (aperture 2 0, HEAD b70b5af) | every
  realm refusal ends on exists:Site = 0: formed on non-Site referents (F-B) | REM-22 | RB-2a |` and
  `| transfer | — | 1/47 realm, 0/6 spine | 46 refused on stores; 30 write-clause no-ops (perform() moving nothing,
  [UNVERIFIED] cause) | REM-2A | RB-2b |`.
- **E-5 · P2:200 and :209** — "build: none" → "build: RB-3 (REM-30, IN-47, beside B-Y; REM-31, IN-46, after B-Y),
  scheduled by REM-03 and cleared by Jordan's ruling of 2026-10-21; each build PR lists both designs as held back
  (ED-1094) until he ratifies them". P2:209's sentence ends: "…until a build batch exists for both: **RB-3 is that
  batch.**"
- **E-6 · P3 §B.1** — one row per RB batch in v9's columns, carrying §2's members, shared files, gates, exit instruments,
  declared re-records, lanes and budgets. The serial spine at P3:182 reads: "… B-O (closed `46ec000`) → B-P → RB-2a → RB-2b → B-Q
  → B-R → B-S → B-T; RB-1 before B-P; RB-4a beside B-P, merging before B-S; RB-3a beside B-Y; RB-3b after B-Y; RB-4b
  after B-Y, beside B-T." [ASSUMPTION; medium; Jordan to correct.]
- **E-7 · P2:354 (R-07 `met`) annotation** — "Conjunct 3 is met by a `Won` or `Lost` field: both bands write
  `Person.stance` (`verb_table.yaml:709-710`); `Unopposed` (`:711`) writes none. Its owner is REM-27 (RB-2b), and G3's value does
  not gate it. Deaths (finding 15): H-209 is this row's contributor at IN-12 step 5 (B-R; `hole_register.yaml:4510-4518`).
  Conjunct 1's `told_by` rests on `epistemic._ch_chronicle`, kept by H-214 until the `<rung kind>` reach channel lands;
  a position that deletes the channel re-reads this conjunct in the same commit."
- **E-8 · P2:312 (R-06 `met`)** — append: "**and** (fourth, recorded; its threshold is JQ-1's) `decision_spread
  --decisions` at seeds 0-2 prints, over persons with a pursuit vector, the share where `pursuit` decides and the share
  where the draw outvoted a strict top (REM-12). Until JQ-1 is answered this conjunct is reported and does not gate, and
  **no `measured:` paragraph may cite R-06 as showing that inclination orders choice.** **and** (fifth, gated by
  ED-IN-0296 (2)) every acting person carries a pursuit vector, or the row names those declared out of scope; at HEAD 37
  of 83 realm actors (the cohorts) carry none."
- **E-9 · P2:381 (R-08 `met`) (rev. 2, C-11)** — "for each sampled person" → "for each person of the corpus's `p_a`
  sample **and each realm person with a pursuit vector, read through `decision_spread --decisions` (REM-12)**".
  Annotation: "Read under the gloss '(the draw breaks only true indifference)' and G-1's precedent (P2:385): a person
  with no vector has no reason to break a tie, so the realm's 37 cohorts are true indifference here and are counted at
  R-06's fifth conjunct instead."
- **E-10 · P2:424-425 (R-09 `met`, third conjunct)** — "`corpus_run`'s `DEGREES RESOLVED` line is non-empty for at
  least one non-combat verb besides `tell` (an inquiry or `speak`)" → "`corpus_run`'s `DEGREES RESOLVED BY VERB` line
  (REM-13) shows a non-combat verb besides `tell` resolved at ≥ 2 bands **whose `writes_at` differ** (`BANDS THAT
  DIFFER`); `speak`, whose four bands write `[]` (`verb_table.yaml:948-951`), cannot satisfy it". Also, under REM-15:
  "and (fourth) `storybar --draw-seeds`, which varies only the chooser's draw on one built world, shows ≥ 1 differing
  chain, with the same-seed control equal and the τ = 0 plant showing none. Rolls stay keyed to `world_seed`, so this
  conjunct reads choice-driven variance only (recorded as its residue)."
- **E-11 · P2:24-25** — "met at B-I; re-checked at each re-take" → "…; re-taken after B-O's FI-01 skip arm and FI-03
  (owed, REM-16) and at RB-2b's close (formation moves the corpus)".
- **E-12 · P5 §J.2** — JQ-1 as a new rank 2 (ranks 2-7 renumber 3-8); rank 1 amended by JQ-2; the CELL-VALUE ask-then row
  gains JQ-3's sentence; a new ask-then row JQ-4, "ask when: REM-32 merged"; and JQ-5 as an optional ask-then (the design holds; nothing waits on it); and JQ-6 as a new ranked row (hunger's
  magnitude).
- **E-13 · `engine/season/verb_table.yaml:89-91`** (REM-40's commit; rev. 3, I-07) — the comment is corrected in the
  commit that makes it true. Replace "The live fold emits `act.ineligible` and `act.refused` as BODY LITERALS, which
  invariant 7's derived kind roster refuses at `append` …" with "Every row declares its refusal kinds, per clause
  (eligibility, each named conjunct, the write, the obstacle); the fold's body literals `act.ineligible`, `act.refused`
  and `attempt.refused` are gone (REM-40), and `state/log.py::append` refuses any kind outside the derived roster
  (REM-41)."
- **E-14 · P2:182** — "realm: only `restore` executes (19)" → "realm at HEAD `b70b5af` (aperture 2 0): `restore` 0/27,
  `migrate` 1/118, `transfer` 1/47, `found` 0/24, `build` 0/19, `work` 0/82 — no settlement-management verb executes; the
  owners are REM-22, REM-29, REM-2A and ED-IN-0297".
- **E-15 · P1 §3 rows IN-09 (:256) and IN-33 (:266)** — batch `none` → `RB-2b (REM-2B)`; and P5:47, :114 likewise.

### 4.2 Layer 0 and Layer 1 edits — listed in one place; agent-landed in the named PR (D-1 RULED yes, 2026-10-21)

**Jordan's ruling of 2026-10-21 (D-1):** an agent may land unmarked `CLAUDE.md` and `architecture/` text in the PR,
stated openly; anything marked (RULED) stays Jordan's.
- So every row below lands as a hunk of the item PR it names, and that PR's body lists it under "Layer 0/1 hunks".
- **None of the rows edits (RULED) text.** Each builder checks this at the anchor before editing; a (RULED) mark found
  there stops that row, and the row returns to Jordan.
- The rev. 3 conditionality on DEF-9, L0-1, L1-1 and L1-3 is removed.
- **Pairing (kept):** DEF-9 and L0-1 are one change in RB-4a's PR (the deletion, its `FORK:` row and §5's sentence).
  L1-1 and L1-3 ride REM-40/41's PR; L1-6 and L1-7 ride REM-44's PR.

| id | file:anchor | proposed text | kind |
|---|---|---|---|
| L0-1 | `CLAUDE.md` §5 ("`engine/engine_params/params_tables.yaml` is a frozen, no-longer-regenerable, ungated capture…") | in the same change as DEF-9's deletion (RB-4a's PR): "`params_tables.yaml` was retired (`FORK:` row in `references/restructure_ledger.md`); it was a frozen capture of prose tables, and its degree bands were superseded by `degree_from_net`." | precedent (NERS X3: "not RULED" text) |
| L0-2 | `CURRENT.md:27` (the **Threadwork** row, today `threadwork_v30.md` + `thread_horizontal_integration_spec.md`) | the head re-points to its code owner `systems/threadwork/sim/coherence.py` (NERS G7; G8's rule: a quarantined head row points at its code owner) | precedent |
| L1-1 | `architecture/meta/04_CODE_ARCHITECTURE.md` §F.20b (`:1169`), PART D row 25 (`:1040`) | after REM-40/41 land: "⚠ CLOSED at v9 REM-40/REM-41 (`<sha>`): every row declares its refusal kinds, the fold's body literals are deleted, and `state/log.py::append` refuses a kind outside the derived roster." | precedent (04's own in-place amendment form) |
| L1-2 | 04 §C.2 (`:596-611`), §B.13 #6 (`:494`) | already IN-44's row (P8:426): the tenth basis `warrant`, `determination`'s widened kinds, `RELEASABLE_KINDS` | precedent (carried) |
| L1-3 | 04 §B.13 (`:523`, "Grade: MECHANICAL, all twelve") | "⚠ At HEAD `b70b5af` invariants 5 and 7 have no check (`write_matrix.yaml` has no `writer:` column; `state/log.py::append` checks no kind). Their grade is CONVENTION until built; invariant 7 is built at REM-41, invariant 5 is unscheduled." | precedent (04 §0: a grade claimed above what is built is the F9 defect) |
| L1-4 | `architecture/meta/01_AXIOMS.md:301-302` (AX-7, "No state is hidden from the player") | narrow to Jordan's verbatim (`:299-300`), which §C.11 satisfies: "What narrows is the OPTION SET; the player keeps their own beyond-game understanding." (NERS G6 (ii)) | agent-landed (D-1): it narrows the gloss to Jordan's own verbatim; checked for a (RULED) mark at the anchor first |
| L1-6 (rev. 4) | 04 §B.10 (`:452`, `Sensation := (subsistence, standing)` and its GDScript `Vector2` note) and §C.3 (DELIBERATE's "two scalars", `:643`) | in REM-44's PR, citing Jordan's ruling of 2026-10-21 (option B): "`Sensation := (standing)` — one scalar, which raises at its point of use until a design supplies it; `subsistence` was removed (L1-6, option B, 2026-10-21). A settlement's hunger reaches a person as a claim (01 §D.10)." §C.3: "two scalars" → "one scalar" | agent-landed (D-1); rests on the ruling |
| L1-7 (rev. 4) | `architecture/meta/01_AXIOMS.md` §D.10 (`:1121`, "a **need** \| a `Sensation` plus a Query") | in REM-44's PR: "a **need** \| a Query (for a settlement, `world_q.hunger`, REM-50) plus the claims a person holds about it (L1-6, option B, Jordan 2026-10-21)" | agent-landed (D-1); rests on the ruling |
| — | 04 §C.11 `explain` | no edit: unbuilt by decision until its first reader (DEF-6) | — |
| — | 04 §A.2 `decision/` may-read | no edit: classes ride `Question.classes`, a declaration the column already admits ("the table's declarations") | — |

---

## 5. Measurement protocol, and the before/after readings each batch owes

### 5.0 Standing rules for every reading

- **Environment, once per session:** `git rev-parse --short HEAD`; `cat .git/shallow` (shallow → `git fetch --unshallow`
  before REM-2B and any `FORK:` row, `CLAUDE.md` §2); `python tools/session_provision.py`. Every run is prefixed
  `PYTHONHASHSEED=0`.
- **Seeds:** 0, 1 and 2 for any figure a commit or a `measured:` paragraph claims (the B-X precedent). Seed 0 alone only for
  a hash-equality control.
- **TEST HORIZON (P1 §0.5, RULED 2026-10-13):** a probe ends at the first season in which a verb errors. Every class this
  plan fixes errors in season 1 (realm: 491 refusals in season 0). So each before/after per-verb reading is `aperture 1
  s`. `aperture 2 0` is run once, only to tie the new base to this session's `SP/aperture_2_0.txt` (the control that the
  instrument reproduces the scan). `aperture 4 0` runs only where propagation is the question: R-04's and R-05's
  `measure:` readings at RB-3b's exit.
- **The base is re-taken on each batch's base commit**, never quoted from an earlier batch (P3 §B "pre-change read on the
  base commit"; `CLAUDE.md` §0.1 pt 3, a run that happened, not a command that exited).
- **Each claim names its control.** A count without a control is not a measurement (`CLAUDE.md` §0.1 pt 4).
- **`register --requirements` exit 0 is a syntax check, not acceptance** (`harness/register.py:657-715`). Every
  `measured:` paragraph a batch writes is read by that batch's Opus critic against the printed figure before the close.
  That read is the gate (rev. 3, I-06).
- **The suite runs once per batch, at its close** (`CLAUDE.md` §0.4): `python -m pytest tests/valoria -q -n auto`, plus
  `engine/season/tests` where the batch reaches it. Mid-batch, only the covering file each item names.

### 5.1 The readings, batch by batch

| id | batch | BEFORE (on the base commit) | AFTER | control | owner of the number |
|---|---|---|---|---|---|
| M-1 | RB-1 | `aperture 2 0`: per-verb `att/ex/ref`; `ref` total 761 (realm) | `ref` total vs the scan's 984; `unrowed` count; refused-on table; never-emitted line | hash equal to base (aperture's control line); the scratch scan's per-class counts | REM-10, REM-11 |
| M-2 | RB-1 | `aperture 1 s`, s = 0, 1, 2: the new per-verb base for RB-2a (M-2b re-takes it on RB-2b's base commit) | — | hash equal to base at each seed | REM-11 |
| M-3 | RB-1 | `decision_spread --decisions` at s = 0, 1, 2: deciders 420/78, 424/74, 418/80 (HEAD; `requirements.yaml:1175`'s 429/69 and 425/73 have drifted) | split: tie 222 ×3; outvoted 198/202/196; pursuit 78/74/80; vectorless 37 | `--null` (no `pursuit` top) and `--control` | REM-12 |
| M-4 | RB-1 | `corpus_run` `DEGREES RESOLVED` total | per-verb split; `BANDS THAT DIFFER`; `EMITS AND WRITES NOTHING` (13 rows expected) | per-verb sum = old total | REM-13 |
| M-5 | RB-1 | `storybar --draw-seeds` on `build_realm(0)` | differing chains across draw seeds | same draw seed twice → equal; constant-draw plant → no difference | REM-15 |
| M-6 | RB-1 | the relayed figures (§1.2) | each reproduced or marked unreproducible | the command that first produced it | REM-16 |
| M-7 | RB-1 | R-01/R-02 `11` re-take (P2 §11: 36 `wd_chunk` cells + `wd_collect`) | reconvergence at `2x3`, `none ≥ default` printed | `none` arm | REM-16 |
| M-8 | RB-2a/RB-2b, per item | `aperture 1 s` (M-2), the item's verbs: formed/att/ex/ref and refused-on | the same | the column removed (the base commit) | REM-22 … REM-2B |
| M-9 | RB-2a and RB-2b, each close | M-2 for all verbs; R-05 `WHERE THE 46 GO` | the same; wrong-kind (`exists:*=0`) total vs base (realm 2-season base: 512; re-based at 1 season by M-2) | base | batch |
| M-10 | RB-2b, close | M-7 | `11` re-take on RB-2b's tree (the second and last `11` run) | M-7 | batch (E15 precedent) |
| M-11 | RB-2b, REM-27 | `field.*` = 0 (both worlds, 2 seasons) | `field.won` + `field.lost` from REM-11 (iv)'s per-kind count line at `aperture 1 s` | the stamp term removed | REM-27 |
| M-12 | RB-2b, REM-29 | season-2 repeat share of (actor, destination) `migrate` refusals | the same | `test_migrate_capacity.py`'s existing refusals | REM-29 |
| M-13 | RB-3b | `aperture 4 0` (propagation: R-04, R-05 `measure:`) | the same, after IN-46 | IN-46 PLAYABLE off = AUTOMATED hash | REM-31 |
| M-14 | RB-4b | `act.ineligible` realm 31 / spine 1 (2 seasons) | 0; refusal kinds per row | REM-41's report-mode run finds no undeclared kind at seeds 0-2 and the corpus | REM-40, REM-41 |
| M-15 | RB-4a/4b | `content_hash` at s = 0, 1, 2 | equal (REM-42, REM-44, REM-46, REM-47); measured (REM-45) | base | each item |
| M-H1 | RB-5 | `hunger` bands by settlement, `census`, realm seeds 0-2 at 1 and 2 seasons, plus `scarce.governed`. Base this session (seed 0): every settlement fed after season 0, cover 21.7 → 41.7 seasons | the same with REM-51/52 | `hunger_reach` off and `body_step` 0 reproduce `89bc9c0ac2a0` (realm, 2 seasons) | REM-50 |
| M-H2 | RB-5 | the response: a harness-only sweep (never shipped) of the cohort weight (×1/×5/×10, capped at `capacity`) and of the per-head weight (×1/×5/×20), read as hunger bands, cohort deaths, cohort acts and lowest body at seeds 0-2 | hunger rising with population and falling with supply; deaths and acts differing from the hunger-off arm | the off arm (both fixtures at control) equals today's hash; the evidence JQ-6 is asked with | REM-50 … REM-52 |

**What each batch must write down:** the base and after figures, the seed list, the horizon and the control's reading, in
the commit body. A `measured:` paragraph in `requirements.yaml` only for a row the batch moves, and
`register --requirements` exit 0 after it.

---

## 6. Risks

| id | risk | where | mitigation |
|---|---|---|---|
| K1 | **Golden and pin re-records (rev. 3).** RB-2a: REM-22, REM-23, REM-24, REM-25, REM-2C. RB-2b: REM-27, REM-29, REM-2B, plus REM-26/REM-28 where a column is built. REM-30 (arm on). **REM-31: every seeded season that fights (P4:34; D-02).** REM-40: the realm's `act.ineligible` Events, plus the declared test and probe re-records (`test_season_shape.py:911, :5493`, `test_g1b_attribution.py:260`, `harness/probes.py:2795-2802`). REM-45 (`engine/tests`, [UNVERIFIED]). **Rev. 4:** REM-44 (a declared candidate mover through `_inputs_fingerprint`'s skip, measured at seeds 0-2); REM-51 (reach ON) and REM-52 (`body_step` 10: realm `89bc9c0ac2a0` → `2e699cfb8a15`, measured), with their re-pins in §2.5b.8: `test_in22_shortfall_reach.py`'s control, `test_territorial_subsistence.py`, the BASE_EVENTS pins in `test_in34_bodies_clock.py` and `test_season_weather.py`, and the realm hashes. Nothing verifies a re-pin was intended (`CLAUDE.md` §7) | §2.3, §2.4, §2.5 | one mover per commit, the old→new hash in the commit body, the falsifier run before the re-pin; `report` before `delta`, with the expected `PROBE FLIPS` stated (REM-41 (d)) |
| K2 | **File collisions** | `verb_table.yaml`/`rosters.yaml`: RB-2a, RB-2b, B-Q, B-R, B-Y, RB-4b; **`rosters.yaml` also B-V** (rev. 2, C-07: P3:342 "hardest: B-V against whichever of B-O…B-R is open"). B-V runs in parallel and merges before B-S (P3:183), so RB-2a/RB-2b merge first and B-V, the later to merge, re-runs its exit and hash control on the merged tree. **`verb_table.yaml`'s `march` row also B-T** (IN-52, P3 §B.1): REM-27 merges first, and IN-52 re-runs. `queries/world_q.py`: RB-2a, RB-2b, B-U, B-Y (`writs_held`, which REM-25 also edits), B-T. `data/requires.py`: REM-29, B-Y (`audience`). `harness/corpus_run.py`: RB-1, B-Q (`:875`). `harness/storybar.py`: RB-1, B-U. `modules/combat/*`, `seam/wrappers/combat.py`: B-Y, RB-3b. `modules/mass_battle/`: B-T (IN-52), REM-32. `state/carriers.py`: B-Q, B-S, RB-3a. **`manifest/registry.py` (rev. 3, D-08): RB-2a (REM-21 (v), `check_stampers`), then B-S (P3 §B.1), which re-runs under §C.2**. **Rev. 4, RB-5:** `loop/matter.py` (RB-5, then B-Q's IN-26, B-S's IN-35 and B-T's extractions, each re-running its hash control); `queries/world_q.py` and `rosters.yaml` (RB-5 merges before RB-2a); `data/fixtures.py` (RB-5; B-F closed); `harness/populated.py::census` (RB-5; B-V and B-T edit other functions of the file) | serial order in §2.8; P3 §C.2's merge rule (the second to merge re-runs its hash control); RB-2a's REM-25 edit to `writs_held` lands before B-Y, which re-reads it |
| K3 | **`give`** keeps its 24 wrong-kind refusals until B-R | C4 | B-R's `give` + Rung step reads the base (24/0) and owns the fix; the single-class column cannot carry Record and Rung |
| K4 | **Shared-class cross-formation (rev. 3).** `Record`: REM-25 and REM-2C with `comply`. `Rung`: REM-27 with `migrate` and `requisition`. The rows form on each other's stamps. **Plus the derived widening (D-06):** classing `march` widens `RUNG_REMIT_ACTS` to `{issue, dispatch}`, so `larders_in_purview` offers larders to dispatch holders | REM-25, REM-2C, REM-27 | each stopping rule (total wrong-kind refusals over the sharing rows must fall; `requisition`'s formed count read before and after); else revert. A per-row `referent_source:` column is built only on a measured need, at the batch critic's step-5 read **Rev. 4:** RB-5 adds no class and no stamp. Its hunger claim is a plain referent, so it is outside K4 by construction (§2.5b.7) |
| K5 | **COR 4** (`decision/options.py:822-826`): a classed row's operands read no claim the question is about, even when the id is also a plain referent. A row newly classed by REM-22 … REM-24 may lose an operand a document supplied | REM-22 … REM-24 | REM-24's control (`petition` executions ≥ the base); a fall is reported, and the item is reverted if the fall comes from a lost operand |
| K6 | **R-01/R-02 may fall** after RB-2a/2b, since fewer always-refused formations change what propagates | M-10 | the `11` re-take at RB-2's close; at ≥ 96 % the rows go `not_met`, and H-116 is named first (P2:75-77) |
| K7 | **R-06 gains a conjunct gated by ED-IN-0296 (2)** (E-8's fifth). Rev. 2 moved it here from R-08 (C-11) | REM-05 | declared; the gate existed, unseen. R-08 no longer waits on it. Revert path in REM-05 |
| K8 | **Un-meetable items.** REM-27 [CONFIDENCE: low]: a `Won`/`Lost` field needs a defended settlement of another faction in a marcher's ledger. REM-30/31 build on held designs by Jordan's 2026-10-21 ruling; a design defect found at build is recorded against the held design, not fixed in prose. `found`/`build`/`work` cannot execute before ED-IN-0297. REM-45's PP-624 exists only in `proposals/` (hand-verify there). REM-15 reads choice-driven chain variance only, since rolls stay keyed to `world_seed` (its recorded residue). REM-2B needs `--unshallow` | §2 | each carries its stop rule; a residue is named in the batch's HANDOFF line, and no position is widened to pass (P1 §0.5) |
| K9 | **REM-41 raising in a path no seed exercised** (ENCOUNTER, CENSUS at other seeds, the corpus) | REM-41 | report mode first at seeds 0-2 and the corpus; any undeclared kind declared at its owner first |
| K10 | **Budget.** Rev. 2's RB-2 ⚠ ~160k whole is split (I-08): RB-2a ~95k, RB-2b ~110k whole | §2.3 | two sessions, each with its own base reading |
| K11 | **A reclassification read as progress.** REM-25 moves `found`/`build` "always refused" → "never attempted", and REM-10 moves contested verbs the other way | R-05 | every R-05 reading after RB-1 states both moves beside the class counts (E-3's caveat) |
| K12 | **Draft numbers drift** before the batch opens (B-X's 429/69 → 424/74 already did) | all | §5.0: re-taken on each base commit, never quoted forward |
| K13 (rev. 4) | **Hunger ships ON and binds almost nowhere** at today's magnitudes (cover 21.7 → 41.7 seasons). Its visible effect in the realm is the season-0, pre-yield starvation of all 37 cohorts | REM-51, REM-52 | stated in the verdict; JQ-6 asks for the ratio. Reverts: `hunger_reach` off, `body_step` 0 |
| K14 (rev. 4) | **A crossing with no write is silent:** an unstocked town that never had a larder write deposits no hunger claim | REM-51 | registered as H-160 registers it for shortfall; the body-write attachment covers it once `body_step` > 0 |

---

## 7. What this plan deliberately does not do, and why

- **It does not make THE NINE `met`** (§0's confirmation table, row by row). R-06 and R-09 wait on Jordan (JQ-1,
  ED-IN-0296 (2), J-13 with JQ-2). R-08 waits on its own reading and possibly on cell values. R-05 waits on ED-IN-0297.
  R-04, R-05 and R-07 still need measured executions this plan cannot promise (K8). R-04 conjunct (1) has no item.
- **It records Jordan's three rulings of 2026-10-21** (D-1, D-2, L1-6) and decides nothing beyond them. The one [ASSUMPTION] it adds (the designs stay held under ED-1094) is stated with its revert.
- **It answers no Jordan question.** τ, capacity and its scope, the cohorts, works, the roster, the design ratification (JQ-5, optional), hunger's magnitude (JQ-6) and the four
  magnitudes stay his. Each
  is drafted with its ladder and evidence (§3).
- **It adds no guard whose subject is process,** no checker over §A.2, no instrument beside the four existing ones
  (`aperture`, `corpus_run`, `decision_spread`, `register --requirements`) plus `storybar`, which already exists. Every
  measurement lands at its single owner (`CLAUDE.md` §0.1 pt 5; `layer-conformance` A3).
- **It creates no standing document and no directory beyond this proposal's own.** Its text lands in v9's parts, and
  these files are then deleted with a `FORK:` row. It writes no `needs_jordan` ledger row (`CLAUDE.md` §0: not a parking space).
- **It does not widen a position to make a falsifier pass.** Every RB-2a/RB-2b item carries a stopping rule, and every
  realm-count figure is recorded, not required (P1 §0.5).
- **It does not fix the scratch scan's "last read" heuristic in scratch.** It moves the reading into `aperture`
  (REM-11), where it is reproducible.
- **It does not special-case a verb or an outcome.** Each formation fix reads the row's own columns
  (`referent_class:`, the cell's `existence` kind, `held_by`, `remit:`) or a roster (`march_target_kinds`), never a verb
  name. The two exclusions (`give`, `move`) are decided by a measured conflict, not by preference.
- **It does not build `explain`, invariant 5, the handoff rules, the THE BAR ordering, or the FI-03 trail** (DEF-2,
  DEF-3, DEF-4, DEF-6, DEF-11): none is on an M1 conjunct, and `CLAUDE.md` §0 scopes session work to Jordan's asks and
  M1 junctures.
- **It does not touch `.designs/`, `.audit/`, `mc_v18`, or a Godot version** (P1 §0.5's "must NOT" list).
- **It does not edit Layer 0 or Layer 1.** §4.2 is proposed text for Jordan's merge.
- **It does not run the full suite or edit the repo now.** The readings it cites are this session's scratch runs at HEAD
  `b70b5af` and the report's; each batch re-takes its own base (§5.0).


---

## 8. Mechanical self-check (rev. 4; read-only, re-runnable: `python3 SP/selfcheck.py v9_remediation_plan_rev4.md`)

Run after writing. The script's output, in substance:

| check | result |
|---|---|
| §0's count: "40 items in 7 batches" | 40 / 7 |
| `**REM-nn ·` item headers in §2.1-§2.5b | 40, all unique |
| §2.9 index rows | 40; header set == index set (no difference) |
| per batch | RB-0 8 · RB-1 7 · RB-2a 6 · RB-2b 6 · RB-3 3 (REM-32 rides B-T's tail) · RB-4 7 · RB-5 3 = 40 |
| every REM id cited anywhere exists in §2.9 | yes, except the three RETIRED ids, which are cited only to say they are retired: REM-07 (folded into REM-16), REM-20 (folded into REM-40) and REM-43 (cut, DEC-11) |
| confirmation table's items per row == §2.9's R rows, both ways | no mismatch for R-01 … R-09. R-03 is "—" in both. REM-51 is on R-04, R-06 and R-08 in both. Items that move no row read "—" in §2.9 |
| §2.6's kinds == realm §D ∩ spine §D from `SP/*_undefined.json` | 47 == 47, identical sets |
| hunger measurements (scratch scripts under `SP/hunger/`, read-only) | `body_step` 0 reproduces `89bc9c0ac2a0` (realm, 2 seasons, seed 0); `body_step` 10 gives `2e699cfb8a15` and a lowest cohort body of 940; cover 21.7 → 41.7 seasons; IN-22's live-arm tests 3 passed |
