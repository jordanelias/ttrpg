# VALORIA — Insurgency Pipeline

## Status: CANONICAL — Pass 2i authoring 2026-05-17

## Scope: canonical specification of the Revolt → Insurgency → Faction emergence pipeline declared by `canon/02_canon_constraints.md` §B GD-3. Specifies the 4-stage emergence model (world-level process → Latent → Insurgency → Promoted Faction), the trigger conditions and stat baselines for each stage transition, mechanical interactions (territorial control, invasion eligibility, Parliamentary participation gates), and suppression conditions. Acts as the implementation surface declaration for `sim/world/insurgency_pipeline.py`.

## GD constraints: **GD-3 enforcement boundary**. Also GD-1 binding (insurgencies and promoted factions produce stat/territorial deltas only, never victory triggers). GD-2 binding (insurgency formation may trigger GD-2 mandatory threat response from owning factions).

## Source authority:
- `canon/02_canon_constraints.md` §B GD-3 (canonized 2026-05-17 commit fe367105) — generic pipeline declaration
- `designs/scene/conviction_track_v30.md` §5 (PP-416) — Latent RM-specific elaboration (precursor stage)
- `designs/audit/2026-05-14-balance-audit/faction_balance_convergence_v12c_2026-05-14.md` §4.2 — world-level RM PT decay (background process)
- `designs/provincial/parliamentary_transfer_v30.md` Pass 2h — extra-parliamentary status block at §1.3
- `designs/scene/social_contest_v30.md` §10 — Parliamentary Vote gating
- `designs/audit/2026-05-14-balance-audit/handoff_2026-05-15_v15.md` HR-10 — original hard rule

## Sim module: `sim/world/insurgency_pipeline.py`

---

## §1. Pipeline Overview — 4 Stages

The Insurgency Pipeline canonizes a 4-stage progression from world-level dissatisfaction to formal faction emergence. Each stage has distinct mechanical character. §5 conviction_track and GD-3 generic-pipeline canon describe **different stages** of this same in-fiction phenomenon — Pass 2i unifies them into one progression.

| Stage | Name | Mechanical character | Canon source |
|---|---|---|---|
| **1** | World-level background process | RM PT decay; reduces piety in eligible territories at arc boundary | v12c §4.2 (RM mechanic, validated_n1000_v12c); `designs/provincial/restoration_movement_v30.md` Pass 2d pending |
| **2** | Latent RM (ambient influence) | Active NPC influence in low-PT territories; does NOT control territory | conviction_track §5 PP-416 |
| **3** | Insurgency formation | Territorial-controlling entity; holds territory; can invade; non-parliamentary status | GD-3 (a-b) |
| **4** | Promoted Faction | Full faction status (parliamentary OR extra-parliamentary per emergence conditions) | GD-3 (c-e) |

**Progression mechanic:** stages 1-2 run independently of stages 3-4 (Latent RM can exist without an Insurgency forming; Insurgency can form without prior Latent RM if territorial neglect creates Uncontrolled territories). Stages 3-4 are the GD-3 pipeline.

**De-escalation** (per §6 below): suppression mechanics return stages 3-4 to lower-stage states; cannot fully erase stage 1 background process.

---

## §2. Stage 1 — World-Level RM PT Decay (background)

Per v12c §4.2 (RM mechanic). Fires at each arc boundary.

| Parameter | Value (v12c balanced) |
|---|---|
| `RM_BASE_STRENGTH` | 1 |
| `RM_GROWTH_PER_ARC` | 1 |
| `RM_PT_DECAY_CHANCE` | 0.35 |
| `RM_VARFELL_COOPTION_BONUS` | 0.1 |

**Procedure per arc** (per v12c §4.2):
1. Compute effective chance: `min(0.8, RM_PT_DECAY_CHANCE × (RM_BASE_STRENGTH + RM_GROWTH_PER_ARC × (arc - 1)))`
2. For each territory where PT > 0:
   - Skip if owner = Church (Church holds the line in own territories)
   - Skip if Church has Inquisitor in territory (Inquisitors resist RM)
   - If Varfell adjacent AND Varfell I ≥ `EINHIR_I_GATE`: chance += `RM_VARFELL_COOPTION_BONUS × rm_strength` (capped at 0.9)
   - Roll uniform [0, 1); if roll < chance: PT − 1

**Mechanical character:** background process; does not require a Latent RM or Insurgency to exist; produces low-PT territories which become trigger surface for Stage 2 (Latent RM emergence) and Stage 3 (RM-variant Insurgency promotion per GD-3 (d)).

[CROSS: `designs/provincial/restoration_movement_v30.md` Pass 2d will author the dedicated RM canon doc consolidating v12c §4.2 (this background process) with conviction_track §5 (Latent stage). Pass 2i references both directly pending Pass 2d completion.]

---

## §3. Stage 2 — Latent RM (Ambient Influence)

Per conviction_track §5 (PP-416). Distinct from the world-level decay (Stage 1); represents organized but unincorporated political activity.

### §3.1 Emergence trigger (conviction_track §5.2)

RM emerges as Latent (active NPC influence) when ALL of the following are true at Accounting:

1. **WA ≤ −2** (Varfell has alienated the Restoration Movement) — see conviction_track §5.1 Warden's Accord track
2. **At least 3 territories have PT ≤ 1**
3. **MS ≤ 50** (rendering instability feeds cultural desperation)

### §3.2 Latent RM characteristics (conviction_track §5.3)

| Stat | Value | Derivation |
|---|---|---|
| Mandate | Count of territories with PT ≤ 1 (min 2, max 5) | Popular mandate from low-conviction populations |
| Influence | 4 | Grassroots network |
| Wealth | 1 | No institutional backing |
| Military | 0 | Non-violent movement at this stage |
| Stability | 3 | Decentralised resilience |

**Critical territorial-control distinction:** Latent RM **exerts influence within territories but does NOT control them**. Latent RM presence adds +1 Ob to any Church action in that territory. No flag changes; no ownership transfer.

### §3.3 Latent RM actions (conviction_track §5.3)

Once per season, NPC-controlled:

| Action | Roll | Effect |
|---|---|---|
| Community Weaving | Influence vs Ob = Thread Tension ÷ 20 (round up, min 1). Requires TS 30+ practitioner affiliated. | OW: MS +2, PT −1 in target. Success: MS +1, PT −1. Partial: no effect. Failure: Stability −1, MS −1. Co-Movement card drawn. |
| Grassroots Organising | Influence vs Ob 2 | Success: RM Mandate +1 in territory with PT ≤ 2 (caps at Mandate 5) |
| Resist Seizure | Influence vs Church Influence | When Church attempts seizure in PT ≤ 2 territory: RM adds +1 Ob to Church seizure roll. Passive — does not consume RM action. |

### §3.4 Latent RM AI priority (conviction_track §5.3)

NPC AI: Reduce PT in adjacent territories. Protect MS. Oppose Church and any faction with Mandate ≥ 5.

---

## §4. Stage 3 — Insurgency Formation

Per GD-3 (a-b). Distinct from Latent RM (Stage 2); represents territorial control by an organized but-not-yet-parliamentary entity.

### §4.1 Formation trigger (GD-3 (a))

An Insurgency forms when:

1. **2+ contiguous territories at Uncontrolled status**, sustained **2 consecutive seasons**

"Contiguous" per `designs/territory/settlement_adjacency_v30.md` adjacency graph (edge-connected). "Uncontrolled" status: no owning faction (per `designs/provincial/peninsular_strain_v30.md` territory ownership semantics).

**Distinct from Latent RM trigger:** Latent RM emerges from PT decay + Varfell-relationship + MS instability (§3.1 above). Insurgency emerges from territorial neglect specifically. An Insurgency can form even if Latent RM does not exist; Latent RM can exist without an Insurgency forming.

### §4.2 Insurgency stat baseline (GD-3 (b))

On formation:

| Stat | Value | Notes |
|---|---|---|
| Legitimacy | 1.0 | Float; baseline for new entity |
| Influence | < starting-faction baseline (e.g., 2-3) | Low |
| Stability | < starting-faction baseline (e.g., 2) | Low |
| Wealth | 0-1 | Minimal; territorial extraction only |
| Military | Variable | Determined by source territory state at formation |
| Status | **non-parliamentary** | See §4.3 |

[PROVISIONAL: specific Influence / Stability / Wealth / Military starting values are not specified in GD-3; values listed above are Pass 2i derivation. Forward-flag INSURGENCY-STATS-001.]

### §4.3 Non-parliamentary status — what Insurgency CAN and CANNOT do

**Insurgency CAN:**
- Hold territory (canonical ownership flag set; territory shows Insurgency-owned in map)
- Invade other territories via Military Conquest action (mass battle resolution per `mass_battle_v30.md`)
- Be targeted by any faction's Military Conquest (Insurgencies are valid invasion targets)
- Generate CB against other factions (e.g., Adjacent Instability CB per `parliamentary_transfer_v30.md` §3)
- Be targeted by CB from other factions
- Be excommunicated (Church may invoke Excommunication Tribunal per `social_contest_v30 §7.1`)
- Negotiate informal treaties or alliances (political surface participation)
- Be the target of Parliamentary Transfer initiated by other factions (their territories CAN be transferred via Parliamentary vote)

**Insurgency CANNOT:**
- Cast Parliamentary Votes (per `social_contest_v30 §10` voting eligibility — gated by parliamentary status)
- Initiate Parliamentary Transfer (per `parliamentary_transfer_v30.md` §1.3 — extra-parliamentary status block; non-parliamentary is the stricter case)
- Hold or sign formal Crown Treaties (Treaty requires parliamentary status; Crown may negotiate informal arrangements but not formal binding)
- Invoke Parliamentary Stay (per `social_contest_v30 §10.1`)

**Critical clause (GD-3):** Insurgencies can invade ANY faction, including the parent faction whose territorial neglect generated them. There is no protection from the spawning faction's retaliation other than military superiority.

---

## §5. Stage 4 — Promoted Faction

Per GD-3 (c-e). Insurgency promotes to formal Faction when all of the following are true at Accounting:

### §5.1 Promotion trigger (GD-3 (c))

1. **L ≥ 3** (Legitimacy threshold)
2. **2+ territories held** (territorial base)
3. **Accord ≥ 4** averaged across held territories (population acceptance)
4. **Sustained 2 consecutive seasons** with all of the above

Sustained-2 condition: at Accounting of season N, all 3 conditions are true; at Accounting of season N+1, all 3 remain true; both Accountings count for the 2-season window. Non-consecutive seasons meeting the conditions do NOT aggregate. Same discipline as `treaty_expiration_v30.md` arc-boundary check and Knot `[Sustained Disposition reduction]` from `knots_v30.md` §5.

### §5.2 Promotion outcome branching (GD-3 (d-e))

At promotion, the Promoted Faction's parliamentary status is determined by **average PT across held territories**:

| Condition | Outcome | Status |
|---|---|---|
| **PT < 3 average** | RM-variant emergence (anti-Church identity) | **extra-parliamentary** |
| **PT ≥ 3 average** | Generic new Parliamentary candidate | **parliamentary** |

The status flag is **persistent** — once set at promotion, the Promoted Faction retains that status for the rest of the campaign. Subsequent PT shifts in held territories do NOT change parliamentary status.

[PROVISIONAL: persistence rule is Pass 2i derivation. GD-3 specifies the trigger conditions but not the post-promotion mutability. Forward-flag INSURGENCY-STATUS-MUTABILITY-001.]

### §5.3 Extra-parliamentary status — political surface gates

Per `parliamentary_transfer_v30.md` §1.3 + this doc:

**Extra-parliamentary factions CAN:**
- Hold and invade territory (inherited from Stage 3)
- Negotiate treaties and alliances (informal participation in political surface)
- Be CB sources and CB targets
- Participate in Excommunication Tribunal proceedings (defendant or accuser)
- Trigger world-level Conviction Scar effects

**Extra-parliamentary factions CANNOT:**
- Cast Parliamentary Votes (per `social_contest_v30 §10`)
- Initiate Parliamentary Transfer (per `parliamentary_transfer_v30.md` §1.3)
- Sign formal Crown Treaties (informal arrangements only)
- Invoke Parliamentary Stay (per `social_contest_v30 §10.1`)

### §5.4 Parliamentary status — full participation

Generic new Parliamentary factions promoted from Insurgency have full faction participation:
- Vote in Parliamentary contests
- Initiate Parliamentary Transfer (with appropriate CB)
- Sign Crown Treaties
- All political surface mechanics available

Their Convictions are set by emergence conditions (PT trajectory, territorial sources, Insurgency action history). [PROVISIONAL: Conviction-derivation algorithm not specified in canon; forward-flag INSURGENCY-CONVICTION-DERIVATION-001.]

### §5.5 RM-variant emergence (GD-3 (d), more likely path)

When the Promoted Faction emerges via PT < 3 path:
- Faction identity: Restoration Movement variant (anti-Church, extra-parliamentary)
- Inherits Latent RM stat profile if Latent RM existed at promotion (Wealth / Stability carry over; otherwise GD-3 baseline applies)
- Increased likelihood: world-state PT-decay (Stage 1 Background process) produces low-PT territories continuously, making PT < 3 average more common over campaign lifecycle than PT ≥ 3 emergence
- Per `canon/02_canon_constraints.md` §B GD-3: "RM-as-emergent-faction is more likely than generic emergence when world-state PT-decay has produced low-PT territories"

---

## §6. Suppression and De-escalation

### §6.1 Stage 2 → Stage 1 (Latent RM suppressed back to background)

Per conviction_track §5.4. Latent RM can be suppressed back to latency if ANY of:

- **WA returns to ≥ 0** (Varfell reconciles)
- **All territories rise to PT ≥ 2** (movement loses popular base)
- **RM Stability reaches 0** (movement collapses internally)

Suppression returns RM to ambient background-process state (Stage 1). RM may re-emerge to Latent (Stage 2) on subsequent §3.1 trigger.

### §6.2 Stage 3 → ??? (Insurgency suppression)

[PROVISIONAL: GD-3 does not specify Insurgency suppression / de-escalation back to non-Insurgency. Two candidate mechanics surfaced by Pass 2i for Pass 2k ratification:

- **Option A** — Insurgency dissolves when territorial count drops to 0 (all territories reconquered by other factions). Promoted Faction status disappears; no de-escalation back to Latent RM.
- **Option B** — Insurgency dissolves when Legitimacy drops below 1.0 AND territorial count drops below 2. Same final state as Option A but different threshold.

Forward-flag INSURGENCY-DISSOLUTION-001.]

### §6.3 Stage 4 → ??? (Promoted Faction dissolution)

[PROVISIONAL: GD-3 does not specify Promoted Faction dissolution. Candidate:

- **Promoted Faction dissolution conditions:** Legitimacy = 0 AND territorial count = 0, OR via Conviction Scar accumulation past survival threshold (specific value TBD).

Forward-flag INSURGENCY-PROMOTED-DISSOLUTION-001.]

### §6.4 Suppression non-symmetric

Suppression mechanics return stages 3 / 4 to "non-existence" rather than to Stage 3 / Stage 2. A Promoted Faction does not "demote" back to Insurgency status. The pipeline is unidirectional except for Stage 2 ↔ Stage 1 (Latent RM suppression).

[PROVISIONAL: non-symmetric model is Pass 2i derivation. Alternative would be full demote-chain. Forward-flag INSURGENCY-DEMOTE-DIRECTION-001.]

---

## §7. GD-3 Sim Enforcement Boundaries

Multiple sim modules participate in GD-3 enforcement. The hierarchy:

| Module | Responsibility |
|---|---|
| `sim/world/insurgency_pipeline.py` | Stage 3 formation check (Accounting cascade); Stage 4 promotion check (Accounting cascade); status flag management; emergence stat baseline |
| `sim/world/restoration_movement.py` | Stage 1 PT decay; Stage 2 Latent RM emergence per §3.1 trigger; Latent RM actions (Community Weaving, Grassroots Organising, Resist Seizure) |
| `sim/personal/parliamentary_vote.py` | Status flag check at vote eligibility; non-parliamentary + extra-parliamentary blocked from casting |
| `sim/provincial/parliamentary_transfer.py` | Status flag check at action declaration; non-parliamentary + extra-parliamentary blocked from initiating |
| `sim/peninsular/accounting.py` | Sustained-2-seasons check (running across season N → N+1) |
| `sim/provincial/faction_action.py` | Insurgency action dispatch (Military Conquest, Govern, Muster — same actions as established factions for non-parliamentary-restricted actions) |
| `sim/autoload/victory.py` | **GD-1 binding**: Insurgencies and Promoted Factions can WIN via peninsular_sovereignty (the sole victory path) once they hold 11+ territories sustained 2 seasons. There is no parliamentary-status gate on victory eligibility. |

### §7.1 GD-1 cross-binding

A Promoted Faction (parliamentary OR extra-parliamentary) IS eligible to win the game via Peninsular Sovereignty. GD-1 does not restrict victory by faction-emergence-status. A successful insurgency that grows to 11+ territory sustained 2 seasons wins — including against the parent faction it emerged from.

This is a load-bearing emergent-gameplay outcome. Player factions cannot rely on parliamentary-status of an emergent faction as a victory-safety mechanism.

### §7.2 GD-2 cross-binding

Insurgency formation triggers GD-2 mandatory threat response by the parent faction (whose neglect produced the Uncontrolled territories):

- Insurgency-held territories adjacent to parent faction territory cause those parent territories to be considered "at risk." Standard GD-2 mandatory action triggers apply if Accord drops below threshold in adjacent parent territories.
- Insurgency formation does NOT directly cause mandatory action; the threat response is per-territory per the standard Accord-trigger rules.

---

## §8. Cross-references

### Canon docs

- `canon/02_canon_constraints.md` §B GD-3 (canonized 2026-05-17) — generic pipeline
- `canon/02_canon_constraints.md` §B GD-1 — victory binding (Promoted Factions can win)
- `canon/02_canon_constraints.md` §B GD-2 — mandatory threat response
- `designs/scene/conviction_track_v30.md` §5 PP-416 — Latent RM (Stage 2)
- `designs/audit/2026-05-14-balance-audit/faction_balance_convergence_v12c_2026-05-14.md` §4.2 — Stage 1 background process
- `designs/provincial/parliamentary_transfer_v30.md` (Pass 2h) — extra-parliamentary status block
- `designs/scene/social_contest_v30.md` §10 — Parliamentary Vote eligibility gate
- `designs/scene/social_contest_v30.md` §10.1 — Parliamentary Stay gate
- `designs/scene/social_contest_v30.md` §7.1 — Excommunication Tribunal (Insurgency may be defendant/accuser)
- `designs/audit/2026-05-15-handoff/handoff_2026-05-15_v15.md` HR-10 — original hard rule predecessor to GD-3
- `designs/provincial/restoration_movement_v30.md` (Pass 2d pending) — consolidated RM canon doc

### Sim modules

- `sim/world/insurgency_pipeline.py` — Stages 3-4
- `sim/world/restoration_movement.py` — Stages 1-2
- `sim/peninsular/accounting.py` — sustained-N-seasons check infrastructure
- `sim/provincial/faction_action.py` — Insurgency-eligible action dispatch
- `sim/personal/parliamentary_vote.py` — status flag enforcement
- `sim/provincial/parliamentary_transfer.py` — status flag enforcement
- `sim/autoload/victory.py` — Promoted Faction GD-1 victory eligibility

### Mechanics index

`canon/mechanics_index.yaml` → `mechanics.insurgency_pipeline` — `canon_authoring_target` field updated from "(Pass 2i, pending)" to canonized path in companion commit.

---

## §9. Forward-flags (Pass 2k editorial-ledger batch)

| ID | Description | Resolution required |
|---|---|---|
| **INSURGENCY-STATS-001** | §4.2 Insurgency starting stat values (I 2-3, Sta 2, W 0-1, Mil variable) are Pass 2i derivation. GD-3 specifies "L=1.0, low stats (I, Sta < starting-faction baselines)" — specific values not canonized. | Jordan ratify specific values or revise. |
| **INSURGENCY-STATUS-MUTABILITY-001** | §5.2 persistence rule (status flag set at promotion is persistent for rest of campaign) is Pass 2i derivation. GD-3 specifies trigger conditions but not post-promotion mutability. | Confirm persistence rule or specify mutability mechanic. |
| **INSURGENCY-CONVICTION-DERIVATION-001** | §5.4 Convictions set by emergence conditions — algorithm not specified in canon. | Author derivation algorithm (PT trajectory weighting, territorial source weighting, action-history weighting) or revise. |
| **INSURGENCY-DISSOLUTION-001** | §6.2 Insurgency suppression / de-escalation mechanic not specified in GD-3. Pass 2i surfaces 2 candidate options. | Jordan ratify Option A or Option B or specify alternative. |
| **INSURGENCY-PROMOTED-DISSOLUTION-001** | §6.3 Promoted Faction dissolution conditions not specified in GD-3. | Jordan author dissolution thresholds. |
| **INSURGENCY-DEMOTE-DIRECTION-001** | §6.4 non-symmetric model (stages 3-4 do not demote back; only Stage 2 ↔ Stage 1 is reversible) is Pass 2i derivation. Alternative would be full demote-chain. | Confirm or revise. |
| **LATENT-RM-vs-INSURGENCY-RM-001** | §1 layering interprets conviction_track §5 (Latent RM) and GD-3 (d) RM-variant Insurgency as **different stages of the same in-fiction phenomenon**. Alternative interpretations exist (Option A: GD-3 supersedes §5; Option B: §5 supersedes GD-3 (d); Option C: distinct mechanisms). Pass 2i adopts the layered interpretation. | Jordan confirm layering, or ratify alternative. |

[FLAG: 7 derivation items forward-flagged. The mechanic core (GD-3 trigger conditions, parliamentary/extra-parliamentary status semantics, GD-1/GD-2/GD-3 cross-bindings) is canon-grounded. Derivation choices (specific stat values, persistence rules, suppression mechanics) require Jordan ratification at Pass 2k.]

---

## §10. Status Declaration

[STATUS: CANONICAL — Pass 2i 2026-05-17. GD-3 pipeline canonized with 4-stage layered model. Pipeline core (trigger conditions, status semantics, cross-stage relationships, sim enforcement boundaries) traces directly to GD-3 + conviction_track §5 + v12c §4.2. 7 derivation choices marked [PROVISIONAL] for Pass 2k Jordan ratification.]

---

## §11. Changelog

- **v30 init (2026-05-17, Pass 2i):** Initial canonization. Consolidates GD-3 generic pipeline (Stages 3-4) with conviction_track §5 Latent RM (Stage 2) and v12c §4.2 PT decay (Stage 1) into one 4-stage progression model. Specifies trigger conditions, stat baselines, parliamentary status semantics, cross-stage de-escalation, GD-1/GD-2/GD-3 sim enforcement boundaries. Forward-flags 7 derivation items to Pass 2k editorial-ledger.
