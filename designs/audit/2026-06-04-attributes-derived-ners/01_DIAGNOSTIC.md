# Turn 2 — NERS Diagnostic · Character Attributes & Derived Stats · ALL DIRECTIONS

**Date:** 2026-06-04 · Dual-instrument (structural NERS via mechanic-audit lens + engine-fitness via resolution-diagnostic). Verdict-first, severity-ranked. Builds on `00_FOUNDATION.md`.

---

## A · Reconciliation with prior audits (build, don't duplicate)
`2026-05-08-character-mechanics-critical-audit.md` (PROVISIONAL) already adjudicated much of this. Convergences and extensions:
- **Recall** → graded **AUDIT/FOLD, N:low E:low R:low S:low**, "standalone stat for a single mechanic [sparking gatekeeper]… BW-Wises heritage" (L129–133); F1 (L589) recommends folding into Mind/Spirit. **My audit confirms and *escalates*:** Concentration's `Focus+Recall` was **STRUCK 2026-06-04 (ED-902)** (derived_stats §5.2/§14.1), removing Recall's last derived-stat role.
- **Bonds (Knots)** → **KEEP, N:critical** (L181–185). **Confirmed.**
- **Attribute-roster structure UNRESOLVED** — F2 (L591): "Sub-pools [Cognition/Focus/Endurance/Charisma/Bonds] — independent tracks, or derived from Mind/Body/Spirit?" (#14 = "Attribute d-pools [Mind/Body/Spirit]", #15 = sub-pools, AUDIT). **Still unresolved; I find no canonical resolution, and the 2026-06 combat engine uses flat fields — deepening the gap.**
- **Spirit naming collision** — F9 (L607): Spirit-the-pool vs Spirit-the-metaphysical-attribute. **Confirmed; now compounded by Spirit-overload (below).**
`[CONFIDENCE: high — prior audit read in full; convergent independent findings.]`

## B · Phase-0 engine assignment (recap from Foundation)
Rolling: combat exchange + social contest exchange → **Instance A** (healthy 5–18D pools); faction Domain → **Instance B** (faction-fed, adjacent). Attributes (1–7) and derived resources are **roll inputs / state**, structurally diagnosed (mechanic-audit), not engine-verdicted.

---

## C · STRUCTURAL NERS (the bulk)

### Mode A — Formula validation (derived stats; cited to `derived_stats_v30`)
| Derived | Formula | Min→Max | Issue |
|---|---|---|---|
| Health | `(End+6)×(MW+1)`, `MW=min(floor(End/2)+1,3)` | 14→52 | clean; but **not** `attr×multiplier` (violates §1 — see Mode B) |
| Stamina | `(3×End)+(2×Spirit)` (S1, 2026-05-29) | 5→**35** | **§4.2 states "Range 5–47" — formula maxes at 35. Range/formula mismatch (P2).** Multi-attribute (violates §1). |
| Composure | `Charisma×3` | 3→21 | clean |
| Concentration | `(3×Focus)+(2×Spirit)` (ED-902, 2026-06-04) | 5→**35** | **§5.2 *body* still says `Focus×3`, range 3–21 — contradicts §12/§14.1 (P2).** Multi-attribute (violates §1). |
| Thread Fatigue | `Spirit×5` (threshold) | 5→35 | clean |
| Disposition cap | **`= Bonds`** (§10.1/§14.2, PP-684) | 1→7 | **CONTRADICTS `floor(Bonds/2)+1` in `complete_systems_reference` L219 + `params/contest.md` L78 (P1). Resolution below.** |
| Knot Pool | `(Bonds×2)+3` | 5→17 | clean, healthy |
| Faction (Treasury ×100, Legitimacy ×20, Reputation ×15, Discipline ×10, Levies ×2) | linear | clean | deterministic-accounting; pass |

**Disposition-cap resolution (evidence-based correction).** `= Bonds` is current: PP-684 §10.1, and it is the only formula consistent with §10.1's own requirement that **Knot candidacy (Disposition +5) requires Bonds ≥ 5** — under `floor(Bonds/2)+1`, Bonds 5 caps Disposition at **3** (< 5), making Knot candidacy unreachable. So `floor(Bonds/2)+1` (csr + contest.md) is **stale pre-PP-684** and must be struck. `[SELF-AUTHORED — bias risk: my Turn-1 reply cited floor(Bonds/2)+1 for the Disposition cap. Corrected here to PP-684 cap = Bonds.]`

### Mode B — Number-system coherence
- Attributes uniformly **1–7** ✓. Derived ranges differ by orders of magnitude (Health 14–52 … Treasury 100–700) — **intended** per §3 multiplier tiers + §14.5 (interaction-frequency calibration). Not a violation.
- **§1 ARCHITECTURE PRINCIPLE VIOLATED (P2, durable):** §1 states *"`derived_value = attribute × multiplier`. One attribute per derived value. No multi-attribute combinations."* This is now **false** — ratified **Stamina `(3×End)+(2×Spirit)`** and **Concentration `(3×Focus)+(2×Spirit)`** are multi-attribute. The system's *defining rule* no longer holds; §1 is unamended stale text. (Deliberate via S1/ED-902 → §1 is the defect, not the formulas — but uncorrected.)
- **§3 multiplier-tier table stale:** lists Concentration ×3 (now compound), Stamina ×5 (now compound).
- Disposition-cap inconsistency (analogous concept, two scales) — Mode-B + Mode-A.

### Mode C — Interaction chains (downstream count → orphan/overload)
| Attribute | Live downstream | Load |
|---|---|---|
| **Spirit** | Thread Fatigue, Inspiration cap, Stamina (2×), Concentration (2×), Sincerity Gate | **OVERLOADED (5)** — super-stat post-S1/ED-902; now central to combat *and* thread *and* social |
| Endurance | Health, Stamina (3×), Wound Interval | rich (3) |
| Bonds | Disposition cap, Knot pool, Socializing, Corroborate | healthy (4) |
| Attunement | Argue(No-adj), Appraise, Read, First-to-Speak, prep | several (contest — currency-tangled) |
| Charisma | Composure, Argue(Crowd) | 2 |
| Focus | Concentration, Thread max-ops | 2 (lost coalition pool) |
| Cognition | Argue(Expert/Panel) | 1 (contest — tangled) |
| **Agility** | poise / `balance_eff` only | **THIN (1)** — Combat Pool dropped Agility 2026-06-04 (was its main role) |
| **Recall** | Sparking gate `Spirit+floor(Recall/2)`, equip-slot gating, `+2D` cite-bonus | **ORPHAN-ADJACENT** — all single-purpose; Concentration role stripped today |
- **Loops (only where a roll sits in the cycle):** (i) §10.4 personal-combat→Garrison→faction-Discipline loop — increments ±10/±20 vs stat-derived caps; recovery exists → **bounded, PASS**; (ii) wound→−1D-pool→worse-roll loop — capped at MW≤3 then felled → **bounded, PASS**; (iii) faction-collapse loop (Instance-B, faction-fed) → terminal-bound finding **deferred to faction audit**. No attribute↔attribute circularity (attributes feed derived, not vice-versa except §8.2 gated structural damage). **PASS.**

### Mode D — Gaps (P1 = blocks/foundational, P2 = ambiguity, P3 = polish)
- **P1** Attribute-roster STRUCTURE unresolved (macro Mind/Body/Spirit + sub-pools *vs* flat ~10); **no single canonical roster doc**; F2 open since 2026-05-08, combat engine forces it.
- **P1/P2** Disposition-cap formula contradiction (3 statements).
- **P2** §1 one-attribute principle vs ratified multi-attribute formulas.
- **P2** §13 ("Combat Pool = `(Agi×2)+Hist+3`") vs §14.4 (STRUCK 2026-06-04 → `max(5,Hist+6)`, Agility-independent) — internal contradiction (doc mid-edit).
- **P2** §5.2 Concentration body (`Focus×3`) vs §12/§14.1.
- **P2** Recall's surviving canonical role-set undefined post-strip.
- **P2/P3** Stamina range 5–47 vs max 35; §3 tier table stale.
- **(ack)** §9 settlement derived PENDING; Intel→Intelligence Holdings PENDING.

### Mode E — Principles compliance (attribute-bearing)
- **#5 "Pool = Attribute + History bonus" — VIOLATED for COMBAT** (`max(5, History+6)`, Agility-independent; §14.4 + combatant.py L69). Argue/Thread/Fieldwork/Knot pools still `Attribute×2 + Hist + 3` (principle holds). Deliberate (the **C-04 Agi-OP fix** moves Agility from pool-size to σ-leverage) — but the foundational principle text is now stale for combat, and combat's stat-economics now diverge from its siblings (→ Mode-S lateral flag).
- **#4 Histories-not-Skills** — holds. `[GAP: full 13-principle list not re-confirmed this session.]`

---

## D · ENGINE-FITNESS (Property Test P-i…P-v — attributes-as-inputs only)
- **Combat exchange (Instance A):** pool ≥5D healthy → correct engine. Agility now a **leverage modifier (Δσ)** not pool size = the C-04 fix → **P-ii uniform leverage by construction.** P-i legible, P-iv graded. Live caveats are **engine-level, not attribute-level**: continuity-correction (`net−(Ob−0.5)`, ER-2) **not yet landed** in `params/core.md §Continuous Engine` (P-i/P-iii below 5D); ED-875 low-input leverage hot (OPEN). **Attribute-input verdict: PASS** (Agility-as-leverage is the right shape; outcome decoupled from raw pool).
- **Social contest (Instance A):** whichever of the three specs is live, pools (`(Primary×2)+Hist+3+style`, 5–18D) are healthy → A; the ratified groundup uses "σ-leverage (= canon's σ-leverage) + base d10" → engine-consistent. **The defect here is structural (which attribute model), not engine.**
- **Faction Domain (Instance B):** ratified ED-874; faction-fed, **adjacent** — deferred to faction audit.

---

## E · ALL DIRECTIONS (explicit)
- **Bottom-up** (attr → derived → input): chains exist but are **not error-free** — Disposition-cap contradiction, §1-principle violation, Stamina/Concentration range/formula mismatches. **R fail.**
- **Top-down** (serves `intent_of_game` = positive-feedback loop + emergent narrative?): Endurance/Spirit/Bonds generate emergent state (combat attrition, inner-resource arcs, relationship dynamics) → serve it. **Recall does not pull weight** (allocation that drives almost nothing emergent). Agility's contribution moved to leverage (still serves combat texture). **Net: serves intent except Recall.**
- **Vertical** (cross-scale): the derived-stat system *is* the vertical bridge (personal ↔ unit `TroopCount` ↔ faction Treasury/Discipline ↔ settlement); §14.5 intends one 1–7 number → scale-specific pools. **Mostly smooth**, but **§9 settlement PENDING** (vertical gap) and the **macro-vs-flat structure hole** is a vertical-legibility failure.
- **Lateral / horizontal** (sibling consistency at the personal scale): **PARTIAL FAIL** — **combat stat-economics now diverge from social/thread/fieldwork/knot** (combat dropped the attribute term; siblings keep `Attr×2+Hist`). Documented & defensible (combat's short small-pool duels amplify pool advantage — corroborated by the v27 weapon-audit lateral flag), but it is a **methodology inconsistency** → S flag.
- **Diagonal** (cross-scale + cross-system loops): §10.4 personal→settlement→faction loop **bounded (PASS)**; faction-collapse loop deferred. Diagonal loops bounded where a roll sits in them.

---

## F · NERS VERDICT
**SYSTEM:** Character attributes + derived stats · **COMPONENTS:** base attributes (static, mechanic-audit) · derived resources/values (deterministic + resources) · feeding Instance-A combat/social rolls
**VERDICT: NON-COMPLIANT (system level) — the individual mechanics are mostly sound; the *system* fails on internal-consistency rot, one near-orphan stat, and an unresolved roster structure.**

- **N: FAIL** — **Recall** is N:low (single-purpose; AUDIT/FOLD per 2026-05-08; Concentration role stripped 2026-06-04; live roles ≈ Sparking gate + equip-gating + a `+2D` bonus, all foldable). Inverse problem: **Spirit is over-necessary** (5 downstream). Most other attributes earn their place.
- **R: FAIL** — not "complete, error-free": Disposition-cap contradictory across ≥3 docs **(P1)**; §1 one-attribute principle contradicted by ratified Stamina/Concentration **(P2)**; §13/§5.2 stale post-2026-06-04; Stamina range 5–47 vs max 35. The roster is mid-edit and internally inconsistent.
- **S: FAIL** — lateral: combat stat-economics diverge from siblings (principle #5 holds for social/thread/fieldwork/knot, not combat); §3 tier rationale stale vs §14 formulas; **Spirit naming collision** (pool vs metaphysical attribute, F9); no single canonical roster → cross-scale friction.
- **E: FAIL** — neither player nor designers can intuit whether there are **3 attributes (Mind/Body/Spirit) or ~10 flat** (F2, unresolved since May); Spirit overload obscures the attribute economy; **Recall is allocation overhead with near-zero intuitive payoff.**

**Individual-component note (no false negative):** Health, Stamina, Composure, Concentration, Thread Fatigue, Knot Pool, and the faction derived buffers are each individually well-formed (Mode-A clean modulo the stale-text mismatches). The failures are at the **integration / roster / Recall** level, not in most single formulas.

### REMEDIATION (worst-first; mechanical-tier, Jordan-vetoable; structural-ontology items are Jordan's call, not mine)
1. **[P1 — Jordan, structural]** Ratify the attribute-roster **structure** — macro `Mind/Body/Spirit` + sub-pools *or* flat ~10 — and write **one** canonical roster doc. (Closes F2; the flat combat-engine fields force the decision.) *This is a canon-structure decision; I flag, I do not decide.*
2. **[P1]** Fix the **Disposition-cap** contradiction → ratify **`= Bonds`** (PP-684); strike `floor(Bonds/2)+1` from `complete_systems_reference` + `params/contest.md`.
3. **[P2 — Jordan]** Resolve **Recall** → fold into Spirit/Mind for the Sparking gate (per 2026-05-08 F1) and route equip-gating off the fold, **or** give it a genuine anchor pool. Its Concentration role is already gone; momentum favours fold/cut. *Recommendation; Jordan decides cut vs keep.*
4. **[P2]** Amend **§1** (one-attribute principle) + **§3** (tier table) to match the ratified multi-attribute Stamina/Concentration — the principle is the stale text.
5. **[P2]** Address **Spirit** overload + naming collision (F9): rename pool-vs-attribute; weigh whether Spirit feeding combat+thread+social is too central.
6. **[P3]** Cleanup: propagate the 2026-06-04 edits to **§13** (combat pool) and **§5.2** (Concentration); fix Stamina range 5–47 → 35.
7. **[S — Jordan]** Decide combat-vs-sibling stat-economics: accept the documented asymmetry (combat pool History-only + Agility-as-leverage) and revise principle #5, or realign.

---

## G · PER-STAT VERDICT — the original worry, answered
| Stat | Verdict | NERS | Basis |
|---|---|---|---|
| **Bonds** | **KEEP** (sound) | N:critical E:high R:high S:high | Relationship pillar: Disposition cap (=Bonds), Knot pool `(Bonds×2)+3`, Socializing, Corroborate. Only live issue = the cap-formula contradiction (fixable, #2). Corroborated KEEP (2026-05-08). |
| **Recall** | **AUDIT/FOLD** (the real problem) | N:low E:low R:low S:low | Near-orphan; independently flagged for fold/cut (2026-05-08); **hollowed further 2026-06-04** (Concentration strip). Live roles all single-purpose & foldable. |

**Answer to "I worry Recall and Bonds are bad stats":** not symmetric. **Bonds earns its place; Recall is the genuinely weak stat** — and canon is *already* drifting toward removing it. Concentrate the worry on Recall.

`[CONFIDENCE: high on Recall/Bonds and the consistency findings — all cited; medium on the macro-vs-flat structure (genuinely unresolved in canon, not just unread).]`
`[GAP: whether params/contest.md is *formally* superseded vs merely divergent — inferred from social_contest_v30 + the ratified groundup; not stated in supersession_register.]`
