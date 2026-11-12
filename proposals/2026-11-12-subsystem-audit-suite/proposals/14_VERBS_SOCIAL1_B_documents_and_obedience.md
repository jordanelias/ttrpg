# VERBS SOCIAL1 · B — documents reach their addressees, and an order can be obeyed or refused, by a draw

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-07, C-21, C-25, C-34) — four readings. (1) §1: a decree is proclaimed (Jordan, A-21), so `comply` and `evade / defy` on a decree form from the claim that it was issued and do not wait on `give`; the addressed-document occasion stays for a covenant and a challenge. (2) `witnesses` is the roster member `watch`; rank standing against an act is `rank_gap`; the band a document was drawn up at is the content key `force`. (3) A row drawn with nobody opposite takes one of two loadable shapes, and a prize this file names that the roster does not keep is read through `U5c_VERBS_residue_and_governance_owner.md` §1 and §2. (4) Covenant acceptance is the counterparty's own `commit`.

## Status: PROPOSED

Batch S1-B of `audits/14_VERBS_SOCIAL1.md` §14 (verbs `give`, `comply`, `evade / defy`, `covenant`'s
in-force reading). Authored in part by Fable; completed by Opus after the Fable usage limit (2026-11-12).
Reference only (CLAUDE.md §0.05). Read at `84d2a02`. Needs S1-A and lane A step 1 (Record-kind formation).

## What it changes in `engine/season/` at runtime

(1) A person holding a document addressed to someone else forms a `give` of it to that addressee.
(2) `give`, `comply` and `evade / defy` become **drawn** rows (Degree-keyed `writes:`/`emits:`, rolled
through the one social roll, obstacle by SC-OB's composition) with a write at every band. (3) `comply`
opens an `oblige` Tenure naming the writ; `evade / defy` closes the hold and writes stance. (4) A reader,
`world_q.covenant_in_force`, exists and a breach of an in-force covenant is a deed the other party judges.
Declared hash mover.

## The problem, with evidence

`aperture 2 0` (`scratchpad/runs/VERBS_PHYSICAL/aperture_2_0.txt`): `give` 19 attempted, 1 executed;
`comply` 33/0/33, `evade / defy` 5/0/5 (all `exists:dispensation=0`, repaired by lane A); `compliance.given`
and `compliance.withheld` never emitted. `world_q.writs_held`: writs are minted into the issuer's hand
(`ED-IN-0292` (1), RULED NO "for now") and reach the addressee only by `give` (H-229). `comply` and
`evade / defy` have no effect body and write `[]` (`[corpus]`: "emits and writes nothing, untagged"). The
covenant's in-force reading is "a reading nothing performs yet" (`_eff_covenant`'s docstring). Under
`AUDIT_BRIEF.md`'s Standing rule, an obedience with no resolution roll is a named known defect.

## The resolution, decided

### 1. `give`: the addressed-document occasion, and a drawn hand-over

- **Occasion.** `rosters.yaml: delivery_sourced` (new; `values: [give]`): a verb named here forms, for each
  Record on the holder's own live `hold` whose content names an addressee other than the holder
  (`person_q.addressed_to`, the one owner of the addressee keys; read off his own content claim, as
  `held_record_claims` does), one Candidate with `subject` = the Record and `to` = that addressee. R-WITH
  (S1-A) applies to `to` as to any `with` conjunct, so an absent addressee costs no scene.
- **Ranking.** `choose` adds `delivery_weight × (the maker's own score for the act that minted it)` when the
  holder is the maker (fixture `delivery_weight`, proposed 1.0, control 0); otherwise the ordinary score.
- **Draw.** Pool `pool_default` (no capability: a hand-over is no skill). Obstacle (SC-OB form) = `plain`
  + `regard` (the receiver's stance toward the giver) + `unwelcome` † (the receiver's own `deeds_judged`-style
  valuation of the document's terms against his pursuits, positive only; read by the host builder from the
  receiver's side, `unwelcome_step` fixture, control 0).
- **Bands.** Overwhelming, Success, Partial: the existing two-hold write; Partial additionally emits
  `record.given.protested` † (a reluctance deed deposited to witnesses); Overwhelming adds a +1 stance row
  from receiver to giver. Failure: no write to the hold; emits `give.refused` with reason `declined`; the
  receiver's firsthand claim of the tender is deposited by WITNESS as for any Event naming him, and that
  claim counts as **service**: `world_q.served(w, rid, pid)` is True once the addressee holds a firsthand
  claim of a tender of `rid`, and the answer windows (challenge, writ evasion) start from it.

### 2. `comply` and `evade / defy`: one obedience effect, drawn

- **`comply` draw.** Pool: `verb_capability[verb_of_terms]` where the writ's `terms` Proposition names a
  verb (`[UNVERIFIED]` that a Proposition carries a verb; if not, `pool_default`). Obstacle = `routine` +
  `stakes` (`stakes_ob['oblige']`, SC-OB) + `violated` † (`violated_pursuits` of the terms' lean, his own) +
  `distance` † (the writ's `at` is not his place: `distance_ob`, control 0).
- **`comply` bands.** Overwhelming: `oblige` Tenure, full term; Success: full term; Partial: half term;
  each closes his `hold` on the writ and emits `compliance.given`. Failure: no Tenure, hold kept, emits
  `compliance.failed` † (judged lightly: its `deed:` alignment cells are authored at half the weight of
  `compliance.withheld`'s).
- **The edge.** In `loop/effects_governance.py` (beside `_eff_oblige`, so the opener walk reads the literal):
  ```python
  @effect_for("comply")
  def _eff_comply(w, a, res=None) -> Change:
      rid = _operand(a, "subject"); seat = issuing_seat(w, rid)
      held = hold_force(w, rid)
      if res is None or held is None or held.subject != a.actor:
          return NO_CHANGE
      term = _writ_term(w, rid, half=(res.degree == PARTIAL))     # the writ's last due tick, or half of it
      edges = [Tenure(H(w.world_seed, w.tick, a.actor, f"oblige:{seat}:{a.id}"), a.actor, seat, "oblige",
                      since=w.tick, term=term, payload={OBEYED_WRIT: rid}, degree=res.degree)] if seat else []
      def perform():
          held.until = w.tick
          for e in edges: w.add_tenure(e)
      return Change(tuple(Subject.edge(e) for e in (*edges, held)), perform)
  ```
  `issuing_seat(w, rid)` (`queries/world_q.py`, new): the `via` of the act whose Event minted `rid`, through
  `state/attribution.py::causing_act`; `None` for a seatless mint. `state/gate.py::purview_reaches`' oath
  clause **skips** an `oblige` carrying `OBEYED_WRIT`, exactly as it skips `DETERMINED_BY`: an obedience is
  not an oath and must not hand the seat the complier's ground. The `oblige` write is admitted by `T-m` (his
  own edge). `[UNVERIFIED]` that the gate admits the hold close and the oblige open in one write under the
  existing bases; if not, the hold close rides `release`'s basis.
- **`evade / defy`.** Payload `mode` from `rosters.yaml: choice_sourced` `"evade / defy": [mode]` and a
  roster `defiance_modes: [evade, defy]`. Draws and bands as `audits/14_VERBS_SOCIAL1.md` §0.6 and §7:
  `evade` = `tradecraft` vs `routine` + `purview` † + `witnesses` †; `defy` = `argue` vs `routine` +
  `opposition` + `regard`. Writes at the standing bands: hold closed; `defy` a stance row (−1, weight 1;
  −2 at Partial). `evade`'s notice at the due tick is a stage `(due, "answer:<pid>")` appended to the writ's
  `Record.stages` at Success and Partial; MATTER's maturation of that label emits `compliance.withheld`
  (attributed at Partial only). `[UNVERIFIED]` whether `loop/matter.py` can emit a row-declared kind per
  stage label; if not, one MATTER step reads `answer:` labels — owner `loop/matter.py`.
- **Rows.** `comply`: `writes: {Overwhelming: [Tenure.since, Tenure.until], Success: […same], Partial:
  […same], Failure: []}`, `emits: {…: [compliance.given], Failure: [compliance.failed]}`, `contests: "an
  order"`, `capability` per DICE's map. `evade / defy`: `writes` by band per the above (`Tenure.until`,
  `Person.stance`, `Record.stages`), `emits` `compliance.withheld` at the bands that announce it,
  `compliance.yielded` † at `defy`'s Failure. Every pair is a `write_matrix.yaml` row already
  (`Record.stages`, `Person.stance`, `Tenure.*`); `[UNVERIFIED]` for `(Tenure, term)` on a `comply` writer.

### 3. `covenant`: the in-force reader and breach

- **Draw at drafting** (§0.6): pool `brokerage` †; obstacle `routine` + `divergence` † + `regard`, both from
  the maker's own claims; band → content key `standing` (3/2/1), added to `rosters.yaml: record_kinds`'s
  `dispensation` keys (as an optional key; `issue` writes none). Failure: `covenant.refused` (reason
  `terms would not hold`), no Record.
- **Reader.** `queries/world_q.py::covenant_in_force(w, rid) -> float`: the Record's maker and its `to` each
  hold a live `commit` on its `terms`; returns `standing × min(degree_weight(c) for the two commits)` (the
  commit degree is S1-D's), else `0.0`. Consumers: FA's tribute `_renewals`, MB's `mustered`; named, not
  edited here.
- **Breach.** `release` of a `commit` whose object is the `terms` of an in-force covenant already earns its
  row's whole `emits:` (`_eff_release`'s commit branch); WITNESS deposits it to those present. The other
  party is told by the existing told channel or reads it at his next contact. Its judgement uses the
  existing `deeds_judged`; this proposal authors the `deed:` cells for `commitment.ended` on a covenant's
  terms at a weight × `covenant_in_force` at the moment of release (`[ASSUMPTION; medium]`: the weight
  rides the claim's confidence, the one numeric slot WITNESS fills).

## Exact edits, by owner, in landing order

1. `rosters.yaml`: `delivery_sourced`, `defiance_modes`, `choice_sourced` row for `evade / defy`, the
   `dispensation` `standing` key, new `obstacle_terms` members (`unwelcome`, `violated`, `distance`,
   `purview`, `witnesses`, `divergence`), new `verb_capability` rows (`evade / defy: tradecraft` keyed by
   mode is not expressible — use `tradecraft` for both and let `defy` read `argue` through a
   `capability_by_mode` sub-map, `[ASSUMPTION]`), new kinds (`compliance.failed`, `compliance.yielded`,
   `record.given.protested`) in `EMITTED_KINDS` via the rows.
2. `data/fixtures.py`: `delivery_weight`, `unwelcome_step`, `distance_ob`, `witness_step`, each with a
   control 0 and a NUMBER row in `hole_register.yaml`.
3. `verb_table.yaml`: rows `give`, `comply`, `evade / defy`, `covenant` made Degree-keyed and `contests:`;
   `give` gains `writes`/`emits` per band as §1; notes cite this file.
4. `queries/world_q.py`: `issuing_seat`, `served`, `covenant_in_force`.
5. `state/gate.py::purview_reaches`: the `OBEYED_WRIT` skip beside `DETERMINED_BY`.
6. `loop/effects_governance.py`: `_eff_comply`, `_eff_evade_defy`; `loop/effects_information.py::_eff_give`
   reads `res.degree` (declines at Failure → the row's Failure emits) and `_eff_covenant` writes `standing`.
7. `seam/wrappers/sigma.py::contest_input`: the new operands, from the row and the counterparty's side.
8. `decision/options.py`: the `delivery_sourced` occasion; `decision/choose.py`: `delivery_weight`.

## Gate (execution artifact)

- Planted world (one seated issuer, one co-located addressee, one writ in the issuer's hand), 20 seeds,
  `PYTHONHASHSEED=0`: `give` resolves at ≥ 3 distinct bands; at the taking bands the addressee forms
  `comply` or `evade / defy` next round; `comply`'s band distribution shifts toward Failure when the writ's
  terms violate his pursuits (the `violated` term moved, all else equal).
- `aperture 2 s`, s = 0, 1: `record.given` > 0 and its addressee-matching share reported.
- Covenant: planted maker and counterparty; after both commit, `covenant_in_force` > 0; after a release, a
  deed claim in the other's ledger and `holds_dispute` True at a rate over seeds.

## Falsifier

A taking band at which the hold does not move, or a Failure that writes and deposits nothing. A `comply`
whose `oblige` widens the seat's purview (`purview_reaches` True through it). A band distribution that does
not move when `violated` or `unwelcome` moves (the state is not setting the odds). Control: all new
fixtures 0 and `delivery_sourced: []` reproduce S1-A's hash except for the draws the rows now take; that
difference is the declared mover.

## NERS reading

- **N:** three chains (writs, challenges, covenants) die at delivery today; obedience is a known
  deterministic defect.
- **R:** orders are obeyed, botched, evaded or defied with nobody watching; each leaves a record others
  judge; a good position still loses sometimes.
- **S:** one roll, one obstacle composition, `oblige` reused; no new Tenure kind.
- **E, last:** one occasion, two effect bodies and a reader against three dead chains.

## Cost class

Small build across `rosters.yaml`, `verb_table.yaml`, two effect files, `world_q`, the gate's one clause and
the seam's input. Declared re-record of the season pins.
