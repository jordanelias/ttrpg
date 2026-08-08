# Social contest — Keys, Knots, NPCs, and the combat model

## Status: PROPOSED (2026-08-08, ED-SC-0030)
## Lane: SC
## Supersedes: nothing. Extends `05` (track architecture) and `06` (adversarial audit) along four axes Jordan named.

**Method.** Six read-only Fable lenses across two waves — inventory/wire, breakage, design consequences; then Keys I/O,
Knots/churn, and the combat comparison — each `valoria-critic` (Read/Grep/Glob only, so independence is structural).
Opus authorship throughout, per CLAUDE.md §10. `file:line` marked ✓ was verified against the working tree by the
author or a lens; cross-lane items are marked **observation**, never ruling.

**The four axes, from Jordan:** Keys I/O with scatter-gather · Knots · world churn as anti-repetition · the contest
as a *multimodal combat with multiple tracks and balances*.

> **Coverage finding, stated first because it is against this unit's own work.** `00`–`06` graded the contest
> against classical rhetoric, against precedent videogames, and against its own doc/code split. **It never opened
> `systems/combat/combat_engine_v1/`** — the repo's own reference implementation of "multiple tracks and balances,"
> running on the *same* σ-kernel (`M_MAX = 1.5`, `M·tanh(net/M)` ✓). The tracks combat load-bears on and the social
> kernel lacks are exactly the ones missing from `05` §2. Separately, grep of the whole audit directory finds
> "knot" **three times**, all incidental, and no CIP addresses repetition or churn at all. Both gaps are this unit's,
> not the kernel's.

---

## §1. The contest as multimodal combat

### 1.1 Track comparison

Combat maintains eight tracks with distinct timescales, consumers and terminals ✓. Mapped:

| Combat | Social counterpart | Status |
|---|---|---|
| **Wounds / Health** — cliff at depletion → *felled* | **Standing / Face** | **Process multiplier only.** No damage channel: Standing is monotonic-up except the CR5 self-backfire (`resolver.py:404-419` ✓). Nothing an opponent does strips it |
| **Stamina** — cliff at ≤ −4 → separation | **Reserve** | **Exists, with a terminal this unit under-credited**: an unaffordable move forces a yield, two yields clinch as *silence* (`resolver.py:326-329`, `primitives.py:278` ✓). Reserve exhaustion **is** the social stamina collapse, already wired. Its pricing is broken (`support` costs 2, regains 4, *and* builds ethos ✓) |
| **Concentration** | folded into Reserve by CR3 | deliberate; fine |
| **Initiative (Vor/Nach)** — signed ±1.5, decays, *stolen* by out-reading a deep commit | — | **NULL.** Strict A/B alternation over a fixed budget (`resolver.py:423-425` ✓) |
| **Poise** — floored at 0.40, disrupted by overcommit/bind | **Readiness** | Partial and structurally different: readiness is slowly *built* support, and nothing lets an opponent disrupt it. There is no stagger |
| **Measure / geometry** | **live stasis ground + dossier stranding** | **Exists and is genuinely good** — the one positional game the kernel has. Upward-only, and a failed shift self-contradiction-clinches ✓ |
| **Tempo** — `ready` accumulator, commit slows your next action | — | **NULL.** One move per side per beat, always |
| **Commitment / legibility / read** — continuous depth ∈[2,5], legibility derived from the move, read as a logistic contest | — | **NULL between orators.** All concealment in the contest is engine-vs-player; the opponent reads nothing and can be read by nothing |
| cross-fight persistence with *differential* recovery | — | NULL — this is CIP-1's record spine. Combat models it *inside* one fight; the social analogue is the chain contest and the ledger |

### 1.2 Where the analogy breaks, and what that settles

Combat is **two-party physics**; the contest is **three-party** — the outcome is rendered by a mind. Combat has
**no points decision**: nobody wins on a tally. So the five-band ladder has no combat counterpart, and the honest
composition is:

> **Bands are the judgment. Cliffs are the collapses that pre-empt judgment.**

The kernel already has this in embryo — the clinch check pre-empts, the win condition judges (`resolver.py:438-447` ✓)
— and `05` §4.3 correctly named it the kernel's best property. **Do not import felled-only termination; do not
delete the bands.** One defect: a clinch returns a winner and a reason **with no band**, so it is heterogeneous with
the ladder. Fix: clinch-family exits map to the **total** band for the felled side unless the venue row overrides.

### 1.3 The four win paths

| Path | Terminal today | What creates it |
|---|---|---|
| **On the merits** | EXISTS — the five bands | — |
| **Procedural fault** | EXISTS — the one non-`adv` terminal ✓ | needs a band mapping (above) |
| **Face collapse — "can't be taken seriously"** | **MISSING** | §1.4 |
| **The room turns** | **MISSING** | a Room strip channel + a venue-configured collapse entry. Grounding is **not** personal combat (no crowd) but **mass battle's rout at morale ≤ 0 with contagion** ✓ — *MB lane, observation*. Default **off**: a court does not end because the gallery jeers; a mob assembly might |

**Stall/silence** already exists per-move; CIP-3's burden supplies the at-close half — and gets new grounding here:
**burden is combat's measure asymmetry.** The shorter weapon carries the obligation to close, and an unresolved
outcome is legitimate only for the side that did not need to act.

### 1.4 The Standing dead zone — a new finding, and it answers the cliff question

`Standing.frac()` is `(v − START)/(HI − START)` clamped to [0,1] with `START = 5` (`primitives.py:47` ✓), and **both**
consumers — `Readiness.of` and `Resonance.leak` (`:243-260` ✓) — read `frac`.

> **Standing 0 and Standing 5 are indistinguishable in reception.** The whole lower half of the scale is dead state.

So the ~45%-of-fully-supported floor is reached at Standing **5**, not 0, and losing face below neutral currently
cannot touch persuasion at all. That reframes the cliff-versus-floor question I posed earlier:

**Combat's answer is both, on different tracks** — floors on *process* (poise 0.40, its 0.72× effect floor, the 5%
upset floor), cliffs on *integrity* (health → felled; stamina → collapse; and at army scale morale → rout with **no**
floor). So the fix is not converting the floor into a cliff. It is **adding an integrity cliff on a different track
than the floor governs** — and the dead zone is exactly where it goes.

**Ruling:** add `discredit_bar` to the venue's `DefeatCatalogue` — fatal iff the venue says so, firing at
`Standing ≤ bar`, bar inside the dead zone (`[SEED]` ≈ 2). It mirrors *felled* (an integrity meter crossing a
threshold), gives the 0–5 region its first consequence, and needs **no re-tuning of the floor above it.** The
alternative — re-founding `frac` on the full 0–10 range — changes every reception in every existing bout and should
be rejected as the higher-blast-radius option.

**Coupling, stated so it is not shipped broken:** the cliff is *unreachable* until a face-attack channel exists —
nothing but a self-inflicted foul strips Standing today. It ships **with** the attack channel, not before. Same rule
that `06` established for `split_standing`/`hard`.

### 1.5 Being "suckered in" — combat has the mechanism, and half of it already runs here

Combat models every element of Jordan's sentence: commitment is a **continuous chosen depth**, not a verb rung;
**the feint is not a verb** — WS-5 dissolved it into the attack, so deception is *how* you attack (shallow commit,
illegible mode) read through a legibility-scaled contest; the punish is the **Indes steal**, where a defender who
out-reads a deep commit takes the initiative and counters — and a botched counter cedes it back. Being drawn in is
**symmetrically dangerous**.

So the bait class is **not a new `bait` verb** — that repeats the double-machinery mistake WS-5 retired. It is three
ported properties on moves that already exist:

1. **Commitment depth on `advance`**, replacing the dead `advance`/`hard` rung pair: gain scales with commit, and
   commit carries **overcommit exposure** — a fault or Face strip when the move is read, or when its scheme's
   critical question lands.
2. **Legibility derived from the move's own properties** — a syllogism reads easy, an insinuation hard; deeper
   commit reads easier — feeding an orator-vs-orator read contest. This is the concealment *between players* the
   kernel entirely lacks.
3. **The punish routed through what exists** — a failed baited reply lands a fault or a Face strip; and under CIP-2's
   schemes, a rebuttal that fails a critical question leaves the attacked claim **strengthened**.

**And the sucker game already runs in one place.** `res = (1 − leak)·venue_w + leak·judge_character` ✓ — build ethos,
raise leak, and the judge drifts off the venue's standard toward a personal vector your opponent has not read.
Jordan's *"even if their opponent sticks tightly to the best practice… they can still be suckered"* **is literally
that term.** It is implemented; what is missing is a judge vector with any skew to drift *toward* (§3).

**Filed, not assumed:** whether to build the *Vor* itself — an initiative scalar that decays per exchange and is
stolen on a landed read — is the one combat track with no social carrier and no CIP. Burden plus the claim graph may
supply enough asymmetry without it. **Fork.**

### 1.6 The balances, and the rule that keeps them non-fungible

Combat's discipline, stated exactly: **tracks enter resolution as multipliers on *process*, never as addends on the
*score*.** No rule converts poise into wounds at any rate; each track has its own timescale and its own consumer;
every gain is priced in a *different* track — damage costs stamina, tempo and exposure; reach costs close control;
power costs legibility.

Seven social balances on that model — and four already exist:

| | Balance | Status |
|---|---|---|
| B1 | **Commitment** — exposure buys magnitude | build (§1.5) |
| B2 | **Effort** — Reserve buys moves; cliff = silence | exists ✓; repricing is a fork |
| B3 | **Investment** — an ethos or pathos move builds position *instead of* maximal present gain ✓ | **exists and survived audit — keep** |
| B4 | **Conformance vs capture** — ethos raises leak, replacing the venue's standard with the judge's ✓ | exists; §1.5's concealed-read game |
| B5 | **Ground-holding vs reframing** — `shift` costs 4 + contradiction risk, strands the opponent's dossier ✓ | exists — the measure game |
| B6 | **Public exposure** — the gallery raises leak *for both sides* ✓ | exists but static; CIP-14 is the dynamic half |
| B7 | **Win the case vs win the room** | CIP-12/14, conditional on CIP-9b |

> **The guard, and it is combat's rule made testable:** *Standing, Room, Reserve, faults and claim state may enter
> resolution only as multipliers or gates on process, or as their own terminals. No site converts any of them into
> `adv`, or `adv` into them, at a fixed rate.*

The kernel already obeys half of this. The failure is that the **close** reads one number — so the fix is **more
terminals and record kinds, not more addends.** That converges with CIP-2's restated condition and supplies the
registry-style guard CIP-12 named as unwritten. **It lands first**, because everything below widens its surface.

---

## §2. Keys as the I/O substrate

### 2.1 The two modes collapse to one discipline

A "parallel track contained within an instance" and a scatter-gathered proceeding have **identical emission
behaviour at the contest boundary** — writ in, close out, both root emissions, **zero interior Keys.** They differ
only in whether subscribers exist downstream. **The contest never needs to know which mode it is in.**

### 2.2 The I/O

**IN — `scene.contest_convened` is the one genuinely new Key type the whole architecture needs.** Nothing in the
55-type roster represents "a proceeding is convened with these stakes"; today the writ travels as a bare `ctx` dict
that is neither logged, citable, nor replayable. Payload: proceeding · question (start ground + rung vocabulary) ·
stakes (the **draft record**) · sides; optional burden, budget, declared ends, presence, evidence provenance refs.
`targets[]` carries **who it is at stake for, with roles** — subject (each side), object (the adjudicator or each
member), **beneficiary** (the bound principal, which is what CIP-7a's mandate check reads), witness (the gallery).

Its `causes[]` cites the topic-raising Key — which makes Jordan's rule machine-checkable: **a writ with an empty
`causes[]` is an authored scenario seed and nothing else.**

**IN — already declared, never wired:** `state.opinion_revised` lists `social_contest` among its consuming systems ✓
and carries exactly the W7 priors data. `scene.insult` / `scene.threat` / `scene.gift` carry `severity`,
`witnessed_by`, `demand` — the emotion-precondition inputs. The registry already names `social_contest` on both
sides of these. **Compose; extend nothing.**

**OUT — `scene.contest_resolved` exists with a live emit site**, needing optional-field extension: `proceeding`,
`verdict_reason` (the clinch terminal is **currently lost at the boundary** — a Grudge priced off a silence-clinch
should differ from one priced off a merits rout), `final_ground`, `margin` (CIP-1's loser-record-by-margin has no
carrier without it), `records`. The `outcome` enum needs `clinch` and `remitted` — **the one change that brushes
Class-A supersession; hold it up loudly rather than bundling it.**

### 2.3 Emit versus contain — the criterion, applied

**Emit iff** (a) a consumer outside this Bout must react by subscription, **or** (b) a later Key must cite it in
`causes[]`, **or** (c) replay cannot reconstruct downstream state without it.

**Corollary that does the work:** because the bout is deterministic given the writ plus the campaign-derived seed ✓,
(c) never forces interior emission — the interior is reconstructible by re-running it. **Only boundary Keys are
load-bearing.**

**Contain:** `adv`, the live ground, the claim graph, Standing/Reserve/Room, running faults, the appraise read, and
**per-exchange speech.** **Emit:** the writ at open; the clinch terminal *as a payload field*; the room's impressions
**on the close Key's witness targets**, never as per-member Keys.

That last ruling is arithmetic, not taste: per-member impression Keys for a 15-member crowd × 2 speakers × 5
proceedings per season is **150 emissions per tick**, against a cap of 64. Riding `targets[]` costs nothing —
**fan-out width never increments cascade depth** ✓.

### 2.4 OF-CAP is now rulable

The contest consumes **zero depth** — writ and close are both root emissions. Depth is spent by the reaction layer,
and the deepest chain using only registered types is `contest_resolved → opinion_revised → gossip → belief_revised`
= **3**.

> **Recommend: `cascade_depth_max = 3`** (4 for one unforeseen hop). **`emissions_per_tick_max = 64`** — worst case
> under this decomposition is ≈45–50. The named sensitivity: if per-member emission is ever ruled back in, 64 breaks
> immediately, **and the design should lose, not the cap.**

**A live latent break, and its fix must ship with the first subscriber:** `drain_tick` and `schedule_emission` have
**zero production callers** ✓; `mc_v18` goes straight from `accounting_boundary()` to `next_tick()`. The first
subscriber that schedules leaves the queue undrained and `next_tick` raises.

**Substrate constraints that bound the design:** `impact_vector` and `symbolic_dimensions` accept **only** the four
canonical Conviction axes ✓, so the armature axes and the three appeals cannot ride Keys without an authored
mapping — they stay in payload. And `public=true` **forbids** observer lists ✓, so a public venue's named gallery
rides `payload.presence`, not `visibility`.

**Independent confirmation:** the slate-freeze rule means a remit re-convenes next tick at fresh depth zero — the
substrate **forces** the terminate-and-reinstantiate horn canon had already chosen for *translatio*.

---

## §3. NPCs as adjudicators and audiences

**Already ratified and wired, which I initially missed:** the adjudicator carries `armature_position`, a **4-axis
Conviction vector** ✓ (Gate C, 2026-07-02), and `STYLE_AXIS` maps it onto the canonical Resonant Styles —
Precedent→Evidence, Vision→Consequence, Suppression→Authority ✓. **Three of four styles are already the contest's
judge axes.** Nothing populates the vector from an NPC sheet; the socket exists and is empty.

**The blend already delivers Jordan's intent, with numbers:** judge-character authority over venue fit is **40% at
default discipline, to a 90% cap** ✓, and the lever is player-operated. The gap is that the default vector is
`0.34/0.33/0.33` — near-uniform — so **judge identity is inert until someone authors skew.** The NPC mapping *is*
that missing data.

**The correct shape is a derivation adapter, not a replacement.** Every resolver read-site consumes exactly
`learned / hostile / discipline / character()`, so an NPC judge must project into those anyway — and `faction.py:39`
already derives an Adjudicator from faction stats ✓, the pattern built and tested. A replacement would also carry
both models permanently, since one crowd venue is a 15-member Panel against a usable roster of ~10.

**Three build rules:** never branch on `is_named` (scripting drift) — one object, richly-populated instances;
aggregate benches by **ballot, not by averaging** (the armature has the identical flaw — a Panel's position is the
*mean* ✓); and let the sheet set only the **dominant axis**, deriving exact weights from mutable state so the
"never the exact vector" reveal boundary stays hidden **and moves.**

**The first cost is data, not code.** There is no machine-readable NPC record, and the prose cannot be transcribed
as-is: §2 and §7.10 disagree on Thread Sensitivity or Truth for **at least six named NPCs** ✓, and §7.10 mis-cites
an ED. Every NPC needs a per-field ruling first. *(Cross-lane: npcs — observation.)*

**The id space is the architectural cost.** Five disjoint spaces with no mapping table ✓, and `ArmatureConfig`
keys positions by **`id(adjudicator)` — ephemeral Python object identity**, which cannot survive a save and is
defeated even in-session because fresh Adjudicators are constructed per call. Fix: key by `actor_id`, the namespace
`targets[].actor_id` already uses — which also lets the writ deliver positions.

---

## §4. Knots

**IN — all prose-live, engine-dead.** Solidarity requires an active Knot ✓ (+1D, no strain on a win, target's next
belief-revision at Ob −1); Knot-sharing corroboration rolls at Ob 1 and is **explicitly strain-free — a ruled
negative, do not add strain there** ✓; the Grand Contest wager is Knot-gated; `knot_partners_present` is a Key
payload field with **zero producers** ✓.

**OUT — and it is unfireable in principle, not merely unwired.** Canon is complete: a Knotted PC extracts private
counsel freely, re-query costs +1 strain, and **public citation of extracted counsel is immediate rupture**, −3
Disposition ✓. `check_knot_rupture` implements it and has **zero callers outside its own module and one test** ✓.

The blocker is that `EvidenceItem` carries only `ground / weight / appeal` ✓ — no provenance — so the kernel
**cannot distinguish extracted counsel from any other evidence.**

> **This gives W3's provenance gap a second, independent consumer the proposal missed.** Provenance is not only what
> makes an attack bite; it is the *sole* input that can ever fire the betrayal rupture. Add `provenance` to
> `EvidenceItem` with at least `knot_counsel(knot_id)`; the emission point is `Dossier.present()` under a
> public-venue flag.

And it instantiates the anti-collapse condition as a single concrete rule: **winning by citing your friend's private
counsel gains on the merits track and ruptures the relational one, with no exchange rate between them.**

**Contest-legitimate strain sources**, all citing existing canon rather than inventing: counsel re-query +1 ·
composure-buffer use +1 · witnessing a scar fire in the partner +1 at accounting · sustained Disposition below +3,
+1 per accounting. Corroboration is **+0, ruled.** A PC-vs-partner contest as an opposing operation is
`[SEED — by analogy to threadwork; needs ratification, do not ship as cited]`.

**PP-724 is designed, PROVISIONAL, zero code** ✓ — six NPC-NPC edge types with strain mirroring the Knot lifecycle,
and §3.3 already rules that Knot strain and edge strain **do not aggregate.** It is **not** a prerequisite for panel
churn: bench churn splits into membership/member-state (needs no PP-724 — and the drift source **already runs every
season** ✓, unread by anything contest-side) and inter-member interaction (what PP-724 buys). **Minimum subset:
Rivalry + Patronage.** Rivalry already specifies auto-formation on *"mutual antagonism in a single Social Contest,
auto-detected at contest resolution"* and escalation on *"social contest defeat"* — **that is the churn loop, already
written down, in one edge type.** *(npcs/FA lanes — observation.)*

**A gate-level bug that would break PP-724 too.** `conviction.py`'s `CONVICTIONS` tuple is **neither the canonical 13
nor the legacy set** — it mixes retired labels under a comment claiming it *is* the canonical 13 ✓. The only live
caller passes `'Loyalty'`, in no set, so it silently no-ops while the caller reports `conviction_scar=1` ✓. PP-724's
break rules scar **Honor** and **Authority** — both canonical, both missing from that gate — so a faithful
implementation would no-op through the same hole. **Fix the gate, not the call site.** *(characters — observation.)*

---

## §5. World churn, and the repeat detector

**Verdict: the churn is insufficient, and it fails in exactly the shape Jordan's ruling prohibits.** Between two
firings of the same emergency council, the only non-noise deltas are `L` — which the contest itself perturbs — and
contingently `Sta`, which only other factions can move, and three of whose four writers push it **down**. Proceeding,
policies, bench, evidence and question are all **pinned** ✓. A faction at `Sta ≤ 2` without Church absolution replays
the same contest before the same synthetic bench every season to campaign end.

**And the topic generator is half a precedent.** I cited `_derive_vote` as the working pattern for the writ. It
derives *who raises* a topic from world pressure but derives **no *what*** — the Motion's only content is
`motion_id=f"parl_s{season}"` plus a fixed genre pair ✓, so it emits the identical contentless motion every season.
The real requirement: **a topic is an object with identity, a raising condition, and a retirement rule**, consumed on
resolution so that re-arguing requires the world to re-raise it. The `(L, 7−Sta)` formula's defect is that it is a
**reading with no writeback.**

**Minimum set for churn to bite:** records mounted on `Faction`, emitted at close and consumed at open (CIP-1);
benches constituted from named NPCs with per-member exposure (CIP-11's stated blocker), so the already-live NPC drift
reaches the bench; and topic retirement. Preferred interim: **a council-held `Precedent` tag with a TTL guarding
re-queue** — composable on `LedgerTag` the moment factions have a ledger, and the first genuine
record-guards-a-transition instance the corpus has been asking for.

**The falsifier, shippable now.** Two contests are an effective repeat iff this tuple is identical: *(scene type,
stakes kind, faction ids, proceeding, start ground, win condition/burden, faculties, policy pair, **sorted bench with
per-member values**, **sorted dossier multiset**, track start, echo target)* — RNG excluded, because variation is
noise, not churn. The bench and dossier terms are load-bearing: a detector over parties and topic alone would pass
while the bench stayed frozen, which is the wrong instrument for Jordan's ruling. Instrument: ~20 lines at build
time, SHA-256 over canonical JSON — **the same convention `KeyLog.serialize()` uses** — accumulated per campaign,
asserting `max(count) ≤ K`.

**As wired today this test fails immediately. That is the point.** Ship it xfail; flip it blocking when the minimum
set lands. `KeyLog.content_hash()` cannot serve: it hashes the whole cumulative log, so it detects run-level
determinism, never intra-run repetition ✓.

---

## §6. Corrections to filed work

| Claim | Correction |
|---|---|
| "Every authored thing about the judge is discarded at the boundary" (mine, in session) | **False.** `armature_position` is a ratified 4-axis Conviction vector mapped onto the canonical Resonant Styles ✓. The socket exists; nothing fills it |
| "Suckered in has no carrier at all" (mine) | **Partly false.** Shifting the ground strands the opponent's prepared dossier and off-ground argument takes an evasion fault ✓. And the leak channel is literally the mechanism (§1.5) |
| "The ethical-mode table is faction-keyed while npc_behavior is person-keyed" (mine) | **False.** Both are faction-keyed; the NPC doc applies faction frameworks per person ✓. The real defect is two drifted label dialects. Owner is faction-level — **FA lane, observation** |
| "W6's reach has no carrier" (mine) | **False.** `Key.time_horizon` and `Key.permanence` are that axis, on the emission |
| "The presence bound needs building" (mine) | **False.** `Visibility.semi_public_observers` is that rule — with the caveat that `public=true` forbids observer lists, so public venues use `payload.presence` |
| "§1.1 Stance Triangle is an empty stub" (mine) | **Over-stated.** The *head* is a skeleton; the co-filed infill carries the definitions ✓ |
| CIP-1: the live Key "already assembles payload **and a populated `causes[]`**" | **Half right.** `scene.contest_resolved` has an **empty** `causes[]`; the populated one belongs to its dormant sibling ✓. Provenance is kept on the dormant leg and discarded on the live one |
| C-8: `_derive_vote` is "the working precedent for CIP-5" | **Soften.** Half a precedent — it derives *who*, not *what* (§5) |
| CIP-13: retire `hard`, rehome amplification to CIP-5's stakes dials | **Partial disagreement.** The `hard` kill stands ✓, but amplification-as-*stakes* and amplification-as-*commit* are different quantities. I rehomed the first and silently discarded the second; §1.5 restores it as per-move commit |
| `00` §4.3's cut list | Deletes the doc's **only** initiative mechanism (rolled first-to-speak) with no remark and no replacement |
| `00` §4.2 "the KeyLog is written and read by tests only" | Stale on the write half — the parliamentary bridge writes a Key most seasons under the default-ON flag ✓. The **read** half stands: zero campaign-side readers |

---

## §7. What must be built, in order

1. **The non-fungibility guard** (§1.6) — a registry-style sweep asserting no site converts a track into `adv` or
   back at a fixed rate. Lands **first**: everything else widens its surface.
2. **The writ Key** (`scene.contest_convened`) + `build_contest(..., armature=, adjudicator_id=)`, keyword-optional,
   three caller files ✓ — and it is the **same seam** as the already-tracked armature-unreachability bug.
3. **Topic retirement** — the ledger tag that guards re-queue; plus the repeat detector shipped xfail.
4. **The NPC derivation adapter** — after the per-NPC data rulings.
5. **Provenance on `EvidenceItem`** — one field, two consumers (attack bite; betrayal rupture).
6. **Bench constitution from NPCs, balloted not averaged**; then Rivalry + Patronage edges.
7. **The face-attack channel with `discredit_bar`**, shipped as one unit with CIP-2's schemes.
8. **`drain_tick` wiring** — with the first subscriber, never after.

---

## §8. Forks

**OF-CAP** — `cascade_depth_max = 3`(–4), `emissions_per_tick_max = 64` (§2.4). · **No NPC lane exists** in the
`ED-<LANE>` roster, and `systems/npcs/` is doc-only; an executable NPC mind needs a lane ruling under §2a first. ·
**The id space** — which of five becomes canonical. · **PP-724 ratification** and its edge subset. ·
**The `outcome` enum extension** (clinch, remitted) — the one Class-A-adjacent item. · **The *Vor*** — build an
initiative scalar, or rule that burden plus the claim graph carry enough asymmetry. · **`discredit_bar`'s value**
and whether the venue default is on. · **Room collapse** as a terminal, default off. · **Reserve repricing.** ·
Carried forward: **CIP-9b**, on which CIP-14 depends.

---

## §9. Falsifiers and confidence

- **The repeat detector** (§5) is itself the falsifier for every churn claim here, and it currently **fails**.
- **§1.4's dead zone** is falsified by any consumer reading raw `Standing.v` below 5 in reception. Two exist —
  the `hard`-licensing margin and the CR5 bound — and neither is a reception path; a third would kill the finding.
- **§1.6's guard** is falsified the moment a legitimate design needs a fixed-rate conversion. That is the point: it
  should be argued, not added silently.
- **§2.3's contain rulings** rest on the bout being reconstructible from writ + seed. If the RNG model changes, re-derive.
- **§2.4's numbers** are falsified by any decomposition emitting per-member Keys — 150/tick against 64.

**Confidence.** HIGH: every `file:line` marked ✓ (six lenses; two independent zero-misquote results on the earlier
documents); the combat track comparison; the dead-zone finding; the churn verdict; the emit/contain criterion.
MEDIUM: the OF-CAP arithmetic (load estimates from current campaign shape); PP-724's minimum edge subset; the
adapter's field list. LOW: classical locators carried from `05`; any effort estimate.

**Nothing here is executable as routine work.** Every §7 item beyond the guard touches a ratified decision, a lane
that does not exist, or another lane's primitive.
