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

### proposals/2026-11-04-knowledge-model-build-plan.md
- **What it is:** Build plan vetting Jordan's 2026-11-04 rulings ED-IN-0319..0331 (knowledge model, ten attributes, histories, hooks) against the tree and the v11 plan; lane IN (file was partly read already; read whole).
- **Status:** "PROPOSED (a plan, not a mechanism; nothing here is built)". Reading: live as intent for CR-82..CR-85; section 11 folds a sequencing check; partly superseded by the 2026-11-05 attribute rulings.
- **Bears on:** CHAR, FI, SC, PC, MB, CORE, WR.
- **Content that matters:**
  - Most of the claim model already exists: told-claim corroboration is a noisy-OR over distinct origins (`person_q.py:938-974`), `deeds_judged` never reads confidence so staleness already leaves judgment alone; the real gap is retention (`ledger_cap` 200 fills in season 1; control reads 0/6/0 of 236 acquaintance claims at season 4) (:19-28, :41-47).
  - CR-82 commits 2/3 as written (refresh or `stance` write at WITNESS) are dropped: `write_matrix.yaml:93-96, 256-262, 180-185` forbid them, and a `stance` write would double count and fork `regard` from `reception` (:30-38). CR-82 commit 2 is the ledger cap alone with a run-time ceiling vs the CI timeout (:243-254).
  - Ten attributes (ED-IN-0328): Agility->Coordination, Acuity->Reason, Will->Spirit, Charisma->Presence, add Perception and Grace (Composure alias), drop Bonds; keys stay stable; Godot bar stays (IN FLUX) (:79-109). The knot oracle `knots.py:185-216` reads `bonds` (:90).
  - Histories: combat `history` is the roll's backbone (pool `max(5, history+6)`, Ob `history/2`, `core.py:54-56,115`); the season never authors it (default 3, every season fight pool 9 vs Ob 1.5); replacing it moves every season fight: needs design CR-85 (:148-177).
  - Derived-value census: 21 registry derived values: 2 duplicates, 12 correlates, 4 single-owner (all `combatant.py`), 3 absent; TroopCount has two weight-to-troop ratios (1:1 at `massbattle.py:228` vs 30 per unit at `:255`); Health carried twice (`Person.body` and `WoundTracker`) (:179-200).
  - A year is four seasons (ED-IN-0332) (:45-48). `lie` builds as CR-27 with no own kind, so detection symmetry with `forge` is impossible (:136-146). Risk tolerance duplicates ED-IN-0304/CR-17/CL-PERSON M40; build nothing (:128-134).
- **Conflicts / stale:** REM-45 dropped; CP-T07-02, PC-14 re-based; CP-T03-04/05, PC-17 conflict with a history replacement (:164-167, :255-261). The Composure/Grace gloss narrowed by AR-44 (see attribute-rulings-adjudication).
- **Open items:** whether `write_matrix.yaml` is Layer-1-bound (:220-222); chained-told-claim count, REM-30 sheet, cast `stats:` blocks unverified (:234-236); `ci_names_consistency` acceptance of new aliases unverified (:274-275).

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

### proposals/2026-11-05-attribute-rulings-by-subject.md
- **What it is:** Verbatim compilation of Jordan's 2026-11-05 attribute rulings (AR-01..AR-58) grouped by subject, with firmness tags; cited by ledger row ED-IN-0347. Lane IN.
- **Status:** "PROPOSED (2026-11-05). A compilation of Jordan's own words ... merging ratifies nothing beyond what that row says." Reading: live as the quoted source of Jordan's attribute intent (the words are Jordan's; tags RULED/HEDGED/PROVISIONAL/DIRECTION).
- **Bears on:** CHAR, PC, SC, FI, MB, DICE.
- **Content that matters:**
  - Strength: damage mitigated by weapon type (blunt big-head most, thin piercing least), heft management, armour wearing, leverage, pushing; contributes to health; weapons have mass; stopping momentum by counterbalancing heft (AR-10..14, :36-42).
  - Coordination: accuracy, footing, dodging, precise manoeuvre, forgery quality, lock-picking; the attack's suddenness disguises it from the defender's read (AR-15..19, :44-50). Endurance: stamina, breath, tiredness impacting concentration (AR-20).
  - Reason: acuity, forecasting, what a choice entails; low Focus gives avoidable errors and irrelevant info in the forecast (AR-21). Focus: lapse/error rate from inattention or pain; high Focus characters less distracted and less influenced by irrelevant info in their choices (AR-22, 23).
  - Perception: factual matters; surveillance, fieldwork; "a governor with high perception more likely to notice grain stores are low"; combat read of the attack is "pure perception" (AR-24..26a, 37, 40). Attunement: understanding others' intentions/pursuits, likelihood of forming knots/bonds, opponent's emotional state and prediction of action, how close an opponent is to yielding (AR-30, 31, 38, 39, 41, 42).
  - Presence = charisma magnetism social impact (AR-29, last statement). Grace: dignity/etiquette; ties to royal conduct; low-standing office with high grace thought well of; promotion; venues may prioritise grace, "parliament would penalize someone who lacks sufficient grace" (AR-32..36a). Spirit: staying true to oneself against influence, tolerating harm/strain, threadwork coherence, ignoring obstacle modifiers or adding to the pool (AR-44).
  - AR-04 RULED: attributes and capabilities are combined with "pursuits convictions ambitions goals obligations demands" to weight the best course of action for a character (:29). AR-05: attribute minimum is 1 (:30). Duel is a choice of combat to settle an issue; proposing is far easier than seeing it accepted; a king would not duel unless at the brink of war (AR-51, 52, :118-119). Familiarity grown outside the subsystem, constant at use (AR-45..48). Health `(S+3)(E+3)` PROVISIONAL (AR-56..58).
- **Conflicts / stale:** AR-27/28 superseded by AR-29. Presence/Grace/Reason/Perception/Spirit readers largely absent in code (see adjudication).
- **Open items:** health formula; AR-17, AR-43, AR-56/57 hedged.

### proposals/2026-11-05-cr85-histories-hooks-and-combat-input.md
- **What it is:** Design file CR-85: what replaces the `history` integer in combat/threadwork/knot rolls; what a lifepath "hook" is; the oracles' fate; the health round trip. Lane PC (with IN, WR). File was partly read already; read whole.
- **Status:** "PROPOSED. Ratified by Jordan at 2026-11-05 (ED-IN-0349) and WITHDRAWN the same day ('undo ratification of combat', ED-IN-0351). Reopened with it ... whether `faculty` ... is the right single input to a contest pool, or attribute and trained skill are separate inputs. Nothing in `engine/` or `modules/` was built on this file." Reading: HELD by Jordan's own withdrawal; design stands as an unratified proposal.
- **Bears on:** PC, CHAR, SC, CORE, FI.
- **Content that matters:**
  - Recommendation: combat pool and Ob read `faculty` (the same reader the social contest uses, `sigma.py:146-160`); the five sigma reads of `history` are deleted not re-pointed; field renamed `faculty` (default 3) (:28-38). Measured: every season fight today rolls (pool 9, Ob 1.5), 28 of 28 over two seasons of `build_realm(0)`; under the design every season fight becomes (8, 1.0) because `faculty(w,p,"fight")` = `pool_default` 2 (:56-70).
  - Control arm: constant 3 for every party must reproduce the pre-item season `content_hash` (the deleted sigma terms are exactly 0.0 when both sit at history 3) (:72-77).
  - A hook is not a new thing: it is a capability key, a goal-row commit (via `seed_goals`) or a heritage value, all written at world build; the lifepath id lives on the cast row only, never on `Person` (:92-109).
  - Oracles: combat `core.py:54-56,115`, `combat_systems.py:171,332,1053,1421,1441`; threadwork `min(3, history+3)` is constant 3; knots `pool = spirit*2`; deprecated `systems/combat/sim/combat.py` untouched; exporters re-derive `combat_engine_v1.json` with a `SCHEMA_VERSION` bump (:125-136).
  - Health: stored once as `Person.body`; `WoundTracker` is per-scene working state; the tracker docstring (persists between encounters) is false; mapped twice and the maps differ (in: `party_end` lowers `end` by band; out: `body*left//full`); seeded damage rides the first commit that passes Endurance from `Person.attributes` (:140-168). `practice` cannot count a fight (gate is the ladder's Success; fights carry Felled/Wounded/Untouched) (:188, :219).
- **Conflicts / stale:** the plan cites `seam/wrappers/combat.py:36-39` as leaving history at default 3; those lines are a docstring omitting `history` (:258). Several line cites drifted (:251-259).
- **Open items:** `faculty` vs attribute+skill as separate inputs (reopened); combat key name (`arms` vs matter kinds); module default 3 vs season default 2; retire v30 combat (:280-283).

### proposals/2026-11-05-unified-design-and-build-plan.md
- **What it is:** "The arc of the realm": one design for factions, clocks, breakdown, war, duty and violence with a build plan and workplan fold spec; lane IN (touches FA, PC, SC, WR), 2026-11-05.
- **Status:** "PROPOSED (ratified on merge, ED-1094, except what §6 holds back)." Reading: live proposal; positions CR-86..CR-91 and batch B10-17b; Part 6 questions open.
- **Bears on:** FA, WR, PC, SC, CHAR, CORE.
- **Content that matters:**
  - Interaction audit: nothing checks a relation or context before `fight` forms; seed 0 season 1: 104 formations, 74 same-faction; the grudge is doubled under `declared` via `stance_term` `(1+stance_gain)*(-regard)` (`choose.py:79-85,104-106`); fight's alignment cells non-null on 2 of 7 axes (:27). Build-time loyalty-to-stance writes -4 toward the King, manufacturing a traitor Spymaster who attacks him 5-13 times a run (:31).
  - Realm data: King, Duchess and Duke are NOT sworn (only two `oblige` tenures exist); faction roster has no Valorsmark; `faction_q.head` returns None in every realm; only 12 of 31 offices name a faction (:54, :76, :60).
  - Clocks (CI 0-100 start 28; Turmoil 0-10) are built as folds of `w.log` (no matrix row, no stored counter), each person reading a believed fold from the Events he holds claims of; bands change what persons want or may do, never fire an act; passive increments refused as a fourth clock (Layer 1 §25.1) (:33-45, :82-130).
  - Violence made exceptional (CR-87): person-side `violence_contexts` (war, crime, duel, defence), -0.3 cost on every axis for `fight`, bounded grudge weight on violent verbs, duel stakes `blood`; casus belli carrier = a claim Proposition on a ground (CR-91); duty-of-office decline with a betrayal reading from deeds (CR-88) (:137-173).
  - CR-90 instrument `harness/arc.py`; reference "breakdown or casus belli in >=80% of seeds 0-9 by season 24" is a proposed default, Jordan's share (:175-180, :266).
  - Fold spec for workplan v11 parts 3/4/5/6/12/16 and the correcting ledger row (Part 5, :239-260).
- **Conflicts / stale:** Strife guard ("at least two terminal codes off") vs "almost inevitable" separated as objects (:46). Contradicts ED-IN-0337/0340 and ED-IN-0335 as found in the audit. `[UNVERIFIED: recalled]` history/precedent tags throughout.
- **Open items:** Part 6: share meaning of "almost inevitable"; war contexts vs duels only; Valorsmark = Crown renamed or a fifth faction.

### proposals/2026-11-05-verb-attribute-map.md
- **What it is:** Map of Jordan's ten attributes (primary/secondary) against the verb roster, with 27 findings on combat/season readers of each attribute; lane IN, 2026-11-05.
- **Status:** "PROPOSED (2026-11-05). Reference ... merging ratifies nothing"; every row `[ASSUMPTION; medium]` unless CODE/RULED. Reading: live reference input to CR-20 `vocation_attribute` rows; several findings corrected by the adjudication (F8, F23, F25).
- **Bears on:** CHAR, PC, SC, FI, MB, CORE, WR.
- **Content that matters:**
  - Verb classes: R (season draws a pool now) 12, D (draw in module off-path) 13, P (performance, no draw) 18, none 50 (:15-22). Capability "supplies dice and gates nothing"; `faculty` takes ONE base per vocation under CR-20, so a Secondary column cannot be carried without a `faculties:` weight table (:24).
  - Primary counts: Presence 7 (all R), Spirit 8, Reason 5, Coordination 4, Perception 4, Attunement 4, Grace 4 (none draw), Strength 0, Focus 0 (:228-239).
  - Combat reads seven fields (`combatant.py:93`) and no Presence/Grace/Attunement; `reading=(2cog+att)/3+history` becomes pure Perception per Jordan; tradition `familiarity` is a two-label constant (1.0/0.93/0.85); a missed read guesses a defence mode uniformly at random (`combat_systems.py:1136`), the natural home of an Attunement prior (:250-252, :293).
  - No attribute or opponent-state (emotion, closeness to yielding) carrier exists in `modules/combat`; `disp` is only static aggression; yield/flee are folded into `fight` with no module state (:252).
  - WITNESS `observers_for` reads no attribute: every governor in reach learns a larder shortfall at the same confidence (`witness.py:491-524`) (:253).
  - Chooser: an attribute weights a choice only through `odds_weight` x `faculty` for the 12 R verbs; nothing weights uncontested candidates; one `choice_temperature` for every person (:255, :262).
  - Health sketch `(S+3)(E+3)` vs code (range 16-100 vs 12-60; Spirit leaves; wound structure interval x count lost) (:301-313).
- **Conflicts / stale:** F8 "moves every combat golden" wrong for the season (see adjudication); `march` CODE grade unverified vs `mass_battle/config.py:534-535` directive (:259); earlier drafts' corrections inline ([CORRECTION] tags).
- **Open items:** nearly every finding ends "Not decided".

### proposals/2026-11-05-verb-attribute-map_part2.md
- **What it is:** Part 2 of the attribute map: the designed-verb lexicon (`proposals/2026-10-16-verbs/verbs-09..18`), 159 rows, 147 names, plus 31 CULLED names; lane IN.
- **Status:** "PROPOSED (2026-11-05). Reference ... merging ratifies nothing." Reading: live reference; weaker than part 1 (only the mechanic column of the lexicon read: "[GAP: suite bodies of verbs-09 to -18 not read]").
- **Bears on:** CHAR, SC, FI, MB, PC, FA, SE, WR.
- **Content that matters:**
  - FOLDED names inherit the host verb's class/attribute; 47 rows override the host; no folded name adds a verb that draws (:9).
  - MB in-battle orders `rally/pursue/retreat/withstand` on the commander's `derive_command` pool (Presence 2 : Reason 1) with module draws `rally_check`/`recall_check` (:39-42).
  - SC folded modes (praise/flatter Attunement-first; concede/lie Grace-first) cannot change the key under CR-20's one attribute per vocation unless `tell`/`speak` take a mode operand into `vocation_attribute` (:251).
  - Culled names listed: PC strike/rush/disengage/withdraw/disarm/kill/wound; MB command/invest/assault/fortify; SC argue/supplicate; etc. (:253-262).
- **Conflicts / stale:** `argue` is listed culled in SC lexicon though part 1 maps the coded `argue` as an R verb (:257 vs part 1 :87).
- **Open items:** override rows could be contradicted by suite text (:13).

### proposals/2026-11-08-design-and-code-critique-report.md
- **What it is:** Filed one-round review record ("Design and code critique") with categorised findings, adversarial corrections, grades and suggestions; written against `f94043d`, lane IN, 2026-11-08.
- **Status:** "FILED — reference, not canon ... its suggestions are proposals, and none enters the plan or a ledger until Jordan so rules." Reading: live as a filed review; the five rulings it records (ED-IN-0353..0357) are ledger rows and live.
- **Bears on:** FA, WR, PC, SC, CORE, SE.
- **Content that matters:**
  - Rulings recorded: one parliament (ED-IN-0353); transnational Church with the Holy See at Himmelenger T9 (0354); 15 territories (0355; geography carries 17; which 15 assumed T1-T14 + T17; victory selector counts Askeheim); Schoenland a neutral offshore trade nation (0356; contradicts timeline text which was corrected); "Queen is widow regent or whatever" (0357) - the unconditional five grants are a normalization artefact; build awaits a go (:18-30).
  - Corrections: CR-87 landed, `fight` formed 0 in an aperture run (the "104 formations" figure is STALE); 40.3% of 821 acts did not execute (331/821); Templars/Loewenritter not one mechanism; CI loop has several brakes, not shown closed (:34-52).
  - Defects from the aperture run: `challenge` fails 43 of 48 on a wrong-collection subject so `accept` refuses 17; 103 of 821 fail the kind check; 106 of 167 declared event kinds never emitted; ED-IN-0292 says no computed `accept` forms until a challenge is `give`n yet 26 formed (:69).
  - Remit is a snapshot taken at seating, so a grant contingent on another seat's vacancy is not a data edit; option 1 recommended (Queen's `remit_acts: []` at build plus a regency seat claimed through `succeed`) (:13, :98).
  - Institution table: Church irrevocability is DEVIATION BY RULING (2026-10-11); Guilds, Restoration thin; Ministries/Rectorates/Praefectures/Imperial Court bodies without seats UNEXPLAINED (:55-67). Grades overall D+ (player-facing F for this repo) (:83-93).
- **Conflicts / stale:** Limits: aperture output not committed; neither critic ran code; "25 of 31 seats strippable by nobody", "160/15", "~100 proposals cite research/" are critic-reported (:111-113). `CURRENT.md` stamp predates several heads (:115).
- **Open items:** Queen mechanism go; seat/declare-nominal parliament and Imperial Court bodies; read layer with perspective-bound chronicles; held-out stylized-facts validation; Schoenland seats and trade goals; Church persons abroad by oath (:97-105).

### proposals/2026-11-08-flow-conditioning/README.md
- **What it is:** Directory README for the settlement content drafts feeding CR-106 (Church site kinds) and CR-107 (several cohorts per settlement); rulings ED-IN-0352.
- **Status:** "RATIFIED as the accepted first reading (Jordan, 2026-11-08, 'ratify all and merge'; ED-1094): a first reading Jordan corrects; every row [ASSUMPTION; medium]." Reading: live builder input; "What it changes in engine/season/: nothing at runtime. No loader, test or gate reads these files."
- **Bears on:** SE, WR, CHAR, FA.
- **Content that matters:** Files: `content_church_sites.yaml` (CR-106), `content_cohorts.yaml` (CR-107), `content_provenance.md`, `content_validate.py`, `content_validate.out`. Directory is to be deleted with a `FORK:` row once both positions are built (:8-9).
- **Conflicts / stale:** At this read, `worship` appears in neither `engine/season/rosters.yaml` nor `venues.yaml` and `cohorts.yaml` has no `heritage:`: CR-106/107 not built into the engine [verified by grep].
- **Open items:** the build positions themselves.

### proposals/2026-11-08-flow-conditioning/content_church_sites.yaml
- **What it is:** Data draft for CR-106: three new Church-owned site kinds with band ladders, an owner table and per-venue `site:` rows.
- **Status:** Header: "read by nothing at runtime ... First reading for Jordan to correct. Every cell is [ASSUMPTION; medium]". Reading: draft awaiting the CR-106 build.
- **Bears on:** SE, FA, WR.
- **Content that matters:**
  - New `site_kinds`: worship, templar_quarters, school; wear 0, capacity_floor 0, works_cost {timber: 10}; `band_floors` 100/500/800 per kind (chapel/church/cathedral; station/house/chapter; school/monastery/university) (:12-41).
  - New `site_owner` table (default null; the three kinds -> `Church of Solmund`): ownership by data cell on the kind, not a `Site.owner` field (:43-49).
  - Venue `site: {kind, condition}` rows per settlement type with condition by capacity tier midpoint (300/650/900) and the Church seat 1000; result: 37 worship, 3 school, 1 templar_quarters = 41 Church Sites; 15 of 15 settled territories under the realm hold >= 1; T15 and terr_ALT excepted (:57-94).
- **Conflicts / stale:** Not in engine yet (see README note). Same condition for Valorsplatz and Sigurdshelm (per-type rows, no per-settlement override) (provenance UNDERIVED 4).
- **Open items:** `house` mid-band name unsourced; a build price decides whether a Church Site can be newly built.

### proposals/2026-11-08-flow-conditioning/content_cohorts.yaml
- **What it is:** Data draft (revision 2) for CR-107: 51 `cohorts:` rows over 37 settlements with heritage and conviction by three rules H, C, V.
- **Status:** "builder's input, read by nothing at runtime ... [ASSUMPTION; medium]". Reading: draft awaiting CR-107 build.
- **Bears on:** SE, CHAR, FA, WR.
- **Content that matters:**
  - No row carries `faction:` (B1): a cohort `commit` makes the faction occupy the settlement at build (`world_q.py:2131-2172`), which would license seize/raze/levies from tick 0 and break `test_in36_foreign.py:120`; allegiance is carried by `heritage` and `conviction` only (:6-8, provenance :34-40).
  - Rule H: one majority cohort per settlement by Varfell/band (southern band <=1 or Varfell T4/T12/T13; northern T11 and band >=4; central band 2-3; schoenlander T16); C: caste/minority cohorts; V: conviction from radiation bands, e.g. einhir_restoration = 6 - band for southern, solmund_orthodoxy = min(5, 1 + band) for northern/central, other affiliations 1 (:10-38).
  - Heritage rows: 24 northern, 15 southern, 10 central, 1 altonian (S-007), 1 schoenlander; 8 settlements hold both a northern and a southern cohort (validator).
- **Conflicts / stale:** Conviction rule V gives a whole populace one intensity by territory band; the cast-median alternative was rejected. Schoenlander has no `engages:` cell so conviction is 1 throughout.
- **Open items:** whether to add `schoenlander: altonia` to `engages:`; faction commitment HELD behind an audit of commit readers.

### proposals/2026-11-08-flow-conditioning/content_provenance.md
- **What it is:** Per-cell provenance for the two content drafts, plus canon-location disagreements and the verbatim validator output.
- **Status:** "Every row ... [ASSUMPTION; medium; Jordan to correct]." Reading: live reference for the drafts; engine wins over prose on places (Jordan 2026-11-08).
- **Bears on:** SE, WR, CHAR, FA.
- **Content that matters:**
  - Canon location disagreements (engine wins): Himmelenger is T9 not T14; Varfell territories T4/T11/T12/T13 not T1-T4; Valorsplatz cathedral S-001 not S-003; Gransol S-018 not S-015 (:67-77).
  - The :655 vs :657 faction_politics conflict about Varfell north/south resolved by "an explicit territory id beats a regional phrase", placing northern Varfell on T11 (:45).
  - Consequences: every village/fortress holding two cohorts reaches summed weight = capacity 4, so `migrate` into them is refused from tick 0 (`has_room` counts named residents) (:98-100). `incompatible[solmund_orthodoxy][einhir_restoration]` is true so each northern/southern pair holds both ends (:101-103).
  - Validator exit 0: 51 rows, 0 FAIL, 41 Church Sites (:111-197).
- **Conflicts / stale:** quarantined docs cited by bare filename only.
- **Open items:** UNDERIVED list (:85-94).

### proposals/2026-11-08-flow-conditioning/content_validate.py
- **What it is:** Read-only Python validator for the two content drafts against `build_realm(0)`; re-derives every cohort row and Church-site condition from the stated rules and diffs.
- **Status:** "Read-only validation ... (writes nothing)". Reading: live proposal tool, not wired to CI (only itself references the directory per grep).
- **Bears on:** SE, CHAR, PROCESS.
- **Content that matters:**
  - Imports `engine.season.harness.populated`, `queries.world_q`, `data.cast`, `data.affiliations.conviction_map`, `data.rosters.FACTIONS`/`roster`, `engine.substrate.descriptors` (:17-23); asserts structure the loaders would require and a rule re-derivation `expected == rows` (:165-254).
  - Hard-codes `T11_SET = {"T11"}` for rule H2 (a by-name territory) (:178) and reads the heritage rule via `descriptors.HERITAGES`.
- **Conflicts / stale:** Hard-coded territory id in a rule validator is scripting drift in miniature (acceptable in a proposal tool). Directory slated for deletion once built.
- **Open items:** none.

### proposals/_session_provenance/2026-08-29-to-31/ARCH.md
- **What it is:** Scratchpad brief (2026-08-29) fixing the "modular hierarchy" code architecture: the module tree IS the containment ladder (Person -> Family -> Community -> Settlement -> Territory -> Duchy -> Realm); faction orthogonal.
- **Status:** "adjudicated, binding on the suite" (for the from-scratch exercise). Reading: historical; the README flags an error corrected by adjudication C-1 (R-1 "receives aggregates" retracted -> compute-on-demand).
- **Bears on:** CORE, FA, SE, PROCESS.
- **Content that matters:**
  - Rules R-1..R-5: a module reads own state only, may compute descendant aggregates on demand, writes only its own state; decisions take (actor, VIEW) never world; a faction is a set of persons, never a rung or module (:57-70).
  - Down-stroke = refraction through child modules; up-stroke = rung refuses/carries a demand (:23-28).
- **Conflicts / stale:** Vocabulary (Family/Community rungs) differs from the live rung_kinds roster {person, hearth, community, settlement, territory, province, duchy, realm}: "Family" became "hearth" in code.
- **Open items:** none (superseded by `11_code_shape` and holonic architecture).

### proposals/_session_provenance/2026-08-29-to-31/AUDIT_BRIEF.md
- **What it is:** Brief for the NERS audit critics of the from-scratch suite: steelman-then-attack, E as ratio, S = up/down propagation, R = structural dominance; 2026-08-29.
- **Status:** none stated (working brief). Reading: historical; the NERS method is now owned by `skills/ners/SKILL.md`.
- **Bears on:** PROCESS, WR, CORE.
- **Content that matters:** "Most valuable finding is a FALSE N-LINE" (:33-34); R worked case = Comply/Defy fork where gain decays but cost compounds (:44-47); return format fixed at 1,600 words (:69-79).
- **Conflicts / stale:** Uses an older NERS wording (N = emergence) than CLAUDE.md §0.06's definitions.
- **Open items:** none.

### proposals/_session_provenance/2026-08-29-to-31/AXIOM.md
- **What it is:** Jordan's containment axiom A-1..A-4 captured mid-session 2026-08-29: Family and Community are first-class rungs; a faction is any aggregate at any scale (derived scale); peers compete in a shared container.
- **Status:** "JORDAN'S BINDING DESIGN AXIOM (2026-08-29...)". Reading: historical statement of intent, still the origin of the rung ladder and of "faction is a set, not a tier".
- **Bears on:** FA, SE, CORE, WR.
- **Content that matters:** A-2 faction scale is DERIVED not declared; "two brothers and a national church are the same object" (:8-10); cadet branches, caste and guild dynamics become mechanical (:27-29); Canon's community level (settlement_layer_v30.md:171) vindicated (:25-26).
- **Conflicts / stale:** "Family" rung is `hearth` in the live roster.
- **Open items:** none.

### proposals/_session_provenance/2026-08-29-to-31/BRIEF.md
- **What it is:** Shared writer brief for the nine from-scratch design lanes: no existing work binds; nine throughlines T1-T9; NERS criteria; closed-loop objects (producer -> carrier -> consumer).
- **Status:** none (working brief). Reading: historical.
- **Bears on:** PROCESS, CORE, WR.
- **Content that matters:** Throughlines T1 all actions by characters; T2-T3 changing/fallible memory; T4 no omniscience; T5 upward aggregation; T6 downward ripple; T7 events/clocks/gates as basis of debate; T8 world churns; T9 field investigation first-class (:31-43). "No CI gates, no validators, no registries whose only consumer is process" (:60-61).
- **Conflicts / stale:** references scratchpad paths now gone.
- **Open items:** none.

### proposals/_session_provenance/2026-08-29-to-31/CODESHAPE_FORBIDDEN.md
- **What it is:** Extract of PR #342's code-shape section 7 (forbidden list), ownership table and three signatures `choose(Person,View)`, `resolve(Act,World)`, `witness(Person,Event)`.
- **Status:** none; MANIFEST says its prose paraphrase lists eleven items where section 7 has fourteen. Reading: historical, flawed extract kept deliberately.
- **Bears on:** CORE, CHAR, FI, PROCESS.
- **Content that matters:** Forbidden: a `World` param on decision functions; cohort deposits carrying a value rather than a distribution; stored aggregate/norm/density/reputation fields; a second resolver or auto-resolve fast path (:14); a flat additive person modifier on a roll (:16); scheduled recovery tick on standing (:18); per-entity branch in resolver (:19). Ownership: Person holds interior; container only stake/judging set/standing dates; "Nobody" holds aggregates (:25-31).
- **Conflicts / stale:** Row 14 "a second resolver, an auto-resolve formula, a fast path" bears directly on Jordan's "one path" rule for mass battle and personal combat (auto vs playable).
- **Open items:** none.

### proposals/_session_provenance/2026-08-29-to-31/FINDINGS_DIGEST.md
- **What it is:** Digest of two work lines handed to integration lanes: the NPC matrix (play-space coverage, ~56 probes) and the arc reachability test (83 arcs), 2026-08-30.
- **Status:** none; findings marked "REVIEW" are under adversarial review. Reading: historical, partly corrected by the integration suite.
- **Bears on:** CHAR, ARCS, WR, CORE.
- **Content that matters:**
  - Verdicts 33 RICH / 16 THIN / 4 BLOCKED / 1 SPLIT / 1 SPECTATOR; 19 of 55 have a blocked core (:5-14). Arc tally 40 REPRODUCED-BETTER, 2 REPRODUCED, 22 TRANSFORMED, 10 LOST, 9 NEVER-WORKED; denominator disputed (:68-71).
  - "A BLOCKED CORE DOES NOT STOP AN ARC FROM RUNNING. IT STOPS IT FROM TERMINATING." (:100).
  - The one hole: no world-substrate quantity (Mending Stability, Gap, Rupture) (:74-80). Keep ONE ACT PER PERSON (:107-108). Thresholds: 13 arcs end at a scheduled sitting and survive; 3 end at a counter reaching a number with nobody deciding and lose their ending (:88-91).
- **Conflicts / stale:** Several claims struck by later `03_corrected_findings` (D-1 "floor" struck; C-3 struck) per SUPERSEDE_BRIEF.
- **Open items:** whether convergence of lanes was seeded by shared briefs.

### proposals/_session_provenance/2026-08-29-to-31/MANIFEST.md
- **What it is:** Manifest of the session scratchpad: 19 files copied, 6 deliberately not (extracts of live research files, the 892K arcs corpus at ref `v30-snapshot-2026-06-28`).
- **Status:** none. Reading: historical.
- **Bears on:** PROCESS, ARCS.
- **Content that matters:** Both Part-2 briefs committed at `3dbdf16d` before lanes returned; Part-3 briefs at `b5777ccc` (:62-64). Six session claims were confident-and-wrong, each authored upstream and caught by a reader who had not seen the producer's reasoning (:67-70). Arcs corpus recoverable at the named ref (:52).
- **Conflicts / stale:** lists `PRECEDENT.md` among copied files; not present in this directory [UNVERIFIED].
- **Open items:** none.

### proposals/_session_provenance/2026-08-29-to-31/NERS.md
- **What it is:** NERS charter as of 2026-08-29: E is a ratio against N and R; S = up/down propagation; R = structural dominance.
- **Status:** "binding on the audit stage" (then). Reading: historical; superseded by CLAUDE.md §0.06's definitions (different N/S wording).
- **Bears on:** PROCESS.
- **Content that matters:** Rule 1 E not independent (:8-16); Rule 2 S = S-UP/S-DOWN (:18-24); Rule 3 R dominance with Comply/Defy worked case (:26-33).
- **Conflicts / stale:** the S definition here (T5/T6 only) is narrower than §0.06 S (pauses, consistent methodology, zoom).
- **Open items:** none.

### proposals/_session_provenance/2026-08-29-to-31/PART2_AGONIST_BRIEF.md
- **What it is:** Brief for the two Part-2 producers (integration proposals against PR #342 for the NPC matrix and arcs).
- **Status:** none. Reading: historical.
- **Bears on:** PROCESS.
- **Content that matters:** Each change carries exact doc/section, text change, NERS line, cost, falsifier (:35-40); smallest change; no validators or registers (:44-46); separate SETTLED from LIVE CHOICE (:48-50).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/_session_provenance/2026-08-29-to-31/PART2_ANTAGONIST_BRIEF.md
- **What it is:** Brief for the cold read-only critic of Part 2 (factuality, compliance, logic, rigour, cost); rules P-2 seeded convergence, P-3 one-sided scale, P-4 pessimistic reading.
- **Status:** none. Reading: historical.
- **Bears on:** PROCESS.
- **Content that matters:** Return format VERDICT/Struck/Compliance/Weakened/Survived/Missed (:53-65); must return NOs and YESes, no replacement designs (:42-50).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/_session_provenance/2026-08-29-to-31/PART3_ANTAGONIST_BRIEF.md
- **What it is:** Brief for the Part-3 critic of the comparative document; hazards: manufactured complementarity, false corroboration, unfalsifiable claims, retrospective coherence, smuggling of struck claims.
- **Status:** none. Reading: historical.
- **Bears on:** PROCESS.
- **Content that matters:** Test whether two instruments have different blind spots (:21-25); check a name collision like `exposure` (:26-29).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/_session_provenance/2026-08-29-to-31/PART3_BRIEF.md
- **What it is:** Brief for the Part-3 comparative document (NPC matrix vs arcs: emergent narrative, code shape, working together).
- **Status:** none. Reading: historical.
- **Bears on:** PROCESS, ARCS, CHAR.
- **Content that matters:** Matrix = coverage instrument over seats and affordances; arcs = reachability test over outcomes (:21-32); four fabricated/unverifiable objects caught each time by a reader who had not seen the producer's reasoning (:52-58); "no rates" - arc tally is an upper bound (:66-68).
- **Conflicts / stale:** mis-pointer to "07 §E" for the `exposure` collision (MANIFEST).
- **Open items:** none.

### proposals/_session_provenance/2026-08-29-to-31/PESSIMISTIC_NERS.md
- **What it is:** P-1..P-5 pessimistic reconciliation rules for the integration stage.
- **Status:** none; promoted to `proposals/2026-08-31-integration/00b`. Reading: historical.
- **Bears on:** PROCESS.
- **Content that matters:** R binds at seats a player can occupy; elsewhere a dominant act is characterisation (:21-27); P-5 a fix that adds a system has failed (:42-46); two proposals to test hardest: a world-substrate quantity and a convergence measure (:48-59).
- **Conflicts / stale:** R-at-player-seats-only conflicts with CLAUDE.md §0.06 R's no-player half (emergent narrative without player involvement) only partly.
- **Open items:** none.

### proposals/_session_provenance/2026-08-29-to-31/README.md
- **What it is:** Note explaining why the scratchpad was committed (priming checks need the briefs).
- **Status:** "working documents, not design. Nothing here is canon". Reading: historical.
- **Bears on:** PROCESS.
- **Content that matters:** ARCH.md contains an error corrected by C-1 (:23); arc corpus not committed (recoverable at ref).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/_session_provenance/2026-08-29-to-31/RELAY.md
- **What it is:** Agonist -> antagonist relay discipline (2026-08-31).
- **Status:** none. Reading: historical origin of CLAUDE.md §10's relay.
- **Bears on:** PROCESS.
- **Content that matters:** Relay not dialogue; critic never sees the producer's reasoning; independence structural (critic = Read/Grep/Glob); orchestrator reconciles and records losers (:4-41).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/_session_provenance/2026-08-29-to-31/REVIEW_B_ARCS.md
- **What it is:** Adversarial review of the arc-reachability body (verdict SOUND-WITH-CORRECTIONS), 2026-08-30.
- **Status:** none. Reading: historical.
- **Bears on:** ARCS, WR, CORE.
- **Content that matters:** Tally denominators 42/83 = 51% not 57% (:15-17); scale had REPRODUCED-BETTER but no REPRODUCED-WORSE; Arc 1 scored BETTER while its own closure table lists closure lost (:26-30); the priming charge upheld (Arc 1's verdict and route were pre-supplied) (:39-42); a global world-substrate scalar re-runs the anti-scalar argument unless place-scoped (:54-56); convergence measure compliant only as an offline instrument (:57-62).
- **Conflicts / stale:** none.
- **Open items:** conferral universal (office-rooted) sweep incomplete (:71-75).

### proposals/_session_provenance/2026-08-29-to-31/SETTING.md
- **What it is:** Setting content brief: caste, institutions, Knots, the Person, places, philosophical foundations P-01..P-15, live politics, named particulars (2026-08-29).
- **Status:** none. Reading: historical snapshot of canon at that date; some values superseded.
- **Bears on:** CHAR, FA, WR, SC, SE, ARCS.
- **Content that matters:**
  - Caste enforced by per-institution rank gates (Crown Standing 3+, Church strongly gated, Guilds Masterpiece Examination, Loewenritter and Niflhel caste-open) (:9-16); Niflhel status a LIVE CANON CONTRADICTION (:40).
  - Knots: Disposition +5, TS>=30 either side, Bonds>=5, max floor(Bonds/2)+1, strain gauge, rupture at +5 or five triggers (:44-52). Nine attributes 1-7 with the tenth unnamed (:55-57); thirteen convictions (:61-62); Momentum 0-4 (:65).
  - 35 settlements/14 provinces/3 duchies + 2 special = 37 march targets; flat T1-T17 scheme coexists unreconciled (:72-80).
  - Named particulars the system must be able to produce: King Almud, Queen Lenneth, Duchess Inge Baralta, Duke Magnus Vaynard, Grandmaster Sigrid Ehrenwall, Yrsa Vossen, etc. (:112-118); the 1218-AG hunting "accident" perpetrator deliberately unresolved (:105-106).
- **Conflicts / stale:** thirteen convictions superseded by fifteen pursuits; nine attributes superseded by ten (ED-IN-0328); Bonds dropped; Schoenland "spoiler" superseded by ED-IN-0356 neutral trade nation.
- **Open items:** none.

### proposals/_session_provenance/2026-08-29-to-31/SPINE_INPUTS.md
- **What it is:** Eighteen failure modes (F-1..F-18) extracted from the nine-throughline critique, as lessons not a worklist.
- **Status:** none. Reading: historical but still a useful audit checklist.
- **Bears on:** CORE, CHAR, FI, SC, FA.
- **Content that matters:** F-1 store without producer; F-3 omniscient deciders by signature; F-7 capped-bias trap ("a lie that cannot change any outcome is flavour text with provenance"); F-8 consensus broadcast; F-13 dead state; F-14 corroboration failed open (empty ancestries disjoint); F-15 knowledge stored on the thing known; F-16 granularity gap in claim identity; F-17 scale-blind primitives; F-18 setting-blindness (:3-44).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/_session_provenance/2026-08-29-to-31/SUPERSEDE_BRIEF.md
- **What it is:** Brief for the superseding exercise (new proposal suite replacing PR #342), with five adversarial axes and twelve known open defects.
- **Status:** none. Reading: historical; names struck claims (D-1 floor struck, C-3 struck).
- **Bears on:** PROCESS, CORE, WR.
- **Content that matters:** Twelve known defects including five senses of `exposure`, view budget K `7+Focus` vs constant 12, practice rank 0-5 vs 0-7, dangling Thread pointer, three spellings of the signatures (:62-77); no apparatus; no rates (:81-84).
- **Conflicts / stale:** uses "Hearth" for the rung that AXIOM calls Family (:24).
- **Open items:** all twelve defects were the exercise's work list.

### proposals/_session_provenance/2026-08-29-to-31/SUPERSEDE_RELAY_PROTOCOL.md
- **What it is:** Iterative challenge protocol for authorship (agonist corrects its own draft against the antagonist's challenges; FIX/REBUT/DEMOTE), amended to ONE single document.
- **Status:** "Jordan-directed, 2026-08-31", amended same day. Reading: historical protocol, partly the ancestor of CLAUDE.md §10; but the "audit -> fix -> audit" iteration it prescribes is now forbidden by CLAUDE.md §0 (REVIEW RUNS ONE ROUND).
- **Bears on:** PROCESS.
- **Content that matters:** Eight of twelve defects are cross-document contradictions that a single document makes unrepresentable (:69-100); the falsifier: an unrecorded challenge means the loop did not run (:62-65).
- **Conflicts / stale:** Contradicts the later ruling "REVIEW RUNS ONE ROUND, THEN STOPS" (2026-10-22).
- **Open items:** none.

### proposals/_session_provenance/2026-08-29-to-31/dice.py
- **What it is:** Python script computing a per-die success distribution (0/1/2 successes at 6/10, 3/10, 1/10), pool mean/sd, obstacle-roll bands and opposed contests.
- **Status:** none. Reading: historical/dead; nothing reads it.
- **Bears on:** DICE.
- **Content that matters:** Defines band cutoffs (Disaster <= -2, Failure -1, Costed Success 0, Clean Success 1-2, Overwhelming >= 3) (:38-45), which differ from the live `degree_from_net` ladder (Overwhelming/Success/Partial/Failure) and the live d+sigma model.
- **Conflicts / stale:** The per-die model is the pre-d+sigma d10 pool model; stale against `engine/dice_engine/dice_engine.py`.
- **Open items:** none.

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/MANIFEST.md
- **What it is:** Index of trace logs behind the 2026-08-31 reconciliation of the code architecture across PRs #337-#344 (8 PR logs, 6 repo-sweep logs).
- **Status:** "PROVENANCE ONLY. Nothing here is a design ruling, and nothing ratifies on merge." Reading: historical.
- **Bears on:** CORE, PROCESS.
- **Content that matters:**
  - Rediscovered findings: nothing in the #337-#344 design line executed at that date (`Person`, `Rung`, `Office`, `Site`, `Tenure`, `Query`, `Act`, `Event`, `Claim` absent from engine/); the running campaign resolved with zero people (`world.npcs` empty, `generate_npc` no call site) (:54-60).
  - Two open Jordan rulings ED-IN-0200 (centralized hierarchical key/module contracts) and ED-IN-0201 (personnel precondition) cited by none of the design line (:61-63).
  - Godot 4.3 vs 4.6: the 84-error compile ratchet only ever measured under 4.3 (:70-73). R1 vs R2 conflict on whether the architecture already exists in code (:76-81).
- **Conflicts / stale:** the "Key substrate" and "Godot 4.3/4.6" threads are retired / ruled elsewhere (ED-IN-0232; ED-GO-0002). The "M1 0/7" figure is dated 2026-08-31.
- **Open items:** none now.

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/adjudications/F1_primitives.md
- **What it is:** Fable-5 read-only adjudication of the primitive set and ownership model (Person, Rung, Office, Site, Tenure, StateChange, Claim, Query) across PRs #339-#344, 2026-08-31.
- **Status:** none stated. Reading: historical; its Key-substrate premise ("Event = Key, executing") is RETIRED by ED-IN-0232; the primitive vocabulary (Person/Rung/Office/Site/Tenure/Claim/Query) became the live Layer-2 state vocabulary.
- **Bears on:** CORE, CHAR, FA, FI.
- **Content that matters:**
  - Authoritative primitive set = #344's with amendments A1-A4: a Proposition is the one identity-bearing IMMUTABLE record; Partition membership test is a schema column `social: bool` per (subject-type, field); every Tenure is owned by its subject; the `hold` collision with mass battle's `STANCE_SPEED_MOD["hold"]` (:153-236, :299-303).
  - Tenure := (id, subject, object, kind in {hold, commit, contain, succeed, tie, knot, oblige}, since, until?, conferrer?, degree?, payload?) with per-kind cardinality declared on the schema (:186-190, :289-295). StateChange := (subject, mode in mint|alter|efface, driver Act|Event) (:191-197).
  - Faction deleted as a carrier (Proposition + commit Tenures); "Nobody owns aggregates" ruled correct (:251-270).
  - Id rule `H(world_seed, tick, subject_id, purpose)` ruled correct; uniqueness rests on one-act-per-tick; every Tenure-graph traversal needs a visited set (:343-371).
  - Single escalation: whether the ratified Light Function / Slate binds the player surface (a curated season vs raw witnessing) (:447-469).
- **Conflicts / stale:** R1 "greenfield" and R2 "already executable" both overturned (:377-389); `key_substrate_v30.md` carries two conflicting status lines (:393-399). Many "NOT in code today" statements are dated 2026-08-31 and are now false for the season (Person/Tenure/Claim exist in `engine/season/state/`).
- **Open items:** Slate/Light Function question; ED-IN-0200/0201 cross-cite and close (answered).

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/adjudications/F2_keys_vocabulary.md
- **What it is:** Fable-5 adjudication of keys, naming and vocabulary: the Key substrate as executed, the key namespace (55 types), ED-IN-0200 as a ruling, a completed collision register, naming rules, closed-set audit; 2026-08-31.
- **Status:** none stated. Reading: historical; its Key-substrate subject is RETIRED (ED-IN-0232); the collision register and closed-set audit remain a useful vocabulary check.
- **Bears on:** CORE, PROCESS, CHAR, PC, MB.
- **Content that matters:**
  - Key substrate summary (keys.py enums AXES/ROLES/SCALES, 8 invariants, KeyLog content hash, TickScheduler caps required with no default) (:32-128) - all retired.
  - ED-IN-0200 ("key contracts and module contracts explicitly defined in a centralized hierarchical manner") answered by a spec: levels GAME > SUBSYSTEM > MODULE > KEYS/STATE; three registries stay separate with a declared parent; a `export_contract_tree.py --check` gate; DONE only when the port or `composition.py` reads the export (:245-332).
  - Collision register: `hold` has six senses (Tenure kind, mood HOLDS, predicate form, coercion quantity, mass-battle stance at `config.py:269`, process HELD), `stance` five (Person.stance, mass-battle unit stance, NPE opinion scalar 1-5, referent kinds, salience weight), `witness` five, `kind` nine; rule: casing is the namespace test (dotted lowercase = registry id, Capitalized = record type, lowercase = field/kind/verb, UPPERCASE = step/phase) (:341-376, :206-241).
  - Naming overturns: StateChange modes `mint/alter/efface` -> `create/alter/destroy`; `Tenure` kept with a mandatory qualifier; design `Event` IS the Key; the compendium's five-band degree ladder overruled by the live four-band `degree_from_net` (:384-400, :457).
  - Closed sets: a set is closed when code raises on a non-member (13 Convictions and substrate enums are; most others are prose) (:483-489).
  - Escalations: which design line (greenfield-v2 Entity/Tag/Post/Gauge vs ideal-v2 Person/Rung/Office/Site/Tenure) is the vehicle for ED-IN-0200/0201; whether to add Disaster/Costed Success bands; `piety_track` owner; F6/G-30 world dying or misunderstood; "no commander, no battle" gate vs penalty (:542-561).
- **Conflicts / stale:** `Tenure` and the Person/Rung/Office/Site vocabulary later became the live Layer-2 state (engine/season), settling escalation 1 de facto. Degree ladder is still four-band in code.
- **Open items:** 5 escalations, most now answered by the built season; "no commander, no battle" gate reading (docket 11 M22/M27 related).

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/adjudications/F3_godot46.md
- **What it is:** Fable-5 adjudication of the Godot 4.6 code shape for the port: version evidence, project layout, autoload policy, carrier placement, purity, fixed-point arithmetic, witness fan-out, determinism, save/load, ids, seam, skeleton verdicts, register, build order; 2026-08-31.
- **Status:** "REFERENCE, not mechanism ... Nothing in it executes." Reading: historical for the version question (ED-GO-0002 now rules the version); the architectural rules are intent for GO.
- **Bears on:** GO, CORE, DICE.
- **Content that matters:**
  - Version evidence: 4.3 has a declared `project.godot`, a CI pin and two executed headless runs (84 compile errors, 63 "Cannot infer the type"); 4.6 is prose, and the file it cites (`ecosystem_versions.yaml`) does not exist; the 84-error ratchet is only meaningful under the binary it was measured on (:57-111).
  - Layout: `core/` headless, not one Node; `game/` is the only Node layer; autoload table empty or presentation-only; `World` driver-owned; `.tres` under `data/` is generated, never hand-authored (:120-209). Rejects `scene_tree_architecture.md`'s GameState autoload and the live `valoria-game` `Meta` single-state-owner pattern (:157-162).
  - Fixed point: `condition` int in [0, `COND_SCALE`=10,000]; `f(degree)` as integer pairs over 16; half-up rounding on magnitude then sign; clamp once; band gate by cross-multiplication; float stays for belief-side arithmetic (:317-404).
  - Determinism: one `RandomNumberGenerator` per operation from `H(world_seed, tick, subject_id, purpose)`; owned SplitMix64, never built-in `hash()` (:438-470). Save = binary snapshot with versioned header, not `.tres`, not event-log replay; JSON ids as hex strings (2^53 trap) (:486-520).
  - Purity guard in the game repo: scan `core/` for `load(`/`preload(` and allowlisted autoloads; exactly one call site of `_witness(` (:295-313, :424-434). Skeleton `wound_module.gd:55` writes a field its own manifest declares non-writable (:606). The Python oracle has no substream implementation, so parity is threshold-level (:478-482).
  - Escalations: engine version target; autoload ruling (STRAT:213) (:739-756).
- **Conflicts / stale:** the Godot version question is now ruled by ED-GO-0002 (CLAUDE.md) so §1 is historical; the skeleton and `Key`/`KeyBus` references are retired. The 12-of-18 resolver-side Queries omitting `World` is a Layer-1 doc issue (:286-293).
- **Open items:** `season_factor` distribution blocks `yield` fixed-point; int-overflow wrap in GDScript untested (:459-462).

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/adjudications/F4_loop_execution.md
- **What it is:** Fable-5 adjudication of the season loop and execution path: rules between three competing loops, upholds the six-step loop as a refinement of the running three-phase tick, specifies four structural tests, the ED-IN-0201 personnel precondition and an execution path; 2026-08-31.
- **Status:** none stated (adjudication; nothing executes). Reading: historical for the execution path (the season loop now exists in `engine/season/`); still the origin of the loop vocabulary, the structural-test list and the personnel gate.
- **Bears on:** CORE, CHAR, FA, WR.
- **Content that matters:**
  - Ruling: three-phase tick (`engine_clock.py`: SEASON_TICK -> ACTION -> ACCOUNTING_BOUNDARY) is the AUTHORITATIVE MECHANISM; the six-step loop (CALENDAR, MATTER, DELIBERATE, RESOLVE, WITNESS, CENSUS; 4 barriers; 4 write classes) is the contract nested inside it (CALENDAR in SEASON_TICK; MATTER/DELIBERATE/RESOLVE in ACTION; WITNESS/CENSUS at the boundary); the seven-phase P0-P7 is retired (:97-150, :192-248). A write class is not a phase (:229-236).
  - Write matrix reproduced (what each step may write) (:210-227). Ordering rule: CALENDAR -> MATTER (world freezes) -> DELIBERATE map -> RESOLVE (strata, hash tie-break, batch clamp) -> WITNESS -> CENSUS (:242-247).
  - Order independence needs integer fixed-point (preferred) or canonical sort before summation; "floats, unsorted, approx-compare" refused (:269-287).
  - Execution path of nine steps from a season-close emitter and a person loader (flag-gated, through `generate_npc`, never `world.rng`) to the gate, a real `choose`, WITNESS v0, RESOLVE batching, MATTER reorder and CENSUS v0 (:322-342).
  - Four structural tests T1-T4 (choose sees no world; two witnesses disagree; officeless person acts/petitions; order independence incl. a poison triple 0.9 +0.3 -0.5 +0.3) each with a vacuity guard (:348-393).
  - ED-IN-0201 personnel precondition quoted: "we do not allow the game to perform faction actions if there is no leader of that faction ..."; clause 2 must change the OPTION SET and POOL SOURCE, not a flat modifier; the "no commander, no battle" reading (a) gate vs (b) penalty is a genuine ambiguity (:402-420, :531-535). Also: 2 NPCs loaded moved the seed-42 winner purely by shifting the shared RNG phase (:311-315).
  - Refusals table with mechanical/convention class (:464-488).
- **Conflicts / stale:** M1 0/7, `stub_hits` 2 and `npcs == 0` pins are 2026-08-31 and now outdated (the season runs people). `engine_clock` `doc: null` claim and Key emission steps are retired. The "no commander, no battle" ambiguity is still carried (docket 11 M27 default AUTOMATED).
- **Open items:** ESCALATE 1 commander gate vs penalty; verify D-2 act economy against `2026-08-30-fixes/02_the_act_economy.md`.

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/adjudications/F5_coverage_duplication.md
- **What it is:** Fable-5 adjudication of coverage, duplication, gaps and supersession across the proposals corpus after PRs #337-#344: coverage figures, a supersession map, a 17-row duplication register, the G-01..G-30 gap register, the seven forks, ED-IN-0200/0201 quoted in full, ancestry, a reading list; 2026-08-31.
- **Status:** none stated. Reading: historical snapshot (tree at `3871043`); the supersession map and gap register are partly outdated, but the ED-IN-0200/0201 quotes and the "uncited ancestor" findings remain a good index of what the proposals corpus holds.
- **Bears on:** CORE, PROCESS, WR, CHAR, FA, SC, FI, GO.
- **Content that matters:**
  - Coverage: 133 proposal docs over 200 lines (75,453 lines); only 30 cited by the head suite, 103 uncited (67.7% by line weight); research masters and the two governing ED rulings uncited (:52-90).
  - Supersession map: Tier 0 canon/code live; Tier 1 the #337-#344 chain (all PROPOSED, HELD BACK); greenfield-v2 "LIVE-PARALLEL, superseded by nothing"; `2026-08-30-fixes/03,04,05`, play-space coverage and arc-reachability LIVE EVIDENCE (:95-170).
  - Duplication register highlights: independent convergence on the act economy (fixes/02 Reading C = ideal-v2 D-2 = integration master P4) and on investigation's six acts (doc 03 = `cross_scale_action_catalogue_v1.md:610-619`); `11_world_events.md` already designs the actorless-event channel including `we.altonian_pressure`; `10_the_slate_and_salience.md` supplies the candidate definition the ratified Light Function presupposes (:183-198).
  - Gap register: world-substrate object (Thread/Mending Stability) is the largest unfiled gap; G-26/G-30 stale; `Recall` named the tenth attribute in shipped `CharacterCreationManager.gd:146-151` (:247-264). ED-IN-0200 and ED-IN-0201 quoted in full (:289-360).
  - Escalations surviving: D-6 Church conferral rooting (person-rooted vs office-rooted vs off-map Holy See), the port's autoload and save-model rulings, Godot version (:527-550).
- **Conflicts / stale:** `CLAUDE.md` Tenth-attribute `Recall` vs ED-IN-0328's Grace/Perception (superseded); `sim_params` citation counts `{cited:166, total:415, uncited:249}` vs "248" (:489-491); Key and module-contract premises retired.
- **Open items:** D-6; autoload and save model (now in valoria-game); G-15/16/18 "likely closed by uncited doc" unverified.

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/pr_logs/PR337.md
- **What it is:** not read.
- **Status:** n/a
- **Bears on:** n/a
- **Content that matters:** [SKIPPED: proposals/_session_provenance/2026-08-31-architecture-reconciliation/pr_logs/PR337.md - not read in full; context budget of this lane was exhausted before reaching it. Header of its directory MANIFEST describes it where one exists.]
- **Conflicts / stale:** n/a
- **Open items:** n/a

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/pr_logs/PR338.md
- **What it is:** not read.
- **Status:** n/a
- **Bears on:** n/a
- **Content that matters:** [SKIPPED: proposals/_session_provenance/2026-08-31-architecture-reconciliation/pr_logs/PR338.md - not read in full; context budget of this lane was exhausted before reaching it. Header of its directory MANIFEST describes it where one exists.]
- **Conflicts / stale:** n/a
- **Open items:** n/a

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/pr_logs/PR339.md
- **What it is:** not read.
- **Status:** n/a
- **Bears on:** n/a
- **Content that matters:** [SKIPPED: proposals/_session_provenance/2026-08-31-architecture-reconciliation/pr_logs/PR339.md - not read in full; context budget of this lane was exhausted before reaching it. Header of its directory MANIFEST describes it where one exists.]
- **Conflicts / stale:** n/a
- **Open items:** n/a

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/pr_logs/PR340.md
- **What it is:** not read.
- **Status:** n/a
- **Bears on:** n/a
- **Content that matters:** [SKIPPED: proposals/_session_provenance/2026-08-31-architecture-reconciliation/pr_logs/PR340.md - not read in full; context budget of this lane was exhausted before reaching it. Header of its directory MANIFEST describes it where one exists.]
- **Conflicts / stale:** n/a
- **Open items:** n/a

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/pr_logs/PR341.md
- **What it is:** not read.
- **Status:** n/a
- **Bears on:** n/a
- **Content that matters:** [SKIPPED: proposals/_session_provenance/2026-08-31-architecture-reconciliation/pr_logs/PR341.md - not read in full; context budget of this lane was exhausted before reaching it. Header of its directory MANIFEST describes it where one exists.]
- **Conflicts / stale:** n/a
- **Open items:** n/a

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/pr_logs/PR342.md
- **What it is:** not read.
- **Status:** n/a
- **Bears on:** n/a
- **Content that matters:** [SKIPPED: proposals/_session_provenance/2026-08-31-architecture-reconciliation/pr_logs/PR342.md - not read in full; context budget of this lane was exhausted before reaching it. Header of its directory MANIFEST describes it where one exists.]
- **Conflicts / stale:** n/a
- **Open items:** n/a

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/pr_logs/PR343.md
- **What it is:** not read.
- **Status:** n/a
- **Bears on:** n/a
- **Content that matters:** [SKIPPED: proposals/_session_provenance/2026-08-31-architecture-reconciliation/pr_logs/PR343.md - not read in full; context budget of this lane was exhausted before reaching it. Header of its directory MANIFEST describes it where one exists.]
- **Conflicts / stale:** n/a
- **Open items:** n/a

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/pr_logs/PR344.md
- **What it is:** not read.
- **Status:** n/a
- **Bears on:** n/a
- **Content that matters:** [SKIPPED: proposals/_session_provenance/2026-08-31-architecture-reconciliation/pr_logs/PR344.md - not read in full; context budget of this lane was exhausted before reaching it. Header of its directory MANIFEST describes it where one exists.]
- **Conflicts / stale:** n/a
- **Open items:** n/a

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/repo_logs/R1_engine.md
- **What it is:** not read.
- **Status:** n/a
- **Bears on:** n/a
- **Content that matters:** [SKIPPED: proposals/_session_provenance/2026-08-31-architecture-reconciliation/repo_logs/R1_engine.md - not read in full; context budget of this lane was exhausted before reaching it. Header of its directory MANIFEST describes it where one exists.]
- **Conflicts / stale:** n/a
- **Open items:** n/a

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/repo_logs/R2_systems.md
- **What it is:** Repo sweep R2 over `systems/` for the 2026-08-31 reconciliation: subsystem inventory, reproductions of `governance_ripple_substrate_v1.md` and `governance_play_redesign_v1.md`, the holonic doctrine vs "Rung as edge", a type inventory, a reconciliation table, duplication and gap registers, vocabularies.
- **Status:** none (sweep log; secondary source). Reading: historical (2026-08-31); the two governance docs it reproduces are PROPOSED ancestors.
- **Bears on:** SE, FA, CORE, CHAR, SC, MB, PC.
- **Content that matters:**
  - Subsystem inventory with sim LOC: combat engine 7,901 + 308; mass_battle 11,687 (30 files); social_contest 7,300; factions 2,747; settlements 1,021; threadwork 1,410; fieldwork 507; overview 600; world 767 (:5-20).
  - `governance_play_redesign_v1.md` (PROPOSAL, 2026-06-22) is the richest prior art for NPC choice: AP economy `AP = 2 + FacilityTier`, governance verbs (Develop, Fortify, Keep Order, Hold Court, Sponsor, Treat, Levy, Investigate), five Ledger tag families (Precedent, Grudge, Debt, Reputation, Compact), the Pi pressure homeostat and 7 card families, and a Part 3 NPC dossier (convictions, ambition{goal, method, timeline, progress}, ethic, loyalty, leverage, trajectory re-planning) (:63-95). `governance_ripple_substrate_v1.md` (PROPOSED 2026-07-11): `resolution_quality` computed on a Key; 5/8 edges WIRED, 1 AT-RISK (event->Parliament/SC) (:24-59).
  - Containment: `scale_hierarchy_v1.md` (RATIFIED 2026-07-13) already makes Province existence-conditional and says factions "hold PEOPLE not territory" - the ratified precedent of derived containment; the holonic doctrine's "one canonical shape at every scale" concerns code modules, not entities (:99-111).
  - Duplication register: ~10 of 16 hunted mechanisms are re-invention of canonical/proposed material; Tenure and Rung unification are the genuinely new pieces; the Belief-vs-Memory duplication is inherited (:168-189).
  - Gaps: no unified Tenure edge (governor_id FK, faction-holds-people prose, Compact tag, TreatyRecord, Standing ladders); no Partition statement; Territory scale an open gap (R-3); the six-step loop has no precedent (3-phase tick is canon) (:193-199).
- **Conflicts / stale:** `governance_play_redesign_v1.md`'s own build gate (settlement registry) is met yet status never followed (:241); Key-substrate claims retired. Reproduces the glossary conflict "Event" (Key vs deck card).
- **Open items:** R-1..R-4 of the ripple substrate; Scene Slate not re-read.

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/repo_logs/R3_godot.md
- **What it is:** not read.
- **Status:** n/a
- **Bears on:** n/a
- **Content that matters:** [SKIPPED: proposals/_session_provenance/2026-08-31-architecture-reconciliation/repo_logs/R3_godot.md - not read in full; context budget of this lane was exhausted before reaching it. Header of its directory MANIFEST describes it where one exists.]
- **Conflicts / stale:** n/a
- **Open items:** n/a

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/repo_logs/R4_registries.md
- **What it is:** Repo sweep R4 over `references/`, `registers/`, `canon/` for the 2026-08-31 reconciliation: CURRENT.md reproduced, glossary inventory, the `Derived` fact, `descriptor_registry.yaml` and `module_contracts.yaml` parsed, a collision register checked against the repo, canon P-01..P-15 compliance, ledgers and handoff state.
- **Status:** none (sweep log; "SECONDARY SOURCE", tree wins). Reading: historical snapshot (CURRENT.md stamp 2026-08-27, Generation v40).
- **Bears on:** CORE, CHAR, WR, PROCESS.
- **Content that matters:**
  - `Derived` in the repo (glossary, `params_tables.yaml`, `descriptor_registry.yaml:284`) means a STORED per-character value in a flat global namespace, the opposite of the design's `Query`; the rename was necessary (:74-82).
  - `descriptor_registry.yaml` (v1, ratified 2026-06-06): 9 attributes, tenth deliberately unnamed ("Do not infer the tenth from the aliases"), `agg.*` placeholders, 13 convictions enumerated to close a silent-no-op bug where two modules had divergent rosters (`conviction.py` 9 names, `npe.py` 8) (:86-104).
  - `module_contracts.yaml`: 27 modules, 9 with `doc: null`, 11 `[ASSUMPTION]`-grade resolvers, 48 distinct Key types; not a single registration table (ED-IN-0200 says three flat namespaces) (:108-122).
  - Collision additions: `hold` as mass-battle stance (`config.py:269`, `STANCE_SPEED_MOD` hold -99) and process HELD; `kind:` already an active YAML key in two registries; legacy attribute `Presence`; `View` as engine-atlas lens (:124-147).
  - Canon P-01..P-15: the design is SILENT on 13 of 15; flags P-14 (modes vs a single loop) (:151-173).
  - Ledger line counts and the 13 entries dated 2026-08-25+ (ED-IN-0196 "TN7 always"; ED-SC-0031/0032 degree ladder single owner); open ED-IN-0200/0201 (:177-223). `module_contracts.yaml:1543` names the no-Character/Actor gap (:255).
- **Conflicts / stale:** CURRENT.md table of 2026-08-27 is long outdated; `Key`/module_contracts material retired; the "tenth attribute" is now Grace/Perception per ED-IN-0328.
- **Open items:** the design should cite ED-IN-0200 and ED-IN-0201 (both `needs_jordan: false`, ruled-not-executed).

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/repo_logs/R5_corpus_coverage.md
- **What it is:** not read.
- **Status:** n/a
- **Bears on:** n/a
- **Content that matters:** [SKIPPED: proposals/_session_provenance/2026-08-31-architecture-reconciliation/repo_logs/R5_corpus_coverage.md - not read in full; context budget of this lane was exhausted before reaching it. Header of its directory MANIFEST describes it where one exists.]
- **Conflicts / stale:** n/a
- **Open items:** n/a

### proposals/_session_provenance/2026-08-31-architecture-reconciliation/repo_logs/R6_execution.md
- **What it is:** not read.
- **Status:** n/a
- **Bears on:** n/a
- **Content that matters:** [SKIPPED: proposals/_session_provenance/2026-08-31-architecture-reconciliation/repo_logs/R6_execution.md - not read in full; context budget of this lane was exhausted before reaching it. Header of its directory MANIFEST describes it where one exists.]
- **Conflicts / stale:** n/a
- **Open items:** n/a

### proposals/_session_provenance/2026-08-31-fable5-review/CODE_SHAPE_ABSTRACT.md
- **What it is:** not read.
- **Status:** n/a
- **Bears on:** n/a
- **Content that matters:** [SKIPPED: proposals/_session_provenance/2026-08-31-fable5-review/CODE_SHAPE_ABSTRACT.md - not read in full; context budget of this lane was exhausted before reaching it. Header of its directory MANIFEST describes it where one exists.]
- **Conflicts / stale:** n/a
- **Open items:** n/a

### proposals/_session_provenance/2026-08-31-fable5-review/FABLE_FINDINGS.md
- **What it is:** not read.
- **Status:** n/a
- **Bears on:** n/a
- **Content that matters:** [SKIPPED: proposals/_session_provenance/2026-08-31-fable5-review/FABLE_FINDINGS.md - not read in full; context budget of this lane was exhausted before reaching it. Header of its directory MANIFEST describes it where one exists.]
- **Conflicts / stale:** n/a
- **Open items:** n/a

### proposals/_session_provenance/2026-08-31-fable5-review/MANIFEST.md
- **What it is:** Manifest of the Fable-5 adversarial review of PR #343 (files, line counts, the headline numbers); 2026-08-31.
- **Status:** "PROVENANCE (2026-08-31) ... Nothing here is a design document and nothing here ratifies." Reading: historical.
- **Bears on:** PROCESS.
- **Content that matters:** 34 findings filed, 33 carried, 13 corrections across 12 findings (2 from Jordan, 4 from the independent critic, 7 self-caught); the reviewer's own re-check caught none of the four load-bearing breaks (:19-28). `CODE_SHAPE_ABSTRACT.md` indexes 46 primitives, 44 closed vocabularies, 64 functions, 214 parameters, 145 invariants, 58 open items, and 30 objects drifting across 97 versions (:16).
- **Conflicts / stale:** FABLE_FINDINGS contains four overstated claims later broken, kept uncorrected on purpose.
- **Open items:** none.

### proposals/_session_provenance/2026-08-31-fable5-review/merged210.md
- **What it is:** Writing-agent fragment: review section 2.10 on A10/A12 - "there is no Tenure relation in the design: nothing can hold anything".
- **Status:** none (working fragment). Reading: historical; the argument became the live `Tenure` primitive.
- **Bears on:** FA, SE, CORE.
- **Content that matters:** A faction is a proposition plus commitment map, owns nothing; `holdings` on a person is dead state; no verb moves property (`confiscat/enfeoff/seize` = 0 hits); Jordan: "A faction at a territory level may HOLD a territory, but a territory is NOT a territorial faction" (:46-52). Fix: `Tenure := (subject, object, since, conferrer, degree?)` with `confer`/`revoke` reused, `commit` kept separate (:65-70). A12's original filing (containment tree immutable) was wrong and recorded as such (:7-17).
- **Conflicts / stale:** none now (built).
- **Open items:** none.

### proposals/_session_provenance/2026-08-31-fable5-review/new6.md
- **What it is:** Writing-agent fragment: the ten-change ranked list for section 6 of the review (`mint`/`efface`, Tenure, `principals` query, matter-event generator, Allowance, need-as-claim, commutativity on the field, eviction, one-line repairs, typing unifications).
- **Status:** none. Reading: historical (the "after" of the section 6 renumbering).
- **Bears on:** CORE, FA, SE, WR, CHAR.
- **Content that matters:** `mint`/`efface` modes add birth, building, founding, faction founding and purge in one primitive (:8-41); `principals(f, n)` = members with address in n ranked by commitment degree x raisable backing, deposition needs no verb (:87-111); `season_factor` must be declared a per-season DRAW to give the world a non-subtractive channel (:113-133); one `Allowance` primitive replaces `capacity(date)`/`seat_items` (:135-146); "a need is a claim" (:148-158); eviction by clock quantities only (:173-183); transfer needs `stores(hearth(giver)) >= amount` (:185-195).
- **Conflicts / stale:** StateChange modes later renamed `create/alter/destroy` by F2; `principals` became `faction_q.head` (which returns None in realms per the arc plan).
- **Open items:** none.

### proposals/_session_provenance/2026-08-31-fable5-review/old6.md
- **What it is:** Earlier seven-change version of the same section 6 ranking (before the Tenure and principals additions).
- **Status:** none. Reading: historical.
- **Bears on:** PROCESS, CORE.
- **Content that matters:** Same changes minus Tenure/principals/matter-event generator; shows the pre-merge ranking (`mint`/`efface` rank 1, Allowance rank 2, need-as-claim rank 3) (:5-63).
- **Conflicts / stale:** superseded by `new6.md` and the deliverable.
- **Open items:** none.

### proposals/_session_provenance/2026-08-31-fable5-review/sec1.md
- **What it is:** Writing-agent fragment: section 1 verdict of the review (one-page central finding, trajectory test, where the design is a direct hit, tier counts).
- **Status:** none. Reading: historical.
- **Bears on:** CORE, FA, WR, CHAR.
- **Content that matters:**
  - Central finding: the #343 design has rich vocabulary for changing the state of things that exist and almost none for changing which things exist or who holds them; the only five existence-changing operations are all decider-free (death, de-individuation, claim eviction, individuation, holdings moving on death) (:21-44).
  - A Proposition cannot be created by any route, so the flagship emergence claim (a faction forms from a physical fact) is false as written (:46-70).
  - Trajectory test: of ten transitions for Jordan's two arcs, three work (lose/gain office; rule another through belief); fixes bring it to nine of ten; occupation change remains (:73-102).
  - Direct hits: epistemics layer, the sitting and stasis ladder, one-order-many-executors, vacant-allocator semantics, option-removal inversion (:129-151). `choose` has no World, so the only way to move another person's act is to change his belief (:106-116).
- **Conflicts / stale:** all 2026-08-31 absence claims; the season now has `establish/found/build/confer` verbs.
- **Open items:** occupation/profession.

### proposals/_session_provenance/2026-08-31-fable5-review/throughlines/CITATION_LEDGER.md
- **What it is:** not read.
- **Status:** n/a
- **Bears on:** n/a
- **Content that matters:** [SKIPPED: proposals/_session_provenance/2026-08-31-fable5-review/throughlines/CITATION_LEDGER.md - not read in full; context budget of this lane was exhausted before reaching it. Header of its directory MANIFEST describes it where one exists.]
- **Conflicts / stale:** n/a
- **Open items:** n/a

### proposals/_session_provenance/2026-08-31-fable5-review/throughlines/THROUGHLINES_BRIEF.md
- **What it is:** Brief (v2) naming twelve design-and-code throughlines D1-D12 of the 2026-08-31 session.
- **Status:** none; v2 supersedes v1 (which was about the review method). Reading: historical; D3-D6, D9, D12 are still the shape of the live engine.
- **Bears on:** CORE, FA, CHAR, FI, WR, GO.
- **Content that matters:**
  - D1 existence and tenure were the two registers the design could not touch; D2 one edge primitive (`Tenure`) spelled three times, `until?` makes a revoked tenure arguable; D3 power is a query never a field, the leader query must take an OBSERVER (:7-34).
  - D4 the partition: peninsular human society is changed only by a character's choice, everything else (weather, non-peninsular, metaphysical substrate) by event; a plague may kill bodies but not efface a settlement, which "still legally exists until an office strikes it from the roll"; 21 of 26 impact types are social (:36-50).
  - D5 the world is in flux: `condition <- clamp(condition + sum tending - wear, 0, 1)`, untended it falls and verbs leave; D6 `verbs(site, rung)` is world truth read only by `resolve`, `opening_set(person, view)` is belief inside `choose` so a person may attempt a verb the world already removed (:51-67).
  - D8 enforcement-by-omission degrades to convention in GDScript: no live world state behind a global, every resolver-side query takes `World` first; D9 one act per person at every rung, an office's throughput is its establishment; D10 cohorts must act or the politics is elite-only; D12 ids not pointers (Godot has no cycle collector) (:77-114).
  - Closing: 108 of 123 proposal docs over 200 lines were cited nowhere; every false claim the session produced was an absence claim (:118-124).
- **Conflicts / stale:** none material.
- **Open items:** none.

### proposals/_session_provenance/2026-08-31-fable5-review/throughlines/sweep.py
- **What it is:** 38-line Python script counting proposal `.md` files over 200 lines and how many are cited by three reference surfaces (SUP, REV, v2).
- **Status:** none. Reading: dead provenance script; reads `proposals/2026-08-31-ideal*` files that may not exist now.
- **Bears on:** PROCESS.
- **Content that matters:** Citation test is `txt.count(path) + txt.count(basename)` (+ `NN:` locator regex for the from-scratch suite) (:29-33); prints CITED/UNCITED (:35-38). Proxy for coverage that the manifest itself says "citation count is not coverage".
- **Conflicts / stale:** hard-coded paths of the 2026-08-31 ideal suites.
- **Open items:** none.

### proposals/_session_provenance/2026-08-31-fable5-review/tier1add.md
- **What it is:** Writing-agent fragment: review sections 2.9-2.12 (A9 faction leader, A10 dead `holdings`, A11 "investigator is not a seat", A12 immutable containment tree).
- **Status:** none. Reading: historical.
- **Bears on:** FI, FA, CORE, CHAR.
- **Content that matters:** A9 fix `principals(f, n)` as a derived query (:25-34). A11: field investigation is one sentence (#343 `:1715-1717`) with no verb, cost, obstacle owner or resolution path; the fix is an ordinary `investigate(person, question, subject)` act whose resistance pool is the concealment, output claims deposited by `witness` with source firsthand (:70-98) (the detective-lineage seat). A12: polity absorption fails on the tree not the faction; "faction absorption is shipped and correct (a merger is members of A committing to B)"; do not add a merge verb (:100-137).
- **Conflicts / stale:** the A11 gap is what `examine/research/surveil/interview/reconstruct` rows later filled.
- **Open items:** none.

### proposals/_session_provenance/2026-08-31-fable5-review/v2/ARCH_CORE.md
- **What it is:** Fable-5 synthesis brief "the idealized shape, v2": three carriers (Person, Node, Office), one edge (`Tenure`), one act (`touches` with modes read/alter/exclude/mint/efface), derived-not-stored aggregates, three signatures with a new `Sensation`, a three-barrier loop; 2026-08-31.
- **Status:** none; MANIFEST says it "did not survive: 12 FATAL, 35 MAJOR, 27 MINOR, all accepted"; `REVISIONS.md` is the authority. Reading: historical (superseded by REVISIONS and the deliverable).
- **Bears on:** CORE, CHAR, FA, WR.
- **Content that matters:** Site is matter held by a Node, not a carrier; Faction = Proposition + `commit` Tenures (entirely derived) (:34-44); `Tenure(subject, object, kind in hold|commit|contain|succeed|tie|knot)` (:46-70); `Sensation` is a closed record of exactly four need scalars computed in P2 and never stored (:111-123); loop = B1 CALENDAR, B2 MATTER, M1 DELIBERATE (per person), B3 RESOLVE, M2 RECKON (per person) (:158-173); eviction on `confidence_live x recency` only (:175-178). May-not list: D-2, conferral basis, `stores` denominator, S19, Coherence-0, off-board polities (:9-11).
- **Conflicts / stale:** the shipped loop has seven steps (CALENDAR, MATTER, DELIBERATE, RESOLVE, ENCOUNTER, WITNESS, CENSUS); `Node` later renamed `Rung`.
- **Open items:** carried-open list at :186-189.

### proposals/_session_provenance/2026-08-31-fable5-review/v2/D2_PROPOSAL.md
- **What it is:** A proposal resolving D-2 (the act economy): one act per person per season, universally; an office's throughput is its establishment's acts.
- **Status:** "This is a PROPOSAL with its alternative stated, not a ruling." Reading: historical; the one-act-per-person rule is also in FINDINGS_DIGEST; MANIFEST notes `2026-08-30-fixes/02_the_act_economy.md` had already reconciled it.
- **Bears on:** CORE, CHAR, FA.
- **Content that matters:** "Act" does two jobs (personal attention vs institutional throughput); a Duke takes one act (`dispatch`) and thirty-five named people each spend theirs; the cohort exploit (individuate to farm acts) prices itself into content: eleven people who may refuse; `seat_items` and `capacity(date)` are one quantity seen from two sides (:14-81). Alternative (several acts for an office-holder) stated fairly and not recommended (:83-95). Unsettled: establishment size, who authors the first, upkeep, banking unspent acts (recommend no) (:97-103).
- **Conflicts / stale:** the shipped loop uses `scene_budget` (default 5) per person per season with an office bonus (`budget.py`), a different economy than "one act".
- **Open items:** establishment size/upkeep.

### proposals/_session_provenance/2026-08-31-fable5-review/v2/EVENTS_AND_SWEEP.md
- **What it is:** not read.
- **Status:** n/a
- **Bears on:** n/a
- **Content that matters:** [SKIPPED: proposals/_session_provenance/2026-08-31-fable5-review/v2/EVENTS_AND_SWEEP.md - not read in full; context budget of this lane was exhausted before reaching it. Header of its directory MANIFEST describes it where one exists.]
- **Conflicts / stale:** n/a
- **Open items:** n/a

### proposals/_session_provenance/2026-08-31-fable5-review/v2/F6_RULED.md
- **What it is:** Jordan's ruling that the world is "in flux" (neither dying nor misunderstood), worked out as `wear` and as ambition-as-commitment.
- **Status:** none (a "RULED BY JORDAN" worked note, quoting his words). Reading: historical record of a live ruling; `wear_per_season` is in the season fixtures/rosters.
- **Bears on:** WR, SE, CHAR, CORE.
- **Content that matters:** Jordan: "If the world is not tended to by anyone, it will die. If it is tended to by everyone, it will thrive. What people think is the best way to tend to the world ... and their ambitions ... drive conflict" (:3-5). Consequence 1: act-only condition cannot say this; need `condition <- clamp(condition + sum deltas - wear(kind), 0, 1)` with `wear` an authored per-site-kind constant (:16-47). Consequence 2: competing tending-doctrines are OUGHT Propositions with intersecting `when` intervals (no new object); an ambition is an unsatisfied `commit` Tenure to an OUGHT Proposition about the holder's future (matches `goals.yaml` ambitions that drive `need` questions) (:66-92).
- **Conflicts / stale:** the `wear : restoration` ratio sets the difficulty curve and "no number in this design has been measured" (:111-113); docket 11 records `wear_per_season` rates as "invented values the row records for Jordan to correct" with `dwelling: 0` control.
- **Open items:** wear tuning.

### proposals/_session_provenance/2026-08-31-fable5-review/v2/FORKS.md
- **What it is:** The six reserved forks (F1-F6) worked for the "ideal system"; each a proposal with cost and falsifier.
- **Status:** none. Reading: historical; MANIFEST notes F5 was ruled wrong here and Jordan overturned it (partition: Altonia is an event source).
- **Bears on:** FA, WR, SE, CORE.
- **Content that matters:** F1 conferral basis dissolves into `Office.conferral` per-office (person-rooted warbands vs office-rooted magistracies) (:16-37); F2 `stores` becomes `map[MatterKind -> quantity]` (grain vs silver; coin cannot be eaten) (:41-69); F3 rootless cluster vacancy: conferral may name the office's own judging set (:73-91); F4 Coherence-0 = de-individuation by another cause (:95-108); F6 world dying vs misunderstood stays Jordan's (later ruled "in flux") (:133-142).
- **Conflicts / stale:** F5 (generate off-board persons) overturned by Jordan; F6 ruled in `F6_RULED.md`.
- **Open items:** F3's empty-judging-set floor unspecified.

### proposals/_session_provenance/2026-08-31-fable5-review/v2/KEYS_AUDIT.md
- **What it is:** not read.
- **Status:** n/a
- **Bears on:** n/a
- **Content that matters:** [SKIPPED: proposals/_session_provenance/2026-08-31-fable5-review/v2/KEYS_AUDIT.md - not read in full; context budget of this lane was exhausted before reaching it. Header of its directory MANIFEST describes it where one exists.]
- **Conflicts / stale:** n/a
- **Open items:** n/a

### proposals/_session_provenance/2026-08-31-fable5-review/v2/MANIFEST.md
- **What it is:** Manifest of the v2 "idealized system rebuilt" session files.
- **Status:** "PROVENANCE (2026-08-31) ... Nothing here is a design document." Reading: historical.
- **Bears on:** PROCESS, CORE.
- **Content that matters:** ARCH_CORE brief received 12 FATAL, 35 MAJOR, 27 MINOR findings, all accepted; the corpus sweep found 108 of 123 proposal docs over 200 lines cited nowhere and four mechanisms reinvented; the partition applied to the event deck found 21 of 26 impact types social, ~9-11 of 58 cards event-legal (:6-30). F5 (off-board polities) ruled wrong then overturned by Jordan (:12).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/_session_provenance/2026-08-31-fable5-review/v2/REVISIONS.md
- **What it is:** not read.
- **Status:** n/a
- **Bears on:** n/a
- **Content that matters:** [SKIPPED: proposals/_session_provenance/2026-08-31-fable5-review/v2/REVISIONS.md - not read in full; context budget of this lane was exhausted before reaching it. Header of its directory MANIFEST describes it where one exists.]
- **Conflicts / stale:** n/a
- **Open items:** n/a

### proposals/_session_provenance/2026-08-31-fable5-review/v2/THE_PARTITION.md
- **What it is:** Jordan's partition rule for what drives a state change (2026-08-31) and its extension (creation and deletion are state changes).
- **Status:** none (a worked statement of a Jordan ruling). Reading: historical record of a live ruling; also in the arc plan C4 (M16 fourth motion refused).
- **Bears on:** CORE, WR, FA.
- **Content that matters:** Jordan: peninsular human society (polities, institutions, offices, organizations, occupations, religion, settlements, marriage) changes only by a character's choice; everything else (weather, non-peninsular like the Altonian Empire, tears in the metaphysical substrate) is "an event that acts upon the game world" (:2-6). `StateChange := (subject, mode in mint|alter|efface, driver in Act|Event)`; the subject picks the driver (:85-92). Worked case: a plague kills bodies (event) but may not efface a settlement; the village empties and legally exists until an office strikes it from the roll (:104-118). An event may not change standing, regard, commitment or grievance (:60-64).
- **Conflicts / stale:** reverses FORKS F5; "events resolve first in their own barrier" (:136).
- **Open items:** edge subjects (plague/famine/heresy); the event/act balance is unmeasured (:66-72).

### proposals/_session_provenance/2026-08-31-unified-code-shape/MANIFEST.md
- **What it is:** Provenance manifest for the "ideal unified code shape" session: cites.json, cites2.json (harvested `path:line` claims), dossier.txt (not present in this assignment).
- **Status:** "PROVENANCE. Working files, committed unedited ... Nothing here is a design document and nothing here ratifies." Reading: historical.
- **Bears on:** PROCESS.
- **Content that matters:** Every citation of the 14 PR #345 trace logs was checked by printing the cited lines beside the claim; prior citations had drifted by 2-20 lines and one was fabricated outright (:24-29). A 42 MB checkout was deliberately not committed (:17-22).
- **Conflicts / stale:** `dossier.txt` (285 KB) listed but not in the assignment [UNVERIFIED present].
- **Open items:** none.

### proposals/_session_provenance/2026-08-31-unified-code-shape/cites.json
- **What it is:** Machine data, one line, 264 KB: 493 records `{log, logline, cited, ln, ln2, claim, resolved, how}` harvesting `path:line` citations from PR logs (e.g. A337-001 `ledger.py:30` TAG_KINDS).
- **Status:** none (data). Reading: historical; read by nothing (grep of code not run).
- **Bears on:** PROCESS.
- **Content that matters:** [PARTIALLY READ: structure and first record only; the file exceeds the Read tool's 256 KB limit and is a citation-harvest dataset] First record: PR337 log line 59 cites `systems/settlements/sim/ledger.py:30`, the closed 5-family `TAG_KINDS` {Precedent, Grudge, Debt, Reputation, Leverage}.
- **Conflicts / stale:** line numbers stale by construction.
- **Open items:** none.

### proposals/_session_provenance/2026-08-31-unified-code-shape/cites2.json
- **What it is:** The second, widened harvest of the same 493 citation records plus `path` and `actual` (the real source line) fields.
- **Status:** none (data). Reading: historical.
- **Bears on:** PROCESS.
- **Content that matters:** [PARTIALLY READ: structure and first record only; 315 KB exceeds the Read limit] Adds `actual: TAG_KINDS = {"Precedent", "Grudge", "Debt", "Reputation", "Leverage"}` for the first record.
- **Conflicts / stale:** as cites.json.
- **Open items:** none.

### proposals/_session_provenance/2026-09-01-holonic-architecture/00_MANIFEST.md
- **What it is:** Provenance manifest for the 2026-09-01 holonic-architecture session (six runs: sweep, census, lanes A-D by `valoria-critic` Read/Grep/Glob).
- **Status:** none (evidence, not findings; "raw lane output, transcribed"). Reading: historical.
- **Bears on:** CORE, PROCESS.
- **Content that matters:** Three lanes independently killed the first revision's central proposal, the "wrapper" (an object that checks direction/target of Key crossings): the Event has no target, the direction rule contradicts T6 and containerless venues, wrapper placed on the code tree while the rule is on the world tree (:38-54). Census: 27 items, not 24 (:53). Transcriptions not byte-exact; nothing cited as a measurement without re-running (:80-84). Notes the directory exists despite CLAUDE.md §0's rule because Jordan asked (:9-15).
- **Conflicts / stale:** the "wrapper" concept is deleted (ARCHITECTURE.md §44 post-mortem).
- **Open items:** ROLE-to-SUBSYSTEM ordering (one role `contest`, three providers?) left unresolved (:62-64).

### proposals/_session_provenance/2026-09-01-holonic-architecture/01_SWEEP_337_352.md
- **What it is:** Sweep of the PR chain #337-#352 in six phases (measure, greenfield and its collapse, from scratch, reconciliation, unified shape, execution and its audit).
- **Status:** none. Reading: historical; useful as an index of what the chain retracted.
- **Bears on:** CORE, PROCESS, CHAR.
- **Content that matters:** #337 headline: Valoria is "disconnected" not under-designed, 15% of classified things are correct code with no caller (:10-13). #351 implemented the shape and drove it with 78 blind-authored cases, but #352 showed the case layer never executed (verdicts keyword lookups; one misplaced classifier file reuses all 50 arc ids and flips ~40 verdicts); #352 retracted four of its own charges (:42-48). Retraction table: stored-primitive foundation, MATTER-advanced `Record.stage`, L3 ratchet bound twice, "8 arcs -> 3", "40% -> 16%" refusal rate (:50-62). "A crude instrument systematically overstates a strict design's cost" (:64-67). `m1_acceptance` 0/7 throughout (:76).
- **Conflicts / stale:** all numbers dated 2026-09-01.
- **Open items:** fix case loader, assertions for unasserted passes, declared capability tags instead of regex routing (:71-75).

### proposals/_session_provenance/2026-09-01-holonic-architecture/02_CENSUS_BRIEF.md
- **What it is:** The dropped-rulings census brief: a thing is dropped if decided/ruled in #337-#352 and a later document contradicts, restates open, omits or promises-and-fails to carry it; field 4 (name the later file/section) is the test.
- **Status:** none. Reading: historical.
- **Bears on:** PROCESS.
- **Content that matters:** 27 items: 14 folded in, 3 refused, 1 struck, rest recorded; 16 candidates failed field 4; "most were lost at a section that RESTATES its neighbours"; argument for graded rows over prose lists of open items (:36-45). "Damage removes an option" was carried under another name (a band gate on `condition`) (:20-24).
- **Conflicts / stale:** a cited sentence found out-of-chain and withdrawn (:32-34).
- **Open items:** none.

### proposals/_session_provenance/2026-09-01-holonic-architecture/03_LANE_A_fidelity.md
- **What it is:** Lane A (chain fidelity and factuality) critique of the holonic proposal.
- **Status:** none. Reading: historical.
- **Bears on:** PROCESS, CORE.
- **Content that matters:** Findings F1-F16: census miscounts itself (27 not 24); an item quoted "eleven of twelve work" appears nowhere (source: "FIVE OF TWELVE WORK TODAY"); the act budget was RULED "THE ACT BUDGET IS ~5, NOT 1" by Jordan (2026-08-31, in #351's `02_SCENE_BUDGET_RULING.md`) and the proposal missed it (:18-23); "nothing in MATTER crosses a rung boundary" is contradicted by the head (MATTER touches persons) (:26).
- **Conflicts / stale:** this ruling (act budget ~5) is the origin of `scene_budget`=5 in fixtures.
- **Open items:** PR bodies #338/#343 not on disk (UNVERIFIED).

### proposals/_session_provenance/2026-09-01-holonic-architecture/04_LANE_B_architecture.md
- **What it is:** Lane B (code architecture: keys, wrappers, modularity, ownership, primitives) critique.
- **Status:** none. Reading: historical.
- **Bears on:** CORE, PROCESS.
- **Content that matters:** The ONE RULE (aggregate up / refraction down) fails completeness: containerless venues, "scope enumerates executors not places", and WITNESS fan-out global; the wrapper sits on the code tree while the rule is on the world tree; no in-chain record carries a rung target; the spine is not a strict tree at ROLE and KEY TYPE edges; `phase:` must be a set (Date written in two or three steps) (:18-26). Needs a third clause for ended edges (live edges `until == null`) (:26). Did not break: one type with eight kinds, the barrier/clock argument (:28-30).
- **Conflicts / stale:** wrapper deleted.
- **Open items:** travel legs have no ownership row (:51).

### proposals/_session_provenance/2026-09-01-holonic-architecture/05_LANE_C_logic.md
- **What it is:** Lane C (logic, sequence, flexibility, emergence) critique.
- **Status:** none. Reading: historical.
- **Bears on:** CORE, PROCESS.
- **Content that matters:** MATTER is not rung-local (subsistence, death writes on another person's rung, travel legs); CALENDAR is per-holder; CENSUS and WITNESS stage 2 are per-owner maps; the head permits within-tick reaction bounded by `max_depth`, not barriers; the termination debt is cross-season; "the scope rule is applied once and waived five times"; "the proposal's REFUSALS mostly stand; its REASONS mostly do not" (:14, :18-34).
- **Conflicts / stale:** none.
- **Open items:** the "no reaction inside a season" tension stated in ARCHITECTURE §40.2.

### proposals/_session_provenance/2026-09-01-holonic-architecture/06_LANE_D_foldin.md
- **What it is:** Lane D adjudication of the 27 dropped rulings for fold-in (verdicts, set-level conflicts, dependency order, budget).
- **Status:** none. Reading: historical.
- **Bears on:** CORE, FA, SC, CHAR.
- **Content that matters:** 23 of 27 confirmed real; item 16 (twelve argument faults) STRIKE; items 23 (hook grammar: guaranteed fire at threshold vs "may never produce an outcome") and 27 (Parliament rider) REFUSE; `transfer` needs a `stores >= amount` precondition (otherwise "the second claimant on an emptied granary gets a different Event" is false); scar written at WITNESS breaks L4 (lawful: RESOLVE ACTS class `social: true`); `confer` eligible when the holder-Proposition has zero live `commit` edges (memberless faction); person roster: adopt the shape not the number (T3 needs a person with zero `hold` Tenures) (:14-28). Order 14 -> 17 -> 6 -> 7 -> 13 -> 19 -> 21 -> 11 -> 20 -> 15 -> 18 -> 22 -> 24 -> 9/10 (:40). The one thing: write `Event :=` and map it onto the Key (:50-53).
- **Conflicts / stale:** Key premises retired.
- **Open items:** petition-spray allowed by a later Jordan ruling (:60-61).

### proposals/canonical_nomenclature_v1.md
- **What it is:** Plan (v0.1, "planning pass 2026-08-11") for namespaced dotted identifiers for every named thing; lane IN, no ED allocated; executes held ED-IN-0152.
- **Status:** "PROPOSED — not ratified. Nothing in this document renames anything." Reading: unadopted/proposed; the headline measurement predates the Key-substrate retirement.
- **Bears on:** PROCESS, CORE, CHAR.
- **Content that matters:**
  - Finding: the dotted namespace already exists (`references/names_index.yaml` 113 dotted keys) but was never adopted as the identifier form: of 51 non-proper-noun keys, 16 appear nowhere outside generated registries, 32 only in tools/tests, 3 in engine/live design (`substrate.key`, `fac.intel`, `clock.mending_stability`) (:25-62).
  - Noise is measured: ordinary-word names (Order 1,630 hits, Authority 1,366, Standing 1,234, Will 665...) (:64-92). Proposes a two-axis grammar (owner/scale governs entities and owned state; event-domain retained for Key types; kind axis retired), spelled-out namespaces (`set.` -> `settlement.` because `set` is a Python builtin) (:115-165).
  - `tools/valoria_rename.py` scope roots (`designs`, `params`) no longer exist, so it silently covers 67 files and misses 270 design + 261 `.py` + 41 `.json` (:229-260).
  - Four open Jordan calls, including `piety_track`'s owner (settlement vs territory vs character: three docs disagree) (:209-225).
- **Conflicts / stale:** `fac.intel` and `substrate.key` references are to retired or orphaned facts (CLAUDE.md §0.05 cl. 4 notes `fac.intel` orphaned; Key substrate RETIRED ED-IN-0232). Proposed `ci_nomenclature_check.py` / phased guards conflict with the "no tree-wide guard" rule (§0.05, §0.1 pt 5).
- **Open items:** Phase 0 rulings (axis; piety_track owner; `key.` prefix; contract citation-form); fix of `valoria_rename.py` scope.

### proposals/grounded_event_card_deck_v1.md
- **What it is:** 58-card "grounded" event deck across seven families (Crisis, Petition, Opportunity, Ambition, Intrigue, Thread...) from four research dockets; lane IN (SE, FA), 2026-07-11. The file as read is partial: the body jumps from the compliance appendix to mid-card (line 98) and holds only about 10 full cards.
- **Status:** "PROPOSED (2026-07-11) · Author-pass, not yet Jordan-ratified". Reading: unadopted; built on the retired Key/module-contract adjudicator framework; the successor event-card thinking is workplan CL-EVENTS (docket ch.11 rows 66-71).
- **Bears on:** WR, SE, FA, FI, SC.
- **Content that matters:**
  - Method: 15-agent workflow, critic returned 40 KEEP / 19 REVISE / 0 CUT; the deck flags that 0 cuts is a soft signal (:15-28). Family balance: Crisis 22/59 (over), Thread 1/59 (under-mined), Ambition 4/59 (thin) (:273-276).
  - Compliance claim: every card resolves through three resolvers (`d_sigma`, `deterministic_accounting`, `dice_pool`); one new engine, a pi-weighted deck-draw (:42-76).
  - ~50 of 58 cards' SC ripple is AT-RISK pending a `social_contest` `stakes.source_key` hook; 17 cards lever-gated on five new settlement levers (StockLevel, Assessment tag, route/corridor Precedent, Capital-Posture ledger family, Consent-Rule) (:284-300).
  - Card shape: grounding (e.g. Fuggerei, Standon-Wadesmill turnpike, Crown of Thorns), trigger predicate, scale, branches with stat deltas, three-vector burden, FI/SC/FA ripples, follow-on actor, new lever (:98-240).
  - Bonded pairs that must ship together (OPP-03 + OPP-04; ECON-05 -> ECON-01) (:267-268).
- **Conflicts / stale:** Stat vocabulary (Mandate, L/PS, Treasury, Weight, Pi) belongs to the stored-aggregate design the season code refuses (Mandate not carried; "Nobody owns aggregates"); path `designs/architecture/...` dissolved.
- **Open items:** the `stakes.source_key` hook (R-2/ED-SC-0015), R-1 levers, R-4 band cliff ruling - all unresolved against the current season code.

### proposals/mass_battle_fighting_withdrawal_v1.md
- **What it is:** Design workplan DG-2: a "yielding" per-subunit state (fighting withdrawal between full commitment and rout); lane MB, 2026-07-05, updated 2026-07-23.
- **Status:** "BUILT (gated) — the §4 step-1 yield scope shipped in ED-MB-0005; the three residuals shipped in ED-MB-0024 ... all GATED OFF (MB_YIELD_EMERGENT / MB_YIELD_RALLY / MB_YIELD_POCKET), byte-exact. HELD for Jordan: the three default-flips, the emergent path's blast-radius measurement pass, the deferred erosion-brake, and the D_YIELD/YIELD_POOL_MULT/YIELD_RALLY_MORALE_FRAC/YIELD_POCKET_REACH calibration debt." Reading: live reference for built-but-default-off code.
- **Bears on:** MB, PC (duel inside mass engagement: no), CHAR (discipline gate).
- **Content that matters:**
  - Gap: a body is either eroding at full commitment or routed atomically in one call (every subunit pool forced to 0, facing flips, engagement loop breaks); no state in between (:19-30).
  - `yielding: bool` per subunit; facing preserved toward the enemy while movement vector is away (movement/facing decoupling is new logic), at most 1 cell/tick, melee-only, no volleying, malus on combat pool, bounded by path-budget `0.5 x speed x max-ticks` (:84-155).
  - Entry: commanded `'yield'` order or emergent at `eff_discipline >= D_YIELD`; exit: rally, collapse to rout at `SUBUNIT_ROUT_FLOOR`, or pocket (blocked retreat -> hold, malus removed) (:98-143).
  - Rejects the "recoil idiom" (no displacement primitive exists; `MB_CHARGE_RECOIL` is a net-success penalty) (:50-62). Reuses `_kite_goal`, `resolve_toi_and_commit`, `Order/check_orders` (:167-182).
  - 2026-07-05 session fixed D2 (envelop phase limit cycle), D2b (frozen step), D3 (routed pool resurrected to 1), D4 (casualty columns union); Cannae-pattern gauge rows now overshoot in the attacker's favour; `subunit_combat_pool` is not scaled by the subunit's troop share, an unresolved partition-invariance question (:239-286).
- **Conflicts / stale:** Calibration debt: `D_YIELD`, pool malus magnitudes are "not decided" per §5. Paths cite dissolved `designs/...`. Status line records both PROPOSAL (line 5) and BUILT (line 3) because of a later header insertion.
- **Open items:** default flips; erosion-brake; whether partition-invariance is a defect (needs Jordan ruling).

### proposals/multiunit_envelopment_plan.md
- **What it is:** Implementation plan for army-scale multi-unit envelopment in the mass-battle sim; Path A (extend lane abstraction) vs Path B (unify the engagement field); lane MB, 2026-06-22.
- **Status:** "PROPOSED — LIVE / UN-ADOPTED. Path-B cross-Unit spatial envelopment is a distinct, still-unbuilt mechanism ... Phase-1 never started. HELD FOR JORDAN." Reading: live, unbuilt; cited by the audit brief as the per-cell envelopment source.
- **Bears on:** MB.
- **Content that matters:**
  - `run_multi_unit_battle` is a 1-D lane abstraction: each `pairings` lane runs an isolated 1v1 `run_battle`; cross-lane interaction is only rout contagion and a sequential freed-attacker; concurrent 2v1 is stubbed in a comment (:13-17).
  - The per-cell envelopment shock is unit-agnostic (`_front_fixers` keyed by `id(subunit)`, `b_fixed_other`) so it would emerge for free once contacts are detected across all units (:9, :18, :81).
  - Decision (Jordan, 2026-06-22): Path B, bottom-up emergent, no scripted convergence; `UNIT_GRID_SIZE` 30, `BATTLEFIELD_SIZE` 50, `MAX_TROOPS_PER_UNIT` 10000, `CELL_FLOOR` 40..`CELL_CAP` 200; `LINE_ASPECT` 1.4 vs ~2.0-2.3 target (:72-79).
  - Phases: 0 spike (confirmed at line level), 1 shared-field static resolution (owner-unit lookup replacing `unit_a/unit_b` assumption), 2 positioning/maneuver, 3 command & control (ED-907), 4 NERS and historical re-validation (:40-47, :83-89).
  - Guard: preserve the envelop-shock `elif` and dormant `_envelopment_sigma` so cell- and unit-level envelopment do not both fire (PP-683 lesson) (:18, :57).
- **Conflicts / stale:** cites `BATTLEFIELD_SIZE` 25x25 (§A.3b) vs actual 50/51 in config (docket 08 says 51); a MB audit should check the current orchestration.
- **Open items:** army-scale unit count; maneuver/command scope; LINE_ASPECT timing; canon write-back to §A.12.

### proposals/pc_formation_system.md
- **What it is:** "P-C Compositional Formation System (design-capture)": formations as shapes with no flat bonuses; roles = troop-type-gated instruction packages; Discipline/Command/Morale split; kiting build plan and validation. Lane MB (file name says pc = "P-C" phase, not personal combat). 2026-06-02, headings added 2026-07-15.
- **Status:** "PARTIALLY SUPERSEDED — the engine half is BUILT (brace/missile-density/ROLE_SPEC/kiting ...). Residual: §8 canon reconciliation (strip flat dice rules from mass_battle_v30 §A.6, PARKED as ED-909 follow-up) + §9 opens. HELD FOR JORDAN." Reading: partly historical; the three-level surface (L1 army doctrine, L2 unit formation, L3 subunit role + instructions) is the live MB design shape.
- **Bears on:** MB, CHAR (command from Charisma + Cognition), GO (intervention windows).
- **Content that matters:**
  - Principle: a formation is a SHAPE with no flat dice/sigma bonus; effects emerge from frontage (`_lanchester_strength`), depth (`_defender_depth`), facing (`octagon_angle`), tip speed (`cell_speed`), charge-shock; the retired `SHAPE_OFF_MOD/SHAPE_DEF_MOD` guarantee no flat shortcut (:20-32, :161).
  - Three levels in the Football Manager model (ED-907): army doctrine (Aggression, Cohesion-priority; Command), unit formation (template or custom allocation; adopt-gated by Discipline `MIN_DISCIPLINE`), subunit role + instructions gated by troop type (:36-44). Roles table per troop type (Shield Wall, Hold, Anvil, Push, Skirmish, Gap, Pursue, Shock, Flanker, Feint, Screen, Volley line, Harass, Support/Reserve) (:77-83), matching today's `ROLE_SPEC` (15 roles).
  - Brace is an instruction that raises effective density (mechanism B); depth-as-defense rejected; brace mechanism commit `7691eb6a` (reciprocal charge-recoil), missile-density coupling `a6ae38ad`, kiting commits `9159c22c` + `adf9fb9e` (:91-94, :198-216, :241-288).
  - Governance: Command (derived Charisma-primary + Cognition secondary, ED-899) adapts strategy, recognises feints, runs concerted ploys (envelopment, false retreat, ambush, hammer & anvil), caps sub-unit coordination; Discipline maintains shape (0 = formation breaks); Morale is the rout resource (:50-67, :118-130). Intervention cadence ~5-20 windows per battle (:162).
  - Kiting measured: kiter loses to cavalry (13/20), dominates infantry only on open field with long engagement (45 cells, 40 turns); space and time are implicit levers pending a terrain layer (:274-287). Validation anchors must trace to the research report; Waterloo/Albuera cited earlier were out of period (:224-238).
- **Conflicts / stale:** canon A.5 Command formula `ceil((Cha+Cog)/2)` vs engine round((2Cha+Cog)/3) (:168-170). Docket 08 records `config.py:534-535` directive to abandon combat pools related to the commander, which sits against the "Command = Charisma + Cognition" base. `designs/` and `tests/sim/mass_battle/` paths are dissolved.
- **Open items:** density-primitive magnitude; confirm role table; `MIN_DISCIPLINE` hard gate vs smooth drift; stratagem degrade-opponent-discipline; intervention cadence; custom-allocation UX granularity; subunit coordination limit (:174-185).

### proposals/repo-reorganization-v1.md
- **What it is:** Content-class taxonomy and phased migration plan for the repository (13 primaries; phases P0-P5) with per-slice execution logs, 2026-07-15/17; lane IN (ED-IN-0071).
- **Status:** "RATIFIED (plan-of-record) — execution pending ... **EXECUTED.** The migration (P0-P5, §4) ran to completion across P0-P4's slices; `designs/` was retired 2026-07-19". Reading: historical (executed); the live tree differs again after ED-IN-0231 (`.designs/` quarantine, `systems/` holds no `.md`).
- **Bears on:** PROCESS, CORE.
- **Content that matters:**
  - Ruled axes: `systems/<subsystem>/` with `sim/` subfolder per subsystem; one subsystem = one folder = one ID lane = one CURRENT.md row = one HANDOFF = one Godot module tree (§2a, :52-56). Registers + handoffs -> `registers/`; params + substrate -> `engine/`; `godot/` own primary (:34-48).
  - Slices 1-9 executed (npcs/articulation/ui, threadwork, `_architecture`, world, settlements, fieldwork, social_contest, combat, mass_battle) with the retirement of the `import systems` landmine by renaming `combat_engine_v1/systems.py` -> `combat_systems.py` (:106).
  - Rulings: character `piety_track` renamed `conviction` (piousness axis) under `systems/character/conviction/`; per-territory Piety Track -> `systems/settlements/` as `piety_track` (ED-644) (:119, :158). Audits filed by category with 1-month auto-deprecation (:120-123).
  - Godot map: `systems/<sub>/sim/` -> `res://engine/modules/<sub>/` (ED-1050 1:1 oracle-port), `engine/engine_params/` -> `res://resources/*.tres` (:139-151).
- **Conflicts / stale:** `audits/` lifecycle, `character/*`, `factions` slices and ED-644 rename were still "deferred" at the last edit; CLAUDE.md now says `audit/` is retired as a category, `.audit/` hidden, `.designs/` quarantined; `module_contracts.yaml` "27 modules" count dated; "Key-emitting" language retired (ED-IN-0232).
- **Open items:** none that matter; reference for where old paths went (use `tools/pathres.py`).

### proposals/social_contest_consolidation_integration_v1.md
- **What it is:** Social-contest consolidation and integration programme v2 (CIP-0..CIP-15), based on four precedent lenses and three adversarial critics; lane SC, v1 2026-08-06, v2 2026-08-07; IDs ED-SC-0023/0024/0027/0028.
- **Status:** "PROPOSED — CIP-0..CIP-15 filed. Needs Jordan: CIP-3, CIP-7b, CIP-9b, CIP-12, CIP-15". Reading: unratified; written against the pre-season SC kernel (`systems/social_contest/sim/contest/`, now UNWIRED from the season loop per docket 07) and the retired Key/echo transport; its principles are the nearest design statement of argument-as-structure in the tree.
- **Bears on:** SC, FI, FA, CHAR, SE, GO.
- **Content that matters:**
  - Governing principle: two configurations of one engine are distinct scenes iff (i) a competent player's best action sequence differs and (ii) the player can tell which they are in; anti-collapse: no common scalar into which all effects convert (C-1, C-2: every win condition reads `s.adv`) (:15-52).
  - CIP-1 Record spine: ledger tags (Precedent, Debt, Grudge) emitted by a contest close with source/parties/uses/superseded_by; fix `ledger_add` replacing on (kind,key); holder dimension and reach carrier needed; falsifier: a contest outcome in season N changes which branch fires in season N+k (:171-230). The kernel's whole interface to the world was two integers (`scene_dispatch.py:298,306-307`) (:78-83).
  - CIP-2 evidence: the close must consume claim-graph state non-fungibly; a warrant scheme (Walton/Toulmin: premise, conclusion, critical questions) defines its own attack surface (no warrant x attack matrix); W3 evidence has no producer in the tree (`investigation.py` all stubs), no apparent-vs-true split so forgery is unrepresentable, no provenance (:232-290). This bears directly on the detective/noir charge (typed bindable evidence, contradiction/rebuttal).
  - CIP-5 the writ declared before the roll (question, stakes = the draft Record, dials, coarse read, compromise axes, the end pursued); a topic the world did not raise should not be arguable (generalise `_derive_vote`) (:335-372). CIP-13 decorum operator: relevance graded not binary; delete `Stasis.TENSE` and the dominated `hard` verb (:551-599). CIP-14 audience as a party (crowd taste, room memory "lose the case, win the room"), conditional on CIP-9b (:601-646).
  - CIP-9b: measure E[auto] against AI-vs-AI played, not expert play; auto-resolve viable only where the outcome surface is low-dimensional (XCOM 2 ships none) (:458-481). CIP-6: factions get `aims`, `redLines`, concealed `threat`, `patience`, voiced reasons (threshold predicates over persisted accumulators) (:374-405). CIP-11 N10 deliberation with named-juror persuasion falsifier (:498-514).
  - Nulls: no published mechanisation of principal repudiation (CIP-7b), concealed willingness scalar, burden-of-proof UI, mid-debate AI concession; no world producer of evidence in the tree (:765-769).
- **Conflicts / stale:** Claims about `parliamentary_bridge`/`echo_transport` (C-8) rest on the retired Key substrate. Ruled items it touches: ED-SC-0033..0039 (proceedings ownership) were later; the programme does not know them. The season now has `social_contest.roll` (margin only) with arrangements as data and `proofs`/`reception`/`forgery_quality` Ob terms (docket 07), so several CIPs (CIP-3, CIP-15) have been overtaken or reframed.
- **Open items:** forks §4: CIP-3, 7b, 9b, 12, 15; Leak destination; C3 scope; Reserve cost; the eleven-primitive reconciliation; adjudicator authority level vs gap.

### proposals/valoria_fork_plan_of_record_v1.md
- **What it is:** "Valoria Fork — Plan of Record" v3: Python-side "Stage 0" plan before the Godot port (fork assembly, centralized value layer, inversion of prose registries to JSON, eight Jordan decisions C1-C8 ruled 2026-08-04); ED-IN-0124/0125, 2026-08-03/04.
- **Status:** "PROPOSED (ED-IN-0124, 2026-08-03). Jordan-vetoable throughout. Class A ... Nothing here ratifies on merge." All eight C-items RULED 2026-08-04 (ED-IN-0125 / ED-MB-0064). Reading: largely historical; the fork was a different repo plan; Key premises retired.
- **Bears on:** GO, CORE, MB, PC, FA, PROCESS.
- **Content that matters:**
  - Rulings (2026-08-04): C1 a personal combat can be triggered by field investigation, mass battle, scene contest AND invoked directly (four entry points); C2 mass battle occurs ON A MAP, loser = whoever loses more units or has a settlement captured (band edges unruled); C3 `engine_clock` stands as season counter + accounting boundary; C4 attribute roster TEN (3/3/3 plus Spirit), reversible; C5 struck (Keys "work all directions"); C6 no new `da.territorial_transfer`; C7 struck (already ruled a defect); C8 Church Influence is a GLOBAL peninsula-wide tracker gating behaviours (e.g. the mass-seizure attempt); `territorial_piety` is per-territory and feeds CI (:433-442).
  - Thesis: a seeded campaign dispatched 29 scene slots, all `contest`, zero combat, so personal combat was unreachable from the loop; 554 typed values extracted and almost none reach anything that runs (:94-104).
  - Code-first boundary: oracle code (`config.py`, `core.py`) is SOURCE; generated exports are GENERATED; prose only where no code pair (:146-163). Provenance ratchet: `uncited` may not increase (cited 84, uncited 240, assumption 8 of 324) (:194-198). Immutability and AST tripwire against new bare constants; a guard must be able to fail (:200-226).
  - Procedure: positive control before asserting absence (:74-78, :514-520).
- **Conflicts / stale:** Everything keyed to `Key IN -> resolver -> OUT`, `keys.py`, ECHO_TRANSPORT, `key_type_registry`, `wiring_manifest.yaml` is retired (ED-IN-0232). The proposed AST tripwire/`cook.py` guard conflicts with "no tree-wide guard" (§0.05). Docket counts of modules/keys are dated.
- **Open items:** the mass-battle `degree_map` four-band edges (C2 residual); `build_fork.py` carry list stale.

### proposals/verb_list.md
- **What it is:** Roster of 92 verbs (coded and proposed) by subsystem lane with effect on the game world, coded/proposed status and justification; sourced from `proposals/2026-10-16-verbs/` (undated file; ~2026-10-16).
- **Status:** none (no Status line). Header: "Coded = a row exists in engine/season/verb_table.yaml today. ... Proposed (planned) = a workplan position with no row yet; Proposed (new) = the v2 synthesis adds it." Reading: live reference roster; input to the attribute map; each row's coded/proposed state must be re-checked against `verb_table.yaml` (63 rows at docket time).
- **Bears on:** CORE, PC, MB, SC, FI, WR, FA, SE, CHAR.
- **Content that matters:**
  - Personal combat: `fight` is the only way a person harms another; `assassinate` (aim death, held cover) and `capture` (aim alive; custody) proposed as same contest with different aims; `challenge` should mint a challenge Record; `accept` requires a held challenge and fights under its terms; `guard` and `rescue` proposed (:9-32).
  - Mass battle: `levy`, `muster`, `drill`, `disband` as settlement acts moving troops by grade; `marshal` writes the `order_of_battle` Record "the field reads whenever the force fights, attacking or defending" (gives the defender a chooser); `march` carries posture and stocks; `supply`, `forage`, `surrender` (:35-69). None of these exist as rows; the coded army verbs are `recruit/form_unit/assign_troops/order_unit/disband_unit/discharge_troops` (docket 08/09).
  - Social contest: `tell` (coded), `persuade` (moves pursuits; renamed from `argue`), `utter`, `commit`, `petition`, `lodge` (renamed from `carry`), `convene`, `open_case`, `speak`, `determine`, `interrogate`; lie parked (:73-131).
  - Fieldwork: `examine`, `research`, `watch` (renamed from `surveil`), `interview`, `reconstruct` ("observations become an accusation; the honest mistake, the Foscarini case"), `survey`, `conceal`, `infiltrate`, `forge`, `bribe` (:133-202); threadwork `thread_read, weave, lock, dissolve, mend, ward, knot` (:204-247).
  - Gaps flagged: `travel/explore` need route model and authored POIs; `ration` needs a draw-policy ruling; `pardon` name a defect (R-17); `tie` kept only if a reader gates on it (:292, :302, :479).
- **Conflicts / stale:** Naming rulings (R-05 `order` vs shipped `dispatch`, R-06 `utter`, R-17 `pardon`) were open; "coded" claims drift since 2026-10-16 (verb_table.yaml now 63 rows with `argue`).
- **Open items:** many "Proposed (new)" verbs have no row; hostile-working `ward` waits on the first hostile operation executing.


## Cross-subsystem leads

- **Status census of this lane (RATIFIED / PROPOSED / held back).** RATIFIED: `2026-11-04-strife-flows/01_STRIFE_KINDS_DRAFT.md` (ED-IN-0316, five calls resolved for emergent narrative); `2026-11-08-flow-conditioning/` (ratified as the accepted first reading, "ratify all and merge", ED-1094; content drafts for CR-106/CR-107, nothing at runtime; engine files do not yet carry it); `repo-reorganization-v1.md` (executed, historical). BUILT-gated-off: `mass_battle_fighting_withdrawal_v1.md` (yield, three MB_YIELD flags off, default flips HELD for Jordan). PARTIALLY SUPERSEDED: `pc_formation_system.md`. WITHDRAWN/held: `2026-11-05-cr85-histories-hooks-and-combat-input.md` (ratified ED-IN-0349 then withdrawn ED-IN-0351). PROPOSED (nothing ratified on merge): the docket chapters 07-11, `cr11-computed-establish-design`, `knowledge-model-build-plan`, `attribute-rulings-adjudication`, `verb-attribute-map` (+part2), `unified-design-and-build-plan` (ratified on merge by ED-1094 except Part 6 questions), `social_contest_consolidation_integration_v1` (needs Jordan: CIP-3, 7b, 9b, 12, 15), `grounded_event_card_deck_v1`, `canonical_nomenclature_v1`, `multiunit_envelopment_plan` (un-adopted, HELD), `valoria_fork_plan_of_record_v1`. FILED reference: `design-and-code-critique-report`, `verb_list.md`, `attribute-rulings-by-subject` (Jordan's words, ED-IN-0347).
- **PC x CHAR x CORE: attributes reach no season fight.** The season builds every `Combatant` at class defaults except `end` (`seam/wrappers/combat.py:36-41`); PC-06 K-1 (the seam builds the fighter from `Person.attributes`) is what makes every combat attribute ruling live (attribute-rulings-adjudication :59, :93). CR-85 (history -> `faculty`) is WITHDRAWN, so the combat input design is unsettled: PC and CHAR must settle whether a contest pool takes attribute and trained skill as separate inputs (CR-85 header).
- **PC x MB: mixed weapons and carry cost.** Nothing in this lane carries a secondary-weapon or carry-cost datum: docket 08 shows equipment (`ARSENAL`, `ARMOURY`, 14-row loadout) is `provisional=True` "NOT YET WIRED into resolution" except `unit_type_for`; per-unit `dr`/`stamina` deliberately unbridged; no kit carrier (M25, CP-T03-03). `pc_formation_system.md` supplies the role/instruction/brace/kiting logic that a loadout switch (pike to arming sword) would hang on; `mass_battle_fighting_withdrawal_v1.md` supplies the state-change precedent (a `yielding` flag plus an order) and its default-off calibration debt.
- **MB: hierarchy and one path.** `multiunit_envelopment_plan.md` (un-adopted) says `run_multi_unit_battle` is a 1-D lane abstraction of isolated 1v1 `run_battle`s; the per-cell envelopment shock is unit-agnostic and would emerge if contacts were detected across all units (Path B). Docket 08: season ships no authored order of battle; `Subformation` 7 fields, army record up to 11 subformations; 7 of 15 role-instruction keywords unwired; the commander feed (`Officer.command`) has no Person link. The auto-resolve vs play question touches the code-shape forbidden row "a second resolver, an auto-resolve formula, a fast path" (provenance CODESHAPE_FORBIDDEN :14).
- **SC x FI: the detective/noir bearing.** `social_contest_consolidation_integration_v1.md` (CIP-1, CIP-2, CIP-5, CIP-11, CIP-13) is the one design in this lane that treats evidence as a typed, bindable object (claim graph, schemes with critical questions, the writ declared before the roll, named-juror persuasion); docket 07 shows the live roll takes evidence only as `proofs`/`reception`/`forgery_quality` numbers in the Ob, speech kinds are UNREAD by game code, and `interview`/`reconstruct`/`thread_read` are ungraded. `verb_list.md` lists `reconstruct` ("observations become an accusation; the honest mistake, the Foscarini case"). The kernel in `systems/social_contest/sim/contest/` is NOT wired. Conflicts with ruled items (ED-SC-0033..0039, knowledge-model ruling) are unexamined by the CIP document (it predates them).
- **CHAR x SC x FA x CORE: the chooser.** Docket 10: one shipped policy (score = pursuit + stance, Plackett-Luce, tau 0.1, one tau for all persons); 22 of 63 verbs have no `alignment` cell so pursuit is 0 for them; the player seat is a dispatch hook with no option list (a player proxy and an NPC do NOT share a menu surface). The attribute adjudication adds CR-93 (attributes in the chooser, per-person tau falling with Focus, Reason shrinking forecast error). The unified plan adds believed-clock thresholds (CI, Turmoil), duty decline (CR-88), violence contexts (CR-87).
- **FA x WR x SE: the arc and the clocks.** `unified-design-and-build-plan` Part 3: Valorsmark a faction, vassals sworn, `head_seat` per faction, the Church's settlement; two clocks as folds of `w.log` (no matrix row), bands changing what persons want, never firing acts; casus belli as a claim Proposition on a ground; civil war a reading; CR-90 arc instrument. `design-and-code-critique-report` rulings (one parliament; transnational Church with Holy See at Himmelenger T9; 15 territories; Schoenland neutral trade nation; Queen is widow regent) bear on FA/SE content that is not yet built.
- **SE x CHAR x WR: flow-conditioning content.** `content_cohorts.yaml` (51 rows over 37 settlements; heritage by radiation band; no `faction:` because a cohort `commit` makes the faction occupy the settlement) and `content_church_sites.yaml` (41 Church Sites) are ready drafts; neither is in `engine/season/` yet. Consequence recorded: every two-cohort village/fortress reaches summed weight = capacity so `migrate` into it is refused from tick 0.
- **GO: port rules.** The F3 adjudication binds the port's shape (empty autoload table, `core/` headless, fixed-point integer `condition`, owned SplitMix64, binary snapshot saves, ids not pointers) and is intent, not code; engine version is ruled by ED-GO-0002 (so its §1 is historical). `valoria_fork_plan_of_record_v1.md` C1: a personal combat can be triggered by field investigation, mass battle, scene contest and direct invocation.
- **PROCESS:** the entire `_session_provenance/` subtree (2026-08-29 to 2026-09-01) is Key-substrate-era working material (Key retired, ED-IN-0232). It is useful for the vocabulary (Tenure, Rung, Claim, Query, partition) and for the F-1..F-18 failure-mode checklist, not for current mechanism claims.

## Likely stale or superseded

- All of `proposals/_session_provenance/**` read here: dated 2026-08-29..09-01 snapshots of a design line that executed nothing then; M1 0/7, `world.npcs` empty, `stub_hits` 2, "nothing executes" are no longer true of `engine/season/`. Claims that rest on the Key substrate (`keys.py`, `KeyLog`, ECHO_TRANSPORT, 55 key types, `module_contracts.yaml` resolver labels, `wiring_manifest.yaml`) are retired by ED-IN-0232.
- `valoria_fork_plan_of_record_v1.md` (Key IN -> resolver -> OUT frozen; `cook.py`, AST tripwire; `build_fork.py` carry list) and `repo-reorganization-v1.md` (executed; `designs/`, `sim/`, `tests/sim/` dissolved; the tree later changed again by `.designs/` quarantine).
- `canonical_nomenclature_v1.md`: its measurement targets `fac.intel`/`substrate.key`/Key types; proposes `ci_nomenclature_check.py` (a tree-wide guard barred by §0.05 and §0.1 pt 5).
- `grounded_event_card_deck_v1.md`: stored-aggregate vocabulary (Mandate, L/PS, Treasury, Weight), five new settlement levers, `stakes.source_key` hook; the body of the file jumps from the compliance appendix into mid-card (only ~10 cards present in this file).
- `social_contest_consolidation_integration_v1.md`: premised on the unwired kernel, the echo bridge (`parliamentary_bridge`), and the Key transport; many CIPs (CIP-3, CIP-15, CIP-1 mount points) are overtaken by the arrangements/proceedings rows (ED-SC-0033..0039).
- `2026-11-04-content-parameters-docket/07-11`: line cites and counts as of 2026-11-04 (63 verbs, 86 fixtures, 14 troop types); CR-87 has since landed per the critique report, so docket 10's chooser picture is partly stale.
- `verb_attribute_map` finding 8 and F23 line cites, and F8 "moves nearly every golden", are corrected in `attribute-rulings-adjudication` §1.1.
- `2026-11-08-design-and-code-critique-report.md` correction 1: "104 fight formations" STALE after CR-87.
- `mass_battle_fighting_withdrawal_v1.md`: carries both PROPOSAL (:5) and BUILT (:3) status lines; paths to `designs/...` dissolved.

## Items that could change an audit finding

- **Mass battle, the ruled trade-off (Jordan's carry cost).** No loadout/carry datum exists in the code per docket 08; if the MB audit finds "mixed weapons per unit with fatigue and speed cost" absent, that is consistent with docket 08 (equipment PLACEHOLDER, NOT WIRED, `dr`/`stamina` unbridged). `pc_formation_system.md` already designs role = shape + instruction package gated by troop type and an intervention-window cadence; the 15-role `ROLE_SPEC` matches it (docket 08).
- **Mass battle, one path.** `multiunit_envelopment_plan.md` documents that multi-unit resolution is lane-pairwise (1v1 `run_battle` per lane) not the cell-based union; an audit claiming a single cell-resolver for army battles should check `run_multi_unit_battle` (orchestration.py ~L2636-2899 per the plan) and the Phase-1 change-set (:83-89).
- **Mass battle, yield.** `MB_YIELD_*` flags exist and are OFF: any audit statement that "fighting withdrawal is absent" must be qualified as "built, default off, calibration debt D_YIELD/YIELD_POOL_MULT/YIELD_RALLY_MORALE_FRAC/YIELD_POCKET_REACH".
- **Personal combat, the two modes.** Nothing in this lane specifies the "approach per phase" surface; but attribute-rulings-adjudication records that `reading` is attribute-fed only by `att` mixed with `cog`, and that the season hands combat only `end` (so no attribute lever reaches a season fight until K-1). CR-85's withdrawn design determines whether a contest pool reads `faculty`; PC audit findings about "levers" should cite this.
- **Social contest, evidence.** F-SC-style findings that "evidence is a number not an object" are supported by docket 07 (Ob terms `proofs`, `reception`, `forgery_quality`; speech kinds unread; kernel unwired); the CIP-2 claim-graph design is the only in-tree design for the alternative; `verb_list.md` carries `reconstruct` and `research` ("tells a forgery from a true one").
- **NPC chooser findings.** Docket 10 supports: one policy for all persons; 22 uncelled verbs; no per-person tau; a player has no option list; `refusal_axis` ships None; `withheld_verbs` hides destroy_record and army verbs from computed play. The adjudication's AR-04 ("attributes/capabilities weight the best course of action") is Jordan's ruling that no code realises for uncontested candidates.
- **Fieldwork findings.** Docket 07: `interview`/`reconstruct`/`thread_read` ungraded; `survey` mints `faction_sheet`; trail from place/alias writes owed (CP-T06-01..09); `why` observation term never supplied.
- **Settlements.** Docket 08/11: `planned_works` 2; subsistence, wear rates "invented values"; POI catalog unread; `site_kinds` 9 (church kinds absent until CR-106 lands).
- **Factions/governance.** Unified plan C9: King, Duchess, Duke not sworn; faction roster lacks Valorsmark; `faction_q.head` returns None; only 12 of 31 offices name a faction; plus the critique report's rulings (one parliament; Holy See at T9).
- **Process finding ids.** No `audits/*.md` finding ids were cross-checked in this lane (no ids known); the claims above are described rather than id-keyed.
