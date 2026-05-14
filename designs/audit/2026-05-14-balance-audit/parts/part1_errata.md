# Errata — Prior Faction Sims (2026-05-13 sessions)
## Date: 2026-05-13 · Session: errata-and-corrections · Status: ARCHIVE
## Companion docs:
- `sim_faction_cards_stress_2026-05-13.md` (PRIOR — superseded in part)
- `sim_faction_balance_proposals_2026-05-13.md` (PRIOR — superseded in part)
## Authority: `designs/provincial/faction_state_authoring_v30.md` §§2–7 (CANONICAL, PP-686 v2 Phase B Stage 5)

---

## §1 Purpose

This memo corrects two structural errors in the prior same-day sims and triages every
finding against the canonical 4-faction model. Future work — granular log schema (Part 2),
4-faction balance re-sim (Part 3), NERS audit (Part 4), throughline audit (Part 5) —
proceeds from this corrected baseline.

---

## §2 Canonical Verification

Index map read this session:

- `references/canonical_sources.yaml` (registry, 389 lines, 17 full-stack systems mapped + supporting param specs)
- `references/file_index_summary.md` (handoff pointer)
- `references/valoria_canonical_definitive_r2.md` (canonical reference)
- `references/mechanical_terms_index.md` (mechanical glossary, 132k chars)
- `references/throughline_registry.md` (T1–T41 + N1–N6, CANONICAL 2026-04-18)
- `references/throughlines_meta.md` (vetting framework, PP-674)

Canonical faction-architecture sources confirmed:

| Source | Status | Faction list |
|--------|--------|--------------|
| `designs/provincial/faction_state_authoring_v30.md` | **CANONICAL** | §2 Crown · §3 Church of Solmund · §4 Hafenmark · §5 Varfell · §6 Restoration Movement · §7 Löwenritter |
| `designs/provincial/faction_canon_v30.md` | PROVISIONAL Stage 1 | Crown + Church sheets present; Hafenmark + Varfell pending Stage 2/3 |
| `designs/provincial/faction_behavior_v30.md` | CANONICAL | PP-686 v2 four-component model + §3.7 triadic Ob decomposition |
| `params/factions/stats_1_7_scale.md` | CANONICAL | 7-stat schema (L · PS · I · W · Mil · Int · Sta), post-ED-787 |

---

## §3 Canonical Faction Set at Game Start

**Four player factions** (Jordan-confirmed 2026-05-13, matches `faction_state_authoring_v30 §§2–5`):

| Canonical name | Game name | Role | Status |
|----------------|-----------|------|--------|
| Crown | **Valorsmark** | Sovereign | Player |
| Church of Solmund | Church | Ecclesiastical | Player |
| Hafenmark | Hafenmark | Mercantile-Procedural | Player |
| Varfell | Varfell | Military-Order | Player |

**Two non-player factions** (canonical §§6–7):

| Canonical name | Role | Status |
|----------------|------|--------|
| Restoration Movement | Reformist | Background actor (no Stability per PP-460; world-state pressure) |
| Löwenritter | Military-Order | NPC with graduated autonomy (per `conflict_architecture_proposal` 2026-04-18) |

**Win-rate target:** 25% per player faction, ±5pp band (20–30%) across N campaigns, with
asymmetric paths to victory preserved per faction identity. Tight equality (±2pp) would
flatten the asymmetry that defines the design; loose equality (±10pp) wouldn't constrain
the work meaningfully. ±5pp is the operating tolerance.

---

## §4 Naming-Migration Status: Crown → Valorsmark

Status: **rename in progress; canonical docs still use "Crown".**

| Doc | Reference count |
|-----|-----------------|
| `faction_state_authoring_v30.md` | "Crown" 15× / "Valorsmark" 0× |
| `faction_canon_v30.md` (Stage 1 PROVISIONAL) | "Crown" 52× / "Valorsmark" 0× |
| Prior sims (this date) | "Crown" used throughout |

**Disposition for this errata and forward:** use **Valorsmark** in all new sim/audit
output; treat "Crown" in canonical docs as the same faction. When canonical docs are
updated, this errata's mapping becomes the audit trail for the rename.

`[ED-NEW: Crown → Valorsmark rename propagation pending. Canonical faction architecture
docs (state_authoring, canon, behavior) still use "Crown" exclusively. Sim output
2026-05-13 forward uses "Valorsmark". Editorial pass needed.]`

---

## §5 Disposition Rules

Three rule classes determine how prior findings carry forward:

**Rule R-1 — RELABEL.** Any finding referring to "Crown" remains valid in mechanical
substance; replace "Crown" with "Valorsmark" in citation. Mechanical content unchanged.

**Rule R-2 — INVALIDATE.** Any finding specific to "Guilds" as a player faction is
invalidated. Guilds is not in `faction_state_authoring_v30` as a player faction. Prior
sims fabricated a Guilds player-faction with stats (L=3, PS=3, I=4, W=6, Mil=2, Int=4,
Sta=5) and a Trade-only action profile. Source for these stats: unknown — they appear
to conflate Hafenmark's mercantile sub-organizations (per `faction_canon §10
Sub-Organization Layers`) with a separate faction. **All Guilds-specific findings,
tweak proposals (T-03b, T-05a, T-05b, T-05c), and Mode C scenario participation
deleted from the model.**

**Rule R-3 — REFRAME.** Findings about Restoration Movement and Löwenritter remain
useful as world-state and NPC behavior observations; reframe from "player faction
balance" to "background actor health" or "NPC reactive behavior." These no longer count
toward the 25% win-share equality target.

---

## §6 Disposition Catalog — Mode A (Single-Mechanic Probability)

| Card | Faction | Disposition | Notes |
|------|---------|-------------|-------|
| A-01 Royal Decree | Crown | **R-1 Relabel** | Probability findings (consecutive-Ob curve 60% → 38% → 19.8% → 8.3%) preserved verbatim |
| A-02 Excommunication | Church | **PARTIAL R-2** | vs L=5/4 rows preserved; vs L=3 row deleted (no L=3 player faction at game start); Löwenritter L=3 reframes as NPC target (Church can still excommunicate NPC institutions but it's not a player-balance concern) |
| A-03 Piety Spread | Church | Preserved | Mechanical surface unchanged |
| A-04 Active Inquisition | Church | Preserved | |
| A-05 Ecclesiastical Appointment | Church | Preserved | A-05-F1 P1 finding (83.5% Succ+ degenerate gate) still valid |
| A-06 CI 60 Seizure | Church | **PARTIAL R-2** | vs L=3 row deleted (no L=3 player target); vs Löwenritter L=3 reframes as NPC-territory seizure; cascade-finding A-06-F3 preserved with target-pool reduced from 4 to 3 |
| A-07 Royal Charter | Crown | **R-1 Relabel** | Charter-loop finding A-07-F1 preserved as **Valorsmark Charter loop** |
| A-08 Outreach to Schoenland | Crown | **R-1 Relabel** | |
| A-09 Parliamentary Challenge | Hafenmark | Preserved | |
| A-10 Diplomat Card | Hafenmark | **PARTIAL R-2** | vs L=3 rows deleted from player-target set; pipeline target list reduces to: Valorsmark (L=5), Church (L=5), Varfell (L=4). Löwenritter L=3 NPC target retained for NPC-flavor moves. |
| A-11 Dynastic Proclamation | Hafenmark | **R-2 + SIGNIFICANT BALANCE SHIFT** | Prereq: Haf L > target L AND Haf L ≥ 4 AND adjacent. Under 4-faction canon, no player target has L < 4 at start. **Pipeline is mechanically inert against player factions at game start.** This sharply diminishes A-11-F1 P1 finding ("60%+ territory transfer at Sta 2 targets, Guilds defenseless") — Guilds doesn't exist; the only valid targets (Varfell L=4) require Haf to reach L=5 first. **A-11 reframes as a mid-game expansion mechanic, not an early-game pipeline.** Pipeline P1 finding **downgraded to P2** with new framing. |
| A-12 Counter-Narrative | Varfell | Preserved | Inquisitor-lockout finding A-12-F1 unchanged |
| A-13 Community Weaving | RM | **R-3 Reframe** | RM bootstrap deadlock now framed as world-state actor's progression problem, not player balance. Still important; less urgent. |
| A-14 Martial Governance | Löwenritter | **R-3 Reframe** | NPC behavior pattern; not player balance |
| A-15 Formal Crown Treaty | Crown | **R-1 Relabel + PARTIAL R-2** | Now Valorsmark Treaty. vs L=3 row deleted from player set; finding A-15-F1 P1 (Treaty Ob = target L, ceiling pattern) preserved against player targets L=4–5 |
| A-16 Diplomacy vs NPC | All | Preserved | |
| A-17 Spy | All | Preserved | A-17-F2 (Valorsmark Int 3 most vulnerable) preserved with relabel |
| A-18 Govern | All | Preserved | |
| A-19 Trade | All | Preserved | |
| A-20 Suppress | Crown/Hafenmark | **R-1 Relabel** | Now Valorsmark/Hafenmark |

---

## §7 Disposition Catalog — Mode C (6-Season Scenario)

The Mode C scenario was built around 5 player factions + RM + Löwenritter. Under
correction it becomes **4 player factions + RM (world actor) + Löwenritter (NPC)**.

| Finding | Disposition | Reason |
|---------|-------------|--------|
| S1-F1 (Decree +1 Sta worked) | **R-1 Relabel** | Valid as Valorsmark |
| S1-F2 (Guilds W cap S1) | **R-2 Invalidate** | No Guilds player; finding does not apply |
| S2-F1 (Piety Spread AP vs Inquisitor distinction) | Preserved | Mechanical, faction-agnostic |
| S2-F2 (Decree consec penalty bit harder) | **R-1 Relabel** | |
| S3-F1 (Inquisitor ramp tight) | Preserved | Mechanical |
| S4-F1 P1 (Phase 5 step 5 AP reset vs PP-185 — GAP-01) | Preserved | Mechanical; remains highest-urgency editorial item |
| S4-F2 (PA Session + Token works clean) | Preserved | Hafenmark mechanism |
| S4-F3 (Hafenmark ascendant M=5 by S4) | **PARTIAL R-2** | Vote was 3 Support / 1 Oppose / 1 Abstain — recount under 4-faction: Vote is Valorsmark, Church, Hafenmark, Varfell only (4 voters). Guilds-Support recount: drops one Support. Recompute Vote at 2-1-1 or 2-2 under 4-faction; Session-pass outcome may differ. **Mode C scenario needs full re-run in Part 3.** |
| S5-F1 (Haf protocol picks Varfell over Token-holder Guilds) | **R-2 Invalidate** | Guilds doesn't exist; finding moot |
| S5-F2 (Crown Charter stack works) | **R-1 Relabel** | Valorsmark Charter stack |
| S6-F1 P1 (T9 revolt cascade) | Preserved | Mechanical |
| S6-F2 (Haf CB+Legionary risky) | Preserved | Hafenmark mechanism |
| S6-F3 (Church Prominent in Varfell territory) | Preserved | Mechanical |
| **C-F1** (trajectory healthy, no runaway) | **PARTIAL R-2** | 6-season run included Guilds player; without it, fragmentation pace likely faster (one fewer faction defending territories). Re-run needed. |
| C-F2 (protocol artifacts produce suboptimal mechanical choices) | Preserved | Faction-agnostic observation |
| **C-F3 P2 (Guilds passive, W-cap)** | **R-2 Invalidate** | |
| **C-F4 P2 (Crown unmolested 6 seasons)** | **R-1 Relabel + REASSESS** | Becomes "Valorsmark unmolested." Under 4-faction with active Hafenmark + Varfell + Church (no Guilds passive buffer), pressure dynamics differ. **Reassess in Part 3.** |
| C-F5 (Intel restoration practical impact) | Preserved | |
| **C-F6 P1 (RM bootstrap deadlock)** | **R-3 Reframe** | Reframed as: "world-state actor RM has bootstrap-impossible progression; this affects MS trajectory and emergent narrative, not player win-share equality." Still urgent for world-state coherence; **drops from player-balance P1 to world-state P1.** |

---

## §8 Disposition Catalog — Mode D (Edge Cases)

| Probe | Disposition |
|-------|-------------|
| D-01-01 (CI thresholds) | Preserved |
| D-01-02 (MS death spiral, RM Weaving 3.8%/14.2%) | **R-3 Reframe** — world-state concern |
| D-01-03 (IP threshold) | **R-1 Relabel** (Valorsmark Outreach) |
| D-02-01 P1 (Hafenmark Token+Proclamation pipeline) | **R-2 SIGNIFICANT** — pipeline-against-Guilds finding invalidated; pipeline at game start is mechanically inert vs all player targets per A-11 disposition. Finding becomes: "pipeline activates mid-game once Haf reaches L≥5 against Varfell only" — much weaker concern. **Drops from P1 to P3.** |
| D-02-02 P1 (CI 60 multi-territory cascade) | **PARTIAL R-2** — recalculate E[# seizures] with player-territory pool reduced from 4 owners (L 3,4,5,5) to 3 owners (L 4,5,5). E[# seizures] drops slightly. Cascade-cascade finding preserved. |
| D-02-03 (Charter loop) | **R-1 Relabel** (Valorsmark loop) |
| D-03-01 P1 (Mandate-suppression ceiling regression) | Preserved — three-sim confirmed regression; **still highest-priority GAP-08**. Note: target set under 4-faction reduces to 3 (instead of 5), still showing same ceiling against L=5/4 players. |
| D-03-02 P1 (Crown Treaty consent gap) | **R-1 Relabel** — Valorsmark Treaty consent gap, preserved |
| D-03-03 P1 (PP-686 v2 triadic vs Consequentialism) | Preserved — mechanical-canonical question |
| D-04-01 (Deadlock probes) | Preserved |
| D-05-02 (Year-End B11 sequencing) | Preserved |
| D-06-01–D-06-03 (Ambiguity probes) | Preserved |
| D-07-01 (Hafenmark pipeline P-08 check) | **R-2 SIGNIFICANT** — under corrected canon, pipeline doesn't trigger early game; P-08 compliance even cleaner. **Finding strengthened (more clearly P-08 compliant).** |
| D-07-02 (Charter loop P-15 check) | **R-1 Relabel** |
| D-08-01–05 (Optimal strategies per faction) | **R-2 PARTIAL** — D-08-05 Guilds-optimal invalidated; D-08-01 Crown→Valorsmark; rest preserved |
| D-09-01–04 (Degenerate cases) | Preserved with relabel |

---

## §9 Disposition Catalog — Tweak Proposals

14 tweaks proposed in balance sim. Disposition:

**P1 originally — kept after correction:**

| ID | Status | Notes |
|----|--------|-------|
| T-01a (Valorsmark Charter diminishing returns) | **R-1 Relabel; PRESERVE** | Was Crown; otherwise unchanged |
| T-01c (Royal Guard cancels passive Intel only) | **R-1 Relabel; PRESERVE** | Was Crown |
| T-02a (Inquisitor +2 Ob first-attempt only) | **PRESERVE** | Varfell-side; unchanged |
| **T-03a (Institutional Mandate gate L≥3)** | **R-2 INVALIDATE — RECONSIDER** | Original purpose: protect Guilds (L=3) and Löwenritter (L=3) from Proclamation. Guilds isn't a player. Löwenritter is NPC. **Under 4-faction, no player has L<4 at start — PP-189 L≥4 gate already covers all players.** Tweak unnecessary. *However:* if Hafenmark L grows to 5+ mid-campaign and Varfell stays at L=4, A-11 pipeline activates against Varfell. PP-189 L≥4 gate works for Varfell. **No tweak needed.** T-03a deleted from recommendation set. |
| **T-05a (Guilds Patronage W→stat conversion)** | **R-2 INVALIDATE** | Guilds isn't a player |
| T-06a (RM starts with 2 Presence) | **R-3 REFRAME** | Was P1 player-balance fix; now P1 world-state fix (RM remains the world-state actor whose progression affects MS trajectory) |

**P2 originally — disposition:**

| ID | Status | Notes |
|----|--------|-------|
| T-01b (Charter exclusivity) | **R-1 Relabel; PRESERVE** | |
| T-02c (CN Overwhelming relocates Inquisitor) | PRESERVE | |
| **T-03b (Guilds W-3 cancel)** | **R-2 INVALIDATE** | Guilds isn't a player |
| T-03c (Token cost W−1) | PRESERVE | Hafenmark mechanism, still valid |
| T-04a (Revelation Tokens relaxed) | PRESERVE | Varfell |
| **T-05b (Guilds Mercenary contract)** | **R-2 INVALIDATE** | |
| **T-05c (Guilds Banking)** | **R-2 INVALIDATE** | |
| T-06c (RM Organising 2D base) | **R-3 REFRAME** as world-state tweak |

**P3 deferred:**

| ID | Status |
|----|--------|
| T-02b (Recall Operative) | PRESERVE deferred |
| T-04b (Tribune Disinformation) | PRESERVE deferred |

**Final tweak set after correction (Player-balance + World-state):**

Player-balance (5 tweaks): T-01a, T-01b (alternative), T-01c, T-02a, T-02c, T-03c, T-04a  
*Plus 2 deferred: T-02b, T-04b*

World-state (2 tweaks): T-06a OR T-06c

**Removed: T-03a, T-03b, T-05a, T-05b, T-05c** (all five were Guilds-specific, invalidated)

This is a **substantial change** to the balance recommendation set: 4 of the original 6
P1 tweaks were Crown/Guilds-related. After correction:
- 2 P1 tweaks remain as P1 (T-01a, T-02a)
- 2 P1 tweaks promoted to remain P1 but relabeled to Valorsmark (T-01c, T-06a-world-state)
- 1 P1 tweak deleted (T-03a — Guilds-defense, unnecessary under 4-faction)
- 1 P1 tweak deleted (T-05a — Guilds-progression, unnecessary)

**Net effect:** the corrected baseline has **fewer tweaks but a much clearer balance
picture** — the 4 player factions are closer to parity than the 6-faction model
suggested, because Guilds and Löwenritter no longer create the asymmetric vulnerabilities
that drove T-03a/T-05a.

---

## §10 Updated Starting State (4-Faction Canonical)

Per `params/factions/stats_1_7_scale.md` (post-ED-787, Intel restored as canonical):

| Faction | L | PS | M\* | I | W | Mil | Int | Sta |
|---------|---|----|----|---|---|-----|-----|-----|
| **Valorsmark** | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 4 |
| **Church** | 5 | 5 | 5 | 6 | 5 | 4 | 4 | 5 |
| **Hafenmark** | 4 | 4 | 4 | 4 | 5 | 3 | 3 | 4 |
| **Varfell** | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |

*M = round(0.5 × L + 0.5 × PS) per `faction_behavior_v30 §4`*

Background actors (no player win-share):

| Actor | Notes |
|-------|-------|
| **Restoration Movement** | No Stability (PP-460); world-state pressure via Presence markers + Community Weaving on MS track |
| **Löwenritter** | NPC with graduated autonomy; Mil 5 / I 2 / Sta 5 reactive behavior per `peninsular_strain_v30 §2.6` |

**Clocks (BG start):** CI 28 · MS 72 · IP 20 · PI 5

**Win-rate target:** 25% per player faction, ±5pp band (operating 20–30% across N campaigns).

---

## §11 P1 Findings After Correction — Final List

The P1 findings that **drive Parts 3–5** (re-sim, NERS audit, throughline audit):

| ID | Finding | Affects |
|----|---------|---------|
| A-02-F1 / A-15-F1 / D-03-01 | Mandate-suppression ceiling (Ob = target stat): Excommunication/Treaty/Proclamation under-perform against parity. Under 4-faction at game start, ALL player-to-player attempts are against L=4 or L=5, all sitting in the 8.3%–22.5% Success+ band. | Inter-player balance |
| A-05-F1 | Ecclesiastical Appointment 83.5% Succ+; gate does all the work | Church accumulation rate |
| A-10-F1+F2 | Hafenmark Diplomat → Token pipeline (now applies only against Valorsmark/Church/Varfell — 3 viable targets, all L≥4 with Mandate defense available) | Hafenmark soft-power |
| A-12-F1 | Inquisitor +2 Ob locks Varfell out of Counter-Narrative | Varfell agency |
| S4-F1 / D-06-02 | Phase 5 step 5 AP reset vs PP-185 per-territory tracking | Editorial gap, blocks balance work |
| S6-F1 | Territory revolt cascade in 4 seasons | Mechanical, working as intended but fast |
| D-03-01 (regression) | Mandate-suppression ceiling: flagged in 3+ sims, unfixed | Editorial decision required |
| D-03-02 (regression) | Crown(Valorsmark) Treaty consent gap | Editorial decision required |
| D-03-03 | PP-686 v2 triadic vs Consequentialism overlap ambiguity | Editorial clarification |
| C-F6 (REFRAMED) | RM bootstrap deadlock — world-state coherence, not player balance | World-state |

**Net change vs prior sim:** previous 18 P1 findings → after correction, **10 P1 findings**.
Five P1 findings invalidated (Guilds-related); three reframed to world-state (RM/Löwenritter);
two preserved with relabel.

---

## §12 Editorial Gap Identified

`[ED-NEW]` While reading `faction_canon_v30.md` (PROVISIONAL Stage 1), found this
phrasing in §1:

> "Does not author missing substrate-postures (Crown / Church / Varfell / Guilds —
> all four are flagged `[GAP — Phase B]`)."

This lists "Guilds" where `faction_state_authoring_v30 §4` has "Hafenmark." Likely a
documentation slip — Hafenmark is the mercantile-procedural player; Guilds is not a
canonical player faction per state_authoring (CANONICAL); only sub-organizations
within `faction_canon §10 Sub-Organization Layers` mention guilds.

**Recommended editorial:** correct `faction_canon_v30.md §1` substrate-posture gap
list from "Crown / Church / Varfell / Guilds" to "Crown / Church / Hafenmark / Varfell"
to match canonical state_authoring. Until that lands, `faction_state_authoring_v30`
remains authoritative.

---

## §13 What Carries Forward

After this errata, the work going forward (Parts 2–5) uses:

- **4 player factions:** Valorsmark, Church, Hafenmark, Varfell — each targeting 25% win-share ±5pp
- **2 background actors:** RM (world-state pressure), Löwenritter (NPC reactive)
- **No Guilds** as a player faction
- **Probability engine:** validated, no rebuild needed
- **Probability tables:** Mode A master grid preserved; per-card tables relabeled
- **Tweak set:** narrowed to 5 player-balance tweaks + 2 world-state tweaks + 2 deferred
- **Open editorial gaps:** GAP-01 (AP reset), GAP-02 (triadic/Conseq overlap), GAP-08 (Mandate-suppression ceiling, 3+ sim regression), GAP-05 (Treaty consent), GAP-09 (RM curve)
- **Authoritative sources:** `faction_state_authoring_v30` (CANONICAL), `faction_behavior_v30` (CANONICAL §3.7), `params/factions/stats_1_7_scale.md` (CANONICAL post-ED-787), `params/contest.md` (canonical social_debate per index)

---

## §14 Part Pipeline

| Part | Status | Deliverable |
|------|--------|-------------|
| 1 — Errata | **this doc** ← complete | |
| 2 — Granular Log Schema | next | Forward-only structured log format for design decisions, sim runs, audit outcomes |
| 3 — 4-Faction Balance Re-Sim | after Part 2 | Mode A/C/D under corrected canon; 25% ±5pp targeting |
| 4 — NERS Audit | after Part 3 | N · E · R · S × 6 directions against corrected tweak set |
| 5 — Throughline + Meta-Throughline Audit | after Part 4 | T1–T41/N1–N6 mapping; PP-674 vetting protocol applied |

---

*Session: errata-and-corrections · 2026-05-13 · Part 1/5 · Author: simulator under Jordan*
