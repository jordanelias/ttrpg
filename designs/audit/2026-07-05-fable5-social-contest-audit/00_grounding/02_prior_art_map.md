# Prior Art Map — what is already settled, so this audit does not re-litigate it

## Status: RATIFIED — 2026-07-05 (PR #80 merge + Jordan post-merge instruction 'Ratify all'; ED-1094 merge-ratifies convention). D6 sequencing adopted; candidates filed as ED-SC-0002..0010 + ED-IN-0012..0013 (see ed_options.md ID map).
## Date: 2026-07-05

## 1. The contest_rebuild gate chain (all ratified — treated as fixed ground)

| Artifact | What it settled |
|---|---|
| `designs/audit/2026-06-01-contest-redesign/RATIFIED_2026-06-01.md` | CR1–CR7 ground-up principles as provisional canon-of-record |
| `designs/audit/2026-06-03-contest-groundup/` | The 9-module kernel prototype (151→385 tests) later promoted to `sim/personal/contest/` |
| `designs/audit/2026-06-28-social-contest-deliberation-critique/` | 38-finding critique ("four games collapse to one"); shaped the game-shape plan |
| Gate 0 (`2026-06-30-contest-stage0-reconciliation/DECISIONS.md`) | D0-1 appeals, D0-2 σ-sibling, D0-3 δσ TN7 (→ HYBRID via fractional-Ob memo, ED-1055) |
| Gate 1c (`2026-06-30-contest-gate-1c-packet/`) | v30 re-skin + `build_contest`/`resolve_contest` wrapper (PR #44) |
| Gate A (`2026-07-01-contest-gate-a-packet/`) | CR1–CR3 fold-in (ED-1055/1056), Face scale-binding, Composure retirement scope |
| Gate B (`2026-07-01-contest-gate-b-packet/`) | Typed dictionaries; Panel VoteAtClose (ED-1057/1059), Terminal Doubt branches (ED-1060 open), Guilds boost (ED-1061) |
| Gate C (`2026-07-01/02-contest-gate-c-packet/`) | Stage 3 rhetoric grounding + 4-axis adjudicator armature, FINAL (ED-1062) |

**Stage 4 (four deliberative games: Negotiation / Inquiry / Consensus beyond Agôn) is ratified-as-next
and unbuilt.** `handoffs/HANDOFF_SC.md` trails this state by ~one stage (its NEXT line still says
Stage 3); `CURRENT.md`'s row still says "Stage 1a σ-kernel landed". Both noted as currency-surface
observations in the main report — not fixed here (read-only).

## 2. PR #77 — the corpus-wide qualitative NERS audit (2026-07-04)

`designs/audit/2026-07-04-ners-qualitative-audit/` — status PROPOSED. Social-contest coverage:

- **`01_workings/dossiers/dossier_social_contest.json`** — core-loop map, decision-density table,
  verdict: "a well-theorized bet-under-uncertainty armature… the executable slice is currently one
  game wearing eight venue skins." Edge inventory including the faction/Domain-Echo edge marked
  **declared-only**.
- **`01_workings/hunts/hunt_social_minmax.md`** — six min-max lines L-A..L-F.
- **Refutations**: `refute_four-games-collapse-one-pattern.md` (REFUTED as P1; real phenomenon already
  filed at design-tier P2/P3, workplan #39 / J-31-extended → LA-19) and
  `refute_orientation-payoff-unwired.md` (REFUTED; CR5 is wired, residual = ED-1060).
- Headline findings F-1..F-5 are corpus-level; the two that bear on this audit are **F-2** (convergence
  markers / emergent-narrative engine has no engine) and **F-3** (playability bar has no maintained home).

### Disposition table this audit inherits

| Item | Status | Disposition here |
|---|---|---|
| Four-games / mature-Agôn dominance | KNOWN-TRACKED (workplan #39, LA-19; Stage 4 pending) | cite only |
| Obscuring dominated in single-exchange proceedings | KNOWN-TRACKED (ED-1060, open with Jordan) | cite only |
| Coalition REINFORCE > solo CLASH | KNOWN-TRACKED (ED-297, ratified-as-intended) | cite only |
| CR5 self-Face-backfire wiring | settled (wired, `resolver.py:404-419`) | cite only |
| **L-A** — no global bonus-die cap (Recall+Corroborate+Prep+Findings, +8D reachable while genre/audience is capped +2D) | KNOWN-UNTRACKED | re-examine, deepen (D2 Ω-d) |
| **L-B** — Appraise audience-boost read is a solvable public lookup | KNOWN-UNTRACKED | re-examine, deepen (D2/D4) |
| **L-E** — Face/Rattled buffer inert in code outside CR5 channel | KNOWN-UNTRACKED | re-examine, deepen (D1/D2) |
| `sim-kernel-no-thread-hooks` (§9.3–9.4b absent in kernel) | KNOWN-TRACKED in #77 (P3, threadwork) | deepen as the P-14 bar (D3) |
| `recall-near-costless` | KNOWN-TRACKED in #77 (P3) | cite; overlaps L-A |

## 3. Rolling-engine lineage (annex baseline)

- 2026-04-08 audit + simulation (`tests/audit/audit_sim_social_contest.md`, `tests/sim/sim_social_contest_stress*.md`).
- 2026-05-28 diagnostic batch: `resolution_diagnostic_social_contest.md` + `ners_verdict_social_contest.md`
  — **VERDICT: NERS-COMPLIANT** (Instance A; Persuasion clock + Composure recognized as non-rolling and excluded).
- `engine/sigma_leverage_engine_armature.md:198` explicitly **excludes** social contest from the σ-engine
  port ("over-engineering; fails NERS-N/E") — the boundary marker this audit honors.

## 4. What is genuinely un-audited before today

- The **campaign-loop reachability** of the promoted kernel (`mc_v18` → `scene_dispatch` path) — no prior
  audit traced whether the rebuilt engine can resolve inside a simulated campaign.
- **Contract/registry currency**: `references/module_contracts.yaml` `social_contest` entry vs the
  Stage 1b–3 code reality.
- **Formula coexistence**: legacy stub's canon-verbatim Argue pool vs the kernel's `[SEED]` `Pool.size`.
- The **P-14/thread juncture gap** at kernel depth (only P3-flagged in passing by #77).
- A **social-contest-scoped** North-Star walk (PR #77 ran it corpus-wide; the dossier is a summary, not
  a clause-by-clause walk of this subsystem).
- The **viability sequencing** question (D6) — never posed as a decision frame.
