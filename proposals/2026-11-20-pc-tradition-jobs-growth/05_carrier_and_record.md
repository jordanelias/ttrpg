# Part 5 — The carrier (where a person's tradition, techniques and boards live) and the record (how a player sees a technique at work)

## Status: PROPOSED. Reference only. **The carrier question is the plan's** (brief §3.8: "Where a person's tradition lives is PC-21's design"; the person-inputs proposal's Part D: "Tradition and disposition: no carrier is proposed here. PC-21 (design-first) owns where a tradition lives", `proposals/2026-11-12-subsystem-audit-suite/proposals/03_PC_person_inputs_content.md:114-115`). This part is input to PC-21, not a substitute for it.

## 5.1 What exists today (verified)

- `Person` holds `capability` (skills), `attributes`, `heritage`, `traits`, `body` and others; **no tradition, technique or board** (`engine/season/state/carriers.py:747-860`; field list read by grep).
- `combat_input` fills `kits`, `scores`, `addends`, `attributes`, `carried`, `ends`; it does not pass `traditions`, `techniques`, `axes` or `dispositions` (no occurrence in `engine/season/seam/wrappers/combat.py`), so they stay `()` (`inputs.py:203-206`: "The season fills none of them until a carrier exists").
- Two build-only fields set the precedent for a field filled once from a cast row and never written in play: `heritage` ("Filled ONCE at world build from a cast row's `heritage:` … NEVER WRITTEN IN PLAY", `carriers.py:823-829`) and `traits` (`:831-835`).
- **Cross-training cannot cross today's door.** The engine's gate unions the kits of `known_traditions` (`ability_primitives.py:174-177`), but `PersonalCombatInput` carries one tradition name per party and `fight.py` passes only `tradition=` to `Combatant` (`fight.py:58-63`, `:182-185`); `Combatant` takes no `known_traditions` argument (`combatant.py:106`). So a second school's techniques are inert in any fight built through the module entry. `sheets.py` shows it on sheets 4 and 5 (computed both ways). B18.02 removes the problem by moving the gate host-side; before it, the fix would be a field on the record.
- The skill map is not a home for techniques: `descriptors.CAPABILITIES` is "THE ONLY SKILL DEFINITION IN THE ENGINE" (`engine/substrate/descriptors.py:87`), and `train` writes only keys that are `VOCATIONS` members (`effects_combat.py:915-916`).

## 5.2 Carrier options, ranked

| | where | for | against |
|---|---|---|---|
| **C-1 (recommended)** | new `Person` fields, added one at a time, each with its reader in the same change | the `heritage`/`traits` precedent; the plan's host-side direction (B18.02: the host composes numbers per slot); no second meaning for an existing map | new fields on `Person` (each must name its reader, ID-13 "no field without a reader", cited at `carriers.py:775-776`) |
| C-2 | technique levels as capability keys (`fight:germanic`, the October adjudication's element 4, `2026-10-24-character-progression-adjudication.md:251`) | no new field; `train` already writes the map | a technique is not a skill (`descriptors.py:87`); `train`'s key must be a vocation; one map with two meanings is the second-owner defect (CLAUDE.md §8). The October answer was given when the duel was "zoomed out" (`:356-357`, "Texture is a good of the played duel; the seam is zoomed out"); B18 makes the duel a played scene, so that answer no longer holds |
| C-3 | nothing stored: levels derived from the record of `train` events, as PC-22 derives Concentration "from the log" | one source of truth | needs the event record to persist for a person's life and to be replayed per fight [UNVERIFIED: whether the season keeps its event record that long]; a level is a fact taught once, not a running summary |

## 5.3 The smallest first increment, and the steps after it

| step | adds | its one reader | what it changes in a fight | hash |
|---|---|---|---|---|
| **1** | `Person.tradition: Optional[str] = None`, filled once at build from a cast row's `tradition:` key (the `heritage_of` precedent); `None` is "untrained" | `combat_input`, which fills `traditions` only. **No technique is filled from membership:** a technique acts only at a level the person has on record (step 2), because efficacy "EMERGES from the invested level, not tradition membership" (`ability_primitives.py:13-15`) | familiarity starts to act (`combat_systems.py:936-938,990,1002`), the one effect a tradition name has without a technique (`traditions.py:8-10`); a person with a tradition and no recorded technique therefore differs from today's default fighter through familiarity alone | build hash MOVER (new field values); season EQUAL in practice because no fight forms (H-264) [UNVERIFIED: not run] |
| 2 | `Person.techniques: dict` (name → level), seeded at build from the lifepath (Part 4, G-4) | the composer (Part 2) | every learned technique acts at its recorded level, the fixed baseline included (board B-2: all on) | build MOVER |
| 3 | `train` writes `Person.techniques` (Part 4, G-1) | — | growth | season MOVER(behaviour) where a technique `train` fires |
| 4 | `Person.path` (ordered entries) and a second tradition | `train` (which technique comes next); the cross-training threshold | ordering, cross-training | build MOVER |
| 5 | `Person.boards` (up to three saved boards) | the composer; the chooser | preparation (board B-1) | EQUAL until a board differs from "all on" |

- **A conflict in the plan's own direction, and which side yields.** B18.02 says the module takes "numbers per slot, never the name of a skill, technique or tradition" (workplan v12, `valoria_master_workplan_v12_part28_cont2.md:82`); the same item keeps B14.11's four fields, `traditions` among them, and familiarity reads the name at four sites (`combat_systems.py:936,938,990,1002`). **B18.02's rule should win** (it is the ratified plan, and a name crossing the boundary is what it exists to stop): the host computes each party's familiarity (from names today; from PC-21's per-bout input, "familiarity grown in the season", `proposals/2026-11-12-subsystem-audit-suite/dossiers/03_PC.md:163`, later) and the module takes it as a number. That is a module edit at the four read sites, owned by B18.02 or PC-21, not by this proposal (listed as such in the head). Until it lands, step 1's name crosses the door as today's record already allows.
- **What step 1 changes in the module door:** nothing. `traditions` and `techniques` already exist on `PersonalCombatInput` (`inputs.py:203-204`) and `fight.py` already passes them to `Combatant` (`:58-63`, `:182-185`).
- **Where each fact lives (§0.05).** The curriculum, columns, costs, sets, gates and the attention rule are authoring data the host reads, behind an export with a `--check` round-trip if the port needs them (CLAUDE.md §5). The proposal's own copy is `sheets.py`, which is a worked example and not that owner. A person's tradition, levels, path and boards are on `Person`.

**N-line for C-1.** Cut it and the season can never hand a fight a tradition or a technique: every board, set and growth rule in Parts 2–4 stays a module-scale result, as the earlier draft found (`00_tradition_sets.md:131`). **Decision it leaves Jordan:** none of its own (PC-21 owns the carrier); the content of the cast rows' `tradition:` keys is his (plan rule P11). **Lessons:** Troubleshooter keeps per-character state (classes, boards, personal masteries) on the character [FAN/V, Part 6]; Tactics Ogre Reborn moved levels back onto the unit after PSP's class-wide levels drew criticism [V: S4, S5].

**Falsifier for the carrier.** With every cast row's `tradition:` empty, the realm built and run one season is hash-equal to today's. With one row filled, exactly one person's fights change and nobody else's.

## 5.4 The record: how a player can tell why

**The gap.** The fight's trace names each party's tradition at `fight_start` (`wrapper.py:585-586`) and never a technique: no event says that a technique acted, or what it changed. The CombatOutcome lifts the whole trace (`fight.py:218-219`), so whatever the engine emits reaches the host.

**B18.02's own falsifier asks for this.** Its falsifier is "a skill or lever value that changes an outcome without appearing in the record" (scratchpad `b18.md:85`). A board that composes into lever numbers will do exactly that unless the record shows them.

### R-1. Show the numbers at the start (RECOMMENDED first)

- **N-line.** Cut it and B18.02's own falsifier cannot be checked, and a player sees a fight change with no account of why.
- At `fight_start`, emit each party's non-neutral slot values: the lever factors and bonuses that are not 1.0 or 0.0, and any open gate. Numbers only; the module still names no technique.
- The host, which composed the numbers, maps each back to the techniques and sets that produced it, and the sheet or the fight log prints them in plain words.
- **Cost.** One emit. `_emit` "adds no rng draw and no state mutation" (`fight.py:210-211`), so outcomes cannot move. **Hash.** The trace is part of `CombatOutcome`; whether any pinned artifact hashes the trace is [UNVERIFIED]; the build must check the combat goldens and state the result.

### R-2. Say when a technique changed what happened (RECOMMENDED second)

- At a site where the engine draws a yes-or-no against a probability that a lever moved (the counter's reach is one: `rng.random() < … * ability_factor(defender,'counter_select')`, `combat_systems.py:1029`), the site already has the draw *u* and the probability *p*; with the lever at 1.0 the probability would have been *p₀*. **The technique decided the event exactly when one of *u* < *p* and *u* < *p₀* holds and the other does not.** That is pure arithmetic on numbers the site holds; it draws nothing.
- Emit a `technique_decided` event naming the lever, the site and the turn. The host turns it into "your Zwerchhau made you reach for the counter here; without it you would not have".
- At the sites that add a lever to a sigma (bind, measure, read) the same test is whether the degree band would have differed without the lever's term. [UNVERIFIED: that each such site holds the net it banded; to be read at build, site by site.]
- A gate opened by a set emits `gate_opened` (gate, turn) whenever it admits a case the closed gate would refuse.
- **Why this is the right size.** The earlier measurement found the ability layer's effect is per-event with a near-zero aggregate (the record's 19/44/81 of 600 seeds differing at levels 1/3/8, brief §2; ED-PC-0023). An aggregate win rate cannot show a player why; a per-event "this decided that" can.
- **Falsifier.** In paired seeds with and without one technique, every fight whose event sequence differs contains at least one `technique_decided` or `gate_opened` event for that technique before the first divergence. A divergence with no such event means an unreported channel.
- **Cost.** One comparison and one emit per instrumented site; the site list is the fifteen levers' sites (Part 2 §2.3.1) plus the four gates.
- **N-line.** Cut it and the record says what a board *was* but never what it *did*; the per-event nature of the effect stays invisible, which is the reason the ability layer was once read as inert.
- **Build order and hash.** After R-1, one site at a time, starting with the binary sites; each a module edit in `modules/combat/`; outcomes cannot move (no draw is added), the trace does. **Decision it leaves Jordan:** none; it is the record B18.02's falsifier already asks for.
- **Lessons.** Troubleshooter's hover preview of hit and damage before a choice [V: one blogger, `troubleshooter_combat_reception.md:69`] and FFT's shown odds (agency proposal §21 A.3) are previews; this is the after-the-fact account, which a game with no GM and a per-beat engine needs more.
