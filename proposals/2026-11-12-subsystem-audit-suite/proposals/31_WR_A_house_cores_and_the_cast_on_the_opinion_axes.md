# WR-31-A — the houses' regime cores and the cast's values on the opinion axes: five roster rows, three decided cells, a link table, and the 46 rows

Reconciled: 2026-11-12, wave 3 (W3-3) — R3 §2 (A-91: Jordan took lane 31's A in all four of J-31-1 to J-31-4): the Status no longer lists four items for Jordan, and the cells A-91 grounds move from `a` to `g` in §4: NPC-050's `solmund_orthodoxy` 4 (A-91 (1)); the Valorsmark fault line's two holders, NPC-036 the Marshal (PR, MI) and NPC-008 the Clerk (PR, MI already `g`) (A-91 (2)); the Restoration Movement's `royal_order` 1 on NPC-041, NPC-087, NPC-088 (NPC-003 already `g`) (A-91 (4)); the Revival's populace starting at the core (A-91 (3)) is carried by `31_WR_B` commit 2's cohort seeding, not by a cast cell here. One reading is marked `[UNVERIFIED]` at NPC-036 (R3 §2: whether PR 2 / MI 3 reads as standing for the militarism end only depends on `20_NARRATIVE_A`'s `stands_for` threshold, R5's lane). Batch (U3 B38). Tier already named.
Reconciled: 2026-11-12, wave-3 mop-up (`unified/work/W3_5b_DONE.md` "For another lane", W3-3 item): the commit table's row 4 now says `20_NARRATIVE_D` owns only the key, loader and readers and that commit 4 here is the declared mover.

## Status: PROPOSED (Jordan's A-87 to A-91 are the cores and the four answered items; every cast cell marked `a` is `[ASSUMPTION; medium; Jordan to correct]`)

Lands in batch: B38 (narrative and regimes), after `30_WR_G` and before `31_WR_B` (U3 §1 item 38).
Depends on: see "Dependencies" below.

Source: Jordan, 2026-11-12, as `unified/DECISIONS_ANSWERED.md` records them: **A-87** (*"varfell anti caste, hafenmark pro caste, valorsmark okay with it"*; *"correlate is restoration movement and Einhir Revival"*; *"hafenmark okay royal order, valorsmark pro royal order, varfell unhappy royal order due to caste"*; *"hafenmark parliamentary, valorsmark mixed, varfell militaristic"*), **A-88** (*"church is neutral on royal order, doesn't care about caste or parliament, cares a lot about religious affiliation and anti-einhir"*), **A-89** (*"hafenmark devout pro solmund, valorsmark pro solmund with Einhir sympathies, varfell neutral leaning Einhir with momentum building for Einhir Revival"*), **A-90** (*"einhir is both"*). Audit: `audits/31_HOUSE_STANCES_AND_CAST_VALUES.md`. Reference only (`CLAUDE.md` §0.05). Lane WR with CHAR.

Completes `30_WR_G_regime_opinions_and_the_pull_of_ones_own.md` commit 2 (the cast's values) and amends its commit 1 (two more rows; no `concerns:` keys). Composes on `20_NARRATIVE_A_stands_for.md` (`stands_for`, `held_reading`), `20_NARRATIVE_D_his_own_side.md` (a faction's `creed:` row), `30_WR_B_regimes_who_believes_whom.md` (`regimes`, `Regime`), `30_WR_G` commit 3 (`accord`). The drift that carries A-89's "momentum building" is `31_WR_B_the_revival_gathers.md`; what the stances feed is `31_WR_C_what_the_stances_feed.md`.

## What it changes in `engine/season/` at runtime

| commit | change | hash |
|---|---|---|
| 1 | five affiliations join the roster (`caste_order`, `royal_order`, `parliamentary_rule`, `militarism`, `einhir_folk`); 35 `incompatible` cells keyed (1 `true`, 2 `false`, 32 `null`); **no** `concerns:` key added; a `vowed:` list keeps the shared vow column off the five | EQUAL (nobody holds them); `engine/engine_params/descriptors.json` re-derived, declared |
| 2 | the 46 cast rows' values on the five new poles; 12 existing `solmund_orthodoxy` cells re-authored under A-89; `einhir_folk` joins concern `einhir` | **declared build-hash mover** (every seeded realm run); the caste estimate `heritage_regard` now means over two poles |
| 3 | `rosters.yaml: regime_cores` (six rows) and `tables.opinion_links` (five rows), with their loaders; `person_q.closeness`, `person_q.link_fit`, `world_q.core_standing` | EQUAL (data with readings only; nothing in the loop reads them) |
| 4 | the faction rows of commit 4 below gain `creed:` signs on the new poles (`20_NARRATIVE_D` edit 1's key; that file owns only the key, its loader and the readers) | EQUAL until `20_NARRATIVE_D` commit 1's reader ships; then this commit is the declared mover (`opinion_of` changes for everyone standing on a pole) |

## 1. The rows (commit 1) — amends `30_WR_G` §2

```yaml
# references/descriptor_registry.yaml: affiliation_roster   (count: 5 -> 10)
    - caste_order         # the order of descent as right: who may hold, earn and command by birth (A-41's informal tiers, held as a position)   [30_WR_G]
    - royal_order         # the kingdom's own order of crown, duchies and bench as the political structure one wants                             [30_WR_G]
    - parliamentary_rule  # that the realm's affairs are decided in assembly and by procedure                                                    [A-87]
    - militarism          # that arms, and those who bear them, should decide the realm's affairs                                                [30_WR_G]
    - einhir_folk         # the Einhir as a people: their kin, speech and custom as one's own or as worthy (the people pole; `einhir_restoration` is the tradition pole)   [A-90]
  concerns:               # commit 1 adds NOTHING here; commit 2 changes one line:
    einhir: [einhir_restoration, einhir_folk]     # was [einhir_restoration]
```

Names are plain words, none a canon name. Three decisions that differ from `30_WR_G` §2, each with its ground:

1. **Government form is two poles, not one.** A-87 puts three houses on one line (parliamentary, mixed, militaristic). The roster's scale "has no AGAINST direction" (`descriptor_registry.yaml:208`), so one pole `militarism` would make Hafenmark's parliament a mere rejection, and under `stands_for` a house that stands for nothing on the question. The tree's precedent for one question with two ends is two members and a `true` cell (`solmund_orthodoxy × einhir_restoration`, "the two poles of the absorbed tracks", `rosters.yaml:3683`). Ladder step 4.
2. **The Einhir are two poles (A-90).** `einhir_restoration` stays the tradition pole; `einhir_folk` is the people pole.
3. **No new `concerns:` key.** `30_WR_G` §2 adds `caste`, `arms` and `crown` under `concerns:` and calls the commit EQUAL. It is not: `data/cast.py::conviction_of` (`:253-262`) refuses every cast row that holds no member of **each** concern, so the realm would not build (probe P-31-5: 46 of 46 rows refused). A member under no concern "is held freely" (`descriptor_registry.yaml:213`), which is also what lets a person not care (A-88): **an absent key is "has not considered it"**, reads 0 in `conviction_stand`, and says nothing in `accord`. `einhir_folk` joins the existing `einhir` concern in commit 2, with the values, because `heritage_regard` counts an absent member as 0 in its mean (`person_q.py:478`) and would halve the caste estimate for everyone if the member arrived before its holders.

4. **An opinion is not a vow.** `affiliation_engagement`'s shared column applies to every roster member alike ("a vow is a vow under every creed on the roster", `rosters.yaml:3724`), so an observer takes a scar count on **every** affiliation he holds for each forgery or defiance he sees, and the shipped crisis then folds his highest-held creed into its `true` partner (`16_PESSIMIST_CHAR_A` §2: 31 of 46). With the `true` cell below, a clerk at `parliamentary_rule` 5 would be folded into `militarism` by three forgeries `[derived from the rule as that lane measured it; not observed in this lane's two-season runs, where the five rewrites were all of religious poles, P-31-8]`. So the roster gains `vowed: [solmund_orthodoxy, inner_tradition, thread_truth, einhir_restoration, altonian_civics]` (the shipped five: EQUAL), and `data/affiliations.py::engagement` returns `None` for a member outside it. `[ASSUMPTION; medium; Jordan to correct; revert: add the member to `vowed`]`. `altonian_civics` stays as ED-IN-0293 ruled it.

**The cells** (`engine/season/rosters.yaml: tables.incompatible.cells`; 45 pairs over ten, 35 new; each keyed once):

| pair | cell | ground |
|---|---|---|
| `parliamentary_rule × militarism` | **`true`** | the two ends of A-87's one line; pair-3 precedent. `[ASSUMPTION; Jordan to correct; revert: null]` |
| `caste_order × royal_order` | **`false`** | the settlement that made the Crown made the caste (`canon/03_canonical_timeline.md:104`); a recorded compatibility, which is what lets `commensurate` read +1 between a holder of each |
| `einhir_folk × einhir_restoration` | **`false`** | A-90: one thing with two faces |
| the other 32, among them `caste_order × einhir_restoration`, `caste_order × einhir_folk`, `solmund_orthodoxy × einhir_folk`, `royal_order × altonian_civics` | `null` | no ruling says holding both strains. A-87's "correlate" is a tendency and is carried as a link (§3), not as a strain; A-89 has Valorsmark hold faith and sympathy for the Einhir people together |

`affiliation_engagement` gains no cell. `heritage_roster.engages` is untouched (ED-IN-0301 stands as written).

## 2. The houses' and movements' regime cores (commit 3, data)

On the roster's own 0 to 5 scale; a half is "between" (the members sit on both sides of it); an absent key is "does not care". **One vocabulary for every axis** (`CLAUDE.md` §0.06 S: one ladder for one quantity): anti 0.5 · unhappy 1.5 · okay, neutral, mixed 2.5 · leaning, sympathies 3.5 · pro 4.5 · devout, cares a lot 5 · does not care: no key.

```yaml
# engine/season/rosters.yaml: regime_cores   (new; loader data/rosters.py::REGIME_CORES; every key a rostered affiliation, every value in [0, 5] in halves)
  "Valorsmark":           {of: {faction: "Valorsmark"},
                           stands: {solmund_orthodoxy: 4.5, einhir_restoration: 1.5, einhir_folk: 3.5, caste_order: 2.5, royal_order: 4.5, parliamentary_rule: 2.5, militarism: 2.5}}
  "Hafenmark":            {of: {faction: "Hafenmark"},
                           stands: {solmund_orthodoxy: 5, einhir_restoration: 0.5, einhir_folk: 1, caste_order: 4.5, royal_order: 2.5, parliamentary_rule: 4.5, militarism: 1}}
  "Varfell":              {of: {faction: "Varfell"},
                           stands: {solmund_orthodoxy: 2.5, einhir_restoration: 3.5, einhir_folk: 4.5, caste_order: 0.5, royal_order: 1.5, parliamentary_rule: 1.5, militarism: 4.5}}
  "Church of Solmund":    {of: {faction: "Church of Solmund"},
                           stands: {solmund_orthodoxy: 5, einhir_restoration: 0, einhir_folk: 0.5, royal_order: 2.5}}      # caste_order, parliamentary_rule, militarism absent: A-88
  "Restoration Movement": {of: {faction: "Restoration Movement"},
                           stands: {einhir_restoration: 5, einhir_folk: 5, caste_order: 0, royal_order: 1, militarism: 1, solmund_orthodoxy: 1}}
  "Einhir Revival":       {of: null,                                                                                         # a cause that crosses factions; no faction row carries it
                           stands: {einhir_restoration: 4.5, einhir_folk: 5, caste_order: 0.5}}
```

| cell | Jordan's word | value | note |
|---|---|---|---|
| caste: Varfell / Hafenmark / Valorsmark | anti / pro / okay with it | 0.5 / 4.5 / 2.5 | "okay" is the midpoint in both places it is used |
| royal order: Hafenmark / Valorsmark / Varfell | okay / pro / unhappy, due to caste | 2.5 / 4.5 / 1.5 | Varfell's is unhappy, not a rejection: its Duke is a duke of that order (`canon/03:88`) |
| government: Hafenmark / Valorsmark / Varfell | parliamentary / mixed / militaristic | PR 4.5, MI 1 / 2.5, 2.5 / 1.5, 4.5 | Varfell's `parliamentary_rule` is not 0: the Jarl Council keeps "the confederacy's oral law" (`engine/season/goals.yaml: goal_jarl_council_confederacy`) |
| Solmund: Hafenmark / Valorsmark / Varfell | devout / pro / neutral | 5 / 4.5 / 2.5 | A-89 |
| Einhir: Valorsmark / Varfell | sympathies / leaning, momentum building | folk 3.5, tradition 1.5 / folk 4.5, tradition 3.5 | A-90: Valorsmark's sympathy sits on the people pole, which holds with faith without strain. Hafenmark's `einhir_folk` 1 is `[ASSUMPTION]`, read off the correlate link |
| the Church | neutral on royal order; does not care about caste or parliament; cares a lot about religious affiliation; anti-Einhir (both, A-90) | RO 2.5; no key on caste, parliament, arms; SO 5; tradition 0, folk 0.5 | so the Church is hostile to the Einhir and indifferent to the tiers |
| Restoration Movement | (A-87's correlate) | caste 0, royal 1 | `goals.yaml: goal_restoration_caste_ended` ("ends the caste order -- communal sovereignty in its place") is engine data; `militarism` 1 from its `reformist` template (`rosters.yaml: role_templates.by_faction`) `[ASSUMPTION]` |
| Einhir Revival | (A-87's correlate; A-89) | tradition 4.5, folk 5, caste 0.5 | not a faction in `names_index.yaml`; in the registry it is a goal shared by the Queen (NPC-032), the Duke of Varfell (NPC-052) and the Movement. It is a regime that crosses three factions, and that is how it is authored |

**What a core row is, and is not.** It is the start state and the name. It is read (a) by the cast rule of §4 and by the generation tables when they seed a cohort or a generated person of that faction (CR-107; `21_PROCEDURAL_B`; A-44, A-50), and (b) by `world_q.core_standing` (commit 3), which reads how near each person's own stands sit to the row. It assigns nobody: membership stays a reading of each person's own `conviction` (`30_WR_B`: "no regime is stored"), a person may be near several rows at once (the Revival crosses Varfell and the Movement by design), and a row nobody is near names nothing. A house's **live** core is the mean stand of its living members, recomputed; the gap between the live core and this row is the drift `31_WR_B` reads.

## 3. The links (commit 3, data): one axis bearing on another

```yaml
# engine/season/rosters.yaml: tables.opinion_links   (new; loader data/affiliations.py::OPINION_LINKS; refused: an unrostered name, a self-link, a pair keyed twice in one direction, a sign outside {-1, 1})
  - {from: caste_order,        to: royal_order,        sign:  1}   # A-87 "unhappy royal order due to caste": the royal order as settled carries the caste (canon/03:104)
  - {from: einhir_folk,        to: einhir_restoration, sign:  1}   # A-90 "einhir is both"
  - {from: einhir_restoration, to: einhir_folk,        sign:  1}   # A-90, the other direction
  - {from: caste_order,        to: einhir_folk,        sign: -1}   # A-87 "correlate"; the caste is the relegation of the southern Einhir (canon/03:96)
  - {from: caste_order,        to: einhir_restoration, sign: -1}   # A-87 "correlate"; goals.yaml: goal_restoration_caste_ended; NPC-032 and NPC-052 hold both goals
```

A link is a **tendency between two of a person's own stands**. It has two readers and neither fires anything:

- **A reading** (this proposal, EQUAL): `person_q.link_fit(p, link) = sign × conviction_stand(p, from) × conviction_stand(p, to)`, on `[-1, +1]`. Above 0 his two stands sit as the link expects ("against the royal order, on account of the caste"); below 0 he is **pulled apart** (the Queen: against the caste at 0, for the royal order at 5, fit −1, because she means to end the one by the other). `regimes` prints, per body and link, the mean fit and the words "on account of" when the mean fit is above 0 and the body's stand on `from` is at least as firm as on `to`.
- **Odds** (`31_WR_B`, behind a fixture): when one of his stands is up for a drawn move, the direction's odds lean by the link. Never a step taken because another was.

So "Varfell unhappy with the royal order due to caste" is one row of data plus two readings: the regime block says why, and the drift makes a Varfell man who softens on the caste likelier to soften on the Crown, and one who cannot be moved on the caste hard to win for it. **Stated limit:** the link is a fact about the realm as settled. If the Crown ends the caste (the Queen's goal), the row `caste_order → royal_order` should stop holding; no act writes `rosters.yaml`, and none is proposed. What is built instead is in `31_WR_B` §3: the deed itself (a decree against the caste, seen or told) is evidence on `royal_order` for those who stand against the caste, so they move toward the Crown by what it does.

## 4. The cast (commit 2)

**The rule**, applied per cell, first that applies:

- **R1, his own text.** The row's `goals`, `role`, `arc_trajectory`, the basis comment on its `affiliations:` line, or a canon sentence naming him states a position: that value, wherever it falls. Marked `g`.
- **R2, his office or body.** A goal row of his seat or body in `engine/season/goals.yaml`, his `cultural_label`, or the plain nature of his office bears on the axis: the core, moved one step toward the office's interest. `g` where a data row is cited, else `a`.
- **R3, his house's core** (§2), as an integer: a half rounds **down** for a person with no ground (nobody is made to stand for a thing on no evidence). `a`.
- **R4, neither.** His faction has no core from Jordan and nothing in his row bears on the axis: **no key**. He has not considered it. This is a value, and the honest one.

Bound: a person with no text of his own sits within one step of his core. Heads and named dissenters may sit anywhere (the Queen, the King, the Duchess, the Duke, the Grandmaster).

**Existing cells** (the five shipped poles) are changed only where A-89 contradicts the stored value: twelve `solmund_orthodoxy` cells, marked `*`. No `einhir_restoration` cell is changed: Varfell's five principals already sit at 4 or 5, each on its own row's text ("fights for Einhir, not Vaynard"), and they are read here as the Revival's vanguard inside a house whose core leans (§2); the house's leaners are its cohorts and generated persons, seeded from the core row (`31_WR_B` §4).

**The table.** Columns: SO `solmund_orthodoxy`, IT `inner_tradition`, TT `thread_truth`, ER `einhir_restoration`, EF `einhir_folk`, AC `altonian_civics`, CO `caste_order`, RO `royal_order`, PR `parliamentary_rule`, MI `militarism`. A bare number is the shipped value, unchanged. `g` grounded (the ground is in the last column), `a` assumption, `*` a shipped cell re-authored, `-` no key. This table is the data commit 2 lands; the probe in the audit's evidence log parsed it from this file.

| id | name | house | SO | IT | TT | ER | EF | AC | CO | RO | PR | MI | grounds (registry row, `goals.yaml`, canon) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NPC-020 | Almud Almqvist | Valorsmark | 3 | - | 1 | 2 | 4g | 1 | 2g | 5g | 3a | 2a | canon/03:138 "ethical doubt about the caste", northern Einhir; the King's seat is the Crown's goal; row: "privately sympathizes with Restoration" |
| NPC-032 | Lenneth Almqvist | Valorsmark | 1 | - | - | 5 | 5g | 1 | 0g | 5g | 2a | 1a | goals: "Einhir revival through Crown authority", "Caste dismantlement through royal decree"; canon/03:139 patronage, not arms |
| NPC-031 | Torben Almqvist | Valorsmark | 2 | - | - | 1 | 3a | 1 | 2a | 3a | 2a | 2a | row: "convictions left by canon to emerge in play: near-flat"; every new cell at the middle |
| NPC-030 | Elske Almqvist | Valorsmark | 2 | - | - | 1 | 3a | 2 | 2a | 4a | 2a | 1a | her marriage ratified the trade peace (canon/03:120) |
| NPC-008 | Peder Almstedt | Valorsmark | 4*a | - | - | 0 | 2a | 2 | 3a | 4a | 5g | 1g | role: Chief Parliamentary Clerk; goals: "procedural correctness", "Block radical action through procedure"; row: Einhir revival is what he blocks |
| NPC-009 | Gerik Strand | Valorsmark | 4*a | - | - | 1 | 3a | 1 | 2a | 4g | 2a | 2a | goals: "Efficient Crown administration" |
| NPC-033 | Kolbrun Thale | Valorsmark | 1 | - | - | 1 | 2a | 1 | 2a | 4a | 2a | 2a | row: "lowest of the circle: all three low" (SO kept) |
| NPC-035 | Theodor Kreutz | Valorsmark | 4*a | - | - | 1 | 3a | 1 | 2a | 5g | 2a | 3a | row: "sworn to Almud personally"; Royal Guard Captain |
| NPC-036 | Wilhelm Voss | Valorsmark | 4*a | - | - | 1 | 3a | 1 | 2a | 4a | 2g | 3g | Royal Marshal: the arms side of a mixed house; A-91 (2): he and the Clerk discount each other's word `[UNVERIFIED: that PR 2 / MI 3 reads as standing for the militarism end only — `20_NARRATIVE_A`'s `stands_for` threshold]` |
| NPC-037 | Annalie Reichard | Valorsmark | 4*a | - | - | 1 | 3a | 1 | 2a | 4a | 3a | 2a | Lord Treasurer: the accounts side |
| NPC-083 | Hedda Kronvald | Valorsmark | 3 | - | - | 1 | 2a | 1 | 3a | 4a | 2a | 2a | row: "the Pope's side"; governs a southern Crown territory "viewed as instrumental" (canon/03:100) |
| NPC-050 | Inge Baralta | Hafenmark | 4*g | - | - | 0 | 0g | 0 | 5a | 3g | 4g | 1a | A-89 against her row's "faith privatised", ruled A-91 (1) (J-31-1: devout in doctrine, set against the Church's jurisdiction); canon/03:143 "Wants the Crown", "Pure RM adversary"; goals: "Hafenmark parliamentary sovereignty"; row: "a divine-right claimant behind the procedural frame" |
| NPC-071 | Torvi Heljason | Hafenmark | 4*a | - | - | 1 | 1a | 1 | 4a | 2a | 5g | 1a | role: Legal Advisor, "the constitutional line"; `goal_hafenmark_constitutional_order` |
| NPC-072 | Olaf Geirson | Hafenmark | 4*a | - | - | 1 | 1a | 1 | 4a | 2a | 3a | 2a | Military Commander in a parliamentary house |
| NPC-081 | Uta Falkenrath | Hafenmark | 5*a | - | - | 1 | 2a | 1 | 3a | 3a | 5g | 1a | role: Commune Representative, "a mediator" |
| NPC-052 | Magnus Vaynard | Varfell | 1 | - | 2 | 5 | 5g | 1 | 0g | 1g | 1a | 5g | goals: "Dismantle post-war caste order", "Varfell military expansion"; canon/03:144; heritage southern_einhir; A-87 on the royal order |
| NPC-073 | Björn Holdar | Varfell | 2*a | - | - | 4 | 4a | 1 | 1a | 2a | 2g | 4a | Senior Jarl; `goal_jarl_council_confederacy` ("oral law and the Jarls' held ground") |
| NPC-074 | Ingrid Stenskald | Varfell | 1 | - | - | 5 | 5g | 1 | 0a | 1a | 2g | 3a | row: "keeper of Einhir tradition"; the council's oral law is hers to keep |
| NPC-082 | Njal Torberg | Varfell | 2*a | - | - | 5 | 5g | 1 | 0a | 1a | 1a | 5g | role: Military Jarl; row: "fights for Einhir, not Vaynard" |
| NPC-002 | Maret Uln | Varfell | 2*a | - | 2 | 4 | 5g | 1 | 0a | 1a | 2a | 3a | birthplace near southern Einhir communities; goals: "Privately sympathize with Restoration Movement" |
| NPC-021 | Arne Himlensendt | Church | 5 | - | 1 | 0 | 0g | 1 | - | 2a | - | - | A-88, A-90: the head holds the core; row: Einhir 0, opposed |
| NPC-038 | Arnlod Olafsson | Church | 5 | - | - | 0 | 0g | 1 | - | 2a | - | - | `goal_inquisitors_find_heresy`; row: office goal is finding Einhir-revivalist activity |
| NPC-004 | Sæmund Haelgrund | Church | 5 | - | 1 | 0 | 1a | 1 | - | 2a | - | - | row: "private conclusions contradict his public role" |
| NPC-040 | Osten Jarnstal | Church | 5 | - | - | 1 | 0a | 1 | - | 2a | - | 3g | `goal_cardinal_fortitude_enforcement` ("the Church's arms ready"): the one churchman who has considered rule by arms |
| NPC-039 | Magnus Klapp | Church | 4 | - | 1 | 1 | 1a | 1 | - | 2a | - | - | row: the archivist who protects forbidden texts |
| NPC-013 | Aldric Tormann | Church | 3 | - | - | 1 | 1a | 1 | - | 3a | - | - | row: the economic arm; tithes need the order kept |
| NPC-034 | Gustav Linder | Church | 5 | - | - | 1 | 0a | 1 | - | 3a | - | - | row: seated in the King's Inner Circle; "the Church side dominates" |
| NPC-003 | Yrsa Vossen | Restoration Movement | 1 | - | 2 | 5 | 5g | 1 | 0g | 1g | 3g | 1a | goals: "Cultural restoration", "Equity and social contract"; `goal_restoration_caste_ended` |
| NPC-041 | Aldric Hann | Restoration Movement | 1 | - | - | 5 | 5a | 1 | 0g | 1g | - | 1a | row: "no authored vector; read off the RM reformist profile"; the faction's goal rows |
| NPC-087 | Uwe Askeland | Restoration Movement | 1 | - | - | 4 | 5g | 1 | 0g | 1g | - | 0a | role: hedge-school teacher of Einhir education |
| NPC-088 | Carin Vedel | Restoration Movement | 1 | - | - | 5 | 5g | 1 | 0g | 1g | - | 1a | role: copyist of suppressed Einhir texts |
| NPC-070 | Lisbeth Ehrenwall | Löwenritter | 2 | - | - | 1 | - | 1 | - | 3g | - | 5g | row: "Almud is faltering, I must be ready to act"; `military-order` template |
| NPC-006 | Halvar Brandt | Löwenritter | 2 | - | - | 1 | - | 0 | - | 4g | - | 4g | `goal_lowenritter_throne_security`, `goal_lowenritter_military_security`; goals: "Strengthen peninsular defenses" |
| NPC-005 | Sigrid Torsvald | Löwenritter | 2 | - | 3 | 1 | - | 1 | - | 4g | - | 3a | `goal_riskbreakers_royal_safety`; covert, "Minimize Thread collateral" |
| NPC-080 | Vidar Haldorsen | Löwenritter | 3 | - | - | 1 | - | 1 | - | 5g | - | 4g | row: doctrine-following; the Riskbreakers' goal rows |
| NPC-007 | Annika Feldhaus | Guilds | 2 | - | - | 1 | - | 1 | - | 2a | 3a | 1a | `goal_guilds_no_faction_controls`; goals: "Protect artisan livelihoods" |
| NPC-084 | Frieda Kessler | Guilds | 2 | - | - | 1 | - | 1 | - | 3a | 4g | 1a | `cultural_label: hafenmark_procedural`; row: "Mandate over Wealth" |
| NPC-085 | Nessa Grindvold | Guilds | 1 | - | - | 1 | - | 1 | - | 1g | 5g | 1a | role: Guild Advocate at the Crown court; row: "guild autonomy against the Crown" |
| NPC-086 | Joren Bergvall | Guilds | 1 | - | - | 1 | - | 1 | - | 2a | 4g | 1a | `cultural_label: hafenmark_procedural` |
| NPC-089 | Zoe Palaiologina | Altonia | 1 | - | - | 1 | 1g | 5 | - | 0g | - | 5g | `goal_altonia_conquer_valoria`, `goal_katepano_press_the_capital`; canon/03:66 (the empire destroyed Einhir heritage) |
| NPC-090 | Stephanos Doukas | Altonia | 1 | - | - | 1 | - | 4 | - | 2g | - | 1g | `goal_kommerkiarios_treaty_order`; row: "the instrument rather than the decider" |
| NPC-011 | Alexios Laskaris | Altonia | 1 | - | - | 1 | - | 3 | - | 3g | - | 1g | goals: "Sandbag imperial directives", "Protect Elske's safety"; row: "leans toward the Crown" |
| NPC-001 | Edeyja | Independent | - | 4 | 5 | 1 | 3a | 1 | - | - | - | - | row: "the work, not politics"; birthplace Southernmost |
| NPC-075 | Orm | Independent | - | 3 | 4 | 2 | 4g | 1 | - | - | - | - | goals: "The work. Only the work."; `cultural_label: einhir_traditional` |
| NPC-010 | Dalla Virke | Independent | 1 | - | - | 1 | - | 1 | - | - | - | - | row: "outside every faction: all three at the floor" |
| NPC-012 | Rikard Solberg | Independent | 1 | - | - | 1 | - | 2 | - | 3a | - | 1g | goals: "Maintain stable trade", "Avoid escalation" |

Counts (the probe's parse of this table, P-31-0): 230 new-pole cells; 163 hold a value (57 `g`, 106 `a`), 67 are no key; 12 shipped cells re-authored. After A-91 (wave 3, counted by hand from the five edited new-pole cells, not re-run): 62 `g`, 101 `a`; NPC-050's re-authored `solmund_orthodoxy` cell is now grounded as well. No person stands for both ends of a `true` pair, so nobody is authored into a strain; the fault lines run between persons.

## Instructions to code

Tier: commits 1, 3, 4 second tier (sonnet); commit 2 is transcription of the table above (haiku, with a second-tier check of the 46 rows against this file). Order 1, 2, 3, 4. Commit 2 after `20_NARRATIVE_A` commit 2 (`held_reading: stands`) if the realm is to read as §5 of the audit shows; it lands without it and then every reader of `_held` treats a value of 1 as a holding, which is the defect that proposal repairs.

**Commit 1 (EQUAL).**
1. `references/descriptor_registry.yaml: affiliation_roster`: `count: 10`; the five names of §1 appended after `altonian_civics`, in that order; the header comment's "A FIFTH" paragraph gains one line naming the five and A-87 to A-90. **No `concerns:` edit.** A new key `vowed: [solmund_orthodoxy, inner_tradition, thread_truth, einhir_restoration, altonian_civics]`, exported with the roster (`AFFILIATION_VOWED` in `engine/substrate/descriptors.py`); `engine/season/data/affiliations.py::engagement` (`:205`) returns `None` for a `name` outside it, before the shared-column lookup. Test, `test_h11_affiliation_scar.py::test_an_opinion_takes_no_scar_from_the_vow_column`.
2. `python tools/export_descriptors.py` then `python tools/export_descriptors.py --check` (never hand-edit `engine/engine_params/descriptors.json`).
3. `engine/season/rosters.yaml: tables.incompatible.cells`: the 35 new pairs, each keyed once: under `caste_order`: `royal_order: false`, and `parliamentary_rule`, `militarism`, `einhir_folk` `null`; under `parliamentary_rule`: `militarism: true`, `royal_order: null`, `einhir_folk: null`; under `militarism`: `royal_order: null`, `einhir_folk: null`; under `royal_order`: `einhir_folk: null`; under `einhir_restoration`: `einhir_folk: false`; and each of the five new names against each of the five shipped ones `null` except that one (25 cells, 24 `null`). The block's `note:` count line becomes "forty-five pairs over ten".
4. Tests. Covering files (`grep -rl AFFILIATIONS engine/season/tests`): `test_h10_affiliations.py`, `test_h11_affiliation_scar.py`, `test_in64_cast_integration.py`, `test_rem30_character_sheet.py`; any pin of five members or ten pairs becomes ten and forty-five, said in the commit. Add `test_h10_affiliations.py::test_a_new_affiliation_nobody_holds_moves_no_hash` (`build_realm(0).content_hash()` equal to the pre-commit pin) and `::test_a_member_under_no_concern_is_not_demanded_of_a_cast_row` (a row holding none of the five new members passes `conviction_of`).

**Commit 2 (declared build-hash mover).**
1. `references/npc_registry.yaml`, each of the 46 rows' `affiliations:` mapping: the cells of §4's table that carry `g`, `a` or `*`. A `-` writes nothing. The row's basis comment gains "A-87..A-90 (lane 31): " and the last column's text. Owner and reader: `engine/season/data/cast.py::conviction_of` (`:234`); `30_WR_G` names `engine/season/npcs.yaml` for this, which is the case roster and holds no conviction.
2. `references/descriptor_registry.yaml: affiliation_roster.concerns.einhir: [einhir_restoration, einhir_folk]`; re-export and `--check`.
3. Re-pin, and say so plainly in the commit: every seeded golden that builds the realm (`engine/tests/`, `engine/season/tests/` pins found by `python tools/tests_for_diff.py`).
4. Tests, `engine/season/tests/test_in64_cast_integration.py`: `test_every_house_member_sits_within_one_step_of_his_core_or_names_a_ground` is **not** added (it would be a guard over authoring, `CLAUDE.md` §0.1 pt 5). Added: `test_the_three_houses_differ_on_caste_royal_order_and_government` (on `build_realm(0)`: the mean `conviction_stand` over each house's members orders Varfell < Valorsmark < Hafenmark on `caste_order`, Varfell < Hafenmark < Valorsmark on `royal_order`, Varfell < Valorsmark < Hafenmark on `parliamentary_rule` and the reverse on `militarism`; `assert checked == 12`), `test_no_churchman_holds_a_stand_on_caste_or_parliament`, `test_the_church_stands_against_both_einhir_poles`.

**Commit 3 (EQUAL).**
1. `engine/season/rosters.yaml`: `regime_cores` (§2) and `tables.opinion_links` (§3), each with a `source:` line naming A-87 to A-90 and `[ASSUMPTION; medium; Jordan to correct; revert: delete the row]`.
2. `engine/season/data/rosters.py`: `REGIME_CORES` (name → `(faction or None, {affiliation: float})`), refusing an unrostered affiliation, a value outside `[0, 5]` or off the half grid, an `of.faction` that is no `FACTIONS` member. `engine/season/data/affiliations.py`: `OPINION_LINKS` (a tuple of `(from, to, sign)`), with the four refusals of §3.
3. `engine/season/queries/person_q.py`, beside `conviction_stand`:

```python
def link_fit(p: Person, link: tuple) -> float:
    """[-1, +1]: `sign * conviction_stand(p, frm) * conviction_stand(p, to)` for one row of
    `data/affiliations.py::OPINION_LINKS`. Above 0 his two stands sit as the link expects; below 0 he is
    pulled apart. 0.0 when he has not considered either (an absent key). Person-side, no World (AX-2)."""
```

```python
def closeness(p: Person, stands: dict) -> float:
    """[-1, +1]: `1 - mean over the axes `stands` names of |conviction_stand(p, a) - (stands[a] - mid) / half|`.
    An axis he has not considered reads 0 (the midpoint). 1.0 is the row exactly; the measure is a distance,
    not `accord`'s product, because a core at the midpoint ("okay", "mixed", "neutral") is a position and a
    product reads it as nothing. Person-side, no World."""
```

4. `engine/season/queries/world_q.py`, beside `regimes` (`30_WR_B` commit 1):

```python
class CoreStanding(NamedTuple):
    name: str           # a `REGIME_CORES` row
    core: tuple         # person ids with `closeness` >= Fixtures `core_closeness`, sorted
    fringe: tuple       # ids with `fringe_closeness` <= closeness < `core_closeness`, sorted
    live: dict          # {axis: mean conviction_stand} over `members(w, faction)` where the row has one, else over `core`
    links: tuple        # per `OPINION_LINKS` row, the mean `link_fit` over `core`

def core_standing(w: World) -> tuple:
    """One `CoreStanding` per `REGIME_CORES` row, in roster order. Recomputed; stores nothing; no consumer in
    the loop. A person may be in several cores (the Revival crosses Varfell and the Movement); a row with an
    empty core names nothing live."""
```

   `data/fixtures.py`: `core_closeness=0.6`, `fringe_closeness=0.3`, each a NUMBER row in `hole_register.yaml`, swept `0.5 / 0.6 / 0.7` and `0.2 / 0.3 / 0.4`, `[ASSUMPTION; medium; Jordan to correct]`; they move only what a reading prints. `Regime` (`30_WR_B`) is not changed: its creed-set bodies stay as that file's reading, and with ten axes they are 25 sets among 46 persons, the largest of five (P-31-3), so `core_standing` is the reading that says which regimes the realm holds.
5. `engine/season/harness/storybar.py --regimes` (`30_WR_B` commit 2) gains, per `REGIME_CORES` row: `core <name>: n=<core> fringe=<n> by faction <…> live=<stand per axis> gap=<live − authored>`, and per link with mean fit above 0.1 or below −0.1, `<to> on account of <from> (fit +0.50)` or `<to> against <from> (fit -1.00)`; then per person in two or more cores, the cores.
6. Tests, `engine/season/tests/test_strife_credit.py`: `test_link_fit_is_zero_for_an_unconsidered_axis`, `test_closeness_of_a_person_exactly_on_a_row_is_one`, `test_the_queen_is_pulled_apart_on_caste_and_crown` (fit −1.0 on the built realm), `test_varfell_reads_against_the_royal_order_on_account_of_the_caste` (the Varfell core's mean fit on the first link above 0, and its live stand on `caste_order` firmer than on `royal_order`), `test_every_core_row_has_a_core_on_the_built_realm` (`assert checked == 6`), `test_the_revival_crosses_three_factions` (its core holds members of Varfell, the Restoration Movement and Valorsmark), `test_regime_cores_and_links_move_no_hash`.

**Commit 4 (EQUAL until its reader ships).** `engine/season/rosters.yaml: factions`, the `creed:` key of `20_NARRATIVE_D` edit 1, sign only, each sign the sign of that house's core where the core is at least one step from the midpoint:

```yaml
"Valorsmark":            {creed: {royal_order: 1, solmund_orthodoxy: 1, einhir_folk: 1}}
"Hafenmark":             {creed: {caste_order: 1, parliamentary_rule: 1, solmund_orthodoxy: 1, militarism: -1, einhir_restoration: -1, einhir_folk: -1}}
"Varfell":               {creed: {einhir_restoration: 1, einhir_folk: 1, militarism: 1, caste_order: -1, royal_order: -1, parliamentary_rule: -1}}
"Church of Solmund":     {creed: {solmund_orthodoxy: 1, einhir_restoration: -1, einhir_folk: -1}}
"Restoration Movement":  {creed: {einhir_restoration: 1, einhir_folk: 1, caste_order: -1, royal_order: -1}}
```

These replace `20_NARRATIVE_D`'s four first-content rows (which they contain) and give the Crown and Hafenmark the creed that file withheld because their members then stood on no common pole. The engaged poles are what `world_q.engaged_poles` returns and `opinion_of` reads; nothing else changes there.

## The gate (execution artifacts)

```sh
python tools/export_descriptors.py --check
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --arms off off --regimes
python -m pytest engine/season/tests/test_h10_affiliations.py engine/season/tests/test_in64_cast_integration.py engine/season/tests/test_strife_credit.py -q   # at the close, once
```

Expected readings are the audit's §5 table (probes P-31-1 to P-31-6), reproduced by the harness on the built realm at seed 0: the three houses ordered as A-87 says on four axes; the Church with no stand on caste or parliament; `commensurate` over the 1,035 cast pairs at `held_reading: stands` reading 357 / 247 / 431 where the shipped values read 130 / 779 / 126; core sizes 18, 6, 5, 12, 9, 10 in roster order, the Varfell core exactly Varfell's five and the Revival's ten drawn from three factions; the first link's mean fit +0.50 for Varfell, 0.00 for Hafenmark, −1.0 for the Queen. Control: the realm before commit 2 (`git stash` of the registry edit, or the pre-commit pin), where every new-pole reading prints `n/a (unheld)` and `commensurate` reads as `20_NARRATIVE_A` measured it.

## The falsifier, and its control

- Any hash moving after commit 1, 3 or 4 (before `20_NARRATIVE_D`'s reader): a reader of the new rows exists that this file did not find.
- The house order on any of the four axes differing from A-87 on the built realm: a transcription error in commit 2.
- A churchman with a key on `caste_order` or `parliamentary_rule`: A-88 broken in authoring.
- `heritage_regard` unchanged for a Valorsmark observer after commit 2: `einhir_folk` did not join the concern (the mean is still over one pole).
- On the shipped values (the control) the six cores read 36, 0, 0, 6, 0, 0 (P-31-6): one wide tent and a church. If the treated realm reads the same, commit 2 did not land; if the control reads six distinct cores, `closeness` is not reading `conviction`.
- A person in a core whose row he stands against on an axis the row holds at 0 or 5: `closeness` is reading the wrong sign.
- A scar count on `caste_order`, `royal_order`, `parliamentary_rule`, `militarism` or `einhir_folk` after a forgery is seen: the `vowed` list is not read.
- Control arms: the roster of five (commit 1); the pre-commit registry (commit 2); `held_reading: any`.

## Dependencies

`20_NARRATIVE_A` (the reading), `20_NARRATIVE_D` (the `creed:` key and its reader), `30_WR_B` commits 1 and 2, `30_WR_G` commits 1 (amended here) and 3. Feeds `31_WR_B`, `31_WR_C`, `30_GO_F`, `U5d_SE_cohort_heavy_moves_and_caste.md` (the `caste_practice` tiers are what `caste_order` is an opinion about), `U5d_FA_owed_edits.md` §4, CR-107 and `21_PROCEDURAL_B` (cohorts and generated persons seeded from a core row).

## Layer 1

`04` §A.2 (`queries/` owns nothing; `data/` loads and refuses): kept, **STRUCTURAL**. AX-2: `link_fit` is person-side; `regimes` is the observer's. `CLAUDE.md` §0.05 cl. 1: every fact here lands in YAML code reads (`descriptor_registry.yaml`, `rosters.yaml`, `npc_registry.yaml`), none in prose; this file is the plan. Scripting drift: no row, reader or test names a house or a person in code; the houses differ because their data differs. **MECHANICAL** (the tests assert an order of means over `members(faction)`, read from data).

## NERS reading

- **N.** Without the values the three poles `30_WR_G` adds are held by nobody and every reading of them is `n/a`; without the cores a generated Varfell man has nothing to be seeded from; without the link "due to caste" is a sentence in a ruling. Holds top-down (three houses that differ), bottom-up (one clerk who stands for procedure in a mixed house), laterally (the same rows serve credit, opinion of a side, the caste estimate and the offer), diagonally (the Queen against her own house's core). Narrowed: 106 of 163 cells are assumptions.
- **R.** The Church hostile to the Einhir and indifferent to the tiers; a devout duchess whose house's goal is to break the Church's hold; a Queen pulled apart; a cause that crosses three factions. Each is in the data with no player. Complete: a person with no key is not a zero.
- **S.** One scale, one stand reader, one accord rule for persons and for cores; the link is read by the same `conviction_stand`.
- **E, last.** Five rows, three cells, two small tables and 163 integers against three houses, a church and two movements that can be told apart. High; it would be low if a house's stance lived anywhere but its people's rows.

## Cost class

Edit (1). Authoring by transcription, a declared mover (2). Small build (3). Edit (4).
