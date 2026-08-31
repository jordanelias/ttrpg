# THE SUPERSEDING EXERCISE — shared brief

## Jordan's instruction, verbatim

> "Please have Fable 5 read-only review the individual findings concerning (a) and (b) for gameplay
> implications and codebase implications followed by a read-only review of the synthesis of (a) and
> (b) for gameplay implications and codebase implications. You are adversarially checking for logic,
> code shape, propagation across all scales, use of primitives, and emergent behaviours. Finally,
> you are to perform an intensive pessimistic NERS audit in order to produce a comprehensive
> code-compliant proposal that will supersede PR#342."

**The end deliverable is a NEW PROPOSAL SUITE THAT SUPERSEDES PR #342.** Every read-only stage exists
to make that suite correct. A stage that produces a finding with no consequence for the superseding
suite has produced nothing.

## The five adversarial axes — apply ALL FIVE to every finding

1. **Logic.** Does the finding follow from its evidence? Is a correlate read as a cause? Does the
   argument assume its conclusion? Could the observation have come out the other way?
2. **Code shape.** Against `proposals/2026-08-29-valoria-from-scratch/11_code_shape.md`: the three
   signatures (§2), the four-row ownership table (§3), the two module rules (R-1/R-2, scoped to RUNG
   MODULES), **the FOURTEEN-row forbidden list (§7 — not twelve, not thirteen)**, and §8's four
   structural tests plus its apparatus prohibition.
3. **Propagation across ALL scales.** Person → Hearth → Community → Settlement → Territory → Province
   → Realm, and the alignment structure crossing all of them. Does the finding hold at every rung, or
   only at the rung it was found at? **A fix that works at a settlement and is identically zero at a
   hearth is not a fix** — that is the `exercise()` defect (S-G) and it must not recur.
4. **Use of primitives.** Does it compose on existing primitives — `choose`/`resolve`/`witness`,
   `touches:{(object,mode)}`, `contest(container, prize, claimants)`, the standing date, the petition,
   the dispensation, `Thread-Read(place)` — or does it invent a parallel mechanism? **Re-implementing
   a rule that already lives once is the cardinal defect.**
5. **Emergent behaviours.** What does it make possible that was not possible, and what does it make
   IMPOSSIBLE that was? Name at least one second-order consequence — a behaviour nobody designed that
   falls out of it. And name what it forecloses.

## For every finding, both implications are required

- **GAMEPLAY:** what a player at a seat can now do, or can no longer do. Concrete, at named rungs.
- **CODEBASE:** what a module must hold, read, write or refuse. Typed where possible.

A finding with only one of the two is incomplete — say which half is missing rather than inventing it.

## BINDING STATE — read before anything else

`proposals/2026-08-31-integration/12_PART3_RECONCILIATION.md` is the current state of the world.
In particular:

- **D-1, "the floor", is STRUCK.** An untrained attempt is legal and *"just a small pool"* (`10:33`);
  `rank ≥ 3` **adds** verbs rather than constituting the list (`02:204`); `mark_salience = 1 + 0.2×(…)`
  makes 1.0 the **identity of a product**, not a cutoff, and the unmarked act reaches at half distance
  (`04:415-424`); and the suite already contains the worked postless season — Torvald Aske, non-empty
  menu, **shortfall identical to a Duke's** (`05:52-62`). **What survives: a 3→5 gap for rank-5-only
  verbs, and a ~2× publicity gradient the design declares deliberately.**
- **C-3 is STRUCK.** `convener` is an **office** — conferred, revocable, vacant-able (`05:197-200`).
  **E1's repair is UNSOLVED.** Do not propose the Person typing.
- **§7 has FOURTEEN rows**, and **`:219` (anti-leverage) has no clearance argument on the current
  text** against `thread_condition(n)` — the only surviving EXTENDS in either lane.
- `03_corrected_findings.md` §A's twelve struck claims still bind.
- **No cross-body corroboration exists**, and by construction none could: all three arc-lane documents
  declare the gap report as a handed input in their headers.

## Known open defects the superseding suite MUST resolve (not an exhaustive list — find more)

| # | defect | where |
|---|---|---|
| 1 | `:219` anti-leverage unwalked against the world-substrate object | `11:219` vs `13`/`09` |
| 2 | **FIVE** distinct senses of `exposure`; senses 3 and 4 are the same concept implemented incompatibly, and `07:556` **refuses by name** the stored counter `03:577-579` defines and mutates | `01:174`, `02:62/78-81/490-492`, `03:574-579`, `07:149-157`, `13:215` |
| 3 | view budget **K** collides: `03:325-329` `K = 7 + Focus` vs `09` asserting a constant **12** four times | `03` vs `09` |
| 4 | `13` §5's two slow fuses say *"every season"* and **P1 SETTLE contains neither** | `13:166-181` vs `09:55-59` |
| 5 | `14` §8: header says **ten acts**, paragraph narrates **seven**, `09:33` says **exactly one** | `14:562-574` vs `09:33` |
| 6 | practice rank **0–5** vs **0–7** | `02:153` vs `10:33` |
| 7 | Pool formula: `02:197-200` carries a conditional `thread_pool` term; `10:30` has **no Thread term** | `02` vs `10` |
| 8 | E1: office clusters unpetitionable; repair unsolved | `05_the_blocked_cores.md` |
| 9 | the dangling Thread pointer — `02:4`, `02:435` defer to "doc 04 (Thread)"; **no Thread owner exists in the suite** | `02` vs `00_INDEX` |
| 10 | **three spellings of the three signatures** coexist | `11:57-59`, `01:212-216`, `09:819-821` |
| 11 | `seat_items` is **already a fourth quantity** against `14` §1's "three quantities and nothing else" | `14:91-92` vs `14` §1 |
| 12 | `depletion` has **no independent definition** anywhere in `13` | `13` |

## Standing constraints

- **No apparatus.** No validator, guard, register, freshness checker, measure or process document.
  `11:243-245` forbids it; P-5 forbids it from the other side.
- **No rates about play.** Both corpora are hand-assembled and elite-heavy. The arc tally is an
  **upper bound**.
- **Cite by file:line.** `09_citation_ledger.md` is the verified fact base and **wins over every other
  document in this suite**. Where it does not cover a claim, open the file yourself.
- **This is from-scratch design.** Existing work is reference, never ruling. Do not remediate
  `engine/` or `systems/`.
