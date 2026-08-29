# 05 — Faction actions: every tier, ethos in the choosing, influence without conquest

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md) ·
## [`01_substrate_primitives_part2.md`](01_substrate_primitives_part2.md) ·
## [`04_personnel_management.md`](04_personnel_management.md) · `engine/autoload/dice_engine.py` ·
## `systems/settlements/settlement_layer_v30.md` · `systems/factions/faction_canon_v30.md` ·
## `systems/world/worldbuilding_v30.md` · v1 [`05`](../2026-08-28-greenfield-systems-suite/05_faction_actions.md) (ARCHIVED)
## Executes: **ED-IN-0201** (Jordan, 2026-08-28, `registers/editorial_ledger_in.jsonl`) — both clauses
## Continues in: [`05_faction_actions_part2.md`](05_faction_actions_part2.md) — §§5–10

**Nothing here is a new primitive.** A faction action is a Post's remit invoked against a Gauge, ranked
by a derivation over an Entity's identity and its holder's form, costing a Gauge, sometimes rolling on
the single-owned kernel. Four stored things, four write leaves, no fifth.

**This document is in two parts, in reading order** (`CLAUDE.md` §4): **part 1** — the playing
surface, the per-tier gate, the per-post budget, `appeal`, and `act.contest_influence` (§§0–4).
**[Part 2](05_faction_actions_part2.md)** — the action set, the resolution shape, the two effects
constraints, J-N and J-O, the module contracts and the property audit (§§5–10). Section numbers run
continuously across both, and the `## Overrides` block above governs both.

**v2 delta in one line:** v1 let a faction act **once, nationally, if it had a head, and chose by its
head's convictions alone.** v2 lets it act **at every tier where it staffs a post**, pays **per post**,
chooses by **institution and holder together**, and can **contest a place it does not own without an
army.**

---

## Overrides

Per the suite's one hard rule (`00 §5.3`): **a silent override is the corpus disease this suite exists
to stop.** Each row is vetoable on its own.

| # | What is overridden | Tier | Why |
|---|---|---|---|
| **O-5.1** | v1 `05 §8`'s `fa.gate` / `fa.select` declared `scales: [peninsula]` — one head, one national actor | this suite's own v1 | It made every faction national or nothing, and made faction *emergence* inexpressible: the Restoration Movement is canonically **territoryless**, operating on community-scoped Presence markers (`systems/factions/faction_canon_v30.md:370`, PP-460). A design in which the RM cannot act is a design that cannot ship the setting. §1 |
| **O-5.2** | v1 `05 §2`'s budget — `min(count of posts held, FACTION_ACTION_CEILING)`, a faction-scope scalar | this suite's own v1 | A count over posts is an **aggregate**, and the write rule forbids writing one; v1 derived it at read, which was legal but put a faction's whole capacity in one number that no post owned. The budget is the `post.budget` Gauge that `01 §5.3` already declares, **summed at read, spent per post**. §2 |
| **O-5.3** | v1 `05 §3.2`'s `appeal` — head's convictions only — and its claim that *"a faction's character is who holds its head post"* | this suite's own v1 | Root cause C (`ARCHIVED.md`): it left **no institution to be in tension with** and no continuity across a succession. `appeal` now reads `identity.ethos` **and** the holder. §3 |
| **O-5.4** | The delta spec's own §5.4: *`act.contest_influence`, shape **SO**, obstacle via `derive_ob` against the incumbent's presence level* | this suite's own spec | Shipped as **DO with an entrenchment obstacle**. An SO makes a staffed defender inert — the incumbent's officer, whose choices ED-IN-0201 clause 2 says must matter, would not be consulted in the one action aimed at them. The obstacle survives unchanged and still derives from presence through `derive_ob`; what is added is the defender's roll. §4.1 argues it in full. **`01 §6` point 2's forward reference to "an incumbent's presence level (`05 §4`)" is honoured exactly**, not routed around |
| **O-5.5** | v1 `05 §5`'s `act.treat` — *"paired `Debt` tags with terms and an exit"* | this suite's own v1 | Superseded by change E: **a treaty is an edge with its terms in its tags** (`00 §4.3`). Two representations of one relationship was the shape-divergence defect v1 claimed immunity to. `12` owns the edge kind; this document only names the action that creates it |
| **O-5.6** | The delta spec's and the task brief's four-rung tier ladder *local → territory → province → peninsula* | this suite's own spec, against **canon** | `systems/settlements/settlement_layer_v30.md:151` reconciles the vocabulary explicitly: geography's **"territory" IS the province-tier node** (T1–T17), the settlement is the base unit, and *"the province is the aggregate of its settlements"*. Territory and province are **one rung under two names**, and minting both would re-commit the collision that line was written to close. **The mechanism is rung-count-agnostic** (§1.1): the gate and the budget iterate over whatever rungs `references/form_registry.yaml` declares, so if Jordan wants a fourth it is a registry row and not a design change |

| **O-5.7** | `01 §6` point 2's narrowing: *"the `modifiers` argument is reserved for terms genuinely properties of the target"* | this suite's own `01` | Correct as a general rule and **wrong for a contested quantity.** Presence has no single owner: it is a *share* of a place, and the meaningful difficulty is the incumbent's **lead**, not their total. `act.contest_influence` therefore derives its obstacle from `presence_defender − presence_challenger`, which is expressible inside `derive_ob` as an instance-specific modifier and is **not** an actor-advantage leaking into obstacle-space by the back door. §4.1 argues it and states the leverage consequence. **This deletes an object** — the capped σ-space foothold boost an earlier draft of §4.1 carried — rather than adding one. ⚠ **Compatible with, and made safe by, `01 §6`'s new obstacle-reachability gate.** That gate's point 3 observes that `derive_ob`'s `modifiers` argument is unbounded in its signature, so a site must **declare** its `modifier_max`. That declaration is what converts this override from *a reading of the ruling* into something **checkable**: a contested lead is a legitimate instance modifier precisely because it is now bounded and audited rather than asserted. The site's declaration is `part 2 §9`; its status is §4.1a |

| **O-5.8** | **Canon's Faction Declaration as a roll** — `settlement_layer_v30.md:1046` prices it as a Domain Action (Influence pool = Renown ÷ 2, Ob 3), and `:1049-1063` (ED-790) ships a founded faction's starting stat sheet | **canon**, under the authority amendment below | `part 2 §5.4` ships `act.charter` as a **gate**. The uncertainty canon spends on the Declaration roll is, in this suite, already spent getting a project to its threshold (`09`'s `am.advance` → `am.fire`); rolling again **charges twice for uncertainty already paid**, which is verbatim `07 §9.2`'s argument for gating a growth threshold rather than re-rolling it (`00 §6` principle 4). ED-790's stat sheet is **superseded structurally, not by preference**: every faction quantity in this suite except `treasury` is a *derivation* (`06 part 2 §9`), so a founded faction cannot be *given* starting values for them — it computes them on its first boundary from what it holds. Three identity fields and one gauge at floor are the whole of a founding |
| **O-5.9** | **This document's own first draft of `fa.select`** — *"consumes no randomness"*, ties broken by cost then registry order | this document, against **the ratified engine** | **v2 had silently deleted stochastic NPC selection that the ratified engine has, and this row retracts it.** `systems/factions/sim/faction_action.py:251` draws `roll = rng.random()` against state-re-weighted action weights, and `:457`/`:566` draw the *target* with `rng.choice`; `audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md:129-132` states it in as many words — *"faction priority trees are NOT fully deterministic … `faction_action.py` draws action and target."* A pure argmax is a fork that resolves identically in every reachable world state, which is not a fork. §3.5 now declares a **softmax over `appeal`** at `APPEAL_TEMPERATURE`, drawn from a per-post substream (`10 §6.4`). One constant; determinism-per-seed is preserved exactly |
| **O-5.10** | **`06 part 2 §9`'s `faction.treasury` row** — `bucket: gauge, writable: false, owner: fm.derive` | this suite's own `06` | **You cannot decrement a derivation**, and `part 2 §5.2` spends it. `01 §2.1`'s aggregate-vs-stock distinction resolves it: an aggregate is recomputable from *current* state; a treasury carrying spend history is **path-dependent**, so it is a **stock**, and a stock is an ordinary gauge with a declared depositor. It leaves `fm.derive`'s state list and becomes a **faction-owned gauge** — deposited at the boundary from `07 §5.1`'s `residual(place)` over places this faction controls, spent by contract muster and upkeep (`part 2 §5.2a`). The precedent shipped a scale down: `accrual.entitlement`, likewise spent directly (`07 §8.3`) |
| **O-5.11** | **`08 §8`'s `sm.act` and `sm.gate` as modules** | this suite's own `08`, coordinated by contract rather than by editing it | They are `fa.resolve` and `fa.gate` in a settlement costume, and **both documents say so in their own sentences** — *"a faction action at the peninsula rung and a settlement verb are the same object at different rungs"* (`part 2 §10.1`), *"a governance response and a faction action remain the same object at different tiers"* (`08 §9.2`). `fa.resolve` already declares `remit: [head, governor, minister, envoy, commander]` and `fa.gate` already iterates **every** declared rung. `part 2 §5.5` absorbs them: `08`'s eight rows land here as action rows with `tiers: [settlement]`, `remit_kinds: [governor]`. **`sm.respond` is untouched and survives** — a directive addressed to a holder is a genuinely different object. **Zero outcomes lost; zero surface verbs added** |
| **O-5.12** | **This document's own `act.motion` row** | this document | The motion was designed **twice, with different shapes**: a one-line family row here (DO, target *"the opposing coalition"*) against `12 §5`'s full design — `price(magnitude) = k·magnitude` in the proposer's own `standing`, a monotone `vote_bar(magnitude)`, and a published `vote_weight` carrying change E's bounded relational term. **`12`'s is the fuller design and it wins.** The row is cut to a pointer; `ad.motion` is self-contained (`remit: [head, minister]`, its own `post.budget` cost), so nothing is orphaned |

**⚠ The authority model was amended mid-draft (Jordan, 2026-08-29): *"existing work is not
necessarily required to keep all the way through to things like obstacles being stat/2 or whatever is
ratified and canon … I just want the best possible proposal."*** Jordan named the **score/2 obstacle
derivation** as his worked example of something a proposal may replace. This document **weighed it and
kept it**, and §4.1a states the argument on the merits rather than on its status — together with the
**commensurability condition** the ruling does not carry and which this page found while testing it.
What is kept regardless, and is an architecture invariant rather than a ruling, is the **single-owner
property**: whatever the derivation is, it lives in `derive_ob` and never per-verb.

**Not overridden, deliberately.** v1's obstacle owner, its σ-space modifier discipline, its
budget-buys-actions-never-modifiers arithmetic, its vacancy recoverability, its effects-totality rule
and its no-elimination-on-failure rule are carried **with their reasoning**, not as bullets — §§2.2,
6, 7. They survived the critique (`ARCHIVED.md`) and re-deriving them would be the elegance failure
`00 §1` names.

---

## 0. The playing surface — what a player is actually asked, and how often

`00 §2` is the binding constraint on this page, and faction action menus are precisely where deep
games drown a player. **The eight action families below are a strategic *capability* list,
not a menu** (`00 §2.3` point 2). Most are invoked headlessly by NPC post-holders. The split is
explicit and it is the point of the whole design:

| | under the hood (substrate) | on the surface |
|---|---|---|
| **who acts** | every post-holder of every faction at every tier, including the player's own faction's other officers | the player, through the posts **they personally hold** (`01 §4.4`) |
| **how the action is chosen** | `appeal` ranks the option set; the highest-ranked available action is taken. No RNG, no player input | the ranking is **shown**, and the player picks |
| **how many decisions** | unbounded — this is the world running | **one per Slate item**, and the Slate's budget is the only bound (`10`) |

**Surface table — the whole of it:**

| what the player is asked | how it reaches them | how often | options |
|---|---|---|---|
| *Direct this season's action for a post you hold* | a Slate item, when that post's tier has an action worth a decision | at most once per held post per season, and only if the Slate lit it | **the top `SHORTLIST_K` actions by `appeal`, ≤ 4** — genuinely different in kind because the ranking spreads them across the symbolic axes |
| *inspect the full ranking* | on demand from that item | never pushed | read-only |

**Substrate objects on this page: 8 action *families* · 1 per-tier gate · 1 per-post budget · 1 appeal
derivation with a declared draw · 1 contested-influence resolver · 1 flat ceiling. Surface affordances:
1 decision, 1 inspection.** Six-to-one, which is the ratio `00 §2.3` point 4 asks for.

⚠ **Families, not rows — and the distinction now matters, because the row count grew and the family
count did not.** A family is a schema entry; its *rows* are registry data (§4.5). `part 2 §5.5` absorbs
`08`'s eight settlement rows into the `act.govern` family, which adds **eight rows and zero families,
zero modules and zero surface verbs**. The playing-surface budget this page bills is unchanged at
**one**, and `08` keeps its own one for `sm.respond`.

**`05` contributes exactly ONE verb-slot to the game's single-digit budget** — *direct a post's
action* — and it is the same slot whether the post is a national head, a provincial minister or a
settlement governor, because it is the same module. **Everything that looks like breadth is the
`appeal` ranking's job, not the player's.** The eight families are registry rows the engine
chooses among; a player who never opens the inspection view never learns their names.

> **The test `00 §2.3` point 5 asks:** *could this be removed from the player's hands entirely and
> still change the game?* For seven of the eight families, **yes** — and they are therefore
> substrate. The one thing that fails the test is *which* of the ranked actions is taken when the
> player is present, and that is the one thing left on the surface.

---

## 1. C1 — the gate, applied per tier

> *"we do not allow the game to perform faction actions if there is no leader of that faction"*
> — ED-IN-0201 clause 1

```yaml
module: fa.gate
resolver: gate
class: substrate
```

Before a faction's action phase runs, **once per rung of the tier ladder it appears on**:

```
for tier in declared_tiers:                      # from references/form_registry.yaml
    acting_posts = [p for p in posts(faction, tier)
                    if p.holder_id is not None
                    and p.remit ∩ action_modules ≠ ∅]
    if acting_posts == []:
        emit faction.action_declined(faction, tier, reason="vacant_post")
        continue                                 # no action AT THIS TIER; other tiers unaffected
    run the action phase for those posts (§2)
```

⚠ **`action_modules` is the whole game's invocable set, not this document's.** It is every module any
post's remit may name — `fa.*` here, `pm.*` (`04`), `ad.motion` and `ad.unit` (`12`), and, per O-5.11,
the settlement rows now carried by `act.govern`. A faction whose only seated post is a `commander` is
**acting** when that commander orders a unit's assignment, so the gate must not read "does this post's
remit contain a `fa.*` row" or a commander-only faction goes silent for a reason nobody designed.

**It is a precondition, not a penalty** — carried from v1 unchanged. Nothing resolves, no roll is made
at a disadvantage, no gauge is docked. The faction simply does not act *there*, and a Key says so with
a reason, because there is no GM and a faction that stops acting with no visible cause is the most
confusing thing a strategic layer can do to a player.

**What per-tier buys, and why v1's single peninsula gate could not:**

| world state | v1 | v2 |
|---|---|---|
| a faction with a governor in one settlement and no national head | **cannot act at all** | acts at settlement tier; declines at territory and peninsula, each with its own Key |
| the Restoration Movement — canonically territoryless, community-scoped Presence (`faction_canon_v30.md:370`) | inexpressible | a faction whose only rungs are settlements |
| a national head vacant while ministers are seated | the whole faction freezes | the peninsula rung freezes; the province and settlement rungs keep running |
| a new faction forming from a single seated officer | no path | the ordinary path — it is a **local** faction, and it grows by staffing rungs |

*Emergent possibility lost if the per-tier gate were cut:* **faction emergence and faction decline
would both be binary.** A faction could only be national or dead, and the ruled hierarchy would have
no mechanical consequence at all.

### 1.1 The tier ladder is data, and the mechanism does not know how long it is

`declared_tiers` is read from `references/form_registry.yaml` (`00 §9`), which owns the containment
axis. **Nothing in this document names a rung count.** The shipped ladder, grounded in canon rather
than invented:

| rung | canon | the `scale` its Keys carry |
|---|---|---|
| **settlement** | the base civic/political/living unit and the siege target (`settlement_layer_v30.md:151`) | `settlement` |
| **territory** | the 17 top-level map nodes T1–T17; *"geography's 'territory' remains the province-tier node"* (`:151`) | `territory` |
| **peninsula** | the whole board; the three provinces are the Altonian colonial administrative overlay (`worldbuilding_v30.md:213`), an aggregate of territories, not a fifth kind of node | `peninsula` |

**Territory and province are one rung under two names** — O-5.6. Minting both would re-open the exact
collision `settlement_layer_v30.md:151` was written to close, and this suite's whole reason for
existing is to stop doing that. If Jordan rules the provincial overlay into a distinct governing rung,
**it is one row in the form registry and zero lines here.**

⚠ **`scale ⟂ tier` still holds** (`00 §3.1`). The three rungs happen to *share names* with three of the
runtime scale enum's four members, and that is a naming coincidence with a mapping declared in the
registry, not an identification. A settlement-tier action whose consequence reaches a whole territory
emits a `territory`-scale Key; the rung says who acted, the scale says how far it reaches. **Nothing
here proposes a fifth scale member**, and the province question routes to ED-IN-0103 rather than being
resolved locally.

### 1.2 A closed gate is always recoverable — carried from v1 §1.2 unchanged

`fa.gate` closing at a rung raises `post.vacant`, which raises a `cg.demand`, which is **total**
(`02`). The head post's demand resolves at the faction's own **seat node** — `identity.seat_node`,
immutable (`01 §1.1`) — *not* at one of its holdings. A faction reduced to zero territory can still
produce a claimant to its own headship. Without that anchor, a faction with no holdings has no node at
which to generate, the gate closes forever, and an elimination mechanism nobody designed arrives as a
side effect of where generation is anchored.

**v2 makes this stronger, not weaker.** With a per-tier gate, losing the peninsula rung is now a
*partial* silence rather than death — the faction keeps acting wherever it still staffs a post, which
is exactly the graded decline `06 §6` describes and the opposite of an elimination check.

---

## 2. The budget is per post, and there is no pool

```
capacity(faction, tier)  =  Σ over posts held at that tier of  gauge_value(post.budget)
```

**Derived at read; never stored, never written.** `post.budget` is the Gauge `01 §5.3` already
declares, owned by `substrate.post`, one per post. There is no faction-scale action-point number
anywhere, because an aggregate has no setter (AU-1) and because the moment one exists somebody
allocates from it.

**This is Jordan's 2026-07-13 ruling as arithmetic rather than as a sentence:** factions hold people,
and *the number of people and the weight of their positions carry the value of the faction.* A faction
with four seated officers does four things because there are four budgets, not because a central pool
was sized at four.

### 2.1 Why a per-post budget and not a pool — three reasons, and the third is the binding one

1. **A pool is a surface decision; a per-post budget is not.** A pool must be allocated, and allocating
   it is a screen — the exact playing-surface inflation `00 §2` forbids. A per-post budget is spent by
   whoever holds the post, headlessly, in the ordinary case.
2. **A pool erases the tier.** One number cannot say *where* a faction can act, so a pool re-creates
   v1's single national actor with extra steps.
3. **A per-post budget makes staffing the strategy.** Wanting to do more means appointing more people
   — which routes through `04`, costs candidates, and exposes the faction to custody, tenure and
   caste-gated eligibility. **The action economy and the personnel economy become one economy**, which
   is what ED-IN-0201 is about and what v1's post-count scalar only gestured at.

*Emergent possibility lost if the per-post budget were cut:* **a faction could not be a coalition of
people with different reach.** Every faction would act with one voice from one purse, and every
appointment would be flavour.

### 2.2 The flat ceiling survives, with its reachability bar

```
FACTION_ACTION_CEILING : int      # shape proposal, not a ledger constant. Declared in the exported
                                  # params with the justification below attached.
```

Actions actually taken by a faction in a season are truncated to this flat cap **across all tiers**.
It does not scale with post count, holdings or success.

**Why a second bound at all.** The first is a positive feedback term: more actions buys more holdings,
which support more posts, which buy more budget, which buys more actions. That cycle *is* bounded —
post count has a ceiling computable from the tier registry (`03 §3`) — but **bounded is not damped**,
and a bound that scales with success is a weak one. A flat cap is the shape every mature franchise's
anti-micromanagement guardrail takes, and it is cheap now and expensive to retrofit.

**Its reachability bar is stated, because a cap that never binds is indistinguishable from no cap.**
The canonical failure of a well-motivated, legible mechanic tuned so its threshold is never reached is
that it becomes decorative while everyone assumes it is load-bearing. So: **the ceiling must bind for
the leading faction in a stated fraction of controlled campaigns.** If it does not, it is lowered or
dropped — never left in place as reassurance.

**Truncation consumes no RNG of its own** — amended for O-5.9, because the unqualified claim is no
longer true of *selection*. When the ceiling binds, the surviving actions are the highest-`appeal` ones
across all tiers, ties broken by §3.5's ordering rule. Each post's selection draw has already resolved
by then, so truncation is a deterministic function of its inputs. A ceiling resolved by a **second**
draw would put a random number in the one place a player must be able to reason about, and that is
still refused.

### 2.3 The loop, and what is unmeasured

| loop | term that closes it | bound | measured? |
|---|---|---|---|
| actions → holdings → posts → budget → actions | staffing a post requires a candidate through `04`, gated on caste, eligibility and a live person | post count ceiling (data-computable, `03 §3`) **and** `FACTION_ACTION_CEILING` (flat) | **per-cycle gain UNMEASURED.** Campaign-reachable; must be measured with a control before the facility writer that feeds it lands. `tools/balance_oracle.py` is the campaign instrument |
| contest → presence → cheaper contest | §4.4 | §4.4 | **unmeasured** |

### 2.4 One point buys one attempt, and never anything else

**One budget point buys one attempt at one module. It never converts into a die and never into an
obstacle shift.** The arithmetic, from `01 §5.3`: an added die at a balanced check is worth `≈0.204σ`
at pool 5 against `≈0.115σ` at pool 18, and `0.107σ`–`0.302σ` at pool 5 alone as the obstacle varies.
A currency spendable as a modifier is therefore worth **about twice as much** on a small pool as a
large one, and a player who notices routes it wherever it pays. Buying attempts keeps the budget out of
the resolution arithmetic entirely — which also means it is not a resolution object at all, and the
question of its leverage stops existing.

---

## 3. `appeal` — the institution and the holder, and where AI faction character comes from

> *"…that leader themselves is going to influence what choices are made for available faction actions
> in the same way that the person(s) who are governing a settlement or conducting a battle may make
> different choices with the same information and options."* — ED-IN-0201 clause 2

The ruling's own constraint is that this must **not** be a flat trait bonus on a selection roll: a flat
shift of size `X` is worth `X / (0.8·√Pool)` in σ-space, so a leader trait as a bonus is worth
systematically more to a weak faction than a strong one. Two mechanisms satisfy the ruling without
touching a roll, and neither is a probability model.

### 3.1 The remit changes *which actions exist*

The option set is `remit(post) ∩ available(world_state, tier)`. A post kind's remit is declared data
(`01 §4.3`). Two factions whose heads hold differently-typed head posts have **different actions
available — not different odds on the same actions.** The choice differs; the odds do not.

### 3.2 The formula — ethos and conviction, over the same axes

```
appeal(action)  =  w_inst · Σ_axis  ethos_projection[axis]              · action.symbolic_vector[axis]
                +  w_hold · Σ_axis  holder.conviction_projection[axis]  · action.symbolic_vector[axis]
                +          Σ_signal action.signal_weight[s] · signal(s, world)
                +          custody_bias(action)                              # CAPPED, 01 §7 / v1 01 §2.4
```

| term | reads | bucket |
|---|---|---|
| `ethos_projection` | `faction.identity.ethos`, a conviction-weight vector — **immutable** (`01 §1.1`) | entity identity |
| `holder.conviction_projection` | the post-holder's convictions, resolved through `descriptors.resolve_conviction`, which **raises** on an unknown name | person form |
| `signal(s, world)` | the world reads — is there a weak neighbour, is my ground ungoverned, is an institution advancing on me | derived |
| `custody_bias` | the controller's *own* appeal for that action, scaled by leverage held, **clamped to `±RELATION_SHARE_MAX · structural_range`** | tag |

`symbolic_vector` projects the action onto the symbolic axes the Key substrate already carries —
hierarchical, sacred, instrumental, traditional — so **an action's character is data on the action and
a person's response to it is data on the person.** The faction takes the highest-appeal available
action per acting post; the player, where present, picks from the top `SHORTLIST_K`.

**The custody cap is not a nicety.** An uncapped custody term makes controlling a head strictly better
than being one — the controller gets the decisions without the exposure — and it dissolves exactly the
positional conflicts that should be unbuyable. **Custody biases; it never substitutes.**

**Ethos is immutable and practice is not, which is the whole of change C.** What moves is the aggregate
conviction of the post-holders, and the distance between the two is `divergence` — a **derivation**,
owned by `06 §2`, which gates an institutional crisis. This page only supplies the term; it does not
define divergence and does not duplicate it.

*Emergent possibility lost if the ethos term were cut:* **an institution could never betray its own
purpose, and no believer could be at odds with their own church.** A faction's behaviour would reset
completely at every succession, and there would be nothing for a schism to be about.

### 3.3 This is how AI factions get character **without scripting**

`00 §6` principle 2: **never special-case an entity or an outcome.** No faction is named in code
anywhere in this suite. A faction's character is `identity.ethos` — a vector in a registry — weighted
against the same option set every faction shares. A faction that reliably reaches for the sacred option
does so because its ethos projects onto the sacred axis, not because a branch says so.

> **Falsifier (the strongest one this page has), in two halves since O-5.9.** A permutation test:
> **swap the `ethos` vectors of any two factions in the registry, hold every other input fixed, replay
> a seeded season.**
> **(a) Their `appeal` vectors must swap exactly, byte for byte.** `appeal` is a derivation and is
> unaffected by the softmax, so this half is exact and is the half that catches scripting drift.
> **(b) Their chosen actions must swap exactly at `T → 0`.**
> ⚠ **The halves are separated deliberately.** The draw is keyed on `post_id` (§3.5), not on faction,
> so at the declared `T > 0` two swapped factions' *choices* are distributional rather than identical.
> A single test written against the old wording — *"their chosen actions must swap exactly"* — would
> now fail intermittently, and the reflex fix is to loosen it into something that proves nothing.
> Splitting it keeps an exact assertion where an exact assertion is available. Load-bearing on the
> game: it is the difference between AI factions with character and AI factions with a script.

**Faction-unique actions are the same rows with a narrower `remit_kinds`.** A row invocable only by a
head post of a kind that only one faction's registry declares is unique to that faction, with no branch
anywhere and no stub module. A faction with no unique action has one fewer row available, not a typed
no-op.

### 3.4 `posture` selects the weight pair — and this is the only job the field has

`faction.form.posture` is the faction's one form field (`01 §1.1`) and would otherwise be a declared
enum nothing reads. Give it the one job it is shaped for: **each posture value declares a
`(w_inst, w_hold)` pair in the form registry**, `w_inst + w_hold = 1`.

| posture (shape proposal — the vocabulary is the form registry's) | reads as |
|---|---|
| high `w_inst` | a disciplined institution: the office outweighs the officer, and successions barely change behaviour |
| high `w_hold` | a personalist faction: who holds the head post *is* the policy, and a succession is a swerve |

⚠ **`06` owns the posture transition** — what gate moves a faction from one posture to another (the
obvious candidate is sustained `divergence`, which is `06 §2`'s to declare). **This page only reads
`posture`; it declares no transition and names none.** Stated explicitly so the two documents do not
both claim the field.

### 3.5 The selection draw, ties, and disclosure — AMENDED, O-5.9

**This section's first draft said selection *"consumes no randomness"*, and that was a regression
against ratified code rather than a design choice.** It is retracted here rather than quietly
corrected, because the deletion was silent and a silent override is the one thing `00 §5.3` forbids.

- **`appeal` is a derivation; the choice over it is a draw.**

```
P(action)  =  exp( appeal(action) / T )  /  Σ_a exp( appeal(a) / T )     T = APPEAL_TEMPERATURE
draw from     seed(post) = H( campaign_seed ‖ accounting_index ‖ post_id )      # 10 §6.4's construction
```

  `T` is **one constant and a shape proposal like the others** (`part 2 §10.3`). `T → 0` is the argmax
  this page first shipped; `T → ∞` is a uniform pick over the option set. **Its reachability bar, in
  both directions, because a temperature can be decorative either way:** at the declared `T` the
  top-`appeal` action must be the **modal** choice, *and* the second-ranked action must be taken in a
  stated fraction of seasons. A `T` that yields the argmax every season is the argmax with extra
  arithmetic; a `T` that flattens the ranking deletes ethos, which is change C.
- **Why a draw at all — this is a restoration, not an addition.** The ratified engine already draws
  (`faction_action.py:251`, `:457`, `:566`), and the churn design records that it must
  (`narrative_engine_design_v2_churn.md:129-132`). Beyond provenance, the argument on the merits: a
  pure argmax over a derivation is a **fork that resolves identically in every reachable world state**
  — the same faction in the same position always does the same thing, so a player learns the table once
  and the strategic layer stops being a world and becomes a lookup. The softmax is also what makes the
  *institution/holder* split observable: two heads with near-equal `appeal` on two options read as a
  faction that could go either way, which is what "who holds the post matters" is supposed to feel like.
- **The substream is what keeps it order-free, and it is not optional.** Keyed on `post_id`, **not**
  drawn from a shared sequential stream — otherwise whether the player attended one Slate item changes
  how many draws are consumed before another post resolves, silently re-rolling it. That is
  `10 §6.4`(3) verbatim, and `10 part 2 §10` row 4's bit-identity test is the falsifier for exactly
  this property. **`05` adds one axis to that discipline; it does not invent a second one.**
- **Ties are now rare and are still ruled**, because the *published ordering* still exists and
  truncation (§2.2) still reads it: lower budget cost first, then declared registry order. Never the
  first rule alone, so a cheap action is preferred to an expensive equal one.
- **Disclosure, and the honest cost of O-5.9.** Each term of `appeal` is published **per available
  action as a band**: the player sees that their head strongly favours a martial option on conviction,
  that the institution mildly disfavours it, and that a rival holds some leverage. `T` is a published
  constant. **The resolved ordering's margin, the tie-break, and the draw itself are not published.**
  So a player can read the *distribution* and cannot predict the *pick* — that is a real loss against
  the argmax draft's perfect predictability, it is stated here rather than buried, and it is the price
  of a faction that can surprise you. Publish every input; publish a band; never publish the trigger
  (`01 §8`).

⚠ **`00 §7`'s four resolver kinds have no name for this**, and this page will not mislabel it to fit.
`fa.select` writes nothing, so `derivation` remains correct on the rule `00 §7` actually states
(*"never use when anything writes it"*) — but a **declared draw over a derivation** is a fifth thing
its table does not describe, and `d_sigma` is wrong (this is not a σ-space roll on the dice kernel).
The contract at `part 2 §9` therefore declares the draw explicitly in a field the schema does not yet
have. **Reported to `00 §7`'s owner as a schema gap, not resolved locally.**
- **The shortlist is truncation, not concealment.** `SHORTLIST_K ≤ 4` (shape proposal) is what reaches
  the Slate item; the full ranked list is one inspection away. A menu that is *ranked and truncated* is
  the playing-surface budget done honestly; a menu that is *hidden* is a different and worse thing.

---

## 4. `act.contest_influence` — challenging for a place you do not hold

v1 had **literally no way to contest a place except militarily.** That is why the Church, the Guilds
and the Restoration Movement could not matter: canon gives the RM no territory and no Mandate at all,
only *"Presence markers + Community Weaving"* (`faction_canon_v30.md:370`), and v1 offered no verb that
moves a presence.

```yaml
action: act.contest_influence
binds:  {institution: <institution_id from references/content_registry.yaml>}
moves:  place.form.presences[institution]      # a Gauge, 07 §4 — NEVER ownership
tiers:  any rung at which the acting post's remit contains this row
```

*Emergent possibility lost if it were cut:* **every faction that is not an army becomes decoration**,
and the only story the strategic layer can tell is conquest.

### 4.1 The shape is **DO**, and the obstacle is the incumbent's **lead**

```
net_c  = continuous net of the challenger's post-holder                 (§6's pool shape)
net_d  = continuous net of the defender's post-holder                   (§6's pool shape)
Ob     = derive_ob( presence_defender ,  modifiers = −presence_challenger/2 + place_terms )
       = max( OB_MIN , (presence_defender − presence_challenger)/2 + place_terms )

degree = degree_from_net( net_c − net_d , Ob )
```

`degree_from_net(net, ob)` reads `margin = net − ob` and nothing else
(`engine/autoload/dice_engine.py:227`), so passing the differential as `net` and the entrenchment lead
as `ob` produces **`margin = (net_c − net_d) − Ob`** on the single-owned ladder, with **no second
degree semantics invented.** TN is 7 and is never named here: `_require_tn7` raises on anything else
(`dice_engine.py:182`, ED-IN-0196). `derive_ob` is the obstacle's only owner (`01 §6`); this document
computes no obstacle of its own, and that single-owner property is the thing actually worth protecting.

**Why DO rather than the SO the spec named (O-5.4).** Under an SO the incumbent does not roll, so the
one action aimed squarely at another faction's officer is the one action in which that officer's
identity is irrelevant — ED-IN-0201 clause 2 satisfied on the attacking side and abandoned on the
defending side. A contest for influence *is* two institutions with two people in the room.

**Why the lead and not the absolute level (O-5.7).** `01 §6` point 2 reserves `derive_ob`'s
`modifiers` for *"terms genuinely properties of the target"*, which is the right general rule — it is
what stops an actor's own advantages leaking into obstacle-space, where leverage is non-uniform. It is
the wrong rule **for a contested quantity**, and presence is the only quantity in this suite that is
inherently a *share* rather than a possession. Three consequences, and they are why this is better
rather than merely different:

| | absolute (`Ob = P_d/2`) | **lead (`Ob = (P_d − P_c)/2`)** |
|---|---|---|
| two institutions both deeply established at one place | the contest is near-impossible for both, forever — a stalemate the world cannot resolve | `Ob` floors at `OB_MIN`: a genuinely even contest is a **coin-weighted-by-officers**, which is what it should be |
| a first incursion into a stronghold | hard | hard, by the same arithmetic |
| the runaway loop (§4.4) | the discount channel is a **separate capped σ-space boost** — a second object, a second constant, a second place to get the cap wrong | the discount **is** the obstacle, and it **saturates at `OB_MIN`**: past parity, further presence buys nothing at all. The feedback term has a hard stop built into the shape rather than bolted on |

**It deletes an object.** An earlier draft of this section carried a capped σ-space `net_boost` from
the challenger's own foothold *in addition* to the absolute obstacle — two channels, two constants,
one job. `00 §1`'s under-distilled failure is *two objects doing one job*, and this is one.

**What each side contributes, and why the incumbent is not counted twice.** It is exactly the
institution/holder split change C introduced, applied to a roll instead of to a ranking:

| | the person | the institution |
|---|---|---|
| **challenger** | `net_c` — their post-holder's pool | their presence, as a **reduction** in `Ob` |
| **defender** | `net_d` — their post-holder's pool | their presence, as an **increase** in `Ob` |

Symmetric channels for symmetric things, which the two-channel draft was not. The defender's *person*
rolls and the defender's *institution* sets the bar; they are different quantities, so this is not
double-counting.

**One recorded consequence, so a later reader does not mistake it for an unnoticed defect.** The
obstacle lives in success-space while the differential's spread is wider than either side's alone
(`σ_diff = √(σ_c² + σ_d²)`), so a fixed `Ob` is worth less per point here than in a one-sided check —
and, because success-space terms are non-uniform in pool, an entrenchment lead protects **most**
against a weak challenging officer. That is non-uniform *in the correct direction* — self-damping, the
shape a bounded system wants — and it is the same property `01 §6` records for capability investment.

### 4.1a Is `score/2` the right derivation here? — weighed on the merits, kept, with a condition

Jordan, 2026-08-29, named this rule as the worked example of something a proposal may replace. So it
is answered here as a design question rather than cited as a settled one.

**Kept, and the argument is not "it was ruled".** Three properties earn it:

1. **Halving is what puts the obstacle inside the range the ladder discriminates over.** The ladder's
   bands are `<0`, `[0,1)`, `[1,3)`, `≥3` in *net successes* (`dice_engine.py:227`). A pool of 6–18
   produces `μ = 0.4·Pool ∈ [2.4, 7.2]`. An obstacle taken at full score would sit on the same scale as
   the score, which for any gauge with a two-digit ceiling puts every contest past the ladder's
   discriminating range; halving is the cheapest correction that keeps the four bands all reachable.
2. **One divisor beats one per verb.** The alternative anybody reaches for — a per-action difficulty
   coefficient — is exactly the fork `01 §6` measured six private copies of. A single derivation that
   is *approximately* right everywhere is worth more than eight that are each locally tuned and drift.
3. **It is auditable by a reader.** *Half the target's score* is a sentence a player can hold; a
   calibrated curve is not, and P-i is this page's strongest property.

**⚠ The condition the ruling does not carry, and this page found while testing it — the finding is
not local to `05`.** `score/2` is only meaningful when **the score's scale is commensurate with the
net's scale.** Nothing in the tree checks that, and the tree contains at least one gauge that would
break it: canon scales Thread Sensitivity **0–100** (`01 §5.2`, citing
`systems/overview/clock_registry_v30.md:72`). A gauge on a 0–100 scale used as a `derive_ob`
`target_score` yields obstacles up to **50** against nets whose μ tops out near **7.2** — every band
but Failure unreachable, a mechanic that looks live and is dead. Since `presence.<institution>`'s
scale is `07`'s to declare and is **not yet declared**, this is a live hazard on the very action this
page introduces, not a hypothetical.

**⚠ THE GATE WAS BUILT, AND THE FORM THIS PAGE FIRST PROPOSED FOR IT WAS WRONG.** An earlier draft of
this section proposed the check as `ceiling/2 < 0.4·POOL_MAX + 3` and flagged it for `01 §6`'s author
rather than duplicating it. That author built it and **rejected the inequality on three counts**, two
of which change what this page must do. Recorded here rather than quietly corrected, because the
finding was this page's and so was the error:

| # | what was wrong | consequence |
|---|---|---|
| 1 | it **omits the σ term** and has the band offset's **sign backwards** — Overwhelming needs `net ≥ ob + 3`, so the obstacle is bounded *below* the envelope, not compared to a mean plus 3 | **2.57× too permissive at pool 5** (it admits `Ob < 5.0` where the correct form admits `Ob ≤ 1.943`), and it agreed at pool 18 only by coincidence |
| 2 | **`POOL_MAX` does not exist** in `engine/` — `roll_pool` enforces only a minimum of 1 (`dice_engine.py:196`) | the gate is necessarily **per-site**: a site's maximum pool is a property of its own pool expression, not a global |
| 3 | **`derive_ob`'s `modifiers` argument is unbounded in its signature**, so checking a bare ceiling proves nothing if a site may add +10 | a site must **declare** `modifier_max`; this is also what makes O-5.7 checkable rather than asserted |

The correct form, owned by `01 §6` and not restated as a rule here:

```
derive_ob(S_max, M_max) + 3  ≤  0.4·N_max + z·0.8·√N_max          z = 1.645
```

**And one further correction this site forces, handed back to `01 §6`.** That inequality's right-hand
side is the envelope of a **one-sided** net, `μ = 0.4·N`, `σ = 0.8·√N`. `act.contest_influence` is a
**DO**: the quantity the ladder reads is a *differential*, whose envelope is

```
μ_diff = 0.4·(N_c − N_d)          σ_diff = 0.8·√(N_c + N_d)
```

so the gate must evaluate a DO site with the differential's moments or it will pass this site on the
wrong arithmetic. It is **stricter, not laxer** — at the most favourable reachable configuration
(strongest challenger `N_c = 18` against weakest defender `N_d = 6`) the envelope is **11.247**, so
`Ob ≤ 8.247`, against **9.783** for a one-sided pool-18 site. Evaluating this site one-sidedly would
be a **false pass**, which is exactly the class of defect the gate exists to catch. ⚠ Flagged to
`01 §6`'s author as a second case the gate must carry; **this page does not implement a second gate.**

**What this site declares, and what follows for `07`** (the block itself is at `part 2 §9`):

| field | value | basis |
|---|---|---|
| `target` | `presence.<institution>` | the gauge the obstacle derives from |
| `pool_max` | **18** | §6's pool shape — `attr` 1–7 twice plus `POOL_BASE = 4`. Not a global; this site's own expression |
| `modifier_max` | **2** *(shape proposal)* | the ceiling on positive `place_terms` — a charter edge, a cathedral facility. **The challenger's lead term is strictly non-positive and cannot threaten reachability**, so the declared bound is the positive side only, which is the worst case the gate must evaluate |

Solving the DO form at `M_max = 2` gives the constraint this page hands to `07`:

> **`presence.<institution>` must be declared with a ceiling of `≤ 12`**, or `act.contest_influence`
> has no reachable Overwhelming band. (At `M_max = 2` the bound is `12.49`; at `M_max = 0` it is
> `16.49`, at `M_max = 3` it is `10.49` — so the modifier ceiling and the gauge ceiling trade against
> each other and both must be declared together.)

**STATUS: UNVERIFIABLE, not passing.** `presence.<institution>`'s ceiling is `07`'s to declare and
does not exist yet. **An undeclared ceiling is not a passing one**, and this page will not assume a
value to manufacture a green result — that is the confounded-measurement failure `CLAUDE.md §0.1`
exists to prevent. Two of the three fields are declared and the third is a named dependency.

### 4.2 An unstaffed defender does not roll — that is a gate, not a cheaper path

If the defending faction holds no post at that rung with the remit to defend, **there is nobody to
roll**, and inventing a phantom defender would be exactly the scripting the suite forbids.

```
if defender has no seated post with remit at this rung:
    resolver = gate                       # NOT a roll, and NOT a second resolution path
    the challenger's presence deposit is the declared UNCONTESTED value — bounded, and
    strictly less than an Overwhelming's — and the defender's presence takes no deposit at all
```

This is `00 §6` principle 4 exactly — *gate where the answer is on the board* — and it is the same
shape as `fa.gate` itself: **an institution that does not staff a place loses ground there without a
roll.** It is also the mechanism that makes §2's per-post budget bite from the other direction:
presence you do not staff is presence you are conceding.

⚠ It is **not** a second engine (`01 §4.4` point 3). The two paths differ in *whether a contest
occurred*, not in how a contest resolves. A defended contest and an undefended one never produce the
same event, so there is no divergence to calibrate.

### 4.3 Effects — graded, total over four bands, and none of them transfers a place

| band | challenger presence | defender presence | other |
|---|---|---|---|
| **Overwhelming** | `+d₃` | `−e₂` | a `Precedent` tag on the place recording the reversal; a `Grudge` on the defending faction's edge |
| **Success** | `+d₂` | `−e₁` | a `Precedent` tag |
| **Partial** | `+d₁` | `0` | budget spent; the attempt is public |
| **Failure** | `0` | `+e₁` *(the defence is itself a demonstration)* | an `exposure` deposit on the challenger's holder |

`d₁ < d₂ < d₃` and `e₁ < e₂` are **shape proposals**, declared per institution kind in
`references/content_registry.yaml` — not ledger constants, and not numbers this document may fix.

**Total over four bands, nothing unique to Partial (P0-3).** The Partial window is a fixed
one-success width over a spread growing as `√Pool`, so its probability falls monotonically and Q-3 is
not this suite's to answer; the design therefore declines to depend on it. Note the Failure row is not
empty — a failed contest *helps* the defender, which is what makes a poorly-chosen contest a real cost
rather than a free reroll of the season.

**Nothing here transfers a place, ever.** Control changes by exactly two routes and neither is this
one: `act.campaign` (force, §5.1) and `04`'s appointment path. What high presence *does* buy is
**eligibility** — a faction with a strong presence at a place has candidates who pass `pm.candidates`
for that place's governance post when it falls vacant. **Influence buys standing to be chosen; it never
buys the chair.** That is the whole answer to *"how do the Church and the Guilds matter without
armies"*, and it costs no new mechanism because `04` already owns the eligibility gate.

Crossing a presence band is a **form transition** on `place.form.presences` — declared in the form
registry with a **required hysteresis band** because the pair is reversible (`01 §2.3`), gated never
rolled, and emitting `form.transitioned` as a **crossing fact, never a forecast**. `07` owns those
rows; this document supplies the deposits that move the gauge.

### 4.4 The loop this opens, its bound, and what stays unmeasured

**The loop:** presence at a place → a smaller obstacle → cheaper further contests there → more
presence. Positive feedback, and naming it is not optional.

| damper | kind | binds? |
|---|---|---|
| the discount **saturates at `OB_MIN`** — past parity, further presence buys the challenger nothing | hard floor, **structural** | yes, by the shape rather than by a constant (§4.1) |
| **one contest per (faction, place, season)** — a gate, not a cost | hard cap | yes; stacking posts on one place is impossible, so the strategy is spread, not mash |
| every contest costs **one budget point of one staffed post** | opportunity cost | yes, and it is the real bound: holding presence at *N* places costs *N* officers' seasons |
| the presence gauge is bounded with geometric decay, fixed point `rest + a/λ` | structural | yes — `01 §5.1`'s declaration-time falsifier applies unchanged |
| a rising presence raises the `Ob` **anyone else** faces at that place | derived | yes for third parties, and the same lead arithmetic applies to them, so a third challenger with a foothold is not locked out |

**The honest residue: the per-cycle gain is UNMEASURED.** It is campaign-reachable, so it is
measurable — `tools/balance_oracle.py` is the campaign instrument and it is deliberately not a CI gate
(CLAUDE.md §7). It must be measured **with a control** before this action is tuned; a number without a
control is not a measurement in either direction (CLAUDE.md §0.1 point 4).

### 4.5 One verb, N institutions — what this refuses to add

`00 §1`'s corollary: **prefer one object with a registry of kinds over several objects.** Proselytising,
guild capture, covert subversion, Warden network-building and Restoration community weaving are **the
same row with a different `institution` binding and a different `symbolic_vector`.** All of the
following were considered and **refused**:

| refused | because |
|---|---|
| `act.proselytise` | `act.contest_influence` bound to the Church institution |
| `act.subvert` | the same row bound to a covert institution, with a sacred/instrumental vector and a larger `exposure` deposit on failure |
| `act.fund` / `act.patronise` | the same row bound to a Guild |
| a separate **covert** resolver with concealment rules | concealment is `01 §8`'s disclosure block on the state row, not a second engine |
| a per-institution presence *primitive* | it is a Gauge keyed by institution id (`01 §5.2`), which is what a registry of kinds means |

**Eight families, not thirteen** — and the eighth justifies its slot against the five above, which is
the test the brief sets (**still eight after O-5.12 cuts `act.motion` and `part 2 §5.4` adds
`act.charter`**; the membership moved, the count did not): each of them is this row with two fields changed, and shipping them separately
would mean five effects tables to keep total and five places for the Partial band to rot.

---

**Continues in [`05_faction_actions_part2.md`](05_faction_actions_part2.md) — §5 the action set onward.**
