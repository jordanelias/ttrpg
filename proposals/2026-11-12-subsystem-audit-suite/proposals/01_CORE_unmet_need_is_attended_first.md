# CORE — within his own purview, a person attends to an unmet need before routine news

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.1 row (CONFORMS, with the read lane's assumption), §7 (INCOMPLETE: no named test, no hash values), §7b-17, §7b-T; `unified/U3_DEPENDENCY_ORDER.md` node B10). Completed: a named test; the standing-rule reading stated at the site (the tier-1 order is an attention order that admits a question, and the act is still drawn by the chooser's sampler, A-9; it decides no consequential outcome) `[ASSUMPTION: an attention order is bookkeeping — basis: R2 §1.1]`; the hash re-records are named as readings the batch takes on its base; lands-it and tier. No other change.

**Lands in batch:** B10, with and before `02_CHAR_goal_lean_on_its_own_question.md` (gate 2 reads both). **Depends on:** B09.

## Status: PROPOSED

Source: `audits/01_CORE_audit_addendum_B.md` F-CORE-20. Read at `785bc62`.

## What it changes in `engine/season/` at runtime

A declared hash mover. Among the questions a person holds at attention tier 1 (a referent he holds or
that lies in his seat's purview), one whose claim records an unmet need is answered before the others,
the larger shortfall first. Today the order inside tier 1 is the question id. Nothing else moves: no
tier boundary, no verb, no score.

## The problem, with evidence

`harness/scarce.py` is the world built to show a need propagate and be relieved: a town that runs dry,
a steward who holds it and stands in a full granary. Its docstring records that the chain executes when
the harness names the steward's question, and that under the shipped rule *"none of those deliberations
is about a shortfall claim, because claims about his own granary sort first"* (measured at `19d`,
before the attention key existed).

Re-run at this tree (`python -m engine.season.harness.scarce`, seed 0, four seasons, `scarce.txt`):

| arm | relief reaching the hungry town over four seasons | the granary after four seasons |
|---|---|---|
| question named by the harness | one transfer: 8 salt at tick 1 (the smaller of two shortfalls); the 15-grain shortfall is never answered | grain 216, salt 139 |
| unassisted (the shipped loop) | **none**. The steward's only transfers are six of 1 grain from the granary to the granary, all refused | grain 216, salt 147 |

The town demands 20 grain and 10 salt every season and is delivered 0 and 0 from the second season on,
beside a granary that doubles. The causal edge exists (the shortfall is recorded, deposited to the
steward as a claim and raises a question); the response does not.

**Where it stops.** `queries/world_q.py::attention_key` places both the hungry town (he holds it) and
his own granary (he stands in it) at tier 1 and says of that tier: *"magnitudes inside tier 1 are not
ranked (LIMIT)"*; the tiebreak is the question id. Routine `stores.changed` claims about the granary
land every round.

**Two experiments, each against its same-seed control** (in-process patches, no repository change):

| experiment | seed 0 | seed 1 | seed 2 |
|---|---|---|---|
| answer the first question not yet answered this season, instead of the first (`probe_unanswered_first.txt`) | hash unchanged; positions answered 0 ×37, 1 ×2 | — | — |
| inside tier 1, a shortfall claim first, larger first (`probe_shortfall_salience.txt`) | hash moves; refused self-transfers 6 → 0; no relief | hash moves; no relief | hash moves; **relief**: 1 grain at tick 0, 15 grain at tick 1 (claim-sourced) |

The first experiment is a null and is reported as one: the question list is headed by a new claim
every round, so "which of several" was never the constraint. The second shows the attention order is a
necessary link and not a sufficient one: at seeds 0 and 1 the steward now attends to the shortfall and
does not choose to relieve it. That second link is the ranking, which reads the verb and not the
situation (the CHAR audit's F-CHAR-01), and is not this proposal's.

## The resolution

One ordering term inside one tier, on the precedent of tier 2, which already orders by `-|valence|`.

### Edit · owner `engine/season/queries/world_q.py::attention_key`

In `key()`, the tier-1 return `(1, 0.0) + tie` becomes `(1, -need) + tie`, where `need` is the held
claim's value when its predicate's stem is `data/requires.py::SHORTFALL_PREDICATE` (the one name of an
unmet-need claim; MATTER writes it, `decision/options.py::_from_shortfall_claim` reads it) and `0.0`
otherwise. The stem is read from its owner; no predicate is spelt at the site. The docstring's LIMIT
sentence is replaced by the rule. `[ASSUMPTION; medium; Jordan to correct; revert: (1, 0.0)]`.

It is a rule about a class of claim, not about a person, a place or an outcome: any holder of any rung
or seat whose ground records a shortfall is subject to it, and nothing is forced to happen. The order is a
fixed sort of the questions he attends to, not an outcome: which act he takes about the question is still
the chooser's sampled draw (A-9; the standing rule), and the `need` it reads is his own held claim's value
(his ledger), so no omniscience enters (`04` §A.2's `world_q` row; PART D row 42).

## Gate (execution artifacts)

1. `python -m engine.season.harness.scarce`, unassisted arm, seeds 0, 1, 2: the steward's deliberations
   include the shortfall question in the season after it is recorded (read off the harness's `asked`
   analogue: the question the chooser received), where today they do not.
2. Relief itself is gated jointly with the CHAR lane's choice edit
   (`02_CHAR_goal_lean_on_its_own_question.md`): with both, a claim-sourced `transfer.made` to the
   hungry town at two or more of the three seeds, and none with the steward's `hold` removed
   (`scarce.build(steward_holds=False)`, the harness's own control). Alone, this edit's reading is one
   of three, as measured above.
3. The realm: `corpus_run` seed 0 and a two-season `build_realm(0)` hash are re-recorded in
   `engine/season/tests/_realm_goldens.py` (`01_CORE_tests_one_golden_owner.md`), said plainly as re-records;
   the values are read on the batch's base, not typed here.
4. Named test (new, `engine/season/tests/test_attention_key.py`):
   `test_a_shortfall_claim_sorts_first_larger_first_in_tier_one` (a hand-built holder with two shortfall
   claims of 8 and 15 and a routine `stores.changed` claim, all tier 1: the 15 first, then the 8, then the
   routine one) and `test_tier_two_order_is_unchanged`.

## Falsifier

The unassisted steward still never receives the shortfall question at any of three seeds (the edit does
nothing), or relief appears in the control world whose steward holds nothing (the edit is not what
carries it).

## NERS reading

- **N.** Top-down (a governor's season): what a seat is for is answering what goes wrong beneath it.
  Bottom-up (the claim): the shortfall is recorded, carried and deposited, and then ordered by a hash.
  Lateral: tier 2 already orders by magnitude. Vertical: it is the upward half of the famine, the
  half that zooms out from a hearth's hunger to a seat's act. Removing it leaves relief to chance.
- **R.** The no-player half: a world in which stewards answer want is one that generates relief,
  neglect and blame without anyone watching. Strategy: a player who holds a seat is shown the need
  first.
- **S.** One comparison in one key; same methodology as tier 2. It pauses nothing.
- **E (last, against N and R).** One term. A reader can predict what a seat-holder turns to.

## Cost class

Edit (one line and a docstring), hash mover; its second link is the CHAR lane's proposal.

**Lands it and tier.** The B10 batch, an IN `valoria-author` session on `sonnet` (`high`), closed by B10's
`methodology-close` once. **Hash movers.** Every world in which a tier-1 holder holds a shortfall claim
(declared; re-pinned once with B10).

## Dependency edges

CHAR → the ranking must read the question (F-CHAR-01) before relief is reliable. SE → the same world is
the settlement lane's standalone scenario (`07_SE_valley_scenario.md`, title read, body not opened).
