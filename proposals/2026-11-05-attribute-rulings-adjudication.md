# Jordan's attribute rulings of 2026-11-05, adjudicated against the tree and reconciled

## Status: PROPOSED (2026-11-05). An adjudication: each ruling read against the code at the file and line opened for it, the earlier rows and plan positions the rulings displace, the ladder's answer to every open question, and a build sequence. Reference under CLAUDE.md §0.05; merging ratifies nothing and decides nothing. Every ladder take is marked `[ASSUMPTION; medium; Jordan to correct; revert: …]` and reverts alone.
## Lane: IN
## Reads: `proposals/2026-11-05-attribute-rulings-by-subject.md` (AR-01 to AR-58, ED-IN-0347) · `proposals/2026-11-05-verb-attribute-map.md` (F1 to F27) and `_part2` · the plan that folds it: `workplans/valoria_master_workplan_v11_part17.md` (`-12`), with its amendments, its batch B10-11b and its handle rows (ED-IN-0348)

**Priority.** The rulings of 2026-11-05 govern every earlier reading where they disagree (AR-07; ED-IN-0347). Inside the set, the last statement governs a chain (by-subject §0). AR-27 and AR-28 are superseded by AR-29 and are not adjudicated; AR-56 to AR-58 (health) are PROVISIONAL by Jordan's own words and are recorded, not adjudicated (§3.3). AR-01 to AR-03 and AR-07 are directions with no code question.

**Method.** Every file:line below was opened on this branch (`ccr-af6cebc0-o9fvpp`, 2026-11-05). The map's claims were re-checked at their cited lines; §1.1 lists the ones that are wrong or incomplete. "SILENT" is a claim of absence; its falsifier is the grep or read named in the row.

## 1. Conformance

Verdicts: **C** conforms · **P** partly conforms · **X** contradicts · **S** silent (nothing in the tree implements or opposes it).

| AR | verdict | the code, opened | note |
|---|---|---|---|
| 04 | P | `decision/choose.py:171-195` (`score_terms`: `pursuit + stance`; `odds_weight` at :195); `seam/wrappers/sigma.py:146-160` (`faculty`, the believer's own pool); `state/carriers.py:716-750` (`Person`: `capability`, `pursuits`, `stance`, no attribute field) | Capability already weights a contested candidate through believed odds (CR-17). No attribute exists to weight anything, and an uncontested candidate has no capability term. Obligations and demands have no term (CR-88's design). |
| 05 | P | `references/descriptor_registry.yaml:34-35` (`scale: "1-7"`, `default: 1`); `modules/combat/combatant.py:93` (`Combatant(...)` takes any number); `seam/wrappers/combat.py:130-138` (`party_end` floors `end` at 1) | The floor is the registry's and the seam holds it for the one field it passes; CR-20's carrier refuses outside 1 to 7 (planned). The module is not a holder of the scale (PC-14 item 1: "No names, aliases, floors or ceilings"). |
| 06 | C | `modules/combat/weapon_physics.py:9` (`mass(kg)` a per-weapon primitive) | One word, one quantity. |
| 10 | P | damage: `modules/combat/core.py:560-571` (`strike_impact = strength + heft`, the same Strength for every head), `combat_systems.py:1239` (only the blunt branch scales its load by `PERC_STR_K·strength`); push and force: `combat_systems.py:1062` (`BIND_STR_K`), `:349` (`WIND_K` on `strn − aggressor.strength`), `contact.py:46` (`GRAB_STR_K`); leverage: `combat_systems.py:842-848` (pure geometry); armour: no Strength or burden term against armour (grep of `combat_systems.py` for armour with stamina, tempo, demand, weight or burden: none; armour reaches only reach `REACH_W` and armour-defeat `ADEF_*`, `config.py:19, 81, 97`) | Damage by weapon type: partial (blunt only). Pushing: built. Leverage: built through the bind's Strength term (§2.4 take). Armour: absent. |
| 11 | C | `combatant.py:40-42` (`health_full = WI·(maxW+1) + STR_HEALTH_W·strength·end`) | Strength adds to health at every Endurance ≥ 1 (AR-05 makes Endurance never 0). The product form is a weight question for the provisional health design, not a contradiction. |
| 12 | P | `combat_systems.py:175-180` (`str_demand`; `handling_penalty = HANDLE_K·max(0, str_demand − strength) + …`) | Heft is managed (a shortfall penalty); weight itself enters only through `wield_heft`'s inertia; surplus Strength buys nothing. |
| 13 | P | `combat_systems.py:184-188` (`balance_eff = ½agi + ½strength − 1 + skill`), `:1151` (`overcommit_exposure`), `:1062` (`BIND_STR_K`) | Own weapon's momentum: Strength only through balance. Another's: only the bind's difference term. |
| 14 | C | `weapon_physics.py:9` | Weapons have mass. |
| 15 | P | `combat_systems.py:172` (`reflex`, agi with att), `:184-188` (balance), `:113` (`AGI_TEMPO_K`), `:839` (footwork) | Footing, dodging and manoeuvre read `agi`. Accuracy does not (AR-18 row). |
| 16 | S | `loop/effects_information.py:777` (`_eff_forge`, the one writer of `Record.forgery_quality`) carries `Fixtures.default_forgery_quality` (`data/fixtures.py:499`, H-210), not the forger; no lock, theft or burglary verb in `verb_table.yaml` (grep for `pick`, `lock`, `steal`, `burgl`, `theft` row keys: none) | Forgery quality is a constant today; lock-picking has no verb. |
| 17 | P | `combat_systems.py:1128-1131` (`read_contest`: tradition `eff_cw`, `fam`, `legibility`) | HEDGED. Skill and tradition inform how well an attack is read, as he guessed; no Coordination term. |
| 18 | X | `combat_systems.py:1131` (`read_a = reading(aggressor)·eff_cw(aggressor,'visual') + consistency_a`); `:915` (`legibility`: mode, commit, lunge, ornament, edges, choke, room; no attribute) | The aggressor's side of the read is his own `reading` (two parts `cog`, one `att`): his perception disguises his attack. The ruling puts the attack's suddenness and dexterity on Coordination. |
| 19 | P | `combat_systems.py:329-332` (`mode_sigma`: `rd` scaled by `read_win`, then `reflex` and technique); `:1427-1431` (`mental_fatigue`), `wrapper.py:279-280` (`consistency_a` on the aggressor's read) | Read then response is staged; Focus enters the read and never the response. |
| 20 | C | `combatant.py:45-47` (`stamina_max = 3·End + 2·Spirit`); `wrapper.py:584` (recovery scaled by `stamina_max`); `combat_systems.py:1427-1431` (fatigue degrades the read, Focus's reserve protects it); `combatant.py:29-43` (health) | Stamina, breath, tiring into concentration and health are all built, Endurance-led. |
| 21 | S | `choose.py:171-195` (no per-person forecast term); `sigma.py:368-419` (`odds_of`, exact from the believer's own pool and ledger, no error term) | Nothing in the season reads Reason. Combat's one `cog` read (`combat_systems.py:171`) is displaced by AR-40, not supported by AR-21. |
| 22 | P | `combat_systems.py:1423-1425` (`consistency` from the reserve `3F+2S`); `wrapper.py:194, 226, 395, 420` (`CONC_DRAIN_HIT` per hit) | Pain drains the reserve per hit. No source of inattention (the module fights one against one: `wrapper.py:533`, `fight(A, B, …)`). |
| 23 | S | `choose.py:352` (`tau = float(fx.get("choice_temperature"))`, one value for every person) | |
| 24, 25, 26, 26a | S | `epistemic.py:794` (`observers_for`), `loop/witness.py:488-524` (the governor deposit of a larder's `shortfall:<kind>`); `grep -c "perception\|attributes"` on both files: 0 | Everyone admitted by a channel learns the same thing at the same confidence. |
| 37 | P | `combat_systems.py:171-172` (`att` read in `reading` and `reflex`) | Combat reads `att`, which these rulings make Perception, but mixed two-to-one with `cog`. |
| 40 | X | `combat_systems.py:171` (`reading = (2·cog + att)/3 + READ_HISTORY_K·(history − 3)`) | Two parts Reason, one Perception, plus history. |
| 29 | P | `descriptor_registry.yaml:45` (Charisma, alias Presence); `modules/mass_battle/core/exchange.py:57-61` (`derive_command(charisma, cognition)`), called at `hierarchy/units.py:2768, 2862` | Presence exists under its old name in mass battle's Officer command; no season reader. |
| 30 | S | `decision/options.py` `refracted_confidence` factor 1 (CR-19 unbuilt); no person-side estimate of another's pursuits (CR-83 design-first) | Planned, consistent with ED-IN-0326. |
| 31 | X | `systems/fieldwork/sim/knots.py:53` (`KNOT_BONDS_MIN`), `:200` (`knot_max = bonds_a // 2 + 1`); `grep -rn bonds engine/season` (non-test): none | The oracle gates knots on Bonds, which the ten drop; the season reads neither. |
| 38, 41, 42 | S | `combat_systems.py:1136` (a missed read guesses `modes[rng.randrange(3)]`, uniform); `:1115, :1149`, `wrapper.py:135-136` (`disp_lean` read only for the fighter's own choices) | No opponent model, no emotional state, no in-bout reading of nearness to yielding. |
| 39 | C | `combat_systems.py:171` (no Attunement read in `reading`) | Vacuously: Attunement does not read attacks. |
| 32, 33, 36, 36a | S | `descriptor_registry.yaml:36-47` (no Grace key); `modules/social_contest/roll.py:89-130` (`obstacle`: no style, register or decorum term); `engine/season/arrangements.yaml` (keys `interposed`, `order`, `floor`, `venue_min_rank`; no Grace requirement) | |
| 34 | P | `queries/person_q.py:397-422` (`regard = stance + judged_gain·judged + told_valence_gain·told`); `queries/world_q.py:678` (`reception`) | Regard reads no office rank, so "despite their standing" already holds; the Grace term is missing. |
| 35 | P | `choose.py:55` (`stance_term`, which under `declared` adds the chooser's regard of the candidate's subject) | A conferrer already favours whom he regards; Grace does not reach regard. |
| 44 | P | harm and strain: `combatant.py:20, 34-37, 45-47, 147` (`SPI_WI_W`, `STAMINA_PER_SPIRIT`, `CONC_SPIRIT`); resisting influence: `sigma.py:163-176` (`_opposition_of` reads the party's key for the same verb); circumstance modifiers: `roll.py:89-130` (room terms subtracted from the obstacle), `combat_systems.py:1044` (`WOUND_DEF_OB·defender.wounds − WOUND_ATK_OB·aggressor.wounds`, ED-1041) | Strain tolerance built in combat; resistance and modifiers silent. |
| 49, 50 | S | follows from 29, 32-35 | Each profile needs Presence on the roll and Grace on regard; neither exists. |
| 43 | X | `modules/combat/traditions.py:30-56` (`familiarity` returns 1.0, 0.93 or 0.85 by two tradition labels) | HEDGED ("I think"); AR-46 governs. |
| 43a | C | `traditions.py:1-11` (a tradition is "a bundle of ABILITY primitives") | |
| 45, 46 | X | `traditions.py:47-56`; read at `combat_systems.py:1128` (the visual read) and `:1057, :1059` (both sides' tactile bind read) | Keyed to two labels, the same for every fighter and every bout; no weapon term. |
| 47 | C | `traditions.py:47` is a pure function; `Combatant` keeps no cross-bout state | Constant at use, as ruled. |
| 48 | P | `seam/wrappers/combat.py:36-41, 130-138` (the one derived field is `end`, from `Person.body`; every other field is the class default) | The pattern is right for `end` and absent for everything else. |
| 51, 52 | S | `choose.py:171-195` (an `accept` is scored as any contested candidate); `-04` PC-10, CR-87 (the challenge Record and its stakes, unbuilt) | Nothing reads the acceptor's station or whether a fight settles the issue. |
| 53 | P | `wrapper.py:508` (`DUEL_TERMS`), `:533` (`fight(..., terms=LETHAL_TERMS)`); `-04` CR-87 item (1) (`violence_contexts`: war, crime, duel, defence; unbuilt) | Terms exist in the module; occasions at formation are planned. |

**Counts (48 adjudicated): 7 conform, 16 partly conform, 6 contradict, 19 silent.** Not adjudicated: AR-01, 02, 03, 07 (direction), AR-27, 28 (superseded), AR-56, 57, 58 (provisional).

### 1.1 The map's claims, corrected

1. **F8: "the change moves nearly every combat outcome and every golden." Wrong for the season.** At the class defaults `cog = att = 3` (`combatant.py:93`), `(2·3 + 3)/3 = 3.0 = att`, and the history term is `K·(3 − 3) = 0`. The season builds every fighter at the defaults except `end` (`seam/wrappers/combat.py:36-41`), so making `reading` Perception alone leaves every season fight byte-identical; it moves only fights with `cog ≠ att` (the workbench and the combat test pins). The aggressor-side Coordination term (AR-18) is likewise identity at `agi = 4` if centred there. Falsifier: `build_realm(0).content_hash()` before and after (PC-18's control).
2. **F8 and F23: familiarity scales "the defender's read (`read_contest`, `:1127`)".** It is at `:1128`, and it also scales both sides' tactile read in the bind (`combat_systems.py:1057, 1059`). A familiarity change moves the bind as well as the visual read.
3. **F8: `reading`'s 16 call sites are "the read contest, the defence sigma, initiative, approach displacement".** The count is right (16 calls on 13 lines, opened); the list omits the bind's tactile reads (`:1057, :1059`) and the tempo term (`:1342-1343`).
4. **F25: "I have the comment, not the run" for `v33-mstr-impact`.** The record is `ED-1040` (`registers/editorial_ledger.jsonl`, 2026-06-19, resolved): multiplicative Strength (`(STR_REF+heft)·(strength/STR_REF)^STR_EXP`) stalled low-Strength heavy-weapon fights (str 2 greatsword mirror, 42% draws against 7%). The same row's CORRECTION says the "~50% draw stall" reported across that session's sims were artifacts of a harness misreading `fight()`'s −1/0/+1 return. The row does not say whether the 42% figure was taken with the corrected harness, so the evidence against a multiplicative form is not established either way. It does not matter for AR-10: the minimal form (§2.1) keeps the term additive.
5. **F4: the knot cap at `knots.py:201`.** It is `:200`.
6. **The `march` row (§3, "CODE") and F12's "only `march` and mass battle's in-battle orders draw (Presence 2 : Reason 1)".** `derive_command` is live (`hierarchy/units.py:2768, 2862`), but `modules/mass_battle/config.py:534-535` records Jordan's 2026-07-08 directive to "abandon combat pools being related to the commander". Whether Command still reaches a draw was not traced here; the CODE grade on `march` is unverified, not shown wrong.
7. **F21(d): "the obstacle is `score/2` plus the instance modifiers, … the room's terms and a document's forgery quality".** Correct (`roll.py:93-97`). Add the combat instance (item 5 of §2.2): the wound modifier `combat_systems.py:1044` is the combat counterpart Spirit can act on.

## 2. Reconciliation

### 2.1 What the rulings displace, and the minimal edit to each

| displaced or narrowed | by | minimal reconciling edit | where |
|---|---|---|---|
| `reading = (2·cog + att)/3 + history` (`combat_systems.py:171`; Jordan 2026-06-03 per its comment) | AR-40 | `reading(c)` returns Perception (`att`) alone; the history term leaves `reading` here if CR-85's build has not already removed it. All 16 calls follow the one function. | PC-18 (1); CR-85 unchanged (its design is B10-10's) |
| `read_a`'s aggressor `reading` (`:1131`) | AR-18 | the aggressor's term becomes a Coordination term, neutral at `agi` 4, coefficient swept | PC-18 (2) |
| `cog`'s only combat read | AR-40, AR-02 | Reason has no combat read (niche, accepted); `cog` leaves `Combatant` as an input nothing reads | PC-18 (1) |
| PC-14's ASKS: "`att` is NOT mapped … Attunement or a separate Attention stays open" | AR-37, AR-40 | `att` → `attr.mind.perception` | PC-14 amended |
| Constant `familiarity(trad, trad)` (`traditions.py:47`) | AR-45 to AR-48 | the value becomes a per-bout input set by the seam from the season, keyed to the reader's tradition skills and the opposing weapon class; the label function stays as the module's default for un-seamed callers (the control) | PC-21 (design) |
| ED-IN-0333 item (3) and CR-84 decision (3): Grace "composure … remaining calm" | AR-44 (later) | Composure stays Grace's alias (a name); being unmoved under pressure is Spirit's. Grace keeps how a person is seen (AR-33). No registry change beyond CR-84's. | §2.2 (iv) |
| CR-84 decision (1): the knot oracle "left, and said so" on `bonds` | AR-31 | the successor reader of the knot gate is Attunement; the oracle is changed only by the position that next edits it, and CR-92's design names the term for the season's `tie / knot` | IN-32 amended (note); CR-84 unchanged (B10-10) |
| ED-IN-0261's ruled sentence "two people with identical pursuits ARE identically disposed and the variation comes from the candidates" (quoted in `-04` CL-PERSON) | AR-04 | Narrowed, not reversed: values still dispose identically; capability and attributes now weight the choice too. CR-17's believed odds already did this for contested candidates. The E-4 hold on CL-PERSON is about stored offsets on value axes, which an attribute term is not, so it does not hold this term. | CR-93 (design) |
| ED-IN-0326's two readers (Attunement: persons; Reason: offices, regimes, obligations) | AR-24 to AR-26a | Extended to three: Perception reads worldly facts. ED-IN-0326 is not displaced. | CR-83 amended; CR-19 unchanged (B10-10: it builds Attunement at gain 0, and the split by kind of claim is CR-83's design, before the flip) |
| ED-IN-0328 / ED-IN-0333: Bonds dropped; Grace primary, Composure alias; keys stable | AR-01, AR-31, AR-32 to AR-36a | Confirmed as CR-84 builds it. No alias is needed: PC-14 maps `att` to the key `attr.mind.perception` directly. | CR-84 unchanged |
| ED-IN-0330: histories eliminated | AR-40, AR-43a | Confirmed. History leaves `reading` entirely (AR-40 says "pure"): PC-18 (1) does it if CR-85's build has not. Its pool and Ob jobs stay CR-85's design choice; AR-43a (traditions are skill bundles, which `Combatant.equipped` and `skills` already carry) is an input its author may read, not an edit to B10-10's position | CR-85 unchanged; PC-18 |
| ED-IN-0251 (convictions: what a person holds) | AR-44 | Not displaced: "stay true to yourself" is Spirit resisting a change to what ED-IN-0251's convictions and the pursuits hold; Spirit is the opposing attribute against influence | CR-96 (`opposed_by`), CR-95 |
| ED-IN-0301's "nine keys; the pending slot refuses" | ED-IN-0328 | Already superseded (CR-84, CR-20's own text); nothing further | — |
| `descriptor_registry.yaml:26-29` comments ("Spirit folds to Will", "Perception folds to Attunement") | ED-IN-0328, AR-24 to AR-26 | CR-84's rewrite removes both | CR-84 (as written) |
| `forgery_quality` a fixture (`fixtures.py:499`) | AR-16 | the forger's Coordination, through the Ob-from-score precedent | CR-94 |
| `str_demand` without weight; no armour burden; one Strength coefficient for every head; momentum arrest only through balance | AR-10, AR-12, AR-13 | four swept terms at their existing owners, each zero or one as its control | PC-20 |
| Focus absent from the response (`mode_sigma`) | AR-19 | a lapse term reading the defender's existing reserve (`consistency`) | PC-19 |
| CR-87 (2): "`accept` and `challenge` keep theirs" | AR-51 | `accept` takes `fight`'s cost on every axis (accepting is fighting); `challenge` keeps its own (proposing is cheap) | CR-87 amended |
| CR-88 (duty of office) silent on duels | AR-52 | its design prices `accept` for an office holder by duty | CR-88 amended |
| `_opposition_of` reads the party's key for the same verb (`sigma.py:163`) | AR-44 | the opposing attribute becomes a column of the `vocation_attribute` rows CR-20 lands, defaulting to the row's own attribute; a follow-on after B10-10, not an edit to CR-20 | CR-96 (B10-13); CR-20 unchanged |
| PC-06's K-1 ("a `Combatant` built from the person"), HELD in B10-Z on K-2 (`Person.attributes`); PC-14 item (8): "the host passes attributes when K-1/K-5 lands" | AR-48 | CR-20 is K-2, so its landing releases K-1 (R8): the seam sets each `Combatant` field from `Person.attributes` by PC-14's `registry_key` map, absent keys at the class default. Without it every combat ruling above is inert in the season, which builds every fighter at the defaults but `end`. K-5 (loadout as `hold` tenures) stays held: CP-T03-03 carries kit. | PC-06 amended; K-1 slots first in B10-11b |
| The registry header: Godot bar and IN FLUX | — | unchanged: the rulings are RULED on meaning, but ED-IN-0328's roster is still hedged ("I think") | — |

Not displaced, checked: CR-33 (lifepath templates: keys only; AR-43a's bundles are combat's, PC-21 says where a martial lifepath's tradition lands), CL-ATTR (M24's composition is untouched by AR-48), CL-SLICE (its build reads M23 and M24; M23 is answered), ED-IN-0261's fifteen pursuits and seven axes, `world_q.practice` (the precedent PC-21 and CR-94 compose on), `arrangements.yaml` (read by CR-92, no fourteenth key).

### 2.2 Tensions, resolved

**(i) AR-04 against "capability supplies dice and gates nothing" (#353 §9.2; probe P11).** No conflict. A gate changes the option set (`opening_set`); a weight changes a candidate's score. What stays true: no attribute adds or removes a candidate, no attribute refuses an act, and the believed-odds path (`odds_weight` × `faculty`) stays the one route by which capability reaches a contested candidate. What AR-04 adds is a second route, for uncontested candidates and for the noise of the choice itself, designed in CR-93. Falsifier for "gates nothing": the set `opening_set` returns is equal for two persons who differ only in attributes (CR-93's control).

**(ii) AR-44 "ignoring obstacle modifiers / adding modifiers to the dice pool" against "advantage is a μ-shift, never an Ob reduction" (`skills/resolution-diagnostic/SKILL.md` §2; `roll.py:103-104`).** Resolved by which quantity Spirit acts on. (a) **Adding to the pool** is dice, not advantage: the door is `register_pool_addend` (`sigma.py:133`), the practice precedent, and is lawful as it stands. (b) **Ignoring obstacle modifiers** may only discount the ADVERSE instance modifiers (a hostile bench's share of the room terms, `roll.py:122-130`; the fighter's own wound term, `combat_systems.py:1044`), never `base_Ob` (`score/2`), never TN, and never take the composed obstacle below `base_Ob` or `OB_MIN`. A discount on an adverse addition cannot cross the floor the diagnostic protects, which is what its §2 forbids. Which modifiers, and the coefficient, are CR-95's design, run through `resolution-diagnostic` before any build `[ASSUMPTION; medium; Jordan to correct; revert: Spirit acts only through the pool addend]`.

**(iii) AR-40 (the read is pure Perception) against ED-IN-0326 and combat's `reading`.** ED-IN-0326 governs judgment of persons and of context in the season; it says nothing of a fight, so AR-40 does not displace it. "Pure" governs which attribute reads, not the tradition and familiarity factors that scale the read (AR-17 and AR-45 keep them). What it leaves Reason in combat: nothing in resolution. AR-02 accepts a niche attribute; AR-21 places Reason in forecasting and understanding what a choice entails, which in a fight is the choice of mode and depth, and the module chooses those by its own rules (`disp_lean`, `select_mode`), not by a roll. Taken: no combat read of Reason; `cog` leaves the fighter's inputs `[ASSUMPTION; medium; Jordan to correct; revert: keep `cog` as an input for a later tactical-choice term]`.

**(iv) Grace and Spirit on pressure (AR-33, AR-44).** Spirit is not being moved (inner: resisting influence and compulsion, tolerating strain). Grace is being seen as composed and correct (outer: regard, the venue's standard). So Spirit is the opposing attribute against persuasion, interrogation and arrest (CR-96's `opposed_by`, CR-95), and Grace never opposes a roll; it acts on how others regard the person and on whether a formal venue penalizes him (CR-92). The ED-IN-0328 gloss "composure (ability to remain calm under pressure, nerve)" is narrowed by AR-44, the later statement: nerve is Spirit's.

**(v) AR-10 (damage mitigated by weapon type) against the reverted multiplicative Strength (`core.py:571`; ED-1040).** The reverted form scaled Strength's share by one exponent for every head. AR-10 asks for a head-dependent weight, and the additive owner already has a head branch (`strike_impact`'s blunt arm). Minimal: `strike_impact = k_str[head]·strength + heft`, additive, with the blunt head's weight highest and the point's lowest, the weights chosen by a measured sweep on `systems/combat/combat_engine_v1/workbench/balance.py` with ED-1040's observable (draw rate of the low-Strength heavy-weapon mirror) as a bound the sweep must not breach; all weights 1 is the control and reproduces today byte for byte (PC-20 (1)).

**(vi) AR-56 to AR-58 (health).** PROVISIONAL. Not planned; §3.3 records it and the form question it inherits.

**(vii) AR-05 (floor of 1) against constructors that accept any number.** The scale has one owner, the registry (`scale: "1-7"`). The carrier enforces it at write (CR-20: refuses outside 1 to 7) and the seam floors what it derives (`party_end`, `max(1, …)`). The module takes typed input and is not a second owner of the bound (PC-14 item (1) and its FALSIFIER: "a spec that carries a registry name or bound → fail"). No module edit. The workbench may build sub-floor fighters for probes (PC-17's Agility 1 / Strength 1 probe sits on the floor, not below it).

**(viii) Familiarity (AR-43 to AR-48) and the module contract (`04` §A.2; `holonic_ARCHITECTURE.md` §43, §45).** Grown in the season, fixed in the bout, handed in by the seam: exactly how `end` arrives (`seam/wrappers/combat.py:130-138`). The season side stores nothing: as `world_q.practice` (`:4095`) derives a pool addend from the holder's own resolved acts in the log, familiarity is derived from the holder's own past fights against opponents of that weapon class (and tradition, through his tradition's skills). Taken over a stored capability key `[ASSUMPTION; medium; Jordan to correct; revert: a `capability` key per weapon class, raised by fighting]`; the weapon class is `weapon_physics.py`'s `wclass` (three classes, the existing classification) `[ASSUMPTION; medium; Jordan to correct; revert: the strike `head` tokens]`. The season half is inert until a person has a tradition and a weapon in a season fight (CP-T03-03, kit, B10-11; no `Person` tradition carrier exists): PC-21's design says which lands first.

**(ix) Grace and "standing" (AR-34, AR-35).** Jordan's "office of low standing" is an office's rank (`rung_kinds`, the ordinal); "think well of them" is regard (`person_q.regard`). The code's `standing_of` (`decision/options.py:1380`) is a third thing, the gap between what others tell of a person and what he holds of himself, and Grace does not touch it (Attunement might: map F16 (a); not built, no ruling names it). The Grace term enters regard, and so promotion through `stance_term` (AR-35), with no change to `confer`. Because regard is person-side and computed from the holder's own ledger, the holder may not read the referent's true Grace: Grace must reach him through something deposited (what he saw of the person's conduct, at WITNESS, where the World may be read), as CR-79's credit term reaches him. That is a design question with a Layer 1 edge (AX-2, the own-ledger rule; `layer-conformance` Lens B first): CR-92.

### 2.3 What each standing rule keeps

- **"Capability supplies dice and gates nothing"** stands (i).
- **"Advantage is a μ-shift, never an Ob reduction"** stands (ii).
- **"A registered module takes typed input and keeps no game state"** stands (viii); every new combat input is set by the seam per bout.
- **"No attribute reaches Godot until IN FLUX lifts"** stands (`CLAUDE.md` §5; CR-84 decision (5)).
- **"Gains are improvements and therefore ship"** (Jordan, B-E; cited by H-192, H-193, H-199, H-202) is the precedent each swept term below uses to choose its shipped value: the sweep's midpoint where the sweep shows the term monotone and the control reproduces the base; otherwise the term ships at its control and the reading is recorded.

## 3. Decisions

### 3.1 Answered by the ladder

Each: the question, the step that answers it, the answer.

1. **Does combat keep any Reason read?** Step 3 (AR-21 places Reason in forecasting; AR-02 accepts niche). No. `[ASSUMPTION; medium; Jordan to correct; revert: keep `cog` for a tactical-choice term]`.
2. **Which attribute disguises the attack?** Step 3: AR-18 names Coordination. The term lands in `read_a` (where the aggressor's side already enters), not `legibility` (the strike's physical readability). Step 5. `[ASSUMPTION; medium; Jordan to correct; revert: the term in `legibility`]`.
3. **Does Focus enter the response?** Step 3 (AR-19) and step 4 (the reserve `consistency` already is Focus's error rate in this model, map F13): a lapse term on `mode_sigma` reading the defender's reserve. No new momentary quantity. `[ASSUMPTION; medium; Jordan to correct; revert: no response term]`.
4. **Inattention as a source (AR-22)?** Step 2: the module fights one against one (`wrapper.py:533`), so "outnumbered, watching two" has no case; inattention in the moment is the drained reserve (3). Pain stays the per-hit drain (`CONC_DRAIN_HIT`); a severity-scaled drain is not built `[ASSUMPTION; medium; Jordan to correct; revert: drain ∝ damage / wound interval]`.
5. **Balance: ½ Coordination + ½ Strength (`combat_systems.py:188`) against AR-15's footing on Coordination?** Step 3: AR-13 gives Strength the counterbalancing of heft, so the half share is consistent with both; the 2026-06-03 ruling stands. No change.
6. **Fluency above demand (AR-12)?** Step 5: "managing heft" is the shortfall the code has; "weight itself" is the missing term. Built: a static mass term in `str_demand`. Surplus fluency not built `[ASSUMPTION; medium; Jordan to correct; revert: a graded surplus term]`.
7. **Leverage (AR-10)?** Step 5: the bind and wind already price Strength in the contest of levers (`:1062`, `:349`); `leverage()` stays geometry. No build `[ASSUMPTION; medium; Jordan to correct; revert: a Strength factor on `leverage`]`.
8. **Armour (AR-10)?** Step 4: the `handling_penalty` form (a Strength shortfall against a demand). Built: an armour demand per tier and a shortfall cost on stamina; the demand values are chosen by sweep, none at `none`. PC-20 (3).
9. **Occasions (AR-53)?** Step 3: CR-87's `violence_contexts` (war, crime, duel, defence) are fight occasions at formation, and PC-10's stakes reach the module as `terms`. No occasion field is coined until a reader of it exists (step 2: the attribute emphasis by occasion is not ruled).
10. **The acceptance asymmetry (AR-51, AR-52)?** Step 5: `accept` takes `fight`'s cost (CR-87 (2) amended); the station and "could the duel solve it" terms are duty of office, CR-88's design (step 4: CR-88 already prices an office holder's conduct).
11. **One secondary attribute per verb (map §1)?** Step 5: no. CR-20 carries one base per vocation. Grace's role in a contest is a venue standard, not a pool contribution (AR-36a), and Spirit's is the opposition (AR-44), so no verb needs a second pool attribute. `[ASSUMPTION; medium; Jordan to correct; revert: the `faculties:` weights of proposal-4]`.
12. **Grace in a formal venue: margin, reception or record (map F18)?** Step 3: AR-36a says the venue "would penalize someone who lacks sufficient grace as even if they're persuasive they aren't 'doing it right'"; a penalty that applies even to the persuasive acts on the result. Taken: the shortfall demotes the contest result (the margin); surplus adds nothing in the venue (it acts on regard). `[ASSUMPTION; medium; Jordan to correct; revert: the shortfall lowers `reception` only]`. CR-92 designs the band and how the requirement is read from `arrangements.yaml`'s existing keys (no fourteenth key; `data/arrangements.py` refuses one).
13. **Where does Perception act in the knowledge model (map F9)?** Step 4 (ED-IN-0326's readers are designed in CR-83) and step 5 (the World may read a true attribute at WITNESS; a person-side reader may not): at WITNESS, on the deposit's confidence, for the `seen` and seat channels; not a gate. CR-83 amended `[ASSUMPTION; medium; Jordan to correct; revert: a gate on the deposit]`.
14. **Focus in the chooser (AR-23)?** Step 5: a per-person τ falling with Focus (`_sample_order` already receives `p`, `choose.py:243`). CR-93 designs it with AR-04 and AR-21.
15. **Reason's forecast (AR-21)?** Step 5: the believed odds are exact today; Reason shrinks, and low Focus widens, an error on the believed chance. CR-93.
16. **Presence beyond rolls (AR-29, map F12)?** Step 5: the commander's Presence weights the receiver's `comply` against `defy`/`evade`, a term on another's choice. CR-92 (others' responses), not CR-93.
17. **Attunement and bonds (AR-31)?** Step 5: a formation-likelihood term on `tie / knot` reading Attunement, designed in CR-92, consumed by IN-32's effect; the oracle's Bonds gate is re-pointed by the position that next edits `knots.py`.
18. **Forgery quality (AR-16)?** Step 4: the forger is the examiner's opposition, so the forger's Coordination enters as an opposition score does, `score/2` (Jordan, 2026-08-14, `roll.py:93-97`); an unauthored forger keeps `default_forgery_quality`. CR-94 `[ASSUMPTION; medium; Jordan to correct; revert: the fixture]`. Lock-picking: step 2, no verb; nothing built.
19. **Strength's health share form (AR-05, AR-11)?** Step 2 for now: the health formula is PROVISIONAL (AR-58); the product `STR_HEALTH_W·S·E` conforms to AR-05 at E ≥ 1. No change until the health design.
20. **Which competence attribute does CR-19 read for a told claim about a fact?** Step 4 (ED-IN-0326 and AR-26 split readers by matter): CR-19 builds Attunement as written, at gain 0; CR-83's design says which attribute grades which kind of claim (persons: Attunement; offices, regimes, obligations: Reason; facts: Perception) before the flip.
21. **Familiarity's store, key and weapon class:** (viii).
22. **How do a person's attributes reach his fight (AR-48)?** Step 4: PC-06's K-1 is the position that builds it, held only on K-2, which CR-20 builds. Released by R8 into B10-11b, first. Precedent for the shape: `party_end` (`seam/wrappers/combat.py:130-138`). Every combat input is then set at the seam per bout and fixed inside it.

### 3.2 For Jordan

None survives the ladder. The two takes most worth his glance, because each changes the game: **(12)** a graceless but persuasive speaker in a formal venue has his result demoted, not only his reception; **(1)** Reason has no part in personal combat. Each reverts alone.

### 3.3 Recorded, not planned

**Health (AR-56 to AR-58, PROVISIONAL).** Jordan's sketch `(S+3)(E+3)` is "to be resolved later". The questions it will meet are map F27's: a total against the code's wound structure (interval × count), Spirit's leaving the formula against AR-44's "tolerate harm", and bout length with damage unchanged (`DMG_SCALE`). The instrument is the combat workbench. No position is written; when he resolves it, it is a PC position after PC-20.

## 4. Sequence

### 4.1 Dependencies

**B10-10 is unchanged (Jordan, 2026-11-05, received during this adjudication: every fold lands after B10-10, and nothing edits B10-10's contents, gates or exits).** CR-84, CR-86, REM-30, CR-20, CR-30, CR-19, CR-85's design, CR-33 and CL-CHAR build as their entries stand. Where a ruling displaces what B10-10 builds, the change is a later position gated on B10-10's close: CR-96 (B10-13) adds the opposing-attribute column to the `vocation_attribute` rows CR-20 lands and re-checks those rows against the RULED attributes (AR-16, AR-24, AR-29, AR-44); PC-18 (B10-11b) removes the history term from `reading` if CR-85's build has not. Nothing in the rulings needs B10-10 to change first: CR-84's ten keys and CR-20's one-base-per-vocation carrier are what every later position composes on.

- **Registry first.** CR-84 → CR-20 (B10-10, both as written) → B10-10's close → every position below.
- **Combat.** PC-14 (B10-10b; `att` mapped to Perception) → B10-11 (CR-85's build removes history from `reading`; CP-T03-03 lands kit) → **B10-11b** (new): PC-06's K-1 (released by CR-20; the seam builds the fighter from `Person.attributes`) → PC-18 (1) → PC-18 (2) → PC-19 (1) → PC-19 (2) → PC-20 (1) to (4); PC-21's design drafted beside B10-11b, its builds scheduled by it into the next batch that edits `modules/combat` and `seam/wrappers/combat.py`.
- **Knowledge.** CR-83's design (B10-13, amended with Perception) → its builds; CR-19's flip waits on it as before.
- **Social.** CR-92's design (B10-19, drafted after SC-02's design and CR-83's are approved, since it composes on `reception` and on the WITNESS deposit) → its builds by R8; IN-32 (B10-15) reads it.
- **Choice.** CR-93's design (B10-19, after CR-20 lands; reads CL-PERSON's M40 risk term so the two terms are not two ladders for one quantity) → its builds by R8 into the next batch sharing `decision/`.
- **Spirit.** CR-95's design (B10-19; its combat half after B10-11b, its social half after SC-02's re-source) → builds by R8; the `opposed_by` data change for Spirit is its first build commit.
- **Forgery.** CR-94 (B10-14) after CR-20.
- **Duels.** CR-87 (B10-11, amended) and CR-88's design (B10-13, amended).

### 4.2 Hash movers

| change | season (`build_realm` hashes, `runs/results.json`, `engine/season` goldens) | combat module (`tests/valoria/test_combat_*`, workbench, PC-11's `fingerprint.py` until it is deleted) |
|---|---|---|
| CR-96 (1) (`opposed_by` = the row's own attribute) | CONTROL-equal (a column read that changes no value) | — |
| CR-96 (2) (rows that contradict a RULED attribute changed) | MOVER where a changed row's verb rolls for an authored person; none if no row changes | — |
| PC-14 amendment (`registry_key`) | CONTROL-equal | CONTROL-equal |
| PC-06 K-1 (the seam passes attributes) | MOVER wherever a fighter's person has authored attributes (CR-20 writes the cast's `stats:`); an all-absent realm CONTROL-equal | — |
| PC-18 (1) reading = Perception | CONTROL-equal on a tree without K-1 (defaults `cog = att = 3`); after K-1, MOVER where an authored fighter has `cog ≠ att` | MOVER where `cog ≠ att` |
| PC-18 (2) aggressor Coordination | CONTROL-equal at K = 0, and at `agi` 4 at any K; after K-1, MOVER where an authored fighter's Coordination is not 4 | MOVER at the shipped K |
| PC-19 (1) at K = 0 / (2) flip | (1) equal; (2) MOVER of every season fight (the reserve drains on the first hit) | (2) MOVER |
| PC-20 (1) to (4) | each EQUAL at its control; each flip a MOVER of every season fight that reaches the changed term ((1) every armed fight; (2) every armed fight; (3) every armoured fighter; (4) every overcommit) | MOVER per flip |
| CR-94 | EQUAL in an all-absent realm; MOVER where a forger has authored Coordination | — |
| CR-83, CR-92, CR-93, CR-95, PC-21 designs | none (designs); each build they schedule declares its own | — |
| CR-87 amendment (`accept`'s cells) | MOVER, inside CR-87's declared mover | — |

Combat-module-only (season-equal at the class defaults): PC-18 (1) and (2) at K = 0, PC-14's amendment. Season movers: PC-19 (2), PC-20's flips, CR-94 where authored, CR-87's amendment, and every build the five designs schedule.
