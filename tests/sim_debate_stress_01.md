# SIM-DB-STRESS-01 — Social Contest System v2 Stress Test
## Modes: A (Isolation) + D (Edge Cases) + J (Cognitive Load) + L (Precedent)
## Date: 2026-04-09
## Source docs: designs/contest/social_contest_system_v2.md (404 lines), references/params_contest.md (242 lines)
## Canon: canon/02_canon_constraints.md

---

## FETCH LOG
- references/canonical_sources.yaml ✓ (154 lines)
- designs/contest/social_contest_system_v2.md ✓ (404 lines)
- references/params_contest.md ✓ (242 lines)
- canon/02_canon_constraints.md ✓ (25 lines)

---

## FINDINGS SUMMARY

| ID | Mode | Severity | Description | Action |
|----|------|----------|-------------|--------|
| D-04 | D | P1 | TIE/CROSS no-strain exception in design doc not reflected in params Interaction Types table | Params patch required |
| D-05 | D | P1 | OBSCURING WIN rule says "winning any exchange" — CROSS has no winner; conflicts with CROSS-specific Doubt Marker clause | Clarification patch required |
| L-05 | L | P1 | §11 Hybrid text + PP-256 clamp not cross-referenced; GM reading §11 alone would not know BG layer cannot fully resolve | §11 must cite PP-256 |
| D-03 | D | P2 | Resistance=2 equal-pool 3-exchange contest stalls all exchanges 37% of time → structurally biased toward Compromise; no design note confirms intent | Editorial candidate |
| D-01 | D | P2 | Att=1-2 orators: P(mislead) = 60%/36% per exchange; no floor or alternative path | Editorial candidate |
| D-07 | D | P2 | Doubt Marker "new replaces old" ambiguous: per-target or global? Two simultaneous markers (one on each orator) not addressed | Clarify rule text |
| D-08 | D | P2 | Regroup after Spent reset: additive over-restoration possible; Concentration has no stated ceiling | Params note |
| D-08b | D | P2 | Concentration has no explicit maximum/ceiling for restoration | Params note |
| D-09 | D | P2 | §9.3 Heresy Investigation: "Church may file" — no Ob, procedure, or timing defined | Cross-ref needed |
| J-01 | J | P2 | Audience resistance calculation requires averaging up to 6 faction Stability scores mid-scene; no simplified lookup | GM tool gap |
| J-02 | J | P2 | GM hidden ledger: ~12 tracked values, 40 sub-steps for Grand Contest; no reference card. Known gap (ED-055). | Carried |
| J-03 | J | P2 | 3v3 coalition Grand Contest: 15+ Composure/Rattled values + shared pools; significant tracking burden | Editorial candidate |
| L-01 | L | P2 | Appraise pool (Att only) vs Argue pool (Attr×2 + History): factor-of-4 gap for social specialists; no design note | Editorial candidate |
| L-04 | L | P2 | Belief-alignment Momentum earn cap (max 1/contest) unique across systems; asymmetry unexplained | Cross-system note |
| D-02 | D | P1 note | Pool=5 vs Pool=23: min-pool orator has near-zero CT movement; structural mismatch — previously identified | Confirms ED-330 |
| J-04 | J | P3 | Asymmetric proceedings: 3 concurrent rule overlays with no consolidated reference | GM tool gap |
| L-02 | L | P3 | Pool minimum 1D not re-stated in contest docs; implicit via core engine | Note for params |
| L-03 | L | P3 | Thread co-movement not a thread operation; P-01 does not apply | CLEAN |

**P1 new: 3 | P2 new: 9 | P3: 3 | CLEAN: 4 | Carried: 1 | Confirms prior: 1**

---

## MODE A — POOL ISOLATION

### Argue Pool

Pool = (Primary Attribute × 2) + History bonus. History bonus = skill points + 3 (per Stage 2 §4.1).
Adjudicator type selects Primary Attribute: Cognition (Expert Judge), Charisma (Crowd), Attunement (No Adjudicator).

| Bracket | Attr | History | Base Pool | E[successes] | P(2+ suc) |
|---------|------|---------|-----------|--------------|-----------|
| Minimum | 1 | 3 | 5 | 2.0 | 0.66 |
| Novice | 2 | 3 | 7 | 2.8 | 0.84 |
| Average | 3 | 5 | 11 | 4.4 | 0.97 |
| Skilled | 4 | 7 | 15 | 6.0 | 0.99 |
| Expert | 5 | 7 | 17 | 6.8 | ~1.00 |
| Master | 7 | 9 | 23 | 9.2 | ~1.00 |

With +2D genre/orientation bonus: min pool = 7, max pool = 25.

At pool=23+: P(0 successes) ≈ 0. Pool is effectively deterministic at master tier.

### Appraise Pool

Pool = Attunement only (no History), Ob 1, TN 7.

| Att | P(mislead) | P(partial) | P(full info) | P(overwhelming) |
|-----|------------|------------|--------------|-----------------|
| 1 | 0.60 | 0.40 | 0.00 | 0.00 |
| 2 | 0.36 | 0.48 | 0.16 | 0.00 |
| 3 | 0.22 | 0.43 | 0.35 | 0.06 |
| 4 | 0.13 | 0.35 | 0.52 | 0.18 |
| 5 | 0.08 | 0.26 | 0.66 | 0.32 |
| 7 | 0.03 | 0.13 | 0.84 | 0.58 |

Att=3 is the inflection point: first Att value where P(full info) > P(mislead). Characters below Att=3 should be expected to receive wrong signals more often than correct ones.

### CLASH CT Movement

Movement = margin − resistance (floor 0). Resistance 0–2.

| Pool A | Pool B | Resistance | P(move > 0) | P(stall) |
|--------|--------|------------|-------------|----------|
| 11 | 11 | 0 | 0.83 | 0.17 |
| 11 | 11 | 1 | 0.51 | 0.49 |
| 11 | 11 | 2 | 0.28 | 0.72 |
| 15 | 11 | 1 | 0.62 | 0.38 |
| 7 | 7 | 1 | 0.41 | 0.59 |
| 5 | 5 | 1 | 0.33 | 0.67 |

At resistance=2 with any equal-pool CLASH, stall is the most likely single outcome (P>0.65).

### Strain calibration

Composure = Charisma + 6 (range 7–13). Charisma modifier: max(0, floor((Cha−3)÷2)) → 0–2. Focus defence: floor(Foc÷2) → 0–3.

At average character (Cha=3, Foc=4): Cha_mod=0, Foc_def=2. Strain = max(0, margin − 2).
Margin=3 → strain=1. Margin=5 → strain=3.
Rattled after ~5 exchanges at avg strain=2 (Composure=9). A 5-exchange Grand Contest will typically produce Rattled on the losing orator.

### Concentration depletion

Typical range: Foc=3, Rec=2 → Conc=5. At −2/exchange (loss every time): Spent after 2 exchanges.
On a 5-exchange Grand Contest with 3 losses: Conc depletes to 5−7=−2 → Spent after 3rd loss.
Spent fires at end of that exchange, resets. Remaining exchanges: −2D penalty then reset again.

### CROSS movement

Effective margin = floor(successes ÷ 2). At average pools (11D each), resistance=1:
E[suc] = 4.4 → EM = 2. Net CT move = max(0, 2−1) − max(0, 2−1) = 0 for matched pools.
CROSS between equal orators produces near-zero CT movement in expectation. CROSS is primarily a Doubt Marker opportunity, not a track-movement tool for equal pools.

---

## MODE D — EDGE CASES

### D-04 [P1]: TIE/CROSS no-strain exception missing from params

**design_doc §4 TIE:** "Exception (PP-236): if the interaction type is CROSS, no strain is dealt."
**params_contest.md Interaction Types table, TIE row:** "1 each" — no CROSS exception listed.

A GM using only params applies TIE strain in all CROSS exchanges. This directly contradicts PP-236 and the design doc. Params table must be updated: TIE row should read "1 each (except: 0 in CROSS — PP-236)".

**Patch required (mechanical fix, no editorial needed).**

### D-05 [P1]: OBSCURING WIN scope vs CROSS exchanges undefined

OBSCURING WIN fires "when winning any exchange with Obscuring orientation." CROSS has no winner — each side moves the track independently. However, §4 CROSS contains a separate Doubt Marker clause: "if the side with larger movement used Obscuring, place a Doubt Marker on the opponent instead of track movement."

These are two separate rules both involving Obscuring wins:
1. OBSCURING WIN: fires on "winning any exchange" → undefined for CROSS
2. CROSS Doubt Marker clause: fires on "larger movement + Obscuring" in CROSS

As written, a GM could apply both (OBSCURING WIN replaces track movement, AND places Doubt Marker), or just the CROSS clause, or just OBSCURING WIN. The design doc intends only the CROSS clause applies in CROSS, but does not say so explicitly.

**Clarification patch required:** "OBSCURING WIN applies in CLASH and REINFORCE only. In CROSS, the Doubt Marker clause in §4 CROSS governs."

### L-05 [P1]: §11 Hybrid + PP-256 not cross-referenced

§11 base text describes a BG Parliamentary Vote running first, then TTRPG contest. If the BG layer reaches CT ≥ 7 or ≤ 3, Let It Ride (§1) would prevent the TTRPG layer from proceeding. PP-256 prevents this by clamping BG offset to ±2 (TC restricted to 4–6 at Hybrid session start), but §11 does not reference PP-256. A GM reading §11 does not know this clamp exists.

**Fix:** Add to §11 Step 1: "Note: BG lobbying offset is capped per PP-256; BG layer cannot produce a final resolution."

### D-03 [P2]: High-resistance contest structurally biased toward Compromise

At resistance=2, equal pools (Attr=3, pool≈11):
- P(stall per exchange) = 0.72
- P(all 3 exchanges stall in Formal Debate) = 37%
- P(all 5 exchanges stall in Grand Contest) = 19%

In a 3-exchange stall, CT remains at starting position (typically 5 = Compromise). The system produces Compromise as the modal outcome under high-resistance conditions regardless of orator skill.

This may be intended design — high-Stability audiences resist change. But no design note in §2 Step 4 or §4 states this explicitly. GMs cannot distinguish "designed stalemate tolerance" from a broken mechanic without this note.

**Recommend:** Add design note to §2 Step 4 audience resistance: "At resistance=2 with matched pools, Compromise is the modal outcome (~37% of 3-exchange contests resolve without CT movement). This reflects entrenched institutional audiences."

### D-01 [P2]: Low-Attunement Appraise systematic information failure

At Att=1: 60% mislead rate per exchange. Att=2: 36% mislead rate. These orators receive a wrong boost signal — choosing the faction's un-boosted axis — more often than they receive correct information. No alternative path (e.g., pre-contest Research replacing Appraise, or skipping Appraise at cost) exists.

A character with Att=1 is not just less effective at Appraise — they are actively misled 60% of the time, paying the genre/orientation penalty for wrong choices. This is a structural disadvantage beyond "lower bonus."

### D-07 [P2]: Doubt Marker mutual placement ambiguity

"Only one Doubt Marker active at a time. New replaces old." Does this mean:
(a) At most one Doubt Marker exists in the entire contest (replacing any existing one), or
(b) Each orator can have at most one on them (so two can coexist, one per orator)?

Reading (b) is correct per mechanical logic, but "one active at a time" implies (a). GMs will split on this. Rule text should read: "Each orator may have at most one active Doubt Marker placed on them. New Marker replaces any existing Marker on the same target."

### D-08 / D-08b [P2]: Concentration ceiling undefined

Regroup: "Concentration restores by Focus score." Spent: "pool resets to maximum." Both mechanics add to Concentration. No explicit ceiling is stated for Concentration. The formula gives a starting maximum (Focus + Recall), but §4 does not say restoration cannot exceed this value.

Design intent: Concentration max = Focus + Recall (derived). This should be explicit in §8 Derived Values.

---

## MODE J — COGNITIVE LOAD

### J-01 [P2]: Audience resistance calculation

Resistance = average Stability of represented factions (round up) − 1. In a multi-faction Parliament (4–6 factions), the GM must: look up 4–6 Stability values → sum → divide → round up → subtract 1. This is done mid-scene at contest setup.

No lookup shortcut or pre-calculated table. ED-055 (GM reference card) should include a pre-calculated resistance table for standard faction configurations.

### J-02 [P2 — carried, known]: GM hidden ledger load

12 tracked values per contest, 8 sub-steps per exchange. Grand Contest = 40 sub-steps minimum. ED-055 open. No new patch needed — confirm ED-055 scope covers this.

### J-03 [P2]: 3v3 coalition Grand Contest tracking

Per-member Composure (N values per side), per-member Rattled (N per side), shared Concentration (1 per side), initiative (1 value), lead nomination (per exchange), corroboration Ob (per exchange). For 3v3 Grand Contest: 12 Composure values + 12 Rattled values + 2 shared Concentration pools + initiative + lead + corroboration = ~30 tracked values at peak.

Exceeds comfortable GM working memory. Recommend a player-facing card for coalition contests.

---

## MODE L — PRECEDENT CONSISTENCY

### L-01 [P2]: Appraise-to-Argue pool ratio

A social specialist (Att=3, social History 3pts) has Argue pool = 12D but Appraise pool = 3D. Ratio 4:1. In combat, the analogue would be a fighter who attacks effectively but cannot perceive the field at all. The asymmetry is likely intentional (Appraise is a scout action, not a primary roll) but the gap is large enough that Att=1 characters are functionally excluded from useful Appraise even with high social Argue capability.

### L-04 [P2]: Belief Momentum cap asymmetry

§9.5 caps Belief-alignment Momentum earn at 1 per contest. No other system (combat, threadwork) imposes a per-action Momentum earn cap. Players earning Momentum via Belief in combat have no such cap. Cross-system inconsistency. May be intentional (social Momentum should be harder-earned) but should be noted.

### L-03, L-02 [P3, CLEAN]: No violations

Thread co-movement is not a thread operation; P-01 does not apply. Pool minimum 1D is core-engine universal; no restatement needed in contest docs.

---

## PATCHES REQUIRED (no editorial needed)

| Patch | Scope | Description |
|-------|-------|-------------|
| PP-NEW-A | params_contest.md | TIE row in Interaction Types table: add CROSS exception (no strain — PP-236) |
| PP-NEW-B | social_contest_system_v2.md §4 OBSCURING WIN | Scope to CLASH/REINFORCE only; state CROSS Doubt Marker clause governs in CROSS |
| PP-NEW-C | social_contest_system_v2.md §11 | Add PP-256 cross-reference: BG layer cannot produce final resolution |
| PP-NEW-D | social_contest_system_v2.md §8 | Add Concentration maximum = Focus + Recall to Derived Values table |

---

## EDITORIAL ITEMS RAISED

| ID | Priority | Description |
|----|----------|-------------|
| ED-NEW-A | P2 | High-resistance Compromise bias: add design note to §2 Step 4 confirming intended behaviour |
| ED-NEW-B | P2 | Low-Att Appraise systematic mislead: confirm no floor/alternative path is intended, or add one |
| ED-NEW-C | P2 | Doubt Marker per-target vs global: clarify rule text |
| ED-NEW-D | P2 | Appraise-to-Argue ratio: confirm intentional gap is acceptable |
| ED-NEW-E | P2 | Heresy Investigation trigger in §9.3: cross-ref or define procedure |
| ED-NEW-F | P2 | Belief Momentum cap (1/contest): confirm intentional asymmetry vs other systems |

---

## SIM-DEBT CLEARED

- SIM-DEBT-03: COMPLETE (prior sim). Mode A confirms pool baselines correct.
- SIM-DEBT-04: COMPLETE (prior sim). Mode A confirms adjudicator-type pool variation calibrated.

---

## PROPAGATION REQUIRED (if patches applied)

- references/params_contest.md: TIE row update (PP-NEW-A)
- designs/contest/social_contest_system_v2.md: §4, §8, §11 updates (PP-NEW-B, C, D)
- canon/editorial_ledger.yaml: ED-NEW-A through ED-NEW-F
- canon/patch_register.yaml: PP-NEW-A through PP-NEW-D
- tests/coverage_matrix.md: SIM-DB-STRESS-01 entry
