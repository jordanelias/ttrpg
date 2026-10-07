# lane_assignments — history and discussion

Companion to `references/lane_assignments.yaml`. **That file is the lane spec; this one is its history.**

## Why this file exists (B-X extraction, 2026-10-06)

Jordan, 2026-10-06: *"you can extract all edit histories/discussion from .yaml files in references and
just make those a supplement"*. `lane_assignments.yaml` is the write-disjoint **Lane A/B/C** operating
model (workplan v2 item 5.11) — an OLDER concept than the nine `ED-<LANE>-NNNN` lanes, whose roster is
owned by `tools/ci_common.py`. Nothing in `tests/`, `tools/`, `engine/`, `skills/`, `.claude/` or
`.github/` reads this file except `tests/valoria/test_references_yaml_parse.py`, which only parses it, so
comment moves are invisible to code.

**What stayed in the YAML:** every data key and value (the lane roster, `owns` globs, reserved ranges,
`shared_files`, `coordination`, `launch_prerequisites`), a one-line summary of the retired-machinery
note, the naming-collision warning and the ID-allocation note, and a pointer here. **What moved:** the
header's provenance prose, the dated notes, the annotated-out `tests/hooks/**` entry, one long trailing
comment, and the `launch_blocker_resolved` key (a dated `[RESOLVED 2026-06-09]` note that nothing reads;
the one deliberate data change, `yaml.safe_load` differs from the file at 8b57336 in that key alone).

**Adding here, not there.** New dated narrative about a lane goes in this file; the YAML keeps only what
an editor needs to act.

The moved text is VERBATIM, grouped by the YAML's own sections. Nothing was deleted.

### Head: source and verification provenance

*(original lines 4-6 at 8b57336, verbatim)*

```yaml
# Source of truth a cold "proceed lane X" session reads. Built bottom-up from the
# Valoria Master Workplan v2 (2026-05-31) "Three-Lane Operating Model"; lane-disjointness
# and reserved ranges verified against live repo state this session (ED max 884, PP max 726).
```

### Head: session-lane declaration, and the RETIRED-MACHINERY note (2026-07-01, ED-1084)

*(original lines 8-16 at 8b57336, verbatim)*

```yaml
# A session DECLARES its lane via:  env VALORIA_LANE=<A|B|C>   OR   file /home/claude/.valoria_lane
# The bootstrap Status Block then prints that lane's line (github_ops.report_lane).
#
# ⚠️ RETIRED-MACHINERY NOTE (2026-07-01, ED-1084): the registers/handoffs/*.yaml + session_logs/
# per-lane continuity machinery referenced below was retired with the orchestrator (LB-22)
# and relocated to deprecated/session_machinery/. Lane OWNS-globs and reserved-ID ranges
# here remain live; launch_protocol steps that mention github_ops/g.* or registers/handoffs/*.yaml
# are historical.
#
```

### Head: NAMING COLLISION WARNING (2026-07-02)

*(original lines 17-23 at 8b57336, verbatim)*

```yaml
# ⚠️ NAMING COLLISION WARNING (2026-07-02): this file's "Lane A/B/C" (write-disjoint
# session concurrency lanes, defined below) is a DIFFERENT, OLDER concept from the
# ED-<LANE>-NNNN editorial namespace's 9 lanes (MB/PC/FI/SC/FA/WR/IN/GO/SE — CLAUDE.md
# §3, ED-IN-0001). Do not conflate them. HANDOFF.md is no longer the only live continuity
# surface: per-lane files now live at registers/handoffs/HANDOFF_<LANE>.md (2026-07-02, using the
# ED-<LANE>-NNNN taxonomy, NOT this file's A/B/C), with root HANDOFF.md as a thin index.
# See HANDOFF.md's own header for the current structure.
```

### Head: ID ALLOCATION note (2026-07-05)

*(original lines 30-34 at 8b57336, verbatim)*

```yaml
# ID ALLOCATION (2026-07-05 note superseding the v5 §0a exhaustion warning): the flat ED
# sequence is FROZEN (ED-IN-0001 cutover 2026-07-02); all new EDs allocate per-lane from
# references/id_reservations.yaml `lane_ids` (read next_free, bump, co-commit). The old
# shared-block exhaustion problem is structurally moot. roadmap_state.yaml (referenced in a
# concurrency rule below) was RETIRED 2026-07-05 to deprecated/references/ (ED-IN-0006).
```

### Lane A `owns`: the `designs/scene/**` annotation (2026-06-12, Jordan)

*(original lines 64-64 at 8b57336, verbatim)*

```yaml
      - "designs/scene/**"          # [2026-06-12 Jordan] scene -> Lane A (sole design-content lane; owns all sibling designs/ globs). Resolves OWNS-GAP: social_contest/combat_engine_v1/conviction_track/derived_stats/miraculous_event/investigation_systems/fieldwork were unowned. Fieldwork to move into designs/scene/fieldwork/ (separate Lane-A op).
```

### Lane A: `launch_blocker_resolved` (the one key removed from the data)

*(original lines 76-80 at 8b57336, verbatim)*

```yaml
    launch_blocker_resolved: >
      [RESOLVED 2026-06-09] check_handoff_conflicts(Lane A owns) returns NONE this session.
      The named overlap handoffs (2026-05-29-resolution-diagnostic-faction-ratifications;
      combat-armature) were archived by the 2026-06-09 consolidation master, so Track 1.1 is
      satisfied. Lane A is launch-ready.
```

### Lane B `owns`: the retired-harness annotation (S6/6a)

*(original lines 85-85 at 8b57336, verbatim)*

```yaml
      - "deprecated/skills/valoria-orchestrator/scripts/**"   # retired harness — forked 2026-08-23 (S6/6a); pattern now matches nothing and is kept only so an old lane citation still reads
```

### Lane B `owns`: the annotated-out `tests/hooks/**` entry (ED-IN-0119)

*(original lines 87-90 at 8b57336, verbatim)*

```yaml
      # - "tests/hooks/**"   # tree emptied 2026-08-01 (ED-IN-0119): 11 dead modules
      #                      # retired to deprecated/tests/hooks/, 2 live ones moved
      #                      # to tests/valoria/. Kept as a comment, not deleted, so
      #                      # the lane's history stays legible.
```
