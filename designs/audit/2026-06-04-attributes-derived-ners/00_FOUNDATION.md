# Valoria — Character Attributes & Derived Stats · NERS Audit · FOUNDATION (Turn 1 of 5)

**Date:** 2026-06-04 · **Status:** substrate for the 5-stage audit — **not** a verdict.
**Bootstrap token:** session-confirmed (audit gate passed). All claims carry file+section.

---

## 0 · Scope & interpretation
- **"Character attributes"** = personal-scale base parameters (1–7 integer stats); the *roll inputs*.
  `[ASSUMPTION: "character" = personal scale — basis: the phrase, and that faction base stats (Military/Stability/…) are a separate roster. Faction stats are touched only where derived stats bridge scales (they feed the Instance-B Domain resolver).]`
- **"Derived stats"** = the `derived_stats_v30` system (resources + cross-scale derived values); by its own §Scope it spans personal/unit/settlement/faction.
- **"All directions"** (canon term) = top-down · bottom-up · vertical · diagonal · lateral · horizontal — applied explicitly in Turn 2.

## 1 · Corrected methodology — DUAL-INSTRUMENT (load-bearing)
The **canonical** `valoria-resolution-diagnostic` SKILL (fetched this session, 36.7k chars — substantially evolved past the stale project-file copy) carries an explicit **SCOPE GATE**: character sheets, static stat blocks, **base parameters (1–7 = "roll inputs")**, and **continuous resources** are *OUT OF SCOPE* and route to `valoria-mechanic-audit`. It verdicts **rolling engines only**, against five properties **P-i** legible odds / **P-ii** in-band uniform leverage / **P-iii** bounded+monotonic / **P-iv** graded+recoverable / **P-v** right-engine-for-regime — via **Instance A** (sigma-leverage continuous), **Instance B** (deterministic+stochastic resolver), **Instance C** (new).

So a methodologically-honest "NERS audit of attributes & derived stats" is **two instruments**:
- **(A) STRUCTURAL NERS** of the roster + derived-stat system — redundancy, role-conflation, coverage/orthogonality, cross-scale smoothness, elegance, formula robustness → `mechanic-audit` Modes A–E + direct NERS. **This is the bulk of the answer.**
- **(B) ENGINE-FITNESS** only where attributes feed a draw — personal combat exchange + social contest exchange (**Instance A**); faction Domain resolver (**Instance B**, faction-fed, adjacent) → the Property Test. Confirms attributes-as-*inputs* don't break engine properties.

Forcing a rolling-engine verdict onto a stat block is **explicitly forbidden** ("Do not manufacture a NERS verdict for a non-rolling system").

## 2 · Canonical NERS criteria + a DRIFT finding
`[DRIFT: canon/definitions.yaml — both skills cite it as the NERS-criteria source; the file does NOT exist (canon/ listing confirms: no definitions.yaml). Operating from PI <canon_terms><definitions> (authoritative governance copy) + canon/00_philosophical_foundations_rules.md. Surface for fix / promotion.]`

NERS in use: **N** can't be removed without worsening play · **R** holds at extremes, complete/error-free, enables strategy + customization · **S** clean cross-scale, methodology consistent with sibling systems, no friction at category boundaries · **E** logically simple, intuit complex outcomes from simple choices.

13 foundational principles (mechanic-audit Mode E) — directly attribute-bearing: **#4 Histories-not-Skills**, **#5 Pool = Attribute + History bonus**. `[GAP: full 13-list not re-read from 00_foundations_rules this session → Turn 2.]`

## 3 · Phase-0 decomposition (rolling vs non-rolling)
| Component | Kind | In resolution-diagnostic scope? | Engine / route |
|---|---|---|---|
| Base attributes (1–7) | roll INPUT / static | **No** — recognize | → mechanic-audit |
| Personal combat exchange | rolling | **Yes** | Instance A (~5–18D) |
| Social contest exchange | rolling | **Yes** | Instance A — **but see §5 tangle** |
| Faction Domain action | rolling | Yes (adjacent, faction-fed) | Instance B (ratified ED-874) |
| Derived resources (Vitality, Stamina, Composure, Concentration, Thread Fatigue) | continuous resource feeding rolls | **No** — recognize | → mechanic-audit + balance |
| Derived deterministic (faction Income/Drain, Disposition cap, TroopCount scaling) | deterministic-accounting | **No** | → mechanic-audit |
| Cross-scale bridges (§10) | deterministic | **No** (loops checked only where a roll sits in the cycle) | → mechanic-audit |

## 4 · Attribute inventory (bottom-up)
`[FINDING-SEED S/E: there is NO single canonical attribute-roster doc. Attributes are defined across ≥3 places — combat prototype combatant.py, contest params, derived_stats — with no unified table. document_consolidation candidate.]`

| Attr | Abbr | Range | Feeds (cited) | Currency |
|---|---|---|---|---|
| Strength | str | 1–7 | combat (combatant.py L56–60) | live (combat engine v1 active) |
| Agility | agi | 1–7 | combat; sources poise/`balance_eff` (ability_armature L66,72) | live |
| Endurance | end | 1–7 | WoundTracker (combatant.py L70); Take-a-Breath stamina (csr L140) | live |
| Cognition | cog | 1–7 | Argue(Expert/Panel) `Cog×2` (contest.md L18,21) | live (combat+contest) |
| Attunement | att | 1–7 | Argue(No-adjud) `Att×2`; Appraise `Att+Recall`; Read; First-to-Speak; prep (contest.md L20,22,24,64) | live |
| Spirit | spirit | 1–7 | combat; Sincerity Gate `Spirit TN7` (csr L179) | live |
| Focus | focus | 1–7 | combat; coalition pool `Focus+Recall` (contest.md L173) | live |
| Charisma | Cha | 1–7 | Argue(Crowd) `Cha×2`; Composure `= Cha+6` (contest.md L19,3) | live |
| **Recall** | Rec | 1–7 | *contest [tangled — §5]:* Appraise, coalition, `+2D` bonus (contest.md L22,23,173); *live:* Recall-gated equip slots (character_histories_v30_index L16) | **CONTESTED** |
| **Bonds** | — | 1–7 | Disposition cap `floor(Bonds/2)+1` (derived_stats §10.1); Knots pool `(Bonds×2)+3` (csr L219); Socializing (csr L179); Corroborate `Bonds≥3/4 →+1D` (contest.md L78) | **live (non-contest); contest role tangled** |
| Disposition | disp | 1–7 (4=neutral) | aggression/temperament AXIS — combat lean `(disp−4)/3`; social Disposition track (combatant.py L62) | live — `[ROLE-SEED: an axis, not an allocated attribute]` |

(csr = `designs/architecture/complete_systems_reference.md`)

## 5 · Version tangle (MAJOR finding-seed) + currency
**Social contest has THREE overlapping specs:**
1. `params/contest.md` (v2.1-PP235, last_updated **2026-04-04**) — Cognition/Charisma/Attunement/Focus/**Recall/Bonds**; Appraise, Corroborate. **The only place Recall & Bonds act as CONTEST attributes.**
2. `designs/scene/social_contest_v30.md` ("v2", **CANONICAL**, approved 2026-04-17) — **Composure + Conviction** model (per the groundup TERMINOLOGY.md); its index shows **0** Recall/Bonds.
3. `designs/audit/2026-06-03-contest-groundup/` (**RATIFIED 2026-06-03**, Jordan-vetoable, **not yet promoted** to canonical_sources) — venue-determined, **pisteis(ethos/pathos/logos)+Standing** engine; uses **neither** the contest.md attributes **nor** Composure/Conviction; "faction stats/dispositions not yet wired."

**Implication for the worry:** Recall's and Bonds' **contest** roles sit on the *oldest* (contest.md) model, absent from both the canonical v30 and the ratified groundup. Surviving live justification:
- **Bonds** → Knots / Disposition cap / Socializing (derived_stats + csr, canonical) = **LIVE, non-contest.**
- **Recall** → equip-slot gating (character_histories, canonical) = **LIVE**; its contest roles = **likely superseded.**

**Combat:** `combat_v30` + ratified **`combat_engine_v1`** (active handoff) + `2026-06-02-combat-engine` ratification/deprecation proposal. Attribute set `{str,agi,end,cog,att,spirit,focus}` (combatant.py); former `balance` stat **removed** → Agility (ability_armature L66,72).
**`derived_stats_v30`: STATUS = PROPOSAL** ("supersedes prior derived_stats_v30.md") — audit it *as a proposal*, not ratified canon.

## 6 · Prior-audit reconciliation map (reconcile at Turn 5 — document_consolidation; do not duplicate/contradict)
- **Prior character audits:** `2026-05-08-character-mechanics-critical-audit.md` · `2026-05-08-character-generation-audit.md` · `character_histories_audit_2026-05-07.md`
- **Comparative (feeds Turn 3):** `2026-05-08-comparative-audit-faction-vs-character.md` · `faction_stats_renaissance_review.md`
- **All-directions NERS templates:** `2026-05-16-faction-ners-all-directions.md` · `tests/audit/all_directions_ners_v27.md` · `tests/audit/pp717_ners_all_directions.md`
- **Contest:** `2026-06-03-contest-groundup/{AUDIT,AUDIT_CRITIQUE,AUDIT_RECONCILED,HISTORICAL_VALIDATION}` · `2026-06-01-contest-redesign/RATIFIED`
- **Combat:** `2026-06-02-combat-engine` · `2026-05-31-percell-combat` · `2026-05-29-combat-armature`
- **R/S/E:** `valoria_rse_critique.md`
- `[ANOMALY: mass_battle_breakthrough_validation_2026-06-05.md is dated 2026-06-05 — after today (2026-06-04). Do not rely on; flag.]`

## 7 · Deferred to Turn 2 (the diagnostic)
- Exact derived-stat **formulas** (Vitality, Stamina, Composure, Concentration, Thread Fatigue) via `fetch_system(depth='full')` — index-routing blocked `read_sections` this turn.
- `params/core.md` continuous engine + continuity correction + degrees + pool floor. `[SEED: mechanics_index says "Pool floor 5"; the resolution-diagnostic skill says "Pool floor 1D" + a "~5D" continuity boundary — possible drift to check.]`
- The 13 foundational principles (`00_philosophical_foundations_rules.md`).
- Prior-audit **verdicts** (read the on-point priors above).
- Current **combat** attribute spec (the 2026-06-02 ratification proposal).
