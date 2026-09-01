# 00 · THE AUDIT — PR #351's shape tracer

## Status: **PROPOSED (2026-09-01). HELD BACK IN FULL.** Reference, never mechanism (`CLAUDE.md` §0.05).

Target: PR #351, merge `32bd13e`. 26,090 insertions / 0 deletions, 59 files, entirely additive under
`proposals/`. ~3,018 lines executable Python; ~12,743 lines generated + case data; ~10,329 prose.

---

## §1 · THE BOTTOM LINE

**The probe layer is sound work. The case layer is not a measurement. One defect explains the whole
discrepancy, and it has a one-line fix.**

- **What executes:** 65 probes, deterministically — 80 acts, 117 events, 337 class-checked writes,
  47 typed gap rows. `gaps.json` regenerates byte-identically.
- **What never executed:** none of the 78 corpus cases. Their verdicts are keyword lookups into
  cached probe results; all 78 trace sections are bare headers. The PR labels case verdicts
  "advisory" in three places and deserves credit for that — but "advisory" reads as *crude*, not as
  *never ran*, while the title and `01` §1/§2 promise per-case seasons.
- **The repository suite is green and this PR regresses nothing** — verified at
  `1777 passed, 23 skipped, 15 xfailed` on a default run.

## §2 · THE ONE ROOT DEFECT, ISOLATED BY CONTROL

`load_cases()` globs `cases/*.yaml`; `per_case` is keyed on the bare `c["id"]`, last writer wins, no
dedupe. `ENDINGS_CLASSIFIED.yaml` — a classifier **input**, not a case lane — reuses `ARC-01…ARC-50`
and sorts after `ARC1/2/3.yaml`:

```
total case entries: 128   distinct ids: 78   COLLIDING ids: 50
lane of LAST writer: ENDINGS_CLASSIFIED 50 · NPC3 10 · NPC2 9 · NPC1 8 · ARC2 1
```

Its rows carry no `season_requires`, and a zero-row case scores **PLAYABLE** — the most flattering
verdict available. So the collision deletes the arc corpus *and* converts ~40 `BLOCKED` arc verdicts
to `PLAYABLE`.

**THE CONTROL THAT ISOLATES IT.** Set that one file aside and re-run:

```
$ mv cases/ENDINGS_CLASSIFIED.yaml /tmp/ && python3 run_cases.py && diff results.json <committed>
== 78 cases loaded ==
IDENTICAL — committed artifact fully reproducible from committed-inputs-minus-ENDINGS
```

**No code drift, no nondeterminism, no hand-editing.** The committed `results.json` is a faithful,
exactly reproducible output of the committed code over the corpus minus one misplaced file.

Two consequences. The PR's own §7 falsifier does fire — after a fresh run the honesty test fails
(`27 passed` pristine → `1 failed, 26 passed` after a run) with *"classifier says 8 arcs close at a
threshold, runner says A2 blocks 0"* — but that divergence is **collision-induced**, not independent
evidence of decay. And the framing "the committed results cannot be produced by the committed code"
was technically true and materially misleading; it is retracted.

**§6.2 discloses a *different*, smaller collision** (two source series reusing arc numbers 16/17/18)
and names the failure mode exactly — *"Any tool indexing arcs by bare number silently merges or
discards one of each pair"* — then fixes it by namespacing to `ARC-R16…R19`. A search of the whole
proposal tree for any acknowledgement of the `ENDINGS_CLASSIFIED` overlap returns nothing.

## §3 · MEASURED FINDINGS

| # | finding | severity |
|---|---|---|
| A-1 | The id collision above; one root defect | critical |
| B-1 | No corpus case executed; verdicts are regex lookups onto cached probe results | critical |
| B-2 | "50 arcs" is 48 arcs + `EMG-10` (endgame checklist) + `EMG-11` (self-described as not an arc); `ARC-META-COLLISION` runs as a 78th case; `ARC3.yaml` opens mid-word because `extract2.py` keeps only a lane's last message | high |
| B-3 | No schema; every field read via `.get()`; a misspelled `season_requires` scores PLAYABLE | high |
| C-1 | `World.write()` validates, logs, returns `True` — and mutates nothing. All state change is direct assignment beside it; the logged value and applied value diverge (unclamped vs clamped). "Enforced by construction" is false | critical |
| C-2 | `(Person, exists)` — death — has no Partition row (15 rows measured), so the tracer cannot lawfully kill anyone; `_died_this_row` has no in-loop producer, so A12's PASS rests on hand-poking a private set | critical |
| C-5 | `ShapeGap.__init__` writes the register, so a *passing* probe deposits a gap. A12 passes and files a `FORBIDDEN`. True distinct ≤45 — the number the PR's own §1 table prints beside kinds summing to 47 | high |
| C-6 | `leaders()` raises `UNSPECIFIED` calling a comparator "unadopted"; `02_ONTOLOGY.md:1210` says "Adopt and record", `08_FUNCTION_SURFACE.md:46` declares it, and a sibling tree adjudicates it adopted | high |
| C-7 | Constants invented against `11_PARAMS.md`'s explicit *"This document proposes NO VALUES"* and its ruling that `COND_SCALE` is *"never a literal in a source file"* | high |
| C-8 | The showcase PASS (P12) writes its outcome by hand after `loop.run()` returns, outside any step — violating the tracer's own fidelity rule 2. Four further passes assert capabilities never exercised | medium |
| D-2 | 11 probes unreachable: `P13–P17`, `A7–A12`. No route can call them | high |
| E-1 | CI reads `proposals/` (a blocking validator walks it) but **no gate executes the tracer, its self-test, or validates artifact freshness** — not even a syntax check | medium |

### The gap register, measured

By AST walk over the 65 probes:

- **45 gap-producing probes.** Roughly half raise **unconditionally** — 23 by careful hand
  classification, 28 by a stricter "no guard present" heuristic; ~6 originate in `shape.py`'s own
  gate or stubs; ~16 raise behind an executed predicate.
- **20 PASS/PARTIAL probes, of which 15 contain no `assert` and no conditional check whatsoever**
  (`P1, P5, F1, F4, F5, W1, A1, A3, A6, P13, A7, A11, P24, P25, A17`). A PASS means "did not crash"
  plus an author-written string. Root cause: `resolve()` mutates no state, so any PASS "through the
  loop" verifies only that an Event was emitted.

**Where the charge lands.** Not on the `UNSPECIFIED`/`COLLISION` rows — fidelity rule 2 declares
raises-as-findings for spec holes, and a hole cannot be executed. It lands on ~13 unconditional
`NO-PRODUCER` rows, whose kind asserts an *executable* absence that sibling probes prove the tracer
knows how to test with a predicate.

## §4 · WHAT IS GENUINELY GOOD

- **The typed refusal vocabulary is a real contribution.** `UNSPECIFIED` / `FORBIDDEN` /
  `NO-PRODUCER` / `COLLISION` makes design review actionable. Keep it whatever happens to the rest.
- **Negative space handled honestly** — 243 of 527 needs (46%) reported `UNMAPPED` rather than
  passed; under-covered cases `NOT-ASSESSED` rather than graded.
- **Crashes are not laundered** into findings (`TRACER-ERROR`, with a self-test asserting none).
- **The PR labels its own two weakest layers**, keeps retractions in the text, and ships per-claim
  falsifiers including one saying "the old falsifier here tested the wrong thing".
- **Nine instrument defects found, fixed and regression-pinned during the run**, three by read-only
  audits, then analysed for *direction* — concluding a crude instrument systematically overstates a
  strict design's cost and instructing the reader to treat its counts as upper bounds.
- **The escalation was narrowed rather than inflated** — eight arcs to three.

## §5 · WHERE THIS AUDIT WAS WRONG, AND CORRECTED

Established by three adversarial review lanes attacking this audit's factuality, inference and
method. Recorded because the correction record is the point.

- **Retracted in full — the "TS 12 fabrication" charge.** `npc_roster_v30.md:260` and
  `faction_canon_v30.md:570` both say TS 12; `references/npc_registry.yaml:107` says `ts: 15
  # per Jordan`, and its own `source:` points at the roster it contradicts. The case lane invented
  nothing; this is a tracked canon-vs-registry conflict, not this PR's defect.
- **Retracted — "≥56% authored" and "exactly 1 of 47".** Unreconciled arithmetic, and false in both
  directions. Replaced with the measured counts in §3.
- **Corrected — "CI reaches none of it".** A blocking validator does walk `proposals/`. Established
  originally by a term-grep, this repo's named costliest error class.
- **Corrected — "the committed results cannot be produced by the committed code".** They can,
  exactly, minus one misplaced file. See §2.
- **Corrected — "`_died_this_row` is written nowhere".** No *in-loop producer*; probes and the test
  do assign it.
- **Corrected — the rung-ladder "collision".** The tracer's 8 rung kinds and the substrate's 4
  `SCALES` enumerate different concepts (identity-bearing social containers vs the scale at which a
  Key's effect registers); the shared tokens `settlement`/`territory` were the entire appearance of
  conflict. Diagnosing it as a collision repeated the term-vs-concept error.
- **Withdrawn — "the most epistemically disciplined artifact in the repository".** An unverifiable
  superlative from a partial read.
- **Corrected mid-audit** — an earlier claim that the 27 NPCs execute while the arcs do not. Neither
  executes; routing is symmetric.

## §6 · REMEDIATION, RANKED

0. **Done, reported in §2** — the ENDINGS-removed control run.
1. Namespace case ids by lane, or move `ENDINGS_CLASSIFIED.yaml` out of `cases/`; assert
   `loaded == distinct`. **One line, and it is the whole fix.**
2. **Untrack `results.json`, `TRACE.txt`, `gaps.json`; build them in the test.** Corrected against
   culling wave 5's precedent — *"with nothing committed there is no staleness to detect."* The
   stated exclusion is runtime inputs read at import, which these are not.
3. Give the PASS verdicts assertions. 15 of 20 have none; a pass that cannot fail is not evidence.
4. Add an "existing owner in tree" column to `gaps.json` — **grep-backed with `file:line`**, never
   prose, or it becomes one more unconditional authored claim.
5. Make the write gate apply the write, or make direct assignment impossible.
6. Route or delist the 11 unreachable probes; publish the four distinct "probe count" referents.
7. Rule `(Person, exists)` in the suite's write matrix **first**, then add it to the Partition —
   order matters, or it repeats the invention its own guard exists to prevent.
8. Distinguish raised-and-escaped from constructed-and-caught in `TraceLog.gap`; recount.
9. Declare the invented constants harness fixtures; run a 3-point sensitivity sweep.
10. Fix the `leaders()` citation; hand-check the other gap rows' citations.
11. Reconcile the PR body against the artifacts: it claims 1778 passed (default run gives 1777 — the
    suite is order-dependent by one test), "20 passed" for a 27-test file, "226 of 527" vs 243.

## §7 · FALSIFIERS FOR THIS AUDIT

| finding | what would prove it wrong |
|---|---|
| A-1 · one defect, not decay | the ENDINGS-removed control producing a non-identical `results.json`. **Run: identical.** |
| B-1 · no corpus case ran | one non-empty corpus `=== CASE ===` section. **Checked: 78, all empty.** |
| §3 · unasserted passes | an `assert` or guard in the 15 named probes. **Run: none present.** |
| D-2 · 11 unreachable | a `ROUTES` entry resolving to any of them. **Checked: none.** |

## §8 · METHOD AND LIMITS

Five read-only Fable lanes, then three adversarial lanes over this audit, then re-verification by
execution. Standing limits, stated rather than hidden:

- **The original audit had no control**, and its lane briefs pre-named suspicions — which measures
  brief-compliance as much as code. Findings later verified by execution are laundered of that bias;
  the rest are marked.
- **Lane numeric disagreements** (probe count 44/51/65; `SOCIAL` rows 15/16/17) were resolved by
  re-measurement (65 and 15). Correct policy — but the disagreement was diagnostic, pointing at four
  distinct meanings of "probe count", which the first version discarded rather than reported.
- **Independent rediscovery is weaker evidence than first claimed** — all lanes read the same small
  codebase from briefs by one author. Real for the id collision (execution vs static provenance);
  weak for the gate bypass.
- **The lane decomposition excluded the headline finding by construction** — the stale-artifact
  result is discoverable only by execution, which no read-only lane could do.
- **Provenance was sampled at 8 entries, not audited.** One in eight is a sampling result, not a
  rate — and that one has been withdrawn.
- **How much `ARC3` lost is unobservable** by construction.

The working tree was restored to `32bd13e` after every execution test, including `__pycache__`
residue an earlier "byte-identical" claim overlooked. Tracked and ignored state both verified clean.

---

## §9 · EVIDENCE APPENDIX

Every claim in §2–§3 that was verified by execution or by direct reading, with the evidence. Nothing
here is quoted from a subagent without independent confirmation; where a finding rests only on lane
assertion it is marked in §8's limits instead.

### 9.1 · The instrument does run — the probe layer is real

```
$ cd tracer && python3 run_cases.py
== running probes against the shape ==
Counter({'NO-PRODUCER': 29, 'PASS': 19, 'UNSPECIFIED': 10,
         'COLLISION': 3, 'FORBIDDEN': 3, 'PARTIAL': 1})

$ python3 -c "import json; print(json.load(open('gaps.json'))['summary'])"
{'acts': 80, 'events': 117, 'writes': 337, 'gaps_total': 47, ...}
```

Two consecutive fresh runs are byte-identical; `gaps.json` regenerates unchanged from the committed
version. Determinism is structural — no RNG, no timestamps, sorted glob, `World.seed` never consumed.

### 9.2 · The repository suite is green; the PR regresses nothing

```
$ python3 -m pytest tests/valoria -q
1777 passed, 23 skipped, 15 xfailed in 411.80s
$ python3 -m pytest tests/valoria -q -p no:randomly
1778 passed          # the PR body claims 1778 — so the suite is order-dependent by one test
```

### 9.3 · The self-test passes only on stale data

```
# pristine tree
$ python3 -m pytest test_tracer_is_honest.py -q
27 passed in 0.08s

# after running the instrument's own documented command
$ python3 run_cases.py && python3 -m pytest test_tracer_is_honest.py -q
E  AssertionError: the two instruments have diverged: classifier says 8 arcs
   close at a threshold, runner says A2 blocks 0.
1 failed, 26 passed
```

The failing assertion is the one `04_UNIFIED_SHAPE.md` §7 names as the falsifier licensing the ending
classification: *"If the two ever diverge, the convergence that licenses citing an agent
classification is gone."* Per §2 this divergence is **collision-induced**, not independent decay.

### 9.4 · Committed vs fresh, before the control was run

| | committed | fresh run at HEAD |
|---|---|---|
| total probe rows | 527 | 219 |
| lane distribution | ARC2 31 · ARC1 18 · NPC 27 · ARC3 2 | ENDINGS 50 · NPC 27 · ARC2 1 |
| A2 core blockers | 9 | 0 |

### 9.5 · The corpus-case trace sections are empty

```
=== CASE ARC2:ARC-20 ===

=== CASE NPC3:NPC-001 ===
```

against a probe section, which carries a full executed season:

```
=== CASE PROBE-P1 ===
-- SEASON 1 --
  [CALENDAR]
  [MATTER]
    W    Site.condition[harbour] <- 520  class=MATTER driver=Event
  [DELIBERATE]
    call choose(carin)   (omits World)
    ACT  carin :: copy -> seam
  [RESOLVE]
    EVT  E1.0 copy @seam causes=[]
  [WITNESS]
    W    Person.ledger[carin] <- 'copy@seam'  class=INTERIOR driver=Event
```

78 corpus headers, all empty; 65 probe sections, all populated. Meanwhile `trace_log.py`'s docstring
claims the trace *"is evidence that a case ran, and in what order."*

### 9.6 · The write gate validates but never applies

```python
w.write("Site", "condition", s.id, before - WEAR.get(s.kind, 20),
        WriteClass.MATTER, driver="Event")          # logs UNCLAMPED
s.condition = max(0, before - WEAR.get(s.kind, 20)) # applies CLAMPED
```

At `condition=10, wear=40` the trace records `−30` while state holds `0`. `d.fired = True` at CALENDAR
is fully ungated and has no Partition row at all. Probes mutate freely and set `w._step` by hand to
stage steps outside the loop. The file's own header claims *"The four laws are enforced by
construction, not by convention … a write outside its class raises."*

### 9.7 · The Partition, measured by importing the module

```
SOCIAL rows: 15
has (Person, exists)?      False      # death
has (Person, capability)?  False
has (Person, convictions)? False
```

The suite rules death explicitly: *"A named person's death is the one place a Person leaves existence
without an act."* Because `(Person, exists)` is an unmarked cell, a death write raises `UNSPECIFIED`
under the suite's own *"any unmarked cell is a write-class violation"* rule. The dict also already
contains a typo — `("Rung","matter.stores")` names a field the `Rung` dataclass does not have.

### 9.8 · A passing probe deposits a gap

```
A12 verdict: PASS
 GAPROW PROBE-A12 FORBIDDEN   # the shape working correctly, filed as a gap
 GAPROW PROBE-A1  UNSPECIFIED # duplicate of F6 — dedup key includes case name
gaps_total: 47
```

Corroborated by the PR's own §1 summary table, which prints them side by side unreconciled:

```
| probes    | 65 executed attempts — 19 PASS, 1 PARTIAL, 45 gaps |
| gap kinds | 29 NO-PRODUCER · 11 UNSPECIFIED · 4 FORBIDDEN · 3 COLLISION |   = 47
```

This is one of three internal count inconsistencies. `01` §5's defect table lists **nine** rows while
its text concludes *"Six defects"*; the PR body claims *"20 passed"* for a file collecting 27.

### 9.9 · The reversed citation

```
02_ONTOLOGY.md:1210        Adopt and record rather than escalate; it is answered by the architecture.
08_FUNCTION_SURFACE.md:46  Comparator: commitment degree x backing raisable   (declared signature)
authoritative-architecture/06_ADJUDICATIONS.md:190   adopt … and record
```

against `leaders()`, which raises `UNSPECIFIED` calling the comparator *"unadopted"*. In fairness §10's
heading is "WHAT IS CARRIED AS OPEN", so the tracer had some textual footing — but item 2's body
instructs the opposite of what the raise does. Scoped correctly this is intra-proposal
misrepresentation, not canon error: everything involved is still PROPOSED.

### 9.10 · Constants against an explicit refusal

```
11_PARAMS.md:4:  This document proposes NO VALUES.
11_PARAMS.md:51: | 10 | COND_SCALE | RULED | pick 10_000 and export it.
                                             Never a literal in a source file
```

The tracer hardcodes a 1000 scale, band edges 750/500/250, a six-entry `WEAR` table with a **silent
default of 20** for unregistered site kinds, band→verb sets, and `witness()`'s `confidence=3`. `WEAR`
is the only table in the file with no citation comment — and the params doc grades `wear(site_kind)`
*"the most load-bearing unmeasured number in the game."* Since the doc proposes no values there is
nothing to re-ground *against*; the actionable form is to declare them harness fixtures and run a
sensitivity sweep.

### 9.11 · The showcase PASS writes its own outcome

```python
loop.run({"stranger": stranger_takes})
# comment claims: "the stranger's act ends Maret's hold"
w.tenures["h0"].until = w.tick                      # <- author, outside any step
w.tenures["h1"] = Tenure(id="h1", subject="stranger", ...)
```

Three ways this fails the instrument's own rules: fidelity rule 2 forbids inventing a plausible
implementation, and the act→tenure producer is exactly what is unspecified — P28 and A4 report that
same missing producer as gaps; routed through the gate these writes would raise
`Forbidden("a write outside the loop")`; and `resolve()` only emits an inert Event, so the causal half
of the claim never executed. `01` §2 calls it *"Verified by execution, not asserted."*

Four further passes assert capabilities never exercised. **P13** *"travel-in-progress ticks at
MATTER"* — nothing ticks. **F5** *"conferral and revocation are acts"* — only `confer` ran. **A6**
*"legitimacy is a Query over claims"* — no query computed. **A17** *"the second can fail on its own"* —
failure never exercised, and A17 is the sole support for ARC-06, the corpus's one PLAYABLE arc.
**P25**'s decider hardcodes `payload={"effort":"half"}`, so *"the operative's own choose returns a
weaker act"* describes a literal the author wrote into the lambda.

### 9.12 · Eleven unreachable probes

```
probes: 65    never routed: 11
['P13','P14','P15','P16','P17','A7','A8','A9','A10','A11','A12']
```

They execute and deposit gap rows, but no corpus need can reach them. A need reading "two people
marry" grades `UNMAPPED` while P15 exists and raised a real `COLLISION` — so the runner's documented
honest loop (*"read the unmapped clusters, add probes, re-run"*) mis-instructs: for these the fix is a
**route**, not a probe. This also explains the audit's own lane disagreement on "probe count"
(44/51/65): the term has at least four referents — defined (65), routed (54), gap-producing (45), and
verdict subsets.

### 9.13 · The provenance retraction, in full

```
systems/npcs/npc_roster_v30.md:260        "Inquisitor antagonist/ally. Hidden TS 12."
systems/factions/faction_canon_v30.md:570 "Sæmund Haelgrund (Inquisitor; TS 12 unrecognized)"
references/npc_registry.yaml:107          ts: 15  # per Jordan; latent Thread perception
```

The registry's own `source:` field points at the roster it contradicts, with a stamp from 2026-05-08,
and no TS ruling is locatable in `registers/`. The case lane inherited one side of a real,
pre-existing, already-tracked conflict. **It invented nothing, and the fabrication charge is
withdrawn.** What survives from the 8-entry provenance sample: 5 verified verbatim, 2 unverifiable,
this one resolved in the PR's favour. Structurally, arc-lane sources remain dead scratchpad paths or
archive captures stamped *"Not valid against any post-CP14 ruleset"*, and the brief's own `[STRUCK]`
convention was applied to two entries but not to that blanket stamp.

### 9.14 · CI reach, corrected

```
tools/ci_pp_frozen_check.py:56  SCAN_ROOTS = (..., 'proposals/', 'tools/')   # blocking gate
```

The workflow's only occurrence of the string `proposals` is a comment — which is how the original
audit reached the wrong conclusion, by grepping a term instead of tracing the concept. Validators walk
trees. The defensible claim is narrower and still serious: **no CI gate executes the tracer, runs its
self-test, or validates its artifacts' freshness**, and the syntax gate compiles `tools/*.py` only.
Four falsifier rows in the flagship document rest on a test file nothing runs.

### 9.15 · A repository-level defect this audit ran into

`.claude/settings.json` invokes the Grep/Glob guard by **relative path**:

```json
{ "matcher": "Grep|Glob",
  "hooks": [{ "command": "python tools/hook_md_sweep_guard.py" }] }
```

Any subagent whose cwd is not the repo root gets exit 2 — the BLOCK code — on every Grep and Glob.
**Four of the five original lanes lost two of their three tools**, degrading them to targeted reading.
The guard carries an inline "fail OPEN, never closed" comment (scoped to its allowlist helper, so
citing it as the module's contract is loose — the substance stands). The fix is also under-scoped: the
hook has two gates, and correcting the path does not restore the markdown-sweep patterns it blocks by
design. Separately, `CLAUDE.md` §8 still states settings.json wires the naming nudge *"and nothing
else"*, which this hook makes false.

This is pre-existing and not PR #351's defect, but it degrades exactly the structural-independence
mechanism `CLAUDE.md` §10 relies on, so it will degrade the next audit too.
