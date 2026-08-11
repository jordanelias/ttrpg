# Personal-scale combat engine — independent re-derivation (reading-only, no grep)

Scope read whole/near-whole: wrapper.py, core.py, combat_systems.py, combatant.py, config.py,
tradition.py (facade only, 19 lines), systems/combat/sim/combat.py (deprecated), engine/cross_scale/
combat_bridge.py, systems/characters/sim/{__init__,conviction,beliefs,companion}.py.
workbench/ only `ls`'d (armour_participation.py, balance.py, build_levers.py, catalogue.py,
commentary.py, data/, narrate.py, presets.py, probabilities.py, server.py, static/, structure_scan.py,
trace.py) — not opened.
Did NOT open any `*_flow_skeleton_v1.md` file.

## 1. Control flow

### fight(A, B, cfg, rng, max_bouts=12) -> int
1. Re-init `A.wt`/`B.wt` (WoundTracker) — must pass spirit/strength or a re-fight silently reverts
   to WoundTracker defaults (documented at wrapper.py:469-471).
2. `_init_live(A,cfg)`, `_init_live(B,cfg)` — `derive_stats(cfg)` (conc_max), then reset
   stamina/conc/initiative/poise from the combatant's own held maxima. `derive_stats` result
   (conc_max) is consumed by the reset line immediately after it.
3. emit `fight_start`.
4. Loop `turn` in `range(max_bouts)` — each iteration is ONE `engagement`:
   a. `first` = A or B, 50/50 rng pick.
   b. `loser, prev_closed = engagement(A,B,first,cfg,rng,prev_closed)` — `prev_closed` from the
      PREVIOUS turn's return is an ARGUMENT to this turn's `engagement` call (threads the
      re-presentation gate, see below).
   c. if `loser is not None`: set `result=±1`, `break` the turn loop.
   d. else (no one felled — engagement ended by separation): both fighters partially recover
      stamina and concentration, loop to next turn.
5. **No automatic tiebreak** — if no turn ever fells anyone in `max_bouts`, `result` stays 0
   (documented, deliberate — "an undecided fight is a legitimate outcome").
6. UPSET_FLOOR: if `result!=0`, with probability `cfg['UPSET_FLOOR']` the decided loser steals the
   win (`result = -result`). This happens strictly AFTER the in-model resolution and is emitted as
   `fight_result` with no corresponding in-model event — the trace stream can show
   `engagement_end felled=X` then `fight_result winner=NOT-X`. Config's own comment flags this as a
   measurement caveat: every reported win-rate is compressed toward [UPSET_FLOOR, 1-UPSET_FLOOR].
7. return `result`.

### engagement(A, B, first, cfg, rng, prev_closed) -> (felled_or_None, closed)
Setup (once per engagement, before the beat loop):
1. `aggressor=first`; `defender`=the other object. A/B identity is NEVER reassigned — only the
   local `aggressor`/`defender` labels move (this is the file's own stated invariant, wrapper.py:1-3).
2. Reset `grip_position=0.0`, `lunge_depth=0.0` on BOTH — open-measure reset. This must happen
   BEFORE step 3 (reach_base reads grip_position).
3. `erA=reach_base(A,cfg)`, `erB=reach_base(B,cfg)` — these feed step 4.
4. `longer`/`shorter` from erA vs erB (coin-flip only on an exact tie).
5. `measure_gap = max(0, er[longer]-er[shorter])` — feeds step 6.
6. `closed` = probabilistic soft-latch on `measure_gap` vs `CLOSE_GAP_REF ± CLOSE_LATCH_BAND`
   (replaces an old hard cliff at gap<=0.3 — ED-PC-0037/F17).
7. RE-PRESENTATION GATE: only runs if `prev_closed AND not closed AND measure_gap>0.3` — i.e. this
   engagement's `prev_closed` argument (from the PRIOR engagement) gates whether step 6's `closed`
   can be overridden back to `True` (crowded-in). Calls `S.represent_measure_p(longer,shorter,cfg,
   TR,measure_gap=measure_gap)`; if the roll fails, `closed=True; measure_gap=0.0`.
8. `A.initiative=B.initiative=0.0` (pre-contact seizure cut; documented as verified inert).
9. `ready={c: rng.random()*ACT_THRESHOLD for c in (A,B)}` — arbitrary independent cadence PHASE per
   fighter (replaces old lockstep `{0,0}` — this is the documented fix for the "first-actor
   monopoly", ED-PC-0037/F16).
10. `beats=0; exchanges=0; soft=8; reopen_moment=False; push_avail=False`.
11. emit `engagement_start`.

Beat loop: `while beats < soft*3` (24 beats max), `beats+=1` first thing each iteration:
  a. Per-fighter fatigue `ffat` from current stamina.
  b. Initiative decay (`init_hold_decay`, tradition-held) applied FIRST, THEN disposition-lean
     drift applied to the DECAYED value (order matters: decay reads old initiative, drift reads
     the post-decay initiative).
  c. Poise regen + clamp for both.
  d. Per-fighter (loop over A,B): `grip_position`, `range_avail`, `facing` derived; `lunge_depth`
     reset to 0 (a lunge that fired last beat does not persist); `select_mode(...)` writes the six
     `sel_*` fields; `selected_arm_magnitudes` writes `sel_eff_cut/sel_eff_thrust` (reads the
     just-written `sel_head`); `er[c]` REFRESH #1 (grip-aware, pre-swap form) — feeds `rate` (next)
     and `reopen`/`disengage`/approach logic later this same beat.
  e. `rate` = `weapon_tempo` (open) or `close_tempo` (closed), using `ffat` from (a).
  f. `ready[c] += rate[c] * tempo_pressure(c, opp, cfg, TR)` — readiness accumulation, using `rate`
     from (e).
  g. IF `closed and beats>1 and reopen_moment` (set by a PRIOR beat's tail, see below): roll to
     re-open measure; on success, `closed=False`, `ready=_carry(ready,cfg)` (residual-preserving,
     not zeroing), `continue` — skips the rest of this beat entirely.
  h. `reopen_moment=push_avail=False` reset (consumed/expires unless re-created below this same
     beat).
  i. IF `closed and beats>1`: PROACTIVE DISENGAGE — attempt roll gated on
     `disengage_attempt_p * reach_threat`; if attempted: `disengage_clean_p` roll decides CLEAN
     break (`closed=False`, carry `ready`, `continue`) vs PURSUED (Nachreisen: `core.resolve` a
     pursuit strike against the withdrawer — possible `core.strike`+`apply_wound`+early felled
     `return`; pursuer's `ready` forced to `ACT_THRESHOLD`, seizing tempo, but no `continue` — falls
     through to the closed-exchange code below in the SAME beat).
  j. IF `not closed`: APPROACH sub-phase.
     - `reach_threat`, `approach_displace`, `base_gap` computed.
     - Stop-thrust: `stophit_p` computed from `reach_threat`+`displace`+gap; if rolled, resolves via
       `core.resolve` -> possible `core.strike`+`apply_wound`+early felled `return`; on a landed hit,
       `recoil = arrest_impulse(...)` is set (else stays 0.0) — `recoil` is an ARGUMENT to the next
       line.
     - `measure_gap = approach_step(measure_gap, base_gap, close_rate, recoil)` — net advance minus
       arrest.
     - `just_closed = measure_gap<=0.3`; if true, `closed=True`, `ready=_carry(ready,cfg)`.
     - emit `approach`.
     - **Only if STILL not closed** (i.e. `just_closed` was false): check stamina collapse (both
       <=-4) -> early `return None, closed`; else `continue` to the next beat, skipping the closed
       block entirely THIS beat.
     - **If `just_closed` fired this beat, execution does NOT `continue`** — it falls straight into
       the "CLOSED: tempo-gated exchange" block below, in the SAME beat, using the `ready` values
       just carried. Approach-closing and a closed exchange can therefore resolve in one beat.
  k. CLOSED EXCHANGE (reached only when `closed` is true, whether from a prior beat or just this
     beat via (j)):
     - `actors = [c for c in (A,B) if ready[c]>=ACT_THRESHOLD]`; if empty, `continue` (no action).
     - Pick `aggressor` = higher-ready actor (random tiebreak if both ready and tied); `defender`
       = the other. `_agg0`/`_def0` labels frozen here for later trace emits (roles may flip via
       riposte below).
     - Half-sword auto-switch: `aggressor.weapon`/`defender.weapon` reassigned via
       `halfsword_target`.
     - `select_mode` re-run for BOTH roles on the (possibly just-switched) weapon form, writing all
       six `sel_*` fields for both — feeds `sel_eff_cut/thrust` refresh, then `er` REFRESH #2
       (post-swap) for both roles.
     - `ready[aggressor] -= ACT_THRESHOLD` (consumes the action).
     - `commit_depth(...)` draws `commit` (Beta) — argument to almost everything downstream this
       beat: possible lunge (`commit>=LUNGE_COMMIT` and a `lunge_quality` roll sets
       `aggressor.lunge_depth`), `act_cost` (stamina spend), the extra tempo-debt subtraction from
       `ready[aggressor]`, `attack_sigma`, `mode_sigma` (via `read_contest`), overcommit exposure,
       the displace-and-step-inside precondition, and the reopen-moment precondition (b).
     - `oob` flag if `aggressor.stamina<=0`; `fat_a`/`fat_d` computed; `mental_fat_d` from `fat_d`.
     - `reach_pen`, `init` (emphasis), `consistency_a` computed — all pure functions of already-
       derived state, all become ARGUMENTS to the sigma assembly below.
     - `read_contest(...)` -> `read_win, read_d, read_a, mode, msig` — `mode` (the chosen defence)
       is an ARGUMENT to `defence_sigma` next.
     - `dsig = defence_sigma(defender, msig[mode], ...)`, `atk_sig = attack_sigma(...)`,
       `adef = armor_defeat_sigma(...)`, `init_edge = initiative_sigma(...)` — all five (dsig,
       atk_sig, reach_pen, adef, init_edge) are ARGUMENTS to `assemble_net_sigma`.
     - IF `read_win and commit>=4`: Indes steal computed and applied to BOTH fighters' initiative
       (mutates state read by nothing else this beat — but persists to next beat); `counter_attempt`
       decided.
     - `pool = resolution_pool(aggressor.history)`; `deg, net = core.resolve(pool, net_sigma, rng)`
       — `net_sigma` (from `assemble_net_sigma`) is the argument. emit `roll`.
     - `overcommit_exposure` computed from `commit`, `fat_a`; if >0, degrades `aggressor.initiative`
       and `aggressor.poise` (feeds the RIPOSTE_ON_FAIL/NEUTRALIZE probabilities below).
     - Outcome mapping keyed on `deg` (fail/partial/success/overwhelming) x `mode`: sets
       `hit`/`riposte`/`bind`. `neutralize` fixed per-mode, computed once before the branch.
     - IF `counter_attempt`: success (`counter_success_prob` roll) voids the attack
       (`hit=0,bind=False,riposte=True`); failure re-applies the seized Vor back to the aggressor
       and resolves the attack UNDEFENDED (`core.strike` at success/overwhelming degree).
     - `sim = hit>0 and riposte` (simultaneous-hit flag) — argument to the riposte block later.
     - CONTACT AXIS precondition site 1 (displace-and-step-inside): only if aggressor's selected
       head is POINT, `commit>=4`, no hit landed, `read_win`, and (`beat_aside` OR `slip_inside`);
       on a further roll, may force `closed=True` (if not already), may apply a graze
       (`core.strike`+`apply_wound`, possible felled `return`), and sets `riposte=True`.
     - Reopen-moment precondition sites 2a/2b/2c (three independent checks: shorter over-committed;
       longer-as-defender won a defensive exchange; longer 2H frees a hand) — each sets
       `reopen_moment=True` (consumed at the TOP of the NEXT beat, step (g)) and
       `opening_created=True` (consumed later THIS beat, at the contact-axis site below).
     - IF `hit>0`: `apply_wound`, conc drain, initiative shift (aggressor up, defender down), poise
       break scaled by hit size, `percussion_stagger` applied (stamina+poise), possible felled
       `return`.
     - IF `bind`: `opening_created=True`; ONE bind-entry Vor steal (`bind_sigma` sign decides who);
       poise break to the bind loser; THEN an INNER loop `for _ in range(3): beats+=1` (mutates the
       OUTER `beats` counter, so a bind can consume up to 3 extra "beats" of the 24-beat budget in
       one exchange) resolving bind-dominance rolls; a dominance win may land a hit
       (`BIND_HIT_P` roll, possible felled `return`); a dominance loss sets `riposte=True` and
       breaks the inner loop.
     - IF `riposte`: if `sim` (simultaneous), a `disrupt_resist_p` roll may still let the ORIGINAL
       aggressor eat a graze (possible felled `return`) despite the riposte; defender conc drains;
       THEN **role flip**: `aggressor, defender = defender, aggressor` (a local Python tuple swap of
       the two role variables — A/B object identity is untouched, only which one is called
       "aggressor" for any code AFTER this line, e.g. the contact-axis grab below).
     - CONTACT AXIS resolution (single insertion point, AFTER hit/bind/riposte all resolve): if
       `CT.grab_available(aggressor, defender, opening_created, cfg)` (using the flag accumulated
       above, and the POST-riposte-flip aggressor/defender), resolves one grab outcome
       (`disarm`/`throw`/`pin`/`foot_pin`/`control`/`escape`) with poise/initiative side effects
       only (no wound/stamina channel) — `escape` is an explicit no-op.
     - emit `outcome`; `exchanges+=1`.
     - TERMINATION CHECKS (in order): stamina collapse (either <=-4) -> `return None, closed`;
       `exchanges >= BURST_MAX` -> `return None, closed`; NOT(`hit>0 or riposte or bind`) — i.e. a
       clean, undefended-but-unlanded, unbound exchange -> `return None, closed` ("clean defence"
       separation). Otherwise the beat loop continues.
12. If the `while` loop exhausts 24 beats without any of the above returns: emit
    `beat_exhaustion`, `return None, closed`.

Every return path returns `(felled_combatant_or_None, closed)` — `closed` always threads forward as
next turn's `prev_closed` argument to `fight`'s loop, which passes it to the next `engagement` call
(step 7 above).

## 2. Does the combat engine touch the Key substrate?

**No — established by reading, not searching.** `core.py`'s only reach into `engine/` is
`from engine.autoload import sigma_leverage as SL` (core.py:19). I opened
`engine/autoload/sigma_leverage.py` and read its own header, which states its dependency
contract explicitly: "Dependencies: stdlib only (math, random) + engine.autoload.dice_engine."
— no `engine.substrate` import anywhere in that chain. `wrapper.py`, `combat_systems.py`,
`combatant.py`, `config.py`, `tradition.py` import nothing from `engine/` at all — only each
other, `weapons`/`weapon_physics`/`geometry`/`vocabulary`/`contact`/`traditions`/
`ability_primitives` (siblings in the same non-package directory). `engine/cross_scale/
combat_bridge.py` (the IN-side seam into the campaign loop) imports only `combatant` and
`wrapper` from `combat_engine_v1/` — again no `engine.substrate` reference. `systems/combat/
sim/combat.py` (the deprecated engine) imports only `engine.autoload.dice_engine.roll_pool` —
same autoload layer, not substrate. `engine/substrate/` (which holds `keys.py`, the Key
registry, plus `canon_buckets.py` and `stubwire.py`) is never imported by anything in the
combat scope I read.

One adjacent (non-combat) data point: `systems/characters/sim/companion.py` DOES import
`from engine.substrate import stubwire` — but `stubwire.py` is a typed-no-op marker utility
(`StubResult`/`stub_resolve`), not the Key registry (`keys.py`) itself; and `companion.py`'s
sole entry point is entirely unimplemented (see §4), so even this contact never reaches live
Key-registry code.

## 3. systems/characters/sim/ — entry points and callers

- `conviction.py`: `apply_conviction_scar(actor, source, magnitude, conviction=None, certainty=3,
  season=0, world=None) -> ScarRecord`; `check_conviction_threshold(actor, world=None) ->
  ConvictionThresholdState`; `mark_belief_revision_pending(actor, belief_id, world=None)`;
  `get_state`, `reset_all`. Within my read scope, the only caller of `mark_belief_revision_pending`
  is `beliefs.py` (two call sites, both via a late `from systems.characters.sim.conviction import
  mark_belief_revision_pending` to break the documented import cycle). Nothing in the combat-scope
  files (wrapper/core/combat_systems/combatant/config/tradition/sim.combat/combat_bridge) calls
  anything in `conviction.py`.
- `beliefs.py`: `add_belief`, `revise_belief(actor, belief_id, new_position, evidence=None,
  world=None) -> RevisionResult`, `social_success(actor, belief_id, aligned, current_momentum=0,
  world=None) -> RevisionResult`, `get_active_beliefs`, `reset_all`. No caller of any of these
  appears in the combat-scope files I read; `beliefs.py` itself is only a caller (into
  `conviction.py`), never a callee, within this reading pass.
- `companion.py`: single entry point `run_companion_scene(scene)`. It has exactly one statement:
  return a `stubwire.stub_resolve(...)` typed no-op. No caller appears anywhere in the scope read.
- None of the three modules is imported or called anywhere in `wrapper.py`, `core.py`,
  `combat_systems.py`, `combatant.py`, `config.py`, `tradition.py`, `systems/combat/sim/combat.py`,
  or `engine/cross_scale/combat_bridge.py` — personal combat and the characters/sim oracle appear,
  from this reading pass, to be structurally disjoint at the scope I was given.

## 4. Declared-but-doesn't-happen inventory (file:line)

1. `systems/characters/sim/companion.py:28-33` — `run_companion_scene`, the module's ONLY declared
   entry point, is a hard stub: it always returns `stubwire.stub_resolve(...)`, never runs the
   "CompanionScene" logic its own docstring/canon-source pointer describes. Declared entry point,
   zero real behavior.
2. `systems/characters/sim/beliefs.py:46` — `BELIEF_MOMENTUM_PER_CONTEST_CAP = 1` is declared with
   a `[canonical: social_contest_v30 §9.5 ...]` citation but is never read anywhere else in the
   file (only `MOMENTUM_CAP` is consulted in `social_success`); the per-contest cap it names is
   not enforced by any code I read.
3. `systems/characters/sim/conviction.py:42-49` — the module docstring/comment says "Canonical
   13-Conviction set per PP-684 ... legacy 9-Conviction ... superseded by taxonomy_v30" and then
   the `CONVICTIONS` tuple that follows lists exactly 9 names, not 13 — a comment describing a
   13-item canonical set immediately above a 9-item tuple.
4. `engine/cross_scale/combat_bridge.py:36-40` — the bridge's own docstring states, as of its
   authoring, "no live loop yet queues a `combat` scene_type (verified: no `queue_scene("combat",
   ...)` call site exists anywhere in the tree at this wave)" — the IN-side seam is fully built
   (`derive_parties`/`resolve`) but self-documented as unreached by the campaign loop at time of
   writing; I did not verify this claim independently (scene_dispatch.py was out of my given
   scope), so I report it as the module's own stated fact rather than something I re-derived.
5. `systems/combat/combat_engine_v1/config.py` carries several REMOVED/retired constants
   documented at their own former call sites as dead when they were live — evidence of the
   pattern this engine actively guards against, not a current defect: `REACH_ADV_K`/
   `RESIDUAL_REACH_FRAC` (comment: "set but read nowhere ... also being exported into the
   Godot-facing engine_params JSON as if live" — config.py:6); `CHOKE_BIND_K` (comment: "its only
   reader ... multiplied it by a `choke` argument its ONLY caller hardcoded to 0.0, so the term
   was a structural zero" — config.py:126); `ATTACKER_BIAS` (config.py:1092, in combat_systems.py
   — "untagged, unledgered fiat that DUPLICATED the initiative/Vor system"); `CHOKE_GRIP_MIN`
   ("zero readers anywhere ... yet the AUTO-collecting exporter kept shipping it into the
   Godot-facing typed contract" — config.py:169-173); `EXPOSE_MOMENT_REF`/`EXPOSE_CHOKE_K`
   ("set but read nowhere" — config.py:140). All are gone from the live file now; noted because
   the task asks specifically for the FACT of unused declarations, and the file's own comments
   are the clearest first-person record of that class of bug recurring (three separate ED-PC-
   tickets caught the same defect shape).
6. `systems/combat/combat_engine_v1/combat_systems.py:1330-1339` — `tempo_pressure`'s own
   docstring is a self-flagged "HONESTY CORRECTION": an adversarial ablation found the function's
   aggregate outcome effect to be statistically indistinguishable from zero at default builds
   (z=-0.23), and further states the READ half of the function is IDENTICALLY ZERO in any
   same-stats fight (because `reading()` and `eff_cw` depend only on stats/tradition). The
   function is live code, called every beat, and is not a stub — but the code's own comment
   states it does not currently do the thing its surrounding narrative claims (fixing the
   first-actor monopoly); that fix is credited elsewhere (the arbitrary cadence-phase draw at
   engagement start, wrapper.py:110).
7. `systems/combat/combat_engine_v1/core.py:97-107` — `QUAL['partial']=0.5` is declared in a dict
   whose own comment says a caller previously believed it dead; the comment now clarifies it is
   NOT dead in the sense of unreachable, but `damage()` never routes a `'partial'` degree into a
   damage call at all (the wrapper maps `partial` to graze/bind, never `core.strike`), so the
   `QUAL['partial']` entry is read by nothing in the resolution path — the comment explicitly
   distinguishes this from a KeyError-generating removal and defends keeping it as documentation
   of the degree-domain rather than as live-read data.

## 5. What surprised me

- The single most consequential piece of control flow — "who acts first" — was, by the engine's
  own extensive in-line history (wrapper.py:99-109, config.py:100-104, combat_systems.py:1310-
  1339), rebuilt from a raw deterministic metronome (fastest weapon always acts first, every beat,
  every fight) to a system of THREE overlapping partial fixes (arbitrary cadence-phase draw,
  `tempo_pressure` anticipation, `INIT_TEMPO_K`/`READ_TEMPO_K` softening) — and the engine's own
  code comments state that of the three, only the FIRST (the arbitrary phase draw) is doing real
  work at default stat builds; the other two are honestly documented as present-but-inert pending
  stat divergence. That kind of self-auditing "this mechanism doesn't do what it says" comment,
  left in the shipped resolver rather than deleted or hidden, was not what I expected walking in.
- A beat in the approach phase can transition straight into a full closed-exchange resolution
  (attack roll, damage, riposte, bind, contact) in the SAME beat once `measure_gap` crosses 0.3 —
  there is no "closing" beat that only moves distance; closing and fighting can be one event.
- The bind's inner `for _ in range(3): beats+=1` mutates the SAME `beats` counter the outer 24-beat
  engagement budget is checked against, so a single bind exchange can consume up to 3 of the
  engagement's 24 beats in one pass through the outer loop body — the beat counter is not a clean
  1:1 with "one pass of the while loop."
- `characters/sim/` (conviction/beliefs/companion) and the personal combat engine are, at the
  scope I read, completely disconnected — no import or call in either direction. Wound state lives
  entirely in `combatant.WoundTracker`; nothing in `characters/sim/` touches it, and nothing in
  combat touches Convictions/Beliefs.
