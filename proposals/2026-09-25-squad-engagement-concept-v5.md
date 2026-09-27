# Squad Engagement Engine — Concept Proposal v5

**Status:** CONCEPT · non-canonical · not bootstrapped · 2026-09-23 · supersedes v4 (self-contained; no earlier version needed)
**Grounding:** the project docs `valoria_authoritative_map_v1.md`, `valoria_authoritative_graph_v1.md` and `valoria-resolution-diagnostic-SKILL.md`, and the adversarial critique `claude/squad_engagement_critique_v4.md` (2026-09-22). These are derived summaries and a review, not canon. GitHub canon was not read for v4 or for v5. The `[READ: map_v1]` and `[READ: graph_v1]` tags are carried forward from v4 and were not re-read for this revision. Every canon value must be re-verified against `mass_battle` and `combat_engine_v1` before commit.

**Jordan directives (structural, taken as given):**
- **a.** FM and Total War inform the overall formation. FM informs subunit roles the way it informs a player's role. A subunit's shape is formation arrangement at a smaller scale.
- **b.** The Mass pool is retired. Everything is built bottom-up from **the number and quality of troops per cell**, modulated by **morale, momentum, pressure and command**.
- **c.** The player must be able to **route paths** (envelopment), make **strategic manoeuvres** (feigned retreats, delay), and give **conditional instructions**.
- **d. (2026-09-23)** Rulings on the four decisions the v4 critique raised, recorded verbatim:
  1. Faction state sets the morale baseline.
  2. Bounded random variance is allowed under GD-2.
  3. The player character is a commander who can duel.
  4. "Channellers" are not a thing.

**Propagation required.**

Directive b (retiring the Mass pool `min(Size,Cmd)+Cmd`) touches:
- the `mass_battle` doc;
- the value taxonomy in `authoritative_map_v1` §3/§4;
- the resolution-diagnostic's worked example ("Size = Command…");
- the §3.8 Scene→Mass handoff name, and any other handoff named for the Mass pool;
- any other doc citing the formula.

Directive d touches:
- **d.1:** the muster procedure and season accounting on the strategic layer (§10.2);
- **d.2:** the text of GD-2, which should record that bounded, seeded timing variance is permitted (§6.4);
- **d.3:** the character layer's account of the player character in battle, and the §3.7 Mass→Personal handoff (§6.6);
- **d.4:** any doc that places Channellers in mass battle.

Directives b and d each need a ledger entry.

---

## 0. Thesis

A battle is built from **cells** (troop count N and quality Q), which are modulated by **morale, momentum, pressure and command**. Cells are arranged by **one formation grammar at two scales**. They are driven by **one rule mechanism in two channels**: plans move squads, and standing rules decide how cells fight. A **plan** is that rule mechanism laid along a route.

| The player… | …by | Sources |
|---|---|---|
| **Keeps** | Doctrine saved on squads and armies and carried between battles; a library of plan templates | FM saved tactics · Unicorn Overlord per-unit tactics |
| **Arranges** | Formations at army and squad scale; roles by position | FM · Total War |
| **Plans** | Routes with waypoints; each step gated by a condition | Door Kickers go-codes · Combat Mission waypoints · Frozen Synapse · historical signal-drilled manoeuvre |
| **Writes** | Standing rules (condition → action) that govern engagement | Unicorn Overlord |
| **Commands** | One regenerating command budget, spent from the general's position on what the general can see | Historical command · *Scourge of War* · *Ultimate General* |

The engine does five things each tick: **evaluate** both channels, **move** squads along plans, **resolve** contact bottom-up, **advance** morale and momentum, and **check** for breaks at cell, squad and army scale. Envelopment, feigned retreat, delaying actions and ambush are **not special rules**. Each is a plan built from the same parts, and it succeeds or fails through the same four modulators. A battle starts from saved doctrine and ends in outputs the campaign keeps (§10.3).

---

## 1. The formation grammar (two scales)

| | **Army scale** | **Squad scale** |
|---|---|---|
| Occupant of a position | Squad | Cell (troops of one kind) |
| Fighting shapes | e.g. line-and-reserve, refused flank, crescent, hammer-and-anvil `[PLACEHOLDER set]` | Line, wedge, square, loose `[PLACEHOLDER set]` |
| Marching shape | Order of march (squads in sequence along a route) | Column |
| Roles a position admits (FM: a position admits certain player roles) | Squad roles, e.g. Anvil, Hammer, Screen, Reserve, Flank Guard `[PLACEHOLDER names]` | Cell roles, e.g. Shieldbearers, Pike, Skirmishers, Shock, Archers, Crossbows `[PLACEHOLDER names]` |
| What a role holds | Plan-channel defaults and a squad instinct (§4.5) | Engagement rules and a cell instinct (§4.5) |
| Instructions (FM team instructions) | Press, hold, envelop, refuse, pursue / don't pursue | Hold shape, give ground when pressed, close gaps or keep intervals |

- **A role is a preset rule list**, as in FM, and a duty (Defend / Support / Attack) is a variant of it. The first rule of the preset is the role's **instinct**: what it does when it is not in hand (§3.3, §4.5). The instinct is printed on the role card.
- **Position constrains role:** archers are not allowed in a front-line position.
- **Stances are squad shapes.** Shield wall is a line whose front positions admit Guard-heavy roles.
- **A shape change at either scale is reforming.** Reforming is a pressure condition (§3.3) and takes time that grows with depth (§7.2).
- **A column moves fast and fights badly. A line fights well and moves slowly.** The grammar carries the classic manoeuvre trade-off (§5). Both the marching and the fighting shape are part of squad doctrine (§4.6).
- **Close gaps or keep intervals** is a real choice. Closing gaps keeps frontage when N falls; keeping intervals of one cell-width or more stops rout contagion (§3.1).

---

## 2. The cell

| Quantity | Kind | Definition |
|---|---|---|
| **N** | Continuous resource | Troops present. Integer; changes only by rounded, clamped casualties (§8.2). |
| **Q** | Base-parameter profile | Troop type × grade (green / trained / veteran / elite `[PLACEHOLDER]`). The type supplies attack profile, defence profile, reach, speed, **brace** (§3.2) and, for missile types, **firing ranks, range and volleys** (§8.3) `[PLACEHOLDER values: J-10]`. The grade supplies the Steadiness base (§3.3) and the morale clock length (§3.1). |

A cell also carries state: morale clock position, momentum, control state (in hand / on instinct), and volleys remaining for missile types.

**N has two uses, one job each, and depth has a price:**
- **Engaged N** drives **output**.
  - Melee: `min(N, frontage × fighting ranks for the type's reach)`. Anchors: the phalanx's first five sarissa ranks; the Roman acies.
  - Missile: `min(N, frontage × firing ranks for the type)` (§8.3).
- **Depth N** = `N − engaged N`. Its benefit is **morale resilience**: it lengthens the morale clock (§3.1). Anchor: Leuctra's deep column. Its costs are that dense formations take more missile casualties (§8.3) and reform more slowly (§7.2). Anchor: Carrhae, where the deep Roman square absorbed Parthian arrows.

**No cell has an officer record.** A cell's Steadiness comes from its grade, its squad leader and any attached character (§3.3, §3.4).

**Named characters** attach to a cell. They add a Steadiness modifier to that cell and add to Q where their prowess matters `[PLACEHOLDER]`. A named character who holds a squad leader's or the general's post supplies Cmd to that post (§3.4). Named characters reach the personal scale only through the canon §3.7 Mass→Personal handoff `[READ: graph_v1]`, by duel (§6.6). This adds no new down-channel and is independent of J-1.

---

## 3. The four modulators (one job each)

### 3.1 Morale: cohesion

**What it is.** A per-cell canon Morale clock: a discrete accumulator, exempt from diagnostic Lessons 2 and 6. One time unit applies throughout: the **tick**.

**Clock length and starting position.**
- **Length** L (steps to rout) = grade base `[PLACEHOLDER: green 4 / trained 5 / veteran 6 / elite 7]` + depth bonus (+1 per `[PLACEHOLDER: 2]` full ranks of depth N behind the fighting ranks, maximum +2 `[PLACEHOLDER]`). `[ASSUMPTION: v4's "resisted by depth N and grade" is made a rule by lengthening the clock — basis: Leuctra's deep column; Total War experience ranks raising morale]`
- **Starting position** s₀ is written onto the cell at muster from faction Stability (directive d.1; §10.2). A cell from an unstable faction starts some steps along its clock.
- The cell **routs** when its position reaches L.
- **Bands** `[PLACEHOLDER: steady / shaken / wavering, as fractions of L]` set cohesion, which scales output (§8.2). The lowest band is a pressure condition (§3.3).

**What advances the clock.**

| Source | Steps | Limit per tick |
|---|---|---|
| **Casualties** | 1 step each time cumulative loss crosses a further x % of the cell's starting N `[PLACEHOLDER x]` | Uncapped |
| Contact on a **flank** face begins | 1 `[PLACEHOLDER]` | Shock cap |
| Contact on the **rear** face begins | 2 `[PLACEHOLDER]` | Shock cap |
| **Charge received** (attacker's net momentum > 0 after brace, §3.2) | 1 `[PLACEHOLDER]` | Shock cap |
| **Leader down** (the squad's leader is lost: the leader's cell routs, or the leader loses a duel) | 1 `[PLACEHOLDER]` | Shock cap |
| **Adjacent rout** (contagion, below) | 1 | Shock cap |

- **Casualty advance** is evaluated on cumulative loss against starting N, so it steps at each x % boundary. The quantization is intended; the clock is discrete.
- **Shock cap.** Shocks (every row except casualties) sum, and at most **2 steps** of shock apply to a cell in one tick. Excess shock is discarded, not carried to the next tick. `[ASSUMPTION: excess is discarded rather than deferred, since deferring rebuilds the stack one tick later — basis: Total War morale shocks act as momentary modifiers, not stored debt]` The rear-contact value of 2 is set so that L4's exception below is reachable. `[ASSUMPTION: rear shock 2, flank shock 1 — basis: Total War's rear-attack morale penalty exceeds its flank penalty]`
- **Declared exception: the rear charge.** In a tick in which a cell receives both a rear contact and a charge, the shock cap for that cell is **3** for that tick only. This is deliberate: it is the Cannae and Gaugamela rear-cavalry blow, and it should be able to break a steady cell. **Safeguard:** a rally order (§6.3) rolls the clock back one step, and the 2-step cap resumes on the next tick.

**What rolls it back.** Only a **rally** order: one step back per rally, never below s₀, and a squad can benefit from rally at most once per `[PLACEHOLDER: 10]` ticks. `[ASSUMPTION: rally floor at s₀ and a cooldown — basis: Total War rally abilities with cooldowns; a rally cannot make troops fresher than they mustered]` Command otherwise acts on control (§3.3), not on morale.

**Rout.** A routed cell:
- leaves its squad's shape and moves away at its run pace along the squad's retreat route, or directly away from the nearest enemy if the squad has none;
- has output 0 and brace 0, and does not strike back;
- counts as **scattered** if it leaves the field or is still routing at battle end (§10.3).

A rally that brings a routed cell's position below L halts the rout. The cell returns to its position in the shape at walk pace (this counts as reforming) and is on instinct until its control state returns (§3.3). Flight, rout and a rallied cell's return are the **only** movements a cell makes independently of its squad (§4.2).

**Contagion, bounded by geometry.** When a cell routs, every cell **adjacent** to it advances one step (a shock, inside the shock cap).
- **Adjacent** means edge-to-edge contact: with a cell of the same squad, or with a cell of another friendly squad where the two squads' footprints touch.
- **A gap of one cell-width or more breaks adjacency.**
- A cell advanced by contagion is **refractory** to further contagion for r ticks (r = 3 `[PLACEHOLDER]`).

**Intent, stated.** A continuous line can be rolled up from a flank, one worn cell at a time: this is historical (Leuthen). A chequerboard or a line-and-reserve formation stops the cascade at the first gap: that is the purpose of the Roman quincunx and of keeping a reserve line. **Formation choice is the safeguard.** Contagion alone cannot rout a fresh cell, because it advances one step at a time and the refractory period spaces the steps; it finishes cells that casualties and shocks have already worn down.

### 3.2 Momentum: impact

**What it is.** A bounded per-cell track, 0 to M_max `[PLACEHOLDER]`.

**Gained:**
- **On contact**, by pace: walk 0, run 1, charge 2 `[PLACEHOLDER]`, times the type's impact factor `[PLACEHOLDER: J-10]`; downhill +1, uphill −1 (§7.1). There is no charge through rough going.
- **By winning an exchange:** +1 `[PLACEHOLDER]`. A cell **wins** an exchange when, in that tick, the casualties it inflicted divided by the casualties it received exceed 1. Inflicting casualties while receiving none is a win; an exchange with no casualties on either side is not.

**Lost:**
- **Stopped:** a cell that does not win its first exchange after contact loses all momentum.
- **The grind:** −1 per tick in contact without a win `[PLACEHOLDER]`.
- **Turning away:** Withdraw or give ground sets momentum to 0.

**Brace.** Each troop type has a **brace** value B `[PLACEHOLDER: J-10]`, high for pikes and braced spears, low or zero for most others.
- Brace applies only on the face the cell fronts, and only if the cell did not move this tick. `[ASSUMPTION: frontal and stationary only — basis: pike blocks were helpless in flank (Cynoscephalae, 197 BC); Total War brace requires a stationary unit facing the charge]`
- On contact, the attacker's **net momentum** = `max(0, M − B)`. Only net momentum multiplies the attacker's output and counts as a charge for the morale shock (§3.1).
- **Excess brace** = `max(0, B − M)`. In the first exchange after contact, the braced cell's output against the attacker is multiplied by `(1 + brace factor(excess brace))` `[PLACEHOLDER factor]`. Charging pikes head-on converts the charge into the attacker's own casualties.
- Brace applies to the first exchange only. It re-arms at the next new contact.
- Anchors: Macedonian and Swiss pike against cavalry; Total War's charge defence.

**Effect.** Net momentum multiplies output (§8.2), triggers the charge shock, and governs pursuit casualties (§8.4).

### 3.3 Pressure: control state

**Pressure** is a weighted sum of adverse conditions on the cell, on the same scale as Steadiness `[PLACEHOLDER weights]`:

| Condition | Weight (example) |
|---|---|
| Contact face changed (flank or rear) | 2 |
| Charged this tick | 2 |
| Leader down | 2 |
| Withdrawing while engaged | 2 |
| Lowest morale band | 1 |
| Adjacent rout this tick | 1 |
| Reforming | 1 |
| Outside the squad leader's span (§3.4) | 1 |
| Pursuing (out of formation) | 1 |

**Steadiness** = grade base (green 2 / trained 3 / veteran 4 / elite 5 `[PLACEHOLDER]`) + squad leader's Cmd contribution `⌊Cmd / 2⌋` `[PLACEHOLDER]` + attached-character modifier `[PLACEHOLDER stat — J-12 / J-33]` + squad familiarity (§10.3). `[ASSUMPTION: the leader contributes half his Cmd, so that one Cmd point never outweighs a grade step — basis: diagnostic Lesson 2 (non-uniform impact); Total War general's aura as a bounded bonus]`

**Control state.** Each cell is either **in hand** or **on instinct**.
- A cell in hand **drops to instinct** when Pressure > Steadiness.
- A cell on instinct **returns to hand** after k consecutive ticks with Pressure ≤ Steadiness (k = 3 `[PLACEHOLDER]`).
- Control state is computed at the end of each tick and applies from the next tick. The hysteresis stops a cell from flickering between states on a single condition.
- **In hand:** the cell follows its engagement channel by precedence (§4.5), and its squad's plan carries it.
- **On instinct:** the cell's engagement channel is its instinct only; hand-written and squad standing rules are ignored. If the cell is the **squad leader's cell**, the whole squad is on instinct (§4.5).
- **Withdrawing cells:** the instinct of any withdrawing cell is flight, whatever its role (stated once, in §4.5).
- Anchors: Total War morale states, which drop and recover with a lag; FM composure under pressure.

**Pressure never changes output.** It changes *which* action happens. **Lateness** (a delay in ticks) now applies only to order transmission (§6.3).

### 3.4 Command: coordination

Command has three holders, one stat (Cmd, where a named character holds the post) and three distinct uses. The UI names each use separately.

| Holder | Source | Supplies | UI name `[PLACEHOLDER]` |
|---|---|---|---|
| **Cell** | Grade (Q); no officer record | Steadiness base (§3.3) | Discipline |
| **Squad leader** | Cmd | Steadiness contribution `⌊Cmd / 2⌋` to every cell of the squad; **span** = 3 + Cmd `[PLACEHOLDER]` cells | Leadership |
| **General** | Cmd | The command budget CP_max = 3 + Cmd (§6.1); the general's cell is where orders originate and what the player sees from (§6.5) | Command |

- **Span of control.** Cells beyond the span, counted outward from the leader's cell by distance, carry the "outside span" pressure condition. `[ASSUMPTION: span counted by distance from the leader's cell — basis: command radius in historical practice; Total War general's aura is a radius]` With squads of 6–9 cells, a Cmd 3 leader holds 6 cells in span. This replaces Symphony of War's leadership cap.
- **Leader Cmd** comes from the named character who holds the post, or from a generic value by grade where no named character does `[PLACEHOLDER — J-9 muster]`.

---

## 4. Rules and plans: two channels

### 4.1 The primitive

A **rule** is `condition → action`, as in Unicorn Overlord. Rules come in two arrangements:

| Arrangement | What it is | Evaluation |
|---|---|---|
| **Plan** | An *ordered* list of steps along a **route**, held by a squad. Each step has the form "when *condition*, do *action*"; the next step begins when the current action completes. A squad can hold several **branches**, alternative plans selected by a go-code or a condition. | The current step is the squad's default behaviour |
| **Standing rules** | An *unordered* set of reactions: cell role preset, cell hand-written rules, squad standing rules | Evaluated every tick; the highest-precedence rule whose condition holds acts |

### 4.2 The two channels

| | **Plan channel** | **Engagement channel** |
|---|---|---|
| Owns | **Movement and posture:** route, pace, shape, facing, pursuit | **Engagement:** what to attack, fire or hold fire, and requests for the three posture actions |
| Scale | Squad | Cell |
| Written as | Plan steps and branches; army instructions | Standing rules |
| Precedence | Current plan step → army instruction (full order §4.5) | Cell hand-written → cell role → squad standing rule (full order §4.5) |

**Channel rules:**
1. **Cells never move independently.** The squad's shape carries them. The only exceptions are flight, rout and a rallied cell's return to its position (§3.1).
2. **A cell engages from where the shape places it.** A melee target must be within the cell's reach; a missile target must be within range and line of sight (§8.3).
3. **An engagement rule may affect posture only through three posture actions:** hold, give ground, reform. A posture action **suspends** the squad's current plan step while the rule's condition holds. When the condition ends, the plan step resumes where it stopped.
4. **Posture conflicts.** If cells of one squad request different posture actions in the same tick, the squad takes the action requested by the cells with the largest total engaged N; a tie goes to hold. `[ASSUMPTION: the engaged front decides the squad's posture — basis: Total War units react as a whole to their main contact; hold is the conservative tie-break]`
5. **Posture actions in role presets carry a condition.** A preset posture action must be gated on contact or own state; only a hand-written rule may issue an unconditional one. `[ASSUMPTION: keeps presets from recreating the L2 stall — basis: Unicorn Overlord tactics are all conditional]`

The plan owns movement, so an ever-true engagement rule such as a skirmisher's "shoot nearest enemy in range" no longer stops the squad's route: the skirmishers shoot from where the moving shape places them. Anchor: Unicorn Overlord, where tactics decide combat and movement is ordered on the map.

### 4.3 Conditions: only what the unit can know

A unit may only condition on what it could plausibly perceive. There are no omniscient triggers.

| Condition family | Examples |
|---|---|
| **Time** | At tick T; after holding for T ticks |
| **Arrival** | This squad reaches waypoint *k* |
| **Own state** | Morale band ≤ *b*; engaged N < *x* % of N; momentum ≥ *m*; engaged / not engaged; volleys ≤ *v* |
| **Observed** (within sight, blocked by terrain §7.1) | Enemy squad sighted or within range; **enemy moving away**; enemy pursuing a friendly squad; enemy engaged with an adjacent friendly squad; friendly squad broken in view |
| **Signal** | Go-code *X* received (§6.2) |

- **Routing and withdrawing are indistinguishable to an observer.** Both appear only as "enemy moving away". There is no "enemy routing" condition. This is what lets a feint draw a pursuit (§5).
- Conditions may be combined with AND / OR, up to `[PLACEHOLDER: 2]` terms. The cap keeps rules readable.

### 4.4 Actions

**Plan channel (squad):**

| Action | Parameters | Notes |
|---|---|---|
| **Move** | To a waypoint; pace (walk / run / charge); shape en route | Charge builds momentum; a column is fast |
| **Hold** | Facing; shape | — |
| **Withdraw** | Along a route; **ordered** or **give ground** | Withdrawal while engaged is a pressure condition (§3.3). Giving ground withdraws only at the pace of contact. |
| **Engage** | Target: nearest / named squad / weakest / flank of X | Moves the squad into contact with the target |
| **Reform** | New shape | Reforming is a pressure condition and takes time (§7.2) |
| **Signal** | Go-code *X* | Free once the code has been defined (§6.2) |
| **Pursue / halt** | — | Pursuit is a pressure condition (out of formation); §8.4 |

**Engagement channel (cell):**

| Action | Parameters | Notes |
|---|---|---|
| **Target** | Nearest / named squad / weakest / a cell on a flank or rear face | Within reach or range from the cell's current position |
| **Fire / hold fire** | — | Missile types only; each firing tick spends one volley (§8.3) |
| **Hold** (posture) | — | Suspends the plan step (§4.2 rule 3) |
| **Give ground** (posture) | — | Suspends the plan step; the squad withdraws at the pace of contact |
| **Reform** (posture) | New shape | Suspends the plan step |

### 4.5 Precedence and instinct

**Engagement channel, per cell, highest first:**
1. The cell is on instinct → its instinct only.
2. Cell hand-written standing rule.
3. Cell role rule.
4. Squad standing rule.

**Plan channel, per squad, highest first:**
1. The squad is broken → withdraw along its retreat route (§8.5).
2. The squad is on instinct → its squad role's instinct.
3. A posture action in force from the engagement channel.
4. The current plan step.
5. The army instruction (it also fills anything the plan step leaves open, such as pursue / don't pursue).

**Instinct rules:**
- **Cell instinct** is the first rule of the cell's role preset.
- **Squad instinct.** A squad is on instinct while its leader's cell is on instinct. Its plan channel then follows the first rule of its squad role preset. `[ASSUMPTION: the squad-scale instinct extends the one-grammar-at-two-scales principle (directive a) and supplies the mechanism by which rash troops pursue without orders — basis: Medieval II Total War units that "may charge without orders"; Rupert's cavalry pursuing off the field at Edgehill (1642)]`
- **The withdrawing-cell rule (role-independent).** The instinct of any withdrawing cell is **flight**. A cell is withdrawing when its squad is executing Withdraw or give ground. A cell in flight routs (§3.1) whatever its clock position.
- **Orders to a squad on instinct** wait until it returns to hand, except rally, which applies on arrival (§6.3).

Example instincts `[PLACEHOLDER set]`:

| Role | Scale | Instinct |
|---|---|---|
| Shieldbearers | Cell | Hold (posture), when engaged |
| Pike | Cell | Target the enemy on the front face; hold (posture), when engaged |
| Skirmishers, Archers, Crossbows | Cell | Target nearest in range |
| Shock | Cell | Target the weakest cell in reach |
| Anvil, Reserve | Squad | Hold |
| Hammer | Squad | Pursue the nearest enemy moving away |
| Screen | Squad | Withdraw along the retreat route |
| Flank Guard | Squad | Hold, facing the nearest threat |

### 4.6 Doctrine, templates and delegation

Doctrine persists. The player does not rebuild an army's behaviour for every battle.

| Layer | Saved on | Contains | Carried between battles |
|---|---|---|---|
| **Squad doctrine** | The squad | Fighting shape, marching shape, cell roles by position, squad instructions, standing rules (cell hand-written and squad) | Yes |
| **Army doctrine** | The army | Army formation, army instructions, squad roles by position | Yes |
| **Plan templates** | A library | Cannae, hammer-and-anvil, feigned flight, refused flank, delaying screen, flank march, ambush `[PLACEHOLDER set]` | Yes; the player may save edited templates |

- **Per battle, the player sets only:** deployment, routes, and the assignment of branches and go-codes, starting from a template.
- **Familiarity** is tied to squad doctrine (§10.3). Changing squad doctrine resets it.
- **Marshal delegation.** Before deployment the player may delegate the battle to a marshal: the AI chooses and adapts a template by the rules in §4.7. The player may review and edit the resulting plan before the battle starts. `[ASSUMPTION: delegation is chosen before deployment and holds for the battle — basis: FM's assistant-manager delegation is set before the match]`
- Anchors: FM saved tactics; Unicorn Overlord's per-unit tactics, which persist between battles.

### 4.7 AI generals

- AI generals select and adapt plan templates through the armature (resolver archetype E) `[verify against canon]`, under the **same doctrine, command-budget and information rules** as the player: they save doctrine, spend CP, and see only through their own general's view (§6.5). `[ASSUMPTION: the AI is bound by the same fog of war — basis: E6 requires the same rules for both sides; Scourge of War AI commanders act on courier information]`
- Adapting means choosing among prepared branches, firing go-codes and spending CP on messenger orders in response to what the AI general sees.
- Printed instincts are exploitable by both sides, which is intended.
- **AI plan quality is a core deliverable, not polish.** Without it the manoeuvre layer has nothing to test it (D9, D14).

---

## 5. Strategic manoeuvres, emergent from the parts

None of these has its own rule. Each is a plan, and each one's risk comes from the modulators.

| Manoeuvre | How it is built | Where it succeeds or fails | Anchor |
|---|---|---|---|
| **Envelopment** | Centre: Hold, then Withdraw (give ground) when engaged. Wings: Move in column along routes around the flanks, reform to line at the last waypoint; "when go-code X is received, Engage the flank of the enemy centre." The general fires X (free) when he sees the wings are in place. | *Time:* the wings must arrive before the centre breaks (§9.1). *Exposure:* wings march in column (fast, weak) and must reform to engage (pressure, time). *Command:* a distant wing is outside signal range and messengers are slow and variable (§6.4), so it depends on its prepared plan and on relayed codes. *Information:* the general fires X only on what he sees or is told (§6.5). *Payoff:* a flank or rear face means pressure and a morale shock on the target; a rear charge can break a steady cell (§3.1). | Cannae (216 BC) |
| **Feigned retreat** | Screen squad: Engage, then "after T ticks, Withdraw (ordered) along route R". Hidden reserve: Hold (concealed), then "when enemy pursuing a friendly squad is observed, OR go-code X, Engage". | *Execution:* each withdrawing cell carries the "withdrawing while engaged" weight. A cell whose Pressure exceeds its Steadiness drops to instinct, and the instinct of a withdrawing cell is flight (§4.5). There is no conversion rule: only cells with a Steadiness margin (grade, leader, familiarity) can feign. *The bait:* the enemy sees only "enemy moving away" (§4.3). It pursues if its plan or army instruction says pursue, or if its squad is on instinct with a pursuit instinct (Hammer). Pursuers carry pursuit pressure and meet the reserve out of shape. *Refusing the bait costs something:* a withdrawing enemy keeps its cohesion and ground, unpursued routed cells can be rallied, and scattered troops return to their faction faster (§10.3). | Hastings (1066); Mongol feigned flight; Carrhae |
| **Delaying action** | Screen: Hold at waypoint 1; "when engaged N < x %, Withdraw (give ground) to waypoint 2"; repeat. | Trades troops and ground for time. Clock length (grade, depth) and Steadiness keep give-ground from turning into flight. | Rearguard doctrine; Thermopylae as the extreme |
| **Timed ambush** | Concealed squad: Hold (concealed) until "tick T, OR go-code X, OR enemy within range", then Move (charge). | Concealment depends on terrain (§7.1). Charging from concealment gives full momentum plus a flank or rear face; against a braced front it fails (§3.2). | Trebia (218 BC); Lake Trasimene |
| **Flank march** | Move in column along a route masked by terrain; reform to line at the final waypoint. | The column is fast and blind to the flank. Chokepoints narrower than the footprint force column and add reforms (§7.2). Reforming at the end is the vulnerable moment, longer for deep formations. | Leuthen (1757) |

**Why this satisfies directive c without new systems.** Routes are a Move parameter. Delay is a Time condition or a give-ground Withdraw. Feints are a Withdraw plus a concealed reserve, and their failure mode falls out of control state. Conditionality is the rule grammar itself. The difficulty of each manoeuvre is decided by N, Q, morale, momentum, pressure and command: the same six quantities that decide a straight fight.

---

## 6. Command: preparation versus improvisation

### 6.1 The command budget

| Rule | Value |
|---|---|
| Maximum | CP_max = 3 + general's Cmd `[PLACEHOLDER]` |
| Start of battle | Full, less 1 CP for each go-code defined pre-battle |
| Regeneration | 1 CP every R ticks `[PLACEHOLDER R]`, up to CP_max |
| Plans, branches, doctrine, standing rules | Free (carried by the unit); their limits are fragility under pressure and the knowledge of whoever wrote them |
| Defining a go-code (pre-battle) | 1 CP from the starting pool |
| Firing a go-code | Free |
| Messenger order | 1 CP |
| Shout (rally, hold, halt pursuit) to a squad within the general's signal range | 0 CP; travels at signal speed |
| Shout beyond signal range | Becomes a messenger order: 1 CP, messenger speed |

- **The trade-off.** Preparation is cheap to transmit but rigid. Improvisation is flexible but slow and limited by CP. A Cmd 1 general has 4 CP: enough for the Cannae template (one go-code and one messenger order) with 2 CP in reserve, and regeneration returns what is spent over the battle.
- **There is no direct control.**
- Anchors: Total War general abilities on cooldowns; the range of historical trumpet and flag signals.

### 6.2 Go-codes

- A **go-code** is a named signal defined pre-battle. Defining it costs 1 CP (§6.1).
- It is **reusable**: it can be fired any number of times. Each firing triggers every branch or plan step conditioned on it in squads that receive it.
- It is fired by the general from the general's cell, or by any squad through a Signal plan step. A squad's Signal action is free once the code exists.
- It **carries within signal range** of its origin `[PLACEHOLDER range]`.
- Any friendly squad that receives it within range **relays it once**, one hop from itself. Each hop adds one signal delay. A chain of squads spaced within signal range therefore carries a code across the field, late in proportion to its length.
- Anchors: Roman *signa*; Mongol signal flags; Door Kickers go-codes.

### 6.3 Messenger orders, shouts and reports

- A **messenger order** is any instruction not prepared in advance: a new plan, branch switch, standing rule or instruction. It costs 1 CP and arrives after the **messenger delay**, proportional to the distance from the general's cell to the squad `[PLACEHOLDER speed]`, with seeded variance (§6.4).
- A **shout** is one of three orders: **rally** (the target squad's cells roll back one morale step, §3.1), **hold**, or **halt pursuit**. Within the general's signal range a shout costs 0 CP and travels at signal speed. Beyond it, it is a messenger order.
- **Orders to a squad on instinct** wait until the squad returns to hand. **Rally** is the exception and applies on arrival. A halt-pursuit order therefore does not stop a squad whose leader's cell is on instinct (§8.4).
- **Rally of a broken squad.** If rallied cells return below the break threshold (§8.5), the squad is no longer broken; this is a deed for a named character who issued the rally or leads the squad (§10.3).
- **Reports.** Every squad sends a report to the general every `[PLACEHOLDER]` ticks and whenever it makes contact, breaks, or sights an enemy squad. Reports cost no CP and travel at messenger delay. `[ASSUMPTION: report cadence and triggers — basis: Scourge of War courier reports; historical dispatch practice]`
- Anchors: courier-borne command; *Scourge of War* couriers `[CONFIDENCE: medium]`.

### 6.4 Friction

Bounded seeded randomness is allowed under GD-2 (directive d.2).
- **What varies:** messenger arrival, signal relay (each hop), and march timing (each route leg of each squad).
- **How:** each nominal delay or leg time is multiplied by `(1 + ε)`, with ε drawn from a Normal distribution truncated to ±20 % `[PLACEHOLDER]`.
- **Replay:** the seed is recorded in the Key log as a pre-battle Key, so a battle replays deterministically.
- **Precedent form:** the canon d+σ resolver archetype `[READ: map_v1, via critique E4]` — a nominal value plus a bounded deviation.
- **Purpose:** a scouted battle cannot be solved in advance, and the classic stories ("the messenger arrived late", "the wing was slow on the march") can happen, within a bound the player can plan around.

### 6.5 The general's view

The player's fog of war is the general's view.
- The player sees what the **general's cell** can see (line of sight per terrain, §7.1, to `[PLACEHOLDER sight range]`), plus what **squad reports** deliver (§6.3).
- A report arrives with the messenger delay from the reporting squad, so distant information is old.
- An enemy squad not currently seen appears as a **ghost** at its last-known position, shape and heading, labelled with the age of the information.
- Go-codes and messenger orders are issued on this information only.
- **The general's position is a trade.** Forward, he sees more, his messengers travel less, and his signal range covers more squads; he is also exposed to contact and to a duel (§6.6), and losing his cell breaks the army (§8.5).
- Anchors: *Ultimate General*; *Scourge of War*.

### 6.6 The player commander

Directive d.3: the player character is a commander who can duel.

**The post.** At deployment the player character takes either the **general's** post or a **squad leader's** post.
- **As general:** the player character's Cmd sets CP_max (§6.1); their cell is where orders originate; their sight defines the player's view (§6.5).
- **As squad leader:** the player character's Cmd sets that squad's span and Steadiness contribution (§3.4). The army's general is an NPC `[PLACEHOLDER: from the faction roster]`, who writes the army plan by marshal delegation (§4.6) and spends the army's CP (§4.7). The player sets their own squad's plan within the assignment the army plan gives it, receives the general's go-codes and orders like any squad, and sees what their own cell sees. `[ASSUMPTION: a subordinate post means commanding one squad inside an AI general's plan — basis: *Scourge of War* lets the player take a subordinate command under AI superiors `[CONFIDENCE: medium]`]`
- In either post, the player character's Steadiness modifier applies to their own cell.

**The duel.** Duels go through the canon §3.7 Mass→Personal handoff `[READ: graph_v1]`.
- **Trigger by contact:** the player character's cell is in contact with an enemy cell that holds a named enemy commander.
- **Trigger by challenge:** a challenge is an Engage order whose target is the cell of a named enemy commander; the duel triggers when contact is made. An enemy commander declines only by keeping out of contact through his own plan. `[ASSUMPTION: a challenge is a targeted Engage, not a separate acceptance mechanic — basis: historical single combats were forced by seeking out the enemy leader (Marcellus and Viridomarus at Clastidium, 222 BC); it keeps one mechanism]`
- **One duel per pair of commanders per battle.** `[ASSUMPTION: prevents repeated triggers from continued contact]`
- **NPC-versus-NPC duels trigger by the same contact rule** and resolve headless through the same §3.7 handoff, so unwatched battles produce deeds too. `[ASSUMPTION: the map lists unpursued S1 personal scenes as "resolve by AI", so a headless personal resolver exists — [READ: map_v1]; a battle with named commanders on both sides that never produces a duel unless the player is present would starve the articulation layer]`
- **Scale transition:** the battle pauses while the personal-scale duel resolves, then resumes with its outcome. `[ASSUMPTION: basis — the project's definition of a smooth mechanic requires the scale left to pause when another scale is called]`
- **Outcome:** a lost duel **routs the loser's cell** (leader down, §3.1). If the loser is a general, the army breaks (§8.5). The duel emits a deed Key for each named participant (§10.3). The loser's personal-scale consequences are settled by the §3.7 handoff, not by this engine.

### 6.7 Tempo

- The battle runs in **real time**, **pausable**, at three speeds `[PLACEHOLDER: 0.5× / 1× / 2×; tick length at 1×]`.
- Orders may be issued while paused. They are dispatched at the paused tick and still travel in game time.
- Shouts are cheap (§6.1), so the player has frequent small interventions; CP is reserved for changes of plan.
- Target battle length: `[PLACEHOLDER ticks]`.

---

## 7. The battlefield: minimal terrain

### 7.1 Terrain properties

Routes require a map. The minimum needed, which Total War also uses:

| Terrain property | Affects |
|---|---|
| **Going** (open / rough / obstacle) | Movement speed; momentum gain (no charge through rough ground) |
| **Slope** | Momentum (downhill +1, uphill −1); engaged-N advantage uphill `[PLACEHOLDER]` |
| **Cover and concealment** (woods, reverse slope, fold) | Line of sight: hides squads from Observed conditions (§4.3), from missile targeting (§8.3) and from the general's view (§6.5); enables ambush |
| **Chokepoints** (fords, bridges, gaps) | Frontage: caps engaged N, the bottom-up reason a few can hold many; force column on squads wider than the gap (§7.2) |

`[OPEN — Jordan decision]` Where battlefield terrain comes from. Candidates are territory and settlement data (Fort, terrain type) or a generated map from territory type. Both need canon.

**Fatigue is deliberately left out.** Long routes already cost time, span-of-control pressure, messenger distance, column exposure and march variance. Add fatigue only if a simulation shows envelopment is too cheap without it.

### 7.2 Moving formations through terrain

- **A squad pathfinds as a single footprint**, the rectangle its current shape occupies.
- **Marching and fighting shape** are both part of squad doctrine (§4.6). A plan step's "shape en route" selects one; changing between them is a **reform**.
- **A chokepoint narrower than the footprint** forces the squad into its marching shape (column). This counts as reforming on entry, and again on exit if the plan step's shape is not column.
- **Reform duration** = base `[PLACEHOLDER ticks]` + `[PLACEHOLDER]` ticks per rank of depth. Deep formations reform more slowly (E5). During a reform the squad carries the reforming pressure condition.

### 7.3 Season and weather

Season and weather set terrain **going** at battle generation `[PLACEHOLDER table: e.g. heavy rain turns open clay to rough; frozen ground turns marsh to open]`. They also set the nightfall cap (§8.5). They have no other battle effect.

---

## 8. Contact and resolution

### 8.1 Geometry

The contact face is the side of a squad an enemy touches. A cell engages if that face lies within its type's reach.
- A flank contact turns side cells into face cells.
- A rear contact means engagement-channel rules do not fire in the first tick of contact; the cell acts on its instinct for that tick. `[ASSUMPTION: v4's rear-contact rule restated in ticks and in the channel model]`
- A square has four faces but little frontage on each.
- At army scale, squad placement determines faces, so an envelopment is shape producing faces.

### 8.2 Melee exchange

On each tick in which a cell is in contact and in reach:

```
output            = engaged N × Q_attack(vs target Q_defence) × cohesion(morale band) × (1 + momentum factor(net momentum))
braced first exchange: the braced cell's output × (1 + brace factor(excess brace))      (§3.2)
expected casualties = output × conversion                                              [PLACEHOLDER, J-10]
realized casualties ~ archetype A, continuous-Normal mode: mean = expected, σ ∝ √(engaged N)
applied casualties  = realized, rounded to the nearest integer, clamped to [0, target N]
```

- **Randomness** comes from two seeded sources: archetype A for casualties `[READ: map_v1]`, and the bounded timing variance of §6.4. Casualty variance shrinks as more troops engage.
- **The combined multiplier** `cohesion × (1 + momentum or brace factor)` is clamped to `[PLACEHOLDER range]`.
- **Winning** the exchange is decided on applied casualties (§3.2).
- **Casualties in exchanges are reported as killed** (killed or disabled). `[ASSUMPTION: one loss type per exchange keeps the Key log simple; wounded-and-recovered modelling is deferred]` Scattered troops come from routs and breaks (§10.3).
- **Forecast:** expected casualties ± 1σ for each projected contact, shown in the preview (§10.5).

### 8.3 Missile exchange

- **Firing ranks** by type: bow 3, crossbow 2, javelin 1 `[PLACEHOLDER]`. **Missile engaged N** = `min(N, frontage × firing ranks)`.
- A missile cell fires at a target within range `[PLACEHOLDER per type]` and line of sight, and only when its squad's pace is hold or walk. `[ASSUMPTION: no fire at run or charge — basis: Total War foot missile units halt to shoot; horse archers `[PLACEHOLDER]` may be the exception (Carrhae)]`
- **Output** = missile engaged N × Q_missile(vs target Q_defence) × cohesion × **density(target)**, where density = target cell's ranks ÷ reference ranks `[PLACEHOLDER reference and clamp]`. Casualties are drawn, rounded and clamped as in §8.2. Deep formations take more missile casualties (E5).
- **Ammunition.** Each missile cell carries volleys `[PLACEHOLDER count]`. Each tick it fires spends one volley. At 0 it cannot use its missile profile; its engagement channel falls back to its melee profile.
- **Resupply** comes only from a **supply cell** `[PLACEHOLDER type]` in contact with the missile cell, at `[PLACEHOLDER]` volleys per tick.
- Missile fire is not a charge and builds no momentum.
- Anchors: Total War ammunition; arrow resupply at Agincourt (1415).

### 8.4 Pursuit

- A squad **pursues** when its plan step, its army instruction or its squad instinct says to, and an enemy moving away is in sight. Its target is the nearest enemy moving away.
- Pursuing cells carry the "pursuing" pressure condition.
- Fleeing and routed cells have output 0 and brace 0. Pursuit casualties are computed as a melee exchange and are killed.
- Pursuit **ends** when no enemy moving away is within the pursuing squad's sight, or when a halt-pursuit order reaches a squad that is in hand.
- A fleeing or routed cell that reaches the field's edge leaves the battle and counts as scattered.

### 8.5 Breaks and the end of battle

Three scales of break, each a rule:

| Scale | Breaks when | Effect |
|---|---|---|
| **Cell** | Its morale clock reaches L (§3.1), or it takes flight (§4.5) | Routs (§3.1) |
| **Squad** | Routed cells hold ≥ 50 % of the squad's starting N, **or** the leader's cell routs | Withdraws along its retreat route, or directly away from the nearest enemy if it has none. Takes no orders except rally. Its remaining cells count as scattered at battle end unless rallied. |
| **Army** | Broken squads hold ≥ 50 % of the army's starting N, **or** the general's cell routs | **The battle ends.** |

- **Measuring "hold".** A cell's share is its starting N, not its current N, so that pursuit killing the routed cannot reverse a break. `[ASSUMPTION: basis — a break is a fact about how much of the formation has gone, not about how many of the fugitives survive]`
- **Un-breaking.** A squad whose routed cells fall below 50 % through rally (§6.3), with its leader's cell not routing, is no longer broken.

**Other ends of battle:**
- **Mutual disengagement:** no contact anywhere for K ticks `[PLACEHOLDER K]`, and no squad executing a Move or Engage step toward the enemy.
- **Nightfall cap:** a tick limit set by season and the time of day the battle begins `[PLACEHOLDER]`.
- At either, the field is held by the side with more unbroken N within the **objective zone** `[PLACEHOLDER: zone definition]`. The other side counts as **withdrawn**, not routed: its cells in unbroken squads are present, and only cells in broken squads or still routing are scattered.
- **After an army break,** the broken army's cells in broken squads and routed cells are scattered; its cells in unbroken squads withdraw in order and are present. `[ASSUMPTION: basis — broken armies historically lost their shattered units but kept formed rearguards]`
- **Winner.** For any canon consequence that needs a winner, the side that did not break, or that holds the field, wins. `[ASSUMPTION: basis — the convention that the side holding the field claims the victory (Malplaquet, 1709)]`
- Anchors: Total War army-wide rout; *Ultimate General* objective-zone timers; pre-modern battles ending at dusk.

---

## 9. Diagnostic pre-screen

| # | Candidate finding | Phase | v4 status | v5 status / safeguard |
|---|---|---|---|---|
| D1 | **Attrition spiral** (Lanchester) | 4 | Deliberate; rout as damper; simulate | **Deliberate, now bounded.** Rout, squad break and army break (§8.5) end the spiral before annihilation. Rate measured by the first simulation (§9.1). |
| D2 | **Momentum loop** | 4 | Decay + cap + clamp | **Safeguarded.** Decay, track cap, clamp, plus brace (§3.2) and a defined win condition. |
| D3 | **Rout contagion** | 4 | "Once per rout, one hop" (misdescribed, critique L5) | **Re-specified.** Bounded by geometry: gaps break adjacency, refractory period r, inside the shock cap (§3.1). Line roll-up is declared intent. |
| D4 | **Pursuit slaughter** | 3b | Deliberate; halt order or go-code | **Deliberate.** Pursuit ends when no enemy moving away is in sight (§8.4); halt pursuit is a 0-CP shout within signal range but waits for a squad on instinct. Pursuit now also decides how many scattered return (§10.3). |
| D5 | **Morale's two expressions** (scaling output and triggering the rout) | 3c | `[INTENT UNDETERMINED]` | **Unchanged: `[INTENT UNDETERMINED]`** until Jordan confirms (§13). |
| D6 | **Small-cell variance** | Lesson 3 | Simulate | **Unchanged: simulate.** Rounding and clamping now specified (§8.2). |
| D7 | **Command at three holders** | 3c | One job per holder | **Resolved** (§3.4): grade, squad leader, general; no officer records; three UI names. |
| D8 | **Feint → real rout conversion** as a threshold cliff | 3b | Deliberate special rule | **Retired as a rule.** The conversion is derived from control state and the withdrawing-cell rule (§4.5). The cliff remains at Pressure > Steadiness; it is legible (weights and Steadiness shown) and damped by hysteresis. |
| D9 | **AI exploitability:** a dominant feint or template | balance | AI writes plans | **Open to simulation.** AI uses the same doctrine, CP and fog rules (§4.7); observers cannot tell a feint from a rout (§4.3). Search for a dominant template. |
| D10 | **Plan fragility compounding across many squads** | 3b | Intended; delay suspends | **Intended.** Instinct suspends only the engagement channel of the affected cell, or the squad's plan channel when its leader's cell is affected; the plan resumes on return to hand. |
| D11 | **Rear-charge shock** (3 steps in one tick) | 3b | — | **New, deliberate** (§3.1). Safeguard: one tick only; rally rolls back one step; 2-step cap resumes. |
| D12 | **Duel decisiveness:** a lost duel by a general breaks the army | 3b | — | **New, deliberate** (§6.6, §8.5). Safeguards: duels need contact; the general's position trades exposure against sight and messenger distance (§6.5); one duel per pair per battle. |
| D13 | **Faction morale loop:** low Stability → worse starting morale → lost battle → lower Stability | 4 | — | **New; simulate at campaign scale.** The Stability → s₀ mapping must be bounded `[PLACEHOLDER]` (§10.2). |
| D14 | **Delegation dominance:** marshal delegation always better or always worse than the player | balance | — | **New; balance.** Tie AI plan quality to the general's character, not a fixed difficulty (§4.7). |
| D15 | **Familiarity lock-in:** never changing doctrine | balance | — | **New, deliberate** (FM trade-off). Bounded by the familiarity cap (§10.3). |

### 9.1 First simulation (E3): snowball against manoeuvre

**Requirement.** For two equal armies (same N, Q, Cmd, doctrine, terrain open, no variance seed advantage), the time for a held centre to break under frontal assault, T_break, must be at least **1.5 × `[PLACEHOLDER]`** the time for a wing to complete a flank march of standard length `[PLACEHOLDER length]`, T_flank:

```
T_break ≥ 1.5 × T_flank
```

- **Tuning levers,** in this order: casualty conversion (§8.2), the morale casualty-advance rate x (§3.1), momentum decay (§3.2).
- **Secondary check.** Envelopment must be viable but not guaranteed: in seeded runs of the Cannae template against an AI general that adapts (§4.7), the envelopment succeeds in fewer than `[PLACEHOLDER %]` of runs. `[ASSUMPTION: a second bound is needed because the primary criterion alone allows a guaranteed envelopment — basis: critique E3 "viable but not guaranteed"]`
- This simulation runs before D1, D6, D9, D13 and D14.

---

## 10. Fit with canon and implementation

### 10.1 Canon hooks

| Canon hook `[READ: map_v1 / graph_v1]` | v5 treatment |
|---|---|
| Mass pool | **Retired** (directive b) |
| TroopCount | = ΣN across cells; losses upward = killed + scattered; scattered return over seasons (§10.3) |
| Levies `Mil×2` | `[OPEN — J-9]` How muster becomes cells (N split, Q assignment). Muster also writes s₀ and grade (§10.2). |
| Morale thresholds (clock) | Held per cell; length from grade and depth; starting position from Stability (§3.1) |
| Archetype A continuous-Normal | Casualty randomness (§8.2) |
| d+σ archetype | Bounded, seeded timing variance (§6.4; directive d.2) |
| §3.7 Mass→Personal (general duel) | The only personal-scale entry; triggers and outcome in §6.6 (directive d.3) |
| §3.8 Scene→Mass | **Pre-battle scenes gain real stakes.** Scouting reveals terrain and enemy deployment (position, shape, heading), which seed the enemy ghosts in the preview (§10.5). It does not reveal enemy plans. `[OPEN]` Whether parley or deception can plant false signals or false ghosts. |
| Battle → MS −1 (−2 War); Stability | Unchanged; the winner is decided per §8.5 |
| Initial conditions + Key log; deterministic replay | **Pre-battle Keys:** doctrine, plans, go-code definitions, the variance seed. **In-battle Keys** carry `causes[]` provenance, used for the turning-points report (§10.5). **Post-battle Keys:** outputs and deeds (§10.3). Aggregated per-contact Keys `[OPEN: J-2]`. |
| BG never pauses (PP-110) | The same engine runs headless. Unwatched sides use AI template selection through the armature, resolver archetype E (§4.7) `[verify against canon]`. |

### 10.2 What a battle takes in

Directive d.1: faction state sets the morale baseline.
- **Delivery at muster.** Muster is a strategic-layer action that creates cells. At muster, faction **Stability** sets each cell's base morale (its starting clock position s₀) `[PLACEHOLDER mapping]`, and `[PLACEHOLDER: which faction stat(s)]` set the grade distribution.
- These values are **written onto the cell** at creation and re-read at each season's accounting.
- The battle engine reads **cell state only**. It never queries faction state, so J-1 is not triggered.
- This is the delivery route chosen for a Jordan-ruled input, not an open question.
- **Season and weather** set terrain going at battle generation (§7.3).
- **Pre-battle scenes** (§3.8) supply scouting information and the general's starting knowledge.

### 10.3 What a battle gives out

| Output | Rule |
|---|---|
| **Killed / scattered / present, per squad** | Killed: exchange and pursuit casualties. Scattered: troops in cells routing or fled at battle end, and in unrallied cells of broken squads (§8.5). Present: the rest. |
| **Return of scattered troops** | Each season a fraction `[PLACEHOLDER rate]` × (1 − p) of the remaining scattered pool returns to its faction, where p is the victor's **pursuit intensity**. Troops not returned after `[PLACEHOLDER]` seasons are lost. |
| **Pursuit intensity p** | p = the victor's unbroken N of fast troop types `[PLACEHOLDER: speed threshold]` in squads with the pursue instruction at battle end, ÷ the loser's scattered N, clamped to [0, 1]. p = 0 if the victor's army instruction at battle end is don't pursue. `[ASSUMPTION: basis — fugitives were cut down or rounded up by fresh cavalry; Napoleon's lack of cavalry after Lützen (1813) left the beaten army intact]` |
| **Grade progress** | Each cell that finishes the battle in hand and in an unbroken squad gains `[PLACEHOLDER]` progress toward its next grade. |
| **Familiarity** | Each squad gains +1 Steadiness for all its cells per battle fought under the same squad doctrine, up to a cap `[PLACEHOLDER]`. A battle counts when the squad was deployed and any contact occurred on the field. Changing squad doctrine (shape, marching shape, roles by position, squad instructions or standing rules) resets familiarity to 0. Replacing losses or reassigning a cell of the same role to the same position is not a change. `[ASSUMPTION: what counts as a doctrine change — basis: FM tactical familiarity attaches to the tactic, not to the players filling it]` |
| **Deeds** | Keys for npc_memory and the articulation layer `[verify against canon]`, emitted for named characters: fought a duel (and its outcome); held under rear contact (their cell stayed in hand for ≥ `[PLACEHOLDER]` ticks while in rear contact); rallied a broken squad (§6.3). |

Anchors: FM player development and tactical familiarity; the historical rally of scattered troops in the weeks after a defeat.

### 10.4 Tick sequence

Each tick runs:
1. **Arrivals:** signals, shouts and messengers arrive (with seeded variance). Rally applies. Queued orders apply to squads now in hand.
2. **Plan channel:** each squad selects its behaviour by plan-channel precedence (§4.5).
3. **Engagement channel:** each cell selects its target and any posture request; posture conflicts are resolved (§4.2); posture actions suspend plan steps.
4. **Movement:** squads move as footprints; flight, rout and rallied-return movement; pursuit.
5. **Contact:** faces assigned; brace set against momentum; first-exchange flags set.
6. **Exchanges:** melee and missile; volleys spent; casualties rounded and clamped; winners decided.
7. **Morale:** casualty advance; shocks within the per-tick cap; routs; contagion with refractory periods.
8. **Momentum** update.
9. **Control state:** Pressure summed, compared with Steadiness, hysteresis applied (takes effect next tick).
10. **Breaks and end:** squad breaks, then army break; mutual disengagement and nightfall checks.
11. **Key log:** events recorded with `causes[]`.

`[OPEN]` This must map onto canon's 7-phase mass-battle tick.

### 10.5 Godot and screens

**Godot.** Pathfinding runs over a terrain grid (Godot's AStarGrid2D fits), with footprint clearance for squad shapes (§7.2). Hundreds of cells resolve only in contact.

**Screens:**
- **Doctrine board.** Saved squad and army doctrine; the template library; the familiarity each squad would lose on a change.
- **Plan board.** Draw routes and waypoints on the map; attach a condition to each step; go-codes are colour-coded; there is a branch tab per squad; a marshal-delegation button.
- **Timeline preview.** Ghost playback of the player's **own** plans at expected speed, with a scrubber and the ±20 % timing band shown on each route leg. **Enemy ghosts** appear only for scouted squads, showing their observed shape and last heading, not their plan. **Per-contact forecasts** (expected casualties ± 1σ) appear only where own routes and enemy ghosts are projected to meet.
- **Formation editor** that zooms between the two scales, with marching and fighting shapes.
- **Rule editor**, split by channel.
- **Cell readout:** N bar (engaged and depth), Q badge (with brace), morale pips (with s₀ and L marked), momentum arrow, control state and instinct tag, Pressure against Steadiness, span pip, volleys.
- **Order panel:** CP and regeneration timer; go-code buttons; shouts with signal-range overlay; messenger orders with an arrival ETA band.
- **General's view:** the fog of war, with ghosts labelled by age (§6.5).
- **Post-battle report.** FM-style ratings, plus **turning points**: the five events with the largest downstream effect, each shown with its cause chain from `causes[]`. Downstream effect = N lost + w × morale steps advanced `[PLACEHOLDER w]` across all later events whose cause chain contains the event. An event already inside a listed event's chain is not listed separately. Anchor: FM post-match analysis.

---

## 11. Resolution crosswalk

| ID | Sev | Resolution | v5 section | Precedent anchor |
|---|---|---|---|---|
| L1 | C | Break at cell, squad (≥ 50 % or leader) and army (≥ 50 % or general) scale; mutual disengagement and nightfall; field held within the objective zone | §8.5 | Total War army-wide rout; *Ultimate General* objective timers; pre-modern battles ending at dusk |
| L2 | C | Two channels: plans own movement and posture (squad); rules own engagement (cell); three posture actions; cells never move independently | §4.2, §4.4, §4.5 | Unicorn Overlord |
| L3 | H | Control state (in hand / on instinct) with weighted Pressure on the Steadiness scale and hysteresis k; lateness only for orders | §3.3 | Total War morale states with recovery lag; FM composure |
| L4 | H | Shock cap of 2 steps per tick; casualty advance uncapped; declared rear-charge exception of 3 with rally safeguard | §3.1 | Total War morale shocks; Cannae and Gaugamela rear cavalry |
| L5 | H | Contagion limited to edge-adjacent cells; gaps break adjacency; refractory period; line roll-up declared | §3.1 | Roman quincunx and reserve lines; Leuthen roll-up |
| L6 | H | No conversion rule: withdrawing cells' instinct is flight; observers see only "enemy moving away"; not pursuing costs cohesion, ground and returns | §4.3, §4.5, §5, §10.3 | Hastings; Mongol feigned flight |
| L7 | M | Firing ranks by type; missile engaged N; volleys; resupply from a supply cell in contact | §8.3 | Total War ammunition; Agincourt resupply |
| L8 | M | Brace per type offsets momentum; excess brace raises the defender's first-exchange output; winning = casualty ratio > 1 | §3.2, §8.2 | Macedonian and Swiss pike; Total War charge defence |
| L9 | M | No cell officers; Steadiness from grade; squad leader Cmd gives contribution and span 3 + Cmd; general gives budget | §3.3, §3.4 | Total War experience ranks; historical span of control |
| L10 | M | CP_max = 3 + Cmd, starts full, regenerates; go-code definition 1 CP, firing free; messengers 1 CP; shouts 0 CP in signal range | §6.1, §6.3 | Total War general abilities on cooldown; historical signal range |
| L11 | L | One unit (tick); casualties rounded and clamped to [0, N]; casualty advance per x % of starting N, cumulative | §3.1, §8.2 | Specification |
| L12 | L | Go-codes defined pre-battle, reusable, carried within signal range, relayed one hop per squad with a delay per hop; Signal free | §6.2 | Roman *signa*; Door Kickers go-codes |
| P1 | C | Squad doctrine, army doctrine and plan templates persist; per battle only deployment, routes and branch assignment; marshal delegation | §4.6 | FM saved tactics; Unicorn Overlord per-unit tactics |
| P2 | C | The player sees the general's view plus delayed reports; ghosts with age; general's position trades exposure for sight and speed | §6.5 | *Ultimate General*; *Scourge of War* |
| P3 | H | Real time, pausable, three speeds; orders issued in pause travel in game time; cheap shouts, CP for plan changes | §6.7, §6.1 | Total War and FM pause and speed control |
| P4 | H | Preview plays own plans; enemy ghosts only for scouted squads (shape, heading, no plan); forecasts only where projected to meet | §10.5, §10.1 (§3.8 row) | Door Kickers; Frozen Synapse |
| P5 | M | Turning-points report: five largest downstream events with cause chains from `causes[]` | §10.5 | FM post-match analysis |
| P6 | M | Squads pathfind as footprints; chokepoints force column; marching and fighting shapes in doctrine; transitions are reforms | §7.2 | Total War column and line movement |
| P7 | L | **Ruled (d.3).** Commander in the general's or a squad leader's post; Cmd, Steadiness and sight by post; duel by contact or challenge through §3.7; lost duel routs the loser's cell | §6.6 | Directive d.3; §3.7 handoff; *Scourge of War* command levels |
| E1 | C | Killed / scattered / present; seasonal return reduced by pursuit intensity; grade progress; familiarity; deeds as Keys | §10.3 | FM player development and tactical familiarity; historical rally of scattered troops |
| E2 | H | **Ruled (d.1).** Stability writes base morale at muster; re-read each season; engine reads cell state only; season and weather set going | §10.2, §7.3 | Directive d.1 |
| E3 | H | First simulation with pass criterion T_break ≥ 1.5 × T_flank, plus a not-guaranteed check | §9.1 | Critique E3 |
| E4 | H | **Ruled (d.2).** ±20 % seeded variance on messengers, relays and march legs; seed in the Key log; replay-deterministic | §6.4 | Directive d.2; canon d+σ archetype |
| E5 | M | Depth costs missile casualties (density) and reform time; ammunition limits massed missiles; pursuit has value | §8.3, §7.2, §10.3 | Carrhae; Total War ammunition |
| E6 | M | AI generals choose and adapt templates through the armature (archetype E) under the same doctrine, CP and fog rules; AI plan quality is a core deliverable | §4.7 | Armature archetype E `[verify against canon]` |
| E7 | L | **Ruled (d.4).** Removed; battle troop types are mundane | §1, §10.1 | Directive d.4 |

---

## 12. Revision history

**v0 → v1**
- Companies replaced fighters.
- One rule mechanism replaced the overlapping behaviour controls.
- One morale clock replaced the separate morale systems.
- Deterministic lateness replaced fidelity dice.
- One command currency replaced several.

**v1 → v2** (directive a)
- One formation grammar at two scales.
- Stances became shapes.
- Exposure is computed from shape.
- Roles are constrained by position.

**v2 → v3** (directive b)
- The Mass pool is retired; the model is rebuilt bottom-up from N × Q per cell, with four single-job modulators.
- Span of control replaces the leadership cap.
- Engaged and depth N are split.
- Variance scales with √(engaged N).
- Pursuit is added.

**v3 → v4** (directive c)
- Plans (routes with conditional steps) and standing rules, as two arrangements of one rule mechanism.
- Condition vocabulary restricted to what the unit can perceive.
- Action vocabulary including withdraw (ordered or give ground) and signal.
- Go-codes versus messengers, drawn from one command budget.
- Manoeuvres (envelopment, feint, delay, ambush, flank march) built from the same parts rather than special rules.
- Minimal terrain.
- Fatigue deliberately left out.
- Pre-battle scenes gain intelligence stakes.
- Document made self-contained.

**v4 → v5** (critique of 2026-09-22; directive d)
- Battle termination defined at cell, squad and army scale, with mutual disengagement, a nightfall cap and an objective zone (L1).
- Rules split into a plan channel (movement and posture, squad) and an engagement channel (cell), with three posture actions and a squad-scale instinct (L2).
- Delay replaced by control state with weighted Pressure and hysteresis; lateness kept only for orders (L3).
- Morale: shock cap per tick with a declared rear-charge exception; contagion bounded by geometry with a refractory period; clock length from grade and depth; starting position from Stability (L4, L5, d.1).
- Feint conversion derived from control state; observers cannot tell withdrawal from rout (L6).
- Missile firing ranks, ammunition and resupply; depth costs missile casualties and reform time (L7, E5).
- Brace added to Q; winning an exchange defined (L8).
- Command holders fixed; regenerating CP budget; shouts; go-code semantics (L9, L10, L12).
- One time unit; rounding and clamping (L11).
- Doctrine persists in three layers; marshal delegation; AI under the same rules (P1, E6).
- The general's view as the player's fog of war; preview limited to own plans and scouted ghosts; turning-points report (P2, P4, P5).
- Real time with pause and three speeds (P3).
- Footprint pathfinding and marching shape (P6).
- The player character as commander with a duel (P7, d.3).
- Battle outputs: killed, scattered, present; grade progress; familiarity; deeds (E1).
- First simulation specified with a pass criterion (E3).
- Bounded seeded timing variance (E4, d.2).
- Channeller cells removed; battle troop types are mundane (E7, d.4).
- Diagnostic pre-screen updated; findings D11–D15 added; resolution crosswalk added.

---

## 13. Decisions needed (Jordan)

Directive d closed E2, E4, P7 and E7. Still open:

1. **Directives b and d:** the ledger entries and the propagation lists (header).
2. **Q profile and J-10 dependence** (attack, defence, reach, speed, brace, missile values); **muster → cells (J-9)**, including which faction stat(s) set grade distribution (§10.2) and where generic squad leaders' Cmd comes from (§3.4).
3. **D5:** whether morale is one concept (cohesion) with two expressions, scaling output and triggering the rout.
4. **Where battlefield terrain comes from** (§7.1), and with it the **objective zone** definition and the source of the **nightfall cap** (§8.5).
5. **Mapping onto the 7 canon phases** (§10.4); **aggregated Key types (J-2)**; **the attached-character Steadiness stat (J-12 / J-33)**.
6. **§3.8:** whether parley or deception can plant false signals or false ghosts (§10.1).

Every `[ASSUMPTION]` tag is a vetoable mechanical call; none blocks the next step.

---

## 14. Path to canon

With repo access:
1. Run bootstrap with task `design_proposal`.
2. Read `mass_battle`, `combat_engine_v1`, `scale_transitions`, any terrain source, the muster and levy source, the GD-2 text, and the armature / npc_behavior source at depth `index`.
3. Re-verify every `[READ: map_v1]` and `[READ: graph_v1]` value carried from v4, and every `[verify against canon]` tag.
4. File the ledger entries for directives b and d.
5. Fill the placeholders.
6. Run the first simulation (§9.1); then D1, D6, D9, D13 and D14.
7. Run the full resolution-diagnostic.
8. Commit to `designs/proposals/`, with a `canonical_sources.yaml` co-file.
