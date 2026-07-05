# Finding Status Ledger — Fable 5 Social Contest Audit

## Status: PROPOSED (audit findings — Jordan review)
## Date: 2026-07-05

Every finding referenced by the main report, tagged per PR #77's novelty vocabulary. NEW findings
appear here only after surviving the independent critic pass (`01_workings/critic.md`).

## KNOWN-TRACKED (cited, not re-litigated)

| ID | Finding | Tracking | Disposition here |
|---|---|---|---|
| KT-1 | Four deliberative games / mature-Agôn dominance ("one game wearing eight venue skins") | Workplan #39 / J-31-extended → LA-19; Stage 4 ratified-as-next | Cited as the load-bearing content gap; feeds D6 |
| KT-2 | Obscuring styles dominated in single-exchange proceedings (Terminal Doubt) | ED-1060 (open with Jordan) | Cited only |
| KT-3 | Coalition REINFORCE dominates solo CLASH | ED-297 (ratified-as-intended) | Cited only |
| KT-4 | CR5 self-Face-backfire wiring | Settled — wired at `sim/personal/contest/resolver.py:404-419` (PR #77 refutation) | Cited only |
| KT-5 | Thread junctures absent from rebuilt kernel (`sim-kernel-no-thread-hooks`) | PR #77 dossier, P3 | **Deepened** in D3 as the P-14 bar |
| KT-6 | Recall near-costless | PR #77 dossier, P3 | Cited; overlaps KU-1 |
| KT-7 | Playability bar has no maintained home (F-3) | PR #77 main report | Cited; D4 supplies the contest-scoped instance |
| KT-8 | Convergence-marker engine has no engine (F-2) | PR #77 main report | Cited; D5 supplies the contest-side evidence |

## KNOWN-UNTRACKED (surfaced by PR #77's hunt, not yet in the ledger — re-examined and deepened here)

| ID | Finding | Source | Where deepened |
|---|---|---|---|
| KU-1 | No global bonus-die cap across Recall/Corroborate/Prep/Findings stacking (+8D over base reachable in exchange 1) while genre/audience boost is capped +2D | PR #77 `hunt_social_minmax.md` L-A | D2 Ω(d) |
| KU-2 | Appraise audience-boost read is a solvable public lookup (faction→boost deterministic and public) | PR #77 `hunt_social_minmax.md` L-B | D2 Ω(d) / D4 |
| KU-3 | Face/Rattled buffer inert in code outside the CR5 self-backfire channel — no live defensive tradeoff | PR #77 `hunt_social_minmax.md` L-E | D1 / D2 Q-robust |

## NEW (first surfaced by this audit — pending critic pass)

| ID | Finding | Evidence anchor | Critic verdict |
|---|---|---|---|
| N-1 | The promoted contest kernel is unreachable from the campaign loop: `scene_dispatch` routes contests to the deprecated legacy stub and structurally defers every contest scene ("context-derivation gap") | `sim/cross_scale/scene_dispatch.py:63,100-108`; `sim/personal/contest/__init__.py` re-exports | _pending_ |
| N-2 | Two contradictory Argue-pool formulas are simultaneously live (legacy stub canon-verbatim vs kernel `Pool.size` `[SEED]`, no Wounds/fatigue coupling) | `sim/personal/contest_legacy_stub.py:111-127` vs `sim/personal/contest/primitives.py:208-211` | _pending_ |
| N-3 | `module_contracts.yaml` social_contest entry drifted from code: pre-CR2 `resolver: dice_pool`; declared Key strings appear nowhere in the kernel; no `godot_home`/`typed_params` (combat entry has both) | `references/module_contracts.yaml:425-447` | _pending_ |
| N-4 | Audience-resistance erosion (ED-295 Option D) is prose-canonical but unplumbed — `MECHANICS["audience_resistance"] = PARTIAL` | `params/contest.md:365` vs `sim/personal/contest/wrapper.py:~301` | _pending_ |
| _further NEW rows added from dossier evidence after the critic pass_ | | | |

## Currency-surface observations (not findings; read-only notes)

- `handoffs/HANDOFF_SC.md` "NEXT: Stage 3" trails the ratified Gate C state (ED-1062) by one stage.
- `CURRENT.md` social-contest row still says "Stage 1a σ-kernel landed"; Stages 1b–3 have since landed.
