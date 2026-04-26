---
atom_id: valoria_session_2026_04_25_master_consolidation__04__4-proposed-architecture-for-term-governance-deferr
source_file: valoria_session_2026_04_25_master_consolidation.md
source_section: "4. Proposed Architecture for Term Governance (deferred — see §10)"
section_index: 4
total_sections: 15
line_count: 21
char_count: 1685
source_sha256: 4c4672049317ec8e
session_date: 2026-04-25
ingested: 2026-04-25
status: pending-prioritization
origin: session-master-upload
---

## 4. Proposed Architecture for Term Governance (deferred — see §10)

Eight-layer enforcement model, ordered by leverage and feedback speed:

| Tier | Layer | Action | Purpose |
|---|---|---|---|
| 1 | **A — Pre-bootstrap** | Project-instructions censure block | Precedes all reads; one-time edit; highest leverage |
| 2 | **B — Bootstrap** | `references/censured_vocabulary.yaml` + bootstrap loader + status block reinforcement | Re-asserts ban every session |
| 3 | **D — Read-time** | Wrap `github_ops.read_files_graphql` to inject `[CENSURED VOCABULARY DETECTED]` warning header on contaminated reads | Breaks the regen cycle: Claude reads file, sees warning, knows not to mirror terms |
| 4 | **Source** | Canon-tier rewrite | **DONE** (this work) |
| 5 | **E — Commit** | New `censure_gate()` in `safe_commit` | Hard reject of additions containing censured terms outside permitted contexts |
| 6 | **F — Post-push CI** | GitHub Actions check on push | Catches manual web-UI edits and any path bypassing hooks |
| 7 | **C — Skill-load** | Editorial scrub of contaminated skill files | Closes secondary propagation channel |
| 8 | **Meta** | `valoria_collator.py` extension: new drift type `CENSURED_VOCABULARY` + recurring sweep | Long-term audit |

**Two-channel surfacing** for what to censure:
1. **Automated discovery** — term-frequency scan across all design docs cross-referenced against `alias_registry.yaml` + `proper_noun_registry.yaml`. Anything appearing 5+ times but unregistered is a candidate for review.
2. **Manual seed** — Jordan provides terms; Claude greps to find footprint and classifies (banned vocab vs. struck concept vs. needs-replacement-decision).

---
