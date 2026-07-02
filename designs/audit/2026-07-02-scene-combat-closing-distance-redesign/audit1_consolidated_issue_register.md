# Master Issue Register — R1 Circumstance-Degradation Redesign

**Consolidated from six independent adversarial audits** of plan
`things-like-a-feather-compressed-rivest.md` against the live engine at
`C:/Github/ttrpg-morph-rearch/designs/scene/combat_engine_v1/`.

Source lenses: `fable_lens_physics`, `fable_lens_schema`, `fable_lens_geometry`,
`fable_lens_coupling`, `architecture_orphan_audit`, `pipeline_trace`.

Merged findings that describe the SAME underlying defect across lenses into one entry.
Ordered most-severe first. Each entry cites the plan design-decisions (D1–D10) / increments
(I1–I8) it breaks, the dimension, the defect, and the acceptance bar a correct fix must meet.

**Counts: 7 BLOCKER · 9 SERIOUS · 7 MINOR (23 distinct defects).**

Dimensions: `physics` · `kinematics` · `morphology-schema` · `biomechanics-facticity` ·
`coupling-sequencing` · `architecture-orphan`.

---

## BLOCKERS

### M-01 — The D2 swing-KE reformulation is physically ill-posed (units error + re-manufactures spear dominance + self-cancelling operands)
- **Severity:** BLOCKER
- **Breaks:** D2 (primary), D1 (the `omega_cap`/`m_eff` bundle members), D4 (range scaling `omega_cap`); increments I2a/I2b, feeds I5.
- **Dimension:** physics
- **Merged from:** physics BLOCKER #1 (dimensional), physics BLOCKER #2 (I_g reconnect), physics SERIOUS (m_eff+omega cancellation), physics SERIOUS (range_avail scaling omega quadratically).
- **Defect:** `omega_cap = τ/I_g` is angular *acceleration* (1/s²), not angular velocity (rad/s), so `½·m_eff·omega_cap²` is dimensionally invalid and numerically inverts the roster onto the dagger (dagger KE ~8.1e6 vs greatsword ~751 vs spear ~47). Worse, any dimensionally-*correct* fixed-ω reading reconnects delivered energy to `I_g` — the exact quantity `heft()` was built to avoid — and `I_g` is LARGEST for the spear/poleaxe, so a correct `½·I_g·ω²` re-creates the 84–96% reach dominance the plan exists to cure (spear=221 > poleaxe=164 > greatsword=115). Additionally, if `ω` is derived correctly from the same `I_g`, the separately-listed `m_eff` mathematically cancels (`½·m_eff·v_tip² = ½·I_g·ω²`), so shipping both `omega_cap` and `m_eff` as independent bundle members either double-counts or is a silent no-op. And because D4 lets `range_avail` scale `omega_cap` while damage ~ `omega_cap²`, lost room collapses swing damage *quadratically* (room→0.5 ⇒ 0.25× damage), directly violating flag **C4** (force-vs-distance non-monotonic, interior optimum — Bolander 2009); the squared form is the harshest possible monotone ramp.
- **Correct fix must achieve:** A dimensionally-closed swing-energy form whose delivered energy is monotone in the terms that are NOT monotone in `I_g` — i.e. applied torque `τ` (2H force-couple + grip_len, the existing REC_K_COUPLE structure) and/or swing angle `θ` (room-to-develop), with `I_g` entering ONLY through `ω = sqrt(2·τ·θ/I_g)` where it cancels for delivered energy. The coupling-to-target term must be striking-mass concentration `m_head`, NOT `I_g`. Pick ONE operand basis (rotational `τ·θ`, or linear-tip `m_eff=I_g/r²` with `v_tip=ω·r`) and drop the redundant member; add an assertion the two forms agree at g=0. Room must scale the swing ANGLE (energy at most linear in room), with an interior optimum honoring C4 — never `ω` (quadratic). The falsifiable ordering `spear < arming < longsword < greatsword` (mace not collapsed) must pass as a hard unit test at ideal circumstance BEFORE any balance sweep.

### M-02 — Whole-weapon `gap` vs per-element `geo['gap']` split: composites are ranked/damaged on the wrong element's precision (roster-wide)
- **Severity:** BLOCKER
- **Breaks:** D5; increment I4 (and pre-existing today).
- **Dimension:** coupling-sequencing (mode-coherence)
- **Merged from:** geometry BLOCKER #1 (comparator/strike read `w['gap']`), geometry MINOR (`sel_head` + `w['gap']` pre-existing), pipeline BLOCKER #1 (roster-wide, 8 weapons measured), pipeline `same_key gap` flag.
- **Defect:** `element_afforded` decides AFFORDANCE per element (`el['geo']['gap']`), but `select_mode`'s greedy comparator (`systems.py:326`), `core.strike→damage` (`core.py:171`), and `adef_cap` (`systems.py:219-220`) all RESOLVE the strike on the WHOLE-WEAPON `w['gap']`. For every one of the 8 mode-element composites these diverge sharply — measured: goedendag 0.29 (whole) vs 0.73 (spike, 2.5×); guisarme 0.50 vs 0.75; ji 0.56 vs 0.68; voulge 0.48 vs 0.63; poleaxe 0.78 vs spike 0.82; bec_de_corbin 0.82 vs beak 0.57; kama_yari 0.70 vs 0.75. So a weapon that SELECTS a point-element is scored and damaged as if the whole weapon's blended gap applied. D5 claims each mode's efficacy derives "from its own geo," but the resolution path never reads that geo. Same conceptual key `gap`, read from two different objects.
- **Correct fix must achieve:** The SELECTED element's baked `geo['gap']` is threaded onto the Combatant (e.g. a `sel_gap` field beside `sel_head`/`sel_dmg`) and read in `core.strike`, `adef_cap`, and the `select_mode` comparator instead of `w['gap']`. Landed in I4 (the same increment that widens mode selection), not deferred. Goedendag is the worst case and must be a regression anchor. A composite's selected-element resolution must use that element's own precision end-to-end (affordance, ranking, damage, armour-defeat).

### M-03 — The `er`-freeze half-switch: grip-aware reach makes frozen `longer/shorter/measure_gap` contradict live reach within a single beat
- **Severity:** BLOCKER
- **Breaks:** D3; increments I3 (and everything downstream that keys off `closed`: I4, I5).
- **Dimension:** coupling-sequencing (kinematics/state)
- **Merged from:** geometry SERIOUS (longer/shorter frozen), coupling BLOCKER #2 (I3 cascade claim false + er-freeze), coupling SERIOUS (slip_inside live vs frozen), pipeline BLOCKER #2 (frozen er, more consumers, same net-sigma), architecture SERIOUS S1 (I3 redefines `closed`), architecture SERIOUS S6 (per-beat read ordering), physics MINOR (mirror `measure_gap` must be symmetric).
- **Defect:** `reach_base` ignores `grip_position` AND the wrapper freezes reach into the `er` dict ONCE per engagement (`wrapper.py:32-33`). The plan's "free cascade: reach_sigma/stophit/close_rate/close_unwieldiness all call reach_base" is FALSE: `reach_sigma` reads the FROZEN `er` snapshot (never calls reach_base); `stophit_sigma`/`close_rate` read derived wrapper locals; only `close_unwieldiness` and the live `slip_inside` call reach_base directly. The `er` dict feeds five consumers (frozen `longer/shorter` label `:37`, `measure_gap` `:38`, reopen `base_gap` `:79`, `reach_sigma` `:141`, reopen-moment attribution `:244/:247`) while grip mutates per-beat. The instant I3 makes reach_base grip-aware but leaves the freeze, a choked pole reads SHORTER via live reach (`slip_inside`, `close_unwieldiness`) while `er`/`reach_sigma`/the role labels still read its FULL reach — it can be simultaneously "longer" (frozen) and "shorter" (live) in the same beat; within ONE net-sigma assembly `reach_sigma` uses frozen reach and `str_demand` uses live reach. This also silently redefines the `closed`/`measure_gap` boundary that I4/I5 build on (they are a dependent chain I3→I4→I5, not independent), and the per-beat `er` recompute is unspecified on WHERE it runs (must be AFTER `grip_target` and AFTER the half-sword weapon swap, or reach reads last beat's grip / the pre-swap weapon).
- **Correct fix must achieve:** I3 lands grip-aware reach AND the full per-beat measure-state refresh (`er`, then re-derive `longer/shorter/measure_gap/closed` from the refreshed `er`) in one commit — not just `er[c]`. An explicit, deliberate decision on whether the `longer/shorter` LABEL may flip mid-engagement (it drives `reopen_moment` and the whole approach asymmetry — a design fork, not a mechanical refresh). A pinned per-beat sequence: `grip_target → half-sword swap → er recompute → measure_gap/closed re-derive`. Invariant tests: within a single beat every reach consumer resolves the SAME grip-aware reach for a given combatant (no frozen/live split); `longer == argmax(er)` every beat; a mid-engagement choke visibly shrinks `er` on the next beat; the mirror `measure_gap` stays symmetric (both roles recomputed). I4/I5 re-labelled as dependent on I3's measure semantics, and I3's acceptance re-run AFTER I5 (whose dynamic `range_avail` can re-open the measure I3 closed).

### M-05 — `mode_elements` carry no position/extent (and the `closed` param is discarded): D5's per-mode reach-gating has no data or signal to compute
- **Severity:** BLOCKER
- **Breaks:** D5; increment I4.
- **Dimension:** morphology-schema
- **Merged from:** schema BLOCKER #1 (mode_elements have no x_m/extent), geometry BLOCKER #1 (positional half), pipeline SERIOUS (7 silent-zip composites + voulge count-mismatch), pipeline `element_mode_inventory` (16/53 flagged), ideal_state_audit (`closed` never read), geometry BLOCKER (dead `closed` param), pipeline SERIOUS (`select_mode` ignores `closed`).
- **Defect:** Post-bake `mode_elements` carry exactly `{head, geo}` — NO `x_m`, NO `extent_m`, NO `element_ref`. They are linked to the mass-model `elements[]` (which DO carry `x_m`) only by LIST ORDER + comment text, and the lists need not agree in length (voulge: 3 mass elements vs 2 mode_elements; flamberge 3 vs 0). So D5's "how far out each mode's working element sits" / "a broad arc-requiring swing collapses in tight quarters" is UN-computable: there is no per-mode position to range-gate on. Seven multi-element composites (dangpa, spetum, partisan, guandao, fauchard, flamberge, hook_sword) have >1 located part but ZERO mode_elements, so `_mode_elements()` collapses each to one synthesized whole-weapon mode — their explicit hooks/tines/prongs/wing-lugs never become selectable fight-modes. Separately, `select_mode` RECEIVES `closed` (`wrapper.py:69`) and never reads it (`systems.py:302` body) — the measure signal D5 needs is discarded at the door. The plan's claim that D5 needs "no data edits" is false.
- **Correct fix must achieve:** Before I4, each `mode_element` carries the working element's `x_m` and `extent_m` (or an explicit `element_ref` index into `elements[]`), populated from the Phase-0 `head_elements[].x_m` already collected. A CI/import assertion that every `mode_element` resolves to a real located element (and flags length mismatches like voulge). The 7 silent-zip composites either gain authored mode_elements (with positions) or are explicitly documented as mass-model-only by design (as flamberge is). `select_mode` actually CONSUMES `closed`/`measure_gap`/`range_avail` in the close-efficacy factor, with a test that the factor is ~1.0 at open measure (behavior-preserving until intended). Until positions and the measure signal both exist, D5's per-mode reach term is fabricated, not derived.

### M-07 — `hook_affordance` cannot distinguish a genuine HOOK from a forward-catching LUG/WING/TINE; the discriminating primitives were dropped
- **Severity:** BLOCKER
- **Breaks:** D9; increment I7.
- **Dimension:** morphology-schema
- **Merged from:** schema BLOCKER #2 (hook vs catch collapse), schema SERIOUS (orient_deg dropped — the discriminator), pipeline `same_key`/inventory (dual_role guards).
- **Defect:** Every catching feature in `weapons.py` is a guard with a single boolean `dual_role_element=True` carrying no orientation, no `type`, no hook/pull semantics. So a saturating sum over `dual_role_element` guards (plan D9) treats a spetum's forward bind-lug identically to a guisarme's pull-hook, a ranseur/partisan wing-lug identically to a poleaxe/bec pull-beak. The Phase-0 artifact DID capture the distinction — a per-guard `type` field ("wing" for lugs), rich `geom_notes` ("often slightly hooked for a catch/pull function" for the bec beak; "catching/hooking … rather than a slashing edge"), and `orient_deg` (rear-curved beak = −90; in-line spike = 0; ~124 occurrences) — and `weapons.py` dropped `type`, `geom_notes`, and `orient_deg` entirely. D9's "grab affinity derives from hook hardware" is therefore un-derivable from the current schema; the "no data edits" claim is true only for retiring the `clinch` scalar, not for building `hook_affordance`.
- **Correct fix must achieve:** Re-ingest the physical discriminator from `phase0_morphology_combined.json` — `orient_deg` (rear-curved/negative orient ⇒ pull-capable) and per-guard `type` — onto elements/guards, so hook-vs-catch (and D5's arc-vs-in-line, D6's fore/aft) fall out of a real located primitive, not a fiat geo guess. `hook_affordance` distinguishes pull/trap/unhorse hardware (guisarme hook, guandao rear notch, ji crescent, poleaxe/bec beak) from straight forward-catching lugs/prongs/tines (ranseur, spetum, partisan, dangpa). A CI check that `hook_affordance` never reads the `clinch` scalar it replaces. Confirm the hook_sword crescent is counted once (element only), not double-summed.

### M-09 — I2a's "byte-identical" heft/percussion widening is unsafe: grip is already non-zero at strike, so threading must update all consumers atomically or split the combat math
- **Severity:** BLOCKER
- **Breaks:** D2; increments I2a, I2b.
- **Dimension:** coupling-sequencing (staging)
- **Merged from:** coupling BLOCKER (I2a), physics-adjacent to M-08.
- **Defect:** `core.strike` calls `WP.heft(attacker.w)` / `WP.percussion_authority(attacker.w)` with the weapon record only; grip lives on the Combatant (`attacker.grip_position`), which `wrapper.py:66` sets `>0` per-beat for a closed pole BEFORE any strike (`test_combat_stance.py:23` asserts spear `grip_target>0` when closed). Today this is harmless because heft/percussion ignore grip. The instant I2a threads grip in, either (a) `core.strike` still passes no grip and the widening is inert on the damage path (contradicting D2's "choked-up thrust deals identical damage" fix), or (b) `core.strike` is updated but the OTHER `percussion_authority` consumers — `adef_cap` (`systems.py:217`), `select_mode` (`systems.py:281,326`), `puncture_pressure` — are NOT, leaving the sigma/armour-defeat path on ideal-grip percussion while the damage path is on live-grip percussion: internally inconsistent math for the SAME blow. So I2a cannot be both grip-aware and byte-identical unless every live caller provably passes grip=0 today, which they do not.
- **Correct fix must achieve:** I2a is sold as behavior-preserving ONLY as a pure signature-widening with ideal defaults, proven by running the full roster through heft/percussion at OLD vs NEW-with-defaults signatures and asserting exact equality, PLUS a grep-assertion that no caller passes a non-default grip in I2a. ALL grip-threading of percussion_authority is deferred to a single later increment that updates `core.strike` + `adef_cap` + `select_mode` (+ `puncture_pressure`) ATOMICALLY — never split across commits. (See M-08 for the physics coherence requirement this staging serves.)

### M-11 — The grab subsystem cannot "mirror bind/riposte" and `contact.axis` cannot "go live" as a drop-in: there is no Contact state, and its three preconditions live at three non-adjacent sites
- **Severity:** BLOCKER
- **Breaks:** D8, D9; increment I7.
- **Dimension:** architecture-orphan (control-structure)
- **Merged from:** geometry SERIOUS (D8/D9 no single insertion point; bind mutates beats), pipeline BLOCKER #3 (state graph is descriptive; 21 orphan labels; contact.axis is metadata site `(WS-5, unbuilt)`), architecture L4/label_crossref.
- **Defect:** The plan says grab "wrapper branches mirror bind/riposte" and "state_graph's documented `contact.axis` injection point goes live." Neither holds. (1) The state graph is a DESCRIPTIVE/test artifact: 0 of 15 STATES nodes and 8 of 9 INJECTION_POINTS are referenced by name anywhere in `wrapper.py`/`systems.py` (21 orphan labels); the engine emits TRACE EVENTS and `state_graph` maps events→states post-hoc. There is NO "Contact" STATE — `contact.axis` exists only as injection-point METADATA, node='Bind', `site='(WS-5, unbuilt)'`, with no `to`/`emits`/terminal wiring. (2) The grab preconditions map to THREE different, non-adjacent code sites: bind (`wrapper.py:260`, a self-contained inner loop that MUTATES the beat counter `beats+=1` at `:271` and can return-felled mid-loop), beaten-aside (`wrapper.py:229-240`), deep-commit reopen (`wrapper.py:244`) — interleaved with the hit/riposte/bind outcome mapping. A branching four-outcome grab menu that all three feed has no analogous single insertion point; "mirrors bind" is false because bind mutates the loop counter and a grab menu must not re-enter it.
- **Correct fix must achieve:** Add a REAL Contact STATE to `state_graph.STATES` with explicit `to`/`emits` edges, a new `TRACE_KINDS` entry, and a `wrapper._emit` call — mirroring how the live coupling actually works (events, not named states) — BEFORE wiring `contact.py`. Choose ONE insertion point in the outcome tail (after the hit/bind/riposte mapping resolves, ~`wrapper.py:253`) that reads a unified `opening_created` flag set by all three precondition sites, rather than three parallel grab checks. Prove the branching menu terminates without re-entering the bind inner loop's beats-mutation. Drop the "mirrors bind/riposte" and "injection point goes live" framing — the Contact node must be BUILT, not activated.

---

## SERIOUS

### M-04 — `reach_base` subtracts the hand-slide `u` (metres) directly from reach in engine reach-units — a units mismatch that under-scales the choke penalty
- **Severity:** SERIOUS
- **Breaks:** D3; increment I3.
- **Dimension:** kinematics (units)
- **Merged from:** physics SERIOUS (units mismatch).
- **Defect:** `reach_base = L0(4.0) + REACH_GEOM_SCALE(0.635)·geom + reach_adj` (engine reach-units), but `u` from `at_grip` is a raw physical displacement in metres (spear u@g=1 = 0.692 m). Subtracting `u` directly treats 1 m of hand-slide as 1 engine-reach-unit, while the weapon's forward geometry entered `reach_base` already multiplied by `REACH_GEOM_SCALE=0.635`. So geometry ADDS reach at 0.635×/unit while the slide REMOVES it at 1.0×/unit — choking removes ~1.57× more reach per metre than extending it added. (Monotonicity and non-negativity are fine — `u≥0`, min `reach_base` 4.44 ≫ max `u` 0.69 — only the magnitude is wrong.)
- **Correct fix must achieve:** The slide lives in the same scaled units as the forward geometry — either subtract `REACH_GEOM_SCALE·(u/UNIT_M)`, or fold `u` into the `geom` expression before `REACH_GEOM_SCALE` is applied (`geom_eff = (head_len − u/UNIT_M) + REACH_2H_K·grip_len·[2H]`). Unit test: a full choke reduces reach by exactly the forward geometry lost, and reach stays `> L0` (weapon still out front).

### M-06 — Phase-0 `orient_deg` + per-part `material` were dropped by `weapons.py`; the fore/aft primitive D5/D6/D9 implicitly need is gone
- **Severity:** SERIOUS
- **Breaks:** D5, D6, D9; increments I4, I6, I7.
- **Dimension:** morphology-schema / biomechanics-facticity
- **Merged from:** schema SERIOUS (orient_deg/material dropped), schema MINOR D6 (facing has no per-element geometry to key on).
- **Defect:** `grep` for `orient_deg`/`material` in `weapons.py` returns 0 matches; Phase-0 has them on every element/guard. The values are load-bearing: bec_de_corbin hammer `orient_deg=+90` (perpendicular strike), curved beak `−90` (REAR-facing), top spike `0` (in-line thrust) — all flattened to positive `x_m` in `weapons.py`, so the engine cannot tell an in-line thrust spike from a rear-curved hooking beak. This is exactly the geometry D5 needs for "arc-requiring swing collapses while thrust barely degrades," what a physically-grounded facing term (D6) would key on, and the discriminator D9 needs (folds into M-07). Material's absence means any future edge-durability/bind-shear term would have to re-source it.
- **Correct fix must achieve:** Re-ingest `orient_deg` onto elements/mode_elements (0 = in-line thrust axis, ±90 = lateral/perpendicular, sign = fore/aft) so D5 close-efficacy, D6 profile, and D9 hook discrimination derive from a real primitive rather than a `[FIAT]` geo guess. Material is lower priority but its absence is flagged as a known re-sourcing cost. (This is the schema-restoration half of M-07 stated at the D5/D6 level; fixing M-07 and M-06 is one re-ingestion.)

### M-08 — `percussion_authority` stays grip-invariant while `heft` becomes grip-aware: the blunt path degrades incoherently vs the cut/thrust path within one beat, and multi-blunt composites are indistinguishable
- **Severity:** SERIOUS
- **Breaks:** D2, D5; increment I2b (and the mode system I4).
- **Dimension:** physics / coupling-sequencing (mode-coherence)
- **Merged from:** geometry SERIOUS (blunt sibling reads static percussion), pipeline SERIOUS (percussion whole-weapon only; lucerne two blunt modes identical), pipeline `percussion_authority` same-key flag.
- **Defect:** `core.damage` routes `blunt` through `percussion_authority` and `cut/thrust` through `heft`. D2 widens `heft(w,grip,range_avail)` but the swing-KE reformulation and `HEFT_REF` re-anchor are cut/thrust-only; `percussion_authority`'s swing authority `sqrt(mass)·pob_frac·energy_credit` has NO grip term, so a choked poleaxe hammer reads identical percussion to full extension. Because `select_mode` picks blunt-vs-point per beat, a composite routed to a blunt element resolves its impact from a grip-INVARIANT percussion while a cut/thrust weapon in the mirror resolves from a grip-AWARE heft — an internally inconsistent "choked thrust degrades but choked percussion does not" asymmetry inside one beat, contradicting D2's own falsifiable "choked-up swing < full-extension swing." Percussion is ALSO only ever whole-weapon, so lucerne_hammer's two blunt mode_elements (hammer + rear fluke) compute identical percussion — mode-distinct in schema, indistinguishable in code (`[PHASE-B6 PENDING]` at `systems.py:268-271`).
- **Correct fix must achieve:** `percussion_authority` becomes circumstance-aware in the SAME increment as `heft` (I2b), so both Impact-term feeders degrade coherently under grip/range; and `element_afforded` gains a per-element percussion so multiple blunt modes differ. If percussion is DELIBERATELY grip-invariant (defensible — a hammer's mass doesn't move on the haft), that is stated explicitly and the blunt/cut asymmetry is proven intended, so the ablation gate does not read it as noise. (Staging atomicity of the threading is M-09.)

### M-10 — Selected-head vs native-head split: `approach_displace`/`reach_threat`/wrapper gate deflection on the NATIVE `w['head']`, so composites that SELECT a point never trigger it
- **Severity:** SERIOUS
- **Breaks:** D5; increment I4.
- **Dimension:** coupling-sequencing (mode-coherence)
- **Merged from:** pipeline SERIOUS (sel vs native split within beat), pipeline `head` same-key flag, geometry D8/D9 discussion, ideal_state_audit (approach_displace stale head).
- **Defect:** `approach_displace` (`systems.py:448`) and the wrapper displace/slip gate (`wrapper.py:232`) read the NATIVE `w['head']=='point'`; `reach_threat` calls `adef_cap` WITHOUT `sel_head` (native), while `armor_defeat_sigma` (same beat, same weapon) passes `sel_head` — so the same weapon's armour-defeat is scored on the SELECTED head in one place and the NATIVE head in another. None of the composites (poleaxe/guisarme/voulge/goedendag/bec_de_corbin/lucerne_hammer) have native head 'point' (they are blunt/cut_thrust), so their SELECTED point-mode never activates the leverage-based deflection/slip-inside branch — the plan's own D5 symptom, exhaustively confirmed across all 8 mode-element + 7 silent-zip weapons. Note the plan's "falls back to static head when unset" is misleading: `sel_head` IS set every beat (`wrapper.py:69`), so wiring `approach_displace` to `sel_head` is an immediate behavior change on the approach, not a fallback-only change.
- **Correct fix must achieve:** Route `sel_head` consistently — pass it to `adef_cap` in `reach_threat`, and make `approach_displace` + `wrapper.py:232` read `sel_head` (falling back to native only when genuinely unset), landed with `select_mode`'s close-efficacy in the same commit. An equivalence test that at open measure (`closed=False`) `select_mode` returns the NATIVE head for every weapon (except the documented poleaxe armour-conditional split), so the approach path stays behavior-preserving until intended. Decide deliberately whether `reach_threat` is intentionally native-head (a standing reach property) or should follow the selection — don't leave it accidental.

### M-12 — `agility` migration to `at_grip` I_g is a re-baseline, not a byte-identity increment: the `I_cm` clamp + float round-trip breaks exact g=0 equality for shifted-origin forms
- **Severity:** SERIOUS
- **Breaks:** — (I1 identity claim); increment I1.
- **Dimension:** coupling-sequencing (staging) / physics
- **Merged from:** coupling SERIOUS (I1 byte-identity), pipeline SERIOUS (agility grip-blind vs wield_heft grip-aware), architecture MINOR (all `derive(w)['MoI']` consumers must agree).
- **Defect:** `agility(w)` reads `derive(w)['MoI']` (full MoI at the lead-hand axis). `at_grip(w,0)['I_g']` is NOT identical: `at_grip` computes `I_cm = max(0.0, I0 − m·PoB²)` then `I_g = I_cm + m·d_g²`; at g=0 this reconstructs `I0` only up to the `max(0,·)` clamp (which fires for degenerate/half-sword shifted-origin records where `I0 < m·PoB²`) and a float subtract-then-add round-trip (not guaranteed byte-identical). So `agility`'s consumers (`defense_affinities` dodge/parry, `mode_sigma` wind cap) can shift for any clamped weapon, while the banded mirror/determinism guards (0.40–0.60) still pass — a change masked as identity. Separately, `agility` is grip-blind while `wield_heft`/`recoverability_factor`/`close_tempo` are grip-aware, so within one beat the defence caps use static inertia while the offence tempo uses grip-aware inertia.
- **Correct fix must achieve:** Before claiming I1 byte-identical, run `agility(w)` OLD vs `at_grip(w,0)['I_g']`-based NEW across the FULL roster (especially `longsword_halfsword`/`estoc_halfsword`, the shifted-origin records that trip the `I_cm` clamp) and assert EXACT float equality, not just the banded mirror guard. If any weapon differs, annotate I1 as a re-baseline. Additionally, every consumer of `derive(w)['MoI']` on the dynamics path (`agility`, `defense_affinities.lever_norm`, `wield_heft`, `_recovery_mode_commitment`) reads the SAME grip-adjusted I_g, so no function reads static MoI while a sibling reads circumstance-adjusted MoI for the same blow.

### M-16 — HEFT_REF re-anchor: the GREEN heft tests are magnitude-blind for the non-anchor roster, so a re-tier can pass CI while silently re-scaling every weapon's damage
- **Severity:** SERIOUS
- **Breaks:** D2; increments I2b, I8.
- **Dimension:** coupling-sequencing (test-coverage)
- **Merged from:** coupling SERIOUS (I2b/I8 magnitude-blind tests).
- **Defect:** `test_combat_heft.py` pins only longsword `heft==1.0` (1e-6), the ORDERING `spear<arming<longsword<greatsword`, and `greatsword>longsword·1.5`. None pin an absolute magnitude for spear/arming/greatsword or any of the ~30 other roster weapons. Since `core.damage` uses `HEFT_HEAVY·heft_units`, a D2 KE re-anchor that holds longsword==1.0 and the ordering but changes the spread (e.g. greatsword 1.6→2.4) shifts every non-anchor weapon's DAMAGE with nothing in the suite pinning it — the classic "test still passes but no longer covers the changed path."
- **Correct fix must achieve:** I2b adds a per-weapon heft snapshot regression (all roster weapons, recorded magnitudes) so the re-anchor's effect on every weapon is visible and Jordan-gated, not just longsword. A held anchor + held ordering must not be able to silently re-tier damage across the roster.

### M-18 — `clinch` D9 disposition is an OR ("retired OR reduced to a residual bias"), leaving an orphan-reintroduction path back into the resolution
- **Severity:** SERIOUS
- **Breaks:** D9; increment I7.
- **Dimension:** architecture-orphan
- **Merged from:** architecture SERIOUS (clinch disjunction), architecture `orphan_table` G1.
- **Defect:** `clinch` is confirmed DEAD today (a 1–10 field on all ~55 records, ZERO live engine readers). D9 says grab affinity DERIVES from real primitives (`hook_affordance` + free-hand + leverage) and the inert field "is retired or reduced to a residual bias." If the residual-bias branch is chosen, `clinch` regains a live reader WITHOUT a stated consumer formula — re-instating exactly the hand-authored per-weapon scalar in the resolution path that this whole re-architecture exists to purge. I7's acceptance ("clinch has a live reader OR is retired") passes either way, so the guard is hollow.
- **Correct fix must achieve:** A single forced disposition — retire the `clinch` field entirely (DELETE it from `weapons.py` records) once `hook_affordance`/free-hand/leverage cover the grab derivation. If a residual bias is genuinely wanted, it must be a NAMED term with its own `[FIAT]`/`[SIM-CALIBRATE]` tag and an ablation gate — not a fallback that quietly re-reads the old scalar. I7's acceptance tightened to "clinch is DELETED from weapon records," not the current disjunction.

### M-19 — `rear_clearance` must be derived from located parts, not the ready-made `derive()['length_m']` shortcut (which is wrong for exactly the composites/half-swords the plan calls out)
- **Severity:** SERIOUS
- **Breaks:** D1, D7; increments I2a, I7.
- **Dimension:** morphology-schema / biomechanics-facticity
- **Merged from:** schema SERIOUS (length_m is the wrong quantity).
- **Defect:** `derive()` exposes `length_m = (head_len+grip_len)·UNIT_M`, the FULL weapon length — not the extent trailing behind the working hand (`x=0`). These diverge sharply: spear `length_m=2.01` but true rear extent −0.36 m; guisarme 2.10 vs −1.06; estoc_halfsword 1.57 vs −1.17; the two auto-switch half-sword forms carry a correctly SHIFTED origin (`origin_shift_m=0.75`) so their rear extent is right ONLY if computed from parts. The primitive IS sufficient — `haft.x_m`/`butt.x_m`/`pommel.x_m` are all present and `_all_parts()` already assembles them about `x=0` — but the hazard is that `rear_clearance()` reads the convenient `length_m` and is badly wrong for the very cases D7 targets.
- **Correct fix must achieve:** `rear_clearance` computed strictly as `−min(x − extent/2 over _all_parts(w))` (how far the most-rearward part trails behind `x=0`), NEVER from `length_m`, and no new stored length field added. Unit tests: `rear_clearance(spear) < rear_clearance(guisarme)`; both half-sword forms exceed their base form (choking up trails more weapon).

### M-21 — I7 is over-bundled: a low-risk continuous lever (rear_clearance penalty) is coupled to the highest-risk new subsystem (contact.py), enlarging the hardest-to-verify increment
- **Severity:** SERIOUS
- **Breaks:** — (sequencing of D7 vs D8/D9); increment I7.
- **Dimension:** coupling-sequencing (staging)
- **Merged from:** architecture SERIOUS S5 + architecture finding.
- **Defect:** I7 chains rear_clearance penalty (D7) → hook_affordance (D9) → contact.py grab/pin (D8) → wrapper/state_graph/capabilities wiring. The rear_clearance penalty (`close_tempo`/`str_demand`) consumes only the I2a bundle and has NO dependency on the grab subsystem; bundling it obscures which half moved a balance number and makes the branching-outcome increment (the riskiest) larger than necessary.
- **Correct fix must achieve:** Split I7 into I7a (rear_clearance penalty, independently ablation-gated, landable as early as post-I2a — its producer) and I7b (contact.py + hook_affordance + wiring). Each half independently verifiable per the plan's own "each increment independently verified" discipline; shorter, safer critical path.

---

## MINOR

### M-13 — `hook_affordance` saturating sum triple-counts `extent_m` already consumed by `blade_guard` and the mass model
- **Severity:** MINOR
- **Breaks:** D9; increment I7.
- **Dimension:** architecture-orphan (double-read)
- **Merged from:** geometry MINOR (hook_affordance re-sums blade_guard extent).
- **Defect:** `_guard_catch_raw` already sums `g['extent_m']` over ALL guards including `dual_role_element` ones, so `blade_guard` already credits the guisarme hook / dangpa tines / partisan wing-lugs as catch surface; those same elements also appear in the mass model's `elements[]`. A new `hook_affordance(w)` "saturating sum over dual_role_element guards" re-sums the SAME extents — three readers of one physical extent.
- **Correct fix must achieve:** `hook_affordance` scoped to the GRAB/PIN axis only (`contact.py`) and proven orthogonal to `blade_guard`'s bind-catch (grab = seize/control via hardware; bind-catch = deflect an opposing blade), OR derived as a documented FUNCTION of `blade_guard` rather than a fresh independent sum over the same guards, so the two are not silently additive on the same `extent_m`.

### M-15 — I5 range_avail write/read must be atomic and must not reorder the `commit_depth` rng draw
- **Severity:** MINOR
- **Breaks:** D4; increment I5.
- **Dimension:** coupling-sequencing (staging)
- **Merged from:** coupling SERIOUS (I5 atomicity + rng order).
- **Defect:** `commit_depth` is a single consumer whose output fans out to ~10 reads; `c.range_avail` does not exist yet. Between I1 (scaffold default 1.0) and I5, `commit_depth` ignores it. The half-switch risk is INSIDE I5: `commit_depth` must start reading `c.range_avail` AND the wrapper must start writing `range_utilization→c.range_avail` in the SAME commit, or the lever is half-wired (inert no-op, or dead field) with nothing failing. `range_avail` must only reshape the Beta PARAMS, never add/reorder a draw, or seeded determinism (`test_combat_balance_guard.py:45`) breaks. (Downgraded to MINOR: the field is new — no existing consumer to half-switch against — and the risk is self-contained to I5's own wiring.)
- **Correct fix must achieve:** I5 lands the `range_utilization` writer (wrapper, before `commit_depth` at `wrapper.py:128`) and `commit_depth`'s read ATOMICALLY. Ablation gate: with `range_avail` forced to 1.0, I5 is byte-identical to I4; with real `range_utilization`, the commit distribution moves beyond noise (else the lever is cut). Confirm the `betavariate` draw order/count is unchanged.

### M-17 — The combat test suite `pytest.importorskip('numpy')`-skips in the numpy-less validator env, so per-increment "pytest green" can mask an all-skip
- **Severity:** MINOR
- **Breaks:** — (verification discipline for every increment I1–I8).
- **Dimension:** coupling-sequencing (verification-infra)
- **Merged from:** coupling MINOR (cross-cutting all-skip gap).
- **Defect:** Every `test_combat_*.py` calls `pytest.importorskip('numpy')`; the lightweight validator job runs WITHOUT numpy. So an increment validated there SKIPS (not fails) every combat identity/ordering assertion — a byte-identity regression would not trip. The very tests meant to catch an incomplete migration are conditionally inert.
- **Correct fix must achieve:** Every increment's verification step runs pytest in an environment WITH numpy + the sim modules present, and asserts a NON-ZERO collected/passed count for the combat suite. A skipped combat suite is treated as a RED verification, not a pass.

### M-20 — The `at_grip` CoM clamp makes the choke-up subsystem inert for a centre-balanced staff (u=0) — the canonical half-staff weapon gets neither inertia benefit nor reach/rear-clearance change
- **Severity:** MINOR
- **Breaks:** D1, D3, D7; increments I2a, I3, I7.
- **Dimension:** kinematics / morphology-schema
- **Merged from:** physics MINOR (staff u=0 inert).
- **Defect:** `at_grip`'s "never slide past the CoM" clamp gives a centre-balanced weapon (staff, PoB=0) `u_max=0` for all g (verified: staff `I_g/S_g/u` constant across g). So under R1 the staff pays no rear-clearance close penalty AND gains no inertia/handling benefit from choking — the choke-up subsystem is inert for the ONE weapon the research most clearly cites for it (half-staff centre grip). The single `u` conflates "where the hand is for reach/self-interference" (a geometric slide along the grippable length) with "where the hand is for minimum I" (bounded by CoM); for a centre-balanced weapon these diverge.
- **Correct fix must achieve:** Decouple the reach/rear-clearance hand-position (a pure geometric slide along the grippable length, independent of PoB) from the inertia-minimising slide (bounded by the CoM). D3/D7 read a geometric grip offset; D1's `I_g` keeps the CoM clamp — so a centre-balanced staff's reach/rear-clearance geometry still changes when the hands move, even though its inertia is already minimal.

### M-22 — I1 scaffolds `facing`/`range_avail` fields whose first consumers are I5/I6 — a multi-increment orphan window that becomes permanent clinch-class dead data if the effort is truncated
- **Severity:** MINOR
- **Breaks:** — (I1 scaffold vs I5/I6 consumers).
- **Dimension:** architecture-orphan
- **Merged from:** architecture MINOR S3 + architecture finding + `orphan_table`.
- **Defect:** `range_avail`'s first live reader is I5; `facing`'s is I6. Between I1 and those, the fields exist with no reader — a deliberate, time-boxed orphan (same pattern as the existing `sel_head`/`sel_dmg` scaffold), which becomes a permanent clinch-class orphan if the effort is cut after I4.
- **Correct fix must achieve:** Either gate each field's addition behind its consumer increment, OR add an I8 structural assertion that every Combatant circumstance field has ≥1 live reader (a standing anti-orphan test that generalizes the lesson `clinch` taught).

### M-24 — The 8 `INJECTION_POINTS` carry hardcoded `wrapper.py:NN` line-number `site` strings that nothing reads and that R1's edits will silently invalidate
- **Severity:** MINOR
- **Breaks:** — (drift hazard across all wrapper-touching increments).
- **Dimension:** architecture-orphan
- **Merged from:** pipeline MINOR (stale-comment coupling).
- **Defect:** `INJECTION_POINTS[...]['site']` strings (e.g. `'wrapper.py:66-74'`, `'wrapper.py:131-133'`) are never imported/read by the wrapper. R1's per-beat facing/range_avail writes + contact branches shift every line number, and nothing tests the site strings against reality — a guaranteed drift source.
- **Correct fix must achieve:** Either drop the line-number `site` strings (keep only node names), or add a test that each site line-range still contains the described logic.

### M-25 — The plan's own "Fable 5 audit findings" section is `[PENDING]`; the increment sequence is not ratifiable until these verdicts fold in
- **Severity:** MINOR
- **Breaks:** — (plan self-completeness / gating).
- **Dimension:** architecture-orphan (process)
- **Merged from:** architecture MINOR (plan not self-complete).
- **Defect:** The "Fable 5 audit findings (folded in)" section is a placeholder listing anticipated candidates (mode_elements carry no positions; orient_deg/material dropped; er-freeze; UNIT_M double-bookkeeping). Approving before these fold in means the sequencing may shift — specifically "mode_elements carry no positions" (M-05) directly affects I4, which M-03 flagged as measure-dependent.
- **Correct fix must achieve:** Do not ratify the increment sequence until the six-lens findings (this register) are folded into the plan; re-derive the I3→I4→I5 dependency chain and the I7 split after fold-in.

---

## Appendix A — Validated as SOUND (non-findings, recorded to close the audit questions)

These were explicitly checked and confirmed OK; no action required beyond keeping the stated invariant.

- **L0 purity honored.** `at_circumstance(w, grip, range_avail)` takes weapon + scalar circumstance params only, no Combatant — matches the existing `at_grip` pattern; `range_utilization` correctly lives in L2 and passes a bare scalar into L0. *(Recommend a structural test asserting `at_circumstance`'s signature contains no Combatant/measure_gap param.)* — architecture L1/L2.
- **Facing on the Combatant, wrapper as sole mutator.** `facing`/`range_avail` per-beat writes slot into the existing `wrapper.py:66-69` loop exactly like `grip_position`/`sel_head`; all mutation stays in L3. — architecture L3/L5/L6.
- **contact.py as its own L2 module** is the correct sizing call (systems.py ~660 lines); the module boundary is sound (the WIRING is M-11, not the placement). — architecture L4.
- **Grip bounds are well-formed** — `grip_choke_max`/`grip_travel_max` already clamp `at_circumstance`'s grip arg; no new schema needed for grip validation. — schema MINOR.
- **`rear_clearance(g) = rear_clearance(0) + u(g)` is monotone non-decreasing for the whole roster** (because `u≥0`); the definition is physically correct — the risk is the SOURCE (M-19) and the staff edge case (M-20), not the monotonicity. Assert the invariant so a future rearward-regrip can't silently break it. — physics MINOR.
- **Mirror-symmetry is preserved by the pure L0 bundle**; the only mirror risk is a role-asymmetric `measure_gap` at L3 (covered by M-03's symmetric-refresh acceptance). — physics MINOR.
- **D6 facing as shipped (near-neutral) is SOUND** — C1 (polearm facing) is unresolved and correctly not load-bearing; the profile term is fiat-flagged. It only becomes a problem if promoted to weapon-shaped without the re-ingested `orient_deg` (M-06). — schema MINOR.

---

## Appendix B — Design-decision classification (D1–D10)

| Decision | Verdict | Governing defects |
|---|---|---|
| **D1** — L0 circumstance bundle (`omega_cap`/`m_eff`/`rear_clearance`) | **SALVAGEABLE-WITH-CHANGES** | Bundle SHAPE and L0-purity are sound (App. A), but two of three new members are broken/at-risk: `omega_cap`/`m_eff` ill-posed (M-01); `rear_clearance` source hazard (M-19) + staff-inert (M-20). |
| **D2** — Swung damage becomes KE-style (`½·m_eff·ω_cap²`) | **BROKEN** | M-01: dimensionally invalid, re-manufactures spear dominance via `I_g`, self-cancelling operands. Must be re-derived, not tuned. |
| **D3** — Reach becomes grip-aware | **SALVAGEABLE-WITH-CHANGES** | Direction correct and necessary; execution wrong/underspecified — er-freeze half-switch + label-flip fork + read-ordering (M-03); metres-vs-reach-units (M-04); staff geometric slide (M-20). |
| **D4** — Range-utilization + commit coupling | **SALVAGEABLE-WITH-CHANGES** | The commit-window continuous coupling is sound; HOW range enters is the M-01 problem (must not scale `ω²`, must honor C4 non-monotonic); write/read atomicity + rng order (M-15). |
| **D5** — Mode selection reads the measure | **SALVAGEABLE-WITH-CHANGES** | The idea is right but UN-buildable as scoped ("no data edits" / "reads its own geo" both false): no per-mode positions (M-05), `closed` discarded (M-05), whole-weapon gap (M-02), native-head gate (M-10), dropped `orient_deg` (M-06). Heaviest decision; blocked on schema + plumbing first. |
| **D6** — Facing = per-beat Combatant state (near-neutral) | **SOUND** | Layering honored (App. A); C1 correctly not load-bearing. Only a latent M-06 dependency IF the profile term is ever promoted to weapon-shaped. |
| **D7** — Rear-clearance close penalty | **SALVAGEABLE-WITH-CHANGES** | Consumer wiring fine and separable; but the bundle member is at risk of the `length_m` shortcut (M-19) and staff-inert (M-20), and it is over-bundled into I7 (M-21). |
| **D8** — Grab/pin = new L2 `contact.py` | **SALVAGEABLE-WITH-CHANGES** | The subsystem is legitimately L2 (App. A), but "wrapper branches mirror bind/riposte" + "contact.axis goes live" is broken — no Contact STATE, three non-adjacent precondition sites, bind mutates the beat counter (M-11). |
| **D9** — `clinch` resolved by derivation, "no data edits" | **SALVAGEABLE-WITH-CHANGES** | The derivation intent is right, but "no data edits" is FALSE (hook needs `orient_deg`/`type` — M-07/M-06); hook-vs-catch collapse (M-07); triple-count (M-13); retire-or-residual disjunction re-orphans (M-18). |
| **D10** — Shields/bucklers + full circular closing OUT OF SCOPE | **SOUND** | A scoping decision, no defect. |

**BROKEN:** D2
**SALVAGEABLE-WITH-CHANGES:** D1, D3, D4, D5, D7, D8, D9
**SOUND:** D6, D10
