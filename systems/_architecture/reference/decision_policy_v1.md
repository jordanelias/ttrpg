# Decision Policy v1 — the precedence order Valoria decides by

## Status: DRAFT FOR RULING — does NOT ratify on merge (ED-1094 exception) — ED-IN-0113 §A, 2026-07-31

**Lane:** IN · **Pointer:** `workplans/POINTER_2026-07-31_m1_program_scaffolding.md`

> **⚠️ LOUD BANNER.** CLAUDE.md §2's "merging ratifies PROPOSED contents by default" is
> **suspended for every row in this document**. Merging it ratifies only *that the questions are
> correctly posed*. Nothing here is adopted until Jordan rules it, row by row.
>
> **This is a draft for correction, not an authored policy.** Jordan corrects faster than he
> authors — this session is direct evidence, having had four reports corrected into shape. So
> every row carries a proposed answer *drawn from measured precedent*, and the one row where the
> evidence does not support an answer carries **NO DEFAULT** rather than an invented one.

---

## §0 — Why this exists

**The queue does not drain because nothing tells it how to resolve itself.** Measured
2026-07-31: **213 open editorial items, 94 awaiting Jordan, 21 of those awaiting him for over a
month.** Sampling the queue found roughly **one in six is genuine authorial taste**; the rest are
resolvable from canon, from the research corpus, from consistency with prior rulings, or by
arithmetic — *if* something states which authority wins when they disagree.

**83 of 85 sampled `needs_jordan` items carry a source pointer; only 10 carry a proposed answer.**
The queue is evidence-rich and answer-poor. A stated policy is what converts the majority from
*decisions* into *conformance*.

---

## §1 — The evidence base

**134 Jordan-attributed rulings** mined across live and archive ledgers (reproducible: grep
`registers/editorial_ledger*.jsonl` for Jordan-attribution). What they show:

| Signal | Count | Reading |
|---|---|---|
| Rulings invoking canon / philosophy | 62 | canon is cited constantly |
| Invoking measurement / control | 56 | measurement is cited nearly as often |
| Invoking history / precedent / physics | 55 | grounding is a live authority, not decoration |
| Invoking emergence-over-fiat | 49 | the method is consistent |
| **Invoking deliberate fantasy** | **1** | the exception is genuinely exceptional |

**The decisive cases are the conflicts** — where two authorities disagreed and a ruling chose:

| Ruling | What happened |
|---|---|
| **ED-899** | Canonical Size-based combat pool **set aside** for the engine's resolution — canon made per-capita effectiveness degrade wrongly |
| **ED-900** | `combat_engine_v1` ratified as canonical resolver, **superseding the RESOLUTION layer** of `combat_v30.md` — *lore/flavour retained* |
| **ED-901** | Combat Pool and Concentration canon **STRUCK**: *"strike existing canon, I don't want that old system"* |
| **ED-PC-0005** | Wound-Ob ruling **overrode** `derived_stats_v30 §4.1`, which was marked **AUTHORITATIVE** and asserted *"No Ob penalty from wounds, ever"* |
| **ED-PC-0009** | The method, stated: *"determine both by testing bottom-up emergent primitives and validating top-down against history and hema and physics"* |

**The pattern is unambiguous for mechanical canon: it loses to measured, physically-grounded
engine behaviour.** Four independent instances, no counter-instance found.

---

## §2 — Proposed precedence (RULE THIS)

| # | Authority | Proposed rank | Evidence |
|---|---|---|---|
| 1 | **Metaphysical canon** — `canon/`, P-01..P-15, Ein Sof, inseparability, rendering | **NO DEFAULT — see §3** | unestablished |
| 2 | **Physical factuality & historical precedent** — physics, HEMA treatises, military history, arms scholarship | **outranks mechanical canon** | ED-899, ED-900, ED-901, ED-PC-0005, ED-PC-0010 |
| 3 | **Measured engine behaviour** — what the oracle actually does, under control | **outranks mechanical canon**; ties with (2) resolve by (2) | ED-899, ED-900 |
| 4 | **Mechanical canon** — formulas and numbers in `*_v30.md` | **subordinate to 2 and 3** | all four strike cases |
| 5 | **Lore / flavour** | **untouched by 2–4** — ED-900 retained it explicitly | ED-900 |

**Proposed rule, one sentence:** *when a `_v30` formula disagrees with a physically-grounded,
control-measured engine result, the engine wins and canon is amended — but the fiction it
described is preserved.*

---

## §3 — THE CRUX. **NO DEFAULT.** Only Jordan can rule this.

**Does metaphysical canon sit in the same subordinate tier as mechanical canon, or does it
outrank measurement?**

The evidence does not answer it. **30 Jordan-attributed entries touch metaphysical canon; 9
contain override language — but those 9 were not read**, so it is unknown whether the metaphysics
itself was ever overridden or merely mentioned in an entry that overrode something else.

**No default is offered, deliberately.** Supplying a precedence order the evidence does not
support is precisely the fabrication CLAUDE.md §5/§7 forbids, and the `NO DEFAULT` convention
exists for exactly this row.

**Why it matters more than any other row.** The metaphysics is not decoration — it *generates* the
mechanics. A2 (inseparability) is instantiated as TD accumulation; A12 (knotting) as the Knots
mechanic; A5 (Ein Sof) as the Key substrate; A11 as the Coherence stat. A canon-guard CI job fails
a build whose mechanics violate the philosophy. **If metaphysical canon is subordinate to
measurement, that gate is advisory. If it is supreme, it is a hard constraint and some measured
results must be discarded rather than canonised.** Both are coherent; they are very different
projects.

**Three ways to rule it:**

- **(a) Supreme** — metaphysical canon outranks everything; a measurement contradicting A1–A15 is a
  defect in the model, never in the canon.
- **(b) Same tier as mechanical canon** — subordinate to grounded measurement; the metaphysics is
  revisable evidence like anything else.
- **(c) Split** — the *constraints* (A1–A15) are supreme; their *mechanical instantiations* are
  subordinate. This is consistent with ED-900's lore/resolution split one tier up, and is the
  option the evidence is least inconsistent with — **but it was not measured, so it is not offered
  as a default.**

---

## §4 — Operational tests (RULE OR AMEND)

A precedence order is unusable without a test for whether an authority is satisfied.

| Authority | Proposed test | Status |
|---|---|---|
| **Emergence** | The **U9 capstone ablation gate**: hold the lever at K=0 and require outcomes degrade *continuously*, not by losing a named outcome. Scripting is what fails this. | **Already built.** Proposed as the definition. |
| **Canon** | A **verbatim quote with a locator**, never a paraphrase. | Proposed |
| **Historical precedent** | A **cited source with a locator** (treatise page, work + section), not "historically, armies…". | Proposed |
| **Physical factuality** | A **measurement or physical derivation**, with a control arm (§0.1 #4). | Proposed |

**The emergence test is the important one**, because "emergent" otherwise licenses any mechanic to
justify itself. The ablation gate already exists and already discriminates.

---

## §5 — The exception clause (RULE THIS)

Deliberate fantasy appears in **1 of 134** rulings — *"knowingly [B]/[L], gloriously fantastical ON
PURPOSE"*.

**Proposed:** grounding is the default; departure from it is permitted, must be **invoked
explicitly and marked in the doc**, and may never be inferred from silence. An unmarked mechanic
that contradicts physics or history is a defect, not an exercise of this clause.

**Proposed invoker: Jordan only.** A session may *propose* an exception; it may not take one.

---

## §6 — What this policy does NOT determine

Stated so the derivation engine cannot overreach, and so the residual queue is honestly small:

- **Magnitudes.** Caps, thresholds, coefficients. ED-SC-0005 self-labels *"cap value is Jordan's
  design number"* — correctly. Policy chooses direction; it never supplies a number.
- **Names.** Naming collisions are resolvable by convention, but a *canonical* name is authorial.
- **Taste.** Which of two coherent designs is the better game.

Everything else should resolve without a ruling. **Measured: ~1 in 6 of the sampled queue is
genuine taste** — so if this policy works, the ~21 stale `needs_jordan` items should fall toward
**3**, which is the target already seeded in `registers/scope_baseline.yaml`.

---

## §7 — How to rule this

Row by row. `Accept` · `Override` · `Amend`. **§3 is the one that unblocks the rest** — §2 is
already evidenced and §4–§6 are mechanical once §3 is settled.

**When a derivation is later overridden, the right question is whether the POLICY is wrong**, not
just that item. Overrides become policy amendments, the policy sharpens, and the override rate
falls. That is the difference between a system that converges and one that needs Jordan forever.

## §8 — Limits of this draft

- **The 9 metaphysical-override candidates were not read.** That is the single gap between this
  draft and a ruled §3, and it is stated rather than papered over.
- **Attribution is by prose match**, so a ruling recorded without a Jordan-attribution phrase is
  invisible here. The corpus is a floor, not a census.
- **Conflict cases were found by keyword**, so a conflict resolved without conflict language is
  missed — the same grep blind spot CLAUDE.md §0.1 #5 names.
- **No counter-instance to §2 was found, but absence of a counter-instance is not proof.** Four
  concordant cases is strong, not conclusive.
