# 04 — Personnel management

## Status: PROPOSED (2026-08-29) — held back from ratification-on-merge
## Reads: [`00_INDEX.md`](00_INDEX.md) · [`01_substrate_primitives.md`](01_substrate_primitives.md) ·
## [`01_substrate_primitives_part2.md`](01_substrate_primitives_part2.md) ·
## `systems/factions/faction_politics_v30.md` (Part 3, caste integration) ·
## predecessor: `proposals/2026-08-28-greenfield-systems-suite/04_personnel_management.md` (v1, ARCHIVED)
## Produces: the assignment surface — the layer where, in every surveyed game that has people, the player spends most of their decisions

**Scope of this document (per the delta spec): v1 unchanged, plus one addition** — the ratified caste
gating matrix now gates `pm.candidates`. Everything in §§1–8 not marked `v2`/`v3` is v1's design,
carried with its reasoning. The v2 material is §3.2 (the caste gate itself), the `class:` field on every
module contract (§10, mandated by `00 §7`), and §9 (the player-facing surface table `00 §2.3.4`
requires).

**v3 — four surgical corrections against the three-critic review, each an edit and none a rewrite:**
**§4.0** an `accepts:` gate so an appointee can refuse (T1-3 — without it a ratified arc shape and the
corpus's most duplicated arc family are unreachable); **§3.2.2a** one institution-id roster, because this
document and `07` were about to key the same registry file on two incompatible vocabularies (A-F10);
**§9.1** the honest bill against `00 §2.2`'s playing-surface budget, with recall and custody routed
through Slate items rather than self-initiated (A-F9); **§11** the property audit re-scoped to the two
modules that actually roll (A-F11). **No new module, no new resolver kind, no new Key type, no new
registry file.**

## Overrides

| # | What is overridden | Tier | Why |
|---|---|---|---|
| **O-04-1** | v1 `04 §4`'s unconditional "deposit into that person's edge-disposition toward the principal" (write 2 of `pm.appoint`) | this suite's own v1 | `01 §7.3`'s O-3 (adopted whole in `01`, not re-argued here) makes NPC↔NPC disposition a **derivation**, never a stored gauge. A stored deposit on an NPC↔NPC pair would violate the one write rule (`01 §2.1`) the same way v1's edge design did before `01` caught it. §4 below makes the write conditional on which kind of edge it is, and states what carries the effect when it is not |

**Adopted whole, on the merits, not by compliance.** The authority note attached to this task lifted
every tier from *must-follow* to *overridable-with-an-argument* — including Jordan's own 2026-08-14
`derive_ob` ruling and the caste matrix below. This document does not touch `derive_ob` (out of scope;
no complaint against it). It **does** examine the caste matrix on the merits and keeps it: `§3.2`
explains why a bespoke gating scheme would be the elegance failure `00 §1` names — re-deriving a worse,
thinner version of ten institution-specific rows (with a deliberately *bidirectional* asymmetry already
argued in prose) to avoid depending on canon. Recorded here because, per `01 §5.3`'s own precedent for
the Light Function, **deciding not to override is also a decision.**

---

## 1. What this layer is for

*(v1, unchanged.)* Every surveyed title with a roster puts the player's time here: assigning officers
to cities and commands, granting and revoking titles, renegotiating obligations, filling council seats.
It is the screen people remember. It is also the layer that gets spammed if it ships without a
guardrail, which is why every mature example ships one, and why **the guardrail is designed here, with
the surface, rather than added after** (§6).

Seven modules, unchanged in count and shape. Each is a data row invocable by a post whose remit names
it (`01 §4.3`).

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

*(v1, unchanged.)* A post whose `holder_id` is `None` emits `post.vacant` once, carrying the tier node,
the post kind and the reason (`worldgen` · `death` · `revoked` · `term_expired` · `resigned`). **v2
context, not a change:** the vacancy gate now applies per tier (`05 §3`), so a faction missing a
governor in one settlement but not another stops acting only at that tier — `pm.vacancy` itself does
not change; what changed is which gate reads it.

---

## 3. `pm.candidates` — a gate, and it gates on class, standing, and now caste

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
| **caste** *(v2, §3.2)* | `person.caste` (identity) against `content_registry.yaml`'s `caste_gate` matrix, keyed on the post's granting institution and kind |

**No roll.** Eligibility is a threshold over state already on the board — `00 §6` principle 4: *gate
where the answer is on the board, roll where it is genuinely uncertain.* Adding a fifth conjunctive term
does not change the resolver; it is one more predicate in an `AND`, same as the four it joins.

### 3.1 Gate on class, never on biography

*(v1, unchanged.)* A post kind declares a qualification like `qualification: martial` or
`qualification: clerical`, and a person satisfies it by their capability profile and conviction
weights, not by having personally done a thing before. Identity still changes outcomes (`05 §3`); it
changes them by *who is eligible for what*, not by making one person irreplaceable.

### 3.2 The caste gate — F, the ratified matrix, and why it lives here

**Where it binds.** `00 §4.3`'s change F names `pm.candidates` as "the exact right place" for caste
gating: it is the eligibility gate, and eligibility is exactly what caste bears on in this setting.
*Emergent possibility lost if cut:* the game's central social injustice would be flavour text (`00 §4.3`).

#### 3.2.1 What canon says, cited by `path:line`

Three castes, ratified (`systems/factions/faction_politics_v30.md:644-651`, §3.1): **Northern Einhir**
and **Central Einhir** are unstigmatized defaults; **Southern Einhir** is stigmatized, structurally
excluded from post-war settlement, and the caste the matrix (§3.2, `:653-668`) gates hardest — *except
where it does not*. Six worked rows, chosen to show the matrix runs in **both directions**, not just
against Southern Einhir:

| institution | Northern | Central | Southern | citation |
|---|---|---|---|---|
| **Crown** | full | full | Std 0→3 open; higher rungs need a named exception (Public Deed, inner-circle sponsorship burning Disposition, or bloodline-extinction/deed-claim) | `:657` |
| **Church** | full | full | strongly gated; Canon+ "a scandal"; **Temperance branch (Klapp) is the canon's own carve-out — caste-neutral in practice** | `:660` |
| **Guild** (`guilds`) | full | full | variable; Free Master examination biased; Guild Master/Comptroller near-closed | `:665` |
| **Niflhel** (`niflhel`) | full | full | **favoured — "caste-blind by necessity"** | `:613`, `:666` |
| **Warden of the Thread** (`warden`) | **gated** — lower baseline Thread Sensitivity makes the initiation threshold harder | slightly gated | **favoured** — higher baseline TS, cultural familiarity | `:636`, `:667` |
| **Restoration Movement** (`restoration_movement`) | ideologically suspect (gated) | variable | ideologically favoured — the RM's base | `:668` |

**The Warden and RM rows are the design intent this document is told, correctly, not to normalise
away.** `:636` states it in prose: *"The Wardens are, effectively, the resistance infrastructure for
the caste system's victims — and the player who climbs this ladder encounters that dynamic directly."*
A caste_gate schema that could only ever *close* options for a stigmatized caste would be unable to
express this row at all. §3.2.2's verdict grammar is signed for exactly this reason.

#### 3.2.2 The registry, and why it is keyed one level finer than `00 §9` states

`00 §9`'s registry table names the payload as *"the `(post_kind, caste)` → open | gated | closed
matrix."* Read literally against the table above, that key **erases every asymmetry in it**: `head`
under `crown` and `head` under `niflhel` would collapse to one verdict per caste, when canon's whole
point is that they differ. This document keys the matrix one level finer — **`(institution, post_kind,
caste)`** — and reads it as `00 §9`'s stated payload realized as *one `(post_kind, caste)` sub-matrix
per institution*, not as a change to which file it lives in or who reads it. Flagged for `00`'s author
in this document's closing report rather than edited there, per this suite's one-file-per-author rule.

```yaml
# references/content_registry.yaml  §caste_gate  (00 §9; read by pm.candidates only, never by a roller)
caste_gate:
  crown:
    head:     {southern_einhir: {closed: {unless: "Precedent:crown.bloodline_extinction_or_deed_claim"}}}
    minister: {southern_einhir: {gated:  {predicate: "person holds Precedent:crown.extraordinary_circumstances_sponsorship"}}}
    governor: {southern_einhir: {gated:  {predicate: "person holds Precedent:crown.public_deed_exceeding"}}}
    # northern_einhir, central_einhir: open at every post_kind (:657) — the registry omits an
    # explicit `open` row per 01 §2.4's spirit: absence from the matrix IS open, stated once here.
  church:
    head:     {southern_einhir: {closed: {unless: "Precedent:church.extraordinary_circumstances"}}}
    minister: {southern_einhir: {gated:  {predicate: "person holds Precedent:church.cardinal_or_confessor_sponsorship"}}}
    envoy:    {southern_einhir: {gated:  {predicate: "person holds Precedent:church.unusual_circumstances_sponsorship"}}}
    clerk:    {southern_einhir: open}   # "accessible but suspicious" is disposition, not a gate (:660)
  church.temperance:                     # canon's own carve-out, not this suite's invention (:660)
    minister: {southern_einhir: open}
  guilds:                                 # v3, A-F10: was `guilds`; 07's roster spells it singular
    head:     {southern_einhir: {closed: {unless: "Precedent:guilds.marginal_trade_exception"}}}
    minister: {southern_einhir: {gated:  {predicate: "person holds Precedent:guilds.free_master_examination_passed"}}}
  niflhel:                               # v3, A-F10: 07 spells this presence `covert`; see §3.2.2a —
    governor: {northern_einhir: open, central_einhir: open, southern_einhir: open}   # :613, :666
  warden:
    minister:
      northern_einhir: {gated: {predicate: "gauge_band(person.thread_sensitivity) >= warden.northern_threshold"}}
      central_einhir:  {gated: {predicate: "gauge_band(person.thread_sensitivity) >= warden.central_threshold"}}
      southern_einhir: open                                                          # the favoured direction, :636/:667
  restoration_movement:                           # v3, A-F10: was `restoration_movement`
    minister:
      northern_einhir: {gated: {predicate: "person holds Precedent:rm.ideological_vetting"}}
      southern_einhir: open                                                          # the RM's base, :668
```

**Verdict grammar — three members, and the predicate reuses vocabulary that already exists** rather
than coining one:

```
caste_gate(institution, post_kind, caste) ::=
    open
  | gated:  {predicate: <same grammar as a form-transition gate, 01 §2.2 — over gauges, tags, form, identity>}
  | closed: {unless:    <same grammar>}
```

A `gated`/`closed` predicate is satisfied or not by reading state already on the board — never by a
roll performed *here*. Where canon's prose names a procedural cost ("+1 Ob on procedural grounds" for
the Guild examination, a Public Deed for Crown advancement), that cost belongs to **whatever module
resolves the examination or the deed** — out of this document's scope, likely a `09` project or a
contest elsewhere in the suite — and what `pm.candidates` checks is the **result**: a named
`Precedent` tag, or a gauge band already crossed. `caste_gate` never feeds `derive_ob`'s `modifiers`
argument and never appears in any `d_sigma` module's tag list. See §3.2.3.

#### 3.2.2a ⚠ Two institution-id vocabularies were about to land in ONE registry file (v3, A-F10)

`references/content_registry.yaml` is this suite's flagship registry and **two documents were keying
blocks in it on incompatible id sets:**

| this document's `caste_gate` keys | `07:296-303`'s `presence_kinds` ids |
|---|---|
| `crown` · `church` · `church.temperance` · `guilds` · `niflhel` · `warden` · `restoration_movement` | `church` · `guilds` · `restoration_movement` · `warden` · `military_order` · `covert` |

The moment both blocks land, **`institution_id` means two things inside one file** — three referents
spelled two ways (`guilds`/`guilds`, `restoration_movement`/`restoration_movement`, `niflhel`/`covert`) — and that
is exactly the disease `00:428-431` says this suite exists to stop. It is worse than the `standing`
collision `00 §7.1` records, because that one was two *scopes* and this is one field.

**The fix is one roster block that both readers key on**, and it needs no third file (`00 §9`'s two-file
ceiling holds). This document adopts the reconciled ids **in its own block above, unilaterally**, since
three of the four divergences are this document's spelling and `07`'s is the better one:

```yaml
# references/content_registry.yaml  §institutions — ONE roster; caste_gate and presence_kinds
# both key on `id` and neither declares its own list.
institutions:
  - {id: crown,             presence: false, cites: "faction_politics_v30.md:657"}   # sovereign, not a subnational presence
  - {id: church,            presence: true,  cites: "settlement_layer_v30.md §3.3 row 1"}
  - {id: church.temperance, parent: church,  presence: false, cites: "faction_politics_v30.md:660"}
  - {id: guilds,             presence: true,  cites: "settlement_layer_v30.md §3.3 row 2"}
  - {id: restoration_movement,       presence: true,  cites: "settlement_layer_v30.md §3.3 row 5"}
  - {id: warden,            presence: true,  cites: "settlement_layer_v30.md §3.3 row 6"}
  - {id: military_order,    presence: true,  cites: "settlement_layer_v30.md §3.3 row 4 (Löwenritter)"}
  - {id: niflhel,           presence: true,  covert: true,
     cites: "settlement_layer_v30.md §3.3 row 7; faction_politics_v30.md:613",
     note: "covert is a DISCLOSURE PROPERTY of this row (presence undisclosed until discovered,
            07 §4.5) — never a second institution id"}
```

**`covert` must be a property, not an id, and this is the load-bearing half of the fix.** It names *how
a presence is disclosed*, not *who is present*. Keyed as an id it (a) makes `07`'s covert row and `04`'s
caste row about the same institution unjoinable, and (b) makes a second covert institution unaddable
without a `covert_2`. As a boolean on the `niflhel` row, both problems vanish and `07 §4.5`'s
undisclosed-presence rule reads off the roster.

**Two contract changes this asks of documents this author does not own, stated as requests, not edits:**

1. **`07`** — `presence_kinds` becomes a *view* of the roster (rows with `presence: true`), and its
   `covert` id becomes `niflhel` carrying `covert: true`. Nothing in `07 §4.5`'s behaviour changes;
   only the key does.
2. **`00 §9`** — record the `institutions` roster as a **block inside the already-declared
   `content_registry.yaml`**, alongside `caste_gate` and `presence_kinds`. No new file, no new ceiling.

**Falsifier**, §11.1: every `institution_id` appearing in any block of `content_registry.yaml` resolves
to exactly one `institutions[].id`. It fails at load on the day the two vocabularies diverge again,
which is the only moment it can be caught cheaply.

**Six institutions populated, six left as rows to add.** Hafenmark, Varfell, Löwenritter, Riskbreakers,
Inquisitors and Templars carry the same shape (`:658-665` for the ones not already shown) and are
content-authoring work under the same registry, not a design question this document leaves open.

**Scope boundary, stated once.** `caste_gate` governs eligibility for a **Post** — a tier-node office
`pm.appoint` actually fills (Bishop's Delegate, Cardinal, Guild Comptroller, Warden-Captain, Dockslord).
It does **not** reproduce canon's internal Standing/rank ladders (Guild Apprentice→Free Master, Church
Catechumen→Canon, Warden Std 0→7) — those are prerequisite tracks a person climbs before ever
appearing as a post candidate, and they are `02`'s life-path/career-stage machinery (delta spec §3,
stage 4+ Career), not this document's. A `Precedent` tag named above (e.g.
`church.cardinal_or_confessor_sponsorship`) is exactly the kind of artifact a career stage would write.
**`02` owns where caste comes from — assigned at generation, stage 0 Origin, as identity (`01 §1.1`).
This document owns only what it gates.**

#### 3.2.3 Why the gate never touches a roll — a clarification of the delta spec's own wording

The delta spec's F, read literally, says the matrix resolves to `"open | gated(+Ob or +requirement) |
closed(unless <exception>)"`. Taken as "`pm.candidates` injects `+Ob` into a roll," that would
contradict the shape taxonomy directly: **`pm.candidates` is a `gate` — it filters the option set, it
never modifies a roll** (ED-IN-0201, `00 §5`; `00 §6` principle 4). This document resolves the tension
by reading "`+Ob`" as **a fact about which other module produced the satisfying `Precedent`** — the
Guild's own examination rolled at some Ob, somewhere else — never as a term this gate adds to a roll of
its own. `pm.candidates` performs zero rolls before and after this addition; the fifth row is a
presence/absence check, structurally identical to "not barred" one row above it.

### 3.3 Disclosure

*(v1 §3.2, extended.)* Eligibility is **published in full**: the player sees who qualifies and why, and
who was excluded and on which requirement. **v2, the one ruled exception (`00 §6` principle 5):** for a
candidate excluded by the caste row, disclosure names the **institution, post kind, caste and verdict**
in full — for `gated`, the unmet predicate; for `closed`, the named exception — never a bare
"ineligible." Concealing it would make the system's central injustice invisible, which is the opposite
of what canon's own asymmetry (§3.2.1) is for. What is still never published is the threshold at which
the *principal's preference* tips (§4.2) — that disclosure rule is unchanged.

---

## 4. `pm.appoint` — the principal chooses; the engine does not roll

```yaml
resolver: gate
budget: {gauge: post.budget, cost: 1}
```

*(v1, with one corrected write — O-04-1, and one added gate — §4.0.)* The principal **offers** the post
to one member of the candidate set; if the offer is accepted, four writes follow, the fourth
conditional:

0. **`accepts(candidate, post)`** — the appointee's own gate (§4.0, v3). **If it fails, none of the four
   writes below fires**: the post stays vacant, a `Precedent` lands on the refuser, and the principal
   has still spent the budget point.
1. `post_grant(post, person)` — `holder_id` set, `granted_season` stamped.
2. **Every passed-over candidate receives** `Grudge(owner_ref=(person, id), key=post_id,
   provenance=<the grant Key>)` — **unconditional given a grant**, regardless of what kind of edge exists
   between the candidate and the principal. *(v3: "given a grant" is the added clause. On a refusal nobody
   was passed over, because nobody was appointed — §4.0's ordering note.)*
3. **v2 correction (O-04-1).** *If* an edge already exists between the passed-over candidate and the
   principal's holder **and `01 §7.3` classifies it as PC↔NPC**, additionally deposit into
   `edge.disposition.pc_npc`. If the edge is NPC↔NPC, **no deposit is made** — disposition there is
   **derived** (`01 §7.3`, O-3), and depositing into it would be writing an aggregate, which the one
   write rule forbids (`01 §2.1`). The Grudge tag from write 2 is what durably carries the effect in
   that case; it is on the *person*, so it needs no edge to exist at all. If no edge yet exists between
   candidate and principal, the same applies: nothing is skipped except the (conditional) deposit.
4. The wrapper emits `post.granted` with the appointee as subject and the passed-over set in
   `targets[]`.

**Why this could not be left as v1 wrote it.** v1's write 2 deposited into "that person's
edge-disposition" unconditionally — correct for a stored gauge, wrong once `01` (O-3) made NPC↔NPC
disposition a derivation with no setter. This is exactly the read/write-asymmetry hazard `CLAUDE.md
§0.1` point 1 names: a primitive changed shape underneath a consumer that still wrote the old way.

### 4.0 `accepts:` — the appointee's own gate on `post_grant` (v3, T1-3)

**v2 shipped an appointment nobody could refuse.** `pm.appoint` was principal-chooses, end of story, and
the one place a person's preference function exists (§4.2) was run **exclusively by the chooser of them,
never by them.** Three consequences, and the third is the one that matters:

1. A person had no decision surface of their own. An unposted person was inert scenery.
2. The **courted-defection** arc family — the corpus's most duplicated shape — was unreachable. Courting
   someone is only a move if they can say no.
3. **A ratified arc shape failed outright.** An offer that cannot be declined is not an offer, and
   nothing else in the suite lets a person change sides deliberately.

**The fix adds zero objects and one gate**, and it is the *same* function §4.2 already specifies, read
from the other side. That symmetry is not a convenience — it is the argument that this is a gate and not
a new subsystem:

```
accepts(candidate, post) ⇔ preference(post → candidate) ≥ θ_accept(candidate)

preference(post → candidate) =
      Σ_conviction  candidate.weight[c] · principal_holder.weight[c]        # IDENTICAL term to §4.2's
                                                                            # first — a dot product is
                                                                            # symmetric, so it is the
                                                                            # same number, computed once
    + standing_margin(post, candidate)     # what the post offers against what they already hold —
                                           # §4.2's qualification_margin with the arguments swapped
    + clamp( disposition_value(candidate, principal_holder)
             + Σ tag_value(Debt or Grudge the candidate holds over the principal),
             ±RELATION_SHARE_MAX · structural_range )                        # relational, CAPPED
```

- **`θ_accept(candidate)` is what they already have, not a tuning constant.** A seated candidate's bar is
  the value of their current post under the same function; an **unposted** candidate's bar is the floor.
  So an unposted person accepts almost anything — which is right, and is also the first decision surface
  an unposted person has ever had in this suite.
- **`RELATION_SHARE_MAX` binds on both sides, and that is `01 §3.4` doing exactly its job.** Favour
  cannot buy an acceptance any more than it can buy an appointment. **Some offers must be refusable and
  unbuyable**, for the same reason `01 §3.4` gives: otherwise cultivation dissolves positional conflict.
- **Ordering, stated because it changes write 2.** The acceptance gate runs **before** any write. If the
  offer is refused, `post_grant` does not fire, **no passed-over `Grudge` is appended** (nobody was
  passed over — the post is still vacant), and the principal has spent their budget point. Offering down
  the list therefore costs one point per offer, which is what stops a principal walking the whole
  candidate set for free in one season.
- **On refusal, one write and no new Key type:** `Precedent(owner_ref=(candidate, id), key=post_id,
  provenance=<the `post.vacant` Key that raised the occasion>)`. A `post.refused` key type was drafted
  and **dropped**: `00 §8`'s P0-1 forbids appending a key type until `rendering_dispositions.yaml`
  exists, and the tag carries the fact without one. **This is a gate plus a tag append — leaves 3 and 2
  of `01 §2.1` — and nothing else.** The refusal is on the record, it travels with the person (§7), and
  it is readable by `pm.candidates`'s "not barred" row and by `06`'s bloc formation. **That tag is the
  story artifact**: the season the Ehrenwall heir refused the ministry is a fact the world remembers.
- **`caste_gate` is untouched.** It filters the set *before* the principal ranks it (§4.2), and
  acceptance runs *after* — three stages, no composition into one number.

**What this makes reachable that was not.** A person changes sides by *accepting* an offer from a rival
institution, or refuses their own and stays. Courting is a real investment because it moves the capped
relational term on the *acceptance* side. And an institution nobody will serve is now a reachable state
— `06 §7.2`'s dissolution gate reads it, and it is a better end than an institution with nobody left.

⚠ **The cost, named rather than hidden: a post can now go unfilled because everyone said no.** That is a
softlock only if nothing else moves; it is not, because `θ_accept` falls as a candidate's own position
worsens, an unposted candidate's bar is the floor, and `06 §7.2`'s Silent band is the designed
consequence rather than an accident. **The falsifier in §11.1 is written against exactly the softlock**,
and if it fires the fix is `θ_accept`'s floor, not removing the gate.

### 4.1 Why the grudge cannot ramp

*(v1, unchanged.)* Two bounds, both structural: the tag dedupes on `(person, Grudge, post_id)` and
refreshes in place; the magnitude lands in a Gauge with geometric decay, fixed point `rest + a/λ` for
every `λ > 0` (`01 §5.1`).

### 4.2 The principal's choice is the C2 decider

*(v1, unchanged in substance; one term renamed to survive O-3.)*

```
preference(candidate) = Σ_conviction  principal_holder.weight[c] · candidate.weight[c]   # structural
                      + qualification_margin(candidate, post)                            # structural
                      + clamp( disposition_value(principal_holder, candidate)
                               + Σ tag_value(Leverage or Debt over candidate),
                               ±RELATION_SHARE_MAX · structural_range )                   # relational, CAPPED
```

`disposition_value` replaces v1's bare `gauge_value(edge …)` — it reads the **stored** PC↔NPC gauge or
the **derived** NPC↔NPC value transparently (`01 §7.3`); the formula's caller does not need to know
which. **The relational cap is `01 §3.4` and it binds here hardest**: favour should tilt an appointment
between two plausible candidates; it should not put an unqualified one in office. Note that a
`caste_gate` verdict of `closed`/unsatisfied `gated` removes a candidate from the set *before*
`preference` ever runs over it — caste and favour act at different stages and never compose into one
number.

**Disclosure:** unchanged from v1 — each term of `preference` published as a band per candidate; the
resolved ordering's margin and the tie-break are not.

---

## 5. `pm.tenure` and `pm.audit` — the end of a term is the accounting

*(v1, unchanged.)* A post with `term = None` is held at pleasure and ends only by recall, death or
resignation. A post with a term expires at `granted_season + term`, and expiry triggers the audit.

### 5.1 `pm.audit` — the accumulated tags *are* the dossier

```yaml
resolver: d_sigma
```

| element | value |
|---|---|
| pool | the auditing post-holder's relevant attribute pair |
| obstacle | `derive_ob(holder.standing_value)` — E-1, `01 §6`, fractional, floor `OB_MIN` |
| modifiers | the post's and the holder's tags, entering as a **σ-space μ-shift** via `net_boost` |
| shape | **SO** — the audited party does not roll; their standing is the obstacle |

*(v1's reasoning carried verbatim: modifiers are σ-space, never obstacle-space, so a dossier is worth
the same probability wherever it lands — `01 §6` point 2 restates the identical argument for
`derive_ob`'s own `modifiers` argument, one level up.)*

### 5.2 The four outcomes, and all four are survivable

*(v1, unchanged.)*

| degree | outcome |
|---|---|
| Overwhelming | cleared with commendation — `standing` deposit up; a `Reputation` tag replaces the prior |
| Success | cleared — `standing` deposit up, smaller |
| Partial | censured — a `Precedent` tag naming the finding; standing unchanged |
| Failure | stripped — the post is revoked, `standing` deposit down, a `Precedent` tag recording the strip |

Total over the four bands, nothing unique to Partial (P0-3, `00 §8`). Failure removes a post, never a
person — tags travel, standing recovers geometrically, no attainder.

---

## 6. `pm.recall` — the guardrail is a provenance requirement, not a number

*(v1, unchanged.)*

> **A recall must cite a Tag.** `pm.recall` takes a `cause: tag_id` and refuses to run without one.

> **One outstanding involuntary post change per principal per season**, each successive one within the
> same term costing an escalating `standing` deposit from the principal's own holder.

### 6.1 Why both, and not just the second

*(v1, unchanged.)* The frequency cap alone bounds volume and says nothing about legitimacy; the
provenance requirement alone bounds legitimacy and says nothing about volume. Together they bound both
without a tuning pass.

---

## 7. `pm.succeed` — what survives a handover

*(v1, unchanged.)*

| carrier | disposition |
|---|---|
| tags on the **place** with `ttl=None` | survive. The place remembers |
| tags on the **place** with a ttl | swept normally |
| tags on the **person** | travel with the person, wherever they go next |
| the post's **budget** gauge | resets to its accrual baseline; unspent points do not carry |
| `Leverage` tags on the **post** (custody, §8) | survive the holder change — that is the point of custody |

---

## 8. `pm.custody` — controlling the holder without deposing them

*(v1, unchanged.)*

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
| on Overwhelming | as Success, `ttl=None` (durable), plus a deposit into the holder's `exposure` |
| on Partial | nothing gained; a `Precedent` tag on the actor records the attempt |
| on Failure | as Partial, plus a `Grudge` for the holder against the actor |

Custody is a tag, not a field (`01 §4.2`). While a `Leverage` tag naming actor A sits on post P, A's
preferences enter P's holder's `preference` function (§4.2) and P's remit selection (`05 §3`).

---

## 9. What the player actually touches at this layer

Per `00 §2.3.4`. The per-object test (`00 §2.3.5`): *could this be removed from the player's hands
entirely and still change the game?* Five of seven modules pass that test — they run the same whether
or not a human is watching (`01 §4.4`'s headless-post principle) and reach the player only as a
situation, not a chosen verb.

| what the player is asked to decide | which module | **what puts it in front of them** |
|---|---|---|
| whom to **offer** a post to, from a published, caste-annotated candidate list — and they may refuse (§4.0) | `pm.appoint` | a **Slate item**: the vacancy. `pm.vacancy` emits `post.vacant`, which is a `10` candidate |
| whether to recall a holder, citing a Tag | `pm.recall` | a **Slate item**: the *cause*. `pm.recall` refuses to run without a `cause: tag_id` (§6), so the arrival of the censure, Grudge or Precedent **is** the item — the guardrail and the Slate binding are the same rule |
| whether to attempt custody of a post they do not hold | `pm.custody` | a **Slate item**: the opening — a holder's `exposure` band, a `Leverage` opportunity, a bloc's interest in the post (`06 §3`) |

| what the player never operates directly | why |
|---|---|
| `pm.vacancy` | raised by state (`holder_id is None`), not invoked |
| `pm.candidates` | a filter feeding the appoint decision, not a decision itself — this is where `caste_gate` lives |
| `pm.tenure` | an accounting-boundary read of `granted_season + term` |
| `pm.audit` | fires at term expiry; the player experiences its verdict, not its invocation |
| `pm.succeed` | pure bookkeeping at handover |

**Three surface entries, five substrate.** The ratio required by `00 §2.3.4` ("if a document's surface
table is longer than its substrate table, the ratio is backwards") holds. **No new verb is added by
this document** — `caste_gate` is a registry term consulted inside an existing gate, not a fourth
appointment-adjacent action the player learns, and §4.0's acceptance gate is a *gate*, not a verb: it is
run by the appointee, who is usually not the player.

### 9.1 ⚠ What this document bills against the whole-game budget (v3, A-F9)

**The playing-surface budget is declared "hard" in `00 §2.2` and no document had summed it across the
suite.** A blind audit's count was `04` 3 + `05` 1 + `06` 1 + `08` 1 + `09` 1 + `12` 2 = **9, against a
single-digit budget with zero headroom.** This section states `04`'s share honestly and reduces it.

**Two things were wrong with v2's three rows, and both are fixed above rather than argued away.**

- **`00 §2.2` row 3 caps decisions per season at "the scene budget, and nothing else."** v2 wrote
  `pm.recall` and `pm.custody` as *"when the player chooses to spend budget"* — i.e. self-initiated, a
  menu the player browses, **outside the Slate and therefore outside the cap.** The table above routes
  all three through Slate items instead, which is what `01:346` already says happens to everything
  (*"filtered by the Slate to the scene budget"*). **This is accounting, not cutting** — no outcome is
  lost; what changes is that nothing here is reachable without an occasion.
- **`04` bills ONE entry against the verb budget, not three.** `05 part 2:40` already fuses all three
  into a single strategic action family — **`act.commission`: *"appoint, recall, or attempt custody —
  routes to `04`."*** At the surface the player learns one verb and answers whichever occasion arrived.
  ⚠ **This is a contract with `05`'s author, not a fact I can assert alone**: it holds only if there is
  no second, `04`-native menu entry beside `act.commission`. **If that fusion is rejected, `04` bills 3
  and the suite's sum is 9 with zero headroom** — in which case `00 §2.2` needs amending explicitly, and
  the right place to do it is `00`, not here.

**What is still open and belongs to `00`/`13`, not to this document:** whether the whole-game budget is
9 or 6–7 is **undecidable from the documents**, because `00 §2.2` names "a single digit" and no document
enumerates the set. Each document audits its own count; **none audits the row the fan-out breaks.** That
is a suite-level finding raised here because this is the document with the largest single share.

---

## 10. Module contracts

`class:` is new (`00 §7`); `form:`/`transitions:` are new and empty on every row below — none of
`pm.*`'s writes touch an entity's `form` bucket (Post grant/revoke is leaf 3, not leaf 4).

```yaml
- module: pm.vacancy
  parent: personnel               class: substrate
  scales: [settlement, territory, peninsula]        tier: null
  resolver: gate
  remit: []                                  # raised by state, not invoked
  budget: null
  consumes:
    - {type: post.revoked, from: [pm.recall, pm.tenure, pm.audit]}
  emits: [{type: post.vacant, terminal: false}]
  state: [{name: post, bucket: post, writable: true, owner: substrate.post}]
  form: []      transitions: []
  disclosure: [{of: post, inputs: published, presentation: exact, trigger: hidden}]

- module: pm.candidates
  parent: personnel               class: substrate
  scales: [settlement, territory]                   tier: null
  resolver: gate
  remit: [head, governor, minister]
  budget: null
  consumes: [{type: post.vacant, from: [pm.vacancy]}]
  emits: []
  state: []
  form: []      transitions: []
  # NOTE: additionally reads references/content_registry.yaml's caste_gate block (§3.2) — a
  # registry read, not a Key, so it is correctly absent from `consumes:`.
  disclosure:
    - {of: candidate_set, inputs: published, presentation: exact, trigger: hidden}
    - {of: caste_gate_verdict, inputs: published, presentation: exact, trigger: hidden}   # v2, §3.3

- module: pm.appoint
  parent: personnel               class: surface                 # 00 §2.1's own worked example
  scales: [settlement, territory, peninsula]        tier: null
  resolver: gate
  remit: [head, minister]
  budget: {gauge: post.budget, cost: 1}           # spent on the OFFER, whether or not it is accepted (§4.0)
  consumes: [{type: post.vacant, from: [pm.vacancy]}]   # v3, A-F9: the vacancy is the Slate item; not self-initiated
  emits: [{type: post.granted, terminal: false}]   # on acceptance ONLY
  # v3, T1-3: a refusal appends a Precedent tag and emits NOTHING NEW. A `post.refused` key type was
  # drafted and dropped: P0-1 (00 §8) forbids appending a key type until
  # references/rendering_dispositions.yaml exists, and the tag carries the fact without one. The tag's
  # provenance is the `post.vacant` Key that raised the occasion, which already exists.
  state:
    - {name: post, bucket: post, writable: true, owner: substrate.post}
    - {name: tag, bucket: tag, writable: true, owner: substrate.ledger}
    - {name: edge.disposition.pc_npc, bucket: gauge, writable: true, owner: substrate.edge}   # O-04-1: conditional
  form: []      transitions: []
  # v3, T1-3: `accepts` is a GATE on post_grant, run by the appointee (§4.0). It adds no state row —
  # it reads the same terms §4.2 already reads and writes only a Precedent tag on refusal.
  disclosure:
    - {of: preference, inputs: published, presentation: band, trigger: hidden}
    - {of: accepts,    inputs: published, presentation: band, trigger: hidden}   # the candidate's own bar is a band, never a number

- module: pm.tenure
  parent: personnel               class: substrate
  scales: [settlement, territory]                   tier: null
  resolver: gate
  remit: []
  budget: null
  consumes: []
  emits: [{type: post.revoked, terminal: false}]
  state: [{name: post, bucket: post, writable: true, owner: substrate.post}]
  form: []      transitions: []
  disclosure: [{of: post.term, inputs: published, presentation: exact, trigger: hidden}]

- module: pm.audit
  parent: personnel               class: substrate               # fires at term expiry, not invoked
  scales: [settlement, territory]                   tier: null
  resolver: d_sigma
  remit: [head, minister]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  emits: [{type: post.revoked, terminal: false}]     # on Failure only
  state:
    - {name: standing, bucket: gauge, writable: true, owner: substrate.gauge}
    - {name: tag, bucket: tag, writable: true, owner: substrate.ledger}
  form: []      transitions: []
  disclosure: [{of: standing, inputs: published, presentation: band, trigger: hidden}]

- module: pm.recall
  parent: personnel               class: surface
  scales: [settlement, territory]                   tier: null
  resolver: gate
  remit: [head, minister]
  budget: {gauge: post.budget, cost: 1}
  consumes: []      # v3, A-F9: reached through a Slate item raised by its `cause` tag (§6, §9) —
                    # the cause is a Tag, not a Key, so it is correctly absent from `consumes:`
  emits: [{type: post.revoked, terminal: false}]
  state:
    - {name: post, bucket: post, writable: true, owner: substrate.post}
    - {name: standing, bucket: gauge, writable: true, owner: substrate.gauge}
  form: []      transitions: []
  disclosure: [{of: recall_cause, inputs: published, presentation: exact, trigger: hidden}]

- module: pm.custody
  parent: personnel               class: surface
  scales: [settlement, territory, peninsula]        tier: null
  resolver: d_sigma
  remit: [head, minister, envoy, clerk]
  budget: {gauge: post.budget, cost: 1}
  consumes: []
  emits: []
  state:
    - {name: tag, bucket: tag, writable: true, owner: substrate.ledger}
    - {name: exposure, bucket: gauge, writable: true, owner: substrate.gauge}
  form: []      transitions: []
  disclosure: [{of: exposure, inputs: published, presentation: band, trigger: hidden}]
```

*(v1's closing note, unchanged: `pm.custody`'s remit includes `clerk` — no vote, no title, no
holdings, and still able to acquire leverage over a post. That remains the best available answer to
"why would a player care about a clerkship," and it costs nothing but a remit row.)*

---

## 11. Property audit

### 11.0 ⚠ Scope, corrected in v3 (A-F11) — this table graded modules that do not roll

**v2 gave a single five-row NERS pass over the whole document, and its reasoning for three of the five
rows cited non-rolling gates.** That is the methodology's own named error: a resolution-scoped property
audit measures *rolls*, and manufacturing a verdict for a threshold is how a document acquires grades it
did not earn. The scope note above it said the right thing (*"diagnosed on P-iii and P-v only, no N/R/S/E
verdict offered"*) and **the table then contradicted it.** v3 splits the two rather than restating the
note.

**Two of seven modules roll: `pm.audit` and `pm.custody` (both `d_sigma`).** They get the five-property
audit. **The other five — `pm.vacancy`, `pm.candidates`, `pm.appoint`, `pm.tenure`, `pm.recall` — are
gates**, and `pm.appoint` gained a second gate in v3 (§4.0). They get the loops-and-gates audit `06 §9`
uses for the same reason, because that is the instrument that fits.

#### 11.0a The two rolling modules — five properties, honestly scoped

| property | verdict | scope: `pm.audit`, `pm.custody` only |
|---|---|---|
| **P-i** legible odds | pass | Pool is the actor's own attribute pair; obstacle is `derive_ob(target)`, both published (§5.1, §8). The audit's dossier terms are published per tag |
| **P-ii** uniform leverage | pass | Tag weight enters through `net_boost`, never as a flat obstacle shift, so a dossier is worth the same probability wherever it lands |
| **P-iii** bounded, monotonic | pass | `derive_ob`'s floor prevents a cliff. `exposure` and `standing` are geometric-decay gauges bounded at `rest + a/λ` (`01 §5.1`) |
| **P-iv** graded, recoverable | pass | Four audit outcomes, total over the bands, nothing unique to Partial (P0-3). The worst removes a post, never a person; custody's Partial and Failure both leave the actor in play with a tag |
| **P-v** right engine | pass | An audit is genuinely uncertain judgement over accumulated evidence; custody is a contested attempt against a resisting holder. Both are the case `d_sigma` exists for |

#### 11.0b The five gate modules — loops, gates and what each reads

**No N/R/S/E verdict is offered for any row below**, and that is a refusal, not an omission.

| gate | reads | fails to | bounded by |
|---|---|---|---|
| `pm.vacancy` | `post.holder_id is None` | nothing is emitted | not a loop — a state read |
| `pm.candidates` | presence, qualification, standing band, bar tags, `caste_gate` (§3.2) | an **empty set** — a reachable, designed state that `06 §7.2` reads | the caste matrix is a **finite table**, bounded by construction, not by tuning |
| `pm.appoint` — principal's choice | `preference` (§4.2), capped by `RELATION_SHARE_MAX` | the post stays vacant | `01 §3.4`'s cap; the Grudge cannot ramp (§4.1) |
| `pm.appoint` — **`accepts`** *(v3)* | `preference` from the candidate's side, `θ_accept` (§4.0) | **refusal** — a Precedent tag, the post stays vacant | the same cap, on the other side. ⚠ **The loop to watch is offer → refusal → offer:** each offer costs a budget point, which bounds it *within* a season; **across** seasons it is bounded only by `θ_accept` falling as a candidate's position worsens, and that is **unmeasured** |
| `pm.tenure` | `granted_season + term` | no expiry | a clock, not a loop |
| `pm.recall` | a cited `cause: tag_id`, one outstanding per principal per season | refuses to run with no cause | the frequency cap **and** the escalating `standing` deposit (§6.1) — the pair bounds volume and legitimacy together |

**The honest limit above all of it**, per `00 §0.1`: a resolution-scoped audit cannot ask whether a
design expresses the game. This document could pass everything here and still be the wrong model of an
appointment. The instrument for that is the elegance criterion, and its answers are §3.2's argument for
keeping the caste matrix, §4.0's statement of what was unreachable without an acceptance gate, and
§9.1's honest bill against the playing-surface budget.

### 11.1 Falsifiers — per `CLAUDE.md §0.1` point 3, each named against what it is load-bearing on

| claim | falsifier | load-bearing on |
|---|---|---|
| the caste gate never modifies a roll | a grep-based test asserting no call site passes `caste_gate` (or any of its predicates) into `derive_ob`'s `modifiers` argument or into any `d_sigma` module's tag/modifier list | the difference between a gate that filters who is considered and a tax charged for existing — the exact failure mode the shape taxonomy exists to prevent |
| caste exclusion is disclosed in full, never as a bare boolean | a test that for every candidate the caste row excludes, the `pm.candidates` disclosure record carries institution, post_kind, caste and (for `gated`) the unmet predicate or (for `closed`) the named exception | `00 §6` principle 5's ruled exception — concealing it would make the game's central injustice invisible, which is design intent, not an omission |
| O-04-1's write fix holds | a write-sweep test (`CLAUDE.md §0.1` point 1's `_CELL_OWNED`-style registry) asserting `pm.appoint` never calls `gauge_deposit` on a disposition gauge for a pair `01 §7.3` classifies NPC↔NPC | the same read/write-asymmetry class that motivated `01`'s own O-3 — a primitive changed shape and this is the one caller that had to change with it |
| the grudge cannot ramp | *(v1, carried)* dedupe on `(person, Grudge, post_id)` plus geometric decay's fixed point `rest + a/λ` | an unbounded selection-feedback loop, the documented failure class §4.1 closes |
| **a person can refuse a post** (§4.0, T1-3) | a test that constructs a candidate whose `preference(post → candidate)` falls below `θ_accept` and asserts `post_grant` does **not** fire, the post stays vacant, the principal's budget point is spent, **no passed-over Grudge is appended**, and a `Precedent` lands on the candidate. **Plus the softlock probe:** across a seeded campaign, assert no post stays vacant for more than `DISSOLVE_DWELL` seasons *purely* through refusal while a floor-bar unposted candidate exists | ratified arc shape 8 and the courted-defection family — the register's most duplicated arc, unreachable in v2 |
| **acceptance is capped like everything else** (§4.0) | a test that `RELATION_SHARE_MAX` bounds the relational term of `preference(post → candidate)` at the same fraction it bounds `preference(candidate)` — favour must not be able to *buy* an acceptance it cannot buy an appointment with | `01 §3.4`: some offers must be refusable and unbuyable, or cultivation dissolves positional conflict |
| **one institution vocabulary** (§3.2.2a, A-F10) | a load-time test that every `institution_id` in every block of `references/content_registry.yaml` — `caste_gate`, `presence_kinds`, and any later block — resolves to exactly one `institutions[].id`; and that `covert` appears only as a **property**, never as an id | the suite's flagship registry meaning one thing. It fails on the day the two vocabularies diverge again, which is the only cheap moment to catch it |
| **nothing here is self-initiated** (§9, A-F9) | a test that every `04` module classed `surface` is reachable **only** through a Slate item — `pm.appoint` from `post.vacant`, `pm.recall` from its cited cause tag, `pm.custody` from a published opening — and that none appears in a browsable menu | `00 §2.2` row 3: *"decisions per season = the scene budget, and nothing else."* v2's recall and custody were outside it |
| the relational cap holds against caste-favoured candidates too | a test that `RELATION_SHARE_MAX` still bounds `preference`'s relational term even when the candidate set has already been caste-filtered to a smaller pool — a smaller pool must not let favour buy more of the ordering than the cap allows | `01 §3.4`'s reachability bar, restated at the point where a caste-favoured institution (Niflhel, Warden) could otherwise let a thin candidate list make favour decisive by default rather than by cap |

**Necessary** — the caste term is one row in an existing conjunction, and v3's acceptance gate is one
predicate over a function that already existed; **neither adds a module, a resolver kind, a Key type or
a write leaf.** **Robust** — the two failure directions the corpus measured (an
unbounded grudge, a caste term that leaks into a roll) are both closed structurally, the second by
construction rather than by discipline. **Smooth** — one gate, one `derive_ob`, one disclosure
contract, unchanged from v1; the caste row uses the *same* predicate grammar `01 §2.2` already defined
for form transitions, coining nothing. **Elegant** — the honest deduction, stated once rather than
buried: **the institution-level key (§3.2.2) is a necessary refinement of `00 §9`'s stated registry
shape, not an addition to it** — the alternative (following `00 §9` literally) would have been unable
to express the one asymmetry this document was explicitly told to preserve.
