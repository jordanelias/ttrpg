<!-- STATUS: PROPOSED — held back in full. Three architectures, none adopted. -->
<!-- AUTHORITY: none claimed. Rules nothing, supersedes nothing. -->

# How behaviour may be calculated — three multi-phase architectures

## Status: PROPOSED — HELD BACK

**§0.05 class: REFERENCE.** Nothing here is a mechanism. Companion to `behaviour_census.md`,
which is the diagnosis this builds on.

Jordan, this session, verbatim: *"I didn't say this needed to be a clean weighted sum equalling 1.
I expect this to include formulas and transformations and matrices and gates and so forth."*

---

## §0 The finding that reframes the brief

**The live engine is already a four-phase algorithm. The weighted sum is only phase three.**

Read bottom-up from `engine/season/loop/deliberate.py:102` outward, a season decision runs:

| | phase | owner | what it is | what it reads |
|---|---|---|---|---|
| **Φ1** | **OCCASION** | `queries/world_q.py:159` → `decision/questions.py:45` | what am I being asked about? | `World` (resolver-side) |
| **Φ2** | **APERTURE** | `decision/options.py:35` | what could I coherently do? | `Person` + `View` only |
| **Φ3** | **APPRAISAL** | `decision/choose.py:302` | how do I rank them? | `Person` |
| **Φ4** | **COMMITMENT** | `_sample_order` → `pack_scenes` → `ask_budget()` | what do I actually spend on? | `Person` |

Φ2 is **already** a gate-and-filter stage — four clauses, none of them a score:

```
{ Candidate(verb, subject, why, operands) :
    verb in the verb table                              -- the roster
  , eligibility(verb, p) holds                          -- the GATE
  , subject in referents(q)                             -- the OCCASION
  , requires(verb) not KNOWN-FALSE from p's OWN claims   -- the EPISTEMIC filter
  , every operand is DERIVABLE }                        -- the instrument's refusal
```

So the architecture Jordan is asking for is not a replacement for what runs — it is **a statement
of what belongs in each of the four phases**, and the additive sum at Φ3 is one candidate policy
for one phase, not the shape of the whole thing. The three proposals below differ in **where the
hard part lives**.

---

## §1 What was measured first, because a proposal built on a guess is worth nothing

### 1.1 The proactive channel exists, fires every season, and is starved

`questions_for` has four sources, declared in order at `rosters.yaml: question_sources`:
`date_due` → `claim_landed` → `band_crossed` → **`need`**. Q4 `need` is *"a live `commit` Tenure
whose object is an OUGHT Proposition"* — **that is the ambition mechanism**, and its own comment
says it exists so that *"an NPC with a standing ambition and a quiet season"* still acts.

Measured on `build_realm(0, cap=12)`, ticking the real season loop:

| after | `date_due` | `claim_landed` | `band_crossed` | **`need`** | questions per person |
|---|---:|---:|---:|---:|---|
| 0 seasons | 0 | 0 | 0 | **12** | 1 each |
| 1 season | 0 | 136 | 0 | **12** | 8 – 18 |
| 2 seasons | 0 | 180 | 0 | **12** | 7 – 28 |
| 3 seasons | 0 | 172 | 0 | **12** | 5 – 27 |

**`need` leads for 12 of 12 persons at genesis and 0 of 12 in every season after.** Reactive
traffic grows without bound; the standing ambition stays at exactly one question per person and
sorts last. A person carrying 27 questions answers a claim about somebody else's granary and never
reaches the thing they want.

> ⚠ **I PREDICTED THIS BEFORE MEASURING IT AND WAS WRONG ABOUT GENESIS.** The prediction was
> "ambition is starved because it sorts last"; at tick 0 it is the *only* question anyone has, and
> leads for everyone. The starvation is a function of accumulated reactive volume, not of the sort
> order alone — the sort order is what converts volume into starvation. §0.1 pt 3's first row.

### 1.2 One deliberation consumes ONE question, and the rule is already a swept hole

`deliberate.py:108` — `q_p = aggregate_questions(qs, q_rule)`. `H-54`, with three arms in
`decision/questions.py:45`: `first` (the incumbent), `one_per_source`, `all`. Its own comment:
*"taking the first silently ruled that A DATE ALWAYS BEATS A NEED, which decides what every NPC
does first."*

Measured at tick 2 — does the ambition's referent reach the deliberation at all?

| `q_rule` | ambition reaches deliberation | mean referents carried |
|---|---|---|
| **`first`** — what runs today | **0 / 12** | 1.0 |
| `one_per_source` | **12 / 12** | 2.0 |
| `all` | **12 / 12** | 5.8 |

**A one-word data edit restores the proactive channel.** Every proposal below assumes this is done;
none of them works without it, and it is not itself one of the proposals.

### 1.3 The two constraints every proposal has to respect

- **No interior write has a producer.** `H-62`: `(Person, convictions)`, `(Person, beliefs)`,
  `(Person, scar)`, `(Person, axis_count)` and `(Person, stance)` are all `social: true` — only an
  act may write them — and **no verb in the table does.** Any phase that remembers something about
  the character needs a producer that does not exist yet.
- **Evidence may not move a conviction.** `state/world.py:86`, a refusal law:
  *"S9.3 — WITNESS NEVER TOUCHES A BELIEF. If evidence can move a conviction the moral layer has
  become a second epistemic layer and T2 is gone."* A proposal that scars a conviction must do it
  through the person's **own act**, never through what they saw.

---

## §2 PROPOSAL A — **The Ladder**

**Hard part: Φ2 and the ordering.** Lexicographic tiers, scored only within a tier.

A character's considerations are sorted into tiers by *kind*, not by strength. A lower tier speaks
only when every higher tier is indifferent. This is the descendant of the priority tree already
canonical at `npc_behavior_v30.md:774`, made person-scale and given a scored tail.

```
Φ1  OCCASION    q_rule = one_per_source            (§1.2 — non-negotiable)
Φ2  APERTURE    gates, in order, each an ADMIT/REFUSE:
                  caste/heritage  →  office+remit  →  presence  →  ownership  →  belief
Φ3  APPRAISAL   tiers, lexicographic; additive ONLY within a tier:
                  T0  survival      subsistence below floor                  -> overrides all
                  T1  duty          the office's remit acts, this season     -> outranks T2+
                  T2  ambition      candidates serving a live OUGHT commit
                  T3  preference    Σ conviction[axis] · alignment(verb,axis)
                  T4  regard        stance_toward(subject)
Φ4  COMMITMENT  budget triage, unchanged
```

**Where the twelve inputs enter:**

| input | phase | operator kind |
|---|---|---|
| ethnicity/caste · profession | Φ2 | **gate** |
| obligations, office, faction | Φ2 gate + Φ3 T1 | **gate then tier** |
| ambitions | Φ1 source + Φ3 T2 | **generator then tier** |
| needs | Φ3 T0 threshold | **gate** |
| moral · religious values | Φ3 T3 | **weight** |
| character opinions | Φ3 T4 | **weight** |
| memories · epistemic | Φ2 clause 4 | **filter** |
| fears · self vs public | — | **unplaced; see §5** |

**Worked example.** A bailiff with a live ambition to hold the reeve's seat, a docket date due, and
a granary claim in his ledger. Φ2 admits the eight remit acts his `hold` Tenure grants plus the
`own`-eligible verbs. Φ3: subsistence is fine (T0 silent), the date is a remit duty (T1 fires) —
**he serves the docket, and his ambition never speaks.** Next season, no date: T1 silent, T2 fires,
he petitions. His convictions decide only *how* he petitions, never *whether*.

**Strengths.** Deterministic and cheap — no draws, no state. Legible to a player: *"he had no
choice, his office required it."* Golden-testable. It is the only proposal that needs **nothing that
does not already exist** beyond the `q_rule` edit.

**Failure mode, stated plainly.** A tier boundary is a cliff. A character one point above the
subsistence floor is a different creature from one a point below, with nothing in between. And T3 —
the entire conviction apparatus — speaks only when nobody has a duty and nobody has an ambition,
which on the measured traffic is rare. **This proposal makes convictions nearly inert by ordering,**
which is the defect it inherits from the priority tree rather than fixes.

**Falsifier.** Run the corpus under A and count how often T3 is the deciding tier. If it is under
~10% of deliberations, convictions are decorative and A is wrong.

---

## §3 PROPOSAL B — **Two Bodies**

**Hard part: Φ4, and a persistent store.** A standing agenda and the world's occasions compete for
attention by *accrued pressure*, not by sort order.

The character carries a **standing agenda** — ambitions, office remit duties, and unmet needs — that
persists across seasons. Each item holds a **pressure** that rises while unserved. The world supplies
**occasions**. Both propose candidates into one pool, and the pool is ranked by pressure.

```
Φ0  ACCRUE      (new, runs at the season boundary)
                  for each standing item i:
                      pressure[i] += rate(kind_i) * (1 if unserved this season else 0)
                      pressure[i] *= decay if served
                  a NEED served after long duration spawns a FEAR item (see below)
Φ1  OCCASION    occasions from questions_for, PLUS every standing item above its floor
Φ2  APERTURE    unchanged — gates
Φ3  APPRAISAL   score(c) = pressure_of_the_item_c_serves * fit(c)
                  where fit = Σ conviction[axis] · alignment(verb, axis), normalised
Φ4  COMMITMENT  budget triage over the merged pool
```

**The needs counter is the point, and it is Jordan's specification directly.** Verbatim: *"needs
must be tracked on a counter. a longstanding need is going to inform an ambition with far more
weight than a new need. a longstanding need finally being met may even turn into a fear for that
character, ie a fear of starving again."*

So a need carries `(magnitude, duration)` and its pressure is a function of both — **duration is the
term that makes a long hunger outrank a fresh insult.** When a long-held need is met, the item does
not vanish: it **transforms into a fear**, a standing item with inverted polarity that *penalises*
candidates risking its recurrence. A fear is a need's scar.

**Why the starvation in §1.1 cannot recur here.** Under `first`, an unserved ambition stays at rank
N forever. Under B, being unserved *is what raises its pressure* — the mechanism is self-correcting
by construction. A character ignored by the world long enough eventually acts on their own account,
which is what "proactive" means.

**Strengths.** Satisfies proactive/reactive structurally rather than by tuning. Produces arcs with
no author — a character whose need goes unmet for six seasons behaves visibly differently from one
fed on schedule, and nobody wrote that. This is NERS-**R**'s half with no player in it: *"emergent
and compelling narrative hooks and scenarios WITHOUT player involvement."*

**What it needs that does not exist.**
- **A persistent per-person store** for pressure. `H-62` forbids every interior write, so this needs
  a producing verb or a new carrier field with an act behind it. **This is the single largest cost
  of proposal B and it should not be understated.**
- **`rate()` and `decay` are invented numbers.** They need an `H-` row with a declared default and a
  sweep, per §G's discipline. Not a blocker — that is what the register is for — but not free.

**Failure mode.** Pressure accrual is a ratchet, and ratchets saturate. If every item rises and
nothing falls fast enough, after enough seasons everything is at ceiling and the ranking is noise
again — the same starvation, arrived at from the other direction. The decay term is load-bearing
and is exactly the parameter with no source.

**Falsifier.** Run twenty seasons and plot the pressure distribution. If it is bimodal at the
ceiling, B has saturated and the decay model is wrong.

---

## §4 PROPOSAL C — **The Internal Contest**

**Hard part: Φ3, resolved by draw rather than by arithmetic.**

When two considerations **of different operator kinds** conflict above a threshold — ambition against
duty, fear against need, conviction against office — the engine does not add them. It runs a
**contest** between them, using the same ladder the game already uses for a social contest:
`degree_from_net` in `engine/autoload/dice_engine.py`.

```
Φ3a  NOMINATE   each standing consideration nominates its best surviving candidate
                  (duty nominates a remit act; ambition nominates its OUGHT-serving act;
                   fear nominates an avoidance; conviction nominates its best-aligned verb)
Φ3b  DETECT     if the top two nominations are of DIFFERENT operator kinds and their
                  strengths are within a threshold, this is a genuine fork
Φ3c  CONTEST    resolve by draw: pool from the stronger consideration, Ob from the weaker
Φ3d  READ THE MARGIN
                  degree -> WHICH action        (the winner)
                  margin -> HOW it is performed (the manner)
                  a NARROW loss leaves a SCAR on the losing consideration
```

**Three things this buys that neither A nor B does.**

1. **§8 compliance by construction.** The resolution rule lives once, in the dice engine, and the
   decision layer *calls* it rather than mirroring it. Every other proposal invents a second way to
   settle a close call.
2. **Margin becomes manner.** The degree ladder already returns bands, not a boolean. A character who
   barely chose duty over ambition performs the duty *resentfully* — which is the "manner of
   expression" axis `engine/season/cases/NPC4.yaml:368` records as an open need at
   `hardness: important`, and which `derived_stats_v30.md` calls Resonant Style. **This proposal
   produces it as a by-product rather than adding a field for it.**
3. **It supplies the missing Scar producer without violating S9.3.** `H-62` says no verb writes
   `(Person, scar)`. Here the writer is **the person's own act of choosing against themselves** —
   not evidence, not a witness. S9.3 forbids evidence moving a conviction; it says nothing about a
   person wounding their own. That is the distinction the refusal law is actually drawn on, and it
   is what makes the Conviction Scar mechanic at `conviction_track_v1.md` §2 executable at last.

**Strengths.** The most Valorian of the three — it makes the interior of a character run on the same
physics as the exterior. It is the only proposal that generates *manner* as well as *action*, and the
only one that closes the Scar loop.

**What it needs that does not exist.** A threshold with no source (an `H-` row, declare · default ·
sweep). A `(Person, scar)` producer — the same `H-62` cost as B, though a smaller one: a scar is
written on a resolved contest, which is already an act.

**Failure mode.** Non-determinism makes goldens harder, and a draw per fork is not free. Worse: if
the threshold is loose, *everything* becomes a contest and the character is a dice-driven weathervane
with no stable disposition — the opposite of a conviction. **C is the proposal most able to destroy
the thing it is modelling if mis-tuned.**

**Falsifier.** Count forks per deliberation across the corpus. If the median is above ~1, the
threshold is too loose and the character has no settled character.

---

## §5 What none of the three places, and that is a finding

**Self-interest vs public interest** and **fears** land in different phases depending on the proposal
and cleanly in none of them.

- Self/other is **already a live registered scalar** — `orient.self_other` at
  `references/descriptor_registry.yaml:260`, with its own drift formula and its own attribution
  formula at `conviction_taxonomy_v30.md` §3.1–§3.2. It is not an axis and should not become one;
  taxonomy §2.3 factors it *out* of Convictions deliberately, citing Borgia against a
  public-spirited magistrate with identical Utility. **It belongs at Φ4, modifying what the character
  counts as a win**, not at Φ3 modifying what they prefer.
- **Fear is an operator kind none of the five names.** It is not a weight, a modifier, a gate, a
  generator or a susceptibility — it is an *anti-generator*: it removes candidates from consideration
  before they are ranked, and it is produced by history rather than held as a trait. Proposal B gives
  it a home by accident (a need's scar); A and C have nowhere to put it. **If fear matters, that is
  an argument for B's persistent store independent of the pressure model.**

---

## §6 Comparison, and what they actually cost

| | **A — Ladder** | **B — Two Bodies** | **C — Internal Contest** |
|---|---|---|---|
| hard part at | Φ2 / ordering | Φ4 / persistence | Φ3 / resolution |
| needs a new store | **no** | **yes** (`H-62`) | yes, smaller |
| needs invented numbers | no | `rate`, `decay` | one threshold |
| deterministic | yes | yes | **no** |
| produces *manner* | no | no | **yes** |
| closes the Scar loop | no | partly (fear) | **yes** |
| proactive by construction | no — by tier position | **yes** | no |
| convictions load-bearing | **weakly** — T3 rarely reached | yes, as `fit` | yes, as a contestant |
| failure mode | tier cliffs; convictions inert | pressure saturation | dice-driven weathervane |

**They are not mutually exclusive, and that is the most useful thing in this document.** They sit at
different phases. The real question is not *which one* but *what policy at each phase*:

- **Φ1** — `one_per_source`. Measured, near-free, and every proposal fails without it.
- **Φ2** — A's gate ordering. Nothing else proposes anything here and the gates already exist.
- **Φ3** — B's `pressure × fit` **or** C's contest. This is the genuine fork.
- **Φ4** — B's merged pool, with self/other modifying what counts as served.

**Recommendation, stated as a recommendation and not as a finding.** Take **A's skeleton, B's Φ0/Φ4,
and C's Φ3 fork detection but not yet its draw** — that is, detect the conflict and record it, resolve
it by B's pressure for now, and hold the contest until the threshold has a sweep behind it. That
sequence is also the cheapest order to build: the `q_rule` edit costs a word, the gate ordering costs
nothing new, the pressure store is the one real `H-62` bill, and the contest can be added later at
Φ3 without disturbing anything above it.

---

## §8 The Question carrier is the aperture, and it is too thin to vary

**Jordan, this session:** *"Questions may need to be expanded/rewritten to enable more variability
and information."* Measured, and he is right in a sharper way than the instruction states.

### 8.1 More questions buy volume, not variability

`Question` today is four fields (`state/carriers.py:242`): `id`, `source`, `referents`, `about`.
Φ2 clause 3 is *"subject in referents(q)"* — so **the referent tuple is the only thing that varies
the aperture.** Measured at tick 2 on `build_realm(0, 12)`:

| `q_rule` | referents | candidates/person | **distinct verbs reached** |
|---|---:|---:|---:|
| `first` | 1.0 | 24.9 | **28** |
| `one_per_source` | 2.0 | 50.2 | **28** |
| `all` | 5.8 | 154.3 (min 50, max 239) | **28** |

**~25 candidates per referent, linear, and the verb set never moves.** Six times the referents
yields six times the candidates and **not one new kind of action.** Widening the question widens
the cartesian product; it does not widen what a person can *do*.

The ten verbs no rule ever reaches are the governance set:
`confer · convene · destroy_record · determine · dispatch · establish · issue · levy · open_case ·
revoke`. They are capped by the **eligibility gate** (`H-71`), not by the question — which locates
the defect precisely: **volume is bounded by `referents`, variety is bounded by Φ2's gate.** Adding
question sources cannot fix variety, and that is worth knowing before anyone adds one.

### 8.2 `source` is provenance, and the carrier has no field for *what the question is*

`claim_landed` supplies 136–180 of every person's questions and covers a threat, a gift, an insult
and an idle rumour **identically**. Nothing downstream can tell them apart, because the only type
information on the carrier says where it came from.

That is the information deficit. Six additions, each earning its place from a phase that needs it
and each grounded in something already single-owned:

| add | what it carries | which phase needs it | grounded in |
|---|---|---|---|
| **roles on `referents`** | `subject` / `object` / `witness` / `beneficiary` / `bystander` instead of a flat tuple | **Φ2** — bind a verb's subject operand to the *subject*-role referent, not to every referent | `engine/substrate/keys.py:63` — the roster already exists and is single-owned. §8-clean, invents nothing. |
| **`kind`** | `obligation · opportunity · threat · grievance · offer · summons` — orthogonal to `source` | **Φ3** — lets duty, fear and ambition be told apart without inspecting a payload | new closed roster; the `source` roster's own note says *"the roster is where a fifth would be argued for"* |
| **`stake`** | what changes if this goes unanswered, signed, per referent | **Φ3 — and this is the repair for `H-73`** | see 8.3 |
| **`asker`** | who is owed the answer | **Φ3** — `stance_toward` needs somebody to have a stance *about* | `Claim` already knows its depositor |
| **`horizon`** | when it stops being answerable | **Φ1/Φ4** — triage needs to know what expires | Q1 reads a `Date` and **throws the date away** |
| **`witnesses`** | who will know what you chose | **Φ3** — Jordan's *"how will the other judge me"* | `key_substrate_v30.md` §6.2 already computes visibility from scene presence |

**`witnesses` belongs on the Question, not on the person.** Whether an act is observed is a property
of the occasion, not a trait of the actor — which is why "how will they judge me" never fitted as a
thirteenth conviction or an eighth axis. It is not something a character *has*. It is something a
situation *is*.

### 8.3 `stake` is not a new idea — it is the fix for a measured dead term

§F2's third term is `urgency(sensation.subsistence)`, and `choose.py:89` records that it **cannot
change any decision**: *"the third term HAS NO `c` IN IT. It is added identically to every candidate,
so it cannot move the ranking."* Registered as `H-73`, inert by construction, kept only so deleting
it would not hide the finding.

A stake carried on the Question makes that term a function of `c` — but **the obvious keying does
not work, and I only found that by running it.**

**MEASURED, and it corrected this proposal.** I added a stake of `+k` to every candidate whose
`subject` is the at-risk referent and swept `k` over 0.25 … 5.0 on twelve deliberating persons:

| stake `k` | top choice changed | first-five scene slate changed |
|---:|---:|---:|
| 0.25 – 5.00 | **0 / 12 at every magnitude** | 12 / 12 at every magnitude |

A term that reorders the whole tail and never once changes what anybody *does*. Two measurements
explain it, and both are structural:

1. **The top candidate's subject is already the at-risk referent, 12 / 12.** Under `one_per_source`
   the leading referent is what the person is most engaged with, so a subject-keyed stake lifts the
   incumbent and its rivals **by the same amount**. It is degenerate at the top by construction.
2. **The gap between first and second place is exactly 0.0000 for all twelve.** Convictions do not
   pick a winner; they pick a **plateau** of 2.2 candidates on average (min 2, max 4), all tied at
   the winning score, and `sorted(..., key=(-score, c.verb, c.subject))` breaks the tie by the
   **alphabetical order of the verb's name**. That is hole-register row 1275's prediction, confirmed.

> ⚠ The narrow reading of that second result is the true one and the sweeping reading is false.
> The chosen verbs across twelve persons are `tie / knot` ×4, `create_record` ×2, `utter` ×2,
> `forge`, `comply`, `commit`, `evade / defy` — **not** the alphabetically-first verbs. Convictions
> *do* discriminate, down to a plateau of two to four; the alphabet decides only within the
> plateau. "The alphabet decides everything" would have been the more quotable claim and it is
> wrong.

**So the correction: a stake must discriminate VERBS, not SUBJECTS.** *"The granary is two weeks
from empty"* has to favour `transfer` and `work` over `speak` and `tell` **about that same granary**
— which is a stake × verb table, the same shape as `alignment`, not a bonus attached to a referent.
That in turn makes `kind` (8.2) the load-bearing addition rather than `stake`: `kind × verb` is a
discriminating table; `stake × subject` is a constant added to a tie.

### 8.4 What this does to the three proposals

- **A (Ladder)** gains its tier tests: `kind: obligation` *is* T1, `kind: threat` *is* T0's trigger.
  Without `kind`, A's tiers have to be inferred from `source`, which cannot distinguish them.
- **B (Two Bodies)** gains `stake` and `horizon` as the pressure function's inputs, which is most of
  what `rate()` was going to have to invent.
- **C (Internal Contest)** gains `witnesses` as the term that decides whether a fork is *worth*
  contesting — a private choice and a public one are different decisions, which is the whole of
  Jordan's judged-by-others axis.

**All three need `kind`. None of them needs a new question source.** That is the ordering: rewrite
the carrier before extending the roster.

---

## §7 Falsifiers

| claim | falsifier |
|---|---|
| §1.1 — `need` leads 12/12 at genesis, 0/12 after | re-run `questions_for` over `build_realm(0,12)` at ticks 0–3 and count leading sources. |
| §1.2 — `one_per_source` restores ambition reach | re-run the three-arm sweep; `first` must give 0/12 and the other two 12/12. |
| §0 — the live engine is already four-phase | `deliberate.py:102–120` → `options.py:35` → `choose.py:302` → `pack_scenes`. Find a fifth stage or show one of these is not a stage. |
| §4 — a Scar producer does not violate S9.3 | `world.py:86` forbids **WITNESS** touching a belief. Show that an act by the person themselves is reached by that law, and C's claim fails. |
| §6 — the three compose | name a phase where two of them make incompatible demands. None was found; that is an absence of evidence and the weakest claim here. |
| §8.1 — more referents add no verbs | re-run the aperture sweep. If `all` reaches more than 28 distinct verbs, the claim is wrong. |
| §8.1 — the ten are gated, not question-bound | admit a remit act person-side (H-71 arm 2) and re-run. The verb count must rise without any question change. |
| §8.3 — a subject-keyed stake cannot decide | re-run the 0.25–5.0 sweep. If any magnitude moves a top choice, the degeneracy claim is wrong. |
| §8.3 — convictions pick a 2–4 plateau, not a winner | re-measure the first-to-second score gap. A non-zero gap anywhere falsifies it. |
| §8.3 — the alphabet decides only *within* the plateau | list the chosen verbs. If they are the alphabetically-first reachable verbs, the stronger claim was right and mine is too weak. |

**Not claimed:** that any of the three is correct, that the phase skeleton is the only possible one,
or that the twelve inputs are fully placed — §5 says two are not.
