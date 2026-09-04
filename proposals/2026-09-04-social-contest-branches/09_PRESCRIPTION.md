# 09 · PRESCRIPTION — what to do going forward

## Status: **PROPOSED (2026-09-04). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE. Nothing here runs.**
## Written by the orchestrator (Opus). **The Fable tier hit its usage limit mid-session**, so this is
## not the Fable-authored prescription the plan called for; the synthesis is Opus-tier and says so.
## Ranked by what is load-bearing on **the game**, per `CLAUDE.md` §0.1 pt 5 and §0.3.
## ⚠ **AMENDED TWICE, 2026-09-04. MOST OF THIS DOCUMENT IS WITHDRAWN.**
## §1.1 and §3 (Tier 2) — **out of scope**, parked in `OUT_OF_SCOPE.md`; Jordan did not commission work
## outside the social contest. §1.2 and §2 (Tier 1) — **seam work**, withdrawn on Jordan's *"ignore the
## seams, I am rebuilding a lot"* (2026-09-04). **What stands is §4 (the branches), §5 (meta-architecture
## posture) and §6 (process).** The measurements behind the withdrawn sections are preserved in place,
## because they say what a rebuild must not reproduce.

---

## §0 · THE THREE THINGS THAT CHANGED LATE, AND WHAT THEY COST

Three corrections landed after most of this session's work was done. Each narrowed a finding, and a
reader who skips them will act on a superseded picture.

1. **The social contest terminal is RATIFIED, not an unratified engine.** `ED-1057` (ratified
   2026-07-01) designs the per-juror ballot verbatim: *"each juror votes A iff
   `sharpness*(adv_A − adv_B) + per-juror-noise > 0`, so a juror can cross against the room (a lopsided
   room is near-unanimous, a close room is near a coin-flip)."* That is exactly `resolver.py:139`.
   **The engine-classification lens (Instance A/B/C, "wrong-engine defect") does not apply and its
   findings are withdrawn.** What survives from the NERS material is the **method** (`CLAUDE.md` §0.06
   per PR #364, and `14_NERS.md`'s scoring rules), which never depended on the engine taxonomy.
2. **Therefore the 87.7 % crisis-side win rate is not a defect of the terminal.** ED-1057 *designs for*
   "a lopsided room is near-unanimous". A lopsided input producing a lopsided verdict is the ratified
   behaviour working. **The defect is upstream, in what makes the room lopsided.**
3. **The `9`-member import-cycle figure is docstring-only**; the test asserts two families, not a member
   count. No cycle test blocks any change here.

---

## §1 · TIER 0 — SHIPPED BEHAVIOUR IS WRONG. Cheapest work in the session, no design authority needed.

### 1.1 · **WITHDRAWN — OUT OF SCOPE.** (The dead victory Political-Stability clause)

Verified, real, and **not part of the social contest.** Parked in `OUT_OF_SCOPE.md` §1.1 with its
evidence and the falsifier owed by either disposition. **Jordan ruled 2026-09-04: "leave it, file the
finding."**

### 1.2 · **WITHDRAWN — SEAM.** (The production-path gate that cannot see a kernel regression)

The finding stands (`test_mc_v18_regression.py` sums a counter `mc_v18.py:160` also increments for the
§10 vote, so it passes with zero kernel contests). But it is a test **of the seam path**, and the seam
is being rebuilt. Its fix is held, unlanded, in `stash@{0}` and should be re-derived against whatever
the rebuilt seam looks like rather than applied to the one being replaced.

## §2 · TIER 1 — **WITHDRAWN 2026-09-04. SEAM WORK.**

Both items were seam work and Jordan is rebuilding that layer: **§2.1** the faculty derivation at
`scene_dispatch.py:139` (`_emergency_council_parties`, a `[SEED]` bridge deriving the two sides from
incommensurable quantities — one faction's Legitimacy against the inverse of the *same* faction's
Stability), and **§2.2** the six parameters `scene_dispatch.py:300-301` fails to pass.

**The measurements survive the withdrawal and are worth carrying into the rebuild**, because they say
what the seam must not do again: 81.9 % of 4,979 councils fought at side-A faculty 1, 87.7 % won by the
crisis side, 74.8 % of echoes floor-clamped to no-ops, and **zero player decisions on the production
path** (all 846 traced moves the defaulted `logos_spammer`). A rebuilt seam that reproduces those
numbers has reproduced the defect.

**And one design question outlives the code it was found in:** whether an Emergency Council is one
faction in crisis — in which case it is **not a contest** and should not route to a contest resolver —
or two parties, and who the second is. That is Jordan's, and it is a question about the rebuild rather
than about the seam being replaced.

## §3 · TIER 2 — **WITHDRAWN 2026-09-04. OUT OF SCOPE.**

This section prescribed work on **territory ownership, mass-battle primitive parity, the degree-word
collision and Key id serialisation** — none of it in the social contest, and **none of it
commissioned.** Jordan's brief was scoped to the social contest system and its own components; the
orchestrator misread it as the whole repository.

**The findings are real and anchored, and they are parked in `OUT_OF_SCOPE.md`** with their evidence
and their overturning conditions. They are **not prescribed**, not ranked, and must not be weighed
against the social-contest work — which is the error this withdrawal corrects.

## §4 · TIER 3 — THE THREE BRANCHES. Do not execute the proposals as written.

`05_RECONCILIATION.md` establishes that none of the four documents is executable. In dependency order,
and **only after Tier 0–1**:

| # | work | blocker to clear first |
|---|---|---|
| 1 | **Spine** | rename `_resolve` (collides with `wrapper.py:303`, called at `:444`); **do not consume `margin()` in production during S0** — the document's own §9.1 states this mitigation and its change list contradicts it; add the 7 unlisted `_kernel_tests.py` break sites |
| 2 | **Inquiry** | the `formal_grounds_check` rewrite **silently regresses shipped faction code** — default the third clause `True` when the new parameters are absent, or gate under a new name; replace `KeyLog.of_type` (does not exist) with an iteration; re-run the dominance analysis against the **reachable** venue (`evasion_strikes=2`, not 1) |
| 3 | **Consensus** | **B1: the degree mapping is arithmetically inoperable** — `margin ∈ [−1,0]` against fixed bands at 0/1/3. Adopt the spine's `SUCCESS_UNIT` division. Then the antibody, which is inert on all three channels |
| 4 | **Negotiation** | reconcile `floor_a`'s two contradictory definitions; delete the false import-cycle argument and the falsifier built on it; re-argue `settle()`'s N-line (`destroy_record` exists); move the breach asymmetry into the exploit table as a **dominant strategy** |

**And one thing that is ready now:** `ED-SC-0020` is answered by architecture on rungs 4–5 — the burden
family already exists in disguise and `ProofBar:71-72` already carries Fork A's stall semantics. **Close
the row with that citation.** `ED-SC-0015` is *closable, not closed*: `ledger_sweep`'s only call site has
zero callers, so `ttl=1` is permanent today. Do not close it until that is fixed.

---

## §5 · META-ARCHITECTURE POSTURE

**PR #362 stays PROPOSED. Do not ratify it.** Three reasons, all from the document:
1. Its own §F names **two gaps that block the build outright** — `F.20`, *nothing founds a hearth or
   builds a site, so **the world only decays***; and `F.24`, every verb's `requires` is a prose string,
   so *"the resolver has no body"* returns as *"the resolver has thirty."* Ratifying a document that
   says it cannot build makes its `## Status:` line a claim the code cannot honour — the §0.05 failure.
2. **Ratifying would not buy dynamism.** Its in-season loop already resolves everything inside the
   season; its constraints are purity guarantees that buy the reproducible season hash.
3. **`F.20` is the real dynamism defect.** *"The world only decays"* is a far more direct threat to a
   living world than commit sequencing, and it is a gap to close, not a ratification to grant.

**Feed two things back to the chain:**
- **The in-scene binding ruling is already satisfiable** — no amendment needed. `§C.4:576` flattens acts
  across all scenes into one ordered fold; `D-49:871` forbids nesting, not same-pass resolution.
- **`§C.5.1` is a genuine finding.** A contest resolves its sides and stakes **once, from `proj`** — the
  barrier-2 pre-fold snapshot — so a later contest in the same fold cannot see an earlier contest's
  write. The document is internally asymmetric: `requires` reads `world_as_predecessors_left_it`
  (`:579`) while the roster reads `proj` (`:707`). **This is the same "time doesn't exist within a
  season" shape one level up**, and it is the most valuable thing this session can return.

**Merge PR #364.** It gives the NERS definitions a canonical home and closes **ED-929**, open since
2026-06-11, where two skills cited `canon/definitions.yaml` as their source and that file **has never
existed**. It is reference under §0.05, which is the correct status.

---

## §6 · PROCESS — four rules this session earned the hard way

1. **Reachability is a property of an EDIT, not a BRANCH.** Three of four proposals got their own
   control wrong, in three different directions. Ask it edit by edit; anything touching
   `systems/factions/`, `systems/settlements/sim/ledger.py` or `engine/cross_scale/` is reachable until
   shown otherwise.
2. **Check the assertion, not the prose above it.** Four instances, mine first: a docstring is not a
   gate, a `values:` line is not the `note:` above it, and a summary of a source is not the source.
3. **An ablation without a positive control is a story with numbers in it.** Arm P — a known-enormous
   intervention — was **invisible to the χ² test** that had just returned "not significant" for the
   real arm. Without it, *"the social contest is inert"* would have shipped: dramatic, wrong, and
   undetectable.
4. **A design document may not be cited as the reason a behaviour is correct** (§0.05), and the
   converse now has a worked case: **a mechanism may not be called unratified without checking the
   ledger.** ED-1057 ratified the thing this session nearly filed as an escaped engine.

---

## §7 · WHAT WOULD MAKE THIS PRESCRIPTION WRONG

- **It is Opus-authored, not Fable-authored**, and it synthesises audits it did not perform. The Fable
  tier was unavailable; a Fable pass over this document has not happened and is the obvious next check.
- **§2.1's default is a design opinion.** "Derive both sides from the same quantity" is architecturally
  conformant but it is not the only conformant answer, and the escalation is real.
- **The Tier 2 items rest on a reading with stated gaps** — `npcs` and `ui` unreached, `_architecture`
  surface-only, ~10,300 lines of combat and mass-battle interior unread. A `Turmoil` writer outside
  Python, or a mass-battle parity test under `tests/sim/`, would overturn §1.1 or §3.3 respectively.
- **Nothing here has run.** Under §0.2 this document is **paper**, and every item above is done only
  when its named falsifier executes and something ran it.
