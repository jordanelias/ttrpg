# Provenance — how v2 was produced, and what it does not establish

## Status: **PROPOSED (2026-09-12, ED-IN-0217). HELD BACK FROM RATIFICATION-ON-MERGE, IN FULL.**

---

## §1 · THE ASK, AND WHY IT PRODUCED A SECOND VERSION

Jordan, this session, in three instalments after v1 landed:

1. *"Proposals don't die because of conflicts with existing work. If a proposal is better, then it must be
   considered."*
2. *"Even the design commitments are to be ignored if they are directly attached to code (eg no aggregates
   on a query)."*
3. *"Fable 5.1 read-only adversarial critique of this document suite for failing/rejecting
   ideas/proposals based upon existing codebase and design rulings rather than on the merits/value/qualities
   of the ideas/proposals. **All we care about is improving the game.** Critically re-evaluate all along
   NERS criteria, emergent narrative, gameplay opportunities, applicability. Pass off findings to Opus 5
   extra to comprehensively rewrite a v2."*

**The third instalment is the method; the first two are the standard.** And all three are `R2`, ratified
2026-09-06 (`references/design_rulings_2026-09-06.md:37-50`), which v1 never cited while citing `R7` from
the same file four times.

---

## §2 · THE RELAY

`CLAUDE.md` §10 reserves the `fable` tier for *"read-only audit · planner · orchestrator · guardrail —
**NOT** synthesis or artifact authorship"*, and requires independence to be **structural rather than
declared**.

| stage | tier | seat | independence |
|---|---|---|---|
| **Audit of Parts A–C** for the incumbency failure | `fable` | `.claude/agents/valoria-critic.md` — `tools: Read, Grep, Glob` | **structural**: no Write, no Edit, no Bash. Dispatched with the suite's output, never its reasoning |
| **Audit of Parts D–F**, same lens | `fable` | same seat, separate agent | **structural**, and blind to the other half's findings |
| Sharpening delivered mid-run | — | both agents | Jordan's second instalment reached both while they were still reading, with instructions to revisit anything judged under the looser wording |
| Verification, re-scoring and authorship | `opus` (orchestrator) | this suite | every load-bearing finding re-read at `file:line` before it was carried |

**Neither critic could write.** Between them they read the seven suite files in full plus, at cited ranges,
`01_AXIOMS.md`, `04_CODE_ARCHITECTURE.md`, `07_DYNAMICS.md`, `PLAN.md`, `design_rulings_2026-09-06.md`,
`requirements.yaml`, `verb_table.yaml`, `write_matrix.yaml`, `rosters.yaml`, `hole_register.yaml`,
`carriers.py`, `options.py`, `choose.py`, `witness.py`, `epistemic.py`, `person_q.py`, `world_q.py`,
`matter.py`, `effects.py`, `calendar.py`, `census.py`, `budget.py`, `requires.py`, `dice_engine.py`, both
narrative-engine heads, the 2026-09-10 proposal set, and the combat config.

**Two findings were reached independently by both, which is the only corroboration available here since
neither saw the other's route:** the **chronicle render** as the highest-value discarded idea, and
**declared terms on tenures** as licensed-and-unbuilt.

---

## §3 · WHAT WAS VERIFIED BY HAND BEFORE BEING CARRIED

Every claim below was re-read from the working tree this session. A critic finding that did not reproduce
was dropped rather than carried.

| claim | verified at |
|---|---|
| `R2` is titled *"THE FIVE PROPERTIES — the terminal criteria"* and makes refusals **instrumental, not terminal**, requiring the null result to be **argued** | `design_rulings_2026-09-06.md:37-50` |
| `R7` is titled *"NORMATIVE AGGREGATES PROPAGATE AT THE SPEED OF NEWS"*, names **legitimacy, standing and populace morale** as Queries the design has, and states *"a ruler can be wrong about their own standing"* | `:159-195` |
| `R4 · THE WORLD MUST CHURN` names four routes, *"three need no axiom moved and all four are unbuilt"*, and warns *"do not answer churn with a clock"* | `:77-87` |
| `T-a`/`L3` restricts itself: *"Say **cannot be a field**, never **cannot be stored**"* | `01_AXIOMS.md:279-282` |
| the chronicle veto is of **labels**; the same NOT-list licenses *"retrospective coherence (chronicle + `causes[]` walk)"* | `narrative_engine_design_v1.md:130-136` |
| MATTER matures act-declared stages — *"the only mechanism… WITHOUT anybody acting again"* | `loop/matter.py:55-109` |
| `_eff_transfer` writes `(Rung, stores)` **×2** and refuses a non-Rung side | `loop/effects.py:436-452` |
| `(Rung, exists)` is declared at `[RES]`, `by: "W2/H-41 — founding a hearth"`; nothing writes it | `write_matrix.yaml:294-299` |
| `standing_of` is a **computed gap**, returning maximum gap when nothing pairs | `decision/options.py:443-464` |
| questions are ranked; `qs[0]` decided by the ordering in **801 of 1,068** deliberations | `queries/world_q.py:250-269` |
| `handoff_rules.py` implements **all eight** cross-scale rules; `cross_scale` is imported only by `mc_v18.py` | `engine/cross_scale/handoff_rules.py:1-14` |
| `forge` has no `EFFECTS` entry, so `resolvable_verbs()` excludes it | `loop/effects.py`, `loop/driver.py:99` |

**A critic finding that was dropped**, recorded because a dropped finding is evidence the verification was
real: the Parts D–F audit inferred that a `Tenure.term` proposal required widening `REQUIRES_STEMS`. It
does not — that roster governs *requirement* predicates, not `Tenure` fields.

---

## §4 · EXECUTION ARTIFACTS

```
$ python -m engine.season.harness.register --requirements
  met 1 · not_met 4 · partial 4
    R-01 not_met · R-02 not_met · R-03 met · R-04 not_met · R-05 not_met
    R-06 partial · R-07 partial · R-08 partial · R-09 partial

$ verb_table.yaml × loop/effects.py × requirements.yaml:301-305
  11 run · 5 foldable and never attempted · 2 always refused · 20 with no effect body

$ python -c "from engine.season.state.carriers import matrix_rows_without_a_field as f; print(f())"
  absent      (Office, remit) · (Person, axis_count) · (Person, claim_ledger)
              (Person, coherence) · (Person, scar) · (Proposition, *)
  unmodelled  (Act[], returned) · (ConveningCondition, attached) · (Date, due_at)
              (Date, fired) · (Dispensation, exists) · (DocketItem, matter) · (Petition, exists)

$ 25 corpus worlds driven through full season spans
  seasons completed 25 | errors {} | person-instances 75
  claim sources across all ledgers: {'firsthand': 4499}
  told_by-about-self: 0 | persons with standing_of != max gap: 0

$ [computed, exact] pool 2 vs Ob 2
  FAILURE 74% · PARTIAL 19% · SUCCESS 7% · OVERWHELMING 0%; max margin +2, band needs ≥3
```

**The 4,499 is a control.** An earlier attempt at that run reported the same zeros from **0 completed
seasons**, having swallowed a setup error — a fake control under `CLAUDE.md` §0.1 pt 4, recorded rather
than quietly replaced.

---

## §5 · THE SOURCES

None of the seven research documents is in this repository, so **every claim about what a document says is
unverifiable from the tree** and is carried at the suite's word. They are pinned by SHA-256 prefix and
byte length so that "the same files" is checkable:

| source | sha256 (first 16) | bytes |
|---|---|---|
| *Emergent Narrative in Games: A Cross-Medium Research Compendium* | `2f4cedecaeb5981b` | 68,573 |
| *Emergent Narrative: Mechanical Specifications* | `04e6f281fa0331fc` | 82,477 |
| *Thirteen Strategy Games* — audited revision | `8d9b26a67ac53d8c` | 103,473 |
| *Thirteen Strategy Games… Analysis* — earlier draft | `5ab41cb1447aa023` | 64,097 |
| *Citizens, Settlements and Factions — Nine Titles* — audited revision | `b0714ed1aa6b7314` | 76,432 |
| *…A Systems Teardown of Nine* — earlier draft | `73ebd4eb1f35fc65` | 52,113 |
| **Twenty Games, One Frame** — the reconciliation | `5cbb17cf8571d6ae` | 64,665 |

**Their numbers are admitted as directions and refused as magnitudes.** Three of the seven disown their own
constants; `D1` flags `[TIER-FLOOR: T2 — community wikis]` on every numeric constant in four sections. Every
figure they carry stays `[OPEN — Jordan tuning]`.

---

## §6 · WHAT v2 DOES NOT ESTABLISH

- **No proposal here has been built, so every one is `paper` as a candidate.** The `I` costs are estimates
  read off declared matrix rows and existing effect bodies, not measurements.
- **Proposal 6 contains the suite's one genuine design call** — *should complication be the modal band* —
  and it is put to Jordan rather than answered.
- **The nine surviving refusals are argued, not proven.** `R2` asks for the argument; whether each argument
  persuades is Jordan's to judge, and any of the nine may be revised by him.
- **Two of the ten proposals wait on proposal 8**, whose own scope question (*which claims admit a person
  referent*) is deliberately left for the landing commit.
- **`engine/cross_scale/`'s eight modules were found but not read in depth.** They implement the handoff
  rules and are unreachable from the season loop; what they would do once reachable is unassessed.
- **No `needs_jordan` row is filed.** Two candidates were tested against `CLAUDE.md` §0's five gates and
  closed; the one live design call attaches to fixtures Jordan already owns.
