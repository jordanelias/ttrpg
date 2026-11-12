# 21 · PROCEDURAL B — the cast in three tiers through one person generator; local seats filled by acts

Reconciled: 2026-11-12, U5d closure — folded **A-44**, **A-15**, **A-41 / A-42** and **A-19**. The hold on decision D-1 is lifted: about 94 generated persons plus kin, capped, with `cast_cap` the dial (it overwrites `ED-WR-0011` by Jordan's answer). `Person.born` is written for every generated person, and the 46 principals' ages are now owed content (A-15 turns natural death on only after they are authored); `22_HAPPENINGS_A` edit 1 is the one writer from authored ages and this file's generator writes through the same field. Heritage is generated per person, and the caste tiers that read it are data (`U5d_SE_cohort_heavy_moves_and_caste.md` edit 4; the territory weight of `U5d_FA_owed_edits.md` §4). Local seats are filled by `confer` in the prologue; an empty inherited seat is claimed in the deed race (A-19), so a generated kinsman is a possible claimant only through a listed title.

## Status: PROPOSED (2026-11-12; Fable design lane; ratifies nothing; reference under CLAUDE.md §0.05). HELD BACK on decision D-1 (it overwrites `ED-WR-0011`, RULED).

Carries `audits/21_PROCEDURAL_GENERATION.md` §4.4, §4.5, §14, resolutions R-21-04, -09, -12; plan batches
**PG-2** and **PG-3**. Depends on `21_PROCEDURAL_A_worldgen_tables_and_ground.md` (the switch, `pick`,
`spread`, `RealmPlan`).

## 1. What changes in `engine/season/` at runtime

With `variable=False` or an empty `cast_quota`: nothing.
With them on: the build mints a generated supporting cast beside the 46 authored persons (kin, keepers,
local claimants, rivals, creditors), each with a name, heritage, birth season, attribute ranks from a
lifepath, pursuits with a possible deviation, and relations written as stance rows and firsthand claims.
Local seat templates are instantiated per settlement and stand vacant until a person's act fills them.
When CENSUS individuates a demanded person, it draws that person with the same function.

## 2. The problem, with evidence

- The cast is 46 authored persons and 37 cohorts. `Person.born` is 0 for 83 of 83; `heritage` is unset for
  79; no person holds an attribute in the shipped arm; there is no kin, no debt and no rival that is not
  hand-authored; 0 Events exist at build (audit §12, P1, P3).
- All 33 seats are held by principals; no settlement has a local office (P3). A villager's petition, a
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
2. **One function, two call sites:** `generate_person` serves the build and CENSUS.
3. **Slots, not a head-count:** a generated person exists because a structural role needs filling (kin of a
   principal, keeper of a serving building, claimant to a local seat, rival for a contested seat,
   counterpart of a debt). No slot, no person.
4. **Capabilities by lifepath, referencing the one definition table.** The generator defines none.
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
cast_cap: 120                      # hard ceiling on generated persons at build; the dial for D-1 and for season cost
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
min_parent_age: 64                 # seasons between a parent's birth and a child's (16 years IF a year is 4 seasons: the generator reads the year's length from the roster `world_q.season_of_year` reads, and this value is in seasons)
age_bands:                         # seasons before tick 0, [lo, hi], by slot; written to Person.born as a negative int
  heir: [64, 120]
  keeper: [100, 240]
  elder: [200, 280]
deviation: 333                     # per thousand: chance one pursuit is re-drawn from the opposite end of the local distribution
relations_per_person: 3            # drawn relations beyond the slot's anchor relation
seed_claims: 6                     # firsthand claims a generated person starts with, about own relations and place
lifepaths:
  origin:                          # weights by settlement type of birth; deltas name capability ids from the definition table
    hearth_born:   {weight: {Village: 5, Town: 3, City: 1}, adds: {endurance: 1}}
    street_born:   {weight: {Town: 2, City: 4, Seat: 4},    adds: {attunement: 1}}
    hall_born:     {weight: {Seat: 2, City: 1, Fortress: 1}, adds: {presence: 1}}
  formation:                       # weights by institution of the slot (null = unaffiliated)
    apprenticed:   {weight: {Guild: 5, null: 2},  adds: {focus: 1},     practice: {craft: 1}}
    schooled:      {weight: {Church: 4, Einhir: 4, Crown: 2}, adds: {cognition: 1}, practice: {letters: 1}}
    mustered:      {weight: {"Löwenritter": 6, Altonian: 6, Crown: 1}, adds: {endurance: 1}, practice: {arms: 1}}
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
  heirs: all                       # every seat whose conferral is `inheritance` has a living eligible heir
```

Capability ids in `adds:` and practice keys are **references**: `worldgen.load` checks each against the
capability definition table and refuses an unknown id by name. The ids above are the nine of the present
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
`:1315-1321`), `born`, `heritage`, `attributes` (through `Person.attributes`, the CR-20 carrier; this
requires `cast_attributes` semantics for generated persons regardless of that switch's default for the
authored cast, and says so in the docstring), `pursuits`, stance rows and seed claims.

**(d) `engine/season/loop/census.py`** (the individuation site): the minted person is
`generate_person(w.world_seed, Slot(key=f"census:{demand_event_id}", role=<the demanded post's vocation>,
home=<the demanding rung>, …), …)`. Same tables, same draws, keyed by the demand, so a replay
individuates the same person.

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

- **PG-2**, `--range 20`: cast size within `cast_cap` in every world; 0 name collisions; V1 clean. Play,
  3 seeds × 2 seasons: every generated person acts at least once; acts whose subject is a generated person
  number more than zero; the share of resolved acts by generated persons is printed. Variety: two worlds
  share fewer than half their generated relation pairs when pairs are keyed by (role, role, kind).
  Character: the CHAR audit's Kendall reading over fifteen candidates separates two generated persons with
  opposed pursuits (negative tau) and not two with near-equal ones. Control: `cast_quota: {}` gives PG-1's
  hash. A demanded person (a `dispatch` to a post nobody holds, the row 9 acceptance case) is individuated
  with relations into the place and acts in the following season.
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
  customization by table; a person arriving mid-game is as formed as one present at the start. Risk named:
  a cast the player cannot remember (RimWorld's 12 against Dwarf Fortress's 200); `cast_cap` is the dial
  and D-1 the decision.
- **S:** one generator for build and CENSUS; relations and attributes on carriers that exist; no second
  capability scheme; seats filled by the same verbs play uses.
- **E, last:** three tables and one function against a realm with a society in it. The slot rule keeps the
  count tied to roles that have readers.

## 8. Cost and dependencies

PG-2: design-first (D-1), then small build. Needs `02_CHAR_capability_definitions.md` and
`01_CORE_capability_authoring_surface.md` (the definition table), `02_CHAR_relations_have_a_ground.md`
(the relation carrier), `07_SE_population_census.md` (CENSUS as the one writer of weight).
PG-3: small build. Needs `06_FA_seat_terms_and_turnover.md`, `06_FA_seat_terms_by_body_B.md`,
`14_VERBS_BINDING_C_turnover.md` (conferral and election executing), `08_FI_01_claim-sourced-referents.md`
(a vacancy reaches a person as a claim), and the institution lanes' accomplishment query and Roll.
