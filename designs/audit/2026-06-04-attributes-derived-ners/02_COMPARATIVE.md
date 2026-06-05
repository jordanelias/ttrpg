# Turn 3 — Comparative Critique vs Critically Acclaimed Games (top-down validation)

**Date:** 2026-06-04 · Validates/calibrates the Turn-2 findings against acclaimed published game design — the anchor the project-owner contract requires for any mechanical call. Builds on `01_DIAGNOSTIC.md`.

**Reconciliation:** the two existing "comparative" audits are *not* acclaimed-game comparisons — `comparative-audit-faction-vs-character` compares internal frameworks (Convictions/cascade); `faction_stats_renaissance_review` compares faction stats to Renaissance history (+ one VTM ref). This character-attribute-vs-games comparison is additive.

**Strongest validity grip:** Valoria *names its own referents* in canon — **Battle Brothers** (Stamina/fatigue, derived_stats §4.2), **SaGa/Romancing SaGa** (Sparking, character_histories), **Disco Elysium / Ogre Battle / Darklands** (character-gen §1), **CK3/EU/KoDP** (the Domain resolver), **Burning Wheel** (combat "Fight!" heritage; Recall = "BW-Wises heritage" per the 2026-05-08 audit). So this is internal-referent consistency, not imposed external taste.

`[CONFIDENCE: high — comparisons rest on settled game-design knowledge; no claim here is time-sensitive. mcp/web off per prefs; settled design facts answered directly. Any single uncertain mechanical claim flagged inline.]`

---

## Comparison 1 — Roster size & structure → **VALIDATES & sharpens the [P1] macro-vs-flat finding**
| Architecture | Acclaimed exemplars | Count |
|---|---|---|
| **Grouped (macro + sub)** | World of Darkness / Storyteller — 9 attributes in 3 categories (Physical/Social/Mental, ×3 each) | 3×3 |
| | Disco Elysium — 4 macro attributes → 24 skills | 4 → 24 |
| **Flat** | D&D / Pathfinder (6), Fallout **SPECIAL** (7) | 6–7 |

Valoria currently holds **both** framings canonically (Mind/Body/Spirit as "core resolution" per the 2026-05-08 audit #14; flat ~7 fields in the 2026-06 combat engine). **Every acclaimed system commits to one architecture and is unambiguous about its count.** The defect is not the choice — WoD-style 3×3 and flat-7 are *both* acclaimed — it is the **un-committed limbo**.

**Verdict:** the Turn-2 [P1] finding is **VALIDATED and sharpened into a clean menu for Jordan:**
- **WoD-style `Mind/Body/Spirit × 3 sub-pools`** — thematic grouping, manageable player surface, room for the existing sub-pool names (Cognition/Focus/Endurance/Charisma/Bonds…). Maps directly to the most influential grouped attribute system in the medium.
- **Flat ~7 (Fallout/D&D)** — directness, no aggregation layer; demands each of the ~7 earn a gate (which is the Recall test, below).
Either commits cleanly. The limbo is what fails E/S. *(Structure choice is Jordan's canon-ontology call; I supply the menu, not the pick.)*

## Comparison 2 — Recall → **STRONGLY VALIDATES the AUDIT/FOLD finding**
| Pattern | Acclaimed handling |
|---|---|
| **Single-gate / dump stat** (Recall = sparking gatekeeper only) | The **D&D Int/Cha dump-stat problem** is the canonical *negative* example — long-criticized; every successor edition worked to give each stat a reason to invest. A one-gate attribute is the purest form of the anti-pattern. |
| **"What you know" / recall** | **Disco Elysium** refactored knowledge *into* 24 voiced skills, each with upside **and** downside — there is no pure dump skill. **Darklands** (which Valoria's own char-gen cites) gates content by **History/background**, not a memory stat. Valoria *already* does History-gated content access. |
| **Heritage check** | Recall is **Burning Wheel "Wises"** — a **GM-facing** knowledge skill that works because a GM adjudicates "what do you know." Valoria has **no GM** (the engine resolves — `design_doc_framing`). A GM-facing knowledge stat does not translate to a no-GM videogame. |

**Verdict: STRONGLY VALIDATED.** Acclaimed practice is unanimous: a single-gate attribute is a defect, and "what you know" is better carried by **skills/Histories** (DE + Darklands — both Valoria referents, and Valoria already has History-gated access). Recall is a TTRPG-GM residue with no videogame home — exactly the 2026-05-08 snob finding, and why ED-902 already stripped its last derived role. **Fold the sparking gate into Spirit/Mind; let History-gating carry "what you know."** The cut is the one acclaimed design endorses.

## Comparison 3 — Bonds → **VALIDATES the KEEP finding**
| Pattern | Acclaimed exemplars |
|---|---|
| **Capability gates relationship depth + grants a relationship pool** | **Persona 3/4/5** Social Links / Confidants (levels gate depth + payoff) — among the medium's most acclaimed systems; **Fire Emblem** supports (C/B/A/S gate bonuses + story); **Mass Effect / Dragon Age / Stardew** affinity meters. |

Bonds → Disposition cap (`= Bonds`) gating Companion formation (Disp ≥ +3 ⇒ Bonds ≥ 5) and Knot candidacy (Disp +5 ⇒ Bonds ≥ 5), plus the Knot **pool** `(Bonds×2)+3`, is **precisely** the Persona/FE "bond-capacity gates relationship depth and feeds a relationship action" pattern.

**Verdict: VALIDATED.** Bonds is squarely in acclaimed practice; the only fix is the internal cap-formula contradiction (a consistency bug, not a design-soundness issue).

## Comparison 4 — Derived split + §1 one-attribute rule → **VALIDATES, with a REFRAME**
- The **stat → derived resource** split ("what you CAN do vs what you HAVE", derived_stats §1) is universal acclaimed practice: D&D HP, CRPG stamina/mana, **Battle Brothers** fatigue (Valoria's cited referent — action costs deplete fatigue, armour adds cost; Valoria's Stamina §4.2 reproduces this almost exactly).
- **But** acclaimed derived resources **freely combine inputs**: D&D HP = f(Con, class, level); fatigue/spell pools are rarely single-stat. The purist **"one attribute × multiplier, no combinations" rule (§1) is NOT how acclaimed games derive resources** — it is an over-constraint.

**Verdict: VALIDATED with a reframe of the Turn-2 [R/P2] finding.** Breaking §1 (Stamina `End+Spirit`, Concentration `Focus+Spirit`) moves Valoria **toward** acclaimed practice, not away. So the defect is the **unamended principle**, not the multi-attribute formulas. **Fix flips:** amend §1 to permit principled multi-attribute derivation (every acclaimed RPG does), keeping the discipline "derivation must stay legible." Not "the formulas broke the rule" — "the rule was wrong; retire it."

## Comparison 5 — Spirit overload → **VALIDATES the asymmetry as a real risk**
| Pattern | Acclaimed handling |
|---|---|
| **Over-centralized "mandatory tax" attribute** | **D&D Constitution/Dexterity** over-centralization (everyone needs Con for HP, Dex for AC/init/saves) is long-criticized for flattening build diversity. **WoD Willpower** powers too much. Good design spreads load so no single attribute is a must-take tax. |

Post-S1/ED-902, **Spirit** feeds Stamina (combat) + Concentration (social) + Thread Fatigue (thread) + Inspiration cap + Sincerity Gate — a **cross-pillar mandatory tax** (you want Spirit whether you fight, talk, or thread). This mirrors the D&D Con/Dex over-centralization acclaimed design avoids.

**Verdict: VALIDATED.** Spirit-overload is the **inverse** of the Recall problem (one stat too central, one too thin); acclaimed practice wants every attribute in a healthy middle band. Rebalance Spirit's load and fix the F9 naming collision. *(The asymmetry — super-stat + dump-stat at once — is the roster's clearest top-down failure.)*

## Comparison 6 — Combat vs sibling stat-economics → **PARTIALLY VALIDATES → SOFTEN**
- **Combat using different math than social is acclaimed-normal:** most CRPGs (combat = d20+mods vs social skill checks); **Disco Elysium** (combat skill-checks differ from white/red checks); **Mount & Blade / Battle Brothers** separate *skill* (reliability) from *attribute* (other effects) — exactly what Valoria's combat pool now does (`max(5, History+6)` = skill-driven; Agility → σ-leverage).
- The divergence is the **C-04 Agi-OP fix** — a real, defensible reason (decouple outcome from pool count, per the sigma-leverage engine).

**Verdict: PARTIALLY VALIDATED → I SOFTEN the Turn-2 S-flag.** The divergence itself is acclaimed-normal and well-motivated; the only real defect is that principle #5 ("Pool = Attribute + History") is now **stale & undocumented as an intentional exception** for combat. **Reclassify** from "lateral structural failure" to "documentation/intent gap — scope principle #5 (siblings yes; combat = History-pool + Agility-leverage)." `[SELF-CHECK: Turn-2 stated this slightly too hard; precedent says combat divergence is fine if intended. Calibrated down.]`

---

## Net effect on the Turn-2 verdict (carried to Turn 5)
| Turn-2 finding | Comparative outcome |
|---|---|
| Recall = AUDIT/FOLD | **Strongly validated** — fold; History-gating carries "what you know" (DE/Darklands) |
| Bonds = KEEP | **Validated** — Persona/FE relationship-capacity pattern |
| [P1] roster structure unresolved | **Validated + sharpened** — commit to WoD-3×3 *or* flat-7 (both acclaimed) |
| §1 one-attribute principle violated | **Reframed** — multi-attribute derivation is acclaimed-normal; retire §1's purist rule, don't revert formulas |
| Spirit overload / asymmetry | **Validated** — D&D Con/Dex over-centralization anti-pattern |
| Lateral combat-vs-sibling S-flag | **Softened** — acclaimed-normal; downgrade to a documentation/intent gap |

**Headline:** held to the standard of the very games Valoria cites as referents, the **core diagnosis survives** — Recall is the weak stat (fold), Bonds is sound (keep), the roster must commit to one architecture, and the Spirit/Recall asymmetry is a real balance defect. Two findings are **recalibrated honestly**: the §1 violation is the *rule's* fault (fix toward acclaimed multi-input derivation), and the combat-vs-sibling split is acclaimed-normal (downgrade to documentation).

`[GAP: exact per-game mechanics stated at the level of settled design knowledge; not retrieved. None load-bearing beyond the pattern level.]`
