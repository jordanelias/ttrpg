# 02 — The Person

## Status: PROPOSED (2026-08-29) — a from-scratch design. Nothing here ratifies on merge.
## Lane: PC (person-scale) · Composes on: `01_substrate.md` (binding) · Defers to: doc 10 (resolver), doc 07 (argument), doc 04 (Thread)
## Method: derived from the substrate's six fields. No prior module, ruling or code constrains it.

The substrate says there is one actor and it carries six fields. This document turns each of those
six into a mechanism with a producer, a carrier and a consumer, and binds every one of them to
something the setting actually contains. Memory is not re-derived — substrate §3 owns the claim
ledger and this document only names the places that read and write it.

The organising commitment: **nothing here is a modifier.** A mark is not a difficulty slider, a
Conviction is not a bonus, a Knot is not a friendship meter. Each is a structure that changes *what
options exist and who reads what*, because a modifier is the one shape that cannot produce a
politics.

---

## 1. Marks

### 1.1 The object

A mark is `(kind, value, legibility, presented, provenance)`. Kinds, and the setting content each
one holds:

| kind | values | held by |
|---|---|---|
| `heritage` | Northern Einhir · Central Einhir · Southern Einhir · Crown-Latinate · Altonian · Schoenlander | everyone |
| `house` | a hearth pointer + `main`/`cadet` | Almqvist, Baralta, Vaynard, Uln, Strand, … |
| `grade` | apprentice · journeyman · Free Master · burgher | guild members |
| `church` | unbaptised · communicant · confirmed · minor orders · Canon · Cardinal | most |
| `office` | praefect · gate warden · magistrate · Grandmaster · Confessor · Doux | few, revocable |
| `sensitivity` | `sign` ∈ {none, latent, evident, marked} — a *sign*, never the TS number | everyone |

**There is no caste field.** This is the single most important sentence in the document and §1.3
explains it.

`provenance` is the event that conferred the mark: an admission act, a baptism, a succession
pointer resolving, a grant of office. A mark with no provenance cannot exist; this is the
precedent's "every durable tag needs provenance bound to the causing event," and it is what makes a
mark *forgeable* in a way that leaves a seam — a forged Free Master token asserts a provenance that
can be checked against the guild roll (T9).

- **Loop:** produced by admission, birth, succession, ordination, grant · carried on the person ·
  consumed by every reading (§1.2) and every gate (§1.3).
- **Cut it and you lose:** the fact that the same act by two persons produces different results.
  Without marks, caste is a number someone typed in.

### 1.2 A mark is READ, not possessed

Reading is a perception, so it routes through `witness` and deposits a claim. `read(reader,
subject, kind) → claim`.

```
legibility(kind, context) ∈ {open, attested, latent}
  open      read on any co-presence            base confidence 0.9   heritage (dress, accent, name), sensitivity=evident
  attested  needs a token, roll, or testimony   base confidence 0.7   grade, office, church, house
  latent    needs a probe act                   base confidence 0.5   sensitivity=latent, cadet-line status, passing
```

**Passing.** A person may set `presented ≠ value` on any mark. That is not a flag; it is a standing
act with a practice (`Passing`, §2) and an exposure cost paid only on investigation. The read
becomes a contest:

```
conceal = actor.practice[Passing] + actor.attr[Will]
pierce  = reader.attr[Acuity] + attention(reader, kind) + Σ prior claims the reader holds
                                                            that bear on this kind, × confidence

attention(reader, kind) = |reader.stance[the proposition that kind indexes].valence|
```

That last line is the design. **A reader's bigotry is exactly their attention.** A Free Master who
holds `prop: Southern Einhir should not hold Free Master` at +4 pierces at +4; a Löwenritter who
holds it at 0 genuinely does not notice. Nobody wrote "bigots detect Southern Einhir"; it is one
absolute-value.

**Exposure is never automatic.** A passing person accrues no hidden counter on a clock. Exposure
rises only when a specific named person spends an investigation act against them, and it is
discovered in proportion to *that person's actual spend* — precedent's concealment steal, taken
whole. There is no timer that eventually catches you.

- **Loop:** produced by co-presence, probe acts and investigation spend · carried as claims in the
  *reader's* ledger · consumed by gates, judging sets and tellings.
- **Cut it and you lose:** Maret Uln and Gerik Strand. A mark that cannot be mistaken, concealed or
  forged makes caste transgression unplayable, and the setting's two named case studies become
  colour text.

### 1.3 Caste is not a rule. It is a distribution of stance across the persons who hold gates.

The setting is explicit: the caste order is informal, uncodified, and enforced as **per-institution
rank-gating.** So the engine must never contain a line that reads a person's heritage and subtracts
anything. It does not.

Every admission act and every office grant is `contest(container, prize, claimants)` from substrate
§4.1, judged by the persons who hold standing in that container. Each judge's vote is their stance
applied to the candidate's **read** marks. A **standard** is a proposition the judges argue over;
it is not a filter the engine applies.

That reproduces the setting's institution-by-institution table with no institution named in code:

| institution | why it gates the way it does |
|---|---|
| **Crown**, Standing 3+ | the persons who confer Crown standing are cadet/deed families whose own standing came from Secession War service; their `prop: the post-war settlement is owed to those who won it` sits at high weight, and Southern Einhir were excluded from that coalition. Public deeds and sponsorship are what move it — which is why they are the documented route. |
| **Church** | the Dicasteries' confirming persons hold `prop:Faith` at weight 5 and read `heritage=Southern Einhir` as evidence against `prop: Solmundan Orthodoxy across the peninsula`. A Southern Einhir Canon is "a scandal" because *scandal is the judging set's regard change on the persons who confirmed him* — a second-order stance move, not a rule. |
| **Guilds** | variable, because the six persons on a Masterpiece Examination committee are six independent stance rows. The bias is documented and real and it is also *different in Goldenfurt than in Oastad*, which is what a rule could never produce. |
| **Löwenritter, Niflhel** | caste-open. Löwenritter because its admission-holders hold `prop: loyal to the Crown as institution, not bloodline` at weight 5, which is orthogonal to heritage. Niflhel because its **needs** computation requires waterfront and covert reach that only Southern Einhir members supply — the recruiter's instrumental need outweighs a stance he may still privately hold. |

**Correlated standards — how harm gets done that nobody intends.** A standard is a predicate over
marks *and over practice provenance* (§2.2). The Masterpiece Examination's idiom clause requires a
piece in the Crown-Latinate ornamental idiom. That idiom is taught in sponsored shops. Sponsorship
runs through Free Masters. So the clause selects on heritage at a correlation of ~0.8 while naming
heritage nowhere, and **a committee of six judges each holding heritage-stance 0 produces the same
rejection rate as a committee of bigots.** This is the mechanism for Confessor Arne Himlensendt
generalised: pastoral compassion and ethnic suppression can be the same act because the act reads a
proxy.

The counter-play, and it is a first-class one: correlation is **measurable**. A field investigation
(T9) over the guild roll — grants against candidates' practice provenance over ten years — produces
a claim with a firsthand root, which can be carried as a petition (substrate §5.1) and attacked or
defended in argument (doc 07) at the guild's standing date. Duke Magnus Vaynard's anti-caste
programme is not a policy toggle; it is (a) replacing admission-holders, (b) moving their stances,
(c) founding institutions whose admission-holders lack the stance, and (d) publishing correlations.
All four are already-existing acts.

- **Cut it and you lose:** institutional harm without villains, regional variation in the same
  prejudice, and any way for reform to be a campaign rather than a setting change.

---

## 2. Capability

### 2.1 The nine, the tenth, and Thread Sensitivity

Nine attributes, 1–7, three triads: **Body** (Strength, Endurance, Agility), **Mind** (Focus,
Acuity, Will), **Social** (Attunement, Charisma, Bonds).

**Thread Sensitivity** is 0–100+ and is *not* an attribute. Thread Pool = `floor(TS/10)`. It is
separate because it is the only capability that is (a) heritage-correlated at the population level
— Southern Einhir baseline runs higher — and (b) a **class gate** rather than a magnitude: below TS
30 certain verbs do not exist for you at any rank. That is P-08's inaccessibility, and it is the
one place this design gates a capability on something a person cannot acquire.

**The tenth.** Index 9 exists in the schema, has no name, is never summed into any pool, and is
read by nothing. Under E-as-a-ratio I will not invent content for it: **I cannot write an N-line
for a tenth attribute, so it is carried as a reservation, not a mechanism.** What it costs to leave
it reserved is one integer per person. What would earn it is a demonstrated dynamic that the nine
plus TS plus stance cannot express. Naming it now would be the exact failure this exercise exists
to escape.

### 2.2 Practices

A practice is `(name, rank 0–5, provenance, idiom)`. Rank is the magnitude. **Provenance** is where
it was learned — a hearth shop, a sponsored shop, a Löwenritter chapter, a Niflhel handler, a
parish school. **Idiom** is the tradition it was learned in. Both are readable marks-adjacent facts,
and both are what correlated standards key on (§1.3). Provenance is why capability and marks are
not independent systems: a practice carries its social origin on its face.

Provenance is also the honest expression of P-13. Southernmost knowledge is mechanically
untransmittable to non-sensitives: a practice whose provenance is a Locked Zone lineage has a
`requires: TS ≥ 30` flag, and teaching it to a person below that produces rank 0 permanently, not
slow progress. Study alone does not cross the barrier.

**Gate on role, never on biography.** A practice is never a unique key. `rarity(practice, rank,
node)` is *derived* by rolling up the containment tree exactly as substrate §1.3 derives presence —
how many persons inside this node hold it at ≥ rank.

⚠ **`rarity` therefore rolls up TRUE practice holdings, and it takes the same two-profile split
adjudication A-2 imposed on the faction profile — it did not get one, and the omission was a leak.**
`rarity_true(practice, rank, node)` exists for bookkeeping, for tests, and **for the resolver**, which
is the world and is allowed to see everything. It is readable by **no agent**. Any person reasoning
about how rare a skill is — a guild deciding whether it can afford to expel a chaser, a duke deciding
whether he can replace an engineer, a recruiter deciding where to look — reads
`rarity_est(practice, rank, node, observer)`, built from that observer's own claims about who holds
what. The failure without the split is exactly A-2's: a covertly-held practice (a Niflhel man's
poisoning, a Southern Einhir woman's letters kept quiet in a house that would punish them) counts
toward everyone's estimate the moment it exists, so **underestimating a rival's depth becomes
impossible** and the guild that thinks it is irreplaceable can never be wrong about it. With the split,
being wrong about your own scarcity is the default, which is what makes the census a thing worth
running and worth falsifying. Nothing in the game ever asks "does the person
who did X exist"; it asks "does this container hold someone at rank ≥ 3." Kill the Kettlemakers'
best chaser and the second-best is promoted and the guild is worse, measurably, for a generation.
Kill the only person with a scripted history and the guild is broken forever. The first is a
politics; the second is a save-file bug.

**Advancement is caused, never ticked.** A practice gains a rank when an attempt at a standard
above its rank resolves *and* one of: it was witnessed by a person holding the practice higher (a
master saw it), or it failed at a cost the person actually paid. There is no experience clock. This
is the precedent's refusal of the scheduled recovery tick applied at person scale.

### 2.3 What capability contributes to an attempt

Doc 10 owns the resolver. Capability contributes exactly two things and they are different in kind.

**Magnitude — dice.**
```
contributed(actor, attempt) = attr[triad_axis(attempt.practice)]      1..7
                            + practice[attempt.practice].rank         0..5   (absent → 0, unpracticed)
                            + thread_pool                             only if attempt.verb is thread-typed
```
The resolver adds tool, situation, opposition and standard. Capability supplies the first block and
nothing else; it never supplies a modifier to someone else's roll.

**Reach — verbs.** At `rank ≥ 3` a practice adds *verbs to the actor's option list*, and at rank ≥
5 it adds verbs that cannot be attempted at all below that rank. This is the precedent's in-band
form of leadership taken down to person scale: **the capable person changes the option set and the
pool source, never adds a flat bonus.** A Free Master chaser at rank 5 doesn't roll better than a
journeyman at rank 4; he can attempt `commission on speculation`, which the journeyman cannot see
in his list.

That split is also the anti-leverage rule (precedent): a person's contribution to a container-scale
outcome is a *fraction of the container's own capacity*, because what they contribute is a verb the
container can now attempt, sized to the container.

- **Loop:** produced by generation (§8) and by caused advancement · carried on the person ·
  consumed by pool assembly, option listing, and correlated standards via provenance.
- **Cut it and you lose:** attempting anything, and the fact that skill has a social address.

---

## 3. Stance

### 3.1 One table

```
stance[referent] = (valence −5..+5, weight 0..5, provenance: claim_ids)
referent ∈ Person | Faction | Proposition | Place
```

Valence toward a person *is* the setting's Disposition. There is no second relationship number.

**Why fusing feelings-about-people with beliefs-about-value is correct, not lossy.** Fusion would
be lossy if it forced "I like Aldwin but I hate what he proposes" into one row. It does not — that
is two rows, `stance[Aldwin] = (+3, 2)` and `stance[prop: remit the Einhir fine] = (−4, 4)`, in one
table. What fusion buys is that **every consumer reads the same two numbers**: view salience reads
`weight`, judging sets read `valence`, petition backing reads `valence × weight`, faction commit
degree *is* `stance[faction].valence` normalised. Split them into two stores and every one of those
consumers needs a merge rule, and the merge rule is precisely where the second copy starts
disagreeing with the first. One table is not a simplification; it is the removal of a
disagreement surface.

- **Loop:** produced by `revise` (§3.3) · carried on the person · consumed by view salience,
  judging, backing, commitment, needs, and argument (doc 07).
- **Cut it and you lose:** every reason a person does anything that their larder does not force.

### 3.2 The two personality scalars, and exactly what reads them

`credulity ∈ 0..5` and `obstinacy ∈ 0..5`. The substrate cuts every other trait. Each is read by
**exactly one function**, and I state them so the claim is falsifiable:

```
hear(hearer, telling) → Δconfidence on the deposited claim
    Δconfidence = base × (0.4 + 0.12 × hearer.credulity)
                        × f(hearer.stance[speaker].valence)
    ── credulity is read HERE AND NOWHERE ELSE.

revise(person, referent, pressure) → Δstance
    resist   = 1 + person.obstinacy + stance[referent].weight
    ── obstinacy is read HERE AND NOWHERE ELSE.
```

If either scalar ever acquires a second reader, it has become a trait vector and should be cut.

### 3.3 How a stance changes

```
Δvalence = clamp( round(pressure / resist), −2, +2 )
weight  += +1  if the pressure was survived (|Δvalence| == 0)
           −1  if the pressure moved it
```

**Weight is hysteresis, and that is the whole mechanism.** Enduring a contradiction hardens you;
being moved loosens you for the next move. From one line you get both the zealot who cannot be
argued out of `prop:Faith` and the convert who cascades — the Restoration cell member who takes one
public refusal and then moves three more times in a season. Nothing else in the design produces
radicalisation, and nothing had to.

Pressure sources, and their magnitudes:

| source | pressure |
|---|---|
| witnessed event contradicting the stance | `severity × vantage_quality` |
| a telling | `|speaker_stance| × credulity_term` (via `hear`) |
| an unmet stance-commitment (a petition dropped, a promise broken) | `commit_degree × 3`, toward the container **and toward the named person who dropped it** |
| cost actually paid for the stance | `weight += 1` only — effort justification, no valence move |

That last row is why the fined smuggler and the rejected journeyman harden rather than recant.

### 3.4 Convictions are priors, not a second store

Thirteen canonical referents — Faith, Authority, Order, Scholastic, Utility, Equity, Liberty,
Precedent, Community, Identity, Warden, Virtue, Honor — each a **proposition row in the same
table**. They are not a separate field, so they cannot disagree with stance.

Every specific proposition in the game (a petition's ask, a dispensation's term, a faction's
proposition, an examination standard) carries a **conviction signature**: a sparse signed vector
over the thirteen, authored with the proposition. *"Remit the Einhir fine"* = `{Equity +2, Precedent
−1, Authority −1}`.

When a person meets a proposition they have no row for:
```
seed_valence = clamp( round( Σ_c sig[c] × stance[c].valence / Σ_c |sig[c]| ), −5, +5 )
seed_weight  = max_c ( |sig[c]| > 0 ? stance[c].weight : 0 ) − 1
```
The seed is written as a real row and thereafter drifts on its own. So Convictions are *the prior a
new proposition is judged by*, and after judgment the specific row can diverge from the Conviction
that seeded it — which is exactly a person betraying their own principle in one case, expressible
without a second system.

**Primary Convictions are derived, not stored**: the rows with `weight ≥ 4`, of which there will
usually be one to three. The setting's "distributed cultural weight" is the default row set a
person inherits from their address and marks at generation (§8) — Kettlemakers' Row seeds Order and
Precedent high; the Einhir hamlet seeds Identity and Community high; a Löwenritter chapter seeds
Authority and Honor and *suppresses* Faith relative to the parish around it.

- **Cut Convictions and you lose:** the ability of a person to have a position on something they
  have never encountered — which is what makes a new dispensation land differently on two
  neighbours on the day it is cried.

---

## 4. Ties and Knots

### 4.1 Ties are channels; stance is attitude. They are different and both are needed.

`tie(a, b) = (familiarity 0..5, last_contact, channel_class)`. A tie carries *tellings*: it sets
the probability and latency with which a claim in a's ledger reaches b.

You can hate your brother and still hear everything from him. If ties and stance were one number,
that sentence would be unsayable, and with it goes every hostile information channel — the informer,
the estranged cousin, the rival who tells you the truth to hurt you.

### 4.2 Knots — re-derivation

The setting hands down a shape. I take most of it, and show the work.

**Slots = floor(Bonds/2)+1. KEPT.** Cut the cap and depth stops being scarce, so "who do I spend my
depth on" stops being a choice. R-shape: more slots compounds (more channels → more news → more
openings) but Bonds competes with Attunement and Charisma in one triad, and each Knot carries strain
liability that also compounds. Non-dominant.

**TS ≥ 30 both sides. KEPT, and the consequence is named rather than mitigated.** This makes the
deepest informal channel in the game *unavailable to non-sensitives* — King Almud Almqvist at TS 0
can never hold a Knot — and, because Southern Einhir carry a higher TS baseline, it makes the
informal channel **caste-correlated in the opposite direction to every formal institution.** That
is not a bug to patch. It is the structural reason Niflhel's covert reach needs Southern Einhir
members, the reason the Restoration's "Community Weaving" functions without Mandate or Wealth, and
the reason a peninsula that gates Southern Einhir out of every roll still cannot see what they
know. Formal exclusion, informal advantage, on one threshold.

**Two tiers Distant/Close. ALTERED to one field.** `depth ∈ {1, 2}`; strain range `(−2·depth) ..
+5`; depth 2 adds Conviction Scar on rupture and enables Coherence contagion. Same content, one
field instead of two object types. Function preserved, so E improves.

**What a Knot adds over a maxed ordinary tie — the bandwidth claim, made mechanical.** Four things,
and only the first is the substrate's headline:

1. **Unbidden deposit.** A material state change in one partner — severe need, coherence drop ≥2,
   death, a stance revision of |Δ| = 2 on a primary Conviction — deposits a low-precision claim in
   the other's ledger **with no speaker, no latency and no intermediary distortion.** Source is
   `firsthand_via_knot`, which corroborates independently of any telling — **but does not mint a new
   root: it reuses the originating event's id** (doc 03 §5). Five partners feeling one rupture hold one
   root between them, not five, or a well-bonded person could manufacture corroboration out of a single
   crisis.
   ```
   bandwidth(k) = max(0, 2 − floor(strain / 3))     # unbidden deposits per season
   ```
   A strained Knot goes quiet *before* it breaks. The channel narrowing is the warning, and it is
   diegetic: your cousin stops appearing in your dreams a season before you lose her.
2. **Composure buffering** in a social contest — the partner absorbs, at +1 strain.
3. **Counsel extraction** — reading the partner's `stance` row on a proposition without consent. The
   only direct read of another person's interior anywhere in the design. +1 strain, and it is
   detectable by the partner on an Attunement check.
4. **Coherence contagion (P-12)** — depth 2 only, §5.3.

**Strain.** One shared bidirectional gauge, `−2·depth .. +5`. Accrues +1 per: remote Thread-Read
through the Knot · composure buffering · counsel extraction · a contested Thread op targeting the
partner · each season ending with `stance[partner].valence < 0`. Decays −1 per season **only if an
`invest` act was performed** — a scene spent, not a timer. This satisfies the refusal of scheduled
recovery.

**R-shape, run against the precedent's own test (maximum mitigation vs maximum accrual).** Gain per
use is flat and never decays. Cost is strain, which compounds toward a large durable rupture. Max
mitigation is −1/season and costs one act. So: **one use per season is sustainable indefinitely;
two per season is an overdraft recoverable only by a season of abstention; three is a rupture
inside two seasons.** The net is recoverable, so the mechanism is not engineered never to fire, and
it is not free either. The choice is legible, and the legibility is published as the bandwidth
number without publishing the trigger point — precedent's view-slice rule.

**Rupture** at strain +5, or on: public betrayal of counsel (a `tell` of a claim whose source is
`counsel(knot)`) · the partner's death · a Fell/Dissolution op targeting the partner · both
partners' primary Conviction rows crossing to opposite sign on a shared referent · deliberate
severance. Costs: `stance[partner].valence := −3` (a set, with provenance pointing at the rupture,
so it is citable in argument) · mutual Composure damage · Coherence −1 · depth 2 only, a
**Conviction Scar**: the Conviction the Knot was aligned with has its weight frozen and its valence
inverted by 1, permanently provenance-bound to the rupture event and therefore quotable against the
person by anyone who knows.

- **Loop:** produced by `form_knot` (Disposition +5, TS ≥ 30 both, Bonds ≥ 5, free slot) · carried
  as a bidirectional edge · consumed by unbidden deposit, social contests, counsel, coherence.
- **Cut Knots and you lose:** *(Corrected N-line — the original claimed too much, and the word doing
  the overclaiming was "only".)* It read *"the only channel by which a person holding no post receives
  news, opportunity and obligation faster and cleaner than the crier."* That is false as stated. An
  ordinary tie already carries tellings, with its own probability and latency (§4.1), and a published
  dispensation deposits into every person in its scope **by presence and channel, never by post**
  (substrate §7) — through the crier, the priest, the guild notice, the market. **The unposted are
  reached without any Knot**, which is the design's own point about how a decree lands on a hamlet.
  What the Knot uniquely owns is narrower and is the thing actually worth keeping: the **unbidden,
  speakerless, undistorted** deposit — a state that arrives with **no teller, no roll and no
  intermediary distortion**, which no other channel in this design produces, since every other arrival
  is somebody choosing to tell you and the telling can be withheld, delayed, or bent on the way. So
  cut Knots and S-DOWN still reaches the unposted; what it loses is the one arrival nobody sent,
  nobody can suppress, and nobody can distort — Gerik's distress in his sister's ledger the season it
  happens, which no crier was ever going to carry.

---

## 5. Coherence and the interior

### 5.1 Does it earn its place?

Yes, and the test is whether anything else charges for Thread use and betrayal. Nothing does.
Stance weight measures conviction; obstinacy measures resistance; neither measures the cost of
acting against yourself. Under P-01 (no isolated effects) a Thread op must move something on the
operator, and Coherence is that something.

Stored, 10→0, **orthogonal to TS** (a TS-90 Southern Einhir practitioner may sit at Coherence 3).

```
seasonal drift:
  −1  if the season contained a resolved attempt opposing a primary Conviction (weight ≥ 4)
      at valence-distance ≥ 3
  +1  if the season contained ≥2 attempts agreeing with a primary Conviction and none opposing
discrete writes: Knot rupture −1 · being memory-pulled −1 (P-09; leaves a perceptible
  orphaned-configuration claim, never a clean erase) · Thread ops per doc 04
```

### 5.2 The bands change structure, not numbers

No band applies a dice penalty. Each removes or degrades a *capability of the person as a social
object* — which is what "integrity of layer-two self-rendering" has to mean if it means anything.

| band | effect |
|---|---|
| 10–8 **Whole** | none |
| 7–5 **Dissonant** | your *presented* marks read at −1 confidence. Passing gets harder. |
| 4–3 **Fragmented** | you may hold at most 2 primary Convictions; the third's weight decays 1/season. One stance row per season loses its provenance and becomes undefendable in argument (doc 07). |
| 2–1 **Fractured** | your tellings land at halved confidence regardless of the hearer's credulity; you may not `carry` a petition — nobody will let you speak for them. |
| 0 **Severed** | you stop individuating. You return to cohort fidelity, cannot originate petitions, cannot hold office. A person has become an object; this is P-06 expressed at the person layer rather than as a creature type. |

**Note what falls out of Dissonant without being written: passing degrades the capacity to pass.**
Each act of concealment that opposes a primary Identity conviction costs a Coherence step, and the
step makes the next concealment harder. Gerik Strand's ceiling is not a rule about Southern Einhir;
it is two mechanisms meeting.

### 5.3 P-12: contagion is a real channel, and it is bounded

At season end, for each depth-2 Knot: if the partner's Coherence dropped ≥ 2 this season, self
drops 1 — **once per season regardless of how many Knots qualify.** The cap is what stops a
peninsula-wide cascade from one Fell op while keeping the dramatic case (your Close partner is
being unmade and you can feel it). Cut the cap and P-12 is an extinction event; cut the channel and
P-12 is a sentence in a canon document with no code behind it.

---

## 6. Needs, computed

Needs are never stored. `needs(person) → ranked [(kind, urgency 0..5, referent)]`, evaluated at
decision time.

```
SUBSISTENCE   reads the WORLD (hearth larder — you feel hunger)
  urgency = clamp( 5 − floor( hearth.larder_days / (10 × hearth.mouth_weight) ), 0, 5 )

STANDING      reads the WORLD for WHO IS THERE, and the LEDGER for WHAT THEY HAVE SHOWN
  peers = siblings in the person's community node          # world: their faces are in front of you
  regard(peer) = Σ valence over the person's OWN claims about how `peer` regards them
                 — deposited by witnessed acts: a greeting, a cut, a sponsorship, a refusal,
                   a telling that reached them. NEVER read off peer.stance directly.
  r     = percentile of regard(peer) among peers, 0..1     # over peers with at least one such claim
  care  = max( stance[prop:Honor].weight, stance[prop:Identity].weight ) / 5
  urgency = round( 5 × (1 − r) × care )
  ── losing rank only hurts a person who holds rank as a value.

COMMITMENT    reads the VIEW
  for each faction f at commit degree d, for each active proposition p of f:
    unmet   = 1 if the person's LEDGER holds a claim that p is unsatisfied, else 0
    urgency = round( d × unmet × stance[p].weight / 5 )

EXPOSURE      reads the VIEW
  for each dispensation claim in the ledger whose scope contains the person's address:
    urgency = |Δ in the value of the person's own reachable options under the asserted terms|
```

**EXPRESSED regard, never true regard — a correction, and it narrows adjudication A-1.** An earlier
version of STANDING read `Σ(peer.stance[person].valence)` directly: the peers' **true interiors**,
concealed contempt included. That is a derivation of true state reaching a decision input without
passing through `witness` — adjudication A-2's banned object, arrived at through the stance table
instead of through the faction profile. Its concrete failure: a burgher who despises you and has never
shown it moves your STANDING urgency, so you feel a slight nobody has committed, and the whole politics
of the concealed enemy — the man who smiles at you for six seasons and then votes — becomes
unexpressible, because the game already told you.

A-1 ruled that standing reads the world, and it still does for the half of the term that is genuinely
in front of you: **who your peers are.** You cannot fail to notice that the Row is full of men. What you
cannot read is what is behind their faces. So the peer *set* is a world read and the regard *values* are
a ledger read, and a peer who has never expressed anything toward you contributes nothing rather than
contributing their hidden valence. The correction makes the substrate's own claim sharper rather than
weaker: **standing is not what your neighbours think of you, it is what your neighbours have let you
know they think of you** — which is the historical quantity, and the reason a man can be ruined in one
afternoon by a cut delivered in public that changed nobody's mind.

**The substrate says needs "change the instant the world does." Two of the four terms must not,
and the distinction is load-bearing.** Needs from the body and the room read the world. Needs from
the polity read the view. A fisher whose Duke signed a treaty three days ago has no changed need
until the crier reaches him — and when the crier's version is distorted, his need is computed from
the distortion. If EXPOSURE read the world, every person in scope would react correctly to a treaty
they had not heard of, and T4 would be broken by the needs function alone. §9 states this as a
formal sharpening of the substrate rather than a silent divergence.

Staleness is impossible in the sense that matters: no need is ever cached, so no need can disagree
with its own inputs. Staleness relative to the world is not a defect — it is the design.

- **Loop:** produced by evaluation at decision time · carried nowhere · consumed by option ranking,
  petition origination, faction commitment and the generator's constraint set.
- **Cut it and you lose:** any reason a person acts that a designer did not write down.

---

## 7. Cohorts and individuation

**One model, at two resolutions.** A cohort record has the *same schema as a person*, with three
differences: `weight ≥ 1`; each stance entry holds `(centroid, spread)` instead of a value; and the
memory ledger is shared, with a per-claim `reach` fraction naming what share of the cohort holds
it. Everything else — marks signature, capability centroid, coherence, Convictions — is the same
field at the same index.

That is why any mechanism written once runs at both fidelities. A cohort backs a petition at
`weight × centroid_valence`. A cohort sits an examination as an aggregate pass rate against the
same standard. A cohort's needs are computed by the same four terms with `mouth_weight` scaled.
No mechanism is elite-only, because there is no elite type.

**Individuation triggers, exhaustive:**

1. **Named.** Any act, telling, witness resolution or petition-backing that requires a *specific*
   referent inside the cohort. Praefect Aldwin fines "a smuggler"; the engine must produce one.
2. **Spread.** For any referent, `spread > 3` on the −5..+5 scale and `weight ≥ 2`. Split at the
   modal cleavage of that referent.
3. **Divergent view.** The shared ledger receives a claim whose channel reaches only part of the
   cohort (a Knot, a parish, one alley). Split by channel reach.
4. **Capability demand.** An attempt needs a practice at rank ≥ r that the centroid lacks but the
   spread implies some members hold.

**The remainder.** The split is moment-preserving: children's weighted stance means reconstruct the
parent's. `weight −= n`. When weight reaches 1, the record *is* a person — no conversion operation
exists, because none is needed.

**Re-merge, and the population bound.** Two cohorts at the same address with equal marks signature
and centroid distance < 1 on every referent of weight ≥ 3 merge. A **person** re-merges into a
cohort only when: no Knot, no office, no live petition, and **no other person's ledger names them.**

That last clause is the answer to CK3's 24,000-character save, and it is a design principle rather
than a memory optimisation: **a person persists exactly as long as somebody remembers them.** The
persons who survive in a hundred-year campaign are precisely the ones who mattered to someone, and
that is the correct set.

- **Cut cohorts and you lose:** populations that can act. Cut individuation and you lose the moment
  a crowd becomes a man with a name, which is the only moment where T5 becomes visible.

---

## 8. Person generation — on demand, never on a clock

**Triggers, exhaustive:** individuation (§7) · a succession pointer resolving to an heir who does
not yet exist · an admission act needing a candidate · a petition needing a carrier at a rung with
no live person · a view assembly requiring a subject the observer is looking at.

There is no monthly cohort of parentless sixteen-year-olds. Nothing generates without a demand.

**Backward consistency: generate the constraints first, sample the person second.** Before anyone
is made, the engine already knows:

1. the **address node** (fixed by the trigger);
2. the node's **marks distribution** — the Einhir hamlet outside Goldenfurt is 0.9 Southern Einhir,
   Kettlemakers' Row is 0.7 Central Einhir / 0.2 Crown-Latinate;
3. the node's **cohort stance centroid**, which seeds Convictions — the distributed cultural weight;
4. the **age band** and any `grade`/`church` the trigger demands;
5. **every claim already asserted about them in anyone's ledger.**

Item 5 is the mechanism. **Existing claims are constraints, and generation is constraint
satisfaction against the ledger, not free invention.** If three ledgers say the reeve's daughter is
a Thread-touched troublemaker, the generator must satisfy those rows — but only the
`firsthand`-rooted ones are binding. `told_by` claims are satisfied where cheap and *violated where
not*, and every violation is a person in the telling chain who lied or erred, which the engine now
owes as content rather than owing as a fix.

**History is not simulated backwards.** The new person gets a provenance stub: practice provenances,
mark provenances, and ≤5 seed claims. Each points at a real prior event in the containing node's
history if one exists; otherwise at a **synthetic root shared with the node's cohort** — the same
device the substrate uses for rumours, reused rather than reinvented. Consequence: a generated
person's past corroborates exactly once no matter how many people repeat it. Which is correct.
Their past is something people believe, not something that happened.

- **Loop:** produced by the five triggers · carried as a person record · consumed by everything ·
  reclaimed by §7's merge rule.
- **Cut on-demand generation and you lose:** a world whose population is bounded by what anyone
  remembers rather than by an authoring budget.

---

## 9. Worked trace — Gerik Strand sits the Masterpiece Examination

**Gerik Strand**, 26. Address: *Gerik / Hearth of Strand / Kettlemakers' Row / Goldenfurt /
Grauwald / Varfell*.
Marks: `heritage = Southern Einhir` (**presented Central Einhir**, Passing 3) · `grade = journeyman`
· `house = Strand` · `church = communicant` · `sensitivity = latent` (TS 34).
Attributes: Str 3 End 4 Agi 4 / Foc 5 Acu 4 Wil 5 / Att 3 Cha 2 Bonds 5.
Practices: `Kettle-smithing 4` (provenance: Hearth of Strand — a family shop, not sponsored; idiom:
Einhir chase-work) · `Passing 3` · `Thread-Listening 1`.
Coherence 8 (Whole). Convictions: Identity w5 (primary), Equity w4 (primary), Faith w1.
Credulity 2, obstinacy 2. Knot slots: `floor(5/2)+1 = 3`, one used — depth 2 to his cousin **Maret
Uln** in Oastad, strain +2.

**The gate.** `contest(Kettlemakers' Row, prize = Free Master, claimants = {Gerik})`. Judging set:
five Free Masters and the burgher. The standard has two clauses. Clause A is open: a piece in the
Crown-Latinate ornamental idiom. Clause B does not exist — there is no heritage clause anywhere.

Clause A alone costs Gerik two effective ranks (`Kettle-smithing 4` in the wrong idiom resolves at
2). Nobody wrote that; it is his practice provenance meeting a correlated standard.

**The read.** `attention` = |stance on `prop: Southern Einhir should not hold Free Master`|. Three
masters hold it at +4, +3, +2 with weight 4. Two hold it at 0 and do not look. The burgher holds it
at −1 — he owes the Hearth of Strand a debt.

Examiner **Hedda Rossum** (Acu 4, attention 4) probes. Gerik conceals at `Passing 3 + Will 5 = 8`.
Hedda pierces at `4 + 4 + prior claims`, and she holds one: *"Strand chase-work runs Southern,"*
told by a rival journeyman at confidence 0.6. That claim — plantable, refutable, attackable — is
what tips it. She pierces, and deposits `(Gerik, heritage, Southern Einhir, this season,
firsthand, 0.9)` into her own ledger.

**The vote.** Three masters revise to oppose; two are indifferent; the burgher would carry him.
Rejected 3–3 against a standard requiring four. No global rule fired at any point.

**The aftermath, all computed.**

- *Needs.* STANDING urgency jumps: his peers advanced, `r` falls to 0.2, `care = 5/5 = 1`, urgency
  `round(5 × 0.8 × 1) = 4`.
- *Stance.* Pressure on `stance[Kettlemakers' Row]`, currently (+1, w2): witnessed, severe, personal
  → pressure 12. `resist = 1 + 2 + 2 = 5`. `Δ = round(12/5) = 2`, clamped, applied negative → +1 →
  **−1**. Weight −1 (it moved) → w1. He is now *easier to move again*, which is what the next season
  does to him.
- *Coherence.* He resolved an attempt (passing) opposing his primary Identity (w5) at
  valence-distance ≥ 3. **Coherence 8 → 7: Dissonant.** His presented marks now read at −1
  confidence. Passing has become harder because he passed.
- *The Knot.* Strain +2 → `bandwidth = 2 − floor(2/3) = 2`. Maret Uln receives, unbidden, with no
  speaker and no distortion: `(Gerik, distress, high, this season, firsthand_via_knot, 0.7)`. She is
  in Oastad, three days away, and nobody told her. Coherence contagion does **not** fire: his drop
  was 1, the threshold is 2.

**The up-stroke, originated by a person holding no post.** Maret raises
`Petition(Maret, "examination standards shall publish their idiom clause and its grants record",
respondent = Kettlemakers' Row, backing = …)`. Conviction signature `{Equity +2, Scholastic +1,
Precedent −2}`. It seeds high with Southern Einhir journeymen in Oastad and Stillhelm — who have no
row for it and compute one from Equity — and negative with anyone whose `prop:Precedent` runs high,
which is most of the Row.

To make it bite, someone must produce the correlation: ten years of Free Master grants against
candidates' practice provenance. That is a field investigation (T9) over the guild roll, producing a
claim with a firsthand root, and it is the *only* thing in this trace that can convert a private
humiliation into an argument. The burgher may carry the petition or drop it; if he drops it, and if
Gerik ever learns he dropped it, `commitment` urgency toward the Restoration cell's proposition
rises by `d × w/5` and one more journeyman commits.

Nothing in that trace was authored. It is marks read through a stance, a standard correlated with a
provenance, one hysteresis line, one coherence band, one bandwidth number, and four need terms.

---

## 10. What this document refuses

- **A caste field, a caste modifier, or any global heritage term.** §1.3 reproduces the whole caste
  order out of stances held by the persons who hold gates. A global −2 cannot be reformed, cannot
  vary by town, and cannot be investigated.
- **A separate Disposition number.** It is `stance[person].valence`.
- **A separate Beliefs store.** The setting distinguishes Convictions (cultural), Beliefs
  (player-authored goals) and Duties (obligation). Under E-as-a-ratio, Beliefs are stance rows on
  propositions the player authored, and Duties are the obligation edges the hearth and the faction
  already own (substrate §4). Three stores that can disagree, replaced by one table plus two
  existing edges. Nothing is lost that I can name.
- **A trait vector.** Two scalars, one reader each (§3.2), and the test for surplus is stated.
- **An experience clock, a coherence recovery tick, or a passive strain decay.** All three are
  caused by acts.
- **A tenth attribute with invented content.** Reserved, inert, and honestly flagged (§2.1).
- **Any unique-person capability key.** Rarity is derived from the containment roll-up, so losing a
  person is a promotion.
- **Momentum, in any form — CUT, and this is a retraction rather than a simplification.** An
  earlier draft of this document carried a §3.5 Momentum streak that fed `+momentum_spent` into the
  pool. It is gone, and the N-line it claimed (*"the only mechanical account of how the Restoration
  produces outcomes"*) was false: a Conviction **is** a stance row (adjudication B-8), and stance
  rows already gate the willingness function, a negotiator's option set, concord, and view salience.
  Convictions keep their resolver consequence with Momentum deleted. What Momentum actually added
  was `+1 die` — a flat pool bonus, the one shape §2.3 and doc 10 §6 both refuse. Doc 10 §9 records
  the full disposition.
- **A trigger point published to the player.** Bands and inputs are published; thresholds are not.

---

## 11. CHALLENGE to the substrate

Three points, marked rather than silently diverged.

**11.1 "Needs change the instant the world does" is too strong, and the weaker claim is better.**
Substrate §2 says storing needs would be a stale copy of the world, so needs are computed and
change the instant the world does. Two of the four need terms must read the *view*, not the world
(§6), or a treaty changes the wants of every person in scope before any of them has heard of it —
and the signature rule falls to the needs function. The correct claim is: **needs are never stale
relative to the person's view, and are supposed to be stale relative to the world.** I believe this
strengthens §3.2 rather than weakening §2 and I have written it that way.

**11.2 The Knot's TS ≥ 30 gate makes the substrate's "channel for a person with no post" unavailable
to non-sensitives, and this should be stated as a deliberate asymmetry.** Substrate §2 names the
Knot as how a person with no post gets news. Half the peninsula cannot form one. I have kept the
gate because the resulting shape is excellent — formal institutions gate Southern Einhir *out*, the
informal channel gates them *in* — but the substrate should say so, because otherwise the next
reader will "fix" the gate and delete the reason Niflhel recruits on the waterfront.

**11.3 A person should be reclaimable, and the substrate's cohort section does not say so.**
Substrate §2 gives individuation but no inverse. Without §7's reference-count merge rule, a
long campaign accumulates persons monotonically — the CK3 failure by a different route. I have
proposed the rule (**a person persists exactly as long as somebody's ledger names them**) as a
design principle rather than a budget cap, and I think it belongs in the substrate.

---

## 12. Object roll-up

| object | producer | carrier | consumer | cut it and you lose |
|---|---|---|---|---|
| Mark | admission, birth, succession, ordination, grant | the person | reads, gates, judging sets | same act, same result, for everyone |
| Mark read | co-presence, probe, investigation spend | reader's ledger | gates, tellings, argument | concealment, forgery, mistaken identity |
| Passing | a standing act + `Passing` practice | `presented` field + exposure | pierce contests | caste transgression as play |
| Practice | generation, caused advancement | the person | pool, option list, correlated standards | attempting anything; skill's social address |
| Practice provenance | the teacher's address | the practice | correlated standards, argument | structural discrimination without villains |
| Stance row | `revise` | the person | salience, judging, backing, commitment, needs | every non-forced motive |
| Weight-as-hysteresis | `revise` | the row | future `revise` | zealots and converts |
| Conviction signature | authored with each proposition | the proposition | seeding a stance row | a position on the unencountered |
| Tie | co-presence, kinship, trade | edge | telling latency | hostile information channels |
| Knot | `form_knot` | bidirectional edge | unbidden deposit, buffering, counsel, contagion | news reaching the unposted first |
| Strain / bandwidth | five named uses; `invest` | the edge | deposit rate, rupture | depth having a price you can watch |
| Coherence | drift + discrete writes | the person | mark reads, primaries, tellings, individuation | any cost on Thread use and betrayal |
| Needs | evaluated at decision time | nowhere | options, petitions, commitment, generation | unauthored motivation |
| Cohort | generation, merge | one record, weight ≥ 1 | every mechanism, unchanged | populations that can act |
| Individuation | four triggers | split | the crowd becoming a man | the visible moment of T5 |
