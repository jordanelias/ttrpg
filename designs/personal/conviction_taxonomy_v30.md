<!-- [CANONICAL: 2026-05-01 — PP-684 v1 Conviction taxonomy; promoted from PROVISIONAL after Stage 10 sim PASS (12/14 battery; commits bb5e293 lateral + 3cb5207 articulation)] -->
<!-- STATUS: PROVISIONAL — Class A canonical document. -->
<!-- AUTHORITY: PP-684 (this doc); supersedes legacy "Reason / Continuity" Conviction labels and per-character anachronistic philosophical-tradition labels. -->

# Conviction Taxonomy (PP-684)

**Class:** A — personal-scale and faction-scale interpretive substrate.
**Status:** PROVISIONAL.
**Companion docs:** `designs/personal/conviction_axis_matrix_v30.md` (axis vectorization with calibration rationale); `designs/personal/conviction_migration_roster_v30.md` (per-character migration mapping).
**Co-files updated:** `references/glossary.md`, `references/alias_registry.yaml`, `canon/supersession_register.yaml`, `references/canonical_sources.yaml`.

---

## §1 Statement

A **Conviction** is a value-frame an actor holds that shapes how they interpret events. Convictions are vector-valued: an actor has weights across the canonical Conviction set, with structured concentration on a primary 1–3 Convictions plus a smaller distributed weight reflecting cultural background. Convictions project onto a 4-axis space (per `conviction_axis_matrix_v30.md`) for engine math; the vector representation is preserved for player legibility.

Convictions exist at both personal and faction scales. NPCs hold `personal_convictions` (and derived `effective_convictions` per faction Cascade math, PP-686 §3.2). Factions consume aggregate Conviction vectors for Mission alignment, Cascade resolution, and Public Expectation evaluation.

**Self-Other orientation** is a separate, orthogonal axis tracking whom an actor primarily benefits — themselves vs the broader populace. Greed, ambition, altruism, and self-sacrifice are represented along this axis, not as Convictions.

---

## §2 The 13 Convictions

| # | Conviction | Short description | Period equivalent |
|---|---|---|---|
| 1 | **Faith** | Devotion to ecclesiastical authority and theological order | *fides*, *pietas* |
| 2 | **Authority** | Deference to and assertion of legitimate command | *auctoritas*, *imperium* |
| 3 | **Order** | Procedural correctness, rule-following, institutional regularity | *ordo* |
| 4 | **Scholastic** | Reasoned inquiry, learning, scholarly method | *studium*, scholastic tradition |
| 5 | **Utility** | Effectiveness, results, instrumental judgment | *utilitas*, *ragion di stato* |
| 6 | **Equity** | Fairness across station; relief of injustice | *aequitas*, distributive concern |
| 7 | **Liberty** | Self-determination, freedom from imposed authority | *libertas* |
| 8 | **Precedent** | Reverence for ancestral practice; *what has been done* | customary law, *consuetudo* |
| 9 | **Community** | Belonging to the immediate community; common life | *communitas*, parish-belonging |
| 10 | **Identity** | Membership in a categorical group; tribe, lineage, faction | *gens*, lineage-honor |
| 11 | **Warden** | Stewardship of the dependent and the vulnerable | *cura*, paternal duty |
| 12 | **Virtue** | Cultivation of moral character; the good life | *virtù* (in the Aristotelian sense, distinct from Machiavellian) |
| 13 | **Honor** | Pledged oath, honor-code, reputation as binding | *honor*, chivalric and military code |

### §2.1 Why these 13 and not others

Each Conviction earns its place by appearing as a load-bearing dimension in Renaissance political and personal ethics:

- **Faith vs Order vs Authority** captures the medieval-Renaissance triad of papal, royal, and procedural sources of legitimacy.
- **Scholastic** is the inquiry-tradition (Aquinas, Salamanca School, scholastic universities); distinguishable from Faith.
- **Utility vs Virtue** is the Machiavellian / civic-humanist split (Machiavelli's *virtù* vs Aristotelian *virtus*; this taxonomy uses Virtue for the Aristotelian sense and represents Machiavellian instrumentalism via Utility + high Self-Other orientation).
- **Equity** is the canon-law fairness tradition (Bracton, Aquinas on distributive justice); distinguishable from Order.
- **Liberty** captures Florentine and Venetian republican ideology; *libertas* in its political sense.
- **Precedent** is customary-law and ancestral observance; distinct from Order (procedural) and Faith (theological).
- **Community vs Identity** is the localist-vs-categorical belonging split. Community is the parish, the village, the neighborhood; Identity is the lineage, the faction, the tribe. Different shapes of belonging; different action implications.
- **Warden** is paternal/protective duty (the lord's duty to peasants, the steward's to the household). Distinguishable from Equity (fairness) and Virtue (character).
- **Honor** is the pledged-oath and reputation-as-binding code (knightly, military, mercantile reputation). Necessary for sovereign and military-order role templates.

### §2.2 Axis-count caveat

The 4-axis vectorization (hierarchical / sacred / instrumental / traditional) collapses some distinctions. Notably: **Community and Identity score similarly** on these 4 axes (both moderately traditional, neither strongly hierarchical). A 5th axis (communal-vs-categorical, or relational-vs-formal) is permitted as a Class B extension if Stage 10 calibration finds the collapse load-bearing for downstream gameplay. Treated as deferred unless required.

### §2.3 Greed and ambition are not Convictions

Greed, ambition, and self-aggrandizement are *not* Convictions in this taxonomy. They are represented via **Self-Other orientation** (§3 below). A Utility-Conviction-dominated NPC can be either selfless (Self-Other negative; uses utility for collective benefit) or self-aggrandizing (Self-Other positive; uses utility for personal gain) — these produce different gameplay even with identical Conviction vectors.

This is deliberate. Cesare Borgia and a public-spirited republican magistrate may share a high Utility Conviction; what distinguishes them is *for whom* they instrumentalize. Self-Other captures that.

---

## §3 Self-Other Orientation

A scalar in `[-1, +1]` per actor:

```yaml
actor.self_other_orientation: -1.0..+1.0
```

| Range | Interpretation |
|---|---|
| -1.0..-0.5 | Self-sacrificing — outcomes attributed primarily to collective benefit |
| -0.5..-0.1 | Mildly altruistic — collective-leaning |
| -0.1..+0.1 | Neutral / balanced |
| +0.1..+0.5 | Mildly self-interested |
| +0.5..+1.0 | Self-aggrandizing — outcomes primarily personal benefit |

### §3.1 Effect on outcome attribution

When a faction-Mission outcome accrues to Popular Support (PP-686 §3.4), Self-Other orientation of the actor responsible modulates the attribution:

```
attributed_outcome = raw_outcome × (1 − 0.5 × max(0, orient))
```

Reading: a leader with orientation +0.8 (self-aggrandizing) receives 60% of the raw outcome's PS contribution (40% is "for himself" and doesn't add to faction PS). A leader with orientation 0 (neutral) receives 100%. A leader with negative orientation receives full 100% (no penalty for selflessness).

This is the C7 calibration from sim v2 §1.8. Provisional formula; future Stage 10 calibration may explore (a) full bidirectional scaling (negative orientation = altruism gives bonus), (b) non-linear scaling, (c) context-dependent scaling.

### §3.2 Drift

Self-Other orientation drifts under accumulated outcomes:

```
Δ orient per season = κ × Σ(outcome_with_self_benefit) − κ × Σ(outcome_with_collective_sacrifice)
```

where `κ` is a small drift constant (default 0.03; calibrate at Stage 10). Drift is bounded by `[-1, +1]` clamps.

This produces emergent character development: a leader whose Mission victories repeatedly enrich themselves drifts toward +; one whose decisions repeatedly favor the collective drifts toward −. Per artifact 10 §8.1.3 — this is the *Macbeth* arc, the *fall-from-grace* arc, the *moral-development* arc — emerging from accumulated outcomes rather than authored beats.

### §3.3 Initial values

Authored per character at scenario init. Default 0.0 if unspecified. Most NPCs start in `[-0.2, +0.2]` range. Outliers (named historical-equivalent figures) may start further. Player characters start at 0.0 unless scenario specifies.

---

## §4 Structured Concentration

Each NPC's `personal_convictions` is a 13-element vector with structured concentration:

```yaml
NPC.personal_convictions:
  primary:
    - conviction: <name>
      weight: 0.6..0.8
    # 1-3 entries; sum of primary weights = 0.6..0.8
  cultural_background:
    - conviction: <name>
      weight: 0.05..0.20
    # multiple entries; sum of cultural_background weights = 0.2..0.4
  # All other Convictions implicitly 0.
  # Sum across the entire vector = 1.0 after normalization.
```

### §4.1 Primary Convictions (1-3 per NPC, weight 0.6-0.8)

The NPC's defining frame. A Crown Captain might have `Authority: 0.5, Virtue: 0.3` as primary (sum 0.8). A republican magistrate might have `Liberty: 0.4, Equity: 0.4` as primary (sum 0.8). A village priest might have `Faith: 0.7` as primary alone.

### §4.2 Cultural background (distributed, weight 0.2-0.4)

Convictions that suffuse the NPC's culture but aren't their primary frame. A character raised in a Solmund Alpine valley carries Community + Warden + Precedent at low weights even if their primary is Liberty or Scholastic. This is the "ambient register" through which the NPC reads ambiguous events.

The cultural-background distribution comes from a **cultural background template** (§5).

### §4.3 Why this structure

Sim v2 confirmed (per artifact 06): structured-concentration NPCs produce *smoother* aggregate vectors and *more interpretable* armatures than flat 13-Conviction distributions. A village raised in the same culture share interpretive substrate; this is how factions of NPCs form coherent collective character at faction level.

The structure also reduces authoring overhead: a designer authors the NPC's *primary* (1-3 Convictions, simple choice) and a *cultural label* pointing to a template; the engine fills in the cultural background distribution from the template.

---

## §5 Cultural Background Templates

A cultural background template is a named distribution over the 13 Convictions, summing to 1.0 (the engine renormalizes against the NPC's primary weights).

### §5.1 Initial templates

Provisional set; calibrate at Stage 10 against character roster.

```yaml
varfell_alpine:
  description: "Varfell alpine culture — communal, devout, conservative"
  distribution:
    Faith: 0.20
    Community: 0.25
    Warden: 0.15
    Precedent: 0.20
    Identity: 0.10
    Authority: 0.05
    Order: 0.05

crown_lowland:
  description: "Crown lowland trading culture — pragmatic, civic, mobile"
  distribution:
    Utility: 0.20
    Order: 0.20
    Community: 0.10
    Liberty: 0.15
    Identity: 0.10
    Scholastic: 0.10
    Equity: 0.10
    Authority: 0.05

valorian_court:
  description: "Valorian sovereign court culture — hierarchical, honor-bound, virtuous"
  distribution:
    Authority: 0.20
    Virtue: 0.20
    Honor: 0.20
    Faith: 0.10
    Identity: 0.15
    Order: 0.10
    Precedent: 0.05

ecclesiastical:
  description: "Cathedral and monastic culture — devout, scholarly, traditional"
  distribution:
    Faith: 0.30
    Authority: 0.10
    Scholastic: 0.20
    Precedent: 0.15
    Order: 0.15
    Virtue: 0.05
    Warden: 0.05

hafenmark_procedural:
  description: "Hafenmark mercantile-procedural — rule-bound, calculative, civic"
  distribution:
    Order: 0.30
    Utility: 0.20
    Scholastic: 0.15
    Liberty: 0.10
    Equity: 0.10
    Community: 0.10
    Precedent: 0.05

lowenritter_military:
  description: "Lowenritter military-order — disciplined, honor-bound, loyal"
  distribution:
    Honor: 0.25
    Authority: 0.20
    Order: 0.15
    Faith: 0.10
    Identity: 0.15
    Warden: 0.10
    Virtue: 0.05

restoration_reformist:
  description: "Restoration reformist culture — egalitarian, idealistic, communal"
  distribution:
    Equity: 0.25
    Liberty: 0.20
    Community: 0.20
    Virtue: 0.10
    Scholastic: 0.10
    Identity: 0.10
    Faith: 0.05

einhir_traditional:
  description: "Einhir tradition — communal, ancestral, hardy"
  distribution:
    Community: 0.20
    Precedent: 0.25
    Identity: 0.15
    Warden: 0.15
    Faith: 0.10
    Honor: 0.10
    Virtue: 0.05
```

### §5.2 Composition rule

```
NPC.personal_convictions[c] = (
    primary_weight[c] +
    cultural_background_template[NPC.cultural_label][c] × (1 - sum(primary_weights))
)
# then normalize so total = 1.0
```

A primary `Authority: 0.5, Virtue: 0.3` (sum 0.8) means cultural background contributes the remaining 0.2 distributed per template. If template is `valorian_court`, the resulting full vector has Authority slightly boosted (primary + cultural_court_authority×0.2), Virtue slightly boosted, plus small contributions from Honor, Faith, etc.

### §5.3 Adding new templates

A new template is a Class B extension. Author distribution over 13 Convictions summing to 1.0; document cultural rationale; commit to this doc. PP-684 entry suffices.

---

## §6 Migration from Legacy Conviction Set

The legacy taxonomy used Reason / Continuity tags and assorted philosophical-tradition labels (Categorical Imperative, Virtue Ethics, Divine Command, Epistemic Reason, Rawlsian, Military Honor). These map to the new 13-Conviction set per `designs/personal/conviction_migration_roster_v30.md` (PP-685).

Common mappings (per-character migration in PP-685):

| Legacy label | Maps primarily to |
|---|---|
| Categorical Imperative | Virtue + (situational; some Order) |
| Virtue Ethics | Virtue (primary) |
| Divine Command | Faith (primary) |
| Epistemic Reason | Scholastic + (situational; some Utility) |
| Rawlsian | Equity + Liberty |
| Military Honor | Honor (primary) + Authority |
| Reason (legacy tag) | composite — see PP-685 per character |
| Continuity (legacy tag) | composite — see PP-685 per character |

Aliases in `references/alias_registry.yaml`:

```yaml
philosophical_tradition_legacy:
  canonical: "Conviction (taxonomy per PP-684)"
  legacy:
    - "Categorical Imperative"
    - "Virtue Ethics"
    - "Divine Command"
    - "Epistemic Reason"
    - "Rawlsian"
    - "Military Honor"
  patch: "PP-684"
  note: "Legacy philosophical-tradition labels superseded by 13-Conviction taxonomy. Per-character migration in PP-685."
```

---

## §7 Vetting Block (per PP-674 framework)

```yaml
vetting:
  class: A
  necessity: pass
  omega: pass
  mu: [Μ-α, Μ-γ]                 # primary modes: pressure, substrate ontology
  m_ratings:
    M-1: "+"   # extends — Convictions provide axis for continuous-pressure interpretation
    M-2: "○"
    M-3: "+"   # extends — Conviction vectors live in shared axis space, the substrate's interpretive layer
    M-4: "✓"
    M-5: "+"   # extends — same vocabulary at personal and faction scales bridges scale gap
    M-6: "✓"
    M-7: "✓"
    M-8: "✓"
    M-9: "+"   # extends — Self-Other drift is a new state-evolution dynamic
    M-10: "✓"
    M-11: "✓"
  q: pass
```

---

## §8 Open Items Resolved per Integration Plan §3.4

| Decision | Resolution |
|---|---|
| **D1** Honor as 13th Conviction | YES — Honor included as canonical 13th Conviction (load-bearing for sovereign and lowenritter_military role templates) |
| **D2** 4-axis count | 4 axes accepted; 5th axis as Class B extension if Stage 10 finds Community/Identity collapse load-bearing |

---

**End spec. PROVISIONAL pending ratification.**

### altonian_imperial
Roman-Byzantine amalgam. Imperial administrative tradition fused with civilizational mission.
- Authority: 0.08 — imperial governance as natural order
- Order: 0.07 — Roman legal-administrative structure
- Identity: 0.06 — Almaic civilizational belonging ("we are Rome")
- Precedent: 0.05 — Roman legal tradition, treaty obligations
- Virtue: 0.04 — Roman civic virtue (*virtus*, *pietas*)
- Scholastic: 0.03 — Byzantine intellectual tradition
- Honor: 0.02 — military discipline
- Remaining convictions: 0.00
- Total: 0.35
