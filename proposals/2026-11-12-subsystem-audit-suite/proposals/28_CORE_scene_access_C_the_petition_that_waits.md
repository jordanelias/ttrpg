# 28 · CORE · SCENE ACCESS · C — the petition that cannot get through: what waiting does, read from what happened

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.7 row 28C (CONFORMS except `petition_state.now`; the regard unit; the inherited lapse write), §7, §7b-14, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` §3 *regard*, ledger R-24, S-11; `unified/U1_GLOSSARY.md` *occupy* → *engaged*, *level*; `unified/U3_CONFLICT_LEDGER.md` C3-D8, C3-K7; `unified/U3_DEPENDENCY_ORDER.md` node B38). Layer 1 rewrite (`04` §C.11 / AX-2: the engine owes a person the arithmetic of what he holds and nothing else): `petition_state`'s `now` (the world's present value) is for the chronicle and the harness only; the person-facing form is `person_q.petition_state_held(p: PersonInterior, rid)`, whose `now` is the reader's own held claim (the player's surface and a bench read their own). The `regard` addend is in the stance row's unit (U1 §3: `waiting_valence` is a valence in that unit; one fully remembered rebuff is `waiting_valence` stance steps), so `regard` keeps one unit. The inherited clause "as the lapse already appends `lapsed`" follows `U5c_SC_proceedings_residue.md` §4 item 6 as rewritten (the lapse is read from its `matter.lapsed` Event; MATTER appends no stage). A visit **engages** its counterparty (glossary). Order: after `20_NARRATIVE_B` in B38 (C3-D8); `harness/storybar.py` edited after `23_STORY_D` and before `30_WR_B` (C3-K7). Named test added for the person-facing read; the rest stands.

**Lands in batch:** B38. **Depends on:** `28_CORE_scene_access_A_…` and `_B_…` (B28), `20_NARRATIVE_B_what_he_was_owed.md` and `20_NARRATIVE_C_who_holds_what.md` (B38, first), `23_STORY_D_story_census_and_gate.md` (B36), `U5c_SC_one_obstacle_form.md` (B05), `14_VERBS_SOCIAL1_D_grievance_and_settlement.md` (B28).

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
`stored -= float(fx.get("waiting_valence")) * kept_waiting(p, referent)`, in the stance row's unit
(`Σ valence × weight`, U1 §3): `kept_waiting` counts fully remembered rebuffs, so one is worth
`waiting_valence` stance steps, and the sum is bounded by `stance_term`'s ±`STANCE_MAX` clamp
(`02_CHAR_scar_cap_and_regard_unit.md` item 3). At `regard_unit: stance` this is the same unit as the judged
and told halves; no second unit for regard.

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
# queries/world_q.py  (resolver-side: the chronicle and the harness only)
def petition_state(w, rid: str) -> dict:
    """{filed: the creating Event's tick, stage: the newest stage label, rebuffs: `rebuffs(w, rid)`,
    then: the terms Proposition's value, now: `WorldReader.read(terms.subject, terms.predicate)` where the
    predicate is a stem the world answers (else None)}. A read; nothing is written. Never handed to a
    person-side reader: `now` is world truth."""

# queries/person_q.py  (person-side; no World)
def petition_state_held(p: PersonInterior, rid: str) -> dict:
    """The same keys as `petition_state`, with `now` read from `p`'s own ledger claim about the terms'
    subject and predicate (newest, then most confident; else None), and `rebuffs` the rebuffs `p` himself
    holds claims of. What the player's surface shows and what a bench member weighs."""
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
| the person petitioned | that this man was kept waiting at his door, each time | the claim deposited from `visitor.kept_waiting` is about him and he is present (proposal A edit 3); the ask and the petition name him |
| those present | the same, with the visitor as doer | the ordinary witness deposit; it travels by `tell`, and a lord who keeps petitioners waiting acquires that reputation through `reception` |
| the bench or clerk who finally reads the paper | `then`, his own `now` (`petition_state_held`), and the levels standing for the petitioner | the roll's named terms (`U5c_SC_one_obstacle_form.md`'s reason line) |
| the player's surface | one line per petition from `petition_state_held` (what his character holds) | `04` §C.11 |
| the chronicle | one line per petition from `petition_state` (the true `now`); and a story class, *kept waiting, then …* | `harness/chronicle.py`: a `visitor.kept_waiting` or lapse Event in the cause chain of a later act by the same person toward the same holder or a seat above |

## Exact edits, by owner (in landing order)

1. **`engine/season/rosters.yaml`** — `rebuff_kinds` (closed, validated against the derived Event
   kinds); `advantage_sources` gains `waiting`.
2. **`engine/season/queries/world_q.py`** — `rebuffs`, `petition_state` (chronicle and harness only),
   beside `issuing_seat` (whose creating-Event scan they share); **`queries/person_q.py`** —
   `petition_state_held` (the person-facing read).
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

`now` equal to `then` after the world moved (the content was stored, not read). A person-facing `now` that
equals the world's value where the reader holds no claim of it (world truth shown). A band at certainty in
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

## Entrenchment moves the world (A-80): what a closed door produces

A person who cannot be reached is a held position. It must be a source of motion. Three parties move:

| party | what the closed door gives him to do (each an existing act, each drawn) | what it leaves in the world |
|---|---|---|
| the one kept out | call again; ask for leave; send another; the clerk's hand; the room; over the head; **forge** a writ in the name of a seat above (`forge`, `record.forged`; found out by `examine` or at a hearing); **force**: `capture` and an accepted `challenge` are never kept waiting (proposal A §1), a cohort's refusal and riot, A-16's rare attempt; leave (`migrate`, a released oath); let it go (`forgive`) | claims of each rebuff; a lower regard; a second paper with a larger ask; a forged instrument; a body, a custody or a death; an oath ended; a household gone |
| the one who holds the door | grant leave to some and not others (proposal B); withdraw it; go where callers are not (`move`: the caller's `with` then fails and the D-46 belief of absence forms); stand behind sworn men (`world_q.guard_weight`, the `audience` stem); answer through a clerk or only in the room | a `commit` with a term; a witnessed break; a reputation in `reception` for keeping petitioners waiting; a backlog |
| third parties | the intermediary and the clerk are sought, paid and resented (`15_INSTITUTIONS_BYZANTINE_C…`: a `give` to the clerk moves his regard for the giver); the seat above receives the papers that went over a head, so its holder comes to hold claims about his officer; what he does with them is his own choice among acts he already has (`revoke`; A-35's strip by a resistible draw). No rule here makes him act | favours owed; a superior who has been told |

**Four census shapes** (rows for `harness/storybar.py::SHAPES`, `23_STORY_D_story_census_and_gate.md`
edit 1; opening, turn, close; window in seasons). The opening of each is a rebuff:
`visitor.kept_waiting`, `carry.refused` or `matter.lapsed`.

| id | name | turn | close | window |
|---|---|---|---|---|
| `S-28a` | kept out, got in by another hand | `record.given` or `news.told`, role `same` | `petition.carried`, `matter.advanced`, `matter.carried` or `matter.determined`, role `other` | 4 |
| `S-28b` | kept out, went over his head | `petition.filed`, role `same` | `petition.carried`, `matter.determined` or `dispensation.issued`, role `other` | 4 |
| `S-28c` | kept out, turned to other means | `challenge.issued`, `record.forged`, `capture.declared`, `compliance.withheld`, `commitment.ended` or `residence.changed`, role `same` | `person.captured`, `body.changed`, `person.died`, `tenure.closed` or `residence.changed`, role `any` | 4 |
| `S-28d` | kept out, then given leave | `commitment.made`, role `other` | `news.told`, `argument.won`, `argument.lost` or `record.given`, role `same` | 3 |

A shape whose kinds no row emits yet prints `n/a (no emitter)` by the census's own rule.

**The entrenched-world arm** is gate row 7 below and proposal A's gate row 12: with the door as hard as
the fixtures make it, the four shapes still occur at a stated rate.

## No scene is still (A-81)

| outcome | the durable change it leaves | who can read it afterwards |
|---|---|---|
| a call refused at `engaged` | the kept-waiting claims in the caller's and the host's ledgers (proposal A) | `kept_waiting`; the host's questions; `rebuffs` |
| a paper declined by the room or returned by a clerk | today the deposits of `carry.refused` only. **Added here:** the declining act appends a stage to the petition Record, `(tick, "declined", act id)`, under its own act (an ACTS write at RESOLVE, `(Record, stages)` being `RES`/`ACTS`); the lapse, by contrast, is read from its `matter.lapsed` Event (`world_q.lapsed_at`, `U5c_SC_proceedings_residue.md` §4 item 6 as rewritten: MATTER appends no stage). The paper carries its own history to whoever next holds it | any holder of the Record (the content deposit); `petition_state_held`; a bench reading the file |
| a matter lapsed on the docket | MATTER's write taking the item off, and its `matter.lapsed` Event (read by `world_q.lapsed_at`) | as above |
| the man who waits and does nothing | no scene was spent, so no scene is still; his claims fade by the read | — |

The no-null-scene reading for this file: of the scenes in a run that hold a `carry` or an engaging act,
the count with no gate write and no `claim.deposited` citing them. Expected 0. Control: the planted
decline of commit 4 with its stage write removed, where the count is 1.

## Instructions to code it (a batch item for workplan v12)

**Lands by:** the IN lane for commits 1, 2, 5, 6; the SC lane's verb batch for commits 3 and 4 (they
edit rows that lane owns). `valoria-author` at `sonnet`; one `methodology-close` with its terminal `opus`
critique per batch. **Cost class:** small build.

| # | files and symbols (single owner) | call sites changed | data rows | named tests (`engine/season/tests/test_scene_access_waiting.py`) |
|---|---|---|---|---|
| 1 | `data/rosters.py`: `REBUFF_KINDS` (validated against `data/verbs.py::EVENT_KINDS`); `queries/world_q.py`: `rebuffs`, `petition_state` beside `issuing_seat` (`:1573`), sharing `_creating_act` (`:1590`); `queries/person_q.py`: `petition_state_held` | none | `rosters.yaml`: `rebuff_kinds: [visitor.kept_waiting, carry.refused, matter.lapsed]` | `test_rebuffs_counts_what_the_log_holds_and_nothing_else`; `test_petition_state_reads_now_without_writing_the_record` (gate row 2: the Record's encoding byte-identical); `test_petition_state_held_reads_now_from_the_readers_own_ledger` (a reader holding no claim of the lowered stores reads the old `now` or `None`) |
| 2 | `queries/person_q.py`: `kept_waiting` beside `held_against` (`:85`); `regard` (`:424`): the `waiting_valence` term; `data/fixtures.py`: `waiting_valence = 0.0` | none (`regard`'s callers are unchanged) | — | `test_kept_waiting_reads_own_ledger_only` (the `decision/` World scan stays green); `test_regard_is_unchanged_at_valence_zero` (hash EQUAL); `test_kept_waiting_fades_to_zero_with_no_write` (gate row 5) |
| 3 | `queries/person_q.py::dues_unmet`: the second clause | `regard`, and CR-88's `grievance_against` when it exists | — | `test_a_lapsed_paper_and_a_promise_broken_by_a_crowded_day_are_each_one_origin` |
| 4 | the leverage composer of `U5c_SC_one_obstacle_form.md` §3: the source `waiting`; `loop/effects_information.py::_eff_carry`: at the declining band, append `(tick, "declined", a.id)` to the Record's stages | the composer's callers for `carry`, `speak` and the hearing's closing draw | `rosters.yaml: advantage_sources` gains `waiting` after `custody`; `verb_table.yaml` `carry`: the declining band's `writes:` gains `Record.stages`; `data/fixtures.py`: `waiting_level` (shipped `None`) | `test_three_rebuffs_shift_the_bands_and_fix_none` (gate row 3, 400 seeds per arm); `test_a_declined_paper_carries_a_stage` (the no-null reading; mutation arm: the write removed, the count is 1) |
| 5 | `harness/storybar.py::SHAPES`: `S-28a` to `S-28d`; `harness/chronicle.py`: the petition line; `harness/access.py`: `kept_waiting` and rebuff counts, `--null-scenes` | none | the four rows above | `test_each_closed_door_shape_matches_a_planted_chain_and_not_its_shuffle` (the census's own null arm) |
| 6 | the measurement (gate rows 4, 6, 7) and the flips of `waiting_valence` to `0.5` and `waiting_level` to `minor`; one declared re-pin | the goldens' one owner | — | the re-pin |

**Gate row 7 (added; the entrenched-world arm, A-80).** Realm, seeds 0 to 4, six seasons, proposal A's
arm of row 12 (`engagement: seat_and_debit`, the strongest `precedence_level`, `appointments: off`): the
census reads `S-28a` + `S-28b` + `S-28c` at a summed rate of at least one instance per two seasons at
four seeds of five; `S-28d` reads 0 (no leave can be given in this arm), which is the control that the
arm is in fact entrenched. `[ASSUMPTION; medium; Jordan to correct: the rate is a seed]`.

**Gate row 8 (added; A-81).** `python -m engine.season.harness.access SEED 4 --null-scenes` at seeds 0
to 4: 0 scenes holding a `carry` or an engaging act with no durable change.

**Control and falsifier:** every fixture at its control (hash EQUAL); the falsifiers above, plus: the
entrenched arm reading no more *kept out* stories than the `engagement: off` arm reads (the door made
nothing move); a still scene in gate row 8.

**Declared hash movers:** `waiting_valence` and `waiting_level` off their controls where the log holds a
rebuff; commit 4's stage write wherever a paper is declined (it lands with S1-D's drawn `carry`, which
is itself a declared mover).

**INCOMPLETE, with what is missing.**

- *Commit 3* rests on `dues_unmet`, which `20_NARRATIVE_B_what_he_was_owed.md` edit 1 proposes and no
  code holds, and on a person-side reader of whom he believes held a seat
  (`20_NARRATIVE_C_who_holds_what.md`). Missing: both.
- *Commit 4's leverage half* rests on the one composer `U5c_SC_one_obstacle_form.md` §3 proposes; today
  the social wrapper passes `leverage=0.0` (`seam/wrappers/sigma.py:147`, as that lane's audit reads it;
  not re-opened here). Missing: the composer. *Its stage half* rests on `carry` having a declining band
  (`14_VERBS_SOCIAL1_D…` §1); today `carry.refused` is a precondition refusal and no effect runs.
- *`S-28c`'s force and forgery turns* count an act by the kept-out person after his rebuff; whether the
  cause graph links them (the later act's scene occasion walking back to the kept-waiting claim) depends
  on that claim raising his question. Missing: the first census reading.
- *`now` in `petition_state`* is `None` for a petition whose terms' predicate is not a stem the world
  answers; in computed play today a petition's `to` equals its `subject`
  (`14_VERBS_SOCIAL2_B…` evidence) and its terms name no quantity. Missing: S2-B §3 and
  `U5c_SC_proceedings_residue.md` §8 (terms as a Proposition).

## Cost class

Small build, after proposal A; the regard terms after NARRATIVE_B's first commit; the leverage source
after U5c's composer. Golden re-record where a fixture leaves its control.
