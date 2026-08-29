# ARCHIVED — this directory is the PRE-CRITIQUE suite (v1)

## Status: SUPERSEDED (2026-08-29) by `proposals/2026-08-29-greenfield-systems-suite-v2/`
## Retained in place, unedited apart from the banner on each file, deliberately

**Why this is kept rather than retired.** It is the version an adversarial critique was run
*against*. Deleting it would leave the critique's findings citing a document nobody can read, and
would make the v2 deltas unverifiable — a reader could not check that a change was a correction
rather than a preference. Every path cited by PR #339 and by `registers/handoffs/HANDOFF_IN.md`
still resolves here.

**Do not build from this directory.** Six of its claims are known false — see below.

---

## What the critique found

A read-only adversarial pass on 2026-08-29 tested this suite against sixteen design requirements
across characters, factions, settlements and emergence. The result: **six structural failures, five
absences, four partials, one pass.** A structural failure means the design as written makes the
requirement *impossible* — an architecture change, not an addition.

The six root causes, and which are **errors** rather than omissions:

| # | Root cause | Class |
|---|---|---|
| **A** | **The one write rule was too tight.** It correctly forbids writing aggregates; it was extended to identity, and identity carried `place.kind` and `person.capability` — so settlements could not grow and characters could not progress | **error** |
| **B** | **Nothing initiates.** No ambition, goal or project primitive; every module fires from a vacancy, a directive or a player action | omission |
| **C** | **Faction personality was over-corrected away.** Deleting the per-faction branch was right; replacing it with nothing but the head's convictions left no institutional ethos for anyone to conflict with | **error** |
| **D** | **An action economy with no attention economy.** Budgets govern what an actor may do; nothing governs what reaches the player, so the season presents undifferentiated volume | omission |
| **E** | **The world has no outside.** Every input is endogenous — no season, no harvest, no plague, no exogenous pressure of any kind | omission |
| **F** | **Setting-blindness.** Caste, heritage, the Church, the Restoration Movement and Knots appear zero times in 3,793 lines. In this game those are not decoration on a political skeleton; they *are* the mechanics | omission |

**A and C are corrections.** While this directory stands unamended, it states something false about
what the design can do.

## What survived the critique, and is carried into v2 unchanged

The geometric decay law · `derive_ob` as the obstacle's single owner · `remit`-as-gate for
ED-IN-0201 clause 2 · the disclosure contract · vacancy-as-a-first-class-state · required tag
provenance · budget-buys-actions-never-modifiers.

## One honest note about the audit that passed this

The pessimistic NERS audit run over this suite was scoped to **resolution**, and the things it
examined did pass. It never asked whether the design could *express the game*, because the
methodology it follows is a rolling-engine diagnostic and that question is out of its scope. None of
the six root causes above is a NERS failure. That is a verdict on the instrument as much as on the
suite, and v2 states the scope limit rather than repeating it.
