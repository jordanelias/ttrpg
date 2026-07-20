# cluster_C-TW

_Evidence cluster dossier, read-only; archived verbatim from the agent's final message by the Fable orchestrator (2026-07-07). Verdicts pending refuter pass + Fable adjudication - see `unaddressed_areas_audit_v1.md`._

# Cluster C-TW dossier

## Reachability chain

**Verdict: total island.** No campaign path in `sim/` executes any Thread operation. Chain, dead-ended:

```
sim/mc_v18.py:108  run_season(world, action_callback=_faction_actions_callback)
sim/mc_v18.py:83   -> scene_dispatch.run_scene_phase(world, world.rng)
sim/cross_scale/scene_dispatch.py:136-140  run_scene_phase()
  -> queue_triggered_scenes() [scene_dispatch.py:64-68]
       -> evaluate_triggers() [scene_dispatch.py:37-52]: the ONLY fired trigger is
          "Stability Crisis" -> scene_type="contest". No "thread" scene_type is ever
          constructed anywhere in this function.
  -> dispatch_scenes() [scene_dispatch.py:118-130]
       -> _resolve_slot() [scene_dispatch.py:78-107]: branches only on
          st == "combat" or st == "contest"; every other scene_type falls into the
          `else` branch and is recorded as "resolver for scene_type=... not live
          (stub or unmapped)" [scene_dispatch.py:104-106].
```

`sim/thread/` is a real (non-stub) package — `operations.py` (7 entry points), `coherence.py`, `collective.py`, `opposing.py`, `co_movement.py` are fully implemented — but **nothing outside `sim/thread/` ever calls into it**:

- `grep -rln "attempt_weaving\|attempt_pulling\|attempt_locking\|attempt_dissolution\|attempt_mending\|attempt_leap\|attempt_past_pulling" sim/` → zero hits outside `sim/thread/`.
- `attempt_collective_operation` / `resolve_opposing_operations` → zero external callers.
- `draw_comovement_card` / `apply_comovement_effects` → zero callers anywhere, including from `sim/thread/operations.py` itself (§ finding C-TW-8).
- `sim/personal/knots.py`'s `form_knot`/`sustain_knot`/`check_knot_rupture` → only ever called from `sim/thread/opposing.py:238` (itself uncalled); `sim/autoload/game_state.py:173,345` only imports the `Knot` dataclass for a registry-field type comment.
- `sim/cross_scale/domain_echo.py:178 compute_thread_echo` (the ED-673 Thread Domain Echo implementation) → zero callers.
- `sim/provincial/faction_action.py`, `sim/peninsular/season.py`, `sim/peninsular/accounting.py` → zero thread/knot/coherence mentions at all.
- `sim/tests/` contains exactly three files (`test_contest_kernel.py`, `test_mc_v18_regression.py`, `test_sigma_leverage_parity.py`) — **no thread-related test exists**, so the modules aren't even exercised in isolation by the regression suite.

This is worse than the combat/contest islands: those at least have a dispatch branch (even if gated by the documented context-derivation gap). Threadwork has no dispatch branch, no scene_type, no trigger, and no test coverage. `designs/godot/skeleton/` (CLAUDE.md §6) covers 0 of Part Two's 7 operations — confirmed no `*thread*` file exists under `designs/godot/`.

## Coherence/Fatigue code-vs-canon table

| # | Canon rule | Citation | Sim behavior | Citation | Verdict |
|---|---|---|---|---|---|
| 1 | Mending costs **0** Coherence at every degree; "not a mechanical exception... structural consequence" of Amendment 3, immutable-tier authority | `canon/02_foundations_amendment_leap_mechanism.md:38`; `threadwork_v30.md:474-481`; `params/threadwork.md:275` | `attempt_mending` hard-codes `coh = -1`; blanket Partial/Failure penalty pushes it to **-2** | `sim/thread/operations.py:321`, `:185-186` | Contradicts **both** candidate readings (0 and the stale §3.2 "-1" row) |
| 2 | §3.2 table itself says Mending = -1 (contradicts §2.4/canon/02 above — an internal doc conflict, not addressed by ED-1010/1011) | `threadwork_v30.md:624` | matches the -1 base, but then over-applies degree penalty | `sim/thread/operations.py:321,185-186` | Sim follows the *weaker* of two contradictory in-doc readings, then adds a third, unsupported number on top |
| 3 | Leap costs 0 Coherence at all degrees (no Coherence line in §2.3 degree table); code's own docstring says so | `threadwork_v30.md:165-171`; `sim/thread/operations.py:224` (docstring) | `_resolve_operation` unconditionally subtracts 1 more Coherence on Partial/Failure, including for Leap | `sim/thread/operations.py:184-186` | Code contradicts its own adjacent comment |
| 4 | TW-05: POP total Coherence cost capped at **-1, "regardless of scale"** | `threadwork_v30.md:177` | Cap applied only when `scale in (Object, Personal)` — the two scales where it's already -1 without a cap; Relational+ scales left uncapped | `sim/thread/operations.py:280` | Cap logic inverted relative to the ruling |
| 5 | ED-1010/RD-2 (open): 4 witnesses establish "canonical-in-effect" total-cap = **-1** for non-FR ops | `canon/editorial_ledger.jsonl:396`; archived `resolution_diagnostic_threadwork_2026-06-11.md:90,104` | Relational+ Weave/Pull Partial/Failure = scale cost (-1) **+** blanket degree penalty (-1) = **-2**, exceeding the established cap | `sim/thread/operations.py:107-112,185-186` | Concrete sim instantiation of the still-open ED-1010 ambiguity, silently resolved toward "no cap" |
| 6 | Thread Fatigue (ED-694) replaces Contact Rounds: counts 0→(Spirit×5); per-op costs (Leap 3, passive 2/rd, Mend 4/rd, Pull 5/rd, Lock 7/rd, Dissolution 10/rd); Focus gates max ops/session | `threadwork_v30.md:185-196` | **Not implemented anywhere.** `grep -rn -i fatigue sim/thread sim/personal/knots.py` → zero hits (only unrelated `CONTEST_FATIGUE_PENALTY` in contest) | — | Total absence of the rate-limiter the archived L1 loop-check explicitly credited as a damper |
| 7 | Overweaving (+1 Ob cumulative/op in same window); healing Overweave (+2 Ob/heal, R-56); Seasonal Mending Fatigue (+1 Ob cumulative/season) | `threadwork_v30.md:306,448,483` | No state tracks prior-ops-this-window or prior-Mendings-this-season | `sim/thread/operations.py` (no such fields) | Absent |
| 8 | Leap eligibility = Approach Training tag **+** TS≥30 **+** not incapacitated | `threadwork_v30.md:146-150` | `attempt_leap` checks only `ts < 30` | `sim/thread/operations.py:226-234` | Two of three gates missing |
| 9 | R-57: Pull requires ≥5D pool; below that, cannot attempt (Lock still available) | `threadwork_v25_historical.md:62-64` (active patch, cross-ref'd `threadwork_v30.md:70-71`) | No eligibility floor in `attempt_pulling`; generic engine floor is 1D | `sim/thread/operations.py:256-262` | Missing gate |
| 10 | R-55: Dissolution vs. living being at Personal scale uses Ob = target Endurance+Spirit+armour, not the generic Depth table | `threadwork_v30.md:73-77` | `attempt_dissolution` always uses `DEPTH_OB` | `sim/thread/operations.py:302-308` | Override not implemented |
| 11 | MS/RS naming fork (ED-WR-0002, resolved "MS wins") | `canon/editorial_ledger.jsonl:577` | `sim/peninsular/ms_track.py` fully live (MS); `sim/peninsular/rs_track.py` + `sim/thread/rendering.py` are `NotImplementedError` stubs — code already picked MS, pre-empting the ruling, but implements none of Part Five's threshold-band *effects* (spontaneous Gaps/Shifting Objects, Mandate loss, Faction Fracture), only the raw number | `sim/peninsular/ms_track.py:1-92`, `rs_track.py:20-21`, `sim/thread/rendering.py:21-26` | KNOWN-TRACKED direction, but `params/threadwork.md` itself is unswept (still 100% "RS") and threshold-band consequences are entirely unimplemented regardless of name |
| 12 | Knot Mechanics: ED-912/ED-773 (resolved 2026-06-28) bidirectional −5..+5 gauge, Close starts −2, Rupture only at +5, seasonal reinforcement, "Tempered" at −5 — **supersedes** PP-632 tier-cost | `params/threadwork.md:32-52`; `canon/editorial_ledger.jsonl:399` (ED-912 resolution) | `sim/personal/knots.py` implements the **superseded** PP-632 model: fixed capacities Distant=4/Close=7, monotonic strain-until-breach | `sim/personal/knots.py:59-71,254-259` | Sim is 9 days stale against a ratified supersession, and this directly gates Coherence-adjacent Knot arithmetic (rupture −1 Coherence, Anchoring +1 Coherence) |

## Op catalog table

| Op (canon §) | Doc citation | Sim status |
|---|---|---|
| Approach Training (§2.1, prerequisite tag) | `threadwork_v30.md:100-135` | Not modeled — no tag/flag anywhere in sim; `attempt_leap` doesn't check for it (C-TW-10) |
| Diagnosis (§2.2) | STRUCK (ED-134/ED-124) | N/A — correctly absent |
| The Leap (§2.3) | `threadwork_v30.md:142-177` | Implemented, `attempt_leap` — eligibility partial (C-TW-10), Coherence-bug (C-TW-3) |
| Weaving (§2.4) | `threadwork_v30.md:260-306` | Implemented, `attempt_weaving` — Coherence cap violation at Relational+ (C-TW-5) |
| Pulling (§2.4) | `threadwork_v30.md:308-345` | Implemented, `attempt_pulling` — missing 5D floor (C-TW-11), same cap issue as Weaving |
| Past-Oriented Pulling (§2.4) | `threadwork_v30.md:346-365` | Implemented, `attempt_past_pulling` — cap applied backwards (C-TW-4) |
| Locking (§2.4, FR) | `threadwork_v30.md:367-412` | Implemented, `attempt_locking` — FR-surcharge arithmetic itself matches canon; degree-penalty stacking bug still applies |
| Dissolution (§2.4, FR) | `threadwork_v30.md:414-442` | Implemented, `attempt_dissolution` — R-55 override missing (C-TW-11) |
| Mending (§2.4) | `threadwork_v30.md:444-509` | Implemented, `attempt_mending` — worst-affected op: Coherence contradiction (C-TW-2) |
| Collective Operations (§2.5) | `threadwork_v30.md:510-525` | Implemented, `attempt_collective_operation` — but self-flagged internally uncertain: the code contains an in-line comment-trail second-guessing its own lattice-fracture formula (`sim/thread/collective.py:116-136`, "Wait — re-read canon..."); zero external callers |
| Opposing Operations (§2.6) | `threadwork_v30.md:529-597` | Implemented, `resolve_opposing_operations` — several MS-delta cells are explicitly marked as approximated proxies, not exact table lookups (`sim/thread/opposing.py:165-166,174-175`); zero external callers |
| Community Organizing / Community Weaving | `params/threadwork.md:25-29` | **Not implemented.** Zero hits for "Community Organizing"/"community_organizing" anywhere in `sim/` |
| Thread-Read (fieldwork cross-ref) | `threadwork_v30.md:175-177` | **Not implemented.** Zero hits for "Thread-Read"/"ThreadRead"/"thread_read" anywhere in `sim/` |
| Co-Movement (Part Four, fires on every op) | `threadwork_v30.md:735-773` | Implemented, `sim/thread/co_movement.py` — 15/18 cards (CM-16-18 explicitly deferred, never landed); never invoked by any `attempt_*` function (C-TW-8) |
| Rendering Stability world track (Part Five, threshold-band effects) | `threadwork_v30.md:782-825` | Numeric track only (`ms_track.py`); threshold-band *consequences* (spontaneous Gaps/Shifting Objects, Mandate loss, Faction Fracture, coup-trigger bonus) unimplemented anywhere |
| Threadcut Beings (Part Six) | `threadwork_v30.md:869-911` | Implemented, `sim/thread/threadcut.py` — zero external callers, island within an island |

## Narrative sinks

This section is dominated by **KNOWN-TRACKED** material from the 2026-07-04/05 audits (`ners_qualitative_audit_v1.md`, `edge_playability_audit_v1.md` cluster G), which I cite rather than re-discover:

- **ED-681 Rendering Crisis beats render richly but entirely outside the Key/articulation/chronicle stack** — `threadwork_v30.md §3.7` has zero "Key" tokens; the protagonist's own played scene, never a mediated render of someone else's consequence (`cluster_G_rendering.md:23`; `lens_threadwork_applicability.md:53-55`).
- **`meta.thread_woven`/`scene.thread_operation` are RENDERED-GENERIC only** — Tier-1 universal read, "weakest of all spot-checked" registry types, no stakes/causes guidance (`cluster_G_rendering.md:22,56`).
- **Off-screen/NPC-witnessed thread consequence has no rendering path at all** — a Dissolution witnessed without the player present, or Calamity radiation into an absent territory, has no Tier-2 trigger and no guaranteed Tier-3 slot; falls through to generic Tier-1 salience with no anti-starvation escape hatch (`lens_threadwork_applicability.md:62-64`). This is P-14 "only half-satisfied" per the #81 rollup (`edge_playability_audit_v1.md §5`, lines 249-250).
- **Knot formed/ruptured/scar acquired is the best-specified render** of the bunch (RENDERED-RICH, triggers #1/#6/#7) (`cluster_G_rendering.md:31`).
- **The RS/MS naming collision compounds the ambiguity** of which track (if either) would even host a future dedicated thread Key (`lens_threadwork_applicability.md:65`, "grounding-03 §1").
- The full ED-673–681 cross-system fire-path spec (Thread Domain Echo, Scene Slate factor, Settlement Thread Environment, CV drift, Case Board overlay, NPC AI doctrine — `thread_horizontal_integration_spec.md`) is marked CANONICAL and largely confirmed PRESENT at the design-doc level by the 07-04 dossier (`lens_threadwork_applicability.md:30-42`).

**What this cluster adds that is genuinely new:** the design-level Key/articulation gaps above are compounded by a total execution-layer gap this dossier is first to confirm (C-TW-1). `compute_thread_echo` (the ED-673 implementation) exists in `sim/cross_scale/domain_echo.py:178` and is **never called** by anything. Even if every Key/render-path defect the 07-04/07-05 audits found were fixed tomorrow, there is currently no source of thread events for any of those routes to carry — the sim produces zero Thread events across any campaign, so the narrative-sink question is presently moot at the execution layer, not just underspecified at the design layer.

## Exploit arena (line · safeguard · verdict)

**Line 1 — Knot-anchoring Coherence-regen dilution.** Build up to `floor(Bonds/2)+1` Close Knots (`params/threadwork.md:40`), then round-robin `threadwork_v30.md §3.5`'s Anchoring Scene (Bonds check TN7 Ob2: +1 Coherence, "Costs the Knot +1 strain," `threadwork_v30.md:668`) across N different Knots. Unlike the "Full season of non-practice" bullet immediately above it (inherently once/season), the Anchoring Scene bullet carries **no stated per-season/per-scene cadence limit**, so N Close Knots ⇒ up to +N Coherence in rapid succession, diluting the strain cost instead of concentrating it.
· **Safeguard found, but weakened underneath the prior verdict.** Coherence's hard ceiling (10) bounds per-burst payoff. The archived 2026-06-11 diagnostic's L3 loop-check gave this shape a **Pass**, citing "roster-bounded... damped and bounded" strain accumulation (`resolution_diagnostic_threadwork_2026-06-11.md:76`) — but that verdict was computed against the pre-ED-912 fixed-capacity model (monotonic strain, forced Break). ED-912 (resolved 2026-06-28, **after** that diagnostic) replaced it with a bidirectional gauge where Close Knots start at −2 and **decay −1/season when rested and undisturbed** — meaning a large-enough roster, rotated with rest, can keep every Knot oscillating near its safe floor indefinitely, never nearing Rupture on any single relationship.
· **Verdict: safeguard is stale, not absent.** The prior "Pass" has not been re-run against the model actually in force since 2026-06-28. Recommend re-running L3.

**Line 2 — Exploitation-Site arbitrage.** `settlement_layer_v30.md §4.9`: any faction/actor who discovers a Thread Proximity≤2 site can harvest — RS −0.5/harvest/season, Wealth +1 to the harvester (`settlement_layer_v30.md:559`) — with no cap on simultaneous harvesters per site or sites per harvester.
· **Safeguard found, but it is intentional-and-systemic, not per-actor.** Already logged as **verified deliberate** tragedy-of-the-commons (R-6, `ners_qualitative_audit_v1.md:221-222`) — the design's own safeguard is the eventual shared-RS collapse toward Rupture, not a mechanical throttle. The only concrete throttle found is Niflhel's own AI doctrine self-limiting to "1 Dissolution/season max" at RS≤30, suspended at RS≤20 (`thread_horizontal_integration_spec.md:202`) — but that gates **only the Niflhel AI faction**, not a player or any other faction, which remains free to out-harvest it.
· **Verdict: accepted-as-deliberate at the systemic level; the player/AI asymmetry (nothing stops a player exceeding Niflhel's own self-imposed cap) is the sharp, un-flagged edge inside an otherwise-endorsed mechanic.**

**Line 3 — Company/War-scale thread-cost arbitrage (rides ED-1010).** `mass_battle_v30.md §A.10`'s table states War-scale (Structural, the deepest/most powerful target) Coherence auto-cost as **−2/op** (`mass_battle_v30.md:530`) in the same paragraph asserting "The Coherence cap (−1 per operation...) applies. No additional surcharge" (`mass_battle_v30.md:533`) — the exact self-contradiction ED-1010/RD-2 already logs. Whichever reading a future Godot port encodes determines whether Structural-depth mass-battle casts cost the same −1 as Territorial-depth ones, collapsing the intended depth-cost curve.
· **Safeguard found but incomplete.** TS≥70 gates access to Structural depth at all (character-build gate, not a per-use throttle); War-scale battle classification is presumably determined by the battle's own size, not selectable by the practitioner at will; the Substrate Saturation Counter (`params/threadwork.md:157-164`) throttles same-turn spam within one battle but doesn't touch the cross-scale cost-parity question.
· **Verdict: live exactly as long as ED-1010 stays open** — this is precisely the item the master workplan already earmarks for a post-resolution sweep (ED-SC-0001, `canon/editorial_ledger.jsonl:579`, "Company-scale thread-cost arbitrage rides ED-1010").

## Findings (C-TW-1..12)

| ID | Claim | Sev | Status | Evidence |
|---|---|---|---|---|
| C-TW-1 | Threadwork sim (`sim/thread/*`, thread-relevant `knots.py`, `compute_thread_echo`) is a complete island — zero callers anywhere on the `mc_v18` campaign-reachable path; no scene_type, no trigger, no test coverage | P1 | NEW | `sim/mc_v18.py:83`; `sim/cross_scale/scene_dispatch.py:37-52,78-107`; `sim/cross_scale/domain_echo.py:178`; `sim/tests/` listing |
| C-TW-2 | Mending Coherence-cost contradiction: canon/02 Amendment 3 (immutable tier) + §2.4 degree table + params/threadwork.md all say **0**; §3.2 says **-1**; sim implements **-1**, and **-2** on Partial/Failure — contradicting both readings | P1 | NEW | `canon/02_foundations_amendment_leap_mechanism.md:38`; `threadwork_v30.md:474-481,624`; `sim/thread/operations.py:185-186,321` |
| C-TW-3 | Blanket degree-penalty in `_resolve_operation` applies -1 Coherence to Leap Partial/Failure, contradicting both canon (no Coherence line in §2.3) and the function's own docstring | P2 | NEW | `sim/thread/operations.py:184-186,224,239-240`; `threadwork_v30.md:165-171` |
| C-TW-4 | POP per-op cap (TW-05: "-1 max regardless of scale") applied only at Object/Personal, leaving Relational+ uncapped — inverted relative to the ruling | P2 | NEW | `threadwork_v30.md:177`; `sim/thread/operations.py:280` |
| C-TW-5 | Sim's additive stacking (scale cost + degree penalty) at Relational+ produces uncapped Coherence totals exceeding RD-2's established "-1 total, non-FR" reading | P2 | KNOWN-TRACKED (rides ED-1010) | `canon/editorial_ledger.jsonl:396`; `sim/thread/operations.py:107-112,185-186` |
| C-TW-6 | Thread Fatigue (ED-694) — the entire per-operation/Focus rate-limiter — is 100% unimplemented | P1 | NEW | `threadwork_v30.md:185-196`; zero hits repo-wide in `sim/thread`, `sim/personal/knots.py` |
| C-TW-7 | Overweave / Seasonal Mending Fatigue Ob-stacking unimplemented (no window/season state tracked) | P2 | NEW | `threadwork_v30.md:306,448,483`; `sim/thread/operations.py` (absent) |
| C-TW-8 | Co-Movement — canon's "constitutive," fires-on-every-op mechanic — is never invoked by any `attempt_*` function even internally | P2 | NEW | `threadwork_v30.md:735-747`; `sim/thread/co_movement.py` (zero callers) |
| C-TW-9 | Community Organizing/Weaving and Thread-Read have zero sim implementation under any name | P2 | NEW | `params/threadwork.md:25-29`; `threadwork_v30.md:175-177`; zero hits in `sim/` |
| C-TW-10 | Leap eligibility check omits Approach Training tag and incapacitation gates, checking TS only | P2 | NEW | `threadwork_v30.md:146-150`; `sim/thread/operations.py:226-234` |
| C-TW-11 | Pull's 5D eligibility floor (R-57) and Dissolution's living-being Ob override (R-55) unimplemented | P3 | NEW | `threadwork_v25_historical.md:62-64`; `threadwork_v30.md:73-77`; `sim/thread/operations.py:256-262,302-308` |
| C-TW-12 | `sim/personal/knots.py` implements the PP-632 model superseded by ED-912 (resolved 2026-06-28) — 9 days stale against ratified canon, gates Coherence-adjacent Knot arithmetic | P2 | NEW | `canon/editorial_ledger.jsonl:399`; `params/threadwork.md:32-52`; `sim/personal/knots.py:59-71,254-259` |

## Honest gaps

- I did not exhaustively read `threadwork_v25_historical.md` (98KB, superseded-but-still-cross-cited for active patch notes like R-55/R-57) beyond targeted greps — there may be additional still-active patch-note callouts I didn't surface.
- I did not independently re-verify sim behavior by executing the code (no test harness exists for `sim/thread/`, and the read-only mandate + time budget argued against writing an ad hoc script); all sim-behavior claims are from static reading of the Python source, not runtime observation. A refuter pass should spot-check at least C-TW-2 and C-TW-5 by actually running `attempt_mending`/`attempt_weaving`.
- The exploit-arena Line 1 (Knot-anchoring dilution) is a paper-walk against text with no stated frequency cap — I could not confirm whether an implicit "once per season" convention exists elsewhere (e.g., an unwritten table convention, or a rule I didn't locate in `knots_v30.md`'s fuller body, which I read only via targeted grep, not cover-to-cover).
- I did not cross-check `references/module_contracts.yaml`'s `threadwork` module entry (`module_contracts.yaml:269-291`) in full depth against the op catalog — I pulled only the grep hits; a full contract-closure pass (the `valoria-module-adjudicator` skill's job) is out of scope here.
- I did not examine `designs/threadwork/threadwork_v25_historical_index.md`, `threadwork_philosophical_reference_v30(_infill).md`, or the `#4` DEFER item ("territory_temperaments coupling") beyond the single grep that surfaced it — flagged by prior audit as DEFER, not re-investigated here.
- C-TW-1's "first direct confirmation for threadwork" framing should be reconciled by the orchestrator against whatever C-REACH's general island matrix independently finds for the same modules, to avoid double-counting at synthesis time.
