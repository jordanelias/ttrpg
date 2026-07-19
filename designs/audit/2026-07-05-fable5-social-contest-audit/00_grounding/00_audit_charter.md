# Fable 5 Social Contest Audit — Charter

## Status: RATIFIED — 2026-07-05 (PR #80 merge + Jordan post-merge instruction 'Ratify all'; ED-1094 merge-ratifies convention). D6 sequencing adopted; candidates filed as ED-SC-0002..0010 + ED-IN-0012..0013 (see ed_options.md ID map).
## Date: 2026-07-05
## Lane: SC (social contest)
## Branch: `claude/fable5-social-contest-audit-oxibtb`

## Mandate

Jordan requested a **read-only Fable 5 audit** of the social contest system, evaluating:

1. **D1 — Code architecture** (`sim/personal/contest/`, campaign-loop integration, contract/registry currency, port-readiness)
2. **D2 — Qualitative NERS compliance** (North-Star framework `references/throughlines_meta.md`: N → Ω → Μ/М/Τ → Q; rolling-engine N/R/S/E as annex)
3. **D3 — Throughlines and meta-throughlines** (T-03, T-14, T-17, T-23, T-24; М-patterns; P-14 as the direct bar)
4. **D4 — Playability and player experience** (dramatic-legibility three-question walk, cognitive-load ceilings, interaction-walkthrough coverage)
5. **D5 — Interactions**: domain echoes, narrative emergence, prose writing (declared vs wired edge inventory)
6. **D6 — Viability path**: how best to pursue social contest as a viable gaming experience (ranked sequencing judgment)

## Read-only mandate

This audit **does not modify** canon docs, `params/`, code, the editorial ledger, `CURRENT.md`,
`module_contracts.yaml`, or any handoff file. The only writes are the artifacts in this directory.
Findings that would change canon are expressed as **candidates** in `../ed_options.md`, deliberately
**not filed** — under the merge-ratifies convention (ED-1094), filing them here would ratify them on
merge, which a read-only audit must not do. This held-back set is called out in the PR body per
CLAUDE.md §2's "the exception must be loud" rule.

## Model tiering (CLAUDE.md §10)

- **Fable 5** (orchestrator): all verdicts, the D1 deep-read, finding reconciliation, D6 synthesis.
- **Sonnet** (agents A–D): evidence gathering only — line-referenced dossiers in `../01_workings/`,
  explicitly barred from rendering verdicts.
- **Sonnet** (agent E): independent critic over the draft report, given only the draft + this charter
  (agonist→antagonist relay; structural independence).

## Non-duplication discipline

PR #77 (`designs/audit/2026-07-04-ners-qualitative-audit/`) already audited social contest at
corpus-dossier depth. This audit **cites and extends**; it does not re-litigate. Every finding in
`../finding_status.md` carries one of:

- **KNOWN-TRACKED** — already filed/ratified; cited and passed over.
- **KNOWN-UNTRACKED** — surfaced by PR #77 but not yet in the ledger; re-stated here with deeper evidence.
- **NEW** — first surfaced here; must survive agent E's refutation pass to appear in the main report.

## Out of scope

- The four filed/settled items from PR #77's hunt: four-games collapse (Stage 4 pending, workplan #39 /
  LA-19), Obscuring dominance in single-exchange proceedings (ED-1060, open with Jordan), coalition
  REINFORCE dominance (ED-297, ratified-as-intended), CR5 self-backfire wiring (confirmed wired,
  `resolver.py:404-419`).
- Any fix, retune, or re-spec — this audit names seams; it changes nothing.
- Other subsystems, except where a social-contest edge terminates in them.

## Deliverables

```
00_grounding/{00_audit_charter, 01_criteria_and_lineage, 02_prior_art_map}.md
fable5_social_contest_audit_v1.md      # main report, verdict-first
finding_status.md                      # KNOWN-TRACKED / KNOWN-UNTRACKED / NEW ledger
ed_options.md                          # candidate ED-SC entries, NOT filed
01_workings/{dossier_code_architecture, dossier_design_and_ners, dossier_interactions,
             dossier_playability, critic, README}.md
```
