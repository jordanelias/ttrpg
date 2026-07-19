# Refutation notes — finding `no-interaction-model-6of7-scales`

Role: adversarial skeptic. Default REFUTED unless evidence holds.

## The finding
Claim: only Agôn contest has a current-era player-interaction model; combat, domain/settlement,
faction strategic, thread ops, mass battle, articulation have none and no live index entry
commissioning one; GM-removal mandate unmet for ~6/7 scales. Criterion Q-robust, top-down, P1, NEW.

## What the cited text actually says
- `player_interaction_walkthrough_v1.md` — status **DRAFT**, explicitly scoped to "the one game
  that is fully built (Agôn/Formal Contest)" (§ intro, lines 12–13). §4 exists precisely so the
  pattern generalizes ("so Stage 2–4 don't lock in an Agôn-only UI"); §5 flags Godot rendering as
  Gate-0-blocked. So the doc is self-aware it is a **pilot template applied once**, not a claim of
  completeness. Literal fact ("only Agôn has a current-era walkthrough") = TRUE.

## Load-bearing claims that DON'T hold
1. **"6 of 7 scales have NONE."** FALSE as stated. `designs/ui/valoria_ui_ux_v4_1.md` is a
   comprehensive **"Godot-development-ready interface specification,"** status **CANONICAL**,
   14 parts + 5 appendices, each Part carrying a **"What the player sees"** surface description,
   rendering **all 19 v30 canonical design docs** (combat, settlement, faction, thread, etc.).
   That is a player-facing / GM-removal design surface for every scale. It is dated 2026-04-16
   (pre-d+σ) so it is *stale in mechanics*, but it is not a void.
2. **"No live index entry commissioning one."** FALSE. `references/canonical_sources.yaml §ui_ux`
   (lines 493–496) registers `valoria_ui_ux_v4.md` + `valoria_ui_ux_v4_1.md` as live canonical
   sources — a machine-readable index entry. Not in `canon/supersession_register.yaml`, not retired.
   The finder's own lens doc (`lens_playability_legibility.md` §11, 28–29) narrowed to
   "current-era" to sidestep the UI spec — but the FILED finding drops that qualifier and asserts
   an absolute void, which overstates.

## Intent evidence (deliberate + safeguarded)
- Decision 5 (2026-07-01), `HANDOFF.md`/`HANDOFF_SC.md` lines 54–61: the player-interaction model
  is a **NEW standing deliverable discipline**, seeded ahead of Stage 6, deliberately piloted on
  the one fully-built contest game first, with Stage 4 owning per-game divergence. Staged-by-design.
- Even within social contest, only 1 of 4 games (Agôn) is built; Negotiation/Inquiry/Consensus are
  Stage 4 (charter: Stage 4 next). Generalizing to 7 scales now would be premature.
- Godot player-facing surface is **PROPOSED, Gate-0 unexecuted, 1/27 modules** (CLAUDE.md §6). The
  absence of built player-interaction for other scales is the deliberate pre-implementation state
  of a design-source repo, not an accidental gap.
- CLAUDE.md §10 / holonic doctrine: "promote a role only after it recurred" — piloting a pattern on
  one scale before commissioning it corpus-wide IS the repo's stated discipline.

## Re-judged severity vs North Star
Fixing this (writing 6 more walkthroughs now) does not widen meaningful choice today — the other
scales/games aren't built and the Godot surface is Gate-0-blocked by design. The real residue is a
low-severity forwards/backwards concern: the current-era contest walkthrough discipline has not yet
been reconciled with, or extended over, the older stale v4.x UI spec across scales. That is currency
debt, not a P1 North-Star blocker. P3 at most.

## Verdict
REFUTED as a P1 Q-robust defect. Underlying fact real but mischaracterized: deliberate,
safeguarded sequencing + an existing (stale) canonical UI spec covering all scales = not a void,
not accidental, not deliberate-without-safeguard. Intent DELIBERATE. Not a ledger duplicate
(decision 5 is contest-scoped, no ED tracks a cross-scale player-model gap). Revised severity P3.
