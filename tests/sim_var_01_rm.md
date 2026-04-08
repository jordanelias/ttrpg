# SIM-VAR-01 — Board Game: Restoration Movement Arc
## Mode: C (Full Scenario) + G-BG + A (Mechanic Isolation) + J (Precedent)
## Date: 2026-04-08 | Canonical sources: params_board_game.md, victory_architecture_v1.md

---

## FETCH LOG
canonical_sources.yaml: ✓ (156 lines)
params_board_game.md: ✓ (1348 lines)
params_factions.md: ✓ (517 lines)
victory_architecture_v1.md: ✓ (393 lines)

---

## Scenario Setup

**5-player game.** RM is the fifth player.
**RM victory requires (§3.5):** ≥ 5 territories at CV ≤ 1 + RM Presence markers ≥ 5 in ≥ 5 non-adjacent territories + RS ≥ 40. Held 2 consecutive Accounting steps.

**Starting state:**
| Faction | M | I | W | Mil | Sta | TCV |
|---------|---|---|---|-----|-----|-----|
| Crown | 5 | 5 | 4 | 4 | 4 | 12 |
| Church | 5 | 6 | 5 | 4 | 5 | 3 |
| Hafenmark | 4 | 4 | 5 | 3 | 4 | 8 |
| Varfell | 4 | 4 | 4 | 4 | 4 | 6 |
| Restoration | 2 | 4 | 2 | 0 | 3 | 0 |

TC: 28. RS: 72. Warden Cooperation (WC): 0. Warden's Accord (WA): 0.

**RM starting position:** No territories. 0 Presence markers. Must build from nothing.

---

## Phase 1: RM Action Economy Analysis (Mode A — Isolation)

RM has two primary actions:
- **Community Organising (Consul Outward):** Ob 2. Effect: place Presence marker in territory.
- **Community Weaving (Thread op):** Ob = (100−RS)÷20 round up, min 1. Effect: CV −1 in territory + Co-Movement auto-effects.

At RS 72: Weaving Ob = (100−72)÷20 = 28÷20 = 1.4 → Ob 2.
At RS 50: Weaving Ob = 50÷20 = 2.5 → Ob 3.
At RS 40: Weaving Ob = 3. (This is RM's victory RS threshold — Weaving gets harder exactly when RM needs RS highest.)

**RM pool:** Mandate 2 for most actions. Community Weaving uses Thread pool (Attunement-based, likely Weaver NPC stat). For BG abstraction: RM Presence markers provide −1 Ob to Weaving per marker in territory.

**Presence marker placement:** Community Organising (Consul Outward, Ob 2, pool = Mandate 2D). P(Success at 2D vs Ob 2) ≈ 22%. P(Overwhelming): ~5%. P(Partial): ~36%. P(Failure): ~42%.

**Finding P1 — RM action economy is brutally thin:**
At Mandate 2, RM fails Community Organising 42% of the time. With PP-403 (failed Domain Action = Stability −1), RM fails itself into Stability collapse. Starting Stability 3, three consecutive failures = Stability 0.

**Resolution required:** Does PP-403 apply to RM's Community Organising? PP-403 scope: "Domain Actions only; not self-improvement." Community Organising targets a territory (places Presence marker) — it's an outward action, not self-improvement. PP-403 applies. RM's low Mandate creates an existential fragility: they cannot sustain a failure streak.

**Mitigation available:** Warden Cooperation (WC) effects — WC ≥ 1 grants +1D to all Thread operations. Does this apply to Community Organising? Community Organising is a Consul Outward, not a Thread op. No WC benefit. Community Weaving IS a Thread op → WC applies.

**Conclusion:** RM's Organising path (Consul Outward) is bottlenecked by pool 2. RM should: first stabilise Mandate (reaching M ≥ 3 unlocks Ob 2 rolls at ~40% success), then expand Presence. But Mandate-building is itself a Domain Action at Ob 2 pool 2. Bootstrapping problem.

---

## Phase 2: RM Early Game — Seasons 1–4

### Season 1
**RM action:** Community Organising in T6 (Stillhelm, Crown-controlled, Proximity 1). Why T6? Adjacent to T15 (Askeheim) — Warden Emergence proximity. RM Presence in T6 eventually enables Warden Contact.
Roll: Mandate 2D vs Ob 2. 
**Result: Partial** (net 1, Ob 2). No Presence placed. No Stability cost (Partial ≠ Failure). RM does nothing effective in S1.

**Other factions:** Crown expands toward TCV 16. Church holds T9, accumulates TC passively (TC 29). Hafenmark plays Parliamentary Manoeuvre. Varfell builds VTM.

### Season 2
RM: **Community Organising in T6 again.**
Roll: 2D vs Ob 2. **Result: Failure.** Stability −1 → Stability 2. First Presence marker still not placed.

**Finding P2 — RM requires early external assistance or lucky streak to survive to viability.**
At Stability 2, RM can absorb one more Failure before triggering Stability Check → elimination risk.

### Season 3
RM: **Community Organising in T13 (Oastad, Varfell-controlled, Proximity 1, Einhir ruins: Weaving −1 Ob).** Switch territories to find a weaker anchor — but Organising Ob doesn't change by territory. Still Ob 2.
**Result: Success.** First Presence marker placed in T13. Stability 2 holds.

### Season 4
RM: **Community Weaving in T13 (now has 1 Presence marker → −1 Ob).** Weaving Ob at RS 72 = 2, minus 1 Presence = Ob 1. Plus Einhir ruins −1 Ob. Ob floor: 1. Ob 1.
Roll: Influence 4D (RM uses Influence for Thread ops) vs Ob 1. P(Overwhelming): ~97% at 4D Ob 1.
**Result: Overwhelming.** CV in T13: was 3, now CV 2. Co-Movement auto-effect fires (RS − minor, temporal/epistemic effects). WC unchanged (no Warden Emergence yet).

**State after S4:**
- RM: Stability 2, 1 Presence marker (T13), T13 CV 2.
- RS: 71 (−1 from Weaving auto-effect, approximately).
- Warden's Accord: 0 (no Warden Emergence — requires triple condition).

---

## Phase 3: RM Mid-Game — Seasons 5–10

**RM strategy becoming clear:** Stack Presence markers in 5+ non-adjacent territories. Weave CV down in each. Maintain RS ≥ 40 (critical — RS decline is the existential threat).

**Non-adjacent territory requirement analysis:**
RM needs 5 Presence markers in ≥ 5 non-adjacent territories. Adjacency graph creates constraints. Non-adjacent territories (no shared border):
- T13 (Oastad) and T5 (Feldmark): non-adjacent ✓ (T13 adj to T6, T12, T15 only)
- T13 and T2 (Kronmark): non-adjacent ✓
- T13 and T7 (Rendstad): non-adjacent ✓
- T13 and T10 (Spartfell): non-adjacent ✓
- T13 and T9 (Himmelenger): non-adjacent ✓ (T9 adj to T2, T3, T8, T14, T17)

RM needs to place Presence across the map — T13, T9, T5, T7, T10 would satisfy non-adjacency. But these are in hostile faction territories (Church controls T9, Hafenmark T7/T10, Crown T5). RM must Organise in enemy territory with Mandate 2D vs Ob 2.

**Season 5–7 goal:** Place Presence in T9 (Himmelenger, Church). Church Mandate 5 does NOT modify Organising Ob (Organising Ob is flat 2). Church can only resist by converting RM's Presence into AP (if Inquisitor active: Organising in Church territory? No — Inquisitor adds +2 Ob to Intel/Tribune actions, not Consul actions).

**S5: RM Organises in T9.** 2D vs Ob 2. **Result: Success.** Presence in T9.

**S6: RM Weaves in T9.** No Presence bonus in T9 before now (1 marker = −1 Ob). Ob = (100−71)÷20 = 1.45 → Ob 2 at RS 71. Minus 1 Presence = Ob 1. Plus T9 has Church Inquisitor? Church played Active Inquisition in S3 — assume Inquisitor in T9. But Active Inquisition Inquisitors affect Intel/Tribune. Weaving is a Thread operation (Phase 4 Priority 5). Inquisitor +2 Ob affects Tribune Investigate/Spy — does it affect Thread ops? Ruling: no — Inquisitors target Intel operations, not Thread ops. Weaving Ob unaffected by Inquisitor.

T9 CV starts at 5 (Himmelenger, high piety). Weaving target: CV −1.
**Result: Success.** T9 CV: 5 → 4. RS −1 from Weaving auto-effect → RS 70.

**S7: RM Organises in T5 (Feldmark, Crown).** Mandate 2D vs Ob 2. **Result: Failure.** Stability 2 → 1. Danger zone.

**State S7:**
- RM: Stability 1, Presence in T13 and T9. CV: T13 = 2, T9 = 4.
- RS: 70.
- RM is 3 Presence markers short of victory condition. 3 more territories needed (non-adjacent to T13 and T9).

**RM CRISIS: Stability 1 means one more Failure = Stability 0 → Stability Check → faction elimination risk.** RM cannot sustain aggressive Organising.

**S8 pivot:** RM plays **Community Weaving** in T13 (now 2+ Presence possible? No — RM only placed 1 marker in T13, in S3. But each Organising success places ONE marker. RM needs to return to T13 to stack more markers? Actually — is the −1 Ob modifier per Presence marker (multiple markers possible per territory)? Re-reading: "Ob = base Ob − 1 per Presence marker in territory." RM can stack multiple Presence markers in one territory, each reducing Ob by 1.

But the victory condition requires "≥ 5 non-adjacent territories with Presence markers" — so stacking in T13 doesn't help the count. RM needs width, not depth.

**S8: RM Weaves in T13 (CV −1 progress).** T13 CV 2 → 1. T13 now at CV ≤ 1. One territory cleared for victory condition.

---

## Phase 4: Win Path Assessment (Seasons 9–20)

**RM victory timeline:**
- Need 5 territories at CV ≤ 1: T13 at CV 1 (done after S8). Need T9, T5, T7, T10 (or similar set).
- T9 CV 4 → needs 3 more Weavings. At 1 marker: Ob 1 each. ~3 seasons of Weaving T9.
- Each new territory: 1 Organising success (build Presence) + N Weavings to reach CV ≤ 1.
- CV starting values: T5 (Crown breadbasket) starts ~3. T7 (Rendstad) starts ~2. T10 (Spartfell) starts ~2.

**Rough timeline (optimistic):**
- T13: ✓ (S8)
- T9: 3 more Weavings → done by S11
- T7: 1 Organise + 2 Weaves → done by S14 (if Organise succeeds first try)
- T10: 1 Organise + 2 Weaves → done by S17
- T5: 1 Organise + 2 Weaves → done by S20

**Season 20 earliest win.** That's 5 in-game years. Other factions can win from S6–8 (Crown at TCV 16 is plausible by S6–8 given expansion pace).

**Finding P3 — RM cannot win a race in a 4-player game.** RM's timeline (S20+) is dramatically longer than any other faction's earliest win path. RM wins only if all other factions are mutually blocking each other for 15+ seasons. This aligns with the design intent ("hardest mode, 5 players only") but the gap is stark.

**RS constraint:** RS starts 72. Weaving costs RS each use (auto-effect ~−1 per op). Over 15 seasons: ~15 Weavings = −15 RS. Baseline decay: −1/year = −3 or −4 over the arc. Other faction Thread ops add more. By S20, RS could be 72 − 15 (Weaving) − 4 (baseline) − 10 (other factions) ≈ **RS 43**. This is above RM's victory threshold of 40. Tight but achievable.

**But F-58 finding:** RS 22 proximity to Dormant threshold (RS 20) means any bad stretch drops RS through 40 into the 39–20 band, which adds +2 Ob to non-Thread in Proximity-0 territories and begins Gap auto-generation. RM's Weaving Ob increases (Ob formula rises as RS falls), making their core mechanic harder precisely as RS approaches the danger zone.

**Weaving Ob at RS 42:** (100−42)÷20 = 2.9 → Ob 3. At 1 Presence: Ob 2. Still workable.
**Weaving Ob at RS 32:** (100−32)÷20 = 3.4 → Ob 4. At 1 Presence: Ob 3. P(Success at 4D vs Ob 3): ~40%. Getting difficult.
**Weaving Ob at RS 22:** Ob 4 flat (1 Presence → Ob 3). Still technically viable but RS ≤ 20 means RM victory threshold (RS ≥ 40) is already missed — they've already lost the RS condition.

**Finding P4 — RM victory and RS floor are mutually reinforcing constraints.** RM must keep RS ≥ 40 to win. But Weaving drives RS down. RM's own core action erodes the victory condition. This is elegant design tension: RM must win before their own actions destroy the win condition.

---

## Warden Emergence — RM interaction

**Warden Emergence triple trigger:** WA ≤ −2 AND ≥ 3 territories CV ≤ 1 AND RS ≤ 50.

After S8 (T13 CV ≤ 1, RS 70): only 1 territory at CV ≤ 1 and RS 70 — trigger far from firing.
After RM clears 3 territories (S14 estimate, RS ~55): 3 territories at CV ≤ 1, RS < 50 possible. If WA ≤ −2 (requires Varfell to have aggressively expanded toward T4 without Expedition care): trigger fires.

**If Warden Emergence fires:** WR track resets to −2 for Varfell (Varfell Path B blocked). WC track shifts: WC ≥ 1 → +1D to RM Thread ops (including Weaving). RM's position improves dramatically on Warden Emergence.

**RM-Warden alignment is the decisive late-game pivot.** RM cannot accelerate enough without it. If Warden Emergence fires by S12–14, RM wins with WC bonus. Without it, RM is racing an impossible clock.

---

## Findings Summary

| ID | Severity | Finding |
|----|----------|---------|
| F-RM-01 | P1 | RM action economy at Mandate 2 is existentially fragile. PP-403 (Stability −1 on Failure) can eliminate RM in S2–4 via consecutive Failures at 42% failure rate. |
| F-RM-02 | P2 | RM win timeline (S20+) structurally cannot compete with other factions (S6–10) in a balanced race. RM wins only via mutual faction stalemate, as designed. |
| F-RM-03 | P2 | Weaving Ob rises as RS falls — RM's core action erodes its own victory condition. Elegant but unforgiving. No mitigation mechanic except Presence stacking (which requires prior Organising success). |
| F-RM-04 | P2 | Warden Emergence is RM's decisive late-game pivot. Without WC +1D bonus, RM cannot complete the win path before RS drops below 40. |
| F-RM-05 | P3 | RM requires 5 non-adjacent Presence territories — the non-adjacency constraint forces RM into hostile territory early (S4–7) when Mandate is lowest. Timing mismatch. |

**New editorial flagged:**
[EDITORIAL: ED-327 — RM bootstrap problem: Mandate 2 Organising at 42% failure rate with Stability −1 penalty creates elimination risk before RM establishes its first viable Presence base. Recommend: consider whether RM's Community Organising should be exempt from PP-403 (failed Domain Action = Stability −1) as self-preservation mechanic, OR whether RM should start with 1 Presence marker in a neutral territory. P2 — does not block but significantly affects RM playability.]

