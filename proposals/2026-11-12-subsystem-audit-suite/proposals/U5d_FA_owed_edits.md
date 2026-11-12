# U5d-FA — owed edits: the FA resolutions decided "in this table" with no file, and the edits Jordan's answers now order

Reconciled: 2026-11-12, wave 3 (W3-3) — R3 §1: §2 takes the first form it offers (the gate scans live `detain` Tenures itself; no Query moves under `state/`), §4's datum is a table keyed by territory id, `rosters.yaml: tables.territory_weight` (U1 ledger F-12; a `weight:` key on a `Rung` would be a social aggregate on a Rung, `04` §B.3 "NEVER: any social aggregate"); §9's `[unverified]` `via` retention resolved at the tree (`world_q.issuing_seat`, `:1573`, reads the creating act's `via`), and R3's suggested route through the `handover` basis corrected at the tree (`handover` admits only a hold opened in the same write that ended the actor's own under T-m, `state/gate.py:212-218`; a successor is not the giver), so §9's opening has no admitting basis and is marked INCOMPLETE with the Layer 1 text it would need; U3 §6.2 (the scratch probes `pf1_static.py`, `pf5_heads.py` are restated as named tests, written first); U3 §4.1 rows 77–78 (§3 lands in B32, §10 in B39); tier (R3 7b-0).

## Status: PROPOSED (a plan for a later implementation lane; nothing here was executed)

Lands in batch: B21 (FA governance) for §1, §2, §4–§9 in C3-D5's order (§2 before `14_VERBS_BINDING_C`; the rest after `06_FA_levy_through_the_seat_B` and `16_PESSIMIST_FA_B`); §3 in B32 (with `15_INSTITUTIONS_PAPACY_B` item 4, cut edge §4.1 row 77); §10 in B39 (with `21_PROCEDURAL_B_cast_and_seats.md`, row 78).
Depends on: `14_VERBS_BINDING_C_turnover.md`, `14_VERBS_BINDING_D_orders.md`, `22_HAPPENINGS_B` (B21); `15_INSTITUTIONS_PAPACY_B` (B32, §3); `21_PROCEDURAL_B` (B39, §10); `06_FA_seat_terms_by_body_B.md` edit 4 (B21, the Löwenritter's `head_seat` for §3 and §8).

Author: U5d closure lane (Fable), 2026-11-12. Carries rows of `audits/06_FA_audit.md` §6.2 (R-05, R-07,
R-16, R-18, R-21), `audits/06_FA_audit_addendum_B.md` §B6.1 (R-27, R-29) and `audits/16_PESSIMIST_FA.md`
(F-PES-FA-02's detained officer, F-PES-FA-08, F-PES-FA-09, F-PES-FA-11), under
`unified/DECISIONS_ANSWERED.md` A-19, A-22, A-23, A-35, A-36 and A-42. Each section is one ordered,
executable item: owner, edit, gate, falsifier, movers, dependencies. Land order: §7 (no code), §10, §8, §9,
§2, §3, §1, §4, §6, §5.

## What it changes in `engine/season/` at runtime

§2: a person in custody forms no act through a seat. §3: a faction's head may strip an officer of that
faction, by a draw the officer may resist. §8: a person's opinion of a faction regards its present head.
§9: a writ stays with the seat when its holder changes. §1, §4, §5, §6, §7 change nothing at runtime in
their first commit (an ordering constraint, a reading, a deferred design, a deferred shape, register
text).

## §1 — the consort's remit lands with the deed race (R-16, F-PES-FA-11; A-19)

- **Edit.** None of its own. `06_FA_remit_grant_by_row.md` edit 1's `off_widow_regent: remit_acts: []`
  and `22_HAPPENINGS_B_the_throne_is_never_stranded.md` edits 1–3 (as reconciled to A-19) are one batch.
- **Gate.** `pf1_static.py` (the PES-FA lane's probe, `audits/16_PESSIMIST_FA.md` §7) is not in the
  repository (U3 §6.2); its reading is first written as a test in the file that covers `succeed`
  (`engine/season/tests/test_in61_succession.py`):
  `test_with_king_and_heir_removed_someone_may_claim_the_throne` (the built realm with King and heir
  removed by hand: at least one person may claim `off_king`).
- **Falsifier.** Zero eligible claimants in that world.
- **Movers.** The realm hash (the row's grant is hashed); declared in REMIT.

## §2 — custody suspends acts through the seat (A-23; F-PES-FA-02 "a detained officer governs")

- **Owner.** `engine/season/state/gate.py::_seat_grants` (`:370`), the first two conjuncts of every
  remit-act basis (`may_determine`, `may_warrant`, `may_seize`, `may_muster`), and the formation that
  mirrors it, `decision/options.py::seat_of` (`:694`).
- **Edit.** `_seat_grants` gains one conjunct: the actor is not in custody. The reader is
  `queries/world_q.py::restrained(w, person, kind)` (`:1766`); the gate may not import a Query, so the
  conjunct is written as the live-`detain` scan that reader performs, over the tenure store the gate
  already reads (R3 §1: the first form is taken; `04` §A.2's `state/gate` row reads the write matrix and
  the store, and no Query moves under `state/`). `seat_of` returns `None` for a detained holder, so no seat-gated
  candidate forms (formation follows admission). The seat-`hold` itself is untouched: custody suspends,
  it does not vacate.
- **Gate.** `engine/season/tests/test_in12_arrest.py` (one of the three files `grep -rl
  "_seat_grants\|may_determine" engine/season/tests` lists, with `test_in31_revocation_cost.py` and
  `test_u7_remit.py`; the arrest file is the custody owner's), new test
  `test_a_detained_holder_forms_and_is_admitted_no_act_through_his_seat`: one hand-built world, the same `issue`
  act admitted for a free holder and refused for the same holder under a live `detain`; released, it is
  admitted again.
- **Falsifier.** The detained arm executes; or the released arm still refuses; or the seat's `hold`
  closes.
- **Movers.** Any seeded run in which a detained seat-holder acted through his seat (`arrest` executed
  rarely: FA audit E-3 reads `arrest` formed 1, attempted 0, so the first reading is expected near zero;
  `[unverified]`, not run).
- **Depends on.** Nothing. Arrest becomes a political act (the ruling's own consequence): the reading to
  record after landing is the count of seat-gated acts suppressed per season.

## §3 — the head of a faction may strip an officer; nobody judges the Confessor (A-35, A-36; R-21)

- **Owner.** `engine/season/rosters.yaml: revocation_bases` and `state/gate.py::REVOCATION_RULES`; the
  rows in `offices.yaml`. The carrying text is `15_INSTITUTIONS_PAPACY_B_patronage_election_discipline.md`
  item 4, un-held by A-35 (see its `Reconciled:` line).
- **Edit.** As that item: the basis `head_of_faction` (the holder of the faction's `head_seat` may strip
  a seat of that faction); the Church officers' rows change `revocation: null → head_of_faction`.
  **`off_confessor` keeps `revocation: null`** (A-36) and gains a note: death or resignation only. The
  Löwenritter rows keep `null` until `06_FA_seat_terms_by_body_B.md` edit 4 gives them a `head_seat`. The
  strip is `revoke`'s contested row (`14_VERBS_BINDING_C_turnover.md`): the officer resists by the draw;
  a Failure is `revocation.resisted` and the seat stays.
- **Gate.** One hand-built world: the Confessor's `revoke` of a Cardinal reaches the roll and both a
  carried and a resisted band occur across the swept dice seeds; a Cardinal's `revoke` of the Confessor
  is refused at eligibility; the King's `revoke` of a Cardinal is refused.
- **Falsifier.** The strip succeeding in every seed (a fixed outcome); any seat stripping the Confessor.
- **Movers.** None at build (bases are read when a `revoke` is formed); every run in which a Church
  `revoke` then forms.
- **Depends on.** VB-C's drawn `revoke`.

## §4 — faction weight reads the authored franchise (R-29; A-41, A-42)

- **Owner.** `engine/season/queries/faction_q.py` (the view); the datum's owner is a table keyed by
  territory id, `engine/season/rosters.yaml: tables.territory_weight` (U1 ledger F-12), loaded and
  refused at import by `data/rosters.py` (a key that is no territory of the geography; a value that is not
  a positive number). No `Rung` field is added: a political weight on a Rung is a social aggregate, which
  `04` §B.3 bars from the Rung ("NEVER: any social aggregate"). An absent key reads 1.0.
- **Edit.** `faction_q.weight(w, f) -> float`: the summed `Person.weight` of members, each multiplied by
  the political weight of the territory he resides in (default 1.0; lowered for the southern Einhir
  territories; movable by good rule and caste reform, which are acts and not built here). No stored
  aggregate. First readers: instruments, then the councils and elections of the institutions kit
  (`15_INSTITUTIONS_VENICE_C_roll_lot_ballot.md`), where the weight sets a voter's draw (A-14), never a
  count. The numbers are content `[ASSUMPTION; Jordan to author]`; canon reach is noted (the Einhir).
- **Gate.** A reading: `faction_q.weight` for each rostered faction at `build_realm(0)`, printed by
  `harness/governance_spine.py`'s digest; with every weight 1.0 it equals the unweighted sum (control).
- **Falsifier.** A reader that gates an act on the weight, or a stored copy of it.
- **Movers.** None until a chooser term or a ballot reads it.

## §5 — what an order orders (R-27, F-FA-18, F-PES-FA-10)

- **Decision (the audit's, kept).** A closed set of term shapes, each performed by an existing verb
  through `rosters.yaml: terms_sourced`; the first shape is a demand of stores. Design-first.
- **Precondition, as an execution artifact.** `06_FA_shortest_loop_B.md`'s `loop_closed` reads
  `answered > 0` on the built realm at two dice seeds. Until then no shape is authored (a term nobody
  answers cannot be measured).
- **Owner when built.** `14_VERBS_BINDING_D_orders.md`'s `issue` row and `rosters.yaml: terms_sourced`.
- **Falsifier of the first shape.** A complied demand that moves no store.

## §6 — one purse per rung (R-07, H-352)

- **Decision (kept).** One store carrier (`Rung.stores`); a seat row may name `treasury: <rung>`,
  default its own rung. Built only when a computed `requisition` lands on a rung seating two factions.
- **Trigger reading.** `requisition.taken` Events whose rung carries seats of two factions, counted over
  realm seeds 0–2; today not read (the audit's E-5 counted Events, not rungs).
- **Owner when built.** `offices.yaml` row key and `state/carriers.py::Tenure.seat_rung`'s writer.

## §7 — register rows re-graded (R-05, H-91, H-144, R-18)

Text edits to `engine/season/hole_register.yaml` rows, made in the next FA commit, no code: H-91 closed
by precedent (every remit verb is admitted by grant and basis, `state/gate.py:370-375`); H-144 closed
(CR-25 option (b), `loop/predicates.py:403-410`); the plan card CP-T09-06 reads `null → inheritance`.
Gate: `python -m engine.season.harness.register --requirements` still loads.

## §8 — one head per faction (F-PES-FA-08)

- **Owner.** `engine/season/queries/world_q.py::opinion_of` (`:3029`).
- **Edit.** The "whom `p` regards on its behalf" clause reads `faction_q.head(w, faction)` first and
  falls back to the creed Proposition's subject.
- **Gate.** The PES-FA lane's `pf5_heads.py` is not in the repository (U3 §6.2); its reading is first
  written as `engine/season/tests/test_faction_q.py::test_after_a_succession_opinion_of_regards_the_successor`
  (hand-built: after a succession the successor is the regarded head).
- **Falsifier.** A dead leader still regarded as head after his seat is filled.
- **Movers.** The Restoration Movement and the Löwenritter at build once TERMS-B edit 4 lands; every
  faction after a succession. Declared.

## §9 — a writ is the seat's (F-PES-FA-09)

- **Owner.** `engine/season/loop/effects_governance.py::_eff_succeed`, `_eff_confer` (the seizure tail
  of `U5d_FA_land_and_seats_pass_on_a_won_march.md` edit 2 now opens no seat, so it passes no Record).
- **Edit.** When a seat-`hold` opens for a new holder, the live `hold`s on Records the previous holder
  made through that seat pass to him in the same write. Which Records: those for which
  `world_q.issuing_seat(w, rid)` (`queries/world_q.py:1573`: "the `via` of the Act that caused the
  Record's CREATING Event") names that seat; no field is added (the `[unverified]` is resolved).
- **INCOMPLETE: the write basis.** Closing the previous holder's `hold` on the Record and opening the
  successor's is a non-owner closure. R3 §1 suggested the existing `handover` basis; at the tree it admits
  only "a `hold` on something that is not a seat, opened in the same write that ended the actor's own
  live `hold` on it under `T-m`" (`state/gate.py:212-218`), and the successor is not the giver. When the
  previous holder died, his edges closed by `cascade`, and nothing admits the successor's opening. Two
  readings: (i) the writ stays unheld and the successor re-issues (no Layer 1 change; the finding stands
  as a residue); (ii) a new opening basis "a Record's `hold` follows the seat its minting act exercised",
  a §C.2 enumeration change, Layer 1 text owed to Jordan, not applied. Not built until one is chosen.
- **Gate.** Hand-built: the King issues a writ, dies, the heir claims; the heir holds the writ and may
  withdraw it.
- **Falsifier.** The Record left with no live holder.
- **Movers.** Runs with a succession after an `issue`. Declared.

## §10 — a seat exists whether or not it is filled (F-PES-GAME-13)

- **Owner.** `engine/season/harness/populated.py::build_realm` (`:1014`), where an `Office` is minted
  with its first holder (`:1740`, `:1801`).
- **Edit.** Every row of `offices.yaml: seats` is built as an `Office` at build, seated where its holder
  is in the cast and vacant where he is not (a cast cap, a generated cast that omits him, a death in the
  prologue). A vacant seat is offered by `world_q.vacancies` as any other.
- **Gate.** `build_realm(0, cap=0)` holds one `Office` per `offices.yaml` row and no seat-`hold` (the
  GAME pessimist's `x5_extremes.py 0 3` line reads `offices=0` today).
- **Falsifier.** A seat row with no `Office` in any built world.
- **Movers.** None at the shipped cast (every row has its holder); worlds built under a cap or by the
  generated cast (A-44) move, declared.
- **Depends on.** `21_PROCEDURAL_B_cast_and_seats.md` reads the same rows.

## NERS (E last)

N: each item is the only carrier of a ruled or decided point. R: arrest and discipline become political
moves; the Church gains internal politics while its head stays beyond judgment (A-36), which leaves
schism and violence as the answers to a bad Confessor. S: custody is one check at the one place every
seat-gated act already passes; the strip is `revoke`'s own row. E: nine short items, six with no new
apparatus.

## Cost class

Edits (§1, §2, §7, §8), small builds (§3, §4, §9 once its basis is chosen), design-first (§5), deferred
shape (§6). Tier: `sonnet` (R3 7b-0).
