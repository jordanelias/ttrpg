# INST-BYZ-C — the hands of the chain: a document is answerable when the named bodies have entered it, and each entry is a clerk's act and a draw

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-14, X-19, X-22, X-24, X-25) — `carry`'s row is the SOCIAL1 verb lane's (`14_VERBS_SOCIAL1_D_grievance_and_settlement.md`; `13_SC_draw_for_unrolled_contests.md` states the same row differently and the two are listed for those lanes); the hand is that row's second `requires_typed` alternative, with the same band shape, and its three band kinds (`document.entered`, `document.held`, `document.returned`) are asked of the row's owner for a document that is not a petition; the terms are named members of the one roster (`backlog` for the clerk's open documents, `regard`, `obligation`, `subject`), and the `altonian_civics` step is leverage or the chooser's, not an obstacle term; the deposit at the last entry composes with `14_VERBS_BINDING_D_orders.md`'s `force` (a dead letter is entered and still binds nobody); a hand is a person and `remove` is space, and both apply; `procedure_draws` is not added. `passes_through`, `hand_term`, `office_bodies.term`, `hands_open` and the return at maturity stand. Every finding below stands.

Re-grounded: 2026-11-12 (audit §18) — no edit of this file changes; two things are added beside it (`15_INSTITUTIONS_BYZANTINE_grounding_mechanisms.md` items 3 and 4): a reading of what a hand's holder was given by the makers of papers in his hand (the purchased toll-post and its abolition, `research/rise_to_power_roster_system_research_v1.md:493-497`), and a gate that an entered instrument is citable evidence (the register as "a precedent file", `proposals/2026-09-05-proceedings-subsystem/source/06-part-V-dossiers.md:39`). The Byzantine chancery's own chain stays memory-grade; the sourced chains are cousins (Ming, Ottoman, papal: audit §18.2). The archived design had already used the *sekreton* for the Church's four arms (`.designs/systems/factions/reference/faction_politics_v30.md:965`), so `passes_through` may name a Church body as well as a Crown one.

Reconciled: 2026-11-12, U5d closure — folded **A-13** and **A-21**. The clerks an order passes (`passes_through`) are one of the three ruled seat facts; a seat declaring none has no hands. Under A-21 the terms of a decree travel with the news that it was issued, so a hand cannot keep an addressee ignorant of an order's terms; what a hand still does is hold, delay or alter the **entered instrument** (the paper that is cited, sealed and audited), which is where this file's draws apply.

Reconciled: 2026-11-12, wave 3 lane W3-4b — applied `R4_READ.md` §1.7 (BYZ_C: e6 "AMBIGUOUS leaning VIOLATES", F-R4-02), §2 (A-21 row: "BYZ_C body's 'not answerable until the last stage is entered' contradicts A-21"), §7, 7b.0, 7b.7 ("a writ's terms are known on learning of its issue; a `hand:` stage makes the entered instrument citable and sealed; an unentered stage whose due has passed reads as `returned` when read; MATTER … writes `Record.stages` nowhere"); `U3_CONFLICT_LEDGER.md` C3-C7, C3-C10, §9 ("`15_INSTITUTIONS_BYZANTINE_C` §1 (terms known on learning of the issue, A-21)"). Changed: the body now follows A-21 and this file's own U5d line, which it had not: entry seals the instrument (citable, audited) and does not gate the answers; edit 6's MATTER branch is withdrawn (the return is read when read); edit 7 no longer withholds a held writ; edit 5's terms are named members and levels (the `altonian_civics` step is removed, as this file's first `Reconciled:` line said); the controls are the pinned roll.

## Status: PROPOSED

**Implementation block (W3-4b; `R4_READ.md` 7b.0).** Lands in batch: **B33**, after BYZANTINE-B (`U3_DEPENDENCY_ORDER.md` §1 item 33). Depends on: `06_FA_decree_binds.md` and `14_VERBS_BINDING_D_orders.md` (B21: the content deposit; `force`), `13_SC_draw_for_unrolled_contests.md` (B07), `14_VERBS_SOCIAL1_D_grievance_and_settlement.md` (B28: `carry`'s row). Lane tag: FA (edit 5 is a cross-lane request to SOCIAL1-D's owner). Tier: `sonnet` producer, effort `high`; `opus` for edit 5's terms (a contested row). Named test: `engine/season/tests/test_inst_byz_c.py`. Standing sentences: *Pool* — `carry`'s pool is its row owner's, the one pool rule on the clerk's trained score (A-6, A-7, A-8). *Failure writes* — a Failure emits `document.returned` with the clerk as doer; WITNESS deposits it to the maker (A-81). *Draw keys* — `carry` at a hand draws `H(w.world_seed, w.tick, <record id>, "carry.hand")` (A-30).

Source: `audits/15_INSTITUTIONS_BYZANTINE.md` §2.3, §2.4, §3, §7.0, §7.1, §10, §14 item 1. Batch C.
Depends on `06_FA_decree_binds.md` (the content deposit that tells an addressee a writ's terms, and
the three answers forming on an addressed writ). Written for option (B) of §14 item 1; with no row
declaring `passes_through` it is option (A) and changes nothing. Ratifies nothing.

## What it changes in `engine/season/` at runtime

1. A seat row may name the bodies its instruments pass through. A writ issued through such a seat is
   minted with one open stage per body, each with a due tick. Its terms travel with the news of its
   issue (A-21: whoever learns a decree was issued knows its terms and may answer it); what waits on the
   last entry is the **entered instrument**: until then the paper is not sealed, cannot be cited as the
   issuer's act before a bench, and is not on the record an audit reads.
2. `carry` is offered to a person who holds a seat of the body an open stage names, on that document,
   wherever it lies within the issuing seat's purview. It is a draw (audit §7.0).
3. A hand stage whose due has passed unentered **reads** as returned to its maker (computed when read;
   MATTER emits `term.matured` for the Record as today and writes `Record.stages` nowhere; WITNESS
   deposits the `term.matured` to the maker). Recoverable: he may issue again.
4. With `passes_through` absent on every row (the control): no stage is a hand, `carry` is offered
   as today, and every hash is the base hash.

## The problem (evidence)

- `_declared_stages` (`loop/effects_information.py:177-194`) winds `record_stages_default` stages
  of `record_stage_term` each, labelled `stage1`, `stage2`. They are clocks with no hand: nothing a
  person does passes one, and nothing waits on one but `term.matured`.
- `arrangements.yaml` rows declare `interposed: [office, procedure, document]`; the loader validates
  the key (`data/arrangements.py:188`) and nothing else reads it (`grep -rn interposed engine/season
  --include=*.py`, less tests: the loader only).
- FA audit F-FA-01: 91 writs in nine realm seasons, none held or answered by an addressee. FA's fix
  makes a writ's terms public at issue. Three provided characters need the step between: NPC-008
  ("passively obstruct"), NPC-009 (absorbs every task; a single point of failure), NPC-011 ("delay,
  dilute, or fail to execute"), and canon's own "Ministry Collapse" card has no producer.
- `carry` requires a `petition` the actor holds (`requires_typed`), carries no `contests:` (audit
  E-2), and so a petition a clerk takes up is docketed with certainty.
- The body `Ministries` has one seat (`off_parliamentary_clerk`); the Lord Steward, "a Crown
  minister" by his case and his registry row, sits in no body (`offices.yaml:343-354`).

## The resolution, decided

A hand is a stage whose label names a body. Entering is `carry`. The clerk who does nothing is making
a choice through the one chooser (his ranking is sampled), at the cost of the scene he spends
elsewhere; the document's return at maturity is a clock, and it destroys nothing. Fees are not a
rule: a `give` to the clerk moves his regard for the giver, which is a `favour` level in his draw
(C3-C10) and a term in his ranking. Dilution at a hand (`construe`) is left to batch G, after FA's answers
land. Ladder step 5; the alternative considered was a delivery chain of `give`s, which FA measured at
one execution in two realm seasons.

## Exact edits

**1. `offices.yaml: seats[].passes_through`** — optional list; each member an `office_bodies` name
or a seat id (`{seat: <id>}`). Order is the order of entry. Authored:

| row | `passes_through` | basis |
|---|---|---|
| `off_king`, `off_duke_valorsmark` | `["Ministries"]` | `worldbuilding_v30.md` §6.1: the Ministries "execute government services" |
| `off_duchess_hafenmark` | `["Inner Council"]` | Hafenmark's "institutional order" (`geography_v30_infill.md:18`); her council holds the Legal Advisor `[ASSUMPTION; medium]` |
| `off_duke_varfell`, every Jarl seat | absent | "first among the Jarls, not a monarch"; Vaynard "wants … Altonian residue expelled" (`03_canonical_timeline.md:144`) |
| Church seats | absent | the papacy lane's |
| `off_katepano` | absent | a frontier command acts on its own seal (audit §2.6) |

**2. `offices.yaml: off_lord_steward.body`** — `null` → `"Ministries"` `[ASSUMPTION; medium; Jordan
to correct; revert: null]`. Ground: `cases/NPC4.yaml` NPC-009 ("A Crown minister who personally
absorbs nearly every important administrative task"). With it the Ministries hold two seats, and the
case's concentration is measurable as his share of entries.

**3. `rosters.yaml: office_bodies.term`** — new optional map, body → seasons a document may wait for
that body; absent reads `fixtures: record_stage_term` (shipped 1). Authored: `"Ministries": 2`
`[ASSUMPTION; medium]`; sweep 1 / 2 / 4. Where the hand is a seat and not a body, the same number
is the optional key `hand_term:` on that seat's own row (used by proposal D and by the spine's
`chancery` scenario, proposal F).

**4. `loop/effects_information.py::_declared_stages`** — when the act is exercised through a seat
(`Act.via`) whose `Office` carries `passes_through`, and the act declares no stages: the stages are
`[(due_i, "hand:<body or seat>", a.id)]`, with `due_i` the running sum of each hand's term from
`w.tick`. Otherwise unchanged. The label prefix `hand:` is the one new convention; the tuple shape
is unchanged, so `(Record, stages)`'s matrix row and `loop/matter.py`'s maturation read it as today.

**5. `verb_table.yaml: carry`** (the social verb family owns the row text; this is the institution's
requirement):

- `requires_typed` gains a second alternative: `existence` of `subject` kind `Record` with an open
  `hand:` stage, and `basis` of `subject`, basis `hand` (new basis rule in `data/requires.py`: the
  actor holds a live seat that is the stage's named seat, or whose `body` is its named body, and the
  document was drawn up at a rung the issuing seat's purview reaches). The petition alternative
  stands.
- `counterparty:` absent; `contests: a matter`; the draw.

| term | reads |
|---|---|
| pool | the row owner's (`14_VERBS_SOCIAL1_D`): the one pool rule on the clerk's trained score for `carry`'s capability |
| `difficulty` | by the rung kind of the issuing seat's rung (a realm instrument is harder to enter than a town's) |
| `backlog` (OBS member 23) | the open documents in the clerk's hands beyond his scene budget this season |
| `subject` (OBS member 4) | the document's `forgery_quality`, as an inquiry reads it (`seam/wrappers/sigma.py::contest_input`) |
| `regard` (OBS member 7) | the clerk's hostility to the maker (hostile half) |
| levels (leverage, C3-C10) | `favour` for the clerk's regard for the maker above zero; `obligation` where the maker and the clerk are sworn to one seat. The `altonian_civics` step is removed (this file's first `Reconciled:` line: leverage or the chooser's, not an obstacle term; no source is added for it) |

| degree | writes | emits |
|---|---|---|
| Overwhelming | the stage entered; the next hand's due tick brought forward by half its term | `document.entered` |
| Success | the stage entered | `document.entered` |
| Partial | the stage's due tick re-wound by one term of that hand, once per document per hand | `document.held` |
| Failure | the stage closed as `returned` (an ACTS write at RES, `(Record, stages)`, as `carry` already holds) | `document.returned` (the clerk its doer; WITNESS deposits `(record, document.returned, True)` to the maker) |

On the entry that closes the last `hand:` stage the instrument is **entered**: from that tick it is
sealed and citable (a held Record a party may cite before a bench, SC-P8; the register an audit reads).
The addressees' answers (`comply`, `evade / defy`, `construe`) do **not** wait on it: they form from the
news of the issue (A-21; FA's content deposit at issue, `06_FA_decree_binds.md`). Each answer is the
addressee's choice and its own draw; entry seals an order, and makes nobody obey.

`write_matrix.yaml`: `(Record, stages)` already lists `carry` at RES; its `emits:` gains the three
kinds. `[UNVERIFIED]` the row's present `emits:` list.

**6.** (Withdrawn, C3-C7: `loop/matter.py` is not edited.) An unentered `hand:` stage whose due has
passed reads as **returned by the clock** when read (`world_q.hand_returned(w, record)`, beside
`hands_open`; nothing stored); MATTER emits `term.matured` for the Record as today and writes
`Record.stages` nowhere; WITNESS deposits the `term.matured` to the maker, from which he reads the
return. Later hands' stages are read as void once an earlier one has returned. The maker's next `issue`
is a new document.

**7. `queries/world_q.py`** — `writs_held` (or FA's `writs_addressed`) is **not** narrowed (A-21: an
addressee answers what he has learned was issued); a new occasion beside `vacancies` and
`sittings_before`, `hands_open(w, p)`: the
Records with an open stage naming a body or seat `p` holds, as `Record` referents of a `need`
question. This is the reach half: without it a clerk is never asked. `[UNVERIFIED]` how the question
slot ranks it (`question_aggregation_rule: first`; H-54 is CORE's).

## Gate (execution artifacts)

1. *The draw.* 400 seeds, one hand-placed `carry` by the Clerk on a King's writ: all four bands
   occur; with the roll pinned to Success, every seed enters.
2. *The chain.* Realm, seeds 0 to 9, four seasons: of the writs issued through `off_king`, the counts
   entered, held over, returned by a clerk, and returned by the clock (read), per seed; at least one
   writ is entered and at least one is not, across the seeds; an addressee's answer forms on an
   unentered writ (A-21); the Lord Steward's share of
   entries reported. Control: `passes_through` deleted from every row reproduces FA's post-P2 hash.
3. *No deadlock.* The same run with both Ministries seats vacated at tick 0: the season completes,
   every King's writ returns by the clock, and `off_duke_varfell`'s writs are unaffected.

## Falsifier

Give the Clerk a `regard` of the maximum for one maker and the minimum for another, identical
documents, 400 seeds each: the entry rates differ. If they do not, patronage is not in the odds.
Remove `hands_open`: the count of `carry` attempts on writs falls to zero, which shows the occasion,
not the mechanism, is what reach depends on.

## NERS

N: without hands, an order's paper is sealed the moment it is issued and a clerk is a spectator; three provided characters
and one canon card lose their mechanism. Holds top-down (the issuer waits), bottom-up (the
petitioner's paper waits in the same hands), laterally (two clerks, one backlog), diagonally (a
duke's writ needs his own council and never the King's). R: enter, hold or return is a real choice
under a budget; the no-player half is the clerk's veto and the purge. Completeness: gate 3. S: the
stage tuple, the gate's write, `term.matured` and the contest seam are unchanged owners; "pauses
correctly" is the document itself, which waits while every other scale runs. E, against that: one
row key, one roster map, one basis rule, one occasion with its read-time return, and one row's terms.

## Cost class

Small build. Movers: any run in which a seat with `passes_through` issues.
