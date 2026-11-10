# Personal combat — tradition sets: kits that plug into the live module

## Status: PROPOSED — design draft, HELD FOR JORDAN. Nothing is wired. No constant in `modules/` changes. Lane PC; no IDs allocated.

**What this is.** A draft of the ability kits for the five traditions that have a historical anchor, the eight levers they need that do not exist yet, and the evidence that the draft loads against the live module. **Where the numbers live.** Every ability value is in `kits_draft.py` and only there; this file names abilities and never restates a value. **Re-run.** `python proposals/2026-11-10-personal-combat-tradition-sets/check_kits.py` (structure, coverage, per-event sign, byte-identity, crash check) and `calibrate_kits.py` (paired texture and win-rate shift). Both are read-only against `modules/`.

**Reading status, stated first.** The first draft was written from slices and greps; Jordan objected, and I then read in full: `wrapper.py`, `combatant.py`, `attributes.py`, `fight.py`, `core.py`, `config.py`, `geometry.py`, `traditions.py`, `tradition.py`, `ability_primitives.py`, `vocabulary.py`, `contact.py`, `state_graph.py` (lines 1–150), and `combat_systems.py` except lines 1330–1340 and 1380–1424 (the second range was read earlier as part of `pursuit_sigma`/`close_rate`). Also read: the fiat audit (lines 45–114), `ability_armature.md`, `tradition_decomposition_v1.md`, `combat_throughlines_v1.md`, `engagement_psychology_recovered.md`, the agency proposal (lines 1–520 and 757–860; the rest grepped for Jordan quotes), `phase4_5_plan_v1.md` (lines 24–62, 143, 240–281), `PC_personal_combat.md` lines 1–200. **Now also read in full:** `weapon_physics.py` (all 997 lines) and `weapons.py` (all 934 lines). **Still not read:** `capabilities.py`, the workbench, `04_the_bout.md` to `07_saying_a_weapon_is_good.md` (Jordan quotes only), `HANDOFF_PC_history.md` (grep only), `PC_personal_combat.md` lines 200–568. The June ability-library designs the ledger cites are not in the tree. Claims below that depend on an unread file carry `[GAP]`.

## 1. The attached ledger is stale against the code

| Ledger says | Live code |
|---|---|
| Traditions are 7-channel vectors (`v ta pc lev te me ba`) | Removed 2026-06-29; "read by nothing as weights" (`traditions.py`). A tradition is `set` + `mode` metadata, a kit, and familiarity. |
| Imposition gate: adopt it (D-5) | Retired as fiat, Jordan 2026-07-23 (ED-PC-0023, ED-PC-0035). |
| `precommit` has 0 consumption sites; wire `eff_cw` (D-1) | Done: `read_contest` reads `precommit`; `eff_cw` is read at many sites in `combat_systems`. |
| 12 weapons | 54 records (50 excluding half-sword forms). |
| Layer B native traditions (Constraint, Root, Reach…) | `martial_traditions_synthesis.md` is not in the tree; unverifiable here. |
| Gap pt21 (`seize`) is the worst | `seize` stays cut; `sen_no_sen` can be re-homed to `precommit`. |
| Attributes `cog`, `history`… | `strength agi end att spirit focus faculty disp` (`attributes.py`); Reason has no combat read. |

The ledger's §5b premise, that a tradition should "impose its preferred node" at a beat, is the retired imposition gate. The kits therefore do not route; they modulate.

## 2. The vision the draft has to fit (Jordan's own rulings, as the repo records them)

1. **No fiat; every build available; not parity.** "Each combatant should have their own feel, emergent from their full stack… It doesn't mean every build is good, but every build should be *available*." (fiat audit, 2026-07-23.) The instrument is per-fight texture with the outcome preserved, not aggregate win rate.
2. **Tradition gates access; investment drives efficacy.** `_invested` already enforces it, and this session's checker confirmed an untaught equip leaves every probed value exactly unchanged.
3. **An ability is meant to be learned access to a graph transition, not a +X dial** (`phase4_5_plan_v1` §4b, NOT STARTED), with seven phase slots. The live layer is the multiplier scaffold. **The kits below are the interim form.** Each ability carries `point` (the transition) and `also`; `SLOT_OF_POINT` derives its phase slot so a Phase 4b schema can adopt them without re-authoring.
4. **Composed, not accumulated** (agency proposal §21 A.4). Slots per tradition: German 5, Italian 5, Spanish 3, English 2, Japanese 4 (`check_kits.py` §3b).
5. **Throughline test for a new lever:** does it move a real axis or duplicate one? Each new lever is named for the axis it moves in §3.
6. **Source-tier rule:** no technique, no ability; Chinese and Filipino stay empty until anchored (§6).

## 3. Plug-in contract

A **lever** is a read site: an `eff_cw`, `ability_factor` or `ability_bonus` call inside a `combat_systems` or `contact` function. It exists with no one trained, and is then exactly neutral. An **ability** is a record: `tradition`, `grade`, one `lever`, `op`, `value`, `desc` (the technique), owned by a kit, scaled by invested level (`value ** level`, level ≤ 8), composed by product with other abilities on the lever and clamped. Levers are not gated by abilities. Abilities are gated by tradition (`_invested`), and some levers are further gated by the weapon (`edge_read`, `choke_control`, `spine_press` need the morphology). The half-sword switch and the capability predicates are not ability targets at all (agency proposal §5, Class B).

**Nine new levers** (eight in the table below plus `handling`, §3c, which has no ability), each one `ability_factor` call at an existing function (`LEVERS_NEW` in `kits_draft.py` gives site, sign-safe form and the `config.py` constant):

| lever | axis it moves | site |
|---|---|---|
| `close` | distance / measure (the closer's rate) | `close_rate` |
| `stophit` | reach (the longer weapon's approach threat) | `stophit_sigma` |
| `disengage` | measure / contact (refuse the bind) | `disengage_clean_p` |
| `pursuit` | measure (catching the withdrawal) | `pursuit_sigma` |
| `guard_prior_{parry,dodge,wind}` | technique (habitual defence on a lost read) | `read_contest` lost-read branch |
| `grapple_control` | contact | `contact.grab_sigma` |

Neutrality: every form is exactly neutral at factor 1.0. `guard_prior_*` must keep `modes[rng.randrange(3)]` when all weights are 1.0, or the RNG stream changes for default builds. Signed sigma sites take `K * log(factor)` (the `lever_log_edge` precedent, ED-PC-0045).

## 3b. Relations: abilities that set up other abilities

The live ability record is flat. `_invested` checks tradition membership only, and abilities on a lever multiply, so a kit is a bag of independent multipliers. Jordan's objection, in his words: an ability "shouldn't just be values over a lever, but should be changing behaviour around that lever too". `phase4_5_plan_v1` §4b names the same fields (`prereq`, `trigger`) and calls an ability "learned ACCESS to attempt a graph transition, never a +X dial". The draft adds three relations (`RELATIONS` in `kits_draft.py`; none is built):

- `requires`: an ability can be invested only while its prerequisites are invested to a level. The access gate gains a second clause.
- `widens`: with the named abilities invested, a gate admits a case it refuses today. This is the agency proposal's Class B ("availability, never magnitude"); it only adds cases, so an empty kit stays byte-identical.
- `branch`: the follow-up depends on a state the lever already computes, instead of one fixed weight.

Five are authored, each where a source read this session states the dependency: Capoferro ties the time available to the measure (wide measure a tempo and a half, narrow a whole tempo, narrowest half), so `mezzo_tempo` and `contratempo` require `misura`, and `misura` widens `mezzo_tempo` to a won read at narrow measure without a deep commit (the engine's `DEEP_COMMIT` gate at `wrapper.engagement` is the repo's, not the treatise's); Zornhau (verses 27–31) takes the blow off if the opponent reacts and winds and thrusts if the opponent is strong, so `fuehlen` branches between `absetzen` and `staerke_schwaeche`, and `indes` requires `fuehlen` (carried from the repo). Chain depth is capped at three, after Fiore's "few plays go past the third master" (V). Spanish, English and Japanese have no authored relation because no source read states one; inventing a chain is the error ED-PC-0026 removed twice. Engine work implied: a `requires` clause in `_invested`, and one availability test at the `DEEP_COMMIT` gate. Neither is a lever.

## 3c. What the full read of `core.py`, `config.py` and `combat_systems.py` changed

- **`IT-3` widens more than the counter.** In `wrapper.engagement` the Indes steal and `counter_select` sit inside one block, `if read_win and commit>=cfg['DEEP_COMMIT']`. Widening that gate for `mezzo_tempo` would also grant the initiative steal. The build must split the block so only the counter attempt widens. This also explains why `mezzo_tempo` and `indes` measure near-inert in aggregate: both act only after a won read against a deep commit.
- **The `measure` lever fades with armour.** `reach_sigma` puts the lever inside `REACH_W[armour]` (0.62 unarmoured, 0.20 heavy), so `misura`, `circulo` and any measure ability lose about two thirds of their effect against plate. `true_time_edge` fades to zero at plate by the same logic. That matches Silver's unarmoured doctrine but means Italian and Spanish measure kits are an off-plate effect.
- **`compas` is the repo's own intended balance lever.** `balance_eff`'s comment says "ability modulation (Destreza compás etc.) arrives with the channel-wiring pass". The draft's `compas` on `balance` is that.
- **Reading is Perception alone, and the tempo read term is zero in any same-stats fight** (`tempo_pressure`'s own honesty note, ED-PC-0037.1). My mirror-weapon calibration therefore under-reads any ability whose effect rides a stat differential; builds that diverge in stats will show more.
- **Silver's rear-clearance quote already sits in the code** (`REAR_CLEARANCE_TEMPO_K`: "the length behind the hands will hinder him to strike, thrust, ward, or go back"), and `true_time_edge` quotes the hand-before-foot passage. `choke_control` therefore has a candidate English anchor, with the repo's own caveat that weapon selection and a mid-fight choke must not be conflated. Not authored.
- **`guard_prior_*` is bounded by `defense_affinities`.** Each weapon's parry, dodge and wind caps are derived in [0.4, 1.0] (`weapon_physics.defense_affinities`) and `mode_sigma` multiplies the mode's sigma by that cap. A habitual guard on a lost read that the weapon is poor at therefore costs at most 60% of that mode's sigma; it is a real but bounded price, and it is paid by the weapon's geometry, not by a new constant. A heavy two-handed sword's dodge cap sits near the floor, so a dodge prior there would be nearly dead weight.
- **`spine` and `edge_lines` are per-element edge data** (`sides`, `false_edge_frac`), so `shinogi` fires only on a single-edged blade and `edge_read` only where a double or false edge exists; the weapon list in each kit should be checked against those two functions before an ability is tied to a weapon.
- **The weapon's skill ceiling was deliberately moved out of the weapon and is owed to the tradition layer.** `weapons.py` and `weapon_physics.handling()` both say the retired `hand` category (Forgiving / Standard / Demanding: a spear "Forgiving", a rapier "Demanding") "encoded a weapon-TRADITION's skill-ceiling", is "EXPLICITLY NOT reconstructed here", and "relocates to the future fighter/tradition competence layer (plan decision 4/6)". Nothing in the kits does this. The engine already has the site: `handling_penalty` (a non-negative deficit of weapon demand over Strength) feeds both `attack_sigma` and `defence_sigma`, so an own-side mitigator is sign-safe. The draft adds it as a ninth lever, `handling`, with **no ability authored**: weapon competence is drill, not a documented technique, so the source-tier rule gives nothing to cite. This is the clearest open design call the read turned up (§8).
- **Edge data limits where the Japanese kit's `shinogi` acts.** `_EDGES` makes `tsurugi` and `yari` double-edged (spine 0), so `shinogi` is inert on two of the seven weapons the kit teaches; it fires on `katana`, `tachi`, `odachi`, `naginata` and `kama_yari`. The rapier is double-edged (`edge_lines` 1.0), the estoc edgeless.
- **Korean polearms already cite a Korean manual in the repo.** `kama_yari` and `dangpa` record "documented hook/bind/catch use, Muyedobotongji" (`weapons.py`), and `spetum` cites "Monte". Neither source was read here, but a Korean tradition would not start from nothing; it is the best-anchored of the weapon clusters with no tradition.
- **German armoured fighting is already physics, not an ability.** The half-sword switch (`affords_halfsword`: longsword, greatsword, flamberge, estoc) and the Mordhau/reversed-grip percussion option (`reversed_grip_percussion`, credited to "Liechtenauer-tradition half-swording") are weapon-level and gated as Class B, so a German ability on either would double-count.

- **Disposition is already the Vor/Nach anchor** (`config.py`: "Anchored to the German Vor/Nach doctrine (S2)"; "tradition=competence, disposition=propensity"). A tradition ability on commit depth would stack on an axis whose German grounding is already spent.

## 4. The kits

Names, lever, point and slot are in `kits_draft.py` and printed by `check_kits.py`. Grounding, with what was and was not read this session:

| tradition | new abilities | basis read this session | not read |
|---|---|---|---|
| German | `fuehlen`, `nachreisen`, `absetzen` | Liechtenauer verses 17–48 (Wiktenauer): Vor/Nach, Indes, Schwach/Stark, Nachreisen v.24, Winden v.26, Zornhau v.27–31; Lecküchner's two Messer manuscripts exist | Fühlen as a term; Absetzen as a term; Zwerchhau's function; Ringeck's gloss |
| Italian | `contratempo`, `volta`, `cavazione`, `abrazare` | Capoferro ch. 1–9 (misura, tempo, "contra tempo", cavationi named); Fiore: abrazare, daga, largo/stretto, half-sword; the three voltas (Windsor 2024) | Cavazione defined; Fiore f.39r (carried from the repo's R9) |
| Spanish | `compas`, `circulo` | none: the Carranza page read does not define circle, compás, atajo, angles or profile | all of it; grade is carried S2/S3 |
| English | `four_governors` | Silver: governors named, hand-before-foot, "place in true pace, space and time", short staff | the governors' list |
| Japanese | `sen_no_sen`, `metsuke`, `kiriotoshi`, `zanshin` | none: a search for the sen terms in Yagyū and Musashi found no passage | all of it; carried S2 |

The weakest mapping is `cavazione` → `disengage`: cavazione changes the blade's line, while the engine's `disengage` is a body withdrawal from a lost bind. It is the same kind of category stretch ED-PC-0026 removed for `winden` and `guardia`. **Hold it** unless Jordan accepts the effect-level match. `four_governors` has `mech=U` and is a candidate, not a recommendation. Held, not authored: `perfil` (the lever fits but `facing_regime` moves `close_rate` by ~0.14%) and `gardant`.

Weapon side (`teaches` per tradition, reference only; the engine lets any fighter wield anything): 24 of 50 weapons have a teaching tradition. Orphans, including the standing gap-register items: `greatsword flamberge estoc` (German/Italian candidates, unsourced), `sabre paired_short`, `mace goedendag bec_de_corbin lucerne_hammer`, the European polearms (`bear_spear ranseur spetum glaive fauchard bardiche sparr_axe voulge guisarme`), `scimitar pulwar shamshir szabla dangpa`, `rondel stiletto misericorde`. The standing short-blunt gap (ledger 5a#1) is unchanged. Messer/falchion (5a#4) is closed on paper by German, with Lecküchner as the source.

## 5. Coverage of the state graph

Eleven of thirteen injection points carry an ability. Deliberately unhooked: `exchange.commit` (disposition owns it and D3 is unresolved) and `burst.continuation` (a separation reason, not a contest; extending it would be the retired imposition gate). Levers with no grounded owner: `edge_read`, `choke_control`, `facing_regime`, `guard_prior_dodge`, `guard_prior_wind`. Those stay bare rather than invented.

## 6. Chinese and Filipino: not authored

- **Chinese.** The one mechanic the repo extracted, fa-jin burst from reach, changes damage transmission, which is Class A (forbidden). The *Jixiao xinshu* editions are inconsistent and the later edition drops the unarmed chapter (search result). Research brief: does any Ming spear, staff or sword text state a measure rule, a counter-timing rule or a defensive habit? (Kennedy & Guo 2005 exists; its reliability was not assessed here.)
- **Filipino.** A search found the earliest unambiguous technique documentation to be modern (a 1957 arnis book, per one secondary source of mixed quality); Spanish chronicles describe weapons, not systems. The paired-short curriculum has Western documentary anchors (sword-and-dagger, rapier-and-dagger) and could be re-homed there.

## 7. Measured (paired seeds, n = 3000 per ability, mirror weapon, one ability at level 1)

`texture` = share of seeds whose event sequence differs; `flip` = share whose result differs; `dWin` is the win-rate shift in points (95% half-width).

| ability | value | dWin | texture | flip |
|---|---|---|---|---|
| `fuehlen` | 1.20 | 0.7 (0.4) | 4.7% | 1.3% |
| `sen_no_sen` | 1.25 → 1.08 | 2.7 → 1.2 (0.9) | 40.9 → 15.4% | 17.5 → 6.1% |
| `metsuke` | 1.20 → 1.06 | 2.2 → 1.3 (1.1) | 55.0 → 22.5% | 21.7 → 9.1% |
| `zanshin` | 1.20 → 1.08 | 4.1 → 2.1 (0.7) | 25.7 → 12.0% | 9.4 → 3.9% |
| `compas` | 1.20 → 1.08 | 3.5 → 1.3 (0.7) | 55.5 → 26.6% | 8.8 → 3.9% |
| `circulo` | 1.15 → 1.04 | 6.1 → 1.6 (0.8) | 76.8 → 30.9% | 14.0 → 4.7% |
| `contratempo` | +0.12 | 0.0 | 0.1% | 0.0% |

The shipped values are the lowered ones. Three findings on existing abilities: `misura` (1.15) shifts win rate 6.1 points with 14% of results flipping, the same as `circulo` at 1.15, so it overshoots; `indes` and `mezzo_tempo` are near-inert in aggregate (0.1% and 0.3% texture), because the counter is a rare event; `contratempo` inherits that. The repo's own floor for rare-event levers is 2% texture (ED-PC-0058), which none of the three meets. No value is validated: the PCA band (|dWin| ≤ 2, texture ≥ 15%, flip 3–10%) is met by `sen_no_sen`, `metsuke`, `compas` and `circulo` within the confidence half-width and missed by `zanshin` (texture 12%, win-rate shift 2.1) and by `fuehlen` and the counters on texture. Results are `[SIM-CALIBRATE]` and unreplicated across weapons: each ability was measured on one weapon.

## 8. Decisions for Jordan, ranked

1. **Chinese and Filipino (agency proposal Q5).** Leave empty (the armature's rule), commission the research in §6, or accept explicitly flagged provisional content. The kits above assume the first.
2. **Build the eight levers?** `pursuit` and `guard_prior_parry` carry three abilities between them; `close`, `stophit`, `disengage`, `grapple_control` one or two each. Each is one call site plus one `config.py` constant and needs the agency proposal's sign-safety test and byte-identity gate.
3. **Interim modulator or Phase 4b access form** for the kits, and whether the relations in §3b are the shape wanted. The draft is shaped for the first and carries the fields for the second.
4. **New traditions** (the roster has Indo-Persian, Polish and Korean weapons with no tradition): adding an eighth tradition raises `ValueError` at import, because `ability_primitives._generics` needs exactly as many traditions as levers (7). It needs the 21 generics retired first (their stated revert).
5. **`misura` at 1.15** overshoots; lower it or accept it.
6. **`cavazione` → `disengage`:** hold or accept.
7. **Weapon competence (`handling`).** The repo moved each weapon's skill ceiling to the tradition layer and nothing carries it. Author it as drill-based competence without a technique citation (against the source-tier rule), leave it to skills, or drop it?
8. **The 2-point ceiling.** The fiat audit says texture with outcome preserved is the instrument and parity the wrong target; the agency proposal's band still states the 2-point ceiling. Which governs?

## 10. Fit with workplan v11 and the hole register

Read: the plan head (lines 1–131), `PC-06`, `PC-08`, `PC-21`, `PC-22`, `CR-95` and `CP-T03-03`; hole rows `H-97`, `H-264`, `H-265`, `H-349`, `H-350` in full and the title of every combat-related row. **Not read:** the other sixteen plan parts and the remaining ~330 hole rows.

- **The kits cannot reach a played fight.** A season `Combatant` is built from `end`, authored attributes, a kit and `faculty` (`fight.py`); no tradition and no equipped ability crosses the seam. `PC-21` says it plainly: "where a person's tradition lives (no `Person` carrier exists; CR-33's keys are the candidate)". `PC-06`'s K-5 (loadout) is held. `H-97` states the engine wants "a tradition" and derives only `end`. Until a carrier is designed, every kit here is a module-scale result.
- **No fight forms either.** `H-264`: `fight` was offered 0 times in about 3,500 opening sets because the violence-context decline (`CR-87`, deliberate) applies. `H-350`: all 83 persons in a built realm fight as `('arming','light')`, because `arms_kinds` and `arms_at_build` are empty and "the inventory is Jordan's content".
- **Nothing in the plan schedules abilities.** `PC-08` keeps Phase 4b (abilities-as-access), the channel-leverage residual and the contact axis named, unscheduled, with the rule that an R-row or hole citing them schedules them "the day that is read". No R-row or hole row cites a tradition or ability. Plan head rule 6 (P11): "Content is not the plan's to author… Equipment, tradition, troop types". The kits are therefore a proposal with no slot, and this PR is correctly outside the plan.
- **`PC-21` owns the site `guard_prior_*` wants.** Its design (item 2) is "the anticipation on a missed read… its effect on the draw order (the `modes[rng.randrange(3)]` contract)". Two designs for one line is the double-count the repo forbids. `guard_prior_*` should be folded into `PC-21`'s design, not built beside it. `PC-21` (1) also changes familiarity to a per-bout input derived from the log, which touches `ADJACENT`.
- **Jordan's 2026-11-07 rulings (`PC-22`) bear on the ability levels.** Experience from fights "should write moreso" to composure, Concentration being one function of Focus, Spirit and experience that retires `consistency`, `mental_fatigue` and `LAPSE_K`; "not increased technique and martial prowess itself". Nothing in the kits touches those three, so no conflict; but it leaves open what raises an *ability* level, since `train` raises a capability key by one and no row maps a key to `equipped`. The kits assume level comes from investment (`ED-PC-0024`); the plan has no source for it.
- **An owed sweep.** `ED-SC-0001` (LEAVE, trigger `CP-T03-03`/`-04` building) is "combat armour-tier and ability stacking". The relations in §3b and the stacking of several abilities on one lever belong to that sweep.

## 9. Falsifiers run

`check_kits.py`: structure (every existing ability restated here matches the live registry; no second ability on a lever within a tradition; every `point` is a real injection point; new levers have no consumer), per-event sign on seven live-lever abilities (taught moves the right way; untaught exactly inert), no crash over 100 seeds per tradition with the kit equipped. It did not test: byte-identity of the engine with the new levers built (they are not), RNG-stream neutrality of `guard_prior_*`, the other seven weapons per tradition.
