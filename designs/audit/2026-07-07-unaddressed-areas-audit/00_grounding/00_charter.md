# Unaddressed-Areas Comprehensive Audit — Charter

## Status: PROPOSED (Jordan-vetoable throughout; the audit half of this PR edits no canon)
## Date: 2026-07-07 · Lane: IN (cross-cutting) · Branch: `claude/fable5-audit-coverage-gaps-22nz7i`
## ED anchor: ED-IN-0017 (allocated this PR)

## Mandate

Jordan directed (2026-07-07): **two deliverables, one PR — (1) a comprehensive audit of every
area the 2026-07-07 coverage review found unaddressed by last week's Fable 5 audits; (2) a Key &
Echo armature that draws from these findings.** This charter governs deliverable 1. Post-charter
additions by Jordan the same day: a **pessimistic NERS review** (C-NERSPESS) and a **pessimistic
diagnostic resolver review** (C-RESPESS).

## The material — what last week covered, and the gaps this audit closes

Last week's Fable-tier coverage: the NERS qualitative audit (PR #77 — 12 subsystem dossiers,
corpus lenses), the edge-playability audit (PR #81 — ~60 seams, clusters A–G,I), the Fable 5
social-contest six-dimension audit (PR #80 — the only per-subsystem deep audit), the Cannae
root-cause audit (PR #73), the weapon-morphology granularity audit (PR #74). The coverage review
found four gap classes, which this audit's clusters map onto:

**Gap class 1 — subsystems without six-dimension depth:** fieldwork/investigation (GAP-1, EP-8,
no CURRENT.md row) · threadwork (never audited directly) · faction/political (thin, fork 10,
ep-14) · NPC (GAP-5 + the 449-finding 06-22 orphan) · mass battle (fidelity-audited, never
playability-audited; RC-5 open) · personal combat (GAP-6 re-hunt obligation live; ED-1042
unowned) · the σ/dice substrate (assigned to no cluster ever; N-10 stale verdict) · settlement/
victory/era/church/strain (cluster-E-only) · articulation (seam-side only).

**Gap class 2 — seams no audit covered:** the Godot port seam (NOW DEFERRED BY RULING — trigger
= Gate-0 entry; recorded in HANDOFF_GO) · injectors (miraculous_event, scenario_authoring — in
the edge inventory's preamble, in no cluster) · sim-internal dispatch seams beyond contest ·
the diagonal direction (causes[] unauthored in practice) · all playability verdicts are
paper-walks (no human-plays evidence anywhere).

**Gap class 3 — transitions and stubs:** doc:null ×10 (npc_memory, scene_slate, game_director,
scene_timer, audit, domain_actions, settlement_economy, engine_clock, faction_politics[stale],
scenario_authoring) · §6.1/§6.3 empty mode-transition headers · ~19 sim NotImplementedError
stubs never mapped to milestones · ~21 filed lane EDs from the three 07-05 ratifications, none
begun (audit-rich, execution-light).

**Gap class 4 — designated-but-unexecuted Fable nodes:** the emergence audit (CLAUDE.md §10;
~87% win-share degeneracy unflagged — RULED: run the current-state probe now) · an independent
audit of narrative-engine v2 (still-scheduled, NOT in this audit — needs its own strong-critic
session with a defender/steelman pairing) · the 32 deferred-unverified NERS candidates.

## Criteria (the corpus's own instruments — unchanged from #77/#81)

Throughlines framework PP-672/PP-674 (N · Ω(a–d) · Q-robust/smooth/elegant + dramatic
legibility) · P-01..15 + GD-1..3, esp. P-14 · the edge rubric (MOMENT/DECISION/FEEDBACK/LATENCY/
FRICTION/RECIPROCITY) where seams are judged · the five rolling-engine properties
(`skills/valoria-resolution-diagnostic/SKILL.md`) for resolver clusters.

## Clusters (14)

C-REACH island/reachability sweep (D1b generalized; paired skeptic per verdict) · C-KEY key/echo
transport census (emit-clause coverage, §12.3 population reality, consumer closure, the 44-row
registry×rendering sweep data) · C-FI fieldwork/investigation depth · C-TW threadwork depth
(+ thread-economy exploit arena) · C-FA faction/political depth (+ faction exploit arena) ·
C-NPC NPC cluster + orphan triage prep · C-SIG σ/dice substrate (exploit-hunter + numeric
verifier) · C-INJ injectors + diagonal · C-STUB stub × milestone map · C-EMERGE emergence/
degeneracy probe (bounded seeded runs; null-hypothesis agent) · C-MBSE MB playability + SE
strategic (thinner, stated) · C-VERIFY the 32-candidate deferred backlog · **C-NERSPESS
pessimistic NERS review** (attack every #77 PASS/PARTIAL under a worst-case prior; a PASS that
cannot survive a pessimist is reported with the downgrade evidence) · **C-RESPESS pessimistic
diagnostic resolver review** (the resolution-diagnostic Phase 0–6 pipeline run pessimistically
across the δσ kernels and the [ASSUMPTION]-grade module resolvers; worst-case regimes,
degenerate inputs, dual-formula coexistence N-2, between-integer band semantics).

## Method and conventions

- **Relay pattern (ED-1083):** Sonnet evidence clusters, read-only tools, barred from verdicts;
  independent refuters on every carried P1/P2 finding (claim + this charter only; prompted to
  REFUTE; default-to-refuted when uncertain; intent gate DELIBERATE/NOT-INTENDED/UNDETERMINED
  with cited intent evidence); Fable 5 orchestrator renders all verdicts and spot-verifies every
  headline claim against the working tree (V-numbered verification log).
- **Non-duplication:** #77 (F-1..F-5, S-1/S-2, R-1..R-6, GAP-1..6), #80 (N-1..N-10, KT/KU),
  #81 (EP-1..11, ep-12..31, SIG-1..4), and all filed lane EDs are KNOWN calibration —
  re-reporting one as a discovery is an audit failure. `finding_status.md` tags every carried
  item KNOWN-TRACKED / KNOWN-UNTRACKED / NEW.
- **Funnel discipline:** P1/P2 verified (refuter pass), P3 collected unverified, every drop
  logged. Per-cluster depth stated honestly; no silent caps.
- **Read-only mandate (audit half):** no canon, params, code, ledger, or handoff edits from the
  audit; candidates go to `ed_options.md` deliberately UNFILED (Jordan ratifies post-merge, the
  #77/#80/#81 precedent; ED-1094 exception clause — the held-back set is loud in the PR body).
  C-EMERGE runs sims read-only; outputs archived under `01_workings/`, no sim code edited.
- **Tiering (CLAUDE.md §10):** Sonnet in the field, Opus for judgment-heavy synthesis, Fable at
  the gate (verdicts, reconciliation, report — this session). Escalation: two independent lenses
  disagreeing after one reconciliation round → Fable adjudicates; any finding that would overturn
  RATIFIED canon → Fable verdict + loud needs_jordan.

## Deliverables

```
00_grounding/00_charter.md                  # this file
01_workings/cluster_<id>.md                 # 14 evidence dossiers (archived agent returns)
01_workings/refutations/                    # refuter records
01_workings/emergence/                      # C-EMERGE run outputs (seeded, bounded)
unaddressed_areas_audit_v1.md               # main report, verdict-first, V-log
finding_status.md                           # KNOWN-TRACKED / KNOWN-UNTRACKED / NEW ledger
ed_options.md                               # candidate EDs, deliberately NOT filed
```

## Relationship to deliverable 2

The armature (`designs/architecture/key_echo_armature_v1.md`, ED-IN-0018) binds to this audit's
findings: every seam-contract row cites the cluster finding(s) motivating it; C-KEY's sweep data
becomes the armature's §2 outward rows; C-REACH's matrix seeds conformance check A13; the fork
docket (armature §5) consolidates every needs_jordan item either audit surfaces.
