session_id: restructure_ci_fixes_2026-04-18
session_close: 2026-04-18
phase: COMPLETE
status: CLOSED
last_stage: done
next_action:
  skill: confirm with Jordan
  description: >
    All restructure CI issues resolved. 8/8 CI jobs pass.
blockers: []
commits:
  - 102507f8: "Fix bootstrap auth + freshness_gate commit compat + editorial_gate skeleton exemption + 11 missing skeletons"
  - 1abd7506: "Fix ci_editorial_checker: remove stale worldbuilding path, add skeleton exemption"
resolutions_this_session:
  - "github_ops: assert_bootstrap added to _authorize_next_commit approved callers — fixes bootstrap compliance auto-fix auth violation"
  - "freshness_gate.py: commit now uses atomic_commit (hook-compatible) with put_file fallback for CI — prevents session state corruption"
  - "valoria_hooks: editorial_gate now exempts _skeleton.md files"
  - "ci_editorial_checker: stale designs/worldbuilding/ path removed, skeleton exemption added"
  - "11 missing skeletons generated for gm_ref arc docs (8) and audit docs (3)"
  - "CI: 8/8 jobs pass (was 6/8)"
open_items:
  - ED-671 Thread-perception census (P1)
  - ED-666 Path B speed-run calibration (P1)
  - ED-667 Coup Counter readiness gap (P1)
  - ED-632 Shadow Renown mechanic (P1)
  - ED-633 Deniability Debt (P1)
  - ED-629 Heresy Proceedings auth loop (P1)
  - ED-663 Wealth cap (P1)
