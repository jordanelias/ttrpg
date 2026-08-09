# World churn — the causal model: opportunities, Keys, and the adjudicated build order

## Status: PROPOSED (read-only audit; nothing executed, no head moved, no flag flipped)
## Date: 2026-08-08 · Lane: IN · ED-IN-0149 · Seven causal lenses + two adversarial critics, all Fable-5 read-only
## Method note: lenses were barred from lexical evidence — a term appearing (or not) is not evidence.
## Claims are semantic ("the design defines X as Y, therefore Z"), and every edge is labelled by build state.

---

## §0 · The finding that reframes the programme

**The causal model is not missing. It is declared and unemitted.**

`skills/valoria-vector-audit/scripts/ripple_audit.py` builds the corpus's own declared propagation graph:
**46 nodes, 139 edges.** Of the 94 module-to-module `emits_consumes` edges, **43 are flagged `notional`
by the tool itself**, 40 distinct Key types carry them, and **only 7 of 94 are carried by a Key type with
any live emitter.**

The canonical example chain — *battle → settlement → governance → population → characters* — is **already
in that graph**: `mass_battle → faction_state / npc_behavior / piety_track` via `scene.battle_concluded`
(live emitter, zero consumers), and `settlement_layer → faction_state` via **`env.population_change`**
(declared, no emitter at all).

So the work is not inventing the causal model. It is **emitting on edges the corpus already committed to.**

Two instruments state the same thing independently: `wiring_map_check --summary` reports **`live: 2` of 27
modules**; `trace_execution_phases --seed 42 --seasons 40` shows **no npcs, characters, fieldwork,
threadwork or combat calls at all** across forty seasons.

---

## §1 · The adjudicated build order

Five lenses each nominated their own domain's edge as first — **self-serving by construction**. The
design-logic critic adjudicated across domains. The result overturns the naive ordering.

### 1. THE FISCAL EDGE — `realized_income(s) = Prosperity × stance × compliance(q)` + the L/PS consume step
**It dominates on all three criteria.**
- **Frequency** — it runs at Accounting cadence for *every* faction over *every* settlement. Every rival
  candidate produces churn only when its event fires.
- **Dependency — and this is binding, not advisory.** Without income, *every Wealth-denominated cost
  terminates in a clamp no-op*. `Faction.adjust` floors at 0.5, so a depleted faction musters for free.
- **External warrant** — it is the corpus's own #1 (`HANDOFF_SE.md:130-136`, "the single highest-priority
  open item in this entire thread"). *Precision:* that item is the broader L/PS wiring, of which income is
  one part.
**Open before building:** the M multiplier fork (ED-SE-0045, ×10 vs ×50).

### 2. THE CONQUEST FORK AT SETTLEMENT GRAIN — paired with Accord-write reconciliation
The first genuine faction-decision→settlement write; L's first mechanical site; the seed constant already
exists (`faction_action.py:489`).
**Two dents, both fair:** its "the ONLY strategic event that already fires" is a frequency claim with **no
instrument** behind it (§0.1 point 4) — parliamentary transfer and mass seizure also write control. And it
covers **one of four** control/accord writers; the critic found a fourth every lens missed — Crown
Initiative's Royal Progress (`crown_initiative.py:102`). Must land **with** the Accord-write
reconciliation (OI-37), or three writers keep bypassing the hinge it exists to unbrick.

### 3. DECLARE `scene_outcome` AT ONE PRODUCER
Near-zero effort; flips the whole dormant person→territory→faction loop live. **Independently
rediscovered by two lenses** — the rediscovery-ranking signal the harness exists to reward.

### 4. `scene.battle_concluded` CONSUMERS — *after* a roster reconciliation
**The most overclaimed nomination in the set.** "Zero new modelling" is false three ways: declared
consumers have **no rule content**; the substrate's write semantics are gated on deliberately-open forks
(ORD-3/OF-3/D.6); and **the two authoritative consumer rosters disagree** — the registry says
`faction_layer, npc_behavior, articulation, conviction_track`; `key_graph.json` says `articulation_layer,
faction_state, npc_behavior, piety_track`. You cannot wire "the" consumers until that is settled.

### 5. THE DERIVATION-CROSSING RULE — rule it, don't build it first
Right architecture, wrong urgency. Largely **pre-existing** as armature §3's g_* gate vocabulary and its
PR-2 keying wave; the contribution is generalizing case-by-case types into one rule. **One requirement the
proposal omitted:** emission must be *edge-triggered with band hysteresis*, or a value oscillating on a
gate boundary emits every tick.

### Ranked separately: three items EVERY causal lens missed
- **The revolt step.** One missing write (`owner = None` at Accord 0) starves an implemented, seasonally-
  invoked emergent subsystem. Plausibly the cheapest edge in the corpus. *Caveat: whether any live path
  can drive Accord to 0 is unverified — if not, the starvation moves up a level.*
- **`process_treaty_expirations`** — implemented, zero callers. One season-loop call buys the only
  diplomacy churn on offer.
- **The vacuous Turmoil victory leg.** Until fixed, *any churn programme silently mis-scores its own
  campaigns.* It belongs **ahead of** new edges.

---

## §2 · Stability — what would break

**Casualty writeback before the fiscal edge is actively destabilizing.** Losers cannot rebuild (the muster
pool reads `Mil + floor(W/2)` with W a verified non-renewing stock), the mil-advantage multiplier steers
the stronger side toward more conquest, and the canonical occupier damper (Treasury → Wealth) dies in the
same clamp. **Build writeback first and the sim degenerates to first-mover extermination.** The ordering
is a hard prerequisite, not a preference.

**Genuinely damped, verified:** the Mandate↔settlement L/PS loop (explicitly stabilizing, sim-verified
bounded over 30 seasons *under the current Weight model*); the war→MS→PT→CI cascade (Calamity Drift caps,
±2/territory/season Thread-source cap, and the Rendering-Crisis counter-oscillation).

**Over-damped:** loyalty-retarded migration, unless paired with an L-erosion term under sustained
unrelieved Dearth. Hirschman's loyalty postpones exit *to give voice a chance*; if voice keeps failing,
loyalty must decay — otherwise the one damper misgovernance cannot argue with is suppressed outright.

**Destabilizing, with a sign flip nobody saw:** a *conserved* population tier. Under conservation, moving
one unit from a low-acceptance to a high-acceptance settlement **raises** `T` — so misgovernance-driven
emigration into your own better-run city *increases* your Mandate. Conservation de-fangs the exact
punishment §1.8c exists to deliver. It also invalidates the K=6 Stage-4 calibration — *the same defect the
proposing lens correctly condemned in `lps_wiring_v1.md`'s divergent Weight table.*

---

## §3 · Double-counting (D.6 is verified open, HIGH priority)

1. **Mandate counts one battle twice — a canon-internal contradiction.** `mass_battle_v30.md:688` writes
   "Mandate −1 (structural)" *directly*, while `settlement_layer_v30.md:165-166` defines Mandate as a
   **pure derived aggregate** `clamp(round(7·T/(T+K)))`. (§6.3's ransom-refusal rule writes Mandate −1
   directly too.) Any proposal routing battle losses through settlement Weight adds the derived path *on
   top of* the direct write. **No lens flagged this instance.**
2. **One conquest at three grains** — faction, territory and settlement, unless the settlement fork lands
   *with* the Accord reconciliation. Canon already owns the discipline to copy: §1.8b's "a single control
   event resolves under exactly one of the two rules."
3. **Casualties charged to two settlements** — one lens charges the muster-source, another the host.
   Convergent channel, divergent target; needs one owner.
4. **Migrants counted twice** — conservation must *replace* §1.8c's "+0.5 Prosperity-growth season", not
   join it.

---

## §4 · The Keys verdict

**The substrate carries actor-scale social churn well and world churn badly**, failing at four joints:

- **No schema-native write path for place/institution state.** `stat_deltas` has **no applier anywhere**;
  §4.1 steps 3-4 are unimplemented by ruling. Both live emit sites duplicate the delta into a closure and
  apply the *captured copy*. Every effect rides a per-emit-site closure — the "no private channel" rule
  eroding in miniature.
- **Derivations are invisible to `causes[]`.** *"Derive, never write" and causal legibility are both
  canonical and in direct conflict at exactly the aggregation joints a churning world runs on.* Mandate
  falls because an aggregate recomputes; no Key is emitted; `walk_backward` terminates at every scale
  boundary. **Neither spec names this conflict.**
- **The roster is jointed by emitting subsystem, not by causal joint.** One joint (settlement control
  change) spans three families. No home at all for: economic flows, settlement stat changes as such,
  L/PS/Mandate movement, governor appointment, **oath/allegiance formation**, migration.
- **Person-scale landing dies in design.** The Scar-trigger matrix is thread-event-keyed only — no row for
  any political fact — and written in a superseded vocabulary.

**Concrete bug, verified by hand:** **six of 55 key types carry registry defaults their own validator
rejects** — three declare `permanence: structural` / `time_horizon: medium` against the enums, one
declares scale `system_meta`, and two carry **raw unparsed YAML comments cooked into the JSON export**
(an export defect as well as a vocabulary one).

**Vocabulary ruling proposed:** store conviction state on the **canonical 13**, derive the 4 axes, never
the reverse. The 13→4 projection is non-invertible — *you cannot wound a projection* — and the registry
already knows it, carrying `conviction` by name in `state.scar_acquired`'s payload.

---

## §5 · The recurring failure mode — found twice, in opposite directions

**A mechanic declared missing without checking the adjacent subsystem where this corpus actually keeps it.**

1. **`mc_v18.py:175-186`** refuses to generate any NPC because "no canon head names an initial world-gen
   population." **`settlement_layer_v30.md:857` is exactly that rule** — Local Actors, count by settlement
   type, ~45–50 across 36 settlements. A scrupulous no-fabrication deferral is blocking **every**
   person-scale edge in the game on a premise that is false one subsystem over.
2. **The captive-pool proposal** asserted ED-898's captured officers are unowned — "no ransom price, no
   prisoner state on any faction card." **`faction_layer_v30.md §6.3` is the owning surface**: 2 Wealth
   per named general (ED-334), Stability −1/season ongoing while unpaid (a line item on the faction card),
   a refusal rule, a 3-season execute-or-hold fork, and its own resolved double-count ruling.

The same error, once by the tree against itself and once by an auditor. **It is the corpus's defining
hazard, and grep is what causes it** — which is why this audit banned lexical evidence, and why the ban
did not fully save it.

---

## §6 · What the adversarial pass changed

**Overturned, in both directions:**
- **There is no live world→person edge at all.** Two lenses labelled the Accord→NPC-worldview link LIVE;
  `generate_npc` has no auto-call and the smoke oracle asserts `npcs_generated == 0` — the repo already
  calls these *"built-but-unreachable islands"*. Correct label: **WIRED-DORMANT**.
- **The council echo is not switched off.** ECHO_TRANSPORT is **default ON**, Jordan-ratified 2026-07-08 —
  "the baseline campaign."
- **The captive-pool proposal is redundant** (§5).
- **The two battle engines are not the same producer** — the canon 28-module engine is never imported from
  `systems/` or `engine/`. Every "unconsumed richness" citation describes an engine that **does not run at
  campaign runtime**. The gap is *wider* than reported.
- **"No battle writes MS" is promoted from ~80% to verified** — but MS has no behavioural reader, so
  writing it alone is a number nothing reads. Pair with the band evaluator or defer.

**Ruling conflict found:** a battle-site shrine drifting Piety upward would convert battles into Church
Influence through the Piety-Yield door — defeating **CLOCK-EDIT-02** (RESOLVED: "Church military victory →
no CI change"), and partially reversing the war-defunds-the-Church cascade the same lens celebrated.

**A required damper nobody had noticed: there is no Scar decay anywhere.** Conviction state only
accumulates. Adding world-fact scars without a symmetric rule converges every long-lived NPC to permanent
crisis. The proposed mirror — **vindication**, where the world confirming a conviction's promise at
genuine stake removes one scar — matches the Knot-reinforcement pattern the corpus already uses.

---

## §7 · Weakest claims, carried forward

Every stability argument in §2 is **reasoned, not simulated** — no seeded campaign was run to measure
conquest frequency, whether `Sta ≤ 2` is ever reached, or whether Accord can reach 0. Per §0.1 point 4
these are hypotheses an instrument should confirm, not measurements. The absence claims ("no Mil writer",
"no MS battle writer") rest on exhaustive greps plus full reads of the owning modules, and **no guard test
pins any of them** — which is precisely what the connectivity instrument in `01_plan.md` T0-4 exists to
fix. Four surfaces neither critic checked remain producer-only and unaudited, not clean.
