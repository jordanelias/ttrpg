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

