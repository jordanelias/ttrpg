# Faction Mechanics — All-Directions NERS Audit

**Date:** 2026-05-16
**Status:** Audit output (PROVISIONAL — open for review)
**Session token:** 6232e49df2a65320
**Scope:** PP-686 v2 faction behavior architecture and the encompassing faction layer
**Framework:** NERS (per PI `canon_terms`) = N + Q tiers; full Class A vetting (N → Ω → Μ → М → Τ → Q) applied where research surfaces direct concerns

---

## §0 Audit context

**Trigger:** Jordan request — consolidate 4-turn research on Renaissance political mechanics, identify throughlines and meta-throughlines, evaluate against faction mechanics, NERS-audit all directions for symmetric and asymmetric variants.

**Research basis:** four prior turns of historical research covering: mechanisms of power and family influence; royal courts and succession; royal land acquisition; intra-realm land transfers; private noble war and the civil-war threshold; secession; decolonization; caste systems; church suppression and Protestant/Catholic dynamics; resistance/nationalist/populist movements; movement-to-legitimacy transitions; parliamentary mechanisms; treaties; negotiations; diplomacy. Synthesis derived 10 research throughlines (T-R-1..10) and 5 meta-throughlines (M-R-1..5) in Pass 1.

**Six directions audited** (per PI `canon_terms`): top-down, bottom-up, vertical, diagonal, lateral, horizontal.

**Symmetric/asymmetric framing:** explicitly requested; verdict in §5.6 H-1.

**Evidence base — files read this session** (cite source for every mechanical claim per audit gate):
- `designs/provincial/faction_behavior_v30.md` — §1–§3 read in full; §4–§8 surveyed (538 lines)
- `params/factions/stats_1_7_scale.md` — headers + key sections
- `designs/provincial/faction_layer_v30_index.md` — full
- `designs/provincial/factions_personal_v30_index.md` — full
- `designs/provincial/faction_politics_v30_index.md` — full
- `designs/provincial/faction_succession_split_v30_index.md` — full
- `designs/provincial/victory_v30_index.md` — full
- `designs/provincial/ci_political_v30_index.md` — full
- `designs/provincial/fractional_province_ownership_v30_index.md` — full
- `designs/architecture/scale_transitions_v30_index.md` — full
- `designs/territory/valoria_political_hierarchy_v30.md` — full
- `params/factions.md` — full
- `canon/02_canon_constraints.md` — full P-01..P-15
- `references/throughlines_meta.md` — full (N → Ω → Μ → М → Τ → Q + 11 М)
- `references/canonical_sources.yaml` — grep + system listing
- `skills/valoria-mechanic-audit/SKILL.md` — full
- `tests/audit/all_directions_ners_v27.md`, `tests/audit/pp717_ners_all_directions.md`, `tests/audit/engine_ners_2026-05-15.md` — format references
- `designs/audit/faction_stats_renaissance_review.md` — full (prior decision context)
- `designs/audit/2026-05-08-comparative-audit-faction-vs-character.md` — surveyed

**Files NOT deep-read this pass** (gap acknowledgments for confidence calibration): `designs/provincial/factions_personal_v30.md` (full doc, index only), `designs/provincial/faction_politics_v30.md` (full doc, index only), `designs/provincial/faction_layer_v30.md` (full doc, index only), `designs/provincial/victory_v30.md` (full doc, index only), `designs/provincial/ci_political_v30.md` (full doc, index only), PP-687 `key_substrate_v30.md`, PP-684 `conviction_taxonomy_v30.md`, `references/throughlines_complete.md`.

---

## §1 What the system is

Per `faction_behavior_v30.md §1` (PP-686 v2 canonical):

A faction's behavior is determined by four interacting components:
1. **Mission** — authored telos with primary objective, beneficiary, aligned/contradicted DA categories. Shifts under defined triggers (`§3.1`).
2. **Cascade** — modus derived from leader Convictions via α-weighted hierarchical blending across `organizational_hierarchy` supervisor edges (`§3.2`).
3. **Public Expectation** — populace expectation, Conviction-shaped, derived from role + Mission consistency (`§3.3`).
4. **Legitimacy + Popular Support** — separately tracked acceptance (0..7) and active backing (0..7) modulating Public Expectation strictness (`§3.4–3.5`).

Domain Action Ob is computed from action alignment across all four (`§3.7`). Mandate retained as derived value during transition (`§4`).

**Stat surface** (`params/factions/stats_1_7_scale.md`): seven faction stats on 1–7 scale — Legitimacy / Popular_Support / Influence / Wealth / Military / Intel / Stability (per PP-686 v2; Mandate split into Legit+PS; Intel restored per `faction_stats_renaissance_review.md` recommendations).

**Role enumeration** (`faction_behavior_v30 §2`): `sovereign / ecclesiastical / mercantile-procedural / intelligence-diplomatic / reformist / military-order`.

**Unique Actions per faction** (`stats_1_7_scale §Unique Actions — All Factions (PP-168)`): Crown = Royal Decree · Church = Excommunication, CI 60 Territorial Seizure · Hafenmark = Sovereign Authority Doctrine · Varfell = The Private Collection · Guilds = Economic Leverage · Löwenritter = Martial Law / Coup Trigger.

**Supporting layers:** CI (peninsular religious authority, `ci_political_v30`); VTM (Varfell-specific); WC; Accord; succession-split mechanics (`faction_succession_split_v30`); fractional province ownership; scale-transitions across personal ↔ settlement ↔ territory ↔ peninsula.

---

## §2 Research throughlines applied to canon

Each maps a research throughline (T-R-N) onto the canon. Verdict: ALIGNED / PARTIALLY ALIGNED / GAP.

### T-1. Power is plural — composite assembly required
**Research basis:** T-R-1 (multi-vector power), T-R-7 (turn-on-you modes), M-R-1 (composability).
**Canon position:** Seven-stat surface covering distinct power vectors; role-specific Unique Actions adding asymmetric mechanism access; Mission/Cascade providing telos-derived modulation atop stat values (`faction_behavior_v30 §1`).
**Verdict:** **ALIGNED.** Architecture explicitly resists single-vector dominance via the four-component composite.

### T-2. Legitimacy and coercion are co-constitutive
**Research basis:** T-R-2.
**Canon position:** Legitimacy is a tracked 0–7 stat with `procedural events` (build) and `violation events` (erode) per `faction_behavior_v30 §3.5`. Military is separately tracked. Interaction routed through Public Expectation Strictness (`§3.6`) and Domain Action Ob (`§3.7`).
**Verdict:** **PARTIALLY ALIGNED — see A-1.** Parallel scalars; combined-dynamic (the Henry-VII / Louis-XI / Ferdinand consolidator profile that requires both axes; single-axis-strong fails) lacks explicit interaction rule.

### T-3. Centralization rewrites what was lawful
**Research basis:** T-R-3, M-R-5.
**Canon position:** Mission can shift via four triggers (`§3.1`: victory-track milestone, succession in contested/emergency/imposed modes, ≥4 consecutive Mission-contradicting outcomes, authored). Mission-shift causes `da.aligned/contradicted` interpretations to recompute — same DA can flip legitimate↔illegitimate per faction state.
**Verdict:** **PARTIALLY ALIGNED — see A-7.** Mission-shift produces *within-faction* category mutation. **Inter-faction / regime-level** category mutation (private war → treason as crown centralizes) is structurally absent.

### T-4. Faction is the unit; institutions are arenas
**Research basis:** T-R-4, M-R-3.
**Canon position:** Factions are first-class agents with state. Institutions appear as CI track (peninsular religious authority — arena), victory tracks (`victory_v30`), the political hierarchy (`valoria_political_hierarchy_v30` — structural map).
**Verdict:** **PARTIALLY ALIGNED — see A-2.** Factions-as-actors canonical. Arenas-as-capture-targets uneven: CI genuinely contestable; political hierarchy itself appears structurally fixed.

### T-5. Recognition as substrate-state constitution
**Research basis:** T-R-5, candidate М-13.
**Canon position:** Legitimacy stat exists, distinguishes procedural Legitimacy from active Popular_Support. Excommunication-affects-Legitimacy (Church Unique Action per `stats_1_7_scale §Church`) is the closest existing primitive to recognition-as-constitution.
**Verdict:** **PARTIAL — see A-8.** Dynamic partially captured via Excommunication-affects-Legitimacy and Mission references to legitimating sources. **Systemic recognition graph** (each faction tracks whom it recognizes; recognition has mechanical weight as substrate-state) not present.

### T-6. Time horizons mismatch by mechanism
**Research basis:** T-R-6.
**Canon position:** Faction state has authoring-time elements (Mission, role, hierarchy), per-Accounting derived state, event-driven stateful updates. Scale-transitions handle season-vs-scene. Succession-split introduces longer-horizon dynastic effects.
**Verdict:** **ALIGNED for season-to-Accounting cycle. See A-3 for multi-season generational compounding gap.** Multi-season / generational (Habsburg marriage-compounding pattern: small dynastic moves compounding over decades) is weakly represented. Succession-split is event-driven, not slow-accumulation.

### T-7. Every tool can be turned against the user
**Research basis:** T-R-7, M-R-1.
**Canon position:** Mission-shift trigger 3 (`≥4 consecutive seasons of Mission-contradicting outcomes`) and Cascade re-resolution (`§3.2.4`) provide *internal* self-degradation. Public Expectation Strictness (`§3.6`) means tightening role-expectation can backfire on deviation.
**Verdict:** **PARTIALLY ALIGNED — see A-4.** Self-undermining via Mission drift captured. Tool-becomes-threat (standing army → coup; bureaucracy → independent power; church → legitimating rebellion) captured only via Löwenritter's Martial Law / Coup Trigger. Crown bureaucracy, Church institutional independence, Hafenmark mercantile-network turn-on-you modes — none have analogous mechanics.

### T-8. Information asymmetry is the substrate
**Research basis:** T-R-8, M-R-4.
**Canon position:** Intel restored as 7th stat per PP-686 v2. Spy actions with Ob formulas referencing Intel. CI partially observable. P-03 (Rendering = consciousness-performed) and Μ-γ make information asymmetry foundational.
**Verdict:** **ALIGNED conceptually — see A-5.** Strategic-fog default-hidden faction-stat visibility unverified at this fetch depth.

### T-9. Crises rewrite the rulebook
**Research basis:** T-R-9.
**Canon position:** Succession-split (`faction_succession_split_v30`), royal-assassination-fuse (`params/bg/royal_assassination.md`), CI Passive Advance with CI 60 territorial seizure (`stats_1_7_scale §CI Passive Advance (PP-402)`), peninsular_strain, crisis-bypass rule (`faction_behavior_v30 §3.2.5`).
**Verdict:** **ALIGNED.** Crisis dynamics first-class. Rulebook-rewriting (peninsular-scale shifts to allowed action-space, Reformation-class events) less developed than per-faction Mission-shift.

### T-10. Coalition cost rises with size
**Research basis:** T-R-10.
**Canon position:** Faction politics references alliance mechanics per `faction_politics_v30` index headers; cost structure opaque at index-only depth.
**Verdict:** **UNVERIFIED — see A-6.**

---

## §3 Meta-throughlines

Pass 1 M-R-1..5 retested against canon:

| Meta-T | Mapped canonical М | Coverage | Gap |
|---|---|---|---|
| M-R-1 Composability beats specialization | М-7 + М-11 | Strong via role asymmetry + Cascade + Unique Actions | Asymmetric *vulnerability* axes underspecified (T-7 / A-4) |
| M-R-2 Legitimacy as substrate-state | М-3 + М-4 | Partial — Legitimacy is stat, not substrate-position | Recognition graph absent (T-5 / A-8 / candidate М-13) |
| M-R-3 Arenas as capture targets | М-4 | Partial — CI is contestable arena; political hierarchy is fixed | Constitutional-level mutation absent (T-4 / A-2) |
| M-R-4 Information asymmetry is substrate | М-3 + М-8 + P-03 | Strong if strategic-fog confirmed | A-5 to verify |
| M-R-5 Regime-relative legality / category mutation | — (candidate М-12) | Within-faction via Mission-shift; cross-faction absent | T-3 / A-7 / candidate М-12 |

**Two genuine gaps surface as absence of meta-pattern, not under-coverage of existing М**: candidate М-12 (regime-relative category mutation), candidate М-13 (recognition substrate). Both flagged to Jordan; not autonomously added (authority §10 of `throughlines_meta`).

---

## §4 NERS scorecard per throughline

4-point: ✓ strong / ◐ partial / ◯ weak / − gap. NERS per PI `canon_terms`: N necessary, R robust, S smooth, E elegant.

| T | N | R | S | E | Notes |
|---|---|---|---|---|---|
| T-1 Plural power | ✓ | ✓ | ✓ | ◐ | E: seven-stat surface + role + Mission/Cascade is a lot of authored input |
| T-2 Legit + coercion | ✓ | ◐ | ◐ | ◐ | Parallel scalars vs combined dynamic — A-1 |
| T-3 Centralization rewrites legal | ✓ | ◐ | ◯ | ◯ | Load-bearing Renaissance dynamic structurally absent — A-7 |
| T-4 Faction as unit | ✓ | ✓ | ◐ | ◐ | Political hierarchy fixed — A-2 |
| T-5 Recognition substrate | ✓ | ◐ | ◯ | ◯ | Distributed across primitives — A-8 / М-13 |
| T-6 Time horizons | ✓ | ◐ | ✓ | ✓ | Generational compounding weak — A-3 |
| T-7 Tool turns on user | ✓ | ◐ | ◐ | ◐ | Only Löwenritter clean — A-4 |
| T-8 Information asymmetry | ✓ | ✓ | ✓ | ✓ | Pending A-5 |
| T-9 Crisis rewrites rulebook | ✓ | ✓ | ◐ | ◐ | Per-faction yes, peninsular no |
| T-10 Coalition cost | — | — | — | — | Unverified — A-6 |

**Aggregate:** N uniformly ✓. R next strongest. S and E show systematic ◐/◯ on cross-faction/constitutional dimensions (T-3, T-4, T-5).

---

## §5 Six-direction audit

### §5.1 Top-down — from victory conditions back to mechanic

Victory chain per `victory_v30_index.md`: multi-path. Mission-shift trigger 1 (victory-milestone) closes the loop victory → Mission → action alignment → DA Ob → seasonal outcomes → next-season state.

**T-D-1 (P3):** Non-victory faction continuation path not visible. Mission-shift trigger 3 (mission-failure threshold) handles partial decay; *victory-impossibility persistence* (Holy Roman Empire as working entity centuries past peak) — needs verification via `victory_v30` full read. Folds into A-11.

### §5.2 Bottom-up — from primitives up

Primitives: PP-684 Conviction taxonomy, PP-687 Key substrate, seven faction stats, NPC state, supervisor edges, role enumeration. Up-chain: primitives → cascade math (`§3.2.3`) → aggregate effective convictions → expected convictions → strictness → DA Ob.

**T-D-2 (P3):** Chain rigorous *given* the conviction/key substrate. **Cannot fully verify without reading PP-687 and PP-684 files.** `[GAP: PP-687 key_substrate, PP-684 conviction_taxonomy not fetched.]`
**T-D-3 (P2):** Cascade math (`§3.2.3` α-weighted hierarchical blending) not formula-validated at full depth. Closure for edge cases (single-leader no-supervisor; all-cascade-roots) needs Mode-A check on §3.2 full content.

### §5.3 Vertical — scale transitions

`scale_transitions_v30` first-class. Down-scale: faction state → DA Ob in scene contexts. Up-scale: peninsular CI affects all factions. **V-1 (P2):** Lateral-within-scale (faction A vs faction B at same scale) less directly addressed — partially overlaps A-2. **V-2:** Fractional province ownership = multi-faction territorial competition without binary control flips. Matches Renaissance overlapping-jurisdiction reality. ✓ ALIGNED.

### §5.4 Diagonal — cross-system interactions

Faction layer × Thread substrate × military × CI × victory × scale-transitions. Key emit/consume via subscription pattern (`§5.1–5.3`).

**D-1 (P2):** Key emit/consume powerful; introduces **dependency risk** when key registry changes. Bootstrap `[FRESHNESS ⚠] 4 stale canonical source(s)` confirms active risk. → A-10, A-12.
**D-2 (P1 candidate):** P-01 Inseparability (`02_canon_constraints §P-01`) requires every thread operation to produce automatic effects in all three dimensions (temporal CD, epistemic certainty, actualized d6 consequence table). Faction DA Ob calculation (`§3.7`) does not explicitly engage three-dimensional structure. **If faction DA is a thread operation per P-14 (Board/VG modes must express inseparability), this is a constraint violation.** → A-9.

### §5.5 Lateral — peer-system parity

Settlement_layer, military_layer, CI political, faction politics. **L-1 (P2):** Per ED-830 (2026-05-15), `derived_stats_v30 §14` 4-bucket taxonomy (Derived Values / Tracks / Clocks / Pools) is authoritative engine-value map. Faction stats need explicit bucketing — `stats_1_7_scale` terms them "stats" but Legitimacy has build/erode dynamics suggesting track-like behavior. → A-14.
**L-2:** Combat/mass_combat 1–7 dice; faction stats 1–7. ✓ ALIGNED.

### §5.6 Horizontal — within-system consistency across roles + symmetric/asymmetric verdict

**H-1 SYMMETRIC/ASYMMETRIC VERDICT (user-requested):**

The architecture is **hybrid asymmetric**:
- **Symmetric layer:** seven-stat surface, four-component model (Mission/Cascade/Public Expectation/Legit+PS), Accounting cycle, DA Ob calculation pattern.
- **Asymmetric layer:** role enumeration (six distinct roles); Unique Actions per faction (Crown Royal Decree, Church Excommunication and CI Territorial Seizure, Hafenmark Sovereign Authority Doctrine, Varfell Private Collection, Guilds Economic Leverage, Löwenritter Martial Law / Coup Trigger); starting stat distributions; role-specific tracks (CI for Church, VTM for Varfell, WC, Accord).

This is the **canonical Renaissance-faithful design**: the Medici, Papacy, French Crown, Hanseatic League all played the same game (Mission/Legitimacy/Wealth/etc.) but with deeply asymmetric mechanism access.

- **Pure symmetric** (same stats, same actions, only values differ) → fails М-4 (reskinned attractor failure per `throughlines_meta §7 Failure Lexicon`).
- **Pure asymmetric** (no shared mechanics) → fails Q-smooth (no comparable methodology).
- **Hybrid asymmetric** → right.

**Verdict: ALIGNED with research.** This is one of the strongest architectural elements; preserve. Document as design intent per A-13.

**H-2 (P2): Asymmetric vulnerability gap.** Per T-7, asymmetric *trump-tool* dimension is well-served by Unique Actions; asymmetric *vulnerability* dimension is underserved. Each role should have an analog to Löwenritter's coup-trigger:
- **Sovereign (Crown):** bureaucracy-independence threshold; standing-army coup. Underspecified.
- **Ecclesiastical (Church):** Reformation-class schism trigger; CI ≥ X → internal schism. Underspecified.
- **Mercantile-procedural (Hafenmark):** wealth-accumulation → oligarchic capture. Underspecified.
- **Intelligence-diplomatic (Varfell):** intel dominance → paranoid purges. Underspecified.
- **Reformist (Restoration Movement):** movement-success → institutional rigidity. Underspecified.

**P2.** Research-grounded gameplay: Renaissance powers all had failure-via-success modes. → A-4.

---

## §6 Tier application (Class A full vetting)

| Tier | Verdict | Evidence |
|---|---|---|
| **N** Necessity | PASS | All 10 research throughlines map to load-bearing Renaissance dynamics. Per-finding N flags: A-7, A-8 (load-bearing dynamics structurally absent — candidate М-12/М-13). |
| **Ω** Intent | PASS | Ω-a cross-scale: scale_transitions + fractional_province + CI. Ω-b personal transformation: faction state shifts engage character convictions via PP-684 substrate. Ω-c autonomous events: Mission-shift triggers + crisis-bypass + CI Passive Advance fire without player action. Ω-d irreducible tradeoff: Strictness × Mission alignment produces tradeoffs. |
| **Μ** Modes (ratings) | NO FAILURES | Μ-α +, Μ-β ✓, Μ-γ ✓, Μ-δ ✓. |
| **М** Meta-throughlines (ratings) | NO FAILURES per §3 rubric; one ◐ (М-11 redesign-or-tradeoff-document for A-4) | М-1 +, М-2 ✓, М-3 ✓, М-4 +, М-5 ✓, М-6 +, М-7 +, М-8 ✓, М-9 ○, М-10 ✓, М-11 ◐. Candidates М-12, М-13 flagged. |
| **Τ** Throughlines | UNDERVERIFIED | `references/throughlines_complete.md` not fetched. **P3 — deferred Τ-tier walk.** |
| **Q** Quality | PASS w/ reservations | See §9 system-level verdict. |

---

## §7 Mode B — number-system coherence

Faction state ranges per `faction_behavior_v30 §2`:

| Field | Range | Scale type | Status |
|---|---|---|---|
| legitimacy | 0..7 | standard stat, 0-floor | OK |
| popular_support | 0..7 | standard stat, 0-floor | OK |
| mandate | 0..7 | derived stat, 0-floor | OK |
| influence / wealth / military / intel / stability | 1..7 | standard stat, 1-floor | OK; asymmetric floor vs Legit/PS — see B-2 |
| cascade_fidelity | -1..+1 | centered deviation | OK; documented |
| strictness | 0..1 | unit interval / probability | OK; documented |
| institutional_culture | -0.2..+0.2 | small α-adjustment | OK; documented |

**B-1 (P3, polish):** Architecture mixes scale *types* (standard, centered deviation, unit interval, α-adjustment). Principled but typology not named explicitly. Per ED-830, faction-state fields need bucketing against `derived_stats_v30 §14`. Folds into A-14.

**B-2 (P3):** 0-floor vs 1-floor split is principled: 0-floor stats (Legit, PS, mandate) are erodable to zero with mechanical consequence (procedural acceptance fully revoked); 1-floor stats (Influence, Wealth, Military, Intel, Stability) are persistent. Document as design principle: *"0-floor stats are erodable; 1-floor stats are persistent."*

---

## §8 Consolidated findings (A-1 through A-17)

Severity per audit skill: P1 (blocks play / canon violation) · P2 (causes ambiguity / important gap) · P3 (polish / verification).

| ID | Sev | Source | Finding | Recommendation |
|---|---|---|---|---|
| A-1 | P2 | T-2 / §4 | Legitimacy and Military are parallel scalars; combined-dynamic absent | Specify Legitimacy × Military interaction in DA Ob or as combined gating |
| A-2 | P2 | T-4 / V-1 / §5.6 | Political hierarchy in `valoria_political_hierarchy_v30` structurally fixed; not faction-capture-target | Specify hierarchy positions contestable by factions vs. authored-fixed |
| A-3 | P3 | T-6 | Generational / dynastic compounding (decade-scale) weakly represented | Slow-burn dynastic-claim accumulator OR document campaign-time-horizon scope deliberately |
| A-4 | P2 | T-7 / H-2 | Five of six roles lack turn-on-you mechanism analog to Löwenritter coup-trigger | Add asymmetric vulnerability per role (bureaucracy-independence, schism, oligarchic capture, paranoid purge, institutional rigidity) |
| A-5 | P3 | T-8 | Default visibility of faction stats to other factions unverified | Verify against `faction_politics_v30` full content; consider strategic-fog per `faction_stats_renaissance_review` |
| A-6 | P3 | T-10 | Coalition cost structure unverified | Read `faction_politics_v30` full content for alliance mechanics |
| A-7 | P2 | T-3 / M-R-5 | Cross-faction regime-level category mutation (private war → treason as crown centralizes) absent — largest Renaissance dynamic structurally missing | **Decision Jordan:** admit candidate М-12 OR document scope-bound |
| A-8 | P2 | T-5 / М-13 | Recognition-as-substrate-state-constitution distributed; not named | **Decision Jordan:** admit candidate М-13 OR document distributed approach sufficient |
| A-9 | P1 candidate | D-2 / §5.4 | Faction DA Ob calculation may not honor P-01 Inseparability — if DA is thread operation per P-14, constraint violation | **Canon-check Jordan:** is Domain Action a thread operation? If yes, three-dimensional auto-effects must fire; current §3.7 doesn't show them |
| A-10 | P3 | D-1 | Key-substrate dependency risk; bootstrap `[FRESHNESS ⚠]` flag active | Run freshness_gate.py --update |
| A-11 | P3 | §5.1 | Post-victory-impossibility persistence path unverified | Read `victory_v30` full |
| A-12 | P2 | §5.4 / D-1 | Key emit/consume fragile on key-registry changes | Document key-registry-change protocol; verify subscription pattern (`§5.3`) handles missing key types gracefully |
| A-13 | P2 | §5.6 / H-1 | Hybrid asymmetric design correct but unnamed in `faction_behavior_v30` | Add §0 or §10 to `faction_behavior_v30` naming "hybrid asymmetric" as design intent |
| A-14 | P3 | §5.5 / L-1 / B-1 | Faction stats need explicit `derived_stats_v30 §14` 4-bucket placement | Add bucketing per ED-830 |
| **A-15** | **P2** | **outside-review** | **Wealth-generation mechanism absent from this audit's reads** (production rates, trade flows, tax infrastructure) | **Verify `params/factions.md` + `settlement_layer_v30` for production yields + `mass_battle_v30` upkeep drains; if absent, build a Wealth-generation specification** |
| **A-16** | **P2** | **outside-review** | **Church-as-territorial-power dimension underverified** (Papal States, prince-bishopric pattern) | **Verify `ci_political_v30` full + `valoria_political_hierarchy_v30` Church territorial entries** |
| **A-17** | **P3** | **outside-review** | **Offstage / extra-peninsular factional pressure not visible at this scope** | **Verify whether Valoria models offstage powers as authored pressure sources, NPC factions, or scenario events; flag for Jordan if absent by design** |

---

## §9 System-level NERS verdict

| Axis | Verdict | Basis |
|---|---|---|
| **N** Necessary | **PASS** | Architecture grounded in load-bearing Renaissance dynamics; N-tier questions answered affirmatively |
| **R** Robust | **PASS with reservations** | Multiple viable approaches per faction; visible state changes; player-independent scenarios. Reservation: A-4 asymmetric-vulnerability gap weakens failure-mode variety |
| **S** Smooth | **PARTIAL PASS** | Scale-transitions explicit; Accounting cycle clean; Key-substrate composes well. Reservations: A-1, A-2, A-9 |
| **E** Elegant | **PARTIAL PASS** | Core four-component model restatable. Second-order consequences require simulation; acceptable given subject grounding but tooltips/visualization must surface chain (Μ̄ concern) |

**Aggregate system verdict: PASS with 17 findings.** Architecture sound at framework level; gaps are in coverage breadth (A-4, A-7, A-8, A-15, A-16, A-17) and one P1-candidate canon-constraint compliance question (A-9).

---

## §10 Decisions flagged for Jordan

Per `throughlines_meta §10`, N/Ω/М-additions are Jordan-owned; Claude flags only:

1. **A-7 / candidate М-12 — Regime-relative category mutation.** Cross-faction rule-space mutation as a meta-throughline (vs. only within-faction via Mission-shift). Load-bearing Renaissance dynamic; structurally absent. Admit М-12, document distributed sufficiency, or scope-bound deliberately.
2. **A-8 / candidate М-13 — Recognition as substrate-state constitution.** Recognition graph as a substrate layer (vs. distributed across Excommunication / Mission / Legitimacy). Admit М-13, document distributed sufficiency, or scope-bound deliberately.
3. **A-9 / canon-check — P-01 Inseparability compliance.** Is Domain Action a thread operation under P-14? If yes, three-dimensional auto-effects must fire and `§3.7` DA Ob calculation needs to engage them; current absence is constraint violation. If no, no further action — but document the boundary.

---

## §11 Audit trail

```
[STAGE: pass_1_complete] — survey, research T/M synthesis, canonical mapping, M candidates flagged, Pass 2 plan
[STAGE: pass_2_open] — canon fetch (13 faction files + 6 prior audits)
[STAGE: canon_read] — faction_behavior_v30 §1-§3 + headers + indexes
[STAGE: pass_2_complete] — 14 findings, NERS scorecard, symmetric/asymmetric verdict
[STAGE: pass_3_open] — re-review, tier application catch-up, Mode B catch-up
[STAGE: pass_3_complete] — T-2 verdict correction; A-15/16/17 added; tiers Ω/Μ/М explicit; Mode B clean; Τ deferred (P3)
```

**Bias acknowledgments:**
- `[SELF-AUTHORED — bias risk]` T-R-1..10 are own synthesis; this audit applies own framework to canon. Pass 3 outside-reviewer pass surfaced 3 real findings (A-15, A-16, A-17) and 1 wording correction (T-2), indicating Pass 2 had moderate over-charity but not extreme.
- `[CONFIDENCE: medium-high]` overall, with `[GAP: PP-687 key_substrate, PP-684 conviction_taxonomy, full design docs for victory/factions_personal/faction_politics/faction_layer/ci_political not fetched]`. A-5, A-6, A-9, A-11, A-15, A-16 require these reads to upgrade verdicts.
- `[ASSUMPTION: PP-686 v2 PROVISIONAL canonical status accepted]` per file headers; treating as canonical for audit basis.
- `[DRIFT: long-deliverable — Pass 2 single-turn]` Acknowledged; fit. Per `<persistence_safeguards>` no actual single-turn enforcement.

---

## §12 Process notes for future audit work

This audit was produced via:
- Pass 1 (Pass 1 §A–§F in chat): research synthesis → throughlines → meta-throughlines → canonical mapping → Pass 2 plan with file fetch list
- Pass 2 (in-chat): canon fetch, audit prose, findings, NERS scorecard, symmetric/asymmetric verdict
- Pass 3 (in-chat): re-review, tier catch-up, Mode B catch-up, outside-reviewer pass, consolidation
- Committed file (this document): Pass 2 + Pass 3 consolidated; T-2 correction + A-15/16/17 added vs Pass 2 draft

**P1 finding (A-9 candidate) NOT yet appended to `canon/editorial_ledger.yaml`** because (a) editorial_ledger is in size violation per bootstrap COMPLIANCE warning — atomizer fix needed first; (b) A-9 is candidate-P1 pending Jordan canon-check decision. Recommended next step: run atomizer fix, then await Jordan decision on P-01 / DA-as-thread-operation boundary, then append if confirmed.
