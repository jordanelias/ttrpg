# KEYS_AUDIT — RUNNER 4 of 5, axis: IDENTITY AND ADDRESSING

**Target:** `scratchpad/v2/ARCH_CORE.md` (189 lines), cited below as `ARCH_CORE:NN`.
**Question this runner answers, and only this one:** is every object in ARCH_CORE nameable, addressable
and referable, and does every input and output carry a declared type?
**Not this runner's job:** whether the architecture is a good idea (correctness runner), whether it
faithfully renders its sources (fidelity runner), whether its factual assertions hold (factuality
runner), whether it stayed inside its remit (scope runner). Where a finding here *looks* like a merit
critique it is stated as a naming/typing consequence and nothing more.

**Method.** Every ARCH_CORE object was resolved against the four surfaces that already own identity in
this tree: the executable Key substrate (`engine/substrate/keys.py`), the descriptor registry
(`references/descriptor_registry.yaml`), the name index (`references/names_index.yaml`), and the prior
design's own inventory (`proposals/_session_provenance/2026-08-31-fable5-review/CODE_SHAPE_ABSTRACT.md`,
cited `ABS:NN`) plus its terminal source (`proposals/2026-08-31-ideal/10_SUPERSEDING.md`, cited `SUP:NN`).

---

## 0 · THE HEADLINE, BEFORE THE TABLES

**ARCH_CORE declares zero identifier fields.** Across eleven record definitions
(`ARCH_CORE:35, 36, 37, 49, 75, 76`, plus the inherited `Claim`, `Proposition`, `Case`, `Ground`,
`Event`), not one field is an id, a handle, a name, or a key. Every reference in the document is
therefore a reference to *something the document has not said how to name*.

This is not a stylistic gap, because the design it inherits **consumes ids it never mints**:

| id consumed | consumer | where |
|---|---|---|
| `event_id` | `Claim.source = firsthand(event_id)` | `SUP:243` |
| `event_id` (reused, deliberately) | knot deposit shares the originating event's token | `SUP:245-246` |
| `claim_id…` | `Claim.source = inferred(claim_id…)` | `SUP:243` |
| `claim_ids` | `stance[referent].provenance` | `ABS:73` (S02:226-227) |
| `claim ids` | `Ground.support[]` | `SUP:1516` |
| `act-id` | conflict tiebreak `hash(act-id, world-seed)` | `SUP:692`, restated without the id at `ARCH_CORE:89-90` |
| `actor_id`, `target_id` | determinism substream | `ABS:354` (S10:174); generalised at `ARCH_CORE:181` to `subject_id` |
| `handle` | `Claim.source = told_by(person, handle)` | `SUP:243` |

Eight id-shaped things are read. Zero are declared. The executable substrate in this repo does the
opposite and is the precedent to copy: `Key.id: str` (`engine/substrate/keys.py:145`), uniqueness
enforced as invariant 1 (`keys.py:379-381`), referential integrity enforced as invariant 3 — a `causes`
entry that names an unknown id **raises** (`keys.py:384-388`) — and lookup by id is a first-class
operation (`keys.py:364-365`). Type ids are themselves shape-constrained by a regex,
`[a-z_]+\.[a-z_]+` (`keys.py:399`), and the descriptor registry uses the same dotted form for every
quantity it owns (`references/descriptor_registry.yaml:49-58`, e.g. `attr.body.strength`).

**So the compendium's first job is not to document ARCH_CORE's identities. It is to record that there
are none, and to say what the eight consumers above require.**

---

# A · THE KEY / IDENTITY AUDIT

Columns: **ident** = what identifies the object, as ARCH_CORE actually states it (never inferred —
"—" means unspecified). **stable/season** = does that identifier survive one season unchanged.
**addressable** = can another object hold a reference to it. **claim/stance** = can it appear as a
`Claim.subject` (open referent space, `SUP:229-234`) and/or as a stance referent (CLOSED 4-kind set
`Person | Faction | Proposition | Place`, `ABS:188` / S02:227).

## A.1 The three carriers

| object | defined | ident | stable/season | addressable | claim / stance |
|---|---|---|---|---|---|
| **Person** | `ARCH_CORE:35` | **—**. Six fields, none an id. `address` is the only candidate and it is a *path* (`SUP:98`), not a name | **NO** — `migrate` and `secede` destroy the `contain` edge (`ARCH_CORE:61`), so the path changes mid-season; `admit`/`annex` change it from outside | as `Tenure.subject`/`object` (`ARCH_CORE:50-51`), `Act.actor` (`ARCH_CORE:75`), `witness`'s first argument (`ARCH_CORE:116`) — all by an unnamed reference | claim: yes by precedent (`SAID(Aldwin, …)`, `SUP:243`). stance: yes, kind `Person` |
| **Node** | `ARCH_CORE:36` | **—**. `kind` is a class, not an identity; the enum is not given anywhere in ARCH_CORE (the ladder is at `SUP:96`) | position is stable, but a Node's *position* is its own `contain` edge, so identity is defined by the very edge whose integrity §B questions | yes — `Tenure` subject and object, `Office.node?`, `norm(n, prop)`, `condition(n)`, `principals(f, n)` | claim: unstated. stance: only if `Node` ⊆ `Place`, which **ARCH_CORE never says** |
| **Office** | `ARCH_CORE:37` | **—**. Best available is `(post, node?)`, and `node` is explicitly optional | `post` and `node` are both writable (conferral/annexation) | yes — `hold` object (`ARCH_CORE:59`), `mint`/`efface` target (`ARCH_CORE:80-81`) | claim: unstated. stance: **NOT a referent kind** — an office is not Person/Faction/Proposition/Place |

**Finding A-1 (rank 1).** `(post, node?)` is not a key when `node` is null, and null is exactly the
**office-cluster** case that `SUP:850-853` introduced and that `ARCH_CORE:37`'s `node?` exists to
support. The one object with the weakest identity is the object at the centre of S19 — the rootless
vacant office — which `ARCH_CORE:187` carries forward as open. Two rootless offices with the same
`post` are indistinguishable, so a petition addressed to one is addressed to both or to neither.

**Finding A-2.** `ARCH_CORE:37`'s Office **drops `revocation` and `seat_items`** from the nine-field
form at `SUP:416`. `seat_items` is not decoration: it is one of the two capacity denominators
(`SUP:390-412`), it is what `carry` spends (`ABS:405`), and rule C2 states *"the cap on live conditions
is `seat_items(office)`"* (`ABS:474`). A quantity three procedures address by name is no longer a field
of the record they address it on. (Fidelity runner owns *why* it was dropped; this runner records that
the name now resolves to nothing.)

## A.2 Non-carriers that are nonetheless addressed

| object | defined | ident | stable/season | addressable | claim / stance |
|---|---|---|---|---|---|
| **Site** | `ARCH_CORE:39` — "matter held by a Node" | **—** | condition is written every season (`SUP:1333-1334`); identity unstated | **required to be** — `Tenure.object` (`ARCH_CORE:51`), `hold` object (`ARCH_CORE:59`), `mint`/`efface` target (`ARCH_CORE:80-81`), second element of `occupation(p)` (`ARCH_CORE:106`), `investigate`'s target (`ARCH_CORE:154`) | claim: needed for §4.4's purge limb; stance: only via `Place`, unstated |
| **Faction** | `ARCH_CORE:42-44` — deleted as a carrier | **the Proposition's identity** | see A-4 | not directly; only through its Proposition | stance: kind `Faction` **still exists in the closed set** (`ABS:188`) with no object behind it |
| **Proposition** | `SUP:1514` — not restated in ARCH_CORE | **—**; structural equality over `(mood, subject, predicate, value, when, scope)` | `when` and `scope` are intervals | yes, as `commit` object and `norm`/`estimated_profile` argument | stance: yes, kind `Proposition` |
| **Claim** | `SUP:221`; touched at `ARCH_CORE:83, 148-149` | **—**; `inferred(claim_id…)` proves an id is required (`SUP:243`) | ledger-local; evicted at M2 (`ARCH_CORE:168`) | addressed as `(ledger owner, claim id)` — a two-part address ARCH_CORE never states | claim: **yes and this is load-bearest** — `SAID(Aldwin, C, season 12)` (`SUP:243`) |
| **Event** | **nowhere in ARCH_CORE**; only as `resolve`'s output and `witness`'s input (`ARCH_CORE:115-116`) | **—** | — | `firsthand(event_id)` requires one (`SUP:243`) and the knot rule requires *the same* one (`SUP:245-246`) | claim: as `source` payload only |
| **View** | `ARCH_CORE:114` | value, per person per tick | — | must be a distinct type from `World` with no coercion (`SUP:153-154`) — not restated in ARCH_CORE | not an object |
| **Sensation** | `ARCH_CORE:118-123` | value; **declared reference-free** | recomputed at B2/M1 | deliberately **not** addressable | **deliberately un-nameable** — see A-6 |
| **Act** | `ARCH_CORE:75` | **—**; `SUP:692` hashes an `act-id` that no record carries | — | `touches[]` entries address objects, nothing addresses an Act | claim: unstated |
| **Tenure** | `ARCH_CORE:49` | **—**; plausibly `(subject, object, kind)`, never stated | see A-3 | **nothing addresses a Tenure** | see A-3 |

**Finding A-3 (rank 1 — the single most serious).** **The `Tenure` is the one record the epistemic
layer most needs to talk about, and it is the one record with no identity at all.**
"Aldwin holds the praefecture", "Mereth is sworn to the Restoration", "the Row seceded" — every
disputable political fact in this design is a `Tenure`. Under `SUP:368` that was defensible, because
*"who holds the praefecture is a query, not a field"* and a query result is not a thing you can name.
`ARCH_CORE:49` **converts it into a record** and does not give the record a name, so the design has
taken the step that makes the fact nameable and stopped one field short of naming it. Consequences
that are pure addressing, not merit:
- A claim about a Tenure must be phrased as a claim about its endpoints, which loses `since`, `degree`
  and `conferrer` — precisely the fields a succession dispute is about.
- `Tenure` carries `since` and **no `until` and no id** (`ARCH_CORE:49`), so a destroyed Tenure leaves
  no record. Re-conferral after revocation is indistinguishable from an unbroken tenure. That breaks
  `entrenchment(h, H) = min(1, seasons_held(h, H) / 60)`, which `ABS:555` says is *"read off transfer
  events, stored nowhere"* — with no id there is nothing on the event to read off.
- `avowed?` (`ARCH_CORE:49`) is written as an optional flag; the inherited domain is a **three-valued**
  enum `avowed · private · covert` (`ABS:239-240`). A boolean-shaped field cannot carry three states.
- `degree?` and `avowed?` are optional *globally* but are required for `commit` and meaningless for
  `contain`/`succeed`. Optionality here is per-kind and the tuple does not say so.
- `conferrer`'s type is unstated. For `hold` it is a Person (or a Person acting by remit — different
  thing). For `contain` created by `annex` it is unstated. For `tie` created by co-presence
  (`ARCH_CORE:63`) there is no conferrer at all, and no null is declared.

**Finding A-4 (rank 2).** **Deleting the Faction object moves faction identity onto value-equality over
a six-tuple with two interval fields.** `ARCH_CORE:42-43` makes a faction *"a Proposition plus the set
of Tenures of kind `commit` pointing at it"*, and `SUP:1514` gives `Proposition = (mood, subject,
predicate, value, when, scope)`. Two persons who commit to propositions differing only in `scope`
belong to two different factions; two who commit to textually identical propositions belong to one.
Nothing in ARCH_CORE says whether Propositions are interned (one canonical record, referenced) or
compared structurally. **`SUP:132-133` refuses merge, split, promote and found-at-size as operations —
under `ARCH_CORE:42` they return as an equality question, and no object owns that question.** This is
addressing, not merit: `commit`'s object field needs a Proposition *reference*, and the document has
not said what a Proposition reference is.

**Finding A-5.** The stance referent set is a **closed** four-kind enum (`ABS:188`). After
`ARCH_CORE:42` deletes Faction, kind `Faction` and kind `Proposition` denote the same thing, so the
closed set has a redundant member and every stance row keyed on a Faction now keys on a Proposition.
Meanwhile `Node`, `Office`, `Site`, `Tenure`, `Act` and `Event` are **not** referent kinds — so:
- you cannot hold an attitude toward an **office** (only toward its holder or its proposition);
- you cannot hold an attitude toward a **site** unless `Place` is defined to cover Sites and Nodes,
  which ARCH_CORE never does — and `Place` is defined nowhere in ARCH_CORE or `SUP`;
- `SUP:1941-1944` already records that a *procedure* is not a referent kind while a canon body is made
  of one. ARCH_CORE adds five more object kinds to that gap without widening the set.

**Finding A-6 (recorded, not a defect).** `Sensation` is the one new object whose identity story is
coherent, **because it is declared reference-free**: *"a closed record of exactly the four need
scalars … carrying no references and answering no query"* (`ARCH_CORE:120-122`). The consequence must
be written down rather than discovered later: **a Sensation is un-nameable, therefore undisputable.**
No person can hold a claim about another person's hunger. Claims can only reach the *larder* (matter on
a Node) and the *body*. Two smaller problems inside it:
- the record is called **closed** and **its four members are not enumerated** in ARCH_CORE. They are
  `subsistence · standing · commitment · exposure` at `SUP:185-190` (`ABS:208-215`). A closed record
  whose membership is stated only by cardinality is not closed to a reader.
- two of the four read **the world** and two read **the view** (`SUP:185-190`). Sensation merges both
  provenances into one flat record with no field marking which is which, so `choose` cannot tell a
  world-sourced scalar from a view-sourced one — and the distinction is the whole point of the A5 fix
  it is answering (`proposals/2026-08-31-ideal/20_FABLE5_ADVERSARIAL_REVIEW.md:552-556`).

## A.3 The six `Tenure` kinds

`ARCH_CORE:52` enumerates **six** kinds; the table at `ARCH_CORE:57-63` has **five rows** because
`tie` and `knot` share one. A compendium must state both numbers or a reader counts wrong.

| kind | row | direction | cardinality declared? | identity of one instance | destroyed by |
|---|---|---|---|---|---|
| `hold` | `ARCH_CORE:59` | Person → Office \| Site \| Node | **no** — may one Person hold one Office twice? may two Persons hold one Office? | `(person, object)` at best | `revoke` |
| `commit` | `ARCH_CORE:60` | Person → Proposition | implied single per (person, proposition) by "degree → 0" | `(person, proposition)` | degree → 0 |
| `contain` | `ARCH_CORE:61` | Node → Node, Person → Node | **YES — single-parent for Persons** (`ARCH_CORE:69`) | `(subject)` if single-parent holds | `secede`, `migrate` |
| `succeed` | `ARCH_CORE:62` | **Node → Person** (the only kind pointing this way) | **NO** — called a "pointer", so single-valued per Node, and never declared as an invariant the way `contain` is | `(node)` if single-valued | re-naming |
| `tie` | `ARCH_CORE:63` | Person → Person | **no** — and a tie is symmetric (`ABS:76`, S02:326) while the record is directed | one record or two? unstated | decay |
| `knot` | `ARCH_CORE:63` | Person → Person | **no** — explicitly *bidirectional* (`ABS:77`, S02:351) | as above | rupture |

**Finding A-7 (rank 2).** **`knot` has two state fields with no home in the Tenure tuple.** A Knot
carries `depth ∈ {1, 2}` and **one shared `strain` gauge** (`ABS:77`, S02:351-352); `bandwidth(k) =
max(0, 2 − floor(strain / 3))` reads that gauge every season (`ABS:502`). `Tenure`'s optional fields
are `degree?` and `avowed?` (`ARCH_CORE:49`) — neither is `depth` and neither is `strain`. A *shared*
gauge on a *directed* record also has no owner: if the edge is stored twice, `strain` is stored twice
and can disagree with itself. Same problem, smaller, for `tie`'s `(familiarity, last_contact,
channel_class)` (`ABS:76`).

**Finding A-8.** `ARCH_CORE:69-70` says single-parent containment is *"enforced as an invariant on the
edge kind, not by a separate tree structure"*. **An invariant on an edge kind is a cardinality
constraint, and a cardinality constraint needs a key to be checkable.** With no id on `Tenure` and no
declared uniqueness over `(subject, kind)`, "single-parent" is a sentence, not a check. §B walks what
breaks when it is violated.

## A.4 The five `touches` modes

`ARCH_CORE:77` — `mode ∈ read | alter | exclude | mint | efface`. Five, extending `SUP:689`'s three.

| mode | `touches` object is… | declared? | identity problem |
|---|---|---|---|
| `read` | an existing object | reference | none |
| `alter` | an existing object | reference | **the object is not enough** — see A-9 |
| `exclude` | an existing object | reference | none |
| `mint` | **an object that does not exist yet** | reference — **impossible** | see A-10 |
| `efface` | an existing object, about to stop existing | reference | dangling — see §B |

**Finding A-9 (rank 3).** **The conflict rule quantifies over a FIELD; the record quantifies over an
OBJECT.** `ARCH_CORE:86-90` declares commutativity *per-field* (`additive` vs `exclusive`) and states
the rule as *"two acts conflict iff they share an object and either mode is `exclude`/`efface`, or both
`alter` an `exclusive` field"*. But `touches := (object, mode)` (`ARCH_CORE:76`) carries no field. The
rule as written is **not computable from the declared record**. `touches` needs a third element —
`(object, mode, field?)` — or the field must be recoverable from `verb`, which is itself untyped
(D-3 below). This is the cleanest pure-typing defect in the document.

**Finding A-10 (rank 1).** **`mint` is given the same tuple shape as `read`, and it cannot have one.**
`touches := (object, mode)` addresses an existing object. A `mint` act has no object to address: the
Person, Node, Office, Site or Proposition (`ARCH_CORE:79-81`) does not exist until the act resolves.
What a `mint` entry must carry is a **type plus a specification plus an output binding** — "make a Node
of kind Hearth, contained in N, and let the resulting id be available to the rest of this act". Three
downstream consequences, all addressing:
- **`mint` acts cannot conflict.** The rule at `ARCH_CORE:89-90` conflicts on a *shared object*; two
  `mint` acts share no object because neither has one. Two settlements can be founded at the same
  place in the same season and the resolver cannot see it.
- **A minted object's id has no source.** Nothing in ARCH_CORE says who names a new Person, Node,
  Office, Site or Proposition, or whether the name is deterministic. `ARCH_CORE:181`'s substream is
  keyed on `subject_id` — for a birth there is no subject id yet, which is exactly the case that
  generalisation was introduced to cover (`ARCH_CORE:182`, P1's actorless rolls).
- **`ARCH_CORE:128` mints a practice RANK** — *"`mint` on a practice rank"*. A rank is a scalar field
  of a `Practice` tuple (`ABS:72`, S02:153), not an object. Either `mint` also operates on fields (in
  which case it overlaps `alter` and the conflict rule has to say which wins) or `ARCH_CORE:128` is
  using the word loosely. Both readings are available to a cold reader; that is the failure
  `CLAUDE.md` §4 calls non-idempotent meaning.

## A.5 The nine Derived

Full signatures are in §C. Identity-relevant findings only, here:

- **`faction(p)`** (`ARCH_CORE:99`) — the parameter is named `p` (the document's letter for Person
  everywhere else: `ARCH_CORE:105, 106, 107`) and the signature says `Proposition → …`. A name/type
  disagreement inside one row.
- **`principals(f, n)`** (`ARCH_CORE:100`) — `f` names a Proposition. Same slip, and this is the row
  that carries *"Deposition = this returning someone else"*, i.e. the row an entire political
  mechanism hangs on.
- **`presence/density/footprint`** (`ARCH_CORE:101`) — three functions given **one** signature.
  `footprint(f)` takes one argument at `SUP:116`; the row says `(Proposition, Node) → scalar` for all
  three. A compendium cannot copy this row; it has to split it.
- **`sovereign_fraction(root)`** (`ARCH_CORE:102`) — **`root` is a distinguished Node that the document
  never declares.** ARCH_CORE has no root, no realm constant, and no statement that the containment
  forest has exactly one root. A parameter whose only occurrence is in a signature.
- **`condition(n)`** (`ARCH_CORE:103`) vs **`condition(site)`** (`ARCH_CORE:39`) — one name, two
  domains, and under `ARCH_CORE:39` a Site is *inside* a Node's `matter`, so the two are not even
  disjoint. Inherited from `SUP:1235` vs `SUP:1245`, made worse here by the Site demotion.
- **`estimated_profile(p, f) → profile`** (`ARCH_CORE:107`) — **`profile` is a type name used nowhere
  else in ARCH_CORE and defined nowhere in `SUP`.** `SUP:124-128` describes true and estimated profiles
  in prose and never gives the record.
- **`occupation(p) → (Practice, Site)`** (`ARCH_CORE:106`) — `Practice` is an inherited type
  (`ABS:72`) that ARCH_CORE never defines, and `Site` is the non-carrier of A.2.
- **Missing rows.** Several ARCH_CORE claims require Deriveds the table does not list:
  `eligible(p, act, n)` (needed by `remit`, `SUP:435`), `share(actor, site)` and `draw_share(c, n)`
  (needed by `condition(n)`'s own formula, `SUP:1245, 1263`), `capacity(date)` (needed by
  `ARCH_CORE:164`'s dockets), and **the judging set** — `ARCH_CORE:36` stores a `judging_set_rule` on
  the Node, so the set itself is derived, and no row names the deriving function.

## A.6 Objects §4 introduces without records

| object | introduced | identity | addressable | verdict |
|---|---|---|---|---|
| **demographic envelope** | `ARCH_CORE:135` | — ; "counts by age band, marks bundle, capability distribution", held as `matter` | it is the source every minted Person draws from (`ARCH_CORE:137`) | **no record, no age-band enum, no id** |
| **channel** | `ARCH_CORE:141-143` | — ; *"the claims their address's channels would have deposited"* | addressed as a thing that *runs through a Node* and *holds a store* | **defined nowhere.** The nearest existing things are `channel_class` on a tie (`ABS:76`) and `handle` in `told_by(person, handle)` (`SUP:243`) — neither is an object |
| **channel store** | `ARCH_CORE:143` | — ; "matter on the Node the channel runs through" | indexed by channel, so it needs channel identity | inherits the gap above |
| **record** (register, charter, deed) | `ARCH_CORE:148` | — ; "matter at a Node" | **claims cite it** — *"removes the corroborating source and drops confidence for everyone whose claim cites it"* | see A-11 |
| **construal distribution** | `ARCH_CORE:143` | — | a minted person *draws* from it | no type, no owner |
| **practice rank** | `ARCH_CORE:128` | field of `Practice` | `mint` target | see A-10 |

**Finding A-11 (rank 1).** **The purge limb requires a claim→record citation edge that the closed
`source` vocabulary cannot express.** `ARCH_CORE:148` makes effacing a record drop confidence *"for
everyone whose claim cites it"*. `Claim.source` is a **closed** four-member set —
`firsthand(event_id)`, `told_by(person, handle)`, `inferred(claim_id…)`, `firsthand_via_knot(event_id)`
— and `SUP:243-245` says so emphatically: *"There is no null source, and `witness` is the only
operation that mints a root token."* **None of the four names a record.** So either §4.4's mechanism
cannot fire, or a fifth source constructor is being added silently. Under the identity axis this is one
missing type constructor and one missing id (`record_id`), and it is the load-bearing half of the
"disseminated / purged" flow at `ARCH_CORE:23`.

## A.7 Roll-up: what the claim system cannot name

Per the brief — *flag every object the claim system cannot talk about.* Against the open `Claim.subject`
space (`SUP:229-234`) the blocker is not the subject space, it is the **absence of a referent to put in
it**. Against the closed stance-referent set (`ABS:188`) the blocker is the enum itself.

| object | nameable in a `Claim.subject`? | nameable as a stance referent? |
|---|---|---|
| Person | yes (by precedent, `SUP:243`) | yes |
| Proposition | yes | yes |
| Faction | collapses into Proposition (A-5) | kind exists, object does not |
| Node | **only if it has an id** — none declared | **no** (unless `Place` ⊇ Node, unstated) |
| Office | **no id declared** | **no** |
| Site | **no id declared** | **no** (unless `Place` ⊇ Site, unstated) |
| **Tenure** | **NO — and this is the thesis-breaking one (A-3)** | **no** |
| Act | **no id declared**, though `SUP:692` hashes one | no |
| Event | **no id declared**, though `SUP:243` requires one | no |
| Claim | yes — `SAID(…)` (`SUP:243`) — but the id it needs is undeclared | no |
| Sensation | **no, by design** (A-6) | no |
| record / charter / deed | **no source constructor exists** (A-11) | no |
| channel | undefined object (A.6) | no |
| demographic envelope | undefined object (A.6) | no |

**Eight of fourteen rows cannot be named by the claim system.** The design's stated thesis is that
everything is disputable; the addressing layer currently supports disputes about **persons and
propositions** and nothing else.

**Section A count: 38 objects audited across A.1–A.6 (3 carriers, 9 non-carrier addressed objects,
6 Tenure kinds, 5 touches modes, 9 Deriveds, 6 §4 objects — Site counted once). 11 findings, A-1…A-11.**

---

# B · THE REFERENCE-INTEGRITY MATRIX

## B.0 The precondition nobody stated: **a `Tenure` has no home**

Before any edge can be checked, someone has to own it. `ARCH_CORE:49` declares the record and **never
says where a Tenure lives**. The five-owner table it inherits (`SUP:334-340`) assigns:
Person → *"`Holding` edges and commitment edges"*; Faction → *"its proposition and its commitment map"*.
So the prior design already stored the same edge **twice**, on both endpoints (`ABS:43-44` records the
Person-side and Faction-side homes side by side), and `SUP:368` states the Holding edge is *"an edge on
the **person**"*. ARCH_CORE unifies six relations into one record and inherits neither answer.

This is not bookkeeping. Under **R-2** — *"a rung module writes only its own state … no module reaches
through another"* (`SUP:379-380`) — **an edge between two owners has no legal writer.** `confer` writes
a `hold` Tenure whose subject is a Person and whose object is an Office: on the Person's side that is
Person state; on the Office's side that is Office state. One of the two is a reach-through unless the
Tenure is declared to live on exactly one of them.

**Finding B-1 (rank 1).** `Tenure` has no declared owner, no declared storage, and no declared index.
Every finding below follows from this one, because **referential integrity needs an inverse index**
(object → edges naming it) and ARCH_CORE declares no index of any kind.

## B.1 Who points at whom

Rows are the referring field; `?` marks a reference whose type ARCH_CORE leaves unstated.

| # | referrer.field | → target | declared at | on target's destruction |
|---|---|---|---|---|
| 1 | `Tenure.subject` | Person \| Node \| **Faction** | `ARCH_CORE:50` | **dangles** |
| 2 | `Tenure.object` | Person \| Node \| Office \| Site \| Proposition | `ARCH_CORE:51` | **dangles** |
| 3 | `Tenure.conferrer` | Person? Office? null? | `ARCH_CORE:49` | **dangles**, type unstated |
| 4 | `Act.actor` | Person | `ARCH_CORE:75` | dangles (an act mid-season by a person effaced mid-season) |
| 5 | `touches[].object` | any of the above, plus Claim (`ARCH_CORE:83`) and record (`ARCH_CORE:148`) | `ARCH_CORE:76` | **this is the destructor itself** |
| 6 | `Office.node?` | Node, or **null** | `ARCH_CORE:37` | dangles; null is the office-cluster/S19 case |
| 7 | `Office.establishment` | [Person] | `ARCH_CORE:37` | dangles per member |
| 8 | `Office.conferral` | an office / a path | `ARCH_CORE:37`; `conferral_path(o)` at `ABS:55` | **may cycle** — see B-6 |
| 9 | `Node.matter` | Site*, `stores`, envelope, channel store, records | `ARCH_CORE:36, 39, 135, 143, 148` | **untyped container** — see B-4 |
| 10 | `Node.dates[]` | standing dates, each naming a **convener office** | `ARCH_CORE:36`; `SUP:337-338` | dangles when the office is effaced |
| 11 | `Person.address` | **duplicates edge 1's `contain`** | `ARCH_CORE:35` vs `ARCH_CORE:61` | see B-2 |
| 12 | `Person.ties` | **duplicates edge 1's `tie`/`knot`** | `ARCH_CORE:35` vs `ARCH_CORE:63` | see B-2 |
| 13 | `Person.ledger` | Claims | `ARCH_CORE:35` | owner-scoped; `efface` forbidden cross-person (`ARCH_CORE:83`) |
| 14 | `Person.stance[referent]` | Person \| Faction \| Proposition \| Place; `provenance: claim_ids` | `ABS:73` | dangles on both axes |
| 15 | `Claim.subject` | open object namespace, **including other Claims** | `SUP:229-234` | dangles |
| 16 | `Claim.source` | `event_id` \| `(person, handle)` \| `claim_id…` | `SUP:243` | dangles |
| 17 | `Ground.support[]` | claim ids in the holder's ledger | `SUP:1516` | dangles |
| 18 | `Derived` args | Proposition, Node, Person, **`root`** | `ARCH_CORE:99-107` | `root` is undeclared (A.5) |
| 19 | `occupation(p)` result | (Practice, **Site**) | `ARCH_CORE:106` | returns a reference to an effaceable object |
| 20 | substream tuple | `(world_seed, tick, subject_id, purpose)` | `ARCH_CORE:181` | **`subject_id` is the only id the document names, and no record carries one** |

**Finding B-2 (rank 2). Two relations are stored twice, in two different shapes.**
`ARCH_CORE:35` keeps `address` and `ties` as **fields of Person**, and `ARCH_CORE:52, 61, 63` make
`contain`, `tie` and `knot` **kinds of Tenure**. Both are live in the same document. The `contain` row
even glosses itself as *"the containment tree; **a person's address**"* (`ARCH_CORE:61`) — the same words
as the Person field. So the design has:
- two homes for one fact, with no statement of which is derived from which;
- two update paths — write `Person.address`, or mint/efface a `contain` Tenure — and only the second is
  covered by the act system's `touches`, so a write through the first is invisible to the conflict rule;
- exactly the read/write asymmetry `CLAUDE.md` §0.1 point 1 names as the recurring hazard class
  (*"when a getter starts computing from a new source while setters still write the old one, every
  writer silently becomes a no-op"*).
The compendium must pick one and record the other as derived. The tree's own precedent says the edge
wins and the field is a view: `SUP:368`, *"Who holds the praefecture is a **query**, not a field."*

## B.2 Dangling-reference risk, by destructor

`efface` is the inverse of `mint` for each of five object kinds (`ARCH_CORE:79-81`), and `revoke` /
`secede` / `migrate` / `degree → 0` / decay / rupture destroy Tenures (`ARCH_CORE:57-63`). **Not one
destruction is paired with a cascade rule, a refcount, or a tombstone.**

| effaced | edges left pointing at it | consequence |
|---|---|---|
| **Person** | 1, 2 (as `succeed` object, `tie`/`knot` object), 3, 4, 7, 14, 15, 20 | an office with a dead establishment member still sources a pool (`SUP:435-438`); a hearth's `succeed` pointer names a corpse |
| **Node** | 1, 2, 6, 9, 10, 18 | **every Person contained in it loses their address**, i.e. loses rung, jurisdiction and aggregation (`SUP:100-101`). Effacing one Node orphans an unbounded set of Persons |
| **Office** | 2 (`hold`), 8, 10 (as convener) | live `hold` Tenures over a nonexistent office; a standing date whose convener does not exist |
| **Site** | 2 (`hold`), 19 | `occupation(p)` returns a dead Site; `condition(n)`'s draw-weighted mean (`SUP:1245`) sums over a missing child |
| **Proposition** | 2 (`commit`), 14 (stance referent), and **the faction itself** (`ARCH_CORE:42-43`) | every committed person is committed to nothing; `faction(p)`'s domain element is gone while its range survives |
| **Claim** | 14 (`provenance`), 16 (`inferred`), 17 (`support[]`) | a ground pleaded from a claim that no longer exists |
| **record** (charter, deed) | claims that cite it (`ARCH_CORE:148`) | **intended** — see B-3 |

**Finding B-3 (the constructive one).** `ARCH_CORE:146-151` already contains the correct pattern and
does not generalise it. Effacing a record **does not delete the citing claims**; it *"removes the
corroborating source and drops confidence for everyone whose claim cites it"*, and
`ARCH_CORE:150` names the principle: **"Suppression is a confidence attack, not a deletion."** That is
exactly the right answer for every row of the table above — an effaced referent should degrade what
points at it, not orphan it. The design applies it to one object out of seven. The compendium should
state it once, as a rule over all references, and note the two guards that already exist:
- **de-individuation is refcounted** — a person re-merges only if *"no other person's ledger names
  them"* (`ABS:299`, `SUP:209-210`). That is the only refcount in the design, and it guards the
  *merge* path, not the `efface` path (`ARCH_CORE:81`), which has no such condition.
- **a dangling `succeed` pointer is repaired by generation, not integrity** — person-generation trigger
  2 is *"a succession pointer resolving to a non-existent heir"* (`ABS:296`). The design's answer to one
  dangling reference is to mint the missing referent. That is a real, citable pattern; it just does not
  scale to the other six rows.

**Finding B-4.** `Node.matter` (`ARCH_CORE:36`) is a **single untyped field asked to hold five distinct
kinds**: Sites (`ARCH_CORE:39`), a hearth's `stores` (`SUP:337`), the demographic envelope
(`ARCH_CORE:135`), the channel store (`ARCH_CORE:143`), and records (`ARCH_CORE:148`). Four of the five
are addressed by name from elsewhere — `hold`-Tenures name a Site, `transfer` names `stores`
(`SUP:1425-1428`), person-minting names the envelope, claims cite records. **A field with no declared
structure cannot be indexed, so none of those four references has a resolution path.** `matter` is
where the document's typing debt is concentrated.

## B.3 Orphan risk

| orphan | how it arises | detected by |
|---|---|---|
| Person with **no** `contain` edge | `secede` and `migrate` are listed as destroyers (`ARCH_CORE:61`) with **no paired creation in the same act**; whether `migrate` is atomic is unstated | **nothing.** `SUP:100-101` says the person then has no rung, no jurisdiction and no aggregation — silently |
| Node with no parent | the root — **never declared** (A.5); `sovereign_fraction(root)` presumes exactly one | nothing |
| Office with `node = null` | by design (`ARCH_CORE:37`); this is the office cluster and S19 (`ARCH_CORE:187`) | nothing — and it is a *reserved* fork, so it must be carried, not fixed |
| Tenure whose endpoint is gone | every row of B.2 | nothing |
| Site whose Node is effaced | B.2 | nothing |
| **`Faction` as a `Tenure.subject`** | see B-5 | nothing |

**Finding B-5 (clean typing defect).** `ARCH_CORE:50` declares `subject ∈ Person | Node | Faction`.
Walk the five table rows at `ARCH_CORE:59-63`: `hold` Person→, `commit` Person→, `contain` Node→ and
Person→, `succeed` Node→, `tie`/`knot` Person→. **No kind admits a Faction subject.** And
`ARCH_CORE:42` has already deleted Faction as an object. So the subject union carries a member that
(a) has no producing rule and (b) no longer names a thing. The object union at `ARCH_CORE:51` is clean
by the same walk — all five members are reachable — which makes the subject union's dead member a
transcription-level defect rather than a design ambiguity.

## B.4 Cycles

| cycle | reachable? | what the design says |
|---|---|---|
| `contain`: Node → Node → … → Node | **YES, and the design admits it** | `SUP:475` states `sovereign_fraction(root)` is *"a reachability query; total and terminating **even on a cyclic graph**"*. Node→Node containment has **neither** a single-parent constraint **nor** an acyclicity constraint — `ARCH_CORE:69` scopes single-parent to **Persons only** |
| `succeed` ∘ `contain`: Node → Person → Node | yes, and it is the **normal** case (the heir lives in the hearth) | unremarked. It means the reference graph is not a DAG and every traversal needs a visited-set |
| `tie`/`knot`: Person ↔ Person | yes by construction — the relation is symmetric (`ABS:76-77`) while the record is directed (`ARCH_CORE:49`) | unremarked |
| `Claim.subject` → Claim → … | yes — *"Subjects include other claims"* (`SUP:243`) | **solved in the substrate and not here**: `engine/substrate/keys.py:389-392` gets cycle-freedom *by construction* from an append-only log whose `causes[]` may cite only already-logged ids, enforced by invariant 3 (`keys.py:384-388`). ARCH_CORE has no append-only claim log and no such rule |
| `inferred(claim_id…)` → Claim → … | yes | as above |
| `Office.conferral` → Office → … | yes | `conferral_path(o) reaches root` (`ABS:55`, MACH:305-311) — a cyclic path never reaches root, so a cycle **silently excludes** the office from its cluster instead of being detected |

**Finding B-6.** Four of six cycle classes are reachable and unremarked; the one the executable
substrate already solved (claims citing claims) is solved there by an **append-only log with an
already-logged-only citation rule**, which is a mechanism ARCH_CORE could adopt verbatim for both
`Claim.source` and `Tenure` history.

## B.5 The charge: is single-parent `contain` enforceable as an edge-kind invariant?

`ARCH_CORE:69-70`: *"`contain` must stay single-parent for Persons — enforced as an invariant on the
edge kind, not by a separate tree structure."*

**As stated, no.** An invariant on an edge kind is a **uniqueness constraint on `(subject, kind)`**, and
a uniqueness constraint needs three things this document does not have:

1. **A key for the subject.** Persons have no id (A-1). You cannot assert uniqueness over a subject you
   cannot compare.
2. **A home and an index for the edge set.** Tenures have neither (B-1). "Single-parent" is a property
   of a *collection*, and no collection is declared. Compare `engine/substrate/keys.py:378-381`, where
   uniqueness is checkable **because** the log owns `self._ids` and `_validate` raises on a duplicate.
3. **A checkpoint.** ARCH_CORE's three barriers (`ARCH_CORE:164-168`) name write classes, not
   validation points. Nothing in the loop is declared to run an invariant pass.

Additionally, the constraint is **kind-conditional on the subject's type** (single-parent for Persons,
unconstrained for Nodes), so it is not a property of the edge kind at all — it is a property of
`(kind, subject-type)`. The sentence as written would forbid a Node having two parents, which the
document does not intend and `SUP:475` implies is possible.

### What breaks if two `contain` edges name one Person

Ordered by how silently it fails, worst first:

1. **Nothing errors.** This is the finding. Every consumer of containment is either an **aggregate** or
   an **existential**, and both absorb a second edge without complaint:
   - `member(p, settlement s) ⟺ address(p) passes through **some** community c whose parent is s`
     (`ABS:556`) — an existential. Two addresses make it true twice; it returns `true` either way.
   - `presence/density/footprint` roll up member addresses (`SUP:116`) — a doubly-contained person is
     **counted twice**, so `density` and `sovereign_fraction(root)` (`ARCH_CORE:102`, range `[0,1]`)
     can exceed their declared range with no guard.
   - `condition(n) = Σ children condition(c) × draw_share(c, n)` (`SUP:1245`) — draw shares no longer
     sum to 1, so the aggregate silently leaves `[0,1]`, and `verbs(site, n) = { v : condition(n) ≥
     floor(v) }` (`ABS:444`) then gates on an out-of-range number.
   - `norm(n, prop)` (`ARCH_CORE:104`) and the judging set (`ARCH_CORE:36`'s `judging_set_rule`)
     **double-count the same person's stance**, so one person becomes two votes.
2. **`address` stops being a value and becomes a set.** `SUP:98`: *"A person's **address** is their path
   to the root."* With two edges it is a set of paths, so every function typed `address(p) → path`
   is mistyped, including `eligible(p, act, n)`'s node test (`SUP:435`) and the channel store's
   *"their address's channels"* (`ARCH_CORE:141`).
3. **Jurisdiction becomes ambiguous rather than false.** Two rungs may both convene, levy and judge the
   same person; nothing arbitrates, because the arbitration was supposed to be structural.
4. **The derivation the whole design rests on evaporates, silently.** `SUP:102-104`: *"If a person can
   be contained twice, divided loyalty becomes a set membership and evaporates."* The failure mode is
   not an exception; it is the game quietly becoming a different game.
5. **Cohorts multiply the error.** A cohort is one record with `weight ≥ 1` (`ABS:56`), so every count
   at a node is already a weighted sum over records rather than a count of persons. Double containment
   corrupts a quantity that has no independent check.

**Finding B-7 (rank 1).** The single-parent invariant is currently **unenforceable and its violation is
undetectable at every one of its consumers.** What would make it enforceable, minimally, is exactly what
the substrate already does for Keys: a subject id, a declared owner for the edge set, an index from
subject to edges, and one validation point in the loop — `keys.py:364-365, 378-381` is the four-line
template.

**Section B count: 20 reference edges mapped; 7 dangling-destructor classes; 6 orphan classes;
6 cycle classes; 7 findings, B-1…B-7; 5 named consequences of a double `contain`.**

---

# C · INPUTS AND OUTPUTS, PER FUNCTION

Convention: **stated** = ARCH_CORE gives the type. **inherited** = the type exists in `SUP`/`ABS` but
ARCH_CORE does not restate it, so a reader of ARCH_CORE alone cannot resolve it. **UNSTATED** = no
surface gives it; these are the compendium's gaps and are marked ⛔.

## C.1 The three signatures — `ARCH_CORE:114-116`

### `choose : (Person, View, Sensation) -> Act`
| | |
|---|---|
| **arguments** | `Person` stated (`ARCH_CORE:35`, no id) · `View` **inherited** (*at most K claims*, `SUP:251`; must be a distinct type from `World` with no coercion, `SUP:153-154` — ARCH_CORE does not restate the no-coercion rule) · `Sensation` stated in prose (`ARCH_CORE:120-122`), **members not enumerated** ⛔ |
| **returns** | exactly **one** `Act` — and `Act.payload` is ⛔ untyped (`ARCH_CORE:75`) |
| **reads** | the person's own ledger, stance, capability; the assembled View; the four need scalars |
| **writes** | nothing (`ARCH_CORE:166`, *"nothing but the returned Act"*) |
| **invariant** | **no `World` in scope** — *"NO World, ever"* (`ARCH_CORE:114`); enforcement is by omission, `SUP:143-147` |
| **gaps** | the View is assembled against a **question `q`** (`SUP:251`, `view(person, question)`), and `choose` has no `q` parameter. `ARCH_CORE:177` names this itself: *"`relevance(c, q)` is undefined with no question `q`"*. So `q`'s type, origin and lifetime are ⛔. Returning a single `Act` types the act economy at 1 per person per season, which `ARCH_CORE:9, 187` reserves as unruled (**recorded as a typing observation; the ruling is not this runner's**) |

### `resolve : (Act[], World) -> Event[]`
| | |
|---|---|
| **arguments** | `Act[]` stated · **`World` ⛔ — defined nowhere in ARCH_CORE and nowhere in `SUP`.** It is the only argument that reaches all state, and it is the type the fourteen refusals are written against (`ABS:283`, row 1) |
| **returns** | `Event[]` — **`Event` is defined nowhere in ARCH_CORE** ⛔; `SUP:243` requires it to carry an `event_id`; `ABS:40` says it carries the degree band as a field |
| **reads** | every object a `touches[]` entry names |
| **writes** | *"everything else"* (`ARCH_CORE:167`) — the `acts` write class |
| **invariant** | **no `Person` parameter**, so the resolver acquires no per-actor special case (`SUP:148-149`); order-independence (`ARCH_CORE:171`) |
| **gaps** | the conflict predicate it must run needs a **field** and an **act-id** that the records do not carry (A-9, §0); `mint` entries have no object, so mint↔mint conflicts are invisible (A-10) |

### `witness : (Person, Event) -> Claim[]`
| | |
|---|---|
| **arguments** | `Person` · `Event` ⛔ |
| **returns** | `Claim[]` — 7 fields, **inherited** (`SUP:221`), **no id field** though `inferred(claim_id…)` needs one |
| **reads** | the event; the person's presence/channel; the person's ledger for collision |
| **writes** | **that one person's ledger only** (`SUP:150-151`) |
| **invariant** | **consensus broadcast is a type error** — no signature accepts a collection of persons and one event; `witness` is *the only operation that mints a root token* (`SUP:243-245`) |
| **gaps** | `ARCH_CORE:116` calls a collection *"a type error"* but does not restate the source rule; the `record` citation the purge limb needs has **no source constructor** (A-11) ⛔ |

## C.2 The nine Derived — `ARCH_CORE:99-107`

| # | as printed | resolved signature | reads | writes | invariant | gaps |
|---|---|---|---|---|---|---|
| 1 | `faction(p)` : Proposition → {commit Tenures} | `faction(prop: Proposition) -> Set[Tenure]` | all `commit` Tenures | none | *nothing stores an aggregate* (`ARCH_CORE:109`) | parameter named `p`, typed Proposition (A.5); requires an **index from Proposition to edges** that B-1 says does not exist ⛔ |
| 2 | `principals(f, n)` : (Proposition, Node) → ranked [Person] | `principals(prop, node) -> List[Person]` | commit Tenures + addresses | none | *"Deposition = this returning someone else"* | **the ranking function is ⛔** — by degree? by `w(d)` (`ABS:226-234`)? by regard? An entire political mechanism rests on an unstated comparator |
| 3 | `presence/density/footprint` : (Proposition, Node) → scalar | **three functions, one row** | member addresses (`SUP:116`) | none | scale is derived and gates nothing (`SUP:112`) | `footprint(f)` takes **one** argument at `SUP:116`; the row gives all three two ⛔. Units ⛔ (count? fraction? weighted by cohort weight?) |
| 4 | `sovereign_fraction(root)` : Node → [0,1] | `sovereign_fraction(root: Node) -> float` | the containment graph | none | *"total and terminating even on a cyclic graph"* (`SUP:475`) | **`root` is undeclared** ⛔ (A.5); range `[0,1]` is unguarded under double containment (B.5) |
| 5 | `condition(n)` : Node → [0,1], draw-weighted mean of children | `condition(node) -> float` | children's `condition`, `draw_share(c, n)` | none | *no coarser rung stores one* (`SUP:1239-1242`) | **name collides with `condition(site)`** (`ARCH_CORE:39`); `draw_share` is a required helper with **no row of its own** ⛔ |
| 6 | `norm(n, prop)` : (Node, Proposition) → scalar | `norm(node, prop) -> float` | member stances | none | replaces a stored norm/unrest/reputation | **range and sign convention ⛔**; whose stances — the judging set, or all contained persons? ⛔ |
| 7 | `opening_set(p)` : Person → [Act] | `opening_set(person) -> List[Act]` | eligibility, remit, matter | none | *"exactly one routine"* (`SUP:1134-1135`); no authored opportunity object (`ABS:283`, row 14) | returns **`Act`s that have not been chosen**, so `Act` names both a *candidate* and a *declaration* — one type, two lifecycle states, no discriminator ⛔ |
| 8 | `occupation(p)` : Person → (Practice, Site) | `occupation(person) -> Tuple[Practice, Site]` | practices, sites, draws | none | *"Not a field"* | `Practice` is **inherited and undefined here** (`ABS:72`); `Site` has no identity (A.2). Undefined for a person with no practice — **no null declared** ⛔ |
| 9 | `estimated_profile(p, f)` : (Person, Proposition) → profile | `estimated_profile(person, prop) -> ???` | that person's ledger only | none | *nobody may read the true profile* (`SUP:124-128`) | **`profile` is a type name that exists nowhere** ⛔ — not in ARCH_CORE, not in `SUP`, not in `ABS` |

**Deriveds the document requires and does not list** (each is addressed by name somewhere in
ARCH_CORE or by a formula it inherits): `eligible(p, act, n)` (`SUP:435`), `draw_share(c, n)` and
`share(actor, site)` (`SUP:1245, 1263`), `capacity(date)` (`ARCH_CORE:164`'s dockets; `SUP:337`),
the **judging set** from `Node.judging_set_rule` (`ARCH_CORE:36`), `regard`, and `address(p)`
(consumed by `ARCH_CORE:141`'s *"their address's channels"*). **Six missing rows.**

## C.3 The loop procedures — `ARCH_CORE:164-168`

| step | signature (reconstructed — ARCH_CORE gives none) | reads | writes (declared) | class | gaps |
|---|---|---|---|---|---|
| **B1 CALENDAR** | `(World, date) -> World'` | dates, convening-condition predicates | dates, dockets | calendar | a convening-condition predicate may read *"own state, an R-1 aggregate, or the calendar"* (`ABS:476`) — not restated here ⛔ |
| **B2 MATTER** | `(World) -> World'` | larders, bodies, travel, sites, envelopes | matter | matter | writes *"bodies"*, which includes **death**, i.e. an `efface` of a Person outside the act system ⛔ — see C-2 |
| **M1 DELIBERATE** | `(Person) -> Act`, per person, pure | own ledger; assembled view; sensation | *"nothing but the returned Act"* | — | Sensation is computed here, but `ARCH_CORE:122` says it is computed **"in P2"** — see C-3 |
| **B3 RESOLVE** | `(Act[], World) -> Event[]` | everything named by `touches[]` | everything else | acts | as `resolve` above |
| **M2 RECKON** | `(Person, Event[]) -> Person'` | own ledger | **"own ledger only"** | — | but M2's listed operations include **individuation** — see C-1 |

**Finding C-1 (rank 1). M2's declared write scope and M2's listed operations contradict each other, and
the contradiction is exactly an identity-allocation problem.** `ARCH_CORE:168` lists M2 as *"witness;
confidence decay; eviction; **individuation**"* and declares its writes as *"own ledger only"*.
Individuation **mints a Person** (`ARCH_CORE:136-137`: *"A Person record is minted on any of five
triggers"*, the first being individuation, `ABS:296`). Minting a Person:
- creates a new globally addressable object — not "own ledger";
- requires an **id allocator**, which is shared mutable state;
- therefore breaks the property `ARCH_CORE:170` explicitly relies on: *"The per-person maps write
  nothing global, which is what licenses running them in any order and in parallel."*
Id allocation is the textbook parallelism hazard, and it is the one piece of machinery this design has
not declared at all. The same applies to de-individuation, which **removes** a Person and whose
predicate reads *other people's ledgers* (`ABS:299`) — also not "own ledger only".

**Finding C-2.** A Person can stop existing by two different routes in two different write classes:
**B2** (*bodies*, `ARCH_CORE:165` — natural death, an unlicensed-decider-free channel that `ABS:272`
licenses as exception 1) and **B3** (`efface`, `ARCH_CORE:81`, as the inverse of birth). Two
destructors, two classes, no shared teardown. Whatever cascade rule B-3 recommends has to be reachable
from both.

**Finding C-3 (cross-reference defect inside one document).** ARCH_CORE **restates the phase namespace**
— `ARCH_CORE:160-168` replaces P0–P7 with `B1 · B2 · M1 · B3 · M2` — and then addresses phases by the
**old** names twice: `ARCH_CORE:122` (*"computed in P2"*) and `ARCH_CORE:182` (*"P1's actorless rolls"*).
Two incompatible spellings of the same namespace inside 189 lines. A reader resolving "P2" against
`ABS:251-252` gets NEEDS, which maps to part of M1 — recoverable, but only by leaving the document.

## C.4 Act constructors and verbs

`ARCH_CORE:75` gives `Act := (actor, verb, touches[], payload)`. **`verb`'s domain is undeclared**, and
this is the field that selects behaviour.

| verb, as named in ARCH_CORE | where | in `remit.acts`' closed five? |
|---|---|---|
| `confer`, `revoke` | `ARCH_CORE:59, 65-66` | **yes** (`ABS:130-132`) |
| `commit(+Δ)` | `ARCH_CORE:60` | no |
| `admit`, `annex` | `ARCH_CORE:61` | `admit` ≈ confer; `annex` **no** |
| `secede`, `migrate` | `ARCH_CORE:61` | **no** |
| *"a naming act"*, *"re-naming"* | `ARCH_CORE:62` | **unnamed — not a verb at all** |
| `form_knot`; *"co-presence"*, *"decay"*, *"rupture"* | `ARCH_CORE:63` | **no** — and three of the four are processes or events, not verbs |
| `investigate` | `ARCH_CORE:154` | **no** |
| `mint`, `efface` | `ARCH_CORE:77-81` | **modes, not verbs** — see below |
| (inherited) `issue`, `determine`, `dispatch`, `convene`, `transfer`, `tell`, `read`, `requisition`, `carry`, `compose_agenda` | `ABS:130-132`, `SUP:1425`, `ABS:405-415` | mixed |

**Finding C-4.** `ARCH_CORE:67` asserts *"none needs a verb that does not already exist in
`remit.acts`"* — a closed set of five (`ABS:130-132`). The table above lists **at least nine** verbs
ARCH_CORE itself names that are not in that five, plus four entries that are not verbs. Whether that
assertion is true is the factuality runner's call; **what this runner records is that `verb` has no
declared domain, and the document's own usage spans at least three vocabularies** (the closed five,
the Tenure table's constructors, and the §4 additions).

**Finding C-5.** `mint` and `efface` are declared as **modes** (`ARCH_CORE:77`) but read throughout §2.3
and §4 as **verbs** (*"`mint` a Site is building"*, `ARCH_CORE:79`). One act can carry several
`touches[]` entries, so `mint` as a mode means a single act may create several objects — and nothing
says whether the resulting ids are visible to the same act's other entries. That is the output-binding
gap of A-10, restated at the act level.

## C.5 Predicates and generators stated as formulas

| thing | as stated | gaps |
|---|---|---|
| **conflict** | *"two acts conflict iff they share an object and either mode is `exclude`/`efface`, or both `alter` an `exclusive` field"* (`ARCH_CORE:89-90`) | needs a **field** the record lacks (A-9) and an **act-id** for the tiebreak (`SUP:692`) ⛔; **cannot see mint↔mint** (A-10) |
| **field commutativity** | `additive` (`condition`, `stores`) vs `exclusive` (a succession pointer, an office's remit), *"declared on the field, not the act"* (`ARCH_CORE:86-88`) | **where the declaration lives is ⛔.** It is a per-field annotation on records that carry no field metadata; four examples are given and no registry. The repo's precedent for exactly this is `references/descriptor_registry.yaml` — dotted keys with per-key metadata (`descriptor_registry.yaml:49-58`) |
| **eviction ranking** | `confidence_live × recency`, *"never on stance-weighted salience"* (`ARCH_CORE:175-176`) | ranks over the ledger; **must be a different function from retrieval ranking** (`ARCH_CORE:177-178`) and neither is named ⛔ |
| **substream** | `(world_seed, tick, subject_id, purpose)` (`ARCH_CORE:181`) | **`subject_id` is the only id the document ever names, and no record carries one** ⛔; **`purpose`'s vocabulary is ⛔** — it is a new opaque discriminator with no declared domain, and determinism depends on it being stable across runs |
| **pool reading** | count 7-9→1, 10→2 (`ARCH_CORE:183`) | input type = a die count = `Pool(person, practice)` (`ABS:340`), inherited |
| **magnitude reading** | `(3 + d10) / 8.5` (`ARCH_CORE:184`) | output units ⛔; used for *"nature, which has no skill"* — its `subject_id` is therefore ⛔ (A-10) |
| **advancement gate** | *"a practice gains a rank when an attempt at a standard above its rank resolves AND (witnessed by someone holding the practice higher, OR it failed at a cost the person actually paid)"* (`ARCH_CORE:128-130`) | *"a standard above its rank"* — `standard` is an ⛔ undefined quantity; *"a cost the person actually paid"* — ⛔ in which of the two capacity currencies (`SUP:390-412`) |
| **`investigate`** | `(actor, question, site\|person, spend)` (`ARCH_CORE:154`) | `question` ⛔ (the same `q` as C.1) · `spend` ⛔ (which currency) · **it is written as a record, not a signature, and its return is prose**: *"whose OUTPUT is claims with `firsthand` source into the actor's own ledger"* — which makes it a **second root-token minter** alongside `witness`, whose monopoly `SUP:243-245` declares ⛔ |
| **person minting** | five triggers; *"draws address/marks/capability/stance from the envelope plus its dispersion"* (`ARCH_CORE:136-137`) | **no id source** (A-10) · `envelope` untyped (A.6) · *"dispersion"* ⛔ |
| **channel handout** | *"a minted person is handed the claims their address's channels would have deposited, and **draws** from a construal distribution"* (`ARCH_CORE:141-143`) | `channel` undefined (A.6) · `construal distribution` ⛔ · the handed claims need `source` values, and their originating `event_id`s may predate the person ⛔ |

**Section C count: 3 signatures fully specified; 9 Deriveds; 6 missing Deriveds named; 5 loop steps;
26 verbs/constructors inventoried; 10 formula-level entries; 37 items marked ⛔ unstated;
5 findings, C-1…C-5.**

---

# D · THE TERM INVENTORY

The test applied is `CLAUDE.md` §4's, verbatim in substance: a term must be **idempotent in meaning**
(a later session reading it cold derives the same meaning) and **idiomatic in choosing** (ordinary
usage already supplies the word). `CLAUDE.md` §4's worked failure — `evacuate` coined for what
`retire` already meant, producing a non-existent blocker escalated across three surfaces — is the
shape to test against. Repo-collision evidence below is from a grep of `engine/ systems/ references/
godot/` for each token.

## D.1 The eight coinages, judged

### 1. `mint` — `ARCH_CORE:77, 79-81, 128` — **FAILS idempotency. Two live meanings.**
- **In ARCH_CORE:** a `touches` mode that brings a Person, Node, Office, Site or Proposition into
  existence, and (at `:128`) that raises a practice rank.
- **Already means something else in the same design:** *"`witness` is the only operation that **mints a
  root token**"* (`SUP:245`, restated `ABS:138`). That is a claim-provenance operation, and it is the
  sentence that guarantees the epistemic layer has one entry point.
- **Repo:** `systems/factions/sim/parliamentary_transfer.py:207` uses it in the token sense too
  (*"this is not the place to mint one"*, of a Key type).
- **Verdict:** a reader meeting `mint` cold now has to decide whether it creates a *thing* or a
  *token*, and §4.5's `investigate` (`ARCH_CORE:154-156`) sits precisely at the intersection. Worse,
  `ARCH_CORE:79-81` **glosses it with four plain words in one sentence** — building, founding,
  establishment, birth — which is the evidence that plain words were available.
- **Recommend:** `create` for the mode; keep `mint` for root tokens only; and note that
  `ARCH_CORE:128`'s rank case is a different operation again (A-10).

### 2. `efface` — `ARCH_CORE:77, 81, 83, 148` — **FAILS idiomatic. Passes idempotency, barely.**
- Plain English `efface` means *rub out / obscure*, and in ordinary usage it is near-reflexive
  ("self-effacing"). It is not the word English supplies for *destroy this object*.
- This is the `evacuate`/`retire` shape exactly: a coined term for an operation that `destroy`,
  `delete` or `demolish` already covers.
- **Repo:** zero occurrences anywhere. No collision — and no support either.
- One meaning-stability wobble: `ARCH_CORE:84` says *"the purge limb is therefore NOT closed by
  `efface`"* and `ARCH_CORE:148` says *"What CAN be done … `efface` a record"*. Both are true (the
  target differs) but a cold reader meets a contradiction.
- **Recommend:** `destroy`, and state the target restriction once (`ARCH_CORE:83`).

### 3. `Tenure` — `ARCH_CORE:46, 49` — **FAILS both tests. The most consequential naming defect.**
- Ordinary usage: *the holding of an office or of land, for a period*. A reader lands there cold and is
  right for `hold` and wrong for the other five kinds. **Calling an ordinary friendship a "Tenure"
  (`ARCH_CORE:63`, `tie`) and calling a person's address a "Tenure" (`:61`, `contain`) is not a
  meaning ordinary usage supplies.**
- The document itself signals the strain: `ARCH_CORE:46` calls it *"the one **edge**"* and
  `ARCH_CORE:54` calls it *"one record shape; six relation kinds"*. **`Edge` and `Relation` are the
  words the document reaches for when it explains itself.**
- **Repo:** zero occurrences — so this is pure new vocabulary in a repo whose §4 rule was written
  because new vocabulary cost it real work.
- **Recommend:** `Edge` (what the document calls it) or `Relation`. Reserve `tenure` as the *name of
  the `hold` kind's duration*, which is what it means.

### 4. `Sensation` — `ARCH_CORE:114, 118-123` — **PASSES idiomatic; RISKS a second name for one thing.**
- The word is well chosen for what it does: a body's report, reference-free, answering no query.
- The risk is `evacuate`-shaped in the other direction: the four scalars already have a name in this
  design — **`Needs`** (`SUP:183-190`, `ABS:208-215`), and `ARCH_CORE:121` calls them *"the four need
  scalars"* in the same sentence that names the type `Sensation`. Two words, one quantity.
- **Repo:** zero occurrences.
- **Recommend:** keep it, and **bind it explicitly**: *"`Sensation` is the record; `needs` are its four
  fields"* — one sentence, in the compendium, so the next session cannot derive two objects.

### 5. `Derived` — `ARCH_CORE:94-95, 97` — **COLLIDES with a shipped quantity family.**
- **Repo collision, direct:** `engine/engine_params/params_tables.yaml:2806, 3114, 4188` ship sections
  named *"Derived Values"* and *"Derived Scores"*, and `references/glossary.md:75-82` lists their
  members — Health, Stamina, Coherence, Composure, Momentum. Those are **stored** per-character values.
  ARCH_CORE's `Derived` is a category of things that are **never stored** (`ARCH_CORE:94`). The word
  therefore means *the opposite thing* on the two surfaces.
- This is also a third synonym: the design already says *"compute-on-demand, never push, never store"*
  (R-1, `SUP:374-377`) and *"a query, never a stored set"* (`ABS:55`).
- **Recommend:** `Query`, and cite R-1 as its definition — that is a word the tree already uses for
  exactly this, and it cannot be confused with a stored derived score.

### 6. `principals` — `ARCH_CORE:100` — **WEAK. Passes idiomatic thinly; a plain word is right there.**
- Ordinary usage gives *principal* three readings (chief person; a party to a transaction; head of a
  school) and one homophone (*principle*) that this design uses heavily in a nearby sense.
- **Repo:** `systems/factions/_identifier_census.yaml:3371` uses "principals" for *the parties present
  in a scene* — a fourth reading.
- The row's own gloss says what it means: *"replaces a faction **leader** field"* (`ARCH_CORE:100`).
- **Recommend:** `leaders(prop, node)`.

### 7. `avowed` — `ARCH_CORE:49` — **the word is inherited and fine; the TYPE was narrowed silently.**
- `ABS:239-240` (MACH:180-184) ships **three** avowal states: `avowed · private · covert`.
  `ARCH_CORE:49`'s `avowed?` is written as an optional flag, which can carry two states at most.
- **Recommend:** keep the word, restore the field as `avowal ∈ {avowed, private, covert}`. (A-3.)

### 8. `Node` — `ARCH_CORE:36` — **NOT on the brief's list, and it is the one that will cost most.**
- **It is a rename, not a coinage:** the same object is `Container (a rung)` at `SUP:337` and
  `Container` at `ABS:50`. That is a third name for one object, which is the exact failure §4 describes
  ("two words for one operation manufactured a distinction that the next reader then tried to honour").
- **And it collides with the port target.** `Node` is Godot's scene-tree base class;
  `godot/scene_tree_architecture.md:16` writes `root (Node)`. Every GDScript file in
  `godot/skeleton/` declares `class_name` against that hierarchy
  (`godot/skeleton/core/engine_manifest.gd:5` and six siblings). A design object named `Node` in a
  design whose destination is GDScript guarantees an unresolvable identifier clash, and `CLAUDE.md` §6
  makes the port the live target.
- **Recommend:** `Rung` (the tree's own word, `SUP:337`) or keep `Container`. Not `Node`.

## D.2 Words carrying two or more meanings

| word | meaning A | meaning B | meaning C+ | severity |
|---|---|---|---|---|
| **`B1` / `B2` / `B3` / `M1` / `M2`** | **loop barriers and maps** (`ARCH_CORE:164-168`) | **adversarial-review finding ids** — `ARCH_CORE:88` cites *"the review's **B1** fix"* and `ARCH_CORE:142` cites *"the review's **M1** objected"*, 76 and 24 lines from the loop table | `M1` is also `CLAUDE.md` §0.2's **milestone**; `B6` (`ARCH_CORE:175`) and `M6` (`ARCH_CORE:10`) are review ids with no loop twin | **highest — two namespaces collide inside one 189-line document** |
| **`hold`** | a `Tenure` kind (`ARCH_CORE:52, 59`) | Proposition mood `HOLDS` (`SUP:1514`) | *"claim ids the **holder** holds"* (`SUP:1516`); **and the refusal *"`force` and `hold` never appear in a precondition"*** (`ABS:287`) — which becomes unstatable once `hold` is an edge kind name | **very high** |
| **`condition`** | `condition(site) ∈ [0,1]` (`ARCH_CORE:39`) and `condition(n)` (`:103`) | **convening condition** (`ARCH_CORE:164`) | *"defeat by named condition"* on the stasis ladder (`SUP:1523`) | high — A and B are 125 lines apart in ARCH_CORE |
| **`subject`** | `Tenure.subject` (`:49`) | `Claim.subject` (`SUP:221`) | `Proposition.subject` (`SUP:1514`); `subject_id` (`:181`); a Key `Target` **role** (`engine/substrate/keys.py:65`) | high — five |
| **`object`** | `Tenure.object` (`:49`) | `touches.object` (`:76`) | *"every **object** in this architecture"* (`:19`); a Key `Target` role (`keys.py:65`) | high |
| **`kind`** | `Node.kind` (`:36`) | `Tenure.kind` (`:52`) | mark kind (`ABS:193-201`), need kind (`ABS:208`), stance referent kind (`ABS:188`) | high — five, all live |
| **`act`** | the record `Act` (`:75`) | `remit.acts`, the closed five (`ABS:130`) | **a unit of currency** — *"costs one of his own acts"* (`ABS:415, 474`) | high — a price denominated in a record type |
| **`matter`** | `Node.matter`, a field (`:36`) | **`B2 MATTER`, a write class** (`:165`) | *"matter events"* (`ABS:273`); the English verb | medium-high |
| **`root`** | `sovereign_fraction(root)` (`:102`) | *"root token"* (`SUP:245`) | `conferral_path(o) reaches root` (`ABS:55`) | medium — and A is undeclared (A.5) |
| **`degree`** | commitment degree 0–5 (`:49, 60`) | degree-of-success band (`ABS:145-152`) | knot `depth` is a third depth-like scalar (`ABS:77`) | medium |
| **`presence`** | the Derived (`:101`) | *"deposits by presence and channel"* (`ABS:428`) | `binds = persons-by-presence` (`ABS:136`); `enforcer_presence` (`ABS:430`) | medium |
| **`View` / `view`** | the **type** passed to `choose` (`:114`) | the **function** `view(person, question)` (`SUP:251`) | — | medium — distinguished only by case |
| **`Act` / `opening`** | a declared act (`:75`) | a **candidate** act returned by `opening_set` (`:105`) | — | medium — one type, two lifecycle states (C.2 row 7) |
| **`magnitude`** | a die reading (`:184`) | `impact_vector: axis -> signed magnitude` (`keys.py:96`) | — | low-medium |
| **`stake`** | `Node.stake[]` (`:36`) | `stake_band` manoeuvre (`ABS:39`); *"escalate the stake"* (`ABS:308`) | — | low-medium |
| **`address`** | `Person.address` (`:35`) | *"a petitioner may **address** many offices"* (`SUP:913`) | *addressable*, this audit's own axis | low |
| **`standard`** | *"an attempt at a standard above its rank"* (`:129`) — undefined | `EntryStandardTerm` (`ABS:141`) | — | low, but A is ⛔ |
| **`commit`** | a `Tenure` kind (`:52`) | the operation `commit(+Δ)` (`:60`) | git commit (`CLAUDE.md` §2) | low — kind/verb pairing is fine if declared |

**Finding D-1 (rank 1).** The `B1`/`M1` collision is the most serious naming defect in the document
because it is **self-inflicted and internal**: ARCH_CORE both cites a finding-id namespace and mints a
barrier-id namespace using the same token shapes, 76 lines apart. A compendium reader looking up "B1"
has two correct answers. Rename the barriers to their words — `CALENDAR`, `MATTER`, `DELIBERATE`,
`RESOLVE`, `RECKON` — which the table already supplies at `ARCH_CORE:164-168`.

**Finding D-2.** ARCH_CORE addresses things in **four unrelated id namespaces** with overlapping token
shapes, none of them declared in the document: review findings (`A5 :118`, `B1 :88`, `B6 :175`,
`C13 :160`, `M1 :142`, `M6 :10`), reserved forks (`D-2 :9`, `S19 :9`), module rules (`R-2 :83`,
`P2 :122`, `P1 :182`), and its own loop steps (`B1…M2 :164-168`). A compendium must publish a
namespace key or every cross-reference in it is ambiguous.

**Finding D-3.** `ARCH_CORE:83` applies **R-2** to persons — *"R-2 forbids reaching through a person"*.
`SUP:379-380` states R-2 over **rung modules**: *"A rung module writes only its own state … No module
reaches through another."* Whether a Person is a rung module is a real question (`SUP:96` puts Person
at the bottom of the containment ladder; `SUP:334-340` makes Person an owner). ARCH_CORE widens the
rule's referent without restating it, so the rule's scope is now derived differently by different
readers — the precise non-idempotency §4 forbids.

## D.3 Terms ARCH_CORE uses and does not define (a reader of ARCH_CORE alone cannot resolve these)

`World` (`:115`) ⛔ *nowhere* · `Event` (`:115`) ⛔ *nowhere in ARCH_CORE* · `Claim` (`:83`) →
`SUP:221` · `Proposition` (`:51`) → `SUP:1514` · `View` (`:114`) → `SUP:251` · `Place` (stance
referent) ⛔ *nowhere* · `Practice` (`:106`) → S02:153 · `profile` (`:107`) ⛔ *nowhere* ·
`K`, `Focus`, `Coherence` (`SUP:251-253`) · `obstinacy`, `credulity` (`SUP:174-176`) · `cohort`,
`individuation`, `de-individuation` (`ABS:56, 293-299`) · `seat_items`, `capacity` (`SUP:390-412`) ·
`remit`, `binds`, `conferral`, `establishment`, `upkeep`, `post` (`SUP:416-424`) · `stores`, `yield`,
`levy`, `draw`, `mouths`, `margin` (`ABS:453-462`) · `judging set` (`SUP:311-313`) · `marks`,
`stance`, `ties`, `Knot` `depth`/`strain` (`ABS:71-80`) · `channel_class`, `handle` (`ABS:76`,
`SUP:243`) · `SAID` (`SUP:243`) · `firsthand` (`SUP:243`) · `salience`, `confidence_live`, `recency`
(`SUP:251-254`) · `season_factor` (`:188`, reserved) · `Venue` (`:189`, reserved) · `standard` (`:129`)
⛔ · `spend` (`:154`) ⛔ · `purpose` (`:181`) ⛔ · `construal distribution` (`:143`) ⛔ ·
`dispersion` (`:137`) ⛔ · `age band` (`:135`) ⛔ · `channel` (`:141`) ⛔ · `record` (`:148`) ⛔.

**Twelve terms marked ⛔ resolve to nothing anywhere in the corpus.**

## D.4 Where these belong, mechanically

`CLAUDE.md` §0.05 rules that prose is reference and code is mechanism, so a compendium **cannot** be
the enforcement surface — but the tree already has the machine-readable homes, and their row shapes are
the ones the compendium should mirror so a later migration is transcription rather than redesign:
- **`references/names_index.yaml`** — the one place a definition's name lives. Its schema is
  `<dotted.key>: canonical / aliases / legacy / category / enforce / context`
  (`references/names_index.yaml:19-32`), and its **`context:` field exists precisely for words that
  collide with common English** (`names_index.yaml:30-32`) — i.e. for D.2's whole table.
- **`references/descriptor_registry.yaml`** — dotted keys with per-key metadata and aliases
  (`descriptor_registry.yaml:49-58`); this is the working precedent for `ARCH_CORE:86-88`'s per-field
  `additive`/`exclusive` annotation, which currently has nowhere to live (C.5).
- **`references/glossary.md`** — curated expansions, hand-maintained *"in the same commit as any file
  that introduces or retires a term"* (`references/glossary.md:6-9`).

**Section D count: 8 coinages judged (3 FAIL both tests, 2 FAIL one, 1 collides with shipped params,
1 weak, 1 pass-with-binding); 18 multi-meaning words; 40 inherited terms inventoried, 12 of them
resolving nowhere; 3 findings, D-1…D-3.**

---

# E · THE COMPENDIUM SKELETON

The third deliverable is *"a compendium with cross-references for keys, inputs, outputs and terms."*
Below is the exact section list, each with **what it holds**, **its row shape**, **where its content
comes from**, and **its acceptance test** — so the writing stage fills rather than invents.

Two constraints bind the whole document before its first section:
- **It is REFERENCE, not mechanism** (`CLAUDE.md` §0.05). It may not be cited as the reason a
  behaviour is correct. Say so in §0, or a later session will treat a table here as a gate.
- **Its own vocabulary must pass §4's two tests.** A compendium that coins while cataloguing coinage
  is self-refuting.

### §0 · How to read this, and what it is not
Status line; the fact that nothing here executes (`CLAUDE.md` §0.2); the citation key
(`ARCH_CORE:NN`, `SUP:NN`, `ABS:NN`, repo paths); and — **new, and required by D-2** — **the namespace
key**: which id families exist (`A#/B#/C#/M#` = review findings · `D-#`, `S#` = reserved forks ·
`R-#`, `P#` = module rules and legacy phases · barrier names) and the ruling that ARCH_CORE's loop
steps are renamed to their words so no token is shared.
*Acceptance: a reader can resolve every id token in the compendium without opening another file.*

### §1 · The identity register — **one row per object, and it is the spine**
| column | content |
|---|---|
| canonical name | after D's renames, with the ARCH_CORE spelling as an alias |
| id field | the field, or **`NONE — DECLARED GAP`**. No inferred ids |
| identity tuple | what actually distinguishes two instances, or "unspecified" |
| stable across a season | yes / no / conditional, with the mutator that breaks it |
| owner | which of the five owners holds it (`SUP:334-340`) — **`Tenure` is `UNOWNED`** (B-1) |
| minted by / effaced by | the verbs, both routes where two exist (C-2) |
| addressed from | the referring fields, keyed to §3's edge numbers |
| nameable in a `Claim.subject` | yes / no |
| nameable as a stance referent | yes / no, against the closed four (`ABS:188`) |

Source: §A of this audit (38 objects). *Acceptance: every "NONE" appears in §8's gap register with
what would close it; no row invents an identifier.*

### §2 · The type catalogue — every record, every field, fully typed
One block per record — `Person`, `Node`/`Rung`, `Office`, `Tenure`/`Edge`, `Act`, `touches`,
`Sensation`, and the inherited `Claim`, `Proposition`, `Case`, `Ground`, `Event`, `View`, `World` —
with per-field type, optionality (**and, for `Tenure`, per-KIND optionality**, A-3), range, and
provenance. Every **closed set enumerated in full**: the six Tenure kinds *and* the five-row table
(A.3), the five `touches` modes, the three avowal states, the commitment ladder 0–5, the degree bands,
the four Sensation members. Type not stated anywhere ⇒ the field carries ⛔ and a §8 pointer.
Source: §A + §C + `ABS` §B. *Acceptance: no field is undocumented; ⛔ count matches §8's.*

### §3 · The reference map — cross-references, in both directions
The 20 numbered edges of §B.1, each with: source field → target type(s), cardinality (**declared or
not** — A.8), optionality, whether the target may be effaced while the edge lives, and the required
inverse index. Plus the three sub-registers:
**3a dangling** (7 destructor classes) · **3b orphans** (6) · **3c cycles** (6, with the append-only
precedent at `engine/substrate/keys.py:389-392`).
Then the **inverse index** — for each object, every field that points at it. *That inverse index is
the compendium's most useful page and nothing else in the corpus has one.*
Source: §B. *Acceptance: every edge in §2 appears in §3, and every §3 row appears in §2.*

### §4 · The function catalogue — inputs and outputs
One block per function: printed signature · fully-typed signature · **reads** · **writes** ·
**write class** (`calendar` / `matter` / `acts` / none) · **invariant maintained** · **gaps ⛔**.
Covers `choose`, `resolve`, `witness`, the five loop steps, the act constructors and verbs (C.4's 23),
and the formula-level predicates (C.5's 11 — conflict, commutativity, eviction, substream, the two die
readings, advancement, `investigate`, person minting, channel handout).
Source: §C. *Acceptance: every function's `writes` is consistent with its declared write class —
the check that surfaces C-1.*

### §5 · The Derived catalogue — kept SEPARATE from §4, deliberately
Nine rows plus the six missing ones named at the end of §C.2. Columns: name · signature · domain ·
range **with units** · what it replaces · what it reads · the index it needs · ⛔s.
Separate because a Derived never writes and is never stored (`ARCH_CORE:94, 109`), and merging them
into §4 is how a query becomes a field.
*Acceptance: every Derived has a declared range and a declared reading set; every formula elsewhere in
the compendium that calls a Derived finds it here.*

### §6 · The vocabulary register — one row per term
Row shape mirrors `references/names_index.yaml:19-32` so a later migration is transcription:
`key · canonical · aliases · legacy · category · defined-at (file:line) · one-sentence definition ·
context terms (for English collisions) · idempotent? · idiomatic? · verdict`.
Holds D.1's eight coinages, D.3's forty inherited terms, and every field name from §2.
*Acceptance: a reader with no memory of this repo lands on the right meaning for every row — the
compendium's own §4-compliance check, run on itself.*

### §7 · The collision register
One row per word carrying two or more meanings (D.2's eighteen), each with: the meanings, their
citations, severity, and **the disambiguation ruled** — either a rename or a mandatory qualifier.
Kept separate from §6 because a collision is a *pair* of entries and belongs on its own page; §6 rows
link here.
*Acceptance: after §7, no term in §1–§5 is used in more than one sense.*

### §8 · The gap register — every ⛔, with what would close it
`gap id · what is unstated · where the absence bites · what closing it requires · whether it is a
RESERVED fork (carry, do not answer)`. Reserved rows come from `ARCH_CORE:9-11, 187-189` and are
marked so nobody closes one by accident — `CLAUDE.md` §0's five-test ordering applies to the rest.
*Acceptance: 34 ⛔ from §C plus §A's and §D's, each traceable to a row in §1–§6.*

### §9 · Cross-reference indices
**9a by object** (object → every section that mentions it) · **9b by function** ·
**9c by term** · **9d by source line** (`ARCH_CORE:NN` → compendium sections, so the three
deliverables stay mutually navigable) · **9e by inherited source** (`SUP:NN`, `ABS:NN`).
*Acceptance: every `ARCH_CORE` line 30–189 that introduces an object, function or term appears in 9d.*

### §10 · What is inherited and NOT restated
The pointer table: for each term/type ARCH_CORE uses but does not define (D.3's forty), where its
definition actually lives. This is the section that stops the compendium re-transcribing `SUP` — the
tree's standing rule is *"registered BY REFERENCE … re-transcription = drift"*
(`references/descriptor_registry.yaml:29-30`).
*Acceptance: nothing in §10 is also defined in full in §2 or §6.*

### §11 · Open and reserved — carried, not answered
`ARCH_CORE:9-11`'s may-not list and `:187-189`'s open list, verbatim, each tagged with which
compendium rows are blocked on it. Read-only.

### §12 · Precedent appendix — what the executable substrate already does
Short, and it earns its place because §1's gaps all have working answers 200 lines away:
`Key.id` (`keys.py:145`) · uniqueness invariant 1 (`keys.py:379-381`) · **referential integrity
invariant 3, which raises on an unknown reference** (`keys.py:384-388`) · cycle-freedom by
construction (`keys.py:389-392`) · lookup by id (`keys.py:364-365`) · type-id shape regex
(`keys.py:399`) · dotted quantity keys with aliases (`descriptor_registry.yaml:49-58`) · role
resolution by name rather than import (`engine/substrate/composition.py:52-68`).
*Acceptance: every §8 gap of the form "no id / no index / no integrity check" points here.*

---

# ROLL-UP · THE FIVE MOST SERIOUS IDENTITY OR TYPING GAPS

1. **`Tenure` has no identity and no home** (A-3, B-1 — `ARCH_CORE:49`). The record that carries every
   disputable political fact — who holds what, who is committed at what degree, who contains whom —
   has no id, no owner among the five (`SUP:334-340`), no storage, and no index. So it cannot be a
   `Claim` subject, which means **the design's central thesis — everything is disputable — does not
   reach the object the politics is made of.** It also has no `until`, so a destroyed Tenure leaves no
   trace and `entrenchment` (`ABS:555`) has nothing to read.

2. **`mint` is given the tuple shape of a reference and cannot have one** (A-10 — `ARCH_CORE:76-81`).
   `touches := (object, mode)` addresses an existing object; a `mint` act's object does not exist yet.
   Consequences: no id source for any created Person/Node/Office/Site/Proposition; **two `mint` acts
   cannot conflict**, because the conflict rule keys on a shared object (`ARCH_CORE:89-90`), so two
   settlements can be founded on one spot undetected; and `ARCH_CORE:128` mints a *scalar field*
   under the same word. `mint` needs `(type, spec, output-binding)`, not `(object, mode)`.

3. **Single-parent `contain` is unenforceable, and its violation is invisible at every consumer**
   (B-7 — `ARCH_CORE:69-70`). An "invariant on the edge kind" is a uniqueness constraint, which needs a
   subject key (absent), an owned indexed edge set (absent), and a validation point in the loop
   (absent). If two `contain` edges name one Person, **nothing errors**: `member(p, s)` is existential
   (`ABS:556`), `presence/density/sovereign_fraction` double-count (`SUP:116`, so `[0,1]` is breached),
   `condition(n)`'s draw shares stop summing to 1 (`SUP:1245`), and the judging set votes the person
   twice — while the derivation the design rests on (`SUP:102-104`) evaporates silently.

4. **M2 is declared "own ledger only" and mints Persons** (C-1 — `ARCH_CORE:168` vs `:136-137`).
   Individuation creates a globally addressable object and therefore needs an **id allocator**, which
   is shared mutable state — breaking the exact property `ARCH_CORE:170` uses to license running the
   per-person maps in parallel. De-individuation compounds it by reading other persons' ledgers
   (`ABS:299`). Id allocation is the one piece of machinery the document never mentions.

5. **The conflict rule quantifies over a field the record does not carry, and the purge limb needs a
   claim source that does not exist** (A-9 + A-11 — `ARCH_CORE:86-90`, `:148`). `alter`'s commutativity
   is declared *per field* while `touches` carries only `(object, mode)`, so the rule is not computable
   from the declared data; and `Claim.source` is a **closed** four-member set (`SUP:243-245`) with
   no constructor naming a **record**, so *"drops confidence for everyone whose claim cites it"* has no
   citation edge to walk. Both are single missing type elements — a `field` slot and a `record_id`
   source constructor — and both sit under load-bearing mechanisms.

**Runner-4 honest limits.** (a) This audit reads ARCH_CORE, `10_SUPERSEDING.md`, `CODE_SHAPE_ABSTRACT.md`
§§A–D, the four cited substrate/registry files, and targeted sections of
`20_FABLE5_ADVERSARIAL_REVIEW.md`; it does not read all 2,017 lines of the review or #342's
seventeen documents, so an identity declared only there would be missed. (b) Repo-collision claims in
§D rest on a grep of `engine/ systems/ references/ godot/` for each token, not of the whole tree.
(c) Nothing here executes and nothing was run — per `CLAUDE.md` §0.2 this is an argument about text.
