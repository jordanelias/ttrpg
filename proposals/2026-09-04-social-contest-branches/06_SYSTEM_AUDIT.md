# 06 · SYSTEM AUDIT — `systems/social_contest/` on twelve axes

## Status: **AUDIT — read-only, PROPOSED disposition of findings, 2026-09-04. Nothing ratifies on merge. This file is the only artifact; no other file was created or edited.**
## Auditor: Fable 5.1, `CLAUDE.md` §10 audit/guardrail node. Tree: branch `claude/social-contest-system-review-dn2y5d`, HEAD `7a23b831`.
## Grade of the subject under `CLAUDE.md` §0.2: **one game (`agon`) EXECUTES in a seeded campaign; everything else in the package is paper or test-only.** The measurements that license that sentence are in §0.3 and §12.

---

## §0 · Status, reading log, method, and what this is not

### §0.1 What was read (in this order)

1. `SESSION_BRIEF.md` (1,015 lines) and `SC_INVENTORY.md` (744 lines) — treated as maps. Every anchor I depend on below was re-opened; the inventory's concatenated-file line numbers were **not** inherited (see §0.4).
2. `05_RECONCILIATION.md` in full; `00`–`04` section maps plus the tree-facing sections (`00 §1`, `01 §1.9/§7.4`, `04 §1/§3/§5.4`).
3. **Every `.py` under `systems/social_contest/`** (21 files, 7,306 lines) and the seven `.md` heads, `social_contest_v30.md` (724 lines) in full.
4. Seams: `engine/cross_scale/scene_dispatch.py`, `echo_transport.py`, `parliamentary_bridge.py`, `domain_echo.py:79-124`; `engine/substrate/composition.py`, `keys.py:300-335`; `engine/autoload/sigma_leverage.py:1-120`, `dice_engine.py:95-135,200-260`, `game_state.py` (MULTS/adjust/floors), `scene_slate.py:30-60`; callers `engine/mc_v18.py:55-300`, `systems/factions/sim/parliamentary_action.py`, `faction_action.py` (censure call site), `tribunal.py:95-125`.
5. Registries: `references/module_contracts.yaml` (`social_contest` row `:739-771`, composition roles `:87-181`, the three consumer rows), `engine/engine_params/key_types.json` (the five declared types), `registers/editorial_ledger_sc.jsonl` (all 32 rows; 0004/0014-0019/0021/0022 in full), `registers/handoffs/HANDOFF_SC.md`.
6. Gates: `engine/tests/test_contest_kernel.py`, `test_mc_v18_regression.py:140-158`, `test_echo_transport.py:95-115`, `test_pipeline_reach.py:825-895`, `tests/valoria/test_import_cycle_game_state_npe.py:56-96`, `test_flow_skeletons.py` (anchor rule), `.github/workflows/valoria-ci.yml` (job list), `tools/balance_oracle.py:140-175`.
7. `04_CODE_ARCHITECTURE.md` (PR #362) §0, §A.1, §C.1, §C.2, §C.4 (grep), §C.5, §C.5.1; `CLAUDE.md` in full.

### §0.2 Method

Per axis: one verdict sentence, then findings worst-first, each with a `path:line symbol` anchor I opened. Where a claim is a *count* it carries the command or script that produced it. Where a claim is an *upper bound* it says so. A null result is recorded in §15 with the evidence of the look, not dropped.

### §0.3 Execution artifacts (read-only w.r.t. the repo; scripts and outputs in the session scratchpad, not committed)

The task permits `python -c` arithmetic. I extended that to **driving the engine under a line/call tracer**, because §0.2 makes "does it run" the grade that matters and the question is unanswerable by reading. No `pytest` was run. Nothing under the repo was written.

| artifact | what it measured | headline |
|---|---|---|
| `trace_sc.py` — `sys.settrace` over two 50-season `mc_v18.run_campaign` runs (seeds 0, 42) | which lines/functions of `systems/social_contest/` execute | **141** kernel contests built and resolved, **130** parliamentary votes; call counts in §12 |
| `calls_sc.py` — seed 0, function-call census | which kernel functions are **never** called in a live campaign | 27 named functions at zero calls, listed in §12.1 |
| `instrument_sc.py` — wraps `_resolve_slot` and `Faction.adjust` | per-council `(season, faction, L, Sta, verdict, faculties)`; every writer of `Faction.L` | crisis side wins **128/141**; side-A faculty is **1 in 137/141**; six writer sites of `L` (§3, §5) |
| direct `build_contest`/`resolve_contest` loops | production-venue win-probability surface; mirror symmetry; band distribution | §5.1, §14.1 |
| `policy_sweep.py` — 11×11 round-robin of `POLICIES` on two venues, N=150, 5-vs-5 | dominance among the **shipped** policy set | §5.2 |
| Key capture — wraps `emit_scene_echo` | the actual `scene.contest_resolved` Keys a campaign emits | `participants: []` on every one (§2) |

### §0.4 What this is not, and one method note

This is not a NERS pass, not a proposal, and not a fix list; it emits no ledger row (`CLAUDE.md` §0, 2026-08-19 amendment — every finding here is either fixable in a commit or is design context; none needs Jordan to answer a question that the tree does not already answer, with one exception named in §13).

**Method note.** `SC_INVENTORY.md` and my own first read both numbered `primitives.py` from a `cat -n` that concatenated `contract.py` (77 lines) in front of it; my first reachability probe of `primitives.py` used those offset numbers and was discarded. Every `primitives.py` anchor below is the true file line (checked against `Reserve.COST` at `:51`, which the inventory also cites). Same correction applied to `faction.py` (−60), `narrative.py` (−214), `appraise.py` (−274), `contest/__init__.py` (−139), `parliamentary_stay.py` (−220).

---

## §1 · FLEXIBILITY

**Verdict: nothing about a contest can be varied without editing Python except which module provides it; the eight canonical proceedings are eight rows that differ in only four fields, and the venue library that would make them different is unreachable from the one production entry point.**

**F1.1 — `proceeding_venue` discards the venue library. (worst)** `modes.py:536-567 proceeding_venue` builds `Venue(budget=budget, win=win, **o)` at `:567` and `build_contest` calls it with no `**o` (`wrapper.py:133`). So every one of the eight `PROCEEDINGS` rows (`modes.py:485-519`) inherits `resolver.py:150-166 Venue`'s dataclass defaults: proof `.30/.30/.40`, equal tense weights, `DefeatCatalogue()` defaults, `Pressure()` none, `allow_rebuttal=False`, `split_standing=False`. The four groundup presets (`modes.py:66-82`), three institutional modes (`:121-154`) and six cross-cultural venues (`:166-325`) — ~260 lines of venue design with per-venue proof registers, fault catalogues and win-conditions — are reachable only by constructing a `Bout` or `ContestedMode` directly, which no production path does (§12.1). A "Royal Audience" and a "Casual Dispute" differ, mechanically, in `budget`, `win`, and the adjudicator's `[SEED]` character. The `roles` and `resistance` fields are read by nothing that resolves (`grep` of `["roles"]`/`['roles']` over `systems/social_contest engine` returns zero readers; `["resistance"]` is read only by `_derive_resistance`, whose output is metadata — `wrapper.py:75-79`).

**F1.2 — the engine hardcodes a subsystem's vocabulary.** `scene_dispatch.py:118 EMERGENCY_COUNCIL_PROCEEDING = "guild_arbitration"` is a literal `PROCEEDINGS` key inside `engine/`. The same file resolves the side labels through `composition.require('contest_side.a')` (`:337`) precisely so that "the engine must not hardcode a subsystem's vocabulary" (`module_contracts.yaml:171-175` note). A rename in `PROCEEDINGS` would make `build_contest` raise `ValueError` (`wrapper.py:130`), which `_resolve_slot`'s `except Exception` (`scene_dispatch.py:373-375`) converts to a silently deferred scene. The only observer is `test_mc_v18_regression.py:151-158`, and §6.6 shows that observer cannot see it.

**F1.3 — a rule doing a config field's job.** `dictionaries.py:696-697 PANEL_DEFAULT_JURORS = inspect.signature(_modes.panel).parameters["size"].default` — a numeric parameter recovered by introspecting another module's function signature so that "the one bench-size literal lives once". It lives once, but the reader is a reflection call, not a declaration. `modes.py:521-534 _use_tracker` derives a tri-state from two fields (`tracker: bool`, `tracker_mode: str`) that encode one fact; `wrapper.py:52 spec["resistance"].startswith("halved")` parses a stringly-typed rule out of a label.

**F1.4 — a config field doing a rule's job, in prose.** `MECHANICS[...]["toggle"]` (`wrapper.py:361,367,368`) carries strings like `"Bout(armature=…, cr5=True)"` — instructions to a human, in a registry the self-test reads for `status` only (`:443-444`).

**F1.5 — no typed export.** `engine/engine_params/` holds no contest artifact (`ls`: `combat_engine_v1.json, composition.json, descriptors.json, game_constants.json, key_types.json, module_contracts.json, params_tables.yaml, sim_params.json, value_pointer_links.json, world_initial_state.json`). Under `CLAUDE.md` §0.05/§5 the ~100 named constants (`SC_INVENTORY.md §H`, reproducible) plus the table cells in `STYLE_AXIS` (`armature.py:242-247`), `PROCEEDINGS`, `STYLES_TABLE`, `Reserve.COST` (`primitives.py:51`), `Dossier.CORROB` (`:295`) are all "the migration backlog". `dictionaries.py:7` states there is "deliberately NO data/*.yaml layer" (locked decision 3, 2026-06); that decision predates the §0.05 ruling (2026-08-24) and has not been re-examined against it.

**What CAN be varied without a code edit:** which module provides `build_contest`/`resolve_contest`/`run_parliamentary_vote`/`Motion`/`VoteDeclaration`/`A`/`B` (`references/module_contracts.yaml:94-101,163-181` → `composition.json`, blocking `--check` in CI at `valoria-ci.yml:141`), the `ECHO_TRANSPORT` and `DISPATCH_COMBAT_BRIDGE` env/params flags (`mc_v18.py:65-89`), and the Key-type roster (`key_types.json`, exported from markdown behind `--check` at `:127`). That is the complete list.

---

## §2 · KEYS

**Verdict: of five declared Key types, one is produced — outside the subsystem, with a payload that satisfies the roster vacuously — and none is consumed by any code; the registry describes a two-cycle between edges that do not exist.**

Real roster: `engine/engine_params/key_types.json` (`scene.dialogue` :7, `scene.insult` :88, `scene.threat` :114, `scene.contest_resolved` :954, `state.opinion_revised` :1338). Declared for `social_contest` at `module_contracts.yaml:747-753`.

| Key type | declared | producer in code | consumer in code | finding |
|---|---|---|---|---|
| `scene.contest_resolved` | emits | `echo_transport.py:427-439 Key(...)`, keyed by `KEY_TYPE_BY_SCENE["contest"]` (`:109`) — **not in `systems/social_contest/`** | **none.** `grep -rn contest_resolved --include=*.py engine systems tools` minus tests → `echo_transport.py:109` and two docstring lines in `tools/contract_runtime_conformance.py:13,217`. `articulation.subscribe_all` (`articulation.py:153-169`) subscribes 13 trigger type_ids to stub-wire callbacks; the roster's declared consumers (`npc_behavior, faction_layer, articulation`) have no reader | **produced-with-no-consumer**, and see K2.1 |
| `scene.dialogue` | emits | none (`grep` over non-test `.py`: only `tools/contract_runtime_conformance.py:19` prose) | none | declared-with-no-producer |
| `scene.insult` | emits | none | none | declared-with-no-producer |
| `scene.threat` | emits | none | none | declared-with-no-producer |
| `state.opinion_revised` | consumes | (npc_behavior; not this audit's scope) | **none in `systems/social_contest/`** (grep: zero hits) | declared-consumed-with-no-consumer |

**K2.1 — the one live Key is content-free. (worst)** Captured from a seed-0 campaign (`§0.3`): `('scene.contest.s4.n2', 'scene.contest_resolved', {'scene_id': 'contest_2', 'outcome': 'initiator_win', 'participants': []}, [('Varfell','subject',{'L': 1})], ['personal'], 'persistent', 'near')`. `participants` is `[]` on **every** live emission because the emergency-council context deliberately carries no `parties` (`scene_dispatch.py:93-94`) and `echo_transport.py:425-426` builds the list from `ctx.get("parties") or ctx.get("participants") or []`. `validate_payload` (`keys.py:308-320`) checks field *presence*, so an empty list passes. The Key records no proceeding, no verdict band, no side faculties, no `reason` — the `out["result"]` dict that has all of these (`scene_dispatch.py:308-309`) is dropped at `_resolve_slot`'s return. `scale_signature` is `personal` for a contest between two faculty integers derived from one faction's aggregates.

**K2.2 — the parliamentary vote emits under the contest scene's Key type.** `parliamentary_bridge.py:183 emit_scene_echo("contest", {...})` — a faction-scale procedure with no scene, no persons and no proceeding is logged as `scene.contest_resolved`, `scale_signature: personal`, `participants: []`, `scene_id: parl_sN`. Captured live (`'scene.contest.s2.n0' … scene_id 'parl_s2' … {'I': 1}`). 55 of the 196 deferred `L`/`I` writes in the two traced campaigns came through this path (§3).

**K2.3 — the registry documents a loop that has no edges.** `module_contracts.yaml:758-759` (social_contest `loops`) and `:347` (npc_behavior `loops`) describe a 2-cycle "emits `scene.contest_resolved`/`scene.dialogue`, consumes `state.opinion_revised`", graded `BOUNDED [verification LD-1]` with dampers. Neither edge exists in code (table above). The `[OPEN — Jordan]` at `:347` is a question about a cycle that cannot occur; under `CLAUDE.md` §0's five tests it closes at rung 2 (irrelevant: the subject was never built).

**K2.4 — the emitted delta is recorded even when the write is a no-op.** `echo_transport.py:441-455 _apply` calls `Faction.adjust`, which floors `L` at 0 (`game_state.py:179,189-195`). In the traced campaigns 137/141 councils had side-A faculty 1 (`L ≤ 1`) and 128 resolved `Failure` (−1); once `L == 0` the Key still carries `stat_deltas={'L': -1}` and the log hash still moves, while the world does not. PR #362 §C.2 names this `NoOpReceipt` and refuses it; the substrate here records it as a write.

---

## §3 · STATE CHANGES

**Verdict: the subsystem's only persistent effects are writes to `Faction.L`/`Faction.I` through three distinct paths with two different timings, and a process-global RNG reseed; every other write is bout-local and dies with the `Bout`.**

Persistent writes originating in or triggered by this subsystem, with the instrumented count over seeds 0+42 (100 seasons):

| # | field | writer | timing | count | second writer of the same field |
|---|---|---|---|---|---|
| W1 | `Faction.L` | `parliamentary_vote.py:214 run_parliamentary_vote` (Total-Victory −1) | immediate, inside the action phase | 31 | W2, W3 and three non-SC sites: `faction_action.py::_try_conquest` 68, `excommunication.py::attempt_excommunication` 8, `parliamentary_transfer.py::propose_transfer` 3 |
| W2 | `Faction.L` / `Faction.I` | `echo_transport.py:441-455 _apply` (deferred closure from the council echo `scene_dispatch.py:336-345` and the vote echo `parliamentary_bridge.py:176-184`) | **deferred** to `accounting_boundary` (OF-7, `:457`) | 196 | W1, W3 |
| W3 | `Faction.L`, `Faction.Sta` | `parliamentary_action.py:157-158 propose_censure` (FA-lane, but only reachable through this subsystem's vote) | immediate | 15 | W1, W2 (L); `faction_action.py:579` (Sta) |
| W4 | `world._echo_key_seq` | `echo_transport.py:422-423` and `:317-318` (two functions), initialised `mc_v18.py:258` | immediate | per Key | three writers of one counter |
| W5 | `world.key_log` (append) | `echo_transport.py:457 sched.emit` | immediate log, deferred apply | 193/169 per campaign | — |
| W6 | `world.scenes_resolved` | `mc_v18.py:150` (councils) and `:160` (votes) | immediate | — | two increments into one telemetry counter, which is what makes §6.6's gate blind |
| W7 | process-global `random` state | `scene_dispatch.py:299 random.seed(rng.getrandbits(32))`, restored `:303` | during the contest | 141 | any other global-`random` consumer; the kernel draws from it at `resolver.py:32,139,144,334` |
| W8 | `slot.context["echo"]` | `scene_dispatch.py:344`, `parliamentary_bridge.py:178` | transient (slot is popped) | — | two shapes (4 keys vs 6 keys) into one consumer, `echo_transport.py:390-401` |

**S3.1 — one stat, two timings, one season. (worst)** W1 and W3 land during the action phase; W2 lands after it. A faction can take an immediate −1 (`propose_censure`, before `run_scene_phase` at `mc_v18.py:149`) and a deferred ±1 from its own council in the same season, and the vote that runs *after* the council (`mc_v18.py:156-160`) derives its roster from `L` values the council has already moved on paper (`parliamentary_bridge.py:97-99`). This is the concrete live-path instance of the invariant `05_RECONCILIATION.md §5` calls observably violated; §14.3 sharpens *where* it is observable.

**S3.2 — a primitive's field written around its own mutators.** `resolver.py:362 c.reserve.cur = min(c.reserve.max, c.reserve.cur + Reserve.COST["evidence"])` assigns `Reserve.cur` directly to refund an evidence spend; `Reserve` owns `spend`/`regroup` (`primitives.py:55-56`) and nothing else writes `cur`. This is the `CLAUDE.md` §0.1 pt-1 shape (a second write path a future mutator change would silently miss). Unreached in production (§12.1), so latent.

**S3.3 — what does NOT persist, said plainly.** `Standing`, `Reserve`, `Room`, `FaultState`, `Dossier`, `ContestState`, `Bout.live`, `Bout.log` are per-`Bout` (`resolver.py:241-248`) and are discarded at `_resolve_slot`'s return; `Chronicle` is never built in production (§12.1). There is no record of *which* contest happened, only of the stat it moved — the "no record spine" finding (ED-SC-0019) restated as a state-write table.

---

## §4 · PLAYABILITY

**Verdict: in the shipped campaign no one decides anything — both sides are `logos_spammer` and every one of the 846 traced moves was `advance(logos, live_ground)`; the per-decision consult load the harness was built to measure has never been measured, and when the kernel *is* played the decision surface is two or three prompts per exchange, most of whose information changes nothing.**

**P4.1 — zero decisions on the production path. (worst)** `resolve_contest`'s defaults are `policy_a=logos_spammer, policy_b=logos_spammer` (`wrapper.py:248`); the seam passes none (`scene_dispatch.py:301`). `policy.py:6-8 logos_spammer` returns `Move("advance", LOGOS, live_ground)` unless `reserve_frac < 0.3` (`:5`), which with budget 3 and `Reserve.MAX=12`/`COST["advance"]=3` (`primitives.py:50-51`) never triggers: 12 → 9 → 6. Trace: `logos_spammer` 846 calls = `_apply` 846 = `_reception` 846; `regroup`, `build_ethos`, `shift`, `present`, `strip_points` zero. The contest is a fixed script whose only variable is dice.

**P4.2 — the consult load was never measured.** `agon_harness.py:1-12` exists to measure the "~13 consults per exchange" claim (audit D4/N-7); it has zero callers and `HANDOFF_SC.md` records that no human has played it. What the harness would count, read off `agon_harness.py:347-361 human_turn`: `kind` (`:347`), `style` (`:353`), `appeal` if advance/hard (`:357`), `ground` if shift (`:361`) — **2–3 discrete prompts per exchange**, not 13. The 13 was a count over the *prose* loop (§11), which has no engine.

**P4.3 — decisions with no information to base them on.** (a) The `Move.appeal` choice (ethos/pathos/logos) is the largest lever in the kernel — `_advance`'s gain multiplies `venue.joint_weight(appeal, tense)` against `adj.character()` through `leak` (`resolver.py:323-326`) — and `ContestView` (`contract.py:53-66`) exposes **neither** the venue's proof weights nor the adjudicator's character; only `audience_learned`/`audience_hostile`. The sweep (§5.2) shows the best appeal flips with the venue (`demagogue` 0.82 before a crowd, 0.52 before the expert panel); the view carries no signal for that. `narrative.venue_brief` (`narrative.py:157-170`) would supply it and is never called. (b) The Style card (CR4/armature) is a choice against a hidden `armature_position` that the production seam cannot populate (`wrapper.py:215-216` passes no `armature=`), so an Appraise reveal via `appraise_armature` (`appraise.py:140-177`) reads a vector that cannot act — information about a lever that is not connected.

**P4.4 — information that changes nothing.** `Contest.resistance`, `Contest.primary_attribute`, `Contest.track_start` (`wrapper.py:74-80`) are computed and carried for display; the resolver reads none of them (`Venue.base_ob` is never set from resistance — `:75-79` says so; `Pool.size` takes an abstract `faculty`, `primitives.py:211`). `ContestView.evidence_available` (`contract.py:66`) is always 0 in production (`_as_contestant` builds no dossier from a bare int, `wrapper.py:97-98`). `ContestView.can_hard` is exposed while `hard` is never licit before a learned, non-hostile bench (`primitives.py:216-217`), which is every production bench (`modes.py:433-438,456-461`).

**P4.5 — the compromise band eats symmetric play.** Direct measurement, 1,000 mirrors, faculty 5 v 5: `formal_contest` with `logos` → **995/1000 `committee`**; `grand_contest`/`logos` → 989; `courtier` → 857/773; `demagogue` → 652/546. With equal faculties and the shipped `[SEED]` gain scale (`MERIT_SCALE=2.6`, `resolver.py:39`; track scale 1.5, `:86`), the Persuasion Track rarely leaves 4–6 in three exchanges. Whether that is the intended feel of a Formal Contest is a calibration question; that it is *unmeasured* is the finding.

---

## §5 · FAIRNESS

**Verdict: side symmetry holds and no first-mover advantage exists; the live equilibrium is degenerate in a different way — the one production contest is a 91 %-predetermined ritual against a faction already at the floor, and among the shipped policies there is a venue-dependent dominant strategy.**

All "no dominant option" claims below are bounded to the **shipped `POLICIES`** (`policy.py:56-60`); no best-response sweep over the full move space (`VALID_KINDS`, `resolver.py:34`) was run, so they remain upper bounds on the design and lower bounds on the exploit.

**FA5.1 — the emergency council is a doom-ritual. (worst)** Instrumented: 141 councils; verdict `b` (the "crisis" side) **128**, `a` **13**; side-A faculty `round(L)` was **1 in 137/141** (`scene_dispatch.py:139`), side-B faculty `round(7−Sta)` 5–7. Win-probability grid on the production venue, N=400: A-faculty 1 → **P(A)=0.07** against B 5/6/7; faculty 5 → 0.48/0.46/0.40; only at faculty ≥7 does the leadership side reach parity. Varfell fired the trigger **37 consecutive seasons** (14–50, seed 0) with `L` already 0 by season 15: the −1 `Failure` echo (`domain_echo.py:106-114`) is floor-clamped and the contest decides nothing. `evaluate_triggers` (`scene_dispatch.py:82-84`) re-fires on `Sta ≤ 2` every season with no hysteresis (the ED-749 hysteresis `social_contest_v30.md:427` mentions lives elsewhere, if anywhere). **Exploit surface:** none for a player — no one plays it. **Degenerate equilibrium:** a faction in crisis is guaranteed a losing council every season until `L` hits 0, after which the mechanism is inert but still runs.

**FA5.2 — venue-dependent dominance among shipped policies.** Round-robin, N=150 per pair, 5 v 5:

| venue | mean win-rate (as A / as B averaged) | head-to-head |
|---|---|---|
| `guild_arbitration` (production: 5×`expert_judge`, `VoteAtClose`) | `build_then_close` **0.81** › `logos` 0.76 = `advocate` 0.76 › `courtier` 0.65 › … › `staller` 0.14 › `overreacher` 0.05 | `build_then_close` beats `logos` 0.60 |
| `grand_contest` (`crowd` 15, `PersuasionTrack`, budget 5) | `demagogue` **0.82** › `exploiter` 0.78 › `courtier` 0.61 › `build_then_close` 0.57 › `logos` 0.40 | `demagogue` beats `build_then_close` 0.84, `courtier` 0.79 |

The reason is arithmetic, not strategy: `crowd` ships `discipline=0.30, char_pathos=0.55` (`modes.py:445-446`), so `leak = 0.70` (`primitives.py:244-245`) and pathos resonance ≈ 0.47 vs logos ≈ 0.23 (`resolver.py:326`); `expert_judge` ships `discipline=0.75, char_logos=0.55` (`modes.py:438`). A policy that reads the adjudicator type wins ~2:1; the `ContestView` does not expose it (§4.3). Pathos additionally feeds `Room` → `Readiness` (`resolver.py:333,338-339`), a self-reinforcing loop with no counter in the shipped move set.

**FA5.3 — the self-destructing policies are venue-blind.** `overreacher` (`policy.py:43`, always `hard`) is barred on move 1 before any learned non-hostile bench (`primitives.py:216-217` → `resolver.py:376-377` → clinch `:457-461`); `staller` yields twice; `off_ground_chancer` evades twice; `counterpuncher` (`:45-54`) rebuts in the back half and — since no canonical proceeding sets `allow_rebuttal` (`modes.py:567` passes none) — each rebut is an evasion (`resolver.py:368-369`), two of which lose (`primitives.py:267` default). ED-SC-0022 F4 is confirmed by reading and by the sweep (`counterpuncher` clinch 0.50/0.79).

**FA5.4 — asymmetries that are venue design, not bugs (recorded so they are not re-found).** `ProofBar` awards the defender at close on any shortfall (`resolver.py:70-72`); `GraceThreshold` likewise (`:76-78`); `SelfGating` licenses `hard` only when `opp < my − 1` before an unlearned or hostile judge (`primitives.py:216-217`). None is reachable from `PROCEEDINGS` (F1.1).

**FA5.5 — attacks that failed.** Mirror matches (1,000 each, three venues, four policies): `guild_arbitration` A/B splits 527/473, 534/466, 531/469, 538/462; `grand_contest` bands symmetric within noise (e.g. `demagogue`: A_dec 164 / B_dec 185, A_tot 56 / B_tot 49); mean `adv[A]` ≈ `adv[B]` to three decimals in every row. **No side-A bias, no first-mover advantage**, despite A moving first at `resolver.py:443` and `DefeatCatalogue.check` iterating A first (`primitives.py:273`; irrelevant because the check runs per move, `resolver.py:457`). `contest_legacy_stub.py:174-178`'s tie-to-A rule (ED-SC-0022 F7) is dead code (§12).

---

## §6 · LOGIC

**Verdict: the resolution atom is internally consistent; the defects are at its edges — a ratified aggregation rule that is behaviourally inert on every bench the code can build, a penalty that cannot bite at the standing it is designed for, a gate that cannot see the failure it exists to catch, and three latent type traps.**

**L6.1 — `weighted_by_standing` equals `simple_majority` on every constructible bench. (worst)** `VoteAtClose` weights ballots by `Adjudicator.discipline` (`resolver.py:133`). Every bench factory builds homogeneous members: `panel()` → 5 × `expert_judge(**o)` (`modes.py:456-461`), `crowd()` 15 × identical (`:440-447`), `_default_panel` (`:115-119`), `excommunication_mode` (`:291-297`), `secret_council_mode` (`:304-310`). Equal weights reduce `wA*2 > total` to a head count. The ratified ED-1057 rule (`dictionaries.py:685`) therefore decides nothing in any reachable contest; the heterogeneous bench that exercises it exists only in `_kernel_tests.py:1159-1194`. Not a bug in the code — a ratified mechanism with no reachable input.

**L6.2 — the CR5 backfire is inert below `Standing.START`.** `strip_points` (`primitives.py:37-46`) lowers `Standing.v`; the only readers of standing in reception are `cred_frac()` → `Readiness.of` and `Resonance.leak` (`resolver.py:323,333`), and `Standing.frac` (`primitives.py:47`) is `max(0, (v − 5)/5)`. A mover at or below 5 who is stripped to 3 has the same `frac` (0) as before: **the penalty changes no reception**. It bites only on standing built above 5 by ethos (`:35`), and it also lowers `rank_v` for the `hard` gate (`resolver.py:376`). `rhetoric.py:413-454` bounds the strip by standing (judge finding 4) but nothing makes the strip *matter* at default standing. Latent in production (armature unreachable), live in the harness and tests.

**L6.3 — Face scale-binding cannot execute through the public API.** `FaceScale.face_max(charisma)` returns `charisma * 3` (`primitives.py:142`); `_as_contestant` never sets `charisma` (`wrapper.py:97-105`), so `_Side.face_max()` (`resolver.py:230-232`) raises `TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'` (executed). ED-SC-0022 F2, confirmed.

**L6.4 — two latent traps at the seam.** (a) `_derive_resistance(proc, world)` (`wrapper.py:43-56`) reads `stabilities` only if `isinstance(world, dict)` (`:47`); passing the live `World` object returns 0 silently (executed: World-like object → 0; dict → 4; halved → 2). The seam passes nothing today (`scene_dispatch.py:300`), so the trap has no victim yet. (b) `Panel(())` raises `ZeroDivisionError` in `discipline`/`character` (`contract.py:47,51`; executed); `crowd(size=0)` would build one.

**L6.5 — the prose ambiguity is coded both ways.** `dictionaries.py:78` ("A single per-**exchange** choice (social_contest_v30 §4 Step 2)") and `armature.py:418-419` ("a single per-**contest** choice, social_contest_v30 §4 Step 2") cite the same sentence for opposite contracts. `ArmatureConfig` is frozen (`armature.py:414`) so the code is per-contest; the harness reassigns `Bout.armature` per exchange to get the other reading (`agon_harness.py:63-70`, "WORKAROUND 2"). Root: `social_contest_v30.md:87` ("fixed at setup — no mid-contest changes") vs `:160` (a per-exchange Step 2).

**L6.6 — the one production-path gate cannot observe the failure it excludes.** `test_mc_v18_regression.py:151-158` asserts `sum(scenes_resolved) > 0` over the seed-0 batch; `world.scenes_resolved` is incremented for councils (`mc_v18.py:150`) **and** for parliamentary votes (`:160`). Votes resolve every season two eligible factions exist (130 in the trace). The assertion is satisfiable with zero kernel contests; the failure mode it names in its docstring ("the party-derivation bridge may have regressed") would pass it. `CLAUDE.md` §0.1 pt 2 exactly. The fix is one expression (`_report["dispatch"]["resolved"]` is already available at `mc_v18.py:149`), not a new guard.

**L6.7 — arithmetic checked and found consistent (so they are not re-derived).** `PersuasionTrack.resolve` bands (`resolver.py:91-95`) are symmetric about 5 and agree with `parliamentary_vote.py:199-208`'s integer thresholds; `_derive_resistance`'s `ceil(avg) − 1` then `ceil(base/2)` matches `social_contest_v30.md:94,392`; `degree_from_net`'s ladder (`dice_engine.py:280-293`) with `PoolDesaturation` (`degree_extension.py:77-82`) can only demote (`may_overwhelm` returns a bool consulted in one branch — STRUCTURAL by signature, `dice_engine.py:95-135`); `Venue.tense_weight` guards a zero sum (`resolver.py:170`); `VoteAtClose` guards a zero-weight bench (`:137-138`); `_view` guards a zero-max reserve (`:277`).

---

## §7 · INTERDEPENDENCIES

**Verdict: the declared couplings are three composition roles and one Key type; the load-bearing couplings are accidental — a global RNG, a shared stat with six writers, a legacy re-export that drags a nine-module import cycle into the vote, and a registry note that says a caller is routed when it is not.**

**Declared (and honoured):** `scene_builder.contest`, `scene_resolver.contest`, `contest_side.a/b`, `parliamentary_vote`, `parliamentary_motion`, `parliamentary_vote_declaration` (`module_contracts.yaml:94-101,163-181`) resolved at first use by `composition.require` (`composition.py:57-69`) with an export-time blocking gate (`valoria-ci.yml:141`) — MECHANICAL; `BandExtension` injection (`resolver.py:26,270,307-308`); the `KEY_TYPE_BY_SCENE` map (`echo_transport.py:108-111`).

**Accidental, ranked by what breaks what:**

| # | coupling | anchor | what breaks |
|---|---|---|---|
| I7.1 | **Global `random`.** The kernel draws from the module-level stream (`resolver.py:32 roll_net`, `:139/:144 random.gauss`, `:334 random.uniform`); the seam reseeds it from `world.rng` and restores it (`scene_dispatch.py:297-303`) | any other consumer of global `random` inside the contest window; any future caller that forgets the save/restore desyncs the campaign goldens | the reproducibility of every seeded campaign rests on a `try/finally` in one caller |
| I7.2 | **`Faction.L` has no owner.** Six writer sites across four subsystems and the engine (§3 table) | ED-SC-0015 stacking is one instance; any new Mandate rule composes with five others by accident | the 2×`L` on a Total-Victory censure |
| I7.3 | **The vote imports the whole kernel for five integers.** `parliamentary_vote.py:44-51` imports `PERSUASION_*` from the package, whose `__init__.py:35-50` re-exports them from `contest_legacy_stub.py:67-71` and `:53-99` imports all 13 kernel modules — the 9-module SCC (`test_import_cycle_game_state_npe.py:56-96`) — before a single die is rolled for a faction vote | any import-time failure in `armature`/`rhetoric`/`dictionaries` breaks the parliamentary path, which does not use them | the faction-scale seam depends on personal-scale Stage-3 code it never calls |
| I7.4 | **`parliamentary_action.py:41-45` imports the provider by name** while `module_contracts.yaml:84-92` states all three callers route through the registry | a provider swap in the registry moves two of three callers | the registry's own note is false about one caller (`SC_INVENTORY.md §B3` found this; re-verified) |
| I7.5 | `dictionaries.PANEL_DEFAULT_JURORS` reads `inspect.signature(_modes.panel)` (`:696-697`) | renaming `panel`'s `size` parameter breaks `panel_win_condition` at import | a signature is a coupling surface |
| I7.6 | The seam names a `PROCEEDINGS` key (`scene_dispatch.py:118`) and swallows every kernel exception (`:373-375`) | a kernel `ValueError` becomes 100 % deferred scenes with `scenes_resolved` still > 0 via votes (L6.6) | silent |
| I7.7 | `Stability Crisis` ↔ council ↔ `L` echo ↔ vote roster (`_derive_vote` picks proposer = lowest `Sta`, `parliamentary_bridge.py:97`) | the faction in crisis is also always the vote's proposer; two SC mechanisms hit the same faction every season | FA5.1's loop has a second leg |
| I7.8 | Church Tribunal / Excommunication exist twice with no code edge: `modes.py:495-501,200-217,291-297` vs `systems/factions/sim/tribunal.py`, `excommunication.py` (no `social_contest` import; `tribunal.py:95-125` rolls `L` vs `L`) | two implementations of one canon section drift independently | the inquiry branch's B2 regression (`05_RECONCILIATION.md §1`) is this coupling made explicit |

---

## §8 · PRIMITIVES

**Verdict: the genuinely primitive layer is four things owned upstream (`roll_net`, `net_boost`, `degree_from_net`+extension, `Faction.adjust`) plus three in-package stores (`Standing`, `Reserve`, `Room`); most of what wears a primitive's name is a composition, the Record primitive is unused, and the false-N-line pattern appears twice in the kernel itself.**

**Genuine primitives (single-owner, minimal, something composes on them):** `sigma_leverage.roll_net`/`net_boost`/`level` (`sigma_leverage.py:190,210,269`); `dice_engine.degree_from_net` with `BandExtension` (`dice_engine.py:95,227`) — the one seam that is STRUCTURAL by signature; `Standing` (`primitives.py:31-47`), `Reserve` (`:49-56`), `Room` (`:232-236`), `Stasis` ladder (`:11-25`), `FaultState` (`contract.py:16-22`), `DefeatCatalogue` (`primitives.py:262-279`).

**Compositions wearing a primitive's name:**

| name | what it is | anchor |
|---|---|---|
| `Face` | `= Standing` (an alias, honestly declared) | `primitives.py:108` |
| `FaceScale` | a pure function of `Standing` and an attribute the kernel does not hold | `:132-149` |
| `Readiness`, `Resonance` | weighted blends of `Standing.frac`, `Room.frac`, `discipline`, `character` | `:253-260`, `:238-251` |
| `Leverage.net` | `(faculty − 4)/6 + level("moderate")` — a **second δσ derivation** outside `sigma_leverage.levels_to_net_sigma` (`:224-236`) | `primitives.py:228-230` |
| `_advance`'s gain | `MERIT_SCALE · deg · res · rdy · U(1±JITTER) · bias` — six factors, five of them `[SEED]` | `resolver.py:334` |
| `Venue.joint_weight` | `role × RhetoricalWeights(3×3) × tense_weight` — three multiplicative layers whose "row sums = 3.0" neutrality is asserted in a comment (`primitives.py:187-189`) | `resolver.py:172-178` |
| `PersuasionTrack` | a linear map `5 + 1.5·(advA − advB)` banded by four literals | `resolver.py:86-95` |
| `ArmatureConfig.dsigma` | `STYLE_AXIS[style] · position`, normalised, clamped ≥ 0, × `level("moderate")` | `armature.py:357-371,436-451` |

**PR8.1 — the false-N-line pattern, inside the kernel. (worst)** `14_NERS.md`'s signature is *a mechanism was named, a store was proposed for it, and the store's job was already being done by an object the design had ruled in.* Two instances ship today: (a) `PersuasionTrack`'s band literals (`resolver.py:91-95`) re-implement `PERSUASION_WIN_THRESHOLD`/`_LOSS`/`_TOTAL_VICTORY`/`_TOTAL_DEFEAT` (`contest_legacy_stub.py:67-70`) — the constants the vote consumes; the kernel does not import them. (b) The neutral start `5` is spelled four ways: `CANONICAL_TRACK_START = 5.0` (`modes.py:475`), `PERSUASION_TRACK_START_DEFAULT = 5` (`contest_legacy_stub.py:71`), `PersuasionTrack(start=5.0)` default (`resolver.py:86`), `5.0 + lobby` (`faction.py:142`); and the ED-621 clamp `[4, 6]` lives at `parliamentary_vote.py:71-72` and again as literals at `faction.py:142`.

**PR8.2 — the Record primitive is single-owner and unused.** `systems/settlements/sim/ledger.py:36-44 LedgerTag`, `:47 ledger_add` (dedupe), `:69 ledger_sweep` (TTL) — durable, on `Settlement.ledger` (`:14-16`). Zero references either way (`SESSION_BRIEF.md §9` confirmed; re-grepped). One real obstacle the brief's "compose, do not reinvent" does not name: **a `LedgerTag` needs a settlement and a live contest has no place** — the council context carries `faction` only (`scene_dispatch.py:89-95`), the vote carries none. Composing on the ledger requires a `place` the scene does not know, which is the negotiation critic's F9 ("the term has no carrier") one level down.

**PR8.3 — `faction.coalition_vote` is a fourth resolver built from primitives without the loop.** `faction.py:128-148` hand-builds `ContestState`, calls `roll_net` per side (`:143-145`) and `PersuasionTrack.resolve` (`:146`) with no exchanges, faults, policies or stasis. It shares the atoms and none of the composition — and has zero production callers (§12).

---

## §9 · OWNERSHIP

**Verdict: inside a `Bout` ownership is clean (one writer per field, by construction); across the seam it is not — the band thresholds have three owners, the neutral start four, `Faction.L` six writers, the venue's win-condition is built twice per contest, and the `WIRED` word has two meanings.**

Violations, ranked:

| # | thing | owners/writers | anchors |
|---|---|---|---|
| O9.1 | Persuasion band thresholds `9/7/3/1` | `resolver.py:91-95` (literals) · `contest_legacy_stub.py:67-70` (constants) · consumed at `parliamentary_vote.py:199-208` | PR8.1(a) |
| O9.2 | neutral track start `5` | four spellings (PR8.1(b)) | — |
| O9.3 | `Faction.L` | six call sites, three timings (§3) | — |
| O9.4 | the proceeding's win-condition | `proceeding_venue` builds `panel_win_condition()` at `modes.py:553-555`; `build_contest` rebuilds it at `wrapper.py:181-190` (`dataclasses.replace`) — trace: `panel_win_condition` **282** calls for 141 contests | duplicate construction, both correct, one dead |
| O9.5 | `Reserve.cur` | `Reserve.spend/regroup` and a bare assignment at `resolver.py:362` | S3.2 |
| O9.6 | `world._echo_key_seq` | `mc_v18.py:258`, `echo_transport.py:317-318`, `:422-423` | W4 |
| O9.7 | `CONCENTRATION_MULTIPLIER = 3` — a formula struck by ED-901 — is still a public export | `contest_legacy_stub.py:63` → `contest/__init__.py:42,104` | ED-SC-0022 F5, confirmed |
| O9.8 | **the word `WIRED`** | `MECHANICS["adjudicator_armature"/"cr4_stasis_genre"/"cr5_self_gating"]["status"] = "WIRED"` (`wrapper.py:361,367,368`) means "fires in a directly-built `Bout`"; `"audience_resistance"` was downgraded to `PARTIAL` (`:337`) for being "derived but not plumbed into resolution" — the identical condition the three Stage-3 rows are in at the seam | `CLAUDE.md` §4's idempotent-in-meaning test: a later reader takes `WIRED` as live |
| O9.9 | `Bout.armature` | a plain attribute (`resolver.py:259`) reassigned per exchange by `agon_harness.py:441` — an outside writer of kernel state the kernel does not re-validate | harness-only |

**Clean, and worth saying:** `Standing.v` (three methods, `primitives.py:35-46`), `Bout.live` (`resolver.py:356` only), `ContestState.adv` (two sites in one method, `:335,373`), `FaultState` fields (all in `_apply`), `Bout.log` (`:453`), `GAMES`/`MECHANICS`/`PROCEEDINGS` (built once, never mutated — `SC_INVENTORY.md §D2` sweep, re-checked by reading).

---

## §10 · CODE SHAPE vs PR #362

**Verdict: the subsystem conforms on the manifest seam and the ladder veto, violates §C.5's contract on four of its five leaks by construction, and inverts §C.5.1's roster rule; almost every grade is CONVENTION because CI runs no checker that could see the difference.**

Grades use PR #362 §0's rule: STRUCTURAL = the defect has no spelling; MECHANICAL = one path and a named test sees a bypass; CONVENTION = a reader notices. CI runs `pytest tests/valoria` (`valoria-ci.yml:365`), `pytest engine/tests` (`:405`) and the seven `export_*.py --check` gates (`:126-150`); nothing else grades code shape.

| PR #362 clause | what the tree does | grade (runtime) |
|---|---|---|
| §A.1 / Stage 2 §D.4 — provider resolved by role, by string, at boot | `composition.require` at first use (`composition.py:57-69`), targets validated at export behind `--check` (`valoria-ci.yml:141`) | **MECHANICAL** (a typo reds CI; `KeyError` at `:60-65` refuses an undeclared role) |
| §C.5 leak 5 — `veto: bool`, ladder takes the minimum, "STRUCTURAL by signature" | `BandExtension.may_overwhelm → bool`, consulted in one branch (`dice_engine.py:95-135`); `validate_context` refuses undeclared keys | **STRUCTURAL by signature** — the one row that earns the word |
| §C.5 leak 1 — "a state write from inside — no token, STRUCTURAL" | `Bout` writes only its own state ✓; but `run_parliamentary_vote` writes `Faction.L` from inside the provider (`parliamentary_vote.py:214`) and `propose_censure` writes `Sta`/`L` (`parliamentary_action.py:157-158`) | **violated; CONVENTION** — no token exists, `Faction.adjust` is callable from anywhere (`game_state.py:153`) |
| §C.5 leak 2 — "a second resolver — CONVENTION" | four resolvers coexist (`Bout`, `run_parliamentary_vote`, `coalition_vote`, `run_contest`) | **violated; CONVENTION** (PR #362 grades it so itself) |
| §C.5 leak 3 — `claimants : PersonId[]`, "a faction as combatant — STRUCTURAL" | claimants are faculty **ints** derived from one faction's `L`/`Sta` (`scene_dispatch.py:139`); the vote's claimants are factions (`parliamentary_bridge.py:105-106`) | **violated; the defect has a spelling and is spelled** — CONVENTION |
| §C.5 — "a subsystem returning a winner has not met the contract — a type assertion" | `Bout.resolve` returns `(winner_or_band, reason)` (`resolver.py:466`); `resolve_contest` returns that plus the `Bout` (`wrapper.py:217`) | **violated; CONVENTION** (`01_SPINE.md` proposes `margin()`; not in tree) |
| §C.5 — Events "into the same log; an unregistered kind fails" | one Key, built outside the subsystem, payload vacuous (K2.1); `KeyValidationError` on unregistered type (`keys.py:304-306`) | registration **MECHANICAL**; content **CONVENTION** |
| §C.5.1 — sides resolved ONCE from the projection, held for the contest | sides are derived **at resolve time from the live world**, on purpose (`scene_dispatch.py:93-94` "derived at RESOLVE time (freshest world state)") | **inverted; CONVENTION** |
| §C.1 driver — `deliberate(frozen)` a map, `resolve` at barrier 3 | `mc_v18.py:124-160`: faction actions, scene dispatch and the vote all mutate inside one action callback with no barrier; OF-7 defers some writes (§3) | **absent; CONVENTION** |
| §C.2 gate — every mutation crosses one write path with a receipt; `NoOpReceipt` refused | `Faction.adjust` is the path; no receipt; floor-clamped no-ops are recorded as Keys (K2.4) | **absent; CONVENTION** |
| AX-4 one owner, one writer | §9 | **CONVENTION** |
| AX-1 only a person acts | no `Act`, no `PersonId` anywhere in the subsystem | **absent** |
| §0's honesty rule (a claimed STRUCTURAL that is MECHANICAL) | `degree_extension.py:16-18` claims "the constraint became STRUCTURAL" — correct: `may_overwhelm` cannot promote by signature. `01_SPINE.md` I-S6a's STRUCTURAL claim was already downgraded by the critic (`05_RECONCILIATION.md §14.3`) | — |

**What CI actually enforces about this subsystem's shape:** the composition targets resolve (`export_composition.py --check`), the engine imports no `systems.*` (`test_engine_does_not_import_systems.py`, cited `CLAUDE.md` §3), exactly two import-cycle families exist (`test_import_cycle_game_state_npe.py:70-96` — verified: it asserts `len(cycles) == 2` and one family per prefix, **not** a member count, confirming `SESSION_BRIEF.md §11.1`), the kernel self-suite is green at exactly 389 checks (`test_contest_kernel.py:93`), and the stub rows self-flag (`test_pipeline_reach.py:831-892`). Everything else above is CONVENTION at runtime.

---

## §11 · PROSE-vs-CODE DIVERGENCE

**Verdict: `social_contest_v30.md` §§3–9 and §11 describe a resolution model that has no engine, the kernel's actual model has no canonical prose, they agree only on the Persuasion Track bands and §10; under §0.05 every row below is a defect in the PROSE (it claims a mechanism that does not exist) or in the CODE (it claims to implement prose it does not), and the resolution is to change the code — never to promote the prose.**

The three-lens audit (ED-SC-0017) stated the headline; this table is the row-by-row instrument, with the side that is wrong named. "Prose-defect" means the doc claims a mechanism the game does not have; "code-defect" means the code claims to implement a rule and does not; "both" means each claims the other.

| § | prose (`social_contest_v30.md`) | code | which is defective | note |
|---|---|---|---|---|
| §2 Step 3 :62-89 | genre/audience bonus dice, faction boosts, Guilds boost "resolved by the engine" (`:80`) | `guilds_boost_for` exists (`dictionaries.py:473-487`) and is called by nothing (§12.1); no faction-boost die anywhere in `_reception` | **prose** claims an engine rule; **code** ships an uncalled function labelled as the rule | — |
| §2 Step 4 :94 · §7 :392 | audience resistance from Stability, halved for the disadvantaged | derived (`wrapper.py:43-56`) and never plumbed (`:75-79`; `Venue.base_ob` untouched) | **code** (self-declared `PARTIAL`, `:337`) | ED-1055..1079 reserved |
| §2 Step 5 :104 | Church Tribunal exchanges "1–5 (Inquisitor sets)"; roles "Inquisitor proposes throughout" | budget is always `max` (`modes.py:551`); no role concept — A always moves first (`resolver.py:443`) | **prose** (no engine) | roles field unread (§1) |
| §3 :121 | Argue Pool = (Primary×2) + History, adjudicator-type primary attribute | `Pool.size(faculty) = max(5, 2·faculty+3)` (`primitives.py:211`), `[SEED]`; `primary_attribute` is display metadata (`wrapper.py:74`) | **both** — ED-SC-0004 (open fork, RATIFIED-AS-ACCEPTED 2026-07-05 per its row, unexecuted) | — |
| §4 Step 1 :146-158 | a per-exchange Appraise roll with a 4-band reveal | no `appraise` in `VALID_KINDS` (`resolver.py:34`); `appraise_armature` is a pure function no resolver calls | **prose** | `agon_harness.py:52-62` WORKAROUND 1 |
| §4 Step 2 :160 vs §2 Step 3 :87 | per-exchange style pick vs "fixed at setup" | frozen `ArmatureConfig` (per-contest) | **prose contradicts itself**; code picked one and cites the other (L6.5) | — |
| §4 Step 2b :162 · Step 3 :169-172 | Corroborate, Recall +2D, Grand-Contest per-source Recall, Momentum spend | none | **prose** | ED-SC-0005 cap question is about dice the code never rolls |
| §4 Step 3 :174-180 | "Every adjudicator … carries a hidden `armature_position`"; CR4 +1D fires "from the opening exchange" in Church Tribunal (`:398`) | `positions` is an empty dict unless a caller fills it (`armature.py:429`); no production caller can pass an armature (`wrapper.py:215-216`) | **prose** (claims a live mechanism) and **code** (`MECHANICS` says `WIRED`, O9.8) | ED-SC-0022 F1 |
| §4 Step 4 :182-210 | CLASH/REINFORCE/CROSS/TIE: compare successes head-to-head, margin − resistance, strain | each side's reception is rolled **independently** against `base_ob` (`resolver.py:302,307`) and accumulates `adv`; no comparison, no margin, no strain; `derive_interaction` (`dictionaries.py:310-323`) is called by nothing | **both** — the doc's loop has no engine; the kernel's loop has no prose | ED-SC-0017 (a) |
| §4 Step 4 :212-220 | Doubt Marker, Terminal Doubt (ED-1060) | `DOUBT_MARKER` is a design-table string (`dictionaries.py:201-235`, "DESIGN-TABLE COMMITMENT ONLY", `:229`) | **prose** ("implemented as the terminal-value rule", `:220`, while the same sentence admits the resolver does not consume orientation) | — |
| §4 Step 5 :228-230 | Regroup (track +1 to opponent, restore to max), Concede | `support`: +2 net reserve, +0.8 Standing, no track cost, no fault (`resolver.py:350-351`); `pass`: a yield fault (`:345-348`) | **both** — different semantics under a shared name | `00_BRANCH_SHAPES.md §1` "silence clinch is dodgeable" |
| §4 Step 6 :232-262 | strain → Face → Rattled −1D; Concentration 5/exchange, −5 on loss, Spent −2D | no strain (grep: zero non-comment hits); `Reserve` spends per move by `COST` (`primitives.py:51`); empty reserve → yield fault, not −2D | **prose** (the honesty note `:248` is the code's, restated) | — |
| §4 Step 6 :248, §8 :519 | "Standing.strip() is never called … Face is monotonic-up" | `strip_points` fires at `resolver.py:437` (CR5) | **prose and the comment at `primitives.py:83-85`** are stale in the conservative direction | ED-SC-0022 F3 |
| §5 :268-272 | rolled first-to-speak, transfers to winner | A first, always | **prose** | — |
| §6 :302 | Contest Fatigue, +1 Momentum, Disposition, Reputation shifts | only in the dead legacy stub (`contest_legacy_stub.py:250-257`) | **prose** | — |
| §6 :290-293 · scale_transitions §5.2 | Decisive+Memory → Mandate +1; Compromise → nothing | live: A-win → `Success` +1 L; B-win → `Failure` **−1 L on the same faction**; draw → nothing (`scene_dispatch.py:336-345`, `domain_echo.py:106-114`) | **code** adds a −1 the SC prose does not state (it is scale_transitions' Failure row applied to a self-contest) | FA5.1's mechanism |
| §6.1 :306-358 · §6.3 :368-383 | Obligations (durations, violation costs), chain contests | no `Obligation` in any `.py` except `tribunal.py`'s comment; no chain | **prose** | ED-SC-0019 |
| §7.1 :624-641 | Excommunication Tribunal, track start 7, prerequisites | `excommunication_court_venue` uses `ProofBar(3.0)` (`modes.py:215`), unreachable; FA-lane `tribunal.py` rolls `L` vs `L` with no track | **both** (two implementations, neither the prose) | I7.8 |
| §7.2 :400-437 | Succession Contest; split ratios `:421-423` | `faction.succession` (`faction.py:86-118`), zero production callers; the split table is anti-monotone on A's side (`:107,:117`) | **prose is the root** (`05_RECONCILIATION.md §6`); code faithfully inherits it | ED-SC-0016 |
| §7.3 :441-489 | Heresy Investigation lifecycle | `scene_resolver.investigation` is stub-wired (`scene_dispatch.py:353-360`) | **prose** | — |
| §9 :531-585 | prep, coalitions, Thread ops, Beliefs, Niflhel | none (Beliefs only in the dead stub `:240`) | **prose** | — |
| §10 :589-611 | BG vote | `parliamentary_vote.py:125-220` matches step for step | **agree** — except "Mandate −1 for **one season**" (`:611`) is permanent (`:214`, no restore facility) | ED-SC-0022 F6 |
| §10.1 :647-659 | Parliamentary Stay | implemented (`parliamentary_stay.py:54-106`), zero callers | **code is dead; prose describes an unreachable mechanism** | — |
| §11 :615-620 | Hybrid contest | none | **prose** | — |

**Resolution under §0.05, stated once:** every "prose" row above is a design doc asserting a mechanism; the game does what the code does. Deciding which rows to *build* is design work; declaring the prose authoritative for any of them is the move §0.05 forbids. The two rows marked "code" (resistance; the −1 Failure echo) and the `WIRED` rows are where the code misdescribes itself and should be corrected in code and its own comments.

---

## §12 · DEAD SURFACE

**Verdict: a seeded 50-season campaign executes 35.6 % of the package's executable lines and calls none of the kernel's build/strip/regroup/present/shift/track mutators; measured by function, the production game is `advance` → `_reception` → `_advance` → `VoteAtClose`, and everything else in 7,306 lines is test-only, harness-only, or unreachable.**

### §12.1 Measured (seeds 0 and 42, 50 seasons each; §0.3)

- Executable-line coverage of `systems/social_contest/`: **1,315 / 3,698 (35.6 %)**, and that figure is *generous* because import-time definition lines count as hit. Per file: `resolver.py` 194/288, `modes.py` 114/238, `wrapper.py` 138/229, `primitives.py` 142/162, `contest_legacy_stub.py` 43/137, `parliamentary_vote.py` 112/124, `narrative.py` 25/119, `faction.py` 32/102, `armature.py` 52/98, `rhetoric.py` 52/87, `appraise.py` 29/62, `parliamentary_stay.py` **0/56**, `policy.py` 22/54, `degree_extension.py` 19/38.
- Call census (seed 0, 117 scenes): `_apply` 846 = `logos_spammer` 846 = `_reception` 846; `_advance` 699 (so 147 receptions banded `Failure`); `resolve` 705 = 141 `Bout.resolve` + 564 `VoteAtClose.resolve` (3 non-closing + 1 closing per bout); `panel_win_condition` 282 (2 per contest, O9.4); `expert_judge` 705 (5 per contest).
- **Zero calls in a live campaign:** `Standing.build`, `Standing.strip`, `Standing.strip_points`, `_Side.build_ethos`, `Reserve.regroup`, `Room.build`, `Dossier.present`, `SelfGating._hard_licensed`, `PersuasionTrack.track`, `_Side.face_max/face_current`, `ArmatureConfig.dsigma`, `cr5_self_backfire`, `primary_genre_pool_bonus`, `appraise_armature`, `derive_interaction`, `guilds_boost_for`, `_crosscheck_proceedings`, `mechanics_selftest`, `proceeding_mode`, `*Mode.play`, `narrative.summarize`, `faction.vote/succession/coalition_vote`, `invoke_stay`, `run_contest`, and the `shift` branch.

### §12.2 Inventory of dead surface, with the reason it is dead

| surface | lines | reason | reachable by |
|---|---|---|---|
| `agon_harness.py` | 522 | zero callers (confirmed) | a human at a terminal |
| `contest_legacy_stub.py` functions `build_argue_pool`/`resolve_exchange`/`run_contest` | ~180 of 268 | zero callers; the module's docstring names a caller path that no longer exists (`contest/__init__.py:24-25` → `sim/cross_scale/scene_dispatch.py:105`) | nothing |
| `parliamentary_stay.py` | 106 | zero callers, 0 lines hit | nothing |
| `faction.py` | 154 | zero production callers | `_kernel_tests.py` |
| `narrative.py` | 170 | `record=False` on the seam (`scene_dispatch.py:301`), `summarize` uncalled | tests, harness |
| `appraise.py` | 177 | no resolver calls it | tests, harness |
| `modes.py` venue library (`:66-325`), `ContestedMode`, `proceeding_mode`, `CANONICAL_PROCEEDINGS` | ~300 | F1.1 — `proceeding_venue` passes no preset; `ContestedMode.play` has no production caller | `_kernel_tests.py`, `balance_oracle.py` |
| `resolver.py` `ThresholdRace`, `ProofBar`, `GraceThreshold` | 26 | no `PROCEEDINGS` row uses them | direct `Venue(win=…)` |
| `resolver.py` move kinds `hard/shift/support/pass/evidence/rebut`, the armature/CR4/CR5 block (`:399-438`), `split_standing`, `allow_rebuttal`, `Pressure` | ~90 | no production policy issues them; no production armature; no venue flag set | tests, harness |
| `dictionaries.py` everything except `panel_win_condition` (`STYLES_TABLE`, `INTERACTIONS_TABLE`, `derive_interaction`, `ADJUDICATORS_TABLE`, `FACTION_BOOSTS`, `guilds_boost_for`, `DOUBT_MARKER*`, `PROCEEDINGS_TABLE`, `_crosscheck`) | ~700 | typed prose read by tests; `STYLES_TABLE` is read by `armature`/`rhetoric`, which are unreachable | tests |
| `wrapper.py` `GAMES` stub rows, `_stub`, `game=` parameter, `MECHANICS`, `_SYMBOLS`, `_resolve`, `_stage3_resolution_invocation_check`, `mechanics_selftest` | ~130 | `game` never passed; self-test called only by `_kernel_tests.py:822` | tests |
| `PersuasionTrack` on the production seam | — | `guild_arbitration` → `panel` → `VoteAtClose` rebind (`wrapper.py:181-190`); the canonical Persuasion Track never closes a live contest | any other proceeding name in `ctx["proceeding"]` (`scene_dispatch.py:290`), which nothing sets |
| `social_contest_system_v2.md` + index | 513 | banner-superseded (`social_contest_system_v2.md:2-11`) | readers |
| `social_contest_flow_skeleton_v1.md` anchors | 184 | traced at `6545067`; e.g. `wrapper.py:106 build_contest` is now `:110`; the guard (`test_flow_skeletons.py:76 SYMBOL_WINDOW = 3`) accepts `:106` because the symbol name appears in a string at `:106-107` (`raise TypeError(f"build_contest: …")`) | — (reference only; no guard proposed, `CLAUDE.md` §0.1 pt 5) |
| `_identifier_census.yaml` | — | **untracked** (`git ls-files` → not known to git); a leftover of a prior `pytest` run's `generated_layer` fixture, not a repo surface | — |
| 97 dangling `params/contest.md` citations | — | `SC_INVENTORY.md §H2` count, spot-checked at `modes.py:475`, `rhetoric.py:206`, `wrapper.py:38,311-317` | — |

**D12.1 — the "three trackers" are one in production.** `TRACKERS` (`primitives.py:154-166`) names Face, Concentration, Persuasion; in the traced game Face never moves (no ethos, no strip), Concentration only decrements (`spend` 846, `regroup` 0), and the Persuasion Track is not the win-condition. The `MECHANICS["three_trackers"]` row is `WIRED` (`wrapper.py:330`).

---

## §13 · CROSS-AXIS SYNTHESIS

Five things the twelve views agree on that no single view shows:

1. **There is one game, and it is not the one the prose or the registry describe.** The executable social contest is: two faculty integers from one faction's `L`/`Sta` → six `advance(logos)` moves → a five-headed identical bench → a head count. The prose describes a fourteen-step exchange (§11); the `MECHANICS` registry says 23 mechanics are `WIRED` (§9); the `module_contracts` row says the subsystem emits four Key types and closes a loop (§2). Axes 4, 5, 11 and 12 measure the same object from four sides and it is the same small object. **Every proposal in `00`–`04` composes on the kernel's unreached branches** (armature, faults, `ProofBar`, `evidence`, `DefeatCatalogue` strikes) and inherits, at the seam, the reachability defect that keeps them dark. `05_RECONCILIATION.md §7` says "nothing here is a reason to rebuild `agon`"; this audit agrees, and adds: nothing here is a reason to build *on* `agon` before the seam can pass a venue, a policy and an armature — three parameters, not a rebuild.

2. **The seam is where the design leaks out.** F1.1 (venue library discarded), F1.2 (proceeding name in the engine), P4.1 (policies defaulted), the missing `armature=`, `record=False`, no `world=` — six parameters at one call site (`scene_dispatch.py:300-301`) are the entire distance between the kernel that exists and the kernel the tests exercise. ED-SC-0022 F1 named one of the six.

3. **Everything that binds, binds to `Faction.L`, and `L` is nobody's.** §2, §3, §5, §7 and §9 converge on the same fact from different directions: the only durable consequence of any social act is a ±1 on one shared stat with six writers and two timings, floor-clamped to a no-op for the factions the mechanism actually fires on. The "no record spine" (ED-SC-0019) is not a missing feature; it is why axes 2, 3 and 5 each found the same emptiness.

4. **`WIRED`, `RATIFIED`, `CLOSED` are three words for "exists in a test".** L6.1 (ratified aggregation inert on every constructible bench), O9.8 (`WIRED` at the kernel, unreachable at the seam), K2.3 (a ratified-bounded loop with no edges), §11's Doubt-Marker row ("implemented as the terminal-value rule" in a table nothing reads). `CLAUDE.md` §0.2 already says a juncture is done when it runs; this subsystem's own vocabulary has not caught up, and a reader who trusts the words is wrong five times.

5. **The gates that would catch a regression cannot see one.** L6.6 (the only production-path test counts votes as contests), I7.6 (kernel exceptions become deferrals), K2.4 (no-op writes are logged as writes), and — for the proposals — the spine's §7.4 falsifier (§14.3 below). Four different observers, all blind to the same class of silent failure. This is `CLAUDE.md` §0.1 pt 2 as a pattern across the subsystem rather than a one-off.

**The one item that survives the five `needs_jordan` tests** (`CLAUDE.md` §0, 2026-08-24): whether the emergency council's B-win should write `Failure` (−1) to the faction's own `L` (FA5.1, §11 row §6). Rung 3 answers half of it — scale_transitions §5.2's Failure row is canon and `domain_echo.py:106-114` implements it — but applying a *self-contest's* loss as a *Failure* against the acting faction is a modelling choice `scene_dispatch.py:327-331` made explicitly ("the honest instantiation … the degenerate binary case") and flagged `[SEED]`. Two defensible readings lead to materially different games (a crisis that drains Mandate to zero versus one that merely fails to restore it). Everything else in this audit closes at rungs 1–5.

---

## §14 · WHAT WOULD MAKE THIS AUDIT WRONG, AND THE ATTACKS THAT FAILED

### §14.1 Attacks run on the kernel that FAILED (reported as failed)

| attack | method | result |
|---|---|---|
| side-A / first-mover bias | 12 mirror matches × 1,000 bouts (3 venues × 4 policies); mean `adv` per side | **no bias** — splits within ±4 % of 50/50, mean `adv` equal to 3 d.p. (§5.5). My own sweep's "A wins 19 % of `demagogue` mirrors" was the committee band (546/1000), not asymmetry — corrected before use |
| `DefeatCatalogue` A-first ordering | read `primitives.py:273` against `resolver.py:457` | inert — the check runs after every move, so faults are never simultaneous |
| `VoteAtClose` draw on the production bench | 5 jurors (odd) → `wA*2 == total` impossible with equal weights | 0 draws in 8,200 bouts |
| Persuasion band asymmetry | `resolver.py:91-95` vs `parliamentary_vote.py:199-208` | symmetric about 5; agree with each other |
| resistance rounding | executed `_derive_resistance` on `[6,6,2]` → 4; halved → 2 | matches `social_contest_v30.md:94,392` |
| `BandExtension` promotion path | `dice_engine.py:95-135` | none by signature — the STRUCTURAL claim is earned |
| the 9-module cycle test pins a member count | `test_import_cycle_game_state_npe.py:70-96` | it does not; `SESSION_BRIEF.md §11.1` stands |
| `parliamentary_action` routed through the registry (registry note) | `parliamentary_action.py:41-45` | direct import — the note is wrong, the inventory was right |

### §14.2 What would make the measurements wrong

- **Two seeds.** All campaign figures are seeds 0 and 42, 50 seasons. A seed in which no faction reaches `Sta ≤ 2` would show zero councils and the same coverage minus `resolver.py`; a seed with a high-`L` crisis faction would move FA5.1's 91 % toward the grid's 0.48 at faculty 5. The *structure* (faculty from `round(L)`, floor at 0, no hysteresis) is read from code and does not depend on the seed.
- **The tracer counts definition lines as hit.** The 35.6 % is an upper bound on runtime reach; the call census is the reliable instrument and the §12.1 zero-call list comes from it.
- **N=150 in the sweep.** Differences under ~0.08 between adjacent policies are noise; the venue-flip (`demagogue` 0.82 vs 0.52) and the top-vs-bottom gaps are not.
- **The sweep covers eleven policies, not the move space.** A best-response over `VALID_KINDS × Appeal × ground` per exchange was not run; FA5.2's dominance is among what ships.

### §14.3 Where this audit disagrees with, or sharpens, `05_RECONCILIATION.md §5 SURVIVED`

- **"Jordan's ruling is observably violated in shipped `agon` today … `_emergency_council_parties:139` reads the stats a prior scene moved."** *Sharpened, not contradicted.* Within one season, `evaluate_triggers` queues at most one council per faction (`scene_dispatch.py:82-96`), and councils are self-contests, so **no second council reads a stat a prior council moved.** The live stale read is `parliamentary_bridge.py:97-99 _derive_vote` (and `parliamentary_vote.py:169 _resolve`'s Mandate pools), which run after `run_scene_phase` in the same callback (`mc_v18.py:149-160`) and read `L` values the deferred council echo has not yet applied. The violation is real; its observer is the vote, not a second scene.
- **The spine's §7.4 falsifier (`01_SPINE.md:1078-1122`) cannot observe what it excludes on the factions the trigger actually fires on.** It queues two councils for one faction and asserts `world.factions[fid].L != before` after `run_scene_phase`. In the traced campaigns 137/141 councils had `L ≤ 1` and 128 resolved to a −1 echo; on a faction at the floor a **binding** write is a clamped no-op and `L == before` under both regimes — the test would fail (or `xfail` "correctly") for the wrong reason. The fixture must hold `L` strictly inside `(0, 7)` and the verdict must be forced or the delta positive; as written this is the §0.1 pt-2 defect the spine itself condemns two sections earlier. This is a **partial contradiction** of §5's "every link exact": the trace links are exact; the falsifier built on them is not.
- **"The `agon` binding-order trace"**'s claim that `test_echo_transport.py:107` "passes while contradicting the invariant" — confirmed: the test defined at `:107` asserts `L == before` after emit at `:114`, i.e. it pins the deferral.
- Everything else in §5 that touches this subsystem (incommensurability of `VoteAtClose`'s output — it returns labels, not a margin, `resolver.py:140-147`; import-cycle test; tribunal never used `ProofBar`, `tribunal.py:95-125`) is consistent with what I read.

### §14.4 What I could not cover (stated gaps)

- No AI-vs-AI best-response sweep over the full move space (ED-SC-0021's falsifier remains unrun); §5.2 is bounded to shipped policies.
- `_kernel_tests.py` (1,727 lines) was read selectively (the golden trace, the weighted-bench checks, the stub checks, the succession check); its 389 checks were not individually audited.
- The `v30-snapshot-2026-06-28` material (CR1–CR7 ratification text, `STRESS*.md`) was not re-read; CR-numbered claims are taken from the code's own citations.
- `engine/autoload/engine_clock.py` and the exact `accounting_boundary` ordering were taken from the spine's trace and the reconciliation's confirmation, plus `mc_v18.py:162-168`'s comment; not re-traced under the tracer.
- The consult load was not measured with a human; §4.2 counts prompts by reading the harness.
- `research/` and the game-precedent companion were out of scope for this pass.

---

## §15 · NULL RESULTS — scopes examined and found clean

| `[NULL:]` scope | evidence of the look |
|---|---|
| `[NULL: side asymmetry in Bout.resolve]` | 12,000 mirror bouts, §14.1 |
| `[NULL: first-mover advantage]` | same; `resolver.py:443` order confirmed A-first and irrelevant to outcome |
| `[NULL: draw path on the production bench]` | 0 draws / 8,200; odd bench, equal weights |
| `[NULL: unknown game / proceeding / adjudicator / move kind / appeal / ground reaches resolution silently]` | `wrapper.py:130,153,261`; `resolver.py:342,319,355,378` all raise `ValueError` — but see I7.6 for the seam's swallow |
| `[NULL: kernel-local write outside its owner]` | one exception found (S3.2); `Standing.v`, `Bout.live`, `FaultState`, `Bout.log`, registries clean (§9) |
| `[NULL: mutation of GAMES/MECHANICS/PROCEEDINGS/POLICIES/TRACKERS after import]` | `SC_INVENTORY.md §D2` grep re-read; only `_SYMBOLS.update` at load (`wrapper.py:285,295`) |
| `[NULL: random draw outside the four sites]` | `resolver.py:32,139,144,334`; `policy.py` imports no `random`; `parliamentary_vote` uses the injected `rng` (`:178`) |
| `[NULL: composition role misbinding]` | `composition.json` targets resolve; `KeyError` on undeclared role executed by reading `composition.py:59-65`; CI `--check` at `valoria-ci.yml:141` |
| `[NULL: Key type unregistered / payload field missing on the live path]` | captured Keys carry `scene_id`, `outcome`, `participants` (K2.1); `validate_payload` would raise otherwise (`keys.py:308-320`) |
| `[NULL: BandExtension can promote a band or touch Failure/Partial]` | `dice_engine.py:95-135` signature; `may_overwhelm` consulted in one branch |
| `[NULL: `_derive_resistance` arithmetic]` | executed on three inputs, §14.1 |
| `[NULL: Persuasion band thresholds disagree between kernel and vote]` | values agree (9/7/3/1 at `resolver.py:91-95` vs `contest_legacy_stub.py:67-70`); the defect is ownership (O9.1), not value |
| `[NULL: `test_import_cycle` needs updating for any spine change]` | it pins families, not members (`:70-96`) |
| `[NULL: `parliamentary_vote.py` diverges from §10 prose]` | step-by-step match `:141-208` vs `social_contest_v30.md:593-611`, except the one-season penalty (F6, already ledgered) |
| `[NULL: `parliamentary_stay.py` writes world state]` | grep for `.adjust(`/assignment: none; returns a `StayResult` (`:54-98`) |
| `[NULL: second `Key(` construction site inside `systems/social_contest/`]` | none (inventory §C, re-grepped) |
| `[NULL: research-sourced numbers in the kernel]` | every non-cited constant is tagged `[SEED]` or cites a params row (`SC_INVENTORY.md §H1`, spot-checked at `resolver.py:39-44`, `primitives.py:33,50,209,233,255-256`); none cites a historical source |
