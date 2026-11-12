# VERBS SOCIAL1 · B — documents reach their addressees, and an order can be obeyed or refused, by a draw

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-07, C-21, C-25, C-34) — four readings. (1) §1: a decree is proclaimed (Jordan, A-21), so `comply` and `evade / defy` on a decree form from the claim that it was issued and do not wait on `give`; the addressed-document occasion stays for a covenant and a challenge. (2) `witnesses` is the roster member `watch`; rank standing against an act is `rank_gap`; the band a document was drawn up at is the content key `force`. (3) A row drawn with nobody opposite takes one of two loadable shapes, and a prize this file names that the roster does not keep is read through `U5c_VERBS_residue_and_governance_owner.md` §1 and §2. (4) Covenant acceptance is the counterparty's own `commit`.
Reconciled: 2026-11-12, wave-3 rewrite lane W3-4a — the head applied to the body (`unified/work/R4_READ.md` §1.5, §2, 7b.6): `comply` declares `contests: "a task"` (C-25: no prize `an order`); `delivery_weight` and the `decision/choose.py` edit are deleted (`unified/U3_CONFLICT_LEDGER.md` C3-L10, J-R4-2 taken A: `give` is ranked by its alignment cells and stance; the addressed paper enters through formation); `issuing_seat` exists in the tree (`queries/world_q.py:1573`, with a `verb` parameter) and is not "new"; the `evade` answer stage's MATTER emission is replaced (C3-C7: MATTER emits `term.matured` only; `compliance.withheld` is computed when read and deposited by WITNESS); `witnesses`/`witness_step` → `watch`/`watch_step`, `distance_ob` → `distance`/`distance_step` (U1 R-22, R-23; OBS members land with their first reader, MAT_A and MAT_B in B12); the covenant's band key `standing` → `force` (U1 §3 "standing"); A-21 confines §1's `give` occasion for a writ (head item (1)); A-63/A-64 for `give` (C3-C13); A-81, A-30, U3 batch B28, R4 7b.0 block. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "ordinary score" → "choice score" (the chooser's, glossary *score*). A-98 vocabulary lane (2026-11-12, A-98; ledger `unified/work/A98_SWEEP.md`): "capability" in prose → skill (2); "trained score/rank" → skill score (1); "talent" → attribute or governing attribute (1).

## Status: PROPOSED

Lands in batch: B28 (`unified/U3_DEPENDENCY_ORDER.md` §3.1), before `14_VERBS_SOCIAL1_D` in the same batch.
Depends on: `14_VERBS_SOCIAL1_A_formation.md` (B11); `06_FA_decree_binds.md` (B21: a decree's answers form from the claim of its issue, A-21); `U5c_VERBS_residue_and_governance_owner.md` §1 and §4 (B07); lane A (B01: Record-kind formation); `05_SC_obstacle_difficulty_and_modifiers_B.md`/`U5c_SC_one_obstacle_form.md` (B05) and the members `watch`, `distance` landed in B12; `02_CHAR_choice_alignment.md` (B10: the `give` alignment cells, CHAR's to author).
Lane: SC. Tier (R4 7b.0 (1)): `sonnet` producer, effort `high`; the three contested rows and `_eff_comply` `opus`; one `opus` read of the 20-seed band tables. Test file: `engine/season/tests/test_vm_s1_b_documents.py` (one function per gate).
Standing (R4 7b.0 (4)): the pool is the one pool rule (`sigma_leverage.pool_of`, D-U1-08) on the actor's skill score in the row's skill (A-6; `pool_default` where none); the governing attribute as levels (A-7); a wound a level against the roll (A-8). Draws: `H(w.world_seed, w.tick, <actor id>, "<verb>.<prize>")` for `give`, `comply`, `evade / defy`, `covenant` (A-30). A `give` is a visit: it occupies its receiver for the round (A-63); precedence, appointments and the waiting petition are `28_CORE_scene_access_A`–`C`'s (A-64; C3-C13). **A-81:** each band names its write below; a refused tender, a failed compliance and a yielded defiance are each witnessed deeds.

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
- **Ranking.** *(W3-4a, C3-L10: the `delivery_weight` summand is deleted.)* `give` is ranked by the
  choice score: the `give` alignment cells of `rosters.yaml: tables.alignment` (CHAR's to author,
  `02_CHAR_choice_alignment.md`) and the actor's stance toward the receiver (`architecture/ARCHITECTURE_V2.md`
  §F2: conviction × alignment + stance). The addressed paper enters through formation (the occasion
  above), not through a score term. Gates that read the summand re-read the formation set instead.
- **Occasion under A-21.** For a writ (a `dispensation` minted by `issue`) the occasion is not the road to an
  answer: a decree is proclaimed, and `comply` / `evade / defy` form from the claim that it was issued
  (`06_FA_decree_binds.md`); `delivery_sourced` still forms a `give` of a writ (the paper is evidence a
  bench can be shown) and is the road for a covenant and a challenge, which stay in person.
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
  `stakes` (`stakes_ob['oblige']`, SC-OB) + `violated` (OBS member 14; `violated_pursuits` of the terms'
  lean, his own) + `distance` (OBS member 20: the `contain` edges between the writ's `at` and his place;
  fixture `distance_step`, landed by `14_VERBS_MATERIAL_B` in B12) + the writ's `force` (the band it was
  issued at, `14_VERBS_BINDING_D` edit 9; a strong writ is easier to obey and harder to evade).
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
  `issuing_seat(w, rid, verb=None)` (`queries/world_q.py:1573`, **existing**; W3-4a: not new): the `via` of
  the act that minted `rid`; `None` for a seatless mint. Extend it only if a writ's creating Event is not the
  first naming the Record (R4 7b.6 (iii)); otherwise no edit. `state/gate.py::purview_reaches`' oath
  clause **skips** an `oblige` carrying `OBEYED_WRIT`, exactly as it skips `DETERMINED_BY`: an obedience is
  not an oath and must not hand the seat the complier's ground. The `oblige` write is admitted by `T-m` (his
  own edge). `[UNVERIFIED]` that the gate admits the hold close and the oblige open in one write under the
  existing bases; if not, the hold close rides `release`'s basis.
- **`evade / defy`.** Payload `mode` from `rosters.yaml: choice_sourced` `"evade / defy": [mode]` and a
  roster `defiance_modes: [evade, defy]`. Draws and bands as `audits/14_VERBS_SOCIAL1.md` §0.6 and §7:
  `evade` = `tradecraft` vs `routine` + `purview` (OBS member 21) + `watch` (OBS member 22; was
  `witnesses`); `defy` = `argue` vs `routine` + `opposition` + `regard`. Writes at the taking bands: hold
  closed; `defy` a stance row (−1, weight 1; −2 at Partial). `evade`'s notice at the due tick is a stage
  `(due, "answer:<pid>")` appended to the writ's `Record.stages` at Success and Partial by the act itself (a
  RESOLVE write, `(Record, stages)` being RES/ACTS, `write_matrix.yaml:346-352`). *(W3-4a, C3-C7: the
  MATTER emission is replaced.)* MATTER matures the Record's term and emits `term.matured` only
  (`(Record, matured)`, `write_matrix.yaml:339-345`); "withheld" is **computed when read** (an `answer:<pid>`
  stage whose due has passed and that no later act entered) and WITNESS deposits `compliance.withheld` from
  the `term.matured` Event of that Record to its issuer and those present (attributed at Partial only).
  `loop/matter.py` is not edited by this file.
- **Rows.** `comply`: `writes: {Overwhelming: [Tenure.since, Tenure.until], Success: […same], Partial:
  […same], Failure: []}`, `emits: {…: [compliance.given], Failure: [compliance.failed]}`, `contests: "a
  task"` (W3-4a, C-25: no prize `an order`; nobody stands opposite the complier), `capability` per DICE's
  map. `evade / defy`: `writes` by band per the above (`Tenure.until`,
  `Person.stance`, `Record.stages`), `emits` `compliance.withheld` at the bands that announce it,
  `compliance.yielded` † at `defy`'s Failure. Every pair is a `write_matrix.yaml` row already
  (`Record.stages`, `Person.stance`, `Tenure.*`); `[UNVERIFIED]` for `(Tenure, term)` on a `comply` writer.

### 3. `covenant`: the in-force reader and breach

- **Draw at drafting** (§0.6): pool `brokerage` †; obstacle `routine` + `divergence` † + `regard`, both from
  the maker's own claims; band → content key `force` (3/2/1; W3-4a: was `standing`, U1 §3 — a document's
  band is `force`, the key `14_VERBS_BINDING_D` edit 9 adds for `issue`), one optional key of
  `rosters.yaml: record_kinds`' `dispensation` shared by both minters. Failure: `covenant.refused` (reason
  `terms would not hold`), no Record.
- **Reader.** `queries/world_q.py::covenant_in_force(w, rid) -> float`: the Record's maker and its `to` each
  hold a live `commit` on its `terms`; returns `force × min(degree_weight(c) for the two commits)` (the
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
   `dispensation` `force` key (if `14_VERBS_BINDING_D` edit 9 has not added it), the `obstacle_terms`
   members this file is the first reader of (`unwelcome` 19, `violated` 14, `purview` 21, `divergence` 18,
   in OBS §2's order; `distance` and `watch` are already landed in B12 and are not added again), new
   `verb_capability` rows (`evade / defy: tradecraft` keyed by mode is not expressible — use `tradecraft`
   for both and let `defy` read `argue` through a `capability_by_mode` sub-map, `[ASSUMPTION]`; the home of
   a verb's skill moves to the row's `capability:` cell at CAP A2/A3, D-U1-07), new kinds
   (`compliance.failed`, `compliance.yielded`, `record.given.protested`) in `EMITTED_KINDS` via the rows.
2. `data/fixtures.py`: `unwelcome_step`, `violated_step`, `divergence_step`, each with a control 0 and a
   NUMBER row in `hole_register.yaml` (`purview` reads `purview_reaches`, a 0/1 term, at the composer's
   step). *(W3-4a: `delivery_weight` is deleted, C3-L10; `distance_ob` and `witness_step` are the one
   fixtures `distance_step` and `watch_step`, landed in B12.)*
3. `verb_table.yaml`: rows `give`, `comply`, `evade / defy`, `covenant` made Degree-keyed and `contests:`
   (`comply`: `"a task"`; the others' prizes per VRES §2's roster: `give` and `defy` have a person opposite,
   `"a standing"`; `evade` and `covenant`'s drafting have none, `"a task"` `[ASSUMPTION: the prize per row
   — basis: VRES §2's rule, one prize row per (who hears, when fought)]`); `give` gains `writes`/`emits`
   per band as §1; notes cite this file.
4. `queries/world_q.py`: `served`, `covenant_in_force` (new); `issuing_seat` exists (`:1573`).
5. `state/gate.py::purview_reaches`: the `OBEYED_WRIT` skip beside `DETERMINED_BY`.
6. `loop/effects_governance.py`: `_eff_comply`, `_eff_evade_defy`; `loop/effects_information.py::_eff_give`
   reads `res.degree` (declines at Failure → the row's Failure emits) and `_eff_covenant` writes `force`.
7. `seam/wrappers/sigma.py::contest_input`: the new operands, from the row and the counterparty's side.
8. `decision/options.py`: the `delivery_sourced` occasion. (`decision/choose.py` is not edited, C3-L10.)

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
not move when `violated` or `unwelcome` moves (the state is not setting the odds). A `compliance.withheld`
claim deposited before its stage's due tick, or a `Record.stages` write at MATTER (C3-C7). Control: all
new fixtures 0 and `delivery_sourced: []` reproduce S1-A's hash except for the draws the rows now take;
that difference is the declared mover.

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
