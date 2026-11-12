# Digest proposals_recent1

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane: proposals dated 2026-09-20 or later, and undated ones (68 assigned entries; see per-entry reading depth notes).
Reading-depth note: the assigned set is about 3.3 MB. Entries marked `[READ IN FULL]` were read to their end; entries marked `[READ PARTLY: ...]` or `[SKIPPED: ...]` say exactly what was and was not opened. Nothing is summarised from memory.

### proposals/2026-09-20-pursuit-basis-worksheet.yaml
- **What it is:** A Jordan authoring worksheet (YAML), 2026-09-20, replacing the 2026-09-18 conviction-basis worksheet. [READ IN FULL]
- **Status:** "WORKSHEET. Not a proposal, not canon, ratifies nothing" (:4-5); file is to be deleted once values land at the owners. Reading: historical/in-flight (the projection `set:` cells are all `{}`, :107-121, so nothing in it was ever filled in).
- **Bears on:** CHAR, CORE, FA (decision layer, pursuits/axes).
- **Content that matters:**
  - Fifteen pursuits replace thirteen convictions: virtue, honour, liberty, justice, wealth, reputation (was status), scholastics, stability (was order/authority), individuality, community, faith, happiness, family, love, warden (:39-54).
  - Seven bipolar axes replace four: hierarchical/equal, precedent/substantive, partisan/equitable, selfish/selfless, rigid/flexible, grandiose/humble, deontological/instrumental (:76-83); deontological/instrumental and precedent/substantive are ruled orthogonal (:70-74); `sacred` leaves the basis and moves to `Person.conviction` (:85-89).
  - Owners named: `references/descriptor_registry.yaml`, `engine/season/rosters.yaml` tables `pursuit_projection`, `alignment`, `role_template_pursuits`, `references/npc_registry.yaml` (:11-22). Warns role-template weights FAIL SILENTLY on a bad pursuit name (`to_axes` skips unrowed pursuits, `table()` validates no keys) while per-person weights RAISE `Unspecified` (:17-22).
  - R6 atomicity: rows, axes, projection and alignment must land in one commit or the loaders (`_load_alignment`, `_load_projection`) ImportError (:24-26).
  - Verb set moves 38 - 1 + 3 = 40: `kill / wound` is NOT a verb (combat seam outcome in an attempt's clothes); `fight`, `challenge`, `accept` IN; `duel` is the name of what resolves (:148-156). ALIGNMENT is read by two callers (`decision/choose.py::score` at DELIBERATE, `loop/effects.py::_scar` at RESOLVE) - recorded as a live defect (:142-147).
  - Scars: unit is a COUNT with thresholds destabilise 1 / weight_shift 2 / crisis 3, for both pursuits and convictions; written at RESOLVE by the act via `observers_for` (:188-207); `crisis_reader` OPEN. Deontological gates (refusal at `opening_set`) rather than scores (:222-226).
- **Conflicts / stale:** Cites a 52-of-152-cell alignment table and 38 verbs (:158); verify against `engine/season/rosters.yaml` before relying. Does not say whether ED-IN-0261 (cited :9) landed the cells. [UNVERIFIED]
- **Open items:** the 105 projection cells, alignment re-cell, crisis reader for both tracks, H-80 (computed act cannot declare operands) (:228-236).

### proposals/2026-09-25-squad-engagement-concept-v5.md
- **What it is:** Concept proposal v5 for a squad-engagement mass-battle engine, 2026-09-23, uploaded from outside this repo. [READ IN FULL]
- **Status:** "CONCEPT · non-canonical · not bootstrapped" (:3). Reading: partly superseded and reconciled by the sibling synthesis (below), which treats it as "a command / perception / plan layer on top of the shipped engine, not a new engine".
- **Bears on:** MB (primary), CHAR, GO.
- **Content that matters:**
  - Directives a-d (:7-14): FM/Total War inform formation at two scales; Mass pool retired (everything from N and Q per cell with morale, momentum, pressure, command); player routes/manoeuvres/conditional instructions; d: Stability sets morale baseline, bounded variance, player character is a duelling commander, Channellers do not exist.
  - Four modulators: morale clock with grade length L 4-7 plus depth bonus, shock cap 2 per tick (3 for rear charge) (:96-133); momentum with brace (:135-155); Pressure vs Steadiness giving in-hand/on-instinct with hysteresis k=3 (:157-184); Command at three holders, span 3+Cmd, CP_max = 3+Cmd (:186-197, :345-361).
  - Two channels: squad plan channel (movement, posture) and cell engagement channel (standing rules) with three posture actions and instinct per role (:201-302); conditions limited to what a unit can perceive; routing and withdrawing indistinguishable ("enemy moving away") (:230-243).
  - Manoeuvres are plans, not rules: envelopment, feigned retreat, delay, ambush, flank march (:327-339). Go-codes, messenger orders, shouts, seeded +/-20% friction, general's-view fog with ghosts (:363-398).
  - Outputs: killed/scattered/present per squad, scattered-return reduced by pursuit intensity p, grade progress, familiarity, deeds (:587-598); 11-step tick sequence (:600-615); first-simulation criterion `T_break >= 1.5 x T_flank` (:545-555).
  - Break ladder: cell (clock), squad (>=50% routed or leader), army (>=50% broken squads or general) (:502-513).
- **Conflicts / stale:** Relies on Keys/Key log (:387, :574, :630) - the Key substrate is RETIRED (ED-IN-0232). Cites `designs/proposals/` commit path (:748), a dissolved tree. Its map_v1/graph_v1 grounding docs are not in this tree (:4). Many `[PLACEHOLDER]` values. Synthesis rules several items superseded or already shipped.
- **Open items:** terrain source, objective zone, nightfall cap, mapping to the 7 canon phases (:615, :723-734); false signals/ghosts via parley (:572).

### proposals/2026-09-25-squad-engagement-synthesis.md
- **What it is:** Reconciliation of concept v5 against mass-battle canon and the sim: Parts A (build), B (do not build), C (Jordan rulings), D (coupling design); MB lane, ED-MB-0067. [READ IN FULL]
- **Status:** "RULED (Jordan, 2026-09-25) — design decided; built: HANDOFF_MB (ED-MB-0069..0077); open: MB-07r (J-18 (A) built, shipped OFF), MB-08 (LEAVE)" (:3). Part D is "PROPOSED — needs Jordan" (:334). Reading: live as a ruling record; execution status lives in HANDOFF_MB, not here.
- **Bears on:** MB (primary), CORE (seam), FA (muster, Stability), PC (duel handoff).
- **Content that matters:**
  - The Mass pool was already retired by ED-MB-0006 (default-ON `POOL_QUALITY_MODEL`); what survives of v5 is a command/perception/plan layer, missile ammunition, terrain, and per-cell Q (:38-53).
  - Part A build slate: routes with waypoints (A1, `_resolve_maneuver_goal`), perception-limited order triggers (A2, `core/contact.py` omniscient today), subordinate-officer Cmd (A3, resolving ED-1090), order latency/go-codes/relay (A4; `target_delay_ticks` is NOT transmission latency), role instincts in `ROLE_SPEC` (A5), missile volleys track (A6), battle terrain from `systems/settlements/valoria_geography_v30.yaml` key `terrain:` (A7), choose `ROUT_CASCADE_FRAC` by sweep (A8, default 1.0 UNCHOSEN), `causes` on trace rows (A9) (:57-135).
  - Part C rulings: per-cell movement/facing (C1); envelopment multiplier stands and feeds morale collapse checked against Discipline (C2); Discipline retained, Pressure folded into the check, not a second gate (C3); feigned retreat stays fog with a repurposed PP-256 recognition roll (C4); span of control stays "= Command" (C5); directives a-d confirmed real (C6) (:243-311).
  - d.1 correction: the morale starting formula was never implemented - `massbattle.py:_faction_to_unit` hardcodes `morale=5, morale_start=5`; PP-711 (morale reset) is unaffected (:308, :313-319).
  - Part D design: replace the pre-combat envelopment delta-sigma penalty (`_charge_shock_sigma`, `orchestration.py:1156-1171`) with a post-damage erosion `dmg / (agg_discipline x command)` gated by `discipline_check_cascade` (recommended option 2) (:345-431).
  - Loop does not call mass_battle: `engine/season/seam/contest.py:142-179`; `rosters.yaml:751-757` "NO PROVIDER" (:145).
- **Conflicts / stale:** Line numbers in `orchestration.py`/`config.py` were as of 2026-09-25 and will have drifted [UNVERIFIED]. The stated headline "built" items (ED-MB-0069..0077) need checking against HANDOFF_MB.
- **Open items:** Part D check-form fork (needs Jordan); d.1 landing at `_faction_to_unit`; objective zone and 7-phase mapping not examined (:441-446); Channeller propagation to Thread lane (:311).

### proposals/2026-09-30-character-and-play-surface/01_the_season_loop.md
- **What it is:** Analysis of how `engine/season/` runs one season, why seeded seasons replay, and where the nine requirements stand; IN lane, measured at HEAD `c8cc408` (after #444), 2026-09-30. [READ IN FULL]
- **Status:** "PROPOSED (2026-09-30) · design-only · ratifies nothing on merge" (:3); README later marks parts ratified as intent (v9, ED-IN-0290). Reading: historical snapshot (figures are as of c8cc408); recommendations partly live via the README roll-up.
- **Bears on:** CORE, CHAR, SC, FA, SE.
- **Content that matters:**
  - Season order: CALENDAR, MATTER (yields/eat/freeze), rounds of DELIBERATE/RESOLVE/ENCOUNTER/WITNESS (scene_budget 5), CENSUS (writes nothing); four barriers each mint one write token, DELIBERATE gets none (:18-42).
  - Replay: every id and draw derives from `H(seed, tick, subject, purpose)`; the PC provider seeds itself with a different purpose string so existing fights were not re-recorded (:44-55).
  - Honest qualifier: sigma-leverage contests roll with ZERO leverage (`sigma.py lev = 0.0`) and `_pool_of` falls to `pool_default`, so a social contest varies by seed and fixture, not by person (:57-60).
  - #444 status: 26 of 44 verbs have effects; carry/exchange/forge/repudiate/succeed/tie-knot have writes and no effect; no coin; shipped realm ~35x surplus; `found`/`build` 14/15 attempted, 0 executed (:64-70).
  - Requirements at that date: met 1, partial 5, not met 3 (R-01, R-02, R-05 not met) (:74-77).
  - Recs L-1..L-4 (supported per-person season read; fix `deliberate.py:114` comment; name zero-leverage state; founding chain reachable by computed play) (:87-94).
- **Conflicts / stale:** All counts (26/44 verbs, 83 persons, requirement tallies) are point-in-time; re-run `register --requirements` and `aperture` before use. [UNVERIFIED]
- **Open items:** L-4 founding chain; zero-leverage producer.

### proposals/2026-09-30-character-and-play-surface/02_against_precedent.md
- **What it is:** Re-scoring of the repo's precedent survey (August verdicts about the retired campaign driver) against `engine/season/`; IN lane. [READ IN FULL]
- **Status:** "PROPOSED (2026-09-30) · design-only" (:3). Reading: historical/reference; verdict table is a snapshot.
- **Bears on:** CORE, FA, SC, SE, CHAR, MB.
- **Content that matters:**
  - "Plan finished" = one consolidated engine with governance/settlement content; NOT faction agency, parliamentary procedure, relationship model or SC manoeuvre set (:20-26).
  - Factions: structure without agency (`faction_q`, `head` empty, `at_war` false); parliament still below floor (`determine` executes 0 times); conquest does not exist (winner gains nothing); relationships: only `march` writes a stance row; economy loop without pressure (:35-39).
  - Mass-battle seam still has one real input (headcount) (:42); R-01/R-02 not met, ~4% later-decision divergence vs 100% world divergence (:63-69).
  - Recs P-1 (more acts write stance rows with causes), P-2 (scarcity teeth with control arm), P-3 (seat faction heads, let a head act), P-4 (procedure before the vote), P-5 (pointer fix) (:80-84).
- **Conflicts / stale:** References plan `workplans/2026-09-28-the-plan-one-order-mc-v18-retired.md` and phase-4 revision - may have been retired since. [UNVERIFIED]
- **Open items:** the missing pieces are explicitly "not in the plan" (:74).

### proposals/2026-09-30-character-and-play-surface/03_play_surface.md
- **What it is:** What an interface can bind to; readiness ranking of PC/SC/FI as playable; IN with PC, SC, FI. [READ IN FULL]
- **Status:** "PROPOSED (2026-09-30)" (:3); README ratifies S-1, S-2/L-1, S-6 as intent. Reading: live as intent.
- **Bears on:** GO, CORE, PC, SC, FI.
- **Content that matters:**
  - Existing seam: `SeasonDriver.season(choose, ...)` calls `choose(p, v, s, ask_budget)` sequentially; `opening_set(p,v,q,fx)` gives candidates; `build_realm` makes 83 persons, 24 seated (:16-29).
  - Missing: no wire format, no supported season record, no omniscient event log (an `Event` has no actor/target/subject), no client; `godot/skeleton/` does not compile (:34-46).
  - Epistemic contract: a client may read only a projection of one person's holdings (:50-54).
  - Readiness: PC runs real deterministic duel but trace dropped; SC `tell` has zero leverage, `arrangements.yaml` thirteen keys / three arrangements all `disposal: bench`; FI five of six acts execute but no graded outcome, `thread_read` untyped precondition, `knots.py` uncalled (:60-67).
  - Recs S-1 (dispatching `choose`, control = hash equality), S-2 (per-person projection), S-3 (journal of belief), S-4 (return trace), S-5 (weapon card), S-6 (graded FI outcome), S-7 (decouple client choice) (:75-81).
- **Conflicts / stale:** Realm numbers (findings made/none per act) are point-in-time. SC proceedings "held back" claim should be checked against the proceedings proposal status. [UNVERIFIED]
- **Open items:** fieldwork graded outcome; Godot version unruled.

### proposals/2026-09-30-character-and-play-surface/04_the_bout.md
- **What it is:** Analysis of the personal combat engine: bout structure, traditions, the nine moments, how much is built; PC lane. [READ IN FULL]
- **Status:** "PROPOSED (2026-09-30)" (:3). Reading: live reference.
- **Bears on:** PC, CHAR, GO.
- **Content that matters:**
  - Bout = `wrapper.fight(A,B,cfg,rng,max_bouts=12)`; the GAME calls one `engagement()` per turn (~10 s fiction); wounds add fractional Ob, never remove dice (ED-PC-0005); unresolved is legitimate; `UPSET_FLOOR = 0.05` (:18-28).
  - Tradition multiplier vectors were measured (18.8 pp imposition spread, 6.8 pp win-rate spread) and deleted 2026-06-29; imposition gate retired (ED-PC-0023/0035); a tradition is now access to learned techniques with source tiers; efficacy from graded investment (ED-PC-0024) (:32-49).
  - Nine moments in `state_graph.py::INJECTION_POINTS`; six are player-facing (measure, reopen, commit, mode, counter, contact), three closed (read, bind entry, burst continuation) (:56-71).
  - Fifteen levers, nine techniques across five traditions on seven levers; eight levers have no technique; `seize` lever dead (consumer cut 2026-06-05) (:79-102).
  - Recs B-1 (author techniques for 5 unhooked levers), B-2 (fix stale `injects` prose), B-3 (per-event tradition identity), B-4 (never restore multipliers) (:143-146).
- **Conflicts / stale:** Cites `.designs/.../tradition_decomposition_v1.md` (archived). July figures not re-measured (:5).
- **Open items:** `seize` retire-or-reroute (Jordan's call, in `ability_primitives.py`).

### proposals/2026-09-30-character-and-play-surface/05_two_modes_of_one_bout.md
- **What it is:** Design of a grid mode and a duel mode over one combat engine, with Jordan's verbatim intent; PC with IN at the seam. [READ IN FULL]
- **Status:** "PROPOSED (2026-09-30)" (:3); README: 05 section 4.1/4.2 attach to M-2, two modes are Jordan's intent (SM-5), suspension IN-46. Reading: live as intent; grid half later suspended (see 2026-10-07-grid-mode-suspension).
- **Bears on:** PC, MB, GO, CORE.
- **Content that matters:**
  - The season `fight` verb (renamed from `kill / wound` 2026-09-29) calls `wrapper.fight()` (the harness) in one act; parties built with one derived field (`end`) - everything else class defaults (:20-32).
  - `_TRACE` fires at 20 call sites over fifteen event kinds; seam sets it and then returns only `bouts` (:41-47).
  - Persistence: only `Person.body` carries a fight's result; wound count/interval rebuilt each fight (:34-37).
  - Three fidelities, one engine (auto = `fight()`, grid = one `engagement()` per attack with trace as bout, duel = beat by beat) - Football Manager pattern vs Total War divergence (:85-99).
  - Plan layer rules: plan is a prior, intent contested, every intent a trade; T0 build / T1 plan / T2 beat closed (:58-73). No person-scale grid; route: mass battle at weight 1 (:75-83).
  - Recs M-1..M-6; For Jordan: do unwatched fights resolve inside one act, and does duel mode open any closed moment (rec: no) (:122-138).
- **Conflicts / stale:** M-1 trace return may since have been built [UNVERIFIED].
- **Open items:** the two Jordan questions; M-3 wound persistence.

### proposals/2026-09-30-character-and-play-surface/06_weapons_from_physics.md
- **What it is:** Measured account of how `weapon_physics.py` turns a weapon record into performance and where armour enters; PC. [READ IN FULL]
- **Status:** "PROPOSED (2026-09-30)" (:3). Reading: live reference.
- **Bears on:** PC, MB, CHAR.
- **Content that matters:**
  - 52 weapon records (header says 53) as located massed parts; `hand_guard`/`blade_guard` literals are overwritten at import (rapier 0.9 -> 0.68) (:19-29).
  - Armour enters via `core.coupling`, `adef_cap` vs `ADEF_THRESHOLD` (light 0.30, medium 0.45, heavy 0.72), and `select_mode` (bec de corbin switches to percussion at heavy; poleaxe punctures at every tier) (:47-76).
  - F1: `material` has no reader, so a wooden staff clears heavy plate (adef_cap 0.915) contradicting `core.adef_cap`'s own docstring (:109-116).
  - F3: parry affinity is at its floor for 35 of 52 weapons; F4: `recoverability_factor` spans 0.30 to 62.1 (guandao) (:124-134). Spine lever reaches 25 weapons, not katana-only (:117-122).
  - Table of what each of nine moments reads (:89-99). Recs W-1..W-5 (:149-153).
- **Conflicts / stale:** Counts as of c8cc408; re-run the section-5 script. [UNVERIFIED]
- **Open items:** W-1 material decision; W-2 parry floor intent; W-3 recovery tail measurement.

### proposals/2026-09-30-character-and-play-surface/07_saying_a_weapon_is_good.md
- **What it is:** How to state a weapon's quality to a player without a fixed number: contribution vs outcome terms, measured table, phrase-to-term mapping; PC (presentation). [READ IN FULL]
- **Status:** "PROPOSED (2026-09-30)" (:3). Reading: live reference.
- **Bears on:** PC, GO, CHAR.
- **Content that matters:**
  - Contribution (function of one weapon: `defense_affinities`, `agility`, `lunge_quality`, `leverage`, `weapon_tempo`, `recoverability_factor`, `heft`, `adef_cap`, `spine`, `grab_hazard`) vs outcome (`bind_sigma`, `mode_sigma`, `reach_threat`, `armor_defeat_sigma`, `read_contest`) (:33-41).
  - Measured table of 11 weapons (:49-61); a badly balanced blunt arming sword is 2.2x worse in recovery, 10% slower, and still clears plate (armour-defeat 1.167) because material is inert (:72-99).
  - "Well balanced" lives in `recoverability_factor` and `weapon_tempo`, not in parry/dodge/wind (:121-125).
  - Phrase as suitability for one of the nine moments; publish a band not a number (precedent S6) (:101-141).
  - Recs C-1 `weapon_card`, C-2 phrase vocabulary as YAML under `references/` with quantile bands, C-3 suitability grammar, C-4/C-5 ordering behind W-1..W-3 (:147-151).
- **Conflicts / stale:** none beyond point-in-time numbers.
- **Open items:** number of bands; blocked on 06 W-1/W-2/W-3.

### proposals/2026-09-30-character-and-play-surface/08_mass_battle_units.md
- **What it is:** What unit kinds `systems/mass_battle/sim/` supports, what builds armies in the season loop, and how units should be composed; MB with PC. [READ IN FULL]
- **Status:** "PROPOSED (2026-09-30)" (:3). Reading: live reference; ED-MB-0068 reference suggests partly dated.
- **Bears on:** MB, CHAR, SE, CORE.
- **Content that matters:**
  - Ten troop types with power/discipline/morale presets (levy 1/1/2 ... knights 5/6/6); `mounted_archers` has none; armour and stamina deliberately unbridged (:18-38).
  - Reach 0.1/0.2/0.3 (P-DEC-1); shapes Line/Arrowhead/GappedLine/Column with min discipline 1/4/5/3; `TROOP_TYPE_ROLES`/`ROLE_SPEC` marked "SCAFFOLD — data only; INERT" (`config.py:568`) (:42-52).
  - `TROOPS_PER_TIER {1:100,2:200,3:400,4:800}`; rout stochastic at 15-30% losses; facing octagon front 1.0 / flank 1.5 / rear 2.0 (ED-MB-0018) (:56-66).
  - Equipment catalogues `equipment/weapons.py`, `armour.py` say "NOT YET WIRED" (:69-76).
  - In the season loop `_weighted_unit` (`massbattle.py:283`): troops = summed `Person.weight`, power fixed 4, morale fixed 5; 37 weight-2 cohorts in `cohorts.yaml`; `march` never attempted in the 143-case corpus (:80-91).
  - Recs U-1..U-6; unit = composed from persons, loadout, officer, role, derived kind (:104-130).
- **Conflicts / stale:** Says `_faction_to_unit` morale from `Sta` "since ED-MB-0068"; synthesis (2026-09-25) said the formula was hardcoded 5/5 and "never implemented" - read both. Roles marked INERT here although synthesis A5 builds role instincts.
- **Open items:** levy/professional `Muster` split (X4) needs Jordan if pursued.

### proposals/2026-09-30-character-and-play-surface/09_the_character_sheet.md
- **What it is:** Census of what `Person` carries and where each character fact lives across subsystems; proposes one reconciled sheet; IN with PC, WR. [READ IN FULL]
- **Status:** "PROPOSED (2026-09-30)" (:3); README: the character sheet ratified as intent via IN-47, K-3 ratified, K-2 only with first reader. Reading: live as intent.
- **Bears on:** CHAR (primary), PC, MB, WR, CORE.
- **Content that matters:**
  - `Person` fields: id/name/weight, body, capability dict, stance rows `(referent, valence -5..+5, weight 0..5)`, pursuits, scar, ledger of Claims, travel_leg, tenures (eight kinds incl. `reside`) (:19-31). Nothing in a season writes `capability` or `pursuits`; only `march` writes `stance` (:33-34).
  - Capability: `verb_capability` maps only `tell` and `speak` to `copying`; empty for most persons, so social contests vary by seed not person (:38-45). Repair named in repo: "a `practice` verb, not a field".
  - `Combatant` is built with exactly one field from the person (`end`); tradition/techniques/weapon/armour do not exist between fights (:47-55).
  - Ledger is the complete part: claims enter only at WITNESS; no claim = unknown not negative; eviction `confidence x (when+1)`; decay at MATTER (:59-66).
  - Attribute roster owned by `descriptor_registry.yaml`: nine named (Strength, Endurance, Agility; Focus, Acuity, Will; Attunement, Charisma, Bonds), ten ruled (ED-IN-0193), tenth unnamed (plan D2); Thread Sensitivity / TPS ratified (ED-IN-0029); no carrier holds any attribute (:70-92).
  - Recs K-1..K-7: build Combatant from Person; unseeded `attributes` dict (K-2); `coherence` + `thread_sensitivity` on Person (K-3); `practice` verb as capability's writer (K-4); loadout as `hold` tenures (K-5); command from the person (K-6); store no rank (K-7) (:128-134).
- **Conflicts / stale:** Says 13 convictions -> 4 axes (:27), which the 2026-09-20 pursuit worksheet changed to 15 pursuits -> 7 axes; verify which landed. [UNVERIFIED] Rank "stored nowhere" vs standing.
- **Open items:** tenth attribute name (D2); loadout (OPEN); `Recall` has no registry name.

### proposals/2026-09-30-character-and-play-surface/10_verbs_and_attributes.md
- **What it is:** Reads the 44-row `verb_table.yaml` four ways (stratum, function, draw, etymology) to decide where attributes have work; IN with PC, SC, FI. [READ IN FULL]
- **Status:** "PROPOSED (2026-09-30)" (:3); README: V-1 follows IN-09's `comply` cell. Reading: live reference.
- **Bears on:** CHAR, PC, SC, FI, MB, FA.
- **Content that matters:**
  - Strata: social 15, uncontested_material 13, binding_decision 9, contested_physical 5, movement 2 (44 verbs); stratum is a resolution-order band, not `contests:` (:24-36).
  - Only three verbs contest today (`fight`/body, `march`/field, `tell`/standing); the proceedings design would add seven (speak, determine, examine, interview, research, reconstruct, surveil) (:62-86). comply / evade-defy / construe do not execute today (:51).
  - Rule: attributes reach a verb only through a faculty and only if the row has `contests:`; §E4 bars capability gating a verb and an office adding a modifier (:56-58, :198).
  - Domains by prize: arms, command (`command = round((2*Cha + Cog)/3)` clamp 1-7), standing and the matter (no attribute bound), inquiry (Cognition/Attunement/Recall), substrate (TS >= 30) (:140-146). `Recall` has no registry name (:152-156).
  - Latent name collision: proceedings design's speech kind `construe` vs the verb renamed from `refract` 2026-09-18; live `arrangements.yaml` carries six forensic speech kinds (:112-118, :126-129).
  - Recs V-1 (split evade/defy inside ED-IN-0210), V-2 standing rule, V-3 `faculty(domain)`, V-4 non-combat acquisition layer, V-5 glosses (:197-201).
- **Conflicts / stale:** Counts "44 rows" as of c8cc408.
- **Open items:** ED-IN-0210 (`comply` one verb or two, blocks `19b`); D2; chooser cannot see capability (:186-189).

### proposals/2026-09-30-character-and-play-surface/README.md
- **What it is:** Index and ranked recommendation roll-up of the ten-document session digest, with a corrections table; IN. [READ IN FULL]
- **Status:** "RATIFIED AS INTENT (v9, ED-IN-0290) for S-1, M-1/S-4, S-2/L-1, K-3, U-3, P-1, P-2 and P-3's mechanism; S-6 -> FI-01; V-1 follows IN-09; K-2 only with its first reader; K-4 superseded by IN-12 step 9's `train`; 05 s4.1/4.2 attach to M-2, two modes are Jordan's intent (SM-5), suspension IN-46; character sheet IN-47; the rest reference" (:3). Reading: live (mixed: ratified-as-intent for the listed items, reference for the rest).
- **Bears on:** CORE, CHAR, PC, MB, SC, FI, GO, FA.
- **Content that matters:**
  - Ranked build order: S-1 dispatching `choose`, M-1/S-4 return trace, S-2 per-person projection, B-3, K-2, K-3 first; then P-1 stance rows with cause, P-3 faction heads, P-2 scarcity, K-1/K-5, K-4+V-3, S-6, U-2/U-1, L-3, M-2..M-6 (:42-69).
  - Two Jordan items survive: unwatched fights one act vs span scenes (05 s4.1); does duel mode open any closed moment (rec no). V-1 is evidence for ED-IN-0210 (:85-97).
  - Corrections table: rapier parry affinity 0.70 not 0.93; `shinogi` is Japanese and reaches 25 weapons; 44 verbs not 42; `confer` bestows a seat; 20 `_emit` sites not 22; `refract` renamed `construe` (2026-09-18); ten troop types not eleven (:106-124).
  - Changes in `engine/season/` if taken up: S-1, S-2, L-1, M-1, K-2/3/4, P-1/2/3, S-6, U-1 (:13-17).
- **Conflicts / stale:** K-4 "superseded by IN-12 step 9's `train`" - check `verb_table.yaml` for a `train` verb. [UNVERIFIED]
- **Open items:** tenth attribute name; Godot version; grid mode suspended (see 2026-10-07-grid-mode-suspension).

### proposals/2026-10-03-verb-coverage-and-gap-fill.md
- **What it is:** Six-revision IN-lane analysis (4663 lines, 528 KB) of the 44 verbs of `verb_table.yaml`: etymology, REACH/NOT baseline, coverage vs surveys, a "resolved suite" of 12 new verbs and 7 widenings, states, build order, 56-conflict register, residual decisions R-1..R-9. [READ PARTLY: header/status, section 2 direction, section 7.1 roster table, section 10.4 build order, full heading map; sections 3-6, 8-9, 11-14 and appendices A-D NOT read, SKIPPED for size]
- **Status:** "RATIFIED AS INTENT (v9, ED-IN-0288) — section 7 suite and 10.4 scheduled (IN-10..IN-13, IN-18 step 2a, SC-03a/SC-03b); step 9 (`train`) and R-5(b) (`inheritance`, IN-51) ratified as the plan's recommendation (RS-21) [medium; Jordan to correct]; R-1(b), R-3(b), R-4(b), R-8(b), R-9(a) adopted at the step each names; 13.9's kill/wound reading ADOPTED: `kill` and `wound` are not verbs, `challenge` -> `accept` stay; K-23 NOT ratified, struck by IN-08; 6.1 reference. Nothing exists until built with its test." (:3). Reading: live as intent (build-order source for IN-10..IN-13); merging does NOT ratify verification policy or any verdict.
- **Bears on:** CORE, FA, SC, FI, CHAR, SE, PC, MB, WR.
- **Content that matters:**
  - Jordan direction (not ledgered): fill gaps; `kill`/`wound` are outputs not verbs, a character may only attempt (`fight`); march is "send an army to a place", the stake derived at the destination (capture/intercept/relocate); war is an uttered `WAR`-mood Proposition plus live `commit`s, no war carrier; no `execute`, no `besiege` (:217-310, :23-60).
  - One binding ruling: no faction actor - every faction act is a person's act through a seat (`Act.via`); `rosters.yaml:1026-1029` forbids a faction that acts (:300-305).
  - Suite: 44 + 12 new (`argue`, `arrest`, `conceal`, `covenant`, `forgive`, `interrogate`, `pardon`, `raze`, `sabotage`, `seize`, `tend`, `train`), `repudiate` recommended cut, `steal` and `proclaim` deferred; 55 verbs; 7 of 55 contested (`argue`,`arrest`,`determine`,`fight`,`interrogate`,`march`,`tell`); 7 widened (`confer`,`determine`,`give`,`march`,`oblige`,`survey`,`tell`) (:1286-1376).
  - `remit:dispatch` is granted to 22 of 29 authored seats while J-8 (is `dispatch` a remit act) is unruled (`offices.yaml:82-95`) (:1370).
  - Build order (:2449-2490): step 1 held-Record operand channel; 2 `utter` hold -> `commit` on Propositions, cut `repudiate`; 3 tenure kinds `detain`/`ban`; 4 `determine` contested; 5 `arrest`/`pardon`/`interrogate`; 6 `seize`; 7 `covenant`; 8 the arrival (`march` writes winner/Unopposed, `Person.travel_leg`, occupation Query); 9 `sabotage`/`tend`/`argue`/`train` (un-retire `Person.capability`); 10 `conceal`; 11 `raze`; 13 `forgive`; later `inheritance`; deferred occupation subsistence hole.
  - Each verb added re-records `len(VERB_TABLE) == 44` (`test_governance_build.py:817`, `test_season_shape.py:2246, :13023`) (:2486-2488).
  - Contest prizes/bands: `sigma_leverage` Overwhelming/Success/Partial/Failure; field Declared/Won/Lost/Unopposed (`rosters.yaml:801-817`); body Felled/Wounded/Untouched (`verb_table.yaml:522-525`) (:1290-1292).
- **Conflicts / stale:** Verb count "44" vs the digest of 09/10 ("44") consistent; the pursuit worksheet (2026-09-20) says 38 - 1 + 3 = 40 at an earlier date. Line cites into `test_season_shape.py` will have drifted. The doc says every grade is `assumption`/`absent`, none `ruled`.
- **Open items:** R-1..R-9 (execute, march-winner write [resolved r3], cut `repudiate`, deposing a seat with no rung above, succession basis, `steal`, grudge fade at MATTER); J-8; tests for each step; the doc lists 27+ conflicts K-01..K-56 in section 12 (not read).

### proposals/2026-10-04-forcing-churn-and-the-story-bar.md
- **What it is:** IN-lane NERS pass on what the engine needs beyond persons-on-a-passive-substrate: outside forcing, transmission to decisions, bounded escalation, a story bar; 2026-10-04, with scratch measurements. [READ IN FULL]
- **Status:** "RATIFIED AS INTENT (v9, ED-IN-0287) for the section 4 handles whose class is not held; FORCE-BODIES, FORCE-FOREIGN, END-VICTORY and CAST-DISPOSITION's capability writer ratified as the plan's recommendation (RS-21) [medium]; CAST-POPULACE NOT ratified; section 5 cuts stand; section 6 superseded by v9's order; section 7 item 1 answered [medium] (the Calamity is tensile, D-3), item 3 answered (a dated pin is a clock, T-c), item 5 is IN-06" (:3). Reading: live as intent.
- **Bears on:** CORE, WR, FA, SE, CHAR, MB.
- **Content that matters:**
  - Diagnosis: persons-only agents on a passive substrate; a system with no forcing and damping loops converges (ID-16); `season_factor` is constant 1.0 (`data/fixtures.py:399`); no code names drought/rainstorm/calamity/empire; plan schedules only hunger `24g` (:42-70).
  - Nine Jordan drivers (weather/food, empire, Church theocracy, monarch+dukes, Einhir heresy, Calamity, ambition, Schoenland trade, succession) classed outside/inside against what is built (:74-86).
  - Handles: FORCE-WEATHER (keyed seasonal draw on yield, control = `season_factor` 1.0 reproduces today's hash), FORCE-BODIES (ageing/illness, birth-tick field), FORCE-HAZARD (Calamity re-expressed as wear coupling, no stored MS scalar), FORCE-FOREIGN (foreign empire and Schoenland as persons using same verbs) (:92-150).
  - Transmission/bounds: CARRY-INTERIOR (stance writers; H-62, J-1), CARRY-SHORTFALL, CARRY-STABILITY (Query not stored), BOUND-LOOPS (signed LOOP row per amplifier; H-106 derived check unscheduled), BOUND-STAKES, BOUND-ATTENTION (office-holder's sixth scene unspendable, `deliberate.py:84-111`, H-92), BOUND-PAPER, STORY-BAR/READ/SOAK, CAST-POPULACE, CAST-DISPOSITION, SEAM-LADDER (one degree ladder), SEAM-CLOCK (season as unit), END-VICTORY (:155-172).
  - Measured baselines (scratch, tree d686eb8): 649-734 acts/season over 83 persons; 66% of acts end in refusal kind; 22 of 44 verbs ever succeed; 91% of events are claim deposit/decay; cross-person antecedent share 9.3%, chain depth max 5; stores grow with no sink; per-season wall time 13 s -> 169 s; ledgers hit the 200-claim cap (:225-243).
  - Cuts: stored MS scalar / stability value, scripted invasion, hazard-rate thresholds producing outcomes, weather module wrapper, lattice-node site kind, arc/story carrier inside the sim (ED-IN-0225) (:177-186).
- **Conflicts / stale:** Plan `workplans/valoria_master_workplan_v8.md` cited as the one plan (:11); likely replaced since (see `workplans/2026-09-28-...`). Figures are scratch and uncommitted. Calamity baseline sign flagged [UNVERIFIED that code and trajectory document reconcile].
- **Open items:** Jordan items 2 (ageing in J-6 scope), 4 (foreign cast content incl. T16), 6 (ending vocabulary GD-1/H-176); the M2 instrument has none (STORY-BAR proposed).

