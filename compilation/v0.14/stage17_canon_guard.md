# Stage 17 — Canon Guard Pass
## Document: compilation/valoria_ttrpg_complete.md
## Date: 2026-03-26

---

## PART A: PRIORITY ISSUES (from session log flags)

### ISSUE 1 — §5.10 Header: "Taint Track"

**Section:** §5.10 header reads: `## 5.10 Transformation and Epistemic Seduction — Taint Track`

**Verdict:** PARTIAL FAIL (naming violation; philosophical framing is correct)

| Constraint | Status | Note |
|-----------|--------|------|
| P-10 | ⚠ | Header names "Taint Track" — implies moral corruption. Body text correctly frames as perceptual shift. |
| P-06 | ✓ | No Threadcut contamination; mechanic is separate |
| P-04 | ⚠ | "Taint" implies moral valence; body text contradicts header |

**Violation:** The header introduces the moral-corruption framing that the body explicitly rejects. "Taint" = corruption, impurity, defilement. The body correctly states: *"Transformation is a perceptual shift, not a corruption mechanic."* The canonical mechanic name is **Coherence Degradation (CD)** for the 0–20 track (§5.9). The §5.10 track is a separate mechanic without a canonical name in current text.

**Required repair:**
- Rename header to: `## 5.10 Transformation and Epistemic Seduction — Dissolution Track`
- All in-body references to "Taint" → "Dissolution level" or "DL"
- Retain the table as-is (0–10 scale); only naming changes required

**EDITORIAL NOTE:** The name "Dissolution Track" / "DL" is a mechanical proposal consistent with canon. If user prefers a different canonical name, flag before patching.
`[EDITORIAL: confirm "Dissolution Track / DL" as canonical name for §5.10 mechanic, or supply alternative]`

---

### ISSUE 2 — Leap Pool uses "Heart" (§5.2)

**Section:** §5.2 The Leap Roll, pool formula and Contact Duration

**Current text:**
- Leap pool: `Cognition + Heart + relevant History bonus`
- Contact Duration: `equal to the practitioner's Heart score`
- Wound disruption check: `Heart check immediately`

**Canonical attribute set (§2.1):** No "Heart" attribute exists. 10 attributes: Agility, Endurance, Strength, Cognition, Memory, Focus, Attunement, Bonds, Presence, Spirit.

**§2.3 Derived Scores note (line 188):** `Contact Rounds uses Focus (not Heart) because sustained Thread contact is an act of concentration, not willpower.`

This is a direct, authoritative resolution — the compiler already made the design call in §2.3.

**Verdict:** FAIL (broken reference — attribute does not exist in canonical set)

**Required repair:**

| Current | Replace with | Rationale (from §2.3) |
|---------|-------------|----------------------|
| `Cognition + Heart` (Leap pool) | `Cognition + Focus` | Focus = concentration; governs Thread contact |
| `Heart score` (Contact Duration) | `Focus score` | §2.3 explicit |
| `Heart check` (Wound disruption) | `Focus check` | Same attribute, same domain |
| `At Heart 2:` / `Heart 3 or more:` | `At Focus 2:` / `Focus 3 or more:` | Inline examples |

**Also in §5.5 Pulling pool (line 858):** `Cognition + Heart + Memory` → `Cognition + Focus + Memory`

No editorial gate required — §2.3 already resolved the design intent.

---

### ISSUE 3 — Composure Formula: Three Conflicting Versions

**This is the most structurally significant issue in the document.**

Three different formulas appear:

| Location | Formula | Attributes |
|----------|---------|-----------|
| §2.3 Derived Scores (line 181) | `Presence + 6` | Presence only; +6 constant |
| §4.11 Composure (line 633) | `Presence + Attunement` | Two canonical attributes |
| §9.1 Composure (line 2585) | `Poise + Heart` | Two non-canonical attributes |
| Glossary §16.1 (line 3933) | `Poise + Heart` with note `*(compiled ruleset uses Presence + Spirit — confirm)*` | Conflicted; three candidate formulas |
| NPC stat blocks §13.x | All use `Poise + Heart` (e.g., Almud: Poise 5 + Heart 4 = 9) | Non-canonical |

**Verdict:** FAIL — attribute names Poise and Heart do not exist in the canonical 10-attribute set. All instances using either must be repaired.

**Three candidate canonical formulas in play:**
1. `Presence + 6` (§2.3 — matches Health derivation pattern: Endurance + 6)
2. `Presence + Attunement` (§4.11)
3. `Presence + Spirit` (Glossary note)

`[EDITORIAL: select canonical Composure formula — three candidates:
(A) Presence + 6 (matches Health derivation pattern; range 7–13)
(B) Presence + Attunement (§4.11; socially intuitive; range 2–14)
(C) Presence + Spirit (Glossary note candidate; range 2–14)
NPC stat blocks all currently use non-canonical Poise + Heart values and will need recalculation once formula confirmed.]`

**Until resolved:** All Poise and Heart instances in Composure formulas are flagged as broken references.

---

### ISSUE 4 — Inspiration Cap uses "Heart" (§4.3, §10.3, §10.4)

**Current text (§4.3 line 357):** `Total Inspiration value ≤ Resolve (Spirit score)`
**Current text (§10.3 CP menu, line 2808):** `Total Inspiration value ≤ Heart score`
**Current text (§10.4, line 2829):** `Heart check TN 7, Ob 1`

**Verdict:** PARTIAL FAIL — §4.3 correctly uses Spirit/Resolve. §10.3 and §10.4 use Heart (non-canonical).

**Required repair:**

| Location | Current | Replace with |
|----------|---------|-------------|
| §10.3 CP menu (line 2808) | `≤ Heart score` | `≤ Spirit score (Resolve)` |
| §10.3 CP menu (line 2809) | `Individual cap = Heart score; total ≤ Heart` | `Individual cap = Spirit score; total ≤ Spirit` |
| §10.4 Inspiration acquisition (lines 2829, 2834, 2847) | `Heart check TN 7` | `Spirit check TN 7` |
| §4.3 (lines 369, 376, 381, 391) | `Heart check TN 7` | `Spirit check TN 7` (Resolve = Spirit) |

**Rationale:** §2.1 states Spirit governs `maximum Inspiration value`. §2.3 confirms `Resolve = Spirit`. §4.3 line 357 already uses this correctly. The §10 instances are cross-stage copy failures using the old attribute name.

No editorial gate — the design intent is unambiguous from §2.1 + §2.3 + §4.3.

---

## PART B: FULL DOCUMENT CANON CONSTRAINT SCAN

| Constraint | Status | Locations Checked | Notes |
|-----------|--------|------------------|-------|
| P-01 Inseparability co-movement | ✓ | §5.8, §12.6, Part 5 intro | §5.8 Three-Dimensional Co-Movement correctly implements mandatory secondary consequences across actual/temporal/epistemic |
| P-02 Ein Sof = fullness | ✓ | §5.9 CD thresholds, §5.13 Shifting Objects | Unintelligible ground framed as source of density/fullness, not void. No violations detected. |
| P-03 Rendering = consciousness | ✓ | §12.6 GM as Rendering Engine | Correctly positions GM as rendering engine. Information asymmetry mechanical via TS tiers (§5.2 visibility table). |
| P-04 Monstrosity = ontological, not moral | ⚠ | §5.13, §5.10 | §5.13 Shifting Objects correctly framed as rendering failures. §5.10 header "Taint Track" implies moral valence (see Issue 1 above). Body text correct; header violates. |
| P-05 Three modes mechanically distinct | ✓ | §5.13, §15 Spell Catalog | Modes 1/2/3 have distinct behaviours. §15.4 Operation Scale Reference distinguishes mode outcomes. |
| P-06 Threadcut = is without becoming | ✓ | §5.12 Thread-Locked Objects | Threadcut objects correctly mechanised as maintenance-requiring. No Taint contamination in this section. |
| P-07 Calamity = rendered-side | ✓ | §5.1–5.5, TT system | TT framed as over-drawing by practitioners, not ground responsiveness. §14.5 Three-Clock Feedback Loop correct. |
| P-08 Epistemic barrier = inaccessibility | ✓ | §4.4 Devout Constraint, §13.2 Himlensendt | Church framed as reinforcing inaccessibility, not causing it. Devout Constraint correctly mechanised as TS-blocking without implying suppression. |
| P-09 Memory pull = messy/costly | ✓ | §5.6 Past-Oriented Pulling | High Ob, produces orphaned configurations, detectable. Correctly implemented. |
| P-10 Epistemic seduction = perceptual shift | ⚠ | §5.10 | Body text correct. Header "Taint Track" violates (see Issue 1). |
| P-11 TD universal | ✓ | §5.8 Co-Movement, §12.7 TD Campaign Arc | All Thread operations produce TD per §5.8. Not restricted to Past-Pulls. |
| P-12 Relational contagion | ✓ | §4.7 Knots, §5.10 Taint 4–6 | Taint 4–6: GM recontextualises one Knot. Transforming practitioner's shift propagates through Knot system. |
| P-13 Forgetting = rendering failure | ✓ | §4.4 TS gating, §4.5 Intelligibility | Southernmost knowledge mechanically untransmittable below TS threshold. Intelligibility countdown correctly mechanised. |
| P-14 Board/VG modes express inseparability | ✓ | §12.2 BG Mode, §12.3 Hybrid Mode, §12.5 Mode-Specific Branching | Co-movement present in all modes. §12.5 Thread section confirms Thread ops produce co-movement in BG/Hybrid. |

---

## PART C: SECONDARY ISSUES FOUND (not in session log flags)

### C-1 — NPC Stat Blocks use non-canonical attributes (§13)

All NPC Composure values calculated as `Poise + Heart`. Both attributes non-canonical. Values will require recalculation once Composure formula confirmed (Issue 3 editorial gate).

Affected NPCs: Almud (9), Lenneth (8), Baralta (10 estimated), Vaynard (6), and all others in §13.

**Blocker:** Cannot patch until Issue 3 editorial decision.

### C-2 — §9.1 and §9.6 Debate pools use "Poise"

**Current:** `Pool: Poise + History bonus` (§9.6); Rattled effect on `Poise` (§9.1).

Poise is not in the canonical 10-attribute set. This requires an editorial decision on what canonical attribute governs Debate.

Candidates: Presence (social command, already governs Appeal) or a new social/Performance attribute. Attunement (social reading) is another option.

`[EDITORIAL: select canonical Debate pool attribute to replace Poise. Candidates:
(A) Presence — consistent with Appeal; social command framing
(B) Attunement — empathy/reading framing
(C) A blended pool: Presence for formal/institutional; Attunement for personal/emotional]`

### C-3 — Military NPC "Officer Heart" (§8 Battle Engine, line 2427)

Line 2427: `Officer Heart: adds dice to unit Cohesion checks.`
Line 2474: `Rally requires an officer with Coordination 4+ to spend their action (Heart roll, Ob 2).`

Both use Heart (non-canonical). Additionally "Coordination" appears — also non-canonical (not in 10-attribute set).

`[EDITORIAL: confirm canonical attribute replacements for Officer Heart and Coordination in the Battle Engine. Candidates for Heart → Focus or Spirit; Coordination → Agility or a named History.]`

### C-4 — §16.1 Glossary Composure entry is self-contradictory

Line 3933: `Equal to Poise + Heart. Strain reduces it...`
Line 3993: `Composure = Poise + Heart *(note: compiled ruleset uses Presence + Spirit — confirm at final pass)*`

The self-referential note in the Glossary confirms the compiler was aware of the conflict but did not resolve it. This entry must be updated once Issue 3 editorial decision is received.

### C-5 — CE accumulation uses "Heart" for TS growth checks (§13.6 Inquisitors)

Line 3515: `Heart TN 7, Ob 1`
Line 3533: `Heart TN 7, Ob 2`

TS growth triggered by CE accumulation. The canonical TS growth mechanic in §4.4 does not use Heart — it uses a free roll structure. The CE-triggered TS growth check attribute needs confirmation.

`[EDITORIAL: CE-triggered TS growth check — confirm canonical attribute. Candidate: Cognition (perception/reasoning) or Spirit (existential coherence). Current §4.4 TS growth uses no attribute check; CE path may intentionally differ.]`

### C-6 — §13.1 NPC Stat Blocks reference "Coordination" and "Power" attributes

Line 3390 (Baralta): `Attributes: Coordination 4, Power 4, Poise 5, Presence 5`
None of Coordination, Power, or Poise are in the canonical 10-attribute set.

**Verdict:** NPC stat blocks were compiled against an earlier attribute schema. All named NPC stat blocks require audit and rebuild against the canonical 10-attribute set.

`[EDITORIAL: NPC stat block rebuild is mechanical (not creative) — Claude may execute once canonical Composure/Debate/Officer attribute decisions are received. No content decisions required beyond the editorial flags above.]`

---

## PART D: ISSUES REQUIRING NO ACTION

The following were verified and found compliant:

- P-01 through P-14 scan (except P-04/P-10 header naming): all PASS
- §5.9 CD track: correctly named, correctly scaled (0–20), no Taint contamination
- §5.8 Three-Dimensional Co-Movement: correctly implements inseparability
- §4.5 Intelligibility / §4.6 Certainty: correctly differentiated and mechanised
- §12.6 GM as Rendering Engine: philosophically correct
- §14.5 Three-Clock Feedback Loop: correctly frames TT over-draw (P-07)
- §4.4 Devout Constraint: correctly mechanises P-08 without suppression framing
- §5.6 Past-Oriented Pulling: correctly mechanises P-09 (messy, costly, detectable)

---

## SUMMARY

**Critical (block compilation):** 0 philosophical violations. All P-01–P-14 constraints satisfied except naming issue in §5.10 header.

**Structural (block patch without editorial input):** 4 editorial gates required before full repair can proceed.

**Mechanical repairs (no editorial gate — execute immediately):**
- §5.10 header + body: Taint → Dissolution Track / DL (pending name confirmation)
- §5.2 + §5.5: Heart → Focus (Leap pool, Contact Duration, Wound disruption, Pulling pool)
- §10.3 + §10.4 + §4.3: Heart → Spirit (Inspiration cap and acquisition checks)

**Blocked pending editorial decisions:**
- Composure formula (Issue 3): affects §4.11, §9.1, §10.3 Composure row, §13.x NPC stat blocks, §16.1 Glossary
- Debate pool attribute (Issue C-2): affects §9.1 Rattled effect, §9.6–9.8 social pools
- Battle Engine: Officer Heart + Coordination (Issue C-3)
- CE-triggered TS growth attribute (Issue C-5)
- NPC stat block rebuild (Issue C-6): blocked by all above

**Editorial gate count:** 5 decisions required (Issues 3, C-2, C-3, C-5, §5.10 name confirmation)
