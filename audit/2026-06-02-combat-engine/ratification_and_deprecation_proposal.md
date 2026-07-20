> **EXECUTED / HISTORICAL (2026-06-19).** combat_engine_v1 was canonized as the personal-combat resolver (ED-900) and `params/combat.md` deprecated 2026-06-04; `combat_v31/v32_proposal` DEPRECATED by ED-900. This 2026-06-02 staging proposal is superseded by those actions and retained for record only. Docket-level adopt-all ratification: ED-1029.

# Combat Engine v1 — Ratification & Deprecation Proposal
**2026-06-02 · personal-combat resolution · proposed canonization**

`[READ: designs/scene/combat_v30.md (canonical incumbent); references/canonical_sources.yaml; weapon_matchup_matrix_v2 + A0–A3 CSVs (external validation)]`
`[SELF-AUTHORED — bias risk: I built this engine; the canonization decision (structural) is Jordan's to ratify. This is a proposal with evidence, not a unilateral status change.]`

## PROPOSAL
Canonize **`designs/scene/combat_engine_v1/`** (committed this session, sha 6e9b6aa) as the **personal-combat
resolution system**, superseding the resolution layer of `designs/scene/combat_v30.md`. The engine is a modular,
multimodal, externally-validated resolver. Per the project contract, the *structural* canon decision — declaring
combat_v30's resolution superseded — is **Jordan's to ratify**; this records the proposal, the evidence, and the
deprecation set for that call.

## WHAT IS BEING CANONIZED
A modular personal-combat engine (655 lines, 6 modules) built and validated this session:
- **Architecture:** roles are objects (frame-safe; the role-inversion bug class is structurally gone). A wrapper owns
  the state-graph + A/B identity; a core owns canonical sigma-resolution (effective_ob / degree / roll, from the
  ratified r1/r8 sigma engine) + armour-aware damage; subsystems are uniform-contract modules.
- **Multimodal cross-tradition resolver** (`tradition.py`): each martial tradition is a COGNITIVE MODE — selection-
  weights over shared physical primitives (measure / commitment-window / contact-as-information), with cross-tradition
  FAMILIARITY (partial knowledge of others degrades the read). Grounded in the repo's own seven-axes/throughlines/
  bridge corpus. Lets German-longsword-vs-Japanese-yari resolve on one substrate.
- **Primitives** (all grounded in martial research): standing reach advantage (falls with armour); event-gated
  measure RE-OPENING (created moment: over-commit / won-defence / freed-hand push; reading-gated, readable);
  conditional TEMPO (grip/stance/fatigue, not static); movement LEGIBILITY (thrusts hard to read, swings/lunges
  easy); LEVER-ARM (redirect/bind from grip-vs-head length); DISPLACE-AND-STEP-INSIDE (set aside a committed thrust
  and close, with pull-back graze caveat); HALF-SWORD auto-switching form (mit dem kurzen Schwert); ARMOUR-DEFEAT
  with gap-thrust precision + a defender-armour shield + cut-collapse/percussion-rise rotation; FEINTING (capped at 3,
  short phase, readable, not overpowered); a 95% videogame upset cap.

## VALIDATION EVIDENCE (vs the external four-state weapon matrix — judgment model, not ground truth)
Cell-by-cell vs `weapon_matchup_matrix_v2` (A0 unarmoured → A3 full plate), mean |Δ| and direction-agreement:
| State | baseline (pre-fix) | current | 
|---|---|---|
| A0 | 38.8pp / 33% | **~23pp / ~74%** |
| A1 | 39.7pp / —   | **~28pp / ~61%** |
| A2 | 43.7pp / —   | **~27pp / ~75%** |
| A3 | 49.8pp / 37% | **~29pp / ~76%** |
The structural inversions (engine anti-correlated with reach; armour not rotating the ranking) are FIXED. Remaining
gap to the ≥80%/≤15pp target is magnitude tuning, not structure. Invariants hold: mirror 50, mastery dominant
(History 6v3 ~73–77, Reading ~93), traditions modest (~48), feinting mirror-neutral (50), no-one-shot (max blow 18 <
End2 Health 24), 95% cap intact.

`[CONFIDENCE: high on architecture/primitives/direction; medium on exact cell magnitudes — the matrix itself is an
expert-judgment model (its §0/§9), so direction+tier match is the bar, not the digits.]`

## DEPRECATION SET (proposed — Jordan to ratify the canonical_status changes)
- **`designs/scene/combat_v30.md`** — RESOLUTION LAYER superseded by combat_engine_v1. Propose `canonical_status:
  "PARTIALLY SUPERSEDED — personal-combat RESOLUTION replaced by designs/scene/combat_engine_v1/ (2026-06-02). Lore/
  flavor/non-resolution content retained."` (Do NOT delete; world-content and any non-resolution mechanics stay.)
- **`params/combat.md`** — already flagged DRIFTED (old engine: Pool=Agi×2+Hist+3, Stamina=End×5; unpropagated).
  Propose deprecate to `deprecated/params/` — the engine's config.py + core.py are the live parameter source.
- **`params/mass_combat.md`** — NOT in scope (mass battle is a separate system; untouched).
- Social contest, investigation, conviction, faction systems — NOT in scope; untouched.

## RATIFICATION CHECKLIST (for Jordan)
1. Approve canonizing `designs/scene/combat_engine_v1/` as the personal-combat resolver.
2. Approve the `combat_v30` `canonical_status` change (partial supersession) + add combat_engine_v1 to
   `references/canonical_sources.yaml`.
3. Approve deprecating `params/combat.md` to `deprecated/params/`.
4. Open items to finish post-ratification (magnitude tuning, not blockers): longsword-vs-spear (19 vs ~40 target) and
   longsword-vs-plate magnitude; A1 mail dials; feint-vs-elite-reader floor (currently collapses to ~5%, slightly
   over-punished); autonomous choke/lunge/feint decision policy (states are wired but not yet engine-chosen).

## STATUS
Engine committed (sha 6e9b6aa). This proposal committed alongside. The `canonical_sources.yaml` edit and the
`combat_v30` status change are STAGED here for Jordan's ratification rather than applied unilaterally (structural canon
authority). On approval they are one `safe_commit` each.
