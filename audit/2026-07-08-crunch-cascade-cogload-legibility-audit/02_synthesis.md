# Crunch-Cascade / Cognitive-Load / Legibility Audit — Synthesis

**Date:** 2026-07-08. **Scope:** all 9 active subsystems per `CURRENT.md`. **Method:** per-
subsystem sonnet-tier audit → independent opus-tier adversarial critique (re-opened every
citation, hunted for overstatement/staleness/refutation) → this synthesis. Full per-subsystem
detail: `01_findings_<subsystem>.md`. Workplan and methodology: `00_workplan.md`.

**Vetting note (Class A, self-exempting):** this audit is an analytic instrument, not itself a
design decision — findings below are evidence for design/engineering triage, not verdicts. No
canon file has been edited as part of this audit; ED-ledger filing for the new items flagged in
§4 is a recommended follow-up action, not executed here.

---

## §0 — Verification disposition ledger

Every finding below has passed an independent adversarial re-verification pass (9 critic agents,
one per subsystem, each instructed to default-skeptical and actively hunt for reasons to refute).
Outcome across ~200 discrete findings:

| Outcome | Count (approx.) | Pattern |
|---|---|---|
| CONFIRMED as-is | ~170 (~85%) | Citation, quote, and conclusion all held up |
| Downgraded/caveated | ~20 | Real finding, overstated severity or missing context |
| Refuted outright | 2 | 1 knots.py finding overtaken by a same-day unrelated fix; 1 mass-battle constant-rename claim was speculative |
| New findings from critics | ~10 | Missed mitigating rulings, missed newer resolutions, one latent cross-doc inconsistency |

**The single largest systematic error class was currency staleness, not fabrication.** Five
findings across three lanes (articulation ×3, faction ×1, settlement ×1) were accurate
descriptions of a real gap that had, unknown to the producer, already been **ratified-as-accepted
by Jordan on 2026-07-05** — the fix direction is decided, only execution is pending. These were
corrected in the per-subsystem files from "open, needs adjudication" to "accepted, awaiting
execution." No finding's core mechanical substance was overturned; two severity ratings moved
(both P1→P2, both because a deprecation banner or a ratified deliberate-staging decision
mitigated what looked like a live defect).

---

## §1 — Cross-system cognitive-load ranking

Benchmarked against the corpus's own stated ceilings (2026-05-08 immersion audit: 3–4
consultations for personal scenes, 7 at ceiling for strategic decisions):

| Rank | Subsystem / combination | Approx. load | vs. corpus ceiling | Note |
|---|---|---|---|---|
| 1 | **Thread ops embedded in Mass Battle** | ~55+ trackers/decisions combined | ~8× strategic ceiling | The 2026-04-04 audit's 19.4/EXTREME score has, if anything, gotten worse — mass battle's internal state has grown strictly more granular since (per-subunit Discipline/Morale/rout, per-cell facing/stamina) with nothing reducing the Thread side |
| 2 | **Mass Battle alone** | ~28 own-side / ~50+ incl. enemy mirror | 7–10× strategic ceiling | One Phase-1 declaration pass for a 4-subunit army already exceeds this by itself |
| 3 | **Social Contest (Agôn)** | 13 consult items/exchange | >3× personal-scene ceiling | The one game-shape that's actually implemented; will worsen when Stage 4 adds 3 more shapes |
| 4 | **Faction/political strategic turn** | 9–10 trackers | ~1.3–1.4× strategic ceiling | "Whose position is at risk" unanswerable from any single stat |
| 5 | **Personal combat** | 0 player decisions, ~15 engine-internal trackers/beat | N/A (no player decision point exists yet) | Currently the load is entirely absorbed by the engine — inverts the moment a Godot combat UI is built |
| 6 | **Settlement/territory (per settlement)** | 4–6 values, scales linearly with settlement count, no aggregation UI | within ceiling per-settlement, unbounded in aggregate | A 3-settlement governor already juggles 12–18 items with zero dashboard |
| 7 | **Threadwork (single op)** | ~14 trackers, ~10 decisions | ~2× the richest personal-scale ceiling | Legitimately rich by design; ~1/14 of the load is pure MS/RS naming-tax overhead, not decision content |
| 8 | **Dice/resolution core (single roll)** | 5–6 sub-decisions/lookups | — | Multi-table, not single-step, even before subsystem-specific pool selection |

**Peak finding:** Thread-during-Mass-Battle remains the single highest cognitive-load combination
in the corpus, and nothing in the last three months of work has reduced it — the mitigating
mechanism (PP-201/204) is still literal GM-address text with no engine-executable analog, in a
repo whose explicit premise is "there is no GM."

---

## §2 — Cascade discipline: the good news

Contrary to what "crunch cascade" audits often find, **most subsystems are actually well-
disciplined about capping feedback loops.** Personal combat's authors explicitly cap initiative
and poise "as required by the NERS audit"; social contest's Rattled/Concentration spiral and Chain
Contests both terminate by hard rule; faction/political's two genuine cascade risks (Stability
collapse, Wealth/Military ratchet) were each found and closed with sim-verified caps within the
last several weeks; threadwork's historical ×3 mass-battle drain is confirmed resolved to a
bounded additive model. **The one loop that was genuinely unbounded and uncaught before this audit
cycle — personal combat's grip↔reach 2-cycle — was already found and locally patched** (though
only by a pin, not a stated general invariant, so the same bug class could recur under R3).

**The exceptions are at the seams, not within subsystems:**
- **Cross-scale propagation (the architecture underlying every aggregate-up/distribute-down
  hop):** proven to terminate within a tick, but explicitly **not proven to converge across
  ticks** — the spec's own words: "It can persist at bounded, non-decaying amplitude for the
  entire campaign... the guarantee is TERMINATION-ONLY, not convergence." The load-bearing
  `decay()` function has zero specified shape, and the D.6 double-count question (does a
  down-targeted settlement write overlap what the up-aggregate reads?) is the spec's own
  self-identified "confirmed driver of non-convergence," unresolved.
- **Mass battle's `subunit_combat_pool` applies the general's full Command to every sub-unit
  independently** — possibly allowing spatially-separated fronts to each fight at near-full
  strength simultaneously. Explicitly flagged by the design team as undecided, gated on a Jordan
  ruling.
- **Articulation's Bonded-NPC starvation path** is a narrative-legibility dead-end, not a numeric
  one: the accumulator meant to guarantee eventual rendering cannot actually rescue an NPC whose
  Keys never match one of ten trigger types — confirmed by direct control-flow trace.

---

## §3 — Consolidated legibility register (cross-system, ranked)

### P1 — blocks play or engine-buildability

1. **Personal combat has zero player-decision surface today** (`01_findings_personal_combat.md`
   §4–5) — the entire engagement loop resolves via RNG with no mid-engagement player input. A
   *scheduled*, ratified gap (ED-PC-0001), not a silent one — but still the largest single
   blocker to a playable combat scene.
2. **No player-facing UI model exists for combat, mass battle, faction/political (per the
   corpus's own prior audit), settlement/territory, or threadwork.** Social contest has exactly
   one implemented, DRAFT walkthrough (Agôn only) — the sole template in the entire corpus, and it
   has been applied once. The one broad player-facing spec that once existed
   (`designs/ui/valoria_ui_ux_v4_1.md`) predates the entire current generation and is absent from
   `CURRENT.md`'s index.
3. **Combat Pool is defined five different ways across the corpus, and the one typed-export
   pipeline built specifically to prevent this kind of drift doesn't cover it** — the exporter
   only reads `config.py`; the Pool formula lives in a sibling module (`core.py`) it never
   touches. A Godot implementer following "regenerate from JSON, never hand-transcribe" would find
   no Pool formula there at all (`01_findings_board_game_dice_core.md` §3).
4. **`params/board_game.md`, the CURRENT.md-designated canonical head for the Board Game row, is a
   broken index** — every one of its 18 links 404s against the actual file layout.
5. **The MS/RS world-track naming split is worse than previously scoped: the canonical Threadwork
   head contradicts itself** (its own Part Five header says "Rendering Stability," its own first
   subsection two lines later says "Mending Stability"), and its co-filed cross-system spec uses
   RS exclusively. Direction is decided (MS wins) but unexecuted.
6. **The cross-scale propagation spec's own determinism proof depends on a sibling canonical doc
   (`key_substrate_v30.md`) that violates the spec's own ordering rule** — a live, verbatim
   self-contradiction between two CANONICAL documents about each other, which the propagation spec
   names but cannot fix itself.
7. **The cross-scale up/down feedback loop's convergence depends on an entirely unspecified
   `decay()` function** with zero cited form, and on an unresolved double-counting ruling (D.6) the
   spec itself calls the "confirmed driver of non-convergence."
8. **Mass battle's formation dice-modifier table (Shield Wall/Wedge/Skirmish/Column) has no live
   engine consumer at all** — a Godot dev implementing from the prose table alone would build dead
   mechanics.
9. **Mass battle's PP-201/PP-204 Thread-risk-disclosure mechanic is literal GM-address text**
   ("the GM should confirm...") with no engine-executable analog, in a repo with no GM — exactly
   where cognitive load peaks (Thread-in-Mass-Battle, §1 above).
10. **Faction count itself is unreconciled (4–8 across four docs)** — a foundational ambiguity
    blocking any faction-scoped binding work.
11. **Settlement/territory has a live, open rule contradiction** (ED-SE-0002: do personal-scale and
    governor Order/Accord changes stack in the same settlement/season, or not? Two canonical docs
    say opposite things) plus several named-but-numerically-undefined trackers (Population, Trade,
    Naval, Piety Influence, Garrison Capacity) and two mechanics (§4.7/4.8) that reference a
    "settlement Wealth"/"settlement Accord" that don't exist at settlement grain.
12. **Only one of social contest's four planned game-shapes (Agôn) is implemented** — Consensus,
    Negotiation, and Inquiry all raise `NotImplementedError`. Compounding this: the campaign's
    actual dispatch path resolves contest scenes through a **legacy stub**, not the sophisticated
    kernel this and prior audits treat as canonical — a reachability gap larger than the one
    originally flagged in this space.
13. **Articulation is wholly blind to victory-era world-state transitions** (MS=0/IP=100/
    all-dissolved) — no Key type exists for them at all. Already Jordan-accepted (ED-IN-0014),
    execution pending.

### P2 — causes ambiguity (selected; full lists per subsystem)

- Every core faction canon doc save one self-contradicts its own CANONICAL/PROVISIONAL status
  line; articulation's head does too.
- "Disposition" names two unrelated mechanics (combat aggression axis vs. NPC-relationship track);
  "Knot Strain" names two unrelated mechanics (opposing-ops penalty vs. bond-strain gauge);
  "cohesion" (mass battle, `hp/hp_max`) is one character from "Coherence" (the core Thread stat);
  "Turmoil" and "Strain" are used interchangeably in one doc with no identity statement.
- Wound-Ob penalties (personal combat) and stasis/genre bonuses (social contest) are both live
  resolver inputs that shift outcomes with no player-visible surface — direct violations of the
  contest rebuild's own stated legibility principle ("every number the resolver uses is a number
  the player can see before committing").
- The Bonded-NPC narrative-starvation path (articulation) and the battle-conclusion self-
  contradiction (§3.1 vs. §6.4 of the same doc) are both real, though both are already
  Jordan-accepted fixes awaiting execution, not open decisions.
- `sim/personal/combat.py` and `references/values_master.yaml` both still carry struck Combat Pool
  formulas — mitigated by deprecation/quarantine banners, but live traps for grep-first workflows.
- CI Mass Seizure drifts across three canon sources with no resolving ED; a residual "RS x3" line
  in threadwork's mass-battle sub-case was never reconciled against the general strike.

### P3 — polish (see per-subsystem files for full lists)

Stale inline comments, orphaned unbannered docs, jargon-without-translation across every lane,
and several honestly-logged known trade-offs (faction's "reward inaction" loop, mass battle's
degenerate multi-root default).

---

## §4 — Cross-cutting patterns worth naming explicitly

1. **The UI/legibility layer is the corpus's single biggest structural gap, not any one
   mechanic.** Every subsystem's internal math is, on the whole, well-bounded and reasonably
   disciplined (§2). The recurring failure is that almost nothing has a player-facing translation
   layer at all — six of nine subsystems have *no* player-interaction model, and the one that
   does (social contest's Agôn walkthrough) is a DRAFT covering one of four planned game-shapes.
   This is the corpus's own "no GM — the engine resolves everything" premise colliding with a
   design layer that still assumes a human will narrate the gap.

2. **"Ratified but unexecuted" is a recurring process pattern.** At least five findings across
   three lanes (articulation ×3, effectively also touching faction and settlement) turned out to
   be gaps Jordan had already resolved in direction on 2026-07-05, just not yet implemented. This
   is not a criticism of the decisions — it means the corpus's execution queue is running behind
   its decision queue in a way that makes fresh audits re-discover already-settled questions.
   Worth a standing habit: check `canon/editorial_ledger.jsonl` for a `status` before filing a
   "needs Jordan" recommendation.

3. **Naming collisions cluster around exactly the trackers with the most downstream
   consequences** — MS/RS (feeds faction Mandate, CV, settlement Order, the Revelation Curve),
   Combat Pool (feeds every combat resolution), Disposition (feeds NPC AI, faction relations, and
   combat temperament simultaneously under one name). The legibility tax is disproportionate to
   these trackers' 1-of-many share of total tracker count precisely because they're the ones that
   fan out furthest.

4. **The typed single-source-of-truth pipelines that exist are good ideas with real coverage
   gaps.** The `combat_engine_v1.json` export is exactly the right pattern (CI round-trip-checked,
   "never hand-transcribe") — but it doesn't actually cover the one value (Combat Pool) most
   central to the audit that prompted its creation, because the exporter and the Pool formula live
   in sibling modules that were never wired together.

---

## §5 — Recommendations

1. **Treat the P1 register (§3) as the actionable punch list.** Items 5, 6, 7, and 13 are cheapest
   to close first (they're already-decided or narrowly-scoped: MS/RS pick a name and propagate;
   fix `compute_observers` to preserve order; specify `decay()`'s functional form or explicitly
   flag it [FIAT]-pending-calibration; execute the already-accepted ED-IN-0014 Key registration).
2. **Before filing any of these as new ED entries, check `canon/editorial_ledger.jsonl` first** —
   per §4.2, several of these may already have a disposition that just hasn't propagated into the
   design docs yet.
3. **The UI/legibility gap (§4.1) is the highest-leverage single investment** — a "does the player
   see this before committing" pass, subsystem by subsystem, using the social-contest walkthrough's
   own stated principle as the template, would close a large fraction of the P2 register in one
   motion rather than fixing each hidden-value/jargon item individually.
4. **Combat Pool's exporter gap (P1 #3) is a template bug, not a one-off** — worth checking whether
   other Class-C typed exports have the same sibling-module blind spot before trusting them as
   single sources of truth.
5. This audit did not modify any canon file. Filing the above as ED entries, and ratifying any
   naming/severity calls, is Jordan's next step, not this audit's.
