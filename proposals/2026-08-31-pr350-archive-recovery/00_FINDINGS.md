# THE BEST IDEAS IN THE 2026-06-28 ARCHIVE — and what PR #350 is missing

## Status: **PROPOSED (2026-08-31). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Under `CLAUDE.md` §0.05 this document is **REFERENCE, never mechanism.** Under §0.2, **nothing here
## runs.** It audits a proposal that also does not run; neither fact excuses the other.

> **THE QUESTION, AS ASKED.** Does the idealized code shape in PR #350 miss anything previously
> identified in `archives/audit/` and `designs/` at `v30-snapshot-2026-06-28` that still provides value
> — for **NPCs, the world, factions, settlements and governance**?
>
> **THE STANDARD, AS RULED BY JORDAN THIS SESSION:** *"It doesn't matter if anything was already built —
> it only matters if it was built extremely well. We are reviewing all prior work only to identify the
> best ideas possible."*

---

## §0 · THE STANDARD THIS DOCUMENT APPLIES, AND WHAT IT DISQUALIFIES

**Merit only. Provenance is evidence about merit, never a substitute for it.**

| what does NOT make an idea good | what does |
|---|---|
| `## Status: CANONICAL` | it produces a possibility nothing else produces |
| a Jordan ratification | the mechanism is small and the consequences are large |
| it shipped, it was built, it runs | it composes on primitives already present, adding no system |
| a lane found it, or eight lanes found it | it survives the N-line test: **name what is lost if it is cut** |
| PR #350 already has it | it was **measured**, and the measurement had a control |

**Two consequences, both applied below rather than announced.** Canonical archive material is
**rejected** in §5 where it is not good enough — including a Jordan-ratified formula and a mechanism the
corpus called "narratively extreme" in its own text. And **PR #350's own best ideas are named as best
ideas** in §4, because "what is missing" is unanswerable without saying what is already excellent.

**What is still disqualifying**, because it is about truth rather than status: an idea explicitly
**retracted or refuted** in the corpus is never a finding. Every lane produced a DEAD ENDS section; the
inverted `Legitimacy = Mandate×20` arrow, faction-level L/PS, the "treated as Ob 4" floor, Niflhel, VTM
and the R6 death-spiral drain locations a grep proved absent from the code appear nowhere below.

### How this was produced

**12 Sonnet lanes** over disjoint file sets across the whole snapshot (114 archive + 705 design files),
each blind to PR #350 by instruction — ~42,000 words, ~200 findings, each with `path:line`, the source's
own status marker, and a rediscovery note. **3 Fable lanes**, read-only by agent definition (`Read`,
`Grep`, `Glob` — no `Write`, no `Edit`, no `Bash`, so independence is a property of the tool surface,
not of a sentence in a prompt), each on a different axis. This synthesis verified by hand every claim it
builds a conclusion on; §7 says which, and which it did not.

---

## §1 · THE ANSWER IN SHORT

**Roughly two-thirds of the archive's governance layer, PR #350 regenerates from smaller primitives** —
and that is a real result, not a preamble (§4). What it misses divides into three:

1. **The best idea in the archive is one PR #350 asserts and does not contain** — a mechanism by which a
   person's character *changes*. §2.1.
2. **The second-best is an invariant, not a number** — that the slate must exceed the budget, and that
   choosing is the gameplay. §2.2.
3. **A cluster of small, excellent mechanisms** that compose on what the shape already has. §2.3–§2.8.

And one finding is about method rather than content: **the shape deleted every stability mechanism the
corpus ever verified by running, ships ratchets of its own, and licenses nothing that could notice.** §3.

---

## §2 · THE BEST IDEAS, RANKED ON MERIT

### 2.1 · PER-CONVICTION SCARRING — the best idea in the archive, and the hole it fits is in PR #350

**The idea.** Each Conviction a person holds scars **independently**. Crisis fires when **any single**
Conviction reaches 3+ — never on an aggregate. The crisis roll lands **on the wounded axis**.

**Why it is excellent, on merit:**
- **It makes character change mechanical without a script.** An outcome wounds a specific commitment,
  and enough wounds to one commitment change who the person is. No authored arc, no beat.
- **It yields a non-obvious and true property**: a person with three primary Convictions is **more
  resilient** than one with a single primary, because damage distributes. The corpus grounds this in
  Charles V's Habsburg-Catholic combination being load-bearing for his longevity. **A design that
  produces a real historical dynamic from its own arithmetic has earned the mechanism.**
- **Its diagnosis of what it replaced is the sharpest sentence in either corpus**: aggregate scarring
  *"collapsed the vector to a scalar at exactly the moment it became most interpretively significant."*
- **It is already the right shape for PR #350.** A per-Conviction counter is interior primary state
  exactly like a ledger row, and its trigger matrix is a `witness` post-step — **a WITNESS-class write,
  which is precisely the row PR #350's write matrix is missing.**

**Its companion ideas, judged separately.** The **13×4 axis matrix** (thirteen Convictions projecting
onto `hierarchical`/`sacred`/`instrumental`/`traditional`, composed as a dot-product) is good because it
is **recomputed at read, never stored** — the archive arrived at Law 3 independently here and says so in
the file. The **orthogonal Self-Other scalar** is good for one reason worth quoting: *"Cesare Borgia and
a public-spirited magistrate may share a high Utility Conviction; what distinguishes them is for whom
they instrumentalize."* **One scalar separating what you believe from whom you serve, generating
divergent play from identical convictions, is a very high ratio of consequence to mechanism.**

**THE HOLE IT FITS, VERIFIED.** `02_ONTOLOGY.md` §5.5 presents a closed moral layer whose Conviction
column reads: *what moves it — **"slowly, by scar and crisis."*** **Nothing in the suite specifies a
scar or a crisis.** The suite says so itself, in `ADVERSARIAL.md`:

| row | verdict, verbatim |
|---|---|
| 12 · "a suppression scar" | ✗ *"named as a mechanism, **no object, no owner, no N-line**"* |
| 15 · `convictions`, `beliefs`, `Duty` | ⚠ *"Person owns them; **no rows in the write matrix at all**, and §4 says 'any unmarked cell is a write-class violation'"* |

**And nothing consumes a conviction.** Grepping all seventeen documents for a formula taking
`convictions` as input returns ownership statements only. The single operative clause is *"Convictions
weight the option ranking"* (`02`:877) — unformalized, in no signature in `08`.

**So the layer is circular.** Beliefs revise, but revision is an act the holder chooses, and `choose`
weighs by Convictions; Convictions move by scar and crisis; a scar has *no object, no owner, no N-line*.
**Every road out of the moral layer's statics runs through a mechanism the suite names and does not
contain.** Four axes of the archive's answer are meanwhile **live in the executing engine** —
`TRACE_REGISTER.md` records `AXES = (hierarchical, sacred, instrumental, traditional)` enforced with a
RAISE on every Key.

**N-LINE.** Cut it and no outcome ever changes what a person *is*. `02`:856's *"revising a Belief is a
tremor in the axis beneath it"* becomes a sentence about nothing, and `06`'s row 15
(suppression-breeds-return) has no producer.
**COST.** One registry table, one person-side Query, one interior counter family, and write-matrix rows
the suite owes regardless. **Zero new objects by the suite's own accounting.**
**FALSIFIER — one sentence Jordan could rule:** *"Convictions are flavour; character change enters this
game only through Belief revision."* That makes the statics sufficient and `02`:792's motion column a
defect to delete rather than a promise to keep.

> **Adopt the archive's mechanism with the archive's own known defect fixed:** its crisis table rolls a
> flat d6 without checking which Convictions the character actually weights. A 3-scar character with no
> Faith weight must never roll "Faith intercedes."

---

### 2.2 · THE SLATE MUST EXCEED THE BUDGET — an invariant that is better than the number attached to it

**The idea, verbatim from the primary:**

> *"There are always more opportunities than actions. **Choosing is the gameplay** — not executing, but
> deciding what to attend to and what to let pass. Opportunities not pursued do not wait — they resolve
> through NPC AI and clock advancement without player input, often in ways the player would not have
> chosen."*

**Why it is excellent:** it makes **triage** the unit of play rather than execution, and it makes the
unchosen option **cost something** rather than wait politely. That second clause is what most
opportunity systems get wrong, and it is one sentence.

**PR #350 has the same idea and states it as well** — *"the surplus is the point, not an overflow to be
minimised. Choosing what to attend to **is** the gameplay"* (`06` §4.5). **Independent arrival at the
same invariant from two corpora is the strongest signal available**, and the invariant is therefore
settled. What is not settled is the number.

#### The number, and why it is now a live correction

**Jordan ruled this session:** *"~5 playable scenes per season, which may mean ~5 actions."*

PR #350 states the opposite twice, in bold, as a universal: *"ONE ACT PER PERSON OR COHORT PER SEASON.
UNIVERSALLY. No office, rank or holding changes it, ever."* **And it already contradicts itself:** `06`
§4.5's funnel states *"6 reach the slate; 4 are acted on"* and ~200 played over 50 seasons — **four acts
per season.** The attention layer was built on a ~4-act season while the act economy declared one, and
no document reconciles them. **Jordan's ~5 resolves an existing collision toward the side already using
it.**

The archive's ladder — 3 / 4 / 5 scene-actions (Hard/Normal/Narrative) against a 7–9 / 5–7 / 4–5 slate —
is **not better for being canonical**; it is useful because **PR #350's own attention layer is already
wearing its numbers**: the suite ships a "4–9 candidates" slate, which is the union of the archive's
three rungs, and its 6-surfaced/4-acted funnel is the archive's Normal rung exactly. **The suite
inherited the archive's economy through its attention layer while its act economy contradicted it.**

**The hedge resolves, and the mapping matters more than the number.** The archive's season-level
currency is the **scene-action**; a scene costs 1–2 of them and contains 1–3 subsystem interactions. So:
**act ≡ scene-action (~5/season, universal); a scene is the rendered resolution of an act at `played`
fidelity — a camera artifact, not a budget unit.** This preserves PR #350's central refusal, because the
within-scene interactions live behind the `09` seam where fidelity invariance already governs them.

**What must NOT be imported, and this is the merit judgment:** the archive scoped its budget
**player-only** (NPC factions take one action off a priority tree; individual NPCs have none; Standing
grants +1/+2). **That is the weaker design** — it is the elite-politics back door PR #350's every-rung
rule exists to close, and it is a GM-shaped answer in a game with no GM. **PR #350's symmetry is the
better idea and should win.** But symmetric-~5 is then a **departure that must be priced**: ~5× NPC-side
act volume, so the funnel's 190–200 candidates is not scale-free; and a flat 5 silently answers the
archive's open difficulty question by picking the Narrative rung, which should be said out loud. The
archive's Standing bonus is meanwhile **covered better** by PR #350's establishment/dispatch mechanism —
the archive's own text says the bonus comes *"from faction resources,"* which is the establishment
intuition stored in the wrong place. **The suite should claim that synthesis rather than ignore the
precedent.**

#### Three surrounding mechanisms, judged individually

- **Witness Mode** — when mandatory scenes exceed the budget, unattended ones resolve at **0 cost** via
  a Read/Appraise at Ob 1 (*not* auto-success), with **no Domain Echo and no Momentum/Coherence
  change.** *Good idea, and PR #350's is better*: `auto` fidelity generalises it to every person and
  drops the player-only free Read. **Take the generalisation, not the mechanism.**
- **Exactly one between-scene currency** — each subsystem owns a *within*-scene resource
  (Wounds/Stamina · Composure/Concentration · Coherence · Exposure); a second between-scene resource was
  proposed and **rejected as double-penalising.** *Excellent, and it is the archive's own argument for
  PR #350's act-as-only-currency shape.*
- **The budget is fractal** — inside an investigation scene, a time budget of 3 over a 4–9 node graph,
  *"not a new resource — it is the scene action budget expressed spatially."* *Good: one scarcity shape
  reused at two scales rather than a second currency invented.*

#### What ~5 voids in PR #350

- **`14`:139 records the petition-spray dominance defect as *"closed — PROVISIONALLY by one act per
  person."*** **That closure is now void** — at five acts a person can spray five petitions.
- `ADVERSARIAL.md` §5.6's S-UP break (a convener's `compose_agenda` costing his whole season) **largely
  dissolves at 5**, and §5.7's news-transport arithmetic divides by ~5. **The suite's own adversarial
  pass is stale on the new budget.**
- **`seat_items` was deleted** on *"one allowance: the act."* At five allowances that identity must be
  re-argued — the double-count evidence survives, the identity claim does not follow from it.
- `dispatch` costing both parties a whole season, and every cost priced in person-seasons (including
  `wear` vs restoration in `05` §2.1), are off by 5×.
- **The transposed R-39 hazard is real.** A stress test found that at 5 actions, mandatory content alone
  consumed the entire budget — *"NPCs always have the initiative."* PR #350's literal version cannot
  recur (mandatory rows force *attention*, never *acts*, and demands are refusable), but *a season in
  which obligations convert all five acts* is unmeasured and belongs beside `12` §6's owed measurements.

---

### 2.3 · FEUD TRANSMITS ALONG KINSHIP ON DEATH — the best small idea in the corpus

**The idea.** Six typed relationship edges, of which **kinship and feud cannot break by strain — they
transition**; and on death, **a feud auto-transmits along every strength-2+ kinship edge.**

**Why it is excellent:** *one rule produces multigenerational narrative.* The archive's own primary
names it *"the key load-bearing mechanic for ROTK-style emergent multigenerational narrative."* The
unbreakability is equally good and less obvious — modelling kinship as strain-breakable *misrepresents
what kinship is*, and the design says so.

**Why PR #350 needs it.** Its person-person kinds are `tie` (decays), `knot` (ruptures) and `oblige` —
**and `oblige` is destroyed by death.** Enmity's carriers are stance rows and Grudge claims, and **claim
confidence decays under the universal rule the suite celebrates** as *"a governor loses the town by
being forgotten."* The same rule means **a feud is lost by being forgotten** — the opposite of the
intended texture. Nothing at death writes anything into an heir's ledger.

**N-LINE.** The Capulet/Montague campaign. Without it every enmity is one generation deep and **every
death is a reset button**, which inverts `06`'s own hostage-politics row.
**COST, and the adaptation is better than the original:** one WITNESS/CENSUS rule depositing the
deceased's high-weight negative stances into ledgers of kin reachable by `succeed`/`oblige` —
**inheritance as witnessing with a channel**, so an heir abroad inherits the feud *when the news reaches
him.* Strictly better than the archive's instant transmission, and it preserves per-person arrival.

*(The other five edge types genuinely dissolve into PR #350 — liege-vassal → `hold`+`oblige`, patronage
→ upkeep/Debt, and rivalry → emergent via ambition-obstruction, which is **better than the archive's
typed edge**. Only this residue needs carrying.)*

---

### 2.4 · "ACYCLIC PROVENANCE IS NOT LOOP-SAFETY" — the best principle found

Stated twice in one session from two artifacts: the `causes[]` graph is acyclic **by construction**, but
every turn of a behavioural spiral emits a new, legitimately-caused entry, so **the DAG grows forward
and never trips cycle detection while the system spirals.** *"A collapse spiral is, to the substrate, a
perfectly valid, perfectly acyclic chain."*

**Why it is excellent:** it is a *false-security* finding — it identifies a guarantee that looks like it
covers a risk and does not. PR #350 rests its narrative layer, audit trail and arc model on `causes[]`.
This is developed as §3, because it is the finding about method.

---

### 2.5 · THE DETERMINISTIC FLOOR OVER THE PROBABILITY FLOOR

**The idea, and the lesson attached.** An anti-death-spiral protection reading *"at Stability ≤2, treat
as Ob 4"* was **measured mathematically inert** — a 2-die pool against Ob 4 succeeds ~1% of the time, so
the "protection" protected nothing. It was replaced with a **deterministic floor**: at Stability ≤2 the
accounting check *cannot reduce* Stability at all; only an active trigger can.

**Why it is excellent, independent of the stat it protected** (which PR #350 correctly deletes): **a
rule that looks protective but is mathematically inert is a whole defect class**, and this is a worked
instance with the arithmetic shown. The general form — *check whether a probabilistic guard's
probability actually guards* — transfers to any floor, cap or fallback in either corpus.

---

### 2.6 · INSTITUTIONAL CAPTURE THROUGH HELPFULNESS

**The idea.** A Chapel gives **+0.5 Order/season to *any* governor who hosts it, secular or not** — and
generates Piety the host cannot switch off. Church presence is four **independent stacking axes**, not a
ladder. **Pastoral Assumption** lets the Church install a governor in any ungoverned settlement holding
a Chapel.

**Why it is excellent:** **accepting the help is itself the vector of losing control.** That is a far
better political mechanic than a Church-versus-Crown war, and the corpus grounds it — *"theocracies grew
not through hostility but through helpfulness"* (Papal States, Geneva, 1979 Iran).

**Disposition, on merit:** PR #350 **generates** this, and its version is better — a Chapel is a Site
with drawers and an office whose establishment **acts**; the +0.5/season drip is a scheduled social
recovery and the auto-firing Assumption is a social change with no actor, both correctly refused. **Take
the insight and the content; leave the carriers.** The archive independently confirms the mechanic reads
in play: a curate NPC in its vertical slice has this arc and nothing else.

---

### 2.7 · SCARCITY OF SEATS MANUFACTURES POLITICS WITH NOBODY ACTING

A Seat has exactly **3 Wing slots**. When full and a fourth claimant arrives, the only outcomes are: a
holder departs, the settlement pays to expand (capped +1/decade), or the claimant takes a provisional
rank requiring a recurring contest to hold.

**Why it is excellent:** *"a political crisis without any political act by any faction"* — the crisis is
generated by a resource limit, so the engine never has to invent one. **PR #350 can express this**
(`establishment[]` is "finite, contested, durable" by design; `capacity(date)` and cardinality on
`hold`) but **nothing in it produces the crisis until a cap is authored.** One registry row; content,
not architecture — and worth authoring.

---

### 2.8 · TWO-STAGE SUCCESSION

**The idea.** Stage 1 resolves *who leads* — stochastic, a contest. Stage 2 resolves *whether the realm
fragments* — **deterministic**, on the numeric strength gap: G≥3 unified, G=2 fractious, G≤1 splits
60/40.

**Why it is excellent:** it separates a genuinely *contested* question (appropriately random) from a
*structural* one (which should follow the numbers). The single-roll version it replaced fragmented ~50%
of near-peer successions **on dice variance regardless of the actual power balance** — a clean
demonstration that one roll answering two questions produces wrong variance.

**Disposition:** PR #350 covers it in principle — who-leads is a contest, whether-it-splits emerges from
members individually re-committing. **The general pattern is the keeper**, and it has one immediate
application: **`leaders()` should read `succeed` edges before its comparator.** `02` §10 proposes
*commitment degree × backing raisable* with no mention of the `succeed` Tenure the shape already ships
one section away. A comparator that ignores standing designations makes every named-heir situation a
computed surprise and deletes the disputed-will shape entirely.

---

## §3 · THE FINDING ABOUT METHOD — the shape cannot see the one defect class the corpus found by running

**PR #350's Law 3 (no stored aggregate) and Law 4 (exactly three clock-driven quantities) jointly delete
every stability mechanism the archive ever verified**, and its anti-apparatus predicate then stops it
owing anything in their place.

| the archive's damper | what PR #350 does with it |
|---|---|
| saturating aggregate `7T/(T+6)` | refused — nothing stored to saturate |
| deterministic floor (§2.5) | refused — a special-cased outcome on a stored social stat |
| mean-reverting drift, **sim-verified convergent over 30 seasons** | doubly refused — writes social state with no act as driver, on a schedule |
| the rich-get-richer Standing fix (~8pp of Order-share over 3 years) | survives only as a warning nobody read |

**Each refusal is individually correct.** The problem is the composite: **the shape ships ratchets of
its own** — suppression scars *"ratchet the arming threshold"*, grievance cheapens `commit` while revolt
generates grievance — **and licenses no bounded-loop assertion among its four guards, owes no
measurement of boundedness among its six, and has no termination argument anywhere in 10,619 lines.**
The archive held itself to a higher bar here: even its *designed-only* defection cascade shipped with
*"net per-cycle gain < 1 ⇒ damped; reach and depth finite ⇒ bounded"* written beside the mechanism.

**Why the existing defences don't cover it.** The termination caps are **per-tick** — every season of a
spiral is individually legal and under-cap, which is exactly the distinction §2.4 draws. Law 3 stops a
stored aggregate *being* the runaway state; it does nothing about primary state spiralling while every
Query truthfully reports it. And `06` §6.3 addresses **convergence** (does the interesting thing
happen?), not **boundedness** (does the world stay playable) — while supplying the resolution it does
not apply: *"if convergence is a game property, it is a property of `wear`, the act budget and the date
calendar — and it is settled by running campaigns, not by building a checker."* **Boundedness is a game
property by the same sentence, and running campaigns is exactly the method that found the 0-of-120
result.**

> **COST: three edits, zero objects, no checker.**
> **(a)** A seventh row in `12` §6 — *whether act-caused feedback is bounded under sustained shock* —
> settled by a two-arm seeded battery on the n≥100 control discipline `12` already mandates, using
> `tools/balance_oracle.py`, which already exists.
> **(b)** One sentence in `14`'s N-line discipline: *a mechanism whose output feeds its own input carries
> a termination argument in its row.*
> **(c)** One falsifier row in `15`: *Laws 3 and 4 are wrong-as-scoped if a bounded political layer
> requires either a saturating stored aggregate or a driver-less restoring drift.* Laws 3 and 4 are
> alone among the four in lacking a falsifier in the dynamic regime — which `15`'s own standard
> ("a ruling without one is an opinion") forbids.

**The empirical warrant.** A 120-campaign instrumented battery found the canonical victory condition
fired **0/120**, because conquest — the only territory-acquiring action — lowered the very Accord the
victory demanded. *"The two halves of the design were never reconciled."* **The transferable idea is not
the gate but the control: measure whether your win condition is reachable under your own action economy
before shipping it.**

---

## §4 · WHAT PR #350 ALREADY DOES EXCELLENTLY

Under a merit standard this is not a courtesy section — these are among the best ideas found anywhere in
the review, and several beat their archive counterparts outright.

- **A faction is somebody's morals, said out loud, that other people signed.** A `Proposition` of mood
  `OUGHT` *is* an uttered Belief; a faction is that plus its `commit` edges. **This is the best idea in
  PR #350.** It grounds the entire political layer in one person having said what they think is right,
  and it makes the hypocrite and the founder-discredited-movement fall out for free.
- **Obstruction needs no verb.** Ambition progress is derived at read over ordinary world terms, so a
  stranger who takes the seat you needed has obstructed you **without knowing you exist and without the
  resolver branching on anything.** Better than the archive's typed rivalry edge, which had to assign
  the rivalry.
- **Nobody is omniscient, enforced by what the signatures omit.** `choose` has no `World` — not masked,
  not read-only. And **a View is *built*, not filtered**: absence produces absence, never a widened
  interval, *"because a widened interval is uncertainty and this game needs ignorance."*
- **The Partition keyed on `(record-kind, field)`.** Stated over subjects it concedes a mixed class, and
  *"both" is not a partition*; keyed on the field, **the mixed class dissolves because there was never
  one change to classify.** The worked case earns it: a plague may empty a village and may not destroy
  it.
- **Fidelity is a camera, never a formula** — one resolver, identical rolls and seeds; a fast path is a
  *formula* where a played path is a *process*, and two different kinds of thing can only be made to
  agree on average.
- **Mechanisms it regenerates from smaller primitives**, each checked: fractional province ownership
  (per-settlement `hold`s make mixed control the natural state); the Ministry as a non-faction actor (an
  Office cluster with `rung? = null`); graduated autonomy (`commit.avowal ∈ {avowed, private, covert}`
  carries "nominal loyalty, functional independence" natively, where the archive stored a stage enum);
  franchise as unequal weight (venue doors + `judging_set_rule`); and **the reformist leader's court
  resisting him** — nine establishment members' own `choose`, **better than an α-blended cascade
  constant**, because each courtier's convictions are their own and the immutable Proposition means a
  reformer cannot rewrite the banner, only utter a new one and migrate commits: **a schism made
  visible.**
- **Refusals that are right against archive material:** Domain Echo's scalar write to a faction integer
  is superseded by acts→Events→WITNESS — *the very fix the archive itself proposed and never executed*;
  the archive's instant *"all NPCs at Disposition ≥+1 take −1"* obligation ripple is **consensus
  broadcast**, the exact forbidden shape; and **the archive's worst structural defect — a central world
  clock writing off the Key bus and invisible to narration — is unrepresentable in this shape.**

---

## §5 · ARCHIVE IDEAS REJECTED ON MERIT — including canonical and ratified ones

The standard cuts here, and it is the section that makes the standard real.

| idea | status in corpus | why it is not good enough |
|---|---|---|
| **Mandate `= clamp(round(7T/(T+6)))`** | Jordan ruling LPS-2e; eight-lane convergence | Its inputs L/PS are stored per-settlement social aggregates, **measured dead in the running tree**; its "few huge > many small" property **holds only above ~4:1 weight contrast**; its weight term likely **double-counts development**; and **D4 (Jordan, 2026-07-13) already retired it as the collapse carrier.** *What survives is a dossier, not a formula:* saturating shape = legitimacy mass, floor-of-mean = collapse detection. |
| **90%-per-arc treaty lapse** | CANONICAL | **The document calls it "narratively extreme" in its own text** — "almost every Treaty breaks every arc." It existed to nerf one faction's win rate. A balance residue to re-measure, not an idea. |
| **Domain Echo's direct scalar write** | live mechanism, 7 lanes | The archive itself proposed replacing it: *"the ripple should flow up through the substrate, one scale at a time, rather than teleporting to a faction integer."* **Superseded by its own corpus.** |
| **The 28-card event deck's gating** | built, sim-tested | Every card gated on a composite pressure quantity **three of whose four summands are social** — so *the deck selected its events by reading society's temperature.* PR #350's trigger purity indicts it by name and is right. |
| **Territory temperament α/β values** | header says CANONICAL | The same document's footer says PROVISIONAL pending calibration that never ran. **The axis is a good idea; the numbers are placeholders wearing a status line.** |
| **The MS trajectory model's numbers** | CANONICAL | Three canonical sources disagreed on its baseline direction and its cap was disputed. It is also global-scalar-shaped, which PR #350's own falsifier names as the wrong object. **The shape transplants; the numbers do not — and it does NOT supply the `wear`:restoration measurement `02` §10 asks for.** |
| **The archive's player-only action budget** | CANONICAL | It is the elite-politics back door, and a GM-shaped answer in a game with no GM. **PR #350's symmetry is the better idea.** (§2.2) |
| **The α-weighted faction cascade** | PP-686 v2, CANONICAL | Approximates numerically what PR #350 produces structurally. **Keep the weights as calibration input; the mechanism is worse.** |
| **PP-688's articulation tiers** | five contradictory status markers in one file | Its stored trackers need Law-3 rework. **What survives is its prior-art law** (below), not its architecture. |

**One archive idea rejected as a *mechanism* but kept as a *constraint*:** a mechanism-level survey of
seven acclaimed titles found that **no acclaimed narrative game generates text at runtime** — they
author tagged fragment libraries offline and select/substitute/splice at runtime. **That is evidence,
not a design, and it forecloses a proposal someone will otherwise make.** PR #350 says nothing about
turning state into readable narrative and `render` is a named operation with no owner; its declared
exclusions are combat, social contest and mass battle **only**, so presentation is not excluded — **it
is unaddressed.** If Jordan scopes it out, it becomes one sequencing row; fragment authoring is a large
design-time cost with no line item either way.

---

## §6 · WHAT TO DO

### Adopt — merit-ranked, zero new objects
1. **Per-Conviction scarring**, with the 13×4 matrix as a read-time Query and Self-Other as
   outcome-driven drift; fix the archive's flat-d6 defect on the way in. (§2.1)
2. **Feud inheritance at death**, as witnessing-with-a-channel. (§2.3)
3. **The damping discipline row and the boundedness measurement.** (§3)
4. **Cultural-background templates** as the representation for the cohort construal spread `02` §10
   carries as open — the archive's 8 templates are the answer-shape, with a measured authoring-cost
   result attached.
5. **`leaders()` reads `succeed` before its comparator.** (§2.8)
6. **Hysteretic band edges** — a recovery edge above the collapse edge. Without it, a site at the
   wear≈tending equilibrium — *the row `05` calls the game* — **strobes its verb set and spams crossing
   events both ways**, and recovery is as cheap as collapse, deleting the flux model's asymmetry at
   exactly the margin where play concentrates.
7. **Author a seat cap** so §2.7's crisis generator actually fires.

### Correct in PR #350
8. **The act economy to ~5**, with `dispatch`'s cost basis, the `seat_items` deletion, `14`:139's void
   closure, and every person-season price. Price the departure from the archive's asymmetry rather than
   ignoring it. (§2.2)
9. **`02` §5.5's motion column** — specify scar and crisis, or delete the claim.
10. **Land the `opening_set` overturn.** `08` row 20 and `15` row 13 say it returns **`Candidate[]`, NOT
    `Act[]`** — and **`07` §3.2 still ships `-> Act[]` and `12`'s test still asserts over act families.**
    *The suite reproduces at its own HEAD the archive failure five lanes documented: a ruling and a
    landed edit are different events.* One line in `13` closes the class: **an overturn is not folded
    until every document it names carries it, and the fold list is part of the ruling row.**
11. **R-11's first ground** — *"a Conviction is already a stance row"* is false by the suite's own §2.1.
    The Momentum cut survives on its other two grounds; **a wrong mechanism attached to a right
    conclusion is what `02`:171 warns "survives review by being agreeable."**
12. **Mark test-3 and test-4 dispositions provisional-pending-sweep.** Two of `15` §3's twelve fail
    against unread canon — the act economy, and *"which seats a campaign offers at start"*, which
    `player_agency_v30` §1.4/§5.1–5.3 answers (campaigns start low; every seat is reachable). **And that
    answer has a consequence:** since seats are reachable mid-campaign, "offered at start" does not bound
    R's domain, so `06` §6.4's defect-or-portrait exemption does no work — **the two dominance defects
    that reproduce the flagship arc are defects.**

### Escalate — these survive all five of `CLAUDE.md` §0's tests
13. **Is the action budget symmetric?** §2.2 argues PR #350's symmetry is the better idea and the
    archive's asymmetry should lose. **That is a recommendation, not a ruling.**
14. **Does a scene contain acts, or is a scene an act?** §2.2 proposes act ≡ scene-action, scene = the
    rendered resolution at `played` fidelity. Jordan's hedge, Jordan's call.
15. **Does D4's renamed Mandate meter survive Law 3, or does Law 3 amend D4?** A 2026-07-13 ratification
    and a proposed law are in direct conflict and **neither document notices**, because the suite never
    read the ruling.

---

## §7 · THE HONEST STATE

**Nothing here executes**, and it audits a suite that does not execute either.

**Verified by hand for this synthesis:** `ADVERSARIAL.md` rows 12 and 15, and the absence of any
conviction consumer across all seventeen documents (§2.1); `player_agency_v30`'s 3–5 budget and its
status line in the snapshot primary (§2.2); PR #350's own one-act and 4-acted-on statements (§2.2);
`14`:139's now-void closure; the `opening_set` split — `08` row 20 and `15` row 13 against `07` §3.2 and
`12` (§6.10); and `governance_consolidation_v1`'s D2 and D4 ruling text in the live tree (§5, §6.15).

**Not verified:** most individual lane citations. Twelve lanes produced ~200 findings; the Fable lanes
hand-checked their own load-bearing subsets and each reported which. **A lane citation not in the list
above is advisory.**

**On convergence, applying the standard to this document.** Eleven cross-lane convergences are indexed
in `01_CONVERGENCE.md`. **C-3** (derive-don't-store, five applications, different authors and PPs) and
**C-11** (the season economy, five documents on the figures, four on the phase order) carry real
independence. **C-1 does not** — eight lanes agreeing that Mandate is derived is mostly one ruling
propagating, and it is counted once. *PR #350 applies this rule unevenly to itself: `16` correctly
discounts a two-lane convergence as "one comparison, not two derivations", then banks "one act per
person | 3 routes" where all three routes descend from the same design line and the corpus's own
precedent points the other way.*

**The measurable cost of the unread 138.** `16` §4 admits the sweep read 24 of 162 documents. **One
unread document has now cost a same-day Jordan overturn of the suite's most-repeated economic claim,
voided a banked closure, staled two of its own adversarial findings, and mispriced four load-bearing
passages.** A second instantiates a ruling's own falsifier condition. **The scope limit was honestly
declared; the error was letting "answered by precedent" verdicts issue from inside it.**

**And the same limit applies here.** Twelve lanes read the archive at varying depth; one covered roughly
20% of a 1.26M-character file by finding-count. **We have not read it all either.**
