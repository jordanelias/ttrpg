# Governance Type Registry (v1) — flags, vectors, and throughlines across the scale hierarchy

## Status: PROPOSED / REFERENCE — 2026-07-13 · Lane: IN (cross-cutting SE, FA, WR) · Jordan-vetoable. A registry and index over existing (mostly PROPOSED, some CANONICAL) content — claims no new mechanical canon by itself. §4's architecture proposal is genuinely new and unratified. No ED allocated yet.

**What this is.** Jordan's direct request (2026-07-13): survey all research and proposals touching
politics, governance, hierarchy, factions, and geography; inventory what applies at each level of
governance (duplicates across levels expected — that's the point); classify every type as a
**vectorized function** or a **flag/specific policy choice**; and use that classification to define "a
framework for propagation and dissemination, accumulation and dissipation... a surface for a wrapper and
keys." Compiled from four parallel corpus surveys (faction canon, settlement/territory canon,
cross-cutting clocks/tracks, the 58-item governance-compendium research corpus) plus the
generation-methodology stack (VSG's P-series, the F/R-series paradigm stacks) already synthesized this
session. Grounded against `designs/territory/scale_hierarchy_v1.md` (the ratified
Settlement→Territory→Province→Duchy→Country hierarchy + independent Faction tiers) and the **existing**
`designs/architecture/key_echo_armature_v1.md` substrate — this registry feeds that armature, it does not
replace it.

---

## §1 · The Flag/Vector taxonomy

**FLAG** — a discrete, specific policy choice: a boolean, a small enum, a named toggle, a staged state
machine. Selected *once* (or occasionally, on a trigger) by an authority; doesn't accumulate or blend.
Jordan's own example: **hostage-kin** (`faction_politics_v30.md §1.0c`) — a governor either takes the
bond or doesn't. Sub-kinds found in the corpus:
- **Binary toggle** — e.g. Church Governor axis, `codified_law` scope switch.
- **Small enum** — e.g. Directive type (Extract/Tax/Suppress/Install/Host/Cede), settlement Type
  (11-way), Entry Terms (Confirm/Impose).
- **Staged state machine** — e.g. IT-2 Condotta's Ferma→Aspetto→Lapsed, Territorial Occupation
  (none/foothold/occupied/transferred).
- **Threshold-derived event** — a FLAG that fires when a VECTOR crosses a line (CI milestone at
  40/55/65/80/100; MS band-crossing; Π≥8 forces a Crisis card). This is the single most common pattern
  in the corpus — nearly every VECTOR meter has at least one derived FLAG riding on it.

**VECTOR** — a continuous or multi-dimensional weighted quantity: accumulates, decays, aggregates,
blends. Jordan's own examples: **economic type, demographics, political sympathies**. Sub-kinds found:
- **Scalar meter** — e.g. Legitimacy/Popular Support (0–7), Suspicion, Π (0–10), MS (0–100).
- **Multi-axis distribution** — e.g. temperament α/β, the 9 political axes, ethic α/β.
- **Weighted portfolio** — e.g. Territorial Holdings (F4), demographic/caste composition.
- **Weighted aggregate-of-aggregates** — e.g. Faction Mandate (settlement L/PS, size-weighted),
  Province Accord (floor-mean of settlement Order).

**The dominant real pattern is neither pure FLAG nor pure VECTOR — it's VECTOR-with-derived-FLAGS.**
Treat this as the default expectation, not an edge case: a continuous meter that mostly behaves like a
VECTOR (accumulates, aggregates, sometimes decays) but periodically throws a discrete FLAG event when it
crosses a threshold. MS, CI, IP, Turmoil, Π, and Accord all follow this shape. This has a direct
consequence for §4: **the same underlying state variable typically needs both a Key (for the FLAG
moment) and a Field/Gauge mechanism (for the VECTOR body) — one substrate primitive cannot serve both
halves well**, per the Key & Echo Armature's own architecture (`key_echo_armature_v1.md §1`: a Key is a
typed, targeted, one-shot emission — it is not built to *be* a continuously-updated meter).

---

## §2 · The registry — organized by type-family, scale(s) noted per family

Deduplicated across all four survey passes; a family recurring at multiple scales is presented once with
every scale it was found at (this is the expected, intended shape — "duplicates are allowed across
levels" because the same dynamic really does recur).

### §2.1 · Structural / hierarchy primitives

| Type family | Scale(s) | Class | Citation | Note |
|---|---|---|---|---|
| Governance-type cascade (each tier sets the type below) | Country→Duchy→Province→Territory→Settlement | **FLAG** — each authority imposes one discrete governance-type enum on the tier below | `scale_hierarchy_v1.md §3` | Explicitly "a noisy cascading throughline," bidirectional |
| Consent/resistance gate on the cascade | Settlement (source) → all tiers above (modulated) | **VECTOR** | `scale_hierarchy_v1.md §4` | This IS Legitimacy/Popular Support (§2.3) — same mechanic, named at the structural level |
| Faction power-basis = people held, not territory | Faction-tier (local/provincial/national) | **VECTOR** — weighted aggregate of population × positional weight | `scale_hierarchy_v1.md §5.1` | — |
| Independence eligibility (any tier can secede from its faction holder) | Settlement/Territory/Province | **FLAG** — binary held/independent | `scale_hierarchy_v1.md §5.2` | Generalizes PP-726's old province-fracturing rule |
| Cross-scale faction claiming (skip-tier claim) | Settlement claimed by any faction tier | **FLAG** — discrete claim event, origin-exceptional | `scale_hierarchy_v1.md §5.2` | e.g. RM claiming one settlement directly |
| Chain-bypass authority (Monarch) | Country acting directly on any lower tier | **FLAG** — binary exemption from nested chain | `scale_hierarchy_v1.md §5.3` | — |
| Chain-bypass authority (Parliament) | Country-level body acting on any lower tier | **FLAG** — same structural exemption | `scale_hierarchy_v1.md §5.3` | Composes with existing Parliamentary Censure mechanics |
| Two-Tier Authority split (Provincial Authority vs. Settlement Governor) | Province↔Settlement | **FLAG** — structural dual-slot | `settlement_layer_v30.md §3.1` | "PA sets the rules, Governor executes" — the base-case cascade instance already built |

### §2.2 · Rank, Standing, and office (faction-membership ladders)

| Type family | Scale(s) | Class | Citation | Note |
|---|---|---|---|---|
| Standing/Rank ladder (0–7) + the 8-dimension "Skyrim Eight" template | Faction-tier (national), binds settlement/territory governor eligibility | **FLAG** — discrete named-position ladder | `faction_politics_v30.md §1.0–1.4` | — |
| Recognition Fork (Confirm vs. New-Grant) | Faction-tier, exercised over a settlement/territory-governing rank-holder | **FLAG** — binary choice by granting authority | `faction_politics_v30.md §1.0b` (ED-FA-0019) | "A graduated stonewalling lever" |
| Court Attendance (mandatory) | Territory/Province governor → capital | **FLAG** — binary compliance action | §1.0c (ED-FA-0020) | — |
| **Hostage-kin** | Faction ↔ Territory governor | **FLAG** — Jordan's own worked example | §1.0c (ED-FA-0020) | — |
| Patron-Sponsored Performance Audit toggle | Faction subordinate chain | **FLAG** — reversible overlay, auto-lapses with patron | §1.0d (ED-FA-0021) | Now RULED to MERGE into the suspicion/recall spine (D5+D6, `governance_consolidation_v1.md`) |
| Suspicion (accountability track) + its new decay counter (**E11**) | Settlement→Faction | **VECTOR** — cumulative, now paired with a symmetric decay term | `governance_consolidation_v1.md` D5/D6/E11 | Direct instance of the registry's "VECTOR needs a decay function" gap — closed here, not generic yet |
| Sub-office ladders (Löwenritter/Riskbreaker/Inquisitor/Templar/Guild/Niflhel/Warden) | Faction-tier, parallel not subordinate to primary ladder | **FLAG** — each a discrete parallel enum | `faction_politics_v30.md` Part 2 | — |
| Guild entry fork (Guarantor vs. Sole-patron) | Faction-tier (local) | **FLAG** | §2.5a (ED-FA-0023) | — |
| Guild mastership fork (Exam vs. capital-gated buy-in) | Faction-tier (local) | **FLAG** + durable "Upstart" tag | §2.5a (ED-FA-0022) | — |
| Ascendancy `power_base` (patronage/merit/kinship/bureaucratic/military/purchased/ideological) | Faction-tier, any level, NPC-grain | **FLAG** — single categorical field | `40_roster_officer_system.md §40.2.3` | The organizing field of the whole Ascendancy layer — 5 independent civilizations' proposals converge on this exact pattern (§3 below) |
| Ascendancy `consolidation_progress` (0–5) | Faction-tier, NPC-grain | **VECTOR** — continuous score, `power_base`-specific weighted formula | same | NERS-validated this session as the review's single strongest KEEP (92/100 downfall-exploitation) |
| Ascendancy downfall liability (structurally matched to `power_base`) | Faction-tier, NPC-grain | **FLAG** — discrete exploitable weakness, typed by `power_base` | same | "Every rise pays a structurally matched fall" |
| Shadow Renown / Deniability Debt | Faction-tier (Riskbreaker) | **VECTOR** — continuous meters, weighted multi-source accrual | `faction_canon_v30.md §2.2b` | — |
| Rank-decoupled-from-office pattern (see §3) | Faction-tier, all levels | meta-pattern, not a single type | multiple (BYZ-1/7, CHN-2, SE-JP3, HAB-2, IT-8) | — |

### §2.3 · The Legitimacy/Consent/Compliance spine

**This is the single most important cross-scale throughline in the whole registry** — see §3.

| Type family | Scale(s) | Class | Citation | Note |
|---|---|---|---|---|
| Legitimacy (L) / Popular Support (PS), 0–7 each | Settlement (source), aggregates to Faction | **VECTOR** — continuous, L slow-moving/legal-rational, PS fast-moving/charismatic | `settlement_layer_v30.md §1.8`; `faction_behavior_v30.md §3.4–3.5` | **Confirmed inert in `sim/` — 100/100, `lps_inert_check`.** The single highest-priority open wiring gap in the entire governance/generation thread (E5) |
| Faction Mandate (aggregate of settlement L/PS, size-weighted) | Faction-tier | **VECTOR** — saturating aggregate `round(7T/(T+K))` | `settlement_layer_v30.md §1.8` | D4-ruled to retire as the *collapse carrier* (masks peripheral collapse); replaced by floor-avg Order + province fracturing/independence + Standing Keys. Two-Mandates naming collision flagged, unresolved |
| Settlement Weight (size-weighting term for L/PS aggregation) | Settlement | **VECTOR** — composite `base(Type)+Prosperity+FacilityTier` | §1.8 | Operationalizes "size-weighted" aggregation |
| Weight-as-Exit (emigration) | Settlement↔neighbor | **FLAG** — discrete threshold-triggered loss + lateral transfer | §1.8c | A second, distinct cascade path from the L/PS acceptance channel |
| compliance(L) yield function | Settlement | **VECTOR** — continuous function of L, 50–100% Prosperity yield | `faction_layer_v30.md §5.9` | Levi's "quasi-voluntary compliance," made fiscally load-bearing — same underlying mechanic as the consent-gate, wearing a tax-yield costume |
| Province Accord (floor-mean of settlement Order) | Territory/Province (aggregates from Settlement) | **VECTOR** — live-recomputed on any child change, not periodic | `peninsular_strain_v30.md §2`; `clock_registry_v30.md` | Explicit bottom-up aggregation formula, the cleanest example in the corpus |
| Settlement Order | Settlement | **VECTOR** — 0–5, feeds Accord | `settlement_layer_v30.md §1.3/§2.1` | Moves only via named triggers — **no unforced decay term of its own** |
| Institutional Culture / Strictness (Public Expectation) | Faction-tier | **VECTOR** — continuous function of aggregated L/PS + role-template weights | `faction_behavior_v30.md §3.6` | — |

### §2.4 · Economic / fiscal

| Type family | Scale(s) | Class | Citation | Note |
|---|---|---|---|---|
| Fiscal Stance (Light/Standard/Extraction) | Faction-tier or per-Province declaration, effect lands at Settlement | **FLAG** — explicit 3-way discrete policy | `faction_layer_v30.md §5.9` (ED-FA-0008) | Textbook top-down policy-then-yield-function pair with §2.3's compliance(L) |
| Treasury | Faction-tier, aggregates from Settlement Prosperity | **VECTOR** — `Σ settlement Prosperity ×10` | `governance_ripple_substrate_v1.md §7` | No decay at the aggregate |
| Prosperity | Settlement (0–5) **and** legacy Territory (1–7, different range) | **VECTOR** at both grains | `clock_registry_v30.md` | **Unresolved same-name/different-scale/different-range collision** — flagged, not reconciled |
| Compact (proposed 5th ledger family) → recurring Debt subtype (D3-ruled) | Settlement | **FLAG** — discrete negotiated fixed-term obligation | §1.3a (ED-SE-0018/19); `governance_consolidation_v1.md` D3 | Confirmed live: writing it through the real 5-family ledger silently corrupts the schema, 100/100 |
| Ledger-of-Consequence tags (Precedent/Grudge/Debt/Reputation/Leverage) | Settlement | **FLAG** ×5 — discrete durable markers, TTL'd | `settlement_layer_v30.md` | Reputation is technically an enum label driven by continuous inputs — a VECTOR-derived FLAG |
| Charter tag (+ Patron field, Za model) | Settlement | **FLAG** — durable presence/absence, survives succession | §3.3a/§3.3b | Privilege durability derived from a separate actor's standing — explicit lateral-cascade dependency |
| Subnational Faction Governance-type (Church/Guilds/Ministry/Löwenritter/RM/Wardens/Niflhel) | Settlement, granted/revoked by Province | **FLAG** — discrete named manager-type enum | §3.3 | **This is the literal, already-built implementation of `scale_hierarchy_v1.md §3`'s "governance type" a tier sets on the tier below** — the new hierarchy doc's vocabulary retroactively names a mechanic that already exists |
| Quo Warranto (charter contest) | Settlement, lateral peninsula-wide echo | **FLAG** — discrete contest branch | §3.3a | Explicit lateral contagion: revoking one settlement's charter echoes to every settlement that faction-type manages peninsula-wide |
| Dearth chain (Granary stock 0–3, response-verb enum) | Settlement | Granary=**VECTOR**; response=**FLAG** | §4.3a | — |
| Grain-route dependency | Territory/Province | **FLAG** — source/dependent tag per settlement | §4.3b | Lateral geographic cascade: cutting a route puts every dependent settlement one season from Dearth |
| HRE-4 Borrow (financier loan against a named right) | Faction-tier/Settlement | **FLAG** — discrete instrument, own discovery/clawback state machine | governance-compendium (ED-FA-0029) | NERS-confirmed clean KEEP this session |

### §2.5 · Demographic / caste

| Type family | Scale(s) | Class | Citation | Note |
|---|---|---|---|---|
| Caste composition (Northern/Central/Southern Einhir) | Settlement/Territory/Province | **VECTOR** — weighted demographic proportions, baseline-TS differential | `faction_politics_v30.md §3.1`; `generation_sourcebook_v1.md` P9/R7 | Matches Jordan's own "demographics" worked example exactly |
| Caste × Rank-advancement gating table | Faction-tier, keyed by caste | **FLAG** — per-faction gate/favored/closed enum | §3.2 | — |
| Caste as Renown/Ob/Disposition modifier (3 separate mechanical hooks) | Territory/Faction-tier | **FLAG** ×3 — threshold rules, not weighted composites | §3.3–3.5 | — |
| Caste-transgressive Conviction risk | personal ↔ Faction-tier | **FLAG** — discrete trigger + threshold-gated crisis arc | §3.6 (ED-777) | — |

### §2.6 · Political sympathy / temperament / axes

| Type family | Scale(s) | Class | Citation | Note |
|---|---|---|---|---|
| Nine Political Axes (Sovereignty…Ontological) | Faction-tier, echoed at Territory/Province via casus belli | **VECTOR** — explicit multi-axis qualitative positioning | `faction_canon_v30.md §7` | Matches Jordan's "political sympathies" example exactly, at faction grain |
| Sociopolitical sympathies / Political allegiance (P11/P12) | Settlement | **VECTOR** — a spread/mix, not a single pick, co-varies with caste/piety/economy | `generation_sourcebook_v1.md §1.1` | "P11 vs. P2 is the fracturing engine" — explicit generator-level throughline |
| 5-typology territory temperament (α/β) | Territory (authored), aggregates to Faction, deferred to Settlement | **VECTOR** — population-weighted average across constituent settlements | `territory_temperaments_v30.md §1/§3`; `generation_sourcebook_v1.md` R4 | Jordan's VSG ruling (2026-07-13): "explore multiple temperaments whereby larger scales are partially informed by the aggregate of their constituent pieces" — directly actionable now that Territory is a real tier |
| Substrate-posture (F1, 6-value enum) | Faction-tier | **FLAG** — one structurally-distinct posture, "never a palette-swap" | `generation_sourcebook_v1.md §1.2` F1 | Binding constraint (M-4): every generated faction's posture must be structurally distinct |

### §2.7 · Cross-cutting clocks (the decay()-gap candidates)

| Type family | Scale(s) | Class | Citation | Decay/dissipation status |
|---|---|---|---|---|
| Mending Stability (MS) | Peninsula/global, graduated per-territory by node-distance | **VECTOR** (0–100) + derived FLAG band-crossings | `clock_registry_v30.md`; `ms_trajectory_v1.md`; `calamity_radiation_v30.md` | **Fully specified decay/recovery** — logarithmic recovery force + hysteresis (8-point asymmetric climb) + distance-based spatial falloff. The strongest existing precedent for a general dissipation-by-distance mechanic |
| Pressure (Π) | Settlement, peninsula-scale "Cooling flag" cascades into every settlement | **VECTOR** (0–10) + derived FLAG (≥8 forces Crisis) | `governance_play_redesign_v1.md §2.1` | **Fully specified homeostat** — the strongest existing precedent for a general decay() *function signature*: `clamp(Π + pressures − releases, 0, 10)`, plus a proposed second mean-reverting term (E1) |
| Church Influence (CI) | Global | **VECTOR** (0–100) + derived FLAG milestones (40/55/65/80/100) | `clock_registry_v30.md`; `ci_political_v30.md §2` | Only passive one-directional increase + an opposing-suppression lever — **no natural decay term** |
| Institutional Pressure (IP) | Global, aggregated from per-territory Accord-threshold count | **VECTOR** (0–100) + derived FLAG (IP≥100 world-state transition) | `peninsular_strain_v30.md §3.2/§4.4` | Stepwise aggregation specified; **no ordinary per-season decay specified** |
| Turmoil/Strain | Global, aggregated from per-territory Accord | **VECTOR** (0–10) + derived FLAG bands | `peninsular_strain_v30.md §4` | **Fully specified decay pair** (advance + explicit per-Accounting decay, capped) — a second strong decay() template |
| Piety Track (PT) + Spiritual Weight (SW) | Territory, PT aggregates upward into global CI | PT=**VECTOR** (dynamic); SW=**VECTOR but static** (fixed multiplier) | `ci_political_v30.md §1` | SW explicitly never decays by design; PT has no stated decay |
| Church Attention Pool | Territory | **VECTOR** (0–10) + derived FLAG (Inquisitor spawn thresholds) | `clock_registry_v30.md` | No decay — pure accumulator |
| Key & Echo Armature `decay()` (OF-3) | Substrate-wide, would serve all of the above with no bespoke logic | infrastructure, not itself a track | `key_echo_armature_v1.md §5.2` | **Deferred by Jordan's own 2026-07-07 ruling** ("to when cross-tick convergence work actually starts") — this registry is direct evidence that time has come; see §4 |

### §2.8 · Same-name / multiple-scale collisions (found, not yet resolved)

Worth its own table — these are real editorial hazards the survey surfaced, not part of the intended
"duplicates across levels" pattern (that pattern is the *same concept* recurring; these are *different*
concepts sharing one name):

| Name | Colliding definitions | Citation |
|---|---|---|
| Prosperity | Settlement (0–5, wired) vs. legacy per-Territory (1–7, board-game table, unclear if still live) | `clock_registry_v30.md` |
| Disposition | Personal/fieldwork (−5..+5, per-NPC-per-PC) vs. Settlement Local-Actor (−5..+5, same range, different subject pool, no cross-reference found) | `clock_registry_v30.md` |
| Guild Favour/Favor | Per-Territory (0–7) vs. per-Settlement (1–7, different start rule) | `clock_registry_v30.md` |
| Standing/Reputation | Faction-oscillating (0–5) vs. an apparently-higher-range personal/PC standing implied by "Standing-6+" gates elsewhere | `clock_registry_v30.md` vs. `governance_consolidation_v1.md` |
| Mandate | Settlement-derived faction meter (§1.8) vs. an unrelated CI-driven `settlement_mgmt` M12 parliamentary meter | D4 already flags this one explicitly, rename pending |

### §2.9 · Generation-layer paradigm stacks (meta — "types of types")

The F/R/P paradigm stacks (`generation_sourcebook_v1.md`, `settlement_generator_v1.md`) are themselves a
parallel classification of most of §2.1–§2.7's content, at the *authoring/generation-time* layer rather
than the *runtime* layer. Cross-referenced here rather than re-tabulated in full (see those docs
directly): **F1** substrate-posture=FLAG, **F3** stat block=VECTOR, **F6** emergence path=FLAG (gated by
VECTOR thresholds), **F7** political axes=VECTOR (§2.6); **R4** temperament=VECTOR (§2.6), **R6** calamity
exposure=VECTOR, **R9** political value/Franchise/Accord=VECTOR; **P8** economy=VECTOR (Jordan's own
worked "economic type" example), **P10** governance type=FLAG (the authoring-time analogue of the
runtime governance-type cascade in §2.1), **P12** sociopolitical sympathies=VECTOR (§2.6), **P13** actor
roster=mixed (power_base=FLAG, Standing=VECTOR, ethic α/β=VECTOR, leverage/Knots=FLAG-like).

---

## §3 · Recurring throughlines — the meta-patterns, independently found by multiple survey passes

Four survey agents, working independently over disjoint document sets, converged on the same handful of
structural patterns. That convergence is itself evidence these are real design grammar, not accidental
duplication:

1. **The consent/legitimacy gate wears three costumes.** `scale_hierarchy_v1.md §4`'s new claim that
   L/PS modulates whether an imposed governance type "sticks" is mechanically identical to
   `faction_behavior_v30.md`'s pre-existing Legitimacy/Popular-Support build/erode dynamics, and to
   `faction_layer_v30.md §5.9`'s `compliance(L)` tax-yield formula. Populace acceptance gating
   authority, gating faction standing, and gating extraction yield are **the same underlying mechanic**
   — political-cascade consent, faction-Mandate aggregation, and tax compliance are one dynamic in three
   presentations. Per the corpus's own subtractive doctrine (§8.2-A), this is a strong MERGE/DISTILL
   candidate: one canonical consent-gate formula, three read-sites.
2. **Weighted-cascade-with-noise is the corpus's own named design grammar**, applied to three different
   content domains: the Duke→Province→Territory→Settlement governance-type cascade (§2.1), the
   α-weighted Conviction Cascade through an NPC hierarchy (`faction_behavior_v30.md §3.2`), and
   Public/Territory Temperament's population-weighted drift under Strain (§2.6). All three are "weights
   bias, noise chooses, propagates top-down and bottom-up" — the same template, different payload.
3. **Rank/status decoupled from formal office**, independently generated by five different historical
   civilizations' research lanes (Byzantine Office/Dignity split and Pronoia revenue-without-governance;
   Chinese Examination Ladder bypassing sponsorship and the `power_base` merit/patronage split; Japanese
   Za patron-lapse and the Recognition Fork; Habsburg's informal-favorite Valido track; Italian
   examination-vs-purchase Mastership). This convergence is exactly why Part 40 promotes `power_base` to
   the *organizing field* of the whole Ascendancy layer rather than treating each instance as bespoke.
4. **Patronage-collapse liability**, paired symmetrically with rank/status decoupling: a patron's fall
   drags their clients down too (Byzantine guarantor-sponsorship, Chinese patron-bound audits, Japanese
   Za lapse, the hostage-kin lever) — named in the compendium's own taxonomy as one of eight general
   downfall shapes (M1) underlying ~96 historical cases. This is the mechanical spine behind the
   Ascendancy downfall table's Ω-d non-dominance claim, independently NERS-validated this session.
5. **Distance/time-based dissipation has real, working precedent already in the corpus** — MS's
   radiation-band falloff and hysteresis, and Π's homeostat clamp formula — even though the generic
   substrate-level `decay()` function (§2.7, §4) remains deferred. These two are the templates to
   generalize from, not blank-slate designs.

---

## §4 · Toward a wrapper-and-keys surface — propagation, dissemination, accumulation, dissipation

**Grounding first: this maps onto an existing substrate, it doesn't invent a new one.** The
`designs/architecture/key_echo_armature_v1.md` (RATIFIED 2026-07-07, ED-IN-0018/0026) already defines a
per-seam Key/Echo transport with directions — bottom-up, top-down, lateral, diagonal, outward, temporal —
and an executable core (`sim/substrate/keys.py`: `Key`, `KeyLog`, `TypeRegistry`, `TickScheduler`). The
four terms Jordan named map onto that existing vocabulary directly:

| Jordan's term | Existing armature direction | What §2's registry contributes |
|---|---|---|
| **Propagation** | Top-down (§2.2 of the armature) — "ONE Key, N `targets[]` entries... fan-out width never increments cascade_depth" | Every §2.1/§2.2/§2.4 FLAG (governance-type cascade, Directive type, Fiscal Stance) is a top-down Key emission already shaped for this; none currently registered as such |
| **Dissemination** | Lateral (§2.3) — scene-scale handoffs, and the fan-out-`targets[]` mechanism shared with top-down | Quo Warranto's peninsula-wide echo, grain-route cascade failures — genuine lateral (lattice, not tree) propagation the armature's §2.3 currently only exemplifies at scene-scale, not settlement-scale |
| **Accumulation** | Bottom-up (§2.1 of the armature) — Domain Echo, deferred-apply at Accounting boundary | §2.3's whole consent-gate spine (L/PS→Mandate, Order→Accord, PT×SW→CI, Prosperity→Treasury) — every one of these is a live bottom-up aggregation formula that should be a Domain-Echo-shaped Key rule but isn't yet registered as one |
| **Dissipation** | Temporal (§2.6 of the armature) + the **deferred `decay()` function (OF-3, §5.2)** | §2.7 is the direct evidence this deferral needs revisiting: MS and Turmoil already have hand-rolled, fully-specified decay math; CI/IP/Church-Attention-Pool have none at all. A generic `decay()` generalized from MS's hysteresis-and-falloff or Π's homeostat clamp would retire most of the bespoke logic and close the gap for the tracks that currently have nothing |

### 4.1 The real gap this registry exposes: Keys model FLAGs well, VECTORs poorly

Per §1's "dominant pattern" note: a Key (per `key_echo_armature_v1.md §1`) is a **typed, targeted,
one-shot emission** — exactly right for every FLAG in §2 (a Directive fires, a Charter tag writes, a
Recognition Fork resolves). It is structurally the wrong shape for a VECTOR's *continuous body* — L/PS,
Π, MS, Accord don't "emit," they *are*, continuously, between emissions. The armature already
half-recognizes this (Keys carry `stat_deltas` as payload, and Accord's write is explicitly
"deferred-apply target," not a Key itself) but has no named, general primitive for "a continuously-read,
continuously-written scale-tagged value that Keys deposit deltas into and that decays between deposits."
**Proposed name, pending Jordan's call: a `Field`** (or `Gauge` — naming not load-bearing, the mechanism
is) — parallel to `Key`, sharing the same `scale_signature`/`targets[]` discipline, but persistent and
continuously readable rather than one-shot-emitted, with a required `decay_fn` (closing OF-3 generically
instead of per-track) and a required `aggregate_fn` (for scales where the Field is itself derived from
child-scale Fields — e.g. Mandate's `round(7T/(T+K))`, Accord's `floor(mean(child.Order))`).

### 4.2 What a Field entry would need (schema sketch, not a ratified spec)

Modeled on `key_type_registry_v30.md §1`'s existing Key-type format, extended for continuous state:

```yaml
field_id: <family.subtype>          # e.g. consent.legitimacy, pressure.homeostat, clock.mending_stability
description: <one-line purpose>
scale_signature: [...]               # every scale this Field exists at (per §2's "duplicates across
                                      #   levels" pattern — one field_id, multiple scale instances)
range: <min, max>
aggregate_fn: <none | weighted_mean | floor_mean | sum | custom:ref>
                                      # how a parent-scale instance derives from child-scale instances
                                      #   (none = this Field has no children, it's a leaf)
propagate_fn: <none | cascade_with_noise:ref>
                                      # how a parent-scale instance's Field value informs (not
                                      #   overwrites) a child-scale instance's Field or governance-type
decay_fn: <none | linear:rate | homeostat:target,cap | hysteresis:thresholds | custom:ref>
                                      # closes OF-3 per-Field instead of leaving the substrate-wide
                                      #   decay() gap; §2.7's MS/Π formulas are the two working templates
derived_flags: [...]                 # threshold Key type_ids this Field fires when crossed (the
                                      #   VECTOR-with-derived-FLAG pattern from §1, made explicit)
emitting_systems / consuming_systems: [...]   # same discipline as key_type_registry_v30.md
```

### 4.3 What this section is and isn't

This is a **grounded proposal sketch**, not a ratified architecture change — it names the gap precisely
(§4.1), shows it's populated by real, already-designed working examples (§2.7's MS and Π), and offers a
schema shape consistent with the existing Key & Echo Armature's own conventions rather than inventing a
parallel vocabulary. Landing it for real is follow-on work: a `field_type_registry_v30.md` companion to
`key_type_registry_v30.md`, a `sim/substrate/fields.py` companion to `sim/substrate/keys.py`, and — the
actual unblock — Jordan finally ruling **OF-3's `decay()` fork** (deferred 2026-07-07, `key_echo_armature_v1.md
§5.2`), now with two working templates (MS, Π) and a registry's worth of tracks (§2.7, §2.8) that need it.

---

## §5 · What this registry does and doesn't do

**Does:** inventory governance/politics/hierarchy/faction/geography types across the whole researched
corpus (four independent survey passes + the generation-methodology stack already in this session's
context), classify each as FLAG/VECTOR/both, surface five genuine cross-scale throughlines independently
found by multiple passes, surface five same-name/different-scale naming collisions nobody had flagged
before, and sketch (not ratify) how the classification maps onto the existing Key & Echo Armature's
propagation/dissemination/accumulation/dissipation vocabulary plus the specific gap (`Field`, closing
OF-3) that vocabulary doesn't yet cover.

**Doesn't:** ratify any of the individually-cited proposals (their own dispositions — authored/
promote-ready/needs_jordan/cut — are unchanged by appearing here); resolve any of the §2.8 naming
collisions; rule OF-3's `decay()` fork (that's Jordan's, per the armature's own §5 docket); or commit to
the `Field`/`Gauge` name or exact schema in §4.2 (a sketch for review, not a spec).
