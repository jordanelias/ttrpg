# INST-BYZ-C — the hands of the chain: a document is answerable when the named bodies have entered it, and each entry is a clerk's act and a draw

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-14, X-19, X-22, X-24, X-25) — `carry`'s row is the SOCIAL1 verb lane's (`14_VERBS_SOCIAL1_D_grievance_and_settlement.md`; `13_SC_draw_for_unrolled_contests.md` states the same row differently and the two are listed for those lanes); the hand is that row's second `requires_typed` alternative, with the same band shape, and its three band kinds (`document.entered`, `document.held`, `document.returned`) are asked of the row's owner for a document that is not a petition; the terms are named members of the one roster (`backlog` for the clerk's open documents, `regard`, `obligation`, `subject`), and the `altonian_civics` step is leverage or the chooser's, not an obstacle term; the deposit at the last entry composes with `14_VERBS_BINDING_D_orders.md`'s `force` (a dead letter is entered and still binds nobody); a hand is a person and `remove` is space, and both apply; `procedure_draws` is not added. `passes_through`, `hand_term`, `office_bodies.term`, `hands_open` and the return at maturity stand. Every finding below stands.

Re-grounded: 2026-11-12 (audit §18) — no edit of this file changes; two things are added beside it (`15_INSTITUTIONS_BYZANTINE_grounding_mechanisms.md` items 3 and 4): a reading of what a hand's holder was given by the makers of papers in his hand (the purchased toll-post and its abolition, `research/rise_to_power_roster_system_research_v1.md:493-497`), and a gate that an entered instrument is citable evidence (the register as "a precedent file", `proposals/2026-09-05-proceedings-subsystem/source/06-part-V-dossiers.md:39`). The Byzantine chancery's own chain stays memory-grade; the sourced chains are cousins (Ming, Ottoman, papal: audit §18.2). The archived design had already used the *sekreton* for the Church's four arms (`.designs/systems/factions/reference/faction_politics_v30.md:965`), so `passes_through` may name a Church body as well as a Crown one.

Reconciled: 2026-11-12, U5d closure — folded **A-13** and **A-21**. The clerks an order passes (`passes_through`) are one of the three ruled seat facts; a seat declaring none has no hands. Under A-21 the terms of a decree travel with the news that it was issued, so a hand cannot keep an addressee ignorant of an order's terms; what a hand still does is hold, delay or alter the **entered instrument** (the paper that is cited, sealed and audited), which is where this file's draws apply.

## Status: PROPOSED

Source: `audits/15_INSTITUTIONS_BYZANTINE.md` §2.3, §2.4, §3, §7.0, §7.1, §10, §14 item 1. Batch C.
Depends on `06_FA_decree_binds.md` (the content deposit that tells an addressee a writ's terms, and
the three answers forming on an addressed writ). Written for option (B) of §14 item 1; with no row
declaring `passes_through` it is option (A) and changes nothing. Ratifies nothing.

## What it changes in `engine/season/` at runtime

1. A seat row may name the bodies its instruments pass through. A writ issued through such a seat is
   minted with one open stage per body, each with a due tick, and is **not answerable** until the last
   is entered: FA's content deposit to addressees happens at that entry, not at the issue.
2. `carry` is offered to a person who holds a seat of the body an open stage names, on that document,
   wherever it lies within the issuing seat's purview. It is a draw (audit §7.0).
3. At MATTER, a hand stage that matures unentered returns the document to its maker: the stage
   closes as `returned`, the maker is told, and nothing else is written. Recoverable: he may issue
   again.
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
rule: a `give` to the clerk moves his regard for the giver, which is a `favourable` term in his draw
and a term in his ranking. Dilution at a hand (`construe`) is left to batch G, after FA's answers
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
| pool | `faculty(w, p, "carry")`; `verb_capability.carry` → `copying` (the vocation exists in `vocation_attribute`) |
| `difficulty` | by the rung kind of the issuing seat's rung (a realm instrument is harder to enter than a town's) |
| `hostile` | one step per open document in the clerk's hands beyond his scene budget this season (the backlog) |
| `subject` | the document's `forgery_quality`, as an inquiry reads it (`seam/wrappers/sigma.py::contest_input`) |
| `favourable` | one step each: the clerk's `regard` for the maker above zero; the maker sworn to a seat the clerk is sworn to; the clerk's `conviction_stand(altonian_civics)` above zero |

| degree | writes | emits |
|---|---|---|
| Overwhelming | the stage entered; the next hand's due tick brought forward by half its term | `document.entered` |
| Success | the stage entered | `document.entered` |
| Partial | the stage's due tick re-wound by one term of that hand, once per document per hand | `document.held` |
| Failure | the stage closed as `returned`; a firsthand claim on the maker, `(record, document.returned, True)`, with the clerk as its doer | `document.returned` |

On the entry that closes the last `hand:` stage, the effect performs FA's content deposit for the
document (`06_FA_decree_binds.md`, the `loop/witness.py` route): from that tick its addressees are
offered `comply`, `evade / defy` and `construe`. Each of those is the addressee's choice and its own
draw; entry makes an order answerable, and makes nobody obey.

`write_matrix.yaml`: `(Record, stages)` already lists `carry` at RES; its `emits:` gains the three
kinds. `[UNVERIFIED]` the row's present `emits:` list.

**6. `loop/matter.py`** — where a stage matures: if its label starts `hand:` and it was not entered,
the Record is not marked `matured`; the stage closes as `returned`, `term.matured` is emitted as
today, and WITNESS deposits `(record, document.returned, True)` on the maker with no doer (nobody
acted). Later hands' stages are dropped. The maker's next `issue` is a new document.

**7. `queries/world_q.py`** — `writs_held` (or FA's `writs_addressed`) excludes a document with an
open `hand:` stage; a new occasion beside `vacancies` and `sittings_before`, `hands_open(w, p)`: the
Records with an open stage naming a body or seat `p` holds, as `Record` referents of a `need`
question. This is the reach half: without it a clerk is never asked. `[UNVERIFIED]` how the question
slot ranks it (`question_aggregation_rule: first`; H-54 is CORE's).

## Gate (execution artifacts)

1. *The draw.* 400 seeds, one hand-placed `carry` by the Clerk on a King's writ: all four bands
   occur; with `procedure_draws: off`, every seed enters.
2. *The chain.* Realm, seeds 0 to 9, four seasons: of the writs issued through `off_king`, the counts
   entered, held over, returned by a clerk, and returned by the clock, per seed; at least one writ
   becomes answerable and at least one does not, across the seeds; the Lord Steward's share of
   entries reported. Control: `passes_through` deleted from every row reproduces FA's post-P2 hash.
3. *No deadlock.* The same run with both Ministries seats vacated at tick 0: the season completes,
   every King's writ returns by the clock, and `off_duke_varfell`'s writs are unaffected.

## Falsifier

Give the Clerk a `regard` of the maximum for one maker and the minimum for another, identical
documents, 400 seeds each: the entry rates differ. If they do not, patronage is not in the odds.
Remove `hands_open`: the count of `carry` attempts on writs falls to zero, which shows the occasion,
not the mechanism, is what reach depends on.

## NERS

N: without hands, an order's force is immediate and a clerk is a spectator; three provided characters
and one canon card lose their mechanism. Holds top-down (the issuer waits), bottom-up (the
petitioner's paper waits in the same hands), laterally (two clerks, one backlog), diagonally (a
duke's writ needs his own council and never the King's). R: enter, hold or return is a real choice
under a budget; the no-player half is the clerk's veto and the purge. Completeness: gate 3. S: the
stage tuple, the gate's write, `term.matured` and the contest seam are unchanged owners; "pauses
correctly" is the document itself, which waits while every other scale runs. E, against that: one
row key, one roster map, one basis rule, one occasion and one row's bands.

## Cost class

Small build. Movers: any run in which a seat with `passes_through` issues.
