# F-33B STRESS TEST — Martial Law Option B
## Valoria Simulator · Mode A (Isolation) + Mode D (Edge Cases)
### Date: 2026-03-27 · Mechanic: F-33 Martial Law Variant B

---

## OPTION B DEFINITION

**Martial Law (B):** Suspends all Domain Actions in affected territories except Military. Only Löwenritter and Crown may act openly. All other factions must succeed at a Covert action (Ob 3) to operate at all.

**Option A (implemented)** for comparison:
- Non-Military actions need secondary Military check (Ob 2) to proceed — blocked on failure
- All factions except Crown + Löwenritter must pass Covert Ob 3 to act openly
- Duration: PC Influence vs Ob (Military ÷ 2) OR TC < 40

---

## TEST B-01 — ISOLATION: What does "Military actions only" mean?

### Input Space
| Variable | Range | Notes |
|---|---|---|
| Territories under Martial Law | 1–8 (all Crown) | Crown holds up to 8 at start |
| Factions attempting to act | All 8 + Löwenritter | Löwenritter exempt |
| Seasons under Martial Law | 1–indefinite | No defined exit condition in B |

### Finding B-01-A: "Military actions only" is undefined
**Setup:** Martial Law (B) suspends all Domain Actions "except Military." But there is no category of Domain Action labelled "Military" in the faction system. Domain Actions use the personal roll + faction stat; the military faction stat is one of six stats, not a type of action.

**Mechanism:** A faction "military" action (e.g., Crown conquering a territory) uses Military stat as the pool — but so does Löwenritter suppression, Altonian proxy operations, and Templar deployment. The category boundary is ambiguous.

**Severity: P2** — confusing at the table; GM must adjudicate case-by-case what counts as "military."

**Option A avoids this entirely** — it doesn't categorise actions, it adds a secondary check. Any action can proceed if the Military check passes.

---

## TEST B-02 — ISOLATION: Exit condition analysis

### Option B has no defined exit condition
**Setup:** Option B specifies duration as: "until PC-driven action removes it" — but provides no Ob or procedure. Option A specifies Influence vs Ob (Military ÷ 2, min 3) OR TC < 40.

**Finding B-02-A:** Without a defined removal procedure, Martial Law under Option B is potentially permanent. At Military 5 (Löwenritter starting value), Option A gives Ob 3 (5 ÷ 2 = 2.5, round up = 3). At P(≥3 net successes with a typical 6D Influence pool): ~45%. Achievable within 2–3 seasons. Option B has no equivalent.

**Severity: P1** — permanent Martial Law collapses faction gameplay. No other factions can act; the campaign freezes.

---

## TEST B-03 — INTERACTION: Covert Ob 3 for all non-Crown/Löwenritter factions

### Probability Analysis
**Ob 3 Covert action at TN 7, pool = Intel stat:**

| Faction | Intel | Pool | P(≥3 net) | Seasons to act reliably |
|---|---|---|---|---|
| Church | 4 | 4D | ~25% | ~4 seasons per action |
| Hafenmark | 3 | 3D | ~15% | ~7 seasons |
| Varfell | 5 | 5D | ~35% | ~3 seasons |
| Guilds | 3 | 3D | ~15% | ~7 seasons |
| Niflhel | 4 (covert specialist) | 4D + Quiet −1 Ob → Ob 2 | ~50% | ~2 seasons |
| Revolution | 3 | 3D | ~15% | ~7 seasons |

**Finding B-03-A:** Under Option B, Church effectively cannot act during Martial Law (~15–25% per season). The primary TC-driving faction is neutralised. TC growth stalls. This is a campaign-arc consequence that may be desirable (players triggered the coup to stop TC) OR may produce an unintended hard stop on the TC clock.

**Finding B-03-B:** Niflhel is barely affected (−1 Ob already on covert ops → effectively Ob 2, P ≈ 50%). Martial Law advantages Niflhel disproportionately — the faction best positioned to operate under Martial Law is the criminal network, not the Crown's allies.

**Severity: P2** — creates systematic faction imbalance. Niflhel emerges stronger from every Martial Law event.

---

## TEST B-04 — EDGE CASE: What if players want to use the coup strategically?

**Setup:** Players intentionally trigger coup (push Torben loyalty to 3, let TC hit 40) to impose Martial Law as a tool against the Church. Under Option B, Church cannot act for however long Martial Law persists with no clear exit.

**Mechanism:** If Martial Law permanently suspends Church Domain Actions and Church cannot remove it (Covert Ob 3, ~25% per season), players have found a dominant strategy: trigger coup early, freeze Church, win the TC clock by attrition.

**Finding B-04-A (Optimal Play — Mode D):** Option B creates a coup-as-weapon dominant strategy. A sufficiently motivated party can engineer Martial Law by season 3–4 (push Torben loyalty via neglect, let TC rise naturally). This freezes the primary TC driver for the rest of the campaign.

**Severity: P1** — trivializes TC clock management.

---

## TEST B-05 — COMPARISON: Option A vs B summary

| Criterion | Option A | Option B |
|---|---|---|
| "Military action" ambiguity | None — no category required | P2 — undefined category |
| Exit condition | Defined (Influence Ob 3 or TC < 40) | Undefined — P1 |
| Church suppression | Partial (Ob 2 check, ~70% pass at Mandate 4) | Near-total (~25% per season) |
| Niflhel advantage | Moderate (Covert Ob 3 same as others) | Significant (−1 Ob → Ob 2 ≈ 50%) |
| Dominant strategy risk | Low | High (coup-as-weapon P1) |
| Crown / Löwenritter can still be opposed | Yes (factions can act with Ob 2 check) | No (factions effectively locked out) |
| Gameplay texture | Faction play continues under constraint | Faction play pauses |

---

## VERDICT

**Option B introduces two P1 issues (no exit condition; coup-as-weapon dominant strategy) and one P2 (categorical ambiguity), with no compensating mechanical advantages over Option A.**

Option A produces a more interesting play experience: factions remain active but constrained, the Martial Law creates pressure rather than a freeze, and the exit condition gives players clear agency.

**Recommendation: Option A (already implemented) is correct. Option B should not be adopted.**

---
*Simulation complete — 2026-03-27*
