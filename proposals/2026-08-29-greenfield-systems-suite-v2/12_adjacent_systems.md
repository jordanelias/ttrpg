# 12 — Adjacent systems

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md) ·
## [`01_substrate_primitives_part2.md`](01_substrate_primitives_part2.md) · v1
## `proposals/2026-08-28-greenfield-systems-suite/09_adjacent_systems.md` (ARCHIVED) + its `ARCHIVED.md` ·
## `engine/cross_scale/combat_bridge.py` · `systems/npcs/npc_relational_graph_v30.md` (PP-724) ·
## `tests/valoria/test_engine_does_not_import_systems.py`

Four things the brief's eight named systems each reach for and none owns: what happens when a post
falls vacant at the top, what a faction's armed force actually *is* and how the ground under it
matters, how a treaty is one object instead of two, and where motions come from. v1 built the first,
second and fourth; this document carries them across the primitive-layer changes and adds the third
and the treaty redesign change E requires.

## Overrides

| # | What | Tier | Why |
|---|---|---|---|
| **12-O1** | v1 `09 §4`'s "wrapper layer" section (its own `composition_roles` YAML, phase table, W-1…W-4) | this suite's own v1 | **Dropped, not re-specified.** Fully superseded by `01 part2 §9`'s herald (W-1…W-6, same phase placement). Restating it here is the duplication `00 §1`'s corollary forbids — cited by section number in §5 below, nowhere re-authored |
| **12-O2** *(confirmed, not overridden)* | PP-724's six-kind edge taxonomy, re-weighed under the 2026-08-29 authority amendment that lifted "must use" to "weigh on merit" | held finding, re-checked | Checked against this document's two live needs — a treaty state machine and a terrain coefficient table — and against the Knot test case (`01 §7.3`). Neither needs a seventh kind. **Kept because the six-plus-two-extensions still expresses everything §4 needs, not because instructed to** |
| **12-O3** *(confirmed, not overridden)* | the `combat_bridge.py` path seam, re-weighed under the same amendment | held finding, re-checked | §3 prices the alternative (widen the seam) against the shipped design (an IN-side coefficient) explicitly, on cost and blast radius. **Not widened, on merit — the comparison is argued, not assumed** |

---

## 1. Succession and collapse — carried forward, unchanged in mechanism

v1 `09 §1` designed this fully and it survives the critique untouched; nothing about the seven changes
touches a claim contest. Restated at the level the primitive-layer changes actually affect:

**The gate.** `substrate.post`'s `holder_id = None` (`01 §4.1`) closes ED-IN-0201's gate at the seat
that fell vacant. **v2 delta:** the gate is now checked **per tier** (`01 §4.1`, `05 §3`) — a faction
missing its national head still acts locally through whatever tier posts it retains. Succession is
triggered per vacant post, not once per faction.

**Two paths**, unchanged from v1: `designation` (outgoing holder's declared successor, gated on
`pm.candidates`) or `claim-contest` (below). Which a faction uses is data on the faction, and changing
it is itself an action leaving a `Precedent` tag.

**The claim contest** — a genuinely two-sided `d_sigma`, shape **DO**, reading the margin between two
nets rather than either against an obstacle:

| margin (`net_a − net_b`) | outcome | deposits |
|---|---|---|
| **≥ 3** | decisive | winner takes the post; loser: `Grudge` + `standing` down |
| **[1, 3)** | contested | winner takes the post; loser keeps a durable `Leverage` tag on it (`04 §8`) — custody without office |
| **< 1** | split | winner fills the post; a `Precedent` tag records the unresolved claim; loser's faction-edge disposition deposits sharply down; loser is a live claimant again next vacancy |

This reads the **single-owned four-band margin ladder** (`00 §5`, Jordan 2026-08-14) collapsed to three
narrative outcomes by merging Partial and Failure into `split` — **P0-3 compliant by construction**,
since nothing here fires on Partial *alone*: split is triggered by the union of the two lower bands, not
by isolating the window between them.

**J-N, named explicitly.** A claim contest can span the seasons it takes claimants to gather support
before the roll — and it does so by **reading state at each accounting boundary**, never by an emission
scheduled to land later. There is no cross-season carry in the substrate (`01 part2 §9.3`): a vacancy
persists as an ongoing `holder_id = None`, re-evaluated fresh every season; nothing about the contest is
"queued for season t+2." **This is the one design fact about succession this document adds to v1 — the
old text simply consumed `post.vacant` and emitted `post.granted` without saying whether the process
could take more than one tick, and now it says so.**

**J-O, named.** `ad.succession` `consumes: [{type: post.vacant, from: [pm.vacancy]}]` — a genuine Key
consumption. If J-O rules for telemetry-only, this row becomes a boundary read of
`post.holder_id is None`, per the already-declared table at `01 part2 §9.4`. Nothing else about
succession changes under that ruling: the gate, the bands and the deposits are all state reads and
gauge/tag writes already, none of them Key-driven.

**Collapse**, restated because it is the same mechanism as v1 `09 §1.3`: a faction fails by degrees, no
detection routine, no elimination check, and the head post's demand always resolves at the seat node,
which cannot be lost.

---

## 2. Units — now a full Entity, and the personnel↔battle seam

### 2.1 What changed and why

v1 modelled Unit as a bespoke `ad.unit` module with its own state rows and a bare `kind`/`assignment`
field pair. **Change A applies to every entity kind, not only person and place**, and `00`'s roster
already lists `unit` as one of the **six** entity kinds with a declared identity/form split
(`01 §1.1`):

| | identity (immutable) | form (transitions only) |
|---|---|---|
| **unit** | `home_node`, `raised_season` | `unit_kind`, `assignment` |

So `unit_kind` and `assignment` are no longer free fields a module writes — they move through
**declared form transitions**, gated, emitting, and hysteresis-bound where reversible (`01 §2`). This is
the concrete instance of change A's loss statement (`00 §4.3`): without it, a unit's shape would be
fixed at muster.

```
Unit
├── entity_id   : str          identity: home_node, raised_season
├── form        : {unit_kind, assignment}      ← via transitions only
├── gauges      : {size, discipline, experience}   ← owned by ad.unit (§2.4)
├── tags        : [Precedent, …]
└── posts       : [commander]
```

Muster (`05 §6`) still produces the entity; without one, muster would write an aggregate directly, and
an aggregate has no setter (AU-1).

### 2.2 Assignment: field ↔ garrison — a tag-gated reversible pair

Four of four surveyed franchises treat garrison-versus-field as the same pool wearing a different
assignment, never a separately-raised troop type — carried forward from v1 `09 §2.2` unchanged.
`assignment` does three things: changes which resolutions the unit participates in; contributes to its
node's `condition.defense` gauge while garrisoned; changes the loss consequence (a garrisoned unit is
lost with its node, a field unit is not).

**The transition is order-gated, not gauge-threshold-gated** — there is no continuous quantity climbing
toward a boundary here, only a commander's order. `01 §2.2`'s row shape still requires a hysteresis band
on any reversible pair, and `01 §2.3`'s `H_MIN` arithmetic assumes a scalar gauge crossing a threshold in
both directions, which this is not. **The pattern this document uses for every such case:** when the
gate is tag-existence rather than gauge-crossing, `band` is declared `null` and the required `dwell` is
supplied by the triggering artifact's own lifetime rather than a second parameter. Here that artifact is
the emitted `form.transitioned` Key itself: the gate for reversing an assignment reads whether **this
unit's own most recent `form.transitioned` on the `assignment` field is at least `D` seasons old**
(a query over `causes[]` history, not a stored counter) — auditable, no new field, no oscillation
cheaper than `D` seasons of standing orders.

```yaml
transition: unit.field_to_garrison   entity_kind: unit   field: assignment
from: field   to: garrison
gate: remit-holding commander orders it (§4.4-style — a post action, not a roll)
cost: {gauge: post.budget, cost: 1}
emits: form.transitioned   reversible: true
hysteresis: {band: null, dwell: 2}   # illustrative — the "tag-gated" pattern above, not a ledger constant
class: substrate
---
transition: unit.garrison_to_field    # mirror, same dwell
```

**Open fork, named rather than decided** (carried from v1 `09 §2.2`): whether a garrisoned unit may be
ordered offensively without first reassigning. Not this document's call.

### 2.3 Unit kind — a gauge-threshold reversible pair, the ordinary case

A second, illustrative form field showing the ordinary (gauge-gated) hysteresis case for contrast with
§2.2's tag-gated one: `unit_kind: levy → regular` on sustained `discipline`, reversing under sustained
privation.

```yaml
transition: unit.levy_to_regular   entity_kind: unit   field: unit_kind
from: levy   to: regular
gate: discipline ≥ θ↑ (illustrative; θ↑ set in unit.discipline's descriptor row)
reversible: true
hysteresis: {band: "θ↑ − θ↓ ≥ H_MIN(discipline)", dwell: 1}   # per 01 §2.3's formula, numbers TBD by the descriptor row
---
transition: unit.regular_to_levy   entity_kind: unit   field: unit_kind   # the mirror — §6's module
from: regular   to: levy                                                  # contract already names it
gate: discipline ≤ θ↓ (same descriptor row; θ↓ < θ↑, the same band §2.3's hysteresis declares)
reversible: true
hysteresis: {band: "θ↑ − θ↓ ≥ H_MIN(discipline)", dwell: 1}   # the identical declared band, both directions
```

**The reverse row, named rather than left implicit.** An earlier draft declared `reversible: true` and
a two-sided hysteresis band on `unit.levy_to_regular` alone, then listed `unit.regular_to_levy` in
§6's `transitions:` with no row defining it — a name with no gate anywhere, the exact defect this
suite's own `references/form_registry.yaml` discipline exists to catch at load. The mirror above is
`unit.field_to_garrison`'s own pattern (§2.2: "mirror, same dwell") applied to the gauge-gated case:
same band, same dwell, opposite direction, `θ↓` supplied by the same descriptor row `θ↑` already names.

Both `θ↑`/`θ↓` and `discipline`'s `λ`/`rest`/`ceiling` are shape proposals belonging to this document's
own `unit.discipline` gauge (§2.4) — no number here is a ledger constant.

### 2.4 The commander, and the personal→mass leverage rule — both carried forward unchanged

`unit.commander` is a `Post` (kind `commander`, closed-at-six roster, `01 §4`); the holder supplies
attributes to the battle model. That is the entire personnel↔battle seam. **Q-2** is designed here as a
**gate**, not a penalty, matching ED-IN-0201's other two clauses: no commander, no campaign for that
unit. `00 §5.1` lists this among the rulings this suite executes and Q-2 is filed there as the reading
taken, unchanged from v1.

**This gate stacks with, and is independent of, the multi-scale gate `05 §3` adds.** Declaring a
campaign at all needs a post at the acting tier (`01 §4.1`'s v2 delta); ordering a *specific* unit into
it needs that unit's own commander post filled. Neither substitutes for the other.

**The personal→mass leverage rule, verbatim from v1 `09 §2.4`:** *a personal-scale effect on a
mass-scale outcome is expressed as a fraction of the affected unit's own size or cohesion — never a
flat amount, never a flat obstacle shift.* A commander's quality scales `discipline`, per-unit and
therefore per-capita. §3 below is this same rule extended from *who* commands to *where* the fight
happens.

Two-tier defeat severity is carried forward unchanged: a unit on the winning side takes a `discipline`
deposit with `experience` intact; a unit whose side breaks takes the harsher outcome. Losing a battle
and losing an army stay different events.

### 2.5 `unit.size`'s decay is an argued choice, not the gauge primitive's silent default (A-F13)

Every Gauge decays geometrically toward a declared `rest` (`01 §5.1`). Leaving `unit.size`'s `λ`/`rest`
unstated, as an earlier draft of §2.1 did, ships **unattended attrition nobody designed** — an army
that shrinks every season whether or not anyone touches it. That is exactly the test `01 §1.3` used to
move capability out of the gauge shape in the first place: *"an attribute decaying toward a rest value
means skills rot every season, which is a different game."*

**Capability failed that test; `size` does not, and the difference is the argument an earlier draft was
missing.** There is no in-world reason a soldier's *competence* should erode absent practice — that is
why `discipline` and `experience` stay gauges but `capability` moved to form (`01 §1.3`). A unit's
*raised strength* is a different quantity: attrition without supply is a real, wanted military
dynamic — a standing levy nobody pays, feeds or reinforces does bleed strength to desertion and
disease, independent of any battle. So the decay is **kept, and made a decision instead of a default**:

```yaml
gauge: unit.size
floor: 0
ceiling: <raised strength, per-unit>                     # SHAPE PROPOSAL, this document's own
lambda: 0.03            # SHAPE PROPOSAL — slow: an unsupplied unit halves toward rest over roughly
                        # 23 seasons, not one. Peacetime attrition, never a battle result
rest: 0.6 · raised_size  # SHAPE PROPOSAL — the standing cadre that does not walk away: veterans,
                        # officers, the locally-rooted levy. Never zero — a unit hollows out toward
                        # its durable core, it does not evaporate for want of a season's pay
```

**What this decay is not.** Battle losses are not this gauge's decay — they are the `overwhelming`/
`success`/`partial`/`failure` bands' own explicit deposits, landing through leaf 1 exactly like any
other combat effect, unchanged from §2 above. The geometric term is the *only* thing that moves `size`
when nobody musters, reinforces, or fights with the unit, and it runs at a rate an order of magnitude
slower than `discipline`'s or `experience`'s own decay.

> **Falsifier.** A declaration-time test asserting `unit.size`'s `λ` is present, `> 0`, and at least
> 5× smaller than both `unit.discipline`'s and `unit.experience`'s own declared `λ` — the arithmetic
> check that this is argued as slow peacetime bleed, not silently inherited from whatever value the
> registry's other gauges happen to use.

---

## 3. Terrain into the force seam

### 3.1 The seam, read before designing against it

`engine/cross_scale/combat_bridge.py` is the sole bridge from the campaign layer to the canonical
personal-combat resolver, and it is a **declared path seam**: `PATH_SEAM_ALLOWED = {'cross_scale/
combat_bridge.py'}` (`tests/valoria/test_engine_does_not_import_systems.py:212`, asserted a floor of
exactly that one entry at `:288-292`), shrink-only, default-OFF (`combat_bridge.py:77-80` — the sys.path
mutation and `combatant`/`wrapper` imports are lazy, memoized, first-use-only). The module's own
docstring is explicit about the lane boundary: *"this module and everything under `engine/cross_scale/`
may NOT edit anything under `systems/combat/` — a wrapper-side need is filed to the PC session, never
patched here"* (`combat_bridge.py:12-16`).

Today the bridge derives **exactly one** field per side — `history`, from a faction's aggregate `Mil`
stat (`combat_bridge.py:103-111`, `f.Mil` at `:109`) — and constructs `Combatant(label=fid,
history=history)`, leaving every other field at the class's own default. `derive_parties(ctx, world)`
reads `ctx['factions'] = (fid_a, fid_b)` (`:114-128`); nothing about terrain is consumed anywhere in the
bridge today.

**⚠ Verified, and stronger than "unconsumed": nothing in production constructs `ctx['factions']` at
all.** A sweep of every writer of that key across `engine/` and `systems/` finds exactly two
construction sites, both tests, both the same hardcoded pair:
`engine/tests/test_pipeline_reach.py:277,756` and `engine/tests/test_combat_bridge_seam.py:44` et seq.
— `context={"factions": ("Crown", "Church")}`. `scene_dispatch.py:241` reads it unconditionally
(`fid_a, fid_b = ctx.get("factions")`) and `:237` carries a declared `"context-derivation gap"` reason
string for exactly the state a live campaign is always in. `systems/combat/combat_flow_skeleton_v1.md:36`
independently confirms this in its own traced-structure table: *"queued scene context (never populated
live — §7)"* — and that document's §7 goes further still: **no live trigger ever queues a `combat`-type
scene at all** — `evaluate_triggers` (`scene_dispatch.py:77-101`) fires only `scene_type: "contest"`,
and the repo's one `queue_scene(...)` call site (`:107`) only ever passes that. So the entire
`derive_parties` path this section designs against is **unreached from the season loop today**,
independent of the `DISPATCH_COMBAT_BRIDGE` flag's value.

**What follows is a design for the caller that does not exist yet**, not an extension of a live
contract — there is no live contract to extend. Framed that way, this section is not weaker for it: it
means nothing already constrains the `ctx` shape, so this document **specifies** the contract the first
production caller (a future `05` action queuing a `combat` scene) must satisfy, rather than inferring
one from an existing convention that turns out not to exist.

### 3.2 Two ways terrain could reach the force model, priced against each other

| option | cost | verdict |
|---|---|---|
| **Widen** — add a terrain-derived field to `Combatant.__init__` or a parameter to `wrapper.fight()` | touches `systems/combat/combat_engine_v1/`, the file the docstring names as off-limits from this side; couples a PC-lane rebalance to IN-side terrain math it doesn't know about; grows what the one declared seam is allowed to reach into, even though `PATH_SEAM_ALLOWED`'s literal file-path ceiling is untouched | rejected — no benefit over the alternative, real cross-lane cost |
| **IN-side coefficient** — apply a registry-declared multiplier to the *already-derived* `history` value, inside `_combatant_from_faction_mil`, before `Combatant()` is constructed | zero edits under `systems/combat/`; zero growth of the seam; a load-time-checkable registry table | **shipped** |

This is not the brief's original instruction taken on faith — it is argued here because the 2026-08-29
authority amendment explicitly asked this question be priced rather than assumed (`12-O3` above). The
IN-side option wins because the seam already has exactly the slot terrain needs: `history` is the one
place a coefficient can land without crossing the boundary at all.

### 3.3 The design

**`ctx` gains one key.** The bridge already defines its own `ctx` contract (`combat_bridge.py:35-37`:
*"a new ctx contract this module defines"*) — extending it is not the same act as widening
`PATH_SEAM_ALLOWED`; nothing about the sys.path/import seam changes. Proposed addition: `ctx['site_id']`,
the place the battle is fought at. **Missing or unresolved `site_id` degrades to neutral terrain, it is
not a context-derivation gap** — unlike missing `factions` (`derive_parties` correctly returns `None`
there, `:126-127`), terrain is an enhancement, not a precondition for combat existing at all.

**Role is a named field, not a tuple position.** Because no production caller exists, there is no
convention to preserve, and reusing `fids[0]`/`fids[1]` positionally would hand the *next* author of the
real caller an ordering they cannot recover from the data itself — a future misreading silently swaps
attacker and defender with no error. So this document specifies: the caller populates
`ctx['attacker']` and `ctx['defender']` (explicit faction ids), not a two-tuple read positionally.
`derive_parties` is extended (still IN-owned, still not crossing into `combat_engine_v1`) to read these
when present, and to fall back to `ctx['factions']`'s existing positional order (`fids[0]` = attacker)
only to keep the two pre-existing test fixtures above passing unmodified. The attacker is the side whose
faction action queued the campaign; the defender is the incumbent holder of the target place — both
resolvable at scene-queue time by whichever future `05` action declares the campaign.

**The formula, applied inside `_combatant_from_faction_mil` (now parameterised by role):**

```
terrain = world.places[ctx.get('site_id')].identity.terrain   if site_id resolves, else 'open'
coeff   = terrain_combat_effects[terrain][role]                # role ∈ {attacker, defender}
history_effective = max(1, round(faction.Mil * coeff))
```

**`terrain_combat_effects` is one new block in `content_registry.yaml`** — not a third registry file
(`00 §9`'s two-file ceiling holds; this is a block, per its own corollary). Illustrative shape proposal,
none of it a ledger constant, and the keys must track whatever terrain vocabulary `07` ultimately ships
(a coordination note, not a claim this document can settle):

```yaml
terrain_combat_effects:
  open:     {attacker: 1.00, defender: 1.00}
  forest:   {attacker: 0.90, defender: 1.15}
  hills:    {attacker: 0.95, defender: 1.10}
  mountain: {attacker: 0.80, defender: 1.25}
  wetland:  {attacker: 0.90, defender: 1.05}
```

**This is the personal→mass leverage rule (§2.4), extended from *who* to *where*.** A coefficient on
`history`, never a flat shift — the same guard, same reasoning, one more input routed through the one
slot the seam already has.

*Emergent possibility lost if cut:* the one system that most rewards knowing the ground would be
geometrically uniform — every campaign decided by muster totals alone, terrain existing only as a place
stat no army ever felt.

**Falsifiers.**

1. **Seam-integrity.** `test_engine_does_not_import_systems.py`'s existing assertion that
   `PATH_SEAM_ALLOWED == {'cross_scale/combat_bridge.py'}` (`:288-292`) continues to pass, unmodified,
   after this change lands. If it doesn't, this document's "not widened" claim is false.
2. **Discrimination.** A load-time test over `terrain_combat_effects` asserting every declared
   coefficient lies in a bounded band (illustrative: `[0.7, 1.3]`) and that no terrain kind other than
   `open` rounds to `1.00`/`1.00` for both roles — a table that doesn't discriminate is decoration, the
   same reachability-bar shape used elsewhere in this suite.
3. **Reachability, stated honestly rather than assumed.** The falsifier for "terrain reaches the force
   model" is that some production path constructs `ctx['attacker']`/`ctx['defender']` (or legacy
   `ctx['factions']`) and that `queue_scene` is ever called with `scene_type == "combat"`. **Today,
   neither is true** — verified above by grep and by `combat_flow_skeleton_v1.md §7`'s independent
   trace — and this document does not claim otherwise. What it ships is the coefficient table and the
   contract the caller must meet; reachability is a separate, currently-open gap this document did not
   create and cannot close from here.

**J-N / J-O:** neither applies here. The lookup is a same-tick read of already-resolved `World` state,
not a Key consumption and not a cross-season carry.

---

## 4. Treaty as edge (change E)

### 4.1 The container, inherited

`01 §7.3` already builds the shared edge container and adopts `treaty` (faction↔faction) as one of the
two kinds PP-724 declares out of its own NPC↔NPC scope (`systems/npcs/npc_relational_graph_v30.md:18`:
*"PC-NPC and NPC-NPC ties compose through shared participation in scenes but do not collapse into one
mechanic"* — the same sentence that scopes PP-724 away from faction-level ties in the first place). What
`01` did not design is treaty's **own** lifecycle: its `transitions:` list (`01 part2 §12`) carries
knot, kinship, patronage and rivalry rows but none for treaty. This section supplies them.

**Terms are `Debt` tags, not a new tag kind.** v1's failure, named at `00 §1` as the worked
under-distillation example, was representing one relationship two ways — a `Debt` tag pair *and* an
edge. The fix here is not a new object; `01 §10`'s cut list already rejected a `Compact` tag family
because *"a recurring term-limited claim is `Debt(recurs=True, ttl=term)`"* — exactly the shape a
treaty's clauses need. So: **one edge, `relation: treaty`; its terms are `Debt` tags it owns**
(`owner_ref = (edge, edge_id)`, per `01 §3`'s tag owner set, which already spans edges). A tribute
clause is `Debt(key='clause:tribute', value=rate, ttl=term)`; a permanent alliance clause is the same
shape with `ttl=None` (durable, per Tag's own convention). No seventh tag kind, no separate object.

**Charter, briefly, for completeness of change E — not designed here.** `charter` (faction→place) is
PP-724's other out-of-scope extension and shares this container. Its privileges-granted and revocation
semantics belong to `07`/`08` (a place's governance layer), not to adjacent systems; noted so change E's
picture is complete, not re-derived.

### 4.2 Formation — the gate `substrate.edge` checks, not the negotiation itself

The negotiation — proposal, counter-terms, acceptance — is a `05`/`06` faction-action module's job
(a contested resolution over the two factions' postures and ethos-`appeal`, out of this document's
scope). What lands here is the **gate** the edge-creation call must satisfy:

| gate clause | reads |
|---|---|
| both endpoint factions hold a post empowered to bind them (`head` or `envoy`) | `01 §4` Post roster |
| **uniqueness** — no existing `active` `treaty` edge already between this ordered pair | a scan over edges, mirroring Knot's own uniqueness gate (`01 §7.5`: "no existing Knot with this NPC") |
| the negotiating module's own resolution succeeded | `05`/`06`'s resolver, not this document's |

**At most one active treaty edge per faction pair.** A new agreement between already-treatied factions
adds `Debt` terms to the **existing** edge; it does not create a second one. New terms after a
denouncement or expiry (below) *do* create a new edge — the old one's tags and rupture record persist as
history rather than being overwritten, which is exactly why the container exists: `causes[]` chains
across the old treaty's life and the new one's rather than being spliced.

### 4.3 State, and the tag-gated hysteresis pattern reused from §2.2

`treaty`'s own form states, declared per-kind as `01 §7.3` requires ("never globally"): `active`,
`violated`, `denounced`, `expired`. No strain gauge — per `01 §7.3`, *"a kind with no strain axis has no
strain gauge,"* and treaty's breaks are discrete tag-flagged events, the same shape PP-724 itself uses
for kinship's *"severance is an institutional act"* (`:334-340` region, cited via `01 §7.2`).

```yaml
transition: treaty.active_to_violated   entity_kind: edge   field: state   # relation: treaty only
from: active   to: violated
gate: a Grudge tag owned by this edge exists, non-empty provenance, citing a clause-breach Key
      (the breach detection itself belongs to whichever module enforces that clause — 05, 06 or 08 —
      this row only reacts to the tag landing)
cost: null   emits: form.transitioned   reversible: true
class: substrate
---
transition: treaty.violated_to_active   # reconciliation
from: violated   to: active
gate: no live (unswept) breach Grudge tag remains on this edge
hysteresis: {band: null, dwell: "inherited from the breach tag's own ttl"}   # the §2.2 pattern, reused
reversible: true
---
transition: treaty.violated_to_denounced
from: violated   to: denounced
gate: a Precedent tag ('denunciation') deposited by an empowered post (head|envoy), naming this edge
reversible: false
---
transition: treaty.active_to_expired
from: active   to: expired
gate: the edge's duration Debt tag (if any) has no live instance and no renewal Debt was deposited
      before it expired   # ttl=None (durable) treaties never reach this gate
reversible: false
```

**The tag-gated hysteresis pattern, stated once, used twice (§2.2 and here).** Where the gate is
tag-existence rather than a gauge crossing a numeric threshold, `01 §2.3`'s `H_MIN` arithmetic (built
for a scalar gauge) does not apply directly; `band: null` and the required dwell is supplied by the
gating tag's own `ttl` rather than a second declared parameter. This is a documented sub-case of the
general rule, not an exemption from it — the falsifier in `01 §2.3` still binds on every *gauge-gated*
reversible pair in this suite.

**Converters, cited not redesigned.** `01 §7.4` already owns `marriage_to_treaty` (`kinship → treaty`)
and notes it as the interesting case *because* the source kinship edge persists unchanged — a marriage
surviving a denounced treaty is expressible only because these are separate objects. PP-724's own feud
auto-transmission-along-kinship mechanic (decision log, `npc_relational_graph_v30.md:670`: *"load-bearing
… without it feuds dissipate at each death"*) is the canon precedent for exactly the chained-causation
property this container buys: a treaty denounced because of a feud inherited through a marriage is one
`causes[]` chain, not three unlinked records.

*Emergent possibility lost if cut:* a treaty and the betrayal that ends it would live in two different
objects again, and a feud inherited through a marriage that later collapses a state's own alliance could
not be told as one biography.

### 4.4 Disclosure and Keys

Treaty reuses the container's single Key surface (`edge.formed`/`edge.transitioned`, already in `00
§9.2`'s minimum set) and its single disclosure rule: a treaty's `state` is published, band-presented
except where a term's own `Debt` value is a decision input this season (then exact, same reasoning as
`substrate.post`'s budget row, `01 part2 §12`). **No new Key type is introduced** — nothing here is
blocked on P0-1.

**J-N.** A treaty's duration and violation checks are boundary reads (TTL sweep, tag existence), never
an emission scheduled to land later — the same discipline as succession (§1). **J-O.** These transitions
`consumes: []` — they are gates over state, not Key reactions — so nothing about treaty depends on J-O's
resolution either way.

---

## 5. The deliberative body — carried forward, now a composition of Posts *and* Edges

**The motion has one design, and it is this document's — settled, not merely claimed.** `05`'s own
first draft carried a one-line `act.motion` family row (`DO`, target *"the opposing coalition"*)
beside `ad.motion` below; `05`'s owner has weighed the two and cut theirs to a pointer, in their own
words: *"`12`'s is the fuller design and it wins. The row is cut to a pointer; `ad.motion` is
self-contained (`remit: [head, minister]`, its own `post.budget` cost), so nothing is orphaned"*
(`05_faction_actions.md` Overrides, O-5.12). **`ad.motion` (§6) is therefore the sole design and the
sole module** — `price(magnitude) = k·magnitude`, `vote_bar(magnitude)` monotone, and the relational
`vote_weight` term below, none of it duplicated in `05`. A reader who finds `act.motion` still named
in `05 §5`'s family table should read it as the retired pointer O-5.12 describes, not a second design
to reconcile against this one.

### 5.1 What is unchanged from v1 `09 §3`

A body has no state of its own: it is a **set of posts** (membership = holding a post whose kind
declares `deliberative: true`) and a procedure. A motion has a `subject` — required, a tag — a
`proposer`, a `magnitude` and a `remedy`. A defeated motion persists as a `Precedent` tag with no force
and full citability. The sanction is **one** parameterised action, `price(magnitude) = k·magnitude` in
the proposer's own `standing`, `vote_bar(magnitude)` monotone increasing — not five discrete tiers.
All of this survives the critique untouched; v1's reasoning for each (§3.2's "one engine, several entry
points," §3.4's rejection of a five-tier sanction as needless machinery) is carried with it, not
restated.

### 5.2 What change E adds: vote weight reads edges, motions may cite an edge's tag

**Vote weight now has a bounded relational term.** v1's `vote_weight` derivation read only `post.kind`
and `holder.faction.acceptance`. Post-holders who sit in the SAME body may also hold **edges** between
them — a `sworn-bond` or `patronage` tie nudges toward voting together; a `rivalry` or `feud` nudges
apart. This is exactly "composition of Posts and edges, not a subsystem": the body invents no new
mechanic, it reads two primitives that already exist.

```
vote_weight(post) = f(post.kind, holder.faction.acceptance)          ← v1, unchanged
                   + relational_term(edges among this season's body membership)
```

**Bounded by the SAME cap that governs every other relational term in this suite** (`01 §3.4`):

```
|relational_term|  ≤  RELATION_SHARE_MAX · (max structural term − min structural term)
```

No new bound is invented; the existing reachability bar — the structurally-worst voter must still be
unable to outrank the structurally-best one on relational weight alone — applies verbatim.

**A motion's `subject` may now be a tag owned by an edge.** `01 §3` already lists `edge` in Tag's
`owner_ref` set. A treaty's `violated` transition (§4.3) deposits a Grudge or Precedent tag on that edge;
that tag is a legitimate motion subject exactly as a person- or faction-owned one is — *"the body
proposes to censure the crown over the Baralta treaty's breach"* names a real tag on a real edge, not a
free-text pretext.

**Blocs are noted, not designed here.** `06`'s bloc (a set of posts inside one faction sharing a
project, `00 §4.3`) is where a coordinated voting bloc's *cause* lives; this document does not invent
bloc mechanics. A bloc surfaces through the body only as correlated votes among its member posts, which
`06`'s composition already implies without this document adding anything.

*Emergent possibility lost if cut:* a body of posts that vote as if the room had no relationships in it
— every session, the same coalition math, with no way for an alliance or a feud sitting outside the
chamber to be felt inside it.

---

## 6. Module contracts

```yaml
- module: ad.succession
  parent: adjacent          class: substrate
  scales: [peninsula]        tier: null
  resolver: d_sigma
  remit: []                                 # triggered by a vacancy, not invoked
  budget: null
  consumes: [{type: post.vacant, from: [pm.vacancy]}]     # Key consumption — J-O, §1
  emits: [{type: post.granted, terminal: false}]
  state:
    - {name: post,     bucket: post,  writable: true, owner: substrate.post}
    - {name: standing, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: tag,      bucket: tag,   writable: true, owner: substrate.ledger}
  form: []      transitions: []
  disclosure:
    - {of: claimants, inputs: published, presentation: exact, trigger: hidden}

- module: ad.unit
  parent: adjacent          class: substrate
  scales: [territory]        tier: territory
  resolver: derivation                       # its own gauges; transitions are gates, applied by the herald (W-5)
  remit: [commander]
  budget: {gauge: post.budget, cost: 1}
  consumes: []      emits: [{type: form.transitioned, terminal: false}]
  state:
    - {name: unit.size,       bucket: gauge, writable: true, owner: ad.unit}
    - {name: unit.discipline, bucket: gauge, writable: true, owner: ad.unit}
    - {name: unit.experience, bucket: gauge, writable: true, owner: ad.unit}
  form:
    - {entity_kind: unit, field: assignment}
    - {entity_kind: unit, field: unit_kind}
  transitions: [unit.field_to_garrison, unit.garrison_to_field,
                unit.levy_to_regular, unit.regular_to_levy]
  disclosure:
    - {of: unit.size,       inputs: published, presentation: exact, trigger: hidden}
    - {of: unit.discipline, inputs: published, presentation: band,  trigger: hidden}
    - {of: unit.experience, inputs: published, presentation: band,  trigger: hidden}

- module: ad.motion
  parent: adjacent          class: substrate
  scales: [peninsula]        tier: country
  resolver: d_sigma
  remit: [head, minister]
  budget: {gauge: post.budget, cost: 1}
  consumes: []      emits: []
  state:
    - {name: standing, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: tag,      bucket: tag,   writable: true, owner: substrate.ledger}
  form: []      transitions: []
  disclosure:
    - {of: motion.subject,   inputs: published, presentation: exact, trigger: hidden}
    - {of: motion.magnitude, inputs: published, presentation: exact, trigger: hidden}
    - {of: vote_weight,      inputs: published, presentation: exact, trigger: hidden}

# Supplementary rows this document contributes to substrate.edge's already-open `transitions:` list
# (01 part2 §12 declares knot/kinship/patronage/rivalry rows; treaty's own lifecycle was left open —
# §4.3 above is the full design; restated here only as the registry-row shape).
edge_transitions_supplied:
  - treaty.active_to_violated
  - treaty.violated_to_active
  - treaty.violated_to_denounced
  - treaty.active_to_expired
```

`ad.unit` discloses size exactly and discipline/experience as bands — how many you have is a decision
input, how good they are is a condition, unchanged from v1's reasoning.

---

## 7. Player-facing surface

Per `00 §2.3`'s requirement that every document state its surface in one short table, and the test
that a surface table longer than the substrate table means the ratio is backwards:

| what the player touches | how, how often |
|---|---|
| **who commands a unit** (appointing/recalling a `commander` post) | through `04`'s appointment flow — this document supplies the gate the appointment satisfies, not a verb of its own |
| **whether to order a unit field ↔ garrison** | `ad.unit`'s own transition (§2.2) — "a post action, not a roll," gated on the commander's order and spent from the commander's own `post.budget` — no new verb, and no `05` action-family invocation either: `05 §5`'s eight rows (`05p2 §5`) have no unit-assignment family, and this document's own transition already supplies the gate and the cost without needing one |
| **a motion, if the player holds a body-eligible post** | propose (choose subject tag + magnitude) or vote — the body's only two verbs, both already in v1 |

| what the player never touches |
|---|---|
| a treaty's formation, violation, denouncement or expiry — these arrive as Slate items (`10`), never as a screen the player operates |
| terrain's coefficient on a battle's force model, or the coefficient table itself |
| a unit's `size`/`discipline`/`experience` values, or any transition's gate threshold |
| the deliberative body's relational vote-weight term, or which edges fed it |

**This document introduces zero new player-facing verbs.** Every substrate object it adds (unit-as-
entity, terrain's coefficient, treaty's lifecycle, the body's relational term) is a situation or an input
to an existing action, never a menu addition — consistent with `00 §2.2`'s hard budget.

---

## 8. Property audit

**Scope.** `ad.motion` and `ad.succession`'s claim-contest genuinely roll (`d_sigma`); `ad.unit` and the
edge transitions are gates and accrual (`01 part2 §13`'s scope limit applies identically here: no N/R/S/E
verdict is manufactured for a module that does not roll). What follows separates the two.

| property | verdict | reasoning |
|---|---|---|
| **P-i** legible odds | pass | Succession publishes both claimants' pools and backers' contributions; the motion publishes subject, magnitude and every vote weight, including its relational component |
| **P-ii** uniform leverage | pass | The relational vote-weight term is capped by `RELATION_SHARE_MAX` (`01 §3.4`), the same bound as everywhere else in the suite — no new leverage channel invented. The personal→mass and place→mass rules (§2.4, §3.3) forbid a flat modifier on the force outcome by construction |
| **P-iii** bounded, monotonic | pass | Succession's three bands are total, nothing fires on Partial alone. Unit gauges are floor/ceiling-bounded, geometric decay (`01 §5.1`). Treaty transitions are one-directional except the reconciliation pair, which is tag-gated with dwell supplied by the breach tag's own ttl |
| **P-iv** graded, recoverable | pass | Succession's worst outcome is a rival holding leverage, not elimination. A denounced treaty is a fact, not a deletion — a new treaty between the same factions is always reachable once the old edge is no longer `active`. Two-tier defeat severity keeps losing a battle and losing an army distinct |
| **P-v** right engine | pass | Succession's DO shape reads a differential correctly. Every form transition here (`unit.*`, `treaty.*`) is a gate, matching `01 §7`'s rule that a transition is never rolled. The motion is a contested vote (`d_sigma`) |

### 8.1 Loops, each with its bound

| loop | bound | gain |
|---|---|---|
| treaty violated → reconciliation → violated | the breach tag's own `ttl`, which is the dwell (§4.3) | **unmeasured**, bounded arithmetically by construction (a bounded ttl bounds the cycle period) |
| unit assignment flip-flop | dwell ≥ D seasons on the unit's own `form.transitioned` history (§2.2) | **unmeasured**; the guard is a query over existing Key history, no new counter |
| unit levy ↔ regular | `H_MIN(discipline)` per `01 §2.3`'s standard arithmetic | **unmeasured until `unit.discipline`'s descriptor row is declared** — the guard is checkable at that point with no campaign run |
| terrain coefficient → force outcome → (no feedback) | not a loop | terrain does not change in response to a battle's outcome in this document's design; a place's own condition gauges (07's) are the feedback channel, if any, and this document does not claim one |
| deliberative body relational vote term → motion outcome → tag → future relational term | `RELATION_SHARE_MAX` (`01 §3.4`), inherited, not re-derived | **unmeasured** — same reachability bar as every other relational-term site in the suite |
| succession claim contest across seasons | none needed — reads current state each boundary, no carry (J-N) | **not a cross-season loop under the current substrate** |

### 8.2 Gates, each with what it reads

| gate | reads | fails to |
|---|---|---|
| commander vacancy (Q-2) | `unit.commander` post's `holder_id` | that unit cannot be ordered into the campaign |
| treaty formation uniqueness | a scan for an existing `active` `treaty` edge on this ordered pair | negotiation proceeds only to add terms to the existing edge |
| `treaty.active_to_violated` | a Grudge tag on the edge, non-empty provenance | the edge stays `active` |
| `treaty.active_to_expired` | the duration Debt tag's liveness | the edge stays `active` indefinitely if the tag is durable (`ttl=None`) |
| `unit.field_to_garrison`/reverse | the unit's own `form.transitioned` history, dwell check | the order is refused this season |
| terrain lookup | `world.places[ctx.get('site_id')].identity.terrain`, defaulting to `open` | falls back to neutral coefficients, never blocks the battle |

### 8.3 The four qualitative verdicts, applied to this document

**Necessary** — succession is what ED-IN-0201's gate makes load-bearing; the unit-as-entity update is
what change A requires uniformly; treaty-as-edge is change E's explicit charge; the body's relational
term is the minimum reading of "composition of Posts and edges." **Robust** — a faction cannot be
eliminated by any roll here; a treaty cannot be un-negotiated, only ended and re-formed as a new edge
carrying its own history; a unit's shape changes only through gated, hysteresis-bound transitions.
**Smooth** — one write rule (four leaves) used throughout, no new tag kind, no new registry file (one
block added to an existing one), the tag-gated-hysteresis pattern stated once and reused twice (§2.2,
§4.3) rather than invented separately. **Elegant** — three modules, four supplementary transition rows,
one registry block; the honest deduction is that the tag-gated hysteresis pattern is doing real work
across two otherwise-unrelated sections, which is the corollary `00 §1` asks for (one shape, several
uses) rather than the failure it warns against (several shapes, one job).
