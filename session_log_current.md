session_id: 2026-04-26-disambiguation-sweep
session_close: 2026-04-26
phase: editorial
status: complete
last_stage: >
  Full abbreviation disambiguation sweep. 9 commits:
    db0dcd0 — TC→CI + RS→MS top 5 files (185 TC, 61 RS)
    1a48d60 — TC→CI residuals in top 5 (83 TC, 21 RS)
    028a748 — TC→CI + RS→MS 60 design/params files (~422 TC, ~181 RS)
    44fbb1e — TC→CI + RS→MS 3 user-authority files (ED-783/784/785)
    dadf8e1 — TC→CI in 46 tests/canon files (853 TC)
    e024512 — Alias registry TC→CI update + numeric bounds review (ED-786)
    7989b11 — Maret Vossen → Yrsa Vossen propagation (14 files, PP-665)
    8563b46 — Maret Vossen → Yrsa Vossen NPC authority file (ED-787)
  Summary: ~1,543 TC→CI, ~263 RS→MS, ~100 Theocracy Counter→Church Influence (full term),
  23 Maret Vossen→Yrsa Vossen. Alias registry updated (theocracy_counter→church_influence,
  collision table TC entry marked resolved). Numeric bounds report reviewed: all 14 flagged
  stats = legitimate multiple thresholds or false positives, no drift.
  CP disambiguation confirmed complete (CP=Character Points per ED-136, no active Combat Power refs).
next_action:
  skill: editorial
  description: >
    Remaining items from consolidation queue:
    (1) RS in tests — ~1,340 instances. Cannot blind-replace: "RS" collides with Rhetorical Style
        (Evidence RS, Authority RS, Solidarity RS, Consequence RS in NPC debate contexts).
        Needs per-context classifier distinguishing RS=Mending Stability from RS=Rhetorical Style.
        Python files blocked by fabrication check; variable names (gs.rs, avg_rs) should not be renamed.
    (2) TD disambiguation — mostly Mermaid flowchart TD (valid). Small count of Thread Depth (removed
        PP-166) references may exist. Low priority.
    (3) ED-768 (P3) — PROVISIONAL marker audit. 13 orphaned markers referencing pre-ledger EDs.
        Requires Jordan review to determine which are still-open vs resolved-but-unarchived.
    (4) ED-543 (P1) — Clock registry refresh verification. Single-atom evidence; needs verification
        whether the registry refresh actually landed under another ED.
    (5) D-4 (Altonian invasion ~18 AG) — timeline revision per ED-725. Requires Jordan worldbuilding authority.
    (6) D-5 (Einhir site-network model) — new spec per ED-726. Requires Jordan worldbuilding authority.
    (7) doc_index_gen.py regen — index files stale after bulk renames. Mechanical but large scope.
    (8) Python sim file Maret rename (campaign_sim_npc_pcs_2026-04-18.py) — blocked by fabrication check.
    (9) TC in deprecated/ files — low priority, old docs.
  priority: "ED-543 (P1) verification is highest severity. RS test disambiguation is highest volume."
blockers: []
notes:
  - "Glossary notes in affected files updated to reflect CI = Church Influence (was TC = Theocracy Counter)"
  - "Alias registry collision_table TC entry marked resolved with 2026-04-26 sweep date"
  - "RS = Rhetorical Style is NOT in the alias_registry — needs entry added if it's a canonical term"
  - "Numeric bounds report reviewed inline (review header added). Regenerate after next collator run."
  - "Maret disambiguation was already decision-resolved (PP-665) but propagation was incomplete — now fixed in 15 active files"

# RS sweep test
