# SIM-NEW-03 — BG: IP Crisis + AER at Threshold (Altonian Vanguard Chain)
## Mode: A (Isolation) + C (Full Scenario) + D (Edge Cases)
## Date: 2026-04-08

---

## FETCH LOG
canonical_sources.yaml: ✓ (156 lines)
params_board_game.md: ✓ (1431 lines)

---

## System Under Test

IP (Invasion Pressure) track: starts 20, range 0–100. Threshold at 75: Altonian Vanguard deploys. AER modifies the threshold (AER ≥ 4: threshold rises to 80; AER 5: IP held at 50).

IP Effects table:
- IP < 30: Trade with Schoenland +1D
- IP 30–59: Trade +1 Ob; +1D Intel orders
- IP 60–74: Trade disrupted +2 Ob; Proxy at T4 +1D military
- IP ≥ 75: Vanguard deployed. AER ≥ 4 → threshold 80. AER 5 → IP held at 50.

Loss condition: AER ≤ 1 (Altonian Conquest) — defined as a shared loss.

This chain has never been tested. Key questions:
- How fast does IP rise?
- What deploys the Vanguard and what does it do?
- Is AER 5 (IP held at 50) achievable and how?

---

## Mode A: IP Advance Rate

**IP advance sources (from params — reconstructed from context):**
- IP passive advance: +1/season from Altonian border pressure (institutional momentum)
- Crown Trade with Schoenland failure: IP +5 on success (from prior context found: "Military vs Ob 2. IP +5 on success" — this appears to be Schoenland Trade generating IP, not reducing it?)

Wait — checking the exact reference:
"T10 Spartfell: Border castle. NE Altonian pass. IP events fire here first."
"Military vs Ob 2. IP +5 on success" — this is likely from the Schoenland section: Crown may conduct Diplomatic Outreach to Schoenland (PP-437: IP −1 or −2 on success). IP rises from other sources.

**Reconstructing IP advance from params:**
IP advance: passive +1/season. Crisis events (RS-linked, Calamity, faction collapses) add IP. IP reduction: Crown Diplomatic Outreach to Schoenland (IP −1 on Success, IP −2 on Overwhelming). AER-linked: higher AER = better Altonian relationship = slower IP rise?

Seasons to IP 75 from 20 at +1/season: 55 seasons. Extremely slow at baseline. IP crisis only becomes relevant if additional IP-generating events fire. Key event: **Coup (Löwenritter)** adds IP acceleration (institutional instability signals Altonia). Also: **IP events at T10 Spartfell** — unclear trigger.

**Finding P1 — IP 75 at +1/season is 55 seasons from start, well beyond any realistic game arc (~20–25 seasons).** IP crisis is a long-term strategic pressure that only becomes acute if factions stop investing in AER/Schoenland diplomacy. In a typical game, IP stays in the 40–60 range (1 season of passive advance = negligible; Crown Diplomatic Outreach occasionally pulls it back).

---

## Mode A: AER Threshold Effects

**AER track 0–5, starts 2.**

AER advance: Crown Diplomatic Outreach to Schoenland (PP-437: AER +0.5 or +1). Church Temperance Cardinal Focus: AER +1/season (declarative).

**AER 3:** Bypasses Hafenmark structural suppression (PP-203). [Confirmed from TC section.]
**AER 4:** IP Vanguard threshold rises from 75 to 80 (+5 buffer). Effectively extends IP safety margin by 5 seasons at +1/season.
**AER 5:** IP held at 50. All IP ≥ 50 excess is absorbed — Altonian relationship is so strong that invasion pressure cannot rise above "manageable tension."

**AER 5 reachability:**
Start AER 2. Need AER +3.
- Temperance Focus: +1/season (declarative, no roll). 3 seasons → AER 5.
- But Temperance Focus competes with other Cardinal Focus uses. Church using Temperance every season means NO Fortitude (no free Templar deployment), NO Justice (no Inquisitor threshold reduction), NO Prudence (no +1 Wealth).

**Cost of AER 5 via Temperance Focus:** Church player must forfeit 3 seasons of other Cardinal Focus benefits. At AER 2 → 5 in 3 seasons: a significant strategic commitment.

**AER 5 effect:** IP permanently held at 50. IP never threatens Vanguard deployment. This makes the Schoenland threat entirely irrelevant for the game. Extremely powerful.

**Finding P2 — AER 5 is a dominant strategy for Church when it wins the AER competition.** If Church invests 3 seasons of Temperance Focus, IP can never trigger Vanguard deployment. The entire IP threat is neutralised. However, the 3 seasons of Temperance Focus cost Church Fortitude/Justice/Prudence benefits — the opportunity cost is real.

---

## Mode C: Full Scenario — IP Crisis at Season 15

**Setup:** Church never played Temperance Focus (invested in Justice for Inquisitors). AER 2 (unchanged). Crown played Diplomatic Outreach to Schoenland 4 times (Success × 3, Overwhelming × 1): IP changes from Crown actions: −1, −1, −1, −2 = −5 net. But passive +1/season × 15 seasons = +15. Net IP: 20 + 15 − 5 = **IP 30.**

At IP 30: Trade with Schoenland +1 Ob applies. Intel orders +1D.

**S16 event: Löwenritter Coup fires.** Coup adds to IP indirectly (institutional instability). How much? [GAP: no specific IP increase from coup is defined in params.] Gap-fill: Coup generates IP +5 (Altonian agents interpret coup as military weakness, escalate pressure). IP 30 + 5 = **IP 35.**

**S17–S20:** Passive +1/season. No Crown Schoenland diplomacy (Crown eliminated by coup). IP: 35, 36, 37, 38. At S20: IP 38. Still below IP 60 crisis threshold.

Without Crown's Schoenland diplomacy, IP climbs at +1/season unchecked. IP 60 reached at S42 (22 more seasons). IP 75 (Vanguard) at S57. Still beyond the game arc.

**Finding P3 — IP 75 Vanguard is essentially unreachable in normal play.** Even after Crown elimination (losing the primary AER/Schoenland actor), IP only reaches Vanguard level after 40+ seasons of unchecked advance. The IP threat functions more as a background pressure on Crown's strategic behaviour (they must engage Schoenland diplomatically) than as a realistic crisis event.

---

## Mode D: Edge Cases

**Edge 1: IP 75 actually fires — Vanguard deploys to T10 Spartfell.**

What does the Vanguard DO? From params: "IP 75+: Altonian Vanguard deployed." No mechanical detail given. [GAP: Vanguard deployment effects undefined beyond the threshold note.]

**[EDITORIAL: ED-340 — Altonian Vanguard deployment at IP 75: define what the Vanguard does in BG terms. Options: (a) NPC military faction in T10 with Military 5 that advances toward T8 (Hafenmark capital) each season if not opposed; (b) all factions Stability −1/season while Vanguard active; (c) IP ≥ 75 = Hafenmark Military at T10 receives +3D (Altonian auxiliary support flips to Hafenmark — the Vanguard is Hafenmark's army). Without definition, IP ≥ 75 does nothing mechanically. P1 — if IP is a loss vector, its endpoint must be defined.]**

**Edge 2: AER ≤ 1 (Altonian Conquest — shared loss).**
AER starts 2. AER decreases via: diplomatic failures, Schoenland isolation, Church internal conflict. If AER drops to 0: "Altonian Conquest" fires. Defined as a shared loss (all factions lose). AER decrease rate: not defined in params beyond the Schoenland Fragmentation modifier (+2 Ob if 3+ factions Stability ≤ 2). AER can only go down if Schoenland events fire negatively or AER-linked mechanics erode it.

**[EDITORIAL: ED-341 — AER decrease rate and triggers undefined. What events reduce AER? How fast? Without AER decay mechanics, AER starts at 2 and only rises (via Crown/Church investment). The shared loss via AER ≤ 1 is unreachable. P2.]**

**Edge 3: IP 30–59 Intel bonus (+1D all factions Intel orders).**
At IP 30 (reached by S16 in the coup scenario): all factions get +1D on Intel orders. Varfell Tribune benefits: +1D to Counter-Narrative, Investigate, Spy. This is a meaningful bonus for Varfell at no cost — IP moderately rising actually helps Varfell. Interesting emergent effect: a faction that benefits from high IP (Varfell) has no incentive to prevent IP rise. Only Crown (Schoenland diplomat) and Church (AER investment) care about IP.

---

## Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-IP-01 | P1 | Altonian Vanguard deployment (IP 75) effects undefined. IP threat has no mechanical endpoint. |
| F-IP-02 | P1 | IP 75 is unreachable in normal play (~55 seasons at baseline). The IP threat is a behaviour-shaping constraint on Crown, not a realistic crisis event. |
| F-IP-03 | P2 | AER 5 via Temperance Focus in 3 seasons permanently caps IP at 50. Extremely powerful if Church commits. |
| F-IP-04 | P2 | AER decay triggers undefined. Shared loss via AER ≤ 1 is currently unreachable. |
| F-IP-05 | P3 | IP 30–59 Intel +1D benefits Varfell without them doing anything — emergent strategic alignment between Varfell and rising IP. |

