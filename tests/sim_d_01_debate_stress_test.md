# SIM-D-01: Debate System Stress Test
## Modes: A (Isolation) + D (Edge Cases) + J (Cognitive Load) + L (Precedent)
## Date: 2026-04-02
## Source doc: designs/debate/debate_system_redesign_v1.md Part 6
## Pool formula tested: (Presence × 2) + History bonus, TN 7
## Primary purpose: SIM-DEBT-01 re-calibration

---

## 7-Dimension Tag

```
Test ID: SIM-D-01
Mechanics: Argue roll, Read roll, CLASH, COMPETITION, DIVERGE, TIE, Conviction Track,
           Composure/Rattled, Concentration/Spent, Doubt Marker, Regroup, Concede
Mode: TTRPG | Temporal: CROSS (applies across scenes)
Tracks: Composure, Concentration, Conviction Track
Factions: Generic (all faction resonance variants modelled)
NPCs: Generic archetypes (Diplomat, Scholar, Warrior-type, Orator)
Archetypes: High-Presence orator, History-specialist, Low-social combatant, Balanced social
```

---

## MODE A — ISOLATION

### A.1 Argue Roll: Pool Distribution

Pool = (Presence × 2) + History bonus, TN 7, E[net per die] ≈ 0.33

| Presence | History | Pool | E[net] | P(≥1) | P(≥2) | P(≥3) |
|---------|---------|------|--------|--------|--------|--------|
| 1 | 0 | 2D | 0.7 | ~45% | ~15% | ~4% |
| 2 | 0 | 4D | 1.3 | ~80% | ~50% | ~25% |
| 3 | 0 | 6D | 2.0 | ~92% | ~70% | ~45% |
| 3 | 2 | 8D | 2.6 | ~97% | ~82% | ~60% |
| 3 | 3 | 9D | 3.0 | ~97% | ~88% | ~73% |
| 4 | 3 | 11D | 3.6 | ~99% | ~93% | ~80% |
| 5 | 3 | 13D | 4.3 | ~99% | ~97% | ~88% |
| 5 | 6 | 16D | 5.3 | ~99% | ~99% | ~96% |
| 7 | 6 | 20D | 6.6 | ~99%+ | ~99%+ | ~99%+ |
| 7 | 6 + Memory | 22D | 7.3 | ~99%+ | ~99%+ | ~99%+ |

Attribute reference: Presence 1–3 → modifier +0. Presence 4–5 → modifier +1. Presence 6–7 → modifier +2.

### A.2 Old vs New Pool Comparison (SIM-DEBT-01 Core)

Representative matchup: Presence 3, History 2 (baseline character)

| Metric | Old (Cog 3 + Hist 2 = 5D) | New (Pres 3 ×2 + Hist 2 = 8D) | Δ |
|--------|--------------------------|-------------------------------|---|
| Pool size | 5D | 8D | +60% |
| E[net] | 1.65 | 2.64 | +60% |
| E[margin, symmetric win] | ~1.6 | ~2.0 | +25% |
| P(Overwhelming, i.e. net ≥ 3) | ~25% | ~60% | +140% |

Symmetric expected winning margin estimated as E[|A−B|] ≈ 0.72√P (derived from normal approximation).
- Old (5D): 0.72 × 2.24 ≈ 1.61
- New (8D): 0.72 × 2.83 ≈ 2.04

**Key calibration shift:** Under new pool, P(Overwhelming) doubles. Overwhelming (margin ≥ 3) triggers escalated consequences. This is the core SIM-DEBT-01 correction.

### A.3 Conviction Track Movement (CLASH, Revealing)

Formula: effective_margin = floor(margin × genre_weight), movement = effective_margin − resistance (min 0)

| Margin | Primary (×1.0), res=1 | Secondary (×0.5), res=1 | Boosted (×1.5), res=1 |
|--------|----------------------|------------------------|----------------------|
| 1 | 0 | 0 | 0 |
| 2 | 1 | 0 | 2 |
| 3 | 2 | 0 | 3 |
| 4 | 3 | 1 | 5 |

Dead zone: margin 1 with any genre against resistance ≥ 1 = 0 movement. Secondary genre requires margin ≥ 4 for 1 step movement at resistance 1.

With new pool (8D symmetric), E[margin|win] ≈ 2.04. Expected movement per CLASH win with primary genre, res=1:
- floor(2.04) − 1 = 1 step. Consistent movement now expected.

With old pool (5D symmetric), E[margin|win] ≈ 1.61:
- floor(1.61) − 1 = 0 steps. Many exchanges produced 0 track movement.

**New system is more decisive per exchange.**

### A.4 Strain Distribution (CLASH)

Formula: Strain_to_loser = margin + 1 + winner_Presence_mod − floor(loser_Focus/2)

Winner Presence modifier: +0 (Pres 1–3), +1 (Pres 4–5), +2 (Pres 6–7)
Focus defence (loser): floor(Focus/2). Typical: Focus 2 → 1, Focus 3 → 1, Focus 4 → 2.

| Margin | Winner Pres mod | Loser Focus def | Strain |
|--------|-----------------|-----------------|--------|
| 1 | +0 | 1 | 1 |
| 2 | +0 | 1 | 2 |
| 2 | +1 | 1 | 3 |
| 3 (OVW) | +0 | 1 | 3 |
| 3 (OVW) | +1 | 1 | 4 |
| 3 (OVW) | +2 | 1 | 5 |
| 3 (OVW) | +2 | 2 | 4 |

**Typical strain per CLASH exchange (E[margin] ≈ 2, Pres 3 winner, Focus 2 loser): 2+1+0−1 = 2 strain.**

Old system baseline: 1-2 strain typical. New system: 2-3 strain typical. The ×2 Presence pool amplifies margin variance, pushing strain higher.

### A.5 Composure Burn Rate (Exchanges to Rattled)

Composure = Poise + Bonds + 3. Range 5–17.

Strain source: CLASH losses + TIE (+1 each)

| Archetype | Composure | Strain/exchange | Exchanges to Rattled |
|-----------|-----------|-----------------|---------------------|
| Warrior-type (low social) | 2+2+3=7 | 3 avg | 2.3 → exchange 3 |
| Generic citizen | 2+3+3=8 | 2-3 avg | 2.7–4 → exchange 3–4 |
| Typical diplomat | 3+3+3=9 | 2-3 avg | 3–4.5 → exchange 4 |
| High-social | 4+4+3=11 | 2-3 avg | 3.7–5.5 → exchange 5-6 |
| Maximum | 7+7+3=17 | 3 avg | 5.7 → exchange 6 |

**3-exchange Formal Debate:** Rattled near-guaranteed for Composure ≤ 7. Possible for Composure 9 if losing all exchanges.
**5-exchange Grand Debate:** Rattled near-certain for Composure ≤ 9. Composure 11+ may escape.

Old calibration (v1+v2): strain ~1/exchange → Rattled in exchange 7-9. That baseline is WRONG under new pool. Composure thresholds were calibrated assuming ~3× the exchange durability actually present.

### A.6 Concentration Burn Rate (Exchanges to Spent)

Concentration = Focus + Presence. Depletes: −1/exchange, −1 additional on exchange loss.

| Build | Concentration | Best case (win all) | Worst case (lose all) | Typical (50/50) |
|-------|--------------|--------------------|-----------------------|-----------------|
| Low (F2, P2) | 4 | 4 exchanges | 2 exchanges | ~3 |
| Mid (F3, P3) | 6 | 6 exchanges | 3 exchanges | ~4 |
| High (F4, P4) | 8 | 8 exchanges | 4 exchanges | ~5–6 |
| Max (F5, P5) | 10 | 10 exchanges | 5 exchanges | ~6–7 |

**Grand Debate (5 exchanges):** Mid-Concentration characters (6) hit Spent by exchange 3 if losing majority. High-Concentration (8) survive without Spent if winning majority.

**Composure vs Concentration race:** For most characters, Composure fires first. Concentration becomes the binding constraint only for characters with Composure > Concentration × (typical_strain), i.e., when Poise+Bonds are very high relative to Focus+Presence.

---

## MODE D — EDGE CASES

### D.1 Boundary Cases

**Presence 1, History 0 (2D pool):**
- E[net] ≈ 0.7. Loses to any opponent with Presence ≥ 2 reliably.
- Conviction Track movement against typical resistance: near zero (margin too low).
- Composure 5 (minimum: Poise 1, Bonds 1): Rattled by exchange 1-2 when losing to Presence 4+ opponent (strain 4-5 from single exchange).
- **Finding [F-D-04]:** Presence 1 characters cannot meaningfully participate in formal debate. No floor mechanic exists. A Presence 1 character debating a Presence 4 orator faces ~4-5 strain per exchange, Rattled before exchange 2, then −2D compounds to full incapacitation. Severity: P2. Design note: institutional screening (no Presence 1 character would be sent to a Formal Debate) is the implied solution, but no rule enforces this.

**Conviction Track at 3 or 7 (win-threshold):**
- Side B at TC=3. Next CLASH with primary genre, res=1, margin=2: movement = floor(2×1.0)−1 = 1 toward Side A. TC→4. No win fires yet. Clean.
- Resistance=0 scenario (bystander audience, Stability avg 1, −1 = 0): margin=1, primary → floor(1)−0 = 1 movement. Every exchange with margin ≥ 1 moves the track. Grand Debate resolves in 2-3 exchanges. Correct for low-institution contexts.

### D.2 Cascade Cases

**Overwhelming + High Presence cascade:**
Margin=3, winner Pres 6 (mod +2), loser Composure 7, Focus 2 (def 1):
- Strain = 3+1+2−1 = 5. Composure 7 → 2. One step from Rattled after exchange 1.
- Exchange 2: loser now at −2D if Rattled (which requires 2 more strain). If exchange 2 produces margin 1 (diminished by −2D penalty): strain = 1+1+2−1 = 3. Total = 8 ≥ 7. Rattled fires exchange 2.
- **[F-D-07] P3:** A Presence 6-7 orator landing an Overwhelming win against Composure ≤ 7 opponent can force Rattled within 2 exchanges. Grand Debate effectively decided in 2 of 5 exchanges. Accepted — this is intended as a breakthrough mechanic. Noted for GM awareness.

### D.3 Regression

**DIVERGE + TIE (both score 0 successes, different genres):**
- Divergence resolution: effective_margin for each = floor(0/2 × genre_weight × orientation_weight) = 0. Net movement = 0.
- Tie rule (§6.4): "Both orators take 1 strain. Conviction Track moves +1 toward initiative holder." Rule specifies "any interaction type."
- Conflict: Divergence resolution concludes with 0 movement. Tie rule then also fires (equal successes = 0 and 0). Two contradictory outcomes.
- **[F-D-01] P1 FINDING:** DIVERGE + TIE ambiguity. Both scoring 0 on a Divergence triggers both the Divergence evaluation (0 movement) and the Tie rule (1 strain each, +1 toward initiative holder). The "any interaction type" language means Tie overrides. Provisional patch PP-097 applied.

**Self-reference (Regroup → Spent → Regroup):**
- Character hits Concentration 0 (Spent). Next action: Regroup. Concentration restores by Focus score. Does this consume the Spent state?
- **[F-D-02] P2:** Regroup at Concentration=0 ambiguity. Spent says "next exchange: −2D, opponent +1D." Regroup has no argue roll — penalty has no target. Provisional patch PP-098 applied.

### D.4 Deadlock

**Symmetric pools, resistance = 2, Track at 5:**
- Each exchange (primary genre, res=2): effective_margin = floor(margin×1.0)−2. Margin must be ≥3 for 1 step. With 8D symmetric pools, P(margin≥3) ≈ 35%.
- Expected exchanges per track movement: ~3. For 3-exchange Formal Debate: ~1 step of total movement. Compromise result nearly guaranteed.
- Deadlock broken by: Concentration depletion (Regroup forces +1 to opponent), Rattled (−2D shifts balance), Concede (+1D recovery next exchange).
- **No infinite deadlock exists.** Concentration and Composure drain force resolution. Design is clean.

### D.5 Crunch Cascade (see also Mode J)

Per-exchange calculations:
1. Read roll (both): 2 rolls, 2 results lookups
2. Choose: 0 rolls, 2 decisions
3. Argue: 2 rolls, 1 comparison
4. Resolve interaction type: 1 formula (effective_margin), 1 resistance comparison
5. Strain: 1 formula
6. Concentration: 1 update
7. Ledger: 1 record

Base: ~7 calculations per exchange.
With Corroboration: +2 rolls per exchange (corroborator + effect). Total: ~9.

**3-exchange Formal Debate: 21 base, 27 with Corroboration.**
**5-exchange Grand Debate: 35 base, 45 with Corroboration.**
See Mode J for full cognitive load analysis.

### D.6 Ambiguity

**Obscuring orientation in a Divergence:**
- Divergence evaluates each side independently. OBSCURING WIN rule: "winning exchange with Obscuring → Doubt Marker, no track movement."
- Does Obscuring apply in Divergence? The Divergence formula uses orientation_weight — but Obscuring has no defined orientation_weight (Revealing = ×1.0; Obscuring replaces track movement with Doubt Marker, no numerical weight given).
- **[F-D-03] P2:** Obscuring in Divergence — unclear whether orientation_weight=1.0 applies (treating Obscuring as equal to Revealing in effective_margin calc) or Doubt Marker rule supersedes. Provisional patch PP-099 applied: Obscuring in Divergence → Doubt Marker if that side's effective_margin (calculated at ×1.0) > resistance; no track movement.

**Doubt Marker refresh (same orator wins Obscuring twice):**
- Second Obscuring win replaces existing Doubt Marker. If same orator wins Obscuring on exchange 2 and exchange 4 while the marker is still unconsumed: marker refreshes. Mechanical effect: the −2 reduction carries forward to next opponent win regardless of which Obscuring exchange placed it. Behaviour is consistent. No action needed.

### D.7 Incoherence

**Tie rule + interaction type priority:**
- Tie rule says "any interaction type." This creates potential conflicts with Divergence and Competition resolution paths. PP-097 addresses the highest-priority case (Diverge + Tie). Recommend: clarify in design doc that Tie rule fires AFTER interaction-type resolution fails to produce a winner, not in parallel.

**Effective_margin negative (impossible):**
- Formula: movement = effective_margin − resistance, min 0. effective_margin = floor(margin × weight). Can effective_margin be negative? Only if margin is negative — impossible, since margin = |A − B| ≥ 0. Clean.

### D.8 Optimal Play

**Memory bonus (+2D) analysis:**
- Pool: (Presence×2) + History + 2D when citing specific named claim.
- At Presence 3, History 2: base 8D → 10D with Memory. P(≥3) rises from ~60% to ~73%.
- No downside stated. No cost, no check — binary rule.
- **[F-D-05] P3:** Memory bonus is always-optimal when any specific claim exists. Creates strong incentive to pre-prep named citations. Minor strategic homogenization — all prepared orators will cite specific claims every exchange. Accepted unless player prep becomes mandatory for competitive play; flag for editorial consideration if playtesting reveals issue.

**Genre/orientation matrix dominant strategies:**
- Primary genre (×1.0) + Revealing (×1.0) is the standard-optimal choice.
- Secondary genre (×0.5) only makes sense if opponent's Read was Overwhelming and you need to misdirect.
- Obscuring is tactically optimal when: (a) holding initiative and opponent's expected win would move track 2+, OR (b) you expect to lose the exchange — a Doubt Marker on your opponent is better than 0 track movement from your loss.
- **No single dominant strategy.** Genre/orientation creates genuine situational decision-making. Design intent fulfilled.

### D.9 Degenerate

**Maximum pool matchup (Presence 7, History 6 = 20D each):**
- E[net] = 6.6. E[margin|win] ≈ 0.72×√20 ≈ 3.22. Primary genre, res=1: movement = floor(3.22)−1 = 2 per exchange.
- Track covers 4 points from neutral (5 to 9 or 5 to 1) in 2 exchanges. 5-exchange Grand Debate is decided in 2 exchanges on average.
- Strain: margin≈3, Pres 7 mod +2, Focus 5 def −2: strain = 3+1+2−2 = 4/exchange. Composure max = 17. Exchanges to Rattled: 17/4 = 4.25 → exchange 5.
- **Not degenerate.** Elite orators still face meaningful Composure pressure in Grand Debates. Fast resolution but not auto-win. Design is clean.

**Minimum vs Maximum matchup (2D vs 20D):**
- E[A] = 6.6, E[B] = 0.7. Expected margin ≈ 5.9.
- Primary genre, res=1: movement = floor(5.9)−1 = 4 per exchange. Track reaches 9 from neutral (5) in one exchange. Debate over in exchange 1.
- Strain to Presence 1 character: 5.9+1+2−1 = ~8. Composure 5 → negative. Rattled before exchange resolution completes.
- **This matchup should not occur** in institutional play (Presence 1 characters would not be selected as orators). GM should not allow it. No rules change needed — institutional gatekeeping is the design intent.

---

## MODE J — COGNITIVE LOAD

**Per-exchange step count:**

| Step | Rolls | Lookups | Formulas | Total actions |
|------|-------|---------|----------|---------------|
| Read (both) | 2 | 2 (result table) | 0 | 4 |
| Choose | 0 | 1 (genre/orientation) | 0 | 1 |
| Argue (×2) | 2 | 1 (Memory check) | 0 | 3 |
| Resolve interaction type | 0 | 1 (CLASH/COMP/DIVERGE/TIE?) | 2 (effective_margin, movement) | 3 |
| Strain | 0 | 0 | 1 (formula) | 1 |
| Concentration | 0 | 0 | 1 (update) | 1 |
| Ledger | 0 | 0 | 1 (record) | 1 |
| **Base total** | | | | **14** |
| + Corroboration | +2 | +1 | +1 | **+4** |

**Table-play feasibility:**
- 3-exchange Formal Debate: ~42 steps base, ~54 with Corroboration. **Manageable** — comparable to a medium-complexity combat round.
- 5-exchange Grand Debate: ~70 steps base, ~90 with Corroboration. **At the edge** — requires a GM reference card. Without one, calculation errors are likely at steps 6-7 when Concentration and Strain are both in play.

**[F-D-06] P2:** Grand Debate (5 exchanges) with Corroboration active reaches ~90 resolution steps. No GM reference card exists in the current design doc. Recommend: create a one-page debate ledger template (pre-filled GM-facing) as a companion tool. Not a design fault — a tooling gap.

**Cognitive load pressure points:**
1. Interaction type identification (Step 3): Players must remember CLASH/COMPETITION/DIVERGE conditions. Most confusing: COMPETITION (same genre, same orientation) vs CLASH (same genre, opposite orientation). A 2×2 grid on the reference card resolves this.
2. Effective_margin formula: floor(margin × genre_weight × orientation_weight) − resistance. The floor + three multiplicands make this the hardest single calculation. For Divergence, halving adds another step.
3. Concentration tracking: Two depletion conditions (−1/exchange, −1/loss). Easy to miss the second trigger.

---

## MODE L — PRECEDENT COMPARISON

### Burning Wheel: Duel of Wits

| Feature | BW DoW | Valoria Debate |
|---------|--------|---------------|
| Health pool | Body of Argument (Will-based) | Composure (Poise+Bonds+3) |
| Actions per exchange | 3 scripted volleys | 1 argue roll + orientation choice |
| Hidden information | Scripted volleys revealed simultaneously | Read exchange partially reveals |
| Compromise | Proportional to remaining BoA | Track position (4–6 zone) |
| Audience | None | Faction composition + weights |
| Character differentiation | Rhetoric skill primarily | Presence, History, Poise, Focus, Attunement, Bonds |
| Matchup problem | Volley type vs volley type | Genre × audience resonance |

**Assessment:** Valoria's system is more mechanically differentiated and context-sensitive than BW DoW. The genre/orientation matrix + audience resonance system has no published precedent — it is a genuine design contribution. Trade-off is cognitive load (~2× BW's per-exchange calculation count).

### Published TTRPG social systems not yet covered in Valoria simulation:
- Ironsworn's Compel (single roll, narrative) — not a model
- PbtA Parley — not a model
- Exalted 3e Social influence — closest to Valoria's multi-attribute social combat; not yet compared

---

## FINDINGS SUMMARY

| ID | Mode | Severity | Description | Disposition |
|----|------|----------|-------------|-------------|
| F-D-01 | D (Regression) | **P1** | DIVERGE+TIE: both score 0, different genres — Tie rule and Divergence resolution conflict | PP-097 PROVISIONAL |
| F-D-02 | D (Deadlock) | P2 | Regroup at Concentration=0: Spent state — does Regroup consume or apply the penalty? | PP-098 PROVISIONAL |
| F-D-03 | D (Ambiguity) | P2 | Obscuring in Divergence: no orientation_weight defined; Doubt Marker rule vs Divergence path | PP-099 PROVISIONAL |
| F-D-04 | D (Boundary) | P2 | Presence 1 characters cannot meaningfully participate in formal debate — no floor mechanic | Institutional gatekeeping implied; no rules change needed |
| F-D-05 | D (Optimal Play) | P3 | Memory bonus (+2D) is always-optimal when any named claim exists; no counter-incentive | Accepted; monitor in playtesting |
| F-D-06 | J (Cognitive Load) | P2 | Grand Debate + Corroboration: ~90 resolution steps, no GM reference card | Tooling gap; recommend ledger template |
| F-D-07 | D (Cascade) | P3 | Overwhelming + Pres 6-7: up to 5 strain in one exchange; Composure ≤ 7 opponent Rattled by exchange 2 | Accepted — intended breakthrough mechanic |

---

## SIM-DEBT-01 RE-CALIBRATION: NEW BASELINES

Old calibration (v1+v2) used Cognition+History pool. Baselines below are corrected for (Presence×2)+History.

| Value | Old baseline (INVALID) | New baseline | Notes |
|-------|----------------------|--------------|-------|
| Typical pool (Pres 3, Hist 2) | 5D | 8D | +60% |
| E[winning margin, symmetric] | ~1.6 | ~2.0 | +25% |
| P(Overwhelming) symmetric | ~25% | ~60% | +140% |
| Typical strain/exchange (CLASH, Pres 3 winner) | 1-2 | 2-3 | +50-100% |
| Exchanges to Rattled (Composure 9) | 7-9 | 3-5 | Halved |
| Exchanges to Rattled (Composure 7) | 5-7 | 2-4 | Halved |
| Track movement/exchange (primary, res=1) | 0 (often zero) | 1 (consistent) | More decisive |
| Concentration durability (mid, Conc=6, losing 50%) | — | ~4 exchanges | New metric |

**SIM-DEBT-01 status: PARTIALLY RESOLVED.** Modes A+D establish new calibration baselines. A full Mode C (scenario run with named characters) is required before treating Composure thresholds as final. Particularly: Rattled trigger frequency at new baseline needs scenario validation.

**Recommended next simulation:** Mode C — 3-exchange Formal Debate, Baralta vs Himlensendt (Church vs Hafenmark, Parliamentary session, known NPC stats), using new pool formula. This would complete SIM-DEBT-01 and establish full scenario coverage.

---

## PROVISIONAL PATCHES APPLIED THIS RUN

| Patch | Description |
|-------|-------------|
| PP-097 | DIVERGE+TIE: Tie rule fires on equal successes regardless of interaction type, including Divergence. Both orators take 1 strain; track +1 toward initiative holder. Rationale: "any interaction type" language is explicit. |
| PP-098 | Regroup at Concentration=0: Regroup consumes the Spent state without applying −2D/+1D penalty. Concentration restores by Focus score. Rationale: no argue roll occurs during Regroup — penalty has no application target. |
| PP-099 | Obscuring in Divergence: use effective_margin formula at orientation_weight=1.0 to determine Divergence winner. If winner used Obscuring, place Doubt Marker on opponent instead of track movement. No track movement. Rationale: Obscuring replaces track movement consistently regardless of interaction type. |

---

## OPEN ITEMS FROM THIS RUN

Carried forward to §6.8 / §6.9 of debate_system_redesign_v1.md for future testing:
- Multi-party debates (3+ orators): P1, no procedure
- Thread operations during debate: P1, no procedure
- Corroboration in practice (not yet simulated): P2
- Royal Audience proceeding: P2
- Rattled → Unmask decision point: P2 (Rattled never triggered in v1/v2; new baselines suggest it will fire regularly)
- Genre pivot mid-debate: P2
- Mixed Guilds audience: P2

---
*End SIM-D-01. Committed: 2026-04-02.*
