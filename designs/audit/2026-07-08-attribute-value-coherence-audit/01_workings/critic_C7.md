# Critic pass — C7 (Cross-index consistency, enforcement tiers & check backlogs)

Antagonist relay over `dossier_C7.md` (independent read-only verification).

## Verdicts

| target | verdict | reason (condensed, evidence-cited) |
|---|---|---|
| C7-F1 | **soften** (calibration NEW→KNOWN-TRACKED; P1 stands) | Facts confirmed (name_collision_database.yaml:461,466-467; glossary.md:86,94; module_contracts.yaml:254) but calibration NEW is the dossier's worst conformance failure: the exact CT/CV/PT collision is tracked by **ED-644** (open, "CV≡PT... full rename deferred pending cost-benefit review"), **ED-1006**, **ED-1009**, **ED-919** — and module_contracts.yaml itself carries an in-file "[OPEN — Jordan]" gap_note two lines from the cited evidence (:272; full write-up :238-239). The dossier read past it. P1 stands on its merits (undecided canonical abbreviation an engine could ingest). |
| C7-F2 | **sharpen** | Confirmed absent from registry (grep 0; not_descriptors.tracks:108 = [Piety, Disposition, Renown, Standing, Persuasion]). Worse than "unregistered": **ED-830** (ledger:86, resolved 2026-05-15) ruled "Coherence reclassified from Derived Value to Track" — the registry never received it and module_contracts.yaml:288 tags the same entry `bucket: pool` [ASSUMPTION], contradicting the ruling. A 3-way bucket disagreement (ledger: Track / registry: absent / contracts: pool) hung off a resolved decision that never propagated. NEW defensible (ED-830 didn't audit the registry), but ED-830 must be cited as the traceable origin. |
| C7-F6 | **uphold** | keys.py validate_payload (:239-251) checks required-field presence via '#'-splitting only; never validates stat_deltas/impact_vector key names; Target (:83-84) stores stat_deltas as a bare dict. KT (census F-SIM-02/03) accepted. |
| C7-F3 | **soften** (wording; conclusion intact) | tools/names.py:91-108 all_legacy() reads only `legacy:`; the 22 attr/agg/fac/set entries (:41-72) all have legacy:[]. But "populate only aliases:" overstates — most fac/set/agg entries have aliases:[] too (empty BOTH fields); only attr.* entries carry alternates. Zero-matcher conclusion unaffected. |
| C7-F4 | **uphold** | ci_names_consistency.py:1-16 implements exactly two mirror pairs and explicitly skips mechanic/clock/track/substrate entries (:14). No tool cross-checks glossary or the secondary indices against anything. |
| C7-F5 | **uphold** | valoria_collator.py:35-36 (sys.path '/home/claude'; github_ops import), :75 hardcoded PAT path; its docstring (:5-8) names values_master.yaml as a cross-reference source — resurrection would re-couple to quarantined data. numeric_bounds_report.yaml:1-20 and mechanical_terms_index.md headers confirm hand-authored provenance. Correctly KT (ED-1084 quarantine; CLAUDE.md §8 dead-tool list). |
| C7-F8 | **soften** (P2→P3; kind collision→stale; NEW→KNOWN-TRACKED) | Cited pair real, but not an undecided fork: params/factions_personal.md:8 flags the linear form as retained backward-compat, and **ED-784** (ledger:46, closed, Jordan 2026-05-02) blessed the "personal_mandate_view = round((L+PS)/2)" as an intentional simplified view beside the canonical aggregate; ED-830 ratifies the taxonomy context. The generalizable point (8/8 registration ≠ single-sourcing) is sound and kept; the instance files as KT/stale/P3. |
| C7-F7 | **uphold** | Spot-check as reported: silo_overlap_matrix.yaml:5 total 55 self-consistent; numeric_bounds_report.yaml:6-19 lists exactly the claimed 14. Correctly low severity. |
| C7-U1 | **soften → reframed** | "Ratify PT as canonical" decides a fork the ledger holds open (ED-644: deferred pending cost-benefit; ED-1006/1009: "Pending Jordan") — rule-(e) violation as written. Reframed options-only in OPT-AV-13; the registry-key addition survives regardless of the name winner. |
| C7-U2 | **uphold** (cite ED-830) | Correct default; should cite ED-830 as its ratified basis (applied in extension §2 D7). |
| C7-U3 | **uphold** | Report-only alias channel; no policy change; makes ED-IN-0008-class conflicts machine-visible. |
| C7-U4 | **uphold** | Historical-snapshot default matches the values_master precedent; re-platform only on demand. |
| C7-U5 | **uphold** | A17 first (deterministic), A18 second (citation judgment); report-only lifecycle per armature §4. |

## Missed findings

**C7-M1 · P2 · orphan · NEW** — The dossier self-scoped to 8 surfaces, but `references/` holds at
least seven MORE naming/vocabulary registries with zero live tool consumers — a stronger defect
than the sampled surfaces' warn-tier gaps: censured_vocabulary.yaml (204 lines),
collision_registry.yaml (59), orphan_terms_registry.yaml (94), proper_noun_triage_decisions.yaml
(121), proper_noun_triage_round2.yaml (1923) referenced by NO tool in tools/*.py (grep 0 hits);
alias_registry.yaml (646) and proper_noun_candidates.yaml each referenced by exactly one tool,
and that tool is dead (valoria_collator.py; extract_proper_nouns.py — CLAUDE.md §8). Entirely
unconsumed data files, directly on-topic for this cluster.

## Conformance note

One serious rule-(c) violation: C7-F1 filed as NEW while ED-644/ED-1006/ED-1009/ED-919 all track
the exact collision, with an [OPEN — Jordan] gap_note in the very cited block. C7-F8 has the same
problem at lower stakes (ED-784/ED-830 reconcile the split as a deliberate dual view). Otherwise
no invented criteria — findings bind the registry KIND discipline and enforcement-tier taxonomy —
and no build-state-as-verdict anywhere. One rule-(e) violation in the options: C7-U1 recommends
ratifying a name the ledger explicitly defers (reframed). No lane-scoping violations (all IN-lane
index/tooling matter). The headline A17/A18 percentages (~34/88, ~25-27/88) are cluster-prose
seeds without per-item citations — a rule-(a) gap for the headline stats specifically; carried
into the extension §3 as "seed, re-derive mechanically before any flip."
