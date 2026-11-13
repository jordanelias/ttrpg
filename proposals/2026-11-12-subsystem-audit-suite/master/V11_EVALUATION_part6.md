# Evaluation of workplan v11, part 6: lane E1, carry-forward blocks (verbatim)

## Status: EVALUATION RECORD, assembled (stage 5 of `STAGES.md`; reference, resolves nothing at runtime, CLAUDE.md §0.05; deleted when workplan v12 is adopted)

**What this part is.** The carry-forward blocks of lane E1, copied by script from `master/eval/E1.md` lines 3506 to 4445, byte for byte; nothing below the rule was retyped or edited. Line numbers cited in the settlement ledger (`V11_EVALUATION_part2.md`) are those of the lane file, so a row of this part is found there as `E1:<line>`. Where the ledger re-dispositions a row, the ledger governs and the copy below keeps the lane's original call as the record.

---

### GO-06

card row (`valoria_master_workplan_v11_part3.md`):

```
| GO-06 | cross-repo: `valoria-game`'s parity reader against the shrunk `MAPPING`; the stale `game_constants.json` sentence; gains GO-01's `engine_series`/`schema_version` item | HELD · BLK:`valoria-game` checkout (another repository: the parity run is done, the hand refresh of the port's copy is not) | E | — | — | carried in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part5.md:216-227`):

````
### GO-06 — cross-repo: `valoria-game`'s parity reader against the shrunk `MAPPING`; the stale `game_constants.json` sentence (GO) · BATCH B10-20 (listed, HELD · BLK; moved from B10-Z) · STATE BLK:`valoria-game` checkout (another repository: the parity run is done, the hand refresh of the port's copy is not) · R —
- WHAT: the coherence reshape retired the `COHERENCE_*` pairs from `tools/export_game_constants.py`'s `MAPPING`. Confirm `valoria-game`'s `tools/check_constants_parity.py` (or equivalent) tolerates a smaller `MAPPING` rather than a fixed constant count, and that its generated `game_constants.json` stops carrying the sentence that named a deleted module. GO-01 adds one item: the reader learns the new `engine_series` key and the bumped `schema_version` (1 → 2). "Nothing here edits the other repository."
- LANDED ALREADY: the reshape on this side (WR); the parity reader's tolerance of a smaller `MAPPING`, run at PC-12 against a scratch copy of `valoria-game@6b0df3d`.
- REMAINING UNBUILT: the hand refresh of the port's `resources/generated/game_constants.json` (another repository); GO-01's `engine_series` key when it lands.
- GATE: a `valoria-game` checkout. DEPS WR (the reshape); EDITS none here.
- EXIT and FALSIFIER: EXIT "here, `python tools/export_game_constants.py --check` exit 0; there, its parity check run against this repository's re-derived constants." FALSIFIER "its parity check, run against a `MAPPING` smaller by the retired pairs, fails if it assumes a fixed count; a pass with the pairs present proves nothing about the smaller set."
- HASH MOVERS: none.
- HOLES AND LEDGER IDS: none. (SOURCE row "Port-bridge constants-parity risk from the coherence reshape" in `registers/handoffs/HANDOFF_WR.md`.)
- ASKS ATTACHED: none.
- RE-BASE: none found. The version is ED-GO-0002's (GO-01 writes it to its owner); this entry asserts nothing beyond GO-01's key. B10-20's exit line 9 (Jordan's side) reads this item.
- SOURCE: `v9_p7:108-113`; state-index row `v9.md:291`.

````

### NM-W6

card row (`valoria_master_workplan_v11_part3.md`):

```
| NM-W6 | fragment bake | HELD · UNBUILT | E | — | — | `proposals/2026-10-13-narration-mechanisms.md` §4 |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:292-307`):

````
### NM-W0 … NM-W9 — Narration packages (IN/WR) · BATCH B10-19 (NM-W0: B10-02, CLOSED, an EDIT whose row left at B10-02's close; NM-W2: B10-05, CLOSED, an EDIT whose row was deleted at B10-05's close; NM-W3: B10-01, an EDIT whose row is deleted in the adoption commit) · STATE as listed · R M2 (the any-seed story bar)
Home: `proposals/2026-10-13-narration-mechanisms.md` §4 (W0-W9). The proposal is PROPOSED, grade `paper`; nothing in W1-W9 had code, a test or a run when it was written. It names four decisions for Jordan (§7 there); they are in `-05`. Premises are one seed, two seasons.

| handle | package | state at HEAD | note |
|---|---|---|---|
| NM-W1 | render v0: an omniscient instrument chronicle (ranking tiers, appraisal, name fallback, per-person pages, anti-repetition, snapshots) | PARTLY LANDED | IN-37 (`bd5d5b45`) landed a narrower `harness/chronicle.py` (numbered lines of actor, verb, emitted kinds); W1's fuller specification was not diffed against it; [UNVERIFIED] whether v9's D1-b #1 is IN-37's render. **The story-telling fold of 2026-11-02 (ED-IN-0311):** the ranking-tier piece moves to CR-68 (B10-10, landed `eddcca8b`); NM-W1 stays HELD · PARTLY LANDED for its remainder (appraisal, name fallback, per-person pages, anti-repetition, snapshots), whose first step is still the diff against IN-37 and which has no consumer until a player seat (CL-SLICE / NM-W5) exists; NM-W4 to NM-W9 unchanged |
| NM-W2 | candidate-typing disposition: refusals as learning versus declined at formation | CLOSED INTO B10-05 | M19 taken (a), decline at formation row by row (`-05`); REM-21 to REM-25 decline at formation; REM-29 is the learning channel for capacity; DEC-12 keeps `finding.none` off the ledger. Its measured arm is `-08` HR-9's control (4); the row was deleted at B10-05's close with that reading quoted in the close commit `1d6cd152`'s body (default cross-person share read literally fails on seeds 0-4, 27.0% against 29.4%, taken on the executed-only share, 19.3% against 17.8%) |
| NM-W4 | a content-bearing record kind | UNBUILT | needs W2 and a working handover (`give` was attempted 14 times and executed 3 in the three seeds). PR #506's G-04(b) is a note here, not a new position: act-minted Propositions have predicate `''` in 52 of 52 (the narration proposal's figure, which the register reports and did not re-measure), so a `covenant` on one binds nothing; HELD with this package |
| NM-W5 | focalized journal on `person_q` | UNBUILT; released from M12 | M12 taken (a) in substance, without the §A.2 row; held on NM-W1 only; the amended entry is below the table |
| NM-W6 | fragment bake | UNBUILT | |
| NM-W7 | scale lines | UNBUILT | |
| NM-W8 | occasion ladder (replacing a per-season deck) | UNBUILT | decision 2 in `-05`: none, authored boot-time rows, or a per-season emitter |
| NM-W9 | conformance items (`Receipt.before/after` against 04 §B.9, and others) | UNBUILT | "not a narration dependency"; hash and golden moves declared |

**NM-W5, amended by the decision round** (B10-19; released from M12). Home: `proposals/2026-10-13-narration-mechanisms.md` W5, with the §A.2 row struck from its "Where" and "Co-edit" lines. NEEDS: NM-W1 (NM-W2 is discharged at B10-05). It slots by R8 into the next unopened code batch after NM-W1 lands its instrument control; it cannot slot earlier. HASH: EQUAL, asserted: `content_hash()` of `build_realm(0)` over two seasons is equal with and without a journal call per person per season. FALSIFIER: W5's three, the control for (1) being the instrument's field count over the same focalizer (above 0) against the journal's 0; plus a covered actor's act reaching the focalizer with `seen.who = None` prints unattributed (planted failure: `actor_of` passed in reddens). The no-row reading holds only if the journal reads what `person_q` may read (`04_CODE_ARCHITECTURE.md:169`); W5 also selects from Scenes (narration proposal `:283`): if Scenes are not person-side, the §A.2 row is owed and lands with NM-W5 as a Layer 1 hunk listed under "Layer 0/1 hunks" (M11 answered (a), ED-IN-0300; an unmarked anchor only `[ASSUMPTION; medium; Jordan to correct; revert: ED-IN-0300 reopened]`). `skills/prose-writer/SKILL.md:158` is narrowed in NM-W5's commit. BUILDER: `CLAUDE.md` §10's second tier. ASKS: M12 taken at step 5 ((a) over (b) on player experience; the Layer 1 half at step 4; (c) excluded by §C.11) `[ASSUMPTION; medium; Jordan to correct; revert: delete the function and test; restore the skill line]`.

````

### NM-W7

card row (`valoria_master_workplan_v11_part3.md`):

```
| NM-W7 | scale lines | HELD · UNBUILT | E | — | — | `proposals/2026-10-13-narration-mechanisms.md` §4 |
```

entry: see the block already copied from `workplans/valoria_master_workplan_v11_part4.md:292-307`.

### NM-W8

card row (`valoria_master_workplan_v11_part3.md`):

```
| NM-W8 | occasion ladder (replacing a per-season deck) | HELD · UNBUILT | E | — | — | `proposals/2026-10-13-narration-mechanisms.md` §4 |
```

entry: see the block already copied from `workplans/valoria_master_workplan_v11_part4.md:292-307`.

### NM-W9

card row (`valoria_master_workplan_v11_part3.md`):

```
| NM-W9 | conformance items (`Receipt.before/after` against 04 §B.9, and others) | HELD · UNBUILT | E | — | — | `proposals/2026-10-13-narration-mechanisms.md` §4 |
```

entry: see the block already copied from `workplans/valoria_master_workplan_v11_part4.md:292-307`.

### CL-THRUST

card row (`valoria_master_workplan_v11_part3.md`):

```
| CL-THRUST | The thrust layer: an ambition plus an authored ladder of typed stages (`goal_stages`) across ten axes, with no arc carrier (TL §1-§4, §6, §8 B0.1, B2-B6; PR #506 G-09, G-10, G-13, G-14, G-19, G-23, G-24, G-26, G-28); M20 taken (b) in part: B0.1 LANDED in B10-02; B2.x and B3.1 LANDED in B10-05 (`edb1e9d2`, `a397fa16`); B3.2 LANDED in B10-09 close two (`67f5b086`, `cf943457`) | the row: HELD (B4.x on `determine` and `covenant` executing; B5.2 on M1's residue; B6.n on content); B5.1 cut (M21) · each landed piece hash EQUAL at empty data | E | CR-10 (landed `1ef8d273`), CR-14, CR-15, CP-T02-01 (landed `f9e4cef`), IN-12 (landed `f9e4cef`), IN-61 (landed `f9e4cef`), CR-28 (landed `1ef8d273`); piece-level gates outside the graph (not a dependency): the `guards` flip under IN-36 (B5.2, HELD until the flip lands in B10-17, ED-IN-0317; the flip does not muster the guards before CP-T09-07 (b)) and a `covenant` and `determine` executing reading (B4.x, no owner) | M1's residue (B5.2) | `proposals/2026-10-25-thrust-layer/00_THRUST_LAYER_DESIGN.md`, `01_MISSING_IN_CODE.md` |
```

entry: see the block already copied from `workplans/valoria_master_workplan_v11_part4.md:308-316`.

### CR-38

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-38 | Court Parliament's bench (design-first): one design file under `proposals/` naming the derivation (the default it tests: the governance-ladder title seats whose rung lies inside the venue), its cost against the duchy-head `determine` grant, an arrangement-level bench key and the interim two-seat bench, and `parliamentary_debate`'s flip to `disposal: declared` | DESIGN-FIRST (drafted beside B10-13; approved before B10-18 closes, else on B10-20's freeze row with the interim bench named) | E (the design; its build M) | CR-36; not a dependency: CR-37 (the design states its falsifier against CR-37's specification) | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:253-265`):

````
### CR-38 — Court Parliament's bench (design-first) (IN/SC) · BATCH B10-19 (DESIGN-FIRST; drafted beside B10-13, approved before B10-18 closes) · STATE DESIGN-FIRST · R —
- WHAT: item 4 (make the endings reachable), the bench taken as design-first: Court Parliament has no bench of its own. At a realm venue `parliamentary_debate`'s bench is the King's and the Widow Regent's seats (`queries/world_q.py:475-481`), the interim two-seat bench. One design file names how a landed bench is derived, so that CR-34's tally can be flipped on at `parliamentary_debate`.
- LANDED ALREADY: the `parliamentary_debate` row; `judging_set`; CR-34's tally (landed `67f118dd`) and, by B10-17, CR-36's Record disposal site.
- REMAINING UNBUILT: one design file under `proposals/` naming the derivation, not authored seats. The default it tests: the holders of the governance-ladder title seats (`offices.yaml: titles.domains` posts) whose rung lies inside the venue ("Landed + distinguished service aristocrats", `worldbuilding_v30.md:180`), sitting by an assembly reading of the bench for a `parliamentary_debate` row. It states the cost of each route: (i) grant `determine` to the duchy-head seats (a remit edit that also lets them judge trials in their duchies, a mover on every duchy determination), or (ii) an arrangement-level bench reading (a fourteenth `arrangements.yaml` key, which the loader refuses today, `data/arrangements.py:73-75`); (iii) the interim realm bench is the third option. The same design flips `parliamentary_debate` to `disposal: declared` (CR-34's tally), and is the seating that H-90's "there is a Parliament" and the translation's named residue, the Parliamentary Stay (`-05` §1b), waits on.
- GATE: a B10-19 row. The design file is drafted beside B10-13 in a worktree (B10-19's card allows a worktree beside any code batch) and approved before B10-18 closes, by ED-1094's merge default unless its PR holds it back. Approved in time, its build (the bench reading it chooses and the `parliamentary_debate` flip) runs by R8 as its own sub-batch between B10-18 and B10-20; unapproved when B10-18 closes, it joins B10-20's freeze row as a declared post-freeze mover, with the interim two-seat bench (the King and the Widow Regent) named and frozen. NEEDS: CR-36 (its first reader). Not a dependency: CR-37 (the design states its falsifier against CR-37's specification).
- EXIT and FALSIFIER (for the design): it names a test in which a motion against the King is carried by a bench of at least two landed seats and refused by one, and a control in which the interim bench is kept.
- HASH MOVERS: EQUAL (a design file); its build a declared MOVER (either route moves every determination in the realm).
- HOLES AND LEDGER IDS: H-90.
- ASKS ATTACHED: item 4 (`-05` §1b) `[ASSUMPTION; medium; Jordan to correct; revert: delete the design; the interim bench stands]`. B10-19 members released later are post-freeze movers (`-03` B10-20).
- RE-BASE: re-read `judging_set` and the `parliamentary_debate` row by symbol on CR-36's landed tree.
- BUILDER: `CLAUDE.md` §10's third tier (judgment).
- SOURCE: `worldbuilding_v30.md:180` (intent); `data/arrangements.py:73-75`; `queries/world_q.py:475-481`.

````

### CR-66

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-66 | Membership contests: admission, expulsion, precedence (the `tribunal` row binds the order) | DESIGN-FIRST | E (design) | CR-60 | which bodies admit by contest is content (Jordan's) | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:621-633`):

````
### CR-66 — Membership contests: admission, expulsion, precedence (design-first) (SC) · BATCH B10-19 · STATE DESIGN-FIRST, then BUILD only on approval · R R-04 (contributor)
- WHAT: the `tribunal` row *binds the order* (`disposes: ban`) and a guild, an order or a council admits and excludes, yet no matter family holds it. Today admission is a self-sworn `oblige` (255 acts at seed 0). Design what contests a membership: the party (the applicant or the member), the disposal (`ban` for exclusion; admission is a `confer` or an `oblige` accepted), the bench, and what is witnessed.
- LANDED ALREADY: `tribunal`, `oblige`, `confer`, `establishment_of`.
- REMAINING UNBUILT: the design file.
- GATE: drafted beside B10-19; build only on approval. NEEDS: CR-60.
- EXIT and FALSIFIER: design approved by ED-1094's merge default unless held back.
- HASH MOVERS: none at the design step (E).
- HOLES AND LEDGER IDS: H-90.
- ASKS ATTACHED: content (which bodies admit by contest) is Jordan's, P11.
- RE-BASE: none.
- BUILDER: second tier (design).
- SOURCE: the build-all fold of 2026-11-02 (`proposals/2026-10-29-parliament-and-debate/2026-11-02-social-contest-build-all-plan.md`, with `2026-11-01-social-contest-matters-standpoints-and-fold.md`, whose probes are in that folder).

````

### CR-67

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-67 | Trade and levy: a market, a toll, a price, a tax (no verb exists beyond `requisition`) | DESIGN-FIRST | E (design) | CR-58 | which taxes exist is content (Jordan's) | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:634-646`):

````
### CR-67 — Trade and levy: a market, a toll, a price, a tax (design-first) (SC/SE) · BATCH B10-19 · STATE DESIGN-FIRST, then BUILD only on approval · R R-04 (contributor)
- WHAT: no tax or levy verb exists beyond `requisition` (parliament design §8), so a matter about a market, a toll or a tax has no disposal and no party. Design whether the matter is a motion about the holder of the market or the rung, what the owner's act is, and whether it needs CR-58's consent conjunct.
- LANDED ALREADY: `requisition`, `exchange` (CR-49), CR-58.
- REMAINING UNBUILT: the design file.
- GATE: drafted beside B10-19; build only on approval. NEEDS: CR-58.
- EXIT and FALSIFIER: design approved by ED-1094's merge default unless held back.
- HASH MOVERS: none at the design step (E).
- HOLES AND LEDGER IDS: H-163.
- ASKS ATTACHED: which taxes exist is content, Jordan's, P11.
- RE-BASE: none.
- BUILDER: second tier (design).
- SOURCE: the build-all fold of 2026-11-02 (`proposals/2026-10-29-parliament-and-debate/2026-11-02-social-contest-build-all-plan.md`, with `2026-11-01-social-contest-matters-standpoints-and-fold.md`, whose probes are in that folder).

````

### CL-OPEN

card row (`valoria_master_workplan_v11_part3.md`):

```
| CL-OPEN | Story openings drawn from pools at world build (role-bound goal rows plus a lawful seed, a Record held from build or none, on a seat or place), opened only by a person's own act; nothing drawn in a season | DESIGN-FIRST · RATIFIED (Jordan, 2026-10-30, ED-IN-0305); build HELD on M26; design approved before B10-18 closes; its build after CL-EVENTS commit (4) | E (design) | CL-EVENTS | M26 | `proposals/2026-10-28-content-architecture-suite/02_P1_templates.md`; `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:335-348`):

````
### CL-OPEN — Story openings drawn from pools at world build, opened only by a person's own act (WR/IN) · BATCH B10-19 (DESIGN-FIRST) · STATE DESIGN-FIRST · RATIFIED (Jordan, 2026-10-30, ED-IN-0305) · build HELD on M26 · R —
- WHAT: the reduced form of the suite's P1-B: a set piece is a bundle of role-bound goal rows plus a lawful seed (a Record held from build, or none; a seeded Claim would need AX-7 amended, `01_AXIOMS.md:263-267`, `:314-317`, and `corpus_run.py:255-260` refuses `knows:` for that reason), hanging on a seat or a place; each world draws a few bundles when it is built; only a person's own act ever opens the story. Nothing is drawn during a season and no clock emits an event (T-c; AX-5's three motions). A pool row may not carry a date, a deadline, a firing condition, an outcome, or a write to standing, a seat, a tenure or a stance (M20's line, as CL-EVENTS commit (3) already applies it to a card).
- N-LINE (V1): the drawn opening — cut it and the gameplay experience is worse, because two worlds built from one cast open on the same situations, so the stories the loop grows from them converge (Jordan, 2026-10-28, as the suite paraphrases him: "You said 100% emergence from characterization, office and faction will produce too many similar stories", `proposals/2026-10-28-content-architecture-suite/01_MAIN_REPORT.md:179`; his own words are owed a ledger row, `-10` §5 H-1). The object each step would otherwise use (at HEAD unless marked): CL-EVENTS commit (3)'s Tensions receiver (a card drawn once at build, its goal rows through `data/goals.py::parse`; after B10-18) and commit (4)'s six cards (after B10-18); `goals.yaml`'s seeded goal rows; a person's own acts to open. If the design finds the Tensions receiver with its schema widened (role-bound goal rows plus a lawful seed) is the whole of it, the row narrows to that widening and becomes a CL-EVENTS commit, not a new receiver.
- LANDED ALREADY: CL-EVENTS commit (1) (B10-05); commits (3) and (4) are B10-18's, switch off.
- REMAINING UNBUILT: the design (home below): the pool row schema, the draw rule and its size (how many bundles per world against the pool's size, so two worlds rarely share an opening), the source arcs each pool would draw on (the pool rows themselves are Jordan's content, as CL-EVENTS (4)'s choices are; B10-19's Must NOT forbids authoring a goal row or a card), and the plan-text amendments it would need, stated and not made here: `-07` §2's "the arcs" row ("no arc is a carrier, a card field or a loaded row" would read "a carrier or a loaded row; a row may quote one in `source:`") and the B10-18 build file's schema clause at `-09-build-B10-18.md`:183, which stands as written. A pool row's `opens_with` (an existing verb name) has a build-time reader or is cut: the loader VERIFIES it at build (the named verb exists; the attach point's holder is eligible for it) and refuses a bad row by its own message (the per-family loader refusal `CLAUDE.md` §0.05 licenses); no step of the season loop reads it, so `-09-build-B10-18.md`:277 ("read a card in any step of the season loop or add a World field for it" is forbidden) and :183 hold, as does `-09-build-B10-19.md`:95 (CL-THRUST's Must NOT: "deal arcs per season (the deck is world-gen only)"), since the draw is at build. ED-IN-0225 is not reopened: M20 (b) already narrowed it (`-06` part 4 §2), and a pool row quoting an arc in `source:` is not an arc carrier.
- GATE: a B10-19 row, DESIGN-FIRST, HELD on M26. Its design runs with CL-EVENTS' schema question as one producer (`-10` §2) and is designed and approved before B10-18 closes. Approved and answered, its build follows CL-EVENTS commit (4) (B10-18) and lands before the freeze if it is EQUAL at the shipped switch, else it is a declared post-freeze mover on B10-20's freeze row. NEEDS: CL-EVENTS (commits (3) and (4)).
- EXIT and FALSIFIER (for the build): the same seed twice draws the same bundles; a planted row with a `fires_at` key, an outcome or a stance write is refused by the loader by its own message; with the draw on, seeds 0-5, at least one bound person forms a candidate on each drawn bundle's object (the count asserted ≥ 1 per seed); no bundle's goal is acted on in a season unless a bound person's own act names it. CONTROL: the draw off reproduces the base hash. The reading, recorded and not a pass condition: STORY-BAR's chains on against off.
- HASH MOVERS: E (design). The build: EQUAL with the draw off; the on-arm a declared mover.
- HOLES AND LEDGER IDS: none allocated.
- ASKS ATTACHED: M26 (storyline form; `-10`); default in force: `-05` §1c.
- RE-BASE: re-read CL-EVENTS' landed loader and card schema, `data/goals.py::parse` and `seed_goals` by symbol.
- BUILDER: design `opus` (with CL-EVENTS' schema section, one producer, `-10` §2); build `sonnet`.
- SOURCE: home `proposals/2026-10-28-content-architecture-suite/02_P1_templates.md` §3 (P1-B; PROPOSED, held back in full); `-04` CL-EVENTS; `-07` §2 "the arcs"; `-09-build-B10-18.md`:183, :277; T-c (`architecture/meta/01_AXIOMS.md`, re-derive by quoted words).

````

### CL-PERSON

card row (`valoria_master_workplan_v11_part3.md`):

```
| CL-PERSON | The personality layer v2 (stored manner offsets, personality-only axes, per-person copies of global settings) and ED-IN-0304's risk appetite and decision horizon; stored offsets would contradict ED-IN-0261's ruled sentence (R7's dissolution clause; R7 = `proposals/2026-09-16-conviction-decision-layer/formal_analysis.md:195`), hence its stored-offset build HELD | DESIGN-FIRST · RATIFIED (Jordan, 2026-10-30, ED-IN-0305); build HELD on M34, M35, M36, M37, M40 and `-10` E-4 (stored offsets); design approved after CR-17's commit (2) (τ), its build after it | E (design) | CR-17 (landed `1ef8d273`) | M34, M35, M36, M37, M40, E-4 | `proposals/2026-10-24-character-layers-v2.md`; `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:349-362`):

````
### CL-PERSON — The personality layer v2, and ED-IN-0304's risk appetite and decision horizon (IN) · BATCH B10-19 (DESIGN-FIRST; its build after CR-17's last commit) · STATE DESIGN-FIRST · RATIFIED (Jordan, 2026-10-30, ED-IN-0305) · build HELD on M34, M35, M36, M37, M40 and `-10` E-4 · R R-08 (contributor), R-06 (contributor)
- WHAT: persons with equal pursuits choose alike (ED-IN-0261, ruled: projected axes are linear in pursuit weights, "two people with identical pursuits ARE identically disposed and the variation comes from the candidates", the sentence that dissolves R7; R7 itself is a result in `proposals/2026-09-16-conviction-decision-layer/formal_analysis.md:195`, not a clause of the ruling). The design (home below) adds manner that varies independently of values and leaves odds untouched: stored per-person offsets on some axes, new personality-only axes, and per-person copies of existing global settings; and it carries ED-IN-0304 (Jordan, 2026-10-29: persons differ in risk appetite and in a SHORT, MEDIUM or LONG decision horizon), whose undecided half (where appetite and horizon come from, what the risk term multiplies, how a horizon weights a later outcome, per person or per verb) is M40. **Stored offsets on those axes would contradict ED-IN-0261's ruled sentence (R7's dissolution clause; R7 = `formal_analysis.md:195`), which is why the row is HELD on `-10` E-4**: a ruled row is not overwritten by a plan.
- N-LINE (V1): per-person manner — cut it and the gameplay experience is worse, because two persons who want the same things are the same character to the player: neither boldness nor patience is visible in what anyone chooses. The shipped object each step would otherwise use: the chooser's score terms and τ (`decision/`; CR-17 re-derives τ), the persons' pursuit vectors, combat's per-person `Combatant.disp` (`modules/combat/combatant.py`), the global settings the traits would copy (`data/fixtures.py`). If τ at CR-17's last commit already makes equal-pursuit persons choose differently through existing terms, or M35's answer is that spreads cannot move a decision at that τ, the row narrows or closes (M35).
- LANDED ALREADY: the 15-pursuit roster and projected axes; `Combatant.disp`; CR-17 (B10-09 close two) is the series this row follows.
- REMAINING UNBUILT: the design (home below) restated against the tree at its start (its source digest is a reconstruction, and its figures are scheduled for re-measurement in `-10`); then its build.
- GATE: a B10-19 row, DESIGN-FIRST, HELD on M34 (`selfish_selfless` at spread 0 or stored), M35 (τ against trait spreads), M36 (the per-verb declared cells), M37 (the refusal gate's convention against one-signed axes), M40 (ED-IN-0304's residue) and `-10` E-4 (stored offsets on the projected axes; no stored offset is built until it is answered). Its design is approved after CR-17's commit (2) lands (τ; it chooses its spreads against the landed τ) and its build is sequenced after that commit, never before; CR-17's τ rule is re-applied after the row's first non-neutral value unless the design shows its terms leave the margins τ divides alone (`-10` M35). It replaces CR-17's FOLLOW-ON line (deleted with that entry at B10-09's close two). NEEDS: CR-17 (landed `1ef8d273`).
- EXIT and FALSIFIER (for the build): two hand-built persons with identical pursuits and opposite values on one new axis rank one exposed verb differently, and identically when the axis is zeroed; planted failure: the term dropped makes them rank alike. CONTROL: every new axis and trait at its neutral value reproduces the base hash at seeds 0-2.
- HASH MOVERS: E (design). The build: EQUAL at neutral values; a declared mover once a value is authored.
- HOLES AND LEDGER IDS: ED-IN-0261 (ruled; the sentence that dissolves R7), ED-IN-0304, ED-IN-0296; H-96 (τ), H-146 (the refusal gate).
- ASKS ATTACHED: M34, M35, M36, M37, M40 and E-4 (`-10`); defaults in force: `-05` §1c.
- RE-BASE: re-read the chooser's score terms, τ and the refusal gate by symbol on CR-17's landed tree.
- BUILDER: design `opus`, critic per `-10` (the lane where the producer is likeliest wrong); build `opus` (judgment on a shared primitive).
- SOURCE: home `proposals/2026-10-24-character-layers-v2.md` (PROPOSED, held back in full; reconstructed from a digest); `registers/editorial_ledger_in.jsonl` ED-IN-0261, ED-IN-0304; `-04` CR-17.

````

### CL-MGMT

card row (`valoria_master_workplan_v11_part3.md`):

```
| CL-MGMT | The management surface, weak reading (a batched front end over the seated person's own seat verbs; AX-1 unchanged); one owner of an order's cost, never a verb-row `management:` marker beside the Scene's | DESIGN-FIRST · RATIFIED (Jordan, 2026-10-30, ED-IN-0305); build HELD on M31 | E (design) | CL-SLICE | M31 | `proposals/2026-10-28-content-architecture-suite/01_MAIN_REPORT_part2.md` §13; `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:363-377`):

````
### CL-MGMT — The management surface: the seated person's own seat verbs, batched (IN) · BATCH B10-19 (DESIGN-FIRST) · STATE DESIGN-FIRST · RATIFIED (Jordan, 2026-10-30, ED-IN-0305) · build HELD on M31 · R R-04 (contributor)
- WHAT: Jordan (2026-10-28, relayed by the suite) asked for "an abstracted surface like a roster management menu" beside the person the player plays. The suite's final position is the weak reading: a batched front end over the seat verbs the seated person already holds, AX-1 unchanged ("only a person acts"; `04_CODE_ARCHITECTURE.md:853`, "for a player character the player IS the decision procedure"); an order writes exactly what its verb row writes. The strong reading (the player outside the world, issuing orders the engine executes) needs an amendment to AX-1 and §C.11 and is not this row's default.
- N-LINE (V1): the management surface — cut it and the gameplay experience is worse, because a player whose person holds a seat must spend that person's scenes one at a time on routine seat acts (`confer`, `requisition`, `transfer`, `issue`), so the seat is played as a queue, not managed. The object each step would otherwise use (at HEAD unless marked): the seat's remit (`offices.yaml`, `remit_unruled`), the verb rows' `writes:`, the scene budget and its release count (`decision/budget.py::budget`, `loop/deliberate.py`'s `scene_budget` reading), CL-SLICE's seat (after CL-SLICE). If the design finds the batched front end is a view over CL-SLICE's seat with no engine change, the row narrows to that and is CL-SLICE's.
- LANDED ALREADY: the seat verbs and remits; the scene budget.
- REMAINING UNBUILT: the design (home below), which must settle two things before a build: (1) which verbs are orders: the suite selects them by a `management:` marker on the verb row (its ORDER SELECTOR, `01_MAIN_REPORT_part2.md:98`; it keeps cost in the budget's one place, not in the marker); the design says whether the seat's remit already selects them, so no second list is kept, and names one owner of what an order costs; (2) whether orders are free of the scene budget: M31 (b)'s three arms (the player's person only, every person, the status quo; `-10` E-3). Freeing orders departs from Jordan's 2026-09-02 budget ruling (`decision/budget.py:19-20`, the function docstring) for whichever persons it covers, moves the hash if for every person, and sits beside `budget_office_bonus`, which already buys a scene per live `hold` that the release count cannot spend (H-92; `loop/deliberate.py:85-113`): two ladders for seat capacity unless the design names one owner.
- GATE: a B10-19 row, DESIGN-FIRST, HELD on M31. Its build is an R8 sub-batch after CL-SLICE's build and after B10-17's close two (which changes `confer` and `revoke`), before B10-20 (`-10` §3). NEEDS: CL-SLICE (the seat it batches).
- EXIT and FALSIFIER (for the build): per M31 (b)'s arm, as `-10` §2 CL-MGMT states them (the status-quo arm: scripted orders equal to the chooser's own seat acts reproduce `content_hash` at seeds 0-2; that falsifier cannot observe the every-person arm, which has its own); for every arm, each order writes exactly its verb row's `writes:` (asserted per verb on a hand-built seat); planted failure: an order that writes beyond its row reddens it.
- HASH MOVERS: E (design). The build: EQUAL under the weak reading with the budget unchanged; a declared mover if M31 frees orders of the budget for every person.
- HOLES AND LEDGER IDS: none allocated.
- ASKS ATTACHED: M31 (`-10`; (b) is E-3, three arms); default in force: `-05` §1c (the status quo).
- RE-BASE: re-read the budget and release count, and the remit lists of the seats the design offers, by symbol.
- BUILDER: design `opus`; build `sonnet`.
- SOURCE: home `proposals/2026-10-28-content-architecture-suite/01_MAIN_REPORT_part2.md` §13 (PROPOSED, held back in full); `architecture/meta/04_CODE_ARCHITECTURE.md:853`; `architecture/meta/01_AXIOMS.md` AX-1; `engine/season/decision/budget.py:19-20`; `engine/season/data/fixtures.py:532` (`budget_office_bonus`); `engine/season/hole_register.yaml` H-92.


````

### CR-92

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-92 | The social attributes acting on others: Grace on regard, promotion and the venue's standard; Presence on obedience; Attunement on bonds (ED-IN-0347) | DESIGN-FIRST | E (design) | CR-20 (landed `c7764a5a`), CR-84 (landed `1abaa612`) (B10-10, read); SC-02 (design written, PROPOSED), CR-83 (design) | the venue shortfall acting on the result, a take | written out in full: `-12` |
```

entry (`workplans/valoria_master_workplan_v11_part17.md:13-25`):

````
### CR-92 — The social attributes acting on others: Grace on regard, promotion and the venue's standard; Presence on obedience; Attunement on bonds (SC/IN) · BATCH B10-19 (DESIGN-FIRST; drafted after SC-02's and CR-83's designs are approved; its builds slot by R8) · STATE DESIGN-FIRST · R R-07 (contributor), R-06 (contributor)
- WHAT: AR-29, AR-31, AR-32 to AR-36a, AR-49, AR-50 (ED-IN-0347). How a person's Grace, Presence and Attunement change what OTHERS do and think: Grace makes others think well of him whatever his office's rank (AR-34) and so raises his chance of an office (AR-35); a formal venue requires Grace and penalizes its want even in a persuasive speaker (AR-36, AR-36a); Presence moves others (AR-29), including whether an order is obeyed; Attunement sets the likelihood that a tie or knot forms (AR-31). Today `regard` (`queries/person_q.py:397`) and `reception` (`queries/world_q.py:678`) read no attribute, `roll.py::obstacle` has no venue standard, `comply`/`defy`/`evade` carry no term from the issuer, and the knot oracle gates on Bonds (`systems/fieldwork/sim/knots.py:53, 200`), which the ten drop (adj §1, §2.2 (iv), (ix)).
- LANDED ALREADY: `regard` and its gains; `stance_term`'s `declared` regard of a candidate's subject (`decision/choose.py:55`), which carries regard into `confer` with no change to `confer`; `reception`; `arrangements.yaml`'s keys `interposed`, `order`, `floor`, `venue_min_rank`; by B10-10's close, the ten keys (CR-84) and `Person.attributes` (CR-20).
- REMAINING UNBUILT: (design) ONE design file under `proposals/`, no code, stating with a falsifier each: (1) **how Grace reaches regard** without a person-side reader of another's true attribute: the candidate door is WITNESS (the World may read the true value; the holder reads only what was deposited), the precedent CR-79's credit term; `layer-conformance` Lens B on AX-2 answered first; (2) **promotion**: confirmed through `stance_term`, no `confer` edit, or the design names why not; (3) **the venue standard**: the requirement read from the existing keys (no fourteenth key; `data/arrangements.py` refuses one), and the shortfall demoting the contest result, surplus adding nothing in the venue (adj §3.1 (12)), with its band and the reading rule that chooses any coefficient; (4) **Presence on obedience**: a term on the receiver's `comply` against `defy`/`evade` from the issuer's Presence, as seen by the receiver; (5) **Attunement on bonds**: the formation term IN-32's `tie / knot` effect consumes, and the re-pointing of the knot oracle's Bonds gate (the oracle changes at its owner, re-exported, `CLAUDE.md` §6); (6) the two profiles as its falsifier pair: high Presence, low Grace wins the contest and loses regard; high Grace, low Presence wins regard and loses the contest (AR-49, AR-50).
- GATE: after B10-10's close, landed `0533c4da` (reads CR-20's carrier and CR-84's keys); after SC-02's design (it re-sources `reception`) and CR-83's design (the WITNESS deposit) are approved. Approved by ED-1094's merge default. NEEDS: CR-20 (landed `c7764a5a`), CR-84 (landed `1abaa612`) (B10-10, read, unchanged); SC-02, CR-83 (designs).
- EXIT and FALSIFIER: the file exists and states (1) to (6), each with a falsifier and a control (every term at 0 reproduces the base hash); no code.
- HASH MOVERS: the design none; each build it schedules a declared MOVER, P14.
- HOLES AND LEDGER IDS: ED-IN-0347; H-215 (`reception`'s valence source); ED-SC-0040.
- ASKS ATTACHED: none open. The venue shortfall acting on the result is a ladder take, worth a glance `[ASSUMPTION; medium; Jordan to correct; revert: the shortfall lowers `reception` only]`.
- RE-BASE: `regard`, `reception`, `stance_term`, `obstacle` by symbol; SC-02's and CR-83's approved designs; IN-32's landed effect if built.
- BUILDER: opus; `valoria-author`; its critic per `CLAUDE.md` §10 (Lens B is the judgment node).
- SOURCE: AR-29 to AR-36a, AR-49, AR-50; adj §2.2 (iv), (ix), §3.1 (12), (16), (17); map F11, F12, F16 to F19 (reference).

````

### CR-93

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-93 | Attributes in a person's own choice: aptitude on uncontested candidates, Focus on the noise of choosing, Reason on the forecast (ED-IN-0347) | DESIGN-FIRST | E (design) | CR-20 (landed `c7764a5a`) (B10-10, read); CL-PERSON's design if approved | — | written out in full: `-12` |
```

entry (`workplans/valoria_master_workplan_v11_part17.md:26-38`):

````
### CR-93 — Attributes in a person's own choice: aptitude on uncontested candidates, Focus on the noise of choosing, Reason on the forecast (IN) · BATCH B10-19 (DESIGN-FIRST; drafted after B10-10's close; its builds slot by R8 into the next batch sharing `decision/`) · STATE DESIGN-FIRST · R R-08 (contributor), R-06 (contributor)
- WHAT: AR-04, AR-21, AR-23 (ED-IN-0347). Attributes and capabilities weight a character's choice beside his pursuits and convictions. Today an attribute can reach a choice only through `odds_weight` on a contested candidate (`decision/choose.py:171-195`; `seam/wrappers/sigma.py:146`), the believed odds are exact (`sigma.py:368-419`), and τ is one value for everyone (`choose.py:352`). ED-IN-0261's "identically disposed" sentence is narrowed, not reversed (adj §2.1).
- LANDED ALREADY: `score_terms`, `odds_weight` (CR-17), `_sample_order` (receives the person, `choose.py:243`); by B10-10's close, `Person.attributes` and the `vocation_attribute` rows (CR-20).
- REMAINING UNBUILT: (design) ONE design file under `proposals/`, no code: (1) an aptitude term on an uncontested candidate from the verb's vocation attribute (CR-20's rows), its scale against the pursuit term, and why it is not a second ladder for `odds_weight` on contested ones; (2) a per-person τ falling with Focus (AR-23); (3) an error on the believed chance that Reason shrinks and low Focus widens (AR-21), and how it composes with CL-PERSON's M40 risk term so the two are not two ladders for one quantity (NERS S); (4) obligations and demands named as CR-88's (no term here). Each coefficient is chosen by a stated reading rule over a measured sweep (`python -m engine.season.harness.decision_spread --persons` or the instrument the design names), never asserted.
- GATE: after B10-10's close (CR-20). NEEDS: CR-20 (read, unchanged), CR-17 (landed `1ef8d273`); reads CL-PERSON's design if approved.
- EXIT and FALSIFIER: the file exists and states (1) to (4) with falsifiers: two hand-built persons with equal pursuits and different attributes rank one uncontested candidate differently, and identically with the term at 0; "gates nothing": `opening_set` returns equal sets for the two; CONTROL: every term at neutral reproduces the base hash at seeds 0-2. No code.
- HASH MOVERS: the design none; each build a declared MOVER of every seeded choice.
- HOLES AND LEDGER IDS: ED-IN-0347; ED-IN-0261; ED-IN-0304 (M40).
- ASKS ATTACHED: none open.
- RE-BASE: `score_terms`, `odds_weight`, `_sample_order`, `odds_of` by symbol; CR-20's landed rows; CL-PERSON's state.
- BUILDER: opus; `valoria-author`.
- SOURCE: AR-04, AR-21, AR-23; adj §2.2 (i), §3.1 (14), (15); map F10, F14, F15 (reference).

````

### CR-95

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-95 | Spirit against circumstance and influence (ED-IN-0347) | DESIGN-FIRST | E (design) | CR-20 (landed `c7764a5a`) (B10-10, read); CR-96 (landed `c0baed2c`); B10-11b (closed) for its combat half | — | written out in full: `-12` |
```

entry (`workplans/valoria_master_workplan_v11_part17.md:52-64`):

````
### CR-95 — Spirit against circumstance and influence (IN/PC/SC) · BATCH B10-19 (DESIGN-FIRST; its combat half after B10-11b, its social half after SC-02's re-source; builds slot by R8) · STATE DESIGN-FIRST · R —
- WHAT: AR-44. Spirit resists influence and compulsion, tolerates harm and strain, and gets good results despite poor circumstances, "ignoring obstacle modifiers or adding modifiers to dice pool". Combat already reads Spirit as strain (`combatant.py:20, 34-37, 45-47, 147`); resistance and circumstance are absent (adj §1, AR-44 row).
- LANDED ALREADY: `register_pool_addend` (`sigma.py:133`); the instance modifiers (`roll.py:122-130`; combat's wound term `combat_systems.py:1044`, ED-1041); CR-96's `opposed_by` column (landed `c0baed2c`).
- REMAINING UNBUILT: (design) ONE design file under `proposals/`, no code: (1) which verbs are opposed by Spirit (influence and compulsion: the persons-targeted rows CR-20 lands), written as `opposed_by` values on CR-96's column (landed `c0baed2c`); (2) which ADVERSE instance modifiers Spirit discounts, never `base_Ob`, never TN, never below `base_Ob` or `OB_MIN` (adj §2.2 (ii)); (3) whether a pool addend is used anywhere instead; (4) the Grace and Spirit boundary (adj §2.2 (iv)). The design is run through `resolution-diagnostic` and carries its output as evidence (`CLAUDE.md` §9).
- GATE: after B10-10's close; the combat half after B10-11b closes (PC-19's and PC-20's terms change the same sigma); the social half after SC-02's re-source. NEEDS: CR-20 (landed `c7764a5a`) (read, unchanged); CR-96 (landed `c0baed2c`).
- EXIT and FALSIFIER: the file states (1) to (4) with falsifiers; the diagnostic's report shows no composed obstacle below `base_Ob` at any Spirit and modifier; CONTROL: Spirit's terms at 0 reproduce the base hash. No code.
- HASH MOVERS: the design none; (1)'s data edit a MOVER wherever a resisting person has authored Spirit; each build declared.
- HOLES AND LEDGER IDS: ED-IN-0347; ED-1041; ED-IN-0251.
- ASKS ATTACHED: none open `[ASSUMPTION; medium; Jordan to correct; revert: Spirit acts only through a pool addend]`.
- RE-BASE: `_opposition_of`, `obstacle`, the wound term by symbol.
- BUILDER: opus; `valoria-author`; the diagnostic run sonnet.
- SOURCE: AR-44; adj §2.2 (ii), (iv); map F5, F21 (reference).

````

### PC-21

card row (`valoria_master_workplan_v11_part3.md`):

```
| PC-21 | The opponent model: familiarity grown in the season, Attunement's anticipation, the combatant's state (ED-IN-0347) | DESIGN-FIRST | E (design) | PC-06 (K-1, landed `2c7f2658`), PC-14 (landed `6732111a`); B10-11 | — | written out in full: `-12` |
```

entry (`workplans/valoria_master_workplan_v11_part17.md:65-77`):

````
### PC-21 — The opponent model: familiarity grown in the season, Attunement's anticipation, the combatant's state (PC/IN) · BATCH B10-19 (DESIGN-FIRST; drafted beside B10-11b; its builds slot by R8 into the next batch editing `modules/combat` and `seam/wrappers/combat.py`) · STATE DESIGN-FIRST · R —
- WHAT: AR-38, AR-39, AR-41, AR-42, AR-43, AR-45 to AR-48. Familiarity is two module constants keyed by tradition labels (`modules/combat/traditions.py:30-56`), read at `combat_systems.py:1128, 1057, 1059`; a missed read guesses uniformly (`:1136`); no quantity reads the opponent's state or nearness to yielding.
- LANDED ALREADY: `TR.familiarity`, `read_contest`, `disp_lean`; PC-10a's `yield` terms (`wrapper.py:508`); `world_q.practice` (`:4095`), the derived-from-the-log precedent; PC-06's K-1 (B10-11b).
- REMAINING UNBUILT: (design) ONE design file under `proposals/`, no code: (1) familiarity as a per-bout input set by the seam (AR-47, AR-48), derived from the holder's own past fights against that weapon class (`wclass`) and his tradition's skills, storing nothing (adj §2.2 (viii)); the label function stays the module default for un-seamed callers; where a person's tradition lives (no `Person` carrier exists; CR-33's keys are the candidate); (2) the anticipation on a missed read, combining familiarity, the defender's Attunement and the opponent's visible state, and its effect on the draw order (the `modes[rng.randrange(3)]` contract, `:1133-1136`); (3) the opponent's state composed from what the module already tracks (fatigue, wounds, poise, initiative, `disp`) before any new quantity is coined (AR-38); (4) nearness to yielding read against PC-10a's threshold, and its consumer, or the statement that it has none yet (AR-42).
- GATE: after B10-10's close and B10-11's (kit, CR-85's build, PC-10); drafted beside B10-11b. NEEDS: PC-06's K-1 (landed `2c7f2658`), PC-14 (landed `6732111a`).
- EXIT and FALSIFIER: the file states (1) to (4) with falsifiers: at least, a fighter with a record of fights against a weapon class reads it better than one without, and equally at no record; an attuned defender's missed-read guess beats a uniform one against a fixed-disposition opponent and not against a neutral one; CONTROL: every term at its control reproduces the base hash and the combat pins. No code.
- HASH MOVERS: the design none; each build declared.
- HOLES AND LEDGER IDS: ED-IN-0347.
- ASKS ATTACHED: none open; `wclass` and the derived store are takes (adj §2.2 (viii)).
- RE-BASE: the read sites and `traditions.py` by symbol; K-1's seam.
- BUILDER: opus; `valoria-author`.
- SOURCE: AR-38 to AR-48; adj §2.2 (viii), §3.1 (21), (22); map F8, F23 (reference).

````

### PC-22

card row (`valoria_master_workplan_v11_part3.md`):

```
| PC-22 | Sparring: a non-lethal venue that pays Concentration and pairwise familiarity, once a season (Jordan, 2026-11-07) | DESIGN-FIRST | E (design) | PC-21; PC-20 (landed `4b334f2a`) | — | written out in full: `-12` |
```

entry (`workplans/valoria_master_workplan_v11_part17.md:78-90`):

````
### PC-22 — Sparring: a non-lethal venue that pays Concentration and pairwise familiarity, once a season (PC/IN) · BATCH B10-19 (DESIGN-FIRST; drafted after PC-21's design is approved and B10-11b has closed; its build slots by R8 into the next batch editing the verb cluster, P13) · STATE DESIGN-FIRST · R —
- WHAT: Jordan, 2026-11-07, this session: *a verb that allows a non-lethal fight, without wounds carried into the season loop, between two individuals*; *a venue in which characters and the player fight without lethal consequences and get practice and experience*; the payoff is *pairwise familiarity and a marginal capability raise*; *you can do it once per season*. A new contested verb `spar`, distinct from `train` (uncontested, one vocation raised by one, no scene: `loop/effects_combat.py::_eff_train`).
- LANDED ALREADY: `rosters.yaml: duel_terms` and `DUEL_TERMS` (`yield`, `blood`, `death`; `capture: yield`, `accept: blood`); `loop/effects_combat.py::_grown` and `raised_capability` (build by doing, CP-T03-04 (iv): +1 whole point on a key the person already holds, never minted, only where blood was drawn); REM-31 and IN-46's `decide` (`modules/combat/fight.py`); `world_q.practice` (the derived-from-the-log precedent).
- REMAINING UNBUILT: ONE design file under `proposals/`, no code: (0) ONE THING, ONE NAME (Jordan, 2026-11-07: *concentration, focus, nerve, composure, whatever we are using in whatever places* all tie into it). The name is CONCENTRATION: the reserve the module already keeps (`conc`, `conc_max = 3F + 2S`), whose inputs are the attributes Focus (`attr.mind.focus`) and Spirit (`attr.mind.will`). *Nerve*, *calmness* and *composure* are plain words for it and are not coined as terms here; `consistency`, `mental_fatigue` and `LAPSE_K` are three code names for its effects, which (3a) asks to be one. The design file's glossary maps every place the tree says one of these words to this one quantity, or shows that place is a different thing (`poise`, the balance state, is not asserted to be the same without reading it). (1) a `spar` row (`contests:` the body prize, V-2; `writes:` its own, below) and a `duel_terms` line (`spar: yield` `[ASSUMPTION; medium; Jordan to correct; revert: blood]`); (2) `_eff_spar` writes no `Person.body` (the `fight` and `accept` effect writes it from the scene's `wound_state`), so no wound is carried; (3a) THE PRINCIPLE (Jordan, 2026-11-07: *everything in a fight, from reading your opponent to defending with the weapon to attacking, is impacted by the character's mental state; being nervous, anxious or inexperienced is very bad because execution is not to the calibre it should be, which is why experience matters: you do not feel as much of the PRESSURE of the moment or of your opponent*). Read against the module as it stands: mental state reaches execution through THREE separate formulas, all keyed on the depleting concentration reserve and none on experience or on the pressure of the moment: `consistency` (`combat_systems.py::consistency`) enters the aggressor's read and `attack_sigma`; `mental_fatigue` scales the defender's read (`MENTAL_FAT_READ_K`) and `defence_sigma` (`MENTAL_FAT_DEF_K`); PC-19's `LAPSE_K*consistency` enters `mode_sigma` (B10-11b, landed). So a fresh novice and a veteran at the same authored Focus and Spirit execute alike while the reserve is full; PC-19's term is 0 only at the default reserve of 15 (`3F + 2S`), and K-1 now feeds authored scores on the registry's 1 to 7 scale (midpoint 4) against combat defaults of 3, so an average authored fighter is fresh at a small positive term and the lapse acts as a static Focus bonus before any hit lands, not as a lapse; the principle is not yet carried. The design states ONE quantity, the pressure a fighter feels, its inputs (the stakes of the scene, `terms` lethal against `yield`; wounds taken; the opponent's menace, read from what the module already tracks, PC-21 (3)) and the experience that attenuates it, and ONE execution penalty from it applied at every execution step (the read, the response, the attack) through one owner, and the ruling on the three code names is made: `consistency`, `mental_fatigue` and `LAPSE_K` ARE ONE (Jordan, 2026-11-07: *concentration, consistency, mental_fatigue and lapse_k should all become one, a composite of your focus, your spirit/willpower AND your amount of experience*). ONE function of three inputs, Focus, Spirit and experience (the log-derived term of (3)), is the Concentration the reserve, the read, the response and the attack all read; the build retires `consistency`, `mental_fatigue`, `LAPSE_K`, `FOCUS_CONSISTENCY_K` and `FOCUS_MENTAL_K` as separate readers and keys (each site keeps one swept weight on the one function, which is its own, not a second ladder). Whether the reserve keeps depleting by pain per hit (`CONC_DRAIN_HIT`) with experience raising its ceiling and slowing the drain, or experience enters only the ceiling, is the design file's take `[ASSUMPTION; medium; Jordan to correct; revert: depletion unchanged, experience in the ceiling only]`; the re-point is a declared mover of every fight, and PC-19's `LAPSE_K` (B10-11b, landed at 0.05) is a transitional key it replaces, so the combat pins re-record again at that build.  A spar is low-pressure by its terms, so it attenuates less per exposure than a fight, which is the *marginal* in Jordan's word and why a better partner (more menace) pays more `[ASSUMPTION; medium; Jordan to correct; revert: a flat step per spar]`. (3b) THE PRESSURE FUNCTION (Jordan, 2026-11-07: *a function called pressure, from the difference in martial capability and experience between combatants, which speaks towards why someone with a lot of training can still be intimidated by someone who is a martial Master*). It is the opponent's term of (3a)'s pressure: a function of the two fighters' STANDINGS, each a combination of martial capability (the party's `faculty` for the verb, already on `PersonalCombatInput.faculties`, CR-85) and experience (the log-derived term of (3), nothing stored), whose value is the gap by which the opponent exceeds him. It is computed at the seam, where both parties are known, and handed to the module as a typed per-bout input beside PC-21 (1)'s familiarity (the module keeps no game state and sees one party's standing only through its Combatant). It is felt by the lesser fighter and is not mirrored: the Master feels none from the veteran `[ASSUMPTION; medium; Jordan to correct; revert: a signed term]`. It is NOT removed by training: a veteran facing a Master still feels the gap, and his own experience attenuates the felt value without zeroing it (3a), which is the case Jordan names. How capability and experience combine into one standing, and the bound on the value, are takes of the design file, swept `[SIM-CALIBRATE]`. The function takes two standings and returns a number; its use at any scale other than a fight (a social contest, a levy) is not asserted here. (3) WHAT THE EXPERIENCE WRITES (Jordan, 2026-11-07: *experience from fighting should write moreso to whatever in the system governs calmness, nerves, composure, concentration while fighting, as that is the real thing it gives you, not increased technique and martial prowess itself*). In the module that is Focus (`attributes.SPEC` `focus`, `attr.mind.focus`: the concentration reserve `conc_max = 3F + 2S`, `consistency` and PC-19's lapse, poise recovery `combat_systems.py` `POISE_FOCUS_K`) and Spirit (`spirit`, `attr.mind.will`, the reserve's other term); no season carrier holds either as a quantity that play can change, because `Person.attributes` is authored once and NEVER WRITTEN IN PLAY (CR-20; no `write_matrix.yaml` row). Two carriers, one taken: (b) TAKEN, `[ASSUMPTION; medium; Jordan to correct; revert: (a)]`: Concentration's experience term is DERIVED from the log, nothing stored (the rule PC-21 (1) and (4) use, `world_q.practice`'s precedent): the THIRD INPUT of (3a)'s one function beside Focus and Spirit (not a step added onto them), a bounded swept term from the person's spars and fights survived, passed at the seam beside K-1's map, with the margin rule above applied to it (a spar counts toward it only against a partner whose Concentration is at least his own); (a) HELD FOR JORDAN: a write row on `attr.mind.focus` and `attr.mind.will`, which lifts CR-20's authored-only rule and overwrites a ratified shape, so it is not taken here. The `arms` raise (`_grown`, CP-T03-04 (iv), built and shipping) shrinks from the main effect to a smaller step or none (*moreso*, read as primary and not exclusive `[ASSUMPTION; medium; Jordan to correct; revert: arms as it is]`); re-pointing `_grown` is a declared mover of every fight that draws blood, scheduled with this build and not before. SPARRING BUILDS THE EXPERIENCE TERM BUT CAPS (Jordan, 2026-11-07: *sparring helps build this experience, but it does cap*): the term is the sum of two derived parts, the spars a person has had and the fights he has survived, and the SPARRING PART HAS ITS OWN CEILING, below the term's overall bound, so a person who only ever spars reaches the ceiling and goes no further, while a fight survived raises the term past it (a spar is low-pressure by its terms, (3a), which is why it cannot carry a person the whole way) `[ASSUMPTION; medium; Jordan to correct; revert: no separate ceiling, the margin rule and once per season alone]`. The ceiling is a swept value `[SIM-CALIBRATE]`. It makes the margin rule above and once per season two further limiters on the same farming; the design file says whether the margin rule is still needed beside the ceiling (the cut test, `ners`). `spar` carries ITS OWN WRITE ROW (Jordan, 2026-11-07: *spar needs own write row*): the spar event Concentration's experience term and familiarity are derived from is declared on `spar`'s row, not borrowed from `fight`'s band writes, so the fold runs the effect at every band, an untouched spar included (`_grown` runs only where blood was drawn because a fight's `Untouched` band writes nothing and the gate refuses a no-op write); (4) pairwise familiarity: derived from the log of spars between the pair, storing nothing (PC-21 (1)'s rule), read by the seam as the per-bout familiarity input; (5) once per season, per person `[ASSUMPTION; medium; Jordan to correct; revert: per pair]`: no existing per-season act limit was found, so the design names its owner (a candidate: derived from the log, a person with a spar this season is declined at formation, `world_q.practice`'s precedent, no counter stored); (6) the player: the per-turn `decide` surface for the player's person in a spar (unverified end to end); (7) chooser formation, and the realm run that shows it executing (`CLAUDE.md` §0.2).
- GATE: B10-11b closed; PC-21's design approved. NEEDS: PC-21; PC-20 (landed `4b334f2a`).
- EXIT and FALSIFIER: the file states (1) to (7) with falsifiers, at least: a spar leaves both parties' `body` as it was; a person sparring a partner with less Concentration than himself gains no step and one sparring a partner with more gains it; a spar that ends untouched still pays and still emits its event; a second spar by one person in one season is declined; a pair's familiarity after a spar reads above no record, and a replay from the log reproduces it; at the same authored Focus and Spirit and a full reserve, a novice's read, response and attack under one pressure each fall below a veteran's, and equally at zero pressure and at no record. A person who spars every season reaches the sparring ceiling and no further across further seasons, and one fight survived then raises the term past it; planted failure: the ceiling removed, the spar-only person keeps rising. At equal standings (3b)'s value is 0; a veteran facing a Master executes below his own execution against an equal at the same stakes, and the Master facing the veteran does not; planted failure: the standing gap dropped, the veteran executes alike against both. CONTROL: the row absent reproduces the base hash. No code.
- HASH MOVERS: the design none; the build is a declared mover (a new verb in the cluster).
- HOLES AND LEDGER IDS: none allocated (P4).
- ASKS ATTACHED: none open; the three bracketed takes above.
- RE-BASE: `_grown`, `duel_terms`, `_eff_fight`'s body write by symbol; PC-21's landed design.
- BUILDER: opus; `valoria-author`.
- SOURCE: Jordan, 2026-11-07; CP-T03-04 (iv); CR-87 (RS-25); PC-21.

````

### FA-07

card row (`valoria_master_workplan_v11_part3.md`):

```
| FA-07 | the original design's faction-vs-faction mechanisms; the second decision round restates five of its row texts onto lawful forms (Piety Track, Church Attention, Deniability Debt, Guild Favour and Schism, Parliament seats and the Sacred Veto) and records five named residues and two refusals on it (`-04` FA-07) `[revert: restore the five texts]` | HELD · LEAVE (named, unscheduled; a row becomes a position when a design reads its surface) | E | — | — | carried in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part5.md:178-190`):

````
### FA-07 — the original design's faction-vs-faction mechanisms (FA) · BATCH B10-Z · STATE LEAVE (named, unscheduled; a row becomes a position when a design reads its surface) · R —
- SECOND DECISION ROUND (item 5, translate the board-game aggregates, `-05` §1b; still LEAVE in B10-Z): five row texts of the v9 table below are corrected by the translation rule: Piety Track → the share of a territory's residents whose live `commit` is to the Church's Proposition (form F3); Church Attention → each Church seat-holder's own attention over his own ledger (F1; no pooled Query); Deniability Debt → no Query: the debt is the claims themselves, each read by its holder (F1); Guild Favour and Schism → each member's own regard (F1) and the members' `release` edges (F3); Parliament seats and the Sacred Veto → CR-34's live-commit tally at `parliamentary_debate` once CR-38 seats a bench; the seats are unbuilt (H-90) and the Veto is a residue. Named residues recorded here: the Parliamentary Stay (trigger: H-90's Parliament seated); the postmortem tribunal (no reader: a dead accused holds no edge); seizure modifiers by others' instruments (trigger: a `seize` matter on a docket); Church levies (trigger: CP-T09-07's obligee army); GD-2's mandatory muster (trigger: H-224's input reaching governors). Refused (`-05` §1b's refusals): the Gransol exception (RF-8, a rule keyed on a named entity) and the Policy Instrument (RF-4 and RF-1: a faction as actor, and a stored aggregate). Not engaged: Jordan's "ratcheting of Church as faction until it attempts to seize lands" (`rosters.yaml:2606`), whose lawful form would be F3 over Church `commit` and `hold` edges; no position takes it. `[ASSUMPTION; medium; Jordan to correct; revert: restore the five texts]`
- WHAT: Keep named, unscheduled, the faction-vs-faction mechanisms of the original design that no position owns (Church Influence, Piety Track, Church Attention, Altonian pressure, Autonomy, Deniability Debt, and others). Every stored clock is refused; each becomes a Query over existing carriers, banded only under T-b.
- LANDED ALREADY: as the per-row gates above show (B-Q, B-V, B-X rows landed their gates); no row is itself built as a position.
- REMAINING UNBUILT: [v9 WHAT, full text: one row per mechanism of the original design's faction work not already owned by a position (A-37 lists the owned ones). "Every stored clock is refused (T-a, T-c, A-29); each becomes a Query over existing carriers, banded only under T-b." Rows (mechanism: Layer-1 form · surface needed · gate): Church Influence: Query over Church holds, seats, members and territory piety · `faction_q.resolve` (landed) and the piety Query · SE-06. Piety Track: `piety_of(w, territory)` over residents' affiliation intensities · SE-06's temperaments, IN-64's convictions · SE-06. Church Attention: Query over the `deed_doers engaging` claims Church seat-holders hold · IN-67 · B-X. Altonian pressure (IP): Altonian head's own windowed estimate of realm weakness · IN-36, FA-01's clause (`ED-IN-0298`), IN-23 (landed `c4eb6f84`) · B-Z. Löwenritter Autonomy: Ehrenwall's regard of the King, banded under T-b; the Split is her `release` · FA-04, `regard` (with IN-58's grievance, `3bf936ee`) · B-X. Deniability Debt: Query over claims others hold about covert acts · `conceal` (IN-12 step 10, `67686661`) · B-Q. Warden's Accord: regard between heads · none (Wardens stay unplaced by Jordan's 2026-09-14 ruling, `harness/populated.py:760-773`). Parliament seats and the Sacred Veto: arrangement plus a Mandate Query · SC-01 (landed), IN-23 (landed) · landed. Mission shift: head's `utter` of an OUGHT plus members' `commit`/`release` · IN-66..IN-68, IN-11 · B-X. Leadership Deviation cost: cost on an act against one's org's goal · IN-69's `alignment` · B-X. Guild Favour and Schism: members' regard and holdings · B-V's Guilds head (`test_fa01_head_seats.py`'s `LEADERLESS` until then) · B-V.] every row, as a position.
- GATE: LEAVE; DEPS per row; EDITS none. A row becomes a position when a design reads its surface, slotted by `_part3` §B.0 (v10: its R8 step).
- EXIT and FALSIFIER: "a row that becomes a position takes its own; `git grep -n "piety\|church_influence\|attention_pool" -- engine/season ':!*cases*'` returning a stored field is the defect (T-a)".
- HASH MOVERS: none.
- HOLES AND LEDGER IDS: none; A-29, A-33 (named residue FA-07: deviation COST and Mission shift as acts), A-37, T-a, T-b, T-c.
- ASKS ATTACHED: none.
- RE-BASE: the per-row gates cite B-Q (`conceal`), B-V (Guilds head), B-X (IN-66..IN-69, FA-04..FA-06; the batch is RS-30), all closed; the rows' "B-X" and "B-V" gate words are now landed. Whether each landed gate makes its row buildable is not examined in v9 [INFERRED]. None else found.
- SOURCE: `v9_p7:136-140`; note on FA-04..FA-07 at `v9_p7:134`; state-index row `v9.md:295`.

````

### MB-08

card row (`valoria_master_workplan_v11_part3.md`):

```
| MB-08 | generated map, AI generals (#445 U-1, U-2, U-6); records the trigger of R-04's commander-chosen orders residue (a typed `Orders` record shared by the PLAYABLE scene and the AUTOMATED planner) | HELD · LEAVE (named, unscheduled) | E | — | — | carried in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part5.md:228-240`):

````
### MB-08 — generated map, AI generals (#445 U-1, U-2, U-6) (MB) · BATCH B10-Z · STATE LEAVE (named, unscheduled) · R —
- WHAT: each its own subsystem: a seeded terrain-shaped generator; an AI planner authoring Orders; #445 U-1 (musters with inputs beyond headcount), U-2 (one equipment model for both scales), U-6 (armour and endurance bridges through U-2). "Their gates are met, but none is scheduled and no R-row moves on them."
- LANDED ALREADY: —.
- REMAINING UNBUILT: all.
- GATE: STATE LEAVE. DEPS: IN (the season-side reader of any of them); EDITS none.
- EXIT and FALSIFIER: EXIT "`python -m engine.season.harness.register --requirements` — no R-row's `measure:` or missing-mechanism text names any of the three." FALSIFIER "an R-row, or a `hole_register.yaml` row, citing one of them as its cause shows 'no R-row moves on it' wrong, and the item is scheduled the day that is read."
- HASH MOVERS: none.
- HOLES AND LEDGER IDS: #445 U-1, U-2, U-6; no hole rows.
- ASKS ATTACHED: none.
- NAMED RESIDUE (decision round, R-04 conjunct (3), `-02`): commander-chosen orders (the AUTOMATED mode may run the default orders, `massbattle.py:170-178`); trigger: a position that designs a typed `Orders` record shared by the PLAYABLE scene and the AUTOMATED planner (this entry's AI-generals half). It is not a position and does not gate R-04.
- RE-BASE: none found.
- SOURCE: `v9_p7:26-31` (SOURCE there: `registers/handoffs/HANDOFF_MB.md`; `proposals/2026-09-25-squad-engagement-synthesis.md:137`; `proposals/2026-09-30-character-and-play-surface/08_mass_battle_units.md:125,126,130`); state-index row `v9.md:282`.

````

### PC-06

card row (`valoria_master_workplan_v11_part3.md`):

```
| PC-06 | #445 recommendations ratified as intent: K-5 held (K-1 landed at B10-11b, `2c7f2658`) | HELD · LEAVE (K-5, unscheduled); K-1 LANDED; K-3 LANDED | E | — | — | carried in full: `-04` part 2 |
```

entry (`workplans/valoria_master_workplan_v11_part5.md:241-252`):

````
### PC-06 — #445 recommendations ratified as intent: K-5 held (PC) · BATCH B10-Z · STATE LEAVE (K-5, unscheduled); K-3 LANDED; K-1 LANDED at B10-11b (`2c7f2658`) · R —
- WHAT: Nothing in the #445 digest recommendations is still scheduled. K-1/K-5 (a `Combatant` built from the person; loadout as `hold` tenures) wait on `Person.attributes` (K-2), which builds only with its first reader. M-2..M-6 stay with PC-08. K-3 and the earlier items have landed.
- LANDED ALREADY: S-1 at B-E (`engine/season/harness/play_surface.py`, falsifier `engine/season/tests/test_play_surface_dispatch.py`; `ac9724fc`); M-1/S-4 and S-2/L-1 at B-L (`9ad86e87`); K-3 at B-S (`1023197b`, B-S closed `6e833a57`, #500) — its EXIT is read under head §0.5 (`engine/season/hole_register.yaml` H-238; H-239 the gate's row), and its FALSIFIER's Coherence clause is unobservable at B-S (HANDOFF_IN, the B-S row).
- REMAINING UNBUILT: [v9 WHAT, full text: no digest recommendation is still scheduled. K-1/K-5 (the `Combatant` built from the person; loadout as `hold` tenures) are NOT scheduled: they need `Person.attributes` (K-2), which builds only with its first reader (K-1/K-6), and "K-2 is not ratified". M-2..M-6 (engagement cadence, wound state between engagements, the Plan layer, duel mode, the grid as mass battle) stay with PC-08; J-15 (#445 `05` §4.1, §4.2) is ask-then and attaches to M-2.] K-1, K-5, K-2 (and with it M-2..M-6 -> PC-08).
- GATE: DEPS K-2 -> K-1/K-5. K-2 is CR-20 (B10-10, `Person.attributes`); K-1 LANDED at B10-11b (`2c7f2658`, closed; ED-IN-0347, AR-48: the seam sets each `Combatant` field from `Person.attributes` by PC-14's `registry_key` map, absent keys at the class default, by `party_end`'s precedent). K-5 stays held (kit is CP-T03-03's). K-1's EXIT: a person with authored Strength 6 fights as Strength 6; CONTROL: an all-absent realm reproduces the pre-item hash; HASH: a declared MOVER wherever an authored person fights.
- EXIT and FALSIFIER: EXIT "`python -m engine.season.harness.register --requirements` — no R-row's `measure:` or missing-mechanism text names K-1 or K-5." FALSIFIER "an R-row, or a `hole_register.yaml` row, citing K-1 or K-5 as its cause shows 'unscheduled' wrong, and the item is scheduled the day that is read."
- HASH MOVERS: none stated for the LEAVE items (K-3's three sweep arms are declared corpus movers, H-239).
- HOLES AND LEDGER IDS: H-238 (SUPERSEDED as a blocker by head §0.5, 2026-10-13), H-239 (gate 30 shipping; 0 the control; arm 50 declared not run), H-85 (G1: the verb gate half is built at K-3; the knowledge-KIND half is not — `thread_substrate` is read by no code in `engine/season`); K-1..K-6; J-15.
- ASKS ATTACHED: J-15 (#445 `05` §4.1, §4.2: do unwatched fights resolve in one act or span scenes?; does duel mode open any closed moment, recommended no) — asked when M-2 is scheduled (PC-08).
- RE-BASE: B-S (#500) landed K-3 and the v9 entry records it. None found since.
- SOURCE: `v9_p7:42-47` (SOURCE there: `proposals/2026-09-30-character-and-play-surface/README.md:44-52`; `.../09_the_character_sheet.md:128-132`); state-index row `v9.md:284`.

````

### PC-08

card row (`valoria_master_workplan_v11_part3.md`):

```
| PC-08 | Phase 4a / 4b / 5, WS-7, channel-leverage: design-gated backlog | HELD · LEAVE (named, unscheduled; J where Jordan names one) | E | — | — | carried in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part5.md:253-264`):

````
### PC-08 — Phase 4a / 4b / 5, WS-7, channel-leverage: design-gated backlog (PC) · BATCH B10-Z · STATE LEAVE (named, unscheduled; J where Jordan names one) · R —
- WHAT: Keep named and unscheduled the design-gated backlog: Phase 4a, 4b and 5, WS-7, the channel-leverage residual (4c), and the #445 items K-4, V-3, V-2, U-4, U-5, K-6, so none is dropped. The R2 capstone finding is history to read first if Phase-C recalibration starts.
- LANDED ALREADY: K-4's role by IN-12 step 9 `train` (`996c16dc`, B-Q).
- REMAINING UNBUILT: [v9 WHAT, full text: abilities-as-access depth (4b), the game-theoretic layer (4a), the contact axis (5), WS-7 multi-combatant (also gated on ED-911) and the channel-leverage residual (4c, where Jordan sets per-paradigm strength) are design-gated, "no immediate action". #445's M-2..M-6 cover live parts; J-15 attaches to M-2. Items named so none is dropped (README ranks at `README.md:62-64, :71, :76, :81`): K-4 (`09_the_character_sheet.md:131`, the `practice` verb as `capability`'s writer) SUPERSEDED by IN-12 step 9's `train` (`996c16dc`; J-13 (iii), RS-21 item 10 [medium; Jordan to correct]); V-3 (`10_verbs_and_attributes.md:199`, `faculty(domain)` as sole owner of the aptitude slot) stays LEAVE, presupposes `Person.attributes` (K-2, unscheduled, PC-06); U-4 and K-6 (`08_mass_battle_units.md:128`, `09_the_character_sheet.md:133`: an `Officer`'s charisma and cognition from the commander's attributes) stay LEAVE ("after K-2"); U-5 (`08_mass_battle_units.md:129`: a stat preset for `mounted_archers` or a written reason it has none; "trivial, any time") stays LEAVE — no season field carries a troop type other than infantry (`_MVP_SUBUNIT_SHAPE`, `massbattle.py:159-161`) — and attaches to the same first position as J-19 (MB-07r, landed `aa6871b8`); V-2 (`10_verbs_and_attributes.md:198`, standing rule: an attribute reaches a verb only through a faculty and only if the verb's row has `contests:`) is not a position — it binds the author of every `verb_table.yaml` row IN-08 and IN-12 add (three rows declare `contests:` today: `fight` `verb_table.yaml:466`, `march` `:601`, `tell` `:889`, read 2026-10-06). The R2 capstone finding (reach-class weapons above the contested-balance target against arming) is history: read first if Phase-C recalibration starts (`HANDOFF_PC_history.md`, heading "R2 (closing-distance/facing/grip/contact redesign)").] everything else named.
- GATE: STATE LEAVE; DEPS none scheduled; EDITS none.
- EXIT and FALSIFIER: EXIT "`python -m engine.season.harness.register --requirements` — no R-row's measure names any of them; for the channel-leverage residual, `python systems/combat/combat_engine_v1/workbench/balance.py context` is the re-measure once Jordan scopes it." FALSIFIER "an R-row, or a `hole_register.yaml` row, citing one as its cause shows 'no R-row moves on it' wrong and the item is scheduled the day that is read."
- HASH MOVERS: none.
- HOLES AND LEDGER IDS: ED-911, K-4, V-2, V-3, U-4, U-5, K-6, M-2..M-6, J-13 (iii), RS-21 item 10, IN-12 step 9; no hole rows.
- ASKS ATTACHED: channel-leverage per-paradigm strength (4c, Jordan sets); J-15 (ask-then at M-2).
- RE-BASE: B-Q (#490) landed `train`, which superseded K-4. None else found.
- SOURCE: `v9_p7:49-54` (SOURCE there: `registers/handoffs/HANDOFF_PC.md` rows; README `:44-52`); state-index row `v9.md:285`.

````

### IN-44

card row (`valoria_master_workplan_v11_part3.md`):

```
| IN-44 | Layer 0 and Layer 1 edits owed: LISTED, NOT MADE (SM-10, SM-12, A-24's wording); row 1 (the `CLAUDE.md` §0.2 `mc_v18` bullet) released by M15 (a), retired as a listed Layer 0 hunk (H-L0-6, applied in PR #507) | HELD · LEAVE (rows 2-16, released from M11 by ED-IN-0300: unscheduled, slotted by R8; each row is re-derived by symbol and (RULED)-checked at its anchor before it is listed or landed) | E | — | — | carried in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:662-675`):

````
### IN-44 — Layer 0 and Layer 1 edits owed: LISTED, NOT MADE (SM-10, SM-12, A-24's wording) (IN) · BATCH B10-Z · STATE rows 2-16 released from M11 (ED-IN-0300), unscheduled in B10-Z; row 1 released by M15 and applied as H-L0-6 · R —
- DECISION ROUND: row 1 (the `CLAUDE.md` §0.2 `mc_v18` paragraph) is released by M15 taken (a) (`-05`; step 1, superseded: it executes Jordan's 2026-09-16 and 2026-09-27 words quoted in row 1): it is applied in PR #507 as H-L0-6 `[ASSUMPTION; medium; Jordan to correct; revert: restore the four lines]`. Rows 2-16 are released from M11 (answered (a): the superseding row of ED-IN-0300, 2026-10-26, ratified): they stay in B10-Z, unscheduled, slotted by R8, and each row is re-derived by symbol and (RULED)-checked at its anchor before it is listed under "Layer 0/1 hunks" or landed.
- WHAT: Hold the sixteen stale Layer 0 and Layer 1 passages (file:line, what is stale, reading owed) that no batch edits; they are Jordan's files. It owns the SM-10, SM-12 and A-24 wording and receives other positions' Layer-1 wording rows.
- LANDED ALREADY: —. (Adoption edited only the two `CURRENT.md` rows named at v9_p8:369-371, item 1.)
- REMAINING UNBUILT: [v9 WHAT, full text: the table of stale Layer 0 and Layer 1 text that no batch edits; "Jordan does". It names the file:line, what is stale and the reading owed. It owns the SM-10 and SM-12 wording and A-24's wording rows, and is the destination for IN-61's Layer-1 wording (`04` §B.8, §A.3 row 8, §F.24a row 5), SE-04 (b)'s `Rung.envelope` row and IN-56's AX-4 log-index reading. v9 treats it as a table, not an entry.] all sixteen rows of the v9 table (rows 1-16, `v9_p8:416-431`): (1) `CLAUDE.md:278-281` §0.2 `mc_v18` paragraph (Jordan's words supporting retirement are quoted there: 2026-09-16 "Remember that mc_v18 is being fully retired."; 2026-09-27 "we need to move beyond any mention or use of this mc_v18. that is critical."); (2) `CLAUDE.md:407-414` §3 `engine/` bullet; (3) `CLAUDE.md:395-447` §3 no `modules/` row; (4) `CLAUDE.md:527-531` §6 "starting with `engine_clock`"; (5) `CLAUDE.md:540-547` §7 retired `balance_oracle` paragraph; (6) `CLAUDE.md:155` §0.05 `fac.intel` "reachable by nothing"; (7) `CLAUDE.md:514` (SM-10 cite); (8) `CURRENT.md:15, :22, :41` stamp, retire-set wording, `engine/autoload`; (9) `architecture/meta/04_CODE_ARCHITECTURE.md:1000`, `architecture/PLAN.md:1271`, `architecture/VOCABULARY.md:125` (SM-10); (10) `architecture/holonic_ARCHITECTURE.md:75` `[engine]` tag (SM-12); (11) `04_CODE_ARCHITECTURE.md:164, :370, :374-376, :596-611 (C.2), :391, :494` (determination opens any `disposes:` kind; tenth basis `warrant`; `RELEASABLE_KINDS`); (12) SM-12 / A-24's holonic item (the 2026-09-17 "holonic shape" preference predates A-25; "later governs; Jordan to note the earlier preference when he edits"); (13) `CLAUDE.md:727-730` §11 deny-list vs `RemoteTrigger` [UNVERIFIED in v9: what `RemoteTrigger` does in the current tool surface]; (14) `04:195, :326, :359, :1188, :609-610` (heir as holder-owned `succeed` edge; RS-27 makes the heir a title; `succeed` Tenure kind opened by nothing); (15) `04:115` AX-4 vs IN-56's `World._last_by_anchor`/`_last_by_subject` log index; (16) `04:255` `Rung :=` `envelope`, `:179`, `:1166` (H-171). Closing line (v9_p8:433): "`CURRENT.md:41`'s pointer repair is the same class as #448's and may ride adoption at Jordan's word." [Line numbers in rows are v9's, read 2026-10-06 and earlier; re-derive each anchor by symbol before use.]
- GATE: released from M11 (ED-IN-0300): an agent may land unmarked `CLAUDE.md` and `architecture/` text in the PR, stated openly under "Layer 0/1 hunks"; text marked (RULED) stays Jordan's and stops its row. v9: "IN-44 sits in B-Z: no batch edits these files; Jordan does." Rows 14-16 carry "Nothing waits on it" / "[medium]" tags where stated (rows 14, 15). `CLAUDE.md` marks some rules (RULED): v10's batch card for B10-03 requires each anchor to be checked for a (RULED) mark before a hunk is listed.
- ALSO OWED (`-08`, REM-41 cut): `architecture/meta/04_CODE_ARCHITECTURE.md:496` says 'the log accepts no other kind'; `matter.py`'s three direct appends (`:105`, `:234`, `:297`) are game emitters that bypass the fold's check, so the sentence is unmet until Jordan edits it or the appends are checked. No position builds either.
- EXIT and FALSIFIER: v9 states none for IN-44 as a table. The instrument v9 names for the adoption-time subset is `python tools/currency_consistency_check.py` and `python tools/valoria_local.py --staged` (v9_p8:389); v9 states no falsifier for the rest.
- HASH MOVERS: none stated (text only).
- HOLES AND LEDGER IDS: H-171 (row 16); ED-IN-0206 (row 8: becomes `superseded` -> `23`, SC-02); ED-IN-0292 (1) (row 14, `founding` wording); SM-10, SM-12, A-24, A-25, RS-11, RS-27, RS-29, IN-56.
- ASKS ATTACHED: whether the PR #450 deletions return, A-24 (i) — v9 working answer NO [medium], "yours to overrule" (v9_p5:246, :350-352). Not answered here.
- RE-BASE: rows 14-16 cite IN-61's stop at B-R, IN-56 (landed B-W) and H-171 (appended at B-T), so they were added after B-R/B-W/B-T [INFERRED from what the rows cite]; rows 8 and 13 are older. Since v9 was written: HEAD is `b7a1e1b`; `CURRENT.md`/`CLAUDE.md` wording may have moved again — re-derive each anchor. No batch among B-Q..B-Y edited Layer 0/1 per the merge subjects.
- SOURCE: `v9_p8:410-433` (table `:416-431`; H.3 adoption edits `:369-385`); state-index row `v9.md:263`.

````

### SC-07

card row (`valoria_master_workplan_v11_part3.md`):

```
| SC-07 | #445 P-4, V-4, V-5: attach to the proceedings design | HELD · BLK:a carrier per item | E | — | — | carried in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part5.md:277-291`):

````
### SC-07 — #445 P-4, V-4, V-5: attach to the proceedings design (SC) · BATCH B10-Z · STATE BLK:a carrier per item · R —
- WHAT: Carry three #445 digest recommendations that wait on a proceedings carrier: P-4 procedure before the vote (agenda, motion order, recorded defeat), V-4 one non-combat acquisition layer, V-5 gloss `survey`/`surveil` by their roots. They stay reference until each has a carrier.
- LANDED ALREADY: —. (SC-01 landed, B-N closed `cf69ceed`; it built nothing for this entry.)
- REMAINING UNBUILT: [v9 WHAT, full text: three digest recommendations waiting on the proceedings build. P-4: procedure before the vote (agenda control, chair's order of motions, recorded defeat). V-4: one non-combat acquisition layer, in the proceedings design. V-5: gloss `survey`/`surveil` by their roots, and name any rostered speech kind other than `construe`. They are NOT in the set ED-IN-0290 ratifies as intent (S-1, M-1/S-4, S-2/L-1, K-3, U-3, P-1..P-3); they stay reference until each has a carrier.] all three items, each awaiting a carrier; then `arrangements.yaml: speech_kinds`, `verb_table.yaml` notes. V-5's gloss half is "trivial, any time" (`README.md:71`) but v9 gates the whole row on SC-01.
- GATE: "BLK: a carrier per item"; v9 BATCH "B-Z (held: each item builds when a carrier exists) [ASSUMPTION; medium; Jordan to correct — basis: #445's own 'SC, when un-held'; revert: Jordan slots an item into the next SC batch]".
- EXIT and FALSIFIER: EXIT P-4: "a carried-and-vetoed motion persists as a citable record (`02_against_precedent.md:83`)"; V-4: "two persons differing only in an acquired technique choose differently in one situation (`10_verbs_and_attributes.md:200`)". FALSIFIER "a motion vetoed in a seeded proceeding that leaves no Record fails P-4; two persons identical but for the technique that choose identically fail V-4; both must be seen failing on the tree before the build."
- HASH MOVERS: none stated.
- HOLES AND LEDGER IDS: #445 P-4, V-4, V-5; ED-IN-0290, ED-IN-0286.
- ASKS ATTACHED: none beyond the assumption's revert ("Jordan slots an item into the next SC batch").
- RE-BASE: SC-01 (B-N) and B-P landed without building a carrier for these. None found since.
- SOURCE: `v9_p6:70-76` (SOURCE there: `proposals/2026-09-30-character-and-play-surface/02_against_precedent.md:83`, `10_verbs_and_attributes.md:200-201`, `README.md:71, :79`); state-index row `v9.md:276`.

---


````

### CR-39

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-39 | Promotion: an emerged creed earns parliamentary standing (`queries/world_q.py::promoted`: its members hold live `hold`s on at least two territories, counted on demand, never stored) | HELD on CR-38 (trigger: CR-38 lands a Court Parliament bench) · BUILD when released | M (when built) | IN-30, CR-38 | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:266-278`):

````
### CR-39 — Promotion: an emerged creed earns parliamentary standing (IN/FA) · BATCH B10-Z (HELD on CR-38) · STATE BUILD (HELD) · R —
- WHAT: item 4, promotion held at step 4: an emerged creed (IN-30) earns standing on Court Parliament's bench. GD-3's promotion conditions are restated in lawful forms and the position is held on its reader, CR-38's bench, because a Query with no consumer is a false N-line (r2 `05` §A.1.5 RULED (d), quoted in H-186's `cite:`). Trigger: CR-38 lands a Court Parliament bench.
- LANDED ALREADY: —.
- REMAINING UNBUILT (when built): `queries/world_q.py::promoted(w, creed)`: the creed's members hold live `hold`s on at least two territories (a count on demand, never stored, T-a's licensed form). GD-3 (c)'s `L ≥ 3` is refused as a gate (a stored aggregate, `-05` §1b's refusals); legitimacy enters as each bench member's reason when he votes the creed's seat in. `Accord ≥ 4 averaged` takes form F3 (the share of the held territories' residents whose live `commit` is to the creed, at or above a band) and is not carried until a band is ruled (no invented number). The two-season sustain is cut (a clock, #457 §5); GD-3 (d)/(e)'s `PT` split is an aggregate and is refused. The finding stands: the retired oracle's `L` was initialised at 1.0 and never written, so promotion was unreachable by construction (`git show 5c5d8ec6:systems/world/sim/insurgency_pipeline.py`, `:41`, `:44`, `:73`, `:218-221`; corroborated only in part by `governance_type_registry_v1.md:106`; the git object was not re-opened).
- GATE: HELD in B10-Z on CR-38. NEEDS: IN-30, CR-38.
- EXIT and FALSIFIER (when built): a creed whose members hold two territories sits on CR-38's bench; one holding one territory does not. CONTROL: CR-38's bench without the promotion term.
- HASH MOVERS: declared MOVER when built (it changes a bench).
- HOLES AND LEDGER IDS: H-186.
- ASKS ATTACHED: item 4 (`-05` §1b) `[ASSUMPTION; medium; Jordan to correct; revert: none needed while held]`. If CR-38 is unapproved when B10-18 closes, CR-39 is on B10-20's freeze row with it.
- RE-BASE: re-read IN-30's landed `faction_props` and CR-38's approved design when the trigger fires.
- BUILDER: `CLAUDE.md` §10's third tier (judgment).
- SOURCE: H-186's `cite:`; `canon/04_game_design_constraints.md` (GD-3).

````

### CR-80

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-80 | The deck: world-build seeds per strife category (A to I) as `[ASSUMPTION]` rows through CL-EVENTS (3)'s schema, switch off; no schema of its own (the strife fold, v11) | HELD (on CL-OPEN's build; the strife fold put it here directly, as CR-39 was) · BUILD (rows) when released, slotted by the plan's R8 (head §7) | E | CL-EVENTS, CL-OPEN | the rows' content beyond `[ASSUMPTION]` rows is Jordan's (P11) | written out in full: `-11` |
```

entry (`workplans/valoria_master_workplan_v11_part16.md:56-72`):

````
### CR-80 — The deck: world-build seeds per strife category (IN/WR) · BATCH B10-Z (HELD on CL-OPEN's build; slots by the plan's R8, head §7) · STATE BUILD (rows; shipped off; hash EQUAL) when released · R —
- WHAT: `strife-00` §8 S6: world-build seeds per category (A to I) through the schema of CL-EVENTS commit (3) (goal rows or yield scales, drawn once at build), so that every category can open in a seeded world without anything firing in a season (R1, R2; T-c). Rows only: the schema, and any widening of it, are CL-EVENTS (3)'s and CL-OPEN's (the one owner of the widening, `-10` §3). Each row is read from the study's occasion column (`strife-00` §2) and carries `[ASSUMPTION; medium; Jordan to correct; revert: delete the row]`; the switch is the Tensions switch, shipped off.
- LANDED ALREADY: none (CL-EVENTS (3) and (4) are B10-18's).
- REMAINING UNBUILT: the rows; their test.
- GATE: CL-EVENTS commits (3) and (4) landed (B10-18); CL-OPEN's build landed (B10-19, HELD on M26). Released, it slots by the plan's R8 (head §7; not `strife-00`'s R8, "People exist within flows") into the next unopened batch that edits `tensions.yaml`, else runs as its own sub-batch; released after B10-20 opens, it is a declared post-freeze change. NEEDS: CL-EVENTS, CL-OPEN.
- EXIT and FALSIFIER: on the test arm (switch on), each category's opening kind appears in the strife reachability report at seed 0; the loader refuses a row outside CL-EVENTS (3)'s schema. CONTROL: switch off reproduces the base hash. "It has no on-arm today": the on-arm flip is the Tensions flip already on B10-20's freeze row.
- HASH MOVERS: none (switch off). Released after B10-20 opens, a registry change re-exported through GO-09 with an `ED-GO-` row.
- HOLES AND LEDGER IDS: none.
- ASKS ATTACHED: the rows' content beyond `[ASSUMPTION]` rows is Jordan's (P11).
- RE-BASE: CL-EVENTS (3)'s schema and CL-OPEN's widening as built.
- FILES: `engine/season/tensions.yaml`, `engine/season/tests/test_tensions.py`.
- VERB CLUSTER: no.
- LAYER 1: none beyond CL-EVENTS (3)'s.
- N-LINE: the deck — cut it and the gameplay experience is worse, because categories whose occasion no default world holds (a subject people under a burden, a servile population, an unpaid army) can never open, so R1 holds only for the categories the cast happens to seed.
- BUILDER: second tier for rows.
- SOURCE: `strife-00` §8 S6.

````

### IN-18

card row (`valoria_master_workplan_v11_part3.md`):

```
| IN-18 | G5, G8, the gated tail (telling workplan residue), narrowed at B10-02's close | HELD · the MEASURE landed (`harness/obligee_report.py`, `165d355c`; survivors-only floor, stated in the module): headline M0e 0 / 0 / 0 at seeds 0 / 1 / 2 over four realm seasons (G5 HELD), the workplan's own M0e (`inferred_about_person`) 4 / 18 / 4 (above 0: its Stop-if, the site `_from_inferred_claim` not derived); G5 unbuilt, G8 gated by judgment | M (conditional: a declared realm-hash mover per commit only if G5 builds; H-204 moves the told channel) | — | — | carried in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:649-661`):

````
### IN-18 — G5, G8, the gated tail (telling workplan residue) (IN) · BATCH B10-Z (HELD; its MEASURE closed at B10-02) · STATE BLK:G5 trigger M0e (re-measured at B10-02: headline 0, the workplan's own definition above 0); G8 gated by judgment · R —
- WHAT: Build the two gated tail rows of the telling table: G5 (an obligee reports to the seat holder) when its trigger M0e > 0 is met, and G8 (letters deposited as `told_by`) when judgment lifts its gate. A field lands only with its reader and falsifier; unfleshed elements stay `absent` hole rows with field-less markers.
- LANDED AT B10-02 (`165d355c`, with the close commit's corrections): the M0e reader `harness/obligee_report.py` (`python -m engine.season.harness.obligee_report SEASONS SEED ...`; it reads survivors only, so every count is a lower bound where an obligee or holder died). Four realm seasons, seeds 0 / 1 / 2: headline `m0e` (an executed `news.told` by an obligee to his seat's holder) 0 / 0 / 0; `attempted` 0 / 1 / 3 (all `news.untold`, degree None); `told_by` 0 / 0 / 0; `inferred_about_person` (the telling workplan's own M0e) 4 / 18 / 4; obligee edges 36 / 44 / 39. G5 is HELD on the headline definition, and on the workplan's definition M0e is above 0 with the site not derived (this position's Stop-if); G5 stays unbuilt either way.
- LANDED ALREADY: step 2a, G1 (live, `judged_gain` and `told_valence_gain` at 0.5), G2, G3 at B-E `ac9724fc`; G4 dropped; G7 recorded (H-198); G6 at B-I `66bf51f9` (dormant in play, H-204); `oblige` (IN-10 sub-step (a)) `905b7a21`; telling T0-T6 (#449).
- REMAINING UNBUILT: [v9 WHAT, full text: the open rows of the telling §5 table, the §6 branches they read and the §10 judgments. G5 (duty to report: an obligee forms a `tell` to the seat holder) builds when M0e > 0; G8 (letters: `create_record(letter)` + `give` deposits the said triple as `told_by`) is gated by judgment. The ties row is IN-32's. Rule that governs both: a field lands only in the same commit as its reader and its falsifier; an unfleshed element is an `absent` hole row plus a field-less `# ABSENT: H-NNN` marker, never a dead carrier.] G5 (site `_from_inferred_claim` — "names no symbol in the tree read at B-E's boundary — re-derive it by grep before editing"); G8 (letters); the ties row (IN-32's). Other `absent` rows and triggers carried: `stake` (M0h > 0); a default-obstacle sweep (M0i after T4 no higher than at T0); `Seen.who` as a source (only if M0d counts zero from it); sanctioned silence (`date.fired` reaching WITNESS, plan position `22`). Standing §10 judgments (recorded, not ruled by Jordan, reversible): G8 letters gated; self-disclosure allowed; private whispers not built.
- GATE: G5: prerequisite T4 (landed), trigger "M0e > 0" (§5 row G5) — read 0 over four realm seasons at B-I's close (2026-10-13) after `oblige` landed; "re-measure when obligees exist before the final season". G8: prerequisite T4; trigger "none; ahead of T5 if M0d < 20%" — realm M0d 12% licensed G8 ahead of T5, T5 landed first, G8 stays gated. Ties: prerequisite IN-32 (`_eff_tie`), trigger `aperture 1 0`: `tie / knot` executed > 0. Each trigger is a figure an existing instrument prints (§0.1 pt 5 forbids a guard).
- EXIT and FALSIFIER: EXIT "per gate, §5's falsifier column, observed at the batch that builds it" (G1's EXIT, `engine/season/tests/test_told_by_channel.py::test_r07_realm_regard_differs_between_hearers_by_claim_not_stance_alone`, ran at B-E's exit). FALSIFIER, G5: "an obligee forms a `tell` to the seat holder, and without `oblige` none (§5 row G5)"; G8: "`create_record(letter)` + `give` deposits the said triple as `told_by`, chain ending in the maker"; ties: IN-32's.
- HASH MOVERS: none stated.
- HOLES AND LEDGER IDS: H-62, H-66, H-175, H-149, H-192, H-193, H-198, H-204 (cited by v9); per G1 classification also H-194 (G2, `stance_polarity`, asked in ED-IN-0296; answered by CR-16, `declared`), H-195 (G2 `holder` operand, trigger M0g >= 5 %), H-196 (G3, `said_slant`), H-197 (G6, `telling_privacy`); ED-IN-0282 (telling workplan); ED-IN-0296.
- ASKS ATTACHED: §10 #1 private whispers, "Jordan's alone" (voids T-e; T4 redone); recommendation recorded "Do not build". §10 #3 self-disclosure; recommendation "Allow". (v9_p4:91-94)
- RE-BASE: v9 re-read the position at B-I (G6, `oblige`) and B-M (CARRY-INTERIOR reads G1 at IN-13's fought field; realm fights 0 fields). Since: B-X (#480) landed the decision-surface cast/goals/salience work and wrote ED-IN-0296, which carries H-194's `declared`-arm question that G2 depends on; B-Q..B-Y subjects do not name IN-18. No M0e re-measure is recorded after B-I [INFERRED from the extracts]. Otherwise none found.
- SOURCE: `v9_p4:58-94` (entry; table rows `:70-74`; §6 branches `:82-87`; §10 `:89-94`); state-index row `v9.md:257`.

````

### CR-07

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-07 | Retire the stored `scale:` column: delete `scale:`/`scale_note` from the 13 rows of `verb_table.yaml` that carry them, `VerbRow.scale` and its `RUNG_KINDS` check, and the guard tests (H-89; A1-46) | HELD (moved from B10-05 at its close: the pre-flight RAN and the cut waits, as the entry said it would; of 309 attempted acts of the 13 scale-carrying verbs (seeds 0-2, two seasons) `Act.via.scope` is missing on 19, all through one registry-derived seat, `off_npc_084` (guild leader, `rung` None), 18 refused and 1 `dispatch` executed; `exchange` and `succeed` mint no act in any run) · BUILD (deletion) when released: `via.scope` populated on that seat, or A1-46's own revert (keep the column and author a reader) | E | REM-2C (landed) | — | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:23-34`):

````
### CR-07 — Retire the stored `scale:` column (IN) · BATCH B10-Z (moved from B10-05 at its close) · STATE HELD · BUILD (deletion) when released · R —
- WHAT: A1-46 takes the answer (scale is `Act.via.scope`, not a column on the verb) but no position performs the cut. Delete `scale:` and `scale_note` from the 13 rows of `engine/season/verb_table.yaml` that carry them, the `VerbRow.scale` field and its `RUNG_KINDS` load check (`data/verbs.py:~860`), the guard test `test_governance_scale_is_a_rung_kind_and_is_crossed_with_the_stratum` and the `.scale` asserts at `test_season_shape.py:~5281` and `:~5386-5387`, and the stale header at `verb_table.yaml:66-79` (it still says nine rows).
- LANDED ALREADY: `Act.via.scope` and `Office.scope`.
- REMAINING UNBUILT: the deletion.
- GATE: B10-05's entry (met). The producer did not verify that `via.scope` is populated on every governance act: if it is not, the cut waits on that. B10-05 RAN THAT PRE-FLIGHT AND THE CUT WAITS (`hole_register.yaml` H-89's cite): of 309 attempted acts of the 13 scale-carrying verbs (seeds 0-2, two seasons) `Act.via.scope` is missing on 19, all through one registry-derived seat, `off_npc_084` (guild leader, `rung` None); 18 refused, 1 `dispatch` executed; `exchange` and `succeed` mint no act in any run. Released when that seat carries a scope (or A1-46's own revert is taken: keep the column and author a reader); the batch then re-runs the pre-flight.
- EXIT and FALSIFIER: the verb-table loader loads and `tests/test_season_shape.py` passes; `grep -n "scale:" engine/season/verb_table.yaml` finds none. Revert: A1-46's own (keep the column and author a reader).
- HASH MOVERS: none (an inert column).
- HOLES AND LEDGER IDS: H-89; A1-46; DEF-5.
- ASKS ATTACHED: none (A1-46 is taken).
- RE-BASE: count the rows by symbol; the count drifts.
- SOURCE: the hole-row pass, lane 2 and critic A.

````

### IN-58

card row (`valoria_master_workplan_v11_part3.md`):

```
| IN-58 | RS-23, RS-24 grievance at read: its sworn-to half | HELD (moved from B10-09 at its close two; not decided against): NARROWED, not built: the `oblige` edge IS person-side (`Person.tenures`), but no claim a judge holds pairs the victim with the seat (`Claim` has one `subject`; `person.died` and `tenure.closed` share only `when` and `round`). Reopening needs a carrier naming the dead holder in a death's claim: a CP-T02-01 follow-up and a Layer 2 shape change (stance-only half LANDED) · BUILD when that carrier exists | E | IN-12 (landed `f9e4cef`), CR-16 (landed `142e91e22`); not a dependency: IN-61 (IN-58's gate is IN-12 step 5's exit, `-04` IN-58) | — | carried in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:680-693`):

````
### IN-58 — RS-23, RS-24 grievance at read: its sworn-to half (IN, FA) · BATCH B10-Z (moved from B10-09 at its close two) · STATE HELD, NARROWED at B10-09 close two: the `oblige` edge is person-side, but no claim pairs a victim with the seat, so the sworn-to half is not built (stance-only half LANDED); the M1 hold is lifted (CR-16) · R R-07 (contributor)
- DECISION ROUND: the sworn-to half loses its M1 hold: CR-16 (B10-07b) ships `stance_polarity: declared`, the arm under which the grievance factor reaches candidate formation. Its own BLK (IN-40's `oblige` edge read person-side) stays; build or narrow at re-base. NEEDS gain CR-16 (B10-07b, closing commit `868fd6034`; landed `142e91e22`) and IN-12 (close one).
- WHAT: Build the sworn-to half of grievance-at-read: a judge sworn to the victim's seat reads a different regard for the killer than an unsworn judge with equal stance and pursuits. It ships OFF until IN-40's `oblige` edge is readable person-side. The stance-only half has landed.
- LANDED ALREADY: stance-only half `3bf936ee` (B-W, PR #477); faction-level grievance with IN-70 `f3e1b7b9` (H-225). Measurements recorded at B-W: M-who (every non-actor witness of a death/wound holds `seen.who`: realm 18/18 and 10/10, corpus 62/62 and 156/156); M-polarity (injected -25 stance, top candidate on the killer turns hostile under `legacy`/`regard`/`declared` in 0/0/7 of 12 realm and 1/1/29 of 58 corpus pairs).
- REMAINING UNBUILT: [v9 WHAT, full text: `person_q.deeds_judged` judges a `PAIRED_KINDS` deed once for its doer via `person_q.deed_doer`; value `_lean * _bond` (cell pairs `deed:person.died`, `deed:body.changed` in `rosters.yaml`; `_bond` from stored `stance_toward` only). What remains: the sworn-to half — a judge sworn to the victim's seat reads a different regard for the killer than an unsworn one — ships OFF because `person_q` reads a `PersonInterior` only and IN-40's `oblige` edge is a `World` Tenure read by a `world_q` reader.] the sworn-to half, as its own commit once the `oblige` edge is readable person-side. Not built either: the factor's reach to candidate formation at the shipped `stance_polarity` `legacy` (reaches only under `declared`, ED-IN-0296; CR-16 shipped `declared` in B10-07b, `142e91e22`).
- NARROWED (B10-09 close two): re-base read in code. A judge's own live, un-`imposed` `oblige` to a seat is in `Person.tenures` and outlives the victim, so the edge is person-side; the v9 blocker is gone. What is missing is the pairing: a death's seat reaches a ledger as `(seat, tenure.closed, True)` (`state/gate.py::Subject.seat`) beside `(victim, person.died, True)`, held firsthand by witnesses only, and `Claim` carries one `subject` and no pairing field, so the two share only `when` and `round`. Reading that as a pairing mis-pairs two deaths in one round (`deed_doer` declines to guess for the same reason). Observed by a planted death of a seat-holder through the real fold and WITNESS, every ledger dumped. Reopens when a claim names the dead holder with the seat (a CP-T02-01 follow-up, a Layer 2 shape change); no hole row is claimed.
- GATE: DEPS IN-40 -> sworn-to half (D: IN-40 landed `3f320093`; the edge must be read person-side first); IN-58 -> IN-12 step 5's EXIT (I). BLK until the `oblige` edge is readable person-side (D). LIMITS: allegiance only scales a pursuit lean; where the actor died attacking no killer is named. Revert: factor off and cells unauthored.
- EXIT and FALSIFIER: the sworn-to falsifier: "two judges with equal stance and pursuits, one sworn to the victim's seat, read different regard for the killer -> else that half is not built." v9 notes the entry's original EXIT "hash MOVED" is NOT MET: hash EQUAL at shipped `legacy` (`2eedf7b0…` before and after).
- HASH MOVERS: equal at shipped `legacy` (stated); the sworn-to half would be a declared mover wherever it executes [INFERRED].
- HOLES AND LEDGER IDS: H-194, H-209, H-225; ED-IN-0296; RS-23, RS-24, RS-29 (cells RATIFIED as authored), A-29 (REFUSED carriers [medium]).
- ASKS ATTACHED: ED-IN-0296's polarity question (H-194; v9_p5:124, :346) is answered: `declared`, by CR-16 (M1, `-05`; its revert is CR-16's).
- RE-BASE: landed at B-W (#477, #479); IN-70 landed B-X/B-R (`f3e1b7b9`, #496). B-Y (#502) added IN-59/IN-60 `guard_weight` (not this position). None found for the sworn-to half.
- SOURCE: `v9_p5:123-127`; state-index row `v9.md:269`.

````

### CR-85

card row (`valoria_master_workplan_v11_part3.md`):

```
| CR-85 | Histories, hooks and combat's input (`ED-IN-0330`, `ED-IN-0331`): the design of `proposals/2026-11-05-cr85-histories-hooks-and-combat-input.md` (landed `12325005`). BUILT, landed `95992146` (#577, B10-11 close three): `faculty` replaces `history` in combat's `pool` and `Ob` (`PersonalCombatInput.faculties`; `resolution_pool` and `ob_from_defender` keep their formulas; the five sigma reads of `history` deleted; export schema 5 to 6). REMAINS: the design's section 4 step 2, the seeded-damage crossing (HELD BACK by the build); the rest of the design's list that the build's receipt does not claim (where a lifepath writes a hook, the oracles' fate, the Health round trip and its consumers' re-bases); the port repo's copy of the export (outside this tree) | HELD (the build stands on an UNRATIFIED design: ratification withdrawn 2026-11-05, ED-IN-0351, PROPOSED and reopened with `faculty`'s role; built on the user's instruction of 2026-11-06) `[ASSUMPTION; medium; Jordan to correct; revert: delete the design file; history stays]` · slotted by R8 when the remainder is approved | M (every season fight; landed: seed 1 only in the shipped realm) | CP-T03-02 (landed `95992146`); PC-14 (landed `6732111a`) | the design's approval (ED-IN-0351) | written out in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:149-160`):

````
### CR-85 — Histories, hooks and combat's input: what replaces the `history` that is summed into rolls (PC, IN, WR) · BATCH B10-11 (after CP-T03-02, before CP-T03-05) · STATE BUILD (the design landed `12325005`, `proposals/2026-11-05-cr85-histories-hooks-and-combat-input.md`; ratification withdrawn 2026-11-05, ED-IN-0351: the design is PROPOSED and reopened with `faculty`'s role; unapproved when B10-11 opens, this build moves to B10-Z as HELD (the gate below)) · R R-09 (contributor)
- WHAT: `ED-IN-0330` and `ED-IN-0331` (Jordan, 2026-11-04): histories are eliminated as rolled integers, and a lifepath leaves hooks. What is eliminated, exactly, is the integer `history` summed into rolls: combat's `Combatant.history` (`modules/combat/combatant.py:93`), threadwork's term (`systems/threadwork/sim/operations.py:246`), knots (`systems/fieldwork/sim/knots.py:215-216`). The skill-shaped half already runs and is not eliminated: `Person.capability` keyed by `verb_capability`, `faculty` (`seam/wrappers/sigma.py:145-159`), `train`, the `practice` addend (`queries/world_q.py:4093-4113`), `tradition`, and CR-33's `lifepath_templates` (a lifepath expands into capability keys). `ED-IN-0330`'s "PRA" wording conflates the two (recorded by ED-IN-0333, the orchestrator's). It is a design, not a rename, because combat's `history` is the roll's backbone: pool `max(5, history + 6)` (`modules/combat/core.py:54-56`), obstacle `defender.history / 2.0` (`core.py:115`), read again at `combat_systems.py:171,332,1053,1421,1441`, exported to the port as `READ_HISTORY_K`, `INIT_HISTORY_K`, `BASE_POOL` (`engine/engine_params/combat_engine_v1.json:113,194,238`); in the season loop `history` is never authored (`seam/wrappers/combat.py:36-39` leaves the class default 3), so every season fight rolls pool 9 against Ob 1.5, and replacing it moves the hash of every season fight. The plan reference is `proposals/2026-11-04-knowledge-model-build-plan.md` §6 and §11 items 2 and 5 (reference, `CLAUDE.md` §0.05).
- REMAINING UNBUILT: the build. The design file (`proposals/2026-11-05-cr85-histories-hooks-and-combat-input.md`, landed `12325005`) answers (1) what replaces combat's `history` in `pool` and `Ob` and the season-loop hash cost, (2) what a hook is and where a lifepath writes it, (3) the oracles' fate, (4) the Health round trip (`-03` B10-11's re-base; one design with PC-14's storage) and (5) its consumers' re-bases (CP-T03-04, CP-T03-05, PC-14, PC-17, CP-T07-02); its section 4 step 2 is held back. In B10-11, after CP-T03-02 and before CP-T03-05, as the design states it, a declared mover of every season fight.
- GATE: the design landed `12325005` (ED-1094's merge default; section 4 step 2 held back). B10-11, after CP-T03-02 and before CP-T03-05; not B10-10b, which is declared EQUAL throughout and whose identity control would read a season-fight move as a defect `[ASSUMPTION; medium; Jordan to correct; revert: the build in B10-10b with its identity control re-based]`. NEEDS: `ED-IN-0330`, `ED-IN-0331`; the build needs CP-T03-02 and PC-14 (B10-10b).
- EXIT and FALSIFIER: its own falsifier, as the design states it: at the least, a season fight's pool and Ob read the replacement input and a planted person whose replacement input differs rolls a different pool; planted failure: the replacement read dropped reproduces pool 9 against Ob 1.5 and reddens; CONTROL: the replacement set to reproduce the class default reproduces the pre-item season hash.
- HASH MOVERS: the build a declared MOVER of every season fight (a PC-lane mover, not B10-09's), goldens re-recorded old to new in the commit body; the combat oracle's exports re-derived by their exporters with `--check`.
- HOLES AND LEDGER IDS: `ED-IN-0330`, `ED-IN-0331`; `hole_register.yaml:1352` (combat's "nine attributes" are `Combatant(strength, agi, end, cog, att, spirit, focus, history, disp)`, not the registry's; CR-84 does not touch them).
- ASKS ATTACHED: none open; Jordan's answers are `ED-IN-0330` and `ED-IN-0331`. Combat history's replacement is the design's choice by the ladder, the one worth his glance `[ASSUMPTION; medium; Jordan to correct; revert: delete the design file; history stays]`.
- RE-BASE: re-read `core.resolution_pool`, `core.ob_from_defender`, `seam/wrappers/combat.py` (`history` default; `party_end`) and CR-33's landed table (`6b068d8a`) by symbol at the build.
- BUILDER: opus; `valoria-author` for the build; its critic per `CLAUDE.md` §10.
- SOURCE: `ED-IN-0330`, `ED-IN-0331`; `proposals/2026-11-04-knowledge-model-build-plan.md` §6, §7 item 2, §11 items 2 and 5 (reference); `proposals/2026-10-24-character-progression-adjudication.md:64` (Jordan's earlier intent).

````

### SC-02

card row (`valoria_master_workplan_v11_part3.md`):

```
| SC-02 | `22a` -> `23` -> `22b`, RESIDUE after B-P: design written (`proposals/2026-11-08-sc02-reception-proofs-own-commit-design.md`), PROPOSED; the re-source build awaits its approval | HELD on the design's approval (ratified on merge by ED-1094's default) · BUILD (the re-source of `reception` and `proofs`) when released, slotted by R8 | M | — | — | carried in full: `-04` |
```

entry (`workplans/valoria_master_workplan_v11_part4.md:698-709`):

````
### SC-02 — `22a` -> `23` -> `22b`, RESIDUE after B-P (SC) · BATCH B10-Z (HELD; left B10-13 at its close) · STATE DESIGN WRITTEN for A1-08's option B (`proposals/2026-11-08-sc02-reception-proofs-own-commit-design.md`, PROPOSED, ratified on merge by ED-1094's default); the re-source BUILD is HELD on that approval · BLK for the rest: H-218, H-219, H-221, H-222, ED-SC-0040 (held; each left item sits at its hole row) · R —
- WHAT: residue only. Each left item sits at its hole row and is not buildable without the input named.
- LANDED ALREADY: at B-P (commits `07510eae..eba20137`): `22a` steps 17, 18, 20 (`reception`, `proofs`, route erosion; `Claim.visibility` KEPT, its reader runs from the fold); `23` (`SeatId`, `load_all()`, loader invariants 4's flat half and 7's fold half); `22b` step 23 (on a hand-built world), step 24 (except its Failure arm), step 25's writer and reader, step 26 (a test); step 27 found nothing to delete.
- REMAINING UNBUILT: step 19 (investigation products) STOPPED, superseded by #453 K-36 and K-37 (H-218; G2: SUPERSEDED, the asked-subject residue "3 of 8 asked subjects not co-located never learn they were asked" stays open); step 21 (failure's severity by observer set) STOPPED, no row has a Failure consequence to gate (H-219); step 24's Failure arm (H-221); step 25's rest (examiner witnessed examining; a forged record counted as a proof until examined), unscheduled; step 23's contradictory-commitments and overdue-obligation sources (no measure exists, H-222) and its realm life (never fires in computed play until a writer of person-predicates exists, step 19); the F8 question: `reception` and `proofs` read other persons' ledgers at RESOLVE against `04` §B.2:250 (ED-SC-0040; answered, option B, A1-08): the design is written and the re-source build (`reception` and `proofs` read the actor's own ledger and the bench's public commits) is HELD on its approval.
- GATE: v9 states no GATE line. STATE line: "B-Z, held. BUILT at B-P (the commits `07510eae..eba20137` are their record)". DEPS "ED-SC-0040 (J) for the F8 question; step 19's writer for steps 21's and 23's realm life."
- EXIT and FALSIFIER: v9 states none.
- HASH MOVERS: none stated.
- HOLES AND LEDGER IDS: H-218, H-219, H-221, H-222; limits of what was built: H-210, H-215, H-216 ("inert at the shipped ceiling; the mirror is total in play; the valence sweep is open; recusal; the bench's place; the uncapped arm's cliff"); per G2 also H-220 (`EventLog.append` takes any kind; refusal built at the fold; SC-02 `23` loader invariant 7) and H-223 (standing-gap bands, `22b` step 23); #453 K-36, K-37; ED-SC-0040, ED-SC-0039.
- ASKS ATTACHED: none open. ED-SC-0040 is answered (A1-08, ANSWERED-DOC, option B: re-source from commits). The design is written; its merge ratifies it by default (ED-1094), and its build, CP-T05-01 and CP-T05-02's part (i) (`hearing`, `hearing_step`) wait on that approval in B10-Z and slot by R8 into the next unopened verb-cluster batch when it is released. The only source text concerns the obstacle reading live commits to a charge, and no charge carrier exists (H-227).
- RE-BASE: B-P closed `eba20137` (#490) — v9 was written after it; the entry is "RESIDUE after B-P". B-O (#488/#489) FI-01/FI-02/FI-03 are the executors that superseded step 19. None found since B-P.
- SOURCE: `v9_p6:22-25`; state-index row `v9.md:271`.

````

### CP-T05-01

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T05-01 | The verdict hears the bench | HELD · BUILD, waiting on SC-02's approved design (its falsifier re-stated on that route) | M | CP-T01-04 (landed `967848b31`), CP-T01-06 (landed `60f32d138`), CP-T05-04, SC-02 | — | `cp-social-contest`:85-133 |
```

entry (`2026-10-23-subsystem-completion-05-social-contest.md:85-134`):

````
### CP-T05-01 · The verdict hears the bench

- **What it adds.** (i) `determine`'s `contests:` moves from `"a proposition"` to `"a matter"` (VT:383-384), the prize whose row already
  says `heard_by: "bench"` (ROS:1323-1328). No prize row changes; `a proposition` keeps `argue` alone. The room is then read at the act's
  place, as for `speak` (`SIG:253-256`). (ii) A third room operand, `opposed`: the bench's signed regard for the **opponent**, read by the
  existing `WQ::reception(w, opponent, venue)` (WQ:553-611) with the opponent in the speaker's slot. It is carried raw by
  `SIG::contest_input` (SIG:178-183) beside `reception`, and is `0.0` where the opponent is the actor or no person (the rule `proofs`
  already states, WQ:633). (iii) `ROLL::obstacle`'s room becomes
  `reception_gain · reception + proof_step · proofs − opposed_gain · opposed` (today `ROLL:104`). One formula for every prize a bench hears:
  `speak` gains the term too, so pressing a matter against a man the bench disvalues is easier, and against one it values harder.
- **Owner artifacts.** VT (one cell and its note); `queries/inputs.py::SocialContestInput` (one field, default `0.0`, the no-room
  reading); SIG (one read); ROLL (one term); FX `opposed_gain` with an HR row (NUMBER, swept `0` control / `0.5` / `1.0`).
- **Primitives.** P23 (seeded draw against a difficulty), P11 (pairwise regard, here judge to party), P27 (what the bench was told),
  P01 (a signed sum over holders). Template TM07 (testimony to verdict), whose verifier half is refused by axiom (D_T06:22) and is not
  built: the bench weighs what it holds, true or not.
- **Reads / writes.** Reads each seated judge's own ledger through `PQ::attributed_deeds` and `PQ::deed_term` (the reads `reception`
  already makes); writes nothing new. `determine`'s writes (VT:385-389) are unchanged; only its band distribution moves.
- **Joins.** GV: the bench is `WQ::judging_set` unchanged. FI: an inquiry's findings and `forge`'s documents reach judges' ledgers by
  existing deposits; nothing is asked of FI. PC: a killing or a wounding is a deed judges value through `deed:person.died` and
  `deed:body.changed` cells (ROS:3423-3424, 3485-3486); nothing is asked of PC. NP: each judge's valence is his own pursuits.
- **Decision handed to the chooser.** Whom to tell what, before the verdict; which bench to bring the matter before (its members'
  memories differ). **Unwatched:** every verdict in the realm now reads what that bench happens to know of the party, so two parties
  docketed alike fare differently, and a judge who saw the deed binds more readily than one who did not.
- ⚠ **Hearsay does not name a doer of violence, and this item keeps that rule.** A told copy of a `PAIRED_KINDS` claim names nobody
  (`PQ::attributed_deeds`, PQ:145-148): measured at HEAD the paired kinds are `body.changed`, `contest.undecided`, `finding.made`,
  `person.died`, `pursuit.moved`, `tenure.closed` (`PQ:190`, read by import). So a killing reaches the verdict through `opposed` only if
  a judge saw it; a witness who tells the judge of it moves nothing here, and moves the verdict instead by pleading (CP-T05-02). Unpaired
  deeds (a forged Record, a filed petition, a seizure) reach the bench by telling. Loosening the rule would change who counts as a doer
  in every reader of `attributed_deeds` (`reception`, `proofs`, `deeds_judged`, the scar), an asymmetry hazard this file does not take.
- **Falsifier.** A hand-built world: one judge holds one firsthand deed claim of the party's that his pursuits disvalue, at a magnitude
  giving `opposed_gain · opposed ≤ −1.0`; a second world identical but for that claim. At `opposed_gain = 1.0`, `determine`'s composed
  obstacle is 1.0 in the first and 2.0 in the second (the floor `OB_MIN` 1 and ceiling 2, `ROLL::obstacle`). The item is wrong if the
  two obstacles are equal, or if `argue`'s obstacle in the same worlds moves (its prize hears no room). **Under the derived-ceiling arm**
  (T01 CP-T01-06: the ceiling is the highest Ob at which a Success is still possible for the actor's pool, `2 · pool − 1` as filed, 3 at
  pool 2; never below `OB_MIN`, per the orchestrator's ruling R2): a third world where the judge *values* the deed at
  `opposed_gain · opposed ≥ +1.0` reads 3.0 against 2.0, which the shipped ceiling clips to 2.0. That half is observable on the derived
  arm only.
- **Control.** Three arms on seeds 0-2, two seasons, plus the hand-built worlds, **each run under both ceiling arms** (shipped `2`;
  derived, CP-T01-06): A today; B prize moved, `opposed_gain = 0`; C prize moved, `opposed_gain = 1.0`. Read per `determine` act the
  composed obstacle and band, and per `speak` the same. It can observe the failure: B against A isolates the prize move (the judge's own
  `reception` and `proofs` now read); C against B isolates the new term; derived against shipped isolates the hostile half. With T01's
  CP-T01-04 (the margin's fraction settled by the act's own draw) a room below 1.0 moves odds too, so the null reading in §7 holds only
  on the arm without it. ⚠ The realm forms one `determine` in three seeds (T05 §0), so the realm arms are weak and the hand-built
  worlds decide; say so in the commit.
- **Declared hash movers.** Arm B moves every world in which a `determine` rolls at a bench whose `reception` of the judge or whose
  `proofs` is non-zero; arm C also moves `speak`. T01 CP-T01-06 lists `determine` and `speak` among its movers (R2); with this item the
  bench room on `determine` is one of the things its derived arm un-clips. **Revert:** the prize cell; the field; `opposed_gain = 0`.
- **Assignment hazard (§0.1 pt 1).** No field's getter changes source. The composed obstacle is a pure function of the record; its one
  owner is `ROLL::obstacle`, and `test_sc01_obstacle_ceiling.py` already fails if a host-side obstacle returns (`queries/inputs.py:54`).

````

### CP-T05-02

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T05-02 | (i) `hearing` and `hearing_step`, re-specified on SC-02's route (parts (ii) and (iii) landed `c627426a`) | HELD · BUILD, waiting on SC-02's approved design | M | CP-T05-04, REM-28; SC-02; CP-T05-01 (part (i) follows it) | — | `cp-social-contest`:135-195 |
```

entry (`2026-10-23-subsystem-completion-05-social-contest.md:135-196`):

````
### CP-T05-02 · The bench remembers the hearing, and the accused may answer

- **What it adds.** (i) One Query, `WQ::hearing(w, matter, venue)`: over the seated bench (`judging_set`), the claims each judge holds
  whose subject is `matter` and whose predicate is a band kind of a row contesting `a matter` (read off those rows' own keyed `emits:`,
  never a second table: `speak`'s four, VT:1172-1176; after CP-T05-01, `determine`'s; after CP-T05-05, `interrogate`'s). Each counts
  `remove_weight(c.source) · c.confidence / full · DEGREE_STEP[band]` (`data/rosters.py:851`; `speak`: carried +2, advanced +1, held 0,
  turned −1), where a kind a row emits at more than one band counts 0 (`matter.determined` is emitted at three bands, VT:393-395, and
  the matter leaves the docket with it; `matter.undetermined`, Failure only, counts −1: a hearing the bench did not carry). The sign is
  **−1 where the act was the party's own** (the sighting's `who` is the matter), +1 otherwise. Positive is the case against the party. The method is `reception`'s (remove, confidence, a sum over the bench), so one
  hearing and one regard are weighed alike (S). (ii) A fourth room operand, `hearing`, carried by `SIG::contest_input` for a bench-heard
  prize, and `ROLL::obstacle`'s room gains `+ hearing_step · hearing`, so after CP-T05-01 `determine` reads it. (iii) A new row column,
  `subject_may_be_self: true` [coined here: *a contested row whose opponent is its `subject` may be formed by that subject on himself*],
  declared on `speak` alone. What bars a plea today is not a counterparty clause (`speak` declares no `counterparty:`, VT:1165, so the
  fold's self clause never fires, `loop/resolve.py:314-321`) but `opening_set`'s self-subject decline, `if opposes_subject and subject ==
  p.id` (`decision/options.py:261`, `subject_is_opponent` at :343-352). The column waives that one line for the row declaring it; the
  loader admits it only on a row `subject_is_opponent` reads as contested against its subject (no `counterparty:`), as it admits
  `counterparty_may_be_self` only where the fan reaches (`data/verbs.py:691-703`). `confer`'s `counterparty_may_be_self` is NOT the
  column: the loader refuses it on a row with no counterparty the known-person fan fills. So a docketed party forms a `speak` on his own
  matter: a plea. `choose.py:106`'s stance-polarity term reads his stance toward himself, which no stance row names (0) [UNVERIFIED].
  His opponent is then himself, so `opposition` is `None` and the obstacle starts at
  `obstacle_default`; `proofs` and `opposed` read `0.0` for a self-opponent (WQ:633's rule); `reception` is the bench's regard for him.
- **Why a Query and not a tally on the docket.** A written tally was drafted and cut at §3: the bench's memory of the hearing already
  exists in the judges' ledgers (WITNESS deposits every `speak` outcome to those present, T05 §2.3), it can be told onward, contested
  and forgotten (MATTER decay), and a stored tally would be the knowledge kept on the thing known (NERS §3, disqualifier 1).
- **Owner artifacts.** WQ (the Query); VT (`speak`'s column and note); `SocialContestInput` (one field); SIG (one read); ROLL (one term);
  FX `hearing_step` with an HR row (NUMBER, swept `0` control / `0.5` / `1.0`).
- **Primitives.** P25 (attrition-pool contest: a two-sided bar, Bannerlord's persuasion bar, Ace Attorney's gauge), P04 (the case
  advances across sittings), P03 (old pleading fades with the claims that carry it), P27.
- **Reads / writes.** Reads judges' ledgers and `speak`'s row; writes nothing. `speak` stays `writes: []` at every band (VT:1166-1171),
  so REM-06's third conjunct is still met by `determine`, not by `speak`.
- **Joins.** GV: a sitting (`convene`, REM-28 for its refusals) is where speaker and bench share a place; no interface change. NP: none.
  FI: none. The chooser lane: `speak`'s one alignment cell (ROS:3414) now prices a plea as well as a prosecution; whether that cell is
  right for a plea is the CELL-VALUE pass's.
- **Decision handed to the chooser.** Whether to plead, where (before the judges, or to a hearer who will tell them), and when: a turned
  speech is remembered against its side, so a weak speaker who presses can hurt his own case. The accused chooses whether to answer.
  **Unwatched:** persons who know a matter is docketed speak to it (CP-T05-04's docket question); judges present remember; the verdict reads it.
- **Falsifier.** A hand-built world: two judges co-located with three speeches on one docketed party (Success, Success by others; one
  Failure by the party himself). `hearing` = 2 × (1 + 1) firsthand, and the party's turned plea counts −1 × −1 = +1 per judge, so
  `hearing` = 6 at full confidence; at `hearing_step = 0.5` the verdict's room gains 3.0 and the obstacle sits at the floor. The item is
  wrong if `hearing` reads the same with the judges absent at the speeches (nothing was witnessed), or if the party's carried plea counts
  toward the case against him. **The plea itself, first:** a person docketed, holding the docketing claim, whose question carries his
  own matter, forms `speak {subject: himself}` under `subject_may_be_self` and forms none with the column removed (`options.py:261`
  declines it); a hand-built plea admitted by the fold rolls with `opposition` `None` and `proofs` 0. The item is wrong if the
  Candidate forms without the column (the decline is elsewhere) or fails to form with it.
- **Control.** `hearing_step = 0` against `0.5` on the hand-built world and seeds 0-2, **under both ceiling arms** (shipped `2`; derived,
  T01 CP-T01-06): at `0` every `determine` band is today's by construction; at `0.5` a `determine` whose bench holds `hearing ≥ 2` must
  show a lower obstacle on both arms, and one whose bench holds `hearing ≤ −2` (the party's pleas won) a higher obstacle on the derived
  arm only (the shipped ceiling clips it). Read also, in the realm, the number of
  bench-held `matter.*` claims per docketed matter: a zero there is a **null result to report**, meaning speakers and benches never share
  a place, not a pass.
- **Declared hash movers.** (i)+(ii) equal at `hearing_step = 0`. (iii) moves every world in which a docketed party is offered his own
  matter (new formations). **Revert:** the column; `hearing_step = 0`; the Query has no other reader.
- **[UNVERIFIED].** Which id a `speak` Event's deposits name: the matter by the empty-changes fallback (EI:509-514 says a `determine`
  Failure's claim lands on the party, which supports this) or the speaker by the `actor` rule (`epistemic.py:188`). `Claim` carries no event id (`state/carriers.py:291-319`), so if
  the deposit names the speaker the Query cannot find the matter, and the build must first make `speak`'s deposit name its matter
  through `claim_subjects`' rule roster (H-79), a declared rule choice, not a field. Conversely, if the deposit names the matter,
  `PQ::attributed_deeds` (an unpaired kind's claim is its subject's deed, PQ:144-145, `HR` H-192) already counts every speech about the
  party as the party's own deed, valued by `speak`'s cell, so CP-T05-01's `opposed` would count the hearing a second time; the build
  excludes the band kinds of `a matter`'s rows from `opposed` [ASSUMPTION; medium; revert: accept the double count and halve nothing]. Also: a told copy carries no `seen`
  (`PQ::attributed_deeds`, PQ:146-148), so a plea heard second-hand counts with the pressing sign [ASSUMPTION; medium; revert: told
  copies count 0].

````

### CP-T04-04

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T04-04 | The field is fought a round after it is declared: the warning and the defender's turn (exists only under Ask C (b); Ask C (a), same round, is taken) | HELD on M4 Ask C (b) (the optional question, confirmed at the default: same round, ED-IN-0301; it blocks no row of the nine) | M | CP-T04-07 (landed `1cdfcaf6`), MB-07r (landed `aa6871b8`), REM-31 (landed `96136014`); Ask C (b) | M4 Ask C (b) | `cp-mass-battle`:179-208; build file `proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-12.md` |
```

entry (`2026-10-23-subsystem-completion-04-mass-battle.md:179-209`):

````
### CP-T04-04 · The field is fought a round after it is declared: the warning and the defender's turn

- **Adds.** The `a field` prize row (`RY:1281`) gains one column, `fought_after: 1` (rounds), read by ENCOUNTER: the selection
  becomes "every declared, unfought act of this prize whose declaration is at least `fought_after` rounds old", read from the Event
  log and `w.acts` (both persistent `World` state, `state/world.py:207, 236`), instead of "this round's declarations" (`encounter.py:51-58`).
  Nothing new is stored: the declaration Event is the carrier, as it is today. A round-5 declaration is fought at the next season's
  round-1 ENCOUNTER (MATTER runs between: legs end, larders draw), so no round is safe from warning. `_survives` still refuses an act
  whose actor died meanwhile (`resolve.py:61`). Fixture `field_fought_after` (shipped `0`, today's same-round field).
- **Owner.** `engine/season/loop/encounter.py`; `RY: contest_subsystems.prizes` (the column, by prize, so `fight`'s deferral under
  REM-31 is untouched unless its own row sets it: no verb special case).
- **Primitives.** P23's information half (the defender sees the threat), P07 inverted (a commitment the attacker cannot take back
  once declared, except by CP-T04-03).
- **Reads / writes.** Reads the log. Writes nothing new; the field's own writes move one round later.
- **Joins.** **FI / WITNESS:** the defender must perceive `march.declared`. The act's place is the marcher's rung, so a presence
  channel delivers it at the origin, not the target; the interface needed is that a declaration whose subject is a Rung is also
  deposited for persons present in that Rung's subtree [UNVERIFIED which channel does this today]. **Decision layer:** REM-27's
  `fields_named` already offers a Rung the ledger names to `march`, so a defender told of the threat can march his own people to his
  own town (an `Unopposed` relocation, `loop/sides.py:121-132`): that is reinforcement, and it arrives a round after the attack it
  answers (relief comes late; named). **PC / REM-31:** both edit `loop/encounter.py`; this lands after REM-31 merges and re-runs its
  hash control, but it is **not bundled** with REM-31, which amends no Layer 1 text (`remediation-02:570-589`).
  **Layer 1 — this item amends it, so it waits on Ask C.** Ratified Layer 1 says `loop/encounter` reads "RESOLVE's own `Event[]`
  (selects `degree == Declared`)" (`architecture/meta/04_CODE_ARCHITECTURE.md:177`) and that the step "folds RESOLVE's own deferrals"
  (`:541-545`). Reading the log and `w.acts` across rounds is outside both lines.
- **Decision handed over.** The defender, between declaration and field: marshal a defence (CP-T04-02), surrender (CP-T04-07), leave
  (`move`), or call in relief. The attacker: the cost of warning the enemy. Unwatched: every NPC defender's chooser now gets a question
  about a real threat.
- **Falsifier.** A march declared in round r against a holder who surrenders in round r+1 fights no field (the place passes, no body
  or stance row is written); with `field_fought_after: 0` the same script fights the field before the surrender can fold. Plus the
  order-independence permutation REM-31 runs (`remediation-02:579-584`), with the delay on. **Control.** `0` is today, hash-equal.
  **Hash.** Mover on flip: every fought field moves a round. **Size** M.

````

### CP-T04-10

card row (`valoria_master_workplan_v11_part3.md`):

```
| CP-T04-10 | Raise and keep a force: the recruit pool, `levy`, the stock at the larder, and `disband` (rides Ask A); exit gains "a computed `levy` and a computed `disband` each execute once, `aperture 2 0`", else R-05 names both as residue | HELD on M3 (Ask A) | E | Ask A; J-C-2 answered: uncoupled (R-POOL) | M3 (Ask A) | `cp-mass-battle`:317-335; build file `proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-12.md` |
```

entry (`2026-10-23-subsystem-completion-04-mass-battle.md:317-336`):

````
### CP-T04-10 · Raise and keep a force: the recruit pool, `levy`, the stock at the larder, and `disband` (rides Ask A)

- **Adds, if Ask A answers A.** TS's positions as written, adopted as v9 positions: TS-3 (the pool, `recruits` in `Rung.stores`,
  regrowth at MATTER toward a ceiling from resident cohort weight, R-POOL), TS-L (re-keying the old `levy` citations), TS-4 (`levy`,
  `remit:dispatch`, with coin as a terms parameter, R-01), TS-11 (a stock eats where it stands, after the people), TS-5/TS-6/TS-8 (the
  order of battle at the seam and write-back on stocks and garrison), TS-7 (the computed levy). **One addition TS lacks:** `disband`
  (L10 Suite 1), `troops_<g>` → `recruits` on the same rung, capped at the pool's ceiling, grade lost, `army.disbanded`; without it a
  raised stock's only end is hunger or a field (TS1 §2.9; TS2 §9 lists "no stand-down verb" as a consequence of A). **What it
  supersedes:** IN-52's feed (TS1 §0 item 10 withdraws LF-1..LF-3), so v9's IN-52 is retired in the same commit that adopts TS-11.
- **Owner.** As TS2 §7 names them (`RY: matter_kinds`, `pool_rung_kinds`; `queries/world_q.py::fielded`, `settlement_above`;
  `loop/matter.py`; `VT` rows `levy`, `disband`; `SW::order_of_battle`). CP-T04-02's `marshal` Record replaces TS2 §4.3's `order`
  payload on `march` (L10's one-owner condition), and CP-T04-01's subunit-per-officer is TS2 §4.2 step 5.
- **Primitives.** P18 (a force capped by the pool), P20 (it eats each season), P02 (unfed, men leave), P16 (who is raised from where).
- **Layer.** Amends `04:793` and `04:802` (and their copies, TS1 §2.4): **Layer 1, by Ask A only.**
- **Decision.** Levy now (the pool's seasons of regrowth, and food) or keep the pool; keep a stock (food) or disband it (lose its
  grade). A consent cost (L10's cohort stance row, M-8) is TS's "weighed, not adopted" (TS1 §2.10) and is not added here. Unwatched: an
  over-levying NPC seat empties its larders (R-POOL's draw order feeds the people first, TS1 §2.5).
- **Falsifier.** TS's per position (TS2 §7), plus: a disbanded stock is re-levyable next season and draws nothing from the larder the
  season it is disbanded. **Control.** TS's arms. **Size** L.

````

