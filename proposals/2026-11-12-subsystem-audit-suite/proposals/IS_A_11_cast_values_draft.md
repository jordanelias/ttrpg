# IS-A-11 stage 1 — the cast's authored values, drafted for Jordan to correct

## Status: PROPOSED (workplan v12 B04.26 step 1, `IS-A-11` stage 1; decision-ready, not canon; reference under CLAUDE.md §0.05 — no program reads this file; BA1 (`BA1-cast-content`, after B10) lands each table into its owner through that owner's loader)

## Written against: the working tree at `1a52ac6` (B04.09 landed: a cast row may author `capabilities:`), 2026-11-17.

**What this is.** `IS-A-11`'s stage 1 (`master/instructions/IS_A_NINE_part2.md`, "Item: IS-A-11"): five tables, each
row carrying its basis from `references/npc_registry.yaml` (`role`, `faction`, `resonant_style`, `convictions`, `goals`,
`notes`, `source`) or marked `[NO BASIS IN THE TREE]`. Jordan corrects the tables; merging the batch ratifies them unless
the PR body holds one back (ED-1094).

**The V2 fold (ED-IN-0378, Jordan 2026-11-17: the social contest's V2 is authoritative on all social verbs).** Table (a)'s
skill keys are five: `copying`, `argue`, `inquiry`, `arms`, `law` — no `insight`, no `deception` (V2 part 2 §C.6, §C.3;
part 4 §G lists the cuts, §H the plan corrections; B04.18). A source cell that rests on a mechanism V2 replaced for the social verbs (a `moved_by` trait as the thing an
argument works on, a judge's skill, a lie's detection draw) is marked `[SUPERSEDED BY V2]` and is not filled.

**Marks.** `[NO BASIS IN THE TREE]` — no registry field (and, for (b)–(e), no source-proposal cell) grounds a value; the
cell proposes none. `[SUPERSEDED BY V2]` — see above. A basis cell names the registry field and quotes it; the
MAGNITUDE beside a grounded key is this draft's (the rule below), never the registry's, except where the row authors it.

**`law`.** B04.18's row (`base: attr.mind.acuity`, scale `[0, 7]`; gloss without "a judge's skill", V2 part 2 §D), landed in this batch after this draft's tree (`c3a89e2`); `cast.py::capabilities_of` admits it.

---

### (a) Per cast person: attributes (`stats:`), skills and skill scores (`capabilities:`), manner

**Row count: 46** — one per `characters:` row of `references/npc_registry.yaml`
(`python -c "import yaml;print(len(yaml.safe_load(open('references/npc_registry.yaml'))['characters']))"` → `46` at
`1a52ac6`).

**Keys.** Attributes: the ten of `references/descriptor_registry.yaml: attributes` — `attr.body.strength`,
`attr.body.endurance`, `attr.body.agility` (Coordination), `attr.mind.focus`, `attr.mind.acuity` (Reason),
`attr.mind.perception`, `attr.spirit.will` (Spirit; NOT the legacy `attr.mind.will`), `attr.social.attunement`,
`attr.social.charisma` (Presence), `attr.social.grace`. Below they are written by their last segment (`acuity`, `will`,
`charisma` …); BA1 writes them under `stats:` by any spelling `substrate.descriptors.attribute_key` resolves. Skills: the
five above, scale `[0, 7]`, whole numbers (`cast.py::capabilities_of` refuses anything else).

**The magnitude rule (one rule, so Jordan corrects one line, not 46 rows) `[ASSUMPTION: no registry field states a
magnitude; the rule is this draft's]`.** Attributes (scale 1–7): the attribute the basis names as the person's trade = **5**;
one it names as secondary = **4**; every other key is LEFT OUT of `stats:` (ABSENT, `cast.py::attributes_of` — never the
registry default) and reads the builder's flat seating. Skills (scale 0–7): the skill the role names as the person's
trade = **5**; a skill the role or a goal implies = **3**; every other skill is left out (`untrained: default`). An
authored score wins over a lifepath grant (`cast.py::capability_of` merges with the authored score winning).

**`manner:` — lands in BA1 after B10** (`IS-B2-CHAR-07` step 5 joins BA1). The three A-108 axes: `rigid_flexible`,
`grandiose_humble`, `deontological_instrumental`; bound ±0.15 (CL-PERSON v2 §2). The sign convention is CL-PERSON's and
not yet fixed, so a cell names the POLE and a magnitude (e.g. "rigid 0.10"); BA1 writes the signed value. An empty
manner is no offset (zero; the control of `IS-B2-CHAR-07`).

| id | person | `stats:` (attributes) | `capabilities:` (skills) | `manner:` (lands in BA1 after B10) | basis (registry) |
|---|---|---|---|---|---|
| NPC-001 | Edeyja | acuity 5, focus 5, endurance 4, attunement 3, charisma 3, grace 3 | `[NO BASIS IN THE TREE]` | rigid 0.10 | `stats:` AUTHORED (`cognition: 5` → acuity, `focus: 5`, `endurance: 4`; `attunement/presence/grace: 3–4` — a range, which `data/cast.py::attributes_of` reads as its lower bound (cast.py ~:338-362), so the engine reads 3 today and Jordan may correct it to 4); role "Warden-Chief" names no skill; manner: goals "Continue the work regardless of interference" |
| NPC-002 | Maret Uln | perception 5, attunement 4 | inquiry 5 | instrumental 0.10 | notes "Vaynard's intelligence operative. Thread-sensitive."; goals "Serve Varfell intelligence", "Privately sympathize with Restoration Movement" (the double game → instrumental); lifepath 3-VA1 holds no skill |
| NPC-003 | Yrsa Vossen | charisma 5, will 4 | argue 5 | `[NO BASIS IN THE TREE]` | role "RM Leader"; goals "Cultural restoration", "Equity and social contract" |
| NPC-004 | Sæmund Haelgrund | perception 5, will 4 | inquiry 5, argue 3, law 3 | rigid 0.15, deontological 0.10 | role "Field Inquisitor"; notes "Attributes Thread perception to investigative instinct … Savonarola archetype"; goals "Investigate heresy", "Enforce Church orthodoxy"; lifepath 3-CH5 holds `inquiry` |
| NPC-005 | Sigrid Torsvald | agility 5, perception 4 | arms 5, inquiry 3 | `[NO BASIS IN THE TREE]` | faction "Löwenritter (Riskbreakers)"; role "TS Riskbreaker (Covert)"; goals "Mission success" |
| NPC-006 | Halvar Brandt | strength 4, charisma 4 | arms 5 | `[NO BASIS IN THE TREE]` | faction "Löwenritter"; role "Officer (Lions' Table)"; goals "Strengthen peninsular defenses" |
| NPC-007 | Annika Feldhaus | charisma 5, acuity 4 | argue 5 | `[NO BASIS IN THE TREE]` | role "Guilds Representative"; goals "Maximize Guilds Wealth", "Protect artisan livelihoods" |
| NPC-008 | Peder Almstedt | focus 5, acuity 4 | law 5, copying 3 | rigid 0.15 | role "Ministry Bureaucrat (Chief Parliamentary Clerk)"; goals "Maintain procedural correctness", "Block radical action through procedure" |
| NPC-009 | Gerik Strand | acuity 5, grace 4 | law 3, argue 3 | instrumental 0.10 | role "Crown Minister (Lord Steward)"; goals "Efficient Crown administration", "Maintain personal indispensability" |
| NPC-010 | Dalla Virke | attunement 5, charisma 4 | argue 5 | `[NO BASIS IN THE TREE]` | role "Syndicate Broker"; goals "Maintain Virke trade network", "Protect personal trust relationships" |
| NPC-011 | Alexios Laskaris | grace 5, charisma 4 | argue 3, law 3 | flexible 0.10 | role "Doux (Altonian Prince)"; goals "Maintain province stability", "Sandbag imperial directives" (bends the order he is given → flexible) |
| NPC-012 | Rikard Solberg | acuity 4, attunement 4 | argue 3 | `[NO BASIS IN THE TREE]` | role "Schoenland Factor"; goals "Maintain stable trade", "Avoid escalation" |
| NPC-013 | Aldric Tormann | acuity 5, will 4 | law 3, argue 3 | instrumental 0.10 | role "Fourth Cardinal (Prudence)"; goals "Maximize Church Wealth throughput", "Aggressive tithe collection" |
| NPC-020 | Almud Almqvist | charisma 5, will 4 | argue 3 | `[NO BASIS IN THE TREE]` | role "King"; no goals; notes name the TS and the honour template only (skills beyond argue: `[NO BASIS IN THE TREE]`) |
| NPC-021 | Arne Himlensendt | will 5, charisma 4 | argue 3 | `[NO BASIS IN THE TREE]` | role "Confessor (Church Leader)"; convictions doctrine 0.50 |
| NPC-030 | Elske Almqvist | `[NO BASIS IN THE TREE]` | `[NO BASIS IN THE TREE]` | `[NO BASIS IN THE TREE]` | role "Princess (married to Doux Alexios Laskaris)" names no trade; notes are about Alexios's behaviour |
| NPC-031 | Torben Almqvist | `[NO BASIS IN THE TREE]` | `[NO BASIS IN THE TREE]` | `[NO BASIS IN THE TREE]` | role "Prince (Heir Apparent)"; notes "Convictions intentionally undefined at game start — emerge during play" (the draft reads this as: author nothing) |
| NPC-032 | Lenneth Almqvist | acuity 5, focus 4 | inquiry 5, copying 3, law 3 | `[NO BASIS IN THE TREE]` | notes "Archivist by training"; goals "Caste dismantlement through royal decree" (law) |
| NPC-033 | Kolbrun Thale | perception 5, attunement 4 | inquiry 5 | `[NO BASIS IN THE TREE]` | role "Spymaster"; faction "Crown (Inner Circle)" |
| NPC-034 | Gustav Linder | grace 4, attunement 4 | argue 3, inquiry 3 | `[NO BASIS IN THE TREE]` | role "Archbishop's Representative / Father"; faction "Church (dual-loyalty: Crown Inner Circle agent for Himlensendt)" |
| NPC-035 | Theodor Kreutz | agility 5, strength 4 | arms 5 | `[NO BASIS IN THE TREE]` | role "Royal Guard Captain"; faction "… Löwenritter Liaison" |
| NPC-036 | Wilhelm Voss | acuity 4, charisma 4 | arms 3 | `[NO BASIS IN THE TREE]` | role "Royal Marshal" |
| NPC-037 | Annalie Reichard | acuity 5, focus 4 | inquiry 3 | `[NO BASIS IN THE TREE]` | role "Lord Treasurer" (the accounts are records → inquiry) |
| NPC-038 | Arnlod Olafsson | will 5, acuity 4 | law 5, inquiry 3 | `[NO BASIS IN THE TREE]` | role "Cardinal Justice (oversees Inquisition)"; notes "Cardinal Justice. Per Jordan 2026-05-08." |
| NPC-039 | Magnus Klapp | acuity 4 | inquiry 3, arms 3 | `[NO BASIS IN THE TREE]` | convictions scholastics 0.35 (inquiry); notes "Klapp Combat, Klapp Thread" arcs (arms) `[ASSUMPTION: an arc named for his combat implies he fights]` |
| NPC-040 | Osten Jarnstal | will 4 | `[NO BASIS IN THE TREE]` | `[NO BASIS IN THE TREE]` | role "Cardinal (Fortitude candidate)" (Fortitude → will, thin) |
| NPC-041 | Aldric Hann | charisma 5 | argue 5 | `[NO BASIS IN THE TREE]` | role "RM Visible Leadership (alongside Yrsa Vossen)" |
| NPC-050 | Inge Baralta | charisma 5, acuity 4 | law 5, argue 3 | `[NO BASIS IN THE TREE]` | role "Duchess (Sovereign Authority claimant …)"; goals "Sovereign Authority Doctrine", "Constitutional framework supersedes Church jurisdiction", "Hafenmark parliamentary sovereignty" |
| NPC-052 | Magnus Vaynard | charisma 5, acuity 5 | inquiry 3 | instrumental 0.15, grandiose 0.10 | role "Duke (Varfell Leader)"; goals "Einhir cultural revival at any cost" (instrumental), "Intelligence-first approach to RM" (inquiry); notes "Reinhardt von Lohengramm archetype per Jordan" (grandiose) |
| NPC-070 | Lisbeth Ehrenwall | will 5, charisma 4 | arms 5 | `[NO BASIS IN THE TREE]` | faction "Löwenritter"; role "Grandmaster"; resonant_style Consequence (a trait, B04.07; not an attribute or skill) |
| NPC-071 | Torvi Heljason | acuity 5, focus 4 | law 5, argue 3 | `[NO BASIS IN THE TREE]` | role "Legal Advisor to Baralta"; resonant_style Evidence |
| NPC-072 | Olaf Geirson | endurance 4, charisma 4 | arms 5 | `[NO BASIS IN THE TREE]` | role "Military Commander" |
| NPC-073 | Björn Holdar | `[NO BASIS IN THE TREE]` | `[NO BASIS IN THE TREE]` | `[NO BASIS IN THE TREE]` | role "Senior Jarl of the Western Highlands" names rank, not a trade; convictions stewardship 0.70 is a pursuit |
| NPC-074 | Ingrid Stenskald | charisma 5 | argue 3, copying 3 | `[NO BASIS IN THE TREE]` | role "Skald-Chief" (a skald carries a text on as given → copying; recites to a hall → argue `[ASSUMPTION]`); convictions community 0.70 |
| NPC-075 | Orm | focus 5 | `[NO BASIS IN THE TREE]` | rigid 0.10 | role "Second Senior Warden"; goals "The work. Only the work." |
| NPC-080 | Vidar Haldorsen | agility 5 | arms 5 | rigid 0.10, deontological 0.10 | faction "Löwenritter (Riskbreakers)"; role "Riskbreaker (doctrine-following — foil to Torsvald)"; resonant_style Authority; lifepath 3-LO3 holds no skill |
| NPC-081 | Uta Falkenrath | charisma 4 | argue 3, arms 3 | `[NO BASIS IN THE TREE]` | role "Commune Representative (Banneret)" (representative → argue; banneret leads a banner → arms) |
| NPC-082 | Njal Torberg | strength 4 | arms 5 | `[NO BASIS IN THE TREE]` | role "Military Jarl" |
| NPC-083 | Hedda Kronvald | acuity 4, focus 4 | law 3 | `[NO BASIS IN THE TREE]` | role "Governor of Ehrenfeld (T14)"; convictions stability 0.80 |
| NPC-084 | Frieda Kessler | charisma 4 | argue 3 | `[NO BASIS IN THE TREE]` | role "Zunftmeisterin (Guildmaster Council)" |
| NPC-085 | Nessa Grindvold | acuity 5, charisma 4 | law 5, argue 5 | `[NO BASIS IN THE TREE]` | role "Guild Advocate (legal representative at Crown court)"; resonant_style Evidence |
| NPC-086 | Joren Bergvall | perception 5, focus 4 | inquiry 5 | `[NO BASIS IN THE TREE]` | role "Guild Surveyor (mapping maritime Forgetting boundary)"; convictions scholastics 0.60 |
| NPC-087 | Uwe Askeland | acuity 4, charisma 4 | argue 3 | `[NO BASIS IN THE TREE]` | role "Buditel (hedge school teacher)" |
| NPC-088 | Carin Vedel | focus 5, agility 4 | copying 5, inquiry 3 | `[NO BASIS IN THE TREE]` | role "Copyist (hand-copies suppressed Einhir cultural texts)" (agility's gloss: "a steady hand"); lifepath 3-CF4 holds `inquiry` (authored 3 wins over the lifepath's `pool_default`) |
| NPC-089 | Zoe Palaiologina | acuity 4, charisma 4 | law 3, arms 3 | `[NO BASIS IN THE TREE]` | role "Katepano (frontier governor)" (governs → law; a katepano holds a military command → arms `[ASSUMPTION]`) |
| NPC-090 | Stephanos Doukas | acuity 4, focus 4 | law 3, inquiry 3 | `[NO BASIS IN THE TREE]` | role "Kommerkiarios (trade prefect at Schoenland interface)" (customs → law, inspection of goods → inquiry) |

**Note on `resonant_style`.** It seats a TRAIT (`moved_by_*`, B04.07), which is no attribute and no skill; table (a)
reads it for no value. V2 cut `moved_by` as what an argument works on (part 4 §G, "Cuts that stand": "`moved_by`,
the `read:` cells, `fit_body`, `misfit_level`"), so no cell of this draft reads a trait for a social roll; the trait
rows themselves stand as B04.07 landed them.

---

**Basis for (b)–(e).** These cells are not per person; each row's basis is the source proposal's cell (named per table,
paths relative to `proposals/2026-11-12-subsystem-audit-suite/`) or a tree owner it cites, and a `registry` column
carries the `references/npc_registry.yaml` evidence where a person bears on the row. A cell with neither is
`[NO BASIS IN THE TREE]`.

### (b) Per verb: `difficulty:` where it is not `routine`

**Source:** `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` Batch U1-C item 2 ("per-verb `difficulty:` levels beyond
`routine` (Jordan's), starting with OBS §4 step 5's `interrogate: demanding`"). The levels are the closed roster
`plain, routine, demanding, hard` (`unified/U1_OWNERS_AND_VOCABULARY.md` R-17; B05.14 lands the column and the roster,
B05.23 the half-step sizes). The rows are the ten rolled rows of `engine/season/rosters.yaml: task_difficulty` (the
same ten B05.14 names). Only `interrogate` takes a level beyond `routine`; the rest are listed so the roster is seen
whole. **Row count: 10.**

| verb | `difficulty:` | basis |
|---|---|---|
| `interrogate` | **demanding** | U1-C item 2; OBS §4 step 5; plan B05.23 (T13 T1: "`interrogate` → `demanding`"). V2 keeps it a verb that opens the full form (`questioning`, V2 part 2 §M; part 4 §H item 4), whose close reads `rite.difficulty` (part 2 §B, §D): when B24p.23 re-points the influence verbs, this level is the `questioning` row's cell `[ASSUMPTION: the level carries over unchanged]` |
| `lie` | `[SUPERSEDED BY V2]` | V2 part 2 §M: "A `lie` is an `argue` whose item is the liar's own false word or forgery"; the detection draw and `deceive` are cut (part 4 §G). A lie's own difficulty (`task_difficulty`'s note: "a lie against a truth") priced the cut mechanism |
| `determine` | `[SUPERSEDED BY V2]` | V2 part 2 §D: the close draws `pool_of(mid)` against `rite.difficulty + rite.gravity`; the adjudicator rolls no skill (B04.18: `law`'s gloss loses "a judge's skill"). A per-verb difficulty on the judge's roll prices the replaced mechanism |
| `argue` | routine `[NO BASIS IN THE TREE]` for any other level | B05.14's control (every rolled row `routine`); `task_difficulty`'s note: "the differences between tasks … are Jordan's to author" — no cell names one |
| `tell` | routine `[NO BASIS IN THE TREE]` for any other level | as `argue`; V2 part 2 §M: the abridged form |
| `speak` | routine `[NO BASIS IN THE TREE]` for any other level | as `tell` |
| `arrest` | routine `[NO BASIS IN THE TREE]` for any other level | B05.14's control; whether `arrest` rolls standing or body is the verb-governing-attributes proposal's §6 Q1, answered at B05 |
| `examine` | routine | plan B05.23, T13 edit 7: "the inquiries stay `routine`" |
| `research` | routine | as `examine` |
| `surveil` | routine | as `examine` |

### (c) The alignment cells of `02_CHAR_choice_alignment` and the pursuit-signature cells of `16_PESSIMIST_CHAR_B`

#### (c.1) Alignment cells on `choice_sourced` values

**Source:** `proposals/02_CHAR_choice_alignment.md` "The resolution, decided" (the `choices:` block under
`tables.alignment`; its two keys' cells are "illustrative; the cells are Jordan's"). The keys and values are the tree's:
`engine/season/data/verbs.py::CHOICE_RANGES` at `1a52ac6` — `role` (15), `retreat_at` (`none`, `0.5`, `0.25`),
`posture` (`storm`). Axes are `references/descriptor_registry.yaml: axis_roster` (seven; −1 the first-named pole, +1
the second). The source's `never`/`early` are mapped to the tree's `none`/`0.5` `[ASSUMPTION: "never" is `none`;
"early" is the earliest threshold, `0.5`]`. No cast row bears on a choice value (the `registry` evidence is absent by
construction, not missing). **Row count: 22 rows (23 cells if `calm` / `press` counts twice).**

| key | value | cells | basis |
|---|---|---|---|
| `retreat_at` | `none` | `rigid_flexible: -0.4, grandiose_humble: -0.3` | source cell `never` (illustrative) |
| `retreat_at` | `0.5` | `rigid_flexible: +0.3, selfish_selfless: -0.2` | source cell `early` (illustrative) |
| `retreat_at` | `0.25` | `[NO BASIS IN THE TREE]` | the source names two values; the tree has three |
| `role` | `ShieldWall` | `[NO BASIS IN THE TREE]` | the source authors no `role` cell |
| `role` | `Hold` | `[NO BASIS IN THE TREE]` | as above |
| `role` | `Anvil` | `[NO BASIS IN THE TREE]` | as above |
| `role` | `Push` | `[NO BASIS IN THE TREE]` | as above |
| `role` | `Skirmish` | `[NO BASIS IN THE TREE]` | as above |
| `role` | `Screen` | `[NO BASIS IN THE TREE]` | as above |
| `role` | `Pursue` | `[NO BASIS IN THE TREE]` | as above |
| `role` | `Shock` | `[NO BASIS IN THE TREE]` | as above |
| `role` | `Flanker` | `[NO BASIS IN THE TREE]` | as above |
| `role` | `Feint` | `[NO BASIS IN THE TREE]` | as above |
| `role` | `VolleyLine` | `[NO BASIS IN THE TREE]` | as above |
| `role` | `Harass` | `[NO BASIS IN THE TREE]` | as above |
| `role` | `Kite` | `[NO BASIS IN THE TREE]` | as above |
| `role` | `Support` | `[NO BASIS IN THE TREE]` | as above |
| `role` | `Reserve` | `[NO BASIS IN THE TREE]` | as above |
| `posture` | `storm` | `[NO BASIS IN THE TREE]` | the source names `march`'s `posture` and authors no cell |
| `approach` | `aggressive` | `grandiose_humble: -0.4` | source cell (illustrative). ⚠ the key is NOT on the tree: `modules/combat/vocabulary.py` defines no `APPROACHES` at `1a52ac6`, and the loader refuses a key that is not `choice_sourced`; the cell waits on the PC lane's key |
| `approach` | `defensive` | `grandiose_humble: +0.3` | as above |
| `questioning` | `calm` / `press` | `[SUPERSEDED BY V2]` | the source's "LACUNA's `calm`/`press` is the separate key `questioning`": V2 makes `questioning` a proceeding row whose moves are `argue`, `press`, `rest`, `concede` (V2 part 2 §B; part 4 §H items 2, 4) — no `calm`/`press` choice key remains |

#### (c.2) Pursuit signatures

**Source:** `proposals/16_PESSIMIST_CHAR_B_a_pursuit_does_what_its_name_says.md` "Step 1" (`pursuit_signatures`, every
row `[ASSUMPTION; medium; Jordan to correct]`). Every verb named is a row of `VERB_TABLE` at `1a52ac6` (67 rows; checked
by import, none absent — the source's "twelve signatures name a verb with no row" is stale). The `registry` column is
the cast rows whose heaviest `convictions` weight is that pursuit (computed from `references/npc_registry.yaml`). No
signature verb rests on a mechanism V2 replaced: `lie`, `determine` and `speak` remain verbs (V2 part 2 §M). **Row
count: 15.**

| pursuit | favours | opposes | basis (source) | registry (holds it first) |
|---|---|---|---|---|
| `love` | give, tend, forgive | sabotage, raze, forge | source row | none |
| `justice` | open_case, determine, petition | forge, lie, conceal | source row | NPC-002, -003, -032, -041, -052 |
| `family` | give, tend, succeed | migrate, sabotage | source row | NPC-030, -031 |
| `wealth` | exchange, work, requisition | give, raze | source row | NPC-007, -010, -012 |
| `reputation` | challenge, speak, utter | conceal, evade / defy | source row | none |
| `scholastics` | research, examine, reconstruct | destroy_record, raze | source row | NPC-039, -086 |
| `community` | build, found, convene | raze, migrate | source row | NPC-074, -081, -082, -084, -087 |
| `stewardship` | build, restore, work | raze, sabotage | source row | NPC-001, -005, -073, -075 |
| `honour` | challenge, accept, commit | lie, forge, evade / defy | source row | NPC-006, -080 |
| `liberty` | evade / defy, release, migrate | comply, arrest, capture | source row | NPC-033, -085, -088 |
| `stability` | restore, comply, create_record | raze, evade / defy | source row | NPC-008, -009, -013, -035, -036, -037, -050, -070, -071, -072, -083, -089, -090 |
| `virtue` | give, forgive, pardon | lie, forge, sabotage | source row | NPC-011, -020 |
| `doctrine` | utter, commit, oblige | forge, destroy_record | source row | NPC-004, -021, -034, -038, -040 |
| `happiness` | give, release, tend | fight, arrest | source row | none |
| `individuality` | evade / defy, found, migrate | comply, oblige | source row | none (NPC-052 holds it second, 0.30) |

### (d) The six relation rows of `02_CHAR_relations_have_a_ground`

**Source:** `proposals/02_CHAR_relations_have_a_ground.md` "Exact edits" item 6 (each `[ASSUMPTION; low]`; "the
numbers are placeholders" and the source states none). Shape per its item 2: `relations: - {to, ground, valence,
weight}` on the holder's row; `ground` ∈ `kin, oath, service, patronage, rivalry, feud`. **The weight rule (this
draft's) `[ASSUMPTION]`:** the stance row's own unit, as the loyalty row's (`data/cast.py::stance_from_loyalty`, 1–5,
under `STANCE_MAX`): **4** where the source's words are absolute (a household; "The enemy"), **3** otherwise. **Row
count: 6.**

| holder | `to` | ground | valence | weight | basis (source) | registry |
|---|---|---|---|---|---|---|
| NPC-020 Almud | NPC-032 | kin | +1 | 4 | *"share a household, a family"* | NPC-032 role "Queen (Widow Regent if Almud eliminated)" |
| NPC-032 Lenneth | NPC-020 | kin | +1 | 4 | the same; "her frustration is a deed judgement, not a stance" | NPC-032 role, as above |
| NPC-050 Baralta | NPC-020 | rivalry | −1 | 3 | *"the other wants the other's job"* | NPC-050 role "Duchess (Sovereign Authority claimant, Custodian/Claimant foil with Almud)" |
| NPC-020 Almud | NPC-050 | rivalry | −1 | 3 | *"a rival whose case is strong"* | NPC-050 role, as above |
| NPC-070 Ehrenwall | NPC-020 | service | +1 | 3 | "the Löwenritter's oath to the Crown; the count is hers to keep" | `[NO BASIS IN THE TREE]`: NPC-070's row (faction "Löwenritter", role "Grandmaster") names no oath to the Crown |
| NPC-052 Vaynard | NPC-050 | rivalry | −1 | 4 | *"The enemy"* (and the foil table's "Total Opposition") | `[NO BASIS IN THE TREE]`: neither row names the other (NPC-052 goals "Dismantle post-war caste order"; NPC-050 goals "Hafenmark parliamentary sovereignty") |

### (e) The signature rows and goals of `U5a_CHAR_owed_amendments` §7 and §10

#### (e.1) §7 — `affiliation_signatures`

**Source:** `proposals/U5a_CHAR_owed_amendments.md` §7 ("one row per member of `affiliation_roster`, `{favours: [...],
opposes: [...]}` … Content is Jordan's (`[ASSUMPTION; low]` rows may be proposed by the CHAR content pass)"); its gate:
"each creed's violating set differs from at least one other creed's". The members are the five of
`references/descriptor_registry.yaml: affiliation_roster`. The tree's own per-creed cells are
`engine/season/rosters.yaml: tables.affiliation_engagement` (`thread_read` only); its R-C4.3 rules that
`create_record` and `destroy_record` engage a creed by WHAT is recorded, which is no cell, so no row here names them.
**Row count: 5.**

| affiliation | favours | opposes | basis | registry (holds it at 4–5) |
|---|---|---|---|---|
| `solmund_orthodoxy` | open_case, examine | thread_read | opposes: the tree cell `solmund_orthodoxy.thread_read: -1`; favours: NPC-004 goals "Investigate heresy", "Enforce Church orthodoxy", NPC-038 role "Cardinal Justice (oversees Inquisition)" | NPC-004, -021, -034, -038, -039, -040 |
| `inner_tradition` | thread_read | `[NO BASIS IN THE TREE]` | favours: the tree cell `inner_tradition.thread_read: 1` | NPC-001 |
| `thread_truth` | thread_read | `[NO BASIS IN THE TREE]` | favours: the tree cell `thread_truth.thread_read: 1`; NPC-001, NPC-075 hold it and their goals ("Maintain substrate stability"; "The work. Only the work.") name no verb | NPC-001, -075 |
| `einhir_restoration` | reconstruct | `[NO BASIS IN THE TREE]` | favours: NPC-088 role "Copyist (hand-copies suppressed Einhir cultural texts)", NPC-003 goals "Cultural restoration", NPC-032 goals "Einhir revival through Crown authority" `[ASSUMPTION: `reconstruct` is the act of restoring a lost record]`; opposes: the natural cell (`destroy_record`) is content-keyed and no cell by the tree's R-C4.3 | NPC-002, -003, -032, -041, -052, -073, -074, -082, -087, -088 |
| `altonian_civics` | `[NO BASIS IN THE TREE]` | `[NO BASIS IN THE TREE]` | NPC-089 role "Katepano (frontier governor)" and NPC-090 role "Kommerkiarios (trade prefect …)" name offices, not acts | NPC-089, -090 |

⚠ As drafted, `inner_tradition` and `thread_truth` share their favours and both have an empty opposes, so §7's gate
(each violating set differs from another's) does not yet hold for those two; the cells that would separate them are
Jordan's.

#### (e.2) §10 — two cast rows gain goals

**Source:** `proposals/U5a_CHAR_owed_amendments.md` §10 ("rows NPC-034 and NPC-071: author `goals:`"; gate: "`data/cast.py`
loads; the two persons hold a live `commit` at build"). The form is the registry's own (a list of short sentences, as
the 17 rows with a non-null `goals:` at `1a52ac6`). **Row count: 2.**

| id | person | `goals:` | basis (registry) |
|---|---|---|---|
| NPC-034 | Gustav Linder | "Carry the Crown Inner Circle's counsel to Himlensendt"; "Hold the Church's place at court" | faction "Church (dual-loyalty: Crown Inner Circle agent for Himlensendt)"; role "Archbishop's Representative / Father"; `arc_trajectory` "Himlensendt's agent inside Crown Inner Circle" (that key left the registry at B04.12; the sentence is now a comment in the NPC-034 case file); convictions doctrine 0.60 |
| NPC-071 | Torvi Heljason | "Ground the Duchess's Sovereign Authority claim in law"; "Keep Hafenmark's procedure correct" | role "Legal Advisor to Baralta"; NPC-050 goals "Sovereign Authority Doctrine", "Constitutional framework supersedes Church jurisdiction"; `cultural_label` hafenmark_procedural (that key left the registry at B04.12); convictions stability 0.40, scholastics 0.30 |

Whether a free-sentence `goals:` entry mints a live `commit` at build (§10's gate) is read by BA1 on landing, not here.
