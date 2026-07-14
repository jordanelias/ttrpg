# Governance Research Corpus — Manifest

## Status: RESEARCH — filed 2026-07-14 · Lane: IN · ED-IN-0064 · analytic/reference, not a design ratification

**What this is.** A durable, thematically-organized comparative-governance research corpus for Valoria,
produced to inform the multi-scale governance / decision-surface design pass. It reorganizes and
deepens the prior civ-organized research (`designs/audit/2026-07-08-fa-se-historical-precedent-research/`,
`designs/audit/2026-07-09-comparative-governance-research/`) into three **theme-scoped** documents, each
spanning **8 historical civilizations**, with an explicit `=> Valoria design hook` mapping every
substantive historical pattern to a specific Valoria mechanic.

**Why it lives here.** Committed as durable repository files (not left in a branch/chat subject to
compaction), under the top-level `research/` convention (precedent: `research/pre_firearms_formations/`,
`research/rhetoric_oratory_contest/`).

## Method (agonist → antagonist, model-tiered)

A multi-agent Workflow ran, per civilization: a **Sonnet** researcher produced a deep brief across all
three themes (model knowledge + web grounding), then an **independent Opus verifier** adversarially
audited it — factual corrections, over-claims, anachronisms, surface-analogy hooks, and
Mandate-of-Heaven leakage. The 8 verified briefs were reorganized by theme (deterministic assembly),
and per-theme **Opus** cross-civilizational synthesizers added the synthesis intro + consolidated
design-hooks table. Every verifier verdict was `SOUND_WITH_FIXES`; the correction notes are quoted
inline before each per-civilization section.

## Coverage — 8 civilizations × 3 themes

Byzantine Empire is **omitted from this pass** (its research agent was interrupted; the design lead
opted to proceed with the eight completed civilizations and add Byzantium later if wanted).

| Civilization | modes | hierarchy / standing | conflicts | verifier |
|---|:-:|:-:|:-:|---|
| Ottoman Empire | ✓ | ✓ | ✓ | SOUND_WITH_FIXES |
| Roman Empire (Republic → Principate → Dominate) | ✓ | ✓ | ✓ | SOUND_WITH_FIXES |
| Carolingian Empire | ✓ | ✓ | ✓ | SOUND_WITH_FIXES |
| Holy Roman Empire | ✓ | ✓ | ✓ | SOUND_WITH_FIXES |
| Renaissance Europe (Florence / Milan / Genoa + Papal States) | ✓ | ✓ | ✓ | SOUND_WITH_FIXES |
| Republic of Venice | ✓ | ✓ | ✓ | SOUND_WITH_FIXES |
| Han Dynasty & Three Kingdoms China | ✓ | ✓ | ✓ | SOUND_WITH_FIXES |
| Shogunate Japan (Kamakura / Ashikaga / Sengoku / Tokugawa) | ✓ | ✓ | ✓ | SOUND_WITH_FIXES |

## Documents

| File | Theme |
|---|---|
| `governance_modes.md` | Modes of governance — decision procedures, legitimation, institutions; mapped to the PROPOSED 8-value `governance_mode` taxonomy. |
| `political_hierarchy_standing.md` | Rank/office hierarchy, advancement & demotion/removal routes; mapped to the `faction_politics` Standing ladder, Demotion Magnitude, and the resolution-quality→standing bridge. |
| `conflicts_power_struggles.md` | Succession crises, usurpations, civil wars, factional strife, ruler-vs-assembly collisions; mapped to the emergent-friction/churn systems and the collision-of-stresses primitive. |

Each document = a header + a **cross-civilizational synthesis** (patterns that recur / vary + a
consolidated design-hooks table) + the exhaustive **per-civilization detail** sections.

## Conventions

- **`=> Valoria design hook:`** lines map a historical pattern to a specific Valoria mechanic. These are
  **proposals for the design pass, not ratified canon.**
- **Mandate of Heaven is history only** — per the design-lead ruling it is **never** proposed as a
  Valoria mechanic. Legitimacy-collapse / two-signal-collision / relief-valve hooks are grounded on
  **non-MoH** precedent (Roman/Byzantine dual-trigger usurpation, Ottoman grand-vizier-as-scapegoat +
  Janissary revolts, imperial penance/recusatio, Polybian regime-cycle).

## Downstream

Feeds the `designs/audit/2026-07-14-scale-chain-and-decision-surface-map/` chain/gap analysis docket
(decision-surface fills, governance-mode taxonomy grounding, non-MoH re-groundings) and the eventual
governance-mode + per-scale decision-surface design pass.
