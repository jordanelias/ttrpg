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

## §7 · THE ADJUDICATION OF AN OUTSIDE INTEGRATION DOCUMENT

An eighth document — *"The Third Strand: integrating the emergent-narrative mechanics with the twenty-game
frame"* (`sha256 02458c7e…`, 78,634 bytes) — was supplied after v2 was written. It integrates the two
**narrative** documents with the twenty-game consolidation, a seam the earlier seven left open. **It never
mentions Valoria**, so it cannot be wrong about this tree — only uninformed about it. Adjudicated against
this session:

**7.1 · Seven of its nine modules are items this session reached independently, or things the tree already
ships.** That is corroboration, not duplication, and it is the strongest warrant available for the set:

| its module | this session |
|---|---|
| **M5** the causal ledger — *"installed by all five proposals… build it alone, first"* | **proposal 1**, ranked first, for the same reason. Also reached independently by **both** read-only critics |
| **M1** the three-band order, middle band *"roughly 40%"* | **proposal 6** — measured 19% Partial against the corpus's 41–45% |
| **M2** disposition drift | `H-62`/`W-F`, Jordan's, planned to the YAML |
| **M3** belief in transit — *source · strength · believability · decay* | **`Claim(subject, predicate, value, when, source, confidence)`** — the carrier already has all four |
| **M4** the cohort clock | **proposal 5**, and `R4` route (2) |
| **M7** perishable allegiance | v1's `B2`; Pax Pamir's punished switching |
| **M8** the stale report — *"nothing anywhere shows the player a stale state"* | ⚠ **Valoria's DEFAULT read is stale.** `LedgerReader` returns the stored value, not world truth — one of three places this tree is *ahead* of the corpus |

**7.2 · One module is genuinely new, and it is now proposal 11.** **M6, the writ** — sifting turned from an
authoring instrument into a player's verb. Neither this session nor either critic produced it, and its
substrate turns out to be nearly built: `causes[]` at every write, `occasioned_by` reading it, `open_case`
declared with `own` in its eligibility **sweep**, `Record` carrying `forgery_quality`/`ttl`/`stages`, and
`Record.matured` ruled by Jordan on the grounds that *"the matrix row is the game"*.

**7.3 · Its Objection 1 is aimed at this suite's highest-ranked proposal and it lands.** The record's value
is argued analytically; the one case where a record demonstrably *functions* is a **graph read at a glance**,
not prose. **Adopted into proposal 1**, together with its falsification stub, which is a better test than
v2 offered.

**7.4 · Where it repeats this session's own error, one level up.** Its Part 5 grades on a rubric whose
criterion **C7 "AI dependence"** penalises a proposal *for needing an agent layer* — P1 scores 3 *"because
it requires an agent layer"*. Under `R2` that is a **cost**, not a quality: the same move as refusing a
mechanic because the code does not have it, relocated into a scoring column. Its own ranking half-corrects
for this in prose (*"P3 is deliberately not ranked first… scoring a subsystem on a rubric built for games
flatters it"*), which is the right instinct applied to one row and not to the criterion.

**7.5 · Its internal arithmetic checks, which v1's did not.** Verified: the fourteen-requirement tally
(3 occupied / 4 partial / 7 absent) reconciles against its own table; all five grade rows re-sum and fall in
their stated bands; and the module-to-proposal matrix reconciles cell by cell against each proposal's
declared module list. It also carries seven `[FIXED:]` entries, four independent objections, and a
`[SELF-AUTHORED — bias risk]` tag, and it states its own yield honestly as *"one new design, one new
mechanism, one repair, one specification, one partial repair."*

**7.6 · What is NOT adopted.** Its five composed proposals are designs for *other games* — a valley with
eight stewards, a city-state of thirty holders, a multiplayer migration map. They are not Valoria and are
not proposed for it. What transfers is **M6**, **Objection 1**, and the corroboration in 7.1.

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
