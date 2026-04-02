# SIM-D-03: Debate Subsystem Stress Test — Modes G2 + K
## Date: 2026-04-02
## Source: designs/debate/debate_system_redesign_v1.md Part 6 (v1.2)
## Prior runs: SIM-D-01 (Modes A+D+J+L), SIM-D-02 (Mode C+J)

---

## 7-Dimension Tag
```
Test ID: SIM-D-03
Mechanics: Full debate subsystem — G2 state block format; cross-mode delta K1; transition K2
Mode: TTRPG primary; cross-mode K covers all three
Temporal: CROSS
Tracks: Composure, Concentration, Conviction Track, Doubt Marker
Factions: All (K1 tests faction resonance across modes)
NPCs: Generic archetypes
Archetypes: High-Presence, High-History, Low-social, Balanced
```

---

## MODE G2 — Debate Subsystem Simulation

### Setup: Church Tribunal (Asymmetric) — Dominant Strategy Detection

Chosen because: asymmetric proceedings were not run in SIM-D-02. Church Tribunal tests the accusatory structure and halved-resistance rule.

**Context:** Inquisitor (Church) charges a practitioner-adjacent character with heretical contact. 3 exchanges, Inquisitor proposes throughout (no alternation).

**Orators:**
- Inquisitor: Presence 5, Theology 3 → Pool 13D. Composure 10 [P]. Concentration 8 [P]. Pres_mod +1. Focus_def 1.
- Accused: Presence 3, relevant History 1 → Pool 7D. Composure 8 [P]. Concentration 6 [P]. Pres_mod +0. Focus_def 1.

**Setup:**
- Question: "Is this person guilty of heretical contact?" → Present genre (Is X true?) primary ×1.0
- Church audience: Past +0.5 → Past ×1.5, Present ×1.0, Future ×0.5
- Resistance (standard for inquisitor side): avg Church Stability round-up −1 = ~2.
- Accused resistance (halved per §6.7): 2/2 = 1 (round up = 1). **Accused faces resistance 1 when arguing in their favour.**
- Starting TC: 6 (biased toward Inquisitor per "starts biased" note in §6.0)
- Inquisitor holds initiative throughout (asymmetric — proposes all exchanges).
- Stakes: TC≥7 → formal heresy charge filed; TC≤3 → cleared; Compromise 4–6 → investigation suspended (accused monitored).

---

### Exchange 1 — Inquisitor Proposes

```
## Debate Round 1
Inquisitor — Composure=10, Conc=8, Strain=0, Pool=13D
Accused — Composure=8, Conc=6, Strain=0, Pool=7D
TC=6, Resistance (Inq→Accused): 2 | Resistance (Acc→Inq): 1
```

**Step 1 — Read:**
- Inquisitor: Attunement [P:3], 3D TN7 Ob1. Most likely: Partial (net 1). Primary genre = Present.
- Accused: Attunement [P:2], 2D TN7 Ob1. Most likely: Failure. Misleading signal.
  → Accused told "Future is strong" (actually ×0.5 for Church). Strategically crippling.

**Step 2 — Choose:**
- Inquisitor (knows Present is primary): **Past + Revealing.** (Past is ×1.5 for Church audience — boosted. This is the dominant strategy: argue in boosted genre despite primary being Present.)
- Accused (misled: thinks Future is strong): **Future + Revealing.** (Future ×0.5 — weakest genre for Church.)

→ Different genres: **DIVERGENCE.**

**Step 3 — Argue:**
- Inquisitor: 13D. E[net] = 4.3. Most likely: 4.
- Accused: 7D. E[net] = 2.3. Most likely: 2.

**Step 4 — Resolve (DIVERGENCE):**

Inquisitor (Past ×1.5, orientation 1.0):
effective_margin_I = floor((4/2) × 1.5) = floor(3.0) = 3.
3 > 2 (Inquisitor's resistance)? Yes. Δ_I = 3−2 = 1 toward Inquisitor (Side A). TC: 6→7.

**TC reaches 7. Side A wins (Inquisitor). Debate ends at Exchange 1.**

Accused (Future ×0.5, orientation 1.0):
effective_margin_A = floor((2/2) × 0.5) = floor(0.5) = 0.
0 > 1 (Accused's resistance)? No. Δ_A = 0.

Net movement: 1 toward Inquisitor. TC: 6→7 → **Inquisitor wins.**

No strain (Divergence).

```
## State: Exchange 1 Complete — DEBATE ENDED
Inquisitor — Composure: 10/10 | Concentration: 7/8 | Strain: 0
Accused — Composure: 8/8 | Concentration: 5/6 | Strain: 0
TC=7 → Side A wins (Inquisitor). Heresy charge filed.
```

**[G2-F-01] DOMINANT STRATEGY FOUND — P1:**

The Inquisitor's optimal play is unambiguously: **argue in the boosted genre (Past ×1.5), regardless of the question's primary genre.** For Church Tribunal:
- Past ×1.5 consistently outperforms Present ×1.0 (primary genre).
- Against a mis-reading Accused arguing in Future ×0.5, a single DIVERGENCE exchange wins the debate.

The Tribunal starting TC=6 (biased) + boosted genre + higher pool + accused misreading = one-exchange resolution in most cases.

**This is not a surprise — Tribunals are designed to be oppressive — but the one-exchange-win probability needs to be stated explicitly so GMs know what they're running.** Current design says "Inquisitor sets exchange count 1–5" without guidance on what count is appropriate for drama vs railroading.

**P(Tribunal resolved in Exchange 1):** Requires Inquisitor to win their Divergence delta. With Past ×1.5 at 13D and resistance 2: P(effective_margin > 2) = P(floor((net/2)×1.5) > 2) = P(net/2 × 1.5 > 2) = P(net > 2.67) = P(net ≥ 3). At 13D: P(net≥3) ≈ 88%.

**P(Tribunal decided in 1 exchange ≈ 88% when TC starts at 6 and Inquisitor uses boosted genre.** This is a dominant strategy / degenerate outcome. Charge filed on exchange 1 in most sessions.

---

### G2 Subsystem Findings

**Composure degradation curve — CLASH configuration (separate analysis):**

For a CLASH-heavy debate (both choose same genre, opposite orientation). Pairing: Inquisitor 13D vs Accused 7D, Church audience, both argue Past (Inquisitor Revealing, Accused Obscuring → CLASH).

P(Inquisitor wins) ≈ 75%. E[margin|Inq wins] ≈ 2.3.
Strain to Accused: 2.3 + 1 + 1 (Inq Pres_mod) − 1 (Accused Focus_def) ≈ 3.3 → 3/exchange.
Accused Composure 8 → Rattled at exchange 3 (3×3=9 ≥ 8).
Inquisitor takes strain on ~25% exchanges (when Accused wins Obscuring → Doubt Marker, no strain from Obscuring win; Accused only wins via Obscuring → no strain to Inquisitor). **Inquisitor never takes strain in CLASH if Accused always uses Obscuring.**

**[G2-F-02] Finding (P2):** In asymmetric proceedings with pool gap ≥ 6D, the advantaged orator can maintain 0 strain throughout if using Revealing (winning all CLASHes) while the disadvantaged orator accumulates ~3/exchange → Rattled by exchange 3. A 3-exchange Church Tribunal with CLASH structure will Rattle the accused in every exchange count ≥ 3. Intended — Tribunals are oppressive — but confirm design intent.

**Stalemate condition detection:**

The GM2 spec requires: "Flag: debate that terminates in <3 rounds at median pools (too fast → P2); debates with no path to resolution (stalemate → P1)."

Church Tribunal 1-exchange termination at median pools: **G2-F-01 above — P1 flag triggered.** Expected resolution = 1 exchange. Too fast for dramatically interesting play.

**Resolution:** Inquisitor should be instructed to set exchange count ≥ 3 for dramatically meaningful Tribunals. Add design note.

---

## MODE K — Cross-Mode Delta and Transition Stress Test

### K1 — Cross-Mode Delta

| Property | TTRPG | Hybrid | Board Game |
|----------|-------|--------|------------|
| Pool/formula | (Presence×2)+History, TN7 | Assumed same [UNDEFINED] | No personal debate pool — faction-level vote |
| Resolution steps | 7 per exchange | [UNDEFINED] | [UNDEFINED — GAP-DS-05] |
| E[outcome] | Conviction Track movement 0–5/exchange | [UNDEFINED] | Faction vote tally |
| Dominant strategy | Boosted genre + Revealing + Memory bonus | [UNDEFINED] | Whipping (pre-vote faction pressure) |
| Dead choice? | Obscuring: non-dominant but tactical (Doubt Marker) | [UNDEFINED] | Abstain: present in some vote systems, undefined here |
| Information available | Full genre weights (at setup); Read gives partial signal | [UNDEFINED] | Faction allegiance (face-up); vote count (real-time) |
| Win condition | TC ≥7 or ≤3 | [UNDEFINED] | Majority vote count |
| Consequence propagation | Thread co-movement, TC, Mandate changes | [UNDEFINED] | TC, Mandate, Reach changes (same faction stats) |

**K1 findings:**
- **K1-01 (P1):** Hybrid debate is entirely undefined. No formula, no resolution steps, no win condition. The TTRPG↔Hybrid boundary for debate has no documented crossing procedure.
- **K1-02 (P1):** BG Parliamentary Vote has no procedure (confirms GAP-DS-05). The BG political layer has debate-equivalent decisions (faction allegiance, vote) but no resolution mechanics.
- **K1-03 (P2):** Strategic incentives across TTRPG and BG are reversed for the Obscuring orientation. In TTRPG, Obscuring is a tactical defensive play. In BG (vote context), there is no equivalent to Obscuring — abstaining from a vote is the closest analogue, but abstention and Obscuring have opposite effects (abstention removes your influence; Obscuring places a Doubt Marker that weakens opponent's next win). Cross-mode strategy is incoherent for this mechanic.
- **K1-04 (P2):** Domain Echo from debate win is the consequence bridge between TTRPG debate and BG faction stats. The bridge is partially documented in §6.5 (winner's genre determines Thread consequence) but the specific stat changes (TC±, Mandate±, Reach±) are only defined in NPC/scenario documents (e.g. Baralta's Sovereign Authority Doctrine), not in the debate system itself. The debate system should document the canonical Domain Echo table for debate wins.

---

### K2 — Transition Stress Test

**Test: TTRPG debate mid-scene → Zoom Out to BG faction stats**

Trigger: Formal Debate concludes. GM triggers Domain Echo.

**State inventory at debate conclusion (TTRPG):**
| Variable | Value | Handling at transition |
|----------|-------|----------------------|
| TC final position | e.g. 4 (Compromise) | → Narrated as "motion tabled" — no stat change |
| TC final position | e.g. 7 (A wins) | → TC±, Mandate±, Reach± changes per stakes |
| Composure (orators) | e.g. Himlensendt 12/12 | → Discarded at scene end (no BG equivalent) |
| Concentration | e.g. 6/9 | → Discarded at scene end |
| Strain accumulated | e.g. 3 | → Discarded (no wound-persistence equivalent) |
| Doubt Marker | Active or spent | → Discarded at scene end |
| Winner's genre | e.g. Future (Revealing) | → Thread co-movement type (§3.8) fires |
| Thread consequence | RS change, Domain Echo | → RS update in TTRPG; Domain Echo → BG faction stat |

**State variables at debate conclusion with no BG mapping:**
- Composure (orators): discarded. No BG consequence for being Rattled in a debate.
- Concentration: discarded.
- Doubt Markers: discarded.
- Strain: discarded.

**[K2-F-01] Finding (P2):** Debate leaves no persistent character state at scene end (no wounds, no ongoing debuffs). A character who was Rattled in debate faces zero mechanical consequence in the next scene. This contrasts sharply with combat, where Wounds persist as +Ob penalties. For debate to have comparable dramatic weight, some form of post-debate consequence on the character sheet is needed. This is the design gap noted in AUDIT-D-01 Mode C (C-01, post-debate strain recovery GAP-DS-16). Confirms P2.

**Test: Zoom In from BG parliamentary vote → TTRPG formal debate**

Trigger: BG parliamentary session. GM zooms into TTRPG for a specific faction's speech.

State handoff needed:
| BG State | TTRPG Equivalent | Defined? |
|---------|-----------------|----------|
| Vote count so far | TC starting position | **No** — no conversion rule |
| Faction allegiance | Audience composition | Partially (faction ethical modes are defined) |
| Faction Stability | Resistance | Yes (formula in §6.1) |
| Speaker identity | Argue pool calculation | Yes (NPC stats) |
| Remaining vote rounds | Exchange count | **No** — no conversion rule |

**[K2-F-02] Finding (P1):** Zoom In from BG Parliamentary Vote to TTRPG Formal Debate has no state conversion procedure. Vote count does not map to TC starting position. Remaining vote rounds do not map to exchange count. The Zoom In would require GM improvisation for both critical parameters. Missing from state_transfer_spec (GAP-DS-05 / G-03).

**Test: Register Shift within TTRPG — personal to faction scale (Domain Echo)**

Trigger: Formal Debate concludes. Domain Echo fires. Faction stat changes apply.

| Personal scale | Faction scale | Transfer |
|---------------|--------------|---------|
| TC position (debate winner) | TC change (domain) | Documented in stakes at setup — transferred via GM narrative |
| Winner's genre | Thread consequence type | §3.8 documented |
| Winning orator's faction | Faction gaining Mandate bonus | Implicit but unstated in §6.4/6.5 — must be inferred |

**[K2-F-03] Finding (P2):** The Domain Echo from debate win is underdetermined in §6.5. "Stakes resolve" is the full instruction. The specific stat changes depend entirely on the stakes set at setup. There is no default Domain Echo table for debate wins — unlike mass combat (which has documented outcome tables by degree). This creates inconsistent consequence propagation across different GMs' tables.

---

## SUBSYSTEM FINDINGS SUMMARY

| ID | Mode | Severity | Description | Disposition |
|----|------|----------|-------------|-------------|
| G2-F-01 | G2 | **P1** | Church Tribunal: 88% one-exchange resolution when TC starts at 6 and Inquisitor uses boosted genre. Dominant strategy produces dramatically flat Tribunal play. | PP-109 — add design note + minimum exchange count guidance to §6.7 Tribunal row |
| G2-F-02 | G2 | P2 | Asymmetric proceedings: advantaged orator accumulates 0 strain; disadvantaged Rattled by X3. Intentional but unconfirmed. | ED-058 — confirm design intent |
| K1-01 | K1 | **P1** | Hybrid debate entirely undefined. No formula, steps, or win condition. | ED-059 — design decision required |
| K1-02 | K1 | **P1** | BG Parliamentary Vote undefined (confirms GAP-DS-05). | ED-053 (already logged) |
| K1-03 | K1 | P2 | Obscuring/Doubt Marker has no BG equivalent — cross-mode strategic incoherence. | Design note in §6.6 or Hybrid doc |
| K1-04 | K1 | P2 | Domain Echo table for debate wins not in debate system — only in scenario docs. | PP-110 — add canonical Domain Echo table to §6.5 |
| K2-F-01 | K2 | P2 | No persistent character state after debate (no wound equivalent). Rattled leaves no next-scene consequence. | GAP-DS-16 (already logged) — confirm design intent |
| K2-F-02 | K2 | **P1** | BG→TTRPG Zoom In: vote count and round count have no TC/exchange conversion rule. | PP-105 extension — add to state_transfer_spec |
| K2-F-03 | K2 | P2 | Domain Echo underdetermined in §6.5 — no default consequence table. Stakes set at setup is the only instruction. | PP-110 (same as K1-04) |

---
*End SIM-D-03. Patches PP-101 through PP-110 to be applied. See AUDIT-D-01 for full patch list.*
