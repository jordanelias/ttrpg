# Mechanical Tasks + Patch Propagation
## Date: 2026-03-30
## Sources: R-54–R-68 (ballot 2026-03-30), MT-01 through MT-03

---

# MT-01: Faction Unit Rosters Derived from Military Scores

Per E-31. Unit rosters derived from starting Military stats (1–7 scale).
Formula: Military score = maximum active units the faction can field simultaneously.

| Faction | Military | Starting Units | Unit Type Notes |
|---------|---------|---------------|-----------------|
| Crown | 4 | 4 | Mixed infantry + cavalry. Standard formation. |
| Church | 4 | 4 | Templars: 2 elite (Cohesion 5, Martial 4). Regular garrison: 2 (Cohesion 3, Martial 2). |
| Hafenmark | 3 | 3 | Ducal guard (1 elite, Cohesion 4, Martial 3) + 2 militia. |
| Varfell | 4 | 4 | Highland infantry. Cohesion 4. Home territory bonus: +1D in Eisengrund. |
| Guilds | 2 | 2 | Hired mercenaries. Cohesion 3, Martial 2. High Wealth allows rapid replacement. |
| Niflhel | 0 (no Military stat) | 0 | No standing units. Relies on Quiet Network; cannot hold territory by force. |
| Revolution | 0 (no Military stat) | 0 | No standing units. Community defence possible (see Community Weaving). |
| Löwenritter | 5 (peacetime) → 6 (post-coup) | 5 → 6 | Professional military elite. All units: Cohesion 5, Martial 4. Post-coup: +1 unit from Crown transfer. |

**Unit stat defaults (board game):**
- Standard: Martial 2, Cohesion 3
- Elite: Martial 3–4, Cohesion 4–5
- Cohesion loss from combat: −1 per defeat until 0 (unit destroyed).

**Mustering:** Muster order raises 1 new unit per success (up to faction Military cap). Units begin at standard stats. Upgrading to elite requires 2 consecutive successful Govern orders in the territory + Wealth ≥ 4.

**Church Templars:** Separate from Church regular garrison. Templars deploy when Theocracy Counter ≥ 40 (free unit, Himmelstift). Templars are elite stat block.

---

# MT-02: Debate Pool Formula Propagation

**Decision R-66:** Debate pool corrected to `(Presence × 2) + relevant History`.

Current state in stage9_social.md:
- Debate pool listed as `Cognition + History bonus`
- Social pools reference table lists Debate → Cognition

**Correct state:**
- Debate pool: `(Presence × 2) + relevant History bonus`
- Rationale: Debate is public performance and persuasion; Presence governs social impact. The doubling reflects that Debate draws on both the speaker's authority (one Presence instance) and their delivery/presence under pressure (second instance). History bonus unchanged.

**Files requiring update:**
1. `compilation/stage9_social.md` — §9.6 pool line + §9.7 summary table + §9.8 quick reference
2. `compilation/valoria_ruleset_checkpoint_14.md` — wherever Debate pool is stated

**Patch text:**
- Old: `**Pool**: Cognition + History bonus.`
- New: `**Pool**: (Presence × 2) + relevant History bonus.`
- Old (table): `| Debate | Cognition |`
- New (table): `| Debate | Presence × 2 |`

---

# MT-03: Territorial-Scale Spell Catalog Ob Audit

**Decision R-62 (E-20):** Mandate Reinforcement Ob corrected to 6 (W-51). Theocracy Counter +1 on visible success retained.

**Current state in stage15_spell_catalog.md:**
- All Territorial operations show `Ob 4` or `Ob 7` uniformly
- W-51 (Mandate Reinforcement) — check current Ob value

**Audit results:**
Territorial-scale spells in catalog show Ob 4 across the board. Per the scale Ob table (Structural = 7, Territorial = 4–5, Relational = 3, Personal = 2, Object = 1), Ob 4 is the standard for Territorial non-FR operations.

W-51 Mandate Reinforcement specifically: corrected to Ob 6 per R-62 (rationale: affecting political legitimacy of a faction in a territory is more contested than physical/configurational work; it operates against active institutional resistance).

**Specific Ob correction:**
- W-51 Mandate Reinforcement: Ob 4 → **Ob 6**
- All other Territorial operations: Ob 4 retained (within spec)

**Files requiring update:**
1. `compilation/stage15_spell_catalog.md` — W-51 Ob field

---

# PATCH PROPAGATION: R-54 through R-68

## R-54: Personal Pull Duration = 3 rounds, not end of scene

**Current text (stage3_thread_operations.md, Pulling section):**
`**Duration by surplus successes:** 0 = end of scene. 1 = end of session. 2+ = until next seasonal accounting.`

**Corrected text:**
`**Duration by surplus successes:** 0 = 3 rounds. 1 = end of scene. 2+ = end of session. 3+ = until next seasonal accounting.`

Note: this shifts the entire duration ladder. Pull is now re-application-required at scene scale, not a fire-and-forget. Consistent with Pull being a temporary disruption that requires sustained intentionality.

**Files:** stage3_thread_operations.md, valoria_ruleset_checkpoint_14.md

---

## R-55: Personal Dissolution Ob = End + Spirit + Armour modifier

**Current text (stage3_thread_operations.md, Dissolution section):**
`**Ob table:** Same as Lock.`
(Lock Ob = same as generic scale table, Ob 4 minimum)

**Corrected text for Personal-scale Dissolution of a living target:**
```
**Personal Dissolution Ob (targeting a living being):**
Ob = target's Endurance + target's Spirit + armour modifier
  - Light armour: +1 Ob
  - Medium armour: +2 Ob
  - Heavy armour: +3 Ob

Standard success = Partial degree (Shifting Object — body partially dissolved, ~50% HP damage). Overwhelming success required for immediate incapacitation.
```

Rationale: a living body is a heavily actualised configuration with continuous spooling from both physical substrate (End) and metaphysical coherence (Spirit). Armour adds configurational rigidity. This makes Dissolution of a person genuinely hard — requiring Thread Sensitivity investment and good roll — while preserving it as a valid combat option at high Thread Sensitivity.

**Files:** stage3_thread_operations.md, stage15_spell_catalog.md (FR-D-12 Lethal Dissolution Ob update), valoria_ruleset_checkpoint_14.md

---

## R-56: Accelerated Overweave for Healing: +2 Ob per healing op, sequence Ob 1/3/5/7

**Current text (stage3, Overweaving / W-08):**
Overweaving: `Each operation after the first in the same contact window: +1 Ob (cumulative).`
W-08: `Ob 2`

**Corrected — healing-specific rule:**
```
**Healing operations (W-08 and variants) — Accelerated Overweave:**
Each healing operation in the same contact window adds +2 Ob (not +1).
Sequence Obs: first heal Ob 1, second Ob 3, third Ob 5, fourth Ob 7.
Rationale: the practitioner is repeatedly interacting with the same living configuration. The configuration is integrating each operation and becoming less responsive to subsequent intervention — not because it is more resistant, but because it is adapting.
```

**Files:** stage3_thread_operations.md, stage15_spell_catalog.md (W-08 note), valoria_ruleset_checkpoint_14.md

---

## R-57: Pull Stacking Floor = 5D minimum; below 5D requires Lock not Pull

**Current text:** no stated floor for Pull pool.

**New rule addition (Pulling section):**
```
**Pool floor:** Minimum 5 dice before rolling a Pull. If the practitioner's Spirit + History + TPS yields fewer than 5 dice (wounds, degradation, or low stats), the practitioner cannot Pull — the intentionality required to open a configuration cannot be formed at this level of configurational depletion. Lock is still available (Locking does not require the same sustained openness; it is total actualization, not sustained potential). 
```

**Files:** stage3_thread_operations.md, valoria_ruleset_checkpoint_14.md

---

## R-58: Mass Lock Rendering Stability Drain Capped at −1/round per scene

**Current text (Locking chronic consequences):**
Duration table shows Rendering Stability drift per season, not per round. No explicit cap on concurrent Lock Rendering Stability drain.

**New cap addition:**
```
**Mass Lock RS drain cap:** Regardless of how many Locks are active concurrently in a scene, total RS drain from active Locks cannot exceed −1 per round of combat or −1 per scene in non-combat contexts. Multiple Locks do not stack RS drain rates within a scene. (Seasonal drift is unaffected — each active Lock still contributes independently to seasonal RS cost at accounting.)
```

**Files:** stage3_thread_operations.md, valoria_ruleset_checkpoint_14.md

---

## R-59–R-60: The Great Unwinding and Great Working — kept, narrative prereqs TBD

No rule text changes. Placeholder note added to spell catalog entries:
`[Narrative prerequisites pending — see editorial_ledger E-17b and E-18b]`

**Files:** stage15_spell_catalog.md (locate entries and add note)

---

## R-61: Crowd Coherence in Debates — retained as-is

No change required. Current rule stands.

---

## R-62: Mandate Reinforcement Ob = 6

Per MT-03 above. W-51 Ob: 4 → 6.

---

## R-63: Locked Institution Chronic Rendering Stability Drift — Variable by Domain Type

**Current text:** Locking a faction/institution: −1 Rendering Stability/season (uniform).

**Corrected:**
```
**Locked Institution chronic RS drift (variable):**
  - Static domain (unchanging institution, frozen process): −0 RS/season. The configuration is already close to Threadcut; locking costs little.
  - Slow-change domain (institution with seasonal/yearly evolution): −1 RS/season.
  - Dynamic domain (active institution, ongoing political contestation, living relationship): −2 RS/season.
GM determines domain type at the time the Lock is applied, based on current state of the target institution.
```

**Files:** stage3_thread_operations.md, stage15_spell_catalog.md (FR-L-30 Mandate Lock note), valoria_ruleset_checkpoint_14.md

---

## R-64: Mode 3 Entities Immune to Conventional Dissolution — Must be Overwhelmed

**Current text (stage3, Dissolution section):**
No Mode 3 exception stated.

**New addition:**
```
**Mode 3 entity exception:** Threadcut beings of the third mode (fully self-sustaining configurations, no natural trajectory) cannot be Dissolved by standard means. Their configuration is not anchored to the substrate in the normal way — there is nothing to tear. Conventional Dissolution automatically yields Partial result (Shifting Object, not true Dissolution) regardless of roll degree. Overwhelming success is required for true Dissolution effect. This is what makes Mode 3 entities the most dangerous Thread encounter in the setting.
```

**Files:** stage3_thread_operations.md, stage15_spell_catalog.md (Mode 3 Dissolution section), valoria_ruleset_checkpoint_14.md

---

## R-65: Debate Weaving Bonus = +Thread Pool Score/3 dice (Thread Sensitivity 30=+1D, Thread Sensitivity 60=+2D, Thread Sensitivity 90=+3D)

**Current text:** no Debate Weaving bonus stated.

**New rule (stage9_social.md, §9.6 Debates):**
```
**Practitioner Weaving bonus in Debates:** A practitioner with TS 30+ who is actively in Thread contact during a Debate exchange adds bonus dice equal to TPS ÷ 3 (round down) to their Debate pool for that exchange. TS 30 = +1D. TS 60 = +2D. TS 90 = +3D. The practitioner must declare the Weaving before rolling. This is visible to all observers (the practitioner is operating during contact while debating). Church may immediately call for Heresy Investigation on observation. Coherence check Ob 1 after the exchange (maintaining Debate and Thread contact simultaneously stresses the configuration).
```

**Files:** stage9_social.md, valoria_ruleset_checkpoint_14.md

---

## R-66: Debate Pool Formula

Per MT-02 above. Pool: (Presence × 2) + History.

---

## R-67: Fortification Level Adds to Structural Pulling Ob

**New rule addition (Pulling section, Foundational/Structural scale):**
```
**Fortified site Pulling:** When attempting to Pull a structural or territorial configuration that includes a fortified site (Fortification ≥ 1), add the Fortification level to the Ob. The physical reinforcement of a configuration increases its actualization — a heavily fortified territory is more firmly woven into its current state and resists loosening.
```

**Files:** stage3_thread_operations.md, stage15_spell_catalog.md (PO-05 Territorial Memory note), valoria_ruleset_checkpoint_14.md

---

## R-68: Accounting Gate Preserved — No Theocracy Counter Change Bypass

No change to existing rules (gate was already present). Confirm note added to accounting procedure:
`**Theocracy Counter accounting gate (confirmed):** All Theocracy Counter changes apply at seasonal accounting. No mechanism in the game bypasses this gate.`

**Files:** compilation/stage5_clocks.md (accounting section — add confirmation note)

---

# SUMMARY: FILES REQUIRING UPDATES

| File | Changes |
|------|---------|
| compilation/stage3_thread_operations.md | R-54, R-55, R-56, R-57, R-58, R-63, R-64, R-67 |
| compilation/stage9_social.md | R-65, R-66 (MT-02) |
| compilation/stage15_spell_catalog.md | R-55 (FR-D-12), R-56 (W-08), R-59/R-60 (note), R-62 (W-51), R-63 (FR-L-30), R-64 (Mode 3) |
| compilation/stage5_clocks.md | R-68 (confirmation note) |
| compilation/valoria_ruleset_checkpoint_14.md | All above propagated |
| compilation/stage_bg_board_game_mode.md | MT-01 (unit rosters) |
