# Digest audit1

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane scope: the surviving audit corpus under `.audit/` (lesser weight than `.designs/`; context and referents). Social-contest code now lives at `systems/social_contest/sim/contest/` (earlier audits call it `sim/personal/contest/`); the `designs/...` paths they cite are now `.designs/...` or gone. Reading note: bulk JSON/data files were read through a structure-aware dump (every field of every record printed, long strings truncated at about 260-330 chars) rather than raw; where a file is data-only the entry says what was sampled.

### .audit/2026-06-03-contest-groundup/engine.py
- **What it is:** 59-line Python module, 2026-06-03, "the shared stochastic core" copy of the base d10 + σ-leverage engine used by the contest ground-up rebuild (no author-lane stated).
- **Status:** none (module docstring says "verified 2026-06-02 against params/core.md ... Fixed; not tuned here"). Reading: historical (a frozen copy; the live owner is `engine/dice_engine/dice_engine.py` and `engine/dice_engine/sigma_leverage.py`).
- **Bears on:** DICE, SC
- **Content that matters:**
  - Base model: net ~ Normal(0.40·pool, 0.80·√pool) at TN 7; die map 1→−1, 2-6→0, 7-9→+1, 10→+2; Ob 1-20 (`:10-13`).
  - `OVERWHELM_SIGMA = 0.85`: degree-3 bar = pool mean + 0.85·σ to hold Overwhelming near 21% across pool sizes (`:14-15`, `:54-57`); pool-less call keeps the legacy `2·ob` bar (`:58`).
  - σ-leverage: `M_MAX=1.5`, LEVEL minor/moderate/strong/major = 0.25/0.50/0.75/1.00, `eff_sigma = M_MAX·tanh(dσ/M_MAX)` (`:18-23`).
  - `net_boost` is the resolution-path advantage (a μ-shift of `eff_sigma·sigma_N(pool)`); `effective_ob` is declared DISPLAY-ONLY post ED-884/ED-934 so the Ob floor is never breached (`:24-38`).
  - Degree bands 0 Failure / 1 Partial / 2 Success / 3 Overwhelming (`:47-59`).
- **Conflicts / stale:** `OVERWHELM_SIGMA` no longer lives here: `engine/dice_engine/sigma_leverage.py:120` says "OVERWHELM_SIGMA MOVED 2026-08-27 (ED-SC-0032)"; `MU_PER_DIE`/`SD_PER_DIE` now owned at `engine/dice_engine/dice_engine.py:181` and aliased in `sigma_leverage.py:118-119`. Degree banding is now `degree_from_net` (`dice_engine.py:236`), so this copy is a superseded second owner (still-live only as audit evidence).
- **Open items:** none.

### .audit/2026-07-01-contest-gate-a-packet/verdict_log.json
- **What it is:** JSON, 5 adversarial-judge rounds (2026-07-01) on the Stage-1d / Gate-A social-contest rebuild diff (CR1/CR2/CR3 fold-in: three trackers Concentration + Face + Persuasion, Composure retired, ED-1055/ED-1056).
- **Status:** none; every round ends `tests_green: True`, `escalate: None`. Reading: historical; most code findings fixed, the design questions superseded by later contest work.
- **Bears on:** SC, DICE, PROCESS
- **Content that matters:**
  - Method: a judge verifies each claim by grep/AST/running the CI validator (e.g. ran `tools/validate_ed_citations.py`, exit 1, 4 OPEN_AS_BASIS violations because `_is_resolved()` excludes `provisional`), ruling upheld / overruled / deferred with severity (blocker/major/minor/nit) and a `spawns_ed` stub. Rounds 1-5 at lines `:2`, `:76`, `:127`, `:161`, `:206`.
  - Blockers R1: `canonical_sources.yaml` absent from the changeset (`ci_co_file_checker.py` Rule 1) and the ED-1055 provisional-citation violations; both "local pass is false because nothing is committed" (`:5-15`).
  - Major R1: "Face" names two incompatible things: `params/contest.md` Face = Charisma×3 (3-21) Rattled strain buffer vs kernel `Face = Standing` (0-10, START 5, ethos-built, monotonic-up, `Standing.strip()` never called) (`:22-33`); R2 adds that they are oppositely signed (`:103-108`).
  - R1/R4/R5: the CR3 tracker layer (`Face` alias, `TRACKERS`, `RETIRED_TRACKERS`, `.face/.concentration`) has no resolution consumer, only tests; three-trackers `WIRED` over-states (`:34-45`, `:194-199`); the judge overruled the "decorative" charge in R2 (`:109-114`) and R4/R5 (`:165-169`, `:210-214`) because Standing/Reserve are live, but upheld it as a nit in R4 (`:194-199`).
  - Recurrent defects found: dead imports (resolver.py:15-17), ED-902 cited alone instead of ED-901+ED-902+ED-933 chain (D0-minor), stale index line numbers after a 140-line insert (index says §8@293, actual 435) (`:136-141`), CRLF-hash canonical SHA pins (`:80-84`).
  - Open decisions carried each round: Face scale-binding; Composure retirement blast radius (knots §4.2 left untouched); may provisional EDs be cited as basis (`:71-75`, `:229-232`).
- **Conflicts / stale:** At the working tree: resolver dead imports FIXED (`systems/social_contest/sim/contest/resolver.py:15-17` imports `FaceScale`, not `Face`/`TRACKERS`); the CR5 backfire now fires (`resolver.py:437` `c.face.strip_points`), so the "Standing.strip never called" finding is stale. Whether the Face Cha×3 vs Standing split was closed: [UNVERIFIED] (`FaceScale` exists in primitives, suggests a scale-binding was added). `RETIRED_TRACKERS` still exported in `__init__`/`primitives`/`wrapper`/`_kernel_tests`.
- **Open items:** the three decisions above; per this log nothing records Jordan's answers (the Gate-B log shows the Face/Composure item "still needs_jordan, ED-1056").

### .audit/2026-07-01-contest-gate-b-packet/verdict_log.json
- **What it is:** JSON, 4 judge rounds on Stage-2 / Gate-B (typed dictionaries: styles, interaction types, adjudicators, faction boosts, proceedings; Panel closure of ED-137 via `VoteAtClose`, ED-1057..ED-1060).
- **Status:** none; each round `tests_green: True`. Reading: historical; most items fixed in code.
- **Bears on:** SC, FA
- **Content that matters:**
  - R1 F1 (major): the Panel simple-majority rule was justified by a fabricated citation ("matches §10 BG parliamentary vote"); canon §10 is a Mandate-weighted pool and §7.2 lists seven heterogeneous aggregation rules (`:5-9`).
  - R1 F2 (major): a prebuilt `contract.Panel` object silently skipped the Panel closure and fell back to Tally/PersuasionTrack (`:11-15`).
  - R1/R2: six Stage-2 typed dictionaries marked WIRED but consumed nowhere in resolution (`:23-27`); no canonical proceeding routes to Panel (dead mechanic) (`:56-60`).
  - R2 F4 (major): Obscuring Styles (Suppression/Insinuation) strictly dominated by Precedent/Vision in single-exchange proceedings (Doubt Marker has no downstream) → ED-1060 Terminal Doubt; R3 found Terminal Doubt self-contradictory on direction (`:62-66`, `:131-135`); R4 found it written only for PersuasionTrack, while Casual Dispute / Personal Appeal resolve by `TallyAtClose` (`:247-251`).
  - R3 and R4: Royal Audience ≡ Guild Arbitration and Casual Dispute ≡ Personal Appeal are mechanically identical until resistance and asymmetric roles are plumbed (`:136-140`); Guilds faction boost carries "GM picks" in a no-GM engine (`:146-150`, `:252-256`); flavour text dishonesty ("bench" for a single judge, "vote" on a track proceeding, Private Negotiation invented mutual-consent).
- **Conflicts / stale:** At the tree: "GM picks" fixed by ED-1061 (`dictionaries.py:427-436` "engine-derived, was GM picks"); prebuilt-Panel path fixed (`wrapper.py:156-165`); `guild_arbitration` now has Panel adjudicator (`modes.py:502` comment "Standard | Panel"), so Panel reachability is answered; `VoteAtClose` now has an `aggregation` parameter and a weighted branch (`resolver.py:121`, `dictionaries.py:674`), so the "simple majority only" decision moved. Default jurors still 7 in `VoteAtClose` (`resolver.py:121`) vs `PANEL_DEFAULT_JURORS` in dictionaries (`dictionaries.py:693`) [size value UNVERIFIED].
- **Open items:** Venue flavour voice (verb-first) and POV-locked flavours (`:263-268`); whether `Terminal Doubt` was registered in glossary/mechanical_terms_index (`:158-162`): [UNVERIFIED].

### .audit/2026-07-01-contest-gate-c-packet/GATE_C_packet.md
- **What it is:** 498-line agonist packet for Stage 3 / Gate C (CR4 stasis×genre, CR5 orientation self-gating, the adjudicator armature), ED-1062, dated 2026-07-01, three re-revisions folded in.
- **Status:** "AUDIT / GATE PACKET ... Not canon until Jordan ratifies" (`:1-2`). Reading: historical (superseded by the `2026-07-02-contest-gate-c-packet` rebuild, see next entries); code described is live.
- **Bears on:** SC, DICE, CHAR
- **Content that matters:**
  - CR4: +1D reception-pool die keyed on the orator's CHOSEN Style genre (`genre_of_style`: Precedent/Suppression→Memory, Vision/Insinuation→Projection) against the live stasis's primary genre, because keying on the move ground was a tautology (`Stasis.relevant` forces `move.ground == live`) (`:13-30`, `:134-164`); ground map FACT→Memory, DEFINITION→None (higher-order reframe, not a genre), CONSEQUENCE/FEASIBILITY→Projection (`:59-69`, `:147-154`).
  - CR5: self-Face backfire only on a deg==0 Obscuring move, magnitude `min(2, own Face)` via `Standing.strip_points` (fixed points; `strip()` scales by STRIP=0.8, so −1.6 was applied against a cited −2); the opponent-Face-attack half is DEFERRED and `orientation_channel` is a design-table label only (`:31-41`, `:70-76`, `:203-240`).
  - Armature: adjudicator gets a 4-axis Conviction vector; Style×position dot-product feeds a continuous δσ μ-shift (`ARMATURE_MAX_DSIGMA = level("moderate") = 0.50σ`) because a fractional pool bonus is floored by `roll_net` (`max(1,int(round(pool)))`) so off-axis 0.15 was byte-identical to flat (`:42-57`, `:259-267`); STYLE_AXIS table Precedent→Evidence, Vision→Consequence, Suppression→Authority, Insinuation→Insinuation (new invention; canon's 4th is Solidarity) with PRIMARY 1.0 / OFFAXIS 0.15 [SEED] (`:294-322`).
  - Gate-off when adjudicator == opponent (asymmetric proceedings) prevents double counting; Panel position = mean of members' positions (`:324-336`); verdict becomes conviction-sensitive, `flat < misaligned < aligned`, closing SIM-DEBT-04 (`:338-346`).
  - Appraise-reveal boundary for `armature_position`: Failure→misleading axis, Partial→register, Success→dominant axis, Overwhelming→axis + coarse strength band; exact vector never revealed (`:363-384`).
  - Verification claimed: `pytest sim tests/valoria` 1041 passed; kernel tests 377 passed (`:7-9`); golden-trace agôn parity held because armature is opt-in (`:10-11`).
- **Conflicts / stale:** Cites `designs/scene/social_contest_v30.md`, `npc_behavior_v30.md §1.3`, `modifier_system_spec.md §2.3` (now `.designs/` paths or retired); `sim/personal/contest/` is now `systems/social_contest/sim/contest/` (`style_axis_dsigma`, `cr5_self_backfire`, `ARMATURE_MAX_DSIGMA` confirmed present there). Test counts (1041, 377) are stale snapshots.
- **Open items:** Jordan forks at `:404-439`: STYLE_AXIS numeric projection and 4th axis (Insinuation vs Solidarity); Appraise-reveal boundary; epideictic loss (recommended accept 2-genre compression); CR5 Face-cost anchor and whether cost should grow with standing; fold the categorical opponent-aimed +1D into the continuous primitive (`:279-281`). Opponent-Face-attack half of CR5 stays unwired.

### .audit/2026-07-01-scene-combat-track2-decision-prep/_workings_joined.md
- **What it is:** 1123-line machine-joined archive (`tools/join_audit_workings.py`) of four working papers, 2026-07-01, for the scene-combat Track-2 residuals: polearm close-quarters grounding memo, Track-2 residual recommendations, `WP.reach()/authority()` comparison, `wt/spd` de-leak report.
- **Status:** each fragment "decision-prep only"/"RECOMMENDATION, not a decision" (`:22`, `:627`, `:868`, `:958`). Reading: historical/superseded (the code it studies was re-architected by the morphology re-arch).
- **Bears on:** PC
- **Content that matters:**
  - Jordan's claims under test: A, grip asymmetry/overhang (a choked spear's trailing butt costs clearance); B, a choked thrust degrades to a shaft/butt strike. Root numeric: spear `grip_choke_max = 1.0` (same as staff), spear `I_g=1.062` vs staff `0.362` at g=1.0, `S_g→0`; model had no trailing-mass term and `select_mode` never read `grip_position`; targeted the reported 94-96% spear win rate (`:29-46`, `:335-404`).
  - Evidence tiers: Claim B well grounded (Le Jeu de la Hache "demy-hache", Fiore Zogho Stretto, Winn); Claim A form-only, no magnitude (ARMA forum, Silver paraphrase, Escamilla and Fleisig 2009 choke-up lowers bat velocity); "half-staff" grip is Victorian, not early-modern; Chinese-source claims unverifiable (`:57-103`, `:124-172`, `:289-331`).
  - Proposal: `overhang_penalty = m_trail·L_behind²` into `recoverability_factor` as `clearance_mult`, plus a hard `available_extension` gate in `select_mode` stripping the point head to a mace-coupled shaft strike; both coefficients (`K_OVERHANG`, `MIN_POINT_CLEARANCE`) are FIAT/SIM-CALIBRATE (`:428-452`, `:608-620`).
  - Residual 1 verdict: approve the `wield_heft`-reuse for `heft_resp` except the spear (spear damage would rise +10 to +14 flat, ×2-2.5); reject full `spd → 1/recoverability_factor` as double-counting with `weapon_tempo`'s `pen` term (`WEIGHT_PEN=0.8`, `HANDS_COMMIT=0.5`); corr(spd, 1/recov)=+0.878 vs +0.359 for thrust-ness (`:705-735`, `:1008-1063`). Staff, not spear, is the largest tempo mover (+1.137) (`:1079-1090`).
  - Residual 2 verdict: do not wire `WP.reach()` (ratio to live `reach_base` 0.16-0.77, non-affine; spear 5.98 < `CLOSE_REACH_REF` 6.5 would zero its close penalty) or `WP.authority()` (`sqrt(mass)·(0.30+pob)`, the only bare literal in the module); relabel as "retired diagnostic" (`:828-861`, `:877-900`).
  - Three overlapping impact formulas existed: `WP.authority` (unwired), `percussion_authority` (blunt, live), `heft_resp` (non-blunt, live) (`:939-944`).
- **Conflicts / stale:** Live tree contradicts the memo's premises: `modules/combat/core.py:147-157` `heft_resp` is now DERIVED from `weapon_physics.heft()` ("morphology-rearch Phase B6 ... replacing the binary wt{light,heavy} class outright"); `WP.reach`/`WP.authority` no longer exist in `modules/combat/weapon_physics.py` (grep for `def authority` and `def reach(` finds only an unrelated `engine/season/queries/world_q.py`); `overhang_penalty`, `MIN_POINT_CLEARANCE`, `shaft_strike` appear nowhere in `modules/`/`systems/`/`engine/` (never built under those names); `grip_choke_max` still exists (`modules/combat/weapon_physics.py`, `config.py`, `combat_systems.py`). Paths cited (`designs/scene/combat_engine_v1/`) are retired; code is `modules/combat/`.
- **Open items:** whether trailing-overhang / thrust-to-shaft-strike is modelled anywhere in current `modules/combat` under another name: [UNVERIFIED] (names above not found).

### .audit/2026-07-01-scene-combat-track2-decision-prep/wp_reach_authority_measurement.py
- **What it is:** 47-line Python harness tabulating `WP.reach()`/`WP.authority()` against `systems.reach_base`/`percussion_authority`/`core.heft_resp` for 12 weapons.
- **Status:** none. Reading: historical (dead: the functions it imports are gone).
- **Bears on:** PC
- **Content that matters:**
  - Imports `config, core, systems, weapon_physics as WP, weapons` via `sys.path` to `../../scene/combat_engine_v1` (`:11-14`); that directory no longer exists.
  - Roster of 12 weapons incl. `longsword_halfsword` (`:19-20`); prints reach ratio and authority columns, using `core.heft_resp(w, CFG)` for edged live heft (`:44`).
  - The `heft_resp(w, CFG)` call signature still matches the live one (`modules/combat/core.py:147`), but `WP.reach`/`WP.authority` do not exist.
- **Conflicts / stale:** cannot run against the working tree (retired import path, removed functions).
- **Open items:** none.

### .audit/2026-07-01-scene-combat-track2-decision-prep/wt_spd_deleak_measurement.py
- **What it is:** 203-line Python harness for the `wt/spd` de-leak (damage-path `heft_resp` vs `wield_heft`-reuse; tempo-path `spd` vs `1/recoverability_factor`), K'=0.6425 anchored on `arming`.
- **Status:** none. Reading: historical (the legacy `wt`/`spd` fields it measures were replaced).
- **Bears on:** PC
- **Content that matters:**
  - Candidate heft = `(at_grip(w,0)['I_g']/REC_I_REF)**WIELD_HEFT_EXP`; candidate tempo = `K'/recoverability_factor`; mock combatant with `agi=4`, `poise=1.0`, `grip_position=0`, `lunge_depth=0` (`:52-72`, `:80-90`).
  - Comparison point `core.damage(..., gap=w['gap'], perc=WP.percussion_authority(w))` with a note "ED-PC-0036: `close=` retired from core.damage" (`:100-105`): the harness was patched for later core changes, so it was kept alive after the memo.
  - Pearson correlation helper and `primitives_table` (`:114-150`) give the +0.878 / +0.359 figures.
- **Conflicts / stale:** `w['spd']` not found in `modules/combat/*.py` by grep for `'spd'`; `heft_resp` is now derived (see joined-workings entry). Not runnable against the working tree (`sys.path` to retired dir).
- **Open items:** none.

### .audit/2026-07-02-contest-gate-c-packet/GATE_C_packet_raw.json
- **What it is:** 38-line markdown-fenced "JSON" (not parseable as JSON because of the code fence) holding the Round-4 closure synthesis of the Gate-C judge/agonist relay, section-per-key (HEADLINE, CR4/CR5, ARMATURE, CHECKER BOARD, CONTEST LOG, OPEN DECISIONS, FILES TOUCHED, RESIDUAL).
- **Status:** "CONVERGED (Round 4 closure)" (`:5` of the content). Reading: historical; a machine-written summary with at least two errors against the sibling packet.
- **Bears on:** SC, DICE
- **Content that matters:**
  - Contest log of 4 rounds (12, 8, 10, 9 findings), with fix status per finding; 11 of 12 supporting findings fixed, 1 deferred (CR5 supersedes vs keeps Doubt Marker) (`:22`, `:34`).
  - Eight open decisions for Jordan: STYLE_AXIS cells; 4th axis Insinuation vs Solidarity; Appraise-reveal boundary; epideictic compression; CR5 specifics; CR5 trigger semantics (deg==0 low roll is not a modelled nigrahasthana; `FaultState` gating vs relabel); CR4 chosen-genre wiring; CR4 Memory-branch reachability (`:26`).
  - Seeded probes cited: CR4 chosen-genre +1D mean track delta +0.27 (200 seeds); armature aligned 0.50σ gives +0.18σ mean-track delta; CR5 strip 10/10 on deg==0 Obscuring (`:18`).
- **Conflicts / stale:** Internal inconsistencies: it says `armature.resonance_uplift(alignment)` is called at `resolver.py:296` (`:18`) although the packet and summary say that path was deleted; it lists `genre_of_style` as Suppression→Authority, Insinuation→Insinuation (axis names, not genres; the packet says Suppression→Memory, Insinuation→Projection); it says "(both round to 0 dice at pool==13+0.15)" as a PASS note. Treat the sibling `GATE_C_packet.md` and `final_build_summary.md` as the reliable statements. File begins with a BOM and a code fence.
- **Open items:** the eight decisions above; none show a recorded ruling in this corpus.

### .audit/2026-07-02-contest-gate-c-packet/final_build_summary.md
- **What it is:** 41-line agonist close-out for the Gate-C re-revision (findings 1, 4, 5 fixed), `HEAD f374b816`, nothing committed.
- **Status:** none; reading: historical, consistent with the 07-01 packet's RE-REVISED #3 block.
- **Bears on:** SC, DICE
- **Content that matters:**
  - Verbatim results: kernel tests 377 passed (was 370); `pytest sim tests/valoria` 1041 passed in 91.72 s (`:5-6`).
  - CR4 re-keyed on chosen Style genre and now armature-gated, which restores byte-identical golden-trace parity on `armature=None` (`:11`); CR5 `min(CR5_BACKFIRE_MAGNITUDE, own Face)` (`:13`); armature as continuous δσ because `roll_net` floors `max(1,int(round(pool)))` (`:15`).
  - Files were modified in a throwaway worktree `.claude/worktrees/happy-shaw-da0f1d` (Windows path), uncommitted; the ED-1062 ledger entry and the `id_reservations.yaml` bump were left to a "Synthesist" (`:41`).
- **Conflicts / stale:** worktree paths do not exist; counts stale.
- **Open items:** same Jordan forks as the packet (STYLE_AXIS cells, 4th axis, standing scaling, opponent-Face-attack deferral, Appraise boundary, epideictic compression).

### .audit/2026-07-02-contest-gate-c-packet/verdict_log.json
- **What it is:** JSON, 4 judge rounds (12, 11, 12, 9 verdicts) on the Gate-C Stage-3 build (CR4, CR5, armature, Appraise-reveal).
- **Status:** none; every round `tests_green: True`, `escalate: None`. Reading: historical; the code defects were fixed, design forks stayed open.
- **Bears on:** SC, DICE, CHAR
- **Content that matters:**
  - Method: grep for consumers + seeded probes. Examples: logos_spammer ×300 moves the mean track only ~0.056 from the pre-existing tense weight (so the CR4 genre map was a dead lookup); 600-seed single `_apply` showed 10/10 backfires also advanced the mover's own track (so the trigger penalised partial successes); 800-seed TallyAtClose run shows FLAT and MISALIGNED band distributions byte-identical `{b:401,a:399}` (the off-axis 0.15 was inert) (`:5-8`, `:62-68`, `:290`).
  - Round 1 majors: CR4 mapped but never consumed (WIRED label hollow because `mechanics_selftest` only checks symbol resolvability); two parallel armature channels (dead subtractive `armature_resistance` marked WIRED, live multiplicative `resonance_uplift` ×0.35 uncited) (`:5-39`, `:58-63`).
  - Round 2: `Standing.strip(2.0)` applies −1.6 (STRIP=0.8) vs cited −2; deg==0 backfire is not a Nyāya nigrahasthāna (the engine's `FaultState` machinery exists at `resolver.py:319-353` and is unused by the backfire); STYLE_AXIS cited "VERBATIM" to an empty `npc_behavior_v30` §1.3 stub (`:94-122`). Round 3 blocker: `STASIS_PRIMARY_GENRE[DEFINITION]=MEMORY` and TENSE-keyed derivation contradict the ratified CR4/reconciliation_map §1.2 (`:178-188`).
  - Round 3: the opponent-Face-attack half of CR5 is unrealized while the `cr5_self_gating` row says WIRED; `appraise_armature` has no call site in the resolver, so the reveal never fires in any playthrough (`:201-206`, `:231-236`).
  - Round 4: CR4's Memory/FACT branch unreachable in canonical play because all 8 proceedings start on QUALITY and the ladder shifts only up; `opponent_is_adjudicator` gate never derived from the proceeding roles (`:269-273`, `:292-297`).
- **Conflicts / stale:** At the tree: Memory-branch reachability answered (modes now start venues on FACT/CONSEQUENCE/DEFINITION, `systems/social_contest/sim/contest/modes.py:25-81`, church_tribunal changed QUALITY→FACT by comment at `:59-61`); `appraise_armature` now has a caller in `agon_harness.py:112,261` (a harness, not the resolver); `opponent_is_adjudicator` still a caller-passed flag (`armature.py:374-430`, no producer outside tests found by grep) so that Round-4 finding is likely still live; the dead imports/`strip(2.0)` findings are fixed (`strip_points`).
- **Open items:** CR5 trigger semantics (deg==0 vs `FaultState`), opponent-Face-attack, 4th axis, STYLE_AXIS cells, `_STRENGTH_LOW=0.34/_STRENGTH_HIGH=0.67` Appraise thresholds not on the Jordan list (`:244-248`).

### .audit/2026-07-02-mass-battle-movement-pathing-audit/README.md
- **What it is:** 283-line audit report and fix plan, 2026-07-02, Fable-led read-only diagnosis with per-finding Opus verification, triggered by Jordan watching the H4 Envelopment-vs-Arrowhead visualization ("the wings just go straight to the opponent").
- **Status:** "Findings ratified (ED-1096). Fix plan EXECUTED (ED-MB-0001, 2026-07-02, PR #66) — steps 1-7 + decision gates 2 and 4 DONE; gates 1 and 3 remain explicitly DEFERRED" (`:3-11`). Reading: mostly fixed; gates 1 and 3 are design that Jordan ruled but nothing built.
- **Bears on:** MB, CHAR
- **Content that matters:**
  - Root cause: since ED-1089 the default movement path `Subunit._node_advance` (`hierarchy/units.py:554-679`) steers each body straight at the enemy centroid and never reads `instructions`/`role`; the four maneuvers (`envelop`, `sweep`, overhang-cell `wheel`, ranged `kite`) live only in the legacy grid branch below the early return at `units.py:719-720` (`:41-57`).
  - Ten verified findings (table `:83-95`): `reset_positions` a no-op on the node path so turns 2-8 are welded to the turn-1 contact line (critical); ED-1095 mounted-archer kiting ineffective because implicit `role='Kite'` never sets `unit_type='ranged'` (critical); v12 column-local targeting dead (high); acceptance validators measure the dead arm and are in no CI (high); `check_drift` corrupts node state (high); `PER_CELL` default OFF (medium); `build_army` silently drops unknown keys such as `'speed':'Fast'` (medium); L1-normalised steps make diagonals ~29% slower (low); 12 of 15 `ROLE_SPEC` instruction tokens consumed nowhere (low); a `tick:N` order fires once per battle (low).
  - The "144-tick total freeze" claim was REFUTED (probable probe bug reading immutable formation ids instead of live `pos`) (`:64-70`).
  - Gate 1 (Jordan, recorded verbatim): directive changes of role/tactic mid-battle with (a) speed gated by Command, (b) effectiveness gated by Discipline, (c) number of conditional variants gated by Command; PROPOSED, NOT ratified: `transition_ticks = max(1, 8 - Command)`, a multiplicative pool penalty `(1 - discipline/DISCIPLINE_MAX)` while transitioning, slots 1/2/3 for Command 1-3/4-5/6-7 (`:108-158`).
  - Gate 2: `unit_type` derives from the troop's assigned weapon (`ARSENAL[...].reach`), and `kite` steering is weapon-independent (cavalry with lances can kite); Gate 3: split body-facing (follows movement path) from attention/FOV (locks on target), so a laterally moving unit "saw it coming" but still shows its flank (`:160-226`); Gate 4: `PER_CELL` default flips ON (`:228-239`).
  - Sequencing ruling: gates 1 and 3 only AFTER envelopment/pincer/wheeling is confirmed working (`:215-226`). Path-length budget ruling: route length limit = `0.5 × speed × max-ticks`, undeliverable paths rejected at design time, never silently truncated (`:272-282`).
- **Conflicts / stale:** At the tree (`modules/mass_battle/`, formerly `tests/sim/mass_battle/`): `PER_CELL` default is now '1' (`config.py:342`, cites ED-MB-0001 gate 4); `unit_type` now derived via `unit_type_for/TROOP_LOADOUT` (`armies.py:14,282-288`), so finding 1.2 is fixed; `check_drift` re-keys node state (`hierarchy/units.py` ~3050-3055 comment); `ROUTE_BUDGET_TICKS = 3 * TICKS_PER_PHASE` (`config.py:425`) is a different formula from the Jordan "0.5×speed×max-ticks" ruling [UNVERIFIED which supersedes]; `transition_ticks` and `_node_attention` names do not appear anywhere in `modules/`/`systems/`/`engine/` (gates 1 and 3 appear still unbuilt). Whether the 12 dead ROLE_SPEC tokens (`config.py:623` comments "blocked on the kiting primitive") are still dead: [UNVERIFIED]. The file's 'tests/sim/mass_battle' paths no longer exist.
- **Open items:** Gates 1 and 3 formulas await Jordan confirmation (and bear directly on the Command/Discipline mapping and on NPC/AI choosers issuing directives); a `tick:N` order re-arming per turn (the raw log asks whether released stance/instructions persisting across turns is intended).

### .audit/2026-07-02-mass-battle-movement-pathing-audit/findings_full.json
- **What it is:** 633-line raw workflow output (keys `diagnosis`, `verified`, `synthesis`, `usedFallback:false`) behind the README: confirmed prior findings, new findings, per-finding verifier transcripts, and the fix plan with byte-exact considerations.
- **Status:** none; reading: historical record, superseded by the README's table (same findings).
- **Bears on:** MB
- **Content that matters:**
  - Four prior claims classed CONFIRMED_EXACT (`envelop` `units.py:821-839`, `sweep` `:849-861`, overhang `wheel` `:807-813`) and CONFIRMED_WITH_CORRECTION (`kite`: works on the legacy grid with explicit `unit_type='ranged'`, dead on the field path) (`:6-17`).
  - Empirical numbers: node-path wings deployed at cols 3 and 15 end at ~9.6-9.8 and ~12.4-13.0 (converged) vs legacy files held (cols 0-7, 15-25); `PC_ENVELOP_PATH` on vs off both give `[4.2,4.2,4.2,4.2,3.5,4.2]` (the toggle has zero effect on the node path); `check_drift` on an Arrowhead tier-3 at discipline 2 (below `MIN_DISCIPLINE['Arrowhead']=4`) leaves 10 of 25 cells at (0,0) (`:20-45`).
  - Synthesis adds a medium finding the README folds in: the node WHEEL facing lerp degenerates to a zero vector at exact 180° reversal (`kw = disc_mult·0.5`, `lmag=0`), stalling exactly the wheel-to-rear case (`:332 ff`, synthesis item 6).
  - Capability assessment: not a ground-up rearchitecture; needs one new primitive, a per-subunit ordered list of `(goal-function, completion-predicate)` pairs modelled on the legacy `envelop` two-state machine, plus three repairs (`capability_architecture_assessment`).
  - Open questions listed: what the freeze probe measured; whether released stance/instructions persisting across turns is intended; where `Kite` should acquire `unit_type` (ROLE_SPEC field vs troop-type flag); what the body faces during a waypoint leg; whether field-path gauge bands need a full re-run; a pre-existing platform-dependent RNG desync in the 'cell' grid digest (`tests/valoria/test_mass_battle_byte_exact.py:32-50`).
- **Conflicts / stale:** line citations point at `tests/sim/mass_battle/...` (retired layout, now `modules/mass_battle/`); mounted_archers had no `TROOP_TYPE_STATS` preset (`troop_types/registry.py:34-45`) [current state UNVERIFIED].
- **Open items:** the freeze-test provenance and multi-turn command-state re-arm question appear unanswered in this corpus.

### .audit/2026-07-02-morphology-rearch-phase0/ (nine cluster files, one entry each below)
Shared shape for the nine `cluster_*.json` files (inspected record by record through a structured dump: every weapon's length, mass, grade, head elements, guard count, citation count, extra keys, plus the full `cluster_notes`): top-level keys `weapons` and `cluster_notes` (the straight-thrust file adds `batch_provenance_summary`); each weapon record carries `total_length_m`, `total_mass_kg`, `mass_grade` (S1 specimen, S2 typology, S3 estimate), `head_elements[]` (label, `mass_kg_est`, `x_m` from the working hand, `orient_deg`, `extent_m`, material, `edge_undulation`), `guards[]`, `haft_or_grip`, `pommel_or_butt`, `adornments`, `mass_budget` (residual vs total), `provenance` (citations, `confidence_tier`). All are Phase-0 inputs to the morphology re-architecture: the live roster derived from them is `modules/combat/weapons.py` (e.g. `hook_sword`, `voulge`, `flamberge` all appear there; `engine/engine_params/combat_engine_v1.json` also names `bear_spear`). The long cite lists (3-6 museum/treatise references per weapon) were counted, not transcribed.

### .audit/2026-07-02-morphology-rearch-phase0/cluster_dagger_and_hook_A.json
- **What it is:** 331-line JSON, 5 weapons (rondel, main_gauche, stiletto, misericorde, hook_sword), 2026-07-02, "cluster A" research batch.
- **Status:** none (data). Reading: input data, adopted (the weapons exist in live `modules/combat/weapons.py`).
- **Bears on:** PC
- **Content that matters:**
  - Lengths/masses: rondel 0.36 m/0.35 kg, main_gauche 0.435/0.55, stiletto 0.375/0.22, misericorde 0.435/0.28, hook_sword 0.60/0.75; all mass budgets close to 0.0% residual against the calibration prior (cluster_notes).
  - rondel is a two-disc dagger whose rear disc acts as a palm-driving pommel for push-thrust (the "second disc ... functioning as a palm-driving pommel"); main_gauche's `extent_m` on its shell/quillon/ring complex is "load-bearing" because the guard is its functional identity (Fabris/Capoferro/Giganti).
  - hook_sword is the weakest record in the whole roster (S3): scaled from one antique-dealer specimen (Mandarin Mansion, Qing, 979 g/103.7 cm) down to the engine anchor; its crescent is recorded under both `head_elements` and `guards` with shared 0.14 kg non-duplicated mass; the file leaves open whether the physics engine should consume one part-record or sum two.
- **Conflicts / stale:** the dual-listed crescent can double-count in a naive consumer (see combined-file flag 6); whether the live `weapon_physics` handles this: [UNVERIFIED].
- **Open items:** hook_sword dual-role mass sharing "a genuine open modeling question for Phase B".

### .audit/2026-07-02-morphology-rearch-phase0/cluster_existing_roster.json
- **What it is:** 778-line JSON, the canonical 12 (rapier, arming, longsword, greatsword, sabre, dagger, paired_short, spear, staff, mace, poleaxe, longsword_halfsword) decomposed into located, graded parts; the schema all other clusters were harmonised to.
- **Status:** none. Reading: input data, adopted.
- **Bears on:** PC
- **Content that matters:**
  - Axis/unit convention: `x_m` from the WORKING HAND (x=0 at hand, +tip, -butt), `weapon_physics.derive()` convention; `UNIT_M = 0.30 m` per length unit (cluster_notes).
  - Masses: rapier 1.3, arming 1.2, longsword 1.4, greatsword 2.7, sabre 0.9, dagger 0.3, paired_short 0.7 (S3: a COMPOSITE reference, no historical weapon of that name), spear 2.0 (butt_kg 0.25 sauroter, head 0.40), staff 1.5, mace 1.2, poleaxe 2.5 (three head elements: hammer, beak, top spike).
  - staff: the 40 mm diameter is a back-solved calibration constant "flagged as circular if used to verify the mass anchor"; spear butt_kg=0.25 is canon-fixed (`SPEAR-BALANCE [Jordan A, 2026-06-30]`).
  - longsword_halfsword = identical part set with the working-hand origin shifted 0.42 m forward along the blade (a FORM, not a separate weapon).
  - Records carry extra keys `pommel`, `butt`, `notes`; `total_length_m` is None for all 12 (derive() needs it; later clusters add it).
- **Conflicts / stale:** `paired_short` S3 is a class stand-in, which is a roster-semantics oddity for any balance claim keyed on it.
- **Open items:** none.

### .audit/2026-07-02-morphology-rearch-phase0/cluster_polearm_choppers_A.json
- **What it is:** 280-line JSON, 5 polearms (podao, fauchard, bardiche, sparr_axe, voulge).
- **Status:** none. Reading: input data, adopted.
- **Bears on:** PC
- **Content that matters:**
  - Masses/lengths: podao 2.6 kg/1.82 m, fauchard 2.2/2.2, bardiche 2.6/1.8 (S1, 3 museum specimens; modelled as ONE crescent element 1.75 kg, extent 1.476 m plus a 'lower_socket_langet' strap), sparr_axe 2.3/1.5 (S3), voulge 2.2/2.0 (S3, three elements: cleaver, heel spike, rear fluke).
  - voulge had zero handling/treatise sources in the prior research pass (weakest in the cluster); the fauchard back-hook is attested only for the developed 'composite glaive' variant.
  - Extra key `mass_source` on every record (the other clusters do not carry it).
- **Conflicts / stale:** none found.
- **Open items:** none beyond the S3 grading.

### .audit/2026-07-02-morphology-rearch-phase0/cluster_polearm_hooks_hammers_A.json
- **What it is:** 341-line JSON, 5 polearms (guisarme, ji, bec_de_corbin, lucerne_hammer, goedendag).
- **Status:** none. Reading: input data, adopted.
- **Bears on:** PC
- **Content that matters:**
  - bec_de_corbin 2.4 kg/1.8 m and lucerne_hammer 2.6/1.8 are three-element compound heads, poleaxe-family siblings (1.8 m haft, 50/50 centre-grip); Met accession 26670 gives 2.66 kg for the lucerne hammer; its length carries an unresolved unit-conversion flag (94 1/8 in vs 139.2 cm) so length is downgraded to S2.
  - ji 2.1 kg/2.4 m: straight spearhead + perpendicular crescent (yueyadao), no separate guard mass; guisarme 1.9/2.1 mirrors that at S2/S3; goedendag 1.8/1.2: extended wooden shaft element carries the mass, a zero-mass club-body placeholder element exists on purpose (flag 2 in the report), iron spike mass S3.
  - Records carry `grade: None` with confidence text in `provenance.confidence_tier` (free text, unlike the S1/S2/S3 tokens of other clusters).
- **Conflicts / stale:** inconsistent grade encoding across clusters (token vs free text) means any consumer that keys on `mass_grade` sees None here.
- **Open items:** goedendag has no museum specimen; lucerne_hammer length unresolved.

### .audit/2026-07-02-morphology-rearch-phase0/cluster_polearm_multi_and_blade_A.json
- **What it is:** 298-line JSON, 5 polearms (spetum, partisan, naginata, glaive, guandao).
- **Status:** none. Reading: input data, adopted.
- **Bears on:** PC
- **Content that matters:**
  - Totals "held IDENTICAL to the harmonized calibration in final_weapons.json": spetum 1.9 kg/2.199 m, partisan 2.6/2.301, naginata 1.4/2.10, glaive 1.9/2.10, guandao 3.8/2.40; only the part decomposition is new.
  - All five are two-handed hafted-tip, `hilt='none'`; every "guard" function (spetum/partisan wing lugs, guandao rear spike) rides on the HEAD, which is why hand_guard tokens in the calibration sit low (0.15-0.2).
  - glaive is the weakest (S3, pure analogy to naginata); guandao carries a tassel adornment (S2, non-universal on war pieces).
  - Residuals: spetum −5.3%, partisan −1.2%, naginata −3.6%, glaive −3.2%, guandao 0.0%, tuned by shaft-length assumptions.
- **Conflicts / stale:** refers to `final_weapons.json` (not in this corpus); its location is unknown [UNVERIFIED].
- **Open items:** none.

### .audit/2026-07-02-morphology-rearch-phase0/cluster_polearm_spears_A.json
- **What it is:** 371-line JSON, 5 spear-family weapons (yari, kama_yari, dangpa, bear_spear, ranseur).
- **Status:** none. Reading: input data, adopted.
- **Bears on:** PC
- **Content that matters:**
  - Masses/lengths: yari 1.23 kg/2.15 m, kama_yari 1.44/2.00, dangpa 1.84/2.29, bear_spear 2.35/2.05 (S1; Royal Armouries boar-spear 1.861 m, head 0.404 m, 2.27 kg), ranseur 2.15/2.10.
  - Method: shaft mass = π(haft_d/2)²·L·700 kg/m³ (ash/oak), subtracted from total to get a head residual, split across separate head elements; all budgets close within 0.15%; shared grip fraction 0.12-0.18 and cross-checked against the canonical `spear` (2.0 kg, haft_d 0.035 m, butt 0.25 kg).
  - ranseur is the weakest whole-weapon (no S1 treatise names it); secondary sources show ~4 kg vs 1.4-2.3 kg variance.
- **Conflicts / stale:** the 0.15% tolerance claim vs the combined report's "<=0.04%" for this cluster (minor inconsistency in the two summaries).
- **Open items:** none.

### .audit/2026-07-02-morphology-rearch-phase0/cluster_sword_curved_world_sabres_A.json
- **What it is:** 332-line JSON, 5 curved/cut-thrust swords (nandao, jian, scimitar, pulwar, shamshir).
- **Status:** none. Reading: input data, adopted.
- **Bears on:** PC
- **Content that matters:**
  - Masses/lengths: nandao 1.3 kg/1.095 m, jian 0.9/0.945, scimitar 1.0/1.065 (S1), pulwar 0.95/0.975, shamshir 0.85/1.005; each is one blade + one guard + pommel/butt-cap.
  - Residuals −4.6% to −9.5% (pulwar −9.47%, shamshir −9.41% sit at the ±10% ASSERT ceiling), attributed to unmodelled rivets, wire-binding, fuller material removal.
  - Curvature ladder from the prior calibration: shamshir 0.70 > pulwar 0.60 > scimitar 0.55 (cluster_notes, truncated in my read at that point); nandao is a 20th-century sport invention graded by analogy to niuweidao; jian has a pommel tassel adornment (S2).
- **Conflicts / stale:** curvature/keenness scalars live in the calibration, not in these physical fields (flagged "visibility only" in the report).
- **Open items:** none.

### .audit/2026-07-02-morphology-rearch-phase0/cluster_sword_japanese_chinese_long_A.json
- **What it is:** 321-line JSON, 5 long swords (katana, tachi, odachi, tsurugi, changdao).
- **Status:** none. Reading: input data, adopted (with the sign fix applied in the combined file).
- **Bears on:** PC
- **Content that matters:**
  - Masses/lengths: katana 1.1 kg/0.97 m, tachi 1.2/1.06, odachi 2.2/1.56 (S3 for the 120 cm/2.2 kg combat class), tsurugi 0.65/0.88 (S1: 527 g/68.4 cm Kofun specimen), changdao 1.6/1.95 (S1 length from Qi Jiguang's treatise).
  - Source bug: all five report `mass_budget.residual_pct` as a positive magnitude while part-sums are below total (true residual −5.7% to −7.9%); fixed in the combined file.
  - Blade centroid at 42-44% of blade length from the guard; no adornments (the Atsuta Shrine 4.5 kg and Norimitsu ~14.5 kg odachi are excluded as votive outliers).
- **Conflicts / stale:** the cluster file still has the uncorrected sign; use the combined file.
- **Open items:** none.

### .audit/2026-07-02-morphology-rearch-phase0/cluster_sword_straight_thrust_and_broad_A.json
- **What it is:** 370-line JSON, 6 weapons (szabla, cinquedea, flamberge, estoc, estoc_halfsword, falchion); has an extra `batch_provenance_summary`.
- **Status:** none. Reading: input data, adopted.
- **Bears on:** PC
- **Content that matters:**
  - Masses/lengths: szabla 0.95 kg/1.05 m, cinquedea 0.8/0.585 (2 Met specimens 740-908 g), flamberge 2.7/1.65, estoc 2.0/1.569, falchion 1.0/1.026.
  - flamberge: three head elements (flame-ground forte-to-mid, plain tip, dulled ricasso) plus a separate Parierhaken guard element; wave amplitude 15 mm/period 90 mm is a bracketed S3 estimate inside 10-20 mm/60-120 mm.
  - estoc_halfsword is a FORM of estoc: same 2.0 kg, same guard/pommel masses, `origin_shift_m=0.75` (~65% of head length), working point `head_length_m=0.399`, grip span 1.17 m.
  - No top-level grade field on these records (confidence in `provenance`).
- **Conflicts / stale:** none found.
- **Open items:** none.

### .audit/2026-07-02-morphology-rearch-phase0/phase0_morphology_combined.json
- **What it is:** 3895-line JSON (212 KB): `{weapons: 53 keys, flags: 7, harmonization_notes}`, the harmonised union of the nine cluster inputs.
- **Status:** none. Reading: derived artifact; the reference copy for the Phase-0 roster (checked: 53 keys, flags list length 7; per-weapon content equals the cluster inputs, which I read through the cluster files rather than line-by-line here).
- **Bears on:** PC
- **Content that matters:**
  - 53 weapons: canonical 12 + 41 new; the seven flags are the ones listed in `phase0_report.md`; `harmonization_notes` records the schema moves (`pommel_or_butt` split into `pommel{}`/`butt{}`, `total_length_m` kept as an extra field, re-derived `shaft_or_grip_est_kg` as sum minus head/guard/pommel/butt, ranseur and guandao tassel retained as attested-but-ceremonial).
  - This file, not the clusters, carries the sign-corrected Japanese/Chinese residuals.
  - Live-tree check: weapons from this set (bear_spear, hook_sword, voulge, flamberge) are present in `modules/combat/weapons.py`, `weapon_physics.py`, `contact.py`, `core.py`, `combat_systems.py` and `engine/engine_params/combat_engine_v1.json`.
- **Conflicts / stale:** the numeric content is a frozen capture of a research pass; the live `weapons.py` is the owner, so any divergence must be decided at `modules/combat/weapons.py` [UNVERIFIED that values match].
- **Open items:** none.

### .audit/2026-07-02-morphology-rearch-phase0/phase0_report.md
- **What it is:** 117-line harmonisation report for the 53-weapon Phase-0 roster (confidence summary, flags, weakest records, mass-budget table, comparability, FORMS/ADORNMENTS compliance).
- **Status:** none. Reading: historical reference for the data provenance.
- **Bears on:** PC
- **Content that matters:**
  - Weakest-grounded ranking: hook_sword (S3, no period treatise), voulge, goedendag, glaive, sparr_axe, odachi (combat class), nandao, ranseur, guisarme, flamberge wave numerics (`:100-115`).
  - All 53 residuals within ±10%; the two tightest are pulwar −9.47% and shamshir −9.41%; seven residuals are 0.00 by construction (`:116-170`).
  - Rules applied: FORMS (halfsword variants share the base part set, only the origin shifts), ADORNMENTS (only 3 survive: ranseur tassel S3, guandao tassel S2, jian pommel tassel S2, flagged non-combat).
  - "No AXIS violations, no UNIT inconsistencies, and no 0-1 behavioral scalars smuggled into mass/position/extent fields" was found (`:40-50`).
- **Conflicts / stale:** counts the clusters differently from one cluster's own note (polearm_spears "≤0.04%" vs file "0.15%").
- **Open items:** hook_sword crescent dual-listing "most likely to bite a downstream consumer that naively sums both lists".

### .audit/2026-07-02-scene-combat-closing-distance-redesign/_workings_joined.md
- **What it is:** 2704-line machine-joined archive of 10 working papers of the scene-combat closing-distance / facing / grip / grapple redesign ("R1" plan, "R2" implementation), 2026-07-02/03: README, two antagonist audits, a 23-item consolidated issue register, capstone punch-list and verifier notes, the I8 capstone audit, the ratified plan `plan_r1_RATIFIED.md`, the R0 research brief, and R0 ideal-state prep notes. Read in full.
- **Status:** README: "R2 implementation is COMPLETE (I0→I8, 2026-07-03)"; plan: "READY FOR JORDAN'S RATIFICATION" (`:893`) and README calls it "the final, Jordan-approved plan" (`:29`). Reading: implemented; the I8 item 1 finding (balance drift, Phase C) is the one open item.
- **Bears on:** PC, DICE
- **Content that matters:**
  - Motivating symptom: reach/pole weapons win 84-96% vs arming sword; Jordan: "we did a lot of work on weapon physics ... in ideal circumstances without considering ... less ideal circumstances"; the fix must be primitive-level degradation of an ideal ceiling, never a class nerf ("PRIMITIVE LAW": no branching on a weapon name; `test_no_weapon_name_literal_in_resolution` stays green) (`:987-1023`).
  - Register/plan decisions D0-D12 and increments I0-I8 with falsifiable acceptance criteria (`:1108-1935`): schema restoration (`orient_deg`, `element_ref`), `at_circumstance(w, grip, room)` bundle (rear_clearance from located parts, floored `geom_slide`), thrust-protection keyed on the SELECTED element's head (`sel_head=='point'` → Φ=1.0) with floored NaN-guarded swing Φ_grip, widened `select_mode` 5-tuple `(dm,h,sel_gap,sel_perc,sel_pc)` written at both call sites, two-recompute `er` contract, range_avail → commit-window + legibility with interior optimum (C4, Bolander 2009), a new Contact STATE + `contact.py` grab/pin, and `clinch` DELETED.
  - Audit method of note: six lens audits (physics, schema, geometry, coupling, architecture-orphan, pipeline-trace) merged into a register of 7 BLOCKER / 9 SERIOUS / 7 MINOR; a four-round agonist/antagonist repair loop (22 agents); then a 3-lens capstone (oscillator, emergence-gate, coherence) found a NEW blocker (grip↔reach 2-cycle: spear 0↔0.865 every beat, JD-9) by iterating the live recurrence (`:461-520`, `:2111-2163`).
  - Concrete findings that falsified earlier "verified" claims: `Φ_grip = S_g(g)/S_g(0)` zeroed closed thrusts (yari 0.000, spear 0.135, staff 0/0 NaN); `orient_deg` and whole-weapon `point_concentration` both fail to separate arc from thrust (bear_spear pc 0.55 < greatsword 0.62); `½·m_eff·omega_cap²` dimensionally invalid; `reach_base` subtracted metres from engine reach-units (`:99-134`, `:178-205`, `:232-238`).
  - I8 capstone record: reach-class poles still win 75-93% vs arming at all armour tiers (spear 78-82%, yari 83-90%, poleaxe 82-94%), dagger/main_gauche 17-26% unarmoured vs a 30-45% target; "not inverted" holds, "CONTESTED 55-75%" band NOT met; attributed to Phase-B grounded masses outrunning pre-Phase-B engine-scale constants, deferred to "Phase C" (`:781-814`, `:861-870`). Accepted-red set: 8 combat reds (5 element-parity tests regenerated at I4, `test_gap_game_poleaxe_spikes_plate`, `test_anchor_is_near_one`, `test_lunge_quality_is_weapon_derived_continuous`).
  - R0 research brief (facts only): fight divides into approach/close regimes across Fiore, Silver, Meyer, Liechtenauer, Capoferro; grabs are bind-gated or open-contact for dagger and always opportunistic on a created opening, with branching outcomes (Fiore 2nd Remedy Master: arm-break, throw, disarm, tie); facing is per-guard not per-weapon-class; polearm facing unresolved (flag C1); `clinch` field was dead data (`:2217-2608`).
  - Nine Jordan-decisions (`:1998-2163`), each with a plan default: JD-1 thrust/retained-material/greatsword cure; JD-2 `longer/shorter` label flip (default freeze); JD-3 poleaxe hammer vs spike; JD-4 hammer percussion grip-invariance; JD-5 seven silent-zip composites; JD-6 two-recompute contract; JD-7 pull-vs-bind primitive (default defer); JD-8 cut_thrust partisan/spetum part-swing; JD-9 fixed-grip drive for `grip_target`.
- **Conflicts / stale:** At the tree (`modules/combat/`): `at_circumstance`, `sel_pc`, `range_avail`, `rear_clearance`, `contact.py` (`grab_available`), `Contact` in `combat_systems.py` all exist, so the plan was built; `clinch` is deleted (`weapons.py:17`, "DELETED, I7b/D9, 2026-07-03"). Whether Phase C (the I8 balance recalibration) was ever done: [UNVERIFIED]; the 75-93% reach-class win rates are from 2026-07-03 and may be stale. The plan quotes Windows paths (`C:/Github/ttrpg-morph-rearch/...`, `designs/scene/combat_engine_v1/`) that no longer exist; JD answers (Jordan "approved" the plan wholesale) are not individually recorded in this corpus.
- **Open items:** I8 item 1 (roster-wide reach-class dominance vs the CONTESTED band, dagger underdog floor), Phase C engine-scale re-tune, JD-3 (poleaxe), JD-7 (pull-hook grab primitive deferred indefinitely), polearm facing (C1) unresolved.


### .audit/2026-07-02-scene-combat-closing-distance-redesign/audit1_lens_architecture_orphan.json
- **What it is:** 234-line JSON, first-generation lens audit (code-architecture / staging / orphan detection) of the original closing-distance plan `things-like-a-feather-compressed-rivest.md`, 2026-07-02.
- **Status:** none; reading: historical, fully absorbed into the consolidated register and the ratified plan (both inside `_workings_joined.md`).
- **Bears on:** PC, PROCESS
- **Content that matters:**
  - Layering verdict: plan honours L0/L1/L2/L3 (`at_circumstance` L0-pure, facing/range_avail as Combatant state with the wrapper as sole mutator, `contact.py` as L2); risks are sequencing, not layering.
  - Findings: I3 silently redefines `closed` (SERIOUS); the per-beat `er` recompute is under-specified on ordering (SERIOUS, must follow `grip_target` and the half-sword swap); `clinch` "retired OR residual bias" disjunction re-orphans (SERIOUS); I7 over-bundled (SERIOUS); scaffold fields orphaned for several increments (MINOR); plan's own Fable-audit section was `[PENDING]` (MINOR).
  - Orphan table: 12 of 13 new items VERIFIED with a named consumer; the one GAP is `clinch`.
- **Conflicts / stale:** its `hook_affordance`, `omega_cap`, `m_eff` items were later dropped from the plan.
- **Open items:** none outstanding in this file.

### .audit/2026-07-02-scene-combat-closing-distance-redesign/audit1_lens_consumer_coupling.json
- **What it is:** 77-line JSON, lens "consumer-coupling / half-switch risk", ten findings (2 BLOCKER, 4 SERIOUS, 4 MINOR) against increments I1-I8.
- **Status:** none; reading: historical, absorbed (M-03, M-09, M-12, M-15, M-16, M-17 in the register).
- **Bears on:** PC, PROCESS
- **Content that matters:**
  - Method: grep-verified every call site of each function an increment touches; cross-checked `wrapper.py` sequencing and the combat tests for hard-coded expectations that silently stop exercising a changed path.
  - BLOCKER: threading grip into `heft`/`percussion_authority` cannot be byte-identical since grip is already >0 at strike (wrapper.py:66); the "free cascade" of `reach_base` is false (`reach_sigma` reads a frozen `er`).
  - SERIOUS: `agility` reads full MoI not `at_grip` I_g; `test_combat_heft.py` pins only longsword==1.0 (re-anchor can silently re-tier damage); `select_mode` is called at three sites with different `closed` values.
  - MINOR: every `test_combat_*.py` does `pytest.importorskip('numpy')`, so a numpy-less validator job skips the combat suite (a green that is an all-skip).
- **Conflicts / stale:** the importorskip/all-skip hazard may still apply to the CI `tests/valoria` job without numpy [UNVERIFIED].
- **Open items:** none.

### .audit/2026-07-02-scene-combat-closing-distance-redesign/audit1_lens_geometry_bake_mode.json
- **What it is:** 48-line JSON, lens "geometry / bake / mode coherence", seven findings (1 BLOCKER, 4 SERIOUS, 2 MINOR).
- **Status:** none; reading: historical, absorbed (M-02, M-05, M-08, M-11, M-13).
- **Bears on:** PC
- **Content that matters:**
  - BLOCKER: `mode_elements` carry only `{head, geo}`, no position, so D5's "how far out each mode sits" is un-computable.
  - SERIOUS: sibling blunt path still reads static whole-weapon `percussion_authority` when `heft` becomes grip-aware; `longer/shorter`/`measure_gap`/`closed` are also frozen at engagement start; "wrapper branches mirror bind/riposte" is false (bind is a nested 3-iteration loop that mutates `beats`); the bake-once `_derived` cache stored on the weapon dict couples the static and dynamic worlds.
  - MINOR: `core.strike` pairs dynamic `sel_head` with whole-weapon `w['gap']`; `hook_affordance` would triple-read `extent_m`.
- **Conflicts / stale:** none beyond absorption.
- **Open items:** none.

### .audit/2026-07-02-scene-combat-closing-distance-redesign/audit1_lens_physics_kinematics.json
- **What it is:** 60-line JSON, lens "physics/kinematics correctness", eight findings (2 BLOCKER, 3 SERIOUS, 3 MINOR).
- **Status:** none; reading: historical, absorbed (M-01, M-04, M-19, M-20).
- **Bears on:** PC, DICE
- **Content that matters:**
  - BLOCKER: `omega_cap = τ/I_g` is angular acceleration (1/s²), so `½·m_eff·omega_cap²` is dimensionally invalid and numerically inverts the roster onto the dagger; any dimensionally correct fixed-ω reading reconnects damage to `I_g`, re-creating spear dominance.
  - SERIOUS: `m_eff` cancels against an `I_g`-derived ω; subtracting hand-slide metres from engine reach-units under-scales the choke by ~1/0.635; scaling ω by room makes swing damage fall quadratically (contradicts flag C4).
  - MINOR: `at_grip` clamps at CoM so a staff (PoB=0) gets u=0, making choke-up inert for the canonical half-staff weapon; mirror matches need the same `measure_gap` for both fighters.
- **Conflicts / stale:** none.
- **Open items:** none.

### .audit/2026-07-02-scene-combat-closing-distance-redesign/audit1_lens_pipeline_trace.json
- **What it is:** 185-line JSON, lens "exhaustive mechanical tracing": a 53-weapon element/mode inventory, comparator table, same-key-different-object flags, beat call graph, label cross-reference, findings.
- **Status:** none; reading: historical, absorbed (M-02, M-05, M-10, M-11, M-24).
- **Bears on:** PC, PROCESS
- **Content that matters:**
  - Read all 8 source files and imported `weapons.py` to enumerate all 53 records; 16 of 53 flagged for mode/element link problems (mode_elements linked to `elements[]` only by list order; 7 composites with >1 located part but 0 `mode_elements`; voulge 3 vs 2).
  - Same-key-different-object flags: `gap` (whole-weapon vs selected element), `head` (native vs selected), `percussion_authority` (whole vs per-element).
  - State graph is descriptive: 21 orphan labels (0 of 15 STATES and 8 of 9 INJECTION_POINTS referenced by name in wrapper/systems); no `Contact` state and no `'contact'` TRACE_KIND; `contact.axis` is metadata `(WS-5, unbuilt)`.
  - Measured divergences: goedendag whole gap 0.29 vs spike 0.73, guisarme 0.50 vs 0.75, ji 0.56 vs 0.68, voulge 0.48 vs 0.63, bec_de_corbin 0.82 vs beak 0.57 (the last later corrected).
- **Conflicts / stale:** `INJECTION_POINTS` site strings were dropped (I8 item 8); `Contact` now exists in `modules/combat/combat_systems.py`.
- **Open items:** none.

### .audit/2026-07-02-scene-combat-closing-distance-redesign/audit1_lens_primitive_schema.json
- **What it is:** 49-line JSON, lens "primitive-schema sufficiency", six findings (2 BLOCKER, 2 SERIOUS, 2 MINOR).
- **Status:** none; reading: historical, absorbed (M-05, M-06, M-07, M-19).
- **Bears on:** PC
- **Content that matters:**
  - Read `weapons.py` fully (53 records) plus the Phase-0 combined JSON; found `mode_elements` carry no `x_m`/`extent_m`; `hook_affordance` cannot tell a pull-hook from a bind-lug; Phase 0 collected `orient_deg` and `material` on every part and `weapons.py` dropped both.
  - `rear_clearance` must come from located-part positions, not `derive()['length_m']` (spear 2.01 vs true rear extent −0.36 m).
  - Non-blockers recorded: grip bounds are well formed; facing keyed on `head` tokens is not tempted into a class shortcut.
- **Conflicts / stale:** the later plan retracted the "orient_deg cleanly gates arc-vs-thrust" idea.
- **Open items:** none.

### .audit/2026-07-02-scene-combat-closing-distance-redesign/r0_flags.json
- **What it is:** 131-line JSON of five labelled contradictions (C1-C5), ten weakly-grounded claims, and nine strongly-grounded highlights from the R0 research synthesis.
- **Status:** none; reading: historical reference, load-bearing for the redesign's flag discipline.
- **Bears on:** PC, DICE
- **Content that matters:**
  - C1 polearm/greatsword facing square vs bladed UNRESOLVED (needs a primary polearm-treatise read); C2 facing is per-guard/per-moment not per-weapon-class; C3 bladed stance does not imply linear-only footwork (destreza circular footwork); C4 force-vs-distance NON-monotonic (Bolander 2009; no hard minimum-distance threshold may be encoded); C5 the `clinch` values (guisarme 2, ji 3, dagger 10, rondel 9) encode only free-hand, ignoring hook hardware.
  - Weakest claims: Silver "square-footed", Bolander single-study, butt-spike fallback, "shaft is easier to grab than a hilt" (inference), no treatise passage on cut-arc truncation, a "~50 cm minimum distance" is unsupported.
  - Strongest: void and close are the same motion (Fiore fol. 39r); sword grappling is bind-gated in both traditions; a single dominant grip gives a branching menu; grabs are opportunistic on a created opening.
- **Conflicts / stale:** none.
- **Open items:** primary read of Fiore spear/pollax and Meyer Stange for polearm facing.

### .audit/2026-07-02-scene-combat-closing-distance-redesign/r0_research_commitment_depth.json
- **What it is:** 153-line JSON, raw R0 research cluster (commitment depth and range-utilization): 12 findings, 3 open questions, engine scan, sources.
- **Status:** none; reading: historical raw input, synthesised in the combined brief (read in full there).
- **Bears on:** PC, DICE
- **Content that matters:**
  - F1 Capoferro graded measure (larga/stretta; the four-tier scheme is a modern gloss); lunge/passata a distinct deeper action; Meyer graduated commitment; peer-reviewed fencing-lunge and strike-force kinetic-chain studies (Rinaldi 2018 181.2 N); Bolander 2009 optimal distance; absence finding that treatises frame close range as switching action, not the same action weakened.
  - Confirmed engine gap: `commit_depth`/`lunge_depth` driven by disposition/wariness only, never by `measure_gap`.
- **Conflicts / stale:** (structure and key fields read via dump, long source lists counted rather than transcribed).
- **Open items:** whether a treatise passage exists for a cut/swing failing to develop force from inside its arc (answered "no" in the brief).

### .audit/2026-07-02-scene-combat-closing-distance-redesign/r0_research_facing_stance.json
- **What it is:** 216-line JSON, raw R0 cluster on facing/stance: 16 findings, 5 disagreements, 4 unreadable sources, 3 follow-ups.
- **Status:** none; reading: historical raw input, synthesised in the brief.
- **Bears on:** PC
- **Content that matters:**
  - Bladed: Fiore Posta di Donna, Fabris and Capoferro rapier; square: Vom Tag, chudan-no-kamae; destreza bladed with circular footwork; Liechtenauer square with offline stepping.
  - The one unreadable key source is the image-based Fiore lancia PDF (`hroarr.com/manuals/fiore/omsg_lanza.pdf`); follow-up: read a translated primary Fiore spear or pollaxe section to settle C1.
- **Conflicts / stale:** none.
- **Open items:** C1 polearm facing.

### .audit/2026-07-02-scene-combat-closing-distance-redesign/r0_research_grappling.json
- **What it is:** 139-line JSON, raw R0 cluster on grappling in armed combat: 10 findings, 5 blocked sources (Wiktenauer 403).
- **Status:** none; reading: historical raw input, synthesised in the brief.
- **Bears on:** PC
- **Content that matters:**
  - High confidence: bind-gated sword grappling in both Fiore (Zogho Stretto) and German (Ringeck "when you bind against his sword"); `clinch` field flagged dead data with Phase 5 not started; engine context records `prior_repo_proposal_not_source`.
  - Seizure targets documented (wrist, hilt, mid-blade with gloved hand, fingers, foot-pin of the weapon Getty Carta 28V).
- **Conflicts / stale:** the file mis-cited some `clinch` values (noted in flag C5).
- **Open items:** counters/escapes for a grabbed fighter documented as existing but not extracted in detail.

### .audit/2026-07-02-scene-combat-closing-distance-redesign/r0_research_measure_gap.json
- **What it is:** 232-line JSON, raw R0 cluster on measure/closing footwork and deflection: 4 finding groups, 3 cross-cutting observations, 19 sources.
- **Status:** none; reading: historical raw input, synthesised in the brief.
- **Bears on:** PC
- **Content that matters:**
  - Fiore Zogho Largo/Stretto as a regime boundary; Silver true times (hand before foot); Meyer Zufechten/Handtarbeit/Abzug; forte/foible as rigid-body lever mechanics; deflection as redirection; seizing a haft distinct from deflection.
  - Cross-cutting: all traditions converge that closing measure makes a different technique repertoire available.
- **Conflicts / stale:** none.
- **Open items:** forte/foible is a within-exchange contact-point quantity while the engine's `leverage()` is a per-weapon scalar (flagged gap, analytic not attested).

### .audit/2026-07-02-scene-combat-closing-distance-redesign/r0_workflow_script.js
- **What it is:** 124-line Workflow script for R0 (4 Sonnet research clusters then Opus synthesis); not in my assignment list (not listed) but present in the directory, read for context only.
- **Status:** none; reading: historical.
- **Bears on:** PROCESS
- **Content that matters:** hard-coded Windows scratch paths and the DISCIPLINE preamble ("facts only, no fiat effectiveness numbers, no invented 0-1 scalars", "do not propose a mechanic that already exists under a different name").
- **Conflicts / stale:** paths do not exist.
- **Open items:** none.

### .audit/2026-07-04-mass-battle-cannae-gauge-audit/README.md
- **What it is:** 443-line root-cause audit and fix plan for the H3-H6/C4 Cannae-pattern historical-gauge collapse after `PER_CELL` came on, 2026-07-04; four-lens adversarial read (`clock_coupling`, `historical_fidelity`, `alternative_mechanism`, `design_options`), Fable-adjudicated.
- **Status:** "RATIFIED (ED-MB-0002, 2026-07-04) — merged via PR #73"; DG-3 and DG-4 RESOLVED by Jordan the same day; DG-1, DG-2, DG-5 OPEN pending re-measurement (`:3-8`). Reading: partly executed; follow-up lanes (RC-3, RC-5, DG-1/2/5) unresolved in this corpus.
- **Bears on:** MB, DICE
- **Content that matters:**
  - RC-1 (very high confidence): three composition-coupling defects make a multi-subunit unit fight worse than the same troops as one subunit: (a) multi-front pool asymmetry, `POOL_VARIANT="C-ii"` (`orchestration.py:504-528`) scales a composed subunit's pool by troop fraction while a single-subunit opponent rolls its full pool into each pair, with the encirclement tax only −0.2σ/pair; (b) subunits with `morale=None` route writes to one shared parent pool, so two §A.4 triggers erode it twice; (c) per-subunit casualty denominators trip 50%/25% triggers faster under `PER_CELL` (`core/state.py:27-38`) (`:39-64`).
  - RC-2 (high): the old green baseline was an artifact: with `PER_CELL=0` cohesion is frozen at 1.0 and §A.4 triggers cannot fire, so the pre-flip H3-H6 pass validated an invincibility bug; "restore the pre-flip numbers" re-installs the artifact (`:66-73`).
  - RC-3 (medium): a fixture ablation shows the pinning-main-body-plus-detachment loses byte-identically whether the detachment envelops, marches in or never moves (refuting "two racing clocks" at fixture scope, but the detachment was a construction-order ghost cell, `validators.py:205`); C4 fails and C7 passes with the same `_envelop_army` composition against a Line (defender stance/discipline untraced) (`:75-100`). RC-4: no state between "eroding" and "routed" so Hannibal's ordered center withdrawal is inexpressible (design gap). RC-5 (low-medium, undiagnosed): nine single-subunit gauge rows (H2, H7, H8, H9, R1, R3, C1, C3, C5) fail off-band; only 4/20 rows pass (H1, C2, C6, C7) (`:102-116`).
  - Fix plan is evidence-gathering only: fix the ghost cell fixture; fix the float-epsilon pool floor; per-coupling ablation harness (8 toggle combinations); gauge-scale frozen-wings ablation; trace C4 vs C7; do not diagnose RC-5 (`:127-187`).
  - Jordan rulings recorded (`:319-357`): DG-3 = Option A (split the defender's pool symmetrically across pairs; accepted cost: full signed digest re-record of every gauge/mirror matchup with >1 pair); DG-4 = "Morale is blend of per-subunit as well as whole unit", operationalised by defaulting each subunit to its OWN starting morale at `build_army`/`build_envelopment`/`build_refused_flank` while `agg_morale()/derive_rout()/cascade_morale_hit()` already carry the whole-unit half.
  - Method discipline worth re-using: every contested fact re-verified against the working tree before adjudication; "confirmation, not just motion" (a mechanism must move, not only a band), and a gauge row landing in-band because a composition or magnitude was retuned does NOT count (`:426-442`).
- **Conflicts / stale:** At the tree (`modules/mass_battle/`): the epsilon floor fix is in (`orchestration.py:854-855` `math.floor(raw + 1e-9)`); per-subunit morale default is in (`armies.py:312-320` cites the DG-4 ruling). `POOL_VARIANT` is still the string "C-ii" (`config.py:27`), so whether DG-3 Option A is implemented under a new variant or not at all: [UNVERIFIED]. Gauge baseline numbers (single 2/20, multi 4/20) are 2026-07-04 snapshots; `gauge_mb.py` is referenced from `tests/sim/` and `systems/mass_battle/sim/workbench/trace.py` (the file's own location not checked). Paths `tests/sim/mass_battle/...` are the retired layout.
- **Open items:** DG-1 (pinning composition: majority pin / thin-and-yielding / status quo), DG-2 (fighting-withdrawal/yield mechanic), DG-5 (wing-timing, conditional on the frozen-wings result), RC-5's nine unexplained single-subunit rows, the C4-vs-C7 split, and the three-way confound of LC-8 + ED-1091 recoil + `PER_CELL` flip landing in one PR window.
