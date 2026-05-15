# Combat Integration — Session A NERS Audit

**Scope:** Phase machine + Strike, Full Guard, Take a Breath
**Commit:** b31c84c
**Method:** Throughlines → Meta-throughlines → NERS per direction → Consistency

---

## Throughlines (this session)

### T1: Canon-first, no invention

Every mechanical constant ledgered or cited. The `sim_fabrication_check` hook caught false-positive integers (PP-numbers in comments, section numbers in docstrings) — even doc references had to use prose forms like "Wounds/Incapacitation section" rather than "L131". No mechanic appears in the sim that isn't in `params/combat.md` or `designs/scene/derived_stats_v30.md`. No "arena," no "taunt," no PP-717 derivatives.

### T2: Godot-shaped state machine

The round runs through six explicit phases (Movement, Range, Declaration, Resolution, Damage, Tracking) matching `combat_v30.md §2` exactly. Each phase is a separate code path. When ported to GDScript, each phase becomes a method on a `CombatRound` scene; the state transitions become signal emissions. The Python sim is a spec for the Godot port, not a parallel implementation.

### T3: Player agency through pool split

The only player input each round (Session A scope) is action choice (Strike/Guard/Breath) and pool split (offence/defence fraction). This minimal interface IS the decision space. Pool split is the lever the player controls; everything else follows from stats, weapon, and dice. The chassis doesn't hide decisions behind opaque AI — the player decides.

### T4: Initiative as information advantage, not action speed

Higher initiative declares SECOND, with full knowledge of opponent's split. This is what `params/combat.md L108` calls out: "Initiative determines declaration order, not action speed. Higher initiative = more information." The chassis routes the pool-split decision through initiative explicitly. Lower-init combatant commits blind; higher-init sees and reacts.

### T5: Stamina as the round timer

A duel ends one of two ways: (a) one combatant reaches 0 Health (incapacitated), or (b) both run out of stamina at zero pool. Stamina drains predictably (5 per Strike, +0/+1/+2 per armour). Take a Breath restores `(End + History) × 2`. The duration of the fight is set by these arithmetic relationships, not by external timing. End and Hist both feed into duration — End raises stamina pool, Hist raises recovery rate.

---

## Meta-Throughlines (this session)

### A: Build the spec, not the balance

This session built the chassis. No balance claims yet — too few actions to test build matrices. The smoke test only validated that the round runs end-to-end. Subsequent sessions add actions; balance review comes only after Session E (all actions integrated). Balance is a property of the full system, not of any subset.

### B: Hook-enforced citation discipline

The `sim_fabrication_check` hook is intentionally noisy. It caught real issues (mace ×1.5 vs ×3 ambiguity in canon, integer values that needed ledger entries) AND noise (PP-numbers in comments, section numbers in docstrings). Working with the hook required treating every literal integer as needing justification. This is slower than free coding but produces an auditable trail.

### C: Editorial flags as deliverables

Found one canonical ambiguity (STR multiplier text "Heavy Blunt = ×3" vs example "Mace=6"). Recorded as an editorial flag in commit notes. Not resolved — that's Jordan's call. The session's output includes both the working sim AND the open questions that emerged while building it.

---

## NERS per Throughline

| Throughline | N | E | R | S |
|-------------|---|---|---|---|
| T1: Canon-first | ✓ | ✓ | ✓ | ✓ |
| T2: Godot-shaped phases | ✓ | ✓ | ✓ | ✓ |
| T3: Player agency through pool split | ✓ | ✓ | ✓ | ✓ |
| T4: Initiative as information | ✓ | ✓ | ✓ | ✓ |
| T5: Stamina as round timer | ✓ | ✓ | ~ | ✓ |

**T5 Robust flag:** With only Strike/Guard/Breath, the round timer is rigid — about 4 rounds at End 4 before Breath becomes mandatory. Future sessions (Feint, Disarm, Tie Up) will add longer-stamina alternatives that change this dynamic. The current rigidity is correct for the scope but not yet representative of the full system.

## NERS per Meta-Throughline

| Meta-Throughline | N | E | R | S |
|------------------|---|---|---|---|
| A: Build spec, not balance | ✓ | ✓ | ✓ | ✓ |
| B: Hook-enforced citation | ✓ | ✓ | ✓ | ~ |
| C: Editorial flags as outputs | ✓ | ✓ | ✓ | ✓ |

**B Smooth flag:** The hook's false positives (PP-numbers, section references) require workaround phrasing. Real cost: doc text becomes slightly less natural. The hook should ideally distinguish "PP-239" (patch reference) from "239" (a mechanical constant). Not blocking, but friction.

---

## NERS per Direction

### Top-Down (Intent of Game)
The chassis preserves the feedback loop: stat choice → derived pool/HP/stamina → action choice → resolution → consequences (damage, wounds, stamina drain). Player decisions map directly to outcomes. **PASS.**

### Bottom-Up (Individual Mechanics)
Each formula validated against canonical reference table (Health by End, weapon TN by combination, STR mult by weapon, weapon mod by armour). Edge cases tested: Agi 0 (pool floor 5), End 7 (maximum Health 65, 4 wounds), zero stamina (OOB). **PASS.**

### Vertical (Attribute Range Scaling)
| Stat | Range | Effect | Status |
|------|-------|--------|--------|
| Agi 1→7 | Pool 5→17 | 3.4× scaling | linear above floor |
| End 1→7 | HP 14→65 | 4.6× scaling | super-linear (WI×MW interaction) |
| STR 1→7 | Damage +1→+21 (×weapon) | 7× linear | uncapped |
| Hist 0→4 | Pool 3→9 above floor | 6× scaling | flat above raw stat |

End remains the highest-leverage stat for survival, STR for offense. This was the original "Tough dominates" concern — but the full action set (especially Feint and Rescue) hasn't been added yet. Cannot judge balance until those land.

### Diagonal (Cross-System Interactions)
- Pool × Wound: -1D per wound stacks with OOB -2D, floor 5 protects against total collapse. Clean.
- Stamina × Armour: Heavy drain +2 per action means End 4 Heavy gets 20/(5+2) ≈ 2-3 rounds before OOB. Severe cost. Clean (per canon).
- Initiative × Pool Split: Higher init sees split, can counter — but Session A doesn't yet model counter-strategies (Adaptive AI is Session B+ work). The hook is present, the strategy layer isn't.

### Lateral (Peer System Parity)
N/A this session — single system.

### Horizontal (Play Context Variation)
- Unarmoured combat: tested via smoke test (40 HP vs 40 HP duel resolved in 8 rounds with crits).
- Heavy armour: not tested. The stamina drain interaction needs validation.
- Group combat: not yet in scope.
- Wounded state: only one combatant accrued wounds in the smoke test; multi-wound progression untested.

---

## System Consistency

### Internal
- ✓ Combat Pool formula matches params L14 exactly
- ✓ Health/MW/WI matches derived_stats §4.1 reference table at all End values
- ✓ Stamina matches `End × 5` canon (no Architecture C drift)
- ✓ Weapon TN matches three-axis system from params §Weapon System
- ✓ Action priority order matches PP-247
- ✓ Initiative tiebreaker matches PP-232/PP-239 chain (Attunement → Agility → random)

### External
- ⚠ STR multiplier text vs example inconsistency (mace) — flagged as editorial
- ⚠ Heavy armour drain (+2 per action) means End 4 Heavy fighter has effective 7 stamina per Strike (20 ÷ 7 ≈ 3 rounds). This may be intended or may be too punishing. Validate after Session E.

---

## Open Items for Session B

1. **Feint (PP-294):** allocate N≥3 dice to Offence, remainder defends this round; vs roll TN 7; on success, opponent loses `margin` dice from total pool next round (floor 1D). Non-stacking, expires on incapacitation.
2. **Establish Distance:** Move to preferred range. Contested Agility if opposed. (Distance/range system not yet active — needs design clarification: is distance binary "Close/Far" or graduated Short/Mid/Long?)
3. **Escape:** Agility contest. Requires not being Tied Up.

---

## Verdict

Session A: clean. Chassis is canon-faithful, fully cited, smoke-tested. Ready for Session B (Feint + Distance + Escape) when you say go.
