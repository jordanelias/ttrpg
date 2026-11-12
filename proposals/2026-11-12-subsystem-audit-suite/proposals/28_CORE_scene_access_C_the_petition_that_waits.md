# 28 · CORE · SCENE ACCESS · C — the petition that cannot get through: what waiting does, read from what happened

## Status: PROPOSED (a plan for future execution; nothing here is executed by the authoring lane)

Carries `audits/28_SCENE_ACCESS.md` §5 and §6. Serves Jordan's A-64 (3): *"someone is trying to petition but
can't get through to person meanwhile the petition content intensifies"* (`unified/DECISIONS_ANSWERED.md`;
its marked assumption: *computed when read where it can be; any change in the petition's force is a drawn
graded result, not a fixed step*). Completes the clause `20_NARRATIVE_B_what_he_was_owed.md` edit 5 left
owed (*"Petitions … Then `dues_unmet` gains a second clause"*). Needs proposal A for the Event
`visitor.kept_waiting`. Reference only (CLAUDE.md §0.05). Not ratified by being written.

## What it changes in `engine/season/` at runtime (first)

With the three new fixtures at their controls (`waiting_valence 0`, `waiting_level None`,
`rebuff_kinds` unread): nothing. Built:

1. `person_q.regard(p, x, fx)` gains a term for how often `p` remembers being kept waiting at `x`'s door,
   and `person_q.dues_unmet` gains the papers and promises that lapsed there.
2. A new leverage source, `waiting`, adds levels to the petitioner's side of the draws that decide
   whether his paper enters a room and how it is heard, one per rebuff the log records.
3. Two reads, `world_q.rebuffs` and `world_q.petition_state`, answer what a paper has been through and
   what the thing it complains of is **now**; the chronicle and the play surface print them.

No field is added to `Record`, `Person` or `World`; no Record is rewritten; nothing is advanced by a
step at any barrier. A declared hash mover only where a fixture leaves its control in a world that holds
a rebuff.

## The problem (evidence)

- A petition is a `Record` of kind `petition` with content `{terms, to, from}`
  (`loop/effects_information.py:707-725`), written once (`state/carriers.py`, `Record.__post_init__`:
  *"written once, inside `(Record, exists)`'s gate"*). Its terms are a Proposition, which is immutable
  (`04` PART D row 30b). So a petition's content cannot be stepped upward in place by any lawful write.
- What the log already records of a paper being put off: `carry.refused` (13 in two seasons at seed 0),
  `matter.lapsed` (`loop/matter.py:442-456`, CR-55's docket lapse), `speech.unheard` (23), and, proposed by
  other lanes, `document.held` and `document.returned` (`15_INSTITUTIONS_BYZANTINE_C_the_hands_of_the_chain.md`).
  Proposal A adds `visitor.kept_waiting`. Nothing reads any of them as a history of one grievance.
- 20 petitions filed, 4 carried, 0 determined in two seasons at seed 0 (`occ_s0_k2.txt`; the petition
  path's kinds). `20_NARRATIVE_B_what_he_was_owed.md` reads 35 / 44 / 44 filed and 0 / 2 / 0 determined over
  four seasons at three seeds. Petitions already do not get through; nobody is the worse or the angrier
  for it.
- Jordan's ruling on what a clock is (`registers/editorial_ledger_in.jsonl`, ED-IN-0345, verbatim):
  *"they trigger behaviours based upon an accumulation of game world events"*; the row adds that such a
  thing *"is not a timer"* and that a threshold conditions a person's choice *"rather than an act being
  imposed"*. And no Event carries a round (`loop/driver.py:557-561`), and a person may not know which
  round it is (`loop/deliberate.py::_qualify_by_round`'s docstring). So "elapsed rounds waiting" is not a
  quantity any lawful reader holds.

## The resolution, decided

**Waiting is read as what happened to the man and his paper, not as time passed; what it changes is
odds and inclination; what then happens is his sampled choice and that act's draw.** Ladder: step 1
(A-64; ED-IN-0345 for what may be counted); step 4 (`dues_unmet`, `custody`'s leverage shape,
`forgive`'s grievance term are the precedents); step 3 for D-48 (a level is computed when read).

A-64's assumption says *a read of elapsed rounds waiting*. This file reads **rebuffs** instead: the
Events in which he or his paper was put off. That count rises with every round he spends at a closed
door, is in the log with its causes, and is the reading ED-IN-0345 permits. Where the two would differ
(a man who files and then does nothing), nothing intensifies but the need itself (§3), which is the
honest reading: he was not kept waiting, he stopped asking.

### 1. The grievance: computed when read, from his own memory

`queries/person_q.py`, beside `held_against` (own ledger only, AX-2; nothing stored):

```python
def kept_waiting(p: Person, x: str) -> float:
    """HOW MUCH `p` REMEMBERS BEING KEPT WAITING AT `x`'S DOOR: the summed present confidence, over
    `confidence_default`, of his own firsthand claims of kind `visitor.kept_waiting` whose subject is
    `x` and whose doer is himself. It fades as those memories fade (the present-confidence read
    `01_CORE_claim_fade_as_read.md` proposes; until it lands, the stored confidence MATTER decays) and is
    0 when he holds none."""
```

`person_q.regard` (`:424-453`), after the dues term NARRATIVE_B adds:
`stored -= float(fx.get("waiting_valence")) * kept_waiting(p, referent)`.

`person_q.dues_unmet(p, x)` (NARRATIVE_B edit 1) gains the owed second clause, each origin once
(ED-IN-0322): a petition of his own addressed to `x` of which he holds a claim that it lapsed or was
returned; and a promise of `x`'s to receive him of which he holds a claim that it ended at its term while
he also holds a `visitor.kept_waiting` claim from inside its span (proposal B's `turned_away`, read
person-side from his own claims). CR-88's `grievance_against`, when its design file is drafted, counts
the same origins: one function, the same callers.

This decides nothing. It moves how he ranks acts toward one person (§4).

### 2. The force of the paper: a leverage source, so the change is always a draw

`rosters.yaml: advantage_sources` (`U5c_SC_one_obstacle_form.md` §3) gains `waiting`, placed after
`custody`, whose shape it copies (*one level per season the prisoner has been held, capped by the soft
cap*):

| source | aggressor levels | defender levels | fixture |
|---|---|---|---|
| `waiting` | one `waiting_level` per rebuff the log records of the petition the act carries or speaks to (`world_q.rebuffs`), netted and capped by the one soft cap | — | `waiting_level` (first value `minor`; control `None`) |

It applies where the act's subject is a petition Record or a docket item that names one: `carry`
(`14_VERBS_SOCIAL1_D_grievance_and_settlement.md` §1), a clerk's entering `carry`
(`15_INSTITUTIONS_BYZANTINE_C_the_hands_of_the_chain.md`), `speak` on the item, and the petitioner's
side of the hearing's closing draw (`05_SC_playable_hearing_B.md`). A paper turned away three times is
likelier to be let in and likelier to be heard hard, and is still sometimes turned away a fourth time.
No band is ever certain and no rebuff adds a fixed amount to any state.

```python
def rebuffs(w, rid: str) -> int:
    """THE EVENTS IN WHICH THE PETITION `rid`, OR ITS HOLDER AT ITS ADDRESSEE'S DOOR, WAS PUT OFF since
    the Record's creating Event (`_creating_act`'s scan): kinds in `rosters.yaml: rebuff_kinds`, whose
    subject is `rid`, its docket item, or (for `visitor.kept_waiting`) its addressee with the petition's
    holder as the causing act's actor. Read off the log; stored nowhere."""
```

`rosters.yaml: rebuff_kinds` ships with the kinds the verb table and the write matrix derive at build
(`visitor.kept_waiting`, `carry.refused`, `matter.lapsed`); `document.held` and `document.returned` are
added in the commit that lands their rows. The loader refuses a kind the derived roster does not hold.

### 3. The content: what the paper said, and what is true now

A petition is not edited. What intensifies is the thing it is about, and a reader is shown both:

```python
def petition_state(w, rid: str) -> dict:
    """{filed: the creating Event's tick, stage: the newest stage label, rebuffs: `rebuffs(w, rid)`,
    then: the terms Proposition's value, now: `WorldReader.read(terms.subject, terms.predicate)` where the
    predicate is a stem the world answers (else None)}. A read; nothing is written."""
```

`then` against `now` is the growth of the demand: a petition filed on a shortfall of three, read when
the shortfall is nine, shows both numbers. **The demand of his next paper is today's**, because a
person utters what he holds (`14_VERBS_SOCIAL2_B_a_word_with_content.md` §1) and what he holds now is
the larger want; so a second petition asks more, and at a hearing it stands against a higher `stakes`
term (`U5c_SC_one_obstacle_form.md` §2 member 5) with more `waiting` levels behind it. Whether a lapsed
matter may be carried again at all is `U5c_SC_proceedings_residue.md` §4 item 5's conjunct (`fresh`:
new grounds); a worsened need gives him a newer claim to cite, and whether that suffices is that lane's
rule, not decided here.

### 4. What he does next: the chooser's read, and a table of ways out

No rule here picks an act. `decision/choose.py::score_terms` is unchanged in form; the inputs that move:

| he | reads (all person-side) | which raises |
|---|---|---|
| seeks the person at all | a `need` question or a claim landed about the matter; whom he believes holds the seat (`14_VERBS_SOCIAL2_B…` §3; `08_FI_01_claim-sourced-referents.md`) | a visit where he believes the man is (`14_VERBS_SOCIAL1_A_formation.md`); a paper where he does not |
| waits and calls again | `admission_weight` on a remembered refusal (`16_PESSIMIST_CORE_a_refusal_is_remembered.md`) | less of the same call each time, more of everything else |
| books | he holds `visitor.kept_waiting` of that host | the ask (proposal B §1) |
| goes through someone | his regard and ties toward people he believes can reach the host; a clerk's body named on the seat | `tell` or `give` to them; the tender to the clerk |
| goes over his head | lower regard for the host (the two terms of §1); a seat above he knows of | `petition` to that holder |
| turns to other means | the same lower regard and, through CR-88, a grievance that can clear the dispute band | `challenge` (its `dispute` conjunct), a released oath, `evade / defy`, `migrate`; for a cohort the heavy moves of `U5d_SE_cohort_heavy_moves_and_caste.md` (refuse, riot); the rare attempt of A-16 behind its own gate |
| gives up | the claims fade (D-48, computed at the read) or the need is met; or his own drawn `forgive` (`14_VERBS_SOCIAL1_D…` §2: Failure is *could not let it go*) | nothing: the matter leaves his questions |

Two people with the same rebuffs differ by their pursuits, their conviction and their regard, as for any
choice, and the sampler (`choose.py::_sample_order`) means the patient man sometimes snaps and the hot
one sometimes waits.

### 5. Who sees it, so the story can be told

| reader | sees | by |
|---|---|---|
| the person petitioned | that this man was kept waiting at his door, each time | the `visitor.kept_waiting` Event names him as its subject and he is present; the ask and the petition name him |
| those present | the same, with the visitor as doer | the ordinary witness deposit; it travels by `tell`, and a lord who keeps petitioners waiting acquires that reputation through `reception` |
| the bench or clerk who finally reads the paper | `then`, `now`, and the levels standing for the petitioner | the roll's named terms (`U5c_SC_one_obstacle_form.md`'s reason line) |
| the chronicle and the player's surface | one line per petition from `petition_state`; and a story class, *kept waiting, then …* | `harness/chronicle.py`: a `visitor.kept_waiting` or lapse Event in the cause chain of a later act by the same person toward the same holder or a seat above |

## Exact edits, by owner (in landing order)

1. **`engine/season/rosters.yaml`** — `rebuff_kinds` (closed, validated against the derived Event
   kinds); `advantage_sources` gains `waiting`.
2. **`engine/season/queries/world_q.py`** — `rebuffs`, `petition_state`, beside `issuing_seat` (whose
   creating-Event scan they share).
3. **`engine/season/queries/person_q.py`** — `kept_waiting`; the `regard` term; `dues_unmet`'s second
   clause (in the commit that lands NARRATIVE_B's first, or after it).
4. **The leverage composer** (`U5c_SC_one_obstacle_form.md` §3's one function) — the `waiting` source.
5. **`engine/season/harness/chronicle.py`** — the petition line and the story class.
6. **`engine/season/data/fixtures.py`** — `waiting_valence` (control `0.0`; swept `0 / 0.5 / 1`; first
   value `0.5`: a quarter of NARRATIVE_B's moderate `dues_valence 2`, since being kept waiting once is a
   slight and a lapsed oath a wrong `[ASSUMPTION; medium; Jordan to correct; revert: 0.0]`);
   `waiting_level`; register rows at build.

## Gate (execution artifacts, §0.2)

| # | reading | passes when |
|---|---|---|
| 1 | every fixture at its control | hash equal at every seed |
| 2 | planted: a petition on a rung's stores; the stores are lowered by an act between filing and reading | `petition_state` returns `now != then`; the Record's encoding is byte-identical before and after |
| 3 | planted: one petition heard after 0 rebuffs and after 3, 400 seeds each | the band distribution shifts toward the petitioner; no band has probability 0 or 1 in either arm |
| 4 | realm, seeds 0 to 4, six seasons, proposals A and B on | persons with `kept_waiting > 0` above zero at three seeds; executed acts by them toward that holder or a seat above, in the two seasons after, differ by verb from the control arm by more than the control's seed-to-seed spread (NARRATIVE_B gate 4's form) |
| 5 | fade | with no new rebuff, a person's `kept_waiting` falls season on season and reaches 0 with no write to him |
| 6 | chronicle | at least one *kept waiting, then …* chain at two seeds; none in the control |

## Falsifier

`now` equal to `then` after the world moved (the content was stored, not read). A band at certainty in
gate 3. A regard that fell where the log holds no rebuff (moved by time alone, against ED-IN-0345). A
person-side reader that names `World`. Gate 4 with no verb moved: the grievance has nothing to ride,
which is a finding about the closing verbs, as NARRATIVE_B's own falsifier says.

## Layer 1 rows

AX-2 (a person reads his own ledger): `kept_waiting` and `dues_unmet` conform. S19.3 (an Event carries no
actor and no target; attribution is per witness): the kept-waiting claim's doer is read by the holder,
not stored on the Event. `04` §B.2 as `U5c_SC_one_obstacle_form.md` §2 applies it (no reader of another
person's ledger at RESOLVE): `rebuffs` reads the log. PART D row 17 and `holonic` §25.1 (three licensed clocks): no fourth; nothing here ticks. Row 30b:
relied on (the petition is never rewritten). Row 39 (eviction ranks on confidence and recency only):
untouched. `holonic` §26.3 (petitions uncapped; *"a matter closes at RESOLVE by scarcity and at CALENDAR
by lapse"*): conform, and the section's own sentence is this proposal's premise: *"A King facing four
simultaneous pressures who can substantively address two, with the other two compounding"*.

## NERS reading (E last)

- **N.** Cut it and a petition ignored for a year is the petition it was on the day it was filed, and
  the man who filed it feels nothing. Top-down: the ruling. Bottom-up: the Events exist and are unread.
  Laterally: an oath left to lapse already makes a grievance (NARRATIVE_B); a prisoner's time already
  makes leverage (`custody`). Diagonally: a village's petition (a cohort's heavy move) and a baron's
  ride the same count. Horizontally: the same read serves the bench, the chooser and the chronicle.
- **R.** The no-player half is the point: neglected petitioners go over heads, leave, refuse, riot or
  give up, each for reasons the log holds. Strategy for a ruler: whom to hear before their case hardens.
  Completeness: the man who stops asking is stated (the resolution's second paragraph); the fade is
  gate 5.
- **S.** *Calculations consistent in methodology*: one grievance function, one leverage form; no second
  ladder for "urgency".
- **E.** Three reads, one roster, one leverage row, two regard terms.

## Cost class

Small build, after proposal A; the regard terms after NARRATIVE_B's first commit; the leverage source
after U5c's composer. Golden re-record where a fixture leaves its control.
