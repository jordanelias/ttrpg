# The character sheet — what a person is in code, and one sheet reconciled from it

## Status: PROPOSED (2026-09-30) · design-only · ratifies nothing on merge · reference under `CLAUDE.md` §0.05
## Lane: IN, with PC and WR · IDs: none allocated
## Read at HEAD `c8cc408` (#444 left `Person` unchanged; it added `Claim.teller` and `Tenure.term`, at plan positions `15b` and `17b` — both absent at `b63e1b3`).
## Builds on: `proposals/2026-08-15-character-and-faction-stats-and-progression.md` (held for Jordan) — its attribute census and roster options are not re-derived here.
## Suite: [README](README.md) · [07 saying a weapon is good](07_saying_a_weapon_is_good.md) · [08 mass battle](08_mass_battle_units.md) · **09 the character sheet** · [10 verbs and attributes](10_verbs_and_attributes.md)

**What this answers.** What the season loop and its subsystems track about a character, where each
fact lives, and what one reconciled sheet would hold — including memory, knowledge and the abilities
each subsystem calls for.

---

## 1. Analysis

### 1.1 The carrier

`engine/season/state/carriers.py::Person` is the character the season loop runs on:

| field | what it is |
|---|---|
| `id`, `name`, `weight` | a person at weight > 1 is a cohort — one class (`is_cohort` is a property) |
| `body` | condition on the same fixed-point scale as `Site.condition`, so there is one scale, not two |
| `capability: dict` | skill keyed loosely by capability name (§1.2) |
| `stance: list` | rows of `(referent, valence −5…+5, weight 0…5)`, read by `choose.stance_toward` |
| `pursuits: dict` | `{conviction: weight}` over the 13 convictions of `descriptor_registry.yaml`, projected onto the four axes of its `axis_roster` for `choose` (`data/pursuits.to_axes`) |
| `scar: dict` | per-axis scars, keyed at read time by whatever the axis roster holds — deliberately not pre-seeded, because ED-IN-0261 rules the four axes to become seven bipolar ones (hierarchical↔equal, precedent↔substantive, partisan↔equitable, selfish↔selfless, rigid↔flexible, grandiose↔humble, deontological↔instrumental) |
| `ledger: list[Claim]` | memory and knowledge (§1.4) |
| `travel_leg` | where the person is mid-journey |
| `tenures: list` | every edge the person is the subject of: seats, holds, commitments, bonds, residence. The kinds are an open roster, now eight (`reside` was added at plan position `19c`) |

Nothing in a season writes `capability` or `pursuits`; `scar`'s writer is inert at its default step;
only `march` writes `stance` (a lost battle's grudge).

### 1.2 Capability — one read path, no season writer

A contested verb draws dice from the actor's capability: `rosters.yaml`'s `verb_capability` maps a verb
to a key and `sigma.py::_capability` reads `person.capability.get(key)`; an unset key falls to the
fixture default. Two verbs are mapped — `tell` and `speak`, both to `copying`. The write matrix retires
season writes to the field; the corpus harness writes authored values at build (NPC-088's cast gives
`copying: 3`), and one probe zeroes it. So capability is real, singly owned and read uniformly — and for
nearly every person in a running season it is empty, which is why a social contest varies by seed rather
than by person ([01](01_the_season_loop.md) §1.2). The repository has already named the repair: *"a
`practice` verb, not a field"* (`references/what_valoria_is_and_what_runs.md` §2, row 9).

### 1.3 The combat build lives on a different object

`combat_engine_v1::Combatant` carries strength, agility, endurance, cognition, attunement, spirit,
focus, history and disposition; a `skills` dict on six axes (bind, parry, dodge, balance, technique,
grab); `equipped` techniques with invested levels; a tradition; a weapon; armour. The season seam builds
one per fight with exactly **one** field read from the person — `end`, from `body` bands — and the rest
at class defaults; afterwards it writes `body` back from the fight's remaining health. A character's
tradition, techniques, weapon and armour do not exist between fights. [05](05_two_modes_of_one_bout.md)
§1.1 gives the seam; [04](04_the_bout.md) the build it discards.

### 1.4 Memory and knowledge — the complete part

`Person.ledger` holds `Claim`s: `id, holder, subject, predicate, value, when, source, confidence,
visibility, round, teller`. Claims enter only at WITNESS — by being present, or by being told, in which
case `teller` names who. Queries answer through `LedgerReader`, whose one comparator is the most recent
season, then the most confident; `standing_of` and the deliberation fingerprint read the ledger
directly. No matching claim means **unknown**, never a negative belief. Eviction ranks claims by
`confidence × (when + 1)`; decay subtracts a flat `claim_decay_per_season` from every claim at MATTER.
This is where the design's hardest
canon property becomes mechanism: a person can hold a false belief and cannot tell.

### 1.5 Attributes: one registered owner, carried by nobody

The attribute roster is owned by `references/descriptor_registry.yaml`: nine named attributes on a 1–7
scale, three each of body (Strength, Endurance, Agility), mind (Focus, Acuity, Will) and social
(Attunement, Charisma, Bonds), with aliases that map legacy names (Cognition → Acuity, Spirit → Will,
Perception → Attunement). Jordan ruled the count at ten; the tenth is unnamed (ED-IN-0193), and naming
it is an open item on the plan's roster (§5.1 item 10, D2). The same file ratifies **Thread
Sensitivity** (0–100+) and **Thread Pool Score** (TS ÷ 10) as practitioner stats (ED-IN-0029).

**No carrier holds any of them.** What exists instead, per subsystem:

| where | what it reads | relation to the registry |
|---|---|---|
| personal combat | `Combatant` strength, agi, end, cog, att, spirit, focus, history, disp | legacy names via the aliases; no Charisma or Bonds |
| mass battle | `Officer` and the general's `Unit`: charisma, cognition → `command` | mass-battle-only dataclasses |
| threadwork | Coherence as `CoherenceState` in `world.practitioners` (the mc_v18-era World) or a module fallback; Thread Sensitivity read duck-typed as `.ts` | the season loop's write matrix declares and gates `(Person, coherence)`, and `Person` has no such field; TS is set only by test stubs |
| social contest kernel | Standing and Face 0–10, Room, Reserve | a kernel retiring at `2-ii` |
| the season loop | `standing_of(p)` | a **perception gap** — how far what others have told p about p departs from what p witnessed firsthand — not a rank |

The August proposal already did this census from the resolvers and reached the conclusion this
document adopts: *"attributes govern, faculties resolve, state modulates"* — combat's law — and *"an
attribute dependency is what a subsystem has instead of an acquisition layer."* Its recommended
eight-attribute roster was overtaken by Jordan's ruling of ten (ED-IN-0193; the proposal's own §20.1
records it, and withdraws its prediction that the roster would shrink). Naming the tenth (the plan's
D2) remains his.

### 1.6 Derived, never stored

Several things a player would call stats are computed and should stay so: the combat faculties
(reading, reflex, tempo, balance, durability, steadiness), `command`, standing as a perception gap, and
rank — which the September chain describes as *the ordinal of a seat's domain, stored nowhere*.

---

## 2. One sheet

Each line is marked **LIVE** (exists and is correct), **LICENSED** (an owner already declares it; no
carrier holds it), **NEW**, or **OPEN** (a decision).

| section | field | status | owner, or where it comes from |
|---|---|---|---|
| identity | id, name, weight | LIVE | `Person` |
| body | body | LIVE | `Person`; the one scale shared with sites |
| attributes | a dict keyed by registry keys (`attr.body.strength` …), unseeded | LICENSED | `descriptor_registry.yaml`; ten by ruling, the tenth unnamed (D2) |
| practitioner | `thread_sensitivity`, `coherence` | LICENSED | TS ratified (ED-IN-0029); `(Person, coherence)` declared in `write_matrix.yaml` |
| self | pursuits, scar | LIVE, no active writer | 13 convictions → 4 axes, ruled to become 7 (ED-IN-0261) |
| memory | ledger of claims | LIVE, complete | WITNESS |
| position | tenures | LIVE | eight kinds, open roster |
| attitudes | stance, each row carrying its cause | LIVE + NEW (the cause) | [02](02_against_precedent.md) P-1 |
| practice | capability — the practice half of each domain's faculty | LIVE, needs a writer | a `practice` verb |
| martial kit | techniques and invested levels | NEW | as capability keys (§3 K-4) |
| loadout | weapon and armour | OPEN | §3 K-5 |
| derived | faculties, command, standing, rank | derived | never stored |

---

## 3. Recommendations

| # | recommendation | where | observable (falsifier) | cost | gate |
|---|---|---|---|---|---|
| **K-1** | Build the `Combatant` from the person at the seam: every field read from the sheet or derived from it; keep `end`'s derivation from body. | `seam/wrappers/combat.py::derive_party` | two persons of different builds produce different fight distributions over N seeds; identical builds reproduce today's results | small once K-2 exists | IN + PC |
| **K-2** | Add `attributes` to `Person` as a dict keyed by registry keys and **seeded with nothing** — the reasoning `scar` already records for a roster in flux. Consumers resolve names through the registry's aliases. | `state/carriers.py`, a `write_matrix.yaml` row | renaming a registry attribute moves no carrier code | small | IN; does not pre-empt D2 |
| **K-3** | Put the two licensed practitioner fields on `Person` — `coherence` (the write matrix already gates it) and `thread_sensitivity` (ratified) — and type `thread_read`'s precondition on TS so it can be attempted. | `state/carriers.py`, `verb_table.yaml` | `thread_read` executes on the populated realm; threadwork's Coherence reads and writes the person, not a module store | small | IN + WR |
| **K-4** | Make `capability` the practice half of each domain's faculty and give it its writer: one `practice` verb that raises a capability key — including a technique key such as `technique:indes` — so generic skill and martial technique share one writer and one reader. | `verb_table.yaml`, an effect | a person who practises a technique for a season holds a higher level, the seam reads it, and `choose` can see it ([10](10_verbs_and_attributes.md) §2.3) | medium | IN + PC |
| **K-5** | Loadout as `hold` tenures on equipment objects rather than a new field: ownership is already what `hold` means, so giving, taking, inheriting and losing a weapon work through verbs that exist. It needs an equipment object kind the loop does not have. Tradition access derived from the techniques a person holds, not stored — `traditions.py` already says preference emerges from the build. | `state/carriers.py`, `rosters.yaml` | a weapon given with `give` changes the recipient's next fight | medium | IN + PC; answerable by the architecture, not a ruling |
| **K-6** | Command from the person: an `Officer`'s charisma and cognition read from the commander's attributes ([08](08_mass_battle_units.md) U-4). `derive_command` stays the owner of the composite. | `hierarchy/units.py`, seam | changing a seated commander's attribute moves `command` | small | after K-2 |
| **K-7** | Store no rank. Derive it from the seats a person holds, and keep `standing_of` for what it measures — the gap between reputation and experience. | `queries/` | no carrier field named `standing` or `rank` | — | standing rule |

**For Jordan:** nothing new. Naming the tenth attribute (the plan's D2) is already his; the count is
ruled at ten. K-2 is built so that naming it, or renaming any other, costs no migration.
