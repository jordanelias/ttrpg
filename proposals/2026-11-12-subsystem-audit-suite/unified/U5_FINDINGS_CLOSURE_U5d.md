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
now order); **LAND** = `U5d_FA_land_and_seats_pass_on_a_won_march.md` (written by this lane on A-57 and A-58).

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
| F-FA-13 | a defeat costs bodies and never a holding or a seat | RESOLVED-BY | **LAND** (`U5d_FA_land_and_seats_pass_on_a_won_march.md`, written by this lane on A-57 and A-58: an aggressor's win on a march onto land another holds passes the land and its seats; a draw or a defender's win passes nothing); WAR-B edit 6 as reconciled | `architecture/meta/10_FACTIONS_AND_DEPLOYMENT.md:90`; `loop/effects_combat.py::_eff_march` ("PRESENCE, NOT TITLE", opened) |
| F-FA-14 | under the planned `at_war`, one committer keeps two factions at war | RESOLVED-BY | WAR-B edits 1–4 as reconciled: A-20 rules (B), so the "lands only on that ruling" hold is lifted | `04:460` |
| F-FA-15 | men are levied by whoever minted a paper | RESOLVED-BY | LEVY-B as reconciled (A-22: the cohort is "the unseated in its land") | E-B3 |
| F-FA-16 | five of ten factions have no head; one has no members | RESOLVED-BY | TERMS-B edit 4 (two heads); the Guilds headless by design; R-34 (`faction x` excluded by name) | E-B2 |
| F-FA-17 | at tick 0 no rung holds a store | RESOLVED-BY | `07_SE_treasury_granary_B.md`; the seeded start draws bounded stores (A-50, `21_PROCEDURAL_D_world_cards_and_churn.md`) | addendum E-B1 |
| F-FA-18 | what an order orders exists only as prose | RESOLVED-BY | OWED-FA §5 (R-27: a closed set of term shapes, built after an answered writ is observed); VB-D owns the row | H-44 |
| R-22 | Layer 1's battle roster names stakes the code does not pass ("keep β: a field writes presence") | SUPERSEDED | A-57, A-58 replace β; LAND carries the edit; holdings and seats both pass, so the Layer 1 clause is met in full | `_eff_march`'s own tag: "revert: Jordan states α, and title moves here" |
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

