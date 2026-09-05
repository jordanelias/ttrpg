# READINGS · 08 — DICTIONARIES, DEFINITIONS, REGISTERS · KEYS AND BUSES

## Status: **RATIFIED 2026-09-05 (ED-IN-0202) — Jordan ruled "adopt in full". This is LAYER 1: the code architecture and shape, which GOVERNS HOW ALL CODING IS CONDUCTED. Under CLAUDE.md §0.05 it is reference for GAME MECHANISM — the code is the formula — and binding as AGENT INSTRUCTION, the same standing as CLAUDE.md itself. The game code it governs is `engine/season/`.**
## A **reading** of Stages 1–4. ⚠ **If this and a stage disagree, the stage is right.**
## Answers: *"How do dictionaries, definitions and registers work? How do keys and buses work?"*

---

# §1 · Four shapes, and one test sorts them

> **Would changing this change the GAME, or change how the CODE works?** A roster changes the game. A
> step→write-class map changes the code and does not belong here.

| | shape | accessor | example |
|---|---|---|---|
| **Roster** | a closed **SET** | returns a frozenset | `tenure_kinds` · `rung_kinds` (ordered) · `remit_acts` · `strata` · `conviction_axes` · `question_sources` |
| **Table** | a **MAPPING** keyed on a roster | returns a dict | `wear_per_season` · `band_floors` · `alignment` · `site_yield` |
| **Fixture** | a free-standing **scalar** | injected by name at a named site | the condition scale · the ledger cap · `view_k` · the budget base |
| **Register** | the **holes**, as rows | `id · hole · kind · owner · grade · default · site · sweep · unblocks · cite` | — |

**Reading a roster with the table accessor RAISES**, so the two shapes cannot be confused at the call
site.

**The number rule that separates a table cell from a fixture:** a number that is a **property of a
roster member** travels with the roster; a number that **stands free of any roster** is a fixture.
`alignment[axis][verb]` has no meaning apart from the axes — it lives with the definition. `view_k`
means something on its own.

---

# §2 · Definitions are data, and absence is a refusal

**A definition — a roster, a taxonomy, an axis set, any closed set — is read at runtime.** Changing
one is a data edit. **A definition written as a literal in a body is a defect whatever else is true
of it.**

> **THE POLARITY RULE GOVERNS EVERY LOOKUP.** An absent roster **RAISES** rather than returning empty;
> a missing key raises rather than defaulting. ⚰ *A wear table that answers `20` for an unregistered
> kind does not fail — **it answers, plausibly and wrongly, forever.***

**A `default_cell` may only cover an unlisted PAIR of registered keys** — never a missing key, never a
missing table.

⚠ **And the strongest argument for keeping closed sets in data rather than in a sentence:**
`question_sources` was declared closed at three and turned out to be missing a fourth. **Without it an
NPC with a standing ambition and a quiet season forms no candidates at all** — a person with a goal
and an empty inbox would simply not act.

---

# §3 · The register, and what each grade licenses

| grade | behaviour |
|---|---|
| `ruled` · `measured` | build on it; the citation or command is on the row |
| `assumption` | **inject the default · declare the site · sweep three points.** ⚠ **A verdict that flips across the sweep is itself a finding, and a more important one than the verdict** |
| `absent` | **REFUSE. No default.** An instrument that fills it has invented |

**A row with no grade FAILS THE EXPORT** — zero evidence maps to the verdict *against*, never to a
silent `assumption`.

**And the register is what turns an instrument's loop into a list with a bottom:** an instrument may
fill **exactly** what the register declares and nothing else, **which makes the antagonist's question
a grep rather than a judgement.**

---

# §4 · Keys — yes, and the roster is DERIVED

An **`Event`** is the key-like record: `id · kind · changes[] · causes[] · emitted_at · degree?`.
Kinds are `family.type`, lowercase dotted.

> ### **THE REGISTERED KIND ROSTER IS DERIVED, NOT AUTHORED** — computed as the union of every
> emission column in the write matrix and the verb table. The log refuses any kind not in it.
> **The consequence is structural: a subsystem cannot invent a kind, because it has no data file in
> which to add one.**

Union-typed references are `(kind_tag, id)`. ⚠ **A storage discriminator is NOT a resolver branch** —
say so beside it, or the first reviewer deletes the tag and the second re-adds it as a class
hierarchy.

---

# §5 · Buses — **no. And the refusal is load-bearing.**

**There is no bus, no signal, no subscription table.**

> **A bus routes a message to a recipient. To route, something must know who it is for — and that is
> a `target` on the Event, which is forbidden. An Event that knows who it is for is an Event that
> CANNOT BE MISATTRIBUTED, and misattribution is a feature.**

**What replaces it:**

> **WITNESS is one global pass. For each Event it COMPUTES the observer set** from the presence index
> and five declared channels — co-located · document · witness-key · post-remit · chronicle — **then
> deposits a Claim into each observer's own ledger. Nobody subscribes. The emitter declares no
> recipient.**

**Two properties fall out of computing rather than subscribing:**

- **Covert action needs no flag.** An act nobody was present for produces no first-hand attribution
  anywhere — not because it was marked hidden, but because **the observer set was empty**.
- **Attribution is per-witness and can be wrong.** What each channel *mints* differs: a co-located
  witness saw who acted; a document holder saw only that the document changed.

⚠ **And the fan-out must not be sharded.** The predecessor loop was retired precisely because its
WITNESS was not global — **which made its parallelism claim unsound rather than merely unproven.**

**The one thing that does route by name is a MODULE, not a message:** the engine names a **role**, a
manifest row names the **provider**, resolution happens by string at boot. **A missing row is a
startup failure naming the row — never a silent fallback.**
