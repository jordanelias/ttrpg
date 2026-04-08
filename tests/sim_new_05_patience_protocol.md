# SIM-NEW-05 — TTRPG: Patience Protocol Full Arc → VTM Advance → Revelation Token
## Mode: C (Full Scenario) + A (Isolation) + B (Interaction Chain)
## Date: 2026-04-08

---

## FETCH LOG
canonical_sources.yaml: ✓ (156 lines)
params_board_game.md: ✓ (1431 lines) — Patience Protocol, VTM, Revelation Tokens
params_factions.md: ✓ (559 lines)

---

## System Under Test

Patience Protocol (PP): Varfell's resource accumulation mechanic. Never tested end-to-end.

**Rules (from params_board_game.md):**
- PC range: 0–4 at VTM 0–3; 0–6 at VTM 4+.
- Gaining: +1 PC per season Tribune available but played differently; +1 PC per season pass on Senate purchase when Wealth ≥ 3. Max +2/season.
- Key spends: 4 PC = Spy anywhere on board; 6 PC at VTM 4+ = VTM +1.

**Revelation Tokens (PP-439):**
Full reveal = Overwhelming Tribune Investigate OR 4 consecutive PC Spy successes. Token placed on target faction mat. Two tokens on two different rival mats = Path A "fully revealed" condition met.

---

## Mode A: PC Accumulation Rate

**Starting state:** Varfell Wealth 4, VTM 0. PC starts at 0.

**Season 1:** Tribune card available. Varfell plays Tribune as Investigate (uses Tribune normally — does not gain PC from this use). Wealth 4 ≥ 3 → Senate purchase pass: +1 PC (Varfell declines to buy a card at Senate Market). Total PC gain: +1 (Senate pass). **PC: 1.**

**Season 2:** Tribune available. Varfell plays Tribune differently (not Investigate — plays something else, e.g. counter-intelligence). +1 PC (Tribune played differently). Senate pass: +1 PC. **PC: 3.**

**Season 3:** Same as S2. **PC: 5.** Wait — max +2/season. At VTM 0–3, PC ceiling is 4. **PC: 4 (capped).**

**Clarification needed:** Can PC accumulate past the ceiling? The cap (0–4 at VTM 0–3) is a hard ceiling — excess is lost. At PC 3 going into S3, gaining +2 brings PC to 5, but cap is 4. **PC stays at 4.**

**Season 3 corrected:** PC 3 + 2 = 5 → capped at **PC 4.**

**Finding P1 — Patience Protocol saturation occurs at S3 (VTM 0–3, PC cap 4).** Once PC is full, every additional gain is wasted unless a spend occurs. The protocol creates pressure to spend before saturation — "patience" is not infinite.

**Optimal early spend:** At PC 4, Varfell can play a 4-PC Spy anywhere on board. This is the primary high-value spend in VTM 0–3.

---

## Mode C: Full Scenario — Varfell Intel Arc (Seasons 1–12)

**Goal:** Reveal two rival factions fully (Path A condition) using Revelation Tokens.

### Seasons 1–3: Build to PC 4

S1: PC 1. S2: PC 3. S3: PC 4 (capped). Varfell also building VTM via normal Tribune Investigate actions.

### Season 4: First 4-PC Spy (Crown target)

**4-PC Spy anywhere on board:** Varfell spends 4 PC → PC 0. Target: Crown. Crown's Royal Guard (PP-442): once per season, cancel one successful Intel action targeting Crown (Phase 4 Priority 1). Royal Guard fires before Varfell's Spy (both are Priority 1 — Intel tier). Does Royal Guard fire before or after the Spy roll?

**Ruling (PP-442):** "Cancel one successful Intel action targeting Crown per season (Phase 4 Priority 1, no card)." This cancels a SUCCESSFUL action — the Spy rolls first, then Royal Guard cancels on success. So: Varfell rolls the 4-PC Spy, Crown's Royal Guard cancels if successful.

4-PC Spy success rate: Tribune Spy (Tribune Outward) pool = Varfell Intel 4D vs Ob = target Intel ÷ 2 round up. Crown has no Intel stat (Crown's stat block: M, I, W, Mil, Sta — no Intel). [GAP: Spy against a non-Intel faction — what is the Ob?]

**Gap-fill:** Spy Ob against factions without Intel stat = Ob 2 (standard). 4D vs Ob 2: P(Success): ~85%. On Success, Royal Guard fires and cancels. **Spy result: cancelled.** 4 PC wasted.

**[EDITORIAL: ED-343 — 4-PC Spy interacts with Royal Guard (cancel on success). This makes the 4-PC spend high-value but not reliable against Crown specifically. Confirm: (a) Royal Guard can cancel a 4-PC Spy (ruling taken: yes), and (b) whether the 4 PC are refunded on cancellation (ruling taken: no — the Spy was attempted, the cost is sunk). P2.]**

PC: 0. No reveal on Crown this season.

### Seasons 5–7: Rebuild PC, target non-Royal-Guard faction

S5–S6: PC 0 → 2 → 4. S7: Spend 4-PC Spy on **Hafenmark** (no Royal Guard equivalent). Hafenmark Intel stat: not defined in params (same gap). Ob 2 (gap-fill). 4D vs Ob 2: P(Success): ~85%. **Result: Success.** This is the first of 4 consecutive Spy successes needed for full reveal.

### Seasons 8–10: Continue 4-PC Spy chain on Hafenmark

S8: PC 0 → 2. Not enough for 4-PC Spy (need PC 4). **Gap: can Varfell accumulate faster?** Max +2/season. S8: PC 2. S9: PC 4. S10: **Second 4-PC Spy on Hafenmark.** 4D vs Ob 2: Success. Count: 2 of 4.

**Finding P2 — 4-PC Spy chains require 2 seasons per attempt (build → spend).** Getting 4 consecutive successes takes minimum 8 seasons (4 attempts × 2 seasons). If any attempt fails, the chain resets. P(4 consecutive successes at 85%): 0.85^4 ≈ 52%. Roughly coin-flip odds for the full reveal chain.

**Alternative: Overwhelming Tribune Investigate.** Investigate (Ob 2, pool 4D). P(Overwhelming: net ≥ 4 AND ≥ 3 at 4D Ob 2): ~27%. One Overwhelming Investigate = instant full reveal without PC cost. Varfell should always attempt Investigate first; fall back to 4-PC Spy chain only if Investigate repeatedly fails.

**Finding P3 — Overwhelming Tribune Investigate is the superior Revelation Token path.** At ~27% per season, expected seasons to Overwhelming: ~3.7. Compare to 4-PC chain: minimum 8 seasons at 52% completion odds. Investigate is faster and free (no PC cost). The 4-PC Spy chain is a fallback, not the primary path.

### Season 11: Revelation Token on Hafenmark (assume Overwhelming Investigate)

**S10 revised:** Varfell plays Tribune Investigate against Hafenmark. Pool 4D vs Ob 2. **Result: Overwhelming** (net 5). **Revelation Token placed on Hafenmark mat.** Public and permanent.

Effects: Hafenmark knows they're revealed (marker is public). Hafenmark Procedural Objection (PP-442): on any future Varfell Investigate success, Hafenmark may spend Parliamentary Challenge use to replace revealed stat with false value. But the Revelation Token is already placed — it affects PATH A conditions, not the specific stat reveal.

**VTM status at S10:** Varfell has been running Investigate every season while building PC. At VTM 0, each Investigate costs nothing (no PC, standard Tribune action). VTM advances via... how?

**VTM advance mechanic (from params):** "6 PC at VTM 4+ = VTM +1." VTM 0 → 1 → 2 → 3 requires some mechanism. At VTM 0–3, VTM advancement is via... [GAP: VTM advance from 0–3 is not explicitly defined in params. The 6-PC spend only applies at VTM 4+. How does VTM advance in early stages?]

From context: "Vaynard TK threshold: Research acceleration." Vaynard's VTM increases through research events and Expedition successes. In BG: Varfell Path A victory requires VTM ≥ 3, so VTM must advance somehow. VTM 3 is described as public (visible to all factions), and Expedition successes advance VTM. But at BG scale: VTM likely advances via successful Thread operations (Community Weaving, Expedition outcomes) rather than PC spend.

**[EDITORIAL: ED-344 — VTM advance mechanism in BG (VTM 0→3) is not defined in params. Only the 6-PC spend at VTM 4+ is specified. How does Varfell raise VTM from 0 to 3? Likely: successful Expedition seasons (+1 VTM per Overwhelming Forgetting Check). This should be canonised. P2.]**

### Season 12: Second Revelation Token — Church

**S12:** Varfell plays Tribune Investigate against Church (T9 territory, Inquisitor present: +2 Ob). Pool 4D vs Ob 2 + 2 Inquisitor = **Ob 4.** P(Overwhelming at 4D Ob 4): ~1%. Essentially impossible.

**Varfell must eliminate the Inquisitor first** or target Church in a non-Inquisitor territory. Church-prominent territory without Inquisitor: T4 (Grauwald, Varfell-controlled, Church prominent if Church M5 > Varfell M4). Investigate in T4 (Varfell's own territory): Ob 2, no Inquisitor. 4D vs Ob 2. **Result: Overwhelming.** Revelation Token on Church mat.

**Path A condition met:** Revelation Tokens on Hafenmark AND Church. Varfell Path A win condition check: TCV ≥ 10, VTM ≥ 3, two reveals, controls ≥ 1 territory outside starting 4.

---

## Mode B: Interaction Chain — Patience Protocol → Revelation → Path A Unlock

**Chain:**
1. PP accumulation (S1–S3) → PC 4.
2. 4-PC Spy (S4): cancelled by Royal Guard. PC wasted.
3. Redirect to Investigate (S5+): Overwhelming at S10 on Hafenmark → Token 1.
4. Investigate on Church in non-Inquisitor territory (S12) → Token 2.
5. Path A conditions checked. VTM gap blocks win (VTM advance undefined).

**Critical path:** The limiting factor on Path A is VTM ≥ 3, not the Revelation Tokens. Tokens can be earned by S12. VTM 3 requires Expedition development (T15 access, TS development — Vaynard TS 30 at VTM 3). This takes parallel investment across the entire arc. Path A win is probably achievable by S14–16 if VTM and TCV tracks progress simultaneously.

---

## Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-PP-01 | P1 | PC saturation occurs at S3 (cap 4). Protocol creates spend pressure — holding PC past S3 wastes accumulation. |
| F-PP-02 | P2 | 4-PC Spy chain requires 8+ seasons for 4 consecutive reveals (52% odds). Overwhelming Investigate is the faster path (~3.7 seasons expected). |
| F-PP-03 | P2 | Royal Guard cancels 4-PC Spy on Crown on success (sunk cost — no PC refund). |
| F-PP-04 | P2 | VTM advance from 0→3 in BG is undefined. Canonisation needed before Path A win condition can be fully adjudicated. |

