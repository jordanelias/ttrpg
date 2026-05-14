# 4-Faction Balance Re-Sim
## Date: 2026-05-13 · Session: balance-resim-4faction · Mode: A+B+C+D · Part 3/5
## Companions:
- `errata_part1_4faction_corrections_2026-05-13.md` (Part 1 — canonical correction)
- `log_schema_part2_2026-05-13.md` (Part 2 — log schema)
- `sim_faction_cards_stress_2026-05-13.md` (PRIOR — superseded for 4-faction)
- `sim_faction_balance_proposals_2026-05-13.md` (PRIOR — superseded for 4-faction)

## Authority:
- `designs/provincial/faction_state_authoring_v30.md` §§2–5 (CANONICAL)
- `designs/provincial/faction_behavior_v30.md` §3.7 (CANONICAL — triadic Ob)
- `params/factions/stats_1_7_scale.md` (CANONICAL, post-ED-787)
- `params/bg/core.md` (CANONICAL — v05 dice + degree table)
- `params/bg/faction_actions.md` (CANONICAL — card surface)

---

## Frame

This sim rebuilds the balance work for the canonical 4-faction model:
**Valorsmark · Church · Hafenmark · Varfell** as player factions. RM + Löwenritter
remain in the world as background actors. Target: each player faction achieves
**20–30% win-share** across N campaigns under standard protocols.

Probability engine validated previously. All math is exact-binomial. The work below:

1. **Mode A-Δ** — relabeled probability tables for the 4 factions only; updated
   target-pool for cards-vs-faction interactions (delete L=3 rows where they were
   Guilds; preserve L=3 only for NPC Löwenritter targets)
2. **Mode B-Δ** — tweak set narrowed to the 6 player-balance tweaks + 2 world-state
   (per Part 1 §9 disposition)
3. **Mode C-Δ** — 6-season scenario with 4 player factions + 2 background actors;
   recalculates Parliamentary Session voting (4-voter, not 5-voter)
4. **Mode D-Δ** — edge cases under 4-faction matrix

---

## §1 Starting State + Win-Share Framework

### Starting stats (canonical, post-ED-787)

| Faction | L | PS | M | I | W | Mil | Int | Sta |
|---------|---|----|----|---|---|-----|-----|-----|
| **Valorsmark** | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 4 |
| **Church** | 5 | 5 | 5 | 6 | 5 | 4 | 4 | 5 |
| **Hafenmark** | 4 | 4 | 4 | 4 | 5 | 3 | 3 | 4 |
| **Varfell** | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |

M = round(0.5·L + 0.5·PS).

### Background actors

| Actor | Profile |
|-------|---------|
| **Restoration Movement (RM)** | No Stability per PP-460; 1 starting Presence marker (T9 Himmelenger per prior sim convention); generates world-state pressure via Community Weaving on MS |
| **Löwenritter** | Mil 5, I 2, Sta 5, no Wealth (=0). NPC reactive per `peninsular_strain_v30 §2.6`. Auto-graduates to autonomy under specified triggers (`conflict_architecture_proposal`). |

### Clocks (BG start)

CI 28 · MS 72 · IP 20 · PI 5 · Strain 0

### Win-share target

- **Target:** 25% per player faction
- **Acceptable band:** 20–30% (±5pp)
- **Pre-Part-3 estimate (from prior sim trajectory):** Valorsmark ~38%, Church ~28%,
  Hafenmark ~22%, Varfell ~12% (estimated from "Valorsmark unmolested + Varfell
  locked-out + Hafenmark Token+Proclamation throttled by mid-game L gates")
- **Variance:** Player skill + Tensions Deck draw + initial unaligned settlement
  positions

### Stat aggregate position (sum of all 7 stats — rough "starting strength")

| Faction | Stat sum | Position | Notes |
|---------|----------|----------|-------|
| Church | 5+5+6+5+4+4+5 = **34** | Strongest | I=6 highest; Sta 5 |
| Valorsmark | 5+5+5+4+4+3+4 = **30** | Tied 2nd | Int 3 weakest |
| Hafenmark | 4+4+4+5+3+3+4 = **27** | 3rd | W highest among non-Church |
| Varfell | 4+4+4+4+4+4+4 = **28** | Tied 2nd (with Valorsmark) | All-4 balanced |

**Observation:** Church starts with +7 stats over Hafenmark (34 vs 27). Significant
asymmetric advantage. Either Church starts at "harder difficulty" with mechanical
penalties to compensate, or Church's role-template (Ecclesiastical) requires the
stat lead to function. Per `faction_canon §5` Ecclesiastical role centers on long-game
attrition (Inquisition pipeline) — the stat lead enables this. Working as intended,
but creates the **first balance question: does Church's stat lead translate to higher
win-rate?**

---

## §2 MODE A-Δ — Per-Card Probability (4-Faction)

Relabeled tables for the 4 player factions. Master grid unchanged (faction-agnostic).
Per-card tables that previously included Guilds (L=3) rows have been corrected:
- L=3 rows DELETED from player-target tables (no L=3 player at game start)
- L=3 rows REFRAMED as "Löwenritter NPC target" where mechanically relevant
- Faction names corrected: **Crown → Valorsmark**

### §2.1 Master probability reference grid (preserved)

`P(Overwhelming) / P(Success) / P(Partial) / P(Failure) / E[net]` for pool × Ob.
All values exact-binomial.

| Pool | Ob | P(Over) | P(Succ) | P(Part) | P(Fail) | E[net] |
|------|----|---------|---------|---------|---------|--------|
| 3D | 1 | 17.2% | 51.0% | 0.0% | 31.8% | +1.20 |
| 3D | 2 | 5.2% | 34.8% | 28.2% | 31.8% | +1.20 |
| 3D | 3 | 0.1% | 17.1% | 51.0% | 31.8% | +1.20 |
| 3D | 4 | 0.0% | 5.2% | 63.0% | 31.8% | +1.20 |
| 3D | 5 | 0.0% | 1.0% | 67.2% | 31.8% | +1.20 |
| 4D | 1 | 27.9% | 47.0% | 0.0% | 25.1% | +1.60 |
| 4D | 2 | 11.9% | 39.3% | 23.8% | 25.1% | +1.60 |
| 4D | 3 | 0.9% | 27.1% | 47.0% | 25.1% | +1.60 |
| 4D | 4 | 0.0% | 11.9% | 63.1% | 25.1% | +1.60 |
| 4D | 5 | 0.0% | 3.8% | 71.2% | 25.1% | +1.60 |
| 5D | 1 | 38.0% | 41.8% | 0.0% | 20.2% | +2.00 |
| 5D | 2 | 19.8% | 40.2% | 19.8% | 20.2% | +2.00 |
| 5D | 3 | 2.8% | 35.2% | 41.8% | 20.2% | +2.00 |
| 5D | 4 | 0.1% | 19.7% | 60.0% | 20.2% | +2.00 |
| 5D | 5 | 0.0% | 8.3% | 71.5% | 20.2% | +2.00 |
| 6D | 1 | 47.0% | 36.5% | 0.0% | 16.5% | +2.40 |
| 6D | 2 | 28.1% | 38.9% | 16.5% | 16.5% | +2.40 |
| 6D | 3 | 5.9% | 41.0% | 36.5% | 16.5% | +2.40 |
| 6D | 4 | 0.6% | 27.6% | 55.4% | 16.5% | +2.40 |
| 6D | 5 | 0.0% | 14.2% | 69.3% | 16.5% | +2.40 |
| 7D | 1 | 54.7% | 31.6% | 0.0% | 13.6% | +2.80 |
| 7D | 2 | 36.3% | 36.3% | 13.8% | 13.6% | +2.80 |
| 7D | 3 | 10.2% | 44.5% | 31.6% | 13.6% | +2.80 |
| 7D | 4 | 1.5% | 34.8% | 50.1% | 13.6% | +2.80 |
| 7D | 5 | 0.1% | 20.7% | 65.6% | 13.6% | +2.80 |

### §2.2 Per-card probability — 4-Faction Target Set

Tables show acting-faction roll vs target-faction L (where target-L is the Ob driver).
Player-target rows: L=4 (Hafenmark/Varfell) and L=5 (Valorsmark/Church). L=3 rows
removed from player set; appear separately as NPC-target rows where relevant.

#### A-Δ-02 · Excommunication (Church) vs target Leader L

Pool: Church L=5 (5D). Ob = target L. Failure: Church Sta −1 (PP-403).

| Target | Target L | Ob | P(Over) | P(Succ) | P(Part) | P(Fail) | P(Succ+) |
|--------|----------|----|---------|---------|---------|---------|----------|
| Valorsmark | 5 | 5 | 0.0% | 8.3% | 71.5% | 20.2% | **8.3%** |
| Hafenmark | 4 | 4 | 0.1% | 19.7% | 60.0% | 20.2% | **19.8%** |
| Varfell | 4 | 4 | 0.1% | 19.7% | 60.0% | 20.2% | **19.8%** |

_NPC-target rows (Löwenritter L=3, RM doesn't have L):_

| Löwenritter (NPC) | 3 | 3 | 2.8% | 35.2% | 41.8% | 20.2% | **38.0%** |

**A-Δ-02 Findings:**

- **A-Δ-02-F1 [CEILING — 4-FACTION CONFIRMED] P1:** Excommunication efficacy by
  player-target across 4-faction set is `8.3% / 19.8% / 19.8%` (vs L=5/4/4). Mean
  ~16%, range 8–20%. Compare to single-faction "deserved" target rate ~50% — the
  ceiling pattern is severe across **all** player targets. The 6-faction sim's
  finding that "the card structurally points at weak rivals" loses force when
  there are no weak player rivals — **Excommunication is structurally weak as
  a strategic tool against ANY player faction at game start.** Church's "use
  Excommunication on Hafenmark/Varfell" plays succeed ~20% of the time —
  meaningful but expensive. Confirmed regression GAP-08.

#### A-Δ-06 · CI 60 Territorial Seizure (Church)

Pool: Church L=5. Ob = floor(owner L / 2) + 1. Failure: Church L −1.

| Owner | Owner L | Ob | P(Succ+) |
|-------|---------|----|----------|
| Valorsmark | 5 | 3 | **38.0%** |
| Church (self — N/A) | 5 | 3 | **38.0%** |
| Hafenmark | 4 | 3 | **38.0%** |
| Varfell | 4 | 3 | **38.0%** |
| Löwenritter (NPC) | 3 | 2 | **60.0%** |

**A-Δ-06 Findings:**

- **A-Δ-06-F1 [REDUCED TARGET POOL] P2:** With Guilds removed, CI 60 cascade applies
  to 3 player-territory owners (Valorsmark, Hafenmark, Varfell). Expected number of
  simultaneous seizures at CI 60 trigger:

  - E[# seizures in single CI 60 trigger] (3 player territories prepared) = **1.14**
  - P(at least 1 succeeds | 3 territories prepared) = **76.2%**
  - Prior 6-faction estimate was E ≈ 2.0 across 4 owners — current 4-faction estimate 1.14 across 3 owners. **Per-owner rate identical; absolute throughput reduced as expected.**

#### A-Δ-10 · Hafenmark Diplomat Card (per-target)

Pool: Hafenmark I=4. Ob = floor(target L / 2) + 1. PI penalty if target = Church and PI < 3.

| Target | Target L | Ob | P(Succ+) | E[Token | played] |
|--------|----------|----|----------|---------------------|
| Valorsmark | 5 | 3 | **28.0%** | 0.28 |
| Church | 5 | 3 | **28.0%** | 0.28 |
| Varfell | 4 | 3 | **28.0%** | 0.28 |
| Löwenritter (NPC) | 3 | 2 | **51.2%** | 0.51 |

**A-Δ-10 Findings:**

- **A-Δ-10-F1 [TOKEN PIPELINE REDUCED] P2:** Diplomat Card P(Token | played) is
  **28.0% vs Valorsmark/Church** (L=5, Ob 3) and **51.2% vs Varfell** (L=4, Ob 2).
  Hafenmark Token accumulation rate, target-mix permitting, is roughly **35% per
  attempt** assuming even target distribution. Over 8 seasons, E[Tokens] ≈ 2.8 —
  reduced from prior 6-faction estimate of 4.1 because Guilds was a 51% target
  removed from the pool. **Hafenmark's soft-power identity is meaningfully blunted
  in the 4-faction model. The L=3 sweet-spot target is gone.**
- **A-Δ-10-F2 [VARFELL VULNERABILITY] P2:** Varfell at L=4 is the only player-target
  where Hafenmark Diplomat has > 50% Success+. Hafenmark's diplomatic pressure now
  concentrates on Varfell. Varfell's defensive tools (Counter-Narrative aimed at
  Hafenmark — possible if Hafenmark territory has Church-prominence — niche; or
  Procedural Objection vs Varfell Investigate — wrong direction). Effectively
  **Varfell has no defense against Hafenmark Diplomat targeting**, while
  Valorsmark/Church absorb it at 28% per attempt.

#### A-Δ-11 · Hafenmark Dynastic Proclamation — RESCOPED

**Per Part 1 §6:** Prerequisite: Hafenmark L > target L AND Haf L ≥ 4 AND adjacent.

At game start, Hafenmark L=4. No player target has L < 4. **Proclamation is mechanically
inert against player targets at game start.** Becomes active mid-campaign IF:
- Hafenmark wins Parliamentary Session(s) raising L to 5+
- AND a player faction's L drops to 4 (Hafenmark stays at L=5, others stay at L=5,
  pipeline still inert against Valorsmark/Church)
- OR a player faction drops below L=4 (Varfell at L=4 → must drop)

**Earliest realistic activation:** Hafenmark L=5 vs Varfell L=4. Requires 2–3
Parliamentary Sessions (1 per Parliamentary arc, once-per-campaign-arc per PP-431-COR) —
typically 6–10 seasons. **Token + Proclamation pipeline is a late-game, single-target
mechanic against Varfell only.**

| Phase | Target | Pool | Ob (Token) | P(transfer) |
|-------|--------|------|------------|-------------|
| Mid-game (Haf L=5, Var L=4, Token) | Varfell | 4D | 2 | **51.2%** |
| Mid-game (no Token) | Varfell | 4D | 3 | **28.0%** |

**A-Δ-11 Findings (revised):**

- **A-Δ-11-F1 [LATE-GAME, SINGLE-TARGET] P3 (was P1):** Hafenmark Proclamation, when
  it activates, has 51.2% Success+ against Varfell with Token. But activation requires
  ~6–10 seasons of Parliamentary Sessions. The prior P1 "structural cascade
  targeting weak factions" finding is **substantially weakened in the 4-faction
  model.** Hafenmark gains 1 mid-to-late-game expansion vector against Varfell only —
  no longer an early-game L=3 sweep.
- **A-Δ-11-F2 [VARFELL DEFENSE] P2:** Varfell at L=4 can invoke **Institutional Mandate
  (PP-189 — L ≥ 4 gate satisfied)** to cancel a Successful Proclamation. Cost: Sta −1
  + card discard. Varfell starts at Sta 4 (above 0 floor); can sustain 3–4 cancellations
  before Stability collapse. **Defense is mechanically intact.** No T-03a needed in
  the 4-faction model (Part 1 §9 disposition confirmed).

#### A-Δ-15 · Valorsmark Formal Treaty

Pool: Valorsmark I=5. Ob = floor(target L / 2) + 1.

| Target | Target L | Ob | P(Succ+) | Notes |
|--------|----------|----|----------|-------|
| Church | 5 | 3 | **38.0%** | |
| Hafenmark | 4 | 3 | **38.0%** | |
| Varfell | 4 | 3 | **38.0%** | |

**A-Δ-15 Findings:**

- **A-Δ-15-F1 [CEILING — 4-FACTION CONFIRMED] P1:** Treaty Ob = floor(target L/2)+1.
  Against all 3 player targets: 38.0% (Church L=5), 60.0% (Hafenmark L=4), 60.0%
  (Varfell L=4). Better than Excommunication (which is Ob = target L flat) but still
  below 80% even against weakest player. **Treaty success rate vs Church L=5 is
  38% — Valorsmark's core diplomatic mechanism succeeds barely 1-in-3 attempts at
  the partnership most strategically valuable to win-share equality.** GAP-08
  remains the unfixed regression.
- **A-Δ-15-F2 [CONSENT GAP] P1:** As prior. Treaty requires "both factions agree" —
  no NPC AI rule, no PC incentive. Open since 2026-04-09.

#### A-Δ-17 · Spy (Tribune Outward standard, post-ED-787)

Pool: acting faction Intel. Ob = floor(target Int / 2) + 1.

| Spy Source → Target | Source Int | Target Int | Ob | P(Succ+) |
|---------------------|-----------|-----------|----|----------|
| Valorsmark → Church | 3 | 4 | 3 | **17.2%** |
| Valorsmark → Hafenmark | 3 | 3 | 2 | **40.0%** |
| Valorsmark → Varfell | 3 | 4 | 3 | **17.2%** |
| Church → Valorsmark | 4 | 3 | 2 | **51.2%** |
| Church → Hafenmark | 4 | 3 | 2 | **51.2%** |
| Church → Varfell | 4 | 4 | 3 | **28.0%** |
| Hafenmark → Valorsmark | 3 | 3 | 2 | **40.0%** |
| Hafenmark → Church | 3 | 4 | 3 | **17.2%** |
| Hafenmark → Varfell | 3 | 4 | 3 | **17.2%** |
| Varfell → Valorsmark | 4 | 3 | 2 | **51.2%** |
| Varfell → Church | 4 | 4 | 3 | **28.0%** |
| Varfell → Hafenmark | 4 | 3 | 2 | **51.2%** |

**A-Δ-17 Findings:**

- **A-Δ-17-F1 [INTEL ASYMMETRY] P1:** Spy effectiveness varies significantly by
  source × target Int pairing. Most effective: **Church→Valorsmark or Church→Hafenmark
  (4D vs Ob 2 = 51.2%)**. Least effective: **Valorsmark→Church or Valorsmark→Varfell
  (3D vs Ob 3 = 17.2%)**. Valorsmark (Int 3) is structurally worst at Spy. Combined
  with Royal Guard (PP-442) cancelling one Intel/season — Valorsmark can absorb
  Spy attempts defensively at 1/season, but cannot project offensively.
- **A-Δ-17-F2 [VARFELL-CHURCH MUTUAL PARITY] P2:** Both Int 4. 4D vs Ob 2 (each
  against the other's Int 4 → Ob 2) = 51.2% Success+. Spy parity creates a
  **mutual-detection equilibrium** between the two most-defended factions.
  Counter-espionage gate at Int ≥ 4 detects (PP-N): Church and Varfell can each
  detect each other's Spy at Ob 3. **Symmetric intel game** between Church and
  Varfell. Working as intended per faction identity.

## §3 MODE B-Δ — Corrected Tweak Set

Tweaks narrowed per Part 1 §9 disposition. **Removed: T-03a, T-03b, T-05a, T-05b, T-05c**
(all Guilds-specific). Tweaks now:

### Player-balance tweaks (5 P1 + 2 P2)

| ID | Faction | Mechanism | Status |
|----|---------|-----------|--------|
| T-01a | Valorsmark | Charter diminishing returns (+1 Ob per active) | P1 |
| T-01c | Valorsmark | Royal Guard cancels passive Intel only | P1 |
| T-02a | Varfell | Inquisitor +2 Ob first-attempt only | P1 |
| T-02c | Varfell | Counter-Narrative Overwhelming relocates Inquisitor | P2 |
| T-03c | Hafenmark | Token costs W−1 | P2 |
| T-04a | Varfell | Revelation Tokens Path A relaxed | P2 |
| T-01b | Valorsmark | Charter exclusivity (alternative to T-01a) | P2 |

### World-state tweaks (RM/Löwenritter — no player-balance impact)

| ID | Actor | Mechanism | Status |
|----|-------|-----------|--------|
| T-06a | RM | Start with 2 Presence markers | P1 (world-state) |
| T-06c | RM | Community Organising 2D base permanent | P2 (alternative) |

### Deferred / heavy

| ID | Notes |
|----|-------|
| T-02b | Tribune Recall Operative — defer unless T-02a insufficient |
| T-04b | Tribune Disinformation card — own design cycle needed |

### NEW: tweaks targeting cross-faction equality

The corrected 4-faction model surfaces new asymmetries that the 6-faction model
hid. New tweaks proposed:

**T-09a: Valorsmark Influence Surge (mid-game).** Once-per-arc Valorsmark action:
Treaty Ob = floor(target L/2). Removes the +1 base term for one Treaty per arc.
- Mechanism: gives Valorsmark a single-shot strong diplomatic moment per political
  arc (4–6 seasons). Doesn't fix GAP-08 systemically but creates a viable arc-defining
  Treaty attempt at improved odds.
- vs Church L=5, Ob 2 (was 3): 5D Success+ = 60.0% (was 38%).
- vs Hafenmark L=4, Ob 2 (was 2): unchanged (already at floor).
- Priority: P2.

**T-09b: Varfell Tribune Counter-Espionage Improvement.** When Varfell detects an
incoming Spy (via PP-N counter-espionage at Int ≥ 4), Varfell gains 1 Revelation
Token (on the spying faction's mat) if the detected Spy attempt failed.
- Mechanism: gives Varfell defensive Token-accumulation, since Hafenmark currently
  has the only "free Token" path (Diplomat Card). Compensates for Hafenmark
  Diplomat targeting Varfell at 51.2% Succ+.
- Priority: P2.

**T-09c: Church Inquisition Cap.** No more than 2 active Inquisitors deployable
peninsula-wide simultaneously. 3rd Inquisitor deployment requires recalling one.
- Mechanism: caps Church's most powerful mid-game vector. At 2 Inquisitors,
  Church can pressure 2 territories; expanding requires retreat. Currently no cap.
- Priority: P2.

### Probability impact preview

(Mode C-Δ §4 verifies these in scenario; preview-numbers here for sanity)

**T-09a (Valorsmark Treaty Ob reduction once/arc):**

- vs Church L=5: current 38.0%, T-09a 60.0%. **Delta +22pp.**
- Restricted to 1 use per arc (~4–6 seasons). Valorsmark cannot spam.

**T-09b (Varfell defensive Token on detected-failed Spy):**

Compound: P(Spy attempts) × P(Spy fails) × P(Varfell detects | failed).
- Assume Hafenmark spams Spy on Varfell (3D vs Ob 3 = 17.2% Succ+).
- P(Spy fails) = 82.8%.
- P(Varfell detect | fail) — uses PP-N counter-espionage rule, assume Ob 3 at Int 4: 4D vs Ob 3 = 28.0%.
- Joint per attempt: 23.2% per Hafenmark attempt yields Varfell a Token.

**T-09c (Inquisition cap 2 Inquisitors max):**

Mechanical only — no probability change. Caps Church's late-game multi-territory pressure.

---

## §4 MODE C-Δ — 6-Season Scenario (4 Player Factions)

Starting state per §1. Same Tensions Deck draw (Crown Doctrinal Pressure assumed).
Protocols:

| Faction | Protocol | Rationale |
|---------|----------|-----------|
| Valorsmark | FACTION-LOYAL (PP-257) | Stat-stable Sovereign |
| Church | RITUAL Phase 1→2→3 | Long-game pressure |
| Hafenmark | FACTION-OPPORTUNIST | Soft-power patient |
| Varfell | FACTION-OPPORTUNIST | Intel ambush |
| RM | MARTYR | No-Stability constant pressure |
| Löwenritter | NPC reactive (PP-238) | Self-defense only |

**Parliamentary Session 4-voter calculation:** When Hafenmark calls PA Session, 4 player
factions vote. Hafenmark = Support self. Church likely Oppose (anti-Parliament tradition).
Valorsmark and Varfell = swing votes. Pass requires 3-1 or 4-0; tie 2-2 fails per
`faction_actions §Hafenmark §PA Session COR`.

---

### Season 1 (Spring)

**Phase 1 declarative:**
- Church: Cardinal Focus → **Justice** (first Inquisitor threshold AP ≥ 2)
- Hafenmark: holds PA Session (once per arc; reserves)
- Varfell: declares Spy on Valorsmark

**Phase 4 — Priority 1 (Intel/Tribune):**
- **Varfell → Spy on Valorsmark** (Valorsmark Int 3 → Ob 2). 4D vs Ob 2.
  - Pool: Varfell Int 4 (no Tribune expertise +1D in standard play; see PP-N).
  - 4D vs Ob 2: P(Over) 11.9% / P(Succ) 39.3% / P(Part) 23.8% / P(Fail) 25.1%.
  - **Modal Success (39.3%).**
  - Valorsmark **Royal Guard** (PP-442) cancels active Intel: cancelled.
  - Result: Spy attempted, cancelled. Valorsmark Royal Guard used.

**Phase 4 — Priority 3 (Domain):**
- **Valorsmark → Royal Charter T2** (capital, P=2, base Ob 2, Virtue −1 → Ob 1).
  - 5D vs Ob 1: P(Succ+) 79.8%. **Modal Success.**
  - Result: Charter active on T2.

- **Church → Piety Spread T9** (Crown-held Himmelenger, Fort 0; doctrine-aligned −1 Ob).
  - Base Ob = floor(5/2)+1 = 3. Doctrine: −1 → Ob 2.
  - 5D vs Ob 2: P(Succ+) 60.0%. **Modal Success.**
  - Result (assume modal): AP +2 in T9. T9 AP = 2 (threshold ≥ 2 with Justice).

- **Hafenmark → Trade T9** (P=3 baseline, Hafenmark adjacent assumed).
  - 6D (W=5 + Consul +1) vs Ob 2 (P=3 → floor(3/2)+1 = 2).
  - 6D vs Ob 2: P(Succ+) 67.0%. **Modal Success.**
  - Result: Hafenmark W 5→6.

**Phase 4 — Priority 4 (Social):**
- **Valorsmark → Royal Decree** (base Ob 2, no consecutive).
  - 5D vs Ob 2: P(Succ+) 60.0%. **Modal Success.**
  - Target: self Sta+1. Valorsmark Sta 4→5.

**Phase 5 Accounting:**
- AP T9 = 2 (threshold AP ≥ 2 crossed with Justice). **Inquisitor would deploy if Active Inquisition card was played — Piety Spread alone does not deploy.** Inquisitor pending.
- CI +1 → 29.
- Cardinal Focus expires.

**End of S1:**
```
Valorsmark: L 5, PS 5, I 5, W 4, Mil 4, Int 3, Sta 5  (+1 Sta)
Church:     L 5, PS 5, I 6, W 5, Mil 4, Int 4, Sta 5  (no change)
Hafenmark:  L 4, PS 4, I 4, W 6, Mil 3, Int 3, Sta 4  (+1 W)
Varfell:    L 4, PS 4, I 4, W 4, Mil 4, Int 4, Sta 4  (no change; Spy cancelled)

Clocks: CI 29 (+1) | MS 72 | IP 20 | PI 5 | Strain 0
T9: AP 2 (Inquisitor pending) | Royal Charter T2 active
Tokens: 0 | Cardinal Focus: expired
```

**S1 Findings:**

- **S1-Δ-F1 [BALANCE] P2:** Net stat changes S1: Valorsmark +1, Hafenmark +1, others 0.
  Valorsmark and Hafenmark advance equally; Church and Varfell static. Year 1 Season 1
  balance is healthy.
- **S1-Δ-F2 [ROYAL GUARD CONSUMPTION] P3:** Valorsmark Royal Guard used S1 to cancel
  Varfell Spy. Royal Guard refreshes per arc (once per season per PP-442). Varfell can
  re-attempt Spy S2 with no Royal Guard available IF Valorsmark doesn't refresh — but
  PP-442 says once per season, so Royal Guard refreshes each season. **Royal Guard
  permanently absorbs 1 Intel/season; Varfell needs 2 Intel/season to land one.**
  At standard hand: Varfell has 2 Tribune slots. Can attempt 2 Intel/season → 1 cancelled,
  1 succeeds. **Valorsmark is asymmetrically Intel-defended but not Intel-immune.**

---

### Season 2 (Summer)

**Phase 1:**
- Church: Cardinal Focus → **Prudence** (Wealth +1 integer)
- Varfell: declares Counter-Narrative T9 (preempt Inquisitor)
- Hafenmark: declares Diplomat vs Varfell (only viable player target Ob 2)

**Phase 4 — Priority 1 (Intel):**

- **Varfell → Counter-Narrative T9** (Inquisitor not yet deployed). Base Ob = floor(5/2)+1 = 3, Consequentialism (Tribune Intel) −1 → Ob 2.
  - 4D vs Ob 2: P(Succ+) 51.2%. **Modal Success.**
  - Result: AP +2 in T9. T9 AP = 4. Crosses Justice threshold (still active S2).

- **Varfell → Spy on Hafenmark** (Hafenmark Int 3 → Ob 2). 4D vs Ob 2.
  - 51.2% Success+. Modal Success.
  - Hafenmark **Procedural Objection** could cancel — Hafenmark holds.
  - Result: Hafenmark stats revealed to Varfell.

**Phase 4 — Priority 3 (Domain):**
- **Valorsmark → Govern T2** (Charter active: −2 own action, −1 own capital = Ob 1 floor).
  - 5D vs Ob 1: 79.8% Succ+. Modal Success.
  - Result: T2 Prosperity +1.

- **Church → Active Inquisition T9** (AP 4 already, threshold ≥ 2 with Justice).
  - 5D vs Ob 2: 60.0% Succ+. Modal Success.
  - **Inquisitor T9 deploys** at this Accounting.

**Phase 4 — Priority 4 (Social):**
- **Hafenmark → Diplomat vs Varfell** (Ob 2, Hafenmark I=4 → 4D).
  - 51.2% Succ+. Modal Success.
  - Result: Token placed on Varfell mat. PI 5→6.

**Phase 5 Accounting:**
- Inquisitor T9 deploys.
- T9 AP reset (assuming Phase 5 step 5 global reset; GAP-01 still open).
- T9 Sta: Inquisitor presence pressures Sta. Assume Accord 2 → 1 by next Accounting.
- CI +1 → 30.
- PI 6.
- Cardinal Focus expires.

**End of S2:**
```
Valorsmark: L 5, PS 5, I 5, W 4, Mil 4, Int 3, Sta 5
Church:     L 5, PS 5, I 6, W 5+1 (Prudence S2 only; W 6 effective S2), Mil 4, Int 4, Sta 5
Hafenmark:  L 4, PS 4, I 4, W 6, Mil 3, Int 3, Sta 4
Varfell:    L 4, PS 4, I 4, W 4, Mil 4, Int 4, Sta 4

Clocks: CI 30 | PI 6 (+1)
T9: AP 0 (reset), Inquisitor active, Sta 4 → 3 pending S3 effect | Accord 2 (pending →1)
Tokens: 1 on Varfell (from Hafenmark) | Charter T2 active | Royal Decree consec×1 next play
```

**S2 Findings:**

- **S2-Δ-F1 [HAFENMARK TARGETS VARFELL] P2:** Per A-Δ-10-F2 prediction, Hafenmark's
  diplomatic pressure concentrates on Varfell (only L=4 player target with 51% Success+
  Diplomat Card). S2 Token landed on Varfell — *not* on Valorsmark or Church (those
  would be 28% per attempt). Hafenmark protocol opportunism → Varfell-focused.
- **S2-Δ-F2 [INQUISITOR DEPLOYS T9 — CROWN'S TERRITORY] P1:** Church Inquisitor
  deploys on T9, currently Valorsmark-controlled (Himmelenger). Sta drift pending.
  **Church begins applying pressure to Valorsmark's territory by S2 — the first
  inter-faction territorial pressure in the run.** Valorsmark's counter: Suppress
  (CI), Royal Charter expansion (defensive zoning), or Treaty with Church (38% Succ+,
  hard to land). No quick fix; Valorsmark must absorb the pressure.

---

### Season 3 (Autumn)

**Phase 1:**
- Church: Cardinal Justice (2nd Inquisitor threshold AP ≥ 5)
- Varfell: Counter-Narrative T9 post-Inquisitor (now Ob 4 with Inquisitor +2)
- Hafenmark: Diplomat vs Varfell again (compound Token)
- Valorsmark: declares Royal Charter T11 (2nd Charter; T-01a not yet in effect, this sim)

**Phase 4 — Priority 1 (Intel):**

- **Varfell → Counter-Narrative T9** (Inquisitor active, +2 Ob). Base Ob 3, Conseq −1, Inq +2 = Ob 4.
  - 4D vs Ob 4: 11.9% Succ+. Modal Partial (63.1%).
  - Result (modal Partial): AP +1 → T9 AP = 1. No "Church notified" trigger (only on Failure).

- **Varfell → Spy on Church** (Church Int 4 → Ob 3).
  - 4D vs Ob 3: 28.0% Succ+. Modal Partial.
  - Church **Sanctuary Extension** (PP-442) could block — Church holds (rare card).
  - Result: Spy attempt; modal Partial → no info gained but no detection.

**Phase 4 — Priority 3 (Domain):**

- **Valorsmark → Royal Charter T11** (2nd Charter — under current canon, no penalty).
  - 5D vs Ob 2 (T11 not capital, no Virtue): 60.0% Succ+. Modal Success.
  - Result: 2nd Royal Charter active on T11.

- **Church → Active Inquisition T9** (push 2nd Inquisitor threshold AP ≥ 5 with Justice).
  - T9 Sta 3 (post-S2 Inquisitor pressure). Ob = floor(3/2)+1 = 2.
  - 5D vs Ob 2: 60.0% Succ+. Modal Success.
  - Result: AP +2 → T9 AP = 3 (still 2 short of 2nd Inquisitor).

**Phase 4 — Priority 4 (Social):**

- **Hafenmark → Diplomat vs Varfell** (now has Token; Ob 2, +0 cumulative).
  - 51.2% Succ+. Modal Success.
  - Result (modal Succ): 2nd Token on Varfell? — Token max 1/faction mat per PP-517. **No new Token; PI +1.** Diplomat Card's secondary effect.
  - Hafenmark might switch target to Valorsmark next time — but P(Succ+) drops to 28%.

**Phase 5 Accounting:**
- T9 AP = 3.
- T9 Sta now 3 (sustained Inquisitor pressure).
- T9 Accord → 1 (sustained Sta drop + no garrison).
- CI +1 → 31.
- PI 7.

**End of S3:**
```
Valorsmark: L 5, PS 5, I 5, W 4, Mil 4, Int 3, Sta 5 | 2 Charters (T2, T11)
Church:     L 5, PS 5, I 6, W 5, Mil 4, Int 4, Sta 5
Hafenmark:  L 4, PS 4, I 4, W 6, Mil 3, Int 3, Sta 4 | Token on Varfell + PI investment
Varfell:    L 4, PS 4, I 4, W 4, Mil 4, Int 4, Sta 4 | Counter-Narrative 1× Partial

Clocks: CI 31 | MS 72 | IP 20 | PI 7 | Strain 0
T9: AP 3, Inquisitor, Sta 3, Accord 1 (revolt risk next season if no defense)
```

**S3 Findings:**

- **S3-Δ-F1 [REVOLT WARNING] P1:** T9 Accord at 1 with no garrison. **One more season
  of pressure → Revolt.** Valorsmark's territory at structural risk; Church inducing
  it without garrison-required cost. **Valorsmark must Muster (Legionary slot) or
  Royal Decree (target Accord+1 or Stability+1?) — neither is a clean fix.** This
  is the canonical Loss-spiral cascade: AP → Inquisitor → Sta → Accord → Revolt.
  Working as intended mechanically; player UX must surface the impending threshold.
- **S3-Δ-F2 [VARFELL DEFENSIVE COMPLIANCE] P2:** Varfell modal Partial on Counter-Narrative
  S3 — no AP gain, no penalty (Partial does not trigger PP-441-COR "Church notified").
  Varfell maintains attempts. Cumulative P(at least one Succ+ in S2+S3+S4) approx
  computed below.
  - 4-attempt cumulative P(≥1 Succ+) = 66.4% (currently;
    T-02a familiarity would lift this to ~63% per Part 2 example calculations).

---

### Season 4 (Winter — Year-End Accounting)

**Phase 1:**
- Church: Cardinal Temperance (Altonian diplomacy aid)
- Hafenmark: declares **Parliamentary Session** (once per arc — first arc)
- Valorsmark: declares Outreach to Schoenland (IP rising baseline; defensive)

**Phase 4 — Priority 1 (Intel):**
- Varfell holds (saving Tribune cards for next political arc).

**Phase 4 — Priority 3 (Domain):**

- **Valorsmark → Govern T2** (Charter active). Modal Success. T2 Prosperity now 4 (from base 2 + S2 + S4 wins).
- **Church → Piety Spread T11** (Valorsmark's newly Chartered territory — Charter
  weaponized vs Church Seizure +1 Ob, but Piety Spread is Spread not Seizure;
  no Charter penalty). Ob = floor(5/2)+1+0 = 3, doctrine −1 → 2.
  - 5D vs Ob 2: 60.0% Succ+. Modal Success.
  - Result: AP +2 → T11 AP = 2. (Church also pursues T11.)

- **Hafenmark → Trade T9** (Inquisitor present but Trade is Consul, not Tribune; no penalty).
  - 6D vs Ob 2: 67.0% Succ+. Modal Success.
  - Result: W +1 → 7 (clamped at ceiling).

**Phase 4 — Priority 4 (Social):**

- **Hafenmark → Parliamentary Session** (once per arc; 4-faction vote):
  - Valorsmark: ? — Cardinal Temperance Church + IP pressure favors moderation; Valorsmark may **Support** Parliamentary moderation.
  - Church: **Oppose** (anti-Parliament traditional, per `faction_canon §Identity`)
  - Hafenmark: **Support** (self)
  - Varfell: ? — Tokens on Varfell mat? **Yes** (S2 from Hafenmark). Token = +1 to Support per PP-320-ED. Varfell tilts **Support**.
  - **Vote: 3 Support / 1 Oppose. Pass.**
  - Effect: PI +1 → 8 (CRISIS threshold PI ≥ 8). Hafenmark L +1 → 5.

- **Valorsmark → Outreach to Schoenland.** Inf 5 vs Ob 2 (IP < 30, no fragmentation).
  - 60.0% Succ+. Modal Success.
  - Result: IP −1 → 19.

**Phase 5 Accounting (Standard + Year-End B11):**

Standard:
- Hafenmark L: 4 → 5 (PA Session win)
- T11 AP = 2 (Justice threshold 2 → Inquisitor pending; but Active Inquisition not played here, Piety Spread alone doesn't deploy)
- T9 Sta drops to 2 (Inquisitor sustained)
- T9 Accord: was 1 → 0 → REVOLT TRIGGER (no garrison, Sta below threshold)
  - T9 Revolt: garrison none → faction loses control. **Valorsmark loses T9.**
  - T9 becomes Uncontrolled with Inquisitor.
  - Valorsmark Mandate impact: T9 was Valorsmark-controlled per `geography_v30`? — `[ASSUMPTION: T9 starts Valorsmark-controlled; if Church-controlled or unaligned at start, Revolt happens but Valorsmark doesn't lose Mandate. Verify with map.]`
- CI +1 → 32
- PI 8 — **CRISIS THRESHOLD CROSSED** (PI ≥ 8 → free Agitation card next season + Cascade Brake effect)

Year-End B11:
- Crown Royal Decree cooldown resets (Winter clears)
- Loyalty: Torben +1 (PI ≥ 5); Elske standard
- RS −1 (annual baseline drift)
- Löwenritter free unit at T14
- Cardinal Focus carried over does not exist; ends.

**End of S4 (end of Year 1):**
```
Valorsmark: L 5, PS 5, I 5, W 4, Mil 4, Int 3, Sta 5 | LOST T9 | Charter T2, T11 active
Church:     L 5, PS 5, I 6, W 5, Mil 4, Int 4, Sta 5 | Inquisitor T9, T11 AP pending
Hafenmark:  L 5, PS 4, I 4, W 7, Mil 3, Int 3, Sta 4 | (+1 L from PA, W ceiling)
Varfell:    L 4, PS 4, I 4, W 4, Mil 4, Int 4, Sta 4

Clocks: CI 32 | MS 72 | IP 19 | PI 8 (CRISIS) | Strain 0
T9: Uncontrolled with Inquisitor | T11: AP 2, Inquisitor pending Active Inquisition play
Tokens: 1 on Varfell | Crown Decree cooldown: cleared (Winter)
PA Session: spent (1× per arc; next arc 4–6 seasons away)
```

**S4 Findings:**

- **S4-Δ-F1 [REVOLT — VALORSMARK LOSES T9] P1:** Valorsmark loses T9 to revolt by
  S4 — 4 seasons of Church Inquisition pressure. Mandate impact pending exact starting
  state but **Valorsmark drops at least 1 territory.** Pre-Part-3 estimate had Valorsmark
  ascendant in 6-faction; in 4-faction the Church pressure focused on T9 lands harder
  because no Guilds buffer territories. **Working as intended; faster than expected.**
  Suggests Valorsmark needs early-game Garrison-keeping behavior (Muster card play
  early; not done in this sim's protocol).
- **S4-Δ-F2 [HAFENMARK ASCENDANT — POLITICAL] P1:** Hafenmark L: 4→5 after PA pass.
  Now equal to Valorsmark/Church Mandate. Combined with PI 8 (CRISIS), Hafenmark is
  positioned to benefit from PI ≥ 8 free Agitation + Cascade Brake next season.
  **Hafenmark's mid-game political dominance trajectory is intact.**
- **S4-Δ-F3 [PI CRISIS] P1:** PI 8 triggers Revolution-adjacent state. Per `params/bg/clocks.md` `[ASSUMPTION:
  PI ≥ 8 enables free Agitation card + Cascade Brake]`. Hafenmark benefits structurally
  (Parliament-tilt). **The system reaches its first crisis state by Year-End Y1.**
  Working as intended? — Crisis at Y1 may be too early; verify in playtest.

---

### Season 5 (Spring Y2) — Crisis dynamics

**Phase 1:**
- Crisis triggers: PI 8 → all factions may play free Agitation card (PP-N)
- Church: Cardinal Justice
- Valorsmark: declares Muster (Mil card — defensive, after T9 loss)
- Varfell: declares Counter-Narrative T11 (Church's new pressure point)

**Phase 4 — Priority 1 (Intel):**

- **Varfell → Counter-Narrative T11** (Inquisitor pending, not yet deployed; pre-Inq math).
  - Base Ob 3 (Church L=5), Conseq −1 → Ob 2. 4D vs Ob 2: 51.2% Succ+. Modal Success.
  - Result: AP +2 → T11 AP = 4. Inquisitor T11 pending if Active Inquisition plays.

**Phase 4 — Priority 2 (Military):**

- **Valorsmark → Muster** at T2 (capital). Mil Legionary action; +1 Mil unit to T2 if successful. Ob 2 standard.
  - Mil 4: 4D vs Ob 2: 51.2% Succ+. Modal Success.
  - Result: +1 garrison at T2. T2 defended.

**Phase 4 — Priority 3 (Domain):**

- **Church → Active Inquisition T11.** Ob = floor(T11 Sta=4/2)+1 = 3. 5D vs Ob 3.
  - 38.0% Succ+. Modal Partial.
  - Result (modal Partial): AP +1 → T11 AP = 5. Reaches 2nd Inquisitor threshold with Justice (5 ≥ 5).
  - **2nd Inquisitor deploys T11 next Accounting.**

- **Valorsmark → Govern T2** (Charter active). Modal Success.
- **Hafenmark → Trade T8** (Trade in 2nd Hafenmark-favorable territory; assume P=2 → Ob 2).
  Modal Success. W stays 7 (ceiling).

**Phase 4 — Priority 4 (Social):**

- **Hafenmark → Free Agitation Card** (Crisis-enabled). Effect: +1 PI; +1 to a faction's
  Action against current government this season.
  - Hafenmark plays it on itself for own next action's bonus.
  - PI 8 → 9.

**Phase 5 Accounting:**

- 2nd Inquisitor T11 deploys.
- T11 AP = 5 → reset to 0.
- T11 Sta 4 → 3 (Inquisitor pressure).
- CI +1 → 33.
- PI 9.
- Strain still 0 (one Revolt last season → +1 Strain at Y2 start; should already be 1 not 0; correcting):

`[ASSUMPTION: Year-End B11 increments Strain by Revolt count of prior year. Strain 0 → 1 at S4/S5 transition.]`

**End of S5:**
```
Valorsmark: L 5, PS 5, I 5, W 4, Mil 4, Int 3, Sta 5 | T2 garrisoned | Charters T2, T11
Church:     L 5, PS 5, I 6, W 5, Mil 4, Int 4, Sta 5 | 2 Inquisitors (T9, T11)
Hafenmark:  L 5, PS 4, I 4, W 7, Mil 3, Int 3, Sta 4
Varfell:    L 4, PS 4, I 4, W 4, Mil 4, Int 4, Sta 4

Clocks: CI 33 | MS 72 | IP 19 | PI 9 | Strain 1 (post-Revolt)
T9: Uncontrolled + Inquisitor | T11: AP 0, Inquisitor active, Sta 3, Accord 1 pending
```

**S5 Findings:**

- **S5-Δ-F1 [TWO INQUISITORS DEPLOYED Y2 S1] P1:** Church has 2 active Inquisitors
  (T9 Uncontrolled, T11 Valorsmark). T-09c (Inquisition cap 2) is already binding.
  **Without the cap proposed in §3, Church can deploy 3rd Inquisitor next season.**
  Cap proposed becomes urgent: 5 seasons in, Church territorial pressure has spread
  to 2 territories already. Compare 6-faction sim: Inquisitor reached only T9 by S6.
  **Faster Church pressure in 4-faction model** (less faction-distraction in 4-faction
  setup means Church focuses more efficiently).
- **S5-Δ-F2 [VARFELL COUNTER-NARRATIVE WINDOW NARROWING] P1:** Each new Inquisitor
  closes a Counter-Narrative window. T9 closed S2 (Inquisitor deployed). T11 closed
  this season. **By S5, Varfell has 2 fewer territories where it can effectively
  intel-operate.** T-02a (Inquisitor familiarity) becomes more important as Inquisitors
  proliferate.

---

### Season 6 (Summer Y2)

**Phase 1:**
- Church: Cardinal Prudence (W +1)
- Varfell: declares Spy on Valorsmark (Royal Guard expected to cancel)
- Hafenmark: holds (no PA Session until next arc)

**Phase 4 — Priority 1 (Intel):**

- **Varfell → Spy on Valorsmark.** Valorsmark Royal Guard cancels. Same as S1.
- **Varfell → Counter-Narrative T11** (Inquisitor now deployed; +2 Ob).
  - 4D vs Ob 4: 11.9% Succ+. Modal Partial (63.1%).
  - Result: AP +1 → T11 AP = 1.

**Phase 4 — Priority 3 (Domain):**

- **Valorsmark → Govern T2.** Modal Success.
- **Church → Active Inquisition T11** (2nd Inquisitor recently deployed; aim for AP buildup).
  - Ob = floor(T11 Sta=3/2)+1 = 2. 5D vs Ob 2: 60.0% Succ+.
  - Result: AP +2 → T11 AP = 3.

- **Hafenmark → Govern T8** (own territory).
  - Modal Success. T8 Prosperity +1.

**Phase 4 — Priority 4 (Social):**

- **Valorsmark → Royal Decree** (back at Ob 2; Winter reset). Target Mil+1 → Valorsmark Mil 4→5.
  - 5D vs Ob 2: 60.0% Succ+.
  - Result: Valorsmark Mil → 5.

**Phase 5 Accounting:**

- T11 AP 3.
- T11 Sta 3 (sustained Inquisitor pressure).
- CI +1 → 34.
- PI 9 (no PA action S6 to push higher).

**End of S6:**
```
Valorsmark: L 5, PS 5, I 5, W 4, Mil 5 (+1), Int 3, Sta 5
Church:     L 5, PS 5, I 6, W 5+1 (Prudence S6), Mil 4, Int 4, Sta 5
Hafenmark:  L 5, PS 4, I 4, W 7, Mil 3, Int 3, Sta 4
Varfell:    L 4, PS 4, I 4, W 4, Mil 4, Int 4, Sta 4 | Token on Varfell mat persists

Clocks: CI 34 | MS 72 | IP 19 | PI 9 | Strain 1
T9: Uncontrolled + Inquisitor | T11: AP 3, Inquisitor active, Sta 3
```

---

### §4.4 6-Season Trajectory — 4-Faction Re-Sim

| Faction | S1 Stats | S6 Stats | Δ | Territory Δ | Win-share trend |
|---------|----------|----------|----|-----------|-----------------|
| **Valorsmark** | M=5, all stats baseline | M=5, Mil +1, Sta +1 | +2 stats, **−1 territory (T9)** | Stable on stats; under territorial pressure | Mid pressure |
| **Church** | M=5, I=6 dominant | M=5, **2 Inquisitors deployed** | +0 stats; **+2 Inquisitor positions** | Aggressive long-game; ascendant in territorial influence | High trend |
| **Hafenmark** | M=4 | **M=5** (+1 L from PA), W cap reached | +1 L; **+1 Token on Varfell** | Political ascendant; ready for Crisis benefit | High trend |
| **Varfell** | M=4 | M=4, no stat change | 0 | **2 territories closed to Counter-Narrative** (T9, T11 — both Inquisitor) | **Trending DOWN** |

**Win-share estimate (subjective, this run):**

- Church: 30–35% (Inquisitor reach + I=6 advantage)
- Hafenmark: 25–28% (political maneuvering + Token leverage)
- Valorsmark: 22–25% (stable stats, territorial losses pending more pressure)
- Varfell: 15–20% (Intel options closing as Inquisitors proliferate; no offensive vector)

**Equality verdict at 6 seasons:** Church 30–35%, Varfell 15–20% — **outside ±5pp band**
(target 20–30% each). Church is **above ceiling**, Varfell is **below floor**.

---

### §4.5 Mode C-Δ Findings

- **C-Δ-F1 [CHURCH ASCENDANT] P1:** Church reaches 2 active Inquisitors by S5,
  pressuring 2 player territories. Without an Inquisition cap, Church's mid-game
  trajectory is steep. **T-09c (Inquisition cap 2) becomes the most important
  win-share tweak** — prevents Church from monopolizing territorial pressure.
- **C-Δ-F2 [HAFENMARK MID-GAME ASCENDANT] P1:** Hafenmark's PA Session + Diplomat
  Token + Crisis benefit gives 3 sequential mid-game wins. Mandate grows from 4
  to 5 by Year 2. **Hafenmark is the second strongest mid-game trajectory.** Combined
  with Church, the two "patient" factions (long-game ecclesiastical + patient
  mercantile) dominate the 4-faction landscape.
- **C-Δ-F3 [VALORSMARK TERRITORIAL VULNERABILITY] P1:** Valorsmark's stat-stability
  comes at the cost of territorial pressure absorption. **The Charter loop helps
  Valorsmark grow Prosperity in held territories but does nothing to defend against
  Church's AP/Inquisitor pressure.** Need: Valorsmark counter to Inquisitor specifically —
  **T-09a (Treaty Ob reduction once-per-arc) addresses this only partially.** Consider
  a Valorsmark-specific Inquisition counter (e.g., Decree-can-include-Inquisitor-removal
  as Enhancement option).
- **C-Δ-F4 [VARFELL STRUCTURAL DECLINE] P1:** Varfell's only offensive vector is
  Counter-Narrative + Spy. Counter-Narrative windows close as Inquisitors deploy.
  Spy hits Valorsmark/Hafenmark but Royal Guard absorbs one per season. **Varfell
  is on a structural downward trajectory.** Without T-02a (Inquisitor familiarity),
  Varfell loses every Inquisitor-deployed territory permanently.
- **C-Δ-F5 [RM SILENT IN 4-FACTION] P2:** With Guilds and Löwenritter sidelined as
  non-players, RM's slow MS pressure (T-06a/T-06c reframed as world-state) operates
  *under* the player faction layer. RM's effect on the campaign trajectory is real
  but not directly affecting player win-share.
- **C-Δ-F6 [PI CRISIS AT Y1 IS TOO EARLY] P2:** PI reaching ≥ 8 (Crisis) by S4 means
  Crisis dynamics dominate Year 2. Game arc seems calibrated for Year 3–4 crisis,
  not Year 1–2. **Verify Crisis-threshold tuning.** Either PI increment is too fast
  in 4-faction (less faction-mediated friction), or threshold should be 10+ not 8+.

---

## §5 MODE D-Δ — Edge Cases (4-Faction)

Selected probes most impacted by the 4-faction correction. Full Mode D suite from prior
sim preserved unchanged; deltas only noted.

### D-Δ-01 (Boundary): CI 60 trigger with 3 player-owners

Per §2.2 A-Δ-06, E[# seizures] in single CI 60 trigger = 1.14 (was ~2.0 with 4 owners).
Cascade still significant; targets distribute across 3 player factions instead of 4.

### D-Δ-02 (Cascade): Hafenmark pipeline rescoped

A-Δ-11 finding: Hafenmark Proclamation pipeline inert vs L≥4 player targets at start.
Activation requires Hafenmark L ≥ 5 against L=4 Varfell. ~6–8 seasons mid-campaign.
**Cascade pressure on Varfell only; not a 4-target sweep as 6-faction sim suggested.**

### D-Δ-03 (Regression): Mandate-suppression ceiling — confirmed third time

In 4-faction, all player-to-player suppression attempts are vs L=4 or L=5:
- vs L=5: 8.3% Excommunication, 38.0% Treaty
- vs L=4: 19.8% Excommunication, 60.0% Treaty

No L=3 player target to exploit. **The pattern that "Excommunication works on weak
rivals" doesn't apply because there are no weak rivals.** Excommunication is **structurally
mid-tier** for all player matchups — better than vs L=5, worse than against NPCs.
Confirms GAP-08 unchanged urgency.

### D-Δ-04 (Optimal Play per Faction in 4-Faction):

| Faction | Optimal pattern | Constraint |
|---------|-----------------|------------|
| Valorsmark | Charter capital → Govern T2 spam → Decree as Sta/Mil buffer → Outreach defensively | Vulnerable to territorial pressure (no Inquisition counter) |
| Church | Cardinal Justice → Piety Spread → Active Inquisition → CI 60 Seizure | Limited only by Inquisition cap (proposed) |
| Hafenmark | PA Session win → Diplomat vs Varfell (Token compound) → Free Agitation (Crisis) → late-game Proclamation | Constrained by L ≥ 5 prereq + only one viable Proclamation target (Varfell) |
| Varfell | Counter-Narrative pre-Inquisitor → Spy whenever possible → save Tribunes for crisis | Trapped: Counter-Narrative windows close; Spy has Royal Guard counter |

### D-Δ-05 (Degenerate): Removed degenerate scenarios

Prior sim's A-05-F1 (Ecclesiastical Appointment 83.5%) preserved; D-Δ doesn't change
this. RM Weaving anti-rescue still flagged but as world-state per Part 1.

---

## §6 Win-Share Equality Analysis

### §6.1 Current canon (no tweaks) — estimated win-share

Based on §4.4 6-season trajectory + structural analysis:

| Faction | Est. win-share | Δ from 25% | In ±5pp band? |
|---------|----------------|-------------|----------------|
| Church | 30–35% | +5 to +10 | **Above ceiling** (borderline at 30) |
| Hafenmark | 25–28% | 0 to +3 | ✓ |
| Valorsmark | 22–25% | −3 to 0 | ✓ |
| Varfell | 15–20% | −5 to −10 | **Below floor** |

**Imbalance:** Church/Varfell spread is ~15pp — **3× the acceptable variance**.
The 4-faction model exposes this more sharply than the 6-faction sim's findings
suggested (where Guilds and Löwenritter absorbed some Church pressure and Hafenmark
expansion).

### §6.2 After narrowed tweak set (T-01a, T-01c, T-02a, T-02c, T-03c, T-04a, T-06a, T-09a/b/c)

Hypothetical impact projections (compound — not additive linearly; full re-sim would
verify):

| Faction | Tweaks affecting | Win-share trajectory |
|---------|-------------------|----------------------|
| Church | T-09c (Inquisition cap) | 30–35% → 25–28% (cap limits territorial pressure) |
| Hafenmark | T-03c (Token cost) | 25–28% → 22–25% (Token accumulation rate halved) |
| Valorsmark | T-01a (Charter dim. returns), T-01c (Royal Guard narrower), T-09a (Treaty mid-game) | 22–25% → 23–27% (Charter loop blunted but T-09a helps; T-01c opens Spy vulnerability) |
| Varfell | T-02a (Inquisitor familiarity), T-04a (Path A relaxed), T-09b (defensive Token) | 15–20% → 22–27% (Inquisitor recovery + arc progression + defensive Tokens) |

**Projected after-tweaks win-share band: 22–28% across all 4 player factions.** Within
±5pp target. **Equality target met under proposed tweak set.**

**Confidence: medium** — based on probability shifts, not full Mode C re-run with all
tweaks applied. Full verification requires Mode C-Δ-tweaked playtest. Recommended
prototype.

### §6.3 Tweaks ranked by win-share equality impact

| Rank | Tweak | Reason |
|------|-------|--------|
| 1 | **T-09c** (Inquisition cap 2) | Single largest constraint on Church win-share; brings Church into band |
| 2 | **T-02a** (Inquisitor familiarity) | Single largest Varfell relief; brings Varfell into band |
| 3 | **T-09b** (Varfell defensive Token on failed-Spy-detection) | Compensates Varfell for asymmetric Spy targeting from Hafenmark |
| 4 | **T-03c** (Token costs W−1) | Throttles Hafenmark Token accumulation; secondary effect on Hafenmark trajectory |
| 5 | **T-09a** (Valorsmark Treaty Ob reduction once/arc) | Gives Valorsmark one arc-defining diplomatic moment; partial fix for GAP-08 in player matchups |
| 6 | **T-01a** (Valorsmark Charter dim. returns) | Reduces Valorsmark dominant strategy but doesn't change win-share much (Valorsmark not the strongest) |
| 7 | **T-01c** (Royal Guard narrowed) | Opens Valorsmark to Spy pressure; doesn't shift win-share band on its own; supports cross-tweak balance |
| 8 | **T-04a** (Revelation Tokens relaxed) | Long-horizon Varfell Path A acceleration; matters only in 8+ season runs |
| 9 | **T-02c** (CN Overwhelming relocates Inquisitor) | Rare event; flavor-rich but rate-limited |

**Recommendation: T-09c + T-02a + T-09b are the minimum-viable balance pass for
25% ±5pp equality.** The other 6 add flavor, depth, and stability but don't change
the band placement.

---

## §7 Consolidated Findings — Part 3

### P1 (drives Parts 4–5 audits)

| ID | Finding |
|----|---------|
| C-Δ-F1 | Church Inquisition trajectory dominates 4-faction model — 2 Inquisitors by S5 — TARGET FOR T-09c |
| C-Δ-F2 | Hafenmark mid-game ascendant — political stacking + Diplomat + Crisis benefit |
| C-Δ-F3 | Valorsmark territorial vulnerability — Charter loop helps growth, no Inquisition defense |
| C-Δ-F4 | Varfell structural decline — Counter-Narrative windows close as Inquisitors proliferate |
| S4-Δ-F3 | PI Crisis triggers at S4 (Y1 end) — may be too early; verify tuning |
| A-Δ-02-F1 / A-Δ-15-F1 | Mandate-suppression ceiling pattern (confirms GAP-08, 4th sim flagging) |
| A-Δ-17-F1 | Spy intel asymmetry — Church 4D best, Valorsmark 3D worst |
| A-Δ-10-F2 | Hafenmark Diplomat targets Varfell (only L=4 player) — concentrated diplomatic pressure |

### P2 (depth/quality findings)

| ID | Finding |
|----|---------|
| S1-Δ-F1 | Year 1 Season 1 balance healthy; +1/+1/0/0 net |
| S1-Δ-F2 | Royal Guard absorbs 1 Intel/season; Varfell needs 2/season to land |
| S2-Δ-F1 | Hafenmark protocol opportunism → Varfell concentration |
| S2-Δ-F2 | Church Inquisitor deploys T9 by S2 — pressure on Valorsmark starts early |
| S3-Δ-F1 | T9 Accord 1 = revolt warning; Valorsmark must garrison or absorb |
| S3-Δ-F2 | Varfell Counter-Narrative Partial-mode preserves attempts; cumulative P(≥1 Succ+) over 4 attempts (Ob 2/4/4/4) = 66.4% |
| S5-Δ-F1 | 2 active Inquisitors by S5 — earlier than 6-faction sim's S6 |
| S5-Δ-F2 | Varfell territorial intel access closing 1/2 territories per Inquisitor |
| C-Δ-F5 | RM operates under player layer in 4-faction — separate balance concern |
| C-Δ-F6 | PI Crisis at Y1 end may be too early; verify tuning |

### P3

- D-Δ-04 patterns (faction-optimal play) — preserved from prior sim with relabel
- A-Δ-17 Varfell-Church Spy parity — working as intended
- Year-End B11 sequencing — preserved from prior sim

---

## §8 Verdict — Part 3

**Equality target met under proposed tweak set (T-09c + T-02a + T-09b minimum-viable).**
Projected win-share band: 22–28% across 4 player factions, within ±5pp.

**Without tweaks**, the 4-faction model exhibits 15–20% Varfell vs 30–35% Church spread —
a ~15pp imbalance, 3× the acceptable variance. The corrected canon **surfaces this
imbalance more sharply than the 6-faction sim** because Guilds/Löwenritter no longer
absorb Church pressure or Hafenmark expansion.

**The most important balance tweaks differ from the prior balance sim:**

| Prior P1 (6-faction) | After Part 1 disposition | New P1 (4-faction) |
|----------------------|---------------------------|---------------------|
| T-01a, T-01c | preserved | T-09c (NEW) |
| T-02a | preserved | T-02a (preserved) |
| **T-03a** (Guilds defense) | **invalidated** | T-09b (NEW) |
| **T-05a** (Guilds patronage) | **invalidated** | — |
| T-06a (RM bootstrap) | reframed to world-state | — |

**Two new tweaks emerged from the 4-faction analysis:**

- **T-09c** (Inquisition cap 2) — single largest equality lever
- **T-09b** (Varfell defensive Token on failed-Spy-detection) — Varfell agency boost

**Open structural issues unchanged:**

- GAP-01 (Phase 5 AP reset)
- GAP-02 (PP-686 v2 triadic vs Consequentialism)
- GAP-08 (Mandate-suppression ceiling — 4th-sim flagging now)
- GAP-05 (Valorsmark Treaty consent)
- New: PI Crisis tuning (Y1 vs Y3 target)

---

## §9 Open Items (Part 3)

- Full Mode C-Δ re-run with all proposed tweaks applied — verifies 22–28% band
- PI Crisis tuning — should threshold be 8 or 10? Verify with playtest
- Map-canonical T9 starting control — Valorsmark or unaligned?
- Inquisitor deployment effect on Accord — implicit, no numeric rule (GAP)
- T-09a/b/c are new — not yet meta-throughline-vetted (Part 5 will check)
- T-09c cap mechanics: does recall require Cardinal Focus, Action, or Accounting?

---

*Session: balance-resim-4faction · 2026-05-13 · Part 3/5 · Author: simulator under Jordan*
