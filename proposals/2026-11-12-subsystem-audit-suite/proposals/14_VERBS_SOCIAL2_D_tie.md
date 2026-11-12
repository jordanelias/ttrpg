# 14 · VERBS · SOCIAL2 · D — `tie`: a chosen bond, drawn for, read by the telling; `knot` handed to the Thread lane

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-21) — `tie_obstacle` is folded into the one roster (`U5c_SC_one_obstacle_form.md` §2). The split of `tie` and `knot` (edit 6) is Jordan's A-28.
Reconciled: 2026-11-12, wave-3 rewrite lane W3-4a — applied `unified/work/R4_READ.md` §1.6 and 7b.6: edit 3 is written from the row, not "re-landed" (the attempt `53ed995d` is not reachable from this clone); edits 2 and 5 fold into the one composer and the `favour` source (C-21, the head line; C3-C10); edit 4's `band_entry` is `task_fraction` (U1 D-U1-11l); `obstacle_default` (deleted, C-04) is the composer's stand-in; edit 6's count is a reading at its batch, never typed (`unified/U3_CONFLICT_LEDGER.md` C3-N30); A-81, A-30, U3 batch B25, R4 7b.0 block.

Reconciled: 2026-11-12, unification lane U4c (test 9; read from this file's own Gate and Falsifiers) — hash movers declared: none at landing if `tie_gain` is landed at its control, 0 (the file's NUMBER row says "control 0"), because "`tie_gain` 0 must hash as the control" (Gate, first Falsifier); the one declared mover is the later flip of `tie_gain` off 0 (the gate hashes 0 and 0.5 differently), re-pinned once in that flip's own commit and said plainly as a re-pin (CLAUDE.md §7). The B25 count reading (67 to 68) is a reading at the batch, never a typed number (C3-N30).

## Status: PROPOSED

Lands in batch: B25 (`unified/U3_DEPENDENCY_ORDER.md` §3.1), after `08_FI_08_knots-season-form.md` §3 in the same batch.
Depends on: `08_FI_02_rumour-that-travels.md` (B11: two-hop told chains, `present_persons`); `08_FI_08_knots-season-form.md` (B25); `U5c_SC_one_obstacle_form.md` (B05: `regard`, the `favour` source; `rank_gap` lands with `14_VERBS_BINDING_A` in B21).
Lane: FI. Tier (R4 7b.0 (1)): `sonnet` producer, effort `high`; one `opus` read of the `tie_gain` arms. Test file: `engine/season/tests/test_vm_s2_d_tie.py` (the gate's arms and the three falsifiers as functions).
Standing (R4 7b.0 (4)): the pool is the one pool rule (`sigma_leverage.pool_of`, D-U1-08) on the actor's skill score (A-6); the governing attribute as levels (A-7); a wound a level against the roll (A-8). The draw takes `H(w.world_seed, w.tick, <actor id>, "tie.standing")` (A-30). **A-81:** `bond.refused` is witnessed by both parties (a claim of it to each): a refused bond is a remembered deed.

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
2. **`rosters.yaml`**: `verb_capability: tie: "copying"` (the row's own `capability:` cell at CAP A2/A3,
   D-U1-07). *(W3-4a: no `tie_obstacle` table, C-21.)* The obstacle, through the one composer:
   `difficulty` + `opposition` (the partner's skill score, A-79) + `regard` (OBS member 7: the partner's
   hostile stance toward the actor) + `rank_gap` (member 6); the partner's favourable stance is a `favour`
   level for the actor (OBS §3), not a −1.
3. **`loop/effects_information.py`** (the module holding `_eff_commit`, beside it; the `"tie"` literal
   must sit in a file `_derive_openers_from_effects` walks). *(W3-4a: written from the row; the earlier
   "re-lands IN-32's body (attempt `53ed995d`)" is withdrawn — that commit is not reachable from this
   shallow clone, so its body cannot be the source.)*
   ```python
   @effect_for("tie")
   def _eff_tie(w, a, res=None) -> Change:
       to = _operand(a, "to")
       if res is None or to is None or to not in w.persons:
           return NO_CHANGE
       if any(t.kind == "tie" and t.subject == a.actor and t.object == to and t.live for t in w.tenures):
           return NO_CHANGE                      # he already owns a live tie to `to`
       edge = Tenure(H(w.world_seed, w.tick, a.actor, f"tie:{to}:{a.id}"), a.actor, to, "tie",
                     since=w.tick, degree=res.degree)
       return Change((Subject.edge(edge),), lambda: w.add_tenure(edge))
   ```
   Typed in: `(World, Act, Resolution)`; out: `Change`. The edge is the actor's own (T-m); no edge is
   opened for the partner (directed, `04` §A.3 row 9). The names are `_eff_commit`'s, read at the tree
   (`loop/effects_information.py:1252-1310`: `@effect_for`, `_operand(a, …)`, `Tenure(id, subject, object,
   kind, since=…)`, `Change((Subject.edge(nt),), lambda: w.add_tenure(nt))`); `degree=` is the `Tenure`
   field `determine`'s `_disposal` already fills (`04` §F.4).
4. **`decision/options.py::teller_weight`**: a `tied` term reading the hearer's own live `tie` to the teller
   and its `degree`, scaled by `rosters.yaml: task_fraction[degree]` (W3-4a: was `band_entry`, the same
   values under a second name; Partial half), times fixture `tie_gain` (control 0; NUMBER row).
5. *(W3-4a: no edit.)* The teller's own live `tie` to the hearer already enters a telling's odds as the
   `favour` source (OBS §3: "a live `tie` of the actor to the counterparty"); `tell_obstacle` is not added
   (`14_VERBS_SOCIAL2_C` §4 as reconciled).
6. `data/verbs.py`: the split adds one verb row, so the count read by R-05's instrument moves; no code
   names the count, and the count is quoted as a reading at the batch that lands it (B25), never typed
   into prose (C3-N30: 67 today, T-7; `01_CORE_tests_one_golden_owner.md` item D re-reads its pin at B25).

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
by their party, closed by `release`; the bond enters the telling's odds as a `favour` level, as every
favourable circumstance does. E, last: one row split, one effect written, one term.

## Cost class

Small build, after FI-02's gate.
