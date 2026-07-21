# VALORIA — Silo Cohesion & Naming Convention Analysis
**Date:** 2026-05-08
**Scope:** Granular pass with all session corrections applied
**Context:** Combat + Mass Combat merged. Peninsular Strain → Turmoil. Conviction Track split → Persuasion Track (contest) / Piety Track (territory). Initiative (contest) → First to Speak. Authority (Pressure Point) → Sanction.

---

## §A — REVISED SILO TAXONOMY (15 silos)

| Silo | What it owns | Change from v1 |
|------|-------------|----------------|
| §1 | Character attributes (what a person *is*) | — |
| §2 | Faction attributes (what a faction *is*) | — |
| §3 | Territory attributes (what a territory *is*) | — |
| §4 | World / cosmological state (EXEMPT from silo rules) | — |
| §5 | **Combat (all scales)** | MERGED: absorbed §10 Mass Combat |
| §6 | Social Contest (Debate) | Persuasion Track, First to Speak |
| §7 | Threadwork (EXEMPT from silo rules) | — |
| §8 | Fieldwork (Exploration / Investigation / Socializing / Exposure) | — |
| §9 | **Piety & Church Influence** | RENAMED from "Conviction Track" |
| ~~§10~~ | ~~Mass Combat~~ | MERGED into §5 |
| §11 | Faction Layer / Domain Actions | — |
| §12 | Clocks (meta — cross-references, not owns) | — |
| §13 | Tensions Deck / Assassination / Special | — |
| §14 | Victory Paths | — |
| §15 | Scale-bridging (EXEMPT — bridge mechanics) | — |
| §16A | Dice Engine (system-agnostic primitives) | SPLIT from §16 |
| §16B | Authoring / Infrastructure (meta — not in-game) | SPLIT from §16 |

---

## §B — CROSS-SILO CONTAMINATION (post-corrections)

### B.1 Remaining violations

| Term | Appears in | Problem | Recommendation |
|------|-----------|---------|----------------|
| **Cover (derived)** | §1 (listed as character property) AND §8 (fieldwork §6.1 source) | Cover is a fieldwork mechanic output, not a character attribute. It's computed from terrain + position, not from the character sheet. | **Move to §8 Fieldwork.** Remove from §1.2. |
| **"Conviction Track"** (89 files) | Corpus-wide residual | Deprecated. Contest → Persuasion Track. Territory → Piety Track. | **Corpus sweep in progress.** |
| **"Initiative"** (contest residual) | Infill/v2 files | Renamed to "First to Speak" in canonical docs; residuals in secondary files. | **Sweep secondary files.** |

### B.2 Cross-references that are NOT contamination

These terms appear in multiple silos as *references* to their owning silo. This is correct.

| Term | Owns | Referenced from | Why clean |
|------|------|----------------|-----------|
| Accord | §3 territory | §14 victory | Victory evaluates the territory attribute |
| Provincial Value (PV) | §3 territory | §14 victory | Same pattern |
| Composure | §1 character | §6 debate | Debate attacks the character's Composure stat |
| Domain Echo | §15 scale-bridging | §6, §11 | Bridge mechanic referenced from endpoints |
| CI (Church Influence) | §9 piety/CI | §12 clocks | Clock silo catalogs all clocks |
| Stability | §2 faction | §12 clocks | Same pattern |

---

## §C — NAMING CONVENTION ISSUES (within silos)

### C.1 §1 Character Attributes

| Issue | Severity | Detail |
|-------|----------|--------|
| **"Memory" dual use** | MEDIUM | "Memory (score)" = stat capping History entries. "Memory entry" = per-NPC Key reference. Same root word, two different things within §1. Disambiguation: rename the score to **"Recall"** or **"Retention"**? Or rename the per-NPC item to **"Key Reference"** (what it actually is)? |
| **§1.7 legacy labels** | LOW | Legacy/superseded character labels duplicated here AND in §6-deprecated. Remove from §1; single home in §6-deprecated. |
| **Cover in §1** | MEDIUM | Doesn't belong — see §B.1. Move to §8. |

### C.2 §2 Faction Attributes

| Issue | Severity | Detail |
|-------|----------|--------|
| **"Faction Pool / Political Pool" residual** | LOW | Two names still appear in the index entry (§2.2). Collapse to **Political Pool** only. |
| **Faction roster (§2.3) is entity data, not attributes** | LOW | The seven factions are entities. Consider moving to a "Factions" reference section separate from faction *attributes*. Low urgency — organizational, not mechanical. |

### C.3 §3 Territory Attributes

| Issue | Severity | Detail |
|-------|----------|--------|
| **CRITICAL: Territory name discrepancies** | **P1** | victory_v30 uses stale territory names (Falkenberg, Steinfeld, Mittelmark...) while canonical docs (conviction_track_v30, settlement_layer_v30, 80+ files) use current names (Kronmark, Lowenskyst, Grauwald...). **13 of 17 territories mismatch.** |
| **"Peninsular Strain" → "Turmoil"** | MEDIUM | Rename needed corpus-wide. Resolves PS abbreviation collision with Public Support. |

Mismatched territory names (conviction_track_v30 = CANONICAL, victory_v30 = STALE):

| T# | Canonical | Stale (victory_v30) |
|----|-----------|---------------------|
| T2 | Kronmark | Falkenberg |
| T3 | Lowenskyst | Steinfeld |
| T4 | Grauwald | Mittelmark |
| T5 | Feldmark | Weissburg |
| T6 | Stillhelm | Sonnental |
| T7 | Rendstad | Grauheim |
| T10 | Spartfell | Nordmark |
| T11 | Halvardshelm | Eisengrund |
| T13 | Oastad | Southernmost |
| T14 | Ehrenfeld | Hafenfeld |
| T15 | Southernmost | Kronheim |
| T16 | Schoenland | Bergstadt |
| T17 | Halvarshelm | Drakensholm |

### C.4 §5 Combat (merged with Mass Combat)

| Issue | Severity | Detail |
|-------|----------|--------|
| **Health vs Vitality ambiguity** | MEDIUM | §1 defines Health = Endurance (universal character stat). §5 says Vitality replaces Health in combat context (ED-548/694). But "Health per Size" (mass combat) uses "Health" not "Vitality." Within the merged silo: personal-scale uses Vitality, unit-scale uses Health-per-Size. Different words for conceptually similar things at different scales. Suggest: **"Unit Health"** for mass-combat to distinguish from personal Health, or align both to Vitality. |
| **Scale qualifier consistency** | LOW | Personal-scale actions are bare verbs (Attack, Defend). Mass-scale uses compound terms (Formation Type, Battle Turn Structure, Cascade Phase). The vocabulary is scale-separated but the pattern isn't explicit. Consider: personal = bare verb, unit = compound noun. Already natural; just document the convention. |

### C.5 §6 Social Contest (Debate)

| Issue | Severity | Detail |
|-------|----------|--------|
| **Genre labels inconsistency** | MEDIUM | §6.2 says "Genre: Past · Present · Future." But params/contest.md Step 2 says "Choose genre (Memory/Projection)." These are different label sets for the same concept. The *axis* is temporal (past/present/future), but the *player choices* are Memory and Projection. **Clarify:** Genre has three values on the axis but two player choices? Or are Memory = Past, Projection = Future, and Present is... implicit? |
| **"Orientation: Revealing / Obscuring"** | — | Clean and unique. No issue. |
| **"Grand Debate"** | LOW | Uses "Debate" in name when system is officially "Contest." The term is canonical and distinct enough. Minor aesthetic. |

### C.6 §8 Fieldwork

| Issue | Severity | Detail |
|-------|----------|--------|
| **"Sincerity Gate" appears in §8.4 AND §8.5** | LOW | Listed in Investigation (§8.4) and Socializing (§8.5). Both are fieldwork sub-modes, so within the same silo. But it's defined in two places — pick one and cross-reference. |

### C.7 §9 Piety & Church Influence

| Issue | Severity | Detail |
|-------|----------|--------|
| **Silo name** | HIGH | Was "Conviction Track" — must be renamed. Canonical track is now "Piety Track (PT)." Silo should be **"§9 — Piety & Church Influence"** or **"§9 — Orthodoxy Mechanics."** |
| **§9.3 heading still says "TC"** | LOW | "TC Generation" heading in conviction_track_v30 not yet updated to "CI Generation." |

### C.8 §12 Clocks

| Issue | Severity | Detail |
|-------|----------|--------|
| **Pseudo-clocks blur silo boundary** | LOW | §12.3 lists Stability, Standing, Public Support, Legitimacy as "pseudo-clocks." These are faction attributes (§2), not clocks. They're tracked numerically but so are all stats. **Recommendation:** remove pseudo-clocks from §12; they're already in §2. §12 should only list dedicated clock mechanics (MS, TT, CI, IP, PI, Turmoil, PT, Cooldown). |

### C.9 §16 Split: Dice Engine vs Authoring

| Issue | Severity | Detail |
|-------|----------|--------|
| **Two unrelated categories** | MEDIUM | Dice engine (TN, Ob, Pool, Degrees) and authoring infrastructure (Patch, ED, SIM, Class A/B, Throughline) are completely different. Split into §16A (Dice Engine) and §16B (Authoring). |

---

## §D — ACRONYM AUDIT (post-corrections)

### D.1 Resolved collisions
| Acronym | Was | Now |
|---------|-----|-----|
| PS | Peninsular Strain AND Public Support | **Turmoil** (no abbrev or Tu) — PS freed for Public Support |
| CT | Conviction Track (contest AND territory) | Deprecated. Persuasion Track (no abbrev) + PT (Piety Track) |
| CV | Conviction Track (legacy) | Deprecated → PT |

### D.2 Remaining clean abbreviations
| Abbr | Term | Silo | Unique? |
|------|------|------|---------|
| MS | Mending Stability | §4/§12 | ✓ |
| TT | Thread Tension | §4/§12 | ✓ |
| CI | Church Influence | §9/§12 | ✓ |
| IP | Institutional Pressure | §12 | ✓ |
| PI | Public Instability | §12 | ✓ |
| PT | Piety Track | §3/§9 | ✓ |
| PV | Provincial Value | §3 | ✓ |
| TS | Thread Sensitivity | §1/§7 | ✓ |
| TPS | Thread Pool Score | §1/§7 | ✓ |
| DR | Damage Resistance | §5 | ✓ (merged silo) |
| CP | Character Points | §1 | ✓ |
| CE | Combat Endurance | §5 | ✓ |
| TN | Target Number | §16A | ✓ |
| Ob | Obstacle | §16A | ✓ |
| EV | Expected Value | §16A | ✓ |
| PP | Patch | §16B | ✓ |
| ED | Editorial Decision | §16B | ✓ |
| PS | Public Support | §2 | ✓ (now unique) |

### D.3 Table-only abbreviations (acceptable per naming rule)
M, I, W, Mil, Int, Sta (faction stats — never standalone in prose)
H (Health per Size — mass combat tables only)
L (Legitimacy — table-only)

---

## §E — SILO COHESION THROUGHLINE CHECK

**Principle:** terms within a silo should connect through a common throughline — they describe the same domain from the same perspective.

| Silo | Throughline | Cohesion | Issues |
|------|-------------|----------|--------|
| §1 Character | "What a person carries on their sheet" | HIGH | Cover doesn't belong (move to §8). Memory dual-use. |
| §2 Faction | "What a faction carries on its ledger" | HIGH | Faction roster is entity data not attributes (minor). |
| §3 Territory | "What a territory carries on its card" | HIGH | **Territory names discrepancy is P1.** |
| §4 World | "What the world is doing" | HIGH | Exempt and coherent. |
| §5 Combat | "How violence resolves at any scale" | HIGH | Merged silo; personal and unit scales well-separated by vocabulary. |
| §6 Contest | "How rhetoric resolves" | HIGH | Genre label inconsistency (Past/Present/Future vs Memory/Projection). |
| §7 Threadwork | "How the substrate is manipulated" | HIGH | Exempt and coherent. |
| §8 Fieldwork | "How non-combat, non-debate, non-Thread interaction resolves" | MEDIUM | Four sub-modes are coherent; investigation's four systems are a silo-within-a-silo. |
| §9 Piety/CI | "How Church orthodoxy spreads and the Church wins" | HIGH | Silo name needs update. Otherwise coherent. |
| §11 Faction Layer | "What factions DO strategically" | HIGH | Coherent. |
| §12 Clocks | "All numerical tracks the world maintains" | MEDIUM | Pseudo-clocks (Stability, Standing) belong in §2, not here. |
| §13 Special | "Auxiliary strategic events" | MEDIUM | Small, catch-all. Löwenritter Graduated Autonomy might belong in §11. |
| §14 Victory | "How factions win" | HIGH | Cross-references §3 terms (correct). |
| §15 Scale-bridging | "How systems hand off to each other" | HIGH | Exempt and coherent. |
| §16A Dice Engine | "Universal resolution primitives" | HIGH | Split needed from §16B. |
| §16B Authoring | "Design process vocabulary" | HIGH | Split needed from §16A. |

---

## §F — PRIORITY ACTIONS

| # | Action | Severity | Scope |
|---|--------|----------|-------|
| 1 | **Fix territory names in victory_v30.md** (13 mismatches) | **P1** | 1 file, ~13 table rows |
| 2 | **Rename "Peninsular Strain" → "Turmoil"** corpus-wide | MEDIUM | ~30 files (TBD) |
| 3 | **Sweep "Conviction Track" → Piety Track or Persuasion Track** | MEDIUM | 87 files |
| 4 | **Move Cover from §1 to §8** | MEDIUM | Index update |
| 5 | **Resolve Memory dual-use** (score vs entry) | MEDIUM | Needs design decision |
| 6 | **Clarify Genre labels** (Past/Present/Future vs Memory/Projection) | MEDIUM | Needs design decision |
| 7 | **Remove pseudo-clocks from §12** | LOW | Index update |
| 8 | **Split §16 into Dice Engine + Authoring** | LOW | Index update |
| 9 | **Update §9 silo name** | LOW | Index update |
| 10 | **Collapse "Faction Pool / Political Pool" → Political Pool** in index | LOW | Index update |

[CONFIDENCE: high — systematic pass against all 15 silos; exemptions applied per Jordan's directive]
[GAP: Genre label inconsistency needs design verification from social_contest_v30 source — may be intentional axis-vs-choice distinction]
[GAP: Memory dual-use rename needs Jordan's decision on which term moves]
