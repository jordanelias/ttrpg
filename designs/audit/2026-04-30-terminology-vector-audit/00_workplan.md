# Vector Audit — 2026-04-30 — Terminology focus

STATUS: AUDIT
RUN: 2026-04-30
PRECEDENT: designs/audit/2026-04-29-topographic-analysis/ (v3 reference run)
TRIGGER: Conversation request — comprehensive terminology conflict check + glossary, escalated to vector-audit (PP-679 skill) at user direction.

---

## §1 Scope

Surface terminology weaknesses unreachable by hand-curation of `references/glossary.md` ↔ `references/alias_registry.yaml`. The hand-curation pass produced 30+ findings against the two governance registries; this run re-executes those findings against the corpus's structural graphs and against today's body content for vocabulary debt.

**Audit corpus:** 47 design + discourse docs from `references/canonical_sources.yaml` `systems:` block + foundation canon + throughlines metadata. Mirrors the 2026-04-29 reference run for graph reuse.

**Audit name:** `terminology-vector-audit` — distinct from the 2026-04-29 `topographic-analysis` run (which was the methodology validation execution). This run reuses v3 graphs but reorients the weakness register to terminology drift, registry coverage, and conceptual overlap.

---

## §2 Pre-committed thresholds (LOCKED — methodology §3.7)

| Diagnostic | Threshold |
|---|---|
| Mode A multi-graph hubs | top quintile by degree in ≥ 3 of 4 graphs (cite, throughline, mu, pp) |
| Mode B implied-but-missing | ≥ 2 of {G_throughline, G_mu, G_pp} link AND no G_cite edge AND cross-class |
| Mode C notional | G_cite edge AND no metadata link |
| Mode D cascade-without-return | chain length ≥ 3 in G_cite, no return path |
| Mode E sparse-context | paragraph ≤ 10th percentile AND G_cite degree ≤ 10th percentile |
| Mode F throughline orphan | ≤ 2 substantiating paragraphs |
| Mode G vocabulary debt | direct grep against expanded struck-term list (see §3 below) |
| Mode H multi-graph isolates | max degree across all graphs ≤ 1 |

Tie-breaking: alphabetical token order. Class taxonomy (§3.4 of methodology) applied for Mode B cross-class filter.

**No threshold deviation. No post-hoc tuning.**

---

## §3 Mode G — expanded struck-term list

The 2026-04-29 reference run swept three terms (Game Master, Cultural Reformation, Coup Counter). This run expands the list to all struck/legacy terms parsed from:
- `canon/supersession_register.yaml` (VTM, CR strikes 2026-04-19)
- `references/alias_registry.yaml` `legacy_renames` block (Combat Power, Cohesion, Thread Depth, Rendering Stability)
- `references/alias_registry.yaml` `collision_table.tc` meaning_a (TC = Theocracy Counter, ED-782)
- Editorial actions ED-781 (Coup Counter), ED-764 (Niflhel as faction)
- Session log P1 sweep target (bare GM, distinct from "Game Master" bigram)

| Term | Pattern | Source authority | Notes |
|---|---|---|---|
| `VTM` | `\bVTM\b` | supersession_register VTM-STRIKE-2026-04-19 | |
| `Vaynard Thread Mastery` | full phrase | supersession_register | |
| `Cultural Reformation` | full phrase | supersession_register CR-STRIKE-2026-04-19 | |
| `Combat Power` | full phrase | alias_registry legacy_renames PP-232 → Power | |
| `Cohesion` | `\bCohesion\b` | alias_registry legacy_renames PP-232 → Discipline | |
| `Thread Depth` | full phrase | alias_registry legacy_renames PP-166 → REMOVED | |
| `Rendering Stability` | full phrase | alias_registry legacy_renames ED-731 → Mending Stability | |
| `Theocracy Counter` | full phrase | alias_registry collision_table tc | |
| `TC (as Church Influence)` | `\bTC\b` + context filter on `Theocracy\|Church\|Influence\|Mass Seizure\|seizure\|threshold\|Holy` | alias_registry collision_table tc / ED-782 | Context filter excludes Conviction-Track-context TC mentions |
| `Coup Counter` | full phrase | ED-781 conflict_architecture_proposal | Replacement: Graduated Autonomy |
| `Game Master` | full phrase | session log: GM sweep PP-678 partial | |
| `GM (bare)` | `\bGM\b` minus `Game Master` mask | session log: bare 'GM' corpus sweep TBD | Distinct from "Game Master" bigram — separately tracked |
| `Niflhel (as faction)` | `\bNiflhel\b` + context filter on `faction\|Mandate\|Influence\|grievance\|Operative\|Syndicate` | ED-764 Niflhel STRUCK params propagation | Place-references retained; only faction-context flagged |

**[STRUCK]/[SUPERSEDED] markers are exempt from action count** per Mode G recommendation in `references/diagnostic_modes.md`. Audit trail intentional.

---

## §4 Run configuration

| Parameter | Value |
|---|---|
| Corpus scope | full design + discourse (47 docs) |
| Token list | inherited from v3 (84 tokens, 70 seed + auto + legacy markers) |
| Disambiguation | inherited from v3 (Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity, Evidence, Consequence, Authority, Loyalty, Crown, Church) |
| Diagnostics | A · B · C · D · E · F · G · H |
| Validation | inherited from v3 (P1 corrected, P2 fail, P3 pass — 2/3 with neighbors_union fix) |
| Implicit citation threshold | ≥ 2 mentions (v3) |
| Random seed | 42 (inherited; no t-SNE in this run) |

**Inheritance disclosure (see §1 of `01_methodology.md`):** Structural graphs (G_cite, G_metadata, tokens, degrees) inherited from `designs/audit/2026-04-29-topographic-analysis/data/`. Mode G re-executed against today's corpus body content with expanded struck-term list. Modes A–F, H read inherited mode outputs; cross-referenced with terminology-relevant context for the weakness register.

**Inheritance is justified** by: (a) no mechanical content commits between 2026-04-29 and 2026-04-30 — the directive completed yesterday produced propagation-only changes, (b) v3 audit's pre-committed thresholds remain locked, (c) reference run's data/ is preserved (per skill output rule "never overwritten across reruns"), (d) reuse is explicit in this workplan and audit name distinguishes runs.

**Inheritance limit:** Mode G results SUPERSEDE v3 because today's corpus reflects PP-678 sweep effects.

---

## §5 Class taxonomy (inherited)

Applied for Mode B within-class filtering:

| Class | Members |
|---|---|
| conviction | Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity |
| pressure_point | Evidence, Consequence, Authority, Loyalty |
| faction | Crown, Church, Hafenmark, Varfell, Löwenritter, Restoration Movement, Guilds |
| npc | All named NPC tokens |
| clock | MS, CI, IP, PI, TS, TCV |
| system | Everything else |

---

## §6 Output structure

```
designs/audit/2026-04-30-terminology-vector-audit/
├── 00_workplan.md                  ← this file
├── 01_methodology.md               ← inheritance + execution provenance
├── 02_weakness_register.md         ← PRIMARY DELIVERABLE — all 8 modes, terminology focus
├── 03_validation_report.md         ← P1/P2/P3 outcome inherited + this run's confidence ceiling
└── data/
    ├── corpus_manifest.json        ← inherited (v3)
    ├── tokens.json                 ← inherited (v3)
    ├── auto_candidates.json        ← inherited (v3)
    ├── pilot.json                  ← inherited (v3)
    ├── g_cite_v3.json              ← inherited (v3)
    ├── g_metadata.json             ← inherited (v3)
    ├── degrees_v3.json             ← inherited (v3)
    ├── multigraph_diagnostics_v3.json  ← inherited (v3) — Modes A,B,C,D,E,F,H
    ├── citation_graph.json         ← inherited (v3)
    ├── validation_v3.json          ← inherited (v3)
    └── mode_g_2026-04-30.json      ← THIS RUN — expanded struck-term sweep on today's corpus
```

---

## §7 Confidence ceiling

Validation outcome is inherited from v3: **2/3 properties pass** (P1 corrected, P3 pass; P2 fail). Per skill output rule, all findings inherit this outcome — methodology is authoritative for hub/isolate/sparse findings but **conviction-symmetric findings are downgraded** (P2 fail means convictions lack lexical anchoring across throughlines). Since this run's terminology focus relies heavily on Mode H isolates and Mode G grep, both of which are independent of P2, confidence is **HIGH** for terminology findings and inherits HIGH for hub/isolate/cascade findings.

P2 fail remains a finding in its own right (see `03_validation_report.md` §3).
