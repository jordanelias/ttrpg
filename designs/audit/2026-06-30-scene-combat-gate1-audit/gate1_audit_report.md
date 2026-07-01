# Scene-Combat Engine — Gate-1 Architecture Audit (2026-06-30)

**Scope:** `designs/scene/combat_engine_v1/` (the 1v1 scene-combat engine, the GDScript port's oracle). **Method:** a 67-agent Workflow — 7 architecture-fidelity lenses (wrapper purity, L0 single-source, live hand-set primitive leaks, dependency direction, bottom-up emergence, dead/stale/contradiction, oracle/config/tests), each finding then re-checked by an independent adversarial skeptic (liveness re-traced, clause re-verified, severity/gate re-graded), then a completeness critic. Audits against the **REARCHITECTURE_v1.md** L0–L5 contract.

**Result:** 59 findings — **54 confirmed**, 5 refuted on adversarial review — plus 8 completeness gaps.

## Resolution status

| Gate class | Count | Status |
|---|---|---|
| behavior-preserving | 18 | **de-leak subset LANDED** (`250eefd7`); the rest are optional or by-design (see note) |
| cleanup | 10 | **safe subset LANDED** (`81850e85`); WP single-source duplicates kept (deferred) |
| re-baseline | 25 | **GATED (Jordan)** — change balance; deferred, see Decisions |
| build | 1 | **DEFERRED** — Phase-4 abilities-as-access |

**Specifically landed this session (byte-identical — the seeded 576-cell batch reproduces SHA `71c3bce9…`; `pytest tests/valoria` 65→73):**
- **`250eefd7` — wrapper de-leak completion.** Lifted the genuine inline σ/formula assemblies into pure
  `systems.*`: `stophit_sigma` (the approach net-σ, wrapper:99 — the dominant ~88% path), `init_emphasis_sigma`
  (:141), `counter_success_prob` (:206), `close_rate`, `consistency`, `mental_fatigue`, `poise_regen`,
  `bind_dominance_p`, `disrupt_resist_p`. Added `tests/valoria/test_combat_balance_guard.py` (the missing
  mirror-fairness + determinism guard).
- **`81850e85` — safe cleanup.** Deleted the dead STAGE-4 block + `K_REACH/K_HEFT/K_TEMPO/K_STRD` + config
  `HANDS2`; removed the dead `Combatant.reach`/`.weight` accessors; corrected the false "BUILD-ONLY / nothing
  reads STAGE 3/4" header and the misleading `MOI_AGILITY_K` "superseded" comment.

**NOT landed by design (per the adversarial ruling), though tagged behavior-preserving/cleanup:** the wrapper's
`stophit_p` / `neutralize` / `RIPOSTE_ON_*` gate-compositions and the bind-entry steal multiply (legitimate L3
orchestration, **refuted** as σ-leaks); the fatigue scalars / `beat_aside`-`slip_inside` (loop-local
orchestration); `systems` reading the injected `TR` facade (sanctioned pattern — the analogous `impose_node`
read was **refuted** as a layering violation); and `WP.reach()`/`authority()`/`armour_defeat_mode()` + the
`ability_armature.md` corrections (the single-source consolidation target + L5 model are Jordan-gated, below).

## Confirmed — behavior-preserving + cleanup class [28] (landed subset noted above)

| sev | gate | ack | layer | location | finding | fix |
|---|---|---|---|---|---|---|
| major | behavior- | new | cross | `test_combat_state_graph.py:1-82` | Three headline architecture claims (wrapper purity, single-source, no live hand-set leaks) have NO guarding... | Add (1) a wrapper-purity guard (e.g. ast/grep assertion that wrapper.py contains no ari... |
| major | behavior- | new | L3 | `test_combat_state_graph.py:54-68` | No mirror=50, byte-identical-no-ability, or de-leak behavior-preservation test exists | Add a seeded mirror test asserting /win_share - 0.5/ < tolerance over N fights, and a s... |
| major | behavior- | new | L3 | `wrapper.py:99` | Stop-hit net-sigma is assembled inline in the wrapper (a literal net-sigma build, the exact construct the g... | Move into a pure systems.stophit_sigma(longer, shorter, measure_gap, cfg) returning the... |
| major | behavior- | new | L3 | `wrapper.py:141` | Initiative/tempo-emphasis sigma 'init' is assembled inline, then fed to attack_sigma | Move into systems.init_emphasis_sigma(aggressor, defender, cfg, TR) and have attack_sig... |
| major | behavior- | new | L3 | `wrapper.py:206` | Counter-success probability 'succ' is assembled inline in the wrapper | Extract systems.counter_success_p(defender, cfg, TR); the wrapper applies the max/min c... |
| minor | cleanup | new | L0 | `weapon_physics.py:19-21` | weapon_physics.py module header still claims STAGE 3/4 is BUILD-ONLY and nothing live reads it — false afte... | Rewrite the header: STAGE 2/3/3b ARE now live consumers (defense_affinities via mode_si... |
| minor | cleanup | new | L0 | `weapon_physics.py:235-248` | STAGE-4 consumer terms reach_term/heft_term/tempo_penalty/strdemand_term are dead — the live consumers reim... | Either delete the four STAGE-4 functions (the live consumers diverged and own the g-awa... |
| minor | cleanup | deferred | L0 | `weapon_physics.py:124-132, 151-166` | WP.authority(), WP.reach(), WP.armour_defeat_mode() are dead outside __main__ (the live reach path is syste... | Mark these explicitly build-only/diagnostic, or delete reach()/authority()/armour_defea... |
| minor | behavior- | new | L0 | `weapon_physics.py:45, 178` | MOI_AGILITY_K comment says 'superseded... kept until the wiring deletes it' but it is still LIVE in defense... | Fix the comment: MOI_AGILITY_K is no longer in the agility formula but is still the liv... |
| minor | cleanup | new | L3 | `combatant.py:43-48` | Combatant.reach and Combatant.weight accessors return categorical hand-set fields ('long'/'short', 'light'/... | Delete the .reach and .weight properties (dead categorical accessors); keep .head (a pr... |
| minor | behavior- | new | L4 | `ability_armature.md:8, 47, 49-62, 170` | ability_armature.md STATUS CORRECTION still claims the channel levers are wired and eff_cw consumed at ~9 s... | Update armature §2.2/§2c/§7 and the STATUS CORRECTION: there is no channel-weight subst... |
| minor | cleanup | deferred | L5 | `ability_armature.md:108, 133, 169` | ability_armature.md §5 marks vorschlag and sen_no_sen as '✅ built', but neither exists in ABILITIES and the... | Correct armature §5 (German/Japanese tables) and §7: vorschlag/sen_no_sen are NOT built... |
| minor | cleanup | deferred | L0 | `weapons.py:57 (spear pob_frac=0.0 with the comment claiming recoverability_factor still reads it)` | spear pob_frac=0.0 legacy field is now inert for spear (point head skips p_auth) but the field's presence a... | Two debts in one line: (1) the pob_frac column is now read live ONLY by core.p_auth for... |
| minor | behavior- | new | L2 | `systems.py:271-279, 318-330, 372-386, 388-403, 413-429` | L4 tradition logic (TR) executes inside L2 pure subsystems on live per-beat paths | The contract's uniform L2 signature is (aggressor, defender, state, cfg[, rng]) with NO... |
| minor | behavior- | deferred | L1 | `core.py:34-38, 126` | core.p_auth: L0 weapon-physics derivation living in the L1 resolver | Delete core.p_auth; have core.strike consume WP.percussion_authority (already on the bu... |
| minor | behavior- | deferred | L1 | `core.py:34-38, 126` | core.p_auth reads hand-set pob_frac on the live damage path | Delete core.p_auth; call WP.percussion_authority(attacker.w) (which derives PoB_frac in... |
| minor | cleanup | deferred | L3 | `combatant.py:43-48` | Combatant.reach (categorical string) and Combatant.weight (wt class) are dead accessors with no live caller | Delete the two dead properties (and the categorical `reach`/`wt` fields from weapons.py... |
| minor | cleanup | deferred | L0 | `weapon_physics.py:239-240` | weapon_physics.heft_term (the L0 MoI-based heft) is dead — zero live callers | Either wire the damage-path heft to WP.heft_term (closing the single-source gap and ret... |
| minor | behavior- | new | L3 | `wrapper.py:88-89` | close_rate is a multi-term rate formula computed inline in the APPROACH path | Extract systems.close_rate(shorter, longer, ffat_shorter, displ, rt, cfg) (or fold disp... |
| minor | behavior- | new | L3 | `wrapper.py:142` | consistency_a sigma term computed inline and passed to attack_sigma/read_contest | Move into systems.consistency_sigma(aggressor, cfg) (one line) and call it from attack_... |
| minor | behavior- | new | L3 | `wrapper.py:55,132-135` | Fatigue scalars (ffat, fat_a, fat_d, cfrac_d, mental_fat_d) derived inline in the wrapper | Provide systems.fatigue(c) and systems.mental_fatigue(defender, cfg) helpers; the wrapp... |
| minor | behavior- | new | L3 | `wrapper.py:64-65` | Per-beat poise recovery embeds a Focus-scaled recovery formula inline | Extract systems.poise_recovery_delta(c, cfg) returning the increment; the wrapper does ... |
| minor | behavior- | new | L3 | `wrapper.py:272,282` | Inline logistic probabilities for bind dominance and riposte-disrupt | Add systems.bind_win_p(bsig) and systems.disrupt_complete_p(aggressor, cfg) (or return ... |
| minor | behavior- | new | L3 | `wrapper.py:191,198,201` | Probability composition inline: RIPOSTE_ON_FAIL+overcommit and neutralize-NEUTRALIZE_OVERWHELM_DROP | Move the probability composition (riposte_p(cfg, overcommit_exposure), neutralize_overw... |
| minor | behavior- | new | L3 | `wrapper.py:264` | Bind-entry initiative-steal amount g assembled inline (parallel to the extracted indes_steal_amount) | Extract systems.bind_steal_amount(bw, cfg, TR) for symmetry with indes_steal_amount; th... |
| minor | behavior- | new | L3 | `wrapper.py:228-230` | beat_aside / slip_inside exploit predicates encode threshold business logic inline | Extract systems.can_beat_aside(defender, aggressor, cfg) and systems.can_slip_inside(de... |
| cosmetic | cleanup | deferred | L3 | `config.py:4` | config HANDS2 is build-only — read only by the dead WP.reach_term; the live reach uses REACH_2H_K | Drop HANDS2 (and the dead WP.reach_term/HANDS2 pair together), or annotate as diagnosti... |
| cosmetic | cleanup | new | L0 | `weapon_physics.py:175 (cross_section default 0.6), 180 (blade_guard default 0.4), 182 (hand_guard default 0.4)` | defense_affinities defaults (cross_section 0.6, blade_guard 0.4, hand_guard 0.4) silently fabricate primiti... | Replace the silent .get(...,default) with a required-key read (or a build-time assert t... |

## Confirmed — GATED on Jordan (re-baseline; change balance) [25]

| sev | gate | ack | layer | location | finding | fix |
|---|---|---|---|---|---|---|
| major | re-baseli | deferred | L1 | `core.py:34-38` | core.p_auth duplicates WP.percussion_authority with a hard-coded constant and reads the legacy hand-set pob... | Per the worklist, MOVE core.p_auth to weapon_physics (call WP.percussion_authority from... |
| major | re-baseli | deferred | L0 | `weapon_physics.py:136-148 (clamp at 148); consumed live at systems.py:181 (dodge) -> 165 (mode_sigma cap) -> wrapper.py:153/161` | agility min(1.0,..) FIAT clamp collapses the entire light-weapon dodge spread on the LIVE defence path | The docstring itself flags this as a Phase-3b blocker. Re-anchor AGILITY_REF at/below t... |
| major | re-baseli | new | L0 | `weapon_physics.py:45 (definition, marked superseded); 178 (live use in lever_norm); reaches the engine via systems.py:165 mode_sigma 'wind' cap` | MOI_AGILITY_K=6.0 ('superseded... kept until the wiring deletes it') is load-bearing LIVE inside defense_af... | The 'superseded' comment is misleading: the power law replaced this constant ONLY for a... |
| major | re-baseli | deferred | L1 | `core.py:38 (p_auth reads w.get('pob_frac',0.15)); live via strike line 126 -> damage line 109 (blunt branch)` | Blunt damage authority (core.p_auth) reads the hand-set pob_frac, not derive()['PoB_frac'] — a live aggrega... | core.p_auth duplicates weapon_physics.percussion_authority but on the LEGACY pob_frac i... |
| major | re-baseli | deferred | L2 | `systems.py:46 (w['spd'] live in weapon_tempo); called every beat at wrapper.py:69-70` | weapon_tempo reads the hand-set spd aggregate LIVE; derived agility is never wired to tempo — the 'fixes th... | This is the acknowledged wt/spd residual, but confirmed still fully live and on the dec... |
| major | re-baseli | deferred | L1 | `core.py:51-62 (heft_resp reads w.get('wt')); live via strike line 125 -> damage line 109 (non-blunt branch)` | Cut/thrust damage impact (heft_resp) reads the binary hand-set wt class LIVE, defeating within-class mass e... | wield_heft (systems.py:24, derived from WP.at_grip I_g) already exists and is wired to ... |
| major | re-baseli | deferred | L2 | `config.py:40` | ADEF_THRESHOLD is non-monotonic in armour tier, contradicting armor_defeat_sigma's docstring | Re-sweep ADEF_THRESHOLD against the harness to a monotone-rising set (cloth < mail < pl... |
| major | re-baseli | deferred | cross | `combat_config.gd:53-58` | Godot combat_config.gd hand-corrects adef_threshold away from the oracle (port 'fixes' canon) | Revert the port to mechanically mirror config.py, OR (preferred) land the monotone re-s... |
| major | re-baseli | deferred | cross | `core.py:34-38` | Percussion authority is derived twice on live paths (hand-set pob_frac vs derived PoB_frac), breaking singl... | Make core.p_auth delegate to WP.percussion_authority (single source), removing the hand... |
| major | re-baseli | deferred | L1 | `core.py:51-62, 125` | core.heft_resp reads the binary wt class as base even under live HEFT_MODE='continuous' | Per HEAD's own note (systems.py:29-30, config.py:87 'damage-impact path keeps heft_resp... |
| major | re-baseli | deferred | L2 | `systems.py:46` | systems.weapon_tempo reads hand-set spd every beat | Replace `w['spd']*SPEED_K` with a derived cadence term from WP.agility(w) (the MoI^-0.2... |
| major | re-baseli | new | L2 | `systems.py:76` | systems.str_demand reads the hand-authored hand-difficulty class (Forgiving/Standard/Demanding) every beat | Replace `D_HAND*HANDLE_RANK[w['hand']]` with the derived WP.strdemand_term(w) (K_STRD*s... |
| major | re-baseli | deferred | L0 | ` weapon_physics.py:core.py:34-38; weapon_physics.py:108-114` | Percussion authority derived twice with DIFFERENT inputs: core.p_auth reads hand-set pob_frac, WP.percussio... | core.p_auth is the exact case CLAUDE.md §6 warns of ('Phase-3b retires hand-set percuss... |
| major | re-baseli | deferred | L1 | `core.py:34-38` | core.p_auth is L0 weapon-physics living in the L1 core engine (worklist says it must move) | Move p_auth out of core.py: have core.strike call WP.percussion_authority. Folds into p... |
| major | re-baseli | deferred | L1 | `core.py:51-62` | core.heft_resp is L0 heft physics in L1 core; third independent heft derivation reading hand-set wt | Heft is derived three ways: a derived MoI form (WP.heft_term, dead), a derived g-aware ... |
| minor | re-baseli | deferred | L0 | `weapon_physics.py:184-186; output consumed live at systems.py:165` | _band() hard-clips parry/dodge/wind into the retired GATE's [0.4,1.0] window — multiple weapons saturate at... | The lo/hi window bounds (parry 0.55-1.0, dodge 0.2-0.95, wind 0.05-0.45) and the 0.4+0.... |
| minor | re-baseli | deferred | L0 | `weapon_physics.py:182 (parry uses min(1.0, ag/0.6)); live via systems.py:165` | The agility FIAT clamp additionally flattens the live PARRY affinity for every light weapon (ag/0.6 saturat... | Same root cause as agility-fiat-clamp: once AGILITY_REF is re-anchored so the cap stops... |
| minor | re-baseli | deferred | L0 | `systems.py:46` | Hand-set aggregate w['spd'] read live in systems.weapon_tempo (L0 aggregate -> L2) | Phase-3 swap: route tempo's speed term through WP.agility (MoI-derived). Acknowledged r... |
| minor | re-baseli | deferred | L0 | `core.py:57-62, 125` | Hand-set aggregate w['wt'] read live in core.heft_resp (L0 aggregate -> L1) | Worklist explicitly defers this ('the damage-impact path keeps heft_resp pending the wt... |
| minor | re-baseli | new | L1 | `core.py:14-24` | core.degree [AUDIT-FIX] continuity correction silently diverges from the discrete r1 oracle it claims to share | Either land the ER-2 continuity correction into r1 canon (so the single oracle carries ... |
| minor | re-baseli | deferred | L0 | `config.py:81-83` | Recovery/heft [FIAT] gains and the agility clamp are owned-in-prose but untracked by any closure gate or test | These are correctly acknowledged_deferred and prose-owned; the gap is the absence of a ... |
| minor | re-baseli | deferred | L0 | ` weapon_physics.py:systems.py:19-21; weapon_physics.py:158-166` | Reach forward-extent derived in two places: live systems.reach_base vs dead WP.reach() | The Phase-3b 'reach wired to geometry' claim is HALF-DONE: the geometry-derived reach l... |
| minor | re-baseli | deferred | L0 | `weapon_physics.py:158-166` | weapon_physics.reach() is dead (zero live callers) despite being the contract's single basis | Either wire systems.reach_base to WP.reach() (closing the single-source gap) or, if sys... |
| minor | re-baseli | deferred | L0 | `weapon_physics.py:234-248` | The entire STAGE-4 consumer-term block in weapon_physics is dead (reach_term, heft_term, tempo_penalty, str... | The STAGE-4 block is the un-executed Phase-3 wiring target. Either complete the wiring ... |
| minor | re-baseli | deferred | L0 | `weapon_physics.py:151-155; 124-132` | weapon_physics.authority() and armour_defeat_mode() are dead (only the self-test calls them) | armour_defeat_mode duplicates the live head-routing logic in core.coupling + systems.ad... |

## Confirmed — DEFERRED (build) [1]

| sev | gate | ack | layer | location | finding | fix |
|---|---|---|---|---|---|---|
| major | build | deferred | L5 | `ability_armature.md:12-13, 86-94` | ability_armature.md encodes the OLD 'Modulate, never unlock' channel-weight model — directly contradicts RE... | Add a supersession banner to ability_armature.md flagging that Principle 1 ('Modulate, ... |

## Refuted on adversarial review (recorded so they are not re-raised)

- **stophit_p probability is composed inline in the wrapper** (`wrapper.py:94`) — Re-traced liveness: fight() (wrapper.py:318) -> engagement() -> approach block `if not closed:` (line 85) -> line 94 stophit_p assignment -> line 97 `if rng.random() < stophit_p`. Code IS on the live path (the approach/stop-hit mechanic is ~88% of interactions per HANDOFF). really_live=true.
- **neutralize mode-shape selection inline (likely ALLOWED — config lookup, flagged for completeness)** (`wrapper.py:189`) — Re-opened wrapper.py and confirmed line 189 verbatim: `neutralize=cfg['NEUTRALIZE_PARRY'] if mode=='parry' else (cfg['NEUTRALIZE_DODGE'] if mode=='dodge' else cfg['NEUTRALIZE_WIND'])`. Liveness CONFIRMED: line 189 sits inside engagement() (def at wrapper.py:29), in the per-beat outcome-mapping bo...
- **agility() is single-source (one derivation, one internal consumer) — the FIAT clamp is the live defect, not duplication** (`weapon_physics.py:136-148`) — Re-traced the full caller chain from the live fight loop. engagement() (wrapper.py:29) -> S.read_contest (wrapper.py:153) -> mode_sigma per mode (systems.py:384) -> cap=WP.defense_affinities(defender.w)[mode] (systems.py:165) -> ag=agility(w) (weapon_physics.py:177) -> dodge=ag*onehand (line 181)...
- **NON-LEAK: w['gap'] reads consume a geometry-baked value, not a hand-set field** (`weapons.py:81-87; consumed core.py:126, systems.py:197-198`) — Re-traced all cited paths and independently corroborated the finding's core claim: w['gap'] is a geometry-DERIVED coefficient, NOT a hand-set aggregate, so there is no leak. Evidence: (1) Grep for `gap=` over weapons.py returns ZERO literal assignments in any WEAPONS record — confirmed. The only ...
- **systems.impose_node reads L4 PREFERRED/preferred() directly (tradition-name routing in L2)** (`systems.py:236-249`) — FACTS CONFIRMED, CLAUSE VIOLATION REFUTED. Liveness is real: engagement() (wrapper.py:29, the live entry) -> wrapper.py:216-217 guards `if cfg.get('IMPOSITION_GATE')` and config.py:147 sets `IMPOSITION_GATE=True`, so `S.impose_node(aggressor, defender, hit, bind, riposte, cfg, rng, TR)` runs by d...

## Completeness-critic gaps

- **[major/L4]** eff_cw collapsed to a constant 1.0, but ~18 live call-sites still compute eff_cw ratios/products as if traditions differentiate there — dead computation masquerading as the bottom-up tradition channel
- **[minor/L0]** geometry.bake derives thrust_factor and cut_factor for every weapon, but NEITHER coefficient is read anywhere on any path — two of the four derived coefficients in the 'single complete surface' are dead
- **[minor/L0]** geometry.py's stated CALIBRATION DISCIPLINE is 'reproduce the already-validated top-down values' — the derivation is fit to a hand-validated tier list, inverting the bottom-up emergence contract
- **[minor/L4]** The imposition gate is the ONLY live tradition differentiator besides familiarity, yet its single call-site comment says 'default off' while config ships it ON — and the whole tradition layer's effect collapses to two narrow mechanisms
- **[minor/L3]** state_graph.INJECTION_POINTS encodes hardcoded wrapper.py line numbers as data, and several no longer match the live wrapper — the WS-1 bridge is doc-as-data drift no test catches
- **[minor/L0]** GEOMETRY is rebuilt as a parallel name-keyed view of data that already lives inside WEAPONS[w]['geometry'], and combatant.py re-exports both — two access paths to the same primitives, one of which the single-source rule says shouldn't exist
- **[cosmetic/L0]** Baked gap silently OVERWRITES whatever ['gap'] a weapon record might carry (none do today), and the only thing preventing a hand-set/baked collision is the absence of the key — no test or assert guards it
- **[major/cross]** The 'cycle-free dependency / wrapper-owns-mutation' architecture claims are verified by NO test — state_graph tests are graph-shape only and never assert layering, mutation-ownership, or import-acyclicity

## Decisions for Jordan (the re-baseline / design-laden remainder)

These change balance numbers or encode a design call, so they are **not** resolved unilaterally:

1. **Single-source the percussion authority (`core.p_auth` vs `WP.percussion_authority`).** They read DIFFERENT inputs — `core.p_auth` the hand-set `pob_frac`, `WP` the derived `PoB_frac` — diverging up to Δ0.359 (poleaxe 0.091 vs 0.450) on the live damage path. Consolidating onto the derived value re-baselines blunt damage. Ties to **ED-1050** (combat parity oracle) and the **D-A lethality** call.
2. **`wt` / `spd` damage-path de-leak.** `core.heft_resp` (damage impact) reads the binary `wt` class and `systems.weapon_tempo` reads hand-set `spd` every beat — route to derived MoI/agility. Re-baseline.
3. **The agility `min(1.0,…)` FIAT clamp + `_band` re-clipping.** Collapses the light-weapon dodge/parry spread (dagger=arming=sabre=half-sword pin to 1.0) and re-imposes the retired GATE's [0.4,1.0] window — emergence is partly cosmetic. Re-anchor `AGILITY_REF` below the lightest MoI (or drop the cap + renormalise).
4. **`ADEF_THRESHOLD` non-monotonicity** (`{none:0, light:0.70, medium:0.45, heavy:0.72}` — light>medium) contradicts the 'rises monotonically with armour' contract; the Godot `combat_config.gd` already hand-corrects it away from the oracle. Fix `config.py` in canon (never let the port correct its oracle). **ED-1050.**
5. **Abilities-as-ACCESS (Phase-4).** The live `ability_primitives.py` is still the `+`/`*` MODULATOR model that REARCHITECTURE L5 and `ability_armature.md`'s own principle say to replace; `eff_cw` is a near-no-op (returns 1.0 by default) threaded through ~18 live sites as dormant scaffolding. Phase-4 build.
6. **Single-source consolidation target (`WP.reach()`/`authority()` vs `systems.reach_base`/`wield_heft`).** Decide whether the canonical derivation lives in `weapon_physics` (wire consumers to it) or stays in `systems` (retire the WP duplicates). Currently both exist in parallel.

_Audit data: `tasks/w6xkf9jtl.output` (this session). Adversarial verification refuted 5 over-claims, confirming the guard works — including correctly ruling that `w['gap']` is geometry-DERIVED (not a leak), and that the wrapper's `stophit_p`/`neutralize`/RIPOSTE gate-compositions are legitimate L3 orchestration, not sigma-assembly._