# 04 — Personnel management

## Status: PROPOSED (2026-08-28) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md) · [`03_world_population.md`](03_world_population.md)
## Produces: the assignment surface — the layer where, in every surveyed game that has people, the player spends most of their decisions

---

## 1. What this layer is for

Every surveyed title with a roster puts the player's time here: assigning officers to cities and
commands, granting and revoking titles, renegotiating obligations, composing squads, filling council
seats. It is the screen people remember. It is also the layer that gets spammed if it ships without a
guardrail, which is why every mature example ships one — an outstanding-change cap, an escalating
price, a per-counterparty frequency limit — and why **the guardrail is designed here, with the
surface, rather than added after** (§6).

Seven modules. Each is a data row invocable by a post whose remit names it.

```
 pm.vacancy ─► pm.candidates ─► pm.appoint          the up-stroke
                                     │
                                     ▼
                                 pm.tenure ─► pm.audit ─► pm.succeed
                                     ▲            │
                                 pm.recall ───────┘        the down-stroke
                                 pm.custody                the sideways one
```

---

## 2. `pm.vacancy` — a vacancy is an event, not a null check

A post whose `holder_id` is `None` emits `post.vacant` once, carrying the tier node, the post kind and
the reason (`worldgen` · `death` · `revoked` · `term_expired` · `resigned`). The Key is what raises a
`cg.demand` (`02 §2.1`) and what a rival faction observes in order to contest the post.

**Why an event rather than a poll:** the reason a post is vacant is load-bearing downstream — a post
vacated by a recall carries a different politics than one vacated by a death — and a poll over a null
field cannot carry it.

---

## 3. `pm.candidates` — a gate, and it gates on class

```yaml
resolver: gate
```

The candidate set for a post is every person satisfying **all** of:

| requirement | reads |
|---|---|
| **presence** | an edge to the post's tier node, or residence at it |
| **qualification** | the post kind's declared qualification — a *class* of person, never a named individual and never a biography |
| **standing band** | `gauge_band(person.standing) ≥` the post kind's declared minimum band |
| **not barred** | no `Precedent` tag on the post or the person barring this pairing |

**No roll.** Eligibility is a threshold over state that is already on the board, which is exactly the
resolver kind the precedent survey finds this tree under-uses. Putting dice here would make a
question with a determinate answer uncertain.

### 3.1 Gate on class, never on biography

This is the single most consequential line in the module and it comes from a documented contrast. A
surveyed franchise gates which unit types a commander can recruit on the commander's **class** — so
losing a person is a promotion opportunity, and a mixed roster is the intended way to reach a full
option set. The alternative shape, gating on an individual's history — *the officer who has cavalry
experience* — means losing one person costs you a capability **permanently**, with no path back.

So a post kind declares a qualification like `qualification: martial` or `qualification: clerical`,
and a person satisfies it by their capability profile and conviction weights, not by having personally
done a thing before. Identity still changes outcomes (`05 §3`); it changes them by *who is eligible for
what*, not by making one person irreplaceable.

### 3.2 Disclosure

Eligibility is **published in full**: the player sees who qualifies and why, and sees who was excluded
and on which requirement. That is an input, and inputs are published.

What is not published is the **threshold at which the principal's preference tips** — see §4.2.

---

## 4. `pm.appoint` — the principal chooses; the engine does not roll

```yaml
resolver: gate
budget: {gauge: post.budget, cost: 1}
```

The principal (a faction, or a superior post) grants the post to one member of the candidate set.
Three writes, and only three:

1. `post_grant(post, person)` — `holder_id` set, `granted_season` stamped.
2. **Every passed-over candidate receives** `Grudge(owner_ref=(person, id), key=post_id, provenance=<the grant Key>)`,
   and a deposit into that person's edge-disposition toward the principal.
3. The wrapper emits `post.granted` with the appointee as subject and the passed-over set in
   `targets[]`.

Write 2 is one line in an appointment flow and it is the cheapest real mechanic in this suite: a
figure passed over for a post they wanted has a reason to act against the person who passed them over,
carried with provenance, decaying on its own. It is what makes an appointment a political act rather
than a personnel assignment.

### 4.1 Why the grudge cannot ramp

Two bounds, both structural rather than tuned:

- The **tag** dedupes on `(person, Grudge, post_id)` and refreshes in place, so repeated contests over
  one post do not stack tags.
- The **magnitude** lands in a Gauge with geometric decay, whose fixed point for a bounded
  per-season accrual `a` is `rest + a/λ` — finite for every `λ > 0`.

A grudge counter with neither bound is an unbounded ramp that feeds target selection which generates
more grudge, which is a real defect class and not a hypothetical one. Both bounds are preconditions of
this module landing, not refinements of it.

### 4.2 The principal's choice is the C2 decider

ED-IN-0201 clause 2: the person shapes which choice is made from the same option set with the same
information. Here that is literal — the option set is the candidate list, and **who the principal is
decides which candidate is picked**:

```
preference(candidate) = Σ_conviction  principal_holder.weight[c] · candidate.weight[c]   # structural
                      + qualification_margin(candidate, post)                            # structural
                      + clamp( gauge_value(edge principal_holder → candidate)
                               + Σ tag_value(Leverage or Debt over candidate),
                               ±RELATION_SHARE_MAX · structural_range )                   # relational, CAPPED
```

A different head of the same faction, with the same candidates and the same information, appoints a
different person. That is the ruling's wording satisfied by a **selection rule over declared inputs**,
not by a modifier on a roll — and it consumes no randomness.

**The relational cap is `01 §2.4` and it binds here hardest.** Uncapped, a warm disposition and a
debt outweigh every question of whether the candidate can do the job, and appointment becomes a pure
favour economy — which is the documented failure of relationship modifiers large enough to dissolve
structural conflict. Favour should tilt an appointment between two plausible candidates; it should
not put an unqualified one in office.

**Disclosure:** each term of `preference` is published *as a band per candidate*. The player can see
that their head strongly favours one candidate on conviction and mildly disfavours another on
disposition. What is never published is the resolved ordering's margin, or the tie-break. Publish the
reasons, never the trigger.

---

## 5. `pm.tenure` and `pm.audit` — the end of a term is the accounting

A post with `term = None` is held at pleasure and ends only by recall, death or resignation. A post
with a term expires at `granted_season + term`, and expiry triggers the audit.

### 5.1 `pm.audit` — the accumulated tags *are* the dossier

```yaml
resolver: d_sigma
```

| element | value |
|---|---|
| pool | the auditing post-holder's relevant attribute pair |
| obstacle | `derive_ob(holder.standing_value)` — E-1, fractional, floor `OB_MIN` |
| modifiers | the post's and the holder's tags, entering as a **σ-space μ-shift** via `net_boost` |
| shape | **SO** — the audited party does not roll; their standing is the obstacle |

**Modifiers are σ-space, never obstacle-space.** A flat obstacle shift is worth more against a small
pool than a large one, which makes the same dossier worth more against a weak auditor than a strong
one — the wrong direction and a non-uniform one. Routing tag weight through `net_boost` scales it by
`σ_N = 0.8·√Pool`, so a unit of evidence is worth the same amount of probability wherever it lands.

This is the mechanic that makes durable tags matter. A governor who took the fast method every season
accumulated `Grudge` and `Debt` tags on the place; at audit they are the evidence, and they are
citable because every one of them carries provenance.

### 5.2 The four outcomes, and all four are survivable

| degree | outcome |
|---|---|
| Overwhelming | **cleared with commendation** — `standing` deposit up; a `Reputation` tag replaces the prior |
| Success | **cleared** — `standing` deposit up, smaller |
| Partial | **censured** — a `Precedent` tag on the person naming the finding; standing unchanged |
| Failure | **stripped** — the post is revoked, `standing` deposit down, a `Precedent` tag recording the strip |

Two properties this table is built to have:

- **Total over the four bands, with no consequence unique to Partial.** Censure is a strictly
  intermediate outcome between cleared and stripped; if the Partial band's width changes, the ladder
  degrades gracefully rather than losing a mechanic. That is P0-3 honoured at the point it binds.
- **Failure is survivable and recoverable.** Stripping removes a *post*, not a person and not their
  future. Their tags travel with them, they remain in the candidate pool for other posts, and their
  standing recovers geometrically. There is no attainder, no elimination, and no permanent bar —
  because an irreversible outcome on a routinely-reached event is the failure P-iv exists to catch,
  and a post audit is routinely reached by design.

---

## 6. `pm.recall` — the guardrail is a provenance requirement, not a number

Mid-term removal. Two gates, and the first is the interesting one:

> **A recall must cite a Tag.** `pm.recall` takes a `cause: tag_id` and refuses to run without one.

That single requirement does most of the anti-spam work that other systems do with escalating opinion
penalties and per-counterparty frequency caps, and it does it in the game's own idiom: you cannot
remove someone for no reason, because *reasons are objects*. A principal who wants to recall a
governor must first have something on them — which means either the governor did something (a tag
written by a verb outcome) or the principal manufactured it (an action that itself writes a tag with
provenance, and is itself visible).

The second gate is the conventional one, and it is cheap now and expensive to retrofit:

> **One outstanding involuntary post change per principal per season**, and each successive one within
> the same term costs an escalating `standing` deposit from the principal's own holder.

### 6.1 Why both, and not just the second

The frequency cap alone bounds volume and says nothing about legitimacy — a principal can still churn
a post once a season forever. The provenance requirement alone bounds legitimacy and says nothing
about volume — a principal with a rich tag ledger could act on all of it at once. Together they bound
both, and neither needs a tuning pass to be correct.

---

## 7. `pm.succeed` — what survives a handover

On any vacancy, before the next appointment:

| carrier | disposition |
|---|---|
| tags on the **place** with `ttl=None` | **survive**. The place remembers |
| tags on the **place** with a ttl | swept normally |
| tags on the **person** | **travel with the person**, wherever they go next |
| the post's **budget** gauge | resets to its accrual baseline; unspent points do not carry |
| `Leverage` tags on the **post** (custody, §8) | **survive the holder change** — that is the point of custody |

The last row is the one worth stating explicitly. A demotion that leaves no residual reads as
consequence-free once survived, and a comeback that resets to zero is a reset button rather than a
recovery. Durable tags on the place and travelling tags on the person are what make a career a
history instead of a state.

---

## 8. `pm.custody` — controlling the holder without deposing them

Five independent surveyed systems separate *who holds the office* from *who controls the holder*, and
Valoria's own roster research named the absence as its sharpest architectural gap.

```yaml
resolver: d_sigma
budget: {gauge: post.budget, cost: 1}
```

| element | value |
|---|---|
| pool | the acting person's social attribute pair |
| obstacle | `derive_ob(holder.standing_value)` + the holder's declared protections |
| shape | **SO** |
| on Success | append `Leverage(owner_ref=(post, id), key=<actor person_id>, ttl=T, provenance=<Key>)` |
| on Overwhelming | as Success, with `ttl=None` (durable) and a deposit into the holder's `exposure` |
| on Partial | nothing gained; the attempt is recorded as a `Precedent` tag on the actor |
| on Failure | as Partial, plus a `Grudge` for the holder against the actor |

**Custody is a tag, not a field** (`01 §3.2`). It carries what a `custodian_id` would carry, plus a
ttl, a provenance chain and a decay a field would not have — and it costs no new schema.

What custody *does*: while a `Leverage` tag naming actor A sits on post P, A's preferences enter P's
holder's `preference` function (§4.2) and P's remit selection (`05 §3`). The holder still holds the
post. They still act. They act somewhat as A would.

---

## 9. Module contracts

```yaml
- module: pm.vacancy
  parent: personnel
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: gate
  remit: []                                  # raised by state, not invoked
  budget: null
  consumes:
    - {type: post.revoked, from: [pm.recall, pm.tenure, pm.audit]}
  emits: [{type: post.vacant, terminal: false}]
  state: [{name: post, bucket: post, writable: true, owner: substrate.post}]
  disclosure: [{of: post, inputs: published, presentation: exact, trigger: hidden}]

- module: pm.candidates
  parent: personnel
  scales: [settlement, territory]
  tier: null
  resolver: gate
  remit: [head, governor, minister]
  budget: null
  consumes: [{type: post.vacant, from: [pm.vacancy]}]
  emits: []
  state: []
  disclosure: [{of: candidate_set, inputs: published, presentation: exact, trigger: hidden}]

- module: pm.appoint
  parent: personnel
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: gate
  remit: [head, minister]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  emits: [{type: post.granted, terminal: false}]
  state:
    - {name: post, bucket: post, writable: true, owner: substrate.post}
    - {name: tag, bucket: tag, writable: true, owner: substrate.ledger}
    - {name: edge.disposition, bucket: gauge, writable: true, owner: substrate.entity}
  disclosure:
    - {of: preference, inputs: published, presentation: band, trigger: hidden}

- module: pm.tenure
  parent: personnel
  scales: [settlement, territory]
  tier: null
  resolver: gate
  remit: []
  budget: null
  consumes: []
  emits: [{type: post.revoked, terminal: false}]
  state: [{name: post, bucket: post, writable: true, owner: substrate.post}]
  disclosure: [{of: post.term, inputs: published, presentation: exact, trigger: hidden}]

- module: pm.audit
  parent: personnel
  scales: [settlement, territory]
  tier: null
  resolver: d_sigma
  remit: [head, minister]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  emits: [{type: post.revoked, terminal: false}]     # on Failure only
  state:
    - {name: standing, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: tag, bucket: tag, writable: true, owner: substrate.ledger}
  disclosure:
    - {of: standing, inputs: published, presentation: band, trigger: hidden}

- module: pm.recall
  parent: personnel
  scales: [settlement, territory]
  tier: null
  resolver: gate
  remit: [head, minister]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  emits: [{type: post.revoked, terminal: false}]
  state:
    - {name: post, bucket: post, writable: true, owner: substrate.post}
    - {name: standing, bucket: gauge, writable: true, owner: substrate.gauge}
  disclosure:
    - {of: recall_cause, inputs: published, presentation: exact, trigger: hidden}

- module: pm.custody
  parent: personnel
  scales: [settlement, territory, peninsula]
  tier: null
  resolver: d_sigma
  remit: [head, minister, envoy, clerk]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  emits: []
  state:
    - {name: tag, bucket: tag, writable: true, owner: substrate.ledger}
    - {name: exposure, bucket: gauge, writable: true, owner: substrate.gauge}
  disclosure:
    - {of: exposure, inputs: published, presentation: band, trigger: hidden}
```

Note `pm.custody`'s remit includes `clerk`. A clerk has no vote, no title and no holdings — and can
still acquire leverage over a post. That is the best available answer to *why would a player care
about a clerkship*, and it costs nothing but a remit row.

---

## 10. Property audit

**Scope.** `pm.vacancy`, `pm.candidates`, `pm.appoint`, `pm.tenure` and `pm.recall` resolve by
threshold and **roll nothing**; they are diagnosed on P-iii and P-v and **no N/R/S/E verdict is
offered for them**. `pm.audit` and `pm.custody` roll and are diagnosed on all five.

| property | verdict | reasoning |
|---|---|---|
| **P-i** legible odds | pass | Pool is the actor's own attribute pair, obstacle is `target_score/2` — both published. The audit's dossier terms are published per tag. This is among the most readable resolutions in the suite |
| **P-ii** uniform leverage | pass | Tag weight enters through `net_boost`, scaled by `σ_N`, never as a flat obstacle shift (§5.1). The failure this avoids is a dossier being worth more against a weak auditor than a strong one |
| **P-iii** bounded, monotonic | pass | The grudge is doubly bounded (§4.1): dedupe bounds tag count, geometric decay bounds magnitude. `derive_ob`'s floor prevents a cliff at `OB_MIN`. Recall volume is capped per principal per season and priced escalatingly |
| **P-iv** graded, recoverable | pass | Four outcomes, total over the bands, nothing unique to Partial (§5.2). The worst outcome removes a post, never a person; standing recovers geometrically; the stripped person stays in every other candidate pool |
| **P-v** right engine | pass | Appointment is a threshold on visible state → `gate`. The audit is a genuinely uncertain judgement over accumulated evidence → `d_sigma`. Custody is a contested attempt → `d_sigma`. Person-scale pools land inside the band the continuous engine is calibrated for |

**Loops.** Appointment → grudge → contested appointments → more grudge is a cycle whose gain runs
through the tag/gauge pair; both bounds in §4.1 are on the amplified variable, so it is damped *and*
capped. Recall → vacancy → appointment → recall is bounded by the per-season cap and priced by the
escalating standing deposit.

**Necessary** — this is the layer the roster exists for; a person object with no assignment surface is
a census. **Robust** — the two failure directions the surveyed precedent documents (an unbounded
grudge counter, a spammable assignment surface) are each closed structurally rather than by tuning.
**Smooth** — the same gate/roll split, the same `derive_ob`, the same four primitives as every other
document in the suite. **Elegant** — seven modules, and the two that carry the most political weight
(the passed-over grudge, the citable-cause recall) are one line and one required argument.
