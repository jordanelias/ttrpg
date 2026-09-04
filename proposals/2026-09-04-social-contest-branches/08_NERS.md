# 08 · PESSIMISTIC STEELMAN NERS — the social contest as it executes, and every proposal this session made about it

## Status: **AUDIT — read-only, PROPOSED disposition of findings, 2026-09-04. HELD BACK IN FULL. Nothing ratifies on merge. This file is the only artifact; no other file under the repo was created or edited.**
## Auditor: Fable 5.1, `CLAUDE.md` §10 audit/guardrail node. Branch `claude/social-contest-system-review-dn2y5d`, HEAD `2b32c24d`.
## Method: `proposals/2026-08-31-unified-code-shape/14_NERS.md` (the charter and its three rules plus the meta-rule) and `proposals/2026-08-31-ideal/04_ners_audit.md` (the worked pessimistic pass). **E is a ratio against N and R, never an axis. S is a ladder test, both halves. R binds only at seats a player can occupy. A fix that adds a system has failed.** `04_ners_audit.md`'s "P-1..P-5" are defined nowhere in the tree and are not used here.
## Grade of the subject under `CLAUDE.md` §0.2, stated first: **one game executes (`agon`, on one proceeding, with defaulted policies, between two integers derived from one faction's own stats); everything else in `systems/social_contest/` is test-only or dead, and every proposal in this directory is paper.** The measurements that license each half of that sentence are in §0.3 and §11. **Under the rolling-engine diagnostic (§12) the production path is a wrong-engine defect in the skill's own words, and its one working leverage channel is dead at the input the seam passes 82 % of the time.**

---

## §0 · Status, method, reading log, and what was executed

### §0.1 What was read, in order

1. `SESSION_BRIEF.md` (1,015 lines; the orchestrator's ground, with its own four self-corrections) and `SC_INVENTORY.md` — treated as maps, every load-bearing anchor re-opened.
2. `14_NERS.md` and `04_ners_audit.md` in full — the method.
3. `05_RECONCILIATION.md` in full; `06_SYSTEM_AUDIT.md` in full; `07_TOPDOWN_BOTTOMUP.md` in full.
4. `00_BRANCH_SHAPES.md` §0, §0.1, §1, §2, §7 in full; `01_SPINE.md` §0, §1.8, §2 (D1–D9, A1–A2), §4, §5, §9 in full; `02_NEGOTIATION.md` §5.2–5.4, §7, §8, §10.2–10.3, §12.5; `03_INQUIRY.md` §5, §7, §8, §10; `04_CONSENSUS.md` §5, §7, §8, §10. Section maps of all five. **I did not re-read the four branch documents end to end**; where I grade a claim of theirs I read the section that makes it.
5. **Every `.py` I cite**, read this session: `systems/social_contest/sim/contest/{resolver,primitives,contract,policy,wrapper,modes(:325-577),faction(:40-154),armature(:405-451),rhetoric(:200-235),degree_extension(:49-100)}.py`, `sim/parliamentary_vote.py:40-220`, `contest_legacy_stub.py:55-75`; `engine/cross_scale/{scene_dispatch(:60-150,:150-240,:280-470),echo_transport(:380-460),parliamentary_bridge(:85-190),domain_echo(:79-124)}.py`; `engine/mc_v18.py:55-95,:100-175,:230-325`; `engine/autoload/game_state.py:70-200`; `engine/autoload/dice_engine.py:95-140`; `engine/substrate/{composition(:40-75),keys(:510-600)}.py`; `systems/settlements/sim/ledger.py`; `engine/tests/{test_echo_transport(:95-118),test_mc_v18_regression(:1-60),test_f7_smoke_oracle(:1-40,:340-348),test_pipeline_reach(:825-895)}.py`.
6. `CLAUDE.md` §0, §0.05, §0.1, §0.2, §0.3, §10; PR #362 `04_CODE_ARCHITECTURE.md` §C.5, §C.5.1 (`:677-720`).
7. The prior verdict: `v30-snapshot-2026-06-28:designs/audit/2026-05-28-resolution-diagnostic/ners_verdict_social_contest.md` and its companion `resolution_diagnostic_social_contest.md` (§1 component table, §2–§8); `…/2026-06-01-contest-redesign/RATIFIED_2026-06-01.md` (CR1–CR7).
8. `registers/editorial_ledger_sc.jsonl` (all 32 rows, ids/status/needs_jordan), `registers/handoffs/HANDOFF_SC.md` (grep for SC3/SC4/SC5: no hits).

### §0.2 Method

Per axis: the rule that governs it, then the verdict, then the artifact. Every number below names the script that produced it (§0.3). **Where a claim could be measured it was measured; where it could not, that is said.** Attacks that failed are in §9. My own skepticism is audited in §10, including the one measurement I chose *not* to run because it would have favoured the subsystem.

### §0.3 Execution artifacts — scratchpad only; no repo write, no `pytest`

All scripts and logs live in the session scratchpad (`ners_ablate.py`, `ners_kernel.py`, `ners_kernel2.py`, `ners_kernel3.py`, with `.log` outputs and `ners_ablate_out*.json`). Nothing was written under the repository except this file.

| artifact | what it measured | headline |
|---|---|---|
| **`ners_ablate.py`** — five arms × 16 seeds × 50 seasons of `mc_v18.run_campaign` (80 campaigns), then arms A/E/C × seeds 16–63 (144), arm B × seeds 16–63 (48), and **arm P, a positive control, × seeds 0–63 (64)** — 336 campaigns | **the necessity question.** A baseline · B council-echo apply suppressed (Key still logged, contest still runs, `world.rng` consumption preserved until the first effective write) · D §10-vote writes suppressed (its dice still rolled) · E both · C council trigger never fires. Plus per-council `(season, faction, faculties, verdict)` and per-write `(before, after, no-op)` | **4,979 councils / 64 campaigns: 87.7 % won by the crisis side; side-A faculty = 1 in 81.9 %; 74.8 % of council echoes are floor/ceiling no-ops; 0.39 effective council writes per season.** At n = 64: no arm — **including the positive control** — moves who wins detectably; on the stat the subsystem writes, the council echo is a measured drain (arm B) and the vote a measured pump (arm E). §1.1, §8.1 |
| **`ners_kernel.py`** — ~340k kernel bouts | P(A) grid on the production venue; shipped-policy spread at the live inputs; an **open-loop best-response sweep over the full move grammar** (343 sequences × 2 sides); `weighted_by_standing` vs `simple_majority` paired; mirror symmetry N=4000; SC4's shape on an 8-exchange venue; consensus F1 and the split identity | at the live inputs (A=1 vs B=6) the best line in the grammar buys **8.0 %** against 6.5 % baseline; at fair inputs a single solved choice (ethos → logos → logos) is worth +12 pts and the reply restores 52/48; `weighted ≡ simple` in **3000/3000**; no first-mover bias (2011/1989) |
| **`ners_kernel2.py`** — ~70k bouts | SC3's successor (CR4's +1D and the armature δσ on a directly built bout where they ARE reachable); the inquiry `restricted` field's N-line under `ProofBar` and under the reachable `church_tribunal`; SC4 on the canonical 5-exchange venue; SC5 by reading | **an accused who stalls loses 1500/1500** under `ProofBar` and 1496/1500 `A_total` on `church_tribunal` — the field guards a non-exploit; CR4's die: 0.486 → 0.477 (inert); armature δσ: +11–15 pts |
| **`ners_kernel4.py`** (`ners_kernel4.log`) — ~230k bouts | the second instrument's P-ii/P-iii check: the σ-scaled δσ channel vs the flat +1 die across pool sizes; per-point faculty leverage on the production venue; **the falsifier — the same δσ under the live discrete draw vs the videogame-canonical continuous draw**; the `net_boost` staircase | **the armature's δσ is quantized away at the live input:** at faculty 1 (pool 5) maximal alignment moves P(A) by **+0.000** on the live discrete draw and **+0.199** on the continuous draw; at faculty 2 by +0.213; the channel acts only through `floor(net_boost)`, which is 0 at faculty 1 and 1 at every other faculty. §12 |
| **`ners_kernel3.py`** — ~180k bouts | the CR4 die's SIGN under the ruled `PoolDesaturation` extension vs the owner's bare ladder, at three pool sizes and two benches; the degree distribution with and without one die | **under the ruled extension the canon "+1D" is −3.6 pts at pool 13 and −5.6 at pool 17 (+8.3 at pool 7); under the bare ladder +3.7/+1.9/+8.3.** Overwhelming falls 9,133 → 7,502 per 20,000 receptions when a die is added. §2 row 4 |

Bouts are ~0.3 ms; a 50-season campaign is 6.5 s. Total: ≈ 830k bouts and 336 campaigns (a duplicate `16:64 A,E,C` run launched by the coordinator in parallel produced identical content and is not counted).

### §0.4 One method note

`06_SYSTEM_AUDIT.md` measured two seeds and said in its own §14.2 that a seed with a high-`L` crisis faction would move its 97 % (side-A faculty = 1) figure. Sixteen seeds move it to **81.4 %** (1,040/1,277), and 161 councils sat with side A at faculty 6–7 and won about half of them. The structure `06` read off the code holds; two of its numbers were two-seed artefacts, and it said so first. I repeat the discipline: the n=16 arm comparisons in §1.1 are per-seed facts; the *distributional* claim waits on the n=64 run (§8, marked where pending).

### §0.5 ⚠ The rubric changed mid-audit — what moved

After §1–§11 were drafted against `14_NERS.md`'s shorthand, the coordinator relayed the canonical NERS definitions in Jordan's own words from **PR #364 (OPEN, unmerged), which adds `CLAUDE.md` §0.06** — the definitions had no home in the tree (`canon/definitions.yaml`, cited by two skills since 2026-06, never existed; ED-929). Cited here as `PR #364 (proposed) CLAUDE.md §0.06`. They are materially wider than the shorthand, and four things in this document moved because of them. The measurements did not move; the rubric they are scored against did.

| §0.06 clause | what it adds to the shorthand | where it lands here |
|---|---|---|
| **N** is tested *from all directions* (top-down · bottom-up · vertical · diagonal · lateral · horizontal) and is defined *through* E, R and S; *an N-line holding in exactly one direction is a narrowed one, not a passing one* | my ablation is a bottom-up instrument; the other five directions were argued or absent | §1.4 (new), §8 |
| **R** has three halves — the player's strategic choice (seat-scoped), *emergent and compelling hooks and scenarios WITHOUT player involvement*, and *mechanics fully formed, error-free, and complete* — and a blocked seat question *never makes R unscorable, only part of it* | **the coordinator's earlier instruction that "R is not scorable" is a legitimate blanket verdict was wrong, and §4 as first drafted followed it.** Rewritten: the player half is not scorable; the other two are, and both fail | §4 (rewritten), §8 |
| **S** carries *calculations consistent in methodology with sibling mechanics* (two ladders for one quantity is an S defect even when each is correct) and *pauses correctly when another system or scale is called for* | both tests were absent from §5 | §5 (extended), §8 |
| **E** is two tests — *no unnecessary overhead* **and** *allows the player to intuit complex outcomes from simple choices* — and a mechanism can pass the first and fail the second; E-as-a-ratio is restated in the same words | §3 scored tidiness only | §3.3 (new), §8 |

| **the second instrument** — `skills/valoria-resolution-diagnostic/SKILL.md` (rebuilt by PR #363, in the working tree): the rolling-engine property test (P-i…P-v), the ENGINE-SELECTION DECISION RULE and the Stage-0 calibration | not pointed at in the brief; applies to any component that resolves by a draw, which the contest does | §12 (new) — and it found, by measurement, the defect in §12.2 that none of the four rubric axes had a name for |

The re-grades are recorded as re-grades, not silently applied; §8 carries both the original verdict and the §0.06 one where they differ.

---

## §1 · N — the N-line for every object, live and proposed

Rule: *cut it, and the emergent possibility lost is ____.* No object enters without one. An object whose N-line names a possibility that survives the cut is in §2, not here.

### §1.1 The live subsystem — the two things that execute, first

**The Emergency Council** (`scene_dispatch.py:76-100 evaluate_triggers` → `:121-139 _emergency_council_parties` → `:300 build_contest(parts[0], parts[1], venue="guild_arbitration")` → `:301 resolve_contest(built)` → `:336-345` echo block → `echo_transport.py:441-455 _apply` → `game_state.py:153 Faction.adjust`).

- **N-line as claimed** (`scene_dispatch.py:110-139`, scale_transitions §5.2): a faction's internal crisis is *resolved by argument*, with the leadership's legitimacy and the crisis's strength as the two cases.
- **What it provides, measured** (`ners_ablate.py`, arm A, 16 seeds): a council fires every season a faction has `Sta ≤ 2` (`:84`), with no hysteresis; **Crown sat in council 45 consecutive seasons in 7 of 16 seeds** (a council fires 1.6 times per season on average across the four factions). Side A's faculty is `round(L)`, which is 1 in 81.4 % of councils; side B's is `round(7 − Sta)`, 5–7 always. The crisis side wins 1,114/1,277 (87.2 %). The echo writes `Failure → −1` or `Success → +1` to the faction's **own `L`** (`:344-345`, `domain_echo.py:106-114`), and `Faction.adjust` clamps at 0 and 7 (`game_state.py:195`): **912 of 1,114 negatives landed on a faction already at 0; 47 of 163 positives on a faction already at 7. 959/1,277 (75.1 %) council echoes changed nothing.**
- **At n = 64** (`ners_ablate_n64.log`): 4,979 councils, crisis side 87.7 %, side-A faculty = 1 in 81.9 %, 74.8 % of echoes no-ops, **0.39 effective council writes per season**.
- **Cut it (arm B, RNG-preserving until the first effective write):** 2/64 campaigns end in an identical state; 23/64 keep the same winner. So it is *not* inert — a quarter of its echoes move `L`, and `L` feeds the vote's Mandate pool (`parliamentary_vote.py:169`), `faction_take_action`'s weights and the fallback score (`mc_v18.py:295`). **Measured, paired by seed at n = 64: removing the council echo raises Varfell's final `L` by 0.83 (t = 3.07) and Crown's by 0.44 (t = 2.12) — the council is a systematic Legitimacy DRAIN on factions in crisis** (the 25 % of `Failure` echoes that land on `L > 0`). **It does not detectably change who wins (χ² = 4.48 on 3 df, p ≈ .21), and §8.1 shows nothing on the `L` channel could.** The possibility it provides is that drain: a state-dependent −1 on the crisis faction's `L`, about 0.4 times per season.
- **The possibility survives the cut**: the grid (`ners_kernel.py` §1) shows the council's outcome is a function of two integers — P(A) = 0.09/0.08/0.05 at faculty 1 against 5/6/7, rising to 0.58 at 7. A two-parameter Bernoulli table drawn from the same reseeded stream reproduces it in distribution, by construction. **Nothing in the kernel — six move kinds, five judges, resonance, readiness, standing, room, the fault catalogue — reaches the campaign except through that scalar.** That is the finding the necessity question asked for, and it is stated in full in §8.
- **The one structural fact that makes the ritual a ritual:** the trigger reads `Sta` (`:84`) and the echo writes `L` (`:345`). **The mechanism cannot clear its own trigger condition by construction.** No hysteresis is needed to see why a crisis council recurs 45 seasons; a store would be a false N-line for that fact (§2 row 7).

**The §10 Parliamentary Vote** (`parliamentary_bridge.py:90-107 _derive_vote` → `parliamentary_vote.py:125-220` → `:214 adjust("L", −1·MULTS)` synchronous; winner echo `:176-184` deferred).

- **N-line as claimed:** parliament decides motions by Mandate pools, with abstention resistance and lobbying.
- **What it provides, measured:** every season two eligible factions exist, the proposer is the lowest-`Sta` faction and the establishment the highest-`L` (`:97-99`); `lobbying_offset` is always 0 and `parliament_dominant_genre` always `None` (`:103-104`). The loser penalty landed on a faction already at 0 in **143/183 (78.1 %)**; the winner echo (+1/+2) landed on a faction already at 7 in **234/431 (54.3 %)**.
- **Cut its writes (arm D, n = 16):** 0/16 identical, 6/16 same winner. **At n = 64, arm E (council and vote writes both suppressed) lowers Crown's final `L` by 0.77 relative to A (t = 2.77) — net of the council's drain, the vote's winner echo is a systematic Legitimacy PUMP on the establishment**, which is the highest-`L` faction by construction (`:98-99`) and is usually Crown. **Its N-line is real and thin:** a Mandate-pool coin whose two writes are mostly clamped, whose net effect is a rich-get-richer on one stat, with no choice by anyone (the genres are constants, `_SIDE_A_GENRE`/`_SIDE_B_GENRE`).

**Both cut (arm E):** 0/16 identical, 6/16 same winner. **Whole-subsystem write census, 16 campaigns:** 1,891 attempted writes, 1,336 no-ops (70.6 %), 555 effective — ≈ 0.7 per season across four factions.

### §1.2 The live subsystem — the objects behind the two things that execute

| object | N-line: cut it and you lose… | verdict, with the artifact |
|---|---|---|
| `Bout` + the exchange loop (`resolver.py:238-466`) | argument content mattering to the outcome | **Real in the kernel, unreachable from the seam.** At fair inputs the open-loop sweep finds a +12-pt line (ethos → logos → logos, 0.657 vs 0.537) and the shipped-policy spread is 0.605 (`build_then_close` 0.605 vs `staller` 0.000). **At the live inputs (faculty 1 vs 6, 81 % of councils) the best sequence in the 343-sequence grammar is 0.080 against a 0.065 baseline (N = 400 each; the gap is within one standard error), and the spread among shipped policies is 0.096 at N = 1000.** The N exists; the seam passes neither a policy (`:301`) nor a faculty above 1 |
| `Move.appeal` (ethos/pathos/logos) | the appeal–venue fit | **Real, one solved choice.** Ethos-first dominates on the production bench (three of the top four sequences open with ethos); B's best reply is the same line and restores 52/48. Reactive policies were not swept (§10) |
| `Venue.joint_weight` / `Adjudicator.character` (`resolver.py:172-178`, `contract.py:34`) | the venue deciding which appeal lands | **Real and invisible to the player** — `ContestView` (`contract.py:53-66`) exposes neither. `06` P4.3 |
| `VoteAtClose` weighted aggregation (`resolver.py:128-142`, ratified ED-1057) | a heterogeneous bench that need not mirror its highest-weight juror | **Nothing on any constructible bench.** 3000/3000 paired bouts agree with `simple_majority` (`ners_kernel.py` §4). Every factory builds homogeneous members (`modes.py:440-461`). `06` L6.1, now executed |
| `PersuasionTrack` (`resolver.py:81-95`) | the committee band | **Provided, and it eats everything at equal faculty:** `formal_contest` logos-mirror 996/1000 committee, `grand_contest` 991/1000, `royal_audience` 874/1000; at 3 v 7 `formal_contest` is still 949/1000 committee. Only `demagogue` before a `crowd` leaves the band (348/1000). Not on the production proceeding at all (`guild_arbitration` → `VoteAtClose`) |
| `Reserve` / Concentration (`primitives.py:49-56`) | stamina as a choice | **Nothing at budget 3** (12 → 9 → 6 → 3; `_low` never fires); one free `support` at budget 5; a yield-clinch economy at budget 8 that no canonical proceeding ships (`modes.py:485-519` max is 5) |
| `Standing`/`Face`, `Room`, `Readiness` (`:31-47`, `:232-260`) | the build-then-close arc | Real in the kernel (`build_then_close` is the best shipped policy on the production bench); Face never moves in production (`06` D12.1) |
| `Stasis` ladder + `shift` (`:11-25`, `resolver.py:352-358`) | reframing terrain | no production policy shifts; `fallback_ladder` scores 0.002 when it does |
| `DefeatCatalogue` (`primitives.py:262-279`) | losing by fouling | reachable only via `pass`/`hard`/off-ground/`rebut`, none issued in production; iterates `(A, B)` only (`:273`) |
| `EvidenceItem`/`Dossier` | hidden proof | no production dossier (`wrapper.py:97-98`); `evidence` with no dossier is a **free no-op move** (`resolver.py:361-362`) — the one costless skip in the grammar |
| the armature (`armature.py:415-451`) — δσ, CR4 die, CR5 | the Style card mattering | **δσ is real: +11–15 pts at perfect alignment (0.486 → 0.595/0.634). CR4's die: inert-to-negative (§2 row 4). CR5: a Face cost with no upside (mean Face 4.76/4.70 vs 5.00, P(A) unchanged) — ED-SC-0021's "Obscuring is dominated" confirmed by measurement.** Unreachable from the seam (`wrapper.py:110` has no `armature=`) |
| `Panel` (`contract.py:37-51`) | a bench that is more than one judge | a homogeneous bench is one judge N times — every factory is homogeneous |
| `scene.contest_resolved` Key (`echo_transport.py:427-439`) | a durable record | `participants: []` on every live emission, no consumer (`06` K2.1); the log hash moves on a clamped no-op (K2.4) |
| `GAMES` (`wrapper.py:236-245`), `game=` | a switch | one row wired, the parameter never passed — no possibility |
| the venue library (`modes.py:66-325`), `INSTITUTIONAL_MODES`, `CROSS_CULTURAL_VENUES` | eight proceedings that differ | `proceeding_venue` passes no `**o` (`:567`); every proceeding inherits `Venue`'s defaults (`06` F1.1). ~260 lines, no possibility from the seam |
| `MECHANICS`, `TRACKERS`, `_derive_resistance`, `Contest.primary_attribute/track_start/resistance` | — | display or self-description; `resistance` is computed and read by nothing (`wrapper.py:75-79`). **No N-line is claimed by their own comments**; they are not false N-lines, they are objects without one |

### §1.3 The proposals' objects

| object (document) | N-line as stated | verdict |
|---|---|---|
| `WinCondition.margin()` (01 §5.1) | a contest that feeds the one ladder | **holds** — the kernel throws a margin away at every return (`00` §1 "margin already exists one field deeper") |
| `SUCCESS_UNIT` ×6 (01 A3) | the ladder's answer being meaningful | **false N-line — §2 row 2** |
| `ContestOutcome` (01 A1) | a caller that can tell a stub from a result | holds (two return shapes today, `wrapper.py:254-259`) |
| `ContestOutcome.veto` as a side (01 §1.4) | a fault-out win | **holds** — attacked in §9: a clinch returns `other(loser)` (`resolver.py:461`) while the leader may be the faulter; under a margin-only return nothing else carries it |
| `ContestOutcome.band` | nothing (its own admission) | not an object; a deletion-dated compatibility field |
| `burden` on `PROCEEDINGS` (01 §1.5, 03 §5.1) | *silence convicts* | **holds as a selector — but see §2 row 1: the thing it selects (`ProofBar`) already convicts silence, so the branch that adds a second guard for the same fact is the one carrying the false N-line** |
| `armature=` passthrough (01 §1.7) | every Stage-3 mechanic from the seam: CR4 terrain, CR5 backfire, the judge's convictions | **holds for one of three at fair inputs and for none at the live input.** The δσ is real at faculty ≥ 2 (+11–21 pts) and **exactly zero at faculty 1**, which the seam passes in 82 % of councils — quantized away by the discrete draw (§12.2). CR5 is a pure cost (measured). **CR4's die is negative at every canonical faculty ≥ 5 under the ruled extension** (§2 row 4). The N-line is one-third right at fair inputs and nil-or-negative at the live one |
| `rng` injection (01 §1.8) | same-seed reproducibility through the seam | holds; the three-draw-site enumeration (`resolver.py:32, :139/:144, :334`) is complete (`06` §15 confirms; `policy.py` imports no `random`) |
| `contestant_from_person` (01 §2.5) | a Person as a claimant | **no producer** — `grep` for `Person\b`/`PersonId` in `engine/` + `systems/`: only `systems/world/sim/npe.py:126 class NPC`, never generated on the loop (`mc_v18.py` stub-flags `generate_npc`). The spine downgraded it itself; confirmed |
| binding-in-scene I-S6a/b (01 §1.9) | time inside a season | holds; and `06` §14.3's objection to the §7.4 falsifier is **confirmed by count** — 912/1,114 negative council echoes land on `L = 0`, where a binding write and a deferred one are both no-ops |
| `settle()` (02 §7.2) | a positive-sum division | **holds — I could not cut it.** Nothing in `resolver.py` (six win conditions return a side or band), `ledger.py` (a store), `treaty.py` (a store + lapse roll) or `faction.py:117` (side-asymmetric, succession only) divides a stake |
| `SHARE_BY_DEGREE` (02) | any reward for winning the exchange | holds (verified: `split(−m) == 1 − split(m)` on 101 points; the live `faction.py:107,117` table gives `(b,.60) (b,.55) (a,.55) (a,.55) (a,.50) (a,.50)` at t = 4.0/4.6/5.0/5.4/5.6/6.0 — the anti-monotone defect reproduced) |
| `Settlement`/`Refusal` (02) | a caller that can tell a bargain from no bargain | holds as a typing choice; not the store pattern |
| A's own `commit` Tenure (02 §7.2 row 4) | a visible breach | **false as stated — §2 row 5** (05 F3) |
| `Grudge` on refusal (02 §7.3) | a refused deal leaving any trace | **not false, unwritable:** a `LedgerTag` lives on `Settlement.ledger` (`ledger.py:14`) and the scene carries no `place` (`scene_dispatch.py:89-95`); `06` PR8.2 |
| `restricted` on `Venue` (03 §5.4) | an accused convicted for saying nothing while appearing to speak | **false N-line, measured — §2 row 1** |
| `bar` on the row (03) | the standard of proof | holds (a constructor argument moved, zero net objects) |
| the third grounds clause (03 §5.3) | a filing that must be earned | holds as a restoration; B2's regression (05) stands |
| the `"inquiry"` dispatch arm (03 §5.6) | the case running at all | wiring; 05 §15.4 notes `scene_dispatch.py:346` already carries `investigation` |
| the finding write (03) | an institutional fact that binds whether or not anyone was convinced | holds — the one genuinely new behaviour in the branch; needs a payload builder (B5) |
| `unanimity_required` branch (04 §5.2) | a body that cannot act until all assent | holds as a rule; **inoperable as written** (B1 — reproduced: margin ∈ [−1, 0] bands `Partial`/`Failure` at every scale, `ners_kernel.py` §7) |
| `Ballot`/`BallotBook` "named holdout" (04 §5.3) | a signed block, an antibody target, a Grudge recipient | **no producer of identity** — members are exchangeable; the "name" is a draw index (05 F6). Same class as `contestant_from_person` |
| `consensus_body_venue` + `holdout_rounds` K (04 §5.1) | the dial between the Great Law and the Sejm | **false N-line — §2 row 3** |
| `on_hung ∈ {defer, majority}` (04 §5.5) | a terminal for a hung unity | **false N-line — §2 row 3** |
| the recusal (04 §5.4) | the alignment gradient itself | **false — §2 row 6** (05 F4) |
| antibody channels 1–3 (04 §5.4) | a consensus that punishes frivolous blocking | **all three inert** (05 §2), confirmed by reading: `DefeatCatalogue.check` iterates `(A, B)` (`primitives.py:273`), `Panel` carries no `FaultState` (`contract.py:37-51`), `Stasis.relevant` is strict equality (`primitives.py:21`) and every shipped policy but `off_ground_chancer` argues `v.live_ground` (`policy.py`) |

### §1.4 N from all six directions (`PR #364 (proposed) CLAUDE.md §0.06`)

The ablation is a bottom-up instrument. §0.06 tests N *from all directions* and says an N-line holding in one direction is narrowed, not passing. The whole subsystem, direction by direction:

| direction | question | verdict |
|---|---|---|
| **bottom-up** (primitives → campaign) | does what the kernel computes reach the campaign? | **through one scalar only.** The verdict's side label becomes ±1 on `L`; everything inside the `Bout` is invisible past it. Measured: a real drain/pump on `L` (§8.1), reproduced in distribution by a two-integer table |
| **top-down** (the game as designed → this mechanism) | does Valoria as designed need a social contest? | **yes, by its own definition** — `CLAUDE.md`'s head names personal-scale resolution *fused* with the strategic layer as the game, and canon gives the contest half the personal scale. **The executing game does not read what the contest writes** (§8.1: no `L` perturbation of any size reaches who wins) |
| **vertical** (scene ↔ faction) | does the scene's outcome move the faction, and the faction's state shape the scene? | **one way, one stat, measured** (§1.1). The other way — faction state shaping the scene — is `(round(L), round(7−Sta))` → two faculties; nothing else of the faction enters |
| **lateral / horizontal** (sibling mechanics at the same scale) | what else at the personal scale executes? | **nothing** — combat is behind a default-OFF flag and no trigger queues it (`07` §2.10), fieldwork and threadwork are dormant on the loop (`07` §2.4–2.5). **The social contest is the only personal-scale mechanism that executes at all; cut it and `scenes_resolved` counts only votes.** This is the one direction in which its N-line holds outright, and it holds by default rather than by merit |
| **diagonal** (cross-scale *and* cross-system) | does a contest reach a settlement, a knot, an NPC, a treaty? | **no** — zero references to `ledger.py` in either direction, no `Person`, no consumer of the Key (`06` K2, PR8.2) |
| **through E / R / S** (§0.06 defines N by the other three) | does keeping it make the game more robust, elegant, smoothly integrated? | R: no player choice and no scenario variety (§4); E: legibility vacuous (§3.3); S: two methodology defects and no pause (§5). **On §0.06's own terms the N-line is narrowed to one direction (lateral) plus a measured but unread vertical effect** |

---

## §2 · THE FALSE N-LINES

The pattern (`14_NERS.md` §3): *a mechanism was named, a store was proposed for it, and the store's job was already being done by an object the design had ruled in.* Hunted against the σ resolver, the armature and `ledger.py` as the brief directs, against the session's own cuts, and against my own fixes. **Six fired. A seventh fired against this document's first recommendation.**

| # | object | its claim | why the possibility survives the cut | grade |
|---|---|---|---|---|
| **1** | **`restricted = {"B": ("support",)}` on `Venue`** (`03_INQUIRY.md` §5.4; its §10.2 calls `support` "a dominant defensive line") | without it the accused's dominant line is a free stall and *silence convicts* is decorative | **MEASURED, and the claim is inverted.** `ProofBar.resolve` (`resolver.py:67-73`) reads `adv[A] − adv[B] ≥ bar`; an accused who never advances contributes 0 to `adv[B]`, so an unopposed inquisitor clears `bar = 2.5` in five exchanges every time. On the unreachable `inquisition_hearing_venue` (ProofBar 2.5, budget 8) a support-forever accused **loses 1,500/1,500** at 5 v 5 and 1,493/1,500 at inquisitor 3 v accused 7; on the reachable `church_tribunal` (PersuasionTrack start 6) the stall yields `A_total` **1,496/1,500** and 1,415/1,500. The arguing accused does far better on `church_tribunal` (committee 69 %/`A_decisive` 22 % at 5 v 5; `B_decisive` 25 % at 3 v 7). The `argue`-vs-`argue` rows on the 8-exchange inquisition venue are confounded by the first-mover yield disadvantage (§9 row 2) and are not used; the support-forever rows there are clean because `ProofBar` resolves at every exchange boundary (`resolver.py:462`) and the inquisitor clears the bar before exhausting. *Silence convicts* is not merely preserved by the cut — it is the existing outcome. The mechanism was named, a side-keyed forbidden-move table was proposed, and `ProofBar` plus `Venue.budget` were already doing the job. **What survives of §10.2:** `support` is riskless (no fault, `resolver.py:350-351`) — riskless is not useful. `yield_strikes = 1` (E8) likewise guards a line (`pass`) that already loses 1,500/1,500 at 2 strikes | **FALSE, high confidence — the best finding of this pass** |
| **2** | **`SUCCESS_UNIT` ×6** (`01_SPINE.md` A3, §5.1 "high") | the ladder's answer being meaningful at all; six margins are on incommensurable scales, so each needs a per-subclass conversion into σ-units | **By precedent.** The tree already maps a win condition's *band* to a Degree with zero constants: `parliamentary_bridge.py:110-131 _winner_and_degree` — `passed/failed × total_victory → Overwhelming/Success/Partial`, "READS THE VERDICT, DOES NOT RE-DERIVE IT", with an exhaustive equivalence test. Every `WinCondition` already returns a band (`resolver.py:52-147`); a band → Degree table per subclass is the ruled-in shape, and it mints no number. Six uncalibrated `[SEED]`s that convert a vote share, a track position and a threshold surplus into dice-σ so that a dice ladder can re-band them are a *store of conversion factors* for a job a table does. The spine's own §9.1 calls this "the strongest case against"; its §9.5 says it considered and did not take the alternative; `05` §14.3 notes the hunt was never turned on it. **Conditional:** PR #362 §C.5 demands a `Margin`, not a band; under that contract the constants are forced. PR #362 is HELD BACK IN FULL, and the spine's own recommended mitigation (do not consume `margin()` in S0) is consistent with cutting | **FALSE under the tree as it is; real if PR #362's Margin contract is ratified** |
| **3** | **`holdout_rounds` (K) and `on_hung` on `Venue`** (`04_CONSENSUS.md` §5.1, §5.5, §7.2) | the dial between the Great Law and the Sejm; a terminal for a hung unity that is not a win for the blocker | `on_hung = "defer"` **is** `scene_slate.queue_scene` plus the chain cap of 3 (`social_contest_v30.md:383`) — which the document itself cites as what "defer" does; `on_hung = "majority"` **is** the existing `weighted_by_standing` branch (`resolver.py:128`); K counts re-referrals, which the chain cap already bounds. And neither field exists: `Venue` is a closed dataclass (`resolver.py:150-166`), `Venue(**o)` with either key is a `TypeError` (05 F8). The critic found the "rounds" are K repetitions of an i.i.d. coin with no per-member term (05 F3), so K decides nothing a re-queue does not | **FALSE, medium** — the intra-scene vs cross-season distinction is real in prose and has no mechanism |
| **4** | **CR4's `+1D` primary-genre pool die** (`rhetoric.py:207 CR4_PRIMARY_GENRE_POOL_BONUS`, `:221 primary_genre_pool_bonus`, consumed at `resolver.py:404`; ratified CR4, `RATIFIED_2026-06-01.md`) — **inside the live kernel, and inherited as a benefit by `01` §1.7/§5.1, `03` §5.5 and `04` §5.4** | "a genuine non-dominated choice … BOTH the live stasis AND the orator's Style choice move the outcome" (`rhetoric.py:200-203`) | **MEASURED, and the possibility is provided by the armature δσ alone — the die subtracts from it.** `ners_kernel3.py`, N = 10,000 per cell, mirror 5 v 5 on FACT terrain with `logos_spammer`: under the ruled extension (`degree_extension.py:60-82 PoolDesaturation`, ED-SC-0032) a Memory style on Memory terrain (die +1) moves P(A) **0.504 → 0.447**; the same style under the owner's bare ladder moves it 0.505 → 0.542. The mechanism is visible in the degree distribution (20,000 receptions): with the extension one added die takes Overwhelming from 9,133 to 7,502 and mean degree from 2.308 to 2.251; without it 14,413 → 15,184 and 2.572 → 2.635. **The sign depends on pool size:** at pool 7 the die is +8.3 pts under both ladders; at pool 13 it is −3.6 (ext) / +3.7 (bare); at pool 17, −5.6 / +1.9. `overwhelm_bar(pool) = μ·pool + 1.5σ·√pool` (`degree_extension.py:57`) rises faster than one die's net contribution above the Overwhelming edge. **Consequence for the Style choice CR4 exists to reward:** with an aligned judge on FACT terrain, Vision (Projection, no die) wins 0.636 and Precedent (Memory, +1 die) wins 0.586 — *the Style the terrain "rewards" is the one that loses.* Two ruled mechanisms (CR4's die, ED-SC-0032's extension) compose to invert a canon bonus. **Latent** (the armature is unreachable from `build_contest`, `wrapper.py:110`); **live the moment the spine's `armature=` lands**, which all three branches require | **FALSE — and negative. The store (a pool die) was proposed for a mechanism (the Style bet) that the δσ already carries, and the store's contribution is below zero at every canonical faculty ≥ 5** |
| **5** | A's own `commit` Tenure (`02_NEGOTIATION.md` §7.2 row 4) | a visible breach — "a `Record` has no verb that ends it" | `verb_table.yaml:146-151 destroy_record` exists (05 F3). A narrower N-line may survive; it is not in the document | **FALSE as stated** (confirmed from the critic; not re-derived by me beyond the cited row) |
| **6** | the recusal `Panel(judging_set MINUS the holdout)` (`04_CONSENSUS.md` §5.4) | the alignment gradient itself — with the holdout on the bench, `position_of` returns the zero vector | `opponent_is_adjudicator` is a **caller-set flag defaulting `False`** (`armature.py:415-451`); nothing detects that a member is a contestant, so a seated holdout yields `ArmaturePosition.mean` — a 1/N dilution, not zero (05 F4). The recusal guards a gate that does not fire | **FALSE** (confirmed by reading `ArmatureConfig`) |
| **7** | ⚠ **against this document — a hysteresis store on the Stability-Crisis trigger**, my own first fix for the 45-season council | a crisis council should not fire 45 seasons running; a per-faction "last council season" would stop it | **the possibility survives with no store**: the trigger reads `Sta` (`scene_dispatch.py:84`) and the echo writes `L` (`:345`); a mechanism that cannot touch the stat that fires it recurs by construction. The fix that adds nothing is a one-line choice — key the echo to `Sta`, or the trigger to `L`, or accept the ritual — and which is a design call adjacent to `06` §13's one surviving item. A hysteresis flag would have been *a store for a fact the trigger's own inputs already carry* | **FALSE, against myself. Deleted from §8** |

**Not false — no producer or no home (the `14_NERS.md` §3 row-6 class):** `contestant_from_person` (no `Person`); `Ballot` naming (no per-member term); `Grudge` on refusal (no `place` on a scene).

**The session's own cuts, spot-checked and holding:** `stall_clock` → `ProofBar:71-72` + `Venue.budget` ✓ · `ContestRecord` → `LedgerTag` ✓ · `Case.stages` → `KeyLog` count ✓ · a `verdict` enum → `key_types.json` ✓ · a `Holdout` object → `BallotBook.dissenters` + `Grudge` ✓ · `on_hung: lot` → cut on its fourth argument (05 F5), the lost churn class stated ✓ · a reservation field on `Contestant` → `Tenure.degree`, **conditional on PR #362** ✓.

**Count: 6 against the subsystem and the session, 1 against this document. Best: row 1**, because it is the only one where measurement reversed a document's central dominance claim rather than trimming it.

---

## §3 · E as a ratio against N and R, watched in both directions

Rule 1: never score E alone; never average. The ratio is *distillation ÷ (emergence + choice preserved)*.

### §3.1 The live subsystem

**Bloat (kept despite distillable).** Executable-line reach of a seeded campaign is 35.6 % and that is generous (`06` §12.1, tracer counts definition lines). Kept without a reachable N: six `WinCondition` classes of which production uses one; ~260 lines of venue design discarded at `modes.py:567`; three `GAMES` stubs, `_stub`, `game=`; `MECHANICS` (23 `WIRED` rows the self-test does not exercise); `TRACKERS` (three trackers, one alive); `FaceScale` (raises `TypeError` on the live path, `06` L6.3); `agon_harness.py` 522 lines zero callers; `contest_legacy_stub.py` ~180 dead lines; `faction.py` 154 lines zero production callers; `parliamentary_stay.py` 106 lines 0 hit; `narrative.py`, `appraise.py` uncalled; `_derive_resistance` computing a number nothing reads; `Panel` over benches that are always homogeneous.

**Amputation (over-distilled, the direction Rule 1 exists for).** `ContestView` (`contract.py:53-66`) hides the two things that decide a bout — the venue's proof weights and the judge's character — while the measured spread they produce is 0.6 among shipped policies; `_emergency_council_parties` reduces a faction's politics to two integers from one faction's own stats, floored at 1 (`:139`); the seam passes six of twelve `build_contest`/`resolve_contest` parameters (no venue choice, no policy, no armature, no rng, no `world`, no `record`); the Key carries `participants: []`; the echo writes a self-contest's loss as `Failure` to the actor's own `L`.

**The ratio.** On the live path N ≈ 0 (a two-integer coin, §1.1) and R = 0 (no seat, §4). **A ratio with a zero denominator is undefined, and that is the verdict:** the production path can be distilled to `random.random() < P[fa][fb]` with no loss of emergence or choice, *because there is none to lose.* That is precisely the amputated design that Rule 1 warns an axis-scoring audit would call elegant — and the 2026-05-28 verdict did (§7).

### §3.2 The proposals

| document | what goes out | what comes in | ratio, honestly |
|---|---|---|---|
| `01_SPINE` | `GAMES`, `_stub`, `game=`, `Contest.game`, 3 `MECHANICS` rows, 4 kernel checks, one test (9 deletions) | `ContestOutcome`, `margin()` ×6, `SUCCESS_UNIT` ×6, `rng`, `armature=`, `contestant_from_person`, `burden` (11 additions; 05 §14.3: 11 names in, 8 out) | **neutral, and worse if §2 rows 2 and 4 hold** — six constants for a job a table does, and a passthrough that delivers a negative die |
| `02_NEGOTIATION` | `NegotiationMode`, the `negotiation` row, `faction.py`'s band duplicate | one module, `settle`/`Settlement`/`Refusal` + private `split`/`SHARE_BY_DEGREE` | **moves the right way** — the one addition nothing else does, and it is six lines. Its `Grudge` has no home |
| `03_INQUIRY` | `CHURCH_TRIBUNAL_TRACK_START`, `tracker`, `tracker_mode`, `_use_tracker`, `use_tracker`, `inquisition_hearing_venue`, its registry row, `Record.stages`, `determine.writes: [Tenure.degree]` (10) | `burden`, `bar`, `restricted` (3) | **moves the right way on the count and better once `restricted` is cut (2 in, 10 out)**; the dispatch arm and the finding write are real code, as the document says |
| `04_CONSENSUS` | `coalition_vote`, `run_contest` (offered, not required) | `unanimity_required` branch, `Ballot`, `BallotBook`, `consensus_body_venue`, `holdout_rounds`, `on_hung`, the recusal, three antibody bindings | **moves the wrong way**: five objects protect no N (B1 inoperable, antibodies inert, K/`on_hung` false), and two do not fit the type they are declared on |

### §3.3 E's second test — *allows the player to intuit complex outcomes from simple choices* (`§0.06`)

Added on the rubric change. §3.1–3.2 score *no unnecessary overhead*; this is the other half, and a mechanism can pass one and fail the other. On the production path there are **zero player choices** (§4), so the test is vacuous — **FAIL by absence**. Where a choice would exist (the harness seat, or a future seat through the seam), `ContestView` (`contract.py:53-66`) hides the venue's proof weights and the judge's character — the two inputs that decide which appeal lands (a 0.6 spread, §1.2) — and exposes `can_hard`, which is never licit before any production bench (`06` P4.4), and `evidence_available`, which is always 0. **A player cannot intuit the outcome because the view withholds its causes and shows levers that do nothing.** FAIL on the second test regardless of the seat question. The armature's Style card compounds it: the terrain "rewards" the Style that loses (§2 row 4).

---

## §4 · R — three halves (`PR #364 (proposed) CLAUDE.md §0.06`), the player half per seat

**⚠ Re-graded on the rubric change (§0.5).** As first drafted this section followed the coordinator's instruction that "R is not scorable" is a legitimate blanket verdict pending seat playability. Under §0.06 that scopes **only R's player half**; a blocked seat question *never makes R unscorable — only part of it*. The other two halves bind everywhere and are scored below.

### §4.1 The player half — per seat, playability first (`14_NERS.md` Rule 3)

| seat | playable? | if it were, the measured impact of choosing |
|---|---|---|
| **Side A of the Emergency Council** (the leadership) | **No.** `resolve_contest(built)` is called with no `policy_a` (`scene_dispatch.py:301`); both sides default to `logos_spammer` (`wrapper.py:248`); no player entity exists | at the live inputs (faculty 1 v 6): best open-loop line **0.080** vs 0.065 baseline (within one SE at N = 400); shipped-policy spread **0.096** (best `build_then_close` 0.096, `logos` 0.081, `demagogue` 0.010). B's best reply to A's best: 0.955 for B. **A delegitimised leadership losing its own council 88 % of the time is a portrait, not a defect — Rule 3 applied** |
| **Side B** (the crisis) | **No** | same |
| **A faction in the §10 vote** | **No.** Proposer, establishment and both genres are derived (`parliamentary_bridge.py:97-106`); `lobbying_offset = 0` always; a faction controls nothing in the vote but its `L`, which it moves elsewhere | no choice exists to measure |
| **The harness seat** (`agon_harness.py`, a human on Side A) | **Yes, by a human at a terminal; zero callers; never played** (`HANDOFF_SC.md`). 2–3 prompts per exchange (`06` P4.2) | on its default proceeding (`formal_contest`, crowd, PersuasionTrack) a 5 v 5 logos mirror is **996/1000 committee** — the human's choices decide almost nothing; on `guild_arbitration` the appeal choice is one solved choice (ethos-first, +12 pts), after which the reply restores parity |
| **Negotiation A/B, inquisitor/accused, member/holdout/convener** (the proposals) | **Not until a `Person` producer exists** — none does (§1.3). The documents say so themselves | bounded where measurable: the accused's only non-dominated line is *argue* (§2 row 1); the reservation is a genuine hidden-information bet, unmeasured; the holdout has no per-member term, so there is no seat there at all (05 F3/F6) |

**Player half: NOT SCORABLE on every seat.** Where I could bound the if-played impact it is ~nil at the inputs the seam actually passes, and one solved choice at fair inputs. Every "no dominant option" claim in every document remains an upper bound; the one dominance I measured (ethos-first, open-loop, production bench) is a lower bound on the exploit.

### §4.2 The world half — *emergent and compelling narrative hooks and scenarios WITHOUT player involvement*

Scorable everywhere, and **FAILS.** The subsystem generates *events* — 1.6 councils per season, a vote every season — and no *scenarios*: the same faction sits in council 45 consecutive seasons (7 of 16 seeds), the outcome is the same 88 % of the time, the vote's two poles are the same two factions by construction (lowest `Sta` vs highest `L`) with constant genres, the Key that records it carries `participants: []` and no verdict, no proceeding, no reason (`06` K2.1), and nothing downstream reads it. A hook that fires identically every season and leaves no trace is not a hook. **The one emergent thing it does produce — a Legitimacy drain on whoever is in crisis and a pump on whoever is established (§8.1) — is a rich-get-richer feedback on a stat the outcome does not read, and no narrative surface can see it** (`narrative.summarize` is never called in production, `06` §12.1).

### §4.3 The completeness half — *mechanics fully formed, error-free, and complete*

Scorable everywhere, and **FAILS, live and proposed.**

| defect | class | where |
|---|---|---|
| a ratified "+1D" bonus (CR4) that is a penalty at every canonical faculty ≥ 5 under a ratified extension (ED-SC-0032) | error | §2 row 4, live kernel |
| `FaceScale.face_max` raises `TypeError` through the public API (`charisma` never set) | error | `06` L6.3 |
| `_derive_resistance` returns 0 silently on a live `World` (reads `stabilities` only from a `dict`) | error, latent | `06` L6.4 |
| two return shapes from one router (`wrapper.py:254-259`) | incomplete | live |
| a Key type the log refuses (`scene.investigation_resolved` payload) | error | 05 B5 (proposal) |
| `margin ∈ [−1, 0]` fed to fixed bands — Overwhelming/Success unreachable in every body | **error, and under §0.06 an R failure, not only a logic defect** | 05 B1, `04_CONSENSUS` |
| `formal_grounds_check` returning `False` for every case that returns `True` today | error (shipped-code regression) | 05 B2, `03_INQUIRY` |
| `_resolve` name collision killing the kernel suite; `log.of_type` invented | error | 05 B3, B4 |
| `Venue(**o)` with `on_hung`/`holdout_rounds` → `TypeError` | error | 05 F8, `04_CONSENSUS` |
| `unanimity_required` named in four places, implemented in none | incomplete | `dictionaries.py:686,707,721,741` |
| three `GAMES` rows that are stubs, three `Mode` scaffolds that are stubs | incomplete | `wrapper.py:239-244`, `modes.py:333-351` |

**R verdict (all three halves): player half not scorable; world half FAIL; completeness half FAIL.**

---

## §5 · S — the ladder test, both halves separately

Rule 2: **S-UP** — can a demand travel up and be filtered by a named person at a rung? **S-DOWN** — can an opportunity travel down and reach a person who holds no post?

**S-UP: FAILS, structurally.** There is no demand object. The council is fired by a stat threshold (`Sta ≤ 2`, `scene_dispatch.py:84`), the motion is derived from stats (`parliamentary_bridge.py:90-107`); no person carries either and nothing filters. The one upward-shaped path — council outcome → `L` → next season's Mandate pool (`parliamentary_vote.py:169`) — is a stat loop between two mechanisms of the same subsystem, not a ladder with a person at a rung. In the proposals, inquiry's `open_case` through `formal_grounds_check` is a gate, not a person; consensus's holdout block is person-shaped and has no person behind it (an exchangeable draw index).

**S-DOWN: FAILS, structurally.** There are no persons (`grep`: only `npe.NPC`, never generated on the loop). All three branches write their durable outcome to `Settlement.ledger` (their §6 write tables; anchors `02:372`, `03:434`, `04:387` per `07` §3.7, not re-derived here), which nothing on the season loop reads and whose expiry sweep has no caller (`07` §3.4); and a scene carries no `place` to write it at (`06` PR8.2).

**What does propagate:** scene → faction stat, one direction, and it is measured (§8.1). Rule 2 does not test that; it tests persons at rungs. **The subsystem's ladder-S is zero for the same reason `14_NERS.md` §6 gives for the whole tree — there are no persons — and the proposals inherit it until PR #362's `Person` lands.**

### §5.1 The two tests §0.06 adds (`PR #364 (proposed) CLAUDE.md §0.06`; added on the rubric change, §0.5)

**Calculations consistent in methodology with sibling mechanics** — *two ladders for one quantity is an S defect even when each is individually correct.* Inside this subsystem: the Persuasion bands live as literals in `resolver.py:91-95` and as constants in `contest_legacy_stub.py:67-71` consumed by the vote (`06` PR8.1a); the neutral start 5 is spelled four ways; `faction.band_of` carries a ±0.06 variant of the same bands (`07` §4 row 8); the council maps `a/b/draw` → `Success/Failure/Partial` (`scene_dispatch.py:337-342`) while the vote maps `passed/failed × total_victory` → `Overwhelming/Success/Partial` (`parliamentary_bridge.py:127-131`) — two band-to-Degree methodologies for one Key type; `Leverage.net` is a second δσ derivation beside `sigma_leverage.levels_to_net_sigma` (`06` PR8); and CR4's die is a *pool-side* bonus under a *pool-scaled* Overwhelming bar, which is why its sign flips with pool size (§2 row 4). **Across subsystems:** mass battle reports a survivor-ratio classifier under the ladder's band labels and the faction layer keys Terms/Storm on it (`07` L2) — the coordinator records that this was earlier softened to "not a single-owner violation"; under §0.06 it is a straightforward S defect. **FAIL.**

**Pauses correctly when another system or scale is called for.** The season loop does not pause: `dispatch_scenes` drains the whole slate synchronously inside the action callback (`scene_dispatch.py:404-417`), the vote runs after it in the same callback (`mc_v18.py:149-160`), OF-7 defers every scene apply to `accounting_boundary` (`keys.py:571,581`), and the vote then derives its roster from `L` values the council has already moved on paper (`06` S3.1, `01` §1.9 I-S6b). Jordan's in-scene ruling is observably violated in shipped `agon` (05 §5). **FAIL.**

**S verdict: S-UP FAIL · S-DOWN FAIL · methodology-consistency FAIL · pauses-correctly FAIL.** The one S property that holds is the mechanical one: the provider is resolved by role at first use behind a blocking export (`composition.py:43-69`, `06` §10 row 1).

---

## §6 · The session's proposals, graded individually

| document | grade under the four rules | what this pass adds to `05`'s disposition |
|---|---|---|
| **`00_BRANCH_SHAPES`** | The framing (one spine, one `settle()`, two rows) is right and the three-lens audit reached it first; its §2.3 hunt cut six real candidates; its §7.7 dispositions of SC3/SC4/SC5 are right in direction and now measured (§7). Paper. | its "keep `on_hung: lot` at medium" was correctly reversed by `04` on arg 4; its `burden` N-line (*silence convicts*) is right about the selector and wrong about what remains to be built (§2 row 1) |
| **`01_SPINE`** | The deletions are good and load-bearing. `SUCCESS_UNIT` is a false N-line by precedent (§2 row 2). The `armature=` N-line is one-third wrong-signed (§2 row 4). The §7.4 falsifier cannot observe on the factions the trigger fires on — confirmed by count (912/1,114). B3 (`_resolve` collision), B5 (the Key payload) stand. Paper. | **the goldens are a control for value-identity and blind to the armature** — the sign inversion is invisible to `test_mc_v18_regression.py` and `test_f7_smoke_oracle.py` because `build_contest` cannot reach it; a branch that passes `armature=` has no golden for the thing it changes |
| **`02_NEGOTIATION`** | `settle()` survives every attack I ran (§1.3). `floor_a` is defined two contradictory ways (05 F4) — stands. Its §10.2 `support`-spam row said "unknown"; **measured:** at 1–3 exchanges a `support` is an advance forgone and strictly worse; SC4's successor is not dominant on any canonical proceeding (§7). Its `Grudge` has no home. Paper. | the split-table identity holds exactly and the live table's defect reproduces (§1.3) |
| **`03_INQUIRY`** | Its three headline findings survive (05). **Its dominance analysis is not merely on the wrong venue — it is inverted on both venues** (§2 row 1); `restricted` is a false N-line; its §5.5 counts CR4's die as a benefit and the die is a penalty at the faculties a tribunal would run (§2 row 4). B2 (the tribunal regression) and B4 (invented API) stand. Paper. | I-I6 and I-I7 regrade: *silence convicts* is **already MECHANICAL** for a stalling accused via `ProofBar`; the CONVENTION grade was for a hole that is not there |
| **`04_CONSENSUS`** | B1 reproduced (three lines, §0.3); all three antibody channels inert, confirmed by reading; `holdout_rounds`/`on_hung` false N-lines; the recusal false; the venue reachable only by a `build_contest` path `scene_dispatch` never takes (07 §5). Its refutations of the shape spec remain its value. Paper. | nothing to add to 05 §2 except that the per-member term it recommends is also what would give `Ballot` a producer (§1.3) |
| **`05_RECONCILIATION`** | Sound; its §5 SURVIVED list holds under re-execution (split identity, incommensurability, binding-order trace, import-cycle test). | **partial contradiction of §7:** "the two campaign goldens are the control for the whole programme" — they control *did it move*, not *did it matter* (arm B: every effective write moves them, 0/16 identical) and cannot reach the armature. Its §8 item 2's "cheapest measurement" is done and holds |
| **`06_SYSTEM_AUDIT`** | The only executed evidence before this pass, and its structure holds at 16 seeds. **Two numbers corrected:** side-A faculty = 1 in **81.4 %** (not 97 %); "the contest decides nothing" is true of **75.1 %** of echoes and false of 25 %. Its §4.1 "zero decisions" is extended: with decisions, 8 %. Its FA5.2 dominance is confirmed and extended to the open-loop grammar. | `06` §14.2 predicted both corrections; its §14.3 objection to the spine's falsifier is confirmed by count |
| **`07_TOPDOWN_BOTTOMUP`** | Mostly outside this scope; its §3.7 (the three branches are paper for the same two reasons) is right. | a third reason: the armature they compose on inverts a canon bonus |

---

## §7 · The 2026-05-28 verdict, re-graded under Rule 1; SC3/SC4/SC5 dispositioned

**What it graded.** Its §1 component table names ten mechanisms — Argue Pool `(Cog×2)+H`, five interaction types, Composure `Cha+6`, Concentration with Spent (−2D), a per-territory Conviction Track, genre weights ×0.5–1.25, the Doubt Marker, Regroup restoring by Focus, Beliefs, the PP-684 Conviction vector. **Not one of the ten exists in the executing kernel under its own mechanics** (`06` §11, row by row; `primitives.py` has no Composure, no Focus, no genre multiplier; the Conviction Track has no store). Under §0.05 the object it graded is reference.

**Re-graded under the rules.** *E* was scored as an axis — "interaction types learnable", "most player-legible identity system" — the exact shape Rule 1 forbids. *R* was scored with no seat-playability question — "2D pool floor … exit-not-floor" is a portrait of a low-stat character, not a choice. *N* — "Conviction Track depth IS the L4 clock-routing" — argues about a track that has no engine. *S* — "Composure shares architecture with personal combat; PP-684 Conviction Vector provides faction-scale path" — Composure is retired in SC and a live, unread currency in two other subsystems (`07` L7); the Conviction Vector has no field (`07` §2.6). **All four PASSes are arguments about a text. On the executing subsystem: N ≈ 0 as wired, R not scorable, S zero on both halves, E undefined (§3.1). The verdict does not transfer.**

| P2 | prior claim | disposition under `CLAUDE.md` §0's five tests | artifact |
|---|---|---|---|
| **SC3** genre 0.5 near-inert at R=1 | a ×0.5 margin multiplier for an off-primary genre collapses the exchange | **Irrelevant by retirement on the executing path (rung 2)** — no genre multiplier on margin exists. **Its successor, CR4's +1D (`rhetoric.py:221`), is measured and closes in the worse direction: not near-inert but inverted** — −3.6/−5.6 pts at pools 13/17 under the ruled extension, +8.3 at pool 7 (§2 row 4). Unreachable from the seam; reachable when `armature=` lands | `ners_kernel2.py`, `ners_kernel3.py` |
| **SC4** Regroup-on-Spent dominant | regrouping while Spent forms a loop | **Irrelevant by retirement (rung 2)** — `Regroup` is not a `Move` (`resolver.py:34`); `pass` accrues a fault. **Its successor (`support`: cost 2, regain 4, +0.8 Standing, no fault) is measured:** on the production venue (budget 3) the reserve never binds; on `grand_contest` (budget 5) supporting more is strictly worse (`support_below0.5` → `B_decisive` 104 vs 1); on the default 8-exchange `Venue`, which no canonical proceeding ships, `support_below0.5` beats `logos_spammer` **0.589**. **Not dominant on any canonical proceeding; mildly dominant on a venue nobody ships.** | `ners_kernel.py` §6, `ners_kernel2.py` |
| **SC5** Focus-1 Regroup trap | a low-Focus character cannot regroup enough | **Irrelevant by retirement (rung 2)** — `Reserve.REGAIN = 4` is flat (`primitives.py:52`); `Contestant` carries no Focus | read |
| SC1 (note) exit-not-floor | no pool floor; exit via Spent is the safeguard | **False of the code:** `Pool.size = max(5, 2f+3)` (`primitives.py:211`) is a floor of 5, and the exit (reserve exhaustion → two yields → clinch) is unreachable below budget 5 | read + `ners_kernel.py` §6 |

---

## §8 · Verdict per axis, and what would overturn each

**The hardest question first — is the social contest NECESSARY at all?**

**As first drafted (n = 16, before the positive control): "no — a coin."** That claim was banked on the winner channel, and §8.1 shows the winner channel is blind to *every* `L`-channel effect, including a positive control ten times larger than anything the subsystem does. **Retracted in that strength; replaced by the measured decomposition:**

- **What the subsystem does, measured (n = 64, paired by seed, RNG-preserving arms):** the council echo is a systematic **Legitimacy drain** on factions in crisis (remove it: Varfell +0.83 final `L`, t = 3.07; Crown +0.44, t = 2.12); the vote's writes are a systematic **Legitimacy pump** on the establishment (remove both: Crown −0.77, t = 2.77). These are real, mechanism-caused, and not entropy consumption — arm B preserves the RNG stream and still shows them.
- **What reaches the outcome the campaign is scored on: nothing detectable — and nothing on this channel could.** Arm P adds +2 `L` to the crisis faction at every council (4,629 writes, every faction's final `L` up 2.6–5.5 points, t up to 13) and moves the winner distribution by χ² = 3.91 (p ≈ .27). The fallback winner is `held·10 + L + len(territories)` (`mc_v18.py:295`) and GD-1 reads territory and Accord (`victory.py`); Legitimacy is a tiebreaker worth at most 7 against 10 per territory. **The subsystem's only output channel does not reach the game's outcome, as the game is scored today.**
- **What the kernel's interior adds beyond a two-integer table: nothing.** The verdict is a function of `(round(L), round(7−Sta))` (§1.1 grid); a Bernoulli drawn from the same reseeded stream reproduces the drain and the pump in distribution by construction. The N that the kernel genuinely holds (a 0.6 spread at fair inputs, a real appeal–venue fit, a +11–15-pt Style alignment) is stranded behind six parameters at one call site (`scene_dispatch.py:300-301`) and an adapter that hands it faculty 1 in 82 % of councils.

**So: cut the whole subsystem and the emergent possibility lost is a systematic Legitimacy drain on crisis factions and pump on the establishment — real, measured, reproducible by a table, unread by the victory condition, unrecorded by any narrative surface, and chosen by no one.** Under §0.06's six directions (§1.4) the N-line holds outright in one (lateral: it is the only personal-scale mechanism that executes at all) and narrowly in one (vertical: it moves a stat), and is nil or failing in the rest. **N: NARROWED, not passing.**

| axis | verdict (shorthand rubric) | verdict (`§0.06`) | what would overturn it |
|---|---|---|---|
| **N** | FAIL as wired (retracted in strength — §8.1, §10) | **NARROWED** — one direction holds by default, one narrowly by measurement; and the engine under it is the wrong one for its inputs (§12.1) | a reader of `L` in the victory condition or the faction AI strong enough that arm P moves who wins; a production input where the kernel's decision surface is reached (side-A faculty ≥ 4 with a non-default policy) |
| **E (ratio)** | undefined on the live path; bloat elsewhere (35.6 % reach) | **overhead FAIL · intuition FAIL by absence, and FAIL by `ContestView` where a seat would exist** (§3.3). Proposals: spine neutral-to-negative, negotiation positive, inquiry positive once `restricted` is cut, consensus negative | the venue library, a policy and the armature becoming reachable, and a view that shows the causes — three parameters at one call site plus two fields on `ContestView` |
| **R** | NOT SCORABLE (retracted as a blanket verdict — §0.5) | **player half not scorable · world half FAIL · completeness half FAIL** (§4) | a `Person` producer and a policy at the seam, then a *reactive* best-response sweep; a Key with content and a reader; the eleven completeness defects in §4.3 fixed with a falsifier each |
| **S-UP / S-DOWN** | FAIL / FAIL | FAIL / FAIL — plus **methodology-consistency FAIL and pauses-correctly FAIL** (§5.1); the kernel draws by the legacy discrete rule while the tree's videogame-canonical draw is continuous (§12.1) | a demand a person carries; a person with no post reading a ledger the loop writes; one band-to-Degree method for one Key type; scene applies landing in the scene |

### §8.1 The n = 64 result, with the positive control and the detector's power

Arms A, B, E, C on seeds 0–63 (`ners_ablate.py`, `ners_ablate_n64.log`; arm B's seeds 16–63 tagged separately), plus **arm P, a positive control**: every council writes **+2 `L` to the crisis faction regardless of verdict** — a perturbation that must matter if anything on this channel does. **Sample size: 64 campaigns per arm, 50 seasons each.**

| arm | Crown | Church | Hafenmark | Varfell | χ² vs A (3 df) | same winner as A | identical final state |
|---|---|---|---|---|---|---|---|
| **A** baseline | 34 | 6 | 4 | 20 | — | — | — |
| **B** council echo suppressed (RNG preserved) | 25 | 4 | 9 | 26 | 4.48 (p ≈ .21) | 23/64 | 2/64 |
| **E** council + vote writes suppressed | 25 | 7 | 11 | 21 | 4.74 (p ≈ .19) | 20/64 | 0/64 |
| **C** council never fires (RNG shifts) | 29 | 4 | 6 | 25 | 1.75 (p ≈ .63) | 22/64 | 0/64 |
| **P** positive control, +2 `L` per council | 35 | 1 | 5 | 23 | **3.91 (p ≈ .27)** | 29/64 | — |

**Detector power** (Monte Carlo, 4 categories, α = .05, n = 64 per arm): a 10-point win-share shift is caught 15 % of the time, 20 points 51 %, 30 points 89 %, a flat 25/25/25/25 98 %. **So a null here means *"I could not detect a difference at n = 64; a ≥ 30-point shift would have shown with ~90 % probability; a 10–20-point shift would likely not have."* It does not mean "there is no difference."**

**Paired t by seed on final `L`** (the stat the subsystem writes):

| arm − A | Crown | Church | Hafenmark | Varfell |
|---|---|---|---|---|
| **B** (council echo off) | **+0.44 (t = 2.12)** | −0.12 | +0.16 | **+0.83 (t = 3.07)** |
| **E** (both off) | **−0.77 (t = 2.77)** | −0.13 | −0.33 | −0.47 |
| **C** (no council) | **+0.63 (t = 2.68)** | +0.13 | −0.06 | +0.16 |
| **P** (+2 per council) | **+5.50 (t = 13.3)** | **+2.57 (t = 6.1)** | **+3.34 (t = 6.7)** | **+3.15 (t = 6.3)** |

Reading, in the order the coordinator asked for:

1. **Who wins.** No arm differs detectably from A — **including the positive control.** A +2-`L`-per-council pump that raises every faction's final Legitimacy by 2.6–5.5 points moves the winner distribution by less than the detector can see. **The winner-channel null is therefore uninformative about the subsystem and informative about the game:** Legitimacy is nearly disconnected from who wins (`mc_v18.py:295`; `victory.py`; `07` L1 records the victory function's third clause as dead). Stated exactly: *at n = 64 I could not detect a difference in who wins between A and any arm; I would have detected a ≥ 30-point shift with ~90 % probability; and no `L`-channel perturbation, however large, produced one.*
2. **The stat it writes.** The subsystem is **not inert.** Arm B — RNG-preserving, so the divergence is the mechanism and not entropy — shows the council echo is a systematic drain on crisis factions' `L`. Arm E shows the vote's writes are a pump on the establishment's `L` that outweighs the drain on Crown. **Arm C diverges in the same direction as B on Crown (+0.63, t = 2.68) — it diverges through the removed drain, not only through the RNG-stream shift**, though C cannot separate the two and B can, which is why B was run to n = 64.
3. **Necessity.** The N-line bottom-up: cut the council and you lose a systematic Legitimacy drain on factions in crisis; cut the vote and you lose a Legitimacy pump on the establishment. Both are real, measured, mechanism-caused — both are reproduced in distribution by a state-conditioned Bernoulli, because nothing inside the kernel reaches `L` except through the verdict scalar — and neither reaches who wins. **"Inert" was the wrong word; "unread" is the right one.**

---

## §9 · Attacks that FAILED, reported as failed

| attack | result | artifact |
|---|---|---|
| side-A / first-mover bias on the production venue | **FAILED** — 2011/1989 at N = 4000, 0 draws (odd bench, equal weights) | `ners_kernel.py` §5 |
| …and on the 8-exchange default `Venue` | **SUCCEEDED, latent** — with no `support`, A exhausts first (12→9→6→3→0, yields at moves 5 and 7) and loses **2000/2000** by `clinch:silence`; a first-mover *disadvantage* at long budgets. No canonical proceeding exceeds budget 5 | `ners_kernel.py` §6 |
| `weighted_by_standing` differs from `simple_majority` somewhere reachable | **FAILED** — 0/3000 paired | `ners_kernel.py` §4 |
| the council is literally inert (all writes clamped) | **FAILED** — 25 % of echoes move `L`; at n = 64 the council echo is a measured drain (t = 3.07 on Varfell) and the vote a measured pump (t = 2.77 on Crown) | `ners_ablate.py`, `ners_ablate_n64.log` |
| the ablation harness does not suppress what it claims | **FAILED** — every suppressed write has `before == after` (B 1,386/1,386; E 1,710/1,710 applies and 115/115 penalties at n = 16); the instrumented arm A reproduces the uninstrumented seed-0 campaign byte-for-byte (`key_log_hash fabb99611758843d`) | `ners_ablate_out.json`, direct run |
| the detector would miss a real effect on `L` | **FAILED** — the positive control is seen at t = 6–13 on every faction | `ners_ablate_n64.log` |
| the detector would see a real effect on who wins | **SUCCEEDED — and it is a finding about the game, not the detector:** a positive control ten times the subsystem's own effect on `L` does not move the winner distribution (χ² = 3.91) | `ners_ablate_n64.log` |
| consensus's `UNANIMITY_MARGIN_SCALE` works at some value | **FAILED** — margin ∈ [−1, 0]; `Partial` at 0, `Failure` below, at scales 1/10/100 | `ners_kernel.py` §7 |
| `split(−m) ≠ 1 − split(m)` somewhere | **FAILED** — holds on 101 points including 0 | `ners_kernel.py` §7 |
| `support` is a dominant defensive line for the accused | **FAILED — inverted** (§2 row 1) | `ners_kernel2.py` |
| SC4's successor is dominant on a canonical proceeding | **FAILED** on `guild_arbitration` (unreachable) and `grand_contest` (worse); succeeded only on the non-shipped 8-budget venue | `ners_kernel.py` §6, `ners_kernel2.py` |
| CR4's die helps at canonical faculties | **FAILED under the ruled extension**; holds under the bare ladder; holds at pool 7 under both | `ners_kernel3.py` |
| the campaign goldens control the armature | **FAILED** — `build_contest` cannot pass one; the inversion is invisible to both goldens | read `wrapper.py:110` + `test_f7_smoke_oracle.py:344` |
| `PoolDesaturation` is inert on the production path | **not attacked — and it is not inert:** at pool 13 it demotes ~1,600/20,000 receptions from Overwhelming to Success (mean degree 2.57 → 2.31). Ruled (ED-SC-0032), so a fact rather than a defect; recorded so nobody re-derives it | `ners_kernel3.py` |
| the armature's δσ channel does nothing at faculty 1 because of a bug in my harness | **FAILED** — the trace shows the shift added (`net` 3.0 → 3.863) and the band unmoved; the falsifier (same δσ on `roll_net_continuous`) moves P(A) by +0.199 | `ners_kernel4.log`, §12.2 |
| the quantization is a property of the leverage layer, not the draw | **FAILED** — swapping only the draw restores the channel at every faculty | `ners_kernel4.log` |
| `settle()` is a false N-line | **FAILED** — nothing ruled in divides a stake (§1.3) | read |
| `ContestOutcome.veto` is a false N-line (`reason` already carries `clinch:`) | **FAILED** — under a margin-only return the clinch's *override* of the margin's sign has no other carrier; `reason` is a string for legibility, not a value the ladder reads | read `resolver.py:457-461` |
| the 9-module import-cycle test pins a member count | **FAILED** — families, not members (05 §5; confirmed twice before me, not re-run) | — |

---

## §10 · Asymmetric-skepticism self-check

1. **I banked "the council is a coin — N: FAIL" on 16 seeds and on the winner channel, before running a positive control.** The coordinator asked for the attack I ran against my own ablation; here it is. *(a) Does the harness suppress what it claims?* Yes — every suppressed write has `before == after`, and the instrumented baseline reproduces the uninstrumented campaign's key-log hash exactly, so the harness itself perturbs nothing. *(b) Would it show a difference if one existed?* On the stat the subsystem writes, yes, loudly (arm P: t = 6–13). **On who wins, no — not even for the positive control.** So the dramatic finding was banked on the one channel the instrument cannot see, which is precisely the direction an author is least inclined to attack. **Retracted in strength (§8): the subsystem is not inert; it is unread.** The positive control was worth more than the ablation, as the coordinator said it would be.
2. **My best-response sweep is open-loop.** A reactive policy (reading `leading`, `reserve_frac`, `evidence_available`) could beat 8 % at the live inputs and could unsettle the ethos-first line at fair inputs. Both R bounds are upper bounds on choice, not estimates; §4 says so.
3. **I measured the CR4 inversion at one terrain (FACT), one appeal (logos), mirror faculties, and three pool sizes.** The sign is pool-dependent and I have stated the crossover (between 7 and 13). I did not measure asymmetric faculties or other terrains. The mechanism (`overwhelm_bar` vs one die's net) is read from code and does not depend on the seed.
4. **The one attack I did not run because it would have favoured the subsystem:** whether the council's *state-dependence* (P(A) rising with `L`) produces a feedback a plain coin would not. I argued it — a state-conditioned coin is still a coin — rather than measured it (an arm F substituting a table lookup for the kernel). The argument is by construction and I believe it; it is nonetheless the one place I let an argument stand where a two-arm artifact was constructible. Flagged rather than hidden. **Note what §8.1 did to this item:** the feedback *does* exist (the drain and the pump are exactly that state-dependence made systematic), and a table reproduces it — so the un-run arm F would have confirmed the argument on the `L` channel and been blind on the winner channel like everything else.
9. **The strongest kernel finding in this document (§12.2) was not planned; it fell out of a P-ii check I ran because the second instrument asked for it.** I nearly attributed the +0.000 to my own harness, ran the trace, and then ran the one falsifier that could separate "the leverage layer is broken" from "the draw quantizes it" — and the falsifier decided it. Recorded because a finding an author did not go looking for is the one to check hardest, and this one was.
8. **The rubric widened after the draft (§0.5), and I re-graded under it without re-measuring.** Every §0.06 re-grade (§1.4, §3.3, §4.2–4.3, §5.1) is a reading of already-measured or already-read facts against a wider test; none rests on a new measurement. Where a §0.06 test would want its own instrument — *pauses correctly* has a constructible falsifier (`01` §7.4, corrected by `06` §14.3) that nobody has run — I have said so rather than graded by argument alone.
5. **I did not re-read `01`–`04` end to end**, and I did not re-verify `05`'s research-honesty null. Where I grade a critic's finding (F3, F4, F6, F8, B1–B5) I re-read the cited code, not the critic's transcript.
6. **Favourable verdicts I gave** — the split identity, `weighted ≡ simple`, no first-mover bias, `settle()` surviving — each carry the same kind of artifact as the unfavourable ones. The asymmetry I can find in myself is in *which* claims I chose to measure: I measured the ones I expected to fail. Item 4 is the residue of that choice.
7. **Self-review bias:** this pass grades a session I was not part of and a subsystem I did not write, so the bias risk `SESSION_BRIEF.md` §8.6 names runs the other way — toward severity. The one limitation an independent reviewer would add: **every "the possibility survives the cut" in §2 was checked against code that exists today; a reviewer holding PR #362 as the target would re-run rows 2 and 3 and may keep both.**

---

## §11 · Paper versus executes, every component

| component | grade (`CLAUDE.md` §0.2) | evidence |
|---|---|---|
| `agon` on `guild_arbitration` via the Stability-Crisis trigger | **EXECUTES** | 1,277 councils / 16 campaigns, instrumented |
| the §10 vote | **EXECUTES** | every season with two eligible factions; 183 penalties, 431 winner echoes / 16 campaigns |
| the council's *decision surface* (policies, venues, armature, evidence, faults) | **executes in tests only** — reachable from the seam through zero of its six parameters | `scene_dispatch.py:300-301`; `06` §12.1 |
| the armature, CR4, CR5 | **executes in tests only; and CR4 executes with the wrong sign** when it does | `ners_kernel3.py` |
| the venue library, `INSTITUTIONAL_MODES`, `CROSS_CULTURAL_VENUES`, `ThresholdRace`/`ProofBar`/`GraceThreshold` | test-only | `06` F1.1, §12.2 |
| `faction.py`, `parliamentary_stay.py`, `agon_harness.py`, `narrative.py`, `appraise.py`, `contest_legacy_stub.run_contest` | **dead** on the loop | zero callers (confirmed by grep for the harness; `06` §12.2 for the rest) |
| `00_BRANCH_SHAPES`, `01_SPINE`, `02_NEGOTIATION`, `03_INQUIRY`, `04_CONSENSUS` | **paper** (their own grade, confirmed) — and two of their mechanisms would execute *against* their claims when built: `restricted` guards a non-exploit; `armature=` delivers a negative die | §2 rows 1, 4 |
| `05_RECONCILIATION`, `07_TOPDOWN_BOTTOMUP` | paper (readings) | — |
| `06_SYSTEM_AUDIT` | **executed evidence**, corrected on two numbers, otherwise upheld | §6 |
| the σ-leverage layer's δσ channel on the production path | **executes as a whole-unit step at faculty ≥ 2 and as nothing at faculty 1** — measured on the live draw and on the continuous falsifier (§12.2) | `ners_kernel4.log` |
| the rolling-engine diagnostic's Stage-0 calibration, run by this pass | two rows reproduced by reasoning, two consistent, one not run; no flipped verdict, no invented defect (§12.0) | §12.0 |
| this document | **executed on every numeric claim; paper on every argument** — §8's necessity verdict now rests on three measured legs (the paired-t drain/pump at n = 64, the positive control's blindness on the winner channel, the grid) and one argued leg (a state-conditioned coin is a coin), with §10 item 4 naming the artifact that would close the argued leg; the §0.06 re-grades are readings, not measurements (§10 item 8) | §0.3, §8.1 |

---

## §12 · The second instrument — the rolling-engine diagnostic (`skills/valoria-resolution-diagnostic/SKILL.md`, PR #363), applied to the production path

The brief did not point at this skill; the coordinator did, after §1–§11 were drafted. It owns the METHOD for any component that resolves by a draw (Stage 0 calibration → Phase 0–6 → lessons → verdict), and the social contest resolves by two: the exchange roll (`resolver.py:283-308 _reception`) and the bench ballot (`:139/:144 random.gauss`). Its Stage 0 says the skill is correct *iff, run blind, it returns the adjudicated answers; if not, fix the skill, not the canon* — a positive control on the method, which is the same reason arm P exists (§8.1). It is run first.

### §12.0 Stage 0 — calibration, run before the verdict

| calibration row | adjudicated answer | what this pass returns, and how | reproduced? |
|---|---|---|---|
| pre-resolver faction layer (bare-stat Domain Actions) | NON-COMPLIANT → route bare stats to deterministic+stochastic | by the same tests this document applies to the contest — odds illegible (P-i), `1/√N` leverage (P-ii), a bare binary on pivotal irreversible outcomes (P-iv), dice on a deterministic ledger (S methodology) — NON-COMPLIANT. **By reasoning, not measurement**: the faction layer's engine was not run here | **yes** |
| post-resolver faction layer | compliant (legible, flat 0.10/pt leverage, ledger-consistent) | `P = clamp(BASE + SLOPE·M)` passes P-i by construction, P-ii by construction, P-iv via the 5 % floor and 3 % residual; the guardrail *engine parameters are Jordan's* is respected — this pass does **not** mint a defect from PROPOSED numbers. §8.1's finding that `L` is unread by the victory condition is **not** attributed to the resolver, which resolves actions, not victory | **yes** — and no defect invented |
| continuous engine below 5D without `net − (Ob − 0.5)` → finding | fidelity defect | N/A to the contest kernel: it does not use the continuous engine — it draws whole dice (`sigma_leverage.py:269 roll_net` → `dice_engine.roll_pool`), which is exact and needs no continuity term. No finding, no flip. **That the kernel draws whole dice is §12.1's subject** | consistent |
| σ-leverage advantage driving `eff_Ob < 1` → finding | Ob-floor cliff | N/A: the kernel's leverage enters as a μ-shift (`net_boost`, `resolver.py:302`, *"base_ob untouched, Ob floor never breached"*), never as an Ob shift. No finding, no flip | consistent |
| mass-battle Size/Command pre-fix cliff | finding (ED-876) | not run — outside this pass's subject | not run |

**Calibration verdict: on the rows this pass can reach, two reproduced and two consistent; no adjudicated verdict flipped and no defect invented where canon ratified the mechanism as fine.** The method is calibrated to the extent it can be here; row 5 is a stated gap.

### §12.1 Phase 0 — scope gate and the ENGINE-SELECTION DECISION RULE on the production path

**Rolling components:** the exchange roll (`_reception`: discrete d10 net + σ-scaled μ-shift → the one ladder); `VoteAtClose` (one `gauss` draw per juror, `:139/:144`); the §10 vote (`dice_engine.roll_pool`, `parliamentary_vote.py:178`). **Recognised and excluded** (no draw): the Persuasion clock, `Reserve`, `Standing`, `Room`.

**The rule, applied to the production council** (`scene_dispatch.py:139` → `wrapper.py:300 build_contest` → `resolver.py:283`):

| the rule's test | the production path's fact | anchor |
|---|---|---|
| the input | **a bare stat**: `faculty = max(1, round(L))` for side A, `max(1, round(7 − Sta))` for side B — one number from one faction's own aggregate, nothing else of the faction enters | `scene_dispatch.py:139` |
| the pool | `Pool.size = max(5, 2·faculty + 3)` → 5–17D; **at the live input (faculty 1, 81.9 % of 4,979 councils) exactly the 5D boundary** the rule names | `primitives.py:211`; §1.1 |
| a genuine setup/skill axis | **exists in the kernel, absent on the path**: no policy (`:301`), no armature (`wrapper.py:110`), no evidence (`:97-98`), no venue choice (`:118`), no `world` | §1.2 |
| pivotal / load-bearing | load-bearing on `L` (a measured drain, §8.1); unread by the victory condition | §8.1 |
| aggregation available | **not today** — PR #362 §C.5.1's roster (`PersonId[]` at weight) is the aggregation the design intends and no `Person` exists (§1.3) | — |

**Verdict under the rule: a bare stat in the 1–7D band on a load-bearing outcome with no aggregation available routes to Instance B; the path is on neither B nor A.** It is on Instance A's *leverage layer* (`net_boost`, σ-scaled, CR6) bolted onto the **legacy discrete d10 draw**: `resolver.py:28-32 roll_net` wraps `sigma_leverage.roll_net`, which delegates to `dice_engine.roll_pool` and returns an integer net — kept deliberately so that "the 151 seeded tests" keep their stream (`resolver.py:18-22`) — while the videogame-canonical draw is `sigma_leverage.py:282 roll_net_continuous` (*"Canonical for Godot"*). The skill: *"`params/core.md §Die Rule (d10)` … is TTRPG-mode only. In videogame canon it is superseded: healthy pools → A; bare-stat strategic → B. Flag any videogame system whose canonical resolution is 'roll a bare pool vs a flat Ob and count successes' as a wrong-engine defect (Lesson 3)."* The production contest rolls a bare pool of whole d10s against a flat integer Ob (`Venue.base_ob = 2.0`, `resolver.py:157`; `_derive_resistance` never plumbed) and bands the integer net. **Wrong-engine defect, Lesson 3, in the skill's own words** — with two precisions so the claim is exact: the kernel bands σ-net (faces −1/0/+1/+2), it does not count successes; and its floor is 5D, not 1D. The *class* fires; the literal is one word off.

### §12.2 The measured consequence — the σ-leverage layer is quantized away at the live input (P-ii, P-iii)

`ners_kernel4.py`. The armature's δσ channel is the one Stage-3 mechanic that works (§1.2: +11–15 pts at faculty 5). Checked across pool sizes, and against the one falsifier that separates "the leverage layer is broken" from "the draw quantizes it":

| faculty (pool) | `net_boost` base → with δσ 0.5 | whole-unit gain | Δ P(A), **live discrete draw** (N = 6,000 mirror) | Δ P(A), **continuous draw** (`roll_net_continuous`) |
|---|---|---|---|---|
| **1 (5D) — the live input** | 0.000 → 0.863 | **0** | **+0.000** | **+0.199** |
| 2 (7D) | 0.351 → 1.325 | 1 | +0.213 | +0.185 |
| 5 (13D) | 1.806 → 2.819 | 1 | +0.130 | +0.147 |
| 7 (17D) | 2.883 → 3.768 | 1 | +0.113 (N = 10,000, `ners_kernel4.log` first block) | — |

**Mechanism, read from code and confirmed by the trace:** `net = roll_net(pool) + net_boost(lev, pool)` (`resolver.py:302`) adds a continuous μ-shift to an **integer** net; `degree_from_net` reads `margin = net − ob` against edges at 0, 1 and 3 (`dice_engine.py:227-293`) with `ob = 2.0`; so a shift below 1.0 can never cross an edge, and only `floor(net_boost)` acts. At faculty 1 the base leverage is 0 (`Leverage.net(1) = (1−4)/6 + 0.5 = 0`) and maximal alignment adds 0.863 → floor 0 → **the Style card buys a faculty-1 contestant exactly nothing, whatever the judge's convictions.** At every other faculty the "continuous" channel is one whole success. **The judge-finding-5 rationale for moving the armature from the pool to the μ-shift (`resolver.py:293-296`: "a fractional pool bonus rounds away … net_boost's μ-shift is NOT rounded") is defeated one line later by the ladder, which rounds it.** On the continuous draw the same alignment is worth +0.20 at faculty 1 — the engine the layer was designed for.

**Properties:** **P-ii FAIL** for the leverage layer (0 at the bottom of the range, +0.21 one step up, +0.11–0.13 above — out of band at the extreme, the ED-875 class in the opposite direction); **P-iii FAIL** (a continuous input crossing discrete boundaries, the skill's own description). The *faculty* channel itself is roughly in-band — per-point ΔP on the production venue measured +0.066/+0.115/+0.115/+0.104/−0.007/+0.105 at N = 2,000 (the 5→6 step disagrees with the N = 1,000 grid's +0.06 and is unresolved at this N) — because `net_boost` is σ_N-scaled; CR6 does its job where it is not rounded away.

**For the proposals:** the spine's `armature=` N-line (§1.3) delivers, at the faculty the seam passes in 82 % of councils, a zero δσ (this section) and a negative die (§2 row 4); CR5 is a cost. All three branches compose on that passthrough.

### §12.3 The pathology class — same class, same order, not the same case

The skill's table names *floor degeneracy (stat 2 vs Ob 3) = 0.069* and *punching-up wall (stat 2 vs strong 7, Ob 4) = 0.010* as what the deterministic+stochastic resolver fixes. Those are bare-2D-vs-flat-Ob numbers (P(net ≥ 3 on 2d10) = 2·0.1·0.3 + 0.01 = 0.07). What this pass measured — P(A) = 0.05–0.09 at faculty 1 against 5–7 — is a 5D-vs-13–17D σ-contest in which faculty enters twice (pool and `lev`). **Same class** (a low bare stat on a load-bearing outcome yields a foregone conclusion that is illegible to anyone and unmovable by any choice at that input — the best line in the whole grammar is 0.080, §4.1), **same order of magnitude, different arithmetic. Not an identity.**

### §12.4 What "give the crisis side more dice" would and would not do

The skill's leverage-uniformity row says the `1/√N` non-uniformity *cannot be fixed by any pool transformation* — the Stage-4 aggregation sweep proved it. On this engine that particular pathology is largely absent (the faculty channel is roughly in-band, above), because CR6 scales the μ-shift by σ_N. What bites here is different and named by the same skill: **the flat-shift trap** (`SKILL.md:87` — *"a flat advantage … not σ_N-scaled … `Δz ∝ 1/√Pool`, hot at small pools"*), which is exactly CR4's whole pool die — and §2 row 4 measured its non-uniformity as +8.3/−3.6/−5.6 pts across pools 7/13/17, with the ruled extension supplying the sign flip; and **the quantization** of §12.2, which is a draw defect, not a leverage defect. Remapping `L → faculty` so the crisis side rolls more dice would move P(A) along the measured grid (~0.1 per faculty point) and touch none of P-i (odds still hidden), P-iii (still quantized) or P-v (still the discrete draw). **It is a re-tune, not a repair.**

The two repairs the decision rule licenses, stated as the fork it is:

- **Instance B — a deterministic+stochastic resolver on the faction's bare stat.** `P(A) = clamp(BASE + SLOPE·M)` with `M = round(L) − round(7 − Sta)` is, to within tuning, **what the production path already computes de facto** (the §1.1 grid is that function, evaluated expensively through six moves and five judges) — made legible (P-i), flat (P-ii), cheap, and free of the draw. **Ratified precedent for the faction layer: ED-874 (Jordan, "works well", 2026-05-31).** Its numbers are `PROPOSED — Jordan's to ratify/tune`; the form is canonical; nothing here presents a tuning value as settled.
- **Aggregate, then A** — build the roster PR #362 §C.5.1 specifies (`PersonId[]` at weight), so the pool is healthy *and* a setup axis exists, and switch the draw to `roll_net_continuous` so the leverage layer is not rounded away. This is what the session's proposals bet on, and it requires a `Person` producer that does not exist (§1.3).

These lead to materially different games — a legible faction-scale resolver versus a person-scale contest — and the tree's precedent (ED-874) and its architecture (PR #362 §C.5.1) point opposite ways. **That is the one fork in this document that survives `CLAUDE.md` §0's five tests; it is recorded here, not as a ledger row (§0, 2026-08-19 amendment), and it is not this pass's to answer.**

### §12.5 Property verdict for the production path (P-i…P-v)

| property | verdict | evidence |
|---|---|---|
| **P-i** legible odds | **FAIL** — no surface exposes them; the odds are a function of two integers nobody sees, and `ContestView` withholds the venue and judge (§3.3) | §1.2, §3.3 |
| **P-ii** uniform leverage | faculty channel: roughly in-band (measured); **leverage layer: FAIL** (0 / +0.21 / +0.13 / +0.11); CR4 die: FAIL (flat-shift trap, sign-flipping) | §12.2, §2 row 4 |
| **P-iii** bounded, monotonic | **FAIL** — a continuous shift quantized by integer edges; a "+1D" that lowers P(A) above pool 7 | §12.2, §2 row 4 |
| **P-iv** graded, recoverable | the ladder is four-band and survivable; **on the production proceeding the win condition returns a side** (`VoteAtClose`, A/B/draw) and the echo is ±1 — a binary on the load-bearing outcome, clamped to a no-op 75 % of the time | §1.1, `06` §10 |
| **P-v** right engine for the regime | **FAIL** — a bare stat with no axis fed to Instance A's leverage layer over the legacy discrete draw; by the decision rule it routes to B or to aggregate-then-A, and it is on neither | §12.1 |

**Stage-3 verdict for the rolling engine on the production path: NON-COMPLIANT — wrong engine (Lesson 3), with the leverage layer's own channel dead at the live input (Lessons 2/6).** The kernel's *design* is Instance A (CR2, CR6) and would pass P-ii on the continuous draw; its *execution* is the TTRPG-mode draw with the videogame layer rounded off, fed a bare stat. The 2026-05-28 verdict and the skill's own Worked Example 2 both graded the design; neither ran the draw.

---

*Closing note. §8.1 is filled from the n = 64 runs (arms A/B/E/C) and the positive-control arm P; §8's N verdict was narrowed on that evidence and the retraction is recorded in §8 and §10. The rubric changed mid-audit (§0.5); re-grades are marked as such; the second instrument was applied after the draft and its findings are in §12. One file. Nothing else was created or edited.*

---

## §8.1 · THE ABLATION — completed by the orchestrator, and the POSITIVE CONTROL DISQUALIFIES ONE OF THE TWO INSTRUMENTS

> **Provenance, stated because it changes who is accountable for this section.** The Fable auditor that
> built the harness and wrote §0–§8 **hit its model usage limit before this section could be written**.
> The arms had all completed; the analysis had not. Everything below was computed by the orchestrator
> (Opus) from the auditor's own harness and output files, unmodified. **The design of the experiment is
> the auditor's; the arithmetic and the verdict are mine.** No number here was re-derived by hand — the
> merge script is the auditor's `ners_ablate_n64.py`, extended only to admit arm P.

**Arms** (`ners_ablate.py:113-119`), 64 seeds × 50 seasons each:

| arm | what it does |
|---|---|
| **A** | baseline |
| **E** | council echo **and** §10 vote writes suppressed — everything still runs, nothing lands |
| **C** | council trigger never fires (no contest built, no `getrandbits` draw — the RNG stream shifts) |
| **P** | **positive control**: a council write that **always** lands, `+2 L` to the crisis faction regardless of verdict (`ners_ablate.py:47-52`) — *"known to matter; if the detector cannot see this, it cannot see anything."* |

### The result

```
winner distribution          chi2 vs A (3 df; p<.05 needs 7.81)
  A  Crown 53.1  Church  9.4  Hafenmark  6.2  Varfell 31.2      —
  E  Crown 39.1  Church 10.9  Hafenmark 17.2  Varfell 32.8      4.74   not detected
  C  Crown 45.3  Church  6.2  Hafenmark  9.4  Varfell 39.1      1.75   not detected
  P  Crown 54.7  Church  1.6  Hafenmark  7.8  Varfell 35.9      3.91   NOT DETECTED  ← the control
paired t, final Crown L
  A−E  +0.773   t = + 2.77     detected
  A−C  −0.625   t = − 2.68     detected
  A−P  −5.500   t = −13.26     detected, overwhelmingly
```

### ⚠ THE WINNER-DISTRIBUTION χ² IS BLIND, AND EVERY CONCLUSION DRAWN FROM IT IS WITHDRAWN

**Arm P is an intervention we know is enormous** — it hands the crisis faction `+2 L` on every one of
~4,979 councils, and the paired-t sees it at **t = −13.26**. The χ² on winner distribution **cannot
see it** (3.91, below the 7.81 threshold).

**A test that cannot detect a known +2-per-council intervention cannot detect anything smaller.** So:

- **`χ²(A vs E) = 4.74 "not significant" is not evidence of anything.** It must not be read as *"the
  subsystem does not change outcomes."* It means *the instrument is blind.*
- The same applies to `χ²(A vs C) = 1.75`.
- **This is precisely the failure `CLAUDE.md` §0.1 pt 2 names** — an assertion that cannot observe the
  failure it excludes — and precisely the reason pt 4 demands a control **in both directions**. Without
  arm P, the honest-looking reading of χ² = 4.74 was *"the social contest is inert"*, and it would have
  been **wrong, dramatic, and invisible**.

### What the WORKING instrument says

The paired t on final Legitimacy detects the control, so it is a real detector, and by it:

**The subsystem's N-line is NOT false. It has a measurable effect** (`A−E` on Crown, `t = +2.77`,
mean +0.77 L). *"Delete it"* is off the table on this evidence.

But note how narrowly it earns that, against the census from the same runs
(4,979 councils, arm A): **87.7 % won by the crisis side · 81.9 % of contests fought at side-A faculty
1 · 74.8 % of council echoes are floor/ceiling no-ops · 0.39 effective writes per season.** The
subsystem clears the necessity bar on **one faction's stat**, while three-quarters of its outputs
change nothing and seven-eighths of its contests are decided before they begin.

**And E versus C is a real distinction, not noise.** They move Crown in **opposite** directions
(`+0.77` vs `−0.63`, both detected). Suppressing the writes lowers Crown's L; never firing the trigger
raises it — because arm C skips a `getrandbits` draw and desynchronises the campaign stream. That is
the difference between *does nothing* and *does nothing but consumes entropy*, and both are true of
different parts of the subsystem.

### What would overturn this section

1. **A larger n.** The auditor's own Monte-Carlo power table (§0) puts this detector's rate at **0.51
   for a 20-point distribution shift and 0.15 for 10 points**. The paired-t is the sensitive
   instrument; the χ² needs several hundred seeds to be worth running at all.
2. **A harness defect.** Arm P proves the harness *can* land a write and the detector *can* see it,
   which is the strongest available evidence that arms E and C suppress what they claim. It does not
   prove the suppression is exactly scoped.
3. **A second control in the opposite direction** — an arm that suppresses something known to be inert,
   which should be indistinguishable from A on every instrument. Not run.

> **The method lesson, which outlives the numbers.** The positive control did not confirm the result —
> **it disqualified an instrument**, and in doing so prevented a false headline. An ablation without a
> positive control is not a measurement; it is a story with numbers in it.
