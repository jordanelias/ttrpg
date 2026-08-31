# 06 · ADJUDICATIONS — every ruling, its ground, its falsifier

## Status: PROPOSED (2026-08-31). These are **design rulings taken by a session, not by Jordan**, except
## where a Jordan ruling is quoted. Under `CLAUDE.md` §2's ED-1094 convention, merge review ratifies —
## **and this suite is HELD BACK, so nothing here ratifies on merge until Jordan says so.**

**Each ruling carries a falsifier**, per `CLAUDE.md` §0.1 point 3: the observation that would show it
wrong. A ruling without one is an opinion.

---

## §1 · THE RULINGS

### R-1 · The Key substrate is the Event mechanism; it is not the Claim/witness/Query mechanism

**Ruling.** Compose `Event` onto `engine/substrate/keys.py` — as a Key type family or as Key's
successor sharing `KeyLog`'s invariants. **Never build a second log.** Build `Claim`, `witness` and
the per-person ledger fresh.

**Ground.** `Key` is append-only, id-unique, referentially checked, cycle-free by construction and
content-hashed, and it **runs default-ON in every seeded campaign** with its emission counts and hash
pinned by goldens. `compute_observers`, `memory.record` and `memory_query` exist **only as
pseudocode**, and the executable substrate's own docstring says observer resolution is deliberately
unimplemented. `CLAUDE.md` §0.05: a design document may not be cited as the reason a behaviour exists.

**Falsifier.** Wrong if any `.py` in the tree defines an executing `compute_observers`/`memory_query`
or a per-person claim ledger; or if the Key substrate were dormant in default campaigns.

**Cost.** Neither sweep's headline survives whole. "Greenfield, not a refactor" is too strong; "already
canonical and executable" is false for half the cluster. **CONFIDENCE: HIGH.**

### R-2 · The six-step loop is a refinement of the running three-phase tick

**Ruling.** `SEASON_TICK → ACTION → ACCOUNTING_BOUNDARY` stays the mechanism; the six steps are the
contract implemented inside it. #343's seven phases are retired.

**Ground.** The three-phase tick executes and is pinned; the proposal does not. §0.05 forbids a
proposal retiring an executing spine by assertion. #343's P7 writes are unlicensed under its own
write-class rule.

**Falsifier.** Wrong if `engine_clock.run_tick` does not in fact run three phases in that order, or if
`ACTION`'s body is not caller-supplied.

**Correction it forces.** The head implies the loop had no precedent; `propagation_spec_v1.md` §O.1 is
CANONICAL and is the coarse spine. **CONFIDENCE: HIGH.**

### R-3 · `Site` is a carrier and `condition` is primary state on it

**Ground.** An accumulator that reads its own previous value *is* primary state; a draw-weighted mean
over children has no base case; node-keying collapses two sites into one scalar and yields **two wrong
verb sets at once.** Base case supplied: at a Rung with no Sites, `condition` is undefined and the verb
gate does not fire.

**Falsifier.** Wrong if `condition` never reads its own previous value — i.e. if `wear` and act deltas
are both absolute rather than relative. **CONFIDENCE: HIGH.**

### R-4 · The Faction row is deleted; a faction is a Proposition plus its `commit` edges

**Ground.** Everything the row owned is derivable. Membership is `commit`; leadership, presence,
density and footprint are Queries; the persistent part is the immutable Proposition.

**Falsifier.** Wrong if any faction property is *not* derivable from the proposition plus the commit
set — the candidate is stored institutional memory, which this design homes in Records on a Rung.

**⚠ Cost, stated because it is large.** `engine/autoload/game_state.py` ships `Faction` as a stat-bag
with ~31 `.adjust()` writer sites. **This ruling forbids that shape.** The path is build-beside,
flag-gate, golden-control, cut over — never an in-place edit. **CONFIDENCE: MEDIUM-HIGH** — the
architecture is clear; the migration cost is real and is priced in `07`.

### R-5 · ⊕ The Partition's membership test is a schema column

**Ruling.** `social` is a static boolean on the `(subject-type, field)` pair, declared in the exported
schema and read by the resolver. Act-driven iff `social: true`; Event drivers may write only
`social: false` rows.

**Ground.** As stated, the Partition is a predicate a programmer must adjudicate per instance — a
convention, not a mechanism, and it will drift at the first hard case. As a column it is decidable at
the call site and at load time. **It reproduces Jordan's own worked example exactly:**
`(Site, condition)` is `false` so a plague may move it; `(Rung, exists)` is `true` so **a plague may
not efface a village.**

**Falsifier.** Wrong if any state change's driver depends on the *instance* rather than on the
`(subject-type, field)` pair. **CONFIDENCE: MEDIUM-HIGH** — this is the amendment most likely to need
a third case; the column can carry one.

### R-6 · ⊕ Five identity-bearing kinds, four carriers

**Ruling.** A carrier is identity-bearing **and mutable**; `Proposition` is the one identity-bearing
**immutable** record. **Ground.** Without the definition, "four carriers" is quotable into a false
claim, since Proposition has an id, persists, and is a Tenure subject and object.
**Falsifier.** Wrong if any Proposition field is ever mutated after utterance. **CONFIDENCE: HIGH.**

### R-7 · ⊕ Every Tenure is owned by its subject, whichever carrier that is

**Ground.** The head states the rule only on the Person row, while `succeed` has a Rung subject and
`hold` permits a Proposition subject; the Rung and Office rows never mention Tenures.
**Falsifier.** Wrong if any Tenure kind needs to be stored on its object for a real access pattern.
**CONFIDENCE: HIGH** — one sentence, closes a real seam.

### R-8 · Fixed-point integers for `condition` and `stores`

**Ruling.** `int64`; `condition` on `COND_SCALE = 10_000` as an **exported row, not a literal**;
`stores` in whole units; coefficients as integer pairs; **round-half-up on the non-negative magnitude
with the sign applied after**; sum then `clampi` once; band gates compared by cross-multiplication.

**Ground.** IEEE float addition is not associative, and the band gate makes the difference observable.
The sign rule is not pedantry: Python floors toward negative infinity and GDScript truncates toward
zero, so a naive port silently diverges on negative deltas.

**Falsifier.** Wrong if no `additive` field is ever both order-free-accumulated and band-gated.

**Correction to an earlier reading.** One sweep reported this fix as entirely absent. **It is already
adopted in the head at `01_ARCHITECTURE.md:454-470`** — the sweep grepped a nearby range and stopped
five lines short. **The residue is real and narrower:** `02_THE_SEASON_LOOP.md:570-578` still carries
the un-fixed claim, and `02:844-846` still carries the withdrawn "type error" wording.
**CONFIDENCE: HIGH.**

### R-9 · The purity guarantee is *unreachable-by-name*, not *unwritable*

**Ruling.** No live world state behind any global name; `World` first on every resolver-side Query.
**Say the guarantee is human-checkable, not compiler-checked.**

**Ground.** [engine] GDScript has no module system, no visibility modifiers and no way to scope an
identifier out of a function body. **The port's own skeleton proves it** — resolver modules reach
`GameState` and `KeyBus` from inside their bodies.

**Falsifier.** Wrong if GDScript acquires a visibility modifier, or if a `RefCounted` body can be shown
unable to reach an autoload. **CONFIDENCE: HIGH.**

### R-10 · The degree ladder is four bands, not five

**Ruling.** The live single owner, `engine/autoload/dice_engine.degree_from_net`, implements the ruled
ladder. **The compendium's five-band table describing itself as "shipped" is overturned.**
**Ground.** §0.05: the code is the formula. This is also the exact hazard `CLAUDE.md` §5 records — the
frozen params capture holds the *pre-ruling* bands, and a reader following it in good faith gets a
retracted model. **Falsifier.** Read `degree_from_net` and count. **CONFIDENCE: HIGH.**

### R-11 · `mint`/`efface` are kept for collision-avoidance, under protest

**Ground.** `CLAUDE.md` §4 prefers the ordinary words, and `create`/`destroy` are the ordinary words.
But they are near-universal identifiers likely to collide in GDScript and in modules that already use
them as method names — which is the exception §4 permits. **The condition of keeping them is that they
are defined in the exported schema's own comment, not only in prose.**
**Falsifier.** Wrong if a survey shows no collision for `create`/`destroy` in the port's namespace.
**CONFIDENCE: MEDIUM** — reasonable people could rule the other way, and it is cheap to reverse now
and expensive later.

### R-12 · ED-IN-0200 is discharged by a specification, and stays open until it runs

**Ground.** Jordan ruled; the ledger correctly marks it `status: open, needs_jordan: false`. A
specification is not a discharge — §0.2. The exporter is.
**Falsifier.** Wrong if the three registries are already hierarchically related; they are not.
**CONFIDENCE: HIGH.**

---

## §2 · WHAT THIS SUITE OVERTURNS

Including claims made by the current head and by this exercise's own sweeps.

| # | overturned claim | where | why |
|---|---|---|---|
| 1 | *"zero design objects have a matching type in `engine/`; greenfield, not a refactor"* | sweep R1's headline | half wrong — the Event half exists and executes (R-1) |
| 2 | *"the Event/Claim/Query cluster is already canonical **and executable**"* | sweep R2's headline | half wrong — Claim/witness/Query are pseudocode (R-1) |
| 3 | *"`resolve` is already wired via `module_contracts.yaml`"* | sweep R2 | the `resolver:` field is a strategy **label**; the 27 roles have incompatible signatures |
| 4 | *the fixed-point fix is absent* | sweep R3 | **already adopted** at `01_ARCHITECTURE.md:454-470`; the residue is in `02` only (R-8) |
| 5 | *"123 documents, 108 uncited"* | the head, `00_INDEX.md:10` | stale — **133 / 103 / 67.7% by line weight** |
| 6 | *the five-band degree ladder is shipped* | the head's compendium | the live owner implements four (R-10) |
| 7 | *the collision register is complete* | the head | **five live-code meanings missed**, incl. `hold` as a mass-battle stance and a whole fifth sense of `stance` |
| 8 | *`investigate` is an invented 13th verb* | the head | corrected in-tree — it is a header over six shipped acts |
| 9 | *this loop has no precedent* | the head | `propagation_spec_v1.md` §O.1 is CANONICAL (R-2) |
| 10 | *the design line has no access to ED-IN-0200/0201* | sweep R4 | **the design line filed ED-IN-0201 itself**, and both are `needs_jordan: false` |
| 11 | a `PP-` id above the frozen ceiling | this exercise's own PR340 log | **fabricated** — appears nowhere in the repository. Caught by a blocking gate, corrected in `63192f0`, recorded rather than deleted |

---

## §3 · WHAT ESCALATES TO JORDAN

`CLAUDE.md` §0 requires five tests **in order** before escalating: superseded · irrelevant · answered
by a design document · answered by precedent · answered by what makes sense for the architecture.
**It is emphatic that most pending decisions are not Jordan's, and that preserving a dead question is
how a 156-row queue formed.**

**Candidates raised across fourteen logs: 20+. Surviving all five tests: three.**

### Closed here, with the test that closes them — do not re-escalate

| candidate | closed by |
|---|---|
| `leaders`' comparator | **test 5** — faction-as-Proposition forces a commitment-derived comparator; adopt *commitment degree × backing raisable* and record |
| the two Coherence band tables; the playable-seat list; the cohort exploit; ED-IN-0201's commander ambiguity | **tests 3/4/5**, each with its citation |
| the `piety_track` owner | **test 4** — the contract layer already ships both scopes as separate modules; the "three docs disagree" question dissolved |
| the ripple-substrate direction | **tests 1/2** — superseded by three later generations; the documents become reference |
| "which architecture is the head?" | **test 5** — this suite, on the head's spine, with the greenfield-v2 storage discipline mapped under it |
| **the tenth attribute** | **test 4** — precedent: shipped Godot code already names `Recall` in ~19 places. Record it; Jordan sees it at merge review |
| the `wear`:restoration ratio; `season_factor`'s distribution; the `R ≤ 1` branch | **not rulings — measurements.** §0.1 point 4 forbids settling them by assertion |

### The three that survive

> **1 · CONFERRAL ROOTING IN THE CHURCH.** Is ecclesiastical office **person-rooted**,
> **office-rooted**, or rooted **off-map in a Holy See**? Not superseded, not irrelevant — **the design
> documents explicitly refuse to answer it**: an arc synthesis adjudicated it office-rooted and then
> formally **withdrew** the adjudication as "not an audit's call", and the gap report independently
> converged on the same question with the third option. **Three defensible options, three materially
> different Church games** — a self-consecrating hierarchy, an externally-rooted one, or an off-board
> authority acting as an event source. This is the shape of a real fork: the code is nearly identical
> and the game is not.

> **2 · THE PORT'S TWO RESERVED RULINGS, NOW DUE.**
> **(a) State ownership and the autoload table** (`STRAT:213`, already in the governing spec's
> `[OPEN — Jordan]` register). **It is forced:** the purity fix requires *no live state behind any
> global name*, while both the stale plan and the live `valoria-game` tree do the opposite.
> **Recommendation: rule the design's way** — autoloads presentation-only, `World` passed by parameter.
> **(b) The save model.** `STRAT:19`'s initial-conditions-plus-log replay and the head's snapshot are
> incompatible load paths. **Recommendation: snapshot is the save; the log is retained for provenance
> and UI; re-run-from-seed stays a test device.** Each is one sentence to rule and a rewrite to leave.

> **3 · THE ENGINE VERSION (Q3) — a briefing addendum, not a new escalation.** `CLAUDE.md` §3 already
> holds this question and forbids picking. **New facts for the ruling:** the only artifact that
> asserted 4.6 no longer exists on `main` and is unreachable in this checkout; 4.3 has a declared
> `project.godot`, a CI pin and **two executed, reproducible headless runs**; only two design
> recommendations are version-gated and each has a fallback. **And the consequence that makes it
> urgent: if 4.6 is ruled, the 84-error compile ratchet is void until re-measured under a 4.6 binary**
> — comparing against it would be a confounded measurement of exactly the kind §0.1 forbids. The
> cheapest thing that prices the decision is **one 4.6 headless run**, which takes minutes.

**Everything else is closed above with its citation. Twenty-plus candidates reduced to three is what
§0's amendment says a session is for.**
