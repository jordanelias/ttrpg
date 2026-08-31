# DISPOSITIONS — runner findings against ARCH_CORE.md
# Each: ACCEPT (with the change), NARROW, or REBUT (with the line that survives).

## RUNNER 3 — SCOPE. 2 FATAL · 11 MAJOR · 6 MINOR. **Accepted: 17. Narrowed: 2. Rebutted: 0.**

### F-2 · COHORTS WERE DELETED. **ACCEPT — this is the worst error in the brief and it is mine.**
I replaced the cohort with a demographic envelope and made population **matter**. Matter does not act.
So under ARCH_CORE as written, nobody outside the five minting triggers — all notability triggers —
chooses an act, commits to a proposition, or holds anything. That directly negates Jordan's *"every
active decision is made by a character"* and manufactures **elite-only politics by construction**,
which is the exact defect `10_SUPERSEDING.md:205` names and the one-type rule exists to prevent. It
also makes every derived faction elite, including the "dynamically generated" replacements for
collapsed royal ones — so it breaks the very demand the Faction deletion was built to serve.

> **THE CORRECTION. There are TWO objects and they were conflated:**
> - **A cohort IS persons, at coarse fidelity** — one record, a weight, evaluated once, applied to all.
>   **It acts. One act per cohort per season**, exactly as `10_SUPERSEDING.md:628` says, and exactly one
>   type with an individuated person (`:205`). Cohorts hold `commit` edges, carry stance, and can be
>   petitioned, levied and roused.
> - **A demographic envelope is the INFLOW RESERVOIR ONLY** — counts by age band for birth and death.
>   It is matter, it does not act, and it is *not* the representation of the living population.
>
> Minting draws a Person out of a cohort; the envelope only supplies *new* weight. Deletion of the
> cohort was never licensed by anything and I did not notice I had done it.

**Consequence for D-2, and it strengthens the proposal:** one act per *person or cohort*. D-16's exploit
is then exactly the trade I claimed — one cohort acting once, versus eleven persons acting once each
with eleven ledgers and eleven stances toward you. The pricing is real, but only because the cohort was
acting in the first place.

### F-1 · `sovereign_fraction` banks the office-rooted branch. **ACCEPT the typing; NARROW the rest.**
`conferrer` is the one field the fork lives in and it is the one field left untyped — accepted, fix:
`conferrer ∈ Person | Office`. The totality point is **already answered by `FORKS.md` F1**, written after
this runner started: conferral basis is **per office**, and `sovereign_fraction` is stated there as total
only over the office-rooted subgraph with callers handling a partial answer. Carry that sentence into
ARCH_CORE rather than restating the fork as open.

### ACCEPTED IN FULL, each a real gap
- **M-1** demands-up and directives-down have no mechanism. Add the **docket item** as a first-class
  object (an Act whose `touches` mints an item on a `dates[]`), and name `remit.acts` as the down-stroke.
- **M-2** parliament, the sitting and argument have **zero** mechanism, and §0 risks reading as if they
  went with deferred social contest. State in §0 that argument-at-a-sitting is IN and distinct; give it
  `determine` at a date.
- **M-3** threats and pressures have no carrier, and **ConveningCondition is invoked at line 164 and never
  defined**. Give it its tuple: `(holder, predicate, date_form, set_by)`.
- **M-4** demotion has no limb while advancement got one. Add the inverse gate.
- **M-5** kin obligation deleted — `requisition` and the obligation edge are gone, so family has an
  inheritance pointer and nothing else. Add **`oblige`** as a seventh Tenure kind.
- **M-6** `opening_set(p)` drops the node parameter that `eligible(p, act, n)` carries. **`opening_set(p, n)`.**
  Acting beyond your own address is the whole of governance above Settlement.
- **M-7** `spend` is an unnamed third capacity quantity next to a fork. Delete it — under `D2_PROPOSAL`,
  `investigate` costs the season's one act, like everything else.
- **M-8** S19 unstatable for want of a dated item. Closed by M-1's docket item plus `FORKS.md` F3.
- **M-9** four new objects (`Tenure`, `Sensation`, `Derived`, `mint`/`efface`) are walked against **none**
  of the fourteen refusal rows, which the source makes mandatory. Must be walked in deliverable (a).
- **M-10** `Proposition` is minted and **owned by nobody** — I deleted the Faction owner row without
  re-homing its contents.
- **M-11** "three barriers, exactly" constrains the deferred subsystems, because a contest **subdivides
  the tick** (`:658`). State that B3 may re-enter as a nested instance adding no write class. **And
  `contest(container, prize, claimants)` was deleted with the conflict routing** — restore it; it is the
  governance-conflict primitive, not the deferred social-contest subsystem.
- **m-1..m-6** reserved list short by one; `stores` as the `additive` exemplar; `choose -> Act` arity is
  D-2's; **`marks` is the identity field and is never defined**; no-fallback is never stated; balance.

### The two observations worth acting on immediately
- `subject ∈ Person | Node | Faction` has a **dead union member** — no row uses a Faction subject and
  Faction is deleted as a carrier.
- ARCH_CORE cites "§5.2" and "§5.4" as self-references when those numbers belong to `10_SUPERSEDING.md`.
  Cross-document section numbers reused as internal ones.

### WHAT THE RUNNER CONFIRMED — do not re-litigate in the writing stage
Apparatus refusal clean · `mint`/`efface` closes existence · **`Tenure` and its four bought operations
are "the document's best work"** · Faction-as-derived delivers dynamic generation and power-is-not-static
· character generation complete as a generator · **epistemics is the most complete layer** and satisfies
disseminated/purged · field investigation correctly built from existing parts · advancement's up-limb ·
determinism generalised to actorless rolls · over-reach into the three deferred subsystems otherwise low.

## RUNNER 1 — FIDELITY. 3 FATAL · 8 MAJOR · 10 MINOR. **Accepted: 21. Rebutted: 0.**

Two of the three FATALs are **regressions against conclusions my own review reached and I then wrote
past.** That is the same failure mode the review recorded in #343 (round 2: nine of sixteen findings
were regressions in round 1's own text) arriving in my work one document later.

### F-1 · The channel store. **ACCEPT — the fix stays withdrawn.**
The review's M1 made **two** objections and I answered only the second. The first is
`10_SUPERSEDING.md:74-75` — *"Knowledge lives only in ledgers"* — and **a Node is no more a ledger than
a channel is**, so relocating the store made it worse, not better. The claimed licence also fails on the
Container row's own test, `:355-360`: *"The line is provenance, not location."* Stored tellings ARE
derived from persons and DO go stale against them. §14 row 7 independently forbids a knowledge value
stored on the thing known. **Strike the licence; carry the channel store in §7 as OPEN.**

### F-2 · Annexation as `confer` on a `contain` edge. **ACCEPT — this reverses my own review.**
The review ruled re-parenting **moot** on Jordan's ontology (`20_FABLE5:618-625`): *"the tree is
geography, and allegiance lives in factions… a hamlet does not move because a King won a war"*, and rank
1 says outright *"**Re-parenting is not added and should not be** — who holds the ground is `Tenure`,
not a parent pointer."* I reintroduced the operation it refused, and phrased it as the review's
conclusion carried forward. **Correction: annexation is a `hold` Tenure (Faction | Person → Node). The
tree does not move. Delete `annex`/`secede` from the `contain` row.** This is also the better mechanism —
it keeps geography and allegiance as the two objects Jordan separated.

### F-3 · `Sensation` credited to "the review's A5 fix, corrected". **ACCEPT.**
There is no A5 fix to correct — the review withdrew it with **no replacement**, three times over
(`:574`, `:585-589`, `:400-402`). **Reword: `Sensation` is THIS document's proposal against a problem
the review left open.** The defect is the attribution alone, and it is the load-bearing kind: it converts
an open problem into a solved one.

### ACCEPTED IN FULL
- **M-1** Faction IS one of the five owner rows (`:339`); deleting it must be stated as an amendment to
  that table, as §4.2 states its own two, not as formalising the "Nobody" row, which never mentions it.
- **M-2** I invoked Jordan's membership-is-not-holding distinction to license the merge the review
  invoked it to **refuse**. Fidelity defect accepted; whether one shared record is in fact conflation
  goes to the correctness runner.
- **M-3 · the loop is FOUR barriers, not three.** C13 classes **WITNESS as global** — `:653`, events *"fan
  out by presence and channel"*, cross-person by construction — and I moved it inside the per-person map.
  C13 also calls the interior map **"the fourth licence"**, and B6 requires P7's write licence be stated.
  So *"three barriers, three write classes, exactly"* is wrong twice. **Correction: four global barriers
  (Calendar, Matter, Resolve, Witness) + one per-person map carrying an explicit fourth INTERIOR write
  licence.** My "strictly cheaper than eight barriers" also mis-stated the baseline — the design has
  eight *phases*, four of which are barriers.
- **M-4** #342 says *"**the world holds** a demographic envelope per containment node"*; I wrote *"each
  **Node carries**"* and added *"as matter, not as a social aggregate"*, which #342 never says and which
  fails the provenance test. Quote as written; state the ownership assignment as my ruling, with ground.
- **M-5** the five mint triggers are **one of at least two declared-exhaustive rosters** — doc 02 ships
  four individuation triggers and five person-generation triggers, and they are not doc 09's five. Under
  §3.4's own conflict rule doc 02's declared subject is the person. **Rule it and record it.**
- **M-6 · `mint` a Proposition reinstates what F4 demolished. ACCEPT — remove it.** A8 was refuted
  precisely because a proposition is **free-form content** needing no constructor; rank 9's surviving fix
  is *"uttering a proposition is part of an ordinary act"*, **no new object**. Founding a faction is
  uttering plus `commit`.
- **M-7** the `Office` tuple silently drops `revocation` and `seat_items`.
- **M-8** single-parent is a property of the **tree**, not only of Persons — *"every hearth exactly one
  community"*. As written I licensed a multi-parent node graph while citing §1.2 as authority.
- **m-1..m-10**, notably: **m-4** `secede` collides with #342's shipped use of *secession* for a duke's
  **defection** (`05:594`) — one word, two meanings, the exact failure CLAUDE.md §4 records this repo
  paying for; **m-5** only **subsistence and standing** read the world, so `Sensation` carries **two**
  scalars, not four — commitment and exposure are computed from the View; **m-6** no claim source cites a
  *record*, so §4.4's confidence-drop mechanism has no carrier in the closed four-source set; **m-9**
  `mint` an Office collides with `establishment` naming both the act and the staff.

### CONFIRMED — do not re-litigate
`Site` as Node matter (**the licence genuinely exists here and genuinely does not in §4.3 — that contrast
is the point**) · advancement restored verbatim and accurately, the strongest restoration claim in the
brief · `form_knot` ships at `02:399` · `efface` barred from another's ledger · per-field commutativity ·
eviction on clock quantities · the determinism generalisation · deposition-as-ranking · §1's diagnosis ·
the Venue figure, where I tracked the review's **corrected** 8 over its uncorrected residue of 14.

## RUNNER 2 — FACTUALITY. 1 FATAL · 5 MAJOR · 4 MINOR · 2 OBS. **Accepted: 12. Rebutted: 0.**

### ⚠ THREE FINDINGS WERE REDISCOVERED INDEPENDENTLY by the fidelity and factuality runners, which
could not see each other. Per §10's rank-by-independent-rediscovery these are the highest-confidence
results in the set and are not open to argument:
1. **the channel store's licence does not exist** (F-1 / F1)
2. **the loop is FOUR barriers, not three, and WITNESS is global** (M-3 / F4)
3. **"as matter" is my classification, not #342's** (M-4 / F6)

Factuality adds a third ground on the channel store I had not seen: `10_SUPERSEDING.md:746-748`'s
**dormancy ruling already decided this exact move** — *"a banked claim is **a claim**, and claims live in
ledgers; and the alternative is a stored flag on a container, which the amended Container row admits
**only for matter**."* So the placement is not merely unlicensed, it is ruled against.

### F2 + F3 · **THE PURGE LIMB IS BROKEN. ACCEPT — and the replacement is better.**
My §4.4 had `efface` remove a *record* and drop confidence for "everyone whose claim cites it". **No
claim can cite a record.** The source set is closed at four (`:243-245`) and none is documentary. And
*"`SAID` claims **already** make a recantation collide"* is false: collision needs *"same subject, same
predicate form, **same arguments**"* (`:229`), and `SAID(A, ¬C, s12)` differs in arguments from
`SAID(A, C, s12)`. `SAID` occurs **once** in 2,017 lines; `recant` zero times.

> **THE CORRECTED PURGE, and it is shipped rather than invented.** You cannot delete another person's
> memory, and **that is correct** — R-2 forbids it and the design is right to. What can be destroyed is
> an idea's **standing**, and the design already has the mechanism: §12.2's `strike`, which *"kills the
> ground at every venue for everyone"*. **Ideas are purged at the venue, not in the ledger.** A struck
> ground is dead everywhere, publicly, by a named person, on a named fault — which is exactly how
> heresy, attainder and the discrediting of a witness actually work.
>
> **Plus one deliberate addition, argued rather than assumed:** add **`documented(record_id)`** as a
> fifth claim source. The design already needs it twice — `admissible_source` is a Venue door (*"a venue
> that hears instruments only"*, `:1589`) and *"a document's forgery quality"* is a named resistance pool
> (§5.2). With it, a register is `efface`-able matter at a Node, forgery has a home, and burning the
> archive drops confidence **only for claims that actually cited it** — no reach into any ledger.

### ACCEPTED IN FULL
- **F5** the `contain` table row lists `annex`/`secede` (**zero occurrences in the corpus**) and
  `admit`/`migrate` (real, but **not in `remit.acts`**) two lines above prose claiming no new verb.
  Fidelity's F-2 already deletes the row; the columns become `confer`/`revoke` throughout.
- **F9** §14 row 12 fences itself — *"Clear, **on the row's own subject**. The row governs **standing** —
  a social quantity."* A practice rank is capability. **Cite `02:189` alone**, which says it directly.
- **F10** `Venue` is a **12-field tuple plus a 5-field door**; "17 parameters" is right only if folded.
- **F7** §4.3's header says "#342's placement, restored" while relocating it — *"#342's mechanism,
  relocated"*.
- **F8** `mint` a Proposition — third independent hit, after fidelity M-6. Removed.
- **O1** `resolve` is declared at §1.4 `:138-140`, not §5. My seam citation is off by a section.

### CONFIRMED — the load-bearing verifications
**All four absence claims survive**, each grep-backed with no counter-instance: nothing creates a
Site/Node/Office · no tenure over sites or nodes · `relevance(c, q)` is **never defined** and P7 evicts on
salience with no question in scope · the predicate vocabulary names **one form in 2,017 lines**.
**Every number checked out**: four needs, six edge kinds, five modes, three write classes, eight
once-only Venue params. **Both restorations are exact** — `02:186-189` verbatim including both gate
limbs and *"There is no experience clock"*, and `09:528-548`'s five triggers, three envelope contents,
and *"Births and deaths move weights"*. R-2, §1.2, §5.2, §5.5, `remit.acts`, the three write classes and
`(3+d10)/8.5` all verified. **§16 does reserve all six items** I named.

⚠ One compression to fix: `09:539-540` conditions **capability** on the naming event and applies
dispersion only to **stance**; I flattened both into "from the envelope plus its dispersion".

### A pointer for the writing stage, from the runner's coverage note
`proposals/2026-08-31-integration/09_citation_ledger.md` is named by `10_SUPERSEDING.md:27-28` as *"the
verified fact base"* that *"wins over any other document in the review suite"*. No runner has checked
ARCH_CORE's **sources'** citations against it. That is the right starting point for any later pass.

## RUNNER 5 — CORRECTNESS. 6 FATAL · 11 MAJOR · 7 MINOR. **Accepted: 24. Rebutted: 0.**

### F2 · `opening_set` — **THE QUESTION I COULD NOT ANSWER, ANSWERED.** ACCEPT.
`choose` has no `World`, yet a person must know their options, and `verbs(site,n) = {v : condition(n) ≥
floor(v)}` reads hidden world state. **The resolution is to split the one name into the two functions it
was conflating:**
> - **`verbs(site, n)`** is **world truth**, read only by `resolve`.
> - **`opening_set(person, view)`** is **belief**, computed inside `choose` from the person's own ledger.
>
> **A person may therefore attempt a verb the world has already removed, and discover the harbour
> silted.** That is better fiction than a menu that greys out, it needs no new primitive, and §10.1
> already argues for it: *"the people who notice first are the ones whose practice used that verb."*

Second limb accepted: my B1 dropped P0's fourth operation, *"recompute option availability"*, which also
silently breaks §8.7 — a suppressed grievance re-arms because its enabling condition is *"recomputed at
P0 like every other option"*. Restore it.

### F3 · `condition` — **THE DELETION OF `Site` DOES NOT SURVIVE. ACCEPT, and reverse it.**
Three limbs, all real: a Derived is *"never stored"* but `condition` is an accumulator reading its own
previous value; the draw-weighted mean has **no base case** and is not total at a leaf; and node-keying
destroys site identity. The failing case is decisive — a settlement holding a silted harbour (0.1) and a
healthy seam (0.9) collapses to one scalar ≈ 0.5, which **keeps the bulk-shipping verbs the harbour
should have closed and closes the mining verbs the seam should have kept. Both answers wrong.** And
`yield(H) = base(H) × condition(site(H))` and `share(actor, site)` both require sites to have identity.
> The runner's verdict is the honest one: **there is no repair within the stated refusals that keeps
> `Site` deleted.** `Site` is readmitted as an identity. `condition` is **primary state at the node an
> act names, derived only for coarser reads**, with the base case written.

### F4 · `mint` sits outside the conflict rule. ACCEPT — and the repair composes on my own move.
A minted object **has no identifier to share**, so `mint` triggers no conflict, and the three objects the
design is most insistent are single-valued are now minted edges: two `succeed` edges on one hearth, two
`hold` edges on one office, two `contain` edges on one person — **each individually legal, no conflict
fired, the invariant broken only after both resolve.**
> **Declare a CARDINALITY per kind on the schema** (`contain`: 1 per Person subject · `hold`: 1 per
> Office object · `succeed`: 1 per Node subject) and extend the rule: *…or both `mint` edges that jointly
> break a declared cardinality.* Same shape as per-field commutativity, no resolver case, no new object.
> Plus: **a `mint` declares `(parent_of(object), alter)` in its `touches`**, which also closes the
> mint-racing-an-efface pair.

### ACCEPTED IN FULL — the rest
- **F1** `Faction` is an **uninhabited** union member; repair is the row the union already promises —
  `hold | Proposition → Node`. Annexation is that tenure changing hands. The tree never moves.
- **F5** the purge replacement traded R-2 for a **§14 row 3 broadcast** — a burned register dropping a
  fjord fisher's confidence in the same tick, six weeks before news of the fire could reach him. **Gate
  the confidence drop on a claim that the record is gone landing in that holder's ledger**, which makes
  arson's effect map onto the news map.
- **F6** `occupation(p)` is derivable in **neither** half — no term associates a Practice with the
  larder, and no per-actor per-site draw is stored. **Repair (b): occupation is a stance row whose
  referent is a Proposition** — *"I am a fisher of Hafenmark"* — readable by others through ordinary
  claims, no new object.
- **M-a** the per-person maps **do** write globally (individuation moves envelope weight) and
  de-individuation is **order-dependent** — X survives or vanishes depending on whether Y's eviction runs
  first. Repair: a fourth global barrier **B4 CENSUS**, matter class, reading the post-eviction ledger set
  once. Four barriers, three write classes, and the parallelism claim becomes true.
- **M-e** `additive` is order-independent **only** under batching — `clamp` is not commutative with
  addition at the bounds, and the runner's three-answer example proves it. State: *the resolver sums a
  season's deltas and applies the clamp once.* Default for an undeclared field is **`exclusive`**.
- **M-f** `principals` as typed is a **true-profile read, which nobody may perform**. It needs an
  **observer** argument, and the Derived table needs a column separating **resolver-side** queries from
  **person-side** ones — that distinction is §1.3's central rule and my table erased it.
- **M-g** Proposition is orphaned by deleting the Faction owner row; restore an owner row for it.
- **M-h** `mint` an Office or a Node needs a verb the closed `remit.acts` does not contain.
- **M-i** birth is in **two write classes** at once. Repair: `mint` a Person = **individuation of a
  record**; birth is envelope weight in B2.
- **M-j** `efface` on Node/Office/Person widens the **uncleared** discrete limb of §14 row 11 by four
  object classes, unremarked.
- **M-k** `revoke` on `contain` **orphans a subtree** — address is *"their path to the root"*. Secession
  is `confer` to a **different** parent, never a bare revoke.
- **Minors:** `avowed?` appears once, with no producer, reader or meaning — delete or define ·
  `faction(p)` signature mismatch · `Sensation` narrows to the **two** world-reading scalars ·
  `investigate` must resolve to an Event the actor **witnesses**, or it becomes a second root-token
  minter · advancement is an **`alter`** on a bounded field, not a `mint` · eviction has a ranking and
  **no trigger** · the `Node` tuple omits per-date capacity and convening conditions.

### CONFIRMED — load-bearing and sound
> **`Sensation` is "the document's best move, and it genuinely solves A5."** Four attacks run and
> failed: constructibility over the frozen post-B2 world · no re-admitted omniscience (four floats
> cannot become a masked world) · nothing stored, so the Nobody row keeps needs · **and the cohort/person
> one-type claim survives**, because a cohort's subsistence and standing are each a single well-defined
> scalar. It repairs a gap without breaking a rule of the subject, which M1, M2 and M8 all failed to do.

Also held: the barrier/map **ordering** · per-field commutativity as the right **locus** · the
determinism generalisation, including `mint` where `purpose` absorbs the missing subject · deposition
needing no verb · the **`Derived` category itself** · and eviction on clock quantities — where the
runner rules my observation that `relevance(c, q)` is undefined at eviction **correct, and an
improvement on the review**, which did not notice it.

## RUNNER 4 — KEYS. 982-line audit, 38 objects, 20 reference edges. **All accepted.**

### THE DEEPEST FINDING IN THE WHOLE SET
> **`Tenure` has no identity and no home.** No id, no owner among the five, no storage, no index — so
> **the record carrying every disputable political fact cannot be a `Claim` subject.** The design's
> entire thesis is that everything is disputable, and it does not reach the object the politics is made
> of. There is no `until` field either, so a destroyed tenure leaves no trace.

**MY RULINGS, taken now so the writing stage has them:**
1. **A Tenure is owned by its SUBJECT** — §4.2 already files *"`Holding` edges and commitment edges"* on
   the Person row, so this is the shipped placement, not a new owner.
2. **`Tenure := (id, subject, object, kind, since, until?, conferrer?, degree?)`.** `until` makes a
   revoked tenure a historical fact that can be claimed about, argued over, and read for entrenchment.
   **`avowed?` is deleted** — it had no producer, reader or meaning.
3. **Object ids are minted from the determinism substream** — `(world_seed, tick, subject_id, purpose)`
   already exists at §6 and already covers `mint` via `purpose`. This closes keys #2 at no cost: ids are
   deterministic, order-independent, and unique **without a shared allocator**, which is exactly what
   keys #4 says breaks M2's parallelism. **One mechanism closes both.**

### ACCEPTED, with rulings
- **keys #2 · `mint` cannot carry a reference tuple** — the object does not exist yet, so two `mint` acts
  share no object and cannot conflict. Independently rediscovered by the correctness runner (F4). Closed
  by the id rule above plus correctness's **declared cardinality per kind**.
- **keys #3 · single-parent `contain` is unenforceable and its violation is invisible at every consumer**
  — `presence` and `sovereign_fraction` leave `[0,1]`, draw shares stop summing to 1, a judging set votes
  one person twice, and **nothing errors**. Needs a subject key, an owned indexed edge set, and a
  validation point. Accepted in full; the cardinality declaration is the validation point.
- **keys #4 · M2 mints Persons while declared "own ledger only"** — independently rediscovered
  (correctness M-a). Closed by B4 CENSUS plus substream-derived ids.
- **keys #5 · the conflict rule quantifies over a field `touches` lacks, and the purge limb needs a claim
  source that does not exist** — third independent hit on the purge (factuality F2, correctness F5).
- **`Node` is RENAMED to `Container`.** It collides head-on with Godot's scene-tree base class
  (`godot/scene_tree_architecture.md:16`) — **the port target** — while renaming what `SUP:337` already
  calls *"Container (a rung)"*. My coinage was worse than the shipped word on both counts.
- **The loop steps are renamed.** `B1`/`M1` collided with the review's own finding ids **B1** and **M1**,
  which I cited 76 lines apart in the same document. Two namespaces, same tokens. Steps become
  **CALENDAR · MATTER · DELIBERATE · RESOLVE · WITNESS · CENSUS**.
- **D-1..D-3 · eight coinages judged, three failing both of CLAUDE.md §4's tests.** Accepted; the
  compendium carries the verdicts and the 12 inherited terms that resolve nowhere in the corpus.

### ⚠ FOUR FINDINGS WERE REDISCOVERED INDEPENDENTLY ACROSS RUNNERS THAT COULD NOT SEE EACH OTHER
the channel store's missing licence (2×) · the loop's barrier count (2×) · `mint` outside the conflict
rule (2×) · the purge limb's missing claim source (3×). Per §10's rank-by-independent-rediscovery these
are the highest-confidence results produced by this exercise.

---

# TOTALS ACROSS ALL FIVE RUNNERS
**12 FATAL · 35 MAJOR · 27 MINOR · ~30 keys findings. Accepted: all. Rebutted: none.**
`ARCH_CORE.md` requires a rewrite, not a patch, and the writing stage builds from these dispositions
rather than from it.
