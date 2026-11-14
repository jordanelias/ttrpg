# Workplan v12 — part 22, continued: Batch B24-sc-hearing, from B24.29

## Status: PROPOSED (the continuation of a body part of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

The batch block's head, its position table and items B24.01 to B24.28 are in `workplan_v12_part22.md`; words, paths and short names are that file's. This file holds B24.29 to B24.42, the batch's Readings, B24.99 and the boundary row.

---

### B24.29 — a reading of the bench, drawn, never revealed · HCAP edit 4 · BUILD · HASH EQUAL
- SOURCE: HCAP "Insight is a use, not a roll" (copied), "Exact edits" 4 (copied), gate 2, "Named tests"; A-11, A-30; `04` §B.2, AX-2.
- ADVANCES: R-04.c3 ("What a player sees": "what he sees of each seat's leaning is the claim WITNESS deposited in his own ledger with a confidence his `insight` sets, drawn and sometimes wrong").
- INSTRUCTION: the bench's reading, drawn and never revealed (HCAP edit 4's draw, with the probability replaced): at the turn view (`seam/wrappers/sigma.py::proceeding_input`, the site's one reader) every seat's public commits are shown; each seat's lean sign enters the viewer's ledger as a claim `(seat, leans, ±1)` deposited with a keyed draw `H(seed, tick, viewer, f"bench_read:{seat}")` (A-30). The chance that the deposited sign is the true one is `acc` of the viewer's reading (B24p.08: his Attunement and his `insight` rank against the seat's Grace), deposited by B24p.22's path. `bench_read_base`, `insight_gain` and the `bench_reading` uses row are not created (one reading, one ladder: CLAUDE.md §0.06 S); H slots 9 and 10 are returned. Gate 2 is read at Attunement 2 and 5. A wrong sign is possible at every Attunement.
- WHERE: `engine/season/seam/wrappers/sigma.py` (`proceeding_input`: the turn view's deposit); `engine/season/loop/witness.py` (the deposit path, if `proceeding_input` reaches WITNESS through it `[ASSUMPTION: the deposit's owner — basis: HCAP edit 4 "WITNESS's deposit"]`); `engine/season/tests/test_sc_hearing_capabilities.py`.
- TESTS: written first, red: `test_bench_reading_is_drawn_and_can_be_wrong_at_every_insight` (gate 2: "A hand-built sitting with one seat leaning against the player's party, over 400 seeds: the share of seats whose lean the viewer holds with the true sign is strictly between 0.5 and 1 at insight 2 and at 5, and higher at 5", read here at Attunement 2 and 5 (B24p.08's reading, no `insight_gain`); `assert checked >= 400`).
- FALSIFIER and CONTROL: "a turn view that shows any seat's true lean with certainty (share 1.0), or that reads a seat's lean from World rather than from the viewer's own claim" (HCAP). Control: "Hash EQUAL at the shipped cast (no holder)": realm hashes equal to B24.28's (the deposit is B24p.22's, `reading_kept` off at control).
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_sc_hearing_capabilities.py -q` → pass; realm hash (`HASH READING`) at seed 0 → equal.
- HASH MOVERS: "None at the shipped cast" (HCAP).
- DEPENDS ON: V12 B24.10 (`proceeding_input`), B24.13; V12 B24p.08 (the reading: `acc`), B24p.22 (the kept reading's deposit path); V12 Batch B04-capability-home (`insight` row); V12 Batch B06-keyed-draw (the A-30 keyed draw).
- IDS: none (H block slots 9, 10 are returned, unused: named at the expunge).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B24's producer; `Item: B24.29`, `[skip ci]`.

### B24.30 — a negotiation is the same sitting under a mutual row · NEG edits 1–4, with IS-B2-SC-03 step 4 · BUILD · HASH EQUAL
- SOURCE: NEG "The resolution, decided" 1–3 and "The end" (copied in part), "Exact edits" 1–4 (copied); `IS-B2-SC-03` step 4 ("A mutual row (`negotiation`) keeps `bench_basis: none`; its rite adds `offer` and `accept`"), placed here because B24.09's rite loader refuses a move that is not a roster member and `offer`, `accept` enter the roster in this commit (UNDECIDED (5)); A-21, A-81, R-29 as recorded; D-06.
- ADVANCES: R-04.c3 ("A negotiation is the same entry under a `disposal: mutual` row", `IS-B2` §1.0).
- INSTRUCTION:
  1. "`engine/season/rosters.yaml: proceeding_moves` — rows `offer`, `accept`, each with `rows: [mutual]` (the disposals under which a rite may list it)." `offer`: "needs: a term set the offerer can meet — an `oblige` term and, when `exchange`'s operands land, stores each side gives; no draw; the offer stands on the board, replacing his previous one"; `accept`: "needs: a standing offer of the other side; no draw; ends the sitting". `concede` on a mutual row "withdraws one of the conceder's own demands from his standing offer … and is witnessed". Neither carries a `capability:` (B24.04's refusal: draw-free). `offer` and `accept` are rows of `proceeding_moves` with effects `offer`, `accept`; under `mutual` nobody is balloted (B24p.12), so "skip the closing draw and the ballots" (step 3) is already the entry's behaviour; the rite row `mutual` is in B24p.03's map form and `negotiation` moves from `rite: contest` to it.
  2. "`engine/season/queries/inputs.py` — `ProceedingInput.closing: Optional[SocialContestInput]`; `ProceedingOutcome.accepted: Optional[tuple]`; an `Offer` record (`id`, `by`, `terms`, `stores`)." `Offer.stores` is `None` (the dormant form of `IS-B2-SC-06`, BLOCKED: "an offer carries an obligation term only").
  3. "`modules/social_contest/proceeding.py::proceed` — on `closing is None`, skip the closing draw and the ballots; apply `offer` and `accept`." "`argue` rolls as in a hearing; at Success or better the arguer's argued claim is deposited to the counterparty as a told claim … The roll changes what the other believes, never what he does."
  4. "`engine/season/seam/wrappers/sigma.py::proceeding_input` — for a mutual row, no seats and no closing."
  5. (`IS-B2-SC-03` step 4) `engine/season/arrangements.yaml`: a rite row `mutual` `[ASSUMPTION: the rite's id — basis: the `rows: [mutual]` key of step 1]` with `moves:` the default rite's party moves plus `offer` and `accept`, no `rule` or `adjourn` (no bench), `faults:` as `default`, `disclosed: true`, `bears: {}`; the `negotiation` row names `rite: mutual` and keeps `bench_basis: none`.
- WHERE: `engine/season/rosters.yaml` (`proceeding_moves` `offer`, `accept`); `engine/season/queries/inputs.py` (`ProceedingInput.closing`, `ProceedingOutcome.accepted`, `Offer`); `modules/social_contest/proceeding.py` (`proceed`); `engine/season/seam/wrappers/sigma.py` (`proceeding_input`); `engine/season/arrangements.yaml` (`rites: mutual`; `negotiation` `rite:`); NEW `engine/season/tests/test_sc_hearing_negotiation.py`.
- TESTS: written first, red: `test_two_npc_negotiation_auto_twice_same_hash` (gate 1, on a hand-built two-NPC sitting called through `proceed`; the `oblige` arm of gate 1 is read at B24.31); `test_a_held_breach_claim_changes_acceptance` (gate 2); `test_scripted_player_reproduces_auto_hash` (gate 3).
- FALSIFIER and CONTROL: "An agreement opened with no `accept` chosen by the accepter (consent decided by a draw). … An `argue` success that changes the outcome without changing a ledger" (NEG). Control: "At the control arm (`sitting_exchanges` 0) the seeded `negotiation` row is unchanged": realm hashes equal to B24.29's.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_sc_hearing_negotiation.py engine/season/tests/test_sc_hearing_sitting.py engine/season/tests/test_arrangements.py -q` → pass; realm hash (`HASH READING`) at seed 0 → equal.
- HASH MOVERS: "None at control (`sitting_exchanges` 0); declared when built" (NEG): no computed act opens a negotiation until B28 (`IS-B2-SC-05`).
- DEPENDS ON: V12 B24.03 to B24.13; V12 B24p.03 (`rites:` in the map form, `rite:`), B24p.12 (nobody is balloted under `mutual`); EXISTS-IN-TREE `arrangements.yaml: negotiation` (`disposal: mutual`, `disposes: oblige`, `order: alternating`, `bench_basis: none`). Not here: NEG edit 6 (the opening verb) is `IS-B2-SC-05` (Batch B28-social-verbs); `exchange`'s operands are `IS-B2-SC-06` (BLOCKED: SE names the act).
- GLOSSARY: row *negotiation* (or *mutual row*): "negotiation: a sitting with no bench in which each party offers terms and may accept the other's, as people bargain" (added if absent; owner `arrangements.yaml: negotiation`).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B24's producer; `Item: B24.30`, `[skip ci]`.

### B24.31 — each party's `oblige` is opened by his own act · NEG edit 5 · BUILD · HASH EQUAL
- SOURCE: NEG "Exact edits" 5 (copied), "The end", gate 1, named tests; C-07; `04` PART D row 10a; A-81.
- ADVANCES: R-04.c3.
- INSTRUCTION: "`engine/season/loop/effects_information.py` — on an `accepted` outcome, each party's `oblige` is written under that party's own act (the offerer's `offer`, the accepter's `accept`, each recorded as an `Act` with that party as actor and the sitting as its scene), and the `exchange` act likewise; their ordinary preconditions apply at MATTER of the same lap. The effect writes no edge under the opener's act." "All rest without acceptance: nothing is opened; the sitting's exchanges are still written to the case file and witnessed, so the failed negotiation leaves a durable write (A-81)." Until `IS-B2-SC-06` is unblocked no `exchange` act is formed (`Offer.stores` is `None`).
- WHERE: `engine/season/loop/effects_information.py` (the mutual-row branch of the hearing's effect).
- TESTS: written first, red: `test_each_oblige_is_opened_by_its_own_partys_act` (gate 1: "the `Act.actor` of each edge's opening act is the party it binds"); `test_a_negotiation_without_acceptance_still_writes_the_case_file` (A-81). `test_two_npc_negotiation_auto_twice_same_hash` stays green.
- FALSIFIER and CONTROL: "An `oblige` edge whose opening act's actor is not the party it binds. … A negotiation that ends with no acceptance and no write" (NEG). Control: realm hashes equal to B24.30's.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_sc_hearing_negotiation.py -q` → pass; realm hash (`HASH READING`) at seed 0 → equal.
- HASH MOVERS: none at control.
- DEPENDS ON: V12 B24.14 (the case-file write), B24.30; EXISTS-IN-TREE `verb_table.yaml: oblige` (`eligibility: own`).
- GLOSSARY: none.
- NAMES: "round" (NEG "for that round", the season's pass) → "lap" (B04, PCR-4).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B24's producer; `Item: B24.31`, `[skip ci]`.

### B24.32 — the ten checks that the kernel's mechanisms arrived · KERN_B "The ten checks" · BUILD · HASH EQUAL
- SOURCE: KERN_B "What is carried, where, and the check that shows it arrived" (the carry table) and "The ten checks, named" (copied); KERN_B edit 1 ("after the ten checks above pass"); its Falsifier ("If any of the ten checks cannot be written against `ProceedingOutcome` …, that mechanism was not carried and the deletion waits").
- ADVANCES: none of the nine by itself; the precondition of B24.33.
- INSTRUCTION: write each check not already written by an earlier item, each against `ProceedingOutcome` or `standing`, in `engine/season/tests/`:
  1. `test_sc_hearing_sitting.py::test_two_scripted_deciders_differing_in_one_move_leave_different_standing`;
  2. `test_sc_hearing_sitting.py::test_concede_descends_one_rung_and_is_witnessed`;
  3. `test_sc_hearing_evidence.py::test_an_off_rung_item_enters_at_half_and_a_same_origin_second_adds_less` (written at B24.19: confirm green);
  4. `test_sc_hearing_evidence.py::test_an_answer_strikes_by_its_band_in_a_share_strictly_between_0_and_1` with `::test_a_struck_item_adds_no_proofs_level` (B24.25, B24.20: confirm green);
  5. `test_sc_hearing_sitting.py::test_silence_adds_levels_only_where_the_row_lists_it`;
  6. `test_sc_hearing_sitting.py::test_swapping_bears_moves_the_closing_odds_over_200_seeds`;
  7. `test_sc_hearing_ballots.py::test_a_seat_can_vote_against_the_board`;
  8. `test_sc_hearing_ballots.py::test_a_trait_row_moves_one_seats_ballot_odds_only` — `Decider` carries `moved_by` (B24p.02), so a trait moves one seat's ballot odds through the `fit` source; UNDECIDED (6) is closed;
  9. `test_sc_hearing_sitting.py::test_an_attendee_at_effort_zero_makes_no_move`;
  10. `test_sc_hearing_shapes.py::test_four_run_shapes_from_hand_built_exchange_lists`, with "a reader of `ProceedingOutcome.exchanges` in the harness": `harness/governance_spine.py::run_shape(exchanges) -> str` returning one of `rout`, `reversal`, `collapse`, `split`. SITE: open `systems/social_contest/sim/contest/narrative.py::classify` (its `SHAPES`, the thresholds `NAIL_MARGIN`, `CLOSE_MARGIN`, `ROUT_MARGIN` and the rules for `ROUT`, `REVERSAL`, `COLLAPSE`, `SPLIT_DECISION`) before B24.33 deletes it, record the four rules in the commit body, and re-derive them over `Exchange` records (a fault-ended run is `collapse`; a ballot split against the board is `split`) — computed, stored nowhere;
  11. `test_sc_proceeding_data.py::test_the_rows_carried_from_the_kernel_load_and_run_a_sitting`: `rally`, `inquisition_hearing`, `excommunication_deliberation` and `audience` each load and `proceed` returns an outcome under them (RD §C.9): the deletion's falsifier now sees the catalogue (COL §4 item 6).
  Every over-seeds check asserts its count (`assert checked >= 200`).
- WHERE: `engine/season/tests/test_sc_hearing_sitting.py`, `test_sc_hearing_ballots.py`, `test_sc_proceeding_data.py` (B24p's; check 11); NEW `engine/season/tests/test_sc_hearing_shapes.py`; `engine/season/harness/governance_spine.py` (`run_shape`).
- TESTS: the ten checks above and check 11; each read green on this commit (the mechanisms landed at B24.06 to B24.31).
- FALSIFIER and CONTROL: KERN_B's: a check that cannot be written against `ProceedingOutcome`. Control: realm hashes equal to B24.31's (tests and a harness reader only).
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_sc_hearing_sitting.py engine/season/tests/test_sc_hearing_evidence.py engine/season/tests/test_sc_hearing_ballots.py engine/season/tests/test_sc_hearing_shapes.py -q` → the ten checks pass, and `engine/season/tests/test_sc_proceeding_data.py -q` → check 11 passes.
- HASH MOVERS: none.
- DEPENDS ON: V12 B24.06 to B24.31; V12 B24p.02, B24p.03 (the rows check 11 loads); EXISTS-IN-TREE `systems/social_contest/sim/contest/narrative.py::classify`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B24's producer; `Item: B24.32`, `[skip ci]`.

### B24.33 — the SC05 kernel retires; its game lives in the hearing · KERN_B edits 2, 4, 5 with SC-P2 edits 1–4, 6 (and `17_CENSUS_C1B_01`'s kernel item) · BUILD · HASH EQUAL
- SOURCE: KERN_B "The resolution, decided", "Exact edits" ("SC-P2's edits 1 to 6 stand … Changed or added: 1 … 5"), "Gate", "Falsifier"; `proposals/05_SC_sc05_kernel_retirement.md` "Exact edits" 1–6 (copied below); `17_CENSUS_C1B_01_deletions.md` (its kernel item: "the SC-05 kernel (75 rows) is `05_SC_sc05_kernel_disposition_B.md`", U3 §4.1 row 8: no edit of its own, its gate 1 is this gate); rulings `ED-SC-0033` clause 2 (RULED: *"orphaned social contest code: retire it"*), `ED-IN-0285`, `ED-SC-0013`.
- ADVANCES: none of the nine; one played path, one obstacle, one ballot, one evidence model (KERN_B's S).
- INSTRUCTION (each SC-P2 edit as KERN_B keeps it):
  1. "`git rm -r systems/social_contest/sim/contest/` (re-derive the set from `git ls-files`), and `systems/social_contest/sim/__init__.py` if nothing remains beneath it. Write the exact-file `FORK:` rows in `references/restructure_ledger.md`." (Sixteen files under `contest/` at `aa31fd2`; the `FORK:` sha is this batch's base, the last commit on the branch that carries them.)
  2. "Tests: delete `engine/tests/test_contest_kernel.py` (its subject is gone; `FORK:` row). `engine/tests/test_sigma_leverage_parity.py`, `tests/valoria/test_band_extension_seam.py` and `tests/valoria/test_degree_ladder_single_owner.py` replace `CONTEST_DEGREE_EXTENSION` with a local `BandExtension` double defined in the test (the seam's contract is what they assert)." (Line numbers dropped: B03a.)
  3. "`references/module_contracts.yaml` `module: social_contest`: `sim_module: modules/social_contest/`, `resolver: d10_sigma`, delete the `wiring.note` (the `persuasion_track` state row is already deleted, B24p.12; the rest stands); keep the row (the loop's prize rows key on the name)." KERN_B edit 2: the `social_contest.proceeding` composition row (B24.06) "is what the retiring `module: social_contest` row's `sim_module:` and `resolver:` describe after the repoint".
  4. "`engine/engine_params/sim_params.json`: re-derive with `python tools/export_sim_params.py --build` after the deletion; never hand-edit. Its `--check` is the gate."
  5. "`registers/handoffs/HANDOFF_SC.md`: the kernel row closes; `CURRENT.md`'s social contest row names `modules/social_contest/` as the head." (SC-P2 edit 6.)
  6. KERN_B edit 4: "`registers/editorial_ledger_sc.jsonl`: one row recording the table above for `ED-1056` to `ED-1062` (superseded for the kernel, with the two carried behaviours named)", id `ED-SC-<B24 block slot 1>`, `needs_jordan: false` (the ladder closed each, KERN_B's table).
  7. KERN_B edit 5: "`engine/season/hole_register.yaml` H-56: the held half is rewritten to *"not required by a hearing: its deciders are called out to at ENCOUNTER (`ED-IN-0349`); open only for a contest that would re-run DELIBERATE"*."
  Not carried: SC-P2 edit 5 and KERN_B edit 3 edit `workplans/valoria_master_workplan_v11_part5.md`, which v12's adoption deletes (`V12_STRUCTURE_part3.md` §8.1 step 4); UNDECIDED (7).
- WHERE: DELETE `systems/social_contest/sim/contest/` (every file `git ls-files` lists), `systems/social_contest/sim/__init__.py` (if empty beneath), `engine/tests/test_contest_kernel.py`; `engine/tests/test_sigma_leverage_parity.py`, `tests/valoria/test_band_extension_seam.py`, `tests/valoria/test_degree_ladder_single_owner.py` (the local double); `references/module_contracts.yaml` (`module: social_contest`); `engine/engine_params/sim_params.json` (re-derived); `references/restructure_ledger.md` (exact-file `FORK:` rows); `registers/handoffs/HANDOFF_SC.md`; `CURRENT.md` (the social contest row); `registers/editorial_ledger_sc.jsonl` (one row); `engine/season/hole_register.yaml` (H-56).
- TESTS: none new; the ten checks (B24.32) green on the commit before this one (KERN_B gate); the three repointed tests green after.
- FALSIFIER and CONTROL: "If a content hash moves on the deletion, something reached the kernel: stop and find the importer" (KERN_B). Control: SC-P2's gate below.
- GATE: (KERN_B "Gate") "one-season content hashes of `headless --case NPC-088 --seasons 2 --seed 0` and `build_realm(0)` equal before and after the deletion; `tools/export_sim_params.py --check` and `tools/freshness_gate.py` green"; "`python -m engine.season.harness.headless --world hearing --play <id>` exits 0 on a scripted stdin, on the commit before the deletion" (read at B24.15 and again on B24.32's commit); `python tools/validate_ed_citations.py` → exit 0; every new `FORK:` row read as an exact row through `pathres.load_alias_map()` (not `pathres.resolve()`, CLAUDE.md §8); `PYTHONHASHSEED=0 python -m pytest engine/tests/test_sigma_leverage_parity.py tests/valoria/test_band_extension_seam.py tests/valoria/test_degree_ladder_single_owner.py -q` → pass.
- HASH MOVERS: "None (unreachable code; the gate's equal hashes are the control)".
- DEPENDS ON: V12 B24.32 (the ten checks and check 11; check 8 no longer STOPS, B24p.02's `Decider.moved_by`); V12 B24p.12 (the `persuasion_track` row is deleted there); V12 B24.15 (`--play`); EXISTS-IN-TREE `systems/social_contest/sim/contest/` (16 files), `engine/tests/test_contest_kernel.py`, `references/module_contracts.yaml` `module: social_contest`, `tools/export_sim_params.py`, `tools/pathres.py::load_alias_map`.
- IDS: ED-SC block slot 1.
- GLOSSARY: none (the kernel's words — Style, genre, Doubt Marker, `FaceScale` — have no glossary row to retire `[ASSUMPTION: basis: `unified/U1_GLOSSARY.md` not searched for them by this lane; the producer greps the file and strikes any row naming a deleted symbol]`).
- COST and TIER: small build (a deletion wave with registry repoints); `sonnet`, `high`.
- LANDS IT: B24's producer; `Item: B24.33`, `[skip ci]`. (KERN_B: "the ledger row (edit 4) is the orchestrator's": the batch's orchestrator lands it in this commit from B24's ED block.)

### B24.34 — who holds a Record can be found out · ARCS item 4 · BUILD · HASH MOVER(behaviour)
- SOURCE: ARCS "Resolution (decided)" item 4 (copied), "Edits, by owner" (copied), "Gate", "Falsifier"; items 1–3 superseded (ARCS's own Status: their owners are EVID_B, ADM, OBS: no item); U1 ledger S-26.
- ADVANCES: R-04.c3 (custody is evidence; NPC-088's defining risk), R-04.c7 (the inquiry's product).
- INSTRUCTION: "the site is `engine/season/loop/witness.py::_found_claims`, which deposits what a look teaches by band through `rosters.yaml: finding_terms` (band → `observation_terms` members; loaded by `data/rosters.py::_load_finding_terms`). Edit: one `observation_terms` member `holder` `[ASSUMPTION: the member name; U1 ledger S-26 owns the roster]`, added to `finding_terms` at `Partial` and above for an inquiry at a place where a Record is kept; `_found_claims` deposits `(holder person, holds, record id)` to the finder. It names a holder, not a doer, so D-U1-06 (a)'s `supplied_by: who` constraint does not bind it `[ASSUMPTION — basis: a holding is a state, not an act's hand]`." SITE (ARCS's `[UNVERIFIED]`): first open `state/carriers.py` and record in the commit body where a Record's holder is (a live `hold` Tenure, as `cases/exercises/NPC-088.yaml` records); deposit from that read. "`hole_register.yaml`: H-216 and H-75 regraded when the gates below read."
- WHERE: `engine/season/rosters.yaml` (`observation_terms` `holder`; `finding_terms` cells); `engine/season/loop/witness.py` (`_found_claims`); `engine/season/hole_register.yaml` (H-216, H-75 `grade:`); NEW `engine/season/tests/test_arcs_possession_found.py`.
- TESTS: written first, red: `test_an_inquiry_finds_who_holds_the_record`, `test_a_given_away_record_names_the_new_holder`, `test_a_failed_inquiry_deposits_no_holds_claim` (ARCS).
- FALSIFIER and CONTROL: "If the `proofs` levels are equal with and without the cited Record, the proof is not read; if the obstacle moves with it, a favourable term was subtracted (A-25). If a forged Record and a true one are indistinguishable to the bench forever, forgery has no risk" (ARCS). Control: a failed inquiry deposits nothing.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_arcs_possession_found.py -q` → pass; ARCS's realm reading, recorded in the commit body (two seasons, A-114): "NPC-086 on the realm, seeds 0, 1, 2: Bergvall's hearing reads more `proofs` levels for his side when he cites his survey Record than when it has been seized beforehand (off-arm) … NPC-088: an inquiry at her workshop that grades `Partial` or better deposits a `holds` claim about her in the inquirer's ledger; with the Record given away first, the claim names the new holder."
- HASH MOVERS: "Every world in which a graded inquiry at a Record's place grades `Partial` or above (declared)." Re-pinned at B24.99.
- DEPENDS ON: V12 B24.25 (`cites` of a Record), B24.22; EXISTS-IN-TREE `loop/witness.py::_found_claims`, `data/rosters.py::_load_finding_terms`; V12 Batch B11-fi-readers (`08_FI_03` §2: graded inquiries' finding terms).
- GLOSSARY: row *holder* (if a row for `observation_terms` members exists): "holder: the person who has a thing in his keeping".
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B24's producer; `Item: B24.34`, `[skip ci]`.

### B24.35 — which ground moves whom: four conditions, backing the fit source · WGM edits 2–3 (with `17_CENSUS_C1A_02` W4's `which_ground` half) · BUILD · HASH MOVER(behaviour)
- SOURCE: WGM "Exact edits" 2 and 3 (copied), "The gate", "Named tests", "The falsifier"; edits 1 and 4 landed in Batch B04-capability-home (B04.07: the four trait rows and `cast.traits_of`); `17_CENSUS_C1A_02_wires_and_corrections.md` "Dependency edges" ("`02_CHAR_which_ground_moves_whom.md` (B24) cites the arm, not a second regard term", U3 §4.1 row 40: no edit of its own); C-U5a-08 (polarity), D-U1-01, U1 §3 items 3 and 6.
- ADVANCES: R-04.c3 at depth; R-06 (people differ in what moves them).
- INSTRUCTION:
  1. "**Four `when` keys** (new members of the uses table's closed `when` roster; one host-side function each in `seam/wrappers/sigma.py`, beside `advantage_sigma`; each reads the act's payload, the **arguer's own** ledger and the hearer's interior fields, never the hearer's ledger, `04` §B.2 F8)": `cites: <proofs member>` (the act's payload cites at least one held item of that kind; `person_q.proof_kind`); `consequence_held: true` (the arguer's own ledger holds a deed claim about the argued Proposition's subject that the hearer's `Person.pursuits` score negative; `person_q.deeds_judged` over the arguer's ledger, scored with the hearer's projected pursuits); `creed_committed: true` (the argued Proposition is a creed Proposition the hearer holds a live `commit` edge to `[ASSUMPTION: the creed half of the design's Authority, kept; basis: the hearer's live Tenures are interior fields OBS §2 member 12 already reads]`); `regard_at_least: <n>` (`person_q.stance_toward(hearer, arguer)`, clamped at `STANCE_MAX`). "`speaker_over_subject` … is **removed**."
  2. The four uses rows are NOT written. The four `when` functions of step 1 are kept and feed `Speaker.backed: tuple` (the grounds whose condition holds for this act; default every ground), a field this item adds; `proceeding.LEVERAGE["fit"]` counts a ground's positive fit only when the ground is in `backed`. So a ground must be chosen AND backed (a cited record for `evidence`, a held consequence, the hearer's creed, regard of at least 3), and one owner sizes what a ground is worth (`fit_level`). Test (b) reads the `fit` source.
  Edit 5 ("the arguer's own knowledge of it") is not built (WGM: "the FI and SC lanes' design").
- WHERE: `engine/season/rosters.yaml` (the `when` roster's four members); `engine/season/seam/wrappers/sigma.py` (four `when` functions beside `advantage_sigma`); `engine/season/queries/inputs.py` (`Speaker.backed`); NEW `engine/season/tests/test_susceptibility.py`.
- TESTS: written first, red: (a) `test_no_seated_trait_is_hash_equal`; (b) `test_a_solidarity_hearer_is_moved_more_often_only_when_the_condition_holds` (400 paired seeds, `assert checked >= 400`); `test_no_when_key_reads_the_hearers_ledger`.
- FALSIFIER and CONTROL: "(b)'s two rates are equal with the condition met (the row is not read), or differ with it unmet (the trait is acting as a flat modifier). Or (c) reads zero at seeds 0 to 2 over four seasons" — read at two seasons here (four in the source; A-114). Control: (a).
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_susceptibility.py -q` → pass; (c), recorded in the commit body: "In a seeded realm season, at least one `argue` on one of the eighteen resolves with the edge reported by the `capability` advantage source (in `fed_by` and SC-P1's `levels`)", `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 s`, s = 0, 1, 2, the per-act block.
- HASH MOVERS: "Declared, confined to `argue` on the eighteen hearers once the traits are seated" (B04.07 seated them). Re-pinned at B24.99.
- DEPENDS ON: V12 Batch B04-capability-home (B04.07 `Person.traits`, the trait rows; B04.05 the uses table and its closed `when` roster); V12 Batch B05-one-roll (U5a Part B: the `edge` reader's signed two-list form); V12 Batch B10-character (`02_CHAR_scar_cap_and_regard_unit` Addendum: the regard arm W4 names); V12 B24.22 (`proof_kind`), B24.27 (`cites` in computed play); V12 B24p.02 (`Speaker`), B24p.08 (`LEVERAGE["fit"]`); EXISTS-IN-TREE `person_q.deeds_judged`, `person_q.stance_toward`, `sigma.py::advantage_sigma`.
- GLOSSARY: none (the four traits' rows landed at B04.07).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B24's producer (an IN/CHAR edit inside the SC batch); `Item: B24.35`, `[skip ci]`.

### B24.36 — the arrangements loader holds `speech_kinds` to its roster · REST_2 W2 · BUILD · HASH EQUAL
- SOURCE: `17_CENSUS_REST_2_wiring.md` "W2" (copied), "Order" ("W2 in B24 after `05_SC_playable_hearing_B.md`'s roster note", B24.03).
- ADVANCES: none of the nine; the loader's refusal per data family (CLAUDE.md §0.05).
- INSTRUCTION: "In `data/arrangements.py::_load`, after the `speech_kinds` rows are read:
  ```
  if set(speech_kinds) != set(LADDER_RUNGS):
      raise SystemExit("arrangements.yaml: speech_kinds ids and rosters.yaml: ladder_rungs disagree — "
                       f"only in speech_kinds: {sorted(set(speech_kinds) - set(LADDER_RUNGS))}; "
                       f"only in the roster: {sorted(set(LADDER_RUNGS) - set(speech_kinds))}")
  ```
  `LADDER_RUNGS` joins the import. `tests/test_arrangements.py` then asserts the refusal (a mutated copy of the document raises) instead of restating the equality, and `tests/test_stress_proceedings_rehost.py`'s `len(LADDER_RUNGS) == 6` stays." "The refusal is written against the roster as that edit leaves it": B24.03 corrected the note and kept the six ids under `ladder_rungs`.
- WHERE: `engine/season/data/arrangements.py` (`_load`; the import line); `engine/season/tests/test_arrangements.py` (the equality assertion becomes the refusal test).
- TESTS: the refusal test in `test_arrangements.py`, written first.
- FALSIFIER and CONTROL: "Add a seventh id to a copy of `arrangements.yaml: speech_kinds` and load it: `SystemExit` naming the id; before the edit the load succeeds." Control: realm hashes equal to B24.35's.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_arrangements.py engine/season/tests/test_stress_proceedings_rehost.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 B24.03; EXISTS-IN-TREE `data/arrangements.py::_load`, `data/rosters.py::LADDER_RUNGS`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B24's producer; `Item: B24.36`, `[skip ci]`.

### B24.37 — the sitting leaves 0: the hearing's settings set to their shipped values · HEAR_B edit 10's shipped arm, ADM, EVID_B · BUILD · HASH MOVER(behaviour)
- SOURCE: U3 §1 item 24's gate ("`sitting_exchanges` leaves 0"); HEAR_B "What it changes" ("At the shipped arm a `determine` on a docketed matter is deferred to ENCOUNTER … A declared mover wherever a `determine` executes with items on file") and its "Hash movers"; ADM "`first_heard_ob`, proposed 1"; EVID_B "`answer_step`: control 0, first value 0.25" and "the control arm, kept until the gate passes"; `V12_STRUCTURE.md` D-22 (a setting set in its own batch needs nothing more).
- ADVANCES: R-04.c3 in computed play; the readings of B24.38 and B24.39.
- INSTRUCTION: in `engine/season/data/fixtures.py`, one commit, each line's `SHIPPED` comment moved to the new value: `sitting_exchanges` 0 → its shipped arm (B24.07's switch); `answer_step` 0 → 0.25; `first_heard_ob` 0 → 1; `evidence_from` `ledger` → `case_file`. `fault_step` stays at control (no source states its value: DIALS AT CONTROL, B98). Revert: the four controls, which reproduce B24.36's hash.
- WHERE: `engine/season/data/fixtures.py` (four values).
- TESTS: none new; `test_realm_hash_equal_at_sitting_exchanges_zero` re-pointed to read B24.07's control fixtures explicitly (it asserts the control, not the shipped value).
- FALSIFIER and CONTROL: the realm hash does not move (no `determine` reaches a sitting with items on file, which is B24.39's question). Control: the four controls reproduce B24.36's reading.
- GATE: realm content hashes (`HASH READING`) after one season at seeds 0, 1, 2 → moved, each recorded; with the four controls restored in a scratch run → equal to B24.36's reading; `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_sc_hearing_sitting.py engine/season/tests/test_sc_hearing_evidence.py engine/season/tests/test_sc_hearing_admission.py -q` → pass; `python tools/ci_sim_fabrication_check.py` → exit 0.
- HASH MOVERS: declared: every world in which a `determine` executes with items on file, or a cited `speak` folds on the case-file arm. Re-pinned at B24.99.
- DEPENDS ON: V12 B24.07, B24.21, B24.25, and every item before (the shipped arm reads all of them).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`; the moved readings read by `opus` at the close.
- LANDS IT: B24's producer; `Item: B24.37`, `[skip ci]`.

### B24.38 — every ending of a sitting writes · IS-B2-SC-08 · BUILD · HASH MOVER(behaviour)
- SOURCE: `IS-B2` §1.1 "Item: IS-B2-SC-08" (copied); `IS-B3-GO-01` (the `kinds` field, `ENDING_KINDS`); A-80, A-81.
- ADVANCES: R-04.c3 (no sitting is still); A-80, A-81 for the hearing.
- INSTRUCTION ("INSTRUCTION, in order", copied):
  1. "`engine/season/harness/governance_spine.py`: `hearing_ending(w, matter) -> str`, a reader over the log and the case file returning one of `carried`, `carried_in_part`, `dismissed`, `adjourned`, `lapsed`, `agreed`, `parted`; computed, stored nowhere."
  2. "`headless --world hearing` prints one summary line per run: the ending, the tick, the count of exchanges, and the count of durable writes the sitting's Events made (case-file stages, Tenures opened or closed, claims deposited to attendees; the budget debit excluded, A-81)."
  3. "`adjourn` writes one `adjourned` stage to the case file under the bench member's own act (HEAR_B edit 7's carrier), so the next sitting reads it."
  4. "The entrenched arm: the same fixture with every party's `argue` and `answer` returning Failure (a planted generator); the reading is that the run still ends by one of the seven kinds and writes."
  5. "The `hearing` row's `kinds` (`IS-B3-GO-01`), from the played party's side `[ASSUMPTION: the seated person is a party or an advocate, not a bench member — basis: HEAR_B's seat list; a seated bench member reads `drawn` for every name]`: `carried` `won`, `carried_in_part` `won`, `agreed` `won`, `dismissed` `lost`, `adjourned` `drawn`, `lapsed` `drawn`, `parted` `drawn`; it is registered in `scenarios.SCENARIOS` by HEAR_B edit 9's `headless --world hearing`, which calls `scenarios.run` (`IS-B2-CORE-01` (4))." The row's `ending` reader becomes `hearing_ending` (B24.15 registered it with none).
  `dismissed` is reachable at B27 (`05_SC_acquittal`); before it, a Failure reads `dismissed` only if the reader maps `matter.undetermined` to it `[ASSUMPTION: the mapping — basis: `verb_table.yaml: determine` emits `matter.undetermined` at Failure today; B27 re-points it]`.
- WHERE: `engine/season/harness/governance_spine.py` (`hearing_ending`); `engine/season/harness/headless.py` (the summary line for `--world hearing`); `engine/season/loop/effects_information.py::_eff_determine` (the `adjourned` stage); `engine/season/harness/scenarios.py` (`SCENARIOS["hearing"]` `ending`, `kinds`); `engine/season/tests/test_sc_hearing_sitting.py`.
- TESTS: written first, red: "`test_every_ending_of_a_sitting_leaves_a_durable_write` (seeds 0 to 19, `--auto`; for each run the write count is above 0, and `assert` that at least three ending kinds occurred across the twenty, so the loop cannot pass by one kind); `test_an_adjourned_stage_is_read_by_the_next_sitting`; control `test_a_sitting_with_its_case_file_writes_suppressed_counts_zero` (the counter can read zero)."
- FALSIFIER and CONTROL: as the tests; control `test_a_sitting_with_its_case_file_writes_suppressed_counts_zero`.
- GATE: "those tests; the summary line at seeds 0 to 2 recorded in B24's close, and again at B27's close with `dismissed` now reachable": `PYTHONHASHSEED=0 python -m engine.season.harness.headless --world hearing --seed s --auto`, s = 0, 1, 2 → one summary line each, write count above 0; `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_sc_hearing_sitting.py engine/season/tests/test_scenarios_runner.py -q` → pass.
- HASH MOVERS: "step (3) only, where a bench adjourns with `sitting_exchanges` above 0 (inside HEAR_B's declared mover)". Re-pinned at B24.99.
- DEPENDS ON: V12 B24.14, B24.15, B24.37; V12 Batch B11-fi-readers (`IS-B2-CORE-01`, `IS-B3-GO-01`: `Scenario.kinds`, `ENDING_KINDS`).
- GLOSSARY: row *ending (of a sitting)*: the seven names, owner `governance_spine.hearing_ending`; "adjourned: put off to a later sitting, as a court adjourns".
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B24's producer; `Item: B24.38`, `[skip ci]`.

*(B24.39 is a READING position, `IS-B2-SC-09` (1) and (2): no item body; its text is reading R1 in this batch's Readings block below.)*

### B24.40 — repair at the refusing clause's owner, if the realm never enters the hearing · IS-B2-SC-09 step (3) · BUILD (RUNS IF) · HASH MOVER(behaviour)
- SOURCE: `IS-B2` §1.1 "Item: IS-B2-SC-09" step (3) (copied); H-01 (the holistic audit's question, asked of the role).
- ADVANCES: R-04.c3 in the realm; H-01 for `social_contest.proceeding`.
- RUNS IF: reading R1's after-arm reads `social_contest.proceeding` entered 0 times at all three seeds. Otherwise this position is recorded "not run: R1 above 0" in B24.99's commit body and makes no commit.
- INSTRUCTION: "If the role is entered in none, the batch does not close on the fixture alone: the refusing clause is read from the run (`clause:docket` asks for *a fired Date with a DocketItem*, `verb_table.yaml: determine`), and the repair is made at that clause's owner (`world_q.slot_for`, `_eff_convene`'s Date, or the chooser's formation of `determine`), as its own `Item:` commit with its own test. No verb is special-cased and no docket is planted in the realm builder."
- WHERE: the owner the reading names (one of `engine/season/queries/world_q.py::slot_for`, the `convene` effect's Date, `engine/season/decision/options.py`'s formation of `determine`); a test beside that owner's tests.
- TESTS: one named for the clause repaired, written first and read red on the realm reading (e.g. `test_a_docketed_case_meets_a_fired_sitting` `[ASSUMPTION: test name; the item creates it]`).
- FALSIFIER and CONTROL: "the fixture's `--auto` run enters the role (the instrument can see an entry); the realm reads 0 at all three seeds after the edit." Control: the fixture's entry count (B24.15) unchanged.
- GATE: reading R1 re-taken → `social_contest.proceeding` entered at least once in at least two of seeds 0, 1, 2, two seasons; the new test green.
- HASH MOVERS: "step (3) if taken (declared then)". Re-pinned at B24.99.
- DEPENDS ON: reading R1; V12 Batch B02-tests (CI-11's `ENGINES` block).
- GLOSSARY: none.
- COST and TIER: build; `opus` (`IS-B2-SC-09`: "`opus` if step (3) is taken").
- LANDS IT: B24's producer; `Item: B24.40`, `[skip ci]`; if the repair needs a file outside B24's census, `STOPPED` with the owner named (CLAUDE.md §0).

### B24.41 — the social attributes acting on others · CR-92 (intake) · DESIGN-FIRST · HASH EQUAL
- SOURCE: the intake `:183` (CR-92, STILL-NEEDED, "IN/SC · design-first beside B24/B10 · design file with six falsifiers"); carry-forward `master/eval/E1.md` "### CR-92" (`:3760` at the intake's read; = E4 `:2913`): WHAT, REMAINING UNBUILT, GATE, EXIT and FALSIFIER, HASH MOVERS (copied below); placed by `_part2` §5.6's third rule (no member names CR-92; its own text says "beside B24/B10", which places no position: the batch's tail, in the intake's order); `V12_STRUCTURE.md` D-18.
- ADVANCES: R-07 (contributor), R-06 (contributor) (v11's R line); nothing at this commit.
- INSTRUCTION (REMAINING UNBUILT, copied): "ONE design file under `proposals/`, no code, stating with a falsifier each: (1) **how Grace reaches regard** without a person-side reader of another's true attribute: the candidate door is WITNESS (the World may read the true value; the holder reads only what was deposited), the precedent CR-79's credit term; `layer-conformance` Lens B on AX-2 answered first; (2) **promotion**: confirmed through `stance_term`, no `confer` edit, or the design names why not; (3) **the venue standard**: the requirement read from the existing keys (no fourteenth key; `data/arrangements.py` refuses one), and the shortfall demoting the contest result, surplus adding nothing in the venue (adj §3.1 (12)), with its band and the reading rule that chooses any coefficient; (4) **Presence on obedience**: a term on the receiver's `comply` against `defy`/`evade` from the issuer's Presence, as seen by the receiver; (5) **Attunement on bonds**: the formation term IN-32's `tie / knot` effect consumes, and the re-pointing of the knot oracle's Bonds gate (the oracle changes at its owner, re-exported, `CLAUDE.md` §6); (6) the two profiles as its falsifier pair: high Presence, low Grace wins the contest and loses regard; high Grace, low Presence wins regard and loses the contest (AR-49, AR-50)." The file is `proposals/2026-11-12-subsystem-audit-suite/proposals/CR-92_social_attributes_on_others.md` `[ASSUMPTION: the path — basis: "ONE design file under `proposals/`"; the producer may choose another and records it]`; its words are A-98's (Grace, Presence, Attunement are attributes; a skill is a skill). It reads SC-02's design as built at B24.02 and CR-83's design (Batch B11-fi-readers). `[ASSUMPTION; medium; Jordan to correct; revert: the shortfall lowers `reception` only]` (ASKS ATTACHED) is carried into the file. Items (3) and (6) are built for the room by B24p.07 and B24p.18 and the design cites them. Item (1) has its carrier: the `ending`'s per-side marks and esteem (B24p.20), which WITNESS deposits; the design decides what regard does with them. Items (2), (4), (5) stand.
- WHERE: NEW the design file above.
- TESTS: none (a design).
- FALSIFIER and CONTROL: "the file exists and states (1) to (6), each with a falsifier and a control (every term at 0 reproduces the base hash); no code" (EXIT).
- GATE: the file exists and states (1) to (6), each with a falsifier and a control; `git diff --stat` for the commit names one `.md` under `proposals/` and nothing else.
- HASH MOVERS: "the design none; each build it schedules a declared MOVER, P14". Its builds are not scheduled in v12 (the design names them; a later plan or B98 reads them).
- DEPENDS ON: V12 B24.02 (SC-02's re-source of `reception`); V12 Batch B11-fi-readers (CR-83's design, `IS-B2-FI-05`); LANDED ALREADY (re-checked at the open): CR-20 (`Person.attributes`), CR-84 (the ten keys), `regard`, `reception`, `stance_term`, `arrangements.yaml`'s `interposed`, `order`, `floor`, `venue_min_rank`.
- GLOSSARY: none (no term coined until the design does; its new words are glossed in the file and added to `unified/U1_GLOSSARY.md` when a build lands them).
- NAMES: "`capability`" in the carried text → skill (A-98); "Bonds" names the knot oracle's gate key, which the ten attributes drop (the design's (5)).
- COST and TIER: design; `opus`, `high` (BUILDER: opus; its critic per CLAUDE.md §10, Lens B the judgment node).
- LANDS IT: B24's producer (on `opus`); `Item: B24.41`, `[skip ci]`.

### B24.42 — the social-contest scale row, measured · IS-B2-SC-01 · POINTER · —
- SOURCE: `IS-B2` §1.1 "Item: IS-B2-SC-01" (the ten steps of §1.0 are v12's batch order: B03, B04, B05, B07, B09–B10, B11, B24, B27, B28, B34, each batch's close recording its SC reading).
- What it does: "At B24's close, and only if `IS-B2-SC-09`'s reading is above zero, edit the `scales:` row `social contests / debates` in `engine/season/requirements.yaml`: `in_loop:` becomes the measured sentence (the command, the seeds, the count of `determine` acts resolved through `social_contest.proceeding`); its `note:` loses the sentences about the kernel, which `05_SC_sc05_kernel_disposition_B.md` retires in the same batch." Lands in B24.99's commit (the batch's last `Item:` commit, `_part4` E-1), and nowhere else.
- Target: `engine/season/requirements.yaml` (`scales:`, the social-contest row).
- GATE: `python -m engine.season.harness.register --requirements` → exit 0, nine statuses unchanged before and after; the row's sentence reproduces by its own command (reading R1). Falsifier: the row edited while R1 reads 0 at all three seeds.

## Readings (B24)

**R1 — `IS-B2-SC-09` (1) and (2), the hearing reached by computed play** (position B24.39; the text of `IS-B2` §1.1 "Item: IS-B2-SC-09", copied byte for byte):

"(1) at B24's open, record `python -m engine.season.harness.aperture 2 s` for s = 0, 1, 2: `open_case`, `speak`, `determine` attempted, executed and the deciding read per refusal. (2) After HEAR_B edit 6: the same three runs, with CI-11's `ENGINES` block. Expected: `social_contest.proceeding` entered at least once in at least two of the three seeds, and at least one `matter.determined` whose `ending` lists an exchange. (3) If the role is entered in none, the batch does not close on the fixture alone: the refusing clause is read from the run (`clause:docket` asks for *a fired Date with a DocketItem*, `verb_table.yaml: determine`), and the repair is made at that clause's owner (`world_q.slot_for`, `_eff_convene`'s Date, or the chooser's formation of `determine`), as its own `Item:` commit with its own test. No verb is special-cased and no docket is planted in the realm builder."

As this plan schedules it: arm (1) is taken on the batch's base before B24.01 and recorded in B24.01's commit body (`reading @<base sha>`); arm (2) is taken after B24.37 (the shipped arm; "after HEAR_B edit 6" is met) with `PYTHONHASHSEED=0` at two seasons, and recorded in B24.99's commit body; step (3) is B24.40. Extraction of the three runs' lines: `haiku` (`IS-B2-SC-09` cost line). `[UNVERIFIED in the source: "this lane read one season at one seed; two seasons at three seeds is the item's first step."]`

### B24.99 — re-pin and close readings · `_part4` E-1 · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2; `_part2` §5.9, §5.12; `IS-A-12`; `IS-B2-SC-01` (B24.42).
- ADVANCES: R-04.c3's reading recorded; M3 and M4 inputs (`V12_STRUCTURE.md` §3).
- INSTRUCTION:
  1. Re-pin, once: the realm pins in `engine/season/tests/_realm_goldens.py` (B02's one owner) at seeds 0 to 2, and every seeded golden under `engine/tests/` a moved `speak` or `determine` reaches (found by running them on this tree, SC-02's §5), read against B21b's after-reading (`reading @<sha>`; the head's RE-PIN line; R2c, K5 F5). The commit says "re-pin": the movers are B24.01 (`DocketItem.case`), B24.02 (`reception`, `proofs` re-sourced), B24.10 (at control: EQUAL), B24.27 (cite variants), B24.34 (the `holds` deposit), B24.35 (the four `edge` rows), B24.37 (the shipped arm), B24.38 (the `adjourned` stage), B24.40 (if run); each named old → new in the body.
  2. `IS-B2-SC-01` (B24.42): the `scales:` row edit, only if R1's after-arm is above zero.
  3. The conjunct's `reading:` record for R-04.c3 in `engine/season/requirements.yaml` (`IS-A-12`): the command, `PYTHONHASHSEED=0`, seed 0, the two hashes, the tree; `status:` is not edited (A-114).
  4. The close's record (`_part2` §5.12) in this commit's body: `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, R-04.c3's reading with its tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<batch-start sha>`) and after, R1's two arms, B24.38's three summary lines, B24.02's §3c table before and after, and the batch's measured wall time (build and close apart).
- WHERE: `engine/season/tests/_realm_goldens.py`; the goldens under `engine/tests/` the run names; `engine/season/requirements.yaml` (R-04.c3's `reading:`; the `scales:` row if step 2 runs).
- TESTS: none new.
- FALSIFIER and CONTROL: a pin re-recorded that no declared mover reaches (then an undeclared mover landed: stop and find it). Control: every behaviour control quoted in the items above.
- GATE: the BATCH GATE of the batch head, read once on this commit.
- HASH MOVERS: the re-pin.
- DEPENDS ON: every position of B24 above.
- GLOSSARY: none.
- COST and TIER: edit and readings; `sonnet`, `high`; the readings read by `opus`.
- LANDS IT: B24's producer; `Item: B24.99`, without `[skip ci]` (the batch's last `Item:` push; CI run 1 of 2).

| STOP. Batch B24-sc-hearing closes here |
