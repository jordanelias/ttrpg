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
  the 5 are {confer, convene, dispatch, revoke, destroy_record} and `H-71` is why
    -- hole_register.yaml:795 (tier 0, grade absent); falsifier already green,
       test_no_person_can_choose_a_governance_verb_and_h71_is_why, reddens when H-71 closes
  ⚠ NOT A FINDING OF THIS SESSION. Carried by requirements.yaml:303, HANDOFF_IN.md:154 and
    architecture/PLAN.md:1369 before this set was written; re-deriving it added nothing.

$ python -c "from engine.season.state.carriers import matrix_rows_without_a_field as f; print(f())"
  absent      (Office, remit) · (Person, axis_count) · (Person, claim_ledger)
              (Person, coherence) · (Person, scar) · (Proposition, *)
  unmodelled  (Act[], returned) · (ConveningCondition, attached) · (Date, due_at)
              (Date, fired) · (Dispensation, exists) · (DocketItem, matter) · (Petition, exists)

$ THE COUNTERPARTY CONTROL -- two arms of corpus_run.build_at, one string apart
                                  candidates   another person as subject
  control  prop_x.subject = r_hearth       84                           0
  arm      prop_x.subject = p_a            84                          56
  arm, restricted to the 11 EXECUTING verbs: all 11 offered with a person counterparty
  control, same restriction:                 none
  falsifier: restore ids[chain[0]] -> 56 returns to 0

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

**7.6 · Its five composed proposals were first dismissed as "designs for other games", and that was
wrong.** A valley of eight stewards and a city-state of thirty holders are indeed not Valoria — but
*"is this our game?"* is a **framing** test, not a merits one, and it is the same error this whole v2
exists to correct, one level further out. Mined properly, every one of the five carries something:

| composition | what it carries | landed as |
|---|---|---|
| **P1** the steward's reasons | **named intermediaries over an anonymous cohort** — and `Person.weight` already unifies the two in one class (S9.1), with probe `P21` having a cohort **`speak`**. Also: a *distribution of small authored costs* beats one scheduled catastrophe, which is the real argument for a modal complication band | **proposal 13**; refinement to **6** |
| **P2** the slow rumour | **provenance as the interface** — a belief shown as its *chain of sources* rather than a magnitude. This discharges §C.11 **without a meter**, and it is the shaping answer proposal 1 was missing. Plus a **dated stale display**, nearly free since reads are already stale and `Claim.when` exists | refinement to **1** |
| **P3** writ of inquiry | beyond the writ itself: **costs are relational, not material** (*"a writ served on a loyal delegate costs loyalty"*) — which is the only pricing available in a design with no currency and no stored magnitudes. And **symmetry as the anti-degenerate device**: rivals serve writs against you | **proposal 11**; refinement to **2** |
| **P4** successors | its curation rule — *Thousand Year Old Vampire*'s forced erasure — was taken as **proposal 12** and is **WITHDRAWN**: nobody chooses to forget, and `AX-5` licenses *"the fading of memory"* as one of exactly three authorless motions, so there was no `AX-1` gap to repair. ⚠ Pressing on that error produced the real finding — **decay is authorless and renewal is the act** (`07_DYNAMICS.md:171-175`), and a telling today renews only `news.told`. Its carry-*state*-not-capability half stands: `Person.marks` and `(Person, scar)` are declared and unwritten | **proposal 12**, rebuilt |
| **P5** word of a good valley | **population moving on belief rather than true state** — and `move` already executes 650× with its destination bound from the question's referent, so this is proposal 8's clause with a *place*-referent. Also its Objection 4, which derives `AX-1` from outside | refinement to **8**; §S.2 |

**What is genuinely not adopted** is the *packaging*: five named games with scales, turn counts and
benchmarks of their own. **The mechanisms inside them transferred almost entirely**, and the dismissal cost
a proposal (12) that repairs an axiom gap and another (13) whose carrier has been sitting unused since S9
was written.

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

---

## §8 · ADJUDICATION AGAINST THE MASTER WORKPLAN — `ED-IN-0218`

**Done at the end of the session, on Jordan's instruction, against
`workplans/valoria_master_workplan_v7.md` (CANON, ratified the same day under `ED-IN-0216`).** The result
is filed as that document's **§7 · Amendment 1**, and the verdict here is the part that belongs with the
set rather than with the workplan.

**v7 §0's last paragraph did most of the adjudicating and it ruled against most of a fold-in:** *"this
file states no work item that is not traceable to a milestone row or a ledger row that already exists, and
it generates nothing — it sorts what the tree already holds."* Of everything this set produced, **six
items attach to a row v7 already carries and the fourteen proposals do not.** They stay here, in
`proposals/`, surfaced by location.

| what the session produced | how it scores against v7 |
|---|---|
| **the counterparty control** (§4 above) | **the strongest artifact, and it is not this set's idea.** It executes `ED-IN-0210` **Ruling 1**, which Jordan issued on **2026-09-10**, two days before this session, and which nothing had run. The set reached it independently and framed it as a schema proposal; it is a corpus-content fact with a one-value route |
| **proposal 4's declared terms** | pairs with `ED-IN-0210` **Ruling 2** — six antonym closers Jordan named, none in `verb_table.yaml`. Same defect from the other side |
| **proposals 12 / 14** | bear on `ED-IN-0210`'s **open fork** (`dispatch` vs `comply`), because `comply`'s precondition is *"a claim of the dispensation's terms is in the actor's own LEDGER"* and is **artifact-agnostic** |
| **the 25-world claim-source measurement** | the execution reading v7 §1 says R-07 and R-08 do not have — and **less flattering than their `partial`** |
| **the conviction measurement** | corroborates `ED-IN-0214` and sharpens it: the *question* decides `qs[0]` in 801 of 1,068 deliberations, so re-cutting the matrix does not by itself move the dominant direction |
| **"five verbs with effect bodies nothing reaches"** | **a rediscovery of `H-71`**, already carried in four places with a green falsifier. Recorded as such in v7 §7.3 |
| **R-04's document surface** (proposal 14, 14.1) | v7 §4 makes R-04 the gate on retiring the FA tree and never says what its surface would be. This is the first candidate. **Recorded as a pointer; v7 may not schedule it** |
| **the fourteen proposals as a body** | **not milestone movement.** `CLAUDE.md` §0.2: done means it runs. The measurements run; the proposals do not |

⚠ **THE FINDING THAT INDICTS THE SESSION'S METHOD, and it is the same one this set was rewritten to fix.**
Four of these fourteen proposals execute or answer `ED-IN-0210` — **a row Jordan ruled on two days
earlier, which the session never read until the adjudication.** The set's own opening complaint about v1
is that it audited against the code and missed `R2`, the ruling that governs it. **This session then
audited against the code and missed `ED-IN-0210`.** Reading the ledger for the fortnight before the work
is the cheap fix and it was not done. `[BIAS: recency — the tree was read as code and as canon, and the
ruling channel between them was not read at all]`
