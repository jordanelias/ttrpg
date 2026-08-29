# 13 — Material Life: Production, Prices, and the Stakes People Fight Over

## Status: PROPOSED (2026-08-29) — a from-scratch design. Nothing here ratifies on merge.
## Lane: IN (cross-cutting) · Composes on: `01_substrate.md` §4 (Hearth, Settlement), §5.2 (Dispensation);
## `04_hearth_and_community.md` §1.2 (the larder), §7–§8 (community roster, `contest`);
## `06_down_stroke.md` §1 (`PriceTerm`, `LevyTerm`, `BlockadeTerm`)
## Method: derived, not adapted. No prior design document, ruling, or existing module constrains it.

**What this document owns, and what it does not.** `04` already builds the larder's mechanism —
`mouths`, `draw`, `margin`, the bands. `06` already builds `PriceTerm` as a dispensation delta. Neither
says what a holding *produces*, what a price *is* before anyone issues a dispensation about it, what a
settlement's stake genuinely is, or why a shortfall today can trace to a decision decades gone. That is
the layer this document supplies: the minimum material substrate that makes the political layer's
prices, levies, and stakes *about something real*. This is a politics game. Every object below exists
because a political act needs it to bite on, and none exists to be simulated for its own sake.

**Reading key, inherited.** Every new object is *producer → carrier → consumer* plus an N-line.
Anything without one is in §11, refused.

---

## 1. The larder, restated as an interface

Owned by `04` §1.2. Restated here only so this document is self-contained:

```
mouths(h)  = Σ appetite(p)                    stores(h) += draw(h) − mouths(h)
draw(h)    = Σ yield(H, season) − Σ levy(d,h)  margin(h)  = stores(h) / mouths(h)
```

Bands run Provisioned → Sufficient → Thin → Hungry → Failing, published in full with their inputs, never
with the trigger point that separates one band from the next. A shortfall does not fire an event — it
raises `need(p, subsistence)`, which outweighs stance entirely once it exceeds 1.0, and a person with no
office reaches for one of five channels: requisition kin, petition, take an opening, migrate, or commit
to a rival proposition. `04` builds all five. **What this document adds is what feeds `yield(H, season)`
and `levy(d, h)` in the first place** — production, and the price a levy is denominated in.

---

## 2. Production: a settlement type is a production profile, derived

The setting names eight settlement types and three 0–5 stats (Prosperity, Defense, Order). Adopting
them because they exist would be exactly the surplus the E-ratio exists to catch. Here is the
derivation, kept to the minimum a holding needs.

Every holding `H` a hearth draws on belongs to a settlement, and a settlement type is nothing but which
goods its holdings can produce and how many mouths it concentrates that no local holding feeds:

| Type | produces | consumption load | derivation |
|---|---|---|---|
| **Town** | grain, wool, fodder | low, rural | the base agrarian holding — most `H` in the game are Town holdings; this is where `yield()` is closest to its own `base(H)` |
| **City** | craft goods (Kettlemakers' Row's kettles, cloth), guild dues | high, dense | few holdings, many mouths — the gap between what a City makes and what it eats *is* its market, and it is why City prices move first |
| **Seat** | nothing | very high (court, garrison) | a Seat owns no holdings of its own; its Prosperity is entirely what tithe and levy it can pull from elsewhere — the derivation for why a Seat's office-holder fights hardest over granary allocation (§3) |
| **Port** | fish, transshipment | moderate | the node where a trade route's two prices are realized in the same market — where forestalling and smuggling (§4) actually happen |
| **Fortress** | nothing | high, concentrated | a pure sink; every mouth is imported, so a Fortress under blockade starves faster than any other type |
| **Cathedral** | tithe-in-kind, glebe land | moderate | its "production" is administrative collection, not growth — its Prosperity tracks the health of every parish feeding it, not its own soil |
| **Mine** | ore, silver | high, few local holdings | `base(H)` for a mine holding declines with ore grade — §5's first slow fuse |
| **Outpost** | none, or one small holding | low | garrison plus a handful of hearths; exists to hold ground, not to feed anyone |

**Prosperity, Defense and Order are computed bands, never stored dials** — the same anti-gauge
discipline `01` §6 already applies to unrest and loyalty, extended to the setting's own stats:

```
Prosperity(s) = band( Σ_{h∈s} draw(h) − Σ_{h∈s} mouths(h) )        the settlement-wide margin, on demand
Order(s)      = band( norm(s, "the office-holder's authority is legitimate") )    04 §5's norm formula
Defense(s)    = band( capacity(garrison, s, "hold the wall") − max_f density(f,s)×threat_weight(f) )
                                                                     04 §8's capacity, 01 §1.3's density
```

A flood, a blockade, or a declining ore seam reaches people because each is a change to exactly one
term already inside these formulas — `base(H)` for a permanent loss, `season_factor(territory)` for a
temporary one — and every hearth drawing on the affected holding feels it through the same `yield()`
line `04` already wrote. Nothing new resolves the shock; the shock just changes an input.

- **Cut the derivation and you lose** the causal chain between one person's hunger and the number a
  duke reads off a map. Keep Prosperity/Defense/Order as stored dials instead, and a distant political
  decision can move the dial directly — the exact severance a down-stroke exists to prevent.

---

## 3. The settlement stake

The settlement rung's stake — the granary, the market's stalls, the levy's exemption — is genuinely
zero-sum because feeding one claimant with it means not feeding another this cycle. The granary is the
worked case:

```
granary_stock(s, cycle) = Σ_{c ∈ communities(s)} tithe_in_kind(c, cycle)          — 06's LevyTerm proceeds
```

Allocated at a standing date every settlement carries alongside the tithe reckoning: **the granary
opening.** The allocator is the settlement's office-holder — praefect, magistrate — and the mechanism
is `04` §8's `contest(settlement, granary_stock, claimants)` verbatim, claimants being the communities'
factions.

**The allocation does not divide.** `score()` ranks the claimants; the office-holder allocates the full
stock to the highest-scoring claimant *first*, before the next claimant sees a single measure. That
exclusivity — not a percentage split — is what makes "the granary opens for the hamlet or for the Row,
never both" a fact a named person did, rather than an outcome an algorithm smoothed over evenly. Any
claimant left unfed carries its mouths-deficit straight into its hearths' own `need()` computation
(§1) — no special crisis object, the ordinary relief channels apply.

- **Cut the settlement stake and you lose** the reason a hamlet and a guild ever fight at that rung at
  all — `contest()` would have nothing real to be about.

---

## 4. Prices: the down-stroke's medium before anyone decides anything

`06` owns `PriceTerm` as a dispensation *delta*. Underneath it there has to be a price a dispensation
multiplies:

```
price(good, s, season)    = base_value(good) × scarcity(good, s, season)
scarcity(good, s, season) = demand(good, s) / supply(good, s)

demand(good, s) = Σ_{h∈s} mouths(h) × diet_share(good)
supply(good, s) = Σ_{H∈s} yield(H, season)  +  Σ_{routes r → s} import_flow(r, good, season)
```

Nothing here is stored; it recomputes each season exactly as `margin()` does. Grauwald's salt is dear
not because a duke decreed it (that is `06`'s `PriceTerm`, layered on top) but because Grauwald's own
coastal holdings never produced salt and its hamlets draw on the same coast Duke Vaynard's blockade can
cut. Two settlements differ in price the instant their production and mouths differ — which is every
season, by construction.

**Scarcity propagates along a route because a person decides it's worth carrying, not because a
pathfinder finds a path.** `import_flow(r, good, season)` is the sum of individual acts, each a person
with capability and presence (or a Knot) at both ends of `r` running exactly `06`'s smuggling EV:

```
EV(carry good, r) = (price(destination) − price(origin) − transport_cost(r)) × volume(person)
                     − p(interception) × penalty
```

positive EV *is* the run — legal carting when it crosses no boundary, smuggling when it crosses a
`BlockadeTerm` or evades a `LevyTerm`. One formula, two labels, exactly as `06` already treats it.

**Forestalling is the one new act.**

```
forestall(person, good, s) — requires presence where s's yield would otherwise reach market or
   granary, and stores(hearth(person)) sufficient to buy it outright. Removes the intercepted
   yield from supply(good, s) this season; adds it to person's own stores.
```

It is witnessed like any act (`04` §4.1's judging set), and it is high-δ: the setting's own moral
economy reads it exactly as it read the historical millers-and-forestallers-first crowd, and the
judging set deposits a strong, publicity-scaled negative stance the instant it is caught.

**Hoarding needs no new mechanism at all.** A hearth simply performs no release act; `stores`
accumulates by default. Its only cost is exposure — if a hungry neighbour's claim about a Provisioned
hearth reaches anyone, `witness`/`tell` carries the grievance, unchanged from `01` §3.

- **Cut the price formula and you lose** every reason a smuggler's run, a forestaller's hoard, or a
  neighbour's charity is worth anything specific — every material fact in the game becomes a flavour
  adjective rather than a number a person can act on.

---

## 5. The slow fuses

Two multi-decade hidden variables, each silently dooming a different settlement seasons later.

**Ore grade — Duchess Inge Baralta's silver mine.**
```
base(H_mine) −= depletion(H_mine)     every season, small — never published (§1's own rule:
                                       bands published, trigger points never)
```
For a decade the mine has fed Inge's counter-armament levy against a nominal `base`. Nobody publishes
the depletion rate; it is discoverable only by investigation (T9) — someone inspecting the seam, or an
accountant noticing `draw()` trending down against a flat formula. When it crosses the level that
funds her levy, her counter-armament and the Baralta Crown Claim it finances stall in the same season a
mine-town hearth three rungs away — who has never heard of the Crown Claim — files a subsistence
petition over wages that quietly halved.

**Siltation — Hafenmark's harbor channel.**
```
transport_cost(Hafenmark ↔ sea) += silt_accrual     every season, small, uncompensated unless a
                                                      dredging LevyTerm is actively funded
```
Hafenmark's Parliament voted down the last dredging levy a generation ago, as a popular tax-relief
measure at the time. Silt accrual folds invisibly into `transport_cost` until a storm (a bad
`season_factor` roll) triggers a channel closure: `transport_cost` becomes effectively infinite for a
season, and a route half the peninsula's grain relies on (§4's `import_flow`) severs exactly when a
famine elsewhere (§6) needs it as a relief channel.

- **Cut the fuses and you lose** the shape this whole exercise exists to recover from per-tick
  simulation: a choice at one settlement, decades cold, silently deciding what a different settlement
  can do this season.

---

## 6. Famine and plague, as politics

**Famine.** Whether a settlement survives a harvest collapse is decided by §3's granary — a settlement
whose `granary_stock` covers the deficit survives it as an administrative act; one whose stock does not
is where the "never both" priority ordering turns lethal. But an earlier ideological precedent can
foreclose the obvious fix. When Almud opened trade via Schoenland, it ratified a standing `OrdenanzaTerm`
scoped to the whole duchy — call it the Almud Free Bond — prohibiting the Crown from fixing grain
prices or compelling private sale below market inside Almud's ports, to make the Schoenland trade
attractive. Dispensation terms persist until countermanded (`01` §5.2). Two generations later, when an
Almud harvest fails, the Praefect's `opening_set` for emergency relief is missing the obvious lever —
compelled requisition from forestallers — because it would first require countermanding a Province-rung
term he has no unilateral office to touch. King Almud Almqvist is not the villain of a famine he never
foresaw; the constraint is real and nobody chose it twice.

**Plague.** The vector is a governance action, not a die roll. A garrison captain holding a Locked Zone
perimeter is ordered to redeploy men to reinforce Baralta's counter-armament (the same levy §5's mine
funds). The vacated post's quarantine inspection on incoming Schoenland grain ships lapses. A Niflhel
dockworker crew, its own larder Thin (§1), takes the resulting opening: wave the ship through for a
bribe. Spread reuses the community rung's own gossip machinery rather than inventing a new model:

```
exposure(p) = Σ_{loci where p was co-present with an infected person} venue_factor(locus)
                                                        — 04 §4.1's publicity table, unchanged
```

the same numbers that carry gossip carry contagion. **The response that ends the outbreak manufactures
the next crisis without any new mechanism:** the office-holder cordons the settlement with an ordinary
`BlockadeTerm` (`06` §1). The cordon that saves lives also zeroes every route's `import_flow` (§4);
prices spike; the settlement's own granary becomes the only relief; and the same office-holder who
ordered the cordon must now run §3's exclusive allocation under maximum scarcity — this time with his
own decision as the proximate cause.

- **Cut the governance-action vector and you lose** the whole point: disease becomes weather, a random
  table with no name attached, exactly the null this document exists to refuse.

---

## 7. Debt, dues, and obligation

```
arrears(hearth, creditor, obligation) += owed(cycle) − paid(cycle)     at every standing date,
    held as a claim in the CREDITOR's ledger, deposited by witnessing the reckoning
```

Bound to real institutions: the Church tithe (the Dicastery of Temporal Affairs' `LevyTerm`), guild
dues (the Kettlemakers' Row dues reckoning), a lord's rent on a holding, tribute under a `TreatyClause`.
At `arrears ≥ threshold(institution)` — the Church tolerant for several cycles, its pastoral stance
entering `04` §6's δ term as a genuine positive; a guild or a lord tolerant for one or two — the
creditor's `opening_set` gains `distrain(creditor, debtor)`, which is `04` §3.1's reclaim act, run by a
creditor instead of a landlord: below entrenchment 0.5 it is administrative, at or above it the
debtor's neighbours draw the same "we're next" inference. For the Church specifically the alternative is
`ExcommunicationTerm` (`06` §1) — stripping Church-conferred marks, which costs a Crown-Latinate burgher
far more than a Southern Einhir hearth already thin on Church penetration, an asymmetry produced by one
threshold, not a caste rule.

- **Cut arrears and you lose** any reason a guild ever expels a member or the Church's patience reads
  differently across castes — no material teeth behind any institution's demand.

---

## 8. The clean off-ramp

Almost every mitigation above writes a debt, a grievance, or a precedent that seeds the next problem.
One act does not:

```
settle_in_full(hearth, creditor) — pay owed(cycle) + arrears in stores, before the reckoning, at
    the going price (§4). Effect: arrears → 0.
```

A reckoning paid on time is not unusual, so `04`'s judging set never fires on it — no stance deposit, no
inference drawn (unlike distraint, which is exactly what makes neighbours conclude they're next), no
dormant claim left banked. It resolves the material problem — this specific obligation, permanently —
and plants nothing. **Its cost is real and immediate**: `stores(h) -= owed+arrears`, which can itself
push `margin(h)` toward Thin the same season, and it is gated by whether the stores exist at all — so it
is unavailable to exactly the hearths that would most want it. That gating, not a hidden fee, is why it
does not dominate (§10).

- **Cut it and you lose** the one arm every doom-loop fork needs to be checkable against: without a
  genuinely clean resolution on the table, R has nothing to compare the compounding options to.

---

## 9. What is refused

- **A full commodity market** (every good, every settlement, simulated continuously). What dies:
  nothing — §4 prices every good only where a political act makes it matter this scene, at zero
  standing cost. Running a market for goods nobody is fighting over is state nobody reads.
- **A supply-chain graph** (ore→tool→plow→grain). What dies: nothing a player can act on — this design
  has one production stage and one transformation anyone cares about, §4's `import_flow`. No throughline
  asks whether the smith had charcoal.
- **A currency system.** What dies: the flavour of coin. Every formula above uses the same `stores`
  scalar the larder already banks in mouth-seasons — the stake was never "how much money," it was
  whose mouths get fed, and a second unit needing conversion has no throughline reading it.
- **A per-good ledger** (tracked units of salt, grain, ore). What dies: nothing — supply/demand and
  arrears are scalars recomputed from production and consumption; no act here asks "which forty units."
- **A trade-route pathfinder.** What dies: nothing a player experiences — `import_flow` is one person's
  EV check on a route *they* already have capability or a Knot on. Routing is a fact about who a person
  knows, not a graph search — an algorithm optimizing a route nobody asked a person to walk violates T4
  in the tooling layer.

---

## 10. The R-criterion check

| Fork | gain shape | cost shape | verdict |
|---|---|---|---|
| **Hoard vs. forestall/sell** | Hoard: flat insurance value, never decays (a bad roll can land any season). Forestall: one-time differential that *closes* as more carts run it (decaying gain). | Hoard: contingent on being witnessed, then durable grievance. Forestall: witnessed at high δ every time, durable and repeat-compounding grievance. | Not dominant either way — hoarding is the safer default; forestalling pays only as a rare, exposed exploitation. |
| **Pay the tithe vs. evade** | Evade: same-size stores kept each cycle (constant per-cycle gain). | Evade: arrears compounds toward the distraint threshold; each further evasion is bought at rising risk (compounding cost against flat gain). | Evade is correctly not dominant. §8's off-ramp is what keeps this from being a pure doom-loop: at any point the compounding cost can be zeroed outright, at a real material price. |
| **Invest levy income: granary vs. wall** | Granary: continuous, compounds forward by reducing future §6 contests and the grievance they seed. Wall: a step function — inert until a hostile faction's density crosses the threshold it was sized against (`01` §5.1), then decisive. | Both cost the same forgone alternative investment. | Neither dominates — they hedge different failure modes on different clocks (subsistence vs. coercive), which is a real choice, not an oversight. |

---

*No object in this document introduces a second resolver, a stored aggregate, a per-good ledger, or a
decision function that reads world state. Every new formula is a read over persons, holdings, and
claims that already exist in `01`, `04`, and `06` — the same discipline this document asked of the
substrate it composes on.*
