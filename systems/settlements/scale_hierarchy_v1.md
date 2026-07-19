# Scale Hierarchy & Cross-Scale Faction Authority (v1)

## Status: RATIFIED — direct Jordan ruling, 2026-07-13, overrules `valoria_political_hierarchy_v30.md` (PP-726) §1's "Territory = Settlement" equivalence and §2.3's fracturing rule. Lane: IN (cross-cutting SE, FA, WR). No ED allocated yet for the propagation work this doc tracks (§6) — allocate on landing.

**What this is.** Jordan's direct ruling (2026-07-13, in conversation) resolving `ners_vsg_reconciliation_v1.md`'s **B12** — a conflict between the generation-sourcebook's proposed Territory/Province generator stack, Part 41's "Territory scale," and PP-726's existing canon, which had no tier between Settlement and Province at all. The ruling is a genuine hierarchy expansion plus a set of load-bearing mechanics for how authority, governance, and faction power move through it. This document records the ruling verbatim-in-substance and scopes the propagation work it requires. **The conceptual structure below is RATIFIED as stated; the mechanical rewrite of PP-726 and downstream docs (§6) is tracked follow-on authoring, not yet executed.**

---

## §1 · The hierarchy

> "People in one place comprise settlements comprise territories comprise provinces comprise duchies comprise country."

```
Country (Kingdom of Valoria)
└── Duchy (Valorsmark / Hafenmark / Varfell — unchanged from PP-726)
    └── Province — CONDITIONAL, not a fixed administrative unit (§2)
        └── Territory — NEW tier, multiple settlements
            └── Settlement — the base unit, people live here
```

This directly supersedes PP-726 §1.1's *"**Territory = Settlement** is the smallest political unit."*
Territory is now a genuine intermediate tier: **"Territory between settlement and province. Multiple
settlements per territory, multiple territories per province."** PP-726's Duchy tier is unchanged
(3 duchies, unchanged ownership: Almud/Valorsmark, Baralta/Hafenmark, Vaynard/Varfell).

## §2 · Provinces are conditional, not fixed — replaces PP-726 §2.3's fracturing rule

> "Provinces are only formed if the same faction holds the constituent territories."

PP-726 §2.3 modeled provinces as fixed geographic units that *fracture* into sub-provinces when
faction-control diverges. This ruling replaces that with a cleaner, unified mechanic: **territories are
the fixed geographic units; a province is an emergent aggregation that exists only while its
constituent territories share a common faction holder.** A province isn't a container that sometimes
breaks — it's a name for "these territories, right now, cohering under one faction." When that
condition stops holding, the province simply stops existing as a unit (no fracturing state-machine
needed); when it starts holding again (a faction unifies the territories), the province re-forms. This
generalizes PP-726's fracturing rule rather than contradicting its spirit — same phenomenon
(faction-alignment-dependent provincial coherence), cleaner mechanic (existence-conditional rather than
a stateful fracture/reunify transition).

## §3 · The governance-type cascade

> "Dukes govern provinces and define provincial governance type, provinces govern territories and
> define territorial governance type, territories govern settlements and define settlement governance
> type. A noisy cascading throughline descends from duchy governance through to settlements and vice
> versa."

Each tier's governing authority sets the governance *type* of the tier immediately below it:

```
Duke        → sets/influences   Provincial governance type
Province    → sets/influences   Territorial governance type
Territory   → sets/influences   Settlement governance type
```

Explicitly named as a **throughline** (the corpus's existing noisy-weighted-cascade vocabulary — see
`designs/territory/goldenfurt_slice/generation_methodology.md` and `settlement_generator_v1.md`'s own
conditioning-throughline formalism): plausibility/pressure flows down noisily, not deterministically.
And it is **bidirectional** ("and vice versa") — settlement-level conditions feed back up, not just
duke-level policy pushing down.

## §4 · The consent mechanic — L/PS is the modulator, not decoration

> "There is a regime or logic that permeates from the top down, but the ability for the ruling faction
> to maintain their power is modulated by what their settlements are willing to accept in terms of
> governance — hence popular support and legitimacy."

This gives **Legitimacy/Popular Support (L/PS) a precise, load-bearing mechanical role it did not
previously have**: L/PS is the resistance/consent gate on the top-down governance cascade. A
duke/province/territory can *impose* a governance type, but whether it sticks — whether the ruling
faction actually *keeps* effective power at that tier — depends on whether the settlements underneath
accept it, measured by L/PS. This is the single most consequential connection this ruling makes to
already-flagged corpus state: **L/PS is currently inert in `sim/`** (confirmed 100/100 by
`tools/sim_harness/`'s `lps_inert_check`, tracked as `governance_consolidation_v1.md`'s E5). E5 is no
longer just "an open FA-lane item, ratified-as-prose-only until wired" — it is now the central
mechanism connecting this entire hierarchy ruling to actual gameplay consequence. **Wiring L/PS is a
precondition for this hierarchy mattering in play, not a parallel task.**

## §5 · Cross-scale faction authority

### §5.1 Factions hold people, not territory

> "Local-scale factions are not necessarily part of provincial-scale factions, and provincial-scale
> factions are not necessarily part of national-scale factions... Factions do not necessarily need to
> hold territory — they need to hold PEOPLE, and it is the number of people and the weight of their
> positions that carry the value of that faction."

Faction tiers (local / provincial / national) are **independent**, not a strict containment hierarchy.
A local faction is not automatically a subsidiary of whatever provincial faction sits above it
geographically. A faction's power derives from **population held and the weight of their positions**,
not territorial control as a proxy. This is a real design departure from treating "faction controls
territory" as the primitive — territory-holding is a *consequence* of holding enough people in enough
places, not the base unit of power itself.

**Named examples by tier** (illustrative, not an exhaustive roster — does not itself resolve **B1**'s
starting-4 vs. emergent-factions structure, which stands as separately ruled):
- **Local-scale**: guilds, independence protests, militia, unions/cooperatives, councils.
- **Provincial-scale**: guilds, bureaucracies, councils, independence movements, large
  unions/cooperatives.
- **National-scale**: the Restoration Movement, Löwenritter.

### §5.2 Independence and cross-scale claiming

> "It is always possible for a settlement, territory or province to become independent of its faction
> holder... It is possible for a settlement to become independent under the purview of a territorial,
> provincial or national level faction. For example, a settlement can be claimed by Restoration
> Movement. These can aggregate into territories and provinces like usual."

Two distinct mechanics:
1. **Independence** — any settlement, territory, or province can break from its current faction holder.
   This is the generalized replacement for PP-726 §2.3's fracturing (see §2 above) extended down to the
   settlement level, not just province-level splits.
2. **Cross-scale claiming** — a settlement can be claimed directly by a faction from a *different* scale
   than its current chain of control, skipping intervening tiers. Jordan's own example: a single
   settlement claimed by the Restoration Movement (a national-scale faction) without needing to first
   hold the settlement's territory or province. Once claimed this way, the settlement (and any
   territories/provinces that subsequently aggregate around it) participates in the normal hierarchy —
   the claim's *origin* is exceptional, not its downstream behavior.

### §5.3 The two authorities that bypass the chain

> "The rulers of a nation are an exception in that they are able to influence duchies/provinces/
> territories/settlements outside their direct chain of control. Parliament, by the same token, has no
> direct chain of control but can forceably impact what happens in a province, territory or settlement."

Two cross-cutting authorities, both explicitly exempted from the normal nested chain-of-command:
- **The national ruler** (the monarch — Almud, per PP-726 §1.1) can act directly on *any*
  duchy/province/territory/settlement regardless of normal ownership nesting. This sharpens PP-726's
  existing note that Almud "exercises overlordship over the other two duchies" into a general
  principle: the Crown's reach is not bounded by the chain at all, not just extended one level beyond
  his own duchy.
- **Parliament** has no fixed position in the hierarchy (it isn't a duke, isn't a provincial governor)
  but can **forcibly** impact any province/territory/settlement. This composes directly with the
  existing Parliamentary/Censure mechanics (`sim/provincial/parliamentary_action.py`,
  `designs/architecture/auto_manual_resolution_duality_v1.md`) — Parliament's cross-cutting reach is
  now explicitly a hierarchy-level property, not just a faction-action-economy one.

### §5.4 The worked example

> "Valorsmark controls multiple provinces. The King has a particular governance type, and he runs a
> royal court from which he appoints distinguished servants as governors of a province. These governors
> oversee, coordinate and vet decisions made by the appointed councils that govern each settlement.
> Accompanying provincial factions here, for example, can be an anti-caste Einhir faction and a farming
> collective."

A concrete instance of §3's cascade: King (duchy-scale governance type: royal-court-and-appointment) →
appoints Governors (provincial scale) → Governors oversee/coordinate/**vet** settlement-level Councils
(settlement scale, themselves appointed bodies) → alongside this chain, independent provincial-scale
factions exist in the same space (an anti-caste Einhir faction, a farming collective) that are *not*
part of the Crown's appointment chain at all — consistent with §5.1's independent-tiers principle.
"Vet" is notable: the province-level authority doesn't merely set policy top-down, it reviews/approves
settlement-level decisions — a concrete instance of the §3 cascade's bidirectionality.

---

## §6 · Propagation — what this ruling requires downstream (tracked, not yet executed)

This section is honest bookkeeping, not a decision surface — nothing below needs further Jordan input,
it needs authoring.

1. **`valoria_political_hierarchy_v30.md` (PP-726) needs a real rewrite**, not just a banner: §1 (the
   hierarchy diagram and the "Territory = Settlement" line), §2.1 (settlement-count-per-province, now
   needs a settlement-count-per-territory rule plus a territory-count-per-province rule), §2.3
   (fracturing rule → superseded by §2 above), §2.4 (political-value computation — now needs a
   territory-tier term), §2.5 (governor assignment — now needs to specify governors exist at territory
   scale too, per §3's cascade). This document supersedes those sections in content; PP-726 itself still
   needs the banner + eventual line-level rewrite.
2. **`generation_sourcebook_v1.md`'s R-series (Territory/Province stack, §1.3)** needs reworking against
   the real hierarchy — R3's "controlling faction + fracture state" row should become "territories are
   the fixed unit; province membership is the conditional-aggregation state," matching §2 above. This
   also resolves **B12** cleanly: the sourcebook's Territory/Province stack and Part 41's Territory
   *scale* turn out to describe the *same* real tier, not two competing concepts — Part 41's
   cross-settlement governance verbs (Beacon Network, Kontor, etc.) operate at exactly this newly-real
   Territory tier.
3. **`generation_sourcebook_v1.md`'s F-series (Faction stack, §1.2)** needs an explicit
   local/provincial/national tier field per generated faction (F1's substrate-posture axis currently
   has no tier concept at all), plus a people-held-not-territory-held power computation replacing or
   supplementing F3's stat block.
4. **E5 (wire L/PS) is now the single highest-priority open item in the whole governance/generation
   thread** — see §4 above. Nothing in this ruling's governance cascade produces observable gameplay
   consequence until L/PS is live in `sim/`.
5. **VSG (`settlement_generator_v1.md`)'s P12 temperament-aggregation ruling** (already recorded in
   that doc's §7 item 1) is now directly actionable: the scales it aggregates across are Settlement →
   Territory → Province, per §1 above.
6. Part 41's Territory-scale content (Relay Tier/Beacon Network) — previously held back pending B12 —
   is **no longer blocked by B12** (resolved, item 2 above) but **remains blocked on `engine_clock`**
   (B11), per `ners_vsg_reconciliation_v1.md §5` item 5. That hold stands.
