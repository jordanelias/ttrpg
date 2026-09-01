# THE SESSION'S FINDINGS LEDGER — four adversarial passes, 56 findings, and what each fix broke

## Status: **PROPOSED (2026-09-01). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Scope: **PR #337 → now only.** Head = `proposals/2026-09-01-holonic-architecture/ARCHITECTURE.md` (#353).

> ### ⚠ HONESTY MARKER ON THIS ARTIFACT ITSELF
> **This is a TRANSCRIPTION made during the session, not a machine-captured log.** The four
> adversarial reports were returned by read-only agents into the orchestrator's context and are
> reproduced here in substance, not byte-exactly. The counts, the section citations and the
> file:line anchors were re-derived from the working tree before being written down; the prose
> summarising each finding is the orchestrator's. **Where a claim here is load-bearing, check it
> against the code, not against this file.** The same marker the chain's own #353 carried, for
> the same reason.

---

## §1 · WHY THIS LEDGER EXISTS, AND WHAT IT IS FOR

This session was asked to test PR #353's idealized code shape by running a season loop for every
NPC and every arc. It built an instrument, ran it, and had it attacked four times. **The instrument
failed the fidelity claim on every attack**, was corrected four times, and the corrections
themselves introduced further defects.

That is the surface story. The ledger exists because of the structural one, which the repository
owner named and which §4 below verifies:

> **The session was in a holding pattern. Every correction round removed an invention the
> instrument needed IN ORDER TO EXECUTE, which stopped it executing, which forced a different
> invention, which the next antagonist flagged.**

**The set of things the instrument had to invent IS the specification's execution gap.** It is not
noise around the measurement. It is the measurement — and it was produced by the only method that
can produce it, which is trying to run the thing.

---

## §2 · THE FOUR PASSES, IN ORDER

| # | attacker | target | findings | direction |
|---|---|---|---|---|
| **A1** | read-only critic, structurally independent | instrument rev 1 | **10** | **all ten FLATTERED the shape** |
| **A2** | read-only critic | instrument rev 2 | **16** | flattery moved from the probe layer to the ROUTER |
| **A3** | read-only critic | instrument rev 3 | **16** | ⚠ **errors ran in BOTH directions** |
| **A4** | anti-fabrication auditor | the RESULTS | **14** | invention-hunting, per the owner's direct question |

**A3 and A4 ran independently, did not see each other, and converged on the same verdict:** the
probe ledger is largely sound; **the case-level verdicts are not citable in either direction.**

### §2.1 The signature of an improving process, and whether this is one

**It is not, and that is the finding.** A process that is converging produces *fewer* findings per
round and *smaller* ones. This produced 10 → 16 → 16 → 14, and round 3's were **worse in kind**
than round 1's, because round 1's all ran one way and round 3's ran both. Round 3 also produced
two findings *inside the regression file written to prevent them*:

- `test_r3_the_a5_control_actually_fires` asserted **the presence of a string**, not that the
  control fired. The confound survived its own pin.
- `test_d1_the_partition_is_not_invented` pinned **`stated == [("Tenure","until")]`** — an
  incomplete transcription of the head — so an omission became an invariant.

> **The rev-2 lesson recurred inside the file written to prevent it: A TEST ASSERTING THE WRONG
> PROPERTY IS WORSE THAN NO TEST.**

---

## §3 · THE FINDINGS, WITH WHAT EACH FIX BROKE

**The third column is the point of this table.** Where a fix broke something, the breakage was
almost always *"and then the loop no longer ran"*.

### §3.1 Pass A1 — ten findings, all flattering

| # | finding | § | what the fix cost |
|---|---|---|---|
| 1 | **The Partition was invented** — 12 `social:` rows declared; the head states 2 and marks 2 MISSING. Two invented rows were exactly the keys the in-chain instrument marks *deliberately absent* | §15.3, §30.1, §42.3 | ⚠ **Removing them stopped every season completing.** Forced `PARTITION_ASSUMED` in rev 3 — a different invention, declared |
| 2 | `witness()` **passed a false driver** (`Act` for an Event-caused deposit) — the one site where the gate would have fired | §28, §22 | none; the truthful driver then required an assumed Partition row (see 1) |
| 3 | The write gate was **opt-in on both limbs**; CENSUS passed an `apply` that mutated nothing | §30.2 | none |
| 4 | **`contest()` was the second resolver** — hardcoded band, no margin, named the most recent unrelated Event as cause | §27.2, §39.2/4 | contest now refuses; **A7 went from PASS to GAP** |
| 5 | **The budget was an engine truncation**, silently discarding a person's acts | §26.3, L1 | none |
| 6 | Three **invented constants in bodies** — a uniform wear rate (the silent default §42.2.1 names), `//60`, `confidence=1` | §42.2.1 | forced 6 more fixtures |
| 7 | **`sense()` returned a constant `standing`** | §18.2 | ⚠ rev 2 made it raise → **`Sensation` was then never constructed in any run**; the driver fed DELIBERATE a bare int, and a test pinned the deviation |
| 8 | Gap taxonomy split one doctrinal condition across two kinds | §30/§30.1 | ⚠ rev 3 over-corrected → **three of the design's refusals were tallied as debts** (A3 finding) |
| 9 | **Nine mechanisms claimed mechanical that were conventional** — incl. a rule written and disabled with `if False` | §34, §47 | none |
| 10 | **Thirteen spec requirements absent** — log hash, sum-then-clamp-once, five strata, Ob gate, L5 emission, T5 carry, T6 dispensation, `hold` cardinality, §15.3 causation, presence index, boot manifest, View `K`, transfer precondition | many | six landed as **stubs or in the probe**, which A2 then found |

### §3.2 Pass A2 — sixteen; the flattery moved to the router

| # | finding | § | what the fix cost |
|---|---|---|---|
| 1 | **A5's control returned FALSE and the probe asserted it returned TRUE** (`differing=False` … *"so the test CAN observe the failure it excludes"*) | §66 art. 4 | ⚠ rev 3's "fix" clamped per step — which made the arms differ **for the wrong reason** and violated §27.3 |
| 2 | **PLAYABLE verdicts manufactured by bare-token routes**; three rested on rows the architecture explicitly REFUSES | §44.4 | tightening moved ARC 39 → 47 BLOCKED |
| 3 | **The fourth bare-token trap**: `standing condition` escaped the 15-noun whitelist | — | ⚠ rev 3's structural guard was wrong in **both** directions (A3) |
| 4 | Rows the design refuses graded PASS (`everywhere` → F5; a crossing producing an outcome → P18) | §37.3, L5 | none |
| 5 | **L5's crossing emission was a stub** — a row appended for every site every season, no Event ever constructed | §12.1, L5 | none; real emission added |
| 6 | **The Partition derivation was permissive by default** and **L4's limb had never run in the whole suite** | §42.2, §42.2.1 | ⚠ making it total stopped the loop again → `PARTITION_ASSUMED` |
| 7 | Retraction 8 recurred three lines from the code that fixed it | §30 | — |
| 8 | **Six of thirteen "landed" requirements were dead code, stubs, or lived in the probe** | §27, §27.4, §39.2 | probes added to reach them |
| 9 | **Thirteen probes mislabelled `construction`** — incl. two calling a guard whose own docstring says it *detects nothing* | §34 | 17 relabelled |
| 10 | Two probes mis-attributed a **working** mechanism as a blocker | §43, §19.4 | routes moved |
| 11 | `Query.budget` a constant; **`choose` did not ask it** | §26.3 | the asking half restored; the variation is unimplementable — see §4.3 |
| 12 | **`Sensation` never constructed**; a test pinned the deviated arity | §26, §18.2 | — |
| 13 | **WITNESS invented a self-witness rule** — the instrument supplied the privacy the design lacks, then reported the design's privacy gap in a probe that never touched the loop | §28, §61 | deposits went 63 → 290 |
| 14 | **Band edges still hardcoded in probe bodies, unswept** — one of §42.2.1's four named prior sins | §42.2.1 | 9th fixture |
| 15 | The seam's `causes[]` fallback sat behind a **permanently false** predicate | §39.2 | — |
| 16 | F2's PASS text described a mechanism its code did not perform | §54 it. 20 | — |

### §3.3 Pass A3 — sixteen; errors now run BOTH ways

| # | finding | § | direction |
|---|---|---|---|
| 1 | **THE FIFTH TRAP: `age\w*` matches AGENT / AGENTS / AGENCY / AGENDA.** The arc corpus's only PLAYABLE was rows about *"two **agents**"* collecting the births-and-deaths PASS | — | flattering |
| 2 | **P17/P26 refused under L3 clause 2 what clause 1 EXPLICITLY PERMITS.** The head calls a per-`(Person, axis)` counter *"legal, since every increment is in the holder's own ledger"*; clause 2 bars only the cross-holder sum. **18 cases — the corpus's largest single blocker** | L3 | ⚠ **against** |
| 3 | All three PLAYABLE verdicts are artifacts; two near-identical NPC rows got opposite verdicts on which keyword fired | §11.1 | flattering |
| 4 | A5's control fires from **the clamp**, not from float non-associativity; the pin asserts a string | §32, §66 | flattering |
| 5 | **F3's route grades a PERSON as a faction** — 12 cases BLOCKED under L1 wrongly | L1 | ⚠ **against** |
| 6 | The `standing` guard is wrong in **both** directions — excludes real regard rows, still admits `standing,` and `Standing` | §18.2 | both |
| 7 | **F13's FORBIDDEN was produced by the instrument's own assumed row**, contradicting §24 and §30's matrix; and `ASSUMPTIONS_USED` is written and never read, so the promised disclosure does not exist | §24, §30 | ⚠ **against** |
| 8 | The enforcement split is inflated: A6/F3 claim *"not spellable"* but **`Act.actor` was unchecked**, so L1 was a convention | §34 | flattering |
| 9 | **A39 was a PASS that could not fail** — reverting the fix left it green | §39.2 | flattering |
| 10 | `Query.budget` ignores `(p,v)`; the disclosed COLLISION was **raised by a probe that did not exist** (`P42`) | §26.3 | suppressed a real finding |
| 11 | **W4 took person-condition rows** — the ambient MATERIAL/SOCIAL correction recurring on a new axis | §12, §18.2 | ⚠ **against** |
| 12 | **W13 took §13.1's WORKED LAWFUL CASE and reported it FORBIDDEN** — the head supplies that mechanism and calls it the better design | §13.1 | ⚠ **against** |
| 13 | `Ev()` minted `purpose` per KIND — **five Events with one id**, violating the invariant A28 certifies while A5 hashed the malformed log | §33, §19.1 | flattering |
| 14 | **Every band crossing is a causal orphan**: MATTER's `condition` writes emit no Event, so there is no antecedent to name — and the probe **asserted the orphan as the invariant** | §19.4 | flattering |
| 15 | **The head states a SECOND Partition row** (§54 item 21's `(Person, scar[axis])`, `social:true`, RESOLVE, ACTS) and rev 3 **pinned the omission in a test** — inverting the sign on a seven-arc finding | §54 it. 21 | ⚠ **against** |
| 16 | P3's *"L2 holds BY TYPE"* overstates: in Python `w` arrives by closure | §26.1, §34 | flattering |

### §3.4 Pass A4 — the anti-fabrication audit

Converged with A3 on the `age`/agents trap, the F13 self-inflicted refusal, the A5 clamp confound,
and the case-layer verdict. Its own additions:

| # | finding |
|---|---|
| 1 | **The ARC3 orphan's rows were DROPPED and both the README and the code docstring said the opposite.** The head fragment begins mid-block-scalar; the reconstruction cannot parse it, the `except` branch fires, and two `core` rows vanish. The guard asserted only that a *note* existed |
| 2 | `DECISIONS.md` recorded **224 executions of a death cascade and a bodies pass that do not exist in the code** — the register's most frequent row described a branch never taken because never written |
| 3 | A31c's *"11–81 seasons"* **mixed two different crossings** — at a floor above the site's starting condition the loop ran on to an unrelated floor |
| 4 | A25's assertion **could not fail** on the property it claimed (the only tie was inside the subtree) |
| 5 | README said 44 tests; the file defined 58 |
| 6 | `STEPS.md` under-counted refused writes: refusals raised inside `partition_lookup` are not preceded by a `TRACE.write(..., False)` |

---

## §4 · THE META-FINDING, VERIFIED

### §4.1 The loop, stated exactly

1. `ARCHITECTURE.md` leaves a large set of things **deliberately unspecified** (Part IX §61–§62 is
   its own list, and §42.2.1 rules that the honest behaviour is to **REFUSE, not to pick**).
2. **An executable instrument cannot run with those holes open.** A season loop that refuses at
   every hole completes zero seasons and measures nothing.
3. So the instrument **fills them** — a fixture, an assumed schema row, a formula, a roster.
4. An antagonist compares instrument to specification and **correctly flags the fill as infidelity**.
5. The fix removes the fill → **the loop stops running** → a different fill is required.
6. Return to 3.

**Four rounds of this produced 56 findings and zero convergence.** The loop has no fixed point,
because step 2 and step 4 are in direct contradiction: *the instrument is required to be both
executable and free of anything the specification does not state, and the specification does not
state enough to execute.*

### §4.2 The register — measured from the working tree, not asserted

| category | count | what it is |
|---|---|---|
| **harness fixtures** | **9** | `condition_scale · act_budget · ledger_cap · view_k · wear_per_season · confidence_default · entrenchment_seasons · obstacle_refusal_multiple · band_floors` |
| **assumed Partition rows** | **3** | `(Person, claim_ledger)` · `(Date, fired)` · `(DocketItem, matter)` — **without these three the loop cannot complete one season** |
| **probe-model verdicts** | **20** | the probe supplied the model the design lacks |
| **no-signature refusals** | **29** | nothing exists to call |
| | **61** | |

**Two of these categories are the specification's execution gap stated precisely.** The 9 fixtures
and the 3 assumed rows are *exactly* what a first implementer must decide before a single season
runs. The 20 probe-model verdicts are *exactly* where a mechanism is named and not modelled.

### §4.3 The three deepest holes, each of which defeats execution on its own

| hole | § | why it stops a loop |
|---|---|---|
| **`assemble(person, question)` has no producer for `q`** | §61 | **DELIBERATE has no declared entry point.** `opening_set` therefore has nothing to compute from, which is why every option set in this instrument is an authored roster — the exact property §17 chose `Candidate[]` to protect |
| **`Sensation.standing` is named and computed nowhere** | §18.2 | it is one of the *two* scalars that are the only bridge from world truth into `choose`, and the obvious computation is barred by §22.4 clause 2 |
| **`budget` cannot vary as §26.3 requires** | §26/§26.3 | §26 types it `(Person, View) -> int` with **no World**; §26.3 says it varies by office, condition and distance — **all three resolver-side**, and travel legs have **no owner at all** (§22.3) |

**None of the three is a defect in the instrument.** Each is a place where the specification, read
strictly, cannot be executed — and each was found only because something tried.

---

## §5 · WHAT SURVIVES AS EVIDENCE, AND WHAT DOES NOT

**Both A3 and A4 ruled independently, and they agree:**

- ✅ **THE PROBE LEDGER IS BANKABLE** with the named corrections. 120 executions; each names the
  section it exercises; ~24 of 26 `construction` gaps verified as raised by a gate, a type or a
  law rather than by the probe. Citation fidelity was checked at ~25 and ~15 sites respectively
  and found **verbatim and accurate**, with one wrong section number between them.
- ⛔ **NO CASE VERDICT IS CITABLE, IN EITHER DIRECTION**, until the router is re-audited. Every
  mis-route A3 and A4 named is now fixed, and **neither has re-audited**. The honest statement is
  that the case layer measures the router at least as much as it measures the design.
- ⚠ **The case corpus is real and is not in question.** 46 NPCs matching the registry exactly; 97
  arcs against a source the in-chain corpus covered only 51 of. The arc extension is this session's
  most durable artifact after the ledger, and it carries its own finding: across the corpora the
  in-chain run never touched, **the ending distribution is far weaker on the axis L1 cuts along**,
  and **three of the four cross-scenario feedback loops name no off-switch at all**.

---

## §6 · WHAT THIS LEDGER HANDS TO THE NEXT STAGE

The next document does not need another instrument. It needs the specification changed so that an
instrument is possible. Concretely, it inherits:

1. **The 61-item invention register** (§4.2) — every one a place the shape must decide, name or
   explicitly delegate.
2. **The three execution-defeating holes** (§4.3).
3. **56 findings** (§3), of which the ones that bear on the *design* rather than on the instrument
   are the ones to fold in.
4. **The meta-finding** (§4.1) — and the structural conclusion that follows from it, which is that
   a specification whose refusals are stated but whose fills are not **cannot be tested by
   execution**, and that this is fixable by *stating the fills as delegations with declared owners
   and grades* rather than by leaving them silent.

**No `ED` allocated.** A gap in a PROPOSED instrument gets no id; the adoption decision gets one.
