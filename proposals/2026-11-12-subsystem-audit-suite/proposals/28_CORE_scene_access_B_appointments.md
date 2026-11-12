# 28 · CORE · SCENE ACCESS · B — an appointment is the host's own commitment, and what a visitor of lower rank can do

## Status: PROPOSED (a plan for future execution; nothing here is executed by the authoring lane)

Carries `audits/28_SCENE_ACCESS.md` §4. Serves Jordan's A-64 (2): *"for appointments to be made"*
(`unified/DECISIONS_ANSWERED.md`; its marked assumption: *an appointment is a commitment between two
persons (an existing kind), not a stored schedule; no Layer 1 clock*). Needs proposal A
(`28_CORE_scene_access_A_occupancy_and_precedence.md`) for the precedence draw that honours it. Reference
only (CLAUDE.md §0.05). Not ratified by being written.

## What it changes in `engine/season/` at runtime (first)

With the new fixture `appointments` at `off` (the control): nothing. Built:

1. A person who was kept waiting can form an `utter` whose Proposition is an **ask for audience**
   (`OUGHT`, subject the host, predicate `receives`, value himself).
2. A host's `commit` to such a Proposition opens his `commit` Tenure with a **declared term**; MATTER's
   existing term branch closes it when the term comes.
3. One read, `world_q.appointment_with(w, host, visitor)`, answers whether such a commitment is live; the
   precedence draw of proposal A adds a level for it.
4. Three reads say whether an appointment was kept, lapsed unused, or lapsed with the visitor turned
   away; the chronicle and the grievance clause of proposal C read them.

No verb, Record kind, carrier field, `World` member or calendar entry is added. A declared hash mover
only in a world where a host commits to an ask.

## The problem (evidence)

- Under proposal A a busy person can be reached only by trying again. Each attempt costs the visitor a
  scene and is redrawn from nothing: there is no way to hold a place.
- The engine already has every part of a promise between two people: `utter` mints an immutable
  Proposition and the utterer's hold (`loop/effects_information.py:1215-1244`); `commit` opens a Tenure
  owned by its subject on a Proposition (`:1253-…`; `verb_table.yaml` `commit`, `own`-eligible), and it
  executes in computed play (65 `commit` acts among the 446 that wrote, two seasons at seed 0,
  PES_CORE's `p34_s0_k2.txt`);
  `Tenure.term` is a declared end MATTER matures for a live edge of any kind (`state/carriers.py:42-68`;
  `loop/matter.py:428-434`, `causes = [term.declared_by]`); `release` closes a `commit` and emits
  `commitment.ended` (`verb_table.yaml` `release`, `emits_note`: *"the vow-break is witnessed HERE"*).
- The formal appointment exists too: a carried petition is a `DocketItem` with a dated slot at a
  sitting (`verb_table.yaml` `carry`, `convene`; `queries/world_q.py::matters_awaiting`, `:3633`), and
  `14_VERBS_SOCIAL1_D_grievance_and_settlement.md` §1 makes admission to that queue a draw with a
  `backlog` term.
- Nothing connects either to who is seen first.

## The resolution, decided

Ladder: step 1 for the carrier (A-64's assumption names a commitment of an existing kind); step 4 for
every mechanism (each is an existing owner, named below); step 5 for the choices marked **(decided
here)**.

### 1. The ask: an audience Proposition, uttered by the one who wants the meeting

`Proposition(mood="OUGHT", subject=<host>, predicate="receives", value=<visitor>)`. The predicate and
its mood live in one new closed table, `rosters.yaml: termed_promises` (edit 1), read by every site
below; no site spells the string.

- **Who forms it.** A person holding his own firsthand claim that he was kept waiting at that host's
  door (the `visitor.kept_waiting` Event of proposal A names the host as its subject; he is its doer).
  `decision/options.py` derives the `said` cell from that claim through the operand derivation
  `14_VERBS_SOCIAL2_B_a_word_with_content.md` §1 adds for `utter` (*"a person says what he holds"*): a
  claim of a kind listed in `termed_promises.<predicate>.asked_on` yields
  `Said(host, "receives", actor)` in the `OUGHT` mood. `[UNVERIFIED: that derivation is proposed, not
  built; this row lands in the same commit as it or after]`.
- **How it reaches the host.** As any utterance does: those present hear it
  (`epistemic.py`'s co-location channel), so a host too busy to be spoken with still hears that he was
  asked, and so do his people; it travels on by `tell`; and a `petition` may carry it as its `terms`
  (`U5c_SC_proceedings_residue.md` §8: a petition's terms are a Proposition), which is the paper route
  through a clerk (§4 below).
- **Its draw.** `utter`'s own (S2-B §1: whether the room believes him). An ask the room does not credit
  is uttered and travels no further by the told deposit.

### 2. The grant: the host's own `commit`, with a term

The host forms `commit` on the Proposition as he forms it on any Proposition a question of his carries
(`verb_table.yaml` `commit`, `referent_class: Proposition`). Whether he ranks it above his other
business is his chooser's score (§6). Whether it takes is `commit`'s draw
(`14_VERBS_SOCIAL1_D_grievance_and_settlement.md` §4: pool `resolve`, obstacle `plain` +
`cross_pressure` + `violated`; Failure writes nothing and emits `commitment.refused`), and its band is
the Tenure's `degree`.

**The term.** `_eff_commit` gives the new edge `Term(w.tick + n, a.id)` when the Proposition is a
self-binding promise the table lists: `mood == OUGHT`, `subject == a.actor`, and `predicate` a key of
`termed_promises`, `n` being the fixture that row names (`appointment_term`). Any other commit is
untermed, as today. The edge is the host's own, opened by his own act (T-m); no one else's act opens or
closes it, and nothing is scheduled: the end is a term the opening act declared, matured by MATTER at a
season boundary (T-n; `04` PART D row 17's MATTER token), which is what `oblige` already does.

**(decided here) An appointment is standing leave for its term, not one slot.** While the commitment is
live the visitor has the level in every precedence draw he enters against that host. Not chosen: closing
the edge at the first meeting, which needs a write to the host's Tenure caused by the visitor's act,
a tenth exception to the owner rule (`04` PART D row 10a) for no gain a reader can see.

**(decided here) `appointment_term = 2`**, swept `1 / 2 / 3` `[ASSUMPTION; medium; Jordan to correct;
revert: 1]`: at 1 a promise made in a season's last round is closed by the next MATTER before any round
in which it could be kept.

### 3. Honoured, missed, broken: reads of what the log already holds

`queries/world_q.py`, beside `writs_held` (one owner each; nothing stored):

```python
def appointment_with(w, host: str, visitor: str) -> Optional[Tenure]:
    """The host's LIVE `commit` to a termed-promise Proposition whose subject is `host` and whose value is
    `visitor`, or None. Read by the precedence draw (proposal A §4)."""

def appointment_outcome(w, t: Tenure) -> str:
    """For such an edge, live or ended: `kept` (an admitted occupying act by the visitor naming the host,
    emitted within the edge's span); `withdrawn` (ended before its term: the host's `release`);
    `turned_away` (ended at its term, or still live, with a `visitor.kept_waiting` of that visitor at
    that host inside the span and no admitted visit); `unused` (ended at its term with neither)."""
```

| what happened | how it is read | what follows, and by which existing path |
|---|---|---|
| kept | `kept` | nothing more: the meeting's own bands |
| the host withdraws | `withdrawn`: his `release`, `commitment.ended` | a witnessed vow-break, judged by those who hold it through `person_q.deeds_judged` (authored `deed:commitment.ended` cells) |
| the visitor came and was not seen | `turned_away` | the visitor's grievance clause (proposal C §2): a promise lapsed unmet at the host's door |
| the visitor never came | `unused` | the term's `tenure.closed` is in the log, citing the host's commit; the chronicle tells it; no rule adds a penalty |

**The level.** In the precedence draw: `appointment_level` where the edge's `degree` is Overwhelming or
Success; one `precedence_level` where it is Partial (a grudging leave). An appointment is usually
honoured and sometimes not: the king arrives, or the host's own business draws high.

### 4. What a visitor of lower rank can do (each an existing act; none a gate)

| route | acts | whom it occupies | its draw | source in the tree |
|---|---|---|---|---|
| wait and call again | the same visit next round | the host, if admitted | precedence, then the visit's own | proposal A; retry is discounted by `16_PESSIMIST_CORE_a_refusal_is_remembered.md` |
| ask for an appointment | `utter` the ask; the host's `commit` | nobody until kept | `utter`'s; `commit`'s; precedence with the level | §1 to §3 |
| send someone who can get in | `tell` or `give` to a person of higher office or with standing leave, who visits | the intermediary, then the host | each act's own | `verb_table.yaml` `carry.held_note`: *"`give` can hand it on, so a petition can be carried by another hand"*; `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md` §8.1 (*who carried the petition shaped its success*) |
| the clerk's hand (A-13) | file a `petition`; tender it to a clerk of a body the host's seat declares in `passes_through`; the clerk's `carry` enters it | the clerk, not the lord | the clerk's `carry` (bands entered / held / returned; hostile term: papers in his hands beyond his scene budget) | `15_INSTITUTIONS_BYZANTINE_C_the_hands_of_the_chain.md` |
| the room | `petition`, then `carry` it oneself to a venue that admits petitions | nobody | `carry`'s, with `backlog` | `14_VERBS_SOCIAL1_D_grievance_and_settlement.md` §1 |
| over his head | a `petition` addressed to a holder of a seat above | nobody | as the room | `14_VERBS_SOCIAL2_B_a_word_with_content.md` §3 (`to` fanned over the seat-holders he knows); A-22: *a writ to a superior is a petition* |
| other means, or giving up | proposal C §4 | | | |

A paper needs no audience: `petition`'s cell asks no `with`, and Layer 1 keeps petitions uncapped
(`holonic_ARCHITECTURE.md` §26.3: *"No dedup, no cap, no per-venue limit"*). What is scarce is the
person, never the right to write to him.

### 5. The formal appointment is the docket's dated slot, and a sitting seats those who attend

No edit to the docket. Two statements so the two kinds of appointment do not diverge:

- A docketed matter's date is its appointment with the bench; what delays it is the convener's and the
  determiner's own scenes, which proposal A makes scarcer, and the clerk's and the room's `backlog`
  terms, which already read it.
- When `05_SC_playable_hearing_B.md`'s sitting runs, each attendee who moves in it is engaged in it for
  that round by proposal A's read; an attendee already engaged elsewhere is absent, and the sitting's own
  `silence` rule applies to his side. Folded there.

### 6. What the chooser reads (no new rule; `decision/choose.py::score_terms` stays the one owner)

| who | decides | from |
|---|---|---|
| the visitor | to ask, rather than call again | he holds a `visitor.kept_waiting` claim, so the ask is a Candidate; calling again is discounted by `admission_weight`; the ask's believed chance is `odds_weight`'s |
| the host | to grant | the `commit` Candidate's ordinary score: the lean of the matter on his pursuits, his regard for the asker, and his believed chance of the draw; a hostile or indifferent host seldom grants, one whose pursuits the visitor serves grants early |
| the host | to withdraw | `release` on his own edge, as for any commitment he no longer stands behind |
| a player | either side | the same Candidates on the same surface (`harness/play_surface.py`); an ask for audience addressed to the player's person arrives as a question on his slate (A-48) |

## Exact edits, by owner (in landing order)

1. **`engine/season/rosters.yaml`** — new closed table
   `termed_promises: {receives: {mood: OUGHT, term: appointment_term, asked_on: [visitor.kept_waiting]}}`,
   loaded and validated by `data/rosters.py` (`term` a fixture name; `asked_on` Event kinds the verb table
   derives). Adding a second termed promise later is a row.
2. **`engine/season/loop/effects_information.py::_eff_commit`** — the term (§2). `_declared_term`'s
   `Term(w.tick + n, a.id)` shape (`loop/effects_governance.py:39-55`), moved to `loop/effects_shared.py`
   so both effects call one constructor.
3. **`engine/season/verb_table.yaml`** `commit` — `writes:` gains `Tenure.term` (check-only, `oblige`'s
   and `confer`'s precedent: the fold gates exactly the pairs a verb declares).
4. **`engine/season/queries/world_q.py`** — `appointment_with`, `appointment_outcome`.
5. **`engine/season/decision/options.py`** — the ask's `said` (§1), inside S2-B's derivation.
6. **`engine/season/loop/resolve.py`** — the precedence draw's second level (proposal A §4) calls
   `appointment_with`.
7. **`engine/season/harness/chronicle.py`** — one line class per `appointment_outcome` value.
8. **`engine/season/data/fixtures.py`** — `appointments: off | on`; `appointment_term`; register rows at
   build.

## Gate (execution artifacts, §0.2)

| # | reading | passes when |
|---|---|---|
| 1 | control `appointments: off` | hash equal at every seed |
| 2 | realm, seeds 0 to 4, four seasons, proposal A on | asks uttered above zero at three seeds; hosts' commits to them above zero at two; outcomes reported in the four classes |
| 3 | planted: one host, two visitors of equal office, one holding an appointment, 400 seeds | the appointed visitor is first more often; never always |
| 4 | planted: a commit at tick t, `appointment_term` 2 | the edge closes at the MATTER of tick t+2 with `tenure.closed` citing the commit; `appointment_with` is `None` after |
| 5 | planted: two hosts alike but for their stance toward the asker (minimum, maximum), 400 seeds | the grant rates differ; neither is 0 or 1 |
| 6 | no schedule | `World.dates` holds the same entries with `appointments` on and off in the planted world; no carrier gains a field |

If row 2 reads zero at every seed, the shipped chooser does not reach the personal route. That is
reported as the result; the docket route (§5) then carries A-64 (2) alone, and no further build is
started from this file.

## Falsifier

A host's `commit` opened or closed by an act that is not his own, or by no act and no matured term. An
appointment live past its term. `appointment_level` added for a visitor with no live edge. An outcome
class that cannot occur at any seed in the planted worlds.

## Layer 1 rows

T-m and T-n (the owner's own act; a declared term MATTER matures: `04` §B.8's `term?`, as
`state/carriers.py:42-68` records it): conform. PART D row 10a (a write by a non-owner): conform, by the choice in §2.
Row 17 and row 21 (no fourth clock; no rung with a clock) and `holonic` §29 (no clock at CENSUS): conform:
the only time read is an act-declared term at MATTER. Row 30b (a Proposition is immutable; a Tenure is
never deleted): relied on. Row 44 (a belief is a `commit` to an `OUGHT`): an appointment is one.

## NERS reading (E last)

- **N.** Cut it and waiting is the only way to reach a busy person, so rank alone decides access and the
  low-born have no move but persistence. Top-down: the ruling. Bottom-up: `utter`, `commit`, `Term` and
  `release` exist and none is edited in kind. Laterally: an oath to a seat is a termed edge; this is a
  termed edge to a person's word. Diagonally: the docket's slot is the same thing at the scale of a
  room. Vertically: a king's standing leave is a favour a courtier can hold.
- **R.** A promise kept, withdrawn, let lapse or broken by a crowded day, each with an author; hosts
  differ by whom they grant.
- **S.** One methodology for every promise with an end. *Zooms*: person to room.
- **E.** One table row, one branch in one effect, two reads.

## Cost class

Small build after proposal A and S2-B §1. Golden re-record where a host commits to an ask.
