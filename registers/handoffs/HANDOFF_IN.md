# Handoff — IN (Infrastructure / Cross-Cutting)

## ⚠ CLOSED WORK LIVES IN `HANDOFF_IN_closed.md` — index, 2026-09-13 (`ED-IN-0221`)

**Finished narrative moved out of this file**, verbatim and in
order, by a predicate that reads each unit's body rather than its heading (the predicate, and why
heading markers were not trusted, are stated in that file's header). **The split is proved
lossless** — the two files' line multisets partition the original exactly.

**Nothing here needs doing.** The index exists so that a standing order inside finished work is one
file-open away instead of buried. **`!` marks a unit containing imperative language** (`Do not` /
`Never`) — check those before acting in their area.

|---|---|---|
| **!** | 7,008 | ⭐ DONE 2026-09-07 — decomposition STEP 4: `state/carriers.py` + `state/world.py`. `shape.py` 5,165 → 4,146 (ED-IN-0203 |
| **!** | 2,215 | ⚠ CURRENT — 2026-09-04, PR #368: the season loop can now branch, and by how little (read this first) |
| **!** | 1,663 | ⭐ DONE 2026-09-07, LATER — FAN-OUT IS OFF `total`. `R7` executed in the season loop (ED-IN-0205) |
| **!** | 1,542 | ⭐ DONE 2026-09-07 — `shape.py` decomposition steps 0b–3 (ED-IN-0203, PR #378) |
| **!** | 1,161 | 2026-08-28 — Systems integration master (PR #337, branch `claude/gameplay-actions-scales-fb6ahu`) |
| **!** | 895 | ANCHOR — Progression scaffolding (2026-08-15/16, session `claude/valoria-progression-systems-5rdj94`, PR #315) |
| **!** | 749 | W3 DELETION REHEARSAL — EXECUTED 2026-08-04 (ED-IN-0144). Read before any W7 slice. |
| **!** | 145 | Next actions :: - **Filed, not acted on:** `tests/sim/mass_battle/config.py` ships `PC_CELL_MORALE` default `'1'` |

**SECOND PASS, 2026-09-17 (`ED-IN-0238`) — +10 units · 3,809 tokens, rows appended to the table above.** (3,809 is measured on the bodies AS THEY SAT HERE; the per-row counts are measured on the moved copies and sum to 3,813 — one trailing newline per unit, not a discrepancy to chase.) The predicate was WIDENED to match case-INSENSITIVELY: the 2026-09-13 pass matched `awaits`/`awaiting` in lower case only, and `**Awaiting Jordan, not self-ratified:**` in the 2026-08-01 gates section slipped it — four sections would have been moved with live items inside. ⚠ AND ONE FALSE NEGATIVE SURVIVES THE WIDENING, so pin by name before re-running: *"a faction becomes buildable and readable, and three items are Jordan's"* declares an escalation set without using any marker word. ⚠ **AND A THIRD PASS MUST READ STRUCK MARKERS CORRECTLY.** `ED-IN-0239` closed four entries whose subject is retired by striking the stale marker rather than deleting it (history stays visible). A struck `~~needs_jordan~~` / `~~awaiting Jordan~~` STILL MATCHES the marker predicate, so those four read as open to a naive re-run: **a marker inside `~~…~~`, or one on an entry carrying a `⛔ CLOSED` note, is not an open item.** **The closed-work lever is now SPENT** — of 84,745 tokens here, only these 3,809 moved; the rest carries live markers.

---

**The full 74-row table of contents now lives in `HANDOFF_IN_closed.md`'s own header** — an archive's index belongs in the archive. The imperative-flagged rows stay above, because a standing order must not need a second file-open to be seen.

## 🧾 2026-09-17 — THE FIRST EXECUTION PASS OVER THE BUILD ORDER (`ED-IN-0246`, PR #414)

**Facts, not a queue.** Three items of `proposals/2026-09-17-governance-and-behaviour/01_THE_BUILD_ORDER.md`
were RUN. `§7` of that file is the record and `probe_execution_pass.py` beside it re-takes every number.

- **Item 3b LANDED, AT ITS CONTROL ARM (`ED-IN-0247`, `H-125`).** A body finally falls: the
  shortfall reaches `Person.body` through the gate, `_crossings` is factored for **sites and
  persons** off the one `band_floors` table, and `World.remove_person` is `_eff_kill`'s cascade with
  MATTER and RESOLVE as its two callers. EXECUTED at `body_step=10`: bodies fall 30/season, cross
  800 at season 7, **and `budget` drops 5 → 4 in the same season** (the write reaching the reader).
  ⚠ **SHIPPED AT `body_step = 0`** because **all 86 buildable corpus worlds hold ZERO stores** while
  258 persons live in them — any nonzero arm starves every case world and moved 19 tests. Proof it
  is inert: `TRACE.txt` and `results.json` come back **byte-identical**. ⚠ **NEEDS JORDAN: the
  magnitude**, and choosing it needs a world that stocks a larder — plus the second question it
  raises, that **nothing restores a body**, so any nonzero arm is monotone decay at person scale.
  ⚠ **Two plan claims died:** the morale write-sweep does **not** cover `engine/season` (its root is
  `systems/mass_battle/sim`), so `Person.body` does *not* inherit that guard for free and none was
  added; and `LB-3c`'s literal `grep -c "t.until = w.tick" == 1` is wrong — the count is 5 and four
  are legitimate per-verb closers.
- **Item 3a LANDED — the larder ladder.** `world_q.nearest_store` + `matter`'s draw per EATER, not
  per rung. Before it, **4,810 units sat at the 37 settlements, 0 at the 211 hearths, every person
  lived in a hearth, and 0 rungs had both eaters and stores** — the subsistence step ran and wrote
  nothing. After: **13 rungs written, unmet subsistence 138 → 0**, and `MW-1`'s four predictions all
  held exactly. ⚠ **The draw bites in SEASON 2, not season 1** (§25 puts larders before yield, so
  season 1 draws against a world that has produced nothing) — a one-season probe reads this item as
  dead. ⚠ `World._subsistence_shortfall` is **item 3b's input**.
- **Item 16 LANDED.** `hold`'s domain/codomain are rosters (`hold_subject_kinds` / `hold_object_kinds`);
  `World._refuse_bad_hold` + `World.class_of` read them. The 16 faction-subject province holds are
  re-homed to persons. **`in_holdings` went from false for EVERY (person, rung) pair in the world to 15
  true pairs over 4 holders** — `revocation: "holdings"` is satisfiable for the first time.
- **It needed a repair the plan did not price.** `provinces_of` implements a RATIFIED ruling
  (`scale_hierarchy_v1.md` §2, provinces cohere under a common FACTION holder) by reading the holder off
  the `hold` edge; the re-home emptied it **silently** (4 factions → `{}`). New `faction_holding` Query
  derives the faction through the holder's membership `commit`, preserving the ratified sentence.
  **A carrier change is not local to its writer** — `world_q.py` is not in `05 §A.3.7`'s file list.
- **Item 1 is HELD, and its headline claim is retracted.** `@effect_for("commit")` runs
  (`resolvable_verbs()` 18→19) and a populated season measures **`commitment.made 0 / refused 42`**: no
  question source offers a Proposition referent. It is gated on items 5/7/8 and re-scheduled to Phase 2.
- **Item 4 is REVERTED.** Deleting `budget_office_bonus` starves the news transport — tellings fall
  **26 → 12 of 27** NPC rung cases, tripping `test_r7_m6`'s floor, because `corpus_run.py:254` seats
  offices. It is gated on the **S26.3 design call** `hole_register.yaml:176` owns in three shapes.

⚠ **`H-92` IS LIVE ON `main` ONCE #414 MERGES.** A landholding buys scene actions: the Crown's head
budgets **12** against a releasable ceiling of 5. Inert by the ceiling, reachable for the first time,
and the same design call as item 4.

⚠ **PHASE 6 IS SCHEDULED** at `01` §7.5 (6a–6g), its four gates having been ruled; **S9/S10/S11** (the
migration verb, `capacity(w, rung)`, `ED-IN-0210`'s fourth ledger row) are scheduled there too.

⚠ **TWO CONSTRAINTS RULED BY JORDAN IN SESSION, now `01` §7.1 and binding on every remaining item:**
no hard-coding (roster · table · `Fixtures` — the three homes that already refuse), and **no term of
`score(c)` may become a name in `loop/`** (measured: `loop/driver.py` imports 18 names from `decision/`;
phase 6 would make it 26).

---

## 🧾 2026-09-17 — THE BEHAVIOUR LAYER: established facts, so the next session does not re-derive them

**PR #409. Why this unit exists:** the session that produced it inspected files 566 times and **298
of those were re-reads of something it had already opened** — `rosters.yaml` 36×, `verb_table.yaml`
19×, `choose.py` 17×, H-71 four separate times. There is no context between sessions (§1), so a fact
established and not written down is a fact the next session pays for again. **This is that
write-down. Read it before grepping `engine/season/` for how a character decides.**

**The live decision pipeline is FOUR PHASES, not a scoring function:**

| | phase | owner |
|---|---|---|
| Φ1 | OCCASION — what am I asked about | `queries/world_q.py:159` → `decision/questions.py:45` |
| Φ2 | APERTURE — what could I coherently do | `decision/options.py:35` (four clauses, none a score) |
| Φ3 | APPRAISAL — how do I rank them | `decision/choose.py:302` (three terms) |
| Φ4 | COMMITMENT — what do I spend on | `_sample_order` → `pack_scenes` → `ask_budget()` |

## 🧾 2026-09-17 — THE SEAM: #408 and #409 collide in eight places (`ED-IN-0243`)

**Sibling to the unit above, and read it second.** That one establishes how a character decides;
this one establishes **where the governance suite and the behaviour layer touch each other.** The
proposal is `proposals/2026-09-17-governance-and-behaviour/` — `00` for the findings, `01` for the
order, `RULINGS.yaml` for the 21 questions. **Nothing has run; nothing ratified.**

**Facts established, so they are not re-derived:**

| fact | where |
|---|---|
| `resolvable_verbs()` = **18** of 38 table rows | `loop/driver.py:72`, executed |
| `in_holdings` is **False for every person × rung** — all 19 person-holds are on Offices, all 16 rung-holds are faction-subject | `build_realm(0)` + `predicates.py:99-102` |
| question sources after one populated season: `claim_landed` 583 · `need` 405 · `date_due` **0** · `band_crossed` **0** | instrumented over 230 `questions_for` calls |
| the six `Person` interior rows are `class: "ACTS"`, **not** `INTERIOR` — the only `INTERIOR` row is `(Person, claim_ledger)` at `[WIT]` | `write_matrix.yaml:14-17` (the loader asserts the derivation), `:147-209` |
| the teller of a `told_by` claim is **`_act.actor`, in scope at `witness.py:316`**, discarded by the constructor at `:361-363` | read in full |
| `standing_of` returns the **1000 max-gap default for all 12 persons** because its `told_by` input is empty | `decision/options.py:443-465` |

**⚠ Three traps for whoever builds next:**

1. **`(Person, body)` is NOT person-interior.** It is `[MAT, RES] MATTER/ACTS`. A session reading
   `STR-1` as a blanket prohibition will block r2 item 3b for no reason. **The six `ACTS` rows are a
   licence nobody has taken up** — that is what closed `STR-1` at gate step 3.
2. **r2's `EXECUTION_PLAN` cites `engine/season/loop/budget.py` twice and that file does not exist.**
   The live reader of `band_floors["body"]` is **`engine/season/decision/budget.py:73`**. Filed, not
   patched — §0.05 cl.3 makes it r2's.
3. **A lane ledger is append-only and last-row-wins.** Grepping one and taking the FIRST hit reads a
   superseded status as current; it produced three stale citations across the two subject suites,
   including `ED-WR-0011`'s pairing rider on `RR-2`, **which its own later row already discharged.**

**Next actions — and there are only two, both Jordan's:**

- **Nine ruling requests**, consolidated from two sheets into one at `RULINGS.yaml`'s
  `escalation_summary`: `CAT-6` · `STR-2` · `STR-5` · `STR-6` · `RR-P` · `RR-A` · `RR-B` · `RR-C` ·
  `RR-2`. **Only `CAT-6` and `RR-A` block a build item** (items 11 and 13).
- **Everything else in r2's plan is buildable today** — 13 of 16 items, item 1 first at ~12 lines.
  **No session needs to re-open the seam to start.**

---

## ✅ 2026-09-17 — ALL NINE ESCALATIONS RULED (`ED-IN-0244`, `ED-IN-0245`)

**The `ED-IN-0243` queue is empty.** Jordan ruled all nine in session. Detail per row:
`proposals/2026-09-17-governance-and-behaviour/RULINGS.yaml`. **Do not re-open these as questions.**

| | ruled |
|---|---|
| **RR-P** | **`AX-7` added to the ratified axiom set** — see `01_AXIOMS.md`, and read its scope clause before citing it |
| **RR-A** | **fold** `comply` / `evade \| defy` / `refract` / `dispatch`; compliance is the executor's own act. **Unblocks r2 item 13** |
| **RR-C** | withdrawn — closes at gate steps 3/4 |
| **CAT-6** | **arm 2**, the Tenure payload. *"Too noisy for a character to have assailable/uncertain remits"* |
| **RR-B** | B-8 descendants only · B-4 withdrawn · B-6 follows RR-A · B-1 keep `scope?` · B-2 keep the operands · B-3/B-5 take r2's · B-7 nominal rung + purview by class |
| **STR-5/6** | `conviction` = **religious affiliations and their intensities**, a vector; confliction **derived** |
| **STR-2** | axes are `memory` · `substantive` · `equity` · `selfish` — the register had the wrong four. **The thirteen are superseded** |
| **RR-2** | matter **plus hearth capacity**; `found` is the throttle; **migration is a verb persons take** |

### ⚠ What the rulings OPENED — four pieces of design work that did not exist before

1. **An affiliation roster and an incompatibility relation.** `conviction` is now a vector over
   creeds. MEASURED FINDING: `ED-IN-0075`'s `Truth` (0–5, Solmund-orthodoxy ↔ Thread-truth)
   **structurally cannot** carry Jordan's case — a midpoint on a pole scalar reads as *lukewarm about
   both*, not *conflicted between two strong commitments*.
2. **A migration verb.** MEASURED: nobody in Valoria can relocate. `move` is TRAVEL (a `travel_leg`
   Tenure alter); `residence` is a contested claim predicate **with no writer anywhere**.
3. **The 13-roster re-authored**, and the 13×N projection with it. `selfish` is measured near-inert
   across the current roster because self/other was factored out into `orient.self_other`.
4. **H-71's second half is still open** — arm 2 closes the holder's own knowledge of his remit, not
   *being understood by others as seated*.

### ⚠ And `AX-7` makes three shipped deposit sites a CONTRADICTION, not a preference

`witness.py:191`, `:271` and `:361` are the only production sites that construct a `Claim`, and all
three hand a character the engine's own resolution as true. Under `AX-7` that is not a design to
revisit. **The machinery to fix it already exists** — `agreement`, `standing_of`, `belief_contradicts`
and the testimony ladder all presuppose divergence; only the producers hand out certainty.

---

## ⚠ OPEN MARKERS IN MOVED UNITS — the index, 2026-09-17 (`ED-IN-0240`)

**Every unit carrying an open marker was moved to `HANDOFF_IN_history.md`** — the rows below are the complete list with the rest of the pre-generation narrative. **Their markers are reproduced here VERBATIM**, so an open item is a table row plus one file-open away instead of buried inside a multi-thousand-token session section — that is the safety claim of this trim, and it is stronger than a move without an index.

⚠ **A MARKER HERE IS NOT A LIVE ITEM UNTIL SOMEBODY CHECKS IT.** Every row predates the current generation (2026-09-13); many sit inside units whose own headings read `[DONE]`, `[RULED]` or `[LANDED]`, which is the defect Jordan named: *"if there are that many live markers in a handoff, then there is a problem with those markers remaining current."* Work the five-step gate in `CLAUDE.md` §0 down this table — superseded · irrelevant · answered by a document · answered by precedent · answered by the architecture — and close each row with its citation. **Closing rows here is session work; preserving them is not conservatism.**

| newest date | markers carried | unit |
|---|---|---|
| 2026-09-12 | `BLOCKED` `HELD` `needs_jordan` | 📐 2026-09-12 — v1: seven research documents NERS-audited (`ED-IN-0217`, PR #399, merged) |
| 2026-09-12 | `HELD` `awaits` `needs_jordan` | 2026-09-02 (third entry) — **H-35 RULED BY JORDAN. THE ESCALATION QUEUE IS EMPTY. |
| 2026-09-10 | `BLOCKED` `needs_jordan` | 📋 2026-09-10 — the `needs_jordan` queue measured, and three of this pass's own conclusions retra |
| 2026-09-10 | `BLOCKED` `HELD` `⏸` | ⏸ ARC 2 / G1 — HELD 2026-09-10. A real game defect found, RULED, implemented, measured, and BACK |
| 2026-09-08 | `DEFERRED` `HELD` | ⭐ DONE 2026-09-08 — decomposition STEP 5: `queries/` + `loop/`. `shape.py` 4,153 → 3,121 (ED-IN- |
| 2026-09-07 | `HELD` `needs_jordan` | ⚠ CURRENT — 2026-09-06, ED-IN-0202: eight design rulings recorded, and the one thing to build fi |
| 2026-09-05 | `needs_jordan` | ⚠ CURRENT — 2026-09-05, ED-IN-0202: a reference for future sessions, and eight false self-claims |
| 2026-09-02 | `HELD` | 2026-09-02 · The season loop was TESTED BY EXECUTION, and a successor architecture exists |
| 2026-09-02 | `BLOCKED` `HELD` | 2026-09-02 (second entry) — PR #354 ADJUDICATED, AND THE IMPROVEMENT PLAN |
| 2026-08-28 | `HELD` `needs_jordan` | 2026-08-28 (session close) — precedent companion, ED-IN-0201, and the harvest provenance |
| 2026-08-27 | `needs_jordan` | 2026-08-27 — contracts, centralized and hierarchical (ED-IN-0200) — RULED, NOT EXECUTED |
| 2026-08-23 | `BLOCKED` `DEFERRED` `HELD` `STILL OPEN` `SUSPENDED` `needs_jordan` | 2026-08-23 — S6 CLOSED except 6c; S7 is next |
| 2026-08-21 | `HELD` | PORT NOTE — this branch is to be absorbed into PR #313 (`claude/review-commits-workplan-7x4q4g`) |
| 2026-08-17 | `BLOCKED` `needs_jordan` | 2026-08-17 — Weekly code review `d36498f`..`f2fc307` + full instrument sweep (ED-IN-0194) |
| 2026-08-14 | `HELD` `needs_jordan` | 2026-08-14 — Jordan's ruling session: all 10 calls RULED; 4 executed, 1 part-built, 5 not starte |
| 2026-08-13 | `HELD` | [RULED] ED-IN-0179 — Jordan: there is no `deprecated/` conflict, and the real lesson is about vo |
| 2026-08-13 | `BLOCKED` `HELD` `needs_jordan` | [DONE] ED-IN-0173/0174/0175 — Wave 1+2: the merge's own compliance debt, and G2 CLOSED (2026-08- |
| 2026-08-12 | `BLOCKED` `HELD` `[OPEN]` `awaiting` | [OPEN] ED-IN-0159 — code-leanness census + a 4-phase consolidation plan (2026-08-11) |
| 2026-08-12 | `BLOCKED` `HELD` | [DONE] ED-IN-0166/0167/0168 — Track G continued: ED-IN-0162 executed, G3, G9 (2026-08-12) |
| 2026-08-12 | `HELD` | [DONE] ED-IN-0178 — Wave 3: the alias plan's foundation EXECUTED, and a control the plan never r |
| 2026-08-11 | `BLOCKED` `HELD` | Next actions :: - **[OPEN — BLOCKED ON JORDAN] Canonical nomenclature plan written (2026-08-11). |
| 2026-08-11 | `HELD` `[OPEN]` | [OPEN] ED-IN-0150 — generated per-subsystem glossary + master term index (2026-08-08) |
| 2026-08-11 | `BLOCKED` `[OPEN]` | [OPEN] ED-IN-0158 — consolidation sweep: 8 opportunities, 3 candidate findings killed (2026-08-1 |
| 2026-08-10 | `HELD` `[OPEN]` | Next actions :: - **[OPEN] ED-IN-0152 — subsystem flow skeletons exist for all 15 `systems/` fol |
| 2026-08-09 | `BLOCKED` `HELD` `[OPEN]` | [OPEN] ED-IN-0148 — post-evacuation vector audit + the GM Resolution Register (2026-08-06) |
| 2026-08-08 | `BLOCKED` `HELD` `[OPEN]` | Pending :: - **[OPEN] ED-IN-0149 — world-churn audit: the machinery is built and DISCONNECTED (2 |
| 2026-08-03 | `DEFERRED` `HELD` `STILL OPEN` `needs_jordan` | 2026-08-03 — Fork Plan of Record rewritten to execute after two read-only Fable-5 passes (ED-IN- |
| 2026-08-03 | `DEFERRED` `HELD` `awaiting` | 2026-08-01 — Four gates that could not see what they guard (ED-IN-0115..0119, PR #284) |
| 2026-08-03 | `BLOCKED` | Next actions :: - **I1 (get `main` green) is CANON-BLOCKED, measured not assumed.** 60/60 identi |
| 2026-08-02 | `BLOCKED` `HELD` | 2026-08-02 — The repointed-path pattern, guarded (ED-IN-0122, PR #284) + a planning failure wort |
| 2026-07-29 | `HELD` `[OPEN]` | Pending :: - **[OPEN] ED-IN-0091 — code-shape open-items register + orchestration plan (2026-07- |
| 2026-07-29 | `DEFERRED` `HELD` `STILL OPEN` | Pending :: - **[LANDED] ED-IN-0097 — W4 landed, bookkeeping AFTER the critic (2026-07-29).** `04 |
| 2026-07-29 | `[OPEN]` | Pending :: - **[OPEN] ED-IN-0094 — fractional-resolution triad, RULED (Jordan directive, 2026-07 |
| 2026-07-29 | `STILL OPEN` `needs_jordan` | Pending :: - **Ecosystem-review Top-5 residuals not covered by their own lane.** Filed 2026-06-3 |
| 2026-07-22 | `BLOCKED` `HELD` | Next actions :: - **Incompleteness Ledger + audit de-cull (2026-07-22, PR #205)** — the vectoriz |
| 2026-07-14 | `needs_jordan` | Next actions :: - **WS0 Structural Observatory + WS1 registry reader (2026-07-13/14, ED-IN-0057. |
| 2026-07-14 | `needs_jordan` | Next actions :: - **Observatory Remediation Program filed (2026-07-14, ED-IN-0066 — renumbered o |
| 2026-07-12 | `DEFERRED` `needs_jordan` | Decisions :: - 2026-07-12 — **Skills-ecosystem staleness remediation, "Phase 7" (ED-IN-0044..004 |
| 2026-07-08 | `needs_jordan` | Pending :: - **Resolution Plan v1 — Stratum-C armature deployment §6.3 wave 3 (consumer/contract |
| 2026-07-08 | `needs_jordan` | Pending :: - **Resolution Plan v1 — Stratum-B THIRD SLICE 2026-07-08: ED-PC-0005 dead-code inves |
| 2026-07-07 | `needs_jordan` | Pending :: - **Unaddressed-areas comprehensive audit — DELIVERED 2026-07-07 (ED-IN-0017, this PR |
| 2026-07-07 | `needs_jordan` | Pending :: - **Edge-playability audit — RATIFIED IN FULL 2026-07-05 (Jordan: "Ratify all", post- |
| 2026-07-07 | `DEFERRED` `HELD` | Decisions :: - 2026-07-07 — **Consolidated ruling pass on the Key & Echo armature §5 docket + ed |
| 2026-07-05 | `HELD` `awaiting` | Pending :: - **Emergent Narrative Engine design v1 — DELIVERED 2026-07-05, awaiting Jordan revie |
| 2026-07-05 | `HELD` `needs_jordan` | Pending :: - **Narrative engine v2 "THE CHURN ENGINE" + Master Workplan v6 + steering reconcilia |
| 2026-07-04 | `DEFERRED` `awaiting` | Pending :: - **Qualitative NERS audit (North-Star) — DELIVERED 2026-07-04, awaiting Jordan revie |
| 2026-07-02 | `needs_jordan` | Decisions :: - 2026-07-02 — **`ED-<LANE>-NNNN` lane-tagged editorial namespace created (`ED-IN-0 |
| 2026-06-30 | `BLOCKED` | Decisions :: - 2026-06-30 — **Adversarial ecosystem review + safe fixes.** Ran a 72-agent verifi |
| 2026-06-29 | `needs_jordan` | Decisions :: - 2026-06-29 — **ED-citation integrity: full reconciliation (292 → 0; gate now BLOC |
| 2026-06-28 | `DEFERRED` `needs_jordan` | Decisions :: - 2026-06-28 — **Editorial-ledger relevance triage.** Deep per-item verification of |
| 2026-09-17 | `HELD` | 2026-09-17 · ROUND TWO of governance-and-holdings (`ED-IN-0233/0234/0235`) — PR #408 |
| 2026-09-17 | `HELD` `needs_jordan` | 2026-09-17 · The governance-and-holdings suite (`ED-IN-0236`, `ED-IN-0237`) — PR #408 |
| 2026-09-16 | `PARKED` | ⚠ ID COLLISION RESOLVED HERE — `ED-IN-0228`, 2026-09-16 |
| 2026-09-16 | `HELD` | 🧭 2026-09-16 — the decision layer interrogated: twelve inputs, one of them live (`ED-IN-0228`) |
| 2026-09-14 | `HELD` `STILL OPEN` | 2026-09-14 — the creed lands, and the axes turn out to have had two owners |
| 2026-09-14 | `BLOCKED` | 2026-09-14 (later) — M1 row 5 has an instrument, and it found something on its second seed |
| 2026-09-14 | `BLOCKED` `SUSPENDED` `needs_jordan` | 2026-09-14 (later still) — M1's remaining two rows, characterised precisely |
| 2026-09-13 | `HELD` | ⚠ CURRENT — 2026-09-13 (later), PR #404: the governance layer is BUILT, and two rulings closed t |
| 2026-09-13 | — | ⚠ CURRENT — 2026-09-13, PR #404: a faction becomes buildable and readable, and three items are J |
**Measured, and each cost a run to establish:**

- **Q4 `need` IS the ambition mechanism** — a live `commit` Tenure to an OUGHT Proposition. It leads
  for **12/12 persons at genesis and 0/12 in every season after**; `claim_landed` grows to 136–180
  while `need` stays at 12. `q_rule = one_per_source` restores its reach to 12/12. One word.
- **The aperture is bounded twice.** ~25 candidates per referent, linear — but **28 distinct verbs
  under every aggregation rule**. More referents buy more candidates and no new KIND of action.
- **10 of 38 verbs are unformable person-side** — every governance verb (H-71), plus `destroy_record`
  (H-75/H-33, *not* H-71). ⚠ **`hole_register.yaml:806` still says "9 of 32" and is STALE** — the
  tree has 38, verified directly. The owner is wrong and the downstream copies are right; fixing the
  owner is a live-registry edit nobody has made.
- **`P(inversion) = 1/(1 + e^{Δ/τ})`** at `_sample_order`, verified against 200,000 draws per row.
  At the shipped `τ = 0.1` a term decides at 95% only when **Δ ≥ 0.294**; the measured live plateau
  gap is **0.0000**. ⚠ **`choose.py:318` runs the sampler AFTER the score sort** — a session that
  reconstructs the ranking with `sorted()` is measuring the wrong stage, and one did.
- **580 claims after two seasons, 100% `firsthand`.** `tell` **resolved 9 times and deposited 0**, so
  `standing_of` returns the maximum-gap default (1000) for every person, permanently.
- **`Person.marks` is read by NO Python; `capability` is read once as a dice source** where the
  fixture states *"Rank supplies dice and gates nothing"*. `stance` holds **0 rows** in a built realm.
- **H-62 in one line:** six loop steps, four carry refusal laws against a Person social write,
  DELIBERATE writes nothing — only RESOLVE remains, i.e. only an act, and no verb does it. Pressure,
  scar, needs, fear and stance production are **one problem, not five**.

**Open for Jordan, in the register's `ruling:` fields** (`proposals/2026-09-16-conviction-decision-layer/adjudication_register.yaml`):
STR-6 (what `conviction` means once reserved for piety, and the person/territory `piety` collision),
STR-1 (the Person-interior write path), CAT-7 (caste intrinsic vs the contested `heritage` claim the
tree already built). STR-5 is the `belief` vocabulary conflict — six live senses, measured.

---

## ⛔ 2026-09-16 — THE KEY SUBSTRATE IS RETIRED (`ED-IN-0232`, RULED by Jordan)

Verbatim: *"Anything key-based gets retired."* This answers the question `ED-IN-0227` left open and
it is DONE, not in progress. **Nothing here needs doing; this unit exists so the next session does
not go looking for a bus that is gone, and so the three things it genuinely cost are on the record.**

**What is gone** — 25 exact `FORK:c6e82105` rows in `references/restructure_ledger.md`:
`engine/substrate/keys.py`; `engine/cross_scale/{echo_transport,articulation,parliamentary_bridge}.py`;
`engine/engine_params/{key_types,module_contracts}.json`;
`tools/{export_key_types,build_key_graph,build_contract_index,contract_runtime_conformance,export_module_contracts}.py`;
the `emits:`/`consumes:` interface and the `articulation_layer` row in `references/module_contracts.yaml`;
two blocking CI validator rows and the report-only Module-Contract Conformance job; 13 test modules
and `tests/valoria/_campaign.py`.
`engine/substrate/__init__.py` now holds no code — it was a pure Key re-export, which is why
`import engine.substrate.descriptors` used to load the whole substrate on a head that emits no Keys.

**Why it was cheap, measured before anything was deleted** (the ED-IN-0227 lesson about mentions vs
dependencies was applied first): 12 files imported `keys`, 8 named a symbol it owns, and the
110-module transitive closure was an artifact of that `__init__`. The bus had ONE production host —
`engine/mc_v18.py` under `ECHO_TRANSPORT` — and three emitters, two of them log-only telemetry whose
removal left the seed-42 n=8 win-share byte-identical while `keys_emitted` fell 180 → 99.

**⚠ THREE THINGS IT COST. Do not read a green suite as evidence any of these still works:**

1. **`structure_audit`'s L2 graph has ZERO edges**, and the vector audit's fifth graph
   (`build_g_key`) returns `{}`. Both derived their entire wiring model from the emit/consume
   interface. `references/module_contracts.yaml` is also back to having **no exporter** and so no
   destination for a new reader — the migration-backlog framing that arrived 2026-08-24 is void.
2. **`directional_coverage_v1.md`'s "all seven Key-delivery directions are exercised" is no longer
   backed by anything.** Fifteen tests in `engine/tests/test_pipeline_reach.py` covered it; ten
   non-Key tests survive in that file.
3. **281 line-numbered anchors from archived flow skeletons into live code are now ADVISORY**
   (`tests/valoria/test_flow_skeletons.py::RETIREMENT_SHIFTED`). The 306 symbolled anchors stay
   binding. They were NOT put in `LINE_UNSTABLE_TARGETS`, which demands a symbol: that set would
   have failed all 281 in frozen documents nobody may correct.

**Goldens moved, and the destination was already in the tree.** `mc_v18`'s campaign fell back to the
`ECHO_TRANSPORT`-off arm — `{'Crown': 62.5, 'Church': 12.5, 'Hafenmark': 0.0, 'Varfell': 25.0}`,
which `engine/tests/test_echo_transport.py` had asserted byte-exactly until it retired in the same
commit. Both arms were recorded before anything was deleted, so this is a predicted move landing
where it was predicted. `GOLDEN_SCENES_RESOLVED` 1072 → 407 (the §10 vote was bus-gated).

**NEXT, and it is not this unit's:** Jordan, same session — *"mc_v18 is being fully retired."*
`ED-IN-0227` holds that. This change deliberately did NOT start it: it removed mc_v18's Key wiring
and re-pinned its goldens only as far as keeping CI green required. The roster went 16 -> 10
(`tests/valoria/test_mc_v18_is_deprecated.py::ALLOWED_IMPORTERS`, counted from the tuple, and the
AST scan in that file finds the same 10). The three non-test importers left — `balance_oracle`,
`campaign_output_probe`, `trace_execution_phases` — are all tools, not shipped engine code.

## Pending

- **[OPEN] ED-IN-0086 — handoff skeleton+infill+archive contract.** `tools/handoff_atomize.py`
  landed; not CI-wired, not yet run on a lane. Held on 2 Jordan calls. 5 lanes carry live items
  the banner counts as settled.

- **[OPEN] Same-lane ED collisions are a pattern, not an accident.** 0085→0086→0087 across PR
  #245/#246/#247 in two days. §3's lane split killed *cross*-lane collision by construction;
  *same*-lane still rests on discipline, 0-for-2 with two sessions on one lane. Remedy
  (reserve-on-branch / CI-visible id-claim) is a governance call — observation only.

- **✅ SessionStart open-work surfacing DONE (2026-07-22, ED-IN-0081).** Closed the "audits /
  editorial / schema / mechanics keep getting missed at session start" gap. New
  `tools/session_open_work.py` composes a `── open work ──` banner block — active-lane
  `HANDOFF_<LANE>.md` pending items (lane inferred from working-tree + recent-commit paths via
  `obs_core.infer_lane`; settled bullets filtered via `build_decisions.RESOLVED_SKIP`), open
  editorial debt + the `needs_jordan` inbox, schema-in-flux flags, and ALL stale audit families
  (was top-2). Wired into `session_status.py` (the superseded top-2 audit call removed);
  defensive-by-contract (degrades to `[]`, never breaks session start); test at
  `tests/valoria/test_session_open_work.py`. Also landed **CLAUDE.md §0 "How we work"** — the
  standing method doctrine (plan-first / bottom-up-from-primitives / adversarial-pass / max-effort /
  honest loop-closure), distinct from §10's fan-out-only patterns. Routines deliberately out of
  scope (remote-layer, not git-readable from a hook). *Follow-up candidate:* a per-lane mechanics
  "inert count" line if `mechanics_index.yaml` gains a cheap inert flag (currently only its
  staleness is surfaced, via the audit family). **⛔ CLOSED 2026-09-17 (`ED-IN-0239`): THIS ENTRY WAS NEVER `needs_jordan`** — the marker predicate matched its narrative mention of *the `needs_jordan` inbox*, a false positive in the opposite direction from the ones `ED-IN-0238` records. Its subject is retired regardless: §0.3 retired the banner and forbids a replacement, and `tools/session_open_work.py`, `tools/session_status.py` and `tests/valoria/test_session_open_work.py` are all absent from the tree (checked), so the *Follow-up candidate* line has no subject either.

- **Resolution Plan v1 — Stratum-C (armature deployment) FIRST SLICE 2026-07-08: ED-IN-0028, echo-transport
  plumbing ("proceed large build").** **⛔ CLOSED 2026-09-17 (`ED-IN-0239`): SUBJECT RETIRED** by `ED-IN-0232` — `sim/cross_scale/echo_transport.py`, the substrate `TickScheduler` and the `scene.*_resolved` Key path are gone, and `sim/` is itself a dissolved tree (§3). Its `DEFERRED` items were deferrals on that mechanism. ⚠ The lane EDs it names (`ED-SC-0006/0007`, `ED-FA-0005`) are UNTOUCHED and remain their lanes' business. Executed the IN-lane core of Key & Echo Armature §6.2. New
  `sim/cross_scale/echo_transport.py` un-orphans `domain_echo.py` (was a ZERO-caller C-REACH island) and
  routes a resolved scene → `domain_echo` (degree-keyed) → one `scene.*_resolved` Key via the substrate
  `TickScheduler` with an OF-7 **deferred** faction apply at the ACTION→ACCOUNTING boundary. Wired into
  `scene_dispatch._resolve_slot` (closes `zoom_out({})`) + `mc_v18` (world-scoped KeyLog; `key_log_hash`/
  `keys_emitted` telemetry), behind an `ECHO_TRANSPORT` flag (default OFF = byte-exact, MB FIELD_MOVEMENT
  precedent). Flag-OFF **and** flag-ON win-share both byte-identical to the F7 seed-42 golden; OF-7/degree/
  replay proven in `sim/tests/test_echo_transport.py` (9 cases); 396-pass sim regression green. **DEFERRED
  (owning lanes, nothing dropped):** SC context-derivation bridge (ED-SC-0006/0007) makes scenes resolve →
  live loop is INERT today (KeyLog born empty-deterministic; F7 named-zero-assertions stay 0 by design and
  flip when the bridge lands); FA comeback (parliamentary_vote-in-loop) is ED-FA-0005; §5.5 RNG fork not
  engaged (domain_echo deterministic). NEXT armature waves = §6.3 PR-3+ (keying / down-seam / rendering).

- **Key & Echo Armature v1 — DELIVERED 2026-07-07 (ED-IN-0018, this PR; deliverable 2 of 2,
  ~~needs_jordan = its §5 fork docket~~).** **⛔ CLOSED 2026-09-17 (`ED-IN-0239`): SUBJECT RETIRED** by `ED-IN-0232` — the armature's executable half (`sim/substrate/keys.py`, 24 tests) is gone and nothing may be built on it, so its §5 fork docket has no subject. ⚠ **The docket's NON-Key items are NOT closed by this** and keep their own ids in their own lanes: `ED-SC-0002`, `ED-SE-0002`, contest live-dispatch, ER-2 band-discipline scope, CI 75-vs-80. The `ED-IN-0012/0013` double-allocation renumber it lists IS settled — `references/id_reservations.yaml` records the renumber to `ED-IN-0019/0020`. `designs/architecture/key_echo_armature_v1.md` (seam
  contracts + Echo Matrix all-directions/all-scales + §3 registry deltas + A13-A16 conformance
  specs + the consolidated §5 docket — **merge does NOT ratify §5**) + the first executable Key
  substrate (`sim/substrate/keys.py`, 24 tests) + `tests/contracts` wired into CI. Staging:
  PR-2 = flag-gated echo wiring + the F7 smoke oracle; PR-3+ = per-lane shaping waves (armature
  §6.3). The §5 docket consolidates: OF-D6/OF-3/OF-7/OF-B1/RNG-COLLISION/ORD-3/ORD-4/OF-CAP,
  ED-SC-0002, ED-SE-0002, the ED-IN-0012/0013 double-allocation renumber (ledger lines 597-600),
  CI 75-vs-80, ER-2 band-discipline scope, contest live-dispatch.

## Decisions

## Next actions

- **J-36 — Key-bus closure for the 6 off-bus writers**, gated on the distillation report's deferred
  adversarial pass. Design-tier docket item ~~awaiting Jordan~~ — **⛔ CLOSED 2026-09-17 (`ED-IN-0239`): SUBJECT RETIRED.** `ED-IN-0232` retired the Key substrate on Jordan's ruling *"anything key-based gets retired"*, so there is no bus to close and no off-bus to be off. Checked rather than assumed: `keys.py` and `echo_transport.py` are absent from the tree, and the three live files still naming `echo_transport` name it only in comments. Nothing left to decide; see also `registers/handoffs/HANDOFF_SC.md`'s J-31
  (social-contest deliberative-game findings) — the two were tracked together in root `HANDOFF.md`
  before the 2026-07-08 per-lane content split.
