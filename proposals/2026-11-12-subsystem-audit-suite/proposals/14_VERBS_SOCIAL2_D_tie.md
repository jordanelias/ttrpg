# 14 · VERBS · SOCIAL2 · D — `tie`: a chosen bond, drawn for, read by the telling; `knot` handed to the Thread lane

## Status: PROPOSED

Carries `audits/14_VERBS_SOCIAL2.md` §10. Batch S2-D. Follows `08_FI_08_knots-season-form.md` §3 (the
reader first, then the producer) and does not redo it.

## What this changes in `engine/season/` at runtime

Nothing until FI-08 §3's two conditions hold (two-hop told chains above 0 in seeded play: FI-02's gate;
the person-side `present_persons` decline). Then a person may try to bind himself to someone present;
whether the bond takes is a draw; a taken bond lowers the odds against his tellings to that partner and
raises his partner's weight as a teller in his eyes. Fixture `tie_gain` at 0 is the control.

## The problem (evidence)

`verb_table.yaml` `tie / knot`: `requires: —`, no operand for a partner, no effect, absent from
`resolvable_verbs()` (`aperture 1 0`: formed 83, offered 0). `H-182` (the row's `effect_decline_note`):
IN-32's `_eff_tie` executed 11 times at seed 0 and nothing read the edges (`teller_weight`'s relation term
never ran for want of chained told claims); `knot` has a reader (`epistemic._ch_witness_key`) that reads
it undirected against Layer 1 (`04` §A.3 row 9: two directed edges). The row names two kinds for one
opener.

## The resolution, decided

Split the row; build `tie` as an ordinary contested opener; leave `knot` declined and owned by the
Thread lane. Ladder: step 3 (`04` §A.3 row 9, directed edges, each owned by its party; `release`'s
domain already holds both kinds), step 1 (the standing rule: whether a bond takes is a draw), step 5 (one
opener per kind: a `kind` operand would be a scale-local dialect).

## Exact edits, by owner

1. **`engine/season/verb_table.yaml`**: delete the `tie / knot` row; add, carrying its notes forward:
   ```yaml
   - verb:        "tie"
     stratum:     social
     eligibility: [own]
     beneficiary: actor
     counterparty: to
     requires:    "the partner is with him and known to him"
     requires_typed: {all: [{form: relation, of: to, relation: with, conjunct: present},
                            {form: own_ledger, of: to, conjunct: known}]}
     contests:    "a standing"
     writes:
       Overwhelming: ["Tenure.since"]
       Success:      ["Tenure.since"]
       Partial:      ["Tenure.since"]
       Failure:      []
     emits:
       Overwhelming: ["bond.formed"]
       Success:      ["bond.formed"]
       Partial:      ["bond.formed"]
       Failure:      ["bond.refused"]
     emits_on_refusal: {present: ["tie.refused"], known: ["tie.refused"]}
     grade:       assumption
   - verb:        "knot"
     stratum:     thread
     eligibility: [own]
     requires:    "—"
     writes:      ["Tenure.since"]
     emits:       ["bond.formed"]
     emits_on_refusal: []
     grade:       ruled
     effect_decline_note: "<the H-182 text for knot; owned by the 29f / Thread lane; FI-08 §1>"
   ```
   `resolvable_verbs()` admits `tie` once its effect exists; `knot` stays out.
2. **`rosters.yaml`**: `verb_capability: tie: "copying"`; new `tie_obstacle` (`obstacle_default` base;
   the partner's `regard` of the actor below zero +1, above +1 −1; rank gap per rung +1).
3. **`loop/effects_information.py`** (the module holding `_eff_commit`, beside it; the `"tie"` literal
   must sit in a file `_derive_openers_from_effects` walks): `_eff_tie(w, a, res)` re-lands IN-32's body (attempt
   `53ed995d`) with `degree=res.degree` on the new `Tenure(..., "tie", ...)`, id salted
   `f"tie:{to}:{a.id}"`; declines `NO_CHANGE` where the actor already owns a live `tie` to `to`.
4. **`decision/options.py::teller_weight`**: IN-32's `tied` term, reading the hearer's own live `tie` to
   the teller and its `degree` (`band_entry`-scaled, Partial half), times fixture `tie_gain`.
5. **`rosters.yaml: tell_obstacle`** (S2-C §4): the `tie: -1` key reads the teller's own live `tie` to the
   hearer.
6. `data/verbs.py`: the verb count read by R-05's instrument moves 67 → 68; no code names the count.

## Gate (execution artifact)

After FI-08 §3's conditions: `build_realm(s)`, s = 0, 1, 2, two seasons, `PYTHONHASHSEED=0`: `tie`
attempted > 0, both `bond.formed` and `bond.refused` occur across seeds; `teller_weight` reads a tied
relation > 0 times; `tie_gain` 0 and 0.5 hash differently; `tie_gain` 0 hashes as the control (no tie
term).

## Falsifiers

- `tie_gain` 0 must hash as the control; if not, a tie is read somewhere it should not be.
- A tie by A to B must not lower the odds of B's tellings to A (directed: B owns no edge).
- A `knot` must never form while its row is declined.

## NERS reading

N: the one chosen person-to-person bond; without it friendship exists only as regard, which nobody
chooses. R: networks of trust form with no player and change who believes whom. S: directed edges owned
by their party, closed by `release`; the bond enters the telling's odds as one more modifier. E, last:
one row split, one effect re-landed, one term and one roster key.

## Cost class

Small build, after FI-02's gate.
