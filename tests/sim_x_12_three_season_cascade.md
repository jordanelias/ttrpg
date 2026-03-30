# SIM-X-12: Three-Season Cascade — All Outcomes Compound
## Mode: D (Edge case) + E (Coverage)
## Mechanics: Full clock system × Faction accounting × Cross-clock interactions × All named NPCs
## Context: Seasons 1–3 post-campaign-start. All SIM-X-05 through X-11 outcomes applied in sequence. Tests compound clock behaviour, faction stat floors/ceilings, and identifies cascade failure modes.

---

## Season 1 Summary (from SIM-X-05 through X-10)

**Events:**
- Himlensendt wins Grand Debate 5–0 (X-05)
- Ehrenwall killed in mass battle (X-07)
- Baralta Doctrine: Partial result (TC −1)
- Baralta Evidence chain (Olafsson): Success (Church Stability −2, TC −3)
- Himlensendt Appeal: Success (TC +1)
- RS cross-clock: RS 28 < 40 → TC +2/season (Church Stability brake check)
- Church Stability brake: Stability 3 < 5 → TC generation suppressed (interpretation A)
- IP passive drift: +1

### Season 1 Clock End State
| Clock | Start | Debate | Battle | Doctrine | Evidence | Appeal | Cross-clock | End |
|-------|-------|--------|--------|----------|----------|--------|-------------|-----|
| RS | 28 | 28 | 28 | 28 | 28 | 28 | 28 | **28** |
| TC | 22 | 22 | 22 | 21 | 18 | 19 | suppressed | **19** |
| IP | 20 | 20 | 20 | 20 | 20 | 20 | +1 | **21** |

### Season 1 Faction States
| Faction | Mandate | Influence | Stability | Notes |
|---------|---------|-----------|-----------|-------|
| Crown | 5 | 5 | 4 | No change |
| Church | 5 | 6 | **3** | Stability −2 from Evidence chain |
| Hafenmark | 4 | 4 | 4 | Baralta: +1 Ob social vs Church (1 season) |
| Varfell | 4 | 4 | 4 | Vaynard TK: 1→2 |
| Löwenritter | — | 3 | 5 | Ehrenwall dead; stability check passed |

### Season 1 NPC State
| NPC | Change |
|-----|--------|
| Vaynard | TS 14→30 (Discovery Event) |
| Klapp | TS ~40→50 (CE chain), CE=6, Coherence 9, Conversion trajectory |
| Vald (Inquisitor) | CE 3, TS growth threshold |
| Ehrenwall | Dead |
| Olafsson | Suspended |

---

## Season 2 (from SIM-X-09, X-11)

**Events:**
- Vaynard audience with Almud: Vaynard wins 3–0, TK 1→2 (wait — TK was already 2 from season 1 Vaynard sim; re-checking: X-09 set TK 2 as endpoint of that sim, X-11 advanced TK 2→3 from Maret's archive extraction)
- Maret archive infiltration: Partial, TK advances to 3, TC +1 (TK3 Church attention)
- Klapp Conversion confirmed mechanically

### Season 2 Clock Adjustments

**Starting clocks:** RS 28, TC 19, IP 21.

**Events this season:**
1. TK3 triggers: TC +1 → TC: 19→20.
2. Vaynard TK2 from X-09: no TC effect (TK2 = "no TC effect"). Already accounted for.
3. Maret X-11 domain echo: TK→3 (TC +1 applied above).
4. RS cross-clock: RS 28 < 40 → TC +2/season. Church Stability: 3 (still < 5 from Season 1). Church Stability brake still active? Stability can recover. Season 2 start: no recovery actions taken → Stability stays at 3. Brake active.
5. With brake active: TC generation suppressed again.
6. IP passive drift: +1 → IP: 21→22.

### Season 2 Clock End State
| Clock | Start | TK3 trigger | Cross-clock (braked) | IP drift | End |
|-------|-------|-------------|---------------------|----------|-----|
| RS | 28 | 28 | 28 | 28 | **28** |
| TC | 19 | 20 | suppressed | — | **20** |
| IP | 21 | 21 | 21 | +1 | **22** |

### Season 2 Faction States
| Faction | Mandate | Influence | Stability | Notes |
|---------|---------|-----------|-----------|-------|
| Church | 5 | 6 | 3 | No recovery |
| Varfell | 4 | 4 | 4 | TK=3, succession leverage active |

**Church Stability at 3 for two consecutive seasons.** The Stability brake has now suppressed TC +2/season for two consecutive seasons that would otherwise have occurred. Without the brake, TC would be at 19+2+2 = 23. The brake has saved 4 TC points over two seasons.

**Finding F-51 [P2]:** Sustained Church Stability depression (from Olafsson exposure) is the single most effective long-term TC suppression mechanism available — more impactful than the Doctrine action itself. The Olafsson Evidence Chain (TC −3 + Church Stability −2) produces cascading suppression every season as long as Stability stays low. This creates a dominant strategy: expose Olafsson early, keep Church Stability below 5 indefinitely through continued pressure.

---

## Season 3: Church Stability Recovery Attempt

At Stability 3, the Church is in internal crisis. Himlensendt (Presence 6, Cognition 5) attempts to restore institutional coherence.

**Church Stability recovery:** No explicit Stability recovery mechanic defined for external damage in faction rules. §6 defines "Stability check" (triggered by deviation) but not Stability restoration. 

**Finding F-52 [P1 — gap]:** No explicit Stability recovery mechanic for externally damaged faction Stability. The rules define Stability checks (which can reduce it) but no formal recovery path. A Faction can presumably recover through Domain Actions that strengthen institutional cohesion — but the Ob, pool, and rate are not specified. This is a rules gap. [GAP: Faction Stability recovery — no rule defined.]

**Working assumption for simulation:** Himlensendt attempts an Appeal to Cardinals (internal, not public) — Presence 6 + History Theology 3 = 12D TN7 vs Ob2 (own faction, warm disposition). P(≥2 net) ≈ 87%. Success → Church Stability +1 (GM-ruled rate: 1 per season max via internal coordination). Church Stability: 3→4.

At Stability 4: still below 5. Brake still active in Season 3.

**Season 3 opening clocks:** RS 28, TC 20, IP 22.

### Season 3 Events

1. **Baralta social penalty expires** (it was 1 season; Season 2 is the penalty season, Season 3 is clear). Baralta can now use full pool against Church.

2. **Church Stability: 4.** Brake still active (needs ≥5 to deactivate). TC generation suppressed.

3. **IP cross-clock:** IP 22 < 30 (Dormant band; no active pressure modifiers). Passive drift +1 → IP: 22→23.

4. **RS passive drift:** −1 per 4 seasons. 3 seasons in: not yet at 4-season mark. No RS passive drift yet.

5. **Vaynard TK=3 active:** "Succession leverage formally linked to Southernmost access terms." Almud must now address TK=3 demands formally. This produces a Domain Action from Vaynard: succession ratification negotiation.

   Vaynard Domain pool: 11D TN7 (personal pool from debate) vs Ob = Crown Mandate = 5.
   P(≥5 net from 11D) ≈ 36%. Most likely: Partial.
   Partial: Almud acknowledges Southernmost access in principle but does not ratify.
   TK stays at 3; no TC effect (TK3 already applied).

6. **Vald's Investigation (Maret):** Stage 2 Formal Accusation. Church Reach 6D (Olafsson still suspended; Stability 4 → minor recovery). P(6D TN7 vs Ob4) ≈ 47%. 
   Most likely: Partial again. Accusation in draft. Stage 2 stalls.
   
   But: Klapp (TS 50, Conversion) is now aware of the Maret investigation. He has access to the file (Cardinal of Scholarship = oversight of educational investigations). He could suppress the investigation as an institutional act. This is [EDITORIAL: requires user decision on Klapp's action].

7. **Ehrenwall succession — Löwenritter.** No named successor. Löwenritter Stability check Season 3 (continued leadership vacuum): Stability 5 vs Ob2. P(≥2 net from 5D TN7) ≈ 55%. Close call.

   If it fails: Stability 5→4. Löwenritter in institutional crisis. If Coup Counter was inherited, it freezes or resets. If not: the faction drifts without the Coup threat.

   Most likely: passes (55%). Stability holds at 5.

### Season 3 Clock End State
| Clock | Start | Season events | Cross-clock (braked) | IP drift | End |
|-------|-------|---------------|---------------------|----------|-----|
| RS | 28 | 28 | 28 | — | **28** |
| TC | 20 | 20 | suppressed | — | **20** |
| IP | 22 | 22 | — | +1 | **23** |

---

## Three-Season State Summary

| Clock | Season 0 (start) | Season 1 | Season 2 | Season 3 |
|-------|-----------------|---------|---------|---------|
| RS | 28 | 28 | 28 | 28 |
| TC | 22 | 19 | 20 | 20 |
| IP | 20 | 21 | 22 | 23 |

**RS: unchanged** across 3 seasons. No Thread operations produced RS movement (all ops at Object/Personal scale or successful Weaving at low scale). RS stability is expected at this stage.

**TC: net −2** over 3 seasons (from 22 to 20). This is a significant player-side victory — without the Doctrine + Evidence Chain, TC would have risen to 22+6 (cross-clock, 3 seasons) = 28 by Season 3. Actual TC is 20 instead of 28. The Stability brake alone saved 6 TC points.

**IP: +3** over 3 seasons (all passive drift). No IP-reducing events simulated.

---

## Cascade Failure Mode Analysis

**Scenario: What if Church Stability recovers before Olafsson suspended?**

If Himlensendt had launched a pre-emptive Appeal before the Evidence Chain landed (Season 1): Church Stability check at Ob3 for recovery — but Stability checks only fire on deviation, not proactively. No pre-emptive stability increase is possible.

**The Stability brake is essentially irreversible once triggered** — it takes 1 season per point to recover (GM assumption; no formal rule), meaning Church Stability at 3 takes 2 seasons to reach 5 again. During those 2 seasons: ~4 TC points suppressed. This is the most powerful anti-TC mechanism in the game and requires no Thread work, only legal evidence and one social action.

**Finding F-53 [P2]:** The Olafsson Evidence Chain is disproportionately powerful relative to its mechanical cost (players supply evidence, Baralta makes one Domain roll at 14D vs Ob3). The combined TC impact over 3 seasons (~6–7 TC suppression) is larger than any single Thread operation can produce.

---

## Cross-Mechanic Audit: 3-Season Chain

| Chain | Fired correctly? | Issue? |
|-------|----------------|--------|
| RS cross-clock → TC suppressed by Stability brake | Ambiguous (F-45); interpretation A taken | Gap |
| Faction Stability recovery rate | No rule; GM improvised 1/season | Gap (F-52) |
| TK3 → TC+1 (Varfell attention) | Correct per §13 | OK |
| Domain Echo success rate vs Mandate-level Ob | 42% at Ob5; correctly predicted Partial | OK |
| Coup Counter terminal on Ehrenwall death | Confirmed gap (F-30/F-33) | Gap |
| Church Stability brake persisting 2+ seasons | Correct; no auto-recovery rule | Design concern (F-51) |

---

## All P1 Findings Requiring Editorial Decision (Complete Register)

| ID | Source | Description |
|----|--------|-------------|
| F-11 | X-03 | W-33 broken for CP≤2 units |
| F-27 | X-07 | Mass battle deadlock — no stalemate resolution rule |
| F-30 | X-07/08 | Coup Counter: no successor rule on Grandmaster death |
| F-33 | X-08 | Confirmed F-30 |
| F-43 | X-10 | Two Domain Actions can drop TC by 4+ in one season; no seasonal cap |
| F-45 | X-10 | Church Stability brake: does it suppress RS-driven TC cross-clock increase? |
| F-52 | X-12 | No Stability recovery mechanic for externally damaged faction Stability |

## All P2 Findings (Open, No Editorial Required Unless Desired)

| ID | Source | Description |
|----|--------|-------------|
| F-04/F-07 | X-01 | W-24 balance entirely depends on Leap vulnerability |
| F-10 | X-02 | W-40 series exchange cost disproportionate |
| F-19 | X-05 | 11D vs 8D pool gap predetermines Grand Debate |
| F-21 | X-05 | High-Composure NPCs immune to Rattled in 5-exchange Debates |
| F-24 | X-06 | Range mismatch more decisive than pool differential |
| F-29 | X-07 | Thread formation-loosening ops irrelevant against weapon/armour deadlock |
| F-31 | X-07 | Mass battle stalemate lacks defined resolution mechanism |
| F-36 | X-08 | Stalemate battles produce zero faction consequences |
| F-39 | X-09 | TS growth cascade requires three ~63% checks (chain P≈25%) |
| F-41 | X-09 | No formal rule for Impression events in social scenes |
| F-51 | X-12 | Church Stability brake dominant TC suppression mechanism — possibly overtuned |
| F-53 | X-12 | Olafsson Evidence Chain disproportionately powerful (6–7 TC over 3 seasons, 14D vs Ob3) |
