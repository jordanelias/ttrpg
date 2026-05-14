# Part 9 — Character-Scale Decoupling: Almud vs Crown
## Date: 2026-05-14 · Session: bottom-up-canonical-verified · Part 9/9
## Trigger: Jordan's question — *"is it really a win for Valorsmark re Almud if he gets deposed?"*
## Companions: Parts 1–8 (4-faction balance audit, canonical sim, sensitivity)
## Authority: `peninsular_strain_v30.md` §5.3 (Dynastic Proclamation legitimacy claim),
ED-318 (Sta 0 = formal submission), `faction_actions.md` (Excommunication mechanics)

---

## §1 The Layering Question

The 8-part audit measured **faction-scale victory**: territories controlled,
Mandate accumulated, treaties bound, sovereignty achieved. But Valoria's
canonical design has at least two semantic layers:

1. **Faction-scale**: Crown (Valorsmark) holds territories with Accord ≥ 2;
   maintains Mandate; satisfies Peninsular Sovereignty (§6.1)
2. **Character-scale**: Almud personally rules. He is not Excommunicated, not
   formally Submitted (Sta 0, ED-318), not deposed by Parliamentary action or
   by Hafenmark's Dynastic Proclamation (Baralta's divine-right claim per §5.3)

These layers can **decouple**. The simulator outputs "Crown wins 30.2%" — but
how many of those wins have Almud still on the throne?

Canonical hooks that drive the decoupling:
- **§5.3 Dynastic Proclamation** (Hafenmark): *"Faith is not mediated — it is
  lived. Anyone who is truly faithful can hear Solmund. **Anyone who cannot
  should not rule.**"* — explicitly a legitimacy challenge to the named monarch
- **Excommunication** (Church, `faction_actions.md`): faction L −1, contests
  the monarch's spiritual standing
- **ED-318**: Stability 0 = formal submission (the King kneels)
- **Parliamentary action** (Hafenmark): votes against Crown can erode the
  king's personal standing distinct from the faction

---

## §2 Instrumentation

Added per-faction per-season tracking to the v5 simulator:
- **Sta**, **Mandate (L)** per season
- Excommunication landings flagged
- Territory losses specifically to Hafenmark Dynastic Proclamation flagged

Character-state classification at campaign end:
- **STRONG** — Sta ≥ 4 AND Mandate ≥ 5 currently; no recent submission/excomm
- **STABLE** — neither STRONG nor any DEPOSED criterion
- **WEAK** — Sta ≤ 2 OR Mandate ≤ 2
- **DEPOSED** (4 subtypes):
  - `deposed-submission`: Sta hit 0 anywhere in campaign (formal submission, ED-318)
  - `deposed-mandate-collapse`: Mandate ≤ 1 sustained 2+ seasons
  - `deposed-excommunicated`: Excomm landed; Mandate didn't recover to ≥ 4 within 4s
  - `deposed-proclaimed-against`: ≥ 50% of starting territories lost specifically to Hafenmark DP

500 campaigns per configuration. Source: `/home/claude/char_decoupling.py`.

---

## §3 Emergent Results

### §3.1 Canonical v5 (consent=0.5, cap=6, 36 seasons)

| Metric | Value |
|--------|-------|
| Crown faction win-share | **30.2%** |
| Almud STRONG overall | 16.2% |
| Almud DEPOSED overall | **16.0%** |
| Crown wins WITH Almud strong | 50.3% of Crown wins |
| Crown wins WITH Almud deposed | **4.6% of Crown wins** ← pyrrhic |

**Almud's deposition modes (canon, 500 campaigns):**
| Mode | Count | % campaigns |
|------|-------|-------------|
| Mandate collapse | 60 | 12.0% |
| Excommunicated | 14 | 2.8% |
| Proclaimed against (Hafenmark DP) | 6 | 1.2% |
| Submission (Sta 0) | 0 | 0.0% |

**Almud's deposition is dominated by Mandate collapse, not Hafenmark Proclamation.**
The intuitive "Hafenmark deposes Almud" narrative is rare (1.2%); the actual
deposition vector is slow Mandate erosion from sustained pressure (Excommunication,
Spy attacks, Standing loss). Hafenmark Proclamation matters at the territory
level but rarely as personal dethroning event.

### §3.2 Long campaign (60 seasons) — catastrophic for Almud

| Metric | Value |
|--------|-------|
| Crown faction win-share | 17.6% (worst) |
| Almud STRONG overall | 14.6% |
| Almud DEPOSED overall | **56.0%** |

**Modes at 60s:**
| Mode | Count | % campaigns |
|------|-------|-------------|
| Mandate collapse | 197 | 39.4% |
| Excommunicated | 72 | 14.4% |
| Proclaimed against | 11 | 2.2% |

**Time compounds against Almud catastrophically.** Excommunication rate climbs
~5× from canon (14 → 72). Mandate collapse rate climbs ~3× (60 → 197). At
60-season campaigns, Almud's personal odds of remaining king are 1-in-7. The
Crown faction may continue under regency or successor, but Almud personally
falls in 56% of these games.

### §3.3 High consent (Q-1=1.0)

| Metric | Value | Δ vs canon |
|--------|-------|------------|
| Crown faction win-share | 51.6% | +21pp |
| Almud STRONG | 32.2% | +16pp |
| Almud DEPOSED | 12.6% | −3pp |

**Resolving Q-1 favorably helps Almud personally AND Crown faction.** Q-1 is a
positive-sum editorial decision for the Crown layer (both faction and character).
This strengthens the Part 8 ranking: Q-1 is the single most important canonical
decision in the audit.

### §3.4 Short campaign (24 seasons)

| Metric | Value | Δ vs canon |
|--------|-------|------------|
| Crown faction win-share | 48.6% | +18pp |
| Almud STRONG | 18.8% | +3pp |
| Almud DEPOSED | **8.0%** | **−8pp** ← best protection |

**Short campaigns protect Almud.** Excommunication essentially never fires
within 24 seasons (only 1/500). Mandate collapse drops to 39/500 (7.8%).
The character-scale game is naturally finite; long campaigns amplify creeping
pressure into deposition.

---

## §4 Direct Answer to Jordan's Question

> *"is it really a win for Valorsmark re Almud if he gets deposed?"*

**No, it is not — and the simulator quantifies the gap precisely:**

- In canonical 36-season games, **~5% of Crown's faction-scale wins are pyrrhic
  for Almud** (he is deposed in those wins). This is small but non-zero.
- In ALL canonical 36-season games, Almud is deposed in **16%** of campaigns,
  regardless of which faction "wins" the territorial map. From Almud's
  perspective, his personal fail-rate is much higher than Crown's faction
  win-rate (30.2%) might suggest.
- At long campaigns (60 seasons), Almud is deposed in **56%** of campaigns —
  even when his faction continues holding territories.

**The faction-scale and character-scale metrics measure different things.**
Crown can "win" the territorial map while Almud has been excommunicated and
ruling under spiritual sanction; or while Mandate has collapsed and Almud
rules under regency; or while a Hafenmark Proclamation has split off enough
provinces that Almud holds only the rump kingdom. None of those are wins
for Almud personally.

**The 8-part audit's "Crown 22.8% / 30.2% / 49% / 51%" framings collapse
this distinction.** A complete balance analysis must track both axes.

---

## §5 Implications for Balance Work

### §5.1 Balance is now multi-axis

The earlier audit framed the question as "what makes 4 factions ~25% each?"
The character-scale layer adds:
- "What % of campaigns does each LEADER survive?"
- "When their faction wins, are they personally on the throne?"

For each faction, there are two separate metrics:
- Faction-victory rate (current sim output)
- Leader-survival rate (new sim output)

The 4-faction × 2-metric matrix is the proper balance frame.

### §5.2 Almud-specific design observations

1. **Mandate floor as character-protection mechanic.** In 60s campaigns,
   12% of Almud-deposition is Mandate collapse below 2. Canonical Royal Decree
   gives Sta +1 but not L recovery. Crown lacks a personal L-recovery action
   beyond Royal Charter (which is territorial). Investigate adding a
   character-scale Mandate restoration mechanic.

2. **Excommunication consequence ambiguity.** Canon says "Mandate −1" on
   successful Excomm, but doesn't specify *recovery path*. Without recovery,
   Excommunication is a permanent character-scale debuff that compounds with
   subsequent Excommunications. Editorial question: can Excommunication be
   lifted? By what mechanism? At what cost?

3. **Proclamation rarely deposes despite design intent.** Only 6/500 (1.2%)
   campaigns end with Almud "proclaimed against" at the threshold tested.
   Hafenmark DP success rate (~28% per attempt × 1/season × 36s = ~10 attempts
   × 28% = 2.8 successful proclamations average) hits Crown territories but
   rarely concentrates enough to threaten Almud's seat directly. **Design
   intent: Hafenmark deposes Almud. Emergent: Hafenmark nibbles at Crown's
   territorial edges.** Editorial gap.

### §5.3 Other faction-leader analogs (briefer treatment)

The decoupling applies to all four factions:

- **Church / "Cardinal"**: Inverse pattern — Church wins faction-scale often;
  the Cardinal figure rarely "falls" mechanically (no equivalent of mandate
  collapse). Church's character-scale layer is most stable.
- **Hafenmark / "Baralta"**: Faction is overscaled at long campaigns (per Part
  8), but Baralta's personal-scale outcomes weren't instrumented here. If
  Baralta is the player avatar, character-scale survival likely tracks
  Hafenmark Mandate (which is generally rising via Proclamation success).
- **Varfell / "Vaynard"**: Faction is structurally underscaled (Part 8 EM-Structural-2);
  Vaynard's character-scale likely also weak (low L, low Sta, no canonical
  recovery mechanic). Estimated worst character-scale faction by structure.

---

## §6 Open Questions Surfaced by Character-Scale Layer

| # | Question | Source |
|---|----------|--------|
| Q-11 | Can Excommunication be lifted? By what mechanism? | `faction_actions.md` |
| Q-12 | Does Mandate L ≤ 1 trigger regency, succession, or character-scale event? | not in v30 sources fetched |
| Q-13 | When Hafenmark Proclamation succeeds against ≥3 Crown territories, what happens to Almud? | §5.3 implies legitimacy challenge but no mechanical consequence |
| Q-14 | Is Almud's personal-scale survival a separate canonical win condition for a Crown player? | hybrid/TTRPG mode question |
| Q-15 | Are there canonical mechanics for "regency" or "successor" when Almud falls but Crown faction continues? | not modeled |

These are new questions surfaced by Jordan's framing. They join Q-1 through Q-10
on the editorial decision list.

---

## §7 Revised Editorial Priority List (Updated for Character Layer)

Most-leverage-first, integrating Parts 1–9:

1. **Q-1 (Treaty consent)** — single highest faction-scale leverage; positive-sum
   for Almud too
2. **Territorial completeness threshold / Co-Victory framing** — 15/15 vs lower
3. **Q-11 + Q-12 (character-recovery mechanics)** — affects Almud-survival rate
   independent of faction win-rate
4. **Q-4 (campaign length)** — strongly affects both faction balance AND Almud
   survival
5. **Varfell post-CR-STRIKE acquisition** — structural redesign (faction +
   character)
6. **Hafenmark scaling** — structural (faction)
7. Q-14, Q-15 — formalize character-scale win conditions for hybrid mode

---

## §8 Cross-Part Synthesis (Final)

| Part | Status |
|------|--------|
| 1 — Errata | Preserved |
| 2 — Log Schema | Preserved |
| 3 — Top-Down Re-Sim | Directionally correct |
| 4 — NERS Audit | Methodologically valid |
| 5 — Throughline Audit | Methodologically valid |
| 6 — Bottom-Up MC v3 | Methodology valid; rule encoding had 10 violations |
| 7 — Canonical Bottom-Up v5 | Canonical rules verified; EM-12 refuted by Part 8 |
| 8 — Sensitivity Analysis | Identifies editorial leverage ranking |
| **9 — Character Decoupling** | **NEW** — faction-scale ≠ character-scale; Almud's personal fate quantified |

**Bottom-up granular emergent methodology delivered three layers:**

1. **Faction-scale balance** (Parts 6–7): which faction wins the territorial map
2. **Editorial leverage** (Part 8): which open canonical questions matter most for faction balance
3. **Character-scale decoupling** (Part 9): which faction wins ≠ which leader survives

The audit is now complete. Outstanding work is editorial (resolve Q-1 through
Q-15) and structural (Varfell + Hafenmark + Almud personal recovery mechanics).

---

## §9 Files Produced This Session (Post-Compaction)

| File | Status |
|------|--------|
| `part7_canonical_v5sim_2026-05-14.md` | canonical v5 sim findings |
| `part8_sensitivity_synthesis_2026-05-14.md` | Q-1/Q-3/Q-4 sensitivity sweeps |
| **`part9_character_decoupling_2026-05-14.md`** | **this doc** — Almud vs Crown |
| `mc_v6_simulator_source.py` | v6 simulator with parameterized rules |
| `mc_v6_sensitivity_results.json` | sensitivity sweep raw data |
| `char_decoupling.py` (in `/home/claude/`) | character-scale instrumentation |
| `char_decoupling.json` (in `/home/claude/`) | character-scale results |

---

*Session: bottom-up-canonical-verified · 2026-05-14 · Part 9/9*
*Surfaced by Jordan's character-layer question. The 8-part audit collapsed
character and faction; this part separates them and quantifies the decoupling.*
