# Workplan v12 — part 38, continued: Batch B33-inst-economy-hands, from B33.21

## Status: PROPOSED (the continuation of `workplan_v12_part38.md`, author lane A38; the batch block's head, its position table and its first items are there; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

Short names (`BYZ_B` … `SYN_C`, `SYN_A`, `SYN_B`, `S/`) and the batch's UNDECIDED list are the head's, in `workplan_v12_part38.md`.

### B33.21 — Hafenmark passes by inheritance, through a title vacant at build · COL_D edit 4 · BUILD · HASH MOVER(encoding)
- SOURCE: COL_D "Exact edits" 4, "What it changes" 4, "Gate" first bullet's last sentence; A-17/A-18 (COL_D's Status line), A-19; U3 §4.1 row 86 (the ledger reading in B33).
- ADVANCES: none of the nine; A-19 (an empty throne is claimed in the deed race), canon's rebuttable presumption.
- INSTRUCTION: "**`offices.yaml: off_duchess_hafenmark.conferral: null → inheritance`; `rosters.yaml: successions` gains `off_duchess_hafenmark: off_heir_hafenmark`; `offices.yaml` gains the title seat `off_heir_hafenmark` (`post: "Heir of Hafenmark"`, `rung: {duchy: "Hafenmark"}`, `conferral: appointed`, `remit_acts: []`, `holder: null`).** `[ASSUMPTION; medium; Jordan to correct; revert: the three edits together]`. Ladder step 4: `off_king`'s shape (IN-61). Canon gives Baralta no heir (:143), so the title is vacant at build and **Hafenmark's succession is open from the first season** … the build refuses a row with `holder: null` today …; BYZANTINE-A's vacant-row edit (B32) admits it." The item's first step builds a realm with the three edits on B32's tree and records that the vacant row is admitted (if it is refused, B32's vacant-row edit is missing: STOP, the item is `BLOCKED (FA: BYZ_A's vacant-row edit, B32)`).
- WHERE: `S/offices.yaml` (`off_duchess_hafenmark.conferral`; NEW row `off_heir_hafenmark`); `S/rosters.yaml` (`successions`); NEW `S/tests/test_inst_col_d_ledger.py`.
- TESTS: in the new file (the source's named test, which "replaces `test_accomplishment.py`, whose function is not added"; U3 §6.1's `test_accomplishment.py` row is this file), written before the edit and read red: `test_the_vacant_heir_title_builds` ("The vacant title `off_heir_hafenmark` builds (BYZANTINE-A's edit)") and `test_hafenmark_passes_to_its_heir_title` (the `successions` mapping reads `off_heir_hafenmark`; `_req_succeed` admits its holder once the seat has no live `hold`) `[ASSUMPTION: the second test's name (E-3)]`.
- FALSIFIER and CONTROL: a holder seated at build on `off_heir_hafenmark` (canon gives no heir). Control: `off_king`'s `successions` row and `off_heir` unchanged.
- GATE: `python -m pytest engine/season/tests/test_inst_col_d_ledger.py -q` → pass; `build_realm(0)` builds; its content hash → moved by one Office and one edited row, recorded for B33.99.
- HASH MOVERS: the build hash (a new Office; an edited conferral basis). Declared; B33.99.
- DEPENDS ON: EXISTS-IN-TREE `S/rosters.yaml: successions`, `S/offices.yaml` rows `off_duchess_hafenmark`, `off_heir`, `S/loop/predicates.py::_req_succeed`; V12 Batch B32 (`BYZ_A`'s vacant-row build edit).
- GLOSSARY: none.
- COST and TIER: content edit; `sonnet`, `medium`.
- LANDS IT: B33's producer; `Item: B33.21`, `[skip ci]`.

### B33.22 — standing passes down the seat: the chain reading · COL_D gate · BUILD · HASH EQUAL
- SOURCE: COL_D "Gate" first and third bullets, "Falsifier" second bullet; `SYN_B` §1 (the chain term of `person_q.legitimacy(p, holder, window, seat, fx)`, cut at a holder believed to have taken the seat by force; `presumption_gain` ships 0); U3 §4.1 row 86.
- ADVANCES: none of the nine; A-17/A-18 (deed-monarchy as each person's own ledger).
- INSTRUCTION: no engine edit (COL_D edits 1–3 are `SYN_B`'s, B32 and B39; edit 5 is not built). The test COL_D names is written: in `test_inst_col_d_ledger.py`, "on a hand-built world, through `legitimacy(p, holder, window, seat, fx)` at `presumption_gain` 0.5: an heir whose predecessor `p` knows of reads own + 0.5 × predecessor's; an heir whose predecessor `p` has never heard of reads own; `presumption_gain: 0` reads own for both; a three-holder chain reads 0.25 of the founder". The fixture is planted at 0.5 in the test only (the shipped value stays 0, `SYN_B`'s dial). The third gate bullet ("After two seasons at seeds 0–2: the orderings are printed again; the count of persons whose ordering changed is reported") needs the seeded founders, which are B39's (`SYN_B` §2): moved there.
- WHERE: `S/tests/test_inst_col_d_ledger.py`.
- TESTS: `test_an_heir_carries_half_his_known_predecessor`, `test_an_unknown_predecessor_carries_nothing`, `test_presumption_gain_zero_reads_own`, `test_a_three_holder_chain_reads_a_quarter_of_the_founder`, `test_the_predecessor_is_read_from_p_s_claims_not_the_world` (the falsifier) `[ASSUMPTION: test names (E-3)]`; green at control if `SYN_B` §1 landed in B32, and each red with the chain term reverted.
- FALSIFIER and CONTROL: "Planted: read the predecessor from the world's Tenures instead of `p`'s claims; the 'never heard of' assertion reddens." Control: `presumption_gain: 0` reproduces `legitimacy`'s pre-`SYN_B` reading for every pair.
- GATE: `python -m pytest engine/season/tests/test_inst_col_d_ledger.py -q` → pass; **STOPS IF** `legitimacy` has no `seat` parameter at the item's open (`SYN_B` §1 not landed): the item is `BLOCKED (FA: SYN_B §1, B32)` and the receipt says so.
- HASH MOVERS: none (a test).
- DEPENDS ON: V12 Batch B32 (`SYN_B` §1: `legitimacy(…, seat, fx)`, `presumption_gain`); V12 B33.21; EXISTS-IN-TREE `S/queries/person_q.py::legitimacy` (today `legitimacy(p, holder, window, scar_shift)`), `::deeds_judged`.
- GLOSSARY: none.
- COST and TIER: a test; `sonnet`, `high`; the per-regime ordering read by `opus` in B39, not here.
- LANDS IT: B33's producer; `Item: B33.22`, `[skip ci]`.

### B33.23 — consecration: a hearing that mints a certificate · PAP_C edit 3 · BUILD · HASH EQUAL
- SOURCE: PAP_C §2 ("Consecration": the row, the route, the band table, the odds), "Exact edits" 3, "Gate" second to fourth bullets, "Falsifier"; X-03, X-05, X-06 (its first `Reconciled:` line: `recites`, not `attests`); A-5, A-81; CR-36 (the `resolution` kind and the Record disposal site, intake `:270`, B21c).
- ADVANCES: none of the nine; canon's "deed-monarchy, Church-consecrated".
- INSTRUCTION:
  0. Open `S/arrangements.yaml` and `_eff_determine`'s Record disposal site (CR-36's, by symbol); record whether B32 added `consecration` and whether `record_kinds.resolution` carries `recites` (`SYN_A` §2).
  1. `S/arrangements.yaml`, the row:
     ```yaml
       - id:               consecration
         disposal:          bench
         bench_basis:        determine
         floor:              open            # a public rite: its outcome is known
         records_dissent:    false
         venue_min_rank:     settlement
         term_required:      false
         appeal_basis:       none
         interposed:         [office, ceremony, document]
         order:              scripted
         proofs:             [record, testimony, oath]
         disposes:           Record
         disposal_reach:      realm
         standard:           demanding       # SC T2
     ```
  2. The bands, at CR-36's site ("this proposal needs CR-36's site to mint under any `disposes: Record` row whose docketed petition names a seat, which is how CR-36 states it"), keyed on that condition and the band, never on the row id:
     | band | effect |
     |---|---|
     | Overwhelming, Success | a `resolution` with `recites: {for: <seat>, deeds: [<the cited deed claims left standing>]}` and `to: [claimant]`, held by the determiner |
     | Partial | the same reciting the first half of them, in cited order: a grudging consecration |
     | Failure | nothing minted; the matter is dismissed (SC-P6); he may petition again; the refusal is witnessed on the open floor and held by those present (A-81) |
     "Consecration opens no `hold` and gates no `succeed`." Where CR-36's site already writes these cells generically, step 2 is recorded present.
  3. Create `S/tests/test_inst_pap_c.py` (the source's named test), written before step 1 and read red.
- WHERE: `S/arrangements.yaml` (`consecration`); the Record disposal site in `S/loop/effects_information.py` (`_eff_determine` / `_disposal`, by symbol) only where step 2 finds the `recites` write absent; NEW `S/tests/test_inst_pap_c.py`.
- TESTS: `test_a_paper_raises_the_odds_of_consecration` ("Arm A: his side cites `ins_consecration_first_king` (given him by its holder). Arm B: no paper. Exact odds printed for both from the module's distribution: P(Success or better) in A exceeds B; 200 seeds per arm show all four bands in both. Arm C: a rival cites a contrary Record against the roll: A's advantage shrinks"); `test_the_houses_order_as_their_recited_deeds` ("the same hearing for a Hafenmark claimant citing `ins_settlement_hafenmark` and a Varfell claimant citing `ins_settlement_varfell` …: the three exact odds are ordered as the recited deeds are (3, 2, 1)"); `test_a_refusal_is_held_by_those_present` ("in arm B's Failure seeds, every person present at the sitting holds a claim of the refusal after WITNESS; the count … asserted non-zero"); `test_a_resolution_opens_no_hold` (the falsifier's last sentence) `[ASSUMPTION: test names (E-3)]`.
- FALSIFIER and CONTROL: "A roll cited under a row whose `proofs:` does not admit `record` and still moving the odds. A consecration whose outcome is the same in every seed for a given state. A build in which a house's head holds its roll … Any reader that treats a `resolution` as opening or gating a `hold`." Control: no matter is docketed under `consecration` in the built realm: hash EQUAL.
- GATE: `python -m pytest engine/season/tests/test_inst_pap_c.py -q` → pass (`checked >= 200` per arm); the build gate is `SYN_B`'s (B32: "the seeded rows; the archive's two papers held by the Cardinal of Temperance's holder"), not repeated. `opus` reads the planted hearing's odds table (PAP_C's tier line).
- HASH MOVERS: none ("Hand-built until a computed docket names a row").
- DEPENDS ON: V12 Batch B32 (`SYN_B` §3, §4: the seeded `ins_consecration_first_king`, `ins_settlement_hafenmark`, `ins_settlement_varfell`; a cited `recites` Record filing one item per deed; `SYN_A` §2's `recites` key); V12 Batch B21c (CR-36's site, reached through B32); V12 Batch B24 (`05_SC_evidence_and_rebuttal_B`, `12_ARCS_cited_evidence`); V12 Batch B25 (`14_VERBS_SOCIAL2_B`); V12 Batch B27 (SC-P6).
- GLOSSARY: row *consecration* (owner `arrangements.yaml: consecration`; "consecration": the Church's hearing that certifies a claimant's deeds for a seat, as a king is consecrated); *certificate* (a `resolution` carrying `recites`).
- COST and TIER: small build; `sonnet`, `high`; the odds table `opus`.
- LANDS IT: B33's producer; `Item: B33.23`, `[skip ci]`.

### B33.24 — the Church keeps its liberties: a goal row, shipped off · PAP_C edit 4 · CONTENT · HASH EQUAL
- SOURCE: PAP_C §3, "Exact edits" 4.
- ADVANCES: none of the nine; the Church's side of the containment charter.
- INSTRUCTION: `S/goals.yaml`, the row, **written commented out** ("Until then the row ships OFF"; the tree's goal rows carry no off switch: `grep -n "enabled\|active:" engine/season/goals.yaml` finds none, so the row is shipped as PAP_E edit 4 ships its house row, commented, with its `[ASSUMPTION]`):
  ```yaml
    # - id: goal_church_liberties_kept
    #   org: {faction: Church of Solmund}
    #   text: the Church keeps its liberties -- whoever a churchman knows to have seized, requisitioned or arrested at Himmelenger
    #   object: {kind: deed_doers, kinds: [rung.seized, record.seized, requisition.taken, arrest.made]}
    #   pursuits: {stability: 0.5, doctrine: 0.3, justice: 0.2}
    #   source: "PAPACY-C; canon/03_canonical_timeline.md:58 (the grant's terms). [ASSUMPTION; medium; Jordan to correct -- the weights]"
  ```
  with the comment line: "OFF: the `kinds:` form has no place filter, so this row as written acts against such deeds done anywhere a churchman hears of them, which is broader than the charter. The narrowing (deeds whose claim subject lies under a named rung) is a fourth `deed_doers` form and belongs to `data/goals.py`'s owner; it is requested, not built here."
- WHERE: `S/goals.yaml` (a commented row).
- TESTS: none (a comment).
- FALSIFIER and CONTROL: the row loads (it must not, until the filter exists). Control: `python -c "import engine.season.data.goals"` loads and the goal count is unchanged.
- GATE: `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); `build_realm(0)`'s content hash → equal to B33.23's reading.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `S/goals.yaml` (`deed_doers` `kinds:` form); V12 B33.23.
- GLOSSARY: none.
- COST and TIER: content; `sonnet`, `medium`; the row is listed in the PR body for Jordan.
- LANDS IT: B33's producer; `Item: B33.24`, `[skip ci]`.

### B33.25 — a ban or a detention opened is an Event of its own · PAP_D edits 1–3 · BUILD · HASH MOVER(behaviour)
- SOURCE: PAP_D §2 ("The opening kinds"), "Exact edits" 1, 2, 3, "What it changes" 1, "Gate" (the sentence bullet's last clause), "Falsifier" ("A `ban` opening with no `ban.opened`"); CR-74 (its carrier is in `PAP_A`, B32); IN-58's rule (`person_q.deeds_judged`).
- ADVANCES: none of the nine; the martyr effect and the popular sentence as one rule.
- INSTRUCTION:
  1. "`engine/season/verb_table.yaml`: `determine` `emits` gains `ban.opened`, `detention.opened` on the three writing bands (earned per edge of that kind); `revoke` `emits` gains `ban.opened` (earned when its disposal opens one). `write_matrix.yaml`: no row (an Event kind, not a field)."
  2. "`engine/season/loop/effects_information.py::_eff_determine` / `_disposal` and `loop/effects_governance.py::_eff_revoke`: earn the kind where the Tenure is constructed." "Two rows emit `ban.opened`, so it has no `KIND_VERB` and joins the paired kinds (`data/verbs.py::_derive_kind_verb`): a hearer judges it **for its doer**, the bench, by his own lean on the kind times his bond to the excluded man."
  3. "`engine/season/rosters.yaml: alignment`: `deed:ban.opened` and `deed:detention.opened` cells on the seven axes, authored by the alignment table's owner `[ASSUMPTION; first reading: leaning to the `hierarchical` and `precedent` poles; sign only; Jordan to correct]`. With no cell the kind scores 0 and only the bond half is silent: the control." On the tree's bipolar axes (`hierarchical_equal`, `precedent_substantive`: the first-named pole is negative, the `alignment` block's note) the two cells are `-1.0` on those two axes and `null` on the other five, each line carrying the `[ASSUMPTION …]` comment.
  4. Create `S/tests/test_inst_pap_d.py` (the source's named test) with `test_every_ban_opened_has_its_kind` ("`ban.opened` count equals `ban` Tenures opened"; and `detention.opened` for `detain`), written before step 2 and read red `[ASSUMPTION: test name (E-3)]`.
- WHERE: `S/verb_table.yaml` (`determine`, `revoke`: `emits`); `S/loop/effects_information.py` (`_eff_determine`, `_disposal`); `S/loop/effects_governance.py` (`_eff_revoke`); `S/rosters.yaml` (`alignment`: two `deed:` rows); NEW `S/tests/test_inst_pap_d.py`.
- TESTS: the one above.
- FALSIFIER and CONTROL: "A `ban` opening with no `ban.opened`." Control: with no `deed:` cell the kind scores 0 (the alignment loader's `null` reading); the realm at seeds 0 and 1 opened no `ban` in three seasons (audit E-1), so the seeded tallies are expected unchanged unless a ban opens: read and quoted at two seasons.
- GATE: `python -m pytest engine/season/tests/test_inst_pap_d.py -q` → pass; `python -c "import engine.season.data.verbs"` → loads (the alignment density rule, `_load_alignment`).
- HASH MOVERS: "A declared mover wherever one opens" (PAP_D "What it changes" 1). Declared; B33.99.
- DEPENDS ON: EXISTS-IN-TREE `S/loop/effects_information.py::_eff_determine`, `::_disposal`, `S/loop/effects_governance.py::_eff_revoke`, `S/data/verbs.py::_derive_kind_verb`, `S/rosters.yaml: alignment`; V12 Batch B27 (SC-P4, SC-P6).
- GLOSSARY: none (Event kinds; `ban` and `detention` are the tree's).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B33's producer; `Item: B33.25`, `[skip ci]`.

### B33.26 — the Church's two sentences grade by band · PAP_D edit 4 · BUILD · HASH MOVER(behaviour)
- SOURCE: PAP_D §1 ("The sentence"), "Exact edits" 4, "What it changes" 2, "Gate" (the sentence bullet); SC-P4; A-36 ("No sentence may be passed on the Confessor").
- ADVANCES: none of the nine; ARC-21's "more than two outcome tiers".
- INSTRUCTION: on `excommunication_deliberation` and `inquisition_hearing` in `S/arrangements.yaml`: "`disposes:  {Overwhelming: ban, Success: ban, Partial: oblige}     # SC-P4's band map`". "Overwhelming, Success: the party is excluded (`ban` on the determining seat; existing readers; scoped to the seat's purview by FA-P3). Overwhelming also writes the pursuit move the row writes today. Partial: the party is bound to the bench by an `oblige` (a monition and penance: he owes the seat; no exclusion). The gate already admits a bench opening an `oblige` on itself (`may_determine`). Failure: acquittal (SC-P6)." The row's `quorum: 2` beside `quorum_share: [2, 3]` is `SYN_A` §6's (B32): recorded present, not written here. A-36 holds by the rows' bench: no sentence routes to `off_confessor` (the test below plants one and expects refusal at formation or at the gate, whichever the tree has; record which).
- WHERE: `S/arrangements.yaml` (`excommunication_deliberation`, `inquisition_hearing`: `disposes`); `S/tests/test_inst_pap_d.py`.
- TESTS: `test_the_sentence_has_four_outcomes` ("one matter under `excommunication_deliberation`, 200 seeds: all four bands occur; a `ban` on O/S, an `oblige` on P, `matter.dismissed` on F"); `test_no_sentence_on_the_confessor` `[ASSUMPTION: test names (E-3)]`, red before the edit.
- FALSIFIER and CONTROL: "A sentence under a row whose band map names a kind `DISPOSABLE_KINDS` lacks." Control: rows other than the two keep their `disposes`.
- GATE: `python -m pytest engine/season/tests/test_inst_pap_d.py -q` → pass (`checked >= 200`).
- HASH MOVERS: "A declared mover where they execute" (PAP_D "What it changes" 2). Declared; B33.99.
- DEPENDS ON: V12 B33.25; V12 Batch B27 (`05_SC_arrangement_rows_that_bind`: the band-map loader); V12 Batch B32 (`SYN_A` §6's `quorum` beside `quorum_share`); EXISTS-IN-TREE `S/arrangements.yaml` rows `excommunication_deliberation`, `inquisition_hearing`, `S/state/gate.py::may_determine`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B33's producer; `Item: B33.26`, `[skip ci]`.

### B33.27 — a man who complied shuns: the decline · PAP_D edit 7 · BUILD · HASH EQUAL
- SOURCE: PAP_D §3 ("Publication: the writ of avoidance", the answer table), §4 ("Interdict"), "Exact edits" 7, "Gate" (the "answers differ" bullet), "Falsifier" (the planted failure); X-29, X-33; `SYN_A` §1 (the forms `avoidance`, `interdict` with `forbears` clauses `by: addressee`), §4 (`forborne`); A-21, A-22.
- ADVANCES: none of the nine; "Historically the sanction's whole force was other people's compliance".
- INSTRUCTION:
  0. Open the tree: `grep -n "def forborne" engine/season/queries/person_q.py`, `grep -n "forborne" engine/season/decision/options.py`, and `S/instruments.yaml`'s `avoidance` row (its `{by: addressee, kind: tenure.opened, over: named}` clause, `SYN_C` edit 2, carried in `SYN_A`'s row). Record each; write only what is absent. If the `tenure.opened` clause is absent from the row, add it here (it is `SYN_C` edit 2's one clause).
  1. "`engine/season/decision/options.py::opening_set`: one person-side decline, the shape of `held_document_declines`, reading `person_q.forborne(p)` (SYNTHESIS-A §4: his own live `oblige` carrying `OBEYED_WRIT` and the forbears clauses of that writ's form), and declining those verbs toward the form's named object. Person-side: his own Tenures and his own content claim."
  2. The answer table's Partial row: "`comply` (Partial): he shuns where he is seen: the decline applies only at a venue where another addressee stands; elsewhere `conceal` forms" `[UNVERIFIED: whether the complier's `oblige` records the band it was opened at; if it does not, the Partial arm is not built and the receipt says so]`.
  3. For an `interdict` the named object is a rung: "A complier declines the forborne verbs toward persons residing under the rung."
- WHERE: `S/decision/options.py` (`opening_set`: the decline); `S/queries/person_q.py` (`forborne`) only where step 0 finds it absent; `S/instruments.yaml` (`avoidance`'s clause) only where absent; `S/tests/test_inst_pap_d.py`.
- TESTS: `test_answers_differ` ("a published writ naming a seated lord, ten addressees, 200 seeds. For one fixed addressee both `compliance.given` and `compliance.withheld` occur across seeds. Two arms: addressees at `solmund_orthodoxy` 1 and at 5: the share complying is higher in the second. Control: no writ issued, no decline forms and the avoided lord's `exchange` partners are unchanged"); `test_a_complier_does_not_seat_the_avoided_man` (`SYN_C` gate 4: "Two conferrers addressed by one `avoidance`; one complies, one defies. The first has no `confer` candidate naming the avoided man; the second has, and its Event is a deed the issuer's faction holds") `[ASSUMPTION: test names (E-3)]`.
- FALSIFIER and CONTROL: "Every addressee shuns in every seed (the writ would be a switch) … Planted failure: make edit 7 unconditional on the answer; the 'answers differ' arm goes red." Control: no writ issued, nothing declines.
- GATE: `python -m pytest engine/season/tests/test_inst_pap_d.py -q` → pass (`checked >= 200`); `opus` reads the "answers differ" arm (PAP_D's tier line). (Patched: P-34) `SYN_A` gate 3's `comply` arm, moved here from B32 by part 34's UNDECIDED (6) ("reads `forborne` (PAP-D edit 7, B33)"), copied: "an addressee whose `comply` drew Success has the named dealings declined and one whose `comply` drew Failure does not"; written in `engine/season/tests/test_inst_syn_a_kit.py` (B32's file, beside `test_one_of_each_dues`) as `test_one_of_each_avoidance_comply_arm` `[ASSUMPTION: test name; this item creates it, E-3]` on SYN_A gate 3's hand-built two-seat world with one `avoidance`, and read with `python -m pytest engine/season/tests/test_inst_syn_a_kit.py -k avoidance -q` → pass. SYN_A's falsifier for the arm: "A roll over 200 seeds of gate 3's `comply` in which every addressee declines (the writ would be a switch)".
- HASH MOVERS: none (no computed `avoidance` or `interdict` is issued in the built realm; B33.47 is where `issue`'s form choice can make one).
- DEPENDS ON: V12 Batch B32 (`SYN_A` §1, §4); V12 Batch B28 (`14_VERBS_SOCIAL1_B`: `OBEYED_WRIT`, the answer rows `comply`, `evade / defy`, `construe`); EXISTS-IN-TREE `S/decision/options.py::opening_set`, `S/rosters.yaml: held_document_declines`.
- GLOSSARY: row *shun* (new: "shun": to decline dealings with a man under sentence, as the excommunicate is shunned; owner the `opening_set` decline over `forborne`).
- COST and TIER: small build; `sonnet`, `high`; `opus` on the arm.
- LANDS IT: B33's producer; `Item: B33.27`, `[skip ci]`.

### B33.28 — penance weighs in a pardon · PAP_D edit 9 · BUILD · HASH EQUAL
- SOURCE: PAP_D §5 ("Absolution and penance"), "Exact edits" 9, "What it changes" 4, "Gate" (penance bullet); C3-C10 (penance is a `proofs` level); A-37.
- ADVANCES: none of the nine; "the route for a great man is therefore: swear, serve the term, ask".
- INSTRUCTION: "`pardon` closes the `ban` through the seat that is its object (existing rule …). This proposal adds one favourable item: if the penitent has owned an `oblige` to that seat, with a term, opened after the ban and matured, his side files one `proofs` item of weight `penance_weight` (leverage, C3-C10). First value 2 (proof-weight units), control 0, sweep 0 / 1 / 2 / 4, owner `data/fixtures.py` with one NUMBER row in `hole_register.yaml`." Edit 9: "`engine/season/data/fixtures.py`: `penance_weight` (0 ships); `seam/wrappers/sigma.py` host input for `pardon` reads the matured `oblige` world-side and adds the `proofs` item." A-37: a penance that is an imposed service ends by the bench's pardon or its term, never by the penitent's own `release` (no edit: the `oblige` the bench opens at Partial is imposed).
- WHERE: `S/data/fixtures.py` (`penance_weight`); `S/seam/wrappers/sigma.py` (the `pardon` host input, by symbol); `S/hole_register.yaml` (NUMBER row, block slot 3); `S/tests/test_inst_pap_d.py`.
- TESTS: `test_penance_odds` ("`pardon` odds printed exactly at `penance_weight` 0 and 2 with a matured `oblige` planted"; asserted: at 0 the two equal the no-`oblige` odds, at 2 the odds are higher) `[ASSUMPTION: test name (E-3)]`.
- FALSIFIER and CONTROL: an unmatured or pre-ban `oblige` filing the item. Control: `penance_weight: 0` (shipped).
- GATE: `python -m pytest engine/season/tests/test_inst_pap_d.py -q` → pass; `python tools/ci_sim_fabrication_check.py` → exit 0.
- HASH MOVERS: none at 0 (shipped). The flip is B98's (DIALS AT CONTROL).
- DEPENDS ON: V12 B33.25; V12 Batch B05 (`proofs` levels); V12 Batch B32 (`pardon` drawn: `14_VERBS_BINDING_B`, through `BYZ_E`'s bands); EXISTS-IN-TREE `S/seam/wrappers/sigma.py::contest_input`.
- GLOSSARY: row *penance* (new: "penance": service sworn and served to a Church seat that weighs for a pardon; owner `Fixtures penance_weight`).
- IDS: H block slot 3 (`penance_weight`).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B33's producer; `Item: B33.28`, `[skip ci]`.

### B33.29 — the strife instrument counts the Church's sentences · PAP_D edit 10 · BUILD · HASH EQUAL
- SOURCE: PAP_D "Exact edits" 10, "Gate" (strife bullet); CR-74 (the CH signature; `PAP_A` edit 5, B32).
- ADVANCES: none of the nine; closes the CH row's `gap:` ("no verb or Event kind names a church sanction", `S/harness/strife_moves.yaml`).
- INSTRUCTION: "`harness/strife_moves.yaml` CH: `kinds` gains `ban.opened`, `detention.opened` (PAPACY-A edit 5)." Open the CH row first: if `PAP_A` edit 5 (B32) already changed it, record its state and add only the two kinds; the `gap:` text is removed where both `verbs:` and `kinds:` are then non-empty, else kept.
- WHERE: `S/harness/strife_moves.yaml` (the CH row).
- TESTS: none new; the existing strife harness test file (`grep -rl strife_moves engine/season/tests tests/valoria` names it) stays green.
- FALSIFIER and CONTROL: the reading moves the content hash. Control: "`content_hash` unchanged by the reading".
- GATE: "`strife 3 0 1 2` reports CH above 0 in the planted world and labels a secular arrest as residue" — at two seasons (A-114): `PYTHONHASHSEED=0 python -m engine.season.harness.strife 2 0 1 2` → CH's line quoted (on the realm it may read 0; the planted world of B33.26's test reads it above 0, asserted there with `ban.opened` counted); content hash before and after the reading equal.
- HASH MOVERS: none.
- DEPENDS ON: V12 B33.25; V12 Batch B32 (`PAP_A` edit 5); EXISTS-IN-TREE `S/harness/strife_moves.yaml` (CH), `S/harness/strife.py::main` (`<seasons> <seed> [seed ...]`).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `medium`.
- LANDS IT: B33's producer; `Item: B33.29`, `[skip ci]`.

### B33.30 — the standing levy, the `tax` edict · CP-T08-07 · HELD (trigger: B12c.34 merged with its gate met: an issuing seat holds a stock claim in the built realm; was BLOCKED (SE/FA: H-163 limit 3(a), a governor's stock claim, has no owner) until A-116)
Reconciled 2026-11-12 (A-115/A-116 lane): H-163 limit 3(a) has an owner, Batch B12c (B12c.30 to .34, A-116: the season's stock report up the chain, the requisition aimed at the believed stock). B12c (W15) precedes this batch (W18). When the trigger fires, this item is written from the home entry's six parts named below, collection being the holder's `requisition` aimed at his believed stock (B12c.32); until then nothing lands. The text below is the entry as it stood.
Placed here by `V12_STRUCTURE_part2.md` §5.6's first rule: PAP_E, the next member, names CP-T08-07 ("the tithe gate waits on it"). The intake entry (`:333`): MISSING-DEP, rows E1:119, E4:307, E4:679, E5:48; **settled:** "its gate H-163 limit 3(a) has no owner in the tree or any proposal (E5:48); owner FA/SE; the tithe and tax kit files wait on it." Its carry-forward (E5 Block C17, the v11 override AM-E-18): "CP-T08-07 is gated on H-163 limit 3(a) (a governor holds a stock claim of the rung he taxes) and does not build before it. Its 'one slot per place' is a slot on EDICTS only … It no longer needs CP-T08-08 … Compliance by `unrest` band (item 5) stays as written and ships at 1000." What it would build when unblocked is the home entry's six parts (E1 §Carry-forward, line 1318: the verb row `tax`, the Record kind `edict` with `edict_kinds: {tax: {phase_in}}`, one slot per place, collection as the holder's `requisition` through the `levy_due` question source, `unrest_compliance` at 1000, and the withdrawals), its falsifier `test_tax_edict.py` on `harness/scarce.governed` and its control "`tax` ships in `Fixtures withheld_verbs` and `unrest_compliance` at 1000". Not built: no item lands until an owner of H-163 limit 3(a) exists. What waits on it here: PAP_E's tithe gate (B33.32 notes it). Owner: FA/SE (the intake). Listed in `V12_STRUCTURE_part3.md` §8.2's "nine blocked entries".
- GATE (when the trigger fires; moved here from B33.32 by `V12_STRUCTURE_part2.md` §5.8, a gate arm that reads a later item's effect goes to that item; R2d, CHK_K9 #14): PAP_E's tithe gate, "after the levy lands: one writ, three sees; stores at `terr_T9` rise by the sum of the renders of the sees whose holders complied", read at two seasons on seeds 0 to 2 and quoted.

### B33.31 — three sees, built vacant · PAP_E edit 1 · BUILD · HASH MOVER(encoding)
- SOURCE: PAP_E §1 ("Sees"), "Exact edits" 1, "What it changes" 1, "Gate" (the vacant-rows, sees and reach bullets), "Falsifier" first sentence; A-35 (`head_of_faction`), C3-L9 (`patronage` is a table entry).
- ADVANCES: none of the nine; canon's "diocesan structure" by 200 AG; investiture as a standing prize.
- INSTRUCTION:
  1. `S/offices.yaml`, three rows (after `BYZ_A`'s vacant-row edit and `PAP_B`'s `head_of_faction`, both B32):
     ```yaml
       - id:         off_see_valorsmark          # ids and posts are content; canon names no see
         post:       "Bishop"                    # a member of harness/populated.py::TITLES already
         rung:       {duchy: "Valorsmark"}
         body:       null
         faction:    "Church of Solmund"
         remit_acts: [issue, determine]
         conferral:  appointed
         revocation: head_of_faction             # A-35 (PAPACY-B item 4, ruled)
         holder:     null                        # built vacant (BYZANTINE-A's vacant-row edit)
         obligees:   []
         source:     "canon/03_canonical_timeline.md:50 (diocesan structure). [ASSUMPTION; medium; Jordan to correct: one see per duchy, the post name, the remit]"
         note:       "[NEW] PAPACY-E."
     ```
     "and the same for `{duchy: "Hafenmark"}` and `{duchy: "Varfell"}`" (`off_see_hafenmark`, `off_see_varfell`).
  2. "each named `[purview, own_faction]` in `rosters.yaml: tables.patronage` (the lord and the Confessor may each fill it; PAPACY-B §1 as reconciled)."
  3. Create `S/tests/test_inst_pap_e.py` (the source's named test), written before step 1: `test_the_vacant_rows_build` ("first, red before BYZANTINE-A's edit: `build_realm(0)` with the three rows raises `Unspecified` naming the row; after the edit it builds" — B32 has landed the edit, so the test is green at its first run and the commit body records that the red half is B32's); `test_each_see_is_fillable_by_its_duke_and_the_confessor_only` ("`build_realm(0)` has three more Offices, each vacant, each fillable through `off_confessor` and through its duke's seat and through no other faction's (`may_fill` table)"); `test_a_held_see_reaches_its_duchy` ("after a see is held, `sits_over(off_see_hafenmark, <a Hafenmark settlement>)` True and a `dispensation` issued through it names a Hafenmark resident as addressee") `[ASSUMPTION: test names (E-3)]`.
- WHERE: `S/offices.yaml` (three NEW seat rows); `S/rosters.yaml` (`tables.patronage`: three entries); NEW `S/tests/test_inst_pap_e.py`.
- TESTS: the three above.
- FALSIFIER and CONTROL: "A see filled by a seat of a third faction." Control: "rows absent, base hash".
- GATE: `python -m pytest engine/season/tests/test_inst_pap_e.py -q` → pass. The realm reading "In a three-season run at seeds 0-2 with the verb lane's `confer` draw and CR-88's vacancy duty landed: at least one see is filled at some seed, and the `Act.via` that filled it is reported" → at two seasons (A-114), seeds 0–2, the fills and their `Act.via` quoted in the commit body; reported, not asserted ("which side won is a reading, not a bar"); CR-88's duty is B21d's (UNDECIDED 7), so the reading says whether it was in the tree. `opus` reads the `Act.via` table (PAP_E's tier line).
- HASH MOVERS: "A declared build-hash mover (three Offices)". Declared; B33.99.
- DEPENDS ON: V12 Batch B32 (`BYZ_A`'s vacant-row edit; `PAP_B`'s `head_of_faction`, `tables.patronage`, `patronage_bases`); V12 Batch B21 (`06_FA_remit_grant_by_row`, `06_FA_seat_terms_and_turnover`); EXISTS-IN-TREE `S/state/gate.py::sits_over`, `S/offices.yaml` (`off_confessor`, the three duke seats).
- GLOSSARY: row *see* (new: "see": a bishop's seat over a duchy, as a cathedral's see; owner `offices.yaml` rows `off_see_*`).
- COST and TIER: content edit; `sonnet`, `medium`.
- LANDS IT: B33's producer; `Item: B33.31`, `[skip ci]`.

### B33.32 — the tithe named in the Cardinal's goal; an exempt house offered, off · PAP_E edits 3–4 · CONTENT · HASH EQUAL
- SOURCE: PAP_E §2 ("The tithe"), §3 ("Exempt houses"), "Exact edits" 3 and 4, "Gate" (tithe and exempt-house bullets); X-02, X-11 (the form `tithe`, `SYN_A`).
- ADVANCES: none of the nine; NPC-013's core need, by construction once the levy exists.
- INSTRUCTION:
  1. "`engine/season/goals.yaml: goal_cardinal_prudence_tithes`: `text` gains *'-- by a standing writ to the sees, each rendering a share of its rung's yield'*; no key changes."
  2. "`engine/season/offices.yaml`: the house row, commented out, with its `[ASSUMPTION]`":
     ```yaml
       # - id: off_templar_preceptor_hafenmark     # [ASSUMPTION; Jordan to name]
       #   post: "Preceptor"
       #   rung: {duchy: "Hafenmark"}
       #   body: "Cardinal of Fortitude"
       #   faction: null
       #   remit_acts: [dispatch]
       #   conferral: appointed
       #   revocation: head_of_faction     # A-35
       #   holder: null
       #   obligees: []
     ```
     with the comment "(its `tables.patronage` entry `[own_faction]`; termed `oblige` to the head seat per PAPACY-GROUNDING item 4, so the exemption lapses unless renewed) … with its holder, once seated, added to `off_cardinal_fortitude.obligees`."
- WHERE: `S/goals.yaml` (`goal_cardinal_prudence_tithes.text`); `S/offices.yaml` (a commented row).
- TESTS: `engine/season/tests/test_inst_pap_e.py::test_reach_by_oath_ends_with_the_release` (the exempt-house gate, the row planted in the test's world only), written before the edit `[ASSUMPTION: test name (E-3)]` (the GATE named it and TESTS read "none new"; R2d).
- FALSIFIER and CONTROL: "A tithe that moves stores with no `requisition` act by a see-holder. Reach through a house that survives its head's `release`." Neither can occur here (no levy, no house row). Control: the build hash equal to B33.31's reading `[UNVERIFIED: whether a goal row's `text` enters the content hash; if it does, the hash moves by the text and the re-pin records it]`.
- GATE: `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); the tithe gate is not this item's: it reads the levy B33.30 builds (HELD), so it is moved to B33.30's GATE (§5.8; R2d, CHK_K9 #14); the exempt-house gate ("with the house row on and its holder sworn, `purview_reaches(off_cardinal_fortitude, duchy_hafenmark)` True; after his `release`, False") is run as a hand-built test in `test_inst_pap_e.py` with the row planted in the test's world only: `test_reach_by_oath_ends_with_the_release` `[ASSUMPTION: test name (E-3)]`.
- HASH MOVERS: none (see the `[UNVERIFIED]` above).
- DEPENDS ON: EXISTS-IN-TREE `S/goals.yaml: goal_cardinal_prudence_tithes`, `S/state/gate.py::purview_reaches` (the oblige clause); V12 B33.31. (The tithe gate's levy, CP-T08-07, is B33.30's, HELD; that gate is B33.30's, so this item depends on nothing missing: R2d.)
- GLOSSARY: none.
- COST and TIER: content; `sonnet`, `medium`.
- LANDS IT: B33's producer; `Item: B33.32`, `[skip ci]`.

### B33.33 — what the one asked owes: `owed_to` · VEN_A edit 3 · BUILD · HASH EQUAL
- SOURCE: VEN_A "The quantity and its two channels" (the `read from` and `lifted by` rows), "Exact edits" 3; X-20, X-29, X-31 (its first `Reconciled:` line: "an `oblige` counts only if `gate.py::sworn_to` counts it"); `SYN_A` §4 (`owed_to`); AX-2 (no world read on the person side).
- ADVANCES: none of the nine; D-5's one lawful effect of an obligation (the odds of his own answer).
- INSTRUCTION:
  0. Open the tree: `grep -n "def owed_to" engine/season/queries/person_q.py`; if B32 landed it, record the reading and its body and stop (the item lands nothing; its test is still written).
  1. "**`engine/season/queries/person_q.py`**: one reader, `owed_to(p, holder_seats, held_terms) -> (whole, lapsing)`: the counts of the person's own live edges of the two shapes above. Person-side: it reads `p.tenures` only." The two shapes: "(a) a live, un-imposed `oblige` whose object is a seat the **actor** (or, for the hostile half, the other party) holds; (b) a live `commit` to a Proposition that is the `terms` of a Record that person holds (a covenant or, with proposal B, a debt). Each such edge counts 1; an edge whose `term` matures within one season counts `obligation_arrears`" (the fixture lands in B33.34; until then the reader returns the lapsing count apart, `(whole, lapsing)`, and applies no weight). "An `oblige` counts only if `gate.py::sworn_to` counts it" (an obedience carrying `OBEYED_WRIT` is not an oath for the odds). The `excused` lift is B33.45's ("until it lands no edge is excused").
  2. Create `S/tests/test_inst_ven_a.py` (the source's named test) with `test_owed_to_counts_his_own_edges` (a person sworn to the King's seat and committed to a covenant's terms the actor holds reads `(2, 0)`; one whose oath matures this season reads `(1, 1)`; an `OBEYED_WRIT` obedience counts 0) and `test_owed_to_reads_only_his_tenures` (it is called with no `World`), written before step 1 and read red `[ASSUMPTION: test names (E-3)]`.
- WHERE: `S/queries/person_q.py` (`owed_to`); NEW `S/tests/test_inst_ven_a.py`.
- TESTS: the two above.
- FALSIFIER and CONTROL: "Mutation: read the **actor's** edges instead of the counterparty's; the hand-built pair then shows no difference and the gate reddens" (read at B33.34). Control: nothing calls `owed_to` yet; the realm hash equals B33.32's reading.
- GATE: `python -m pytest engine/season/tests/test_inst_ven_a.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `S/state/gate.py::sworn_to`; V12 Batch B28 (`OBEYED_WRIT`); V12 Batch B32 (`SYN_A` §4).
- GLOSSARY: row *obligation* — its owner column gains `person_q.owed_to`; "owed": what a man owes another by an oath or an undertaking he himself made.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B33's producer; `Item: B33.33`, `[skip ci]`.

### B33.34 — `obligation` as levels; three fixtures at control; member 12 widened; the host's operands · VEN_A edits 1, 2, 4, 5 · BUILD · HASH EQUAL
- SOURCE: VEN_A "The quantity and its two channels" (all rows), "Exact edits" 1, 2, 4, 5, 6, "Gate", "Falsifier"; C3-C10, A-25 (what helps the roller is levels; nothing lowers the obstacle); F-39; `U5c_SC_one_obstacle_form.md` §3 (`obligation` after `favour`); `SYN_A` §2 (`advantage_sources`), §5.
- ADVANCES: none of the nine; "the King's ask of a sworn duke is likelier to be met than of a stranger".
- INSTRUCTION (one commit: `S/seam/wrappers/sigma.py` refuses an `ADVANTAGE_SOURCES` set that differs from the roster's, so the roster row and its function land together):
  0. Open the tree: `rosters.yaml: advantage_sources` (an `obligation` member?), `data/fixtures.py` (`obligation_level`, `obligation_arrears`, `sealed_obligation`?), `sigma.py::ADVANTAGE_SOURCES`, `roll.py::obstacle`'s member 12; record which B32 landed; write only what is absent.
  1. Edit 1: "**`engine/season/rosters.yaml: advantage_sources`** (OBS §3; this edit lands after it): add the source `obligation` after `favour`, with the rows above (`read_from`, `size`, `applies_to`)": `read_from` the counterparty's `owed_to` toward the actor; `size` "one `obligation_level` per whole unit of the count, on the leverage channel, under the soft cap `M_MAX`"; `applies_to` "every contested act with a person counterparty (`argue`, `petition` once contested by SC's hearing, `speak` where a bench member is rolled, `interrogate`, `interview`); and the answer rolls of `comply` / `evade / defy` where FA's repair makes them rolls", and, from this batch, `requisition` (B33.04: "`obligation` where persons residing under the place are sworn to the exercised seat", read as the residing cohort's own `owed_to` toward the exercised seat) and `carry` at a hand (B33.07: "where the maker and the clerk are sworn to one seat"). "the room: both halves multiplied by `sealed_obligation` when the act is heard under an arrangement row with `records_dissent: false`". "**Cross-lane request (SC owner):** OBS member 12 `commitment`'s read gains the counterparty's `owed_to` toward the other party of the heard matter; `obstacle_terms` gains no member" — landed here, at the member's reader, "at `commitment_ob` per unit, as a live commit to the contrary does" `[ASSUMPTION: the hostile half folds into `commitment` — basis: … reversible by U1]` (VEN_A).
  2. Edit 2: "**`engine/season/data/fixtures.py`**: three fixtures, each with a hole-register row and a sweep: `obligation_level: None` (swept {None, `minor`, `moderate`}; proposed `minor`), `obligation_arrears: 1.0` (swept {0.5, 1.0}; proposed 0.5), `sealed_obligation: 1.0` (swept {0, 0.5, 1.0}; proposed 0). `obligation_step` is not added. Shipped values are the control arm; every value is recalibrated with OBS §4 step 5 (A-5, A-6, A-7, A-26). `[ASSUMPTION; medium; Jordan to correct; revert: the control values]`."
  3. Edit 4: "**`engine/season/seam/wrappers/sigma.py::contest_input`** …: carry three raw operands: the counterparty's `owed_to` toward the actor, his `owed_to` toward the opposing party where the matter has one, and the docketed arrangement row's `records_dissent`. The host sums nothing."
  4. Edit 5: "**`engine/season/seam/wrappers/sigma.py::ADVANTAGE_SOURCES`**: the `obligation` source returns the actor's levels from the carried operand (the other side's list empty); **`modules/social_contest/roll.py::obstacle`**: member 12 adds the carried hostile count at `commitment_ob`. Both are recorded in the `levels` and `terms` SC-P1 writes on the Event." Edit 6: "**No `verb_table.yaml` row changes.**"
  5. `test_inst_ven_a.py` gains the gate's tests, written before steps 1–4 and read red.
- WHERE: `S/rosters.yaml` (`advantage_sources.obligation`); `S/data/fixtures.py` (three fixtures); `S/hole_register.yaml` (three NUMBER rows, block slots 4–6); `S/seam/wrappers/sigma.py` (`contest_input`, `ADVANTAGE_SOURCES`); `S/queries/inputs.py` (`SocialContestInput`: the three operands); `modules/social_contest/roll.py` (`obstacle`, member 12); `S/tests/test_inst_ven_a.py`.
- TESTS: `test_an_obliged_counterparty_gives_a_level` ("one `argue` at a person with a live `oblige` to the actor's seat, and the same act at a person without, same seed stream: the recorded `levels` differ by exactly `obligation` and the `terms` are equal"); `test_an_oath_to_the_other_party_widens_commitment` ("the counterparty obliged to the other party of a docketed matter: the `terms` differ in `commitment` and the `levels` are equal"); `test_a_sealed_room_collects_nothing` ("the same hand-built act heard under `council_of_state` (`records_dissent: false`) with `sealed_obligation: 0` carries no `obligation` level"); `test_the_cap_leaves_failure_possible` ("with `obligation_level: major` and ten edges the soft cap (`M_MAX`) must still leave a non-zero chance of Failure") — the first three at `obligation_level: minor` planted in the test `[ASSUMPTION: test names (E-3)]`.
- FALSIFIER and CONTROL: "The control: any hash move at arm 0. Mutation: read the **actor's** edges instead of the counterparty's … A planted certainty: … if an obliged man can be made unable to refuse, the term has become a lever and D-5 is broken." Control (arm 0): "`obligation_level` None, member 12 unwidened: content hash equal to the pre-item hash at build and at each season".
- GATE: `python -m pytest engine/season/tests/test_inst_ven_a.py -q` → pass; arm 0 at seeds 0, 1, 2, two seasons (three in the source; A-114) → content hash equal to B33.33's reading at build, one and two seasons; arm 1 (`minor`, planted by a fixture override in the probe, not shipped): "every contested act whose counterparty is NPC-050, NPC-052 or NPC-070 and whose actor holds `off_king` carries the term; the band counts of asks to obliged and to unobliged counterparties are **read and reported** for the three seeds" — quoted in the commit body; `python tools/ci_sim_fabrication_check.py` → exit 0. `opus` reads the seeded arm's band table (VEN_A's tier line).
- HASH MOVERS: none at ship ("Hash EQUAL at ship; the fixture change is a declared mover and its own commit": B98's).
- DEPENDS ON: V12 B33.33; V12 Batch B05 (`U5c_SC_one_obstacle_form`, `05_SC_obstacle_difficulty_and_modifiers_B`, `05_SC_contest_record_on_event`: the roster, the leverage channel, `M_MAX`, `commitment_ob`, the recorded `terms` and `levels`); EXISTS-IN-TREE `S/rosters.yaml: advantage_sources`, `S/seam/wrappers/sigma.py::ADVANTAGE_SOURCES` (and its set check), `::contest_input`, `S/arrangements.yaml: council_of_state`.
- GLOSSARY: row *obligation* — "obligation" (the leverage source): levels for a man asking someone who owes him, as an obligation is called in; owner `rosters.yaml: advantage_sources.obligation`; refused: `oath_step`, `obligation_step`.
- IDS: H block slots 4–6 (`obligation_level`, `obligation_arrears`, `sealed_obligation`).
- COST and TIER: small build; `sonnet`, `high`; `opus` on the band table.
- LANDS IT: B33's producer; `Item: B33.34`, `[skip ci]`.

### B33.35 — the `debt` kind, its operands and the distraint's one check · VEN_B edit 1 · BUILD · HASH EQUAL
- SOURCE: VEN_B "Exact edits" 1, "The resolution" (Kind, Parties, Recourse (b)); X-09; K-14 (`proposals/2026-10-03-verb-coverage-and-gap-fill.md:1478`); D-5; `SYN_A` §2 (both roster rows are listed there as VEN-B edit 1's).
- ADVANCES: none of the nine; ARC-15 N1, NPC-037 N2, SCN-12 N2 (VEN_B, the problem).
- INSTRUCTION:
  0. Open the tree: `rosters.yaml: record_kinds` (`debt`?), `record_sourced_operands` (`debt`?), `instruments.yaml: forms` (the `debt` form row, `SYN_A`); record which B32 landed; write only what is absent.
  (Patched: P-17, resolved at the merge.) B32.03 steps 2 and 5 land `record_kinds: debt: [terms, to, kind, amount, at]` and `record_sourced_operands: debt: {subject: terms, kind: kind, amount: amount}` with the same text, in the batch that also lands the `debt` form row (B32.03 step 6) and two steps earlier in the order (S17 against S19): B32.03 owns both rows. Step 1 here adds only its note ("the derived parties … K-14 un-deferred", and the `to`-not-mapped and `warrant_sourced`-not-edited sentences) to the row B32.03 wrote; steps 2–3 are this item's own.
  1. "**`engine/season/rosters.yaml: record_kinds.values`**: add `debt: [terms, to, kind, amount, at]`, with a note stating the derived parties and that it is K-14 un-deferred. **`record_sourced_operands.values`**: add `debt: {subject: terms, kind: kind, amount: amount}` (the reservation …). `to` is **not** mapped: a `transfer`'s `to` is a rung and the bond's `to` is a person; the place is read from `at` by the effect … **`warrant_sourced` is NOT edited.** … The distraint instead forms through `record_sourced_operands`' second reader (a held Record answers the operands it maps): the officer who holds the lapsed bond forms `requisition` with `kind` and `amount` from it, and the effect reads the debtor's `reside` rung as the place."
  2. "The one new check is in `_eff_requisition` …: an act formed on a `debt` declines unless the bond reads lapsed (last stage matured, `world_q.owed > 0`) and takes no more than the uncounted amount." (`_eff_requisition` as B33.04 left it; by symbol.)
  3. Create `S/tests/test_inst_ven_b.py` (the source's named test; "the hand-built chain is its first function", built up through B33.38) with `test_a_debt_row_loads_and_maps_its_operands` and `test_distraint_takes_only_a_lapsed_bond_s_remainder`, written before steps 1–2 and read red `[ASSUMPTION: test names (E-3)]`.
- WHERE: `S/rosters.yaml` (`record_kinds`, `record_sourced_operands`); `S/loop/effects_governance.py::_eff_requisition` (by symbol); NEW `S/tests/test_inst_ven_b.py`.
- TESTS: the two above.
- FALSIFIER and CONTROL: "D-5: a hand-built act by the creditor that closes the debtor's `commit` is `NotYours` at the gate" (`test_the_creditor_cannot_close_the_debtor_s_commit`, here). Control: "with the `debt` row absent from `record_kinds`, the pre-item hash at build and at three seasons" — read at two (A-114).
- GATE: `python -m pytest engine/season/tests/test_inst_ven_b.py -q` → pass; the realm hash (`HASH READING`) at seed 0, one season → equal to B33.34's reading.
- HASH MOVERS: none ("With no act naming `kind` and `amount` (every computed `covenant` today) nothing moves: hash EQUAL").
- DEPENDS ON: V12 Batch B32 (`SYN_A` §1 the `debt` form, §4 `world_q.owed`, `dues`, `breaches`); V12 B33.04 (`_eff_requisition`'s band dispatch); EXISTS-IN-TREE `S/rosters.yaml: record_kinds`, `record_sourced_operands`, `warrant_sourced`.
- GLOSSARY: row *debt* (owner `rosters.yaml: record_kinds.debt`; "debt": a bond the creditor holds for an undertaking the debtor owns; refused "loan" for the document).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B33's producer; `Item: B33.35`, `[skip ci]`.

### B33.36 — `covenant` mints a bond · VEN_B edit 2 · BUILD · HASH EQUAL
- SOURCE: VEN_B "Exact edits" 2, "What it changes" 1.
- ADVANCES: none of the nine; credit at every scale.
- INSTRUCTION: "**`engine/season/loop/effects_information.py::_eff_covenant`**: if the act's payload names `kind` and `amount`, mint through `_mint_document(w, a, "debt", …)`; refuse (`covenant.refused`) a `kind` off `matter_kinds` or an `amount` that is not a positive whole number; else today's body. One mint." `Record.stages` are the due dates ("the last is the maturity"), declared through `_declared_stages` as any Record's.
- WHERE: `S/loop/effects_information.py` (`_eff_covenant`); `S/tests/test_inst_ven_b.py`.
- TESTS: `test_covenant_with_kind_and_amount_mints_a_debt` (the chain's first steps: "utter → commit → covenant (a `debt` exists, held by the lender)"); `test_a_bad_kind_or_amount_is_refused` `[ASSUMPTION: test names (E-3)]`, red first.
- FALSIFIER and CONTROL: a `covenant` with no `kind` and `amount` minting a `debt`. Control: today's `dispensation` mint unchanged for every computed covenant.
- GATE: `python -m pytest engine/season/tests/test_inst_ven_b.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 B33.35; EXISTS-IN-TREE `S/loop/effects_information.py::_eff_covenant`, `::_mint_document`, `S/rosters.yaml: matter_kinds`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B33's producer; `Item: B33.36`, `[skip ci]`.

### B33.37 — a payment to the bond's place counts toward it · VEN_B edits 3–4 · BUILD · HASH EQUAL
- SOURCE: VEN_B "Exact edits" 3 and 4, "The resolution" (Discharge, Lapse), "Gate" first and third bullets, "Falsifier" (the mutation); C3-C7; `SYN_A` §4 (`owed`).
- ADVANCES: none of the nine.
- INSTRUCTION: edit 3 is no reader: "The amount is `world_q.owed` (SYN-A §4); the creditor's and the debtor's occasions are `world_q.dues` and `world_q.breaches` … `debt_state`, `debts_held` and `debts_owed` are not added." Edit 4: "**`engine/season/loop/effects_economy.py::_eff_transfer`**: no new write. When the act's question is about a `debt` Record and its `to` is that bond's `at`, the Event carries the Record among its subjects so `world_q.owed` can count it. A `transfer` to another rung counts nothing." The lapse is read, not emitted: "after the last stage's `term.matured`, a bond with `owed > 0` is lapsed when read … WITNESS deposits the `term.matured` to the holder and the committed debtors". `loop/matter.py` is not edited (edit 5 withdrawn).
- WHERE: `S/loop/effects_economy.py` (`_eff_transfer`); `S/tests/test_inst_ven_b.py`.
- TESTS: the chain continued: "→ advance (`transfer`) → part payment (state `running`, counted) → … last stage matures (`term.matured`; `world_q.owed > 0`; the holder holds the WITNESS claim of the maturity) … Asserted: no Event of kind `debt.lapsed` exists and `loop/matter.py` wrote no `Record.stages` cell"; "Conservation: the sum of stores by kind over all rungs is unchanged by every act of the chain"; the mutation arm `test_payment_to_the_wrong_place_counts_nothing` `[ASSUMPTION: test names (E-3)]`.
- FALSIFIER and CONTROL: "Mutation: count a `transfer` to a rung other than `at`; the 'pay the wrong place' arm must then lapse and does not." Control: every `transfer` not on a `debt` question is unchanged.
- GATE: `python -m pytest engine/season/tests/test_inst_ven_b.py -q` → pass; `git diff <batch-start-sha> -- engine/season/loop/matter.py` → empty.
- HASH MOVERS: none.
- DEPENDS ON: V12 B33.36; V12 Batch B32 (`world_q.owed`); EXISTS-IN-TREE `S/loop/effects_economy.py::_eff_transfer`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B33's producer; `Item: B33.37`, `[skip ci]`.

### B33.38 — a suit for debt; the loan's terms at control · VEN_B edits 6–7 · BUILD · HASH EQUAL
- SOURCE: VEN_B "Exact edits" 6, 7, "The resolution" (the reckoning, Recourse (a)), "Gate" (the chain's last steps), "Falsifier" (the draw); A-39; `audits/15_INSTITUTIONS_VENICE.md` §8 (the `stakes_ob` row for `debt`: "amount ÷ the asked rung's stores of that kind, capped at 2 | {off, on} | off").
- ADVANCES: none of the nine; "a king cannot be sued" ends.
- INSTRUCTION:
  1. Edit 6, `S/arrangements.yaml`, one row (B32 may have added it, `SYN_A` §6: open first, write only if absent):
     ```yaml
        - id:               debt_suit
          disposal:          bench
          bench_basis:        determine
          floor:              open
          records_dissent:    true
          venue_min_rank:     settlement
          term_required:      true
          appeal_basis:       determine
          interposed:         [person, document]
          order:              alternating
          proofs:             [record, testimony, oath]
          disposes:           ban
          disposal_reach:      settlement
     ```
     "`disposes: ban` is the Success-or-better kind until SC-P4's band-keyed form lands, after which the row reads as stated above. `[ASSUMPTION; medium; SC's to correct]`." SC-P4 is in the tree from B27, so the row lands band-keyed as the Recourse paragraph states it: "Overwhelming `ban` (the debt-bar …) or `detain`; Success an `oblige` to the creditor's seat (service); Partial a new stage on the bond; Failure an acquittal (SC-P6), after which the bond can no longer be cited before that bench": `disposes: {Overwhelming: ban, Success: oblige, Partial: Record}` `[ASSUMPTION: Partial's "a new stage on the bond" is written as the `Record` cell (the bond re-wound at CR-36's Record site); if that site cannot wind a stage on an existing Record, Partial is left out of the map and the receipt says so]`. "An appeal … is admitted only on new grounds" (A-39; the loader's ground check is B24a's carrier).
  2. Edit 7: "**`engine/season/data/fixtures.py`**: `credit_terms` (owed ÷ advanced by the loan ask's band, used only where a computed act names no amount): proposed `{Overwhelming: 1.1, Success: 1.25, Partial: 1.5}`, shipped flat 1.0, swept. `stakes_ob` (SC's table) gains the `debt` reading in the audit's §8" — `stakes_ob.debt`: "amount ÷ the asked rung's stores of that kind, capped at 2", shipped `off` (the audit's control).
  3. The reckoning is no edit: "a `petition` to the debtor with the Record cited. It is the ask of proposal A, with the debtor's live `commit` as `obligation` levels for the creditor and the bond as `proofs` levels" (B33.34; `proofs` B05). Bands are `petition`'s.
- WHERE: `S/arrangements.yaml` (`debt_suit`); `S/data/fixtures.py` (`credit_terms`; `stakes_ob.debt`); `S/hole_register.yaml` (NUMBER row, block slot 7: `credit_terms`); `S/tests/test_inst_ven_b.py`.
- TESTS: the chain's end: "reckoning rolled at each band by seed selection (Partial winds a stage) → … → suit under `debt_suit` → a `ban` that refuses a `confer` inside the bench's purview and admits one outside"; `test_the_reckoning_is_drawn` ("over the reckoning's seeds at a fixed position, more than one band occurs (an assertion that asserts it observed at least two)") `[ASSUMPTION: test names (E-3)]`.
- FALSIFIER and CONTROL: the draw falsifier above. Control: `credit_terms` flat 1.0 and `stakes_ob.debt` off (shipped).
- GATE: `python -m pytest engine/season/tests/test_inst_ven_b.py -q` → pass; "Seeded: a spine fixture with one stocked hearth and its head seat … seeds 0–2, six seasons: bonds minted, reckoning bands, lapses and suits are **read and reported**. If no bond is minted the reading says so" — at two seasons (A-114) on `harness/scarce.py`'s governed arm (a hand-stocked `Rung.stores`), quoted in the commit body. `opus` reads the reckoning's band table (VEN_B's tier line).
- HASH MOVERS: none (no computed act names an amount; the fixtures ship at control).
- DEPENDS ON: V12 B33.37; V12 Batch B27 (SC-P4, SC-P6); V12 Batch B24a (the appeal ground, through B27); V12 Batch B12c (`07_SE_treasury_granary_B`'s stocked stores, through B12c); EXISTS-IN-TREE `S/harness/scarce.py`; the `stakes_ob.debt` arm is `BLOCKED (v12: a carrier is owed; owner the SC lane)`: the tree has no `stakes_ob` in `data/fixtures.py` and no item creates it (part 2 C-26), so this item's other arms stand and the `stakes_ob.debt` setting ships nothing until the carrier exists.
- GLOSSARY: none (*debt*, B33.35).
- IDS: H block slot 7 (`credit_terms`).
- COST and TIER: small build; `sonnet`, `high`; `opus` on the band table.
- LANDS IT: B33's producer; `Item: B33.38`, `[skip ci]`.

### B33.39 — a seat on a building · VEN_D edit 1 (§1) · BUILD · HASH EQUAL
- SOURCE: VEN_D §1 ("The house: a hearth with a head seat"), "Exact edits" 1, "Gate" first bullet, "Falsifier" (the mutation); `SYN_A` §3 ("`harness/populated.py::resolve_anchor` gains the form `{venue: <building id>}` (VEN-D edit 1)").
- ADVANCES: none of the nine; "a firm, a bank, a guild chapter and a foreign factory have no head" (VEN_D NERS) ends.
- INSTRUCTION:
  0. Open the tree: `resolve_anchor` in `S/boot/realm.py` (B03c's home) for a `venue` form; if B32 landed it, record the reading and stop (the test is still written).
  1. "`harness/populated.py::resolve_anchor` gains a fifth form, `{venue: "<building id>"}`, resolving to the `hearth` rung `venues.yaml` builds, by the same rule as the other four (it names exactly one live rung of the kind it says)." The `offices.yaml` header's "ONE resolver over the four forms" sentence says five.
  2. Create `S/tests/test_inst_ven_d.py` (the source's named test: "the anchor gate and the content gate") with `test_a_venue_anchor_seats_on_its_hearth` and `test_an_unknown_building_is_refused_at_build` ("a row with a `venue` anchor seats on the named hearth; a row naming an unknown building is refused at build"), written before step 1 and read red.
- WHERE: `S/boot/realm.py` (`resolve_anchor`); `S/offices.yaml` (the header comment); NEW `S/tests/test_inst_ven_d.py`.
- TESTS: the two above.
- FALSIFIER and CONTROL: "Mutation: anchor a head seat on a settlement; clients' upkeep then draws on the town's stores and the conservation reading names the wrong rung" (read at B33.40). Control: no shipped row uses the form; the build hash equals B33.38's reading.
- GATE: `python -m pytest engine/season/tests/test_inst_ven_d.py -q` → pass.
- HASH MOVERS: none ("Items 1 and 3 with no row or charter using them: hash EQUAL").
- DEPENDS ON: V12 Batch B03c (`boot/realm.py::resolve_anchor`); EXISTS-IN-TREE `S/venues.yaml` (the hearth rungs it builds); V12 Batch B32 (`SYN_A` §3).
- GLOSSARY: none.
- NAMES: `harness/populated.py::resolve_anchor` → `S/boot/realm.py::resolve_anchor` (§5.10, B03c).
- COST and TIER: small build; `sonnet`, `medium` (VEN_D's tier line for the anchor form).
- LANDS IT: B33's producer; `Item: B33.39`, `[skip ci]`.

### B33.40 — the Guilds' house, their list and a commune council · VEN_D §4 (i)–(iii) · CONTENT · HASH MOVER(encoding)
- SOURCE: VEN_D §4 ("Content rows": `office_bodies`, `offices.yaml: seats` (i)–(iii)), §1's head-seat row pattern, §2 (the rector pattern's keys), "Exact edits" 2, "Gate" (content bullet); X-10, X-11, X-12, C3-L9 (the tables), C3-N19; A-44; VEN_D's head: "posts and bodies are functional labels owed a row in `references/names_index.yaml` before they ship".
- ADVANCES: none of the nine; ARC-15, ARC-08, NPC-007, NPC-084, NPC-085 "turn on a guild house".
- INSTRUCTION ("Every content row below is `[ASSUMPTION; medium; Jordan to correct]`; no canon name is coined"):
  1. "**`engine/season/rosters.yaml: office_bodies`** (only what a seat below needs …): `"Commune Council": "Hafenmark"` ('An elected council of a chartered town.')" — in both the body → faction map and the description map, as the file's two `office_bodies` maps carry every body. (The three Schoenland bodies go with B33.43.)
  2. "(i) `off_house_feldhaus` at the guildhall NPC-007 is homed in (`npcs.yaml`: `b_s_006_guildhall`), `faction: "Guilds"`, holder NPC-007, beside her existing `off_guild_comptroller`." On §1's pattern: `post: "Family Head"`, `rung: {venue: "b_s_006_guildhall"}`, `body: null`, `remit_acts: [issue, confer]`, `conferral: null`, `revocation: null`, `upkeep: null`.
  3. "(ii) A guild list seat `off_guild_roll` (`{duchy: "Hafenmark"}`, `body: "Guild"`, `binds: members_by_warrant`, `remit_acts: [issue]`, `conferral: elected`, `term: 4`, vacant at build; in the tables: `selection: lot`, `eligible_from: off_guild_roll`, `cooling_off: 4`), and `tables.eligible_from: off_guild_roll` for `off_guild_comptroller` and FA-P2's `off_guild_leader`." (The narrowing of this seat's `issue` is `15_INSTITUTIONS_VENICE_grounding_E` edit 7's, B40, not here.)
  4. "(iii) Three commune council seats on one Hafenmark settlement (`body: "Commune Council"`, `conferral: elected`, `term: 4`, `audit_at_exit: audit`, `remit_acts: [determine, convene]`; in the tables: `selection: lot`, `eligible_from: off_guild_roll`, `cooling_off: 4`), vacant at build; `tables.eligible_from: off_guild_roll` for `off_commune_rep_hm`." Ids `off_commune_council_hm_1` to `_3` and the town `[ASSUMPTION: the source names neither; the town is the settlement `b_s_006_guildhall` stands in, so list and council sit in one place, recorded in the commit body and listed in the PR body for Jordan]`.
  5. `references/names_index.yaml`: one row each for the posts "Family Head" (if absent) and the body "Commune Council", in the file's existing row shape.
  6. `test_inst_ven_d.py` gains `test_the_house_the_list_and_the_council_build` (the four rows build, each vacant but the house; the tables load; every council seat's `eligible_from` is the list) `[ASSUMPTION: test name (E-3)]`.
- WHERE: `S/rosters.yaml` (`office_bodies`; `tables.selection`, `tables.eligible_from`, `tables.cooling_off`); `S/offices.yaml` (five NEW rows); `references/names_index.yaml`; `S/tests/test_inst_ven_d.py`.
- TESTS: the one above.
- FALSIFIER and CONTROL: a council holder off the list or inside his cooling-off (asserted in B40's scenario run). Control: the build with the five rows absent equals B33.39's hash ("the realm's pre-item hash is unchanged with the rows absent").
- GATE: `python -m pytest engine/season/tests/test_inst_ven_d.py -q` → pass; `python tools/ci_naming_check.py` → exit 0 (the new labels); `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`).
- HASH MOVERS: the build hash (five Offices). "Each content row is a declared mover." Declared; B33.99.
- DEPENDS ON: V12 B33.39; V12 B33.18 (`audit`); V12 Batch B32 (`VEN_C`: the tables, `members_by_warrant`, the lot); V12 Batch B21 (`06_FA_remit_grant_by_row`: `off_guild_leader`); EXISTS-IN-TREE `S/offices.yaml` rows `off_guild_comptroller`, `off_commune_rep_hm`, `S/rosters.yaml: office_bodies` (`"Guild"`), `S/npcs.yaml` (NPC-007's home `b_s_006_guildhall`).
- GLOSSARY: row *list* (glossary *roll*: "prose calls the membership a list"; `off_guild_roll` keeps its id).
- COST and TIER: content; `sonnet`, `medium`.
- LANDS IT: B33's producer; `Item: B33.40`, `[skip ci]`.

### B33.41 — the secret bench and the enrolment ballot · VEN_D §4, the two rows · BUILD · HASH EQUAL
- SOURCE: VEN_D §4 (`arrangements.yaml`: two rows; "`exit_audit` is not added"; the two named and not seeded); X-12, X-15 (the one tally for `declared` rows); `SYN_A` §6.
- ADVANCES: none of the nine.
- INSTRUCTION: open `S/arrangements.yaml` and record whether B32 added either; write only the absent:
  ```yaml
  - id: security_bench        # the secret bench: denunciation, no accused in the room, no appeal
    disposal: declared
    quorum: 3
    bench_basis: determine
    floor: closed
    records_dissent: false
    venue_min_rank: settlement
    term_required: false
    appeal_basis: none
    interposed: [office, document]
    order: scripted
    proofs: [testimony, confession, record]
    disposes: detain
    disposal_reach: realm

  # `exit_audit` is not added (X-12): the audit at exit is the colonial lane's `audit` row
  # (`15_INSTITUTIONS_COLONIAL_C` edit 1), named by `audit_at_exit: audit`.

  - id: enrolment_ballot      # a body votes a candidate onto its roll; his deeds are the evidence
    disposal: declared
    quorum: 3
    bench_basis: determine
    floor: admitted
    records_dissent: false
    venue_min_rank: settlement
    term_required: true
    appeal_basis: none
    interposed: [procedure]
    order: rank
    proofs: [record, testimony]
    disposes: oblige
    disposal_reach: body
  ```
  "`enrolment_ballot` uses what `determine` already does (a finding opens an `oblige` owned by the party on the judging seat): carried, the candidate is in `establishment_of` the roll seat. Two further rows are **named and not seeded** … a senate's decree disposes a `Record` and an election a `hold`, and `_disposal` has no site for either until CR-36 and CR-35." "Unanimity (the three inquisitors) is not expressible without a new key and is not taken."
- WHERE: `S/arrangements.yaml` (two rows); `S/tests/test_inst_ven_d.py`.
- TESTS: `test_the_two_rows_load_and_enrolment_swears_the_candidate` (both load; a hand-built carried `enrolment_ballot` puts the candidate in `establishment_of(off_guild_roll)`) `[ASSUMPTION: test name (E-3)]`.
- FALSIFIER and CONTROL: an `exit_audit` row in the file. Control: undocketed rows move nothing.
- GATE: `python -m pytest engine/season/tests/test_inst_ven_d.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 B33.40 (`off_guild_roll`); V12 Batch B32 (`SYN_A` §6: the `declared` tally, `quorum` beside `quorum_share`); EXISTS-IN-TREE `S/queries/world_q.py::establishment_of`.
- GLOSSARY: none.
- COST and TIER: edit (rows); `sonnet`, `medium`.
- LANDS IT: B33's producer; `Item: B33.41`, `[skip ci]`.

### B33.42 — a staple is a proof on an `exchange`; a market's standard · VEN_D §3 · BUILD · HASH EQUAL
- SOURCE: VEN_D §3 ("The trade privilege: a level, not a gate"), "What it changes" 3, "Exact edits" 3; X-10, C3-C10; A-81; `14_VERBS_MATERIAL_B_stores.md` §3 (`exchange` drawn, B12c.14).
- ADVANCES: none of the nine; the Hanse's privilege, the embargo.
- INSTRUCTION:
  0. **STOPS IF** `exchange` does not draw at the item's open (`S/verb_table.yaml: exchange` has no draw: B12c.14 not landed or HELD): the item is `HELD (exchange draws, MATERIAL-B)` and leaves to the held list at the expunge ("**Held** until `exchange` draws").
  1. "A held live `staple` naming the `to` rung, cited on an `exchange` by the actor (or held by the seat he is sworn to), is a `proofs` level for the actor on `exchange`'s draw (`U5c_SC_one_obstacle_form.md` §3)." Its validity: "in force while `world_q.in_force` says so" (`SYN_A` §4). **No obstacle term is asked of the MATERIAL lane.**
  2. "One venue key on the market's row, a `standard` (SC's `difficulty_levels`) the host faction's seat-holder may raise by `establish`, stands against every trader there (an embargo is the market's standard raised and its privileges left to lapse)." `S/venues.yaml` market rows gain `standard:` (absent reads the row's `routine`); the `exchange` row's `difficulty` reads it. "Its Failure band forfeits the goods offered to the market's rung (a durable write, A-81)" is MATERIAL's band and is not edited here; the item records whether B12c's `exchange` Failure cell writes it.
- WHERE: the `proofs` source's reader for `exchange` (`S/seam/wrappers/sigma.py`, by symbol); `S/venues.yaml` (market rows: `standard`); the `exchange` row's `difficulty` read (`S/verb_table.yaml`, or its host, by symbol); `S/tests/test_inst_ven_d.py`.
- TESTS: `test_a_held_staple_is_a_proof_on_exchange` (the same `exchange` with and without a held live `staple` naming `to`: the recorded `levels` differ by one `proofs` level, the `terms` equal) and `test_a_raised_standard_stands_against_every_trader` `[ASSUMPTION: test names (E-3)]`, red first.
- FALSIFIER and CONTROL: "Nothing is refused outright: under the standing rule a smuggler sometimes gets through": a trade without a staple that never succeeds over 200 seeds falsifies it. Control: no market carries `standard` and no `staple` is held in the built realm: hash EQUAL.
- GATE: `python -m pytest engine/season/tests/test_inst_ven_d.py -q` → pass (the smuggler arm asserts `checked >= 200` and at least one success).
- HASH MOVERS: none until a staple is cited or a standard raised.
- DEPENDS ON: V12 Batch B12c (B12c.14: `exchange` drawn); V12 Batch B32 (`COL_A`'s `staple` form; `world_q.in_force`); V12 Batch B05 (`proofs`, `difficulty_levels`); V12 B33.41.
- GLOSSARY: row *staple* (owner `instruments.yaml: forms.staple`; "staple": a trade privilege at a named market, as a staple town's right).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B33's producer; `Item: B33.42`, `[skip ci]`.

### B33.43 — Schoenland's seats · VEN_D §4 (`foreign_seats`) · CONTENT (lane D4: the place is in the tree) · HASH MOVER(encoding)
- SOURCE: VEN_D §4 ("Content rows": `office_bodies`' three Schoenland bodies; `offices.yaml: foreign_seats`, the Schoenland rows; `factions.head_seat`), §2 (the rector pattern), "Gate" (the content bullet: "a realm built with the foreign cast seats Schoenland's rows; `queries/faction_q.py::head` answers a person for Schoenland's Proposition; the realm's pre-item hash is unchanged with the rows absent"); A-44 (D-63, the cast); the place, read in the tree: `engine/season/rosters.yaml: foreign_cast` note ("`Schoenland` IS NOT HERE AND IS FOREIGN ALL THE SAME: its persons and its T16 root are already in the realm as built (`build_realm` keeps T16 out of the realm by giving it no parent)"), `engine/season/venues.yaml` (`Schoenland: S-037`), `cohorts.yaml` (`set_s_037`, "S-037 Schoenland (City, T16)"); precedent B33.09 (one `status: proposed` NPC row, "No name is proposed") and B33.40 (seats "vacant at build").
- ADVANCES: none of the nine; ARC and NPC needs that turn on Schoenland's houses (VEN_D's head).
- INSTRUCTION ("Every content row below is `[ASSUMPTION; medium; Jordan to correct]`; no canon name is coined", B33.40's rule):
  1. The place. VEN_D's "needs a `foreign_cast` row for Schoenland minting one place, WR's" is answered by the tree: Schoenland's place exists in both arms (`terr_T16`, its root; the settlement `S-037` under it). No `foreign_cast` row is added (the note refuses one: "a switch on it would move a world that does not need to move") and no WR item is owed. The rows below anchor at `{territory: "T16"}` and, for the line and yard seats, at `{settlement: "S-037"}` `[ASSUMPTION: the settlement anchor's code form — basis: `{settlement: "ALT-1"}` in `foreign_seats` and `venues.yaml`'s `Schoenland: S-037`; the item reads the anchor resolver at its open and records the form it accepts]`.
  2. `engine/season/rosters.yaml: office_bodies`: `"Assembly": "Schoenland"` ("Every enrolled citizen. Elects; does not debate."), `"Senate": "Schoenland"` ("Votes on the College's written opinions; cannot initiate."), `"Security Council": "Schoenland"` ("Secret bench for offences against the state."), in both maps the file carries (B33.40's note: "The three Schoenland bodies go with B33.43").
  3. `engine/season/offices.yaml: foreign_seats` (built only with `foreign=True`, as Altonia's are, so the control arm `foreign=False` is unchanged), VEN_D §4's rows as written: a head (`post` a functional label, `body: null`, `faction: "Schoenland"`, `remit_acts: [convene]`, `conferral: elected`, `revocation: null`); two councillors and two sages on `Senate` (`remit_acts: [issue]`, `conferral: elected`, `term: 2`; tables `selection: lot`, `cooling_off: 2`); three on `Security Council` (`remit_acts: [determine]`, `conferral: elected`, `term: 4`; table `cooling_off: 4`); one advocate (`remit_acts: [determine]`, `body: "Assembly"`); one line seat and one yard seat on the rector pattern (§2: `conferral: appointed`, `revocation: rung_above_in_holdings`, `term: 8`, `tables.cooling_off: 8`, `audit_at_exit: audit`), vacant at build `[ASSUMPTION: eleven seats and VEN_D's nine persons; the two rector seats are the vacant ones — basis: B32.11's vacant-row build and B33.40's council seats "vacant at build"]`. Row ids `off_schoenland_head`, `off_schoenland_senate_1` … `_4`, `off_schoenland_security_1` … `_3`, `off_schoenland_advocate`, `off_schoenland_line`, `off_schoenland_yard` `[ASSUMPTION: ids; the source names none]`.
  4. The nine holders: nine rows in `references/npc_registry.yaml`, each `status: proposed`, faction `Schoenland`, `territory: T16`, a `[PLACEHOLDER]` role naming the seat, the fifteen pursuits and three concern affiliations `data/cast.py` requires, `[ASSUMPTION; whole row; Jordan to author]`, "No name is proposed" (B33.09's form, verbatim in each row's `source:`). Ids from the NPC block (UNDECIDED 3; B33.09's fallback if B00 gives none). Authored content outside A-44's generated cap, counted with the other authored additions (VEN_D).
  5. `rosters.yaml: factions.head_seat` gains `"Schoenland": off_schoenland_head`; `references/names_index.yaml` gains a row for each new post and body label (VEN_D's head: "posts and bodies are functional labels owed a row in `references/names_index.yaml` before they ship").
- WHERE: `engine/season/rosters.yaml` (`office_bodies`; `factions.head_seat`; `tables`); `engine/season/offices.yaml` (`foreign_seats`: eleven NEW rows); `references/npc_registry.yaml` (nine NEW `proposed` rows); `references/names_index.yaml`; `engine/season/tests/test_inst_ven_d.py`.
- TESTS: `test_inst_ven_d.py::test_schoenland_seats_build_in_the_foreign_arm` (at `foreign=True` the eleven rows build, nine held and two vacant; `faction_q.head` answers the head's holder for Schoenland's Proposition; at `foreign=False` none builds) `[ASSUMPTION: test name (E-3)]`, written first, red.
- FALSIFIER and CONTROL: a Schoenland seat built in the `foreign=False` arm; `faction_q.head` answering nobody for Schoenland with the rows in. Control (VEN_D's): "the realm's pre-item hash is unchanged with the rows absent", and the `foreign=False` build hash equal to B33.42's.
- GATE: `python -m pytest engine/season/tests/test_inst_ven_d.py -q` → pass; `python tools/ci_naming_check.py` → exit 0 (the new labels); `python tools/export_npc_roster.py --check` → exit 0 (if the registry's exporter covers `proposed` rows; the item records which); `python -m engine.season.harness.register --check` → each check's violation count does not rise from the batch's opening reading (quote both, `reading @<sha>`).
- HASH MOVERS: the `foreign=True` build hash (eleven Offices, nine persons; "Each content row is a declared mover", B33.40). Declared; B33.99.
- DEPENDS ON: V12 B33.42 (the batch's tree before it); V12 B33.40 (`office_bodies`' other new body); V12 Batch B32 (B32.11: a vacant row builds; `VEN_C`'s tables and the lot); V12 B33.09 (the NPC block's first id, UNDECIDED 3); EXISTS-IN-TREE `offices.yaml: foreign_seats`, `rosters.yaml: foreign_cast` (its Schoenland note), `terr_T16`, `S-037`, `queries/faction_q.py::head`.
- GLOSSARY: none new (posts and bodies are functional labels, `names_index.yaml` rows).
- IDS: NPC 9 (B33's NPC block, after B33.09's one).
- COST and TIER: content; drafting `opus`, landing `sonnet`, `high` (D-19's pattern); the PR body lists every authored value for Jordan.
- LANDS IT: B33's producer; `Item: B33.43`, `[skip ci]`.

### B33.44 — The Counting-House · VEN_D §5 · POINTER (to B40)
VEN_D §5 is the scenario "The Counting-House" on the spine fixture: a case file `S/cases/exercises/INST-VENICE-01.yaml` with `base: spine` (`SYN_D` §1's schema) and its readings as rows of `harness/institution.py`'s report, run by `python -m engine.season.harness.institution INST-VENICE-01 12 <seed>` (twelve seasons in the source; two before B99, A-114). VEN_D's implementation block: "the scenario's reading lands with SYNTHESIS-D in **B40**"; the schema and the harness are B40's (`SYN_D`), so the case file, its report rows and its gate (stores conserved; every council holder on the list and outside his cooling-off; an `obligation` level at the live arm and none at control; the entrenchment arm, A-80) are B40's items (UNDECIDED 6: A43 carries them). `counting_house.py` is not written. No commit here.

### B33.45 — excused: whoever shuns a man, or was wronged by him, owes him nothing in the odds · SYN_C edit 1, with PAP_D edit 8 · BUILD · HASH EQUAL
- SOURCE: SYN_C "Exact edits" 1 (the predicate and its two readers), "What it changes" 1, "Gate" 1, 2, 3, "Falsifier" first, second and third bullets; PAP_D "Exact edits" 8 ("CR-88's duty decline (when built): one exception, read from the same person-side fact as edit 7"), §3's answer table (the `release` clause); VEN_A's "lifted by" row; X-20, X-29, X-31.
- ADVANCES: none of the nine; "a sanction is worth what the people around its target decide it is worth".
- INSTRUCTION:
  1. "`engine/season/queries/person_q.py::excused(p, holder_id) -> bool` — Person-side, computed when read, no World":
     ```python
     def excused(p, holder_id) -> bool:
         """Is `p` excused from what he owes `holder_id`?  True when EITHER
         (a) `p` shuns him: among `p`'s own live `oblige` Tenures carrying OBEYED_WRIT, one obeys a writ whose
             form has a `forbears` clause `over: named` and whose content (in `p`'s own claim of it) names
             `holder_id`;                                                    -- he chose to comply; it was a draw
         (b) `p` holds a breach against him: `kept(p, r) < 0` for a live instrument `r` in `p`'s ledger whose
             bound party is `holder_id`.                                     -- the other side broke faith first
         Nothing is written.  A man who never heard of the sentence or the breach is not excused."""
     ```
  2. Reader one, "**`person_q.owed_to`** (`15_INSTITUTIONS_VENICE_A` edit 3): an edge toward a seat whose holder, as `p`'s own ledger names him, `p` is excused from counts 0. This replaces VEN-A's ban-keyed lift. Who holds a seat as `p` knows it is `person_q.holders_named` … Until that lands the predicate takes the seat and reads the avoided or breaching person from the writ or instrument, which names him." The item records whether `holders_named` is in the tree (B25's `14_VERBS_SOCIAL2_B`) and which branch it took.
  3. Reader two (PAP_D edit 8 generalised): "**CR-88's duty decline** (when built …): it does not decline `p`'s own `release` of an `oblige` to a seat whose holder `p` is excused from. Whether he releases is his own score." **STOPS IF** CR-88's duty decline is not in the tree at the item's open (`grep` the decline CR-88 builds in `S/decision/options.py`; B21d, UNDECIDED 7): step 3 is not written, it is `HELD (CR-88's duty decline, B21d)` and leaves to the held list, and gate 2 is not read; steps 1–2 land.
  4. "An oath is never dissolved by rule. `gate.py::purview_reaches`' oath clause is untouched."
  5. Create `S/tests/test_inst_syn_c_crossings.py` (the source's named test), written before step 1 and read red.
- WHERE: `S/queries/person_q.py` (`excused`; `owed_to`'s lift); `S/decision/options.py` (CR-88's decline: the one exception, by symbol, only if step 3 runs); NEW `S/tests/test_inst_syn_c_crossings.py`.
- TESTS: gate 1 `test_excused_by_his_own_compliance` ("A lord, a vassal sworn to his seat, a published `avoidance` naming the lord. Arm A: the vassal's `comply` drew Success. Arm B: it drew Failure. The lord then `petition`s the vassal: the recorded levels carry no `obligation` level in A and one in B (at `obligation_level` live). Arm C: the vassal never heard of the writ: as B."); gate 3 `test_excused_by_a_breach` ("A duke under a seeded `homage`; the King's `requisition` inside the duchy succeeds and the duke witnesses it. `kept` as the duke reads it is below zero; `excused(duke, king)` is True; the King's next ask of him carries no `obligation` level. Control: the levy unwitnessed by the duke and untold: `excused` False."); gate 2 `test_the_oath_stays_his` (only if step 3 runs: "Over 200 seeds of arm A with CR-88's decline built: the vassal's `oblige` closes only by his own `release`; a vassal with a planted grievance releases more often than one without, and neither always nor never"; PAP_D's "oath" gate is this test) `[ASSUMPTION: test names (E-3)]`.
- FALSIFIER and CONTROL: "An `oblige` that closes with no `release` act of its owner. A man excused who holds no claim of the writ, the sentence or the breach. Every vassal of a sentenced lord releasing in every seed (the sanction is a switch)." Control: with no `avoidance` complied with and no instrument breached, `excused` is False for every pair and `owed_to` reads as at B33.33.
- GATE: `python -m pytest engine/season/tests/test_inst_syn_c_crossings.py -q` → pass (`checked >= 200` in gate 2 where it runs); `opus` reads gate 2 ("whether a sanction is a switch", SYN_C's tier line).
- HASH MOVERS: none at ship (`obligation_level: None`; no computed `avoidance` is complied with in the built realm).
- DEPENDS ON: V12 B33.33, B33.34, B33.27; V12 Batch B32 (`kept`, `SYN_A` §4; the seeded `homage`, `SYN_B` §3); V12 Batch B28 (`OBEYED_WRIT`); V12 Batch B25 (`person_q.holders_named`, `14_VERBS_SOCIAL2_B`); V12 Batch B21d (CR-88's duty decline: not in §2.1's `after` list, UNDECIDED 7).
- GLOSSARY: row *excused* (new: "excused": released, in the odds only, from what one owes a man one shuns or who broke faith first, as one is excused a debt; owner `person_q.excused`).
- COST and TIER: small build; `sonnet`, `high`; gate 2 `opus`.
- LANDS IT: B33's producer; `Item: B33.45`, `[skip ci]`.

### B33.46 — the suit's forum stated; a hand of another faction · SYN_C edits 3, 6 · BUILD · HASH EQUAL
- SOURCE: SYN_C "Exact edits" 3 and 6, "Gate" 5, "Falsifier" (the suit bullet); CR-60 (realm benches, B24a); `PAP_A` edit 3 (B32).
- ADVANCES: none of the nine; "a king cannot be sued" ends; BYZ_D edit 5's reliance holds.
- INSTRUCTION:
  1. Edit 3, no code but a comment: "Stated in `arrangements.yaml`'s header comment for `debt_suit`: *'a suit is brought where a bench sits over the debtor; for a holder of a realm seat that is his own court or the Church's.'*" `debt_suit` (B33.38), `audit` and `quo_warranto` (B33.18) "are docketed by `open_case` before a bench for which `may_determine` holds, which asks `sits_over(seat, home_of(party))`".
  2. Edit 6: "`passes_through` … admits a body or a seat of any faction, and the loader does not compare factions. `15_INSTITUTIONS_BYZANTINE_D` edit 5 already relies on it … The basis rule `hand` in `data/requires.py` asks only that the actor hold the named seat or a seat of the named body; BYZ-C's further conjunct ('drawn up at a rung the issuing seat's purview reaches') is about the issuing seat and stands." No code: the test below holds the loader to it.
- WHERE: `S/arrangements.yaml` (the comment above `debt_suit`); `S/tests/test_inst_syn_c_crossings.py`.
- TESTS: `test_a_hand_of_another_faction_loads_and_enters` (a Guilds seat whose `passes_through` names an Altonian seat loads, and that seat's holder may `carry` at the hand); gate 5 `test_a_bond_before_the_church` ("A `debt` lapsed whose debtor holds a realm seat. `open_case` under `debt_suit` is admitted before a bench of realm scope and refused (`may_determine`) before a ducal bench. Over 200 seeds all four bands occur; a `ban` disposed there reads CH on the strife instrument") `[ASSUMPTION: test names (E-3)]`.
- FALSIFIER and CONTROL: "A suit admitted before a bench that does not sit over the debtor." Control: comment-only edit to the YAML (the loader's reading equal).
- GATE: `python -m pytest engine/season/tests/test_inst_syn_c_crossings.py -q` → pass (`checked >= 200`).
- HASH MOVERS: none.
- DEPENDS ON: V12 B33.38, B33.11, B33.07, B33.29; V12 Batch B24a (CR-60's realm `scope_rung`, through B27 and B32); V12 Batch B32 (`PAP_A` edit 3); EXISTS-IN-TREE `S/state/gate.py::may_determine`, `::sits_over`.
- GLOSSARY: none.
- COST and TIER: edit (a comment) and tests; `sonnet`, `high`.
- LANDS IT: B33's producer; `Item: B33.46`, `[skip ci]`.

### B33.47 — a publication is not a command: `issue` asks the form's basis · SYN_C edit 7 · BUILD · HASH MOVER(behaviour)
- SOURCE: SYN_C "Exact edits" 7, "What it changes" 7; X-33; A-21, A-22; `SYN_A` §1 (the form row's `basis: command | purview`, default `command`; `avoidance: purview`); `14_VERBS_BINDING_D_orders.md` edits 3 to 5 (B21: `issue`'s `authority` conjunct, `basis: command`).
- ADVANCES: none of the nine; the sanction reaches the persons it is aimed at.
- INSTRUCTION: "Decided: the basis is a property of the **form**. A form row carries `basis: command | purview` (default `command`); `issue`'s `authority` conjunct asks the basis the chosen form names, and the bare decree (no form) asks `command`. `avoidance` is `purview` … `interdict` and `tithe` stay `command` … One conjunct, one reader, no second predicate: both basis values are that proposal's." The key is `SYN_A`'s (B32); this item writes its one reader in `S/data/requires.py`'s `basis` dispatch for `issue`. "`[UNVERIFIED]` that the `authority` conjunct can read a value sourced from the act's `form` operand; if a `requires` cell cannot be keyed by an operand, `issue` gains a second row alternative for published forms, which is the table's existing way to say 'either'." The item opens the dispatch first and records which branch it took.
- WHERE: `S/data/requires.py` (the `basis` dispatch, by symbol); `S/verb_table.yaml` (`issue`: only in the second branch, a row alternative); `S/tests/test_inst_syn_c_crossings.py`.
- TESTS: `test_an_avoidance_addresses_the_seated_vassals_of_another_lord` (a see's `issue` of form `avoidance` admits a seated vassal on the see's ground who is neither sworn nor revocable; the same see's bare decree to him is refused); `test_an_interdict_addresses_only_the_commanded` `[ASSUMPTION: test names (E-3)]`, red first.
- FALSIFIER and CONTROL: an `avoidance` refused toward a person on the issuing seat's ground; a bare decree admitted toward a person the seat does not command. Control: every `issue` naming no form (all of the built realm's) asks `command`, as B21 left it.
- GATE: `python -m pytest engine/season/tests/test_inst_syn_c_crossings.py engine/season/tests/test_command_basis.py -q` → pass (`test_command_basis.py` is B21's, and stays green).
- HASH MOVERS: any seeded run in which a computed `issue` chooses a `purview` form (`choice_sourced: issue: [form]`, `SYN_A` §2). Declared; B33.99.
- DEPENDS ON: V12 Batch B21 (`world_q.commands`, the `basis` value `command`; `test_command_basis.py`); V12 Batch B32 (`SYN_A` §1, §2); V12 B33.46.
- GLOSSARY: row *publication* (new: "publication": a writ that addresses everyone on the issuing seat's ground and orders nobody, as a banns is published; owner `instruments.yaml: forms[].basis: purview`).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B33's producer; `Item: B33.47`, `[skip ci]`.

### B33.48 — rival certificates · SYN_C edit 4 · POINTER (to B32.10 and B33.23; edit 5 is B33.49; lane D4)
- What it points at (E-5): SYN_C edit 4's one sentence ("**a Record carrying `recites` for a seat is admissible on either side of any docketed matter whose petition names that seat**, each recited deed filed as one item") is `SYN_B` §4's request, built at the evidence owner by V12 B32.10 (lane D4: the filing step B24.25 landed, one branch, either side, since the owner files a cite for whichever side cites it). A rival's deeds "do not contradict the claimant's (they are different cells), so nothing is struck; they stand against, as the other side's levels" (SYN_C §4): no further code.
- Gate: SYN_C gate 6 ("Rival paper. A consecration hearing with the claimant's certificate cited, with and without a rival's certificate for the same seat cited against it: exact odds printed; the advantage shrinks") is read in B33.23's `test_inst_pap_c.py`, its Arm C. Edit 5 (the immunity in the levy) is B33.49. No commit here.

### B33.49 — a grant against a levy: the levied side's levels · SYN_C edit 5 (lane D4: built at the `proofs` reader B33.04 writes) · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/15_INSTITUTIONS_SYNTHESIS_C_crossings.md` §5 ("A grant against a levy"), "Gate" 7, "Falsifier" ("An immunity that refuses a levy at the gate"); C3-C10 ("nothing is subtracted from the obstacle"); precedent B33.04 (this batch writes the collector's `proofs` reader for `requisition` in `S/seam/wrappers/sigma.py`) and B33.42 (a `staple` read as a `proofs` level on `exchange` at the same reader); lane D4's ladder record.
- ADVANCES: none of the nine; "An immunity nobody on the ground has heard of protects nothing; one the whole town holds makes the levy harder and its taking a known breach" (SYN_C §5).
- INSTRUCTION, copied (SYN_C §5): "On `requisition` and `seize` …, the `proofs` source has two sides: the actor's levels, a held assessment and the instrument that confers the exercised seat …; **the other side's** levels, a live instrument one of whose `forbears` clauses names this act's success kind over this ground, when the levied cohort or holder holds its content claim. Unit: one `proof_level` per instrument (C3-C10: nothing is subtracted from the obstacle)." Here: in the `proofs` reader B33.04 wrote for `requisition` (by symbol), the opposing side's levels are summed over live instruments (`world_q.in_force`, B32) with a `forbears` clause naming `requisition.taken` (the row's success kind) over a rung containing the requisitioned one, counted when the cohort residing at that rung (B12c.13's `regard` operand's cohort) or the rung's holder holds the instrument's content claim; one `proof_level` per instrument; netted under the soft cap by the one composer (`levels_to_net_sigma`), never a gate. **`seize`**: the same reader serves it only if `seize`'s draw composes a `proofs` source at the item's open (`grep` its row and wrapper; record which); if it composes none, the `seize` half is recorded and not built (no second reader is written).
- WHERE: `S/seam/wrappers/sigma.py` (the `proofs` reader for `requisition`, B33.04's); `S/tests/test_inst_syn_c_crossings.py` (B33.45's file).
- TESTS: SYN_C gate 7 as `test_the_immunity_in_the_levy` ("400 seeded levies on a ground under a seeded `immunity` the cohort holds a claim of, and 400 on a like ground without: Failure's share is higher inside; each arm holds at least three bands. Control: the cohort holds no claim of the grant: the arms' shares are equal within sampling"), `assert checked >= 400` per arm `[ASSUMPTION: test name (E-3)]`, written first, red.
- FALSIFIER and CONTROL: "An immunity that refuses a levy at the gate" (SYN_C); a level counted for an instrument the levied side holds no claim of. Control: the cohort holds no claim of the grant: the two arms' Failure shares equal within sampling; realm hash at seed 0, one season, equal to B33.48's tree where no levied side holds such a claim (read and quoted).
- GATE: `python -m pytest engine/season/tests/test_inst_syn_c_crossings.py -q -k immunity` → pass (`checked >= 400` per arm).
- HASH MOVERS: any seeded run in which a `requisition` falls on a ground under a live instrument whose `forbears` names it and whose content claim the levied side holds (the seeded `ins_containment_charter`, an `immunity` at T9, B32.08, is such an instrument where its holders hold the claim). Declared; B33.99.
- DEPENDS ON: V12 B33.04 (the collector's `proofs` reader for `requisition`); V12 Batch B32 (`world_q.in_force`; the `forbears` clauses and the `immunity` form, `SYN_A`/`COL_A`; B32.08's seeded instruments); V12 Batch B12c (B12c.13: `requisition` drawn, the residing cohort); V12 Batch B05 (`proof_level`, `levels_to_net_sigma`).
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`; gate 7's reading `opus`.
- LANDS IT: B33's producer; `Item: B33.49`, `[skip ci]`.

### B33.50 — deeds done at a place: `deed_doers` narrowed `under:` a rung · PAPACY-C §3's request (and BYZ-G item 2's) to `data/goals.py`'s owner (lane D4) · BUILD · HASH EQUAL
- SOURCE: `proposals/15_INSTITUTIONS_PAPACY_C_consecration_and_deed_ledger.md` §3 (`[UNVERIFIED: the `kinds:` form has no place filter … The narrowing (deeds whose claim subject lies under a named rung) is a fourth `deed_doers` form and belongs to `data/goals.py`'s owner; it is requested, not built here. Until then the row ships OFF.]`), "Exact edits" 4; BYZ-G "Item 2" ("with the filter, the row's `under:` names the treaty ground"; B40.13); the tree's precedents: `queries/person_q.py::deed_doers`' `against:` form ("the caller (`world_q.goal_referents`, a World read) resolves and passes in"), `queries/world_q.py::place_of` ("The rung a THING is at, for ANY id", ARCH §F.14's own name), `queries/world_q.py::within` (a rung's ancestry); lane D4's ladder record.
- ADVANCES: none of the nine; the carrier of two goal rows that ship off without it (`goal_church_liberties_kept`, B33.24; `goal_kommerkiarios_side_roads`, B40.13).
- INSTRUCTION:
  1. `engine/season/data/goals.py` (the `deed_doers` branch of the object check): the `kinds:` form admits one optional key `under: <rung id>`, checked at seeding as the `rung` kind's id is (IN-68: "checked at seeding … once rungs exist"); `under` beside any other form is refused naming the row. `rosters.yaml: goal_object_kinds.forms.deed_doers`' note gains one sentence for it (the form list itself is unchanged: `under` narrows `kinds:`, it is not a fourth way to name a deed).
  2. `engine/season/queries/world_q.py::goal_referents` (the World-side caller, `against:`'s precedent): for a `deed_doers` object with `under: R`, it passes `deed_doers` the predicate "the claim's subject lies under `R`", resolved as `R` in the ancestry of `place_of(w, subject)` (the one owner of "the rung a thing is at": a rung subject is its own place, a person his, a Record its holder's) `[ASSUMPTION: read at the time of the read, not the deed's — basis: `place_of` reads the present; a deed's own place is no stored field (no Claim or Event field is added)]`.
  3. `engine/season/queries/person_q.py::deed_doers(ledger, spec, holder, against=(), under=None)`: a claim passes the `kinds:` form only if `under` is `None` or `under(claim.subject)` is true; the paired-kind rule (`deed_doer`) and the never-the-holder rule are unchanged. Person-side, no World: the predicate arrives resolved (AX-2), as `against` does.
- WHERE: `engine/season/data/goals.py` (the `deed_doers` check); `engine/season/rosters.yaml` (`goal_object_kinds`' note); `engine/season/queries/world_q.py` (`goal_referents`); `engine/season/queries/person_q.py` (`deed_doers`); NEW `engine/season/tests/test_deed_doers_under.py` `[ASSUMPTION: test-file name (E-3)]`.
- TESTS: `test_a_deed_under_the_named_rung_names_its_doer_and_one_elsewhere_does_not` (one holder told of two seizures, one at a settlement under `R` and one outside: the `under: R` goal names the first doer only), `test_under_beside_against_is_refused_at_load`, `test_no_under_is_todays_reading` `[ASSUMPTION: test names (E-3)]`, written first, red.
- FALSIFIER and CONTROL: a doer named for a deed whose subject lies outside `R`; `deed_doers` reading the World (it must receive the predicate). Control: no shipped goal row carries `under:` at this item: realm hash at seed 0, one season, equal to B33.49's tree.
- GATE: `python -m pytest engine/season/tests/test_deed_doers_under.py -q` → pass; `python -c "import engine.season.data.goals"` → loads.
- HASH MOVERS: none (no shipped row uses the key here; B33.24's and B40.13's rows ship it, each declaring its own move).
- DEPENDS ON: V12 B33.49 (the batch's tree before it); EXISTS-IN-TREE `data/goals.py` (the `deed_doers` branch), `queries/person_q.py::deed_doers`, `queries/world_q.py::goal_referents`, `::place_of`, `rosters.yaml: goal_object_kinds`.
- GLOSSARY: none (`under` is the plain word, as a place is under a rung).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B33's producer; `Item: B33.50`, `[skip ci]`. B33.24's `goal_church_liberties_kept` (shipped commented out) may then ship with `under:` naming Himmelenger's rung: not done by this item; listed for the orchestrator (part 2 §4 row 88, B98.69).

### B33.99 — re-pin and close readings · `V12_STRUCTURE_part4.md` E-1 · BUILD · HASH MOVER (the re-pin)
- SOURCE: E-1, E-2; `V12_STRUCTURE_part2.md` §5.9, §5.12; CLAUDE.md §7 ("say plainly when you re-record one").
- ADVANCES: the batch's close; `IS-A-12`'s record.
- INSTRUCTION: (1) re-record, once, the realm pins in `S/tests/_realm_goldens.py` (B02's one pin file) at seeds 0, 1, 2 — build, one season and two seasons, both arms of `build_realm(foreign=)` — read against B31's after-reading (`reading @<sha>`; the RE-PIN line; lane H3); (2) any other seeded result a test of this batch pins and two items moved; (3) the commit says "re-pin" and lists the moving handles: B33.01 (encoding, if `Office` values are encoded), .02, .03, .04, .05 (encoding: the `Office` fields `passes_through`, `hand_term` it adds; R2d, CHK_K9 #2), .08, .09, .10, .11, .12, .14, .15, .16, .17, .19, .21, .25, .26, .31, .40, .43 (encoding, the foreign arm; lane D4), .47, .49 (lane D4); (4) the commit body carries the readings of §5.12: `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, the executed-verb tallies of `corpus_run --seasons 2` [v12: two seasons a case, D-17; the case's own span, to `MAX_SEASONS`, is B99's] at seed 0 beside B31's after-reading (lane H3), and the batch's measured wall time; no conjunct's `reading:` is written (REQUIREMENT: none); `status:` is not edited.
- WHERE: `S/tests/_realm_goldens.py`; any test-local pin two items moved.
- TESTS: the batch's thirteen test files and the covering suites (`python tools/tests_for_diff.py --base <batch-start-sha>`), the one full-suite run (CLAUDE.md §0.4; E-2).
- FALSIFIER and CONTROL: a pin that moved with no declared mover in the batch (stop: an undeclared mover is a defect of its item, not a re-pin). Control: the executed-verb tallies of every hash-EQUAL item's control equal.
- GATE: the BATCH GATE of the block head.
- HASH MOVERS: the re-pin itself.
- DEPENDS ON: V12 B33.01 to B33.50 (B33.49, B33.50 lane D4).
- GLOSSARY: none.
- COST and TIER: reading and a re-pin; `sonnet`, `high`.
- LANDS IT: B33's producer; `Item: B33.99`, the batch's last `Item:` commit (no `[skip ci]`: it opens BATCH-CLOSE's first CI run).

**SERIAL EDGES (written last, E-11).** Within the batch, U3 §1.2's order with these edges: B33.01 → B33.02 (`upkeep_owed` reads the authored grades) → B33.03 (the bill sums `upkeep_owed`) → B33.04 (Partial's remainder is read by `bills_due`). B33.05 → B33.06 (the occasion reads `hand:` stages) → B33.07 (`carry`'s alternative needs an open `hand:` stage and the occasion) → B33.08 (rows turn the hands on only after the machinery is EQUAL-landed). B33.08 → B33.09 → B33.10 (the court's row names the person and `off_doux`) → B33.11 (`hand_term` on rows that exist) and → B33.12, B33.17; B33.11 → B33.13. B33.10 → B33.14 (`centre.hops`, `root_of` over the foreign root) → B33.15 (the host reads the one reader) and → B33.16 (the border test asks `root_of`). B33.15 → B33.19 (the opener's distance). B33.18 → B33.19, B33.20. B33.21 → B33.22. B33.23 → B33.24. B33.25 → B33.26, B33.28, B33.29; B33.27 → B33.45 (`excused` (a) reads the compliance B33.27's decline keys on). B33.31 → B33.32. B33.33 → B33.34 → B33.35 (the bond's reckoning reads `obligation`) → B33.36 → B33.37 → B33.38; B33.34 → B33.45 (the lift is on `owed_to`). B33.38 → B33.46 (the comment sits on `debt_suit`); B33.11 → B33.46 (the cross-faction hand). B33.46 → B33.47. B33.18 → B33.40 (`audit_at_exit: audit` on the council seats). B33.39 → B33.40 → B33.41 → B33.42. B33.04 → B33.34 (the `obligation` level on `requisition`), B33.07 → B33.34 (on `carry`); both point forward. B33.99 last. With other batches, by step (§2.3), on the files this batch edits (U3 §5.1's chains re-read in v12's order): `S/offices.yaml` B21 → B32 → B33 → B40; `S/rosters.yaml` B32 (S17) → B31, B33 (S19, different keys; B31 merges first) → B38; `S/verb_table.yaml` B32 → B33, B36 (S19, different rows; B33 merges first) → B38; `S/data/fixtures.py` B32 → B33 → B38; `S/queries/world_q.py` B32 → B33 → B38 → B40; `S/queries/person_q.py` B32 → B33 → B38; `S/loop/effects_information.py` B32 → B33 → B38; `S/decision/options.py` B28 → B33 → B38; `S/seam/wrappers/sigma.py` B32 → B33; `S/arrangements.yaml` B32 → B33 → B40; `S/loop/effects_governance.py` B32 → B33 → B39; `S/loop/effects_economy.py` B12c → B33; `modules/social_contest/roll.py` B05 → B33; `references/npc_registry.yaml` B37 (S16) → B33 → B38; `S/data/requires.py` B22 → B35 (S18) → B33 (U3 lists B33 before B35; v12's schedule opens B35 a step earlier, and B35 does not gate on B33: each edits its own basis or row, kept by hand); `S/epistemic.py` B28 → B33 → B38; `S/instruments.yaml` B32 → B33 → B39 → B40; `S/goals.yaml` B10 → B33 → B40; `S/harness/strife_moves.yaml` B32 → B33; `S/boot/realm.py` B32 → B33 → B38. Edges not taken, recorded for H2: B21d → B33 (UNDECIDED 7; asked, not added here). Requirement order and dependency order do not conflict here (REQUIREMENT: none).

**FILE CENSUS (this batch; every WHERE, parsed by hand):** `S/offices.yaml` (B33.01, .08, .10, .11, .19, .21, .31, .32, .39, .40); `S/rosters.yaml` (B33.08, .09, .10, .12, .16, .17, .21, .31, .34, .35, .40); `S/verb_table.yaml` (B33.04, .07, .25, .47); `S/arrangements.yaml` (B33.18, .23, .26, .38, .41, .46); `S/goals.yaml` (B33.17, .24, .32); `S/queries/world_q.py` (B33.02, .03, .06, .14, .19); `S/queries/person_q.py` (B33.27, .33, .45); `S/queries/inputs.py` (B33.15, .34); `S/seam/wrappers/sigma.py` (B33.04, .15, .28, .34, .42); `modules/social_contest/roll.py` (B33.15, .34); `S/data/fixtures.py` (B33.14, .20, .28, .34, .38); `S/hole_register.yaml` (B33.14, .20, .28, .34, .38); `S/data/requires.py` (B33.07, .47); `S/data/rosters.py` (B33.05, .09, .16); `S/data/verbs.py` (B33.04, .07); `S/state/carriers.py` (B33.05: the two `Office` fields B32 leaves to B33); `S/loop/effects_information.py` (B33.05, .07, .23, .25, .36); `S/loop/effects_governance.py` (B33.04, .25, .35); `S/loop/effects_economy.py` (B33.02, .37); `S/epistemic.py` (B33.16); `S/decision/options.py` (B33.27, .45); `S/boot/realm.py` (B33.09, .39); `S/write_matrix.yaml` (B33.07); `S/harness/strife_moves.yaml` (B33.29); `S/venues.yaml` (B33.42); `S/instruments.yaml` (B33.27, if absent); `references/npc_registry.yaml` (B33.09); `references/names_index.yaml` (B33.40); `unified/U1_GLOSSARY.md` (B33.01, .03, .04, .05, .07, .14, .16, .18, .20, .23, .27, .28, .31, .33, .34, .35, .40, .42, .45, .47); NEW tests: `test_inst_byz_b.py` (B33.01–.04), `test_inst_byz_c.py` (B33.05–.08), `test_inst_byz_d.py` (B33.09–.12, .17), `test_remove.py` (B33.14–.16), `test_audit_and_charter.py` (B33.18–.20), `test_inst_col_d_ledger.py` (B33.21–.22), `test_inst_pap_c.py` (B33.23), `test_inst_pap_d.py` (B33.25–.28), `test_inst_pap_e.py` (B33.31–.32), `test_inst_ven_a.py` (B33.33–.34), `test_inst_ven_b.py` (B33.35–.38), `test_inst_ven_d.py` (B33.39–.42), `test_inst_syn_c_crossings.py` (B33.45–.47). Differences from U3 §5.1: `S/data/requires.py` (U3: B33 before B35; v12 by step: after, see above); `S/loop/matter.py` is in U3's B33 chain and is **not** edited here (C3-C7: BYZ_B, BYZ_C, VEN_B each withdraw their MATTER edit; three items gate `git diff … loop/matter.py` empty); `S/governance_spine.yaml` is in U3's B21 → B33 chain through VEN_D's scenario, which is B40's here (B33.44); `S/queries/inputs.py`, `S/venues.yaml`, `references/names_index.yaml`, `S/write_matrix.yaml`, `S/hole_register.yaml` are edited here and have no U3 §5.1 chain naming B33. Hot files (U3 §5.1, twenty or more proposals) this batch edits: `rosters.yaml`, `fixtures.py`, `world_q.py`, `verb_table.yaml`, `person_q.py`, `options.py`, `boot/realm.py` (was `populated.py`), `sigma.py`, `offices.yaml`, `effects_information.py`.

| STOP. Batch B33-inst-economy-hands closes here |
