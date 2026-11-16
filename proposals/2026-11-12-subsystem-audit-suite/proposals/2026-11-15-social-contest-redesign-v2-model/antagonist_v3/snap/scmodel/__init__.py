"""scmodel -- an EXECUTABLE TRANSCRIPTION of the social-contest proceeding as the amended spec states it.

Spec: proposals/2026-11-12-subsystem-audit-suite/proposals/2026-11-14-social-contest-redesign.md (RD) and its
_part2/_part5, with workplans/valoria_master_workplan_v12_part22_b24p*.md (the PLAN) governing where they differ.
This is a scratch model for stress-testing the spec's logic. It is NOT repository code and improves nothing:
where the spec is wrong it is implemented as written and logged in ../SPEC_GAPS.md (ids Gnn are cited in comments).
"""
import os
import sys

REPO = os.environ.get("VALORIA_REPO", "/home/user/ttrpg")
if REPO not in sys.path:
    sys.path.insert(0, REPO)
