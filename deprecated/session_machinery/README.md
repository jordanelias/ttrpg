# Retired session-log / checkpoint / handoff machinery

**Relocated here 2026-07-01 (ED-1084)** per CLAUDE.md §1's recommended cleanup. These files
belonged to the orchestrator-era continuity model (per-session logs, checkpoint file,
per-lane `handoffs/*.yaml`), retired when the ecosystem moved to Claude-Code-native tooling
(2026-06-24 migration; orchestrator retired 2026-06-28, LB-22).

**Do not resume from anything in this folder.** The only live continuity surface is
`HANDOFF.md`; continuity = git history + `HANDOFF.md` (CLAUDE.md §1–2).

Original locations:
- `session_log_current.md`, `session_log_archive.md`, `session-handoff-2026-05-06.md` — repo root
- `session_logs/` — repo root
- `handoffs/` — repo root (per-lane YAML handoffs; lane OWNS-globs live on in
  `references/lane_assignments.yaml`)
- `canon/session_checkpoint.md` — carried `status: active` but was NOT authoritative
- `references_subsystems/{handoff,checkpoint,session_log}_subsystem.md` — from
  `references/subsystems/`; documented the retired machinery as if live
