session_id: 2026-04-23-consolidation-system
session_close: 2026-04-23
phase: infrastructure
status: complete
last_stage: >
  Naming/value/glossary consolidation system built in 4 parts (all committed).
  Part 1 (proper_noun_registry.yaml) at 4146bac + round-2 finalization at 0f0f38f:
    62 entries across 10 categories, 42 aliases, 0 open candidates.
    All 466 round-1 candidates auto-triaged via deterministic rules.
  Part 2 (alias_registry.yaml) at 3addd2b: 96 entries across 15 categories
    covering core/derived/thread stats, world clocks, debate, faction stats, combat,
    dice engine, narrative, thread ops, infra, modes, 4 collisions, 4 unresolved gaps,
    4 legacy renames.
  Part 3 (values_master.yaml + tools/extract_values.py) at ad6a8fd: 464 values
    extracted from 12 of 14 params files; 5 real conflicts surfaced (threadwork/superseded drift).
  Part 4 (tools/valoria_collator.py + references/collation_report_summary.yaml) at 8516cf6:
    scans all design/params/canon .md against the 3 registries.
    First run: 9101 findings after context-aware exemptions.
      COLLISION_USED_ALONE: 1092 (TC 943×, TD 80×, CP 69×)
      LEGACY_TERM_USED: 903 (RS 531×, Rendering Stability 158×, Cohesion 73×, CP 63×, TD 74×)
      UNKNOWN_ABBREVIATION: 3640 (long tail of per-doc terms)
      UNKNOWN_PROPER_NOUN: 3466 (mostly compound mechanical phrases)
next_action:
  skill: infrastructure
  description: >
    Concrete follow-ups surfaced by the collator:
    (1) Bulk-fix tool to consume collation_report_summary and do context-aware
        substitutions: TC → Theocracy Counter or Conviction Track (requires per-context
        disambiguation), RS → Mending Stability, Cohesion → Discipline,
        Combat Power → Power, CP in game-stat contexts → Character Point.
    (2) Extend values_master to scan designs/*.md too (not just params/), since the
        CI ceiling 75 vs 100 conflict likely lives in designs/, not params/.
    (3) Glossary additions for deferred terms from round 1: Arc, Zoom In, Cardinal.
    (4) Populate alias_registry unresolved gaps: CERT, TLK, DD, FSTAT — confirm full names.
    (5) Maret disambiguation pass — flagged for per-file context (two Marets: Uln vs Vossen).
  priority: "(1) bulk-fix tool is highest impact — addresses the 1092 collision + 903 legacy findings"
blockers: []
notes:
  - "Collation report per-instance detail (985KB) not committed — regenerate via tools/valoria_collator.py"
  - "Proper noun registry at 62 entries is saturated for this round; additional promotions will come from new design work"
  - "Five carried-over follow-ups from 2026-04-22 editorial session still pending: D-4, D-5, ED-735 (RWCE/Miracle Investigation/SA-gating), PROVISIONAL marker audit, doc_index_gen.py regeneration"
