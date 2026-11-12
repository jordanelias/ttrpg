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
- GATE: `python -m engine.season.harness.register --check` → exit 0; `build_realm(0)`'s content hash → equal to B33.23's reading.
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
- GATE: `python -m pytest engine/season/tests/test_inst_pap_d.py -q` → pass (`checked >= 200`); `opus` reads the "answers differ" arm (PAP_D's tier line).
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

### B33.30 — the standing levy, the `tax` edict · CP-T08-07 · BLOCKED (SE/FA: H-163 limit 3(a), a governor's stock claim, has no owner)
Placed here by `V12_STRUCTURE_part2.md` §5.6's first rule: PAP_E, the next member, names CP-T08-07 ("the tithe gate waits on it"). The intake entry (`:333`): MISSING-DEP, rows E1:119, E4:307, E4:679, E5:48; **settled:** "its gate H-163 limit 3(a) has no owner in the tree or any proposal (E5:48); owner FA/SE; the tithe and tax kit files wait on it." Its carry-forward (E5 Block C17, the v11 override AM-E-18): "CP-T08-07 is gated on H-163 limit 3(a) (a governor holds a stock claim of the rung he taxes) and does not build before it. Its 'one slot per place' is a slot on EDICTS only … It no longer needs CP-T08-08 … Compliance by `unrest` band (item 5) stays as written and ships at 1000." What it would build when unblocked is the home entry's six parts (E1 §Carry-forward, line 1318: the verb row `tax`, the Record kind `edict` with `edict_kinds: {tax: {phase_in}}`, one slot per place, collection as the holder's `requisition` through the `levy_due` question source, `unrest_compliance` at 1000, and the withdrawals), its falsifier `test_tax_edict.py` on `harness/scarce.governed` and its control "`tax` ships in `Fixtures withheld_verbs` and `unrest_compliance` at 1000". Not built: no item lands until an owner of H-163 limit 3(a) exists. What waits on it here: PAP_E's tithe gate (B33.32 notes it). Owner: FA/SE (the intake). Listed in `V12_STRUCTURE_part3.md` §8.2's "nine blocked entries".

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
- TESTS: none new.
- FALSIFIER and CONTROL: "A tithe that moves stores with no `requisition` act by a see-holder. Reach through a house that survives its head's `release`." Neither can occur here (no levy, no house row). Control: the build hash equal to B33.31's reading `[UNVERIFIED: whether a goal row's `text` enters the content hash; if it does, the hash moves by the text and the re-pin records it]`.
- GATE: `python -m engine.season.harness.register --check` → exit 0; the tithe gate ("after the levy lands: one writ, three sees; stores at `terr_T9` rise by the sum of the renders of the sees whose holders complied") waits on B33.30 (BLOCKED) and is not run; the exempt-house gate ("with the house row on and its holder sworn, `purview_reaches(off_cardinal_fortitude, duchy_hafenmark)` True; after his `release`, False") is run as a hand-built test in `test_inst_pap_e.py` with the row planted in the test's world only: `test_reach_by_oath_ends_with_the_release` `[ASSUMPTION: test name (E-3)]`.
- HASH MOVERS: none (see the `[UNVERIFIED]` above).
- DEPENDS ON: EXISTS-IN-TREE `S/goals.yaml: goal_cardinal_prudence_tithes`, `S/state/gate.py::purview_reaches` (the oblige clause); V12 B33.31; MISSING (SE/FA: CP-T08-07, B33.30) for the tithe gate.
- GLOSSARY: none.
- COST and TIER: content; `sonnet`, `medium`.
- LANDS IT: B33's producer; `Item: B33.32`, `[skip ci]`.
