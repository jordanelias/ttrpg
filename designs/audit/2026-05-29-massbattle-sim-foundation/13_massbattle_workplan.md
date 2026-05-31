# Mass Battle — Extensive Workplan: Inventory → Pipelines → Integration → Path Forward

**Date:** 2026-05-29
**Skill:** valoria-simulator (NERS framing: valoria-resolution-diagnostic)
**Scope:** simulation · planning (no build without Jordan scope confirmation)
**Session token:** df5079812d207c7e
**Builds on (committed `2a4834ce`):** audit docs 07–12 in `designs/audit/2026-05-29-massbattle-sim-foundation/`
**Architecture frame (Jordan, 2026-05-29):** *"We are pursuing σ-leverage forms while accepting that historically battles were based on attrition then routs."* — σ-leverage is the **exchange-probability substrate**; **attrition→rout is the outcome spine**. They compose; this plan is built on that reconciliation.
**Standing rule:** counters emerge from bottom-up primitives ONLY; history is the validation gate, never an input. No counter tables.

`[SELF-AUTHORED — bias risk]` This plan supersedes the top-down counter direction I pursued earlier this session. Challenge surface §8.

---

## §0 — THE ARCHITECTURE (reconciled)

The apparent tension in doc 10 (σ-leverage vs attrition) was a false dichotomy. The correct stack, top to bottom:

```
SETUP ADVANTAGES  (formation, weapon class, reach, facing, terrain, mount)
        │  expressed as δσ (uniform impact, pool-invariant)   ← σ-LEVERAGE SUBSTRATE
        ▼
EXCHANGE RESOLUTION  p_success(base_ob, pool, net_σ)  →  who wins each clash
        │
        ▼
ATTRITION  winner inflicts casualties (TroopCount drains)      ← OUTCOME SPINE
        │   (weapon×armour matrix sets how lethal)
        ▼
MORALE EROSION  casualties + flanking + cohesion → Army Morale falls
        │
        ▼
ROUT  morale crosses threshold → unit breaks → pursuit          ← HISTORICAL ENDING
        │   (rout contagion → cascade)
        ▼
BATTLE OUTCOME  (rarely annihilation; usually one side routs)
```

**Why doc 10's σ-leverage scored 2/11:** I injected δσ at the *contested Ob* where it collided with the geometry's per-side pool asymmetry — an implementation error. The correct injection is on **the exchange's success probability** (one side's *net* setup advantage in δσ → that side's win-probability of the clash), leaving the attrition/morale/rout spine intact. The spine is **already in the engine and already historically faithful** (casualties → morale erosion → rout); it must be *kept*, not replaced.

**The personal-scale proof this is one architecture:** the combat-armature `WoundTracker` (M9/R2) is the isomorph of mass-battle rout — cumulative damage → wound-gates → felled at MW+1 *is* casualties → morale-erosion → rout, one scale down. Same attrition-to-threshold spine. So personal and mass battle are **one model at two scales**, and the σ-leverage substrate + weapon/armour/reach matrix that the personal layer already has should be **inherited upward**, not rebuilt.

---

## §1 — COMPLETE PRIMITIVE INVENTORY (complete → stub → missing)

Status key: ✅ complete & sound · 🟡 partial/coarse/switched-off · 🔴 stub-only (field exists, no logic) · ⛔ missing entirely. Donor = exists at personal scale, liftable.

### Spatial layer (unit scale)
| Primitive | Status | Notes |
|---|---|---|
| Cell patterns (5 shapes) | ✅ | `CELL_PATTERN_FN`, tier-scaled |
| Oriented placement (advance_dir) | ✅ | row-flip; column-symmetric shapes correct |
| Contact detection / pairing | ✅ | `find_contacts`, `assign_targets` |
| Cross-side contention | ✅ | speed-priority, equal-speed→co-locate (symmetric) |
| Support stacking (depth) | ✅ | `support_engage_frac` depth-weighted 1.0/0.7/0.5 |
| Encirclement penalty | ✅ | ≥2 engagements → −1 |
| Facing / octagon flank | 🟡 | 3-zone (front/flank/rear), **averaged** over contact cells → fine concentration lost (Root B) |
| Per-cell speed | 🟡 | integer 0/1/2 by shape position; not a velocity vector |
| Puncture (momentum) | 🟡 | speed-differential, cap 3; coarse |
| Formation-break under pressure | 🟡 | `resolve_internal_collisions` IMPLEMENTED BUT NOT INVOKED |
| Field of vision (targeting gate) | ⛔ | all contacts "seen"; no screen/surprise. Donor: M7 facing/FoV (personal) |
| True velocity / charge build-up | ⛔ | no acceleration; charge has no physical basis |

### Force/damage layer (the matrix — Root Gap A)
| Primitive | Status | Notes / Donor |
|---|---|---|
| Combat pool | ✅ | `base_combat_pool` = min(Size,Cmd)+Cmd |
| Degree → damage | ✅ | `DAMAGE_BY_DEGREE`, contested |
| Casualty scaling (TroopCount) | ✅ | D-B: HP=soldiers, `CASUALTY_SCALE` |
| Weapon CLASS (LC/HC/LB/HB…) | ⛔ | collapsed to flat `power`. **Donor: M3 `WEAPON_CLASSES`** |
| Armour CLASS (None/Light/Med/Heavy) | ⛔ | collapsed to flat `dr`. **Donor: M3 `WEAPON_ARMOR_MOD` / M9 `armor_resist` per damage-type** |
| Weapon REACH | ⛔ | absent. **Donor: M9 `reach_ob_shift`** (reach = Ob/tempo advantage, not damage) |
| Weapon-vs-armour interaction | ⛔ | the whole §A.2 matrix. **Donor: M3+M9 (validated 5/5 historical)** |
| Mounted / cavalry (charge/shock/pursuit) | 🔴 | `troop_type='cavalry'` field exists, never branched; "no cavalry in current battery" |
| Ranged melee penalty | ✅ | pool÷3 (archer marginal in melee) |
| Volley / projectile DR | 🟡 | `RANGED_DR_DEFAULT` flat; projectile-class matrix (LP/HP/LBl/HBl) not implemented |
| Ammunition / volley limit | ⛔ | archers have infinite volleys |

### Morale / outcome spine (attrition→rout — the part to KEEP)
| Primitive | Status | Notes |
|---|---|---|
| Morale erosion (casualties) | ✅ | `dmg/(disc×cmd)`, generalship-scaled, CS-invariant |
| Rout trigger (morale≤0) | ✅ | emergent ~30% rout fraction |
| Army Morale composite (§10.2) | ✅ | wired (v31/v32): floor(avg)+Cmd_mod+Disc_mod |
| Stamina / exhaustion (per-tick) | ✅ | contact-cell drain |
| Discipline degradation | ✅ | `discipline_penalty`, shape-collapse below threshold |
| Rout contagion | 🟡 | `ROUT_CONTAGION_MORALE_HIT` exists; full adjacency-cascade partial |
| Pursuit / recall | ✅ | `pursuit_damage`, `recall_check`, freed-attacker |
| Fatigue over multi-day | ⛔ | per-tick stamina only; no forced-march/multi-day fatigue (Hastings) |
| **Rout-resolution order bug** | 🔴 | `unit_b` wins ties (doc 11); fix ready, unapplied |

### Environment / campaign layer
| Primitive | Status | Notes |
|---|---|---|
| Environmental modifiers | 🟡 | §A.9 exists, thin |
| Terrain / ground (slope, broken, river) | ⛔ | **every cited battle turned on it**; should modify speed/pool/formation. Not a primitive |
| Command radius / control | ⛔ | Command is a scalar, never spatially gated (general's reach over field) |
| Reserves / commitment timing | ⛔ | no depth-held-back-and-committed primitive (Cannae's deliberate center) |
| Screening / deception | 🟡 | feigned retreat PP-256; screening-to-blind absent |
| Campaign supply / logistics | ⛔ | precedents §1.3a "largest omission"; campaign-scale |
| Service duration / levy limits | ⛔ | precedents §1.3b; campaign force-quality |

---

## §2 — SYSTEM INTEGRATION MAP (integrated / partial / none)

| System pair | Integration | State |
|---|---|---|
| Mass battle ↔ personal combat (weapon/armour/reach) | **NONE** | §A.2 says "inherits personal table" — never wired. The #1 integration gap |
| Mass battle ↔ σ-leverage substrate | **NONE** | doc 10 bolt-on failed; needs exchange-probability integration (§0) |
| Mass battle ↔ derived_stats (Army Morale §10.2, TroopCount §7) | **PARTIAL** | Army Morale wired (v31/v32); TroopCount output-scaling §7 approximated by CASUALTY_SCALE, not exact |
| Mass battle ↔ Thread operations | **PARTIAL** | §A.10 + params Thread MS; thread phase exists, thread-check stubbed in engine |
| Mass battle ↔ faction layer (muster, Stability) | **PARTIAL** | `run_multi_unit_battle` exists; muster-quality bridge (Military stat→unit quality) is §A.4 PROPOSAL, not wired |
| Mass battle ↔ campaign (supply, levy, reinforcement §A.13/14) | **NONE** | campaign-scale primitives absent |
| Mass battle ↔ terrain/geography | **NONE** | no terrain primitive |
| Personal ↔ σ-leverage | **INTEGRATED** | the combat-armature IS σ-leverage (M1 core, R1 resolution) |
| Within mass battle: spatial ↔ damage ↔ morale | **INTEGRATED** | the engine's tick loop composes these (the working core) |

**Reading:** the engine's *internal* pipeline (spatial→damage→morale→rout) is integrated and sound. Every *cross-system* bridge that would supply the missing primitives is NONE or PARTIAL — and the highest-value one (inherit weapon/armour/reach from personal) is a clean lift because the donor is validated.

---

## §3 — PIPELINE MAPS

### 3.1 Current engine pipeline (per tick, `run_battle`)
```
volley_phase → find_contacts(pre) → halt → assign_targets → cache centroids
 → advance_cells(A) → advance_cells(B) → halt_before_enemy → resolve_cross_side_contention
 → find_contacts → stamina drain → resolve_engagements[ support_frac × octagon_angle
     × puncture − encirclement − ranged÷3 → roll → degree → DAMAGE_BY_DEGREE − dr × CASUALTY_SCALE ]
 → apply (volley+engagement simultaneous) → morale erosion[a,b] → rout check[a,b]   ← BUG: order
 → phase_boundary(stamina/morale/discipline/rally*/reform*/threadwork*)   (*stubbed)
```

### 3.2 Target pipeline (σ-leverage exchange on the attrition spine)
```
SETUP: per pair, accumulate net δσ from { formation-geometry, weapon-class-vs-armour,
        reach, facing/octagon, terrain, charge-momentum } — each a δσ contribution
 → EXCHANGE: p_win = p_success(base_ob, pool, net_σ)   [M1 σ-engine; uniform impact]
 → ATTRITION: winner inflicts casualties scaled by weapon×armour matrix (M3/M9)  [KEEP spine]
 → MORALE: casualties + flank + cohesion → Army Morale erosion  [KEEP]
 → ROUT: threshold → break → contagion → pursuit  [KEEP; apply doc-11 simultaneity fix]
 → VALIDATE: Wilson CI vs historical bands; stop when met
```
The change is **only the SETUP→EXCHANGE head** (advantages as δσ → win-probability); the ATTRITION→MORALE→ROUT spine is preserved (it is the historically-correct part).

### 3.3 Cross-scale inheritance pipeline (the integration to build)
```
personal: WEAPON_CLASSES + WEAPON_ARMOR_MOD + armor_resist + reach_ob_shift  (M3/M9, validated)
        │  aggregate to unit scale (per-soldier → per-cell → per-subunit average)
        ▼
mass: unit carries (weapon_class, armour_tier, reach) → feeds the SETUP δσ + ATTRITION lethality
```

---

## §4 — EVIDENCE BASE & ASSUMPTIONS (and what granular investigation exposes)

**`precedents_warfare.md` (2026-04-17, status ANALYSIS) evidence base:** named Western ancient/medieval land battles — Cannae 216 BC, Pydna 168 BC, Leuctra 371 BC, Hastings 1066, Agincourt 1415, Crécy 1346 — plus Weber's authority typology (governance).

**Load-bearing assumptions:**
1. **Casualty bands** ("15–30% typical, 50–70% catastrophic, winner less") are *generalized from that battle set*, not derived from first principles. Our validation gate inherits this assumption.
2. **"Generalship dominates"** is asserted as an axiom (the engine honors it via `cmd` in erosion).
3. **Formation-counter directions** come from those specific battles (wedge=cuneus, envelopment=Cannae, oblique=Leuctra, manipular=Pydna).
4. **Attrition→rout** as the outcome shape (battles end in rout, rarely annihilation) — Jordan's frame, and historically sound.

**Evidence-base GAPS (what the set does NOT cover):** steppe / horse-archer doctrine (Parthian, Mongol — kiting, feigned flight, ammunition economy); naval; gunpowder / pike-and-shot; sieges only lightly (§2). **Implication:** primitives these would demand — FoV/mobility/ammunition (horse-archer), terrain at sea/walls — are under-grounded; if the game needs them, the evidence base must be extended first (do not invent doctrine).

**What granular investigation of the cited battles ITSELF exposes (primitives the abstraction dropped):**
- **Terrain is first-class, not a modifier** — Cannae anchored a flank on the Aufidus river; Leuctra chose the ground for the oblique; **Pydna's phalanx shattered on broken ground** (the maniple won *because of terrain*, not pure formation); Hastings turned on the ridge. Every showpiece counter is partly a *terrain* story. The doc abstracts this into thin §A.9 modifiers; the evidence says terrain belongs in the spatial layer (per-cell ground modifying speed/pool/cohesion).
- **Fatigue decides** — Hastings: Harold's army "exhausted from forced march"; Cannae's encircled Romans fought to exhaustion. Multi-day/forced-march fatigue is a real decider, not just per-tick stamina.
- **Cavalry is the envelopment engine** — Cannae's double envelopment was *cavalry* clearing the flanks then the rear. The engine fakes Cannae with infantry contact-wrap precisely because cavalry is absent (this is why H3/H4 were artifacts).
- **Reserves & commitment timing** — Hannibal's deliberate fighting-center-withdrawal is a *reserve/timing* primitive, not a formation shape.

---

## §5 — ADDITIONAL MISSING PRIMITIVES (beyond doc 12's Root A/B), prioritized by historical leverage

| Primitive | Source | Scale | Why it matters | Priority |
|---|---|---|---|---|
| **Terrain / ground** (slope, broken, water, cover) | precedents (every battle) | spatial | Pydna/Cannae/Leuctra/Hastings all hinge on it; modifies speed/pool/cohesion per-cell | **HIGH** |
| **Cavalry / mounted** | §A.2, precedents | force | Cannae unmodellable without it; charge/shock/pursuit | **HIGH** (already in doc 12 #3) |
| **Command radius / control** | implied (generalship) | spatial+command | general's spatial reach; out-of-command units degrade; ties "generalship dominates" to geometry | **MEDIUM** |
| **Reserves / commitment timing** | precedents (Cannae) | tactical | depth held and committed; the deliberate-center-collapse | **MEDIUM** |
| **Fatigue over time** (forced-march, multi-day) | Hastings, Cannae | morale/force | beyond per-tick stamina; campaign-battle bridge | **MEDIUM** |
| **Ammunition / volley economy** | horse-archer gap | force | archers currently infinite; enables skirmish/kiting | **MEDIUM** |
| **Rout contagion (full adjacency cascade)** | precedents §1.3c | morale | partial in engine; complete the cascade | **MEDIUM** |
| **Screening / deception** | feigned retreat (PP-256) | spatial/FoV | screen-to-blind; needs FoV (doc 12 #7) | **LOW** |
| **Campaign supply** | precedents §1.3a | campaign | "largest omission"; out-of-battle force quality | **LOW (separate track)** |
| **Service duration / levy limits** | precedents §1.3b | campaign | levy degradation over seasons | **LOW (separate track)** |

---

## §6 — ROBUST PATH FORWARD (phased; each phase validates against historical bands, Wilson CIs, stops when met)

**Phase 0 — Foundation hygiene (small, do first, unblocks measurement).**
- Apply the doc-11 simultaneous-rout fix (kills the `unit_b` tie-skew so all validation numbers are trustworthy). One-block change.
- Lock the validation protocol: Wilson 95% CI, n≥300 pooled ≥3 seed banks, bands from `precedents_warfare.md`. Retire bare-frequency judging.
- *Gate:* mirrors all 50/50 CI-symmetric; baseline re-measured.

**Phase 1 — Build the σ-leverage exchange head (architecture, the core fix).**
- Replace the SETUP→EXCHANGE head per §0/§3.2: per-pair net δσ from existing geometry primitives → `p_success` → winner inflicts casualties. Keep the attrition→morale→rout spine untouched.
- This is the corrected version of doc 10 — δσ on *exchange win-probability*, not contested Ob.
- *Gate:* mirror 50/50; casualty-neutral; baseline counters reproduce ≥ current 5/11 CI-aware (sanity that the head doesn't regress the spine).

**Phase 2 — Inherit the weapon×armour×reach matrix (Root Gap A; highest counter-leverage).**
- Lift M3 `WEAPON_CLASSES`/`WEAPON_ARMOR_MOD` + M9 `armor_resist`/`reach_ob_shift` to unit scale (aggregate per-soldier→per-cell). Weapon class & reach feed the SETUP δσ; weapon×armour feeds ATTRITION lethality.
- Reach as δσ on the closing exchange (canonical: tempo not damage).
- *Gate:* heavy-vs-light, blunt-vs-armour, pike-reach matchups validate against precedent; Pydna's reach physics emerges.

**Phase 3 — Cavalry (Root Gap A; unlocks Cannae).**
- Branch `troop_type='cavalry'`: charge momentum (δσ from velocity), shock, pursuit superiority, +5 cut. Requires Phase 1 (δσ head) + a velocity primitive (Phase 4 partial).
- *Gate:* **Cannae emerges bottom-up** — cavalry envelopment, not infantry contact-wrap; H3/H4 validate for the right physical reason.

**Phase 4 — Spatial resolution deepening (Root Gap B).**
- De-average the octagon (finer angle or continuous; the wedge tip concentrates, the oblique angle counts); promote `cell_speed` to a velocity with charge build-up; invoke `resolve_internal_collisions` with a flank/cohesion trigger (formation-break-under-pressure → manipular-flex-vs-phalanx-rigidity).
- *Gate:* wedge, oblique, manipular-flex matchups validate.

**Phase 5 — Terrain (HIGH, history-pervasive).**
- Per-cell ground type modifying speed/pool/cohesion (slope, broken, water, cover). Re-validate the showpiece battles *on their actual terrain*.
- *Gate:* terrain-dependent outcomes (Pydna broken ground, Cannae river-anchor) validate.

**Phase 6 — Command/reserves/fatigue/cascade (MEDIUM, depth).**
- Command radius (spatial control), reserves/commitment timing, multi-day fatigue, full rout-contagion cascade, ammunition economy.
- *Gate:* combined-arms and timing-dependent outcomes validate; no over-build (drop any primitive that doesn't move a band).

**Phase 7 — Campaign track (separate, LOWER).**
- Campaign supply, service duration, reinforcement (§A.13/14). Affects between-battle force quality, not the in-battle counter.

**Cross-cutting discipline (every phase):** bottom-up only; after each primitive, run the gauge with Wilson CIs against the bands; **stop adding when bands are met** (NERS-N/E — over-building is a defect); if a primitive doesn't move its target band, it's wrong (diagnose, don't patch); express advantages in σ-leverage form so they're pool-invariant; keep the attrition→rout spine throughout. Omega-vet (PP-674) any Class-A/B addition before canon commit.

---

## §7 — DEPENDENCIES & SEQUENCING

```
Phase 0 (hygiene) ──┬──> Phase 1 (σ-leverage head) ──┬──> Phase 2 (weapon/armour/reach)
                    │                                 ├──> Phase 3 (cavalry) [needs P1 + P4-velocity]
                    │                                 └──> Phase 4 (spatial resolution)
                    │                                          │
                    │                                          └──> Phase 5 (terrain)
                    │                                                   │
                    └──────────────────────────────────────────────────┴──> Phase 6 (command/reserves/fatigue)
Phase 7 (campaign) — independent track, any time
```
Critical path: **0 → 1 → 2 → 3** delivers the showpiece counters (Cannae, Pydna) bottom-up; 4–6 refine; 7 is parallel. Phases 1–3 are the high-leverage core and the natural coupling point to the `10` σ-leverage architecture decision (this *is* that migration, done primitive-first).

---

## §8 — Independent-reviewer challenge surface `[SELF-AUTHORED — bias risk]`

1. **"This is enormous — is it realistic?"** It's phased with hard validation gates and a stop-when-bands-met rule; the high-leverage core (0–3) is bounded and the donors (weapon/armour/reach) are *already built and validated* at personal scale. But yes — this is a multi-session program; I flag it honestly. `[CONFIDENCE: high — inventory/integration/pipelines; medium — phase ordering, which depends on Jordan's architecture choice]`
2. **"You're inheriting precedents_warfare's assumptions wholesale."** Surfaced explicitly (§4): the casualty bands and counter directions are generalized from a Western ancient/medieval set with real gaps (no steppe/naval/gunpowder). The validation gate is only as good as that evidence base; extending it is a prerequisite for any doctrine it doesn't cover, and inventing doctrine is barred.
3. **"σ-leverage head — didn't that already fail (doc 10, 2/11)?"** Doc 10 injected δσ at the contested Ob (collided with geometry). Phase 1 injects on *exchange win-probability* — the corrected location. Untested; it's Phase 1's gate to prove it. `[ASSUMPTION: exchange-probability injection composes where contested-Ob injection didn't — basis: §0 reasoning + personal-scale precedent; UNTESTED]`
4. **"Is keeping attrition→rout just preserving the old engine?"** Yes — deliberately. It's the historically-correct outcome spine (Jordan's frame) and the personal-scale `WoundTracker` isomorph. The change is the advantage→probability head, not the spine.
5. **"Terrain as HIGH — scope creep?"** Grounded in the evidence itself (§4): every cited battle turned on terrain. It's Phase 5 (after the matrix/cavalry core), not deferred to campaign, precisely because it's a *spatial* primitive the showpieces need.

---

## §9 — IMMEDIATE NEXT (on Jordan's scope confirmation)

- **Confirm the phase plan + critical path (0→1→2→3).** Particularly: build Phases 1–3 in **σ-leverage form** (coupling to the `10` architecture decision — this plan IS that migration, primitive-first), and authorize the personal→mass primitive lift.
- **Phase 0 is safe to start now** (hygiene: the doc-11 fix + validation protocol lock) — no design decision needed, it only removes measurement noise.
- **No Phase 1+ build** until the architecture/scope is confirmed (owner contract; Class-A/B vetting applies).
- Carried GAP: re-read the personal combat-armature module internals in full before the Phase 2 lift (verify the aggregation math; doc 12 §9.5).

---

### Audit trail
- `[READ: precedents_warfare.md — evidence base + §1.3 proposed primitives + §6 priority + §8 post-commit cut/keep]`
- `[READ: tests/sim/v32-combat-balance/ — m3_weapon_class_layer (WEAPON_CLASSES, WEAPON_ARMOR_MOD, reach/weight/type), m9_wound_model_bottomup (armor_resist per type, reach_ob_shift, wound_severity), r2_consequence_wounds (WoundTracker = attrition→threshold isomorph)]`
- `[READ: sim_mb_06_v22_DB.py — full primitive inventory, prior turn]`
- `[FINDING: σ-leverage and attrition→rout COMPOSE — σ-leverage is the exchange-probability substrate, attrition→rout the outcome spine; doc 10's failure was injection location (contested Ob), not architecture]`
- `[FINDING: personal WoundTracker is the isomorph of mass-battle rout — one attrition-to-threshold model at two scales; weapon/armour/reach matrix is liftable, validated 5/5 at personal scale]`
- `[FINDING: terrain is first-class per the evidence itself — every cited showpiece battle turned on ground; the abstraction dropped it]`
- `[FINDING: evidence base is Western/ancient-medieval/land — gaps in steppe/naval/gunpowder; primitives those need are under-grounded; extend evidence before inventing doctrine]`
- `[COMMIT: 2a4834ce — docs 07-12 to designs/audit/2026-05-29-massbattle-sim-foundation/]`
- `[ASSUMPTION: exchange-probability δσ injection composes where contested-Ob injection failed — UNTESTED, Phase 1 gate]`
- `[CONFIDENCE: high — inventory, integration map, pipelines, architecture reconciliation; medium — phase ordering (depends on architecture choice)]`
- `[DRIFT: B6 resolved on main; github_ops.py re-fetched; commit landed via it]`
- `[GAP: personal-armature internals not fully re-read; verify aggregation before Phase 2 lift]`
- `[PASS-3: verdict stands — inventory complete→stub→missing tabled; integration mapped; pipelines drawn; σ-leverage-on-attrition-spine reconciled; phased path 0→7 with validation gates; Phase 0 safe now, Phase 1+ awaits Jordan scope]`
