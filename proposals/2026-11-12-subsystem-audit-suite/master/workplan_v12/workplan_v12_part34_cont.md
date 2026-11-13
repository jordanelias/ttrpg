# Workplan v12 — part 34, continued: B32-inst-kit from B32.22; B37p-wr-kin-and-life

## Status: PROPOSED (continuation of `workplan_v12_part34.md`, author lane A34; renumbered by the orchestrator after all authors return; resolves nothing at runtime, CLAUDE.md §0.05)

Short names and paths are the head of `workplan_v12_part34.md`'s. The batch block of B32 (its gates, C, dials, UNDECIDED and position table) is in that file; this file carries B32.22 to B32.99, the batch's serial edges and file census, its boundary row, and the whole of B37p.

---

### B32.22 — one convening per seat · BIND_B commit B1 · BUILD · HASH MOVER(behaviour)
- SOURCE: BIND_B "Exact edits" commit B1 (edit 1), "Gate" B1, "Falsifier" B1; rulings A-63, A-64 (a sitting occupies its parties, read by `28_CORE_scene_access_*`, nothing added here).
- ADVANCES: R-04.a (`convene`).
- INSTRUCTION: "`loop/effects_governance.py::_eff_convene`: `did = H(w.world_seed, w.tick, a.actor, f"convene:{a.via or '-'}:{venue or '-'}")`. Docstring: the G4 paragraph's *"a SECOND identical convening by the same person at the same venue"* gains *"through the same seat"*."
- WHERE: `engine/season/loop/effects_governance.py` (`_eff_convene`); NEW `engine/season/tests/test_vb_b_sittings.py`.
- TESTS: `test_vb_b_sittings.py::test_b1_two_seats_two_sittings` (one person convening one venue through two seats in one tick makes two Dates) `[ASSUMPTION: name; BIND_B: "one function per gate B1–B4"]`; red before.
- FALSIFIER and CONTROL: "B1: revert the salt: the collision returns." Control: one convening through one seat unchanged.
- GATE: `python -m pytest engine/season/tests/test_vb_b_sittings.py -q` → pass; "`aperture 2 1` realm: `convene.refused` 1 → 0, `date.scheduled` 12 → 13, the new Date's `holder` `off_king`" (the source's numbers at its tree; quoted before (`reading @<B32.21 sha>`) and after, UNDECIDED 10).
- HASH MOVERS: "moves only where the collision occurs (one act at seed 1 realm in two seasons)". Re-pinned at B32.99.
- DEPENDS ON: EXISTS-IN-TREE `loop/effects_governance.py::_eff_convene`; V12 Batch B27 (the room).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.22`, `[skip ci]`.

### B32.23 — `convene` asks purview over the venue; no past date · H-278 (with H-297's remainder) · BUILD · HASH MOVER(behaviour)
- SOURCE: the intake `:286-288` (H-278, B32-inst-kit, "FA lane, B32 after B09; CF-E8-3"); `master/eval/E8.md` CF-E8-3 (`:183-217`): INSTRUCTION (H-278), WHERE, FALSIFIER, GATE, Hash movers; E8 `:89` (H-297: "the two remaining sub-claims (purview over the venue, a past date accepted) are … folded into H-278's item"); closes H-278 and H-297's remainder. Placed after B32.22 by its own text (§5.6: "`14_VERBS_BINDING_B_sittings.md` edits `_eff_convene`").
- ADVANCES: R-04.a (`convene`: a convening is now within the convener's seat's reach).
- INSTRUCTION (E8, copied): "in `loop/predicates.py::_req_convene` add one conjunct after the ordinal: the convener's exercised seat reaches the venue (`state/gate.py::purview_reaches`, the owner the establish path already asks through `founds_over`), routed through `_refuse("purview", ...)` once B09 lands, and refuse a date earlier than `w.tick` at `_eff_convene`'s precondition (the H-297 past-date remainder)". The register rows H-278 (and H-297's remainder in H-278's text) are closed in this commit, pointing at `_req_convene`.
- WHERE: `engine/season/loop/predicates.py` (`_req_convene`); `engine/season/loop/effects_governance.py` (`_eff_convene`'s precondition); `engine/season/hole_register.yaml` (H-278); `engine/season/tests/test_vb_b_sittings.py`.
- TESTS: (E8's falsifier, as tests, red before) `test_convene_at_another_duchy_refused_purview` ("a scope-D duke's `convene` at another duchy is refused with the purview clause named"), `test_past_dated_convene_refused`, and the positive control `test_lawful_convene_executes` `[ASSUMPTION: names]`.
- FALSIFIER and CONTROL: the two plants above reading admitted. Control: "A positive control for each (the lawful act still executes)".
- GATE: `python -m pytest engine/season/tests/test_vb_b_sittings.py -q` → the three tests above pass (with the file's earlier test); "`python -m engine.season.harness.aperture 2 0` before and after for H-278 (the `convene` executed count and the new refusal reading named)", quoted.
- HASH MOVERS: "H-278 declared (convening by a seat with no purview over the venue is refused where the realm executed it: `06_FA_remit_grant_by_row.md:33` records `convene` executed by `p_npc_032`)". Re-pinned at B32.99.
- DEPENDS ON: V12 B32.22; V12 Batch B09 (`01_CORE_predicates_name_their_clause`: `_refuse`); EXISTS-IN-TREE `loop/predicates.py::_req_convene`, `state/gate.py::purview_reaches`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high` (E8: tier sonnet).
- LANDS IT: B32's producer; `Item: B32.23`, `[skip ci]`.

### B32.24 — `determine` forms only on a party before the bench · BIND_B commit B2 · BUILD · HASH MOVER(behaviour)
- SOURCE: BIND_B "Exact edits" commit B2 (edits 2–5), "Gate" B2, "Falsifier" B2; "The resolution, decided" (CR-56's RL2 caution).
- ADVANCES: R-04.a (`determine`); `BUILT OUT`: `determine`.
- INSTRUCTION:
  1. "`data/verbs.py`: `PARTY_CLASS = "Party"`, checked against `REFERENT_CLASSES` as `DETAINEE_CLASS` is."
  2. "`rosters.yaml: referent_classes`: add `Party`; note: *"`Party` (VB-B): a person on the docket of a fired sitting before the asker's bench (`world_q.sittings_before`); stamped explicitly; `determine` declares it."*"
  3. "`queries/world_q.py`: `parties_before(w, p) -> tuple`: the persons in the matters of `sittings_before(w, p)`, in docket order, deduplicated. `questions_for`: append `((m, PARTY_CLASS) for m in parties_before(w, p))` to the classed tuple."
  4. "`verb_table.yaml`, `determine`: `referent_class: Party`, with a `referent_class_note` naming VB-B and its revert (delete the column). The typed cell is unchanged: `party` and `docket` stay conjuncts (the fold's check against the world it left; a matter disposed earlier in the lap still refuses)."
- WHERE: `engine/season/data/verbs.py` (`PARTY_CLASS`); `engine/season/rosters.yaml` (`referent_classes`); `engine/season/queries/world_q.py` (NEW `parties_before`; `questions_for`); `engine/season/verb_table.yaml` (`determine`).
- TESTS: `test_vb_b_sittings.py::test_b2_determine_forms_only_on_a_party` `[ASSUMPTION: name]`; red before.
- FALSIFIER and CONTROL: "B2: stamp every plain referent as `Party`: refusals at `party` return." Control: a docketed party at a fired sitting still forms.
- GATE: `python -m pytest engine/season/tests/test_vb_b_sittings.py::test_b2_determine_forms_only_on_a_party -q` → the test passes; "`aperture 2 0` and `2 1`: `determine.refused` keyed `party` and `docket` → 0; `matter.determined` not below 0/1. If executions fall (RL2's mode), the reading is recorded and B2 is held, not shipped" (a fall stops the item: HELD, and the batch close says so).
- HASH MOVERS: declared "where it bites" (every run in which `determine` formed on a non-party). Re-pinned at B32.99.
- DEPENDS ON: V12 B32.22; EXISTS-IN-TREE `queries/world_q.py::sittings_before`, `::questions_for`, `data/verbs.py::DETAINEE_CLASS`, `::REFERENT_CLASSES`; V12 Batch B24 (`05_SC_playable_hearing_B`: the `a verdict` row).
- GLOSSARY: row *party*: "a person on the docket of a sitting before the asker's bench" (the class `Party`).
- NAMES: "earlier in the round" → "earlier in the lap" (the source's sense is the season's pass; §5.10, B04).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.24`, `[skip ci]`.

### B32.25 — `pardon` forms only on a person restrained on the asker's seat · BIND_B commit B3 · BUILD · HASH MOVER(behaviour)
- SOURCE: BIND_B "Exact edits" commit B3 (edits 6–9), "Gate" B3 (with the R4 7b.3 addition), "Falsifier" B3.
- ADVANCES: `BUILT OUT`: `pardon` (with B32.26).
- INSTRUCTION:
  1. "`data/verbs.py`: `RESTRAINED_CLASS = "Restrained"`, checked as above."
  2. "`rosters.yaml: referent_classes`: add `Restrained`; note: *"`Restrained` (VB-B): a living person with a live restraint (`RESTRAINT_KINDS`) whose object is a seat the asker holds granting `determine`; `pardon` declares it. `Detainee` stays `detain`-only, for `interrogate`."*"
  3. "`queries/world_q.py`: `restrained_on_seats(w, p) -> tuple`, `detainees_held`' body with `t.kind in RESTRAINT_KINDS` for `t.kind == DETAIN_KIND`; `questions_for` appends its pairs to the classed tuple."
  4. "`verb_table.yaml`, `pardon`: `referent_class: Restrained`, note naming VB-B and the revert."
- WHERE: `engine/season/data/verbs.py` (`RESTRAINED_CLASS`); `engine/season/rosters.yaml` (`referent_classes`); `engine/season/queries/world_q.py` (NEW `restrained_on_seats`; `questions_for`); `engine/season/verb_table.yaml` (`pardon`).
- TESTS: `test_vb_b_sittings.py::test_b3_pardon_forms_only_on_the_restrained` and `::test_b3_pardon_through_a_seat_not_the_edge_object_refused` ("a `pardon` formed through a seat that is not the edge's object is refused at formation …; a new holder of that seat may pardon") `[ASSUMPTION: names]`; red before.
- FALSIFIER and CONTROL: "B3: widen `restrained_on_seats` to every person: refusals return. Stamp `Restrained` for a restraint whose object is another bench's seat: refusals return". Control: `interrogate`'s `Detainee` unchanged.
- GATE: `python -m pytest engine/season/tests/test_vb_b_sittings.py -q -k "test_b3_"` → the two tests pass; "`pardon` formed → 0 persons and `pardon.refused` → 0 while no restraint is live" (`aperture 2 0`, `2 1`), quoted.
- HASH MOVERS: declared where it bites (runs in which `pardon` formed on an unrestrained person). Re-pinned at B32.99.
- DEPENDS ON: V12 B32.24; EXISTS-IN-TREE `queries/world_q.py::detainees_held`, `::restrained`, `RESTRAINT_KINDS` `[ASSUMPTION: the constant's module; the producer greps it]`.
- GLOSSARY: row *restrained*: "held in custody or under a ban on a seat the asker holds" (the class `Restrained`).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.25`, `[skip ci]`.

### B32.26 — `pardon` is drawn · BIND_B commit B4 · BUILD · HASH MOVER(behaviour)
- SOURCE: BIND_B "Exact edits" commit B4 (edits 10–12), "Gate" B4, "Falsifier" B4, Standing line (A-6, A-7, A-8, A-30); the orchestrator's relay of A10's `contest_owed` (`workplan_v12_part10_cont2.md`, B07's UNDECIDED (1): "the owning authors' items … each delete their verb from `contest_owed`"); rulings A-37, A-81.
- ADVANCES: `BUILT OUT`: `pardon`.
- INSTRUCTION:
  1. Edit 10, "`verb_table.yaml`, `pardon`:"
     ```yaml
     contests:    "a matter"
     difficulty:  routine
     writes:
       Overwhelming: ["Tenure.until"]
       Success:      ["Tenure.until"]
       Partial:      ["Tenure.until"]
       Failure:      []
     emits:
       Overwhelming: ["detention.ended", "ban.ended"]
       Success:      ["detention.ended", "ban.ended"]
       Partial:      ["detention.ended"]
       Failure:      ["pardon.denied"]
     ```
     "`emits_on_refusal: ["pardon.refused"]` stays. The man pardoned is no opponent: the row declares no `counterparty` and SC-B's `opposition` term is absent." "**Durable write of the Failure band (A-81; C3-C11):** `pardon.denied` is witnessed by the bench (`judging_set`) and the restrained man where present, and deposits a claim of the denial to each". The draw key: "`H(w.world_seed, w.tick, <actor id>, "pardon.matter")` (A-30)".
  2. Edit 11, "`loop/effects_governance.py::_eff_pardon`: at `Partial`, close only the `detain` edges (a ban stands: commutation); else unchanged. `_RESTRAINT_ENDED` is read per band from the row's `emits` (the `Partial` list has one kind), so no kind is spelt in the effect."
  3. Edit 12, "`seam/wrappers/sigma.py::contest_input`: `stakes` keyed by the restraint kind being closed (the heaviest live one on the seat), `standard` from the arrangement that disposed it when the docket records it, else `plain`; `reception` over the seat's bench (`judging_set`)."
  4. `engine/season/rosters.yaml: contest_owed` (B07): delete `pardon` in this commit (the loader refuses a member that declares `contests:`).
- WHERE: `engine/season/verb_table.yaml` (`pardon`); `engine/season/loop/effects_governance.py` (`_eff_pardon`); `engine/season/seam/wrappers/sigma.py` (`contest_input`); `engine/season/rosters.yaml` (`contest_owed`: `pardon` removed); `engine/season/loop/witness.py` (the `pardon.denied` deposit, if WITNESS needs a reach row for the new kind; SITE).
- TESTS: `test_vb_b_sittings.py::test_b4_pardon_bands` ("hand-built world with one `detain` and one `ban` on a bench seat (the `interrogate` tests' fixture), 40 seeds: Partial ends the custody and keeps the ban; Failure ends nothing and emits `pardon.denied`; the act re-forms next scene"; `assert checked >= 40`); `::test_pardon_left_contest_owed` (`"pardon" not in CONTEST_OWED` and its row declares `contests:`) `[ASSUMPTION: names]`; red before.
- FALSIFIER and CONTROL: "B4: pin the roll: one band only." Control: the roll pinned to Success reproduces B32.25's frees.
- GATE: `python -m pytest engine/season/tests/test_vb_b_sittings.py -q` → pass; the 40-seed band table quoted (an `opus` read, BIND_B tier line).
- HASH MOVERS: every run in which a `pardon` resolves. Re-pinned at B32.99.
- DEPENDS ON: V12 B32.25; V12 Batch B05 (SC-B: `difficulty`, `stakes`, `standard`, `reception`), Batch B07 (`contest_owed`; `U5c_VERBS_residue` §2: `audience_of`), Batch B27 (`05_SC_acquittal`, `05_SC_arrangement_rows_that_bind`); EXISTS-IN-TREE `loop/effects_governance.py::_eff_pardon`, `seam/wrappers/sigma.py::contest_input`, `queries/world_q.py::judging_set`.
- GLOSSARY: none.
- COST and TIER: small build (one band-keyed row, one effect branch); `sonnet`, `high`; one `opus` read of the band table.
- LANDS IT: B32's producer; `Item: B32.26`, `[skip ci]`.

### B32.27 — the list kept by warrant: roster, tables, loader, `audit_at_exit` · VEN_C edits 1–3 · BUILD · HASH MOVER(encoding)
- SOURCE: VEN_C "The resolution, decided" §1, §4, "Exact edits, by owner" 1, 2, 3, "Gate" (Control); SYN_A §2 rows `tables.selection`, `tables.eligible_from`, `tables.cooling_off`, `binds_bases`; SYN_A §3 refusal row `audit_at_exit`; rulings A-13, A-24.
- ADVANCES: none of the nine.
- INSTRUCTION:
  1. "`engine/season/rosters.yaml`: `binds_bases.values: [members_by_admission, members_by_warrant]` with its note …; `tables.selection: {}`, `tables.eligible_from: {}`, `tables.cooling_off: {}` (empty at this edit). `conferral_bases` is **not** edited."
  2. "`engine/season/data/rosters.py`: the three tables' loader refuses a key that is no `offices.yaml` row; a `selection` value other than `lot`, or on a seat whose `conferral` is not `elected`; an `eligible_from` value that is no row id; a `cooling_off` value that is not a positive whole number, or on a seat whose row has no `term`. **`_load_offices`** admits `audit_at_exit` (and `binds`, if the loader does not already admit it on a row) and refuses one that is no `arrangements.yaml` id." The `audit_at_exit` row joins B32.06's key set.
  3. "`engine/season/state/carriers.py::Office`: one optional field, `audit_at_exit`". The source's "folded into the hashed representation only when not `None`" does not hold for a dataclass field: the field name enters `World.content_hash()` (`state/world.py::_object_head`; D-04), so the item is an encoding mover (UNDECIDED 3). `boot/realm.py` passes the row's value.
  4. Glossary: row *list* (a membership kept by warrant; *roll* rejected as the dice word, U1 glossary).
- WHERE: `engine/season/rosters.yaml` (`binds_bases`, `tables`); `engine/season/data/rosters.py` (the tables' loader; `_load_offices`); `engine/season/state/carriers.py` (`Office.audit_at_exit`); `engine/season/boot/realm.py` (the Office mint); NEW `engine/season/tests/test_inst_ven_c.py`; `unified/U1_GLOSSARY.md` (*list*).
- TESTS: in the new file, red before: `test_tables_refusals` and `test_audit_at_exit_must_name_an_arrangement` `[ASSUMPTION: names]`; `test_inst_syn_a_kit.py`'s falsifier: "An `Office` carrying a `patronage`, `eligible_from` or `cooling_off` field, or a `conferral_bases` carrying `lot`" fails.
- FALSIFIER and CONTROL: an `Office` field for a table; `lot` in `conferral_bases`. Control: act and Event tallies (`corpus_run --seasons 2` [v12: two seasons a case, D-17; the case's own span, to `MAX_SEASONS`, is B99's] seed 0, `headless --case NPC-088 --seasons 2 --seed 0`) equal B32.26's (an encoding mover's control is tallies-equal, D-04).
- GATE: `python -m pytest engine/season/tests/test_inst_ven_c.py engine/season/tests/test_inst_syn_a_kit.py -q` → pass; the seed-0 hash (`HASH READING`) moved, tallies equal (E-2).
- HASH MOVERS: every content hash, by encoding only (`Office` gains a field name). Declared; re-pinned at B32.99.
- EXPECTED RED UNTIL B32.99: the realm pins.
- DEPENDS ON: V12 B32.06, B32.19 (the `tables` family); V12 Batch B21 (`06_FA_seat_terms_and_turnover`, `_by_body_B`: the row `term:`); EXISTS-IN-TREE `state/carriers.py::Office`, `rosters.yaml: binds_bases`.
- GLOSSARY: *list* (step 4).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.27`, `[skip ci]`.

### B32.28 — `may_seat`, with `may_sit` its first conjunct; `selection_of` · VEN_C edit 4; PES_FA_B decision 1 · BUILD · HASH EQUAL
- SOURCE: VEN_C "The resolution, decided" §2, §4 (cooling-off), "Exact edits" 4; PES_FA_B "The resolution, decided" row 1 ("If VENICE-C's `may_seat(w, off, person)` lands first, this is its first conjunct and no second predicate is written"), "Lands it: … the `may_seat` conjunct form in B32"; U3 §4.1 row 73. One item: U3 lands VEN_C "with `16_PESSIMIST_FA_B`'s `may_seat` edit" (§5.5).
- ADVANCES: none of the nine.
- INSTRUCTION:
  1. "`engine/season/state/gate.py`: `may_seat` (reads `tables.eligible_from`, `tables.cooling_off`); `selection_of(off_id)`; no `FILLED_BY` change." `may_seat(w, off, person)`: "true when the table names no list for the seat, or the person holds a live `oblige` to the named seat"; false for "a person whose most recent `hold` on this seat closed by term maturity fewer than [`cooling_off`] ticks ago. Computed from the closed Tenure's `until`; stored nowhere."
  2. `may_sit` (landed in B21 by PES_FA_B edit 1) becomes `may_seat`'s first conjunct: `may_seat` returns False where `may_sit(w, person)` does; the callers B21 wired to `may_sit` (`tenure_write_basis`'s `conferral` and `claim` clauses, `_req_confer`, `_req_succeed`, the `confer` counterparty fan) ask `may_seat` where a seat is in hand and keep `may_sit` where only a person is (`_req_succeed` of the actor asks `may_seat(w, off, actor)`), so one predicate decides a seat's eligibility (PES_FA_B: "no second predicate is written").
- WHERE: `engine/season/state/gate.py` (NEW `may_seat`, NEW `selection_of`; `may_sit`'s callers); `engine/season/loop/predicates.py` (the callers named in step 2).
- TESTS: `test_inst_ven_c.py::test_may_seat_cooling_off_reads_until` (VEN_C's mutation: "`cooling_off` read against the hold's `since` instead of its `until`" reddens it) and `test_fa_eligibility.py::test_cohort_cannot_be_named_heir` (B21's G1, still green through `may_seat`) `[ASSUMPTION: first name]`; red before.
- FALSIFIER and CONTROL: a cohort seated through `may_seat`; the cooling-off read from `since`. Control: tables empty, every caller's answer equals B32.27's (hash equal).
- GATE: `python -m pytest engine/season/tests/test_inst_ven_c.py engine/season/tests/test_fa_eligibility.py -q` → pass; seed 0 hash equal to B32.27's after-reading.
- HASH MOVERS: none (tables empty).
- DEPENDS ON: V12 B32.27; V12 Batch B21 (`state/gate.py::may_sit`, PES_FA_B edit 1).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.28`, `[skip ci]`.

### B32.29 — the warrant clause and the eligibility ask · VEN_C edit 5 · BUILD · HASH EQUAL
- SOURCE: VEN_C "The resolution, decided" §1, "Exact edits" 5; SYN_A §1 row `warrant` (B32.02); rulings A-24.
- ADVANCES: none of the nine.
- INSTRUCTION: "`engine/season/loop/predicates.py`: `_req_oblige` gains the warrant clause for `members_by_warrant`; `_req_confer` asks `may_seat` for every seat but one `selection_of` reads as `lot` (where the effect asks it of each drawn name)." The clause (§1): "`_req_oblige` admits an `oblige` to a seat whose `binds` is that value only if the joiner **holds a `dispensation` whose `terms` is that seat and of which he is an addressee**, minted through that seat (the Record's rung is the seat's rung, as `_seat_rung` writes it)." "A member's `oblige` carries a term and lapses at MATTER unless the seat renews it" (the existing `oblige_term`; nothing new at MATTER).
- WHERE: `engine/season/loop/predicates.py` (`_req_oblige`, `_req_confer`).
- TESTS: `test_inst_ven_c.py::test_warrant_needed_to_join_a_list` `[ASSUMPTION: name]`; red before.
- FALSIFIER and CONTROL: an `oblige` to a `members_by_warrant` seat with no warrant admitted. Control: `members_by_admission` seats unchanged; hash equal (no row uses the value).
- GATE: `python -m pytest engine/season/tests/test_inst_ven_c.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 B32.28, B32.02 (`warrant`); EXISTS-IN-TREE `loop/predicates.py::_req_oblige`, `::_req_confer`.
- GLOSSARY: none (*warrant* is a plain word: a written authority).
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.29`, `[skip ci]`.

### B32.30 — the lot · VEN_C edit 6 · BUILD · HASH EQUAL
- SOURCE: VEN_C "The resolution, decided" §3, "Exact edits" 6, "Gate" (the spine fixture; the capture reading; entrenchment), "Falsifier"; Implementation block (draw key, Failure writes); rulings A-30, A-81, A-80.
- ADVANCES: none of the nine.
- INSTRUCTION: "`engine/season/loop/effects_governance.py::_eff_confer`: the `lot` branch, keyed draw as §3. `verb_table.yaml`, `confer` row: `emits` gains `lot.seen`, `lot.empty`." §3: "For a seat that `selection_of(off.id)` reads as `lot`, `_eff_confer` ignores the act's `to` and **draws** the conferee with `H(w.world_seed, w.tick, off.id, "confer.lot.<n>")` … uniformly from the persons for whom `may_seat` holds and who are present at the seat's rung or below it. A drawn person who is barred (… cooling-off; a live `ban` within the seat's purview) is *seen and not seated*: the act emits `lot.seen` naming him, and the draw repeats over the remainder; an empty bag leaves the seat vacant and emits `lot.empty`." Each is "witnessed by those present at the seat's rung and deposited to them (A-81)". The new kinds go at the end of `confer`'s list.
- WHERE: `engine/season/loop/effects_governance.py` (`_eff_confer`); `engine/season/verb_table.yaml` (`confer.emits`); `engine/season/tests/test_inst_ven_c.py`.
- TESTS: (red before) `test_rotating_council_two_seasons`: VEN_C's spine fixture ("a list seat (`members_by_warrant`) with eight enrolled persons; three council seats (`conferral: elected`, `tables.selection: lot`, `tables.eligible_from` the list seat, … `audit_at_exit: audit`); a presiding seat. Seeds 0–2 … Asserted: no holder is seated inside his cooling-off; no holder is off the list; the three seeds do not seat the same sequence"), written at two seasons with `term: 1` and `tables.cooling_off: 1` (twelve seasons with term 4 and cooling-off 4 in the source; A-114) `[ASSUMPTION: the fixture's term and cooling-off lowered so a rotation falls inside two seasons]`; `test_lot_keys_differ_for_two_seats_one_tick`; `test_lot_ignores_the_acts_to` ("the seated person differs from the act's `to` in at least one draw"). `audit_at_exit: audit` names B33's row: the fixture plants an `audit` arrangement row in its overlay until B33 lands it `[ASSUMPTION]`.
- FALSIFIER and CONTROL: "the lot ignoring `may_seat` seats a stranger"; "the lot reading the act's `to`"; "the lot keyed on the tick alone". Control: no shipped seat is `lot`; hash equal to B32.29's.
- GATE: `python -m pytest engine/season/tests/test_inst_ven_c.py -q` → pass; the per-seed council holders, `lot.seen` and `lot.empty` counts quoted (an `opus` read of the spine gate's output, VEN_C tier line); the capture reading and the entrenchment counts ("petitions, `tell`s and `evade / defy` aimed at the keeper's seat, by season") printed from the same fixture, reported not asserted.
- HASH MOVERS: none at this tree (no `lot` seat); each authored council row is a declared mover (B33's content).
- DEPENDS ON: V12 B32.29; V12 Batch B06 (the one draw owner `H`); EXISTS-IN-TREE `loop/effects_governance.py::_eff_confer`.
- GLOSSARY: row *lot* ("a seat filled by drawing a name from those eligible").
- COST and TIER: small build; `sonnet`, `high`; `opus` reads the spine output.
- LANDS IT: B32's producer; `Item: B32.30`, `[skip ci]`.

### B32.31 — the audit at exit, read when asked · VEN_C edit 7; SYN_A §4 `audits_due` · BUILD · HASH EQUAL
- SOURCE: VEN_C §4 ("`audit_at_exit` …"), "Exact edits" 7; SYN_A §4 row `audits_due` ("X-12: for each closed `hold` on a row carrying `audit_at_exit` whose `tenure.closed` claim `p` holds and over whose seat `p` may open …, the departed holder (`Party`) and the arrangement"); C3-C7.
- ADVANCES: none of the nine.
- INSTRUCTION: "`engine/season/queries/world_q.py::audits_due` (SYN-A §4) and `questions_for`: the `audit_at_exit` referent, computed when read. `loop/matter.py` is **not** edited (C3-C7)." The class is B32.24's `Party`. "**Nothing is docketed by the engine.** A person opens the case or does not."
- WHERE: `engine/season/queries/world_q.py` (NEW `audits_due`; `questions_for`).
- TESTS: `test_inst_ven_c.py::test_audit_due_on_any_close_for_those_who_heard` `[ASSUMPTION: name]`; red before.
- FALSIFIER and CONTROL: an audit stamped on a person with no `tenure.closed` claim; a stamp written at MATTER. Control: no row keyed `audit_at_exit`; hash equal to B32.30's.
- GATE: `python -m pytest engine/season/tests/test_inst_ven_c.py -q` → pass; VEN_C's control "content hash equal to the pre-item hash at build and at four seasons" read at two (A-114).
- HASH MOVERS: none.
- DEPENDS ON: V12 B32.30, B32.24 (`Party`), B32.27 (`Office.audit_at_exit`).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.31`, `[skip ci]`.

### B32.32 — the convening condition is read before a sitting fires · REST_2 W5 · BUILD · HASH MOVER(behaviour)
- SOURCE: REST_2 "W5 — the convening condition is read, or its key goes" (Problem, Resolution); "What it changes" W5; "Lands in batch: … W5 in B32"; U3 §4.1 row 85.
- ADVANCES: none of the nine.
- INSTRUCTION: (Resolution, copied) "The condition a sitting must meet is `15_INSTITUTIONS_PAPACY_B…`'s `quorum_share:` (or today's integer `quorum:`), read from the arrangement row the convening names. When that proposal lands: `_eff_convene` writes the row's condition under the key in place of `True`, and CALENDAR tests it against the bench present before `date.fired`; a Date whose condition fails emits nothing and stays due." PAP_B lands in this batch (B32.20), so the fallback (deleting the key) is not taken. The cell `(ConveningCondition, attached)` stays Layer 1's (`04` §A.2's `loop/calendar` row).
- WHERE: `engine/season/loop/effects_governance.py` (`_eff_convene`, the `convening_attached` write); `engine/season/loop/calendar.py` (the due-Date fire); NEW `engine/season/tests/test_convening_condition.py` `[ASSUMPTION: file and test names; E-3]`.
- TESTS: `test_a_date_below_its_condition_stays_due` (a Date whose row's `quorum` exceeds the bench present emits no `date.fired` and stays due), `test_a_date_meeting_its_condition_fires`; red before.
- FALSIFIER and CONTROL: a Date below its condition that fires; "Nothing reads the key" (`grep -n convening_attached engine/season` finds a reader after the edit). Control: a row with no `quorum` fires as today.
- GATE: `python -m pytest engine/season/tests/test_convening_condition.py -q` → the two tests pass; `aperture 2 0`: `date.fired` count before (`reading @<B32.31 sha>`) and after, quoted (the source measured the write 17 times in a three-season run at its tree).
- HASH MOVERS: every run in which a convened Date's bench falls below its row's condition. Declared; re-pinned at B32.99.
- DEPENDS ON: V12 B32.20 (`quorum_share`), B32.22 (`_eff_convene`); EXISTS-IN-TREE `loop/calendar.py`, `loop/effects_governance.py::_eff_convene` (`convening_attached`).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.32`, `[skip ci]`.

### B32.99 — re-pin and close readings · `V12_STRUCTURE_part4.md` E-1 · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2; `V12_STRUCTURE_part2.md` §5.9, §5.12; CLAUDE.md §7.
- ADVANCES: the batch's REQUIREMENT line (R-04.a: `determine`, `convene`; `BUILT OUT`: `determine`, `pardon`).
- INSTRUCTION: re-record, once, the realm and corpus pins in `engine/season/tests/_realm_goldens.py` at seeds 0 to 2 (build, one season, two seasons) against B27's close (`reading @<sha>`), and every test-local golden two items moved; write the R-04.a conjunct's `reading:` record in `engine/season/requirements.yaml` (`determine`, `convene` via-counts from `aperture 2 0`; `IS-A-12`), `status:` untouched; the commit says "re-pin" and lists the movers of the RE-PIN line.
- WHERE: `engine/season/tests/_realm_goldens.py`; `engine/season/requirements.yaml` (`reading:` only).
- TESTS: the full gates the BATCH GATE names, once (CLAUDE.md §0.4); no new test.
- FALSIFIER and CONTROL: a pin moved that no item declared; a behaviour tally moved where an item said EQUAL (B32.01 to B32.04, B32.06, B32.07, B32.09, B32.11, B32.15, B32.28 to B32.31). Control: B32.31's seed-0 hash equal to B32.30's.
- GATE: the BATCH GATE, read once.
- HASH MOVERS: the re-pin itself.
- DEPENDS ON: V12 B32.01 to B32.32 (B32.10 is BLOCKED and B32.18 a POINTER: no commit).
- GLOSSARY: the close reads every glossary row the items named against the code (`STAGES.md` rule 2).
- COST and TIER: reading; `sonnet` runs; the close's terminal critique `opus`.
- LANDS IT: B32's producer; `Item: B32.99`; the batch's last `Item:` commit, CI runs on its push.

## Readings (B32)
None: no position is a READING item.

SERIAL EDGES (B32): within the batch: B32.01 → B32.02 → B32.03 → B32.04 → B32.05 (registry, rows, kinds, readers, then the formation that offers forms); B32.03 → B32.08 (`resolution` with `recites`); B32.06 → B32.11 → B32.12 (a seat key needs the closed set; dignities need vacant rows) → B32.13 → B32.14 (`legitimacy` with `seat` from B32.07); B32.06 → B32.19 → B32.20, B32.21, B32.27 (the `tables` family) → B32.28 → B32.29 → B32.30 → B32.31; B32.22 → B32.23, B32.24 (both edit `_eff_convene`'s neighbourhood and `questions_for`) → B32.25 → B32.26; B32.24 → B32.31 (`Party`); B32.20 + B32.22 → B32.32; B32.99 last. Encoding mover B32.27 after every behaviour item whose source orders it earlier (none forces it later).
  With other batches: `contest_owed` B07 → B21 → B23 → B25 → B28 → B32 (each deletes its verb); `14_VERBS_SOCIAL1_B`'s `covenant_in_force` B28 ∥ B32 at S17 (UNDECIDED 1: no edge taken); PAP_A edit 5 → B21s (UNDECIDED 4); SYN_B gates 2, 4 → B39; SYN_B gate 5, SYN_A gates 3 (`comply`) and 4 → B33.
FILE CENSUS (B32; `→` is landing order, U3 §5.1 chains read in v12's order): `instruments.yaml`, `data/instruments.py` B32 (new) → B33 → B39 → B40; `rosters.yaml` (`record_kinds`, `choice_sourced`, `patronage_bases`, `revocation_bases`, `binds_bases`, `tables`, `referent_classes`, `contest_owed`) … B27 → B32 → B33; `offices.yaml` B21 → B21c → B32 → B33 → B40; `arrangements.yaml` B27 → B28 → B32 → B33 → B40; `data/arrangements.py` B27 → B32 → B40; `verb_table.yaml` (`determine`, `pardon`, `confer`) B28 → B32 → B33; `data/rosters.py` (`_load_offices`, tables) B21 → B32 → B33; `data/verbs.py` (`PARTY_CLASS`, `RESTRAINED_CLASS`) B28 → B32 → B38; `state/gate.py` (`may_fill`, `may_seat`, `selection_of`, `PATRONAGE_RULES`, `REVOCATION_RULES`) B28 → B32 → B33; `state/carriers.py` (`Office`) B21 → B32 → B34; `queries/world_q.py` (`instrument_of`…`breaches`, `in_force`, `owed`, `parties_before`, `restrained_on_seats`, `audits_due`, `questions_for`) B28 → B32 → B33 (B37p, same step, `questions_for`); `queries/person_q.py` (`legitimacy`, `kept`) B28 → B32 → B33; `loop/predicates.py` (`_req_confer`, `_req_oblige`, `_req_convene`) B25 → B32; `loop/effects_governance.py` (`_eff_confer`, `_eff_convene`, `_eff_pardon`) B28 → B32 → B33 (B37p, same step, `_eff_succeed`); `loop/effects_information.py` (`_mint_document`, the ballot tally) B28 → B32 → B33; `loop/calendar.py` B32; `seam/wrappers/sigma.py` (`contest_input`: `confer`, `succeed`, `revoke`, `pardon`) B28 → B32 → B33; `decision/options.py` (`operand_bags`) B28 → B32 → B33; `boot/realm.py` B25 → B32 → B33; `npcs.yaml` B32 → B37; `data/fixtures.py` (`presumption_gain`, `dignity_grades`) B28 → B32 → B33; `hole_register.yaml`, `requirements.yaml` (permanent surface).
PARALLEL (S17): with B11F2 (IN), B22 (MB), B26 (FI), B28 (SC), B37p (WR). Hot files shared, in different keys or functions (`V12_STRUCTURE_part3.md` §7.3; the coordinator checks the census at the step's open): `rosters.yaml`, `verb_table.yaml`, `world_q.py`, `data/fixtures.py`, `boot/realm.py` with all five; `witness.py`, `person_q.py`, `options.py`, `effects_information.py`, `arrangements.yaml`, `state/gate.py`, `sigma.py` with B28; `questions_for`, `state/gate.py` and `loop/effects_governance.py` with B37p (different functions but `questions_for`, which both splice: B32 merges first, slack 0, B37p rebases). B28's `covenant_in_force` is read by B32.04 (UNDECIDED 1). Merge order in S17 (`workplan_v12_part2.md` §3: B11F2, B22, B26, B28, B32, B37p): B32 rebases on B28's merge before B32.04 and re-pins once; B37p rebases on B32's (§7.4).

| STOP. Batch B32-inst-kit closes here |

---

## Batch B37p-wr-kin-and-life · lane WR · wave W17 · step S17 · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B37p-wr-kin-and-life
IN-FLIGHT ROW: registers/handoffs/HANDOFF_WR.md, Open table
GATE: Batch B12c-material-verbs-and-valley
GATE: Batch B37-happenings
HASH READING: `PYTHONHASHSEED=0 python -c "import sys; from engine.season.boot.realm import build_realm; from engine.season.harness.populated import run; s, k = int(sys.argv[1]), int(sys.argv[2]); w = build_realm(s); run(k, s, w=w); print(w.content_hash())" <s> <k>` → the realm content hash at seed `<s>` after `<k>` seasons: `<k>` = 1, one season, unless the gate names two (never more before B99, D-17); `<k>` = 0 reads the build hash; per item `<s>` = 0 (a mover's reading, E-2), at `.99` `<s>` = 0, 1, 2; each value quoted `reading @<sha>`, the tree it was read on (`workplan_v12.md` §3.B, "the hash reading").
REQUIREMENT: none — carried v11 positions (the intake `:363`, CP-T10-04, -06, -07, -09; `V12_STRUCTURE.md` §2.2: "carried v11 positions"); they serve A-15 (natural death makes estates), A-75 (kin for births and `marry`) and the world's no-player half (holdings follow kin; the wounded mend)
BATCH GATE (read once, on the closing tree, `PYTHONHASHSEED=0`):
  `python -m pytest engine/season/tests/test_kin.py engine/season/tests/test_deeds_to_me.py engine/season/tests/test_estate.py engine/season/tests/test_recovery.py engine/season/tests/test_season_shape.py -k "kin or estate or recovery or tend or wounded or bond" -q` → pass;
  the realm reading of CP-T10-07's LIMIT (AM-F-20), seeds 0 to 2, two seasons (four in the source; A-114): kin edges at build; `estates` entries written; `heir_of` non-empty; estate `succeed` formed / executed — "All zero is the expected base and is recorded as such" for the last two;
  the recovery reading (B37p.05's gate), seeds 0 to 2, two seasons: upward `condition.band_crossed` count and the `tend`-on-a-healed-man pair count (`wounded_with`'s docstring measurement), quoted;
  `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); `--requirements` → nine lines; `python tools/m1_acceptance.py --summary` → its verdict line quoted;
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names;
  the glossary rows named, read against the code;
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, and the batch's measured wall time; no conjunct is named, so no `reading:` record is written; `status:` is not edited (`IS-A-12`).
RE-PIN: once, in B37p.99: the realm and corpus pins in `engine/season/tests/_realm_goldens.py`, read against B37's close (`reading @<sha>`), or against B32's if B32 merged first in S17 (`V12_STRUCTURE_part3.md` §7.4); the commit says "re-pin: encoding (B37p.03 `World.estates`); behaviour (B37p.01 kin edges at build, B37p.02 `_bond`, B37p.04 `tend_share`, B37p.05 the rising arm and `body_mend` on)".
EXPECTED RED UNTIL B37p.99 (under `[skip ci]`, E-1; one batch line, repair lane R1): the realm and corpus pins any mover item of this batch moves read red from its first mover (B37p.01) to the re-pin; the files that pin them (`git grep -lE '"[0-9a-f]{32}"'` over the test trees and the golden files, those this batch names): `engine/season/tests/_realm_goldens.py` (B02's one pin file); `engine/season/tests/test_go07_canonical_digest.py` (its asserting test, `SHIPPED`/`CENSUS`).
IDS: ED-WR 0; H 2 (NUMBER rows of `recovery_step` (B37p.05) and `tend_share` (B37p.04))
DIALS AT CONTROL: none left at control: `body_mend` (shipped False by B12b.14, "This is CP-T10-04's ground") is set True by B37p.05, with `recovery_step` 50 and `tend_share` 0.5 (the card's `[ASSUMPTION]` values); target: CP-T10-04's falsifier readings (`test_recovery.py`) and the two-season realm reading of B37p.05's gate (A24's note: "set by B37p"; UNDECIDED 2).
UNDECIDED: (1) **CP-T10-06's kin channel is cut** (AM-F-01, E5 Block C30: "a sixth channel is a §C.6 Layer-1 row … the cut stands until a position builds the channel"); the card's falsifier arm "the Princess holds a `person.died` claim … source `told_by`" is dropped and the AM-F-01 arm taken. (2) **`body_mend`**: reading (a), taken: CP-T10-04 is a BUILD (the card ships the arm; "mover on the on arm"), so B37p.05 flips it; reading (b): ship the arm dormant and leave the flip to B98 with "target: none stated". (3) **Two rises for one body**: B12b.14 already adds a fed cohort's rise (`body_step × (2·ration − 1)` under `body_mend`) and the upward crossing (`_crossings`' body-row predicate); CP-T10-04 item 1's cohort half is therefore B12b.14's and is not written twice: B37p.05 adds the **named person's** arm (`recovery_step`, "a named person always (he does not eat)") under the same switch, and its cohort test reads B12b.14's step (one ladder per quantity, NERS S). (4) **An estate claim is `succeed`, which BIND_C made a draw** (B21): the estate arm rides the row as it stands (drawn); CP-T10-07's falsifier "her `succeed` on the Record opens her `hold`" is read with the roll pinned to Success. (5) CP-T10-09's card row ("narrowed: a live `kin` edge … counts as an ally in `_bond`; no new kinds") and AM-F-03 govern over the home's `patient_valence` design. (6) The recovery half of `U5d_WR_owed_edits` §3 (B12a.69 left it to CP-T10-04, H2_NOTES A20) lands in B37p.05.
C(B37p-wr-kin-and-life): this batch's entries; the plan's head parts; `master/eval/E1.md` CP-T10-04 (`:2459`), -06 (`:2162`), -07 (`:2203`), -09 (`:2256`); `master/eval/E5.md` Blocks C30, C31, C32, C34, C35 (`:501-566`); `proposals/U5d_WR_owed_edits.md` §3 and "Named tests" §3; `unified/U1_GLOSSARY.md` rows *kin*, *estate*, *heir*;
  `engine/season/rosters.yaml` (`tenure_kinds`, new `kin_roles`, `estate_object_kinds`, `estate_heir_order`); `engine/season/verb_table.yaml` (`release`'s `domain:`, `succeed`, `tend`); `references/npc_registry.yaml`; `engine/season/data/cast.py`; `engine/season/data/rosters.py`; `engine/season/data/verbs.py` (`RELEASABLE_KINDS`, the release-domain check); `engine/season/data/fixtures.py`;
  `engine/season/state/world.py` (`remove_person`, `_departed`, `_STATE_COLLECTIONS`, `content_hash`); `engine/season/state/gate.py` (the `inheritance` basis); `engine/season/queries/world_q.py` (`questions_for`, `larders_in_purview`, `places_named`, `wounded_with`); `engine/season/queries/person_q.py` (`_bond`, `regard`); `engine/season/loop/matter.py` (the body pass, `_crossings`); `engine/season/loop/effects_combat.py` (`_eff_tend`, `_eff_kill`, `body_observed`); `engine/season/loop/effects_governance.py` (`_eff_succeed`, `_eff_release`); `engine/season/loop/predicates.py` (`_req_succeed`); `engine/season/boot/realm.py`;
  the tests named; instruments `register`, `aperture`, `tools/m1_acceptance.py`, `tools/tests_for_diff.py`; `engine/season/tests/_realm_goldens.py`;
  the closing SHAs of B12c, B37 (and of B12b for B12b.14, B12a for B12a.69); the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, `registers/handoffs/HANDOFF_WR.md`, the skill and `methodology-close`).
SERIAL EDGES and FILE CENSUS: at the end of the batch.
PARALLEL: S17 with B11F2 (IN), B22 (MB), B26 (FI), B28 (SC), B32 (FA); files shared at the end of the batch.
COST: small builds; `sonnet`, `high`; no `opus` node (the cards' tier: "per home (Size line)").
EST: 5 h [estimate: 0.4 h × 6 positions + 2.5 h, E-15; §2.2's 4 h]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B37p.01 | kin: a releasable `kin` kind and its authored edges | CP-T10-06 (AM-F-01) | BUILD | MOVER(behaviour) | Batch B37, Batch B12c |
| B37p.02 | harm to a man's kin weighs on him as harm to himself | CP-T10-09 (AM-F-03) | BUILD | MOVER(behaviour) | B37p.01 |
| B37p.03 | an estate passes by its heir's claim | CP-T10-07 (AM-F-02, AM-F-20) | BUILD | MOVER(encoding) | B37p.01; Batch B21 (BIND_C `succeed`) |
| B37p.04 | `tend` heals a share of the headroom; its refusal names its clause | CP-T10-04 items 3, 4 | BUILD | MOVER(behaviour) | Batch B12a (B12a.69) |
| B37p.05 | the wounded mend over seasons, and the mend is seen | CP-T10-04 items 0–2 (AM-F-06); `U5d_WR_owed_edits` §3 (the recovery half) | BUILD | MOVER(behaviour) | B37p.04; Batch B12b (B12b.14, B12b.01) |
| B37p.99 | re-pin and close readings | `V12_STRUCTURE_part4.md` E-1 | BUILD | MOVER (the re-pin) | B37p.01 to B37p.05 |

Placement (§5.6): no member names these ids (the batch has no proposal members); each entry's own text orders it ("after CP-T10-06" for -07 and -09); the rest at the tail in the intake's order (-06, -07, -09, -04), -09 moved before -07 because it is one clause and -07 adds the batch's encoding mover, which goes last among the movers it does not depend on (`V12_STRUCTURE_part2.md` §5.9: EQUAL and smaller movers first where the source's order allows).

### B37p.01 — kin: a releasable `kin` kind and its authored edges · CP-T10-06 · BUILD · HASH MOVER(behaviour)
- SOURCE: the intake `:365` (CP-T10-06; carry-forward E1 `:2162`, E4 `:1815`, E5 Block C30); the home `2026-10-23-subsystem-completion-10-world-travel-survival-npc-life.md:265-292` as E1 copies it; AM-F-01 (E5 Block C30: the override); closes CP-T10-06.
- ADVANCES: none of the nine; the readers CP-T10-07 (B37p.03), CP-T10-09 (B37p.02), `marry` (CP-T10-08 is SUPERSEDED by `23_STORY_B`, B39).
- INSTRUCTION:
  1. "**A `kin` Tenure kind**: Person → Person, directed, its content from a `rosters.yaml: kin_roles` row `[spouse, parent, child, sibling]`, added to `tenure_kinds`." AM-F-01: "`kin` is a releasable kind. Add `kin` to `release`'s `domain:` (`verb_table.yaml`); `RELEASABLE_KINDS` derives it from `tenure_kinds` with no edit. Divorce or disowning is the owner's `release` of his own directed edge. It is one-sided: the releaser forfeits his claim on the other's estate, and hers stays live (`_eff_release` closes only edges whose subject is the actor)".
  2. "**Authored only from canon.** An optional `kin:` field on rows of `references/npc_registry.yaml` (`{to: NPC-nnn, as: <kin_role>}`), loaded by `data/cast.py` (which already raises on a malformed row) and minted by `harness/populated.py` beside the person. A row whose text states no relation gets none … only the Princess–Doux marriage is stated outright, so the rest are [UNVERIFIED] until a canon source is cited row by row." First step (SITE, §5.7): open the Princess's and the Doux Alexios Laskaris's rows in `references/npc_registry.yaml` and confirm both are built in the realm's cast; record in the commit body. If one is absent, the two `kin:` rows are still authored and the build edge test is planted in a test world `[ASSUMPTION]`.
  3. Item 3 (the `kin` witness channel, `kin_news_kinds`) "is cut from this item" (AM-F-01; UNDECIDED 1).
  4. Glossary: row *kin* ("a family tie: spouse, parent, child or sibling"); owner → `rosters.yaml: kin_roles`.
- WHERE: `engine/season/rosters.yaml` (`tenure_kinds`: `kin`; NEW `kin_roles`); `engine/season/verb_table.yaml` (`release.domain`); `references/npc_registry.yaml` (the Princess's and the Doux's `kin:`); `engine/season/data/cast.py` (the `kin:` field); `engine/season/boot/realm.py` (mint the edges beside the person); NEW `engine/season/tests/test_kin.py`; `unified/U1_GLOSSARY.md` (*kin*).
- TESTS: `test_kin.py` (red before): `test_princess_doux_two_kin_edges_at_build` ("the authored Princess–Doux pair gives two kin edges at build"); `test_kin_row_naming_an_absent_id_raises` ("A `kin:` row naming an absent id raises at load"); `test_release_of_a_spouse_edge_is_one_sided` (AM-F-01: "a `release` of a spouse edge closes it and leaves the other spouse's edge live").
- FALSIFIER and CONTROL: the three tests' plants. Control: "No `kin:` rows → no edges … → base hash."
- GATE: `python -m pytest engine/season/tests/test_kin.py -q` → pass; `python -c` loading `RELEASABLE_KINDS` → contains `kin`; seed 0 build hash moved (two edges), recorded.
- HASH MOVERS: "mover once rows are authored" (two edges at build). Re-pinned at B37p.99.
- EXPECTED RED UNTIL B37p.99: the realm pins.
- DEPENDS ON: EXISTS-IN-TREE `data/verbs.py` (the release-domain check), `data/rosters.py` (`RELEASABLE_KINDS`'s derivation), `data/cast.py`, `loop/effects_governance.py::_eff_release`; V12 Batch B03c (`boot/realm.py`); V12 Batch B37 (`22_HAPPENINGS_A`: births and ages, A-15).
- GLOSSARY: *kin* (step 4).
- NAMES: `harness/populated.py` → `boot/realm.py` (B03c).
- COST and TIER: small build (Size M); `sonnet`, `high`.
- LANDS IT: B37p's `valoria-author` producer, `isolation: worktree`; `Item: B37p.01`, `[skip ci]`.

### B37p.02 — harm to a man's kin weighs on him as harm to himself · CP-T10-09 · BUILD · HASH MOVER(behaviour)
- SOURCE: the intake `:367` (CP-T10-09; E1 `:2256`, E4 `:1887`, E5 Block C35); AM-F-03 (the override, E5 Block C35); the card row ("narrowed …; no new kinds"); closes CP-T10-09.
- ADVANCES: none of the nine.
- INSTRUCTION (AM-F-03, copied): "In `queries/person_q.py::_bond`, `a = 1.0` when `patient == p.id` or the patient is the object of a live `kin` edge in `p.tenures` (a Person carries every Tenure whose subject he is: `state/carriers.py`, read person-side at `decision/budget.py`); otherwise the stance ratio as today. One clause. `patient_valence` and `patient_gain` are not created, and the unpaired kinds (`body.tended`, `record.given`) are dropped from the item".
- WHERE: `engine/season/queries/person_q.py` (`_bond`); NEW `engine/season/tests/test_deeds_to_me.py`.
- TESTS: `test_deeds_to_me.py` (red before) `test_killing_his_sibling_weighs_as_harm_to_him` (the home's falsifier narrowed to the paired kinds: A kills B's sibling → B's regard of A falls as for a deed done to B himself; C, same pursuits and no kin edge, moves by the stance ratio only) `[ASSUMPTION: name and the narrowed reading — basis: AM-F-03 keeps death and wound, drops the unpaired kinds]`; mutation "key the term on the witness instead of the patient → C moves → red".
- FALSIFIER and CONTROL: the mutation. Control: no live kin edge → `_bond` as today.
- GATE: `python -m pytest engine/season/tests/test_deeds_to_me.py -q` → pass.
- HASH MOVERS: every run in which a person with a kin edge judges a death or wound of his kin. Re-pinned at B37p.99.
- DEPENDS ON: V12 B37p.01; EXISTS-IN-TREE `queries/person_q.py::_bond`, `::deeds_judged` (IN-58's pairing), `::regard`.
- GLOSSARY: none.
- COST and TIER: edit (Size S); `sonnet`, `high`.
- LANDS IT: B37p's producer; `Item: B37p.02`, `[skip ci]`.

### B37p.03 — an estate passes by its heir's claim · CP-T10-07 · BUILD · HASH MOVER(encoding)
- SOURCE: the intake `:366` (CP-T10-07; E1 `:2203`, E4 `:1835`, E5 Blocks C31, C32); the home's items 1–4 as E1 copies them; AM-F-02 (override), AM-F-20 (limit); closes CP-T10-07 for the record and the hand-built chain (AM-F-20: "not reported done for the live world until an estate `succeed` executes in a seeded run").
- ADVANCES: none of the nine.
- INSTRUCTION:
  1. AM-F-02: "`_estates` is renamed `World.estates`, declared in `World._STATE_COLLECTIONS`, written once inside `remove_person` beside the `_departed` line, value `(tick, sorted object ids)`, keyed by the dead man's id, never cleared and never rewritten. It is a new owner and says so. 'Unclaimed' is read, not stored: an object is claimable while `hold_force(obj)` is `None`." The objects are those of "his live `hold`s whose kind is in `estate_object_kinds`" (home item 1), recorded "before the dead man's own edges leave". "Nothing is deposited by it."
  2. "**`heir_of(w, dead, obj)`** in `queries/world_q.py`: the first living person, by a `rosters.yaml: estate_heir_order` row `[spouse, child, sibling, parent]`, among those who **own** a kin edge naming `dead` that closed at his death; ties by id. It reads heir-owned edges only".
  3. AM-F-02: "`estates_named(w, p)` offers an object only to `p == heir_of(w, dead, obj)` AND who holds a `person.died` claim naming `dead`, from any source (the `told` shape of `places_named`). The kin channel is cut (AM-F-01), so a far heir waits for a `tell`. … `estates_named` is one more term in `questions_for`'s `added` splice beside `larders_in_purview`".
  4. "**GV's `succeed`** … **accepts an estate object**, a Record or a Rung (a `rosters.yaml: estate_object_kinds` row `[Record, Rung]`), under the `inheritance` basis admitting exactly `heir_of` for an object in `w._estates[dead]` [now `w.estates`]. The act opens the claimant's `hold` in one write (`give`'s shape). Offices stay on IN-61's `successions` route; Propositions are excluded." The claim is drawn as every `succeed` is since B21 (UNDECIDED 4).
- WHERE: `engine/season/state/world.py` (`estates`, `_STATE_COLLECTIONS`, `remove_person`); `engine/season/queries/world_q.py` (NEW `heir_of`, NEW `estates_named`; `questions_for`); `engine/season/rosters.yaml` (NEW `estate_object_kinds`, `estate_heir_order`); `engine/season/state/gate.py` (the `inheritance` basis for an estate object); `engine/season/loop/predicates.py` (`_req_succeed`); `engine/season/loop/effects_governance.py` (`_eff_succeed`: the estate arm); NEW `engine/season/tests/test_estate.py`.
- TESTS: `test_estate.py` (red before), the home's falsifier with AM-F-02's gains: "a holder of a Record and a landholding dies far from his spouse; `w.estates` records both; she (and nobody else) is offered both [once she holds the `person.died` claim]; her `succeed` on the Record opens her `hold` [roll pinned to Success] and raises her `budget()` by 1; a person standing at the death holds the `person.died` claim but no claim naming the Record; a non-kin's claim is `succession.refused`; with a spouse and a child alive, the child's claim is refused"; "a hash difference between a world with a recorded estate and one without; the entry survives three ticks". Mutations: "`heir_of` ignores the order → the child is admitted → red; the estate objects ride the `person.died` Event's changes → the bystander holds a claim naming the Record → red".
- FALSIFIER and CONTROL: the mutations. Control: "`estate_object_kinds: []` → `_estates` is never written, no estate claim forms" (tallies equal to B37p.02's; the hash moves by the collection's name, D-04 `[ASSUMPTION: an empty collection in `_STATE_COLLECTIONS` enters the digest — basis: `content_hash` iterates the tuple; the producer reads the seed-0 hash before and after and records it]`).
- GATE: `python -m pytest engine/season/tests/test_estate.py engine/season/tests/test_in61_succession.py -q` → pass; AM-F-20's realm reading (seeds 0–2, two seasons; four in the source, A-114): kin edges at build, `estates` entries written, `heir_of` non-empty, estate `succeed` formed / executed, quoted ("All zero is the expected base").
- HASH MOVERS: every content hash by encoding (`World.estates` declared in `_STATE_COLLECTIONS`); behaviour where a holder of an estate object dies ("mover on the on arm"). Re-pinned at B37p.99.
- DEPENDS ON: V12 B37p.01; V12 Batch B21 (BIND_C's drawn `succeed`; IN-61 landed `f9e4cef`); EXISTS-IN-TREE `state/world.py::remove_person`, `::_departed`, `::_STATE_COLLECTIONS`, `queries/world_q.py::larders_in_purview`, `::places_named`, `::questions_for`; REM-21 (as amended, no registry: AM-F-02).
- GLOSSARY: rows *estate* ("what a dead man held that his heir may claim") and *heir* (the existing row: add the estate sense, owner `world_q.heir_of`).
- COST and TIER: small build (Size M); `sonnet`, `high`.
- LANDS IT: B37p's producer; `Item: B37p.03`, `[skip ci]`.

### B37p.04 — `tend` heals a share of the headroom; its refusal names its clause · CP-T10-04 items 3, 4 · BUILD · HASH MOVER(behaviour)
- SOURCE: the intake `:368` (CP-T10-04; E1 `:2459`, E4 `:1805`, E5 Block C34); the home's items 3, 4 and "Falsifier" (the `tend` arms); `loop/effects_combat.py`'s own revert note ("a swept fixture fraction of the headroom — #453's 'fast partial and slow full form', C-48").
- ADVANCES: none of the nine.
- INSTRUCTION: "**`tend` heals a share of the headroom** … fixture `tend_share` **[ASSUMPTION: 0.5]** of the headroom to `body_ceiling`." "**`tend.refused` keyed by clause** (dead or absent / not with / whole), on `migrate`'s keyed-refusal precedent." `tend_share` ships 0.5 with a NUMBER row (H block slot 2); "Control: … `tend_share` 1.0 → the behaviour of today". The Observation B12a.69 put on `_eff_tend` carries the new written body.
- WHERE: `engine/season/loop/effects_combat.py` (`_eff_tend`); `engine/season/data/fixtures.py` (`tend_share`); `engine/season/verb_table.yaml` (`tend`'s keyed `emits_on_refusal`); `engine/season/hole_register.yaml` (its row); NEW `engine/season/tests/test_recovery.py`.
- TESTS: `test_recovery.py` (red before): "`tend` at 250 with `body_ceiling` 1000 gives 625, and at 250 with `body_ceiling` 799 (a T03 mark) gives `250 + 0.5 × 549 = 524`, never 1000"; mutation "`tend` reads `condition_scale` instead of `body_ceiling` → the marked person rises past 799 → red"; `test_tend_refused_names_its_clause` `[ASSUMPTION: name]`.
- FALSIFIER and CONTROL: the mutation. Control: `tend_share` 1.0 reproduces B37p.03's tallies.
- GATE: `python -m pytest engine/season/tests/test_recovery.py engine/season/tests/test_season_shape.py -k "tend or wounded" -q` → pass (B12a.69's `test_a_witnessed_recovery_clears_a_believed_wound` still green).
- HASH MOVERS: every run with a `tend` that heals. Re-pinned at B37p.99.
- DEPENDS ON: EXISTS-IN-TREE `loop/effects_combat.py::_eff_tend`, `state/carriers.py::Person.body_ceiling` (CP-T03-07, landed: `effects_combat.py::CEILING`); V12 B12a.69 (the Observation on `_eff_tend`).
- GLOSSARY: none.
- IDS: H block slot 2.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B37p's producer; `Item: B37p.04`, `[skip ci]`.

### B37p.05 — the wounded mend over seasons, and the mend is seen · CP-T10-04 items 0–2; `U5d_WR_owed_edits` §3 (the recovery half) · BUILD · HASH MOVER(behaviour)
- SOURCE: the intake `:368` (CP-T10-04, "after `U5d_WR_owed_edits` §3"); the home's items 0, 1, 2, "Asymmetry", "Falsifier", "Control"; AM-F-06 (the needs cycle with CP-T03-07, resolved: CP-T03-07 landed); `proposals/U5d_WR_owed_edits.md` §3 ("`_eff_tend` and the recovery step write a `(pid, "body", v)` Observation as `_eff_kill` does") with "Named tests" §3; `workplan_v12_part20.md` B12a.69 step 1 (the recovery half owed here); `workplan_v12_part24.md` B12b.14 (`body_mend`, the cohort rise, the upward predicate); closes CP-T10-04, F-WR-23's recovery half, H-211 with B12b.14.
- ADVANCES: none of the nine; "the wounded mend over seasons, and the mend is news".
- INSTRUCTION:
  1. Item 0: "Every rise here — this arm and `tend` — heals toward the person's `body_ceiling` …, or toward `condition_scale` where no ceiling is set. … So this arm never heals a mark away."
  2. Item 1 (the named-person half; the cohort half is B12b.14's, UNDECIDED 3): "a living person below his `body_ceiling` who is not short this season gains `recovery_step` **[ASSUMPTION: 50 a season]**, capped at the ceiling. … a named person always (he does not eat)", in MATTER's body pass beside B12b.14's ration step, read under the same `body_mend` switch; `recovery_step` with a NUMBER row (H block slot 1).
  3. Item 2 ("Upward crossings … `_crossings` gains `before < floor <= after`") is B12b.14's: the named arm's write is passed to the same predicate (no second predicate).
  4. `U5d_WR_owed_edits` §3's recovery half: the rising write (both halves of the body pass that raise `Person.body`) writes a `(pid, "body", v)` Observation "as `_eff_kill` does", `v` the mended body, "so a witness's claim of the wound is superseded by a claim of the mended body"; `wounded_with`'s docstring line "MATTER's recovery does not yet" (B12a.69) is struck.
  5. `data/fixtures.py: body_mend` False → True (UNDECIDED 2; the dial A24 named for B37p).
- WHERE: `engine/season/loop/matter.py` (the body pass: the named arm, the Observation on the rising write); `engine/season/data/fixtures.py` (`recovery_step`, `body_mend`); `engine/season/queries/world_q.py` (`wounded_with`'s docstring); `engine/season/hole_register.yaml` (`recovery_step`'s row); `engine/season/tests/test_recovery.py`; `engine/season/tests/test_season_shape.py`.
- TESTS: in `test_recovery.py` (red before): "a fed cohort at 450 rises 50 a season and crosses `limited` (500) upward once, emitting one `condition.band_crossed` (MW-11 green); a short cohort does not rise" (read through B12b.14's step: the expected rise is that step's at a full ration, and the test asserts the crossing; `[ASSUMPTION: the 50 is the card's figure for `recovery_step`; the cohort reads `body_step`]`); "a marked person at 799 gains nothing from the rising arm"; mutations "the rising write lands on a copy → `budget()` unchanged → red"; "the arm … reads `condition_scale` instead of `body_ceiling` → the marked person rises past 799 → red". In `test_season_shape.py`: `test_a_witnessed_mend_at_matter_clears_a_believed_wound` (U5d_WR §3's test, on MATTER's write) `[ASSUMPTION: name — basis: B12a.69 took the source's name for the `tend` half]`.
- FALSIFIER and CONTROL: the mutations; "A `NoOpReceipt` refusal of `tend` on a man a witness saw mended" (U5d_WR §3). Control: `body_mend` False → B37p.04's hash (B12b.14's control: "no rise, no upward crossing"); "the per-season count of downward site crossings is unchanged" (H-211's control).
- GATE: `python -m pytest engine/season/tests/test_recovery.py engine/season/tests/test_season_shape.py -k "recovery or wounded or tend" engine/season/tests/test_hunger.py -q` → pass; seeds 0 to 2, two seasons: upward `condition.band_crossed` on bodies and "the docstring's measurement re-run (pairs forming `tend` on a healed man)" before (`reading @<B37p.04 sha>`) and after, quoted; the second "reads 0 after a recovery is witnessed".
- HASH MOVERS: every run in which a body rises or a mend is witnessed ("the on arm is also an outcome mover"; "Every run with a `tend`"). Re-pinned at B37p.99.
- DEPENDS ON: V12 B37p.04; V12 B12b.14 (`body_mend`, the cohort step, the upward predicate), B12b.01 (CP-T10-03's `season_terms`, the card's dependency), B12a.69 (the `_eff_tend` Observation and `wounded_with`'s docstring); EXISTS-IN-TREE `loop/matter.py::_crossings`, `loop/effects_combat.py::body_observed`, `::_eff_kill`, `state/carriers.py::Person.body_ceiling`; REM-29, REM-44 (landed `4ffddcdeb`; REM-29 not opened by this lane).
- GLOSSARY: none.
- IDS: H block slot 1.
- COST and TIER: small build (Size M); `sonnet`, `high`.
- LANDS IT: B37p's producer; `Item: B37p.05`, `[skip ci]`.

### B37p.99 — re-pin and close readings · `V12_STRUCTURE_part4.md` E-1 · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2; `V12_STRUCTURE_part2.md` §5.9, §5.12; CLAUDE.md §7.
- ADVANCES: none of the nine (the batch's REQUIREMENT line names no conjunct); the batch's one re-pin.
- INSTRUCTION: re-record, once, the realm and corpus pins in `engine/season/tests/_realm_goldens.py` at seeds 0 to 2 (build, one and two seasons) against the RE-PIN line's baseline; the commit says "re-pin" and lists the movers; no `requirements.yaml` record (no conjunct named).
- WHERE: `engine/season/tests/_realm_goldens.py`.
- TESTS: the full gates the BATCH GATE names, once (CLAUDE.md §0.4); no new test.
- FALSIFIER and CONTROL: a pin moved that no item declared. Control: no item here is hash EQUAL, so the control is the RE-PIN line's list: every mover it names moved a pin, and nothing else did.
- GATE: the BATCH GATE, read once.
- HASH MOVERS: the re-pin itself.
- DEPENDS ON: V12 B37p.01 to B37p.05.
- GLOSSARY: the close reads the rows *kin*, *estate*, *heir* against the code (`STAGES.md` rule 2).
- COST and TIER: reading; `sonnet` runs; the close's terminal critique `opus`.
- LANDS IT: B37p's producer; `Item: B37p.99`; the batch's last `Item:` commit.

## Readings (B37p)
None.

SERIAL EDGES (B37p): B37p.01 → B37p.02 (`_bond` reads the kin edge) → B37p.03 (`heir_of` reads kin edges; the encoding mover after the behaviour items); B37p.04 → B37p.05 (`tend_share` and the rising arm share `body_ceiling`'s reading and `test_recovery.py`); B37p.99 last. With other batches: `loop/matter.py` body pass B12a → B12b (B12b.14) → B37p; `loop/effects_combat.py::_eff_tend` B12a (B12a.69) → B12b → B37p; `questions_for` B32 → B37p in S17 (B32 merges first).
FILE CENSUS (B37p): `rosters.yaml` (`tenure_kinds`, `kin_roles`, `estate_object_kinds`, `estate_heir_order`) B37 → B37p → B38; `verb_table.yaml` (`release`, `tend`, `succeed`) B37 → B37p → B38; `references/npc_registry.yaml` B37 → B37p → B38; `data/cast.py` B10 → B37p; `state/world.py` (`estates`, `remove_person`) B37 → B37p; `state/gate.py` (`inheritance` basis) B32 → B37p; `queries/world_q.py` (`heir_of`, `estates_named`, `questions_for`, `wounded_with`) B32 → B37p → B38; `queries/person_q.py` (`_bond`) B32 → B37p → B38; `loop/matter.py` B12b → B37 → B37p → B39; `loop/effects_combat.py` (`_eff_tend`) B12b → B37p; `loop/effects_governance.py` (`_eff_succeed`) B32 → B37p → B39; `loop/predicates.py` (`_req_succeed`) B32 → B37p; `data/fixtures.py` (`tend_share`, `recovery_step`, `body_mend`) B37 → B37p → B38; `boot/realm.py` B37 → B37p → B38.
PARALLEL (S17): with B11F2 (IN), B22 (MB), B26 (FI), B28 (SC), B32 (FA). Shared with B32: `questions_for`, `state/gate.py`, `loop/effects_governance.py`, `loop/predicates.py`, `rosters.yaml`, `verb_table.yaml`, `data/fixtures.py`, `boot/realm.py`, `person_q.py` (different functions or keys; B32 merges first). With B37's successors in other lanes: none open. `loop/matter.py`: no other S17 batch edits it per U3 §5.1 (B22's `matter.py` edits, if any, checked by the coordinator).

| STOP. Batch B37p-wr-kin-and-life closes here |
