# Finding Status Ledger — Fable 5 Social Contest Audit

## Status: PROPOSED (audit findings — Jordan review)
## Date: 2026-07-05

Every finding referenced by the main report (`fable5_social_contest_audit_v1.md`), tagged per PR #77's
novelty vocabulary. NEW findings carry the independent critic's verdict (`01_workings/critic.md`).

## KNOWN-TRACKED (cited, not re-litigated)

| ID | Finding | Tracking | Disposition here |
|---|---|---|---|
| KT-1 | Four deliberative games / mature-Agôn dominance ("one game wearing eight venue skins") | Workplan #39 / J-31-extended → LA-19; Stage 4 ratified-as-next | Cited as the load-bearing content gap; feeds D6 |
| KT-2 | Obscuring styles dominated in single-exchange proceedings (Terminal Doubt) | ED-1060 (open with Jordan) | Cited only |
| KT-3 | Coalition REINFORCE dominates solo CLASH | ED-297 (ratified-as-intended) | Cited only |
| KT-4 | CR5 self-Face-backfire wiring | Settled — wired at `sim/personal/contest/resolver.py:404-419` (PR #77 refutation) | Cited only |
| KT-5 | Thread junctures absent from rebuilt kernel (`sim-kernel-no-thread-hooks`) | PR #77 dossier, P3 | **Deepened** in D3 as the P-14 bar (fails at kernel depth) |
| KT-6 | Recall near-costless | PR #77 dossier, P3 | Cited; overlaps KU-1 |
| KT-7 | Playability bar has no maintained home (F-3); UI v4.1 stale/contaminated (Taint/CD) | PR #77 main report + lens | Cited; N-6 adds the contest-specific depth |
| KT-8 | Convergence-marker engine has no engine (F-2) | PR #77 main report | Cited; D5 adds contest-side evidence (only COLLISION E contest-fed, as payload) |
| KT-9 | Audience-resistance derived-but-unplumbed, static vs ED-295 per-exchange erosion | Self-flagged in code with reserved ED range (`wrapper.py:74-76,295-301` — "reserved ED stub, contest_rebuild ED-1055..1079"); tracked-by-plan | Cited as Q-robust evidence (§2), not filed as NEW |

## KNOWN-UNTRACKED (surfaced by PR #77's hunt, not in the ledger — re-examined and deepened here)

| ID | Finding | Source | Deepening |
|---|---|---|---|
| KU-1 | No global bonus-die cap across Recall/Corroborate/Prep/Findings (+8D doc-math reachable) | PR #77 `hunt_social_minmax.md` L-A | **Refined**: all four channels are entirely unimplemented in the kernel — the hazard is doc-math-only; cap the spec before wiring (D2 Ω-d) |
| KU-2 | Appraise audience-boost read is a solvable public lookup | PR #77 `hunt_social_minmax.md` L-B | Confirmed: `guilds_boost_for` deterministic (`dictionaries.py:472-486`); only the armature dimension is reveal-protected |
| KU-3 | Face/Rattled buffer inert outside CR5 channel | PR #77 `hunt_social_minmax.md` L-E | Confirmed + sharpened: Face is monotonic-up (`primitives.py:83-90`); Rattled cascade has no kernel consumer; the CR3 tradeoff triangle runs on two legs |

## NEW (first surfaced by this audit)

| ID | Finding | Evidence anchor | Critic verdict |
|---|---|---|---|
| N-1 | Promoted kernel unreachable from campaign loop: dispatch routes to the deprecated stub AND structurally defers every contest scene; zero non-test callers of the kernel API (self-flagged in code comments, untracked in any ledger/workplan) | `scene_dispatch.py:19-24,63,100-108`; `__init__.py:30-36`; repo-wide grep | _pending_ |
| N-2 | Two contradictory Argue-pool formulas simultaneously live (stub = canon-verbatim incl. Wounds/fatigue, floor 1; kernel = `[SEED]` `max(5, faculty*2+3)`, floor 5) | `contest_legacy_stub.py:111-127` vs `primitives.py:208-211` | _pending_ |
| N-3 | `module_contracts.yaml` social_contest entry drifted: pre-CR2 `resolver: dice_pool`; five declared Key/state literals have zero kernel hits; no `godot_home`/`typed_params` | `references/module_contracts.yaml:425-447` | _pending_ |
| N-4 | Domain-echo spec conflict: §5.4 keys by track band (with loser-penalty) vs §6 keys by genre (no loser row); neither doc references the other's scheme. **N-4b**: "Piety Track" has two referents across three docs (debate tracker per glossary → `conviction_track_v1.md`; per-territory BG stat per `params/bg/`) | `scale_transitions_v30.md:194-199` vs `social_contest_v30.md:287-290`; `references/glossary.md:84`; `params/bg/core.md:117` | _pending_ |
| N-5 | `sim/cross_scale/domain_echo.py` is a complete §5 implementation with no caller; `scene_dispatch` passes `zoom_out({}, world)` — the outcome→echo mapping is empty (self-flagged in code, untracked) | `domain_echo.py`; `scene_dispatch.py:16-32,116` | _pending_ |
| N-6 | `valoria_ui_ux_v4_1.md` Part 6 specifies the pre-CR3 contest wholesale (Piety Track, Composure damage, Stance Triangle steps) — deeper than the Taint/CD contamination PR #77 flagged | `designs/ui/valoria_ui_ux_v4_1.md:592-649` | _pending_ |
| N-7 | ~13 recurring per-decision consultations per Agôn exchange vs the immersion audit's 3–4 personal-scene ceiling; no onboarding/complexity-gating doc exists | dossier D §2; `2026-05-08-meta-audit-immersion.md:64,82` | _pending_ |
| N-8 | (a) Kernel's structured `Chronicle` outcome record consumed by nothing but its own tests — the cheapest wiring win for the emergence feed; (b) `Chronicle`/`classify()` carries no focalization and renders neutral omniscient summaries — P-03 non-compliant if it ever reaches a player | `narrative.py:25,39-100`; repo-wide consumer grep | _pending_ |
| N-9 | Throughline registry stale w.r.t. the contest rebuild: T-14/T-23 cite retired names (Piety Track, Composure); Solidarity Resonant Style sits under T-16 (not T-17 as downstream docs assume); T-24 never names the contest though COLLISION E resolves through one | `references/throughlines_complete.md:121-124,137-145,192-200` | _pending_ |
| N-10 | The 2026-05-28 rolling-engine NERS-COMPLIANT verdict is stale-based: its component model (success-counting pool, 5-type interaction taxonomy, Composure, 2D floor) no longer exists in the kernel; conclusion not invalidated, basis gone — re-run needed post N-2 decision | dossier B Part 3; `ners_verdict_social_contest.md:6-19` | _pending_ |

## Currency-surface observations (not findings; read-only notes)

- `handoffs/HANDOFF_SC.md` "NEXT: Stage 3" trails the ratified Gate C state (ED-1062) by one stage.
- `CURRENT.md` social-contest row still says "Stage 1a σ-kernel landed"; Stages 1b–3 have since landed.
- `RES_FLOOR`/`REBUT_CAP` (`resolver.py:33,35`) are `[SEED]`-character constants lacking the tag.
