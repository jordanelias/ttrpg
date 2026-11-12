# Workplan v12 — part 38: Batch B33-inst-economy-hands

## Status: PROPOSED (a body part of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree at `30c978f` (branch `ccr-62958c70-0kjhsw`), read 2026-11-12; author lane A38 of `master/workplan_v12/V12_STRUCTURE_part2.md` §4.2, with the errata of `V12_STRUCTURE_part4.md`. Every item is written against the tree as the batches before it leave it; a symbol absent at `30c978f` names the batch that makes it.

**What this part holds.** One batch of the FA lane, `B33-inst-economy-hands`: the thirteen institution proposals U3 §1 item 33 lists, in its order (`_BYZANTINE_B` → `_C` → `_D` → `_COLONIAL_B` → `_C` → `_D` → `_PAPACY_C` → `_D` → `_E` → `_VENICE_A` → `_B` → `_D` → `_SYNTHESIS_C`), and the one intake entry under the intake's B33 heading (CP-T08-07, `:333`, MISSING-DEP). A part cites another part's batch or item by handle only; the head's index maps a handle to its file.

**Words.** `unified/U1_GLOSSARY.md`; a person's numbers are an attribute, a skill and its skill score, a derived score (A-98); a *lap* is one pass of the season's scene budget and a *round* is one engagement of a fight (A-101); armies follow the mass-battle lexicon (no size words). Source text that says "capability" in prose reads *skill* here; the identifier `capability:` keeps its spelling in backticks. "Sworn man" for an obligee (U4d, glossary *sworn*).

**Paths.** As `V12_STRUCTURE.md` states: a bare path is under `proposals/2026-11-12-subsystem-audit-suite/`; `U3` is `unified/U3_DEPENDENCY_ORDER.md`; `the intake` is `master/eval/V12_INTAKE.md`. `S/` abbreviates `engine/season/`. A member proposal is cited by its short name: `BYZ_B` is `proposals/15_INSTITUTIONS_BYZANTINE_B_the_roga_and_the_fisc.md`, and likewise `BYZ_C`, `BYZ_D`, `COL_B`, `COL_C`, `COL_D`, `PAP_C`, `PAP_D`, `PAP_E`, `VEN_A`, `VEN_B`, `VEN_D`, `SYN_C` (`15_INSTITUTIONS_<FAMILY>_<letter>_*.md`); `SYN_A` and `SYN_B` are B32's `15_INSTITUTIONS_SYNTHESIS_A_one_kit.md` and `_B_the_deed_ledger.md`.

**One overlap this part cannot see across, and how each item handles it.** `SYN_A` (B32) is the kit: its §3 and §4 tables name, as owners on its files, several symbols whose edits this batch's members specify (`world_q.upkeep_owed` from BYZ_B edit 3, `hands_open` from BYZ_C edit 7, `audits_due`, `person_q.owed_to` from VEN_A edit 3, `forborne` with its `opening_set` decline from PAP_D edit 7, the `debt` row of `record_kinds` and `record_sourced_operands` from VEN_B edit 1, the `obligation` member of `advantage_sources`, `office_bodies.<body>.term` from BYZ_C edit 3, `resolve_anchor`'s `venue` form from VEN_D edit 1, and the eight arrangement rows of its §6). SYN_A's own "What it does not do" says "It builds no institution: every institution is the family proposals' content on these owners", so this part writes each of those edits as a B33 item; B32's part was not written when this part was, so **every such item's first step opens the tree and, where B32 landed the symbol, records the reading in its commit body and writes only what is absent** (one owner, CLAUDE.md §8). The receipt names them for the orchestrator to reconcile with B32's author.

---

## Batch B33-inst-economy-hands · lane FA · wave W18 · step S19 · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B33-inst-economy-hands
IN-FLIGHT ROW: registers/handoffs/HANDOFF_FA.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
GATE: Batch B02-tests
GATE: Batch B04-capability-home
GATE: Batch B05-one-roll
GATE: Batch B07-task-draw
GATE: Batch B12c-material-verbs-and-valley
GATE: Batch B21-fa-governance
GATE: Batch B24-sc-hearing
GATE: Batch B25-fi-questioning
GATE: Batch B26-fi-inquiry
GATE: Batch B27-sc-proceedings
GATE: Batch B28-social-verbs
GATE: Batch B32-inst-kit
REQUIREMENT: none — A-12, A-13, A-14 (`V12_STRUCTURE.md` §2.2's B33 row): the seat facts and the economy of the institutions kit (upkeep by grade, the hands an order passes, the audit at a term's end, the debt, the obligation that moves odds, the Church's sentence by other people's answers). No conjunct of R-01 to R-09 is moved; the close re-reads the nine and prints their held counts (`IS-A-12`).
BATCH GATE (read once, on the closing tree, `PYTHONHASHSEED=0` on every seeded command; no command past two seasons, D-17):
  `python -m pytest engine/season/tests/test_inst_byz_b.py engine/season/tests/test_inst_byz_c.py engine/season/tests/test_inst_byz_d.py engine/season/tests/test_remove.py engine/season/tests/test_audit_and_charter.py engine/season/tests/test_inst_col_d_ledger.py engine/season/tests/test_inst_pap_c.py engine/season/tests/test_inst_pap_d.py engine/season/tests/test_inst_pap_e.py engine/season/tests/test_inst_ven_a.py engine/season/tests/test_inst_ven_b.py engine/season/tests/test_inst_ven_d.py engine/season/tests/test_inst_syn_c_crossings.py -q` → all pass (every file is created by an item of this batch; each item names its own);
  the controls, each a reading of B32's close (`reading @<sha>`): `build_realm(0, foreign=False)`'s content hash → equal except where B33.01, B33.08, B33.21, B33.31 and B33.40 declare a build mover (each named in the re-pin commit); every fixture this batch adds at its shipped control (`obligation_level: None`, `penance_weight: 0`, `credit_terms` flat 1.0) and every new arrangement row undocketed → the realm content hash after one and two seasons at seeds 0, 1, 2 equal to the value the re-pin records, and the executed-verb tallies of `python -m engine.season.harness.corpus_run` at seed 0 read and quoted beside B32's (`reading @<sha>`), every moved tally attributed to a declared mover;
  `python -m engine.season.harness.register --check` → exit 0 (the batch's NUMBER rows, `IDS:`); `python -m engine.season.harness.register --requirements` → nine lines; `python tools/m1_acceptance.py --summary` → its verdict line quoted;
  `python tools/export_descriptors.py --check`, `python tools/export_sim_params.py --check`, `python tools/ci_sim_fabrication_check.py` → exit 0 (every new fixture carries its tag);
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (the batch touches engine core and registries: the full gates, CLAUDE.md §0.4);
  the glossary rows each item names, read against the code it landed (`STAGES.md` "The glossary always matches" rule 2): a mismatch fails the close;
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, and the batch's measured wall time; no conjunct is named, so no `reading:` record is written; `status:` is not edited (`IS-A-12`).
EXPECTED RED UNTIL B33.99: none beyond each item's own `EXPECTED RED UNTIL` line (the realm pins move from B33.01 and are re-pinned once at B33.99, under `[skip ci]`).
RE-PIN: once, at B33.99: the realm pins in `engine/season/tests/_realm_goldens.py` (B02's one pin file) at seeds 0 to 2, build, one and two seasons, both arms of `build_realm(foreign=)`; every seeded result the batch's movers moved, read against B32's close (`reading @<sha>`), or against B31's merge where B31 merges first in S19 (§7.4); the commit says "re-pin" and lists the moving handles (B33.01, .02, .03, .04, .08, .09, .10, .11, .12, .14, .15, .16, .17, .19, .21, .25, .26, .31, .40, .47).
IDS: ED-FA 0; H 7 (NUMBER rows: `border_hops` B33.14; `prescription_seasons` with its second field `prescription_cap` B33.20; `penance_weight` B33.28; `obligation_level`, `obligation_arrears`, `sealed_obligation` B33.34; `credit_terms` B33.38; each written only if B32's `SYN_A` §5 did not already write it, and an id unused is named in the expunge commit); NPC 1 (the court's holder, B33.09; `references/id_reservations.yaml` carries no NPC lane at `30c978f` (`grep -n NPC` finds a comment only), so B00 is asked for an NPC block, UNDECIDED 3).
DIALS AT CONTROL: `obligation_level` = `None`, `obligation_arrears` = 1.0, `sealed_obligation` = 1.0 (proposed `minor`, 0.5, 0); set by B98; target: none stated (VEN_A's gate reads Arm 1's band counts "read and reported"; "every value is recalibrated with OBS §4 step 5"), so `BLOCKED (design: no target reading)` unless OBS §4 step 5's joint re-centring names one (D-22) ·
  `penance_weight` = 0 (first value 2); set by B98; target: none stated ("`pardon` odds printed exactly at `penance_weight` 0 and 2"), `BLOCKED (design: no target reading)` ·
  `credit_terms` = flat 1.0 (proposed `{Overwhelming: 1.1, Success: 1.25, Partial: 1.5}`); set by B98; target: none stated, `BLOCKED (design: no target reading)` ·
  `goal_church_liberties_kept` shipped off (written commented out, B33.24); set by no batch until `data/goals.py`'s owner builds a place filter for `deed_doers` (PAP_C: "requested, not built here"), `BLOCKED (design: no carrier)` ·
  inherited, not set here: `distance_step` (B12c's), `presumption_gain` = 0 (B32's `SYN_B`; B33.22 reads it planted at 0.5 in a test only).
C(B33-inst-economy-hands): this batch's entries; the plan's head parts; `unified/U1_GLOSSARY.md` rows *upkeep*, *hand*, *distance*, *audit*, *consecration*, *excused*, *obligation*, *debt*, *sworn*, *roll*;
  `S/offices.yaml`; `S/rosters.yaml` (`office_bodies`, `foreign_cast`, `faction_leaders`, `factions.head_seat`, `successions`, `endings`, `record_kinds`, `record_sourced_operands`, `shortfall_sourced_operands`, `advantage_sources`, `alignment`, `tables`); `S/verb_table.yaml` (`carry`, `requisition`, `determine`, `revoke`, `issue`); `S/arrangements.yaml`; `S/goals.yaml`; `S/instruments.yaml` (B32); `S/write_matrix.yaml`; `S/hole_register.yaml`; `S/venues.yaml`; `S/harness/strife_moves.yaml`; `references/npc_registry.yaml`;
  `S/state/carriers.py` (`Office`); `S/state/containment.py` (`ancestry`); `S/state/gate.py` (`sworn_to`, `purview_reaches`, `seated_on_the_rung_above`, `REVOCATION_RULES`, `may_determine`, `sits_over`); `S/queries/world_q.py`; `S/queries/person_q.py`; `S/queries/inputs.py` (`SocialContestInput`); `S/seam/wrappers/sigma.py` (`contest_input`, `ADVANTAGE_SOURCES`); `modules/social_contest/roll.py` (`obstacle`); `S/data/fixtures.py`; `S/data/rosters.py` (`_load_offices`, `FOREIGN_CAST`); `S/data/requires.py`; `S/data/verbs.py` (`_derive_kind_verb`); `S/data/affiliations.py` (`_load_engagement`); `S/data/geography.py` (`adjacent_territories`, `geography`); `S/loop/effects_economy.py` (`_renewals`, `_eff_transfer`); `S/loop/effects_governance.py` (`_eff_requisition`, `_eff_revoke`); `S/loop/effects_information.py` (`_declared_stages`, `_mint_document`, `_eff_covenant`, `_eff_determine`, `_disposal`); `S/epistemic.py` (the reach predicate); `S/decision/options.py` (`opening_set`); `S/boot/realm.py` (B03c; `resolve_anchor`, `build_realm`);
  instruments: `register`, `corpus_run`, `strife`, `tools/m1_acceptance.py`, `tools/tests_for_diff.py`, `tools/ci_sim_fabrication_check.py`; `S/tests/_realm_goldens.py` (B02);
  the closing SHAs of B00, B01, B02, B04, B05, B07, B12c, B21, B24, B25, B26, B27, B28, B32 (and of B11, B21b, B21c, B24a, reached through them); the permanent surface.
SERIAL EDGES and FILE CENSUS: written after the position table and the items (E-11); see the end of this batch block, before the boundary row.
PARALLEL: S19 with B31-mb-loadout-economy (MB) and B36-wr-story-instruments (WR). Shared files (U3 §5.1 rows): `S/rosters.yaml` with B31 (different keys: this batch's are listed under C(B33)); `S/verb_table.yaml` with B36 (different rows: this batch edits `carry`, `requisition`, `determine`, `revoke`, `issue` only). Kept by hand at merge in §2.1's order, never regenerated (`V12_STRUCTURE_part3.md` §7.3). Merge position: after B31 (a mover; B33 rebases on B31's merge and re-reads its after-reading as the baseline, §7.4), before B36 (hash EQUAL).
COST: small builds and content rows, no calibration; producer `valoria-author` on `sonnet`, `high` (content rows `medium`); judgment nodes on `opus`: B33.04's band table, B33.07's terms on a contested row, B33.18–B33.20's 400-and-400 arms, B33.26's "answers differ" arm, B33.34's band reading, B33.45's "oath" arm (each named in its item); the close's terminal critique `opus`.
EST: 22 h [estimate: `V12_STRUCTURE.md` §2.4's formula over this batch's 49 positions (0.4 h × 49 + 2.5 h), E-15; §2.2's 8 h counted the thirteen members and one intake entry]
UNDECIDED: (1) BYZ_B edit 5 measures `distance` "from the exercised seat's rung to the place"; COL_B §1 and its falsifier measure it from "the **actor's** `place_of`" ("Planted: make `distance` read the seat's rung instead of the actor's place … reddens"). Taken: the actor's place (COL_B, the later and falsified statement), in B33.04 and B33.15. (2) OBS §2 defines `distance` as "the count of `contain` edges on the ladder path"; COL_B §1 proposes territory adjacency hops plus `border_hops` and leaves the pick to the member's owner. B12c lands the member's first reader on the ladder definition (`14_VERBS_MATERIAL_B` §2, B12c.12), so the reading that changes less is taken: the ladder reader stays the one reader, and B33.14 adds only what it cannot answer (two places under different roots: `root_of` and `border_hops`, with the `hops` of the centre settlement). (3) The court's holder needs an NPC id "allocated at landing from `references/id_reservations.yaml`'s `next_free`" (BYZ_D edit 1; COL_B §4), and that file has no NPC lane: either B00 adds an NPC block (H2's id table) or B33.09 reads the registry's next free id on `main` at landing and lands that bump first (CLAUDE.md §4's discipline). B33.09 is written for the first; the second is its fallback. (4) The settlement key for the centre: BYZ_D edit 2 writes `centre: {code: "ALT-0"}`, COL_B §4 writes `capital: {code: ALT-0, hops: 3}` for the same place (X-13: one seat, one person). Taken: one key, BYZ_D's name with COL_B's `hops` (`centre: {code: "ALT-0", hops: 3}`), since COL_B's own seat row says "BYZANTINE-D (whose row text governs)". (5) BYZ_B gate 3 runs "the `roga` scenario of proposal F" (`15_INSTITUTIONS_BYZANTINE_F`, B40) at eight seasons: moved to B40 at two seasons (A-114). (6) VEN_D §5's scenario needs `SYN_D` §1's case-file schema and `harness/institution.py`, both B40's: written here as a POINTER (B33.44), and A43 must carry the case file `S/cases/exercises/INST-VENICE-01.yaml` and its report rows. (7) PAP_D edit 8 and SYN_C gates 2 and 5 need CR-88's duty decline, which lands in B21d; B21d is not in B33's `after` list (§2.1) though it closes at S15, before B33 opens at S19. Taken: the items carry a `STOPS IF` on the tree (B33.45), and H2 is asked to add the edge B21d → B33 (no step is lost: B21d has slack 8). (8) SYN_C edits 4 and 5 are "requests, not edits" to the SC evidence owner and the MATERIAL lane; edit 4's sentence is `SYN_B` §4's request (B32), and edit 5 has no carrier in any batch this lane could read: B33.48 is BLOCKED with its owner, and SYN_C gate 7 waits with it. (9) VEN_D's Schoenland seats need "a `foreign_cast` row for Schoenland minting one place, WR's"; the tree's `S/rosters.yaml: foreign_cast` note refuses one ("`Schoenland` IS NOT HERE AND IS FOREIGN ALL THE SAME: its persons and its T16 root are already in the realm as built … a switch on it would move a world that does not need to move"): B33.43 is BLOCKED (WR). (10) BYZ_D edit 5's `off_guild_comptroller: passes_through: [{seat: off_kommerkiarios}]` puts a foreign seat into a realm row, so the control arm `foreign=False` (gate 1: "`content_hash` unchanged") may move; B33.11 carries a `STOPS IF` for it.

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B33.01 | a seat may say what it pays its sworn men, by grade | BYZ_B edits 1–2 | BUILD | MOVER(encoding) | Batch B32 (`BYZ_A`'s `dignity` rows; `SYN_A`'s `upkeep` refusal) |
| B33.02 | what a sworn man is owed, read per person | BYZ_B edit 3 | BUILD | MOVER(behaviour) | B33.01 |
| B33.03 | the bill, read when read | BYZ_B edit 4 | BUILD | MOVER(behaviour) | B33.02; Batch B12c |
| B33.04 | a tax rendered is not a tax taken: `requisition`'s terms and bands | BYZ_B edit 5 | BUILD | MOVER(behaviour) | B33.03; Batch B12c (B12c.13) |
| B33.05 | a stage that names a body or a seat is a hand | BYZ_C edit 4, with edit 3's `hand_term` read | BUILD | EQUAL | Batch B21, Batch B32 |
| B33.06 | the clerk is asked; an unentered stage reads as returned | BYZ_C edits 6–7 | BUILD | EQUAL | B33.05 |
| B33.07 | `carry` at a hand, drawn | BYZ_C edit 5 | BUILD | EQUAL | B33.06; Batch B28 |
| B33.08 | the King's and two dukes' papers pass their clerks | BYZ_C edits 1–3 | BUILD | MOVER(behaviour) | B33.07 |
| B33.09 | the centre beyond the map: a place and a person | BYZ_D edits 1–2; COL_B §4 bullets 1 and 3 | CONTENT | MOVER(encoding) | B33.08 |
| B33.10 | the court's seat and the Doux's; the empire may recall its officers | BYZ_D edit 3; COL_B §4 bullet 2 | BUILD | MOVER(encoding) | B33.09 |
| B33.11 | distance at a hand: the Doux's term and the trade gate's keeper | BYZ_D edits 4–5 | BUILD | MOVER(behaviour) | B33.10 |
| B33.12 | an order defied scars a holder of `altonian_civics` | BYZ_D edit 7 | CONTENT | MOVER(behaviour) | B33.10 |
| B33.13 | the tutoring demand is a covenant held at the hand | BYZ_D edit 6 | POINTER | — | B33.11; Batch B21b (CP-T09-03) |
| B33.14 | distance across a border; the root of a place | COL_B §1, §3 (`root_of`) | BUILD | MOVER(behaviour) | B33.10; Batch B12c (B12c.12) |
| B33.15 | a roll through a seat reads distance from where the actor stands | COL_B §1 (the host operand) | BUILD | MOVER(behaviour) | B33.14 |
| B33.16 | news of a change of office stops at the border | COL_B §3 | BUILD | MOVER(behaviour) | B33.14; Batch B24 (B11's CR-29 map) |
| B33.17 | the court wants quiet; reabsorption is an ending | COL_B §4 bullet 4, §5 | CONTENT | MOVER(encoding) | B33.10 |
| B33.18 | two hearings: `audit` and `quo_warranto` | COL_C edit 1 | BUILD | EQUAL | Batch B27, Batch B32 |
| B33.19 | the audit's occasion, and the seats an audit follows | COL_C edit 2 | BUILD | MOVER(behaviour) | B33.18 |
| B33.20 | a held grant pleads its age; a granted seat carries its term | COL_C edits 3–4 | BUILD | EQUAL | B33.18 |
| B33.21 | Hafenmark passes by inheritance, through a title vacant at build | COL_D edit 4 | BUILD | MOVER(encoding) | Batch B32 (`BYZ_A`'s vacant-row edit) |
| B33.22 | standing passes down the seat: the chain reading | COL_D gate (`test_inst_col_d_ledger.py`) | BUILD | EQUAL | B33.21; Batch B32 (`SYN_B` §1) |
| B33.23 | consecration: a hearing that mints a certificate | PAP_C edit 3 | BUILD | EQUAL | Batch B32 (`SYN_B` §3, §4; CR-36's site through B21c) |
| B33.24 | the Church keeps its liberties: a goal row, shipped off | PAP_C edit 4 | CONTENT | EQUAL | B33.23 |
| B33.25 | a ban or a detention opened is an Event of its own | PAP_D edits 1–3 | BUILD | MOVER(behaviour) | Batch B27 |
| B33.26 | the Church's two sentences grade by band | PAP_D edit 4 | BUILD | MOVER(behaviour) | B33.25 |
| B33.27 | a man who complied shuns: the decline | PAP_D edit 7 | BUILD | EQUAL | Batch B28, Batch B32 |
| B33.28 | penance weighs in a pardon | PAP_D edit 9 | BUILD | EQUAL | B33.25 |
| B33.29 | the strife instrument counts the Church's sentences | PAP_D edit 10 | BUILD | EQUAL | B33.25 |
| B33.30 | the standing levy, the `tax` edict | CP-T08-07 (the intake `:333`) | BLOCKED (SE/FA: H-163 limit 3(a), a governor's stock claim, has no owner) | — | — |
| B33.31 | three sees, built vacant | PAP_E edit 1 | BUILD | MOVER(encoding) | Batch B32 |
| B33.32 | the tithe named in the Cardinal's goal; an exempt house offered, off | PAP_E edits 3–4 | CONTENT | EQUAL | B33.31 |
| B33.33 | what the one asked owes: `owed_to` | VEN_A edit 3 | BUILD | EQUAL | Batch B32 |
| B33.34 | `obligation` as levels; three fixtures at control; member 12 widened; the host's operands | VEN_A edits 1, 2, 4, 5 | BUILD | EQUAL | B33.33; Batch B05 |
| B33.35 | the `debt` kind, its operands and the distraint's one check | VEN_B edit 1 | BUILD | EQUAL | B33.34; Batch B32 |
| B33.36 | `covenant` mints a bond | VEN_B edit 2 | BUILD | EQUAL | B33.35 |
| B33.37 | a payment to the bond's place counts toward it | VEN_B edits 3–4 | BUILD | EQUAL | B33.36 |
| B33.38 | a suit for debt; the loan's terms at control | VEN_B edits 6–7 | BUILD | EQUAL | B33.37; Batch B27 |
| B33.39 | a seat on a building | VEN_D edit 1 (§1) | BUILD | EQUAL | Batch B32 |
| B33.40 | the Guilds' house, their list and a commune council | VEN_D §4 (i)–(iii) | CONTENT | MOVER(encoding) | B33.39 |
| B33.41 | the secret bench and the enrolment ballot | VEN_D §4, the two rows | BUILD | EQUAL | B33.40 |
| B33.42 | a staple is a proof on an `exchange`; a market's standard | VEN_D §3 | BUILD | EQUAL | B33.41; Batch B12c (B12c.14) |
| B33.43 | Schoenland's seats | VEN_D §4, `foreign_seats` | BLOCKED (WR: a place for Schoenland's seats) | — | — |
| B33.44 | The Counting-House | VEN_D §5 | POINTER (to B40) | — | — |
| B33.45 | excused: whoever shuns a man, or was wronged by him, owes him nothing in the odds | SYN_C edit 1, with PAP_D edit 8 | BUILD | EQUAL | B33.34, B33.27; B21d (CR-88, `STOPS IF`) |
| B33.46 | the suit's forum stated; a hand of another faction | SYN_C edits 3, 6 | BUILD | EQUAL | B33.38, B33.11 |
| B33.47 | a publication is not a command: `issue` asks the form's basis | SYN_C edit 7 | BUILD | MOVER(behaviour) | B33.46; Batch B21, Batch B32 |
| B33.48 | rival certificates; an immunity in the levy | SYN_C edits 4–5 | BLOCKED (SC: evidence owner, edit 4 if B32 left it; SE: the MATERIAL lane, edit 5) | — | — |
| B33.99 | re-pin and close readings | `V12_STRUCTURE_part4.md` E-1 | BUILD | MOVER (the re-pin) | B33.01 to B33.48 |

Not in this batch, and where each is: `BYZ_A`, `BYZ_E`, `COL_A`, `PAP_A`, `PAP_B`, `VEN_C`, `SYN_A`, `SYN_B` (B32); the grounding files `15_INSTITUTIONS_BYZANTINE_grounding_mechanisms` (the treasurer's and the two Altonian seats' `audit_at_exit`, the `deed_doers` row for NPC-090), `15_INSTITUTIONS_PAPACY_grounding_mechanisms` (items 2, 3, 4, which PAP_D and PAP_E say "land with" them), `15_INSTITUTIONS_COLONIAL_grounding_F_what_the_tree_adds`, `15_INSTITUTIONS_VENICE_grounding_E_what_the_tree_adds` and the scenarios `BYZ_F`, `COL_E`, `PAP_F`, `SYN_D`, `SYN_E` (B40, U3 §3.1 rows); COL_D edits 1–3 (`SYN_B` §1 to §3: the chain term of `person_q.legitimacy` in B32, the founders' prehistory in B39, U3 §4.1 row 86) and COL_D edit 5 (not built: A-66, A-58); PAP_C edits 1, 2 and 5 (`SYN_A` §1 and `SYN_B` §3, §4, B32); PAP_D edits 5 and 6 (withdrawn, X-02); PAP_E edit 2 (withdrawn: the form `tithe` is `SYN_A`'s row), item 5 (dropped, A-36) and item 6, the schism (design-first and held, I-10: `unified/U4_DOCUMENT_STATUS.md` row for `PAP_E`, "not an edit of this batch"); VEN_B edits 3 and 5 (withdrawn: `world_q.owed`, `dues`, `breaches` are `SYN_A` §4's; C3-C7); SYN_C edit 2, the secular arm (a clause of `SYN_A`'s `avoidance` row, B32; B33.27's first step checks it is there); BYZ_B gate 3 and VEN_D §5's reading (B40); H-108 with IN-48 (the intake `:248`, under B21b's heading: the intake's heading decides the batch, E-8).

### B33.01 — a seat may say what it pays its sworn men, by grade · BYZ_B edits 1–2 · BUILD · HASH MOVER(encoding)
- SOURCE: BYZ_B "Exact edits" 1 and 2, "What it changes" 1, "Gate" 1; X-19, X-22 (its first `Reconciled:` line); rulings A-13; closes the audit's E-1 reading "no office declares `upkeep`" (`audits/15_INSTITUTIONS_BYZANTINE.md` §2.2).
- ADVANCES: none of the nine; A-13 (the seat's economy), through B33.02 and B33.03.
- INSTRUCTION:
  0. Open the tree: `grep -n "dignity:" engine/season/offices.yaml` and `S/data/rosters.py::_load_offices`'s refusal for `upkeep` ("not an int ≥ 0", `SYN_A` §3, B32). Record both readings in the commit body. **STOPS IF** no row carries `dignity:` (`SYN_A` §3: "`dignity` is not among" the applied Seat keys and "needs a ruling's amendment text before it lands"): then step 1's dignity rows are not written, the item lands `off_king`'s row alone, and the receipt says so.
  1. `S/offices.yaml: seats[].upkeep` — "optional int ≥ 0, loaded onto `Office.upkeep` (`state/carriers.py`, the field exists and `__post_init__` already validates it). Authored:"
     | rows | `upkeep` | basis |
     |---|---|---|
     | dignity rows, by `dignity` 5, 4, 3, 2, 1 | 5, 3, 2, 1, 1 | `[ASSUMPTION; medium]`; sweep: flat 1 (H-158's shipped default) / linear 5..1 / the proposed |
     | `off_king` (what the seat pays a sworn person who holds no graded seat) | 1 | `default_upkeep`'s shipped value, now stated on the row |
     | every other row | absent | falls to `default_upkeep` as today |
     "Unit: units of the matter the paying `transfer` carries, per sworn person, per term (`upkeep_of`'s own stated limit, H-158). The bill of edit 4 names `default_store_kind`" (`coin` has no producer at build).
  2. Edit 2 is no edit: "`offices.yaml` seeds `obligees:` with 'no term (a seat seeded at world-gen has no opening act to declare one)', and that stands: the dukes' and the Grand Master's oaths are not stipendiary." The considered-and-refused `meta.sworn_term` is not written.
  3. Create `S/tests/test_inst_byz_b.py` (the source's named test) with `test_upkeep_rows_load_onto_the_office` (each authored row's `Office.upkeep` equals the table; an unauthored row reads `None` and `upkeep_of` returns `default_upkeep`) and `test_the_built_oaths_carry_no_term` (gate 1's second half: the four built `oblige` edges read `term None`), written before step 1 and read red on the first (the rows carry no `upkeep`).
- WHERE: `S/offices.yaml` (`seats[].upkeep` on the dignity rows and `off_king`); NEW `S/tests/test_inst_byz_b.py`.
- TESTS: the two above, in the new file, red then green as stated.
- FALSIFIER and CONTROL: "Plant `upkeep: 0` on the dignity rows: one unit pays everyone, and `upkeep_owed` is not read if the count renewed does not rise" (read at B33.02, where `upkeep_owed` exists). Control: the executed-verb tallies of `corpus_run` at seed 0 equal B32's close (`reading @<sha>`): no oath is termed at build and nothing reads the new values yet but `upkeep_of`, whose `off_king` value equals `default_upkeep`.
- GATE: `python -m pytest engine/season/tests/test_inst_byz_b.py -q` → pass; `build_realm(0)`'s content hash → the source says "proposal A's (this file adds no Tenure, Record or claim at build)"; read it and record it `[UNVERIFIED: whether `Office` field values enter `World.content_hash()` (`state/world.py::_encode_into`); if they do, the hash moves by the authored values and the move is this item's declared encoding mover, re-pinned at B33.99; the tallies stay equal either way]`.
- HASH MOVERS: the build hash, by values on a hashed carrier only, if `_encode_into` reaches `Office` (declared; B33.99). No behaviour.
- DEPENDS ON: EXISTS-IN-TREE `S/state/carriers.py::Office.upkeep`, `S/queries/world_q.py::upkeep_of`, `S/data/fixtures.py` `default_upkeep`, `default_store_kind`; V12 Batch B32 (`BYZ_A`'s `dignity` rows, `SYN_A` §3's `upkeep` refusal in `_load_offices`).
- GLOSSARY: row *upkeep* — its owner column points at `Office.upkeep` and `world_q.upkeep_of`; "upkeep": what a seat pays each man sworn to it per term, as a lord's keep of his household.
- COST and TIER: content edit; `sonnet`, `medium`.
- LANDS IT: B33's `valoria-author` producer, `isolation: worktree`; `Item: B33.01`, `[skip ci]`.

### B33.02 — what a sworn man is owed, read per person · BYZ_B edit 3 · BUILD · HASH MOVER(behaviour)
- SOURCE: BYZ_B "Exact edits" 3, "What it changes" 2, "Falsifier"; `SYN_A` §4 (`upkeep_owed` names BYZ_B edit 3 as its source); closes "`world_q.upkeep_of` is one amount per paying seat. A court pays by rank" (BYZ_B, the problem).
- ADVANCES: none of the nine; A-13.
- INSTRUCTION:
  0. Open the tree: `grep -n "def upkeep_owed" engine/season/queries/world_q.py`. If B32 landed it, record the reading and its body in the commit body and do step 2 only if `_renewals` does not yet call it.
  1. "`queries/world_q.py::upkeep_owed(w, seat_id, person_id) -> int` — new, beside `upkeep_of`: the maximum `Office.upkeep` over the seats `person_id` holds whose rung the paying seat's purview reaches and that declare one; else `upkeep_of(w, seat_id)`."
  2. "`_renewals` (`effects_economy.py`) replaces its `upkeep_of(seat)` apiece with `upkeep_owed(seat, obligee)`; its order (soonest-maturing first, ties by edge id) and its four clauses are unchanged."
- WHERE: `S/queries/world_q.py` (`upkeep_owed`, beside `upkeep_of`); `S/loop/effects_economy.py` (`_renewals`); `S/tests/test_inst_byz_b.py`.
- TESTS: in `test_inst_byz_b.py`, written before step 1 and read red (no `upkeep_owed`): `test_upkeep_owed_is_the_highest_grade_he_holds_under_the_payer` (a person holding a dignity-5 and a dignity-2 seat both under the payer's purview reads 5; one holding only a seat outside the purview reads `upkeep_of(payer)`) and `test_renewals_pay_by_grade` (a hand-built `transfer` of 6 from the paying rung renews a dignity-5 man's term and one ungraded man's, in soonest-maturing order) `[ASSUMPTION: test names; the item creates them (E-3)]`.
- FALSIFIER and CONTROL: "Plant `upkeep: 0` on the dignity rows: one unit pays everyone, and `upkeep_owed` is not read if the count renewed does not rise." Control: a world with no dignity-holder sworn to a paying seat renews exactly as before (`upkeep_owed` returns `upkeep_of` for every obligee).
- GATE: `python -m pytest engine/season/tests/test_inst_byz_b.py -q` → pass; the realm content hash at seed 0 after one season → recorded (equal to B33.01's reading where no sworn dignity-holder is paid; the source's mover class "a sworn dignity-holder is paid" is declared either way).
- HASH MOVERS: any run in which a sworn dignity-holder's term is renewed by a `transfer` (BYZ_B "Cost class"). Declared; B33.99.
- DEPENDS ON: EXISTS-IN-TREE `S/loop/effects_economy.py::_renewals`, `S/queries/world_q.py::upkeep_of`, `S/state/gate.py::purview_reaches`; V12 B33.01.
- GLOSSARY: none (*upkeep*'s owner column gains `world_q.upkeep_owed`, in B33.01's row).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B33's producer; `Item: B33.02`, `[skip ci]`.

### B33.03 — the bill, read when read · BYZ_B edit 4 · BUILD · HASH MOVER(behaviour)
- SOURCE: BYZ_B "Exact edits" 4, "What it changes" 3, "Gate" 4; C3-C7 (MATTER emits `term.matured` only), C3-N24; `14_VERBS_MATERIAL_B_stores.md` §4 ("BYZ_B's `world_q.bills_due(w, p)` reads it when read"); closes "nothing tells a seat-holder that terms sworn to his seat are falling due" (BYZ_B, the problem).
- ADVANCES: none of the nine; A-13 (the stipend has a payer).
- INSTRUCTION: "**`queries/world_q.py::bills_due(w, p)` — the bill, computed when read.** Beside `vacancies` (L-4) and `upkeep_owed`: for each office `p` holds with at least one live termed `oblige` whose term matures within `season` ticks, `bill = Σ upkeep_owed`; if `stores(seat rung, default_store_kind) < bill`, the stamp is the referent `(seat rung, "shortfall:<default_store_kind>", bill − stores)` on `p`'s question, read when read and stored nowhere. MATTER writes nothing for it (C3-C7; `write_matrix.yaml` gives MATTER no claim). `rosters.yaml: shortfall_sourced_operands` (`kind`, `amount`) then forms a `requisition` and a `transfer` from the stamped referent exactly as from a held shortfall claim (`verb_table.yaml: requisition.requires_typed_note`). `[UNVERIFIED: that `shortfall_sourced_operands` reads a stamped referent as it reads a held claim; if it reads only claims, the stamp's referent class is added to its reader, one line, in the same commit.]` `loop/matter.py` is not edited." The item's first step opens `shortfall_sourced_operands`' reader and records which branch it took. The stamp is wired where `vacancies` is stamped on a question (the same occasion site; `grep -n "vacancies(" engine/season` names it).
- WHERE: `S/queries/world_q.py` (`bills_due`); the occasion site that stamps `vacancies` (by symbol, as the grep names it); `S/rosters.yaml: shortfall_sourced_operands`' reader only if the `[UNVERIFIED]` branch needs it; `S/tests/test_inst_byz_b.py`.
- TESTS: `test_the_bill_is_read_not_written` (gate 4: after a season in which a bill fell due, no claim of predicate `shortfall:*` names the paying rung as written by MATTER, and `bills_due` returns the stamp) and `test_a_bill_forms_a_requisition_and_a_transfer` (a stamped referent forms both candidates for the holder), written before the edit and read red `[ASSUMPTION: test names (E-3)]`.
- FALSIFIER and CONTROL: "Empty the paying rung and withhold every `requisition`: every sworn term matures in season 4 and `world_q.establishment_of(off_king)` is empty in season 5. If the terms do not mature, MATTER is not reading them" — written here as a planted test at two seasons with the term set to mature in season 2 (four and five seasons in the source; A-114): `test_an_unpaid_court_lapses`. Control: with `oblige_term: None` (H-159's control arm) no oath carries a term and `bills_due` stamps nothing.
- GATE: `python -m pytest engine/season/tests/test_inst_byz_b.py -q` → pass; `git diff <batch-start-sha> -- engine/season/loop/matter.py` → empty.
- HASH MOVERS: any run in which a bill falls due (new `requisition` and `transfer` candidates). Declared; B33.99.
- DEPENDS ON: EXISTS-IN-TREE `S/queries/world_q.py::vacancies`, `S/rosters.yaml: shortfall_sourced_operands`, `S/data/fixtures.py` `default_store_kind`; V12 B33.02; V12 Batch B12c (`14_VERBS_MATERIAL_B` §2, §4: `transfer` and `requisition` drawn; B12c.12, B12c.13).
- GLOSSARY: row *bill* — new, "bill": what a seat owes its sworn men this season beyond what its rung holds, read when read, as a bill falls due; owner `world_q.bills_due`.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B33's producer; `Item: B33.03`, `[skip ci]`.

### B33.04 — a tax rendered is not a tax taken: `requisition`'s terms and bands · BYZ_B edit 5 · BUILD · HASH MOVER(behaviour)
- SOURCE: BYZ_B "Exact edits" 5, "Gate" 2; X-27; C3-Y7 and `unified/U2_LAYER1_CONFORMANCE.md` row 416 ("taken here: adopt"); `14_VERBS_MATERIAL_B_stores.md` §4 ("if the kind is adopted, BYZ_B's batch (B33) converts the row", "the move to shape (b) is made once"); rulings A-25, A-81; closes F-R4-02's BYZ_B half.
- ADVANCES: none of the nine; A-13, A-81.
- INSTRUCTION:
  1. Open `S/verb_table.yaml: requisition` as B12c.13 left it and record its `difficulty:` line, `emits:` and `emits_on_refusal:` in the commit body.
  2. **Request 1, adopted** (U2 row 416): "Overwhelming emits `requisition.rendered`, a kind **not** in `standing_routes.kinds.dominance` (a tax paid willingly is no sign of unrest), where MATERIAL-B's row emits `requisition.taken` at every carrying band." The row moves to shape (b), `contests: "a task"` (the shape B07 lands, `U5c_VERBS_residue_and_governance_owner` §1), once (MATERIAL_B §4: "made once, in the batch that adopts either the stake or `requisition.rendered` (whichever is first, B33 or the STORY_A batch B38)"), with these band cells:
     | band | moves (`graded_amount` on `task_fraction`) | emits |
     |---|---|---|
     | Overwhelming | the whole amount | `requisition.rendered` |
     | Success | the whole amount | `requisition.taken` |
     | Partial | half, at least 1 (Request 2; `graded_amount` already rounds up) | `requisition.taken`; "the rest is still owed and is read when read by `bills_due` (edit 4), not deposited by the effect" |
     | Failure | nothing | `requisition.resisted`, "which the place's people hold as a deed of the collector's" |
     `requisition.rendered` gets `KIND_VERB` `requisition` (one emitter) in `S/data/verbs.py`'s derivation, and no `standing_routes` membership.
  3. "**Terms, in the SC form** (C3-C10: what helps the collector is levels, nothing lowers the obstacle): obstacle `distance` (OBS member 20 …; D-U1-11k); `stakes` by the share asked (MATERIAL-B's); the place's `reception` toward the collector (the cohort's `regard`, hostile half). The collector's levels: `proofs` for a held assessment (a `faction_sheet` Record of the place's faction, from `survey`), and `obligation` where persons residing under the place are sworn to the exercised seat." Here: `distance` joins the row's `difficulty:` comment line and is measured from the actor's place to the requisitioned rung (UNDECIDED 1; the source's "hops from the exercised seat's rung" is not taken); `stakes` and the cohort's `regard` are already the row's (B12c.13) and are not added again; the `proofs` source on `requisition` reads a held `faction_sheet` Record of the place's faction; the `obligation` level is added by B33.34 (the source's `applies_to` gains `requisition`), not here.
  4. Withdrawn, not written: "the hunger band as `stakes`, the `copying` skill row, the `altonian_civics` step, and `procedure_draws`."
- WHERE: `S/verb_table.yaml` (`requisition`: `contests:`, band cells, the `difficulty:` comment); `S/loop/effects_governance.py::_eff_requisition` (dispatch on `res.degree` per the table; the file where B12c.13 left it, by symbol); `S/data/verbs.py` (the kind's verb); the `proofs` source's reader for `requisition` (`S/seam/wrappers/sigma.py`, beside the source's other readers); `S/tests/test_inst_byz_b.py`.
- TESTS: `test_requisition_draws_four_bands_and_conserves` (gate 2, below), written before step 2 and read red (one band only), and `test_rendered_is_not_dominance` (`requisition.rendered` is in no `standing_routes.kinds.dominance` list) `[ASSUMPTION: test names (E-3)]`.
- FALSIFIER and CONTROL: an Overwhelming collection counted by `person_q.stability` as a taking; a band that does not conserve the two rungs' sum. Control: "with `task_draw_arm: off` the full amount moves in every seed" (B07's control arm).
- GATE: "400 seeds, a hand-placed `requisition` of half a place's stores by a collector the place regards at zero: all four bands occur; conservation holds in every seed (the two rungs' sum is unchanged); with `task_draw_arm: off` the full amount moves in every seed" → `python -m pytest engine/season/tests/test_inst_byz_b.py -q` → pass (the test asserts `checked >= 400`). The realm's `requisition` counts by band at seeds 0 to 2, two seasons, read and quoted (BYZ_B gate 3's realm half; its scenario half is B40's, UNDECIDED 5). `opus` reads the band table.
- HASH MOVERS: "any run in which a `requisition` resolves" (BYZ_B "Cost class"). Declared; B33.99.
- DEPENDS ON: V12 Batch B12c (B12c.13: `requisition` drawn in shape (a), `requisition.resisted`, `Larder`); V12 Batch B07 (`task_draw_arm`, shape (b)); V12 Batch B05 (`proofs`, `distance` via B12c.12); V12 B33.03.
- GLOSSARY: row *rendered* — new, "rendered": a levy paid willingly in full, as a tax is rendered; owner `verb_table.yaml: requisition`'s Overwhelming cell; refused synonym "taken" for this sense.
- COST and TIER: build (a row's shape and its effect's dispatch); `sonnet`, `high`; the band table read by `opus`.
- LANDS IT: B33's producer; `Item: B33.04`, `[skip ci]`.

### B33.05 — a stage that names a body or a seat is a hand · BYZ_C edit 4, with edit 3's `hand_term` · BUILD · HASH EQUAL
- SOURCE: BYZ_C "Exact edits" 4 and the last sentence of 3, "What it changes" 1 and 4; `SYN_A` §2 (`office_bodies.<body>.term`), §3 (`passes_through`, `hand_term` refusals); rulings A-13, A-21; closes "`_declared_stages` … winds `record_stages_default` stages … They are clocks with no hand" (BYZ_C, the problem).
- ADVANCES: none of the nine; A-13 (the clerks an order passes).
- INSTRUCTION:
  0. Open the tree: `grep -n "passes_through\|hand_term" engine/season/state/carriers.py engine/season/data/rosters.py` and `grep -n "term" engine/season/rosters.yaml` under `office_bodies`. Record which of `Office.passes_through`, `Office.hand_term` and the `office_bodies.<body>.term` reader B32's `SYN_A` item landed. Where one is absent, add it here in `SYN_A` §3's form ("folded into the hashed representation only when present"; loader refusals: `passes_through` "a member that is neither an `office_bodies` name nor `{seat: <row id>}`", `hand_term` "not a positive int"; `office_bodies.term` an optional map body → seasons).
  1. "`loop/effects_information.py::_declared_stages` — when the act is exercised through a seat (`Act.via`) whose `Office` carries `passes_through`, and the act declares no stages: the stages are `[(due_i, "hand:<body or seat>", a.id)]`, with `due_i` the running sum of each hand's term from `w.tick`. Otherwise unchanged. The label prefix `hand:` is the one new convention; the tuple shape is unchanged, so `(Record, stages)`'s matrix row and `loop/matter.py`'s maturation read it as today."
  2. A hand's term: for a body, `rosters.yaml: office_bodies.term[<body>]`, "absent reads `fixtures: record_stage_term` (shipped 1)"; "Where the hand is a seat and not a body, the same number is the optional key `hand_term:` on that seat's own row".
  3. Create `S/tests/test_inst_byz_c.py` (the source's named test) with `test_a_writ_through_a_seat_with_hands_has_one_stage_per_hand` (a hand-built seat with `passes_through: ["Ministries", {seat: <id>}]`, `office_bodies.term` `{"Ministries": 2}` and the seat's `hand_term: 1`: the minted Record's stages are `[(tick + 2·T, "hand:Ministries", id), (tick + 3·T, "hand:<id>", id)]` with `T` the ticks of one term as `_declared_stages` already counts `record_stage_term`) and `test_no_hands_no_change` (a seat with no `passes_through` mints today's `stage1`, `stage2` labels), written before step 1 and read red on the first `[ASSUMPTION: test names (E-3)]`.
- WHERE: `S/loop/effects_information.py` (`_declared_stages`); `S/state/carriers.py` (`Office.passes_through`, `Office.hand_term`) and `S/data/rosters.py` (`_load_offices`; the `office_bodies` reader) only where step 0 finds them absent; NEW `S/tests/test_inst_byz_c.py`.
- TESTS: the two above, red then green.
- FALSIFIER and CONTROL: a stage labelled `hand:` on a writ through a seat that declares no `passes_through`. Control (BYZ_C "What it changes" 4): "With `passes_through` absent on every row … no stage is a hand, `carry` is offered as today, and every hash is the base hash" — no shipped row carries the key until B33.08.
- GATE: `python -m pytest engine/season/tests/test_inst_byz_c.py -q` → pass; the realm content hash at seed 0, one season → equal to B33.04's reading.
- HASH MOVERS: none (no row declares `passes_through` yet; an absent key is not folded into the hash).
- DEPENDS ON: EXISTS-IN-TREE `S/loop/effects_information.py::_declared_stages`, `S/data/fixtures.py` `record_stages_default`, `record_stage_term`; V12 Batch B32 (`SYN_A` §2, §3); V12 Batch B21 (`06_FA_decree_binds`: the writ's content deposit, A-21).
- GLOSSARY: row *hand* — new or narrowed, "hand": a clerk or office an order's paper must pass before it is sealed, as a document passes through hands; owner `_declared_stages`'s `hand:` label and `Office.passes_through`.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B33's producer; `Item: B33.05`, `[skip ci]`.

### B33.06 — the clerk is asked; an unentered stage reads as returned · BYZ_C edits 6–7 · BUILD · HASH EQUAL
- SOURCE: BYZ_C "Exact edits" 6 and 7, "What it changes" 3; C3-C7; A-21; `SYN_A` §4 (`hands_open` from BYZ_C edit 7).
- ADVANCES: none of the nine; A-13.
- INSTRUCTION:
  0. Open the tree: `grep -n "def hands_open\|def hand_returned" engine/season/queries/world_q.py`; record what B32 landed; write only what is absent.
  1. Edit 7: "`queries/world_q.py` — `writs_held` (or FA's `writs_addressed`) is **not** narrowed (A-21: an addressee answers what he has learned was issued); a new occasion beside `vacancies` and `sittings_before`, `hands_open(w, p)`: the Records with an open stage naming a body or seat `p` holds, as `Record` referents of a `need` question. This is the reach half: without it a clerk is never asked. `[UNVERIFIED]` how the question slot ranks it (`question_aggregation_rule: first`; H-54 is CORE's)." Wire it at the occasion site `vacancies` and `sittings_before` stamp (by symbol); record in the commit body how the slot ranks it.
  2. Edit 6: "An unentered `hand:` stage whose due has passed reads as **returned by the clock** when read (`world_q.hand_returned(w, record)`, beside `hands_open`; nothing stored); MATTER emits `term.matured` for the Record as today and writes `Record.stages` nowhere; WITNESS deposits the `term.matured` to the maker, from which he reads the return. Later hands' stages are read as void once an earlier one has returned. The maker's next `issue` is a new document." `loop/matter.py` is not edited (C3-C7).
- WHERE: `S/queries/world_q.py` (`hands_open`, `hand_returned`, beside `vacancies`); the occasion site that stamps `vacancies` (by symbol); `S/tests/test_inst_byz_c.py`.
- TESTS: `test_hands_open_lists_a_clerk_s_open_documents` (a holder of a `Ministries` seat reads the Record whose open stage names `Ministries`; a holder of no such seat reads `()`), `test_a_stage_past_due_reads_returned_and_later_hands_void`, `test_matter_writes_no_stage` (after the due tick passes through a season, `Record.stages` is byte-equal to the mint's), written before the edits and read red `[ASSUMPTION: test names (E-3)]`.
- FALSIFIER and CONTROL: "Remove `hands_open`: the count of `carry` attempts on writs falls to zero, which shows the occasion, not the mechanism, is what reach depends on" (read at B33.08's realm reading). Control: no Record carries a `hand:` stage in the shipped world, so both readers return empty.
- GATE: `python -m pytest engine/season/tests/test_inst_byz_c.py -q` → pass; `git diff <batch-start-sha> -- engine/season/loop/matter.py` → empty.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `S/queries/world_q.py::vacancies`, `::sittings_before`, `::writs_held`; V12 B33.05.
- GLOSSARY: none (*hand*, B33.05).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B33's producer; `Item: B33.06`, `[skip ci]`.

### B33.07 — `carry` at a hand, drawn · BYZ_C edit 5 · BUILD · HASH EQUAL
- SOURCE: BYZ_C "Exact edits" 5 and its two tables, "Gate" 1, "Falsifier" first sentence; X-14, X-24, X-25 (its first `Reconciled:` line: "the hand is that row's second `requires_typed` alternative, with the same band shape"); C3-C10; A-21, A-30, A-81.
- ADVANCES: none of the nine; A-13.
- INSTRUCTION:
  0. Open `S/verb_table.yaml: carry` as B28 (`14_VERBS_SOCIAL1_D`) left it and record its `requires_typed`, `contests:` and bands in the commit body.
  1. "`requires_typed` gains a second alternative: `existence` of `subject` kind `Record` with an open `hand:` stage, and `basis` of `subject`, basis `hand` (new basis rule in `data/requires.py`: the actor holds a live seat that is the stage's named seat, or whose `body` is its named body, and the document was drawn up at a rung the issuing seat's purview reaches). The petition alternative stands." `hand` joins the closed basis vocabulary in `S/data/requires.py` (the tuple beside `"purview"`, `"bench"`).
  2. "`counterparty:` absent; `contests: a matter`; the draw." Terms on that alternative, through the one composer:
     | term | reads |
     |---|---|
     | pool | the row owner's (`14_VERBS_SOCIAL1_D`): the one pool rule on the clerk's skill score for `carry`'s skill |
     | `difficulty` | by the rung kind of the issuing seat's rung (a realm instrument is harder to enter than a town's) |
     | `backlog` (OBS member 23) | the open documents in the clerk's hands beyond his scene budget this season |
     | `subject` (OBS member 4) | the document's `forgery_quality`, as an inquiry reads it (`seam/wrappers/sigma.py::contest_input`) |
     | `regard` (OBS member 7) | the clerk's hostility to the maker (hostile half) |
     | levels (leverage, C3-C10) | `favour` for the clerk's regard for the maker above zero; `obligation` where the maker and the clerk are sworn to one seat (read by B33.34's source once it lands) |
  3. Bands on the hand alternative (the three kinds are asked of the row's owner for a document that is not a petition):
     | degree | writes | emits |
     |---|---|---|
     | Overwhelming | the stage entered; the next hand's due tick brought forward by half its term | `document.entered` |
     | Success | the stage entered | `document.entered` |
     | Partial | the stage's due tick re-wound by one term of that hand, once per document per hand | `document.held` |
     | Failure | the stage closed as `returned` (an ACTS write at RES, `(Record, stages)`, as `carry` already holds) | `document.returned` (the clerk its doer; WITNESS deposits `(record, document.returned, True)` to the maker) |
     "On the entry that closes the last `hand:` stage the instrument is **entered**: from that tick it is sealed and citable … The addressees' answers (`comply`, `evade / defy`, `construe`) do **not** wait on it" (A-21). The draw key is `H(w.world_seed, w.tick, <record id>, "carry.hand")` (A-30).
  4. "`write_matrix.yaml`: `(Record, stages)` already lists `carry` at RES; its `emits:` gains the three kinds. `[UNVERIFIED]` the row's present `emits:` list" — record it in the commit body before the edit.
- WHERE: `S/verb_table.yaml` (`carry`: the second `requires_typed` alternative, its terms and bands); `S/data/requires.py` (the basis `hand`); `S/loop/effects_information.py` (`carry`'s effect at a hand, by symbol); `S/data/verbs.py` (the three kinds' verb); `S/write_matrix.yaml` (`(Record, stages)` `emits:`); `S/tests/test_inst_byz_c.py`.
- TESTS: `test_carry_at_a_hand_draws_four_bands` (gate 1), `test_patronage_moves_the_entry_rate` (the falsifier), `test_a_petition_carry_is_unchanged`, written before step 1 and read red `[ASSUMPTION: test names (E-3)]`.
- FALSIFIER and CONTROL: "Give the Clerk a `regard` of the maximum for one maker and the minimum for another, identical documents, 400 seeds each: the entry rates differ. If they do not, patronage is not in the odds." Control: a `carry` of a petition draws as B28 left it (same bands, same kinds).
- GATE: "400 seeds, one hand-placed `carry` by the Clerk on a King's writ: all four bands occur; with the roll pinned to Success, every seed enters" → `python -m pytest engine/season/tests/test_inst_byz_c.py -q` → pass (`checked >= 400` asserted); `opus` reads the terms on the contested alternative.
- HASH MOVERS: none (no Record carries a `hand:` stage until B33.08).
- DEPENDS ON: V12 Batch B28 (`14_VERBS_SOCIAL1_D`: `carry`'s row and band shape; `14_VERBS_SOCIAL1_B`); V12 Batch B05 (the composer, members 4, 7, 23; `favour`); V12 Batch B07 (`13_SC_draw_for_unrolled_contests`); V12 B33.06; EXISTS-IN-TREE `S/data/requires.py` (the basis tuple), `S/seam/wrappers/sigma.py::contest_input`.
- GLOSSARY: rows *entered* (new: "entered": a paper sealed into the record by the last clerk it must pass, as a deed is entered in a register; owner `document.entered`) and *held over* (new: "held": a paper kept back a term at a hand; owner `document.held`).
- COST and TIER: build (a contested alternative); `sonnet`, `high`; the terms `opus` (BYZ_C's tier line).
- LANDS IT: B33's producer; `Item: B33.07`, `[skip ci]`.

### B33.08 — the King's and two dukes' papers pass their clerks · BYZ_C edits 1–3 · BUILD · HASH MOVER(behaviour)
- SOURCE: BYZ_C "Exact edits" 1, 2, 3, "Gate" 2, 3, "Falsifier" second sentence; A-13, A-21.
- ADVANCES: none of the nine; A-13; NPC-008, NPC-009, NPC-011's cases (BYZ_C, the problem).
- INSTRUCTION:
  1. "`offices.yaml: seats[].passes_through` — optional list; each member an `office_bodies` name or a seat id (`{seat: <id>}`). Order is the order of entry. Authored:"
     | row | `passes_through` | basis |
     |---|---|---|
     | `off_king`, `off_duke_valorsmark` | `["Ministries"]` | `worldbuilding_v30.md` §6.1: the Ministries "execute government services" |
     | `off_duchess_hafenmark` | `["Inner Council"]` | Hafenmark's "institutional order" (`geography_v30_infill.md:18`); her council holds the Legal Advisor `[ASSUMPTION; medium]` |
     | `off_duke_varfell`, every Jarl seat | absent | "first among the Jarls, not a monarch" |
     | Church seats | absent | the papacy lane's |
     | `off_katepano` | absent | a frontier command acts on its own seal |
  2. "`offices.yaml: off_lord_steward.body` — `null` → `"Ministries"` `[ASSUMPTION; medium; Jordan to correct; revert: null]`. Ground: `cases/NPC4.yaml` NPC-009 … With it the Ministries hold two seats, and the case's concentration is measurable as his share of entries."
  3. "`rosters.yaml: office_bodies.term` — new optional map, body → seasons a document may wait for that body; absent reads `fixtures: record_stage_term` (shipped 1). Authored: `"Ministries": 2` `[ASSUMPTION; medium]`; sweep 1 / 2 / 4."
- WHERE: `S/offices.yaml` (`off_king`, `off_duke_valorsmark`, `off_duchess_hafenmark`: `passes_through`; `off_lord_steward`: `body`); `S/rosters.yaml` (`office_bodies.term`); `S/tests/test_inst_byz_c.py`.
- TESTS: `test_no_deadlock_when_the_clerks_are_vacant` (gate 3, below), written before the edit and read red (no row has a hand) `[ASSUMPTION: test name (E-3)]`.
- FALSIFIER and CONTROL: the falsifier of B33.06 ("Remove `hands_open`: the count of `carry` attempts on writs falls to zero"), read here at seed 0, two seasons. Control: "`passes_through` deleted from every row reproduces FA's post-P2 hash", read as B33.07's realm hash (`reading @<sha>`).
- GATE: gate 2 at two seasons (four in the source; A-114): realm, seeds 0 to 9, two seasons, `PYTHONHASHSEED=0`: "of the writs issued through `off_king`, the counts entered, held over, returned by a clerk, and returned by the clock (read), per seed; at least one writ is entered and at least one is not, across the seeds; an addressee's answer forms on an unentered writ (A-21); the Lord Steward's share of entries reported" — the counts quoted in the commit body, the two "at least one" clauses and the A-21 clause asserted with `checked >= 10` seeds. Gate 3: "The same run with both Ministries seats vacated at tick 0: the season completes, every King's writ returns by the clock, and `off_duke_varfell`'s writs are unaffected" → `python -m pytest engine/season/tests/test_inst_byz_c.py -q` → pass, every King's writ whose due has passed by the end of season 2 reading returned.
- HASH MOVERS: "any run in which a seat with `passes_through` issues" (BYZ_C "Cost class"); the build hash, by the new key on three Offices and `off_lord_steward`'s body. Declared; B33.99.
- DEPENDS ON: V12 B33.05, B33.06, B33.07; EXISTS-IN-TREE `S/offices.yaml` rows `off_king`, `off_duke_valorsmark`, `off_duchess_hafenmark`, `off_lord_steward`; `S/rosters.yaml: office_bodies` (`Ministries`, `Inner Council`).
- GLOSSARY: none (*hand*, B33.05).
- COST and TIER: content edit; `sonnet`, `medium`; the realm reading `sonnet`, `high`.
- LANDS IT: B33's producer; `Item: B33.08`, `[skip ci]`.

### B33.09 — the centre beyond the map: a place and a person · BYZ_D edits 1–2, COL_B §4 bullets 1 and 3 · CONTENT · HASH MOVER(encoding)
- SOURCE: BYZ_D "Exact edits" 1, 2, "What it changes" 1; COL_B §4 (the `capital` bullet and the registry bullet); X-13; A-44 (authored content outside the generated cap), `ED-WR-0011`; `audits/12_ARCS_adjudication.md:368` (row 12, "generate a person").
- ADVANCES: none of the nine; NPC-011's need 4, NPC-089's need 6, ARC-45 (BYZ_D, the problem).
- INSTRUCTION:
  1. "`references/npc_registry.yaml` — one row, `status: proposed`, the next free NPC id (allocated at landing from `references/id_reservations.yaml`'s `next_free`, CLAUDE.md §4, not here and not by max+1 …). Authored content outside A-44's generated cap (`ED-WR-0011`); U1 counts it: faction `Altonia`; role `[PLACEHOLDER] head of the imperial centre`; `cultural_label: altonian_imperial`; `affiliations: {solmund_orthodoxy: 1, einhir_restoration: 1, altonian_civics: 5}`; pursuits led by `stability` and `reputation` `[ASSUMPTION; medium; Jordan to author]`. No name is proposed." COL_B adds: "the fifteen pursuits and the three concern affiliations as `data/cast.py` requires, `status: proposed` `[ASSUMPTION; whole row]`". The id: the NPC block B00 gives this batch (UNDECIDED 3); if B00 gave none, read the registry's highest id on `main` at landing, take the next, and land that row on `main` before any other session cites it; record the reading in the commit body.
  2. "`rosters.yaml: foreign_cast.by_faction."Altonia"` — add `centre: {code: "ALT-0"}`, a second settlement under `ALT`. `[UNVERIFIED]` which keys `build_realm(foreign=)` reads off this mapping (`data/rosters.py::FOREIGN_CAST`); the reader gains the key." With COL_B's distance declared on the same key (UNDECIDED 4): `centre: {code: "ALT-0", hops: 3}` (`hops` "[ASSUMPTION; the code and the 3; Jordan names the place; sweep {1, 3, 5}]"), read by B33.14. The builder (`S/boot/realm.py::build_realm`, B03c's home of `populated.py`'s builder) mints the settlement under the `ALT` root in the foreign arm only, and homes the new person there ("The holder **resides at `ALT-0`**", COL_B §4).
  3. "`faction_leaders."Altonia"` moves from NPC-089 to the new person; `factions.head_seat` gains `"Altonia": off_altonian_court`" — the seat is B33.10's, so this key lands in B33.10's commit, not here; `faction_leaders` moves here.
  4. Create `S/tests/test_inst_byz_d.py` (the source's named test) with `test_the_control_arm_has_no_empire` (gate 1: `build_realm(0, foreign=False)`'s content hash equals B33.08's reading) and `test_the_centre_is_a_settlement_under_alt_and_its_holder_lives_there` (foreign arm), written before step 2 and read red on the second `[ASSUMPTION: test names (E-3)]`.
- WHERE: `references/npc_registry.yaml` (one row); `S/rosters.yaml` (`foreign_cast.by_faction."Altonia".centre`; `faction_leaders."Altonia"`); `S/data/rosters.py` (`FOREIGN_CAST`'s reader); `S/boot/realm.py` (`build_realm(foreign=True)`: the second settlement and the person's home); NEW `S/tests/test_inst_byz_d.py`.
- TESTS: the two above.
- FALSIFIER and CONTROL: the control arm's hash moves (the centre leaked into `foreign=False`). Control: gate 1, "`build_realm(0, foreign=False)`: `content_hash` unchanged".
- GATE: `python -m pytest engine/season/tests/test_inst_byz_d.py -q` → pass; `python tools/validate_ed_citations.py` → exit 0 (the registry row cites nothing new); the foreign-arm build hash at seed 0 → moved, recorded for B33.99.
- HASH MOVERS: "the foreign-arm build hash" (BYZ_D "Cost class"): one Person, one Rung. Declared; B33.99.
- DEPENDS ON: EXISTS-IN-TREE `S/rosters.yaml: foreign_cast.by_faction."Altonia"` (`territory: {code: "ALT"}`, `settlement: {code: "ALT-1"}`), `faction_leaders`, `S/data/rosters.py::FOREIGN_CAST`, `references/npc_registry.yaml` (last row NPC-090); V12 Batch B03c (`boot/realm.py`); V12 B33.08.
- GLOSSARY: none (`[PLACEHOLDER]` posts are not words; the place has a code and no name, as the `foreign_cast` note states).
- NAMES: `harness/populated.py::build_realm` → `S/boot/realm.py::build_realm` (§5.10, B03c).
- IDS: NPC 1 (UNDECIDED 3).
- COST and TIER: content; `sonnet`, `medium`; the person's row is listed in the PR body for Jordan to author.
- LANDS IT: B33's producer; `Item: B33.09`, `[skip ci]`.

### B33.10 — the court's seat and the Doux's; the empire may recall its officers · BYZ_D edit 3, COL_B §4 bullet 2 · BUILD · HASH MOVER(encoding)
- SOURCE: BYZ_D "Exact edits" 3, "What it changes" 1 and 3, "Gate" 4; COL_B §4's seat bullet (its comment: "one seat, shared with BYZANTINE-D (whose row text governs)"); X-13; A-22 (BYZ_D's U5d line); closes "`offices.yaml`: two Altonian seats, both `conferral: null`, `revocation: null`".
- ADVANCES: none of the nine; A-22 (the far superior commands its sworn men and the holders of seats it may revoke).
- INSTRUCTION:
  1. `S/offices.yaml: foreign_seats`, two rows added (BYZ_D's text, which governs):
     ```yaml
       - id:         off_altonian_court        # X-13: the one far superior, shared with COLONIAL-B §4
         post:       "[PLACEHOLDER] head of the imperial centre"
         rung:       {territory: "ALT"}         # the parent rung of ALT-1; its holder resides at ALT-0 (hops: 3)
         body:       null
         faction:    "Altonia"
         remit_acts: [issue, confer, revoke]
         conferral:  null
         revocation: null
         passes_through: [{seat: off_doux}]
         holder:     "<the new NPC id>"
         obligees:   ["NPC-089", "NPC-090", "NPC-011"]
         source:     "ARCS adjudication row 12; cases/exercises/NPC-011.yaml ('the Altonian imperial authority')"
         note:       "[NEW]. No `dispatch`: the centre does not march; its governors do."

       - id:         off_doux
         post:       "Doux"
         rung:       {settlement: "ALT-1"}
         body:       null
         faction:    "Altonia"
         remit_acts: []
         conferral:  appointed
         revocation: rung_above_same_faction
         holder:     "NPC-011"
         obligees:   []
         source:     "references/npc_registry.yaml NPC-011 (`title: Doux`; goals: 'Sandbag imperial directives')"
         note:       "[NEW]. Seated at the staging post beside the Katepano [ASSUMPTION; medium; Jordan to place him: his province is off the map]. An empty remit: in this world his power is the hand."
     ```
     `<the new NPC id>` is B33.09's.
  2. "On `off_katepano` and `off_kommerkiarios`: `conferral: null` → `appointed`; `revocation: null` → `rung_above_same_faction`. The court is anchored at `{territory: "ALT"}`, the parent rung of `ALT-1`, so `seated_on_the_rung_above` finds it from either seat's rung; a settlement anchor at `ALT-0` would have been a **sibling** and failed."
  3. `S/rosters.yaml: factions.head_seat` gains `"Altonia": off_altonian_court` (BYZ_D edit 2's last clause; COL_B §4).
  4. `test_inst_byz_d.py` gains `test_the_court_may_recall_the_katepano` (gate 4), written before step 2 and read red (`revocation: null` refuses).
- WHERE: `S/offices.yaml` (`foreign_seats`: `off_altonian_court`, `off_doux` added; `off_katepano`, `off_kommerkiarios` edited); `S/rosters.yaml` (`factions.head_seat`); `S/tests/test_inst_byz_d.py`.
- TESTS: the one above; `test_the_control_arm_has_no_empire` (B33.09) stays green.
- FALSIFIER and CONTROL: "Delete `passes_through` from the court's row: every instrument is entered at issue and gate 2's lag is zero" (read at B33.11). Control: B33.09's control-arm test.
- GATE: gate 4, "A hand-placed `revoke` of `off_katepano` through `off_altonian_court`: admitted at eligibility (it is refused today: `revocation: null`); its bands are proposal E's" → `python -m pytest engine/season/tests/test_inst_byz_d.py -q` → pass; `queries/faction_q.py::head` (or the reader `factions.head_seat` feeds) names the court's holder for Altonia.
- HASH MOVERS: the foreign-arm build hash (two Offices, two edited rows, NPC-011 seated). Declared; B33.99.
- DEPENDS ON: EXISTS-IN-TREE `S/offices.yaml` rows `off_katepano`, `off_kommerkiarios`, `S/state/gate.py::seated_on_the_rung_above`, `REVOCATION_RULES["rung_above_same_faction"]`, `S/rosters.yaml: factions.head_seat`; V12 B33.09; V12 B33.05 (`passes_through` on a seat hand); V12 Batch B32 (`BYZ_E`'s recall bands, "proposal E").
- GLOSSARY: none.
- COST and TIER: content and a small build; `sonnet`, `high` (BYZ_D's tier line).
- LANDS IT: B33's producer; `Item: B33.10`, `[skip ci]`.

### B33.11 — distance at a hand: the Doux's term and the trade gate's keeper · BYZ_D edits 4–5 · BUILD · HASH MOVER(behaviour)
- SOURCE: BYZ_D "Exact edits" 4, 5, "What it changes" 2, "Gate" 2, 3; A-21.
- ADVANCES: none of the nine; NPC-011 need 4; NPC-090's case (BYZ_D, the problem).
- INSTRUCTION:
  1. Edit 4: "`hand_term:` on the row that **is** the hand (`off_doux: hand_term: 2`), seasons a document may wait for that seat. Sweep 1 / 2 / 4. A writ of the court's is thus entered (sealed, citable) two or more seasons after it is written, or returned; its terms are known to whoever learns of its issue from the start (A-21)." (B33.05 reads the key.)
  2. Edit 5: "`offices.yaml: off_kommerkiarios` gains `hand_term: 1`, and the realm's trade seat that faces him names him as a hand on its instruments across the gate: `off_guild_comptroller: passes_through: [{seat: off_kommerkiarios}]` `[ASSUMPTION; medium]` (NPC-007, 'Guilds Representative'; the registry's named counterparty, 'Solberg', has no seat and is content debt)." No new rule.
  3. **STOPS IF** (UNDECIDED 10): with step 2's `off_guild_comptroller` key in, `build_realm(0, foreign=False)`'s content hash differs from B33.10's control reading, or the loader refuses a `{seat:}` member naming a seat the control arm does not build. Then the `off_guild_comptroller` key is not landed, the commit body says so, and the PR body lists it for Jordan (it is `[ASSUMPTION; medium]` in its source).
  4. `test_inst_byz_d.py` gains `test_the_prince_s_regard_moves_his_hand` (gate 3, below) `[ASSUMPTION: test name (E-3)]`.
- WHERE: `S/offices.yaml` (`off_doux.hand_term`; `off_kommerkiarios.hand_term`; `off_guild_comptroller.passes_through`); `S/tests/test_inst_byz_d.py`.
- TESTS: the one above.
- FALSIFIER and CONTROL: "Delete `passes_through` from the court's row: every instrument is entered at issue and gate 2's lag is zero. Set the Doux's `altonian_civics` to 5 and his stance toward everyone to zero: his entry rate rises toward the Katepano's own compliance rate; if it does not, the affiliation is not in the odds." Control: gate 3's "planted control with the stance row toward an unrelated person shows no difference".
- GATE: gate 2 at two seasons (six in the source; A-114): "Foreign arm, seeds 0 to 19 …: the court's instruments issued; at the Doux's hand, the counts entered, held over, returned by him and returned by the clock (read when read, BYZANTINE-C edit 6); the lag in ticks from issue to entry for those entered. All of entered and not-entered occur across the seeds" — quoted, the last clause asserted (`checked >= 20`); at two seasons with `hand_term: 2` an issue in season 1 cannot be past due, so "returned by the clock" may read 0 and is reported, not asserted. Gate 3: "The same run in two arms differing only in the Doux's stance row toward NPC-030 (Elske): his entry rate differs between the arms … A planted control with the stance row toward an unrelated person shows no difference" → a hand-built 400-seed `carry` pair in `test_inst_byz_d.py` (the realm pair at two seasons is quoted beside it); `opus` reads gate 3 (BYZ_D's tier line).
- HASH MOVERS: the foreign-arm runs in which the court issues; the realm runs in which `off_guild_comptroller` issues (if step 2 lands). Declared; B33.99.
- DEPENDS ON: V12 B33.05, B33.07, B33.10; EXISTS-IN-TREE `S/offices.yaml` rows `off_kommerkiarios`, `off_guild_comptroller`.
- GLOSSARY: none.
- COST and TIER: small build (content keys); `sonnet`, `high`; gate 3 `opus`.
- LANDS IT: B33's producer; `Item: B33.11`, `[skip ci]`.

### B33.12 — an order defied scars a holder of `altonian_civics` · BYZ_D edit 7 · CONTENT · HASH MOVER(behaviour)
- SOURCE: BYZ_D "Exact edits" 7, "What it changes" 4; NPC-090's case need (BYZ_D, the problem).
- ADVANCES: none of the nine; NPC-090's anticipable strictness.
- INSTRUCTION: "`rosters.yaml: tables.affiliation_engagement` — a column `altonian_civics`, sign cells:"
  ```yaml
        altonian_civics:
          "evade / defy":  -1
          destroy_record:  -1
          forge:           -1
          comply:           1
          carry:            1
  ```
  "`[ASSUMPTION; medium; Jordan to correct]`. `[UNVERIFIED]` that none of these five verbs carries a cell in the shared column `sacred` (`data/affiliations.py::_load_engagement` refuses a verb with both); a verb that does is dropped from this column." The item's first step reads the `sacred` column and records which, if any, of the five it drops. "Its one reader today is the scar (`person_q.elements_violated_by`): a holder who sees an order defied takes a count on `altonian_civics`."
- WHERE: `S/rosters.yaml` (`tables.affiliation_engagement`: the `altonian_civics` column); `S/tests/test_inst_byz_d.py`.
- TESTS: `test_a_civics_holder_who_sees_defiance_is_scarred` (a hand-built observer at `altonian_civics: 4` witnessing an `evade / defy` takes a count; one at 0 does not) `[ASSUMPTION: test name (E-3)]`, red before the edit.
- FALSIFIER and CONTROL: the loader accepts a verb carrying both a `sacred` and an `altonian_civics` cell. Control: an observer holding no `altonian_civics` is scarred as before.
- GATE: `python -m pytest engine/season/tests/test_inst_byz_d.py -q` → pass; `python -c "from engine.season.data import affiliations"` → loads (the engagement loader's refusal is its check).
- HASH MOVERS: every seeded run in which a holder of `altonian_civics` above 0 witnesses one of the five verbs. Declared; B33.99.
- DEPENDS ON: EXISTS-IN-TREE `S/rosters.yaml: tables.affiliation_engagement`, `S/data/affiliations.py::_load_engagement`, `S/queries/person_q.py::elements_violated_by`; V12 B33.10.
- GLOSSARY: none.
- COST and TIER: content; `sonnet`, `medium`.
- LANDS IT: B33's producer; `Item: B33.12`, `[skip ci]`.

### B33.13 — the tutoring demand is a covenant held at the hand · BYZ_D edit 6 · POINTER
Edit 6 adds nothing: "The head's demand is a `covenant` offer addressed to the King … Minted through `off_altonian_court`, it carries the Doux's hand like any instrument of that seat. A covenant stays in person (A-21 …), so while he holds it over or returns it, the King holds no claim of it. Nothing is added for the arc: the suppression is a person's act at a hand." What carries it: the hand (B33.05 to B33.07, B33.10, B33.11) and `covenant` as CP-T09-03 makes something read it (Batch B21b, the intake `:244`). A dispatched order from the court waits on `_eff_dispatch` (`IS-B3-FA-05`, B21, `V12_STRUCTURE_part2.md` §5.7), which BYZ_D says the court does not use ("No `dispatch`"). Gate: none of its own and no commit; B33.11's gate 2 counts every instrument the court mints at the Doux's hand, a `covenant` offer among them where one forms, and the close's commit body quotes how many offers did.
