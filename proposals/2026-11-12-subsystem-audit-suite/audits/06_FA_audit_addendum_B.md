# FA — adversarial steelman audit, addendum B

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 6eff039 (working tree)

Addendum to `audits/06_FA_audit.md` (the first FA lane, read at `601e715`; its §0 to §15 and its six
proposals stand except where §B2 below corrects them). This addendum does the reading the first lane
reported as not done (its §12), and adds: a reading of the whole design set for governance, factions,
war and diplomacy against the code (§B3); the campaign layer that mass battle needs from FA (§B4);
the capability consequences (§B5); further proposals (§B6); and an evidence log (§B7). Findings
continue the first audit's numbering from `F-FA-13`; resolutions continue from `R-22`.

Nothing here is the reason a behaviour is correct (`CLAUDE.md` §0.05). `.designs/`, `.audit/` and
`research/` are cited as referents by path. `[UNVERIFIED]` marks what was not checked.
`git diff --stat 601e715 6eff039 -- engine modules references architecture systems tools tests
workplans registers` is empty (the commits between are the suite's own documents), so the first
audit's readings of computed play hold at this SHA; every code citation below was opened at `6eff039`.

## B0. What this addendum changes in the first audit's verdict

**The verdict stands and is sharpened in three places.** (1) The first audit judged FA against `04` and
the plan; Layer 1 also holds a ratified page on exactly this subject, `architecture/meta/10_FACTIONS_AND_DEPLOYMENT.md`,
which it did not cite. Against that page the code is conformant on the faction view and on war as an
uttered Proposition, and **short on one stated contract: the battle seam is to receive each side's
stakes (its holdings and seats, "for what a defeat costs"), and no field outcome touches a holding or a
seat** (F-FA-13). (2) "War has no producer" (F-FA-04) is narrower than stated: the producer exists and
is tested (`utter` of mood `WAR`, then `commit`); what is absent is anyone with a reason to do it, and
the planned shape of `at_war` has a defect the plan does not name (one committer anywhere keeps two
factions at war, F-FA-14). (3) The campaign layer is further built than the first audit's §10 row says,
and its authority is split two ways: a march is ordered through a seat, an army is raised and commanded
by whoever minted a paper (F-FA-15, measured). The single largest obstacle is unchanged: the acts that
redistribute power do not execute in computed play.

## B1. What was read

**Faction design set, `.designs/systems/factions/reference/` — read in full, no line truncated**
(line lengths were measured with `awk` first, E-B8; the three lines over 1,900 characters were each
read to their last word):
`faction_canon_v30` (739 lines; it ends after the Church sheet, the other sheets were never written
into this file), `faction_layer_v30` and its `_infill`, `faction_behavior_v30`,
`faction_state_authoring_v30`, `factions_personal_v30` and its `_infill`, `faction_politics_v30`
(all 1,189 lines, Parts 0 to 11), `faction_succession_split_v30`, `faction_systems_overview_v30`,
`franchise_v30`, `parliamentary_transfer_v30`, `treaty_expiration_v30`,
`fractional_province_ownership_v30`, `fail_forward_pp177`, `ci_political_v30`,
`baralta_crown_claim_v30` and its `_infill`, `varfell_path_b_v30` and its `_infill`,
`political_dynamics_keys_migration_v30`, `factions_flow_skeleton_v1`. The `_index` files are generated
heading tables (`doc_index_gen.py`; `faction_layer_v30_index` was opened to confirm they carry no
content of their own) and were not read further.

**Cross-cutting `.designs`, read in full:** `_architecture/reference/governance_consolidation_v1`,
`governance_ripple_substrate_v1`, `governance_type_registry_v1`, `campaign_modes_v30`,
`campaign_architecture_v30`; and, followed as referents because the campaign layer turns on them,
`settlements/reference/march_layer_v30`, `scale_hierarchy_v1`, `valoria_political_hierarchy_v30`,
`mass_battle/reference/military_layer_v30`, `mass_battle_integration_v30`.

**Layer 1 and plan, read in full where cited:** `architecture/meta/10_FACTIONS_AND_DEPLOYMENT.md`;
`04_CODE_ARCHITECTURE.md` rows F.32, F.33 and D-48; the B10-17 and B10-17b position rows of
`workplans/valoria_master_workplan_v11_part3.md`; §0, §1, CP-T09-02 and CP-T09-03 of
`proposals/2026-10-23-subsystem-completion/…-09-factions-war-diplomacy.md` (the plan's home file for
the war positions).

**Sibling lanes, read for citation:** `audits/04_MB_audit.md` §1.2, §1.3, §10, §11, §17, §18.1 and its
outline; `audits/07_SE_audit.md` by search; `proposals/02_CHAR_capability_uses_table.md` (head);
`audits/10_DICE_audit.md` §14 by search; the first lane's six proposals (three in full, three to their
"Exact edits").

**Code opened for this addendum:** `loop/effects_army.py`, `loop/sides.py` (both in full);
`loop/effects_combat.py:451-756`; `seam/wrappers/mass_battle.py:160-358`; `queries/world_q.py:2132-2316`,
`:3551-3712`; `state/gate.py:1036-1064`; `harness/army_presets.py`; `loop/effects_information.py:105-124`;
`tests/test_faction_q.py:205-262`, `tests/test_levy_feed.py:1-60`, `tests/test_term_upkeep.py:1-45`
(read, not run); `offices.yaml`, `verb_table.yaml`, `arrangements.yaml` and `rosters.yaml: terms_sourced`,
`factions.head_seat`, `role_templates` through a YAML reader (E-B2, E-B3).

The `.audit/` and `research/` reading is accounted for in §B8, with what was not reached.

## B2. Corrections to the first audit, and new findings

### B2.1 Corrections

| # | first audit | correction | evidence |
|---|---|---|---|
| C-1 | F-FA-04: "No verb declares a war, no computed act makes `at_war` true" | True of a `declare` row and of computed play. The producer exists: an `own`-eligible `utter` of mood `WAR` followed by the utterer's `commit` makes `at_war` true through the real fold, and `release` ends it. `at_war` also has one production reader already, `world_q.enemies_heard` (CR-87, the `war` violence context), beside the `strife` instrument. What is missing is an occasion and a target set (CP-T09-02) | `tests/test_faction_q.py:223-262` (read, E-B5); `world_q.py:3566-3598`, `:3677-3712`; E-B4 |
| C-2 | §1 "Never formed: `succeed`, `interrogate`, `marshal`, `surrender`" (no cause given for the last two) | `marshal`, `surrender` and all six army verbs are withheld from every NPC's opening set by a fixture, shipped: `withheld_verbs=("destroy_record", *ARMY_VERBS, "marshal", "surrender")` (H-156). They never form because they are switched off, not because no question reaches them | `data/fixtures.py:1157` (E-B4) |
| C-3 | §10, MB row: FA emits "`march` through `remit:dispatch`; the mustered set from `commit` members" | Incomplete. The loop also holds: an `army` Record with six verbs (`recruit`, `form_unit`, `assign_troops`, `order_unit`, `disband_unit`, `discharge_troops`); a standing order of battle (`marshal`); a siege band (`Invested`, garrison wear); `surrender`; a ration debit per field (`field_provisioning`, shipped off); and the muster basis at the gate (`may_muster`). The MB audit describes these (§1.2); the FA side is §B4 here | `loop/effects_army.py`; `effects_combat.py:451-716`; `gate.py:1036-1059` |
| C-4 | §5.2 last-but-one row: "[UNVERIFIED: ED-FA-0001's last ledger row was not opened]" | Opened. `registers/editorial_ledger_fa_archive.jsonl` carries one `ED-FA-0001` row (2026-07-05, status `ratified`, `needs_jordan: false`); the four-starting-factions ruling is recorded in `governance_consolidation_v1.md` §6 ("RULED 2026-07-13, second pass") and `scale_hierarchy_v1.md` §5.1 leaves it standing. The built realm holds ten faction Propositions (E-B1), under the later roster ruling the first audit cites | E-B7, E-B1 |
| C-5 | §7: the archived design "is a statistics-bearing faction … Layer 1 refused the stored aggregate, so none of it is a specification" | The archived design moved off that position itself, in three dated steps the first lane could not see without the full set: Legitimacy and Popular Support became per-settlement and Mandate a derived aggregate (LPS-1/LPS-2e, 2026-05-30; `faction_canon_v30` §5, `faction_behavior_v30` §4); D4 retired the Mandate formula as the carrier of collapse (2026-07-13; `governance_consolidation_v1` §1, §6); and `scale_hierarchy_v1` §5.1 (RATIFIED 2026-07-13) states "factions do not necessarily need to hold territory — they need to hold PEOPLE, and it is the number of people and the weight of their positions that carry the value of that faction." The design and Layer 1 converge; what remains design-only is the *weighing* (§B3.3) | the documents named |
| C-6 | `06_FA_seat_terms_and_turnover.md`: first authoring "the eight `elected` rows at `term: 8`" | The mechanism stands. The content assumption does not fit the design it would implement: of the eight `elected` rows (E-B2), the Confessor, the Duke of Varfell, the Senior Jarl of the West, the Skald-Chief and the Military Jarl are life seats in the archived ladders, emptied by death, incapacity or a vote of their body (`faction_politics_v30` §1.3 Standing 5 to 7, §1.3a, §1.4 Standing 6 and 7); only the Guild Comptroller (a rotating council, `factions_personal_v30` §8.6) and the Commune Representative are posts the design rotates. Superseded in content by `06_FA_seat_terms_by_body_B.md` | E-B2; the sections named |
| C-7 | §9 "FA's edges to the loop are the loop's own writes … nothing a battle … decides is read back by a governance verb" | Holds, and is stronger than stated: it is a Layer-1 shortfall, not only a plan item (F-FA-13) | `10_FACTIONS_AND_DEPLOYMENT.md` §3 |
| C-8 | §12 lists `factions_flow_skeleton_v1` as a design document not read | Read. It traces `systems/factions/sim/` (16 modules), `engine/mc_v18.py`, `engine/autoload/` and `engine/cross_scale/` at `6545067`. None of those paths is in the tree (`git ls-files`, E-B6): the document describes the retired campaign driver. Its §7 is still the best single record of what the stat-bearing faction code did and did not do (conquest by one stochastic draw, six stub modules, `mass_seizure` and treaty expiry with no caller, `casus_belli` with no writer), and nothing in it is a finding about the season loop | E-B6 |

### B2.2 New findings

### F-FA-13 · degrades narrative, and a Layer-1 shortfall · a defeat costs bodies and never a holding or a seat

- **Claim.** Layer 1's roster contract for the battle seam names four things the seam receives: the
  sides, the units, **the stakes ("`holdings` and `seats`, for what a defeat costs")**, and the freeze
  (`10_FACTIONS_AND_DEPLOYMENT.md` §3). The code builds the first, second and fourth. No stake is
  passed in and none is written out.
- **Evidence.** `seam/wrappers/mass_battle.py::field_input` (`:225-279`) builds `MassBattleInput` from
  weights, territory, fortification, stances, origin, loyalties, orders of battle, members: no holding,
  no seat. `_eff_march` (`effects_combat.py:451-683`) writes `Person.body`, two `stance` rows per loser,
  the movers' `contain` legs and `Rung.stores` debits; its docstring states the choice: "a won field
  writes PRESENCE, never title — β … [ASSUMPTION; medium; Jordan to correct]" (`:532-536`). Title moves
  by `seize`, which is `remit:issue` with a purview cell (E-B3), a different seat's act than the
  `remit:dispatch` march.
- **Falsifier and outcome.** A `hold` on a rung or an office that opens or closes in the same season as
  a `field.won` or `field.lost` naming its holder's faction. The first audit's realm runs read
  `rung.seized` 0 at seeds 0, 1 and 2 over three seasons, and `seize` attempted 9, refused 9 in
  `aperture 2 0` (its E-3, E-5); no fought field in those runs was `Won`. Not re-run here: no code
  changed between the two SHAs (header).
- **Touches.** R-02, R-04. **Narrative consequence.** A lost battle is a casualty list. Nobody loses a
  province, a fortress or an office because of it, so no arc of conquest, ransom, deposition after
  defeat or a marshal broken for losing can occur.
- **Minimal fix.** Not a new write on the field. CP-T09-04 already gives occupation its taking
  (plurality occupation licenses `seize`), which is the β reading the code chose, and its part (d)
  already plans the occasion for *uncontrolled* land where the seat's faction is mustered. What is
  missing is the same occasion for *held* land the faction occupies after an arrival: one clause on that
  planned term (`06_FA_war_lives_in_seats_B.md` edit 6). The seats half of the stake (a commander who
  lost) is the recall of the first lane's `06_FA_decree_binds.md`, fed by one more claim kind; named in
  the same file's edit 7 (b), not built.

### F-FA-14 · design defect in a planned position · under the planned `at_war`, one committer keeps two factions at war, and Layer 1's own open gap is where it comes from

- **Claim.** `at_war(a, b)` is true while any live `commit` to a `WAR` Proposition naming the pair
  exists (`world_q.py:3594-3598`). CP-T09-02 (d) adds rallying (any member of either side may commit)
  and CP-T09-03 (c) ends a war "when no committer is left". Peace therefore needs every committer on
  both sides to release, or die. Layer 1 recorded the opposite failure as open (F.32: "the declarer dies
  and the war can be ended by nobody … the repair is an edge subjected to *the seat's holder*, and the
  design has no Tenure that changes hands"); in the code as built a dead man's edges are deleted with
  him, so today a war of one ends by his death, and after CP-T09-02 a war of many ends only by
  unanimity.
- **Evidence.** The Query above; `04_CODE_ARCHITECTURE.md:1232`; the plan file `:176-184`, `:229-231`.
- **Falsifier.** A reader of `at_war` that distinguishes who committed. There is none: `enemies_heard`
  (`:3703`) and the planned target set both ask the bare pair.
- **Touches.** R-04, R-08 (a war nobody can end is omniscient bookkeeping, not a person's decision).
- **Narrative consequence.** Either no war outlives its declarer (today), or no war ends (planned). The
  design's "de jure war that nobody will muster for" (10 §2) needs someone whose word ends it.
- **Minimal fix.** `06_FA_war_lives_in_seats_B.md`: the war is de jure while a committer **holds a seat
  of either party whose grant carries the muster act**. A successor to the seat decides, by committing
  or not, whether the war continues; an unseated zealot's commit is the de facto share and no longer
  the war. No Tenure changes hands and no stored flag is added. It narrows a ratified docstring, so it
  is §B6.2 item 1.

### F-FA-15 · degrades narrative, an S defect · men are levied by whoever minted a paper; stores are levied through a seat

- **Claim.** The authority to take stores from a place is a seat's (`requisition`: `remit:issue` and a
  purview cell). The authority to take men from the same place is a Record's: the six army verbs are
  `own`-eligible on `held_by`, the army may be minted by any member of the faction, one per faction, and
  thereafter only the Record's holder commands it. A march is `remit:dispatch`. So one quantity, the
  right to extract from a place, runs on two ladders, and the right to command the army is separated
  from the right to send it.
- **Evidence.** `verb_table.yaml` rows (E-B3); `effects_army.py:34-42` (the commander is the holder,
  committed to the army's faction); `effects_information.py:105-124` (`_army_mintable`: a member, one
  per faction); `world_q.py:2186-2195` (`raisable_by`: the faction holds where the cohort lives).
- **Falsifier run and outcome (E-B9).** `build_realm(0)`: `p_npc_002`, a Varfell member holding no seat,
  mints Varfell's army (`record.created`) and raises 60 levy from `cohort_set_s_026`
  (`army.recruited`); the same `recruit` by `p_npc_052`, the Duke of Varfell and the faction's head,
  is then refused (`recruit.refused`), because he does not hold the Record. In the same probe the
  Löwenritter, the Guilds and the Restoration Movement each mint an army and have **no** raisable
  cohort: they hold no land and the realm's cohorts carry no `commit`.
- **Touches.** R-04, R-06. **Narrative consequence.** The faction's only army belongs to whoever acted
  first, and a duke cannot levy his own duchy. The design's standing military order (the Löwenritter as
  the Crown's army, `faction_layer_v30` §1.5) cannot raise a man. Unreached in computed play only
  because the verbs are withheld (C-2).
- **Minimal fix.** `06_FA_levy_through_the_seat_B.md`: `recruit` and `discharge_troops` are exercised
  through a seat whose grant carries the muster act and whose purview reaches the cohort's residence,
  the two predicates `requisition` and `march` already use. The Record stays the order of battle.

### F-FA-16 · degrades narrative · five of ten factions have no head, and one has no members

- **Evidence (E-B1).** `faction_q.resolve` at `build_realm(0)`: `head` is `None` for Altonia, the
  Guilds, the Löwenritter, the Restoration Movement and Schoenland; `fac_faction_x` has no member, seat
  or holding. `rosters.yaml: factions.head_seat` names four seats (`:2062-2066`); `off_grand_master`
  and `off_restoration_leader` exist as rows and are not in it (E-B2).
- **Why it matters.** Every planned route that addresses "the head" (a discontented member's petition,
  CP-T09-01; the first audit's §11 item 3 option B; a head who declares) has nobody to address in half
  the roster. `faction x` is a deliberate placeholder (`references/names_index.yaml:317-320`) and is
  harmless; it should not be counted as a polity by any reading.
- **Resolution.** R-25: add the two seats the file already authors to `head_seat`
  (`"Löwenritter": off_grand_master`, `"Restoration Movement": off_restoration_leader`); leave the
  Guilds headless (the design's Guildmaster Council is a collective by intent, `factions_personal_v30`
  §8.6, `faction_politics_v30` §2.5) and say so on the roster; Altonia's and Schoenland's are WR's.
  Carried by `06_FA_seat_terms_by_body_B.md` edit 4 (one file, one owner).

### F-FA-17 · hygiene with a campaign cost · at tick 0 no rung in the realm holds a store

- **Evidence (E-B1).** `build_realm(0)`: 414 rungs, none with a non-empty `stores`; eight seat rungs,
  none stocked; four live `oblige`, none with a term.
- **Consequence for FA.** Every fiscal act of office starts refused: `requisition` asks
  `stores >= amount`, upkeep is paid by `transfer` out of the seat's rung, a field's ration is read from
  the seat's rung. The first audit's `requisition.taken` 0, 1 and 6 over three seasons is this. Primary
  owner SE (`07_SE_ground_and_granaries.md` stocks larders and granaries); cross-listed, not re-decided.

### F-FA-18 · design that exists only as prose · what an order orders

- **Claim.** A writ's `terms` is whatever Proposition its issuer's question named (`issue`:
  `own_ledger of: subject`). No roster says what a writ may order, so no act of the addressee is the
  performance of the order. The first lane's `06_FA_decree_binds.md` makes the answer a choice and the
  defiance an occasion, and states that "what compliance performs is still the separate act the writ's
  terms name (H-44)". The archived design has the missing roster: a Directive is one of Extract, Tax,
  Suppress, Install, Host, Cede (`governance_type_registry_v1` §1; `.audit/2026-07-12-governance-compendium/43_directive_types.md`).
- **Where the route already is.** `rosters.yaml: terms_sourced` (`:2508-2546`) forms a listed verb on
  what a held writ's terms name; its one cell today is `commit: [dispensation, petition]`.
- **Resolution.** R-27, design-first, no proposal file: the performing verbs exist for four of the six
  (`transfer` for Extract and Tax, `confer` for Install, `surrender` or `give` + Rung for Cede); what
  does not exist is a Proposition shape that names a kind, an amount and a destination, and that is
  CORE's vocabulary, not a roster cell. The order of work is: the first lane's P1 (answers and the
  recall), then one term shape (a demand of stores to the issuer's seat rung, performed by `transfer`,
  which is also the war levy and tribute of §B4), measured before a second is added. Held to that until
  a writ is answered at all.

## B3. The full design set for governance, factions, war and diplomacy, against the code

### B3.1 What the design says authority is

The archived set is not one design. It is four layers written at different times, and they disagree
with each other before they disagree with the code. In order of date:

1. **The board-game faction (April 2026).** A faction is a sheet of six statistics (Mandate, Influence,
   Wealth, Military, Intel, Stability). It acts by Domain Actions drawn from a card hand with cooldowns
   (`ci_political_v30` §5), resolved as stat against stat. Authority between factions is Parliament:
   Mandate-weighted votes on a ladder of sanctions (Censure, Embargo, Blockade, Outlawry), constructive
   motions (Subsidy, War Authorisation, Treaty Ratification, Recognition Challenge, Succession
   Endorsement), a Church veto on a cooldown (`faction_layer_v30` §5). War is occupation (a marker,
   three seasons to transfer), treaties in three phases with a guarantor, a casus belli as a
   consumable licence, and five Stability triggers with a collapse procedure (§1 to §3).
2. **The ladder (April to July 2026).** Authority inside a faction is a Standing ladder of eight ranks
   with gates, obligations, halls, livery, a mentor and a demotion trigger, per faction, with sub-office
   ladders, caste gating, graded demotion with appeal, ministries, committees, dicasteries and councils
   (`faction_politics_v30`). Leadership is not a rank: it is reached by succession (declared, elected by
   a body, or contested).
3. **The behaviour model and the person (May 2026).** A faction's conduct is derived from persons:
   Mission, a cascade of convictions weighted by seniority down a supervisor graph, a role template the
   populace expects, and legitimacy and popular support tracked per settlement
   (`faction_behavior_v30`, `faction_state_authoring_v30`). Succession is a contest between named
   claimants that can split the realm (`faction_succession_split_v30`).
4. **The governance thread (July 2026, partly RATIFIED).** Authority is exercised downward as a
   Directive answered by Comply, Bargain or Defy, with suspicion accruing and reducible, ending in a
   recall with an audit escape (D5, D6, E11); the hierarchy is settlement, territory, conditional
   province, duchy, country; "factions hold people, not territory"; the Crown and Parliament may reach
   past the chain; each tier sets the governance type of the tier below and the governed consent or do
   not (`governance_consolidation_v1`, `scale_hierarchy_v1`, `governance_ripple_substrate_v1`).

Layer 1 (September 2026) then ruled the shape all of it must take: a faction is a resolved view over
persons' edges, never an actor, and a war is an uttered Proposition (`10_FACTIONS_AND_DEPLOYMENT.md`).

### B3.2 Element by element

"Has" means executed in a seeded run cited in an evidence log; "built" means in the tree and reached
only by a hand-built act or a test; "lacks" means no code.

| element | what the design says | code | plan owner |
|---|---|---|---|
| **Seat** | a named office with a rung, a remit and a holder | **has**: 34 offices at build, 31 authored rows (E-B1, E-B2) | — |
| **Remit** | what a rank may do (Access column; card hand) | **has**, six remit acts; 26 seats carry `dispatch` by a placeholder (first audit F-FA-03) | first lane P2 |
| **Purview and oath** | a liege's reach over a vassal; fealty of the dukes to the Crown | **has** (`purview_reaches`, oath clause); 4 live `oblige` at build, none termed (E-B1) | CR-09 |
| **Appointment** | at the leader's pleasure (Crown); by vote of a body (Hafenmark, Varfell, Church) | **built**: `confer` formed 5, attempted 0 (first audit E-3) | first lane P3, P6; CR-35 |
| **Removal** | graded demotion with magnitudes and an appeal; removal by the body; recall after suspicion | **built** as revoke plus a ban; no grades, no appeal, no body, no suspicion | first lane P1 (recall); CR-37 (deposition) |
| **Term and rotation** | rotating Guildmaster Council; annual assembly attendance; life seats elsewhere | **built** (`Tenure.term`, MATTER matures it); no seat is termed | first lane P3, re-contented by `…seat_terms_by_body_B` |
| **Succession** | a designated heir if the apparatus accepts him, else a contest; near-peers split the realm | **built** for one line (the throne, one-act claim); no contest, no split | CR-35; the split unowned |
| **Rank inside a faction** | Standing 0 to 7 with eight dimensions | **lacks**; `rank` reads 0 for every pair (H-181) | CR-32 (names and order only) |
| **Franchise** | a territory's weight in Parliament, 0 to 5, lowered by caste, raised by good rule (`franchise_v30`, DRAFT) | **lacks**; no reader of a territory's political weight | none; see B3.3 |
| **Parliament** | the forum of all factions; weighted votes; sanctions ladder; veto | **lacks** as a body: no seat has `body: Parliament` (E-B1). An arrangement row `parliamentary_debate` exists (E-B3); a `determine` there is the nearest thing | declined as a faction vote (plan GP-12); SC's hearing |
| **Parliamentary transfer** | a territory moved by a vote wrapped round a roll, licensed by a casus belli | **lacks** | none; `give` + Rung is the cession that exists |
| **Treaty** | six types, three-phase negotiation, guarantor, breach costs, 90 per cent lapse per arc | **built** as `covenant` (0 of 10 executed) whose terms nothing reads | CP-T09-03 (alliance and peace only; truce, tribute and dated terms declined, GP-5b) |
| **Casus belli** | a consumable standing right from eight sources | **lacks** | CR-91 (a claim Proposition on four grounds) |
| **War** | declared, authorised by vote or licensed by a casus | **built**: `utter` + `commit`; `at_war` false everywhere (E-B1) | CP-T09-02 |
| **Occupation and conquest** | a marker, then transfer after three seasons or on Overwhelming | **has** as presence (`army.arrived`, `occupies`); title by `seize`: 0 executed | CP-T09-04 |
| **Province** | conditional: exists while one faction holds its territories (RATIFIED) | **has**, as a Query (`world_q.provinces_of`); `build_realm` builds no province rung (E-B1) | — |
| **Directive, Comply, Bargain, Defy, suspicion, recall** | RULED (D5, D6, E11) | **built** as verbs that write nothing; no suspicion, no recall | first lane P1 |
| **Court attendance and hostage-kin** | RATIFIED (ED-FA-0020) | **lacks**; needs kin, which the closed cast does not carry (plan GP-13) | parked |
| **Legitimacy and popular support** | per settlement, the consent gate on every cascade | **partly**: `person_q.legitimacy` is a Query over claims; nothing aggregates by settlement | SE / CHAR |
| **Role template and cascade** | expected convictions by faction role; members' conduct blended down a supervisor graph | **partly**: `rosters.yaml: role_templates` is read at build to seed pursuits (`data/goals.py:313`, `populated.py:1399`); no cascade, no fidelity | — |
| **Faction collapse and emergence** | Stability 0 collapses; insurgency in four stages | **lacks** the first; IN-30 owns the second and is stopped | IN-30 |
| **Stability, Mandate, Wealth, Military as numbers** | the six-stat sheet | **refused** by Layer 1 (a view has no field) | — |

### B3.3 Where the design and the code disagree, and what it costs

- **The design's inter-faction politics is a parliament; the code's is nothing yet.** Every instrument
  by which one faction constrains another short of war (sanction, embargo, recognition, ratification,
  transfer, veto) is a Parliament motion in the design and has no counterpart in the tree. The plan
  declines a faction vote on good grounds (a vote is SC's `convene` and `determine` under an
  arrangement; a second-person closer is refused by ruling). The cost is that between "nothing" and
  "march" there is no rung. This is the largest gap the full set shows that the first audit did not
  state, and it is not FA's alone: R-28.
- **"Factions hold people, not territory" is ratified and half-implemented.** The view has `members`,
  `seats` and `holdings`. Nothing weighs them. The design's two weighings are both prose: franchise (a
  territory's weight, DRAFT, never ratified) and "the number of people and the weight of their
  positions" (RATIFIED sentence, no formula). The code's nearest quantity is a march's muster weight
  (`Person.weight` summed over those present). A faction's standing among factions therefore has no
  reading at all, which is why nothing can rank a rival, price a treaty or choose a target: R-29.
- **The ladder is the design's answer to "what does a member do"; the code's answer is the verb table.**
  The eight-rank ladders are 60 per cent of the faction design by volume and almost wholly content:
  titles, gates, halls, livery, mentors. Under the code's rule (a seat adds no verb beyond its remit;
  capability gates nothing) most of a ladder row has nowhere to live. What transfers is narrow and is
  already scheduled (CR-32: names and order). What does **not** transfer and should be said plainly: an
  Initiation Duty as a gate, a mentor's die, a hall tier, a caste Ob modifier. Each is a threshold
  producing an outcome, which Layer 1 refuses. No resolution is needed; the ladders stay vocabulary.
- **Succession in the design is a contest of strengths; in the code it is a title.** `successions`
  passes one seat by one title. The design's two-stage rule (who leads, by a resolver over claim
  strength; whether the realm splits, by the deterministic gap) depends on faction statistics the code
  refuses. The part that survives translation is the *trigger matrix* (a sole heir the apparatus
  accepts inherits; otherwise a contest), and CR-35 builds the contest as an election by the faction's
  bench. The split has no owner and should have none until a contest executes: R-30.
- **Treaty expiry at 90 per cent per arc was a balance lever for a stat game.** `treaty_expiration_v30`
  says so itself ("the primary Crown-nerf lever … narratively extreme"). It transfers nothing. The
  shape that does transfer is its alternative, recorded and deferred there: an agreement that lapses
  unless renewed by an act. The tree already has that shape for service (`oblige` with a term, renewed
  by `transfer`, lapsing at MATTER). A treaty with a term is the same rule on a different edge, and the
  plan declined it because it "would widen T-n's maturity close to `commit` edges" (GP-5b). That
  reasoning holds; no change proposed.
- **The Directive is ruled and its content is not built.** F-FA-18.

### B3.4 The scripting-drift test, re-applied with the full set in hand

The archived faction code that the flow skeleton traces *was* scripted in the sense the brief means: a
faction drew one random number per season and dispatched on `faction.name` to a Crown or Church branch,
every other name falling through to a default (`factions_flow_skeleton_v1` S2.4.1). That code is gone.
The season loop has no such branch (first audit §5.3, re-checked by reading `loop/sides.py`,
`effects_army.py` and the wrapper: each dispatches on the prize's module or the Record's kind, never on
an entity). One place deserves a second look and passes: `army_presets` gives every unplayed faction
the same doctrine, folded between seasons and outside any person's budget. It is a harness, called by
nothing, and says so; if it is ever installed at build (MB's R-07) it becomes a per-faction script the
day two factions are given different plans in Python. The plan belongs in data on the Record or it
belongs to the commander's own choices.

### B3.5 The shortest playable loop

The standing requirement asks for a governance scenario a player can play and an NPC realm that governs
itself. With the full design read, the loop the design keeps returning to is one sentence: **an office
receives an order it cannot fully satisfy, answers it, and is kept, recalled or replaced for the
answer.** Every layer of the archived set has it (the Directive vise; Required Obligations and the
Demotion Trigger; Leadership Deviation; the recall). It needs five links, and the tree has the verbs
for all five:

| link | verb | today | made to execute by |
|---|---|---|---|
| 1. an order is issued to a named officer | `issue` | executes (91 writs in nine realm seasons, first audit E-5) | — |
| 2. the officer answers | `comply`, `evade / defy`, `construe` | never forms on an addressed writ | first lane P1 |
| 3. the issuer notices and responds | `revoke` (also `open_case`, `arrest`) | forms, never attempted | first lane P1 (the recall occasion) |
| 4. the seat falls vacant | `revoke`'s close; a term; a death; `release` | deaths only | first lane P3; `…seat_terms_by_body_B` |
| 5. the seat is filled, by someone chosen for a reason | `confer`; `succeed` | formed, never attempted | first lane P3, P6 |

**The player's scenario** is the first lane's `order` and `vacancy` situations run as one season pair
on the spine: the player is the Count of chain `a`; the Sovereign issues a writ naming him; he answers;
if he defies for the threshold's seasons the Duke's question carries his seat; the Duke revokes or does
not; if revoked, the seat is vacant and the Duke's next question carries the vacancy. The end
conditions are the first lane's. Nothing new is needed to play it but the three proposals above; what
is missing is a statement that this, and not three separate situations, is the subsystem's game, and an
instrument line that says whether the loop closed.

**The self-governing realm** is the same five links with no player, counted on the built realm. Today
the count is 1 of 5 (link 1). The exit is all five at least once, by different persons, in one seeded
run, with a control arm that reproduces today's hash. `06_FA_shortest_loop_B.md` states both as one
gate over the existing instrument and adds nothing to the game path.

What this loop deliberately leaves out, because each needs a mechanism that does not execute yet: a
vote, a treaty, a war. A realm whose officers can be ordered, can refuse and can be replaced is already
a game about governance; a realm that can only march is not.

## B4. The campaign layer for mass battle: the FA side

The referents are Total War (a campaign layer that feeds the battle and receives its result) and
Bannerlord (a party and army economy: recruited, upkept, lost; a commander with authority to call
others). The MB audit judges the battle side and the seam (`04_MB_audit.md` §1.2, §10, §17, §18.1) and
finds the campaign-to-battle-to-campaign half "understood, the best part of the seam; dark and
mis-scaled as shipped". It is not redone here. This section states what FA must supply and receive.

### B4.1 The loop, link by link

| link | archived design | code today | reached in computed play? | FA's part |
|---|---|---|---|---|
| **A reason for war** | casus belli from eight sources; a grievance; a claim | none; a march needs no war | — | CR-91 (claims), CP-T09-02 (b) (the grievance occasion) |
| **Declaration** | a Senator action, or War Authorisation by Parliament vote | `utter` (WAR) + `commit` (C-1) | no | CP-T09-02 (`declare`); F-FA-14 for whose word ends it |
| **Call to arms** | Muster as a Domain Action (Legionary card); a vassal answers the muster (Varfell's first rank is "Answer the Muster") | `mustered`: the seat's faction's members *present* at the actor's origin; `may_muster` at the gate; no call | marches form on whoever is home | CP-T09-07 (a seat's obligees join its army); CP-T09-08 (`dispatch` sends an obligee) |
| **Levy** | a unit raised from a territory's population; type gated by Prosperity and Wealth; Accord 1 raises levy only, Accord 0 nothing (`military_layer_v30` §1.4, §1.5, §4.1) | `recruit` from a cohort, capped by weight and by training Sites; authority is the Record holder's (F-FA-15) | no (withheld) | `06_FA_levy_through_the_seat_B.md` |
| **Command** | the faction's Military stat as the general's Command; a named officer attached at risk | the Record's holder is the commander; "an army is where its commander is" (`mass_battle.py:192-214`); Command is a literal in the module (MB F-MB-14) | no | who commands is an appointment: a seat with the muster act. Capability is §B5 |
| **Movement** | a march budget over an adjacency graph, supply radius, route blocking, a casus-belli check at a border (`march_layer_v30`) | a march reaches any settlement or territory in one act; no graph, no cost | yes, as teleport | SE step 11 (design-first); IN-36's cap of one march a season into a territory; CR-91's gate |
| **Supply** | attrition beyond eight settlements from a supply node; a besieged garrison supplied from an adjacent territory | a ration per *field* from the seat's rung, shipped off; nothing on the march, nothing for an army in being | no | the treasury is the seat's rung (`_seat_treasury`); F-FA-17 |
| **Upkeep** | Wealth 0 costs professional units Discipline; a garrison costs the occupier | sworn service lapses unpaid (`oblige` term, `transfer` renews); raised troops cost nothing to keep | `term.renewed` 0 in every reading | R-31 |
| **The field** | tactic cards; margin of two | `resolve_field` | 3 unopposed arrivals in two seasons at seed 0 (MB §1.3) | none |
| **Result to the campaign** | territory captured; Military −1; five Stability triggers; officer fate (wounded, captured, killed) and ransom | bodies, stance rows, presence, garrison wear, stores | as above | F-FA-13: the holdings and seats half |
| **Occupation to title** | three seasons, or a treaty cession | `occupies` licenses `seize` and `raze` | `seize` 0 | CP-T09-04 |
| **Surrender and terms** | Submit or Resist; capitulation as a treaty type | `surrender` (a seat yields a settlement under a pressed siege) | no (withheld) | lifted from `withheld_verbs` with the army verbs, MB's step 5 |
| **Peace** | mutual treaty, truce, tribute; Stability +1 | `release` of the commit | no | CP-T09-03; F-FA-14 |

### B4.2 The interface FA states

What FA hands the field, each a read that exists:

1. **Who may send.** `Act.via` is a seat whose grant carries the muster act (`MUSTER_ACT`, today
   `dispatch`). After the first lane's P2 that is a seat whose row names it.
2. **Under whose banner.** `seat_faction(via)`, turned into the Proposition id by the one owner
   (`faction_prop_id`). Never the actor's own membership.
3. **Whether the two sides are at war.** `at_war(attacker, defender)`. Layer 1 leaves open whether it
   may gate anything (F.33). It should not gate the march (the plan's "a march needs no war" is right:
   a raid, a relief, a rebellion are marches). It should be *carried on the outcome*, so that what a
   field does to opinion can depend on whether there was a war (R-32).
4. **The treasury.** The rung of the seat exercised (attacker) and the nearest held rung at or above the
   target (defender), as built.
5. **The standing order.** The newest order of battle about the place held by a seat of the faction.

What FA must receive, and does not:

6. **Who lost, by name and office.** `_eff_march` names the losers as persons. Nothing records that
   the *commander* lost: the seat through which the march was ordered is on the act (`via`) and on no
   Event a later question reads as "this officer lost a field". That claim is the natural feeder of the
   recall (the first lane's suspicion fold counts defied writs; a lost field is the other reason a
   superior replaces a subordinate in every referent the design cites, Trigger 5 and the ladder's
   "military failure of a campaign the Senior Jarl commanded"). One more claim kind in an existing fold,
   named in `06_FA_war_lives_in_seats_B.md` edit 7 (b) as a follow-on, not built there.
7. **That the army now stands on someone's land.** `army.arrived` is emitted. CP-T09-04 (d) plans the
   occasion for uncontrolled land only; nothing tells a seat with `issue` that its faction occupies a
   place another faction holds, so `seize` never forms there for a reason. Edit 6 of the same proposal.
8. **Captives.** The design's officer fate (wounded, captured, killed, with ransom) has a carrier in
   the tree (`detain`) and no writer on a field. PC and MB own the write; FA's part is that a captive
   holder's seat is not vacant and cannot act, which `restrained` already gives the muster and would
   need to give `opening_set`. Named, not proposed.

### B4.3 What is left out on purpose

A march budget, a supply line and fog of war are SE's and WR's (the geography file has the edges and no
reader, SE audit step 11). Tactic cards, unit experience and the Military-stat ceiling are refused or
MB's. A war-exhaustion or aggressive-expansion meter is refused as a stored track; if wanted it is a
fold of the log on CR-89's pattern.

## B5. Capability-authoring consequences

The owner is not FA's and is not re-proposed: `rosters.yaml: verb_capability` and `vocation_attribute`
over `references/descriptor_registry.yaml`, read by `faculty` (CHAR's `02_CHAR_capability_uses_table.md`
adds the decision-side table; DICE §14 states what a roll needs). The first lane's
`06_FA_office_capabilities.md` adds vocations for `determine`, `interrogate` and `arrest` and an
optional `vocation:` on a seat. The full design set adds four things to that picture.

1. **The design's office capabilities are access, and access is already data.** Every "Granted Access"
   cell in the ladders (speak in the Crown's name, convene Bannerets, initiate a minor Domain Action,
   chair a committee, conduct trials) is a remit act, a purview or an arrangement row in the code. A
   designer adds one by editing a seat's `remit_acts` or an arrangement, never engine code. The ladders
   therefore need no capability system; they need CR-32 (posts) and the first lane's P2.
2. **Statecraft, law and diplomacy are three vocations the verb table has no row for.** The contested
   governance verbs the plan adds will each roll: `declare` does not (it is an utterance); a treaty's
   acceptance does not; `determine` does (first lane: `judgment`). What the design calls Influence
   (positioning in a negotiation), Mandate (ratification) and Command (the general) are faction
   statistics there and have **no person-side heir** in the code. Two do have a natural one and one
   does not: Command is a vocation of the person who commands the field (`arms` exists; the design's
   Command is closer to a separate `command` vocation whose attribute is Presence or Reason, content
   for Jordan), read by the mass-battle input where a literal 4 sits today (MB F-MB-14 owns the seam).
   Negotiating skill is `argue`'s existing vocation. Mandate has none and should have none: it is other
   people's regard, which the code already computes person by person.
3. **A seat's vocation should feed three readers, not one.** The first lane has it rank the conferee.
   The campaign layer gives it two more: the commander chosen for an army (the same ranking, on the
   seat that carries the muster act), and the estimate a march is weighed by (`field_estimate` exists
   and is the player's only, MB §16). Same key, same loader, no new field.
4. **Rank as a capability is the one thing the design has and the code should not copy.** A Standing
   number that adds dice, lowers obstacles and unlocks actions is the tabletop convention the ladders
   are written in. The code's ruled axiom is that capability supplies dice and gates nothing and that a
   seat adds no modifier. A designer who wants "a Seneschal is better at this than a Retainer" writes it
   as a vocation the Seneschal holds, gained by practice in office (the first lane's §14 (c) 3), and
   the ladder row names the post.

**The interface FA needs, restated with the campaign layer included:** `faculty(person, verb)` and its
opposition twin at a roll; `vocation_of(seat)` for ranking a conferee or a commander; and one input the
mass-battle projection takes from a person where it takes a constant today. FA reads no attribute by
name.

## B6. Resolutions and proposals

### B6.1 Resolutions (continuing the first audit's table)

| id | inconsistency, gap or unclear passage | resolution | step | carried by |
|---|---|---|---|---|
| R-22 | Layer 1's battle roster contract names stakes (holdings, seats); the code passes and writes none (F-FA-13) | keep β (a field writes presence; title is a second act); widen CP-T09-04 (d)'s planned occasion from uncontrolled land to any land the seat's faction occupies, so the taking forms for a reason after an arrival | 3 (`_eff_march`'s own recorded choice; CP-T09-04), then 5 | `06_FA_war_lives_in_seats_B.md` edit 6 |
| R-23 | F.32 open in Layer 1: whose edge a war is; under the plan, peace needs every committer (F-FA-14) | a war is de jure while a committer holds a seat of either party carrying the muster act; rank-and-file commits are the de facto share | 5 | `06_FA_war_lives_in_seats_B.md`; §B6.2 item 1 |
| R-24 | men are levied by a Record's holder, stores by a seat (F-FA-15) | `recruit` and `discharge_troops` through a seat with the muster act whose purview reaches the cohort's residence; one army per faction stays; the Record's holder must be that seat's holder to command | 4 (`requisition`, `march`, `may_muster`) | `06_FA_levy_through_the_seat_B.md` |
| R-25 | five factions have no head (F-FA-16) | `head_seat` gains the Grand Master and the Restoration Leader; the Guilds stay headless by design, stated on the roster | 3 (the rows exist; `factions_personal_v30` §8.6 for the Guilds) | `06_FA_seat_terms_by_body_B.md` edit 4 |
| R-26 | which seats take a term (C-6) | by body, from the design's own tenure rules: a term on the two rotating posts; `null` on life seats, whose turnover is removal by their body | 3 | `06_FA_seat_terms_by_body_B.md` |
| R-27 | what a writ may order (F-FA-18, H-44) | a closed set of term shapes, each performed by an existing verb through `terms_sourced`; first shape a demand of stores; built only after an answered writ is observed | 3 (the design's Directive set; `terms_sourced`), then 5 | this table; design-first, no file |
| R-28 | nothing stands between "no act" and "march" between factions (B3.3) | not a faction vote. The plan's own alliance-and-peace shape (a `covenant` whose terms are a Proposition, accepted by `commit`) is the general instrument; a sanction is a `covenant` among third parties whose terms are a claim against the target. No new verb; it waits on `covenant` executing | 4 (CP-T09-03) | this table |
| R-29 | "the number of people and the weight of their positions" has no reading | one Query, `faction_q.weight(f)`: the summed `Person.weight` of members, plus the muster weight their seats can call (`guard_weight` where built). Read by instruments first; by a chooser term only when a planned position needs it (CP-T09-02's target choice). No stored value | 5 | this table; shape only |
| R-30 | who owns a split realm | nobody, until a contested succession executes. `provinces_of` already makes a province vanish when its territories diverge, which is the split's geography for free | 2 (no subject yet), 3 (`scale_hierarchy_v1` §2) | this table |
| R-31 | an army in being costs nothing | upkeep is a property of service, and the tree has one rule for it: an `oblige` with a term, renewed by `transfer`. Troops raised by `recruit` are a cohort's people under arms; while raised they should not `work`. That is SE's census, and it is the cost that bites without a new charge | 4 (`oblige` and `transfer`; MB T-MB-5 "raising troops removes a cohort, not a number") | cross-listed to `07_SE_population_census.md` |
| R-32 | whether `at_war` may reach a verb's `requires` (F.33) | no. It reaches the *outcome*: a field's Events name the war Proposition when one is live between the two factions, so claims about the field are claims about the war | 5 | `06_FA_war_lives_in_seats_B.md` edit 3 |
| R-33 | the first lane's §13 row for NPC-089 ("she may `march` and `issue`") | still true; add that she cannot raise a man (F-FA-15) and her treasury is empty (F-FA-17), so "probe, pressure, invasion" has one rung | 3 | this table |
| R-34 | `faction x` in the faction roster | leave; exclude from every count by name in instruments | 3 (`names_index.yaml:317`) | this table |

Thirteen rows; twelve decided, one (R-23) decided and also listed for Jordan.

### B6.2 For Jordan (additions to the first audit's §11)

**1. Whose word ends a war.** Layer 1 D-48 and `04:460` say `at_war` is "over live `commit`s to a WAR
Proposition". Two defensible games:

- *(A) Any committer (as ratified).* War is a popular fact: while one person still holds to it, it is a
  war. Declarations are cheap to keep alive and hard to end; a peace is a negotiation with every
  zealot. With rallying built, most wars never end.
- *(B) The seats that wage it.* War is an act of office: it lives while someone who can order a muster
  is committed to it, passes to his successor as a decision, and ends by the word of those officers.
  Popular commitment is how many will come when called. Wars begin and end by named persons in named
  seats, and a succession can be a peace.

The proposal takes (B). It is a narrowing of a ratified sentence, so it is Jordan's.

**2. Franchise.** `franchise_v30` is DRAFT and never ruled: a territory's political weight, lowered for
the southern Einhir, movable by good rule and by caste reform. It is the one place the archived design
gives the caste system a strategic expression. Without a parliament it has no reader. Two options:
leave it archived until something votes (the default taken here), or author it as a datum on territory
rungs now so that `faction_q.weight` (R-29) weighs a member by where he sits. The games differ in
whether caste is felt above the personal scale. Not decided here; it is content with a canon reach.

## B7. Evidence log

All with `PYTHONHASHSEED=0` at `6eff039`. Outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/FA_B/`. No season
was run and no `aperture` was run; every reading of computed play is the first audit's (its E-3 to E-6)
or the MB audit's, cited as such.

| id | command | seed | outcome |
|---|---|---|---|
| E-B1 | `build_probe.py 0` (read-only; `build_realm(0)`, no season) | 0 · build | 83 persons, 34 offices, 414 rungs (realm 1, duchy 3, territory 18, settlement 38, community 60, hearth 211, person 83; no province rung), 2 records (both `works`), 70 Propositions (HOLDS 4, OUGHT 66; no WAR); live tenures: contain 411, reside 83, commit 148, hold 52 (34 offices, 16 territories, 2 records), oblige 4 (none termed); offices by conferral: appointed 18, elected 8, inheritance 1, none 7; by revocation: none 19, `rung_above_same_faction` 13, `rung_above_in_holdings` 2; seats carrying each remit act: dispatch 26, issue 19, convene 13, determine 8, confer 7, revoke 7; rungs with non-empty stores 0; ten faction Propositions, head `None` for five, `fac_faction_x` empty; `at_war` true for no pair; no army Record (`build_probe_0.txt`) |
| E-B2 | YAML read of `offices.yaml` | n/a | 31 seat rows and 2 foreign rows; the eight `elected` rows are `off_duke_varfell`, `off_confessor`, `off_commune_rep_hm`, `off_guild_comptroller`, `off_senior_jarl_west`, `off_skald_chief`, `off_military_jarl`, `off_restoration_leader`; no row has `body: Parliament` |
| E-B3 | YAML read of `verb_table.yaml`, `arrangements.yaml`, `rosters.yaml: terms_sourced` | n/a | 67 rows; the army verbs are `own` on `held_by`; `march`, `marshal`, `surrender`, `raze`, `capture`, `arrest` are `remit:dispatch`; `seize`, `requisition`, `covenant` are `remit:issue`; nine arrangement rows including `parliamentary_debate`; `terms_sourced` has one cell, `commit: [dispensation, petition]` |
| E-B4 | `grep` for `at_war`, `WAR_MOOD`, `withheld_verbs`, `field_provisioning`, `default_upkeep` in non-test Python | n/a | `at_war` read at `world_q.py:3703` (`enemies_heard`) and `:5150`, and by `harness/strife.py`; `fixtures.py:809`, `:1117`, `:1157` |
| E-B5 | read of `tests/test_faction_q.py:223-262` (not run: no pytest) | n/a | the test folds `utter` (WAR), `commit`, `release` and asserts `at_war` False, True, False |
| E-B6 | `git ls-files` for `systems/factions`, `engine/mc_v18.py`, `engine/autoload`, `engine/cross_scale` | n/a | none present; `systems/` holds `characters`, `combat`, `fieldwork`, `mass_battle`, `overview`, `settlements`, `social_contest`, `threadwork`, `world` |
| E-B7 | JSON read of `registers/editorial_ledger_fa_archive.jsonl` | n/a | 49 rows; `ED-FA-0001` once, `ratified`; `ED-FA-0008` superseded 2026-10-06; `ED-FA-0020` ratified |
| E-B8 | `awk` line-length census of the 28 faction design files and 18 cross-cutting ones | n/a | three lines over 1,900 characters in two faction files (longest 2,393: `faction_layer_v30:95`, `:211`, `factions_personal_v30:351`); none in the cross-cutting set. Each of the three was read to its end (their closing words are in the read) |
| E-B9 | `levy_probe.py 0` (in-memory world only; hand-built acts through the real fold between seasons, the `army_presets` route) | 0 · build | Varfell: `p_npc_002` (no seat) mints `army_fac_varfell_0` and `recruit`s 60 levy from `cohort_set_s_026` (`army.recruited`); the same `recruit` by the Duke `p_npc_052` is `recruit.refused`. Guilds, Restoration Movement, Löwenritter: an unseated member mints the army; raisable cohorts 0 (`levy_probe_0.txt`) |

`git status --short` at the end of the lane is recorded in §B8.

