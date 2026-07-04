# Refutation notes — pc-legibility-fails

## Claim under test
"Dramatic-legibility test fails from personal_combat's state alone — no goal/intent field, no
political-stake naming, no season-clock hook; the fight resolves as a synchronous numeric event."
Criterion Q-robust, direction top-down, P2, novelty NEW.

## What the criterion actually is (01_criteria_ners_lineage §(a),(e); charter §Criteria)
The dramatic-legibility test is the **game-state / screen-level** playability bar: "can a designer
read the game-state and answer whose position is at risk / what each actor wants / what happens if
no one acts next season" — requiring "a human and a screen," per `workplan_v2_throughline_2026-04-26`
§5. It is NOT specified as a per-subsystem-in-isolation gate. Applying it to the innermost 1v1
tactical resolver "from this subsystem's state alone" is a category error: season-clock hooks and
political-stake NAMING are the province of the wrapping layers (scene-slate, faction, articulation),
not the dice engine. `01_criteria §(e)` further cites `2026-05-08-meta-audit-immersion.md`: a system
"can pass N/E/R/S and still destroy immersion if it surfaces too much of itself to the player." So a
resolution engine deliberately NOT surfacing its numeric internals as narration is a design virtue,
not a defect — the finding inverts this.

## Factual errors in the claim
1. **"no goal/intent field" — FALSE.** wrapper.py models disposition/intent directly:
   `disp_lean`/`DISP_INIT_K` (aggressive temperament drifts Vor up, cautious cedes it — lines 59–61),
   `tradition` channel-weights (line 146), `commit_depth` skewed by disposition + wariness (line 135).
   These are the combatant's intent-analog state, live per-beat.
2. **"no disposition/intent surfaced as narration" — FALSE.** The TRACE SEAM (wrapper.py lines 8–15)
   exists *explicitly* so "the narrator and the branch explorer can reconstruct the local probability
   of every alternate branch" — every decision node `_emit()`s the inputs it consumed. Narration is a
   deliberately separate layer (articulation = universal sink, 02_interdependency §(a) edge 11); the
   engine "emits facts; probability math lives in the workbench." The absence of narration text *in
   the resolver* is architecture, not omission.
3. **"the fight resolves as a synchronous numeric event"** — combat IS a resolution engine; that is
   correct-by-design. And it is NOT inert: `scene_combat_design_v1.md` §Roll-up emits
   `scene.combat_resolved{outcome, participants, casualties, wounds_inflicted}` plus per-bout
   `scene.combat_felled{actor_id, by_actor}`. §Churn-positivity is an explicit design axiom: target
   selection → `by_actor` → NPC grudges; outnumber → swarm lethality; flee/reinforce → `rout` vs
   `withdrawal` → faction ripples; wounds → scars. Political-relevant content IS produced; the world
   layer names the stakes from it.

## Intent evidence (DELIBERATE, safeguarded)
- Wrap-never-fork stance (§Architectural stance) + articulation-as-sink (interdependency §11): a
  deliberate scale separation — combat produces Keys, downstream layers render drama.
- The trace seam is a purpose-built narration hook; churn-positivity + the WS-1 coverage harness are
  a safeguard against inert combat transitions (§Churn-positivity: "Any scene mechanic that produces
  no distinguishable Key/state delta is suspect").

## Genuine residual — and it is KNOWN
The one real gap in this territory is that combat's out-edge does not actually *reach* the political
layer: `scene.combat_resolved` is **declared-but-unconsumed** (02_interdependency §(a) edge 2 +
§(d); module_contracts personal_combat gap_notes) and combat has no threadwork interface (**ED-911**,
KNOWN P1, and charter calibration list). ED-911's substance is resolution-scope (ranged/group/thread),
so not an exact duplicate of a *legibility* claim, but the "stakes don't propagate outward" concern is
the declared-unconsumed edge — a KNOWN-UNTRACKED-to-KNOWN-TRACKED item, not a NEW P2 discovery.
Re-reporting it as novel Q-robust failure is precisely the calibration failure the charter forbids.

## Verdict
REFUTED. The criterion is misapplied (per-subsystem vs game-state), two of three factual sub-claims
are false against wrapper.py, and the residual is the known declared-unconsumed edge / ED-911.
Intent DELIBERATE. Revised severity P3 (debt on wiring the existing out-edge, already tracked).
