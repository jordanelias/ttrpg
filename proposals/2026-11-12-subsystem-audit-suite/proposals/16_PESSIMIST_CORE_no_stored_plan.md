# 16 · PESSIMIST · CORE — no stored plan: delete the queue-reuse branch that never fires

## Status: PROPOSED

Carries F-PES-CORE-07 of `audits/16_PESSIMIST_CORE.md` (§1.1 pt 4, §2 row 1). Reference only
(CLAUDE.md §0.05). A deletion.

## What it changes in `engine/season/` at runtime (first)

**Nothing observable.** `loop/deliberate.py` stops remembering the unreleased tail of a person's plan
between rounds and stops fingerprinting his inputs to decide whether to reuse it. Every round, a person
with budget left is asked to choose, which is what already happens at every call. No content hash moves
(gate below).

## The problem (evidence)

- `deliberate.py:199-263` keeps `self._queued[p.id]` and re-plans only when
  `self._inputs.get(p.id) != fp or not queue`, `fp` from `_inputs_fingerprint` (`:468-552`, 85 lines with
  its notes), so that a plan is *"re-made only when the inputs change"*.
- **Realm, seed 0, three seasons: 0 of 1,137 released scenes came from a stored queue**; every release
  followed a fresh `choose()` call in the same round; 516 of 527 re-plans that found a queue released a
  different scene from the one queued (`run_dump.py 0 3`, `knock.py` baseline).
- **Headless world, seed 0, four seasons: 0 of 38**, and with the reuse branch cut outright (the
  fingerprint forced to differ at every call) the four season hashes are identical to the shipped run's
  (`19081c4a, 5405522c, 383206ba, 4cf2b09f`; `qreuse_small.py`). The cut was run and nothing died.
- The control that bounds this: showing the chooser a one-scene budget is **not** free (`qcut.py 0 2`:
  812 and 799 acts against 821 and 882). The plan a person makes with his whole budget in view shapes
  his next scene; only *storing its tail* is dead. This proposal touches the storing alone.
- Cost carried today: the fingerprint is computed per person per round over questions, tenures, the
  requires-stem claims of the ledger, body and travel leg; `driver.py:472-473` resets four dicts a
  season of which two exist for this branch; and the notes describe a behaviour (a plan spent over five
  rounds) the engine does not have.

## The resolution, decided

Delete the reuse branch and its fingerprint. Step 5 of the `needs_jordan` ladder (what makes sense for
the architecture): a rule that never selects its second branch on any world run here is not a rule.
`_drop_what_was_already_done` and `_qualify_by_round` stay: both act on the freshly chosen list.

Not chosen: making reuse fire (a coarser fingerprint, so a person sticks to a plan). That is a design
change to how persons decide (a person who ignores news for a season) and belongs to the CHAR lane if
anyone wants it; nothing measured here argues for it.

## Exact edits, by owner

1. **`engine/season/loop/deliberate.py`**
   - `:199-201` becomes `if b > 0:` followed by the existing `choose` / `as_scenes` / budget and slot
     checks / `_drop_what_was_already_done` / `_qualify_by_round`; `scenes` is that local list (empty
     when `b == 0`).
   - delete `fp = _inputs_fingerprint(p, qs)`, `self._inputs[p.id] = fp`, `self._queued[p.id] = scenes`
     and the function `_inputs_fingerprint` with its imports (`REQUIRES_STEMS`, `ledger_names` if no
     other use remains in the module).
   - keep `self._deliberated_at[p.id] = (w.tick, self.round)` (read by `_questions_at_barrier`).
2. **`engine/season/loop/driver.py`** `:472-473` and `__init__`: drop `_queued` and `_inputs`.
3. **Tests that assert reuse on a hand-built world** (the `test_u2_` family, where one plants equal
   inputs): delete those cases with the branch; the commit names them.

## Gate (an execution artifact, §0.2)

- Realm seed 0, three seasons: hashes `5ab73af2…`, `bacd687f…`, `52ff67bc…` unchanged.
- Headless seed 0, four seasons: `19081c4a, 5405522c, 383206ba, 4cf2b09f` unchanged.
- `engine/season/tests` goldens unchanged except the deleted reuse cases.

## Falsifier

Any pinned hash moves. Then some world does reuse a stored tail, the cut is not free there, and that
world is the evidence this proposal lacked: keep the branch and cite it.

## NERS reading (E last)

- **N.** The cut was executed: nothing died on two worlds at the shipped configuration. The N-line
  (*"re-made only when the inputs change"*) is false because the inputs always change.
- **R, S.** Unaffected: no behaviour changes.
- **E.** About a hundred lines of code and notes, one per-round computation, two driver dicts.

## Cost class

Edit (a deletion). No golden re-record expected; if one is needed the falsifier has fired.
