# CHAR — adversarial steelman audit

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 601e715 (working tree)

## 0. Verdict

(provisional head, written before the reading finished; replaced at the close)

The decision layer is a sound *structural* basis for an emergent-narrative game and not yet a sound
*behavioural* one. The person-side wall (AX-2: no `World` under `engine/season/decision/`), the computed
option set (`options.py::opening_set`), the single owner of the score (`choose.py::score_terms`) and the
candidate-keyed Plackett-Luce draw (`choose.py::_sample_order`) are real and execute. What the chooser
ranks by is two terms only, a pursuit dot product and a stance term; goals, ambitions, need, risk and
horizon do not weigh a candidate, and the only departure from the score's optimum is one realm-wide
temperature, identical for every person.

## 1. What it is, as coded

(first part, from `decision/choose.py` and `decision/options.py` read in full)

- `decision/options.py::opening_set(p, v, q, fx)` forms the candidate set from `VERB_TABLE`, in sorted
  verb order, by person-side eligibility, the question's referents, a known-false belief test
  (`epistemic.belief_contradicts`) and operand derivation.
- `decision/choose.py::make_ranker` scores each candidate with `score_terms` -> `(pursuit, stance)`,
  settles effort variants (`settle_efforts`), orders by score (`score_order`) and samples the order
  (`_sample_order`, Gumbel noise at `choice_temperature`).
- `decision/choose.py::release` packs the order into scenes against the budget the person asked for
  (`pack_scenes`) and lets a telling declare a later chosen act (`declare_intents`).

(the remaining sections are appended below as the reading completes)
