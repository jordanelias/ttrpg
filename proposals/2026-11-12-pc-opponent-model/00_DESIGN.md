# The opponent model: familiarity, anticipation, visible state, nearness to yielding (PC-21)

## Status: PROPOSED (workplan v12 item B14.28; design only, no code; reference, never mechanism, CLAUDE.md §0.05: each term below names the code that would carry it)

Source: the B14.28 entry (`workplans/valoria_master_workplan_v12_part10_cont.md:501-514`), copying PC-21's REMAINING UNBUILT (read at `git show 11da87e6:workplans/valoria_master_workplan_v11_part17.md`, lines 65-77; the intake `V12_INTAKE.md` at `FORK:698dc907` is not reachable from this shallow clone, and the entry says it copies the same text). Rulings: AR-38 to AR-48, RULED (`proposals/2026-11-05-attribute-rulings-by-subject.md:72-114`, recorded by ED-IN-0347); adjudication §2.2 (viii) (`proposals/2026-11-05-attribute-rulings-adjudication.md:114`); A-112 (combat reads skill scores through the skill table, `unified/DECISIONS_ANSWERED.md:148` of the suite); D-18 (a design item stops for Jordan only on what the ladder cannot settle).

**What the tree holds today (opened):**
- `modules/combat/traditions.py::familiarity(reader_trad, opponent_trad)`: 1.0 when the two match or either is `'none'`, else `FAMILIARITY_ADJACENT` 0.93 or `FAMILIARITY_DEFAULT` 0.85. Four call sites in `modules/combat/combat_systems.py`: `bind_sigma`'s two tactile reads (:935, :937), `commit_depth`'s `wary` (:989) and `read_contest`'s `fam` (:1001).
- `combat_systems.py::read_contest`: on a missed read, `mode = modes[rng.randrange(3)]` (:1015) over `vocabulary.py::DEFENCE_MODES`, an ordered tuple whose order is part of the draw contract (`vocabulary.py:65-71`). After B06 this reads `modes[rng.below(3)]`. `wrapper.py` only calls `S.read_contest`.
- The season passes no tradition and no disposition. `fight.py:182-185` fills `tradition` and `disp` only from `PersonalCombatInput.traditions` and `.dispositions`, which the workbench sets and `seam/wrappers/combat.py::combat_input` never does; `disp` has no registry key (`attributes.py:52`), so `_attr_kw` cannot carry it either (`fight.py:71-72`). Every season fighter is tradition `'none'` and `disp` 4.
- The season gives every fighter the same kit: `world_q.py::kit_of` returns the Combatant default while `rosters.yaml: arms_kinds` ships empty (`world_q.py:3404-3406`).
- `engine/season/queries/world_q.py::practice` is the shape precedent: a whole-number addend derived from `w.log` (acts counted by id through `causing_act`, over the closed window `[w.tick - practice_window, w.tick - 1]`, `// practice_step`, capped at `practice_cap`), storing nothing; `practice_cap` 0 returns 0 before the log is read.
- Attunement is `attr.social.attunement` (`references/descriptor_registry.yaml:56`). It is not in `modules/combat/attributes.py::SPEC` (`att` is `attr.mind.perception`, PC-14), and no Combatant field carries it. Under `cast_attributes=True` every person draws it uniformly on 1 to 6 (`state/carriers.py::generated_attributes`), and `combat_input` passes every person's attributes (`seam/wrappers/combat.py:307-309`).

---

## (1) Familiarity as a per-bout input set by the seam

**Copied:** "familiarity as a per-bout input set by the seam (AR-47, AR-48), derived from the holder's own past fights against that weapon class (`wclass`) and his tradition's skills, storing nothing (adj §2.2 (viii)); the label function stays the module default for un-seamed callers; where a person's tradition lives (no `Person` carrier exists; CR-33's keys are the candidate)."

**Answer.**
- **The season side.** `world_q.familiarity_level(w, p, key) -> int` takes `practice`'s shape and reuses its `practice_window` and `practice_step`. It counts the distinct scene acts in which `p` was a party and faced an opponent under `key`, and returns `min(familiarity_cap, n // practice_step)`. One new fixture, `familiarity_cap`, gets its own H row; its value 0 is the control, returning 0 before anything is read.
- **The key** is `(opponent's tradition bundle, opponent's wclass)`. `wclass` is `weapon_physics.py`'s three classes (`bladed`, `hafted_tip`, `hafted_block`), the existing classification (adj §2.2 (viii)), read from the module's data and never copied: the build adds `wclass` per weapon to the `kit` section of `combat_engine_v1.json` (through `tools/export_engine_params.py` and its `--check`), and `engine/substrate/combat_kit.py`, that section's one runtime reader, gets a `WCLASS` map.
- **What a scene leaves in the log.** No Event names the opponent's weapon except `fell_to` on a felling (`loop/effects_combat.py::fell_observed`, B14.03). The build adds **a new Observation per party per scene, written for this reader**, naming the key that party faced. Adj (viii)'s "stores nothing" is read as *no carrier field; the log is the record*, which is ladder 4: `fell_observed` and `broke_observed` already deposit a scene fact on `Event.observed` this way. The rejected alternative, reading the opponent's current `kit_of`, gives a past fight the wrong class once stores change. The deposit happens only when `familiarity_cap > 0`, since a non-empty `observed` is folded into `World.content_hash`.
- **Where a person's tradition lives.** As skill-table rows he holds; he carries no tradition label. AR-43a RULED makes a martial tradition a bundle of skills; A-98 and A-112 put skills in the skill table; CR-33 expands a lifepath into keys "stored NOWHERE on the `Person`" (`engine/season/rosters.yaml:3500-3502`). No bundle row exists, so the bundle half of the key reads `none` for everyone until one is authored (CONTENT, D-19).
- **As shipped, the key is one value.** With `arms_kinds` empty and no bundle rows, every opponent is `(none, bladed)`, so `familiarity_level` is a count of scenes fought. That overlaps `practice`, which already adds pool dice to `fight` (capability `arms`, `verb_table.yaml:746-748`) on a different count: the actor's own acts at Success or better. **The split is named (NERS S) and kept, with a condition.** The two count different things: `practice` what he did well, so it reads his band, and a fight's `degree` is the actor's band; familiarity what he has faced, which has no band and teaches both parties, the felled one included (ladder 5). Window and step are shared, so the counting method is one. While the key is constant the two quantities nearly coincide, so two ladders would reward the same thing: **`familiarity_cap` is not flipped until a key varies** (an `arms_kinds` row, or a bundle row). Adj (viii) asks which lands first: the weapon does, since its carrier and reader (`kit_of`) are built and only the rows are missing.
- **The seam to the module.** `combat_input` passes `PersonalCombatInput.familiarity = (level_a, level_b)`: each party's level against the other party's key, whole numbers, as `scores` and `addends` are passed. At cap 0 the field is absent and keeps its default `()`. `fight.py::fight` sets each Combatant's `familiar` instance attribute, as it sets `carried` and `pool_addends` (B05.61).
- **The module side.** One owner, `traditions.familiarity_of(reader, opponent, cfg)`, which all four call sites use. With `reader.familiar` absent it returns the label function unchanged, so the workbench is unaffected; otherwise `familiarity(label) * (1 + CFG['FAMILIARITY_LEVEL_K'] * level)`. At level 0 the multiplier is exactly 1.0.
- **A record raises the read; no record is today's read.** Ladder 4: PC-18 (2) (`AGI_READ_K*(agi-NEUTRAL)`, "a default aggressor reads as before") and `disp_lean`'s centring; the EXIT's "equally at no record" says the same. Above 1.0, `commit_depth`'s `wary = WARINESS_K*(1-fam)` would go negative; the build clamps it at 0, which keeps the code's comment ("`>=0`, biases shallow") true.

**FALSIFIER.** *Module:* call `read_contest` twice with identical arguments and an identically seeded rng, the defender's `familiar` at L > 0 and then 0: `p_read` is strictly higher at L. With `familiar` 0 and with it absent, `p_read`, `mode` and the rng's state after the call are equal to the bit. *Season, through the seam:* in a test world whose `arms_kinds` gives opponents two classes X and Y, a person with one scene against X inside the window, at step 1, has level 1 against X and 0 against Y; a scene resolved earlier this tick counts 0. `combat_input` for him then passes 1 against an X opponent and 0 against a Y opponent, so he reads X better than a fighter with no record and Y exactly as one. Module half in `tests/valoria/test_combat_opponent_model.py`, season half in `engine/season/tests/`.
**CONTROL.** `familiarity_cap` 0: the input is absent, nothing is deposited, the label function is read, and the realm hash at s = 0, 1, 2 equals the base. `FAMILIARITY_LEVEL_K` 0: the multiplier is 1.0 exactly, and the combat goldens (`tests/valoria/r3_identity_golden.json`, `tests/valoria/test_combat_audit_pins.py`, `tools/ci_golden_modes_check.py`) equal the base.

---

## (2) Anticipation on a missed read

**Copied:** "the anticipation on a missed read, combining familiarity, the defender's Attunement and the opponent's visible state, and its effect on the draw order (the `modes[rng.randrange(3)]` contract)."

**In the season it cannot fire.** What a defender could anticipate is the opponent's skew of depth, `g = COMMIT_BETA_K*(DISP_COMMIT_K*ln - wary)` (`combat_systems.py:990`). In the season `ln` is 0 (`disp` 4, see above) and `wary` is 0 (every tradition `'none'`, `traditions.py:44`; (1) clamps it at 0 from below), so `g` is 0 in every season fight and there is nothing to read.

**Cut test (NERS).** Built now, (2) would cost a `SPEC` row, a `commit_params` refactor, a new kind of draw and a dial, and move no realm hash. Cutting it loses nothing in the game, so its N-line is false today and E fails as a ratio. **Verdict: cut from the build.** What dies: the B15 build of the `attun` row, `commit_params`, the weighted draw and `ANTICIPATE_K`. Attunement still reads nothing in the season after B15, and AR-38/AR-41 stay unmet in combat. **(2) lands with the first item that gives the season a source of `g`**: a disposition carrier that `combat_input` passes (a registry key for `disp`, or a filled `dispositions`), or a tradition label that `familiarity` compares. That item owns the carrier's design; this one does not.

**The shape it lands in** (so that item builds no second one):
- **Carrier.** One `attributes.SPEC` row, `AttributeSpec('attun', 3, 3, 'attr.social.attunement', IN_FLUX)`, carried by `_attr_kw` with no new path. Centred on neutral 3, as in (1): a default fighter anticipates nothing, and below neutral the guess is uniform, the floor of guessing without information.
- **What is anticipated** is depth, since depth is what moves the defender's best mode. `commit_params(aggressor, defender, cfg, TR) -> (ba, bb, span, g)` is factored out of `commit_depth`, and both call it (one owner). The anticipated mode is `argmax_m mode_sigma(m, ..., commit_hat, False, fat_d, cfg)` at `commit_hat = 2 + span*ba/(ba+bb)`, the Beta's mean; never at the actual commit, which would be a read.
- **Weight.** `w = min(1, ANTICIPATE_K * max(0, attun - 3)/3 * fam_d * min(1, |g|))`, `fam_d` being (1)'s `familiarity_of(defender, aggressor)`. The `|g|` gate is deliberate: at `g` = 0 the argmax at the unskewed mean is only the defender's own best mode, which is not a read of the opponent (AR-39).
- **Draw order.** At `w == 0` the existing `modes[rng.randrange(3)]` (after B06, `rng.below(3)`) runs unchanged and the stream is byte-identical. At `w > 0` one uniform `u` is drawn in the same position, on a missed read only: `u < w` takes the anticipated mode, else `modes[min(2, int(3*(u-w)/(1-w)))]`. Still one draw per missed read; only its kind changes, and only where `w > 0`. `DEFENCE_MODES`' order stays part of the contract.

**FALSIFIER** (the landing item's). Both parties tradition `'none'`, so `wary` is 0 and `g` is the disposition's alone. A defender whose parry and dodge `mode_sigma` at the unskewed commit `2 + span/2` lie within the commit ramps' reach (`combat_systems.py:331-334`), so that depth can change his argmax; the test asserts the argmax at `commit_hat` differs from that at the unskewed commit for `disp` 7 or 1, or it observes nothing. Over N seeded missed reads, three arms on the same stream: (a) uniform; (b) the same `w`, but the argmax taken at the unskewed commit; (c) the anticipation. Against `disp` 7 and against `disp` 1, the mean `msig[chosen]` at the actual commit is strictly higher in (c) than in (b). (b) beating (a) shows only that a defender's own best mode is good; if (c) does not beat (b), anticipation adds nothing over it and (2) is cut outright. Against `disp` 4, (c) equals (a) draw for draw; that arm checks the gate, not a measurement. A loop asserts `checked >= N` (CLAUDE.md §0.1 pt 2).
**CONTROL.** `ANTICIPATE_K` 0, or `attun` at or below 3: `w` = 0, the existing branch runs, and the combat goldens and realm hash equal the base.

---

## (3) The opponent's state, composed from what the module tracks

**Copied:** "the opponent's state composed from what the module already tracks (fatigue, wounds, poise, initiative, `disp`) before any new quantity is coined (AR-38)."

**Answer.** No new quantity is coined. The opponent's choice of depth reads `disp_lean`, `wary` (his own familiarity with the defender) and `range_avail` (`combat_systems.py:988-992`): the first two make `g`, and `range_avail` sets `span`, which moves `commit_hat` and not `w`. The opponent's fatigue (`1 - stamina/stamina_max`, `wrapper.py:288`), wounds (`wt.health_remaining/health_full`), `poise` and `initiative` (`combatant.py:148-149`) are tracked but enter no part of his choice of depth, so anticipating depth would gain nothing by reading them. The defender's own fatigue and poise do enter his choice of mode on a won read, through `balance_eff` in the dodge row (:178, :326); (2)'s anticipated mode is `mode_sigma`'s argmax, so it reads them there and needs no second path. AR-38's other half (RULED), that emotional state colours what a combatant does, means putting one of these into `commit_params`: a change to what the opponent chooses, not to what is read, and not built here. Because the anticipation reads `commit_params` and nothing else, such a change would be anticipated with no second edit.

**FALSIFIER** (binding on (2)'s build). At fixed `disp`, varying the opponent's fatigue, poise, wounds and initiative leaves `commit_params` and the anticipated `(mode, w)` unchanged; varying `disp` moves both. A test that stubs `commit_params` sees the anticipation move with the stub; if the anticipation computes its own depth, the test fails, since there would be two ways of computing one quantity.
**CONTROL.** `git diff` of `modules/combat/combatant.py` shows no new `self.` state assignment, and the base hash is equal under (2)'s control.

---

## (4) Nearness to yielding, against PC-10a's threshold

**Copied:** "nearness to yielding read against PC-10a's threshold, and its consumer, or the statement that it has none yet (AR-42)."

**Answer.** **It has no consumer yet, so nothing is built.** The threshold is `wrapper.py::_terms_crossed`: under `'yield'`, `health_remaining <= YIELD_HEALTH_FRAC*health_full`; under `'blood'`, `wounds >= 1`; under `'death'`, none. The read would be the margin to that threshold, with `_terms_crossed` rewritten as `margin <= 0` so the two cannot drift apart. Nothing would read it:
- The AUTOMATED loop engages every turn (`wrapper.py::TURN_CHOICES` is `{engage, withdraw}`, and `decide=None` means engage).
- The only decider is a played person's `host.decide` (`seam/wrappers/combat.py:508`), which already receives each party's exact `wound_state` through `queries/inputs.py::CombatTurnView`.

The consumer arrives with whichever comes first: an AUTOMATED decider that can withdraw or yield (M-4; J-15 decides whether `yield` joins `TURN_CHOICES`), or a `CombatTurnView` that shows Attunement's estimate in place of exact health. That build declares its own hash.

**FALSIFIER.** Run `rg -n "_terms_crossed|health_remaining" modules/combat engine/season -g '!**/tests/**'`. A printed site that chooses an in-bout action from the opponent's condition makes "no consumer" false. On this tree it prints only `_terms_crossed` and its two callers (`_terms_met`, `_terms_yielder`), the after-scene harm read (`loop/effects_combat.py::_marks`), and declarations and comments; none is a choice.
**CONTROL.** Nothing is built, so nothing moves.

---

## Where the build lands, and what it moves

(1) lands in **B15-pc-calibration** (`workplans/valoria_master_workplan_v12_part18.md:15`), the next batch whose census names both `modules/combat/` and `seam/wrappers/combat.py`; IS-PC-05 already edits `attributes.py` there. Its dials ship at control (`familiarity_cap` 0, `FAMILIARITY_LEVEL_K` 0), listed under that batch's `DIALS AT CONTROL`, and move no hash. Each flip is declared alone:
- `familiarity_cap` is flipped only once a key varies ((1), "As shipped"). The flip moves the realm hash (the deposit, plus reads for anyone with a record) and no combat golden, the workbench being un-seamed.
- (2) does not land in B15. It lands with the item that gives the season a source of `g`; its flip then moves the realm hash wherever a person with `attun` above 3 (about half the population, drawn on 1 to 6) misses a read against an opponent with `g` ≠ 0, and moves the combat goldens only where a workbench fighter is given `attun` above 3. Before then, a flip would move nothing in the season, which is why it waits.
- (3) adds nothing; (4) builds nothing.

Glossary rows (*familiarity level*, *anticipation*) are added when each build lands.

## Needs Jordan

None. Every choice was settled by the ladder:
- Tradition as skill rows: AR-43a, A-98 and the CR-33 precedent.
- A record raises the read, and no record is today's read: PC-18 (2) and `disp_lean`'s centring, and the EXIT.
- Every scene counts, for both parties, beside `practice`'s actor-only count: ladder 5, the quantities differ; the flip waits for a varying key so the two never reward one thing.
- The class is recorded at the scene as a new Observation: the `fell_to`/`broke` precedent.
- (2) waits for a source of `g`: the NERS cut test (ladder 5).
- Attunement centred on neutral; the state read is `commit_params` only (AR-38, "before any new quantity").
- Nearness to yielding: no consumer.

The tradition-bundle and `arms_kinds` rows are CONTENT for Jordan's authoring (D-19), not a decision; the season disposition carrier belongs to the item that builds it.
