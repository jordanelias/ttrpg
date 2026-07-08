# Inverted Critic Pass — Lane TW (Threadwork)

**Method:** independent Sonnet pass, read-only, judging each condemned action as-if-built per the charter's cardinal rule. Verified against `designs/threadwork/threadwork_v30.md`, `params/threadwork.md` (Three-Axis Ob System, TN table), `sim/thread/operations.py`, `canon/02_foundations_amendment_leap_mechanism.md` Amendment 3, and the 2026-07-04 hunt findings the dossier cites.

Two actions in this lane carry a subtractive verdict (DISTILL, REFINE). Five carry KEEP; three were spot-checked. No verdict in the dossier rests on build state — confirmed below.

---

## Condemned action 1 — Past-Oriented Pulling (attempt_past_pulling) — dossier verdict: DISTILL

**Steelman attempt (best case for keeping it as a standalone operation):**
The temporal-target concept is real Renaissance-adjacent content — contesting historical grievance, legitimacy, unresolved grief — and one could argue reaching into a past configuration is *categorically* different from reaching into a present one, such that a separate Ob methodology (recency, not Depth/Breadth/Distance) is not a defect but a correct recognition that "how long ago" is an axis the spatial Three-Axis system cannot express, and therefore POP's separateness is *earned*, not redundant.

**Why the steelman fails:**
1. Checked `sim/thread/operations.py:265-283` against `params/threadwork.md` §Three-Axis Ob System directly. POP's Ob computation (`pop_recency_ob.get(recency, ...)`) *replaces* Depth+Breadth+Distance entirely rather than adding a temporal term to it — meaning an Object-scale historical grievance and a Structural-scale historical grievance cost the *same* Ob (only recency matters), while every other operation in the lane gates cost by scale via the Three-Axis system. That is not "a fourth axis correctly kept separate," it's scale-blindness the other six operations don't have — a mechanical incoherence, not a principled design choice.
2. The corpus itself gestures at generalizing this rather than keeping it siloed: `params/threadwork.md`'s TN table has a live row for "POP Binding (Past-Oriented Lock or Dissolution)" at TN 9 — i.e., canon already contemplates temporal-targeting as a *modifier available to other operations*, not an operation-specific concept. No `attempt_past_locking`/`attempt_past_dissolution` exists in the design or the code; the TN row is an orphaned generalization pointing exactly where the dossier's remedy (fold recency into a Pulling/Ob-axis extension) would go.
3. Pool formula, degree table, Mending Stability consequences, and Fraying Bane are all "retained" verbatim from standard Pulling per the doc's own text (line 363) — the only deltas are TN+1, the Ob source table, and a flat −1 Coherence/MS surcharge. That is the textbook Abstractable failure mode (meta:34-37): a near-identical operation kept as a structurally separate sibling rather than a parameterized variant.

**Outcome: UPHELD.** DISTILL is correct and, if anything, the orphaned "POP Binding" TN row strengthens the case that the fix belongs at the Ob-axis level (generalizable to any past-oriented target), not just a Pulling-specific patch. No change to severity/verdict.

---

## Condemned action 2 — Mending (attempt_mending) — dossier verdict: REFINE

**Steelman attempt (best case for keeping Gap-repair as a single-tool, no-branch decision):**
Even with one legal tool, "when to Mend" could itself be the real decision: a practitioner weighs scarce Focus/Fatigue and Contact Rounds against other Thread operations, chooses which of several open Gaps to prioritize, and risks Partial/Failure (Mending Stability −2, no Gap progress) at Entrenched/Catastrophic Ob 6-7. Canon's own design note frames Catastrophic Gaps as needing "collective operations, the Einhir framework, or multi-season Mending arcs" — arguably three distinct *approaches* to the same repair problem, which would satisfy Q-robust's three-viable-approaches bar and rescue the KEEP.

**Why the steelman fails:**
Checked all three "approaches" against `threadwork_v30.md` §Mending and the Depth Ob table. All three — solo Mending, collective Mending, and "Einhir framework" Mending — resolve through the *same* `attempt_mending` operation and the *same* Ob-by-Gap-severity table; "collective" and "Einhir framework" are stated as ways to beat the Ob 7-8 math (more dice, better tools), not alternative mechanics or alternative philosophies of repair. That's one tool used at different scale of application, not three viable approaches in the Q-robust sense (which the charter ties to *visible traceable change* + *dramatic legibility*, i.e., distinct fictional postures a player could choose between). Timing/prioritization is a resource-allocation question layered on top of the single tool, not a second or third tool — and the charter's Q-robust bar is explicitly about approach-plurality, not just risk/timing on one approach. Also confirmed against `canon/02_foundations_amendment_leap_mechanism.md` Amendment 3 that the zero-cost asymmetry is philosophically load-bearing (restorative operations aligned with substrate tendency) and must not be touched — the dossier's REFINE already isolates the fix to Gap-repair's branching, not the cost, which is the correct scope.

**Outcome: UPHELD.** REFINE stands: zero-cost Mending is untouchable canon; the missing second legal branch (or explicit friction) on Gap-repair is a genuine Q-robust gap, not a build-state artifact — Mending is fully specified in prose and 1:1 coded, and the finding is about the *design's* branching structure.

---

## KEEP spot-checks (no full steelman required, sampled for over-generosity)

- **Weaving** (KEEP, Ω-d caveat re: Domain-Action parallel economy): checked against the cited hunt (`2026-07-04.../hunt_threadwork_exploit.md` LINE 3). The hunt's own counterweight holds up on inspection — practitioner-only gate (TS 50+, Approach Training), negative Domain Echo in Church territory, live Gap/Dissolution risk — so "a real decision survives" is not generous rhetoric, it's a verified reading of the source. KEEP not over-generous.
- **Locking** (KEEP, conditioned on ED-1010 resolving to a scale table): ED-1010 confirmed open in `canon/editorial_ledger.jsonl` (P1, "per-operation Coherence cap homeless + contradicted") — this is a real, already-tracked editorial fork, and the KEEP correctly frames itself as conditional on the *design* resolving one way rather than smuggling in a build-state excuse. Appropriately scoped.
- **Pulling** (KEEP, R-54 duplicate duration table dismissed as editorial defect): confirmed in `threadwork_v30.md` lines 330-337 — the R-54 correction only reshuffles the surplus-successes-to-duration mapping; the underlying decision (loosen a consolidated hold, risk Wound snap-back on failure) is unchanged by which ladder wins. Correctly not treated as a design flaw.

No KEEP verdict inspected shows over-generosity requiring downgrade.

---

## Build-state audit (cardinal-rule compliance check)

Re-read every `criterion`/`one_line`/`verdict` field (not just `build_state_note`) across all seven actions. None of the seven verdicts cites stub-ness, unwired-ness, or lack of a player-facing caller as a reason for KEEP/DISTILL/REFINE — every `build_state_note` is correctly quarantined as routing metadata with an explicit "not a verdict input" disclaimer, and cross-checking the actual reasoning (Three-Axis Ob mismatch for POP, restorative-taxonomy grounding + Q-robust branching for Mending, hunt-verified non-dominance for Weaving, ED-1010 for Locking) confirms all reasoning is design-intrinsic. **No correction needed.**

## Summary

| Action | Dossier verdict | Critic outcome | Final verdict |
|---|---|---|---|
| Leap | KEEP | not steelmanned (KEEP) | KEEP |
| Weaving | KEEP | spot-checked, sound | KEEP |
| Pulling | KEEP | spot-checked, sound | KEEP |
| Past-Oriented Pulling | DISTILL | UPHELD | DISTILL |
| Locking | KEEP | spot-checked, sound | KEEP |
| Dissolution | KEEP | not steelmanned (KEEP) | KEEP |
| Mending | REFINE | UPHELD | REFINE |

