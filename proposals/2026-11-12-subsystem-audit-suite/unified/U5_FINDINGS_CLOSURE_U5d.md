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
| F-PES-FA-04 | a faction cannot refuse a member; the governed are in none | RESOLVED-BY | PES-FA-B edit 3; the governed: `U5d_WR_SE_cohort_heavy_moves.md` (A-56) | `pf2` P4; `pf3_cut.py 0 2` |
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

