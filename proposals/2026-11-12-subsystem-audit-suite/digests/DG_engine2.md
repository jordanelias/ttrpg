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
  - Capability/attribute: `verb_capability` maps tell/speak->copying, argue->argue, research/examine/surveil->inquiry, fight/accept/capture->arms (:1542-:1550); `vocation_attribute` copying->focus, argue->charisma, inquiry->acuity, arms->agility (:1606-:1609). The file says capability is "nearly inert on the corpus" (1 of 430 built persons held one, a dated count, :1513-:1520) and `arms` is held by nobody at landing (:1538). `lifepaths` = 34 ids with `lifepath_templates` mapping each to 0 or 1 of {argue, inquiry} (copying held by none; :3628-:3661): 21 of 34 lifepaths grant nothing (`holds: []`), 13 grant one key (argue or inquiry), none grants copying.
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

### engine/season/state/gate.py
- **What it is:** the write gate: `Gate` (receipt mint), `Token`, the F3 tenure-write bases (who may write another's edge), the F9 no-op refusal (`Change`, `Subject`, `NoOpReceipt`), and the seat-authority predicates the preconditions share (1932 lines).
- **Status:** none (code; header cites `04 §C.2` Layer 1). Reading: live; the single owner of "which basis admits a tenure change".
- **Bears on:** CORE, FA, SC, PC, MB, WR.
- **Content that matters:**
  - Fourteen named bases (`tenure_write_basis`, :1137-:1481): T-m (owner), T-n (matured term, actorless closure), T-o (revocation through `Act.via`), cascade, conferral, claim (heir), handover (`give`), renewal (upkeep), determination (bench), warrant (`arrest`), seizure, muster (`march` arrival), cession (surrender), founding (newborn rung's `contain`). Layer 1 `04 §C.2` enumerates only nine and is declared stale ("not edited here", :157-:164, :244-:252).
  - Authority is asked of the SEAT exercised (`Act.via`), never the actor: `seat_hold` (:345), `purview_reaches` (own rung or descendants, plus ONE EDGE of vassalage via `oblige`, non-imposed, :386-:461), `sits_over` (a bench's `scope_rung`, not `rung`; the two differ for an untitled ranked seat, :899-:919).
  - Remit acts keyed to bases are fixed strings: `WARRANT_ACT = "dispatch"`, `SEIZURE_ACT = "issue"`, `MUSTER_ACT`, `CESSION_ACT` all = `dispatch` (:289, :305, :326, :342), each `[ASSUMPTION]`, gated by J-8 (per-post remit unruled, `offices.yaml meta: remit_unruled`). `BENCH_BASIS = "determine"` (:260).
  - Dispatch tables checked at import: `REVOCATION_RULES` vs `revocation_bases`, `REVOCATION_DISPOSAL` {appointed: ban, elected/annex/inheritance/None: none} (:653-:654, Jordan 2026-10-21: an appointed seat revoked -> permanent ban), `FILLED_BY` {inheritance: claim only} (:697-:698), `SUCCESSIONS` vs `offices.yaml` (:746-:767).
  - F9: `Change(subjects, apply)` names subjects BEFORE running; `World.write` reads each subject before/after and mints receipts only for those that moved; none moved -> `NoOpReceipt` (:1669-:1683, :1776-:1816). `NO_CHANGE` is the declining effect. Undeclared mutation of a non-Tenure entity inside `apply` is invisible (bound stated :1786-:1799; `H-130`); a body mutation before `Change` is built is caught for Tenures only by `World.effect_body_observed` (CR-06).
  - `Subject.earns` decides which of a row's `emits:` kinds a moved subject publishes; `death_subjects` names the dying person plus each emptied seat (`tenure.closed`); a seat Receipt names the OFFICE, the one receipt whose subject is not the record written (:1751-:1768).
  - `Gate._minted` keeps every Receipt object for the life of the gate (`issued` is an identity check, :1885, :1920-:1929): the mint table grows without bound over a long campaign `[UNVERIFIED memory effect]`.
- **Conflicts / stale:**
  - Layer 1 divergence: bases count (14 here vs nine in `04 §C.2`), gate reads `data/arrangements` against §A.2 (disposition recorded :47-:49). Spec "not edited to match the code" is correct per CLAUDE.md §0.05 but the Layer 1 text is now behind; compare F-CORE-16, F-CORE-11 (two gate conformance gaps filed, verified open).
  - Narrative drift: the module header still describes the receipt window as surviving to the next write (:18-:34) and then corrects it (:36-:42); several docstrings say "`scope_rung` has no reader / `18a` deletes it" then are corrected in place (:397-:401). Dated measurements embedded (532 writes of 2,688, :1622-:1624).
  - `tenure_write_basis` computes `_moved/_closes` twice per change (its own comment says the claimed fix was false, :1510-:1521): known double work on every tenure write.
  - Seat purview is read through `descendants` (a full tenure scan per call, containment.py) in `_ground_reaches` and `purview_reaches` (asked on every purview precondition, :454-:455): see F-CORE-09.
  - Gate cannot ask faction occupation, siege, warrant or Record content (state/ may not import queries/), so each basis is looser than its effect and the EFFECT carries the second half of the licence (seizure, cession): two owners of one licence, deliberate (:1081-:1087).
- **Open items:** J-8 (which posts carry `dispatch`/`issue`) gates warrant, muster, cession, seizure; `H-130` (undeclared non-Tenure mutation); `H-108` (delegation without a `hold`, :354-:360); the `ban` mapping is enforced only for non-judging `via` (:1204-:1208).

### engine/season/state/world.py
- **What it is:** `World`, the store and the one write path (`World.write`), the tenure observation (snapshot/shadow/diff), the death cascade, the last-emission index, and `content_hash` with its canonical encoding (GO-07). 1743 lines, extracted from `shape.py` (ED-IN-0203).
- **Status:** none (code). Reading: live; the single store and the hash the port compares.
- **Bears on:** CORE, GO, WR, FA, SE, CHAR.
- **Content that matters:**
  - State collections: `persons, rungs, offices, sites, records, propositions, dates` (hashed as mappings) plus `docket` (list, positional) plus all tenures sorted by id (:1660-:1665, :1699-:1726). Tenures live on `Person.tenures`; `_unowned` holds those whose subject is not a person (every `contain: Rung->Rung`), `w.tenures` is a read-only `_TenureView` concatenation that raises on every mutator (:112-:141, :455-:471).
  - `World.write(thing, token, apply|change, record_kind, fieldname, driver, ...)` enforces in order: token present and for this tick (`NoToken`, :1225-:1234), apply-xor-change, matrix row exists (`Unspecified`), step allowed (`Forbidden` with the named law from `MATRIX_REFUSAL_LAW`, :1263-:1286), write-class equals token class (:1287-:1293), `social:true` rows only by `driver == "Act"` (:1294-:1300), `(Person, coherence)` only by `Seam` (:1305), actorless `Tenure.until` only for a death or a matured term (:1325), MATTER rows with a declared `emits:` must emit (D22, :1345-:1354), then F3 (tenure bases) then F9 (no-op), then mint and emit (:1379-:1554). Emitted Event id = `H(seed, tick, subject, "emit:kind#draw")` with `draw` the per-tick ordinal `new_draw()` (:1487).
  - Closure writes (`apply=`) are applied UNJUDGED by F9: MATTER/CALENDAR/WITNESS writes that move nothing still trace and still emit; `dwelling` wear 0 is the live example (every dwelling emits `condition.worn` each season, :1163-:1169).
  - Death cascade `remove_person`: closes every live edge naming the person, pops the person and their `person`-kind rung, records `_departed[who] = (rung, tick)` for event placement (:930-:1074); `InstrumentDefect` unless a gate write is open (`gate.is_open`, :1034).
  - Grant stamp: `add_tenure` of a `hold` on an Office writes `{remit_acts, seat_rung}` into `Tenure.payload` once (`_grant_remit`, :798-:880); `establish` re-stamps via `force=True`.
  - Last-emission index: `_last_by_anchor` and `_last_by_subject` maintained on every log append (`_on_logged`, :1606-:1624); `_covers_logged` freezes a logged Event's cover anchor. These maps and `_tshadow`, `_departed`, `_staged`, `_barrier_cache`, `writes` are unhashed derived/ephemeral state; `_departed` is game state "the content hash does not fold" (:432-:437), so a loaded/replayed world would differ `[UNVERIFIED]`.
  - `content_hash` is blake2b-16 over canonical byte encoding; tags N,T,F,U,i,s,f,e,t,l,m,u,z,o (:210-:333); `repr` no longer reaches it. An unknown type raises `TypeError`. `Event.ending` is folded only when non-empty (:1724).
- **Conflicts / stale:**
  - `World.tenures` rebuilds a sorted concatenation of every person's tenure list on EVERY access (`sorted(self.persons)` plus `extend`, :467-:471). Its docstring cites 219 reads inside DELIBERATE and 67,005 inside WITNESS per season on `build_realm(0)` before an earlier repair (:459-:466). Callers (`containment.parent_of/descendants/home_map`, `gate.seat_hold`, `sworn_to`, `in_holdings`) each iterate it afresh. This is the mechanism behind F-CORE-09 (per-access scans on the hot path); the claim "`[timing on the realm UNVERIFIED]`" there stands, the structure is confirmed here.
  - `remove_person` scans `self.tenures` (all persons) per death (:1046); comment concedes it must (edges owned by others naming the dead).
  - Docstrings carry long correction-history paragraphs (e.g. :952-:1033, :1569-:1601) and numeric line citations that the file itself says go stale; stale-by-construction per its own note (:994-:1004).
  - `deepcopy` of a World rebinds `_on_logged` and the `act_ids` thunk; "a World does not pickle" (:387-:392), so there is no save/load path in `state/` (relevant to F-CORE-05 "play surface is a seam with no client" and to any save-game requirement `[UNVERIFIED elsewhere]`).
- **Open items:** closure-writer migration to `Change` (MATTER has no refusal kind for a no-op to become, :1168-:1169); `H-131` open question on closing the window at barrier transitions; `H-130`/`H-137` (undeclared entity mutations); `_rehome` has one caller (MATTER) and no scan guards other steps (:1092-:1110).

### engine/season/write_matrix.yaml
- **What it is:** Part D of Layer 1 as data: 42 rows keyed `(kind, field)` with `steps`, derived write `class`, `social` (L4), `by` provenance, `emits`, optional `unproduced`; plus a `retired:` list (Person.marks, axis_count, Rung.stake, Site.drawers, Person.beliefs, Office.establishment). Read by `data/matrix.py::MATRIX` and `data/verbs.py` (invariant 2).
- **Status:** none (data; header cites `architecture/PLAN.md` W2 and `ARCHITECTURE_V2.md` §D3). Reading: live mechanism (the write gate refuses any `(kind, field)` it does not list, S30); header prose is dated.
- **Bears on:** CORE, PC, MB, SC, FA, SE, FI, CHAR, WR.
- **Content that matters:**
  - Rule: ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION; step determines class (CAL->CALENDAR, MAT->MATTER, RES/DEL->ACTS, WIT->INTERIOR, CEN->MATTER; ENC shares RESOLVE's class, :14-:17, :179). `social: true` rows can be written only by `driver == "Act"` (L4: the world may not sour a mood), enforced in `World.write` (world.py:1295).
  - ENC (ENCOUNTER) was added to many rows by precedent from `march`'s deferral: Person.body, body_ceiling, capability, conviction, exists, scar, stance, travel_leg; Rung.stores; Site.condition; Tenure.since, until (:170, :187, :235, :242, :253, :265, :277, :290, :391, :413, :441, :458).
  - `unproduced:` rows (no verb writes them, loader invariant 2): Person.coherence (H-47/H-62, "only an act may write it and the verb table carries none that does", :206), Person.conviction (written only by the scar-3 crisis in the fold, :247), Person.scar (written by `loop/resolve.py::_scar_witnesses`, :270), Rung.dates (orphan, "no hole row", :374). So Person.coherence has a row, a carrier on nothing, and no writer.
  - Singletons: `(Person, weight)` is CEN-only; `(Person, claim_ledger)` is WIT-only INTERIOR; `(Claim, confidence)` is the third licensed clock (decay); `(Record, ttl)` and `(Record, matured)` are MATTER; `(Record, subject_matter)` is RES and exists only for the `army` kind (:353-:359); `(Tenure, term)` is RES, social true (:449-:455).
  - Emission kinds named per row (`emits:`) are the source of the derived Event-kind roster (`data/verbs.py::EVENT_KINDS`, with `fold_kinds` and `logged_kinds` from rosters.yaml:1460-1496): `person.individuated`, `weight.changed`, `envelope.changed` are emitted only by CENSUS (CEN) rows.
- **Conflicts / stale:**
  - Header cites `engine/season/shape.py`'s `write()` and `python engine/season/register.py --verify-write-matrix` (:4-:6, :29-:31): `shape.py` is deleted and the register lives in `engine/season/harness/register.py` (no `register.py` at `engine/season/`; verified by `ls`). Stale reference. The 11-row / 9-row / 8-row "no producing verb" counts in the header are dated (:47-:70) and the file itself says "re-run the command rather than trust a figure".
  - The header's rule "retire rows with no producing verb" is "false of its own table" (:80-:82): four `unproduced` rows live. Tracked H-41/H-50/H-62.
  - `Rung.dates` is declared in the matrix and on `Rung._DECLARED` with zero writers or readers (carriers.py:1176-1183): a three-way dead row.
  - `Person.pursuits` is written only by `determine`/`argue` (rows pursuit.moved shared, :207-:228); `Person.stance` by `march` (`Won`/`Lost`) and others. Interior-state writes (pursuits, stance, conviction, scar, capability) are all RES/ENC and social-true: nothing moves a person's interior between acts, by L4. This bears on character development (F-CORE-01/12 and the CHAR lane).
  - `retired:` Person.marks is listed by bare string, the others carry `name/reason/needs`: inconsistent shape (:480).
- **Open items:** H-47 (what triggers Person.coherence), H-62 (interior writers), H-41/H-50; `(Rung, dates)` orphan; whether the 42-row table should be generated from the verb table's `writes:` columns (it is cross-checked at load, not derived).

### engine/season/verb_table.yaml
- **What it is:** Part E of Layer 1 as data: the resolver's body. 67 verb rows (`verbs:` list), each with stratum, eligibility, beneficiary, referent_class, requires / requires_typed (a closed predicate grammar), counterparty, contests, degree-keyed `writes:` and `emits:`, `emits_on_refusal`, grade, and long per-column `*_note` provenance strings (2111 lines).
- **Status:** none (data; header cites `architecture/PLAN.md` W3). Reading: live mechanism (`data/verbs.py` loads and cross-validates it against `write_matrix.yaml` and `rosters.yaml`); its prose notes are history.
- **Bears on:** CORE, CHAR, PC, MB, SC, FA, SE, FI, WR.
- **Content that matters:**
  - **[PARTIAL READ, stated plainly]:** lines 1-260 (header block and rows carry, argue, arrest, commit, comply, conceal start) were read in full. For the other 60-odd rows I read a structured projection (every row's verb, stratum, eligibility, beneficiary, referent_class, counterparty, contests, grade, scale, requires, requires_typed, writes, emits, emits_on_refusal) produced from the loaded YAML, with free-text `*_note` provenance strings truncated; the full text of those notes in lines 261-2111 was NOT read line by line. Findings below are from the projection and from the full header and first rows.
  - Counts from the loaded table: 67 verbs; grade `assumption` 44, `ruled` 23; stratum `uncontested_material` 23, `social` 21, `binding_decision` 12, `contested_physical` 9, `movement` 2; beneficiary `none` 28, `actor` 28, `subject` 8, `to` 3. The header's counts (32 verbs, 24 or 28 with a `requires`) are dated (:95-:104, :28).
  - Contested verbs and their prizes (the only ones the seam rolls, 11): argue, determine, interrogate -> "a proposition"; arrest, lie, tell -> "a standing"; speak -> "a matter"; fight, capture, accept -> "the body"; march -> "a field". `examine`, `research`, `surveil`, `interview`, `thread_read`, `reconstruct` declare no `contests:` and are routed by `graded_inquiries` (rosters.yaml:1407): of the six, three are graded by the social roll, three are flat `finding.made`/`finding.none`.
  - Combat is three verbs sharing one prize: `fight` (lethal default), `capture` (`remit:dispatch`, yield terms, `Tenure.since` on Wounded), `accept` (a held `challenge` Record; duel). Degrees for "the body" are `Declared / Felled / Wounded / Untouched` with writes `Person.body, exists, Tenure.until, capability, body_ceiling` on Felled; so killing and wounding are a band of the one scene verb, not separate verbs (`kill / wound` was renamed `fight`, 2026-09-29).
  - `march` (prize "a field", step ENCOUNTER) writes `Won / Lost / Unopposed / Invested` bands: body, stance (grudge and morale), `Tenure`, `Person.travel_leg`, `Rung.stores` x2; an army is mustered by `commit` to the seat's faction. Army composition is changed by six menu verbs on an `army` Record that NO NPC forms (`army_verbs` in `withheld_verbs`): `recruit, form_unit, assign_troops, disband_unit, discharge_troops, order_unit`. So NPC armies exist only as authored records; the AI cannot recruit, which bears directly on the MB lane (F-CORE-13 and the MB audit).
  - Social contests: `argue` (moves the hearer's `Person.pursuits` toward the arguer's), `speak` (a docketed matter, no writes, emits `matter.carried/advanced/held/turned`), `tell`/`lie` (no writes; emit `news.told` + `confidence.broken` or `news.untold`; `lie` formed only while `Fixtures lie_offered`), `determine` (bench; writes `Tenure.since, DocketItem.matter, Tenure.degree, Person.pursuits`), `interrogate` (confession bands, no writes). `speak`, `tell`, `lie`, `interrogate` write NOTHING to state: their consequence is a claim deposit by WITNESS only.
  - Character-state verbs are few: `train` (`Person.capability`), `tend` (`Person.body`), `forgive` (`Person.stance`), `argue`/`determine` (`pursuits`), `conceal` (a cover Record). Nothing writes skills, traits, needs, age, or a goal: the CHAR lane's authoring surface is `cast:` overlays and `train`.
  - `referent_class` is declared on 29 rows (Record, Proposition, Office, Rung, Site, Person, Detainee): the person-side formation partition (IN-53) lives as a column on the row, plus per-row `*_note` MEASURED blocks (formed/attempted/executed counts at specific commits for seeds 0-2), e.g. `commit` formed for 83 of 83 persons and executed 0/1/1 before the class (:214); `argue` forms on nobody after the class (0/0/0, :139).
- **Conflicts / stale:**
  - `scale:` is carried on 15 rows (confer, determine, dispatch, establish, exchange, issue, requisition, march, marshal, surrender, pardon, revoke, raze, seize, succeed) although the header says nine and that Layer 1 refuses the key; this CONFIRMS F-CORE-16 (15 rows, no reader) and contradicts the header at :66-:79. `convene`'s was removed.
  - Rosters keyed by verb: counting `rosters.yaml`, 17 blocks key on a verb (verb_capability, graded_inquiries, duel_terms, warrant_sourced, terms_sourced, choice_sourced, vocation_sourced, held_document_declines, own_stance_declines, lie_verbs, army_verbs, own_hold_declines, own_title_declines, held_edge_declines, violence_contexts, affiliation_engagement, alignment with its `uncelled:`), against F-CORE-18's fourteen; this CONFIRMS F-CORE-18's pattern and shows the count has grown (`army_verbs`, `affiliation_engagement`, `alignment` are the extra ones I count). 44 of 67 verb rows are graded `assumption`.
  - Header comment says all 24 verbs carrying a `requires` carry `emits_on_refusal` (:95-:104); the projection shows no row with a `requires` lacking one, but `thread_read`, `interview`, `reconstruct` refuse with `finding.none`, a kind shared with five inquiry rows (one refusal kind for several verbs).
  - `Person.coherence` has a matrix row and a verb-less writer set; no verb in the table writes it (see write_matrix).
- **Open items:** `H-75` (`destroy_record` eligibility can decline on both alternatives and never fire, :87-:90); `H-44` (which acts a dispensation's terms may name); J-8 (`dispatch` and `issue` remit per post) gates arrest, capture, march, marshal, surrender, raze, seize, warrant; `thread_read` waits on a value space; `reconstruct` (K-37) waits on a value space nothing supplies; the 44 `assumption`-graded rows are each `[ASSUMPTION; medium; Jordan to correct]`.

## Cross-subsystem leads
- **CORE, CHAR, PC:** No state writer exists for a person's skills, traits, needs or goals beyond `capability` (raised by `train` or a fight), `pursuits`, `stance`, `conviction`, `scar` and the unhashed-nothing `attributes`/`thread_sensitivity`/`heritage` (build-time only; carriers.py:797-826). `attributes` SHIPS EMPTY (the `cast_attributes` switch ships OFF, carriers.py:813-815), so the ten-attribute pool derivation (`vocation_attribute`) is latent in every shipped realm; `verb_capability` is held by 1 of 430 persons (rosters.yaml:1518-1520). Whatever the CHAR audit says about character definition mapping to RPG axioms must start from this.
- **MB, FA:** Army composition verbs are `withheld_verbs` (rosters.yaml:2671-2680); NPCs never recruit, form units or assign troops, and `march` is the only army act the AI can take; `besiege` is unreachable because `march_postures` ships `[storm]` (rosters.yaml:1176). `arms_kinds` and `arms_at_build` are empty, so no one has equipment (rosters.yaml:1851, 1862).
- **SC, FI:** Investigation is rolled by the social-contest module entry, not a fieldwork roll (`graded_inquiries`, rosters.yaml:1433-1435), and a failed or refused inquiry teaches the actor nothing (`undeposited_kinds`, rosters.yaml:1452-1457, H-111). The `fieldwork.find` module only masks a trail by `finding_terms`; only `record.forged` is covert (`covert_kinds`).
- **WR, FA:** Endings: `peninsular_sovereignty` is unreachable in computed play and the loop never halts on an ending (rosters.yaml:3460-3464); `strife_kinds` lists are hand-maintained (rosters.yaml:3348-3398). `foreign_cast` carries only Altonia; Schoenland has no persons built through this row.
- **GO:** `World.content_hash` is a language-neutral canonical encoding for the port (world.py:210-340); `_departed`, `_covers_logged`, `_last_by_*` and the tenure shadow are unhashed state a port must also reproduce; no save/load path exists in `state/` (world.py:387-392).
- **DICE:** the `alignment` table's `fight`/`accept` cells are -0.3 on every axis (CR-87, ED-IN-0340) while `uncelled` lists 21 verbs scoring 0.0 on every axis, so the pursuit term cannot rank them (rosters.yaml:4032-4118).

## Likely stale or superseded
- rosters.yaml:38-44 and :575-:588 describe `engine/substrate/keys.py::AXES` as a live reader; the Key substrate is RETIRED (CLAUDE.md §0, ED-IN-0232).
- verb_table.yaml:66-79 (`scale:` on nine rows, "retired when `Act.via` carries the scope") and :95-:104 (24 or 28 `requires` verbs, 32 `writes:` entries): the table is now 67 rows and 15 carry `scale:`.
- write_matrix.yaml:4-6, :29-31 (shape.py `write()`, `engine/season/register.py`): both gone; and the "eleven/nine/eight rows with no producing verb" counts at :47-:70.
- state/__init__.py:15 names `shape`; carriers.py:7-8 says the facade was deleted at step 10.
- carriers.py:688-702 (`Act.stratum` "19 of the 32 verb-table rows" latent sentinel clash) and :305-:307 (`Event.ending` "no production reader").
- state/gate.py header :18-:34 (receipt window lifetime) corrected in place at :36-:42; world.py:459-466 read counts (219 / 67,005) and :1569-:1601 count "six, not seven" callers are dated.
- rosters.yaml `modules.members` homes under `systems/` for a tree that holds no `.md` (CLAUDE.md §3) are path facts, not mechanism; `victory` stub home `engine/season/` while `endings` is implemented in `queries/world_q.py`.
- rosters.yaml:1368-1376 seam table says faction management and character development are UNRULED and "absent from the loop entirely"; it is a dated comment `[UNVERIFIED against the current loop]`.

## Items that could change an audit finding
- **F-CORE-09 (per-access scans):** CONFIRMED structurally: `World.tenures` re-sorts and concatenates per access (world.py:467-471) and is walked by `parent_of`, `descendants`, `home_map`, `seat_hold`, `sworn_to`, `in_holdings`, `remove_person`; `event_by_id`/`matured_terms` are linear log scans (attribution.py:238-277); `EventLog.__contains__` is a list scan (log.py:119). Also: `Gate._minted` retains every Receipt for the gate's life (gate.py:1885), which the finding does not name `[memory growth UNVERIFIED]`.
- **F-CORE-16 (scale: column):** CONFIRMED, 15 rows; the verb-table header still says nine (:66-:79).
- **F-CORE-18 (verb-keyed rosters):** CONFIRMED and larger: I count 17 verb-keyed blocks in rosters.yaml, not fourteen (see verb_table entry); the loaders are `data/verbs.py`.
- **F-CORE-11 (two gate conformance gaps):** the gate header itself records the Layer 1 `04 §C.2` enumeration as nine bases while the code has fourteen, "not edited here" (gate.py:157-164, :244-:252), and `EventLog` still admits a bare `StateChange` (log.py:24-31): these look like the filed gaps; I did not match them to the audit's two by id.
- **F-CORE-17 (a refusal is priced, no receipt):** consistent with gate.py: a refusal path leaves nothing minted (`no_op` raised before any mint, world.py:1428-1435) and the fold emits the row's refusal kind; MATTER closure writes that move nothing still emit (`dwelling` wear 0, world.py:1163-1169). Opposite directions of the same asymmetry.
- **F-CORE-15 (capability: one reader, six authors):** rosters.yaml shows the authors: `verb_capability` (9 verbs), `vocation_attribute` (4 vocations), `lifepath_templates`/`lifepaths` (34 ids, 13 grant a key), the `cast:` overlay, `train`, and the fight raise; the reader is `seam/wrappers/sigma.py::faculty`. Consistent.
- **F-CORE-13 (one module a scene, three calls):** consistent with `contest_subsystems.prizes`: combat is `ENCOUNTER`/suspendable, mass battle `ENCOUNTER`, social three prizes at RESOLVE via `social_contest.roll`; fieldwork is a fourth provider (`inquiry` role) with different shape (fieldwork.py:14-27).
- **F-CORE-01 / ledgers:** ledger eviction is `confidence x (when+1)` with `ledger_cap` per person (ledgers.py:17-32); the roster note's tuple wording (rosters.yaml:898) is imprecise.
- **F-CORE-23 (provided corpus through a repair routine):** not touched by these files.
- New, unfiled: (a) the act-id collision (acts.py:74-83): two distinct but EQUAL acts under one id are silently deduplicated, so the second never exists; the mint lacks a draw ordinal and fixing it moves every golden; (b) `knowledge_kinds` (rosters.yaml:1763) has no reader and `Person.coherence` has a matrix row, an emission kind and no writer (write_matrix.yaml:199-206); (c) `remit_default` (every office every remit act) is a test fixture living in the shipped roster and is what makes `confer, convene, establish, revoke` formable at all (rosters.yaml:355-407); (d) GD-1's victory is unreachable in computed play by the roster's own words (rosters.yaml:3460-3462).
