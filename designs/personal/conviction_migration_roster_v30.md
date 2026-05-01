<!-- [PROVISIONAL: 2026-05-01 — PP-685 v1, Conviction migration roster, ratified per integration plan §3.2 commit 2] -->
<!-- STATUS: PROVISIONAL — Class A canonical mechanical document. Maps existing characters from legacy Conviction labels to PP-684 13-Conviction taxonomy. -->
<!-- AUTHORITY: PP-685 -->

# Conviction Migration Roster (PP-685)

**Class:** A — mechanical bookkeeping for taxonomy migration.
**Status:** PROVISIONAL.
**Reads:** `designs/personal/conviction_taxonomy_v30.md` (PP-684).
**Companion:** `designs/personal/conviction_axis_matrix_v30.md`.

---

## §1 Purpose

Existing character canon references "Reason" and "Continuity" Conviction tags plus assorted philosophical-tradition labels. PP-684 supersedes these. This roster maps each named character to the new 13-Conviction taxonomy with structured concentration (primary 1–3 Convictions + cultural background template).

Each entry specifies:

```yaml
character_name:
  prior_labels: [...]              # what was used before
  primary_convictions:
    - {conviction: <name>, weight: <0.6..0.8 sum>}
  cultural_label: <template_name>  # from §5 of conviction_taxonomy_v30
  self_other_initial: <-1.0..+1.0>
  notes: <migration rationale>
```

Per-character authoritative until promotion to canonical character sheets.

---

## §2 Migration Mappings (Named Characters)

The following 13 named characters appear in canon with prior Conviction tags. Migration mappings are recommendations per integration plan default; specific overrides per Jordan or designer will land as Class B amendments to this roster.

### §2.1 Sovereign Court (Crown faction)

#### Almud (Crown Captain, currently Crown leader per sim continuity)

```yaml
prior_labels: ["Virtue Ethics", "Reason"]
primary_convictions:
  - {conviction: Virtue, weight: 0.45}
  - {conviction: Authority, weight: 0.30}
cultural_label: valorian_court
self_other_initial: -0.10
notes: |
  Per sim v2 §1.8 baseline (Virtue:0.6, Authority:0.4 → smoothed via cultural background).
  Self-Other slightly altruistic — public-spirited Captain archetype.
  Honor Conviction enters via valorian_court cultural template.
```

#### Cesare (Crown succession alternate per sim §1.2)

```yaml
prior_labels: ["Reason", "Military Honor"]
primary_convictions:
  - {conviction: Authority, weight: 0.40}
  - {conviction: Utility, weight: 0.30}
cultural_label: valorian_court
self_other_initial: +0.40
notes: |
  Per sim v2 §1.2 (Authority:0.5, Utility:0.5 baseline; structured to 0.40+0.30).
  High Self-Other captures the Cesare Borgia signature — instrumental Authority for self-aggrandizement.
  Honor enters via valorian_court but at low weight; Cesare's signature is anti-Honor on principal-of-utility grounds.
```

#### Lorenzo (Crown succession alternate per sim §1.2)

```yaml
prior_labels: ["Virtue Ethics", "Epistemic Reason"]
primary_convictions:
  - {conviction: Virtue, weight: 0.35}
  - {conviction: Scholastic, weight: 0.30}
  - {conviction: Authority, weight: 0.10}
cultural_label: valorian_court
self_other_initial: -0.20
notes: |
  Per sim §1.2 (Virtue:0.5, Scholastic:0.4, Authority:0.1 baseline).
  Mildly altruistic — principled-scholar archetype.
```

### §2.2 Solmund / RM Faction

#### Yrsa Vossen (RM leader; per PP-665 rename from Maret Vossen)

```yaml
prior_labels: ["Continuity", "Military Honor"]
primary_convictions:
  - {conviction: Honor, weight: 0.35}
  - {conviction: Warden, weight: 0.25}
  - {conviction: Community, weight: 0.20}
cultural_label: solmund_alpine
self_other_initial: -0.30
notes: |
  Strong Continuity legacy → primary on Honor (oath-bound) + Warden (stewardship of dependents) + Community.
  Alpine cultural background reinforces Community / Precedent.
  Self-Other strongly altruistic — leader-protects-people archetype.
```

#### Maret Uln (Varfell; per PP-665 not renamed)

```yaml
prior_labels: ["Reason", "Military Honor"]
primary_convictions:
  - {conviction: Honor, weight: 0.30}
  - {conviction: Authority, weight: 0.30}
  - {conviction: Identity, weight: 0.20}
cultural_label: lowenritter_military
self_other_initial: +0.10
notes: |
  Military-honor archetype with Identity (Varfell categorical loyalty).
  Mild self-interest — pragmatic warlord rather than self-sacrificing or self-aggrandizing.
```

#### Solmund (the figure, per designs/world/solmund_v30.md)

```yaml
prior_labels: ["Virtue Ethics", "Divine Command", "Continuity"]
primary_convictions:
  - {conviction: Virtue, weight: 0.30}
  - {conviction: Faith, weight: 0.25}
  - {conviction: Warden, weight: 0.20}
cultural_label: solmund_alpine
self_other_initial: -0.50
notes: |
  Founding figure; archetype of selfless protective Virtue-Faith-Warden composite.
  Strong altruism. Honor enters via cultural template at low weight.
  Note: per project naming directive, always Solmund, never Galbados.
```

### §2.3 Ecclesiastical Faction (Cathedral)

#### Cardinal Reichard (per artifact 15 sample)

```yaml
prior_labels: ["Divine Command", "Continuity"]
primary_convictions:
  - {conviction: Faith, weight: 0.40}
  - {conviction: Precedent, weight: 0.20}
  - {conviction: Authority, weight: 0.15}
cultural_label: ecclesiastical
self_other_initial: +0.10
notes: |
  Senior cardinal archetype. Primary Faith with strong Precedent backing.
  Mild self-interest captures the institutional-positioning behavior shown in artifact 15.
```

#### Baralta (per designs/npcs/baralta_v30.md)

```yaml
prior_labels: ["Divine Command", "Virtue Ethics"]
primary_convictions:
  - {conviction: Faith, weight: 0.50}
  - {conviction: Virtue, weight: 0.20}
  - {conviction: Warden, weight: 0.10}
cultural_label: ecclesiastical
self_other_initial: -0.40
notes: |
  Theological-position figure; strong primary Faith with Virtue-Warden secondary.
  Selfless devotional archetype.
```

#### Lenneth (per designs/npcs/npc_character_analyses_v30.md, ED-727)

```yaml
prior_labels: ["Epistemic Reason", "Continuity"]
primary_convictions:
  - {conviction: Scholastic, weight: 0.40}
  - {conviction: Faith, weight: 0.20}
  - {conviction: Precedent, weight: 0.20}
cultural_label: ecclesiastical
self_other_initial: -0.10
notes: |
  Scholarly cleric with TS pathway per ED-727. Slow scholarly loosening over time captured by potential Self-Other drift toward 0 or +.
```

### §2.4 Hafenmark Faction

#### Hafenmark Speaker (placeholder name; specific character in PP-685 finalization)

```yaml
prior_labels: ["Rawlsian", "Reason"]
primary_convictions:
  - {conviction: Order, weight: 0.40}
  - {conviction: Equity, weight: 0.20}
  - {conviction: Utility, weight: 0.15}
cultural_label: hafenmark_procedural
self_other_initial: 0.00
notes: |
  Procedural-civic archetype. Rule-bound with fairness backing and pragmatic Utility.
  Neutral Self-Other — institutional position rather than personal stake.
```

### §2.5 Lowenritter Faction

#### Lowenritter Master (placeholder name)

```yaml
prior_labels: ["Military Honor", "Continuity"]
primary_convictions:
  - {conviction: Honor, weight: 0.35}
  - {conviction: Authority, weight: 0.25}
  - {conviction: Identity, weight: 0.20}
cultural_label: lowenritter_military
self_other_initial: -0.10
notes: |
  Military-order leader archetype. Strong Honor with Identity (categorical loyalty to the Order) and Authority.
```

### §2.6 Restoration Faction

#### Restoration Spokesperson (placeholder)

```yaml
prior_labels: ["Rawlsian", "Virtue Ethics"]
primary_convictions:
  - {conviction: Equity, weight: 0.30}
  - {conviction: Liberty, weight: 0.30}
  - {conviction: Community, weight: 0.15}
cultural_label: restoration_reformist
self_other_initial: -0.30
notes: |
  Reformist-egalitarian archetype. Strong Equity-Liberty paired with Community grounding.
```

### §2.7 Niflhel Faction

#### Niflhel envoy (placeholder)

```yaml
prior_labels: ["Reason"]
primary_convictions:
  - {conviction: Scholastic, weight: 0.30}
  - {conviction: Utility, weight: 0.30}
  - {conviction: Authority, weight: 0.10}
cultural_label: hafenmark_procedural
self_other_initial: +0.20
notes: |
  Intelligence-diplomatic archetype. Scholastic-Utility composite with mild self-interest.
  Cultural background placeholder; replace with niflhel-specific template post-Stage-10.
```

---

## §3 Edge Cases (D-decision class)

The following migrations are flagged for designer review during Stage 10 calibration. Default mapping suggested; revise per character's narrative needs:

| Character | Issue | Default mapping |
|---|---|---|
| Solmund | Pre-Altonian, possibly pre-Einhir per ED-728; cultural template needs review | solmund_alpine (placeholder) |
| Vaynard (per PP-650 STRUCK; see canonical_sources struck) | Was tied to Cultural Reformation (struck) and VTM (struck) — Conviction profile needs clean redraft | Authority + Honor + Identity, lowenritter_military background; orientation +0.20 (pragmatic militarist) |
| Captain Vossler (sim continuity per artifact 15) | New character introduced in artifact 15 sample chronicle; needs full sheet | Honor + Warden + Identity (military-order); solmund_alpine; -0.20 |
| Captain Reinholt (sim continuity per artifact 15) | New character; needs full sheet | Honor + Authority + Order; valorian_court; 0.00 |

These four are flagged for Phase B per-character review. Default mappings are *placeholders*; the integration plan §3.4 D11 deferred per-character refinement to authoring time.

---

## §4 Migration Process

For each character not in this roster:

1. Identify prior Conviction tags in canon.
2. Choose 1–3 primary Convictions with weights summing to 0.6–0.8.
3. Select cultural_label from the 8 templates (PP-684 §5).
4. Set initial Self-Other orientation per the character's archetype.
5. Append entry to this roster as Class B extension.

If a character has no prior Conviction tags (legacy era characters), default:

```yaml
primary_convictions:
  - {conviction: <inferred from role>, weight: 0.6}
cultural_label: <inferred from origin>
self_other_initial: 0.00
notes: "Defaults applied per PP-685 §4; revise on first canon pass."
```

---

## §5 Open Items Resolved per Integration Plan §3.4

| Decision | Resolution |
|---|---|
| **D1** Honor as 13th Conviction | Yes — used in §2.2/§2.3/§2.5/§2.6 mappings |
| **685-3** Edge-case migration | Per-character review at Phase B; defaults provided in §3 |

---

**End roster. PROVISIONAL pending ratification.**
