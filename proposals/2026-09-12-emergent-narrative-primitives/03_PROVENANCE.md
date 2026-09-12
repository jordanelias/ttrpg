# Part C — provenance, execution artifacts, and what could not be established

## Status: **PROPOSED (2026-09-12, ED-IN-0217). HELD BACK FROM RATIFICATION-ON-MERGE, IN FULL.**

---

## §1 · HOW THIS WAS PRODUCED

**Jordan, this session, in four instalments.** (1) Read four research documents in the context of each
other and of the repository as it stands; run an adversarial pessimistic NERS audit of each document's
mechanics and proposals; have Fable 5.1, read-only, use those findings to interrogate the game; then
identify and propose the most apt mechanics, curated for gameplay, emergence, applicability,
relevancy, immediate impact and implications going forward; and pass all of it to Opus to write out in
agonist–antagonist methodology with fidelity to findings. (2) Three further documents, consolidated
with the first four. (3) Plot Valoria on every axis the seven documents evaluate games against.
(4) At the granularity of the clusters, axes and sets of primitives themselves.

**The relay, stated because `CLAUDE.md` §10 rules on it.** §10 reserves the `fable` tier for
*"read-only audit · planner · orchestrator · guardrail — **NOT** synthesis or artifact
authorship,"* and requires that independence be **structural rather than declared**. The shape used:

| stage | tier | seat | independence |
|---|---|---|---|
| Repository inventory — resolution layer · season loop · settlements/factions | `sonnet` ×3, parallel | read-only explorers | bounded extraction; no judgment delegated |
| **NERS audit** of D0+D1 · D2 · D3 | `opus` ×3, parallel | agonist auditors | each ran `skills/ners/SKILL.md` in full against the tree; none saw the others' output |
| **Interrogation of the game** | `fable` | `.claude/agents/valoria-critic.md` — `tools: Read, Grep, Glob` | **structural**: no Write, no Edit, no Bash. A sentence in a prompt saying "you are read-only" restricts nothing; the agent definition does |
| Curation and authorship | `opus` (orchestrator) | Parts A, B, C | every decisive claim re-verified by hand against the working tree before being carried |
| **Adversarial attack on the consolidation** | `fable` | `valoria-critic` — `Read, Grep, Glob` | **structural**: dispatched with Part D's claims and not the reasoning behind them; seven claims attacked against the tree |
| **Adversarial attack on the plot** | `fable` | `valoria-critic` | **structural**: same seat, dispatched on correctness, logic, breadth and depth of the primitive ledger |
| Consolidation, plotting, the reverse ledger, and the rewrite | `opus` (orchestrator) | Parts D, E, F, and the revisions to A and B | each surviving attack verified at `file:line` before being carried; each failed attack discarded |

**Tiering rationale** (§10's downgrade triggers): the inventories are bounded extraction over known
paths → `sonnet`. The NERS passes weigh competing design considerations against ratified canon and
gate a result → `opus`. The interrogation is the audit/guardrail node where *"being wrong is
silent"* → `fable`, used as an upgrade trigger on one node rather than as a fan-out default.

**Agonist→antagonist was run as a relay, not a dialogue** (§10): each stage was dispatched with the
prior stage's **output** and not its reasoning, and the orchestrator reconciled. `02_PROPOSALS.md`
carries that structure into the document itself — every proposal is stated by an agonist, attacked
by an antagonist, and reconciled with its residual left standing.

---

## §2 · EXECUTION ARTIFACTS — run on this tree, 2026-09-12, pasted rather than characterized

`skills/ners/SKILL.md` §10: *"The grade is the one row you cannot fill in by writing. Run something
and paste what it said."*

```
$ python -m engine.season.harness.register --requirements
THE NINE (9 rows, ruled Jordan, 2026-09-05, ED-IN-0204)
  met 1 · not_met 4 · partial 4
    R-01  not_met  decisions must propagate
    R-02  not_met  decisions affect subsequent decisions
    R-03  met      seasons must tick scene-by-scene
    R-04  not_met  strategic and management actions must be possible
    R-05  not_met  all verbs must be built out
    R-06  partial  characters must be robustly built with goals, ambitions, convictions
    R-07  partial  characters must have memories and feelings and attitudes and relationships
    R-08  partial  decisions must not be omniscient and perfectly rational
    R-09  partial  chains of events within a scene are probabilistic, not deterministic
```

```
$ python tools/m1_acceptance.py --summary
  verdict: NOT MET      2 row(s) failing
  ● Stub invocations on the M1 path == 0                    2  FAIL
  ● Same seed -> same KeyLog.content_hash()          641aa8c55c3e…  PASS
  ◐ Every emitted key has a consumer or declared terminal        —  PARTIAL
  ● All M1 junctures execute                              0/7  FAIL   ⚠ DOC-DERIVED
  ○ N seeds, zero invariant violations                      —  BLOCKED
```

```
$ python -m engine.season.harness.corpus_run
  RANKING DISCRIMINATION   16..22 of 28 candidates carry a nonzero conviction score;
                           the rest TIE and the tie is broken BY THE DRAW (U4/H-96)
  DISTINCT WORLDS RUN      89
  DISTINCT EXECUTED SETS   25
  DEGREES RESOLVED         {'Failure': 386, 'Partial': 60, 'Success': 37}
  VERBS THAT EXECUTED      11 of 38
  NPC  (46 cases)   RUNS = NOT-COMPUTABLE
  ARC  (97 cases)   ENDS = NOT-COMPUTABLE
  CONTROL — planted cross-person edge: R3 False -> True  (the detector works)
```

```
$ python -c "build_world(0) …"
  persons 3 · live `hold` tenures 0
  stance     {p_carin: [], p_bailiff: [], p_warden: []}
  capability {p_carin: {},  p_bailiff: {},  p_warden: {}}
  verb rows  38
```

**The measurement the set turns on** — `opening_set` instrumented across the corpus run, with the
person-id set collected from the harness's own `build_at` rather than inferred from an id prefix:

```
$ # patch engine.season.decision.options.opening_set (and choose's direct binding), then run corpus_run
distinct person ids built across corpus:      3
opening_set calls                      :  6,714
candidates formed                      : 177,170
  subject == the asker                 :  17,400
  subject == a person OTHER than asker :        0
```

This is the falsifier the read-only node named for its own headline claim — *"`TRACE` on
`opening_set` shows a non-self person subject in at least one corpus world; today it must show
zero."* **It shows zero**, and the 17,400 self-subject candidates are the control: the detector sees
person ids reaching candidate subjects, and sees that every one of them is the asker.

**[computed]** — exact enumeration over all 100 two-die outcomes, at the shipped fixtures
(`pool_default=2`, `obstacle_default=2`, `data/fixtures.py:358-360`), through the **discrete**
`roll_net` path the season seam imports:

| band | share | |
|---|---|---|
| FAILURE | **74%** | |
| PARTIAL | **19%** | against the 41–45% D1 §I.2 measures for PbtA and Blades across their whole competent range |
| SUCCESS | **7%** | |
| OVERWHELMING | **0%** | reachable nets are `[-2 … +4]`, so max margin is **+2**; the band needs **≥3**. **Unreachable, not rare.** Pool 3 is the smallest that admits it |

**Confidence.** `[CONFIDENCE: high]` for the enumeration — it is exhaustive over the outcome space,
not sampled. `[CONFIDENCE: high]` for the four tool outputs, which are pasted. The 74/19/7/0
figure and the measured `Failure 386 / Partial 60 / Success 37` are **not the same population** and
are not presented as agreeing: the corpus figure mixes two prizes (`tell`'s *a standing* and
`kill / wound`'s *the body*, the only two rows declaring `contests:`). The claim both support is the
one that matters and is exact in the enumeration: **OVERWHELMING is unreachable at the shipped
fixtures.** `[GAP: the ~6-point difference between the computed and measured FAILURE share is
unreconciled; candidate causes are the second prize, `obstacle_refusal_multiple`, and person-subject
obstacles reading `capability/2`. Not load-bearing on any claim made here.]`

---

## §3 · CORRECTIONS — made to this session's own work, and to the passes it commissioned

`skills/ners/SKILL.md` §9a: *"A self-retraction in one section is the pass at its best. The same
operation not run on the other sections is the pass at its most misleading."* Eight were made —
six to this session's own work, two to the passes it commissioned.

**3.1 · To the orchestrator's own working thesis, before it reached this document.** The move
identified early as highest-value — *an outcome writes `Person.stance` through the existing
degree-keyed column* — **is already planned**, as `U5`/`W-F`
(`workplans/2026-09-09-r-execution-plan.md:1324`), specified down to the YAML with its guardrails,
acceptance, falsifiers and control arms written. Proposing it as new would have been exactly the
failure `SKILL.md` §3 disqualifier 3 names. **It is not claimed here.** What is proposed instead is
the thing that plan declares it lacks, in its own words: *"The magnitudes are INVENTED and this row
is what makes that lawful."*

**3.2 · To the orchestrator's claim that `witness.py` mints `value=True` for everyone.**
**Too wide.** There are **two** deposit channels: the event-kind claim carries `predicate = e.kind,
value = True`, and the `W-B` observation channel carries a real value in the `LedgerReader`
vocabulary — `stores:<kind>`, `condition`, `contain.path:<to>`. This matters in the favourable
direction and was corrected before it could score a finding the wrong way: **Valoria has stale
information**, D1's requirement #10, and the original claim would have hidden it.

**3.3 · To the orchestrator's `stance` finding.** Verified and **widened**. It is not a `stance`
defect; it is `H-62`, six rows, one hole. Six separate findings became one, which is why
`02_PROPOSALS.md` has five entries rather than a list.

**3.4 · To the orchestrator's reach-bottleneck claim.** The route list is **three, not four**:
`succeed`'s subject is a Rung, so its Tenure is filed unowned and never enters any person's reach
set. The tree's own prior pass had already struck this and the correction is taken from it rather
than re-derived. And the constraint is **stronger** than first stated — the four verbs are outside
`resolvable_verbs()` entirely, so the block is at the **grammar**, not at the effect table.

**3.5 · To a commissioned pass, on `emits_by_degree`.** One audit reported it as having **zero
callers**, citing `H-113`. **That citation is stale and the claim is false.** Verified first-hand:
`engine/season/data/verbs.py:151-170` `emits_at(degree)` and `:172-204` `writes_at(degree)` are
live readers that **raise** when a contested verb is folded with no degree, or with an undeclared
band — *"an ABSENT degree RAISES rather than falling back to the union"*, *"a missing branch is a
hole, not a full write"*. This correction runs **in favour of** the proposal set: the degree-keyed
interior-write machinery is not merely declared, it is implemented and defended.

**3.6 · To a commissioned pass, on the faction defection penalty.** One audit quoted
`faction_politics_v30.md` as *"drop 3 ranks or to Standing 1, whichever is higher."* The source says
defection is graded **severe, 2–3 ranks** (ED-776), with no intermediate-rank pass-through, mentors
voided immediately, and Hall Tier and Livery cleared within a season. Quoted correctly in
`01_THE_PASSES.md` §2.3.

**3.7 · To this document's entire proposal ordering, by the interrogation.** The first draft of
`02_PROPOSALS.md` led with `tie / knot`'s effect body as **the reach channel**. The read-only node
showed that is wrong: `tie / knot` binds its Tenure to the act's subject, which is a question
referent, which is never a person — so the effect would open edges to rungs and propositions and
change nothing about who can reach whom. **`P2` is demoted in place and the demotion is left
legible** rather than the draft being rewritten to look as though it had always said so. The same
finding demoted `W-F` from *the thing to warrant* to *a producer whose consumer does not yet exist*.

**3.8 · To the orchestrator's reading of the claim-deposit path.** An earlier reading held that a
claim mint at WITNESS *"is not a `w.write()` call site"* and therefore bypassed the gate. **It is
one** — `witness.py:145`. The conclusion it was offered for survives, on a better warrant, and the
correction is carried in §5 rather than silently repaired: the gated pair is
`(Person, claim_ledger)`, and a `Claim`'s fields are set upstream of it.

**One claim of a commissioned pass is recorded as overstated rather than wrong.** A pass presented
`AX-5`'s three world motions as closed — *"Three is a stipulation."* The axiom's own text continues:
*"⚠ **AND THE LIST MAY BE INCOMPLETE — THERE IS A FOURTH CANDIDATE THIS DOCUMENT NEVER NAMED**"*
(CENSUS), which it then resolves by ruling CENSUS demand-driven. The refusal of a fourth clock
stands; presenting the list as never having been questioned does not.

---

## §4 · SOURCE TIERS

**The documents.** All seven are secondary syntheses over game systems, and four of the seven say so
about themselves. Two of the seven are **earlier revisions** of documents also supplied in a later
form; where they differ the later revision governs, being better-sourced (17 provenance tags against
0, `04_CONSOLIDATION.md` §1). All seven are pinned there by SHA-256 prefix and byte length, since
none is in this repository and the claims about their relationship are otherwise unverifiable. D3 §7.2: *"With the sole exception of Pax Pamir's rulebook, every mechanic here is
a player-facing account of a closed system… This is a catalogue of **folk models** — accurate to how
these systems present themselves, not necessarily to how they are implemented. For design transfer
that is largely acceptable… It is **not** acceptable for any claim about a specific constant."*
D2 §6.2 says the same and adds *"None of the six proposals has been played."* D1 flags
`[TIER-FLOOR: T2 — community wikis]` on every numeric constant in §§II.2, III.2–III.4, IV.2.

**The consequence for this set, and it is the whole of §2 of `02_PROPOSALS.md`:** the documents are
admitted as evidence for **directions** and refused as evidence for **magnitudes**. Every number
they carry stays `[OPEN — Jordan tuning]` (`SKILL.md` §11: *"Parameters are Jordan's. The form is
the audit's business; the values are not."*).

**The tree.** Every Valoria claim in this set is cited at `file:line` and was read from the working
tree, not from memory or from a prior session's summary (`CLAUDE.md` §2). Ratified canon is cited by
its ED; a `## Status:` line on a `.md` is treated as **reference and never as a mechanism**
(`CLAUDE.md` §0.05), including where it says CANONICAL.

---

## §5 · WHAT COULD NOT BE ESTABLISHED

Stated plainly rather than left to be found.

- **Whether the provenance repair (P1) is *sufficient*, as opposed to necessary.** `standing_of`
  pairs `told_by` claims **about p** against p's own firsthand claims about p. A telling about B
  deposits a claim with `subject == B` into every observer's ledger
  (`engine/season/epistemic.py:133-137`), so the route exists — but it goes live only where **B is
  among the telling's observers** under the shipped `all_five` fan-out. Not measured here.
- ~~**Whether `(Claim, source)` needs a write-matrix row.**~~ **ESTABLISHED — and the first
  statement of it in this session was wrong in a way worth recording.** The claim deposit *is* a
  gated write, contrary to an earlier reading: `engine/season/loop/witness.py:145` calls
  `w.write("claim_ledger", WriteClass.INTERIOR, lambda: p.ledger.append(c), record_kind="Person",
  fieldname="claim_ledger", …)`. But the gated pair is **`(Person, claim_ledger)`**, not
  `(Claim, source)` — `write_matrix.yaml:168-174`, steps `[WIT]`, class `INTERIOR`,
  `social: false`, emits `claim.deposited`, with the warrant *"DR-3 · §20 makes `witness` the only
  minter, **and it is not an act**."* A `Claim`'s own fields are set at construction, **upstream of
  the gate**. So stamping `source` differently touches no matrix row, needs none, and cannot refuse.
  **And this is what distinguishes P1 from `H-62` and keeps it lawful:** P1 is not an act writing an
  interior — it is the declared minter stamping what it already mints. `H-62`'s six rows are all
  `social: true`; this one is `social: false` precisely because witness is not an act.
- **The corpus-scale fork rate.** `requirements.yaml` R-01 records its own `~4%` as *"stale in an
  unknown direction"* pending a chunked re-run that this session did not perform. No claim here
  rests on it.
- **`firsthand_via_knot` reachability.** It is declared and minted conditionally on a live `knot`
  Tenure; with no effect on `tie / knot`, no corpus world has one. So the branch is **unobserved**
  rather than shown absent.
- **Whether the conviction correlation is a matrix defect or a seeding defect.** `U3` measured both
  arms — re-seeding 1–3 convictions per person raised distinct axis directions 13 → 80 of 86 and
  **did not recover the executed sets**. That is `ED-IN-0214` and it is Jordan's; nothing here
  re-opens it.
- **`pytest` was not re-run inside one commissioned pass's container.** That is a container
  artifact, not a fact about `main` (`CLAUDE.md` §0.4's known-red note). The instruments in §2 were
  run by the orchestrator in this session's own container.

---

## §6 · WHAT IS NOT CLAIMED, AND WHOSE IT ALREADY IS

`CLAUDE.md` §0 requires that a finding be tested against five gates before it is flagged for Jordan,
and that a finding needing no ruling be fixed or dropped. **This set files no new `needs_jordan`
row.** Two candidates were tested and closed:

- **The conviction-matrix re-centring** closes at gate 1 — it is already `ED-IN-0214`, allocated,
  open, and Jordan's. D1 §VIII.3's quantified variety trap is independent corroboration for it and
  changes nothing about who answers it. Re-filing it would be the queue-formation §0 forbids.
- **A dual-scoring-mode transplant** (D2's E2, the document's own "most portable single rule")
  closes at gate 5 — it requires a scored event, R7 forbids the aggregate that would be scored, and
  the architecture has a cheaper answer to the live half of `R-08` already named as build work
  (`H-96` / `H-66` / `U3`). It is refused by composition, not by a live two-option design choice.

**And these are already planned or ruled; this set names them and does not re-propose them:**

| | whose it is |
|---|---|
| `W-F` / `U5` — an outcome moves `Person.stance` | planned, `workplans/2026-09-09-r-execution-plan.md:1324`, specified to the YAML |
| `H-71` — `remit:` evaluable person-side | a tier-0 register row; one commissioned pass calls it *the single highest-value object in the tree* |
| `H-62` — a verb writes an interior | Jordan's R7, in his own words: *"unavoidable and first-rank"* |
| `ED-IN-0214` — the conviction matrix | Jordan's |
| `ED-PC-0036` — `UPSET_FLOOR`'s existence | Jordan's. The *defect* it produces is not — see `02_PROPOSALS.md` P4 |
| The director, the meter, salience, the fourth clock, auto-allocation, magnitude carriers | ruled out — `01_THE_PASSES.md` §4 |
