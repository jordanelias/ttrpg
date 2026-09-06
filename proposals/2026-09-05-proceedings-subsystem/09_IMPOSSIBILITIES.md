# 09 · WHAT IS IMPOSSIBLE BY CONSTRUCTION — with the grades stated honestly

## Status: **PROPOSED (2026-09-05). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**

> **`§0`'s rule, restated so the column cannot drift:** **`STRUCTURAL` means the defect HAS NO SPELLING
> in the target language as built.** A property that holds only under an optional checker is
> `STRUCTURAL under a checker · MECHANICAL at runtime`, **written out, both halves** — and if the build
> does not run the checker in CI, **the runtime grade is the real one.**
>
> **`G.1.7`: a claim of STRUCTURAL that is actually MECHANICAL is "a guard that cannot observe what it
> guards."** A row appears below **because a reader will assume it is structural**, and the assumption
> is the failure mode.

| # | the defect | the construction | Python / GDScript |
|---|---|---|---|
| **1** | **a court, a bench or a body ACTS** | no such type exists. `Act.actor : PersonId`; a bench is a Query returning **seats**; `claimants : PersonId[]`. **There is nothing to pass and nothing to pass it to** | **STRUCTURAL / MECHANICAL** (tag assertion) |
| **2** | **the subsystem writes state** | the wrapper is handed **no token**, and the gate cannot be called without one | **STRUCTURAL / ⚠ MECHANICAL** — in GDScript `proj` is a reference to live objects unless actually copied; the guarantee **must be bought with a copy or a lock** (`D-49`) |
| **3** | **a participant reads the room's mind** | `choose` receives a frozen `PersonInterior` and no `World`; `decision/` cannot import `state/` or `world_q` | **STRUCTURAL (typed) / MECHANICAL (path scan)** |
| **4** | **the subsystem returns a WINNER** | `provider.run` returns a `Margin`; a type assertion at the boundary | **STRUCTURAL by signature / MECHANICAL** |
| **5** | **the subsystem widens an outcome** | `veto : bool`, and the ladder takes the **minimum** | **STRUCTURAL by signature** |
| **6** | **an appeal chain never terminates** | `max_depth` is caller-supplied with **no default**; a typed `Refusal` at the cap | **MECHANICAL.** ⚠ In GDScript recursion depth is a **crash**, so reaching the cap without crashing is itself the test |
| **7** | **a proceeding advances on a clock** | no step of it is anything but somebody's act; the seam holds no timer | **MECHANICAL** — a fourth clock is a scan, not a type |
| **8** | **a verdict nobody can undo** | a finding is a `Tenure` its determiner opened; `release` (`own`) and `T-o` (the seat's basis) close them | ⚠ **MECHANICAL at load** — loader invariant 6, **and only once `release` exists.** Today it does not, so the grade is **CONVENTION** |
| **9** | **a stored vote tally** | no field slot; a tally over holders has no owner (`T-a`); a Query is a function | **STRUCTURAL at the type; ⚠ CONVENTION at a schema edit** — a session can add a field, and `05_PROCEDURE.md` §C says a quorum is exactly where somebody will |
| **10** | **a `bias` value anyone can read** | no field exists. The bias is the **divergence** between a ledger and the world, plus conviction weights | **STRUCTURAL by absence — ⚠ and absence is the weaker guard.** Nothing stops a later session adding one; `ID-15`'s price, charged here |
| **11** | **evidence moves a conviction** | ledger and convictions are **different sub-stores with different write tokens** — INTERIOR at WITNESS, ACTS at RESOLVE — and a step holding one cannot reach the other | **MECHANICAL / CONVENTION + scan.** ⚠ The load-time check `F.23` proposes over `requires` **is a comment until `requires` is typed** (`F.24`) |
| **12** | **a shared transcript** | Events carry **no actor, no target, no subject**; WITNESS deposits per person per channel. **There is no field into which a common account could go** | **STRUCTURAL** |
| **13** | **an arrangement's name reaching a resolver** | nothing branches on `arrangement.id`; the twelve differ only in values read as ordinals, sets and relations | ⚠ **CONVENTION + a scan.** `03_PARAMETERS.md` §F.3's falsifier. **This is the closure claim's real grade and it is the weakest one that matters** |
| **14** | **a `speak` that only a seat-holder may take** | `eligibility: ["own"]`, and `eligibility_kinds` has **no `capability` member**; the loader raises on one | **MECHANICAL at load** |
| **15** | **a proceeding-specific Event family** | the kind roster is **derived** from every declared emission column; the log accepts no other kind | **MECHANICAL** — loader invariant 7. ⚠ **And the live fold already violates it**: three kinds are body literals (`F.20b`), so *the loop as built cannot run under the loader as specified* |
| **16** | **a second degree ladder** | one `ladder.degree(margin, veto)`, in the seam | ⚠ **CONVENTION.** `T-k` is *"the one the chain says is enforced by a person noticing"* — no mechanism, no cheap test, and **its violation is locally reasonable every time.** Named as the weak point rather than claimed |

---

## What the count is, and the rule that produces it

**Nine rows have a structural component in Python; three of those degrade in GDScript; four are
CONVENTION at their real strength.**

⚠ **THE NUMBER IS NOT THE POINT AND IS NOT HAND-TALLIED AS EVIDENCE.** `G.3.3` forbids a count typed
by hand, so the rule is stated instead: **count the rows whose grade column contains no `CONVENTION`
term and names no scan.** A later reader should re-run the rule rather than trust the number.

> ### **THE FOUR ROWS TO WATCH, BECAUSE THEY ARE WHERE THIS DESIGN WILL ACTUALLY FAIL**
> **Row 13** — the closure claim is a scan, and a scan is the weakest thing that can carry the
> proposal's central promise. **Row 9** — a quorum is the natural next feature and the natural place
> to store a tally. **Row 16** — a subsystem writing its own band edges is *locally reasonable every
> time*, and `P-01` leaves the edges unruled, which is precisely the condition under which somebody
> writes them locally. **Row 10** — a bias field would be an easy, plausible, ruinous addition.
>
> **Each of the four is a place where a later session does something sensible and deletes a
> mechanism.** That is what this table is for.
