# Term Usage Sweep — Batch 6: Combat Terms, Personal-Combat internals, and the Combat Pool 5-way check

# Batch 6 Audit: Combat Terms, Personal-Combat Internals, and the Combat Pool 5-Way Check

Method note: home definitions were read directly from cited files; every usage site below was opened and inspected (not inferred from filenames). Line numbers refer to the working tree as of 2026-07-08.

---

## 1. Command (mass battle)

**Home definition (as it *should* be):** `designs/provincial/mass_battle_v30.md:266` (this is the CURRENT.md-designated mass-battle head) —
> `**Command = clamp(round((2 × Charisma + Cognition) ÷ 3), 1, 7)** *(ED-899: Charisma primary, Cognition secondary — engine CMD_CHA_WEIGHT=2 / CMD_COG_WEIGHT=1, leading canon; supersedes the equal-weight ⌈(Cha+Cog) ÷ 2⌉ form)*`

This is also the formula the live reference engine implements: `tests/sim/mass_battle/core/exchange.py:25-34` `derive_command(charisma, cognition)`: `round((CMD_CHA_WEIGHT*charisma + CMD_COG_WEIGHT*cognition)/w)`, clamped `[1,7]`, with `CMD_CHA_WEIGHT=2`/`CMD_COG_WEIGHT=1` set in `tests/sim/mass_battle/config.py:158-159`.

**Exhaustive usage sweep.** "Command"/"⌈(Cha+Cog)" formula occurs in dozens of files. Distinct textual formulas found:

- **Weighted (ED-899, current):** `designs/provincial/mass_battle_v30.md:266,278`; `params/mass_combat.md:5(banner),62(banner),139,361,369`; `tests/sim/mass_battle/core/exchange.py:25-34`; `tests/sim/mass_battle/config.py:158-159`; `tests/sim/mass_battle/hierarchy/units.py:1476,1483-1484`; `tests/sim/mass_battle/engine.py:76`; `designs/proposals/pc_formation_system.md:56`; `designs/audit/2026-06-09-session-consolidation-master.md:151`; `designs/audit/2026-07-08-pessimist-action-audit/01_workings/dossier_MB.md:25`.
- **Old equal-weight (⌈(Cha/Presence+Cog)÷2⌉, superseded):** `references/glossary.md:121` (Part Five, **no ED-899 note at all**); `references/mechanical_terms_index.md:958` (**cites "mass_battle §A.5" as its source**, which no longer contains this formula); `references/values_master.yaml:1912-1914` and `:1656-1661` (stale extraction snapshots of `params/mass_combat.md`, predating the ED-899 banner being added); `references/valoria_interdoc_audit.md:369` (audit-output snapshot); `designs/audit/2026-05-28-resolution-diagnostic/resolution_diagnostic_mass_battle.md:52`; `designs/audit/2026-05-28-combat-reframe/derived_stats_audit.md:5,32,35,70,77,89` and `combat_mechanical_armature.md:53`; `designs/audit/2026-05-15-mb-comparative-audit/audit.md:250,305`; `designs/arcs/arcs_20_23.md:271`; `designs/audit/player_world_bridge_2026-04-16.md:221`; `designs/audit/valoria_complete_system_audit.md:592`; numerous narrative sim logs (`tests/sim/sim_batch_5_2026-04-16.md:523`, `sim_fieldwork_transitions.md:272`, `sim_stress_batch_2_2026-04-16.md:180,230,593`, `simulation_report_arcs_31_33.md:314`, `sim_x_07_massbattle_npcs_thread.md:181`, `emergent_arc_skeleton_test_2026-04-17_batch5.md:24`, `tests/stress/emergent_arc_2026-04-17_batch5.md:24`) — consistent with each other in restating the old formula, e.g. "Player Command: ⌈(Charisma 4 + Cognition 4) ÷ 2⌉ = 4".
- **Self-diagnosing, already-stale complaint:** `designs/proposals/pc_formation_system.md:167` — "**Reconcile A.5 Command** — the canon doc still reads `⌈(Cha+Cog)/2⌉` (equal weight); the engine now uses Charisma-primary `round((2·Cha+Cog)/3)` (ED-899). Update the doc." This complaint is **itself now stale** — `mass_battle_v30.md` §A.5 already carries the ED-899 formula (confirmed by direct read) — but the action item was never marked resolved/removed.

**Divergence check.** Two textually distinct formulas for the same stat, unreconciled in `references/glossary.md` and `references/mechanical_terms_index.md` (the two indices CLAUDE.md names as most authoritative for machine lookups), with **zero acknowledgment** of ED-899 in either — verified by `grep -n "ED-899"` returning no hits in `glossary.md` or `mechanical_terms_index.md`. Contrast:
- Glossary (line 121): `⌈(Presence + Cognition) ÷ 2⌉. ... (PP-232)`
- Current canonical head (line 266): `clamp(round((2 × Charisma + Cognition) ÷ 3), 1, 7)` — explicitly "supersedes the equal-weight ⌈(Cha+Cog) ÷ 2⌉ form".

`params/mass_combat.md` and `mass_battle_v30.md` (the two files CLAUDE.md/`canonical_sources.yaml` pair as the mass-battle canon set) are internally reconciled with each other and with the live engine.

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `designs/provincial/mass_battle_v30.md:266` | CANONICAL DEFINITION | CURRENT.md-designated head, ED-899-cited | — (this is canon) |
| `tests/sim/mass_battle/core/exchange.py:25-34` | CANONICAL DEFINITION (code) | Live-engine implementation, cited as "leading canon" by both mass-battle docs | Yes (by construction) |
| `tests/sim/mass_battle/config.py:158-159` | CANONICAL DEFINITION (code, tunables) | Defines `CMD_CHA_WEIGHT`/`CMD_COG_WEIGHT` consumed by `derive_command` | Yes |
| `params/mass_combat.md:62,139,361,369` | PULLED / REFERENCED | Explicitly cites "engine `CMD_CHA_WEIGHT=2`/`CMD_COG_WEIGHT=1`, leading canon" — a bare citation restating the code's own formula, with an explicit precedence statement ("config.py is leading canon; this doc follows") | Yes |
| `designs/proposals/pc_formation_system.md:56` | PULLED / REFERENCED | Cites commit `2cf3feb6` / ED-899 by name | Yes |
| `references/glossary.md:121` | HARDCODED DUPLICATE | Independent literal restatement, no ED-899 citation, no import mechanism | **No — stale, pre-ED-899 formula** |
| `references/mechanical_terms_index.md:958` | HARDCODED DUPLICATE | Independent literal restatement citing "mass_battle §A.5" — a citation that is now factually wrong since §A.5 changed | **No — stale, and its own citation is broken** |
| `references/values_master.yaml:1656-1661,1912-1914` | HARDCODED DUPLICATE | Frozen auto-extraction snapshot (generator dead per file's own banner), independently restates value | **No — stale** |
| `designs/audit/2026-05-28-combat-reframe/derived_stats_audit.md` (multiple lines) | HARDCODED DUPLICATE | Independent restatement in audit prose | No (dated audit artifact, pre-ED-899) |
| `tests/sim/*.md` narrative sim logs (`sim_batch_5_2026-04-16.md:523` etc.) | HARDCODED DUPLICATE | Each independently computes/restates the formula in-narrative | No (historical sim artifacts, pre-ED-899) |
| `designs/proposals/pc_formation_system.md:167` | UNCLEAR / STALE META-CITATION | Flags the divergence as an open to-do, but the to-do is itself now factually wrong (the doc it names as un-updated has already been updated) | N/A — the finding itself is stale |

**Incidental usage excluded:** none — every occurrence found was the game-mechanical Command stat, not the English word.

---

## 2. Damage Resistance / DR

**Home definition:** DR is **mass-battle-only** in the current corpus — personal combat's armour model uses fractional `RESIST` transmission (not DR) in `designs/scene/combat_engine_v1/core.py:86-89`, confirmed by `grep "\bDR\b" params/core.md` returning zero hits. Mass-battle DR canonical text: `params/mass_combat.md:69` `Health per Size (H) = min(Discipline, Command) + DR`, melee table `params/mass_combat.md:173-182`, ranged/projectile table `:191-200`; code home `tests/sim/mass_battle/hierarchy/units.py:1488` `self.h_per_size = max(1, min(self.discipline, self.command) + self.dr)`.

**Exhaustive usage sweep:** `references/glossary.md:122,126`; `params/mass_combat.md` (multiple sections); `designs/provincial/mass_battle_v30.md:234,238-256,443,447`; `tests/sim/mass_battle/equipment/armour.py:9-51`; `tests/sim/mass_battle/hierarchy/units.py:400,1488`; `references/mechanical_terms_index.md:522,959`; `references/values_master.yaml:1621,1639` (worked-example DR values); `designs/scene/combat_v30.md:266-277,394,401` (old personal-combat DR, superseded).

**Divergence check — three findings:**

1. **Melee DR table row-corruption in `params/mass_combat.md:176-181`.** The header row declares 4 columns (`LC | HC | LB | HB`), but every data row carries **5** values:
   > `| None | 0 | 0 | 0 | 0 | 0 |`
   > `| Light | 2 | 1 | 1 | 0 | 2 |`
   > `| Medium | 4 | 3 | 2 | 1 | 4 |`
   > `| Heavy | 6 | 5 | 3 | 1 | 6 |`

   The phantom trailing column (`0,2,4,6`) exactly duplicates the LC column's own values — a copy/paste artifact. Compare against `designs/provincial/mass_battle_v30.md:238-244`, whose 4-column melee DR table is clean and matches the *first* four values exactly (`None:0/0/0/0`, `Light:2/1/1/0`, `Medium:4/3/2/1`, `Heavy:6/5/3/1`). The two docs agree on substance; `params/mass_combat.md`'s table is malformed.

2. **Two irreconcilable Ranged/Projectile DR tables, both presented as current, in the two paired canonical files.** `designs/provincial/mass_battle_v30.md:246-256` ("Ranged DR (Volley Phase) — MASS COMBAT SCALE [PP-188]... Scaled (÷2 rounded up) from personal combat DR"):
   > None 0/0, Light 1/1, Medium 2/1, Heavy 3/2 (vs Piercing/vs Blunt)

   `params/mass_combat.md:191-197` ("### Projectile weapons (mass combat only — PP-104)"):
   > None 0/0/0/0, Light 1/1/2/0, Medium 4/3/4/1, Heavy **7**/5/6/2 (LP/HP/LBl/HBl)

   These are not the same table rescoped — Heavy caps at 3 in one and 7 in the other, and the category schemes differ (2-axis Piercing/Blunt vs 4-axis LP/HP/LBl/HBl). Neither doc cross-references or supersedes the other; both are cited by CLAUDE.md/`canonical_sources.yaml` as the paired mass-battle canon set.

3. **Mass_battle_v30.md contradicts itself on the per-hit damage formula (bleeds into DR's role).** §A.3 (`:88`): `effective_damage = floor(successes × (1 + Power) × TroopCount / max_TroopCount)` — DR is **not** subtracted per-hit here; it's baked into Health-per-Size instead (matching `params/mass_combat.md:69-74` and the live engine, `tests/sim/mass_battle/core/attrition.py:15` "canonical exchange scale (PP-233 successes×(1+Power))" and `orchestration.py:1712` "canonical: params/mass_combat.md PP-233 — Damage = successes × (1+Power)"). But §A.7 Phase 5 step 5 (`:447`), in the *same file*, gives a different formula: `Damage = max(0, net hits + weapon modifier − DR)` — DR subtracted directly, with a "weapon modifier" term that doesn't exist in the Power/TroopCount model at all. This is verbatim the old personal-combat formula from the now-superseded `designs/scene/combat_v30.md:401` (`Damage = max(0, net hits + weapon modifier − DR)`), inherited via mass_battle_v30.md's own §A.4 note ("Armour Tier / DR table — inherits personal combat tables") — but the personal-combat system it claims to inherit from no longer exists in that form (`combat_engine_v1` replaced it with additive Str+heft×coupling, no DR, no flat weapon modifier). §A.7 was never updated when §A.3's Power/TroopCount model landed.

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canonical value today? |
|---|---|---|---|
| `tests/sim/mass_battle/hierarchy/units.py:1488` | CANONICAL DEFINITION (code) | `h_per_size = min(discipline,command)+dr` | Yes |
| `params/mass_combat.md:69` (Health-per-Size row) | PULLED / REFERENCED | Matches code exactly, paired-canon params doc | Yes |
| `designs/provincial/mass_battle_v30.md:234-236` | PULLED / REFERENCED (implicit) | References DR/Discipline/Command feeding H, does not restate the literal formula itself | Yes (by omission, not contradiction) |
| `references/glossary.md:122,126` | HARDCODED DUPLICATE | Independent restatement `min(Discipline,Command)+DR` | Yes — this one agrees |
| `params/mass_combat.md:176-181` (melee DR table) | HARDCODED DUPLICATE | Independent literal table with corrupted 5th column | **Malformed** — not wrong in substance but structurally corrupted |
| `params/mass_combat.md:191-197` (Projectile DR table, PP-104) | HARDCODED DUPLICATE | Independent literal table, cites PP-104 | **Diverges** from `mass_battle_v30.md`'s PP-188 ranged DR table |
| `designs/provincial/mass_battle_v30.md:246-256` (Ranged DR, PP-188) | HARDCODED DUPLICATE (design-doc prose) | Independent table, explicitly "scaled ÷2 from personal DR" | **Diverges** from `params/mass_combat.md`'s PP-104 table |
| `designs/provincial/mass_battle_v30.md:447` (§A.7 damage step) | HARDCODED DUPLICATE, internally contradicts its own §A.3 (`:88`) | Independent restatement of a formula not used by the live engine | **No — stale, superseded model coexisting in the same file** |
| `tests/sim/mass_battle/equipment/armour.py:9-51` | PULLED / REFERENCED | Explicit comment: "NOT YET WIRED into resolution (the engine still computes DR the old way)" — an honestly-flagged non-canonical seed | Partially (values match `params/mass_combat.md`'s PP-104 table specifically, by its own citation) |
| `references/mechanical_terms_index.md:522,959` | UNCLEAR / NO CANONICAL SOURCE | Cites `combat_v30 §6` (superseded personal-combat doc) as DR's primary home, "cross-listed" mass-combat as secondary — inverts current reality where DR survives only in mass battle | N/A |

**Incidental usage excluded:** none.

---

## 3. Size

**Home definition:** `designs/provincial/mass_battle_v30.md:140`: `Size = floor(TroopCount / block_size)`. At Size 0: destroyed. Code: `tests/sim/mass_battle/hierarchy/units.py:1541-1549` `recalc_size()`: `effective_size = hp/BLOCK_SIZE`, `size = floor(effective_size)`; `BLOCK_SIZE=100` hardcoded in `config.py:40` citing "Company scale" from the same doc's §A.3 table.

**Usage sweep:** `references/glossary.md:123` ("Size | — | Unit headcount stat (replaces Strength). At 0: unit destroyed. Pool contribution capped at Command. (PP-232)"); `params/mass_combat.md:109,140` (`| Size | Headcount/health pool. At 0: destroyed. |`); `mass_battle_v30.md:24,32,140,411`; `tests/sim/mass_battle/hierarchy/units.py:1486-1487,1494,1541-1549`. All consistent — no divergence found. The glossary's brief phrasing ("headcount stat") is a simplification of the `floor(TroopCount/block_size)` formula, not a contradiction of it; it doesn't restate a competing formula.

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees? |
|---|---|---|---|
| `mass_battle_v30.md:140` | CANONICAL DEFINITION | CURRENT.md head | — |
| `tests/sim/mass_battle/hierarchy/units.py:1541-1549` | CANONICAL DEFINITION (code) | Live implementation | Yes |
| `params/mass_combat.md:109,140` | PULLED / REFERENCED | Paired params doc, simplified restatement, no independent formula | Yes |
| `references/glossary.md:123` | PULLED / REFERENCED (conceptual) | Restates concept ("At 0: destroyed", "Pool contribution capped at Command") without an independent competing formula | Yes |

**Incidental usage excluded:** many hits for "size" as an ordinary English word (battlefield size, grid size, pool size) throughout `config.py`/`orchestration.py` (`BATTLEFIELD_SIZE`, `UNIT_GRID_SIZE`, etc.) were excluded as non-game-mechanical (they're geometry constants, not the Size stat).

---

## 4. Power (unit)

**Home definition:** `designs/provincial/mass_battle_v30.md:142-151`: dice-pool ceiling stat, 1-7, tiered (1 Levy … 6-7 Exceptional/Peerless). Damage relation per §A.3 (`:88`): `1+Power` multiplier on successes. Matches `params/mass_combat.md:72-73`: `Damage per success | 1 + Power`, `Damage dealt | successes × (1 + Power)`. Code: cited in `tests/sim/mass_battle/core/attrition.py:15` and `orchestration.py:1712` as "the canonical exchange scale."

**Usage sweep:** `references/glossary.md:124` ("Power | — | Unit offensive quality (replaces Combat Power, PP-232/PP-233). Damage per success = 1 + Power. Derived from unit type."); `params/mass_combat.md:72-73,84-104,110,117-125`; `mass_battle_v30.md:88,124,142-151`; `tests/sim/mass_battle/core/attrition.py:15`; `orchestration.py:1654,1712`; `references/mechanical_terms_index.md:956`; `references/values_master.yaml:1620-1655` (worked example, matches).

**Divergence check:** Same internal split already documented under DR (finding 3): `mass_battle_v30.md` §A.7 line 447 damages via `net hits + weapon modifier − DR` (no "Power" term at all), contradicting the same file's own §A.3 line 88 and the live engine's `1+Power` model. This is the same divergence viewed from Power's side — worth restating here because it means **Power's role in damage output is literally absent from one of the two procedural descriptions inside the current canonical mass-battle head.**

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees? |
|---|---|---|---|
| `params/mass_combat.md:72-73` | CANONICAL/PULLED (paired doc, matches live engine exactly) | Cited directly by engine comments | Yes |
| `mass_battle_v30.md:88` (§A.3) | PULLED / REFERENCED | Matches params doc and engine | Yes |
| `mass_battle_v30.md:447` (§A.7) | HARDCODED DUPLICATE of the OLD (superseded) personal-combat model | Independent restatement, no Power term present | **No — internally contradicts the same document's §A.3** |
| `references/glossary.md:124` | PULLED / REFERENCED | Matches current model | Yes |
| `tests/sim/mass_battle/core/attrition.py:15`, `orchestration.py:1712` | CANONICAL DEFINITION (code, citing its own source) | Comment cites "PP-233 successes×(1+Power)" | Yes |

**Incidental usage excluded:** "Power" as a faction stat (Mandate/Influence/Wealth/**Military**/Intel/Stability — glossary Part Four) is a *different* stat (Military, not Power) and was not conflated here; likewise ordinary-English "power" ("Command dominates", "political power") was excluded throughout the corpus scan.

---

## 5. Discipline (mass battle)

**Home definition:** `designs/provincial/mass_battle_v30.md:169-183`: 1-7, "Starting value = min(general's Command, Military ceiling)"; stepped Effective-Power-penalty table: `5-7: None`, `3-4: −1D`, `1-2: −2D`, `0: Formation broken`. Matches `params/mass_combat.md:111,146-153` exactly (same stepped table, same thresholds).

**Usage sweep:** `references/glossary.md:125` ("Discipline | — | Unit organisational integrity (replaces Cohesion, PP-232). Contribution to Health per Size capped at Command."); `mass_battle_v30.md:169-230` (extensive, including the 2026-06-17 per-sub-unit ED-1019/1020/1022/1026 additions); `params/mass_combat.md:111,146-155`; `tests/sim/mass_battle/hierarchy/units.py:1551-1555,1582`; `references/mechanical_terms_index.md:957`.

**Divergence check (new finding, not previously documented anywhere I found with an ED banner):** the live engine's Discipline→Power-penalty relationship is a **continuous linear function**, not the stepped table both canonical prose docs present:

`tests/sim/mass_battle/hierarchy/units.py:1551-1555`:
```python
def discipline_penalty(self):
    # SMOOTH (Jordan 2026-06-15 'fix discipline'): continuous linear penalty over the SAME range as the
    # old tiers' endpoints (discipline>=5 -> 0, discipline 1 -> -2) -- no step/cliff.
    if self.discipline <= 0: return -99
    return -max(0.0, min(2.0, (5.0 - self.discipline) * 0.5))
```

This function only matches the stepped table at the tier *endpoints* (Discipline 5→0, 3→−1, 1→−2). It **diverges in between**: at Discipline 2, the code gives `-1.5` where the table (`mass_battle_v30.md:181`, `params/mass_combat.md:152`) says flat `−2D` for the whole 1-2 band; at Discipline 4, the code gives `-0.5` where the table says flat `−1D` for the whole 3-4 band. Unlike the Pool formula (ED-899/ED-1013) and Morale (ED-1024, "Morale is continuous in play"), which both got an explicit banner in the design doc announcing the smoothing change, **Discipline's smoothing (2026-06-15) has no equivalent banner anywhere in `mass_battle_v30.md` or `params/mass_combat.md`** — both still present the discrete 4-row table as if it were exactly what the engine does.

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees? |
|---|---|---|---|
| `tests/sim/mass_battle/hierarchy/units.py:1551-1555` | CANONICAL DEFINITION (code) | Live smooth-linear implementation | — |
| `mass_battle_v30.md:169-183` | HARDCODED DUPLICATE (stepped table) | Independent restatement, no smoothing banner | **Partial — agrees only at tier endpoints, diverges mid-band, and the doc doesn't disclose the code has moved on** |
| `params/mass_combat.md:146-153` | HARDCODED DUPLICATE (stepped table) | Same as above | Same partial divergence |
| `references/glossary.md:125` | PULLED / REFERENCED (conceptual, no numeric table) | Just states "Contribution to Health per Size capped at Command" — doesn't restate the penalty table at all | N/A (doesn't make the claim, so can't diverge on it) |

**Incidental usage excluded:** none.

---

## 6. Health per Size

**Home definition:** formula lives in `params/mass_combat.md:69` (`H = min(Discipline, Command) + DR`) and code `tests/sim/mass_battle/hierarchy/units.py:1488` (`max(1, min(self.discipline, self.command) + self.dr)`) — note the code has a `max(1, ...)` floor the prose formula doesn't mention. `designs/provincial/mass_battle_v30.md:236` references "H" as a concept ("H is computed once at battle start from the unit's opening Discipline and Command values") but **never spells out the literal formula itself** in that file — it assumes the reader already has `params/mass_combat.md` open. This means the CURRENT.md-designated head doc is not self-contained for this term.

**Usage sweep:** `references/glossary.md:126`; `params/mass_combat.md:6(banner),69,81,86,92`; `mass_battle_v30.md:236`; `units.py:1488`; `references/values_master.yaml` (worked example only, no independent formula restated for H itself, only Total Health, see below).

**Divergence check:** substance agrees everywhere it's stated; the only wrinkle is the undisclosed `max(1,...)` floor in code absent from every prose site, and the fact that the officially-designated canonical head (`mass_battle_v30.md`) doesn't itself carry the formula text.

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees? |
|---|---|---|---|
| `units.py:1488` | CANONICAL DEFINITION (code) | Includes an unstated `max(1,...)` floor | — |
| `params/mass_combat.md:69` | PULLED / REFERENCED | Matches code minus the floor | Yes (substance) |
| `references/glossary.md:126` | PULLED / REFERENCED | Matches exactly: `min(Discipline, Command) + DR` | Yes |
| `mass_battle_v30.md:236` | UNCLEAR / NO INDEPENDENT CLAIM | Doesn't state the formula at all, just references the concept — the CURRENT.md-designated head is not self-contained here | N/A |

**Incidental usage excluded:** none.

---

## 7. Total Health

**Home definition:** `params/mass_combat.md:70,74`: `Total Health = Size × H`; `Size after round = ⌊remaining Health ÷ H⌋`. Code: `units.py:1489-1492` implements a **different, v19 TroopCount-based model** — `hp_max = float(total)` (sum of cell troop counts) rather than `Size × H` directly; Size is then *derived back* from HP via `recalc_size()` (`hp / BLOCK_SIZE`, floored). `mass_battle_v30.md:236` states "H ... does not recalculate H or Total Health" (frozen for the battle) but again does not give the literal formula.

**Usage sweep:** `references/glossary.md:127` ("Total Health | — | Size × H. Full Size always used regardless of Command cap. (PP-233)"); `params/mass_combat.md:70,74,79-102` (worked example); `mass_battle_v30.md:236`; `units.py:1489-1494`; `references/values_master.yaml:1626-1649` (two "Total Health" worked-example entries, matching `params/mass_combat.md`'s own worked example numbers exactly, since they're extracted from it).

**Divergence check:** The v19 TroopCount rearchitecture (`mass_battle_v30.md:88`, `units.py:1489-1494`) changed *how* Total Health is derived (bottom-up from troop counts, casualties = soldier counts) versus the PP-233 top-down `Size × H` formula that `params/mass_combat.md` and the glossary still present as the mechanism. Neither prose doc's Total-Health row acknowledges this v19 inversion (contrast with how explicitly the pool/Morale changes are bannered) — this is the same "H is computed once... does not recalculate" line (`:236`) doing double duty as the only disclosure, and it doesn't actually explain the TroopCount inversion.

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees? |
|---|---|---|---|
| `units.py:1489-1494` | CANONICAL DEFINITION (code) | v19 TroopCount-first model; Total Health is emergent from cell troop sums, not `Size×H` directly | — |
| `params/mass_combat.md:70,74` | HARDCODED DUPLICATE (older PP-233 top-down formula) | Independent restatement, no v19/ED-694 cross-reference | Numerically equivalent at muster time, but describes the wrong causal direction post-casualties |
| `references/glossary.md:127` | HARDCODED DUPLICATE | Same PP-233 framing, no v19 note | Same caveat |
| `references/values_master.yaml:1626-1649` | HARDCODED DUPLICATE (extraction of the worked example) | Frozen snapshot of `params/mass_combat.md`'s own numbers | Yes (internally consistent with its stale source) |

**Incidental usage excluded:** none.

---

## 8. Combat Pool (the 5-way check, plus everything else found)

**Home definition:** `designs/scene/combat_engine_v1/core.py:27-32`:
```python
POOL_FLOOR = 5     # [canonical: params/core.md §Derived Scores (Combat Pool min 5)]
BASE_POOL = 6      # [class-C: armature — History-driven pool base; pool = max(5, History+6), ED-901]
def resolution_pool(history):
    """Agility-INDEPENDENT resolution pool (ED-901; re-ratified ED-900/904): max(5, History + 6)."""
    return max(POOL_FLOOR, int(round(history)) + BASE_POOL)
```
Consumed live at `wrapper.py:101,184`: `pool=max(1, core.resolution_pool(longer.history))` / `core.resolution_pool(aggressor.history)`.

**Checking every specified location:**

**(a) `params/core.md`** — THREE distinct mentions, not fully mutually consistent:
- Line 4 (changelog comment, historical): `<!-- PP-247 (Combat Pool formula corrected... Agi + hist_pts + 3) -->` — an old, now-superseded changelog note, harmless as history.
- Line 161 (current, correct): `Combat Pool | max(5, Relevant History + 6) | min 5 | **Agility-INDEPENDENT** resolution pool — ratified 2026-05-29 R1 (ED-901; re-ratified ED-900/904...). Supersedes the struck (Agility × 2) + History + 3 form (PP-615/PP-247 era). Single source: designs/scene/combat_engine_v1/`.
- Line 252 (**internally inconsistent with line 161, in the same file**): `Fieldwork Pool: (Primary Attribute × 2) + History bonus (matching Combat Pool and Contest Pool construction per PP-615/PP-234).` This describes Fieldwork Pool as matching an Agility(Primary-Attribute)×2-based Combat Pool construction — but line 161, 91 lines earlier in the *same file*, explicitly says Combat Pool is now Agility-**independent** and no longer built that way. Line 252 was never updated when line 161's ED-901 rewrite landed.

**(b) `designs/scene/combat_engine_v1/core.py:30-32`** — CANONICAL DEFINITION, confirmed above.

**(c) `references/module_contracts.yaml:811,851`** — PULLED/REFERENCED:
- Line 811: `resolver: d_sigma ... pool=max(5,History+6), base Ob 3 FIXED ... NOT v30 dice_pool (Agi×2 / TN-7).`
- Line 851 (gap_notes): explicitly documents the exact divergence this batch was asked to find: *"MODEL CORRECTION: resolver is d_sigma (sigma-leverage), NOT the v30 dice_pool model (pool=Agi×2, TN-7, damage=net_hits+STR) that the Godot skeleton placeholder, sim/personal/combat.py, mechanics_index.yaml, and data_serialization_spec.md WeaponData all still carried."* This is a bare citation to the code plus an honest, self-flagged list of stale sites — not an independent numeric claim.

**(d) `references/values_master.yaml`** — TWO locations specified, both found, **both stale**, plus 3 more incidental mentions:
- Location 1, line 212-217, filed under the key `"params/combat.md"` (a **file that does not exist** — moved to `deprecated/params/combat.md`): `formula: "(Agility × 2) + Relevant History + 3 (minimum 5)"` — the pre-ED-901 struck formula.
- Location 2, line 1150-1163, filed under the *real* key `"params/core.md"` (i.e., this one IS a snapshot of the real file, just a stale-dated one): `formula: "(Agility × 2) + weapon History (points + 3)"`, `range: "min 5"` — a **third, differently-worded** old formula (neither matches location 1's wording nor the current `params/core.md:161` text), confirming this is a frozen pre-ED-901 extraction never regenerated (the generator is dead per the file's own quarantine banner at lines 7-24).
- Also line 327-329 (`"Per Wound" -1D Combat Pool only (no Ob penalty)`) — the OLD wound-penalty model, pre-dating ED-PC-0005's reversal to fractional-Ob (see term 9 below); filed under the same fictitious `"params/combat.md"` key.
- Also line 2680-2682 (`params/threadwork.md` extraction): `"**Thread pool split (Off/Def) applies** identically to personal combat pool split"` — an orphaned citation to an "Off/Def pool split" concept for Combat Pool that does not appear anywhere in `combat_engine_v1` (no `sel_off`/`sel_def` split exists in `combatant.py`/`wrapper.py`); this looks like a residual reference to an even-older personal-combat model.

**(e) `sim/personal/combat.py`** — explicitly `[DEPRECATED 2026-06-23]` in its own docstring (`:4-11`), but its old formula is still live in the file, `:45-48,120-132`:
```python
COMBAT_POOL_MIN = 5
COMBAT_POOL_HISTORY_CONSTANT = 3
def _combat_pool(actor) -> int:
    pool = (agi * 2) + history + COMBAT_POOL_HISTORY_CONSTANT   # Agi×2 + History + 3
    pool = max(COMBAT_POOL_MIN, pool)
    pool += wounds * WOUND_PENALTY_PER   # -1D per wound
    ...
```
**Critical finding beyond the banner:** this "deprecated, retained for reference/history only... do NOT wire new game code through this file" module is **still live-wired**: `sim/cross_scale/scene_dispatch.py:96` — `import sim.personal.combat as combat; rr = combat.resolve_combat_round(parts, ...)` — inside `_resolve_slot()`'s `if st == "combat":` branch, which is the actual scale-transition dispatcher (`sim/cross_scale/scene_dispatch.py`, docstring dated 2026-06-06, status "[PROVISIONAL — seam-mechanism wiring]"). This file was never updated after `sim/personal/combat.py` was deprecated on 2026-06-23 to redirect to `combat_engine_v1`. Any code path that exercises `run_scene_phase`/`dispatch_scenes` for a `"combat"` scene type executes the deprecated Agility×2+History+3 pool formula, not the canonical `max(5,History+6)` one.

**Other sites this list missed, found in the sweep:**
- `designs/scene/combat_engine_v1/combatant.py:117` — `self.pool=max(5, history+6)` — this restates the *current* formula correctly, but it is **dead code**: `designs/audit/2026-06-29-combat-corpus-recovery/combat_workplan_v1_2026-06-18.md:63` explicitly notes *"drop dead `max(5)` POOL_FLOOR ... `combatant.pool` is vestigial (live pool = `core.resolution_pool`)"*, and a repo-wide grep for `.pool` attribute reads in `combat_engine_v1` (excluding the workbench UI's unrelated `.pool` template variable) confirms **zero call sites read `combatant.pool`** — the wrapper always calls `core.resolution_pool(...)` fresh at `wrapper.py:101,184`. A currently-correct value that no code path ever consumes.
- `canon/mechanics_index.yaml:210-219` — correctly repoints to `combat_engine_v1`, explicitly labels `sim/personal/combat.py` "the DEPRECATED v30 wiring," and states the correct formula. This directly **contradicts** the live wiring found in `sim/cross_scale/scene_dispatch.py:96` — the index says the deprecated module is inert; the code shows it is not.
- `references/engine_params/combat_engine_v1.json` — GENERATED export from `config.py` (`tools/export_engine_params.py`) — correctly does **not** include `POOL_FLOOR`/`BASE_POOL` (those constants live in `core.py`, not `config.py`, so they're out of this export's declared scope — not a gap, a correct scoping boundary).
- `tests/sim/v32-combat-balance/r1_sigma_resolution.py:71-72` — the FROZEN historical validation harness's own copy of `resolution_pool`/`POOL_FLOOR`. Per `combatant.py:9-14`'s own banner, this frozen harness is intentionally retained with its own historical copies "for its own archived runs" post the ED-1085 de-leak — a deliberately-retained duplicate, not a live-canon risk, but still technically a second literal copy of the formula in the tree.

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon today? |
|---|---|---|---|
| `combat_engine_v1/core.py:27-32` | CANONICAL DEFINITION | — | — |
| `combat_engine_v1/wrapper.py:101,184` | PULLED / REFERENCED | Calls `core.resolution_pool(...)` directly | Yes |
| `params/core.md:161` | PULLED / REFERENCED (prose mirror, correctly updated) | States formula + explicit ED-901 supersession note | Yes |
| `params/core.md:4` | HARDCODED DUPLICATE (historical changelog comment) | Old PP-247 note, harmless as dated history | No (but doesn't claim to be current) |
| `params/core.md:252` | HARDCODED DUPLICATE (uncorrected residual) | Independently describes Combat Pool's construction, contradicting line 161 in the same file | **No — internally contradicts its own file** |
| `references/module_contracts.yaml:811,851` | PULLED / REFERENCED | Bare citation + self-diagnosed stale-site list, no independent number | Yes |
| `references/values_master.yaml:212-217` | HARDCODED DUPLICATE | Frozen extraction, filed under a nonexistent file path | **No — struck pre-ED-901 formula** |
| `references/values_master.yaml:1150-1163` | HARDCODED DUPLICATE | Frozen extraction of the real `params/core.md`, never regenerated | **No — a third, differently-worded stale formula** |
| `references/values_master.yaml:327-329` | HARDCODED DUPLICATE | Old wound-penalty model | No (see term 9) |
| `sim/personal/combat.py:45-48,120-132` | HARDCODED DUPLICATE, self-labeled DEPRECATED | Independent restatement, explicit deprecation banner | No — old formula, by design |
| `sim/cross_scale/scene_dispatch.py:96` | **LIVE WIRING TO A HARDCODED DUPLICATE** (not a mere citation — an executable call) | `import sim.personal.combat as combat; combat.resolve_combat_round(...)` | **No — actively executes the deprecated formula when this dispatch path fires** |
| `combatant.py:117` (`self.pool`) | HARDCODED DUPLICATE, but dead/unread | Independent restatement of the *current* correct formula; zero call sites | Agrees today, but duplication risk remains and it's flagged dead in the workplan doc |
| `canon/mechanics_index.yaml:210-219` | PULLED / REFERENCED | Correct citation, correctly labels the deprecated module — but is contradicted by the scene_dispatch.py wiring it doesn't know about | Textually yes; operationally the claim "repointed off the deprecated sim" is false for the scene_dispatch.py path |
| `tests/sim/v32-combat-balance/r1_sigma_resolution.py:71-72` | HARDCODED DUPLICATE (deliberately frozen/archival) | Explicit banner retains it for historical parity runs | Yes, by design, non-live |

**Incidental usage excluded:** none — every "pool" occurrence traced was the Combat Pool mechanic (fieldwork/thread/contest pools were noted only where they cross-reference Combat Pool's construction).

---

## 9. Wound-Ob penalty

**Home definition:** `designs/scene/combat_engine_v1/config.py:65`: `WOUND_ATK_OB=0.15, WOUND_DEF_OB=0.25` — "+0.15 Ob attacking / +0.25 Ob defending per wound; supersedes the -1D aggressor-only pool penalty (ED-1021)." Ratified by Jordan 2026-07-08 per `combatant.py:16-19,54-56`: *"WOUND_POOL_PENALTY removed 2026-07-08 (ED-PC-0005 ruling: wounds NEVER cut pools -1D; each wound adds a fractional Ob instead)."* Consumed at `systems.py:664,693,805`.

**Mechanism nuance worth flagging:** despite the "_OB" naming and the prose framing ("adds a fractional Ob to the roll"), the implementation is **not** a literal Ob (obstacle-threshold) shift. `core.py:25-53` fixes `DECISIVE_OB=3` for every action and explicitly states `SL.eff_ob is display-only`; the wound terms are added into `net_sigma` (`systems.py:664,693,805`, and consumed in `assemble_net_sigma`), which shifts the roll's mean via a mu-shift, not the Ob itself. The mechanism achieves an Ob-like *effect* but is architecturally a sigma addend — the name and the prose description ("adds a fractional Ob") are a step removed from the literal code path.

**Exhaustive usage sweep:** `config.py:65`; `systems.py:664,693,805`; `combatant.py:16-19,54-56` (docstring only, no independent numbers); `derived_stats_v30.md:72` (independently restates `+0.15`/`+0.25`); `references/engine_params/combat_engine_v1.json:201-202` (generated export, `"WOUND_ATK_OB": 0.15, "WOUND_DEF_OB": 0.25`); `references/module_contracts.yaml` (mentions "bilateral-Ob wounds" conceptually, no literal numbers); `params/core.md:158` (independently restates the ED-1041 values: "+0.15 Ob attacking / +0.25 Ob defending per wound"); `references/values_master.yaml:326-331` (**stale** — the OLD `-1D` model, filed under the nonexistent `params/combat.md`); `designs/provincial/clock_registry_v30.md:76` — cites `"params_combat.md §Wounds"` for the Wounds track, a **dangling citation**: `params/combat.md` was moved to `deprecated/params/combat.md` (confirmed via `mechanics_index.yaml:213`'s own comment "params/combat.md deprecated -> deprecated/params/"); the correct current home is `params/core.md:158` / `derived_stats_v30.md §4.1`.

**Divergence check:**
- `references/values_master.yaml:326-331` still carries: `"Per Wound" | "**−1D Combat Pool only** (no Ob penalty)"` — the exact model ED-PC-0005 (2026-07-08, the *same day* as this audit) reversed. Given the currentness of this reversal, this is expected/tolerable staleness in a file already globally quarantined, but it is the textbook case this audit exists to catch: a hardcoded duplicate of a design decision that has since flipped 180 degrees (from "-1D pool, no Ob" to "no pool cut, fractional Ob").
- `clock_registry_v30.md:76`'s citation to `params_combat.md §Wounds` points at a deprecated, relocated file rather than the current `params/core.md:158`/`derived_stats_v30.md`.

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees? |
|---|---|---|---|
| `config.py:65` | CANONICAL DEFINITION | — | — |
| `systems.py:664,693,805` | CANONICAL DEFINITION (consumer, reads `cfg['WOUND_*_OB']` — not an independent literal) | `cfg['WOUND_DEF_OB']*wounds - cfg['WOUND_ATK_OB']*wounds` | Yes |
| `references/engine_params/combat_engine_v1.json:201-202` | PULLED / REFERENCED | GENERATED by `tools/export_engine_params.py` from `config.py`, round-trip-checked in CI | Yes |
| `params/core.md:158` | HARDCODED DUPLICATE | Independently restates `+0.15`/`+0.25`, cites ED-1041/config.py/systems.py by name but has no automated regeneration link | Yes, currently |
| `derived_stats_v30.md:72` | HARDCODED DUPLICATE | Same as above | Yes, currently |
| `references/values_master.yaml:326-331` | HARDCODED DUPLICATE | Frozen snapshot, pre-dates ED-PC-0005 | **No — reversed model** |
| `clock_registry_v30.md:76` | STALE CITATION (bare pointer, not a value-restatement) | Points at a relocated/deprecated file | Citation is broken; doesn't itself restate a wrong number |

**Incidental usage excluded:** none.

---

## 10. grip_position

**Home definition:** `designs/scene/combat_engine_v1/combatant.py:102`: `self.grip_position=0.0` — "CONTINUOUS grip-position in [0,1]: 0=as-issued (full reach), 1=gathered to the working balance (close control)." Derived per-beat by `systems.py:172-182` `grip_target(c, closed, cfg)`, written by the wrapper at `wrapper.py:66`.

**Usage sweep:** confined entirely to the `combat_engine_v1` ecosystem and its own audit trail: `wrapper.py:66,71`; `config.py:98,100`; `core.py:171,180`; `systems.py` (10+ read sites, all via `getattr(c,'grip_position',0.0)` — lines 25,38,53,57,74,86,147,166,180-182,329,335,469,478); `combatant.py:102`; plus design/audit docs (`phase4_5_plan_v1.md`, the 2026-07-01/07-02 closing-distance-redesign audit trail, `HANDOFF_PC.md`, `HANDOFF.md`) and `tests/valoria/test_combat_invariants.py`, `test_combat_units_refactor.py`, `test_combat_recoverability.py`, `test_combat_stance.py`.

**Divergence check:** none found. Every read site uses `getattr(c,'grip_position',0.0)` against the single owning attribute; the only writer is `systems.grip_target` via `wrapper.py:66`. No duplicate formula or competing definition exists anywhere in the corpus — this is a clean single-owner attribute.

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees? |
|---|---|---|---|
| `combatant.py:102` | CANONICAL DEFINITION (attribute declaration/semantics) | — | — |
| `systems.py:172-182` (`grip_target`) | CANONICAL DEFINITION (derivation logic) | Sole writer-side formula | — |
| `wrapper.py:66` | PULLED / REFERENCED | Calls `S.grip_target(...)`, assigns result | Yes |
| All other `systems.py`/`core.py` read sites | PULLED / REFERENCED | `getattr(c,'grip_position',0.0)` — reads the live attribute, no independent restatement | Yes |
| Test files (`tests/valoria/test_combat_*.py`) | PULLED / REFERENCED | Exercise the live attribute via the engine's own API | Yes |

**Incidental usage excluded:** none — no ordinary-English collision exists for this compound term.

---

## 11. initiative (personal combat)

**Home definition:** `combatant.py:128`: `self.initiative=0.0` — "the Vor/Nach state (signed; +ve = holds initiative)." Range: clamped to `[-INIT_CAP, INIT_CAP]` via `systems.py:745-747` `clamp_initiative`, with `INIT_CAP=1.5` (`config.py:121`). Effect formula: `systems.py:673-678` `initiative_sigma = INIT_SIGMA_K*tanh((aggressor.initiative-defender.initiative)/INIT_SCALE)`.

**Usage sweep:** `combatant.py:128`; `config.py:121` (`INIT_DECAY=0.75, INIT_CAP=1.5`); `systems.py:673-678` (`initiative_sigma`), `:733,745-747` (`clamp_initiative`), `:753-773` (`init_steal_factor`, `init_hold_decay`, `init_overcommit_loss`), `:817-822` (`init_emphasis_sigma`); `wrapper.py` (writes via `clamp_initiative` at the indes-steal and overcommit-exposure points); `tests/sim/combat-stress-matrix/stress_matrix.py` (stress-tests the same live attribute, no independent restatement).

**Divergence check:** none found — every touch point is a read/write against the same `Combatant.initiative` float via `clamp_initiative`/`initiative_sigma`; no second definition or competing range exists in the corpus.

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees? |
|---|---|---|---|
| `combatant.py:128` | CANONICAL DEFINITION | — | — |
| `config.py:121` | CANONICAL DEFINITION (tunable constants: `INIT_CAP`, `INIT_DECAY`) | — | — |
| `systems.py` (all initiative functions) | CANONICAL DEFINITION (derivation/consumption logic) | Pure functions reading/returning against the live attribute | — |
| `wrapper.py` (mutation sites) | PULLED / REFERENCED | Calls `clamp_initiative`/`S.initiative_sigma` | Yes |
| `references/engine_params/combat_engine_v1.json` | PULLED / REFERENCED | `INIT_CAP`/`INIT_DECAY` present in the generated export (verified `config.py` section keys) | Yes |
| `tests/sim/combat-stress-matrix/stress_matrix.py` | PULLED / REFERENCED | Exercises live engine, no independent formula | Yes |

**Incidental usage excluded:** "initiative" as a colloquial English word ("player agency", "domain action initiative," narrative "seize the initiative" prose in arcs/audits) appears widely across the corpus but was excluded — only the combat-engine `Combatant.initiative` float and its Vor/Nach mechanics were counted.

---

## 12. poise

**Home definition:** `combatant.py:129`: `self.poise=1.0` — "kuzushi/balance (1.0=balanced, broken downward)." Range `[POISE_FLOOR, 1.0]` via `systems.py:783-785` `clamp_poise`, `POISE_FLOOR=0.5` (`config.py:128`). Effect: `systems.py:776-781` maps `[POISE_FLOOR,1]` structure to a `[POISE_EFFECT_FLOOR,1]` tempo/defence multiplier, `POISE_EFFECT_FLOOR=0.88`. Recovery: `systems.py:836-837`, `POISE_RECOVER=0.20`, `POISE_FOCUS_K=0.10` (`config.py:128`). Breaks: `POISE_BREAK_OVERCOMMIT=0.09`, `POISE_BREAK_BIND=0.05`, `POISE_BREAK_HIT=0.07` (`config.py:129`).

**Usage sweep:** heavily used, all within `combat_engine_v1` and its ~30-file audit trail (`combat_throughlines_v1.md`, `ability_armature.md`, the 2026-06-13/06-22/06-28/06-29/07-01/07-08 combat audit directories, `scene_combat_design_v1.md`). Spot-checked several: `wrapper.py:167-168,193` (applies `clamp_poise` on overcommit exposure); `systems.py:776-785,836-837`; `combatant.py:129`. All consistent — no independent numeric restatement of the poise formula found outside `config.py`/`systems.py`; audit docs discuss poise's *design implications* (e.g., `personal_combat_stat_and_weapon_breakdown_2026-06-13.md`) without re-deriving its formula.

**Divergence check:** none found.

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees? |
|---|---|---|---|
| `combatant.py:129` | CANONICAL DEFINITION | — | — |
| `config.py:128-129` | CANONICAL DEFINITION (tunables) | `POISE_FLOOR/EFFECT_FLOOR/RECOVER/FOCUS_K/BREAK_*` | — |
| `systems.py:776-785,836-837` | CANONICAL DEFINITION (derivation) | `balance_eff`, `clamp_poise`, poise-recovery function | — |
| `wrapper.py:167-168,193` | PULLED / REFERENCED | Calls `S.clamp_poise` | Yes |
| Audit/design docs (30+ files) | PULLED / REFERENCED (conceptual discussion) | Discuss poise's role without restating its numeric formula | Yes |

**Incidental usage excluded:** none — "poise" has no competing ordinary-English game-mechanical use in this corpus.

---

## 13. disp / Disposition (combat aggression axis, cross-checked against NPC-relationship Disposition)

**Home definition (combat):** `combatant.py:99`: `self.disp=4` (constructor default) — `"disposition / temperament, aggression axis (1-7, 4=neutral); lean=(disp-4)/3, orthogonal to tradition"`. Consumed in `systems.py:695-699` `commit_depth` (disposition lean skews a Beta draw over `[2,5]` commitment depth).

**Cross-batch collision (explicitly required by this batch):** `references/glossary.md:160` (Part Seven, World/Narrative Terms) defines a **completely different** "Disposition": *"NPC-attached attitude state toward another entity (PC, faction, settlement). Drives behaviour-tree branching in NPC AI. Canonical in `designs/npcs/npc_behavior_v30.md`."* Confirmed by reading `designs/npcs/npc_behavior_v30.md` directly: this Disposition uses a **signed, apparently unbounded** integer scale (observed values in the file: `+5, +3, +2, +1, −1, −2, −3, −4`, e.g. lines 192, 359-362, 428-458, 650-951) representing relationship sentiment, gated behavior triggers ("Disposition ≥ +2"), and Knot-formation prerequisites — entirely unrelated in scale, mechanism, and purpose to `combatant.disp`'s 1-7 in-fight aggression-lean axis.

**These are two genuinely distinct mechanics sharing a name/abbreviation family, and the collision is unflagged.** `references/glossary.md` Part Twelve ("COLLISION / DISAMBIGUATION TABLE," lines 235-246) exists specifically to catalog abbreviation conflicts (it lists CI, CP, TD, COMP, RS) but **does not list `disp`/Disposition** despite both existing live in the corpus. This is a gap in the very mechanism (Part Twelve) designed to catch exactly this kind of collision.

**Usage sweep (`disp`, combat sense):** `combatant.py:99,`; `systems.py:695-699` (`commit_depth`); no other files reference `Combatant.disp` by that attribute name outside `combat_engine_v1`'s own modules and its audit trail (spot-checked `designs/audit/2026-06-13-combat-bottomup/*` — discusses "disposition/temperament" conceptually, no independent numeric restatement).

**Usage sweep (Disposition, NPC sense):** `references/glossary.md:160`; `designs/npcs/npc_behavior_v30.md` (60+ occurrences, e.g. lines 192,359-362,416-458,650-951, consistent signed-integer relationship-gate usage throughout); `designs/npcs/npc_behavior_v30_infill.md` (co-filed prose, not separately verified line-by-line here but expected consistent per co-filing convention); `designs/scene/fieldwork_v30.md` (`params/core.md:149` cites "Disposition +5 + TS ≥ 30" for Knot Formation — matches the NPC sense).

**Divergence check:** not a numeric divergence (they're not competing definitions of the *same* stat) — it is a **naming collision between two unrelated mechanics**, exactly the kind of thing Part Twelve is supposed to catch and doesn't. Quoting both:
- Combat: `combatant.py:99` — `disp=4` default, "aggression axis (1-7, 4=neutral)... orthogonal to tradition."
- NPC: `glossary.md:160` — "NPC-attached attitude state toward another entity... Drives behaviour-tree branching."

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees? |
|---|---|---|---|
| `combatant.py:99` | CANONICAL DEFINITION (combat `disp`) | — | — |
| `systems.py:695-699` | PULLED / REFERENCED | Reads `aggressor.disp`/`defender.disp` via the commit-depth Beta skew | Yes |
| `designs/npcs/npc_behavior_v30.md` (60+ lines) | CANONICAL DEFINITION (NPC Disposition — distinct mechanic, per its own glossary-cited home) | — | N/A — different mechanic, not a divergence from combat `disp` |
| `references/glossary.md:160` | PULLED / REFERENCED (NPC sense) | Cites `npc_behavior_v30.md` as canonical | Yes, for the NPC sense |
| `references/glossary.md` Part Twelve (collision table) | **UNCLEAR / GAP** | Collision-detection mechanism exists but omits this pair | N/A — the omission itself is the finding |

**Incidental usage excluded:** none — both senses found are game-mechanical; no ordinary-English "disposition" (as in "temperament" in prose descriptions of NPCs outside the tracked-stat sense) was counted toward either definition unless it was clearly invoking the tracked mechanic (e.g., a bare narrative adjective like "he has a suspicious disposition" would have been excluded, but no such cases were found in the sampled files — all hits were the tracked stat).

---

## 14. Momentum (combat — cross-checked against Batch 2's world clocks)

**Home definition:** `references/glossary.md:54` (Part One, Derived Character Stats): `"Momentum | — | 0-4 | Tactical resource. Gained on Overwhelming success or Belief achieved. Spent for automatic successes (non-Thread only)."` Full mechanical rules in `params/core.md:84-93,170-180`: range 0-4, `+1` on Overwhelming (`:49`), spend 1 Momentum = 1 automatic success (non-Thread rolls only, `:87`), resets to 0 at session start, carries between scenes within a session but not across sessions (`:90-93`), auto-successes add to (not replace) the roll and can be cancelled by a rolled 1 (PP-243, `:172-180`).

**Cross-check against Batch 2 (world clocks):** `designs/provincial/clock_registry_v30.md:66-78` correctly files Momentum under "## Personal Tracks (TTRPG/Hybrid)" (a per-character track), range `0–4`, start `0`, citing `params_core.md §Momentum` — this is **not** one of Part Two's shared/world clocks (Mending Stability, Church Influence, Institutional Pressure, Public Instability); it's correctly kept out of that bucket. No collision found here — Momentum is unambiguously the Part One personal tactical resource in every site checked. The apparent world-scale hits for "momentum" (`victory_v30.md:673`, `faction_layer_v30.md:619`: **"Institutional Momentum: CI +1 (passive)"**) are **incidental English usage** — a descriptive label for a Church-Influence passive-gain trigger, not a distinct tracked stat named "Momentum"; excluded from the game-mechanical count.

**Critical finding: Momentum is declared canonical but has zero implementation in the live personal-combat resolver.** Exhaustive sweep of `designs/scene/combat_engine_v1/*.py` (`combatant.py`, `core.py`, `systems.py`, `wrapper.py`, `config.py`, `ability_primitives.py`, `capabilities.py`, `tradition.py`, `traditions.py`, `state_graph.py`) for "momentum" (case-insensitive) returns **exactly one hit**, and it's an unrelated physics metaphor: `core.py:110` — *"(E=1.0, momentum-like)"* in a comment about percussion-authority transmission, not the game stat. `combatant.py` has no `momentum` attribute; `core.py`'s `degree()` function determines 'overwhelming' outcomes but never increments any counter; `wrapper.py`/`systems.py` never touch it. `references/module_contracts.yaml`'s `personal_combat` module entry (`:819-825`) lists declared state as `Health, cumulative_damage, Wounds, Stamina, Initiative, Poise` — **Momentum is absent from this list entirely.**

This gap is honestly (if tersely) self-documented: `canon/mechanics_index.yaml:111-119` —
```yaml
momentum:
  scale: primitive
  canon_sources: ["params/core.md#Momentum", "params/core.md#Momentum Carry"]
  sim_module: sim/autoload/dice_engine.py
  test_status: not_implemented
  notes: "PP-255 momentum carry mechanic."
```
Confirmed: `grep -in momentum sim/autoload/dice_engine.py` returns zero hits — the `sim_module` pointer is itself aspirational/wrong (points at a file that doesn't implement it), but at least `test_status: not_implemented` is honestly flagged, so this is a properly-disclosed gap rather than a silent one — worth noting precisely because most of this batch's findings are *silent* staleness, and this one isn't.

**Usage sweep (non-exhaustive list given very high hit-count from ordinary-English "momentum"):** game-mechanical hits — `references/glossary.md:54`; `params/core.md:49,84-93,170-180`; `designs/provincial/clock_registry_v30.md:78`; `references/values_master.yaml` (multiple entries mirroring `params/core.md`, not independently checked line-by-line here beyond confirming consistency with the params doc); `canon/mechanics_index.yaml:111-119,947`; `designs/scene/derived_stats_v30.md:442,521`. Excluded-as-incidental: the dozens of "momentum" hits in `designs/provincial/*_v30.md`, arc files, and audit prose that use the word colloquially (e.g., "Institutional Momentum," "campaign momentum," "the audit has momentum") — spot-checked a representative sample (`victory_v30.md:673`, `faction_layer_v30.md:619`, `military_layer_v30.md:237,249`) and confirmed none of them introduce a competing tracked-stat definition.

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees? |
|---|---|---|---|
| `params/core.md:84-93,170-180` | CANONICAL DEFINITION | — | — |
| `references/glossary.md:54` | PULLED / REFERENCED | Concise restatement matching params/core.md | Yes |
| `designs/provincial/clock_registry_v30.md:78` | PULLED / REFERENCED | Cites `params_core.md §Momentum` directly | Yes |
| `canon/mechanics_index.yaml:111-119` | PULLED / REFERENCED, but with a broken pointer | `sim_module: sim/autoload/dice_engine.py` — this file does not implement Momentum | Honestly flagged `not_implemented`, but the `sim_module` field itself is inaccurate |
| `designs/scene/combat_engine_v1/*.py` (entire package) | **ABSENT — no implementation site exists** | Zero attribute, zero increment/spend logic anywhere in the live personal-combat resolver | N/A — canonical mechanic with no live combat-engine implementation |
| `references/module_contracts.yaml:819-825` (personal_combat `state:` list) | ABSENT by omission | Momentum is not declared as tracked state for the personal_combat module | N/A |
| `designs/provincial/victory_v30.md:673`, `faction_layer_v30.md:619` | INCIDENTAL ENGLISH USAGE (excluded) | "Institutional Momentum" is a descriptive label for a CI passive-gain trigger, not the tracked Momentum stat | N/A |

**Incidental usage excluded:** the "Institutional Momentum" phrase (CI passive-gain framing) in `victory_v30.md`/`faction_layer_v30.md`, and general colloquial "momentum" throughout narrative/audit prose corpus-wide, were excluded as ordinary English, not the tracked 0-4 stat.
