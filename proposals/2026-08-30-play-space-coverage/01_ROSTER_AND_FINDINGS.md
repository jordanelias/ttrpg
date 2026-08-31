# The canon roster, and four findings that precede the seasons

## Status: FILED (2026-08-30) — read-only review output. Reference for the season lanes.
## Source: `references/npc_registry.yaml` (90 ids, `canonical`/`proposed`), cross-checked against
## `references/proper_noun_registry.yaml`, `systems/factions/faction_canon_v30.md`,
## `faction_politics_v30.md`, `canon/03_canonical_timeline.md`, and the Goldenfurt slice cast.

---

## FINDING 1 — THE MERGED SUITE BORROWED CANON NAMES AND GAVE THEM INCOMPATIBLE LIVES

This is the finding with the most immediate consequence, because it binds every season lane.

| name | canon says | the merged suite used them as |
|---|---|---|
| **Maret Uln** | Varfell intelligence operative, TS ~50, Southern Einhir of the western fjords, **and Duke Vaynard's succession fallback if he is eliminated** (PP-486) | a Southern Einhir journeyman kettlemaker sitting the Masterpiece Examination in Goldenfurt |
| **Gerik Strand** | **Lord Steward of the Crown Inner Circle**, flagged an "OVERPERFORMER", flattery-vulnerable | a Southern Einhir journeyman smith, covertly Niflhel, in a hamlet outside Goldenfurt |

These are not variant readings. They are different people wearing one name, and the suite's versions
are the ones its worked traces are built on.

**The suite is not wrong as design** — the *mechanisms* those traces demonstrate hold regardless of
who is standing in them. What is wrong is the naming, and it matters here because a season written
for "Maret Uln" must be a season for **the Varfell operative who is a duke's heir-in-waiting**, which
probes an entirely different cell than a guild candidate does.

**Binding on every lane: canon's person is the person. Where a lane needs a commoner, invent an
unmistakably new name rather than borrowing one.**

---

## FINDING 2 — THE KING OF VALORIA HAS NO STATED WANTS

`goals: null` in the registry, for Almud Almqvist. Also null for Elske, Torben, Himlensendt, Aldric
Hann, and most of the Crown Inner Circle (Voss, Reichard, Kreutz explicitly).

**Under this design that is not a blocker — it is the sharpest available test.** Needs are *computed*
from a person's situation, never authored, so the design's own claim is that it can produce a want
for a king whose canon says nothing. **A lane that cannot derive Almud's needs from his larder, his
standing among peers, his unmet stance-commitments and his exposure to terms has found a real hole**,
and must report it rather than inventing a goal for him.

---

## FINDING 3 — FIVE LIVE CANON CONTRADICTIONS. DO NOT RESOLVE ANY OF THEM.

| # | contradiction | the two sides |
|---|---|---|
| 1 | **The Löwenritter Grandmaster's name** | `npc_registry.yaml:721` says **Lisbeth Ehrenwall**; `canon/03_canonical_timeline.md:145` says **"Sigrid Ehrenwall"** — apparently conflating the first name of *Sigrid Torsvald* (a different character, the TS Riskbreaker) with Ehrenwall's surname. The proper-noun registry lists both as aliases |
| 2 | **Who is Cardinal of Justice** | registry says **Arnlod Olafsson**, and explicitly overrides; `faction_canon_v30.md:570` says **Sæmund Haelgrund**, whom the registry calls "Field Inquisitor, NOT a Cardinal" |
| 3 | ~~Whether Niflhel exists~~ **CLOSED — RULED BY JORDAN 2026-08-30** | **Niflhel is NOT a faction; struck months ago.** The strike is authoritative. The present-tense four-arm rank ladder in `faction_politics_v30.md` §2.6 and the live faction row in the timeline are **stale text never cleaned up**. Not a contradiction; a cleanup debt |
| 4 | **Almud's Thread Sensitivity** | registry **TS 28**; timeline **TS 0** |
| 5 | **Reichard** | a possible person-collision between the Lord Treasurer and an ecclesiastical "Cardinal Reichard", open in the registry's own issue log |

Each is a season-relevant fact. **Where a season depends on one, write both branches or write the
season around the ambiguity, and say which you did.**

---

## FINDING 4 — TWO OF FOUR CARDINAL SEATS ARE NOT ACTUALLY FILLED, AND THE GUILDS HAVE NO LEADER BY DESIGN

**Klapp and Jarnstal are "candidates"** in both sources and are never stated as seated. So of the four
Dicasteries the design leans on, canon confirms **one** occupant outright (Tormann, Prudence), one in
dispute (Justice), and two vacant-or-candidate.

**The Guilds are not one faction at all. RULED BY JORDAN 2026-08-30: they are "just a loose
collective of economic factions."** The registry's "Guildmaster Council, no single leader, a design
feature not a bug" now reads correctly: there is no single leader **because there is no single
proposition**. The theoretical Standing-6 Grand Guildmaster stays existence-unconfirmed.

**This is a vindication of the design's faction model, not a gap in it.** A faction is a proposition
plus a commitment map; several overlapping economic factions along one street — a guild's masters, a
grain factor's creditors, a ford-toll syndicate — are exactly what that model predicts, and none of
them needs a charter, a head, or a registry row in order to exist and act.

**Both remain probes, one of them reframed by Jordan's ruling:**
- a **vacancy** at a Dicastery is a live standing date with claimants, which is exactly what the
  design says an office vacancy is. **Unchanged.**
- the **economic collective** now tests something sharper than a headless faction would have: whether
  *several small overlapping factions with no institution at all* can be expressed and can act, purely
  through the persons who hold them. If they can, it is the strongest available vindication of the
  claim that a faction is a proposition plus a commitment map with no verbs of its own.

---

## The roster, as assigned

Depth is proportional to what canon gives. **FULL** = the nine-part season shape in `00_PLAN.md §4`.
**PROBE** = coordinates, option set, diagnostic, and nothing else.

| lane | characters | depth |
|---|---|---|
| **1 · Crown** | Almud, Lenneth, Elske, Torben **FULL** · Voss, Reichard, Thale, Linder, Kreutz, Almstedt, Strand (Lord Steward) **PROBE** | mixed |
| **2 · Church** | Himlensendt, Tormann **FULL** · Olafsson, Klapp, Jarnstal, Haelgrund **PROBE** + the two unfilled seats as a vacancy probe | mixed |
| **3 · The duchies** | Baralta, Vaynard **FULL** · Heljason, Geirson, Falkenrath, Uln *(canon's operative)*, Holdar, Stenskald, Torberg **PROBE** | mixed |
| **4 · Sword and shadow** | Ehrenwall, Torsvald **FULL** · Brandt, Haldorsen, Virke, Thale, Vorn **PROBE** + Niflhel's existence contradiction as a probe | mixed |
| **5 · Power without office** | Vossen **FULL** · Hann, Askeland, Vedel, Saatfeld **PROBE** · Feldhaus, Kessler, Grindvold, Bergvall, Tallow **PROBE** + the headless-Guilds probe | mixed |
| **6 · Edges and ground** | Laskaris **FULL** · Palaiologina, Doukas, Solberg **PROBE** · Edeyja, Orm **PROBE** · Vorn, Wessel, Ems, Mertha, Brun, Aldith **PROBE** · one invented unremarkable fisher **FULL**, as the control | mixed |

**The control matters.** One wholly unremarkable person — no office, no alignment, no notable marks,
no Knot — written at full depth. Every other season is measured against it. If the baseline is
SPECTATOR, the design has a floor problem that no amount of richness at the top repairs.
