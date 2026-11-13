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
GATE: Batch B21d-fa-arc   (added by H2: `H2_DECISIONS.md` HD-13, CR-88's duty decline; no wave moves; `workplan_v12_part2.md` §1)
GATE: Batch B21s-strife-supply   (added by H2: `H2_DECISIONS.md` HD-14, PAP-D extends the CH row; no wave moves)
HASH READING: `PYTHONHASHSEED=0 python -c "import sys; from engine.season.boot.realm import build_realm; from engine.season.harness.populated import run; s, k = int(sys.argv[1]), int(sys.argv[2]); w = build_realm(s); run(k, s, w=w); print(w.content_hash())" <s> <k>` → the realm content hash at seed `<s>` after `<k>` seasons: `<k>` = 1, one season, unless the gate names two (never more before B99, D-17); `<k>` = 0 reads the build hash; per item `<s>` = 0 (a mover's reading, E-2), at `.99` `<s>` = 0, 1, 2; each value quoted `reading @<sha>`, the tree it was read on (`workplan_v12.md` §3.B, "the hash reading").
REQUIREMENT: none — A-12, A-13, A-14 (`V12_STRUCTURE.md` §2.2's B33 row): the seat facts and the economy of the institutions kit (upkeep by grade, the hands an order passes, the audit at a term's end, the debt, the obligation that moves odds, the Church's sentence by other people's answers). No conjunct of R-01 to R-09 is moved; the close re-reads the nine and prints their held counts (`IS-A-12`).
BATCH GATE (read once, on the closing tree, `PYTHONHASHSEED=0` on every seeded command; no command past two seasons, D-17):
  `python -m pytest engine/season/tests/test_inst_byz_b.py engine/season/tests/test_inst_byz_c.py engine/season/tests/test_inst_byz_d.py engine/season/tests/test_remove.py engine/season/tests/test_audit_and_charter.py engine/season/tests/test_inst_col_d_ledger.py engine/season/tests/test_inst_pap_c.py engine/season/tests/test_inst_pap_d.py engine/season/tests/test_inst_pap_e.py engine/season/tests/test_inst_ven_a.py engine/season/tests/test_inst_ven_b.py engine/season/tests/test_inst_ven_d.py engine/season/tests/test_inst_syn_c_crossings.py -q` → all pass (every file is created by an item of this batch; each item names its own);
  the controls, each a reading of B32's close (`reading @<sha>`): `build_realm(0, foreign=False)`'s content hash → equal except where B33.01, B33.08, B33.21, B33.31 and B33.40 declare a build mover (each named in the re-pin commit); every fixture this batch adds at its shipped control (`obligation_level: None`, `penance_weight: 0`, `credit_terms` flat 1.0) and every new arrangement row undocketed → the realm content hash after one and two seasons at seeds 0, 1, 2 equal to the value the re-pin records, and the executed-verb tallies of `python -m engine.season.harness.corpus_run --seasons 2` [v12: two seasons a case, D-17; the case's own span, to `MAX_SEASONS`, is B99's] at seed 0 read and quoted beside B32's (`reading @<sha>`), every moved tally attributed to a declared mover;
  `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`) (the batch's NUMBER rows, `IDS:`); `python -m engine.season.harness.register --requirements` → nine lines; `python tools/m1_acceptance.py --summary` → its verdict line quoted;
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
  `stakes_ob.debt` = `off` (the reading "amount ÷ the asked rung's stores of that kind, capped at 2", `audits/15_INSTITUTIONS_VENICE.md` §8: sweep {off, on}, control off; B33.38); set by B98; target: none stated, `BLOCKED (design: no target reading)` ·
  `goal_church_liberties_kept` shipped off (written commented out, B33.24); set by no batch until `data/goals.py`'s owner builds a place filter for `deed_doers` (PAP_C: "requested, not built here"), `BLOCKED (design: no carrier)` ·
  inherited, not set here: `distance_step` (B12c's), `presumption_gain` = 0 (B32's `SYN_B`; B33.22 reads it planted at 0.5 in a test only).
C(B33-inst-economy-hands): this batch's entries; the plan's head parts; `unified/U1_GLOSSARY.md` rows *upkeep*, *hand*, *distance*, *audit*, *consecration*, *excused*, *obligation*, *debt*, *sworn*, *roll*;
  `S/offices.yaml`; `S/rosters.yaml` (`office_bodies`, `foreign_cast`, `faction_leaders`, `factions.head_seat`, `successions`, `endings`, `record_kinds`, `record_sourced_operands`, `shortfall_sourced_operands`, `advantage_sources`, `alignment`, `tables`); `S/verb_table.yaml` (`carry`, `requisition`, `determine`, `revoke`, `issue`); `S/arrangements.yaml`; `S/goals.yaml`; `S/instruments.yaml` (B32); `S/write_matrix.yaml`; `S/hole_register.yaml`; `S/venues.yaml`; `S/harness/strife_moves.yaml`; `references/npc_registry.yaml`;
  `S/state/carriers.py` (`Office`); `S/state/containment.py` (`ancestry`); `S/state/gate.py` (`sworn_to`, `purview_reaches`, `seated_on_the_rung_above`, `REVOCATION_RULES`, `may_determine`, `sits_over`); `S/queries/world_q.py`; `S/queries/person_q.py`; `S/queries/inputs.py` (`SocialContestInput`); `S/seam/wrappers/sigma.py` (`contest_input`, `ADVANTAGE_SOURCES`); `modules/social_contest/roll.py` (`obstacle`); `S/data/fixtures.py`; `S/data/rosters.py` (`_load_offices`, `FOREIGN_CAST`); `S/data/requires.py`; `S/data/verbs.py` (`_derive_kind_verb`); `S/data/affiliations.py` (`_load_engagement`); `S/data/geography.py` (`adjacent_territories`, `geography`); `S/loop/effects_economy.py` (`_renewals`, `_eff_transfer`); `S/loop/effects_governance.py` (`_eff_requisition`, `_eff_revoke`); `S/loop/effects_information.py` (`_declared_stages`, `_mint_document`, `_eff_covenant`, `_eff_determine`, `_disposal`); `S/epistemic.py` (the reach predicate); `S/decision/options.py` (`opening_set`); `S/boot/realm.py` (B03c; `resolve_anchor`, `build_realm`);
  instruments: `register`, `corpus_run`, `strife`, `tools/m1_acceptance.py`, `tools/tests_for_diff.py`, `tools/ci_sim_fabrication_check.py`; `S/tests/_realm_goldens.py` (B02);
  the closing SHAs of B00, B01, B02, B04, B05, B07, B12c, B21, B24, B25, B26, B27, B28, B32 (and of B11, B21b, B21c, B24a, reached through them); the permanent surface.
SERIAL EDGES and FILE CENSUS: written after the position table and the items (E-11), at the end of the batch block in `workplan_v12_part38_cont.md`, before the boundary row.
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
| B33.30 | the standing levy, the `tax` edict | CP-T08-07 (the intake `:333`) | HELD (trigger: B12c.34 merged, its gate met; A-116 gave H-163 limit 3(a) an owner) | — | B12c.34 |
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
- FALSIFIER and CONTROL: "Plant `upkeep: 0` on the dignity rows: one unit pays everyone, and `upkeep_owed` is not read if the count renewed does not rise" (read at B33.02, where `upkeep_owed` exists). Control: the executed-verb tallies of `corpus_run --seasons 2` [v12: two seasons a case, D-17; the case's own span, to `MAX_SEASONS`, is B99's] at seed 0 equal B32's close (`reading @<sha>`): no oath is termed at build and nothing reads the new values yet but `upkeep_of`, whose `off_king` value equals `default_upkeep`.
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
- GATE: `python -m pytest engine/season/tests/test_inst_byz_b.py -q` → pass; the realm content hash (`HASH READING`) at seed 0 after one season → recorded (equal to B33.01's reading where no sworn dignity-holder is paid; the source's mover class "a sworn dignity-holder is paid" is declared either way).
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
- GATE: `python -m pytest engine/season/tests/test_inst_byz_c.py -q` → pass; the realm content hash (`HASH READING`) at seed 0, one season → equal to B33.04's reading.
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
- GATE: `python -m pytest engine/season/tests/test_inst_byz_d.py -q` → pass; `python tools/validate_ed_citations.py` → exit 0 (the registry row cites nothing new); the foreign-arm build hash (`HASH READING`) at seed 0 → moved, recorded for B33.99.
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
- TESTS: the one above; `test_the_control_arm_has_no_empire` (B33.09) stays green. `[ASSUMPTION: test names; the item creates them (E-3) — basis: the names appear in no source file of the suite; K9 added this mark]`
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

### B33.14 — distance across a border; the root of a place · COL_B §1, §3 (`root_of`) · BUILD · HASH MOVER(behaviour)
- SOURCE: COL_B §1 ("`distance`"), §3's last bullet (`root_of`), §4's `hops` sentence, "Gate" first bullet; D-U1-11k, R-22 (one member `distance`, one fixture `distance_step`; `remove_step` not added); `14_VERBS_MATERIAL_B_stores.md` §2 ("this batch (B12) is the first to land of its readers … the institutions' `remove` folded into it"); `SYN_A` §4 ("COL-B §1's `remove` is this reader, not a second one"); closes F-R4-08 (distance as one member) for the institutions.
- ADVANCES: none of the nine; A-22's far superior is far.
- INSTRUCTION:
  0. Open the tree: the reader of OBS member 20 that B12c.12 landed (`grep -rn "distance_step" engine/season --include=*.py` names it and its module) and its definition; record both in the commit body. Do not write a second reader (UNDECIDED 2; `SYN_A` §4). **If none exists** (B12c did not land it), write COL_B's reader as its §1 states it: "`engine/season/queries/world_q.py::distance(w, place_a, place_b) -> int` … territory hops on the shortest path over `data/geography.py::adjacent_territories()` between the territory rung containing `place_a` and the one containing `place_b` (0 within one territory), plus `border_hops` when the two places lie under different root rungs", and skip step 2's composition.
  1. `root_of`: "`root_of` does not exist (checked: no `def root_of` in `queries/world_q.py`); it is written once, beside `place_of` …, as the last element of `state/containment.py::ancestry(w, rung_id)` of the place's rung; `foreign_cast`'s note defines the root as the territory with no `contain` edge into `r_valoria`." (Not `world_q.py`'s method `ancestry` of another class.)
  2. Two places under different roots (the one case the ladder reader cannot answer: no common ancestor). The one reader gains a branch, `[ASSUMPTION: the cross-root composition on the existing reader's unit — basis: UNDECIDED 2; COL_B §1's border rule, measured as B12c's reader measures]`: when `root_of(place_a) != root_of(place_b)`, the distance is the reader's own count from the inner place to the crossing territory, plus `border_hops`, plus the count from the foreign root to the foreign place. COL_B's crossing: "A foreign root with no edge in the geography file is entered at the nearest territory the file's `altonian_passes` names (for `terr_ALT`: T3 or T10, whichever is nearer `place_a`); `terr_T16` has its own `coastal` edge to T1 … The pass lookup reads `geography()["altonian_passes"]`, never a literal." And COL_B §4: the reader "reads `hops` when one place is that settlement and the other is not" — the `centre` key's `hops` (B33.09) is added for `ALT-0`.
  3. "`data/fixtures.py`: `distance_step` is OBS's one fixture (`remove_step` is not added); `border_hops = 2` (hops; sweep {1, 2, 3}), a parameter of the reader, NUMBER row in `hole_register.yaml`, graded `assumption`. `levy_ob` is not added."
  4. Create `S/tests/test_remove.py` ("the name this file gave; kept"), written before steps 1–2 and read red: `test_root_of_is_the_last_ancestor` (a T1 settlement reads `terr` of the realm's root chain's top; `ALT-1` reads the `ALT` root); `test_distance_is_zero_for_one_place_and_symmetric`; `test_distance_inside_one_root_is_the_reader_unchanged` (three hand-checked pairs inside the realm equal the reader's reading at B32's close: the control that nothing in-root moved); `test_distance_across_the_border` (a T3 settlement to `ALT-1` equals the reader's count to T3 + `border_hops` + the count from `ALT` to `ALT-1`; `ALT-0` adds its `hops`); `test_distance_ignores_radiation_bands` ("independent of `radiation_bands` (IN-35's control, kept)"). The source's three pairs ("T1–T2 1; T1–T13 by the file; T3–`ALT-1` `border_hops`") are territory-adjacency values, rewritten here to the one reader's unit (UNDECIDED 2) `[ASSUMPTION: the test bodies — basis: the source's gate, re-pointed at the reader B12c landed]`.
- WHERE: `S/queries/world_q.py` (`root_of`, beside `place_of`); the module of B12c's `distance` reader (its cross-root branch, by symbol); `S/data/fixtures.py` (`border_hops`); `S/hole_register.yaml` (NUMBER row, block slot 1); NEW `S/tests/test_remove.py`.
- TESTS: the five above.
- FALSIFIER and CONTROL: an in-root pair whose distance moved (the second reader the rule forbids, by another route). Control: `test_distance_inside_one_root_is_the_reader_unchanged`; `distance_step: 0` reproduces B33.13's realm hash.
- GATE: `python -m pytest engine/season/tests/test_remove.py -q` → pass; `python tools/ci_sim_fabrication_check.py` → exit 0 (`border_hops` tagged); `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`).
- HASH MOVERS: any roll whose two places lie under different roots (the foreign arm's acts toward the realm, and back). Declared; B33.99.
- DEPENDS ON: V12 Batch B12c (B12c.12: the member's first reader, `distance_step`); EXISTS-IN-TREE `S/state/containment.py::ancestry`, `S/queries/world_q.py::place_of`, `S/data/geography.py::geography`, `adjacent_territories`, `systems/settlements/valoria_geography_v30.yaml: altonian_passes` (`primary` T3, `secondary` T10); V12 B33.09 (`centre.hops`), B33.10.
- GLOSSARY: row *distance* — its owner column points at B12c's reader and `world_q.root_of`; "root": the outermost place a place lies within, as the root of a family tree (here, the territory with no parent); `remove` stays a refused synonym for this sense.
- IDS: H block slot 1 (`border_hops`).
- COST and TIER: small build; `sonnet`, `high`; the cross-root composition read by `opus` (UNDECIDED 2).
- LANDS IT: B33's producer; `Item: B33.14`, `[skip ci]`.

### B33.15 — a roll through a seat reads distance from where the actor stands · COL_B §1 (the host operand) · BUILD · HASH MOVER(behaviour)
- SOURCE: COL_B §1 (second and third paragraphs), "What it changes" 2, "Gate" second bullet, "Falsifier" first two bullets; C3-C10; `SYN_A` gate 4.
- ADVANCES: none of the nine; "Every roll made through a seat on something in another territory carries the obstacle term `distance`".
- INSTRUCTION:
  0. Open `S/queries/inputs.py::SocialContestInput` and `S/seam/wrappers/sigma.py::contest_input`, and record whether B12c (or B28's `comply`) already carries a distance operand into the social roll, and from which two places. If it carries one from the actor's place, step 1 is recorded as present and skipped.
  1. "`rosters.yaml: obstacle_terms` gains nothing: member 20 `distance` exists in OBS's roster. `modules/social_contest/roll.py::obstacle` sums it inside the bound as a hostile term; the host carries the raw hop count (`queries/inputs.py::SocialContestInput` gains `distance: int = 0`, set by `seam/wrappers/sigma.py::contest_input` from the **actor's** `place_of` and the place of the act's subject or `to` [UNVERIFIED: the wrapper's present signature; SC-B's implementation lane fixes it])." The count is the one reader's (B33.14), at `distance_step` per unit. For `requisition` this is the measure B33.04 declared (UNDECIDED 1).
  2. `S/tests/test_remove.py` gains the draw arms (below), written before step 1 and read red (one arm's shares equal the other's).
- WHERE: `S/queries/inputs.py` (`SocialContestInput.distance`); `S/seam/wrappers/sigma.py` (`contest_input`); `modules/social_contest/roll.py` (`obstacle`, the member's term) only where step 0 finds the term unsummed; `S/tests/test_remove.py`.
- TESTS: `test_the_levy_is_a_draw_at_both_distances`, `test_distance_reads_the_actor_s_place` `[ASSUMPTION: test names (E-3)]`.
- FALSIFIER and CONTROL: "Planted: make `distance` read the seat's rung instead of the actor's place; a king standing in Oastad then levies it at the capital's odds and the hand-built 'progress' assertion reddens. Planted: force the roll's band to Success; the 'three of four bands' assertion reddens in both arms." Control: "`distance_step: 0` makes the two arms' shares equal within sampling."
- GATE: "**The draw is a draw:** for one hand-built levy (MATERIAL-B's row), 400 seeded rolls at `distance` 0 and 400 at `distance` 4 (`PYTHONHASHSEED=0`, seeds 0–399). Printed: band shares for each arm. Pass: Failure's share is higher at 4 than at 0, **and each arm contains at least three of the four bands**" → `python -m pytest engine/season/tests/test_remove.py -q` → pass (`checked >= 400` per arm); `SYN_A` gate 4's arm: "On a hand-built `issue` to a sworn addressee two territories away, the recorded roll (SC-P1's `terms` and `levels`) carries `distance` among its terms … and no `oath_step`, `remove` or `obligation` term" (its `obligation` level half is read at B33.34). "Crowd-out (rule V2 …): executed counts of `requisition`, `transfer`, `issue` pooled over realm seeds 0–2 are printed before and after; a fall is reported, not asserted against" (two seasons). `opus` reads the 400-and-400 arms.
- HASH MOVERS: every seeded realm in which a roll is made through a seat on something away from the actor's place. Declared; B33.99.
- DEPENDS ON: V12 B33.14; V12 Batch B05 (`U5c_SC_one_obstacle_form`, the composer; SC-P1's recorded `terms`); V12 Batch B12c (B12c.13: the levy row); EXISTS-IN-TREE `S/queries/inputs.py::SocialContestInput`, `S/seam/wrappers/sigma.py::contest_input`, `modules/social_contest/roll.py`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`; `opus` on the arms (COL_B's tier line).
- LANDS IT: B33's producer; `Item: B33.15`, `[skip ci]`.

### B33.16 — news of a change of office stops at the border · COL_B §3 · BUILD · HASH MOVER(behaviour)
- SOURCE: COL_B §3 (four bullets), "What it changes" 3, "Gate" third bullet; A-32, A-33 (COL_B's U5d line); CR-29 as B11.03 and B11.04 land it (`rosters.yaml: event_reach`, `epistemic.py::_ch_reach`).
- ADVANCES: none of the nine; the border (`foreign_cast`'s note: "perception channels at the border" NOT BUILT).
- INSTRUCTION: §3 is "content for CR-29's kind→reach map"; CR-29's map is in the tree from B11 (`event_reach`, values `room` or a `rung_kinds` member). The edits:
  1. "The border: no reach value admits a person whose place is under another root than the Event's place. `engine/season/epistemic.py`'s reach predicate asks `world_q.root_of(place)` equality first." In `_ch_reach`: return False when `root_of(place_of(pid)) != root_of(event_place(e))`, before the kind lookup.
  2. "A reach value `purview`: persons at a place the exercised seat's purview reaches (`state/gate.py::purview_reaches`, asked of `Act.via`). Proposed for `dispensation.issued`, `order.given`, `date.scheduled`, `office.established`, `requisition.taken`, `rung.seized`." `purview` joins the closed value set `data/rosters.py` refuses others outside; the six kinds take `purview` in `event_reach` (a kind B11.04 keyed at `realm` through `from_stratum: binding_decision` is overridden by its own key; record each override in the commit body) `[ASSUMPTION; medium; the source's "proposed"; Jordan to correct]`. `requisition.rendered` (B33.04) takes the same value as `requisition.taken`.
  3. "`tenure.closed`: realm reach **within the Event's root** (A-32 …)" — B11.04's `realm` value, now bounded by step 1. "`person.died`: **not** realm reach … (A-33)" — B11.04 already leaves it out; nothing is written.
- WHERE: `S/epistemic.py` (`_ch_reach`: the root test; the `purview` value's arm); `S/rosters.yaml` (`event_reach`: six keys, `requisition.rendered`); `S/data/rosters.py` (the value set); `S/tests/test_remove.py`.
- TESTS: `test_no_realm_news_crosses_the_border` (the border gate below, as a test at one season) and `test_purview_reach_follows_the_seat` (a hand-built `order.given` through a duke's seat reaches a resident of his duchy and not one of another) `[ASSUMPTION: test names (E-3)]`, red before the edits.
- FALSIFIER and CONTROL: a person at `ALT-1` holding a `told_by` claim of a realm `tenure.closed`. Control: inside the realm, `tenure.closed` reaches as B11.04 left it (A-32's shipped arm).
- GATE: "Border: `build_realm(0, foreign=True)`, one season (after CR-29): no person at `set_alt_1` or `ALT-0` holds a claim of a realm Event of this tick whose `chain` is empty and whose source is `told_by`" → `python -m pytest engine/season/tests/test_remove.py -q` → pass. "M-ABROAD: over seeds 0–4, four seasons, the report prints every `dispensation.issued` through `off_altonian_court`, the band it rolled, and the Katepano's next act. Pass: at least two different bands occur across the seeds" — at two seasons (A-114), printed in the commit body; "at least two bands" asserted only if at least two such issues occur, and the count is quoted either way (`checked >= 2` before the band assertion).
- HASH MOVERS: every seeded run in which a reach-keyed kind is emitted (who learns it). Declared; B33.99.
- DEPENDS ON: V12 Batch B11 (B11.03, B11.04: `event_reach`, `_ch_reach`; reached through B24); V12 B33.14 (`root_of`); EXISTS-IN-TREE `S/state/gate.py::purview_reaches`, `S/queries/world_q.py::place_of`.
- GLOSSARY: row *reach* — the `purview` value's reading: "news that reaches the persons under the issuing seat's ground, as a proclamation is read in the lord's own towns".
- COST and TIER: small build and content; `sonnet`, `high`.
- LANDS IT: B33's producer; `Item: B33.16`, `[skip ci]`.

### B33.17 — the court wants quiet; reabsorption is an ending · COL_B §4 bullet 4, §5 · CONTENT · HASH MOVER(encoding)
- SOURCE: COL_B §4 (the `goals.yaml` bullet), §5; X-13.
- ADVANCES: none of the nine; A-80 (a structural conflict authored as pursuits).
- INSTRUCTION:
  1. "`goals.yaml`: `goal_altonian_court_frontier_quiet`, `org: {seat: off_altonian_court}`, `object: {kind: orientation}`, `pursuits: {stability: 0.6, wealth: 0.4}`, `derives: {from: goal_altonia_conquer_valoria, kind: influences}`: a court that wants revenue and quiet above a governor who wants honour is the structural conflict, authored as two persons' pursuits and nothing else." The row is a foreign-arm row as `goal_altonia_conquer_valoria`'s are (it names a foreign seat).
  2. "`rosters.yaml: endings.members` gains `reabsorption: {victory: false, holds: {post: King}, under: Altonia, source: "by `theocracy`'s precedent (#457 D6): an endpoint, not a victory"}` `[ASSUMPTION; medium; Jordan to correct; revert: drop the row]`. No reader changes: `endings_reached` already evaluates a `{post:}` selector under a faction."
- WHERE: `S/goals.yaml` (one row, after `goal_altonia_conquer_valoria`'s family); `S/rosters.yaml` (`endings.members.reabsorption`); `S/tests/test_inst_byz_d.py`.
- TESTS: `test_reabsorption_loads_and_is_not_a_victory` (the ending row loads, `victory: false`; a planted world whose King coheres under Altonia reports it from `endings_reached`) `[ASSUMPTION: test name (E-3)]`.
- FALSIFIER and CONTROL: the control arm (`foreign=False`) seeding the goal row. Control: B33.09's control-arm test stays green.
- GATE: `python -m pytest engine/season/tests/test_inst_byz_d.py -q` → pass; `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`).
- HASH MOVERS: the foreign-arm build hash (a seeded goal). The ending row moves nothing (read, not written). Declared; B33.99.
- DEPENDS ON: EXISTS-IN-TREE `S/goals.yaml: goal_altonia_conquer_valoria`, `S/rosters.yaml: endings` (`theocracy`), `S/queries/world_q.py::endings_reached`; V12 B33.10.
- GLOSSARY: none.
- COST and TIER: content; `sonnet`, `medium`.
- LANDS IT: B33's producer; `Item: B33.17`, `[skip ci]`.

### B33.18 — two hearings: `audit` and `quo_warranto` · COL_C edit 1 · BUILD · HASH EQUAL
- SOURCE: COL_C "Exact edits" 1 and its notes on the cells, "What it changes" 1 and 4, "Gate" first bullet; X-12 (the kit's one audit row); `SYN_A` §6 (the rows "each as its file wrote it as reconciled"); A-39 (appeal on new grounds); SC-P4 (`05_SC_arrangement_rows_that_bind`, a band-keyed `disposes:`).
- ADVANCES: none of the nine; A-13 (`audit_at_exit` names this room).
- INSTRUCTION:
  0. Open `S/arrangements.yaml` and record whether B32 added `audit` or `quo_warranto`; write only the absent row(s), and record the reading.
  1. "`engine/season/arrangements.yaml` — two rows, in the thirteen-key shape plus SC-B's `standard:` and SC-P4's mapped `disposes:`":
     ```yaml
       # ── audit — an officer answers, on the ground he governed, to those he governed ───────────────
       - id:               audit
         disposal:          bench
         bench_basis:        determine
         floor:              open            # the governed may speak
         records_dissent:    true
         venue_min_rank:     settlement
         term_required:      true
         appeal_basis:       determine       # admitted on new grounds only (A-39)
         interposed:         [office, procedure, document]
         order:              rank
         proofs:             [testimony, record]
         standard:           demanding
         disposes:           {Overwhelming: ban, Success: oblige, Partial: Record}
         disposal_reach:      body

       # ── quo warranto — by what warrant do you hold? ───────────────────────────────────────────────
       - id:               quo_warranto
         disposal:          bench
         bench_basis:        determine
         floor:              open
         records_dissent:    true
         venue_min_rank:     duchy
         term_required:      true
         appeal_basis:       determine       # admitted on new grounds only (A-39)
         interposed:         [person, procedure, document]
         order:              rank
         proofs:             [record, testimony, oath]
         standard:           demanding
         disposes:           {Overwhelming: ban, Success: ban, Partial: oblige}   # the fallback, taken
         disposal_reach:      realm
     ```
     The cells' notes, each "`[ASSUMPTION; medium; this lane's; a data edit reverts it]`", are copied as the rows' comment block: `audit`'s Overwhelming `ban` "scoped to the banning seat's purview, FA-P3 change 3"; Success "an `oblige` of the officer to the opening seat, whose instrument is a `tribute`-shaped restitution (`15_INSTITUTIONS_COLONIAL_A_instruments.md`; the `due` is a `transfer.made` to the governed ground's rung)"; Partial "a `Record` (an admonition …) this cell waits on that site and is inert before it"; Failure "nothing is opened and `05_SC_acquittal.md`'s quittance is the officer's". `quo_warranto`'s Overwhelming and Success "a `ban` on the holder from that one seat …, **the file's own fallback, taken**"; "`release` is not a `disposes:` value … so the closing arm once requested of SC is withdrawn. Where the grantor's own seat holds a `revocation` basis over the conferred seat (T-o, `04` §C.2), the calling-in can also be his `revoke` …; the bench is the route when it does not"; Partial "the grant stands for a fee: an `oblige` whose `due` is one `transfer.made` to the grantor's rung"; Failure "the grant stands; the docket's closing Record is the holder's evidence in any later calling-in".
  2. Create `S/tests/test_audit_and_charter.py` (U3 §6.1: MISSING; "write it … red against the control where the claim is a defect") with `test_both_rows_load` and `test_a_fourteenth_key_or_an_off_enum_band_cell_is_refused_naming_the_row` ("both rows load; a fourteenth key or a band cell off the enum is refused naming the row"), written before step 1 (the first red: no row).
- WHERE: `S/arrangements.yaml` (`audit`, `quo_warranto`); NEW `S/tests/test_audit_and_charter.py`.
- TESTS: the two above.
- FALSIFIER and CONTROL: "A row with no docketed matter moves nothing: seeded hash EQUAL." Control: the realm hash at seed 0, one season, equal to B33.17's reading.
- GATE: `python -m pytest engine/season/tests/test_audit_and_charter.py -q` → pass; `python -c "import engine.season.data.arrangements"` → loads (`_ARRANGEMENT_KEYS` and SC-P4's band-map check are the loader's refusals).
- HASH MOVERS: none ("EQUAL until docketed", U3 §3.1's row).
- DEPENDS ON: EXISTS-IN-TREE `S/data/arrangements.py::_ARRANGEMENT_KEYS`; V12 Batch B27 (`05_SC_arrangement_rows_that_bind`: the band-keyed `disposes:` loader; `05_SC_acquittal`); V12 Batch B05 (`standard:`); V12 Batch B32 (`COL_A`'s `tribute` form; `SYN_A` §6).
- GLOSSARY: rows *audit* (owner `arrangements.yaml: audit`; "audit": a hearing in which an officer answers for his term, as a governor is audited at its end) and *quo warranto* (owner `arrangements.yaml: quo_warranto`; the plain words "by what warrant", a hearing that asks a grant-holder to show his title).
- COST and TIER: edit (rows) and a test; `sonnet`, `high`.
- LANDS IT: B33's producer; `Item: B33.18`, `[skip ci]`.

### B33.19 — the audit's occasion, and the seats an audit follows · COL_C edit 2 · BUILD · HASH MOVER(behaviour)
- SOURCE: COL_C "Exact edits" 2 (three bullets), "Gate" (the distance and appeal bullets); X-12; A-13, A-39; `SYN_A` §4 (`audits_due`: "for each closed `hold` on a row carrying `audit_at_exit` whose `tenure.closed` claim `p` holds and over whose seat `p` may open (VEN-C edit 4's set), the departed holder (`Party`) and the arrangement").
- ADVANCES: none of the nine; A-13 (the exit audit), the *visita*.
- INSTRUCTION:
  0. Open the tree: `grep -n "def audits_due" engine/season/queries/world_q.py` and `grep -n "audit_at_exit" engine/season/offices.yaml engine/season/data/rosters.py`; record what B32 landed; write only what is absent.
  (Patched: P-18, resolved at the merge.) B32.31 builds `world_q.audits_due` and its `questions_for` referent from the same `SYN_A` §4 row (and B32.27 the `Office.audit_at_exit` field), in B32, which lands first: step 2 below is landed there and is read here, not written; this item writes step 1's test, step 3's three seat rows and step 4's tests.
  1. "**Who may open, and where** — no new predicate; three facts already asked: `open_case` is `remit:determine` (`verb_table.yaml`). An `audit` is opened through a seat whose purview reaches the audited seat's rung; the bench is `judging_set`'s. **The opener's `distance` from the audited ground enters every `determine` and `speak` in the hearing** (… OBS member 20), so an audit held from the capital is a weaker instrument than one held on the spot" — carried by B33.15's host operand (the opener's place), nothing added here but the test.
  2. "The occasion: `world_q.audits_due` (SYNTHESIS-A §4; X-12), `world_q.vacancies`' sibling. When a `hold` on a seat whose row carries `audit_at_exit: audit` closes (term matured, revoked, released, died), for a person who holds the `tenure.closed` claim and may open (VENICE-C §4's set), the departed officer and the arrangement ride his question as `Party` referents, read when read. He may open the audit, or not." Wired at the occasion site `vacancies` stamps (by symbol).
  3. "`offices.yaml`: the seat-row key is `audit_at_exit: <arrangement id>` (A-13; X-12), not `audited:`. A form's `confers:` block carries `audit_at_exit: audit` into the established seat (SYNTHESIS-A §1), and it is proposed for `off_lord_treasurer` (BYZANTINE-GROUNDING item 1), `off_royal_marshal`, `off_military_commander_hm` `[ASSUMPTION; content; Jordan to correct]`." The three rows gain `audit_at_exit: audit` (`off_lord_treasurer`'s key is the grounding file's item 1 too, B40: whichever lands first writes it and the other records it present).
  4. `test_audit_and_charter.py` gains the distance and appeal tests below, written before steps 2–3 and read red.
- WHERE: `S/queries/world_q.py` (`audits_due`, beside `vacancies`); the occasion site (by symbol); `S/offices.yaml` (`off_lord_treasurer`, `off_royal_marshal`, `off_military_commander_hm`: `audit_at_exit: audit`); `S/tests/test_audit_and_charter.py`.
- TESTS: `test_audits_due_names_the_departed_officer_to_one_who_holds_the_closing` (a hand-built hold on an audited seat closed by term; the holder of the `tenure.closed` claim who may open reads the officer and `audit`; a bystander with no claim reads nothing); `test_distance_weakens_the_audit` ("the same audit determined at `distance` 0 and at `distance` 3: shares differ in the direction of the term"); `test_appeal_needs_a_new_ground` ("an appeal of an `audit` verdict naming no new ground is refused; one naming an excluded testimony is admitted") `[ASSUMPTION: test names (E-3)]`.
- FALSIFIER and CONTROL: an audit opened with no person's act (COL_C: "No automatic audit"); an occasion stamped for a person who holds no `tenure.closed` claim. Control: a seat without `audit_at_exit` closes and nothing is stamped.
- GATE: `python -m pytest engine/season/tests/test_audit_and_charter.py -q` → pass; the realm at seeds 0–2, two seasons: `audits_due` stamps quoted (a count per seed, read and reported).
- HASH MOVERS: every run in which a hold on one of the three seats closes (a new question referent). Declared; B33.99.
- DEPENDS ON: V12 B33.18; V12 B33.15 (the opener's distance); V12 Batch B32 (`VEN_C` §4's set of who may open; `SYN_A` §1 `confers.audit_at_exit`, §3 the key's refusal); V12 Batch B24a (CR-59, CR-61: the appeal ground's carrier, reached through B27); EXISTS-IN-TREE `S/queries/world_q.py::vacancies`, `S/offices.yaml` rows `off_lord_treasurer`, `off_royal_marshal`, `off_military_commander_hm`.
- GLOSSARY: none (*audit*, B33.18).
- COST and TIER: small build and content; `sonnet`, `high`.
- LANDS IT: B33's producer; `Item: B33.19`, `[skip ci]`.

### B33.20 — a held grant pleads its age; a granted seat carries its term · COL_C edits 3–4 · BUILD · HASH EQUAL
- SOURCE: COL_C "Exact edits" 3 and 4, "What it changes" 2 and 3, "Gate" (the verdict and age bullets), "Falsifier"; C3-C10 (a cited Record is a `proofs` level; `proof_step` deleted); A-5.
- ADVANCES: none of the nine; prescription and the calling-in.
- INSTRUCTION:
  1. "`engine/season/data/fixtures.py: prescription_seasons = 8` (seasons per unit of item weight; sweep {4, 8, 16}; NUMBER row, graded `assumption`). Reader: where SC's evidence weight function weighs a cited Record (an item entering the roll as `proofs` levels, C3-C10) that is a `dispensation` whose form has `hardens: true`, its weight is `1 + min(3, held_seasons // prescription_seasons)`, `held_seasons` read from the citing party's own `hold` on the Record (`Tenure.since`). One clause at the single owner of evidence weight (`05_SC_evidence_and_rebuttal_B.md`'s weight function; until it lands, `world_q.proofs`). The cap is the `3` in that expression and is the same fixture row's second field (`prescription_cap`, sweep {1, 3, 5})." The item opens the tree and names in its commit body which owner it edited (`05_SC_evidence_and_rebuttal_B`'s function, B24, or `world_q.proofs`).
  2. "**Terms.** `instruments.yaml` `confers:` blocks carry `term:` equal to the form's `term`; `_eff_confer` reads it by FA-P3's rule. Proposed content on existing seats …: none. This file adds terms **only** to seats a grant creates, so no seat in the built realm changes." Open `_eff_confer` (by symbol) and record whether B32's `COL_A` item already reads `confers.term`; write the read only where it is absent.
  3. `test_audit_and_charter.py` gains the verdict and age tests below, written before step 1 and read red.
- WHERE: `S/data/fixtures.py` (`prescription_seasons`, `prescription_cap`); the evidence weight function (by symbol, as step 1 records); `S/hole_register.yaml` (NUMBER row, block slot 2); `_eff_confer` only where step 2 finds the read absent; `S/tests/test_audit_and_charter.py`.
- TESTS: `test_the_verdict_is_a_draw` ("On a hand-built hearing under `audit` (one officer, a bench of one, three residents each holding a firsthand `requisition.taken` claim of the officer's doing): 400 seeded `determine` rolls with the three testimonies cited and 400 with none. … Pass: the cited arm's Overwhelming + Success share is higher, **and each arm contains at least three bands**. Control: `proof_level: None` … equalises the arms within sampling"); `test_age_is_odds_not_outcome` ("Under `quo_warranto`, the same instrument held 0 seasons and 16 seasons: 400 rolls each; the older arm's Failure share (the grant stands) is higher; both arms contain a band in which the grant falls"); `test_the_seizer_cites_at_weight_one` (the falsifier's arm) `[ASSUMPTION: the last test's name (E-3)]`.
- FALSIFIER and CONTROL: "Planted: read `held_seasons` from the Record's creation instead of the citing party's hold; a charter seized last season by a stranger then pleads its full age, and the hand-built 'the seizer cites it at weight 1' assertion reddens. Planted: force the band to Success; the 'three bands' assertions redden." Control: `proof_level: None`.
- GATE: `python -m pytest engine/season/tests/test_audit_and_charter.py -q` → pass (`checked >= 400` per arm); `python tools/ci_sim_fabrication_check.py` → exit 0; "Realm reading (after CR-60/61 and FA-P3): seeds 0–4, six seasons, with one `farm` seeded (`…_E_scenario.md`): the report prints whether an audit was opened at the term's end and its band" — the scenario is `COL_E`'s (B40) and six seasons pass the cap: moved to B40 at two seasons (A-114). `opus` reads the 400-and-400 arms.
- HASH MOVERS: none (no hardening form is cited in the built realm; no built seat gains a term).
- DEPENDS ON: V12 B33.18; V12 Batch B24 (`05_SC_evidence_and_rebuttal_B`: the weight function), Batch B05 (`proof_level`, `U5c_SC_one_obstacle_form` §3), Batch B21 (FA-P3, `06_FA_seat_terms_and_turnover`: `term:` and `_eff_confer`), Batch B32 (`SYN_A`'s `hardens: true` rows; `COL_A`'s `confers:`); EXISTS-IN-TREE `S/queries/world_q.py::proofs`.
- GLOSSARY: row *prescription* (new: "prescription": title that strengthens with long holding, as in law; owner `Fixtures prescription_seasons`).
- IDS: H block slot 2 (`prescription_seasons` with `prescription_cap`).
- COST and TIER: edit (a fixture and one clause) and tests; `sonnet`, `high`; `opus` reads the arms (COL_C's tier line).
- LANDS IT: B33's producer; `Item: B33.20`, `[skip ci]`.

*(This part continues in `workplan_v12_part38_cont.md`, from B33.21. The last item written here is B33.20.)*
