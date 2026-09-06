# 08 · THE SEAM — the contract, the manifest row, and the two extensions

## Status: **PROPOSED (2026-09-05). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**

---

# PART A · THE SIGNATURE

Specified against `04_CODE_ARCHITECTURE.md` §C.5, and shaped by the one built provider,
`combat_seam.py`.

```
seam.contest(proj, place, prize, claimants, depth, max_depth)          -- the ONE seam. Unchanged.
  depth < max_depth        or return Refusal(depth_cap), []            -- NO DEFAULT
  provider = manifest.resolve("contest", prizes[prize])                -- BY STRING, AT BOOT
  margin   = provider.run(proj, place, claimants, depth+1, max_depth)  -- a MARGIN. Never a winner
  degree   = ladder.degree(margin, veto = provider.veto)               -- ONE ladder; veto DEMOTES ONLY
```

```
proceedings.run(proj, place, claimants, depth, max_depth) -> Margin
    arrangement = data.arrangements[ occasion_at(proj, place).arrangement ]   -- a ROW, read at load
    bench       = judging_set(proj, place, matter)                            -- a Query
    attendees   = present_at(proj, place)                                     -- FROZEN at entry
    ...                                                                       -- 05_PROCEDURE.md
    return Margin
```

| the four crossings | how this provider meets it |
|---|---|
| **the call** | `World` first — **STRUCTURAL that `choose` cannot make it** |
| **the persons, read never written** | a read-only projection, **and no token.** The provider has nothing to write with |
| **Events back** | `log.append`, same invariants, kinds derived from declared columns |
| **the degree** | a **`Margin`**, never a winner. A type assertion at the boundary |

| the five leaks | grade |
|---|---|
| a state write from inside | **STRUCTURAL** — no token exists in the wrapper's scope |
| a second resolver | **CONVENTION**, stated at that strength. `§C.4` says so of itself |
| a faction as a claimant | **STRUCTURAL** — `claimants : PersonId[]`. A bench is a Query returning **seats**, and a seat is not a claimant |
| a subsystem-specific event family | **MECHANICAL** — the derived kind roster; loader invariant 7 |
| a widened outcome | **STRUCTURAL by signature** — `veto : bool`, and the ladder takes the minimum |

---

# PART B · THE MANIFEST ROW, AND WHY THIS DESIGN REFUSES THE `if`-BRANCH

`shape.py:6740` dispatches with a literal **`if _sub["module"] == "personal_combat":`**, and every
other declared prize falls through to a refusal (`02_THE_SOCKET.md` §2.1).

**This design specifies a manifest row and registers the `if` as a shim, because copying it would
violate three rules at once:**

| rule | how a second `if` breaks it |
|---|---|
| **`§C.5`** | *`provider = manifest.resolve("contest", prizes[prize])`* — **resolution by declaration, at boot** |
| **`02_HIERARCHIES.md` §D.4** | *the engine names the ROLE, the registry names the MODULE, resolution happens by string.* **An import binds the caller at authoring time; a row makes it a fact about the world** |
| **`G.2.6`** | *resolution is a row — never an import, never an inference.* The corpse behind it is the 114-line regex router |

```yaml
# manifest.yaml
- role: contest
  provider: proceedings
  prize: "a matter"
```

⚠ **AND THE PRIZE IS NEW RATHER THAN CLAIMED, WHICH IS A DECISION AND NOT AN OVERSIGHT.**
`rosters.yaml:441-446` maps `"a standing"` and `"a proposition"` to a module named `social_contest`,
which `H-120` records Jordan calling *"an unfinished engine"* on 2026-09-04. **This directory was
directed to be a from-scratch derivation that does not build on that work**, so it declares `"a
matter"` and **leaves both existing rows untouched.** Routing them here instead would supersede
somebody else's work by editing one line — the quiet ratification `CLAUDE.md` §2 says must be loud or
not done. **`02_THE_SOCKET.md` §4 states the option; it is Jordan's.**

---

# PART C · TWO EXTENSIONS TO THE CONTRACT, STATED AS AMENDMENTS

`§E.3`: *a variation needing a richer return is an amendment to the one owner, made once, never a
parallel ladder in a subsystem.* **This design needs two things no prior provider needed. Both are
stated as amendments; neither is smuggled.**

## C.1 · The caller's ordering is a parameter of the run

`combat_seam` needs no order — two combatants alternate. **A proceeding's order IS its mechanism**
(`05_PROCEDURE.md` §A), and it varies by game: rank, alternating, scripted, free, written-only.

> **The amendment:** `provider.run` may order its own sub-steps from a value it read in the
> arrangement row. **It may not order them from anything else** — not from the world, not from a
> capability, not from a default in a body.
>
> **Why this is an amendment and not a second resolver:** the provider is not resolving anything. It
> is **sequencing whose turn it is**, which is the one thing a procedure is (`§G.2.9`), and the
> sequence comes from **data the loader validated**, not from a body. **The falsifier: permute the
> order key and the outcome must move; permute anything else about the sub-steps and it must not.**
>
> ⚠ **The honest risk:** `§C.4`'s *no second resolver* is graded **CONVENTION** — *"the one enforced by
> a person noticing"* — and this amendment is exactly the kind of thing that person must notice.
> **Registered `10_LOOPS_AND_GAPS.md` `P-18`.**

## C.2 · The margin must be produced, and nothing has ever produced one

`degree_of()` recognises `"wound_state"` (live) and `"net"`/`"ob"` (**a reader with no producer** —
`shape.py:6553-6561`: *"NOTHING PRODUCES A `net` ANYWHERE IN THE TRACER"*).

> **This provider is the first producer of the margin-graded branch.** That is not an amendment —
> **it is the branch working for the first time** — but it means every defect in that path will be
> found here, and the band edges (`F.9`, `H-31`) do not exist. **The subsystem cannot run until
> somebody rules them, and this design refuses to invent them.**

---

# PART D · THE DATA — the rows a loader must accept, and the invariants that must fire

## D.1 · `write_matrix.yaml` — the rows the verbs need

| kind | field | steps | class | writer | emits | status |
|---|---|---|---|---|---|---|
| `Tenure` | `degree` | `[RES]` | ACTS | `act_only` | `matter.moved` | ⚠ **exists, with a writer and NO READER** (`F.4`). **This design is its reader** |
| `Tenure` | `since` / `until` | `[MAT, RES]` | MATTER/ACTS | — | `tenure.opened` / `tenure.closed` | exists |
| `Person` | `stance` | `[RES]` | ACTS | `act_only` | `stance.changed` | ⚠ `F.20a` — **a matrix row with no producing verb.** `speak` is a producer |
| `Record` | `exists` / `stages` | `[RES]` | ACTS | `act_only` | `case.opened` | exists |
| `Date` | `due_at` | `[RES]` | ACTS | `act_only` | `date.scheduled` | exists |

⭐ **`(Person, stance)` IS ONE OF THE FOUR ROWS `F5` FOUND WITH NO PRODUCER** — *"no verb in the table
writes any `Person` interior field at all"*, which blocks build step 2 and is tier-0 `H-62`. **`speak`
is a producer for one of the four, and it is a producer of exactly the shape `F.20a` predicted:** *an
interior write is a consequence of an outcome, which is what the degree-keyed column declares.*

## D.2 · The loader invariants this design must satisfy

| # | invariant | how |
|---|---|---|
| 1 | every `verb.writes` pair is a matrix row, **for every `Degree` branch** | four branches × the rows above |
| 2 | every `RES` row has ≥1 producing verb | ⭐ `(Person, stance)` gains one |
| 3 | eligibility kinds ⊆ roster, **`capability` refused by name** | `speak` and `interview` are `own`; `determine` is `remit:` |
| 4 | **every failable CONJUNCT has a refusal kind** | ⭐ **Fig. 26 supplies four conjuncts and four named failures** (`03_PARAMETERS.md` §B.4) |
| 6 | `release`'s kind domain == `tenure_kinds \ {contain}` | ⭐ **satisfiable for the first time — `release` lands** |
| 7 | the Event-kind roster is **derived** from emission columns | nine kinds, all declared. **No body literal** (`F.20b`) |
| 9 | contest prizes ⊆ the subsystem roster | `"a matter"` → `proceedings` |
| 10 | unknown keys rejected — **a `scale:` key fails the load** | ⚠ `convene`'s `scale:` must go (`03_PARAMETERS.md` §C.1) |
| 12 | a verb declaring `contests:` has **`Degree`-keyed `writes` AND `emits`, key sets equal** | `speak`: 4 and 4 · the five investigation rows: 3 and 3 each |

⚠ **AND ONE THIS DESIGN CANNOT SATISFY, NAMED RATHER THAN GLOSSED.** `§C.2`'s `Receipt` — *only the
gate mints one; the log's append asserts every receipt id is in the minted set* — **has no
implementation.** `Event.changes` is a fold-built `StateChange[]`, appended at **eleven** sites
(`HANDOFF_NEXT.md` `1g`), and `Event.__post_init__` checks only `causes`. **So this design's Events
are not gate-verified, and no claim here should be read as saying they are.** `10_LOOPS_AND_GAPS.md`
`P-02`.
