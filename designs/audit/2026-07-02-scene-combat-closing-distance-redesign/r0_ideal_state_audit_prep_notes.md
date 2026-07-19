# Ideal-state audit (prep for R1) — 2026-07-02

Jordan's framing: Phase B derived weapon physics for the IDEAL/optimal circumstance (full extension, natural
grip, unimpeded swing) and treated those as fixed values, rather than as the CEILING of a continuous function
that degrades under actual circumstances (closed range, altered grip, poor facing, shallow commitment).

## Already grip-position-aware (the model to extend, not rebuild)
- `systems.wield_heft(c,cfg)` — reads `WP.at_grip(c.w, grip_position)['I_g']`.
- `systems.recoverability_factor` / `systems._recovery_mode_commitment(w,g,cfg)` — reads `WP.at_grip(w,g)`'s
  I_g/S_g at the CURRENT grip position; also lunge_depth-aware.
- `systems.close_tempo` — reads `close_unwieldiness` scaled by `(1-grip_position)`.

## Confirmed static / ideal-state-only (candidates for R1 to make continuous)
- `weapon_physics.heft(w)` — `(m_head * max(0,PoB_frac)) / HEFT_REF`. No grip_position, no range/facing input.
  Feeds `core.heft_resp` → `core.strike()`'s Impact term. A choked-up thrust and a full-extension thrust
  currently deal IDENTICAL damage.
- `weapon_physics.percussion_authority(w)` — `PERC_SCALE*(sqrt(mass)*PoB_frac*energy_credit)^PERC_EXP`. Uses
  `derive(w)['PoB_frac']` (whole-weapon, as-issued), not grip-position-adjusted. No range check (a mace swung
  with no room to develop momentum should authority-scale down; currently doesn't).
- `weapon_physics.agility(w)` — `(AGILITY_REF/derive(w)['MoI'])^AGILITY_EXP`. Uses static whole-weapon MoI, NOT
  `at_grip`'s grip-position-adjusted I_g — inconsistent with wield_heft/recoverability_factor, which already
  made this exact correction. A gathered grip should read MORE agile; currently doesn't.
- `weapon_physics.defense_affinities(w)` — parry/dodge/wind, built on the static `agility(w)` above, so
  inherits the same gap.
- `systems.reach_base(c,cfg)` — `L0 + REACH_GEOM_SCALE*(head_len + REACH_2H_K*grip_len*hands2) + reach_adj`.
  COMPLETELY ignores `grip_position` — a fully choked-up spear reads the SAME reach as one held at full
  extension. This is likely the single biggest contributor to the 84-96% reach-weapon dominance: reach never
  shrinks even when the wielder has gathered in for close-quarters control.
- `systems.select_mode` / `systems.afforded_heads` — the `closed` parameter is passed into select_mode but
  never read in the function body (confirmed via grep). Mode AVAILABILITY does not degrade in tight quarters —
  a weapon can always select its full mode-set regardless of whether there's room to develop it.

## Approach-phase specific gaps (from the closing-distance investigation)
- `systems.approach_displace` gates on the weapon's STATIC `w['head']` field (`if longer.w['head']!='point'`),
  not the actually-SELECTED mode this exchange — stale relative to Phase B's own primitive-emergent mode
  system. Many new reach-dominant weapons (guisarme/ji/kama_yari/voulge, statically cut_thrust/curved_cut but
  carrying real point elements) never trigger the leverage-based deflection they should.
- No thrust-commitment/retraction-depth mechanic in the approach-phase stop-hit (`stophit_sigma`) — it's a flat
  per-beat probability, structurally separate from the closed-exchange's `commit_depth` Beta-distribution
  system. No "many shallow thrusts are weaker than one deep committed one" tradeoff exists during approach.
- No range-utilization concept anywhere — nothing checks whether the ACTUAL distance affords a weapon's full
  swing/thrust arc (the "greatsword can't be fully swung at 50cm" case).
- No facing/stance state exists at all (square vs bladed) — Combatant has no such field.
- No shield/buckler mechanic; no disarm/grab/pin mechanic; `clinch` (every weapon's 1-10 grappling-affinity
  field) has ZERO live readers anywhere in the engine — confirmed fully inert.

## Likely R1 architecture direction (not decided — R1's job, informed by R0 research)
A single new "how ideal are the current circumstances" continuous state (candidate name: effective range/
extension state), combining grip_position + actual measure/facing + commitment depth, threaded through heft/
percussion_authority/agility/reach_base/mode-availability as a shared degradation factor — rather than ad hoc
independent fixes to each function. Needs R0's grounding (esp. commitment_depth + facing_stance clusters)
before committing to the shape.

## Architectural placement (Jordan, 2026-07-02) — where this lives in the L0-L3 shape
- **Continuous circumstance derivations -> extend weapon_physics.at_grip, STAY IN L0, no new module.**
  `at_grip(w, g)` already IS the right pattern: a pure function of (weapon, one continuous circumstance
  parameter) returning a bundle of circumstance-adjusted dynamics (I_g, S_g, d_g, u) that L2 reads. Range-to-
  target and facing are just more circumstance parameters of the same kind. Extend toward
  `at_grip(w, g, range_gap, facing)` returning I_g/S_g PLUS a new `range_utilization` (and maybe
  `facing_mult`); rewrite heft()/percussion_authority()/agility()/reach_base() to read THAT bundle instead of
  computing off the static derive(w) directly — one shared source, not five independent patches. Keeps L0
  purity (weapon+circumstance only, no Combatant object).
- **Facing -> new Combatant per-beat state, not a new module.** Lives alongside grip_position/lunge_depth on
  the Combatant, mutated by wrapper.py's engagement loop the same way those already are.
- **Grab/pin -> a new L2 resolution SUBSYSTEM, not a continuous derivation.** Closer in kind to the existing
  bind_sigma/impose_node machinery (a distinct exchange outcome with its own win/escape logic) than to a
  physics quantity. New functions in systems.py alongside those + new branches in wrapper.py's state machine
  mirroring how bind/riposte/neutralize already work. Whether it's big enough to split into its own module
  (systems.py is already 650+ lines) is an R1 sizing call, not decided now.
- **Signature consequence to flag for R1:** heft()/percussion_authority() currently take just `w`; extending
  them to read the circumstance bundle means core.heft_resp/core.strike need grip/range/facing threaded through
  from the Combatant — the same threading wield_heft/recoverability_factor already do in systems.py. A real but
  contained signature change, not a new architectural layer.

## Rearward self-interference (Jordan, 2026-07-02) — a SPATIAL gap distinct from the mass/inertia one
Choking up (increasing g toward the CoM) makes the butt-end extend FURTHER behind the new working-hand position
(the original butt is at a fixed x; the hand slides forward by u, so the rearward extent from the NEW pivot
grows by u). Two SEPARATE physical consequences:
1. **Mass/inertia (swing dynamics)** — ALREADY CORRECT. Verified: `at_grip`'s `I_cm = I0 - m*PoB**2` then
   re-pivoting to `d_g = PoB - u` is the parallel-axis theorem applied properly; I_cm is the weapon's TOTAL
   inertia about its own CoM, so it already fully accounts for the rearward mass's contribution regardless of
   where the new pivot sits. No fix needed here.
2. **Spatial clearance (self-interference) — CONFIRMED MISSING.** The physical LENGTH now trailing behind the
   hand is a clearance problem independent of its mass/inertia contribution: it can strike the wielder's own
   body, an ally, terrain, or restrict footwork/turning. Nothing in the engine currently tracks "how much
   weapon length trails behind the working hand" as a distinct spatial quantity, separate from I_g/S_g. R1
   needs a new derived quantity for this (candidate: `rear_extent(w, g)` = the butt's distance behind the NEW
   grip position, growing with g/u) feeding into whatever penalizes cramped/close-quarters mobility (footwork,
   turning, closed_tempo, or the facing/footwork system depending on R0's grounding) — distinct from, and
   additive to, the existing MoI-based cost in wield_heft/recoverability_factor.
