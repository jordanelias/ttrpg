# Errata and audit record

Parts 1 and 2 and the audit records below were written at `a4ca9a5` and cite line numbers there; they are kept as recorded. Part 3 (round 3)
was written against `51d7b05` and the precedent suite (`research/game_precedent_suite/`), and where it restates or overturns an earlier
line it says so. The control run (`ctl/`) is byte-identical on `51d7b05`.

## Part 1 — Round-1 errata (applied to the tutorials)

# ERRATA — corrections to the first draft, from six independent audits (A accuracy-core, B accuracy-combat/SC/TW, C accuracy-gov/econ/info,
# D verbs-directory comprehensiveness, E remediation+code-tree comprehensiveness, F logic/consistency). Authoritative over the draft appendices.
# Each line: CORRECT FACT — evidence. Ids in [] are audit findings. The tree decides what is built; proposals decide intent only.

## G. Global rules
G1 GRADE RULE (use this everywhere). RUNS-IN-LOOP = the behaviour produced a non-refusal outcome inside SeasonDriver.season over build_realm under
   the populated.run recipe (barrier passes MATTER/CENSUS/WITNESS always qualify). "RUNS-IN-LOOP at control" = runs but is inert at shipped
   fixture values (body_step 0, age_step 0, illness_rate 0, telling_privacy 0, confliction_weight 0, scar_weight_shift 0). TESTS-ONLY = wired or
   implemented, executes only under unit tests / fixture worlds / oracles / zero successful executions in the realm run (cite a test). DESIGN-ONLY =
   no executing code. A refusal gate firing is not the verb executing. [F1,F-grade-rule,C-F1,C-F2,C-F5]
G2 COUNTS. Use $SP/ctl/realm_seed{0,1,2}_2seasons.txt (one script; acts attributed by Event.causes[0]; "ok" = at least one non-refusal event; runs are
   deterministic across processes: PYTHONHASHSEED varied, outputs identical). Where an appendix table differs (A2 §C.3 counted differently; e.g. fight, accept,
   commit, work 78 vs 77, sabotage 35 vs 34, survey 58 vs 57, research 125, examine 62 attempted) the ctl files win. Outcomes vary by seed: seed 1 executes
   oblige 22 of 24 and confer 1 of 5; seed 0 never attempts either. Statements of the form "never attempted / 0 live oblige" are seed-0 only. [F-count,A-08,A-09,A-10]
G3 VERB TABLE. 53 rows; 47 admitted by resolvable_verbs(); the chooser menu is resolvable_verbs() minus withheld destroy_record = 46 (populated.py:1531). 7 contested
   rows (argue, determine, speak, tell, fight, accept, march). Typed preconditions: 37 rows typed, 6 `requires_typed: none`, 10 with no key; 7 hand predicates in
   REQUIRES_PREDICATES (loop/predicates.py). [F5, A-13]
G4 WRITE MATRIX has 40 rows + 6 retired (write_matrix.yaml:86-418, :440). [A-01,E-04]
G5 LADDER. Only the social path (and graded inquiries) reads the margin ladder degree_from_net. Combat reads Felled/Wounded/Untouched off the subject's wound tracker
   (seam/ladder.py combat_degree); field reads attacker_wins -> Won/Lost/Unopposed. Mass battle has its own roller and ladder copy. [F3]
G6 "NO FACTION CLASS". No stored Faction/Settlement/Province entity; faction_q.Faction (faction_q.py:84-95) is a frozen per-barrier VIEW dataclass. 17 territory rungs;
   provinces are a Query. [A-02, F33]
G7 SCAR is written at RESOLVE/ENCOUNTER by the fold (loop/resolve.py::_scar_witnesses; carriers.py:692-693; write_matrix steps RES,ENC), never at WITNESS. Conviction crisis folds a conviction at scar>=3. [A-03]
G8 MATTER also runs claim-confidence decay (claim_decay_per_season=5; matter.py:317-347) and standing crossings; decay is a MATTER write, not WITNESS. "MATTER owns every exogenous motion" is
   true for term lapse, draw, yield, wear, leg end, hunger, ageing, decay; Rung.stores is also written at RESOLVE by transfer/requisition. [A-14, C-F6]
G9 SHIPPED CONTROLS: MATTER kills nobody at shipped values (body_step 0 -> continue at matter.py:513-520; ageing/illness skipped :549). Every realm death is combat. [E-15, B-F13, F14]
G10 REFUSAL KINDS act.ineligible/act.refused/attempt.refused are DECLARED in rosters.yaml:1168-1188 (fold_kinds) and checked (data/rosters.py check_fold_kinds; loop/resolve.py:1157-1163). Invariant 7 is built at
   the fold; the half where the log itself refuses is open (hole_register.yaml:4684). [A-04]
G11 SCENE BUDGET. budget = max(1, 5 + 1 per live `hold` Tenure - body bands - 1 per travel leg) (budget.py:57-61); EVERY live hold counts (seat, landholding, held Record via create_record). Whether the excess over 5 can
   be spent is disputed in-tree: deliberate.py:89-97 says release is capped at 5 (rounds x scenes_per_round) so a sixth is unspendable; fixtures.py:497-502 makes the remainder a COST budget and an extended
   scene (cost 2) affordable. Read both lines before stating either. "5 per person-season" are SCENES of <=3 acts; observed ~8-10 acts per person per season. [A-06,A-07,F8,F9]
G12 CHOOSER. Score = verb alignment with value axes + stance toward subject (+ inert urgency), then Gumbel/Plackett-Luce order at tau 0.1. "72% overridden" is a harness-slice reading with no season (decision_spread.py:23-28):
   28% of strict-top cases (16% of all; 222 more are ties, REM-12 unbuilt). R-08: the sampler IS built (requirements.yaml:1274-1285); the row stays partial because inclination cannot break ties. make_chooser is never
   constructed in loop/; callers are harness/, engine/reference degree-sweep arms, proposals/ probes. SeasonDriver is also built by proposals/ probes and 4 tests/valoria files. [E-01,E-02,A-11,A-12]
G13 UNCELLED VERBS: tell, thread_read, restore are uncelled BY DESIGN ("testimony's moral weight is in WHAT is told"); carry, examine, interview are the real gaps (B5 targets) (verbs-05:110-112; verbs-07:26). [F16]
G14 LOC: modules/combat 5,643 (+ systems/combat 2,812); modules/mass_battle 10,154 (+ systems/mass_battle 3,089); SC kernel 6,693; modules/social_contest 127; modules/fieldwork 36; threadwork 1,955;
   chooser 2,546; loop+state 13,141. Weapons: 54 keys (50 base + 4 half-sword forms; header says 53); traditions 7 + none. [F29, F30, B-F1]
G15 GODOT: godot/ holds design docs and godot/skeleton/ (GDScript strike/wound modules, .tres); it does not compile; no runnable port exists in this repo. [E-13]
G16 PLAYER POSITION: no player interface in code. D-2 (RULED yes, Jordan 2026-10-21): RB-3 builds IN-46 (grid-mode suspension; played fight) and IN-47 (character-sheet space). Repo's comparative frame calls the player "embedded: one person's decision procedure"
   (research/by_lane/00_COMPARATIVE_ANALYSIS.md:312). [E-07]
G17 DESIGNED-BUT-DELETED LAYERS (module_contracts.yaml): `victory` (MS=0 -> Post-Calamity; all factions dissolved -> Anarchy; code deleted at 28-iii, :675-719); peninsular_strain / MS track
   (systems/overview/sim/ms_track.py, floor 0 ceiling 100, -1/yr, start 60, no live caller); faction_state Mandate/Treasury/stats 1-7 (action code deleted at 29b, :77-107); accounting_sequence (:921-948);
   piety_track = systems/characters/sim/conviction.py (:178-182). Repo module roster is 26 rows, most `sim_module: none`. The game has no ending condition in the running loop. [E-05,E-06]
G18 REMEDIATION VERDICT: even fully executed, the 40-item plan (RB-0 PLAN paper, RB-1 INSTRUMENTS hash-equal, RB-2a/b FORMATION AND SCARCITY, RB-3 SCALE BUILDS, RB-4 LAYER-1 + NERS, RB-5 HUNGER) cannot make THE NINE met:
   R-01..03 stay met (may fall); R-04, R-05, R-07 move up with no guarantee; R-06, R-08, R-09 made honest not met (-01:29-31). R-04 conjunct (1) has no item. Rulings D-1 (agent lands unmarked Layer 0/1 text), D-2, L1-6 (subsistence leaves Sensation).
   JQ-1..JQ-6 are the open forks (JQ-2 options are "materially different games"; JQ-3 four character-change magnitudes H-187,H-188,H-200,H-208; JQ-5 optional release of the two RB-3 designs; JQ-6 hunger ratio). Hunger: even after RB-5 it binds only
   before the first yield (cover 21.7 -> 41.7 seasons). [E-08..E-11]
G19 VERBS PROPOSAL OVERRIDE RULE: every lexicon opens with "Rulings that override this section"; verbs-03 §III.5 (R-01..R-29) governs where a lexicon body disagrees. So: levy is MB's (R-01), knot TW's (R-02), raze/tax GV's (R-03/R-04), forage MB's (R-08),
   succeed GV's (R-11), FA roster = 7 hosts: covenant, declare, recruit, conspire, assign, seize, sabotage (verbs-03:148-158); GV = 20 rows (12 shipped+3 planned+5 new; 5 parked names are not rows); dispatch->assign/order rename is held as D-V7;
   `watch`/`travel`/`pledge`/`lodge`/`dissolve` are PROPOSED renames (V0 batch, R-10). These are NOT unresolved conflicts. The roster has 92 verbs; §III.4 has 52 host entries. Reliability: v2 itself, the divergence test and the reconciliation have NO critic;
   the from-scratch attribute work failed its critic (CONTAMINATED); [MEMORY] precedents are unchecked. [D-F1..F17]
G20 ATTRIBUTES (verbs-02): nine ruled names Strength, Endurance, Agility, Focus, Acuity, Will, Attunement, Charisma, Bonds (descriptor_registry.yaml:36-48) + a tenth (Thread Sensitivity, own 0-100 scale); evidence ranks 7 strong, Bonds medium, Attunement "a rescaled Acuity",
   Charisma "near-inert at T2", Recall none; alternative E8 (8 attributes); build track B1-B7 (five builds need no ruling: template B1-B3, TS carrier B4, alignment cells B5). [D-F9,F11]

## C. Per-subsystem corrections
C1 PC: wound impairment is a SIGMA term (combat_systems.py:1038-1044, summed into net_sigma), not an Ob term; Ob is history/2 only (core.py:108-115). The seam varies only `end`; the actor is never written; the scene fells the actor in about half of mirror
   fights; a cohort subject is deleted whole by one Felled; `stance` is written at runtime only by march and forgive (effects_combat.py:426), not fight/accept. systems/combat/combat_engine_v1/state_graph.py (duel state machine as data) and capabilities.py
   (weapon-affordance gates) exist. Control-run counts (seed 0): fight 7/4, accept 18/11, challenge 23/6. [B-F2, A2-F13, E-17]
C2 MB: the season seam also varies morale start and a terrain row; tactic_cards.py is an EMPTY dict stub (systems/mass_battle/sim/tactic_cards.py:33), altonian_reinforcements.py raises NotImplementedError (:21); neither is under modules/. march: control 21 attempted-declared, 25 march.refused events, 0 field events. [B-F3, F7]
C3 SC: arrangements.yaml has THIRTEEN keys plus id (lines 8-14); `quorum` is required only for disposal: declared and no row uses it; two rows dispose `Record`, which open_case refuses (effects_information.py:333-336); H-221 text is at verb_table.yaml:155 (not :146); the
   `a matter` row/heard_by is rosters.yaml:1321-1325; obstacle composition roll.py:103-113; the "1 of 430" line is a paraphrase (rosters.yaml:1223-1224). argue/determine unreached is evidenced by argument.won = argument.lost = 0, not by the refusal count. [B-F4..F10]
C4 TW: opposing.py "6 rows" is an inline comment (opposing.py:172). [B-F12]
C5 GV: work's typed precondition is condition >= floor with NO presence clause (verb_table.yaml:1511-1517); a rise is staged only where a live works Record names the site (effects_economy.py:103-104; H-165), hence 77/77 work.unavailable. In-tree notes say `restore` executes on the realm
   (requirements.yaml:165-166; rosters.yaml:1461-1463) but the control run shows 0/23: an unresolved conflict. Authored obligees are TWO term-less oblige edges built at world-gen (populated.py:1317-1339: off_king->NPC-070, off_restoration_leader->NPC-041); term-less edges never lapse at MATTER, so any 0 live oblige means release or death closed them;
   seed 1 shows 24 live. The 32nd office is the unauthored seat off_npc_084 (populated.py:1240-1244). Every binding_decision-stratum emission (dispatch, issue, confer, release...) is broadcast to everyone by the chronicle channel (epistemic.py:649-686); governance acts are public realm-wide. The seat roster is `open: true` (rosters.yaml:316). sovereign_fraction's denominator is held rungs
   only (world_q.py:1555-1560). [C-F3,F4,F7,F15,F16,F17,F35]
C6 FA: see G19. holder_faction_of callers: survey (effects_information.py:653-726), seize (:958), _eff_march (effects_combat.py:270), sides.py:131. covenant row/effect exist at HEAD (verb_table.yaml:254, effects_information.py:240); the lexicon claim is STALE at its base (716c253), not refuted. [C-F14, D-F17]
C7 EC/WT/NP: `coin` is registered (rosters.yaml:1420) and used only by a harness probe (probes.py:1611-1616); no shipped world uses it. `succeed` row only declares heir.designated, never emitted. `forage` is MB's. `tend`, `train`, `give`, `commit`, `work`, `restore`, `sabotage`, `found`, `build`, `requisition`, `migrate` are TESTS-ONLY by G1 in the realm run;
   `forgive`, `release`, `move`, `transfer` (1/45) execute. [A6-F1,F2,C-F12]
C8 FI/info: `watch` is a PROPOSED rename; `dissents` fires when an incoming claim contradicts the holder's own claim about HIMSELF or a cell (options.py:1394-1399) plus an act-level prior; `finding.none` is undeposited so inquiry failure/refusal leave no belief (chooser failures otherwise do). 250 `finding.none` break-down (218 refusals + 32 Failures) is NOT reproduced by A8's own arithmetic: treat as unverified. witness_key and post_remit admitted nobody in the run (TESTS-ONLY by G1). [F10, C-F5, C-F10, C-F13]
C9 Loops: say "reaches X; return leg unmeasured" for conviction loop, yield loop, wound->end loop. Information model: "strong" means complete and running; it does not deceive (no lie verb, covers do not hide `who` from those present, forgery inert at the ceiling); mean ledger 199.0/200 at 4 seasons. [F18,F19,F37]


## Part 2 — Cross-cutting rulings from round 2 (applied to the tutorials)

# CROSS-CUTTING RULINGS for all tutorials (from round-2 audit L, J, G, H, K, I). Apply wherever your tutorial touches them.
C1 SCENE BUDGET (ERRATA G11 is RESOLVED; use this). budget() returns SCENE ACTIONS (budget.py:19-20): max(1, 5 + 1 per live `hold` (seat, landholding, held Record or Proposition) - body bands - 1 per travel leg).
   pack_scenes treats it as a COST budget; a scene holding more than one act is EXTENDED and costs extended_scene_cost = 2 (fixtures.py:489); a chunk is trimmed to one act when only 1 is left (choose.py:643-657).
   The driver releases at most 1 scene per round over 5 rounds (rounds 0..4; driver.py:456) and charges cost(ext) (deliberate.py:252-259). So budget 5 -> 2+2+1 = 7 acts; budget 6 -> 2+2+2 = 9; a leg costs a budget-6 holder one scene action, which cuts 9 acts to 7 (budget 5 -> 2+2+1).
   Hold-minters: create_record, issue, open_case, petition, survey, forge, utter (and conceal via a cover Record); `utter` always succeeds so it is a budget lever. Cap = 5 scenes x cost 2 = 10 actions. There is NO 'free journey' for an office-holder.
   Acts per person-season: ~6.3-8.0 depending on basis (d.resolved 1,132 / ~74 persons / 2 seasons ~ 7.6; w.acts 1,407): always name your basis. Never say "up to 5 scene actions" or "each act costs one scene".
C2 SEED RULE. State per-seed execution ("executes at seed 1, not seed 0"). ctl "attempted" = acts that reached the fold (`d.resolved`, appended on entry to `_fold`, resolve.py:377-379), so ordinary admission refusals ARE counted (seed 0: `interview`, ungraded, reached the fold 32 times, 21 with no non-refusal event); left out are acts whose actor was already gone (:974-977), refusals for an obstacle too high for the pool (:981-998) and contested or graded acts refused by `_admits` before the seam (:1012-1032); "ok" = at least one non-refusal Event (ctl/control.py:13, :21), not Partial-or-better (speak's Failure, `matter.turned`, counts; for fight and accept "ok" means Felled or Wounded on the subject).
   Verbs formed but refused at admission (examine: 62 formed seed 0, 0 admitted) are "never pass admission", not "never formed/attempted". Print run columns as attempted/ok.
C3 TICKS not "season 0/1": MATTER at tick 0 is the first MATTER.
C4 REMIT roster: rosters.yaml:316 `open: true`, but :315 and verb_table.yaml:257,801,1478 say "CLOSED": the tree contradicts itself; say so. remit_default ("NOT CANON, a testing fixture") IS applied in the shipped realm build and is where dispatch, hence march, comes from.
C5 BROADCAST: the chronicle channel is a KIND filter (epistemic.py:652-654, :685-686): any Event whose kind some binding_decision row emits is broadcast to everyone, including pursuit.moved (from determine) and MATTER's tenure.closed. Not "every binding_decision act".
C6 UNCELLED VERBS: tell and thread_read are uncelled by design; restore is NOT (its note: "THE PREMISE IS STALE ... cells are owed", rosters.yaml:2979-2985); carry, examine, interview are gaps. (Overturns ERRATA G13 for restore.)
C7 COHORT COMMIT: no code gate stops cohorts committing; NP-G36 is a [PROPOSED] gap row; observed: none did.
C8 NULL-CONFERRAL seats (six authored rows: King, Duke of Valorsmark, Duchess of Hafenmark, Widow Regent, Heir, Princess; seven built seats with the unauthored `off_npc_084`, Part 3 R-F1) can never be refilled once vacant; succeed has no effect.
C9 HUNGER cover caveat: D02's "cover 21.7 -> 41.7 seasons" counts ore and timber as food; grain alone is ~10 seasons; yield reaches 0 only at tick 100 without repair.
C10 requires: teach the typed cell (requires_typed), not the prose `requires:` string, and say which half is untyped (speak: venue half; determine: the date).
C11 PRIMITIVES and PROCESS IDS: the master file will carry a shared glossary (Rung, Tenure, Record, Proposition/mood, Office/purview, stratum, prize, "with", establishment, Observation, Calamity/Locked Zone/Exposure, H-/REM-/JQ-/D-V/R-/M-/J-T ids). Still define each primitive in one clause on first use in your tutorial.
C12 GRADES: ERRATA G1 only. Never the draft's 'the loop reaches it'. Regrade accordingly; apply per seed.
C13 PROPOSED material: tag [PROPOSED]; never state a gap-register id as a built rule.


## Round-1 audit D (verbs directory, comprehensiveness)

# Audit D (comprehensiveness/fairness, verbs directory) — findings as returned
F1 S2 Overview §8: "unresolved conflicts" (levy, dispatch->order, knot, succeed, R-01/03/08) are settled in verbs-03 §III.5 (R-01 levy=MB :231, R-02 knot=TW :232, R-05 rename held as D-V7 :235, R-11 succeed=GV :241); each lexicon header "Rulings that override this section" (verbs-10:8-14, -14:8-18, -15:8-15, -18:8-12). Bodies that disagree are superseded on purpose. Fix: drop from "unresolved"; keep only D-V7 as Jordan-held.
F2 S2 A5/A6/A7: same defect repeated: no lexicon-appendix synthesiser read the governing roster verbs-03.
F3 S2 A5 FA table: governing FA roster has 7 hosts: covenant, declare, recruit, conspire, assign, seize, sabotage (verbs-03:148-158). levy is MB's, succeed is GV's, posting act is `assign` (R-05).
F4 S2 A5 FA §6: D-V6 = contents-aware value term vs mood-keyed alignment cell (verbs-04:151); `declare` own row = R-06 ruled; D-V2 now = do births exist; kin-tie answered "marry stands" (verbs-04:147).
F5 S2 A6 EC: `tax` is GV's own row (R-04 overrides EC fold); `raze` is GV's (R-03).
F6 S2 A5: GV "20 rows" resolves: 12 shipped + 3 planned + 5 new = 20; 5 parked names are not rows (verbs-14:27-31; verbs-03:123-146).
F7 S2 A8: `watch` is a PROPOSED rename (V0 rename batch, verbs-03:240 R-10), not staleness of L12.
F8 S3 A2: §III.4 has 52 host entries (51 distinct), not ~46; R-10 also adopts sever->dissolve.
F9 S4 attributes: nine names (Strength, Endurance, Agility, Focus, Acuity, Will, Attunement, Charisma, Bonds; descriptor_registry.yaml:36-48), evidence ranking (verbs-02:105-160), E8 alternative (verbs-02:285-286), TS keeps its own 0-100 scale (verbs-02:196-208) missing.
F10 S4 reliability ledger absent: divergence test, v2 itself, reconciliation have no critic; from-scratch work failed its critic (CONTAMINATED); [MEMORY] precedents unchecked (verbs-07:82-100; verbs-04:172-178).
F11 S4 B-track (B1-B7: person/attribute builds; five builds need no ruling) absent (verbs-07:12-14, :50-56); thesis 2 absent.
F12 S4 standards S-6, S-7, S-8 and Part VI section anatomy; critics L-01..19/V-01..21 absent.
F13 S4 Part V retained engine findings absent (record_sourced_operands; closers as presets of release; deed: cell pricing; bribe != oblige; conceal hub; chronicle deletion D-V3; execution before additions) (verbs-08:18-34).
F14 S4 gap headline lacks 189 (39%) undisposed rows and kind split (missing verb 125, reader 118, carrier 66, shortfall 61, collision 36, name defect 24) (verbs-04:101,117).
F15 S3 A6: `forage` is MB's (R-08), WT supplies yield only (M-WT-8).
F16 S5 Overview §6.1: uncelled-by-design verbs: tell, thread_read, restore; only carry/examine/interview are gaps (verbs-05:110-112; verbs-07:26).
F17 S5 A5: "L15's no-covenant claim refuted" -> stale at its base 716c253, not refuted.
Verified correct (selection): 53 rows, fight :612, seize :1042; 92 = 7+9+11+12+7+20+7+8+3+8; 48/11/33; 488/312/58/97/13/8; 127 mechanics, 14 shared; V0..V6; 16 node types 3/5/8; template 21 fields 8/1/3/2/7; J-T1/2/4; registry scale 1-7.
Not reached by D: verbs-09,-13,-17 bodies; verbs-20..23 rows.


## Round-1 audit E (remediation directory and code tree)

# Audit E (comprehensiveness: remediation dir + code tree) — findings as returned
E-01 S1 R-08 basis: requirements.yaml:1274-1285 itself says "THE LAST SENTENCE IS FALSE AS OF U4 ... sampled, softmax via Gumbel"; row stays partial because inclination cannot break ties (:1282-1285, :1309-1311), not because sampler is missing. Suite said the stored text is stale/deterministic: wrong reading.
E-02 S2 "72% overrides strict top": decision_spread --decisions is BUILT REALM, NO SEASON, one synthetic shared question (decision_spread.py:23-28); 198/276 are strict-top cases only; 222 are ties, of 498 (-04:258 M-3); say "28% of strict-top cases (16% of all)", harness-slice reading.
E-03 S2 "population<->hunger<->body open by design": Jordan required hunger 2026-10-21 (-01:18-19, -03:195-196); open only at shipped control (fixtures.py:594) pending RB-5/JQ-6.
E-04 S2 write matrix is 40 rows, not 41 (write_matrix.yaml:86..418; retired at :440). A2 has 40.
E-05 S4(highest) designed world-clock/ending layer with deleted code absent: victory gates MS=0 -> Post-Calamity, all factions dissolved -> Anarchy ("code deleted at 28-iii", module_contracts.yaml:675-719); peninsular_strain + systems/overview/sim/ms_track.py (MS clock floor 0 ceil 100, -1/yr, start 60, no live caller; ms_track.py:1-29, :499-502); faction_state Mandate/Treasury/stats 1-7 (action code deleted at 29b, :77-107); accounting_sequence (:921-948).
E-06 S4 repo module roster is 26 rows (module_contracts.yaml:75-905): piety_track/territorial_piety, miraculous_event, ci_political, faction_politics, settlement_layer, domain_actions, game_director, scenario_authoring, campaign_architecture... mostly sim_module: none. systems/characters/sim/conviction.py is the PERSONAL piety_track's code (:178-182), not just a "scar oracle".
E-07 S4 player position: D-2 RULED yes: RB-3 builds IN-46 (grid-mode suspension, played fight) and IN-47 (character-sheet space) (-01:153; -02:546-591). Repo comparative frame: player = "embedded: one person's decision procedure" (00_COMPARATIVE_ANALYSIS.md:312).
E-08 S4 rulings D-1, D-2; hunks L0-1 (params_tables retired, DEF-9), L0-2 (threadwork head -> coherence.py), L1-1, L1-2, L1-3 (04 §B.13 claims MECHANICAL all twelve but invariants 5 and 7 unbuilt), L1-4 (AX-7 narrowed), L1-7 (a need is a Query plus held claims) (-04:214-223) absent.
E-09 S4 remediation reduced to one sentence; missing: row-by-row verdict (R-01..03 stay met, may fall; R-04,05,07 move up no guarantee; R-06,08,09 made honest; -01:29-31); batch purposes RB-0 PLAN(paper), RB-1 INSTRUMENTS(hash-equal), RB-2a/b FORMATION AND SCARCITY, RB-3 SCALE BUILDS, RB-4 LAYER-1+NERS, RB-5 HUNGER; critical path (-01:50); "cannot" list (-04:303-305).
E-10 S4 JQ-3 (four character-change magnitudes H-187,H-188,H-200,H-208; -04:57-66) and JQ-5 (-04:77-83) never appear; JQ-2 options "materially different games" (-04:53-54).
E-11 S4 hunger result: even with RB-5, binds only before first yield (cover 21.7 -> 41.7; K13 -04:296; -03:250-251) missing from overview.
E-12 S4 repo already has sourced "Twenty Games" axis set: population resolution, named-agent cardinality, contested object, player position, control channel, coupling latency, durability/ending, clock count, legibility (00_COMPARATIVE_ANALYSIS.md:302-336); closest whole-game analogue Mount & Blade (valoria_game_precedent_companion_v1.md:506). Overview §7 lacks player position, control channel, contested object, ending, progression.
E-13 S3 "Godot is not in this repo": godot/ has 7 design docs + godot/skeleton/ (GDScript strike_module.gd, wound_module.gd, .tres); registry golden_path (module_contracts.yaml:976-981); does not compile (:985-989).
E-14 S3 `work` stated 78/0, 0/77, 0/82 in one document without recipe note.
E-15 S3 A3: "person.died also has a matter source, hunger" — at shipped values MATTER kills nobody (matter.py:513-520 continue; :549 skip).
E-16 S3 A5: hunger->body graded RUNS-IN-LOOP (inert) vs overview rule.
E-17 S4 A3: systems/combat/combat_engine_v1/state_graph.py:1-15 (duel state machine as DATA, tested) and capabilities.py:1-13 (weapon-affordance gates) not described.
E-18 obs LOC mismatch PC ~5,600/MB ~10,200 (overview) vs ~5,000/~13,500 (A3).
Verified correct (selection): 53 rows; pool2/Ob2 odds; control zeros fixtures.py:594,606-607,707,715; tau 0.1 fixtures.py:286; no hunger Query; four composition roles module_contracts.yaml:52-73; SC roll 127 LOC; FI 36 LOC; THE NINE 3/5/1 (requirements.yaml status lines); 40 items sum 8+7+6+6+3+7+3; engine tree.
Unverifiable-static: 72% from plan scratch session b70b5af; food cover 21.7->41.7, hashes from SP scratch files not in repo; 1,102 refusals/52.9% b70b5af.
Not opened by E: ci_checks_registry.yaml, tools/, canon/, engine/season/tests/, architecture/ bodies.


## Round-1 audit F (logic and consistency)

# Audit F (logic/consistency) — findings as returned (condensed; 41 findings)
S1: F1 TESTS-ONLY def makes whole loop TESTS-ONLY (chooser constructed only by harness/; "harness is the only driver") — redefine RUNS-IN-LOOP = non-refusal outcome inside SeasonDriver.season on build_realm under populated.run recipe; TESTS-ONLY = unit tests/fixtures/oracles. F2 overview §3 does not follow A5's stricter rule (NP "bodies RUNS" with tend 0/34 etc.; WT RUNS with migrate 0/81; GV "verbs TESTS-ONLY" covers release 3/45, issue 5/6, dispatch 6/18, transfer 1/45 which run; FA survey 13/57 runs; SC hides argue 0/10, determine 0/2). F3 "shared four-band margin ladder (social, combat, field)" is wrong: only social uses the ladder; combat uses Felled/Wounded/Untouched, field Won/Lost/Unopposed. F4 §7 cells for MB, SC kernel describe non-executing designs as play: add grade tag per cell.
S2: F5 chooser menu is resolvable_verbs() (populated.py:1531): 47, 46 with destroy_record withheld, not 53. F6 "a little noise": noise usually decides (cite seed-0 caveat; see audit E-02). F7 MB seam varies troop count + morale start + terrain row; SC bench reception/proofs vary the obstacle. F8 office +1 budget is unspendable at shipped fixtures (deliberate.py:89-97). F9 "5 per person-season" are scenes (<=3 acts each): ~8-10 acts per person per season. F10 chooser failed acts "leave a belief" except inquiries (finding.none undeposited). F11 22 verbs "produced outcome": 8 of 22 have writes [] (dispatch, challenge, speak, tell, interview, research, surveil, reconstruct); ~14 change state. F12 "1,132 acts" vs attempts sum 1,407 (=676+731): counter undefined. F13 A2 "stance via fight/accept/march/forgive": only march and forgive (effects_combat.py:426). F14 hunger as person.died source false at shipped values (matter.py:518-520, :549). F15 A6 grades work/restore/sabotage/tend/train/forgive RUNS-IN-LOOP/"unmeasured" but suite measured them (tend 34/0, train 38/0, work 77/0...). F16 A8 and A2 also mix grading rules. F17 "unproduced" in write_matrix means no verb row declares the field; conviction/scar are written by crisis and _scar_witnesses. F18 loops "close" claims: conviction loop (no measured effect on choice; confliction weight 0), yield loop one-way, wound->end return leg untraced — use "reaches X; return leg unmeasured". F19 "information model is strong": witness_key/post_remit admit nobody; 0 chained told claims; teller_weight inert; mean ledger 199/200 at 4 seasons. F20 "deterministic" -> "seeded-stochastic, reproducible". F21 "gate-rich, response-poor" mixes by-construction/ruled (train needs vocab key; destroy_record withheld; dispatch writes [] ruled) with defects (wrong-class referents REM-22/23, REM-27) and untraced (give): add cause column. F22 SC comparison class should be the shipped 2d10-vs-Ob-2 roll. F23 "nothing founds at runtime" -> in 2-season run. F24 "advantage never an obstacle change" holds for sigma-leverage only; bench room lowers Ob, forgery raises it. F25 kind A "season calls MB" (never fights); kind E WITNESS "inert yield" wrong (drives questions).
S3: F26 write matrix 40. F27 count variants work 78/77, commit 64/61, examine 62 attempted. F28 §3 header mixes counters/horizons (resolved counts, 1-season aperture, 4-season scar). F29 LOC mismatch. F30 weapons 50+4 forms, traditions 7+none. F31 march: A5 says attempted 21 refused 25 (refused > attempted); A2 25 attempted 21 declared. F32 offices.yaml "31 seats (all held)" but per-case loop seats 24 (offices.yaml:120); 24 live holds of 32. F33 17 territories (provinces are a Query), not 17 provinces. 
S4: F34 32nd office = off_npc_084 (offices.yaml:124-127). F35 authored obligees are oblige tenures "with no term" (offices.yaml:128) so they cannot lapse at MATTER: upkeep loop cannot start in realm. F36 PC: actor never written; scene fells actor in ~half of mirror fights; cohort deleted whole by one Felled. F37 mean ledger 199.0/200 at 4 seasons.
S5: F38 "a battle, a theft and a decree reach the same chooser": no field fought, no theft verb. F39 typed precondition on 43 of 53 rows. F40 "complete" -> "running" (invariants 5,7 unbuilt; presence: DESIGN-ONLY). F41 findings land same round after RESOLVE at WITNESS, shape next round's question.
GRADE RULE recommended: grade a behaviour not a body. RUNS-IN-LOOP = non-refusal outcome in SeasonDriver.season over build_realm under populated.run recipe; barrier passes (MATTER, CENSUS, WITNESS) always qualify. "RUNS-IN-LOOP at control" for inert shipped fixtures (body_step=0, telling_privacy=0). Wired with zero successes = TESTS-ONLY and must cite a test (revoke: test_in31_revocation_cost.py; covenant: test_in12_covenant.py; test_in12_step9.py, test_in12_forgive.py); nothing executes = DESIGN-ONLY. Refusal gates graded separately as gates.
UNVERIFIABLE: off-by-one between A2 and A5/A8 counts for one recipe (work 78/77, sabotage 35/34, survey 58/57, forge 53/52, create_record 88/87, utter 40/39, interview 33/32, reconstruct 40/39, commit 64/61): counting (causes[0] vs causing_act) or cross-process nondeterminism (only A7 pinned PYTHONHASHSEED=0; repo has fixed this class before: rosters.py:668-672).


## Round-2 audit G_T01_T03_T07

# Round-2 audit G (T01, T03, T07) — findings (15; no S1)
F1 S2 ctl "attempted" = acts that reached _fold (d.resolved is appended in _fold, resolve.py:377-379); contested/graded acts refused at admission (resolve.py:1025-1032) and S27.4 party-gap refusals (:714-728) never reach it. So for tell, speak, research, surveil, fight, accept: "attempted" = admitted and rolled; "ok" = exactly Partial-or-better. Relabel column "admitted (reached the roll)". (T01 #8 claim about ctl; T03 labels fight 7/accept 18 "attempted".)
F2 S2 T01 §5d: hearer holding copying 1-3 easier: only scores 1-2 (Ob 0.5-1) are easier; score 3 -> Ob 1.5 plays as Ob 2.
F3 S2 T01 §4: speak/determine "requires" are prose strings; typed cells: speak = DocketItem existence only (venue half not typed, verb_table.yaml:1073-1077); determine = party/docket/bench/quorum, drops the date (:322-341).
F4 S2 T03 §0/§4/§5c and T07 §0/§7: "up to 5 scene actions" -> 5 scenes each up to 3 acts (fixtures.py:488); a fight is one act within a scene. T01 states it correctly.
F5 S3 T03 §8#6: "0 of 12 executed accepts had a challenge" is an IN-08-era 4-season measurement (142 attempted, 12 executed), not this run.
F6 S3 T07 §0: cites draft grade rule; use ERRATA G1; regrade co-movement and threadcut.
F7 S3 T07 §2.6: "docstring '6 rows'" is an inline comment (opposing.py:172).
F8 S3 T01 §4: "driver releases at most 5" is the disputed reading; cite both deliberate.py:89-97 and fixtures.py:497-502.
F9 S4 T07: DEPTH_TS_MINIMUM, BREADTH_OB, DISTANCE_OB read by nothing at runtime but exported to engine/engine_params/sim_params.json:3131-3204 and value_pointer_links.json:233,:528,:689: dead constants cross into the port contract.
F10 S4 T07: attempt_leap docstring says target_state takes optional 'ts_minimum' (default 30) but code hard-codes ts < 30 (operations.py:354-360); a caller cannot raise the gate.
F11 S5 T03 §2.5: overwhelming 26-28 "three wounds": 26//9 = 2 wounds; "26 (two) to 28 (three)".
F12 S5 T03 §2.1: stance term added at weight 1 + stance_gain, stance_gain ships 1.0 (choose.py:74-86; fixtures.py:837): doubled.
F13 S5 T01 tell row: confidence.broken never fires at shipped telling_privacy 0 (verb_table.yaml:1197).
F14 S5 T07 §2.7: actualised co-movement column is often the more negative (co_movement.py:44-58), not "larger MS number".
F15 S5 T07 §9: threadwork line count 1,950 vs ERRATA 1,955: state scope.
Verified correct: T01 Table A pool 2 and 3 by hand; Table B boosts; obstacle composition; S27.4 cannot fire; Gaussian pool-2 odds; 133 rolls = 70+63; T03 wi/mw/health tables end 1-4 (9/3/40/18, 8/2/27/15, 7/2/23/12, 6/1/13/9); pool 9, Ob 1.5; wound impairment as sigma (+0.25/-0.15); read contest; outcome-map constants; _eff_kill writes subject only; 650 example; 400-fight consistency; T07 pool 14; coherence arithmetic; opposed Ob; loop never reaches threadwork; mending defect.


## Round-2 audit H_T05_T06

# Round-2 audit H (T05, T06) — findings (16; no S1)
F1 S2 T05 §0: commit/convene/carry graded TESTS-ONLY "refused every time" — ctl: commit 56/1 seed1, 63/1 seed2; convene 5/1 seed2 -> grade per seed per G1; only carry is 0 everywhere.
F2 S2 T06 §2.8/§5d: wrong reason inquiries stay pool 2: VERB_CAPABILITY maps only tell and speak (rosters.yaml:1228-1231); _capability returns None for unmapped verb (sigma.py:113-116); no capability row names an inquiry -> writing capability would NOT change inquiry pools.
F3 S4 T05 §3.2/§5b5: proofs are near-zero in practice: mirror matches any claim opponent holds with same (subject,predicate) (world_q.py:632-633); unpaired deed attributed only when subject is the doer (person_q.py:153); doer witnesses own act (co_located; epistemic.py:555) so nearly every proof is self-mirrored unless evicted.
F4 S3 T06 §0: seed-2 `inferred` claim implies post_remit admitted someone on seed 2 (inferred producers: witness.py:598, :514-524, :289) -> say "seed 0 only" or regrade.
F5 S3 T05 §3.1: news.untold still deposits event-kind and seen claims (witness.py:359-365); only finding.none undeposited (rosters.yaml:1145); only told content withheld (witness.py:860).
F6 S3 T06 §0: destroy_record formation is TESTS-ONLY, withheld by fixture (verb_table.yaml:306,312; fixtures.py:923), not DESIGN-ONLY.
F7 S3 T06 §4: not every inquiry/doc row includes `own`: open_case is remit:determine only (verb_table.yaml:902).
F8 S3 T05 §2.1: generator at resolve.py:792, not :806.
F9 S4 T05 petition: computed petition's `to` and `subject` bind one referent (verb_table.yaml:941; effects_information.py:401-409) (H-94).
F10 S4 T06: add G11 caveat; interactions_per_scene=3 at fixtures.py:488 (so "<=3 acts per scene" is confirmed).
F11 S5 T05 §5d: "hostile room cannot hurt you" is true only against a defaulted Ob 2; with an opponent holding capability the base Ob < 2 and a hostile room raises it (roll.py:89-94, :103-113); inert in realm only because nobody holds capability.
F12 S5 T05 vs T06: the copying:3 person is in the 430-person case corpus overlay, in no realm run (rosters.yaml:1222-1224; build_realm never writes capability).
F13 S5 T05 §2.3: judges' date.fired claim: code checks subject, predicate, when == due_at from any source (world_q.py:298-299); drop "firsthand".
F14 S5 T05 §2.4: kernel leverage +0.5 only on-ground (primitives.py:228-230).
F15 S5 T05 §7: REM-24 = "petition forms on a Person only" (remediation-02:387), a formation change.
F16 S5 T06: anyone co-located learns who inquired (epistemic.py:428-453); examine "never attempted" not "never formed".
OBS: _ch_chronicle broadcasts any Event whose kind appears in ANY binding_decision row's emits (epistemic.py:685-686): determine emits pursuit.moved (verb_table.yaml:355) so argue's pursuit.moved (:157) also goes realm-wide. Chronicle claim now CONFIRMED (epistemic.py:649-686).
Verified correct: T05 odds table rows, obstacle composition order, room arithmetic, reception remove weights, determine conjuncts/quorum, Partial/Failure writes, arrangement counts/keys, kernel tally arithmetic; T06 removes 0,1/3,2/3,2/3,1; refraction table 100/83/67/50; finding_terms; Partial closes trail; decay; eviction; dedup; cover/anchor; forgery +1 capped; knots Close 14%/Distant 33%.


## Round-2 audit I_T08_T09

# Round-2 audit I (T08, T09) — findings (19; one S1)
F1 S1 T09 §5a "secure succession" and T08 §5d: "a dead holder's seat falls vacant; confer can refill it" is false for 6 of 31 authored seats: _req_confer refuses any office with no conferral basis (loop/predicates.py:126-127; has_conferral_basis = roster membership, gate.py:643-657); King, Duke of Valorsmark, Duchess of Hafenmark, Widow Regent, Heir, Princess have `conferral: null` (offices.yaml:188,201,214,240,253,266); succeed has no effect (verb_table.yaml:1113). A null-conferral seat, the throne included, stays empty forever once vacant.
F2 S2 T09 §0/§5b/§6: occupation for `seize` = mustered(rid, seat faction): ANY faction member standing in the subtree, residents included (effects_information.py:927-931, 959); tests/test_march.py:918-927: at seed 0 the Crown seizes Church-held set_s_036 with no march, via resident p_npc_037. March is one way to get members there.
F3 S2 T09 §1: "16 of 17 territories held by four persons" counts add to 15 (populated.py:1086-1087: of 16 provinces held, 15 re-home to a person, Schoenland's does not): 15 of 17 held; T15 unheld; T16 (Schoenland) unheld and outside the realm.
F4 S2 T08 §2.3 may-revoke: rung_above_in_holdings = your seat is on the parent rung AND you hold the TARGET seat's own rung: in_holdings(w, actor, off.rung) (gate.py:555-565; offices.yaml:81-84).
F5 S3 T09 leaders: one entry per held SEAT (world_q.py:1412-1416); p_npc_020 holds off_npc_020 and off_duke_valorsmark (both Crown) so listed twice; "Crown 11" is 10 people; counts add to 32 = seats, at most 31 distinct holders.
F6 S3 T09 vs T08 remit "closed" vs open: rosters.yaml:316 `open: true`; prose says CLOSED (rosters.yaml:315; verb_table.yaml:257,801,1478): tree contradicts itself.
F7 S3 T09 §7: dispatch "14 of 15 computed orders name a non-person" is an old in-tree figure (verb_table.yaml:383); ctl: dispatch 18/6, 18/7, 10/10 (seed 2 every dispatch executed).
F8 S3 T08 §8: rung above a territory seat is the duchy, or the realm for T9 and unheld territories (populated.py:736-738; offices.yaml:66-68).
F9 S4 T08 §2.5/§5d, T09 §4: in the realm, harbour/seam/garrison sit on the settlement rung (populated.py:776,816) where that settlement's cohort is always present (:441); share counts persons on that rung (world_q.py:436, 1181-1186): any individual shares with the cohort, n >= 2, half per act.
F10 S3 T09 §2.1: since IN-11 a live edge's object puts a Proposition in reach (effects_information.py:1013-1018; verb_table.yaml:1501); commit executes in seeds 1 and 2 (ctl 56/1, 63/1); conclusion holds only for non-members (no edge to the faction's Proposition).
F11 S3 T09 §8: holder_faction_of callers: survey, seize, _eff_march, uncontrolled (world_q.py:1736), faction_of (:1695); seam/wrappers/mass_battle.py mentions it only in docstrings/comments.
F12 S3 T08 §0: transfer executes 1, 0, 5 per seed (seed 1: 37/0).
F13 S4 T09 §1/§7: remit_default ("NOT CANON" test fixture) IS applied in the shipped realm build: every loop-built seat is seated with it and keeps dispatch via remit_unruled (offices.yaml:100-119,141); that is where dispatch, and so march, comes from (22 of 23 loop-built seats may march).
F14 S3 T08 §1/T09 §8: loop-built seats are off_npc_NNN; six minted seats keep their row ids (off_duke_valorsmark, off_lord_steward, two cardinals, off_senior_inquisitor, off_restoration_leader; offices.yaml:120-127; populated.py:1304).
F15 S3 T08 §4: evade/defy is NOT resolvable (untyped, no predicate; verb_table.yaml:405-408).
F16 S5 T08 §4 dispatch: CENSUS individuation on an absent id: person.individuated is 0 in all three ctl seeds: TESTS-ONLY in the realm.
F17 S5 T09 §2.2: T16/set_s_037 outside the containment tree by design: Schoenland is foreign, built as a root rung (populated.py:725-735).
F18 S5 T09 §0/§2.4: "every FA act except sabotage is remit:-eligible" false: survey, forge, commit, release, utter, oblige, give are `own`; limit to covenant, seize, march, dispatch.
F19 S5 T08 §5d: "Food is in permanent surplus": harbour wear 10/season and nothing repairs (restore 0/23) so yield reaches 0 at tick 100 (rosters.yaml:1466); say "surplus within any plausible horizon"; `body` is not a Site (rosters.yaml:1386).
Verified correct: T08 §3 stores 40/30/50/10 -> 75/57/99/19 and truncation; grain 108->142->176->210; 322 condition.worn; renewal clauses; D02 cover 21.7->41.7 only if ore and timber count; Senior Inquisitor seat has [determine] only; confer conditions; work gate; works costs; capacity; conferral 17/8/6; season 0 no shortfall; T09 head always None; at_war no caller; members/mustered/density/fortification_of; seize Rung half; march non-settlement empty army -> Unopposed; covenant mint; sovereign_fraction (0.4, 304) = 6/15; all attempted/ok counts match ctl.


## Round-2 audit J_T02_T10

# Round-2 audit J (T02, T10) — findings (17; one S1)
F1 S1 T10 §2.5, §5d, trap 9: treats the sixth budget point as "disputed / office may make first journey free". The code decides: budget counted in scene ACTIONS (budget.py:19-20); pack_scenes treats it as a COST budget, extended scene = 2 (choose.py:578-585, :645-658); driver releases 1 scene/round over 5 rounds charging cost(ext) (deliberate.py:252-259). Budget-6 holder spends 2+2+2; a leg (6->5) loses an act: 9 acts become 7. Real ceiling 5 scenes x cost 2 = 10 actions. T02 trap 4 is right; T10 contradicts it. => ERRATA G11 DISPUTE IS RESOLVED by T02/J.
F2 S2 T10 §3a: a multi-act scene is extended and costs 2; greedy packing: budget-5 first scene costs 2 -> remainder 2 not 3; rounds run 0..4 (driver.py:456).
F3 S2 T10: budget unit is "scene actions" (budget.py:19-20), not "scenes".
F4 S2 T02/T10: `utter` also opens a maker's hold on its Proposition (effects_information.py:1010-1034; _makers_hold :125-139); hold-minters: create_record, issue, open_case, petition, survey, forge, utter (+ conceal's cover Record via _mint_document :269). utter always succeeds (39/39, 39, 49) -> budget lever on a par with create_record.
F5 S2 T10 commit row: "cohorts cannot commit (NP-G36)" has no code gate; commit needs only that a Proposition exists (verb_table.yaml:171-175); is_cohort read only by subsistence and hazard (world_q.py:1012, :1074); H-171 limit 4: cohorts act like anyone. NP-G36 is [PROPOSED]; observed: none did.
F6 S2 T10 §6: forgive RAISES stance_toward (removes negative rows, person_q.py:68-77; effects_combat.py:441-449); teller_weight reads regard keyed on the teller PERSON (options.py:1517-1522); battle grudge row keyed on the winning faction (effects_combat.py:302-303) so forgiving a faction changes no teller's weight.
F7 S4 T10: Schoenland's territory is minted as a ROOT with no parent (populated.py:725-735); contain.path needs a shared ancestor (world_q.py:2709; containment.py:95-112): nobody can move or migrate into T16/S-037; Schoenland's cohort cannot leave; every journey into/out is travel.blocked.
F8 S3 T02 §8: restore is NOT uncelled by design: its uncelled note says "THE PREMISE IS STALE ... its cells are owed" (rosters.yaml:2979-2985); only tell and thread_read are by design (:2969-2978). OVERTURNS ERRATA G13 for restore.
F9 S3 T10: terrain: polygons, water:, provinces: ARE read at runtime by data/geography.py:3-8 for the mass-battle field (TESTS-ONLY: no seeded field is fought; tests/test_mass_battle_module.py:39); only adjacency, settlement_adjacency, terrain_cost_matrix, march_budget, poi_catalog have no reader.
F10 S3 T02: pursuit weights not normalised (Saemund sums 1.31; npc_registry.yaml:188-202; pursuits.py:82-89).
F11 S3 T02 §7: REM-21..25 + REM-2C are RB-2a; REM-26 opens RB-2b (remediation-02:308-310).
F12 S3 T10: geography file says both 55 (:580/:589) and 56 (:602); "24 primary + 1 sea" (:640).
F13 S3 T10: wear rates harbour 10, seam 10, dwelling 0, garrison 0 (rosters.yaml:1465-1470).
F14 S4 T02 gates: rows whose `to` is a known person form one Candidate per known person (operand_bags, options.py:267-278); train one per vocation (:279-280); self-contest and self-counterparty declines (:261-262, :302-303).
F15 S5 T02 §0 vs §7: say "non-control arms TESTS-ONLY".
F16 S5 T10 trap 5 vs §5b: cohort "never" settles at shipped build; build grows capacity (world_q.py:1317-1321).
F17 S5 T02 §2.9: 73% is pairwise P(A before B), P(first among 30) ~0.17.
Unverifiable: T02 u-value 0.9505 equals first question's salience (suspicious: check copy error); ctl-derived acts per person-season = 7.2 (ERRATA G11 "~8-10" not supported by ctl: correct to ~6-8).
Verified correct: T02 axis vector sums; cells and scores (-7.8663/-7.9765; P=.751); Gumbel keys; stance gain x2; budget trail; step order; attention tiers; tenure kinds; shift 2 crisis 3; T10 path rule, capacity, MATTER arithmetic 75/57/99/19, hazard, MATTER kills nobody, tend/train/forgive, stance writers.


## Round-2 audit K_T04

# Round-2 audit K (T04 mass battle) — findings (14; no S1)
F1 S2 T04 §3.1/§5b2/§8#4: the binding rout rule is 100 troops, not 80: Unit.recalc_size effective_size = hp/100, size = floor(...), routs when size 0 (units.py:2933-2936), every tick (orch:2205-2206) before the 80-troop check (orch:2262-2268); on a single-subunit army the 80 floor never binds first; a side of 80-99 troops also routs on tick 1 (matters for REM-32).
F2 S2 T04 §5b3 "by 2 in a same-faction field": cannot happen; sides_of sets subject None when holder is marcher's own faction (sides.py:131-132) -> Unopposed (SW:236-251), no losers (EC:259). H-151 note in MB.py:139-142 stale.
F3 S2 T04 §3.2/§8#9: "no contact because discipline<3 speed 0.4" contradicted by its own data (stance-hold row: A static, B closes 1.0 cell/tick and contact made; 4v1 closes 1.1 and no contact): contact not monotone in closing speed; cause unexplained.
F4 S2 T04 §3.2/§8#8 Column "draw for draw identical on all 200 seeds" is the signature of an arm that never took effect (CLAUDE.md §0.1 pt 3). Command 2 explained by code: pool does not read command under POOL_QUALITY_MODEL (exchange.py:103-124); reform needs command >= discipline+1 = 6 (orch:322-328).
F5 S4 T04: WALLS mechanism: season power 4, walled DR 1+3 = 4: Success (damage = power) does max(0,4-4)=0; Partial 0; only Overwhelming (5-4=1) hurts the defender (cfg:307-308; orch:1377-1378).
F6 S4 T04 §5c: levers on walls: garrison wear 0 so walls never decay (rosters.yaml:1451-1470); sabotage writes Site.condition downward (verb_table.yaml:1034-1035); restore raises; a settlement minted by found gets no Sites (effects_founding.py:109) so fortification 0 and river/polygon rows become reachable (TESTS-ONLY).
F7 S3 T04 "25 of 32 realm offices grant dispatch" comes from remit_default "NOT CANON. A TESTING FIXTURE hands EVERY seated office EVERY remit act" (rosters.yaml:324-334, :376): default-build limit, not a rule.
F8 S3 T04 "no attackers -> PARTY-GAP at the provider": on the season path refused earlier by _refuse_party_gap at resolve.py:787-788; provider branch (SW:225-227) unreachable from march.
F9 S3 T04: terrain row constants at terrain.py:45-50 (not :60-65).
F10 S4 T04 arrival play: marching on your own origin settlement is refused (NO_CHANGE, EC:257-263; VT:828).
F11 S5 T04: at most one degrade_discipline per phase boundary (state.py:233-237); morale cap min(loss,3)*0.7 = 2.1 (state.py:112-117); exhaustion term (state.py:95-96) omitted.
F12 S5 T04: 1000 -> 10 x the SIDE's summed weight (pct = sum weight/100 under 100 troops; MB.py:285; EC:299).
F13 S5 T04: seed-1 breakdown 6+3 = 9 of 10 acts: name the tenth.
F14 S5 T04: comment at units.py:1847 says "disc3 -> 0.4" but code at :1823 gives 0.7 at discipline 3.
Verified correct: morale start formula; single Line infantry subunit P4/C4/D5; both sides at (8,12); WALLS before river (terrain.py:174-180) upheld over draft A3; all 37 settlements fortified (populated.py:815-818, world_q.py:1505-1511); attacker_wins rule; 6 troops -> 0.06 -> body 60; 250 -> 1.25; loser-only writes; MARCH_TARGET_KINDS = [settlement]; budget formula; friction; support weights; Lanchester constants; ladder; discipline speed multipliers; volleys; troop stats; reach; army rout; wired/unwired instructions; empty hooks; MB_CELL_MORALE default '1'; march counts 21/10/4 with field.* 0.


## Round-2 audit L_cross_tutorial

# Round-2 audit L (cross-tutorial consistency, verb coverage, teaching completeness) — findings (23)
X1 S1 "Each act costs one of your 5 scenes"/"Five scenes hold up to 15 acts"/shared move-scene charged 1 appears in T08 §0/§4, T05 §4, T10 §3a/§8.9, T03 §0/§4, T07 §0, T04 §0. Truth: a chunk of >1 act costs extended_scene_cost = 2 (fixtures.py:489); chunk trimmed to one act when only 1 left (choose.py:653-657): budget 5 -> 2+2+1 = 7 acts (T02 §2.6 right); 15 acts needs budget >= 10.
X2 S2 G11 settled: fixtures.py:497-502 (a COST budget) and deliberate.py:89-97 (a SCENE ceiling) count different quantities; choose.py:643-657 spends the cost; T02's reading reconciles them. A leg still costs a budget-6 holder one act (2+2+2 -> 2+2+1). Delete T10's "free journey". (n=1 instrument but code supports.)
X3 S2 T01 §4 determine/speak requires copy prose; typed cells differ (determine drops the date; speak's venue half not typed). Teach requires_typed.
X4 S2 G1 applied inconsistently across seeds: T05 says convene/commit refused every time vs its own table (convene 5/1 s2, commit 1 ok s1,s2); T08 grades convene/confer/oblige as executing; T10 grades give (19/1 s2), commit TESTS-ONLY; T05 counts determine (1/1 s1) executed. One seed rule: "executes at seed N".
X5 S2 T10 commit: "cohorts cannot (NP-G36)" no gate (= audit J F5).
X6 S2 T06 "examine never formed/0 attempted": ctl counts d.resolved only; examine is formed 62 times in seed 0 (w.acts) and refused at admission; say "never passes admission".
X7 S3 T09 vs T08 remit "closed roster" vs "open: true": tree contradicts itself (rosters.yaml:315 "CLOSED five", :316 open: true; verb_table.yaml:257 "is closed").
X8 S3 T10 repeats "cover 21.7 -> 41.7" without T08's caveat (figure counts ore and timber as food; grain alone ~10 seasons).
X9 S3 T03 vs T10 tend refusals (34 seed 0) split differently (18 absent/2 not-with/14 whole vs 20 failed "with"/14 whole): one flat kind tend.refused (verb_table.yaml:1164-1165); both inferred.
X10 S3 acts per person-season ~8-10 (errata) vs 6.3-8.0 (T10) vs 7.2-7.6: bases differ (d.resolved 1,132 vs w.acts 1,407); name the basis; ERRATA G11 "~8-10" not supported by ctl.
X11 S3 T04 budget "max(1,5+offices-3)": holds, not offices.
X12 S3 T07 §0 uses the superseded reachability grade rule (see audit G F6).
X13 S3 T01 research eligibility ["own","presence:<site>"]: own admits anyone; presence: never admits (verb_table.yaml:1366).
X14 S3 T10 forgive-then-listen (= audit J F6).
X15 S4 conviction crisis never graded or counted in any tutorial (ERRATA G7 says built); Saemund reaches affiliation scar 1 after one season; whether a fold fires is unmeasured per tutorials (S2's earlier run: 9 rewrites in 4 seasons).
X16 S4 T08 §4 lacks `comply` (verb_table.yaml:191-204: typed dispensation and own_ledger; writes []; emits compliance.given).
X17 S5 "every binding_decision ACT is broadcast": the channel is a KIND filter (epistemic.py:652-654, :685-686); includes MATTER's tenure.closed.
X18 S5 T09 "every FA act except sabotage is remit:-eligible" vs its own 7 `own` verbs: true only of the FA host roster.
X19 S5 run columns: T02 ok/attempted vs T03-T10 attempted/ok: one order.
X20 S5 first draw named "season 0 MATTER (tick 0)" (T08) vs "season 1 MATTER" (T10): use tick numbers.
X21 S5 seed-0 speak formed 22 (T02) vs 21 (T05).
X22 S5 T04 "unheld target means defender None": holder_faction_of walks to the territory holder; say "holder_faction_of is None".
X23 S5 T02 "confidence 100 at deposit": refraction lowers (67 or 50).
VERB COVERAGE: 46 of 53 taught with prerequisite, outcome, writes. Partial: comply (T02 only). Not resolvable and only named: evade/defy, construe, exchange, succeed, tie/knot, thread_read (T06/T07 give its row). destroy_record in T06.
PRIMITIVES used but undefined where used: Rung, Tenure, Record, Proposition/mood, Office/purview, stratum, prize, the "with" relation, establishment, Observation carrier (nowhere), Calamity/Locked Zone/Exposure (nowhere), process ids H-/REM-/JQ-/D-V/R-/M-/J-T (no glossary anywhere).
GRADES (0-3 x 8 criteria): T01 23, T02 23, T03 24, T04 21, T05 23, T06 23, T07 18, T08 23, T09 22, T10 22. Weakest: T07 (teaches an oracle that is not in the game; Calamity/Locked Zone/Exposure undefined; no consequence for "stay human"; outdated grade rule) and T04 (one verb; never fields a battle; "defend" listed as action but is not one; Rung/Tenure undefined; goal plays reduce to "Unopposed or nothing").
FRAMING: T06 §5d "Telling to companions is wasted" generalises 4 seed-0 tellings; T04 §5b3/§8.8 "morale/command don't matter" is a 200-seed null on one single-subunit configuration (draw-for-draw identity untraced).
COMPARISON HANDLES STILL MISSING: cross-subsystem action-economy table (cost per act, acts per season, what each degree buys); in-world time per season/turn/tick; campaign length and absence of an end state; one resolution-family summary with genre analogues; sources and sinks per resource (coin absent); player-interface position; information model vs standard fog-of-war.


## Not preserved verbatim

Round-1 audits A, B and C (accuracy of the overview and appendices A1–A8; 15, 13 and 18 findings) were applied through Part 1 above (ERRATA G1–G20, C1–C9)
but their original tables were not saved to files; their substance is in the ERRATA lines tagged [A-nn], [B-Fnn], [C-Fnn].

## Control-run method

`ctl/control.py` runs `build_realm(seed)` for two seasons with the chooser built as `harness/populated.py::run` builds it. "att" counts acts that reached `_fold`
(`d.resolved`); "ok" counts acts with at least one non-refusal event attributed by `Event.causes[0]` (`control.py:13`, `:21`). Not counted in "att": acts whose actor
was already gone, refusals for an obstacle too high for the pool, and contested or graded acts refused by `_admits` before the seam (`loop/resolve.py:974-998`,
`:1012-1032`); other admission refusals are counted. For `tell` and the graded inquiries "ok" is Partial-or-better, because their Failure kinds end in `untold` or
`none`, which `control.py:13` treats as refusals; for `speak`, `argue` and `determine` the Failure kinds (`turned`, `lost`, `undetermined`) count as ok; for `fight` and
`accept` it means Felled or Wounded on the subject (Untouched is `contest.undecided`; seed 0: 15 ok = 9 `person.died` + 6 `body.changed`). Output is identical across processes (checked with random PYTHONHASHSEED). Results differ by seed.
Round 3: re-run at `51d7b05` for seeds 0, 1 and 2; the three outputs are byte-identical to the committed files. The acts the "att" column leaves out
are counted in the act store (`w.acts`); Part 3 R-F3 gives both.


## Part 3 — Round-3 findings (precedent-disposition pass and I1 verification)

**Method.** A verified precedent suite (`research/game_precedent_suite/`: capability tables and "how it plays" tutorials for about seventy
games, and the disposition record) was routed game by game to the ten Valoria tutorials. Thirteen read-only Opus disposition critics gave
every routed item HAS / LACKS / DIFFERS / CONTRADICTS / DISCARD against a named tutorial section and a code line opened at `3aa908b`
(`a4ca9a5` plus this suite). The I1 verification (at `3aa908b`: an independent re-check of the capability inventory, with paired controls for
ten named refusal causes; `seize` not run) gated the critics. A re-run of `ctl/control.py` at `51d7b05`, byte-identical for seeds 0-2, gated the appliers.
Ten appliers made the CONTRADICTS edits to files 02-11 after re-opening each cited line at `51d7b05`; one more revised files 00, 01 and 13
and re-ran the decisive probes there. No LACKS row survived `CLAUDE.md` §0's five-step triage as a Jordan question, and none is this session's work:
each stays design-level, reference only. Except `ctl/`, the probes cited here (the I1 verification, the seam trace, the round-3 trace, the revoke scan)
were session files and are not committed; their numbers cannot be reproduced from the tree, and each is tagged "(uncommitted round-3 probe)" at its first use below.

**Round-3 findings.** Each is a fact several critics found independently, re-opened at the code at `51d7b05`; none is a ruling of Jordan's. Where one overturns a line above, it says which.

- **R-F1 Null-conferral seats.** Seven of the 32 built seats have no conferral basis and can never be refilled once vacant: King
  (`off_npc_020`), Queen (the Widow Regent row, `off_npc_032`), Prince (the Heir row, `off_npc_031`), Princess (`off_npc_030`),
  Duchess of Hafenmark (`off_npc_050`), Duke of Valorsmark (`off_duke_valorsmark`), and the unauthored guild-leader seat `off_npc_084`.
  Evidence: `conferral: null` at `engine/season/offices.yaml:188, 201, 214, 240, 253, 266`; `harness/populated.py:1240-1250` builds
  `off_npc_084` with no row, so `conferral=None`; `has_conferral_basis` (`state/gate.py:643`) and `_req_confer` (`loop/predicates.py:126-127`)
  refuse them; `succeed` has no effect (`verb_table.yaml:1113`). Probe: appointed 17, elected 8, none 7, the same list in seeds 0-2.
  The King dies at tick 0 in every seed (seed 0: Wounded in a fight with `p_npc_006`, who fell, then Felled by the Queen's `accept`); seats vacated after two seasons
  (ticks 0-1) are 8 / 7 / 10, null-basis seats 3 / 5 / 6 of them (uncommitted round-3 probe); one seat is refilled across the three seeds (seed 1, a
  self-conferral of `off_senior_inquisitor`), so the seats still vacant at the end are 8 / 6 / 10. **Overturns Part 2 C8's "six"**, which counted authored rows only.
- **R-F2 Revocation.** A revocation can pass only through `off_duke_valorsmark`: the six (seat, target) pairs at build all use it, held by the
  King (`state/gate.py:452-484`; revoke scan, uncommitted round-3 probe). The realm seats are on the rung above the duchy seats but fail on
  faction or holdings (`offices.yaml:78-85`; `state/gate.py:452-484`, `:547-565`). It is vacant from tick 0 in every seed and has no basis, so after
  that no `revoke` can pass, on top of the computed acts' missing `office` operand (I1 verification claim 2).
- **R-F3 The control-run column.** "att" counts acts that reached the fold (`d.resolved`, appended at `loop/resolve.py:377-379`), not acts
  formed: 1,132 / 1,122 / 1,175 against 1,407 / 1,394 / 1,447 in the act store. "Never attempted / never formed" is wrong for `argue` (formed
  10 / 17 / 18, every one refused before the roll), `speak` at seed 1 (14 formed, all `speech.unheard`), `examine` (62 / 59 / 39 formed, none
  admitted) and the `determine` (2 / 6 / 2), `accept` (34 / 29 / 29) and `fight` (19 / 13 / 17) denominators. Say "reached the fold" for a ctl
  column and give the formed count from `w.acts`. `thread_read` is never formed because the menu is `resolvable_verbs()` (`loop/driver.py:101`,
  used at `harness/populated.py:1531`), which lacks it. **Restates Part 2 C2**, whose word "attempted" this replaces.
- **R-F4 Player interface.** None reaches the season loop: the only seam is `dispatching_chooser` (`harness/play_surface.py:41-52`), exercised
  only by tests. Outside the loop, `systems/social_contest/sim/contest/agon_harness.py` is a stdin-played Bout-kernel contest (`input()` at
  `:148-155`): three scripted runs at `51d7b05` took 9 prompts over 3 exchanges each and ended in both `A_decisive` and a committee
  compromise. The same input (`yes 1`) gave different verdicts across runs because the harness never seeds `random`
  (module-level `random` at `systems/social_contest/sim/contest/resolver.py:12`, `:139`, `:334`; no seed in `agon_harness.py`), so no run tally is a
  measurement. Two HTTP designer workbenches trace a duel (with branch odds: the combat trace carries `dist`,
  `systems/combat/combat_engine_v1/workbench/server.py:8-9`) and a battle (one n=1 trace, no odds: `systems/mass_battle/sim/workbench/trace.py:11`;
  server `systems/mass_battle/sim/workbench/server.py`). **Qualifies Part 1 G16.**
- **R-F5 Hand-built acts.** A callback can submit any resolvable verb with any extra payload; every hand-built act of a resolvable verb, by its own
  actor, in a scene of 3 acts or fewer, was folded in the I1 verification (claim 5, uncommitted round-3 probe). A non-resolvable `exchange` raised `Unspecified` and aborted the
  season, an act naming another person as actor raised `Forbidden`, and a four-act scene raised `Ungraded`. A hand-built `march {subject: set_s_036}` by `p_npc_033` via `off_npc_033` gives `march.declared`, then
  `field.lost` at ENCOUNTER, in seeds 0, 1 and 2 (attacker body 1000 → 20, budget 6 → 3; re-run at `51d7b05`, uncommitted round-3 probe). So "no field is fought" and
  "the battle oracle runs only under tests" are true of the natural run, not of the loop. No natural `march` names a settlement in seeds
  0-2, so its army is empty and it is refused. The grade stays TESTS-ONLY (`engine/season/tests/test_march.py:80-136`,
  `test_a_lost_field_writes_casualties_and_stance_on_the_attacker_only`): G1 grades the natural run.
- **R-F6 Scene budget and acts per person.** Part 2 C1's budget arithmetic stands; its acts-per-person line (the "~6.3-8.0 ... w.acts 1,407" range) is
  replaced by the per-tick figures below. Budgets drift up because every held Record and uttered Proposition is a
  hold and `create_record` and `utter` always succeed: seed 0 mean 5.57 at build, 6.41 after tick 0, 7.69 after tick 1 (uncommitted round-3 probe), when
  11 of 74 persons have a budget above 10 (the 10-action ceiling is Part 2 C1's five scenes at cost 2; the hold-counting drift is H-92,
  `loop/deliberate.py:107-113`, whose own comment at `:89-97` gives 5). Per tick, per person alive at its start, seed 0: 8.1 / 9.4 formed
  (676 and 731 over 83 and 78 persons), 6.4 / 7.7 reaching the fold (535 and 597), at most 15. State the basis with every number. **Reconciles
  Part 1 G11's "~8-10"**: right for formed acts, not for the ctl column.
- **R-F7 Births.** ED-WR-0011 was RULED by Jordan on 2026-09-13, Option A: a closed cast of 46, no births "for now" (the second ED-WR-0011
  row in `registers/editorial_ledger_wr_archive.jsonl`; `loop/census.py:39-40`, "NO CLOCK GENERATES ANYTHING"). Calling it held or
  `needs_jordan` reads the superseded first row.
- **R-F8 Inquiry.** `examine` refuses every attempt because its `site` operand is filled with the question's subject (`decision/options.py:1047-1048`),
  never a Site. `research` is formed 125 / 109 / 116 times and makes `finding.made` 7 / 1 / 2 times (I1 verification); no found deposit
  (FI-03's trail) lands in seeds 0-2. A Partial finding closes that trail to its finder for as long as he holds that claim (`epistemic.py:356-366`); eviction
  at the ledger cap removes the claim (`state/ledgers.py:24-32`). People learn by presence, by being told (the told deposit,
  `loop/witness.py:822-830`, `:860`), by holding a written object (`document_key`), by the chronicle channel for binding-decision kinds
  (`epistemic.py:649`), and through a seat (`post_remit`, R-13).
- **R-F9 Economy.** In natural play no `work` or `restore` names a Site: the `site` operand is the question's subject (`decision/options.py:1047-1048`;
  I1 verification claim 2), and `work` also waits on a works Record that names the Site (Part 1 C5; `loop/effects_economy.py:103-104`). Given a Site,
  `work` can never run on dwellings and garrisons, 248 of the 322 Sites: their `band_floors` are empty
  (`rosters.yaml:2631-2632`), so the floor read refuses (`queries/world_q.py:2787-2801`); `restore` refuses at full condition. All 37
  settlements are built with one Site of each yielding kind (`harness/populated.py:771-776`), so they yield the same four goods. Yield reads a
  Site's condition and the season factor, never a worker (`loop/matter.py:589-591`). In seeds 0-2 population only falls (83 → 74 persons at seed 0;
  CENSUS individuation, `loop/census.py:57-77`, fired 0 times: ctl `person.individuated 0`).
- **R-F10 Combat and NPC life.** Every Wounded or Untouched band is a fight the attacker lost: over seeds 0-2, 33 of 59 combat calls felled
  the actor in the scene, exactly the 33 non-Felled ones (seam trace re-run at `51d7b05`); the seam returns both parties' wound states
  (`seam/wrappers/combat.py:230`) and `_eff_kill` reads the subject's only (`loop/effects_combat.py:108`, `:125`). None of the 39 resolved
  `accept`s answered a challenge from its subject (D_T03 critic's count over the I1 per-act rows). No score term reads hunger:
  `urgency(subsistence)` adds the same amount to every candidate and "CANNOT CHANGE ANY DECISION" (`decision/choose.py:220`). Migration
  0 of 367: destinations come only from places the mover's own ledger names (`queries/world_q.py:2111`), every effect call met a full
  hearth, and none of the 185 hearths empty at build was chosen (I1 verification claim 2).
- **R-F11 Odds.** The only closed-form helper for the social roll, `sigma_leverage.p_success`, is the Gaussian stand-in and understates
  Partial-or-better on the real social dice by 10-15 points at the four pairs measured (exact enumeration at `51d7b05`: 14.4 % against 26.0 % at
  pool 2 / Ob 2; 43.0 against 58.0 at pool 2 / Ob 1; 40.1 against 51.2 at pool 4 / Ob 2; 50.0 against 60.0 at pool 5 / Ob 2), by 17.3 points at
  pool 1 / Ob 1 (40.0 against 22.7), by under 5 points at Ob 3-4 for pools 1-2, and overstates at pool 1 / Ob 3. The combat workbench's
  `degree_distribution` (`systems/combat/combat_engine_v1/workbench/probabilities.py:30`) is a second closed form, for the combat roll. Under the ruled ladder Partial is never the most likely band
  at pools 1-8 against Ob 1-4 (largest 32 %, pool 2 / Ob 1). Layer 1: "No state is hidden from the player" (AX-7,
  `architecture/meta/01_AXIOMS.md:301-302`).
- **R-F12 Ending.** The realm as built reaches no ending. Since PR #494 the season reports `world_q.endings_reached` (IN-27,
  `loop/driver.py:515-518`; `queries/world_q.py:1764-1766`), "a Query over holds and seats that the season reports -- never an actor", over two rows (`rosters.yaml:2494-2553`):
  `peninsular_sovereignty`, the victory, "UNREACHABLE IN COMPUTED PLAY" by its own note (`:2531-2541`), and `theocracy`, not a victory.
  It returned `[]` after both seasons in seeds 0-2 (probe), and nothing halts on it. IN-23's `legitimacy` and `stability`
  (`queries/person_q.py:451`, `:480`) are one person's windowed estimates whose only reader is `harness/storybar.py`; IN-37's chronicle
  renderer (`harness/chronicle.py`) is an observer the loop never imports. Goals are attention-only (A-31, `engine/season/goals.yaml:10-12`)
  and nothing tests whether one is met. **Restates Part 1 G17**: the deleted `victory` layer is still deleted; an ending vocabulary now
  exists, is reported, and is unreached.
- **R-13 `post_remit`.** It admits one person: the King's obligee `p_npc_070` holds an `inferred` claim of a refused royal act at tick 0
  (uncommitted round-3 probe). The producer is the obligee predicate `_ch_post_remit` (`epistemic.py:563`, through `Act.via`; the claim source is
  set at `loop/witness.py:598`), not the seat-report limb (`:513-524`), which reads only actorless Events (`:517-518`); the Events are the King's refused
  `open_case` via `off_npc_020` (`act.ineligible`, seeds 0 and 1) and `revoke` (`revoke.refused`, seed 2). The claim is still held at the end of two
  seasons at seeds 1 and 2; at seed 0 it was deposited at tick 0 and `p_npc_070` is gone by the end of tick 1 (re-run, uncommitted). **Overturns Part 1 C8's "post_remit admitted nobody"** (round-2 audit H F4 had
  flagged it); `witness_key` still admits nobody.
- **R-14 The wound loop.** wound → body → `end` → next fight runs: seed 0, tick 0, the King is Wounded to body 450 (`end 2`) and Felled the
  same tick; over seeds 0-2, 11 calls met a subject below `end 4` and 7 Felled him (seam trace). **Restates Part 1 C9** for this loop.

**Corrections to the round-3 brief itself, resolved from the code.** The draft list for R-F1 named the Queen and the Widow Regent, and the
Prince and the Heir, as separate seats; each pair is one row. Its R-F8 said research leaves zero findings; it makes `finding.made` 7 / 1 / 2
times, and what is zero is found deposits. It credited the FI-02 inquiry role and the FI-03 trail to PR #494; they landed in PR #489, which
`a4ca9a5` already contains (`git merge-base --is-ancestor 46ec000 a4ca9a5`), so the suite was written with them. The single `agon_harness`
verdict reported earlier is one of several: the harness is unseeded.

**What remains Jordan's.** Nothing above is a design ruling; each states what the code does. These stay open and are his:
- the remediation's forks **JQ-1..JQ-6** (`proposals/2026-10-21-v9-remediation/`, part 04): how much of a person is the draw; whether
  "pool only" reaches combat and mass battle ("materially different games"); the four character-change magnitudes; weight → troop value;
  whether to ratify the two RB-3 designs (IN-46, IN-47; remediation-04:77); the hunger ratio;
- the verbs proposal's **D-V1..D-V21** (part 04 "Items for Jordan"), among them D-V6 (a contents-aware value term) and D-V7 (whether `dispatch` is renamed; verbs-04:152);
- **J-C-2** (whether a levy costs population), **J-T1, J-T2, J-T4** (persons; J-T3 is answered for the template, verbs-01:341), **SM-15** (when the social-contest kernel retires);
- the two open `needs_jordan` rows the tutorials cite: **ED-IN-0296** (`registers/editorial_ledger_in.jsonl:72-73`; the decision-surface ask: question aggregation and stance polarity, cohort pursuit vectors, the own-act screen and tier 1) and
  **ED-IN-0297** (`:74`; where a works comes from in computed play, the producer behind R-F9).

**Defaults already taken, which he may correct** (not open questions): the code's own `[ASSUMPTION; ...; Jordan to correct]` readings the suite quotes,
among them the two ending rows' reading of GD-1 and of "become a theocracy" (`rosters.yaml:2531-2553`), the territory refusal for `seize`, `tend`'s full mend
and the estimate window (H-224). Retiring file 12 (the first-draft appendices) is not a Jordan question: it is a delete plus a `FORK:` row
(`CLAUDE.md` §2), not done here.

Every LACKS row in `research/game_precedent_suite/dispositions/` is reference: it shows what a precedent buys or costs and decides nothing.
