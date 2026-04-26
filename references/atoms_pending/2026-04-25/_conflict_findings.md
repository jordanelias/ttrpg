# Conflict Evaluation — Stage 4 outputs vs canon

**Generated:** 2026-04-25
**Scope:** Stage 4 outputs (ED-543 + 17 PROVISIONAL EDs + 33 PROVISIONAL PPs + 5 Solmund/RWCE design files + throughlines_meta_infill PART 8 append + canonical_sources additions + censured_vocabulary stub) compared against canon (canon/ + designs/world/ + designs/scene/ + designs/threadwork/ + canon/patch_register_active.yaml).

## Severity counts

| severity | count |
|---|---|
| HIGH | 1 |
| MEDIUM | 3 |
| LOW | 3 |

## Findings

## HIGH severity (1)

### HIGH-01 — `PRE-EXISTING-YAML-Bug`

**Summary:** canon/patch_register_active.yaml has malformed YAML in PP-674 entry: a `vetting:` key is indented as a sibling to items in the `affects:` list, breaking yaml.safe_load. This is pre-existing (PP-674 dates 2026-04-19) and was not caused by Stage 4 work.

**Canon evidence:**
> Lines ~405-410:
    - canon/editorial_ledger.yaml
    vetting:        # ← INVALID: sibling to list items
    class: E

**Recommendation:** Fix the indentation of the inner vetting block in PP-674 (should be at 2-space indent under PP-674's mapping, not 4-space under affects). Affects downstream tooling that yaml-parses the active register.


## MEDIUM severity (3)

### MEDIUM-01 — `Solmund-Baralta-Routing`

**Summary:** Solmund world docs (designs/world/solmund_*_v30.md) contain ZERO Baralta references; all 17 Baralta refs went to designs/scene/rwce_mechanism_v30.md (per Stage 4 split routing PART 7 → scene). Setting/character canon for Baralta now lives in a SCENE file, which is a structural anomaly — Baralta is a world-entity, not a scene-mechanic.

**Recommendation:** Extract Baralta-as-entity content from rwce_mechanism_v30.md and route to designs/world/solmund_v30.md or a new designs/world/baralta_v30.md. Keep RWCE as pure mechanism doc.

### MEDIUM-02 — `RWCE-Witness-Conviction-Mechanic`

**Summary:** RWCE introduces a 'Conviction Mechanic for RWCE Witnesses' (§25) — a witness-specific conviction subsystem layered on top of conviction_track_v30. Verify this isn't double-tracking conviction state for the same NPCs across both systems.

**Stage 4 evidence:**
> 25. Conviction Mechanic for RWCE Witnesses" -->



**Recommendation:** Specify how RWCE-witness conviction integrates with the canonical Conviction Track (extension, parallel system, or override?).

### MEDIUM-03 — `Throughlines-Append-No-Table-Rows`

**Summary:** PART 8 append to throughlines_meta_infill.md does NOT add table rows in the canonical format. The append is prose content following the original table; downstream tools that parse throughlines_meta as a table won't see new throughlines.

**Stage 4 evidence:**
> # Solmund Throughlines (Stage 4 Promotion 2026-04-25)

[PROVISIONAL] Source: atoms_pending/2026-04-25/_consolidated/02_solmund_cultural_guide.md PART 8 (atoms 30, 31). Pending Jordan review before integration into canonical throughlines table.

<!-- atom: solmund_master_document__30__27-five-through

**Recommendation:** Either convert PART 8 content to canonical table-row format (| T-NN | name | parent | secondary | description |), or split the append into a separate appendix file.


## LOW severity (3)

### LOW-01 — `Solmund-Niflhel-Drift`

**Summary:** Solmund file mentions Niflhel without acknowledging dissolution. Setting drift.

**Stage 4 evidence:**
> certainty | section_index: 21 | source_section: "18. tonal calibration by certainty" -->

## 18. tonal calibration by certainty

| certainty | dominant register | voice |
|---|---|---|
| 1-2 | böhme, niflhel plain speech | rejection or indifference to theological framing |
| 3 | thomas, early levertov | faith as habit without conviction |
| 4 | di cicco inhabitation, folk/vernacular | faith as cul

### LOW-02 — `CanonicalSources-Status-Field-New`

**Summary:** Added `status: provisional` to 5 new system entries; canonical_sources.yaml didn't previously use a status field. Downstream tools may not handle this.

**Recommendation:** Confirm whether downstream readers (freshness_gate, broken_dependency_checker) tolerate or filter on status field, or remove field if not yet schema-supported.

### LOW-03 — `Censured-Vocabulary-Stub-Empty`

**Summary:** censured_vocabulary.yaml is now a stub but referenced by 1 canon files: ['run_eval.py'].

**Recommendation:** Populate or update references to acknowledge stub.


## Manual review of findings (post-generation)

Re-inspected each finding before commit:

| finding | verdict |
|---|---|
| HIGH-01 PRE-EXISTING-YAML-Bug | **REAL** — PP-674 has malformed indentation (`vetting:` at sibling level to `affects` list items); breaks `yaml.safe_load`. Pre-existing issue surfaced by Stage 4 eval. |
| MEDIUM-01 Solmund-Baralta-Routing | **REAL** — PART 7 of consolidated Solmund was titled "Baralta's Theological Position" and routed to designs/scene/rwce_mechanism_v30.md per the mechanical-content rule. Result: 17 Baralta refs in scene file, 0 in world files. Structural anomaly. |
| MEDIUM-02 RWCE-Witness-Conviction-Mechanic | **REAL** — RWCE §25 introduces witness-specific conviction subsystem; integration with conviction_track_v30 is underspecified. |
| MEDIUM-03 Throughlines-Append-No-Table-Rows | **REAL** — PART 8 append is prose under the existing table; downstream tooling parsing throughlines_meta as table format won't pick up new throughlines. |
| LOW-01 Solmund-Niflhel-Drift | **FALSE POSITIVE** — the Niflhel reference is in a tonal-calibration table ("Böhme, Niflhel plain speech" as low-certainty voice register), naming a stylistic register, not asserting Niflhel currently exists as a faction. |
| LOW-02 CanonicalSources-Status-Field-New | **REAL but minor** — `status: provisional` field added to 5 new entries; schema didn't formalize a status field. Verify downstream readers tolerate it. |
| LOW-03 Censured-Vocabulary-Stub-Empty | **FALSE POSITIVE on the count** — the "1 canon file" reference was actually `/home/claude/conflict_eval/run_eval.py` (my eval script), not a canon file. The censured_vocabulary stub is referenced ONLY by atoms (expected — PP-675/ED-783 atoms reference it). The stub being empty is real but not a canon-blocker. |

**Net real findings:** 1 HIGH, 3 MEDIUM, 1 LOW (the 1 minor LOW + 1 false-positive LOW are below action threshold individually).


## Per-surface summary

| surface | severity | finding |
|---|---|---|
| PRE-EXISTING-YAML-Bug | HIGH | canon/patch_register_active.yaml has malformed YAML in PP-674 entry: a `vetting: |
| Solmund-Niflhel-Drift | LOW | Solmund file mentions Niflhel without acknowledging dissolution. Setting drift. |
| Solmund-Baralta-Routing | MEDIUM | Solmund world docs (designs/world/solmund_*_v30.md) contain ZERO Baralta referen |
| RWCE-Witness-Conviction-Mechanic | MEDIUM | RWCE introduces a 'Conviction Mechanic for RWCE Witnesses' (§25) — a witness-spe |
| Throughlines-Append-No-Table-Rows | MEDIUM | PART 8 append to throughlines_meta_infill.md does NOT add table rows in the cano |
| CanonicalSources-Status-Field-New | LOW | Added `status: provisional` to 5 new system entries; canonical_sources.yaml didn |
| Censured-Vocabulary-Stub-Empty | LOW | censured_vocabulary.yaml is now a stub but referenced by 1 canon files: ['run_ev |