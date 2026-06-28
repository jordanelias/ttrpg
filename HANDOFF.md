# Handoff

Plain, hand-maintained continuity for Valoria. Update this when you pause mid-task; a
git commit *is* the session close. The SessionStart banner (`tools/session_status.py`)
surfaces the "Next actions" section below, alongside `git status` / last commit.

This replaces the old session-log + `canon/session_checkpoint.md` + checkpoint machinery
(which depended on the retired GitHub-API harness and token budgets).

## Pending

- _(nothing in flight)_

## Decisions

- 2026-06-28 — **Master Workplan v5** authored (`designs/audit/2026-06-28-recent-work-orchestration/`),
  reconciling the post-v4 work (06-12→06-28) into one register and superseding v4. Roadmap +
  lane_assignments repointed to v5. Ledger verified live: 711 entries / 0 duplicate IDs / ED 1042.
- 2026-06-28 — **ED-912**: Disposition & Knot unified on a ±5 swing (Bonds ≥5 now a Knot
  prerequisite; break = Disposition −3 / 4 Composure). Resolves ED-841/842/912/914; supersedes
  PP-632/PP-684. Source-of-truth + consumer tail regenerated; "Stance table" rename in combat.
- 2026-06-26 — **J-31** social-contest docket recovered (ED-938/939/1042 + rule resolutions);
  22-doc cross-corpus reference + terminology repair landed (#13). contest.py sim edit deferred
  behind pre-existing sim-fabrication debt (19 uncited constants on main).
- 2026-06-24 — Migrated the Claude↔GitHub automation to a Claude Code-native model:
  retired the `/home/claude` GraphQL/cache/session harness; gates now live once in `tools/`
  and run in CI (authoritative) + local hooks/`.githooks` (advisory). See the migration PR.

## Next actions

_(Reserved-ID blocks are exhausted — ED ceiling 1042 past A/B/C 890–999. Re-block before any new ID
allocation: workplan-v5 **LB-21**, at the next integration pause.)_

- **Done this pass:** coverage_matrix size threshold consolidated to one source
  (`ci_register_size_check.py` reads it from `atomization_rules.yaml`, safe fallback); old-harness
  boilerplate (`Model:`/`assert_bootstrap`/`g.read_files_graphql`) stripped from the 12 simple
  `skills/*/SKILL.md`.
- **Skill-port remainder (LB-22):** rewrite `valoria-vector-audit` to read the working tree (its
  read-path is load-bearing — a real rewrite); decide whether `valoria-orchestrator` (retired-harness
  skill) stays; **then** flip the `/home/claude` warning in `ci_hooks_verifier.py` to blocking.
- **CI debt blocking-flips (LB-23):** after the **K-2 SHA-split** (115 `canonical_sha` fields out of
  `canonical_sources.yaml` → `references/canonical_freshness.yaml`), flip `freshness_gate`'s
  stale-canonical step back to blocking; reconcile/flip `validate_ed_citations` (HANDOFF said
  report-only ~722, but the tool currently `sys.exit(1)` — verify which is live in CI). Solo / K-2 / LB-6.
- **`ci_political_v30` read-routing (LB-24):** raw file ~26k but tracked read returns 0 (index-routes).
- **Ledger-status reconciliation (LA-23, Lane A):** the 2026-06-28 ED-912 ruling regenerated prose but
  left **ED-841/842/912/914 at status=open** in the ledger (ratified-in-prose, not-in-ledger); and the
  J-31 commit (#13) referenced **ED-938/ED-939 which were never filed** to `editorial_ledger.jsonl`.
  Flip the four / file the two (or repoint #13's references). Each also subtracts from the report-only
  `validate_ed_citations` count (748 corpus-wide; the job is `continue-on-error`, non-blocking).
- **Design-tier docket awaiting Jordan:** J-31 extended (social-contest deliberative-game findings,
  row #39 → LA-19) and the new **J-36** (Key-bus closure for the 6 off-bus writers, row #40 — gated on
  the distillation report's deferred adversarial pass).
