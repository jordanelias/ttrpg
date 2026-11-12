# Digest proposals_recent4

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane: proposals dated 2026-09-20 or later, and undated ones. Note: the assignment list also carries the `_session_provenance/` trees (dated 2026-08-29 to 2026-09-01) and several undated top-level proposals; all are digested in assignment order.

### proposals/2026-11-04-content-parameters-docket/07_social_fieldwork.md
- **What it is:** Docket chapter 07 (collation of social-contest, Proceedings, fieldwork parameters and choice surfaces), 2026-11-04, lane IN.
- **Status:** "PROPOSED (2026-11-04). Collation ... reference under CLAUDE.md §0.05, not a mechanism; merging ratifies nothing." Reading: live as a measured snapshot of 2026-11-04 (line numbers will have drifted); a map, not a mechanism.
- **Bears on:** SC, FI, CHAR, FA, CORE.
- **Content that matters:**
  - Both `social_contest` and `fieldwork` are typed-record-in/typed-record-out; the single module entry is `social_contest.roll(inp, rng)` returning `Margin(net, ob)` (no band/winner); graded inquiries `research/examine/surveil` also route through it, while `interview/reconstruct/thread_read` are ungraded (:24, :53-58).
  - The Ob composition (`obstacle`): opposition halved, minus `reception_gain*reception + proof_step*proofs` floored at OB_MIN, plus `forgery_quality`, capped by `obstacle_ceiling` (:25). So evidence enters as `proofs`/`reception`/`forgery_quality` numbers, not as a cited typed item.
  - `speech_kinds` (6 rostered; only `impugn_motive` caps bands to `[Partial]`) is UNREAD by game code: only the loader and tests read it; H-153/H-154 blocked on an unbuilt resolution ladder (:41, :160-168).
  - `Person.capability` is held by 1 authored person (Carin Vedel, `copying: 3`); every other person falls to `pool_default`=2; `verb_capability` maps only `tell`,`speak` -> `copying` (2 of 63 verbs); nine attribute keys have no Person carrier (:76, :87-101).
  - 8 live arrangements (arbitration, parliamentary_debate, council_of_state, legal_trial, tribunal, interrogation, inquisition_hearing, excommunication_deliberation), all `disposal: bench`; 13 keys; loader C-1 check is a report, not a refusal; 5 games unseeded (negotiation, envoys, audience, appeal, public debate) (:137-158).
  - Social-contest kernel in `systems/social_contest/sim/contest/` (11 policies, 4 styles, 8 proceedings) is NOT wired to the season loop; retirement timing is Jordan's (SM-15) (:42-44, :225).
  - Part B lists PROPOSED-ONLY parliament/debate parameters (motion docket keys, `council_share` 0.5/0.6/2/3, consent rows, `aptness` obstacle price, 12 speak kinds, appeals with caller-supplied `max_depth`) all with NONE in code (:287-346).
- **Conflicts / stale:** P4's `faculties:` replaces `VERB_CAPABILITY` (PROPOSED-ONLY); roll.py:30-33 says kernel reads a faculty while live path reads `Person.capability` (:84). Part B conflicts a-e (:349): PD vs RD withdrawals; P03 lists 15 keys vs live 13; P04V speech roster vs live `ladder_rungs`; P04V investigation emission kinds vs live `finding.made/none`. Line cites not re-verified [UNVERIFIED].
- **Open items:** risk appetite/horizon source undecided (ED-IN-0304, CR-17); `proofs` roster may need `performance`; `why` observation term never supplied; no site kind for library/archive; "which acts need consent is Jordan's content".

### proposals/2026-11-04-content-parameters-docket/08_mass_battle.md
- **What it is:** Docket chapter 08 (mass battle and armies parameters, choices, module entries), 2026-11-04, lane IN.
- **Status:** "PROPOSED (2026-11-04)... merging ratifies nothing." Reading: live snapshot; most values since 2026-11-04 may have moved (e.g. army-phase5).
- **Bears on:** MB, CHAR, SE, PC, CORE.
- **Content that matters:**
  - The season ships NO authored army, unit, subformation or order of battle; `army` Records are minted at runtime by 6 verbs (`recruit, form_unit, assign_troops, order_unit, disband_unit, discharge_troops`); all mass-battle rosters live as Python dicts in `modules/mass_battle/`, not in `engine_params` (:11, :15-31).
  - Hierarchy in the data: army Record -> up to 11 subformations (`SUBUNIT_CAP`) -> Subformation 7 fields (name, troop_type, troops, role, stance, target, fall_back_at); `Subunit` ~35 fields, `Unit` ~25; Unit power/command/discipline are baseline stubs 4/4/5 with morale season-derived (:35-73).
  - 14 troop types; four per-type tables have unequal membership (stats 14, roles 11, reach 15, loadout 14, training site 13, density cap 4, mounted set 3, preset ROLE_OF 12); 5 types are "provisional-by-analogy" (:77-102).
  - Equipment (10 weapons, 4 armours, 14-row loadout) is PLACEHOLDER, `provisional=True`, "NOT YET WIRED into resolution" except `unit_type_for` reading weapon `reach`; per-unit `dr` and `stamina` deliberately unbridged; no kit carrier (:144-163). Relevant to Jordan's mixed-weapon/carry-cost intent: no secondary-weapon or carry-cost datum exists here.
  - Commander: `Officer.command` clamped 1-7, default 4; no Person feeds command/charisma/cognition (:167-181). Recruitment: `TROOPS_PER_WEIGHT` 300, `MUSTER_FRACTION` 0.10 (:111-112).
  - Order triggers (6 kinds), 17 order-settable fields, 15 roles, 4 shapes with MIN_DISCIPLINE; 7 of 15 role-instruction keywords are UNWIRED (pin, loose, harass, screen, pursue, volley, shoot_move) (:312-357). Battlefield constants: BATTLEFIELD_SIZE 51, UNIT_GRID_SIZE 30, CELL_CAP 200 (:215).
  - Troop-stock design (`2026-10-16-troop-stock-design`) not built; M22 gates it (:123-140). No logistics/supply parameters for armies (:244-255).
- **Conflicts / stale:** 08_mass_battle_units.md says ten types and roles INERT; code has 14 and wiring since MB-04 (:265-266). `orderofbattle.py:75` duplicates baseline literals from `massbattle.py` (two copies of one fact, test pins them equal) (:72). Docstrings cite dissolved `designs/...` paths (:162, :218). knights_templar excluded from MOUNTED_TYPES despite lance reach (:101).
- **Open items:** M22 ruling (troop stock); equipment grounding; commander feed; per-type speed tier; roles for 5 types.

### proposals/2026-11-04-content-parameters-docket/09_verbs_params.md
- **What it is:** Docket chapter 09 (the 63-row verb table, write_matrix, engine_params families, season fixtures), 2026-11-04, lane IN.
- **Status:** "PROPOSED (2026-11-04)... merging ratifies nothing." Reading: live snapshot; the verb table here is a full inventory.
- **Bears on:** CORE, FA, SC, FI, PC, MB, SE.
- **Content that matters:**
  - 63 verbs; 48 have an `@effect_for` handler, 15 have none (challenge, comply, construe, dispatch, evade/defy, examine, interrogate, interview, reconstruct, research, speak, surveil, tell, thread_read, tie/knot) (:38). Grades: 40 `assumption`, 23 `ruled` (:32).
  - The per-verb table (:39-103) lists eligibility, slots, handler `file:line`, preconditions, and prize owner: only `fight`/`accept` -> combat, `march` -> mass_battle, `argue/determine/interrogate/tell/arrest/speak` -> social_contest; army verbs call `mass_battle.army` by composition role, not a contest.
  - write_matrix 41 rows + 6 retired; 4 rows carry `unproduced` provenance (:111-122).
  - engine_params: sim_params 292 entries (mass_battle 164, threadwork 36, social_contest 31, engine.season 18, fieldwork 15, combat 12), 168 uncited, 8 assumption-grade; game_constants 6; composition roles 16 (:124-145).
  - 86 `DEFAULT_FIXTURES`, all injected defaults graded `assumption`; 15 rule-switch strings, 4 bools, 3 None (:147-158).
  - Common to every Act: degree/intensity is NOT chosen but comes from the contest result and fixtures `effort_level`, `pool_default`, `obstacle_default` (:37).
- **Conflicts / stale:** `verbs.py` header says VERB_TABLE assigned twice (harmless). `thread_read` is gated on `thread_sensitivity >= 30`; `construe`/`evade` untyped.
- **Open items:** none structural; operand object types (dispensation, petition, works) are owed by other lanes.

### proposals/2026-11-04-content-parameters-docket/10_season_loop_choices.md
- **What it is:** Docket chapter 10 (season loop phases, decision points, chooser, budget, seam), 2026-11-04, lane IN.
- **Status:** "PROPOSED (2026-11-04)... merging ratifies nothing." Reading: live snapshot.
- **Bears on:** CORE, CHAR, FA, SC, MB, PC, GO.
- **Content that matters:**
  - Season order: CALENDAR -> MATTER -> `scene_budget` rounds of {DELIBERATE, RESOLVE, ENCOUNTER, WITNESS} -> CENSUS; 7 steps, 4 barriers (:15-28).
  - Chooser = one shipped policy: score = pursuit (15 convictions projected to 7 axes, damped by confliction) + stance; Plackett-Luce sampled order, tau=0.1; scene packing; intent disclosure 0.0 (:73-104). 22 of 63 verbs have no `alignment` cell, so pursuit scores 0 for them (:86, :102).
  - Opening set formed from all 63 verbs, filtered by withheld verbs, eligibility, own-state, `refusal_axis` (shipped None), declines (:51-71).
  - Budget `max(1, k + office_bonus*holds - body_penalty - leg_penalty*legs)` with k=5 (:106-117).
  - `dispatching_chooser` is a dispatch hook only: the callback receives View/Sensation/ask_budget but no option list; opening_set needs Fixtures not reachable from the callback; no UI text exists (:154-158). This is the player/NPC-same-interface answer: same callback signature, but the player has no menu.
  - Contest seam: degree token from result (combat 3 bands, field 4, margin 4); `contest_max_depth`=2 caller-supplied; endings: 2 members (peninsular_sovereignty, theocracy) read only, no halt (:138-195).
  - `view_builder_rules` has no fixture key; DELIBERATE passes none (:47).
- **Conflicts / stale:** `driver.py:252` docstring says "Six steps"; `options.py:413`/`choose.py:129` docstrings say thirteen convictions/four-axis; roster has 15 and 7 (:31, :103).
- **Open items:** none code-side per the file; GO mapping is `04` §C.12.

### proposals/2026-11-04-content-parameters-docket/11_workplan_owed.md
- **What it is:** Docket chapter 11, 77-row table of content the active plan (`workplans/valoria_master_workplan_v10*`) says only Jordan can author, 2026-11-04.
- **Status:** "PROPOSED (2026-11-04)... merging ratifies nothing." Reading: live as an index; individual rows' defaults may have been answered since.
- **Bears on:** CHAR, FA, MB, PC, SE, WR, ARCS, PROCESS.
- **Content that matters:**
  - CR-20: attribute values for the 46 authored cast rows are owed; until then `faculty` falls back to `pool_default`; M23 tenth attribute name; M24 training composition (`max` default) (:16-18).
  - `Person.capability` empty on 83 of 83 realm persons (429 of 430 corpus persons); arms inventory (CP-T03-03/04) "supplies none": inert at zero holders (:32-34, :93).
  - M22 (may an army be a counted troop stock; amends Layer 1 04:801/810) default NO; JQ-4/REM-32 weight->troops multiplier ships at 1; M27 commander orders default AUTOMATED (:38-40).
  - 5 heritage roster members and nine ladders (66 named posts) owed per-person/seat mapping; `rank_gain` stays asleep until `ladders:` exists (:22-24).
  - ED-595..602/610/649-653: arcs for named NPCs (Ehrenwall, Torsvald, Vossen, Hann, Orm, Almud, Vaynard) "require user approval" - LEAVE (:25-31).
  - CL-THRUST ladders for ten thrust axes, CL-OPEN story-opening pool rows, CL-EVENTS cards and per-territory weather triples are Jordan content with no builder (:45-47, :49, :66-69).
  - M31/E-3 management budget default (iii) none; M37 `refusal_axis` ships None (:83, :85).
- **Conflicts / stale:** rows cite workplan line numbers that may have moved; several rows "from grep only". Plan rule P11 (no position authors a Jordan answer).
- **Open items:** all rows are open by construction; many default-confirmed ("CONFIRMED AT THE DEFAULT").

### proposals/2026-11-04-cr11-computed-establish-design.md
- **What it is:** Design note for plan position CR-11/CR-25: how a computed `establish` act derives the office it founds, 2026-11-04, lane IN.
- **Status:** "PROPOSED (design reference for CR-25's builder; the code is the mechanism)". Reading: live design reference for one builder; history if CR-25 landed.
- **Bears on:** FA, CORE, CHAR.
- **Content that matters:**
  - Computed `establish` refuses today because `office_described_by(a)` (`loop/predicates.py:218`) needs payload keys `office/post/rung/remit` that the closed operand roster (eight operands, `rosters.yaml:2078`) cannot carry (:11-18).
  - Proposed: a World-taking sibling derives rung from `subject` (four refusal conjuncts incl. `in_holdings`, `purview_reaches`, strict rung-kind ascent, `seated_on_the_rung_above_structure`), post from `titles.domains` read in reverse (first authored post when many-to-one), remit = seat remit less `confer`/`revoke`, conferral `appointed`, revocation `rung_above_in_holdings` (:29-37).
  - Clause 5 changes: purview on re-remit of any existing office (H-144 b); a reduction of remit is a partial revocation requiring `may_revoke` (H-132 b) (:42-58).
  - Falsifier: six hand-built cases + planted failure (drop conjunct i turns test 2 red) + control (`holdings_to_found` off = pre-item hash); realm reading via `harness.aperture 4 s` (:60-75).
  - Read-only probe on `build_realm(0)` returned 16 live holds, 14 holdings meeting (i)+(iv); the card said 15 (:92-94). No realm seat sits directly under the realm on a territory it holds, so card test 1's "King" needs a hand-built territory (:88-91).
- **Conflicts / stale:** Card line citations moved (rosters.yaml 1864-1890 -> 2106-2140) (:79-81); card prose vs `seated_on_the_rung_above_structure` differ (:82-87); `off_king` has `revocation: null` and M8's third `revocation_bases` value is not yet in the tree (:100-102).
- **Open items:** ID derivation and first-post pick are `[ASSUMPTION; medium]`; M8's throne basis owed by CR-37.

### proposals/2026-11-04-knowledge-model-build-plan.md [partial 71%; read whole]
- **What it is:** Build plan vetting Jordan's 2026-11-04 rulings ED-IN-0319..0331 (knowledge model, ten attributes, histories, hooks) against the tree and the v11 plan, lane IN.
- **Status:** "PROPOSED (a plan, not a mechanism; nothing here is built)". Reading: live as intent for CR-82..CR-85; sections 11 folds a sequencing check; partly superseded by 2026-11-05 attribute rulings.
- **Bears on:** CHAR, FI, SC, PC, MB, CORE, WR.
- **Content that matters:**
  - Most of the claim model already exists: told-claim corroboration is a noisy-OR over distinct origins (`person_q.py:938-974`), `deeds_judged` never reads confidence so staleness already leaves judgment alone; only retention (ledger_cap 200 fills in season 1; control 0/6/0 of 236 acquaintance claims at season 4) is the gap (:19-28, :41-47).
  - CR-82 commits 2/3 as written (refresh/`stance` write at WITNESS) are dropped: the write_matrix forbids them (`write_matrix.yaml:93-96, 256-262, 180-185`), and a `stance` write would double count and fork `regard` from `reception` (:30-38).
  - Ten attributes (ED-IN-0328): Agility->Coordination, Acuity->Reason, Will->Spirit, Charisma->Presence, add Perception and Grace (Composure alias), drop Bonds; keys stay stable; Godot bar stays (IN FLUX) (:79-109). The oracle `knots.py:185-216` reads `bonds` (:90).
  - Histories: combat `history` is the roll's backbone (pool `max(5, history+6)`, Ob `history/2`, `core.py:54-56,115`); the season never authors it (default 3, every season fight pool 9 vs Ob 1.5); replacing it moves every season fight: needs design CR-85 (:148-177).
  - Derived values census: 21 registry derived values, 2 duplicates, 12 correlates, 4 single-owner (all in `combatant.py`), 3 absent; TroopCount has two weight-to-troop ratios (1:1 at `massbattle.py:228` vs 30 per unit at `:255`); Health carried twice (`Person.body` and `WoundTracker`) (:179-200).
  - A year is four seasons (ED-IN-0332) (:45-48). `lie` builds as CR-27 with no own kind, so detection symmetry with `forge` is not possible (:136-146).
  - Risk tolerance is a duplicate of ED-IN-0304/CR-17/CL-PERSON M40; build nothing (:128-134).
- **Conflicts / stale:** REM-45 dropped; CP-T07-02, PC-14 re-based; CP-T03-04/05, PC-17 conflict with a history replacement (:164-167, :255-261). Superseded in part by `2026-11-05-attribute-rulings-adjudication.md` (Composure/Grace gloss narrowed by AR-44).
- **Open items:** whether `write_matrix.yaml` is Layer-1-bound (:220-222); unverified chained-told-claim count, REM-30 creation sheet, cast `stats:` blocks (:234-236); `ci_names_consistency` acceptance of new aliases not verified (:274-275).

### proposals/2026-11-04-strife-flows/01_STRIFE_KINDS_DRAFT.md
- **What it is:** Kind list (OPENS/JOINS/NEVER) of Event kinds for the "strife flows" person reading, 2026-11-04, lane IN.
- **Status:** "RATIFIED (2026-11-04, ED-IN-0316)... five open calls of §6 resolved ... ratified with the list"; the list the loop reads is to be `rosters.yaml` `strife_kinds` once CR-75 builds it. Reading: ratified as intent; live reference until CR-75 lands the roster.
- **Bears on:** WR, CORE, CHAR, FA.
- **Content that matters:**
  - Measured on `build_realm` seeds 0/1 over 4 seasons (73,277 and 85,183 Events): default play opens only 3 and 4 strife events; the shipped realm is quiet at the kind level (:72).
  - OPENS (9): field.won, field.lost, rung.seized, rung.razed, record.seized, arrest.made, compliance.withheld, requisition.taken, site.damaged. JOINS (23 kinds) incl. march.declared (44/86 per run, opens only in the world reading by side R or O), person.died, petition.*, dispensation.issued, tenure.closed/opened. NEVER (12) incl. duty.taken (221/165), duty.refused (388/379), news.told, travel.moved (:22-64, :84-94).
  - A tax is mostly invisible to the person reading; the world reading opens a rival succession (second claim on one seat), a petition movement (second petition on one matter) and a burden writ by CONTENT, reading `Record.subject_matter` (:70, :76-78).
  - Rulings 1-5 resolved "for the better emergent narrative": march.declared joins (lag yields rumour and late warning), requisition.taken opens, compliance.withheld opens (defiance of a held writ; supply 0 because writs reach addressees only by `give`) (:96-106).
  - A kind is terminal only if every code it maps to is terminal; detention.ended/ban.ended/field outcomes conclude only in the world reading (:71).
- **Conflicts / stale:** PR #553's master lists `duty.taken` as a tax opening; this file overrules (:60, :70). Study test phrases `[UNVERIFIED]` (:108).
- **Open items:** `[GAP]` person-side attachment of a joining claim to a world-held strand; `[GAP]` which `subject_matter` term marks a burden (:103-104).

### proposals/2026-11-05-attribute-rulings-adjudication.md
- **What it is:** Adjudication of Jordan's 2026-11-05 attribute rulings (AR-01..AR-58) against code, with reconciliation and build sequence, lane IN.
- **Status:** "PROPOSED (2026-11-05). An adjudication ... merging ratifies nothing." Reading: live design reconciliation; precedes B10-10 etc.
- **Bears on:** PC, CHAR, SC, FI, MB, CORE.
- **Content that matters:**
  - Conformance of 48 rulings: 7 conform, 16 partly, 6 contradict, 19 silent. Contradictions include `reading=(2cog+att)/3+history` (`combat_systems.py:171`, AR-40 wants pure Perception), aggressor read (AR-18), traditions' `familiarity` keyed to two labels (AR-43/45/46), knot gate on Bonds (`knots.py:53,200`) (:15-55).
  - The season builds every combat fighter at class defaults except `end` (`seam/wrappers/combat.py:36-41`); so making `reading` Perception alone leaves season fights byte-identical (cog=att=3). Without PC-06 K-1 (seam builds the `Combatant` from `Person.attributes`) every combat ruling is inert in the season (:59, :93).
  - Nothing in the season reads Reason, Perception, Presence or Grace today; `choose.py:352` uses one tau for every person (:31-34).
  - Rule reconciliation: AR-04 (attributes weight the choice) narrows ED-IN-0261's "identical pursuits dispose identically"; capability "gates nothing" survives because a weight is not a gate (:80, :100). Spirit may only discount ADVERSE instance modifiers, never base Ob (:102).
  - Taken by the ladder: Reason has no combat read (cog leaves Combatant); Grace in a formal venue demotes the contest result for a graceless-but-persuasive speaker (the two takes most worth Jordan's glance); per-bout familiarity set by the seam (:104, :143, :157).
  - New positions: CR-92 (Grace/Presence/Attunement-bond), CR-93 (attributes in chooser, per-person tau), CR-94 (forger Coordination), CR-95/96 (Spirit, `opposed_by`), PC-18..21, B10-11b batch (:167-176). Hash-mover table (:178-194).
- **Conflicts / stale:** Corrects the verb-attribute map: F8 "moves nearly every combat outcome" is wrong for the season; F23 line cites; F25 evidence (ED-1040 does not establish the stall was real) (:57-65). `modules/mass_battle/config.py:534-535` records a 2026-07-08 directive to abandon commander-related combat pools vs live `derive_command` [UNVERIFIED which wins] (:64).
- **Open items:** Health formula AR-56..58 PROVISIONAL, no position written (:159-161).

