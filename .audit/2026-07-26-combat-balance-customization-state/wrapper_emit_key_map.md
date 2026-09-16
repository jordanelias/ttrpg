# `wrapper.py` `_emit()` → Key map, and the §12 wrapper blind-spot audit

## Status: PROPOSED — read-only audit + mapping table (ED-PC-0044)

| field | value |
|---|---|
| **ID** | **ED-PC-0044** (reserved-block draw; the ledger entry is filed by the orchestrating session, not here) |
| **Batch** | I4 of the PC-lane execution plan (`combat_execution_plan.md` §15 I4, promoted from conditional 2026-07-29), executing §12 |
| **Date** | 2026-07-29 |
| **Lane** | PC (personal combat) |
| **Kind** | READ-ONLY audit. **No code was changed. No fix was applied.** This document is the only file created. |
| **Subject** | `systems/combat/combat_engine_v1/wrapper.py` (496 lines) + `systems/combat/combat_engine_v1/state_graph.py` (232 lines) |
| **Registry read (never written)** | `systems/_architecture/key_type_registry_v30.md` §7 — IN-owned. Per §15 I4 (F16), **this table is consumed by IN's Wave 3; nothing here edits the registry.** |
| **Consumes** | `combat_execution_plan.md` §12, §15 I2/I3/I4 |

**Two parts.** §1 is the deliverable IN Wave 3 consumes: every `_emit()` kind classified against the four
canonical `scene.combat_*` types, no "misc" bucket, plus the mapping *impossibilities* — which are findings
for IN, not things this session resolved. §2 is the §12 audit: mutation ordering, RNG-draw sequencing,
burst/latch state machine. **Findings are reported, not fixed** — every one is a behaviour change that needs
its own guard and disclosure per §0.1 point 5.

---

## §0 MEASURED-BY register

Per CLAUDE.md §0.1 point 3 and the I4 brief: **every quantitative claim below names the method that produced
it.** Claims are tagged `[M1]`…`[M8]`. All methods are in-process instrumentation of the live engine on this
branch (`claude/combat-balance-strategy-sdmt43`); none mutated a file, none was run under `pytest`. Where a
claim is *not* measured it is labelled **[UNQUANTIFIED]** and says so.

| tag | method | corpus |
|---|---|---|
| **M1** | **AST walk**, not grep: `ast.parse(wrapper.py)`, collect `ast.Call` where `func.id == '_emit'`, read `args[0]` (`ast.Constant`) as the kind and `[kw.arg for kw in keywords]` as the payload field list. | static |
| **M2** | Traced fights via `workbench/trace.run_traced_fight`; match `engagement_start.weapon_A/weapon_B` against `weapons.HALFSWORD_FORM.values()`; bucket by the preceding `turn_start.turn`. | (a) `{longsword, greatsword, arming, poleaxe}` vs `poleaxe`, both `heavy`, seeds 0–59 → 1 949 `engagement_start` events. (b) `longsword` vs `poleaxe`, both `heavy`, seeds 0–119. |
| **M3** | `combat_systems.reach_base(Combatant(weapon=X), CFG)` for each `HALFSWORD_BASE`/`HALFSWORD_FORM` pair, default build. | static, 2 pairs |
| **M4** | `random.Random` **subclass counting `random`/`randrange`/`betavariate`/`gauss`**, counter read inside the `_TRACE` callback so each emit records the cumulative draw index. | 6 matchups, seed 0, `max_bouts=1`, default `light` armour |
| **M5** | Monkeypatched `core.strike` recording `sys._getframe(1).f_lineno` (the *wrapper* call site), then attributed against the five sites whose result reaches `outcome.hit`. | 5 matchups × seeds 0–39, both `light` → 200 fights, 627 `core.strike` calls |
| **M6** | For every `engagement_end` event with `felled` non-null, record `kind` of the immediately preceding event. | same corpus as M5 |
| **M7** | `sys.settrace` line counter filtered to `wrapper.__file__` — counts **line evaluations**, so a one-line `if X: body` counts the *test*, not the branch taken (called out where it matters). | 8 matchups × armour {none, light, heavy} × seeds 0–14 = **360 fights** |
| **M8** | Compare `fight_result.winner` against the last `engagement_end.felled` label in the same fight. | 4 matchups × seeds 0–499 = 2 000 fights, 1 993 decided |

**Count reconciliation (M1).** The I4 brief says *22 `_emit(` call sites*. `grep -c '_emit('` does return **22**,
but two of those hits are not call sites: `wrapper.py:10` (a prose mention inside the TRACE SEAM comment) and
`wrapper.py:17` (the `def _emit` definition). The AST count is **20 call sites across 15 distinct kinds**.
The 15-kind figure is what §1's table is built on. *(Also noted because the brief's "~15–25 emit kinds"
estimate is now exact: 15.)*

---

# §1 — the `_emit()` → Key mapping table

## §1.1 What `state_graph.py` is (asked explicitly)

`state_graph.py` has **zero `_emit(` sites [M1]**. It is neither a producer nor, in the engine sense, a
consumer. It is three things:

1. **A declarative mirror of the control flow** (`STATES`, `state_graph.py:37–62`) with a hand-maintained
   `emits` list per node and a `site` string pointing back at `wrapper.py`.
2. **A hand-maintained duplicate of the emit vocabulary** — `TRACE_KINDS` (`state_graph.py:20–23`), a literal
   set of **14** kinds. `wrapper.py` never reads it. **The wrapper is the sole owner of the vocabulary; this
   set is a copy with no guard binding it to the owner** — see **F-4**, where that copy is already wrong.
3. **The only in-repo trace consumer outside `workbench/`** — `fired_states_from_events()`
   (`state_graph.py:133–157`) and `separation_reasons_from_events()` (`:160`), used by its own `__main__`
   coverage sweep and by `tests/valoria/test_combat_state_graph.py`.

The other consumers are all workbench-side and switch on `ev['kind']`: `workbench/narrate.py:39`,
`workbench/commentary.py:56`, `workbench/probabilities.py:108`, `workbench/server.py:59`
*(fourth consumer added by the adversarial pass)*.

So for I4's purposes: **`state_graph.py` does not define the vocabulary; it restates it, and the restatement
is unguarded.** Any Key-mapping layer must bind to `wrapper.py`, not to `TRACE_KINDS`.

## §1.2 The four canonical types (read-only, from the IN-owned registry)

`systems/_architecture/key_type_registry_v30.md` §7 declares exactly four `scene.combat_*` types:

| `type_id` | registry line | required payload | optional payload |
|---|---|---|---|
| `scene.combat_resolved` | `:727` | `scene_id`, `outcome`, `participants` | `casualties`, `wounds_inflicted` |
| `scene.combat_strike` | `:746` | `attacker`, `defender` | `commit`, `weapon` |
| `scene.combat_hit` | `:764` | *(none — `required_payload_fields: []`)* | `degree`, `damage`, `net` |
| `scene.combat_felled` | `:781` | `actor_id` | `by_actor` |

**All four carry a `[STUB: … provisional per J-2 register-all; pending Jordan ratification]` marker**
(registry `:744`, `:762`, `:779`, `:795`). Every mapping below is therefore a mapping against a *provisional*
target — recorded here so IN does not read this table as validating the types.

## §1.3 The map — 15 kinds, all classified

Payload field lists are verbatim from **[M1]**. `type_id` values are the registry's exact identifiers.

| # | emit kind | call sites (`function:line`) | payload fields | maps to `type_id` / **internal-only** | notes a consumer must know |
|---|---|---|---|---|---|
| 1 | `fight_start` | `fight:473` | `A`, `B`, `weapon_A`, `weapon_B`, `armor_A`, `armor_B`, `tradition_A`, `tradition_B` | **internal-only** — the registry has no combat-*started* type; the dramatis personae it carries are `scene.combat_resolved.participants`, published at close. | Only emit carrying **armour and tradition** — a port that needs them at resolution must cache from here. `weapon_A/B` are the *opening* forms and **go stale on the half-sword swap** (F-1). |
| 2 | `turn_start` | `fight:479` | `turn`, `first` | **internal-only** — bout pacing, one level below scene granularity. | `first` is a **fresh coin-flip each turn** (`:478`). It is **not** `scene.combat_resolved`'s "attacker" (see G-3). |
| 3 | `engagement_start` | `engagement:114` | `aggressor`, `defender`, `longer`, `shorter`, `weapon_A`, `weapon_B`, `reach_A`, `reach_B`, `measure_gap`, `closed` | **internal-only** — measure/geometry latch; no registry type covers measure state. | Best *available* source for `scene.combat_strike.weapon`, but stale-prone (F-1, G-5). `aggressor`/`defender` here are the turn's initiator/responder, **not** the per-beat exchange roles. `closed` is the latched engagement measure-state. |
| 4 | `approach` | `engagement:226` | `beat`, `shorter`, `longer`, `gap`, `close_rate`, `just_closed`, `stophit_p` | **internal-only** — per-beat measure telemetry. | `gap` is **post-step** (after `approach_step`, `:222`). `stophit_p` is a *probability*, not an outcome — do not read it as an event. |
| 5 | `stophit` | `engagement:213` | `longer`, `shorter`, `gap`, `pool`, `net_sigma`, `net`, `degree` | **`scene.combat_strike` + `scene.combat_hit`** — one emit, **two** Key types (composite; see G-7). | Fires **before** the strike and wound (`:216–221`), so **`damage` is not in the payload** — `degree`/`net` are, `damage` is not. **83 of 199 fellings [M6] happen on this path with no damage-bearing emit at all** (F-2). |
| 6 | `disengage` | `engagement:178`, `engagement:183` | `:178` → `longer`, `shorter`, `ok`, `gap`  ·  `:183` → `longer`, `shorter`, `ok`, `pursued`, `degree` | `ok=True` row: **internal-only** (a clean measure break; no registry type for measure). `ok=False`/`pursued` row: **`scene.combat_strike`** whose resolution has **no** `scene.combat_hit` producer. | **This kind is absent from `state_graph.TRACE_KINDS` (F-4)** and no state-graph node declares it. **Two payload shapes under one kind** — branch on `ok`. The pursuit strike (`:185`) can **fell** (`:187`); 2 of 199 fellings [M6]. |
| 7 | `commit` | `engagement:257` | `aggressor`, `defender`, `commit`, `beta_a`, `beta_b`, `stance_lean` | **`scene.combat_strike`** — the declared action entering resolution. Covers required `attacker`/`defender` and optional `commit`. | **`weapon` is absent** and cannot be filled from a stable source (G-5). `beta_a`/`beta_b`/`stance_lean` are the commit distribution's shape parameters — workbench-only (`probabilities.py`), no Key home; drop them at the boundary. |
| 8 | `read` | `engagement:284` | `defender`, `read_d`, `read_a`, `p_read_win`, `read_win` | **internal-only** — the pre-resolution anticipation contest; its payload is sigma-assembly internals the Key layer deliberately does not carry. | Fires **before** `roll`; `p_read_win` is the local probability, `read_win` the realised draw. Only the aggressor's *counterpart* is named (`defender`), so the pairing must be recovered from the enclosing `commit`. |
| 9 | `mode` | `engagement:286` | `defender`, `mode`, `msig`, `chosen_by` | **internal-only** — defence-mode selection, same reasoning as `read`. | `msig` is a dict of per-mode sigmas. `chosen_by` is `'read'` or `'random'` — the *random* case is `combat_systems.read_contest`'s `randrange(3)` over the **ordered** `V.DEFENCE_MODES`, which is part of the RNG contract. |
| 10 | `roll` | `engagement:306` | `aggressor`, `pool`, `net_sigma`, `net`, `degree`, `mode` | **`scene.combat_hit` (partial)** — supplies optional `degree` and `net`; supplies **no `damage`**. | The **only** damage-degree emit that fires on the fatal exchange path — **114 of 199 fellings [M6]**. Its `degree` may be *contradicted* by the following `outcome` (neutralize/counter can zero the hit for the same roll). A port publishing `combat_hit` here must reconcile with row 11 or it double-counts. |
| 11 | `outcome` | `engagement:449` | `aggressor`, `defender`, `mode`, `degree`, `hit`, `bind`, `riposte`, `A_wounds`, `B_wounds`, `A_felled`, `B_felled` | **`scene.combat_hit`** when `hit > 0` — the **only** emit carrying `damage`. | **Never fires on a felling beat** (F-2): six early returns bypass it. **Under-reports**: bind hits (`:409`), displace pull-back grazes (`:368`) and the (dead) riposte graze (`:420`) apply wounds without updating `hit`. `A_wounds`/`B_wounds` are running totals, so the delta is *visible* but unattributed. `aggressor`/`defender` are the **frozen pre-riposte** labels (`_agg0`/`_def0`, `:239`) while mutations at `:384–448` may have applied to the **flipped** roles. |
| 12 | `contact` | `engagement:436` | `aggressor`, `defender`, `actor`, `opponent`, `outcome`, `gsig` | **NO CANONICAL TYPE — mapping impossible.** See **G-1**. Not a strike (the grapple has no wound/stamina channel — `wrapper.py:438–439`), so `scene.combat_hit` is wrong; not a scene resolution, so `scene.combat_resolved` is wrong. | **The largest unmapped channel**: the grab gate was reached 2 452 times and fired **1 069 times (43.6%) [M7]**. Outcomes are `disarm`/`throw`/`pin`/`foot_pin`/`control`/`escape`. Emits **before** its own mutations (`:440–448`, F-9). Carries both frozen (`aggressor`/`defender`) and post-flip (`actor`/`opponent`) identities — the only emit that does. |
| 13 | `separation` | `engagement:229`, `:460`, `:461`, `:462`, `:463` | `reason` | **internal-only**, with a caveat: `reason` is the *only* producer of a `withdrawal`-shaped signal for `scene.combat_resolved.outcome`, but it is **engagement-scoped** while the type is **fight-scoped** — it cannot be lifted directly (G-2). | Reasons: `collapse` (`:229`, `:460`), `burst_ceiling` (`:461`), `clean_defence` (`:462`), `beat_exhaustion` (`:463`). Per ED-PC-0042 (`state_graph.py:29–35`) `collapse`/`beat_exhaustion` **are** reachable; a narrow sweep flags them as dead — do not re-litigate. A `clean_defence` separation can fire in the same beat as an effective grapple (F-8). |
| 14 | `engagement_end` | `fight:481` | `turn`, `felled` | **`scene.combat_felled`** when `felled` is not `None` — supplies the required `actor_id`. | **`by_actor` is not in the payload** and is only inferable as "the other combatant" under a strict 1v1 assumption (G-6). Fires for **every** engagement, felling or not — the Key is conditional on the field, not on the kind. |
| 15 | `fight_result` | `fight:495` | `result`, `winner` | **`scene.combat_resolved`** — supplies `outcome` after a lossy `+1/0/−1` → token mapping, and nothing else. | No `scene_id`, no `participants`, no `casualties`; `wounds_inflicted` is **unreconstructable** from the trace because of F-2. **Can contradict `engagement_end(felled=X)`: 94 of 1 993 decided fights (4.72%) name the felled combatant as the winner [M8]** — F-5. |

**Coverage check.** 15 kinds, 15 rows, no residual bucket. Kind-level split — **7 mapped**
(`stophit`, `disengage` (its `pursued` row; the `ok=True` row is internal), `commit`, `roll`,
`outcome`, `engagement_end`, `fight_result`) · **7 internal-only** (`fight_start`, `turn_start`,
`engagement_start`, `approach`, `read`, `mode`, `separation`) · **1 unmappable** (`contact`).
*(Tally corrected 2026-07-29 by the adversarial pass — the original line said 6 mapped / 8 internal,
double-counting `disengage` on the internal side and mislabelling its own seven-item list.)*

## §1.4 Mapping impossibilities — findings **for IN**, not resolved here

Per the brief: a mapping impossibility is a finding for the registry owner. Eight, in descending order of
how much they block Wave 3.

| # | gap | evidence |
|---|---|---|
| **G-1** | **No type for the contact/grapple axis.** `disarm`, `throw`, `pin`, `foot_pin`, `control` are structurally significant, player-visible outcomes with real mutations (poise, initiative) and no `scene.combat_*` home. IN must either register a fifth type or rule the axis explicitly non-Key (internal telemetry). | `wrapper.py:433–448`; fired 1 069 / 2 452 (43.6%) [M7] |
| **G-2** | **Scale mismatch.** The registry types are **scene**-scoped; the wrapper's structure is fight → turn/engagement → beat → exchange (→ bind sub-loop). `scene.combat_resolved` maps to `fight_result` **only if one fight == one scene** — a ruling nobody has made. Nothing in the trace carries `scene_id`; the port must inject it from outside the engine. | `wrapper.py:477` (`for turn in range(max_bouts)`), registry `:731` |
| **G-3** | **`scene.combat_resolved.outcome` vocabulary is unproducible.** Tokens are `attacker_win \| defender_win \| draw \| rout \| withdrawal`. The wrapper has **no stable "attacker"** — the exchange aggressor flips on riposte (`:426`) and `first` is re-coin-flipped every turn (`:478`) — and **no producer at all** for `rout` or `withdrawal`. Only `draw` and "A won / B won" are producible. | `wrapper.py:426`, `:478`, `:483`; registry `:733` |
| **G-4** | **`scene.combat_hit` cannot validate anything**: `required_payload_fields: []`. Any emit trivially satisfies it. Separately, its `damage` field is **unproducible for 100% of fatal blows** (F-2) and for the bind / pull-back / riposte-graze sites (F-2, M5). | registry `:768`; [M5], [M6] |
| **G-5** | **`scene.combat_strike.weapon` has no stable source.** The weapon **mutates mid-fight** (half-sword auto-switch, `:241–242`) and **no per-strike emit carries it**. The nearest sources (`fight_start`, `engagement_start`) are both stale by construction — and F-1 makes `engagement_start`'s value wrong on **100% of turns ≥ 2** in the measured matchup. | `wrapper.py:241–242`; [M2] |
| **G-6** | **`scene.combat_felled.by_actor` is in no emit.** Derivable as "the other one" in 1v1 only; breaks for any future multi-party fight. | `wrapper.py:481`; registry `:788` |
| **G-7** | **The trace vocabulary is not 1:1 with the Key vocabulary in either direction.** One emit → two types (`stophit`). Two payload shapes → one kind (`disengage`). Two kinds → one type (`roll` + `outcome` → `scene.combat_hit`, with the second able to contradict the first). A naive kind→type dictionary is not sufficient; the port needs a per-kind adapter. | rows 5, 6, 10, 11 |
| **G-8** | **All four target types are provisional STUBs pending Jordan.** This table maps onto an unratified surface; if the payloads change, every row's field column changes with them. | registry `:744`, `:762`, `:779`, `:795` |

---

# §2 — the §12 blind-spot audit (read-only, nothing fixed)

Thirteen findings, severity-ordered. Every one carries `file:line`, the concrete failure scenario, and
whether any existing test could see it. **None was fixed** — each is a behaviour change requiring its own
guard and disclosure (§0.1 point 5).

---

### F-1 — HIGH — the half-sword form carries across the engagement boundary (class ED-PC-0033/0034, still open)

**Where.** `wrapper.py:59–60` (the OPEN-MEASURE RESET), `:61`, `:66–67` (frozen geometry), `:241–242` (the
only writer of `.weapon`).

**Scenario.** ED-PC-0033 added an engagement-start reset because per-beat transient geometry carried on the
`Combatant` object and corrupted the new engagement's opening geometry. The reset covers exactly two fields:

```python
for c in (A, B):
    c.grip_position = 0.0; c.lunge_depth = 0.0
```

It does **not** cover `c.weapon`. `halfsword_target` (`combat_systems.py:773`) is called **only** inside the
closed exchange (`:241–242`), so a fighter who ends an engagement in the half-sword form **stays in it** —
and the next engagement's `reach_base` (`:61`), `longer`/`shorter` labels (`:66`) and `measure_gap` (`:67`)
are all computed on the shortened form and then **frozen for the whole engagement**. `.weapon` is not reset
by `_init_live` either, so it persists for the remainder of the fight. `Combatant.w` is a property
(`combatant.py:138`) reading `WEAPONS[self.weapon]`, so the entire weapon vector shifts, not just reach.

This is verbatim the failure ED-PC-0033's own comment describes for `grip_position`: *"would UNDER-READ its
own reach at THIS engagement's opening `reach_base` — corrupting the frozen longer/shorter labels and
measure_gap for the whole new engagement."*

**Magnitude [M2], [M3].**

- Across `{longsword, greatsword, arming, poleaxe}` vs `poleaxe`, both `heavy`, seeds 0–59: **272 of 1 949
  `engagement_start` events (14.0%) open with at least one fighter already in a half-sword form.**
- `longsword` vs `poleaxe`, both `heavy`, seeds 0–119, by turn:

  | turn | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|
  | opens at half-sword | **0/120** | **118/118** | 110/110 | 95/95 | 71/71 | 47/47 | 30/30 | 19/19 | 14/14 | 11/11 | 7/7 | 4/4 |

  **Turn 1: 0%. Every turn thereafter: 100%.**
- Reach delta: `longsword` 5.994 → `longsword_halfsword` 5.549 (**−0.445**); `estoc` 6.857 →
  `estoc_halfsword` 5.936 (**−0.921**).

**Why that magnitude matters.** `CLOSE_GAP_REF = 0.3`, `CLOSE_LATCH_BAND = 0.3` (`config.py:109`), so the
probabilistic closed-latch band is `measure_gap ∈ [0.0, 0.6]`. A **−0.445** reach shift moves a matchup
*through the entire band*. This is not a rounding error — it is the same order as the parameter the ED-PC-0037
F17 soft-latch was introduced to de-cliff, and it applies to a fixed, predictable subset of the roster
(half-sword-capable weapons vs rigid armour) — i.e. exactly the armour-participation surface the E-batches are
measuring. It also reproduces ED-PC-0034's signature exactly: **engagement 1 differs systematically from
engagements 2+**.

**Could an existing test see it?** **No.** `test_combat_halfsword_affordance.py` tests the *affordance*
predicate, not its lifetime. `test_combat_state_graph.py` maps kinds to nodes and is indifferent to payload
values. The engine's own `state_graph.py` `__main__` sweep checks state coverage, not geometry. No golden
pins `engagement_start.reach_A` on turn ≥ 2.

---

### F-2 — HIGH — every fatal blow is invisible in the trace's damage channel

**Where.** Six early returns bypass the `outcome` emit at `:449`: `:187` (disengage pursuit), `:220`
(stop-hit), `:370` (displace pull-back graze), `:392` (main exchange), `:413` (bind loop), `:424` (riposte).

**Scenario.** `outcome` is the **only** emit carrying a damage figure (`hit`). Each of the six sites applies
the wound and then `return`s before reaching `:449`. Consequence: the killing blow's damage is never emitted,
and the trace's last exchange-level event before `engagement_end(felled=X)` is a *pre-mutation* emit.

**Magnitude [M5], [M6].** 200 fights, 5 matchups, both `light`:

- 627 `core.strike` calls; **233 (37.2%) at sites whose emit carries no damage field**:

  | wrapper line | calls | reaches `outcome.hit`? |
  |---|---|---|
  | `:185` disengage pursuit | 12 | no |
  | `:216` stop-hit | 205 | no |
  | `:409` bind loop | 16 | no |
  | `:322`/`:323`/`:328`/`:331`/`:343` main exchange | 394 | yes |

- 199 fellings. **The emit immediately preceding `engagement_end(felled=…)` was `roll` 114×, `stophit` 83×,
  `disengage` 2× — and `outcome` 0×. Zero. 100% of fatal blows are unreported.**
- Cross-check: 394 strike calls at "reported" sites but only 281 `outcome` events with `hit > 0` — the
  113-event gap is exactly the fights whose exchange killed and returned at `:392`.

**Key-layer consequence (feeds §1.4 G-4).** `scene.combat_felled` will always arrive with **no antecedent
`scene.combat_hit`**, and `scene.combat_resolved.wounds_inflicted` cannot be reconstructed from the trace at
all.

**Could an existing test see it?** **No.** `state_graph.fired_states_from_events` maps
`engagement_end(felled)` → `Felled` and the coverage check passes. Nothing asserts that a felling is preceded
by a damage-bearing event.

---

### F-3 — HIGH — `sim` is provably always `False`; `wrapper.py:344`, `:417–424` is dead code

**Where.** `wrapper.py:344` (`sim = (hit > 0 and riposte)`), consumed at `:417–424`.

**Scenario.** `sim` is computed at `:344`, immediately after the outcome mapping (`:319–343`). Enumerating
that mapping, `hit > 0` and `riposte` are **mutually exclusive at that point**:

| `deg` | outcome | `hit` | `riposte` |
|---|---|---|---|
| `fail` (`:319`) | riposte roll only | 0 | maybe |
| `partial` (`:321`) | dodge/parry graze **or** bind | maybe | False |
| `success` (`:325`) | bind **xor** riposte **xor** hit — three exclusive branches | maybe | maybe, never with hit |
| `overwhelming` (`:329`) | hit or 0 | maybe | False |
| counter lands (`:335`) | `hit = 0; riposte = True` | 0 | True |
| counter misses (`:337`) | `riposte = False`; hit assigned | maybe | False |

`riposte` *is* later set `True` at `:371` (displace) and `:415` (bind) — but both are **after** `:344`, so
they cannot make `sim` true. Therefore `sim` is always `False`, and the entire "simultaneous exchange"
block — the aggressor eating a riposte graze while completing his own blow, gated on
`S.disrupt_resist_p` — **never executes**. `disrupt_resist_p`'s only call site is `:419`, so that function is
dead in practice.

**Magnitude [M7].** 360 fights: `if sim:` (`:417`) evaluated **455 times**, body (`:419`) entered **0 times**.
`:420` and `:424` likewise 0.

**Class.** This belongs on I2's dead-surface list (`combat_execution_plan.md` §15 I2), which does not
currently carry it. Note the asymmetry with `beat_exhaustion`/`collapse`: those are *reachable* branches a
narrow sweep mislabels (ED-PC-0042, `state_graph.py:29–35`); `sim` is **structurally** unreachable and the
argument above is a proof, not a sweep.

**Could an existing test see it?** **No.** No test names `sim` or `disrupt_resist_p`; the `structure_scan.py`
zero-caller sweep would not flag `disrupt_resist_p` because it *has* a caller — the caller is simply never
reached.

---

### F-4 — MEDIUM-HIGH — `disengage` is an emit kind no declaration knows about, and the guard is one-directional

**Where.** `wrapper.py:178`, `:183` emit `'disengage'`. `state_graph.py:20–23` `TRACE_KINDS` lists **14**
kinds and does **not** include it. No `STATES` node declares it, and no node models the
reopen / disengage / pursuit transition at all — `AwaitTempo` (`state_graph.py:43`) has `'emits': []`.

**Scenario.** `tests/valoria/test_combat_state_graph.py:40–44` (`test_emit_legality`) asserts
`declared emit ∈ TRACE_KINDS`. It does **not** assert the converse (`emitted kind ∈ TRACE_KINDS`). So a kind
the engine actually fires can be entirely absent from the declared vocabulary and every gate stays green.
Any consumer built from `TRACE_KINDS` — including a Key-mapping layer, which is precisely what I4 is
producing — would silently drop `disengage`. That matters because the `pursued` branch can **fell**
(`:187`): 2 of 199 fellings [M6] are reached through a kind the declaration does not admit exists.

**Magnitude [M5] corpus.** `disengage` fired 36 times across the 200-fight sweep.

**Could an existing test see it?** **The existing test passes.** That is the finding: the guard direction is
wrong. The one-line falsifier — `assert observed_kinds <= G.TRACE_KINDS` over a live sweep — does not exist.

---

### F-5 — MEDIUM — `fight_result` can contradict `engagement_end(felled)`

**Where.** `wrapper.py:493–495`.

**Scenario.** `engagement_end(felled=X)` is emitted inside the turn loop (`:481`) the moment X is felled.
Afterwards, `:493` applies `UPSET_FLOOR` (0.05, `config.py:257`, an explicit designer rule) and **flips the
result**, then `:495` emits `fight_result(winner=…)`. So the trace can contain, in order:
`engagement_end(felled='A')` … `fight_result(winner='A')`.

**Key-layer consequence.** `scene.combat_felled(actor_id=A)` followed by
`scene.combat_resolved(outcome: A won)` — two Keys, both `permanence: indelible`/`persistent`, in direct
contradiction. NPC memory and faction consumers (registry `:742`, `:793`) would ingest both.

**Magnitude [M8].** 2 000 fights, 1 993 decided: **94 (4.72%)** have `fight_result.winner` equal to the label
`engagement_end` reported felled — matching `UPSET_FLOOR = 0.05` as expected.

**Could an existing test see it?** **No.** `fired_states_from_events` routes `winner is not None` → `Decided`
and never cross-checks against `felled`.

---

### F-6 — MEDIUM — engagement-start RNG draw count depends on static configuration (draw-in-a-conditional)

**Where.** Four configuration-gated draws: `:66` (reach tie coin-flip), `:80` (soft closed-latch band),
`:93` (re-presentation gate, short-circuited when `represent_p == 1.0`), `:382` (2H freed-hand shove).

**Scenario.** Each is a `rng.random()` that is consumed **only on some configurations**, so two runs that are
logically "the same experiment with one thing changed" consume different numbers of draws and their streams
desynchronise from that point on. Unlike an *outcome*-conditional draw (unavoidable in a branching sim),
these are gated on **static geometry and equipment**:

- `:66` — drawn only when `reach_A == reach_B` exactly.
- `:80` — drawn only when `measure_gap` falls **strictly inside** the latch band `[0.0, 0.6]`.
- `:93` — drawn only when `represent_p < 1.0`, i.e. only at mail/plate (deliberate and documented at
  `combat_systems.py:705`, but still armour-dependent).
- `:382` — drawn **on every closed beat** when the longer weapon is two-handed, never when it is one-handed.
- `:235` additionally switches RNG *method* (`rng.randrange(2)` instead of `rng.random()`), consuming the
  underlying stream differently — reachable only on exact float equality of `ready[A]`/`ready[B]`, so
  effectively never, but it is a second method on the same stream.

**Magnitude [M4], [M7].** Cumulative draws consumed at the moment the `engagement_start` emit fires, seed 0,
`max_bouts=1`:

| matchup | `measure_gap` | in latch band? | reach tie? | draws @ `engagement_start` |
|---|---|---|---|---|
| spear v dagger | 3.35 | no | no | **3** |
| rapier v mace | 1.04 | no | no | **3** |
| staff v arming | 1.07 | no | no | **3** |
| greatsword v dagger | 2.50 | no | no | **3** |
| longsword v arming | 0.57 | **yes** | no | **4** |
| arming v arming | 0.00 | no | **yes** | **4** |

The count is 3 or 4 **purely as a function of static reach geometry**, before a single decision is made.
`:382`'s condition was evaluated **2 586 times in 360 fights [M7]** (407 successes) — for a one-handed longer
weapon that is 2 586 draws that never happen.

**What this does and does not break — [MEASURED, and a correction to the obvious inference].** The natural
claim is "the balance harness's paired-seed comparisons are void". **That claim is wrong for the current
harness and I am not making it.** `workbench/balance.py:22` `_seed(key)` derives a **per-cell** seed from a
`crc32` of the cell key, so different weapons/attributes already get different seeds — the harness never
relied on common random numbers across cells. The live hazard is therefore **prospective**: any future
ablation, A/B or variance-reduction harness that assumes "same seed ⇒ same stream, one factor changed" is
invalid by construction here, and per §0.1 point 4 that is exactly the "are the two arms the same
experiment?" question a controlled measurement has to answer. Recording it so the answer exists before
someone needs it.

**Could an existing test see it?** **No.** Goldens pin *values*; nothing pins stream alignment across
configurations.

---

### F-7 — MEDIUM — the `just_closed` beat runs the closed exchange on open-measure grip / facing / range_avail

**Where.** `wrapper.py:133–135` (per-beat derived geometry), `:222–225` (`approach_step` then the
`just_closed` latch), `:231+` (closed exchange), `:252` (`er` REFRESH #2).

**Scenario.** At the top of each beat, `grip_position`, `range_avail` and `facing` are derived from the
**current** `closed` and `measure_gap`:

```python
c.grip_position = S.grip_target(c, closed, cfg)          # :133
c.range_avail  = S.range_utilization(c, measure_gap, cfg) # :134
c.facing       = S.facing_target(c, closed, cfg)          # :135
```

In the approach branch, `measure_gap` is then decremented (`:222`) and `closed` may flip to `True` (`:224–225`).
When it does, control **falls through into the closed exchange in the same beat** (`:228`'s `continue` is
skipped). The `sel_*` family **is** correctly refreshed for both roles at `:247–251`, but `grip_position`,
`range_avail` and `facing` are **not** — so the closed exchange resolves on *open-measure* body geometry:
`grip_target` returns the ungathered grip, `range_utilization` used the pre-step gap, `facing` used
`closed=False`.

**The self-inconsistency this creates.** `:252`'s comment says REFRESH #2 *"re-derives `er` … on the
grip+FORM-aware POST-SWAP weapon"* and adds *"Consistency-proven: at open measure (grip=0, no swap) this
equals #1 exactly."* On a `just_closed` beat that consistency proof is not a reassurance — it is the bug: the
grip **is** still 0 because nothing re-derived it, so REFRESH #2's "grip-aware" claim is vacuous on exactly
the beat where the grip should have changed.

Downstream consumers of the stale trio in the same beat: `reach_sigma` (`:268`, via `er` and `facing`),
`commit_depth`'s Beta window and the swing-room legibility term (via `range_avail`), and `select_mode`'s
`Φ_room` — the last of which *is* re-run at `:248` but reads the stale `range_avail` written at `:134`.

**Magnitude.** **[UNQUANTIFIED]** — measuring the balance delta requires re-deriving the trio mid-beat, which
is a behaviour change and out of scope for a read-only pass. The *frequency* is bounded by
`approach.just_closed = True`, which the trace already exposes; a follow-up can count it without touching
behaviour.

**Could an existing test see it?** **No.**

---

### F-8 — MEDIUM-LOW — grapple outcomes do not participate in the burst-termination predicate

**Where.** `wrapper.py:433–448` (contact axis) and `:462` (clean-defence separation).

**Scenario.** The contact block mutates `poise` and `initiative` for `disarm`/`throw`/`pin`/`foot_pin`/
`control` but sets **none** of `hit`, `bind`, `riposte`. The burst-continuation test at `:462` is
`if not (hit>0 or riposte or bind)`. So a beat in which the aggressor **threw or pinned** the defender can
immediately emit `separation(reason='clean_defence')` — "an exchange resolved cleanly on defence, so the
measure breaks" (`:456–457`) — which is the opposite of what happened.

**Magnitude [M7] corpus.** 360 fights: **801** effective (non-`escape`) grapple outcomes, of which **418
(52.2%)** are followed by an `outcome` with `hit == 0`, `bind == False`, `riposte == False` — i.e. satisfy
`:462` and terminate the burst.

**Could an existing test see it?** **No.** `test_combat_state_graph.py`'s contact tests assert the node is
reachable and fires; nothing asserts what follows it.

---

### F-9 — LOW (contract, load-bearing for the port) — emit-before-mutation is the rule; `outcome` is the exception

**Where.** `:213` `stophit` precedes the strike/wound/stagger at `:216–221`. `:183` `disengage(pursued)`
precedes the pursuit strike at `:185`. `:436` `contact` precedes the poise/initiative mutations at `:440–448`.
`:449` `outcome` is emitted **after** its mutations.

**Scenario.** Decision-node emits report the **inputs** a node consumed — which is exactly what the TRACE
SEAM docstring promises (`:12–15`) and correct for the workbench's branch explorer. But it means a
Key-publishing port that emits at those seams publishes **pre-mutation** state, while the same port emitting
at `outcome` publishes **post-mutation** state. Mixing the two in one Key stream produces an ordering a
consumer cannot interpret without per-kind knowledge.

**Not a defect in the engine** — it is an undocumented contract. Recorded so the port picks one ordering and
states it, rather than inheriting the inconsistency.

**Could an existing test see it?** N/A (no behaviour to observe).

---

### F-10 — LOW — unreachable branch at `wrapper.py:365`

**Where.** `wrapper.py:365`: `if not closed: closed=True; measure_gap=0.0; ready=_carry(ready,cfg)`, inside
the DISPLACE block in the closed-exchange tail.

**Scenario.** `closed` is provably `True` at `:365`. The only route into the code below `:231` is: either
`closed` was already `True` at `:190`, or the approach branch ran and either `continue`d at `:230` (so we
never reach `:231`) or set `closed = True` at `:225`. Nothing between `:231` and `:365` clears it. So the
guard can never be taken and the three statements are dead.

**Magnitude [M7].** `:365` was *evaluated* once in 360 fights (`:367` also once — the DISPLACE block itself is
rare). Because it is a one-line `if X: body`, `settrace` cannot distinguish test from body — the
unreachability argument above is **static, not measured**, and is the load-bearing evidence.

**Could an existing test see it?** **No.**

---

### F-11 — LOW — dead assignment `close = closed` at `wrapper.py:307`

`close` is assigned with the comment *"C-1: per-beat close-coupling follows the engagement measure-state"* and
**never read**. Grep for the bare identifier `close` in `wrapper.py` returns only comment prose and the
distinct names `close_rate` / `close_tempo` / `closed`. I2-class dead surface, not currently on I2's list.

---

### F-12 — LOW, **[UNQUANTIFIED]** — `ready` has no floor within an engagement

**Where.** `wrapper.py:261`; contrast `_carry` (`:38–45`).

**Scenario.** `ready[aggressor] -= RECOVERY_TEMPO_K * (commit-2.0) * recoverability_factor(aggressor, cfg)`
with `RECOVERY_TEMPO_K = 0.15` (`config.py:177`) and no clamp. `_carry`'s own docstring (`:40–41`) states
`recoverability_factor` spans **0.3–67.8** and that overcommit "can drive [readiness] deeply negative — a
committed guandao can owe ~−30". `_carry` clamps that debt to 0, but **only at phase transitions**
(`:158`, `:177`, `:225`, `:365`). Within a closed engagement there is no floor, while `ACT_THRESHOLD = 2.5`
(`config.py:112`) and the beat budget is `soft*3 = 24` (`:111`, `:117`). A fighter carrying ≈−30 needs
~13 beats of accumulation to act again and can be tempo-locked for the remainder of the engagement.

**Honest status.** I have **not** measured whether the tail of the `recoverability_factor` distribution is
actually reached with `commit ≈ 5` in live play — that needs a per-weapon sweep. Reported as an
unquantified structural hazard, explicitly **not** as a demonstrated defect. The asymmetry is the point: the
`_carry` fix (ED-PC-0037.1) recognised this debt as real enough to clamp at transitions and left the
within-engagement case unclamped without saying why.

---

### F-13 — LOW, informational — `reopen_moment` / `push_avail` lifetime and the disengage ordering

`reopen_moment` and `push_avail` are set in the outcome tail (`:375–383`), consumed by the reopen check at
the **next** beat's `:155–160`, and unconditionally cleared at `:161`. Because `:161` runs **before** the
disengage block at `:171`, a moment created last beat is already gone by the time a disengage attempt is
evaluated. That is consistent with `:161`'s stated intent (RR-01: the moment is fleeting) and I do **not**
call it a defect — it is recorded because the flags' one-beat lifetime and the `:155` → `:161` → `:171`
ordering are load-bearing and undocumented, and any future reordering of those three blocks silently changes
reopen behaviour.

---

## §2.1 Checked and found sound (negative results, stated so the audit is falsifiable)

Per §0.1 point 4 — absence of a failure is only informative if the check that would have found it is named.

| checked | verdict |
|---|---|
| **`sel_*` pre-write reads inside the beat loop** (the (a) target) | **Sound.** `:132–140` writes all eight `sel_*` fields for **both** `A` and `B` unconditionally at the top of every beat, before any reader; `:247–251` re-writes both roles after the half-sword swap, with the spelled (non-positional) pairing ED-PC-0042/I3 introduced. All readers (`core.py:481–493`, `combat_systems.py:659,673,816,839,849,1063–1074`, `weapon_physics.py:257–383,658–681`) are reached after the write. No pre-write read found. |
| **`sel_*` read across the engagement boundary** (the `represent_measure_p` instance) | **Already fixed, verified by reading the code.** `:92` calls `S.represent_measure_p` **before** the beat loop, which is exactly the ED-PC-0034 hazard — but the function (`combat_systems.py:677+`) now derives its own open-measure geometry (`grip = 0.0`, room from `range_utilization(measure_gap)`) instead of reading live `sel_*`/`grip_position`. Confirmed by inspection: it touches no `sel_*` field. **This is the one instance the brief flagged, and it is closed.** F-1 is the *same class* on a different field (`.weapon`) and is **not** closed. |
| **`steal` cross-beat leak** (`:300` write, `:340` read) | **Sound.** `steal` is bound only inside `if read_win and commit>=4` (`:299`), the same branch that sets `counter_attempt` (`:303`); `counter_attempt` is reset to `False` every beat at `:298`. `:340` is reachable only under `counter_attempt`, so `steal` is always this beat's value. Fragile (a loop-local relied on for scoping) but correct. |
| **`opening_created` carry** | **Sound.** Reset at `:348` every beat, set at `:364`/`:376`/`:379`/`:383`/`:394` (the bind branch — added by the adversarial pass), consumed once at `:433`. All set sites lie between the reset and the consume; never crosses a beat, as its comment claims. |
| **Role-object inversion** (the bug class the module was built to cure) | **Sound.** No subsystem indexes raw `'A'`/`'B'`; the riposte flip at `:426` swaps object references, and the frozen `_agg0`/`_def0` labels (`:239`) are used only for emit payloads. The one consequence is reporting, not resolution — see row 11's note. |
| **`grip_position` / `lunge_depth` engagement reset** (ED-PC-0033) | **Sound and working** (`:59–60`). Its scope is the finding (F-1), not its correctness. |
| **Dict/set iteration order in RNG-consuming code** | **Sound.** `ready = {c: rng.random()*… for c in (A,B)}` (`:110`) and `rate = {c: … for c in (A,B)}` (`:142–143`) iterate a **tuple**, so draw order is deterministic. `combat_systems.read_contest:979` explicitly pins `list(V.DEFENCE_MODES)` order as part of the RNG contract. |

---

## §3 Next actions (for the orchestrator — none taken here)

1. **File ED-PC-0044** in `registers/editorial_ledger_pc.jsonl` citing this document.
2. **Hand §1 to IN Wave 3**, including §1.4's eight gaps. G-1 (no grapple type) and G-3 (unproducible
   `outcome` vocabulary) block a faithful mapping and are registry decisions, not PC ones.
3. **Route F-1 to a PC fix batch.** It is a behaviour change on the armour-participation surface, so it needs
   the full §0.1 treatment: a write-sweep guard on `.weapon` mirroring
   `tests/valoria/test_morale_write_sweep.py`'s `_CELL_OWNED` pattern, a named falsifier, and a golden-blast
   assessment before anything moves. **Do not fold it into a "behaviour-preserving" batch.**
4. **Route F-2 + F-4 + F-5 together** — all three are trace/Key-contract defects and the fixes touch the same
   emit sites. F-4's fix is one assertion (`observed_kinds <= TRACE_KINDS` over a live sweep) and is the
   cheapest guard in this document.
5. **Add F-3 and F-11 to I2's dead-surface list**, which does not currently carry them; F-3 also retires
   `S.disrupt_resist_p`'s only reachable caller, so removing the block and the function is one change, not
   two.
6. **F-6 needs no fix, only a written contract**: state in the engine docstring that the RNG stream is
   configuration-dependent, so nobody builds a paired-seed ablation on top of it.
