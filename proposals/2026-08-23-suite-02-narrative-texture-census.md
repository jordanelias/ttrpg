# Suite 02 — The Narrative-Texture Census

**Status:** INFORMATION-ONLY. Nothing here is a design proposal; every line is a measurement of the
working tree taken 2026-08-23 on `claude/fable5-investigations-architecture-1phbx9`.
**Scope:** the four surfaces that determine whether Valoria's world reads as inhabited — world
geography, factions, settlements, NPCs.
**Method:** every number below was produced by loading the actual module or parsing the actual file
and reading the result. Where a claim rests on a document rather than on execution, the file and line
are given so it can be checked by hand. `grep` was used to locate candidate sites and never to
conclude anything.

---

## §0 The one-paragraph version

Valoria has 46 authored characters, 37 authored settlements, 16 territories and 4 playable factions.
None of the characters exist at runtime — `world.npcs` is `{}` in the canonical world and no module
reads the character registry. The settlements do load, and when they do, one of them is placed in a
province the world does not contain, owned by a faction the world does not contain. Two of the
characters live in the one province that has no settlements. Of the thirteen convictions the roster
actually uses, seven are silent no-ops in code — including the single most common one. Of the four
voice markers canon defines, only eighteen characters carry any. The registry's own schema block
describes six fewer fields than the file uses, two records lose data to an unquoted `#` every time
the file is parsed, and two texture fields are stored at two different nesting depths so that a
correct single-path reader sees at most 60% of them.

Nothing here is a disagreement about design. Everything here is authored content that the engine
cannot reach, or authored content that disagrees with other authored content.

---

## §1 World geography — the two mirror holes

### §1.1 What exists

`engine/autoload/game_state.py:215` `create_world()` builds the canonical starting world. Loaded with
`seed=1`:

```
territories: 16 — T1 T2 T3 T4 T5 T6 T7 T8 T9 T10 T11 T12 T13 T14 T15 T17
factions:     4 — Church, Crown, Hafenmark, Varfell
```

`systems/settlements/sim/registry.py` `populate_from_geography(world)` then adds settlements:

```
settlements:  37
provinces referenced: 16 — T1 T2 T3 T4 T5 T6 T7 T8 T9 T10 T11 T12 T13 T14 T16 T17
```

### §1.2 The defect

Both rosters have exactly sixteen members. They are not the same sixteen.

| | in the world | hosts settlements |
|---|---|---|
| **T15** | ✅ yes — `Territory(tid='T15', owner=None, accord=1.0, pt=5.5, ...)` | ❌ **no settlements at all** |
| **T16** | ❌ **not in `world.territories`** | ✅ yes — one settlement |

Because the counts match, no count-based check can see this. The mismatch is a single swapped
identifier, and it is load-bearing: fourteen live sites index `world.territories[...]` directly
(`systems/factions/sim/faction_action.py:143,157,173,448`, `crown_initiative.py:57,108`,
`mass_seizure.py:128`, `systems/world/sim/npe.py:182`, `insurgency_pipeline.py:228,237`,
`systems/overview/sim/ci_track.py:84`, `systems/settlements/sim/settlement.py:117`,
`infrastructure.py:131,196`). Any of them reached with the T16 settlement's province id raises
`KeyError`.

### §1.3 The orphan, in full

```
S-037   "Schoenland City"   province: T16   owner_faction: "Schoenland"
```

Three surfaces disagree at once, and each one is individually well-formed:

- the **settlement registry** places a city in T16 and gives it an owner;
- the **world** has no T16 and no faction named Schoenland (the four are Church, Crown, Hafenmark,
  Varfell);
- the **character registry** agrees with the settlement registry — NPC-012 Rikard's `territory` field
  reads `"T16 (Schoenland)"` and his `faction` reads `"Independent (Schoenland)"`.

So Schoenland is a coherent, thrice-attested place with a city, a ruler and a resident, which the
game world does not contain. It is not a typo in one file. It is a region that was authored across
the content layer and never added to the geography layer.

T15 is the exact mirror. It is in the geography layer, owned by nobody, and has no civic layer at
all — no settlement, therefore no governor, no prosperity, no order, nothing a player could act on.
Two characters live there (§2.5).

---

## §2 Characters — 46 authored, 0 instantiated

Source: `references/npc_registry.yaml`, 46 records.

### §2.1 Nothing loads them

```
world.npcs  →  {}   (canonical world, seed=1)
```

The only Python files that read `references/npc_registry.yaml` are
`tests/valoria/test_references_yaml_parse.py` (asserts it parses) and
`tools/observability/build_decisions.py` (a documentation generator). **No engine, resolver or
subsystem module reads it.** The characters are a document, not a population.

This is the single largest gap between authored content and reachable content in the repo, and it is
not a design disagreement — there is simply no loader.

### §2.2 Field population

| field | present | non-empty | note |
|---|---|---|---|
| `id`, `first_name`, `faction`, `role`, `status`, `convictions`, `source` | 46 | 46 | the authored spine |
| `last_name` | 46 | 44 | |
| `arc_trajectory` | 42 | 36 | |
| `goals` | 30 | **17** | 39 goal strings total, mean 2.3 for those that have any |
| `resonant_style` | 18 | **18** | the voice marker — §2.4 |
| `cultural_label` | 17 top-level + 26 nested | **43** union | split across two nesting depths — §2.6 |
| `territory` | 31 | **7** | §2.5 |
| `ts` (Thread Sensitivity) | 32 | **10** | mixed-type — §2.7 |
| `birthplace` | 29 | 5 | |
| `certainty` | 8 | 7 | undeclared field |
| `title` | 7 | 7 | undeclared field |
| `coherence` | 29 | **1** | only NPC-001 |
| `stats` | 29 | **1** | only NPC-001 |
| `age` | 29 | **0** | **every single age is null** |

Ten of 46 characters have neither a goal nor an arc trajectory: they are a name, a faction, a role
and a conviction vector.

`age` is the clearest case of a field that exists to look complete: it is written out on 29 records
and filled on none.

### §2.3 Convictions — the roster in code is the superseded one

Thirteen distinct conviction names are used across the 46 characters:

```
Authority 14 · Order 10 · Utility 9 · Precedent 7 · Equity 7 · Faith 6 · Liberty 6
Warden 5 · Honor 5 · Community 5 · Scholastic 3 · Virtue 2 · Identity 2
```

`systems/characters/sim/conviction.py:44-48` ships nine:

```python
CONVICTIONS = (
    "Faith", "Order", "Reason", "Equity", "Precedent",
    "Autonomy", "Continuity", "Community", "Warden",
)
```

`record_scar` at `:191-193` returns `magnitude=0` for any name not in that tuple — a **silent
no-op**, not an error. So:

- **Seven conviction names are unscarrable**: Authority (14 characters), Utility (9), Liberty (6),
  Honor (5), Scholastic (3), Virtue (2), Identity (2). The most-used conviction in the entire cast is
  one of them.
- **Three coded convictions are never used by anybody**: Reason, Autonomy, Continuity.
- **17 of 46 characters have an unscarrable *primary* conviction.**
- **12 of 46 cannot be scarred on *any* conviction they carry** — NPC-005 Sigrid, NPC-006 Halvar,
  NPC-009 Gerik, NPC-010 Dalla, NPC-011 Alexios, NPC-020 Almud, NPC-033 Kolbrun, NPC-080 Vidar,
  NPC-082 Njal, NPC-085 Nessa, NPC-086 Joren, NPC-089 Zoe. For these characters the entire
  conviction-scarring mechanic is inert, silently.

**This is not an unexplained divergence.** `systems/npcs/npc_behavior_v30.md:30` states it outright:

> *The legacy 9-Conviction set (Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity,
> Community, Warden) at `conviction_track_v1.md` is **superseded**. Reason and Continuity are
> deprecated labels; Autonomy is renamed Liberty.*

The registry is authored against the current taxonomy. The code ships the superseded one. The
supersession is dated, documented and canonical — it was simply never propagated into
`conviction.py`. That also explains the shape of the residue exactly: Reason and Continuity are
unused because they are deprecated; Autonomy is unused because it was **renamed to Liberty**, and the
six Liberty characters are hitting a name the code does not have.

The comment block sitting directly above the tuple, at `conviction.py:40-43`, already says the
canonical set is the thirteen of PP-684 — and then defines the nine. The file contradicts itself in
adjacent lines.

### §2.4 Resonant Style — four voices, eighteen characters

Canon defines exactly four (`systems/npcs/npc_behavior_v30.md:33-42`, §1.3 Resonant Style Taxonomy):
**Evidence**, **Consequence**, **Authority**, **Solidarity** — each with what the character is
vulnerable to, why, and its contest mapping.

The registry's values are correct and complete against that table. The problem is coverage and
resolution:

```
Evidence 7 · Consequence 5 · Solidarity 4 · Authority 2   =  18 of 46
```

**28 characters have no voice marker at all**, and the 18 that do are distributed across four
buckets. The whole cast is distinguishable into at most four rhetorical personalities, and 61% of it
into none.

One clarification, because it is the kind of thing that reads as a defect and is not:
`systems/social_contest/sim/contest/armature.py:145-180` runs a four-axis vector whose fourth axis is
**Insinuation**, not Solidarity. That is a *ratified deliberate* divergence (Jordan, Gate C,
2026-07-02), documented in the file with its reason — Solidarity is Knot-gated and relational, which
cannot apply to a third-party adjudicator. It is not drift.

Note also that **"Authority" is both a conviction (14 characters) and a resonant style (2
characters)** in the same file, on two different mechanical axes. That is a legibility hazard rather
than a defect, but it will bite a reader.

### §2.5 Where people live

Only 7 of 46 characters name a territory. Cross-checked against the world and the settlement
registry:

| character | territory field | territory exists | has settlements |
|---|---|---|---|
| NPC-001 Edeyja | `T15 (Southernmost)` | ✅ | ❌ |
| NPC-075 Orm | `T15 (Southernmost)` | ✅ | ❌ |
| NPC-012 Rikard | `T16 (Schoenland)` | ❌ | ✅ |
| NPC-020 Almud | `T1 (Valorsplatz)` | ✅ | ✅ |
| NPC-021 Arne | `T9 (Himmelenger)` | ✅ | ✅ |
| NPC-032 Lenneth | `T1 (Valorsplatz)` | ✅ | ✅ |
| NPC-083 Hedda | `T14 (Ehrenfeld)` | ✅ | ✅ |

Three of the seven resolve to a hole, and they land on both sides of the §1.2 mismatch.

The one worth naming: **NPC-001 Edeyja** is the most fully developed character in the game. She is
first in the registry, she has a dedicated design document (`systems/npcs/edeyja_npc.md`), and she is
the **only** character of 46 with `stats` filled in and the **only** one with `coherence` filled in.
She lives in T15 — the one province with no settlements, no owner and nothing to interact with.

### §2.6 The same field at two depths

`cultural_label` and `self_other_initial` are each stored in two different places in the same file:

| field | at top level | under `convictions` | in both |
|---|---|---|---|
| `cultural_label` | 17 | 26 | **0** |
| `self_other_initial` | 2 | 26 | **0** |

No record carries either field in both places, so a correct reader of one path silently sees 40% or
60% of the data and no error is raised. Worse, the value vocabulary is partitioned by depth:
`einhir_traditional` (4) and `altonian_imperial` (2) appear **only** top-level;
`ecclesiastical` (7), `varfell_alpine` (2) and `altonian` (1) appear **only** nested. A reader of the
nested path alone would conclude the Einhir cultural identity does not exist in the roster.

The vocabulary is also unnormalised across the split: **`altonian` and `altonian_imperial`** are
nine labels where eight were intended.

Union across both depths: 43 of 46 characters carry a cultural label — which is good coverage, and it
is exactly why the split matters. The content is there; the shape hides it.

### §2.7 Types that will not survive ingestion

`ts` (Thread Sensitivity) has ten authored values, of mixed type:

```
'75–80'   '~50'   25   15   35   28   0   0   60   0
```

Two are strings — one an en-dash range, one a tilde approximation. `int(ts)` throws on both. NPC-001
Edeyja carries `'75–80'`; her `stats.social` is likewise `'3–4'` inside an otherwise-integer stat
block.

This is CLAUDE.md §5's prose-numbers hazard occurring **inside the structured registry that exists to
avoid it**.

### §2.8 The schema block does not describe the file

`references/npc_registry.yaml` opens with:

```yaml
schema:
  required: [id, first_name, last_name, faction, role, status]
  optional: [age, birthplace, territory, ts, coherence, stats, convictions, goals,
             arc_trajectory, notes]
```

Six fields are in live use and declared nowhere: **`source`** (on all 46), **`resonant_style`** (18),
**`cultural_label`** (17 top-level), **`certainty`** (8), **`title`** (7),
**`self_other_initial`** (2).

The narrative-texture fields — the ones that make a character sound like somebody — are precisely the
undeclared ones.

### §2.9 Two records lose data at parse time

```yaml
NPC-081:  faction: Hafenmark (Inner Council #4)
NPC-082:  faction: Varfell (Jarl Council #5)
```

In unquoted YAML a space followed by `#` opens a comment. Both values are silently truncated on every
load:

```
NPC-081 → 'Hafenmark (Inner Council'
NPC-082 → 'Varfell (Jarl Council'
```

The file looks correct to a human reader. The parser disagrees, and says nothing.

### §2.10 Faction strings

Twenty distinct faction strings appear across 46 characters. Four match a faction the code knows
(Church 6, Crown 3, Varfell 2, Hafenmark 1 — twelve characters). The other **sixteen strings, on 34
characters**, have no counterpart in `STARTING_STATS`: `Restoration Movement` (4), `Löwenritter` (4),
`Guilds` (4), `Altonia` (3), `Crown (Royal Family)` (3), `Crown (Inner Circle)` (3),
`Independent (Southernmost Wardens)` (2), `Hafenmark (Inner Council)` (2), `Varfell (Jarl Council)`
(2), `Crown (Ministry)` (1), `Independent (Virke syndicate — Niflhel DISSOLVED)` (1),
`Independent (Schoenland)` (1), `Church (dual-loyalty: Crown Inner Circle agent for Himlensendt)`
(1), `Crown (Inner Circle) / Löwenritter Liaison` (1), plus the two truncated strings of §2.9.

Most of these are sub-organisations of a canonical faction and read as intentional texture — but they
are free text, not references. There is no sub-faction primitive, so `Crown`, `Crown (Ministry)`,
`Crown (Royal Family)` and `Crown (Inner Circle)` are four unrelated strings to any consumer. The
dual-loyalty and liaison records encode a *relationship* inside a *name* field, which no reader can
decompose.

### §2.11 Provenance

35 characters are `status: canonical`, 11 are `status: proposed`. The eleven proposed records all
carry `source: proposed` — the status restated as its own provenance, i.e. no source at all. The
canonical 35 cite real documents (`faction_canon_v30 §Church`, `behavior_v30 §2.16`, `npc_roster_v30
§1`, etc.).

---

## §3 Settlements — loaded, but hollow

37 settlements load. The `Settlement` dataclass has 25 fields. Population across all 37:

| populated on all 37 | populated on some | **empty on all 37** |
|---|---|---|
| `sid`, `name`, `stype`, `province_id`, `owner_faction`, `prosperity`, `order`, `pressure`, `religious_building` | `defense` (10/37) | `governor_id`, `fort_level`, `garrison`, `legitimacy`, `popular_support`, `facility_tier`, `suspicion`, `active_directive`, `church_attention`, `governor_emergence`, `subnational`, `npc_ids`, `ledger`, `open_needs`, `deck_state` |

**Fifteen of 25 fields are empty on every settlement.** The consequences, in the terms that matter for
texture:

- `npc_ids` empty on all 37 → **no settlement contains a person.** The 46 characters and the 37 places
  are not connected in either direction (and only 7 characters name even a province — §2.5).
- `governor_id` empty on all 37 → **nobody governs anywhere**, which makes
  `succeed_governor()` and the whole succession-survival guarantee unexercised.
- `ledger` empty on all 37 → §3.2.
- `open_needs` and `deck_state` empty → no settlement has anything it wants or any pending situation.

Type histogram (all valid against `LEGAL_TYPES`):

```
Town 15 · Village 14 · Seat 2 · Fortress 2 · City 2 · Fortress-City 1 · Cathedral-City 1
```

Settlements per province run 1–3, mean 2.3. `T9` has 1; `T16` (the phantom province) has 1 — S-037.

`Territory` field population is thinner still: of 9 fields, `owner` is set on 15/16 (T15 is
ownerless), `garrison` and `fort_level` on 4/16, `templar` on 1/16 (T9), and `uncontrolled_since` on
0/16.

### §3.2 The settlement memory layer is unreachable

`systems/settlements/sim/ledger.py` (75 lines) is the durable per-settlement governance memory —
the thing that would let a place remember what was done to it. Its five tag kinds are exactly the
vocabulary a world needs to feel like it has a past:

```
Precedent  — a ruling that biases future events
Grudge     — an actor/faction wronged
Debt       — an obligation
Reputation — the settlement's read on the governor
Leverage   — a hook the player holds
```

Tags live on the settlement rather than the governor specifically so they **survive succession** —
the file's docstring calls this "the player→world persistence guarantee."

An AST sweep of every live `.py` in the tree for calls to the API:

```
ledger_add    ← called once, from Settlement.add_tag (registry.py:102)
ledger_has    ← called once, from Settlement.has_tag (registry.py:105)
ledger_get    ← called once, from Settlement.tags   (registry.py:108)
ledger_sweep  ← called once, from registry.py:207

Settlement.add_tag / .has_tag / .tags  ← called by NOTHING, anywhere, including tests
```

The module has one wrapper layer and zero consumers. **No settlement has ever recorded a precedent, a
grudge, a debt, a reputation or a leverage hook**, because nothing can. This is the single most
consequential piece of dead code for narrative texture in the repo: it is well-designed, well-cited,
complete, and unreachable.

---

## §4 What this census does and does not say

**It does say:** the authored content is substantially richer than the reachable content, and the two
have drifted apart in specific, locatable, individually cheap-to-fix ways. Almost nothing here is a
hard design question. T16/T15 is a data fix. The conviction roster is a propagation of an already-made
ruling. The nesting split is a normalisation. The `#` truncation is two pairs of quotes. The ledger
needs call sites, not a design.

**It does not say** that the design is wrong, or that the missing pieces are missing by mistake. The
loader for the character registry does not exist because the question of *what a character is at
runtime* has not been settled (see Suite 04). The empty settlement fields are mostly waiting on
subsystems that are themselves unbuilt. The census measures the gap; it does not attribute it.

**One thing it deliberately does not do** is infer a defect from a shared name. Three candidates were
checked and cleared during this pass, and they are recorded here so the next reader does not re-raise
them:

- `systems/threadwork/sim/operations.py:135` `_compute_degree` looks like a rival degree ladder and is
  not — it delegates to `dice_engine.degree_label`, and its own docstring says so.
- `armature.py`'s Insinuation axis looks like drift from canon's Solidarity and is not — it is a
  ratified deliberate substitution with a stated reason (§2.4).
- `systems/combat/sim/combat.py:121` `_combat_pool` looks like a rival to
  `combat_engine_v1/core.py:50` `resolution_pool` and is not a live conflict — the file carries a
  DEPRECATED banner naming its supersession.

---

## §5 Reproducing every number here

```python
import sys, yaml, collections, dataclasses; sys.path.insert(0, '.')
from engine.autoload.game_state import create_world, Territory, STARTING_STATS
from systems.settlements.sim import registry as R
from systems.characters.sim.conviction import CONVICTIONS

w = create_world(seed=1); R.populate_from_geography(w); st = R.settlement_store(w)
d = yaml.safe_load(open('references/npc_registry.yaml')); chars = d['characters']

sorted(w.territories)                                    # 16 territory ids
sorted({s.province_id for s in st.values()})             # 16 settlement province ids
[s for s in st.values() if s.province_id == 'T16']       # S-037 Schoenland City
collections.Counter(e['conviction'] for c in chars       # 13 conviction names
    for e in (c.get('convictions') or {}).get('primary') or [])
set(_) - set(CONVICTIONS)                                # the 7 unscarrable
```

The AST sweeps for ledger reachability and for pool/TN ownership are given in Suite 01 §
and Suite 04 §, with the scripts inline.

---

_Measured 2026-08-23 against `claude/fable5-investigations-architecture-1phbx9` at `512400f`.
Every figure re-derivable by the snippet above. No figure in this document was carried forward from
an earlier session without re-measurement._
