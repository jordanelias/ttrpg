# Character Histories Audit — Valoria v30

**Date:** 2026-05-07
**Auditor:** Claude (Opus 4.7)
**Subject:** `designs/world/character_histories_v30.md` (audit performed against `_infill.md`)
**References used:**
- `canon/03_canonical_timeline.md`
- `designs/world/southernmost_v30_infill.md`
- `designs/world/worldbuilding_v30_infill.md`
- `designs/world/geography_v30_infill.md`
- `designs/territory/territory_temperaments_v30.md`
- `skills/prose-writer/SKILL.md`

**Status:** Initial audit, one self-review pass applied.
**Self-authored — bias risk.** This audit has been reviewed once and corrected for mechanical-invention overreach and canonical-material overreach in proposed prose addenda. Limitations are noted at the end.

---

## Summary table

| Flag | Severity | Status |
|---|---|---|
| GEO-1 — Halvarshelm/Halvardshelm | — | **Closed.** Both spellings canonical (T17 Hafenmark, T11 Varfell). No fix needed. |
| GEO-2 — Lowenskyst | — | **Closed.** Confirmed T3 Crown Border Fortress. Correctly placed in 1G. |
| CASTE-1 — 1D in-game social consequences | High | **GAP.** Needs design specification. |
| STRUCT-1 — Stage 3 Vocations unwritten | High | **GAP.** Content needs Jordan. Template proposed. |
| CASTE-2 — 2F practitioner social risk | Medium | **GAP.** Needs design specification. |
| STRUCT-2 — 4B and 4E incomplete | Medium | **PROPOSED narrative + GAP mechanics.** |
| RENN-1 — Swiss/Norwegian labels | Low | **APPLY.** In-world replacements drafted. |
| RENN-2 — "Empiricist" anachronism | Low | **APPLY.** Label change to "Observer." |
| PROSE-1 — File refs in narrative sections | Low | **APPLY.** Convert to design-note callouts. |
| PROSE-2 — Tartt underweight in Knots | Low | **PROPOSED.** Tartt addenda for existing Knots only. |

**Surfaced from geography verification (additional minor):**

| | Severity | Status |
|---|---|---|
| 1C "western coast" misdescription | Low | **APPLY.** Halvardshelm (T11) is Central Fjords, Grauwald (T4) is Central Highlands — neither is western coast. |
| 1G includes Halvarshelm (T17) under fortress framing | Low | **APPLY.** Halvarshelm is Northern Mines, not fortress-dependent. Soften the framing. |

**Status legend:**
- **APPLY** — text change ready for direct application; no canon invention.
- **GAP** — design gap requiring Jordan's specification.
- **PROPOSED** — narrative content drafted for Jordan's approval; mechanical values left as `[TBD]`.
- **Closed** — no action needed; flag was a false positive after verification.

---

## Self-review note

[SELF-AUTHORED — bias risk]

Two classes of overreach were identified in the first-draft proposals and corrected here.

**1. Mechanical invention.** First-draft proposals for CASTE-1, CASTE-2, and STRUCT-2 included specific mechanical values: Social Contest Ob modifiers (+1, −1), Renown floors, "Scrutiny tokens," Certainty modifiers (−1), Thread Sensitivity bonuses (+5 permanent). These are canonical mechanical specifications and are not Claude's to set. They have been reclassified from APPLY to GAP. The audit identifies the *surfaces* that need specification (which factions react how, which scales are affected, whether Renown / Certainty / TS / Ob modifiers apply) without filling in numbers.

**2. Canonical material in prose addenda.** First-draft Tartt addenda introduced new canonical objects (a ledger in 1B), upgraded indeterminate canon to determinate (1D's elder shifted from "may be dead" to definitively dead with a specific gesture), and specified PC-specific details (age 17 in 1G, twenty years' upbringing in 1E). These have been narrowed: Tartt addenda are now proposed *only* for existing Knots in the canon, and amplify existing Knot content with atmospheric weight rather than introducing new objects, ages, or biographical specificity.

**Independent-reviewer limitation:** This audit was performed against `character_histories_v30_infill.md`. The primary file `character_histories_v30.md` was INDEX-ROUTEd by `github_ops` and not directly read. If primary content differs from the infill (e.g., Stage 3 Vocations may have content in the primary that isn't in the infill), audit gaps may exist. Verification against the primary is recommended before any edits are committed there.

---

## Detailed resolutions

### GEO-1 — Halvarshelm vs. Halvardshelm — **Closed**

Both spellings are canonical. Verified against `designs/territory/territory_temperaments_v30.md`:

- **Halvarshelm (T17)** — Hafenmark, Northern Mountains / Northern Mines. Iron/copper mining, Guild operations.
- **Halvardshelm (T11)** — Varfell, Central Fjords. Adjacent to Spartfell (T10) via the Hafenmark-Varfell border.

The character histories use both spellings correctly:
- 1B (Highland Born, Hafenmark) lists Halvarshelm — correct (T17 is Hafenmark).
- 1C (Fjord Child, Varfell) lists Halvardshelm — correct (T11 is Varfell).
- 1G (Border Settlement) lists Halvarshelm — correct location, but framing is imprecise (see surfaced minor flag below).

No fix needed for the spelling.

### GEO-2 — Lowenskyst — **Closed**

Verified canonical: T3, Crown, Northern Mountains / Border Fortress, NE Altonian-pass garrison. Correctly placed in 1G (Border Settlement Child) alongside Spartfell (T10, NW pass) and Halvarshelm (T17). All three are northern border-area territories; the framing fits.

### CASTE-1 — 1D in-game social consequences — **GAP**

The 1D origin describes 245 years of Church institutional suppression and the cultural memory it leaves. The audit confirms the description is internally consistent and historically grounded against the canonical timeline.

What is missing is the *mechanical surface*. A player choosing 1D needs to know what this origin costs in play, not just what it carries narratively. The mechanical surfaces that would benefit from specification:

- **Faction relationship starting states** — does Church faction begin at lower relationship for 1D? Does Varfell faction begin at higher? (Compare: 1A Crown Heartland Child probably starts at higher Crown relationship — is this specified anywhere?)
- **Social Contest interaction** — do 1D characters face Ob modifiers in Crown / Church territories? Do they receive Ob bonuses in Varfell territories?
- **Renown** — is there a Renown floor or ceiling tied to caste-stigmatized origin?
- **Information access** — do Church informants withhold from 1D characters? Do Einhir-sympathetic NPCs offer earlier access?

**This is a design gap, not a content gap.** The narrative is correct. The mechanical translation needs Jordan's specification.

**Proposed editorial item:** *Caste mechanical consequences — specify how Southern Einhir Descendant origin (and other caste-marked origins) translates to Faction Relationship, Social Contest Ob, Renown, and Information Access mechanics. Same-pattern decisions needed for 1A (Crown Heartland privilege), 1E (Himmelenger Church proximity), and 1F (Valorsplatz urban underclass — economic class, not ethnic caste; distinction matters).*

### CASTE-2 — 2F practitioner social risk — **GAP**

The 2F (Practitioner Mentorship) formation reads in the current text as a neutral choice equivalent to Church Schooling or Guild Apprenticeship. In 245 AG canon, it isn't. Practitioner communities are suppressed; Church surveillance applies; the character carries information that cannot be openly discussed.

The narrative addition needed (which I can draft) is straightforward: a paragraph noting that practitioner mentorship in 245 AG carries social risk, that the formation involved navigating suppression, and that the character carries knowledge they cannot articulate publicly.

The **mechanical surface**, again, needs specification:

- Does 2F start with a Church faction relationship penalty?
- Does the character begin with a Scrutiny / Watch flag in Church-influenced territories?
- Are there Social Contest Ob implications for openly discussing certain topics?
- How does this interact with 1D origin (Southern Einhir Descendant) — do they stack, or does one absorb the other?

The narrative addition can be drafted; the mechanical surface needs Jordan.

**Proposed editorial item:** *Practitioner formation social risk — specify mechanical consequences of 2F (Practitioner Mentorship) given 245 AG Church suppression. Coordinate with CASTE-1 on stacking with origin-based caste effects.*

**Proposed narrative addition (no mechanical claims):**

> **Social risk (245 AG):** Practitioner communities are not recognized institutions. They are marginal networks — scattered wardens, isolated scholars, communities in the Southernmost-adjacent territories that have maintained folk practice under suppression. Seeking this formation required navigating Church awareness. Your mentor took risks. You carry knowledge you cannot explain to a Church-educated person without triggering doctrinal challenge. You learned to speak carefully before you knew why.

### STRUCT-1 — Stage 3 Vocations unwritten — **GAP (template proposed)**

The infill contains section headers for Crown, Church, Hafenmark, Varfell, Guild, Niflhel, Restoration Movement, Löwenritter, and Cross-Factional Vocations. None have content in the infill. (Possibly content exists in the primary file that didn't extract — verification needed.)

Vocations are the most mechanically dense section: they grant 2 starting skills (1 unique), determine faction affiliation, and produce the canonical Origin/Formation/Vocation contradictions framing.

The content per vocation requires Jordan's design input on:
- Which specific vocations exist within each faction
- The 2 skills granted (and which is unique)
- The faction relationship state on character creation
- The Knot template per vocation

**Proposed template per vocation entry** (for use once content is specified):

```
### [Faction] — [Vocation Name]
**Faction affiliation:** [Faction]. Starting relationship: [TBD per CASTE-1 spec].
**★ Unique skill:** [Skill name] — [one-line description].
**Second skill:** [Skill name] — [one-line description].
**Spark list additions:** [skills available for spark during play].
**Knot:** [specific in-faction person — recruiter, master, mentor, rival].
**Certainty modifier:** [TBD].
**Narrative impact:** [one sentence on the worldview this vocation presupposes].
**Canonical tension example:** [one Origin/Formation pairing that produces character tension when combined with this vocation].
```

**Proposed editorial item:** *Stage 3 Vocations — specify content per faction. Approximate scope: 9 faction sections × 2-4 vocations each ≈ 20-30 vocation entries.*

### STRUCT-2 — 4B and 4E incomplete — **PROPOSED narrative + GAP mechanics**

Both options are header-only in the infill. Narrative drafts proposed below for Jordan's review and mechanical specification.

**4B. Betrayed by Your Institution — proposed narrative:**

> The institution that shaped your Formation turned on you — or used you as a means to its own ends, which is a quieter version of the same thing. Specify: which institution (Crown, Church, Hafenmark, Guild, or the faction your Formation aligned you with), what the betrayal was (false accusation, abandonment when convenient, using your specific knowledge against someone you protected, being made an example to discipline others), and what you lost (position, mentor, community, the version of yourself that trusted institutions).
>
> The betrayal doesn't destroy faith — it reveals that the institution's account of itself was never complete. Something was always held back from you.
>
> **Belief shape:** *"[Institution] treats [specific value] as a tool. I will use [different institution or my own judgment] to correct what they won't."*
>
> **Knot:** A member of the institution who either participated in the betrayal (and knows it was wrong) or was protected from it (and doesn't know the cost). Whether they are complicit or ignorant shapes every scene you share.
>
> **Certainty modifier:** [TBD — proposal needs Jordan]
> **Starting skill:** [TBD]

**4E. The First Leap — proposed narrative:**

> You have Leaped. The thread pulled through. Whatever you understood before about the world's substrate — whether you understood nothing or had heard the wardens' careful descriptions — was replaced by direct contact with the unintelligible ground.
>
> This is not a mystical experience in the common sense. There was no vision, no voice, no revelation. There was: a moment where the categories that structure ordinary experience became perceptible as categories. Where the thing beneath the rendering became briefly, structurally apparent. The experience has no content you can translate. It left a scar.
>
> **Knot:** Someone who was present, or who found you afterward, or who you told. Their response (belief, disbelief, fear, recognition) defines a live tension. If no one was present, the Knot is instead someone you *almost* told — and chose not to.
>
> **Belief shape:** *"What I touched is [real / terrifying / the only thing that matters / not what the Church calls it]. I will [act in accordance with this]."*
>
> **Thread Sensitivity modifier:** [TBD — Leap scar mechanics need spec]
> **Certainty modifier:** [TBD]
> **Starting skill:** [TBD]

**Proposed editorial item:** *4B and 4E mechanical specs — specify Certainty modifiers, starting skills, and (for 4E) Thread Sensitivity / Leap scar mechanics. Coordinate 4E with existing Leap mechanics in `threadwork_v30.md`.*

### RENN-1 — In-world replacements for ethnic comparison labels — **APPLY**

**1B "Swiss-character territory"** — replace with:

> Landlocked, mineral-rich, and constitutionally stubborn — a territory that built its identity out of what it wasn't: not coastal, not easily governed, not willing to accept authority on someone else's terms.

**1C "Norwegian-character fjord communities"** — replace with:

> Communities shaped by water and separation. The fjords connect what the mountains divide. No single family survives without maritime knowledge; no community survives without knowing its neighbours by the rhythm of their boats.

Both replacements describe the existing characteristics in in-world terms without inventing new canon. The "Italian-coded" framing in `territory_temperaments_v30.md` (e.g., for T2 Kronmark heartland) is a parallel internal-shorthand label that should receive the same treatment if/when it surfaces in player-facing text.

### RENN-2 — "Empiricist" → "Observer" — **APPLY**

Change the option header from:

> **2D. Self-Taught / Empiricist**

to:

> **2D. Self-Taught / Observer**

The body text describes the practice (direct observation, mistrust of institutional framing, unstable Certainty) accurately without needing the anachronistic school name. No body changes required.

### PROSE-1 — File refs to design notes — **APPLY**

In 1D, replace:

> *"(a metaphysical mechanism localised to Askeheim per calamity_radiation.md)"*

with a set-off design note:

> **[Design note:** The Forgetting is a structural mechanism distinct from cultural suppression — it erases perception of the Southernmost's danger, not memory of lived experience. Full specification in `calamity_radiation.md`. These two mechanisms are frequently conflated by players; the distinction matters for how this origin plays out.**]**

Apply the same treatment to other inline file references in narrative passages throughout the document (the cross-reference header at the top of the file is appropriate as-is; only inline parentheticals in prose passages need conversion).

### PROSE-2 — Tartt addenda for existing Knots — **PROPOSED (revised after self-review)**

**Self-review correction.** First-draft proposed Tartt addenda introduced new canonical material (specific objects, PC ages, definite shifts in indeterminate canon). Revised proposals below: addenda are limited to *existing* Knots only and amplify existing Knot content without introducing new objects, ages, or biographical specificity.

Each is one Tartt-inflected sentence: atmospheric retrospection, weight without explicit emotional naming, sensory anchor.

**1B Knot** (community elder embodying constitutional values):
> What you remember is not the lesson but the cadence in which it was delivered — a specific patience that did not soften when you misunderstood.

**1C Knot** (community member — fisher, elder, childhood rival):
> The boats they returned in carried the smell of distance — that specific particularity of having been somewhere else — and you came to recognize them by the smell before you saw the sail.

**1D Knot** (the existing line *"They may be dead — and what they gave you is the only record that they existed as carriers of something the Church tried to erase"* is already heavily Tartt-loaded. No addition recommended; the existing prose is the strongest in the document.)

**1F Tideward Knot** (sibling who works Niflhel's dockworker arm):
> Their hands had taken on the calibration of weights you had never lifted, and you learned not to look at their hands while you spoke.

**1F Ashmarket Knot** (Church charity teacher):
> Your earliest surviving memory of any text is in their voice — they read the syllables for you before you knew that the marks were syllables — and the words you most distrust now arrive in that exact cadence.

**1G Knot** (garrison soldier or border-veteran parent):
> The maps they kept were marked in two colours — the route as it was supposed to go, and the route as the patrol actually took — and you understood, much later, that the difference between those two lines was the entire reason they were still alive.

**1H Knots** (the three displacement variants are tightly written; existing prose is already at the right weight. No additions recommended.)

**Options without Knots in the original (1A, 1E):** No additions proposed. Adding atmospheric content where no Knot exists is content elaboration, not flag resolution.

Each addendum amplifies the existing Knot description with one sentence of atmospheric load. None introduces new objects, ages, or biographical specifics that aren't already implied in the existing canon.

### Surfaced minor 1: 1C "western coast" misdescription — **APPLY**

Current text: *"Born on Varfell's western coast — Sigurdshelm, Halvardshelm, Oastad, or Grauwald."*

Verified against `territory_temperaments_v30.md`:
- Sigurdshelm (T12) — Western Fjords / Varfell Seat ✓ (western coast applies)
- Halvardshelm (T11) — Central Fjords (not western coast)
- Oastad (T13) — Varfell, gate to Askeheim
- Grauwald (T4) — Central Highlands / Highland Timber (highland, not coastal)

**Replacement:** *"Born in Varfell territories — fjord, highland, or coastal."* Preserves the geographic variety without inaccurate compression.

### Surfaced minor 2: 1G framing for Halvarshelm — **APPLY**

Current text: *"Communities that exist because a fortress needs people to supply it."*

Lowenskyst (T3, Crown Border Fortress) and Spartfell (T10, Hafenmark Border Castle) fit this framing. Halvarshelm (T17, Hafenmark Northern Mines) is a mining community, not fortress-dependent.

**Replacement:** *"Communities at the northern edge — fortress garrison towns, mining settlements in the mountain passes, provisioning depots."* Covers Halvarshelm without misrepresenting its character.

---

## What's strong (anchor in what works)

The system is structurally sound. Key strengths:

1. **1D (Southern Einhir Descendant) is the most carefully written option.** The 245-year suppression count is accurate; the distinction between cultural destruction and the Forgetting is precise; the "ten generations" detail is mathematically correct; the prose ("the only record that they existed as carriers of something the Church tried to erase") is the document's strongest line.

2. **The Knot system across origins is excellent.** Each Knot creates a live narrative tension specific to the origin, anchors a factional or relational dynamic, and avoids backstory-only treatment. The Knots in 1F (Tideward sibling, Ashmarket teacher) and 1H (the three displacement variants) are particularly tight.

3. **Renaissance institutional accuracy is consistent.** Crown deed-monarchy, Church educational monopoly, guild master-apprentice hierarchy, ducal household education, contemplative monasteries, knightly orders (Löwenritter), border garrison communities, empiricism vs. institutional authority tension — all period-correct without anachronism (with the minor RENN-1/RENN-2 exceptions).

4. **The 245 AG timeline integration is exact.** Spartfell Incident, Templar Suppression, and Ducal Border Clash all land within the 238-245 window the canonical timeline establishes. 1D's "245 years of Church suppression" matches the Church-formation start point. 1H's calamity-event variant correctly references active game-world Calamity phenomena.

5. **The Forgetting / cultural suppression distinction is canonically precise.** This is genuinely subtle canon (the Forgetting is metaphysical and Askeheim-localized; cultural suppression is institutional and peninsula-wide), and 1D handles it correctly.

6. **The Origin/Formation/Vocation contradiction framing is sound.** The design note that *"a Crown Heartland Child with Practitioner Mentorship and a Church Vocation is a character whose biography is an argument with itself"* is the right principle for character creation — biographical contradictions produce live tension, not invalid characters.

The audit's flags are refinements on a solid foundation, not structural critiques.

---

## Editorial item proposals

These are proposed for the editorial ledger. ED numbers are placeholders for Jordan's assignment.

| Placeholder | Severity | Description |
|---|---|---|
| ED-NEW-A | High | **Caste mechanical consequences.** Specify how caste-marked origins (1D Southern Einhir, 1A Crown Heartland privilege, 1E Himmelenger proximity, 1F Valorsplatz underclass — distinguishing economic class from ethnic caste) translate to Faction Relationship, Social Contest Ob, Renown, and Information Access mechanics. |
| ED-NEW-B | Medium | **Practitioner formation social risk (2F).** Specify Church faction relationship state, surveillance / Scrutiny mechanics if applicable, and how 2F stacks with 1D for characters with both. |
| ED-NEW-C | High | **Stage 3 Vocations content.** Specify per-faction vocation entries (~20-30 entries across 9 factions). Use template proposed in audit. |
| ED-NEW-D | Medium | **Stage 4 4B and 4E content.** Approve or revise narrative drafts proposed in audit. Specify Certainty modifiers, starting skills. For 4E, coordinate with `threadwork_v30.md` Leap scar mechanics. |
| ED-NEW-E | Low | **Character histories text refinement.** Apply RENN-1 (Swiss/Norwegian replacements), RENN-2 (Empiricist → Observer), PROSE-1 (file ref → design note), 1C "western coast" → "Varfell territories", 1G fortress framing softening, and approved Tartt addenda. |
| ED-NEW-F | Low | **Knot atmospheric weight (PROSE-2 ongoing).** Approve or revise proposed Tartt addenda for 1B, 1C, 1F-Tideward, 1F-Ashmarket, 1G Knots. 1D and 1H Knots flagged as already at strength; no additions recommended. |

ED-NEW-A and ED-NEW-C are the highest-leverage items: they unblock player-facing character creation. ED-NEW-E and ED-NEW-F are low-risk text refinements that can be applied immediately upon Jordan's approval.

---

## Pre-existing open items in source

These are already flagged within `character_histories_v30_infill.md` and are tracked outside this audit:

- **ED-377** — Intuitive Threadwork (3-RE3) + Co-Movement interaction: does folk practice trigger P-01?
- **ED-380** — Southern Einhir Descendant Deep South +8 TS: Leap-eligible with Formation 2F at session 1?
- **ED-390** — War/Invasion specific events (Spartfell Incident, Templar Suppression, Ducal Border Clash): new setting content requires approval.
- **ED-391** — Lost Someone "ghost sheet": design-layer requirement or GM-reference recommendation?

The audit does not duplicate these.

---

## Verification recommendation

Before any edits land in `character_histories_v30.md`:

1. **Verify the audit against the primary file**, not just the infill. The infill is extracted; if extraction is stale or incomplete, gaps may exist in this audit.
2. **Cross-check Stage 3 Vocations status** in the primary — content may exist there that didn't extract to the infill.
3. **Confirm 4B and 4E do not exist** in the primary in some draft form before treating them as fully unwritten.

The audit's flag classifications hold against the infill's content. They are conditional on the infill being a faithful extraction.
