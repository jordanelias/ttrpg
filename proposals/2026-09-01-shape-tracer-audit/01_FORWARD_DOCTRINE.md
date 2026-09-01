# 01 · THE FORWARD DOCTRINE — resolution, configuration, testing

## Status: **PROPOSED (2026-09-01). HELD BACK IN FULL.** Reference, never mechanism (`CLAUDE.md` §0.05).

Derived from `00_AUDIT.md`. For a project **iterating and configuring a game design**, not shipping a
Python library. **This is not a plan and must not become one** — `HANDOFF.md`: *"If you are about to
write a new plan instead of taking a step, that is the loop; take the step."*

---

## §0 · START HERE

**Most of this doctrine already exists in the tree, unratified.**
`systems/_architecture/decision_policy_v1.md` has been `DRAFT FOR RULING` since 2026-07-31, with a
loud banner suspending merge-ratification and §3 carrying `NO DEFAULT`. Its own §0 states the
diagnosis: *"The queue does not drain because nothing tells it how to resolve itself."*

**The highest-leverage act available is not writing anything. It is ruling that document, row by
row** — especially §3. Every conflict resolution below leans on its §2 precedence order.

---

## §1 · THE FOUR KINDS, AND WHY THEY MUST NOT SHARE A QUEUE

The tracer's typed-refusal vocabulary is the right taxonomy: each kind has a different resolver, a
different landing surface, and a different failure mode when left open. A single "open issues" list
mixes them and therefore drains at the speed of its hardest member — which is how a 156-row queue
forms.

| kind | the resolution IS | lands in | defended by |
|---|---|---|---|
| **GAP** (`UNSPECIFIED`) | a design decision — **split FORM from VALUE**; form is usually answerable from precedent, value is sometimes genuinely Jordan's | the naming doc's spec; on adoption a `references/*.yaml` row behind an exporter | defining it at the **invocation site** as well as in prose |
| **CONFLICT** (`COLLISION`) | an adjudication + a **recorded supersession** | `registers/supersession_register.yaml` (`superseded_id / superseded_by / replacement / files_to_recheck`) | the `files_to_recheck` list; ultimately, one owner that code reads |
| **EXCEPTION** (`FORBIDDEN`) | **accept the cost** (the case is not expressible, on purpose) or **amend the law knowing the blast radius**. There is no silent third option | accepted cost → closed ledger row + a note beside the law; amendment → the law's own home | an executable falsifier: a test asserting the refusal still raises |
| **MISSING PRODUCER** (`NO-PRODUCER`) | a **wiring choice**: which step, which write class, which owner | `references/module_contracts.yaml` + the emitting module | the resolution *is* an execution artifact — a test that runs the write |

**While a GAP is open, `raise Unspecified` is CORRECT BEHAVIOUR.** Do not invent a placeholder. This
is the one thing the tracer got right and then violated with its own constants.

### R1 — an unlocatable ruling is a claim, not a ruling
A `# per Jordan` comment with no date, quote or ID has *evidentiary* weight — never delete it,
deleting a real ruling re-opens a settled question — but no *adjudicative* weight. Quarantine it:
keep it visible, mark it "claimed", escalate the one-sentence question. Without R1, any unlocatable
annotation outranks cited canon forever, which is the incentive that produces annotations instead of
ledger rows.

### R2 — "already built" cuts both ways
Jordan, this session: *"It doesn't matter if anything was already built — it only matters if it was
built extremely well."* That strips incumbency as a **defence** and as a **disqualifier**,
symmetrically. It does not license mis-citation: a proposal presenting a live mechanism as absent is
a provenance defect regardless of which version wins. **Cite the incumbent, then argue quality.**

---

## §2 · THE LADDER AND THE ESCALATION GATE

Before anything is flagged for Jordan — or left flagged — walk `CLAUDE.md` §0's ladder:
**1** superseded · **2** irrelevant · **3** answered by a design document (take partial answers —
a doc that settles *form* but not *value* has done most of the work) · **4** answered by precedent ·
**5** answered by what makes sense architecturally (take it, and record the reasoning).

**A row may carry `needs_jordan: true` only if its description states:** (a) the question in one
sentence, (b) why each of steps 1–5 fails, **(c) a proposed answer with its evidence.**

(c) is load-bearing and usually missing. The measured pathology was **answer-poverty, not
question-scarcity**: of 85 sampled rows, 83 carried a source pointer and 10 a proposed answer.
A question with a proposed answer is a two-minute confirmation; without one it is a work assignment.

**IDs.** A resolution that changes what a later session should believe gets an `ED-<LANE>-NNNN`
(allocate from `references/id_reservations.yaml` — `next_free`, bump, co-commit). **A gap in a
PROPOSED architecture does not.** The tracer's 47 rows stay in `gaps.json` and travel with the
proposal; the *adoption decision* gets one ID. Forty-seven EDs for an unratified architecture would
rebuild the queue in a new location.

---

## §3 · CONFIGURATION — DECLARE, DON'T ROUTE

Nearly every audited defect was the same shape: **something load-bearing living somewhere with no
mechanism behind it** — a hand-typed Partition dict, a corpus of chat transcripts, routing by regex
over English, constants as literals, a gap register of prose with no tree anchor.

### The pattern already proven in-tree (eight instances)

```
authored surface  references/descriptor_registry.yaml   hand-edited, rulings inline beside their rows
      ↓
exporter          tools/export_descriptors.py           THE SOLE PARSER; validates at export time
      ↓                                                 blocking --check round-trip in CI
typed artifact    engine/engine_params/descriptors.json _generated banner + schema_version
      ↓
leaf reader       engine/substrate/descriptors.py       stdlib-only; RAISES on a non-member
      ↓
consumers                                               pinned by a single-owner test
```

Four properties make it work, each earned by a recorded failure: **one parser**; **export-time
resolution** (a typo reds CI, not a campaign run); **loud readers** (`require(role)` is deliberately
not `get(role, default)`); and **coverage checks that quantify over the registry-derived side** —
a coverage check that once iterated a *hand-maintained* binding dict made its own docstring false as
shipped. **Every hand-maintained binding map inside an exporter is a miniature Partition table.**

### What to configure

| thing | authored surface | reader | the check asserts |
|---|---|---|---|
| **write matrix** | two blocks authored once each, merged by the exporter never by hand; every row carries `status: ruled\|unruled\|deliberately_absent` and a `source:` | the write gate; later the Godot gate | fields resolve by reflection; ruled rows covered or explicitly `unruled`; declared absences match; round-trip |
| **case corpus** | one YAML per case, ids from **disjoint reserved blocks** (`id_reservations.yaml`'s own header: disjoint blocks make collision impossible by construction) | the case runner | ids unique corpus-wide; parses as YAML from byte 0; classifier inputs in a declared separate role |
| **routing** | a `capability:` tag per need, closed vocabulary | a dict lookup | every tag declared; every probe reachable; unparked capabilities map to a probe |
| **constants** | rows with `grade: measured\|ruled\|assumption`, owner, citation | one params reader; later Godot | no bare literal outside the reader; assumption-grade never cited as measured; **no silent defaults** |
| **gap register** | **none — generated only** | session triage | every `resolves_to` resolves; a `NO-PRODUCER` row executed a predicate |

**Don't route — declare.** The 114-line regex router is an inference engine reconstructing a fact
**the case author knew at authoring time**: which mechanism this need exercises. Hence seven
mis-route defects, a 46% miss rate, 11 unreachable probes. The same shape was solved once already:
the engine names a ROLE, `module_contracts.yaml` names the MODULE, the resolver raises on undeclared.
The unrouted 46% then becomes a **countable authoring queue** instead of a diagnosis problem.

**The constants case is sharper than "invented numbers".** `11_PARAMS.md` is already the
specification of the config-first answer — it rules that a value the engine uses lives where code
reads it, and that `COND_SCALE` is *"never a literal in a source file."* The tracer violated its own
suite's params doctrine. The fix is not better numbers; it is a **grade** per row. The sin was never
that 1000 is wrong — it is that a guess carried no grade.

### The boundary tests

**Stays code** unless it passes all three: (1) a total function from a small enumerable key domain to
plain values, no control flow; (2) changing it needs a design decision but no new mechanism;
(3) validatable without executing it. **The moment a registry row wants an `if`, stop** — you are
writing a worse programming language in YAML. Over-configuring has a live local failure:
`atomization_rules.yaml`'s `force_skeleton_routing_for_design_docs` had **zero readers**.
Configuration nothing reads is prose with worse ergonomics.

**Stays prose:** rationale, ruling history, worked failures, intent. Test: *delete the document; does
the game behave differently?* The registries show the correct hybrid — mechanism in rows, rulings
verbatim in comments **beside the rows they govern**, so prose travels with the data it explains.
**Prose may state a number only with its grade and its owner pointer.**

---

## §4 · TESTING

### Three tiers, with entry criteria

| tier | when | entry criterion |
|---|---|---|
| **0 — blocking** | every push, <~2 min | all three: **(a)** load-bearing on the engine, exported params, the port, or a Jordan decision; **(b)** deterministic with a committed baseline; **(c)** can only red on *regression*, never on arrival |
| **1 — on demand** | before *believing* a claim | you are about to write "X is true of the design" into a ledger, PR body or report |
| **2 — deep check** | pre-ratification, or before a golden re-pin | a `PROPOSED` artifact is a ratification candidate |

**What NOT to test, as binding as the rest.** No behavioural unit tests for `PROPOSED` mechanics —
they encode your model of a design that will churn, and each becomes a re-pin chore. No goldens on
proposed numbers. No guards on apparatus-only artifacts. **Do not wire proposal-tree exporters into
blocking CI before ratification** — that makes unratified material load-bearing. (One exception: a
cheap syntax/import check on a proposal's executable instrument is not a semantic gate, and a
bitrotted instrument that still reads as evidence is the failure that already happened.)

### The evidence standard — one fillable block

Enforcement already exists: a blocking validator demands `MEASURED-BY:` on quantitative ledger
claims. So this lives in the ledger entry and the commit message, not a new document.

```
CLAIM:       one sentence, with the number
MEASURED-BY: exact command, seed included
CONTROL:     what the other arm was — never "n/a"
FALSIFIER:   the check that would show this wrong, AND ITS OUTCOME
ARTIFACT:    a hash or pinned value a reader can re-derive
```

**A block with an empty CONTROL or FALSIFIER is not a claim; it is a hypothesis, and it gets written
as one.** The tracer's fifteen unasserted `"OK: …"` strings are claim blocks with four of five fields
blank.

### Anti-vacuity: three mechanics

The existing vacuity detector quantifies over *assert nodes* — so a probe with **zero** assertions is
invisible to it by construction. That is the audit's worst finding.

1. **Assert that you asserted.** A probe returns PASS only through a `checked(predicate, why)` helper
   that increments a counter; the harness refuses PASS at `checks == 0`. Ten lines; makes the defect
   structurally impossible rather than reviewable.
2. **The mutant run.** Run the PASS set against a world with the resolver stubbed to a no-op. **Any
   probe still passing is vacuous, mechanically.** Run today it fails all fifteen at once — because
   the resolver already mutates nothing. The check and the defect are the same fact from two sides.
3. **Absence claims need a positive control.** A `NO-PRODUCER` verdict is admissible only from a run
   where (a) the field did not change across a season **and** (b) a sibling field with a known
   producer *did* change in the same run. Without (b) you cannot distinguish "no producer" from "the
   loop didn't run". `UNSPECIFIED`/`COLLISION` are exempt — a spec hole cannot be executed.

**The polarity rule:** zero evidence maps to the verdict **against** the thing being measured —
UNKNOWN or BLOCKED, never PLAYABLE. Find the default branch of every verdict function and check which
way it falls. That single rule would have contained the audit's entire root defect.

### The reproducibility ritual

**Untrack generated artifacts and build them in the test**, per culling wave 5: *"their `--check`
modes existed to detect a STALE COMMITTED COPY. With nothing committed there is no staleness to
detect."* The stated exclusion is **runtime inputs** read at import. But note the tracking decision is
secondary — **the loader silently overwriting on duplicate id is the real root cause**, and that fix
is required either way:

- **Fail loud on input surprises.** A duplicate id must raise. Unknown field names must raise at load.
- **One writer.** The artifact header names its generator.
- **The self-test must regenerate, not read.** A test that reads a committed artifact is exactly the
  test that passes on stale data and fails when its own generator runs.

### Testing a design that is still moving

1. **Calibrate the instrument before believing any verdict.** Before a real verdict is admissible the
   harness must pass a synthetic suite: a known-BLOCKED case that must not score PLAYABLE, a
   known-PLAYABLE that must not score BLOCKED, a planted-vacuous probe the mutant run must fail, a
   duplicate-id corpus the loader must reject. That suite catches the root defect, the unasserted
   passes and the polarity bug **before** a design conclusion ships.
2. **Report the four refusal counts; never pin them.** An iteration resolving three gaps and creating
   one is progress; a golden would punish it.
3. **Never invent a constant — parametrize and sweep.** Where the params doc refuses a value, the
   honest verdict is `UNSPECIFIED`. Where a probe needs a number to run, inject it and run a 3-point
   sensitivity sweep. **A verdict that flips across the sweep is itself a finding.**
4. **Reachability is structural and cheap** — fifteen lines of set difference.
5. **Ratification requires an execution artifact.** The proposal graduates when the calibrated
   instrument runs the *actual corpus*. Until then verdicts stay labelled advisory — and "advisory"
   must be glossed as **"never ran"**, because the softer word demonstrably misleads.
6. **Before claiming something does not exist, grep the adjacent subsystem.** The two most expensive
   recurring failures — a reversed citation and a live mechanism re-presented as missing — are both
   this. **A claim of the form "X does not exist" carries a grep transcript in its FALSIFIER field,
   or it is not admissible.**

### The standing controls

| measurement | its control |
|---|---|
| "Mechanic X moved balance" | same-process two-arm patch, same seeds. For a campaign-unreachable change both arms are identical and running it is a *fake* control |
| "This run is deterministic" | fixed declared seed + a content hash a reader re-derives |
| "Artifact matches generator" | in-process regenerate; or untrack and build (preferred) |
| "Y caused the divergence" | **ablation** — remove Y, re-run, compare. The single most decisive act of this review |
| "This detector works" | planted fixtures in *both* directions, plus mutate the guard and require red |
| "Nothing writes this" | a positive control: a sibling with a known producer changes in the same run. **Nothing owns this today** |
| detector precision | at least as many must-NOT-flag cases as must-flag |

---

## §5 · WHERE TO START

1. **Rule `decision_policy_v1.md`, row by row** — especially §3 (`NO DEFAULT`). The only item that
   makes the queue drain itself.
2. **Case schema, reserved id blocks, rejecting loader.** Half a day; makes the root defect
   unconstructible rather than fixed.
3. **The polarity rule and `checked()`.** Two small mechanics that kill the unasserted-pass class and
   the fail-toward-the-shape class permanently.
4. **Capability tags; delete the router.** Converts a diagnosis problem into a countable queue.
5. **Owner column on the gap register** — grep-backed with `file:line`, never prose. **This decides
   whether ~45 rows are game-design work or a generator of parallel-dialect work items.**
6. **Params rows with grades.** Mechanical; the params doc already wrote the ledger.
7. **Write matrix registry; make the gate apply the write.** The one item with real code work, and
   the one whose config surface must cross into Godot.

---

## §6 · THE ESCALATIONS THIS WORK IDENTIFIES

Named here, **not filed** — filing is a separate act under `CLAUDE.md` §0's one-row gate.

- **`decision_policy_v1.md` §3** — the rank of metaphysical canon, deliberately `NO DEFAULT`.
- **The unpriced reversal** in the unified shape's §4.2, marked *"Jordan's call, not mine"* and
  overturning four named rulings. Of the corpus's two Jordan-facing questions this is the
  escalation-worthy one; §6.1's ambient-social question says of itself that at three arcs it *"may
  not be worth Jordan's time at all"*.
- **TS 12 vs `ts: 15`** — a one-sentence confirmation, with 12 as the proposed answer.
