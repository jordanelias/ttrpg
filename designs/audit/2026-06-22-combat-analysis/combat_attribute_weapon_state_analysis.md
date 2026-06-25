# Combat Engine — Attribute/Weapon Impact, State Graph, and Tradition-Ability Opportunities
**2026-06-22 (rev. 2) · `designs/scene/combat_engine_v1/` · balance probe on committed HEAD**

*rev. 2: plain-English terms (no fencing jargon); marginal attribute table; resolution outcome shown as a branch, not a sequence; wound model updated to the ED-1041 bilateral-Ob channel.*

`[SELF-AUTHORED — bias risk: analysis of an engine this session also edited. Findings are sim-grounded (position-swapped, −1/0/+1 attribution, mirror sanity-checked) and read-grounded (engagement() lines 16-274).]`

Method: each factor varied against a uniform baseline opponent, 500–800 fights per cell, attacker/defender positions swapped to cancel first-mover effects, `fight()`'s `−1/0/+1` return correctly attributed. Mirror cells ~50% (fairness confirmed). Draws ~0% at `max_bouts=40`.

---

## 1 — ATTRIBUTE IMPACT (marginal — what a single point buys)

The decision-relevant view: all nine attributes at 3, raise **one**, measure the raised fighter's win-rate. Mirror sits at 51.2 here, so effects are relative to that.

| Attribute | win@4 (+1) | win@5 (+2) | what +1 buys | primary channel |
|---|---|---|---|---|
| **Strength** | 85.7 | 93.7 | **+35.7pp** | strike impact, leverage (bind/displace), handling |
| **Cognition** | 85.8 | 91.7 | **+35.8pp** | reading (visual read + initiative term) |
| History | 83.5 | 93.5 | +33.5pp | the resolution pool `max(5,History+6)` + initiative experience |
| Endurance | 81.6 | 91.7 | +31.6pp | stamina (tempo/cost/balance) + health |
| Attunement | 79.0 | 87.7 | +29.0pp | reading (paired with Cognition) |
| Agility | 78.5 | 88.6 | +28.5pp | initiative tempo, footwork, reflex |
| Spirit | 66.2 | 73.3 | +16.2pp | feeds stamina/concentration/health — contributor |
| Disposition | 53.7 | 52.0 | +3.7pp | risk-style axis — both poles cost (≈neutral) |
| Focus | 51.0 | 60.8 | +1.0pp | concentration/poise/disruption-resist (protective; ramps later) |

**Findings.** At the center of the range the highest-leverage single point is **Strength or Cognition (~+36pp each)**; History/Endurance next; Attunement/Agility next; Spirit a real but lower contributor; Focus near-zero for the first point but ramps (it's protective, not offensive); Disposition ≈neutral by design. The *cumulative* win@7 endpoints rank differently (History/Agility/Cognition ~96%) because they reflect total investment, not the next point — the marginal table is the one to budget against.

**Balance note (Jordan's call):** reading is double-weighted — both Cognition and Attunement feed it and both rank high. Fine if it's one capability split across two stats; near-interchangeable in outcome if they were meant to be distinct.

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
- **Reach dominates: r = +0.83** between reach and win-rate — the strongest weapon characteristic.
- **Reach is grounded, not arbitrary: it correlates r = +0.87 with the actual blade-length field.** `reach_base` uses a parametric formula (`4.0 body + 2.0 long-flag + 0.8 two-handed + head-type bonus + reach_adj`), and the `reach_adj` constants are tuned so the result tracks blade length. The point head-type gets the max reach bonus (+1.0 vs +0.5 cut vs +0.0 blunt) because a thrust extends — which is why the rapier (point) reaches 7.15. Caveat: this makes a thrusting rapier reach nearly as far as a much-longer greatsword (7.25), which may overweight thrust-extension; and `paired_short` lands at exactly arming-sword reach via a heavy +1.40 `reach_adj`, arguably too long for a short sword.
- **Guards and dimensions are wired** — `blade_guard` drives the bind catch (the cross controls the opposing blade), `grip_len/head_len` drive leverage, `mass`/point-of-balance drive damage and handling. They're not in `reach_base` specifically, but the weapon's physics is used.
- **Delivery secondary** (point/thrust hardest to read in the legibility model, but co-varies with reach in the fixed roster); **weight is not a primary driver** (heavy-but-short mace tanks).
- **Balance flag:** at equal stats and equal (light) armour, weapon choice ≈ reach choice — the closing mechanics don't fully compensate at uniform-4. Armour and attribute asymmetry will compress this; untested here.

## 3 — STATE GRAPH (the per-turn machine; outcome is a branch, not a sequence)

`engagement()` walks these points each beat (a turn = approach → emergent burst of exchanges → separation). "Initiative" below is the held edge; "the steal" is an in-tempo counter that seizes it.

**Pre-exchange (distance & state, recomputed every beat):**
| Point | Mechanic | Attributes → | Weapon → |
|---|---|---|---|
| Reach / measure | `reach_base` → gap; closed vs approach | — | reach |
| Initiative hold & drift | high measure holds the edge; disposition drifts it (both poles cost) | Disposition | — |
| Poise recovery | balance regathers; Focus speeds it | Focus | — |
| Tempo / cadence | weapon speed × stamina-fatigue → readiness | Endurance, Spirit | spd |
| Reach re-opening | longer weapon re-makes distance on a created moment | Cognition, Attunement, Agility | reach, hands |

**Approach (out of measure):** closing rate (Agility balance × weapon tempo); **stop-hit** — a longer weapon threatens, rolling `pool(History)` vs reach → strike (weapon reach, History, Strength).

**Closed exchange (resolution core):**
| Point | Mechanic | Attributes → | Weapon → |
|---|---|---|---|
| Aggressor selection | who crosses the action threshold first (tempo) | Endurance, Spirit | spd |
| Half-sword switch | form adapts to range/armour | — | halfsword geo |
| Commit depth (2–5) | disposition skews deep/shallow; costs stamina | Disposition, Endurance | — |
| Visual read | `reading × familiarity × legibility × (1−mental-fat)` | Cognition, Attunement, Focus | head, armour |
| Defence mode | parry/dodge/wind by mode sigma; read picks best | — | — |
| Defender sigma | mode sigma − handling + stance | Agility, Strength | weight, hand |
| Attacker sigma | commit + initiative − OOB − handling + consistency | Agi+Cog+Att+History, Focus | weight |
| Armour-defeat | controls armoured exchanges | (Strength minor) | percussion, head, armour |
| **Resolution roll** | `pool = max(5,History+6)`; `net_sigma` → degree | **History**, **wounds (Ob)** | (all of net_sigma) |
| The steal | read wins + commit ≥4 → seize initiative, counter | Cognition/Attunement, Disposition | — |
| Overcommit exposure | deep commit past balance → lose initiative/poise | Agility | — |

**Outcome — a single branch, not a sequence.** The resolution roll produces **exactly one of: MISS / HIT / BIND / RIPOSTE.** They are alternative results of the same roll, not ordered steps:
- **MISS** — clean defence; the exchange may end.
- **HIT** — lands → `apply_wound` (Strength/weapon damage, Endurance absorbs); initiative/poise shift by hit size.
- **BIND** — blades lock → `bind_sigma` (leverage + guard catch + tactile, Strength minor, **+ wound Ob**) decides who dominates; winner seizes initiative + breaks the loser's balance.
- **RIPOSTE** — defender reverses; role flips; Focus lets the original aggressor complete through the blow.

**Wounds apply only on a landed strike** — the HIT branch, a strike produced inside the bind, or a landing riposte. The swing/commit itself never wounds. Each wound impairs both roles via an obstacle (Ob): **−0.15 net when the wounded fighter attacks, +0.25 net when they defend** (defence ~1.6×; ED-1041), applied in the main resolution, the stop-hit, and the bind.

## 4 — TRADITION-ABILITY HOOKS

The engine carries named, mostly-neutral hooks where a tradition's signature ability plugs in:

**Channel-weight biases (the cognitive-mode lean over the shared substrate):** `tempo` (initiative gain, counter-selection, overcommit recovery), `visual` (reading/anticipation), `leverage` (bind dominance + balance-break).

**Explicit ability hooks (placeholders today):** `counter_select` (how often the counter is reached for), `counter_success` (its landing — code: *abilities modulate this upward*), `anti_overcommit` (exposure reduction on deep commits).

**Scalar levers already tradition-keyed:** initiative-steal magnitude (counter & bind), initiative-hold (holding the measure), `familiarity` (reading degrades vs an unfamiliar style — a built-in counter to mirror-matches), half-sword adoption.

**Four signature schools map cleanly:** pressure/tempo (tempo + counter-select + steal up); defensive/reading (visual + anti-overcommit + hold up); grappling/half-sword (leverage + bind-steal + counter-success up); veteran/generalist (familiarity breadth, no single spiked channel). These are *attachment points*; the roster of named traditions and their flavour stays creative-layer (Jordan's).

## 5 — HONESTY & STATE OF RECORD

`[NULL: engine fairness — mirror cells ~50% across all sweeps; the prior "50% stall" and first-mover bias were attribution artifacts (ED-1040), confirmed absent]`
`[CONFIDENCE: high — attribute ranking, reach dominance (r=+0.83) and grounding (r=+0.87 blade-length), state-graph influences (read from engagement()), wound-Ob effect (validated). medium — delivery/weight isolation (fixed roster confounds reach×delivery×hands); attribute×weapon and armour-tier interactions untested]`
`[GAP: tested at uniform attributes + light armour + tradition none only. Armour-tier matchups, attribute×weapon interactions, and live tradition-ability values are each a follow-on matrix.]`

**State of record (wound model):** the wound penalty is the ED-1041 bilateral Ob (committed: `ab4e550c` net_sigma+stop-hit, `300d7081` bind). The wound **count** model carries open drift — code runs `WI = round(2.6·End+1.6·Str+1.0·Spi)`, N=4, but `derived_stats_v30 §4.1` still specifies Endurance-only interval + max 3 (ED-1042, open for Jordan's ratification).
