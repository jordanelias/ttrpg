# Valoria Combat Integration — Handoff

**Date:** 2026-05-15
**Last commit:** `b29c0c5` (Session A audit)
**Stopped at:** Pre-Session B, due to context >75% and GraphQL rate limit hit
**Resume with:** Fresh chat, `bootstrap simulation`, then "begin Session B"

---

## Docs to read first (in order)

1. **VALORIA_PAT** (project knowledge) — auth token at `/mnt/project/VALORIA_PAT`
2. **project-architecture-valoria-v2_2.md** (project knowledge) — governance, two-repo structure
3. **Valoria PI** (project instructions) — bootstrap script, hook contracts
4. **session_log_current.md** (in repo `jordanelias/ttrpg`) — set during bootstrap
5. **params/combat.md** — post-revert canonical state (PP-718 in effect)
6. **designs/scene/derived_stats_v30.md** — Health/Stamina canonical spec
7. **designs/scene/combat_v30.md** — Round structure, actions, initiative
8. **tests/sim/combat_integration/session_a_chassis.py** — built this session, Godot-shaped
9. **tests/sim/combat_integration/sim_verification_ledger.json** — 33 cited constants
10. **tests/audit/combat_integration_session_a_ners.md** — Session A NERS audit

---

## What was done

### Phase 1: Revert (commit `4d89cbb`)
PP-717 fully rolled back. Canonical state restored:
- **Pool:** `(Agi × 2) + Hist + 3`, minimum 5 (no DR)
- **Health:** `WI × (MW+1)`, MW = `floor(End/2)+1` (no cap — End 7 = 65 HP, 4 wounds)
- **Stamina:** `End × 5` (canonical ED-694)
- **Crit:** net hits ≥ 3
- **Weapons:** three-axis Reach/Weight/Type (PP-232 original)
- D4 (mace +2D) and D5 (defense triangle) stay REMOVED — correctly identified as patches

### Phase 2: Session A chassis (commit `b31c84c`)
Combat phase machine + Strike, Full Guard, Take a Breath. Six explicit phases matching `combat_v30.md §2`. Every constant cited (33 ledger entries). Smoke test passes.

### Phase 3: Session A NERS audit (commit `b29c0c5`)
All 5 throughlines pass NERS (canon-first, Godot-shaped phases, player agency via pool split, initiative as information, stamina as round timer). All 3 meta-throughlines pass (spec not balance, hook-enforced citations, editorial flags as outputs).

---

## What remains (in order)

### Session B: Feint + Establish Distance + Escape
- **Feint (PP-294):** allocate N≥3 dice to Offence; remainder defends this round. Roll N vs opponent's Defence pool at TN 7. On success: opponent loses `margin` dice from total pool **next round**, floor 1D. Non-stacking. Expires on incapacitation.
- **Establish Distance:** Move to preferred range. Contested Agility if opposed.
- **Escape:** Agility contest vs opponent. Requires not Tied Up.
- **[GAP: Distance system needs design clarification — is distance binary Close/Far, or graduated Short/Mid/Long? Session B blocked on this. Check `combat_v30.md §5 Weapon System Reach` and any zone-based movement spec before implementing.]**

### Session C: Disarm + Tie Up + Retrieve + Dodge
- Disarm: Offence roll vs opponent's STR+Agi Ob. Success drops weapon. Short range.
- Tie Up: Short range. Both parties −2D Combat Pool for one round; opponent loses reach advantage; escape requires STR contest.
- Retrieve: Pick up dropped item. Opposed Agility if in melee.
- Dodge: Ranged attacks only. Full pool as passive Defence vs one ranged attack.

### Session D: Rescue (PP-292) + Fibonacci + multi-combatant
- Rescue: redirect attack to self. Eligibility: rescued actor outnumbered. Rescuer N dice TN 7 vs attacker's roll. Success: hit redirects, rescuer gains 2 Momentum.
- Fibonacci group bonus: +0/+1/+2/+3/+4/+5 offence dice at 1/2/3/4-5/6-7/8+ attackers.
- Multi-combatant scenarios (1v2, 2v2, 1v3, 3v3) — this is where group dynamics actually matter.

### Session E: Stunt
- Canon: "+N dice to Offence from environmental/positional narrative (GM sets N, max 5)."
- Videogame surfacing decision: contextual UI affordance? Removed? Parameterized?
- This is a design call, not a sim tuning question.

### Session F: Balance review
- Full action set integrated.
- Build matrix re-test (the original "Tough dominates" concern from earlier this session should be re-examined here, NOT before).
- Only propose formula changes if measured problems appear with the complete chassis.

---

## Critical context for next session

**Do NOT:**
- Import the Burning Wheel Strike/Feint/Defend reductive triangle as a framework. Valoria has 12 canonical actions; that's the design.
- Use "arena" as a parameter — it's sim scaffolding, not canonical. Stunt is canonical (GM-set environmental +N up to 5 offence dice).
- Build a stripped-down parallel sim like `v9_fiore.py` did. Use the actual canonical action set.
- Add a `taunt` action — it appears in `tests/sim/duel_architecture_stress_01/duel_stress_test.py` but is SIM-ONLY, not in `params/combat.md`. Reference only, don't import.
- Propose MW caps, pool DR, or crit threshold changes until Session F has the full chassis to test.

**Do:**
- Use `session_a_chassis.py` as the foundation. Each new action extends the round runner.
- Cite every constant. The `sim_fabrication_check` hook is at `/home/claude/sim_verification_ledger.json`. Put the ledger there.
- Avoid bare integers in comments — rewrite section refs as "Round Structure section" instead of "§2" because the regex catches "2" as a constant.
- Run smoke tests after each session before audit.
- NERS-all-directions audit each session in the same format as `tests/audit/combat_integration_session_a_ners.md`.

---

## Open editorial questions (Jordan decisions)

1. **STR multiplier ambiguity** — Text says "Heavy Blunt = ×3" but example says "Mace=6 at STR 4" (implies ×1.5). Resolved provisionally in sim by matching example values (mace=1.5, warhammer=3.0). Confirm interpretation: does "Heavy Blunt = ×3" apply only to Long Heavy Blunt (warhammer), with Short Heavy Blunt (mace) getting ×1.5? Or is the example wrong?

2. **Distance system** — Binary "in range / out of range" per weapon reach axis, OR graduated Short/Mid/Long with cost-to-traverse? Blocks Session B.

3. **Heavy armour stamina drain** — Canonical +2/action means End 4 Heavy fighter gets ~3 Strike rounds before OOB. Is this intended punishment for Heavy, or too steep? Validate empirically after Session E.

4. **Stunt in videogame** — Surface as UI affordance, remove entirely, or parameterize per-encounter? Session E will need a decision.

5. **Taunt** — Not canonical, but appears in v9 sim. If desired as a videogame action, needs canonicalization. Currently NOT in plan.

---

## Bootstrap sequence for next chat

```python
# Standard bootstrap from PI <bootstrap_script>
# Then add audit/sim gates for this work:
h.assert_bootstrap()
h.task_gate('simulation')  # or 'audit' when auditing
h.sim_gate('custom', systems=['combat'])
```

Files to fetch with `force_full=True`:
- `session_log_current.md`
- `references/canonical_sources.yaml`
- `canon/02_canon_constraints.md`
- `skills/valoria-simulator/SKILL.md`
- `skills/valoria-mechanic-audit/SKILL.md`
- `params/combat.md`
- `designs/scene/derived_stats_v30.md`
- `designs/scene/combat_v30.md`
- `tests/sim/weapon_system_v2/testing_plan.md`
- `tests/sim/weapon_system_v2/sim_verification_ledger.json`
- `tests/sim/combat_integration/session_a_chassis.py`
- `tests/sim/combat_integration/sim_verification_ledger.json`
- `tests/audit/combat_integration_session_a_ners.md`
- `tests/coverage_matrix.md`
- `tests/sim/duel_architecture_stress_01/duel_stress_test.py` (reference)

Then: "begin Session B" — Feint + Establish Distance + Escape.

---

## Confidence/Assumption tags

- `[CONFIDENCE: high]` — Session A chassis matches canon exactly (validated against reference tables).
- `[ASSUMPTION: hook ledger path remains /home/claude/sim_verification_ledger.json — basis: current hook source. If hook updated, check.]`
- `[ASSUMPTION: PP-203 pool floor 5 remains canonical — basis: params/combat.md current state. No recent supersedence noted.]`
- `[GAP: Distance system mechanics — see Open Question #2. Session B requires resolution.]`
- `[GAP: STR mult canonical interpretation — see Open Question #1.]`
