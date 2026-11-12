# WR · A strand concludes on a conclusion

Reconciled: 2026-11-12, U5d closure — folded **A-45**, **A-46** and the addendum's standing-rule pass. Edit 3 (bounding the same-doer link: a doer's later deed joins a strand he opened, or joins by its subject) was listed for Jordan as the audit's §11 item 1; A-45 rules it (several strands that can each end), so edit 3 is no longer conditional and its `[ASSUMPTION]` reads as ruled, with the unbounded link kept as the control arm. A-46 adds one strife move: leaving a faction's creed or its head seat (a `release` of that `commit` or that seat-`hold`) is a move of the era; a routine release is not. Step added to edit 2: the move roster gains that kind, keyed on the released edge's object being a faction's creed Proposition or its `head_seat`. Edits 1–2's rules are eligibility; a strand concludes only on its closing move's drawn degree (`09_WR_B_draws_not_thresholds.md` edit 4).

## Status: PROPOSED

Carries finding F-WR-02 of `audits/09_WR_audit.md`. Evidence ids (E-nn) are that file's §12. One part of it
(edit 3) narrows a ratified assumption and is listed in the audit's §11 with both options; edits 1 and 2
follow the ratified text and need no ruling.

## What it changes in `engine/season/` at runtime

**One thing, through one consumer.** `queries/world_q.py::flow_stakes` (stamped by `questions_for` while
`Fixtures stamp_flow_stakes` is on, the shipped value) skips a strand its holder reads concluded
(`concluded_known`). Under edit 2 a person whose latest claim on a strand is a petition, a succession claim
or another content-opening kind no longer reads it concluded, so its referents stay among his occasions.
That is a **declared hash mover** on any seed where a person holds such a strand (between 0 and 27 persons of
75 to 83 in the runs of E-05 to E-12, by seed). Edit 1 alone moves no hash: the world reading has no consumer in the
loop (`world_q.py:4749-4752`).

## The problem

`strife-00` R6 (ratified, ED-IN-0316): *"A flow … terminates or resolves with a concluding outcome, or it
is not a flow."* §4: *"A strand cannot conclude on its own opening move."* As coded, the first is not
enforced and the second is enforced for a strand of one move only (`world_q.py:5162`).

| observation | run |
|---|---|
| 24 of 40 codes are terminal, among them the sided codes of `march.declared` (FR, WN, OW), which is also an opener for sides R and O | `harness/strife.py:143-145`; `strife_moves.yaml:74,84,91`; `world_q.py:5207` |
| a strand of 15 moves, 13 terminal, 11 of them openers, by 2 doers, reads `concluded`; its sequence is marches | seed 0, two seasons, E-05 |
| a strand of 8 moves, all `march.declared`, all terminal, reads `concluded` | seed 0, forcing arm, E-11 |
| two strands by one doer each (`WN-SB/SZ-FR`, `WN-FR-SB/SZ-FR`) read `concluded`: one person marched on an unopposed place | seed 1, three seasons, E-12 |
| the strand concluded at two seasons is gone at three: absorbed into a strand of 63 moves, 17 doers, 50 terminal moves, 34 opening moves | seed 0, E-05 against E-07 |
| the largest strand holds 63 of 75 strand moves (84%) at seed 0 and 45 of 61 (74%) at seed 1, three seasons | E-07, E-12 |
| person side, `concludes` lists `petition.filed`, `succession.claimed`, `dispensation.issued`, `transfer.made`, `record.given`, `tenure.opened` | `rosters.yaml: strife_kinds.lists.concludes` |

The terminal set comes from the study's "last substantive move of each case" (A3). Where a historian's
record stops is not what concluded the matter: a case whose last coded move is a petition ended on a
petition being filed, not because of it.

## The resolution, decided

1. **An opening move is never terminal.** The rule the world reading already applies to a content opener
   (`world_q.py:5212-5213`: *"a move that content-opens … is never terminal, though its kind is in
   `concludes`"*) holds for every opener.
2. **A kind that can open a strand by content does not conclude one at the person reading.**
3. (§11 item 1, not decided here.) **The same-doer link clause is bounded**, so one busy person does not
   join the realm's strife into one strand.

## The edits

### Edit 1 · `engine/season/queries/world_q.py::flows_in` (the one owner of `Move.terminal` for the world reading)

Old (`:5212-5213`):

```python
        m = Move(e.id, i, e.kind, a.actor if a is not None else None, refs, None, opens or content_opens,
                 bool(term(e, a)) and not content_opens)
```

New:

```python
        opening = opens or content_opens
        m = Move(e.id, i, e.kind, a.actor if a is not None else None, refs, None, opening,
                 bool(term(e, a)) and not opening)
```

The docstring's sentence "A move that content-opens, and each earlier move it takes, is an OPENING move and
is never terminal" becomes "An OPENING move (by kind, by side, by death verb or by content), and each
earlier move a content opener takes, is never terminal". An authority's march (side A) does not open and
stays terminal where its code is.

### Edit 2 · `engine/season/rosters.yaml: strife_kinds.lists.concludes` and its import check

Remove from `concludes` the members of `world_q.CONTENT_OPENING_KINDS`: `succession.claimed`,
`petition.filed`. The list becomes:

```yaml
      concludes: [army.arrived, petition.carried, covenant.offered, matter.determined, dispensation.issued,
                  rung.ceded, record.given, transfer.made, record.destroyed, tenure.opened]
```

`queries/world_q.py::check_strife_openers` gains one refusal, so the roster and the opener list cannot
drift: a kind in `CONTENT_OPENING_KINDS` that is also in `CONCLUDING_KINDS` raises `Unspecified` at import,
naming the kind. `tests/test_strife_kinds.py`'s re-derivation of `concludes` takes the same exclusion
(the test is the roster's existing check, edited with it).

Not removed, and why: `dispensation.issued`, `transfer.made`, `record.given` and `tenure.opened` are
concessions and settlements in the study (CO, XS, CP), which do conclude. Whether a *grant* can be told
from a *burden* is CR-67's question (`world_q.py:4775-4778`) and is left there.

### Edit 3 · the same-doer clause of `_links` (§11 item 1; written here so the edit is on file)

`world_q.py:5081-5083`:

```python
    if m.referents & s.refs or up & s.refs or m.referents & s.parents:
        return True
    return m.doer is not None and m.doer in s.doers
```

Option B of §11: the last line becomes

```python
    return m.doer is not None and m.doer in s.doers and (m.kind in OPENS_KINDS or s.opened_by(m.doer))
```

where `_Chain.opened_by(doer)` is true when `doer` did one of the chain's opening moves: a person's later
deed joins a strand he *started*, or joins by referent; a clerk who filed one petition in a strand does not
pull his unrelated march into it. `Move` gains nothing; `_Chain` gains one set (`openers`), filled in `take`.

## The gate that shows it worked

```sh
PYTHONHASHSEED=0 python -m engine.season.harness.strife 3 0 1 2 --strands
python -m pytest engine/season/tests/test_strife_flows.py engine/season/tests/test_strife_kinds.py -q   # the covering files, at the close
```

Passes when, on the first: no strand whose latest move is an opening kind prints `concluded`; and, with
`09_WR_story_instruments_that_can_fail.md` edit 3 landed, the `shape:` line's `closed` count equals the
`concluded` count (today they differ at every seed run). With edit 3: the largest strand's share of strand
moves falls below the 74% and 84% of E-07 and E-12 at the same seeds.

Hash discipline: edit 1 EQUAL (`build_realm(0)` and the one- and two-season pins unchanged); edit 2 a
declared mover, measured with `stamp_flow_stakes` on against off as H-274's guard was; edit 3 a declared
mover through the same consumer.

## The falsifier

- Edit 1: a planted strand `petition, petition, march(R)` reads `concluded` (it must not); a planted strand
  `requisition.taken, …, matter.determined` with no open referent does not (it must).
- Edit 2: a person holding `arrest.made` then `petition.filed` on one referent reads the strand concluded.
- Edit 3: two deeds of one doer, the first an opener, no longer link (they must); a non-opening doer's
  unrelated deed still links (it must not).

## NERS reading

- **N.** Remove edit 1 and the world reading keeps announcing endings on declarations (F-WR-02); nothing
  else in the tree says a strand ended. Top-down (the era's slot frees on a realm-rung terminal move) and
  bottom-up (a person's `concluded_known`) both read `Move.terminal`, so the rule holds in two directions;
  diagonal (person reading against world reading) improves: both now refuse a content opener.
- **R.** "Emergent and compelling narrative hooks … without player involvement" needs an ending to be
  distinguishable from a pause. Completeness: a strand with no terminal non-opening move stays open, which
  is R6's "or it is not a flow" read honestly: it is an open matter.
- **S.** One terminal rule for both readings; no second ladder.
- **E, last.** Two lines of code and two roster members against the only "it is over" signal the design
  has. High. Edit 3 is costlier (a new set on `_Chain`) and buys legibility at the strand level; its ratio
  depends on the ruling in §11.

## Cost class

Edit (1, 2). Small build (3), design-first on §11 item 1.
