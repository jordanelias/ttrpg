# Coverage Matrix — Weapon System v2 (Active)

Archived entries in tests/coverage_matrix_archive.md
## Smooth command-sigma combat pool + continuous discipline penalty (2026-06-15, ED-1013)
- CANONICAL BASIS: Jordan directive 2026-06-15 'smooth pools / fix discipline' (path 1 of documented fork).
- base_combat_pool COMMAND_SIGMA branch: flat 2*Command -> Command*(1 + hp/hp_max) -- 2*Command at full
  strength (size-decoupled, ED-899 preserved; cohesion is a FRACTION so per-capita effectiveness stays
  size-independent, Lanchester exponent ~1), degrading smoothly to Command at annihilation.
- discipline_penalty(): tiers {0,-1,-2} -> continuous -(5-disc)/2 clamped [-2,0] (same endpoints, no step).
- WHY: the flat pool left the discipline STEP as the sole pool-degradation term, which amplified a tiny
  latent contact-geometry asymmetry into a side-B mirror bias (H1 62/38, |A-B|=21.7pp). The smooth
  own-casualty degradation dilutes the discipline term -> mirror side-symmetric.
- VALIDATED: H1 Line-Line mirror n=120 A=53%/B=47% decisive, |A-B|=3.3pp (was 21.7); command decisive
  (cmd6-vs-2 -> 40-0); discipline decisive (disc5-vs-disc2 -> 20-0); mechanics_selftest clean.
- COVERAGE IMPACT (Jordan-accepted trade-off): smooth pool reduces FORMATION/charge decisiveness; the
  historical gauge tests/sim/gauge_mb.py (precedents_warfare.md bands) is now STALE and needs
  RE-CALIBRATION to the smooth engine (in-band dropped flat 3/6 -> smooth 1/6 on the 6-test subset).
  FLAGGED as a separate Jordan-canon follow-up.

## 2026-06-15 — Mass-battle gauge recalibration (ED-1014) [resolves the ED-1013 gauge-staleness flag]
- tests/sim/gauge_mb.py recalibrated bottom-up from historical precedent + peer-reviewed academic military
  analysis (grounding doc: references/historical/mass_battle_gauge_grounding.md). Bands set by HISTORY, the
  engine validated against them -- a fail FLAGS engine divergence, it does not lower the band.
- METRIC: raw-A% -> DECISIVE SPLIT decA=A/(A+B) (raw-A% failed symmetric mirrors purely on draw rate); the
  draw rate is validated separately (draw_exp). Near-parity high-draw is analytically expected (Hillestad 1995
  NRL 42(2); Taylor 1979/1983; Lanchester tie Armstrong&Sodergren 2015).
- VALIDATION (smooth engine, multi, n=120): 9/20 VALIDATED (mirrors; envelopment foot+mounted C4 93.8%, C7
  86.7%; command-decisive; maniples-absorb-wedge; misconception-corrected C1 45.7%). 6 DIVERGE-soft (subtle
  formation edges washed by the ED-1013 cohesion pool -- defensible per Biddle/Burkholder, below the v9 A.6
  modest edge). 3 DIVERGE-hard ENGINE-DEFECT FLAGS left FAILING: C2/C6 braced foot never beats cavalry (brace
  under-repels); C5 morale-shock inert (decA identical to C1). R1 ranged too-drawish open-field; R3 ranged
  mirror unresolvable; single-mode all-draws (18-tick cap).
- C1 REBASELINE 52-80 -> 35-55: the old band encoded the cavalry-beats-unprepared-infantry misconception
  (Burkholder 2007). Engine-defect flags (frontal cav shock/brace/morale flat) are future-work, not bands.
- Jordan directive 2026-06-15 (bottom-up recalibration, repeated); Jordan-vetoable.

## 2026-06-16 — Mass-battle gauge cavalry construction fix (ED-1015) [corrects the ED-1014 C2/C5/C6 "engine-defect" flags]
- RE-DIAGNOSIS (bottom-up, reading mass_battle/resolution.py + orchestration.py + config.py): the 3 ED-1014
  DIVERGE-hard cavalry flags (C2/C5/C6) were NOT engine defects -- they were GAUGE-CONSTRUCTION defects. The
  engine's brace-recoil (PC_CHARGE_RECOIL, calibrated vs Courtrai/Swiss/Waterloo) and shaken-shock
  (PC_SHOCK_SHAKEN_GAIN) are already grounded + WIRED; the gauge was not triggering them. Engine UNTOUCHED.
- FIX (gauge only): make_unit gains morale_start=None + instructions=() with byte-exact defaults (the 13 H/R
  rows + C1/C3/C4/C7 unchanged; H1 identical 52.8). C2/C6 defenders carry instructions=('brace',) ->
  _unit_braced fires the reciprocal recoil -> the braced wall REPELS. C5 is morale 2 of morale_start 6 ->
  genuinely shaken ("shaken" is RELATIVE, du Picq) -> shaken-amplifier + _morale_sigma fire.
- METRIC: C2/C6 judged on RAW cav-a LOW (band 0-30), draws expected (a repulse is a HOLD; decisive-split
  saturates at a tiny decisive n). Optional 10th tuple field metric='rawA' added (default 'decA').
- BANDS (history-grounded, Jordan-vetoable): C5 ceiling 90->98 (cavalry vs disordered foot is NEAR-TOTAL --
  Boddy 2015 dispersed 15,000; Hastings post-feint; the Phase-2 ceiling was set when the shock was inert);
  C7 ceiling 90->100 (encirclement of an immobile hold-stance line is annihilating -- Cannae; decA saturates
  to 100 when infantry is shut out).
- VALIDATION (multi, n=120; C5 re-checked n=240): cavalry block 7/7 -- C1 contested 45.7 OK, C2 REPELLED (raw
  cav-a 1.7), C3 mirror 43.7 OK, C4 envelop 93.8 OK, C5 shaken 95.6 (94.8@n=240) OK, C6 REPELLED 1.7, C7
  envelop 100.0 OK. Differentiation EMERGENT: braced-repulse ~2% != contested ~46% != shaken-shock ~95% !=
  envelopment ~94-100% (this validates the ED-1014 C1 rebaseline by differentiation). gauge_mb.py: 0 uncited
  constants, mechanics_selftest (True,[]).
- LATENT FLAG (out of scope, not triggered): the charge-recoil (orchestration ~L1647) does not zone-gate -> a
  flank/rear charge into a braced unit wrongly fires the recoil; C7 uses hold-only to avoid it. Fix candidate:
  gate on the frontal (GREEN) zone. The 6 formation soft-divergences (H2/H4/H5/H6/H7/H9) remain a separate residual.
- Jordan directive 2026-06-16 ('for 1/2/3 do everything you can to fix everything from a bottom-up emergent
  approach'); implemented by Claude, Jordan-vetoable.
- ED-1016 (per-subunit stat derivation, Jordan directive 2026-06-16; per-subunit pool option 1, "intensive
  attention to detail"): pushed power/discipline/morale/morale_start/dr onto Subunit (OPTIONAL; None inherits
  parent Unit via _unit back-ref), added per-subunit cohesion + subunit_combat_pool (SHARED command, per-subunit
  discipline+cohesion, shared stamina), repointed the engagement pool + Lanchester casualty power/dr +
  charge-shock/brace-recoil/morale sigma + Phase-2 volley (power/discipline/eff_size) to the contacting subunit's
  effective stats; Unit derives agg_power/discipline/morale/dr (troop-weighted) atop existing HP=Size=Sum(subunits).
  BYTE-EXACT verified vs a CLEAN pre-edit engine across melee/cavalry/brace/morale AND ranged/volley (exact states +
  win-rates identical) -- single-subunit fast-paths (cohesion->hp/hp_max, eff_size->effective_size) + None-inheritance
  guarantee the homogeneous historical battery is untouched. Mixed-unit differentiation demonstrated: cavalry subunit
  P6/D6 pool 8 vs infantry subunit P4/D4 pool 7, carried into the combat trace. Added make_mixed_unit gauge constructor
  (make_unit unchanged). V1 SCOPE: per-subunit combat morale uses the subunit's nominal value for overriding subunits;
  the eroding morale pool + rout + discipline degradation stay UNIT-level. Implemented by Claude, Jordan-vetoable.
- ED-1017 (per-subunit stamina, Jordan directive 2026-06-17; mirrors ED-1016): pushed stamina onto Subunit as OPTIONAL
  fields (stamina/stamina_max; None inherits parent Unit via _unit back-ref), added eff_stamina/eff_stamina_max +
  drain_stamina/recover_stamina (write routing: own-if-set else inherited Unit -> single-subunit reproduces the old
  Unit.stamina arithmetic) + agg_stamina (troop-weighted). Repointed per-subunit: subunit_combat_pool penalty
  (atom.eff_stamina), base_combat_pool (self.agg_stamina), the per-tick contact drain (each engaged subunit drains by its
  own cells-in-contact; reserves do not drain), phase-boundary recovery (stamina_check via new per-subunit _subunit_depth),
  between-turn recovery, and the exhaustion-pressure morale read. _fatigue_sigma UNCHANGED (its call site already passes the
  engaged subunit's contact columns -> already sub-unit-scoped; an atom param would be unused apparatus, NERS-E). BYTE-EXACT
  vs a CLEAN pre-edit engine across 9 matchups (melee mirror/asymmetric/envelopment, ranged/volley, cavalry charge/braced/
  envelopment/shaken) x 20 seeds in the resolving multi-turn mode -- identical state-vector digest. Rotation demonstrated:
  an engaged front subunit drains to 32/100 while a held reserve stays 100/100 (divergence impossible under shared
  Unit.stamina); the fresh reserve yields +1 combat-pool die over the exhausted front. make_mixed_unit extended for
  per-subunit stamina (make_unit unchanged). Grounding (references/historical/mass_battle_gauge_grounding.md §6): Sabin 2000
  JRS line relief / supporting troops; Zhmodikov 2000 Historia; du Picq Battle Studies; Clausewitz On War III.12. V1 SCOPE:
  per-subunit rout + eroding morale/discipline stay UNIT-level (deferred, Jordan-vetoable). Implemented by Claude, Jordan-vetoable.
- ED-1018 (troop-taxonomy stat home, Jordan directive 2026-06-17): wired the troop taxonomy onto the per-subunit stats
  (ED-1016/ED-1017). Added orchestration.TROOP_TYPE_STATS -- canonical per-type Power/Discipline/Morale presets transcribed from
  mass_battle_v30 B.2, keyed to the existing TROOP_TYPE_ROLES snake_case taxonomy (levy, light_infantry, heavy_infantry,
  cavalry, archers, crossbow, sling, artillery, knights_templar) -- plus orchestration.stats_for(troop_type) (case-insensitive
  accessor mirroring roles_for; fresh dict or None) and the constructor Subunit.of_type(troop_type, shape, tier,
  starting_position, **kw), which fills power/discipline/morale/morale_start from the preset unless the caller overrides;
  an unknown type fills nothing so fields stay None and inherit the parent Unit. PURELY ADDITIVE: nothing that does not call
  of_type changes, so the gauge constructors (make_unit/make_mixed_unit) are untouched and single-subunit units stay
  BYTE-EXACT (9-matchup x 20-seed multi-turn battery digest unchanged: fe99574610caca44052509beb8c0b81a1b3d1972c6a3c8e3513e38933ef27c69).
  SCOPE: only the three unambiguous B.2 integers are mapped; dr (the Armour column -> a vs-Piercing DR scale at orch L413-417
  whose identity with Subunit.dr is unconfirmed) and stamina (the Endur column, no clean bridge to the 0-100 pool) are
  deliberately left to inherit and flagged, not guessed; unit_type (melee vs ranged) stays caller-controlled (a role, not a
  stat). Differentiation demonstrated: of_type reproduces every B.2 row exactly; the stats separate combat on both channels --
  pool via discipline (Levy 6 dice -> Cavalry/Knights Templar 8) and damage via the (1+Power) multiplier (Levy x2 -> Cavalry
  x6); caller overrides beat the preset; unknown types inherit the Unit. Grounding (references/historical/
  mass_battle_gauge_grounding.md §7): the canonical B.2 table itself (bottom-up); Sabin Lost Battles 2007 validated
  ancient-battle model rating units by type and quality, plus the settled heavy/light/missile distinction (top-down).
  Implemented by Claude, Jordan-vetoable.
- ED-1019 (per-subunit rout + eroding morale/discipline, Jordan directive 2026-06-17 + "Continue" confirm; completes
  the per-subunit lifecycle after ED-1016 stats / ED-1017 stamina): pushed rout, morale erosion, and discipline
  degradation from the Unit onto the Subunit so a section of the line breaks from its OWN casualties while a fresh
  sibling holds. (SUBUNIT_ROUT_FLOOR was a dead config stub -- defined/exported/never referenced; this is the
  per-subunit rout it pointed at.) New Subunit fields routed/broken/discipline_start; props/methods eff_discipline_start,
  erode_morale, degrade_discipline, restore_discipline (write-routed own-else-inherited-Unit -> single-subunit
  reproduces the old unit arithmetic); Unit methods derive_rout + cascade_morale_hit. Repointed per-subunit:
  morale_check_phase (each subunit erodes by its OWN cohesion + own stamina/discipline exhaustion), rout_resolution
  (each subunit routs at own eff_morale<=0, then derive_rout), discipline_check_phase (unit-loss asymmetry drives a
  per-subunit counter), reform_check (flag OFF), the run-loop rout trigger, the per-tick drain (routed subunit skipped),
  subunit_combat_pool (routed/broken subunit -> 0), and the multi-unit inter-unit cascade / flank-erosion morale hits
  (cascade_morale_hit hits the unit's inherited-default morale ONCE plus each own-morale subunit -> no double-count on
  homogeneous units). TWO CANON-STRUCTURE FORKS, Jordan-vetoable: (a) unit-rout DERIVED (agg morale 0 / all subunits
  routed / Command<=0; winner/pursuit/cascade keep keying on derived unit.routed -> spec's unit-level rout preserved);
  (b) NO intra-unit cascade added (A.12 cascade stays inter-unit per spec, though its "section of the line breaks"
  Cannae/Hastings rationale could justify intra-unit -- a canon-model change left for Jordan). NO mass_battle_v30 edit.
  BYTE-EXACT: 9-matchup x 20-seed multi-turn battery digest unchanged (fe99574610caca44052509beb8c0b81a1b3d1972c6a3c8e3513e38933ef27c69).
  Per-subunit rout demonstrated: a 2-subunit unit (heavy front + levy rear) with the rear gutted to ~18% eroded the
  rear's morale to 0 over 2 phases (cohesion 0.18 -> -2/phase) while the front held at 5.0 (cohesion 1.0); rout_resolution
  routed the rear only (rear.routed=True, front.routed=False, UNIT.routed=False -- line held), rear pool -> 0 while front
  kept 7 dice; breaking the front too routed the unit (derive_rout). Single-subunit routs exactly at morale 0 as before.
  Grounding (references/historical/mass_battle_gauge_grounding.md S8): A.12 Cannae/Hastings sectional collapse; du Picq
  Battle Studies (panic is local, spreads from a break). Implemented by Claude, Jordan-vetoable.

- **ED-1020** (bugfix -- per-subunit broken-state scope; ED-1019 follow-up). Per-subunit stress testing
  (tests/sim/mass_battle/test_persubunit_stress.py) caught subunit_combat_pool flagging the WHOLE unit broken when
  ONE sub-unit hit Discipline 0, whose top gate then zeroed every healthy sibling's pool -- an unintended intra-unit
  break cascade contradicting the canonized A.4 ('siblings fight on') and A.12 inter-unit-only cascade. Fix: the
  Discipline-0 gate sets atom.broken and promotes to unit.broken only when ALL sub-units are broken; single-subunit is
  the lone sub-unit broken => unit.broken (byte-exact, digest unchanged). Re-test: broken levy 0 while healthy heavy
  sibling fights and unit not broken; all broken -> unit.broken. Stress battery all pass. Found + fixed by Claude
  during the ED-1018/1019 NERS audit; Jordan-vetoable.

- **ED-1021** (simulation -- D-A personal-combat wound model: Spirit->Wound Interval, Strength->Health, health-based felling).
  Jordan-ratified (2026-06-18): add Spirit to the Wound Interval at low weight (WI = round(End + 4 + 0.4*Spirit);
  flat base 6->4, the 2 points reallocated into the Spirit/Strength terms so avg Health stays 40) and Strength to
  Health proportional to Endurance (Health = round(WI*(MaxWounds+1) + 0.25*Strength*End)). Felling switched from the
  wound-COUNT rule (>= MW+1 wounds) to health-depletion (cumulative damage >= Health) because the count rule made the
  Strength->Health buffer a verified no-op on outcomes (str7-v-4 0.877 ~ mirror); health-based felling makes Strength
  buy survivability. Validated (np.default_rng, MB=50): equal average chars fall in ~5.2 hits (target 4-6); mirror 0.516;
  Spirit now matters spi7-v-4 0.50->0.81; Strength holds str7-v-4 ~0.88; noise Health 37/40/43 (str1/4/7), WI 8/9/11
  (spi1/3/7). r2 self-test 7/7 PASS (Health-40 fixture held; WI 10->9). Pre-existing ~50% multi-bout mutual-stall noted
  (baseline too, not caused here). Isolated to personal combat (WI/Health unused by mass-battle). Implemented by Claude,
  Jordan-vetoable. derived_stats_v30 §4.1 propagation follows.

- **ED-1022** (bugfix -- roll-input fidelity). discipline_check_phase drove every sub-unit's Discipline from the
  UNIT's cumulative loss + unit-level asymmetry, so a fresh reserve sub-unit cracked from siblings' casualties. Now each
  sub-unit degrades from its OWN (start_troops-cur_troops) loss; single-sub-unit uses the exact (hp_max-hp) expression
  (byte-exact, digest unchanged). Asymmetry baseline stays the opposing UNIT (no per-sub-unit opponent in 1v1). Verified:
  a gutted sub-unit degrades while a fresh reserve sibling (unit loss 2.0) does not. Regression S11.
- **ED-1023** (simulation -- of_type wiring). make_mixed_unit now builds each sub-unit via Subunit.of_type, so a canonical
  troop type draws its B.2 presets (ED-1018 consumed -- closes the Part-2 wiring gap); only caller-set stat keys forwarded
  so the preset fills the rest, non-canonical 'infantry' inherits, override wins. Additive (no callers; bat.py unaffected).
  Regression S12.

- **ED-1024** (editorial -- ruling). Morale is CONTINUOUS in play (Jordan): B.2 starting values integer, erosion
  continuous. No engine change -- Morale is already float throughout; only the turn-LOG rounds (round(.,3)), no int()
  coercion. Resolves the Mode-B audit flag.
- **ED-1025** (simulation -- campaign-boundary reset). New reset_morale_between_battles(unit): resets unit + per-subunit
  own Morale to start and clears routed/broken (rout is derived from Morale, so the flags must clear); Discipline persists
  (PP-712). Uncalled within a battle -> byte-exact (digest unchanged); the campaign layer calls it at the battle boundary.
  Regression S13.

- **ED-1026** (simulation -- sweep fidelity findings 1-2). Two formation paths now read per-subunit Discipline:
  advance_cells (movement formation-hold; run_battle passed unit.discipline -> atom.eff_discipline) and Unit.check_drift
  (formation drift; self.discipline -> a.eff_discipline). Byte-exact single-subunit (digest unchanged). A low-Discipline
  subunit now advances slower and drifts to Line independently of disciplined siblings. Regression S14 (drift) + S15 (advance).

- **ED-1027** (simulation -- sweep findings 3-6 closeout). (3) recalc_size now propagates rout to subunits on
  destruction; (4) the inter-unit cascade denominator uses agg_discipline (per-subunit troop-weighted, == unit when
  homogeneous); (6) between_turn_recovery recovers per-subunit Morale (inert at RECOVERY=0); (5) deleted dead
  discipline_penalty_volley. Byte-exact single-subunit (digest unchanged). Regression S16 + S17 + S18.

## 2026-06-20 — Formation-drift cell orphaning fix (ED-1032) [DIGEST CHANGE — first since the per-subunit gauge baseline]
- FINDING (diagnosed bottom-up vs orchestration.py + percell.py this session): on formation drift to Line (Unit.check_drift, L1368) cell_troops was not re-keyed to the new shape's pattern. ~42% of a drifted sub-unit's troops (157/376 in test) became spatially orphaned -- counted in HP (sum(cell_troops)==hp held, so strength/pool stayed correct) but invisible to iter_cells AND inert to front-cell casualty distribution (the orphaned wing never bled, held no frontage, could not be enveloped). Violates ED-907's "each cell inherits the best execution".
- FIX (orchestration.py check_drift): on drift, total=sum(cell_troops); shape="Line"; re-key cell_troops to _oriented(a)'s Line pattern with uniform per=total/len(new_ids), mirroring spawn (L629). Preserves total strength; restores the full cell complement.
- VALIDATION: test_persubunit_stress S1-S18 ALL PASS (no property regression); drifted unit final orphan=0.00 with HP preserved; no committed golden-digest test (digest asserted only by local bat.py).
- DIGEST CHANGE (intended, first since baseline): fe99574610caca44052509beb8c0b81a1b3d1972c6a3c8e3513e38933ef27c69 -> 1f8c05a9748d0b29c35a3acbd5e87d8f7112e159513cd3782af4f781a7cee05e. The fix deliberately alters drift-scenario outcomes (re-keyed casualties spread over the full Line, not the shared spine); IDENTICAL for any sub-unit that does not drift (reassignment is inside the drift branch). Jordan-approved adoption 2026-06-20.

## 2026-06-20 — base_combat_pool comment alignment + PP-683 framing (byte-exact; defect cleanup)
- orchestration.py base_combat_pool: the [canonical:] comment cited the legacy min(Size,Command)+Command; updated to the live Command*(1+cohesion) (ED-899/ED-1013), consistent with the now-propagated §A.4. Comment-only -> byte-exact (gauge digest 1f8c05a9 unchanged).
- PP-683 (encirclement -3 morale-cap removal) intentionally NOT wired: the engine delivers encirclement via PC_ENVELOP_SHOCK + Lanchester contact-overlap; a second cap-removal term double-counts and breaks H4 Cannae (same reason _envelopment_sigma is held dormant, NERS-N/E: no unneeded apparatus). The -3 cap (L314 min(loss,3.0)) stays in force; encirclement lethality is the shock + overlap. Doc PP-683 note added in the matching editorial commit.

## 2026-06-30 — Mass-battle bottom-up audit: provenance registry seed (ED-1043) [additive, data-only, byte-exact]
- ADDED `tests/sim/mass_battle/provenance.py`: a primitive-provenance registry SEED (the `Prov` schema +
  `PROVENANCE` rows for the 9 anti-pattern findings F1-F9 + the 3 grounded laws). Pure data record — it does
  NOT import or touch the engine, so the gauge digest is UNCHANGED (byte-exact). All `value` fields are stored
  as strings (a record of a constant, not a live constant), so it adds no mechanical literal to the engine.
- PURPOSE: machine-readable grounding tier per constant (derived / academic-law / historical / calibrated /
  ungrounded), enforcing the "no asserted value" bar. Seed counts: 3 academic-law, calibrated + ungrounded =
  the retirement worklist (target zero). Audit: `designs/audit/2026-06-30-massbattle-bottomup/`.
- NO regression test (data-only, no behavior); CI cross-check (provenance pass on ci_sim_fabrication_check)
  is roadmap Stage 0/5, not this pass.

## 2026-06-30 — Stage 1 (re-architecture): committed byte-exact DIGEST gate (bat.py)
- ADDED `tests/sim/mass_battle/bat.py`: the deterministic golden-digest harness the matrix previously
  referenced but that was never committed. Fixed battery (10 matchups × 24 seeds, per-trial seed) hashing full per-trial end state; `--check` asserts baseline, exit 1 on drift.
- BASELINE (HEAD 4d970a0, pre-refactor): unit=7be8499b4fe6a047a4c01e925719e11d5214ae0c124c784f929bc69ad6511725 ;
  cell=1c5b2851b75761e35cf8d54283af82269383e5c70b894d021eaed981c716d4a7. These are the G5 gate for the
  Stage-1 wrapper/core split (behaviour-frozen) and update ONLY on an intentional behaviour change in a
  later stage (recorded here, like the ED-1032 digest change above).

## 2026-06-30 — Stage 1a (re-architecture): extract core/exchange.py (behaviour-frozen) [byte-exact]
- EXTRACTED the pool-assembly primitives (derive_command, command_base_pool, subunit_combat_pool,
  _stamina_pool_penalty) from orchestration.py into a new resolver layer tests/sim/mass_battle/core/
  (core/__init__.py + core/exchange.py). orchestration.py re-imports them via `from mass_battle.core.exchange
  import *` so every call site is unchanged; engine.py adds core.exchange to its public surface + _resolve scan.
  G1 import-direction: core/exchange imports config+math only (no up-DAG import; no cycle).
- BYTE-EXACT: bat.py --check passes both modes (unit 7be8499b…, cell 1c5b2851… unchanged); stress S1-S18 ALL PASS;
  mechanics_selftest green. A pure code move — identical call graph.
- GATE FIX (tools/ci_sim_fabrication_check.py): masks multi-line triple-quoted docstrings before the line scan
  (docstring prose numerals were false positives; real in-code constants still caught). Cited 19 pre-existing
  uncited constants in orchestration.py (§A.4/§B.2/§A.7/§A.3b) — comment-only; orchestration scans clean.

## 2026-06-30 — Stage 1b (re-architecture): extract core/state.py (behaviour-frozen) [byte-exact]
- EXTRACTED the morale/discipline/rout state-transition phase hooks (morale_check_phase, rout_resolution,
  discipline_check_phase) from orchestration.py into core/state.py — the resolver layer's sole state-mutation
  site alongside core/exchange. orchestration re-imports via `from mass_battle.core.state import *` (phase_boundary
  and the stress-test imports unchanged); engine.py adds core.state to its surface + _resolve scan.
- G1 import-direction: core/state imports config+math only; calls Subunit/Unit methods duck-typed (erode_morale,
  derive_rout, degrade_discipline) — no up-DAG import, no cycle.
- BYTE-EXACT (G5): bat.py --check both modes match baseline; stress S1-S18 ALL PASS; mechanics_selftest green.

## 2026-06-30 — Stage 1c (re-architecture): extract core/attrition.py (behaviour-frozen) [byte-exact]
- EXTRACTED _lanchester_strength (the linear-law contact-frontage attrition term) from orchestration.py into
  core/attrition.py. (coeffs injected, not authored). G1 clean; BYTE-EXACT both modes + stress.

## 2026-06-30 — Stage 1d (re-architecture): extract core/contact.py + _oriented->geometry [byte-exact]
- EXTRACTED the targeting/contact-detection cluster (assign_targets, resolve_cross_side_contention,
  find_contacts, count_engagements_per_atom) from orchestration.py into core/contact.py.
- RELOCATED _oriented (the oriented-footprint helper — pure geometry: footprint_for + oriented_pattern) from
  orchestration.py into geometry.py (its proper cells/geometry home; added to geometry __all__). Its ~16 callers
  (Subunit/Unit methods + the contact fns) resolve it via the existing geometry star-import.
- G1: core/contact imports config+geometry+math only; geometry imports config only — no up-DAG import, no cycle.
- BYTE-EXACT (G5): bat.py --check both modes match baseline; stress S1-S18 ALL PASS; selftest green;
  geometry exposes _oriented; orchestration re-exports the contact fns. orchestration.py: 2,740 -> 2,549 lines.

## 2026-06-30 — Stage 1e (re-architecture): extract troop_types/registry.py [byte-exact]
- EXTRACTED the troop-type module (TROOP_TYPE_STATS canonical §B.2 stat presets + stats_for / roles_for /
  role_allowed gated-role accessors) from orchestration.py into troop_types/registry.py — the user-requested
  "troop types module". Depends on config (TROOP_TYPE_ROLES) only. orchestration re-imports via star
  (Subunit.of_type + stress-test imports unchanged); engine.py adds troop_types.registry to its surface.
- G1: no up-DAG import, no cycle. This also unblocks the hierarchy/units (Subunit/Unit) move — stats_for was
  the only orchestration-internal module dependency of those dataclasses' methods.
- BYTE-EXACT (G5): bat.py --check both modes match baseline; stress S1-S18 ALL PASS; selftest green;
  stats_for('cavalry') correct. orchestration.py: 2,549 -> 2,505 lines.

## 2026-06-30 — Stage 1f (re-architecture): extract hierarchy/units.py (Subunit/Unit) [byte-exact]
- MOVED the Subunit/Unit dataclasses from orchestration.py to hierarchy/units.py (deps all lower-layer; no cycle). Fixed: restored orchestration's resolution import; moved PC_ENVELOP_PATH/PC_SWEEP toggles to the consumer; repointed validators. BYTE-EXACT both modes + stress ALL PASS. orchestration.py: 2,899 -> 1,705.

## 2026-06-30 — Stage 1g (re-architecture): engine.py true wrapper (build_unit + resolve_battle) [byte-exact]
- ADDED the wrapper's two non-resolution duties to engine.py: build_unit (faction→unit adapter) + resolve_battle
  (router dispatching single/multi/multi_unit). Wrapper resolves nothing (P1 seam). Dogfooded: bat.py builds+routes
  via them; BYTE-EXACT both modes (digests unchanged) → provably transparent; stress S1-S18 ALL PASS.

## 2026-06-30 — Stage 2 (re-architecture): standalone weapons + armour modules [additive, byte-exact]
- ADDED equipment/ package (weapons.py ARSENAL, armour.py ARMOURY, _base.py EquipmentRecord+Registry, __init__ TROOP_LOADOUT): weapons/armour split out of troop_types into their own dynamic/adaptable registries (open records + runtime register/override/variant) so the equipment model can be re-mapped onto scene-combat without disturbing the troop taxonomy. Descriptive axes only (no primitive grounding yet); a troop type NAMES a weapon+armour. NOT wired into resolution.
- G5 byte-exact: bat.py --check both modes match baseline (unit 7be8499b, cell 1c5b2851); sim-fabrication gate clean (only canonical DR literals). Co-file: the oldest 2026-06-05/06 build-log sections were archived to coverage_matrix_archive.md to stay under the 10k cap.

## 2026-06-30 — Stage 2 / Track M: FIELD_MOVEMENT continuous-speed toggle [default OFF → byte-exact]
- ADDED config.FIELD_MOVEMENT (default OFF) + Subunit._speed_accum; advance_cells uses a per-cell
  fractional-speed accumulator when ON, so a discipline-degraded body advances at its TRUE average rate
  instead of flooring to 0 every turn (floor(1*0.7)=0 freezes a slow degraded unit). Integer positions
  preserved; only per-turn step TIMING changes. [movement-substrate review 06 — finding 2]
- G5: bat.py --check both modes byte-exact with the toggle OFF (unit 7be8499b / cell 1c5b2851 unchanged,
  the OFF branch is the exact prior code). ON is a recorded behaviour change carrying its own digest
  (unit 4c5943c1…); NOT yet gauge-re-baselined — the field path's validation is the gated Track-M
  G-decision (06_movement_substrate_review.md). Heading-continuous + cid-threading deferred (need the
  float substrate / a contact-path refactor).
