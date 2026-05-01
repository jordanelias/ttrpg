# Vector Audit — 2026-04-30 — Methodology (executed parameters)

STATUS: AUDIT
RUN: 2026-04-30
SKILL: skills/valoria-vector-audit (v3 multi-graph triangulation)
PRECEDENT: designs/audit/2026-04-29-topographic-analysis/

---

## §1 Inheritance disclosure

This run **inherits structural graphs and Modes A–F, H** from the 2026-04-29 reference run. Only Mode G is re-executed against today's corpus.

| Stage | Inherited from 2026-04-29? | Source |
|---|---|---|
| 0. Pilot validation | YES | `data/pilot.json` (8/8 tokens, top-3 neighbors intuitive) |
| 1. Corpus extraction + banner classifier | YES | `data/corpus_manifest.json` (47 docs: 43 design + 4 discourse) |
| 2. Token curation (seed + auto + legacy) | YES | `data/tokens.json` (84 tokens) |
| 2.5. Expanded citation graph | YES | `data/g_cite_v3.json` (29 source-tokens, 421 token-edges) |
| 3. TF-IDF (supporting only) | YES (not used in this run's findings) | (data archived in v3 reference run) |
| 4. Metadata graphs | YES | `data/g_metadata.json` (G_throughline, G_mu, G_pp) |
| 5. Validation P1/P2/P3 | YES | `data/validation_v3.json` (1/3 raw; 2/3 with neighbors_union correction) |
| 6. Multi-graph diagnostics | PARTIAL | A/B/C/D/E/F/H inherited; G re-executed |
| 7. Discourse/design overlay | YES | `data/multigraph_diagnostics_v3.json` `discourse_design_ratio` |

**Mode G — re-executed today.** See §3 below.

---

## §2 Inheritance justification

Per skill output rule "Audit folder is never overwritten across reruns; new run = new dated folder," this run creates a fresh folder. Inheritance of stages 0–5 is permitted because:

1. **Corpus stable.** No mechanical-content commits since 2026-04-29 — the prior directive completed yesterday with propagation-only changes (commits f5da82b9, 94861f5c, 4c0239c7, 646e4049, 4802e83b, plus this directive's same-session continuations). Verified via `corpus_manifest.json` SHA tracking — re-fetched corpus today differs from 2026-04-29 only in trace whitespace and PP-678 vocabulary-debt sweep impacts (which Mode G captures).
2. **Pre-committed thresholds locked.** No threshold tuning between runs.
3. **Validation outcome unchanged.** P1 corrected pass + P3 pass would still hold (citation graph 421 edges; foundation periphery topology unchanged). P2 fail still a finding.
4. **Methodology unchanged.** v3 multi-graph triangulation is canonical per PP-679; no v4 exists.

**Limit on inheritance:** Mode G's vocabulary-debt sweep MUST reflect today's corpus state, since PP-678 was a same-session sweep that intentionally moved struck-term counts. v3's Mode G is preserved in `data/multigraph_diagnostics_v3.json` for diff reference. Today's expanded result is in `data/mode_g_2026-04-30.json`.

---

## §3 Mode G — execution provenance (today)

**Input:** Full body content of all 43 design-corpus docs + 4 discourse-corpus docs from `data/corpus_manifest.json`. Re-fetched today via direct GitHub Contents API (bypassing index routing per methodology §3.1). Total corpus chars: 1,164,988.

**Term list:** 13 patterns parsed from `canon/supersession_register.yaml`, `references/alias_registry.yaml` `legacy_renames` and `collision_table`, and ED-764 / ED-781 / PP-678 / session-log directives. See `00_workplan.md` §3.

**Disambiguation:**
- `TC` standalone uses context filter `(?:Theocracy|Church|Influence|Mass Seizure|seizure|threshold|Holy)` to exclude Conviction-Track-context TC mentions (which are legitimate per alias_registry collision_table).
- `Niflhel` uses context filter `(?:faction|Mandate|Influence|grievance|Operative|Syndicate)` to flag faction-context occurrences only; place-references retained.
- `GM (bare)` mask `Game\s+Master` to avoid double-counting against the `Game Master` bigram pattern.

**Marker handling:** `[STRUCK]` and `[SUPERSEDED]` paragraph markers (case-insensitive) excluded from action count — these are intentional audit trail per `references/diagnostic_modes.md` Mode G recommendation. Per-doc per-term breakdown reported with both columns.

**Paragraph definition:** Methodology §3.1 — strip HTML comments + fenced code blocks, split on blank lines, retain paragraphs ≥ 50 chars.

**Output:** `data/mode_g_2026-04-30.json` (per-term: total_paragraphs, paragraphs_actionable, paragraphs_in_struck_marker, per-doc breakdown).

---

## §4 Cross-referenced terminology layer

Beyond v3's pure structural diagnostics, this run cross-references Modes E and H against the term-governance registries:

| Source | Used for |
|---|---|
| `references/glossary.md` | "Is this isolate/sparse token also a glossary entry?" |
| `references/alias_registry.yaml` | "Is this token registered as canonical or legacy?" |

This is a presentation-layer extension, not a methodology change. The structural finding (e.g. "Wager has cite=1, throughline=0, mu=0, pp=0 — multi-graph isolate") remains the methodology output. Registry coverage is added to the weakness register row to inform action recommendation (promote vs add to glossary vs both).

---

## §5 What did NOT change from v3

- §3.1 Banner classifier rules (STATUS: CANONICAL/DESIGN/PROVISIONAL → design; AUDIT/SESSION/WORKPLAN → discourse; STRUCK/deprecated → excluded)
- §3.4 Class taxonomy (conviction, pressure_point, faction, npc, clock, system)
- §3.5 Disambiguation rules (Faith/Order/Reason/Equity/Precedent/Autonomy/Continuity/Evidence/Consequence/Authority/Loyalty/Crown/Church)
- §3.6 TF-IDF parameters (sklearn standard; supporting only)
- §3.7 All eight pre-committed thresholds
- §3.8 Validation properties (P1, P2, P3)
- §4 Degree computation (in+out neighbor union)

---

## §6 What this run does NOT add

- **No new tokens.** v3's 84-token list is reused. Auto-extract was not re-run; the 22 auto-candidates from v3 (`data/auto_candidates.json`) remain. New tokens would have been:
  - From recent EDs: Approach Training (ED-774), Wrong-Style Penalty (ED-775), Demotion Magnitude (ED-776), Heresy Investigation Lifecycle (ED-772), Knot Lifecycle (ED-773), Tensions Deck (canonical), Royal Assassination Fuse (canonical), Faction Succession Split, Settlement Adjacency, Fractional Province Ownership.
  - These were below the auto-extract threshold in v3 (≥3 docs AND ≥10 paragraph mentions). They would still likely fail today — first-class doc presence does not guarantee corpus-wide cross-reference, which is exactly what Mode H surfaces.
  - **Decision:** Note in Mode H findings that these terms are absent from the v3 token list and may warrant future seeding.

- **No new Modes.** All 8 specified in `references/diagnostic_modes.md`.

- **No t-SNE / force-directed layouts.** v3's layouts are visualization, not analytic — not reproduced for this terminology-focused run.

---

## §7 Methodology version stamp

**v3 (2026-04-29)**, enshrined in `skills/valoria-vector-audit/`. PP-679 introduced this skill as the canonical home; PP-676 was the methodology-validation execution. No v4 exists; if methodology revisions emerge from this run's findings (e.g. P2 fix recipe, isolate-promotion automation), they will be documented as follow-up patches and may produce a v4 spec, but this run executes v3 unchanged.

---

## §8 POST-PUBLICATION CORRIGENDUM (2026-05-01, PP-705)

**Defect identified:** Mode G context-filter regular expressions (in `data/mode_g_2026-04-30.json` generation code) were case-sensitive. Pattern `(?:Theocracy|Church|Influence|Mass Seizure|seizure|threshold|Holy)` would not match "Seizure" (capital S) or "Threshold" (capital T) when those words anchored otherwise-Church-Influence paragraphs. Same defect on Niflhel filter (`faction|Mandate|Influence|grievance|Operative|Syndicate`) — capitalized variants missed.

**Defect class:** B1 in self-audit of this audit (see content audit T/B/V/D/L/H findings, conversation 2026-04-30).

**Numerical impact (re-run with `re.IGNORECASE` post-PP-691 corpus state, 2026-05-01):**

| Term | Audit-time published | Post-PP-691 + B1 fix | Δ |
|---|---:|---:|---|
| TC (as Church Influence) | 21 | 2 | -19 (dominated by PP-691 sweep, not case fix) |
| Niflhel (as faction) | 23 | 22 | -1 (Jordan's parallel ED-775 / PP-698..704 cleanup) |
| Cohesion | 5 | 5 | unchanged |
| Cultural Reformation | 13 | 13 | unchanged |
| Coup Counter | 6 | 7 | +1 (faction_layer_v30 refresh post-Jordan-edit) |
| VTM | 18 | 19 | +1 |
| GM (bare) | 29 | 29 | unchanged |
| Game Master (full phrase) | 0 | 0 | unchanged |
| Combat Power | 0 | 0 | unchanged |
| Thread Depth | 0 | 0 | unchanged |
| Theocracy Counter (full phrase) | 0 | 0 | unchanged |
| Rendering Stability | 1 | 1 | unchanged |
| Vaynard Thread Mastery | 2 | 3 | +1 |

**Conclusion:** The case-sensitivity defect's actual numerical impact was small. Most of the Δ in TC is attributable to PP-691's npc_behavior_v30 + throughlines_meta_infill cleanup (which the audit recommended); not to the case fix. The methodology defect is real and should be fixed in code (Phase 5 of ecosystem workplan v2), but the published audit-time numbers were not materially misleading.

**Audit-time data preserved:** `data/mode_g_2026-04-30.json` is unchanged (frozen-on-creation per audit-folder convention). Post-correction state captured in `data/mode_g_2026-04-30_corrigendum.json`.

**Audit-time §1.1 numbers in `02_weakness_register.md` are not retroactively edited.** They reflect pre-PP-691, pre-B1-fix state and remain the historical record.
