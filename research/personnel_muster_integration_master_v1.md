# Valoria — Personnel, Governance and Muster: a phase-ordered integration master

## Status: FILED — reference, not canon (CLAUDE.md §0.05: code is the mechanism, prose is reference)
## Date: 2026-08-27 · Lane: IN (cross-cutting: FA, SE, MB, PC, SC, FI, WR)
## Supersedes nothing. Companion to `research/cross_scale_action_catalogue_v1.md` (the action census).
## Scope: folds one code audit, five design-corpus archaeology passes, five game-precedent passes and
## four muster-precedent passes into a single build plan ordered by the season loop.

---

## 0. How to read this

**This document proposes. It ratifies nothing.** Under ED-1094 a merge normally ratifies PROPOSED
contents; this file is FILED reference and asserts no mechanism of its own, so merging it changes no
status anywhere. Every ruling it identifies is listed in §9 and stays open until Jordan answers it.

**Impact taxonomy.** Every proposal below carries one of four impact classes. They are not severity
grades — they are *what you have to do to land it safely*.

| Class | Meaning | What it costs |
|---|---|---|
| **DOC** | Documentation only. No code, no test, no golden. | An edit and a commit. |
| **INERT** | Code lands but is default-off, unread, or provably non-campaign-reachable. Seeded goldens byte-identical **by construction**. | Review only. |
| **MOVES** | Changes RNG draws or campaign-reachable state. Seeded goldens shift. | Re-pin + a `tools/balance_oracle.py` control (240 campaigns, ~13 min, not a CI gate) to show the shift is not a balance regression. |
| **RULING** | Cannot be built until Jordan decides. | A decision, not a commit. |

**Precedent strength.** Claims from the game research carry a convergence count (how many of the
independent lanes agree) and, where it matters, a sourcing flag. **Sourcing caveat, stated once and
applying throughout:** fan wikis were bot-walled almost everywhere in this research —
`ck3.paradoxwikis.com`, `ck2.paradoxwikis.com` and `forum.paradoxplaza.com` returned 403 to two
independent agents; `koei.fandom.com` and `neoseeker.com` returned 402/403; the Brigandine and
Unicorn Overlord wikis would not load. The load-bearing numbers therefore rest on guide sites, forum
synthesis, `acoup.blog`, and the handful of official manuals that do fetch (Koei Tecmo's Awakening
and RoTK 8 Remake manuals, Total War Academy, the JA2 v1.13 documentation). **Treat every specific
number below as a lead, not a settled fact**, and treat the convergences — which are structural, not
numeric — as the durable findings.

---

## 1. The three findings that reorganise everything

Everything downstream follows from these. Each was verified against primary source in the working
tree, not inferred.

### 1.1 The people already exist

`references/npc_registry.yaml` holds **46 characters — 35 `canonical`, 11 `proposed`** — every one
with a `role` and a `faction`, spanning Crown, Church, Varfell, Hafenmark, Löwenritter, Guilds,
Altonia and the Southernmost Wardens. The schema carries `convictions`, `goals`, `arc_trajectory`,
`territory`, `ts`, `coherence`, `stats`.

**Zero runtime loaders.**

Coverage is uneven in a way that matters: `role`, `faction`, `convictions` and `source` are on
**46/46**; `arc_trajectory` on 36/46; `goals` on 17/46; `territory` on **7/46**; `stats` on **1/46**.

So the roster exists as *identities and offices* and not as *capabilities* — and capability is
precisely the half an assignment check needs. **This is a wiring-and-completion problem, not an
authoring problem.**

### 1.2 Jordan already ruled that personnel is the faction primitive, and it is unexecuted

`systems/settlements/scale_hierarchy_v1.md` §5.1, **RATIFIED** by direct ruling 2026-07-13, verbatim:

> "Factions do not necessarily need to hold territory — they need to hold **PEOPLE**, and it is the
> number of people and the weight of their positions that carry the value of that faction."

The document states its own propagation is unexecuted. A roster system is therefore **the execution
of a standing ruling**, not a feature proposal — which changes what kind of approval it needs.

### 1.3 The cross-scale bridge is already canon

`systems/mass_battle/mass_battle_v30.md:949`, CANONICAL:

> "**Officer as settlement governor:** After a battle, a named officer at Disposition ≥ +2 may be
> assigned as governor of the battle settlement or any garrisoned settlement… The military officer
> transitions to civil administrator — the ROTK post-conquest appointment."

Plus `companion_specification_v30.md:34`: "A single NPC may be both — the officer-governor path
produces exactly this." And `npc_behavior_v30.md §9.5` (PP-642) is a complete recruitment procedure
in which **"Territory governance" is a −2 Ob incentive**.

The loop you would otherwise design is already legislated. What is missing is the object it operates
on.

---

## 2. Cross-cutting: the Person model

### 2.1 Why one object, not a roster subsystem

A person is the only object that appears at **every** scale: a combatant (personal), a governor
(settlement), a commander (mass battle), a councillor or voter (faction), a contest participant
(social). That is why the word "officer" carries **four to seven distinct senses inside ratified
canon** — the collision is *evidence the object is cross-scale*, not evidence of sloppy naming.

The build is therefore **one Person object with two intrinsic facets and three edges**, each scale
*reading* the facet it needs and none redefining it. The edges are the Knots-graph shape the
`rise_to_power` research docket already proposed, so this composes with an existing design rather
than adding a parallel one.

| | Facet | Home | State today |
|---|---|---|---|
| intrinsic | **Identity** — id, name, faction, role, convictions | registry | ✅ 46/46 |
| intrinsic | **Capability** — stats | registry | ⚠️ **1/46** |
| edge → person/faction | **Relation** — Disposition −5..+5 | canon | ⚠️ code duplicates it as `affiliation_loyalty` 0–3 |
| edge → faction | **Attachment** — retainer \| contractor, terms, exit conditions | — | ❌ absent |
| edge → post | **Office** — scale, seat, tenure | — | ❌ absent |

**Scale reads, none of which need a new personnel type:**

| Scale | Reads | Into |
|---|---|---|
| Personal combat | Capability | `resolution_pool` |
| Social contest | Capability + Face; Convictions | pool; adjudicator character weights |
| Fieldwork | Relation | the stepped Disposition Ob table |
| Settlement | Office(governor) + Capability | governance verb pools |
| Mass battle | Office(commander) + Capability | Command |
| Faction | Office(seat) + Relation | vote weight, defection check |

### 2.2 The two design rules the precedent research produced

**Rule 1 — legible inputs, fuzzy thresholds.** Five of five game lanes keep the defection threshold
unpublished while making the inputs visible (Three Kingdoms' Satisfaction, JA2's hidden tolerance
clock, RoTK's LOY≤70 recruiter-side tell, Triangle Strategy's hidden per-character number, CK's
opinion floor under opaque dread interplay). Independently, four of five lanes show that **legibility
is what separates a celebrated system from a resented one** — JA2's social layer is loved and its
tactical math resented *in the same game*, and v1.13's fix **exposed the models rather than changing
them**, shipping an audit tool that itemises every pairwise opinion by source.

For a **no-GM engine** these combine into a hard constraint: *you owe the player the reasons, never
the trigger point.* There is nobody to narrate why a governor defected.

**Rule 2 — JA3, not JA2.** Every lane recommended its own game's full apparatus. Jagged Alliance 3
compressed JA2's five-layer morale stack, ±25 pairwise matrix, event deltas and prejudice axes into
**"liked squadmate present: +1 AP; disliked: −1 AP"** without losing the feel. That is the ambition
ceiling for a d10/TN-7 engine, and the antidote to importing five games' worth of machinery.

### 2.3 Vocabulary, resolved against the collision rather than around it

The Total War lane recommended adopting Three Kingdoms' "Administrator." **Rejected** — it solves the
wrong half. *Governor* is already canonical, already in code (`governor_id`, `succeed_governor()`),
already idiomatic, and carries settlement-residence semantics that TK's Administrator explicitly
lacks (TK administrators are decoupled from physical presence; `npc_relational_graph` derives NPC
residence *from* Governor assignment). The overloaded term is **officer**, not governor.

| Term | Restricted to | Status |
|---|---|---|
| **Officer** | mass-battle unit commander | already built; strip its political senses |
| **Governor** | settlement post | already canonical + in code — keep |
| **Minister / Councillor** | faction post | already in `faction_politics` ministries |
| **Person** | the cross-scale object | the registry |
| **Ascendancy** | the progression system | the research docket's own name; names the arc, not the body |

---

## 3. Phase P0 — World generation and population

### What exists

- `references/npc_registry.yaml` — 46 records (§1.1). No loader.
- `systems/world/sim/npe.py::generate_npc` — a working, territory-conditioned generator. **No
  production call site.**
- `engine/mc_v18.py:194` — a `stubwire.stub_resolve('generate_npc(world-gen|season-tick)')` with an
  honest documented reason: no canon head names a world-gen initial count or a season-tick
  generation trigger, so rather than invent one it generates none.
- `systems/world/sim/npe.py::simulate_npc_actions` — **runs every accounting, over an empty dict.**
- The live NPC models **belief only**: `stance` per issue (1–5), `worldview` convictions,
  `affiliation_faction` + `affiliation_loyalty` (0–3), `hidden_allegiance`, `compromise_category`,
  `volatility` (1–5), `persistent_state`. No name, no attributes, no post, no ambition, no tenure.

### What the precedent says

**Two lanes converged, independently, against the grain of their own subject.**

- **Crusader Kings lane**: do *not* import CK3's population model. Its symptoms are documented —
  roughly 6–7 parentless sixteen-year-olds spawning monthly, late-game saves past ~24,000 characters,
  two community mods pulling in **opposite** directions (cull vs. populate), and Paradox's own fix
  was throttling the tap at the low-value tail (no wives for barons, reduced concubine fertility).
  CK2's model — births plus scripted events, no ambient guest queue — is closer to your scale.
  Verdict: **"generate on demand, not on a clock."**
- **Radiata Stories lane**: 175 NPCs are affordable because each is a config row and the "life" is a
  static 2–3 block schedule — but that schedule is "pure spatial theater" gating fetch-quests, with
  zero connection to persuasion or office-holding. Port the *principle* (cheap row, theater not
  simulation) onto the axes that carry your mechanics — **{territory, faction, issue}** — not
  clock-time. Explicitly invokes §0.1's load-bearing predicate against building the clock version.

### Proposal options

| | Option | What it is | Impact |
|---|---|---|---|
| **A** | **Registry-only** | Load the 35 `canonical` records. No generation at all. The answer to "how many people exist" is "these ones." | **MOVES** (see below) |
| **B** | **Registry + lazy on-demand** | A, plus: when a scene, appointment or resolution needs a person at a territory and none exists, generate one keyed to `{territory, faction, issue}`, seeded deterministically so the same territory reliably yields the same person. | **MOVES** |
| **C** | Ambient population with turnover (CK3 shape) | Population targets, wandering spawns, departure rates. | **Rejected** — both converging lanes argue against it, and it imports the exact complexity that produced CK3's two contradictory community mods. |

**Recommendation: A first, B second, as separate commits.** A answers the blocking question with an
authored answer and is independently verifiable; B is the general rule and can wait until something
actually demands a person the registry doesn't supply.

### Impact analysis

**This is the one place in the whole plan with a measured, non-obvious hazard.** Loading even **two**
NPCs flips the seed-42 campaign winner, because `simulate_npc_actions` runs every accounting and
draws `rng.randint(1,6)` per eligible pair from the **shared** `world.rng`. Any population at all
re-phases every downstream draw in the campaign.

**Therefore the RNG substream is not step one of the roster work — it is a precondition of it**, and
it must land and be proven byte-inert *before* any loader.

### Required coding

**P0.1 — RNG substream (INERT, and the gate on everything else).**
- `systems/world/sim/npe.py::simulate_npc_actions` — replace `rng = world.rng` with a dedicated
  substream derived deterministically from the campaign seed, e.g. a module-level
  `random.Random(world_seed ^ NPC_DRIFT_SALT)` stashed on `world` at creation the way
  `world.echo_scheduler`'s presence-flag pattern already works.
- Falsifier (§0.1 pt 3): a test asserting `test_mc_v18_regression` and `test_f7_smoke_oracle`
  goldens are **byte-identical** across the change with an empty NPC store, *and* that they remain
  byte-identical with a two-NPC store — the second assertion is the one that proves the substream
  did its job. Without it this change is unfalsifiable.
- Impact: **INERT by construction** with an empty store; the whole point is that it stays inert once
  the store is populated.

**P0.2 — Registry loader (MOVES only via P0.1's absence; INERT once P0.1 lands).**
- New `systems/world/sim/npc_roster.py` — `load_registry(world, *, canonical_only=True)` reading
  `references/npc_registry.yaml`, constructing `NPC` records keyed into `world.npcs` by
  `territory` where present.
- Declare the seam: add a `composition_roles` row (`npc_roster_loader`) in
  `references/module_contracts.yaml`, then regenerate `engine/engine_params/composition.json` via
  `tools/export_composition.py` and run its blocking `--check`. Do **not** import across the seam —
  `engine/substrate/composition.py::require('npc_roster_loader')` is the call shape.
- `engine/mc_v18.py` — replace the `stub_resolve('generate_npc(world-gen|season-tick)')` call with
  the loader call, and **update the stubwire reason text** rather than deleting it silently, since
  `engine/tests/test_pipeline_reach.py` carries a strict xfail against that site.
- **The 7/46 territory-coverage gap is the practical blocker**: 39 records have no `territory`, so
  they cannot be keyed into a territory-indexed store. Either extend the registry (authoring) or key
  unplaced records to their faction's seat as a documented default.

**P0.3 — Capability completion (DOC + data).**
- `stats` is on 1/46. Every assignment, appointment and governance check reads Capability. Fill it,
  or every downstream mechanic falls back to a default and the roster does no work.
- This is authoring, not coding, and it is the single highest-leverage non-code task in the plan.

---

## 4. Phase P1 — Season tick, needs, and the Slate

### What exists

- `engine/autoload/engine_clock.py::run_tick` — three phases, one owner:
  `season_tick → action → accounting_boundary` (ED-IN-0199, live 2026-08-27).
- `engine/autoload/scene_slate.py` — a priority queue. `queue_scene` / `next_scene` / `pending_count`.
- `engine/cross_scale/scene_dispatch.py::evaluate_triggers` — fires **exactly one** canonical
  trigger: Stability Crisis (`Faction.Sta ≤ 2` → emergency-council contest). The other seven §4.3.2
  mandatory triggers are **reported as deferred, not faked**, because the aggregate World lacks the
  schema.
- `player_agency_v30 §6.1` — scene budget 3–5 per season by difficulty, against 4–9 slate
  opportunities. "The game's tension scales with the gap between opportunities and actions."

### What the precedent says

**Every game punishes idleness** (4/5 lanes): JA2 docks both merc morale and town loyalty after three
days without offensive action; Three Kingdoms loses satisfaction for idle characters and names "give
them something to do" as the top mitigation; CK's unlanded courtiers leave at a base 2%/month; RoTK
officers want posts. **Valoria has no state that degrades from neglect** — an unassigned person is
inert, not restless.

**Fold the administrative layer into a role the player already wants to use** (4/5 lanes, and it is
Total War's twenty-year arc: classic agents → Rome II's three-type consolidation → Warhammer's
Hero fusion → Three Kingdoms' general-does-assignments). Valoria's Slate doctrine already lands where
that series eventually arrived.

### Proposal options

| | Option | Impact |
|---|---|---|
| **A** | Wire additional §4.3.2 triggers as their schema preconditions become available (each trigger is independent). | **INERT** while the scene phase stays side-effect-free by default |
| **B** | Add an **idleness driver**: a person with no Office and no active Duty accrues a Relation decay or a Grudge tag over N seasons. | **MOVES** once persons exist |

**Recommendation: A opportunistically, B deferred.** B is the mechanic that makes a roster feel
alive, but it is worthless before P0 and dangerous before the Ledger has a person-scoped home (§5.3).

### Required coding

- `scene_dispatch.evaluate_triggers` — one branch per newly-evaluable trigger; keep the
  `deferred` reporting for the rest. **Do not fake a trigger whose schema is absent** — the current
  honest-deferral pattern is the right one and is what makes the module trustworthy.
- Each trigger needs its world-state predicate to actually exist; that is schema work in
  `game_state`/`registry`, not dispatch work.

---

## 5. Phase P2 — The Directive (Provincial Authority → Governor)

### What exists

**Design only.** `governance_play_redesign_v1.md §1.4` specifies one Directive per season, typed
**Extract · Tax · Suppress · Install · Host · Cede**, with three responses:

| Response | Cost | Up-tier | Down-tier |
|---|---|---|---|
| Comply | — | faction Standing +, trust + | usually strains the settlement |
| Bargain | social contest vs PA, you as petitioner | soften terms; mild suspicion | partial strain |
| Defy / Divert | — | Standing-debt, **suspicion +1**; at threshold → recall, audit, replacement | Local-Actor Disposition +, PS + |

In code: `Settlement.active_directive: str | None` exists with **zero readers**. `Settlement.suspicion`
exists with one non-defining reference.

### What the precedent says

**Crusader Kings supplies a fourth response Valoria lacks.** Its special duchy-or-higher contract
roles *trade one kind of extraction for another* rather than offering more-or-less of the same:

| Role | Terms |
|---|---|
| **Scutage** | +50% tax, −75% levy, −20% troop maintenance — buying out of military service with money |
| **March** | −50% tax, +20% levy/garrison — a militarised frontier, cheap in cash, expensive in autonomy |
| **Palatinate** | −20% tax *and* levy, prestige to both parties — autonomy bought with reduced extraction, compensated in reputation |

CK also rate-limits the whole surface deliberately: **one "tyrannical" contract change outstanding at
a time**, escalating opinion costs (−15 then −25 for successive increases against +5 then +10 for
decreases), and a per-vassal frequency cap. Paradox built those caps *as an anti-micromanagement
guardrail* rather than trusting players to self-regulate.

### Proposal options

| | Option | Impact |
|---|---|---|
| **A** | Three responses as designed (Comply / Bargain / Defy). | **INERT** until a Directive generator exists |
| **B** | A + **Commute** — a fourth response trading extraction types along the Scutage/March/Palatinate axis, available only where the settlement's own state supports it. | **INERT**, then **MOVES** at wiring |
| **C** | B + CK's frequency cap and escalating price on repeated Directives against the same settlement. | as B |

**Recommendation: B, with C's frequency cap included from the start.** The cap is cheaper to build
now than to retrofit, and it is the mechanism that stops the Directive loop from becoming the
per-turn busywork every precedent lane warned about.

### Required coding

- `systems/settlements/sim/directive.py` (new): the Directive type enum, a generator reading faction
  priority + settlement state, and a response resolver. Bargain routes to the existing contest
  resolver via `composition.require('scene_resolver.contest')` — **do not re-implement a contest**.
- `Settlement.active_directive` gains its first reader; `Settlement.suspicion` gains its first
  writer.
- Commute needs a durable per-settlement terms record — that is the **Compact** tag family (§5.3),
  so P2-B depends on the ledger reconciliation below.

---

## 6. Phase P3 — Faction action, and the muster problem

This is the largest section because it holds both the built surface and the three-way contradiction.

### 6.1 What exists

`faction_take_action` selects one action per faction per season from four state-weighted buckets:

```
w_unique   = 0.30
w_conquest = 0.35 × (1 + 0.5·has_target + 0.5·mil_advantage)
w_muster   = 0.20 × (1 + threat_signal)
w_govern   = 0.15 × (1 + undergoverned_share)      → renormalise, one rng.random() draw
```

Grounding: Levy 1983, Blainey 1973, Olson 1993 (ED-FA-0012). Signals consume no RNG. **8 of 16
faction-unique actions execute; 8 are typed no-ops.** Varfell and Hafenmark have no working unique
action and reach the board only through the Censure fallback.

### 6.2 The three incompatible muster models

| | Where | Model |
|---|---|---|
| **A** | `faction_action._try_muster` (code) | pool = `Mil + floor(W/2)`, **Ob 1**, `W −1` up front always; Overwhelming `Mil +5`, Success `Mil +3`. **Raises the Military stat.** |
| **B** | `military_layer_v30 §1.3–1.5` (CANONICAL) | Produces **one unit token** — Size 2 (+1 at Prosperity 4–5, +2 at 6–7), Power = `floor(Mil/2)+1`, Discipline, Type. **Military is a ceiling** Muster reads, not changes. Prosperity gates type; Wealth gates quality on a *separate* roll; Muster-success-with-Wealth-failure **downgrades** to light infantry. |
| **C** | `params_tables.yaml` frozen capture | "Muster (Legionary Inward), **Ob 2**." |

A and B are not two descriptions of one mechanic. In A, mustering *raises* Military; in B, Military
is the fixed ceiling determining what mustering can produce. **Run both and mustering raises the
ceiling on what mustering can produce.** A and C also disagree on the obstacle.

A fourth mismatch: A charges `W −1` on **every** muster, but B's Levy is Ob 1 with **no
prerequisites** and §1.7 exempts levies from Wealth-0 degradation as "conscripts or locally
sustained." **You pay money to raise a unit your own rules say doesn't need money.**

### 6.3 The Wealth-0 contradiction — settled

Two documents, both CANONICAL, both approved 2026-04-17 in the same editorial batch:

- **`faction_layer §5.7`**: at Wealth 0, "**Military −1** at each subsequent Accounting," with a
  re-muster recovery loop grounded in the Habsburg bankruptcies.
- **`military_layer §1.7`**: "This is more specific than the prior simulation's Military −1 at
  Wealth 0. **Military stat itself does not degrade from Wealth shortage** — the faction still has
  officers and doctrine." Instead heavy infantry and cavalry lose Discipline per season; levy and
  light infantry are unaffected.

**§1.7 wins, on two independent grounds.**

*Precedent (4/4 lanes).* No franchise degrades an abstract military-capacity stat on insolvency. The
penalty always lands on concrete formations: Rome II halts replenishment (treasury floors at zero,
never negative), Shogun 2 automatically culls units, Medieval II requires manual disbanding, CK
refuses to field or reinforce unaffordable men-at-arms, KOEI resolves shortfall as desertion, JA2
militia desert when upkeep lapses. *(Correction on the record: I briefed the Total War lane that
Medieval II auto-disbands. It does not — that is Shogun 2. The agent caught the error.)*

*Internal coherence, which is the stronger argument.* §1.3 declares that **money cannot buy past the
Military ceiling**. §5.7 lets money *failure* lower it. That is asymmetric and incoherent — today's
insolvency punishing tomorrow's muster, on a stat explicitly ring-fenced from wealth.

**And it is free to fix.** Verified: **Wealth-0 degradation is implemented nowhere in the tree** —
no `W == 0` branch, no re-muster loop, no Military decrement in `run_accounting`. The contradiction
is documentation-only.

> **Proposal M-1 — strike §5.7's Military −1 clause and its re-muster recovery loop, citing §1.7 as
> the surviving model.** Impact: **DOC.** Zero code, zero tests, zero goldens. This is the cheapest
> correct action available anywhere in this document.

### 6.4 The muster model reconciliation

> **Proposal M-2 — adopt Model B as the single owner; retire A's stat-raising and C's Ob.**

Model B is CANONICAL, is the richer object, and is the one the mass-battle engine can actually
consume (it produces a unit with Size/Power/Discipline/Type). Model A's `Mil +5/+3` is the loop.

**Impact: MOVES, and substantially.** `_try_muster` is one of four buckets drawn every season in
every campaign; changing its Ob, its output, and its effect on `faction.Mil` re-phases campaign
state and every downstream draw. Requires re-pinned `test_mc_v18_regression` and
`test_f7_smoke_oracle` goldens plus a `balance_oracle.py` control at ≥120 campaigns per arm.

**Sequencing note:** this is the highest-impact single change in the document and it should not be
bundled. Land M-1 (free) first, then M-2 alone, then the additions below.

### 6.5 Muster additions, in ascending cost

**M-3 — Accord cost per muster (precedent: 2/4 lanes; sourcing solid).**
JA2's Kerberus channel charges town loyalty **per unit purchased** — 0.1 per regular, 0.15 per
veteran — **globally, not to the receiving sector**, rationalised as "the population is wary of
foreign guns with no ties to the country." RoTK VIII Remake (official manual) drops city public
order on Conscript. **Quality and consent-cost move together** in JA2: veterans cost 50% more
loyalty per head, they do not trade off against each other.

This fits your Redlich/Tilly grounding exactly — impressment and recruitment *are* coercive acts.
Charge Accord per muster, **scaling with the unit's quality tier**.

*Impact: MOVES.* Accord feeds `_undergoverned_share`, which weights the Govern bucket — so this is a
feedback edit, not an isolated cost, and the balance control is mandatory.

**M-4 — a hard Accord floor, narrowly scoped (precedent: 1/4 lanes, but sourced to an official manual).**
RoTK VIII Remake gives two thresholds: below 50 order, conscription capacity drops and soldier income
falls; **below 25 (revolt), conscription is unavailable entirely**. The JA lane warns that a
threshold gate risks double-counting, since Accord already gates governance.

*Both are right, and the resolution is scope.* "A population in open revolt will not hand you
soldiers" is a different claim from "you govern badly here." Set the floor at revolt-adjacent Accord
only, justified by the revolt state. It will rarely fire; the per-muster cost is the live mechanic.

*Impact: MOVES* (a new `_NOOP` path in the bucket dispatch changes fall-through).

**M-5 — sabotage-to-deny-muster (precedent: 1/4, and it is a designed enemy action in RoTK VIII).**
Enemy schemes deliberately lower a rival city's order **to block its recruitment**. Valoria's Intel
and Influence currently have no military use; this gives them one, and it is a natural home for the
unbuilt `Spy (Tribune Outward)` domain action.

*Impact: MOVES.* New faction-unique action; also a candidate content fill for the Varfell slot, which
is one of the two factions with no working unique action.

**M-6 — split Muster into levy and professional (precedent: 4/4; the strongest structural finding).**
Every franchise implements the asymmetry, and CK is explicit: **levies cost zero gold to raise or
hold** — a standing entitlement drawn down, rationed politically (contract %, control, opinion) and
temporally (muster travel time), never economically. Men-at-arms cost gold plus prestige, carry
maintenance **even while unraised**, and maintenance **roughly triples once fielded**. Shogun 2
implements the same split as a *starting-stat delta*: 0-honour ashigaru begin at **−4 morale** with
essentially no building requirements, samurai sit behind building chains.

JA2 prices its two channels so the bought option is **strictly worse on economics and wins only on
speed**: ~$75/head to train green militia against $440/head for bought regulars, **2× the daily
upkeep** ($40/$60 vs $20/$30), *plus* the loyalty tax training doesn't carry.

**Your Muster is already the professional model wearing a generic label** (§6.2). ED-FA-0009's
grounding is Wallenstein — a mercenary contractor paid regardless. That is not a feudal levy.

*Impact: MOVES + partially RULING.* Splitting a ratified action is a canon change: ED-FA-0009's
grounding attaches to the whole action, and the levy half would need its own. **You already break
the single-Muster template once** — Knights Templar are raised by Sacred Assembly, Ob 3, no Wealth
roll, cap 2, "not standard Muster" — so the precedent for splitting exists *inside your own canon*.
The question is whether one exception is the right number.

**M-7 — gate troop types on officer CLASS, not biography (precedent: 1/5, and it corrects an earlier
finding of mine).** Your `§1.5` already gates ranged units on "a named officer with Ranged
proficiency" and cavalry on Prosperity ≥6 **or** "a named officer with Cavalry History." I reported
this as unprecedented on the KOEI lane's evidence. **That was wrong.** Total War: Three Kingdoms
gates recruitable unit types by the character's **class** — Strategists unlock ranged and siege, and
"a mixed-archetype army is the intended way to access a full unit roster."

TK's version also fixes the failure mode: gate on a **class**, and losing a person means promoting
another. Gate on *biography* — "the officer with Cavalry History" — and losing one person costs you
cavalry permanently.

*Impact: DOC + RULING-adjacent.* Rewriting §1.5's two gates from biography to class is a canon edit;
it becomes MOVES only when muster consumes personnel, i.e. after P0.

### 6.6 What stays unprecedented, and should be defended rather than justified

- **Military as a *quality* ceiling.** 4/4 franchises cap **quantity** by rank or title (RoTK Class
  → troops per unit; RoTK VI rank → command cap; CK title → 2–5 regiment slots; Rome II Imperium →
  army count). **None caps how good a unit can be** by a faction scalar, and CK explicitly lets
  effectiveness climb open-endedly. Your ceiling encodes faction military culture ("Hafenmark
  Military 3 cannot field Power-4 heavy infantry regardless of Wealth — their training culture tops
  out at Professional"). Keep it as a deliberate statement; do not cite precedent for it. Note also
  Shogun 2's softer counter-model: ashigaru start worse but **can** earn honour, so their gap is a
  floor, not a ceiling.
- **The axis everyone else caps — how many formations you hold at once — you don't bound at all.**
- **A recoverable Wealth-0 model.** Every franchise resolves non-payment as permanent desertion. Both
  of your canonical options are recoverable. Combined with your rule that a destroyed unit loses all
  Experience permanently, permanent desertion would make your army brutally hard to rebuild. Keep
  recoverable — deliberately.

### 6.7 Required coding for P3

- `systems/factions/sim/faction_action.py::_try_muster` — the M-2 rewrite. It must stop writing
  `faction.Mil` and start producing a unit record. **The unit record has no home in `game_state`
  today** (`Faction` has no unit list; `Territory` has only a `garrison` boolean) — so M-2 depends
  on a unit-object schema, which is the real cost and should be priced as such.
- `references/descriptor_registry.yaml` — any new scalar (e.g. a per-faction formation count) must be
  declared in the right domain block (`faction_stats`) and exported via `tools/export_descriptors.py`,
  or `Faction.adjust` will fall through to `UNDECLARED_FLOOR`.
- New faction-unique actions (M-5) follow the existing `_try_*` convention and dispatch from
  `_faction_specific_unique`; the Censure fallback stays as the universal backstop.
- Every change here is golden-moving. Budget one re-pin cycle per landed change, not one for the
  batch — a batched re-pin cannot attribute a shift to its cause.

---

## 7. Phase P4 — Settlement governance

### What exists — and this is the surprise

The **chassis is built and entirely inert.** `systems/settlements/sim/registry.py:55` — `Settlement`
carries `governor_id`, `npc_ids`, `ledger`, `active_directive`, `open_needs`, `deck_state`,
`facility_tier`, `suspicion`, `pressure`, `governor_emergence`, `legitimacy`, `popular_support`, and
an `ap` property implementing `AP = 2 + facility_tier (+1 at Seat/Cathedral)` — which *is*
`governance_play_redesign §1.1`, in code. `ledger.py:30` ships the tag families.
`registry.py:199` has a working `succeed_governor()` that preserves durable tags across a handover —
the player→world persistence guarantee, implemented.

Liveness check:

| Field / function | Non-defining references |
|---|---|
| `governor_id` | **0** |
| `succeed_governor` | **0 callers** |
| `npc_ids`, `active_directive`, `open_needs`, `facility_tier`, `governor_emergence`, `.ap` | **0** |
| `suspicion` / `deck_state` | 1 / 2 |

**The schema is done and nothing reads it.** That inverts the naive build order: the hard modelling
is finished; what is absent is the verb layer that spends AP.

**Two code-vs-canon discrepancies found here:**
1. **Ledger families.** Code ships `{Precedent, Grudge, Debt, Reputation, **Leverage**}`;
   `governance_play_redesign §1.6` names the fifth family **Compact** (ED-SE-0019). Code and canon
   disagree on what the fifth family *is*.
2. **Two Standing ladders in canonical canon.** `settlement_layer §3.2` gates governor eligibility on
   **Counselor / Lieutenant / Successor** — the retired 0–5 titles. `faction_politics` PP-660
   replaced that with 0–7 and different names. **The governor eligibility table points at ranks that
   no longer exist.**

### What the precedent says

- **RoTK's domestic-action table** is the closest template: eight commands, each keyed to one of four
  stats, flat 10 gold per officer — and Commerce, Cultivate and Conscript **all drop Safety**. That
  built-in "every gain costs you elsewhere" shape matches your verbs' method-choice tradeoffs,
  arrived at independently.
- **Total War's governor history is a warning, not a template.** CA added, removed and re-added the
  role three times for three different reasons across twenty years. *"There is no convergent answer
  — this is a real, unsettled design tension, not a solved problem you are behind on."*
- **CK's council-seat denial**, scaled down: a powerful figure passed over accrues a flat −40 opinion.
  You need no Council institution to get the payoff — you need "a named NPC who wanted a post and
  didn't get it accrues a Grudge tag," which is one line in an appointment flow.
- **Medieval II's trait triggers** are the franchise's best-loved character mechanic and map onto
  your tag ledger. The lesson is "**keep the triggers legible**," not "add more tags."

### Proposal options

| | Option | Impact |
|---|---|---|
| **A** | **Minimum viable governor**: one verb (Levy or Keep Order), wired to spend `.ap`, write one ledger tag, and read `governor_id`. | **INERT** — see the reachability note below |
| **B** | A + the full 8-verb menu with method forks. | as A, larger |
| **C** | B + the event deck and NPC ambition engine (the Goldenfurt slice). | large; depends on P0 |

**Recommendation: A, deliberately small.** The value of A is not the verb — it is that it makes
`governor_id`, `.ap`, the ledger and `succeed_governor` *live* for the first time, converting a
declared schema into a running one. Everything else composes onto that.

**Reachability, resolved (do not re-derive this).** Settlements **are** campaign-reachable: `create_world`
calls `composition.require('world_gen_settlements')(world)` at world-gen
(`engine/autoload/game_state.py:351`), populating `world.settlements` from
`systems/settlements/valoria_geography_v30.yaml`, and they are serialised into `final_state`.
`engine/tests/test_pipeline_reach.py::test_world_settlements_populated_after_a_seeded_campaign` is a
STRICT (non-xfail) probe on this.

The population step itself **consumes no RNG** — deterministic by construction, guarded by
`engine/tests/test_world_population.py`, which asserts `world.rng.getstate()` is unchanged across it.
So the precise impact rule for P4 is:

> A governance verb is **INERT** to campaign goldens while its writes stay *settlement-local*
> (`.ap` spend, ledger tags, `suspicion`, `governor_id`). It becomes **MOVES** the moment it draws
> from `world.rng`, or feeds back into territory `Accord` / faction stats through the province
> aggregators (`registry.province_accord`, `registry.province_effective_prosperity`).

Build P4-A on the inert side of that line first — an auto-resolving verb that spends AP and writes a
tag proves the chassis without touching the campaign. Add the roll and the feedback afterwards, as a
separately-attributable golden move.

### Required coding

- `systems/settlements/sim/governance.py` (new): a verb resolver taking `(settlement, verb, method,
  actor, rng)`, spending `.ap`, rolling through the standard kernel, and writing a ledger tag.
- **Reconcile the fifth ledger family** — `ledger.py`'s `TAG_KINDS` vs `§1.6`'s Compact. **DOC + one
  constant.** Pick one; Compact and Leverage are different mechanics (Compact fires every season of
  its term; Leverage is a spent hold), so this may be "add the missing one" rather than "rename."
- **Reconcile the two Standing ladders** — `settlement_layer §3.2` must be rewritten against PP-660's
  0–7. **DOC**, and a prerequisite for any appointment code, which otherwise gates on rank names
  that do not exist.
- First caller for `succeed_governor` — the appointment flow.

---

## 8. Phase P5 — Personal scenes, and the fidelity ladder

### What exists

`auto_manual_resolution_duality_v1.md` — **RULED 2026-07-08**. Three fidelities of one slate event:
**Played** (interactive scene) · **Witnessed** (present, one free Read/Appraise roll at Ob 1, *not*
auto-success, no control) · **Auto** (absent; NPC AI and clock advancement resolve it). Budget 3–5
scene actions per season against more opportunities than actions.

In code: contest scenes resolve live through the promoted kernel. The combat bridge exists behind
`DISPATCH_COMBAT_BRIDGE`, **default OFF, and no trigger anywhere queues a combat scene**. Echo
mapping is deliberately empty except two channels, so **the scene phase is side-effect-free on
strategic state by default** — which is why wiring it cannot regress the strategic loop.

### What the precedent says

The Total War lane's auto-resolve analysis is the most useful thing in the game research, and it
reframes your open calibration question.

- CA **never published a calibration target** in twenty years. The community's two dominant
  complaints are mirror images — "auto-resolve is too punishing" and "auto-resolve doesn't credit my
  army's quality" — and both are the same underlying problem: **auto-resolve collapses a
  multi-dimensional tactical space into a scalar**, so it is systematically wrong for exactly the
  battles that turn on the dimension it dropped.
- **Your Auto tier is an easier problem than TW's**, because in Auto the player made no choices to
  compress. **Your Witnessed tier is the danger case** — present, one light roll — because that is
  structurally closest to the scalar collapse.
- Therefore: **do not tolerance-test the mean.** Test the failure mode. The right question is *"does
  Auto ever produce a result that a player who did play it out would call unrecognisable?"* — a
  distribution-*shape* question, not a distribution-*centre* question.
- And: because your fidelities get used for scenes that may never recur (unlike TW's dozens of
  battles per campaign, whose errors average out or get save-scummed away), err toward **legible,
  coarse-grained and inspectable** — a short list of factors the player can see feeding the roll.
  That is the opposite of what TW shipped and exactly the complaint TW players never stopped making.

### Proposal options

| | Option | Impact |
|---|---|---|
| **A** | Define the Witnessed roll as checking **one or two named axes** the scene actually turned on, not a scalar sum. | **DOC** (a design definition) |
| **B** | A + an inspectable factor list surfaced with the result. | **INERT** then UI |
| **C** | Set the auto/played tolerance as a *shape* criterion, not a mean criterion, and write the falsifier. | **DOC** + a test |

**Recommendation: all three, and C first**, because it is the one that turns a ruled doctrine into a
checkable one. Fork C of ED-SC-0013 (calibration tolerance) is the residual that was explicitly left
open; this is the answer to it.

### Required coding

- A falsifier test comparing Played and Auto outcome **distributions** on seeded repeats of the same
  scene, asserting no unrecognisable-outcome band rather than asserting matched means.
- `scene_dispatch` — the Witnessed branch does not exist yet; it is the third fidelity and only two
  are implemented.

---

## 9. Phase P6 — Resolution

### What exists

Five resolvers at very different completeness — mass battle (31/31 mechanics wired), personal combat
(complete continuous model), social contest (7 moves × 8 proceedings, running), threadwork (7/7
operations), fieldwork (**six typed no-ops; only `knots.py` executes**).

### Two cheap, high-value imports

**R-1 — the pre-vote intelligence gate (Triangle Strategy).** TS gates *which arguments you may
attempt* on information gathered beforehand. **Your investigation lane and your contest resolver do
not touch each other at all.** Investigation output unlocking appeal/ground availability is a link
between two systems you already have, and it directly rewards the legwork a political game should
reward.

*Do not* import TS's hard "wrong appeal = flat fail" gate — that is a special case in a deliberately
continuous system, i.e. scripting drift. **The softer version is already a built primitive:**
`dice_engine.BandExtension`, the ED-SC-0032 injection seam, **may veto an Overwhelming and can do
nothing else**. A mismatched appeal declares a BandExtension; your ceiling drops. In-idiom, zero new
machinery.

*Impact: INERT* (the extension seam is opt-in per subsystem and defaults to None).

**R-2 — two-tier defeat severity (Total War: Three Kingdoms).** A general's death destroys his
retinue **only if the whole army also routs**; partial defeat preserves the formation. Apply it to
units with no personnel layer at all: a unit that loses while the army holds takes Discipline loss
with **Experience intact**; a unit whose army *breaks* takes your harsh "loses all Experience
permanently" rule. That softens your most brutal mechanic in a principled way.

*Impact: MOVES* (mass-battle outcome handling).

**R-3 — proximity-at-rout (Brigandine).** Knights never die; they retreat. What is permanently lost
are the monsters — killed, or **stranded outside the knight's Rune Area when he retreats**. "The
commander is a reusable chassis, the army under him is the consumable." You already have the chassis
half (`§D.2`: officers incapacitated or captured, never killed). Proximity-at-rout determining what
survives is a natural fit for an engine that already models cells, facing and Discipline.

*Impact: MOVES.*

**Garrison (4/4 convergence).** JA2, Brigandine, Unicorn Overlord and Total War all treat
garrison-versus-field as **the same unit pool wearing a different assignment**, never a separately
raised cheaper tier. `Territory.garrison` is currently a boolean written once (on conquest,
`faction_action.py:503`) and read once (`settlement.py:124`, +1 to a derived defence value).

> **Proposal G-1 — make garrison an assignment state on existing units**, with place-assignment
> changing combat resolution (your Defense stat and Fortify verb are already positioned for it) and
> changing loss consequences (Brigandine's shape: garrisoned units lost wholesale if the territory
> falls). **Do not build a garrison troop type.** Open fork: JA2's garrison units can *move*
> offensively, and it is a major feature — decide whether yours can.

*Impact: MOVES, and depends on the unit-object schema (§6.7).*

---

## 10. Phase P7 — Accounting

### What exists

`run_accounting` runs clock advances, insurgency promotion, `simulate_npc_actions` (over an empty
store), and a report-only accord-drift probe. **No Wealth-0 degradation of any kind is implemented.**

### What lands here

- **M-1** (strike §5.7's Military −1) — **DOC**, free, do it first.
- **The §1.7 model, when built**: HI and cavalry lose Discipline per season at Wealth 0; levy and
  light infantry unaffected; Discipline never auto-recovers — retraining costs a Muster action.
  *Impact: MOVES, and depends on the unit schema.*
- **Ledger sweep** already exists (`ledger_sweep` on succession); it needs a season-boundary caller.

---

## 11. Build order, with the dependency that is not optional

```
P0.1  RNG substream ─────────────────┐  (INERT; the gate on everything with people in it)
                                     ▼
M-1   strike §5.7 Military −1  ──► DOC, free, unblocked, do today
LDG   reconcile ledger 5th family ► DOC + one constant
STD   reconcile the two Standing ladders ► DOC, prerequisite for appointments
M-7   officer gates → class not biography ► DOC
                                     │
P0.2  registry loader (canonical-only, 35) ◄─ requires P0.1
P0.3  fill `stats` on the registry (authoring) ◄─ blocks every capability read
                                     │
REL   reconcile Relation: Disposition wins, retire affiliation_loyalty 0–3
OFF   Office as a typed field; first `succeed_governor` caller
                                     │
P4-A  one governance verb, spending .ap, writing one tag
M-2   muster model reconciliation (B wins)  ◄─ needs a unit-object schema
                                     │
M-3/4/5  Accord cost · revolt floor · sabotage-to-deny
G-1   garrison as assignment
R-1/2/3  intelligence gate · two-tier severity · proximity-at-rout
                                     │
M-6   levy/professional split  ◄─ RULING first
P2-B  Directive + Commute
```

**The one non-negotiable edge**: P0.1 before anything that puts a person in the world. Two NPCs flip
the seed-42 winner; skip the substream and you trigger an unargued goldens re-record that nobody can
attribute.

---

## 12. The ruling docket — what only Jordan can answer

Each of these survives all five of CLAUDE.md §0's tests (not superseded, not irrelevant, not answered
by a design document, not answered by precedent, not obviously right for the architecture).

| # | Ruling | Why it is genuinely open |
|---|---|---|
| **R-A** | **The population rule.** How many people exist, where, and when are they created? | This is the stated reason `generate_npc` is stubbed. Two research lanes converged on "generate on demand, not on a clock," and the 35 canonical registry records may already be the answer — but choosing is a design call. |
| **R-B** | **`player_seats_are_contestable`** — can an NPC depose the player from a held rank? | The architecture supports either behind one toggle. Materially different games follow. |
| **R-C** | **Split Muster into levy and professional?** | 4/4 precedent says yes; ED-FA-0009's ratified grounding attaches to the undivided action, so splitting is a canon change, and the levy half needs its own grounding. |
| **R-D** | **ED-FA-0018** — the Crown Administrative examination ladder. | Pre-existing; confirmed by the throughlines analysis as surviving all five tests. |
| **R-E** | **The `score/2` obstacle derivation** (M1 juncture 1, Half B). | Suspended, not neglected: three built sites disagree, and wiring it uniformly would overwrite ratified canon and collapse the Tribunal's two-tier halving. |

**Not on this docket, deliberately**: the Wealth-0 contradiction (§6.3 settles it on precedent plus
internal coherence), the vocabulary split (§2.3 settles it on existing code and canon), and the
garrison question (§9 settles it on 4/4 convergence).

---

## 13. Impact summary

| Proposal | Class | Precedent | Depends on |
|---|---|---|---|
| M-1 strike §5.7 Military −1 | **DOC** | 4/4 + coherence | — |
| Ledger 5th family reconcile | **DOC** | — (internal) | — |
| Standing ladder reconcile | **DOC** | — (internal) | — |
| M-7 officer gate → class | **DOC** | 1/5 (TK) | — |
| P0.1 RNG substream | **INERT** | — (measured hazard) | — |
| P0.2 registry loader | INERT *given P0.1* | 2/5 converged | P0.1 |
| P0.3 fill registry `stats` | data | 5/5 (capability ≠ allegiance) | — |
| REL Disposition reconcile | **MOVES** | 5/5 | P0.2 |
| P4-A one governance verb | **INERT** while settlement-local | 2/5 | OFF |
| R-1 intelligence gate | **INERT** | 1/5 (TS) | — |
| M-3 Accord cost | **MOVES** | 2/4 | M-2 |
| M-4 revolt floor | **MOVES** | 1/4 (official manual) | M-3 |
| M-5 sabotage-to-deny | **MOVES** | 1/4 | — |
| G-1 garrison as assignment | **MOVES** | 4/4 | unit schema |
| R-2 two-tier severity | **MOVES** | 1/5 (TK) | — |
| R-3 proximity-at-rout | **MOVES** | 1/4 (Brigandine) | — |
| M-2 muster model | **MOVES** (largest) | — (internal) | unit schema |
| M-6 levy/professional split | **RULING** → MOVES | 4/4 | R-C |

**Four DOC-class items are free, unblocked, and settle live contradictions. Start there.**

---

## 14. Method and provenance

**Code audited directly** (working tree, this session): `engine/autoload/{game_state,dice_engine,
sigma_leverage,engine_clock,scene_slate,victory}.py` · `engine/cross_scale/{scene_dispatch,
zoom_in_out,combat_bridge}.py` · `engine/mc_v18.py` · `engine/substrate/composition.py` ·
`systems/factions/sim/*.py` · `systems/settlements/sim/{registry,ledger,settlement,infrastructure,
temperaments,adjacency}.py` · `systems/world/sim/npe.py` · `systems/mass_battle/sim/**` ·
`systems/combat/combat_engine_v1/*.py` · `systems/social_contest/sim/contest/*.py` ·
`systems/fieldwork/sim/*.py` · `systems/threadwork/sim/operations.py` ·
`references/{module_contracts,descriptor_registry,npc_registry,id_reservations}.yaml`.

**Design corpus**: five independent read-only passes — `systems/`; `proposals/` + `research/`;
`archives/audit` and `designs/` at `FORK:6311caa8` (2026-06-28, the pre-restructure tree, 819 files
materialised for reading). Method constraint on all five: **no grep, no regex** — navigation by
directory listing and reading, so the pass would surface what nobody remembered was there rather
than only what was already known to look for.

**Game precedent**: nine research passes across Romance of the Three Kingdoms (VI–XIII), Nobunaga's
Ambition (1983, Sphere of Influence, Iron Triangle, Awakening), Crusader Kings II/III, Total War
(Medieval II, Empire, Shogun 2, Rome II, Attila, Warhammer, Three Kingdoms), Jagged Alliance 1/2/
v1.13/3, Brigandine, Unicorn Overlord, Tactics Ogre (SNES/PSP/Reborn), Triangle Strategy and Radiata
Stories — five on personnel, four on mustering.

**Corrections made to this session's own earlier findings**, recorded so they are not re-derived:
(1) the catalogue's "no personnel object exists" was wrong — the registry, `governor_id` and
`succeed_governor` all exist; (2) the KOEI lane's "4+1 stat invariant" is contradicted by its own
fetched sources; (3) "officer-gating is unprecedented" was wrong — Three Kingdoms does it by class;
(4) "Medieval II auto-disbands on bankruptcy" was my briefing error, corrected by the agent — that
is Shogun 2; (5) "widen loyalty to 0–100" was the wrong idiom — the tree's answer is Disposition
−5..+5, which canon already uses for exactly this; (6) an earlier draft of this document left
settlement campaign-reachability as an open "verify" — it is resolved above, settlements ARE
populated at world-gen through a declared composition role.
