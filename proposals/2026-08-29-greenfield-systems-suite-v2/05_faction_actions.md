# 05 — Faction actions: every tier, ethos in the choosing, influence without conquest

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md) ·
## [`01_substrate_primitives_part2.md`](01_substrate_primitives_part2.md) ·
## [`04_personnel_management.md`](04_personnel_management.md) · `engine/autoload/dice_engine.py` ·
## `systems/settlements/settlement_layer_v30.md` · `systems/factions/faction_canon_v30.md` ·
## `systems/world/worldbuilding_v30.md` · v1 [`05`](../2026-08-28-greenfield-systems-suite/05_faction_actions.md) (ARCHIVED)
## Executes: **ED-IN-0201** (Jordan, 2026-08-28, `registers/editorial_ledger_in.jsonl`) — both clauses

**Nothing here is a new primitive.** A faction action is a Post's remit invoked against a Gauge, ranked
by a derivation over an Entity's identity and its holder's form, costing a Gauge, sometimes rolling on
the single-owned kernel. Four stored things, four write leaves, no fifth.

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

| **O-5.7** | `01 §6` point 2's narrowing: *"the `modifiers` argument is reserved for terms genuinely properties of the target"* | this suite's own `01` | Correct as a general rule and **wrong for a contested quantity.** Presence has no single owner: it is a *share* of a place, and the meaningful difficulty is the incumbent's **lead**, not their total. `act.contest_influence` therefore derives its obstacle from `presence_defender − presence_challenger`, which is expressible inside `derive_ob` as an instance-specific modifier and is **not** an actor-advantage leaking into obstacle-space by the back door. §4.1 argues it and states the leverage consequence. **This deletes an object** — the capped σ-space foothold boost an earlier draft of §4.1 carried — rather than adding one |

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
games drown a player. **The seven-plus-one action families below are a strategic *capability* list,
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

**Substrate objects on this page: 8 action rows · 1 per-tier gate · 1 per-post budget · 1 appeal
derivation · 1 contested-influence resolver · 1 flat ceiling. Surface affordances: 1 decision, 1
inspection.** Six-to-one, which is the ratio `00 §2.3` point 4 asks for.

**`05` contributes exactly ONE verb-slot to the game's single-digit budget** — *direct a post's
action* — and it is the same slot whether the post is a national head, a provincial minister or a
settlement governor, because it is the same module. **Everything that looks like breadth is the
`appeal` ranking's job, not the player's.** The eight families are eight registry rows the engine
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

**Truncation is deterministic and consumes no RNG.** When the ceiling binds, the surviving actions are
the highest-`appeal` ones across all tiers, ties broken by §3.5. A ceiling resolved by a draw would put
a random number in the one place a player must be able to reason about.

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

> **Falsifier (the strongest one this page has).** A permutation test: **swap the `ethos` vectors of
> any two factions in the registry, hold every other input fixed, replay a seeded season, and their
> chosen actions must swap exactly.** If they do not, something in the tree is reading a faction's
> identity rather than its data, and that is scripting drift by definition. Load-bearing on the game:
> it is the difference between AI factions with character and AI factions with a script.

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

### 3.5 Determinism, ties, and disclosure

- **Selection consumes no randomness.** It is a `derivation`. A draw here would be the wrong tool for a
  decision and would re-phase every downstream consumer for no gain (P0-2's attributability).
- **Ties break deterministically:** lower budget cost first, then declared registry order. Never a
  draw, and never the *first* rule alone, so a cheap action is preferred to an expensive equal one.
- **Disclosure.** Each term of `appeal` is published **per available action as a band**: the player sees
  that their head strongly favours a martial option on conviction, that the institution mildly
  disfavours it, and that a rival holds some leverage. **The resolved ordering's margin and the
  tie-break are not published.** Publish every input; publish a band; never publish the trigger
  (`01 §8`).
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

> **Falsifier, and it belongs in `01 §6` rather than here** — flagged for that document's author
> rather than duplicated into a second owner. A **declaration-time** check over the descriptor
> registry: for every gauge declared as a `derive_ob` target, `ceiling/2` must leave all four ladder
> bands reachable for the pools that roll against it — i.e. `ceiling/2 < μ_max + 3` where
> `μ_max = 0.4 · POOL_MAX`. It needs no campaign run. **Load-bearing on the game**
> (`CLAUDE.md §0.1` point 5): it is the difference between an action with four outcomes and an action
> with one. On the scales this page assumes for presence it passes; on a 0–100 gauge it fails, which
> is the point of having it.

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
the test the brief sets: each of them is this row with two fields changed, and shipping them separately
would mean five effects tables to keep total and five places for the Partial band to rot.

---

## 5. The action set — eight rows, one shape

An action is a **row, never a branch.** Adding one is a registry edit.

```yaml
- action: <id>
  remit_kinds: [<post kinds whose remit may contain this>]
  tiers: [<rungs at which it is available>]              # NEW (v2) — §1.1
  binds: {<slot>: <registry id>}                          # NEW (v2) — §4.5
  attrs: [<attr_a>, <attr_b>]                             # keys on descriptors.ATTRIBUTES; never literal
  target: <what supplies target_score for derive_ob>
  symbolic_vector: {hierarchical: ±, sacred: ±, instrumental: ±, traditional: ±}
  signal_weight: {<world signal>: <weight>}
  cost: {budget: 1, gauge_deposits: [...]}
  effects: {overwhelming: [...], success: [...], partial: [...], failure: [...]}   # TOTAL over four
```

| family | what it does | shape | `derive_ob` target |
|---|---|---|---|
| **`act.muster`** | raise a unit at a place (§5.2) | **gate** | — |
| **`act.govern`** | deposit into a held place's `acceptance` and `condition` gauges | **U** | the place's own condition |
| **`act.campaign`** | declare a campaign against an adjacent holding (§5.1) | gate, then a declared seam | — |
| **`act.motion`** | raise a motion in the deliberative body on a named subject (`12`) | **DO** | the opposing coalition |
| **`act.treat`** | offer a bilateral agreement — **creates a `treaty` edge with its terms in its tags** (O-5.5; `12` owns the kind) | **SO** | the counterparty's `acceptance` |
| **`act.commission`** | appoint, recall, or attempt custody — routes to `04` | gate / **SO** | per `04` |
| **`act.inquire`** | spend an action to learn (§5.3) | **U** | the concealing party's relevant score, where one exists |
| **`act.contest_influence`** *(v2)* | raise presence at a place you do not hold (§4) | **DO + entrenchment Ob** | the defending institution's presence |

### 5.1 `act.campaign` is a gate over a declared seam, not a stub

Force-on-force resolution is out of this suite's scope, and saying so **with a specified seam** is
different from leaving a hole.

| | |
|---|---|
| **the gate** (here) | the target is adjacent to a held node; a `commander` post is filled; the committed units exist and are assigned to the field |
| **the seam** | `resolve_force(attacker_units, defender_units, place) → Degree` — one call, one return, on the single-owned ladder |
| **the consumption** (here) | the degree drives an Entry Terms fork: on a lesser margin the taken place keeps its arrangements and seeds `acceptance.legitimacy` high; on a decisive one it does not and seeds low |

Its interface is fully specified in both directions, so the caller is complete and testable against a
stand-in, and the seam returns a `Degree` — the same currency every other action consumes — so whatever
implements it cannot introduce a second degree semantics for one event class.

### 5.2 `act.muster` — two economies, separated at birth

Four of four surveyed franchises implement the levy and the professional soldier as **different
economies, not different tiers.** Building one muster now and splitting it later means splitting a
mechanic that has already accreted grounding, effects and goldens; building two channels from the start
costs one extra registry row.

| | **`act.muster.levy`** | **`act.muster.contract`** |
|---|---|---|
| pays with | the place's `accrual.entitlement` gauge | the faction's derived treasury |
| rationed by | how fast entitlement accrues — a property of the place | how much money there is |
| upkeep | none | recurring, larger when assigned to the field |
| quality | bounded by the place's `condition` band | bounded by price |
| consent cost | a deposit into `acceptance.support`, scaled by the unit's quality tier | the same deposit at the same scale |

Recruitment is coercive in both channels: the per-unit consent deposit is the live dial, and separately
and rarely a **gate** — a place whose `acceptance.support` band is at *revolt* supplies no soldiers in
either channel. Scoping the gate to the revolt band is what keeps it from double-counting the dial.
`act.muster` is a **`gate`, not a `d_sigma`**: whether you can afford a unit is a question whose answer
is on the board, and rolling for it is the wrong-engine defect this tree is most prone to.

**Muster raises no aggregate.** It produces a unit record (`12`). Faction military weight is *derived*
from units held; building it the other way — mustering raising the number that gates what mustering can
produce — is a loop with no external term in it at all.

### 5.3 `act.inquire` — information **gates**, it never adds dice

Information determining *which arguments you may attempt* is a mechanic worth having; its hard form —
the wrong choice flatly fails — is a special case bolted into a continuous system, which is scripting
drift. The soft form is already a built primitive. `act.inquire` deposits into an information gauge on
the target, and that gauge's band does exactly two things:

1. **It gates the option set.** Rows declaring `requires_information: <band>` are unavailable below it —
   a gate, on the board, published.
2. **Acting against an uninvestigated target declares a `BandExtension` that vetoes Overwhelming**
   (`dice_engine.py:95`, ED-SC-0032). Your ceiling drops; your odds of Success are untouched.

Neither adds a die, shifts an obstacle, or touches the Partial or Failure boundaries. An extension's
only power is to veto the top band — the return channel is structurally bounded to `3 → 2` — and the
seam refuses undeclared context keys rather than swallowing them.

---

## 6. Resolution — one pool shape, one obstacle owner

Every action here that rolls, rolls the same way.

| element | rule |
|---|---|
| **actor** | the post-holder invoking the module — **never "the faction"** |
| **pool** | `attr[a] + attr[b] + POOL_BASE`, `[a, b]` the row's declared attribute pair, keyed on `descriptors.ATTRIBUTES` |
| **obstacle** | `derive_ob(target_score, target_modifiers)` — E-1 and nowhere else. **In the DO shape, the differential is the `net` and the entrenchment is the `ob`** (§4.1) |
| **modifiers** | σ-space μ-shifts via `sigma_leverage.net_boost`; never extra dice. **One exception, argued and listed at O-5.7:** a *contested* quantity's obstacle derives from the lead, inside `derive_ob` (§4.1) |
| **degree** | `degree_from_net`, unmodified, with an extension only where §5.3 declares one |
| **TN** | never named. `_require_tn7` raises (`dice_engine.py:182`) |

**The pool arithmetic, because P-v turns on it.** Attributes are 1–7, so `attr[a] + attr[b]` spans 2–14
and the pool spans `2 + POOL_BASE … 14 + POOL_BASE`. With `POOL_BASE = 4` — **a shape proposal, the one
bare number on this page, declared in the exported params with this justification attached** — the pool
spans **6–18**, inside the band the continuous engine is calibrated for at both ends. Reachability bar:
*the weakest possible actor on the least-suited pair must still produce a pool inside the calibrated
band.* At `attr = 1, 1` that is pool 6 — satisfied.

**This is also why the pool is one person's score and never an aggregate over a roster.** A
roster-sized pool grows `μ` linearly in roster size while `σ` grows only as `√size`, so `z` grows
without ceiling and the roll becomes decorative for a large faction — and it would put the same action
on two different engines depending on how many people a faction has. **The roster buys actions; it
never buys dice.** That is §2.4's restriction reached from a different direction.

---

## 7. Two constraints binding on every effects table

- **Total over the four bands.** Every action declares an outcome for Overwhelming, Success, Partial and
  Failure, and **no effect is unique to Partial** (P0-3), so a change to the Partial band's width
  degrades the ladder gracefully rather than deleting a mechanic.
- **No Failure branch removes a post or eliminates a faction.** Failure deposits, writes tags and costs
  the budget point. Elimination is only ever the gate closing for want of a candidate, and that is
  recoverable by producing one (§1.2). An irreversible outcome on a routinely-reached roll is exactly
  what P-iv exists to catch, **and a faction takes one of these every season, at every rung.** The
  per-tier gate makes this *more* load-bearing than in v1, not less: there are now more of these rolls
  per season, so a single irreversible branch would fire that much sooner.

---

## 8. What this page assumes about the substrate — J-N and J-O, stated once each

### 8.1 ⚠ J-N — the substrate supplies NO cross-season latency

Verified against the tree by `audit/2026-08-08-world-churn-audit` and reproduced at `01 part 2 §9.3`:
`drain_tick` has zero production callers, `next_tick` **raises `TerminationBreach`** on a non-empty
queue, and `DEFAULT_CASCADE_DEPTH_MAX = 0` is a self-labelled provisional bound. **The guard prevents
cascades outright; it does not schedule them late.** One-hop-per-season latency is not a property this
design has — it is a mechanism someone would have to build.

**What that forbids on this page, concretely:**

| forbidden | the correct shape |
|---|---|
| a contest that "posts a challenge" resolving next season | it resolves **within the tick**, or not at all |
| a multi-season influence campaign carried by an emission | it advances because **presence is a certain way at the accounting boundary** — a gauge read, not a message |
| `fa.gate` reacting next season to a `post.vacant` raised this season | the gate **reads `holder_id`** at the boundary; it does not wait to be told |
| an action whose consequence "arrives later" | its deposits land now and **decay geometrically**, which is the only cross-season channel the substrate has besides reading state |

**J-N is the ruling that would change this.** If it rules for reactive chains, this section is what to
revisit; nothing else on this page depends on the answer.

### 8.2 ⚠ J-O — what here leans on Key *consumption*

`00 §5.1` files J-O: whether the Key substrate deserves promotion from telemetry spine to churn engine
at all, the alternative being an append-only telemetry/causality log with churn driven at the boundary
directly. **Stated so the affected parts stay identifiable if J-O rules the other way:**

| depends on Key **consumption** | survives a "telemetry only" ruling? |
|---|---|
| `fa.gate`'s `consumes: [post.vacant]` | **no** — it becomes a boundary read of `holder_id`, which is what §8.1 says it already is in substance. **One line of contract, no design change** |
| everything else on this page — `appeal` (reads state), the budget (reads a gauge), `act.contest_influence` (reads presence, rolls, deposits), every effects table | **yes** |
| the emission side (`faction.action_declined`, and the action rows' own emissions through the herald) | **yes** as a log |

**This page is nearly robust to J-O**, and deliberately so: the per-tier gate was written as a *state
read* rather than a *Key reaction* precisely because §8.1 says the transport for the latter does not
exist. That is one constraint doing two jobs.

---

## 9. Module contracts

Shape per `00 §7`. Per W-6, every `consumes:` row names what the consumer does with the Key; none is
declared speculatively.

```yaml
- module: fa.gate
  parent: faction_actions
  class: substrate
  scales: [settlement, territory, peninsula]     # v2: no longer [peninsula] — O-5.1
  tier: null                                     # runs at EVERY declared rung; §1.1
  resolver: gate
  remit: []                                      # not invocable; the boundary runs it
  budget: null
  consumes: [{type: post.vacant, from: [pm.vacancy]}]   # rule content: re-evaluates the rung's
                                                        # acting_posts set. See §8.2 — this is the
                                                        # ONE J-O-fragile row on the page.
  emits: [{type: faction.action_declined, terminal: true}]   # carries faction, tier, reason
  state: []
  form: []
  transitions: []
  disclosure: [{of: decline_reason, inputs: published, presentation: exact, trigger: hidden}]

- module: fa.select
  parent: faction_actions
  class: substrate                               # the RANKING is substrate; the player's pick is 10's
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: derivation                           # a ranking over declared inputs; consumes no RNG
  remit: [head, governor, minister, commander, envoy]
  budget: null
  consumes: []
  emits: []
  state: []
  form: []
  transitions: []
  disclosure: [{of: appeal, inputs: published, presentation: band, trigger: hidden}]

- module: fa.resolve
  parent: faction_actions
  class: substrate
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: d_sigma
  remit: [head, governor, minister, envoy, commander]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  emits: []                                      # the herald emits per the resolved row (W-1)
  state:
    - {name: gauge, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: tag,   bucket: tag,   writable: true, owner: substrate.ledger}
  form: []
  transitions: []
  disclosure:
    - {of: pool,     inputs: published, presentation: exact, trigger: hidden}
    - {of: obstacle, inputs: published, presentation: exact, trigger: hidden}

- module: fa.contest_influence                   # NEW (v2)
  parent: faction_actions
  class: substrate
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: d_sigma                              # DO; the UNDEFENDED path is a gate, §4.2
  remit: [head, governor, minister, envoy]
  budget: {gauge: post.budget, cost: 1}
  consumes: []                                   # reads presence at the boundary; §8.1
  emits: []                                      # the herald emits; a band crossing is 07's
                                                 # form.transitioned, not a second emission here
  state:
    - {name: presence.<institution>, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: exposure,               bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: tag,                    bucket: tag,   writable: true, owner: substrate.ledger}
  form: []                                       # 07 owns place.presences transitions, NOT this module
  transitions: []
  disclosure:
    - {of: presence.<institution>, inputs: published, presentation: band,  trigger: hidden}
    - {of: pool,                   inputs: published, presentation: exact, trigger: hidden}
    - {of: obstacle,               inputs: published, presentation: exact, trigger: hidden}

- module: fa.muster
  parent: faction_actions
  class: substrate
  scales: [settlement, territory]
  tier: settlement
  resolver: gate                                 # affordability is a threshold, not a contest
  remit: [head, governor, commander]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  emits: []
  state:
    - {name: accrual.entitlement, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: acceptance.support,  bucket: gauge, writable: true, owner: substrate.gauge}
  form: []
  transitions: []
  disclosure:
    - {of: accrual.entitlement, inputs: published, presentation: exact, trigger: hidden}
    - {of: acceptance.support,  inputs: published, presentation: band,  trigger: hidden}

- module: fa.inquire
  parent: faction_actions
  class: substrate
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: d_sigma
  remit: [head, governor, minister, envoy, clerk]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  emits: []
  state:
    - {name: information, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: exposure,    bucket: gauge, writable: true, owner: substrate.gauge}
  form: []
  transitions: []
  disclosure: [{of: information, inputs: published, presentation: band, trigger: hidden}]
```

**Note what is absent.** No module here declares `form:` or `transitions:` — **this page changes no
entity's shape.** Presence band crossings are `07`'s transition rows, posture is `06`'s, and appointment
is `04`'s. A faction action deposits, tags and spends; it does not reshape the world directly. That
absence is `01 §2.4`'s "grep over one field" staying true, expressed in the contracts rather than
promised in prose.

---

## 10. Property audit

**Scope, honestly.** `fa.gate` and `fa.muster` are **gates**; `fa.select` is a **derivation**. `00 §10`
and the methodology's own rule forbid manufacturing a NERS verdict for a module that does not roll, so
**no N/R/S/E verdict is offered for those three** — their loops and gates are §10.2 instead. The audit
below is of `fa.resolve`, `fa.contest_influence` and `fa.inquire`, which roll.

### 10.1 The five properties, each with the falsifier that would show it wrong

| property | verdict | falsifier |
|---|---|---|
| **P-i** legible odds | **pass, and still the strongest in the suite.** Pool is a named person's two named attributes plus a declared constant; obstacle is the target's score halved; **the DO differential is two published nets minus a published obstacle.** Selection is a published ranking rather than a draw, so a player can read *why this action and not that one* | A test asserting every rolling module's `disclosure:` publishes `pool` and `obstacle` at `exact`, and that `fa.select` publishes every `appeal` term. **If any input to a roll or a ranking is unpublished, P-i is false** |
| **P-ii** uniform leverage | pass, **with one recorded non-uniformity in the correct direction** (§4.1) | A test asserting no module contract declares a `budget:` whose cost is consumed inside a pool or obstacle expression (`01 §5.3`'s falsifier, applied here), **plus**: no action row's modifier reaches the roll except through `sigma_leverage.net_boost` **or** `derive_ob`'s declared instance term, and no row declares both for the same quantity. A modifier applied twice through two channels — the defect the two-channel draft of §4.1 would have shipped — falsifies it |
| **P-iii** bounded, monotonic | pass, **with two loops stated and both gains unmeasured** (§2.3, §4.4) | `01 §5.1`'s declaration-time check — `rest + max_seasonal_accrual/λ ≤ ceiling` — applied to `presence.<institution>` with `act.contest_influence` counted among its depositors. **A controlled campaign pair on `tools/balance_oracle.py` showing presence share diverging without bound falsifies it** |
| **P-iv** graded, recoverable | pass | A test asserting every action row's `effects` map is **total over the four `Degree` members** and that **no `failure` branch revokes a post or removes a faction**. A row with a Partial-only effect, or an empty Failure branch, falsifies it |
| **P-v** right engine | pass | Three questions, three tools: selection is a **derivation** (a decision, not an uncertainty); affordability and eligibility are **gates**; contested outcomes are `d_sigma` at pools 6–18. **A test asserting every `resolver:` matches `00 §7`'s table** — in particular that nothing determinate rolls. `fa.muster` declared `d_sigma` would falsify it |

**N** — under ED-IN-0201 this is the layer the ruling is *about*; it is not optional. No roll here is
redundant: every `d_sigma` module resolves something genuinely uncertain and everything determinate is a
`gate`. **R** — the extremes are the weakest possible actor (pool 6, inside the calibrated band) and the
largest possible faction (flat ceiling; pool unchanged, because pools are person-scale at every rung).
**S** — the same pool shape, the same obstacle owner and the same four primitives as `04` and `08`; **a
faction action at the peninsula rung and a settlement verb are the same object at different rungs**, which
is what per-tier makes literally true rather than merely analogous. **E** — eight rows, one contract
shape, **no per-faction branch anywhere**, and five would-be verbs collapsed into one binding slot (§4.5).

### 10.2 The non-rolling modules — loops, gates, and what each reads

| module | kind | reads | bound |
|---|---|---|---|
| `fa.gate` | gate | `post.holder_id`, `post.remit`, the declared rungs | none needed; it is a predicate. **Recoverable by construction** (§1.2) |
| `fa.select` | derivation | `faction.identity.ethos`, holder convictions, world signals, `Leverage` tags | `custody_bias` clamped to `±RELATION_SHARE_MAX · structural_range`; no other term is unbounded because each is a bounded projection |
| `fa.muster` | gate | `accrual.entitlement`, treasury, `acceptance.support` band | the entitlement accrual rate is a property of the place; the revolt gate is a hard floor |
| the budget | derivation over gauges | `post.budget` per held post | `FACTION_ACTION_CEILING`, flat and non-scaling (§2.2), **with a stated reachability bar** |

### 10.3 The three claims on this page that are weakest, named rather than buried

1. **`FACTION_ACTION_CEILING`, `POOL_BASE`, `SHORTLIST_K`, `d₁…d₃` and `e₁…e₂` are
   shape proposals, not ledger constants.** None is cited to a `PP-NNN` or an `ED-NNN`, because none has
   one. They are declared with justifications and reachability bars so that tuning them is an act with a
   named target, not a preference.
2. **Both loops' per-cycle gains are unmeasured** (§2.3, §4.4) and are stated as unmeasured. They are
   campaign-reachable, so the instrument exists; running it with a control is work this page does not do.
3. **The DO-plus-obstacle shape is the page's most contestable design call** (§4.1). It is argued, listed
   at O-5.4, and it is *reversible in one line*: dropping `net_d` from the differential returns the SO the
   delta spec named, with every other part of the action unchanged.
