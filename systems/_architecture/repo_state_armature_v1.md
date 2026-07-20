<!-- Architecture spec. Substrate tier (RULED underscore-prefix, not editorial-governed content). -->
# Repository State Armature — v1

## Status: PROPOSED (ED-IN-0077, 2026-07-20)
## Class: A — substrate/infrastructure architecture. Merge of the Phase-1 PR ratifies Phases 0–2 (ED-1094 merge-ratifies-by-default); Phases 3–5 carry their own loudly-held-back EDs.
## Provenance: designed by a producer→critic→informed-design relay — an initial plan (Opus adversarial review, verdict NEEDS-REDESIGN) then a Fable-5 max-effort redesign built around the critique. Seeded by this session's world-state primitive survey (`audit/other/2026-07-19-module-io-state-survey.md`).

---

## 1. Why

The corpus carries **~40 review/survey/mapping apparatuses across 6 layers** (vocabulary/glossary,
canonical-currency + mechanics, propagation/chain maps, ledgers/verdicts, coverage/observability,
and this session's primitive/module state survey) — heavily overlapping, several stale/dead, with
**no index of them and no single judgment of repository state**. Definitions are fragmented across
`names_index.yaml` / `descriptor_registry.yaml` / `glossary.md` / ~7 collision-alias-deprecation
registers; numeric ground-truth is un-centralized; freshness enforcement is leaky
(`freshness_gate.py` advisory pins, ~12 stale). This is the same opacity the primitive survey
fought, one level up.

Goal (Jordan, this session — *collate, appraise, reconcile, consolidate; unify and simplify*,
extended to CI/import/gates and GitHub actions, with **currency/freshness** as a first-class
pillar): **one armature** that (1) works across all Claude + GitHub surfaces, (2) exhaustively
reviews repository state, (3) centralizes all definitions/terms/formulae/attributes as one source
of truth existing stores become views of, (4) enforces legibility so unification holds, and (5)
guarantees freshness.

## 2. The armature — three artifacts, everything else is a projection or a collector

### 2.1 `references/definitions/` — the single source of truth (Phase 2)
A directory of typed YAML (`attributes / stats / derived / formulae / terms / names / _meta`) with
one loader `tools/definitions_store.py`. A term, an attribute, a formula, a constant, and a
world-state primitive are the **same record** with different fields populated (`id, kind, name,
aliases, legacy, enforce, lane, scale, owner, writers, readers, formula, status, provenance{source,
source_sha, citation}`). Seeded from `descriptor_registry.yaml` + `names_index.yaml` **plus the
per-primitive writers/readers/formula/citation columns of the 2026-07-19 survey**.

**The inversion that keeps every CI reader green:** `tools/gen_definition_views.py` regenerates
`names_index.yaml` and `descriptor_registry.yaml` **at their existing paths** as `# GENERATED`
views. `ci_naming_check.py` / `ci_names_consistency.py` never change their input path — no blocking
reader is ever rewired. `quantity_registry.py` (already "the single reader merging descriptor +
names_index") becomes a thin shim over `definitions_store.py`, public API frozen. A **blocking
round-trip gate** `ci_definitions_roundtrip.py` (cloned from the engine-params round-trip
precedent) byte-diffs regenerated views vs committed, so a hand-edit to a projection fails CI.

### 2.2 `tools/review_core.py` → `review_state.json` — the one review engine (Phase 1, BUILT)
Implements **zero rules** (CLAUDE.md §8: every rule lives once) — a **verdict aggregator** that
runs each existing check tool and normalizes the result to a `Signal` (`id, source, tier, lane,
verdict, baseline, regressed, detail`), then rolls up a **per-lane + overall repository grade**
(GREEN/AMBER/RED). Collectors are a single `CHECKS` registry (adding a signal = one row); Phase-1
subset: currency, A17 vocabulary closure, wiring coverage, audit staleness, workplan. Later
collectors fold in freshness, A18, contract conformance, apparatus-diff, registry coverage,
definitions round-trip, and (online) the GitHub CI mirror. **One core, three faces:** the
SessionStart banner (`session_status.py`, guarded, reads committed state), a GitHub `review-state`
job, and the published artifact (`window.VALORIA_REVIEW`) all read from here.

### 2.3 `registers/review_baseline.yaml` — the ratchet (Phase 1, BUILT)
One row per report-only signal = its accepted-debt ceiling. `review_core --check` fails only on a
**regression vs baseline** (a signal exceeding its ceiling) or a blocking failure — so report-only
signals are **blocking-on-regression from day one** with no branch-protection edits and no CI job
renames. Debt can only shrink; each shrink is a one-line baseline edit in the PR that earns it;
when a row hits `target: 0` it is fully blocking. This is the safe report-only→blocking burndown
(incl. A17 36/71 and the ~12 stale freshness pins). CODEOWNERS-gated to Jordan.

## 3. Currency / freshness (Phase 4)
`freshness_gate.py` + `currency_consistency_check.py` are superseded **by absorption**: freshness
pins move into store entries (`provenance.source_sha`, git blob OIDs via the lifted
LF-normalized `_blob_sha_bytes`); a store entry whose source's working-tree OID ≠ its pin is a
`stale` verdict on that lane; `review_core --update-pins` re-syncs. `canonical_sha__*` pins (already
"advisory, not trustworthy") retire with `freshness_gate.py` once every pinned source has a store
pin.

## 4. Cross-surface wiring
- **Claude:** `session_status.py` SessionStart stanza (BUILT); `CLAUDE.md` routing row *"state of
  repo? → `python tools/review_core.py --summary`"* + `references/definitions/` as the vocabulary
  authority (Phase 2); skill situational-awareness pointers to `review_core --json`; the artifact
  becomes the armature's face (`VALORIA_REVIEW` + `VALORIA_LEXICON`). No `.claude/agents/` roster
  (roster discipline — the engine is a tool, not a recurred role).
- **GitHub:** a new `review-state` CI job (`continue-on-error` until Phase 4 graduation, then added
  to `ci-summary.needs`); `ci_checks_registry.yaml` rows co-committed (keeps
  `broken_dependency_checker.check_ci_registry_coverage()` green); `.github/PULL_REQUEST_TEMPLATE.md`
  mechanizing ED-1094 (lane declaration + ratify-on-merge + held-back call-out); `.github/CODEOWNERS`
  gating the authority files (`references/definitions/`, `review_baseline.yaml`, `.github/workflows/`)
  to Jordan; the 3 generator workflows fold into one `refresh.yml` (low-risk). **CI job regrouping
  is explicitly REJECTED** (load-bearing: parallelism, the `ci-summary` ran-not-skipped assertion,
  and `dashboard_data.py`'s pinned job names) — the single-judgment property comes from
  `review_state.json`, so cosmetic check-run consolidation is pure risk.

## 5. Phased sequence (branch-protected `main` stays green throughout)
- **P0 — charter (this PR):** allocate ED-IN-0077; this spec; `review_baseline.yaml`; PR template;
  CODEOWNERS. *Must not break:* nothing executable. Records intent before any fold (ED-1094).
- **P1 — minimal core (this PR):** `review_core.py` (subprocess collectors over already-CLI tools);
  guarded `session_status.py` stanza; CLAUDE.md/CURRENT.md pointers. *Must not break:* SessionStart
  never crashes (every import guarded, `--fast` reads committed state only); no existing CI job
  touched. Independently shippable; satisfies mandate items 2 + 4's skeleton.
- **P2 — store bootstrap + view inversion:** `definitions/`, `definitions_store.py`,
  `gen_definition_views.py`, `quantity_registry.py`→shim, blocking round-trip gate. **A permanent
  parity test** in `tests/valoria/` asserts `quantity_registry.load()` + `names.all_legacy(block)`
  are set-identical pre/post inversion. Attributes imported `status: in_flux` — **no roster choice
  made** (see §6).
- **P3 — vocab fold:** alias/deprecated/censured/synonym/collision registers → store projections;
  `build_lexicon.py` re-sourced; glossary tables projected. Record the ED-IN-0029 frozen-keep
  overturn as a loud held-back superseding ED (ED-1094) before executing.
- **P4 — freshness absorption + graduation:** §3; retire `freshness_gate.py`; add `review-state` to
  `ci-summary.needs`, drop its `continue-on-error`.
- **P5 — attribute centralization: HARD-GATED on a Jordan ruling of OPT-AV-1** (the 7/9/10-with-Recall
  roster, explicitly left OPEN in ED-IN-0029). Collapse the 3 Combat-Pool definitions to one
  `kind: formula`; burn A17 toward 0.
- **P6 — deliberately not done:** CI job regrouping (rejected, §4); folding `wiring_manifest.yaml` /
  `proper_noun_registry.yaml`; any agent roster.

## 6. Consolidation map (summary; full appraisal → the register)
VIEW (generated): `descriptor_registry.yaml`, `names_index.yaml`, then (P3) `alias_registry`,
`deprecated_terms_registry`, `censured_vocabulary`, `synonym_registry`, `name_collision_database`,
`glossary.md`. SHIM: `quantity_registry.py`. COLLECT (kept, verdicts aggregated): `audit_staleness`,
`workplan_status`, `wiring_map_check`, A17, A18, contract-conformance, mechanics-index,
canonical-index-coverage, `currency_consistency_check`. SUPERSEDED/RETIRE: `freshness_gate.py` +
`canonical_sha__` pins (P4); `values_master.yaml`, `numeric_bounds_report.yaml`,
`collation_report_summary.yaml`, `mechanical_terms_index.md`, `orphan_terms_registry.yaml`,
`propagation_log.md`, `file_index_summary.md`, the 4 orphan tools (once zero live readers confirmed).
UNTOUCHED (the blocking spine): `ci_naming_check.py`, `ci_names_consistency.py`, `names.py`,
engine-params round-trip, sim-fabrication, ED-citations, pytest, `ci-summary`. KEEP standalone:
`proper_noun_registry.yaml`, `wiring_manifest.yaml`, `d10_success_probabilities.json`.

## 7. Top risk + mitigation
The P2 inversion regenerates the two files the blocking naming spine reads; a silently-dropped
alias/legacy name turns `ci_naming_check` quietly wrong — drift created by the anti-drift armature.
Mitigation is structural: (a) a permanent parity test asserting set-identical
`quantity_registry.load()` / `names.all_legacy(block)` from store vs pre-inversion files;
(b) the seed importer migrates every hand-written registry comment into structured
`provenance.citation`/`note` and **fails loudly on any comment it cannot attribute** (comments
become data, not casualties); (c) `ci_naming_check`'s existing empty-`FORBIDDEN`⇒exit-1 fail-safe
plus the daily round-trip gate. The inversion is provably lossless before merge and drift-proof
after.
