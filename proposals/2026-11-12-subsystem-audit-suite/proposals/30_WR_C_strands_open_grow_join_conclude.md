# WR-30-C — strands: how one opens, grows, is joined, concludes or fails to, and several at once

Reconciled: 2026-11-12, wave 3 (W3-3) — R3 §1 found it CONFORMS and R3 §2 found no ruling it contradicts; added: the serial order on `harness/storybar.py` (C3-K7), the batch (U3 B38), and the glossary's reading of "between regimes or inside one" (§4: `30_WR_B`'s creed bodies; "regime" in A-82's sense is `core_standing`'s, U1 glossary). Tier already named.

## Status: PROPOSED

Lands in batch: B38 (narrative and regimes), after `30_WR_A` and before `23_STORY_A` (U3 §1 item 38). Commit 2 edits `harness/storybar.py` after `30_WR_B`, before `30_WR_E` (C3-K7).
Depends on: `09_WR_strand_conclusion.md` (B12); `09_WR_B_draws_not_thresholds.md` edit 4 (B38); `20_NARRATIVE_A`, `20_NARRATIVE_B` (B38); `28_CORE_scene_access_C_the_petition_that_waits.md` (B38).

Source: `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md` F-30-06, F-30-07. Rulings: A-45 (several strands that can each end; a doer's later deed joins a strand he opened, or joins by its subject), A-46 (leaving a creed or a head seat is a move), A-80 (a held position must still move the world). Reference only (`CLAUDE.md` §0.05). Lane WR; owner file IN's (`engine/season/queries/world_q.py`).

Extends, and does not restate: `09_WR_strand_conclusion.md` (edit 1: an opening move is never terminal; edit 2: content openers leave `concludes`; edit 3: the same-doer link bounded; the A-46 step), `09_WR_B_draws_not_thresholds.md` edit 4 (a strand concludes only on its closing move's drawn degree), `09_WR_B_readings_of_closure_and_tension.md` (close by act, by term, by threshold), `09_WR_story_instruments_that_can_fail.md` edit 3 (the shape line), CR-97 (plot points and closure class per strand), CR-73 (natural shock), CR-67 (the burden opener).

## What it changes in `engine/season/` at runtime

| commit | change | hash |
|---|---|---|
| 1 | `_links` reads a strand's **subject** and its recent moves in place of every referent it ever named, behind `Fixtures strand_links` (`all` the control) | EQUAL at `all`; at `subject_recent` a **declared mover** through `flows_known` → `flow_stakes` → `questions_for` (the stamp ships on, `data/fixtures.py:1024`) |
| 2 | harness readings of a strand's state (open, concluded, dormant, revived) and its subject | EQUAL |

No strand is stored; no timer retires one; no state is written (T-a, R6).

## The problem, with evidence

- **Strands do not stay several.** Seed 0, two seasons (`strife 2 0 --strands`, audit §12, P-1): three strands, **all three read at the realm rung** (`per rung kind: realm 3`), `presented: 0 in 0 rung(s)`. WR's readings at three seasons: the largest strand holds 63 of 75 strand moves at seed 0 and 45 of 61 at seed 1 (`09_WR_strand_conclusion.md`, its E-07 and E-12). A-45 rules several strands; edit 3 of that proposal bounds the same-doer clause only.
- **The other clause is unbounded too.** `_links` (`world_q.py:5081`) links a move to a strand on any referent the strand has *ever* named (`s.refs`, grown by every move, `_Chain.take`, `:5054-5059`). A person or seat that many matters name (the head seat's holder; a bench) joins them all. `_move_referents` keeps the crown's office as a referent by an `[ASSUMPTION]` (`:5009-5011`).
- **Order carries nothing yet.** Adjacent code pairs against the shuffled control: `WN->WN` 9 observed, 8.23 control; `PT->PT` 7 against 6.25; none of the study's 16 links shown by any strand (P-1). A strand that is most of the log has the log's order, which is no order.
- **"Fails to conclude" has no reading.** R6: a flow "terminates or resolves with a concluding outcome, or it is not a flow"; "no timer retires a flow". So an unconcluded strand is open for ever in the world reading, and the study's commonest ending, XP "trouble persists" (20 of 102 cases, `strife-00` §4), is a `GAP` with no producer (P-1).
- **Nobody holds one.** After one season at seed 0, 0 of 83 persons hold a strand in their own reading (audit §12, P-2); the NARRATIVE lane read 1, 8 and 23 at four seasons (W7).

## The resolution, decided

### 1. What a strand is about: its subject

A strand's **subject** is the referents of its opening moves (and, for a content opener, its matter). It is fixed when the strand opens and widens only when another opening move joins. Later moves add **parties** and **referents** (for `open_referents`, the stamp and the telling) and do not widen what the strand is about.

**The linking rule, bounded (A-45's "or joins by its subject").** A move links to a strand when:
- it shares a referent with the strand's **subject**, or one rung step from it; or
- it shares a referent with one of the strand's **last three moves** (the study's own window, `harness/strife.py:269`, `LINK_WINDOW`), so a strand can travel as the cases do (R3: flows are mutable) and "capture, then execution" stays one strand; or
- the same doer did it and he opened the strand, or the move is itself an opener (`09_WR_strand_conclusion.md` edit 3, unchanged).

A referent named long ago and not since no longer joins anything. Ladder step 1 (A-45) for the bound; step 4 (the study's window is already the tree's window) for its size. `[ASSUMPTION; medium; Jordan to correct; revert: `strand_links: all`]`.

### 2. A strand's life, in the order it is lived

| stage | what happens | owner |
|---|---|---|
| **opens** | an `opens` kind; a challenger's or outsider's march; a death by `fight` or `accept`; the second claim or petition on one matter (`world_q.py:4768-4817`); leaving a creed or head seat (A-46); a natural shock (CR-73); a burden by writ (CR-67). An opening is always some drawn act or the world's drawn motion; nothing opens a strand on a count | as cited |
| **grows** | moves that link by the rule above; its rung is the lowest covering its moves, so it zooms (a hearth's quarrel, a duchy's) | `_strand_of` (`:5120`) |
| **is joined by persons** | one who holds its moves finds its stakes among his occasions (`flow_stakes`, `:5524`) and may act on them; acting makes him a party. One who lives within it and has heard nothing meets its stakes through CR-100's within-stamp, once built | CR-78 (landed), CR-100 |
| **is joined by another strand** | a move that links to two strands merges them, oldest id kept (`_attach`, `:5094`). Under the bounded rule this needs a shared **subject** or a recent move in common: two quarrels become one when someone makes them one | `_attach` |
| **turns** | a move that changes what holds it open: a restraint, a war, a docketed matter, a holder (CR-97 (a), read from the log) | CR-97 |
| **concludes** | its latest move is terminal, was not an opening, landed in a degree that closes (`09_WR_B_draws_not_thresholds.md` edit 4), and no open referent remains (`_concluded`, `:5158`). A later conflict move reopens it (rule (b)) | as cited |
| **fails to conclude** | below | this proposal |

### 3. Failing to conclude is a state with consequences, not a pause (A-80)

A strand that does not conclude is not still. While it is open:
- each open referent is a standing occasion for someone, by the stamps that exist: a prisoner (`detainees_held`, `world_q.py:3602`), a docketed matter (`matters_awaiting`, `:3633`), a war's enemy (CP-T09-02), its stakes (`flow_stakes`);
- the aggrieved party's due stays unmet and his regard for the one he believes owes it falls further with each lapse (`20_NARRATIVE_B`); a petition kept waiting intensifies (A-64, `28_CORE_scene_access_C`);
- other routes open to him (`30_WR_D` §4): another forum, a patron, an ally, force, forgery, flight, a rival claim.

Four states, each a reading (derived, never stored, no timer):

| state | reading | what it means in play |
|---|---|---|
| `open` | not concluded | live |
| `concluded` | `_concluded` | over; its slot frees |
| `dormant` | open in the world reading, and no living person holds an open strand of his own reading that shares its subject (his claims of it have faded, D-48, or their holders are dead) | R6 read honestly: for everyone alive it is no longer a flow. Its open referents remain facts: the man is still in the cell |
| `revived` | a strand that was dormant at a season's end and gains a move in a later season | the study's XP, "trouble persists": an old matter taken up again, by someone who found the prisoner, the paper or the grave. It now has a producer-free reading and needs no verb |

Dormancy is set by memory, which is persons', not by an age in the strand. A dormant strand takes no slot in `presented` (it is held by nobody, so nobody is shown it), which is the bound on L5 that CR-98's row says it lacks ("a strand's referent set only grows until it concludes").

### 4. Several at once, and their relation to the era

- Capacity is unchanged (A1: realm 1, duchy 2, then n+1; `flow_capacity`, `:4896`). With eras defined by rule and condition (`30_WR_A`), the realm's one slot is the era itself, so a second realm-wide strand no longer competes for it: it is a condition of the era or it is of the era.
- A strand is dated and named by the era it opened in ("a quarrel from the old king's time"); it can outlive the era, and an era turn is itself a move that joins every strand whose subject holds the head seat.
- A strand is **between creed bodies** or **inside one** (`30_WR_B`'s grouping; in A-82's sense a regime is read by `core_standing`, U1 glossary); it has **sides** per party (`side_against`, `:4868`); it has a **closure class** (CR-97 (a'): decider, roll, threshold, open). These four, with its subject and opening kind, are what `30_GO_F` names it from.

## Instructions to code

Tier: commit 1 third tier (opus: judgment on the linking rule, as S3 was), critic second; commit 2 second tier.

**Commit 1a (EQUAL).** `engine/season/queries/world_q.py`.
1. `STRAND_RECENT = 3` beside `flow_capacity`, tagged `[JUSTIFIED: the study's window for a windowed link, inherited, not fitted]`; `harness/strife.py:269` becomes `LINK_WINDOW = world_q.STRAND_RECENT` (one owner; the harness already imports `world_q`).
2. `rosters.yaml`: closed roster `strand_link_rules`, `values: [all, subject_recent]`; `data/fixtures.py`: `strand_links="all"` with the sweep comment `all (control, SHIPPED at 1a) / subject_recent`, refused outside the roster.
3. `_Chain` (`:5045`): add `subject: set` and `subject_parents: set`, filled in `take` when `mv.opens` (`mv.referents`, `_parents(rd, mv.referents)`), merged in `absorb`; add `def recent(self, n) -> set` returning the union of the referents of its last `n` moves by `index`.
4. `_links(m, up, s)` (`:5068`) gains `rule: str = "all"`. At `all` its body is today's, line for line. At `subject_recent`: `near = s.subject | s.recent(STRAND_RECENT)`; return true if `m.referents & near or up & near or m.referents & s.subject_parents`; else the same-doer clause as `09_WR_strand_conclusion.md` edit 3 leaves it. `_attach` (`:5094`) and the pulled-prior merge (`:5225-5226`) pass the rule; `flows_in` and `flows_known` read it once from `w.fixtures.get("strand_links")`.
5. `Strand` (`:4916`) gains `subject: frozenset = frozenset()`, set by `_strand_of`.
6. Tests, `engine/season/tests/test_strife_flows.py`: `test_links_all_is_byte_identical` (the realm's flows before and after, equal); `test_a_referent_named_long_ago_does_not_merge_two_strands` (strand X on rung A, strand Y on rung B; X names person K once, then four more X moves; a Y move names K: one strand at `all`, two at `subject_recent`); `test_capture_then_execution_is_one_strand` (an `arrest.made`, then a lethal `fight` on the held man within three moves: one strand in both arms); `test_a_strand_travels` (a chain of four moves each sharing a referent only with the one before: one strand); `test_the_person_reading_uses_the_same_rule` (planted ledger). `assert checked >= 5`.

**Commit 1b (declared mover).** Flip `strand_links` to `subject_recent`. Pre-change and post-change hashes at seeds 0, 1, 2; the strife guard on against off (CR-99's function if landed, else H-274's method: terminal-code histogram with the stamp reading each arm); re-record shared pins once.

**Commit 2 (EQUAL).** `engine/season/harness/strife.py::strands_block` (`:389`) and `harness/storybar.py`'s `on_season` hook.
1. `strife.py`: `def held_by_anyone(w, strand, known) -> bool`, where `known` is `{pid: flows_known(w, p)}` computed once per block: true if some living person has an unconcluded strand (`concluded_known`) whose referents meet `strand.subject`. `def strand_state(w, strand, known) -> str` in `("open", "concluded", "dormant")`. The strand line gains `state=<…> subject=<n ids> between|inside`.
2. `storybar.py --strands-life`: snapshots `{strand id: state}` each season; prints `revived=<n>` (dormant at season k, a new move by k+1) and `dormant=<n>`; per rung kind the number of open strands (so "several, at several rungs" is read, not assumed).
3. Tests, `engine/season/tests/test_strife_instrument.py`: `test_a_strand_nobody_remembers_reads_dormant` (planted: an `arrest.made` in the log, a live `detain`, every ledger emptied of it); `test_a_new_move_on_a_dormant_strand_reads_revived`.

## The gate (execution artifacts)

```sh
PYTHONHASHSEED=0 python -m engine.season.harness.strife 3 0 1 2 --strands
python -m pytest engine/season/tests/test_strife_flows.py engine/season/tests/test_strife_instrument.py -q   # covering files, at the close
```

Expected at `subject_recent`, against the `all` arm run beside it at the same seeds: (1) the largest strand's share of strand moves is below the `all` arm's at every seed (84% and 74% at seeds 0 and 1 in WR's reading); (2) `per rung kind` prints at least one kind below the realm at two seeds or more (today `realm 3` only, P-1); (3) the mean number of moves per strand stays at 2 or more; (4) at least one adjacent pair or drawn link beats its shuffled control at one seed or more, or the block says none does (reported, not required: order needs the closing verbs to execute); (5) the strife guard passes or reads BLIND and says so.

## The falsifier, and its control

- Mean moves per strand below 2 at `subject_recent`: the rule fragments (every move its own strand). Revert to `all` and keep only `09_WR_strand_conclusion.md` edit 3.
- The planted capture and execution reading as two strands.
- A strand's `subject` changing when a non-opening move joins.
- `dormant` printed for a strand some living person holds open (the join through subjects is wrong).
- Control: `all` is today's reading, byte for byte; the shuffled-membership control of CR-97 (moves re-dealt to strands of the same sizes) must read lower coherence than either arm.

## Dependencies

After `09_WR_strand_conclusion.md` (edits 1 to 3; this adds the referent bound beside its doer bound). Reads better after `20_NARRATIVE_A` (between or inside) and CR-97 (closure class). Feeds `30_WR_A` (realm-rung strands as conditions), `30_WR_E` (shapes), `30_GO_F` (named strands), CR-98 (L5's bound), CR-100 (a dormant strand stamps nobody).

## Layer 1

`04` §A.2 and §B.9 (a reading; the doer through `causes[]`; no person-side read of the act store): kept, **STRUCTURAL**; `flows_known` still fills the doer from `Claim.doer` only. T-a (nothing stored), T-b (a flow fires nothing): kept, **STRUCTURAL**. ID-16: commit 1b changes L1's and L5's reach (fewer, smaller strands stamp fewer referents): a damping, recorded on those rows, **CONVENTION**. `strife-00` §4's linking rule (A9) is narrowed under A-45; the master's text edit is owed with `09_WR_strand_conclusion.md`'s.

## NERS reading

- **N.** Without the bound, A-45's several strands become one within three seasons and every reading over strands (plot points, closure, order, the player's named stories) reads the log. Holds top-down (the realm shows several matters), bottom-up (one move joins one matter), vertically (a strand zooms by its own moves, not by a hub), diagonally (person and world readings share the rule).
- **R.** A matter that outlives memory and is taken up again is drama with no player in it. Complete at the extremes: a one-move strand is open and has a subject; an empty log has no strand; a strand with no route to any terminal code is printed by the route check as a defect.
- **S.** One linking rule for both readings; the study's window, already the tree's; no second definition of concluded.
- **E, last.** One set on a chain and one clause. A player can say what a strand is about, and so can the engine. High.

## Cost class

Small build (1a), a declared mover (1b), small build (2).
