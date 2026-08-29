# 06 — Faction management: ethos, divergence, blocs, and being at a tier

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md) ·
## [`01_substrate_primitives_part2.md`](01_substrate_primitives_part2.md) ·
## [`05_faction_actions.md`](05_faction_actions.md) (acting at a tier — this page is *being* at a tier) ·
## canon: `systems/factions/faction_politics_v30.md` (PP-660, CANONICAL) ·
## `systems/settlements/settlement_layer_v30.md` (CANONICAL) ·
## `systems/npcs/npc_relational_graph_v30.md` (PP-724)
## Produces: what a faction **is**, how it disagrees with itself, what it is worth at each tier, and how it ends
## Continues in: [`06_faction_management_part2.md`](06_faction_management_part2.md) — §§5–11

**This document is in two parts, in reading order** (`CLAUDE.md` §4 — sequential parts, never
index+infill; the single file exceeded the suite's token cap). **Part 1** — the `## Overrides` block,
what a faction is, ethos and divergence, blocs, and being at a tier (§§1–4).
**[Part 2](06_faction_management_part2.md)** — the six political compositions, posture, collapse by gate,
the module contracts, the loops and the property audit (§§5–11). **Section numbers run continuously
across both parts, and every `§n` cross-reference resolves across both.**

**Change C.** `05` owns what a faction *does*; this page owns what it *is*. Everything here is a
composition of `01`'s four primitives plus the form bucket. **No new stored kind is proposed, no new
registry file is proposed** (`00 §9`'s two-file ceiling holds), and this page adds **one** player verb.

**Every number below is a shape proposal, not a ledger constant** — a band edge, a weight or a dwell
written so the shape is checkable, not because a register backs it. Where a number *is* backed, it is
cited by `path:line` and named as canon's. Nothing here invents a number and presents it as ratified.

---

## Overrides

**The authority model this block is written under (Jordan, 2026-08-29, mid-suite):** *"existing work is
not necessarily required to keep all the way through to things like obstacles being stat/2 or whatever
is ratified and canon"* · *"I just want the best possible proposal."* **Nothing in the tree is out of
bounds** — not ratified canon, not a prior ruling. Tier no longer decides *whether* something may be
overridden; it decides **how strong the argument has to be**. The one hard rule is unchanged: **an
override is explicit, listed and argued, and silence is the only thing forbidden.**

The counterweight binds equally, and it is the one this page acted on more often: **re-deriving a worse
version of a shipped design to keep authorship is its own failure.** Three of the six rows below are
this page adopting or restoring something it did not write, because the existing thing is better. Where
this page keeps a ruling, it keeps it **because the ruling is right**, and says why — never because it
is a ruling.

Listed, tiered and argued (`00 §5.3` collects them so each can be vetoed individually).

| # | What is overridden | Tier | Why |
|---|---|---|---|
| **C-1** | v1 `06 §3`: *"a faction's character is who holds its head post … swap two factions' names in the starting data and nothing else changes, because there is nothing else to change"* | this suite's own v1 | It is the ARCHIVED critique's root cause C. Deleting the per-faction branch was right; replacing it with nothing left **no institution for anyone to be in tension with** and no continuity across a succession. Corrected by `identity.ethos` + derived `divergence` (§2) — still no `if faction == X` anywhere |
| **C-2** | v1 `06 §5`'s three orthogonal policy rows (fiscal stance · muster stance · succession rule) | this suite's own v1 | `01 §1.1` gives a faction **exactly one** form field, `posture`, and `01 part 2 §12` lists it as the only faction row in `substrate.form`. Three switches cannot land. They become **one posture value per row in the form registry**, each row carrying its own fiscal, muster and succession terms — `00 §1`'s "one object with a registry of kinds" corollary (§6) |
| **C-3** | v1 `06 §2`'s provisional `faction.acceptance` derivation | this suite's own v1, **superseded on merit by ratified canon** | `settlement_layer_v30.md:158-171` already ships a size-weighted, **saturating**, settlement-sourced aggregate with a calibrated constant and a 30-season convergence result (`:173`). v1 invented a weaker one beside it. **Adopted whole** (§4.2) — not because it is canon, but because nothing this page could design without a sim would beat a calibrated saturating form with a convergence result attached. Q-4's *name* question stays open and untouched; what closes is the invention of a second arithmetic |
| **C-4** | v1 `06 §6`: *"There is no collapse procedure, no elimination check … A faction that stops acting can **always** produce a claimant"* | this suite's own v1, **plus a narrow amendment to the delta spec's §9.5 carry-forward** | The restored end condition is at `settlement_layer_v30.md:1077` — *"if the faction leader is killed or captured and no successor exists with Standing 4+, the **faction dissolves**"* — but it is kept **because it is right**, not because it is canon: a world that cannot lose an institution cannot gain one in its place, and v1's arrangement left a faction that can neither act nor end. §7 restores the end **as a gate with a dwell**, keeps the recoverability §9.5 carries forward, and does so by narrowing what the immortal seat node guarantees. **This is the one place this document amends a §9 carry-forward; flagged loudly rather than folded in** |
| **C-5** | v1 `06 §4`'s bespoke faction↔faction `disposition` gauge and `hostility()` sum | this suite's own v1, superseded by `01 §7` | Faction enmity is now a `treaty` edge (or its absence) in the shared container with per-kind semantics, and `01 §7.3` already forbids the stored aggregate v1's disposition term was. Target selection is `05`'s, reading edges; this page does not restate it |
| **C-6** | `settlement_layer_v30.md:165`'s **fixed 50/50 blend** `q_s = 0.5·L_s + 0.5·PS_s`, taken *before* aggregation | **ratified canon — a narrow amendment, proposed and flagged, NOT taken unilaterally** | The same document keeps **aggregate L and aggregate PS separate** at `:170` *because consumers need them separately*, then discards the distinction one line earlier by pre-blending. Institutional acceptance and popular backing are the two axes this setting is *about* — a chartered Church with L 6 / PS 1 and a Restoration cell with L 1 / PS 6 are opposite objects and this blend makes them identical. **The better shape is to aggregate the two axes separately and blend at the consumer**, where the weight is the consumer's question. ⚠ **This invalidates canon's calibrated `K = 6` and its Stage-4 convergence result** (`:166`, `:173`) — a re-calibration is a sim job, not a proposal's. So §4.2 ships canon's blend **as-is** and this row records the amendment as a **flagged proposal for the SE lane**, with the reason it is not taken here stated plainly: an unre-calibrated improvement is worse than the thing it improves |

### Kept because they are right — recorded, since deciding not to override is also a decision

Under the amended authority model these were re-examined on merit rather than inherited.

- **ED-POL-11** (`systems/factions/faction_politics_v30.md:1093`) — *"Patronage is political/institutional;
  Knot is spiritual/personal … **do not conflate**."* **Kept, and it is right.** `01 §7.5`'s per-kind table
  shows the two are not magnitudes of one another: a Knot's disposition is *stored*, an NPC↔NPC edge's is
  *derived*; a Knot's strain is a different object with different bounds; a Knot *ruptures* where a
  patronage *breaks*. Letting a Knot assemble a court faction would make a Thread-constituted binding into
  a strong political tie, which is exactly the conflation, and it would also make the Warden ladder — whose
  whole point is Thread Sensitivity — silently the best route to political power.
  **But the ruling's reach is narrower than "Knots are politically inert", and this page takes only what
  it needs:** `knot` is excluded from **bloc connectivity** (§3.2) and from nothing else. A Knot still
  moves a person's convictions through a conviction scar (`01 §7.5`), and those convictions still feed
  `practice`, `divergence` and `05`'s `appeal`. A Knot changes what an officer *believes*; it never
  decides which wing they are in. That is the distinction ED-POL-11 is protecting, stated as a mechanism.
- **PP-724 §7–§8**'s defection cascade (`:501-528`) — **kept, and adopted rather than rebuilt.** It already
  ships hop-attenuation, a capped-and-decaying gain term, a player brake and a hard depth cap, with an
  explicit no-double-count clause. Anything this page wrote would be a worse version of it. Its own
  `[NEEDS TESTING — SIM-DEFECT]` caveat is carried forward unupgraded (§9.1).
- **PP-724's six edge kinds as the bloc-connectivity basis** — kept, and each earns its place rather than
  being inherited wholesale (§3.2).
- **ED-IN-0201**'s no-leader-no-action gate — `05`'s, read here and not restated.

---

## 1. A faction is a composition, and almost nothing about it is stored

```
Faction (entity kind: faction — 01 §1.1)
├── identity   IMMUTABLE
│   ├── seat_node       tier node id. Cannot be lost (carried from v1 05 §1.2; see §7.3 for
│   │                   exactly what that guarantees and what it does not)
│   ├── charter_season  when this institution began. Identity, so a re-founded faction is a
│   │                   NEW entity with a new charter season — which is what makes a Restoration
│   │                   a claim rather than a resumption
│   └── ethos           {conviction: weight} — what the institution is FOR (§2.1)
├── form       posture — one value from a declared registry row; moved only by a form transition (§6)
├── tags       Precedent · Grudge · Debt · Reputation · Leverage (the faction's ledger)
├── gauges     NONE owned at faction scale. Every continuous faction quantity is DERIVED (§4).
└── posts      the interior: different kinds, different holders, different remits, different convictions
```

**Four things v1 stored that are now derived, and one that moved bucket.**

| v1 stored | v2 | derived from |
|---|---|---|
| `holdings: [tier node id]` | **derived** | the places whose governance post's `principal` is this faction (§4.1) |
| `policy: {fiscal, muster, succession}` | **one form field** | `posture`, a registry row carrying all three terms (§6, C-2) |
| `faction.acceptance` as a bespoke aggregate | **derived, canon's arithmetic** | `settlement_layer_v30.md:165-171` (§4.2, C-3) |
| faction↔faction `disposition` gauge | **an edge** | `01 §7` — `treaty` kind, per-kind semantics (C-5) |
| a faction's character | **derived** | `distance(ethos, practice)` (§2.3) |

**Every quantity a faction has is derived, and that is AU-1 made structural, not remembered.** There is
no `Faction.stat` to write because `01 §2.1`'s four write leaves contain no faction scalar. The
enforceable form is `writable: false` on every derivation row in §8.

⚠ **A wart, named rather than hidden.** `00 §7`'s contract schema requires every `state:` row to name a
bucket from `entity | gauge | tag | post`, and **a derivation is stored in none of them**. v1 wrote
`bucket: gauge, writable: false`; this page keeps that shape for continuity, and closes the hazard it
opens with a falsifier instead of a fifth bucket: **no `writable: false` state name may appear as a
gauge id in `references/descriptor_registry.yaml`.** A derivation that acquires a gauge instance has
become a stored aggregate, and that test catches it at load. Reported to `01` as a schema gap.

---

## 2. Ethos, practice, and the divergence between them

This is the headline of change C: **internal conflict between a faction's ethos and the people who
operate inside it.** It needs no conflict subsystem. It needs one immutable vector, one derivation, and
a distance.

### 2.1 Ethos — identity, not drift

`identity.ethos` is a weight vector over the canonical Convictions, resolved through
`descriptors.resolve_conviction`, which **raises** on an unknown name rather than silently scoring zero
(`01 §1.2`, `engine/substrate/descriptors.py:194-206`). **This page names no conviction literally.**
Weights are normalised to `Σ|w| = 1`, so the distance in §2.3 is bounded by construction rather than by
a clamp.

Ethos is **immutable** because an institution's purpose is what makes it the same institution across a
succession. A faction whose ethos moved with its head post would have no purpose to betray — v1's
error. What moves is **practice**, and the gap is the mechanic.

*Emergent possibility lost if ethos were cut:* an institution could never betray its own purpose, no
believer could be at odds with their own church, and a succession could not change anything except a
name.

### 2.2 Practice — one derivation, three consumers

```
practice(S)  =  Σ_{p ∈ S, seated}  w(p) · conviction_projection(holder(p))
                ────────────────────────────────────────────────────────────
                Σ_{p ∈ S, seated}  w(p)

w(p) = weight(post.kind)          # a content_registry block; a shape proposal, six closed kinds (01 §4)
```

`practice` is defined over **any set of posts**, and that is the whole reason blocs cost nothing extra:

| consumer | `S` | reads |
|---|---|---|
| **`divergence`** (§2.3) | every seated post of the faction | how far the institution's operators have drifted from its charter |
| **`bloc.pull`** (§3) | the bloc's member posts | how far *this wing* stands from the charter |
| **`05`'s `appeal`** | the acting post-holder alone | the `w_hold` term — **`05` owns that formula; this page supplies the vector and stops** |

**Vacant posts contribute to neither numerator nor denominator.** A faction with one seated officer is
fully described by that officer, which is correct: an institution operated by one person *is* that
person's practice, and the Silent band (§7) is where that fact becomes visible.

### 2.3 Divergence — derived at read, never stored

```
divergence(f)  =  ½ · Σ_axis | ethos_f[axis] − practice_f[axis] |        ∈ [0, 1]
```

Total variation between two normalised vectors. Four properties, each load-bearing:

1. **Bounded by arithmetic, not by a clamp.** Both operands are normalised, so the result lies in
   `[0,1]` for every possible faction. No floor, no ceiling, no reachability question — a **P-iii pass
   that needs no campaign run**, on the same footing as `01 §5.1`'s gauge bound.
2. **Never stored.** `resolver: derivation`, `writable: false`, no gauge instance, no tag. It is
   recomputed at every read from posts, holders and identity — all of which are primitives with owners.
   A stored divergence would be **an aggregate with a setter**, which AU-1 forbids and which is exactly
   the failure `01 §7.3` caught v1 committing on edge disposition.
3. **Undefined, not zero, at zero seated posts.** `practice` has an empty denominator, so `divergence`
   returns `None`. **Every consumer treats `None` as "no institution to diverge from"** and declines to
   fire; a faction in that state is in §7's Silent band and its live question is succession, not schism.
   Stated because a silent `0.0` would read as *perfect alignment* — the maximally wrong answer.
4. **Monotone in the aggregate, deliberately NOT monotone in one officer's distance.** Divergence rises
   as practice moves away from ethos, by construction. It does **not** rise every time an individually
   heterodox officer is seated: an officer extreme in the *opposite* direction from the current drift
   genuinely pulls the institution back. That is why appointing a hardliner is a real reform move and
   not a slogan, and it is the property a naive `mean(|officer − ethos|)` would destroy.

### 2.4 What divergence gates — because a measure that gates nothing is decoration

| gate | reads | fires | owner |
|---|---|---|---|
| **bloc formation** | `divergence ≥ θ_form` **and** a qualifying edge component (§3.2) | a `bloc` entity is created, `state: latent` | `fm.bloc`, this page |
| **schism** | a bloc at `state: open` whose `bloc.pull > divergence` by `θ_schism`, cohesion above band, for `dwell` seasons | `bloc.state → in-schism`; the bloc's project (`09`) becomes a founding claim (§3.5) | `fm.bloc` |
| **posture change** | `divergence` band gates *which* posture rows the head may transition to (§6) | a divergent institution cannot adopt a posture its own officers will not operate | `fm.posture` |
| **candidate weighting at succession** | — | **NOT this page's.** `04` owns `pm.candidates` and its caste gate; `12` owns succession. This page supplies `ethos` and `practice` and stops | `04`, `12` |

The third row is the one worth reading twice. It is not a penalty and it is not a modifier on a roll: it
is `01 §4.3`'s `remit`-as-gate applied to an institution instead of a person — **the option set narrows,
the odds do not move.** A faction whose operators have drifted far from its charter finds that some of
what its charter allows is simply not on the table, and the way to widen the table is to change who is
seated. That is the mechanic v1 had no object for.

### 2.5 Disclosure

`divergence` and `bloc.pull` present as **bands, never numbers**; their **inputs are published** (who
holds which post, and each holder's conviction weights to the granularity `02` discloses them); the
**band edges that gate schism are hidden** (`01 §8`). A player can see the whole court and read the
strain in it; they cannot read off the season it breaks.

---

## 3. Blocs — the object between "faction" and "post"

`bloc` is `01 §1.1`'s sixth entity kind. **Substrate** (`00 §2.1`): the player never opens a bloc
manager. They meet a bloc as *"the Ehrenwall wing is against you and you can feel it in every
appointment"* — a situation on the Slate (`10`), never a screen.

```
Bloc
├── identity   faction_ref · formed_season                       IMMUTABLE
├── form       members [post_id] · state ∈ {latent, open, in-schism, reconciled, dissolved}
├── gauges     cohesion   — THE ONLY ONE (01 §5.2)
├── tags       its record: which motions it carried, who it passed over
└── project    at most one, owned per 09
```

**Keep it minimal, and here is what "minimal" cost.** A bloc has **no ethos of its own** — its position
is `practice(members)`, the §2.2 derivation applied to a subset. It has **no treasury, no footing of
its own, no posture**. It is not a second faction; adding any of those would make it one, and then the elegance
failure is two objects doing one job.

*Emergent possibility lost if the bloc were cut:* there is no object between a faction and a post, so a
court of influence, a wing, a succession party, a coalition purge and the graduated autonomy of a
military order are all **untypeable** — faction politics collapses to individuals disagreeing with no
way to act together.

### 3.1 Membership is posts, not persons — and that is what makes it survive a succession

A bloc's `members` are **post ids**. A wing that loses its founder but keeps the seats is still the
wing; a person who resigns their post leaves the bloc by leaving the post. Storing persons would make
every bloc dissolve on the first death and would put the same fact in two places (a person's membership
and their post's).

### 3.2 Formation is a gate over the edge graph — never a bespoke rule

At the accounting boundary, `fm.bloc` reads state (**no Key consumption — see §9.3**):

```
candidates(f) = { seated posts p of f  :  distance(conviction(holder(p)), ethos_f) > divergence(f) }
components    = connected components of candidates(f) under PP-724's SIX political edge kinds
                {sworn-bond, liege-vassal, kinship, patronage, rivalry, feud}  — NEVER knot (ED-POL-11)
gate          = divergence(f) ≥ θ_form  AND  |component| ≥ 2  AND  component is coherent:
                max pairwise conviction distance within it ≤ θ_coherence
```

Three things this buys that a bespoke rule would not:

1. **The patronage network *is* the court.** A wing forms where the ties already run, so who cultivated
   whom over the last twenty seasons decides which wing exists — emergent, not authored.
2. **ED-POL-11 is honoured by construction, not by discipline.** `knot` is absent from the connectivity
   set, so a spiritual tie can never assemble a political bloc. The rule is in the gate, not in a
   sentence someone must remember.
3. **A rivalry edge can hold a bloc together.** PP-724 ships `rivalry` and `feud` as edge kinds with
   negative valence (`:56`), and connectivity does not care about sign — two officers bound by a shared
   feud against a third are one component. That is a real court dynamic and it costs nothing.

**All six kinds are admitted, and each earns it rather than being inherited wholesale** — the set was
re-examined rather than adopted on PP-724's authority. `patronage` and `liege-vassal` are the direct
political spine. `sworn-bond` is the oath-brotherhood that outlives the office. `kinship` is the single
most historically standard way a court faction assembles, and excluding it would make marriage
politically inert in a setting that has a marriage-to-treaty converter (`01 §7.4`). `rivalry` and `feud`
enter for the reason above. **The one kind excluded is `knot`**, and that exclusion is argued on merit in
the `## Overrides` block's *kept because they are right* list, not taken from the ruling's authority.

⚠ **`θ_coherence` is the bar against the degenerate case**: without it, every disaffected officer in a
large faction is one component and the "bloc" is just "everyone who disagrees" — an object with no
position. **Reachability bar, both directions:** at the maximum reachable divergence, a faction must be
able to produce **two or more distinct components**, and at low divergence it must produce **none**. A
θ pair that yields exactly one bloc at every divergence is a decoration, not a gate.

### 3.3 `cohesion` — the only gauge, and what it is for

Declared in `descriptor_registry.yaml` (`01 §5.2` already lists it), owner `bloc`, geometric decay per
`01 §5.1`, so it is bounded at `rest + a/λ` and checked at declaration with no campaign run.

| deposits into cohesion | reads |
|---|---|
| **+** members' posts voting or acting together; the bloc's project (`09`) advancing; a member promoted | outcomes that already fire and already know both parties, so provenance is free (`01 §3.3`) |
| **−** a member passed over at `pm.appoint`; a `rivalry` edge forming *inside* the component; the project lapsing; a member's post falling vacant | ditto |

**Cohesion is not a hit-point track and does not decide anything by hitting zero.** It is one input to
the state gates in §3.4 — every one of which also reads membership and divergence.

### 3.4 States, and the transitions between them

Rows in `references/form_registry.yaml` (`00 §9`); every one is a **gate, never a roll** (`01 §2.2`).

| transition | gate | reversible | hysteresis |
|---|---|---|---|
| *(creation)* → `latent` | §3.2's formation gate | — | — |
| `latent` → `open` | cohesion ≥ θ↑ **and** the bloc has declared a project (`09`) | **yes** | **REQUIRED**: `θ↑ − θ↓ ≥ H_MIN(cohesion)`, `dwell ≥ 1` |
| `open` → `latent` | cohesion ≤ θ↓ | yes | as above |
| `open` → `in-schism` | §2.4's schism gate | **no** — terminal for this bloc | not applicable |
| `open` → `reconciled` | divergence falls below θ_form **or** the faction's posture moves to one the bloc's practice supports | **no** | — |
| any → `dissolved` | fewer than two seated members for `dwell` seasons | **no** | — |

**Why `latent ↔ open` must have a band and the others must not.** It is the one reversible pair here,
and `01 §2.3` is exact about the failure: a cohesion gauge sitting on a single threshold **oscillates
every season** under ordinary play, emitting a `form.transitioned` Key each time, each of which is a
Slate candidate. That is not a tuning problem; it is a property of the shape, and it would flood the
one surface this suite has. The other four are irreversible by design — a schism does not un-happen,
and a dissolved bloc is done. A later wing is a **new bloc entity**, which is correct: it has a
different founding season and a different membership.

### 3.5 Schism is where a new faction comes from

At `in-schism`, the bloc's project (`09`) becomes a **founding claim**, and what happens next is not
this page's to script:

```
bloc in-schism  ──►  its project fires (09) or lapses
                     │
      fires:         a NEW faction entity is chartered — new charter_season, a seat node,
                     and ethos = practice(bloc members) FROZEN at the schism season
                     │
      lapses:        the bloc's members' posts stay where they are; the bloc dissolves;
                     the faction keeps a Precedent tag recording the attempt
```

**The new faction's ethos is the old faction's practice.** That is the whole shape of a schism in one
line — the wing that thought the institution had betrayed its purpose founds one whose purpose is what
the institution was actually doing. It is also why ethos must be immutable: if the parent's ethos could
drift, a schism would be indistinguishable from a policy argument.

⚠ **The chartering act itself is `05`'s**, not this page's — creating an entity is generation
(`00 §4.1`), and canon already owns the shape at `settlement_layer_v30.md:1046` (a formal Declaration
with a roll and an obstacle). This page supplies the **ethos vector** the new faction is founded on and
the gate that makes the moment arrive. **This is faction emergence with no faction-emergence
subsystem.**

---

## 4. Being at a tier — the multi-scale derivation

`05` owns **acting** at a tier: no post-holder at a tier, no action at that tier. This section owns
**being** at a tier, and it is one function evaluated at different nodes — not three quantities.

### 4.0 ⚠ A naming collision this document nearly shipped, caught and fixed

The obvious word for this quantity is *standing*, and **the tree already has two live meanings for it**:

| # | what it names | where |
|---|---|---|
| 1 | a **person** gauge — the public half of a person's reputation, paired with `exposure` | `01 §5.2` |
| 2 | a **person's rank inside one faction**, the ratified 0–7 ladder with per-rung gates, demotion magnitudes and a −1 dismissal | `systems/factions/faction_politics_v30.md:38`, `:61-94` |

A third, faction-scoped, multi-scale meaning is exactly how the tree acquired three readings of Combat
Pool and two of Mandate — the disease `00 §5.3` says this suite exists to stop. **This document's
derivation is therefore named `footing`**, which is the word §4.1 already needed for the three grades,
is ordinary English for *how firmly established you are somewhere*, and yields the same meaning to a
reader with no memory of this repo (`CLAUDE.md` §4's idempotent-and-idiomatic test). **Neither existing
meaning is overridden or renamed** — a rename at that volume costs more than it buys, and both are
correct in their own scope. Reported to `00` as a vocabulary finding rather than fixed here.

### 4.1 Three grades of footing, and none of them is stored

| grade | what it is | how it is represented | can it act? |
|---|---|---|---|
| **post** | the faction holds the governance post at the place's tier node | a `Post` whose `principal` is this faction (`01 §4`) | yes — `05`'s gate is satisfied at that tier |
| **charter** | a chartered privilege at a place the faction does not govern | a `charter` **edge**, faction → place (`01 §7.2`) | no; it draws yield and gates facilities |
| **presence** | institutional reach short of any right | a `presence.<institution>` gauge on the place (`07`, `01 §5.2`) | no; it is what `act.contest_influence` moves (`05`) |

**`holdings` is not a field.** It is *"the places whose governance post's principal is this faction"* —
a query, not a list, so it cannot drift from the posts that define it. The Church holding a cathedral
inside a Crown province is a `charter`, which is exactly canon's composite control
(`settlement_layer_v30.md:99`) and exactly what v1's flat `holdings[]` could not express.

*Emergent possibility lost if the three grades were collapsed to one:* a faction would be national or
nothing. A guild in one port, a church with cathedrals in three duchies, and a movement with no ground
at all would all be inexpressible — and those are three of the setting's live institutions.

### 4.2 The derivation, adopted from canon rather than reinvented (C-3)

`settlement_layer_v30.md:158-171` (CANONICAL) already owns this arithmetic. **Adopted whole**, cited
not restated, per `00 §5.3`'s *"adopt what is better even when it is not yours"*:

```
W_s  = base(Type) + Prosperity_s + FacilityTier_s                    settlement_layer :159-163
q_s  = 0.5·L_s + 0.5·PS_s                                            :165
T    = Σ_s  W_s · (q_s / 7)                                          :165
footing  = clamp( round( 7 · T / (T + K) ), 0, 7 ),   K = 6          :166  (K calibrated by canon's sim)
```

**The one thing this page adds is the summation domain**, and it adds it in a direction canon already
went:

```
footing(faction, node) : T sums over every place in NODE's subtree where the faction has a footing,
                          each weighted by its grade —  post: W_s ·  charter: γ_c · W_s
                          presence: γ_p(band) · W_s
```

- **Evaluating at different nodes is what makes it multi-scale.** The same function at a settlement
  node, a province node and the peninsula gives settlement-, province- and peninsula-level footing.
  One derivation, three tiers, no third quantity to keep consistent.
- **Extending `T` over non-governed places is canon's own move, not an invention.**
  `settlement_layer_v30.md:171` already sums `T` over **Presence localities** for a territoryless
  faction (the Restoration Movement). This generalises that case instead of special-casing it —
  and `00 §6` principle 2 forbids the special case.
- `γ_c` and `γ_p` are **shape proposals**, `0 < γ_p < γ_c < 1`, with the ordering doing the work: a
  right is worth less than governance and more than reach.
- **Bounded and saturating for free.** `T/(T+K)` gives diminishing returns and holds the result in
  `[0,7]` for any holding, which canon names as its own Lesson-5 bound (`:168`) — `∂footing/∂q`
  shrinks as `T` grows. This is a **measured** bound, not an argued one: canon records a Stage-4 sim
  over 30 seasons under mission shocks with no runaway (`:173`). That is the only measured loop bound
  cited anywhere in this document, and it is canon's, not this suite's.

**Q-4 is untouched.** This page calls the quantity `faction.footing` and takes **no position** on
whether it is what canon calls Mandate. What C-3 closes is narrower and worth being precise about:
v1 invented a *second arithmetic* beside a ratified one. The name question stays exactly as open as
`00 §5.1` leaves it.

⚠ **A canon tension found while reading, reported and not resolved.**
`settlement_layer_v30.md:1075` says a collapsed city-state faction has **"no Mandate"**, while `:165-169`
derives Mandate from settlements and a city-state holds settlements — so the derivation returns a small
positive value where `:1075` says there is none. Both are in the same CANONICAL document. This page's
derivation is **total** (it returns the small value; nothing divides by a stage), so nothing here
depends on the resolution, but an SE/FA-lane reader should know the two sections disagree.

### 4.3 Canon's emergence ladder is a set of BANDS, not a stored stage

`settlement_layer_v30.md:1027-1047` ships a five-stage ladder — Cell · Organization · Movement ·
Faction · Hegemon — with per-stage requirements stated in terms this derivation already reads
(settlements controlled, provinces, province seats). Under v2 those become **bands on
`footing(faction, peninsula)` plus footing counts**, derived at read.

**A stored stage counter would be an aggregate with a setter**, and AU-1 forbids it. It would also need
a writer at every conquest, every charter lapse and every governance revocation — four writers for a
number that is a function of state already on the board. The bands are `gauge_band`'s job
(`01 §5.1`), and the mapping from canon's stage requirements to band edges is a **shape proposal**:
canon's thresholds are ratified for canon's Renown-keyed ladder, not for this derivation.

### 4.4 What footing gates

| gate | reads | owner |
|---|---|---|
| **charter lapse** — a chartered privilege whose backing institution's footing falls below a band **lapses automatically at the next Accounting, with nothing revoking it** | `footing(patron, node)`, at the boundary | canon, `settlement_layer_v30.md:651-661` (RATIFIED ED-SE-0021) — expressed here as an `edge` form transition `granted → lapsed`, `reversible: false` |
| deliberative vote weight; diplomatic reach | `footing(faction, node)` | `12` |
| per-tier action | **a post at that tier**, not footing | `05` — stated so the two are not confused |

The first row is worth naming as a template. Canon's Za-guild charter is **collapse by gate in
miniature**: the privilege ends because a condition stopped holding, nobody rolled, nobody detected
anything, and the mechanism is a boundary read. §7 is the same shape applied to a whole institution.

### 4.5 The double-count hazard (Q-5) — declared, not resolved

`propagation_spec_v1` §3 D.6 flags it HIGH PRIORITY and forbids resolving it locally. **What this
document does instead:** every derivation here reads **settlement-owned gauges only** and writes
nothing back; `05`'s down-targeted deltas write those same gauges. So the magnitude crosses in exactly
one direction and this page never carries it in the other — `01 part 2 §9.2`'s "which of its two
channels carries the magnitude, and never both", stated as a property of this page rather than as a
convention someone must apply. **That keeps this suite internally disjoint. It is not a resolution of
the general question**, and a later design that routes a faction-scale magnitude back down onto the
same gauges reintroduces the hazard regardless of this paragraph.

---
