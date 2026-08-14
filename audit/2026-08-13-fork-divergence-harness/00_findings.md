# FORK divergence — the alias plan's foundation, executed rather than read

## Status: REFERENCE — measurement with a re-runnable instrument; nothing ruled, nothing consolidated

## Date: 2026-08-13 · Lane: IN (cross-cutting) · ED-IN-0178

**Instrument:** `fork_divergence.py`, beside this file. Every number here is reproduced by it.
**Ratchet:** `tests/valoria/test_fork_divergence.py`.

---

## 0. Why this exists

`audit/2026-08-12-alias-index-consolidation/00_plan.md` rests its whole sequencing argument on one
claim:

> five parsers disagree about what its rows mean … the same row resolves five different ways, two
> of them inside BLOCKING gates.

That claim was **read off the page**. The plan says so itself (§6) and names running it as the
first executable step, *because everything else depends on it*. Wave 3 is that step. It changes no
parser and consolidates nothing — Phase A2 does that. It exists so Phase A starts from a
measurement.

---

## 1. The plan's central claim: **CONFIRMED**

One 1-hop FORK row (`engine/params/core.md` → `FORK:c451bcb`) produces **5 distinct verdicts across
6 consumers**:

| consumer | verdict |
|---|---|
| `pathres` | `FORKED` |
| `broken_dependency_checker` | `INFO-EVACUATED` |
| `ci_claude_workflow_paths` | `DEAD` *(fails a BLOCKING gate)* |
| `vector_audit` | `missing` |
| `workbench` | `missing` |
| `gen_audit` | `nonexistent` |

The plan's other two structural claims also reproduce:

- **Hop count.** `params/core.md` is a real 2-hop chain (`params/` → `engine/params/` → FORK).
  `pathres` (chained, max 6) returns `FORKED`; `broken_dependency_checker` (single-hop) returns
  **BROKEN**. Confirmed exactly as written.
- **FORK payload shape.** One function, two shapes: `bdc` returns the bare `FORK:c451bcb` for an
  exact row and `FORK:c451bcb:<original-path>` for a prefix row.

---

## 2. The finding the plan does not have — and the control that produced it

The plan asks *"do the consumers disagree about a FORK row?"* That is the easy half. The question
that matters is the one `tests/valoria/test_forked_status.py` was written to defend:

> a path that left deliberately must not look like a path that never existed.

That file calls the separation **"the repo's anti-fabrication property"** and proves it for exactly
one consumer. So this harness runs every probe against a **control**: `totally/made/up/never/existed.md`,
a path with no ledger row at all.

**Result: the distinction survives in 5 of 18 (consumer × fork-row) pairs.**

| consumer | forked vs fabricated |
|---|---|
| `pathres` | preserved on every row |
| `broken_dependency_checker` | **PARTIAL** — preserved on 1-hop rows, **collapses on the 2-hop chain** |
| `ci_claude_workflow_paths` | **COLLAPSED on every row** (`DEAD` = `DEAD`) |
| `vector_audit` | **COLLAPSED on every row** (`missing` = `missing`) |
| `workbench` | **COLLAPSED on every row** (`missing` = `missing`) |
| `gen_audit` | **COLLAPSED on every row** (`nonexistent` = `nonexistent`) |

The plan states *"three of five consumers collapse exactly that distinction"*. Measured against a
control it is **four of six collapse it outright, and a fifth collapses it conditionally** — and
the conditional one is a blocking gate.

### 2.1 Why per-pair, not per-consumer — this is the part worth carrying

The first version of this instrument tracked a set of *consumer names*, on the natural assumption
that a consumer either understands `FORK:` or does not. **`broken_dependency_checker` refutes that
assumption**: it returns `INFO-EVACUATED` for a 1-hop row and `BROKEN` for a 2-hop chain — and
`BROKEN` is precisely what a fabricated path returns. Its anti-fabrication property is **conditional
on hop count**.

A per-consumer roster cannot express that. It would have recorded `bdc` as wholly safe or wholly
broken, and **both are false**. The granularity of a measurement is not a presentation choice; it
decides which findings are expressible.

---

## 3. Two corrections to my own work, recorded because they are the method

1. **The instrument was wrong before the plan was.** The first probe modelled
   `bdc._resolve_remap()` as the decision and reported `params/core.md` as *"mapped"* —
   contradicting the plan's BROKEN prediction. The plan was right. `_resolve_remap` is a helper;
   the decision is in the caller (`bdc:217-227`), which tests membership in `all_files` first. A
   harness that models a helper instead of a decision measures its own model. Fixed before any
   result was reported, and recorded in the instrument's docstring.
2. **I reported "only `pathres` and `bdc` preserve the distinction" before running the strict
   comparison.** Under the per-pair test that is too generous to `bdc` — see §2.1. Corrected here.

---

## 4. What this does and does not license

**Licenses:** Phase A2 proceeding on a measured foundation rather than a reading. The plan's
ordering argument — consolidate onto `pathres` *while the markdown is still the source* — is
strengthened, because `pathres` is the only consumer that preserves the property on every row, so
it is the correct consolidation target on evidence and not just on design.

**Does not license:** any claim that the collapsed consumers are *bugs to fix now*. Three of the
four (`vector_audit`, `workbench`, `gen_audit`) are audit-side tools where `missing` may be an
adequate answer; `ci_claude_workflow_paths` is the one that **fails a blocking gate** on a
legitimately-evacuated path, and it is the one Phase A5 already targets. Ruling which of the five
semantics is canonical is **Phase A1, held for Jordan**, and nothing here pre-empts it.

**The ratchet is deliberately not a conformance gate.** Failing on today's 13 collapsed pairs would
red every unrelated PR immediately — the "reds on day one" mistake ED-IN-0112 already paid for. It
pins the 5 pairs that work and fails only when one stops working. Phase A2 grows it.

---

## 5. Falsifiers

| claim | falsifier | outcome |
|---|---|---|
| 5 distinct verdicts, 6 consumers | run the instrument | reproduced |
| the 2-hop chain collapses in `bdc` | `test_bdc_still_collapses_the_two_hop_chain…` | pinned, and fails *if fixed* — pointing at the baseline to update |
| the control never resolves | `test_the_control_is_dead_everywhere` | passes |
| the ratchet can see a loss | `test_the_ratchet_can_observe_a_loss` plants one | reports exactly it |
| the probe reaches all six | `test_the_probe_reaches_every_consumer` | a silent import failure cannot read as agreement |

## 6. Not measured

- The plan's **116 header-less FORK rows** (`00_plan.md` §2) — a parser-fidelity question about the
  ledger's table shape, not a semantics question. It is the next thing a capture must prove.
- The **duplicate-key precedence** and **existence-test** disagreements (§1). Both are real per the
  plan's reading and neither is exercised by these four probes; extending `PROBES` is the cheap way
  to settle them and it was deliberately not done here, to keep this wave to its stated scope.
