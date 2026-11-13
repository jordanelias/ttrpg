# CHAR — the goal's lean on its own question: an input to CR-88's design item (3)

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.2 row (CONFORMS), §7 (INCOMPLETE: no named test), §7b-17, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` ledger S-15; `unified/U3_CONFLICT_LEDGER.md` C3-D7, C3-N14; `unified/U3_DEPENDENCY_ORDER.md` node B10, §6.2). Added: named tests (the falsifier becomes one); "749 resolved acts" reads "749 folded acts (821 attempted)" (C3-N14); the scratch `probe3.py` reading is marked and restated by the gate's `decision_spread` reading; the landing order on the shared `score_terms` tuple (`aim` third, before `risk`; voices after both, C3-D7); lands-it and tier. No other change.

**Lands in batch:** B10, before `02_CHAR_what_an_act_risks.md` and `02_CHAR_voices_and_the_room.md` (C3-D7). **Depends on:** B09 (`02_CHAR_reason_trail_and_small_edits.md` Part A's `watch`); plan position CR-88's design item (3) `[PL]`.

## Status: PROPOSED

Written by the CHAR audit lane (`audits/02_CHAR_audit.md`, finding F-CHAR-01). Ratifies nothing.
Reference under `CLAUDE.md` §0.05. It is addressed to CR-88's DESIGN-FIRST step
(`workplans/valoria_master_workplan_v11_part4.md` CR-88, *"duty's positive half"*), which is the plan's
own home for a goal term in the score; it proposes how that term is scoped, and adds no position.

## What this changes in `engine/season/` at runtime

`decision/choose.py::score_terms` returns a third term, `aim`, which is 0.0 for every candidate at the
shipped `aim_gain` 0 (the control; hash EQUAL). At a non-zero gain, a candidate formed on a `need`
question raised by a goal the person is committed to is also scored by THAT GOAL's own pursuit lean.
A declared mover when the gain is flipped.

## The problem, with evidence

**A person's order of verbs is the same in every situation.** The pursuit term is
`Σ_axis axis_w[axis] · align(c.verb, axis)` (`decision/choose.py:215`): it reads the candidate's verb
and nothing else about it. Read on the built realm, cast only, the six common referents (the heads of
six factions), temperature 0 (scratch `probe3.py`, seed 0; not in the repository, its reading is restated by
the gate below): **36 of 46** persons have one score-top
verb across all six, the other ten have two; 23 of 46 hold one full verb order across all six. The
commonest top is `create_record`, for 25 to 28 of the 46 at every referent. What differs between
situations is only the stance term, which is zero-variance in 253 of 276 readings.

**A goal chooses the subject and then stops.** An ambition is a live `commit` to an OUGHT Proposition;
it raises the `need` question (`world_q.questions_for`, Q4) and orders attention (`attention_key`,
tiers 0 and 3). Nothing under `decision/` reads the goal once the question is formed. H-283 (register
line 5565): *"one commit and four give identical candidates and identical scores ... Ambitious is
therefore a kind of person, not a degree."* H-289 (line 5643): with the throne vacant the heir forms
`succeed` every season and executes it 0 times in 9 heir-seasons, because it scores near 0.022 against
a top candidate near 4.05. In one played season at seed 0 (`decision_spread --season`), the questions
raised by organization goals account for 5 of 749 folded acts (821 attempted; C3-N14).

**The plan's term would flatten officers toward their faction.** CR-88 item (3): *"while he holds the
office his score adds `goals.expected("faction", F)` at `fx.duty_weight`"*. `expected` is a pursuit
map, so the addition moves the officer's whole vector toward the template for every question he
answers. Two officers of one faction then rank every candidate more alike, on business that has
nothing to do with the office. That works against R-06 (characters differ) to buy R-04 (an office
binds), where the two need not trade.

## The resolution, decided

The goal's lean applies to the question the goal raised, and to no other.

- A `need` question carries its ambition on `Question.about` (`q:need:<prop id>`); the person holds the
  live `commit`; the goal's `pursuits:` are static data under `data/goals.py`, which `decision/` may
  import. So the term is person-side and World-free (AX-2).
- `aim(c) = aim_gain · damp · Σ_axis to_axes(goal.pursuits)[axis] · align(c.verb, axis) · odds_weight`
  when `q.source == "need"`, `goals.goal(q.about)` is a goal and `p` holds a live `commit` to it;
  0.0 otherwise. The same dot, the same owners (`data/pursuits.to_axes`, `data/verbs.align`), the same
  believed-odds factor: one methodology with the pursuit term.
- A person's own want (`prop_<cid>`) and a creed are not rows of `goals.yaml` and carry no `pursuits:`,
  so they read 0.0. That is a limit and is stated: the 46 own wants gain nothing here until a want
  carries a lean, which is authored content.

Ladder: step 3 answers WHETHER (CR-88, approved by ED-1094's merge default, puts a goal term in the
score); step 5 answers WHERE (a term scoped to its occasion has one owner and one reading; a term
applied everywhere is a second copy of the person's vector).

This does not make a person reason from ends to means. It makes him act as the goal would on the
goal's business and as himself otherwise. Means-ends valuation proper needs each verb's declared
`writes:` joined to a goal's aim predicate; the tree's carrier for that is `goal_stages` (CL-THRUST
B2.2, unauthored), and AM-B-09 narrowed aim states to rung goals. Neither is re-opened here.

## The exact edits, by owner

1. **`engine/season/decision/choose.py`** — `score_terms(p, c, fx, memo, odds, q=None)` returns
   `(pursuit, stance, aim)` (the shared tuple's third element; `02_CHAR_what_an_act_risks.md` appends `risk`
   after it, and `02_CHAR_voices_and_the_room.md` names all four, C3-D7); `make_ranker` passes the View's question; `make_chooser`'s `score` is the
   left-to-right sum of three. `deliberation_memo` hoists the goal's projected lean once per
   deliberation under a third tuple key (it does not depend on the candidate).
2. **`engine/season/harness/decision_spread.py`** — `TERMS = ("pursuit", "stance", "aim")`; the
   attribution loop is already written over `TERMS`.
3. **`engine/season/data/fixtures.py`** and **`hole_register.yaml`** — `aim_gain`, default 0, sweep
   `[0, 0.5, 1, 2]`, [ASSUMPTION; medium; Jordan to correct; revert: 0].
4. **CR-88's design file** — item (3) restated as this term, with `duty_weight` naming the same
   fixture if the design prefers its word.

## Gate (an execution artifact, §0.2)

- `aim_gain` 0: `build_realm(0)` one-season hash EQUAL.
- `aim_gain` 1, `decision_spread --season`, seeds 0–2: resolved acts answering an organization goal's
  question show a verb distribution that differs from the same persons' acts on `claim_landed`
  questions (today they are drawn from one fixed order). Reading rule, stated before the run: the
  share of persons with one score-top verb across a `need` question and a `claim_landed` question on
  the same referent falls below the 36-of-46 read above.
- `aperture 2 0`: no verb's `executed` count falls to 0 that was above 0 at the control.

## Falsifier

Two hand-built persons with identical pursuits, committed to two goals whose `pursuits:` point opposite
ways on one axis, handed each goal's `need` question on one referent: they rank one exposed verb
differently at `aim_gain` 1 and identically at 0. The same two handed one `claim_landed` question rank
alike at every gain.

**Named tests** (new, `engine/season/tests/test_goal_lean.py`): `test_aim_is_zero_at_gain_zero` (with the
`build_realm(0)` one-season hash EQUAL);
`test_two_goals_with_opposite_leans_rank_one_verb_differently_on_their_own_question`;
`test_a_claim_landed_question_ranks_alike_at_every_gain`.

## NERS reading (§0.06)

- **N.** Top-down, an authored goal that changes nothing a member does once he attends to it is
  decoration; bottom-up, the verb order that never moves is the reason the realm's commonest act is
  the same in every situation; laterally, CR-88 needs the term and this is its narrowest form.
- **R.** Strategic: a player who learns a councillor's office can predict how he acts on its business
  and how he acts off it. Variety: the same person shows two faces. The no-player half: officers
  pursue their organizations' ends between sessions.
- **S.** One dot product, three weightings of it. It pauses correctly: off the goal's question it is
  exactly zero.
- **E (last, as a ratio).** One term, one fixture, no carrier, no roster. The plan's alternative is
  the same size and loses the distinction between the office and the man.

## Cost class

Small build, after or inside CR-88's design (B10-17b). Shared files: `decision/choose.py`,
`harness/decision_spread.py`, `data/fixtures.py`, `hole_register.yaml`.

**Lands it and tier.** The B10 batch, an IN `valoria-author` session on `sonnet` (`high`), closed by B10's
`methodology-close` once. **Hash movers.** None at `aim_gain` 0 (control); declared when the gain flips.
