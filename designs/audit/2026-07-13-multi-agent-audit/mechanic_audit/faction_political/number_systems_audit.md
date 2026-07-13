# Mode B — Number System Coherence: Faction / Political

## Inventory of scales in scope

| System | Range | Scale basis | Source |
|---|---|---|---|
| Faction stats: Influence / Wealth / Military / Intel | 1–7 | Renaissance-analogue tier scale | `faction_canon_v30.md` §5.1; `params/factions/stats_1_7_scale.md` |
| Faction Stability | 0–7 | Same 7-scale family | `stats_1_7_scale.md`; `faction_layer_v30.md` §1 |
| Mandate (derived faction headline) | 0–7 | Aggregation of per-settlement L/PS, saturating (K=6) | `faction_canon_v30.md` §5.1; `faction_behavior_v30.md` §4 |
| Legitimacy / Popular Support | 0–7 (per-**settlement**, not faction — LPS-1/LPS-2e) | Same 7-scale family | `settlement_layer_v30.md` §1.8 (cross-subsystem); referenced throughout faction docs |
| Rank Standing (per-faction ladder) | **0–7, plus −1 (Dismissed-with-Dishonor)** | Skyrim-Eight rank ladder | `faction_politics_v30.md` §1.0–§1.0a |
| Sub-office Standing (Löwenritter, Riskbreaker, Inquisitor, Templar, Guild, Niflhel, Warden) | 0–6 or 0–7 (varies by ladder — Riskbreaker tops at 6, Inquisitor/Templar cap at 5) | Parallel Skyrim-Eight, faction-specific top | `faction_politics_v30.md` Part 2 |
| Shadow Renown | 0–10 (cap; spills to Deniability Debt past 10) | Covert-mirror of public Renown (0–? scale, out of this subsystem) | `faction_politics_v30.md` §2.2b.i |
| Deniability Debt | 0–7 (cap 7) | Independent risk-accrual track | `faction_politics_v30.md` §2.2b.ii |
| Torben Generational Readiness / Readiness Track | "Accumulated Generational Readiness ≥5" trigger (§8.1) vs. "Readiness Track (0–10)" (§8.3) | NPC-specific maturation clock | `faction_politics_v30.md` Part 8 |
| Church Influence (CI) | 0–100 | Institutional-advancement clock, milestone-banded (40/55/65/80/100) | `faction_layer_v30.md` §9; cross-subsystem (`ci_political_v30`) |
| α (cascade blend weight) | 0–1 (clamped) | Continuous weighting coefficient | `faction_behavior_v30.md` §3.2.3 |
| Strictness | 0–1 (clamped) | Continuous deviation-cost modulator | `faction_behavior_v30.md` §3.6 |
| Cascade Fidelity | −1 to +1 | Cosine similarity | `faction_behavior_v30.md` §3.3.2 |
| Ob_modifier (final DA difficulty adjustment) | −2 to +2 (clamped, C1) | Sum of three sub-modifiers | `faction_behavior_v30.md` §3.7 |
| Casus Belli | binary presence + 1-season/3-season duration | Standing-right flag | `faction_layer_v30.md` §3.5 |

## Findings (Mode B)

### FA-B-01 — Rank Standing's documented range omits the −1 (Dismissed) state [P3]
`faction_politics_v30.md` §1.0 states the ladder is "an eight-position ladder (Standing 0 through
Standing 7)" — the top-level range statement for the whole Part 1 rank system. §1.0a (Demotion
Magnitude, ED-776) then introduces **Standing −1** ("Dismissed-with-Dishonor... Note that −1 is below
Standing 0") as a real, reachable, mechanically-distinct state (Excommunication, treason, permanent
Conviction-framework abandonment all route here). The top-level scale declaration is never amended to
say "−1 to 7." This is purely a documentation-completeness gap — the −1 state itself is fully
specified with its own effects, re-entry rules, and interaction table.
**Disposition: no action — working as intended; recommend the §1.0 header be updated to state the
true range (−1 to 7) at the next doc touch.** Not filed as a new ED (cosmetic).

### FA-B-02 — Torben's "Readiness" appears as two similarly-named tracks with different ranges [P2]
`faction_politics_v30.md` §8.1 defines a trigger condition "Accumulated Generational Readiness ≥ 5"
(accrues via specific Duties, capped +2/year-arc, no stated ceiling). §8.3, two paragraphs later,
introduces "Torben's internal **Readiness Track (0–10)**... tracked separately from his Disposition"
with its own threshold ("At Readiness ≥ 7, Torben exits ward status"). The document never states
whether §8.1's "Generational Readiness" and §8.3's "Readiness Track" are **the same variable** read at
two different thresholds (5 and 7), or two distinct tracks that happen to share the word "Readiness."
If they are the same track, the doc should say so explicitly and reconcile the "0–10" range statement
in §8.3 with the uncapped-sounding accrual language in §8.1. This is a genuine same-name /
different-scale ambiguity of exactly the kind Mode B is meant to catch (Torben's "Readiness" also
reads as an NPC-specific analogue of the player's 0–7 Standing track, using a different 0–10 range for
a structurally similar "how senior/prepared is this actor" concept, per §8.3's own framing —
"paralleling player Standing").
**Disposition: no action — flag for a documentation-clarity pass; recommend §8.1 and §8.3 be merged
into one explicit "Torben Readiness (0–10); Generational Trigger fires at ≥5, ward-exit at ≥7" spec.**
Not filed as a new ED — this is narrow (single-NPC mechanic), not load-bearing across the wider
faction system, and no gameplay-breaking ambiguity results (both thresholds are individually
well-specified even if their shared identity is unstated).

### FA-B-03 — Multi-scale zoo (0–7 / 0–10 / 0–100) is intentional, not a defect [no action]
The faction/political layer spans 0–7 (most faction and rank stats), 0–10 (Shadow Renown, Torben
Readiness, Public Instability — the last is cross-subsystem), and 0–100 (Church Influence). This was
explicitly reviewed and ruled non-defective in `references/canonical_sources.yaml`'s "Mandate x20
meter resolved (2026-05-30, mechanical-tier)" note: "NOT a defect — per derived_stats §3 multipliers
are per-system... no 0-100 master scale." Re-confirmed here rather than re-litigated.
**Disposition: no action — already resolved (see canonical_sources.yaml note, 2026-05-30).**

### FA-B-04 — Sub-office ladder ceilings are inconsistent by faction-specific design, not error [no action]
Riskbreaker tops at Standing 6 ("there is no rank above 'Commander'"), Inquisitor/Templar cap at
Standing 5 ("rank 5 IS the Cardinal"), while Löwenritter/Guild/Niflhel/Warden run the full 0–7. This
variance is explicitly justified per-ladder in `faction_politics_v30.md` (§2.2, §2.3, §2.4, §2.5) as
a structural feature of each sub-office's real ceiling (the rank above is a *different* named
position, not a numbering gap), and Part 9's parity table (§9.1–§9.3) explicitly audits and accepts
this variance ("cross-faction rank-at-same-Standing is equivalent" mechanically, even where flavor and
ceiling differ).
**Disposition: no action — reviewed, consistent with the corpus's own documented parity-audit
rationale.**
