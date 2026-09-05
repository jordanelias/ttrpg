# 11 · THE FOUR GAMES — AUDIT · PLAN · INSTRUCTIONS

## Status: **PROPOSED (2026-09-04). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE. Nothing here runs.** Read-only pass over `systems/social_contest/` at branch `claude/social-contest-system-review-dn2y5d`, HEAD `3ade3e33` (PR #364 merged). This file is the only artifact; no other file under the repository was created or edited.
## Auditor: Fable 5.1, `CLAUDE.md` §10 audit/planner node. Grade of the subject under `CLAUDE.md` §0.2: **one path executes** (`build_contest` → `Bout.resolve` → one terminal); the three other games are paper; every recommendation below is paper until its named artifact runs.
## Three deliverables in order: **PART 1 AUDIT** (§1–§4) → **PART 2 PLAN** (§5–§8) → **PART 3 INSTRUCTIONS FOR OPUS 5** (§9–§12). Part 3 is the operative section and is written to be executed without this author.
## Scored against `CLAUDE.md` §0.06 (the definitions) with `skills/valoria-resolution-diagnostic/SKILL.md` (the method). E is scored last, as a ratio. R is scored on all three halves. N is tested from six directions.

---

## §0 · Scope, what changed, what was executed, and the corrections this pass makes to inherited claims

### §0.1 Scope, and the two exclusions

**In scope:** the social-contest engine — `systems/social_contest/` in full — and its four games: `agon` (built), `negotiation`, `inquiry`, `consensus` (unbuilt; `wrapper.py:236-245 GAMES`, three `STUB` rows). The kernel was read module by module (§0.5); every load-bearing claim below carries a `path:line` I opened this session.

**Out of scope, by Jordan's instruction (*"Ignore the seams. I am rebuilding a lot."*):** `engine/cross_scale/scene_dispatch.py`, `parliamentary_bridge.py`, `echo_transport.py`, and the kernel↔campaign wiring. Nothing below audits, plans for, or prescribes anything there. Appendix A carries the one-line observations I met while tracing in-scope code, uninvestigated. Also out of scope: every other subsystem; the prior session's out-of-scope findings stay parked in `OUT_OF_SCOPE.md`.

### §0.2 What changed with the merges, and what each change does and does not do

**1. `CLAUDE.md` §0.06 is the canonical home of the NERS definitions** (`CLAUDE.md:165-224`). Three things are wider than the shorthand and all three bind here: N is tested from six directions and *an N-line holding in exactly one direction is narrowed, not passing* (`:191-193`); E is *never scored as an independent axis* — last, as a ratio against N and R (`:194-198`); R has a world half with no player in it and a completeness half (`:199-204`); S carries *pauses correctly* and *calculations consistent in methodology* — *two ladders for one quantity is an S defect even when each is individually correct* (`:205-208`). §4 scores against that text.

**2. Jordan ruled "1D is floor", and `engine/autoload/sigma_leverage.py:259-279 p_success` now floors the mean as well as the variance** (`effective_pool = max(1.0, float(pool))` at `:276`, used in both the location term `:277` and the spread term `:278`). **What it fixes:** the closed-form probability helper agreed with the sampler `roll_net_continuous` only at and above 1D; below 1D the two flooring conventions disagreed by up to 9.7 pp (`:264-267`). Now they agree. **What it does not touch, measured:** the contest kernel. `grep -rn "p_success\|roll_net_continuous\|continuous_engine_sample" systems/social_contest --include=*.py` → **zero hits**. The kernel draws through `resolver.py:28-32 roll_net` → `sigma_leverage.roll_net` (`:286-296`) → `dice_engine.roll_pool` — the **discrete** d10 path, floored at `max(1, int(round(pool)))` (`:294`). And the kernel's own pool floor is not 1D: `primitives.py:208-211 Pool.size = max(5, faculty*2 + 3)` is a **5D floor**, so faculties ≤ 1 all roll five dice (§1.2 row 1). The measured faculty-1 contests (81.9 % of councils, `08_NERS.md` §0.3) are therefore untouched by this ruling in three independent ways: wrong function, wrong floor, wrong pool. The defect that actually lives at faculty 1 is the quantization of the leverage channel by the integer ladder edges (§1.2), which the ruling does not reach. **The ruling is correct and the kernel is a second flooring convention beside it** — a `[SEED]`-adjacent literal `5` at `primitives.py:211` that cites nothing (only `Pool.BASE = 3` carries the `[SEED]` tag at `:209`). Recorded as an S finding in §4.

**3. `skills/valoria-resolution-diagnostic/SKILL.md` owns the method** and its §11.4 records the floor fix. Its §11.2's *"uniform impact is exact"* holds for the closed form and **not for the kernel's execution**, because the kernel adds a continuous shift to an integer roll and bands it against an integer Ob — §1.2 row 2 is the measurement.

### §0.3 ⚠ Four requirements Jordan added mid-session, carried into Parts 2 and 3

Relayed by the coordinator, verbatim: (1) *"the player has to have at least somewhat okay odds to 'win' or at least not completely lose, which is where degrees and bands come in"*; (2) *"there are many different lines of adjudication requiring verdict so you can win on one thing but partially lose three items and lose completely on five"*; (3) *"all of these games may concern more than one topic or the topic is a bundle of subtopics, and we need to be able to handle conditions and stuff"*; (4) *"for things like a negotiation it's possible for both sides to win or for there to be more than two sides, so it's not always a zero sum game necessarily"*.

These are not four feature requests. Read jointly they say the **unit of resolution is wrong**: the kernel resolves one matter between two sides to one label (`resolver.py:241` builds exactly `{A, B}`; `:462-466` returns one label). §3 grades the four games against them; §5 answers the shape question they pose; Part 3 carries them as work items. The coordinator's paired measurement that motivated them (the band ladder gives the 1-v-6 weak side 29.8 % `committee` on the same rolls where the production ballot gives it 0 % of any middle outcome) is **re-verified in §0.4 row A** rather than inherited.

### §0.4 Execution artifacts (scratchpad only; nothing under the repo written; no `pytest`)

| script | drives | headline |
|---|---|---|
| `m1_kernel.py` | 15 probes over the kernel's public API and primitives, ~120k bouts and ~420k receptions | the leverage staircase (row 1 below); `Resonance.effective` 0.372 vs inline 0.420; `classify("A_total")` → `CLEAR_WIN` vs `classify("a")` → `ROUT`; consensus margin bands `Partial`/`Failure` at every scale; all eight proceedings share `faults=(True,True,2,2)`, `start_ground=quality` (one exception), `allow_rebuttal=False`; `crowd().learned == False`; committee 1,991/2,000 on `formal_contest` 5v5; `guild_arbitration` P(A)=0.070 at 1v6; armature δσ Δ=+0.000 at faculty 1, +0.134 at faculty 2; `support`-forever accused loses 500/500 on both bar venues; `weighted == simple` 3,000/3,000 |
| `m2_paired.py` | the production terminal and the band ladder read off the **same** final state; draw reachability by bench size; the owner's ladder on the raw gap; 9-issue vector expectations; a two-issue fold prototype with shared side runtime; a per-side bar terminal on N sides | 1v6: vote `b`=0.934 `draw`=0.000, band `committee`=0.295; `draw` 0/4000 at bench 5, 7, 15 and 1,541/4,000 at bench 4; `degree_from_net(gap, 0)` at 1v6 → Partial 3.8 %; a fault on issue 1 clinches issue 2 at move 1 with zero new rules; two `GraceThreshold`s on one state → both sides win |
| inline CR4 probe | `+1` pool die under `PoolDesaturation` vs the bare ladder, pools 5–17, N=40k each | mean degree Δ: +0.221 (pool 5), +0.186 (7), **+0.000 (9), −0.053 (13), −0.065 (17)** under the extension; always positive under the bare ladder |

### §0.5 Coverage — what was read, at what depth

`contract.py`, `primitives.py`, `resolver.py`, `wrapper.py`, `modes.py`, `policy.py`, `degree_extension.py`, `faction.py`, `narrative.py`, `contest/__init__.py`: **full.** `armature.py:185-451`, `rhetoric.py:88-237,393-462`, `dictionaries.py:260-340,680-765`, `appraise.py:64-74,128-140`, `contest_legacy_stub.py:54-192`, `parliamentary_vote.py:68-102,120-220`, `agon_harness.py:1-115`, `parliamentary_stay.py` (docstring + grep): **partial**, the parts the claims below rest on. `_kernel_tests.py`: `:75-85`, `:182`, `:436-452`, `:1574-1582`, plus a whole-file scan for disjunctive and loop-embedded checks — **not audited check by check** (§12.3). Upstream: `dice_engine.py:1-270`, `sigma_leverage.py:200-320`; `engine/tests/test_contest_kernel.py` (full), `test_mc_v18_regression.py:140-158`, `test_f7_smoke_oracle.py:1-24`, `test_pipeline_reach.py:825-895`, `tests/valoria/test_import_cycle_game_state_npe.py:56-96`, `test_degree_ladder_single_owner.py:120-150`, `tools/balance_oracle.py:140-175`. Corpus: `10_SC_STRUCTURAL_READING.md` (full), `05`, `06`, `08`, `09` (full), `00` (full), `01_SPINE.md` §1.3–§1.5, §2, §3.4, §6.3, §7; `02` §4, §5.2–5.5, §7.2–7.3, §10.2–10.3; `03` §2.3, §5, §7.2–7.3, §10.2; `04` §4.2, §5, §7.2–7.3; PR #362 `04_CODE_ARCHITECTURE.md` §0, §A.1–A.2, §B.4–B.6, §C.2, §C.4, §C.5–C.5.1, §G.2.9; `01_AXIOMS.md:396-404`; `social_contest_v30.md:140-313`; `registers/editorial_ledger_sc.jsonl` (all 32 rows, id/status/needs_jordan); `HANDOFF_SC.md:1-140`.

### §0.6 Corrections to inherited claims — the assertion checked, not the prose above it

| inherited claim | source | verdict this pass |
|---|---|---|
| `hard` "is licit only before an unlearned or hostile bench, which no canonical proceeding builds" | `10_` §2.1; `06` P4.4 ("every production bench") | **FALSE for two of eight proceedings.** `modes.py:445 crowd()` builds `Adjudicator(learned=False, …)`; `contract.py:43 Panel.learned` is a majority, so a crowd bench is unlearned; `primitives.py:216-217 _hard_licensed` requires `(not learned or hostile)` — **executed: `hard` is licit before `crowd` at standing 7 v 5**. `formal_contest` and `grand_contest` are crowd proceedings (`modes.py:486-491`). True of the production proceeding (`guild_arbitration` → `panel`, learned) only. |
| the `id()` recycling hazard (consequence 3) | `10_` §1.6, marked "inference" | **attacked and not reproduced**: `del` + `gc.collect()` + a new `Adjudicator` did not reuse the id in CPython 3.11. Consequences 1 (key not computable before `build_contest`) and 2 (not serialisable) stand by reading `armature.py:393-395,:429` and `wrapper.py:151`; consequence 3 stays inference. |
| "the 1D-floor fix bears directly on the measured faculty-1 contests" | the brief | **it does not reach them** (§0.2 item 2, three independent reasons, one of them a grep). |
| `restricted` on `Venue` guards a dominant defensive line | `03_INQUIRY.md` §5.4, §10.2 | **re-measured, inverted** (§0.4; `08` row 1 confirmed): support-forever loses 500/500 on `inquisition_hearing_venue` and 500/500 `A_total` on `church_tribunal`. |
| CR4's `+1D` is negative above pool 7 under the ruled extension | `08` §2 row 4 | **re-measured, confirmed in sign** (§0.4 row 3), with a flat point at pool 9 the prior pass did not report. |
| the paired-terminal measurement (band `committee` 29.8 % where the ballot gives 0 % middle at 1v6) | the coordinator | **reproduced**: 0.295 / 0.000 (§0.4 row A). |

### §0.7 The three binding corrections, honoured

(1) The terminal is **RATIFIED** — `ED-1057` (`registers/editorial_ledger.jsonl:268`) designs the per-juror ballot verbatim, *"a lopsided room is near-unanimous"*, and its ratification tail selects `weighted_by_standing`; `resolver.py:98-147 VoteAtClose` is that design. Nothing below calls it wrong or unratified. (2) Therefore the 87.7 % crisis-side win rate is that design working on a lopsided input; the defect is upstream (seam, out of scope) and — per §3 — in what the *seam discards*, not in what the ballot returns. (3) The import-cycle test asserts **two families**, not a member count: `tests/valoria/test_import_cycle_game_state_npe.py:70-96` — `assert len(cycles) == 2` and one cycle per prefix. No cycle test blocks any change below.

---

# PART 1 — AUDIT

## §1 · The kernel a rebuilder meets: the load-bearing findings, re-verified

### §1.1 `10_SC_STRUCTURAL_READING.md`'s findings, carried forward only where I re-opened the anchor

| finding | re-verified at | status |
|---|---|---|
| **The armature is keyed on a memory address.** `ArmatureConfig.positions: {id(adjudicator-or-member) → ArmaturePosition}` (`armature.py:429`), consumed as `positions.get(id(m), …)` / `positions.get(id(adjudicator), …)` (`:393-395`). `build_contest` constructs the adjudicator itself (`wrapper.py:151`, `modes.py:445-447, :461`), so a caller cannot compute the key before the call; `Adjudicator` is `frozen=True` (`contract.py:24`) with value equality — executed: `a3 == a4` and `hash(a3) == hash(a4)` for two default judges, `id(a3) != id(a4)` — which is why `id()` was reached for. | opened | **stands.** Not on any branch's change list (`01_SPINE.md` §2 A6/A7 add the parameter and not the identity). Part 3 W-B3 |
| **`Resonance.effective` diverges from the live reception rule.** `primitives.py:247-248` computes `(1−leak)·role + leak·char`; `resolver.py:325-326` computes `max(RES_FLOOR, (1−leak)·joint_weight + leak·char)` with `Venue.joint_weight` (`:172-178`). Executed on identical inputs: **0.372 vs 0.420.** Exported at `contest/__init__.py:58`; zero callers (own grep). | executed | **stands** — a public primitive that teaches the wrong rule. W-A1 |
| **No interaction model.** `_apply` is per side (`resolver.py:341-438`); each side's reception rolls independently against `base_ob` (`:302, :307`) and accumulates its own `adv` (`:335`). `derive_interaction` (`dictionaries.py:310-323`) has zero resolution callers (own grep); `strain` appears in no kernel code outside table strings. **New this pass:** the compare-model canon describes (`social_contest_v30.md:182-210`: compare successes, margin − resistance → track) **exists in code, dead** — `contest_legacy_stub.py:132-190 resolve_exchange` rolls both pools, takes `margin = abs(a_net − b_net)`, moves the track by `max(0, margin − resistance)`. So the fork is not "build the model or not"; it is *the dead stub's model versus the live kernel's*, and the live one is the one the goldens pin. §8 escalation E1 |
| **Two win-condition families.** Executed for all eight proceedings (`m1_kernel.py` §7): `resolve()` returns a side label from five classes and a band string from `PersuasionTrack` (`resolver.py:91-95`); `Bout.resolve:466` reconciles them only by `"draw" if w == "draw" else "win"`, so a `committee` outcome is labelled `"win"`. `ProofBar:72` and `GraceThreshold:78` award a 0–0 close to the defender/non-petitioner — a burden rule inside two terminals. | executed | **stands.** W-C1 |
| **Seventeen duplicated rules.** Re-opened: D1 `resolver.py:91-95` literals vs `contest_legacy_stub.py:67-70` constants (values agree); D2 neutral start at `modes.py:475`, `contest_legacy_stub.py:71`, `resolver.py:86`, `faction.py:142`, `parliamentary_vote.py:100` (five homes); D3 `[4,6]` at `parliamentary_vote.py:71-72` and bare at `faction.py:142`; D5 `scale=1.5` at `resolver.py:86` and `faction.py:87`, `1.0` at `faction.py:128`; D6 above; D7 `armature.py:229` comments *"= resolver.RES_FLOOR value"* and never imports it, `_kernel_tests.py:1579` asserts `_SAO == 0.15` while `:450` imports `RES_FLOOR as _RF` and does not use it; D8 `Pool.size = max(5, 2f+3)` vs `build_argue_pool = max(1, 2p + h + fatigue)` (`contest_legacy_stub.py:111-129`); D9 `appraise.py:68-71` retypes the ordinal owned at `dice_engine.py:48-53`; D10 `degree_extension.py:138-139` hard-wires the extension the resolver injects (`resolver.py:307-308`); D11 `rhetoric.py:142` copies `:91` with two error contracts (`:108` `.get`, `:167-168` raises); D12 `armature.py:242-247`, `dictionaries.py:86-` `STYLES_TABLE`, `appraise.py:132-137` (hand-derived, says so at `:129-131`); D13 four bench aggregations (`contract.py:43-51`, `armature.py:286-297`, `resolver.py:133-141`); D14 `committee` at `resolver.py:93`, `faction.py:68-74`, `parliamentary_vote.py:191,205`; D15 `"a"/"b"` (`contract.py:7`) vs `'A'/'B'` (`contest_legacy_stub.py:91,103`, `parliamentary_vote.py:92`); D16 `modes.py:553-555` and `wrapper.py:181-190` build the panel terminal twice; D17 `resolver.py:362` assigns `Reserve.cur` around `primitives.py:55-56`. | all seventeen opened | **all stand.** Under §0.06 S, D1–D5, D8, D13, D14 are *calculations inconsistent in methodology* — each is one quantity with two computations. Part 3 phase A |

### §1.2 Findings new to this pass, executed

**Row 1 — the pool floor and the leverage staircase (`m1_kernel.py` §1–§2).** Under the live discrete draw the σ-leverage layer acts in **whole successes only** at the Failure/Partial/Success edges, because `net = roll_net(pool) + net_boost(lev, pool)` (`resolver.py:302`) adds a fraction to an integer and `degree_from_net` reads `margin = net − 2.0` against edges at 0, 1 and 3 (`dice_engine.py:234-239`; `Venue.base_ob = 2.0` at `resolver.py:157`). Measured, N=20,000 per cell:

| faculty | pool | `net_boost` | floor | P(≥1) discrete / no-boost | P(≥2) discrete / no-boost | P(Overwhelming) discrete / no-boost |
|---|---|---|---|---|---|---|
| 0 | 5 | −0.297 | 0 | — | — | (negative fraction is *not* rounded away; latent, unreachable from the seam) |
| 1 | 5 | 0.000 | 0 | 0.600 / 0.600 | 0.382 / 0.382 | 0.086 / 0.086 |
| 2 | 7 | 0.351 | 0 | 0.728 / 0.728 | 0.544 / 0.544 | 0.209 / 0.209 |
| 3 | 9 | 0.787 | 0 | 0.811 / 0.811 | 0.670 / 0.670 | **0.348 / 0.213** |
| 4 | 11 | 1.280 | 1 | 0.934 / 0.864 | 0.864 / 0.761 | 0.332 / 0.210 |
| 5 | 13 | 1.806 | 1 | 0.952 / 0.904 | 0.904 / 0.828 | 0.453 / 0.208 |

Three facts a rebuilder needs: (a) **faculties 0–3 all roll the same five-to-nine dice and their leverage is inert at the three lower edges** — `Pool.size`'s 5D floor and the integer edges together make faculty a no-op below 4 except through pool size; (b) the fractional part *does* act at the Overwhelming edge, because `overwhelm_bar(pool)` (`degree_extension.py:57`) is fractional — the staircase is at the owner's integer edges only, which is why row 3 moves P(O) and nothing else; (c) the negative fraction at faculty 0 rounds *down* into Failure — the quantization is asymmetric (a positive fraction is discarded, a negative one is charged). Reachable only by direct construction (the seam passes `max(1, round(L))`), so latent. This is `SKILL.md` §11.5 P-iii in the kernel's own arithmetic, and `08` §12.2's finding reproduced from a different direction. **The continuous draw does not have it**: on `roll_net_continuous` the same five cells move smoothly — but at pool 5 the two draws disagree by 10 pp on P(net ≥ 2) (0.600 vs 0.498), which `dice_engine.py:213`'s *"statistically equivalent"* does not survive at the pool the seam actually passes. That disagreement is a *substrate* fact and is recorded, not prescribed on.

**Row 2 — `draw` is unreachable on every shipped bench (`m2_paired.py` B).** `VoteAtClose` returns `"draw"` when `wA*2 == total` (`resolver.py:140-142, :145-147`). With equal weights that needs an even bench. Every factory builds an odd one: `panel(size=5)` (`modes.py:456`), `crowd(size=15)` (`:440`), `_default_panel(n=7)` (`:115`), `excommunication_mode(7)` (`:291`), `secret_council(5)` (`:304`). Measured at gap 0: **0/4,000 draws at benches 5, 7, 15; 1,541/4,000 at 4; 1,205/4,000 at 6.** A declared third outcome with no reachable input — an R-COMPLETE finding, small, and not a reason to touch the ratified ballot (a bench of even size would reach it).

**Row 3 — the paired terminals (`m2_paired.py` A), the coordinator's claim reproduced.** On the production proceeding, the ballot's verdict and the band ladder's verdict read off the *same* final state:

| A v B | vote a / draw / b | band A_total / A_dec / committee / B_dec / B_total | mean gap | max \|gap\| |
|---|---|---|---|---|
| 1 v 6 | 0.066 / 0.000 / 0.934 | 0.000 / 0.001 / **0.295** / 0.497 / 0.206 | −1.79 | 4.26 |
| 1 v 4 | 0.114 / 0.000 / 0.886 | 0.000 / 0.004 / 0.426 / 0.443 / 0.128 | −1.45 | 4.04 |
| 3 v 4 | 0.370 / 0.000 / 0.629 | 0.002 / 0.053 / 0.723 / 0.198 / 0.025 | −0.44 | 3.75 |
| 4 v 4 | 0.511 / 0.000 / 0.488 | 0.002 / 0.079 / 0.851 / 0.068 / 0.002 | +0.01 | 3.18 |
| 6 v 1 | 0.925 / 0.000 / 0.075 | 0.198 / 0.499 / 0.302 / 0.001 / 0.000 | +1.81 | 4.27 |

The ballot is a majority *count* and discards the magnitude of the room; the band ladder reads it. **The texture Jordan asks for in requirement (1) already exists one field deeper** (`PersuasionTrack.track`, `resolver.py:87`) and the production terminal does not report it. And the owner's ladder applied to the raw gap gives no middle either — `degree_from_net(gap, 0.0)` at 1v6: Failure 958 / Partial 38 / Success 4 (`m2_paired.py` C) — because its Partial window is one success-unit wide and the gap is in `adv` units. **The width of the middle band is the whole difference**, and the Persuasion bands' `committee` (`3 < t < 7`, i.e. `|gap| < 1.33` at scale 1.5) is canon (`social_contest_v30.md:279`). This decides §5.4: the band→Degree table, not a `SUCCESS_UNIT`.

**Row 4 — `support` by budget (`m1_kernel.py` §14).** `logos_spammer` never supports at budget 3 (12 → 9 → 6 → 3; `_low` needs `< 0.3`), supports once at 5, three times at 8. `support` spends 2 and regroups 4 (`primitives.py:51-52, :56`; `resolver.py:350-351`), builds +0.8 Standing, incurs no fault and no roll. Confirmed as the kernel's one riskless move; **not dominant on any canonical proceeding** (`08` SC4, not re-run) — an `[OPEN — Jordan tuning]` on `REGAIN > COST["support"]`, not a structural defect.

**Row 5 — `hard` before a crowd (§0.6).** Corrects the inherited claim; changes nothing measured (no shipped policy issues `hard` except `overreacher`, `policy.py:43`).

### §1.3 What executes, what is declared, what is dead — the accounting a rebuild needs

Inherited and not re-measured (`10_` §1.5, `06` §12.1): 62 % of non-test defs unreachable through the public API at any argument; 21 % of runtime lines under any API call. Re-verified by my own greps: zero callers of `Resonance.effective`, `derive_interaction`, `guilds_boost_for`, `appraise_armature`, `narrative.summarize`/`venue_brief`, `faction.coalition_vote`/`succession`, `contest_legacy_stub.run_contest`, `parliamentary_stay.invoke_stay`/`resolve_stay_lift`, `agon_harness` (remaining grep hits are docstrings and self-calls inside the same dead module). `mechanics_selftest` is reached only by `_kernel_tests.py`.

---

## §2 · Per-game audit — judged as a game

Each game: **logic** (does it do what it claims; can its arithmetic produce its stated range), **coherency** (does it fit the other three and the kernel's primitives, or invent a parallel vocabulary), **NERS** per §0.06 with E last and R on three halves. Seat playability is answered per game before R-CHOICE is scored.

### §2.1 Agôn — the built game

**What it is, executed end to end.** `build_contest(int, int, venue=<one of eight>)` → `Contest` → `resolve_contest` → `Bout.resolve` → one label. Eight proceedings differ in four live fields — `budget`, terminal class, adjudicator factory, and `start_ground` for one row (`m1_kernel.py` §7: every row carries `faults=(True,True,2,2)`, `allow_rebuttal=False`, the default proof register). The venue library (`modes.py:66-325`, ~260 lines) never reaches a proceeding because `proceeding_venue:567` builds `Venue(budget=budget, win=win, **o)` and `build_contest:133` passes no `**o`.

**Logic.** The resolution atom is consistent (`06` L6.7, re-read): `_reception` → the owner's ladder with a declared veto-only extension (`resolver.py:307-308`, `dice_engine.py:95-135`) → `_advance` → per-side accumulation → terminal. Its arithmetic produces its stated range everywhere I probed **except**: (i) the leverage staircase (§1.2 row 1) — the "continuous δσ" channel `resolver.py:289-296` argues for is quantized one line later; (ii) CR4's `+1D` composes with `PoolDesaturation` into a penalty above pool 9 (§0.4 row 3 — mean degree −0.053 at pool 13, −0.065 at 17; `overwhelm_bar(pool+1)` rises faster than one die's expected net); (iii) `draw` unreachable on every shipped bench (§1.2 row 2); (iv) `FaceScale.face_max(None)` raises through the public API (`06` L6.3 — `_as_contestant` never sets `charisma`, `wrapper.py:97-105`; not re-executed, read); (v) `Adjudicator.discipline` carries two meanings — leak resistance at `resolver.py:323` (bench **mean**, `contract.py:47`) and bench-weight at `:133` (per member, **summed**) — and every factory builds homogeneous members, so the ratified weighted rule equals a head count on every constructible bench (executed: 3,000/3,000). Points (i)–(v) are the R-COMPLETE findings.

**Coherency.** It *is* the kernel, so it fits the kernel's primitives by definition. It invents no parallel vocabulary except the one it exports: two winner vocabularies (§1.1 row 4) and two side-label cases (D15). Against the other three games it is the base they all compose on, and the three-lens verdict (`00` §2, `03` §2.3, `08` §6) that they are venue rows plus one terminal is confirmed by reading their §7.2 tables: inquiry adds one field and one write, consensus one aggregation branch, negotiation one pure function.

**NERS (§0.06).**
- **N, six directions.** Bottom-up: what the kernel computes reaches the campaign through one scalar (seam; `08` §1.4, inherited). Top-down: the game as designed needs a social contest (`CLAUDE.md` head). Vertical: one stat, one direction (seam). Lateral: it is the only personal-scale mechanism that executes at all (`08` §1.4). Diagonal: no reference to `ledger.py`, no `Person` (own grep of the package: zero `Key(`, zero `.emit(`). Through E/R/S: see below. **N NARROWED** — holds outright in one direction (lateral), narrowly in one (vertical), by default rather than merit. The cut that would show it *false* — a two-integer Bernoulli reproducing the production path in distribution — is `08` §8's argued leg, not re-run here.
- **R-COMPLETE: FAIL** — five arithmetic defects above, none of them at the atom.
- **R-VARIETY: real in tests, absent on the path.** Eleven policies span 0.6 in win rate at fair inputs (`06` FA5.2, inherited); six of seven move kinds are never issued by a production policy; the appeal choice is the largest lever and `ContestView` (`contract.py:53-66`) exposes neither the venue's proof weights nor the judge's character.
- **R-WORLD: FAIL, seam-dependent.** The unwatched drama is the emergency council recurring 45 seasons on one faction (`08` §4.2, inherited; seam-measured, out of scope to re-run). Inside the kernel: no record leaves a `Bout` (`resolver.py:239-270`; `Bout.log` consumed by nothing) — a contest that emits nothing durable cannot throw a hook.
- **R-CHOICE: NOT SCORABLE** at every seat — no seat exists (`resolve_contest` defaults both policies, `wrapper.py:248`; no `Person`). Bound, inherited: at the live input the best open-loop line buys 8 % against 6.5 % (`08` §4.1); at fair inputs one solved choice (+12 pts). Upper bounds.
- **S-UP / S-DOWN: FAIL** — no demand object, no person (seam; inherited, one line).
- **S, methodology: FAIL, inside the kernel.** Two draws for one quantity (discrete here, continuous in the faction layer — `SKILL.md` §11.3); two pool floors (5D here, 1D everywhere else); four bench aggregations (D13); two band-to-Degree methodologies for one Key type (seam; one line); the seventeen duplicates. **S, pauses correctly: PASS by construction inside the kernel** — a `Bout` is a pure function of its inputs and calls nothing that yields; the FAIL is at the seam (`08` §5.1) and out of scope.
- **E, last, as a ratio.** Denominator: 7,306 lines, ~100 named constants, four resolvers, a 25-row registry, two test suites, a harness — for an executing path that a two-integer table reproduces in distribution. Numerator: what N and R found surviving — a pure seed-reproducible atom, a structurally-bounded ladder seam (`degree_extension.py:60-82`), venue-configured defeat conditions (`primitives.py:262-279`), and a decision surface real only in tests. **E-OVERHEAD: FAIL** (62 % of the surface unreachable; three resolvers beside the one that runs). **E-LEGIBILITY: FAIL** — the player cannot intuit the outcome because the view withholds its causes and shows levers that do nothing (`can_hard` before a learned bench; `evidence_available` always 0 on the path). The one E property that survives the cut test is the ladder seam, and it is the one place the word STRUCTURAL is earned.

**Verdict: EXECUTES; internally consistent at the atom; incomplete at five edges; over-built by a factor of three around an atom of ~1,000 lines; and — the finding that matters for the rebuild — resolves ONE matter between TWO sides to ONE label, which is the wrong arity for every one of Jordan's four requirements (§3).**

### §2.2 Negotiation (`02_NEGOTIATION.md`) — paper

**Logic.** `settle(margin, floor_a, ceil_a)` (`02:308-327`) is six lines and its arithmetic holds: `split(−m) == 1 − split(m)` by construction (`:299-305`; verified by `08` on 101 points, and by reading — the two arms both return 0.50 at m = 0); the ZOPA clamp is monotone; `Refusal` is one kind. **Its band edges do not hold**: `SHARE_BY_DEGREE` is keyed by `degree_from_net(abs(margin), 0.0)` (`:304`), so the 0.50/0.55/0.60 boundaries fall at `|margin|` = 1 and 3 **in whatever unit `margin` arrives in** — the spine's `SUCCESS_UNIT`, an uncalibrated `[SEED]` (`01_SPINE.md:501-503`), and §1.2 row 3 shows the gap on the production proceeding has mean |1.8| and max 4.3 in `adv` units, so at `SUCCESS_UNIT = 1` almost every non-committee bout is a 0.55 and the 0.60 share is rare. The document says so honestly (`:282-286`). §5.4 replaces the unit with the band→Degree table and the edges become canon's. `floor_a` carrying two contradictory definitions (`05` F4) is inherited and not re-read. The `Grudge` on refusal has no `place` to be written at (`06` PR8.2, `08` §1.3) — inherited.

**Coherency.** Composes on `Bout`, `TallyAtClose`, `private_negotiation` (`modes.py:513-515`), `DefeatCatalogue`, the one ladder, `LedgerTag`; adds exactly one function and two return types; deletes `NegotiationMode` and a `GAMES` row. It fits the kernel and it fits inquiry (the abjuration composition, `00` §4(j)). **Where it does not fit is Jordan's requirement (4):** `settle` divides one stake between **two** parties along **one** axis (`terms: dict` was cut as a false N-line at `02:454`, correctly — the function has no per-axis input). A bundle of issues, a three-party stake, or a conditional concession is outside its type. The 2-party/1-axis restriction is inherited from `Bout` (`resolver.py:241`), not chosen by the branch.

**NERS.** N for `settle()` **holds** — attacked in `08` §9 and here by reading every terminal (`resolver.py:52-147`): none divides; `faction.py:117` divides side-asymmetrically for succession only. `SHARE_BY_DEGREE` holds (cut it and every settlement is 50/50). A's own `commit` Tenure survives on the breach-path N-line (`02:453`) — conditional on PR #362. **E moves the right way**: one module in, three names in, three objects out, seven candidates cut before writing (`02:463`). **R-COMPLETE: FAIL as designed for requirement (4)** and for the `[SEED]` band edges. **R-VARIETY:** the reservation is a genuine hidden-information bet — the branch's best property. **R-WORLD:** a `Refusal` that leaves a Grudge is a hook, if the Grudge had a home. **R-CHOICE: NOT SCORABLE** (no `Person`); the exploit table (`02:540-547`) is an upper bound and says so. **S:** binding-in-scene resolved by modelling the settlement as a `Record` (`01_SPINE.md` §3.4 (iii)), which PR #362's gate admits (`04_CODE_ARCHITECTURE.md:529-534`); the negotiation *terminal* pauses correctly by being a pure `Query`; the write path is the seam's.

**Verdict: the one genuinely new object in the programme, six lines, arithmetically sound, on the wrong arity. Keep `settle()`; generalise its inputs to a share vector when the fold lands (§5.6); replace `SUCCESS_UNIT` with the band table.**

### §2.3 Inquiry (`03_INQUIRY.md`) — paper

**Logic.** Its central mechanism is `ProofBar` (`resolver.py:67-73`) with `challenger=A`: the burden and the stall rule are already there (`:71-72`, `if closing: return df`). **Its central *addition* is a measured false N-line:** `restricted = {"B": ("support",)}` (`03:365-382`) exists to stop a "dominant defensive line" of `support`-forever; executed here, that line **loses 500/500** on `inquisition_hearing_venue` (ProofBar 2.5, budget 8) and yields `A_total` **500/500** on the reachable `church_tribunal` — because an accused who never advances contributes 0 to `adv[B]`, so the inquisitor clears any bar unopposed. Silence already convicts; the field guards a non-exploit. `yield_strikes=1` (`03:303-307`) guards `pass`, which loses at 2 strikes for the same reason. The remaining logic — the grounds check restored with two canon constants (`:331-363`), the Stay wired (`parliamentary_stay.py:54, :101`, zero callers), the finding write — is sound by reading, with two inherited blockers not re-read here: B2 (the `formal_grounds_check` rewrite regresses `systems/factions/sim/tribunal.py:102`'s only caller — FA lane) and B4 (`KeyLog.of_type` does not exist; `03:358` uses it).

**Coherency.** The branch's own §2.3 is right: *"a venue row plus a write. Anyone reading this document as licence to build an `inquiry.py` has misread it."* It fits the kernel (burden already lives inside two terminals; `is_pre_merits`, `rhetoric.py:172`, is the Stay), fits agôn (same `Bout`), and fits negotiation (the abjuration). It invents `burden`, `bar`, `restricted` — one of which is refuted. It merges `inquisition_hearing_venue` (`modes.py:181-198`) onto the canonical row — the right deletion.

**NERS.** N for `burden` as a selector **holds** (one field replacing `CHURCH_TRIBUNAL_TRACK_START`, `tracker`, `tracker_mode`, `_use_tracker`, `use_tracker` — `03:526`, three in, ten out); N for `restricted` **FALSE, measured**; N for the finding write **holds** — an institutional fact that binds whether or not a mind changed (`03:70-80`), the one new behaviour. **E: positive once `restricted` is cut** (2 in, 10 out). **R-COMPLETE: FAIL** on B2/B4 as written; the drama floor at bar venues is intrinsic (`03:637`, held for Jordan, not re-opened). **R-WORLD:** a case that runs 2–4 seasons with a Stay is exactly an unwatched hook — *if* it ran. **R-CHOICE: NOT SCORABLE**; the accused's only non-dominated line is *argue* (`08` row 1). **S:** the Stay is a band on a Query (`CI < 55`), not a stored flag — correct shape; *pauses correctly* is the Stay's whole content (a season sleeps) and it is designed, not run.

**Verdict: the smallest branch and the most honest about it. Adopt `burden` on the row and the finding write; drop `restricted` and the `yield_strikes` change; fix B2/B4 before any line lands.**

### §2.4 Consensus (`04_CONSENSUS.md`) — paper

**Logic.** Arithmetically inoperable as written, **re-executed**: `margin = assent_share − 1.0 ∈ [−1, 0]` (`04:267-268`) against fixed edges at 0/1/3 gives `Partial` at share 1.0 and `Failure` at every other share, at scales 1/2/5/10/100 (`m1_kernel.py` §6) — `Overwhelming` and `Success` are unreachable in every body and `UNANIMITY_MARGIN_SCALE` decides nothing. The antibody's three channels: channel 1 (`evasion_strikes`) fires only on an off-ground move (`resolver.py:380-381`), and ten of eleven shipped policies argue `v.live_ground` (`policy.py`, read in full); channel 2 (`cr5_self_backfire`, `rhetoric.py:413-454`) takes no armature and no alignment (signature read) — so "keyed to alignment" is not what it does; channel 3 (`Grudge`) writes on a degree the aggregation cannot produce. The recusal (`04:341`) guards `position_of`'s gate-off, which is a caller-set flag defaulting `False` (`armature.py:374-390`) — nothing detects a member who is also a contestant. **And a structural fact the branch composes over without naming:** `VoteAtClose` draws i.i.d. per juror (`resolver.py:139, :144`) with no per-member term, so "the named holdout" is named by draw order (`05` F3/F6, confirmed by reading). `Ballot(member_index=i)` (`04:254-258`) gives the draw an index, not the member a disposition.

**Coherency.** The slot exists: `panel_win_condition` names `unanimity_required` and returns a `StubResult` for it (`dictionaries.py:707-722`); the branch fills a declared alternative. It composes on `VoteAtClose`, `Panel`, `_default_panel`, `DefeatCatalogue`, `cr5_self_backfire` — no parallel resolver; it offers to delete two (`coalition_vote`, `run_contest`; `04:463-464`), correctly. It puts the venue in `INSTITUTIONAL_MODES`, not the canonical eight (`04:246`) — the right tier. Its refutation of the shape spec's antibody and its cut of `on_hung: lot` (`04:480-489`) are the strongest reasoning in the four branch documents. It invents `Ballot`, `BallotBook`, `holdout_rounds`, `on_hung`, `UNANIMITY_MARGIN_SCALE`, `FRIVOLITY_STRIKES`, `QUORUM_FRACTION` — five `[SEED]`s (`04:373-383`).

**NERS.** N for the `unanimity_required` branch **holds** — no tally expresses *no decision until all assent*; the Type-3 conflict class is unreachable without it. N for `Ballot` retention holds **only with a per-member term** (no producer of identity otherwise, `08` §1.3). `holdout_rounds`/`on_hung` are false N-lines by precedent (`08` §2 row 3: `queue_scene` + the chain cap; the existing weighted branch). **E: moves the wrong way as written** — five objects protecting no N. **R-COMPLETE: FAIL** (inoperable; and `draw`, a fourth label the branch inherits, is unreachable on its 7-member bench, §1.2 row 2). **R-WORLD:** the *liberum veto* reproduction (F-C2) is precisely an unwatched-drama hook — a bribed deputy blocking a body — and it is the falsifier that would make the branch worth building. **R-CHOICE: NOT SCORABLE.** **S:** the auto-arm/played-arm split (`04:356-371`) is the right shape and the parity number is a `[SEED]`.

**Verdict: the right slot, the wrong arithmetic, and no per-member term. Rebuild on `SUCCESS_UNIT`-free banding of the *assent share* (§5.4 gives the table) and a per-member disposition on `Adjudicator` before any antibody.**

---

## §3 · The cross-game verdict

**Four games or one game with four skins?** One game with four **terminals** — and that is the *correct* shape, not the defect. Every branch's own §7.2 table reduces to a venue row (inquiry: one field + one write; consensus: one aggregation branch), or a terminal (negotiation: one pure function), on the one `Bout`. The three-lens audit said it (`00` §0.1 `:334`), `00` §2 restated it, `08` §6 confirmed it, and each branch document concedes it in its own words. A rebuild that produces `negotiation.py`, `inquiry.py`, `consensus.py` has misread all four.

**Does the set cover the space a deliberative system needs?** The corpus's own frame is *crown a winner · strike a bargain · discern a truth · enact a unity* (`00` §0.1, the 2026-06-28 critique) and the four terminals map onto it one-to-one. **Against Jordan's four requirements (§0.3) it does not cover the space, and the gap is not a fifth terminal:**

| requirement | what the four games provide | the gap |
|---|---|---|
| (1) somewhat-okay odds; degrees and bands | the band ladder exists (`resolver.py:81-95`) and reads the room's magnitude; the production terminal discards it (§1.2 row 3: 0 % middle at 1v6 vs 29.5 %) | a *terminal* that returns a degree, on every proceeding — one table, §5.4 |
| (2) many lines of adjudication, a verdict each | none — every terminal returns **one** label for **one** matter (`resolver.py:52-147`); `settle` divides one stake | the **unit of resolution** — §5.1 |
| (3) a bundle of subtopics, with conditions | none — `Bout.live` is one stasis ground (`resolver.py:245`); `Move.ground` is a stasis, not a topic (`contract.py:14`); no object relates two matters | the fold and the edge — §5.2 |
| (4) both sides win; more than two sides; non-zero-sum | `settle()` (two parties, one axis); the bar-type terminals `ProofBar`/`GraceThreshold` are per-side and *can* both pass — executed: two `GraceThreshold`s on one state → both sides win (`m2_paired.py` F); but `Bout.c` is `{A, B}` by construction (`resolver.py:241`), `other()` is binary (`contract.py:8`), `DefeatCatalogue.check` iterates `(A, B)` (`primitives.py:273`) | **N sides is architecturally blocked at the `Bout`**, not merely unbuilt — §5.3 |

So: **one game, four terminals, one issue, two sides.** The four terminals are right and cheap; the arity is wrong and expensive. The rebuild's central move is therefore not among the three branches at all — it is the issue fold (§5), after which each of the three branches is a terminal *per issue*.

---

## §4 · The NERS verdict for the engine as a whole (§0.06), with what would overturn each

```
NERS PASS: systems/social_contest (kernel + four games)     INSTRUMENTS: A + B (B on the exchange roll and the ballot)

MUST BE STATED AS A LIMIT
  - "the armature is a continuous δσ channel"        — quantized to whole successes by the integer ladder edges at the live draw; exactly 0 at faculty 1 [§1.2 row 1; P-iii]
  - "CR4's +1D rewards the terrain-matched Style"     — a penalty above pool 9 under the ruled extension [§0.4 row 3; P-ii flat-shift trap]
  - "weighted_by_standing is the Panel's rule"        — equals a head count on every constructible bench; needs a heterogeneous bench to mean anything [§2.1 (v)]
  - "VoteAtClose can draw"                            — not on any shipped bench [§1.2 row 2]
  - "the eight proceedings are eight venues"          — four live fields; the venue library never arrives [§2.1]
  - "silence convicts needs `restricted`"             — silence already convicts; the field guards a non-exploit [§2.3]
  - "consensus grades distance from unity"            — margin ∈ [−1,0] bands Partial/Failure only [§2.4]
  - "the four games cover deliberation"               — one issue, two sides, one label; none of Jordan's four requirements is reachable [§3]
MAY BE CLAIMED, HAVING SURVIVED
  - the resolution atom is pure and seed-reproducible — attacked for hidden state: every mutable object traced to Bout.__init__ (resolver.py:239-270); only Reserve.cur is written around its owner (:362), latent
  - the ladder seam is STRUCTURAL by signature       — attacked for a promotion path: may_overwhelm returns a bool consulted in one branch (dice_engine.py:95-135); none
  - no side / first-mover bias                        — attacked: inherited 12,000 mirrors (06 FA5.5) and 4,000 (08 §9); my own 5v5 mirrors symmetric within noise (m1_kernel.py §9)
  - settle() is necessary                             — attacked against every terminal and faction.py:117; nothing ruled in divides a stake
  - the band ladder gives the weak side a middle      — measured 29.5 % committee at 1v6 on the same rolls the ballot resolves 93.4 % clean loss

| axis / test | verdict | what would overturn it |
|---|---|---|
| N (six directions) | **NARROWED** — lateral holds by default, vertical narrowly; diagonal/bottom-up nil (inherited seam measurements; the kernel emits nothing durable) | a consumer of Bout.log or of a Key with content; a production input where the decision surface is reached |
| E-OVERHEAD | **FINDINGS** — 62 % unreachable surface, four resolvers, 17 duplicates, a self-describing registry with two meanings of WIRED | evidence that a cut object's loss does NOT survive — e.g. a caller of `derive_interaction` or `coalition_vote` that a grep missed |
| E-LEGIBILITY | **FINDINGS** — ContestView hides the two causes of the outcome and shows two levers that do nothing on the path | a ContestView that carries venue role + adjudicator character, and a measured consult load |
| R-COMPLETE | **FINDINGS** — five kernel edges (§2.1), one per branch (§2.2–§2.4) | each fixed with a falsifier that fails before and passes after (Part 3) |
| R-VARIETY | **PASS in tests, FINDINGS on the path** — 0.6 policy spread at fair inputs; six of seven move kinds never issued | a reactive best-response sweep (ED-SC-0021's falsifier, still unrun) finding one line that answers everything |
| R-WORLD | **FAIL** — nothing durable leaves a Bout; the seam's hook recurs identically (inherited) | a Bout outcome that writes a Record a later scene reads |
| R-CHOICE | **NOT SCORABLE** — no seat; bounds are upper bounds (8 % at the live input) | a Person producer and a policy at the seam |
| S-UP | **FAIL** — no demand object carried by a person (seam; one line) | out of scope |
| S-DOWN | **FAIL** — no person with no post reads anything the kernel writes (nothing is written) | a durable write and a reader |
| S — methodology | **FAIL, in-kernel** — two draws, two pool floors, four bench aggregations, two winner vocabularies, 17 duplicates | one owner per quantity (Part 3 phase A) |
| S — pauses correctly | **PASS inside the kernel** (a pure function yields nothing) · FAIL at the seam (inherited, out of scope) | — |
| S — coverage | lateral carried; vertical one-way; diagonal uncarried | a `LedgerTag` written by a contest outcome |

REPAIRS (worst first; each a deletion or one object — Part 3 numbers them)
  1  the unit of resolution: issue, not contest — one fold function, shared side runtime            [W-D1..D3]
  2  the terminal reports a degree: one 5→4 table, zero constants                                    [W-C1..C2]
  3  the venue arrives: **o through proceeding_venue, one row key                                    [W-B1]
  4  the armature is reachable and value-keyed: positions tuple + armature=/rng= passthrough        [W-B2..B3]
  5  deletions: GAMES/_stub/game=, MECHANICS, coalition_vote/band_of, legacy stub bodies, harness,
     Resonance.effective/tension, the appraise ordinal, the duplicate panel construction            [W-A1..A8]
  6  single owners: bands, start, clamp, scale, RES_FLOOR, Reserve.refund                            [W-A2..A5]

GRADE: runs (agôn, one proceeding, defaulted policies) | paper (everything else, including every repair above)
```

---

# PART 2 — PLAN

## §5 · The shape question, decided by the meta-architecture's ownership rules rather than by taste

Jordan's four requirements (§0.3), read jointly, ask one question: **is the contest a container of sub-contests, or is the issue the unit and the contest a fold over issues?** PR #362 (`04_CODE_ARCHITECTURE.md`, PROPOSED, a shape constraint) answers it five times over, and every answer points the same way.

### §5.1 The issue is the unit; the contest is a fold

| rule | text | what it decides here |
|---|---|---|
| **T-i · No container gets a clock** | `01_AXIOMS.md:396-398`: *"a container that schedules itself has no caller"*; `04_CODE_ARCHITECTURE.md:121`: *"carriers have state and no behaviour"* | a `Contest` class with a loop over sub-contests is a container with a clock. The contest must be a **function**, not an object with behaviour |
| **§C.4 · the one fold** | `:575-586`: `acts = canonical_order(flatten(scenes)); for a in acts: … eval(row.requires, world_as_predecessors_left_it)` | the precedent for "many things resolved in a declared order, each seeing what the earlier ones did" is already the architecture's central loop. An issue fold is that shape one level down |
| **§G.2.9 · a procedure is required wherever order changes the outcome** | `:1205-1213` | conditions (§5.2) make order load-bearing — issue Y's outcome changes issue X's — so the fold must be an **ordered procedure with declared order**, never a map |
| **AX-4 · one owner, one writer** | `:115` | each issue's outcome has one owner: its terminal. The contest owns **only the order**. No contest-level "who won the contest" aggregation — that would be a second owner of nine facts |
| **T-k · one resolver, one ladder** | `:122` | per-issue margins go through the one ladder (§5.4). A contest-level score summing verdicts into a winner would be a second ladder for a quantity nobody owns |
| **§C.5 · the seam returns a Margin, never a winner** | `:683, :692` | the contest's return is a **vector of per-issue outcomes**, each carrying a margin and a degree; "won on one, partially lost three, lost five" is that vector read out, not a summary of it |

**Decision: the unit of resolution is the issue — a contested Proposition (`§B.6`, `:263-267`) — resolved by one `Bout` on its own venue and terminal; the contest is `resolve_issues(issues, sides, …)`, an ordered fold that builds the participants' side runtime ONCE and shares it across every issue.** The shared runtime is the only thing that makes it one *contest* rather than nine: Reserve, Standing, Room and FaultState persist across issues (`_Side`, `resolver.py:197-236`), so exhausting yourself on issue two costs you on issue seven, and a fault on issue one cascades — **executed, zero new rules** (`m2_paired.py` E: a `barred` fault carried into a second `Bout` clinches it at move 1, because `DefeatCatalogue.check` runs after every move, `resolver.py:457`). That cascade is Jordan's "lose completely on five" falling out of shared state, and it is a design default rather than a rule — a venue may reset faults per issue if he wants it otherwise (§8 E6).

**Rejected, with the reason:** (a) a per-issue key inside one `Bout` (`ContestState.adv[issue][side]`, `Move.issue`, `Bout.live[issue]`) — touches every terminal's signature, every policy and `ContestView`, and makes the `Bout` a container of issues with one loop, which is T-i's failure; (b) a `Contest` class holding sub-`Bout`s with its own `resolve` — the same failure with a name; (c) resolving every issue off one shared momentum (nine bands read from one `adv`) — the per-issue vector is then perfectly correlated and carries **no texture** (§5.4).

### §5.2 Conditions — an act whose content is an edge, evaluated by the fold

*"I concede X if you grant Y."* Three candidate homes; the architecture picks by asking what each thing is:

- It is **authored by an act** — an utterance by a person (AX-1; `utter`, `verb_table.yaml:475` per `00` §2.3). The kernel does not author it; the seam's caller does, upstream of `resolve_issues`. So it is not a kernel object with a producer inside the kernel.
- Its **content is an edge** — it names two issues and a direction. It is never a property of one issue alone, because it references another.
- It is **evaluated by the fold** — in declared order, against `out[depends_on]`, exactly as `§C.4` evaluates `requires` against `world_as_predecessors_left_it`. An issue whose condition names a later issue is a declared-order violation and refuses loudly (`KeyError`), which is `§G.2.9`'s point: if the order matters, the order is the mechanism and must be declared.

**Representation (the smallest that carries it):** one optional tuple on the dependent issue — `condition = (depends_on: str, when_winner: side, effect: "concede" | "withdraw")`. *If issue Y resolved for `when_winner`, then this issue is conceded to the other side without a bout (`effect="concede"`), or dropped (`effect="withdraw"`).* Both effects reduce to what already exists: a conceded issue is an outcome with `winner = other(when_winner)`, `degree = SUCCESS` (the counterparty's stated ask, granted — not more), `reason = "conceded:<Y>"`; a withdrawn issue is an outcome with `winner = None`, `degree = None`, `reason = "withdrawn:<Y>"`. **No new class, no store, no clock; one tuple field and two branches in the fold.** A bar-shift effect (a concession that moves a bar-type terminal's bar rather than settling the issue) is expressible on the same tuple later and is deliberately not shipped — nothing in the four requirements needs it.

### §5.3 N sides and non-zero-sum — a property of the terminal, not of the game

Zero-sum-ness is not something a game has; it is something a **terminal** has. Read off `resolver.py:52-147`: the **compare-type** terminals (`ThresholdRace`, `TallyAtClose`, `PersuasionTrack`, `VoteAtClose`) compare two accumulations and are zero-sum by construction; the **bar-type** terminals (`ProofBar`, `GraceThreshold`) measure one side against a bar and are not — executed, two `GraceThreshold`s on one state let **both sides win** (`m2_paired.py` F). `settle()` is a third kind: a **division**. So "both sides can win" is already in the kernel; what is not is *a bout with more than two sides*, and that is blocked at `resolver.py:241` (`self.c = {A: …, B: …}`), `contract.py:8 other()`, `primitives.py:234 Room`, `:273 DefeatCatalogue.check`, `resolver.py:443` (`for side in (A, B)`), and every terminal's `s.adv[A]`/`s.adv[B]`.

**Decision:** the contest has **participants**; each issue names its **sides** (`Issue.sides`, default `(A, B)`). A compare-type terminal names exactly two of them (a three-party bargain decomposes into pairwise issues plus one division issue — which is how bargains are actually written); a bar-type terminal takes any subset; a division terminal takes all of them and returns a share **vector**. `Bout` is generalised from `(A, B)` to an ordered `sides` tuple with a **byte-identical two-sided default**, so the 389-check suite and both goldens are the control. This is phase E, after the fold, because two-sided issues in an N-participant bundle already carry most of requirement (4); the N-sided *issue* is needed only for a shared stake and a many-orator hearing.

### §5.4 The bands — the answer to requirement (1), and what it costs to make them reachable

**What exists.** `PersuasionTrack.track` = `start + scale·(adv[A] − adv[B])` (`resolver.py:87`), banded at 9/7/3/1 (`:91-95`) — canon (`social_contest_v30.md:279`). It is the terminal on four of eight proceedings and on **none** of the production path (`guild_arbitration` → `VoteAtClose`, ED-1059). Measured (§1.2 row 3): on the same rolls, at 1v6 the ballot gives the weak side 0 % middle and the band gives it 29.5 %.

**What it costs — three edits, one of them a deletion.**
1. **One owner for the track.** Hoist `track_of(gap)`, `band_of_track(t)`, the four band constants and the start/scale to module level in `resolver.py`; `PersuasionTrack` reads them; `contest_legacy_stub.py:67-71`, `modes.py:475`, `faction.py:142`, `parliamentary_vote.py:100` import them. This is D1/D2/D5 closed — a deletion of four homes.
2. **A five-to-four table, zero constants** — `A_total → (A, OVERWHELMING)`, `A_decisive → (A, SUCCESS)`, `committee → (None, PARTIAL)`, `B_decisive → (B, SUCCESS)`, `B_total → (B, OVERWHELMING)`. The precedent is `engine/cross_scale/parliamentary_bridge.py _winner_and_degree` (`m2_paired.py` G): *"READS THE VERDICT, DOES NOT RE-DERIVE IT"*, exhaustively tested. **Not `SUCCESS_UNIT`:** the spine's A3 (`01_SPINE.md:501-503`) divides an `adv`-unit margin by an uncalibrated `[SEED]` so that `degree_from_net` can re-band it — six constants for a job a table does (`08` §2 row 2), and measured here it *cannot* reproduce the middle: `degree_from_net(gap, 0)` at 1v6 is Partial 3.8 % because the owner's Partial window is one success-unit wide, while canon's `committee` is `|gap| < 1.33` and gives 29.5 %. The width of the middle is canon's, not a constant to fit.
3. **Every terminal reports `(winner, degree)`.** `WinCondition.outcome()` = its own `resolve()` for the winner plus `degree_of_margin(self.margin(s))` for the degree, where `degree_of_margin` is the band table on `track_of(margin)`. `VoteAtClose` keeps its **ratified ballot** for the winner (ED-1057, untouched) and reads its degree off the room's track — which is precisely ED-1057's own two-quantity design (*"the Persuasion-Track advancement is the room's MOMENTUM… the VERDICT is a SEPARATE terminal secret ballot"*), finally reported as two fields. **Methodology becomes consistent**: one band function for one quantity across all six terminals, and the output vocabulary is the owner's four Degrees.

**Texture versus noise, measured (`m2_paired.py` D).** Per-issue banding multiplies texture only if issues accumulate **independently** (their own `Bout`, shared runtime): then a nine-issue bundle at 1v6 expects 0.0 wins / 2.7 committees / 6.3 losses (P(≥1 win) = 0.4 %); at 1v4, 0.1 / 3.7 / 5.3 (6.6 %); at 3v4, 0.5 / 6.7 / 1.8 (37 %); at 4v4, 0.7 / 7.6 / 0.7 (54 %). Each component is exactly as noisy as a single verdict; the *count* concentrates. Jordan's "win one, partially lose three, lose completely on five" needs a per-issue mix near 0.11 / 0.33 / 0.56, which no faculty pair above gives — the 3v4 row is committee-heavy. **The dials are `MERIT_SCALE` (`resolver.py:39`) and `TRACK_SCALE` (`:86`), both `[SEED]`, and the band edges, which are canon.** That is Jordan's tuning (§8 E4), and the instrument for it is the D table re-run after the fold lands. If issues share one momentum instead, the vector is perfectly correlated and there is no texture at all — which is why §5.1 rejects option (c).

### §5.5 Does a per-issue outcome vector satisfy all four requirements at once?

| requirement | carried by | verdict |
|---|---|---|
| (1) odds / degrees | `ContestOutcome.degree` per issue, read from the band table; `committee` → `PARTIAL` reachable on every terminal | **yes**, at the measured rates; the *mix* is Jordan's tuning |
| (2) many verdicts | `resolve_issues` → `{issue_key: ContestOutcome}` | **yes** |
| (3) bundle + conditions | the fold in declared order; `Issue.condition` | **yes** for concede/withdraw; a bar-shift is expressible later on the same tuple |
| (4) both win / N sides / non-zero-sum | bar-type and division terminals per issue; `Issue.sides`; the N-sided `Bout` (phase E) | **yes for "both win" today; N sides after phase E**; compare-type terminals stay two-sided by declaration |

**It does, with one stated limit:** the vector carries no *contest-level* verdict, deliberately (AX-4, T-k). A consumer that wants "did A win the negotiation" must read the vector — which is the consumer's degree-keyed column (`§C.4 F6`, `:606-617`), per issue, never a sum minted here.

### §5.6 What this does to the three unbuilt terminals

- **Negotiation:** `settle()` becomes the division terminal for a division issue; its inputs generalise from `(margin, floor_a, ceil_a)` to a share vector and a reservation per participant when phase E lands; until then it ships two-sided as `02` §5.3 writes it, with `SHARE_BY_DEGREE` keyed on the band table rather than `SUCCESS_UNIT`. The ZOPA over a *bundle* is the fold plus conditions — "I concede X if you grant Y" is no longer a modelling problem.
- **Inquiry:** `burden: ACCUSER` on the `church_tribunal` row selecting `ProofBar`; the finding write; `restricted` dropped (§2.3). A multi-charge tribunal is a bundle of issues, one per charge, each with its own `ProofBar` — "guilty on one, inconclusive on three, acquitted on five" is requirement (2) in the inquiry's own vocabulary.
- **Consensus:** the `unanimity_required` branch on `VoteAtClose`, with a per-member disposition field on `Adjudicator` (the one addition `05` §2 and `08` §1.3 both name as necessary) so a holdout is a member rather than a draw index; a multi-clause motion is a bundle of issues with per-clause ballots.

### §5.7 NERS on the requirements themselves — the smallest structure, and its N-line

The meta-rule (`14_NERS.md:31`: *a fix that adds a system has failed*) applied to the requirements: **most of it is composition.** Bands: exist (`resolver.py:87-95`). Both-win: exists (bar-type terminals). Conditions: the `§C.4` fold shape plus one tuple. Per-issue verdicts: one `Bout` per issue, which exists. Shared stamina across issues: `_Side` exists; sharing it is one constructor parameter. What is genuinely new: **`Issue` (one frozen dataclass, five fields) and `resolve_issues` (one function, ~25 lines)**, and — in phase E — the generalisation of a hard-coded pair to a tuple, which is the *deletion* of a special case. `derive_interaction` and `INTERACTIONS_TABLE` (`dictionaries.py:283-323`) are **not** reached for: they describe a head-to-head compare model the live kernel does not run (§1.1 row 3), and composing on them would mean choosing that fork first (§8 E1).

**The N-line, stated so it can be cut:** *`Issue` + `resolve_issues` — cut them and the game can no longer resolve a bundle of matters between the same parties in one sitting with one stamina, one bench and cross-matter conditions; every multi-matter dispute must be serialised into unrelated single-matter contests in different scenes, which cannot express "I concede X if you grant Y" at all and cannot express "won one, partially lost three" except as nine unrelated events.* Attacked: can `queue_scene` chaining (`social_contest_v30.md:368-383`, cap 3) carry it? No — chained scenes share no runtime, carry no condition, and are capped at three. Can one `Bout` with nine exchanges carry it? No — one `adv` per side, one terminal, one label. **N holds, in the lateral and vertical directions** (a bundle is a same-scale object; its per-issue degrees are what the degree-keyed column upstream consumes).

**Vocabulary count for the whole plan** (§7 tallies per phase): **deleted** — `GAMES`, `_stub`, `game=`, `Contest.game`, three `MECHANICS` stub rows and then `MECHANICS`/`_SYMBOLS`/`_resolve`/`mechanics_selftest` (the stage-3 check moves into the kernel suite), `Resonance.effective`, `Resonance.tension`, `coalition_vote`, `coalition_rate`, `band_of`, `rate_banded`, `run_contest`, `resolve_exchange`, `build_argue_pool`, `ExchangeResult`, `ContestResult`, `CONCENTRATION_MULTIPLIER`, `agon_harness.py`, `APPRAISE_FAILURE..OVERWHELMING`, `CANONICAL_TRACK_START`, `PERSUASION_TRACK_START_DEFAULT`, the second panel construction, `NegotiationMode`, `_use_tracker`/`tracker`/`tracker_mode`/`use_tracker`, `CHURCH_TRIBUNAL_TRACK_START`, `inquisition_hearing_venue` (**31 names**); **added** — `Issue`, `resolve_issues`, `ContestOutcome`, `WinCondition.margin`/`outcome`, `track_of`, `band_of_track`, `degree_of_margin`, `BAND_TO_OUTCOME`, `Reserve.refund`, `Adjudicator.disposition`, `Issue.condition`, `settle`/`Settlement`/`Refusal`, `burden`, `bar` (**17 names**). The vocabulary gets shorter by fourteen, and the largest single move is a deletion (the legacy stub and the registry).

---

## §6 · Where PR #362's shape and the live kernel conflict, and where compliance must wait

PR #362 is **PROPOSED and unratified** (`04_CODE_ARCHITECTURE.md:3`); nothing below treats it as canon (`CLAUDE.md` §0.05). Two kinds of item: conflicts a kernel-local change can honour now, and compliance that cannot be built until ratification.

| PR #362 clause | the live kernel | disposition |
|---|---|---|
| §C.5 `:692` *"a subsystem returning a winner has not met the contract"* | `Bout.resolve` returns a label (`resolver.py:466`) | **honoured by phase C** — `ContestOutcome` carries `margin` and `degree`; `winner` and `band` stay as legibility fields with a **deletion date**: the commit in which the rebuilt seam reads `degree`. Keeping them past that date breaks the contract (`01_SPINE.md` §3.4 (i)); the dated comment is the guard, not a test |
| §C.5 `:696` `veto : bool` | a clinch names the faulting side (`resolver.py:457-461`); the leader can be the faulter | **departure accepted** — `veto: side \| None` (`01_SPINE.md` §1.4 A). Feedback owed to `:696`: *where the seam has no single actor, the veto names the vetoed party* |
| §C.5 `:695` `claimants : PersonId[]` — a faction as combatant is STRUCTURAL | `_as_contestant` coerces ints (`wrapper.py:91-107`); the seam passes `round(L)` | **waits on ratification** — no `Person` type exists in `engine/` or `systems/` (`01_SPINE.md` A10). Until then `_as_contestant` stays; the refusal adapter is written the day `PersonId` exists |
| §C.5.1 sides resolved ONCE and held | `Bout.__init__` builds sides once and never re-reads the world (`resolver.py:239-270`) | **already compliant inside the kernel**; the fold builds the runtime once (§5.1) |
| §C.4 the fold; D-49 *no Act resolves inside another's resolution* | the issue fold is a loop inside `seam.contest`'s provider | **no conflict, stated so it is not re-derived**: issues are not Acts; the fold is the provider's procedure under §G.2.9, and `max_depth` (`:681`) bounds nested *contests*, which an issue is not. One note owed: §C.5 could say a provider may be a procedure over issues |
| §C.2 the write gate, `Receipt`, `NoOpReceipt` | the kernel writes nothing persistent (`10_` §1.10 re-verified; the fold writes nothing — conceded/withdrawn issues are outcomes, not writes) | **compliant by vacuity**; the writes are the calling verb's, degree-keyed per issue (`§C.4 F6`). Waits on ratification for the gate itself |
| T-k one ladder | `degree_from_net` is the ladder; the Persuasion bands are a *different quantity* (a track position) with a 5→4 table into the ladder's vocabulary | **compliant after phase C**; the table mints no constant. The `2·Ob` ladder in `combat_engine_v1` is a declared HELD exception and not this plan's |
| T-l / AX-1 a cohort is a Person at weight; only a person acts | `Contestant.faculty` is an int | **waits** (same as `PersonId`) |
| `§B.6` `Proposition` | `Issue.key` is a string | `Issue.key` becomes a `PropositionId` on ratification; a string is the value-identical stand-in |
| §A.2 `seam/wrappers/*` *"nothing, ever"* (no token) | `run_parliamentary_vote` writes `Faction.L` from inside the package (`parliamentary_vote.py:214`) | **a faction-scale entry point, not the kernel** — CONVENTION-graded by PR #362 itself; left to the FA/seam rebuild, one line |

**Where compliance must wait:** everything that needs `PersonId`, `Act`, `Receipt`, the gate, or the roster. **Where it need not:** the fold, the per-issue vector, the band table, conditions, N sides, and every deletion — all kernel-local, all buildable against the tree as it is, all value-identical for agôn by construction until phase G.

---

## §7 · The sequence — seven phases, each naming what it unblocks and the artifact that makes it done (`CLAUDE.md` §0.2)

Every phase before G is **value-identical for agôn**: the control is the two campaign goldens (`engine/tests/test_mc_v18_regression.py:142-150`, `test_f7_smoke_oracle.py`) **unchanged**, plus `engine/tests/test_contest_kernel.py` green at a `_KERNEL_EXPECTED` re-pinned by exactly the checks deleted or added, with the `RESULT:` line quoted in the commit. A phase that moves a golden before G has changed agôn and is a regression regardless of the reasoning.

| phase | what | unblocks | done when (execution artifact) | control |
|---|---|---|---|---|
| **A · deletions and single owners** (W-A1..A8) | dead code out; one owner for the bands/start/scale/clamp/floor; `Reserve.refund`; the appraise ordinal read from the owner; the second panel construction gone; `GAMES`/`MECHANICS` gone, the stage-3 check kept in the suite | every later phase reads one constant instead of five; the count pin stops being a trap | kernel suite green at the new pin; `python -c "from systems.social_contest.sim.contest import resolver; assert not hasattr(resolver, 'run')"` style probes in the commit message; both goldens byte-unchanged | goldens; the pin arithmetic stated per item |
| **B · reachability** (W-B1..B3) | `**o`/venue key through `proceeding_venue`; `armature=`/`rng=` through `build_contest`; positions as a tuple aligned with the bench | the venue library, the armature and same-seed reproducibility reach the seam; consensus's antibody and inquiry's CR4 have a carrier | F-S5/F-S6/F-S7 (`01_SPINE.md` §7.2) executing green; `ArmatureConfig` constructed **before** `build_contest` moves a track | goldens (defaults `None` / no override are byte-identical) |
| **C · the outcome shape** (W-C1..C2) | `ContestOutcome`; the band table; `WinCondition.margin()`/`outcome()`; `narrative.classify` on the new shape | every consumer reads a degree; requirement (1) reachable on every terminal | F-S1..F-S4 green; the paired table (§1.2 row 3) reproduced from `ContestOutcome.degree` — 1v6 `PARTIAL` ≈ 0.30 | goldens (`resolve_contest` still returns the tuple); `band` verbatim |
| **D · the fold** (W-D1..D3) | `Bout(sides=…)` shared runtime; `Issue`; `resolve_issues`; conditions | requirements (2) and (3); the three terminals become per-issue terminals | a seeded nine-issue bundle through `resolve_issues` printing the vector and its counts; the cascade test; the concede/withdraw test; `assert checked == 9` | goldens (the seam still resolves one issue); the vector's per-issue distribution equals the single-issue distribution at the same inputs (a two-arm check) |
| **E · N sides** (W-E1) | `Bout` over a `sides` tuple; per-issue sides; a three-orator bar issue; `settle` on a share vector | requirement (4) in full | a three-party bundle resolving with a division issue whose shares sum to 1; a two-sided run byte-identical to phase D | goldens; the 389-descendant pin unchanged for two sides |
| **F · the three terminals** (W-F1..F3) | `settle()` on the band table; `church_tribunal` → `burden`/`ProofBar`; `unanimity_required` + `Adjudicator.disposition` | the three games run as venue rows | F-N1/F-N2/F-N4 (`00` §3(i)) green; F-I1/F-I3/F-I5 green; F-C1/F-C2 green with F-C2 printing P(block) rising with N; `_kernel_tests` stub checks deleted | goldens (`church_tribunal` and the consensus venue are not on the production path); the `guild_arbitration` bench untouched |
| **G · Jordan's decisions, defaults shipped** (W-G1..G3) | the continuous draw; a venue preset per proceeding row; the interaction table out of code | the S methodology defects that require a re-pin | **the goldens MOVE, deliberately**, re-pinned in one commit with the before/after table in the message and `tools/balance_oracle.py` run once (240 campaigns) | the re-pin is the control; nothing lands in G without Jordan's word on each item |

**Order inside a phase** is the order of the work items in Part 3. **Phases A–D are the milestone**; E–G are sequenced after because each depends on D's shape and G moves goldens.

---

## §8 · What this plan does not do, and the six decisions that are genuinely Jordan's

**Not done here:** the seam (`scene_dispatch`, `echo_transport`, `parliamentary_bridge`) — every reachability gain above stops at `build_contest`/`resolve_issues` and waits for the rebuilt seam to call them; `formal_grounds_check` (FA lane, `systems/factions/sim/tribunal.py`) — inquiry's B2 fix is owed there and is named, not prescribed; a `Person` producer; the write gate; any change to the `2·Ob` combat ladder; any tuning number.

**The six escalations that survive `CLAUDE.md` §0's five tests, each with the architecture-conformant default shipped so nothing blocks:**

| # | decision | why it is Jordan's (two defensible options, materially different games) | default shipped |
|---|---|---|---|
| **E1** | **the interaction model** — independent per-side accumulation (the live kernel, `resolver.py:341-438`) vs head-to-head comparison with margin − resistance (canon `social_contest_v30.md:182-210`, the typed table `dictionaries.py:283-323`, and the dead stub `contest_legacy_stub.py:132-190`) | the first is a race; the second is a duel with attrition. Different games. Neither prose nor precedent decides — the goldens pin the first, canon describes the second | **keep the accumulation model** (it runs; a compare model needs a strain carrier nothing holds); delete the compare table from *code* and keep it as prose reference (W-G3) |
| **E2** | **the draw** — discrete `roll_pool` (the kernel today) vs `roll_net_continuous` (*"canonical for Godot"*, `sigma_leverage.py:299-303`; *"d10 everywhere, fractional"*) | switching un-quantizes the leverage channel (§1.2 row 1) and moves every seeded expectation; at pool 5 the two draws differ by 10 pp on P(net ≥ 2) | **continuous**, bundled with G's re-pin (W-G1) |
| **E3** | **which venue preset each of the eight proceedings re-skins** — today all eight inherit `Venue`'s defaults | eight design assignments; the docstrings name candidates (`inquisition_hearing_venue` for `church_tribunal`, `secret_council_venue`'s bench for `guild_arbitration`) but a table is content, not architecture | a `venue:` key on each row defaulting to `None` (= today), plus a proposed table marked `[SEED]` (W-G2) |
| **E4** | **the win / partial / lose mix** for "somewhat okay odds" — `MERIT_SCALE` 2.6, `TRACK_SCALE` 1.5, `JITTER` | tuning; the D table is the instrument | leave the values; re-run `m2_paired.py` D after phase D and hand Jordan the table |
| **E5** | **N-sided compare terminals** — may a `PersuasionTrack` have three poles? | a three-pole track is a new object; pairwise issues plus a division cover the cases named | compare-type terminals declare exactly two sides; N-sided issues use bar/division terminals (W-E1) |
| **E6** | **fault cascade across issues** — a clinch on issue k ends the sitting (emergent, §5.1) or resets per issue | Nyāya's *nigrahasthāna* defeats the disputant; a modern hearing continues | cascade (zero rules); a venue may declare `faults_reset_per_issue=True` later — not shipped |

Everything else in this document closes at rungs 1–5: the `restricted` field (rung 5, measured); `SUCCESS_UNIT` (rung 4, precedent); `holdout_rounds`/`on_hung` (rung 4); ED-SC-0020 (rung 4/5 — `01_SPINE.md` §1.5 already states the closure; the row should be marked resolved citing it); ED-SC-0015 (rung 4 per `00` §5(k)1, *closable, not closed* until `ledger_sweep` has a caller — seam); the CR4 die's sign (rung 5 — it is a measured defect of the composition with `PoolDesaturation`, fixed by making the die enter as δσ rather than as a pool die, W-B2's residual).

---

# PART 3 — INSTRUCTIONS FOR OPUS 5

**This section is executable without the author.** Twenty-three work items in seven phases; do them in order. Each names the file, the current state (with the line I read), the target state, the exact signature or shape, the falsifier that **fails before and passes after** (`CLAUDE.md` §0.1 pt 3), the control, and the blast radius. Every invented number is marked `[SEED]`. Where a decision is Jordan's the item ships the architecture-conformant default and says so.

## §9 · Ground rules for every item

1. **Branch from `main`; one commit per phase, or per item where the item re-pins the kernel count.** Format `[design]` for A–C (deletions, shape), `[simulation]` for D–F, `[fix]` for G; cite `ED-SC-0031/0032` where the ladder seam is touched and `ED-1057/1059` where the panel is.
2. **The control is stated per phase in §7 and is not optional.** Before G: `python -m pytest engine/tests/test_mc_v18_regression.py engine/tests/test_f7_smoke_oracle.py -q` **unchanged**, and `python -m pytest engine/tests/test_contest_kernel.py -q` green. Quote the `RESULT: N passed, 0 failed` line in the commit message every time `_KERNEL_EXPECTED` (`engine/tests/test_contest_kernel.py:93`) moves, with the arithmetic (which checks were deleted, which added). A golden that moves before G means the item changed agôn — stop and find out why.
3. **No seam edits.** `engine/cross_scale/*` is not touched by any item. Where an item's benefit is only reachable through the seam, the item stops at `build_contest`/`resolve_issues` and says so in its docstring.
4. **No new test files except one**: `engine/tests/test_contest_issues.py` (phase D onward) — the fold, conditions and N sides are load-bearing on the game (`CLAUDE.md` §0.1 pt 5). Everything else lands as `ck()` lines in `_kernel_tests.py` (1-for-1 rewrites where a pinned expectation changes) or as a probe quoted in the commit message. **Mint no guard for apparatus.**
5. **Deletions first within a phase.** Every deletion greps for callers across `systems/ engine/ tools/ tests/` before it lands and lists the hits in the commit; a hit in a docstring is not a caller.
6. **`[SEED]` on every invented number, in the code, at the literal.** Cite nothing to `params/contest.md` (97 dangling citations already; the file does not exist — `find . -iname contest.md` → nothing).
7. **Do not touch:** `resolver.py:98-147 VoteAtClose`'s ballot rule (ED-1057, ratified — W-F3 *adds* a branch and a per-member term, it does not alter `weighted_by_standing`); `degree_extension.py`'s veto-only seam (ED-SC-0032); `engine/autoload/*`.

---

## §10 · The work items

### PHASE A — deletions and single owners (value-identical for agôn)

**W-A1 · Delete `Resonance.effective` and `Resonance.tension`.**
- File: `systems/social_contest/sim/contest/primitives.py:246-251`; export at `contest/__init__.py:58` (`Resonance` stays exported; the two methods go).
- Current: `effective` computes `(1−leak)·role + leak·char` with no `joint_weight` and no `RES_FLOOR`; the live rule is `resolver.py:325-326`. Executed: 0.372 vs 0.420 on identical inputs. Zero callers.
- Target: `Resonance` carries `ETHOS_UNLOCK`, `LEAK_CAP`, `leak()` only. The reception rule lives once, at `resolver.py:_advance`.
- Falsifier: `grep -rn "Resonance.effective\|\.tension(" systems engine tools tests --include=*.py` → zero hits after; before, the two defs exist and disagree with the resolver. If any `ck()` in `_kernel_tests.py` reads them, rewrite it 1-for-1 against `Bout._advance`'s `res` (record the count delta).
- Control: goldens unchanged (nothing on the path calls them). Blast radius: `primitives.py`, `__init__.py`, possibly `_kernel_tests.py`.

**W-A2 · One owner for the Persuasion track: bands, start, scale.**
- Files: `resolver.py:81-95` (`PersuasionTrack`), `contest_legacy_stub.py:66-71`, `modes.py:475`, `faction.py:87,96,142`, `parliamentary_vote.py:44-51,:100`.
- Current: five homes for the neutral start `5` (§1.1 D2), two for the bands 9/7/3/1 (D1), three for the scale (D5).
- Target, in `resolver.py` at module level, above `PersuasionTrack`:
  ```python
  TRACK_START = 5.0              # neutral start — social_contest_v30.md:279 (was modes.CANONICAL_TRACK_START, stub PERSUASION_TRACK_START_DEFAULT, faction 5.0, parliamentary_vote 5)
  TRACK_SCALE = 1.5              # [SEED] adv -> track; was PersuasionTrack(scale=1.5) and faction.succession(scale=1.5)
  TRACK_LO, TRACK_HI = 0.0, 10.0
  BAND_TOTAL, BAND_DECISIVE, BAND_LOSS, BAND_DEFEAT = 9.0, 7.0, 3.0, 1.0   # social_contest_v30.md:279,:302
  # Public aliases so parliamentary_vote.py:44-51 and the package re-export keep their names:
  PERSUASION_WIN_THRESHOLD, PERSUASION_LOSS_THRESHOLD = int(BAND_DECISIVE), int(BAND_LOSS)
  PERSUASION_TOTAL_VICTORY, PERSUASION_TOTAL_DEFEAT = int(BAND_TOTAL), int(BAND_DEFEAT)
  PERSUASION_TRACK_START_DEFAULT = int(TRACK_START)
  def track_of(gap: float, start: float = TRACK_START, scale: float = TRACK_SCALE) -> float:
      return max(TRACK_LO, min(TRACK_HI, start + scale * gap))
  def band_of_track(t: float) -> str:
      if t >= BAND_TOTAL:    return "A_total"
      if t >= BAND_DECISIVE: return "A_decisive"
      if t >  BAND_LOSS:     return "committee"
      if t >  BAND_DEFEAT:   return "B_decisive"
      return "B_total"
  ```
  `PersuasionTrack.__init__(self, scale=TRACK_SCALE, start=TRACK_START)`; `track()` → `track_of(s.adv[A]-s.adv[B], self.start, self.scale)`; `resolve()` → `band_of_track(self.track(s))`. `modes.py:475` → `from .resolver import TRACK_START as CANONICAL_TRACK_START` (keep the alias one release; delete in W-F2). `contest/__init__.py:35-50` re-exports the five `PERSUASION_*` names **from `.resolver`**. `parliamentary_vote.py:100` → `starting_track: int = PERSUASION_TRACK_START_DEFAULT`. `faction.py:87` default → `TRACK_SCALE`; `:142` goes with W-A3.
- Falsifier: `python -c "import re,pathlib; t=pathlib.Path('systems/social_contest/sim/contest/resolver.py').read_text(); assert t.count('>= 9')+t.count('>= 7')+t.count('> 3')+t.count('> 1') == 0"` — the literals are gone from `resolve()`; and `PersuasionTrack().resolve(state)` equals its pre-change output on a 200-state seeded sweep (a 1-for-1 `ck`). Fails before (literals present), passes after.
- Control: goldens; kernel count unchanged. Blast radius: five files, all in the package.

**W-A3 · Delete the fourth resolver and the fourth band rule.**
- File: `faction.py:67-82` (`band_of`, `rate_banded`), `:127-154` (`coalition_vote`, `coalition_rate`), and `RESIST_DAMP` at `:28`.
- Current: `coalition_vote` hand-builds `ContestState`, calls `roll_net` per side and `PersuasionTrack.resolve` with no loop (`:143-146`); `band_of` bands a *vote share* ± 0.06 (`:68-74`); zero production callers (own grep — `:153` and `:123` are self-calls).
- Target: gone. `succession`/`succession_rate` stay until W-F1.
- Falsifier: `_kernel_tests.py` checks that call them (grep `coalition_vote\|band_of\|rate_banded`) are **deleted, not skipped**; `_KERNEL_EXPECTED` moves by exactly that count, stated. Fails before (the symbols import), passes after (`AttributeError`).
- Control: goldens. Blast radius: `faction.py`, `_kernel_tests.py`, `test_contest_kernel.py:93`.

**W-A4 · Delete the legacy stub.**
- File: `systems/social_contest/sim/contest_legacy_stub.py` (268 lines); `contest/__init__.py:35-50` and the `__all__` block; the `__init__` docstring's "BACK-COMPAT SHIM" paragraph (`:19-30`, which names a caller path `sim/cross_scale/scene_dispatch.py:105` that does not exist).
- Current: `build_argue_pool`/`resolve_exchange`/`run_contest`/`ExchangeResult`/`ContestResult` dead; `CONCENTRATION_MULTIPLIER = 3` is a formula struck by ED-901 and still public (`:63`); the five `PERSUASION_*` constants are its only live content, and W-A2 has moved them.
- Target: file deleted. ⚠ **Before deleting, record in the commit message** that `resolve_exchange:132-190` was the only code implementing canon §4's compare-model (§1.1 row 3) and that it is recoverable at this commit's parent — that is E1's evidence and it must not vanish silently.
- Falsifier: `python -c "import sys, systems.social_contest.sim.contest; assert 'systems.social_contest.sim.contest_legacy_stub' not in sys.modules"` fails before, passes after; `grep -rn "contest_legacy_stub\|CONCENTRATION_MULTIPLIER\|ContestResult\b" systems engine tools tests --include=*.py` → zero.
- Control: goldens; `parliamentary_vote.py` still imports its five names from the package (W-A2). Blast radius: the two files; `references/restructure_ledger.md` gains a `FORK:` row per `CLAUDE.md` §1.

**W-A5 · `Reserve.refund` — one write path for `Reserve.cur`.**
- Files: `primitives.py:49-56`, `resolver.py:361-362`.
- Current: `resolver.py:362` assigns `c.reserve.cur = min(c.reserve.max, c.reserve.cur + Reserve.COST["evidence"])` around the two mutators `spend`/`regroup` (`CLAUDE.md` §0.1 pt 1's shape).
- Target: `def refund(self, kind): self.cur = min(self.max, self.cur + self.COST[kind])` on `Reserve`; the resolver line becomes `c.reserve.refund("evidence"); return`.
- Falsifier: one `ck` in `_kernel_tests.py`: `assert not re.search(r"reserve\.cur\s*=", resolver_source)` — fails before, passes after. Behaviour identical.
- Control: goldens (the branch is T2-only). Blast radius: two lines.

**W-A6 · The appraise ordinal reads the owner; the RES_FLOOR "reuse" comment stops claiming what it does not do.**
- Files: `appraise.py:68-71`; `armature.py:225-229`.
- Current: `APPRAISE_FAILURE..OVERWHELMING = 0,1,2,3` retyped (D9); `armature.py:229` comments `= resolver.RES_FLOOR value (reused, not fresh)` and never imports it (D7); `_kernel_tests.py:1579` asserts `_SAO == 0.15` and imports `_RF` at `:450` without using it.
- Target: `from engine.autoload.dice_engine import DEGREE_ORDINAL, Degree` and `APPRAISE_FAILURE = DEGREE_ORDINAL[Degree.FAILURE]` etc. (four lines). `STYLE_AXIS_OFFAXIS = 0.15   # [SEED] off-axis partial overlap` — the reuse claim deleted (it is one number for two quantities, the opposite of single-sourcing). `_kernel_tests.py:1579` unchanged (it pins a `[SEED]`).
- Falsifier: `python -c "from systems.social_contest.sim.contest import appraise as a; from engine.autoload.dice_engine import DEGREE_ORDINAL, Degree; assert a.APPRAISE_OVERWHELMING is DEGREE_ORDINAL[Degree.OVERWHELMING]"` — trivially true before too (equal ints); the honest falsifier is the source: `grep -n "= 3$" appraise.py` → zero after. `grep -n "RES_FLOOR" armature.py` → zero after.
- Control: nothing executes either. Blast radius: two files.

**W-A7 · Build the panel terminal once.**
- File: `wrapper.py:181-190`.
- Current: `proceeding_venue:553-555` builds `panel_win_condition()` for a `panel` proceeding and `build_contest:181-190` rebuilds it via `dataclasses.replace` (D16; `06` measured 282 calls for 141 contests).
- Target: `if adj_type == "panel" and not isinstance(the_venue.win, VoteAtClose):` — the rebuild fires only on the prebuilt-`Venue`-plus-`adjudicator="panel"` path, where `proceeding_venue` never ran. `VoteAtClose` reads the paired bench's members at resolve time (`resolver.py:127, :143`), so the discarded `jurors` argument was already inert.
- Falsifier: wrap `panel_win_condition` in a counter; `build_contest(5, 5, venue="guild_arbitration")` → **1** call (before: 2). A `ck`.
- Control: goldens (identical object either way — executed, `10_` §2.4). Blast radius: one condition.

**W-A8 · Delete `GAMES`, the router parameter, the registry, and the harness; keep the stage-3 check.**
- Files: `wrapper.py:23` (`stubwire` import), `:64-88` (`Contest.game`), `:199-245` (`_stub`, `GAMES`), `:248-264` (`game=`), `:267-448` (`_SYMBOLS`, `_resolve`, `MECHANICS`, `_stage3_resolution_invocation_check`, `mechanics_selftest`); `contest/__init__.py:73,:119` (`GAMES`, `MECHANICS`, `mechanics_selftest` exports); `_kernel_tests.py:696-703` (four stub checks) and every `ck` that reads `MECHANICS`/`mechanics_selftest` (grep; `:822` per `06`); `engine/tests/test_pipeline_reach.py:826-844` (`_OI18A_GAMES_ROWS` + `test_oi18a_contest_games_router_stub_rows_are_self_flagged` — reads `wrapper.GAMES[g]["resolve"](None)` at `:838` and dies with `GAMES`; **leave `:847` `test_oi18a_mode_scaffolds_are_self_flagged` and the three `modes.py` scaffolds alone until W-F1/W-F3 delete each scaffold with its terminal**); `agon_harness.py` (522 lines, zero callers).
- Current: a four-row router with one live row and one caller that never passes `game` (`wrapper.py:248`); a 25-row registry in which `WIRED` means two things (`10_` §1.9); a harness that replicates `Bout.resolve` verbatim (`agon_harness.py:99-104`, WORKAROUND 5).
- Target: `resolve_contest(contest, *, policy_a=logos_spammer, policy_b=logos_spammer, record=False)` → `_resolve_bout(...)` (renamed from `_resolve_agon`; **never `_resolve`** — B3's collision). `MECHANICS` and its machinery gone. **`_stage3_resolution_invocation_check`'s three measurements move into `_kernel_tests.py` as three `ck()` lines** (CR4 die raises mean net; aligned armature raises mean track; CR5 strips at least once) — they run the resolver and are the only executable specification of Stage 3; the registry around them was the overhead. `agon_harness.py` deleted; its five WORKAROUNDs (`:47-104`) pasted into the commit message as requirements notes (WORKAROUND 3 is W-B2; 2 and 4 are open design questions; 1 and 5 are harness-shaped and die with it).
- Falsifier: `python -c "from systems.social_contest.sim.contest import wrapper as w; assert not hasattr(w,'GAMES') and not hasattr(w,'MECHANICS')"`; `resolve_contest(c, game='agon')` raises `TypeError` after (accepted before). Count arithmetic: −4 (stub checks) −k (`MECHANICS` checks, grep) +3 (stage-3 measurements) — state k.
- Control: goldens (the production path passes no `game`). Blast radius: `wrapper.py` (~250 lines out), `__init__.py`, `_kernel_tests.py`, `test_pipeline_reach.py`, `agon_harness.py`, `test_contest_kernel.py:93`.

### PHASE B — reachability (defaults byte-identical)

**W-B1 · The venue arrives: `**venue_overrides` through `build_contest`, and a `venue:` key on the row.**
- Files: `modes.py:485-519` (`PROCEEDINGS`), `:536-567` (`proceeding_venue`), `wrapper.py:110-133`.
- Current: `proceeding_venue` returns `Venue(budget=budget, win=win, **o)` (`:567`) and `build_contest:133` passes no `**o`, so all eight rows inherit `resolver.Venue`'s defaults (executed: every row `faults=(True,True,2,2)`, `allow_rebuttal=False`, default register; §2.1). The ~260-line venue library (`:66-325`) is unreachable from any proceeding.
- Target:
  ```python
  # modes.py — every PROCEEDINGS row gains one key; None keeps today's behaviour exactly
  "church_tribunal": dict(..., venue=None),        # W-G2 proposes inquisition_hearing_venue here — Jordan's
  def proceeding_venue(name, *, use_tracker=None, **o):
      spec = PROCEEDINGS[name]; budget = spec["exchanges"][1]; win = ...   # unchanged selection
      if "start_ground" in spec and "start_ground" not in o: o["start_ground"] = spec["start_ground"]
      base = spec.get("venue")
      if base is None:
          return Venue(budget=budget, win=win, **o)
      import dataclasses as _dc
      return _dc.replace(base(), budget=budget, win=win, **o)   # the preset's register/faults/tense, the row's budget/terminal
  # wrapper.py
  def build_contest(side_a, side_b, *, venue, adjudicator=None, stakes=None, world=None,
                    use_tracker=None, degree_extension=CONTEST_DEGREE_EXTENSION, **venue_overrides):
      ...
      the_venue = proceeding_venue(proc_name, use_tracker=use_tracker, **venue_overrides)
  ```
  A prebuilt `Venue` with non-empty `venue_overrides` raises `ValueError` (the same shape as the `use_tracker` refusal at `:137-140`).
- Falsifier: `build_contest(5, 5, venue="church_tribunal", proof_logos=0.9).venue.proof_logos == 0.9` — `TypeError` before, passes after; and with every `venue=None` the executed eight-row table (§0.4, `m1_kernel.py` §7) is byte-identical (a `ck` over all eight comparing `proceeding_venue(name)` field-by-field to a frozen copy taken before the change).
- Control: goldens (no row sets `venue`; the seam passes no overrides). Blast radius: two files.

**W-B2 · `armature=` and `rng=` reach the kernel; CR4's die enters as δσ.**
- Files: `wrapper.py:110-196` (`build_contest`, `Contest`), `:203-217` (`_resolve_bout`); `resolver.py:28-32` (`roll_net`), `:139/:144` (`gauss`), `:334` (`uniform`), `:239-270` (`Bout.__init__`), `:399-406` (the CR4 pool die), `:283-308` (`_reception`); `rhetoric.py:206` (`CR4_PRIMARY_GENRE_POOL_BONUS`).
- Current: no `armature=` (`wrapper.py:110-111`; `agon_harness.py` WORKAROUND 3); the kernel draws from the module-level `random` at three sites and the seam reseeds it around the call. CR4's `+1` **pool die** composes with `PoolDesaturation` into a penalty above pool 9 (§0.4 row 3: mean degree −0.053 at pool 13, −0.065 at 17) — a flat-shift trap (`SKILL.md` §11.2) and, under the ruled extension, a sign flip.
- Target:
  ```python
  # resolver.py
  def roll_net(pool, rng=None): return _sigma.roll_net(pool, rng=rng if rng is not None else random)
  class Bout:
      def __init__(self, ca, cb, venue, adjudicator=None, record=False, armature=None,
                   degree_extension=_DEFAULT_DEGREE_EXTENSION, rng: random.Random | None = None):
          self._rng = rng            # None => the module stream (the 389 seeded checks depend on it)
      # every draw: roll_net(pool, rng=self._rng) · (self._rng or random).gauss(...) · (self._rng or random).uniform(...)
  # _reception: the CR4 bonus is a δσ, not a die
      lev = Leverage.net(c.faculty, on_ground=True) + max(0.0, dsigma_bonus) + max(0.0, cr4_dsigma)
  # _apply: cr4_dsigma = CR4_PRIMARY_GENRE_DSIGMA if primary_genre_pool_bonus(chosen_genre, self.live) > 0 else 0.0
  # rhetoric.py: CR4_PRIMARY_GENRE_DSIGMA = level("minor")   # [SEED] 0.25σ — the +1D re-expressed under CR6 as a setup advantage; the pool-die constant is deleted
  # wrapper.py
  def build_contest(..., armature: "ArmatureConfig | None" = None, rng: "random.Random | None" = None, **venue_overrides):
      # A7 from 01_SPINE.md: derive the asymmetric gate from the row, never from the caller
      _ASYMMETRIC_ROLES = frozenset({"crown_objects", "inquisitor_proposes"})     # modes.py:493, :496
      if armature is not None and proc_name is not None:
          armature = dataclasses.replace(armature, opponent_is_adjudicator=(spec["roles"] in _ASYMMETRIC_ROLES))
  def _resolve_bout(contest, *, policy_a, policy_b, record=False):
      bout = Bout(contest.side_a, contest.side_b, contest.venue, contest.adjudicator, record=record,
                  degree_extension=contest.degree_extension, armature=contest.armature, rng=contest.rng)
      return bout.resolve(policy_a, policy_b), bout
  ```
- Falsifiers (each a `ck`, in this order): **F-S7** — snapshot `random.getstate()`, run `resolve_contest(build_contest(5,5,venue="guild_arbitration", rng=random.Random(7)))`, assert the global state is unchanged, assert two `Random(7)` runs are identical and `Random(8)` differs — **fails before** (no `rng=`), passes after, and observes any missed draw site forever; **F-S5** — `build_contest(..., venue="formal_contest", armature=ArmatureConfig(styles={A:"vision"}, positions=…))` over 200 seeds moves the mean track vs `armature=None` (needs W-B3's positions shape; land B2 and B3 in one commit); **F-S6** — `build_contest(venue="church_tribunal", armature=ArmatureConfig(opponent_is_adjudicator=False))` yields a contest whose armature has it `True`; **CR4 sign** — mean reception degree with the chosen genre matching the terrain ≥ without, at pools 5, 9, 13, 17 (the §0.4 probe as a `ck` at N = 4,000 per cell; **fails before at 13 and 17**, passes after). The existing `_kernel_tests` CR4 checks that assert a pool-die shape (`_mean_net(1.0) > _mean_net(0.0)`, moved in W-A8) are rewritten 1-for-1 to the δσ form.
- Control: goldens — `armature=None`, `rng=None` are byte-identical by construction (`resolver.py:249-258` documents the first; the second is the module stream). Blast radius: `resolver.py`, `wrapper.py`, `rhetoric.py`, `_kernel_tests.py`. **Residual, stated:** `level("minor")` as the δσ magnitude for a matched genre is a `[SEED]`; Jordan tunes it; the *form* (δσ, not a die) is CR6's own (`armature.py:316-320`).

**W-B3 · The armature is keyed on the bench position, not a memory address.**
- Files: `armature.py:374-395` (`position_of`), `:414-451` (`ArmatureConfig`); every constructor site (`_kernel_tests.py`, the moved stage-3 checks).
- Current: `positions: Dict = {id(adjudicator-or-member) → ArmaturePosition}` (`:429`), read at `:393-395`. Not computable before `build_contest` (which mints the judges, `wrapper.py:151`; `modes.py:445-447,:461`); not serialisable; value-equal judges share a hash and differ in id (executed).
- Target:
  ```python
  @dataclass(frozen=True)
  class ArmatureConfig:
      styles: Dict[str, str] = field(default_factory=dict)
      positions: tuple = ()          # ArmaturePosition per bench seat, in Panel.members order; a lone Adjudicator is seat 0. () => zero vector everywhere
      opponent_is_adjudicator: bool = False
      cr5: bool = True
  def position_of(adjudicator, *, opponent_is_adjudicator=False, positions=()):
      if opponent_is_adjudicator: return ArmaturePosition.zero()
      members = adjudicator.members if isinstance(adjudicator, Panel) else (adjudicator,)
      if positions and len(positions) != len(members):
          raise ValueError(f"armature positions {len(positions)} != bench seats {len(members)}")
      ps = positions or tuple(ArmaturePosition.zero() for _ in members)
      return ArmaturePosition.mean(ps) if isinstance(adjudicator, Panel) else ps[0]
  ```
- Falsifier: construct the config **before** the contest — `cfg = ArmatureConfig(styles={A:"vision"}, positions=(ArmaturePosition(consequence=1.0),))`; `c = build_contest(5,5,venue="royal_audience", armature=cfg)` — wait: `royal_audience` is asymmetric (gated off, δσ = 0); use `formal_contest` with a 15-tuple or a prebuilt `Venue` + `expert_judge`; assert the mean track over 200 seeds exceeds the `armature=None` mean. **Fails before** (the key is unknowable), passes after. Plus `dataclasses.asdict(cfg)` round-trips through `json.dumps` — a one-line probe in the commit. Plus a length-mismatch `ValueError` `ck`.
- Control: the kernel suite's armature checks rewritten 1-for-1 (they currently construct `positions={id(adj): …}`); count unchanged. Blast radius: `armature.py`, `_kernel_tests.py`.

### PHASE C — the outcome shape

**W-C1 · `ContestOutcome`, `margin()`, the band→Degree table, `outcome()`.**
- Files: `contract.py` (new dataclass; imports only `dataclasses` — keep that property, `contract.py:2-3`); `resolver.py:52-147` (every `WinCondition`), `:440-466` (`Bout.resolve`), new `Bout.outcome`; `dictionaries.py:699-725` untouched.
- Current: six `resolve()`s return a side label or a band string; `Bout.resolve:466` labels `committee` as `"win"`; no margin, no degree; `VoteAtClose` draws inside `resolve()` so a second read would draw again.
- Target:
  ```python
  # contract.py
  @dataclass(frozen=True)
  class ContestOutcome:
      """The ONE thing a resolved issue returns. `winner` and `band` are legibility fields with a
         deletion date: the commit in which the rebuilt seam reads `degree` (PR #362 §C.5 :692)."""
      winner: str | None            # A | B | None (committee, draw, withdrawn)
      degree: object | None         # engine.autoload.dice_engine.Degree; None only for a withdrawn issue
      margin: float                 # signed, A-positive, adv units (WinCondition.margin)
      reason: str                   # 'win' | 'draw' | 'clinch:<family> - <detail>' | 'conceded:<key>' | 'withdrawn:<key>'
      veto: str | None = None       # the side whose fault ended the bout
      band: str | None = None       # WinCondition.resolve()'s verbatim output
      beats: tuple = ()
  # resolver.py
  BAND_TO_OUTCOME = {"A_total": (A, Degree.OVERWHELMING), "A_decisive": (A, Degree.SUCCESS),
                     "committee": (None, Degree.PARTIAL), "B_decisive": (B, Degree.SUCCESS), "B_total": (B, Degree.OVERWHELMING)}
  def degree_of_margin(margin: float) -> "Degree":
      """ONE banding for ONE quantity across all six terminals: the Persuasion bands read on the track of the margin."""
      return BAND_TO_OUTCOME[band_of_track(track_of(margin))][1]
  class WinCondition:
      def resolve(self, s, closing, adj=None): raise NotImplementedError
      def margin(self, s, adj=None) -> float: raise NotImplementedError      # signed, A-positive, adv units
      def outcome(self, s, adj=None, reason="win") -> ContestOutcome:
          w = self.resolve(s, True, adj); m = self.margin(s, adj)
          winner = None if w in ("draw", "committee") else (A if w in (A, "A_total", "A_decisive") else B)
          return ContestOutcome(winner=winner, degree=degree_of_margin(m), margin=m, reason=reason, band=w)
  # margins (the spine's A3 table WITHOUT SUCCESS_UNIT — §5.4 gives the measured reason):
  #   ThresholdRace / TallyAtClose:  s.adv[A] - s.adv[B]
  #   ProofBar:      ((s.adv[self.ch] - s.adv[other(self.ch)]) - self.bar) * (1.0 if self.ch == A else -1.0)
  #   GraceThreshold:(s.adv[self.pet] - self.bar) * (1.0 if self.pet == A else -1.0)
  #   PersuasionTrack: s.adv[A] - s.adv[B]            # track - start == scale * gap; margin stays in adv units
  #   VoteAtClose:   s.adv[A] - s.adv[B]              # the ROOM's margin; the WINNER is the ratified ballot (ED-1057), untouched:
  #       def outcome(...): w = self.resolve(s, True, adj); return ContestOutcome(winner=(None if w=="draw" else w), degree=degree_of_margin(self.margin(s)), margin=..., band=w)
  #       resolve() draws once; outcome() calls it once. Docstring gains one sentence: "draw is unreachable on an odd bench with equal weights (every shipped bench)".
  class Bout:
      def outcome(self, polA, polB) -> ContestOutcome:
          w, reason = self.resolve(polA, polB)
          if reason.startswith("clinch"):
              loser = other(w); out = self.v.win.outcome(self.state, self.adj, reason=reason)
              return dataclasses.replace(out, winner=w, veto=loser, beats=tuple(self.log or ()))
          return dataclasses.replace(self.v.win.outcome(self.state, self.adj, reason=reason), beats=tuple(self.log or ()))
  ```
  `resolve_contest` keeps its `((band, reason), bout)` return (the seam unpacks it, `scene_dispatch.py:301` — not touched); `_resolve_bout` computes `out = bout.outcome(...)`, stores `bout.last_outcome = out`, and returns `((out.band, out.reason), bout)` — value-identical. `narrative.Chronicle.margin` → `share` (six sites, `narrative.py:44,:55,:96,:98` + two `render` reads) — the name collision `01_SPINE.md` §1.4 rules on.
- Falsifiers: **F-S1** iterate `WinCondition.__subclasses__()`, call `margin()` on a fixture state, `assert checked == 6`; **F-S2** A-positive on every subclass including `ProofBar(challenger=B)` and `GraceThreshold(petitioner=B)` (this is the one that catches the sign inversion); **F-S3** `sign(margin)` agrees with `resolve(closing=True)` wherever it names a side — with `ThresholdRace`'s early branch asserted separately as a named divergence; **F-S4** `VoteAtClose.outcome()` describes the same ballot as `resolve()` over N seeds, `assert checked == N` (fails on any implementation that draws twice); **the paired table** — 2,000 `guild_arbitration` bouts at 1v6 through `Bout.outcome`: `PARTIAL` ≈ 0.30, `winner` distribution ≈ the ballot's (0.066/0.934) — fails before (no `outcome`), passes after, and is the requirement-(1) artifact.
- Control: goldens (`resolve_contest`'s return is byte-identical; `band` verbatim). Blast radius: `contract.py`, `resolver.py`, `wrapper.py`, `narrative.py`, `_kernel_tests.py` (two checks at `:694-695` rewritten per `01_SPINE.md` R2).

**W-C2 · `narrative.classify` reads a winner, not a token.**
- File: `narrative.py:83-100` (`classify`), `:112-154` (`summarize`).
- Current: `wsign = 1 if winner == A else -1` (`:92`) — a `PersuasionTrack` band is never `A`, so every band verdict classifies as a B win. Executed: `classify("A_total", …)` → `CLEAR_WIN`, `classify("a", …)` → `ROUT` on identical leads.
- Target: `summarize(outcome: ContestOutcome)`; `classify(winner, why, …)` receives `outcome.winner` (`A`/`B`/`None`); `DEADLOCK` on `None`; `margin` renamed `share` (W-C1).
- Falsifier: `summarize(ContestOutcome(winner=A, band="A_total", …, beats=log))` and `summarize(ContestOutcome(winner=A, band="a", …, beats=log))` yield the same `shape` — fails before, passes after. A `ck`.
- Control: nothing on the path calls `narrative`. Blast radius: one file.

### PHASE D — the fold (requirements 2 and 3)

**W-D1 · `Bout` accepts a shared side runtime.**
- File: `resolver.py:239-241`.
- Current: `self.c = {A: _Side(ca, …), B: _Side(cb, …)}` — every `Bout` builds fresh Reserve/Standing/Room/FaultState; nothing persists across bouts.
- Target: `Bout.__init__(..., sides: dict | None = None)`; `self.c = sides if sides is not None else {A: _Side(ca, venue.split_standing), B: _Side(cb, venue.split_standing)}`. `Room` stays per-bout (`resolver.py:246`) — the room is the audience's state for *this* matter; `_Side` is the person's.
- Falsifier (`engine/tests/test_contest_issues.py::test_fault_state_carries_across_bouts`): bout 1 with A playing `hard` before `expert_judge` → `clinch:barred-device`; bout 2 built with `sides=bout1.c` and both sides on `logos_spammer` → clinches at move 1 for the same reason (executed prototype, `m2_paired.py` E). **Fails before** (`TypeError: unexpected keyword 'sides'`), passes after.
- Control: goldens (default `None`). Blast radius: three lines.

**W-D2 · `Issue` and `resolve_issues`.**
- Files: `contract.py` (new dataclass), `wrapper.py` (new function; the `_as_contestant` adapter reused).
- Current: nothing resolves more than one matter; `Contest` carries one `venue`.
- Target:
  ```python
  # contract.py
  @dataclass(frozen=True)
  class Issue:
      """One contested matter — under PR #362 a Proposition (§B.6); `key` is its id until PropositionId exists."""
      key: str
      venue: object                 # resolver.Venue — its own terminal, register, faults
      sides: tuple = (A, B)         # W-E1 generalises; two-sided until then
      condition: tuple | None = None  # (depends_on: str, when_winner: side, effect: "concede" | "withdraw") — W-D3
  # wrapper.py
  def resolve_issues(issues, side_a, side_b, *, adjudicator=None, policy_a=logos_spammer, policy_b=logos_spammer,
                     armature=None, rng=None, record=False, degree_extension=CONTEST_DEGREE_EXTENSION) -> dict:
      """The contest: an ORDERED fold over issues sharing ONE side runtime (PR #362 §C.4's shape, §G.2.9's
         order criterion). Writes nothing. Returns {issue.key: ContestOutcome} in declared order."""
      ca, cb = _as_contestant(side_a), _as_contestant(side_b)
      adj = adjudicator if adjudicator is not None else Adjudicator()
      pa = POLICIES[policy_a] if isinstance(policy_a, str) else policy_a
      pb = POLICIES[policy_b] if isinstance(policy_b, str) else policy_b
      runtime = None; out = {}
      for iss in issues:
          if iss.key in out: raise ValueError(f"duplicate issue key {iss.key!r}")
          # W-D3 inserts the condition branch here
          bout = Bout(ca, cb, iss.venue, adj, record=record, armature=armature, degree_extension=degree_extension, rng=rng, sides=runtime)
          runtime = bout.c                                # built on the first issue, shared thereafter
          out[iss.key] = bout.outcome(pa, pb)
      return out
  ```
- Falsifiers (`test_contest_issues.py`): **vector** — nine issues on `proceeding_venue("guild_arbitration")` at 1v6, seed 7 → nine `ContestOutcome`s, in order, `assert checked == 9`; **two-arm equivalence** — over 500 seeds, the first issue's outcome from `resolve_issues([iss])` equals `Bout.outcome` on the same inputs and seed (the single-issue fold is byte-identical to a bout); **texture** — over 2,000 nine-issue bundles at 4v4, the per-issue `PARTIAL` rate is within ±0.03 of the single-bout rate at 4v4 (0.85, §1.2 row 3) **and** the bundle's `PARTIAL` count is not constant (independent accumulation, not one shared momentum — this is the test that distinguishes §5.1's chosen shape from its rejected option (c)). All three fail before (no function), pass after.
- Control: goldens (nothing on the path calls it). Blast radius: two files, one new test file.

**W-D3 · Conditions: concede and withdraw, evaluated in declared order.**
- File: `wrapper.py` (`resolve_issues`, the branch marked in W-D2).
- Target:
  ```python
          if iss.condition is not None:
              dep, when_winner, effect = iss.condition
              if dep not in out:
                  raise ValueError(f"issue {iss.key!r} depends on {dep!r}, which is not resolved before it — declare the order (§G.2.9)")
              if out[dep].winner == when_winner:
                  if effect == "concede":
                      out[iss.key] = ContestOutcome(winner=other(when_winner), degree=Degree.SUCCESS, margin=0.0, reason=f"conceded:{dep}"); continue
                  if effect == "withdraw":
                      out[iss.key] = ContestOutcome(winner=None, degree=None, margin=0.0, reason=f"withdrawn:{dep}"); continue
                  raise ValueError(f"unknown condition effect {effect!r}")
  ```
  `SUCCESS` for a concession is not a `[SEED]`: a concession grants the counterparty's stated ask, no more (`OVERWHELMING` would be "more than asked", `PARTIAL` would be "less"); state that in the docstring.
- Falsifiers (`test_contest_issues.py`): **concede** — Y resolved for A by construction (B plays `staller` → `clinch:silence` → `winner A`), X has `condition=("Y", A, "concede")` → `out["X"].winner == B`, `reason == "conceded:Y"`, `out["X"].beats == ()` (no bout ran); **withdraw** — same with `"withdraw"` → `winner None`, `degree None`; **not triggered** — Y resolved for B → X runs a bout (`beats` non-empty when `record=True`); **order** — X listed before Y raises `ValueError`. Four tests, each fails before (the tuple is ignored / the field does not exist), passes after.
- Control: goldens. Blast radius: one function.

### PHASE E — N sides (requirement 4, the second half)

**W-E1 · `Bout` over a `sides` tuple, byte-identical for two.**
- Files: `contract.py:7-8` (`A, B, other`), `resolver.py:46-50` (`ContestState`), `:197-236` (`_Side`), `:239-281` (`Bout.__init__`, `_view`), `:440-457` (`resolve`), `primitives.py:232-236` (`Room`), `:262-279` (`DefeatCatalogue.check`), every terminal's `s.adv[A]`/`s.adv[B]`; `wrapper.py` (`resolve_issues` passes `{s: runtime[s] for s in iss.sides}`).
- Current: two sides by construction at every one of those sites (§3, requirement (4) row).
- Target: `Bout.__init__(specs: dict[str, Contestant] | tuple, venue, …, sides: dict | None = None)` — a two-tuple `(ca, cb)` maps to `{A: ca, B: cb}` (byte-identical path); `self.sides = tuple(self.c)`; `ContestState(sides)` → `self.adv = {s: 0.0 for s in sides}`; `Room(sides)`; `for side in self.sides:` at `:443`; `DefeatCatalogue.check(faults)` iterates `faults` in insertion order; `_view`'s `opp_standing = max(self.c[o].rank_v() for o in self.sides if o != side)` (the strongest opponent gates `hard`); `other(side)` keeps its two-sided meaning and every compare-type terminal gains `pair: tuple = (A, B)` and reads `s.adv[pair[0]] - s.adv[pair[1]]`; bar-type terminals already name their side. **A division terminal over N sides is NOT shipped in this item** — its share rule is a `[SEED]` with no precedent (`split` is two-sided by construction, `02:299-305`); `settle()` stays two-sided (W-F1) and a three-party stake is written as pairwise issues until Jordan rules (§8 E5).
- Falsifiers (`test_contest_issues.py`): **three orators, one bar each** — three contestants, an issue per side with `GraceThreshold(bar, petitioner=<side>)`, all three can pass in one seeded run (a many-win outcome); **byte-identity** — 500 seeded two-sided bouts through the new constructor equal the old tuple form (run the old path from the parent commit into a fixture file first); the kernel suite green at an **unchanged** pin.
- Control: goldens; the kernel pin. Blast radius: the widest item — `contract`, `resolver`, `primitives`, `wrapper`, `narrative` (`_name`), every terminal. Land it alone.

### PHASE F — the three terminals as venue rows

**W-F1 · `settle()` on the band table; the succession split fixed by import.**
- Files: new `systems/social_contest/sim/contest/settle.py` (per `02_NEGOTIATION.md` §5.2–5.3, verbatim except the keying); `faction.py:86-118` (`succession`), `_kernel_tests.py:182`; `modes.py:342-350` (`NegotiationMode` deleted; `test_pipeline_reach.py:847`'s list loses one name); `PROCEEDINGS["private_negotiation"]` gains `burden="NONE"` (W-F2's field).
- Current: no division terminal; `faction.succession:107,:117` is anti-monotone on A's side (executed: t=4.0 → b/0.60, t=5.0 → a/0.55, t=6.0 → a/0.50) and `_kernel_tests.py:182` cannot observe it (a disjunction satisfied by any of three values).
- Target: `SHARE_BY_DEGREE = {Degree.PARTIAL: 0.50, Degree.SUCCESS: 0.55, Degree.OVERWHELMING: 0.60}` (canon `social_contest_v30.md:421-423`, three ratios); `split(margin) = lead if margin >= 0 else 1 - lead` with `lead = SHARE_BY_DEGREE[degree_of_margin(abs(margin))]` — **the band table, not `degree_from_net(abs(margin), 0.0)`**; `settle(margin, floor_a, ceil_a)` as written at `02:308-327`. `succession` deletes its `leader`/`ratio` lines and returns `('split', A if share >= 0.5 else B, share, t)` with `share = split(gap)`. `_kernel_tests.py:182` rewritten: `succession` at a forced `t == 5.0` (equal adv) yields `share == 0.50` — **fails before** (0.55 to A), passes after.
- Falsifiers: F-N1 (disjoint reservations → `Refusal`), F-N2 (`split(-m) == 1 - split(m)` on 101 points incl. 0), F-N4 (mirror symmetry of `share` over N seeds within a declared tolerance `[SEED]`), from `00` §3(i); plus **the band edges are canon's** — `split(m)` steps at `|track_of(m) - 5| == 2` and `== 4`, not at `|m| == 1` and `3`.
- Control: goldens (`private_negotiation` not on the path). Blast radius: one new module, `faction.py`, `modes.py`, `_kernel_tests.py`, `test_pipeline_reach.py`.

**W-F2 · `burden` on every row; `church_tribunal` becomes the inquiry venue; the tracker tri-state goes.**
- Files: `modes.py:485-519` (rows), `:521-534` (`_use_tracker`), `:536-567` (`proceeding_venue`), `:475-476` (the two start constants), `:181-198` (`inquisition_hearing_venue` — merged into the row via W-B1's `venue:` key and deleted with its `CROSS_CULTURAL_VENUES` entry at `:319`), `wrapper.py:110` (`use_tracker` parameter); `_kernel_tests.py` sections that pin `church_tribunal` on `PersuasionTrack(start=6.0)` and the tracker tri-state (the +13 rev3 checks, `test_contest_kernel.py` docstring).
- Current: no `burden`; `church_tribunal` fakes a burden with a biased start (`CHURCH_TRIBUNAL_TRACK_START = 6.0`, `:476`); the tri-state encodes one fact in two fields (`10_` §2.5); `ProofBar` is reachable from no row.
- Target: `BURDENS = ("ACCUSER", "RESPONDENT", "NONE")` beside `PROCEEDINGS` (`LOWER_STANDING` from the spine is dropped — no row needs it; add it the day one does); every row carries `burden`: the four tracked rows `NONE` (their terminal stays `PersuasionTrack`), `guild_arbitration` `NONE` (panel), the three untracked rows `NONE` (`TallyAtClose`), and **`church_tribunal` `ACCUSER` with `bar=2.5  # [SEED] inherited verbatim from inquisition_hearing_venue (modes.py:196)`**, terminal `ProofBar(bar=spec["bar"], challenger=A)`, `venue=inquisition_hearing_venue`'s register/faults (`evasion_strikes=1` inherited, `yield_strikes=2` **unchanged** — §2.3), `start_ground=FACT` unchanged, `track_start` deleted from the row. `proceeding_venue`: `win = _WIN_BY_BURDEN[spec["burden"]](spec)` where `NONE` keeps today's `tracker`-derived choice **for this item** (the tri-state's deletion is the second half: replace `tracker=True/False` with an explicit `terminal="track" | "tally"` string on the `NONE` rows and delete `_use_tracker`, `tracker_mode`, `use_tracker`; a caller wanting the track on `private_negotiation` passes `win=PersuasionTrack()` through W-B1's overrides). **`restricted` is not built** (§2.3, measured).
- Falsifiers: **F-I1** — `church_tribunal` at equal faculty over N ≥ 200 → acquittal ≥ 0.9; passive (`staller`) defence → conviction ≥ 0.9 (the snapshot's own numbers as the control band); **the row selects the class** — `type(build_contest(5,5,venue="church_tribunal").venue.win) is ProofBar` (fails before: `PersuasionTrack`); **burden consistency** — over the eight rows, `ACCUSER` ⇒ burden-bearing terminal, `NONE` ⇒ not, `assert checked == 8`; **silence still convicts with no field** — B on `support`-forever loses ≥ 0.99 (the §0.4 measurement as a `ck`; passes before and after — it is the *control* that the deleted `restricted` guarded nothing). The pinned `church_tribunal` expectations in `_kernel_tests.py` move — state each.
- Control: goldens (`church_tribunal` is not on the production path). Blast radius: `modes.py`, `wrapper.py`, `_kernel_tests.py`, `test_contest_kernel.py:93`. The FA-lane grounds check (`systems/factions/sim/tribunal.py:73`, inquiry's B2/B4) is **not** in this item; it is named for the FA lane.

**W-F3 · `unanimity_required`, with a per-member disposition — the holdout becomes a member.**
- Files: `contract.py:24-35` (`Adjudicator`), `resolver.py:98-147` (`VoteAtClose` — a new branch beside `:128`, the weighted branch untouched), `dictionaries.py:699-725` (`panel_win_condition` accepts the third value; the `stubwire` branch deleted), `modes.py` (a `consensus_body_venue`/`_mode` in `INSTITUTIONAL_MODES`, per `04:224-243` **without** `on_hung`/`holdout_rounds`), `engine/tests/test_pipeline_reach.py:876-879` (the OI-19 probe expecting `unanimity_required` to be `stub_wired` — deleted), `CeremonialMode`/`DyadicMode` untouched.
- Current: `unanimity_required` named at `dictionaries.py:686,:707,:721` and implemented nowhere (returns a `StubResult`); the ballot draws i.i.d. per juror (`resolver.py:139,:144`) so no member can be a holdout except by draw order; `margin = share − 1 ∈ [−1,0]` bands `Partial`/`Failure` only (executed).
- Target:
  ```python
  # contract.py — the ONE new per-member field; 0.0 is byte-identical to today
  @dataclass(frozen=True)
  class Adjudicator:
      ...; disposition: float = 0.0     # signed lean on the motion in ballot units; feeds the ballot only (character/discipline untouched)
  # resolver.py — VoteAtClose
      def _ballots(self, s, adj, rng):                      # ONE draw pass, in members order, same count as today
          gap = s.adv[A] - s.adv[B]; members = getattr(adj, "members", None) or (adj,) * self.jurors
          r = rng or random
          return tuple((i, max(0.0, float(getattr(m, "discipline", 0.0))), (self.k*gap + getattr(m, "disposition", 0.0) + r.gauss(0, self.noise)) > 0) for i, m in enumerate(members))
      # weighted_by_standing and simple_majority: unchanged rules, now reading _ballots (same draws, same order — the goldens are the control)
      # unanimity_required:
      #   winner = A iff all(assent) else B ; dissenters = tuple(i for i, w, a in ballots if not a)
      #   degree by table, zero constants:  all assent -> (A, OVERWHELMING) ; weighted majority for A but not all -> (B, PARTIAL) "referred back" ;
      #                                     weighted majority against -> (B, SUCCESS)      # the precedent is parliamentary_bridge._winner_and_degree's shape
      #   outcome() carries dissenters in `beats`? No — add `dissenters: tuple = ()` to ContestOutcome ONLY if a consumer reads it; until then expose VoteAtClose.last_ballots (read by the tests)
  ```
  **`Ballot`/`BallotBook` as dataclasses are not added**: a tuple of `(index, weight, assent)` is the retained ballot, and `dissenters` is a Query over it (`04` §7.3's own cut, applied one step further). `holdout_rounds`, `on_hung`, the recusal: **not built** (§2.4, `08` §2 row 3).
- Falsifiers (`test_contest_issues.py`): **F-C1'** — a 7-bench with one member `disposition=-5.0` under `unanimity_required` → `winner B`, `degree PARTIAL`, `dissenters == (i,)` for that seat, over 200 seeds `assert checked == 200`; under `weighted_by_standing` the same bench carries for A at a high gap; **F-C2** — P(block) → 1 as N grows with one `disposition=-5.0` member under unanimity, unchanged under weighted (the *liberum veto*, printed as a table); **draw counts** — `_ballots` draws exactly `len(members)` gaussians (patch `random.gauss` with a counter) so the goldens cannot move; **F-S4** re-run. Each fails before (no branch / no field), passes after.
- Control: goldens (`guild_arbitration` runs `weighted_by_standing` with every `disposition == 0.0`; the draw count and order are unchanged — this is the whole control, and it is the reason `_ballots` must be one pass). Blast radius: `contract.py`, `resolver.py`, `dictionaries.py`, `modes.py`, `test_pipeline_reach.py`. **Residual:** the antibody (frivolity clinch / CR5 backfire, `04` §5.4) is not wired here — channel 1 already executes for any off-ground move, channel 2 needs an armature and a Style, and neither is *consensus-specific*; a holdout who argues off the question already clinches.

### PHASE G — Jordan's decisions, defaults shipped (the goldens MOVE, deliberately)

**W-G1 · The continuous draw.** `resolver.py:28-32 roll_net` → `_sigma.roll_net_continuous(pool, rng=…)`. Un-quantizes the leverage channel (§1.2 row 1); makes the kernel's draw the same as the faction layer's (S methodology). Every seeded `_kernel_tests` expectation, `GOLDEN_TRACE`, and both campaign goldens re-pin in **one commit** whose message carries the §1.2 row-1 table before/after and the `tools/balance_oracle.py` two-arm result (240 campaigns, ~13 min; `CLAUDE.md` §7). Falsifier: at faculty 1 an aligned armature moves P(A decisive+) by > 0 (`m1_kernel.py` §11: +0.000 before). **Jordan's; default ON.**

**W-G2 · A venue preset per proceeding row** via W-B1's `venue:` key. Proposed table, every cell `[SEED]`: `formal_contest`/`grand_contest` → `public_oration_venue`; `royal_audience` → `imperial_petition_venue`'s register with `GraceThreshold` replaced by the row's terminal; `church_tribunal` → `inquisition_hearing_venue` (W-F2 already); `guild_arbitration` → `secret_council_venue`'s register/faults with the panel ballot; `casual_dispute`/`private_negotiation`/`personal_appeal` → `None`. Falsifier: the eight-row table (§0.4) re-executed and pasted. Moves `guild_arbitration`, hence the goldens. **Jordan's; default = the table above.**

**W-G3 · The interaction table leaves the code.** Delete `InteractionType`, `INTERACTIONS_TABLE`, `derive_interaction` (`dictionaries.py:269-323`) and their `_kernel_tests` Stage-2 checks; keep the table as prose reference in `social_contest_v30.md` §4 Step 4, which already has it. This is E1's default (accumulation model kept). Falsifier: grep zero. **Jordan's; default = delete.** If Jordan chooses the compare model instead, the work item is a new terminal-side reception (`_reception` compares the two sides' nets per exchange, margin − resistance → `adv`) built from `resolve_exchange`'s logic at W-A4's parent commit — a different game, not this plan.

---

## §11 · Order of execution, and the commit plan

```
A1 A2 A3 A4 A5 A6 A7 A8        one commit each for A3, A4, A8 (each re-pins the count); A1/A2/A5/A6/A7 may share one
B1 · (B2 + B3 together)        B2 and B3 land in ONE commit — F-S5 needs both
C1 · C2                        C1 alone (the shape); C2 with it or after
D1 · D2 · D3                   D1 alone (three lines, its own falsifier); D2+D3 together with test_contest_issues.py
E1                             alone; the widest diff in the plan
F1 · F2 · F3                   one commit each; F2 and F3 re-pin the count
G1 · G2 · G3                   NOTHING lands without Jordan's word per item; G1 first (it re-pins everything once)
```

After each phase: `python -m pytest engine/tests/test_contest_kernel.py engine/tests/test_mc_v18_regression.py engine/tests/test_f7_smoke_oracle.py tests/valoria/test_import_cycle_game_state_npe.py -q` and, from D on, `engine/tests/test_contest_issues.py`. Update `registers/handoffs/HANDOFF_SC.md` at each phase boundary with the phase letter, the `RESULT:` line and the pin; close `ED-SC-0020` at F2 citing `01_SPINE.md` §1.5 and this §5.4; leave `ED-SC-0015` open (seam).

---

## §12 · Self-audit (SKILL.md §9), attacks that failed, null results, what would make this wrong

### §12.1 9a — backward propagation

- §2.2 says negotiation's band edges "do not hold" because of `SUCCESS_UNIT`; §5.4 and W-F1 replace the unit with the band table. **Propagated**: §2.2's verdict line names the replacement.
- §3 says "N sides is architecturally blocked at the `Bout`"; §5.3 and W-E1 unblock it; §8 E5 limits the compare-type case. **Consistent**; §5.5's table says "after phase E".
- §1.2 row 1's "faculties 0–3 are a no-op below 4 except through pool size" is stated for the *lower three edges*; the Overwhelming edge moves at faculty 3 (P(O) 0.213 → 0.348). The row says so. **No early summary prints the stronger claim.**
- The vocabulary count in §5.7 (31 out, 17 in) was tallied from Part 3's items after Part 3 was written; `LOWER_STANDING` is in neither list (never added, W-F2). **Re-counted, holds.**
- `09_PRESCRIPTION.md`'s "Tier 3, do not execute the proposals as written" — this plan does not execute them; it takes one object from each (`settle`, `burden`, `unanimity_required`) and rejects one from each (`SUCCESS_UNIT`, `restricted`, `holdout_rounds`/`on_hung`). **Consistent with `05`'s dispositions.**

### §12.2 9b — the seventh false N-line, turned on this document's own additions

| my addition | the pattern's question | verdict |
|---|---|---|
| `Issue` + `resolve_issues` | is a bundle already carried by `queue_scene` chaining or by one long `Bout`? | **stands** (§5.7: no shared runtime, no conditions, cap 3 / one `adv`, one label) |
| `Issue.condition` | is a condition an act's `requires` clause upstream? | under PR #362, a condition on *the caller's* act is `requires`; but the *effect on another issue's outcome* has no carrier there — `requires` refuses an act, it does not concede a matter. **stands, at MEDIUM**: if the rebuilt seam expresses "concede X on Y" as two acts with `requires`, the tuple is a second home and should go |
| `Adjudicator.disposition` | is a per-member lean already `character()` (ethos/pathos/logos) or `discipline`? | `character` feeds resonance (`resolver.py:326`), `discipline` feeds leak and bench-weight; **neither reaches the ballot** (`:139/:144` read `gap` and noise only). No producer exists for the field (a bench is authored, `modes.py:113`). **stands, at MEDIUM — the addition closest to the pattern**, and the one `05` §2 and `08` §1.3 independently called necessary |
| `BAND_TO_OUTCOME` / `degree_of_margin` | is this a second ladder? | a table from a band vocabulary into the owner's, precedent `_winner_and_degree`; it bands a *track position*, the owner bands *net vs Ob*. **stands** |
| `venue:` on the row | does `**venue_overrides` alone do the job? | overrides are per call; the row is what a proceeding *is*. **stands** — but it is only load-bearing once W-G2 assigns a non-`None`; until then it is a pointer to nothing, which is why W-G2 is Jordan's and not this plan's |
| `Reserve.refund` | a mutator for a write that already exists | **stands** (it deletes a bare assignment) |
| cut, against myself: a `Bundle`/`Contest` class with a `resolve` loop (T-i); a `faults_reset_per_issue` flag (no producer; §8 E6); an N-sided division rule (a `[SEED]` with no precedent; W-E1 refuses to ship it) | | |

### §12.3 Attacks that failed, reported as failed

| attack | result |
|---|---|
| `id()` keys get recycled to a different judge after GC | **did not reproduce** in CPython 3.11 (§0.6); consequence 3 of `10_` §1.6 stays inference |
| `hard` is never licit on any canonical proceeding | **inverted** — licit before `crowd` (two proceedings) |
| `draw` is reachable on some shipped bench | **failed** — every shipped bench is odd; 0/12,000 at 5/7/15 |
| the band table cannot reproduce canon's middle band | **failed** — it *is* canon's middle band; 29.5 % at 1v6 |
| `SUCCESS_UNIT` could reproduce it at some value | **failed by measurement**: the owner's Partial window is one unit wide; canon's `committee` is 1.33 adv wide at scale 1.5 — no single divisor makes `degree_from_net` produce a two-sided middle *and* the outer bands at 2 and 4 track units |
| the fold cascade needs a rule | **failed** — a carried `FaultState` clinches at move 1 with zero rules (executed) |
| the paired measurement was the coordinator's counting error | **failed** — reproduced at N = 2,000 with the tuple unpacked correctly |
| `support`-forever is a dominant defensive line under `ProofBar` | **inverted** — loses 500/500 (both venues) |
| CR4's die is positive at every pool under the extension | **failed** — +0.000 at 9, negative at 13 and 17 |
| first-mover / side-A bias | **failed** — mirrors symmetric within noise (own 5v5 runs; inherited 12,000 + 4,000) |
| the two campaign goldens control the armature | **failed** — `build_contest` cannot pass one; the sign inversion is invisible to both until W-B2 |

### §12.4 Null results, with the evidence of the look

`[NULL: Key construction or emission inside the package]` — `grep -rn "Key(\|KeyLog\|\.emit(" systems/social_contest --include=*.py` → nothing. `[NULL: persistent state written by a Bout]` — every mutable object constructed in `Bout.__init__` (`resolver.py:239-270`), `Contestant` write-once (`:180-195`); the one cross-package write is `parliamentary_vote.py:214`, faction-scale. `[NULL: a resolver hiding in dictionaries.py or modes.py]` — read; every factory returns a `Venue`/`ContestedMode`/`WinCondition`. `[NULL: a research-sourced number in the kernel]` — spot-checked `resolver.py:35-44`, `primitives.py:33,50,209,214,233,241-242,255-256,295`, `armature.py:228-229,336`, `narrative.py:30-32`; each is `[SEED]` or cites a params row. `[NULL: a disjunctive `ck()` beyond the two known]` — 383 `ck(` lines; two carry ` or ` (`:80`, a conjunction of named cases, sound; `:182`, vacuous, W-F1 rewrites it); one `ck(…, True)` inside an `except` (`:439`, sound). `[NULL: a fractional pool reaching `roll_pool`]` — `Pool.size` is integer for integer faculty and `_as_contestant` coerces `int()` (`wrapper.py:98,:100`); a float faculty passed to `Contestant` directly would round at `sigma_leverage.py:294` — not reachable from the API.

### §12.5 What would make this document wrong

1. **`_kernel_tests.py` was not audited check by check** (383 lines scanned for two shapes only). If a meaningful fraction of the Stage-3 checks are vacuous, W-A8's "keep the stage-3 measurements" preserves less than it claims and the armature is "unvalidated and untested" rather than "unvalidated". The single most valuable follow-up, and it needs no tooling.
2. **The fold prototype shared the runtime by monkeypatching `b2.c = b1.c`**, not through W-D1's parameter. The behaviour is the same by construction (the attribute is the only reader), but the parameter has not run.
3. **The nine-issue expectations (§5.4) assume per-issue independence.** In a real fold the jitter draws are independent but the bench and Standing are shared, so components are mildly positively correlated and the counts spread a little wider than the binomial. The direction of the argument (texture needs independent accumulation) does not depend on it; the exact expectations do.
4. **The N-sided division is unshipped and its rule is a `[SEED]`** (W-E1). Requirement (4) is met for "both win" and "N orators vs bars", and only pairwise for a shared divisible stake, until Jordan rules E5.
5. **`level("minor")` for CR4's δσ (W-B2) is a `[SEED]`**; the *form* is CR6's, the *magnitude* is a guess. A Jordan tuning, flagged at the literal.
6. **Everything in Parts 2–3 is paper** (`CLAUDE.md` §0.2). The measurements executed; the repairs have not. The grade changes at each phase's named artifact, not at merge.
7. **`[SELF-AUTHORED — bias risk]`**: this pass grades four proposals and two audits from the same session and concurs with their central verdict (one game, four terminals) — the direction an author is least inclined to attack. The independent check an outside reviewer would add: whether §5.1's fold is genuinely smaller than a per-issue key inside one `Bout` (rejected option (a)) *once phase E lands*, since E touches many of the same sites (a) would have. My answer is that (a) still makes the `Bout` a container with a loop (T-i) and E does not; a reviewer should test that rather than take it.

---

## Appendix A · Out-of-scope observations, one line each, uninvestigated

1. *(seam)* `scene_dispatch.py:118 EMERGENCY_COUNCIL_PROCEEDING = "guild_arbitration"` and `:139 (max(1, round(f.L)), max(1, round(7.0 - f.Sta)))` — the two integers every §1.2 measurement was fed; the rebuilt seam decides what a council *is* (`09` §2's one surviving question).
2. *(seam)* the seam unpacks `resolve_contest`'s tuple at `:301` and discards the `Bout`; W-C1 keeps the tuple shape for exactly that line, and `Bout.last_outcome`/`resolve_issues` are what the rebuild should read instead.
3. *(seam)* whether a self-contest's B-win writes `Failure` to the acting faction's own `L` (`06` §13's one surviving item) — Jordan's, about the rebuild, not this plan.
4. *(FA lane)* inquiry's B2/B4 (`systems/factions/sim/tribunal.py:73,:102`; `KeyLog.of_type`) are owed before any inquiry scene can open; W-F2 does not depend on them.
5. *(prose)* `social_contest_system_v2.md` (+index, 513 lines) is banner-superseded and still in the live folder; a prose pass, not a code item.

*End. One file. Nothing else was created or edited.*
