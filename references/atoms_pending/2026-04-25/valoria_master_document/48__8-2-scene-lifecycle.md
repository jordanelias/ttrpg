---
atom_id: valoria_master_document__48__8-2-scene-lifecycle
source_file: valoria_master_document.md
source_section: "8.2 Scene Lifecycle"
section_index: 48
total_sections: 125
line_count: 10
char_count: 537
source_sha256: 8f501f471217ba59
session_date: 2026-04-25
ingested: 2026-04-25
status: pending-prioritization
origin: session-master-upload
---

## 8.2 Scene Lifecycle

1. **Entry** — triggered by player action, NPC, world event, or Scene Slate
2. **Resolution** — one of the mechanics above
3. **Consequences** — stat changes, track advances, Exposure, Disposition
4. **Domain Echo check** — Sufficient Scope? If yes → faction stat change
5. **Transition** — to next scene, Accounting, or scale shift

⚠ **GAP-01: Scene Lifecycle not formally codified.** These five steps are implicit across documents but never stated as a unified model. For Godot: create a SceneLifecycle class.
