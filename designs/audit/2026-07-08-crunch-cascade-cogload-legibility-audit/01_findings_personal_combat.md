# Personal / Scene Combat — Findings (adversarially verified)

**Canonical head:** `designs/scene/combat_engine_v1/` (README.md:14, CANONICAL, ED-900/904/1029).
R2 (closing-distance/facing/grip/contact redesign) merged; R3 (weapon-model consolidation)
in flight on PR #76 — this audit covers the merged R2 state.

## 1. Tracker inventory

Combat Pool `max(5, History+6)` (`combatant.py:117`, `core.py:27-32`, canon `params/core.md:161`);
Health `round(WI×(MW+1)+0.25×Str×End)` (`combatant.py:40-42`); Wound-Ob penalty +0.15 Ob(atk)/
+0.25 Ob(def) per wound (`config.py:65`, applied `systems.py:664,693,805`) — **shifts success
probability but is never surfaced as a labeled number**; ~15 continuous internal-only fields per
beat (`grip_position`, `lunge_depth`, `range_avail`, `facing`, `sel_head/dmg/gap/perc/pc`,
`initiative`, `poise`, `ready[]`, `commit`, `measure_gap/closed`, `opening_created`) — all
invisible to any consumer outside the Python module. **Momentum** (0–4, the universal
`params/core.md:84-93` tracker) — confirmed **zero read/write sites anywhere in
`combat_engine_v1/*.py`** (independently re-grepped by the critic pass). Combat's `disp`
(aggression axis, 1–7, `combatant.py:99`) collides in name with the unrelated NPC-relationship
Disposition (−5..+5, ED-912, `params/core.md:147`).

## 2. Interaction chain map

- **grip_position 2-cycle** — a genuine circular dependency was found and locally patched:
  `grip_target`'s drive term read `close_unwieldiness` at the *current* grip (the value it was
  computing), producing a hard 2-cycle (spear flips 0↔0.865 forever) — fixed by pinning the
  drive input to `grip=0.0` (`systems.py:172-189`, JD-9). **Verified verbatim** — the code comment
  itself documents the exact failure mode. The fix is a local pin, not a stated general invariant;
  the same bug class could recur under R3.
- **Initiative / poise** — both amplification loops, both explicitly capped and self-documented
  as required "by the NERS audit" (`config.py:116-128`, `INIT_CAP=1.5`, `POISE_FLOOR=0.5`).
- **Concentration** — floored at 0 but functionally a one-way ratchet *within* a single
  engagement: recovery only fires between bouts (`wrapper.py:362`), and an engagement can run up
  to 24 beats with no in-engagement recovery path.
- **Momentum** — unconnected. `core.degree()` routinely produces `'overwhelming'` results but
  nothing in the resolver reads or writes Momentum.
- **`seize` ability channel (vorschlag, sen_no_sen)** — dead-end, self-documented as such:
  "The 'seize' lever is DEAD (its pre-contact-seizure consumer was cut 2026-06-05)... do nothing
  when equipped" (`ability_primitives.py:15`).
- **Skills (`c.skill(axis)`)** — read at ~9 sites with no canonical acquisition/allocation rule;
  defaults to 0.0 (inert) unless hand-set in test harnesses.

## 3. Cascade check

No chain in the audited code is genuinely unbounded — the engine's authors have been unusually
disciplined about capping positive-feedback states (initiative and poise both explicitly justified
against "the NERS audit"; wound-Ob bounded by `max_wounds` 1–3). The one loop that *was* unbounded
(grip↔reach) was found and closed, though only by a local pin rather than a stated general rule —
flagged as a residual process risk for R3, not a live cascade.

## 4. Cognitive load

**The load-bearing finding of this lane, independently verified end-to-end by the adversarial
critic:** reading `wrapper.engagement()`/`fight()` in full (`wrapper.py:28–371`) confirms **zero
call sites read a player-supplied choice mid-engagement** — every branch (mode selection, defence
mode, commit depth, counter, grapple) resolves via `rng` draws against derived σ. In-fight player
decisions: **0**. Pre-fight decisions (once per build): ~5 (weapon/armor/tradition/skills/ability).
Trackers the *engine* consults per beat: ≈15, several requiring cross-file lookups into
`weapon_physics.py`/`geometry.py` (616 lines, 27 functions, currently zero player-facing
translation).

**Adversarial correction:** this gap is not an undiscovered defect. Ledger entry **ED-PC-0001**
(RATIFIED-AS-ACCEPTED by Jordan, 2026-07-05) confirms the absent player-decision surface is
**deliberate sim-first staging** — the player-input surface and threadwork hook (ED-911) are
scheduled as post-R3 increments, not an oversight. (ED-IN-0024 separately flags that this
ratification's own intent-provenance is circular — worth tracking, but doesn't change the
scheduling fact.) Treat as: real, current, and already on the roadmap — not a fresh finding to
re-litigate.

## 5. Legibility gaps (severity per critic-corrected verdict)

- **P1 — combat has no player-decision surface today.** Confirmed against code; blocks
  engine/UI-buildability outright, but is a *scheduled* gap (ED-PC-0001), not a silent one.
- **P2 (downgraded from producer's P1) — `sim/personal/combat.py` still implements the struck
  Combat Pool formula** `(Agility×2)+History+3` (`:47-48,127`). The critic pass confirmed this
  file carries a loud `[DEPRECATED 2026-06-23]` banner ("do NOT wire new game code through this
  file... reference/history only") — mitigating the severity from a live P1 buildability risk to
  a P2 dead-reference-drift hazard for anyone who greps past the banner.
- **P2 — `values_master.yaml` carries the same struck formula** (`:213-215,1150-1163`) plus a
  wound rule (`−1D Combat Pool only, no Ob penalty`, `:327-329`) that **ED-PC-0005 (ratified
  2026-07-08 — today)** just reversed again: wounds now add fractional Ob, never cut the pool
  (`combatant.py:16-19`). Banner-quarantined (ED-1084) but a live trap for grep-first workflows.
- **P2 — "Disposition" names two unrelated mechanics** with no canonical doc stating how combat's
  `disp` is derived or player-visible/settable.
- **P2 — Wound-Ob penalty is invisible** pre-commit, failing the legibility bar the contest
  rebuild states explicitly ("every number the resolver uses is a number the player can see
  before committing").
- **P2 — jargon with no player-facing translation** (`wield_heft`, `gap_precision`,
  `point_concentration`, `recoverability_factor`, `PoB_frac`, `close_unwieldiness`, `adef_cap`,
  `strike_concentration`, `sel_head/dmg/gap/perc/pc`) — downstream of the P1 above, not
  independent.
- **P3 — `derived_stats_v30.md` self-contradicts its own currency line** (`:2` CANONICAL, `:4`
  PROPOSAL, back to back).
- **P3 — stale inline comment** at `state_graph.py:42` ("Contact — BUILT, not activated (M-11)")
  lags the actual activation (`TRACE_KINDS`/`STATES` now include Contact; `wrapper.py:309-324`
  actively calls it). Note: the producer's supporting citation for "M-11 verified closed" was
  itself wrong (the cited punchlist line says the *opposite*, as of its 2026-07-02 date) — the
  comment is stale because of a *later* change, not because that punchlist closed it. Substance
  holds; provenance corrected here.

## New finding from adversarial pass

**The PC action set is being actively consolidated as of today (2026-07-08).** ED-PC-0007
(ratified from the pessimist subtractive-action audit, ED-IN-0027) merges/distills five resolver
rows (Feint→commit, Establish Distance+Escape merge, Disarm/Tie-Up/Retrieve merge into one
Contact-axis verb, Full Guard+Dodge distill) — net −5 resolver rows. This audit's action-inventory
analyzes a surface that is mid-consolidation; a re-audit after R3 + this consolidation lands would
need to re-run the tracker/chain tables above.
