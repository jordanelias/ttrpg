<!-- [EDITORIAL: ED-IN (allocate on ratification) — governance ripple substrate, integration spec, 2026-07-11] -->

# The Governance Ripple Substrate — Integration Spec

## Status: PROPOSED (2026-07-11) · Lane: IN (cross-cutting) · Author-pass, not yet Jordan-ratified

**What this is.** The connective tissue for the four research passes filed this session
(`designs/audit/2026-07-09-comparative-governance-research/`,
`.../2026-07-10-historical-concerns-action-catalogue/`,
`.../2026-07-11-rise-to-power-roster-system-research/`,
`.../2026-07-11-proactive-governance-scale-research/`). Those passes surfaced ~200 candidate
mechanics. Authored one-by-one they produce **content volume, not a system.** This spec defines
the small set of **primitives** over which events, settlement levers, standing changes,
field-investigation / social-contest / faction-action content, and emergent arcs all *compose* —
so ripples **emerge from independent systems reading and writing shared state** (Μ-β autonomous-agent
composition, `references/throughlines_meta.md` §2) rather than being hand-scripted per case.

**What this is NOT.** Not a content catalogue (the four dockets are). Not new numbers. It is the
*wiring diagram* the dockets' individual proposals plug into. Every proposal cited below already
exists in a filed docket; this spec says how they connect.

**Binds to (read for exact current values):** `designs/territory/governance_play_redesign_v1.md`
(verbs §1.3, Directive §1.4, event deck §2.1–2.3, Ledger §1.6, ambition engine §3.1–3.4);
`designs/territory/settlement_layer_v30.md` (settlement stats §1.5–1.8, Local Actors §4.5,
Dearth §4.3a); `designs/provincial/faction_politics_v30.md` (Standing ladder, Demotion Magnitude
§1.0a); `designs/architecture/key_substrate_v30.md` (the Key emission substrate).

---

## §1 · The core loop — the causal spine

Every subsystem this session touched is one arc of a single closed loop. Naming it is the point;
once named, each docket proposal is legible as "which arc does this serve," and gaps become visible.

```
   ┌─────────────────────────────────────────────────────────────────────────┐
   │                                                                          │
   ▼                                                                          │
[EVENT fires]  ──►  [hits SETTLEMENT OPERATION]  ──►  [RESPONSE BURDEN on the  │
 deck draw,          via the typed levers (§2)         governing character:    │
 Π-gated (§4)                                          3 pressure vectors, §3] │
                                                              │               │
                                                              ▼               │
                                              [RESPONSE shaped by GOVERNANCE   │
                                               MODE — which verbs, at what     │
                                               cost, gated by how they hold    │
                                               power (§3, power_base)]         │
                                                              │               │
                                                              ▼               │
                                              [OUTCOME emits a Key (§5) that   │
                                               updates the responder's         │
                                               STANDING — advance or demote]   │
                                                              │               │
                        ┌─────────────────────────────────────┤               │
                        ▼                     ▼                ▼               │
              [ripples into FI    ripples into SC/    ripples into FA          │
               leads (§6.1)]      Parliament (§6.2)]  windows (§6.3)]          │
                        │                     │                │               │
                        └─────────────────────┴────────────────┘               │
                                              ▼                                │
                              [AGGREGATES across scale: settlement →           │
                               territory → faction → peninsula (§7)]           │
                                              ▼                                │
                              [seeds / advances an EMERGENT ARC (§8),          │
                               which re-weights the deck] ──────────────────────┘
```

The loop is already half-built in canon: `governance_play_redesign_v1.md` P4 ("the two-stroke
churn: world→player and player→world alternate and condition each other") is arcs 1→3; the ambition
engine (§3.1–3.4) is a second initiative source on the same loop. What this session's research adds
is the **rest of the circle** — the standing bridge (§5), the cross-subsystem ripples (§6), the
cross-scale aggregation (§7), and the arc feedback (§8) — and, critically, insists they all run over
the **same five primitives** (§9) so the loop composes instead of being five scripted subsystems
bolted together.

---

## §2 · Settlement mechanical levers — mechanical identity to match narrative identity

**The design lead's constraint (binding):** prefer reusing the existing settlement stats
(Prosperity 0–5, Order 0–5, Defense 0–5, Legitimacy 0–7, Popular Support 0–7, Weight, FacilityTier
0–3, Treasury, Π 0–10) over inventing granular resource meters. A settlement earns a **new** tracked
lever only when it changes *what kind of decision the settlement presents* — not the magnitude of an
existing dial. "Food supply" abstracts to Prosperity; "water quality" abstracts to Prosperity/Order;
a bare `trade_volume: 0–10` sitting next to Prosperity is exactly the reskin to reject.

**The test a lever must pass:** *would two settlements of different narrative type, facing the same
event, behave mechanically identically without it?* If yes, the lever earns its place; if no, reuse a
stat. Applying that test to the proactive-projects docket §4 reuse-ledger and the historical-concerns
docket §5 shortlist yields this **minimal new-lever set** (each is a *device*, not a meter — it
changes the shape of a decision, not just its size):

| Lever | What it is | Why it's a device, not a meter | Home docket |
|---|---|---|---|
| **StockLevel** (buffer institution: None / Established, + a hidden drawdown) | A standing granary/reserve that auto-absorbs a famine-class Crisis at reduced severity for as long as maintained | Matters for *timing and pre-commitment*, not magnitude — you build it *before* the shock or not at all; a Prosperity number can't express "insured vs exposed" | concerns §5 #5 |
| **Assessment tag** (`assessed_base`, a locked Prosperity figure) | Extraction reads the *locked* figure, not live Prosperity, until re-Surveyed | Creates a *legible gap* (assessed vs actual) the governor can exploit or that detonates on neglect — a decision about *when to look*, absent from any stat | SE-JP2 (authored) |
| **Capital-Posture** (Mobile / Fixed, one family) | Flips *what type* of extraction a Directive can ask for | Changes the *kind* of question, not the amount — the one Ledger family that re-types a decision | VEN-SE-3 + concerns §5 #1 |
| **Consent-Rule** (Unanimity / Majority) | Governs *how many* must agree before a ruling binds | Turns one council member into a veto or not — a structural gate on whether the governor can act at all | HAB-6 (queued) |
| **route/corridor Precedent** (single-corridor / diversified) | Whether a settlement's Prosperity depends on one named chokepoint | Makes a settlement *targetable* through its geography — a vulnerability flag a rival can read and attack | concerns §5 #4 |

Five levers, not fifty. Each makes a *settlement type* (granary-town vs trade-chokepoint-port vs
garrison-fortress) present a **different decision under the same event** — which is the definition of
mechanical identity. Everything else the dockets proposed as "new settlement state" collapses into
these five or reuses an existing stat (the proactive-projects §4 ledger did this accounting; this
table is its survivors, cross-checked against the concerns §5 shortlist to dedupe the reskin
clusters both passes independently flagged).

> **Open ruling R-1 (Jordan):** are these five levers in scope for the settlement layer, or is the
> intended identity-differentiator purely the *subnational-faction roster* (Seggio/Guild/RM) that
> already varies by settlement? The two are complementary but the priority ordering is a taste call.

---

## §3 · The response burden — three pressure vectors, kept distinct

When an event lands on the character responsible for a settlement/office, **three mechanically
distinct pressures converge.** Collapsing them into one "stress" scalar is the failure mode to avoid;
they read different state, resolve through different verbs, and fail in different directions. Keeping
them separate is what makes a governance decision a genuine *vise* rather than a meter to top up.

| Vector | Direction | Reads (existing state) | Resolves through | Failure signature |
|---|---|---|---|---|
| **Upward** | the governed pushing up | Local-Actor Disposition, unserved Needs, Π, Petition cards | Hold Court, Sponsor, Treat | revolt / Π→Crisis |
| **Downward** | superiors demanding results | the Directive (Comply/Bargain/Defy §1.4), a patron's performance ledger (CHN-9 Kaochengfa), Ministry/Consulta (HAB-4) | Comply, Bargain, Petition | recall / audit / Demotion |
| **Positional** | the seat's own cost | AP scarcity (P1), the dual-authority squeeze (§1.4), the **power_base-typed vulnerability** (roster docket §3.5) | *the choice of which vector to pay* | the collapse mode of *how you hold power* |

The **positional** vector is this session's genuinely new contribution: from the rise-to-power docket,
*how* a character came to hold the seat (patronage / merit / kinship / bureaucratic / military /
purchased / ideological) determines **which levers they can pull and what it costs them politically to
pull them.** A patronage-seated governor who defies a Directive spends their patron's capital, not
just their own Standing; a purchased-office holder has no loyalty reserve to draw on. The response is
not "spend AP to reduce stress" — it is "given the event, *which of three creditors do I pay this
season, and which do I let compound,*" where the affordable answer is shaped by the power_base.

This is where "modes of governance and politics impacted responding to events" (the design lead's
framing) becomes mechanical: the governance mode isn't flavor on the response, it's the **constraint
set** on the response.

---

## §4 · Event generation — the deck reads settlement state, not a random table

Already canon (`governance_play_redesign_v1.md` §2.1–2.3), restated here only to fix the two ends of
the loop the ripple substrate depends on:

- **Events are the world's *moves, drawn from current state*** — Π-gated (low Π → Opportunity/Ambition;
  mid → Petition/Friction/Intrigue; high → Crisis), trigger-predicate-filtered, tag-weighted. A
  famine Crisis fires because `StockLevel==None AND external_shock AND Π≥8`, not because a die said so.
- **The historical-concerns catalogue is the deck's content library** — every card there carries a
  trigger predicate in real stat vocabulary and a `follow_on` seed. The substrate's job is to make the
  `follow_on` seed land not just as *another card* but as a standing/FI/SC/FA consequence (§5–§6).

The one substrate requirement on the deck: **every card resolution must emit a Key** (§5). A card that
resolves by silently mutating a stat is invisible to the rest of the loop and breaks the ripple.

---

## §5 · The event→standing bridge — the primitive the design lead named directly

> *"the ways in which someone can respond to events can have them gain, maintain or lose standing
> within their organization. So something from an event deck about a poor crop yield or a flood…
> can ripple into someone being demoted for handling it poorly."*

**The mechanism, stated as a primitive — not a script:**

1. An event resolution (Comply/Bargain/Defy, or a Crisis-card branch choice) **emits a Key**
   (`key_substrate_v30.md` schema: `source_actor`, `causes`, `targets/impact_vector`, `scale_signature`)
   carrying a **resolution-quality signal** — the delta the response produced on the settlement's stats
   *relative to what the Directive/Need demanded*. Not "good/bad" as an authored label; the *arithmetic
   gap* between demanded outcome and delivered outcome.
2. **Standing systems READ that Key.** `faction_politics_v30.md` §1.0a Demotion Magnitude already fires
   on "sustained Duty failure"; the bridge is to make an event-resolution Key that shows a negative
   resolution-quality signal **count as a Duty-failure input**, and a positive one **count toward
   advancement** (the ambition engine's `consolidation_progress`, roster docket §3.4). CHN-9
   (Kaochengfa) is the *explicit, patron-scoped instance* of this general rule — which is exactly why
   the NERS audit flagged its standalone version as a reskin (audit §2, MERGE): the *general* bridge
   should live in §1.0a, and Kaochengfa is one patron-bound configuration of it.
3. **The resolution-quality signal is the single new primitive here.** It is not a new stat on any
   entity — it is a *computed field on the emitted Key*, defined against machinery that already exists.
   The two jaws of the vise (`governance_play_redesign_v1.md` §1.4 Directive + §1.5 Needs) each carry a
   *demanded* magnitude; the season's actual stat deltas are the *delivered*. So:

   ```
   resolution_quality(Key) = w_d · (delivered_to_Directive − demanded_by_Directive)
                           + w_n · (delivered_to_Need      − demanded_by_Need)
       where the two demands are the §1.4/§1.5 vise the character faced,
             delivered is the season's actual stat delta on each contested axis,
             and w_d / w_n weight who the character answers to
             (w_d high for a Directive-bound governor; w_n high for an electively-seated one).
   ```

   A governor who Complied with an Extract Directive *and* left the famine Need unserved posts a Key with
   `delivered_to_Need − demanded_by_Need ≈ −(relief demanded)` — a large negative signal on the Need jaw,
   positive on the Directive jaw. Who that *hurts* depends on `w_d/w_n`, which is set by the §3 positional
   vector (power_base): a Crown-appointed governor (high w_d) is fine; a Hafenmark alderman who answers to
   the settlement's estate (high w_n) is not. **The same event, same response, different standing outcome
   — because the constraint set differs.** That is "modes of governance impacted responding to events,"
   arithmetic.

4. **The signal projects onto the Key's existing `impact_vector`.** `key_substrate_v30.md` §2.1 already
   requires every Key to carry a Conviction-axis projection (`hierarchical / sacred / instrumental /
   traditional`, signed magnitudes). resolution_quality is not a *new* field fighting that schema — it is
   the **magnitude the impact_vector already carries, read on the axis the event contested** (a famine-
   relief failure lands on `hierarchical`/`instrumental`; a broken sacred oath on `sacred`). The bridge is
   therefore *zero new schema* — it is a *read convention* on a field the substrate already mandates.

**Why a primitive and not a lookup table:** because the *same* computed field drives demotion, advancement,
*and* the §6 ripples, a designer never authors "famine handled badly → demotion" as a rule. They author
the famine card (deck), and the resolution_quality read is already defined. The demotion *emerges*. Add a
flood card later and it inherits the whole chain for free — the anti-pattern-matching test (§9) is: if
adding a new event required hand-writing its standing consequence, the bridge isn't a primitive.

### §5.5 · Worked example — one famine, walked around the entire loop

To prove the loop composes rather than being narrated, here is a single event traced through every arc,
touching only the five primitives (§9). *Illustrative magnitudes; the shape is the claim.*

> **S0 · Setup.** Kronmark (S-004), a granary-adjacent Town, `StockLevel==None` (§2 lever, never built),
> Prosperity 4, Π 6. Governor: Aldric, Crown-appointed, **power_base = patronage** (seated by Minister
> Voss), so `w_d` high — he answers up. A regional Cooling flag (§7 peninsula layer) is active.
>
> **S1 · Event fires (§4).** Cooling flag pushes `external_shock` into Kronmark's Π → 8; deck trigger
> `StockLevel==None AND external_shock AND Π≥8` draws the **Famine Crisis** card (concerns catalogue).
> Simultaneously Minister Voss issues an **Extract Directive** (a war-levy). The §3 vise is live: the
> **Need** (famine relief) and the **Directive** (extract) each demand AP/Treasury Aldric doesn't have
> for both.
>
> **S2 · Response, shaped by mode (§3).** Aldric's positional vector: as Voss's client, defying the
> Directive spends *Voss's* capital, not just his own Standing. He **Complies** (extracts) and leaves
> relief unserved — the affordable choice *given his power_base*, not given the event.
>
> **S3 · Resolution Key (§5).** Emitted: `delivered_to_Directive = +levy (demand met)`;
> `delivered_to_Need = −(relief demanded)` → `resolution_quality` strongly negative on the Need jaw,
> projected onto the Key's `impact_vector.hierarchical`/`instrumental`. `scale_signature: [settlement]`,
> escalating.
>
> **S4 · Standing (§5).** With `w_d` high (patronage seat answering up), the negative Need-jaw signal does
> **not** trip Aldric's Demotion — he served his patron. *But* the Key is now in the log for §6.
>
> **S5 · Ripples, all three from the one Key (§6).**
> — **FI (§6.1):** the unserved famine raises Kronmark's concealment inventory — a grain-hoarder Local
>   Actor's black-market **Debt tag** becomes Investigate-discoverable. A lead now exists that did not.
> — **SC/Parliament (§6.2):** the resolution Key's magnitude crosses the contest-predicate threshold →
>   a Hafenmark alderman can open a **Parliamentary Censure** motion citing *this Key* — the debate is
>   over what actually happened at Kronmark, its opening Ob read from the signal magnitude (ties to the
>   pending ED-SC-0015).
> — **FA (§6.3):** Kronmark's Mandate contribution (Σ settlement L/PS) drops; aggregated with sibling
>   settlements it nudges the faction toward a defensive domain-action window.
>
> **S6 · Aggregation (§7).** The Mandate bleed rolls up; the Cooling flag that *caused* S1 is
> simultaneously pushing the same shock into *other* settlements — a **peninsula-scale correlated
> pressure** no single governor authored. Power over the region shifts because many Aldrics each made the
> locally-rational Comply choice.
>
> **S7 · Arc feedback (§8).** The Grudge tag from the unserved relief biases the grain-hoarder's **Ambition
> card** upward; the Censure motion's outcome writes a **Precedent** that re-weights Aldric's successor's
> legitimacy-Crisis draw. `valoria-arc-generator` reads this Key chain as a seed: *"the governor who fed the
> war and starved the town"* — an arc **no one authored**, emergent from five primitives composing over
> three seasons.

Every step read or wrote exactly one of: a Key, a Ledger tag, a Disposition, Π, or Standing. Nothing was
scripted. Swap the famine for a flood, or Aldric's patronage seat for an elected one, and the loop
re-runs with different signs — which is the definition of a substrate rather than a plot.

> **Open ruling R-2 (Jordan):** the resolution-quality signal makes NPCs demotable/promotable by
> event outcomes *on the same Standing ladder the player climbs* (roster docket §3.2 recommends shared
> rank space). Does an NPC's well-handled Crisis let them **contest a seat the player holds**? The
> architecture supports it either way behind one flag (`player_seats_are_contestable`); this is the
> sharpest "every action pays what it buys" stakes call in the whole design.

---

## §6 · The ripples — one signal, three downstream consumers

The design lead: *"it ripples across into field investigations and content for social contests and
faction actions."* The resolution-quality Key from §5 is read by three more consumers besides standing.
None of these is a new subsystem; each is an existing surface subscribing to the same Key.

### §6.1 · Field Investigation
A poorly-handled event (negative resolution-quality, or a Defy that protected the settlement at the
Crown's expense) **seeds a concealed actor / secret** — precisely the `Investigate` verb's existing
input (`governance_play_redesign_v1.md` §1.3: "surface a covert actor, a secret, a broker"). The
famine mishandled → a grain-hoarder Local-Actor's black-market Debt tag becomes Investigate-discoverable.
The primitive: a negative resolution Key **raises the concealment inventory** the Investigate verb draws
from. (Concerns catalogue: the Clerk-Corruption hidden counter, CHN-3, is the same shape — a hidden
liability that Investigate later surfaces.)

### §6.2 · Social Contest / Parliament  *(⚠ AT-RISK edge — see §13)*
The event *and the standing shift it caused* become the **subject matter** of a contest — not backdrop
the contest ignores. A Demotion-Magnitude trip from a mishandled Crisis is the **factual predicate** a
Parliamentary Censure motion (`HANDOFF_SC.md`, ED-SC-0015) or a Negotiation/Inquiry contest argues over.
The intended primitive: a resolution-quality Key past a threshold feeds the contest's Step-6 stakes and
opening resistance, so Parliament debates *what actually happened in the world* rather than an abstract
motion. **Honesty flag (§13):** canon's contest resolver (`social_contest_v30` §6, the Parliament
Persuasion-Track motion rule) has a "Define stakes" step but **no input hook that reads an external Key** —
so "opening Ob from the Key magnitude" is *this spec's proposal, not a found dependency.* Before this edge
is trusted it must be **earned** (author a `stakes.source_key` input the Step-6 stakes read) or **weakened**
to "a motion may *cite* the resolution Key as its narrative predicate" (real today, less mechanical). This
is the one edge where the spec caught itself reaching for a resemblance instead of a read/write dependency —
flagged rather than hidden.

### §6.3 · Faction Action  *(routes through Mandate — see §13)*
A run of well-handled Crises (positive signal, rising Mandate) unlocks an expansion/Muster window; a run
of mishandled ones (Mandate bleed) forces a defensive Consolidate/Suppress posture. The primitive is the
**canon path, stated honestly**: resolution Keys move settlement L/PS → **Mandate = Σ settlement L/PS**
(`settlement_layer §1.5`, canon) → domain-action availability already gates on faction stats. There is
**no separate "Key aggregate"** — §6.3 is real precisely *because* it routes through the Mandate
aggregation that already exists, not a new faction-level sum. Faction strategy is thereby downstream of
settlement-level event handling without a new track.

### §6.4 · Why these three are one mechanism
All three read the *same* §5 resolution-quality Key at three scales (personal FI lead, court-scale
contest, faction-scale window). That is the anti-reskin guarantee: FI/SC/FA "content" is not three
content pipelines to fill, it is **three subscribers to one signal.** Authoring an event authors all
three ripples at once.

---

## §7 · Cross-scale aggregation — individual to peninsula, and back

The design lead: *"how this can cause shifts in power over a region… ripples… that range in scale for
impact from the individual to the peninsula."* This is not a new axis to build — **`key_substrate_v30.md`
§2.1 already requires every Key to carry `scale_signature: [personal | settlement | territory | peninsula]`**,
the exact four-scale chain below. The substrate *already* stamps every state-change with the scales it
touches; §7 is the *aggregation read-convention* over that existing stamp, not new machinery. The four
management scales (proactive-projects docket §1) are a single **aggregation chain**, already partly canon:

```
INDIVIDUAL  ─(Disposition, consolidation_progress, Standing)─►  a character's rise/fall
    │  aggregates via the roster layer's clientele/patron edges
    ▼
SETTLEMENT  ─(L, PS, Prosperity, Order, Π)─►  a place's operation
    │  aggregates: Mandate = Σ settlement L/PS (settlement_layer §1.5, ALREADY CANON)
    │             faction Treasury = Σ settlement Prosperity ×10 (derived_stats §8.1, CANON)
    ▼
TERRITORY   ─(the connective tissue between settlements: shared AP pool, route network)─►
    │  the currently-UNBUILT scale — BYZ-6 (Consolidated Command) / IT-5 (Legation Split) are
    │  its two candidate mechanics (both needs_jordan); proactive-projects §3B proposes its menu
    ▼
FACTION     ─(Mandate, Accord, domain-action windows §6.3)─►  the polity's power
    │  aggregates to:
    ▼
PENINSULA   ─(a correlated world-layer: the concerns catalogue's "Cooling flag" §5 #15)─►
             region-wide shifts (a multi-settlement climate/economic shock that no single
             governor caused and none can fully answer)
```

**The aggregation is bidirectional** (already true in canon: Mandate feeds *back* to settlement L/PS,
`settlement_layer §1.5`). So a peninsula-scale shock (Cooling flag) pushes *down* into every
settlement's Π simultaneously, which pushes down into individual response burdens (§3), which push
*back up* through resolution Keys into faction Mandate — the loop closes across scale, not just across
time. A regional power shift is **the emergent sum of individual event-handling**, not a separate
strategic-layer mechanic.

> **Open ruling R-3 (Jordan):** the **Territory** scale is the one genuine architectural gap (the two
> unbuilt scales, org and territory, from the proactive-projects docket). BYZ-6 and IT-5 both propose
> multi-settlement authority but were held `needs_jordan` for exactly this reason. This spec's position:
> Territory should be authored as *the connective-tissue scale* (shared AP pool + route network +
> the resolution-Key aggregation that opens §6.3 windows), **not** as "a bigger settlement." That is a
> ratifiable design decision, not more research — R-3 is the highest-leverage ruling in this spec.

---

## §8 · Emergent-arc fuel — the loop's feedback edge

The design lead: all of this should *"provide content for emergent arcs."* Every ripple chain that
survives §9's test **is an arc seed** — a Key with a `follow_on` and a named actor whose standing moved
is exactly what `valoria-arc-generator` (CLAUDE.md §9) consumes. The feedback edge that closes the loop:

- A resolved chain **re-weights the deck** (a mishandled famine that demoted a governor raises the
  draw-weight of the successor's legitimacy-Crisis; a Grudge tag from a Defy biases the wronged NPC's
  Ambition card upward). This is already the Π/tag-modifier machinery (§2.2 `weight: base + Π-scaling
  + tag-modifiers`) — the substrate just requires resolution Keys to *write* those tag-modifiers.
- An arc is therefore **not authored** — it is the trace the loop leaves as the same five primitives
  compose over several seasons. The arc generator reads the Key log; it does not need a plot.

---

## §9 · What counts as a real primitive vs. pattern-matching (the discipline)

The whole spec rests on **five primitives** and nothing else. A proposed ripple/lever/mechanic is
real **only if it is a genuine read/write dependency over one of these**, not a thematic resemblance:

1. **Key emission** (`key_substrate_v30.md`) — every state-change is an emitted Key; the loop's bus.
2. **Ledger tag** (Precedent / Grudge / Debt / Reputation, + the audited Compact/Concession/Capital-
   Posture families) — durable state that biases future rolls and deck weights.
3. **Disposition** — the universal relationship scalar, per-actor.
4. **Π** (settlement pressure homeostat) — the event-draw governor.
5. **Standing / consolidation_progress** — the rank/advancement axis (player *and* NPC, §5 R-2).

**The test (applied ruthlessly, per the design lead's "avoid pattern matching, work from emergent
primitive logic"):** for any proposed connection between two things, ask — *is there a specific field
one writes that the other reads?* If yes, it's a primitive dependency and the ripple is real. If the
only link is "these are both about guilds / both about famine / both feel related," it is pattern-
matching and must be cut, however plausible. The NERS audit (`.../pessimist_ners_audit_v1.md`) found
this exact failure in ~15 of the 44 proposals (its §5 reskin clusters) — a "shared abstract shape"
repeatedly mistaken for a shared mechanism. This spec's §9 is the standing guard against re-committing
it: **shape is not mechanism; only a read/write dependency is.**

---

## §10 · Evaluation gates — the four success criteria, made checkable

The design lead's success criteria, turned into pass/fail gates every mechanic entering this substrate
must clear (anything failing **all four** is cut, not iterated):

| Gate | Passes if… | Reads |
|---|---|---|
| **Meaningful choice** | it presents a decision with a traceable consequence and no dominant option | Ω-d non-dominance; §3 vise |
| **Progression / regression** | it moves a visible trajectory (Standing, consolidation_progress, settlement stat) over a campaign, not just a per-season flutter | §5, §7 |
| **Parliament / contest content** | its resolution Key can become a citable contest predicate (§6.2) | §6.2 |
| **Emergent-arc fuel** | its Key carries a `follow_on` + named actor the arc generator can consume | §8 |

A mechanic that improves a stat but creates no choice, no trajectory, no contest predicate, and no arc
hook is content volume, not system — and is cut here regardless of how well-grounded its history is.

---

## §11 · What this spec asks Jordan to rule (consolidated)

- **R-1 (§2):** are the five new settlement levers in scope, or is settlement identity carried purely
  by the subnational-faction roster? (priority call)
- **R-2 (§5):** does a well-handled event let an **NPC contest a seat the player holds** (shared rank
  space)? (`player_seats_are_contestable` — the sharpest stakes call)
- **R-3 (§7):** author **Territory** as the connective-tissue scale (shared AP + routes + Key
  aggregation), folding BYZ-6/IT-5 into it? (the highest-leverage architectural ruling)
- **R-4 (§14.2):** the event-deck draw's **discrete band-cliffs** (Π 7→8 flips Intrigue→Crisis) — an
  intended dramatic threshold, or softened with a transition band? (the one resolution-diagnostic P-iii
  finding gating the deck-draw engine's ratification)

None of the four needs more research. Each is a taste/scope/architecture decision this spec has framed to be
ratifiable as-is. Everything else in the loop is wiring over primitives and contracts that already exist —
verified against `module_contracts.yaml`, the resolver enum, and the resolution diagnostic in §14.

---

## §12 · Immediate consequences for the open PR (from the NERS audit)

The audit (`designs/audit/2026-07-11-comparative-governance-pessimist-ners-audit/`) found two of the
12 authored-into-canon proposals are **defective as-authored** and this spec explains *why* in loop
terms:

- **SE-JP1 (Goningumi, §1.3b)** — MERGE. Verified substrate incoherence: partitions Local Actors into
  5-household cells, but `settlement_layer §4.5` gives 1–2 Local Actors/settlement. In loop terms: it
  tried to add a §2 lever (collective-liability cell) *below* the granularity the settlement model
  supports. Retire §1.3b; if the enforcement idea is wanted, it belongs as a Force-method elaboration,
  not a new sub-population layer.
- **CHN-9 (Kaochengfa, §1.0d)** — MERGE. It is a patron-scoped instance of the **§5 general standing
  bridge**, authored as a standalone toggle. Fold its season-count escalation into §1.0a's general
  Demotion rule (which §5 already requires building); drop the promotion clause (asserted, no rule).

Both are the *same lesson this spec exists to prevent*: a mechanic authored as its own subsystem when
it is really one configuration of a shared primitive. Building §5's general bridge makes CHN-9 a
three-line configuration, not a section — which is the whole argument for the substrate.

---

## §13 · Self-audit — grading the loop edges against this spec's own §9 test

§9 sets a hard bar: a connection is real only if *"there is a specific field one writes that the other
reads."* Intellectual honesty demands the spec meet its own bar. Grading each loop edge against actual
canon (verified this pass, not asserted) yields a mixed result the spec must state plainly rather than
paper over — an edge graded **WIRED** composes today; **HOOK-NEEDED** has a real read-target but needs one
explicitly-authored input clause (not more research — one clause); **AT-RISK** is currently closer to
pattern-matching than a verified dependency and must be earned before it is trusted.

| Loop edge | Grade | Verified against canon | What it still needs |
|---|---|---|---|
| Event → settlement operation (§4) | **WIRED** | `governance_play_redesign_v1.md` §2.1–2.3 — cards trigger on stat predicates; already canon | — |
| Settlement → Mandate → faction (§7) | **WIRED** | `settlement_layer §1.5` (Mandate = Σ L/PS) + `derived_stats §8.1` (Treasury = Σ Prosperity×10) — both canon | — |
| Cross-scale stamping (§7) | **WIRED** | `key_substrate §2.1` `scale_signature: [personal\|settlement\|territory\|peninsula]` — the four scales already on every Key | — |
| Event → FI lead (§6.1) | **WIRED** | `Investigate` reads "concealment" (§1.3); CHN-3 Clerk-Corruption is an existing event→hidden-counter→Investigate chain | — |
| Event → standing (§5) | **HOOK-NEEDED** | §1.0a Demotion Triggers read state ("3 consecutive Duty failures," "Disposition −3," "inner-circle majority turning") — real read-targets, but **none reads a per-event resolution signal today** | one authored §1.0a trigger clause: *"a settlement resolution_quality Key below threshold, on a Directive-bound seat, counts as a Duty failure"* — until authored, §5 is not "already wired," it is *one clause from wired* |
| Faction-action window (§6.3) | **HOOK-NEEDED** (via Mandate) | domain actions gate on faction stats (canon); Mandate bleed from §7 is real — but there is **no separate "Key aggregate"**; §6.3 is real *only* routed through Mandate | reframe §6.3 as "reads the **Mandate** delta (§7)," not "the settlement-Key aggregate" — the honest path is the canon one |
| Event → Parliament/SC predicate (§6.2) | **AT-RISK** | `social_contest_v30 §6` "Define stakes" step + `§...` Parliament resolver ("Persuasion Track ≥7 = motion passes") **exist**, but **no hook reads stakes/opening-Ob from an external Key** — "opening Ob from the signal magnitude" is *this spec's proposal, not a found dependency* | either author a real hook (a contest `stakes.source_key` input the Step-6 stakes and opening resistance can read) **or** downgrade §6.2's claim to "a Censure motion may *cite* a resolution Key as narrative predicate" (weaker, but honest) — as written §6.2 is the one edge that would fail this spec's own §9 test |
| Arc feedback → deck re-weight (§8) | **HOOK-NEEDED** | tag-modifiers on card weight are canon (§2.2 `weight: base + Π-scaling + tag-modifiers`); resolution Keys writing those modifiers is the one added step | one convention: resolution Keys write a tag-modifier delta on the settlement's future draws |

**The honest headline:** the loop's **spine is wired today** (event→settlement→Mandate→faction, plus
cross-scale stamping and the FI ripple — five of eight edges compose on current canon). Two edges are
*one authored clause* from wired (§5 standing, §8 arc-feedback), and §6.3 just needs to be *reframed onto
the canon Mandate path it already has.* **Exactly one edge — §6.2, event→Parliament — is currently
AT-RISK of being the pattern-matching §9 condemns**, because I asserted an "opening-Ob-from-Key-magnitude"
dependency that canon does not have. That edge must be *earned* (author the `stakes.source_key` hook) or
*weakened* (a motion merely *cites* the Key) before it is trusted. Flagging it here, against the spec's own
test, is the difference between a substrate and a wish.

> **Consequence for §11's rulings:** R-2 (can an NPC contest a player-held seat) presupposes the §5 edge,
> which is HOOK-NEEDED — so R-2's *architecture* is one clause away, not zero. And the §6.2 AT-RISK edge is
> the one place this spec asks to be checked hardest before authoring, because it is the one place the spec
> caught *itself* reaching for a resemblance instead of a dependency.

---

## §14 · Architecture compliance — module contracts, resolver shapes, resolution diagnostic

A mechanic that "reads well" but has no legal Key IN → resolver → OUT shape is not implementable. This
section binds every arc of the loop to `references/module_contracts.yaml` (the IN→resolver→OUT registry,
governed by `valoria-module-adjudicator`), the fixed resolver enum, the Key Type Registry vocabulary, and
— for anything that resolves via a draw — the resolution diagnostic (`valoria-resolution-diagnostic`,
NERS resolver-stress P-i…P-v). **Verified against the actual contracts this pass, not asserted.** Two
findings up front, both favorable: the standing bridge needs *no new Key type*, and the card branches need
*no new resolver*.

### §14.1 · The loop, mapped to module contracts (owner · resolver · Keys)

| Loop arc | Owning module (`module_contracts.yaml`) | Resolver (fixed enum) | Keys IN → OUT (registry vocabulary) | Compliance |
|---|---|---|---|---|
| Event draw (§4) | `scene_slate` surfaces (manifest); driven by `settlement_layer` state + env shocks | **weighted-event table** — *not* in the enum; a draw | IN: `settlement_layer` state (Π, Order…) + `env.disaster` / `env.peninsular_strain_shock` (registered) → OUT: a drawn card | **NEW ENGINE** — diagnose by P-i…P-v (§14.2), surface for ratification |
| Settlement impact (§2) | `settlement_layer` | `deterministic_accounting` | writes `Prosperity/Order/Defense/L/PS` tracks (all `writable: true` in the contract) | the 5 new levers (§2) = new `state:` rows (`bucket: track`) on `settlement_layer` — a **contract edit to surface** (R-1) |
| Response resolution (§3) | `domain_actions` (governance verbs / Directive) | **`d_sigma`** (ED-874: legible odds, flat +10%/pt uniform-P-ii, FLOOR .05/CAP .90, FAIL_FLOOR .97 graded-P-iv) | IN: player choice → OUT: `da_outcome.*` (registered) | **WIRED** — reuses the ratified deterministic+stochastic resolver; social/Hold-Court branches route to `social_contest` `dice_pool` (5–18D, "keep dice") |
| Standing bridge (§5) | `faction_politics` | `deterministic_accounting` | IN: consumes the `da_outcome.*` / `scene.*_resolved` Key (carrying `resolution_quality` on its impact_vector) → OUT: **`state.standing_change`** (ALREADY REGISTERED, already emitted by faction_politics) | **NO NEW KEY TYPE.** The only new thing is one *consumes-edge* (faction_politics ← settlement resolution Key) — a finding to surface, not a subsystem |
| FI ripple (§6.1) | `scene_slate` / `fieldwork_knots` | `manifest` / `dice_pool` | a negative-resolution Key raises the concealment inventory the `Investigate` (`dice_pool`, `investigation_systems`) resolver reads | **WIRED** — CHN-3 Clerk-Corruption is the existing precedent |
| SC ripple (§6.2) | `social_contest` | `dice_pool` | would need a NEW `consumes: {stakes.source_key}` edge | **AT-RISK** (§13) — the contract has no such consumes-edge today; author it or weaken to "cite" |
| FA ripple (§6.3) | `faction_state` | `deterministic_accounting` | via `settlement_layer`'s existing **Mandate derivation** → `faction_state` | **WIRED via Mandate** (the derivation is in the contract, §1.8 LPS-2e) |
| Aggregation (§7) | `settlement_layer` → `faction_state`; `peninsular_strain` | `deterministic_accounting` | `scale_signature` on every Key (registered); `env.peninsular_strain_shock` (registered) | **WIRED** — the Mandate rollup + peninsular_strain shock both already in-contract |

### §14.2 · Resolution diagnostic on the event-deck draw (the one NEW engine)

`valoria-resolution-diagnostic` §"new engine" rule: *a card/deck draw / weighted-event table is diagnosed
against P-i…P-v directly and surfaced for ratification.* Running it on the Π-weighted draw
(`weight = base + Π-scaling + tag-modifiers`, band-gated 0–2 / 3–7 / 8–10):

| Property | Verdict | Reasoning |
|---|---|---|
| **P-i legible odds** | **PASS (band) / PARTIAL (card)** | Π legibly maps to the family band (the player reads high Π → Crisis). The *specific* card is tag-weighted — legible only if active tag-weights are surfaced in the UI (a tooltip). Mitigation: surface the draw-weight contributors. |
| **P-ii uniform leverage** | **PASS** | A weighted-event table has **no pool / no √N term** — exempt from the flat-shift `1/√N` trap by the diagnostic's own scope rule (a no-pool resolver has no √N). A tag's draw-weight contribution is uniform across Π. |
| **P-iii bounded + monotonic** | **⚠ FINDING** | The band thresholds are **discrete cliffs** — Π 7→8 flips the draw from the Intrigue band to the Crisis band, a continuous input crossing a discrete boundary that jumps the outcome class (the ED-884-class concern). **Ruling needed:** intended dramatic threshold, or soften with a transition band (7–8: both bands draw, Crisis-weighted). |
| **P-iv graded, recoverable** | **PASS** | The draw is a *selection*, not a fragile binary; the card's *resolution* is graded through `d_sigma` (FAIL_FLOOR .97 — ≥3% residual even at overmatch). No irreversible bare-binary on the draw. |
| **P-v right engine** | **PASS** | A weighted-event table is the correct shape for *event selection* (not a dice pool, not a skill contest). Tag `[NEW ENGINE — surface for canon ratification]` per the diagnostic. |

**Net:** the deck draw is compliant on four of five properties; the single **P-iii band-cliff finding** is the
one thing that must be ruled (intended vs softened) before the draw is ratified as a canonical engine. This
is exactly the kind of result the resolution diagnostic exists to surface — a real finding, not a rubber stamp.

### §14.3 · Findings to surface (not silently resolved — the adjudicator discipline)

`module_contracts.yaml`'s own discipline: *cross-doc edges are kept VISIBLE as findings, never normalized
silently.* This spec therefore **surfaces, does not auto-edit**, the contract deltas it implies:

1. **New consumes-edge:** `faction_politics ← {type: da_outcome.* / scene.*_resolved, from: [domain_actions, settlement_layer]}` — the §5 standing bridge. (No new Key type; `state.standing_change` OUT already exists.)
2. **New state rows on `settlement_layer`:** the 5 levers (§2), `bucket: track` — gated on R-1.
3. **New consumes-edge on `social_contest`:** `{type: stakes.source_key}` — the §6.2 AT-RISK hook; author or drop.
4. **New engine to ratify:** the Π-weighted event-deck draw (§14.2), with the P-iii band-cliff ruling attached.
5. **Any Key type a generated card emits that the registry lacks** is a *finding to surface*, never a silent
   new type — per the transcription discipline. The card compliance pass (§14.4) enforces this per card.

None of these is edited into `module_contracts.yaml` here — that is a `valoria-module-adjudicator`
ratification step (contract edits follow doc authoring + Jordan sign-off), and doing it silently would
violate the registry's own visible-findings rule.

### §14.4 · Binding requirement on the in-flight event-card deck (and all future mechanics)

Every card in the generated deck (and every mechanic anywhere in this program) is **not compliant until**
it carries, explicitly: (a) its **owning module** + **resolver** from the enum; (b) **registry-valid Key
types** for everything it emits/consumes, with any gap surfaced as a finding; (c) for any card that
resolves via a **draw** (the deck draw, or a `dice_pool` branch), a **resolution-diagnostic P-i…P-v verdict**.
A dedicated **architecture-compliance pass** runs over the surviving deck to attach exactly these three
things per card — a card with a real impact but no legal IN→resolver→OUT shape is a design sketch, not an
implementable mechanic, and is held until shaped. This section is the gate that gets applied to it.
