<!-- DERIVED FROM: Checkpoint 14 (compilation/valoria_ruleset_checkpoint_14.md, 2026-03-26) -->
<!-- SESSION: 2026-03-30 / 2026-03-31 — see session_log_archive.md -->
<!-- STATUS: Pre-release reference tool. Not valid against any post-CP14 ruleset. -->

# D-06 — THREAD OPERATION RESOLUTION CARD
*Run through in order. Every step applies every time.*

---

## PRE-OPERATION CHECKLIST

**Leap eligibility (all must be true):**
- [ ] Approach Training tag
- [ ] TS ≥ 30
- [ ] TT ≥ 20
- [ ] Not currently in melee with opponent who declared attack this round
- [ ] Not at/above incapacitation Wound threshold

---

## STEP 1 — DECLARE AND LEAP (Priority 5, full-round)

**Leap Pool:** Attunement + relevant History bonus (pre-calculated on sheet)
**TN:** 7 | **Ob:** TS 30–49 = 2 · TS 50+ = 1 · −1D per Wound

| Degree | Outcome |
|--------|---------|
| Overwhelming | Clean contact. Next op Ob −1 (min 1). +1 TS. |
| Success | Contact achieved. Proceed. |
| Partial | Unstable. Op Ob +1. −2 Composure. |
| Failure | No Thread op this scene. −4 Composure. Rattled. |

**Contact window:** Focus score in rounds (inclusive of Leap round)

---

## STEP 2 — DIAGNOSIS (Priority 4, free action, Round N+1)

No roll. GM exchange: GM describes actualization tightness (sets Ob), prior workings, Gap risk, Coherence trace.

**Mandatory before FR:** Skip = +2 Ob + auto-Gap on Failure
**Mandatory before Past-Pull:** Skip = +3 Ob + temporal Gap on Failure

---

## STEP 3 — DECLARE OPERATION + SCALE

| Op Type | Pool | TN | Scale Ob Range |
|---------|------|----|----------------|
| Weaving | Spirit + History | 7 | Ob 1–5 |
| Pulling | Spirit + History | 7 | Ob 1–5 |
| FR Lock | Spirit + History | 7 | Ob 4–8+ (min 4) |
| FR Dissolution | Spirit + History | 7 | Ob 4–8+ (min 4) |
| Mending | Attunement + Focus + TPS | 7 | Ob 2–8 |

**Current Op Ob Modifiers (stack additively, cap at 10):**
- Partial Leap: +1
- Wounds: −1D (not Ob)
- TT > 60: +1 Ob all ops
- TT > 79: +2 Ob all ops
- Coherence Fragmented/Fractured/Severed: +1/+1/+2 Ob
- Overweaving (2nd+ in same scene): +1 Ob cumulative

---

## STEP 4 — RESOLVE OPERATION (roll + degree)

*(See individual operation degree tables in ruleset §5.4–5.7)*

---

## STEP 5 — CO-MOVEMENT FIRES (mandatory, every operation)

### Temporal Auto-Effect (automatic)

| Op Type | Effect | TT Change |
|---------|--------|-----------|
| Weaving (any degree) | Target's temporal axis compresses; observers TS 10+ perceive target as "clearer" 1 scene | −1 |
| Pulling (any degree) | Loosened thread's temporal anchoring frays; social roll citing it as precedent +1 Ob until reaffirmed | −1 |
| FR Lock | Locked config's temporal axis freezes permanently | −2 |
| FR Dissolution | Temporal void; present feels denser | −2 |
| Past-Pull (additional) | Witnesses retain both memories; paradox unresolvable without Thread understanding | −3 add. |

**→ Narrative: [SEE D-11 CO-MOVEMENT MATRIX — temporal beat row]**

### Epistemic Auto-Effect (automatic)

| Op Type | Effect |
|---------|--------|
| Weaving (S/O) | Target MORE intelligible; TS 10+ perceive clarity 1 scene |
| Weaving (P/F) | Target LESS intelligible; testimony about target +1 Ob 1 session |
| Pulling (any) | Epistemic instability; witnesses disagree on details; investigation/Circles +1 Ob until accounting |
| FR Lock | Locked config opaque; Diagnosis on target +2 Ob |
| FR Dissolution | Epistemic void; Certainty check for all non-practitioners (Spirit TN 7 Ob 1); cap 1/scene |
| Past-Pull | Witnesses retain both memories; inert knowledge of paradox |

**Stacking cap:** Epistemic investigation mod + temporal precedent mod do not stack; use higher. Cap +1 Ob/roll.

**→ Narrative: [SEE D-11 CO-MOVEMENT MATRIX — epistemic beat row]**

### Actual d6 (roll now)

| d6 | Effect |
|----|--------|
| 1 | Knot strain ±1 (target's or practitioner's — GM choice) |
| 2 | Nearby object enters partial potentiality (minor Shifting Object risk; self-corrects 1d3 days) |
| 3 | Physical residue at operation site |
| 4 | Target's physical config overshoots intended scope |
| 5 | Environmental texture shifts (temperature/light/sound; detectable TS 10+) |
| 6 | Delayed manifestation (1d3 scenes later) |

**→ Narrative: [SEE D-11 CO-MOVEMENT MATRIX — d6 table column]**

---

## STEP 6 — POST-OPERATION CHECKS

**Coherence Retention Roll** (at end of full Leap contact window, not per operation):
- Pool: Spirit + relevant History + TPS, TN 7
- Ob: sum of all operation Obs performed during this Leap
- Fail → −1 Coherence

**TT change:** Apply all auto-effects + degree table changes to TT tracker

**TS growth check** (if Leap was Overwhelming): +1 TS

**Fraying Bane check:** 3rd+ FR Dissolution or Past-Pull this season → Fraying active

**History Resonance:** If temporal co-movement fired + practitioner has relevant History → Resonance active; next use of that History +1D (on result 1: −1 TT)

---

## SCALE QUICK-REFERENCE

| Scale | Ob | Min TS | TT Cost Modifier |
|-------|-----|--------|-----------------|
| Object | 1–2 | 30+ | ×1 |
| Personal | 2–3 | 30+ | ×1 |
| Relational | 3–4 | 50+ | ×2 |
| Territorial | 4–5 | 50+ | ×3 (floor) |
| Structural | 5–8+ | 70+ | ×3 (floor) |

*Mass combat Thread ops: all TT costs ×3 floor, capped at +15/op*

---

## COLLECTIVE OPERATION QUICK-REFERENCE

- Anchor: highest TS; sets intentionality; cannot Fork
- Each helper contributes: floor(Cog ÷ 2) bonus dice
- Helpers cannot Fork
- Anchor fails Leap → lattice does not form (helpers proceed individually)
- Helper drops mid-op: if pool < half Anchor solo pool → +1 Ob
- Conflicting Beliefs: tangential = no chaining; direct = Spirit Ob 1 pre-Leap or drop out
- Co-movement scales with participant count
