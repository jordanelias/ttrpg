# 05 · RECONCILIATION — what the adversarial pass did to the four proposals

## Status: **PROPOSED (2026-09-04). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE. Nothing here runs.**
## Orchestrator's reconciliation of a four-way agonist→antagonist relay (CLAUDE.md §10). Each critic
## was `valoria-critic` — `Read`/`Grep`/`Glob` only, so its independence is **structural, not declared** —
## and each received a producer's OUTPUT without its reasoning.

---

## §0 · THE VERDICT, FIRST

**None of the four proposals is executable as written.** Three carry defects that would ship a bug or
crash the suite; one carries an arithmetic impossibility that makes its central mechanism inoperable at
every parameter value. **This document is the reason the execution phase does not run on them yet.**

That is the relay working rather than failing. The proposals were produced against a shape spec that
was itself produced against a tree nobody had re-measured, and the critics measured it. **What the pass
did NOT find is as load-bearing as what it did: on research honesty, across ~440 anchors and four
documents, the critics found nothing.** No number in any of the four is sourced to a historical claim
rather than marked as a seed, the corpus's own confidence flags are respected, and one document's
correction of a source overstatement is carried faithfully.

| document | anchors checked | wrong | verdict |
|---|---|---|---|
| `01_SPINE.md` | ~170 | 9 | **3 build-breaking defects**, 2 grade errors, 2 counts irreproducible |
| `02_NEGOTIATION.md` | ~95 | 9 | **5 claims overturned, 4 new defects** |
| `03_INQUIRY.md` | ~205 | 17 (4 load-bearing) | **1 shipped-code regression**, 1 invented API |
| `04_CONSENSUS.md` | 62 | 12 | **arithmetically inoperable**; all three antibody channels inert |

**No critic fabricated a finding.** Every wrong anchor named real code in the right file, mostly within
±20 lines. Ten attacks were run and reported as failed, which is the result the method asks for.

---

## §1 · BLOCKING — these must be fixed before any line is written

### B1 · Consensus is arithmetically inoperable (`04_CONSENSUS.md`)

`margin() = assent_share − 1.0`, so **margin ∈ [−1, 0]**, fed to a ladder with **fixed** edges at 0, 1
and 3 (`engine/autoload/dice_engine.py:234-239`). **No positive scale maps a non-positive number into a
band requiring ≥ 1.** Verified by computation:

| assent share | margin | band at scale 1 · 2 · 5 · 10 · 100 |
|---|---|---|
| 1.000 (unanimous) | 0.000 | **Partial** in all five |
| 0.990 | −0.010 | Failure in all five |
| 0.600 | −0.400 | Failure in all five |

**A body that unanimously agrees refers its own matter to next season.** `Overwhelming` and `Success`
are unreachable in *every* body; every non-unanimous result is `Failure`; no `Precedent` ever writes;
`UNANIMITY_MARGIN_SCALE` decides nothing.

**The aggravating fact:** `01_SPINE.md` measured this exact defect class and fixed it by dividing
**inside** `margin()` by a per-subclass `SUCCESS_UNIT`. The consensus branch cites the spine as its
supplier of `margin()` and then substitutes an **external multiplication**, which cannot work at any
value. *Term-matching, not concept-matching* — `degree_from_net` is a fixed-threshold ladder, not a
scale-free one. **Fix: adopt the spine's `SUCCESS_UNIT` division. This is an arithmetic error, not a
design choice.**

### B2 · Inquiry would ship a silent regression into shipped faction code (`03_INQUIRY.md`)

§5.3 rewrites `formal_grounds_check(church, world)` with two new keyword-only parameters and
`if accused is None or place is None: return False`. **Its only live caller passes neither**
(`systems/factions/sim/tribunal.py:102`), so it returns False for every case that returns True today —
and that flag adds `+1D` to the pool (`:109-111`) and halves the Ob (`:117-120`). **The comment
`"typed, never a crash"` shows the None case was considered and resolved the wrong way.**

**And the branch is not campaign-unreachable**, as the document claims: the chain runs
`tribunal.py` → `excommunication.py:119` → `faction_action.py:329` → `engine/mc_v18.py:138`, fired every
season the Church holds `L >= EXCOMM_PREREQ_L_LIGHT`. So the campaign goldens **are** a genuine control
for this edit, and §12.2 talked itself out of its only real instrument. **Fix: default the third clause
`True` when the new parameters are absent, or add the three-way gate under a new name.**

### B3 · The spine's `_resolve` is a name collision that kills the kernel suite (`01_SPINE.md`)

`wrapper.py:303 def _resolve(sym)` already exists as the MECHANICS symbol resolver and is called at
`:444`. Module-level rebinding breaks either the new caller or the old one; the kernel suite dies at
`_kernel_tests.py:635` either way. **Grep-findable in one command, in the file the change list edits
most.** Fix: name it something else.

### B4 · The inquiry correction invents an API (`03_INQUIRY.md`)

Its fix calls `log.of_type("scene.investigation_resolved")`; **`KeyLog` has no `of_type`**
(`engine/substrate/keys.py:336-461`). `KeyLog` is iterable, so `[k for k in log if k.type == …]` works.
**A document whose central finding is "the other document invented an API" cannot invent one in the
correction.**

### B5 · The inquiry Key row emits a payload the log refuses (`01_SPINE.md` A11 · `03_INQUIRY.md` E11)

`echo_transport.py:434-438` hardcodes `{scene_id, outcome, participants}` for every scene type;
`scene.investigation_resolved` requires `[scene_id, subject_id, finding]`; `keys.py:317-320` raises
**`KeyValidationError`**. **Found independently by two agents on disjoint tasks** — the corroboration
signature worth trusting. The emission is additionally gated on a non-zero faction stat delta
(`:421`), so an inquiry scene producing no delta emits nothing at all. **Fix: the row does not ship
alone; it needs a payload builder, and it belongs in the inquiry document.**

---

## §2 · THE ANTIBODY IS INERT — the consensus branch's central promise fails on three legs

The branch's stated test of itself: *"if channel 1 were removed, this branch would ship a
known-defective consensus procedure with a decorative antibody."* All three channels fail.

1. **It cannot fire on a member at all.** `DefeatCatalogue.check` iterates only the two contestants
   (`primitives.py:273`), reading `FaultState`, which `Bout` builds only for `{A, B}`
   (`resolver.py:241`). `Adjudicator`/`Panel` carry none. **Members ballot; they never move; nothing can
   be charged to them.** It reaches a holdout only after promotion in S4.1 — which does not exist at
   **K = 0**, and **K = 0 is the *liberum veto***, the arm the whole grounding is about.
2. **Its trigger is unreachable under every production policy.** `fault.evasion` accrues at one place
   (`resolver.py:380-381`) gated on strict-equality `Stasis.relevant`; ten of eleven shipped policies
   build every move with `ground=v.live_ground`, and the exception is a fixture. **The evasion clinch
   has never fired in production and cannot, absent a policy authored to argue off-topic.**
3. **The durable mark is written on a degree the aggregation cannot produce** — `Grudge` only on
   `Success`, which the branch's own strict rule makes impossible and which B1 makes unreachable.

**Recommended repair (the critic's, and I agree): give the ballot one per-member term.** A member
disposition added to `k*gap + gauss(0, noise)` buys back five claims that currently have no referent —
the *liberum veto* falsifier's bribed-deputy arm, the "named author" invariant, the `T-b` defence, a
target the antibody can bind at the moment of blocking, and **the difference between a body of persons
and K repetitions of a coin-weighting.** It also forces a hidden trade into the open: it moves the
campaign goldens.

---

## §3 · CONTROLS — three of four documents got their own control wrong

This is the pattern worth naming, because it recurred independently across three branches.

| document | claimed | actual |
|---|---|---|
| `01_SPINE.md` | the goldens are a control on three grounds, one being that `margin()` is *"added and not consumed"* in S0 | **its own change list computes `margin()` on every production resolution.** Two grounds, not three — and the goldens become hostage to a `VoteAtClose` double-draw the document itself calls the likeliest builder bug |
| `03_INQUIRY.md` | campaign-unreachable ⇒ the goldens are a **fake** control | **one of its six edits sits on the `mc_v18` season loop.** The goldens are real, and the document disclaimed its only campaign-level instrument |
| `02_NEGOTIATION.md` | the goldens are the control; `balance_oracle` is disqualified as a fake control | **the changeset is campaign-unreachable, so the goldens' arms are identical by construction too** — for exactly the ED-MB-0066 reason cited to disqualify the other instrument. The real difference is cost and resolution, not "identical by construction", which cuts both ways |

> ### THE RULE, STATED SO IT DOES NOT HAVE TO BE RE-DERIVED
> **Reachability is a property of an EDIT, not of a BRANCH.** A changeset is campaign-reachable if
> *any single edit* lands on a path `mc_v18` drives. Ask it edit by edit. Any change touching
> `systems/factions/`, `systems/settlements/sim/ledger.py` or `engine/cross_scale/` is reachable until
> shown otherwise.

---

## §4 · THE SAME ERROR, FOUR TIMES — inheriting a summary instead of checking the source

The session's most reproducible failure, and it is mine as much as the agents':

1. **I** asserted breaking the import cycle would trip a live gate. It would not.
2. The spine checked the test body and corrected me.
3. `04_CONSENSUS.md` inherited `fixed_lean` from the shape spec **without opening it** — it lives on a
   different class in a parallel voting model, so the *liberum veto* falsifier's key arm is not
   constructible.
4. `02_NEGOTIATION.md` rebuilt the same false import-cycle argument **after** the correction was
   published, and made a falsifier out of it — one that cannot observe the failure it excludes.

**The rule: check the assertion, not the prose above it.** A docstring is not a gate; a `values:` line
is not the `note:` four lines above it; a summary of a source is not the source.

---

## §5 · WHAT SURVIVED — attacks run and reported as failed

Recorded because a failed attack reported as failed is a result, and because these are the claims the
build can rely on.

- **The PR #362 conflict stayed refuted under direct attack on two branches.** Every anchor verbatim:
  `§C.4:576` flattens acts across all scenes into one ordered fold, `D-49:871` forbids nesting rather
  than same-pass resolution, `:579` evaluates against `world_as_predecessors_left_it`. On consensus the
  critic looked specifically for a place where one member's ballot is an input to another's and **found
  none**, so simultaneity holds and *"the refusal to manufacture a conflict is correct."*
- **The spine's incommensurability refutation, recomputed and upheld** — `VoteAtClose.margin ∈
  [−0.5, +0.5]`, so a unanimous 7–0 does band `Partial`.
- **The `agon` binding-order trace, every link exact.** `dispatch_scenes` drains the whole slate in one
  loop, `_emit_at_depth` defers under `_PHASE_ACTION`, `accounting_boundary` runs after the action
  phase, and `_emergency_council_parties:139` reads the stats a prior scene moved. **Jordan's ruling is
  observably violated in shipped `agon` today**, and `test_echo_transport.py:107` passes while
  contradicting the invariant.
- **The three inquiry "would have shipped broken" findings all survive independent reading** — the
  tribunal has never used `ProofBar`, the grounds expression does not typecheck, and the
  2-prior-convictions clause can never fire because `ledger_add` dedupes on exactly the key the spec
  itself writes.
- **The consensus branch's refutation of the shape spec's antibody is upheld link by link** — called
  *"the document's best work"* — as is its refutation of ED-SC-0015's closure on all three legs.
- **`split(−m) == 1 − split(m)` holds exactly**, verified through Sterbenz, including at `m == 0`.
- **The import-cycle test needs no update** — independently confirmed twice.
- **Research honesty: nothing found, in any document.** The Heath correction on Hermagoras is carried
  faithfully; §9.7's "history validates the structure, never the numbers" is respected; Putnam's
  *"a metaphor"* tier-flag is carried verbatim; every invented number is marked `[SEED]`.

---

## §6 · THE SPLIT-TABLE DEFECT — stated better than any single document had it

Real, verified independently three times, and **latent rather than live**: `succession()` has zero
production callers (`faction.py:86`, called only by its own `succession_rate` and `_kernel_tests.py`).

> **The leader's share is the same function of `|t−5|` on both sides, offset by a constant 0.05 in B's
> favour.** Both sides step at `|t−5| = 0.5`; **B steps up to 0.60, A steps down to 0.50.**

So: a dead tie awards A 55% (`>=` is inclusive); A's share is **anti-monotone** — more advantage buys a
smaller share; and mirrored positions differ by 10 points. Banker's rounding matters — `round(4.5) == 4`
and `round(5.5) == 6`.

**The root is canon, not code.** `social_contest_v30.md:415` claims *"track-distance weighting"* while
`:421-423` pays equidistant tracks 4 and 6 differently — a **directional** reading of a **bidirectional**
track. Under §0.05 the fix goes in the code, but the prose is where the confusion starts.

⚠ **The proposed repair deletes a canon outcome, unmeasured.** The `split` branch is reached only when
`3 < t < 7`, i.e. `|t−5| < 2`, while the proposed keying reaches `0.60` only at `|margin| ≥ 3`. **Under
the natural map the canonical 60/40 split becomes unreachable in succession**, and restoring it needs
an uncalibrated scale factor — a `[SEED]`, in a document asserting it has none.

---

## §7 · DISPOSITION — what to do with each document

| document | disposition |
|---|---|
| `01_SPINE.md` | **Revise and keep.** Its architecture holds; B3 and B5 are local, and its own §9.1 already states the fix for the control defect (*do not consume `margin()` in production during S0*) — the change list simply contradicts it. |
| `02_NEGOTIATION.md` | **Revise and keep.** `settle()` survives as the one genuinely new object, but its N-line must be re-argued (`destroy_record` exists), `floor_a` reconciled, the import-cycle argument deleted, and the breach asymmetry moved into the exploit table as a **dominant strategy**, graded. |
| `03_INQUIRY.md` | **Revise and keep.** Its three headline findings are its value and they survived. B2 and B4 are the blockers; the dominance analysis must be re-run against the **reachable** venue. |
| `04_CONSENSUS.md` | **Revise before anything else.** B1 makes it inoperable and §2 makes its central promise decorative. Its refutations of the shape spec are excellent and should be preserved verbatim; its own mechanism needs rebuilding on a per-member term. |

**Nothing here is a reason to rebuild `agon`.** Every defect above is at a seam, in a table, or in a
proposal — none is in the resolution atom, and `agon` remains the only part of this subsystem that
executes. The two campaign goldens are the control for the whole programme, and a rebuild would destroy
the instrument that proves the rest of the work is sound.

---

## §8 · WHAT AN INDEPENDENT REVIEWER WOULD ADD

1. **This reconciliation is self-authored by the orchestrator that dispatched both halves of the
   relay**, and it grades its own earlier errors as one of four instances of a pattern. A reviewer
   should check whether the pattern framing is doing work or providing cover.
2. **Nothing in this session has run.** Every document, including this one, is **paper** under §0.2.
   The four critics read code; they did not execute it. The cheapest genuine measurement available is
   still the one `02_NEGOTIATION.md` names: run the symmetry identity against the current
   `faction.py` and watch it fail. Four lines, no fixtures.
3. **Every "no dominant option" claim in every document remains an upper bound.** No AI-vs-AI
   best-response sweep has been run for any branch; ED-SC-0021's falsifier is still unrun.
