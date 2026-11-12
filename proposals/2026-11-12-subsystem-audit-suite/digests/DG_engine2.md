# Digest engine2

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane engine2: `engine/season/` seam, state, rosters, verb table, write matrix. Method: every assigned file read in full to its last line (windows of 650 lines for the large ones). Line references are to the file as read on 2026-11-12. Finding ids `F-CORE-NN` are those of `audits/01_CORE_audit.md` and its addenda B and C.

### engine/season/rosters.yaml
- **What it is:** the single data file of every closed set, table and fixture-adjacent definition the season loop reads at import (4547 lines, 2 top-level keys: `rosters:` from :99 and `tables:` from :3507); ruled by Jordan 2026-09-02 ("I do not want definitions etc to be hardcoded", :3-:11); read by `data/rosters.py` (`roster()` returns a frozenset, `table()`/`roster_map()` a dict; an absent name raises, :34-:36).
- **Status:** none (a YAML data file; its header says every roster is `open: true` unless stated, "provenance, NOT ratification", :95-:97). Reading: live mechanism (code opens it at runtime, CLAUDE.md §0.05), but much of its prose is a change-log in comment form, and a number of rows are `[ASSUMPTION; medium; Jordan to correct]`.
- **Bears on:** CORE, CHAR, PC, MB, SC, FA, SE, FI, WR.
- **Content that matters:**
  - The ruling and the shape rule: a number that is a property of a roster member lives here (`alignment`, `pursuit_projection`, `wear_per_season`); a free-standing scalar is a `Fixture` (`data/fixtures.py`), :17-:28. Source precedence for world vocabulary: world > factions (identity only) > npc_behavior supersedes faction_politics > research > governance_play_redesign (:46-:93).
  - Tenure kinds are ten (`hold, contain, commit, oblige, succeed, tie, knot, reside, detain, ban`, :130); `succeed`, `tie` and `knot` have no opener effect (holes still true, :142-:146, computed by `data/verbs.py::_derive_openers_from_effects` by AST scan of `effects.py`). `reside` vs `contain` = where one lives vs where one is (:105-:114).
  - `record_kinds` (:179-:285): exact key sets per kind (`Record.__post_init__` refuses both missing and extra keys); kinds: text, dispensation, petition, works, faction_sheet, cover, army, challenge, order_of_battle. `army` keys equal `modules/mass_battle/armyrecord.py::KEYS`, held equal by a test, not an import (:243-:246). `order_of_battle` deliberately drops two of the home's five keys (:261-:266).
  - Epistemics as data: `witness_channels` is ordered by precedence (co_located, witness_key, document_key, chronicle, post_remit) with `claim_source` per channel (:410-:456); only three of five channels can admit anyone in a buildable world (chronicle matches nobody; :1240-:1246); shipped fan-out arm is `all_five` (:1233-:1237). `observation_terms.supplied_by` (:1313-:1318): no channel supplies `why`, so "no discernible reason" is every deposit (:1302-:1305); `document_key` shows nothing.
  - Combat/field degree as READS of the engine: `combat_degree_bands` Felled/Wounded/Untouched with edges `{felled>0}`,`{wounds>0}` (:941-:1062); `field_degree_bands` Declared/Won/Lost/Unopposed/Invested (:1099-:1119); `wound_harm_models` default `scene_fraction`, `field_casualty_models` default `scaled_by_degree`, both flagged as invented magnitudes (:1065-:1147). `duel_terms` `{capture: yield, accept: blood}` (:1018-:1020), `challenge_terms` [yield, blood, death] held equal to `modules/combat/wrapper.py::DUEL_TERMS` by a test (:1029).
  - The contest dispatch (`contest_subsystems.prizes`, :1676-:1732): "the body" -> combat (step ENCOUNTER, declares Declared), "a field" -> mass_battle (ENCOUNTER), "a standing"/"a proposition"/"a matter" -> social_contest (sigma-leverage roll `social_contest.roll`, `heard_by: bench` for a matter). `graded_inquiries` routes research/examine/surveil to the SAME `social_contest.roll` (:1433-:1435): investigation is graded by the social roll, not a fieldwork roll. `inquiry_modules` routes `finding.made` to `fieldwork.find` (:3303).
  - Seam table in comments (:1368-:1376): faction management and character development are listed as UNRULED / "absent from the loop entirely" (:1375-:1376). `[UNVERIFIED]` whether still true; the table is a dated comment, not a mechanism.
  - Capability/attribute: `verb_capability` maps tell/speak->copying, argue->argue, research/examine/surveil->inquiry, fight/accept/capture->arms (:1542-:1550); `vocation_attribute` copying->focus, argue->charisma, inquiry->acuity, arms->agility (:1606-:1609). The file says capability is "nearly inert on the corpus" (1 of 430 built persons held one, a dated count, :1513-:1520) and `arms` is held by nobody at landing (:1538). `lifepaths` = 34 ids with `lifepath_templates` mapping each to 0 or 1 of {argue, inquiry} (copying held by none; :3628-:3661): most lifepaths grant nothing (about 22 of 34 have `holds: []`).
  - Decision-side declines as rosters: `own_hold_declines` [destroy_record, give], `own_title_declines` [succeed], `held_edge_declines` {commit: commit}, `violence_contexts` {fight: [war, crime, duel, defence]} (:2743-:2771; ED-IN-0336/0337 "fighting is exceptional"), `violent_prizes` ["the body"], `lie_verbs` [lie], `own_stance_declines` [forgive], `army_verbs` (six verbs, all in `withheld_verbs` so no NPC forms them, :2680).
  - Alignment table (`tables.alignment`, :4014-:4546): verb x seven bipolar axes; `selfish_selfless` carries no non-null cell by design except `fight`/`accept` at -0.3 (:4137-:4145, :4352, :4377); the whole column `fight`/`accept` is -0.3 on every axis (CR-87, ED-IN-0340). `uncelled:` lists 17 verbs with no lean on any axis (recruit, form_unit, assign_troops, order_unit, disband_unit, discharge_troops, covenant, argue, sabotage, tend, train, conceal, forgive, interrogate, arrest, capture, pardon, raze, marshal, surrender, tell; :4032-:4118): they score 0.0 so the chooser is indifferent to them on pursuit.
  - `pursuit_projection` 15x7 (105 cells, :3853-:4012), `role_template_pursuits` (:3775-:3851), `affiliation_engagement` (:3706-:3771; scar is nearly inert, :3747-:3752), `incompatible` pairs (5 of 10 null, :3669-:3698).
  - `endings` (:3418-:3477): `peninsular_sovereignty` (victory, rung_kind territory under one faction) and `theocracy`; the file itself says peninsular_sovereignty is UNREACHABLE IN COMPUTED PLAY (`terr_T15` uncontrolled, no verb opens a `hold` on a territory, :3460-:3462), and the loop only reports endings, never halts.
- **Conflicts / stale:**
  - Dead: `knowledge_kinds` (:1763-:1777) has NO reader in any `.py` under `engine/season` (grep `KNOWLEDGE_KINDS`/`knowledge_kinds` = nothing); its own note says "no code reads this roster" (:1771-:1772). `genres` is read only by `data/arrangements.py` to validate `speech_kinds` rows; its note says nothing derives genre (:3172). `fight_endings` is read at import, used in `loop/effects_combat.py`.
  - Doubled: the faction head exists twice, `faction_leaders.by_faction` (person NPC-ids, :2137-:2148) and `factions.head_seat` (seat ids, :2062-:2066), two mechanisms for one fact; `faction_leaders` is a hand transcription of `faction_state_authoring_v30.md` slugs (:2111-:2115). `foreign_factions` [Altonia, Schoenland] (:3412) and `foreign_cast` (Altonia only, :2181) and `factions` (from `names_index.yaml`, :2057) are three surfaces for the foreign set. `strife_kinds.lists` hand-maintains a `concludes` list checked by a test (:3373).
  - Hard-coded in a roster that the file's own rule says belongs in a Fixture or code: `modules.members` homes (:3238-:3256) are `systems/<x>/` paths for a tree with no `.md` (CLAUDE.md §3), and `victory` home `engine/season/` is a stub.
  - Header says `keys.py::AXES`/Key substrate is outside the chain (:38-:44); CLAUDE.md §0 says the Key substrate is RETIRED (ED-IN-0232): the header sentence is stale. The `pursuits` note cites `engine/substrate/keys.py::AXES` as a reader (:575-:588).
  - Many comments cite `tools/balance_oracle.py`-style instruments: `field_casualty_models` note (:1139-:1146) correctly says it is retired/inapplicable; consistent with CLAUDE.md §7.
  - `remit_default` is explicitly a TEST FIXTURE that hands every seated office every remit act (:355-:407) yet sits in the shipped roster file: the governance verbs are exercised on it. Compare F-CORE-13/F-CORE-18 (verb facts spread across rosters).
  - Several `values` are YAML-1.1 hazards handled by quoting (`"off"`, :1157, :2907, :2932); a fresh roster with `on`/`off`/`no` keys will silently become a boolean.
- **Open items:** `remit_default` owed replacement by per-post remits needing `Office.post` normalised (:382-:389, post field fuses post and scope); `arms_kinds` and `arms_at_build` are EMPTY ON PURPOSE (Jordan's content, :1849, :1861), so no person has equipment and every fight uses the Combatant default kit; `march_postures` shipped `[storm]` so `besiege` never forms (:1169-:1175); `weights`, `works_cost`, `site_yield`, `band_floors`, `wear_per_season` are invented magnitudes with sweeps; `site_kinds` `garrison`/training sites have wear 0 (:1913-:1916), `H-165` open; GD-1 clauses (Accord, Stability, sustain) not carried (:3455-:3465); `proofs` known-thin (:3182-:3186); `H-111`'s strict skip means a failed inquiry teaches nothing and the same person re-forms it (:1452-:1457).

### engine/season/seam/__init__.py
- **What it is:** package docstring and re-export surface for the contest seam (`contest`, `ladder`, `wrappers`), ED-IN-0206 / plan unit L2.
- **Status:** none (code). Reading: live.
- **Bears on:** CORE, PC, MB, SC, FI.
- **Content that matters:**
  - The seam package is `contest.py` (dispatch, `grade()`, `find_trail()`, `contest_subsystem()`), `ladder.py` (`degree_of`, `combat_degree`, `party_degree`), and `wrappers/*` that "own nothing, ever" and return a `Margin` (:1-:18, :61-:63).
  - `from . import wrappers` is what REGISTERS the providers via `@provider(...)`; omitting it silently shrank `resolvable_verbs()` from 18 to 17 and `tell` executed zero times (dated measurement, :49-:59). Since plan position 30 `manifest.check_contest_prizes()` refuses an unregistered prize provider at `SeasonDriver` construction (:56-:58). Registration by import side effect remains.
  - `__all__` is derived by predicate, not listed, to satisfy `test_jordan_no_definition_is_hardcoded_in_a_body` (:65-:73).
  - `PATH_SEAM_ALLOWED` entry and the `sys.path` seam into `modules/combat` are tied to `wrappers/combat.py`; the guard follows relative imports only, so an absolute import would silently stop the scan (:31-:36).
- **Conflicts / stale:** dated counts ("17 instead of 18", :52) are stale snapshots. Says FI wrapper "called by find_trail()" (:10): consistent with `fieldwork.py`.
- **Open items:** none.

### engine/season/seam/wrappers/_entry.py
- **What it is:** 33-line leaf: `entry_for(prize, module, module_entry)` looks up the registered module entry in `manifest.registrar.MODULE_ENTRIES`.
- **Status:** none (code). Reading: live.
- **Bears on:** CORE, PC, MB, SC, FI.
- **Content that matters:**
  - Returns `(entry, None)` or `(None, {"status": "ENGINE-UNAVAILABLE", ...})`: the typed refusal when a provider is reached before any driver was constructed (:19-:33). The registrar fills `MODULE_ENTRIES` only at `SeasonDriver` construction (:3-:6), so module state is process-global.
  - `module_entry` may be named directly by a `graded_inquiries` route; otherwise it is read from the prize row (:25).
- **Conflicts / stale:** none seen. The module-global `MODULE_ENTRIES` means two drivers with different composition rows in one process share one table `[UNVERIFIED]`.
- **Open items:** none.

### engine/season/seam/wrappers/fieldwork.py
- **What it is:** the `inquiry`-role provider `find` and the host input builder `fieldwork_input`, FI-02/FI-03 (ED-FI-0002, SM-3).
- **Status:** none (code). Reading: live.
- **Bears on:** FI, CORE, WR.
- **Content that matters:**
  - `fieldwork_input` builds `FieldworkInput(band=event.degree, items=<trail Events: id, kind, emitted_at>, terms=dict(FINDING_TERMS))` from `epistemic.trail_of(w, refs[0], act.actor)` (:49-:60). The trail is only what `trail_of` can find; only `record.forged` is a covert kind today (rosters.yaml:3346).
  - `find` calls the module entry `fieldwork.find` and raises `Unspecified` if the return is not `Findings` (:63-:80). Placement deviation from Layer 1 is stated three ways at :14-:27 and "recorded and NOT made" (Layer 1 amendments owed).
  - It decides nothing about WHAT is found (module's) or what the finder then holds (WITNESS's found deposit, `SeasonDriver.findings`, a driver-held store outside `loop/witness`'s may-read column, :23-:25).
- **Conflicts / stale:** the three Layer-1 deviations are open amendments; compare F-CORE-16 (Layer-1 conformance of the verb table) and F-CORE-13 (one module a scene, three calls) for the same family. `refs[0]` only: an inquiry naming several referents uses the first `[UNVERIFIED whether act_refs can return more than one for an inquiry]`.
- **Open items:** Layer 1 §A.2 amendments for a second role's adapter, a `findings` store, and `find_trail` returning pairs (:25-:27).

### engine/season/state/__init__.py
- **What it is:** 17-line package docstring; imports nothing, deliberately.
- **Status:** none. Reading: live (documentation only).
- **Bears on:** CORE.
- **Content that matters:**
  - Layering is one-way: `ids` imports nothing local, `carriers` imports `data` and `gaps`, `world` imports `carriers`; nothing imports `shape`, `queries`, `decision` or `loop` (:13-:16). An eager import would make seven modules parse two YAML registries and be able to `SystemExit` at import (:7-:12).
  - Lists "sixteen things the world holds" (:4).
- **Conflicts / stale:** mentions `shape` as a module (:15); `shape.py` was deleted at step 10 of the decomposition (carriers.py:7-8). Stale reference.
- **Open items:** none.

### engine/season/state/acts.py
- **What it is:** `ActStore`, the append-only store `causes[]` resolves against (122 lines).
- **Status:** none (code). Reading: live.
- **Bears on:** CORE, WR.
- **Content that matters:**
  - `append` is idempotent on an EQUAL act (dataclass equality), refuses a DIFFERING act on a live id with `Unspecified` (:49-:99). Reason: `W17` control arm folds four `speak` acts by one actor with the same mint `H(seed, tick, actor, "act:verb:key")`, which carries no draw ordinal, so ids collide (:74-:82).
  - The id collision is REAL, predates the store, and is explicitly NOT fixed here because changing the act mint moves every golden (:79-:83). Event ids derived from `a.id` collide with it.
  - The store has no remove/clear/setter; `__iter__` yields from a tuple copy (:21-:24, :111-:116).
- **Conflicts / stale:** the docstring's `resolve.py:395` citation (:18) is a line number; `[UNVERIFIED]`. The act-id collision is a standing latent defect: an equal act under a colliding id is silently deduplicated, so two distinct but equal `speak` acts in one tick count once.
- **Open items:** give the act mint a draw ordinal (own re-record, :82-:83).

### engine/season/state/attribution.py
- **What it is:** `actor_of`, `causing_act`, `anchor_of`, live-cover reads and `matured_terms`: who acted and what an Event is about, after `Event.subject` was deleted (G1b).
- **Status:** none (code). Reading: live; owner of attribution.
- **Bears on:** CORE, FI, SC, WR.
- **Content that matters:**
  - `anchor_of` has three tiers: the causing act's actor (or its LIVE COVER id), the first `changes[]` entry with a subject, then the cause's anchor; otherwise `None`, which every reader treats as absence, so an emitter that drops its change silently vacates its witness channel (:57-:64, :105-:153).
  - A concealed identity: `live_cover` returns the min id of a held `cover` Record whose `terms` names the actor and which has an unmatured stage (:183-:217); a logged Event's anchor is frozen at logging in `World._covers_logged`, assumed to be the end of the round's fold, so a cover taken in a round covers every act of its taker logged with it, including acts resolved before the `conceal` (:164-:168, [ASSUMPTION; medium]).
  - `matured_terms` counts `term.matured` Events in the log by change subject (linear scan; the log is the carrier of "how many stages ripened", :238-:263). `event_by_id` is a linear scan, deliberately not indexed (:266-:277).
- **Conflicts / stale:** `event_by_id` and `matured_terms` are O(n) over the log and called from `anchor_of` tier 3 and `live_cover`; compare F-CORE-09 (per-access scans on the hot path) which this confirms as a mechanism `[timing UNVERIFIED]`. Dated measurement counts (1,428, 3,411, 90 events, :29-:45) are historical.
- **Open items:** `None` anchor is silent; the only instrument is `test_g1b_attribution.py` (:57-:64).

### engine/season/state/containment.py
- **What it is:** the containment-tree reads moved down from `queries/world_q.py`: `parent_of`, `descendants`, `home_of`/`home_map`, `ancestry`.
- **Status:** none (code). Reading: live.
- **Bears on:** CORE, FA, SE.
- **Content that matters:**
  - Each of the four walks is a linear scan of `w.tenures` per call; `parent_of` loops all tenures per step (:33-:37), `ancestry` calls it per ancestor (:128-:134), so a depth-d ancestry is O(d x tenures). `descendants` builds a children dict once per call (:46-:49).
  - `home_of` is "last write wins" for a person with two live `contain` edges, which `add_tenure` does not forbid (:87-:89). The 4 hand copies it replaced fed `tools/export_npc_roster.py --check`.
  - Traces: `home_of` and `descendants` write `TRACE.query` rows; `ancestry` deliberately writes none (:121-:127).
- **Conflicts / stale:** `queries/cache.py::home_index` is a barrier-scoped copy of `home_map` (:94-:97), a second index of the same fact, flagged by the file itself. See F-CORE-09.
- **Open items:** none.

### engine/season/state/ledgers.py
- **What it is:** `eviction_key(confidence, recency) = confidence * (recency + 1)` and `evict_over_cap`, the claim-ledger eviction comparator (32 lines).
- **Status:** none. Reading: live (called by `loop/witness.py`).
- **Bears on:** CORE, FI, CHAR.
- **Content that matters:**
  - Eviction ranks on the PRODUCT `confidence x (recency+1)` only, never salience (S20/S34); the lowest goes first (:17-:21). A claim a person is told early with high confidence and a fresh trivial claim are on one scale.
  - The store split (claim rows in a separate sub-store with their own write token, `04:117`) is NOT done: `Person.ledger` stays on the carrier and eviction goes through `World.write(... "claim_ledger" ...)` (:8-:13).
- **Conflicts / stale:** `rosters.yaml` `claim_subject_rules` note says the cap "evicts on `(confidence, recency)`" (rosters.yaml:898), and `carriers.py:330-331` shows `c.confidence * (c.when + 1)`; the product is the code. The roster comment's tuple wording is imprecise. Eviction is a bounded memory of `ledger_cap` claims per person: in the CORE audit this is F-CORE-01 (log mostly memory-fade).
- **Open items:** the G2 token-type rewrite that would split the store (:8-:11).

### engine/season/state/log.py
- **What it is:** `EventLog`, append-only, refusing foreign receipts and unresolvable causes (140 lines).
- **Status:** none. Reading: live.
- **Bears on:** CORE, WR, FI.
- **Content that matters:**
  - Two assertions at `append`: every `Receipt` on `changes[]` was minted by `Gate.issued`, and every cause is ROOT, a logged Event id or an act id (:7-:15, :71-:96).
  - A bare `StateChange` is still ADMITTED (only `Receipt` is verified), "the file's weakest seam ... stops the accident, not the adversary"; `G4` is where it should stop (:24-:31). `harness/probes.py:1797` builds one outside any gate write.
  - `__contains__` is a list scan (:119-:120); `has_id` is O(1) via `_ids` (:122-:126). `extend` routes through `append` one at a time (:128-:137).
- **Conflicts / stale:** `world.py:625` and `harness/corpus_run.py:565` line citations are stale-prone `[UNVERIFIED]`. The unchecked bare-`StateChange` admission means "changes[] is a record of writes" holds only for Receipt-carrying Events; relevant to F-CORE-17 (a refusal is priced and leaves no receipt) as a neighbouring provenance gap.
- **Open items:** G4 to refuse bare `StateChange` (:30-:31).

### engine/season/state/carriers.py
- **What it is:** the sixteen world carriers as dataclasses: `Term`, `Tenure`, `StateChange`/`Receipt`, `Event`, `Claim`, `Said`, `Sensation`, `View`, `Question`, `Candidate`, `Scene`, `Act`, `Person`, `Site`, `Record`, `Proposition`, `Office`, `Rung`, plus `matrix_rows_without_a_field` (1253 lines; extracted from `shape.py` at step 4, ED-IN-0203).
- **Status:** none (code). Reading: live; the typed schema of the world and the hash domain (`World.content_hash`).
- **Bears on:** CORE, CHAR, FA, SE, FI, SC, PC, MB, WR.
- **Content that matters:**
  - `Person` fields (:737-:852): `weight` (cohort when >1), `capability`, `stance` (list of tuples), `pursuits`, `ledger`, `body`, `body_ceiling`, `born` (age = `w.tick - born`, never stored), `scar` (`{element: count}`), `conviction` (`{affiliation: 0-5}`), `thread_sensitivity` (None = unauthored, gate reads UNKNOWN so unscreened persons cannot attempt), `attributes` (ten registry keys 1-7, SHIPS EMPTY because `cast_attributes` switch ships OFF, :813-:815), `heritage`, `travel_leg`, `tenures`. There is no `needs`, `skills`, `traits`, `age` or `goal` field: character state is these dicts.
  - `Tenure` counts every attribute set in `_v` for the world's snapshot diff; payload carries the remit grant (`granted_acts`, `seat_rung`) as a SNAPSHOT at seating (:75-:192); `Term(matures_at, declared_by)` is a declared end that MATTER matures (:42-:68). `Tenure.payload` has an untyped dict "grant" convention (`seat_rung` graded CONVENTION, :183-:187).
  - `Event` has `observed` (what the fold READ) and `ending` (per-party fight ending); `Event.__post_init__` refuses empty `causes` (:314-:320). `ending` is documented "NO PRODUCTION READER EXISTS" (:305-:307); producers are `loop/effects_combat.py::fight_ending` and `loop/resolve.py:988-990`; I found no reader outside the hash and tests `[UNVERIFIED, one grep]`.
  - `Claim` holds `chain` (tellers, origin first), `doer`, `visibility` ("own" or a circle tuple), `round`; `teller`, `hops`, `firsthand` are derived (:323-:399). `Said` is the NamedTuple passed in `Act.payload["said"]` (:402-:417).
  - `View` forbids world access by type (`__getattr__` raises `Forbidden`) and carries `questions`, `odds` callable; the standing-occasion stamps ride the HEAD question only, so a View built on a later question forms no classed-referent rows (`confer`, `succeed`, `commit`, `interrogate`; :489-:493).
  - `Scene.slots = sum(1 + effort_of(a))`, `cost(extended_cost)` = extended when slots>1 else 1 (:641-:654). `Act` carries `via` (SeatId), `stratum` (default 4 doubling as the "nothing declared" sentinel, :688-:702), `obstacle`, `pool`, `scene`.
  - `Office` (:1018-:1155) validates remit acts, faction/body (`office_faction`), conferral, revocation, binds and upkeep at construction; title-in-body is refused; `scope_rung` is kept because `judging_set` reads it. `Rung` is a whitelist class over `{id, kind, stores, sites, records, dates, envelope, yield}` (:1160-:1216); `sites`, `records`, `dates` have zero readers by the file's own account (:1176-:1183).
- **Conflicts / stale:**
  - `Act.stratum` default doubles as sentinel: "19 of the 32 verb-table rows" carry a non-social stratum, so an explicit `stratum=4` is overridden; "latent, not live" (:688-:702). Dated count (32 rows) is stale (verb table is larger now `[UNVERIFIED]`).
  - Dead or near-dead fields documented in place: `Rung.sites/records/dates` (:1176-:1183), `Event.ending` reader, `Candidate.why` removed, `Person.attributes` empty at ship (:813-:815), `Person.thread_sensitivity` mostly None; these bear on F-CORE-23 and the character lane (the creation sheet writes nothing, :813).
  - `Claim.round` docstring cites eviction as `c.confidence * (c.when + 1)` while `ledgers.eviction_key` is `confidence * (recency+1)` with `recency = c.when`: consistent. `View`'s `k` cap is the roster `view_k`.
  - The title-in-body function docstring is partly history ("kept as history", :999-:1008).
- **Open items:** `Act.stratum` sentinel fix needs a schema change (:700); `Rung.sites/records/dates` removal blocked by Layer-1 text (:1176-:1183); View later-question classed stamps (:489-:493).

