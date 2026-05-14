# Faction Balance Convergence — v12c
## 2026-05-14 · Session: balance-vectors · Handoff document for parallel session

---

## §1 Objective

Equal probability of winning (25% each) across all four factions: Crown, Church, Hafenmark, Varfell.

Prior audit (Parts 6–13, same date) established an asymmetric balance hypothesis (Crown 35–45%, Church 20–30%, Hafenmark 15–25%, Varfell 10–20%). Jordan rejected asymmetric balance. Target is symmetric 25% ± 5pp per faction.

---

## §2 Starting State (Pre-v12)

Canonical starting territory split per `peninsular_strain_v30 §2.1`:
- Crown: 6/15 territories (40% of map)
- Hafenmark: 4/15 (27%)
- Varfell: 4/15 (27%)
- Church: 1/15 (7%)

Prior best config (v11 + 50 seasons, from Part 13):
- Cr 55.8% / Ch 22.0% / Ha 11.8% / Va 10.4%
- Crown structurally dominant via Treaty-compounding hegemony path.
- Church balanced by Q-21 EA throttle.
- Hafenmark and Varfell lacked territorial acquisition vectors.

---

## §3 Design Decisions (Jordan-Directed)

### §3.1 Three new territorial vectors

**Einhir Revival (Varfell)** — Varfell can acquire adjacent settlements where piety has eroded, once they have sufficient national influence to be seen as legitimate Einhir revivalists. The Restoration Movement (RM) is independent of Varfell but can be co-opted.

**Altonian Reinforcements (Hafenmark)** — Hafenmark can call military reinforcements from Altonia/Schoenland. She would never betray Valoria itself, but she would administer a new Valoria-Altonia dynamic. Produces military capacity, not territory directly.

**Parliamentary Territory Transfer (all factions)** — All factions can acquire or "sell" territory through Parliament. Requires sufficient cause (equivalent to casus belli — even harder than invasion because justification must convince a majority, not just the aggressor). Four modes: adversarial, consensual, punishment, appeasement. Crown can execute transfer if it dips below starting number of territories (6).

### §3.2 Piety and the Restoration Movement

Piety was always meant to be degradable. The Restoration Movement is independent of Varfell — an organic cultural force opposing Church institutional dominance. Varfell can co-opt RM but does not create or control it. RM degrades PT across the peninsula over time; Church-owned territories and Inquisitor-held territories resist.

### §3.3 Einhir gate

Einhir Revival is gated by Varfell having sufficient *national Influence* (I stat), not by local territory PT conditions or Legitimacy. The question is whether Varfell has enough peninsula-wide political reach to make the cultural claim stick.

---

## §4 Mechanical Specifications (v12c)

### §4.1 Einhir Revival

| Field | Value |
|-------|-------|
| Faction | Varfell only |
| Card slot | 1/arc (not 1/season) |
| Gate | Varfell I ≥ EINHIR_I_GATE (default 4; Varfell starts at I=4) |
| Target | Adjacent territory not owned by Varfell |
| Pool | Varfell I |
| Ob (uncontrolled) | max(1, 1 + PT × EINHIR_PT_OB_WEIGHT) |
| Ob (held) | max(1, holder_Sta/2 + 1 + PT × EINHIR_PT_OB_WEIGHT) |

| Degree | Effect |
|--------|--------|
| Overwhelming | Territory transfers. Accord 2. PT−1. Varfell L+1. Holder L−1. |
| Success | Territory transfers. Accord 1. PT−1. |
| Partial | PT−1 (cultural influence spreads). Varfell gains CB vs holder. |
| Failure | Nothing. Cultural revival failure is "not yet", not backlash. |

Design note: No Stability penalty on Failure. This was the critical fix — earlier iterations with Sta−1 on Failure caused a death spiral (548 attempts / 217 failures across 50 campaigns → Varfell Sta collapses → own territories revolt → territories go Uncontrolled → Einhir reclaims them → fails again).

AI scoring: Priority 1 (never choose) when target PT ≥ 3. Priority 5 when PT = 2. Priority 14+ when PT ≤ 1 (RM has done its work). This reflects "little to no piety" — Varfell only attempts Einhir where RM has already eroded Church influence.

### §4.2 Restoration Movement (RM)

Independent world-level process. Fires at each arc boundary.

| Parameter | Default | Balanced value |
|-----------|---------|----------------|
| RM_BASE_STRENGTH | 1 | 1 |
| RM_GROWTH_PER_ARC | 1 | 1 |
| RM_PT_DECAY_CHANCE | 0.3 | **0.35** |
| RM_VARFELL_COOPTION_BONUS | 0.1 | 0.1 |

Procedure per arc:
1. Compute effective chance: min(0.8, RM_PT_DECAY_CHANCE × (RM_BASE_STRENGTH + RM_GROWTH_PER_ARC × (arc − 1)))
2. For each territory where PT > 0:
   - Skip if owner = Church (Church holds the line in own territories)
   - Skip if Church has Inquisitor in territory (Inquisitors resist RM)
   - If Varfell adjacent + Varfell I ≥ EINHIR_I_GATE: chance += RM_VARFELL_COOPTION_BONUS × rm_strength (capped at 0.9)
   - Roll: if random < chance, PT−1

RM gets stronger over time (rm_strength grows each arc), representing the organic cultural shift away from Church dominance. Church can resist via Inquisitor placement (canonical mechanic, already in sim).

### §4.3 Altonian Reinforcements (Hafenmark)

Automatic at arc boundary. No action slot cost.

| Field | Value |
|-------|-------|
| Gate | Hafenmark I ≥ ALTONIAN_I_GATE (balanced value: **5**) |
| Pool | Hafenmark I |
| Ob | 3 |

| Degree | Effect |
|--------|--------|
| Overwhelming | Mil +1 permanent |
| Success/Partial | No permanent gain |
| Failure | No effect |

Design note: Earlier iterations with Mil+1 on Success pushed Hafenmark to 39–45%. Restricting permanent gain to Overwhelming only keeps Hafenmark in band. The mechanic represents Altonia's willingness to support Hafenmark militarily — but reliable support requires exceptional diplomatic execution.

### §4.4 Parliamentary Territory Transfer

| Field | Value |
|-------|-------|
| Available to | All factions |
| Frequency | 1/arc per faction |
| Prerequisite | **Casus Belli against holder** (see §4.4.1) |
| Pool | Proposer I |
| Ob | Holder L + PARL_MAJORITY_OB_BONUS (default 2) |

| Degree | Effect |
|--------|--------|
| Overwhelming | Territory transfers. Holder L−1. Accord 1. |
| Success | Territory transfers. Accord 1. |
| Partial | Proposer gains CB vs holder (for next attempt). |
| Failure | Proposer Sta−1. Holder L+1 (public sympathy). |

Protections: Cannot strip a faction's last territory.

#### §4.4.1 Casus Belli sources

CB is consumed on use (whether transfer succeeds or not).

| Source | Mechanism |
|--------|-----------|
| Crown constitutional restoration | Auto-justified when Crown territories < 6 (starting count) |
| Adjacent instability | At arc boundary: if a faction has a territory at Accord ≤ 1, adjacent faction holders gain CB against that faction |
| Einhir Revival Partial | Varfell gains CB vs territory holder |
| Parliamentary Transfer Partial | Proposer gains CB vs holder (enables retry) |
| Military actions | Various existing actions generate CB per canonical rules |

### §4.5 Treaty Expiration

Per RC-v1 from Part 13, with tuned rate.

At each arc boundary, each Crown Treaty has TREATY_LAPSE_RATE chance of lapsing. Lapsed Treaty: cleared from both factions' treaty registers. Crown may re-bind via Senator Outward action.

| Parameter | Balanced value |
|-----------|----------------|
| TREATY_LAPSE_RATE | **0.90–0.95** |

Design note: 90–95% lapse rate is mechanically functional but narratively extreme. Almost every Treaty breaks every arc. This is the primary Crown-nerf lever. If too aggressive for the fiction, an alternative is Treaty stability tied to Crown diplomatic investment (maintaining treaties requires ongoing Senator Outward actions, creating opportunity cost). Canonical precedent: Roman foedera required renewal; medieval treaties required oath renewal at coronation.

### §4.6 EA Throttle (revised)

Ecclesiastical Appointment: **every-arc** (loosened from every-other-arc in RC-v1).

This was the critical Church balance lever. With RM degrading PT peninsula-wide, Church needs EA firing every arc to maintain institutional influence. Without this loosening, Church drops to 14–16% win rate. With it, Church reaches 27–29%.

### §4.7 Treaty Consent Rate

| Parameter | Balanced value |
|-----------|----------------|
| CONSENT_RATE | **0.28–0.30** |

Lower consent rate means factions are less willing to accept Crown Treaties, reducing Crown's hegemony-by-binding pathway.

---

## §5 Balanced Configuration (Confirmed N=1000)

### §5.1 Primary recommended config

| Parameter | Value |
|-----------|-------|
| CAMPAIGN_SEASONS | 50 |
| TURMOIL_CAP | 12 |
| CONSENT_RATE | 0.28 |
| TREATY_LAPSE_RATE | 0.90 |
| RM_PT_DECAY_CHANCE | 0.35 |
| RM_GROWTH_PER_ARC | 1 |
| RM_VARFELL_COOPTION_BONUS | 0.1 |
| EINHIR_I_GATE | 4 |
| EINHIR_PT_OB_WEIGHT | 1 |
| ALTONIAN_I_GATE | 5 |
| PARL_MAJORITY_OB_BONUS | 2 |
| Victory threshold | 11/15 |
| EA throttle | every-arc |

### §5.2 Results at N=1000

| Faction | Win % | End L (avg) | End Terr (avg) |
|---------|-------|-------------|----------------|
| Crown | 24.7% | 3.4 | 0.8 |
| Church | 28.6% | 4.8 | 0.5 |
| Hafenmark | 24.2% | 5.6 | 0.6 |
| Varfell | 22.5% | 2.3 | 1.0 |

Deviation from 25%: **7.2pp** total. Spread: **6.1pp**. All factions in 20–30% band.

Secondary metrics: Direct sovereignty 4.7%. Almud deposed 64.9%. Turmoil mean 12.2.

### §5.3 Stable config variants (all confirmed balanced N=1000)

| Config | Cr | Ch | Ha | Va | Dev |
|--------|----|----|----|----|-----|
| RM0.35/treaty0.9/con0.28 | 24.7 | 28.6 | 24.2 | 22.5 | 7.2 |
| RM0.35/treaty0.95/con0.28 | 24.7 | 28.7 | 24.0 | 22.6 | 7.4 |
| RM0.35/treaty0.95/con0.3 | 26.3 | 28.0 | 23.1 | 22.6 | 8.6 |
| RM0.35/treaty0.9/con0.3 | 26.9 | 27.7 | 22.6 | 22.8 | 9.2 |
| RM0.35/treaty0.92/con0.3 | 26.9 | 28.1 | 22.5 | 22.5 | 10.0 |

Balance is robust across the parameter neighborhood. Treaty lapse 0.9–0.95 and consent 0.28–0.30 are interchangeable within this band without breaking balance.

---

## §6 Iteration History (What Failed and Why)

### §6.1 v12a — initial implementation

Parliamentary Transfer without CB requirement. Crown I=5 vs others' L=4–5 made it trivially easy for Crown. Crown 90%+ win rate. All non-Crown factions spiraled to 0 territories via Punishment cascade.

Fix: CB requirement, Crown-only auto-justification below 6 territories, protect last territory.

### §6.2 v12a — Einhir PT ceiling

Original design: Einhir only targets territories with PT ≤ 1. At game start, only T15 (Askeheim, Uncontrolled) qualifies. Gate too restrictive — Einhir almost never fires.

Fix: PT as Ob component instead of ceiling. RM degrades PT over time, creating targets organically.

### §6.3 v12b — Einhir death spiral

Einhir Failure cost Sta−1. Varfell attempted ~11 Einhir actions per campaign, failing ~40%. 217 Sta losses across 50 campaigns → Varfell collapses → own territories revolt → Uncontrolled → Einhir tries to reclaim → fails → more Sta loss. Varfell 0% win rate with Einhir ON vs 12% with Einhir OFF.

Fix: No Sta penalty on Failure. Limit to 1/arc. Cultural revival is soft power — failure is "not yet", not backlash.

### §6.4 Altonian over-buff

Mil+1 on Success (automatic, every arc, no cost) pushed Hafenmark to 39–45%. Mil compounds because higher Mil → better Military Conquest → more territory → more scoring.

Fix: Permanent gain only on Overwhelming. Gate raised to I≥5.

### §6.5 Church collapse under RM

RM at any strength degraded Church to 14–16%. Church's institutional power depends on PT for Piety Spread, EA effectiveness, and Seizure. RM erodes this base.

Fix: (a) Inquisitor-held territories resist RM. (b) EA throttle loosened to every-arc (from every-other-arc). This was the single most impactful change — Church went from 16% to 28%.

---

## §7 Sensitivity Analysis

The balanced config sits in a stable neighborhood. Key sensitivities:

| Lever | Effect per unit change |
|-------|----------------------|
| RM_PT_DECAY_CHANCE +0.05 | Varfell +2pp, Church −2pp |
| TREATY_LAPSE_RATE +0.05 | Crown −1pp, distributed to others |
| CONSENT_RATE +0.05 | Crown +3pp, others −1pp each |
| EA throttle (every-arc vs every-other-arc) | Church ±12pp (largest single lever) |
| EINHIR_I_GATE ±1 | Varfell ±2pp (minor — RM does the heavy lifting) |
| ALTONIAN_I_GATE ±1 | Hafenmark ±1pp (minimal impact — gain too rare) |
| Campaign length +10 seasons | Crown −2pp, challengers +0.7pp each |

**Highest-sensitivity levers in priority order:**
1. EA throttle (binary: every-arc vs every-other-arc)
2. Consent rate (continuous)
3. Treaty lapse rate (continuous)
4. RM decay chance (continuous)

---

## §8 Open Items and Flags

### §8.1 Almud deposition rate

65% of campaigns end with Almud deposed. Crown wins as institution even when Almud personally collapses. This may be canonical (Valorsmark survives its king) or a problem. Jordan decision required.

### §8.2 Direct sovereignty rate

Only 4.7% of campaigns end with decisive territorial victory. 95% end by scoring tiebreaker. This may indicate the victory threshold (11/15) is still too high, or that the game naturally produces contested endings. Jordan decision on whether more decisive outcomes are desired.

### §8.3 Treaty lapse rate narrative

90–95% lapse is mechanically necessary but may feel unrealistic. Alternative: Treaty maintenance as an active Crown action (Senator Outward to renew, creating opportunity cost). Would require sim re-validation.

### §8.4 Varfell end-state Legitimacy

Varfell ends campaigns at L≈2.3 on average. They win via territory count and RM cultural spread, not institutional legitimacy. This matches their canonical identity as military outsiders who conquer rather than govern — but may create a disconnect between winning and narrative coherence.

### §8.5 Decisions deferred from Phase 1

The following Phase 1 decisions were superseded by the parameter sweep but should be formally ratified:
- Q-21: EA throttle → **every-arc** (changed from RC-v1's every-other-arc)
- Treaty Expiration → **ratified at 90–95%/arc**
- Co-Victory threshold → **11/15** (confirmed)
- Campaign length → **50 seasons** (confirmed)

---

## §9 Simulator Code Reference

Simulator: `mc_v12c.py` (local working copy at `/home/claude/mc_v12c.py`).

Depends on: `mc_v4.py` (base classes, canonical territories, roll/resolve), `mc_v5.py` (v5 action system), `mc_v6.py` (v6 outcomes, PARAMS), `mc_v8.py` (v8 seasonal reset), `prob_engine.py` (stub).

All sourced from `designs/audit/2026-05-14-balance-audit/sim/` in `jordanelias/ttrpg`.

v12c is a working-session file — not yet committed. Canonical citation pass required before commit per sim_fabrication_check (every mechanical constant needs `# [canonical: path §section]` comment).

---

## §10 Canonical Source Cross-References

| Mechanic | Canonical source |
|----------|-----------------|
| Starting territories | `peninsular_strain_v30 §2.1` |
| Territory adjacency | `designs/world/adjacency_map.jsx` / `designs/territory/settlement_adjacency_v30.md` |
| Faction starting stats | `params/factions_personal.md` |
| Faction unique actions | `params/bg/faction_actions.md` |
| Dynastic Proclamation | `params/bg/faction_actions.md §Dynastic Proclamation` / `peninsular_strain_v30 §5.3` |
| Varfell military-only | `faction_actions §Varfell` / PP-664 (Cultural Reformation STRUCK) |
| EA degree table | `params/bg/faction_actions.md §Ecclesiastical Appointment` |
| Crown Initiative | `designs/audit/2026-05-14-balance-audit/part10_crown_initiative_design_2026-05-14.md` |
| Vaynard's Settlement/Hall | Part 10 §5.3 / Part 13 §4.2 |
| Charter of Liberties | Part 13 §4.2 |
| Treaty Expiration | Part 13 §4.3 |
| Asymmetric balance (rejected) | Part 13 §3 |

---

*Session: balance-vectors · 2026-05-14 · Convergence achieved at v12c.*
*Equal probability target met: all factions 20–30% across 5 confirmed configs at N=1000.*
*Handoff-ready for parallel session on same subject.*
