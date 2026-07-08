# PROPOSED — throughlines_meta.md §8.2 extension (subtractive disposition addendum)

> ## Status: PROPOSED (2026-07-08, pessimist-action-audit). NOT canon until Jordan rules the ed_options docket. Do not flip any `## Status:` line, ledger field, or `CURRENT.md` on this text alone. Filed under Lane IN; anchor ED-IN-0027. Merge-ratification (CLAUDE.md §2, ED-1094) applies only once the docket is ruled and this text is intentionally landed — it must not ride in on a routine-work PR.

## §8.2-A · The subtractive disposition (extends §8.2's build/wire/redesign/flag/iterate routing)

§8.2 today routes every failed check to a *constructive* disposition — build, wire, redesign, flag, or iterate. It has no verdict that says *this action should not exist, or should exist only as part of a more general one.* This addendum supplies that missing half. It is the canonical mapping from the existing N/Ω/Q criteria and the Failure Lexicon (meta:157-173) to a **subtractive verdict**, so that scope can be *reduced* upstream of realization rather than only *added to* downstream of it.

### §8.2-A.1 · The cardinal rule (binding on every subtractive verdict)

**Judge as-if-built, never by build state.** For any action, evaluate how it *would* contribute to the game if built as its design intends. Stub-ness, unwired-ness, unbuilt-ness, and Godot-unported status are **orthogonal to the verdict** and appear only as `build_state_note` routing metadata for the additive resolution plan. A never-built action whose realized contribution is load-bearing is a **KEEP**; a fully-built action that would be dominant or redundant even when realized is a **CUT**. **Any subtractive verdict that cites build-state as a reason is invalid by construction.**

### §8.2-A.2 · The disposition table (canonical trigger → subtractive verdict)

| Canonical signal (judged as-if-built) | Verdict | Semantics |
|---|---|---|
| N-fail — even realized, not a load-bearing leadership dynamic (Fantasy imposition, meta:34) | **CUT** | remove the action; it models nothing real |
| Duplicate coverage (N, meta:35) — two actions do the same job even if both built | **PRUNE / MERGE** | collapse to one; PRUNE if one is re-homed to another lane, MERGE if both live in-lane |
| Abstractable / Edge-case (N, meta:36-37) — folds into a general rule with no lost decision | **DISTILL** | dissolve the standalone action into an outcome-branch/parameter of a more general verb |
| Q-elegant fail (meta:114) — even well-built, not restatable after one read | **REFINE** | keep the action, simplify the design until it is one-read-legible |
| Dominant strategy (Ω-d, М-6) — if built, a strictly-best no-brainer that doesn't pay its cost | **CUT / PRUNE** | remove or fold; a free win is not a choice |
| Flavor-only (Ω, Μ-γ, М-3) — adds no decision the player weighs | **CUT / DISTILL** | CUT if inert; DISTILL if a general verb can carry the flavor |
| Personal-only / Strategic-only (Ω-a / Ω-b) — no cross-scale consequence | **PRUNE signal** | re-home or fold unless a distinct in-scale reason survives |
| Passes N + Ω + Q as-if-built, under adversarial attack | **KEEP** | whether or not any code exists yet |

### §8.2-A.3 · Verdict ladder (strength order, least→most removed)

`KEEP → REFINE → DISTILL → MERGE → PRUNE → CUT`. REFINE and KEEP preserve the action; DISTILL/MERGE preserve the *decision* while dissolving the *packaging*; PRUNE/CUT remove both. Prefer the weakest verdict that resolves the failure — DISTILL a duplicate into a branch before CUTting it; REFINE an illegible rule before DISTILLing it.

### §8.2-A.4 · The intent gate (applied to the design, never the code)

Every subtractive verdict carries one gate:
- **DELIBERATE** — the design intends this contribution; the subtraction is a considered scope call.
- **NOT-INTENDED** — the contribution conflicts with a foundational premise (e.g. the no-GM invariant) or an established ratification.
- **UNDETERMINED** — design intent is genuinely unresolved; the verdict flags a decision Jordan owes.

*"It isn't wired/built/ported yet"* is **never** a gate value — it routes to the additive resolution plan, which already owns wiring debt.

### §8.2-A.5 · The complementarity requirement (what makes a cut a scope cut)

A subtractive verdict is a **scope reduction** only if it names the downstream resolution-plan Stratum, OPT item, docket entry, or lane task it *retires or shrinks*. **A row that cannot name downstream work it removes is not a cut — it drops to an ordinary §8.2 finding** and routes back to the constructive dispositions. This is the checkable boundary with the additive Stratum A→E program: the subtractive audit only earns its keep by removing deployment surface the additive program would otherwise spend effort on.

### §8.2-A.6 · The inverted-critic gate (a CUT/PRUNE must survive being saved)

No CUT, PRUNE, MERGE, or DISTILL is final until an **independent adversarial pass has steelmanned the action** — argued, as-if-built, why it should be KEPT — and *failed* against direct source inspection. A subtraction that cannot withstand an honest attempt to justify the action's existence is overturned. (In the 2026-07-08 pilot, this gate overturned 2 of 37 candidates and softened 2 more; it re-grounded every survivor against source text rather than dossier paraphrase.)

### §8.2-A.7 · Ratification path

This addendum is **PROPOSED**. Individual subtractive verdicts are ratified only by Jordan ruling the `ed_options.md` docket; acting on any CUT/PRUNE is a separate Jordan-ratified follow-up. Per ED-1094, if a future PR intentionally lands this §8.2-A text as canon, that merge ratifies it — but it must be landed *as the point of the PR*, flagged in the body, never bundled into routine work.
