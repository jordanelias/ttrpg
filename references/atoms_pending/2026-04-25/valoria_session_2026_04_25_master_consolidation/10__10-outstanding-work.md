---
atom_id: valoria_session_2026_04_25_master_consolidation__10__10-outstanding-work
source_file: valoria_session_2026_04_25_master_consolidation.md
source_section: "10. Outstanding Work"
section_index: 10
total_sections: 15
line_count: 83
char_count: 4844
source_sha256: 4c4672049317ec8e
session_date: 2026-04-25
ingested: 2026-04-25
status: pending-prioritization
origin: session-master-upload
---

## 10. Outstanding Work

### 10.1 Term-governance enforcement infrastructure (NEXT)

Implementation of Layers A/B/D/E from §4 architecture. Now that canon is clean, the gates can prevent reintroduction:

1. **Layer A — Project-instructions censure block.** Edit project instructions to include a censured-vocabulary section.
2. **Layer B — `references/censured_vocabulary.yaml`.** Create registry file. Extend bootstrap to fetch it. Add status-block line: "Censured terms: [N loaded]."
3. **Layer D — Read-time injection.** Wrap `github_ops.read_files_graphql` to scan fetched content for censured terms and prepend warning header to contaminated files.
4. **Layer E — `safe_commit` censure gate.** New gate function `censure_gate()` runs after `commit_message_gate`. Blocks any addition containing a censured term outside permitted contexts (revision-note markers, deprecated/ path).

### 10.2 Sub-system terminology boundary directive

Per Jordan: terms relating specifically to mass battle / personal combat / social contest / faction actions / fieldwork must be sharply defined and have **no possibility of confusion** with other systems — most critically, **no terminology overlap with metaphysics / ontology / threadwork / beliefs / personalities / inspirations / duties**.

This is a governance principle requiring:
- Audit of current sub-system vocabulary for any cross-domain collisions.
- Encoding the boundary in `censured_vocabulary.yaml` as a separate `cross_domain_collisions` block or in `alias_registry.yaml` per-term.
- A separate drift type in the collator: `CROSS_DOMAIN_COLLISION`.

### 10.3 Design-tier sweep

Per pre-rectification scan:
- "taint" raw hits: 288 (many false positives from "Certainty" substring; need word-boundary scan)
- "corruption" raw hits: 64
- "epistemic seduction" raw hits: 40

Many in `deprecated/` (legitimate). Real contamination in active design docs:
- `designs/threadwork/threadwork_v30.md` and infill
- `designs/npcs/npc_behavior_v30.md` and infill
- `designs/ui/valoria_ui_ux_v4_1.md` and v4_2_workplan and max_audit
- `designs/arcs/arc_expansion_v30.md`
- `designs/provincial/faction_politics_v30_index.md`
- `designs/architecture/player_agency_v30.md`
- `designs/audit/throughlines_transitions_hierarchy.md`
- `designs/audit/valoria_systems_workplan.md` and valoria_workplan_final.md
- `designs/scene/fieldwork_godot.md`
- `designs/world/worldbuilding_canon_audit_v30_infill.md`
- `references/throughlines_complete.md`
- `references/throughlines_meta_infill.md`
- `references/propagation_log.md`
- `params/board_game.md`
- `params/bg/ministry.md`

Plus skill files:
- `skills/valoria-canon-guard/SKILL.md`
- `skills/valoria-mechanic-audit/SKILL.md`
- `skills/valoria-simulator/SKILL.md`

This is multi-session editorial work. The censure gate (Layer E) will prevent further drift from this point; the sweep is cleanup of pre-existing state.

### 10.4 Conviction Track rename

Jordan flagged: "Conviction Track" implies "how influenced someone is by your arguments" but that's misleading. Replacement name needed.

**Status:** GAP — requires either (a) Claude reads `designs/scene/conviction_track_v30.md` and proposes 2–3 candidate names, or (b) Jordan specifies what CT actually tracks semantically and Claude proposes against that.

### 10.5 Certainty → Religious Conviction rename

Jordan directed: rename Certainty to Religious Conviction. The current "Certainty" doc's range is "Solmund orthodoxy (5) → Thread acceptance (0)" — i.e., it tracks belief-in-Solmund-theology, not spiritual strength. Renaming to "Religious Conviction" disambiguates from Spirit (which is the spiritual-strength stat).

**Status:** Decision pending on:
- Abbreviation: "RC"? Conflicts with anything?
- Order of operations: rename Conviction Track first (to avoid collision), then rename Certainty?

Scope of rename:
- `references/alias_registry.yaml` (canonical entry)
- `params/core.md` (Certainty Track section, ~30 lines)
- All design docs that mention Certainty (significant footprint — collator will surface as `LEGACY_TERM_USED` post-rename)
- All session logs / editorial-ledger entries
- `canon/02_canon_constraints.md` P-01 ("Certainty modifiers")

The collator's existing `legacy:` field per alias entry is exactly the case the registry was designed for. Once renamed, the collator flags every legacy use for cleanup.

### 10.6 Editorial ledger regeneration

ED-783 is now active (cited in editorial marker in `canon/00_philosophical_foundations.md`). The editorial ledger summary (`canon/editorial_ledger_summary.yaml`) is auto-generated and currently shows `next_id: 739` (stale — actual max in ledger is 782, now 783 with this work). A regeneration is needed to:
- Update `next_id` to 784
- Add ED-783 to `recent_resolutions`
- Reflect the canon/00 + canon/01 + canon/02 + rules updates

---
