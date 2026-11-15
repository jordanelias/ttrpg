# Workplan v12 — part 34: batches B32-inst-kit, B37p-wr-kin-and-life

## Status: PROPOSED (a body part of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree at `09bb5a1` (branch `ccr-62958c70-0kjhsw`), read 2026-11-12; author lane A34 of `master/workplan_v12/V12_STRUCTURE_part2.md` §4.2, with `V12_STRUCTURE_part4.md` (errata E-1 to E-15) applied where it differs. Every item is written against the tree as B00 to B27 will leave it; a symbol a later batch makes is named with its batch.

**What this part holds.** Two batches that open together at step S17: `B32-inst-kit` (FA; on the critical path, slack 0), the institutions kit and the first family builds on it, and `B37p-wr-kin-and-life` (WR; slack 3), four carried v11 positions on kin, estates and recovery. Each batch is one block with one close (`V12_STRUCTURE_part2.md` §5.2, §5.3; `_part4.md` E-1: each ends with a `.99` re-pin position). A part cites another part's batch or item by handle only.

**Words.** `unified/U1_GLOSSARY.md`; a person's numbers are an attribute, a skill and its skill score, a derived score (A-98); a *lap* is one pass of the season's scene budget, a *round* one engagement of a fight (A-101). A membership kept by warrant is a **list** (glossary *roll*: "roll" is a dice roll); identifiers keep their names. Source text that says "round" for the season's pass is copied with `NAMES:` (every item here lands after B04's PCR-4).

**Paths.** A bare path is under `proposals/2026-11-12-subsystem-audit-suite/`; a path under `engine/`, `tools/`, `references/`, `registers/`, `tests/` is the repository's. `the intake` is `master/eval/V12_INTAKE.md`; `U3` is `unified/U3_DEPENDENCY_ORDER.md`; `COL_A`, `SYN_A`, `SYN_B`, `HAP_B`, `BYZ_A`, `BYZ_E`, `PAP_A`, `PAP_B`, `BIND_B`, `VEN_C`, `PES_FA_B`, `REST_2` are `proposals/15_INSTITUTIONS_COLONIAL_A_instruments.md`, `_SYNTHESIS_A_one_kit.md`, `_SYNTHESIS_B_the_deed_ledger.md`, `proposals/22_HAPPENINGS_B_the_throne_is_never_stranded.md`, `15_INSTITUTIONS_BYZANTINE_A_dignities_and_the_roll.md`, `_BYZANTINE_E_accession_recall_and_the_crowd.md`, `_PAPACY_A_ground.md`, `_PAPACY_B_patronage_election_discipline.md`, `proposals/14_VERBS_BINDING_B_sittings.md`, `15_INSTITUTIONS_VENICE_C_roll_lot_ballot.md`, `proposals/16_PESSIMIST_FA_B_who_may_sit_join_and_declare.md`, `proposals/17_CENSUS_REST_2_wiring.md`.

---

## Batch B32-inst-kit · lane FA · wave W17 · step S17 · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B32-inst-kit
IN-FLIGHT ROW: registers/handoffs/HANDOFF_FA.md, Open table
GATE: Batch B00-ids @c3418a6a160fc6a17e5a8bf45112a0e55699a695
GATE: Batch B01-laneA @cfd9aefb049c2fe49b55c7ada1b0b624919af23d
GATE: Batch B02-tests
GATE: Batch B04-capability-home
GATE: Batch B05-one-roll
GATE: Batch B07-task-draw
GATE: Batch B20-mb-orders
GATE: Batch B21-fa-governance
GATE: Batch B21b-fa-war
GATE: Batch B21c-fa-seats
GATE: Batch B24-sc-hearing
GATE: Batch B24a-sc-outside-the-room
GATE: Batch B25-fi-questioning
GATE: Batch B27-sc-proceedings
HASH READING: `PYTHONHASHSEED=0 python -c "import sys; from engine.season.boot.realm import build_realm; from engine.season.harness.populated import run; s, k = int(sys.argv[1]), int(sys.argv[2]); w = build_realm(s); run(k, s, w=w); print(w.content_hash())" <s> <k>` → the realm content hash at seed `<s>` after `<k>` seasons: `<k>` = 1, one season, unless the gate names two (never more before B99, D-17); `<k>` = 0 reads the build hash; per item `<s>` = 0 (a mover's reading, E-2), at `.99` `<s>` = 0, 1, 2; each value quoted `reading @<sha>`, the tree it was read on (`workplan_v12.md` §3.B, "the hash reading").
REQUIREMENT: R-04.a (`determine`, `convene` executed with `Act.via` set) → each reads at least 1 in the `BUILT OUT` block's `via` column of `aperture 2 0` (four seasons in `IS_A_NINE.md` §5; A-114); `BUILT OUT`: `determine`, `pardon` → each built out (`IS-A-08`: a verb not built out at the close is a failed gate). No `status:` is edited (A-114).
BATCH GATE (read once, on the closing tree, `PYTHONHASHSEED=0` on every seeded command):
  `python -m pytest engine/season/tests/test_instruments.py engine/season/tests/test_inst_syn_a_kit.py engine/season/tests/test_inst_syn_b_deed_ledger.py engine/season/tests/test_inst_byz_a.py engine/season/tests/test_inst_byz_e.py engine/season/tests/test_inst_pap_a.py engine/season/tests/test_inst_pap_b.py engine/season/tests/test_vb_b_sittings.py engine/season/tests/test_inst_ven_c.py engine/season/tests/test_convening_condition.py engine/season/tests/test_fa_eligibility.py engine/season/tests/test_faction_q.py engine/season/tests/test_in61_heir_hears_vacancy.py engine/season/tests/test_in61_succession.py -q` → all pass;
  `python -m engine.season.harness.aperture 2 0` and `2 1` → the `BUILT OUT` lines for `determine`, `pardon`, `convene` quoted, before (`reading @<B27 closing sha>`) and after; `determine.refused` keyed `party` and `docket` 0, `pardon` formed only on a restrained person (BIND_B gates B2, B3); `convene.refused` keyed `purview` quoted (H-278);
  `build_realm(0)` content hash at build, one season and two seasons, seeds 0 to 2 → moved, as declared per item; each item's behaviour control as stated in it;
  `python tools/export_npc_roster.py --check` → reports the NPC-021 row as a hand edit (its documented behaviour, PAP_A edit 1), nothing else;
  `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); `--requirements` → nine lines; `python tools/m1_acceptance.py --summary` → its verdict line quoted;
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (engine core and registries: the full gates, CLAUDE.md §0.4);
  the glossary rows the items name, read against the code landed (`STAGES.md` "The glossary always matches" rule 2): a mismatch fails the close;
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the named conjuncts' readings with their tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, and the batch's measured wall time; B32.99 writes the conjuncts' `reading:` records; `status:` is not edited (`IS-A-12`).
RE-PIN: once, in B32.99: the realm and corpus pins in `engine/season/tests/_realm_goldens.py` (B02's one owner), read against B28's after-reading (`reading @<sha>`; S17's merge order is B11F2, B22, B26, B28, B32, B37p, part 2 §3, HD-06; lane H3: every baseline this batch named as "B27's close" now reads B28's after-reading); the commit says "re-pin: encoding (B32.27 `Office.audit_at_exit`); behaviour (B32.05 the form fan, B32.08 the four seeded Records, B32.12 six vacant dignity seats, B32.13, B32.14, B32.16, B32.19 to B32.26, B32.32)".
EXPECTED RED UNTIL B32.99 (under `[skip ci]`, E-1; one batch line, repair lane R1): the realm and corpus pins any mover item of this batch moves read red from its first mover (B32.05) to the re-pin; the files that pin them (`git grep -lE '"[0-9a-f]{32}"'` over the test trees and the golden files, those this batch names): `engine/season/tests/_realm_goldens.py` (B02's one pin file); `engine/season/tests/test_go07_canonical_digest.py` (its asserting test, `SHIPPED`/`CENSUS`).
IDS: ED-FA 0; H 2 (the NUMBER rows of `presumption_gain` (B32.07) and `dignity_grades` (B32.12); `V12_STRUCTURE_part3.md` §7.5 turns counts into blocks)
DIALS AT CONTROL: `presumption_gain` = 0; set by B98; target: SYN_B gate 2 at 0.5 on the realm after B39's prehistory ("among persons holding claims of all six seeded deeds, a majority order them king, Hafenmark, Varfell, **and at least one does not**"), at two seasons (A-114).
  `tables.selection`, `tables.eligible_from`, `tables.cooling_off` = `{}`, `binds: members_by_warrant` on no row, `audit_at_exit` on no row: not dials (content: the councils are VEN-D's rows, B33; SYN_A §3.6 "content numbers are not fixtures").
UNDECIDED: (1) **`covenant_in_force` and `OBEYED_WRIT` are `14_VERBS_SOCIAL1_B`'s (B28), which opens beside B32 at S17 and is not in B32's `after` list** (`V12_STRUCTURE.md` §2.1). B32.04's `in_force` asks `covenant_in_force` for a covenant-made form. Readings: (i) the coordinator merges B28 before B32 in S17 (B32 rebases on it, `V12_STRUCTURE_part3.md` §7.4); (ii) B32.04 lands with a `STOPS IF` and the covenant arm reads "unmatured stages" until B28 lands. Taken (ii), the reading that adds no edge; H2 decides whether to add B28 → B32. (2) **`dignity`** is no Seat field (SYN_A §3: "`dignity` is not among them … it needs a ruling's amendment text before it lands as a Seat field"); BYZ_A edit 3 needs it read. Taken: row data on `data/rosters.py::SEAT_ROW_BY_ID`, no `Office` field, the precedent B21 took for `term:` (C3-C15). (3) **`Office.audit_at_exit`** (VEN_C edit 3) is a ruled Seat field (A-13, `04:331`); the source's "folded into the hashed representation only when not `None`" does not hold for a dataclass field (`state/world.py::_object_head`, D-04): B32.27 is an encoding mover. (4) **PAP_A edit 5 waits on CR-74**, which lands in B21s (S18, after B32): a back edge if carried here; it is a POINTER (B32.18) and joins B21s (E-8: the dependency wins); A35 and H2 must take it. (5) **SYN_B gates 2 and 4 read the prehistory (SYN_B edit 2, B39)** and gate 5 reads PAP-C's consecration hearing (B33); each is moved to that batch (§5.8). (6) **SYN_A gate 3's `comply` arm reads `forborne` (PAP-D edit 7, B33) and gate 4 reads the `obligation` level (`owed_to`, VEN-A edit 3, B33)**; moved to B33. (7) **SYN_B §6 (Hafenmark's heir title)** is "`15_INSTITUTIONS_COLONIAL_D` edit 4, unchanged" (B33) and SYN_B's own implementation block puts only edits 1, 3, 4 in B32; the B21 author attributed the `off_duchess_hafenmark` successions row to SYN_B in B32 (`HAP_B` edit 2's "when … SYN-B edit 6 lands"). Taken: the row lands with COL_D edit 4 in B33, which makes the title row it names. (8) **PAP_B cites `15_INSTITUTIONS_PAPACY_grounding_mechanisms.md` item 1 "lands inside this batch"**; U3 puts that file in B40. PAP_B's own edits 6 to 8 already carry item 1's text (floor, combinable `quorum`, candidate skip); B40's item for grounding item 1 is then a POINTER to B32.20. (9) **`contest_owed`** (B07, A10): B32.26 deletes `pardon`. `release` is attributed there to `14_VERBS_BINDING_B`, which gives `release` no `contests:`: it is not deleted here; H2 to name its owner. **Patched (R2d, CHK_K8 #4):** HD-27 named B32's BIND_B item, but `release`'s row closes a seat `hold` (abdication), which B07's loader refuses on a `bookkeeping_verbs` member, and a task route would make abdication a drawn act: a design choice, sent to Jordan (`checks/R2d_APPLIED.md` J-1); B32.26 step 5 carries the assumption (it stays in `contest_owed`). (10) BIND_B's gate B1 to B3 read `aperture 2 1` and `2 0` counts at the tree the source measured; the readings are quoted, not asserted equal to the source's numbers. (D4) Lane D4 (ladder steps 4 and 5): B32.10 is built here, not left as a request. The owner it asks for already exists by B32: B24 (S13) lands the evidence filing step (B24.25), and `recites` is B32.09's, so B32 is the first batch holding both; the sentence SYN_B asks is fully stated (one item per recited deed, the cell, weight 1, the certifying seat as origin; impeachment by the owner's existing origin rule), so it is one branch in the owner's filer, never a second filer. B32 (FA) edits the SC file once, as B33.42 edits MATERIAL's `proofs` source (precedent). B33.48's edit 4 becomes a POINTER to it.
C(B32-inst-kit): this batch's entries; the plan's head parts; `unified/U1_GLOSSARY.md` rows *instrument*, *form*, *list*, *dignity*, *patronage*, *lot*, *party*, *restrained*, *seat*;
  `engine/season/instruments.yaml` (NEW), `engine/season/data/instruments.py` (NEW), `engine/season/data/files.py`, `engine/season/data/__init__.py` (`load_all`), `engine/season/data/arrangements.py` (`_refuse_unknown`, `_refuse_not_in`, `_ARRANGEMENT_KEYS`), `engine/season/data/rosters.py` (`_load_offices`, `SEAT_ROW_BY_ID`, `OFFICES_BY_HOLDER`), `engine/season/data/verbs.py` (`DEED_KINDS`, `_load_choice_sourced`, `REFERENT_CLASSES`), `engine/season/data/fixtures.py`;
  `engine/season/rosters.yaml`, `engine/season/offices.yaml`, `engine/season/arrangements.yaml`, `engine/season/verb_table.yaml`, `engine/season/npcs.yaml`, `references/npc_registry.yaml`;
  `engine/season/state/gate.py` (`may_fill`, `may_claim`, `may_sit`, `REVOCATION_RULES`, `check_filled_by`, `sworn_to`, `purview_reaches`, `sits_over`), `engine/season/state/carriers.py` (`Office`), `engine/season/state/world.py` (`_object_head`);
  `engine/season/queries/world_q.py` (`questions_for`, `vacancies`, `sittings_before`, `detainees_held`, `restrained`, `judging_set`, `declared_votes`, `establishment_of`), `engine/season/queries/person_q.py` (`legitimacy`, `deed_term`, `attributed_deeds`, `projected_axes`);
  `engine/season/loop/predicates.py` (`_req_confer`, `_req_succeed`, `_req_oblige`, `_req_convene`), `engine/season/loop/effects_governance.py` (`_eff_confer`, `_eff_convene`, `_eff_pardon`, `_eff_revoke`), `engine/season/loop/effects_information.py` (`_mint_document`, the ballot loop), `engine/season/loop/calendar.py`, `engine/season/seam/wrappers/sigma.py` (`contest_input`), `engine/season/decision/options.py` (`operand_bags`), `engine/season/boot/realm.py` (was `harness/populated.py`: `build_realm`, the minted-seat loop, `resolve_anchor`);
  the tests named in the items; instruments `aperture`, `register`, `tools/m1_acceptance.py`, `tools/tests_for_diff.py`, `tools/export_npc_roster.py`; `engine/season/tests/_realm_goldens.py`;
  read only: `audits/15_INSTITUTIONS_COLONIAL.md` §4.3 (copied into B32.02), `audits/15_INSTITUTIONS_SYNTHESIS.md` §3.6;
  the closing SHAs of B00, B01, B02, B04, B05, B07, B20, B21, B21b, B21c, B24, B24a, B25, B27; the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, `registers/handoffs/HANDOFF_FA.md`, the skill and `methodology-close`).
SERIAL EDGES and FILE CENSUS: at the end of the batch (`V12_STRUCTURE_part4.md` E-11), after B32.99.
PARALLEL: S17 with B11F2 (IN), B22 (MB), B26 (FI), B28 (SC), B37p (WR); files shared, by census, at the end of the batch.
COST: small builds and edits, one encoding mover; producer `valoria-author` on `sonnet`, `high`; judgment nodes on `opus`: BYZ_A edit 7's terms (B32.13), BYZ_E's terms (B32.14), the gate readings of SYN_B (B32.07) and PAP_B (B32.20); the close's terminal critique `opus`.
EST: 16 h [estimate: `V12_STRUCTURE.md` §2.4's formula over 33 positions (0.4 h × 33 + 2.5 h), E-15; §2.2's 7 h counted the members]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B32.01 | the instruments registry, empty, and its one loader | COL_A edits 1–2; SYN_A §1 (schema, loader) | BUILD | EQUAL | Batch B21, Batch B27 |
| B32.02 | the sixteen forms | COL_A §4.3 rows; SYN_A §1 (changed cells, six rows) | BUILD | EQUAL | B32.01 |
| B32.03 | a dispensation may name a form; `debt` is a Record kind | COL_A edit 3; SYN_A §2 rows 1–5 | BUILD | EQUAL | B32.02; Batch B21c (CR-36's `resolution`) |
| B32.04 | the readers of an instrument | COL_A edits 5–7; SYN_A §4 rows 1–4 | BUILD | EQUAL | B32.03 |
| B32.05 | `issue` and `covenant` may name a form | COL_A edit 4; SYN_A §2 `choice_sourced` | BUILD | MOVER(behaviour) | B32.04 |
| B32.06 | one closed key set over a seat row | SYN_A §3 | BUILD | EQUAL | B32.01 |
| B32.07 | standing passes down the seat, at a discount | SYN_B edit 1 | BUILD | EQUAL | Batch B21 (BIND_C edit 9) |
| B32.08 | the four seeded Records | SYN_B edit 3; SYN_A §1 `seeded:` | BUILD | MOVER(behaviour) | B32.03, B32.06, B32.07 |
| B32.09 | a certificate recites deeds | SYN_B edit 4 (the writing half) | BUILD | EQUAL | B32.08 |
| B32.10 | a cited certificate files one item per deed | SYN_B edit 4 (request to SC's evidence owner, built at its owner; lane D4) | BUILD | EQUAL | B32.09; Batch B24 (B24.25) |
| B32.11 | a seat row may name no holder: it builds vacant | BYZ_A (the vacant-row build edit) | BUILD | EQUAL | B32.06 |
| B32.12 | dignities: the key, six vacant rows, `dignity_grades` | BYZ_A edits 3, 4 | BUILD | MOVER(behaviour) | B32.11 |
| B32.13 | `confer` on a dignity: oath, cited deed, terms | BYZ_A edit 7 | BUILD | MOVER(behaviour) | B32.12; Batch B21 (BIND_C) |
| B32.14 | `succeed` and `revoke` read the room; the deed race's odds | BYZ_E edits 1, 3; HAP_B edit 4 | BUILD | MOVER(behaviour) | B32.07, B32.13 |
| B32.15 | the `acclamation` row | BYZ_E edit 4 | BUILD | EQUAL | B32.14 |
| B32.16 | the Confessor at Himmelenger; the Templars' command; a comment | PAP_A edits 1, 2, 4 | BUILD | MOVER(behaviour) | Batch B21 |
| B32.17 | three Church benches judge realm-wide | PAP_A edit 3 | BUILD | MOVER(behaviour) | B32.16; Batch B24a (CR-60) |
| B32.18 | the Church strife signature | PAP_A edit 5 | POINTER (lands in B21s with CR-74) | — | — |
| B32.19 | who may fill a seat for somebody else | PAP_B edits 1–3, 5 | BUILD | MOVER(behaviour) | B32.06 |
| B32.20 | the conclave, the share and the graded count | PAP_B edits 6–8; SYN_A §6 (`quorum_share`, `matter.undetermined`) | BUILD | MOVER(behaviour) | B32.19; Batch B07, Batch B27 |
| B32.21 | the head of a faction may strip an officer | PAP_B edit 9 with `U5d_FA_owed_edits` §3 | BUILD | MOVER(behaviour) | B32.19; Batch B21 (BIND_C) |
| B32.22 | one convening per seat | BIND_B commit B1 | BUILD | MOVER(behaviour) | Batch B27 |
| B32.23 | `convene` asks purview over the venue; no past date | H-278 (with H-297's remainder), intake `:286` | BUILD | MOVER(behaviour) | B32.22 |
| B32.24 | `determine` forms only on a party before the bench | BIND_B commit B2 | BUILD | MOVER(behaviour) | B32.22 |
| B32.25 | `pardon` forms only on a person restrained on the asker's seat | BIND_B commit B3 | BUILD | MOVER(behaviour) | B32.24 |
| B32.26 | `pardon` is drawn | BIND_B commit B4 | BUILD | MOVER(behaviour) | B32.25; Batch B05, Batch B07 |
| B32.27 | the list kept by warrant: roster, tables, loader, `audit_at_exit` | VEN_C edits 1–3 | BUILD | MOVER(encoding) | B32.06, B32.19 |
| B32.28 | `may_seat`, with `may_sit` its first conjunct; `selection_of` | VEN_C edit 4; PES_FA_B decision 1 (the `may_seat` form) | BUILD | EQUAL | B32.27; Batch B21 (`may_sit`) |
| B32.29 | the warrant clause and the eligibility ask | VEN_C edit 5 | BUILD | EQUAL | B32.28 |
| B32.30 | the lot | VEN_C edit 6 | BUILD | EQUAL | B32.29 |
| B32.31 | the audit at exit, read when asked | VEN_C edit 7; SYN_A §4 (`audits_due`) | BUILD | EQUAL | B32.30, B32.24 |
| B32.32 | the convening condition is read before a sitting fires | REST_2 W5 | BUILD | MOVER(behaviour) | B32.20, B32.22 |
| B32.99 | re-pin and close readings | `V12_STRUCTURE_part4.md` E-1 | BUILD | MOVER (the re-pin) | B32.01 to B32.32 |

Not in this batch, and where each is: COL_A's grounding row changes (`15_INSTITUTIONS_COLONIAL_grounding_F`, B40); SYN_A §2's `obligation` leverage source and `owed_to`, `forborne`, `upkeep_owed`, `hands_open` (VEN-A, PAP-D, BYZ-B, BYZ-C, B33); SYN_A §3's `passes_through`, `hand_term` keys and `resolve_anchor`'s `{venue:}` form (BYZ-C, VEN-D, B33); SYN_A §5's fixtures other than `presumption_gain` and `dignity_grades` (each with its B33 reader, SYN_A §3.6 rule 3); SYN_A §6's other rows (`consecration`, `debt_suit`, `security_bench`, `enrolment_ballot`, `audit`, `quo_warranto`, B33); SYN_B edit 2 (the prehistory, B39) and its gates 2 and 4 (B39), gate 5 (B33, PAP-C); SYN_B §6 (COL_D edit 4, B33; UNDECIDED 7); HAP_B edits 1–3 (B21); `16_PESSIMIST_FA_B` decisions 1–4 (B21: `may_sit` landed there); `U5d_FA_owed_edits` §1, §2, §4–§9 (B21), §10 (B39); REST_2 W1 (B20), W2 (B24), W3 (B35); PAP_A edit 5 (B21s, UNDECIDED 4).

### B32.01 — the instruments registry, empty, and its one loader · COL_A edits 1–2 with SYN_A §1 · BUILD · HASH EQUAL
- SOURCE: COL_A "Exact edits, by owner" 1, 2, "Gate" (loader refusals), "Falsifier" (control); SYN_A §1 ("Top level", "Form row", "Loader, beyond COL-A's refusals", "`seeded:` row"), "Gate" 1–2; rulings A-10, A-21, A-22, A-41; closes the `covenant.writes_note` "ITS READERS ARE DEFERRED" (with B32.04).
- ADVANCES: none of the nine; the kit's one home for every form a document can take (SYN_A "What it changes" 1).
- INSTRUCTION:
  1. First, NEW `engine/season/tests/test_instruments.py` (U3 §6.1: MISSING, "write it as the batch's first commit") and NEW `engine/season/tests/test_inst_syn_a_kit.py` with the loader refusals below, read red (no loader).
  2. NEW `engine/season/instruments.yaml`, "the single owner of the forms". "Header states the claim and the count" (the claim: "an instrument is just defined parameters"; the count read by command, C3-N31). "Two keys, `forms:` and `seeded:`" (SYN_A), each `[]` in this commit. Row schema, every key required unless marked (COL_A's, with SYN_A's additions):
     ```yaml
     forms:
       - id:          farm
         made_by:     covenant            # issue | covenant
         grantor_act: issue               # a rosters.yaml: remit_acts member the granting seat must hold
         term:        4                   # seasons; null = while the grantee holds the conferred seat
         renewal:     both                # grantor | both | none
         confers:                         # optional: the seat the grant establishes and confers on the grantee
           post:       "Farmer"
           at:         grant_ground
           remit_acts: [issue]
           conferral:  appointed
           revocation: rung_above_in_holdings
           # audit_at_exit: <arrangements.yaml id>   (optional, SYN_A)
         due:
           - {by: grantee, kind: transfer.made, every: once, to: grantor_rung}
         forbears:
           - {by: grantor, kind: requisition.taken, over: grant_ground}
         lapse:       reverts             # reverts | stands
         hardens:     false
         record_kind: dispensation        # dispensation | debt          (default dispensation)
         bearer:      false               # true: entitled = the Record's holder; bound = a live commit to its terms
         recites:     false               # true: the Record may carry a `recites` list
         basis:       command             # command | purview (issue-made only)
         # clause value sets:  by: grantor | grantee | addressee   over: grant_ground | grantee | named   to: grantor_rung | grantee_rung | grant_ground | named_rung
     ```
     (an example of the schema, not a row of this commit).
  3. NEW `engine/season/data/instruments.py`, "the one loader", in "`data/arrangements.py`'s idiom (`_refuse_unknown`, `_refuse_not_in`)". COL_A's refusals: "an unknown key; a `kind` that is not a `data/verbs.py::DEED_KINDS` member; a `grantor_act` off `REMIT_ACTS`; a `confers:` whose `conferral` or `revocation` is off its roster or whose `remit_acts` is not a subset of `REMIT_ACTS`; `made_by` off `{issue, covenant}`; `every` that is neither a positive int nor `once`; `over` off …; `to` off …" (the value sets widened by SYN_A, step 2). SYN_A's: "`basis` off `{command, purview}`, or present on a row whose `made_by` is `covenant`; `record_kind` off `{dispensation, debt}`; `bearer: true` on a row whose `made_by` is not `covenant`; `by: addressee` on a row whose `made_by` is not `issue`; `over: named` or `to: named_rung` on a row with no clause able to name one; `confers.audit_at_exit` that is no `arrangements.yaml` id; `recites: true` with `record_kind: debt`." The `seeded:` rows: "Keys: `id`, `kind` (a `record_kinds` member), `form` (a `forms:` id, or absent for a `resolution`), `via` and `held_at` (seat row ids), `to` (case ids), `at` (an anchor), `terms`, `amounts`, `recites` (`{for: <seat id | case id>, deeds: [<prehistory deed id>]}`), `source`. The loader refuses an unknown key, a `form` whose `record_kind` is not the row's `kind`, a `recites` on a kind or form that does not admit it, and a `via` or `held_at` that is no seat row." Exposes `INSTRUMENTS: dict[str, Form]` and `SEEDED: tuple` ("frozen dataclasses `Form`, `Clause`"). "Import-order: `DEED_KINDS` is derived in `data/verbs.py`; the loader imports it lazily inside `_load()`" as `data/arrangements.py` does for its derived map (the source's `[UNVERIFIED]`: the producer confirms the lazy import loads and records it in the commit body).
  4. `engine/season/data/files.py` gains `INSTRUMENTS_YAML`; `engine/season/data/__init__.py::load_all` calls the loader.
  5. Glossary: row *instrument* (and *form*): owner → pointer to `data/instruments.py::INSTRUMENTS`; "instrument": a document that binds its parties to stated duties, as a legal instrument does.
- WHERE: NEW `engine/season/instruments.yaml`; NEW `engine/season/data/instruments.py`; `engine/season/data/files.py` (`INSTRUMENTS_YAML`); `engine/season/data/__init__.py` (`load_all`); NEW `engine/season/tests/test_instruments.py`; NEW `engine/season/tests/test_inst_syn_a_kit.py`; `unified/U1_GLOSSARY.md` (*instrument*, *form*).
- TESTS: `test_instruments.py::test_each_malformed_form_row_is_refused_naming_it` (one planted row per COL_A refusal), `test_inst_syn_a_kit.py::test_kit_loader_refusals` (one per SYN_A refusal, including "A form row with `by: addressee` under `made_by: covenant`"), `::test_seeded_row_refusals`, `::test_neutral_until_used` (SYN_A gate 1) `[ASSUMPTION: test names beyond the files the sources name; E-3]`; red before step 3; green after.
- FALSIFIER and CONTROL: a planted malformed row that loads. Control (SYN_A gate 1): "With the registry empty … `build_realm(0)` `content_hash` at build, one season and two seasons equals the pre-item hash (`PYTHONHASHSEED=0`)".
- GATE: `python -m pytest engine/season/tests/test_instruments.py engine/season/tests/test_inst_syn_a_kit.py -q` → pass; realm hash (`HASH READING`) at seed 0, one season → equal to B28's after-reading reading (`reading @<sha>`).
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `data/arrangements.py::_refuse_unknown`, `::_refuse_not_in`, `data/verbs.py::DEED_KINDS`, `data/files.py::ARRANGEMENTS_YAML` (the pattern), `data/__init__.py::load_all`; V12 Batch B21 (`06_FA_decree_binds`, FA-P1: a writ's terms reach its addressee).
- GLOSSARY: *instrument*, *form* (step 5).
- COST and TIER: small build; `sonnet`, `high` (COL_A, SYN_A: "no `opus` node").
- LANDS IT: B32's `valoria-author` producer, `isolation: worktree`; `Item: B32.01`, `[skip ci]`.

### B32.02 — the sixteen forms · COL_A's ten rows with SYN_A's changed cells, and SYN_A's six rows · BUILD · HASH EQUAL
- SOURCE: COL_A edit 1 ("The ten rows of audit §4.3 … each `grade: assumption`, each with a `source:` string"); `audits/15_INSTITUTIONS_COLONIAL.md` §4.3 (the table, copied below); SYN_A §1 ("COL-A's ten rows, changed cells only", "Six rows added"); rulings A-21, A-22 (`basis`), A-41 (no `corvee` form).
- ADVANCES: none of the nine; every treaty and grant in canon has a form a person can keep, break or cite.
- INSTRUCTION: append to `forms:` sixteen rows, each `grade: assumption`, each with a `source:` string naming the research paragraph (COL_A's re-grounding names: `staple` `research/proactive_governance_scale_research_v1.md:123`, `:84`; `land_grant` `.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md:103`; `wardship` `.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:502-506`; `homage` `research/governance/political_hierarchy_standing.md:457-461`). "Amounts are **not** in the form." "Posts in `confers:` are generic labels `[ASSUMPTION; the names are Jordan's, through references/names_index.yaml]`."
  1. The ten (audit §4.3, by row: made by · confers · due · forbears), each clause in the schema's keys and kinds:
     `homage` covenant · — · grantee: a relief (`transfer.made` to the grantor's rung) once at each succession of either seat; grantor re-issues at each succession (`renewal: both`) · grantor: `tenure.closed` by `revoke`, `rung.seized`, `requisition.taken` over the grantee's ground;
     `land_grant` issue · a `Lord`-post seat at the ground, `conferral: appointed` · grantee: a `rung.founded` within the term, or the grant reverts · grantor: `requisition` over the ground for the first term;
     `march` issue · a warden's seat with `dispatch` and `determine` at a pass or gate territory · grantee: a `garrison` kept in repair (`site.restored`) · grantor: `open_case` over the warden's men;
     `farm` covenant · a farmer's seat with `issue` at the ground, term 4 · grantee: an advance once, a rent each season, both `transfer.made` to the grantor's rung · grantor: `requisition` over the ground while it runs;
     `charter` issue · the body's head seat, `conferral: elected` · grantee: a fee at each succession of the grantor's seat · grantor: `revoke`, `confer` on the chartered seats;
     `staple` issue · a factor's seat with `issue` at the settlement · grantee: a rent each year · grantor: a second `staple` of that kind there (`dispensation.issued` with the same `of:`);
     `immunity` issue · — · grantee: none · grantor: `requisition`, `seize`, `open_case` over the ground;
     `tribute` covenant · — · grantee: `transfer.made` each year · grantor: `march` on the grantee (the `protected` variant's `march.declared` due is not authored here `[ASSUMPTION: one row per form; basis: §4.3 names it a variant]`);
     `wardship` covenant · — · grantee: the named person's `residence.changed` to the grantor's settlement, once · grantee: the person's return while it runs;
     `capitulation` covenant · — · grantee: `place.surrendered`, once · grantor: `rung.razed`, `requisition` over the place for the first term.
     SYN_A's changed cells: "`homage`, `land_grant`, `march`, `charter`: `recites: true`. `charter`, `staple`, `immunity`: `hardens: true`. `farm`, and every row whose `confers:` seats an officer over other people's ground (`march`, `land_grant`): `confers.audit_at_exit: audit`. `homage`: no `term` (… `renewal: both`)." `confers.audit_at_exit: audit` names a row B33 lands (COL-C edit 1): until it does the loader's refusal would fire, so those three cells are written by B33's `audit` item `[ASSUMPTION — basis: SYN_A's refusal "`confers.audit_at_exit` that is no `arrangements.yaml` id"]`. A clause whose `kind` is not a `DEED_KINDS` member at landing is left out of its row and listed in the commit body (SYN_A: "a verb with no success kind yet is left out of the row until its lane lands one").
  2. The six, verbatim from SYN_A §1 "Six rows added" (`warrant`, `commission`, `avoidance`, `interdict`, `tithe`, `debt`, each as the YAML block there writes it, `basis: purview` on `avoidance`, `record_kind: debt` and `bearer: true` on `debt`). `debt`'s `record_kind: debt` loads only after B32.03 adds the kind: land `debt` in B32.03's commit `[ASSUMPTION: order inside the batch]`.
- WHERE: `engine/season/instruments.yaml` (`forms:`).
- TESTS: `test_instruments.py::test_every_shipped_form_loads` ("every shipped row loads (the count read by command at the run: these ten plus SYNTHESIS-A's six; C3-N31)"); red before (no rows). `[ASSUMPTION: test names; the item creates them — basis: no source file of the suite names them (E-3); repair lane R2d]`
- FALSIFIER and CONTROL: a form row that names a kind off `DEED_KINDS` and loads. Control: nothing reads a form yet; the realm hash at seed 0, one season, equal to B32.01's.
- GATE: `python -m pytest engine/season/tests/test_instruments.py -q` → pass; `python -c "from engine.season.data.instruments import INSTRUMENTS; print(len(INSTRUMENTS))"` → the count, quoted (16 expected, SYN_A gate 2, less any clause-less row left out).
- HASH MOVERS: none.
- DEPENDS ON: V12 B32.01.
- GLOSSARY: none.
- COST and TIER: edit (data); `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.02`, `[skip ci]`.

### B32.03 — a dispensation may name a form; `debt` is a Record kind · COL_A edit 3; SYN_A §2 rows 1–5 · BUILD · HASH EQUAL
- SOURCE: COL_A edit 3; SYN_A §2 table rows `record_kinds.dispensation`, `record_kinds` (`debt`), `record_kinds.resolution`, `record_kinds` (no `roll`), `record_sourced_operands`; rulings none new.
- ADVANCES: none of the nine.
- INSTRUCTION: `engine/season/rosters.yaml`:
  1. `record_kinds`: "The `dispensation` row's content keys gain `form` (optional; a writ with none is today's bare decree) and `amounts` (optional; a mapping from clause index to an int)" and `recites` (SYN_A, X-03). "The loader refuses `form` on any other kind."
  2. `record_kinds`: "add `debt: [terms, to, kind, amount, at]`" (VEN-B edit 1 as SYN_A carries it).
  3. `record_kinds.resolution` (CR-36's row, landed in B21c): "optional content key `recites`".
  4. "**no** `roll`" (X-04): nothing added.
  5. `record_sourced_operands`: "add `debt: {subject: terms, kind: kind, amount: amount}`".
  6. B32.02 step 2's `debt` form row lands here.
- WHERE: `engine/season/rosters.yaml` (`record_kinds`, `record_sourced_operands`); `engine/season/data/rosters.py` (the `form` refusal on other kinds) `[ASSUMPTION: the record-kind loader is in `data/rosters.py`; the producer greps `record_kinds` and records the file]`; `engine/season/instruments.yaml` (`debt`).
- TESTS: `test_inst_syn_a_kit.py::test_form_on_a_non_dispensation_kind_is_refused` `[ASSUMPTION: name]`; red before.
- FALSIFIER and CONTROL: a `form` key on a `works` Record that loads. Control: realm hash equal to B32.02's (no Record carries the keys).
- GATE: `python -m pytest engine/season/tests/test_inst_syn_a_kit.py engine/season/tests/test_record_kind_fold.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 B32.02; V12 Batch B21c (CR-36: the `resolution` kind; SYN_B: "if CR-36 has not landed, this proposal lands the roster row alone"; STOPS IF `resolution` is not in `record_kinds` at the open: land the row alone, as SYN_B says).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.03`, `[skip ci]`.

### B32.04 — the readers of an instrument · COL_A edits 5–7; SYN_A §4 rows 1–4 · BUILD · HASH EQUAL
- SOURCE: COL_A edits 5, 6, 7, "Gate" (the hand-built tribute; `kept` as the payee reads it), "Falsifier"; SYN_A §4 rows `instrument_of…breaches`, `in_force`, `owed`, `kept`; SYN_A gate 3 (its `dues` arms); rulings A-21, A-22.
- ADVANCES: none of the nine; `covenant`'s readers (with B32.05).
- INSTRUCTION:
  1. `engine/season/queries/world_q.py`:
     ```python
     def instrument_of(w, record_id) -> Optional[Form]      # the form a live dispensation names, or None
     def clauses_binding(w, record_id, pid) -> tuple[Clause, ...]
         # the `due` clauses whose `by:` side `pid` is: grantor = the Record's maker; grantee = its `to`
     def in_force(w, record) -> bool
         # SYN_A: `covenant_in_force(w, rid) > 0` for a covenant-made form; unmatured `Record.stages` for an issue-made one.
         # `dues` and `breaches` ask it and nothing else
     def owed(w, record, clause) -> int
         # VEN-B's `debt_state` arithmetic, for any clause whose instrument names an amount: the amount, less the
         # `transfer.made` Events to the clause's place whose act cites the Record (`debt_state`, `debts_held`, `debts_owed` not added)
     def dues(w, pid) -> tuple[Referent, ...]
         # for each live formed instrument `pid` is party to (he holds it, or his own ledger holds its content
         # claim, FA-P1's `writs_addressed` test), each binding `due` clause with no matching deed in its
         # current period -> the clause's target, classed by `referent_classes`, stamped on out[0] by the one
         # stamp site (`vacancies`' shape). SYN_A: "`dues` stamps a clause while `owed > 0`; a party to a `bearer` form is read as X-09 states"
     def breaches(w, pid) -> tuple[Referent, ...]
         # where person_q.kept(p, record) < 0: the other party (Person) and the conferred seat (Office).
     ```
     "Matching deed": "an Event of the clause's `kind` whose doer is the bound party (or a holder of the conferred seat) and whose target is the clause's, inside the period `[made + k·every, made + (k+1)·every)`." "`breaches` reads only `pid`'s ledger." `questions_for` splices `dues` and `breaches` into the classed tuple beside `vacancies`.
  2. `engine/season/queries/person_q.py::kept(p, record_content, now) -> int`: "Person-side, computed when read, `suspicion_of`'s shape (FA-P1 edit 4): +1 for each elapsed period in which `p` holds a claim of the due deed by the bound party; −1 for each elapsed period in which he holds none; −1 for each claim of a forborne deed by the bound party over the clause's ground. Distinct origins once (ED-IN-0322). Nothing is written."
  3. "Lapse and renewal. No MATTER pass is added." At maturity "a form with `lapse: reverts` whose `renewal` party has not re-made it is no longer live for `dues` and `breaches`" (through `in_force`); "the conferred seat's `hold` carries the same term (FA-P3's `term:` mechanism)".
  4. STOPS IF `queries/world_q.py::covenant_in_force` (`14_VERBS_SOCIAL1_B` §3, B28) is absent at the open: `in_force` for a covenant-made form reads "unmatured `Record.stages`" as for an issue-made one, the call is left as a marked line naming B28, and the commit body says so (UNDECIDED 1).
- WHERE: `engine/season/queries/world_q.py` (`instrument_of`, `clauses_binding`, `in_force`, `owed`, `dues`, `breaches`; `questions_for`); `engine/season/queries/person_q.py` (`kept`); `engine/season/rosters.yaml` (`referent_classes`, the class `dues` stamps) `[ASSUMPTION: a class row is needed for the stamp — basis: "classed by `referent_classes`"]`.
- TESTS: in `test_instruments.py`, written first and read red: `test_tribute_dues_return_each_period` ("on a hand-built two-seat world with one `tribute` made at tick 0, `every: 1`: `dues(payer)` names the payee's rung in season 1; after a `transfer.made` by the payer to that rung it does not; in season 2 it does again"); `test_kept_differs_by_what_the_payee_witnessed` ("`kept` as the **payee** reads it is +1 after a season whose payment he witnessed and −1 after a season whose payment was made and not witnessed by him"); `test_bystander_is_offered_nothing`; in `test_inst_syn_a_kit.py`: `test_one_of_each_dues` (SYN_A gate 3's `dues` arms: "`dues` stamps the tribute payer and the debtor and not a bystander; after a `transfer.made` to the clause's place the stamp is gone and returns next period for the tribute and not for the debt"). SYN_A gate 3's `comply` arm moves to B33 (UNDECIDED 6). `[ASSUMPTION: test names; the item creates them — basis: no source file of the suite names them (E-3); repair lane R2d]`
- FALSIFIER and CONTROL: "delete the period test in `dues` (any past payment then matches for ever); the season-2 assertion … reddens"; "A bystander is offered nothing"; "A `forbears` clause refuses no act"; "A `debt` whose debtor `dues` does not stamp". Control: no instrument in the realm, hash equal to B32.03's.
- GATE: `python -m pytest engine/season/tests/test_instruments.py engine/season/tests/test_inst_syn_a_kit.py -q` → pass; realm hash (`HASH READING`) at seed 0, one season, equal to B32.03's.
- HASH MOVERS: none (no instrument exists in a built world until B32.08).
- DEPENDS ON: V12 B32.03; V12 Batch B21 (`06_FA_decree_binds`: `writs_addressed`, `suspicion_of`); V12 Batch B28 (`covenant_in_force`; STOPS IF, step 4); EXISTS-IN-TREE `queries/world_q.py::vacancies`, `::questions_for`.
- GLOSSARY: none (*due*, *breach* are plain words).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.04`, `[skip ci]`.

### B32.05 — `issue` and `covenant` may name a form · COL_A edit 4; SYN_A §2 `choice_sourced` · BUILD · HASH MOVER(behaviour)
- SOURCE: COL_A edit 4, "What it changes" 1; SYN_A §2 row `choice_sourced`.
- ADVANCES: none of the nine; a writ and a covenant carry a readable shape.
- INSTRUCTION: "`engine/season/rosters.yaml: choice_sourced`. `covenant: [form]`, `issue: [form]`: the route `marshal`'s `role` and `march`'s `posture` take (`data/verbs.py::_load_choice_sourced`, `decision/options.py::operand_bags`; the function body was not opened [UNVERIFIED: that a choice roster may be filtered per candidate])." Step 0 (SITE, §5.7): open `operand_bags` and record in the commit body whether a choice roster can be filtered per candidate; if it cannot, the filter is added there, in the same shape `posture`'s fan uses. "The fan is the forms whose `made_by` is the verb and whose `grantor_act` the exercised seat's grant carries, **plus the empty choice** for `issue` (a bare decree). `loop/effects_information.py::_mint_document` writes the chosen `form` into the Record's content." Additions to `rosters.yaml` go at the end of their family's block (CIP part 2 §5 note 1).
- WHERE: `engine/season/rosters.yaml` (`choice_sourced`); `engine/season/decision/options.py` (`operand_bags`); `engine/season/loop/effects_information.py` (`_mint_document`).
- TESTS: `test_instruments.py::test_issue_offers_the_bare_decree_and_each_granted_form` `[ASSUMPTION: name]`; red before.
- FALSIFIER and CONTROL: an `issue` through a seat whose grant lacks the form's `grantor_act` offered that form. Control: the empty choice reproduces today's bare decree.
- GATE: `python -m pytest engine/season/tests/test_instruments.py -q` → pass; COL_A's realm reading moves to B32.08 (it needs the seeded instruments); seed 0, one season: the content hash read and recorded (moved: the formation fans of `issue` and `covenant` widen).
- HASH MOVERS: every seeded world with an `issue` or `covenant` formed (the fan gains choices). Declared; re-pinned at B32.99.
- EXPECTED RED UNTIL B32.99: the realm pins.
- DEPENDS ON: V12 B32.04; EXISTS-IN-TREE `data/verbs.py::_load_choice_sourced`, `decision/options.py::operand_bags`, `loop/effects_information.py::_mint_document`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.05`, `[skip ci]`.

### B32.06 — one closed key set over a seat row · SYN_A §3 · BUILD · HASH EQUAL
- SOURCE: SYN_A §3 ("One seat schema (D-U1-11r; S-24)", the refusal table, the tables' loader paragraph); `U3_CONFLICT_LEDGER.md` C3-L9; rulings A-12, A-13 (APPLIED, `04:331`).
- ADVANCES: none of the nine; a seat key nobody reads cannot be authored.
- INSTRUCTION: "`data/rosters.py::_load_offices` refuses no unknown row key today … this edit gives it **one closed key set** over a seat row, the tree's keys (`id, post, rung, body, faction, remit_acts, scope_rung, binds, conferral, revocation, upkeep, holder, obligees, source, note`, read from `offices.yaml` at landing, not from this list) plus the keys below as each lands, and a refusal naming the row and the key." Read the key set from the `offices.yaml` of this batch's base (it carries B04's `capability:`, B05's `modifier:`, B21's `term:` and every key an earlier batch added) and record it in the commit body. In this commit, refusals for the keys that already exist: "`upkeep` not an int ≥ 0"; "`modifier` not a member of `sigma_leverage.LEVEL_SIGMA`" (if B05 left that refusal unwritten). The rows for `dignity` (B32.12), `audit_at_exit` (B32.27) are added by the items that land the keys; `passes_through`, `hand_term` by B33. "`audited:` (COL-C edit 2) is not a key. `founding:` (BYZ-A edit 1) and `instruments:` (PAP-C edit 1) are not sections of this file." (`offices.yaml`'s `founding:` block of B04.23 is a different meaning, `06_FA_office_capabilities` edit 5, and stays.)
- WHERE: `engine/season/data/rosters.py` (`_load_offices`).
- TESTS: `test_inst_syn_a_kit.py::test_unknown_seat_key_is_refused` (SYN_A gate 2: "A planted `patronage:` key on an `offices.yaml` row is refused as an unknown key"; and "A seat row carrying `audited:` that loads" is the falsifier); red before. `[ASSUMPTION: test names; the item creates them — basis: no source file of the suite names them (E-3); repair lane R2d]`
- FALSIFIER and CONTROL: a planted `audited:` that loads. Control: every shipped row loads; realm hash equal to B32.05's after-reading.
- GATE: `python -m pytest engine/season/tests/test_inst_syn_a_kit.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `data/rosters.py::_load_offices`, `::SEAT_ROW_BY_ID`; V12 Batch B05 (B05.20, `modifier:`), Batch B21 (`term:`).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.06`, `[skip ci]`.

### B32.07 — standing passes down the seat, at a discount · SYN_B edit 1 · BUILD · HASH EQUAL
- SOURCE: SYN_B "Exact edits" 1, "Gate" 1, 3, "Falsifier"; SYN_A §4 row `legitimacy`; rulings A-17, A-18, A-19, A-43, A-58, A-66.
- ADVANCES: none of the nine; the deed race's odds read this (A-19; B32.14).
- INSTRUCTION: `engine/season/queries/person_q.py::legitimacy`: "Signature gains `seat: Optional[str] = None, fx=None`. After the existing sum:"
  ```python
      g = float(fx.get("presumption_gain")) if (seat is not None and fx is not None) else 0.0
      if g:
          axis_w = projected_axes(p, scar_shift)
          weight, successor = g, holder
          for prior in prior_holders(p.ledger, seat, holder):      # newest first; p's own reading
              if took_by_force(p.ledger, successor, seat):         # p believes `successor` seized the seat:
                  break                                            #   nothing from before him passes
              for c in attributed_deeds(p.ledger, prior):          # NOT windowed: age is the claim's own fade
                  total += weight * deed_term(p, axis_w, c)
              weight, successor = weight * g, prior
  ```
  "`prior_holders(ledger, seat, holder)`: the persons whose `hold` on `seat` closed before `holder`'s opened, in `p`'s own `tenure.opened` / `tenure.closed` claims naming the seat, newest first. It is the same reading `14_VERBS_BINDING_C` edit 9 (`seat_belief_declines`) … one helper, beside `attributed_deeds`." If B21 landed that reading as a helper, `prior_holders` composes on it and is not written twice (SITE: grep `seat_belief_declines` at the open, record it). The source's `[UNVERIFIED]` that a `tenure.closed` claim's subject names both person and seat for a `hold` is checked by the first test. "`took_by_force(ledger, person, seat)`: `p` holds a `standing_routes.kinds.dominance` deed attributed to `person` whose subject is `seat` or its rung." "Person-side, no World (AX-2). The two existing callers pass no `seat` and are unchanged." "`person_q.accomplishment` … is not added." `data/fixtures.py: presumption_gain`: "ships 0; proposed 0.5; sweep {0, 0.5, 0.75, 1.0}; NUMBER row, graded `assumption`" (its `hole_register.yaml` row from B32's H block, slot 1).
- WHERE: `engine/season/queries/person_q.py` (`legitimacy`, NEW `prior_holders`, NEW `took_by_force`); `engine/season/data/fixtures.py` (`presumption_gain`); `engine/season/hole_register.yaml` (its NUMBER row); NEW `engine/season/tests/test_inst_syn_b_deed_ledger.py`.
- TESTS: in the new file, red before: `test_control_legitimacy_unchanged_at_zero` (gate 1: "`legitimacy` returns today's value for every (person, holder) pair of the cast"); `test_the_chain` (gate 3: "an heir whose predecessor `p` knows reads own + 0.5 × the predecessor's; one whose predecessor `p` has never heard of reads own; a third holder reads 0.25 of the founder; a holder `p` believes took the seat by force reads own only, and so does everyone after him"). `[ASSUMPTION: test names; the item creates them — basis: no source file of the suite names them (E-3); repair lane R2d]`
- FALSIFIER and CONTROL: "`prior_holders` read from the world's Tenures instead of `p`'s claims: gate 3's 'never heard of' arm reddens"; "A `legitimacy` that differs from today's at `presumption_gain` 0". Control: realm hash equal to B32.06's.
- GATE: `python -m pytest engine/season/tests/test_inst_syn_b_deed_ledger.py -q` → pass; `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`) (the NUMBER row).
- HASH MOVERS: none (`presumption_gain` ships 0).
- DEPENDS ON: EXISTS-IN-TREE `queries/person_q.py::legitimacy`, `::deed_term`, `::attributed_deeds`, `::projected_axes`, `rosters.yaml: standing_routes`; V12 Batch B21 (`14_VERBS_BINDING_C` edit 9).
- GLOSSARY: none.
- IDS: H block slot 1.
- COST and TIER: small build; `sonnet`, `high`; gate 2's reading (B39) is the `opus` read SYN_B names.
- LANDS IT: B32's producer; `Item: B32.07`, `[skip ci]`.

### B32.08 — the four seeded Records · SYN_B edit 3; SYN_A §1 `seeded:` · BUILD · HASH MOVER(behaviour)
- SOURCE: SYN_B "Exact edits" 3 (the four rows and the three bullets), "What it changes" 2; SYN_A §1 "`seeded:` row" (the mint); COL_A "Gate" (the realm reading); rulings A-17, A-18.
- ADVANCES: none of the nine; the paper NPC-008's case turns on exists.
- INSTRUCTION:
  1. `engine/season/instruments.yaml: seeded`, the four rows exactly as SYN_B §3 writes them: `ins_containment_charter` (`dispensation`, form `immunity`, `via: off_king`, `held_at: off_cardinal_temperance`, `to: ["NPC-021"]`, `at: {territory: "T9"}`); `ins_consecration_first_king` (`resolution`, `via: off_confessor`, `held_at: off_cardinal_temperance`, `to: []`, `recites: {for: off_king, deeds: [deed_secession_k1, deed_secession_k2, deed_secession_k3]}`); `ins_settlement_hafenmark` (`dispensation`, form `homage`, `via: off_king`, `held_at: off_parliamentary_clerk`, `to: ["NPC-050"]`, `recites: {for: off_duchess_hafenmark, deeds: [deed_secession_h1, deed_secession_h2]}`); `ins_settlement_varfell` (the same, `to: ["NPC-052"]`, `recites: {for: off_duke_varfell, deeds: [deed_secession_v1]}`), each with SYN_B's `source:` string. The deed ids name the prehistory B39 lands (SYN_B edit 2); the loader does not check them against it here `[ASSUMPTION — basis: SYN_A's seeded refusals name no deed check]`.
  2. `boot/realm.py::build_realm` (was `harness/populated.py`): "mints each row once, through the existing mint, after seats are held, with the `hold` on the live holder of `held_at`; a vacant `held_at` is skipped and reported."
  3. The bullets: "The two `homage` rows are the instruments the built oaths of NPC-050 and NPC-052 to `off_king` are held under … The `obligees:` list keeps bare ids." "**No house holds its own paper.** The parties hold content claims, which is what `dues` and `kept` read."
- WHERE: `engine/season/instruments.yaml` (`seeded:`); `engine/season/boot/realm.py` (`build_realm`, the seeded pass).
- TESTS: `test_inst_syn_b_deed_ledger.py::test_no_house_holds_its_own_paper` ("A build in which a house's head holds the paper that recites his house's deeds" fails it); `test_instruments.py::test_seeded_records_minted_once` `[ASSUMPTION: names]`; red before.
- FALSIFIER and CONTROL: a house head holding his own paper; a vacant `held_at` minted. Control: with `seeded: []` the build hash equals B32.07's.
- GATE: `python -m pytest engine/season/tests/test_inst_syn_b_deed_ledger.py engine/season/tests/test_instruments.py -q` → pass; COL_A's realm reading: "`build_realm(0)` with SYNTHESIS-B §3's two seeded `homage` instruments …, two seasons, seeds 0–2: the count of `dues` referents stamped, and of acts whose `occasioned_by` is one, printed" (quoted in the commit body; a zero is reported, not asserted against).
- HASH MOVERS: the build hash (four Records minted; "A declared build-hash mover", SYN_B). Re-pinned at B32.99.
- EXPECTED RED UNTIL B32.99: the realm pins.
- DEPENDS ON: V12 B32.03 (`resolution` with `recites`), B32.06; V12 Batch B21c (CR-36: `off_parliamentary_clerk`, `resolution`); V12 Batch B03c (`boot/realm.py`); EXISTS-IN-TREE the Record mint `boot/realm.py` uses for `works`.
- GLOSSARY: none.
- NAMES: `harness/populated.py::build_realm` → `boot/realm.py::build_realm` (§5.10, B03c).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.08`, `[skip ci]`.

### B32.09 — a certificate recites deeds · SYN_B edit 4 (the writing half) · BUILD · HASH EQUAL
- SOURCE: SYN_B "Exact edits" 4 bullets 1 and 4 ("Commemoration needs no code"); `15_INSTITUTIONS_PAPACY_C` §2's bands as SYN_B quotes them.
- ADVANCES: none of the nine.
- INSTRUCTION: "Content key `recites: {for, deeds}` on `resolution` and on a `dispensation` whose form says `recites: true`. In play the list is written by the act that mints the Record: `determine` under a `disposes: Record` row writes the cited deed claims left standing at Overwhelming and Success and the first half of them, in cited order, at Partial …; `issue` and `covenant` of a reciting form write the deed claims the act cites." The `determine` arm is written at CR-36's disposal site (B21c); `issue`/`covenant` at `_mint_document`. "Commemoration needs no code."
- WHERE: `engine/season/loop/effects_information.py` (`_mint_document`); the `resolution` disposal site CR-36 landed (`loop/effects_governance.py` or `effects_information.py`; SITE: grep `resolution` at the open, record the symbol).
- TESTS: `test_inst_syn_b_deed_ledger.py::test_recites_by_band` (Overwhelming/Success all standing, Partial the first half in cited order, Failure none) `[ASSUMPTION: name]`; red before.
- FALSIFIER and CONTROL: a certificate that opens or gates a `hold` (SYN_B). Control: no computed act cites a deed with a reciting form at this tree; realm hash equal to B32.08's after-reading.
- GATE: `python -m pytest engine/season/tests/test_inst_syn_b_deed_ledger.py -q` → pass.
- HASH MOVERS: none at this tree (declared: any run where a reciting form is minted with cites).
- DEPENDS ON: V12 B32.08; V12 Batch B21c (CR-36's disposal site).
- GLOSSARY: row *certificate*: "a Record that recites deeds" (the content key `recites`); no new word.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.09`, `[skip ci]`.

### B32.10 — a cited certificate files one item per deed · SYN_B edit 4 (the request, built at its owner; lane D4) · BUILD · HASH EQUAL
- SOURCE: SYN_B edit 4 bullet 2 ("Request to SC's evidence owner … not edited": "citing a Record that carries `recites` files **one item per recited deed**, each the cell `(doer, kind, True)` at a Record's weight (1) and with the certifying act's seat as its origin … an impeachment of the paper … that draws Overwhelming strikes every item of its origin"); `15_INSTITUTIONS_SYNTHESIS_C` §4 (the same sentence asked for both sides of a docketed matter, B33.48); the owner's filing step, V12 B24.25 (`05_SC_evidence_and_rebuttal_B` edit 4 with ADM edit 3: the `speak` effect writes `filed` stages per admitted cite); lane D4's ladder record.
- ADVANCES: none of the nine; SYN_B gate 5 (a consecration petition with and without the predecessor's certificate) becomes readable, at B33.23 with PAP-C.
- INSTRUCTION: in `engine/season/loop/effects_information.py`, the `speak` effect's filing step that B24.25 landed (by symbol; SITE: open it first and record the function), one branch and no second filer: an admitted cite whose id is a Record carrying the content key `recites` (B32.09) files, in place of the one Record item, one item per recited deed: the cell `(doer, kind, True)` of that deed claim, at a Record's weight (1, the owner's unit), its `origin` the seat of the act that minted the Record (the certifying act's `via`), the band dispatch of B24.25 applied to each item exactly as to a single cite (Failure `excluded`, Partial half weight, Success full, Overwhelming full and `first`). The owner's impeachment rule ("strikes origin-wide only at overwhelming", B24.25's gate 3) then strikes every item of the paper's origin with no new code. A Record without `recites` files as today.
- WHERE: `engine/season/loop/effects_information.py` (the `speak` filing step); `engine/season/tests/test_inst_syn_b_deed_ledger.py` (B32.07's file).
- TESTS: `test_a_cited_certificate_files_one_item_per_deed` (a hand-built hearing; a Record reciting three deeds cited at Success files three items of weight 1, each the deed's cell, each with the certifying seat as origin; at Partial three items at half weight) and `test_an_overwhelming_impeachment_strikes_every_item_of_the_paper` `[ASSUMPTION: test names; the item creates them, E-3]`, written first, red.
- FALSIFIER and CONTROL: a cited certificate filed as one item; an item whose origin is not the certifying seat; an impeachment at Overwhelming that leaves one recited item standing. Control: no shipped or computed cite names a reciting Record at this tree (the seeded certificates recite B39's prehistory deeds, not yet landed): realm hash equal to B32.09's.
- GATE: `python -m pytest engine/season/tests/test_inst_syn_b_deed_ledger.py engine/season/tests/test_sc_hearing_evidence.py -q` → pass (`test_sc_hearing_evidence.py` is B24.25's and stays green).
- HASH MOVERS: none at this tree (declared: any run in which a reciting Record is cited).
- DEPENDS ON: V12 B32.09 (`recites`); V12 Batch B24 (B24.25: the filing step, its band dispatch and its impeachment rule); EXISTS-IN-TREE `loop/effects_information.py` (the `speak` effect).
- GLOSSARY: none (*certificate* is B32.09's row).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.10`, `[skip ci]`.

### B32.11 — a seat row may name no holder: it builds vacant · BYZ_A (the vacant-row build edit) · BUILD · HASH EQUAL
- SOURCE: BYZ_A "Exact edits" 3, paragraph "The vacant-row build edit (carried here for the kit …)"; SYN_B §6 ("Settled at the tree"); cited by SYN_B §6, COL_D edit 4 and PAP_E (B33).
- ADVANCES: none of the nine; the first vacant rows in the one order (BYZ_A's dignities; COL_D's and PAP_E's in B33).
- INSTRUCTION: "`harness/populated.py`'s minted-seat loop slugs `row["holder"]` into a person id and raises `Unspecified` when that person is not built, so a row with `holder: null` is refused today. Edit, in that loop, before the person lookup: a row whose `holder` is `None` builds its `Office` from the row exactly as a held row does and opens **no** `hold` (the seat is vacant, as a dead holder's seat is). `data/rosters.py` (`OFFICES_BY_HOLDER`) skips a `None` holder. The refusal of a named holder who is not built stays." If B39's `U5d_FA_owed_edits` §10 or another batch has already admitted vacant rows at the open, this item is a POINTER to it (SITE: run the test first).
- WHERE: `engine/season/boot/realm.py` (the minted-seat loop in `build_realm`); `engine/season/data/rosters.py` (`OFFICES_BY_HOLDER`); NEW `engine/season/tests/test_inst_byz_a.py`.
- TESTS: "`test_inst_byz_a.py::test_a_vacant_row_builds_vacant` (red before the edit: `Unspecified` naming `off_dignity_1a`; green after: the Office exists and no Tenure has it as object)" — planted with one `holder: null` row in a test overlay, since the six rows land in B32.12.
- FALSIFIER and CONTROL: "Delete the vacant-row edit: the build raises." Control: no shipped row has `holder: null`; realm hash equal to B32.10's tree.
- GATE: `python -m pytest engine/season/tests/test_inst_byz_a.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 B32.06; V12 Batch B03c (`boot/realm.py`); EXISTS-IN-TREE `data/rosters.py::OFFICES_BY_HOLDER`.
- GLOSSARY: none.
- NAMES: `harness/populated.py` → `boot/realm.py` (B03c).
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.11`, `[skip ci]`.

### B32.12 — dignities: the key, six vacant rows, `dignity_grades` · BYZ_A edits 3, 4 · BUILD · HASH MOVER(behaviour)
- SOURCE: BYZ_A "Exact edits" 3 (the key, the six rows), 4 (`dignity_grades`), "Gate" 1; SYN_A §3 (refusal row `dignity`), §3.6 row `dignity_grades`; rulings A-12 (precedence only as `modifier:`).
- ADVANCES: none of the nine; the Imperial Court gains seats.
- INSTRUCTION:
  1. "`engine/season/offices.yaml: seats` — one new optional key, `dignity:`, an int in `[1, dignity_grades]`. A row carrying it must have `remit_acts: []` and `revocation: null` (the loader refuses otherwise: a dignity with a remit is an office; a revocable one is not for life)." Refusal row added to B32.06's set: "`dignity` not an int in `[1, dignity_grades]`; or the row's `remit_acts` is not `[]`; or `revocation` is not `null`". Row data on `SEAT_ROW_BY_ID`, **no `Office` field** (UNDECIDED 2; B21's `term:` precedent). "A dignity's precedence on a roll, if authored, is the row's `modifier:`, never a step."
  2. The six rows, appended to `seats:` exactly as BYZ_A writes them (`off_dignity_1a` dignity 5; `off_dignity_2a`, `_2b` dignity 4; `off_dignity_3a`, `_3b` dignity 3; `off_dignity_4a` dignity 2; each `post: "[PLACEHOLDER] Dignity of the … grade"`, `rung: {territory: "T1"}`, `body: "Imperial Court"`, `faction: null`, `remit_acts: []`, `conferral: appointed`, `revocation: null`, `holder: null`, `obligees: []`, `source: "INST-BYZ-A…"`, `note: "[NEW]…"`). Posts are placeholders; names are Jordan's (`references/names_index.yaml`), listed in the PR body (D-19).
  3. "`engine/season/data/fixtures.py` — one fixture: `dignity_grades`, shipped 5, swept 3 / 5 / 7, read by the `offices.yaml` loader", with its NUMBER row (H block slot 2). A loader bound, not a dial (SYN_A §3.6: "— (loader bound)").
- WHERE: `engine/season/offices.yaml` (six rows); `engine/season/data/rosters.py` (`_load_offices`: the `dignity` refusal); `engine/season/data/fixtures.py` (`dignity_grades`); `engine/season/hole_register.yaml` (its row).
- TESTS: `test_inst_byz_a.py::test_dignity_row_with_a_remit_is_refused`, `::test_six_dignities_build_vacant` (BYZ_A gate 1) `[ASSUMPTION: names]`; red before.
- FALSIFIER and CONTROL: a dignity row with `remit_acts: [issue]` that loads. Control: the rows removed reproduce B32.11's hash.
- GATE: `python -m pytest engine/season/tests/test_inst_byz_a.py engine/season/tests/test_inst_syn_a_kit.py -q` → pass; seed 0 build hash (`HASH READING`) → moved (six vacant Offices), recorded.
- HASH MOVERS: the build hash ("the build hash (six vacant seats)", BYZ_A cost class). Re-pinned at B32.99.
- EXPECTED RED UNTIL B32.99: the realm pins.
- DEPENDS ON: V12 B32.11, B32.06; V12 Batch B04 (`06_FA_office_capabilities`); V12 Batch B21 (`06_FA_remit_grant_by_row`).
- GLOSSARY: row *dignity*: "a seat with no remit, held for life, an honour" (`offices.yaml` rows with `dignity:`); the owner is `data/rosters.py::SEAT_ROW_BY_ID`.
- IDS: H block slot 2.
- COST and TIER: edit and data; `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.12`, `[skip ci]`.

### B32.13 — `confer` on a dignity: oath, cited deed, terms · BYZ_A edit 7 · BUILD · HASH MOVER(behaviour)
- SOURCE: BYZ_A "Exact edits" 7, "Gate" 2, 3, "Falsifier"; Implementation block's standing sentences (A-6, A-7, A-8, A-30, A-81); `14_VERBS_BINDING_C_turnover.md` (B21: `confer`'s row, bands, `provisional_term`, `appointment.resisted`).
- ADVANCES: none of the nine; R-04.a's `confer` is B21's.
- INSTRUCTION (`loop/predicates.py::_req_confer`; `loop/effects_governance.py::_eff_confer`; the row text is the BINDING lane's):
  1. "two more conjuncts, asked only where the object row carries `dignity`: the conferee holds a live `oblige` to the exercised seat (`gate.py::sworn_to`: homage before investiture …); and the payload's `cites` names a deed claim about the conferee in the conferrer's own ledger (`own_ledger` of `to`, the form `survey` and `tell` use). A computed act binds `to` from the persons the conferrer holds deed claims about and ranks them by his own `deeds_judged`, which replaces the positional conferee for these rows."
  2. "the draw is `14_VERBS_BINDING_C_turnover.md`'s row … This file supplies, for a dignity row only, the terms in the SC form (C3-C10: what helps is levels): obstacle `difficulty` by the rung kind of the seat's rung and the `reception` of the live holders of seats of the row's body toward the conferee (hostile half; an empty body: none), `standard` raised at an open floor; the conferrer's levels: `proofs` for a `cites` claim held firsthand, `favour` for the conferee's regard for the conferrer above zero. The conferee's own highest live dignity is **not** a level here." Written at `seam/wrappers/sigma.py::contest_input`'s `confer` arm (where B21 put BIND_C's terms; SITE: record the symbol).
  3. "by degree: Overwhelming and Success open the `hold`, and the effect emits the investiture Event carrying the cited deed as an Observation; **WITNESS deposits the told claim** through its `told_by` channel … (full confidence on Overwhelming, the conferrer's own on Success); Partial opens it with `Term(tick + provisional_term·season)`; Failure opens nothing, emits `appointment.resisted`, and closes nothing. No new emitted kind."
- WHERE: `engine/season/loop/predicates.py` (`_req_confer`); `engine/season/loop/effects_governance.py` (`_eff_confer`); `engine/season/seam/wrappers/sigma.py` (`contest_input`, the `confer` terms); `engine/season/decision/options.py` (the `confer` counterparty binding for dignity rows).
- TESTS: `test_inst_byz_a.py::test_confer_dignity_draws_all_bands` (gate 2: "200 seeds, one hand-placed `confer` of `off_dignity_3a` by the King on a sworn person with one firsthand deed: all four bands occur; no band exceeds 0.9; with the roll pinned to Success every seed opens the hold"; `assert checked >= 200`), `::test_dignity_conferee_must_be_sworn_and_cited`; red before. `[ASSUMPTION: test names; the item creates them — basis: no source file of the suite names them (E-3); repair lane R2d]`
- FALSIFIER and CONTROL: "Delete the `cites` conjunct: a seeded conferral names a person the conferrer holds no deed of. Write the cited deed's claim from the effect instead of WITNESS: a person outside the kind's reach holds it." Control: a `confer` on a non-dignity row unchanged (B21's reading).
- GATE: `python -m pytest engine/season/tests/test_inst_byz_a.py -q` → pass; gate 3 (reach) at two seasons, seeds 0 to 2: "the count of `tenure.opened` on dignity rows and of `appointment.resisted` on them, reported … A zero count is a finding against reach …, not against this mechanism" (eight seasons and seeds 0 to 9 in the source; A-114).
- HASH MOVERS: "any run in which a `confer` on a dignity resolves". Re-pinned at B32.99.
- DEPENDS ON: V12 B32.12; V12 Batch B21 (BIND_C's `confer` row and draw, `provisional_term`); EXISTS-IN-TREE `state/gate.py::sworn_to`, `queries/person_q.py::deeds_judged`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet` producer, `high`; `opus` for the obstacle and leverage terms (step 2, BYZ_A tier line).
- LANDS IT: B32's producer; `Item: B32.13`, `[skip ci]`.

### B32.14 — `succeed` and `revoke` read the room; the deed race's odds · BYZ_E edits 1, 3; HAP_B edit 4 · BUILD · HASH MOVER(behaviour)
- SOURCE: BYZ_E "Exact edits" 1 (the `succeed` term table), 3 (the `revoke` term table), 5 ("Disqualification: nothing"), "Gate" 1, 2, "Falsifier"; HAP_B edit 4 ("Request to VB-C and BYZ-E … BYZ-E's `favourable` term … reads **the first listed title** as the designated one"); U3 §4.1 rows 75–76 (the deed race's odds in B32); rulings A-19, A-35, A-36, A-14.
- ADVANCES: none of the nine; A-19's deed race has odds.
- INSTRUCTION: the bands, kinds, `provisional_term` and draw keys are BIND_C's (B21) and are not re-written. This item supplies the terms at the `succeed` and `revoke` arms of `seam/wrappers/sigma.py::contest_input`, replacing B21's interim audience ("until then the seat's body"):
  1. `succeed` ("`contests: a standing`; no `counterparty:`"): pool BIND_C's; "`difficulty` by the rung kind of the seat's rung"; "`reception` (OBS member 8, hostile half): three audiences, each member `q` reading `legitimacy(q, claimant, seat)` (SYNTHESIS-B's chain, his own ledger; the resolver sums as `world_q.reception` sums a bench): the live holders of seats on the seat's rung and the rungs directly beneath it; the persons sworn to the seat (`gate.py::sworn_to`); the persons, cohorts by weight, residing where the seat's holder last resided. An empty audience is left out"; "`opposition` (OBS member 2): a rival who has docketed a claim on the same seat …; his skill score; none without a docketed rival"; "`standard` raised one step at an open floor under `acclamation`"; levels "`favour` from the favourable half of the same three audiences' `legitimacy`, and from a live occasion under `acclamation` at his place; `office` from the title seat he exercises (`Act.via` names the `successions` title; its row's `modifier:`, D-U1-01a; none ships)". HAP_B edit 4: the title term counts **the first listed title** of the seat's `successions` list as the designated one; "holding a later one earns no step."
  2. `revoke` ("`counterparty: to`"): "`difficulty` by the rung kind of the stripped seat's rung"; "`reception` (hostile half): one audience: the persons sworn to **his** seat (`establishment_of`), each reading his regard for the holder"; "`rank_gap` (OBS member 6) where a seat the holder holds stands above the revoker's exercised seat"; levels "`proofs` for a deed claim the revoker holds against the holder from the window". "No recall reaches `off_confessor` (A-36: `revocation: null`)." "`revocation.resisted` is the ground a later `arrest` or `march` can cite. It is not a dominance kind."
  3. Edit 5: nothing (the ban is asked by `_req_succeed`, settled at the tree in BYZ_E's U4c line). Edit 2 (who may claim) is CR-35's and A-19's set, landed (B21, B21c): nothing here.
- WHERE: `engine/season/seam/wrappers/sigma.py` (`contest_input`: the `succeed` and `revoke` terms); `engine/season/queries/world_q.py` (`reception`'s audiences, if B07's `reception` takes an audience list; SITE); NEW `engine/season/tests/test_inst_byz_e.py`.
- TESTS: in the new file, red before: `test_accession_title_and_presumption_are_odds` (gate 1: "400 seeds, a hand-vacated throne, the title-holder claiming: all four bands occur; the Success-or-better rate with the title exceeds the rate for the same person with the title stripped; with `presumption_gain` raised from its shipped 0 to 0.5 both rates rise. With the roll pinned to Success every seed opens the hold"); `test_recall_resisted_by_his_men` (gate 2: "400 seeds, a hand-placed `revoke` of a governor with three men sworn to his seat, in two arms (their regard for him high, low): `revocation.resisted` occurs in both and is more frequent in the first; no Partial seed opens a `ban` at any tick"); `test_heir_holds_first_listed_title_term` (HAP_B edit 4) `[ASSUMPTION: name]`.
- FALSIFIER and CONTROL: "Seat a title-holder whom every person present regards at the minimum, and a rival-free field: if he is seated in every seed, the `reception` term is not read. A Partial `revoke` that opens a `ban` at any later tick". Control: the roll pinned to Success resolves both verbs as today.
- GATE: `python -m pytest engine/season/tests/test_inst_byz_e.py engine/season/tests/test_in61_heir_hears_vacancy.py -q` → pass (HAP_B's G1 "in most seeds **and not in all**" still green); gate 3 (FA's `succession` situation, seeds 0 to 19) read at two seasons: "the distribution of bands, of provisional holds confirmed, and of seasons the seat stood vacant", quoted.
- HASH MOVERS: "any run in which a `succeed` or a `revoke` resolves". Re-pinned at B32.99.
- DEPENDS ON: V12 B32.07 (`legitimacy` with `seat`), B32.13; V12 Batch B21 (BIND_C rows; HAP_B edits 1–3), Batch B21c (CR-35, CR-37), Batch B27 (`05_SC_arrangement_rows_that_bind`); EXISTS-IN-TREE `state/gate.py::sworn_to`, `queries/world_q.py::establishment_of`.
- GLOSSARY: none.
- COST and TIER: small build; `opus`, `high` for the terms of steps 1–2 (BYZ_E tier line), `sonnet` for the tests.
- LANDS IT: B32's producer; `Item: B32.14`, `[skip ci]`.

### B32.15 — the `acclamation` row · BYZ_E edit 4 · BUILD · HASH EQUAL
- SOURCE: BYZ_E "Exact edits" 4; "What it changes" 3 ("Data only until a `convene` names it").
- ADVANCES: none of the nine; one occasion with an open floor.
- INSTRUCTION: `engine/season/arrangements.yaml`, appended last, the row exactly as BYZ_E writes it (comment block and `id: acclamation`, `disposal: none`, `bench_basis: none`, `floor: open`, `records_dissent: false`, `venue_min_rank: settlement`, `term_required: false`, `appeal_basis: none`, `interposed: [ceremony]`, `order: rank`, `proofs: [testimony]`, `disposes: none`, `disposal_reach: settlement`). "The loader accepts `disposal: none` and `disposes: none`." The source's `[UNVERIFIED]` (whether `bench_basis: none` must pair with `disposal: none`) is read by loading the row; a refusal is recorded and the pairing written as the loader asks.
  Added by the B24p fold (F.3): the row carries the five keys of B24p.03 (`rite`, `exchanges`, `authority`, `presumes`, `strikes`) or the loader refuses it: `acclamation`: `rite: address`, `exchanges: [1, 1]`, `authority: none`, `presumes: none`, `strikes: 0`.
- WHERE: `engine/season/arrangements.yaml`.
- TESTS: `test_inst_byz_e.py::test_acclamation_row_loads` `[ASSUMPTION: name]`.
- FALSIFIER and CONTROL: a row that moves a hash with no `convene` naming it. Control: realm hash equal to B32.14's after-reading.
- GATE: `python -m pytest engine/season/tests/test_inst_byz_e.py engine/season/tests/test_arrangements.py -q` → pass `[ASSUMPTION: `test_arrangements.py` exists — basis: U3 §3.1 names it for `05_SC_arrangement_rows_that_bind`]`.
- HASH MOVERS: none.
- DEPENDS ON: V12 B32.14; V12 Batch B24 (REST_2 W2's `speech_kinds` check).
- GLOSSARY: row *acclamation*: "a gathering before a crowd that decides nothing; what it produces is what those present heard".
- COST and TIER: edit (data); `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.15`, `[skip ci]`.

### B32.16 — the Confessor at Himmelenger; the Templars' command; a comment · PAP_A edits 1, 2, 4 · BUILD · HASH MOVER(behaviour)
- SOURCE: PAP_A "Exact edits" 1, 2, 4, "Gate" (first step), "Falsifier"; Implementation block (edits 1, 2, 4 wait on nothing).
- ADVANCES: none of the nine.
- INSTRUCTION:
  1. "First step, written before edit 1": `engine/season/tests/test_inst_pap_a.py::test_confessor_stands_at_himmelenger`: "`build_realm(0)`; walk `ancestry` from NPC-021's `reside` rung; count persons whose `reside` chain contains `terr_T9`. Expected before edit 1 (red, the defect): the chain is `b_s_003_market → q_s_003_market_quarter → set_s_003 → terr_T1`. Expected after edit 1 (green): the chain passes through `terr_T9` … the test prints [the count] and asserts only that the Confessor is among them."
  2. Edit 1: "`engine/season/npcs.yaml`, row `case: NPC-021`: old: `institution: null` / `home: b_s_003_market` / `tie: neighbour`; new: `institution: Church` / `home: b_s_036_cathedral` / `tie: institution`. `concerns: NPC-001` is unchanged. `tools/export_npc_roster.py --check` will report the row as a hand edit, which is its documented behaviour."
  3. Edit 2: "`engine/season/offices.yaml`, row `off_cardinal_fortitude`: old: `remit_acts: [issue, convene]`; new: `remit_acts: [issue, convene, dispatch]`; `note:` gains: *"`dispatch`: the Templars' command (PAPACY-A). [ASSUMPTION; medium; Jordan to correct; revert: drop `dispatch`, and the Church commands no force after FA-P2.]"*". If B21's `06_FA_remit_grant_by_row` left `meta.remit_unruled` in place, the row moves nothing until it goes; recorded either way.
  4. Edit 4: "`engine/season/arrangements.yaml`, the comment above `excommunication_deliberation`: add one sentence, *"Until three Church benches carry a realm `scope_rung:` (CR-60, PAPACY-A) the party must stand in `terr_T9`: `may_determine` asks `sits_over(seat, home_of(party))`."* A comment; no key." Written with B32.17 if CR-60 has landed at the open (then the sentence is stale on arrival and is not written; recorded).
- WHERE: `engine/season/npcs.yaml` (NPC-021); `engine/season/offices.yaml` (`off_cardinal_fortitude`); `engine/season/arrangements.yaml` (a comment); NEW `engine/season/tests/test_inst_pap_a.py`.
- TESTS: step 1's test, red before edit 1, green after.
- FALSIFIER and CONTROL: "each edit reverted reproduces the base build hash" (PAP_A's control).
- GATE: `python -m pytest engine/season/tests/test_inst_pap_a.py -q` → pass; `python tools/export_npc_roster.py --check` → the NPC-021 hand edit reported, nothing else; seed 0 build hash (`HASH READING`) → moved (NPC-021's `contain` and `reside` edges), recorded.
- HASH MOVERS: "A declared build-hash mover (one person's `contain` and `reside` edges and whom he is co-located with)". Re-pinned at B32.99.
- EXPECTED RED UNTIL B32.99: the realm pins.
- DEPENDS ON: V12 Batch B21 (`06_FA_remit_grant_by_row`); EXISTS-IN-TREE `engine/season/npcs.yaml` (`b_s_036_cathedral`, "`engine/season/npcs.yaml:105`, `:141` home persons there"), `tools/export_npc_roster.py`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `medium` (PAP_A tier line).
- LANDS IT: B32's producer; `Item: B32.16`, `[skip ci]`.

### B32.17 — three Church benches judge realm-wide · PAP_A edit 3 · BUILD · HASH MOVER(behaviour)
- SOURCE: PAP_A "Exact edits" 3, "Gate" bullet 2, "Falsifier"; CR-60 (B24a: the `scope_rung:` authoring key).
- ADVANCES: none of the nine.
- INSTRUCTION: "`engine/season/offices.yaml`, with CR-60's authoring key for the judging ground, spelled `scope_rung:` (… resolved by `populated.py::resolve_anchor` into the existing `Office.scope_rung`, which `state/gate.py::sits_over` reads and `purview_reaches` does not): `off_confessor`: `scope_rung: {realm: true}`; `off_cardinal_justice`: `scope_rung: {realm: true}`; `off_senior_inquisitor`: `scope_rung: {realm: true}`; the other four Church rows: no `scope_rung:`. `[ASSUMPTION; medium; Jordan to correct; revert: no `scope_rung:` on the three rows.]`" STOPS IF CR-60's key is not loaded at the open (`grep -n scope_rung engine/season/data/rosters.py`): then the item is HELD to CR-60 and the commit body says so.
- WHERE: `engine/season/offices.yaml` (three rows).
- TESTS: `test_inst_pap_a.py::test_church_benches_judge_realm_wide` ("`sits_over(off_confessor, terr_T1)` True; `sits_over(off_cardinal_prudence, terr_T1)` False; `purview_reaches(off_confessor, terr_T1)` still False (judging reach, not acting reach)"); red before. `[ASSUMPTION: test names; the item creates them — basis: no source file of the suite names them (E-3); repair lane R2d]`
- FALSIFIER and CONTROL: "A `scope_rung:` that changes `purview_reaches`." Control: the four other Church rows' `sits_over` unchanged.
- GATE: `python -m pytest engine/season/tests/test_inst_pap_a.py -q` → pass.
- HASH MOVERS: "which seat may open a case or sit on a bench". Re-pinned at B32.99.
- DEPENDS ON: V12 B32.16; V12 Batch B24a (CR-60's `scope_rung:` key); EXISTS-IN-TREE `state/gate.py::sits_over`, `::purview_reaches`, `state/carriers.py::Office.scope_rung`.
- GLOSSARY: none.
- NAMES: `populated.py::resolve_anchor` → `boot/realm.py::resolve_anchor` (B03c).
- COST and TIER: edit; `sonnet`, `medium`.
- LANDS IT: B32's producer; `Item: B32.17`, `[skip ci]`.

### B32.18 — the Church strife signature · PAP_A edit 5 · POINTER · HASH —
- What the pointed section does: "the CH row … `verbs: [arrest, determine, revoke]`, `kinds: [arrest.made]` …, `gap:` removed"; one signature function: an Event of the row's kinds whose causing act has a `via` seat `s` with `ROLE_TEMPLATE_OF.get(office_faction(s.body, s.faction)) == "ecclesiastical"`.
- Target files: `engine/season/harness/strife_moves.yaml` (CH row), `engine/season/harness/strife.py` (CR-74's files); `data/rosters.py::ROLE_TEMPLATE_OF`.
- Gate: "a planted restraint through a Church seat reads CH; the same through a secular seat does not and lands in the labelled residue; `content_hash` unchanged by the reading."
- Where it lands: B21s, with CR-74 (PAP_A: "edit 5 [waits] on CR-74"; CR-74 is B21s's, after B32: UNDECIDED 4). Harness only, hash EQUAL.

### B32.19 — who may fill a seat for somebody else · PAP_B edits 1–3, 5 · BUILD · HASH MOVER(behaviour)
- SOURCE: PAP_B "The resolution, decided" §1, "Exact edits" 1, 2, 3, 5, "Gate" bullet 1 (`patronage`), "Falsifier"; SYN_A §2 rows `patronage_bases`, `tables.patronage`; SYN_A §4 row `PATRONAGE_RULES`, `patronage_of`; C3-L9.
- ADVANCES: none of the nine.
- INSTRUCTION:
  1. "`engine/season/rosters.yaml`: new roster after `binds_bases`: `patronage_bases: {open: false, values: [purview, own_faction], source: "PAPACY-B", note: "WHO MAY FILL A SEAT FOR SOMEBODY ELSE -- a closed set of rule names, read through tables.patronage. The rule is behaviour and lives in state/gate.py::PATRONAGE_RULES."}`; and `tables.patronage: {}` (empty at this edit)."
  2. "`engine/season/data/rosters.py`: the loader of `tables.patronage` refuses a key that is no `offices.yaml` row and a member off `patronage_bases`. **No `Office` field** (C3-L9)."
  3. "`engine/season/state/gate.py`: `PATRONAGE_RULES = {"purview": …, "own_faction": …}` with an import-time totality check beside `check_filled_by`; one reader `patronage_of(off_id) -> tuple` (the table's list, else `("purview",)`); `may_fill`'s last line becomes `return any(PATRONAGE_RULES[b](w, w.offices[via], off) for b in patronage_of(off.id))`." The rules (§1's table): "`purview`: today's rule: `purview_reaches(via, off.rung)`"; "`own_faction`: `seat_faction(via) == faction_prop_id(off.faction)` …; no purview walk".
  4. Edit 5: "`tables.patronage`: `[own_faction]` for `off_cardinal_fortitude`, `…_justice`, `…_prudence`, `…_temperance`, `off_senior_inquisitor`, `off_archbishops_rep` (a declared mover for `confer` formation on those seats)." Commit order: steps 1–3 (EQUAL with the table empty, read as the control), then step 4 in the same commit `[ASSUMPTION: one commit; E-13: shared files and gate]`.
  5. Glossary: row *patronage*: "the right to appoint someone to a seat"; owner → `state/gate.py::PATRONAGE_RULES`.
- WHERE: `engine/season/rosters.yaml` (`patronage_bases`, `tables.patronage`); `engine/season/data/rosters.py` (the table's loader); `engine/season/state/gate.py` (`PATRONAGE_RULES`, `patronage_of`, `may_fill`); NEW `engine/season/tests/test_inst_pap_b.py`; `unified/U1_GLOSSARY.md` (*patronage*).
- TESTS: in the new file, red before: `test_patronage_refuses_the_king_on_a_church_seat` ("the King's `confer` on a vacated `off_cardinal_prudence` → refused at `may_fill`; the Confessor's → admitted and rolled. With the seat's entry deleted from `tables.patronage` the King's is admitted (control)"); `test_patronage_table_refusals` `[ASSUMPTION: name]`.
- FALSIFIER and CONTROL: "A seat declaring `[own_faction]` filled through a seat of another faction." Control (PAP_B realm control): "`build_realm(0)` one and two seasons, base hash, with `tables.patronage` empty".
- GATE: `python -m pytest engine/season/tests/test_inst_pap_b.py -q` → pass; seed 0, one season, hash with the table empty → equal to B32.17's after-reading; with step 4 → moved, recorded.
- HASH MOVERS: "a Crown or Löwenritter seat's `confer` on a Church seat is refused … (`world_q.vacancies` stops offering them to seats that may not fill)". Re-pinned at B32.99.
- DEPENDS ON: V12 B32.06; EXISTS-IN-TREE `state/gate.py::may_fill`, `::check_filled_by`, `::purview_reaches`; V12 Batch B21 (BIND_C's `confer` draw).
- GLOSSARY: *patronage* (step 5).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.19`, `[skip ci]`.

### B32.20 — the conclave, the share and the graded count · PAP_B edits 6–8; SYN_A §6 · BUILD · HASH MOVER(behaviour)
- SOURCE: PAP_B "The resolution, decided" §2, §3, "Exact edits" 6, 7, 8, "Gate" bullets 2–4, "Falsifier"; SYN_A §6 bullets 1–2 (`quorum_share` combinable with `quorum`; the one tally; `matter.undetermined`); `13_SC_draw_for_unrolled_contests.md` edit 3 (B07: the ballot loop); rulings A-14, A-36.
- ADVANCES: R-04.a (`determine` through a declared row) where an election executes; none at this tree (no computed docket names `conclave`, PAP_B "What it changes" 2).
- INSTRUCTION:
  1. Edit 6: "`engine/season/arrangements.yaml`: the `conclave` row (with `quorum: 2`)", exactly as PAP_B §2 writes it (`disposal: declared`, `quorum: 2`, `quorum_share: [2, 3]`, `bench_basis: determine`, `floor: closed`, `records_dissent: true`, `venue_min_rank: settlement`, `term_required: false`, `appeal_basis: none`, `interposed: [procedure, ceremony]`, `order: rank`, `proofs: []`, `disposes: hold`, `disposal_reach: realm`, `standard: demanding`; its `[ASSUMPTION; medium; Jordan to correct; revert: the Confessor is elected under CR-35's generic `election` row.]`). "`data/arrangements.py`: `quorum_share` added to `_ARRANGEMENT_KEYS` (the key-count test is re-recorded and says why), validated as two positive ints `n <= d`, lawful only on `disposal: declared`, **combinable with `quorum`**."
  2. Edit 7: "`engine/season/loop/effects_information.py` (the ballot loop …): the pass test is `fors >= max(1, row.get("quorum", 1))` and, where the row carries `quorum_share: [n, d]`, `fors * d >= n * (fors + againsts)`; before casting, a seated member who is the party of the docketed petition is skipped; for a row whose `disposes:` is `hold` it applies the three-outcome table. `verb_table.yaml: determine` gains the emitted kind `matter.undetermined`". The table: "the pass test above holds → the candidate holds the seat (CR-35's `hold` disposal)"; "fors a simple majority, short of the pass test → no election; the candidacy **stays on the docket** …; emits `matter.undetermined`"; "fors not a majority → the candidacy is dismissed (`matter.dismissed`); he may petition again". SYN_A: a body weighted by territory reads `tables.territory_weight` "as a term of each voter's draw, never as a count" (B21's `faction_q.weight`; nothing here authors weights).
  3. Edit 8: "`excommunication_deliberation`: keeps `quorum: 2` and gains `quorum_share: [2, 3]` beside it `[ASSUMPTION; revert: no share]`."
  4. Glossary: row *conclave* (the Church's election row, `arrangements.yaml: conclave`).
  Added by the B24p fold (F.3): each row seeded here carries the five keys of B24p.03 (`rite`, `exchanges`, `authority`, `presumes`, `strikes`) or the loader refuses it; the values are written at the item's open from RD §C.3's table (the nearest of its thirteen rows) and listed in the PR body (D-19), `[ASSUMPTION; Jordan to correct]`.
- WHERE: `engine/season/arrangements.yaml` (`conclave`, `excommunication_deliberation`); `engine/season/data/arrangements.py` (`_ARRANGEMENT_KEYS`, the `quorum_share` validation); `engine/season/loop/effects_information.py` (the ballot loop's tally); `engine/season/verb_table.yaml` (`determine.emits`: `matter.undetermined`, at the end of the row's list); `engine/season/tests/test_inst_pap_b.py`; the key-count test (SITE: `grep -rn "_ARRANGEMENT_KEYS" engine/season/tests`).
- TESTS: in `test_inst_pap_b.py`, red before: `test_election_three_outcomes_hand_built` ("**four hand-built electors** … Arm B: three electors committed for, none against. Arm C: two for, two against. Each over 200 seeds: all three outcomes of the table occur in at least one arm; P(seat opened) is higher in B than in C; neither is 0 or 1. The exact probability of each outcome is printed from the per-ballot odds"); `test_election_built_realm_two_electors` ("`off_cardinal_justice` and `off_senior_inquisitor` …: a case file of PAPACY-F's shape whose one set-up act is the Confessor's `release`, and a petition by NPC-039. 200 seeds: the seat opens in some and not all … With `off_senior_inquisitor` also vacated the seat opens in no seed. Zero ballots: every elector's draw pinned to Partial carries nothing"); `test_share_moves_with_the_bench` ("under `quorum_share: [2, 3]` the pass mark moves with the bench; under `quorum: 3` it does not (control)"). `[ASSUMPTION: test names; the item creates them — basis: no source file of the suite names them (E-3); repair lane R2d]`
- FALSIFIER and CONTROL: "Arms B and C giving the same outcome distribution … An election decided the same way in every seed for a given set of commits … An inconclusive candidacy that leaves the docket." Control: realm hash with the `conclave` row absent equals B32.19's after-reading.
- GATE: `python -m pytest engine/season/tests/test_inst_pap_b.py -q` → pass; each seeded share with `assert checked >= 200`; the printed exact probabilities quoted in the commit body (`opus` reads them: PAP_B tier line).
- HASH MOVERS: "wherever a declared determination executes (in the realm today: none)"; `excommunication_deliberation`'s share where it executes. Re-pinned at B32.99.
- DEPENDS ON: V12 B32.19; V12 Batch B07 (`13_SC_draw_for_unrolled_contests` edit 3, the ballot loop), Batch B21c (CR-35's election arm and `hold` disposal), Batch B27 (the arrangement rows that bind); EXISTS-IN-TREE `data/arrangements.py::_ARRANGEMENT_KEYS`, `queries/world_q.py::declared_votes`.
- GLOSSARY: *conclave* (step 4).
- COST and TIER: small build; `sonnet`, `high`; one `opus` read of the gate's output.
- LANDS IT: B32's producer; `Item: B32.20`, `[skip ci]`.

### B32.21 — the head of a faction may strip an officer · PAP_B edit 9 with `U5d_FA_owed_edits` §3 · BUILD · HASH MOVER(behaviour)
- SOURCE: PAP_B "The resolution, decided" §4, "Exact edits" 9, "Gate" (Strip, A-35); `proposals/U5d_FA_owed_edits.md` §3 (Owner, Edit, Gate, Falsifier, Movers); U3 §4.1 row 77; rulings A-35, A-36. One item: U3 lands the two "with" each other (§5.5).
- ADVANCES: none of the nine; R-04.a's `revoke` is B21's.
- INSTRUCTION: "`rosters.yaml: revocation_bases` gains `head_of_faction` (A-35 …); `REVOCATION_RULES["head_of_faction"]`: the seat exercised is the `head_seat` of the faction the stripped seat belongs to (`rosters.yaml: factions.<f>.head_seat`, U1 F-02). The `appointed` Himmelenger rows and `off_archbishops_rep` change `revocation: null → head_of_faction`." "The import-time check extended." "**`off_confessor` keeps `revocation: null`** (A-36) and gains a note: death or resignation only. The Löwenritter rows keep `null` until `06_FA_seat_terms_by_body_B.md` edit 4 gives them a `head_seat`" (if B21 landed that edit, the Löwenritter rows stay `null` still: A-35 names the Church rows only; recorded). "The strip is `revoke`'s contested row (`14_VERBS_BINDING_C_turnover.md`): the officer resists by the draw; a Failure is `revocation.resisted` and the seat stays."
- WHERE: `engine/season/rosters.yaml` (`revocation_bases`); `engine/season/state/gate.py` (`REVOCATION_RULES`, its import-time check); `engine/season/offices.yaml` (the six rows' `revocation`, `off_confessor`'s note).
- TESTS: `test_inst_pap_b.py::test_head_of_faction_strips_and_is_resisted` (PAP_B: "the Confessor's `revoke` of `off_cardinal_prudence`'s holder forms and rolls; Failure leaves him seated and emits `revocation.resisted`; the same act on `off_confessor` by any seat is refused at formation"; U5d §3: "both a carried and a resisted band occur across the swept dice seeds; a Cardinal's `revoke` of the Confessor is refused at eligibility; the King's `revoke` of a Cardinal is refused"); red before. `[ASSUMPTION: test names; the item creates them — basis: no source file of the suite names them (E-3); repair lane R2d]`
- FALSIFIER and CONTROL: "The strip succeeding in every seed (a fixed outcome); any seat stripping the Confessor." Control: a non-Church `revoke` unchanged.
- GATE: `python -m pytest engine/season/tests/test_inst_pap_b.py -q` → pass.
- HASH MOVERS: "None at build (bases are read when a `revoke` is formed); every run in which a Church `revoke` then forms." Re-pinned at B32.99.
- DEPENDS ON: V12 B32.19; V12 Batch B21 (BIND_C's drawn `revoke`; `06_FA_seat_terms_by_body_B` edit 4); EXISTS-IN-TREE `state/gate.py::REVOCATION_RULES`, `::may_revoke`.
- GLOSSARY: none.
- COST and TIER: edit (ruled, A-35); `sonnet`, `high`.
- LANDS IT: B32's producer; `Item: B32.21`, `[skip ci]`.

<!-- part34: the batch continues in `workplan_v12_part34_cont.md` from B32.22 -->
Last item written in this file: B32.21.
