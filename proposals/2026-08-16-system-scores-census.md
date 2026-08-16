# System Scores Census — every attribute and score, by system

## Status: MEASURED REFERENCE — not a proposal, not ratified, not canon. This document records **what the code declares and reads**, so the bottom-up attribute method (`proposals/2026-08-15-character-and-faction-stats-and-progression.md` §19) has raw material. Nothing here is a recommendation.

**Date:** 2026-08-16 · **Lane:** IN · **Companion to:** `2026-08-15-character-and-faction-stats-and-progression.md` (§16 maps, §19 promotion criterion)
**Method:** AST over entity declarations (`__init__` / dataclass fields) plus direct reading of the resolvers. Not grep frequency — that instrument was measured to *invert* the truth (see the companion §1.3, §17.4).

**Legend — role of a score in resolution:**
`POOL` sizes the dice pool · `BLEND` enters a computed faculty · `GATE` a threshold, never rolled ·
`CEILING` bounds a resource · `TRACK` accumulates/decays · `META` carried but never read by a resolver ·
`STATE` live per-resolution · `DECLARED` present in the entity, read by nothing.

---

## 1. PERSONAL COMBAT — `systems/combat/combat_engine_v1/`

Entity: `Combatant` (`combatant.py:93-116`).

| score | own/borrowed | role | site |
|---|---|---|---|
| `history` | **own** | **POOL — the entire pool**, `max(5, History+6)` | `core.py:50` |
| `strength` | borrowed | BLEND — Impact `Str+heft`; `½Agi+½Str` balance; bind; `0.25·Str·End` health | `core.py:537`, `combat_systems.py:188,1061` |
| `agi` | borrowed | BLEND — tempo `K(agi−4)`; reflex; balance; footwork | `combat_systems.py:113,172,188,836` |
| `end` | borrowed | BLEND — `WI = End+4+0.4·Spi`; `stamina = 3End+2Spi`; MW | `combatant.py:20-47` |
| `cog` | borrowed | BLEND — `reading = (2Cog+Att)/3` | `combat_systems.py:171` |
| `att` | borrowed | BLEND — reading (⅓); reflex | `:171,172` |
| `spirit` | borrowed | BLEND — WI, health, stamina, `conc = 3Foc+2Spi` | `combatant.py:21,27,41` |
| `focus` | borrowed | BLEND — `conc_max`; `disrupt_resist`; `poise_regen` | `:1435,1451` |
| `disp` | **own** | BLEND — commit skew, counter tilt, Vor drift | `:186` |
| `skills{bind,parry,dodge,balance,technique,grab}` | **own** | BLEND — additive into σ terms. **Only these 6 axes are read**; any other key is inert | `:188,332,349,1052`, `contact.py:47` |
| `equipped{name: level}` | **own** | BLEND — graded technique modulators on named levers | `ability_primitives.py:129-151` |
| `tradition` | **own** | GATE (ability access) + BLEND (`familiarity` → wariness) | `traditions.py:47-55` |
| `weapon`, `armor` | **own** | BLEND — dominant; ~40 of ~60 derived functions read `c.w` | `weapons.py`, `weapon_physics.py` |
| **computed faculties** | **own** | reading · reflex · balance_eff · weapon_tempo · close_tempo · impact · durability (WI/health/MW) · stamina_max · conc_max | `combat_systems.py` |
| **live state** | — | STATE — `stamina`, `conc`, `poise`, `initiative`, `wounds`, `grip_position`, `lunge_depth`, `facing`, `range_avail`, `sel_*` | `combatant.py:104-131` |

**Obstacle:** fixed `DECISIVE_OB = 3` (`core.py:45`). **Channel:** σ carries all opposition.

---

## 2. SOCIAL CONTEST — `systems/social_contest/sim/contest/`

Entity: `Contestant(faculty, standing_start, reserve_max, dossier, evidence, charisma)` (`resolver.py:182`).

| score | own/borrowed | role | site |
|---|---|---|---|
| `faculty` | **own** | **POOL** `faculty×2+3` **and BLEND** `(faculty−4)/6` into σ — **double-dipped** | `primitives.py:211,227-230` |
| `standing_start` → `Standing`/`Face` | **own** | TRACK 0–10, ethos-built; feeds Readiness + leak | `primitives.py:31-47` |
| `reserve_max` → `Reserve` | **own** | CEILING/TRACK — stamina, per-move cost, `regroup` | `:49-56` |
| `dossier` / `evidence` | **own** | BLEND — `EvidenceItem(ground, weight, appeal)`, corroboration decay | `:282-310` |
| `charisma` | borrowed | **CEILING only** — `Face_max = Cha×3`; explicitly *"NOT kernel state"* | `:128,142` |
| `Room` | **own** | TRACK — pathos accumulator, cap 3.0 | `:232-236` |
| `Stasis` | **own** | GATE — 6-rung ground ladder, upward-only | `:11-25` |
| `Readiness` / `Resonance` / `leak` | **own** | computed — `0.40 + 0.60·min(1, 0.40·sf + 0.40·rf)` | `:238-260` |
| `ADJUDICATOR_PRIMARY` (Cog/Cha/Att) | borrowed | **META** — read by the adapter (`wrapper.py:159`), never by the resolver | `modes.py:426-431` |

**Obstacle:** flat `venue.base_ob` (default 2.0). **Channel:** pool **and** σ.

---

## 3. THREADWORK — `systems/threadwork/sim/`

Actor is duck-typed (no dataclass). Entity: `CoherenceState(actor, coherence, band, log, crisis_active)`.

| score | own/borrowed | role | site |
|---|---|---|---|
| `spirit` | borrowed | **POOL** `Spirit×2`; Thread-Fatigue threshold `Spirit×5` (doc; unimplemented) | `operations.py:157` |
| `ts` (Thread Sensitivity) | **own** | **POOL** `⌊TS/10⌋` + **GATE** (≥30 Leap, ≥50 Lock/Dissolve) + **sets the OPPONENT's Ob** `⌊opp_TPS/2⌋` | `:98-101,145-157`; `opposing.py:80-85` |
| `coherence` | **own** | TRACK 10→0, banded; +Ob on all future Thread ops | `coherence.py:114-127` |
| `history` | borrowed | **INERT** — `min(3, history+3)` returns 3 for any `history ≥ 0`. Docstring says *"optionally `.history` dict"* | `operations.py:17,153-157` |
| `cognition` | borrowed | BLEND — collective-op helper only, `⌊Cog/2⌋` | `collective.py:58-64` |
| `focus` | borrowed | **DECLARED, NEVER READ** — named in the module docstring, no function body touches it | `operations.py:16` |
| `BREADTH_OB` / `DISTANCE_OB` | **own** | **DECLARED, NEVER READ** — the "Three-Axis Ob" is Depth-only in practice | `:82-96` |

**Obstacle:** scale table (`DEPTH_OB`, Fibonacci 1→13) **+ opponent TPS ÷ 2**. **Channel:** pool only. **TN varies** (7/8/9) — the only subsystem that moves TN.

---

## 4. KNOTS (relational) — `systems/fieldwork/sim/knots.py`

Entity: `Knot(knot_id, actor_a, actor_b, tier, strain, disposition, active, formed_season, log)`.

| score | own/borrowed | role | site |
|---|---|---|---|
| `bonds` | borrowed | **GATE** — `≥5` to form; max count `⌊Bonds/2⌋+1`. Never rolled | `knots.py:185` |
| `spirit` | borrowed | **POOL** `Spirit×2` | `:216` |
| `history_relationships` | borrowed | **POOL** — note: a **different field** from combat's `history` | `:215` |
| `ts` | borrowed | GATE | `:186` |
| `disposition_with_X` | **own** | GATE (+5 to form) | `:50` |
| `strain` | **own** | TRACK −5..+5; rupture at +5, Tempered at −5 | `:266,304` |
| `tier` | **own** | STATE — Distant/Close; the degree selects a persistent **object type** | `:227` |

**Obstacle:** fixed 2. **Channel:** pool only.

---

## 5. MASS BATTLE — `systems/mass_battle/sim/`

Entities: `Unit`, `Subunit` (`units.py:326,51`). ⚠ `tests/sim/mass_battle/` is the **J2 canon** engine (Jordan ruling 2026-08-03); this table covers the **wired** one that `faction_action` calls.

| score | own/borrowed | role | site |
|---|---|---|---|
| `power` | **own** | BLEND — the only damage multiplier, `(1+power)` | `massbattle.py:965` |
| `command` | **own** | POOL — twice: `min(size, command) + command` | `units.py:398-407` |
| `discipline` / `discipline_start` | **own** | POOL penalty; movement; formation hold. Persists across battles | `:382-386` |
| `morale` / `morale_start` | **own** | GATE — rout. Resets each battle (PP-711) | `:375-380` |
| `size`, `hp`, `size_max`, `hp_max`, `h_per_size` | **own** | POOL/STATE — `Size = ⌊TroopCount/block⌋` | `:358-380` |
| `dr` | **own** | flat subtractor on damage | `massbattle.py:965` |
| `stance`, `speed`, `routed`, `broken`, `stamina` | **own** | STATE / modifiers | `units.py` |
| `shape`, `troop_type`, `tier`, `starting_position`, `advance_dir`, cell geometry | **own** (Subunit) | BLEND — octagon facing, engage fraction | `units.py:51-99` |
| `charisma`, `cognition` | borrowed | BLEND — **only** via `Command = ⌈(2Cha+Cog)/3⌉` | `mass_battle_v30.md:298-317` |
| **physical attributes** | — | **ABSENT.** No `strength`/`agi`/`end` read exists in `units.py`. Canon: *"No mass-battle mechanic kills the general."* | — |

**Obstacle:** the opponent's net — the only opposed-roll resolver. ⚠ **The degree is a dead assignment** (damage reads raw `net`).
⚠ **At the wired strategic entry, `_faction_to_unit` hardcodes `shape='Line', tier=2, command=4, discipline=5, morale=5` and co-locates both sides** — every score above except `power` is unreachable there.

---

## 6. FACTIONS — `engine/autoload/game_state.py`, `systems/factions/sim/`

Entity: `Faction(name, parliamentary, L, Sta, W, I, Mil, intel, territories, standing, excommunicated, peaceful, …per-arc flags)`.

| score | own/borrowed | role | site |
|---|---|---|---|
| `W` (Wealth) | **own** | POOL — Muster `Mil + ⌊W/2⌋` | `faction_action.py:538` |
| `Mil` (Military) | **own** | POOL / advantage signal | `:145-163` |
| `I` (Influence) | **own** | POOL — the Govern action pool | `:560` |
| `Sta` (Stability) | **own** | GATE — 5 canonical triggers; collapse at 0; floor at ≤2 | `faction_layer_v30 §1.2-1.5` |
| `L` | **own** | TRACK — **used as the scalar Mandate** (the superseded pre-LPS-1 convention) | `game_state.py:100` |
| `standing` | **own** | POOL term (`crown_initiative`) + TRACK — **the only durable, cross-season, pool-feeding standing in the tree** | `crown_initiative.py:79,115` |
| `intel` | **own** | **DECLARED, NEVER READ** — *"currently unread/unwritten by live code"* | `game_state.py:105-110` |
| **character attributes** | — | **NONE.** No character attribute reaches any faction action. | — |

---

## 7. SETTLEMENTS — `systems/settlements/sim/registry.py`

Entity: `Settlement(sid, name, stype, province_id, owner_faction, governor_id, prosperity, defense, order, fort_level, garrison, legitimacy, popular_support, facility_tier, suspicion, pressure, active_directive, religious_building, church_attention, governor_emergence, subnational, npc_ids, ledger, open_needs, deck_state)`.

| score | own/borrowed | role | site |
|---|---|---|---|
| `prosperity`, `defense`, `order` | **own** | derived values (×50 / ×20+fort×30 / ×20) | `registry.py` |
| `fort_level`, `garrison`, `facility_tier` | **own** | BLEND / CEILING | `registry.py` |
| `ap` (Administration Points) | **own** | CEILING — the governance action economy, `AP = 2 + FacilityTier` | `registry.py:92`; `governance_play_redesign_v1 §28-33` |
| `compliance(s)` | **own** | BLEND — local attenuation; *"the CK3-Administrative shape realized as a formula"* | `lps_wiring_v1.md:85-95` |
| `legitimacy`, `popular_support` | **own** | **DECLARED, NEVER READ or WRITTEN in `systems/`** — flagged inline | `registry.py:69-74` |
| `ledger` (Precedent/Grudge/Debt/Reputation/Leverage) | **own** | TRACK — durable, TTL, survives succession. **Zero consumers in `systems/`** | `ledger.py` |
| `suspicion`, `pressure`, `church_attention`, `governor_emergence` | **own** | TRACK | `registry.py` |
| **character attributes** | — | **NONE.** | — |

⚠ `Territory` (`game_state.py`) separately declares `accord, pt, garrison, prosperity, fort_level, templar` — **`prosperity`, `fort_level` and `garrison` exist at both settlement and territory scale.** Whether these are the same quantity at two grains, or two quantities sharing three names, is unresolved.

---

## 8. FIELDWORK (exploration / investigation)

**No scores are read by any resolver.** `fieldwork.py` and `investigation.py` are `stubwire.stub_resolve` at all six entry points. The design assigns Cognition (Examine/Surveil/Cover), Attunement (Interview/Read/Negotiate), Recall (Research/Reconstruct), Spirit (Thread-Read/Sincerity), Endurance (marches), Bonds (Connect), Charisma (Impress/Rumour/Converse) — **none of it executes.** Only Knots (§4) is live.

---

## 9. THE OVERLAP MATRIX — the raw material for the §19 promotion criterion

| score | combat | contest | thread | knots | mass btl | faction | settle | systems | same semantics? | same shape? |
|---|---|---|---|---|---|---|---|---|---|---|
| **Spirit** | BLEND | — | **POOL** | **POOL** | — | — | — | **3** | ✅ contact | ✅ (thread/knots both `×2`) |
| **Thread Sensitivity** | — | — | POOL+GATE | GATE | — | — | — | **2** | ✅ perceptual depth | ✅ gate |
| Cognition | BLEND | META | BLEND | — | BLEND | — | — | 4 | ❌ reading vs generalship vs lattice | ❌ |
| Charisma | — | CEILING | — | — | BLEND | — | — | 2 | ❌ Face vs command | ❌ |
| Attunement | BLEND | META | — | — | — | — | — | 1 | — | — |
| Strength / Agility / Endurance | BLEND | — | — | — | — | — | — | 1 | — | — |
| Focus | BLEND | — | **declared, unread** | — | — | — | — | 1 | — | — |
| Bonds | — | — | — | GATE | — | — | — | 1 | — | — |
| Recall | — | — | — | — | — | — | — | **0** | — | — |
| **"History"** | `history` POOL | — | `history` inert | `history_relationships` POOL | — | — | — | 3 | ✅ practice | ❌ **three different fields** |

**Reading it:** two scores clear all three promotion tests (**Spirit**, **Thread Sensitivity**); two are multi-system homonyms (Cognition, Charisma); five are single-system; **Recall is used by nothing**; and *History* is a **shape** — per-domain practice, already instantiated under three different field names.

---

## 10. SCORES DECLARED BUT NEVER READ

| score | entity | note |
|---|---|---|
| `focus` | threadwork actor | named in the module docstring; no function body reads it |
| `intel` | `Faction` | *"currently unread/unwritten by live code"* |
| `legitimacy`, `popular_support` | `Settlement` | flagged inline at `registry.py:69-74` |
| `BREADTH_OB`, `DISTANCE_OB`, `DEPTH_TS_MINIMUM` | threadwork | the "Three-Axis Ob" is Depth-only |
| `ledger` tags | `Settlement` | real and durable; **zero consumers in `systems/`** |
| `ADJUDICATOR_PRIMARY` | contest | read by the adapter, never by the resolver |
| all 6 unread `skills` axes | `Combatant` | dict accepts any key; only 6 are read |

## 11. SCORES READ BUT NEVER WRITTEN

Per the companion §16.0 (AST over assignments, excluding constructor self-assignment): **every one of the ten roster attributes, plus `history`, `ts`, `equipped`, `skills`, `tradition`, `faculty`, `renown` and `disposition`, has ZERO writers.** The only per-character quantity any live code changes is `coherence` (`coherence.py:155`), and it only decreases.

---

## 12. CAVEATS

1. **Static census.** Fields reached via `setattr`, dict-backed access or duck-typing may be missed. No evidence of those patterns was seen; their absence was not proven.
2. **`tests/sim/mass_battle/` is the J2 canon engine** and is *not* covered here; §5 covers the wired engine `faction_action` actually calls. The two differ.
3. **Fieldwork's assignments are design-only** — nothing executes, so §8 is a statement of intent, not of behaviour.
4. **"Own vs borrowed"** is a judgement about where a score is *declared*, not about who should own it. It is descriptive.
5. This is a **snapshot at `f92b840`.** It will change as systems are built — which, per §19, is the method working.

---

# 13. CORRECTIONS — adversarial audit 2026-08-16

An independent read-only critic audited every claim. **Five claims false, three role tags
unsupported, two overlap counts inflated, five entities missing.** Corrected here; the document above
is left intact so the corrections are legible as corrections.

## 13.1 ⚠ THE HEADLINE IN §11 IS FALSE

*"The only per-character quantity any live code changes is `coherence`, and it only decreases."*
**Wrong, and wrong in a way the instrument could not detect by construction.** The AST scan matched
only `ast.Attribute` targets, so **`Subscript` writes were invisible**:

- `systems/characters/sim/conviction.py:213` — `state.scars[conviction] = after` (plus
  `resonant_active`, `in_crisis` at `:217-220`), reached from live code at `knots.py:349-351`.
- `systems/world/sim/npe.py:355-365` — mutates NPC `stance[issue]` **up and down**.
- `wrapper.py:23-26,219,260,301-313,387-391` — writes `stamina`, `conc`, `poise`, `initiative`.
- `combatant.py:83-89` — `WoundTracker.apply` mutates `cumulative_damage`.

The defensible claim is narrower: **no *durable roster attribute* has an external writer.** That
still holds (verified: only constructor self-assignments). **The sweeping version is withdrawn.**

**Three blind spots, not one:** `setattr`, dict-backed access, **and subscript writes**. §12's caveat
1 — *"no evidence of those patterns was seen"* — is **falsified**: `known_traditions` is set
post-construction and read via `getattr` (`ability_primitives.py:118`), and `build_levers.py:33` is a
literal registry of the pattern (`_POST_INIT = ('known_traditions',)`). The repo had also already
proved the point: `test_public_governance_transfer_key.py:17-21` states that `Faction.adjust()`'s
`setattr` write *"an AST scan for `Attribute` targets cannot see."*

## 13.2 FALSE CLAIMS

| § | claim | correction |
|---|---|---|
| 3 | TS **"≥50 Lock/Dissolve"** gate | **No such gate.** `attempt_locking`/`attempt_dissolution` contain no TS check. The `50` at `operations.py:242` is a **Leap Ob band selector**. The ≥50 threshold lives in `DEPTH_TS_MINIMUM` — which §10 correctly lists as **never read**. The two claims contradicted each other. |
| 5 | `Command = ⌈(2Cha+Cog)/3⌉` | **`clamp(round((2·Cha + Cog)/3), 1, 7)`** — `round`, not ceiling, and the clamp was dropped. Code agrees with the doc, not with me (`exchange.py:49`). Written five times across both documents. |
| 5 | discipline **"persists across battles"** | **Not in the wired engine** — `_faction_to_unit` reconstructs `discipline=5, discipline_start=5` on every call. |
| 5 | Cha/Cog row tagged **BLEND** | **Violates §5's own scope note.** It cites a *design doc* in a table of code sites, and the derivation exists only in the **excluded** J2 engine, flag-gated (`COMMAND_SIGMA_ENABLED`), with `charisma`/`cognition` defaulting to `None` and classified **provably inert** by `test_field_golden_pins.py:47-49`. In the wired engine `command` is the literal `4`. |
| 7 | `AP = 2 + FacilityTier` | **`2 + facility_tier + bonus`**, `bonus = 1` at Seat/Cathedral/Cathedral-City (`registry.py:92-97`). |
| 9 | *"History — three different fields"* | **Two names, not three.** Combat and threadwork **both** read `.history`; only knots differs. **The real finding is worse:** one name carrying two incompatible semantics — the entire combat pool, and structurally inert in threadwork. That is a homonym collision, not a naming spread. |
| 5 | *"the only opposed-roll resolver"* | **False** — `opposing.resolve_opposing_operations` rolls both practitioners against Obs set by each other's TS. §3 documents this two sections earlier. |

## 13.3 UNSUPPORTED ROLE TAGS (§7 is the weakest section)

- **`ap` tagged CEILING** — it has **zero readers** in `systems/`. Same evidentiary position as
  `legitimacy`/`popular_support`, which this document *does* flag as inert. Identical evidence,
  opposite tags.
- **`suspicion`, `pressure`, `church_attention`, `governor_emergence` tagged TRACK** — none is read
  or written anywhere in `systems/` outside `to_dict`/`from_dict`. Nothing tracks them.
- **`compliance(s)` tagged BLEND** — **zero occurrences in any `systems/**/*.py`**. It is from
  `lps_wiring_v1.md`, whose status is **PROPOSED**. A proposed formula was tabulated as measured.
- **The derived multipliers are mis-cited** to `registry.py`; they are in
  `systems/settlements/sim/settlement.py:89-91`.
- `legitimacy`/`popular_support` *"never read or written"* is literally false (`registry.py:120,145`
  — serialisation). The source comment's qualifier — *"zero **non-definition** references"* — was
  dropped.

## 13.4 OVERLAP MATRIX — both homonym counts inflated

- **Cognition: 4 → 3.** The mass-battle cell is doc-only and out of scope.
- **Charisma: 2 → 0 wired reads.** Contest is a display *view* (`FaceScale` consumers are the
  harness and tests; the wired adapter never sets `charisma`), and mass battle is the excluded
  engine. **The "multi-system homonym" verdict for Charisma rested entirely on two cells this
  document's own scope disallows.**
- Charisma's contest tag is corrected **CEILING → META/display**.
- Spirit, Thread Sensitivity, Attunement, Str/Agi/End, Focus, Bonds and **Recall = 0** all confirmed.

## 13.5 ENTITIES AND SYSTEMS MISSING

1. **`systems/characters/sim/` — omitted entirely.** Per-Conviction Scars, `certainty` 0–5 scaling
   severity, thresholds, season caps; plus `beliefs.py`, `companion.py`. **For a census whose purpose
   is raw material for a *character* stats method, this is the most consequential gap.**
2. **`systems/world/sim/npe.py`** — a second character-like entity (`stance`, `affiliation_loyalty`,
   `volatility`, `deviation_roll`) with live mutation.
3. **`systems/overview/sim/`** — the CI/RS/MS/IP world tracks; `ms_track` is called *by threadwork*.
4. **Contest's `Adjudicator` and `FaultState`** — the contest has three scored entities; §2 lists one.
5. **`SettlementState` / `ProvinceState`** (`settlement.py:44-75`) — a second settlement entity.
6. **The four degree ladders** — combat (held), threadwork/knots (`dice_engine`), contest
   (`sigma_leverage`), mass battle (bespoke size-fraction). **A census that catalogues pools and
   obstacles but not the degree channel omits the axis where the systems actually disagree.**

## 13.6 Also: §1 and §2 incompletenesses

`history` is not only POOL in combat — it is a σ BLEND at four further sites (`reading`, technique,
bind, counter-success), and the `reading` formula quoted in §1 **drops its History term**.
`known_traditions` is missing from §1 entirely. `Pool.size`'s `max(5, …)` floor is dropped in §2.
Several `file:line` citations are off by one to a few lines.

## 13.7 The pattern

The document's own method line says *"AST over entity declarations… not grep frequency."* The audit's
verdict is that **an AST over declarations is a weaker instrument than it appears**: it cannot see
`setattr`, dict writes, subscript writes, or post-construction attachment, and it says nothing about
whether a declared field is *read*. Role tags require reading call sites; several here were inferred
from the declaration and from design prose. **Where this document is wrong, it is wrong because a
declaration was read as though it were a behaviour.**
