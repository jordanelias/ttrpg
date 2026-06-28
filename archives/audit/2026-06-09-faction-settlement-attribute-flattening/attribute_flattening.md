# Faction / Settlement / Territory / Province — Attribute Flattening
**Audit deliverable · 2026-06-09 · scope: every faction/settlement/territory/province attribute + associated statistic**

Bottom-up flatten of all mechanically-meaningful uses of these quantities, classified **DEF** (defined / scale),
**WRITE** (set or delta'd), **READ** (consumed in a formula/check). Built to expose the structure and the
contradictions for analysis — it does not resolve them.

**Method.** Grepped the authoritative *defining* set (23 docs: `designs/provincial/`, `designs/territory/`,
`designs/scene/derived_stats`, `designs/factions/`, `designs/ui/`, key `params/bg` + `params/factions`),
keeping only lines with a mechanical token (`= ± → × ÷ |`, a digit, or stat/derived/scale/check keywords).
Per-quantity classification is heuristic (a WRITE pattern fires on `X -1 / X += / ±X / +N X / X→0 / set/gain/lose X`;
a DEF on a table row, `X = formula` LHS, or a stated scale). **Scope caveat:** downstream sims, `_infill`
companions, `factions_personal_v30 §8.1`, and clock/track subsystems (CI, MS, AP, PI, AER) were not separately
flattened — they are consumers, and the definitional contradictions live in the docs scanned here.

**Docs scanned:** `factions/faction_systems_overview_v30.md`, `prov/ci_political_v30.md`, `prov/faction_behavior_v30.md`, `prov/faction_canon_v30.md`, `prov/faction_layer_v30.md`, `prov/faction_politics_v30.md`, `prov/faction_state_authoring_v30.md`, `prov/fractional_province_ownership_v30.md`, `prov/military_layer_v30.md`, `prov/peninsular_strain_v30.md`, `prov/strategic_layer_v30.md`, `prov/victory_v30.md`, `scene/derived_stats_v30.md`, `terr/march_layer_v30.md`, `terr/settlement_adjacency_v30.md`, `terr/settlement_layer_v30.md`, `terr/territory_temperaments_v30.md`, `terr/valoria_political_hierarchy_v30.md`, `ui/valoria_ui_ux_supplement_derived_settlement.md`, `params/bg/faction_actions.md`, `params/bg/tracks.md`, `params/bg/victory.md`, `params/factions/stats_1_7_scale.md`


## 1 — Quantity map

| Quantity | Level | Type | Scale | Authoritative definition | Flag |
|---|---|---|---|---|---|
| **Legitimacy (L)** | settlement | **base** | 0–7 | `settlement_layer §1.8` (Jordan 2026-05-30); `faction_canon`, `faction_behavior` | ⚠ `derived_stats §14` calls it **derived** (`= Mandate×20`) |
| **Popular Support (PS)** | settlement | **base** | 0–7 | `settlement_layer §1.8` | aligned across docs |
| **Mandate** | faction | **derived** — size-weighted saturating aggregate of settlement L/PS (`q_s=0.5L+0.5PS`) | 0–7 | `settlement_layer §1.8`; `faction_canon §`; `faction_behavior §4` (LPS-2e) | ⚠⚠ `derived_stats §14` calls it **base**; written `±N`/`→0` in ≥6 docs; **read as d+σ input** `M=Mandate−2` |
| **Influence** | faction | base | 1–7 | `faction_canon`; `stats_1_7_scale` | → Reputation (`×15`) |
| **Wealth** | faction | base | 1–7 | `faction_canon`; `stats_1_7_scale` | → Treasury (`×100`) |
| **Military** | faction | base | 1–7 | `faction_canon`; `stats_1_7_scale` | → Levies Available (`×2`) |
| **Intel** | faction | base | 1–7 | `faction_canon`; `stats_1_7_scale` | no derived capital listed |
| **Stability** | faction | base | 0–7 | `faction_canon`; `stats_1_7_scale` | → Discipline (`×10`); 0 = collapse trigger |
| **Prosperity** | settlement | base | 0–5 | `settlement_layer` | → Local Economy (`×50`); `strategic_layer P-22` labels it "territory-level track" |
| **Defense** | settlement | base | 0–5 | `settlement_layer` | → Garrison Strength (`×20 + Fort×30`) |
| **Order** | settlement | base | 0–5 | `settlement_layer`; `peninsular_strain §` | → Public Order (`×20`); → Province Accord `= floor(mean Order)` |
| **Local Economy** | settlement | derived | `Prosperity×50` | `settlement_layer` | → faction Treasury |
| **Garrison Strength** | settlement | derived | `Defense×20 + Fort×30` | `settlement_layer` | written `+10/−10/→0` by combat |
| **Public Order** | settlement | derived | `Order×20` | `settlement_layer` | `<0` → riot events |
| **Treasury** | faction | derived | `Wealth×100` | `derived_stats §14` | ⚠ **also** fed by aggregated settlement Local Economy (double-source) |
| **Reputation / Levies / Discipline** | faction | derived | `Inf×15 / Mil×2 / Stab×10` | `derived_stats §14` | base→capital pattern (Mandate row is the broken one) |
| **Accord** | province / territory | track | 0–5 | `peninsular_strain §`; `settlement_layer §1.3` (`= floor(mean Order)`) | also written `±1` directly across many docs |
| **Temperament** | territory | descriptor | α (outcomes) + β (conduct) weights | `territory_temperaments §3.4.1`; `faction_canon §` | the 5-temperament table |
| **Fort Level** | settlement | base/modifier | — | `settlement_layer` | feeds Garrison Strength |
| **Population / Size** | settlement | base | type-tiered Weight | `settlement_layer §1.2/Weight` | feeds Mandate size-weighting |


## 2 — Derivation graph (flattened)

```
SETTLEMENT (base, per-settlement)         SETTLEMENT (derived)         FACTION (derived / aggregate)
  Legitimacy (L) 0-7  ─┐
  Popular Support 0-7 ─┴ q_s=0.5L+0.5PS ─(size-weighted, saturating)─▶ MANDATE 0-7
                                                                         ▲  ⚠ ALSO written ±N / →0 directly (≥6 docs)
                                                                         └─ ⚠ ALSO read as d+σ input: M = Mandate − 2
  Prosperity 0-5 ─────── ×50 ──────────▶ Local Economy ──(aggregate)──▶ faction TREASURY
  Defense 0-5 ─┐                                                          ▲  ⚠ ALSO defined Treasury = Wealth×100 (derived_stats §14)
  Fort Level ──┴──── ×20 + Fort×30 ────▶ Garrison Strength  ◀ written +10/-10/→0 by combat
  Order 0-5 ──────── ×20 ──────────────▶ Public Order  (<0 → riots)
  Order 0-5 ──────── floor(mean) ──────▶ PROVINCE ACCORD 0-5  ◀ ALSO written ±1 directly (many docs)

FACTION (base, 1-7)            FACTION (derived "capital", derived_stats §14)
  Influence ── ×15 ─▶ Reputation
  Wealth ───── ×100 ▶ Treasury   (double-sourced — see above)
  Military ─── ×2 ──▶ Levies Available
  Stability ── ×10 ─▶ Discipline
  Intel ──────────── (no capital)
  [Mandate is listed HERE as a base stat by derived_stats §14 — CONTRADICTED by LPS-2e;
   it belongs in the FACTION-derived column, fed by settlement L/PS.]
```


## 3 — Contradictions & tensions (worst first)

**[P1] C-1 Mandate derivation is inverted between docs.**
`derived_stats §14` L291: `Mandate (base) → Legitimacy = Mandate × 20`. LPS-2e (`settlement_layer §1.8`,
`faction_canon §`, `faction_behavior §4`, Jordan ruling 2026-05-30): Mandate is **derived** (aggregate of
settlement L/PS); Legitimacy is a **per-settlement base** stat. The derivation arrow is reversed. The faction
docs were migrated for LPS-2e; **`derived_stats §14` was not**. Only the Mandate→Legitimacy row of §14's
base→capital table is stale — `Wealth→Treasury`, `Military→Levies`, `Influence→Reputation`, `Stability→Discipline`
are correct (those are genuine base stats).

**[P1] C-2 Mandate is declared derived but is written and rolled as a base stat.**
Despite LPS-2e, Mandate is directly mutated in ≥6 canon docs — `faction_layer` (treaty breach −2, assassination −1,
collapse →0), `ci_political` (Govern +1, recovery +1, check-fail −1), `victory` (target −1, Crown +1, Church −2),
`strategic_layer` (Appease −1, collapse →0), `derived_stats §14` (campaign defeat −1, Turmoil −1) — **and read as a
d+σ resolver input** (`stats_1_7_scale`: Royal Decree `M=Mandate−2`, Excommunication `M=Mandate−target Mandate`).
A derived aggregate cannot simultaneously be a directly-written, directly-rolled base quantity. The LPS-2e ruling
declared the ontology but the **migration was never propagated to the mechanics**: every `Mandate ±N` either must
write the settlement L/PS sources, or Mandate needs a defined non-aggregate write path. This is the F1 defect at scale
(R4 will advise on each occurrence).

**[P2] C-3 Treasury is double-sourced.**
`derived_stats §14` L292: `Treasury = Wealth × 100`. `settlement_layer` L47/L51: settlement `Local Economy = Prosperity×50`
"contributes to faction Treasury." Two derivations; composition rule unstated (is faction Treasury `Wealth×100`, the
sum of settlement Local Economy, or both summed?).

**[P2] C-4 Faction-stat count: 6 vs 7.**
`faction_canon` L26/L39 flags "6-stat (`factions_personal §8.1`) vs 7-stat (`stats_1_7_scale` post-ED-787)"; yet
`stats_1_7_scale` L3 itself reads "Faction stats (6): Mandate / Influence / Wealth / Military / Intel / Stability."
The post-ED-787 "7-stat" claim is unreconciled with the 6-stat lineup.

**[P3] C-5 Prosperity level label.**
`settlement_layer`: Prosperity is a settlement stat (0–5) feeding province Effective Prosperity. `strategic_layer P-22`:
"Prosperity is a territory-level track, not a faction stat." Settlement-vs-territory wording diverges (likely the same
quantity at different granularity, but the labels conflict).


## 4 — Per-quantity flattening


### 4a — Contested trio + faction stats


### Mandate  — DEF 28 · WRITE 78 · READ 185

**Definitions / scale:**

- `prov/faction_canon_v30.md` L26: - `params/factions/stats_1_7_scale.md` (post-ED-787; per LPS-2e the faction lineup is 6-stat (Mandate headline) — L/PS are per-settlement (s
- `prov/faction_canon_v30.md` L39: - Does not silently fix the 6-stat (`factions_personal §8.1`) vs 7-stat (`stats_1_7_scale` post-ED-787) schema conflict at source. Surfaces 
- `prov/faction_canon_v30.md` L153: > **[REVISED by LPS-1 → LPS-2e (settlement_layer_v30 §1.8), Jordan ruling 2026-05-30 — resolves the §5.2 design-issue below.]** Legitimacy a
- `prov/faction_canon_v30.md` L199: > **The faction stat lineup is 6-stat: Mandate (headline, derived) / Influence / Wealth / Military / Intel / Stability.** Legitimacy and Pop
- `prov/faction_canon_v30.md` L211: Mandate is **the faction headline stat, derived by aggregation** (LPS-1; no longer "transitional"):
- `prov/faction_canon_v30.md` L219: > **[RESOLVED by LPS-1 → LPS-2e (settlement_layer_v30 §1.8), Jordan ruling 2026-05-30.]** L and PS are **per-settlement** (0–7); faction **M
- `prov/faction_canon_v30.md` L229: 1. **Scope-blind L/PS** (each scalar reflects intra-faction support density): a one-province faction with strong internal backing reads Mand
- `prov/faction_canon_v30.md` L358: | **D3** | Stat schema conflict (6-stat factions_personal vs 7-stat stats_1_7_scale) | 6-stat canonical post-LPS-2e — L/PS per-settlement (s
- `prov/faction_canon_v30.md` L449: | **Mandate (derived)** | 5 | 5 |
- `prov/faction_canon_v30.md` L614: | **Mandate (derived)** | 5 | 5 |
- `prov/faction_behavior_v30.md` L12: **Co-files updated:** `references/canonical_sources.yaml`, `params/bg/core.md` (Ethical Framework Modifiers struck), `params/factions.md`, `
- `prov/faction_behavior_v30.md` L25: Domain Action Ob is computed from action alignment with all four. Mandate is retained as a derived value during transition.
- `prov/faction_behavior_v30.md` L68: mandate: <0..7>                            # DERIVED — size-weighted saturating aggregate of controlled settlements' L/PS per settlement_lay
- `prov/faction_behavior_v30.md` L396: ## §4 Mandate (canonical faction aggregate — REVISED by LPS-2e)
- `prov/faction_behavior_v30.md` L398: > **[REVISED by LPS-1 (settlement_layer_v30 §1.8), Jordan ruling 2026-05-30.]** Mandate is **not** transitional and is **not** derived from 
- `prov/faction_behavior_v30.md` L454: | 4 | Update `params/bg/tracks.md`: Mandate becomes derived | 0.1 |
- `params/factions/stats_1_7_scale.md` L3: **Faction stats (6): Mandate / Influence / Wealth / Military / Intel / Stability.** Mandate is the headline (DERIVED — size-weighted aggrega
- `prov/faction_state_authoring_v30.md` L325: > **[REVISED by LPS-1 → LPS-2e (settlement_layer_v30 §1.8), Jordan ruling 2026-05-30.]** L and PS are **per-settlement**, not faction-level.
- `terr/settlement_layer_v30.md` L149: **Jordan ruling (2026-05-30, structural/metaphysical layer):** Legitimacy (L) and Popular Support (PS) are **per-settlement** political-acce
- `terr/settlement_layer_v30.md` L165: **Faction Mandate (size-weighted aggregate).** Let per-settlement acceptance `q_s = 0.5·L_s + 0.5·PS_s` (0–7), and weighted legitimacy mass 
- `terr/settlement_layer_v30.md` L166: `Mandate = clamp( round( 7 · T / (T + K) ), 0, 7 )`, with **K = 6** (calibrated, Stage-4 sim below).
- `terr/settlement_layer_v30.md` L168: - **Saturating / bounded:** the `T/(T+K)` form gives diminishing returns (the marginal legitimacy of the Nth loyal hamlet is less than the f
- `terr/settlement_layer_v30.md` L173: **Feedback (Mandate → settlement L/PS) — mean-reverting / stabilizing.** Each Accounting, held settlements drift toward the faction's Mandat
- `terr/settlement_layer_v30.md` L175: **Faction-level mission outcomes** (PP-686 cascade-fidelity / procedural / violation ΔL/ΔPS) now apply their ΔL/ΔPS **to the faction's contr

**Direct writes / deltas:**

- `prov/faction_layer_v30.md` L107: **Treaty breach:** Breaching faction: Mandate −2, Stability −1, all co-signatories gain Casus Belli (§3.5). Faction at Stability 1 facing el
- `prov/faction_layer_v30.md` L137: | Assassination of named officer NPC, Success | −2; Mandate −1 |
- `prov/faction_layer_v30.md` L180: | Church Absolution (Church unique action) | Target Stability ≤ 2; costs Church Mandate −1 | +1 to target; Church Influence +1 |
- `prov/faction_layer_v30.md` L181: | Löwenritter public endorsement | Löwenritter Stability ≥ 3, Military ≥ 4 | +1 to target; Löwenritter Mandate +1 |
- `prov/faction_layer_v30.md` L210: **Step 1 — Attribute snapshot.** Mandate drops to 0 immediately (political legitimacy is gone). All other attributes (Military, Wealth, Infl
- `prov/faction_layer_v30.md` L228: **Collapse immunity:** A faction at Stability 1 that would be reduced to 0 by an Accounting Stability Check (§1.4) may invoke a one-time Sur
- `prov/faction_layer_v30.md` L311: - Failure: Occupation marker remains; Church loses Mandate −1 (failed intervention exposed their overreach)
- `prov/faction_layer_v30.md` L339: > **[ED-865/874 migration, 2026-05-30]** Phase-1 positioning and Phase-3 ratification resolve via the deterministic+stochastic resolver (par
- `prov/faction_layer_v30.md` L357: Each signatory resolves **M = Mandate − 2** (legacy Ob 2 → difficulty 2).
- `prov/faction_layer_v30.md` L366: **Guarantor option:** A third faction offers guarantee (Mandate roll, difficulty 1, to offer). If accepted: each ratifier gains **+1 to M**.
- `prov/faction_layer_v30.md` L395: | Crown | Royal Guarantee | Instead of third-party Guarantor | Treaty proceeds without Guarantor; Crown Mandate −1; breach cost doubled |
- `prov/faction_layer_v30.md` L396: | Church | Sacred Compact | Both parties consent at signing | Breach triggers Excommunication threat immediately (Mandate −1 to breacher bef
- `prov/faction_layer_v30.md` L432: Church **Sacred Veto:** Cadence — available once per 4 consecutive seasons (ED-751). Reset triggers on the season when used (e.g., used Seas
- `prov/faction_layer_v30.md` L434: If Church uses Sacred Veto to block a motion that protects Church interests: additional Mandate −1 (self-interested veto is transparent; rep
- `prov/faction_layer_v30.md` L442: | **Censure** | Mandate 2 | Majority | Stability −1; Mandate −1 | None | One-time | N/A |
- `prov/faction_layer_v30.md` L445: | **Combined Embargo+Blockade** | Both | Supermajority | Wealth −2/season; Stability −1/season; Mandate −1 (once) | Wealth −1/season + Milit
- `prov/faction_layer_v30.md` L446: | **Outlawry** | Mandate 5 | Supermajority | Mandate −2; Stability −2; CB granted to all | Mandate −1 | Permanent until petitioned | Superma
- `prov/faction_layer_v30.md` L450: | **Recognition Challenge** | Mandate 4 | Supermajority | Target: −1 TCV from victory calculation (no territory change) | Mandate −1 | Until
- `prov/faction_layer_v30.md` L467: | Overwhelming | Both costs negated; proposer Mandate −1 (reputational damage) + target Stability +1 |
- `prov/faction_layer_v30.md` L492: **Guilds AI vote rule:** Always votes against Blockade and Combined Embargo+Blockade (threatens Wealth). Votes for Subsidy. Votes against Ou
- `prov/faction_layer_v30.md` L518: **Ransom refusal (capturing faction refuses negotiation):** Counts as Subterfuge (Trigger 4 category): capturing faction Stability −1, Manda
- `prov/faction_canon_v30.md` L282: 4. **Major Subterfuge** (Trigger 4): Sabotage −1; Assassination −2 + Mandate −1.
- `prov/faction_canon_v30.md` L298: Per `faction_layer_v30 §1.5`. Six-step procedure: Mandate → 0 immediate; territories → Uncontrolled; named officers → Independent; PC affili
- `prov/faction_canon_v30.md` L300: **Collapse immunity** (one-time per faction per campaign): Stability 1 facing reduction to 0 may invoke Survival Exception — Stability stays
- `prov/faction_canon_v30.md` L310: | Crown | Royal Decree | d+σ resolver: M = Mandate − 2 | 1/season; +1 Ob/season consecutive |  <!-- LPS-2e: L per-settlement, not a faction 
- `prov/faction_canon_v30.md` L311: | Church | Excommunication | d+σ resolver: M = Mandate − target Mandate (leader) / Mandate − 2 (non-leader) | Requires Church Mandate ≥ 3 | 
- `prov/faction_canon_v30.md` L312: | Church | CI 60 Territorial Seizure | Influence + floor(CI/15) vs Ob = 7 − PT | Per-territory; CI ≥ 60 trigger; AUTHORITATIVE per faction_l
- `prov/faction_canon_v30.md` L622: Resolution: d+σ resolver (stats_1_7_scale §Domain Action Resolution) — contested (faction leader): M = Mandate − target Mandate; non-leader:
- `prov/faction_canon_v30.md` L626: | Overwhelming | Strips target's Circles bonus with Church contacts; −1 Legitimacy to each of the target's controlled settlements (lowers ag
- `prov/faction_canon_v30.md` L636: Roll: Influence + floor(CI/15) vs Ob = 7 − PT (AUTHORITATIVE per faction_layer §2.7; supersedes the stale L-based formula). Failure → Mandat
- `prov/faction_canon_v30.md` L641: | Failure | Mandate −1 (authoritative faction_layer §2.7) |
- `prov/ci_political_v30.md` L22: | Govern effect | Mandate +1 on success (sim) | Mandate recovery (OW in capital per PP-174) + Accord maintenance |
- `prov/ci_political_v30.md` L96: - Mass Seizure bid fails if: Church loses 3 territories to counterattack in a single Year-End, OR Church Mandate drops to 3 or below. No sec
- `prov/ci_political_v30.md` L146: Ob of the vote threshold calculation is unchanged, but each secular faction voting against Church reduces their effective Mandate contributi
- `prov/ci_political_v30.md` L155: **Floor (ED-865/874 consistency, 2026-05-30):** a faction's effective vote contribution is **floored at 0** — the CI penalty can reduce an o
- `prov/ci_political_v30.md` L228: | Overwhelming | Both: Accord +1 AND Mandate +1 in own capital (PP-174) |
- `prov/ci_political_v30.md` L250: | 3–4 | All factions: Mandate check at Accounting (Mandate pool vs Ob 1). Failure → Mandate −1 |
- `prov/ci_political_v30.md` L401: PP-174 (Govern OW in own capital: Mandate +1) is retained.
- `prov/ci_political_v30.md` L402: New: Govern Success in any territory = Accord +1. Govern OW in capital = Mandate +1 AND Accord +1.
- `prov/faction_politics_v30.md` L280: | **4** | **Bishop's Delegate** (Bischofslegat) | 3 completed Canon-rank Duties; plus one **Public Doctrinal Defense** — the player successf

**Reads** (185 occurrences; samples):

- `prov/faction_layer_v30.md` L74: Crown holds the highest perceived strength at game start: highest Mandate, highest Wealth, capital + heartland territory (T1 Valorsplatz, T2
- `prov/faction_layer_v30.md` L123: | Action | Stability Δ | Mandate Δ |
- `prov/faction_layer_v30.md` L138: | Assassination Overwhelming (clean, no evidence) | −2; no Mandate cost |
- `prov/faction_layer_v30.md` L221: | Reconstitute collapsed faction | Influence Domain Action, Ob 4, repeated 3 seasons consecutively | Faction re-emerges at Stability 1, Mand
- `prov/faction_layer_v30.md` L230: **Engine note:** Collapse is evaluated at Accounting Step 2 (after trigger consequences, after §1.4 cascade check). The engine checks Stabil
- `prov/faction_layer_v30.md` L296: - Ob: floor(occupying faction Mandate / 2) + 1


### Legitimacy  — DEF 21 · WRITE 12 · READ 33

**Definitions / scale:**

- `prov/faction_canon_v30.md` L153: > **[REVISED by LPS-1 → LPS-2e (settlement_layer_v30 §1.8), Jordan ruling 2026-05-30 — resolves the §5.2 design-issue below.]** Legitimacy a
- `prov/faction_canon_v30.md` L199: > **The faction stat lineup is 6-stat: Mandate (headline, derived) / Influence / Wealth / Military / Intel / Stability.** Legitimacy and Pop
- `prov/faction_canon_v30.md` L203: | **Legitimacy** (per-settlement, settlement_layer §1.8) | 0–7 | Populace acceptance — papal bulls, dynastic claims, constitutional authorit
- `prov/faction_canon_v30.md` L442: | Legitimacy | 5 | 5 |
- `prov/faction_canon_v30.md` L607: | Legitimacy | 5 | 5 |
- `prov/faction_behavior_v30.md` L285: > **[SUPERSEDED-BY LPS-1 (settlement_layer_v30 §1.8), Jordan ruling 2026-05-30.]** Legitimacy is a **per-settlement** value (0–7), not facti
- `prov/faction_behavior_v30.md` L328: | Legitimacy | Popular Support | Strictness | Effect |
- `params/factions/stats_1_7_scale.md` L163: 3. Legitimacy: Constitutional monarchy vs Theocratic governance
- `prov/faction_state_authoring_v30.md` L331: crown:           {Legitimacy: 5, Popular_Support: 5}
- `prov/faction_state_authoring_v30.md` L332: church:          {Legitimacy: 5, Popular_Support: 5}
- `prov/faction_state_authoring_v30.md` L333: hafenmark:       {Legitimacy: 4, Popular_Support: 4}
- `prov/faction_state_authoring_v30.md` L334: varfell:         {Legitimacy: 4, Popular_Support: 4}
- `prov/faction_state_authoring_v30.md` L335: guilds_npc:      {Legitimacy: 3, Popular_Support: 3}
- `prov/faction_state_authoring_v30.md` L336: restoration:     {Legitimacy: 0, Popular_Support: 0}    # no Mandate; PS climbs from 0 via Mission outcomes
- `prov/faction_state_authoring_v30.md` L337: lowenritter:     {Legitimacy: 0, Popular_Support: 0}    # no Mandate; embedded under Crown initially
- `terr/settlement_layer_v30.md` L149: **Jordan ruling (2026-05-30, structural/metaphysical layer):** Legitimacy (L) and Popular Support (PS) are **per-settlement** political-acce
- `terr/settlement_layer_v30.md` L154: - **Legitimacy (L), 0–7** — institutional/constitutional acceptance (slow-moving: dynastic claims, papal bulls, constitutional authority).
- `terr/settlement_layer_v30.md` L177: **Consumers.** PP-686 Public Expectation strictness `base + 0.5·(L/7) − 0.3·(PS/7)` reads the faction **aggregate** L and PS defined above. 
- `scene/derived_stats_v30.md` L537: | Faction | Legitimacy* | **Legitimacy (derived)** | ×20 | Drains down |
- `scene/derived_stats_v30.md` L547: \* LPS-1 → LPS-2e (Jordan ruling 2026-05-30): Legitimacy and Popular Support are PER-SETTLEMENT values (0–7; settlement_layer §1.8), NOT a f
- `ui/valoria_ui_ux_supplement_derived_settlement.md` L16: Mandate ████████░░ 5      Legitimacy: 87/100  [▲ +5/season]

**Direct writes / deltas:**

- `prov/faction_canon_v30.md` L460: | Failure | Legitimacy −1 (overreach) |
- `prov/faction_canon_v30.md` L626: | Overwhelming | Strips target's Circles bonus with Church contacts; −1 Legitimacy to each of the target's controlled settlements (lowers ag
- `prov/faction_canon_v30.md` L628: | Failure | −1 Legitimacy to each Church-controlled settlement; target gains +1 Legitimacy in each of its controlled settlements (sympathy m
- `params/factions/stats_1_7_scale.md` L154: | Church | Excommunication | d+σ resolver: M = Mandate − target Mandate (leader) / Mandate − 2 (non-leader) | Strips Circles bonus; −1 Legit
- `params/factions/stats_1_7_scale.md` L177: | Baralta | Church Influence suppression | −1 Legitimacy/season to each Church-controlled settlement (settlement_layer §1.8) while Baralta L
- `params/factions/stats_1_7_scale.md` L197: | Success | Strips target's Circles bonus; −1 Legitimacy to each of the target's controlled settlements (settlement_layer §1.8) |
- `params/factions/stats_1_7_scale.md` L214: | Overwhelming | Church Influence −3; −1 Legitimacy to each Church-controlled settlement (settlement_layer §1.8); Heresy Investigation block
- `params/factions/stats_1_7_scale.md` L215: | Success | Church Influence −2; −1 Legitimacy to each Church-controlled settlement (settlement_layer §1.8); Heresy Investigation opens (Ob 
- `scene/derived_stats_v30.md` L327: - Turmoil Mandate check failure: Legitimacy −25 AND Mandate −1
- `scene/derived_stats_v30.md` L463: | Strain 3–4: Mandate check → Mandate −1 | Legitimacy −25 | tc_political, peninsular_strain |
- `params/bg/tracks.md` L1: <!-- [PP-686 v2 NOTE 2026-05-01] Mandate is now derived per designs/provincial/faction_behavior_v30.md §4: `Mandate = round(0.5 × Legitimacy
- `prov/peninsular_strain_v30.md` L319: | 3–4 | Tension | All factions: Legitimacy −25 at Accounting (derived_stats_v1). |

**Reads** (33 occurrences; samples):

- `prov/faction_canon_v30.md` L21: - `designs/provincial/faction_behavior_v30.md` (PP-686 v2: Mission / Cascade / Public Expectation / Legitimacy + Popular Support — the 4-com
- `prov/faction_canon_v30.md` L73: Legitimacy / PS Dynamics — what builds and erodes per faction
- `prov/faction_canon_v30.md` L151: ### §3.4 Legitimacy + Popular Support
- `prov/faction_canon_v30.md` L241: `factions_personal_v30 §8.1` documents a 6-stat faction sheet (Mandate / Influence / Wealth / Military / Intel / Stability). `params/faction
- `prov/faction_canon_v30.md` L261: | 3. Legitimacy | Constitutional monarchy | Theocratic governance | Crown / Hafenmark vs Church |
- `prov/faction_canon_v30.md` L518: | 3. Legitimacy | Pole A (Constitutional monarchy / deed-claim) | Church (Theocratic) |


### Popular Support  — DEF 9 · WRITE 0 · READ 17

**Definitions / scale:**

- `prov/faction_canon_v30.md` L153: > **[REVISED by LPS-1 → LPS-2e (settlement_layer_v30 §1.8), Jordan ruling 2026-05-30 — resolves the §5.2 design-issue below.]** Legitimacy a
- `prov/faction_canon_v30.md` L199: > **The faction stat lineup is 6-stat: Mandate (headline, derived) / Influence / Wealth / Military / Intel / Stability.** Legitimacy and Pop
- `prov/faction_canon_v30.md` L204: | **Popular Support** (per-settlement, settlement_layer §1.8) | 0–7 | Active populace backing — Florentine signoria support, urban guild mob
- `prov/faction_canon_v30.md` L443: | Popular Support | 5 | 5 |
- `prov/faction_canon_v30.md` L608: | Popular Support | 5 | 5 |
- `prov/faction_behavior_v30.md` L227: > **[SUPERSEDED-BY LPS-1 (settlement_layer_v30 §1.8), Jordan ruling 2026-05-30 — resolves the §5.2 design-issue faction_canon flagged.]** Po
- `terr/settlement_layer_v30.md` L149: **Jordan ruling (2026-05-30, structural/metaphysical layer):** Legitimacy (L) and Popular Support (PS) are **per-settlement** political-acce
- `terr/settlement_layer_v30.md` L155: - **Popular Support (PS), 0–7** — active populace backing (faster-moving: mobilization, local approval).
- `scene/derived_stats_v30.md` L547: \* LPS-1 → LPS-2e (Jordan ruling 2026-05-30): Legitimacy and Popular Support are PER-SETTLEMENT values (0–7; settlement_layer §1.8), NOT a f

**Reads** (17 occurrences; samples):

- `prov/faction_canon_v30.md` L21: - `designs/provincial/faction_behavior_v30.md` (PP-686 v2: Mission / Cascade / Public Expectation / Legitimacy + Popular Support — the 4-com
- `prov/faction_canon_v30.md` L151: ### §3.4 Legitimacy + Popular Support
- `prov/faction_canon_v30.md` L158: - **Popular Support** (faster-moving): active populace backing. Integrates Mission outcomes + Cascade Fidelity + random shocks per Public Te
- `prov/faction_canon_v30.md` L241: `factions_personal_v30 §8.1` documents a 6-stat faction sheet (Mandate / Influence / Wealth / Military / Intel / Stability). `params/faction
- `prov/faction_behavior_v30.md` L23: 4. **Legitimacy + Popular Support** — populace acceptance and active backing (separately tracked, modulating Public Expectation strictness)
- `prov/faction_behavior_v30.md` L66: aggregate_popular_support: <0..7>          # DERIVED — W-weighted mean of controlled SETTLEMENTS' Popular Support (LPS-2e, settlement_layer 


### Influence  — DEF 5 · WRITE 23 · READ 109

**Definitions / scale:**

- `prov/faction_canon_v30.md` L205: | **Influence** | 1–7 | Diplomatic reach — Medici banking diplomacy, Venetian diplomatic service |
- `prov/faction_canon_v30.md` L444: | Influence | 5 | 5 |
- `prov/faction_canon_v30.md` L609: | Influence | 6 | 6 |
- `prov/strategic_layer_v30.md` L555: **EMERGENT CONCLUSION:** A seemingly inevitable invasion is repelled by a military that sacrificed political legitimacy to get there. The Lö
- `scene/derived_stats_v30.md` L294: | Influence | **Reputation** | Influence × 15, starting = stat × 15 | Political capital across factions |

**Direct writes / deltas:**

- `prov/faction_layer_v30.md` L180: | Church Absolution (Church unique action) | Target Stability ≤ 2; costs Church Mandate −1 | +1 to target; Church Influence +1 |
- `prov/strategic_layer_v30.md` L257: - Restoration faction: Influence + 1D per Presence marker in T13.
- `prov/strategic_layer_v30.md` L260: **Correction (PATCH P-26, PP-663 revised):** "In board game mode, the Forgetting Check pool is: Influence + 1D per Presence marker in T13 (R
- `prov/strategic_layer_v30.md` L348: - If successful (Attention Pool ≥ 3): Church Influence +0.5; AER +1; Restoration potentially loses Presence marker.
- `prov/strategic_layer_v30.md` L353: - Church Influence +1 (T3 control) at Accounting.
- `prov/strategic_layer_v30.md` L369: 1. Church Influence +3. Current Church Influence 52 + 1 (Assert) + 3 (Resist) = 56.
- `prov/strategic_layer_v30.md` L389: **Gap identified:** The Cascade Depth Cap says "more than 3 immediate mechanical effects in one resolution step." Are clock changes (Church 
- `prov/strategic_layer_v30.md` L440: - Church Influence +2 (Seizure successful per Church Influence formula).
- `prov/strategic_layer_v30.md` L463: - Church Influence +1 (Church Influence 39). Klapp card removed.
- `prov/strategic_layer_v30.md` L468: - Church Influence −1 (Church Influence 37). Klapp Active continues.
- `prov/strategic_layer_v30.md` L473: - **Prosecute:** Church Stability −1. AER −1. Church Influence −2. Klapp removed.
- `prov/strategic_layer_v30.md` L477: - Warden Cooperation +1 (now 2). Church Influence −2 (Church Influence 36). Church Stability −1.
- `prov/strategic_layer_v30.md` L590: **With Hafenmark Baralta suppression (Mandate ≥ 4 passive: −1/season):** Net gain ~1/season before Church Influence 50, ~2/season after. Est
- `prov/strategic_layer_v30.md` L594: Alternatively, add an additional Church Influence gain source: "Church wins any contested Institutional Mandate dispute (another faction Com
- `params/factions/stats_1_7_scale.md` L89: - **All faction Domain Actions** (Assert, Reconstitute, Govern, Claim Masterless, etc.). Assert: M = Influence − 2 (legacy Ob 2 → difficulty
- `params/factions/stats_1_7_scale.md` L214: | Overwhelming | Church Influence −3; −1 Legitimacy to each Church-controlled settlement (settlement_layer §1.8); Heresy Investigation block
- `params/factions/stats_1_7_scale.md` L215: | Success | Church Influence −2; −1 Legitimacy to each Church-controlled settlement (settlement_layer §1.8); Heresy Investigation opens (Ob 
- `params/factions/stats_1_7_scale.md` L216: | Partial | Church Influence −1; Heresy Investigation opens immediately; Church Influence +1 |
- `params/factions/stats_1_7_scale.md` L217: | Failure | Church Influence +1; Heresy Investigation immediate; Baralta's L −1 |
- `params/factions/stats_1_7_scale.md` L218: CI Suppression: while Baralta's L ≥ 4, Church Influence −1/season. Suppression ends if L < 4 or excommunication (CI +4 immediately).
- `params/factions/stats_1_7_scale.md` L264: **Martial Law effects:** All non-Military Domain Actions in Crown territories require secondary Military check (Löwenritter Military pool, T
- `params/factions/stats_1_7_scale.md` L338: - Effect persists until Church Influence drops below 40 OR Reformed Settlement is withdrawn.
- `scene/derived_stats_v30.md` L340: **When Reputation reaches 0:** Diplomatic and Intel actions +1 Ob. At next Accounting still at 0: Influence −1.

**Reads** (109 occurrences; samples):

- `prov/faction_layer_v30.md` L86: Varfell Military stat 4 is mid-tier (matches Hafenmark, one below Crown). Their advantage is *cunning in service of pride* — Vaynard ("Magnu
- `prov/faction_layer_v30.md` L210: **Step 1 — Attribute snapshot.** Mandate drops to 0 immediately (political legitimacy is gone). All other attributes (Military, Wealth, Infl
- `prov/faction_layer_v30.md` L221: | Reconstitute collapsed faction | Influence Domain Action, Ob 4, repeated 3 seasons consecutively | Faction re-emerges at Stability 1, Mand
- `prov/faction_layer_v30.md` L309: - Seizure roll proceeds normally (Influence + floor(CI/15) vs Ob = 7 − PT)
- `prov/faction_layer_v30.md` L339: > **[ED-865/874 migration, 2026-05-30]** Phase-1 positioning and Phase-3 ratification resolve via the deterministic+stochastic resolver (par
- `prov/faction_layer_v30.md` L342: Initiator resolves **M = own Influence − target Influence**. Success or Overwhelming → initiator controls opening terms (sets first demand);


### Wealth  — DEF 6 · WRITE 35 · READ 93

**Definitions / scale:**

- `prov/faction_layer_v30.md` L268: | Wealth | −1/season | 0 (extraction inefficient) |
- `prov/faction_layer_v30.md` L483: - Military −1 at each subsequent Accounting while Wealth = 0 (mercenaries unpaid)
- `prov/faction_canon_v30.md` L206: | **Wealth** | 1–7 | Economic resources — trade revenue, mercenary funding, treasury |
- `prov/faction_canon_v30.md` L445: | Wealth | 4 | 4 |
- `prov/faction_canon_v30.md` L610: | Wealth | 5 | 5 |
- `scene/derived_stats_v30.md` L292: | Wealth | **Treasury** | Wealth × 100, starting = stat × 100 | Accumulated economic resources |

**Direct writes / deltas:**

- `prov/faction_layer_v30.md` L443: | **Embargo** | Mandate 3 | Majority | Wealth −1/season | Wealth −1/season | Until lifted | Majority |
- `prov/faction_layer_v30.md` L444: | **Blockade** | Military 3, Mandate 3 | Majority | Wealth −2/season; Stability −1 (once) | Military −1 (garrison) | Until lifted | Majority
- `prov/faction_layer_v30.md` L445: | **Combined Embargo+Blockade** | Both | Supermajority | Wealth −2/season; Stability −1/season; Mandate −1 (once) | Wealth −1/season + Milit
- `prov/faction_layer_v30.md` L447: | **Subsidy** | Mandate 2 | Majority | Recipient Wealth +1 | Wealth −1 | One-time | N/A |
- `prov/faction_layer_v30.md` L484: - Recovery: any Wealth gain restores the Wealth stat. **Military re-muster (FSS-LOOP-2, 2026-05-30 — resolution-diagnostic ratification; Les
- `prov/ci_political_v30.md` L240: | Success | Wealth +1 |
- `prov/ci_political_v30.md` L241: | Overwhelming | Wealth +2 (capped by seasonal cap of +2) |
- `prov/military_layer_v30.md` L150: Recovery: when Wealth rises above 0, Discipline degradation stops. Discipline does not auto-recover — requires Muster action on existing uni
- `prov/military_layer_v30.md` L173: | Overwhelming | Fort −2 | MS −1, Wealth −1 |
- `prov/military_layer_v30.md` L174: | Success | Fort −1 | MS −1, Wealth −1 |
- `prov/military_layer_v30.md` L175: | Partial | No change | MS −1, Wealth −1 |
- `prov/military_layer_v30.md` L176: | Failure | No change | Stability −1, Wealth −1 |
- `prov/military_layer_v30.md` L270: At each Accounting: for each territory where Church is Prominent AND Church Wealth ≥ (controlling faction Wealth + 2):
- `prov/strategic_layer_v30.md` L230: **Correction (PATCH P-22):** Prosperity is a **territory-level modifier** (not a faction stat). Each territory has a Prosperity value (0–5).
- `prov/strategic_layer_v30.md` L527: Hafenmark Trade T7: Wealth 5 vs Ob 3 (Institutional Pressure friction). Roll 5d10: 9, 3, 7, 1, 6 → 2-1 = 1 net. Ob 3. Partial: Wealth +1, bu
- `prov/strategic_layer_v30.md` L709: Resource expenditure threshold: 2× rolled net successes. Below threshold = "stressed" — faction takes Wealth −1 at Cascade. Above threshold 
- `prov/strategic_layer_v30.md` L796: | G-093 | Threshold = 2× rolled; below = stressed (Wealth −1) |
- `params/factions/stats_1_7_scale.md` L234: | Overwhelming | Target loses 1 Wealth + 1 Prosperity in that territory |
- `params/factions/stats_1_7_scale.md` L235: | Success | Target faction loses 1 Wealth for 1 season |
- `params/factions/stats_1_7_scale.md` L278: - 1 Wealth token → +1D on Trade or Diplomacy Domain Action (max +2D per action)
- `params/bg/faction_actions.md` L54: | Prudence | Wealth +1 (integer) this season |
- `params/bg/faction_actions.md` L282: | Prudence | Wealth +1 (integer) this season |
- `terr/settlement_layer_v30.md` L543: - Settlement Wealth +0.5 (illicit trade is still trade).
- `terr/settlement_layer_v30.md` L559: **Harvesting:** Any faction/actor who discovers the site can harvest. RS −0.5 per harvest per season. Wealth +1 for harvesting faction.
- `scene/derived_stats_v30.md` L315: **When Treasury reaches 0:** Faction cannot Muster, Fortify, or perform gold-cost actions. Professional units begin Discipline degradation (
- `scene/derived_stats_v30.md` L317: **When Wealth stat drops:** Treasury maximum drops (new max = Wealth × 100). Current Treasury retained. Recovery requires Trade actions.
- `scene/derived_stats_v30.md` L410: | Treasury reaches 0 while faction officer | Wealth −1 at Accounting | Counselor+: Renown −1 |
- `scene/derived_stats_v30.md` L452: | Campaign Supply: Wealth −1/season | Treasury −100/season | mass_battle_v30 |
- `scene/derived_stats_v30.md` L456: | Siege supply: Wealth −1/season | Treasury −100/season | military_layer_v30 |
- `scene/derived_stats_v30.md` L462: | Trade Success: Wealth +1 | Treasury +Wealth×25 | tc_political |
- `scene/derived_stats_v30.md` L468: | Settlement expansion: Wealth −3 | Treasury −300 | settlement_layer |
- `scene/derived_stats_v30.md` L469: | Mine surplus: Wealth +1 | Treasury +50/season | settlement_layer |
- `scene/derived_stats_v30.md` L484: | Trade Overwhelming: Wealth +1 | KEEP | Exceptional success = structural improvement |
- `params/bg/tracks.md` L62: | 1 | Templar deployment costs +1 Wealth in Hafenmark-adjacent territories |
- `params/bg/tracks.md` L91: | 1 | Templar deployment costs +1 Wealth in Hafenmark-adjacent territories |

**Reads** (93 occurrences; samples):

- `prov/faction_layer_v30.md` L74: Crown holds the highest perceived strength at game start: highest Mandate, highest Wealth, capital + heartland territory (T1 Valorsplatz, T2
- `prov/faction_layer_v30.md` L102: | Minor cession | ≤1 territory OR indemnity ≤1 Wealth | −1 |
- `prov/faction_layer_v30.md` L103: | Major cession | 2+ territories OR indemnity ≥2 Wealth | −2 |
- `prov/faction_layer_v30.md` L105: | Tributary | Annual Wealth obligation accepted | −1/year while active |
- `prov/faction_layer_v30.md` L210: **Step 1 — Attribute snapshot.** Mandate drops to 0 immediately (political legitimacy is gone). All other attributes (Military, Wealth, Infl
- `prov/faction_layer_v30.md` L329: | Tributary arrangement | Annual | Wealth transfer obligation; hegemon provides recognition |


### Military  — DEF 9 · WRITE 17 · READ 150

**Definitions / scale:**

- `prov/faction_layer_v30.md` L269: | Military | No recruitment from territory | Garrison cost: −1 pool per occupied territory |
- `prov/faction_layer_v30.md` L453: **Embargo/Blockade renewal:** Must be renewed annually (Year-End Accounting). Fails to renew = lapses. Proposing faction below minimum Manda
- `prov/faction_canon_v30.md` L207: | **Military** | 1–7 | Armed forces — standing armies, fortification networks |
- `prov/faction_canon_v30.md` L446: | Military | 4 | 4 |
- `prov/faction_canon_v30.md` L611: | Military | 4 | 4 |
- `prov/ci_political_v30.md` L348: - Military: defend T1, T14, T2, T3 (core territories). Only expand when those four are garrisoned.
- `prov/ci_political_v30.md` L354: - Military: defensive only. T8 and T10 must remain garrisoned. T7 is expendable.
- `prov/military_layer_v30.md` L398: | ED-NEW-MIL-03 | Experience stack ceiling. | **RESOLVED (PP-667)** — ceiling is faction Military stat (1–7). |
- `scene/derived_stats_v30.md` L293: | Military | **Levies Available** | Military × 2 (ceiling) | Force projection capacity — not spendable, constrains active unit count |

**Direct writes / deltas:**

- `prov/faction_layer_v30.md` L444: | **Blockade** | Military 3, Mandate 3 | Majority | Wealth −2/season; Stability −1 (once) | Military −1 (garrison) | Until lifted | Majority
- `prov/faction_layer_v30.md` L445: | **Combined Embargo+Blockade** | Both | Supermajority | Wealth −2/season; Stability −1/season; Mandate −1 (once) | Wealth −1/season + Milit
- `prov/faction_layer_v30.md` L483: - Military −1 at each subsequent Accounting while Wealth = 0 (mercenaries unpaid)
- `prov/faction_layer_v30.md` L484: - Recovery: any Wealth gain restores the Wealth stat. **Military re-muster (FSS-LOOP-2, 2026-05-30 — resolution-diagnostic ratification; Les
- `prov/faction_layer_v30.md` L638: | ED-NEW-005 | Wealth Zero Military drain per season. | **RESOLVED** — confirmed; −1 Military per season. |
- `prov/ci_political_v30.md` L189: | Battle loss (margin −2+) | Defender Military −1 (not Mandate) | mass_battle_v30 §B.3 |
- `prov/military_layer_v30.md` L148: This is more specific than the prior simulation's Military −1 at Wealth 0. Military stat itself does not degrade from Wealth shortage — the 
- `prov/military_layer_v30.md` L203: | Attacker wins | Attacker net ≥ Defender net + 2 | Territory captured; Defender Military −1 |
- `prov/military_layer_v30.md` L205: | Defender wins | Defender net ≥ Attacker net + 2 | No territory change; Attacker Military −1 |
- `prov/military_layer_v30.md` L399: | ED-NEW-MIL-04 | Wealth Zero → HI/Cavalry Discipline −1/season. | **RESOLVED (PP-667)** — confirmed; supersedes "Military −1" prior rule. |
- `prov/strategic_layer_v30.md` L161: > **Military loss timing by mode (PP-041):** Military loss from unit destruction applies differently by mode: — TTRPG mode: Military −1 is a
- `prov/strategic_layer_v30.md` L506: **Downstream intelligence use:** Varfell negotiates with Crown in Phase 2 next season (Open Pledge: share Restoration intelligence in exchan
- `params/factions/stats_1_7_scale.md` L284: When a unit is destroyed in TTRPG mass combat: Faction Military −1 (immediate). Cap: −2 per season from destruction. [PROVISIONAL]
- `scene/derived_stats_v30.md` L354: **Levies Available (from Military):** Ceiling, not spendable. Military × 2 = max active units. If Military drops, ceiling drops — disband ex
- `scene/derived_stats_v30.md` L475: | Battle loss (margin ≥2): Military −1 | KEEP | Decisive loss IS structural military damage |
- `scene/derived_stats_v30.md` L476: | Unit destroyed: Military −1 | KEEP | Permanent force loss |
- `ui/valoria_ui_ux_supplement_derived_settlement.md` L39: **Levies Available:** Not a bar — shows "X/Y fielded" where Y = Military × 2. If over cap after Military drop, show in red with "DISBAND REQ

**Reads** (150 occurrences; samples):

- `prov/faction_layer_v30.md` L78: Crown's standing army is the Löwenritter Order. All Crown military operations field Löwenritter units pre-coup. Crown faction Military stat 
- `prov/faction_layer_v30.md` L82: Hafenmark Military stat 4 is mid-tier numerically but expressed mechanically as *equipment quality*. Hafenmark's mining (T17 Halvarshelm Nor
- `prov/faction_layer_v30.md` L86: Varfell Military stat 4 is mid-tier (matches Hafenmark, one below Crown). Their advantage is *cunning in service of pride* — Vaynard ("Magnu
- `prov/faction_layer_v30.md` L143: #### Trigger 5 — Failed Military Engagement: Significant Losses
- `prov/faction_layer_v30.md` L147: **Condition A — Committed force.** Acting faction's Military pool ≥ 4 at time of roll. (Pool 1–3 = raid/skirmish; no Stability consequence o
- `prov/faction_layer_v30.md` L181: | Löwenritter public endorsement | Löwenritter Stability ≥ 3, Military ≥ 4 | +1 to target; Löwenritter Mandate +1 |


### Intel  — DEF 3 · WRITE 5 · READ 68

**Definitions / scale:**

- `prov/faction_canon_v30.md` L208: | **Intel** | 1–7 | Institutional intelligence — Venice's Council of Ten, papal nuncio network |
- `prov/faction_canon_v30.md` L447: | Intel | 3 | 3 |
- `prov/faction_canon_v30.md` L612: | Intel | 4 | 4 |

**Direct writes / deltas:**

- `prov/faction_canon_v30.md` L314: | Varfell | The Private Collection | d+σ resolver: M = Intel − 2 | 1/season; long-term TS cost |
- `prov/strategic_layer_v30.md` L500: Influence 4 (standard Intel) vs Ob 2. Thread Resonance: +1D. Scholastic (Varfell): evidence-based Intel −1 Ob = Ob 1.
- `params/factions/stats_1_7_scale.md` L95: - **Unique Actions (migrated 2026-05-30, ED-874 — Jordan-ratified 2026-05-31).** Formerly bare-stat "vs Ob" rolls; now resolve via this meth
- `params/factions/stats_1_7_scale.md` L221: Resolution: d+σ resolver (§Domain Action Resolution) — M = Intel − 2 (legacy Ob 2). Once per season.
- `params/factions/stats_1_7_scale.md` L225: | Failure | Artefact's Thread signature detected by a practitioner; Church Intel +1D vs Varfell for 1 season; Thread Tension +1 |

**Reads** (68 occurrences; samples):

- `prov/faction_layer_v30.md` L86: Varfell Military stat 4 is mid-tier (matches Hafenmark, one below Crown). Their advantage is *cunning in service of pride* — Vaynard ("Magnu
- `prov/faction_layer_v30.md` L136: | Sabotage success (Intel vs Stability, Success degree) | −1 |
- `prov/faction_layer_v30.md` L397: | Hafenmark | Deed-claim | Prior Intel op documented legal claim | Positioning roll +1D; Ratification Ob −1 |
- `prov/faction_layer_v30.md` L398: | Varfell | Diplomatic stratagem | Default | May withhold maximum concession until Phase 2 (Talleyrand-style political reading); Varfell Int
- `prov/faction_layer_v30.md` L543: Priority 1: Intel/Tribune
- `prov/faction_canon_v30.md` L199: > **The faction stat lineup is 6-stat: Mandate (headline, derived) / Influence / Wealth / Military / Intel / Stability.** Legitimacy and Pop


### Stability  — DEF 9 · WRITE 97 · READ 144

**Definitions / scale:**

- `prov/faction_layer_v30.md` L230: **Engine note:** Collapse is evaluated at Accounting Step 2 (after trigger consequences, after §1.4 cascade check). The engine checks Stabil
- `prov/faction_layer_v30.md` L270: | Stability | See Trigger 1 | — |
- `prov/faction_canon_v30.md` L209: | **Stability** | 0–7 | Internal cohesion — Pazzi conspiracy resistance, Visconti-Sforza succession discipline |
- `prov/faction_canon_v30.md` L296: ### §8.3 Collapse (Stability = 0 at Accounting)
- `prov/faction_canon_v30.md` L448: | Stability | 4 | 4 |
- `prov/faction_canon_v30.md` L613: | Stability | 5 | 5 |
- `prov/strategic_layer_v30.md` L191: **Correction (PATCH P-18):** "Within tier: resolve in descending Stability order. Tied Stability (exactly equal): resolve simultaneously *on
- `params/factions/stats_1_7_scale.md` L52: | Mending Stability | 60 | 72 | Mending Stability = 0 |
- `scene/derived_stats_v30.md` L295: | Stability | **Discipline** | Stability × 10, starting = stat × 10 | Internal faction unity |

**Direct writes / deltas:**

- `prov/faction_layer_v30.md` L20: | TC_SUPPRESS_STABILITY | Suppress Failure → Stability −1 is RETAINED. It is a named exception to PP-403 repeal, not covered by the new trig
- `prov/faction_layer_v30.md` L46: **PP-403 exception retained:** Suppress action (CI Accounting formula, params_board_game §CI Generation Step 4) Failure → Stability −1. This
- `prov/faction_layer_v30.md` L107: **Treaty breach:** Breaching faction: Mandate −2, Stability −1, all co-signatories gain Casus Belli (§3.5). Faction at Stability 1 facing el
- `prov/faction_layer_v30.md` L183: **Seasonal cap:** FACTION_STAT_SEASONAL_CAP = ±2 applies. No more than +2 Stability per season from any combination of sources.
- `prov/faction_layer_v30.md` L195: | Failure | Stability −1 (cascade consequence) |
- `prov/faction_layer_v30.md` L198: | Overwhelming | Stability +1 (faction rallied under pressure) |
- `prov/faction_layer_v30.md` L202: **Deterministic low-Stability floor (FSS-LOOP-1, 2026-05-30 — resolution-diagnostic ratification; supersedes the §8.12 / factions_personal "
- `prov/faction_layer_v30.md` L285: | 2 seasons | — | Occupation active; displaced faction Stability −1/season accumulating |
- `prov/faction_layer_v30.md` L289: | Any duration | Recapture (Overwhelming) | Occupation marker removed; occupying faction Stability −1 (costly suppression) |
- `prov/faction_layer_v30.md` L299: - Overwhelming: marker removed AND occupying faction Stability −1 (costly suppression)
- `prov/faction_layer_v30.md` L442: | **Censure** | Mandate 2 | Majority | Stability −1; Mandate −1 | None | One-time | N/A |
- `prov/faction_layer_v30.md` L444: | **Blockade** | Military 3, Mandate 3 | Majority | Wealth −2/season; Stability −1 (once) | Military −1 (garrison) | Until lifted | Majority
- `prov/faction_layer_v30.md` L445: | **Combined Embargo+Blockade** | Both | Supermajority | Wealth −2/season; Stability −1/season; Mandate −1 (once) | Wealth −1/season + Milit
- `prov/faction_layer_v30.md` L446: | **Outlawry** | Mandate 5 | Supermajority | Mandate −2; Stability −2; CB granted to all | Mandate −1 | Permanent until petitioned | Superma
- `prov/faction_layer_v30.md` L467: | Overwhelming | Both costs negated; proposer Mandate −1 (reputational damage) + target Stability +1 |
- `prov/faction_layer_v30.md` L475: Parliamentary Censure, Embargo, Blockade, and Outlawry reduce target Stability. If Stability drops to ≤ 2, Accord −1 in all territories cont
- `prov/faction_layer_v30.md` L516: Per new doc: captured officer costs capturing faction's target Stability −1/season ongoing until ransom paid or resolved.
- `prov/faction_layer_v30.md` L518: **Ransom refusal (capturing faction refuses negotiation):** Counts as Subterfuge (Trigger 4 category): capturing faction Stability −1, Manda
- `prov/faction_layer_v30.md` L520: **Maximum capture duration:** If ransom unpaid for 3 seasons, capturing faction must choose: execute (officer killed, Stability −1 additiona
- `prov/faction_layer_v30.md` L532: | 8–9 | Killed. Permanent; Stability −1 additional to their faction. |
- `prov/faction_layer_v30.md` L533: | 10 | Heroic survival. Morale effect: faction Stability +1. |
- `prov/faction_layer_v30.md` L576: → Institutional Consolidation: no Trigger 1–5 this season → Stability +1
- `prov/faction_layer_v30.md` L621: 3. **Assert** (optional Church action, Phase 4 Priority 6): Influence vs Ob 2. Success: CI +1. Failure: Church Stability −1.
- `prov/faction_layer_v30.md` L622: 4. **Suppress** (optional opponent action, Phase 4 Priority 4): Mandate vs Ob = floor(Church Mandate/2)+1. Success: negate Step 1 passive th
- `prov/faction_layer_v30.md` L637: | ED-NEW-004 | Parliament Embargo+Blockade: ongoing Stability penalty? | **RESOLVED** — Stability −1/season ongoing while both active. Ends 
- `prov/faction_canon_v30.md` L660: - **Arc B — Crisis of Faith.** Total Victory Contest defeat via Evidence Resonant Style. OR: Cardinal of Temperance presents Thread-adjacent
- `prov/faction_canon_v30.md` L661: - **Arc C — Confrontation.** Public confrontation. If Confessor heretic publicly known: Church Stability −3. CI may decrease rapidly as inst
- `prov/ci_political_v30.md` L225: | Failure | No change; Stability −1 if Prosperity was 0 in that territory (resource mismanagement) |
- `prov/faction_politics_v30.md` L829: - **Church rank consequences:** Himlensendt's position is severely weakened. Church Stability drops to 0 (anti-death-spiral floor). Standing
- `prov/faction_politics_v30.md` L839: - **Hafenmark survives unless Baralta was eliminated in the contest.** Baralta alive + Hafenmark-lost-contest means Baralta reverts to pre-c
- `prov/faction_politics_v30.md` L950: | +3 or higher | **Loyal Heir** | Torben formally renounces claim in favor of the player if the player is non-dynastic; or supports the play
- `prov/faction_politics_v30.md` L951: | +1 to +2 | **Cooperative Heir** | Torben supports the player as regent until he reaches full age (additional readiness accumulation requir
- `prov/faction_politics_v30.md` L952: | 0 | **Neutral Heir** | Torben asserts his claim independently; willing to coexist with the player as a rival but not necessarily hostile. 
- `prov/faction_politics_v30.md` L953: | −1 to −2 | **Wary Heir** | Torben pursues his own claim actively; builds inner-circle support to displace the player. Player's Crown Std 6
- `prov/faction_politics_v30.md` L954: | −3 or lower | **Hostile Heir** | Torben becomes a Rival candidate with full Rival Standing track (SUC-02 mechanic). Active contested succe
- `prov/military_layer_v30.md` L176: | Failure | No change | Stability −1, Wealth −1 |
- `prov/military_layer_v30.md` L204: | Partial | Margin ≤ 1 either direction | No territory change; Attacker Stability −1 (commitment cost) |
- `prov/military_layer_v30.md` L302: | Failure | +0 CI | Church Stability −1 |
- `prov/military_layer_v30.md` L317: | Failure | No CI effect | Suppressing faction Stability −1 (existing named exception to PP-403 repeal) |
- `prov/victory_v30.md` L202: **Degree effects:** Overwhelming: Treaty formed + target Mandate −1 + Stability +1 + Crown Mandate +1. Success: Treaty formed + target Manda

**Reads** (144 occurrences; samples):

- `prov/faction_layer_v30.md` L4: <!-- Supersedes: PP-403 (Failed DA Stability Cost — REPEALED except §Suppress exception) -->
- `prov/faction_layer_v30.md` L19: | OFFICER_CAPTURE_CONFLICT | ED-334/335 is canonical for BG/Hybrid officer resolution. New Stability trigger applies additionally. d10 fate 
- `prov/faction_layer_v30.md` L22: | ACCOUNTING_STABILITY_CHECK | Existing Phase 5 Step 2 (Stability pool roll on ≥2 attribute loss) is RETAINED alongside new trigger system. 
- `prov/faction_layer_v30.md` L23: | TRIGGER5_POOL_CLIFF (ED-876) | Trigger-5 Condition C clause "Engaged pool ≥ 6" REMOVED from the gate, retained in the cost table as a seve
- `prov/faction_layer_v30.md` L44: **PP-403 REPEALED.** Failed Domain Actions no longer cost Stability. See §0 for one named exception (Suppress failure).
- `prov/faction_layer_v30.md` L48: ### §1.2 Stability Triggers (Five Canonical)


### 4b — Settlement stats + settlement-derived


### Prosperity  — DEF 8 · WRITE 11 · READ 66

**Definitions / scale:**

- `prov/faction_behavior_v30.md` L406: PP-686's 0.5L+0.5PS blend, now SIZE-WEIGHTED and saturating per settlement_layer §1.8 (Weight W=base(Type)+Prosperity+FacilityTier; K=6); fa
- `prov/military_layer_v30.md` L396: | ED-NEW-MIL-01 | Population modifier to initial Size (Prosperity tiers). | **RESOLVED (PP-667)** — Prosperity 1-2: Size +0 · 3-4: Size +1 ·
- `prov/strategic_layer_v30.md` L224: ## G-02 — Prosperity: Undefined Track
- `prov/strategic_layer_v30.md` L226: > **P-22:** **Prosperity** is a territory-level track, not a faction stat. Each territory has a Prosperity value (0–5); starting values show
- `terr/settlement_layer_v30.md` L43: **Derived values (derived_stats_v1 §4):** Settlement stats (Prosperity/Defense/Order, 0–5) produce derived values for the videogame layer:
- `terr/settlement_layer_v30.md` L47: | Prosperity | Local Economy | Prosperity × 50 | Gold income contribution to faction Treasury |
- `terr/settlement_layer_v30.md` L57: | **Prosperity** | Economic output and quality of life | Contributes to province Effective Prosperity. Each point of settlement Prosperity a
- `scene/derived_stats_v30.md` L372: | Prosperity | **Local Economy** | Prosperity × 50 |

**Direct writes / deltas:**

- `prov/strategic_layer_v30.md` L229: **Gap:** Govern outcome says "Prosperity +1" on Success. T11 grants "+1 Prosperity/season." Community Projects mention "Prosperity +1." But 
- `prov/strategic_layer_v30.md` L230: **Correction (PATCH P-22):** Prosperity is a **territory-level modifier** (not a faction stat). Each territory has a Prosperity value (0–5).
- `params/factions/stats_1_7_scale.md` L234: | Overwhelming | Target loses 1 Wealth + 1 Prosperity in that territory |
- `terr/settlement_layer_v30.md` L51: Settlement derived values feed upward to faction derived values: Local Economy contributes to faction Treasury income. Garrison Strength is 
- `terr/settlement_layer_v30.md` L427: | Develop | Cognition + Wealth-relevant History | floor(Prosperity/2) + 1 | Prosperity +1 (cap: settlement type max) |
- `terr/settlement_layer_v30.md` L510: | Past-Oriented Pulling | No positive effect | Prosperity −1 (paradox window disrupts routine) |
- `terr/settlement_layer_v30.md` L512: | Mending | Prosperity +1 (substrate coherence restored, infrastructure strengthens) | No settlement effect |
- `terr/settlement_layer_v30.md` L513: | Community Organizing | Order +1 AND Prosperity +1 (if PT ≤ 2 in province) | No settlement effect |
- `terr/settlement_adjacency_v30.md` L101: | Mine | Attacker gains captured Prosperity on victory |
- `terr/settlement_adjacency_v30.md` L111: - **Settlement Prosperity −1** on Assault outcome Partial or worse (battle damage to local economy).
- `prov/peninsular_strain_v30.md` L176: | City | Military governor. Prosperity −1 at onset. Guild management revoked unless explicitly re-granted (Influence, Ob 2). |

**Reads** (66 occurrences; samples):

- `prov/faction_canon_v30.md` L219: > **[RESOLVED by LPS-1 → LPS-2e (settlement_layer_v30 §1.8), Jordan ruling 2026-05-30.]** L and PS are **per-settlement** (0–7); faction **M
- `prov/ci_political_v30.md` L221: Govern (Consul Inward): **resolves via the deterministic+stochastic resolver** — M = Mandate − difficulty, difficulty = max(1, (Ob−1)·2), Ob
- `prov/ci_political_v30.md` L225: | Failure | No change; Stability −1 if Prosperity was 0 in that territory (resource mismanagement) |
- `prov/ci_political_v30.md` L234: Trade (Consul Outward): **resolves via the deterministic+stochastic resolver** — M = Wealth − difficulty, difficulty = max(1, (Ob−1)·2), Ob 
- `prov/faction_behavior_v30.md` L68: mandate: <0..7>                            # DERIVED — size-weighted saturating aggregate of controlled settlements' L/PS per settlement_lay
- `prov/faction_politics_v30.md` L206: | **3** | **Lendmann** (Lendmann) | **Formal Recognition Event:** The Jarl grants the player a **Land-Grant** — a specific settlement or def


### Defense  — DEF 5 · WRITE 7 · READ 25

**Definitions / scale:**

- `terr/settlement_layer_v30.md` L43: **Derived values (derived_stats_v1 §4):** Settlement stats (Prosperity/Defense/Order, 0–5) produce derived values for the videogame layer:
- `terr/settlement_layer_v30.md` L48: | Defense | Garrison Strength | Defense × 20 + Fort Level × 30 | Settlement defensibility score |
- `terr/settlement_layer_v30.md` L58: | **Defense** | Fortification and garrison readiness | Determines Ob for attackers. Defense 0 = undefended (auto-capture). Defense 5 = major
- `terr/settlement_layer_v30.md` L582: Each settlement can host a garrison (one military unit). The garrison's stats (from military_layer_v30) add to the settlement's Defense for 
- `scene/derived_stats_v30.md` L373: | Defense | **Garrison Strength** | Defense × 20 + Fort Level × 30 |

**Direct writes / deltas:**

- `prov/faction_politics_v30.md` L206: | **3** | **Lendmann** (Lendmann) | **Formal Recognition Event:** The Jarl grants the player a **Land-Grant** — a specific settlement or def
- `terr/settlement_layer_v30.md` L323: | Kronmark Watchtower | Fortified outpost | S-004 Kronmark | Guards northern approach to Valorsplatz; Defense +1 contribution to parent sett
- `terr/settlement_layer_v30.md` L327: | Ehrenfeld Citadel district | Fortress district | S-014 Ehrenfeld | Crown military HQ; Löwenritter base; Defense +2 to parent settlement |
- `terr/settlement_layer_v30.md` L428: | Fortify | Military-relevant stat + History | floor(Defense/2) + 1 | Defense +1 (cap: settlement type max) |
- `terr/settlement_layer_v30.md` L445: | Löwenritter | Fortress | Military efficiency: Defense +1 passive. Löwenritter governor uses Military as primary stat. Province faction ret
- `terr/settlement_layer_v30.md` L511: | Dissolution | No positive effect | Defense −1 AND Order −1 (substrate torn, structures weaken) |
- `terr/settlement_layer_v30.md` L514: | Lock | Defense +1 (configuration becomes architecturally permanent) | No settlement effect |

**Reads** (25 occurrences; samples):

- `prov/faction_politics_v30.md` L180: | **Martial** | Defense Committee | Hafenmark Militia rank ladder (provisional — see ED-640 below) | Hafenmark Military Commander |
- `prov/faction_politics_v30.md` L280: | **4** | **Bishop's Delegate** (Bischofslegat) | 3 completed Canon-rank Duties; plus one **Public Doctrinal Defense** — the player successf
- `prov/faction_politics_v30.md` L289: | **Fortitude / Military** | Jarnstal (canonical) | Templar ladder (Part 2, §2.4) | Dicastery for the Defense of the Faith |
- `prov/faction_politics_v30.md` L878: | **Defense Committee** | Hafenmark military (defensive); border garrisons; relations with Löwenritter | Martial-branch Parliamentarian | 1 
- `prov/faction_politics_v30.md` L897: | **Dicastery for the Defense of the Faith** | Fortitude (Jarnstal) | Templar deployment; monstrous-incursion response; enforcement | Templa
- `terr/settlement_layer_v30.md` L32: | **Seat** | Provincial capital. Administrative center. Court location. | Province-controlling faction | Prosperity, Defense, Population |


### Order  — DEF 8 · WRITE 32 · READ 83

**Definitions / scale:**

- `prov/faction_behavior_v30.md` L201: | mercantile-procedural | Order: 0.35, Utility: 0.25, Scholastic: 0.20, Liberty: 0.10, Equity: 0.10 |
- `prov/faction_behavior_v30.md` L204: | military-order | Honor: 0.30, Authority: 0.25, Virtue: 0.15, Identity: 0.15, Order: 0.15 |
- `terr/settlement_layer_v30.md` L43: **Derived values (derived_stats_v1 §4):** Settlement stats (Prosperity/Defense/Order, 0–5) produce derived values for the videogame layer:
- `terr/settlement_layer_v30.md` L49: | Order | Public Order | Order × 20 | Civil stability meter — below 0 triggers riot events |
- `terr/settlement_layer_v30.md` L59: | **Order** | Local institutional stability and compliance | Analogous to province Accord but at settlement scale. Order 0 = local revolt. O
- `terr/settlement_layer_v30.md` L156: These are **distinct from settlement Order** (Order = civil compliance, feeds province Accord via `floor(mean settlement Order)`, §1.3; L/PS
- `scene/derived_stats_v30.md` L374: | Order | **Public Order** | Order × 20 |
- `prov/peninsular_strain_v30.md` L146: **Order** (0–5) is a *settlement-level* attribute governing local stability within a specific settlement inside a territory. It is tracked p

**Direct writes / deltas:**

- `prov/faction_politics_v30.md` L168: | **3** | **Alderman** (Ratsherr) | **Formal Recognition Event:** Parliamentary vote of admission to a local council seat. Requires: Burgher
- `prov/victory_v30.md` L449: **Suppression — Crown (Enforce variant):** Pool = Military. TN 7. Ob 2. Success: −1 marker, Order −1 in target settlement. Failure: no marke
- `terr/settlement_layer_v30.md` L128: | Church | +1 Order at installation (one-time) |
- `terr/settlement_layer_v30.md` L129: | Cathedral | +1 Order at installation + Order decay −1 (Order is more stable) |
- `terr/settlement_layer_v30.md` L141: **Restrictions:** Pastoral Assumption does not change Provincial Authority — the province faction retains taxation, military, and legal fram
- `terr/settlement_layer_v30.md` L429: | Pacify | Charisma + local History | floor((3 − Order) + 1), min 1 | Order +1 (cap: 5) |
- `terr/settlement_layer_v30.md` L456: **Revoking management:** The province faction may revoke subnational management as a Domain Action (Influence, Ob = subnational faction's In
- `terr/settlement_layer_v30.md` L492: | Prosperity 0 | Famine or economic collapse. Population leaving. Order −1 automatic. |
- `terr/settlement_layer_v30.md` L496: | RM takes control of settlement | **Governance Transition scene** (historical_precedents_analysis §4.3). Player (or Vossen if NPC) chooses:
- `terr/settlement_layer_v30.md` L508: | Weaving | Order +1 (social configurations stabilize) | No settlement effect |
- `terr/settlement_layer_v30.md` L509: | Pulling | No positive effect | Order −1 (co-movement disrupts local configurations) |
- `terr/settlement_layer_v30.md` L511: | Dissolution | No positive effect | Defense −1 AND Order −1 (substrate torn, structures weaken) |
- `terr/settlement_layer_v30.md` L513: | Community Organizing | Order +1 AND Prosperity +1 (if PT ≤ 2 in province) | No settlement effect |
- `terr/settlement_layer_v30.md` L573: | Siege | Military ≥ Defense | No immediate roll. Each season: defender Order −1 (starvation/pressure). When Order = 0, settlement surrender
- `terr/settlement_layer_v30.md` L688: **Settlement succession:** When a settlement governor dies, is removed, or departs, the province faction must assign a new governor. If no e
- `terr/settlement_adjacency_v30.md` L110: - **Accord drop:** now applies to the **settlement's Order** (Order −1), not the province's Accord. Province Accord recalculates via floor-a
- `terr/settlement_adjacency_v30.md` L115: Siege (`settlement_layer §5.1`) runs per-settlement. Attacker holds adjacent position, cannot move, defender Order −1/season until Order = 0
- `prov/fractional_province_ownership_v30.md` L69: - **Submit:** settlement transfers to consolidating faction. Order −2 in that settlement. No battle.
- `prov/fractional_province_ownership_v30.md` L101: - **Partial:** A random non-Seat-held settlement's Order drops −1.
- `prov/fractional_province_ownership_v30.md` L126: - Submit: Market transfers back to Hafenmark at Order −2. Province unifies.
- `prov/peninsular_strain_v30.md` L148: They are independent: a province at Accord 2 (Compliant governance) may contain a settlement at Order 1 (simmering unrest). Turmoil threshol
- `prov/peninsular_strain_v30.md` L156: **The conquest cost is paid in Order, not Prosperity.** Per §2.4b above, Order at the affected settlements drops at conquest (typically −2 p
- `prov/peninsular_strain_v30.md` L175: | Seat | Military governor. Govern pool: Military. Govern Ob +1. Order −1 at onset. |
- `prov/peninsular_strain_v30.md` L189: | Social fieldwork: reach Disposition +3 with 2+ local NPCs in one settlement in one season | Settlement Order +1 (queued to Accounting) | P
- `prov/peninsular_strain_v30.md` L190: | Investigation: resolve a local concern affecting a settlement's population (Evidence Track threshold reached) | Settlement Order +1 (queue
- `prov/peninsular_strain_v30.md` L191: | Community Organizing in a settlement | Settlement Order +1 (queued to Accounting) | Settlement in territory with PT ≤ 2 AND Community Orga
- `prov/peninsular_strain_v30.md` L192: | Public violence: player initiates combat in settlement (public, 3+ witnesses) | Settlement Order −1 (immediate) | Combat Exposure ≥ 3 (pub
- `prov/peninsular_strain_v30.md` L193: | Assassination or killing of named NPC residing in settlement | Settlement Order −1 (immediate) | Dead NPC had Disposition ≥ +1 with local 
- `prov/peninsular_strain_v30.md` L194: | Player publicly defies controlling authority in a settlement | Settlement Order −1 (immediate) | Player's action is witnessed (Exposure ≥ 
- `prov/peninsular_strain_v30.md` L220: **Category A — Province-Level Set (Accord set to N):** Macro-political events that reset the entire province's relationship with its populat
- `prov/peninsular_strain_v30.md` L229: | Strain Crisis (§2.6 roll 7-8) | All non-capital settlements −1 Order | Capital settlements insulated by institutional presence |
- `prov/peninsular_strain_v30.md` L233: | Parliamentary action (faction_layer §9) | All settlements −1 Order | Economic sanctions affect entire province |

**Reads** (83 occurrences; samples):

- `prov/faction_layer_v30.md` L74: Crown holds the highest perceived strength at game start: highest Mandate, highest Wealth, capital + heartland territory (T1 Valorsplatz, T2
- `prov/faction_layer_v30.md` L78: Crown's standing army is the Löwenritter Order. All Crown military operations field Löwenritter units pre-coup. Crown faction Military stat 
- `prov/faction_layer_v30.md` L178: **Settlement targeting (AUD-SET-02):** Accord ±N rules in this document target specific settlements per peninsular_strain_v30 §2.5. Province
- `prov/faction_canon_v30.md` L182: | mercantile-procedural | Order 0.35, Utility 0.25, Scholastic 0.20, Liberty 0.10, Equity 0.10 | **Hafenmark** |
- `prov/faction_canon_v30.md` L185: | military-order | Honor 0.30, Authority 0.25, Virtue 0.15, Identity 0.15, Order 0.15 | **Varfell**, **Löwenritter** |
- `prov/faction_canon_v30.md` L451: Crown standing army is **Löwenritter Order** (`faction_layer §1.5`). All Crown military operations field Löwenritter units pre-coup. Crown f


### Public Order  — DEF 0 · WRITE 1 · READ 5

**Direct writes / deltas:**

- `scene/derived_stats_v30.md` L421: | Player wins with Overwhelming | Garrison Strength +20 + Public Order +5 |

**Reads** (5 occurrences; samples):

- `terr/settlement_layer_v30.md` L49: | Order | Public Order | Order × 20 | Civil stability meter — below 0 triggers riot events |
- `terr/settlement_layer_v30.md` L51: Settlement derived values feed upward to faction derived values: Local Economy contributes to faction Treasury income. Garrison Strength is 
- `scene/derived_stats_v30.md` L374: | Order | **Public Order** | Order × 20 |
- `scene/derived_stats_v30.md` L545: | Settlement | Order | **Public Order** | ×20 | PENDING |
- `ui/valoria_ui_ux_supplement_derived_settlement.md` L58: - **Detail panel shows:** Full stats, derived values (Local Economy, Garrison Strength, Public Order), facility slots, governor, Church infr


### Local Economy  — DEF 0 · WRITE 0 · READ 5

**Reads** (5 occurrences; samples):

- `terr/settlement_layer_v30.md` L47: | Prosperity | Local Economy | Prosperity × 50 | Gold income contribution to faction Treasury |
- `terr/settlement_layer_v30.md` L51: Settlement derived values feed upward to faction derived values: Local Economy contributes to faction Treasury income. Garrison Strength is 
- `scene/derived_stats_v30.md` L372: | Prosperity | **Local Economy** | Prosperity × 50 |
- `scene/derived_stats_v30.md` L543: | Settlement | Prosperity | **Local Economy** | ×50 | PENDING |
- `ui/valoria_ui_ux_supplement_derived_settlement.md` L58: - **Detail panel shows:** Full stats, derived values (Local Economy, Garrison Strength, Public Order), facility slots, governor, Church infr


### Garrison Strength  — DEF 0 · WRITE 4 · READ 6

**Direct writes / deltas:**

- `scene/derived_stats_v30.md` L420: | Player wins defense (repels attacker) | Garrison Strength +10 |
- `scene/derived_stats_v30.md` L421: | Player wins with Overwhelming | Garrison Strength +20 + Public Order +5 |
- `scene/derived_stats_v30.md` L422: | Player loses defense | Garrison Strength −10 |
- `scene/derived_stats_v30.md` L423: | Settlement falls during player defense | Garrison Strength → 0, Defense stat check Ob 2 at next Accounting |

**Reads** (6 occurrences; samples):

- `terr/settlement_layer_v30.md` L48: | Defense | Garrison Strength | Defense × 20 + Fort Level × 30 | Settlement defensibility score |
- `terr/settlement_layer_v30.md` L51: Settlement derived values feed upward to faction derived values: Local Economy contributes to faction Treasury income. Garrison Strength is 
- `scene/derived_stats_v30.md` L373: | Defense | **Garrison Strength** | Defense × 20 + Fort Level × 30 |
- `scene/derived_stats_v30.md` L418: | Combat Outcome | Garrison Strength Effect |
- `scene/derived_stats_v30.md` L544: | Settlement | Defense | **Garrison Strength** | ×20 + Fort | PENDING |
- `ui/valoria_ui_ux_supplement_derived_settlement.md` L58: - **Detail panel shows:** Full stats, derived values (Local Economy, Garrison Strength, Public Order), facility slots, governor, Church infr


### Treasury  — DEF 2 · WRITE 7 · READ 13

**Definitions / scale:**

- `ui/valoria_ui_ux_supplement_derived_settlement.md` L17: Wealth  ██████░░░░ 4      Treasury:  340/400  [▼ −60/season net]
- `ui/valoria_ui_ux_supplement_derived_settlement.md` L29: Treasury: 340/400 gold

**Direct writes / deltas:**

- `terr/settlement_layer_v30.md` L92: 2. **Settlement expands capacity** via Domain Action **Expand Institutional Capacity** (Treasury −300 (derived_stats_v1), scene action at se
- `terr/settlement_layer_v30.md` L499: | Mine type + Prosperity 3+ | Resource surplus. Province Treasury +50/season at Accounting (economic contribution, derived_stats_v1). |
- `scene/derived_stats_v30.md` L317: **When Wealth stat drops:** Treasury maximum drops (new max = Wealth × 100). Current Treasury retained. Recovery requires Trade actions.
- `scene/derived_stats_v30.md` L452: | Campaign Supply: Wealth −1/season | Treasury −100/season | mass_battle_v30 |
- `scene/derived_stats_v30.md` L456: | Siege supply: Wealth −1/season | Treasury −100/season | military_layer_v30 |
- `scene/derived_stats_v30.md` L468: | Settlement expansion: Wealth −3 | Treasury −300 | settlement_layer |
- `scene/derived_stats_v30.md` L469: | Mine surplus: Wealth +1 | Treasury +50/season | settlement_layer |

**Reads** (13 occurrences; samples):

- `terr/settlement_layer_v30.md` L47: | Prosperity | Local Economy | Prosperity × 50 | Gold income contribution to faction Treasury |
- `terr/settlement_layer_v30.md` L51: Settlement derived values feed upward to faction derived values: Local Economy contributes to faction Treasury income. Garrison Strength is 
- `terr/settlement_layer_v30.md` L169: - **Aggregation is settlement→faction directly**, consistent with the existing settlement→faction rollup (faction Treasury income = `Σ settl
- `terr/settlement_layer_v30.md` L177: **Consumers.** PP-686 Public Expectation strictness `base + 0.5·(L/7) − 0.3·(PS/7)` reads the faction **aggregate** L and PS defined above. 
- `scene/derived_stats_v30.md` L47: | Faction | ×10–100 | Treasury, Legitimacy, Reputation, Discipline | Seasonal interaction frequency (1–5 events/season). Each calibrated ind
- `scene/derived_stats_v30.md` L291: | Mandate | **Legitimacy** | Mandate × 20, starting = stat × 20 | Popular/institutional trust capital. 0–140 at Mandate 0–7 — a per-system d


### Fort Level  — DEF 0 · WRITE 0 · READ 9

**Reads** (9 occurrences; samples):

- `prov/military_layer_v30.md` L169: **Pool:** (Attacker Military stat) + 3 (siege engineering bonus — engineers, equipment, sapper crews), TN 7. **Ob:** 2 + Fort Level. *(PP-71
- `prov/military_layer_v30.md` L192: - Fort Level adds bonus dice to the defending pool (per existing rule)
- `prov/victory_v30.md` L263: **Fort interaction (PP-500, ED-355 resolved):** Fort Level does not modify Seizure Ob directly — it is already captured in the infrastructur
- `params/bg/faction_actions.md` L17: Roll: L vs Ob = floor(controlling faction L / 2) + 1 + Fort Level.
- `params/bg/faction_actions.md` L243: Roll: L vs Ob = floor(controlling faction L / 2) + 1 + Fort Level.
- `terr/settlement_layer_v30.md` L22: **Provinces are not changed.** All existing province-level mechanics (Accord, Piety Track, TCV, Fort Level, Calamity radiation, adjacency) c


### Fortification  — DEF 0 · WRITE 0 · READ 1

**Reads** (1 occurrences; samples):

- `terr/settlement_layer_v30.md` L58: | **Defense** | Fortification and garrison readiness | Determines Ob for attackers. Defense 0 = undefended (auto-capture). Defense 5 = major


### Population  — DEF 0 · WRITE 2 · READ 13

**Direct writes / deltas:**

- `terr/settlement_layer_v30.md` L324: | Lowenskyst Garrison Town | Civilian quarter | S-007 Lowenskyst Fortress | Soldiers' families; supply depot; Population +1 to parent; milit
- `terr/settlement_layer_v30.md` L333: | Spartfell Village | Civilian quarter | S-021 Spartfell Fortress | Border garrison support; Population +1 to parent |

**Reads** (13 occurrences; samples):

- `prov/faction_layer_v30.md` L274: - Occupation → automatic control transfer (3 seasons): Accord set to 1 (Resistant). Population endured 3 seasons of military occupation — th
- `prov/military_layer_v30.md` L350: ### §4.1 Accord as Population Commitment
- `prov/military_layer_v30.md` L396: | ED-NEW-MIL-01 | Population modifier to initial Size (Prosperity tiers). | **RESOLVED (PP-667)** — Prosperity 1-2: Size +0 · 3-4: Size +1 ·
- `terr/settlement_layer_v30.md` L32: | **Seat** | Provincial capital. Administrative center. Court location. | Province-controlling faction | Prosperity, Defense, Population |
- `terr/settlement_layer_v30.md` L33: | **City** | Major urban center. Trade, population, culture. | Province-controlling faction or Guilds | Prosperity, Population, Trade |
- `terr/settlement_layer_v30.md` L34: | **Town** | Smaller settlement. Local governance. Agricultural or resource base. | Province-controlling faction | Prosperity, Population |


### 4c — Territory / province


### Accord  — DEF 20 · WRITE 41 · READ 169

**Definitions / scale:**

- `prov/faction_layer_v30.md` L271: | Accord | May decline during Occupation from Stability effects (faction_layer §1.2 Trigger 1) — NOT frozen. Accord resets at control transf
- `prov/ci_political_v30.md` L421: Starting Accord: capitals = 3, all other home territories = 2. Per params_board_game.
- `prov/military_layer_v30.md` L354: | Accord | Battle effect | Muster effect |
- `prov/victory_v30.md` L44: | Accord | ≥ 2 in all directly-controlled territories |
- `prov/victory_v30.md` L63: | Accord | ≥ 2 in all territories controlled by each faction |
- `prov/victory_v30.md` L317: Altonian Ecclesiastical Accord (AEA) track 0–5. Milestone: AEA = 5 + CI ≥ 60 + Church controls T9 (Himmelenger). Indicates diplomatic route 
- `prov/victory_v30.md` L607: - **Resistance repulsion (during Occupation):** Underground Network Mandate ≥ 3 AND Governorate Accord = 0 in all occupied territories AND M
- `terr/settlement_layer_v30.md` L61: **Province Accord derivation (REVISED):** Province Accord is now the floor of the average Order across all settlements in the province, roun
- `terr/settlement_layer_v30.md` L705: | S07 Victory | Province Accord now derived from settlement Order averages. TCV unchanged. Universal victory still requires Accord ≥ 2 in al
- `terr/settlement_layer_v30.md` L750: | ED-SETT-03 | Province Accord derivation edge cases. | **RESOLVED** — single-settlement: Accord = that settlement's Order. Multi-settlement
- `terr/settlement_layer_v30.md` L768: | designs/board_game/victory_v30.md | Verify Accord ≥ 2 still functional with settlement-derived Accord. |
- `ui/valoria_ui_ux_supplement_derived_settlement.md` L59: - **Province Accord:** Displayed at province level above the settlement graph as "Province Accord: N (derived from settlement Order)"
- `params/bg/tracks.md` L109: | Accord | Name | Effective Prosperity | Other Effects |
- `prov/peninsular_strain_v30.md` L55: | Accord | Name | Effective Prosperity | Other Effects |
- `prov/peninsular_strain_v30.md` L68: **Derivation (authoritative, per settlement_layer_v30 §1.3 REVISED):** Province Accord = floor(mean Order across all settlements in the prov
- `prov/peninsular_strain_v30.md` L196: **Cap:** ±1 Order per settlement per season from personal-scale actions. Province Accord is derived at Accounting: floor(mean(settlement Ord
- `prov/peninsular_strain_v30.md` L204: | Accord | Environmental Description |
- `prov/peninsular_strain_v30.md` L218: Province Accord = floor(mean(settlement Order)) per settlement_layer_v30 §1.3. Existing Accord change rules operate as follows:
- `prov/peninsular_strain_v30.md` L422: | Accord | ≥ 2 in all directly-controlled territories |
- `prov/peninsular_strain_v30.md` L448: | Accord | ≥ 2 in all territories controlled by each faction |

**Direct writes / deltas:**

- `prov/faction_layer_v30.md` L178: **Settlement targeting (AUD-SET-02):** Accord ±N rules in this document target specific settlements per peninsular_strain_v30 §2.5. Province
- `prov/faction_layer_v30.md` L179: | Institutional consolidation | No Trigger 1–5 fired against this faction this season at Accounting | +1 (also: Accord +1 in one territory a
- `prov/faction_layer_v30.md` L212: **Step 2 — Territory transition.** All territories controlled by the collapsed faction become Uncontrolled. Accord in those territories drop
- `prov/faction_layer_v30.md` L228: **Collapse immunity:** A faction at Stability 1 that would be reduced to 0 by an Accounting Stability Check (§1.4) may invoke a one-time Sur
- `prov/faction_layer_v30.md` L475: Parliamentary Censure, Embargo, Blockade, and Outlawry reduce target Stability. If Stability drops to ≤ 2, Accord −1 in all territories cont
- `prov/faction_canon_v30.md` L290: - Institutional consolidation (no Trigger 1–5 fired this season): +1 + Accord +1 in one territory.
- `prov/ci_political_v30.md` L227: | Success | Accord +1 in target territory (max 3); OR Mandate recovery +1 if in capital (max starting Mandate, once/season, PP-174) |
- `prov/ci_political_v30.md` L228: | Overwhelming | Both: Accord +1 AND Mandate +1 in own capital (PP-174) |
- `prov/ci_political_v30.md` L251: | 5–6 | All factions: Accord −1 in one non-capital territory (controller's choice) |
- `prov/ci_political_v30.md` L252: | 7–8 | All factions: Accord −1 in ALL non-capital territories. Mandate check Ob 2 |
- `prov/ci_political_v30.md` L402: New: Govern Success in any territory = Accord +1. Govern OW in capital = Mandate +1 AND Accord +1.
- `prov/military_layer_v30.md` L363: **Revolt (Accord 0):** Any garrisoned unit fights a Popular Uprising each Accounting (Military vs Ob 2, existing rule). No new Muster possib
- `prov/victory_v30.md` L514: 2. **Löwenritter chain of command governs.** Ehrenwall (Grand Master) is acting head of government. Knight-Commanders govern Crown-held terr
- `prov/victory_v30.md` L601: **Altonian Alignment:** NPC faction AI — when NPC faction reaches Mandate ≤ 2, chance it secretly contacts Altonian Vanguard Commander. Not 
- `prov/strategic_layer_v30.md` L175: > **Battle Consequences (PP-647):** Each Battle resolved on Valorian soil: MS −1 (Campaign/War scale: MS −2). Each season with inter-faction
- `params/bg/faction_actions.md` L70: | Overwhelming | Church bishop-governor installed. Settlement governance transfers to Church. Accord +1 in settlement (population accepts — 
- `params/bg/faction_actions.md` L298: | Overwhelming | Church bishop-governor installed. Settlement governance transfers to Church. Accord +1 in settlement (population accepts — 
- `params/bg/faction_actions.md` L493: | Partial | No transfer. Hafenmark gains CB vs target. Target territory Accord −1. |
- `params/bg/faction_actions.md` L513: **Effect:** Accord +1 on Success (cap 2 via Martial Governance — Accord 3 requires standard Govern with Influence).
- `terr/settlement_layer_v30.md` L496: | RM takes control of settlement | **Governance Transition scene** (historical_precedents_analysis §4.3). Player (or Vossen if NPC) chooses:
- `terr/settlement_layer_v30.md` L544: - Settlement Accord −0.5 (population distrusts lawless governance).
- `scene/derived_stats_v30.md` L329: **When Legitimacy reaches 0:** Mandate check at Accounting (Ob 2). Failure: Mandate −1. Accord −1 in all territories.
- `scene/derived_stats_v30.md` L347: - Accord drops to 0 in any territory: −20
- `scene/derived_stats_v30.md` L409: | Accord drops in governed territory | Discipline −20 | Governor: Renown −1 |
- `terr/settlement_adjacency_v30.md` L110: - **Accord drop:** now applies to the **settlement's Order** (Order −1), not the province's Accord. Province Accord recalculates via floor-a
- `params/bg/tracks.md` L113: | 1 | Resistant | 0 | Govern Ob +1. Garrison required (≥ 1 unit) or Accord → 0 at Accounting. |
- `params/bg/tracks.md` L133: | 5–6 | Fracture | All factions: Accord −1 in one territory (lowest first). |
- `params/bg/tracks.md` L134: | 7–8 | Crisis | All factions: Accord −1 in ALL non-capital territories. L check Ob 2. |
- `prov/peninsular_strain_v30.md` L59: | 1 | Resistant | 0 (no Prosperity contribution) | Govern Ob +1. Garrison required (≥ 1 military unit) or Accord → 0 at Accounting. |
- `prov/peninsular_strain_v30.md` L60: | 0 | Revolt | Territory becomes Uncontrolled at Accounting | Garrison (if present) fights Popular Uprising: Military vs Ob 2. Win: territor
- `prov/peninsular_strain_v30.md` L150: **Both can reach 0 simultaneously.** When Province Accord 0 and Settlement Order 0 both trigger in the same territory at the same Accounting
- `prov/peninsular_strain_v30.md` L166: Löwenritter uses Accord but gains access to **Martial Governance**: a Govern variant using Military as pool instead of Influence. Accord +1 
- `prov/peninsular_strain_v30.md` L220: **Category A — Province-Level Set (Accord set to N):** Macro-political events that reset the entire province's relationship with its populat
- `prov/peninsular_strain_v30.md` L276: The Accord-based trigger means battle-occurrence does not directly advance IP. What advances IP is the *sustained inability* to bring conque
- `prov/peninsular_strain_v30.md` L280: **IP and Strain may advance from the same world-state** (e.g., a conquered Accord-1 territory contributes to both counts) but through separa
- `prov/peninsular_strain_v30.md` L320: | 5–6 | Fracture | All factions: Accord −1 in one territory (lowest-Accord first, controller's choice among ties). |
- `prov/peninsular_strain_v30.md` L321: | 7–8 | Crisis | All factions: Accord −1 in ALL non-capital territories. Mandate check Ob 2 at Accounting. |
- `prov/peninsular_strain_v30.md` L392: | Partial | Territory does not transfer. Hafenmark gains Casus Belli vs target (rejected claim = justification for force). Target territory 
- `prov/peninsular_strain_v30.md` L480: 1. Each territory at Accord 1: if no garrison present (no military unit from controlling faction), Accord → 0.
- `prov/peninsular_strain_v30.md` L482: 3. Passive normalisation: each territory with garrison present AND no hostile action this season for 2 consecutive seasons: Accord +1 (cap A

**Reads** (169 occurrences; samples):

- `prov/faction_layer_v30.md` L6: <!-- Integrates with: Phase 4 Priority-4 Social actions; Phase 5 Accounting steps 1–13; peninsular_strain_v1.md (Accord, Strain, battle cons
- `prov/faction_layer_v30.md` L109: **Accord on treaty-based control transfer (peninsular_strain_v1.md §2.3):**
- `prov/faction_layer_v30.md` L110: - Territory ceded via Truce or Peace: Accord set to 2 (diplomatic legitimacy).
- `prov/faction_layer_v30.md` L111: - Territory ceded via Capitulation: Accord set to 1 (population views cession as humiliation, resists new ruler).
- `prov/faction_layer_v30.md` L112: - Territory ceded via Tributary: Accord set to 2 (institutional continuity maintained).
- `prov/faction_layer_v30.md` L273: **Accord on Occupation resolution (peninsular_strain_v1.md §2):**


### Temperament  — DEF 2 · WRITE 0 · READ 8

**Definitions / scale:**

- `prov/faction_canon_v30.md` L162: | Temperament | α (outcomes) | β (conduct) | Period example |
- `terr/territory_temperaments_v30.md` L12: | Temperament | α (outcomes weight) | β (conduct weight) | Period example |

**Reads** (8 occurrences; samples):

- `prov/faction_canon_v30.md` L158: - **Popular Support** (faster-moving): active populace backing. Integrates Mission outcomes + Cascade Fidelity + random shocks per Public Te
- `prov/faction_canon_v30.md` L160: **Public Temperament** (per-territory, 5 types):
- `prov/faction_canon_v30.md` L245: ## §6 Public Temperament (per-territory)
- `terr/territory_temperaments_v30.md` L5: # Per-Territory Public Temperament (PP-686 v2 Phase B Stage 6)
- `terr/territory_temperaments_v30.md` L29: ## §2 Per-Territory Temperament Table
- `terr/territory_temperaments_v30.md` L31: | T | Name | Faction | Region / Sub | Temperament | α | β | Rationale |


---
*Generated from a 23-doc grep (`flatten_scan`). Occurrence lists capped per quantity; full grep on disk. R4/R7 advisories will fire on this doc itself — it documents write/formula lines (expected false positive).*
