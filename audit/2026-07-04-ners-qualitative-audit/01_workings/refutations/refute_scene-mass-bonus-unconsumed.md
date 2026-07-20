# REFUTE — scene-mass-bonus-unconsumed

## Candidate claim
§3.8 Scene→Mass bonus table (Social/Investigation/Combat win modifiers) declared in
`scale_transitions_v30.md` but "never referenced or hooked anywhere in mass_battle_v30.md's
own 7-phase turn structure." Criterion Q-smooth, diagonal, P2, NEW.

## What the text actually says
- `designs/architecture/scale_transitions_v30.md` §3.8 (L71–76): Social win → +1D relevant
  unit Command; Investigation win → +1D first Volley; Combat win → one free Reform action;
  "Modifier to most relevant unit; 1 turn duration. (PP-261, ED-151)."
- `designs/provincial/mass_battle_v30.md` §A.7 (L362–456): 7-phase structure. Grep for
  social/investigation/scene/PP-261/ED-151 in mass_battle → **no cross-reference**. So the
  *literal* fact (mass_battle does not cite §3.8) is TRUE.

## Why the DEFECT characterization is REFUTED
1. **Correct source-of-truth locality, not an orphan.** `scale_transitions_v30` is the canonical
   home for all eight cross-scale handoffs — its own coverage table (L315) reads "the eight
   handoffs (§3.1-§3.8) | covered." §3.6 Thread→Mass (L62–66) works the *same* way: the spec
   lives in scale_transitions and forward-references INTO mass_battle §A.10; the engine doc is not
   expected to reciprocally re-declare every incoming cross-scale input. Duplicating §3.8 into
   mass_battle would violate CLAUDE.md §8 "every rule lives once."
2. **Not "unconsumed" — it lands on named, existing mechanisms.** All three modifiers target
   quantities the §A.7 engine already computes: Command (Phase 1 declaration / Phase 5 Effective
   Pool, L440–443), first Volley (Phase 2, L379), Reform action (Reform Phase, L185 "Discipline
   restoration: Reform Phase only, +1 Discipline"). The bonus is a standard modifier on standard
   quantities, applied by the transition/scheduler layer — not orphan state that renders nowhere.
3. **It IS carried in the integration + machine surfaces.** `params/scale_transitions.md` L27
   restates the full table; `references/mechanical_terms_index.md` L1308 indexes §3.8. So it is
   integrated into the params/index layer, contradicting "never referenced anywhere."

## Intent evidence
- The eight-handoff architecture (one integration doc, subsystem engines stay clean) is a
  deliberate, safeguarded (single-source) design pattern — §3.6 demonstrates the identical shape.
- The transition's *provisional status* is already TRACKED: `tests/sim/sim_h01_to_h07…` L300/468/509
  flag **ED-151** — "Scene→Mass transition rules… PROVISIONAL. Confirm modifier values and whether
  unresolved combat carries across phases. P1-BLOCKER for Hybrid integration." `params/factions.md`
  L21 + `riskbreakers_identity.md` L88 carry "ED-151 Resolution — Scene→Mass Transition [FLAGGED]."
  So the genuine open question about this handoff has a tracking artifact.

## Genuine residuals (distinct from the finder's claim; not P2)
- **"Most relevant unit" is under-adjudicated for a no-GM engine** (which unit? deterministic
  selector needed) — a real Q-smooth wrinkle, but it is the ED-151 provisional-calibration
  question, not "never hooked."
- **Patch-citation collision (backwards axis):** §3.8 cites PP-261, but PP-261 corpus-wide means
  the Coherence-0→NPC threadwork transition (knots_v30 L242, arcs_05_09, ED-1011). ED-151's patch
  backing also conflicts: PP-328 (params/factions) vs PP-244 (tests/sim) vs PP-261 (scale_trans).
  This is a real provenance smell — but a SEPARATE finding, not the "unconsumed" claim.

## Verdict
REFUTED. The literal non-cross-reference is verified, but the characterization as a Q-smooth defect
("unconsumed / hooked nowhere") does not hold: the modifier lands on existing named mechanisms,
lives correctly in the single-source integration doc + params + index, and duplicating it would
break the single-rule invariant. The North Star cross-scale incentive (win a social scene → army
fights better) is already live and specified. The genuinely open facet (modifier calibration +
combat-carry) is tracked under ED-151. Fixing the finder's stated item widens no choice-space.

Intent: DELIBERATE (deliberate single-source handoff architecture, mirroring §3.6).
Duplicate_of: ED-151 (the transition's provisional integration status).
Revised severity: P3 at most (doc cross-ref hygiene / the tracked ED-151 residual is ranked
elsewhere; the finder's specific "unconsumed" framing does not reach P2).
