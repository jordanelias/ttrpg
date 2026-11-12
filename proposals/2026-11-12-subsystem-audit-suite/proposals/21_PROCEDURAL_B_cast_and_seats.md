# 21 · PROCEDURAL B — the cast in three tiers through one person generator; local seats filled by acts

Reconciled: 2026-11-12, U5d closure — folded **A-44**, **A-15**, **A-41 / A-42** and **A-19**. The hold on decision D-1 is lifted: about 94 generated persons plus kin, capped, with `cast_cap` the dial (it overwrites `ED-WR-0011` by Jordan's answer). `Person.born` is written for every generated person, and the 46 principals' ages are now owed content (A-15 turns natural death on only after they are authored); `22_HAPPENINGS_A` edit 1 is the one writer from authored ages and this file's generator writes through the same field. Heritage is generated per person, and the caste tiers that read it are data (`U5d_SE_cohort_heavy_moves_and_caste.md` edit 4; the territory weight of `U5d_FA_owed_edits.md` §4). Local seats are filled by `confer` in the prologue; an empty inherited seat is claimed in the deed race (A-19), so a generated kinsman is a possible claimant only through a listed title.

Reconciled: 2026-11-12, U4 fact check (`unified/U4_FACT_CHECK.md` F-04) — P3's "All 33 seats" is 34 seats held by 33 principals (the King holds `off_king` and `off_duke_valorsmark`; `audits/25_GROUNDING_ENGINE.md` L-02, re-read at the tree: `build_realm(0)` has 34 offices and 83 persons); no other sentence changes.

Reconciled: 2026-11-12, wave 3 lane W3-5b (`unified/work/R5_READ.md` §1 rows cast_and_seats ((d) VIOLATES; `lifepaths.formation` VIOLATES; PG-3 CONFORMS), §2 rows Status (A-44, A-19) and `kin_slots` (A-19), §7, 7b; `unified/U3_CONFLICT_LEDGER.md` C3-L13, C3-K10; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-10; `unified/U3_DEPENDENCY_ORDER.md` §1 item 39, §3.1). The body now follows the head. Changed: (1) the Status line's hold is removed (A-44 answered D-1; `ED-WR-0011` is overwritten by Jordan's answer); (2) edit (d): CENSUS writes no interior (C3-L13, `04` §A.2 `:179`, inv. 5 `:497`, `:244`): a person individuated in play is minted as today (`exists`, with its identity fields, and `weight`; the person rung and `contain` edge), taking only his name and `born` from `generate_person` keyed by the demand; heritage, attributes, pursuits, relations and seed claims are written at world build only, and an arrival gains pursuits by his own first acts and claims by WITNESS; §1, §3 item 2 and the NERS R line follow; (3) `lifepaths.formation` is keyed by institution kind, not by faction names (`04` PART D 27a; this file's own V1); (4) ages are authored in years and converted through the one owner of the year (D-U1-10), not as seasons that restate "4"; every generated person is aged through `22_HAPPENINGS_A` edit 1's writer of `Person.born` (C3-K10); (5) `bars.heirs` states that A-19's deed race reads the claimant set; (6) tests named; (7) dependency, batch and tier lines. A-98 vocabulary lane (2026-11-12, A-98; ledger `unified/work/A98_SWEEP.md`): "capability" in prose → skill (5).

Depends on: `21_PROCEDURAL_A_worldgen_tables_and_ground.md` (B39); `01_CORE_capability_authoring_surface.md`, `02_CHAR_capability_definitions.md` (B04, the definition table); `02_CHAR_relations_have_a_ground.md` (B10); `08_FI_01_claim-sourced-referents.md` (B11); `07_SE_population_census.md` (B12); `20_NARRATIVE_E_the_year_and_the_reason.md` edit 1 (B12, the year); `06_FA_seat_terms_and_turnover.md`, `06_FA_seat_terms_by_body_B.md`, `14_VERBS_BINDING_C_turnover.md` (B21); `15_INSTITUTIONS_BYZANTINE_A_dignities_and_the_roll.md` (B32), `15_INSTITUTIONS_COLONIAL_D_accomplishment.md`, `15_INSTITUTIONS_VENICE_B_debt_instrument.md` (B33); `22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn.md` (B37, the `born` writer); `U5d_SE_cohort_heavy_moves_and_caste.md` (B38).
Lands in batch: B39 (lanes WR / CHAR / FA), after `21_PROCEDURAL_A`; PG-2 and PG-3 one commit each; the census edit (d) its own commit with its test.
Tier: opus for the CENSUS reading (taken above) and the faction-kind roster; sonnet / high for the tables, generator and tests.

## Status: PROPOSED (2026-11-12; Fable design lane; ratifies nothing; reference under CLAUDE.md §0.05). A-44 taken: decision D-1 answered (about 94 generated persons plus kin, capped; `cast_cap` the dial), `ED-WR-0011` overwritten by Jordan's answer.

Carries `audits/21_PROCEDURAL_GENERATION.md` §4.4, §4.5, §14, resolutions R-21-04, -09, -12; plan batches
**PG-2** and **PG-3**. Depends on `21_PROCEDURAL_A_worldgen_tables_and_ground.md` (the switch, `pick`,
`spread`, `RealmPlan`).

## 1. What changes in `engine/season/` at runtime

With `variable=False` or an empty `cast_quota`: nothing.
With them on: the build mints a generated supporting cast beside the 46 authored persons (kin, keepers,
local claimants, rivals, creditors), each with a name, heritage, birth season, attribute ranks from a
lifepath, pursuits with a possible deviation, and relations written as stance rows and firsthand claims.
Local seat templates are instantiated per settlement and stand vacant until a person's act fills them.
When CENSUS individuates a demanded person, it takes his name and birth season from the same function and
writes nothing of his interior (C3-L13): he begins thin and is formed by his own acts and what he
witnesses.

## 2. The problem, with evidence

- The cast is 46 authored persons and 37 cohorts. `Person.born` is 0 for 83 of 83; `heritage` is unset for
  79; no person holds an attribute in the shipped arm; there is no kin, no debt and no rival that is not
  hand-authored; 0 Events exist at build (audit §12, P1, P3).
- All 34 seats (held by 33 principals: the King holds two, `audits/25_GROUNDING_ENGINE.md` L-02; U4 fact check
  row F-04) are held by principals; no settlement has a local office (P3). A villager's petition, a
  local inquiry and a contested small office have nobody to hold them.
- The provided cases assume heirs, rivals, creditors and clerks the corpus does not seat
  (`audits/12_ARCS_adjudication.md` §2.2: one template world; open roles unbound).
- The lawful mid-game generator exists and draws nothing: CENSUS individuation mints a person on demand
  (`04_CODE_ARCHITECTURE.md` PART E row 9), and the hole register asks what such a person *is*
  (`hole_register.yaml:584`).
- Ruling in the way: `ED-WR-0011` (RULED 2026-09-13): "World-gen NPC count, for now, is just the 46 NPCs we
  built. We will return much later." It is provisional by its own terms and is decision D-1.

## 3. The resolution, decided

1. **Three tiers** (audit §4.4): A the authored principals, untouched; B a generated supporting cast at
   build; C cohorts, individuated on demand.
2. **One function, two call sites:** `generate_person` serves the build (the whole plan) and CENSUS (the
   name and `born` only; `04` §A.2 `:179` licenses CENSUS `exists`, `weight`, `envelope`, and inv. 5
   keeps interior cells at RESOLVE and WITNESS, C3-L13).
3. **Slots, not a head-count:** a generated person exists because a structural role needs filling (kin of a
   principal, keeper of a serving building, claimant to a local seat, rival for a contested seat,
   counterpart of a debt). No slot, no person.
4. **Skills by lifepath, referencing the one definition table.** The generator defines none.
5. **Relations on existing carriers** (`02_CHAR_relations_have_a_ground.md`): a stance row and a firsthand
   claim with the ground.
6. **Generated persons never enter `npcs.yaml`** (its header forbids inventing a row there). They are
   minted from tables; the table row and the draw key are the author (AX-6).
7. **Seats are filled by acts.** Local seats ship vacant; the prologue (proposal C) is where the
   conferring seat-holder's `confer`, or the body's election, fills them by draw. A build with no prologue
   fills them by a keyed weighted draw over eligible candidates. Never by rank order.
8. **No rank is defined here.** Deed standing is the institution lanes' per-viewer query
   (`15_INSTITUTIONS_COLONIAL_D_accomplishment.md`: `person_q.accomplishment`); this proposal supplies
   pedigree Records and reads the query for weights.

## 4. Exact edits

### PG-2 — the person generator

**(a) `engine/season/worldgen.yaml`:**

```yaml
cast_cap: 120                      # hard ceiling on generated persons at build; the dial A-44 names (D-1 answered) and for season cost
cast_quota:                        # generated keepers and locals per settlement, by type (sums to 94 on the canon map)
  Seat: 6
  City: 5
  Cathedral-City: 5
  Fortress-City: 4
  Town: 3
  Fortress: 2
  Village: 1
kin_slots:                         # per principal, each filled with the stated chance (integers per thousand), keyed by (case id, slot)
  heir: 600
  spouse: 500
  sibling: 400
  parent: 250
min_parent_age_years: 16          # years between a parent's birth and a child's; converted to seasons by len(rosters.yaml: seasons_of_year) (D-U1-10), never by a typed 4
age_bands_years:                   # years before tick 0, [lo, hi], by slot; the generator draws a season count in [lo × Y, hi × Y] (Y = len(SEASONS_OF_YEAR)) and writes it through `22_HAPPENINGS_A` edit 1's one writer of Person.born (C3-K10)
  heir: [16, 30]
  keeper: [25, 60]
  elder: [50, 70]
deviation: 333                     # per thousand: chance one pursuit is re-drawn from the opposite end of the local distribution
relations_per_person: 3            # drawn relations beyond the slot's anchor relation
seed_claims: 6                     # firsthand claims a generated person starts with, about own relations and place
lifepaths:
  origin:                          # weights by settlement type of birth; deltas name skill ids from the definition table
    hearth_born:   {weight: {Village: 5, Town: 3, City: 1}, adds: {endurance: 1}}
    street_born:   {weight: {Town: 2, City: 4, Seat: 4},    adds: {attunement: 1}}
    hall_born:     {weight: {Seat: 2, City: 1, Fortress: 1}, adds: {presence: 1}}
  formation:                       # weights by the KIND of the slot's institution (none = unaffiliated); never by a faction's name (04 PART D 27a)
    apprenticed:   {weight: {guild: 5, none: 2},  adds: {focus: 1},     practice: {craft: 1}}
    schooled:      {weight: {church: 4, tradition: 4, ruling_house: 2}, adds: {cognition: 1}, practice: {letters: 1}}
    mustered:      {weight: {order: 6, foreign_crown: 6, ruling_house: 1}, adds: {endurance: 1}, practice: {arms: 1}}
  vocation:                        # the slot's role fixes this row; it is not drawn
    priest:  {adds: {grace: 1},    practice: {rite: 1}}
    factor:  {adds: {cognition: 1}, practice: {accounts: 1}}
    reeve:   {adds: {presence: 1},  practice: {law: 1}}
    captain: {adds: {focus: 1},     practice: {command: 1}}
    kin:     {adds: {}}
relations:
  kinds:                           # each: the stance seed band toward the other, and whether it is mutual
    kin:       {stance: [1, 2],   mutual: true}
    patron:    {stance: [0, 2],   mutual: false, inverse: client}
    rival:     {stance: [-2, -1], mutual: true,  ground: required}
    creditor:  {stance: [-1, 1],  mutual: false, inverse: debtor, ground: required}
    comrade:   {stance: [1, 2],   mutual: true}
    enemy:     {stance: [-2, -2], mutual: true,  ground: required}
  weights_by_reach: {same_hearth: 5, same_institution: 4, same_settlement: 3, kin_of_kin: 2, same_territory: 1}
bars:
  rival_pairs: 6                   # pairs with opposed top pursuits who share a venue or an institution
  heirs: all                       # every seat whose conferral is `inheritance` has a living eligible heir; A-19's deed race reads the claimant set (a generated kinsman claims only through a listed title, `22_HAPPENINGS_B`); the bar guarantees a claimant, never a winner
```

**Formation keys are institution kinds** (R5 §1; `04` PART D 27a: a proper noun in a rule-bearing file is
a scenario declaration or a defect; G.1.6: a rule that branches on a member is drift). The kinds are a
closed roster added in this commit, `rosters.yaml: faction_kinds: [guild, church, tradition,
ruling_house, order, foreign_crown, movement]`, and a map `rosters.yaml: factions.kind` beside
`head_seat` giving each faction its kind (the world roster, which 27a licenses to name factions)
[ASSUMPTION: medium; the seven kinds and each faction's kind are this file's draft, Jordan to correct —
basis: no `kind` key exists in `rosters.yaml: factions` (read: it carries `from_names: faction` and
`head_seat` only)]. `worldgen.load` refuses a formation key outside `faction_kinds`, naming the row.

Skill ids in `adds:` and practice keys are **references**: `worldgen.load` checks each against the
skill definition table and refuses an unknown id by name. The ids above are the nine of the present
attribute block as the tree names them (CR-20; the `build_realm` docstring lists cognition, focus,
endurance, attunement, presence, grace) and are placeholders for whatever
`02_CHAR_capability_definitions.md` and `01_CORE_capability_authoring_surface.md` settle; this file holds
no definition. A relation kind with `ground: required` writes a claim stating the ground (the debt's
amount and term; the seat both want; the injury), so the grievance can be found by a reader.
A `creditor` relation uses the debt instrument once it exists (`15_INSTITUTIONS_VENICE_B_debt_instrument.md`);
until then it is a stance row and a claim only, and the sheet marks it unsecured.

**(b) `engine/season/data/worldgen.py`:**

```python
@dataclass(frozen=True)
class Slot:
    key: str                       # stable: "kin:NPC-020:heir", "keeper:S-006:chapel", "local:S-006:reeve", "rival:off_x", "census:<demand event id>"
    role: str                      # a lifepaths.vocation row
    home: str                      # an anchor form build_realm already resolves ("S-006:chapel")
    institution: str | None
    anchor: tuple[str, str] | None # (relation kind, other person's key) fixed by the slot

@dataclass(frozen=True)
class PersonPlan:
    key: str; name: str; heritage: str; born: int; home: str; institution: str | None
    attributes: Mapping[str, int]; practice: Mapping[str, int]
    pursuits: Mapping[str, float]; deviated: str | None        # which pursuit was re-drawn, for the sheet and the tests
    relations: tuple[tuple[str, str, int, str | None], ...]    # (kind, other key, stance, ground)
    claims: tuple[tuple[str, str, object], ...]                # (subject, predicate, value), firsthand

def slots(seed: int, tables: dict, canon: dict, cast_rows: list, venues: dict, attempt: int = 0) -> tuple[Slot, ...]: ...
def generate_person(seed: int, slot: Slot, tables: dict, reach: Mapping[str, tuple[str, ...]], attempt: int = 0) -> PersonPlan: ...
```

`generate_person` is pure. Every field is one `pick` or `spread` keyed by `slot.key` and the field name.
`reach` is the set of person keys within each reach class of the slot (computed by the caller from the
plan so far, in sorted-key order, so the result does not depend on iteration order). Names come from
`worldgen_names.yaml` (proposal E); until that lands, the name is the role and the settlement ("the reeve
of Goldenfurt"), which is unique and collision-free.

**(c) `engine/season/harness/populated.py::build_realm`**, after the authored cast and cohorts are seated
and when `variable` is true: `plan.persons = [generate_person(…) for slot in slots(…)]` truncated at
`cast_cap` in slot-priority order (kin, local seat claimants, keepers, rivals, creditors); then for each:
the same minting the authored cast gets (`Person`, its `person` rung, `contain` and `reside` tenures;
`:1315-1321`), `born` (through `22_HAPPENINGS_A` edit 1's one writer, C3-K10), `heritage`, `attributes`
(through `Person.attributes`, the CR-20 carrier; this requires `cast_attributes` semantics for generated
persons regardless of that switch's default for the authored cast, and says so in the docstring),
`pursuits`, stance rows and seed claims. This is world build (`04` §F.31: the world-generation roster),
not CENSUS, so every field may be written here.

**(d) `engine/season/loop/census.py`** (the individuation site; C3-L13): CENSUS individuates the
demanded person as today (`loop/census.py:105-109`: `Person(pid, …, born=…)`, the person rung, its
`contain` edge, weight 1 from the envelope), i.e. the cells `04` §A.2 `:179` licenses it (`exists`,
`weight`, `envelope`). Two of the minted tuple's identity fields come from
`generate_person(w.world_seed, Slot(key=f"census:{demand_event_id}", role=<the demanded post's vocation>,
home=<the demanding rung>, …), …)`: the name and `born` (in place of today's `pid` and `w.tick -
age_at_build`), keyed by the demand, so a replay individuates the same person. Nothing else of the plan is
written at CENSUS: heritage is written at world build only (`04` `:244`), and pursuits, relations and seed
claims are ACTS and INTERIOR cells (inv. 5, `:497`); the arrival gains pursuits by his own first acts at
RESOLVE and claims by WITNESS. If a generated interior at individuation is ever wanted, it is a Layer 1
question (a matrix row `(Person, pursuits) steps [RES, CEN]` against inv. 5), not built here.

**(e) V1 additions** (`worldgen.invariants`): no name equal to a canon name, a cast name or another
generated name in the same settlement; `born` of a child at least `min_parent_age` after the parent's;
every generated person has a resolvable home, at least one pursuit and at least one relation; no generated
person is the `holder` of an `offices.yaml` seat; no `lifepaths` row is keyed to a proper noun outside
`scenario`.

### PG-3 — local seats and pedigrees

**(f) `engine/season/worldgen.yaml: local_seats, pedigrees`:**

```yaml
local_seats:                       # role templates; one Office per (template, settlement of a listed type); vacant at build
  reeve:   {types: [Village, Town], post: "Reeve", remit_acts: [convene, open_case, determine], conferral: appointed, conferred_by: territory_holder}
  factor:  {types: [Town, City, Seat], post: "Guild Factor", remit_acts: [exchange, requisition], conferral: elected, body: guild_chapter}
  curate:  {types: [Village, Town, Fortress], post: "Curate", remit_acts: [convene], conferral: appointed, conferred_by: church_seat}
  castellan: {types: [Fortress, Fortress-City], post: "Castellan", remit_acts: [marshal, requisition], conferral: appointed, conferred_by: territory_holder}
pedigrees:                         # which generated persons start holding a pedigree Record, and what it may claim
  kinds: [service, gift, fieldwork]        # deed kinds a generated house may claim at build; never a founding deed
  chance: 250                              # per thousand, for a hall_born generated person
bars:
  contested_seats: 3               # seats with a second eligible person who holds a goal row toward them
```

`remit_acts` values must be verbs of `verb_table.yaml`; `conferred_by` and `body` are queries the existing
anchor resolver answers (`resolve_anchor`, `seat_anchor`), never a named person. The post names are
drafts; the roster of posts a seat may carry is `rosters.yaml`'s and each new post is a row there
(`refuse_a_titled_post_off_its_rung` already checks the rung).

**(g) Build:** each template mints an `Office` with no holder at every settlement of a listed type. With
`prologue=0`: the first holder is `pick(seed, seat_id, "seat:first_holder", weights)` over eligible
generated persons of that settlement, the weights being the conferrer's `person_q.accomplishment` reading
of each candidate once that query exists, and equal weights until it does. With a prologue: the seat stays
vacant and the vacancy reaches the conferrer as a claim (`08_FI_01_claim-sourced-referents.md`,
ED-IN-0292), so `confer` is a candidate of his own chooser.

**(h) Pedigree Records:** a Record of kind `pedigree` at the holder's home hearth, `subject_matter` naming
the ancestor (a generated name, no Person) and a deed kind from `pedigrees.kinds`; the holder and his kin
get a claim whose `source` is the Record. The founding deeds and the Roll are **not** minted here: they
are the institution lanes' rows (`15_INSTITUTIONS_BYZANTINE_A_dignities_and_the_roll.md`,
`15_INSTITUTIONS_COLONIAL_D_accomplishment.md`), read by this build if present. V1: no pedigree deed kind
may be one of the founding deed kinds.

## 5. Gate

Tests: `engine/season/tests/test_worldgen_switch.py` (PROC_A's file) gains
`test_lifepaths_name_no_proper_noun_outside_scenario`, `test_formation_key_outside_faction_kinds_is_refused`,
`test_generated_person_is_aged_through_the_one_born_writer` and `test_cast_quota_empty_gives_pg1_hash`;
NEW `engine/season/tests/test_census_generated_arrival.py`: `test_arrival_carries_name_and_born_only`,
`test_same_demand_same_seed_same_person`, `test_census_writes_no_pursuits_heritage_or_claims`,
`test_arrival_acts_in_the_following_season` (the 04 PART E row 9 case: a `dispatch` to a post nobody
holds individuates a person who acts next season, and `person.individuated` cites the demand). The
`--range` readings below are printed by `harness/worldgen.py` (PROC_A (d)); the CHAR audit's Kendall
reading is a scratch probe not in the repository, so that clause is read by
`test_opposed_generated_persons_rank_fifteen_candidates_apart` in the same test file (negative tau for
opposed pursuits, near zero for near-equal ones).

- **PG-2**, `--range 20`: cast size within `cast_cap` in every world; 0 name collisions; V1 clean. Play,
  3 seeds × 2 seasons: every generated person acts at least once; acts whose subject is a generated person
  number more than zero; the share of resolved acts by generated persons is printed. Variety: two worlds
  share fewer than half their generated relation pairs when pairs are keyed by (role, role, kind).
  Character: the CHAR audit's Kendall reading over fifteen candidates separates two generated persons with
  opposed pursuits (negative tau) and not two with near-equal ones. Control: `cast_quota: {}` gives PG-1's
  hash. A demanded person (a `dispatch` to a post nobody holds, the row 9 acceptance case) is individuated
  with a name and `born` only and acts in the following season (C3-L13).
- **PG-3**, after proposal C's prologue: every settlement of a listed type has its local seats, and each
  filled seat's `tenure.opened` cites a `confer` or an election Event (an act filled it). Over 20 seeds the
  holder of a given local seat differs in at least half the worlds. `bars.contested_seats` met in every
  accepted world. With `prologue=0` the same seat is filled by the keyed draw and the test asserts the
  holder is *not* always the highest-weighted candidate across seeds (the no-deterministic rule, observed).

## 6. Falsifiers

- If generated persons never act, or are never the subject of another's act, they are furniture: the slot
  design failed and the quota should fall, not rise.
- If two generated persons with opposed pursuits rank candidates alike, the chooser is not reading what
  was drawn (the CHAR lane's finding, which generation cannot fix).
- If a local seat has the same holder in every world, the fill is a rule wearing a draw.
- If season time rises faster than linearly in cast size, tier B is too expensive and `cast_cap` falls.

## 7. NERS reading

- **N:** cut tier B and cases, succession and local government have only principals to happen to; every
  culprit, heir and clerk is one of 46 or does not exist. What the cut loses is not provided elsewhere:
  cohorts cannot hold a seat, owe a debt or be accused.
- **R:** the no-player half (kin and rivals generate succession and feud with nobody watching);
  customization by table; a person arriving mid-game begins thin and is formed by what he does and sees
  (C3-L13: the intended game, not a loss). Risk named: a cast the player cannot remember (RimWorld's 12
  against Dwarf Fortress's 200); `cast_cap` is the dial (A-44).
- **S:** one generator for build and (name and birth only) CENSUS; relations and attributes on carriers that exist; no second
  skill scheme; seats filled by the same verbs play uses.
- **E, last:** three tables and one function against a realm with a society in it. The slot rule keeps the
  count tied to roles that have readers.

## 8. Cost and dependencies

PG-2: small build (D-1 answered by A-44). Needs `02_CHAR_capability_definitions.md` and
`01_CORE_capability_authoring_surface.md` (the definition table), `02_CHAR_relations_have_a_ground.md`
(the relation carrier), `07_SE_population_census.md` (CENSUS as the one writer of weight).
PG-3: small build. Needs `06_FA_seat_terms_and_turnover.md`, `06_FA_seat_terms_by_body_B.md`,
`14_VERBS_BINDING_C_turnover.md` (conferral and election executing), `08_FI_01_claim-sourced-referents.md`
(a vacancy reaches a person as a claim), and the institution lanes' accomplishment query and Roll.
