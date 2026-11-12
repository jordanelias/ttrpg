# CHAR — pessimist audit (NERS, premise, emergent narrative) of the character model and the decision layer

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: d161a61 (working tree)

Scope: `engine/season/decision/`, `engine/season/queries/person_q.py`, goals, convictions, scars,
attributes, the cast, the chooser; the NPC and AI-chooser intent as established in `02_CHAR_audit.md` §0A
and `02_CHAR_audit_addendum_B.md`; and the six premise sentences of a person. Prior work cited, not redone:
`02_CHAR_audit.md` (F-CHAR-01..15), `02_CHAR_audit_addendum_B.md` (F-CHAR-16..22), the `02_CHAR_*`
proposals, `18_DETERMINISM_SWEEP.md`, `16_PESSIMIST_GAME.md`. No code under `engine/`, `modules/`,
`systems/`, `references/` or `tools/` differs between the first CHAR audit's read (601e715) and this one
(`git diff --stat`: empty), and this lane's season hashes reproduce theirs (`5ab73af2`, `bacd687f` at seed 0;
`8aae8412` at seed 1, season two), so the earlier figures are cited as current.

Everything measured here is new unless a lane is named. All runs: `PYTHONHASHSEED=0`,
`harness/populated.py::build_realm`, the shipped chooser over `resolvable_verbs()`, no player, no hand-built
act unless the row says PROXY. Scripts and outputs:
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_CHAR/`.

**IN PROGRESS: this head was written before the reading finished; sections are appended as they are
established. If this line is still present, the lane was interrupted and what follows is partial.**

## 0. Verdict

(pending the last runs; the premise section below is complete as far as it goes)

## 1. The six premise sentences — three accounts

### 1.1 Account one: the ordinary meaning (written BEFORE reading any note or code)

This table was the first thing written to this file, before `02_CHAR_audit.md` or any code was opened
(`skills/premise-check` STEP 2). It is what a player who knows strategy and RPG games would take each
sentence to mean.

| # | premise | what each link should do, in ordinary words |
|---|---|---|
| P1 | a man pursues what he wants and is stopped by what he believes | He has a want that is his own and that he can name. Given a free hand he takes the act that advances it. There is at least one act that would advance it and that he will not take because of a belief, and a man without that belief takes it. The stop has a cost he can be seen to pay (the want goes unserved), and under enough pressure the belief may give way, which is itself an event. |
| P2 | two men with different convictions choose differently in the same situation | Hold the situation fixed (same place, same options, same knowledge, same want); change only the conviction; the choices differ often enough to be noticed, in the direction the convictions' names predict (the merciful man spares, the lawful man reports). The difference is the conviction's and not the dice's: the same man re-drawn mostly chooses as himself. |
| P3 | a man changes over time because of what he does and what is done to him | What he does (kills, betrays, keeps faith, fails) and what is done to him (wounded, robbed, pardoned, bereaved) leave marks that persist, and the marks change later choices: he chooses differently after than before, in a direction the event explains. Change is not only decay; it is specific to the event. A man to whom nothing happened is unchanged. |
| P4 | a man is wrong about the world | He holds a belief about a fact (who did it, who holds the seat, how strong the garrison is, whether he is liked) that differs from the truth; he acts on the belief and not the truth; the act goes badly or strangely because of it; he can find out, and finding out changes what he does. Ignorance (not knowing) is the weaker cousin; the sentence asks for a false belief. |
| P5 | a man's reasons are readable afterwards | After the act, a record states why this man took this act rather than the other on offer: which want, which belief, which pressure, what he knew. A narrator can read it without re-running the chooser, and two different reasons produce two different records. |
| P6 | a skilled man usually beats an unskilled one | Skill is a property of the person. In any contest where it applies, the more skilled wins more than half the time, rising with the gap, never to certainty (the standing rule: no deterministic outcome); the same holds in a choice of what to attempt (the skilled man attempts what he is good at). |

### 1.2 Account two: what the code's notes say, in aggregate

Read from the docstrings of `decision/choose.py`, `decision/options.py`, `queries/person_q.py`, the roster
notes and the first audit's §0A (cited, not redone).

- **P1.** A want is a weighted vector over fifteen pursuits projected on seven axes (I-3), plus a standing
  `commit` to an OUGHT that raises a question each season (I-4). The stop is `ED-IN-0261`'s deontological
  gate: *"it's a refusal to take certain actions"*, *"the weighting is a threshold"* (`options.py:568-608`),
  and separately clause 4, a person does not form an act whose premise he believes false. The notes say the
  gate is *"armed nowhere"* (`rosters.yaml:540`).
- **P2.** *"A choice is a ranking by values and regard, sampled"* (I-6); `Person.conviction` is religious
  affiliation as a separate intensity (ED-IN-0251) that *"strongly modulates"* the `doctrine` pursuit
  (`person_q.py:804`).
- **P3.** *"What is right is moved by argument and consequence, never by evidence"* (I-8); the scar is a
  count per element accrued by witnessing, with thresholds 1 / 2 / 3 (`person_q.py:796-801`); the crisis at
  3 *"ROLLS NOTHING"* (`person_q.py:903`); practice raises a pool (`data/fixtures.py:467-479`).
- **P4.** A person decides on his own ledger and never on world truth (I-2); hearsay is graded when read
  (I-10); believed odds are his own (`sigma.py:363-365`).
- **P5.** The occasion rides the `Scene`; `Act.reads` exists as a field; `why` was cut from `Candidate`
  (first audit §0A).
- **P6.** *"Capability supplies dice and gates nothing"* (I-11); `pool_default` *"IS WHAT `capability` WOULD
  SUPPLY AND DOES NOT"* (`data/fixtures.py:434`).

### 1.3 Account three: the running code (verdict by execution)

Verdicts: **HOLDS**, **NARROWED** (holds in a sense the words do not promise, or in one direction only),
**FAILS**, **UNREACHED** (no instance occurs in computed play, so the premise has nothing to be true of).

| # | premise | verdict | the cheapest observation that decided it |
|---|---|---|---|
| P1a | a man pursues what he wants | **NARROWED** | 243 commitments are live after three seasons (148 at build) and **0 have ever ended** (seed 0); 11 of 749 resolved acts in a season answer the actor's own want (first audit). A want is a question he is asked each season; nothing counts toward it and nothing completes or abandons it |
| P1b | and is stopped by what he believes | **FAILS, both ways** | shipped (`refusal_axis: None`): no candidate is refused in 276 readings. Armed: all 46 cast refuse `transfer`, `move`, `forge`, `reconstruct`, `exchange` in 276 of 276 readings, so the stop is the realm's and not the man's (F-PES-CHAR-02) |
| P2 | two men with different convictions choose differently | **NARROWED** to pursuits, **FAILS** on the field named `conviction` and on the names | swap a man's whole religious affiliation: his top act moves in 6 to 15 of 276 readings (2 to 5%); redraw the same man: his top act moves in 61%. A man of `love` alone tops `forge` in 266 of 276 readings (F-PES-CHAR-01, -04) |
| P3 | a man changes because of what he does and what is done to him | **FAILS on cause, FAILS on direction** | the one change that fires (the conviction crisis) strikes the same six persons at seeds 0 and 1, by a rule with no draw, from witnessing strangers' paperwork, and moves an orthodox man to the rival creed at a higher intensity than he held his own (F-PES-CHAR-03) |
| P4 | a man is wrong about the world | **NARROWED** to stale granary counts | of 21,312 beliefs held after three seasons, 1,448 are about a present fact; 312 of those are wrong, and 296 of the 312 are the count of grain or salt in a store (F-PES-CHAR-06) |
| P5 | a man's reasons are readable afterwards | **FAILS** | `Act.reads` is empty on 2,367 of 2,367 resolved acts (seed 0, three seasons); the record carries the occasion and nothing of the ranking |
| P6 | a skilled man usually beats an unskilled one | **UNREACHED**, and **FAILS** where built by hand | all 46 cast roll a pool of 2 on all nine verbs that read a skill; at that pool an argument succeeds 7% of the time for everyone; an opponent's skill at argument does not enter the roll (F-PES-CHAR-05) |

The detail of each is in the findings (§4). Three results a player would be most surprised by, in the
genre's own terms: a man of honour fights and a man of love forges; a devout man who sees three forged
papers converts to his church's enemy; and nobody in the realm is better than anybody at anything.
