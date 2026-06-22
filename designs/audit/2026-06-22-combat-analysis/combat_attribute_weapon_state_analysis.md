# Combat Engine — Attribute/Weapon Impact, State Graph, and Tradition-Ability Opportunities
**2026-06-22 · `designs/scene/combat_engine_v1/` (additive engine, post-ED-1040) · balance probe on committed HEAD**

`[SELF-AUTHORED — bias risk: analysis of an engine this session also edited (additive revert). Findings are sim-grounded (N=500, position-swapped, −1/0/+1 attribution, mirror sanity-checked) + read-grounded (engagement() lines 16-274).]`

Method: each factor varied against a **uniform-4 baseline** opponent (all nine attributes = 4, arming sword, light armour, tradition `none`), 500 fights per cell, attacker/defender positions swapped to cancel first-mover effects, `fight()`'s `−1/0/+1` return correctly attributed. Mirror cells return ~49% (fairness confirmed). Draws ~0% at `max_bouts=40`.

---

## 1 — ATTRIBUTE IMPACT ON WINNING

Win-rate of a fighter with one attribute raised/lowered, vs the uniform-4 baseline:

| Attribute | win@1 | win@4 (mirror) | win@7 | swing(7−1) | primary channel |
|---|---|---|---|---|---|
| **History** | 4.8 | 49.0 | **96.2** | +91.4 | *is* the resolution pool `max(5,History+6)` + initiative experience term |
| **Agility** | 7.2 | 49.0 | **95.8** | +88.6 | initiative tempo (`INIT_K·Δagi`), footwork (closing/re-open), reflex (counter) |
| **Cognition** | 5.8 | 49.0 | **95.6** | +89.8 | reading (visual read + initiative reading term) |
| **Endurance** | 7.2 | 49.0 | 93.8 | +86.6 | Stamina (→ tempo, commit cost, OOB) + Health |
| **Strength** | 5.6 | 49.0 | 93.2 | +87.6 | strike impact (`strength+heft`), leverage (bind/displace), handling |
| **Attunement** | 6.8 | 49.0 | 93.0 | +86.2 | reading (paired with Cognition) |
| **Spirit** | 13.4 | 49.0 | 82.4 | +69.0 | feeds Stamina/Concentration/Health — contributor, not a primary axis |
| **Focus** | 32.2 | 49.0 | 66.0 | +33.8 | Concentration (consistency, mental-fatigue resist), poise recovery, riposte disruption-resist |
| **Disposition** | 53.2 | 49.0 | 50.8 | −2.4 | risk-style axis (Vor drift + commit skew) — **both poles cost; ~neutral by design** |

**Findings.**
- **Three dominant levers — History, Agility, Cognition (~96%).** Pool size, tempo/initiative, and reading. A +3 swing on any is near-decisive at equal everything else.
- **Second tier — Endurance, Strength, Attunement (~93%).** Stamina/health, damage/leverage, reading-partner.
- **Spirit (82%)** is a derived-stat *contributor* — it raises Stamina, Concentration, and Health but owns no resolution term directly, so its leverage is real but lower.
- **Focus (66%)** is protective, not offensive — it buys structure-recovery and mental-fatigue resistance, a defensive edge.
- **Disposition is ~neutral (50.8%), and that is correct.** It drifts the Vor and skews commit depth; aggressive presses (builds Vor, exposes to riposte) and cautious cedes (defends, slower) — a genuine tradeoff axis, not a power stat. The slight cautious edge at the extreme (53.2 @1) is the defensive bias, not an imbalance.
- **Balance note (Jordan's call):** reading is double-weighted — both Cognition *and* Attunement feed it, and both land in the top tiers. If reading is meant to be one capability split across two stats, that is fine; if the two were meant to be distinguishable, they are currently near-interchangeable in combat outcome.

---

## 2 — WEAPON CHARACTERISTIC IMPACT

Win-rate of each weapon vs the arming sword (both fighters uniform-4):

| Weapon | win% | head | weight | reach | hands |
|---|---|---|---|---|---|
| rapier | 94.2 | point | light | 7.15 | 1 |
| spear | 94.2 | point | light | 7.80 | 2 |
| staff | 90.8 | blunt | light | 7.30 | 2 |
| paired_short | 87.0 | cut_thrust | light | 5.90 | 1 |
| poleaxe | 83.4 | blunt | heavy | 6.75 | 2 |
| sabre | 80.0 | curved_cut | light | 6.40 | 1 |
| greatsword | 79.2 | straight_cut | heavy | 7.25 | 2 |
| longsword | 72.2 | cut_thrust | heavy | 6.40 | 2 |
| longsword_halfsword | 71.0 | point | heavy | 5.80 | 2 |
| **arming (baseline)** | 49.0 | cut_thrust | light | 5.90 | 1 |
| dagger | 26.8 | cut_thrust | light | 4.50 | 1 |
| mace | 24.8 | blunt | heavy | 5.45 | 1 |

**Findings.**
- **Reach dominates: Pearson r = +0.83** between reach and win-rate. This is the single strongest weapon characteristic. The roster sorts almost monotonically by reach.
- **Delivery is secondary and partly real: point/thrust ranks highest (86.5% mean).** Mechanically grounded — the engine's `legibility` makes in-line thrusts *hard to read* (the defender's read drops vs a thrust, rises vs a swing), so point weapons land more. But the three point weapons here are also long (rapier/spear), so reach and "hard-to-read" reinforce; `longsword_halfsword` (point but reach 5.8) at 71% shows the delivery effect surviving short reach partially.
- **Weight is not a primary driver.** Heavy-but-short `mace` (24.8) and heavy-but-mid `longsword` (72.2) bracket the field; reach, not mass, predicts the outcome. With additive impact (ED-1040), heft adds a flat damage bonus that the win-rate saturates over (as the M-STR sim already showed).
- **`paired_short` (87%) and `rapier` (94%, 1h) prove 1-handed can top the field** — `hands` correlates with win only because 2h weapons tend to be longer, not because two-handing itself wins.
- **Balance flag (Jordan's call):** at equal stats and equal (light) armour, weapon choice ≈ reach choice. The closing mechanics (approach, stop-hits, displace-and-step-inside, reach re-opening) exist specifically to let a shorter weapon counter reach, but at uniform-4 they do not fully compensate — the longest weapon wins ~9 in 10. Whether that is intended (longer weapons *should* hold the measure) or too flat (weapon variety collapses to "pick the longest") is a design decision, not a mechanical defect. Armour and attribute asymmetry will compress this; that interaction is untested here.

---

## 3 — STATE GRAPH: every mechanic point and its attribute/weapon influence

`engagement()` is the per-turn state machine (a turn = approach → emergent burst of exchanges → separation). Each beat walks these points. `[READ: wrapper.py — engagement() lines 16-274; core.resolve/strike; systems.py helpers]`

**Pre-exchange (distance & state, recomputed every beat):**
| # | State point | Mechanic | Attributes → | Weapon → |
|---|---|---|---|---|
| 1 | **Reach / measure** | `reach_base` → `measure_gap`; closed vs approach | — | reach, reach_adj |
| 2 | **Vor decay (initiative hold)** | `init_hold_decay` — high measure holds Vor longer | (destreza measure) | — |
| 3 | **Disposition Vor drift** | `disp_lean` drifts initiative ±; both poles cost | **Disposition** | — |
| 4 | **Poise / structure recovery** | balance regathers toward 1.0; Focus speeds it | **Focus** | — |
| 5 | **Tempo / cadence** | `weapon_tempo`/`close_tempo` × stamina-fatigue → readiness | Endurance, Spirit (stamina) | spd |
| 6 | **Reach re-opening** | longer weapon re-makes distance on a created moment | Cognition, Attunement (read), Agility (footwork) | reach, hands (2h shove) |

**Approach phase (out of measure):**
| 7 | **Closing** | `close_rate` = balance × weapon tempo × (1+displace) | Agility (balance) | spd, reach |
| 8 | **Stop-hit** | longer weapon threatens; roll `pool(History)` vs reach-nsig → `strike` | **History** (pool), Strength (damage) | reach, head |

**Closed exchange (the resolution core):**
| 9 | **Aggressor selection** | whoever crosses `ACT_THRESHOLD` first (tempo) | Endurance/Spirit (stamina) | spd |
| 10 | **Half-sword auto-switch** | weapon form adapts to range/armour | — | halfsword geo |
| 11 | **Commit depth (2-5)** | `disp_lean` skews deep/shallow; `act_cost` (stamina) | **Disposition**, Endurance | — |
| 12 | **OOB** | stamina ≤ 0 → attacker sigma penalty | Endurance, Spirit | — |
| 13 | **Visual read** | `reading × tradition-visual × familiarity × legibility × (1−mental-fat)` → `read_win` | **Cognition, Attunement**, Focus (conc) | head (thrust hard, swing easy), defender armour |
| 14 | **Defence mode** | parry/dodge/wind by `mode_sigma`; read_win picks best | (defence) | — |
| 15 | **Defender sigma** | `mode_sigma − handling_penalty + stance_stability` | Agility (stance), Strength (handling) | wt, hand |
| 16 | **Attacker sigma** | `COMMIT·(commit−3) + init − oob − handling + consistency` | Agi+Cog+Att+History (init), Focus (consistency) | wt (handling) |
| 17 | **Initiative term `init`** | `INIT_K·Δagi + reading-Δ + History-Δ`, × tradition tempo | **Agility, Cognition, Attunement, History** | — |
| 18 | **Armour-defeat sigma** | `armor_defeat_sigma` controls armoured exchanges | (Strength minor) | percussion, head (point/blunt), defender armour |
| 19 | **Vor edge** | `initiative_sigma` (bounded; +ve if aggressor holds Vor) | (accumulated) | — |
| 20 | **Resolution roll** | `pool = max(5,History+6) − wounds`; `net_sigma` → degree | **History**, wounds | (all of net_sigma) |
| 21 | **Indes / sen-no-sen steal + counter** | read_win & commit≥4 → steal Vor; counter selected | Cognition/Attunement, Disposition | — |
| 22 | **Overcommit exposure** | `commit − anti_overcommit(balance) − tradition` → Vor/poise loss | Agility (balance) | — |
| 23 | **Outcome mapping** | degree → hit / riposte / bind; `neutralize` by mode | Strength (strike), History+Agi (counter) | head, wt (damage) |
| 24 | **Displace-step-inside** | vs committed thrust, leverage(def) > leverage(agg) | **Strength** (leverage) | head (point), mass |

**Post-strike resolution:**
| 25 | **Hit application** | `apply_wound`; Vor gain/loss; poise stagger ∝ hit size | Endurance (health absorbs) | head/wt (damage) |
| 26 | **Bind** | `bind_sigma` (leverage + tactile, Str minor); kuzushi poise-break ∝ leverage | **Strength** (leverage) | mass, clinch |
| 27 | **Riposte** | role flip; Focus lets aggressor complete through the blow | **Focus** | — |
| 28 | **Burst / turn end** | continues on hit/riposte/bind; ends on clean defence / BURST_MAX / stamina collapse | Endurance, Spirit (stamina) | spd (re-reach) |

**Cross-cutting:** wounds (`−1D` per wound to the *aggressor's* pool, offense-only — point 20) and Stamina/Concentration depletion thread through every beat; Health (Endurance) sets how many strikes a fighter absorbs (point 25).

---

## 4 — TRADITION-ABILITY OPPORTUNITIES

The engine already carries **named tradition hooks** — most currently neutral (`1.0`/`0.0`) with code comments saying abilities plug in here. Each is a place a martial tradition's signature ability differentiates without new mechanics:

**Channel-weight biases (`TR.eff_cw`) — the cognitive-mode lean over the shared substrate:**
- `tempo` (points 17, 21, 22) — initiative gain, counter-selection rate, overcommit recovery. *Italian/tempo traditions.*
- `visual` (point 13) — reading/anticipation strength. *Reading-forward traditions (Liechtenauer Indes, destreza).*
- `leverage` (points 24, 26) — bind dominance and kuzushi (Stärke-Schwäche). *German tactile/winding traditions.*

**Explicit ability hooks (`TR.ability_bonus` / `ability_factor`) — currently placeholders:**
- `counter_select` (point 21) — how often the single-time counter is reached for.
- `counter_success` (point 23) — counter landing; code: *"Tradition abilities will modulate this upward (added later)."*
- `anti_overcommit` (point 22) — exposure reduction on deep commits.

**Scalar levers already tradition-keyed:**
- `init_steal_factor` (points 21, 26) — Vor-steal magnitude on indes and bind.
- `init_hold_decay` (point 2) — Vor retention (destreza holds the measure).
- `familiarity` (point 13) — knowledge-of-others; reading *degrades* vs an unfamiliar tradition (a built-in counter to mirror-matchups and a hook for "studied that style" abilities).
- `halfsword_target` (point 10) — half-sword adoption vs plate.

**Design opportunity map (which hook expresses which signature):**
- **Pressure/tempo school** → `tempo` cw up + `counter_select` up + `init_steal` (open-line) up.
- **Defensive/reading school** → `visual` cw up + `anti_overcommit` up + `init_hold` (measure) up.
- **Grappling/half-sword school** → `leverage` cw up + bind `init_steal` up + `halfsword` readiness + `counter_success` (close) up.
- **Veteran/generalist** → `familiarity` breadth (reads many styles) rather than a single spiked channel.

These are *mechanical hooks*; the *roster of named traditions and their flavour* is creative-layer (Jordan's). This section identifies where abilities attach, not what the traditions are.

---

## 5 — HONESTY BLOCK

`[NULL: engine fairness — mirror cells 49% across all attribute and weapon sweeps; first-mover bias and the prior "50% stall" were attribution artifacts (ED-1040), confirmed absent here]`
`[CONFIDENCE: high — attribute ranking, reach dominance (r=+0.83), state-graph influences (read directly from engagement()). medium — delivery/weight isolation (fixed roster confounds reach×delivery×hands); attribute×weapon and armour interactions untested]`
`[GAP: tested at uniform-4 attributes + light armour + tradition none only. Armour-tier matchups, attribute×weapon interactions, and live tradition-ability values are not measured — each is a follow-on matrix.]`
`[ASSUMPTION: weapon "characteristic impact" measured as marginal win-rate vs arming; basis — the question asks per-characteristic impact, and marginal-vs-baseline is the cleanest isolation the fixed roster allows.]`
