# Stress Test — Negotiations, Alliances, Treaties
## Session: 2026-04-09 | Modes: A + D + J + L
## Scope: BG and Hybrid modes only
## Sources: bg_v05, params_board_game.md v0.9.1, victory_architecture_v1.md, params_factions.md v0.15

---

## FETCH LOG
- canonical_sources.yaml: ✓ 154 lines
- designs/board_game/valoria_bg_v05_simulation_and_patches.md: ✓ 734 lines
- references/params_board_game.md: ✓ 1541 lines
- designs/board_game/victory_architecture_v1.md: ✓ 460 lines
- canon/02_canon_constraints.md: ✓ 25 lines
- references/params_factions.md: ✓ 565 lines
- skills/valoria-simulator/SKILL.md: ✓ 199 lines

---

## SYSTEM INVENTORY

| Mechanic | Source | Mode |
|----------|--------|------|
| Diplomacy vs NPC (Senator Outward) | params_board_game.md L114 | BG + Hybrid |
| Diplomacy between players (negotiated) | params_board_game.md L115 | BG + Hybrid |
| Formal Crown Treaty | victory_architecture_v1.md §3.1, PP-423 | BG + Hybrid |
| Hafenmark Diplomat Card | params_board_game.md §Hafenmark, ED-320 | BG + Hybrid |
| Hafenmark Diplomatic Token | params_board_game.md L1254 | BG + Hybrid |
| Coalition Suppression Bonus | params_board_game.md §PP-296 | BG + Hybrid |
| Canonical Coalition Pairs | params_factions.md §PP-405 | BG + Hybrid |
| Missed Coalition Opportunity Penalty | params_board_game.md §PP-404 | BG + Hybrid |
| Casus Belli (treaty-derived) | bg_v05 §I-03, PP-14 | BG + Hybrid |
| Treaty Betrayal Consequences | bg_v05 B7 | BG + Hybrid |
| Co-Victory Pairings | victory_architecture_v1.md §4 | BG + Hybrid |
| Thread Liaison | params_board_game.md PP-436 | BG + Hybrid |
| Crown Diplomatic Outreach to Schoenland | params_board_game.md PP-437 | BG + Hybrid |
| Allied Definition | params_board_game.md L1287 | BG + Hybrid |
| Diplomatic Token interaction (Parliamentary) | params_board_game.md PP-320-ED | BG + Hybrid |

---

## MODE A — SINGLE MECHANIC ISOLATION

### A-01 — Formal Crown Treaty

**Probability Table (Crown Inf 5, Monte Carlo 100k):**

| Target Mandate | Ob | P(Overwhelming) | P(Success) | P(Partial) | P(Failure) |
|---------------|-----|----------------|------------|------------|------------|
| 1 | 1 | 60% | 20% | 13% | 7% |
| 2 | 2 | 38% | 22% | 20% | 20% |
| 3 | 3 | 20% | 18% | 22% | 40% |
| 4 | 4 | 8% | 11% | 18% | 62% |
| 5 | 5 | 3% | 5% | 11% | 80% |

**A-01-F1 [DEGENERATE] P1:** Crown Treaty Ob = target Mandate. Against any faction at Mandate ≥ 3: 80%+ failure rate. Crown victory requires every rival at Mandate ≤ 2 OR eliminated OR Treaty — but Treaty Ob = their Mandate. A faction strong enough to matter is a faction too strong to Treaty. Circularity defeats the mechanic.

**A-01-F2 [AMBIGUITY] P1:** "Both factions must agree" — consent has no mechanical structure. No incentive table, no NPC AI rule, no refusal consequence. In competitive play: no opponent will consent (Treaty costs them Mandate −1). Treaty path is unilaterally vetoed.

**A-01-F3 [AMBIGUITY] P2:** Treaty dissolution asymmetric. Crown breaking costs Stability −2, Mandate −1. Target faction breaking (via Domain Action vs Crown) triggers no consequence — only stated dissolution trigger for target is Mandate reaching 0.

---

### A-02 — Hafenmark Diplomat Card

**Probability Table (Hafenmark Inf 5, Ob = ceil(Mandate/2)):**

| Target Mandate | Ob | P(success+) |
|---------------|-----|------------|
| 1–2 | 1 | ~80% |
| 3–4 | 2 | ~60% |
| 5–6 | 3 | ~38% |
| 7 | 4 | ~20% |

**A-02-F1 [AMBIGUITY] P2:** Diplomatic Token removal condition "military conflict with Hafenmark" undefined. Does March (Legionary without battle) count? Does a declared battle that is then avoided count? No alignment with Conflict Marker definition (PP-479).

**A-02-F2 [DESIGN NOTE] P3:** Odd/even Mandate pairs share Ob — no defect, intentional stair-step.

---

### A-03 — Coalition Suppression Bonus (PP-296)

**Probability Table (Primary pool 4D, Ob = min(target Mandate, 4)):**

| Factions | Pool | Ob 1 | Ob 2 | Ob 3 | Ob 4 |
|----------|------|------|------|------|------|
| 1 | 4D | 75% | 51% | 28% | 12% |
| 2 | 6D | 83% | 67% | 47% | 28% |
| 3 | 8D | 89% | 77% | 62% | 44% |
| 4+ | 10D | 92% | 84% | 72% | 57% |

**A-03-F1 [OPTIMAL PLAY] P2:** Coalition suppression is dominant strategy. "No formal pact declaration required" makes it cost-free. Late-game = all non-leaders pile on the leader automatically. Reduces political texture.

**A-03-F2 [AMBIGUITY] P2:** "Valid suppression action" undefined. Does a Tribune Investigate that has Mandate reduction as secondary effect count? Only explicit Mandate-targeting cards?

---

### A-04 — Casus Belli (treaty-derived)

**A-04-F1 [CASCADE] P2:** No cap on simultaneous CB holdings. A serial treaty-breaker accumulates permanent CB vs all factions. No stacking rule stated.

**A-04-F2 [AMBIGUITY] P2:** CB use/consumption not stated in treaty context. One-use? Persistent? Consumed on declaration or on roll?

---

### A-05 — Player-to-Player Diplomacy

**A-05-F1 [STRUCTURAL GAP] P1:** "Negotiated — not a roll." Full diplomatic layer between player factions is purely social with zero mechanical enforcement. No Pledge system. No betrayal consequence for non-Treaty agreements. Undeclared design choice.

---

## MODE D — EDGE CASE DISCOVERY

**D-01 [BOUNDARY] P2:** Treaty vs Mandate-0 target: Ob = 0 → floor Ob 1 per correction. Treaty signed; dissolution condition (Mandate = 0) fires immediately. Signs and dissolves in same step.

**D-02 [BOUNDARY] P3:** Diplomatic Token on Mandate-0 faction: Token grants Parliamentary Support but collapsed faction cannot participate. Suspension rule absent.

**D-03 [BOUNDARY] P3:** Missed coalition penalty: "above" vs "at or above" coalition floor — ambiguous.

**D-04 [CASCADE] CLEAN:** Crown Treaty signed at Accounting + victory check: 2-Accounting holding requirement absorbs this correctly. No defect.

**D-05 [CASCADE] P2:** Diplomatic Token + Parliamentary Manoeuvre + Coalition Suppression: Token Support ≠ Domain Action. Secondary suppressor bonus requires a played Domain Action — Parliamentary vote does not qualify. No cascade, but needs explicit documentation.

**D-06 [CASCADE] P2:** Thread Liaison dissolution timing: retroactive vs prospective not stated. Operations already credited same season should remain valid.

**D-07 [DEADLOCK] P1:** Crown Treaty path vetoed: all opponents can refuse consent. No mechanical appeal. Crown must eliminate or suppress — Treaty path is inaccessible in competitive play.

**D-08 [DEADLOCK/DESIGN] P1:** No non-Crown binding agreement mechanism. Crown-exclusive diplomatic structure. Either intentional (Crown's constitutional role) or unexamined gap — either way must be declared.

**D-09 [REGRESSION] CLEAN:** Treaty Mandate −1 accelerating target collapse — intended political tension, not a defect.

**D-10 [REGRESSION] P3:** Diplomatic Token on a Crown Treaty partner: Token redundant (Allied status now structural). Token should be removed on Treaty formation.

**D-11 [AMBIGUITY] P2:** "Allied definition" OR conditions too broad. Same-side Parliamentary voter = Allied for Thread Liaison purposes? One shared vote creates Liaison eligibility — too easily triggered.

**D-12 [INCOHERENCE] P1:** Coalition Pairs table references "Guilds" and "Niflhel" — neither is a canonical faction. Economic Bloc and Restoration Compact are inoperable. Table is stale.

**D-13 [AMBIGUITY] P2:** Trade-Mandate Pact requires Hafenmark Influence ≥ 6, starts at 4. No defined Influence growth mechanism. May never be triggerable.

**D-14 [CRUNCH] P2:** Treaty betrayal consequence chain hits Cascade Depth Cap exactly at 3. If CB is immediately usable (4th effect), cap violated.

**D-15 [INCOHERENCE] P2:** Simultaneous solo + co-victory conditions: no priority rule for declaring faction.

**D-16 [OPTIMAL PLAY] CLEAN:** Hafenmark Diplomat correctly rewards targeting strong factions. No defect.

**D-17 [OPTIMAL PLAY] P1:** Crown Treaty negative expected value vs all alternatives at Mandate ≥ 3. Confirms A-01-F1.

---

## MODE J — PRECEDENT COMPARISON

**J-01:** Valoria's player-player diplomacy matches Root (pure social). Crown Treaty most analogous to TI4's Diplomacy card but with a roll where TI4's is guaranteed. Lag behind Here I Stand in structural clarity (no offer format, no secret agreements).

**J-02:** Games running pure social contract (Diplomacy, Root) succeed because betrayal IS the drama. Valoria sits awkwardly between models: Crown has structure (broken), others have none. Recommend: implement light Pledge system (Open/Closed), as referenced but never defined in bg_v05.

---

## MODE L — COGNITIVE LOAD

**L-01 [LOAD 7/10]:** Crown Treaty resolution: no timing declaration, no degree table, no consent order, no stated effect on partial success. Cannot be run without GM intervention.

**L-02 [LOAD 5/10]:** Coalition suppression: automatic trigger reduces table load but "valid suppression action" ambiguity creates disputes.

**L-03 [LOAD 6/10]:** Coalition Pairs: fog-of-war sub-game + Missed Coalition flag. Manageable but only 2 of 4 pairs operable (D-12).

**L-04 [LOAD 8/10]:** Hybrid personal-scene alliance → BG Treaty: no bridge rule. Every instance requires GM adjudication.

---

## FINDINGS SUMMARY

| ID | Sev | Description |
|----|-----|-------------|
| A-01-F1 | P1 | Crown Treaty Ob = target Mandate → inaccessible vs strong factions |
| A-01-F2 | P1 | Consent mechanism undefined |
| A-01-F3 | P2 | Treaty dissolution asymmetric — target-break unpenalized |
| A-02-F1 | P2 | "Military conflict" removal condition for Token undefined |
| A-03-F1 | P2 | Coalition suppression dominant strategy; no declaration cost |
| A-03-F2 | P2 | "Valid suppression action" undefined |
| A-04-F1 | P2 | Treaty CB: no stacking cap |
| A-04-F2 | P2 | CB use/consumption rule absent |
| A-05-F1 | P1 | Non-Crown diplomacy: pure social, undeclared design choice |
| D-01 | P2 | Treaty vs Mandate-0: signs and dissolves instantly |
| D-05 | P2 | Token Support ≠ Domain Action for coalition suppression |
| D-06 | P2 | Thread Liaison dissolution timing unstated |
| D-07 | P1 | Crown Treaty path deadlocked by unanimous refusal |
| D-08 | P1 | No non-Crown binding instrument — Crown-exclusive |
| D-11 | P2 | Allied definition OR conditions too broad for Thread Liaison |
| D-12 | P1 | Coalition Pairs references non-existent factions (Guilds, Niflhel) |
| D-13 | P2 | Trade-Mandate Pact threshold potentially unreachable |
| D-14 | P2 | Treaty betrayal chain may exceed Cascade Depth Cap |
| D-15 | P2 | Simultaneous solo + co-victory: no priority rule |
| D-02 | P3 | Token on Mandate-0 faction: suspension absent |
| D-03 | P3 | Missed coalition penalty: "above" vs "at or above" |
| D-10 | P3 | Token redundant on Treaty partner |

**P1 total: 7 | P2 total: 13 | P3 total: 3**

---

## EDITORIAL FLAGS (for ED assignment)

| Flag | Description | Priority |
|------|-------------|----------|
| ED-a | Confirm: is player-player diplomacy intentionally pure social? If yes, document. If no, define Pledge system. | P1 |
| ED-b | Crown Treaty consent design: incentive table, NPC AI consent rule, refusal consequence. | P1 |
| ED-c | Coalition Pairs audit: remove Guilds/Niflhel, redesign for canonical faction list. | P1 |
| ED-d | Thread Liaison "allied" scope: Treaty-only or all three OR conditions. | P2 |

---

## SIM-DEBT

| ID | Description |
|----|-------------|
| SIM-DIPL-01 | Multi-season Crown diplomatic path with revised Treaty Ob |
| SIM-DIPL-02 | Coalition trigger rates across 20-season campaign |
| SIM-DIPL-03 | Hybrid personal-scene alliance → BG Treaty bridge |
