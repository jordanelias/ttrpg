# 02 · THE LOOP — the season, nested in the tick that already runs

## Status: PROPOSED (2026-08-31). The three-phase tick in §1 **runs today and is pinned by tests**.
## The six steps **do not run**. `CLAUDE.md` §0.2: done means it runs. §0.05: the code is the mechanism.

---

## §1 · THE RULING THAT ORDERS THIS DOCUMENT

Three loops were in circulation:

| source | shape | state |
|---|---|---|
| `engine/autoload/engine_clock.py` | **three phases: `SEASON_TICK → ACTION → ACCOUNTING_BOUNDARY`** | **RUNS.** Ratified, pinned by `test_engine_clock_phases.py` and by byte-exact seeded goldens |
| `SUP` (#343) | seven phases, P0…P7, three write classes | retired |
| `ARCH`/`02` (#344) | six steps, four barriers, four write classes | proposed |

> **RULING: the six-step loop is a REFINEMENT of the running three-phase tick, not a replacement.**
> The three phases stay the mechanism. The six steps are the authoritative *contract*, implemented
> **inside** `run_tick`:
>
> | phase (runs today) | steps (the contract) |
> |---|---|
> | `SEASON_TICK` | **CALENDAR** |
> | `ACTION` | **MATTER · DELIBERATE · RESOLVE** |
> | `ACCOUNTING_BOUNDARY` | **WITNESS · CENSUS** |

**Why a refinement and not a replacement.** Under `CLAUDE.md` §0.05 the running tick is mechanism and
the proposal is reference; a proposal does not get to retire a ratified, executing spine by
assertion. And the mapping is clean: `ACTION`'s body is already caller-supplied by design, which is
exactly the seam MATTER/DELIBERATE/RESOLVE need.

**#343's seven phases are retired on their own terms**, not by preference: its P7 writes are
unlicensed under its own three-write-class rule, and its "SEVEN PHASES" header sits over an
eight-row table.

**The steps are named by words only, permanently.** The prior brief spelled them `B1 … M2` and cited
review findings `B1` and `M1` seventy-six lines away in the same file — two namespaces, one token
shape, one document. The legacy `P0…P7` labels are retired with the phases they named.

**Correction to the head, worth stating because it cuts the other way.** `ARCH` implies this loop
had no precedent. It has one: `systems/_architecture/propagation_spec_v1.md` §O.1 is CANONICAL
(2026-07-02) and is the coarse spine this refines. This document is the *fine-grain* `engine_clock`
canon — and `engine_clock` is one of the nine modules in `references/module_contracts.yaml` carrying
`doc: null`, so filing it closes a real hole.

---

## §2 · THE SIX STEPS

Four barriers, six steps. **The counts differ because DELIBERATE is a map, not a barrier, and CENSUS
shares WITNESS's join.**

### CALENDAR — barrier 1

| | |
|---|---|
| **reads** | dates; live convening conditions; option-enabling claims |
| **writes** | dates, dockets (**CALENDAR** class) |
| **invariants** | It **fires occasions and decides nothing.** A convening predicate may read only the holder's own state, an on-demand aggregate, or the calendar — never another person's interior. A vacant date **fires, allocates nothing, and lapses**: vacancy is a tax, not a wall. Option availability is recomputed here, which is what keeps a suppressed grievance reachable later. |
| **refuses** | to decide any outcome; to read a person's ledger |

### MATTER — barrier 2; the world freezes after it

| | |
|---|---|
| **reads** | frozen prior state; per-operation substreams |
| **writes** | matter, bodies, travel, the `yield` roll, envelope weights (births and deaths), `condition -= wear` (**MATTER** class); the existence of non-social subjects |
| **invariants** | Events resolve **first**, before anyone chooses. **No social quantity moves here** and no act's effect lands. Death sets `until` on the deceased's Tenures but does **not** open the conferral Date — CALENDAR does that next tick — and does **not** propagate: news travels. **Birth is envelope weight, not a `mint`.** |
| **refuses** | to efface anything whose `(subject-type, field)` row is `social: true` — the Partition's schema column (`01` §2.8). A plague empties a village; only an office strikes it from the roll. |

### DELIBERATE — a map, not a barrier

| | |
|---|---|
| **reads** | the frozen world **through `sense` only** (two floats); the person's own ledger via `assemble`; their own remits |
| **writes** | **nothing but the returned Act** |
| **invariants** | A pure map over persons; any order; fully parallel. `opening_set` is **belief** and can be wrong — a person may attempt what is not in fact available. **One act per person or cohort, universally** (D-2); an office's throughput is its **establishment's** acts. |
| **refuses** | the World; another person's interior; any write |

### RESOLVE — barrier 3

| | |
|---|---|
| **reads** | the declared Acts — `changes[]`, `reads[]`, `contests[]` — and the world |
| **writes** | **everything else** (**ACTS** class), including every act-caused `condition` delta |
| **invariants** | Conflict is decided by the **touch graph** plus declared per-kind cardinality (`01` §2.4). Five strata resolve in order. **One roll, one obstacle**; an attempt at `Obstacle > 2 × Pool` is refused **and the season is still spent.** Additive fields are **summed once and clamped once**, never clamped as they go. Ties break on `H(act_id, world_seed)` — never on submission position. |
| **refuses** | a per-actor special case (it has no `Person` parameter); a second resolver; a fallback when no person acts |

### WITNESS — barrier 4, the join

| | |
|---|---|
| **reads** | this season's Events; presence, channels, Knots |
| **writes** | **one person's own ledger, and only their own** (**INTERIOR** class) |
| **invariants** | **Fan-out is global and one pass; deposit is per-person.** No signals, no subscription table. A Knot deposit **reuses the event id**, so corroboration fails closed rather than manufacturing a second sighting. Four claim constructors, no fifth. **Eviction ranks on `confidence_live × recency` only, never on salience** — otherwise motivated retrieval becomes motivated deletion. |
| **refuses** | a collection signature; writing another person's ledger; consensus |

### CENSUS — shares WITNESS's join

| | |
|---|---|
| **reads** | the post-eviction ledger set, **once** |
| **writes** | the population: individuation and de-individuation; envelope-weight reconciliation (**MATTER** class) |
| **invariants** | **Demand-driven only — nothing generates without a demand, and no clock generates anything.** A weight-1 record *is* a person; there is no conversion operation. |
| **refuses** | scheduled population generation |

---

## §3 · THE FOUR WRITE CLASSES, AND WHY A CLASS IS NOT A PHASE

**CALENDAR · MATTER · ACTS · INTERIOR.**

> **RULED: a write class is not a phase — and the running code already practises this.**

The `ACCOUNTING_BOUNDARY` today both drains ACTION-phase deferred applies *and* accepts immediate
applies from accounting emissions (`engine/substrate/keys.py`, deferring only when the scheduler is
in the ACTION phase). **One write class, two phases writing it, by ratified design (OF-7,
2026-07-07.)** So the class-not-phase rule is not a novelty of the proposal; it is how the only
running barrier already behaves. #343's class-per-phase binding is retired with it.

### The write matrix

| written thing | CALENDAR | MATTER | DELIBERATE | RESOLVE | WITNESS | CENSUS |
|---|---|---|---|---|---|---|
| `Date`, `DocketItem` | **yes** | no | no | **yes** (`carry`, `convene`) | no | no |
| larders, `stores` | no | **yes** | no | **yes** (`transfer`, `levy`) | no | no |
| bodies, ageing, death | no | **yes** | no | no | no | no |
| travel legs | no | **yes** | no | **yes** (movement) | no | no |
| `yield` | no | **yes, only here** | no | no | no | no |
| envelope weight | no | **yes** | no | no | no | **yes** |
| `condition(site)` | no | **yes — `wear` ONLY** | no | **yes — act deltas, only here** | no | no |
| `Tenure` | no | **yes** (`until` on death) | no | **yes** | no | no |
| carrier existence | no | **yes** (death) | no | **yes** (`mint`/`efface`) | no | **yes** (individuation) |
| `stance` | no | no | no | **yes** | no | no |
| the claim ledger | no | no | no | no | **yes, own only** | no |
| the returned `Act` | no | no | **yes** | — | no | no |

**Any unmarked cell is a write-class violation.**

> ⊕ **DECLARED INTERIM VIOLATION.** Until `07_EXECUTION_PATH.md` step 8 executes, `run_accounting`'s
> writes are MATTER-class work performed at the boundary. **This is named here so that no session
> "fixes" it by moving code without the mandated control** — the move is golden-changing and needs
> the two-arm control of `CLAUDE.md` §0.1 point 4.

---

## §4 · ORDER INDEPENDENCE, AND EXACTLY WHAT IT RESTS ON

**The claim.** Within DELIBERATE, persons may be processed in any order or in parallel, because
`choose` reads only the frozen world through two floats and the person's own ledger, and writes
nothing but its returned Act. Within WITNESS, deposits may be made in any order because each writes
only its own ledger.

**What it rests on, precisely:**

1. **The world is frozen** from the end of MATTER to the start of RESOLVE. No barrier writes during
   the map.
2. **No shared allocator.** Ids come from `H(world_seed, tick, subject_id, purpose)` — this is why
   §2.3 of `01` refuses an id service.
3. **The act array is canonicalized before resolution.** A parallel map that `append`s produces a
   nondeterministic array; the array must be sorted by a content-derived key, not by completion order.
4. **Sum-then-clamp-once**, so that clamping cannot depend on arrival order.
5. **⚠ AND ON FIXED-POINT ARITHMETIC, WHICH IS THE PART THAT WAS WRONG.**

> **`additive` order-independence does not survive IEEE floating-point addition.** Float addition is
> not associative; three deltas of `+0.3, −0.5, +0.3` applied to a field at `0.9` land on different
> last-bit values under different orders, and **the degree-band gate makes that difference
> observable.** The design conflated *clamp*-order independence, which batching genuinely delivers,
> with *summation*-order independence, which it does not.
>
> **The fix is fixed-point integers, specified in `03_CODE_SHAPE_GODOT_4_6.md` §4.** Integer addition
> is associative and commutative, so order independence becomes a fact instead of a claim. **The loop
> requires it; the port document owns the representation.**

**What CENSUS is for.** It reads the post-eviction ledger set **once**, against a single snapshot, so
that individuation decisions cannot depend on the order in which ledgers were written. Without a
step that reads one snapshot, order independence is unachievable no matter how the map is written.

---

## §5 · DETERMINISM ACROSS THE LOOP

| | |
|---|---|
| **the seed** | one `world_seed` per campaign |
| **substreams** | every roll draws from `H(world_seed, tick, subject_id, purpose)` — never a shared, re-seeded generator. **The one measured hazard in this tree is real: drawing from the campaign RNG in a new place shifts every downstream draw**, which is how adding two NPCs was observed to move a seeded winner |
| **replay** | identical seed + identical code ⇒ identical event log ⇒ identical content hash |
| **the artifact** | `KeyLog.content_hash()` already exists and is already pinned by `engine/tests/` |

**Executable precedent, and it is the control for every change below.** `engine/tests/` runs full
seeded campaigns and pins exact win-shares, winners, battles and the key-log hash. **Any change that
moves a golden needs the two-arm control of §0.1 point 4** — flag-OFF byte-identity as one arm, and
`tools/balance_oracle.py` (n≥100 campaigns, deliberately not a CI gate) as the other where the change
is campaign-reachable. A change that is campaign-*un*reachable makes both oracle arms identical by
construction, and running it would be a fake control.

---

## §6 · WHAT THE LOOP REFUSES, AND WHETHER THE REFUSAL IS MECHANICAL

A refusal that only a reader enforces is a convention. Both kinds are listed; the distinction is the
point.

| refusal | enforcement |
|---|---|
| `choose` sees no World | **mechanical in Python** (absent parameter, plus World-first on resolver-side Queries). **Convention in GDScript** — see `03` §3 |
| `resolve` sees no Person | **mechanical** — absent parameter |
| `witness` never takes a collection | **convention with a named check** — the collection signature is writable in GDScript |
| no write outside the matrix | **mechanical if the write class is a parameter of the store API**; convention otherwise. *Make it a parameter.* |
| **no fallback: if no person acts, the thing does not occur** | **mechanical** once the personnel gate lands (`07` step 3) — and it is Jordan's ruling ED-IN-0201, not a preference |
| a vacant date lapses rather than blocking | mechanical in CALENDAR |
| nothing generates without a demand | **convention** — there is no clock to remove, but nothing stops one being added |
| no scheduled social recovery | convention |
| an attempt at `Ob > 2 × Pool` is refused, season spent | mechanical in RESOLVE |
| eviction never ranks on salience | mechanical in the eviction comparator |
| a Knot deposit reuses the event id | mechanical in the deposit constructor |
| **no live world state behind a global name** | **mechanical only as a project-settings check** — see `03` §3. This is the weakest link in the port and is stated as such |
