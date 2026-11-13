# U5d — findings closure: FA, SE, WR, GO, institutions, ARCS, narrative churn, procedural generation, happenings, determinism, the remaining pessimist scopes, story enablement

## Status: REFERENCE (a closure table for the suite; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: 4ae20f0 (working tree), 2026-11-12. Lane: U5d, a Fable unification-closure lane (UNIFICATION_BRIEF.md, "Closure rule").

Every row closes one finding, resolution row, survivor, census-style row or decision of the documents this
family owns, with exactly one disposition:

| code | meaning |
|---|---|
| **RESOLVED-BY** | a proposal in `proposals/` carries the exact edit at the single owner and a gate (file and section named) |
| **SUPERSEDED** | a later finding, a reconciliation or one of Jordan's answers (`unified/DECISIONS_ANSWERED.md`, `A-n`) replaces it (cited) |
| **STALE-FALSE-POSITIVE** | the audit's own later evidence, or the tree at HEAD, shows the finding does not hold |
| **DISPUTED** | this lane's evidence is against it; the finding stays in its document, marked |
| **JORDAN** | survives the five-step ladder (CLAUDE.md §0); two options stated in the row |

**Resolve is a plan, not an edit** (the brief). Nothing here was executed against code, a registry or
canon; nothing was run under pytest. A carrying proposal is an ordered set of instructions for a later
implementation lane. Where a finding had no carrying proposal this lane wrote one under
`proposals/U5d_*.md` (listed below).

**Jordan's answers govern.** `unified/DECISIONS_ANSWERED.md` (A-1 to A-56 and the ladder-closed table)
supersedes any lane document. A proposal built on the other answer carries a `Reconciled: 2026-11-12, U5d
closure` head line naming the ruling and the steps rewritten; its author's line is kept and no finding is
deleted. The reconciliations are listed in **Part R** at the end, one row per file.

**Reading the tables.** "Carrier" names a file under `proposals/` of this suite unless a path is given;
"§" is that file's own section or edit number. "Evidence" is the audit's own citation as read by this
lane. A row marked `[not re-opened]` cites evidence this lane did not open at the code; a row marked
`[unverified]` rests on a claim this lane could not ground. Rows whose subject another family closes are
closed here as SUPERSEDED with the owning closure named (`U5a`, `U5b`, `U5c`), never twice.

**Abbreviations.** `es/` = `engine/season/`. "plan" = a position of the active master workplan, cited by
id. `A-n` = an answer in `unified/DECISIONS_ANSWERED.md`. `D-n` = a row of
`unified/DECISIONS_FOR_JORDAN.md` (closed by `A-n` or by the ladder-closed table).

---

# Part 1 — FA (factions, governance, offices, war and diplomacy)

Carriers: **DECREE** = `06_FA_decree_binds.md`; **REMIT** = `06_FA_remit_grant_by_row.md`; **TERMS** =
`06_FA_seat_terms_and_turnover.md`; **TERMS-B** = `06_FA_seat_terms_by_body_B.md`; **SCEN** =
`06_FA_playable_scenario.md`; **LOOP-B** = `06_FA_shortest_loop_B.md`; **HYG** = `06_FA_hygiene.md`;
**CAPS-FA** = `06_FA_office_capabilities.md`; **WAR-B** = `06_FA_war_lives_in_seats_B.md`; **LEVY-B** =
`06_FA_levy_through_the_seat_B.md`; **PES-FA-A/B/C** = `16_PESSIMIST_FA_A…C_*.md`; **VB-C/D/E** =
`14_VERBS_BINDING_C_turnover.md`, `_D_orders.md`, `_E_war_seats.md` (U5c closes the verb verdicts; cited
here as the owner of a band row); **OWED-FA** = `U5d_FA_owed_edits.md` (written by this lane: the FA
rows decided "in this table" with no file, and the edits Jordan's answers A-19, A-22, A-23, A-35 and A-36
now order); **LAND** = `U5d_FA_land_and_seats_pass_on_a_won_march.md` (written by this lane on the land rulings A-57, A-58 and A-65 to A-70).

## 1.1 `audits/06_FA_audit.md` — findings

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| F-FA-01 | a decree binds nobody and reaches nobody as a writ | RESOLVED-BY | DECREE edits 1–5 as reconciled (A-21: proclaimed is ruled, so edit 1 loses its `[ASSUMPTION]`; A-22: the addressee set an order binds is the command basis, OWED-FA §2) | realm seeds 0–2: 29, 21, 41 writs, 0 answered; `comply` 0 of 33 (audit E-3, E-5) |
| F-FA-02 | power does not change hands in computed play | RESOLVED-BY | TERMS edits 1–5 (the term on the row); TERMS-B (which rows); DECREE edit 5 (`revoke` reads its office); VB-C (the drawn `confer`, `revoke`, `succeed`); natural death on (A-15) through `22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn.md` as reconciled | `confer` formed 5, attempted 0; `succession.claimed` 0 (E-3, E-5) |
| F-FA-03 | the military verbs are open to clerks by an unruled placeholder | RESOLVED-BY | REMIT edits 1–4 | 26 of 33 seats may `march` (E-3) |
| F-FA-04 | war has no producer and draws no response | RESOLVED-BY | plan CP-T09-02 (`declare`) with WAR-B edits 1–5 as reconciled (A-20) and VB-E; corrected in part by addendum C-1 (the producer exists by `utter`/`commit`) | `at_war` false at every seed; `tests/test_faction_q.py:223-262` (C-1) |
| F-FA-05 | an officer's choices do not read his office | RESOLVED-BY | CAPS-FA edits 3–4 as reconciled (A-12: the seat's modifier may now reach the roll, not only the conferee ranking); plan CR-88 for duty | `decision/choose.py` reads no seat (audit §15) |
| F-FA-06 | orders and sittings are announcements | RESOLVED-BY | DECREE (orders); OWED-FA §5 (what an order orders, R-27); sittings are SC's (`05_SC_playable_hearing_B.md`, closed by U5c) | H-260; `determine` 0, 1, 0 (E-5) |
| F-FA-07 | no FA scenario, digest or end condition | RESOLVED-BY | SCEN; LOOP-B (A-10 confirms the form: a scenario on the season loop, no module) | `harness/governance_spine.py` prints a census only |
| F-FA-08 | a malformed term and two live holders end the season instead of refusing | RESOLVED-BY | TERMS edit 2 (`_req_confer` refuses a malformed term); H-133 stays registered, unreached by any builder | `effects_governance.py:50-54` `[not re-opened]` |
| F-FA-09 | the contract file describes a faction the code retired | RESOLVED-BY | HYG item 5 (R-09) | `module_contracts.yaml:127, :797` `[not re-opened]` |
| F-FA-10 | unreached query surface in `faction_q` | RESOLVED-BY | HYG item 3 (R-10) | audit E-9 |
| F-FA-11 | `dispensation` and `oblige` say the opposite of what they do | RESOLVED-BY | HYG item 4 (R-11, R-12); declared hash mover | H-262, H-298 |
| F-FA-12 | H-230 and H-206 describe a tree that no longer exists | RESOLVED-BY | HYG item 1 (R-13) | `_eff_succeed`, `successions`, `death_subjects` in the tree |

## 1.2 `audits/06_FA_audit.md` §6.1 — hole-register and workplan rows

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| H-21, H-41, H-99, H-100 | listed open; verified closed | STALE-FALSE-POSITIVE | none owed (H-352 carries H-21's residue) | `effects_governance.py:538-544`; `office.established` 1 (E-5); `REVOCATION_DISPOSAL` |
| H-70, H-156, H-161, H-163, H-281, H-297 | open; another lane's (CHAR, CORE, SC) | SUPERSEDED | the owning closures (U5a for H-70, H-156; U5c for H-161, H-163, H-281, H-297) | audit §6.1 "cross-listed" |
| H-90 | ladder and purview built; Parliament and delegation unbuilt | RESOLVED-BY | plan CR-35 to CR-37, IN-48; the vote's form is ruled (A-14: a draw on the voter inside the presiding act) and its first reader is the kit's council (`15_INSTITUTIONS_VENICE_C_roll_lot_ballot.md`) | — |
| H-91 | `remit:revoke` beside purview | STALE-FALSE-POSITIVE | closed by precedent (R-05); OWED-FA §7 re-grades the row | `gate.py:370-375` `[not re-opened]` |
| H-108 | delegation without a hold reverted | SUPERSEDED | A-10 (governance is the loop's own verbs) leaves IN-48 the owner; A-22 fixes whom a seat commands | — |
| H-133 | two live holders on one office | RESOLVED-BY | none owed: stays registered (F-FA-08); no builder produces the state | — |
| H-144 | measured; verified closed | STALE-FALSE-POSITIVE | OWED-FA §7 re-grades the row | `predicates.py:403-410` |
| H-101 | closed at office scale by assumption | RESOLVED-BY | plan CR-09 (the set form) | `gate.py:422-461` |
| H-158 | no computed act pays upkeep | RESOLVED-BY | `07_SE_population_census.md` (men under arms do not `work`, R-31); `04_MB_campaign_party_economy.md` (U5b) | not re-measured by the audit |
| H-206, H-230 | stale heads | RESOLVED-BY | HYG item 1 | `gate.py:1819-1832` |
| H-207 | `confer` formed, never attempted | RESOLVED-BY | TERMS (vacancies on a clock) and CAPS-FA edit 4 (the conferee is ranked) | E-3 |
| H-252 | which clause refused | RESOLVED-BY | HYG item 2 (R-14) | E-3 |
| H-260 | obeying and defying change nothing | RESOLVED-BY | DECREE edit 4 | measured on hand-placed writs |
| H-262, H-298 | names | RESOLVED-BY | HYG item 4 | — |
| H-290 | a malformed term raises | RESOLVED-BY | TERMS edit 2 | — |
| H-292, H-217 | elected seats fill by plain `confer`; no `succession` row | RESOLVED-BY | plan CR-35 with the kit's election (`15_INSTITUTIONS_PAPACY_B_patronage_election_discipline.md` items 1–3; `15_INSTITUTIONS_VENICE_C_roll_lot_ballot.md`), each ballot a draw on the voter (A-14) | `FILLED_BY["elected"]` is `{conferral}` |
| H-294 | a ban bars openings only, everywhere | RESOLVED-BY | TERMS edit 6 (R-06: scoped to the banning seat's purview) | — |
| H-352 | one purse per rung | RESOLVED-BY | OWED-FA §6 (R-07: the `treasury:` anchor, built when reached); `07_SE_treasury_granary_B.md` owns the store | `requisition.taken` 0, 1, 6 (E-5) |
| H-353 | a seat's faction and a holder's membership are two records | STALE-FALSE-POSITIVE | none owed (R-08: leave them two; `world_q.leaders`' docstring) | — |
| CP-T09-01 to -09, CR-09, CR-32, CR-35 to CR-37, FA-01 | planned, unbuilt | RESOLVED-BY | the plan positions; one clause each from WAR-B edits 5–6 | no `declare`, `retain`, `conspire` row (E-2) |
| CP-T09-06 | the card misstates the present value | RESOLVED-BY | PES-FA-A edit 1 (`null → inheritance` and the `successions` row) as reconciled (A-19) | `offices.yaml:206` |
| CR-54 | no design file | RESOLVED-BY | DECREE §4 and edit 5 | — |
| CR-88, CR-89, CR-91 | B10-17b unbuilt | RESOLVED-BY | the plan positions; CR-89's clocks open scenes and decide nothing (A-47) | — |
| FA-03, FA-07 | held, leave | RESOLVED-BY | none owed (reference) | — |
| `HANDOFF_FA.md` row 3 | orders authoring into `.designs/` | RESOLVED-BY | HYG item 6 (R-15) | — |

## 1.3 `audits/06_FA_audit.md` §6.2 — resolutions R-01 to R-21; §11 survivors

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| R-01 | a writ reaches no addressee | RESOLVED-BY | DECREE edits 1–3 (A-21) | — |
| R-02 | obeying and defying change nothing | RESOLVED-BY | DECREE edit 4; the recall threshold opens the issuer's question and decides nothing (A-47, A-24) | ED-IN-0046, ED-IN-0047 `[ledger rows not re-opened]` |
| R-03 | `revoke` has no motive and reads no subject | RESOLVED-BY | DECREE edit 5 | — |
| R-04 | which seats hold `dispatch` | RESOLVED-BY | REMIT edits 1–3 | — |
| R-05 | is `remit:revoke` necessary | RESOLVED-BY | OWED-FA §7 (no code edit; the register row re-graded) | — |
| R-06 | a ban's scope and reach | RESOLVED-BY | TERMS edit 6 | — |
| R-07 | one purse per rung | RESOLVED-BY | OWED-FA §6 | — |
| R-08 | faction of seat against membership of holder | RESOLVED-BY | none owed (leave two); PES-FA-B edit 3 adds admission to joining | — |
| R-09, R-10, R-11, R-12, R-13, R-14, R-15 | hygiene rows | RESOLVED-BY | HYG items 5, 3, 4, 4, 1, 2, 6 | — |
| R-16 | the queen consort holds the King's remit | RESOLVED-BY | REMIT edit 4 as reconciled: it lands with A-19's deed race so the throne is not stranded (F-PES-FA-11); OWED-FA §1 | NPC-032 |
| R-17 | no computed act declares a term | RESOLVED-BY | TERMS edit 1 | — |
| R-18 | CP-T09-06's card | RESOLVED-BY | PES-FA-A edit 1 | — |
| R-19 | no scenario, digest or end | RESOLVED-BY | SCEN; LOOP-B | — |
| R-20 | "registered module" against a subsystem with no verbs of its own | SUPERSEDED | A-10: the loop's own verbs; no governance module | — |
| R-21 | Church and Löwenritter seats strippable by nobody | SUPERSEDED | A-35 (the head strips an officer by a resistible draw; Löwenritter unstrippable until a head seat exists) and A-36 (nobody judges the Confessor); carrier `15_INSTITUTIONS_PAPACY_B_patronage_election_discipline.md` item 4 as reconciled (un-held) with VB-C's `revoke` draw; OWED-FA §3 | 2026-10-11 `revocation: null` |
| §11 item 1 | is a decree public or paper | SUPERSEDED | A-21 (proclaimed); DECREE as written | — |
| §11 item 2 | the standing requirement against Layer 1 for FA | SUPERSEDED | A-10 | — |
| §11 item 3 | seats nobody can strip | SUPERSEDED | A-35, A-36 (as R-21) | — |

## 1.4 `audits/06_FA_audit.md` §13 (provided arcs and characters), §14, §15

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| NPC-083, NPC-038 (warrant), ARC-17, ARC-04 | orders answered; the superior responds | RESOLVED-BY | DECREE | E-3, E-5 |
| NPC-083 (methods handing influence to internal factions) | no method operand | SUPERSEDED | SE's closure (Part 2: `07_SE_capability_and_chooser_surface.md`) | — |
| NPC-008 (an office makes reform harder by being held) | "wrongly stated against the architecture" | SUPERSEDED | A-12: a seat may carry a modifier; the need stands as stated and is carried by CAPS-FA as reconciled (the seat's modifier term) and plan CR-36 | `04` §B.7 (to be amended on A-12; text owed, not applied) |
| NPC-008 (refill), NPC-070, NPC-006, NPC-009 | who is next in the chain | RESOLVED-BY | TERMS; TERMS-B | — |
| NPC-038, NPC-004, NPC-070 (removal) | removable only by death | SUPERSEDED | A-35 (as R-21) | — |
| NPC-020 (acts in his name diverge), NPC-089, NPC-090, ARC-45, NPC-012 | `dispatch` that sends; demand; treaty | RESOLVED-BY | plan CP-T09-08, CP-T09-02, CP-T09-03, FA-01 | — |
| NPC-020, NPC-070 (an army reassesses its loyalty) | carrier yes, behaviour no | RESOLVED-BY | plan CR-88; the Split is a strife move (A-46) | — |
| NPC-020, NPC-031 (heir; the throne by claim) | claim unobserved | RESOLVED-BY | SCEN (`succession` situation); `22_HAPPENINGS_B_the_throne_is_never_stranded.md` as reconciled (A-19) | E-6 |
| NPC-020, NPC-050, NPC-081, NPC-052 | contested succession; election | RESOLVED-BY | plan CR-35; A-19 (the deed race); A-14 (the vote) | H-217, H-292 |
| NPC-050 (campaign toward a higher seat), ARC-40 | claims, deposition, clocks | RESOLVED-BY | plan CR-91, CR-37, CR-89, restated as "a threshold opens a mandatory scene" (A-47) | — |
| NPC-032 | a consort with standing and no action economy | RESOLVED-BY | REMIT edit 4 (as R-16) | `aperture 2 0` |
| NPC-003, NPC-041 | a leader with influence before any seat | RESOLVED-BY | plan IN-30, CR-39 | — |
| NPC-036, NPC-072, NPC-082, NPC-034 | a command post matters | RESOLVED-BY | REMIT | E-3 |
| NPC-037, NPC-013 | a treasury post moves resources | RESOLVED-BY | OWED-FA §6 | E-5 |
| NPC-073, NPC-074, NPC-084, ARC-R18 | a council seat casts a position; a vote neither side wins | SUPERSEDED | SC's closure (U5c); the vote is A-14 | — |
| ARC-01, ARC-03 | a quantity that moves from the absence of any act ("wrongly stated against a ruling") | RESOLVED-BY | restated on events that mark inaction (the audit's own restatement); plan CR-89 | ED-IN-0345 `[ledger row not re-opened]` |
| fourteen UNCLEAR needs (NPC-071, -034 to -037, -039, -041, -072 to -074, -081, -082, -084, -085) | content debts on `npc_registry.yaml` and `offices.yaml` | RESOLVED-BY | REMIT edit 3 (rows for unauthored seats); the generated cast (A-44, `21_PROCEDURAL_B_cast_and_seats.md`) authors the rest | E-8 |
| §14 (capability surface), §15 (chooser surface) | whom to seat reads nothing about the candidate | RESOLVED-BY | CAPS-FA; `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` owns the home | audit §14 table |

## 1.5 `audits/06_FA_audit_addendum_B.md`

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| C-1 | F-FA-04's "no producer" is true only of computed play | RESOLVED-BY | corrected in the addendum; no edit owed | `tests/test_faction_q.py:223-262` |
| C-2 | `marshal`, `surrender` and the army verbs are withheld by a fixture | RESOLVED-BY | MB's step 5 lifts the withholding (U5b); LEVY-B lands first | `data/fixtures.py:1157` |
| C-3 | the FA→MB interface was understated | RESOLVED-BY | corrected in the addendum §B4.2; `04_MB_campaign_party_economy.md` (U5b) | — |
| C-4, C-5, C-8 | corrections of reading | RESOLVED-BY | corrected in the addendum; no edit owed | E-B1, E-B6, E-B7 |
| C-7 | nothing a battle decides is read back by a governance verb (a Layer 1 shortfall) | RESOLVED-BY | LAND (as F-FA-13) | `10_FACTIONS_AND_DEPLOYMENT.md:90` |
| C-6 | eight `elected` rows at `term: 8` do not fit the design | RESOLVED-BY | TERMS-B (three rows; life seats `null`), which supersedes TERMS's first authoring in content | E-B2 |
| F-FA-13 | a defeat costs bodies and never a holding or a seat | RESOLVED-BY | **LAND** (`U5d_FA_land_and_seats_pass_on_a_won_march.md`, written by this lane on A-57, A-58 and A-65 to A-70: the field writes presence; a victor standing on another's land chooses to seize, occupy or withdraw; a seizure carries the seats anchored on the place; on a draw both armies are back at their stations; an unopposed entry is read by a draw as trespass or aggression); WAR-B edit 6 as reconciled (the occasion on which the taking is offered) | `architecture/meta/10_FACTIONS_AND_DEPLOYMENT.md:90`; `loop/effects_combat.py::_eff_march` ("PRESENCE, NOT TITLE", opened) |
| F-FA-14 | under the planned `at_war`, one committer keeps two factions at war | RESOLVED-BY | WAR-B edits 1–4 as reconciled: A-20 rules (B), so the "lands only on that ruling" hold is lifted | `04:460` |
| F-FA-15 | men are levied by whoever minted a paper | RESOLVED-BY | LEVY-B as reconciled (A-22: the cohort is "the unseated in its land") | E-B3 |
| F-FA-16 | five of ten factions have no head; one has no members | RESOLVED-BY | TERMS-B edit 4 (two heads); the Guilds headless by design; R-34 (`faction x` excluded by name) | E-B2 |
| F-FA-17 | at tick 0 no rung holds a store | RESOLVED-BY | `07_SE_treasury_granary_B.md`; the seeded start draws bounded stores (A-50, `21_PROCEDURAL_D_world_cards_and_churn.md`) | addendum E-B1 |
| F-FA-18 | what an order orders exists only as prose | RESOLVED-BY | OWED-FA §5 (R-27: a closed set of term shapes, built after an answered writ is observed); VB-D owns the row | H-44 |
| R-22 | Layer 1's battle roster names stakes the code does not pass ("keep β: a field writes presence") | RESOLVED-BY | β is ruled for the field's write (A-66); the stakes are met by the victor's choice: LAND edits 1–3 (a seizure passes holdings and seats, A-58) and WAR-B edit 6 | `_eff_march`'s own tag ("revert: Jordan states α") is discharged as ruled, not reverted |
| R-23 | whose edge a war is | RESOLVED-BY | WAR-B (A-20) | — |
| R-24 | men by a Record's holder, stores by a seat | RESOLVED-BY | LEVY-B | — |
| R-25, R-26 | heads; which seats take a term | RESOLVED-BY | TERMS-B | — |
| R-27 | what a writ may order | RESOLVED-BY | OWED-FA §5 | — |
| R-28 | nothing between "no act" and "march" | RESOLVED-BY | plan CP-T09-03 (`covenant` as the instrument); no new verb | — |
| R-29 | faction weight has no reading | RESOLVED-BY | OWED-FA §4 as amended by A-42: `faction_q.weight` reads the authored territory/caste weight (franchise) | — |
| R-30 | who owns a split realm | RESOLVED-BY | none owed until a contested succession executes; the Split is A-46's | — |
| R-31 | an army in being costs nothing | RESOLVED-BY | `07_SE_population_census.md` (cross-listed) | — |
| R-32 | may `at_war` reach a verb's `requires` | RESOLVED-BY | WAR-B edit 7 (a) (no; an outcome Query) | — |
| R-33, R-34 | NPC-089's rung; `faction x` | RESOLVED-BY | none owed (statements) | — |
| §B6.2 item 1 | whose word ends a war | SUPERSEDED | A-20 (the seats that wage it) | — |
| §B6.2 item 2 | franchise | SUPERSEDED | A-42 (authored as the vote-block carrier); OWED-FA §4 | — |
| §B8.2 (old findings re-verified; what transfers) | reading account | RESOLVED-BY | no edit owed; the transfers are carried by the kit (Part 5) | — |

## 1.6 `audits/16_PESSIMIST_FA.md`

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| F-PES-FA-01 | a vacant seat is filled by the Crown or by nobody | RESOLVED-BY | PES-FA-B edits 1–2; VB-C; the election arms; the crown's fallback is ruled (A-19) and carried by `22_HAPPENINGS_B_the_throne_is_never_stranded.md` as reconciled | `pf1_static.py 0`; `pf2_premise.py 0` P2 |
| F-PES-FA-02 | the power to dismiss is one unfillable seat; the ban cannot be undone; a detained officer governs | RESOLVED-BY | PES-FA-A edits 1–3; the detained officer: OWED-FA §2 (A-23: custody suspends acts through the seat) | `pf2b` §1, §4, §5 |
| F-PES-FA-03 | "under the seat" is where a person sleeps | RESOLVED-BY | PES-FA-C as reconciled (A-22: the predicate is the command basis: sworn men, holders of seats it may revoke, the unseated in its land; a writ to a superior is a petition) | 18 of 34 seat-holders off their ground |
| F-PES-FA-04 | a faction cannot refuse a member; the governed are in none | RESOLVED-BY | PES-FA-B edit 3; the governed: `U5d_SE_cohort_heavy_moves_and_caste.md` (A-56) | `pf2` P4; `pf3_cut.py 0 2` |
| F-PES-FA-05 | anyone declares war for anyone | RESOLVED-BY | PES-FA-B edit 4 with WAR-B (A-20) | `pf2` P3 |
| F-PES-FA-06 | royalty by noble conquest is not in the engine | RESOLVED-BY | `15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger.md` (the seeded deeds), on A-17/A-18 (the south fought, ranked third; Varfell's deed realm-wide at the third confidence) | grep and `pf1` (c) |
| F-PES-FA-07 | offices are free to cut | RESOLVED-BY | none of its own (a measure): the NO_SEATS arm is the gate of DECREE, TERMS and PES-FA-A–C (it must differ from SHIPPED by more than DRAW2) | `pf3_cut.py 0 2 NO_SEATS` |
| F-PES-FA-08 | two heads for one faction | RESOLVED-BY | OWED-FA §8 (`opinion_of` reads `faction_q.head` first) | `pf5_heads.py` |
| F-PES-FA-09 | a dead ruler's decrees are orphan paper | RESOLVED-BY | OWED-FA §9 (a writ is the seat's; its `hold` passes with the seat) | `pf2` P1.5, P1.7 |
| F-PES-FA-10 | the governance record does not carry its reasons | RESOLVED-BY | OWED-FA §5; `01_CORE_reason_trail_in_the_act_store.md` (U5a) | audit §3.4 |
| F-PES-FA-11 | R-16 strands the throne one death earlier | RESOLVED-BY | as R-16: lands with A-19's race | `pf1`, `pf2b` §7 |
| F-PES-FA-12 | single-seed verb counts are one draw from a wide spread | RESOLVED-BY | none owed (a caution); gates in this family read at ≥ 2 dice seeds | `oblige` 26 → 0 |
| §4.1 | fixed outcomes in FA's code | RESOLVED-BY | VB-C (the draws); PES-FA-B edit 2 prices, never forbids | `18_DETERMINISM_SWEEP.md` C-07, C-11 |
| §5 item | when the royal line fails, who may take the crown | SUPERSEDED | A-19 (the deed race) | — |

---

# Part 2 — SE (settlements, territory, economy)

Carriers: **GROUND** = `07_SE_ground_and_granaries.md`; **TREAS-B** = `07_SE_treasury_granary_B.md`;
**CENSUS** = `07_SE_population_census.md`; **REGROW-B** = `07_SE_population_regrowth_B.md`; **KERN-SE** =
`07_SE_kernel_repairs.md`; **ARCN** = `07_SE_arc_needs.md`; **SUPPLY** =
`07_SE_campaign_supply_and_muster.md`; **CAPS-SE** = `07_SE_capability_and_chooser_surface.md`;
**RATE-B** = `07_SE_capability_rate_B.md`; **VALLEY** = `07_SE_valley_scenario.md`; **PES-SE-A/B** =
`16_PESSIMIST_SE_A…B_*.md`; **DRAWS** = `09_WR_B_draws_not_thresholds.md`; **LAPSE** =
`23_STORY_C_a_founded_place_can_fail.md`; **OWED-SE** = `U5d_SE_owed_edits.md` and **COHORT** =
`U5d_SE_cohort_heavy_moves_and_caste.md` (both written by this lane).

## 2.1 `audits/07_SE_audit.md` — findings

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| F-SE-01 | every settlement is the same economic object | RESOLVED-BY | GROUND (endowment by territory, R-SE-01) as annotated by the addendum's P-1 to P-6 | `se_bind.py`; 8 of 37 settlements in no polygon |
| F-SE-02 | population is a constant that can only fall, falls whole, and its loss is invisible | RESOLVED-BY | CENSUS §4 (thinning, R-SE-04 to -06) and REGROW-B (the rising arm) | `subsist.py:72` `[not re-opened]` |
| F-SE-03 | the realm's only hunger event is a world-gen artefact, and a test pins it | RESOLVED-BY | GROUND (stocked larders, R-SE-02) as reconciled: the starting stock is drawn within bounds (A-50) | the audit's §1.4 control table |
| F-SE-04 | relief is one act, one kind, once | RESOLVED-BY | GROUND §4 d (the remainder walk, R-SE-11); TREAS-B (the stock at the seat rung); PES-SE-A edit 1 (a short rung is shared) | `harness/scarce.py` |
| F-SE-05 | the fabric's raising arm does not reach in play | RESOLVED-BY | OWED-SE §1 (the reading added to H-105's and H-171's cites; cause not isolated, so no code edit is planned until it is) | `restore` 0 attempts, seed 0, three seasons |
| F-SE-06 | the geography feeds the battlefield and nothing else | RESOLVED-BY | TREAS-B (the granary's reach is the first reader); `09_WR_B_weather_with_memory_and_the_year.md` edit 3 (a leg's price) and `16_PESSIMIST_WR_A_the_road_is_drawn.md` (the road); the rest design-first (audit §8 step 7) | 55 settlement edges, 26 territory edges, an 11-row cost matrix unread |
| F-SE-07 | what persons do to the economy is nil in size and partly a sink | RESOLVED-BY | ARCN §3 b (amount as a choice, R-SE-24); OWED-SE §2 (CR-49's class on `transfer`, `migrate`) | `default_transfer_amount=1` (`fixtures.py:625`) |
| F-SE-08 | 248 of 322 `condition.worn` Events report a wear that did not happen | RESOLVED-BY | KERN-SE §3 (R-SE-08) | the audit's count |
| F-SE-09 | capacity acts as noise and migration as churn | RESOLVED-BY | OWED-SE §2 (CR-49's class for `migrate`'s `to`); CENSUS (weight gains a writer); COHORT (`migrate` is one of the cohort's heavy moves, A-56) | `aperture 3 0`: 16 migrations |
| F-SE-10 | a store move accepts a negative, zero or fractional amount | RESOLVED-BY | KERN-SE §2 (R-SE-07) | `effects_shared.py:120-136` |
| F-SE-11 | a move to where the mover stands publishes as travel | RESOLVED-BY | KERN-SE §4 (R-SE-09) | 14 of 15 executed moves same-place |
| F-SE-12 | the world never grows | SUPERSEDED | A-55 (fixed map); households within settlements are founded and may lapse (LAPSE); the producer of `build` candidates is IN-45's content | `found` 0 of 7, `build` 0 of 4 |
| F-SE-13 | there is no settlement scenario to play | RESOLVED-BY | VALLEY (with the addendum's P-13 change) | audit §9 |
| F-SE-14 | the people of a town act as one individual | RESOLVED-BY | COHORT (A-56: a cohort forms only the heavy moves) | 708 of 1,529 resolved acts at seed 0 are cohorts' |
| F-SE-15 | a season's cost grew with the tick in every arm run | DISPUTED | none: the audit itself marks the reading load-confounded and names no cause; this lane has no measurement either way, so it stays a caution and no edit is planned | audit §3 (`[not re-measured]`) |
| F-SE-16 | the instruments cannot see the economy's loops | RESOLVED-BY | none owed (CLAUDE.md §0.1 pt 5: no instrument over an instrument); each SE proposal's gate names its own reading | — |

## 2.2 `audits/07_SE_audit.md` §6.1, §6.2, §11, §13

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| H-105, H-171 | cite `restore` executing in the realm | RESOLVED-BY | OWED-SE §1 (R-SE-16) | F-SE-05 |
| H-140, H-306, H-327 | same-place move; amounts; arrival teaches nothing | RESOLVED-BY | KERN-SE §4, §2, §5 | — |
| H-149, CP-T08-09 | ruled and enforced; withdrawn | STALE-FALSE-POSITIVE | none owed | `test_march.py` |
| H-166 | who holds an unheld place | RESOLVED-BY | `09_WR_world_motion.md` edit 2 as reconciled (unheld land is taken by occupation; ground no party holds is outside A-57/A-58) | `effects_founding.py:51-89,170` |
| H-236 | the lattice has no source (filed under SE by path) | SUPERSEDED | WR's (Part 3: `09_WR_world_motion.md` edit 1; A-40 makes the wear a real condition of places) | T15 holds no Site |
| H-241 | `field_provisioning` built, shipped off | RESOLVED-BY | SUPPLY; PES-SE-B edit 4 (the flip's load-time refusal); OWED-SE §4 (R-SE-22) | `fixtures.py:809` |
| H-293, S-SE-2 | what custody takes from a ruler | SUPERSEDED | A-23 (custody suspends acts through the seat); `U5d_FA_owed_edits.md` §2 | #453 names the travel readers only |
| H-303 | a partly stocked rung blocks the walk | RESOLVED-BY | GROUND §4 d (R-SE-11) | — |
| H-305 | hunger's loss scales with headcount | RESOLVED-BY | CENSUS §4 a (R-SE-04) | `subsist.py:72` |
| H-309 | a seat holder who migrates keeps the seat | RESOLVED-BY | OWED-SE §1 (close the row, R-SE-17); the addendum's P-16 stands | — |
| H-304, H-307, H-168 | `tend` restores whole (PC's); over capacity at build; `migrate` only hand-built (now false) | RESOLVED-BY | PES-SE-A edit 4 (owed to PC, U5b); folded into F-SE-09; OWED-SE §1 (R-SE-18) | `aperture 3 0` |
| CR-40, CP-T08-01, -03, -04 to -08, -10, CR-08, CR-22, CR-49, CR-67, CR-106, CR-107, SE-06 | planned, unbuilt | RESOLVED-BY | the plan positions as amended by R-SE-01 to -05 and -19 (GROUND, CENSUS, OWED-SE §2) | — |
| SE-04 (b), R-SE-20 | `Rung.envelope` declared, unwritten, unread | RESOLVED-BY | plan IN-44 (delete through its Layer 1 row); OWED-SE §3 | grep `[not re-opened]` |
| `HANDOFF_SE` Open row 1 | waits on a closed ED | RESOLVED-BY | KERN-SE §6 (R-SE-13) | AM-E-15 |
| R-SE-01, -02, -03, -11 | endowment; stocking; the gate; the walk | RESOLVED-BY | GROUND | — |
| R-SE-04, -05, -06 | per-head loss; thinning; `empty` band | RESOLVED-BY | CENSUS | — |
| R-SE-07 to -10, -12 to -15 | kernel repairs and stale pointers | RESOLVED-BY | KERN-SE §2–§6 | — |
| R-SE-16, -17, -18 | register edits | RESOLVED-BY | OWED-SE §1 | — |
| R-SE-19 | `transfer`'s `to` binds the question's referent | RESOLVED-BY | OWED-SE §2 | — |
| R-SE-21 | a cohort's weight is 2 everywhere | RESOLVED-BY | plan CR-107 (authored rows); the generated cast (A-44) authors cohorts with weights, `21_PROCEDURAL_B_cast_and_seats.md` | H-170 |
| R-SE-22 | the ration is a `min` over every eaten kind | RESOLVED-BY | OWED-SE §4 | — |
| R-SE-23, -24 | case worlds hold no eater; every store move is 1 unit | RESOLVED-BY | ARCN §3 a, b | — |
| R-SE-25 | no settlement verb reads a capability | SUPERSEDED | by R-SE-32 (RATE-B) | H-164 |
| S-SE-1 | may a population recover | SUPERSEDED | the register's ladder table ("Yes, bounded by food and room", the 2026-09-17 ruling) and the addendum's C-1; REGROW-B | ED-SE-0051 `[ledger row not re-opened]` |
| §13 NPC-083, NPC-037, NPC-013 | shortfall against orders; treasury post; the tithe | RESOLVED-BY | ARCN §3 a, b; plan CP-T08-06, -07 | `corpus_run.build_at` seats no eater |
| §13 NPC-083 (methods), ARC-44/ARC-01 (drift with nobody acting) | "wrongly stated" | RESOLVED-BY | restated by the audit (the tier-4 redesign's; claim decay on a cohort's reasons); no SE edit | `rosters.yaml:79-80` |
| §13 NPC-090, ARC-20 | treaty trade; a trade dependency | RESOLVED-BY | ARCN §3 c; GROUND; TREAS-B (R-SE-30: the gate is a person's store move across two duchies) | `exchange` 0 of 79 |
| §13 ARC-46, ARC-07 | a depletable resource; a standing drain | RESOLVED-BY | SUPPLY (R-SE-34) | — |
| §13 ARC-12, EMG-C3, NPC-001, NPC-003, NPC-081 | owned by FI, WR, FA | SUPERSEDED | the owning closures (U5c; Parts 1 and 3 here) | — |
| §14 (capability surface) | (c) and (e) superseded | SUPERSEDED | the addendum §6; RATE-B | — |

## 2.3 `audits/07_SE_audit_addendum_B.md`

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| C-1 to C-8 | corrections to the first audit | RESOLVED-BY | made in the addendum; carried by TREAS-B (C-2, C-3), REGROW-B (C-1, C-8), RATE-B (C-5) | — |
| F-SE-17 | the proposed granary tier has no steward | RESOLVED-BY | TREAS-B (R-SE-28) | — |
| F-SE-18 | every quantity has one working arm, so any binding arm is a ratchet | RESOLVED-BY | REGROW-B (R-SE-26, -27) | — |
| F-SE-19 | the realm can raise only levy, at no cost to the place | RESOLVED-BY | SUPPLY (R-SE-33, -35); `06_FA_levy_through_the_seat_B.md` | — |
| F-SE-20 | supply has no place and no duration | RESOLVED-BY | SUPPLY (R-SE-34, -36) as constrained by R-PES-SE-14 (one ration, charged once a season) | — |
| F-SE-21 | two lanes' capability edits collide | RESOLVED-BY | RATE-B as reconciled; the home is `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md`'s | — |
| F-SE-22 | the food dependency's recorded resolution points at trade | RESOLVED-BY | TREAS-B (R-SE-30) | BALANCE-005; ED-SE-0009 `[not re-opened]` |
| F-SE-23 | the relief ladder's top is the Crown's for three duchies and not for the other two | RESOLVED-BY | OWED-SE §5 | the addendum's probe |
| F-SE-24 | `amount_shares` at 1000 strips below subsistence with no consequence path | RESOLVED-BY | OWED-SE §6 (R-SE-38: the flip is sequenced after CP-T08-06) | — |
| §2.3 (twelve `.audit/` findings re-verified) | true, false now, moved, irrelevant | RESOLVED-BY | none owed beyond the rows above (G-33 and G-04 false now; the stress-sim mechanics irrelevant, ladder step 2) | the addendum's table |
| §2.4 ARC-37/39, NPC-007, EMG-11, NPC-082, ARC-R17, ARC-14, NPC-087 | cases the first audit did not list | RESOLVED-BY | GROUND and OWED-SE §2 for SE's half; FA, FI, WR, CHAR own the rest (CR-107b; COHORT for ARC-14's population) | — |
| P-1 to P-16 | decisions on the first lane's placeholders | RESOLVED-BY | as the addendum's table: P-7 superseded by TREAS-B, P-10 by REGROW-B, P-14 by RATE-B; the rest stand in GROUND, CENSUS, ARCN, VALLEY | — |
| R-SE-26, -27 | recovery; flight is an act | RESOLVED-BY | REGROW-B | — |
| R-SE-28, -29, -30 | where relief sits; relief is the rule; the trade channel | RESOLVED-BY | TREAS-B | ED-IN-0255 `[not re-opened]` |
| R-SE-31, -37, -38 | endowment annotations; `ration` is no verb; when `amount_shares` flips | RESOLVED-BY | OWED-SE §6 (notes for the builder of GROUND and ARCN) | — |
| R-SE-32 | the capability rate against the other surfaces | RESOLVED-BY | RATE-B | — |
| R-SE-33 to -36 | hands under arms; the standing ration; training; the occupier | RESOLVED-BY | SUPPLY | — |
| §6 "stewardship: no passive bonus from a holder to his domain's yield" | declined by the addendum | SUPERSEDED | A-54 (a steward's skill bears on the harvest draw) and A-12 (a seat may carry a modifier); RATE-B as reconciled | — |

## 2.4 `audits/16_PESSIMIST_SE.md`

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| F-PES-SE-01 | a failing place changes nothing that any person does | RESOLVED-BY | PES-SE-A edits 2, 4; COHORT (the hungry cohort's petition, migration, refusal and riot, A-56); OWED-SE §7 (the kinds a trade is formed on, R-PES-SE-09) | the fail arm: eleven towns starve unseen |
| F-PES-SE-02 | nothing in the settlement layer is drawn | RESOLVED-BY | DRAWS edits 1–2 as reconciled (A-54: wear, harvest and hunger on the one four-band ladder); PES-SE-A edit 1 (the remainder) | `18_DETERMINISM_SWEEP.md:110` corrected by OWED-SE §8 |
| F-PES-SE-03 | a shared granary feeds towns in id order | RESOLVED-BY | PES-SE-A edits 1–2 | — |
| F-PES-SE-04 | a death by hunger is recorded as a death by nothing | RESOLVED-BY | PES-SE-A edit 3 | — |
| F-PES-SE-05 | the shipped supply fixture, turned on, reduces every army to its crash floor | RESOLVED-BY | TREAS-B and SUPPLY; PES-SE-B edit 4 | `pes_supply.py` |
| F-PES-SE-06 | a founding cannot fail, cannot found a town, and leaves a lot nobody uses | RESOLVED-BY | LAPSE as reconciled (A-55: fixed map; an empty founded household may lapse) | — |
| F-PES-SE-07 | the harvest is not an event; the weather runs the mines | RESOLVED-BY | PES-SE-B edits 1–2 as reconciled (A-54) | — |
| F-PES-SE-08 | a second garrison adds nothing and a new one halves the walls | RESOLVED-BY | PES-SE-B edit 3 | — |
| F-PES-SE-09 | two fifths of production has no use; three objects have no reader | RESOLVED-BY | OWED-SE §9 (R-PES-SE-05 to -08) | — |
| F-PES-SE-10 | want lowers the attempt to trade | RESOLVED-BY | OWED-SE §7 (owed to CHAR's formation; U5a) | — |
| F-PES-SE-11 | the story instruments cannot see a place | RESOLVED-BY | none owed (§0.1 pt 5); `23_STORY_D_story_census_and_gate.md` reads places | — |
| F-PES-SE-12 | stocking the larders at world-gen coincides with every migration stopping | RESOLVED-BY | OWED-SE §10 (a gate arm on GROUND's stocking edit); the drawn start (A-50) leaves some larders low | the pessimist's two-arm run |
| F-PES-SE-13 | smaller kernel defects | RESOLVED-BY | OWED-SE §9 (R-PES-SE-13) and KERN-SE | — |
| R-PES-SE-01 to -04 | sharing; the crossing; causes; `tend` and hunger | RESOLVED-BY | PES-SE-A edits 1–4 | — |
| R-PES-SE-05, -07, -08, -09, -13 | ore's reader; hunger bands; `coin`; trade kinds; Site-kind names | RESOLVED-BY | OWED-SE §7, §9 | — |
| R-PES-SE-06, -10, -11, -12 | `Rung.yield`'s reader; grown kinds; walls; the flip | RESOLVED-BY | PES-SE-B edits 2, 1, 3, 4 | — |
| R-PES-SE-14 | one ration on two clocks | RESOLVED-BY | SUPPLY (a constraint on R-SE-34) | — |
| J-1 | does a chronic dearth speak | SUPERSEDED | the ladder table's D-69 (A: famine reports once; the never-stocked edge repaired); PES-SE-A edit 2 as reconciled | H-160 limit 3 |
| J-2 | how does the world's own motion draw | SUPERSEDED | A-54 (the one four-band ladder) | — |
| J-3 | may a place begin, and may a begun place end | SUPERSEDED | A-55 | SE-9(a) |
| §5 lists; §6.3 owed | false N-lines; failed premises; items owed to other lanes | RESOLVED-BY | OWED-SE §8–§10; PC's `tend` is U5b's | — |

---

# Part 3 — WR (the world's own motion, story readings, threadwork)

Carriers: **STRAND** = `09_WR_strand_conclusion.md`; **INSTR** = `09_WR_story_instruments_that_can_fail.md`;
**MOTION** = `09_WR_world_motion.md`; **THREAD** = `09_WR_threadwork_module.md`; **ARCS-WR** =
`09_WR_provided_arcs.md`; **READ-B** = `09_WR_B_readings_of_closure_and_tension.md`; **CHRON-B** =
`09_WR_B_chronicle_that_tells.md`; **WEATHER-B** = `09_WR_B_weather_with_memory_and_the_year.md`;
**THREAD-B** = `09_WR_B_threadwork_session_and_practitioner.md`; **DRAWS** =
`09_WR_B_draws_not_thresholds.md`; **PTR-B** = `09_WR_B_pointer_text_for_the_orchestrator.md`;
**PES-WR-A/B/C/D** = `16_PESSIMIST_WR_A…D_*.md`; **OWED-WR** = `U5d_WR_owed_edits.md` and **UNKNOWABLE** =
`U5d_WR_zero_coherence_unknowable.md` (both written by this lane).

## 3.1 `audits/09_WR_audit.md` — findings, §6, §11, §13

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| F-WR-01 | no story in the shipped realm escalates or ends | RESOLVED-BY | INSTR edit 4 (the reading); the closing acts are other lanes' (PC's duel, SC's `determine`, FA's `revoke` and `succeed`: U5b, U5c, Part 1); PES-WR-D edit 4 (`storybar.turns`) | six seasons, seed 0: one strand of 234 moves; 0 deaths |
| F-WR-02 | a strand's conclusion does not discriminate; strands collapse into one | RESOLVED-BY | STRAND edits 1–3 as reconciled (A-45: several strands that can each end; edit 3 is now the ruled form) with DRAWS edit 4 (concludes on the move's drawn degree) | E-08 |
| F-WR-03 | the story bar cannot fail, has no forcing arm, and one control is inverted | RESOLVED-BY | INSTR edits 1–3 (R-01, R-02, R-18; plan CR-99 folded into edit 1) | `harness/storybar.py` `[not re-opened]` |
| F-WR-04 | the world's own motion ships off; the world's readings have no reader | RESOLVED-BY | MOTION edit 1; WEATHER-B edits 1–2 and DRAWS edits 1–2 as reconciled (A-54: one four-band ladder) | fixtures at 0 |
| F-WR-05 | threadwork is not in the game and is not a module | RESOLVED-BY | THREAD edit 3 (tables as typed data) and THREAD-B edits 1–4 (which supersede THREAD edits 1, 2, 4) | `(Person, coherence)` unproduced, `write_matrix.yaml:200-206` (opened) |
| F-WR-06 | the victory ending is unreachable on one territory; its register row is stale | RESOLVED-BY | MOTION edit 3 (settled territories), reached by a draw (DRAWS edit 3) | GD-1 |
| F-WR-07 | the flow stamp's reach hangs on one Event kind | RESOLVED-BY | none of its own (the stamp is correct; its inputs are rare): it reads again once F-WR-01's closing acts execute; H-274 stays open with that note | dose 0 to 28% by seed |
| F-WR-08 | `ENDINGS_CLASSIFIED.yaml` is prose read by a builder | RESOLVED-BY | ARCS-WR edit 3 (stop planting; correct the path) | `corpus_run.py:656-660` |
| F-WR-09 | memory decay is half the log and grows | RESOLVED-BY | `01_CORE_claim_fade_as_read.md` (U5a's; the ladder's D-48: forgetting computed when read) | 179,056 `claim.decayed` (E-08) |
| F-WR-10 | every cohort starves in season 0 and never again | RESOLVED-BY | plan CR-22 with `07_SE_ground_and_granaries.md` as reconciled (the drawn start, A-50) | `body.changed` 37 in season 0 |
| F-WR-11 | MATTER recovery is silent (H-211) | RESOLVED-BY | ARCS-WR edit 2 (the signed step) with OWED-WR §3 (F-WR-23's body Observation lands with it) | `matter.py:119, :690-711` |
| F-WR-12 | currency rows point at retired documents | RESOLVED-BY | PTR-B (text for the orchestrator: R-11, R-12, R-20) | `CURRENT.md:36, :28` `[not re-opened]` |
| §6.1 rows closed at HEAD (H-04, -05, -27, -34, -40, -51, -95, -103, -110, -118, -172, -242, -243, -245 to -247) | listed open or unsure; verified closed | STALE-FALSE-POSITIVE | PTR-B carries the re-grade text for H-05, -27, -172 | the audit's E-07, E-08, E-15 |
| §6.1 rows "not WR's" (H-32, -65, -107, -129, -130, -135, -139, -150, -164, -167, -168, -185, -209, -215, -216, -223, -225, -227, -230, -278, -283, -287, -291, -307, -311, -326, -350, -356) | another lane's mechanism | SUPERSEDED | the owning closures (U5a, U5b, U5c; Parts 1 and 2 here); the addendum's §6 re-reads each (3.2 below) | — |
| H-102, H-125, H-159, H-232 | open as a sign, a value, a value, a refusal | RESOLVED-BY | none owed by WR: H-125 is re-derived by CR-22; H-159 is FA's term (Part 1, TERMS-B); H-232 is CHAR's and FA's formation | E-05, E-08 |
| H-176, H-186, H-235, H-236 | endings; insurgency; the lattice | RESOLVED-BY | MOTION edits 3, 2, 1 | E-13 |
| H-208, §11 item 2 | natural death deferred | SUPERSEDED | A-15 (on, after the ages are authored); carrier `22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn.md` and PES-WR-C as reconciled | ED-IN-0317 `[not re-opened]` |
| H-211 | a body only falls | RESOLVED-BY | ARCS-WR edit 2; plan CP-T10-04 | — |
| H-238 | no corpus thread sensitivity | RESOLVED-BY | none owed (answered at ladder step 1 by the row itself) | E-15 |
| H-257, R-06 | a real execution reads KL, not XE | RESOLVED-BY | OWED-WR §1 (`strife.py:85`) | — |
| H-274 | the stamp | RESOLVED-BY | as F-WR-07 | — |
| B10-15, B10-18, CL-THRUST, CL-OPEN, CR-80, B11-F2/F3, WR-01, HANDOFF_WR item 2 | plan positions | RESOLVED-BY | the plan, with THREAD-B before CP-T07-02 (R-08) and CR-99 folded into INSTR edit 1 | — |
| R-01, R-02, R-18 | story bar | RESOLVED-BY | INSTR edits 1–3 | — |
| R-03, R-04, R-05 | lattice source; victory selector; unheld land | RESOLVED-BY | MOTION edits 1, 3, 2 (edit 2 stands under A-57/A-58: ground no party holds is outside the rule) | — |
| R-07 | a strand concludes on an opening kind | RESOLVED-BY | STRAND edits 1–2 | — |
| R-08, R-09 | the module; its tables | RESOLVED-BY | THREAD-B; THREAD edit 3 | — |
| R-10, R-17, R-19 | the empty thrust ladder; sixteen links read 0; live tenures at a move's tick | RESOLVED-BY | none owed (statements recorded in the audit; no code) | — |
| R-11, R-12, R-20 | pointer text | RESOLVED-BY | PTR-B | — |
| R-13 | a body only falls | RESOLVED-BY | ARCS-WR edit 2 | — |
| R-14 | claim decay | RESOLVED-BY | `01_CORE_claim_fade_as_read.md` | — |
| R-15, R-16 | the planted column; automatic clocks | RESOLVED-BY | ARCS-WR edits 3, 1, 4 as reconciled (A-47: the count opens a mandatory scene) | — |
| §11 item 1 | the same-doer link | SUPERSEDED | A-45 (several strands) | ED-IN-0316 |
| §11 item 3 | the slate | SUPERSEDED | A-48 (a list of questions for the player; NPCs take the first); `11_GO_player_surface_contract_B.md` as reconciled | H-54 |
| §13 ambient decay, bands, the lattice (ARC-05, -48, -27, -43, EMG-C3, NPC-075) | in kind; needs a source | RESOLVED-BY | MOTION edit 1; PES-WR-B | E-07, E-16 |
| §13 threadwork cases (ARC-48, -05, -41, -42, -09, NPC-002, -004, -005, ARC-51, EMG-X7, -X8, SCN-LOOP-A) | no working exists | RESOLVED-BY | THREAD-B; plan B10-15 (CP-T07-02 to -10); ARC-51's growth is CHAR's | `write_matrix.yaml:206` |
| §13 private counters (ARC-34, -47, -31, -32, NSC-05, -08, EMG-C1, EMG-10) | a counter forces a step | RESOLVED-BY | ARCS-WR edit 1 as reconciled (A-47) | `world_q.py:162-168` |
| §13 "wrongly stated" (ARC-47/NSC-08 never decreases; ARC-46 passage of time; ARC-52 a ceiling eliminates) | restated | RESOLVED-BY | ARCS-WR edit 4; A-47 keeps the restatement's core (the crossing decides nothing) and adds that it may open a mandatory scene | — |
| §13 institutional clocks (ARC-46, -50, EMG-C2, NSC-09, ARC-03, -45) | standing rises by itself | RESOLVED-BY | plan CR-89 (FA; Part 1) | — |
| §13 ARC-02 | a state-change check with no actor | SUPERSEDED | A-15 | — |
| §13 ARC-53, SCN-07, ARC-23 | represented today | STALE-FALSE-POSITIVE | none owed | `tend` 37/69 (E-07) |
| §13 SCN-06, SCN-LOOP-C | drains and restorations summed | RESOLVED-BY | ARCS-WR edit 2 | H-211 |
| §13 ARC-07, NPC-052, ARC-01, ARC-44 | other lanes' | SUPERSEDED | U5b; Parts 1 and 2 | — |
| §13 the 19 `forced_by_threshold` cases | misrepresented by a planted holderless date | RESOLVED-BY | ARCS-WR edit 3; A-47 | `corpus_run.py:656-660` |
| §14 (capability surface; "banded scalar") | asked CHAR for a row kind | SUPERSEDED | the addendum's R-24 (none needed) | — |

## 3.2 `audits/09_WR_audit_addendum_B.md`

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| F-WR-13 | the realm closes by clock, not by act (23 lapsed against 3 determined) | RESOLVED-BY | READ-B edit 1 (R-29); the acts that close are other lanes' | three seeds, six seasons |
| F-WR-14 | the chronicle prints who and when, never what, from no viewpoint | RESOLVED-BY | CHRON-B (R-28, R-32) as reconciled (A-49, A-33, A-43) | `world_q.py:4374-4441` |
| F-WR-15 | no reading of open situations, tension or idle persons | RESOLVED-BY | READ-B | — |
| F-WR-16 | flattening every person to the realm mean lowers no story reading | RESOLVED-BY | READ-B (the ablation kept as a reading); the fix is CHAR's (H-283, U5a) | EB-01 |
| F-WR-17 | threadwork's designed session has no code and no plan position | RESOLVED-BY | THREAD-B edits 1–2 | — |
| F-WR-18 | the first lane's scenario shows the practitioner his own Coherence band | RESOLVED-BY | THREAD-B edit 3 (R-25); UNKNOWABLE (A-43, for what others read of him) | `data/requires.py:809` |
| F-WR-19 | the scheduled weather has no memory, no neighbours and a mean of 1.167 | RESOLVED-BY | WEATHER-B edits 1–2 as reconciled (A-54) | — |
| F-WR-20 | the second contest (the world's survival) has no reading and no ending | RESOLVED-BY | WEATHER-B edit 4; DRAWS edit 3 | — |
| F-WR-21 | 248 of 322 `condition.worn` Events are writes of zero | RESOLVED-BY | READ-B edit 2 (R-30); `07_SE_kernel_repairs.md` §3 removes the write | EB-07 |
| F-WR-22 | three hole rows rest on deaths that no longer occur at their seed | RESOLVED-BY | PTR-B (R-31) | — |
| F-WR-23 | a believed wound is never cleared | RESOLVED-BY | OWED-WR §3 (a body Observation on `tend` and on recovery; owed at PC's and CHAR's owner, sequenced before R-13 and CP-T10-04) | `world_q.py:3806-3812` |
| F-WR-24 | wear, strain, the hungry body, a lapse, endings and a strand's conclusion are fixed functions of state | RESOLVED-BY | DRAWS edits 1–4 (R-37 to R-40), confirmed in form by A-54 and A-24 | — |
| §2.2 corrections 1–11 | corrections to the first audit and to this addendum | RESOLVED-BY | made in place; THREAD-B supersedes THREAD edits 1, 2, 4; CHRON-B carries 8; R-25 carries 9 | — |
| R-21, R-22, R-25, R-34, R-40 | host declaration; cost by direction; coherence world-only for its owner; a Partial's scope; contact, cost and breach drawn | RESOLVED-BY | THREAD-B edits 1–3 | — |
| R-23, R-26, R-27 | a leg's price; the Rupture's selector; a spell | RESOLVED-BY | WEATHER-B edits 3, 4, 1–2 | — |
| R-24, R-33, R-35 | no "banded scalar"; no navigation capability; no Approach Training gate | RESOLVED-BY | none owed (A-11 confirms: training gates nothing; Thread Sensitivity is the one gate) | — |
| R-28, R-32 | what a line is about; the journal's source | RESOLVED-BY | CHRON-B | — |
| R-29, R-30 | closed by act or by clock; non-zero changes only | RESOLVED-BY | READ-B edits 1–2 | — |
| R-31 | re-point three rows | RESOLVED-BY | PTR-B | — |
| R-36 | the Rendering Crisis's four beats | RESOLVED-BY | none owed (the Event alone; the journal tells) | — |
| R-37, R-38, R-39 | wear drawn; endings drawn; a strand concludes on a drawn degree | RESOLVED-BY | DRAWS edits 1, 3, 4 | — |
| §6: 19 rows closed at HEAD | H-04, -05, -27, -34, -40, -51, -95, -103, -107, -110, -118, -129, -172, -242, -243, -245, -246, -247, -356 | STALE-FALSE-POSITIVE | PTR-B for the rows whose text is owed | the addendum's table |
| §6: 6 rows open in this lane | H-102, -125, -135, -159, -164, -208 | RESOLVED-BY | READ-B (H-135's reading); CR-22 (H-125); TERMS-B (H-159); A-15 (H-208); H-102 and H-164 stay open as measured signs with no edit owed | — |
| §6: 4 rows whose measurement is stale | H-168, -209, -225, -230 | RESOLVED-BY | PTR-B (re-pointed); `U5d_SE_owed_edits.md` §1 for H-168 | — |
| §6: 20 rows another lane's | read and left | SUPERSEDED | the owning closures | — |

## 3.3 `audits/16_PESSIMIST_WR.md`

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| F-PES-WR-01 | no story in computed play has a turn | RESOLVED-BY | PES-WR-D edit 4 (the reading); the closing verbs are FA's, SC's and PC's | — |
| F-PES-WR-02 | the Calamity has no source, no break and no answer | RESOLVED-BY | PES-WR-B edits 1–3 as reconciled (A-40: the wear is a real condition of places, one Site per territory); MOTION edit 1 lands only with them | — |
| F-PES-WR-03 | the world's own change is one ramp in 37 places | SUPERSEDED | F-SE-01 (Part 2: GROUND) and F-PES-GAME-05 (Part 6) own it | — |
| F-PES-WR-04 | CALENDAR can be removed and no reading notices | RESOLVED-BY | PES-WR-D edits 3, 5 (R-1) | the cut arm |
| F-PES-WR-05 | the Thread is read off letters, finds nothing and costs nothing | RESOLVED-BY | PES-WR-D edit 2 (`referent_class: Site`); THREAD-B | — |
| F-PES-WR-06 | a journey is free, instant and certain | RESOLVED-BY | PES-WR-A | — |
| F-PES-WR-07 | the bodies clock is a coin, the same coin for everyone | RESOLVED-BY | PES-WR-C as reconciled (A-15: no longer dark once the ages are authored); `22_HAPPENINGS_A` owns the rate and the bout | `fixtures.py:692` |
| F-PES-WR-08 | every run is the same run | RESOLVED-BY | none of its own (the sum of F-WR-01 and the world's motion being off); the seeded start (A-50) and the generated cast (A-44) are the differences between seeds, `21_PROCEDURAL_B`, `_D` | — |
| F-PES-WR-09 | a Date due in the past never fires | RESOLVED-BY | PES-WR-D edit 1 (R-9) | — |
| F-PES-WR-10 | "pressure" never fires | RESOLVED-BY | PES-WR-D edit 1 | — |
| F-PES-WR-11 | the band-crossing channel is dead from end to end | RESOLVED-BY | PES-WR-B edit 4 | — |
| R-1 to R-12 | resolutions | RESOLVED-BY | PES-WR-A (R-5, R-6), -B (R-2, R-3), -C (R-7, R-8), -D (R-1, R-9 to R-12); R-4 is text for the orchestrator (OWED-WR §4) | — |
| §5, §6, §7 lists | false N-lines; premises; stories | RESOLVED-BY | none owed beyond the rows above | — |
| §8 (items listed for other lanes) | illness not yet graded; the lattice flip a fixed-function collapse | RESOLVED-BY | PES-WR-C; PES-WR-B edits 1–2 before MOTION edit 1's flip | — |

---

# Part 4 — GO (the port gate and the player surface)

Carriers: **DRAW** = `11_GO_one_draw_owner.md`; **FLOAT** = `11_GO_float_contract.md`; **GATE** =
`11_GO_port_gate_order_and_coverage.md`; **SURF** = `11_GO_player_surface_contract.md` (superseded);
**SURF-B** = `11_GO_player_surface_contract_B.md`; **MODES** = `11_GO_fidelity_and_campaign_modes.md`;
**REF** = `11_GO_design_reference_disposition.md`; **TEXT** = `11_GO_pointer_and_stale_text_resolutions.md`;
**KEYED** = `16_PESSIMIST_GO_keyed_draw_no_recorder.md`; **PINS** = `16_PESSIMIST_GO_surface_pins.md`;
**HELD** = `16_PESSIMIST_GO_the_offer_names_what_is_held.md`; **WHY** =
`16_PESSIMIST_GO_a_witness_may_connect_what_he_holds.md`; **OWED-GO** = `U5d_GO_owed_edits.md` (written
by this lane).

## 4.1 `audits/11_GO_audit.md`

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| F-GO-01 | the pinned slices barely enter the two largest modules | RESOLVED-BY | GATE §3 (R1); PINS (the surface block) | combat entered 0/2/4 times, a fought field 0/0/1 (E4) |
| F-GO-02 | the float contract is unstated; Layer 1 and the plan disagree | RESOLVED-BY | FLOAT A, B, C as reconciled (A-29: declared floats now; the Layer 1 text for step 13 is owed, not applied) | `04:1130`; 1,245 floats folded a season |
| F-GO-03 | draws are built in two places; replay never tests the port's samplers | RESOLVED-BY | KEYED (A-30: one draw per key, no recorder) with DRAW as reconciled (one constructor and one sampler kept; the recorder and replay withdrawn) | `combat.py:397` (E4) |
| F-GO-04 | 91 mass-battle tunables read from the environment and exported nowhere | RESOLVED-BY | GATE §5 (R10) | the audit's count |
| F-GO-05 | halts have no portable form; GO-10 covers four sites | RESOLVED-BY | GATE §4 (R11) | 172 in-loop raises |
| F-GO-06 | the gate freezes behaviour while the game is being invented; two edges wrong | RESOLVED-BY | GATE §1, §2 (R12, R13, R14) | — |
| F-GO-07 | what the player is shown has an owner for the choice and none for the reason or the result | RESOLVED-BY | SURF-B §1–§4 (supersedes SURF §1–§4) | — |
| F-GO-08 | PLAYABLE exists at one seam | RESOLVED-BY | SURF-B §6 (corrected by F-GO-18: two kinds of play) as reconciled (A-9: a turn is a short sequence); GATE §3 | — |
| F-GO-09 | no save; the canonical encoding cannot rebuild a world | RESOLVED-BY | OWED-GO §1 (R44's snapshot, as a plan with a round-trip gate; A-29 makes a save a state snapshot and A-30 keeps a seed a world) | `state/world.py:390`; no decoder (grep) |
| F-GO-10 | stale and contradictory text at the pointers a porter reads first | RESOLVED-BY | TEXT 1–13 | the audit's table |
| F-GO-11 | the digest test's control half is spent | RESOLVED-BY | TEXT 11 (R32) | `test_go07_canonical_digest.py:282-311` `[not re-opened]` |
| F-GO-12 | the determinism controls vary the hash seed, not the interpreter | RESOLVED-BY | FLOAT (removes the cause at its owner); no guard (§0.1 pt 5) | the audit's E5: no drift reproduced at seed 0 |
| GO-07, GO-13, GO-14 | listed closed; verified closed | STALE-FALSE-POSITIVE | none owed (GO-07's test trimmed by TEXT 11) | E3, E5, E8 |
| GO-09, GO-11, GO-01, GO-05 | open; early landings | RESOLVED-BY | GATE §2 (R13, R14); TEXT 8, 9 | — |
| GO-10, GO-12, GO-08, GO-15 | open; under-scoped or mis-shaped | RESOLVED-BY | GATE §4, §5, §3, §1; DRAW (R8: every unseeded fallback refuses) | — |
| GO-16 | the draw recorder; premise false | SUPERSEDED | A-30: not built; KEYED | PES-GO §1.1 |
| GO-06 | cross-repo reader, held | RESOLVED-BY | none owed (correctly held; another repository) | — |
| ED-1054 | stale navigation open since 2026-06-30 | RESOLVED-BY | TEXT (R35: closed; the banners are its resolution) | — |
| Strategy Part VIII items 1–8 (R36–R43) | open items | SUPERSEDED | closed by the ladder in the audit (the Key substrate retired; the oracle by ED-1050; no stat vector; §C.12) | R42 `[UNVERIFIED]` in the audit: stays marked |
| R1, R10–R14 | pins; tunables; halts; freeze; edges | RESOLVED-BY | GATE §1–§5 | — |
| R2, R3, R4 | float sums; transcendentals; "slice 3" | RESOLVED-BY | FLOAT A, B | — |
| R5, §11 survivor | step 13's "integer domain" | SUPERSEDED | A-29 (declared floats now; integer state stays possible); FLOAT C | — |
| R6, R8 | one constructor; fallbacks refuse | RESOLVED-BY | DRAW | — |
| R7, R9, R33 | replay of the port's samplers; what GO-16 records; "statistical parity" | SUPERSEDED | A-30 and A-5: the port implements the same keyed hash and the one sampler; nothing is recorded or replayed | — |
| R15–R20 | offer rows; `explain`; aftermath; scar Events; "a player must be able to"; PLAYABLE | SUPERSEDED | by SURF-B (R50–R57, R72–R78), which corrects R17 and R20 | addendum §B6.2 |
| R21, R36–R43, R47 | superseded or irrelevant items | RESOLVED-BY | none owed | — |
| R22–R32, R34, R35 | pointer and stale text | RESOLVED-BY | TEXT 1–13 | — |
| R44 | no save | RESOLVED-BY | OWED-GO §1 | — |
| R45, R46 | the UI design set; "witnessed" fidelity | RESOLVED-BY | SURF-B; MODES §2 (R62 refines R46) | — |
| §13 arcs represented today (ARC-R16, ARC-25, -36, -38, NPC-012, -033, -007; ARC-47, -R19, EMG-C2 as epistemics) | the world acts unattended; hidden quantities | STALE-FALSE-POSITIVE | none owed (represented) | 749 acts, 13,379 Events a season (E3) |
| §13 ARC-R16 summary, ARC-46 history, ARC-24 | readings a person lacks | RESOLVED-BY | SURF-B §3–§4 (`receipt`, `account`); SURF-B §2 for a history over his own claims | E7 |
| §13 ARC-14, ARC-17 ("a single threshold stat", "a fixed lookup") | wrongly stated (a player/NPC fork) | RESOLVED-BY | restated by the audit; A-47 keeps the threshold as the opener of a mandatory scene, never the decider | — |
| §13 "players must be able to X" (53 needs), the 16 `WAITS-ON-PLAYER` cases | per verb | RESOLVED-BY | SURF-B §2 (`OFFER-CONTAINS`); each act is its verb lane's | 23 of 67 verbs execute (E10) |
| §13 ARC-09, NPC-088 and others cross-listed | not GO's | SUPERSEDED | U5a (CORE, CHAR) | — |
| §14 (capability surface; R31) | may a field bind to an attribute | RESOLVED-BY | TEXT 10 | `descriptors.json` |

## 4.2 `audits/11_GO_audit_addendum_B.md`

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| F-GO-13 | the UI set's content-level half is not in the tree | RESOLVED-BY | REF (R48: not reconstructed; the oracle's readings are the specification) | — |
| F-GO-14 | the newest UI document carries two dead tracks; its repair plan stopped | RESOLVED-BY | REF (R49) | — |
| F-GO-15 | no shared surface vocabulary; six lane dialects | RESOLVED-BY | SURF-B (R50) | — |
| F-GO-16 | a person cannot read what his own act came to | RESOLVED-BY | SURF-B §3 (`receipt`), with the measure corrected by F-PES-GO-11 (6 to 8%, three inquiry verbs) | — |
| F-GO-17 | `AftermathRow.own_act` cannot be computed | RESOLVED-BY | SURF-B §4 (R52) | — |
| F-GO-18 | two kinds of play; two choice surfaces missed | RESOLVED-BY | SURF-B §6 (R53, R54) | — |
| F-GO-19 | the offer is three to five times the legible size | RESOLVED-BY | SURF-B §2 (R55); MODES §3 (R56) as reconciled (A-48: the player triages a list of questions) | up to 544 rows (F-PES-GO-09) |
| F-GO-20 | the Godot specification contradicts Layer 1 at five points | RESOLVED-BY | REF edit 1 (R66–R71) | — |
| F-GO-21 | two opposite answers to "what does the player know" | RESOLVED-BY | REF (R58, R59); the end-of-campaign half is A-49 | — |
| R48–R78 | thirty-one resolutions | RESOLVED-BY | SURF-B (R50–R55, R57, R72–R74, R76–R78), MODES (R56, R60–R65), REF (R48, R49, R58, R59, R66–R71, R75) | — |
| R77 | the Scene Slate has no generator | SUPERSEDED | A-48: the slate is a list of questions offered to the player; NPCs take the first; SURF-B §1 as reconciled | — |
| §B6.3 survivor | may the end of a campaign show what the person never knew | SUPERSEDED | A-49 (reveal after the line ends and no continuation is taken; never in play); MODES §4 as reconciled (E2 added on top of E1) | — |

## 4.3 `audits/16_PESSIMIST_GO.md`

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| F-PES-GO-01 | the parity contract cannot see the player's surface | RESOLVED-BY | PINS | — |
| F-PES-GO-02 | GO-16 is a false N-line | RESOLVED-BY | KEYED (A-30) | PES-GO §1.1 cut |
| F-PES-GO-03 | the offer names persons the seat does not know | RESOLVED-BY | HELD §1–§3 (seat news ships realm-wide, A-32) | `seat_holders` |
| F-PES-GO-04 | "why" is `None` by construction | RESOLVED-BY | WHY | `Seen.why` |
| F-PES-GO-05 | believed odds answer on 0.8% of candidates | RESOLVED-BY | `10_DICE_believed_odds_have_a_prior.md` (U5a's; the pessimist's three edits listed for CHAR and DICE); OWED-GO §2 records the order | — |
| F-PES-GO-06 | what a person learns of others' acts is nothing for most | RESOLVED-BY | WHY; `18_DETERMINISM_notice_is_a_draw.md` (U5a) | 57 to 62% |
| F-PES-GO-07 | the offer is half inert | RESOLVED-BY | `16_PESSIMIST_CORE_a_refusal_is_remembered.md`, `16_PESSIMIST_FI_D_withhold_what_has_no_product.md` (U5a, U5c); GO adds no filter (resolution 5) | 21% of acts on fifteen rows |
| F-PES-GO-08 | PLAYABLE's reach is one person's one verb | RESOLVED-BY | SURF-B §6; "one code path" shown for all 83 seats (resolution 11) | E2 |
| F-PES-GO-09 | the offer's size has a tail of up to 544 rows | RESOLVED-BY | SURF-B §2; MODES §3; A-48 | — |
| F-PES-GO-10 | the creation sheet cannot tell seats apart and offers 37 cohorts | RESOLVED-BY | HELD §4 (`CreationRow.holdings`, `cohort`); `U5d_SE_cohort_heavy_moves_and_caste.md` (a cohort forms the heavy moves only; whether one may be played is not ruled) | — |
| F-PES-GO-11 | corrects F-GO-16's measure | RESOLVED-BY | made in the audit | — |
| F-PES-GO-12 | no exported word for any Event kind or verb | RESOLVED-BY | PINS (words for kinds and verbs) | — |
| F-PES-GO-13 | exit line 4 lists a check that reports drift and passes | RESOLVED-BY | OWED-GO §3 (a card edit at B10-20's open) | the tool's own text |
| resolutions 1–11 | decided | RESOLVED-BY | PINS (1), KEYED (2), HELD (3, 6), WHY (9); 4 → F-PES-GO-05's row; 5 none; 7 → `03_PC_typed_outcome_one_door.md` (U5b) and OWED-GO §2; 8 → OWED-GO §3; 10, 11 statements | — |
| §7 survivor | the draw | SUPERSEDED | A-30 | — |

---

# Part 5 — ARCS (`audits/12_ARCS_adjudication.md`)

Carriers: **CASE** = `12_ARCS_case_on_the_realm.md` (extends `01_CORE_case_setup_and_beats.md`, U5a's);
**STAGED** = `12_ARCS_arcs_as_staged_goals.md`; **GROUND-T** = `12_ARCS_substrate_as_ground.md`;
**CITED** = `12_ARCS_cited_evidence.md`. The adjudication numbers no findings; its rows are the fifteen
mechanisms of §4, the twenty resolutions of §6, the tables of §5 and §7 to §10, and two survivors.

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| §3 (the per-case table, 143 cases) | each case's unreached core needs, by mechanism | RESOLVED-BY | the mechanism rows below; no case is closed separately | the generated mapping (`arcs_work/census.py`, §12) `[not re-run]` |
| M-CASE | a case built from its own people, seats, records and dates; beats read by a run with a control | RESOLVED-BY | `01_CORE_case_setup_and_beats.md` as extended by CASE as reconciled (A-44, A-50, A-51: the case is a delta on a generated, seeded realm that has run its five-year prologue) | template builder; no need read (§2.2) |
| M-LATENT | 84 core needs are a counter, clock or scalar that fires with nobody deciding | RESOLVED-BY | STAGED as reconciled (A-47: the armed last stage opens a mandatory scene; the crossing decides nothing); `02_CHAR_goal_lean_on_its_own_question.md` | `state/world.py:64-107`; `loop/matter.py:132-135` `[not re-opened]` |
| M-INFO | information that travels, is withheld, is found | SUPERSEDED | FI's closure (U5c: `08_FI_01`, `_02`, `_03`); death news apart (A-33) | `told_by` 64 of 93,760 claims |
| M-SEAT | an office that does its business | RESOLVED-BY | Part 1 (DECREE, REMIT, TERMS, TERMS-B, CAPS-FA) and the institutions kit (Part 7); "passive effects of holding a seat" are now lawful (A-12) | `confer` 70/0, `revoke` 15/0 |
| M-PERC | the Thread, person side | RESOLVED-BY | GROUND-T (person half) as reconciled; `09_WR_B_threadwork_session_and_practitioner.md`; `U5d_WR_zero_coherence_unknowable.md` (A-43) | `harness/loops.py:96`; `write_matrix.yaml:200-206` |
| M-SUB | the Thread, world side | RESOLVED-BY | GROUND-T as reconciled (A-40: ground, one Site per territory; the hold is lifted) with `16_PESSIMIST_WR_B_the_calamity_strains_and_breaks.md` | no carrier (grep, §12) |
| M-AIM | the chooser reads what an act would do | SUPERSEDED | CHAR's closure (U5a: `02_CHAR_goal_lean_on_its_own_question.md`, `02_CHAR_choice_alignment.md`) | F-CHAR-01 |
| M-SIT | a sitting that binds | SUPERSEDED | SC's closure (U5c: `05_SC_playable_hearing_B.md` and siblings) | — |
| M-REGARD | the interior moves | SUPERSEDED | U5a (`02_CHAR_scar_cap_and_regard_unit.md`) | F-CHAR-03 |
| M-REC | a record as an object with consequence | RESOLVED-BY | CITED as reconciled (admission and the strike are draws: `19_LACUNA_admission_rides_the_citing_draw.md`; the interface is `08_FI_05_evidence-interface_B.md`) | H-75 |
| M-CAP | persons differ in what they can do | SUPERSEDED | U5a (`unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md`; A-7 two inputs) | — |
| M-FIELD | force at scale with lasting consequences | SUPERSEDED | U5b (`04_MB_*`, `03_PC_exits_withdrawal_recovery.md`); the land and its seats pass by `U5d_FA_land_and_seats_pass_on_a_won_march.md` | `march` never attempted in the corpus |
| M-STORES | material economy | RESOLVED-BY | Part 2 (GROUND, ARCN) | — |
| M-ABROAD | powers beyond the map, through persons | RESOLVED-BY | `15_INSTITUTIONS_BYZANTINE_D_the_empire_at_a_distance.md` and `15_INSTITUTIONS_COLONIAL_B_distance.md` (the far superior is one seat, `off_altonian_court`) | §6 row 12 ("none written") |
| M-PLAYER | a player's seat (16 cases) | RESOLVED-BY | `01_CORE_case_setup_and_beats.md`; `11_GO_player_surface_contract_B.md` (`OFFER-CONTAINS`) | `play_surface.dispatching_chooser` has no caller in the runner |
| M-SPAN | long arcs (`MAX_SEASONS = 6`) | RESOLVED-BY | `01_CORE_claim_fade_as_read.md` (U5a) | `loop/matter.py` |
| §5 (staged sequence, stages 0–8) | the order that unlocks cases | RESOLVED-BY | none owed: an ordering input to the suite's one landing order; stages 7 and 8 no longer wait (A-40, A-43) | — |
| §5 scripting-drift table (ARC-14, -17, -11, NPC-011, ARC-52, -55, -46, NPC-020 N8, ARC-22, ARC-01 N5) | needs that can only be met by special-casing | RESOLVED-BY | the non-script form in the table; two are changed by rulings: the "auto-resolve at a ceiling" needs gain a mandatory scene (A-47); "an unpredictable family death" is natural death at a rate (A-15), never an event card | — |
| §6 rows 1, 7, 17 | social counters; struck mechanics; ARC-55's circle | RESOLVED-BY | STAGED | — |
| §6 rows 2, 3, 4, 5, 10, 11, 13, 14, 15, 19, 20 | a faction "chooses"; fixed lookup; "GM-judged"; a skill gates; registry values; collisions; lost head; ordinary knowledge; unauthored goals | RESOLVED-BY | none owed (decided by ladder steps 1–3 in the audit; A-11 confirms row 5) | — |
| §6 row 6, S-2 | Coherence at zero | SUPERSEDED | A-43; `U5d_WR_zero_coherence_unknowable.md` | — |
| §6 rows 8, 9, 16 | spans as prose; case text against the roster; `knows:` | RESOLVED-BY | `01_CORE_case_setup_and_beats.md`; CASE (knowledge seeded as prehistory through the fold; the prologue is five years, A-51) | `populated.py:647` |
| §6 row 12 | off-map superiors decide things | RESOLVED-BY | as M-ABROAD | — |
| §6 row 18 | the SCN loops contradict themselves on exits | RESOLVED-BY | GROUND-T (its condition, M-SUB built, is met by A-40) | — |
| S-1 | does the world itself decay | SUPERSEDED | A-40 (ground) | — |
| §7 (traits the model cannot carry) | temper; personal goals; doubt; "resonant style"; a weakness; typed relationships; sensitivity; Coherence | RESOLVED-BY | `02_CHAR_resolve_and_temper.md`, STAGED, `10_DICE_advantage_sources_for_the_arcs.md` (U5a); `14_VERBS_SOCIAL2_D_tie.md` (U5c; A-28 splits `tie` and `knot`); kin are generated (A-44, `21_PROCEDURAL_B_cast_and_seats.md`) | — |
| §8, §9 (capability; the chooser) | what the corpus implies | SUPERSEDED | U5a | — |
| §10 e1–e6 (cited items; tiers; corroboration; venue; wrong conclusions; planted evidence) | typed evidence and argument | RESOLVED-BY | CITED as reconciled; U5c's evidence carriers (EVID, ADM, VERD); e3 holds by construction; the ladder's D-44 and D-45 keep wrong conclusions to lies and forgeries | — |

---

# Part 6 — the GAME pessimist (`audits/16_PESSIMIST_GAME.md`)

Carriers: **CAUSE** = `16_PESSIMIST_GAME_standing_occasions_carry_their_cause.md`; **WDRAW** =
`16_PESSIMIST_GAME_the_world_draws.md` (as reconciled to A-54); **CONSEQ** =
`16_PESSIMIST_GAME_consequence_reading.md`.

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| F-PES-GAME-01 | the world's skeleton does not respond to its people | RESOLVED-BY | CONSEQ (the reading); the first ring (§7.2) is the order of the carriers it names | X1 |
| F-PES-GAME-02 | no consequence crosses a seam | RESOLVED-BY | CONSEQ; the ring | §1.2 seam matrix |
| F-PES-GAME-03 | the acts that close a story carry no cause | RESOLVED-BY | CAUSE | — |
| F-PES-GAME-04 | in computed play the game is a fixed function of state | RESOLVED-BY | the determinism carriers (`18_DETERMINISM_*`, closed by U5a Part 6) and each verb lane's band rows; A-24 makes the standing rule govern earlier fixed-outcome rulings | sweep C-01 to C-15 |
| F-PES-GAME-05 | the world's own motion is fixed and synchronized | RESOLVED-BY | WDRAW as reconciled, that is `09_WR_B_draws_not_thresholds.md` edits 1–2 (A-54) | 37 of 37 cohorts in step |
| F-PES-GAME-06 | rest cures starvation | RESOLVED-BY | `16_PESSIMIST_SE_A` edit 4; `03_PC_exits_withdrawal_recovery.md` Part C (U5b) | — |
| F-PES-GAME-07 | the largest news in the realm does not travel | RESOLVED-BY | U5c's FI carriers (`08_FI_02_rumour-that-travels.md`, `U5c_FI_residue.md`) under A-32 and A-33 (the seat by its reach; the death by presence, trail and telling) | the King's death held by 16, then 17 |
| F-PES-GAME-08 | a vacant seat has one route, and it is the heir's | RESOLVED-BY | `22_HAPPENINGS_B_the_throne_is_never_stranded.md` as reconciled (A-19) | X2 |
| F-PES-GAME-09 | most persons are downstream of nobody and upstream of nobody | RESOLVED-BY | none of its own: the formation proposals of each verb lane and FI's rumour; CONSEQ reads reach | reach 0.6 |
| F-PES-GAME-10 | a player-king who does nothing loses nothing | RESOLVED-BY | the ring; in particular `06_FA_decree_binds.md` (defiance has a cost) and natural death (A-15) | §2.5 |
| F-PES-GAME-11 | the provided arcs conflict with two standing rules as specified | SUPERSEDED | A-47; STAGED and `09_WR_provided_arcs.md` as reconciled | `ENDINGS_CLASSIFIED.yaml` |
| F-PES-GAME-12 | three `met` requirements are met on a channel that carries paper | RESOLVED-BY | CONSEQ | — |
| F-PES-GAME-13 | offices exist only where the cast seats them | RESOLVED-BY | `U5d_FA_owed_edits.md` §10 (every `offices.yaml` row is built, seated or vacant); the generated cast (A-44) fills them | `x5_extremes.py 0 3`: `offices=0` |
| W-1 | nobody can die of age or illness | SUPERSEDED | A-15 | 0 natural deaths in every run |
| W-2 | every harvest the same | RESOLVED-BY | plan B10-18 CL-EVENTS (2) with `09_WR_B_weather_with_memory_and_the_year.md` as reconciled (A-54) | `yield.taken` 111 at every seed |
| W-3, W-4 | who suffers in a famine; every Site decays alike | RESOLVED-BY | WDRAW as reconciled | — |
| W-5 | nobody lets an intent slip; nothing is confided | SUPERSEDED | U5a and U5c own `intent_disclosure` and `telling_privacy`; the audit's `[UNVERIFIED]` stays marked (this lane did not find a carrier that turns either on) | both draws never taken |
| G-1 | the realm is identical at every seed | SUPERSEDED | A-50 and A-44; `21_PROCEDURAL_B`, `_D` as reconciled | 22 of 22 components equal |
| G-2 | one authored situation yields the one death | SUPERSEDED | U5b (`03_PC_duel_chain_reach.md`); murder is lawful, rarely (A-16), `22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits.md` | `p_npc_013` at seeds 1 and 2 |
| G-3 | the heir, always, at once, unopposed | SUPERSEDED | A-19; sweep C-07, C-11 | X2 |
| G-4 | eighteen verbs refused at every attempt | SUPERSEDED | the verb lanes' formation proposals (U5b, U5c) | 1,585 of 7,940 acts |
| §7.2 (the first ring; the game gate) | the shortest order in which one consequence crosses one seam | RESOLVED-BY | none owed: an ordering input; its step 1 "natural death on (Jordan's)" is answered (A-15) | today every clause fails |
| J-1 | a land with no people | SUPERSEDED | the ladder's D-72 (leave a lord over an empty land) | ED-IN-0255 |
| J-2 | cohorts as full actors | SUPERSEDED | A-56; `U5d_SE_cohort_heavy_moves_and_caste.md` | X6 |
| J-3 | arcs that end on a threshold | SUPERSEDED | A-47 | — |
| J-4 | the realm is one realm | SUPERSEDED | A-50 | — |

---

# Part 8 — narrative churn (`audits/20_NARRATIVE_CHURN.md`)

Carriers: **NARR-A** = `20_NARRATIVE_A_stands_for.md`; **NARR-B** = `…_B_what_he_was_owed.md`; **NARR-C** =
`…_C_who_holds_what.md`; **NARR-D** = `…_D_his_own_side.md`; **NARR-E** = `…_E_the_year_and_the_reason.md`;
**NARR-F** = `…_F_story_inventory_and_gate.md`. (Part 7, the institutions kit, follows Part 11 in
writing order.)

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| F-NARR-01 | the regime is one value | RESOLVED-BY | NARR-A edits 1–2 (R-N1, R-N16) | H-275's term returns one value |
| F-NARR-02 | an omission has no author | RESOLVED-BY | NARR-B edits 1–4 (R-N4, R-N5, R-N13) with the story lane's R-11 (the blamed is the believed holder of the seat that may fill it) | — |
| F-NARR-03 | an office is a licence and owes nothing | RESOLVED-BY | NARR-B; plan CR-88; a seat may now also carry a modifier (A-12) | — |
| F-NARR-04 | nobody knows who holds what, so nothing is aimed | RESOLVED-BY | NARR-C edits 1–5 (R-N6) as reconciled: seat news ships realm-wide (A-32), the death apart (A-33) | 0 `held_by` claims (H-195) |
| F-NARR-05 | allegiance is fixed and no stand can cross it | RESOLVED-BY | NARR-D edits 1–4 as reconciled (A-46 un-holds edit 4 in its narrow form) | — |
| F-NARR-06 | the calendar has no year and the era has no reader | RESOLVED-BY | NARR-E edit 1 (R-N9: a roster owns the year; the weather reads it) — the owner A-51's "five years" is counted on | `world_q.season_of_year`: `len(season_factor_draw)`, shipped `()` (opened) |
| F-NARR-07 | conviction can be removed and no story reading moves | RESOLVED-BY | NARR-A (R-N1, R-N2) | the audit's ablation |
| F-NARR-08 | a change of conviction is silent and decided by rule | RESOLVED-BY | `16_PESSIMIST_CHAR_A_a_crisis_of_faith_is_drawn_and_told.md` (U5a's carrier; A-24 confirmed it), under which NARR-E edit 3 is merged and un-held | `person_q.py:903` "ROLLS NOTHING" |
| R-N1, R-N2, R-N16 | three readings of one intensity; a call-not-spread test; `regime_gain`'s row | RESOLVED-BY | NARR-A edits 1, 6, 2 | — |
| R-N3 | ED-IN-0352 against "affiliation sets odds" | RESOLVED-BY | none owed (no conflict: a flow, an era or a regime never sets odds; a person's own edges do) | — |
| R-N4, R-N5, R-N13 | a lapse laid at a door; the household's dissolving; omissions counted | RESOLVED-BY | NARR-B edits 1–4 | — |
| R-N6 | how a person learns who holds a rung | RESOLVED-BY | NARR-C | — |
| R-N7 | `release` raises regard under `stance_polarity: declared` | SUPERSEDED | the BINDING verb lane and CHAR own the polarity rule (U5c, U5a); NARR-C edit 5 and NARR-D edit 3 name it | — |
| R-N8 | eight creeds engage no pole | RESOLVED-BY | NARR-D edits 1–2 | — |
| R-N9, R-N10 | the year's length; a referent's ground | RESOLVED-BY | NARR-E edits 1, 2 | — |
| R-N11, §10 item 1 | a crisis of conviction: by rule or drawn and seen | SUPERSEDED | A-24 (D-27 taken B: drawn and seen); carrier as F-NARR-08 | ED-IN-0261 |
| R-N12, §10 item 2 | is leaving a side a strife move | SUPERSEDED | A-46 (narrow: only leaving a faction's creed or head seat); NARR-D edit 4 and `09_WR_strand_conclusion.md` edit 2 as reconciled | `strife_kinds.never` |
| R-N14 | "era" and "regime" in two senses | RESOLVED-BY | NARR-F (the reign as a reading) | — |
| R-N15 | CR-100 and CR-101 stamp the same stake for everyone | RESOLVED-BY | none owed: two preconditions, both now carried (strands conclude and are several, A-45; the regime differs, NARR-A) | — |
| H-195, H-275, H-274, H-159, H-356 | register rows re-measured | RESOLVED-BY | NARR-C; NARR-A; Part 3 (F-WR-07); NARR-B reads the clock closures | — |
| CR-76 to CR-80, CR-88, CR-91, CR-97, CR-100 to CR-103 | plan positions | RESOLVED-BY | the plan; R-N13 and R-N15 are their inputs | — |
| §4.2 (stories impossible or starved: fourteen rows) | blocked at a named link | RESOLVED-BY | the carriers of this part and of Parts 1–3; "a succession crisis: impossible by ruling" is lifted by A-15; "a war" by A-20 and A-57/A-58; "an excommunication" by `15_INSTITUTIONS_PAPACY_D_sanction_and_absolution.md`; "a debt called in" by `15_INSTITUTIONS_VENICE_B_debt_instrument.md` | — |
| §7 (the coupled narrative basis; the five pulls) | design | RESOLVED-BY | NARR-A to -F | — |

---

# Part 9 — procedural generation (`audits/21_PROCEDURAL_GENERATION.md`)

Carriers: **PROC-A** = `21_PROCEDURAL_A_worldgen_tables_and_ground.md` (PG-0, PG-1); **PROC-B** =
`…_B_cast_and_seats.md` (PG-2, PG-3); **PROC-C** = `…_C_prologue_and_case_seeds.md` (PG-4, PG-5);
**PROC-D** = `…_D_world_cards_and_churn.md` (PG-6, PG-7); **PROC-E** = `…_E_names_and_texts.md` (PG-8).

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| R-21-01 | four card receivers with four schemas | RESOLVED-BY | PROC-D (one `world_cards` schema) | — |
| R-21-02 | `build_realm` takes a seed and draws nothing from it | RESOLVED-BY | PROC-A as reconciled (A-50: some starting state drawn, small and bounded; the `variable=` arm's flip is licensed) | 22 of 22 components equal at seeds 0–2 (PES-GAME G-1) |
| R-21-03 | canon geography's fields are read by nothing | RESOLVED-BY | `07_SE_ground_and_granaries.md`; PROC-A | — |
| R-21-04 | the `npcs.yaml` header forbids invented NPCs, against a generated cast | RESOLVED-BY | PROC-B as reconciled (A-44 lifts the hold; generated persons never enter `npcs.yaml`) | ED-WR-0011 `[not re-opened]` |
| R-21-05, R-21-06, R-21-07 | trace store; solvability checked once; evidence pattern by deed kind | RESOLVED-BY | PROC-C | — |
| R-21-08 | pre-history: simulate or invent ("one simulated year") | SUPERSEDED | A-51 (five years); PROC-C as reconciled | — |
| R-21-09 | `Person.born` 0 for all 83; `heritage` unset for 79 | RESOLVED-BY | PROC-B (tier B writes both); the 46 principals' ages are owed under A-15 (`22_HAPPENINGS_A` edit 1 is the one writer of `Person.born` from authored ages) | `fixtures.py:692` |
| R-21-10 | the world builder lives under `harness/` | SUPERSEDED | U5a (a Layer 1 placement question for CORE); PROC-A adds `data/worldgen.py` only | — |
| R-21-11 | a director for pacing | RESOLVED-BY | none owed (refused by axiom); PROC-D measures a drought | — |
| R-21-12, R-21-13 | die notation in data; seed stability under table edits | RESOLVED-BY | PROC-B; PROC-A (the batch-0 probe) | — |
| PG-0 to PG-8 | the nine batches | RESOLVED-BY | PROC-A to -E, in the audit's order | — |
| D-1 | the cast: 46, or 46 plus a generated supporting cast | SUPERSEDED | A-44 (about 94 generated persons plus kin, capped) | — |
| D-2 | depth of the past | SUPERSEDED | A-51 (five years; no generational pass; no births or ageing pass ordered) | — |
| D-3 | re-arming in play | SUPERSEDED | A-52 (a docket read inside convening, after a test shows cards-at-build runs dry); PROC-D §5 as reconciled | — |
| D-4 | Thread-bearing generation | SUPERSEDED | A-40: the substrate ruling its Option A waited for is made (ground); PROC-C may generate Thread cases on Sites | — |
| D-5 | a wrong world | SUPERSEDED | A-53 (next seed by default; play-it behind a setting) | — |
| §5 (validation V1–V3) | a world that can be rejected; a bar that can fail | RESOLVED-BY | PROC-A, PROC-C (the detective gate), under A-53 | — |
| §9, §13, §14, §15 | the generated inquiry; arcs; capability; the standing rule | RESOLVED-BY | PROC-C; `12_ARCS_case_on_the_realm.md`; U1's capability home; no fixed outcome found in the kit's text by this lane's reading of the resolutions | — |

---

# Part 10 — happenings (`audits/22_HAPPENINGS.md`)

Carriers: **HAPP-A** = `22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn.md`; **HAPP-B** =
`…_B_the_throne_is_never_stranded.md`; **HAPP-C** = `…_C_a_killing_is_a_crime_someone_commits.md`;
**HAPP-D** = `…_D_batches_and_added_gates.md`. The audit's own table names a carrier for each
happening; this lane re-read that column and changed it only where a ruling did.

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| H-01 | officers seize with no cause, take no prisoner, and kill | SUPERSEDED | U5b (`14_VERBS_PHYSICAL_A_custody_and_force.md` A2, A3; `16_PESSIMIST_PC_A`); HAPP-D §2 adds the four-season gate | seeds 1, 2: 9 scenes fought, 0 custody, 3 dead |
| H-02 | nobody named dies of age, illness or enmity; everyone is zero seasons old | RESOLVED-BY | HAPP-A and HAPP-C as reconciled (A-15, A-16); PROC-B | `born` 0 for 83 of 83 |
| H-03, H-04, H-09, H-10, H-28 | refused acts; senseless aims; paperwork; villages forging; retries | SUPERSEDED | U5a and U5c (`02_CHAR_offer_what_can_be_done.md`, the formation proposals, `16_PESSIMIST_CORE_a_refusal_is_remembered.md`); H-10 also by `U5d_SE_cohort_heavy_moves_and_caste.md` (A-56) | 322 refusal Events on 749 acts |
| H-05, H-27 | the world is the same whether anyone acts; a player-king who does nothing loses nothing | RESOLVED-BY | `16_PESSIMIST_GAME_consequence_reading.md`; NARR-B | F-PES-GAME-01, -10 |
| H-06, H-16, H-17, H-18, H-20, H-32 | certain outcomes; verdicts; lies; hearings; two dice; acts that write nothing | SUPERSEDED | U5a (determinism, DICE) and U5c (SC, LACUNA); a convict no longer ends his own sentence (A-37) | F-PES-GAME-04 |
| H-07 | no seat changes hands, no one changes side, no oath is paid, no writ is obeyed | RESOLVED-BY | Part 1 (DECREE, VB-C, VB-D); NARR-A to -F | 0 of 193 writs complied with |
| H-08, H-19, H-34 | everyone behaves alike; a silent crisis; no reaction to being attacked | SUPERSEDED | U5a (`16_PESSIMIST_CHAR_A`, `_B`; `02_CHAR_relations_have_a_ground.md`) | F-PES-CHAR-01, -03 |
| H-11, H-12 | no duel is fought; a fight is two blows | SUPERSEDED | U5b (`03_PC_duel_chain_reach.md`, `03_PC_duel_round_and_approach_B.md`; A-31 longer fights) | 48 of 48 challenges refused |
| H-13 | anyone declares war; marches meet nobody; a defended field is always lost | RESOLVED-BY | `16_PESSIMIST_FA_B` edit 4; `06_FA_war_lives_in_seats_B.md` (A-20); the field's scale is U5b's | F-PES-FA-05 |
| H-14, H-15, H-29, H-30 | every town the same; rest cures starvation; a hunger death by nothing; id-order feeding | RESOLVED-BY | Part 2 (GROUND, PES-SE-A); `09_WR_B_draws_not_thresholds.md` (A-54); PROC-A | — |
| H-21 | no crime is ever committed, so no case can begin | RESOLVED-BY | HAPP-C as reconciled (A-16); PROC-C; U5c's paper and case carriers | `fight` 0 |
| H-22 | news does not travel | SUPERSEDED | U5c (`08_FI_02`, `16_PESSIMIST_FI_A`); A-32, A-33 | a death known to 16 of 82 |
| H-23 | the King cannot dismiss as King; a dismissal is permanent | RESOLVED-BY | `16_PESSIMIST_FA_A_dismissal_survives_the_king.md` | F-PES-FA-02 |
| H-24 | the throne can be stranded; a consort can seat herself as Confessor; a cohort can be King | RESOLVED-BY | HAPP-B as reconciled (A-19); `16_PESSIMIST_FA_B` edits 1–2 | F-PES-FA-01 |
| H-25 | the King lives in a cottage apart from his Queen | RESOLVED-BY | HAPP-D §3 (the homes); `16_PESSIMIST_FA_C` makes governance independent of residence | `npcs.yaml` rows |
| H-26 | the world never ends and never ends differently | RESOLVED-BY | Part 3 (STRAND, READ-B, DRAWS edit 3) | `endings == []` |
| H-31 | armour does not turn a blade; a second garrison adds nothing | RESOLVED-BY | walls: `16_PESSIMIST_SE_B` edit 3; armour: `16_PESSIMIST_PC_D_armour_turns_a_blade_by_a_draw.md` (U5b; the audit said "no proposal identified here", and one exists) | — |
| H-33 | the record cannot retell | RESOLVED-BY | `16_PESSIMIST_GAME_standing_occasions_carry_their_cause.md`; `16_PESSIMIST_CORE_the_record_holds_what_changed.md` (U5a) | — |
| §1 (the King's death, re-run and explained) | he dies at seed 2 in the fourth season, seized by his Spymaster | RESOLVED-BY | as H-01; the corrections of §5 | `runs/HAPPEN/king_2.json` `[not re-opened]` |
| §3 (batches 1–8) | the landing order | RESOLVED-BY | HAPP-D | — |
| §4 item 1 | natural death on or off | SUPERSEDED | A-15 (on, after the 46 ages are authored) | — |
| §4 item 2 | may a person commit a killing | SUPERSEDED | A-16 (yes, rarely) | ED-IN-0337 |
| §4 item 3 | who may claim the throne when the line fails | SUPERSEDED | A-19 (the deed race: heir, consort, princess and both houses' heads; the founding order a head start) | — |
| §5 (four corrections owed in files this lane does not edit) | "King dies tick 0 in all seeds" and three others | RESOLVED-BY | recorded here as the standing correction (the digest and the two audits are not edited by a closure lane: their findings stay; the correction is this row); the PHYSICAL_A gate line is HAPP-D §2's and U5b's | the audit's §1.1 reproduction |

---

# Part 11 — story enablement (`audits/23_STORY_ENABLEMENT.md`)

Carriers: **STORY-A** = `23_STORY_A_what_a_roll_leaves.md`; **STORY-B** = `…_B_a_house_continues.md`;
**STORY-C** = `…_C_a_founded_place_can_fail.md`; **STORY-D** = `…_D_story_census_and_gate.md`; **STORY-E** =
`…_E_first_playable_the_lean_year.md`. The audit's subject is the 73 stories S-01 to S-73, the nineteen
carried mechanisms, three gaps, eleven batches and its decisions.

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| M1, M2, M3 (the floor) | the offer makes sense; the act is drawn and every band writes; the record keeps cause, value and margin | SUPERSEDED | U5a and U5c carriers named in the audit's §3; `16_PESSIMIST_GAME_standing_occasions_carry_their_cause.md` | 1,585 of 7,940 acts refused at every attempt |
| M4, M11, M12 | news with a name; a trail and a conclusion; a hearing that binds and ends | SUPERSEDED | U5c | — |
| M5 | regard moves with deeds and dues, and has a ground | RESOLVED-BY | NARR-A to -D; U5a's CHAR carriers | — |
| M6, M7 | seats pass by a draw; an order is answered by a draw | RESOLVED-BY | Part 1; HAPP-B; VB-C, VB-D | — |
| M8 | bodies and time | RESOLVED-BY | HAPP-A; `16_PESSIMIST_WR_C`; `09_WR_B_weather_with_memory_and_the_year.md`; NARR-E edit 1 (all as reconciled: A-15, A-54) | — |
| M9 | places differ and stores bind | RESOLVED-BY | Part 2 | — |
| M10, M13, M15 | violence with a cause and a mercy; a field that can be won; capability differs and grows | SUPERSEDED | U5b and U5a; the land and seats a field wins are `U5d_FA_land_and_seats_pass_on_a_won_march.md` | 0 `field.won` in any run |
| M14 | the interior draws | SUPERSEDED | U5a (PES-CHAR-A, -C); `12_ARCS_arcs_as_staged_goals.md` | — |
| M16 | instruments and ties | RESOLVED-BY | Part 7 (the institutions kit) | — |
| M17 | the world strains, breaks and ends | RESOLVED-BY | Part 3 | — |
| M18 | a scene runs in its own order | SUPERSEDED | A-9 (a short sequence); `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md` (U5a); S-67 no longer waits | — |
| M19 | a seat can read it | RESOLVED-BY | Part 4 (WHY; SURF-B) | `Seen.why` is `None` |
| G1 | what a roll leaves | RESOLVED-BY | STORY-A edits 1–4 as reconciled (A-5: the margin is the one sampler's; A-38 for whom a verdict names) | margin discarded |
| G2 | a house continues | RESOLVED-BY | STORY-B edits 1–4 as reconciled: the marriage and the majority land; `majority_age` goes live with the authored ages (A-15); births stay behind `birth_rate` at 0 (J-1) | persons never increase |
| G3 | a founded place can fail | RESOLVED-BY | STORY-C as reconciled (A-55) | — |
| S-01 to S-73 (the inventory) | each story completes when its mechanisms land | RESOLVED-BY | by batch, the audit's §6.2: E-2 (S-60, 68, 69, 71, 72, and S-67 now that A-9 is ruled), E-3 (S-01, 31, 32, 34, 35, 36, 40, 66), E-4 (S-02, 29, 33, 37, 52, 57, 70, 73), E-5 (S-04, 05, 06, 07, 10, 15, 16), E-6 (S-08, 27, 28), E-7 (S-03, 09, 12, 30, 43–47, 49, 51, 53–56), E-8 (S-14, 20–26), E-9 (S-59, 61, 63, 64, 65), E-10 (S-11, 13, 17, 18, 19, 48, 50, 62), E-11 (S-38, 39, 41, 42); STORY-D is the reading that gates each | `runs/STORY/p2_count.py` `[not re-run]` |
| S-58 | a planted clue that misleads | SUPERSEDED | decided out (R-10); the ladder's D-44 and D-45 agree (no engine-authored wrong conclusions) | K-37 |
| E-0 to E-11 | the batches and their gates | RESOLVED-BY | STORY-D (the gate every batch uses) and the batch table as reconciled in STORY-D's head line | — |
| §6.3 (thirteen places intent meets Layer 1) | named at the site | RESOLVED-BY | none owed by this lane except three that rulings moved: "arcs that end when a counter fires" (A-47), "natural death … the shape lands dark" (A-15: live), "chains inside a scene" (A-9) | — |
| R-01, R-02, R-03, R-04, R-13, R-14, R-15, R-16, R-17, R-19, R-20 | decided by the ladder | RESOLVED-BY | as the audit's table (STORY-A, -C, -D, -E; §5; §6) | — |
| R-05 | the deposition of a crowned or anointed head | RESOLVED-BY | none new: conquest (`U5d_FA_land_and_seats_pass_on_a_won_march.md`, for a head whose seat is anchored on a march-target rung), a sentence his sworn men each answer (`15_INSTITUTIONS_PAPACY_D`), CR-37; the Confessor is judged by nobody (A-36), so "by a College after a crisis" does not reach him | — |
| R-06 | what a regency is | RESOLVED-BY | STORY-B edit 4; HAPP-B (Partial) | — |
| R-07 | a besieged town's larder | RESOLVED-BY | `U5d_STORY_owed_edits.md` §1 (a constraint on `07_SE_campaign_supply_and_muster.md`) | — |
| R-08 | a burned granary | RESOLVED-BY | `U5d_STORY_owed_edits.md` §2 (owed at the MATERIAL lane's `sabotage` row) | — |
| R-09 | a hoarder, a profiteer | RESOLVED-BY | none owed (no price mechanism; told as relief withheld and a debt on terms) | — |
| R-10 | a planted clue | RESOLVED-BY | none owed (out of plan) | — |
| R-11 | who is blamed for a due that lapses under an empty seat | RESOLVED-BY | `U5d_STORY_owed_edits.md` §3 (an amendment to NARR-B's `dues_unmet`) | — |
| R-12 | an ambush: the opener's edge | RESOLVED-BY | `U5d_STORY_owed_edits.md` §4; the ladder's D-41 takes it (a first-exchange edge on an unexpected opener, following A-16) | — |
| R-18 | refugees need a population that can move | SUPERSEDED | A-56; `U5d_SE_cohort_heavy_moves_and_caste.md` | — |
| R-21 | two men who kill each other | RESOLVED-BY | `U5d_STORY_owed_edits.md` §5 (owed at PC's owner) | 0 of 5,000 |
| J-1 | are named persons born in play | JORDAN | (a) births on, in STORY-B's shape behind `birth_rate`: houses continue or fail, a regency has a child at its centre, the cast grows; (b) no births: the cast is what the build and the prologue made, minors come of age, every line is finite. Not answered by A-15 (deaths) or A-51 (which orders no births or ageing pass for the prologue). STORY-B's marriage and majority land under either | — |
| §8.3 (twelve items "already Jordan's") | defaults under which no batch waited | SUPERSEDED | eleven are answered: A-15, A-16, A-19, A-24 (D-27, D-28), A-9, A-46, A-55, A-38, A-33 and the ladder's D-69; where the answer differs from the plan's default the batch is re-read in STORY-D's head line (A-9: S-67 completes in E-2; A-46: the Split is a strife move; A-38: the verdict names the petitioner). One stays open: the form of fortune in a field (D-34, held for `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md`; U5b's) | — |

---

# Part 7 — the institutions kit (`audits/15_INSTITUTIONS_*.md`)

These five documents are designs and plans in proposal form; their closable items are the collision
ledger, the Layer 1 meetings, each lane's decided resolutions and survivors, and the re-grounding
additions. Carriers: **SYN-A…E** = `15_INSTITUTIONS_SYNTHESIS_A…E_*.md`; **VEN-A…D**, **VEN-E** (the
grounding file `…VENICE_grounding_E_what_the_tree_adds.md`); **COL-A…E**, **COL-F** (`…COLONIAL_grounding_F_…`);
**PAP-A…F**, **PAP-G** (`…PAPACY_grounding_mechanisms.md`); **BYZ-A…F**, **BYZ-G**
(`…BYZANTINE_grounding_mechanisms.md`). Re-grounding status at the time of writing: all four grounding
proposals exist on disk; PAP-G and BYZ-G carry their own table of the rulings; VEN-E and COL-F cited
none and carry this lane's `Reconciled:` line. The Venice, Medici and colonial re-grounding sections
(§17, §16) were read at their headings and their proposals' outlines only (see Coverage).

## 7.1 `audits/15_INSTITUTIONS_SYNTHESIS.md`

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| X-01 to X-11 | registries, records and the founding order: one `instruments.yaml`; no rival roster of forms; a certificate is a Record with `recites`; one meaning of "roll"; the order as seeded deeds (3, 2, 1); one `legitimacy` function; `presumption_gain` ships 0; two keepers; `debt`; `charter` and `staple`; `warrant` and `commission` | RESOLVED-BY | SYN-A edit 1; SYN-B; the family files' own `Reconciled:` lines (audit §2.1's last column) | the ledger's rows, read at 105 characters a cell |
| X-12 to X-18 | seat rows, bodies, procedures: `audit_at_exit`; one far superior `off_altonian_court`; two distances; the ballot is SC's; two non-collisions; Hafenmark's heir title | RESOLVED-BY | COL-C, VEN-C, BYZ-D, COL-B, PAP-B (as reconciled); X-15 on A-14; X-16, X-17 are STALE-FALSE-POSITIVE by the audit's own finding (not collisions); X-18 by COL-D edit 4 | — |
| X-19 to X-22, X-30 | obstacle terms and fixtures: named terms for BYZ's steps; `oath_step` withdrawn; `provisional_term` is VB-C's; one control style; one currency model | RESOLVED-BY | SYN-A §3.4 to §3.6; `U5c_SC_one_obstacle_form.md` (the one composer); the dignity "precedence" step dropped by X-19 is lawful again under A-12 and is not re-added (BYZ-A as reconciled) | — |
| X-23 to X-29 | verb rows rewritten by more than one lane (`confer`, `revoke`, `succeed`, `issue`, `carry`, `requisition`, `transfer`, `seize`, the answer to a writ) | SUPERSEDED | the verb lanes own each row (U5c: VB-C, VB-D, SOCIAL1-B, -D, MATERIAL-B, -D); the kit supplies terms | audit §3.5 |
| X-31, X-32, X-33 | `person_q.excused`; one scenario style; a form's `basis` | RESOLVED-BY | SYN-C edit 1; SYN-D §1; PAP-D (A-21, A-22 rule the two bases) | — |
| items listed outside the four families (three names for distance; `rank_gap` against `standing`; the content key `standing`; three names for the graded route; `dues_unmet` against `breaches`) | names that collide across lanes | SUPERSEDED | U5c's conflict ledger (`unified/U5_CONFLICTS_U5c.md`) and `U5c_SC_one_obstacle_form.md`; `dues_unmet` and `breaches` stay two halves (NARR-B reads the oath, COL-A the instrument) `[unverified that U5c lists each]` | — |
| §3, §5, §6, §7 (the one kit; the interlock map; structural conflicts; the commensuration test) | design | RESOLVED-BY | SYN-A, SYN-C, SYN-D | — |
| §4 (the deed ledger), §4.6 (canon wording A1 to A4) | legitimacy as believed deeds; the canon amendment drafted | RESOLVED-BY | SYN-B as reconciled; the canon edit is owed by A-17 and applied by no suite lane | `canon/03_canonical_timeline.md:76, :90, :96` `[not re-opened]` |
| §8.1 (the Layer 1 statement, fourteen rows) | the kit against AX-1, AX-2, AX-4, T-k, AX-5, AX-6, §B.7, §B.8, §B.13, §C.11 | RESOLVED-BY | SYN-A (no module, no stored quantity, no trigger); two rows change by ruling: "§B.7 a seat adds no verb and no modifier" (A-12) and the `Seat` tuple (A-13); amendment texts owed, not applied | `04_CODE_ARCHITECTURE.md` §B.7 `[not re-opened by this lane]` |
| L-1 | intent "office" as a modifier against §B.7 | SUPERSEDED | A-12 | — |
| L-2 | seats that are paid, routed and audited against the `Seat` tuple | SUPERSEDED | A-13 | — |
| L-3 | a vote may not be a count of commitments | SUPERSEDED | A-14 | — |
| L-4 | `dues`, `audits_due`, `hands_open`, `recalls` read the World to hand a person a referent | DISPUTED | the audit grades it CONVENTION and names it without resolving; this lane's evidence: `world_q.vacancies` does the same today and Layer 1 accepts it as the occasion pattern, so no edit is planned; the finding stays for U2's conformance matrix | `queries/world_q.py` (`vacancies`) `[not re-opened]` |
| L-5 | "a registered module" against institutions as the loop's verbs | SUPERSEDED | A-10 | — |
| §9 (the implementation plan, batches I-0 to I-9) | the kit's landing order | RESOLVED-BY | SYN-E as reconciled | — |
| §10 item 1 | the south's part in the Secession War | SUPERSEDED | A-17, A-18 | — |
| §10 item 2 | may the head of the Church strip a Church officer | SUPERSEDED | A-35; PAP-B item 4 un-held | — |
| §10 item 3 | can anyone judge the Confessor | SUPERSEDED | A-36 (nobody; the council is dropped) | — |
| §10 item 4 | forced labour keyed on caste | SUPERSEDED | A-41 (neither option; regard, vote blocks, informal tiers), A-42; `U5d_SE_cohort_heavy_moves_and_caste.md` | — |
| §10 "closed here" (eight family items) | answerable at issue or entry; the empire's names; a barred order; lay investiture; a roll closed by blood; Schoenland; a house as its own faction; sale of office | RESOLVED-BY | as the audit's table (per-row keys and content; no form `purchase`); the register lists them as answered ("Not yours") | — |
| §10 "carried" (four open questions of other lanes) | proclaimed or delivered; orders down the chain; swearing to a seat; governance's home | SUPERSEDED | A-21; A-22; the ladder's D-31 under A-24 (a draw against the seat); A-10 | — |

## 7.2 The four family audits

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| VENICE §14.1 resolutions 1–14 | the debt un-deferred; no creditor's lever; ballots drawn; `lot`; `binds_bases`; terms by body; Schoenland authored; a house head as the actor; kind-denominated instruments; no purchase basis; the roll by warrant; Key-era hooks irrelevant; a suspended act returns to the docket | RESOLVED-BY | VEN-B (1–3, 10), VEN-C (4–7, 12, 13), VEN-D (8, 9, 14); 11 none owed | — |
| VENICE §14.2 items 1–3 | a roll closed by blood; Schoenland's constitution; a house on a hearth with no faction | RESOLVED-BY | closed by the synthesis (§10 table): no; authored as marked assumption (VEN-D); every house belongs to a faction | — |
| VENICE §17 (re-grounding: corrections; mechanisms M-1 to M-13; what stays memory-grade) | what the tree's research adds | RESOLVED-BY | VEN-E edits 1–7 as reconciled; memory-grade claims stay marked in the audit and are relied on by no edit `[section read at its headings]` | `unified/RESEARCH_MAP_INSTITUTIONS_B.md` `[not opened]` |
| COLONIAL §11 item 1 | the canon sentence on the south | SUPERSEDED | A-17 | — |
| COLONIAL §11 item 2 | may an office be sold | RESOLVED-BY | closed by the synthesis (composed `transfer` then `confer`; no `purchase` form) | #453 row 38 `[not re-opened]` |
| COLONIAL §11 item 3 | forced labour keyed on caste | SUPERSEDED | A-41 | — |
| COLONIAL §3 to §10, §12 to §14 (distance; the play-facing model; the accomplishment ledger; verbs; scenario; plan) | design | RESOLVED-BY | COL-A to -E as reconciled (COL-D's hold released by A-17; its edit 5 rewritten on the land rulings) | — |
| COLONIAL §16 (re-grounding: corrections; mechanisms M-14 to M-28) | what the tree's research adds | RESOLVED-BY | COL-F edits 1–8 as reconciled `[section read at its headings]` | — |
| PAPACY F-PAP-01 to F-PAP-10 | the audit's findings on what the tree holds (among them: the Confessor housed in a market, -04; `off_cardinal_fortitude` commanding through the unruled `dispatch`, -08; a verdict by count, -09; an absent party judged, -10) | RESOLVED-BY | PAP-A (R-1, R-4, R-5, R-14), PAP-B (R-3, R-6, R-9), PAP-C (R-2, R-12, R-13, R-17), PAP-D (R-7, R-8, R-16) `[F-PAP-01, -02, -03, -05, -06, -07 were not opened one by one; they are closed through the resolution rows that cite them]` | — |
| PAPACY R-1 to R-17 | seventeen decided resolutions | RESOLVED-BY | as above; R-10, R-15 none owed; R-11 (the canon sentence) SUPERSEDED in effect by A-17 | — |
| PAPACY §13 item 1 | the head strips an officer | SUPERSEDED | A-35 | — |
| PAPACY §13 item 2 | judging the Confessor | SUPERSEDED | A-36; PAP-E item 5 and procedure P-13 dropped | — |
| PAPACY §13 item 3 | lay investiture on ducal ground | RESOLVED-BY | closed by the synthesis (per-row `patronage` content) | — |
| PAPACY §13 item 4 (a note) | canon lines and the attestation counts | SUPERSEDED | A-17, A-18 for the order; the counts stay Jordan's content | — |
| PAPACY §15 (re-grounding) | what the tree's research adds | RESOLVED-BY | PAP-G items 1–8 (its own rulings table folds A-13, A-14, A-21, A-35, A-36, A-37) | — |
| BYZANTINE §14 item 1 | an order answerable at issue or at entry | RESOLVED-BY | BYZ-C as reconciled (a per-row key; under A-21 the terms travel with the news and the hands act on the entered instrument) | — |
| BYZANTINE §14 item 2 | who credits Varfell's deed | SUPERSEDED | A-18 | — |
| BYZANTINE §14 item 3 | the names at the empire's centre | RESOLVED-BY | BYZ-D (placeholders marked; names are content) | — |
| BYZANTINE §14 item 4 | a barred order for the bureaux | RESOLVED-BY | closed by the synthesis (no bar; the deed order bars a clerk by his odds) and by the audit's own re-grounding note (the 2026-07-12 closure ruled the form) | — |
| BYZANTINE §17 (the standing rule checked), §18 (re-grounding) | fixed outcomes in its own text; what the research adds | RESOLVED-BY | BYZ-A to -F as reconciled by the synthesis (X-19, X-22); BYZ-G items 1–5 (its own rulings table folds A-12, A-13, A-17, A-18, A-21) | — |

---

# Part 12 — the determinism sweep (`audits/18_DETERMINISM_SWEEP.md`)

U5a closed the sweep row by row (`unified/U5_FINDINGS_CLOSURE_U5a.md` Part 6: D-01 to D-11, C-01 to
C-15, and §3's nine items). Those dispositions stand and are not repeated. The rows it handed to this
family:

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| D-07 | a levy raises as asked | RESOLVED-BY | `06_FA_levy_through_the_seat_B.md` (eligibility only; the turnout is `recruit`'s graded draw, U5b) | the file's D-07 note |
| D-08 | succession and set-up acts certain | RESOLVED-BY | `06_FA_playable_scenario.md` as reconciled (A-19); VB-C | — |
| D-09 | inheritance by rule | SUPERSEDED | A-19 (the deed race); `22_HAPPENINGS_B` | — |
| D-10 | "governing acts do not roll" | RESOLVED-BY | overruled in `07_SE_audit_addendum_B.md`; the route is `18_DETERMINISM_task_draw_for_uncontested_verbs.md`; a steward's skill bears on the harvest draw (A-54) | — |
| C-07 (FA's share) | the binding acts take effect with certainty | RESOLVED-BY | VB-C, VB-D (U5c) with Part 1's carriers | `issue` 49, `release` 4 |
| §3: WR's thresholds become draws | — | RESOLVED-BY | `09_WR_B_draws_not_thresholds.md` (A-54 confirms the form) | — |
| §3: the institutions' deterministic text | — | RESOLVED-BY | the synthesis's X-19, X-22 and each family file's `Reconciled:` line; PAP's R-16 refuses the automatic sentence | — |
| §3: the GAME pessimist's count | one definition of a draw | RESOLVED-BY | an Event that carries a degree (the sweep's own); `16_PESSIMIST_GAME_consequence_reading.md` reads on it | 7.8 to 10.8% of acts drawn |
| `:110` (`world_q.subsistence_draw` listed as drawn) | the SE pessimist reads it as arithmetic | DISPUTED | both readings recorded (`U5d_SE_owed_edits.md` §8); this lane did not open the function; settled in effect when the hungry body is drawn (`09_WR_B_draws_not_thresholds.md` edit 2) | `[not re-opened]` |

---

# Part 13 — the land rulings (A-57, A-58, A-65 to A-70), which arrived during this closure

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| D-20 as re-ruled | what a won battle does to land and seats | RESOLVED-BY | LAND (`U5d_FA_land_and_seats_pass_on_a_won_march.md`): rules 1–9, edits 1–7 | `_eff_march`, `_seize_rung`, `_take_hold`, `occupies`, `gate.py:291-300` (each opened) |
| `26_MASS_BATTLE_aggression_and_land.md` §3 row 5 (the uninvited rescuer) | does the land pass when the beaten army was not the holder's | SUPERSEDED | A-65, A-66 (he chooses); LAND rule 4 | — |
| the same file §2, §4 (an unopposed entry; a drawn aggressor's station; a drawn defender; what is carried home; leave and a guest; presence by leave) | open land cases | SUPERSEDED | A-67 to A-70; LAND rules 5–8, decisions D5, D6, D8 | — |
| A-66's marked assumption | is seizure a default or an act the victor forms | RESOLVED-BY | LAND, "The settled rules" 1–2: confirmed at the owner; `seize` is the existing act | `_seize_rung` docstring |
| A-68's marked assumption (the parliament's referent) | "the kingdom parliament is functional" has no working state in code | JORDAN | (A) the Court Parliament when it is built (the rule waits; until then every unopposed entry is read on tension, regard and war alone); (B) any working realm bench stands in now (`world_q.parliament_sits`, built behind a fixture). LAND builds (B) switchable to (A) | body `Court Parliament` in `rosters.yaml: office_bodies`; arrangement `parliamentary_debate`; no seat in the body; `offices.yaml:150` "RULED AND NOT BUILT, H-90" (all opened) |

Listed for other families (not edited by this lane; each assumed title passes only by a separate act or
by presence, and is now consistent with A-66 or needs one line): `04_MB_playable_field_scenario.md:57`
(its end condition "`seize` after occupation" agrees with A-66 and should add the seats, U5b);
`14_VERBS_MATERIAL_D_paper.md` §6 (`seize` of an occupied place gains the seats and the leave
conjunct, U5c); `14_VERBS_MILITARY_A_movement.md` (an unopposed arrival takes the entry draw, U5b).

---

# Proposals this lane wrote (carriers for findings that had none, and for rulings with no carrier)

| file | what it carries |
|---|---|
| `U5d_FA_land_and_seats_pass_on_a_won_march.md` | the title write under the land rulings A-57, A-58, A-65 to A-70: a field writes presence; the victor seizes, occupies or withdraws; a seizure carries the seats; leave is not occupation; the unopposed entry's graded reading; the parliament's referent (flagged) |
| `U5d_FA_owed_edits.md` | ten FA items: the consort's remit with the deed race; custody suspends acts through a seat (A-23); the head's strip and the Confessor's exemption (A-35, A-36); faction weight on the authored franchise (A-42); what an order orders; one purse per rung; register re-grades; one head per faction; a writ is the seat's; a seat exists whether or not it is filled |
| `U5d_SE_owed_edits.md` | ten SE items decided with no file (register edits, CR-49's class, `Rung.envelope`, the ration's kinds, the relief ladder's top, builder notes, trade kinds, the sweep's one line, readers or deletions, the stocking gate arm) |
| `U5d_SE_cohort_heavy_moves_and_caste.md` | A-56 (a cohort forms seven heavy moves; the `riot` row) and A-41 / A-42 (caste in regard, vote blocks and a practice table of informal tiers) |
| `U5d_WR_owed_edits.md` | an execution read as a killing; the order in which WR's draws land; a believed wound cleared; one roster sentence |
| `U5d_WR_zero_coherence_unknowable.md` | A-43: legibility as the one dial on what others read of a practitioner; continuity kept |
| `U5d_GO_owed_edits.md` | the save snapshot with a round-trip gate (F-GO-09); two cross-lane orders; one card line |
| `U5d_STORY_owed_edits.md` | five story decisions that named an owner and no file (a besieged larder, a burned granary, blame under an empty seat, the opener's edge, a mutual felling) |

# Part R — rulings folded into existing proposals

Ninety-two proposals carry a head line `Reconciled: 2026-11-12, U5d closure — …` that names the ruling
and the steps rewritten; the author's line is kept in every file and no finding was deleted. By ruling
(the files' own lines are the record; this table is an index):

| ruling | folded into |
|---|---|
| A-5 (bell curve), A-7 (two inputs) | `11_GO_one_draw_owner`, `11_GO_port_gate_order_and_coverage`, `16_PESSIMIST_GO_keyed_draw_no_recorder`, `09_WR_threadwork_module`, `09_WR_B_threadwork_session_and_practitioner`, `16_PESSIMIST_WR_A`, `23_STORY_A`, `15_…PAPACY_C`, `_F`, `06_FA_office_capabilities` |
| A-9, A-48 (a scene is a short sequence; the slate) | `11_GO_player_surface_contract_B`, `11_GO_fidelity_and_campaign_modes`, `23_STORY_A`, `23_STORY_D` |
| A-10 (governance is the loop's verbs) | `06_FA_playable_scenario`, `06_FA_shortest_loop_B`, `15_…SYNTHESIS_A`, `_D` |
| A-12 (a seat may carry a modifier), A-13 (three seat facts) | `06_FA_office_capabilities`, `07_SE_capability_rate_B`, `07_SE_capability_and_chooser_surface`, `07_SE_arc_needs`, `20_NARRATIVE_B`, `15_…SYNTHESIS_A`, `_D`, `_E`, `15_…BYZANTINE_A`, `_B`, `_C`, `15_…COLONIAL_C`, `15_…VENICE_C`, `…VENICE_grounding_E` |
| A-14 (a vote is a draw on the voter) | `06_FA_seat_terms_and_turnover`, `15_…PAPACY_B`, `_F`, `15_…VENICE_C`, `15_…SYNTHESIS_A`, `_D`, `…VENICE_grounding_E` |
| A-15 (natural death on) | `06_FA_seat_terms_and_turnover`, `06_FA_seat_terms_by_body_B`, `07_SE_population_census`, `09_WR_provided_arcs`, `16_PESSIMIST_WR_C`, `20_NARRATIVE_F`, `21_PROCEDURAL_B`, `_C`, `22_HAPPENINGS_A`, `_D`, `23_STORY_B`, `_D`, `15_…BYZANTINE_E`, `15_…PAPACY_F`, `16_PESSIMIST_GAME_consequence_reading` |
| A-16 (murder, rarely) | `12_ARCS_arcs_as_staged_goals`, `21_PROCEDURAL_C`, `22_HAPPENINGS_C`, `_D`, `23_STORY_D` |
| A-17, A-18 (the south; Varfell's deed) | `15_…SYNTHESIS_B`, `15_…COLONIAL_D`, `…COLONIAL_grounding_F`, `15_…PAPACY_C`, `15_…BYZANTINE_A` |
| A-19 (the crown by the deed race) | `06_FA_playable_scenario`, `06_FA_remit_grant_by_row`, `16_PESSIMIST_FA_A`, `_B`, `21_PROCEDURAL_B`, `22_HAPPENINGS_B`, `_D`, `23_STORY_B`, `_D`, `15_…SYNTHESIS_B`, `15_…COLONIAL_D`, `15_…BYZANTINE_E`, `16_PESSIMIST_GAME_consequence_reading` |
| A-20 (war lives in the seats that wage it) | `06_FA_war_lives_in_seats_B`, `16_PESSIMIST_FA_B` |
| A-21 (decrees proclaimed), A-22 (command) | `06_FA_decree_binds`, `06_FA_levy_through_the_seat_B`, `06_FA_playable_scenario`, `16_PESSIMIST_FA_C`, `15_…SYNTHESIS_A`, `15_…PAPACY_D`, `15_…BYZANTINE_C`, `_D`, `15_…COLONIAL_A`, `_B`, `…COLONIAL_grounding_F` |
| A-23 (custody suspends the seat) | `06_FA_decree_binds`, `06_FA_remit_grant_by_row`, `07_SE_treasury_granary_B`, `20_NARRATIVE_B`, `22_HAPPENINGS_B`, `_C`, `15_…SYNTHESIS_C` |
| A-24 (the standing rule over earlier rulings) | `06_FA_decree_binds`, `12_ARCS_cited_evidence`, `20_NARRATIVE_E`, `15_…VENICE_C`, `23_STORY_D` |
| A-29, A-30 (floats; one draw per key) | `11_GO_float_contract`, `11_GO_one_draw_owner`, `11_GO_port_gate_order_and_coverage`, `16_PESSIMIST_GO_keyed_draw_no_recorder` |
| A-32, A-33 (seat news; death news apart) | `16_PESSIMIST_GO_the_offer_names_what_is_held`, `09_WR_B_chronicle_that_tells`, `20_NARRATIVE_C`, `21_PROCEDURAL_C`, `22_HAPPENINGS_A`, `_B`, `16_PESSIMIST_GAME_standing_occasions_carry_their_cause` |
| A-35, A-36 (the head strips an officer; nobody judges the Confessor) | `06_FA_seat_terms_and_turnover`, `06_FA_seat_terms_by_body_B`, `15_…PAPACY_B`, `_D`, `_E`, `_F`, `15_…SYNTHESIS_C`, `_E`, `15_…BYZANTINE_E` |
| A-37, A-38, A-39 | `16_PESSIMIST_FA_A`, `15_…PAPACY_D`, `15_…COLONIAL_A`, `23_STORY_A`, `_D`, `12_ARCS_cited_evidence` |
| A-40 (the wear is ground), A-43 (zero coherence) | `09_WR_world_motion`, `09_WR_threadwork_module`, `09_WR_B_threadwork_session_and_practitioner`, `09_WR_B_chronicle_that_tells`, `16_PESSIMIST_WR_B`, `_D`, `12_ARCS_substrate_as_ground`, `21_PROCEDURAL_C`, `11_GO_player_surface_contract_B` |
| A-41, A-42 (caste; franchise) | `15_…SYNTHESIS_A`, `_E`, `15_…COLONIAL_A`, `…COLONIAL_grounding_F`, `15_…VENICE_C`, `21_PROCEDURAL_B` |
| A-44 (generated cast) | `12_ARCS_case_on_the_realm`, `21_PROCEDURAL_B`, `23_STORY_B` |
| A-45, A-46 (strife strands; the Split) | `09_WR_strand_conclusion`, `09_WR_B_readings_of_closure_and_tension`, `20_NARRATIVE_D`, `_F`, `23_STORY_D` |
| A-47 (a threshold opens a mandatory scene) | `06_FA_decree_binds`, `06_FA_shortest_loop_B`, `09_WR_provided_arcs`, `09_WR_B_draws_not_thresholds`, `16_PESSIMIST_WR_D`, `12_ARCS_arcs_as_staged_goals`, `16_PESSIMIST_GAME_standing_occasions_carry_their_cause`, `21_PROCEDURAL_D`, `11_GO_player_surface_contract_B` |
| A-49 (the end reveal) | `11_GO_fidelity_and_campaign_modes`, `09_WR_B_chronicle_that_tells` |
| A-50 (seeded start), A-53 | `07_SE_ground_and_granaries`, `07_SE_valley_scenario`, `12_ARCS_case_on_the_realm`, `21_PROCEDURAL_A`, `_D`, `23_STORY_E`, `11_GO_fidelity_and_campaign_modes` |
| A-51 (the five-year prologue) | `07_SE_population_regrowth_B`, `12_ARCS_case_on_the_realm`, `20_NARRATIVE_E`, `21_PROCEDURAL_A`, `_C`, `22_HAPPENINGS_A`, `23_STORY_B`, `_D`, `_E` |
| A-52 (the docket after its test) | `21_PROCEDURAL_D` |
| A-54 (world motion on the four-band ladder) | `07_SE_ground_and_granaries`, `07_SE_capability_rate_B`, `07_SE_valley_scenario`, `16_PESSIMIST_SE_B`, `16_PESSIMIST_GAME_the_world_draws`, `09_WR_world_motion`, `09_WR_B_weather_with_memory_and_the_year`, `09_WR_B_draws_not_thresholds`, `16_PESSIMIST_WR_A`, `_B`, `20_NARRATIVE_E`, `21_PROCEDURAL_A`, `23_STORY_C`, `_E` |
| A-55 (fixed map), the ladder's D-69 | `23_STORY_C`, `09_WR_world_motion`, `07_SE_population_regrowth_B`, `21_PROCEDURAL_A`, `16_PESSIMIST_SE_A` |
| A-56 (the common people's heavy moves) | `07_SE_population_census`, `07_SE_capability_and_chooser_surface`, `07_SE_valley_scenario`, `07_SE_arc_needs`, `23_STORY_E`, `16_PESSIMIST_GO_the_offer_names_what_is_held` |
| A-57, A-58, A-65 to A-70 (land) | `06_FA_war_lives_in_seats_B`, `14_VERBS_BINDING_E_war_seats`, `16_PESSIMIST_FA_A`, `_B`, `06_FA_shortest_loop_B`, `07_SE_campaign_supply_and_muster`, `07_SE_treasury_granary_B`, `09_WR_world_motion`, `09_WR_B_draws_not_thresholds`, `16_PESSIMIST_WR_A`, `22_HAPPENINGS_B`, `_D`, `16_PESSIMIST_GAME_consequence_reading`, `23_STORY_D`, `15_…SYNTHESIS_B`, `15_…COLONIAL_B`, `_D`, `…COLONIAL_grounding_F`, `15_…PAPACY_C` |

**The two premises the story-enablement lane assumed**, reconciled in `23_STORY_B_a_house_continues.md`
and `23_STORY_D_story_census_and_gate.md`: (1) natural death and `majority_age` go live (A-15 orders the
ages authored, which is the condition STORY-B's own loader refusal names); (2) the prologue is five
years (A-51), counted on a declared year. The year has no shipped owner today
(`queries/world_q.py::season_of_year` reads `len(season_factor_draw)`, which ships `()`); its owner is
the roster `20_NARRATIVE_E_the_year_and_the_reason.md` edit 1 adds, which every age in seasons and the
prologue's length now depend on.

# Jordan — what survives in this family (two items; each with two options in its row)

1. **Are named persons born in play?** (Part 11, J-1.) (a) births on, in STORY-B's shape behind
   `birth_rate`; (b) no births: the cast is what the build and the five-year prologue made.
2. **What stands for "the kingdom parliament is functional"?** (Part 13; A-68's own marked assumption.)
   (A) the Court Parliament when it is built; (B) any working realm bench now.

Everything else the audits of this family listed for Jordan is answered by A-1 to A-70 or by the
ladder-closed table, in its row. Marked assumptions that were not escalated, each with its revert at the
site: to whom a seized place's seats pass (LAND D3); the levels and band map of the unopposed entry's
draw (LAND D6); the `riot` row's cells and every caste tier (COHORT); the legibility curve (UNKNOWABLE).

# Coverage (what this lane read, and how)

This family is about 2.4 MB of audits and 1.2 MB of proposals; it was not read in full, and that is
stated so that no row is taken as a second reader's full pass.

- **Read in full:** `CLAUDE.md`, `UNIFICATION_BRIEF.md`, `unified/DECISIONS_ANSWERED.md` (as it grew to
  A-70), `unified/DECISIONS_QUICKSHEET.md`; the head and Part 6 of `U5_FINDINGS_CLOSURE_U5a.md` and the
  head, tail and first tables of `U5_FINDINGS_CLOSURE_U5c.md`; `26_MASS_BATTLE_aggression_and_land.md`.
- **Read at their decision surfaces** (finding headings and fix lines; every §6 disposition and
  resolution table; survivors; proposal lists; arcs tables), with long table cells cut at 75 to 400
  characters: the two FA, two SE, two WR and two GO audits; `16_PESSIMIST_{GAME,FA,SE,WR,GO}`;
  `12_ARCS_adjudication` (§3's 143-row table was not read; it is closed through §4's mechanisms);
  `20`, `21`, `22`, `23`; `18` (verdict and outline; its rows are U5a's).
- **Institutions:** the synthesis's collision ledger, Layer 1 section, commensuration tables and
  survivors; the Venice and Papacy resolution and survivor sections; the Byzantine and Colonial survivor
  sections; the four re-grounding sections **at their headings only**, and the four grounding proposals
  at their outlines (PAP-G's and BYZ-G's rulings tables in full). The historical sections (§1 to §3 of
  each family audit) were not read.
- **Proposals:** the ten `06_FA_*` and three `16_PESSIMIST_FA_*` at their runtime statement, resolution
  and edits; every other proposal of the family at its title, source line, status line and runtime
  statement, a subset also at its resolution (`16_PESSIMIST_SE_A`, `_B`, `16_PESSIMIST_GAME_*`,
  `09_WR_B_draws_not_thresholds`, `09_WR_B_weather…`, `23_STORY_B`, `_C`, `21_PROCEDURAL_C` PG-4,
  `12_ARCS_cited_evidence`). A `Reconciled:` line therefore names the ruling and the step it changes as
  far as that reading reached; where a file's body holds a further passage built on the overruled
  answer, the head line governs it and the passage is not individually rewritten.
- **Not read:** `digests/`, `dossiers/`, `census/`, `unified/DECISIONS_FOR_JORDAN.md` beyond four
  entries, `unified/RESEARCH_MAP_INSTITUTIONS_A/B.md`, `architecture/meta/04_CODE_ARCHITECTURE.md`
  (cited through the audits; Layer 1 conformance is U2's), `audits/26_*`, `27_*`.
- **Code opened to ground a claim:** `engine/season/loop/effects_combat.py::_eff_march`;
  `loop/effects_information.py` (`_take_hold`, `_seize_rung`); `loop/effects_shared.py::occupying_faction`;
  `state/gate.py` (`_seat_grants`, `seat_faction`, the `seizure` basis, `may_seize`);
  `queries/world_q.py` (`season_of_year`, `faction_holding`, `opinion_of`'s head, function index);
  `queries/person_q.py` (function index, `heritage_regard`); `queries/faction_q.py::head`;
  `decision/options.py:132-139`; `data/fixtures.py` (`season_factor_draw`, `withheld_verbs`,
  `bench_quorum`); `rosters.yaml` (`march_target_kinds`, `office_bodies`); `offices.yaml` (`off_king`,
  `off_parliamentary_clerk`, the Parliament note); `arrangements.yaml: parliamentary_debate`;
  `verb_table.yaml` (the verb roster; `succeed`, `petition`); `write_matrix.yaml` (`coherence`);
  `harness/populated.py` (the Office mint sites). Nothing was run but read-only greps and two YAML
  loads; no pytest; no file outside this suite directory was edited; nothing was committed.
- **Rulings that arrived late and are not folded here** because they belong to other families: A-59 to
  A-62 (mass battle, CORE), A-63 and A-64 (a visit occupies its counterparty; precedence, appointments,
  a petition that intensifies while it waits). A-64 touches `petition`, which FA's seats receive; no FA
  proposal was rewritten for it.

**Counts.** 550 rows: RESOLVED-BY 425, SUPERSEDED 110, STALE-FALSE-POSITIVE 10, DISPUTED 3, JORDAN 2.
A row may close several ids that share one decision; ids are named in the row.
