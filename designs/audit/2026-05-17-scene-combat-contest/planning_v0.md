# Scene Combat Reform — Planning Document

**Date:** 2026-05-17
**Authorized by:** ED-864 follow-on
**Companion to:**
  - `designs/audit/2026-05-17-scene-combat-contest/decisions.md`
  - `designs/audit/2026-05-17-scene-combat-contest/battlecon_extraction.md`
  - `designs/audit/2026-05-17-scene-combat-contest/mass_battle_audit_flags.md`
  - `designs/scene/combat_c4_draft_v0.md`
  - `tests/sim/phase11_c4_v0_2026-05-17.md`
  - `tests/sim/phase12_mass_archetype_v0_2026-05-17.md`

**Status:** DRAFT. Jordan review pending. Not yet canonical.

---

## 1. Problem statement

### What was originally specified

Scene combat Agility too powerful. Diagnosis: Combat Pool = (Agi × 2) + History + 3 is single-attribute. Phase 8 sim verified 100% Fast vs Strong at canonical Agi gap (6 vs 3).

### What the deeper investigation actually found

The pool formula is one symptom. The structural cause is **direct linear pool-to-damage scaling**:

> pool → roll → net successes → DAMAGE × damage_mod → direct HP reduction

Pool magnitude advantage cascades **linearly** into damage. A 6D pool advantage produces ~2 extra net successes, which produces 2× the damage modifier in HP loss per round. Pool advantage compounds across rounds because both Offence and Defence scale with pool.

### Why this matters

Contest! has the same simultaneous-roll structure but does NOT have the dominance problem. The difference: Contest!'s Argue roll feeds into the Persuasion Track (bounded 0–10, resistance threshold ~3 to compromise zone, 7 to side A win). Pool advantage cascades **sub-linearly** into outcome because the track absorbs variance.

Combat lacks an intermediating layer between pool comparison and damage.

### What this rules out

- **C4 stance + interaction type (M1+M2+M3):** does not address linear scaling. Phase 11 verified — light-vs-light dominance persists at 94/6 even with reach gate, stance counters, and init preempt active. C4 redistributes dominance across weapon classes but does not eliminate within-class dominance.
- **C2 weapon-keyed primary attribute:** fixes cross-archetype matchups (Strong-with-heavy ≈ Fast-with-light) but does not address within-weapon-class same-attribute dominance.
- **Asymmetric commitment / round restructure:** PP-232 already encodes Vor/Nach via declaration order. Round structure is not the defect.

### What this points toward

An intermediating layer between pool comparison and damage. Three candidates (see §3).

---

## 2. Current state of work

### What is shipped to canon

| Item | Commit | Status |
|---|---|---|
| ED-864 + audit decisions doc | `a6e9ccd` | canonical |
| Contest! design-doc rename (2 files) | `1749395` | canonical |
| BattleCON extraction memo + Phase 8/10 reads | `e34c5b7` | canonical |
| Phase 11 scene C4 sim (M1+M2+M3) + writeup | `2328b12` | canonical |
| Phase 12 mass-battle archetype sim | `eff02dc` | canonical |
| C4 draft spec | `8e3fed4` | draft, not merged |
| Contest! atomization + rename + ED-295 D | `9d6abf2` | canonical |
| Mass-battle audit flags comparator review | `c2d4800` | canonical |
| Session handoff filed | `b17ac25` | active |

### What is closed

- Contest! audit (renames + ED-295 D spec + ED-296 found-canonical + ED-297 ratified)
- Reframing 2 verification (sim-validated asymmetric magnitudes)
- Mass-battle audit flags (HeavyBlunt + Heavy-vs-Heavy reviewed — neither canon defect)

### What is open

- Scene combat structural defect (linear pool-to-damage scaling) — root cause newly identified
- C4 draft has 7 open canonical questions Jordan has not ratified
- C4 magnitudes (Phase 11) redistribute but do not eliminate dominance
- Phase 13 sim (Heavy-vs-Heavy with tactical levers) — folded into Phase 7 Mass Battle handoff
- Hook drift (M3 `completeness_gate` unimplemented; ED-868 standing)

### What is deferred

- HeavyBlunt anti-armor magnitude review (separate audit, faction recruitment / economy layer)
- Cross-system niche dominance sims (Reframing 2 generalization beyond combat/mass)
- Editorial ledger consolidation (separate handoff `2026-05-XX-editorial-ledger-consolidation`)

---

## 3. Three candidate intermediating layers

### Layer A — Posture/Composure track

**Pattern source:** Sekiro posture system; Liechtenauer Vor/Nach as posture state; Contest! Persuasion Track parallel.

**Mechanic:**
- Each fighter has a Posture state: Steady → Pressed → Reeling → Broken (0–3 levels).
- Strike net successes drain opponent's Posture (not HP directly).
- Stamina cost still applies per Strike.
- Broken state opens a **Vulnerability window** for one round.
- During Vulnerability, opponent's next Strike fires at reduced Ob and full damage modifier.
- Posture recovers 1 step per Take Breath action.

**Why this works structurally:**
- Pool advantage cascades sub-linearly: bounded 0–3 state limits how fast dominance compounds.
- Multiple Strikes required to advance state (not one mega-Strike for 6× damage).
- Net successes feed posture damage, then damage fires only at Broken.

**UI consideration:** posture can be narrated (Steady/Pressed/Reeling/Broken) without a visible meter. Compatible with character-gen questionnaire's "player never sees numbers" constraint.

**Implementation cost:** Medium. New state variable per fighter, new transition rules, Vulnerability window action modifier. No new pool, no new dice. Damage formula changes (Strike → posture damage; Vulnerability + Strike → HP damage).

**Sim work required:** Phase 13 — test Posture mechanic vs. Phase 11 baseline. Targets: light-vs-light at 60–70% rather than 94%; within-class dominance compressed; cross-class via reach gate at 60–70% rather than 78%.

### Layer B — Advantage position track

**Pattern source:** Sid Meier's Pirates! advantage bar.

**Mechanic:**
- Single shared variable: position. Bounded -10 to +10.
- Each exchange, pool comparison shifts position toward winner.
- Position +10 or -10 = match decided.
- No HP track. Damage is narrated when position crosses thresholds.

**Why this works structurally:**
- Single bounded variable absorbs all pool variance.
- Match length determined by position movement rate, not HP attrition.

**UI consideration:** Visible advantage bar conflicts with "player never sees numbers" constraint. Could be narrated, but the bar visibility is most of what makes Pirates! legible.

**Implementation cost:** High. Replaces HP entirely. Requires re-doing wound system, character incapacitation rules, body-zone damage (currently in canon).

**Trade-off:** Cleanest mechanical solution but largest canonical disruption. May break narrative weight (a fight at +9 position with no wounds is structurally one shift from defeat — feels arcadey).

### Layer C — Stamina as primary attrition

**Pattern source:** Boxing rounds 8–12, MMA round 3, NERS principle 6.

**Mechanic:**
- Stamina remains canonical attrition driver. HP loss rare.
- Strike consumes opponent's Stamina (not HP) when net successes accrue without clean hit.
- Stamina-out triggers Spent state.
- Spent + clean Strike = decisive blow (direct HP, large damage modifier).
- Take Breath recovery is the primary defensive action.

**Why this works structurally:**
- Stamina is already canonical (Stamina = End × 5, Take Breath recovers End × 2).
- Pool advantage drains opponent Stamina, but Stamina is bounded by End × 5.
- High-pool fighter still wins, but via fatigue not damage cascade.

**UI consideration:** Stamina already exists as variable; surfacing as "winded / steady / spent" is consistent with current canon idioms.

**Implementation cost:** Low. Rebalances existing Stamina mechanic; adds Spent → Vulnerability rule; reduces HP scaling.

**Trade-off:** Conservative. Doesn't fully address scaling — Stamina-out is faster than HP-out at high pool advantage, but the mechanism is still pool-driven. May produce same dominance profile, just shorter fights.

---

## 4. Open decisions for Jordan

### D1 — Confirm root cause identification

The linear pool-to-damage scaling diagnosis was identified this session. Sim work confirms Phase 11 dominance redistribution (not elimination). Does Jordan agree with this diagnosis, or is there a missing factor?

### D2 — Which intermediating layer (A, B, C, or none)

Each layer has different implementation cost, UI surface, and canonical disruption. None has been sim-tested.

| Layer | Cost | UI conflict | Canonical disruption | Addresses scaling |
|---|---|---|---|---|
| A — Posture | Medium | None (narrated) | Damage formula changes | **Yes** |
| B — Advantage bar | High | Yes (visible bar) | HP system replaced | **Yes** |
| C — Stamina primary | Low | None | Stamina re-balanced | Partial |
| None | None | None | None | No — accepts Reframing 2 as solution |

### D3 — Accept Reframing 2 as design solution OR pursue intermediating layer

Reframing 2 (cross-scale niche dominance) is sim-validated. Within-class scene dominance (94/6) and cross-class via reach (78/22) ARE the design picture if Reframing 2 is the canonical position. Pursuing an intermediating layer means going beyond Reframing 2 to address within-class dominance too.

**This is the load-bearing decision.** All subsequent work depends on it.

### D4 — C4 draft fate

If Jordan selects an intermediating layer (D2), the C4 draft is superseded. Its M1/M2/M3 mechanics may still be relevant components within the new framing.

If Jordan accepts Reframing 2 as solution (D3), the C4 draft can be ratified with magnitude calls on its 7 open questions, then merged into canonical params/combat.md + combat_v30.md.

### D5 — Implementation order

Several dependencies:
- D2/D3 must precede C4 fate (D4).
- Phase 13 sim cannot be designed until D2 selected.
- Hook drift (M3 completeness_gate) is infrastructure, independent of design path.

---

## 5. Work phases (dependency-ordered)

### Phase α — Decision

1. Jordan reviews this planning document.
2. Jordan ratifies D1 (root cause) or surfaces alternative.
3. Jordan decides D2/D3 (layer or accept Reframing 2).
4. Jordan decides D4 (C4 fate) following D2/D3.

**Output:** ratified direction.

### Phase β — Spec (only if D2 = A/B/C)

1. Draft spec for selected layer (Posture / Advantage Bar / Stamina Primary).
2. Spec includes: state transitions, action effects, damage formula changes, integration with existing Stamina/HP/wound system.
3. Open canonical questions tabled per spec.

**Output:** layer specification doc.

### Phase γ — Sim (Phase 13)

1. Implement layer in sim atop Phase 11 baseline (undoubled pool + M1+M2+M3 if Jordan keeps C4 components, or stripped if Jordan supersedes).
2. Run matchups: symmetric calibration, light-vs-light Agi gap, light-vs-heavy reach, balanced builds, F3 gap (Mighty-light vs Fast).
3. Targets:
   - Calibration: 50/50
   - Light-vs-light Agi gap: 60–70% Fast (compressed from 94%)
   - Light-vs-heavy: 50–60% (parity rather than 78/22 inversion)
   - F3 gap: 40% Mighty-light vs Fast (up from 12%)
   - Balanced: 45–55% (viable rather than 17.8%)

**Output:** Phase 13 sim + writeup. Verdict: layer adopted, tuned, or rejected.

### Phase δ — Merge

1. Layer + C4 components (if retained) merge into params/combat.md.
2. designs/scene/combat_v30 updated.
3. Editorial ledger updated.
4. Character-gen questionnaire reviewed for impact (does posture/advantage/Stamina surface in character creation?).

**Output:** canonical scene combat reform.

### Parallel work (not blocking)

- HeavyBlunt anti-armor audit (faction recruitment / economy layer).
- Phase 7 Mass Battle integration (existing handoff).
- Hook drift M3 completeness_gate implementation (ED-868).
- Editorial ledger consolidation (existing handoff).
- Cross-system niche dominance sims (Reframing 2 generalization).

---

## 6. Risks and unknowns

### R1 — Root cause may be incomplete

Linear pool-to-damage scaling is the structural cause identified this session. There may be additional factors (e.g., wound interval, stamina-vs-HP loss-rate asymmetry, action-cost equilibrium). Phase 13 sim will surface these.

### R2 — Layer A (Posture) may not transfer cleanly to mass battle

Mass battle (params/mass_combat.md) already has Discipline + Command + tactic card layers. Adding scene-level Posture doesn't automatically integrate. Scale transitions need verification.

### R3 — Layer C (Stamina primary) may not address scaling enough

Conservative path. Phase 13 sim may show Stamina-out at high pool advantage still produces 80/20 dominance.

### R4 — Real-combat research may continue to surface "new" structural insights

The real-combat detour identified the linear-scaling defect only after extensive treatise + sports + games research. Future research may surface additional factors. Watch for: bias toward synthesis, easiest-to-justify framing, pattern-matching to specific exemplar games.

### R5 — Character-gen questionnaire integration

Questionnaire commits to "player never sees numbers." Any layer choice must be narratively surfaceable. Layer A (Posture as states) and Layer C (Stamina as states) compatible; Layer B (Advantage Bar) less so.

### R6 — Assistant bias surface

Three biases identified across session:
- Confirmation bias toward synthesis framings (tiered design pushed twice, withdrawn)
- Recommendation-reflex when faced with multiple options
- Easiest-to-justify bias (toward direction preserving prior sim work)

Watch for these in subsequent sessions, especially around Phase 13 sim design (where temptation to design sim that validates a preferred layer is high).

---

## 7. Decision summary required from Jordan

| ID | Decision | Blocks |
|---|---|---|
| D1 | Confirm linear pool-to-damage as root cause | All subsequent work |
| D2 | Select intermediating layer (A / B / C / none) | Phase β, γ, δ |
| D3 | Accept Reframing 2 as solution OR pursue layer | Equivalent to D2 reframed |
| D4 | C4 draft fate (ratify, supersede, partial-retain) | Phase δ |
| D5 | Approval to begin Phase β when D2 selected | Phase β |

Until D1 ratified or alternative root cause surfaced, all combat reform work is blocked.

---

## 8. Related artifacts

**Sim infrastructure:**
- `tests/sim/scripts/phase8_smart_ai_v2_2026-05-15.py` — baseline Agi dominance
- `tests/sim/scripts/phase10_str_stam_reform.py` — undoubled pool reform
- `tests/sim/scripts/phase11_c4_v0.py` — M1+M2+M3 stack
- `tests/sim/scripts/phase12_mass_archetype_v0.py` — mass-battle archetype
- `tests/sim/phase11_sim_verification_ledger.json` — Phase 11+12 canonical value attestation
- `tests/coverage_matrix.md` — sim register

**Design canonical:**
- `params/combat.md` — current scene combat spec (PP-232 declaration order; PP-294 Feint mechanics)
- `params/contest.md` + `params/contest_extensions.md` — Contest! atomized; ED-295 D specced
- `params/mass_combat.md` — mass battle Core Formula PP-233
- `params/core.md` — d10 pool engine spec, continuous engine (ED-833)
- `designs/scene/combat_v30_index.md` + `_infill.md` — combat design canonical
- `designs/personal/character_generation_questionnaire_v30.md` — narrative direction (numbers-hidden constraint)

**Editorial ledger:**
- ED-864 — combat C4 direction
- ED-838 — Phase 8 Agi dominance baseline
- ED-839 — Phase 10 reform baseline
- ED-869 — Contest! plain-English rename
- ED-295/296/297 — Contest! resolutions
- ED-868 — hook drift (M3 completeness_gate)

**Handoffs:**
- `2026-05-17-scene-combat-redesign-exploration` (this work)
- `2026-05-18-phase-7-mass-battle` (mass battle integration)
- `2026-05-XX-editorial-ledger-consolidation` (separate)
