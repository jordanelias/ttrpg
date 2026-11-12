# INST-SYN-E — one implementation plan for the institutions: ten batches, their edges to every other lane, their gates, cost classes

Reconciled: 2026-11-12, U5d closure — folded **A-36**, **A-35**, **A-41 / A-42**, **A-13** and **A-12**. From the deferred list: the council that judges the Confessor (`15_INSTITUTIONS_PAPACY_E` item 5) is dropped, not deferred (A-36); schism (item 6) stays design-first and is now the only lawful answer to a bad Confessor besides his death or resignation; the `corvee` form is not built (A-41). Un-held and scheduled in its family's batch: `15_INSTITUTIONS_PAPACY_B` item 4 (`head_of_faction`, A-35). Added to the batch that lands the councils and elections: the territory and caste vote weight (`U5d_FA_owed_edits.md` §4), whose first reader they are (A-42). Batches that add seat keys (`passes_through`, paper-hands, `audit_at_exit`) proceed on a ruled shape (A-13). A seat modifier may be scheduled as content after the one obstacle form lands (A-12).

Reconciled: 2026-11-12, wave 3 lane W3-4b — rewritten against A-12 to A-14, A-35, A-36, A-41 to A-43, A-56 and the four grounding plans (`OWED_TO_UNIFICATION.md` §B); applied `R4_READ.md` §1.7 (SYN_E: stale against A-35, A-36, A-41 in I-10), §2 (the PAP_E/SYN_E row; the electorate row), §7, 7b.0, 7b.7 ("I-10: delete the council …; delete `head_of_faction` (scheduled in I-6) and `corvee`; I-6's election gate quotes the built-realm arm with two electors; 'twenty-six' → 'twenty-five'"); `U3_CONFLICT_LEDGER.md` C3-N21 (the plan's size), C3-N31 (form count by command), §9; `U3_DEPENDENCY_ORDER.md` B32, B33, B39, B40 (**the suite's one order governs where it differs from this plan's I-n order**; mapped below); `U1_OWNERS_AND_VOCABULARY.md` D-U1-11k (`distance`). Changed: I-10 holds only what is still held; the council is dropped (A-36), `head_of_faction` is scheduled in I-6 (A-35), `corvee` is not built (A-41); I-6's election gate runs the two electors in force beside the hand-built four; the term names follow the kit (`distance`, `obligation` as a level, the lapse read when read, `rank_gap`); the four grounding plans are placed; the I-n batches are mapped to the U3 handles. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "vocation" → "capability"; capability `judgment` → `law` (glossary *capability*, *law*); "graded route" → "task route" (glossary *task*).

## Status: PROPOSED (a plan; it schedules the twenty-one family proposals, this lane's A to D and the four grounding plans, and builds nothing itself)

**Implementation block (W3-4b; `R4_READ.md` 7b.0).** Listed in batch **B40**, last (`U3_DEPENDENCY_ORDER.md` §1 item 40): a plan lands nothing; it is read by v12's author. Lane tag: IN (cross-cutting: it orders FA, SC and verb-lane work). Tier: none (a plan); v12's author reads it at `opus`. Named test: none; its gate is SYNTHESIS-D's (the integrated scenario) and the per-batch gates below. Standing sentences: *Pool*, *Failure writes*, *Draw keys* — the plan adds no roll, row or draw; every batch's files carry their own (A-6 to A-8, A-81, A-30). *Entrenchment* — the plan's gate includes SYNTHESIS-D gate 8 (A-80).

**The one order (U3) against this plan's batches.** U3's handles are the landing order; the I-n names below are kept as this plan's grouping of gates and are not a second order. B32 (institutions kit) carries I-1, the key and roster halves of I-6, PAP-A, PAP-B (with `head_of_faction`), VEN-C, BYZ-A, BYZ-E and SYN-B's ledger reader (I-3 in part); B33 (economy and hands) carries I-2 (VEN-A, COL-B §1, now in B33, after B32), I-4, I-5, I-7 and I-8's PAP-E and VEN-D; B39 carries SYN-B's and COL-D's prehistory (I-3 in part); B40 carries I-9 and the four grounding plans. Where an I-n gate below names a file U3 places later, the gate runs at that later batch.

Source: `audits/15_INSTITUTIONS_SYNTHESIS.md` §9; the four family audits' own plans
(`15_INSTITUTIONS_BYZANTINE.md` §12, `…_PAPACY.md` §11, `…_VENICE.md` §13, `…_COLONIAL.md` §12), which
this file merges and orders. A workplan is one per lane and `CURRENT.md` names it (CLAUDE.md §2): this
file is a **proposal for the batches** such a plan would carry, not a second plan. Ratifies nothing.

## What it changes in `engine/season/` at runtime

Nothing. It fixes the order in which the kit's edits land, what each waits on, and the execution artifact
that shows each batch worked.

## The problem (evidence)

The four family plans are each ordered internally and each depends on the same other-lane proposals, but
they were written without sight of each other: three of them land a founding-order carrier
(BYZ batch A, PAP batch 4, COL batch C-4), two land an audit (VEN batch C, COL batch C-3), two land the
Altonian superior (BYZ batch D, COL batch C-2), and four name different first playables. Landed in their
own orders they would collide on files (`offices.yaml`, `rosters.yaml`, `arrangements.yaml`,
`data/fixtures.py`, `queries/person_q.py`) and on facts (audit §2).

## The resolution, decided

Ten batches, a batch being a set of items linked by a shared file or gate (`methodology-execute`'s unit).
The reconciled owners land first and empty (I-1), so every later batch writes into a home that exists.
Ladder step 5.

## The batches

Each row: what lands, from which files, the gate (an execution artifact, with its control and a planted
failure), and the cost class. `PYTHONHASHSEED=0` for every seeded run; every gate on a draw reports band
frequencies over seeds.

### I-1 — the owners (hash EQUAL)

- **Lands:** `15_INSTITUTIONS_SYNTHESIS_A` in full; `15_INSTITUTIONS_COLONIAL_A` edits 1 to 7 as
  reconciled (the registry empty of seeded rows; every form loaded, the count read by command, C3-N31).
- **Gate:** SYN-A gates 1 and 2 (neutral until used; the loaders refuse); COL-A's `test_instruments.py`
  loader half.
- **Planted failure:** a seat row carrying `audited:`; a form with `by: addressee` under `covenant`.
- **Cost:** small build.

### I-2 — ties and distance in the odds (EQUAL at ship)

- **Lands:** `15_INSTITUTIONS_VENICE_A` (edits 1 to 5: the `obligation` leverage source; member 12's
  widened read); `15_INSTITUTIONS_COLONIAL_B` §1 as reconciled (the distance between two rungs is OBS
  member 20 `distance` with `distance_step`, D-U1-11k; `remove` and `remove_step` are not added).
- **Gate:** VEN-A's hand-built pair (the recorded levels differ by exactly `obligation`) and its
  sealed-room arm; COL-B's 400-and-400 rolls at `distance` 0 and 4 hops (Failure's share higher at 4;
  each arm holds at least three bands); at control values the realm's hash at build and each season
  equals the pre-item hash.
- **Planted failure:** read the actor's edges instead of the counterparty's; read the seat's rung instead
  of the actor's place.
- **Cost:** small build. Each fixture's move to its proposed value is its own declared mover.

### I-3 — the deed ledger (declared build mover)

- **Lands:** `15_INSTITUTIONS_SYNTHESIS_B`; `15_INSTITUTIONS_BYZANTINE_A` edits 3, 4 (`dignity_grades`
  only), 7 (the dignity conjuncts and the telling of the cited deed, on the BINDING lane's `confer`
  draw); `15_INSTITUTIONS_COLONIAL_D` edits 4 and 5.
- **Gate:** SYN-B gates 1 to 3 and 5; BYZ-A gate 2 (a `confer` of a dignity over 200 seeds: all four
  bands; with the roll pinned, every seed opens the hold).
- **Planted failure:** swap two founders' deed counts; read the chain from the world's Tenures.
- **Cost:** small build.

### I-4 — the purse (movers)

- **Lands:** `15_INSTITUTIONS_BYZANTINE_B` (edits 1, 3, 4 with `default_store_kind`; edit 5 as terms and
  band requests on the MATERIAL lane's `requisition`); `15_INSTITUTIONS_VENICE_B` (the `debt` kind, the
  mint in `_eff_covenant`, the count in `_eff_transfer`, the lapse read when read from `world_q.owed`
  (no `debt.lapsed` kind, C3-C7), `debt_suit`, the distraint check); the forms `homage`, `farm`, `tribute` in use under `dues`, `kept`, `breaches`.
- **Gate:** BYZ-B gates 1 to 3 (nothing moves at build; the collection is drawn and conserves; sworn terms
  both renew and mature across twenty seeds, control `oblige_term: None`); VEN-B's hand-built chain
  (mint, part payment, reckoning by band, extension, the last stage's `term.matured` with `owed > 0`,
  suit, a `ban` that
  refuses a `confer` inside the bench's purview and admits one outside); COL-A's tribute occasion test
  (stamped in season 1, gone after payment, back in season 2); stores conserved by every act.
- **Planted failure:** count a `transfer` to the wrong place toward a debt; delete the period test in
  `dues`.
- **Cost:** small build, three times.

### I-5 — paper and distance (movers; the court in the foreign arm only)

- **Lands:** `15_INSTITUTIONS_BYZANTINE_C`; `15_INSTITUTIONS_BYZANTINE_D` and `15_INSTITUTIONS_COLONIAL_B`
  §4 as one seat (audit X-13); COL-B §2's terms on `issue`, §3's reach rows, §5's ending row.
- **Gate:** BYZ-C gates 1 to 3 (a `carry` at a hand is drawn; of the King's writs some become answerable
  and some do not across ten seeds; with both Ministries seats vacated the season completes and every
  King's writ returns by the clock); BYZ-D gates 2 and 3 (the Doux's entry rate differs between two arms
  that differ only in his stance toward a person in the realm); COL-B's border gate (after CR-29: no
  person at the foreign settlements holds an untold claim of a realm Event of that tick) and its
  M-ABROAD reading (at least two `force` bands across five seeds).
- **Planted failure:** delete `passes_through` from the court's row (the lag is zero); remove
  `hands_open` (no clerk is ever asked).
- **Cost:** small build plus content.

### I-6 — turnover (the keys EQUAL; the tally a mover)

- **Lands:** `15_INSTITUTIONS_VENICE_C` edits 1 to 7 (the tables and `selection: lot`; no fifth
  `conferral_bases` value); `15_INSTITUTIONS_PAPACY_A`; `15_INSTITUTIONS_PAPACY_B` items 1 to 4 (item 4,
  `head_of_faction`, is ruled: A-35) with the tally of audit X-15 and PAPACY-GROUNDING item 1's floor;
  `15_INSTITUTIONS_BYZANTINE_E` edit 4 (`acclamation`) and its audiences for `succeed`.
- **Gate:** VEN-C's rotating council on the spine (twelve seasons, three seeds: no holder inside his
  cooling-off, none off the list, the seeds do not seat the same sequence, the drawn name differs from
  the act's `to` at least once); PAP-B's election, two arms: **four hand-built electors** (three
  committed for against two for and two against, 200 seeds each: different outcome distributions,
  neither 0 nor 1, all three tally outcomes seen) and **the built realm's two electors**
  (`off_cardinal_justice`, `off_senior_inquisitor`; `quorum: 2`: the seat opens in some seeds and not
  all; with one elector's seat vacant, in none); PAP-B's `patronage` pair (the King's `confer` on a
  Cardinal's seat refused, the Confessor's admitted); PAP-B's strip (the Confessor's `revoke` of a
  Cardinal drawn and resistible; none of `off_confessor`); BYZ-E gate 1 (the Success-or-better rate
  with the title exceeds the rate without, and both fall at `presumption_gain` 0).
- **Planted failure:** the lot ignoring `may_seat`; a pass test that carries an election on zero
  ballots.
- **Cost:** small build. The ballot itself is SC's (`13_SC_draw_for_unrolled_contests.md`, B07): VEN-C's
  edit 8 is withdrawn into it.

### I-7 — sanction, audit and the calling-in (EQUAL until a matter is docketed or a writ issued)

- **Lands:** `15_INSTITUTIONS_SYNTHESIS_C`; `15_INSTITUTIONS_PAPACY_D` as reconciled (the forms in
  `instruments.yaml`; the decline reading `forborne`); `15_INSTITUTIONS_PAPACY_C` §2 (`consecration`,
  minting a certificate with `recites`); `15_INSTITUTIONS_COLONIAL_C` (rows `audit`, `quo_warranto`;
  `prescription_seasons`; the occasion `audits_due` under the key `audit_at_exit`).
- **Gate:** PAP-D's four (a sentence over 200 seeds gives all four bands; one fixed addressee both
  complies and defies across seeds, and the complying share rises with conviction; a vassal with a
  planted grievance releases more often than one without, neither always nor never; penance moves the
  `pardon` odds); COL-C's three (testimony moves an audit's bands; a grant's age moves a calling-in's;
  `distance` moves both); SYN-C's gates.
- **Planted failure:** make the decline unconditional on the answer; read a seized charter's age from the
  Record's creation instead of the citing party's hold.
- **Cost:** small build.

### I-8 — content (a mover per row)

- **Lands:** `15_INSTITUTIONS_VENICE_D` §1 to §4 (houses on a `{venue:}` anchor; the commune council;
  Schoenland's seats, bodies and `security_bench`; a held `staple` as a `proofs` level on `exchange`);
  `15_INSTITUTIONS_PAPACY_E` items 1 to 4 (sees, the tithe as a form, an exempt house, a legate); the
  forms `land_grant`, `march`, `charter`, `staple`, `wardship`, `capitulation` in seeded or case rows;
  the Altonian trade treaty as a seeded `staple`.
- **Gate:** each file's own (a see filled by one of two lawful conferrers at some seed; a tithe that
  moves stores only by a see-holder's own `requisition`; Schoenland's head answered by `faction_q.head`;
  a row with a `{venue:}` anchor seated on the named hearth).
- **Cost:** edit (content) and small build (the anchor form). Names are Jordan's; placeholders ship
  marked.

### I-9 — the playables (no game-path change)

- **Lands:** `15_INSTITUTIONS_SYNTHESIS_D` (the integrated scenario in three cuts, and the one report);
  the four standalones on FA's runner: `15_INSTITUTIONS_BYZANTINE_F` (`roga`, `chancery`),
  `15_INSTITUTIONS_PAPACY_F` (The Vacant Chair), `15_INSTITUTIONS_VENICE_D` §5 (The Counting-House),
  `15_INSTITUTIONS_COLONIAL_E` (The Farm of the Southern Tolls; The Katepano's Latitude).
- **Gate:** SYN-D's; each standalone's own; in every case `content_hash` of an all-NPC run equals
  `populated.run` on the same world after the same tick-0 acts.
- **Cost:** small build, harness only.

### I-10 — held (design-first)

Schism (`15_INSTITUTIONS_PAPACY_E` item 6; needs FA's emergent-faction carrier); the kin-bar (`15_INSTITUTIONS_VENICE.md` §6.3; needs
`02_CHAR_relations_have_a_ground.md` and `14_VERBS_SOCIAL2_D_tie.md`); unanimity on a bench;
`15_INSTITUTIONS_BYZANTINE.md` §12 batch G (a revenue grant that roots; the rule of avoidance; `forge`
of an instrument; `construe` at a hand), each of which is a counter-pressure and waits for a reading of
the pressure it counters.

Not held, and so not here: the council that would judge the Confessor (`15_INSTITUTIONS_PAPACY_E` item 5)
is **dropped** (A-36: nobody judges him; its procedure P-13 and the CR-37 strip motion go with it); the
head's discipline (`15_INSTITUTIONS_PAPACY_B` item 4) is **ruled** and lands in I-6 (A-35); a `corvee`
form is **not built** (A-41: caste is carried by regard, vote blocks and informal tiers; the vote weight
lands with the councils, A-42, and the commons' heavy moves are A-56's, `U5d_SE_cohort_heavy_moves_and_caste.md`).

### The grounding plans (B40; their items land with the files they amend)

`15_INSTITUTIONS_PAPACY_grounding_mechanisms.md` (item 1 with PAP-B in I-6; items 2, 3 with PAP-D in
I-7; item 4 with PAP-E in I-8; items 5, 6 with I-9); `15_INSTITUTIONS_BYZANTINE_grounding_mechanisms.md`,
`15_INSTITUTIONS_COLONIAL_grounding_F_what_the_tree_adds.md` and
`15_INSTITUTIONS_VENICE_grounding_E_what_the_tree_adds.md` (each after its family's last file; content
and readings, with the small builds their own files name). Each gate is its file's.

## Dependency edges, by the lane that owns the other end

"Blocks" names the batch that cannot land before it; "feeds" names a batch that lands without it and is
thin until it arrives.

| other lane's proposal or plan position | edge |
|---|---|
| `05_SC_obstacle_difficulty_and_modifiers_B.md` | blocks I-2 (the roster and the composer), and through it every drawn row |
| `05_SC_contest_record_on_event.md` (SC-P1) | blocks I-2's gates (the term list on the Event) |
| `13_SC_tuning_tables.md` | blocks the `standard:` values of I-6 and I-7's rows; owns `stakes_ob` (`proof_step` is deleted: OBS §3's `proofs` levels) |
| `13_SC_draw_for_unrolled_contests.md` | blocks I-4 (`covenant`'s acceptance), I-5 (`carry`), I-6 (the ballot), I-7 (the appeal) |
| `13_SC_calibration.md` | the method by which every fixture in audit §3.6 leaves its first value |
| `05_SC_arrangement_rows_that_bind.md` (SC-P4) | blocks I-4 (`debt_suit`'s bands), I-7 (`audit`, `quo_warranto`, the sentence) |
| `05_SC_acquittal.md` (SC-P6) | blocks I-4 and I-7 (Failure as an acquittal and a quittance) |
| `05_SC_evidence_and_rebuttal_B.md`; `12_ARCS_cited_evidence.md`; `08_FI_05_evidence-interface_B.md` | blocks I-3 gate 5 and I-7 (a held Record cited; a certificate's weight; prescription; penance) |
| `05_SC_playable_hearing_B.md`; `05_SC_hearing_capabilities.md` | blocks I-7's realm reading and I-9 cut 2 (a computed docket that names a row) |
| `18_DETERMINISM_task_draw_for_uncontested_verbs.md` | blocks I-4 and I-5 (the task route for `requisition`, `transfer`, `carry`, `issue`; the `task_draw_arm` control) |
| `18_DETERMINISM_notice_is_a_draw.md` | feeds I-5 (what crosses a border is told, and telling is noticed by a draw) |
| `18_DETERMINISM_rival_acts_in_one_fold.md` | feeds I-6 (two `confer`s on one see in one season) |
| `18_DETERMINISM_no_certain_matchup.md` | feeds I-8 (the field a `march` or a `capitulation` turns on) |
| `14_VERBS_BINDING_A_formation.md` | blocks I-6 (`oblige` and `release` forming on what the actor owns), I-8 (`establish` of a see, a branch, a legation) |
| `14_VERBS_BINDING_B_sittings.md` | blocks I-7 (`pardon` as a draw; a judge asked about the parties before him) |
| `14_VERBS_BINDING_C_turnover.md` | blocks I-3 (`confer` on a dignity), I-6 (`confer`, `succeed`, `revoke`; `rank_gap`; `provisional_term`, its one fixture) |
| `14_VERBS_BINDING_D_orders.md` | blocks I-5 (`issue`'s `force`; the `command` basis), I-7 (publication) |
| `14_VERBS_BINDING_E_war_seats.md` | feeds I-8 (`capitulation`) |
| `14_VERBS_MATERIAL_B_stores.md` | blocks I-4 (`transfer`, `requisition`), I-8 (`exchange`) |
| `14_VERBS_MATERIAL_D_paper.md` | blocks I-5 and I-7 where a paper is seized, forged or surveyed |
| `14_VERBS_MATERIAL_A_mending.md`, `_C_works.md`, `_E_knowledge.md` | feed I-7 and I-8 (the services an `interdict` withholds; `found` as a `land_grant`'s due deed) |
| `14_VERBS_SOCIAL1_A_formation.md`, `14_VERBS_SOCIAL2_A_formation_on_what_is_known.md` | block I-1's `form` choice and every `covenant` and `petition` formation |
| `14_VERBS_SOCIAL1_B_documents_and_obedience.md` | blocks I-4 (`covenant_in_force`; `give` of a bond), I-7 (`comply`, `evade / defy`; `OBEYED_WRIT`) |
| `14_VERBS_SOCIAL1_D_grievance_and_settlement.md` | blocks I-5 (`carry`'s row, its `petition_venue` and `backlog`; this lane and `13_SC` state the row differently, audit X-25) |
| `14_VERBS_SOCIAL1_C_persuasion_and_deceit.md` | feeds I-2 (the ask's row) and I-6 (canvassing) |
| `audits/14_VERBS_SOCIAL2.md` §9 (`oblige` as an admission draw; proposal `14_VERBS_SOCIAL2_B`) | feeds I-6 (joining a roll: the warrant is eligibility, the admission is that lane's draw if Jordan takes it) |
| `14_VERBS_SOCIAL2_B_a_word_with_content.md` | blocks I-3 gate 4 (telling what a held certificate recites) |
| `14_VERBS_SOCIAL2_C_case_question_confession.md` | feeds I-7 (the inquisitorial rite) |
| `14_VERBS_SOCIAL2_D_tie.md` | blocks I-10's kin-bar |
| `14_VERBS_MILITARY_*`; `06_FA_levy_through_the_seat_B.md`; `06_FA_war_lives_in_seats_B.md` | feed I-8 and I-9 (the hired company; a revolt's field; the Katepano's march) |
| `14_VERBS_PHYSICAL_A_custody_and_force.md` | feeds I-7 (the warrant behind an arrest or a distraint) |
| `06_FA_decree_binds.md` | blocks I-5 and I-7 (the content deposit; the answers forming; `recalls`) |
| `06_FA_remit_grant_by_row.md` | blocks I-3, I-5, I-8 (a row's own remit; the Guild leader's and the Representative's rows) |
| `06_FA_seat_terms_and_turnover.md`; `06_FA_seat_terms_by_body_B.md` | block I-6 (`term`, so `cooling_off` and `audit_at_exit` have something to follow) and I-4's `farm` (a conferred seat's term) |
| `06_FA_office_capabilities.md` | blocks I-3's ranking of whom to honour; feeds every pool |
| `06_FA_playable_scenario.md`; `06_FA_shortest_loop_B.md` | block I-9 (`play`, `situation`, `digest`, `world="realm"`) |
| `07_SE_treasury_granary_B.md`; `07_SE_ground_and_granaries.md` | block I-4's seeded gates and I-9 (stores at seat rungs; places of unlike stock) |
| `10_DICE_capability_axiom_map.md`; `10_DICE_one_score_two_roles.md` | block SC-B's `opposition` and `capability` terms, and so I-2 |
| `10_DICE_one_roller_one_fraction_rule.md` | feeds I-4 (the fraction a magnitude row reads) |
| `10_DICE_believed_odds_have_a_prior.md` | feeds I-2 (what a person believes of `obligation` and `distance` before he asks) |
| `02_CHAR_which_ground_moves_whom.md`; `10_DICE_advantage_sources_for_the_arcs.md` | feed I-7 (conviction as leverage on an answer to a writ) |
| `02_CHAR_relations_have_a_ground.md`; `02_CHAR_scar_cap_and_regard_unit.md` | feed I-3 and I-6 (authored stance rows; the unit `reception` and `legitimacy` share) |
| `02_CHAR_goal_lean_on_its_own_question.md` | feeds every batch: whether anyone lends, pays, tells or audits is the chooser's |
| `02_CHAR_capability_definitions.md`; `02_CHAR_capability_uses_table.md`; `01_CORE_capability_authoring_surface.md` | feed the pools (`law`, `copying`; a steward's capability if Jordan wants one) |
| `01_CORE_claim_fade_as_read.md` | feeds I-3 (the fade the chain relies on) |
| `01_CORE_reason_trail_in_the_act_store.md`; `01_CORE_unmet_need_is_attended_first.md` | feed I-9's legibility and the attention a bill gets |
| `12_ARCS_case_on_the_realm.md` | blocks I-3 (prehistory through the fold) and I-9 (a case as a delta) |
| `09_WR_B_weather_with_memory_and_the_year.md` | feeds every yearly number (audit §7.4) and the tax revolt |
| `20_NARRATIVE_A_stands_for.md` | feeds I-3 (whom a hearer credits when a keeper tells) |
| CR-29 | blocks I-5's border and reach rows |
| CR-35, CR-36 | block I-6 (an elected seat filled by its bench; the `resolution` Record and its disposal site); CR-36's kind row blocks I-3's seeded consecration |
| CR-37 | none (its use here, the strip of the Confessor, is dropped by A-36) |
| CR-60, CR-61 | block I-7 (a bench that judges where it does not act; a docket item that names its row) |
| CR-74 | feeds I-7 (the CH reading) |
| CR-88 | feeds I-6 and I-7 (why a vacancy is filled; the duty decline a sanction lifts) |
| CP-T09-03, CP-T09-08, CP-T08-07 | feed I-5 and I-8 (a covenant something reads; `dispatch` that sends; the standing levy) |

No cycle: every edge runs from an other-lane item to a batch, or from a lower-numbered batch to a
higher one, except I-5 and I-6, which are independent of each other.

## Where each family proposal lands

| file | batch |
|---|---|
| BYZ-A | I-1 (keys), I-3 |
| BYZ-B | I-1 (key), I-4 |
| BYZ-C | I-1 (keys), I-5 |
| BYZ-D | I-5 |
| BYZ-E | I-6 (the row; the audiences); its two verb rows are the BINDING lane's |
| BYZ-F | I-9 |
| PAP-A | I-6 |
| PAP-B | I-1 (roster, table), I-6 (with item 4, A-35) |
| PAP-C | I-3 (seeded rows, as reconciled), I-7 (`consecration`) |
| PAP-D | I-7 |
| PAP-E | I-8; item 6 in I-10; item 5 dropped (A-36) |
| PAP-F | I-9 |
| VEN-A | I-2 |
| VEN-B | I-1 (kind), I-4 |
| VEN-C | I-1 (keys, rosters), I-6 |
| VEN-D | I-1 (anchor), I-8, I-9 |
| COL-A | I-1, I-4 |
| COL-B | I-2 (§1), I-5 (§2 to §5) |
| COL-C | I-7 |
| COL-D | I-3 |
| COL-E | I-9 |
| BYZ-G, COL-F, PAP-G, VEN-E (the grounding plans) | per item, as above; listed in B40 |

## Gate for the plan as a whole

`15_INSTITUTIONS_SYNTHESIS_D`'s: the integrated scenario's three cuts, each with its control and its
planted failure, and its gate 8 (A-80: with every position held, the world still produces acts that cite
the institutions). A plan whose batches each pass and whose integrated scenario shows one ending at every
seed has built institutions that sit beside each other.

## Falsifier

Two batches that write the same fact in two files. A batch whose gate can pass with its predecessor
reverted (the edge was not real). The integrated scenario reaching the same ending at every seed with
the rolls unpinned.

## NERS reading

- **N.** Without one order the four family plans land three founding carriers and two audits.
- **R.** Each batch after I-1 ends in something a player-proxy can do that it could not before.
- **S.** One registry lands once; each verb row is touched by its owner; every gate is a seeded run with
  a control.
- **E, last.** Ten batches for the twenty-five proposals (twenty-one family files and the lane's A to D)
  and this plan, four of them harness-only; the four grounding plans ride inside them (C3-N21).

## Cost class

The plan itself: none. Its batches: one edit-and-small-build of owners; eight small builds; one batch of
content; one held batch that is design-first.
