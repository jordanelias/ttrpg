# Digest auditB1
## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Scope: 29 files under `.audit/` (archived-not-canon, lesser weight). Verified-at-tree notes use `systems/social_contest/sim/contest/` (the contest kernel moved there from the `sim/personal/contest/` path the audits cite) and one-grep checks. Text in these JSON files is mojibake (UTF-8 read as cp1252); quotes below are normalised.

### .audit/2026-07-01-contest-gate-a-packet/verdict_log.json
- **What it is:** adjudication log of a 5-round panel review of "Gate A" (the social-contest CR1/CR2/CR3 fold-in: three trackers Concentration/Face/Persuasion, Composure retired, ED-1055/1056), 2026-07-01; array of rounds, each with verdicts (claim/ruling/severity/reason/spawns_ed), `open_decisions`, `escalate`.
- **Status:** none (JSON log). Reading: historical (a pre-merge review of an uncommitted worktree diff); the process (agonist, panel, judge rulings) is dead, the findings are leads.
- **Bears on:** SC, DICE, PROCESS.
- **Content that matters:**
  - R1:9-16 `ci_co_file_checker.py` Rule 1 and `validate_ed_citations.py` OPEN_AS_BASIS failed on the draft (provisional ED-1055 cited as basis, 4 violations); local green was false because `origin/main...HEAD` diffs nothing uncommitted. A reusable method note: a pre-commit "all rules satisfied" is not CI-green.
  - R1:27-37 `Face` was defined two ways: params `Face = Charisma x3 (3-21)` strain buffer consumed downward (Rattled) vs kernel `Face = Standing` (0-10, START 5, built upward by ethos). R2:123-127 adds that the SIGNS are opposite; R2:109-113 adds a third meaning (split-standing: `_Side.face` returns Credit). Carried to Jordan as "Face scale-binding" in R3-R5 (:186, :241, :274), options (a) rescale surface onto Standing, (b) the reverse, (c) two coupled sub-tracks.
  - R1:34 and R4:200 / R5:254: `face_tracker` is WIRED only because the underlying Standing is live; no `.strip(` call anywhere in the kernel at audit time (monotonic-up); `TRACKERS` dict has zero resolution consumers (R1:41); WIRED vs PARTIAL taxonomy in `wrapper.py` `MECHANICS` is a labelling call (overruled as defect at R4/R5).
  - R2:98 SHA-pin finding: four `social_debate` `canonical_sha` pins were raw CRLF-byte hashes, not `git hash-object` OIDs, and an unmodified file's correct pin was overwritten; `freshness_gate.py:37-38` docstring claimed raw bytes equal the blob OID (false on CRLF checkouts).
  - R3:163-166 `social_contest_v30_index.md` Line/token columns went stale after ~140 lines inserted into the main doc (index said Section 8 @293, actual @435); `ci_co_file_checker.py` never checks the `_index` pair.
  - R4:204-208: ED-1055 is the CR1/CR2/D0-3 substrate ED, ED-1056 the CR3/Face ED; the prose cited ED-1055 alone on CR3 rows (social_contest_v30.md 196,437,441,484,605; params/contest.md 104,109,115,118,121,218).
- **Conflicts / stale:** the `sim/personal/contest/` and `designs/` paths are gone (now `systems/social_contest/sim/contest/`). At the tree `resolver.py` no longer imports Face/TRACKERS/RETIRED_TRACKERS (grep: no hit in resolver.py), `wrapper.py:26` still imports `Face ... TRACKERS, RETIRED_TRACKERS` (it uses them in `_SYMBOLS`/MECHANICS; the earlier "unused RETIRED_TRACKERS" nit not re-checked). `primitives.py:33` still has `STRIP = 0.8`, `primitives.py:108` `Face = Standing`, so the scale-binding fork is [UNVERIFIED] as ruled; `resolver.py:433` now strips standing-bounded points (Gate C fix).
- **Open items:** Face scale-binding (a/b/c); Composure-retirement blast radius (scoped to the contest tracker vs corpus-wide rename: knots_v30 s4.2 "Knot-as-Composure-buffer", combat, conviction); whether provisional EDs may be cited as basis; Stage-3 downward Face channel (R3:181 asks the params "Face and Rattled" block be tagged UNREACHABLE until wired); a kernel check that binds Face through a resolution outcome (R4:236).

### .audit/2026-07-01-contest-gate-b-packet/verdict_log.json
- **What it is:** 4-round panel adjudication of "Gate B" (Stage-2 typed dictionaries: styles, venues/proceedings, adjudicators, faction boosts; Panel/ED-137 closure; Terminal Doubt ED-1060), 2026-07-01.
- **Status:** none. Reading: historical; many findings fixed at the tree (below), the design forks are carried by later ED rows.
- **Bears on:** SC, FA (faction boosts), DICE.
- **Content that matters:**
  - R1:9 The ED-1057 Panel simple-majority aggregation was justified by a fabricated precedent ("matches s10 BG parliamentary vote and s7.2 Succession plain-majority"); s10 is a Mandate-weighted dice pool and s7.2 is seven heterogeneous rules; the same sentence was copied to dictionaries.py, params/contest.md, social_contest_v30.md, ED-1057. Fork left: simple majority vs weighted-by-standing vs unanimity (R1:43).
  - R1:13-17 / R2:62: a prebuilt `contract.Panel` passed to `build_contest` skipped the VoteAtClose closure (adj_type never set); and no canonical proceeding routed to Panel at all (dead mechanic, ED-1059). Tree: `wrapper.py:165-166` now sets `adj_type = "panel"` only when `adj_type is None`; `dictionaries.py:380` says Panel is reachable via Guild Arbitration (FIXED).
  - R2:66-70 Obscuring Styles (Suppression, Insinuation) strictly dominated by Precedent/Vision in single-exchange proceedings (Doubt Marker EV 0 with no next exchange; casual_dispute and personal_appeal are always (1,1)); ED-1060 "Terminal Doubt" is the fix. R3:113-117 found the fix's wording self-contradictory (-2 "in the marked side's favour" vs "toward the Obscuring winner"); R4:168-172 found it defined only for PersuasionTrack bands, not for TallyAtClose (casual_dispute always, personal_appeal default).
  - R3:127-131 and R4:175-179: Guilds boost carried the literal "GM picks" into a typed dict (No-GM violation). Tree FIXED: `dictionaries.py:427-436` "Context (venue-derived)" under ED-1061.
  - R1:20 / R3:120-124 four of eight venues collapse into two pairs (Royal Audience = Guild Arbitration, Casual Dispute = Personal Appeal) because `resistance_modifier` and `role_structure` are metadata-only; deferred to the ED-1055..1079 `contest_rebuild` block. `modes.py:59-61` shows Church Tribunal's start_ground has since been changed QUALITY -> FACT.
  - Flavor-honesty defects (Lens 6): Formal Contest says "vote" (R1:34), Royal Audience says "bench" for a single judge (R2:52), Private Negotiation invents a mutual-consent tracker (R3:140), Church Tribunal "room" and "meant to stick" (R3:147, R4:189), POV-locked flavor (R4:182), no venue flavor verb-first though ED-1058 claims it (R4:196).
  - R2:94-98 three different "default panel size" literals (resolver `VoteAtClose` jurors=7, `PANEL_DEFAULT_JURORS`=5, groundup presets 7); R2:80 ED-1057's ledger text names `PANEL_VOTE_SHARPNESS/NOISE` that exist nowhere.
- **Conflicts / stale:** tree `dictionaries.py:528-557` shows the vote/bench/panel wording guards were added; the Guild Arbitration flavor now deliberately names the bench (ED-1057 weighted ballot), so the audit's "Panel simple majority" description is stale: the tree has a bench-weighted majority (`dictionaries.py:380` "bench-weight = Adjudicator.discipline").
- **Open items:** Panel aggregation rule (ruled in code but a Jordan call at the time); Panel reachability (a/b); Terminal Doubt under TallyAtClose; `Terminal Doubt` term not in glossary/mechanical_terms_index (R3:134); Venue flavor voice.

### .audit/2026-07-01-scene-combat-track2-decision-prep/wp_reach_authority_measurement.py
- **What it is:** a 47-line measurement script printing `weapon_physics.reach()/authority()` beside live `systems.reach_base` and `core.heft_resp` for 12 weapons (Track-2 decision prep for the old scene-combat engine).
- **Status:** no Status line (code). Reading: historical; the imported paths do not exist.
- **Bears on:** PC.
- **Content that matters:**
  - :10 `sys.path.insert(... '../../scene/combat_engine_v1')` - a path of the pre-restructure tree; `import config, core, systems, weapon_physics, weapons`.
  - :1-5 the docstring states `WP.reach()`/`WP.authority()` were `[BUILD-ONLY/DIAGNOSTIC]` with zero live callers; the script exists to show where those diagnostics diverge from the live reach and from `core.damage`'s impact inputs.
  - :38-41 for an edged weapon the live analogue of authority is `core.heft_resp`, not `percussion_authority` (0 for non-blunt heads); the table column was added so the comparison is not misread as apples to apples.
  - ROSTER (:16) 12 weapons including `longsword_halfsword` and `paired_short`.
- **Conflicts / stale:** cannot run as written (`../../scene/combat_engine_v1` absent; `systems/combat/combat_engine_v1` exists and `modules/combat` is the live head). `[UNVERIFIED]` whether `weapon_physics.reach/authority` survive: one grep for `def reach`/`def authority` under systems/combat and modules/combat returned nothing.
- **Open items:** the Jordan-gated "WP.reach/authority vs reach_base/wield_heft" single-source residual, if still wanted.

### .audit/2026-07-01-scene-combat-track2-decision-prep/wt_spd_deleak_measurement.py
- **What it is:** 203-line harness measuring the roster-wide delta if the legacy hand-authored `wt`/`spd` weapon fields were replaced by derived `weapon_physics` quantities (A: damage-path heft via `wield_heft` formula; B: tempo path via `1/recoverability_factor`), no live code touched.
- **Status:** no Status line (code). Reading: historical decision-prep.
- **Bears on:** PC.
- **Content that matters:**
  - :12-19 `core.heft_resp` anchors on binary `wt` with a continuous refinement (`HEFT_MODE='continuous'`); candidate reuses `wield_heft`'s exact formula `(I_g/REC_I_REF)**WIELD_HEFT_EXP`; inert for blunt heads (their heft comes from percussion authority, core.py:144).
  - :21-30 tempo path currently reads `w['spd']` (a bare constant, -0.5..3.0) times `SPEED_K`; v2 candidate uses `recoverability_factor` at grip 0, lunge 0.
  - :34-37 the script itself reports corr(spd, 1/recoverability_factor)=0.878 vs corr(spd, point_concentration)=0.359 (printed by `corr_table`; not re-run here), i.e. the hand-tuned `spd` constants already approximate the recoverability physics.
  - :37-42 explicit caveat: `weapon_tempo`'s `pen` term already penalises weight and hands through `wield_heft`, so a naive swap double-counts weight and hands; the script reports without de-duplicating.
  - :98 comment `ED-PC-0036: close= retired from core.damage` - the file was edited after the ED, so the script ran on the later engine.
- **Conflicts / stale:** same dead sys.path (:47) as above. [UNVERIFIED] whether `wt`/`spd` have since been de-leaked; not grepped.
- **Open items:** the double-counting decomposition (named as design judgment, unresolved); the `wt`/`spd` de-leak ruling.

### .audit/2026-07-02-contest-gate-c-packet/GATE_C_packet_raw.json
- **What it is:** raw capture of the Gate C (Stage-3: CR4 stasis-genre +1D, CR5 self-Face backfire, adjudicator armature, appraise) review packet in JSON sections (headline, CR4/CR5 grounding, armature table, four-lens checker board, contest log, open decisions, files touched, residuals), 2026-07-02; the content is wrapped in a code fence.
- **Status:** none; the headline says "CONVERGED (Round 4 closure)". Reading: historical; the packet stages work that is now in the tree.
- **Bears on:** SC, DICE, CHAR (adjudicator conviction/armature).
- **Content that matters:**
  - Section "THE ARMATURE" (:14): `STYLE_AXIS` 4x4: Precedent->Evidence, Vision->Consequence, Suppression->Authority, Insinuation->Insinuation; primary weight 1.0, off-axis 0.15; `style_axis_alignment` = dot product (range 0-4) mapped through `ARMATURE_MAX_DSIGMA = 0.50 sigma` (`level("moderate")`) to a mu-shift on `net_boost`; off-axis 0.075 sigma. Tree: `armature.py:229,336` confirm.
  - :10 CR4 realised as `primary_genre_pool_bonus(orator_genre, live_ground)` keyed on the chosen Style's genre; CR5 as `cr5_self_backfire(style, landed, my_standing)` = `min(CR5_BACKFIRE_MAGNITUDE, own Face)`; both called from `resolver._reception/_apply` (resolver.py:368/390 as cited; line numbers will have drifted).
  - :22 contest log: 39 findings over 4 rounds, all upheld (one deferred), 11+ FIXED; 377 kernel tests / 1041 pytest at close.
  - :26 eight open decisions: STYLE_AXIS magnitudes; 4th axis Insinuation vs canonical Solidarity (npc_behavior_v30 s1.3 head lines 32-42); Appraise-reveal PARTIAL; epideictic compression 3->2 genres; CR5 specifics (opponent-Face half deferred, -2 on a 0-10 stat vs a track margin, standing-scaling); backfire trigger (deg==0 is a low roll, not a modelled foul / FaultState); CR4 chosen-genre confirm; CR4 Memory-branch unreachable (all proceedings start QUALITY).
  - :30 file list is a Windows worktree (`C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d`), HEAD f374b816, nothing committed: the work arrived by later commits.
- **Conflicts / stale:** the doc says `genre_of_style` maps Suppression->Memory/Insinuation->Projection in one place and Authority/Insinuation in another (final_build_summary :13 vs here :14); `rhetoric.py:209` is the owner. `modes.py:59-61` shows the Memory-branch reachability gap was addressed by starting Church Tribunal at FACT.
- **Open items:** all eight above unless closed by later EDs (ED-1062 allocation noted as pending).

### .audit/2026-07-02-contest-gate-c-packet/final_build_summary.md
- **What it is:** 41-line close summary of the Gate C build (three judge-upheld findings fixed).
- **Status:** none; reading: historical.
- **Bears on:** SC, DICE.
- **Content that matters:**
  - :13 Finding 1: CR4 +1D was tautological because `Stasis.relevant` forces `move.ground == live`; fix keys on `genre_of_style` and makes CR4 armature-gated (no chosen Style, no bonus), restoring golden-trace parity on the `armature=None` path.
  - :15 Finding 4: `cr5_self_backfire` had no standing parameter; fix passes mover Face, capped `min(2, Face)`.
  - :17 Finding 5: `roll_net` does `max(1,int(round(pool)))`, so an off-axis 0.15 bonus rounded away (flat == misaligned byte-identically); moved to the continuous delta-sigma mu-shift channel on `net_boost`; old `ARMATURE_MAX_POOL_BONUS`/`style_axis_pool_bonus` deleted. An instance of a sub-1 fractional-pool quantisation hazard (cf. `resolution-diagnostic` skill).
  - :9 test counts 377 (kernel) and 1041 pytest.
- **Conflicts / stale:** line 1 is a stray orphan sentence ("`mechanics_selftest` green...") with no heading.
- **Open items:** same as the raw packet; ED-1062 ledger entry and id_reservations bump deferred "to the Synthesist".

### .audit/2026-07-02-contest-gate-c-packet/verdict_log.json
- **What it is:** 4-round adjudication log for Gate C (35 verdicts), 2026-07-02.
- **Status:** none; reading: historical, fixes largely in the tree.
- **Bears on:** SC, DICE, CHAR.
- **Content that matters:**
  - R1:5-9, R2:111-115: CR4 genre-primary was a dead/tautological lookup marked WIRED; `mechanics_selftest` asserts only symbol resolvability so WIRED was hollow (a recurring pattern across all three gates).
  - R1:33-37: two armature formulations shipped (subtractive `armature_resistance`, WIRED but never called; multiplicative `resonance_uplift`, uncited 0.35). Deleted in later rounds.
  - R2:138-142: `STYLE_AXIS` was cited to an empty stub (`npc_behavior_v30` s1.3); 3 of 4 axes ground at `complete_systems_reference.md:20`, the 4th (Insinuation) is invented, canon's 4th is Solidarity/Loyalty.
  - R2:124-128 `Standing.strip(2.0)` removes 1.6 (STRIP=0.8) so the cited -2 was not what was applied; R2:131-135 and R3:265-269: seeded probe 7/500 licit Suppression moves backfired on `deg==0` with 0/7 fault flags set - the nigrahasthana label outruns the mechanism; engine's `FaultState` machinery exists unused by the backfire.
  - R3:209-213 (blocker): `STASIS_PRIMARY_GENRE[DEFINITION]=Memory` contradicted ratified CR4 ("definitional = reframe via Present-rendering") and reconciliation_map s1.2; routing genre via `Stasis.tense` was forbidden by that map.
  - R3:272-276 `appraise_armature` has no resolver/wrapper call site (the reveal is not player-triggerable; Stage 6). Tree: `agon_harness.py:35-58` now describes it, `grep` shows no resolver call still.
  - R4:310-313, 338-342 rejected "chosen-genre" tautology and the 0.15 inert off-axis (800 seeds: flat and misaligned both {b:401,a:399}).
- **Conflicts / stale:** armature citations flip between "s6.1 empty / s6.3 populated" - the file itself records the inversion (R3:244-248). References `designs/architecture/complete_systems_reference.md`, now `.designs/`.
- **Open items:** the open_decisions lists R1:98-104, R2:196-203, R3:295-302, R4:374-382 (same eight items); CR5-supersedes-Doubt-Marker vs Gate-B-keeps-and-extends (R1:19-24, R3:251-255).

### .audit/2026-07-02-mass-battle-movement-pathing-audit/findings_full.json
- **What it is:** one JSON object (632 lines): a Sonnet-agonist diagnosis of mass-battle movement/pathing (H4 envelopment wings "just go straight at the enemy"), each finding re-verified by an independent verifier ("verified" array), then a synthesis, an 8-step fix plan and sequencing; 2026-07-02, against the then `tests/sim/mass_battle/` package (now `modules/mass_battle/` + `systems/mass_battle/sim/`).
- **Status:** none (`usedFallback:false`). Reading: historical but UNUSUALLY WELL-INSTRUMENTED; most findings are now fixed at the tree (below). Treat as the best map of how mass-battle movement was probed.
- **Bears on:** MB (primary), CORE (golden/digest discipline), CHAR (roles/instructions).
- **Content that matters:**
  - Root cause (:8-23, :415): after ED-1089 flipped `FIELD_MOVEMENT`/`PC_NODE_COHESION` ON, `advance_cells` early-returns (units.py:719-720) to `_node_advance`, a pure centroid attractor that never reads `instructions`/`role`; envelop, sweep, overhang-wheel and kite all lived in the legacy grid branch below it and were unreachable by default. Method: toggle each flag on/off and compare outputs byte-for-byte (identical = dead arm); run the same scenario on both paths.
  - :28-38 (critical) `reset_positions` is a positional no-op on the node path, so multi-turn battles weld at the turn-1 contact line for turns 2-8 (126 of 144 ticks static); golden field digests (`bat.py` unit_field/cell_field) embed that behaviour. Verifier :228 reproduced with a micro-probe (shift `_node_pos`, call reset, nothing moves).
  - :41-52 (critical) ED-1093 "mounted archers fly by and use range" was ineffective: implicit role "Kite" never sets `unit_type='ranged'` (ROLE_SPEC carries only shape+instructions), so no volley (orchestration gate), no kite branch, speed multiplier PER_CELL-gated, and no `TROOP_TYPE_STATS` preset. Lesson recorded: a ruling "verified by construction-inspection, not by running the behaviour".
  - :66-74 envelop/sweep acceptance validators pin PER_CELL but not the field toggles, so since ED-1089 they measure the dead arm (on == off, 4.2125 rows in front) and run in no CI; verifier :291 grep found them wired nowhere.
  - :77-85 `check_drift` re-keys `cell_troops` but not `_node_pos/_node_rel` (verified: 10 of 25 Arrowhead cells at (0,0), then permanently stacked at the anchor after one advance); reachable via `discipline_check_phase` -> `degrade_discipline`.
  - :111-117 / verifier :370 field anchor step is L1-normalised (`mag=|dr|+|dc|`) so diagonal speed is 0.707x (29% slower); 12 of 15 ROLE_SPEC instruction tokens have no consumer (corrected from the original "10 of 14", :389); `build_army` silently drops unknown spec keys (`speed:'Fast'` has no home: Subunit has no speed field); `tick:N` orders fire once per battle because `_order_idx` never re-arms (counterfactual re-arm gave 8 fires).
  - :141 the "144-tick freeze" report was REFUTED (does not reproduce at HEAD or 3 prior commits); best-fit cause was reading a cell's immutable pattern `id` instead of live `pos`. :142 architecture assessment: one new primitive (ordered goal-function + completion-predicate list consumed ahead of the centroid fallback) plus repairs; clearance/rear-offset magnitudes must derive from existing quantities (`standoff_from_reach`, `COL_WIDTH`, the legacy "+2 frontage margin"), `TROOP_TYPE_REACH` stays empty.
- **Conflicts / stale:** Tree check (one grep each): `modules/mass_battle/config.py:342` `PER_CELL` now defaults `'1'` (ED-MB-0001, "yes, all options/modules must be turned on") - the PER_CELL finding is FIXED; `hierarchy/units.py:74-76` lists `_resolve_maneuver_goal -> _envelop_goal/_sweep_goal/_kite_goal` and `:279` a `route` of absolute waypoints with `_route_idx` (ED-MB-0067) - the waypoint primitive EXISTS; `orchestration.py:1953-1959` `reset_positions` docstring says node-path atoms are now explicitly SKIPPED (movement audit finding 1.1 / ED-1096), `units.py:1154` has a node-state re-key (check_drift fix). `config.py:599,623` still comments "Kite blocked on the kiting primitive (gap)" next to `Kite` role without a `unit_type` hit by grep (`unit_type` not in config.py ROLE_SPEC row) [UNVERIFIED that the ED-1093 data half is closed]. The "MB_NODE_COHESION" name replaced `PC_NODE_COHESION`.
- **Open items:** Jordan rulings requested and (per tree) mostly answered by code: multi-turn re-arm semantics (do stance/orders reset each engagement turn?), where `unit_type='ranged'` lives, transit facing policy (WHEEL conflates steering and facing target; the lerp-normalize facing update stalls at exactly anti-parallel facing, untested for reachability), L1->L2 step normalisation (deferred "only on evidence"), the platform-dependent RNG desync in the 'cell' grid digest (`test_mass_battle_byte_exact.py:32-50`) [UNVERIFIED still open].

### .audit/2026-07-02-morphology-rearch-phase0/phase0_report.md
- **What it is:** 118-line harmonisation report on 53 weapon part-decompositions (1 canonical roster of 12 + 8 cluster batches) feeding a "morphology re-architecture" of the combat engine's weapon geometry; 2026-07-02.
- **Status:** none. Reading: historical; its output (per-element `x_m / mass / extent_m / orient_deg / material` records) is what `modules/combat/weapons.py` now holds.
- **Bears on:** PC (weapon physics, `weapon_physics.derive`), CHAR (equipment).
- **Content that matters:**
  - :10-20 per-cluster confidence table: strongest are bear_spear, bardiche, cinquedea, bec_de_corbin, lucerne_hammer (specimen-anchored); weakest-grounded weapon in the whole 53 is `hook_sword` (S3, single antique-dealer specimen scaled by length ratio, no treatise), then `voulge`, `goedendag`, `glaive`, `sparr_axe` (:44-57).
  - :24-38 seven flags; the substantive ones: `hook_sword` crescent guard is listed in BOTH `head_elements` and `guards[]` with shared mass (:36), "the single item most likely to bite a downstream consumer that naively sums both lists"; `goedendag` club body is a zero-mass placeholder element with mass folded into the haft (:28); the five Japanese/Chinese long swords reported `residual_pct` with the wrong sign (corrected in the combined file).
  - :61-101 mass-budget table: all 53 residuals within +/-10%; pulwar -9.47 and shamshir -9.41 nearest the ceiling; residuals were deliberately NOT squeezed (:101).
  - :105-110 cross-cluster comparability claims (sabre family 0.85-1.3 kg / 0.78-0.87 m blades; poleaxe/bec_de_corbin/lucerne_hammer share a 1.8 m, 50/50 centre-grip haft).
  - :116-117 FORMS: `longsword_halfsword` and `estoc_halfsword` are the same part-set with a shifted working-hand origin (`origin_shift_m=0.75` for estoc); ADORNMENTS: only 3 survive (ranseur tassel S3, guandao tassel S2, jian tassel S2), flagged non-combat.
- **Conflicts / stale:** Tree check: `modules/combat/weapons.py:25` documents `PARTS elements=[{x_m, mass_kg, extent_m, orient_deg, material, [edge_undulation]}]`, `:59` says edge_undulation is used by exactly one weapon (flamberge), `:686` carries amplitude 15 / period 90, `:803` has `hook_sword`: the Phase-0 output is landed. The report calls the part-set "53 weapons"; the roster size at the tree [UNVERIFIED].
- **Open items:** the hook_sword dual-record question (does the engine sum both lists?) [UNVERIFIED whether `weapon_physics._head_elements` (:148) guards it]; flamberge wave amplitude/period remain an S3 bracket.

### .audit/2026-07-02-morphology-rearch-phase0/cluster_dagger_and_hook_A.json
- **What it is:** Phase-0 part decomposition of 5 weapons (rondel, main_gauche, stiletto, misericorde, hook_sword): per element position, mass, extent, material, geom_notes, citations, confidence tier.
- **Status:** none. Reading: historical input to the combined file.
- **Bears on:** PC.
- **Content that matters:**
  - Each record is `{total_length_m, total_mass_kg, mass_grade, head_elements[], guards[], haft_or_grip, pommel_or_butt, adornments, mass_budget, provenance}`; all five close to 0.0% residual because the blade mass is the RESIDUAL (total minus guard/pommel/grip estimates), e.g. rondel :45-51, hook_sword :307-315. A closed budget therefore carries no evidential weight for the blade figure.
  - main_gauche :63-134 guard complex 0.16 kg + ring 0.02 = 0.18 of 0.55 kg total; quillon `extent_m` is the half-span (0.14) "matching the catch surface's physical span" (:88).
  - hook_sword :256-328 `crescent_hand_guard_striking_element` 0.14 kg listed in `head_elements` AND `guards`, counted once (:309-310); record-level `mass_grade` is "S2" (:259) while provenance `confidence_tier` is "S3" (:325): the two fields disagree for the same weapon.
  - rondel/misericorde/stiletto engine blade lengths (0.24/0.30/0.27 m) sit at the short end of the cited specimen ranges (:15, :208, :147); chosen to match the engine's head_len, i.e. the engine value drove the record and the specimen is a typology anchor (stated :15).
- **Conflicts / stale:** the hook_sword S2/S3 mismatch above. Cited `weapons.py` is the old `designs/scene/combat_engine_v1/` path.
- **Open items:** crescent dual-record handling for Phase B.

### .audit/2026-07-02-morphology-rearch-phase0/cluster_existing_roster.json
- **What it is:** decomposition of the canonical 12 (rapier, arming, longsword, greatsword, sabre, dagger, paired_short, spear, staff, mace, poleaxe, longsword_halfsword); the schema used as the harmonisation target.
- **Status:** none. Reading: historical.
- **Bears on:** PC.
- **Content that matters:**
  - Uses an older field naming (`pommel{mass_kg_est,x_m}`, `butt{...}`, `mass_budget.sum_est_kg`) than the 8 later clusters (`pommel_or_butt`, `computed_total_kg`): the combined file had to reconcile two schemas (phase0 report :12).
  - Residuals are non-zero here, unlike the residual-split clusters: rapier +5.23% (:55), dagger -8.67% (:374), poleaxe +3.32% (:699), greatsword +1.89%.
  - :38-44 rapier pommel 0.348 kg and swept-hilt guard 0.30 kg are canon anchors from `weapons.py` ("already the calibrated canonical pommel mass"), against a specimen total of 1.01 kg; pommel at 27% of weapon mass is a calibration artefact, not a specimen fact.
  - :503-553 staff haft diameter 0.040 m is "back-solved" from the staff's own mass, so using it to verify the staff mass is circular (stated :552).
  - :711-775 longsword_halfsword: same 1.4 kg partitioned across a 0.42 m origin shift; blade split 0.435 fore / 0.435 aft; the "grip" is steel.
- **Conflicts / stale:** sabre `curvature=0.42` is marked `[NO SPECIMEN DATA] LOW-CONF` by the engine itself (:270).
- **Open items:** none beyond the flags in the report.

### .audit/2026-07-02-morphology-rearch-phase0/cluster_polearm_choppers_A.json
- **What it is:** 5 polearms (podao, fauchard, bardiche, sparr_axe, voulge) decomposed into blade/hook/langet elements plus full-length haft.
- **Status:** none. Reading: historical.
- **Bears on:** PC, MB (polearm troop equipment).
- **Content that matters:**
  - :37 a method defect found and fixed: using only the 0.33 m grip segment as shaft mass gave a -36.9% residual; the correct convention is `shaft_grip_estimate_kg` sized to the FULL `total_length_m` ("this cluster's hafted-tip weapons need the shaft sized to total_length_m, not grip_len_m alone" - a Phase-B modelling note).
  - bardiche S1 (:107-164): one extended crescent element (1.75 kg, 1.476 m) modelled as ONE element with a 0.06 kg "lower_socket_langet" guard realising the two-point mount; 1.8 m total vs specimens of 1.38-2.3 m.
  - voulge S3 (:212-276) and sparr_axe S3 (:166-211): no treatise/specimen; mass interpolated. voulge key is `voulege` in weapons.py (:273 display name corrected).
  - fauchard back hook (:66-74) is attested only for the "composite glaive" variant.
- **Conflicts / stale:** `mass_grade` is "S2" on voulge and sparr_axe records while `confidence_tier` is "S3" (:215/:275, :169/:209): same pattern as hook_sword.
- **Open items:** none.

### .audit/2026-07-02-morphology-rearch-phase0/cluster_polearm_hooks_hammers_A.json
- **What it is:** 5 polearms (guisarme, ji, bec_de_corbin, lucerne_hammer, goedendag), 341 lines.
- **Status:** none. Reading: historical.
- **Bears on:** PC, MB.
- **Content that matters:**
  - bec_de_corbin and lucerne_hammer are poleaxe siblings (1.8 m, 3.0u/3.0u centre grip, 0.040 m haft); the handling research flags that rondel/langet protection is attested for bec_de_corbin but NOT lucerne_hammer (:257): "the one guard field where the two poleaxe siblings should NOT match".
  - :274 Met Lucerne Hammer (accession 26670) length is internally inconsistent in the source: 94 1/8 in = 239.1 cm vs a 139.2 cm summary figure (and the grip note at :220 uses 1.392 m); the record keeps the engine's 1.80 m and downgrades length to S2. An unresolved unit conflict.
  - goedendag (:284-337): the club body is a zero-mass placeholder element (mass folded into `shaft_estimate_kg` 1.336), 0.46 kg iron spike; `grip_choke_max=0.0` (not re-grippable, :315).
  - ji (:59-126): spearhead + perpendicular crescent; crescent counted once (guards entry mass 0.0).
- **Conflicts / stale:** bec_de_corbin Met specimen 3.40 kg / 202.9 cm vs engine 2.4 kg / 1.80 m (:131), kept as "typology variance".
- **Open items:** re-verify the Lucerne Hammer length against the Met page.

### .audit/2026-07-02-morphology-rearch-phase0/cluster_polearm_multi_and_blade_A.json
- **What it is:** 5 polearms (spetum, partisan, naginata, glaive, guandao), 298 lines.
- **Status:** none. Reading: historical.
- **Bears on:** PC, MB.
- **Content that matters:**
  - Mass budgets are tuned "by adjusting shaft-length assumptions and head-element proportions within specimen-plausible bounds; no total_mass_kg was altered" (:297) - residuals spetum -5.3, partisan -1.2, naginata -3.6, glaive -3.2, guandao 0.0.
  - glaive (:182-222) is explicitly "family analogy to the naginata (matched total length and head/grip split, discriminated by mass and curvature only)" - curvature 0.22 vs naginata 0.50.
  - guandao (:223-295) 3.8 kg S1 anchored on a mid-19th-c. Royal Armouries piece (253 cm/99 cm blade); apocryphal 18-48 kg "Guan Yu" and 48-83 kg wuju lift implements are explicitly excluded as non-combat. Tassel adornment attested S2.
  - spetum anchored on a folding ceremonial specimen (1.5 kg, 234.5 cm), mass raised to 1.9 kg (:58); partisan S1 on Saint Louis Art Museum 32556 (2.454 m, 2.8 kg) with engine 2.6 kg / 2.301 m.
  - naginata is tanged, not socketed (:161) - a construction difference from the European heads.
- **Conflicts / stale:** guard entries with `mass_kg_est:0.0` cross-reference head elements (partisan :104-114) - the same dual-listing pattern as hook_sword, but flagged only for hook_sword.
- **Open items:** revisit glaive first if a specimen surfaces.

### .audit/2026-07-02-morphology-rearch-phase0/cluster_polearm_spears_A.json
- **What it is:** 5 spear-family records (yari, kama_yari, dangpa, bear_spear, ranseur), 371 lines.
- **Status:** none. Reading: historical.
- **Bears on:** PC, MB.
- **Content that matters:**
  - Method (:370): `shaft_mass = pi*(haft_d/2)^2 * total_length_m * 700` (RHO_WOOD), `head_residual = total - shaft`, split across elements; residuals <=0.15%. So the head mass is DERIVED from the engine's total, the sub-element split an S3 apportionment (no source weighs a jumonji-yari's side blades or dangpa's flank tines).
  - bear_spear S1 (2.35 kg / 2.05 m) vs Royal Armouries 1.861 m / 2.27 kg; crossbar lug is both penetration-stop and a documented combative parry surface (Phoebus, Talhoffer, Mair).
  - ranseur: wing-lugs are `guards` with mass 0.087 each, one S3 ceremonial tassel; Grokipedia's ~4 kg figure is rejected as an outlier vs the 1.4-2.3 kg band (:359).
  - yari 1.23 kg (a su-yari, not the 2.49 m nagae-yari pike at 2.15 kg, :56); dangpa centre prong deliberately longer than flanking tines (Muyedobotongji).
- **Conflicts / stale:** ranseur haft note (:329) contains a garbled sentence ("0.032->but ranseur listed 0.036"); a transcription slip, no number affected.
- **Open items:** none.

### .audit/2026-07-02-morphology-rearch-phase0/cluster_sword_curved_world_sabres_A.json
- **What it is:** 5 swords (nandao, jian, scimitar, pulwar, shamshir), 332 lines.
- **Status:** none. Reading: historical.
- **Bears on:** PC.
- **Content that matters:**
  - Residuals all negative, -4.62 to -9.47%, attributed to unmodelled rivets/wire/fuller removal (:331); pulwar -9.47 and shamshir -9.41 are tightest.
  - The curved-cutter ladder is preserved: curvature shamshir 0.70 > pulwar 0.60 > scimitar 0.55; edge_keenness shamshir 0.95 > pulwar/scimitar 0.90; centroid fraction scimitar 45% > nandao = jian 44% > pulwar 43% > shamshir 41% (:331). These are engine primitives, not specimen facts.
  - scimitar 1.0 kg is "trimmed below the single cited specimen (1.21 kg kilij, 79.5 cm)" to seat the cross-cluster ladder (:194): the engine value overrode the specimen.
  - pulwar hilt ergonomics (Hutton 1897/98) suppress thrust: a documented-ergonomics claim used for `haft_or_grip` notes (:233, :259).
  - nandao is a 20th-c. IWUF sport invention graded S2/S3; the record uses the heavier 0.87 m / 1.3 kg combat-typology anchor rather than the 445-500 g competition prop (:60).
- **Conflicts / stale:** none verified.
- **Open items:** none.

### .audit/2026-07-02-morphology-rearch-phase0/cluster_sword_japanese_chinese_long_A.json
- **What it is:** 5 swords (katana, tachi, odachi, tsurugi, changdao), 321 lines.
- **Status:** none. Reading: historical.
- **Bears on:** PC.
- **Content that matters:**
  - `mass_budget.residual_pct` is reported POSITIVE (6.8, 7.9, 5.7, 6.9, 7.8; :54, :117, :181, :244, :307) although every part-sum is below total: the sign bug flagged in the report (:38 of report). Magnitudes are right, direction wrong.
  - odachi 2.2 kg / 120 cm is interpolated; Atsuta Shrine (221.5 cm, 4.5 kg) and Norimitsu (14.5 kg) are excluded as votive outliers (:134, :186-187).
  - tsurugi 0.65 kg is "rounded UP" from the 527 g Kofun specimen to represent a combat exemplar (:248); grip rescaled to 20 cm (specimen's 7.5 cm is a scabbard collar).
  - changdao: grip 0.68 m (35% of 1.95 m) from Qi Jiguang (0.40 m handle + 0.33 m bronze extension), the strongest treatise-specified record.
  - tsuba masses are the only S1 component data (Met 71-136 g, rounded to 100 g).
- **Conflicts / stale:** the sign bug (corrected downstream per the report).
- **Open items:** none.

### .audit/2026-07-02-morphology-rearch-phase0/cluster_sword_straight_thrust_and_broad_A.json
- **What it is:** 6 swords (szabla, cinquedea, flamberge, estoc, estoc_halfsword, falchion); no top-level grade field per weapon, a schema difference from the other clusters.
- **Status:** none. Reading: historical.
- **Bears on:** PC.
- **Content that matters:**
  - flamberge (:108-189) is three head elements plus Parierhaken guard: forte-to-mid wavy section (`edge_undulation` amplitude 15 mm, period 90 mm, S3 bracket of the 10-20 / 60-120 mm cluster instruction), plain distal tip, dulled ricasso; this is the only weapon with a nonzero `edge_undulation`.
  - estoc_halfsword (:253-314): `origin_shift_m=0.75`, free tip 0.399 m, grip span 1.17 m, pommel at -1.17; "no new mass".
  - cinquedea 0.8 kg (:56-105) but the pommel is 0.23 kg (29%) - the same residual-split artefact as the other small blades; Met specimens 740-907 g bracket the total.
  - szabla pommel 0.21 kg of 0.95 (:36) likewise; cluster note says "All five records" for six weapons (:369).
  - estoc 2.0 kg vs Met 27434 at 1.616 kg/106.9 cm; falchion 1.0 kg vs Thorpe ~0.9 kg.
- **Conflicts / stale:** `modules/combat/weapons.py:686` carries the flamberge blade at 0.8859 kg / 15 / 90 (not 1.05 kg as here): the engine record re-partitioned the masses (a `dict(...)` per element) [UNVERIFIED which is authoritative; the code governs].
- **Open items:** none.

### .audit/2026-07-02-morphology-rearch-phase0/phase0_morphology_combined.json
- **What it is:** 3,894-line concatenation of the nine cluster files into one `{weapons{53}, flags[7], harmonization_notes}` object; each weapon gains `_source_cluster` and a `notes` field that duplicates `provenance.note`; read in full.
- **Status:** none. Reading: historical product of Phase 0; the engine's own `weapons.py` is the live descendant.
- **Bears on:** PC.
- **Content that matters:**
  - Only mechanical changes versus the clusters: `pommel_or_butt` split into `pommel{}`/`butt{}` for the dagger and spear clusters (:3885-3894 harmonization notes), the Japanese/Chinese `residual_pct` signs corrected (katana -6.82, tachi -7.92, odachi -5.68, tsurugi -6.92, changdao -7.81; :2404, :2473, :2543, :2612, :2681), and `shaft_or_grip_est_kg` re-derived for the multi/blade polearms as sum minus parts (:3894).
  - `mass_grade` is missing on the six `sword_straight_thrust_and_broad_A` weapons (szabla, cinquedea, flamberge, estoc, estoc_halfsword, falchion; e.g. :3052-3119) while all others carry it, so a reader keyed on `mass_grade` sees 47 of 53; `total_length_m` is absent on the 12 canonical records (:3-3).
  - `hook_sword` still has `mass_grade:"S2"` (:3803) next to `confidence_tier:"S3"` (:3878); `rondel/main_gauche/stiletto/misericorde/hook_sword` gained an empty `double_count_guard_note` (:3566, :3645, :3716, :3786) populated only for hook_sword (:3868); no other dual-listed record (ji, partisan, kama_yari, dangpa, guandao) carries one.
  - `flamberge` retains amplitude 15 / period 90 (:3202-3203) as the only nonzero `edge_undulation`.
  - :3894 states the part-sets were NOT checked against `weapon_physics.derive()` sums; no 0-1 behavioural scalar was found in mass/x/extent fields.
- **Conflicts / stale:** mojibake throughout (UTF-8 read as cp1252); `provenance.citations` cite `designs/scene/combat_engine_v1/weapons.py`, a deleted path. Counts of 53 not recounted [UNVERIFIED]. The engine's `weapons.py:686` flamberge blade 0.8859 kg differs from the 1.05 kg here.
- **Open items:** hook_sword dual-record decision; whether the engine consumes `guards` or `head_elements` where both list one part.

### .audit/2026-07-02-scene-combat-closing-distance-redesign/audit1_lens_architecture_orphan.json
- **What it is:** one of six parallel "Fable 5" lens audits (2026-07-02) of a PLAN ("R1 circumstance-degradation redesign", increments I1..I8, decisions D1..D10) for personal-combat closing distance, grip/range-aware damage, facing and grappling; this lens checks layering, increment sequencing and orphans. The plan file itself (`C:/Users/Jordan/.claude/plans/...`) is not in the tree.
- **Status:** none; plan was `[PENDING]` its own four-lens fold-in at read time (:7, :220). Reading: historical; the plan has largely landed (tree checks below).
- **Bears on:** PC, CORE (layer discipline L0-L3).
- **Content that matters:**
  - :55 (SERIOUS) I3 (grip-aware, per-beat reach) silently redefines `closed`/`measure_gap` that I4/I5 build on: a dependent chain, not independent increments; re-run the I3 acceptance (polearm-vs-arming out of the 93-96% band) after I5. :90 (SERIOUS) the per-beat `er` recompute must run after `grip_target` and after the half-sword weapon swap or reach reads a stale grip.
  - :197 (SERIOUS) D9 "retire `clinch` OR reduce to a residual bias" leaves an orphan re-entry path; recommended hard disposition: delete the field. :83 I7 over-bundled; split rear_clearance (I7a) from contact.py + hook_affordance (I7b).
  - :69 I1 adds `facing`/`range_avail` Combatant fields several increments before readers exist (I5/I6); recommended a standing anti-orphan test "every Combatant circumstance field has >=1 live reader".
  - :215 half-switch hazard: `agility`, `defense_affinities.lever_norm`, `wield_heft`, `_recovery_mode_commitment` must all read the same grip-adjusted `I_g`.
  - :94-179 orphan table: 12 items VERIFIED consumers, 1 GAP (clinch); layering verdict: plan honours L0 pure (`at_circumstance(w, grip, room)` takes scalars only), wrapper sole mutator, contact.py an L2 module (:231).
- **Conflicts / stale:** Tree check (one grep each, `modules/combat/`): `weapon_physics.py:933` `at_circumstance(w, grip=0.0, room=1.0)` exists and returns `rear_clearance`/`geom_slide`; `weapons.py:17` "`clinch` DELETED, I7b/D9, 2026-07-03" and contact.py:9 forbids re-reading it (FIXED, both the disposition and the split); `wrapper.py:172` "er REFRESH #1 (I3, D3)" - the per-beat refresh exists with longer/shorter labels frozen at engagement start (resolves the S6 ordering ask in the plan's default); `state_graph.py:48-51` now has a `Contact` node. The `omega_cap`/`m_eff` names do not exist in `weapon_physics.py` (the KE formulation of D2 was not adopted as written). Files cited (`designs/scene/combat_engine_v1/`) are now `modules/combat/` + `systems/combat/combat_engine_v1/` (state_graph.py, capabilities.py).
- **Open items:** none outstanding from this lens that a grep can show; whether the standing anti-orphan test (S3) was built [UNVERIFIED].

### .audit/2026-07-02-scene-combat-closing-distance-redesign/audit1_lens_consumer_coupling.json
- **What it is:** second lens: grep-verified call sites of every function each increment touches, hunting half-switch risk; 9 findings (2 BLOCKER, 5 SERIOUS, 2 MINOR).
- **Status:** none. Reading: historical.
- **Bears on:** PC, CORE (test discipline).
- **Content that matters:**
  - :9 (BLOCKER) `core.strike` calls `heft_resp(attacker.w, cfg)`/`WP.percussion_authority(attacker.w)` with the weapon only; grip lives on the Combatant and is already >0 at strike time for closed poles. Threading grip into `heft/percussion_authority` must update `core.strike`, `adef_cap`, `select_mode` (two calls) and `puncture_pressure` ATOMICALLY or damage and armour-defeat disagree on the same blow.
  - :17 (BLOCKER) the plan's "free cascade" through `reach_base` is false: `reach_sigma` reads the frozen `er` dict, `stophit_sigma`/`close_rate` do not call `reach_base`; only `close_unwieldiness` and `slip_inside` read it live. The `er`-freeze (wrapper.py:32-33) must be refreshed in the same commit, with an explicit decision about whether the longer/shorter label may flip (role-thrash).
  - :31 I1's "agility reads at_grip I_g, byte-identical at g=0" is not exact for records where `I_cm = max(0, I0 - m*PoB^2)` clamps (the half-sword shifted-origin forms) or by float round-trip; the 0.40-0.60 mirror band would mask drift: demand exact-float equality before calling an increment identity.
  - :37 `test_combat_heft.py` pins only the longsword anchor (1e-6) and an ordering spear<arming<longsword<greatsword, so a KE re-anchor can silently re-tier every other weapon: add a per-weapon heft snapshot.
  - :72 every `test_combat_*.py` does `pytest.importorskip('numpy')`, so a numpy-less run skips the guards that would catch a half-switch: treat a skipped combat suite as RED.
  - :45 `select_mode` is called at 3 sites and its `closed` argument is never read; `approach_displace` reads native `longer.w['head']`, so wiring it to `sel_head` is a behaviour change on the approach (sel_head is always set), not a fallback.
- **Conflicts / stale:** tree: `combat_systems.py:385` `close_efficacy(pc, measure_gap, range_avail, closed, head)` now exists (the unused `closed` hook was consumed), `:649-694` shows `select_mode` returning `sel_gap/sel_perc/sel_pc` (ED-PC-0037.1), `:441` `range_utilization`, `:430` `facing_target`. The numpy-importorskip hazard (:72) is a standing process hazard [UNVERIFIED still open].
- **Open items:** whether a per-weapon heft snapshot test exists (not grepped).

### .audit/2026-07-02-scene-combat-closing-distance-redesign/audit1_lens_geometry_bake_mode.json
- **What it is:** third lens: geometry / bake / mode coherence; 7 findings (1 BLOCKER).
- **Status:** none. Reading: historical.
- **Bears on:** PC.
- **Content that matters:**
  - :7 (BLOCKER) `element_afforded` ranks affordance on each element's `geo['gap']`, but `select_mode`'s comparator (systems.py:325-326), `core.strike` and `adef_cap` resolve on whole-weapon `w['gap']`; `mode_elements` carried only `{head, geo}`, no position, so a "close-efficacy from its own geo" is un-computable without plumbing.
  - :13 (SERIOUS) `core.damage`'s blunt branch reads whole-weapon `percussion_authority` while the cut/thrust branch would be grip-aware: a choked blunt strike would deal full-extension damage; make percussion circumstance-aware in the same increment or state that it is deliberately grip-invariant.
  - :19 (SERIOUS) `longer/shorter`, `measure_gap`, `closed` are all frozen from the same `er`; refreshing only `er[c]` lets a choked pole be labelled "longer" while reading shorter.
  - :25 (SERIOUS) "contact mirrors bind/riposte" is false: bind is a nested 3-iteration loop that mutates `beats`; `contact.axis` is injection metadata only (node=Bind, site "(WS-5, unbuilt)") and `STATES` has no Contact node.
  - :31 weapons are shared singletons (`combatant.w = WEAPONS[self.weapon]`) with `_derived` baked at import: circumstance quantities must take `(w, scalars)` and never be written onto the weapon dict. :43 `hook_affordance` as a saturating sum over `dual_role_element` guards would triple-read the same `extent_m` already summed into `blade_guard` by `_guard_catch_raw` (weapon_physics.py:316-324).
- **Conflicts / stale:** tree: `weapons.py:43,52` mode_elements now `{head, element_ref, geometry}` linked to `elements[]` by reference "NOT list order" (FIXED), 11 weapons; `sel_gap` threaded (combat_systems.py:649); Contact node present in state_graph. Whether `percussion_authority` became grip-aware was not grepped [UNVERIFIED].
- **Open items:** the percussion grip-invariance decision.

### .audit/2026-07-02-scene-combat-closing-distance-redesign/audit1_lens_physics_kinematics.json
- **What it is:** fourth lens: physics/kinematics correctness of the plan's formulas; 8 findings (2 BLOCKER).
- **Status:** none. Reading: historical, but its two BLOCKERs are the most reusable physics checks in the corpus.
- **Bears on:** PC, DICE (units discipline).
- **Content that matters:**
  - :14 (BLOCKER) `omega_cap = tau/I_g` is angular ACCELERATION (1/s^2), not velocity; fed into `1/2*m_eff*omega_cap^2` it ranks dagger KE ~8.1e6 over greatsword ~751 and spear ~47 (tau=30 N m; tau/I_g: dagger 10047, arming 200, longsword 132, greatsword 29, spear 15), the inverse of the intended ordering.
  - :20 (BLOCKER) the existing `heft()` (weapon_physics.py:389-399) deliberately reads `m_head*PoB_frac`, NOT MoI, because the spear's I_g (1.966) and poleaxe's (1.461) dwarf longsword (0.227)/arming (0.150); a KE term built on `I_g` re-creates the 84-96% polearm dominance via the damage channel. Ordering can only come from non-I_g terms (applied torque, swing angle).
  - :26 `m_eff = I_g/r^2` makes `m_eff * (omega r)^2/2 = I_g omega^2/2`: carrying both `m_eff` and an `I_g`-derived omega double counts or no-ops.
  - :31 `u` (metres) subtracted from `reach_base`, which is `L0 + REACH_GEOM_SCALE(0.635)*geom`: a units mismatch understates choke penalty by 1/0.635 (reach_base spans ~4.44 dagger to 7.80 spear; spear u@g=1 = 0.692 m).
  - :37 `range_avail` scaling omega then squaring makes swing damage fall quadratically with lost room; Bolander 2009 (via r0_flags C4) warns of a non-monotonic optimum. :43 the at_grip clamp makes the staff's `u_max=0` (PoB=0), disabling the very choke-up case the research cites; decouple the geometric slide from the CoM-bounded inertia slide.
- **Conflicts / stale:** tree: `weapon_physics.py:933-966` shows `geom_slide` decoupled from `u` ("M-04/M-20") and `rear_clearance` computed from located parts, i.e. findings :43 and `length_m` misuse were taken; `omega_cap`/`m_eff` do not appear (the faulty KE form was dropped). `REACH_GEOM_SCALE` is applied to `forward_extent(c,cfg,grip)` (combat_systems.py:62), consistent with the units fix.
- **Open items:** none.

### .audit/2026-07-02-scene-combat-closing-distance-redesign/audit1_lens_primitive_schema.json
- **What it is:** fifth lens: is the weapon schema sufficient for the plan's derivations; 6 findings (2 BLOCKER).
- **Status:** none. Reading: historical.
- **Bears on:** PC.
- **Content that matters:**
  - :15 (BLOCKER) `mode_elements` had no x_m/extent and were joined to `elements` only by list order (flamberge 3/0, poleaxe 3/3, voulge 3/2).
  - :21 (BLOCKER) every catching feature is `dual_role_element=True` with no hook-vs-lug discrimination; the Phase-0 per-guard `type`, `orient_deg` (rear-curved beak = -90) and notes were dropped by `weapons.py`.
  - :26 `orient_deg` (~124 occurrences) and `material` were collected on every element/guard and dropped; the bec_de_corbin hammer +90 / beak -90 / spike 0 distinction was flattened to positive `x_m`.
  - :32 `derive()['length_m']` is the full length, the wrong operand for rear clearance (spear 2.01 vs true rear extent -0.36; guisarme 2.10 vs -1.06; estoc_halfsword 1.57 vs -1.17); compute from `_all_parts`.
  - :38 grip bounds are already well-defined (`grip_choke_max`, `grip_travel_max`; mace/dagger/longsword 0.0, spear/staff/poleaxe 1.0, longsword_halfsword 0.8).
- **Conflicts / stale:** tree: `weapons.py:25` now documents `orient_deg` and `material` in `elements[]` (RE-INGESTED); `weapon_physics.at_circumstance` computes `rear_clearance` from `_all_parts` (matches :32); mode_elements link by `element_ref` (`weapons.py:43`).
- **Open items:** whether hook-vs-lug is now encoded [UNVERIFIED; `hook_affordance` does not exist, only `rear_clearance` at combat_systems.py:127 was found by grep].

### .audit/2026-07-02-scene-combat-closing-distance-redesign/audit1_lens_pipeline_trace.json
- **What it is:** sixth lens: exhaustive mechanical trace, walking `wrapper.engagement()` beat by beat across all 53 records; the richest of the six.
- **Status:** none. Reading: historical, except the beat call graph, which is a reusable map.
- **Bears on:** PC, CORE (state_graph / trace seam).
- **Content that matters:**
  - :6-73 `element_mode_inventory`: of 53 weapons only 8 had `mode_elements`; 16 flagged; 7 "silent-zip failures" (dangpa, spetum, partisan, guandao, fauchard, flamberge, hook_sword have >1 mass element, 0 modes); voulge 3 elements vs 2 modes; goedendag whole-gap 0.29 vs spike 0.73, guisarme 0.50 vs 0.75, poleaxe 0.78 vs 0.82/0.59 (:92).
  - :75-89 `comparator_table`: `element_afforded` is split-brain (cut/point read per-element `geo`, blunt reads whole-weapon `percussion_authority`, flagged `[PHASE-B6 PENDING]` in code at systems.py:268-271); `reach_threat` calls `adef_cap` with no `sel_head` while `armor_defeat_sigma` passes it, so one weapon's armour-defeat is scored on two different heads in one beat; `approach_displace` (systems.py:448) and wrapper.py:232 gate on NATIVE head.
  - :99-130 29-step `beat_call_graph` with a `staleness_risk` per step (frozen `er` read by reach_sigma/reopen/labels/reopen_moment, live reads by slip_inside/close_unwieldiness/str_demand; after riposte role-flip `sel_head/grip_position` are stale until next beat).
  - :132-171 label cross-reference: 0 of 15 `state_graph.STATES` and 8 of 9 `INJECTION_POINTS` are referenced by the wrapper; the state graph is a descriptive test artifact (`fired_states_from_events` reconstructs nodes from the trace event stream), only `TRACE_KINDS` (13), `SEPARATION_REASONS` (4) and 3 capability predicates are live. 21 orphan labels. INJECTION_POINTS hold hardcoded `wrapper.py:NN` line strings that no test checks (:183).
  - :173-184 findings: whole-weapon gap vs per-element geo (BLOCKER); frozen `er` (BLOCKER); state graph descriptive-only so "contact.axis goes live" must be built (BLOCKER); sel_head vs native head; percussion only whole-weapon; select_mode ignores `closed`; agility grip-blind.
- **Conflicts / stale:** tree: `state_graph.py:48-51` lists `Contact` in `Exchange/Bind/Riposte` edges; `wrapper.py:172` `er` refresh; `sel_gap` threading. Line numbers in the audit all refer to the deleted worktree.
- **Open items:** the trace-seam observation (state graph is not a control structure) stands unless `state_graph` became read by the wrapper [UNVERIFIED].

### .audit/2026-07-02-scene-combat-closing-distance-redesign/r0_flags.json
- **What it is:** Round-0 research cross-check: contradictions C1-C5 across four research streams (commitment_depth, facing_stance, grappling, measure_gap), a "weakly grounded" list and "strongly grounded" highlights.
- **Status:** none. Reading: historical research (tier 3 by repo rule); useful as an evidence-grade register.
- **Bears on:** PC (primary), SC (the same bind-gated / state-conditional contest logic), FI (epistemic grading).
- **Content that matters:**
  - :6-31 contradictions: C1 polearm facing (square vs bladed) unresolved, a Quora 403 snippet vs F3/F8; C2 facing is per-guard/per-moment, not per-weapon-class (so no per-class facing constant); C3 destreza circular footwork vs Italian linear lunge (do not generalise the Italian lunge); C4 Bolander 2009 non-monotonic force-vs-distance, "do not encode a strictly monotonic range-power relationship".
  - :34-39 C5 `clinch` values encode "free hand" (dagger 10, rondel 9, estoc_halfsword 9) not "hook hardware" (guisarme 2, ji 3, fauchard 2, dangpa 2, partisan 3).
  - :42-92 ten weakly grounded claims, including an unsupported "~50 cm minimum distance" (do not encode a hard threshold), an absence finding for treatise language about a truncated swing, and a "shaft easier to grab than hilt" inference with 0 direct sources.
  - :93-129 strongly grounded: the void and the close are the same motion (Fiore fol. 39r); sword grappling is bind-gated in both Fiore and German sources; a dominant grip yields a menu of outcomes (arm-break / throw / disarm / restrain); grabs are opportunistic on a prior opening; leverage is absolute hand-to-contact distance; long behind-the-hands length is a close-range liability; commit_depth and lunge_depth are driven by disposition/wariness, never by `measure_gap`.
- **Conflicts / stale:** tree: `clinch` deleted (weapons.py:17); `range_utilization` now couples commitment to measure.
- **Open items:** C1 polearm facing remained "needs a primary polearm-treatise read".

### .audit/2026-07-02-scene-combat-closing-distance-redesign/r0_research_commitment_depth.json
- **What it is:** Round-0 research file on thrust commitment depth and range utilisation, with a prior engine scan; 12 findings F1-F12 with sources and confidence.
- **Status:** none. Reading: historical research (tier 3); secondary-source heavy (web search summaries), several citations flagged unverified by the file itself.
- **Bears on:** PC.
- **Content that matters:**
  - :10-24 engine already had `commit_depth` (Beta over [2,5]), `lunge_depth` (LUNGE_COMMIT=4.0) and `grip_target`; the confirmed gap (:23): neither is driven by the current `measure_gap`.
  - F1 :29 Capoferro misura larga/stretta; the four-tier "larghissima/strettissima" is a modern teaching gloss (:34). F6 :77 German half-swording vs Fiore's "mezza spada" as a measure name (:82): do not conflate.
  - F8-F10 :95-:128 karate/boxing kinetic-chain studies (Rinaldi 2018 181.2 N; Dinu 2020; Beattie and Ruddock 2022; Dunn 2021; Bolander 2009) show force tied to joint-extension completion; Bolander is non-monotonic and read from snippets only ("most load-bearing and least-triple-verified numeric claim", :127).
  - F11 :132 absence: no treatise language for a checked swing, treatises switch to a different action by measure; F12 :140 Meyer's committed-vs-feinted depth as a chosen spectrum.
- **Conflicts / stale:** relies on Consensus.app paper links and Wiktenauer/Grokipedia paraphrases; not primary text.
- **Open items:** :148-151 three open questions (swing-arc truncation, Filipino/Chinese short-range doctrine, Bolander full table).

### .audit/2026-07-02-scene-combat-closing-distance-redesign/r0_research_facing_stance.json
- **What it is:** Round-0 research on square vs bladed stance across traditions and its link to footwork and grip change; 16 findings F1-F16, explicit disagreements, unreadable sources.
- **Status:** none. Reading: historical research (tier 3).
- **Bears on:** PC (primary), CHAR (tradition differences), FI (source grading).
- **Content that matters:**
  - :19 confirmed no body-facing concept existed in the engine ("bladed" there means the weapon class). F9 :102 no clean 1H-bladed / 2H-square rule; facing is per-guard/per-moment, counterexample Fiore's Posta di Donna (bladed, 2H).
  - F11 :122 Fiore's mezza-spada crossing as divider/unifier of zogho largo and stretto, grip change is measure-triggered (consistent with the engine's `halfsword_target`); F12-F15 German doctrine steps to the side though squared, destreza bladed with circular footwork closes measure, Italian rapier gathering-step plus lunge.
  - F16 :172 sport-fencing lunge ~1.5x height, 260.0 +/- 9.8 cm mean: modern sport data, "do not transfer directly".
  - :183-187 the lowest-confidence claims: Silver's "square-footed stance" rests on AI-aggregated paraphrase; polearm facing is the weakest sub-question.
  - :189-209 four sources unreadable (a Fiore lanza scan, ARMA study guide over 10 MB, a Meyer footwork article timeout, Quora 403).
- **Conflicts / stale:** F7 Silver claim unverified against the primary text.
- **Open items:** :211-214 three recommended primary-source reads before design relies on the polearm or Silver claims.

### .audit/2026-07-02-scene-combat-closing-distance-redesign/r0_research_grappling.json
- **What it is:** Round-0 research on historical weapon/limb grabs and pins, hooks, outcomes and the dead `clinch` field.
- **Status:** none. Reading: historical research (tier 3); Wiktenauer and ARMA pages partly blocked (403/10 MB), claims rest on secondary summaries and Mele's Getty reconstruction.
- **Bears on:** PC (grab/pin/disarm), SC (the same bind-gated contest shape, FA via nothing), FI (evidence grading).
- **Content that matters:**
  - :6 `clinch=<1-10>` on every weapon record with zero readers; sampled values dagger 10, rondel 9, estoc_halfsword 9, misericorde 7, bec_de_corbin 8, spear 2, rapier 2, guisarme 2, ji 3 (:126 notes the inconsistency with hook hardware). A prior unratified proposal exists at `designs/audit/2026-05-29-combat-armature/grappling_system_design.md` (:7).
  - Range finding (:25): Fiore's 25 stretto sword plays all proceed from an existing crossing (right foot forward); dagger and unarmed grabs are open-contact (the grab is the first contact, Dagger 1st Master at the apex of the strike, :45).
  - Four-branch outcome menu from one dominant grip (:48): arm-break, throw, disarm, tie in the high bind. Weapon foot-pin (rompere di punta, Getty Carta 28V, :38, :113). German Ringeck: hilt seize, mid-blade "Taking a Sword", biceps grabs, shoulder-fulcrum leg-break (:57-63).
  - Polearm hooks (:80-86): eight weapons carry `dual_role_element` catch hardware; the pattern beat/parry -> shaft-as-hook across the neck -> pull down -> thrust is Getty-cited for a plain spear; no source for a named play with a forged guisarme hook.
  - Success factors (:99-105): timing at the apex of a committed linear strike, leverage over raw grip, a free hand, a created opening; no source documents a grab against an uncompromised weapon.
- **Conflicts / stale:** tree: `contact.py:28` `grab_available(actor, opponent, opening_created, cfg)` implements the "opening_created" gate; `clinch` deleted.
- **Open items:** escape/counter detail extracted only at secondary level (:115); Ott Jud plays uncited (:73).

## Cross-subsystem leads
- **PC / CORE:** the beat call graph in `audit1_lens_pipeline_trace.json` (:99-130) and the state-graph finding that `state_graph.STATES` is reconstructed from trace events and never read by the engine (:170) bear on any lane that treats `state_graph` or `INJECTION_POINTS` as a control structure (CORE seam, PC). Tree shows a `Contact` node added since.
- **SC (+ DICE):** the Gate A/B/C verdict logs are the only record of social-contest design forks: Face scale-binding (Charisma x3 downward buffer vs 0-10 Standing upward), Composure retirement blast radius, Panel aggregation and reachability, Terminal Doubt on TallyAtClose, CR5 backfire trigger, STYLE_AXIS 4th axis, epideictic compression. Tag SC; CHAR for the armature (adjudicator conviction vector).
- **SC / CHAR:** `armature.py` `ARMATURE_MAX_DSIGMA = level("moderate")` (0.50 sigma) and the sub-1 pool quantisation lesson (0.15 off-axis rounded away by `max(1,int(round(pool)))`) bear on DICE and on any lane scoring fractional pool bonuses.
- **MB / CORE:** `findings_full.json` is the best evidence on default-toggle drift: two `FIELD_MOVEMENT`/`NODE_COHESION` defaults flipped without moving the acceptance validators or the multi-turn reset, validators wired into no CI, golden field digests recording the bug. Tree shows `PER_CELL` since flipped to 1 (ED-MB-0001) and route/maneuver goals added; MB and CORE lanes should check the field-digest and validator-gate state themselves.
- **MB / PC:** `check_drift`-style state re-keying (node state vs cell_troops) and `build_army` silent key drop are examples of pattern defects the repo's own predicate (§0.1 pt 5) governs.
- **PC / MB / CHAR:** the morphology records (53 weapons) feed `modules/combat/weapons.py`; MB troop equipment (`TROOP_TYPE_REACH`, `mounted_archers` with no `TROOP_TYPE_STATS`) references the same weapon names (polearms) [UNVERIFIED cross-link].
- **FI / WR:** research-file evidence grading (S1/S2/S3 tiers, "unverified snippet", absence findings) is the closest thing in `.audit/` to an epistemics register for fieldwork lanes; tag FI.
- **PROCESS:** Gate A R2:98 (CRLF-hash pins vs `git hash-object`) and R3:163 (`_index` Line columns stale after a main-doc edit) describe checker blind spots (`freshness_gate.py`, `ci_co_file_checker.py`); `ci_co_file_checker.py` still checks only `canonical_sources.yaml` co-change [UNVERIFIED].

## Likely stale or superseded
- Every path in these files is pre-restructure: `sim/personal/contest/` (now `systems/social_contest/sim/contest/`), `designs/scene/combat_engine_v1/` (now `modules/combat/` and `systems/combat/combat_engine_v1/`), `tests/sim/mass_battle/` (now `modules/mass_battle/` + `systems/mass_battle/sim/`), `designs/audit/...` (now `.audit/`).
- Contest Gate A/B/C findings: Guilds "GM picks" (fixed: "Context (venue-derived)", ED-1061), prebuilt-Panel skip (fixed `wrapper.py:165-166`), Panel reachability (Guild Arbitration, `dictionaries.py:380`), CR4 chosen-genre, CR5 standing cap, armature delta-sigma channel, Church Tribunal start ground (`modes.py:59-61`). The two-meanings Face scale fork appears still present (`primitives.py` `Face = Standing`, STRIP 0.8).
- MB movement/pathing findings: PER_CELL default (now 1), node `reset_positions` (now skipped explicitly), waypoint/route primitive (present), `check_drift` node re-key (present, units.py:1154); the 144-tick "freeze" was refuted at the time.
- Closing-distance plan lens findings: `clinch` (deleted), `mode_elements` linkage (element_ref), `er` per-beat refresh (present), `sel_gap` (present), `orient_deg` (re-ingested), `omega_cap` KE form (dropped). The plan file referenced is not in the tree.
- Both Track-2 decision-prep scripts: dead `sys.path` to `../../scene/combat_engine_v1`; they cannot run.
- Morphology Phase-0 JSON: superseded by `modules/combat/weapons.py` as the live record; combined file keeps the `mass_grade`/`confidence_tier` mismatches and the pre-fix path citations.

## Items that could change an audit finding
- **Face (SC):** if an SC lane reports "Face is decorative" or "Face has one scale", Gate A R1:34, R2:123 and R4:200 say the same thing about the 2026-07 kernel; the tree today still has `Face = Standing` and `STRIP = 0.8` (`primitives.py:33,108`), but `resolver.py:433` now strips standing-bounded points, so "never stripped" is false now. Re-verify before repeating.
- **Panel (SC):** "Panel unreachable" (Gate B R2:62) is false at the tree if `dictionaries.py:380` is accurate (reachable via Guild Arbitration); "simple majority" is stale: bench-weight = `Adjudicator.discipline`.
- **Obscuring dominance (SC):** Gate B R2:66-70 and R4:168-172 (Terminal Doubt undefined under TallyAtClose): I did not re-check whether ED-1060 was ever specified for the tally subset.
- **CR4/CR5 (SC):** the Memory (FACT) branch is reachable only if a proceeding starts on FACT; `modes.py:59-61` shows Church Tribunal moved to FACT; an SC audit saying "all 8 start on QUALITY" is stale.
- **Armature reveal (SC/CHAR):** `appraise_armature` has no resolver call (Gate C R3:272); the tree's `agon_harness.py:35-58` describes wiring it through an Appraise roll [UNVERIFIED whether live].
- **Combat (PC):** "clinch is dead data", "mode_elements have no positions", "reach_sigma reads frozen er", "heft ignores grip" are all stale per the tree checks above; the omega_cap units error and the "I_g is the wrong operand for impact" argument are the lasting physics lessons. A PC audit proposing a KE swing model should cite `audit1_lens_physics_kinematics.json` :14-26.
- **MB:** any MB audit claiming "maneuvers are dead on the default path", "PER_CELL is off", "reset_positions no-ops" or "validators measure the dead arm" must re-verify: the first three are fixed at the tree; the CI-gating of maneuver validators was not re-checked. The "mounted archers unit_type" gap (ED-1093 data half) cannot be confirmed closed by grep (`config.py:599,623` still comment "blocked on the kiting primitive").
- **Morphology (PC):** `hook_sword` double-listing, the Lucerne Hammer length conflict (239.1 vs 139.2 cm), pommel masses of 23-35% of weapon mass on residual-split blades (rapier 0.348/1.3, cinquedea 0.23/0.8, szabla 0.21/0.95, paired_short 0.202/0.7) are calibration artefacts, not specimen facts.
