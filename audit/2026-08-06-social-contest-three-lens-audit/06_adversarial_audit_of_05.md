# Adversarial audit of `05_track_architecture_and_state_graph.md`

## Status: RECORD (2026-08-06, ED-SC-0028)
## Lane: SC

Three read-only Fable critics (`valoria-critic`: Read/Grep/Glob only — independence structural, not declared) were
run against `05` on separate attack surfaces: **correctness** (every claim against the working tree), **logic**
(does the reasoning hold), **elegance/execution** (does it serve the pruning brief). None saw the authoring
reasoning; each received only the artifact. Per CLAUDE.md §10 this is the agonist→antagonist relay with the top
tier on the audit node.

`05` has been revised in place. This file records **what was found**, so the corrections are auditable rather than
silently absorbed.

---

## §1. What held

Stated first because it bounds the rest. Roughly **25 of `05`'s ✓-marked citations were hand-verified across two
critics; zero misquotes.** Independently re-run and confirmed:

- `joint_weight` and its tense-only content input (`resolver.py:170-176, 303`).
- Six WinConditions reading no *contest* state but `adv` (`:52-145`); faults the only terminal reading none
  (`:438-442`).
- The gain formula, leak/public, bias, readiness, `split_standing`, `standing_start` with no in-tree producer.
- `Stasis.TENSE` (`primitives.py:16-17`), exact-match relevance (`:21`), Reserve support-2/regain-4 (`:51-52`),
  hidden evidence weights (`:282-310`), Adjudicator's six fields and Panel averaging (`contract.py:24-51`).
- **The complete-`EvidenceItem` falsifier** — repo-wide grep reproduces exactly the four cited sites; **no world
  producer of evidence exists anywhere.**
- **The `Stasis.TENSE` falsifier** — only non-test reader is the weight path; the deletion is clean.
- All three `investigation.py` entry points are stubs.
- `LedgerTag`'s dataclass shape, five kinds, ttl, and succession docstring — exactly as cited.

**Sharpened in `05`'s favour:** `hard` is *strictly dominated*, not merely redundant (costs 5 vs 3 for identical
post-gate effect, plus clinch risk). `FactionBoost` has **no resolution consumer at all** — the +1D is prose-level,
so it is more inert than `05` claimed. Reserve is net-positive *and* builds ethos, so the economy finding was
understated.

**Attacks that failed:** the "player's utility recollapses the two axes anyway" objection — the anti-collapse
condition is explicitly about engine-side fixed-rate conversion. The three-owner credibility count survived a
merge attempt (holder-indexed vs holder-independent state is a real distinction). The genre kill and the
retraction discipline both held.

---

## §2. Errors found, ranked

| # | Finding | Severity | Disposition in `05` v2 |
|---|---|---|---|
| 1 | **The headline measurement is false at the scope written.** "Sealed off in both directions"; "the entire world→contest interface"; W1 "today they don't." A second path is live by default: `mc_v18.py:148-151` runs `parliamentary_bridge` every season (`ECHO_TRANSPORT` default ON, Jordan 2026-07-08); `_derive_vote` **generates a topic from world pressure**; `parliamentary_vote.py:206-216` writes back to `world.factions`. Two more callers in `systems/factions/sim/`. **`05`'s own falsifier names this exact test and it was never run.** | **CRITICAL** | Scoped to the Bout kernel; the parliamentary path named as the counter-example; the surviving narrower claim stated |
| 2 | **The two-category test is not decidable and was applied to a moving target.** The rider "…that anything reads" appears in §8's heading and not in §7's statement of the test. Kills graded against the kernel **as built**; withdrawals against the architecture **as proposed**. That asymmetry rescues anything by hypothesising a future reader | **CRITICAL** | Test restated with two mandatory riders: name the system graded against; every withdrawal names an existing consumer or a numbered fork |
| 3 | **The duality claim does not hold.** Fork A is RULED "auto = the kernel run headless… consistent by construction"; §6 makes matched-input consistency the hard constraint. So either playing shapes nothing in expectation (and `04`'s wasted-attention charge returns on two scalars), or the player steers a trade-off the auto policy does not — **mode-shopping, the exact exploit §6 prevents.** The escape is **CIP-9b**, an unratified amendment `05` never cited | **HIGH** | Headline downgraded to conditional; CIP-9b named; the trilemma stated |
| 4 | **"No new primitive" is false.** `ledger_add` treats Reputation as `SINGLE_VALUED` **by kind, ignoring `key`** — every prior Reputation tag is deleted on insert. Tags live on one settlement: **no holder dimension**, and factions have no ledgers. W6's *reach* has no carrier at all. (Import **direction** is fine — `systems.*→systems.*` is established, no cycle) | **HIGH** | Restated as "one primitive, extended cross-lane, **needs SE**" |
| 5 | **Three absolutes overstated.** "No authority of any kind" — juror `discipline` is explicitly bench-weight, "institutional rank/rigor" (`resolver.py:109-118`, ED-1057). "All six WinConditions read only `adv`" — `VoteAtClose` reads it. "Pressure is a one-way arrow into the bench" — `SelfGating.licit` gates the contestant's `hard` on `adj.learned`/`hostile` (`:357`), exposed via `ContestView` | HIGH | Each replaced with what is genuinely absent: **cross-contest** authority |
| 6 | **`§7a` and `§8` rule opposite ways on `split_standing`** — and the rescue depends on `hard`, which the same document kills: ascribed Rank's one distinct in-bout consumer is `SelfGating.licit` | HIGH | Contradiction named; fate coupled to the institutional-party fork |
| 7 | **"Same object" is an elision.** `f` has no speaker and no occasion argument; the coupling operator is strictly larger. Their failure modes differ (fabricated tables vs god-object). Internal collision: §4.5 absorbs `Dossier.available` into judge-graded salience while §4.2 insists atechnic value is engine-fixed | HIGH | Downgraded to "the same slot reached from two directions"; the weight/relevance asymmetry resolved explicitly |
| 8 | **The FactionBoost→disposition-matrix rescue is a category error.** The table maps faction → the argument-style a room dominated by that faction rewards. No holder, no valence, no opinion *about* a faction. It is crowd-profile data plus ethical-mode vocabulary | HIGH | Reassigned; recorded in `05` §7.3 as what the broken instrument cost |
| 9 | **The warrant-vs-appeal reversal is motivated reasoning.** The separation is a property of a table that does not exist and whose every cell is a `[SEED]` — the same authoring cliff that produced the ED-SC-0025 retraction | HIGH | **Downgraded from banked reversal to undecided-pending-authoring**; HIGH confidence rating withdrawn |
| 10 | **The dropped sweep condition.** `00` Fork B ratified the warrant-scheme direction **conditional on a pick-entropy sweep not yet run**; `05` adopted the mechanism without the condition — a §0.1 point-3 violation | HIGH | Condition reinstated |
| 11 | **C-1's decomposition uses a term the document deletes.** Genre = `hearer_role × question_tense × verdict_standard`, but correction 4 deletes `Stasis.TENSE`, so after `05`'s own recommendations `question_tense` is stored nowhere | MED | Kill survives on the independent argument; decomposition's middle term re-founded on venue temporal weights |
| 12 | **The "iff" is rhetorical**, the four couplings are heterogeneous (C-2 is a config refactor, C-4 an unbuilt mechanism), and a fifth is nameable from `05`'s own material: **leak**, which rewrites E1's weights mid-contest — P4 rewriting P3's standard | MED | Softened; C-5 added |
| 13 | **Accretion, structurally.** "Nine trajectories" over 14 rows; **W7 cited four times, never defined**; W table ordered W1,W2,W3,W5,W6,W4; T9 wedged between T8b and T8c; E15 before E14; the T8 split never propagated back to E2/E3; **§5's state graph omits every late object, and its emission list omits Reputation and Leverage — the very kinds the headline mechanism writes**; §7b never tests the pairs the new tracks create; no falsifier for the priors; "exactly four divergence terms" broken by a fifth added in §1 | MED | Architecture reduced to 8 tracks / 8 edges / 2 config surfaces / 1 ledger interface, generated by `05`'s own *rows, not code* rule; W1–W7 renumbered in order; graph and counts corrected |
| 14 | **Net-additive against the brief.** ≈20 mechanisms and 7 edges added, 14 forks opened, against ≈1 incremental cut — everything else was already claimed by `00` or `04`. ~29 named objects against `04`'s ruling that the irreducible set is **eleven**, never reconciled | MED | Stated plainly in `05` §12; reduction applied |
| 15 | **Unreconciled with the corpus it distils.** CIP-12 (attribution as second currency) and CIP-6 (disposition-reads-record) are the two nearest proposals and go unmentioned. The unit now carries **three independently-derived "second currencies"** with no statement of whether they are one axis or three | MED | Named as a condition on the headline |
| 16 | **An un-failable falsifier.** "A number whose only justification is completing the table" names no procedure — a sentiment, not a test; applied honestly it fires immediately | MED | Replaced with a fork dependency |
| 17 | **Missing guard.** `05` identified that fixed-rate conversion "would be easy to add by accident" and shipped no guard — §0.1 point 5 requires one | MED | Named as open work rather than left implicit |
| 18 | **Four unmarked cross-lane commitments** — FI (evidence producer), SE (ledger), characters (C3), FA (institutional Reputation) | MED | Marked as observations |
| 19 | **Two mechanisms for one axis.** Thesis/hypothesis and W6's authority both carry verdict *reach*. "Nearly free: one flag on a claim" is false accounting — the claim record is ABSENT, so the flag's cost includes the object it sits on | MED | Filed as a fork; not shipped |
| 20 | **An absence wearing an edge number.** Amplification's own row said "no owner anywhere in the tree" while sitting in the edge table — and was then cited as half the justification for a two-track verdict | LOW | Removed from the edge model; filed as a fork |
| 21 | **Unpriced liability.** The decorum operator reduces *mechanism* count but explodes *parameter* count — hundreds of authored cells replacing twelve `[SEED]`s, with no authoring bound, where `00` Fork B at least had the 40% invariant | LOW | Named; an authoring-budget fork added |
| 22 | Minor citation drift, none load-bearing: `dispatch:307-308`→`306-307`; `contract:65-77`→`69-77`; `primitives:15-16`→`16-17`; `Room` is two per-side floats, not one; a cross-reference to `04 §12` that belongs to `00 §4.2` | LOW | Corrected |

---

## §3. The methodological lesson

`05` was written under a correction that stopped a real error — collapsing trajectories that merely correlate. The
correction was right. **The instrument it produced was not**, and the failure mode is worth stating generally
because it will recur:

> A test that distinguishes "duplicate" from "distinct" is only decidable against a **fixed** system. Grading kills
> against what exists and rescues against what is proposed converts a pruning instrument into a licence, and it
> does so invisibly — every individual verdict looks reasoned.

The repair is two riders (`05` §0). The evidence that the failure was real, not hypothetical, is `05` §7.3: a
seven-row table with no holder dimension was rescued into a matrix indexed by holder, because the new track needed
content and content was found for it.

**A second lesson, cheaper to state and more embarrassing:** the falsifier that caught the headline error was
written by the author, published in the document, and never executed. §0.1 point 3 asks for a named falsifier *and
that test's outcome*. Naming it is not running it.
