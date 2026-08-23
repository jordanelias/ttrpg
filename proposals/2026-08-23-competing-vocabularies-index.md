# Competing Vocabularies — the index, and what each conflict costs the fiction

## Status: FINDINGS — an index and analysis. Nothing here rules anything. No `.py` touched, no registry edited. Content/design only; another session owns the restructure.

**Date:** 2026-08-23 · **Method:** six producer sweeps (three narrative, three supplementary), one structurally read-only antagonist, and independent re-verification by parse or execution of every load-bearing claim. Grep located lines; **reading and parsing established every finding**, per Jordan's standing constraint this session.

**What this document is.** Jordan asked for every site where the repo carries **conflicting, duplicated, competing or overlapping frameworks** — *"like multiple convictions"* — for the things that determine narrative quality: world, factions, settlements, NPCs. §1 is the index. §3 onward flattens and analyses by topic.

**Four kinds, because they need different remedies:**

| | Meaning | Remedy shape |
|---|---|---|
| **CONFLICT** | two surfaces state incompatible things about one referent; both cannot be right | a ruling |
| **DUPLICATION** | the same thing stated twice, consistently *so far* | an owner + a guard |
| **COMPETITION** | two frameworks claim the same job; a caller must choose | a scoping decision |
| **OVERLAP** | partial intersection; each captures something the other does not | a named boundary, not a merge |

**⚠ Read §2 before acting on any single row.** Three root causes generate most of this index, and fixing them is cheaper than fixing the symptoms one at a time.

**⚠ And read §11 before treating any row as new.** The antagonist established that **seven of the flagship findings are already registered as prioritised open work** — one of them is `HANDOFF_IN.md`'s Tier-0 next action. This session has already been caught once presenting tracked defects as discoveries; §11 marks every row honestly.

---

## §1 THE INDEX

**Legend.** **Live?** = does running code hit it today. **Guarded?** = does any tool or test fail on it. **Tracked?** = already registered as open work before this sweep. **Verified** = re-established by me personally, by reading, parsing or execution.

### Person texture

| # | Site | Kind | Surfaces | Authoritative? | Guarded? | Live? | Tracked? |
|---|---|---|---|---|---|---|---|
| **P1** | **Conviction rosters — 13 / 9 / 8 / 7 / 7** | CONFLICT | **5 rosters, 12 homes**, union 21 names, intersection **{Faith, Order}** | 13 ruled (PP-684); the 8 never superseded | **NO** | **yes** | partly (J-C) |
| **P2** | **7 of 13 canonical Convictions cannot be Scarred** | CONFLICT | `conviction.py:46-49` vs the canonical 13 | 13 | **NO** — green blind test | **yes** ✅**verified by execution** | **yes — T0-1** |
| **P3** | `knots.py` scars `'Loyalty'`, a member of no roster | CONFLICT | `knots.py:349-353` → `conviction.py:191-193` | unresolved | test asserts intent flag, not effect | latent | **yes — T0-1** |
| **P4** | `conviction.py`'s comment says "canonical 13" over the legacy 9 | CONFLICT (self) | `:42-49` | 13 | NO | yes | yes |
| **P5** | **Resonant Style / Pressure Point — `Solidarity` vs `Loyalty`** | CONFLICT | 4 surfaces, differing on **one member** | rename ruled 2026-05-08, **reversed 2026-07-21** | NO | yes | no |
| **P6** | **The prescribed fix for the `Authority` collision collides too** | CONFLICT | `name_collision_database:421-425` prescribes **Sanction**; `faction_layer_v30.md:455-461` is a live 5-tier **Parliamentary Sanction** ladder | — | NO | latent | **no — new** |
| **P7** | `resonance_style` DEPRECATED on a premise the same entry records as FALSE | CONFLICT | `descriptor_registry.yaml:177` | NEEDS-JORDAN since 2026-07-07 | NO | 18 NPCs + a UI enum carry values | yes |
| **P8** | `armature_position` names two incompatible 4-vectors | CONFLICT | basis α (conviction projection) vs basis β (adjudicator) | both ratified, unreconciled | glossary flags, report-only | β live | **yes — ED-IN-0073 L2** |
| **P9** | Three surfaces assign **different convictions to the same NPC** | CONFLICT | registry vs `npc_behavior §2` vs migration roster | D1 ruled, doc unratified | NO | latent | **yes — L3/L4** |
| **P10** | `alias_registry` lists **5 canonical Convictions as deprecated legacy** | CONFLICT | `:648-663` vs `conviction_taxonomy:274-281` | taxonomy | NO — regenerated + gate-excluded | ships to dashboard | **no — new** |
| **P11** | **PP-684 mis-superseded Ethical Framework**, an orthogonal axis | CONFLICT | *what you value* vs *what your institution rewards* | D2 ignores the supersession | NO | latent | no |
| **P12** | "Conviction" also names a per-territory 0–5 Piety stat | CONFLICT | `conviction_track_v30.md:24-26`; ED-644 rename **ran on itself** | rename deferred | NO | yes | yes |
| **P13** | "Truth" — a Conviction, a 0–5 axis, and `certainty` in code | CONFLICT + DUPLICATION | 5 surfaces | ED-IN-0075; sweep staged not executed | NO | yes | yes |
| **P14** | "Loyalty" — conviction / 0–3 scalar / pressure point (+2 weaker senses) | CONFLICT | 3 solid | unresolved | NO | yes | no |
| **P15** | Player Conviction vs NPC Conviction — a unification claim PP-684 broke | CONFLICT | `player_agency_v30.md:71` | both CANONICAL | NO | latent | no |
| **P16** | Cultural templates — `altonian_imperial` **sums to 0.35, not 1.0**, and sits below the file's own "End spec" | CONFLICT | `conviction_taxonomy §5.1` | §5.1 | NO | latent | no |
| **P17** | `cultural_label` etc. stored at **two nesting levels** in one registry | DUPLICATION | 26 nested / 17 top-level | — | NO | blocks any loader | **no — new** |
| **P18** | **Goldenfurt's person schema shares no field with the registry** | COMPETITION | `ethic α/β · ambition · leverage{wants,fears,secret}` | PROPOSAL | NO | latent | no |
| **P19** | Belief — 4 rival models; the registry has **no `beliefs` field at all** | COMPETITION | `beliefs.py` / prose tables / a Key type / the PROPOSED Proposition | proposal unbuilt | NO | 2 live, incompatible | partly |
| **P20** | Attribute roster — 9 vs 7 vs 4, count ruled at **10**, tenth unnamed | CONFLICT | `descriptor_registry` vs `vocab_source` vs `npc_registry` | count ruled 2026-08-14 | partial | yes | yes |
| **P21** | Arcs — prose blurb / boolean / lettered branches / stage ladder | COMPETITION | 4+ | unresolved | NO | latent | no |
| — | *Negative:* **TS is not a homonym**; **Coherence is one consistent axis** | — | — | — | — | — | *reported as clean* |

### Place and polity

| # | Site | Kind | Surfaces | Authoritative? | Guarded? | Live? | Tracked? |
|---|---|---|---|---|---|---|---|
| **L1** | **"Territory" means 17 things, 37 things, or a new tier** | CONFLICT | `scale_hierarchy_v1` (RATIFIED) vs PP-726 vs `settlement_layer §1.1` vs code | **ruled, unexecuted** | NO | yes | yes (§6.1) |
| **L2** | **T16 is authored, described, tempered — and not in the world** | CONFLICT | geography 17 vs `game_state` 16 | unresolved | NO | **yes** ✅**verified: S-037 orphaned** | no |
| **L3** | `game_state.py` carries **two territory sets** (15 and 16) in one file | CONFLICT | `ALL_PLAYABLE_15` vs `STARTING_OWNER` | — | NO | yes | **no — new** |
| **L4** | Accord — 0–3 named bands / 0–4 map / 0–5 derived / continuous 0.5–7.0 | CONFLICT | 4 | D4 endorses one, ignores range | NO | yes; **T9 yields Accord 5, outside every vocabulary** | partly |
| **L5** | Prosperity — 0–5 / 1–7 / 1–2 / 0–6 / 0–10 | CONFLICT | 5 | flagged, unreconciled | NO | yes | partly |
| **L6** | **Settlement types — 8 / 11 / 9 / 7 realized** | CONFLICT | §1.2 vs `LEGAL_TYPES` vs §1.8 vs the map | fix authored, unratified | `LEGAL_TYPES` raises | **yes** ✅**verified: Village 14, absent from 3 tables** | yes |
| **L7** | **Ledger tag families — 5 rival lists**, union 11, intersection 4 | CONFLICT | code / Goldenfurt / §1.6 / §9 / the deck | **D3 RATIFIED, unpropagated** | NO | yes | partly |
| **L8** | Reputation single-valued on the settlement; the deck writes it onto NPCs | CONFLICT | `ledger.py:50-52` vs deck | — | NO | **silently erases** | no |
| **L9** | `religious_building` stored twice, in two keyspaces, never synced | CONFLICT | `registry.py:82` (sid) vs `infrastructure.py:81` (territory) | canon says settlement; code is territory | NO | yes | no |
| **L10** | Settlement state — 25 code fields vs 3 canonical stats vs 9 vs 6 registered | COMPETITION | 8 surfaces | partial | 6 of 25 registered | yes | no |
| **L11** | AP — three bonus lists; and "AP" also means **Church Attention Pool** | CONFLICT | governance vs `registry.py:92-97` vs clock registry | D2 partial | NO | yes | no |
| **L12** | **Goldenfurt's authored numbers are not loadable** | CONFLICT | spec literals vs `populate_from_geography` | code | NO | **the slice's own vise is off by a third** | no |
| **L13** | **Niflhel struck by CANONICAL Jordan approval, alive in 9 files** | CONFLICT | `conflict_architecture_proposal.md:103-115` | **ruled** | NO | yes | no |
| **L14** | Local Actors — table sums to 25 across 21 of 37 settlements | CONFLICT | §4.5 | unresolved | NO | latent | no |
| **L15** | Faction stats — canon 6-stat vs code's `L/Sta/W/I/Mil`, **`L` doing Mandate's job** | CONFLICT | 6 surfaces | canon ruled; code self-documents the gap | NO | yes; **Mandate computes 0 for every faction** | yes |
| **L16** | Standing — 0–7 / 0–5 / 0–10 / untyped, with a −1 case | CONFLICT | 4 | unresolved | NO | yes | no |
| **L17** | **Part B of `faction_canon` has 2 sheets of ~8** | OVERLAP | — | PROVISIONAL+CANONICAL, both | NO | **5 polities have no voice** | no |
| **L18** | Faction actions — 4 rival verb rosters, **zero name overlap between the top two** | COMPETITION | 5 | home doc `doc: null` | NO | yes | yes (ED-FA-0002) |
| **L19** | 20 faction strings, 2 truncated by unquoted `#` | CONFLICT | `npc_registry.yaml:835,:850` | — | parse test can't see it | latent | yes |
| **L20** | `worldbuilding_v30 §9.1` lore-to-map — **not one row matches** | CONFLICT | vs live geography | geography | NO | latent | flagged in-file |
| **L21** | `settlement_layer` CANONICAL contradicts itself on S-003 / S-023-25 | CONFLICT | §1.4.4, §6.3 vs §2.1, §2.3 | PP-726 | NO | latent | no |
| **L22** | Public Temperament — **clean duplication**, one broken registry citation, one dead-read drift | DUPLICATION | doc ≡ code, verified | CANONICAL | NO | drift inert | no |

### Outcome, event, structure, voice

| # | Site | Kind | Surfaces | Authoritative? | Guarded? | Live? | Tracked? |
|---|---|---|---|---|---|---|---|
| **O1** | **37 distinct outcome/degree vocabularies** | CONFLICT + COMPETITION | see §7 | one owner, two declared holds | ladder **only**, Python-only | yes | partly |
| **O2** | **`key_type_registry` — 9 outcome vocabularies in one CANONICAL file** | CONFLICT | `:52 :198 :403 :568 :657 :845 :905 :942 :974` | CANONICAL | NO | yes | no |
| **O3** | `:942` puts **`graze` in the Failure slot** and calls it `degree` | CONFLICT | — | STUB | NO | latent | no |
| **O4** | **`graze` has four incompatible meanings** — and the Godot skeleton contains the collision internally | CONFLICT | `core.QUAL` / `PERC_QUAL` / `strike_module.gd` / `combat_config.gd` / the registry | none | NO | port-time | **no — new** |
| **O5** | `stalemate`, `rout`, `withdrawal` registered and **unwritable** | CONFLICT | registry vs `_OUTCOME_BY_DEGREE` | CANONICAL | NO | yes | no |
| **O6** | `da_outcome` is a **3-band** ladder — the strategic layer cannot express Overwhelming | CONFLICT | `:198` | CANONICAL | NO | yes | no |
| **O7** | Contest verdicts — **6 win-conditions, 5 verdict vocabularies**; `committee` cannot cross a scale boundary | COMPETITION | `resolver.py` | unresolved | NO | yes | yes (ED-SC-0015) |
| **O8** | **Scale rosters — 4 (enforced) / 5 (doc) / 6 (threadwork)** | CONFLICT | `keys.py:65` raises | substrate enforced | **raises** | **yes — a Foundational Weaving cannot emit a Key** ✅**verified** | no |
| **O9** | Knot Formation — **3 canonical tables**, 3 of 4 rows one band off | CONFLICT | §5.6a / §3.2 / socializing | ED-912 + the ladder ruling | NO | code current, all 3 tables stale | yes (S4/G3) |
| **O10** | Event cards — one family roster, **two irreconcilable schemas**; 58 of 86 cards have no `family:` field | COMPETITION | Goldenfurt vs grounded deck | both unratified | NO | latent | partly |
| **O11** | **Scripted hooks — six bespoke arming idioms, no framework** | COMPETITION | fuse / counter / condition table / CI curve / 2 deck forms | mixed | NO | latent | no |
| **O12** | **The Church-dominance threshold is 40 / 60 / 65 / 100** | CONFLICT | 4 surfaces | unresolved | NO | latent | no |
| **O13** | Contest venues — **21 venue-shaped objects across 4 disjoint rosters**; 9 carry "Jordan assigns Valorian names" | COMPETITION | `modes.py` | 8 canonical | NO | yes | partly |
| **O14** | **`alias_registry` ships phantom vocabulary**: `Past\|Present\|Future`, `AMPLIFY\|DIVERGE`, `Regular`, a 4-member Gap scale | CONFLICT | vs doc + code | doc + code | drift-**locked** by `--check` | **player-facing labels** ✅**verified** | **no — new** |
| **O15** | Threadwork opposing table promises a downgrade the fold **cannot perform** | CONFLICT | `opposing.py:159-224` | — | pinned as a fold | latent | no |
| **O16** | **Voice — two disjoint author frameworks; the CANONICAL one lists 8 of its claimed 12** | COMPETITION | canon 8 vs Solmund 21 vs skill 12 | canon claims exclusivity | NO | **no renderer cites any** | partly (gap 16) |
| **O17** | **The RATIFIED narrative engine cites the PROVISIONAL and the skill, not the CANONICAL** | CONFLICT | precedence inverted | — | NO | it is the plan of record | no |
| **O18** | **Truth-0 has no voice register**; §18 runs 1-2/3/4/5/6+ on a 0–5 track | CONFLICT | Solmund §18 vs `clock_registry:71` | ED-IN-0075 | NO | latent | no |
| **O19** | 4 code renderers, none citing any voice spec; 2 narrate the same stream in rival voices | COMPETITION | `narrate` / `commentary` / `Chronicle` / `dictionaries.flavor` | none | NO | the player-facing one is in an unnamed register | no |
| **O20** | Solmund corpus stored **5 times**; 2 Jordan-REJECTED sources still assigned | DUPLICATION + CONFLICT | master + 4 chunks | neither is head | NO | latent | no |
| **O21** | `SHAPES` — the tree's **only** dramatic-arc classifier, unregistered, bout-scale | OVERLAP | `narrative.py:25` | `[SEED]` | NO | yes | no |
| **O22** | Relationship models — 6 edge types / 2 Knot tiers / 11 free-text labels / a 7-value power_base | COMPETITION | 5 | graph PROVISIONAL | NO | latent | partly |
| **O23** | World tracks — **RS is a retired name on a live stub**; CI starts at 30 where canon says 28 | CONFLICT | `rs_track.py` vs ED-731; `game_state:247` vs `clock_registry:17` | rename registered | NO | yes | no |
| **O24** | Calamity type modifier names **3 settlements of the wrong type** and a type with 0 instances | CONFLICT | `calamity_radiation:24-29` | node map is clean | NO | latent | no |

### Supplement — machinery beneath the fiction

| # | Site | Kind | Note |
|---|---|---|---|
| **M1** | **`dice_engine.roll_pool` accepts `tn`, stores it, never reads it** | CONFLICT | ✅**verified by Monte Carlo**: 4.005 at TN 6/7/8, while `continuous_engine_sample` in the same module gives 5.005 / 3.980 / 3.004. **19 decorative `tn=` args; 3 live** — threadwork's TN-8 Lock/Dissolution and the whole v30 weapon-TN matrix are inert |
| **M2** | **The ratified ED-874 Domain Action resolver has zero implementations** | CONFLICT | Its own text: *"It supersedes the bare-stat-pool-vs-Ob dice approach."* Every faction action uses the superseded method |
| **M3** | Seven rival pool formulas, no owner function | CONFLICT + OVERLAP | `Pool.size` and `build_argue_pool` disagree **inside one package** |
| **M4** | Suppress obstacle — `Ob = M` vs `⌊M/2⌋+1`, diverging up to 3 points | CONFLICT | two ratified surfaces; implementer picked one in prose, implemented neither |
| **M5** | **Two mass-battle engines, ~40 shared function names, different architectures** | CONFLICT | Live tree lacks the σ head, the fractional pool, and PP-241 Reform (an empty `pass`). 40 of 51 tests target the tree that never runs |
| **M6** | **A fabricated path under `deprecated/` resolves FORKED and is tolerated** | CONFLICT | ✅**verified by probe.** The identical fabrication under `systems/` is blocked. A blocking gate, quietly widened |
| **M7** | **PP is FROZEN, and three live surfaces tell you to allocate the next one** | CONFLICT | ✅**verified.** Following CLAUDE.md §4's protocol turns a blocking gate red |
| **M8** | **23 of 30 "missing status" warnings are encoding artifacts** | CONFLICT | three rival `## Status:` encodings; ~35 values, two disjoint machine vocabularies |
| **M9** | `## Status: PROPOSAL DOCKET — awaits Jordan's explicit pick` classifies as **ratified** | CONFLICT | `"PROPOSED" in "PROPOSAL"` is False |
| **M10** | CLAUDE.md §1 tells every session to distrust a gate that measures **109/109 FRESH** | CONFLICT | §1 vs §8 |
| **M11** | §8's retirement list gives **twelve wrong locations** | CONFLICT | all twelve absent; `deprecated/engine/` does not exist |
| **M12** | `module_contracts.yaml` — 33 direct readers, no owner, one normalization written **five times** | DUPLICATION | `consumes[].from` is a list on most rows and a bare string on two |
| **M13** | Key-envelope construction hand-rolled **4 times**, two error policies, two counters never reset | DUPLICATION | — |
| **M14** | The contract spine and the Key registry **agree with each other and both disagree with the code** on who emits what | CONFLICT | 11 producer-set disagreements |

---

## §2 THE THREE ROOT CAUSES

Most of §1 is downstream of these. Fixing them is cheaper than fixing rows.

### §2.1 There is no roster primitive anywhere in the tree

Every registry maps **name → canonical string**. `names_index.yaml`, `descriptor_registry.yaml`, `proper_noun_registry.yaml`, `alias_registry.yaml` — all of them. **None can express "these thirteen and no others."**

That is why five conviction rosters coexist invisibly, why `ci_names_consistency` skips `conviction` and `pressure_point` by design, and why every membership conflict in §1 is unguarded. A registry that stores names cannot detect a set.

### §2.2 The naming gate enforces exactly one rule in the entire repository

I parsed it:

```
enforce tiers across 113 entries: {'warn': 112, 'block': 1}
conv.* tiers: all 7 -> 'warn'
```

`ci_naming_check` builds its forbidden set **only** from `enforce: block`. Exactly one entry qualifies — the canonical-name rule for the Solmund figure. **No conviction, no pressure point, no roster conflict, no phantom vocabulary could ever trip the naming gate**, regardless of which files are excluded from it.

*(Confirmed the hard way: the pre-commit guard rejected the first draft of this very document, on that one rule, in the sentence describing that it is the only rule.)*

This is more load-bearing than any individual row, and it is the one thing a remedy must change. The antagonist found it; I verified it.

### §2.3 The flagship subsystems have no currency row, so a supersession has nowhere to land

`CURRENT.md` carries 22 subsystem rows. **None is Convictions or Characters. There is no `systems/world/` row at all** — the entire 3,275-line world and Solmund corpus, including the voice canon, is invisible to the currency index a session is instructed to trust first.

CLAUDE.md §3 already knows: *"`characters/`/`overview/`/`victory/` are doc homes, **not yet formalized 1:1 subsystems** (no dedicated ID lane / `CURRENT.md` row / `HANDOFF_<LANE>.md` yet)."*

**So there is no surface on which "the 13 supersede the 9" can be recorded as current.** Four rosters have coexisted for 3.5 months with nothing empowered to adjudicate them. The consolidation doc written to fix exactly this — `character_canon_v30.md` — has been `PROVISIONAL — pending Jordan ratification` since May, with PART B never authored.

---

## §3 CONVICTIONS — five rosters, and the one that runs

**Every membership below was parsed or read, not grepped.**

| Roster | n | Members | Where it lives |
|---|---|---|---|
| **R1 — canonical** | **13** | Faith, Authority, Order, Scholastic, Utility, Equity, Liberty, Precedent, Community, Identity, Warden, Virtue, Honor | `conviction_taxonomy_v30.md:29-41`, the 13×4 axis matrix, **all 46 registry entries**, `npc_behavior §1.2`, `character_canon`, `faction_canon` role templates |
| **R2 — legacy 9** | 9 | R1's 6 shared + Reason, Autonomy, Continuity | `conviction_track_v1.md:20-28` — **and `conviction.py:46-49`, the live runtime gate** |
| **R3 — legacy 7** | 7 | R2 − {Community, Warden} | `conviction_track_v1.md:70` (the §3 matrix), **`references/names_index.yaml` — the live name registry** → `definitions.yaml` → `lexicon.json` → the dashboard |
| **R4 — NPE 8** | 8 | Faith, Order, Reason, Justice, Survival, Loyalty, Truth, Power | **`npe.py:80` — the live generator** + `investigation_systems_v30.md:84`, which asserts these *are* "the existing conviction taxonomy" |
| **R5 — "Seven Convictions"** | 7 | = R3 | `complete_systems_reference.md:23` — **and its supersession banner is scoped only to PART 2 combat**, so §1.1 stands as live canon |

**Union: 21 names. Present in all five: `Faith` and `Order`.**

| pair | ∩ |
|---|---|
| R1 ∩ R2 | 6 |
| R1 ∩ R3/R5 | 4 |
| **R1 ∩ R4** | **2** |

### §3.1 The cost, executed

```
SCARRABLE   : Faith, Order, Equity, Precedent, Community, Warden
SILENT NO-OP: Authority, Scholastic, Utility, Liberty, Identity, Virtue, Honor  (7 of 13)
Honor scar -> {'conviction': 'Honor', 'magnitude': 0}

named NPCs with authored primaries: 43
CANNOT be scarred on ANY primary : 12
```

`conviction.py:191-193` returns `magnitude=0` for any name outside its 9-tuple — no exception, no warning. **Conviction Scars are the only mechanism by which an NPC's value-frame destabilises, shifts weight, activates Resonant Style at Scar 2, or enters crisis at Scar 3+.**

> **So the cast is split along a line no designer chose.** Cardinal Reichard (Faith/Precedent) can have a crisis of faith. **Grandmaster Ehrenwall (Order 0.60, Liberty 0.20), Cesare (Authority/Utility) and Maret Uln (Honor/Authority/Identity) are inert.** Nothing that happens to them can move them, ever.

And the one production write path — `knots.py:349-353`, the ED-912 Close-Knot Scar — passes `'Loyalty'`, a member of **no** roster. It returns magnitude 0. The test asserts the intent flag set three lines earlier and never inspects the record, so it is green.

### §3.2 Two structural observations

**The registry is not the problem.** All 46 entries use R1 exactly. The authored content is on the canonical roster; the *runtime gate* is on the superseded one, and the *name registry* is on the doubly-superseded one.

**Settling the roster does not settle the assignments.** Three surfaces give King Almud three different conviction profiles. The antagonist identified the mechanism: the registry migrated his **Ethical Framework** (`Virtue (Crown)`) as if it were his Primary Conviction, via the legacy→canonical map, and **dropped his actual Primary Conviction, `Order`, entirely**. `Authority 0.30` has no antecedent in the doc at all.

### §3.3 A deprecation table transcribed into its own inverse

`alias_registry.yaml:648-663` lists **Virtue, Faith, Scholastic, Equity, Honor** — five of the canonical thirteen — as *legacy labels superseded by the taxonomy that contains them*. The entry's own `note` field enumerates all thirteen as canonical, four lines below.

The mechanism is a one-line diagnosis: `conviction_taxonomy_v30.md:274-281` is a two-column map (`Virtue Ethics → Virtue`, `Divine Command → Faith`, `Epistemic Reason → Scholastic`, `Rawlsian → Equity`, `Military Honor → Honor`). **The registry transcribed the right-hand column into the left-hand slot.** Targets replaced sources.

It is generated by `vocab_store`, so `--check` guarantees the error is faithfully republished, and it ships to `lexicon.json` and the dashboard.

---

## §4 RESONANT STYLE — the antagonist overturned my framing, and the remedy changed

I reported a four-way. **It is not.** The antagonist established, and the citations bear out, that one of the four is a *ratified, explicitly distinct concept*:

| Roster | Axes 3 & 4 | What it answers |
|---|---|---|
| `npc_behavior_v30.md:34-42` §1.3 | Authority + **Solidarity** | **what argument-form gets past this person's defences** (opponent-aimed) |
| `name_collision_database.yaml:421-430` | **Sanction** + Solidarity | a 2026-05-08 rename to kill the Authority/Conviction collision |
| `names_index.yaml:112-115` `ppt.*` | Authority + **Loyalty** | a 2026-07-21 registry addition that **re-canonizes both retired names**, with `legacy: []` |
| `armature.py:192-205` | Authority + **Insinuation** | **what moves the adjudicator** — RATIFIED, Gate C, ED-1062 |

`social_contest_v30.md:174` states the distinction in canon prose: *"This is what the ADJUDICATOR is moved by, **distinct from** … the existing opponent-aimed Resonant Style targeting, which fires on the party you are arguing against. The armature fires on the party who rules."* The reason `Solidarity` was not reused is written out: it is Knot-gated and relational, and a third-party judge is not Knot-bound to either orator.

> **A remedy that merged these would destroy a ratified distinction.** This is why the four-kind taxonomy in §0 matters: A vs D is an **OVERLAP with a correctly-named boundary**, not a conflict.

**What survives is a genuine two-name conflict on one member** — `Solidarity` vs `Loyalty` — where a July registry addition silently reversed a May collision fix.

**And the antagonist found something stronger than anything the producer filed.** `name_collision_database.yaml:421-425` prescribes renaming "Authority (pressure point)" → **Sanction**. That rename is unusable: `faction_layer_v30.md:455-461` is a live five-tier **Parliamentary Sanction** ladder (Censure / Embargo / Blockade / Combined / Outlawry). **The collision database prescribes a fix that manufactures a new collision.**

Meanwhile `descriptor_registry.yaml:177` retires `resonance_style` as *"never canonically enumerated"* and then corrects itself in the same entry: *"⚠️ **the premise is factually FALSE** — npc_behavior_v30.md §1.3's Resonant Style Taxonomy is CANONICAL… **NEEDS-JORDAN**"* — flagged 2026-07-07, still open. Since that retirement, **three further namings of the same four concepts appeared.** That is what happens when a registry says a live concept does not exist.

---

## §5 THE SECOND AXIS PP-684 DESTROYED

`npc_behavior_system_v1.md:19-23` states the distinction plainly:

> **Conviction** — determines what the NPC *wants to do*.
> **Ethical Framework** — inherited from the NPC's faction — determines what the NPC is *rewarded for doing*.

PP-684 §6 aliased the Ethical Framework labels **into** the Conviction taxonomy, treating them as the same axis. They are not.

> **This destroys the most legible dramatic engine in the corpus: a devout man serving a cynical institution.** Collapsed to one axis, every character becomes internally consistent, and every institutional-betrayal arc in the roster — Haelgrund-as-Bellarmine, Torsvald-as-Granville — loses its mechanism.

`character_canon_v30.md` D2 has been quietly ignoring the supersession for 3.5 months, retaining the labels as "descriptive disposition tags" with live Ob modifiers. That instinct was right and is unratified.

---

## §6 WHAT THE CORPUS ALREADY DOES WELL — reported because it is the model

Three vocabularies came back **clean**, and two seeded suspicions came back **false**. Recording both, because a sweep that only finds breakage is not measuring.

- **Public Temperament** — `territory_temperaments_v30.md` and `temperaments.py` are **identical**, including T16, including the per-faction aggregates. Registered `by_reference`. This is what a shared vocabulary looks like.
- **Coherence bands** — `Stable / Dissonant / Fragmented / Fractured / Severed` with identical numeric bands across `knots.py`, the prose-writer skill, and `threadwork_v30 §3.3`. Three surfaces, no drift.
- **The Calamity node map** — `calamity_radiation_v30.md` and the geography YAML agree band-for-band, and match every province's `proximity_calamity`.
- **`_ACCORD_SCENE_OUTCOMES`** — a closed vocabulary, validated before trust, honestly marked DORMANT, with a written record of why inferring it from `scene_type` was **deleted as fabrication**. The best-behaved vocabulary in the sweep.
- **`da.*` vs the action verbs** — explicitly disambiguated in-tree: *"those are the Keys domain-action resolution EMITS; the verbs below are the actions a player SELECTS."* This is the model for how a boundary should be written.

**Two seeds I supplied that were wrong:** **TS is not a homonym** — it is Thread Sensitivity everywhere, and the mass-battle hit was a grep artifact. **Coherence is one consistent axis** across threadwork, `CoherenceState` and P-15. I also seeded the three `*_currency_v1.md` files as possible rival currencies; **they are currency-*of-record*, doc lineage** — my misreading, and itself a live instance of the §4 word-choice hazard.

---

## §7 OUTCOMES — 37 vocabularies, and a canonical file carrying nine of them

The degree ladder is **the one axis with a purpose-built guard**, and it is correspondingly the cleanest: `degree_from_net` is single-owned, and every migrated adapter is verified equivalent cell-for-cell. Two declared holds remain, both ruled to migrate and neither executed.

**Everything the guard cannot see has forked.** `test_degree_ladder_single_owner.py` matches only four spellings, scans only `.py`, and raises `KeyError` on anything else — so it cannot see any `.md`, any `.gd`, or any rival vocabulary using different words.

**`systems/_architecture/key_type_registry_v30.md` — one CANONICAL Class-A file — carries nine outcome vocabularies:**

| line | field | membership |
|---|---|---|
| `:52` | `outcome` | decisive · compromise · stalemate |
| `:198` | `outcome` | success · partial · failure — **no Overwhelming** |
| `:403` | `outcome_class` | the ladder **+ `unknown`** |
| `:568` | `outcome` | active · failed_counterattack · failed_mandate_floor |
| `:657` | `outcome` | success · failure · inconclusive |
| `:845` | `outcome` | initiator_win · target_win · compromise · **stalemate** |
| `:905` | `outcome` | attacker_win · defender_win · draw · **rout** · **withdrawal** |
| `:942` | **`degree`** | **graze** · partial · success · overwhelming |
| `:974` | `scene_outcome` | governance · destabilisation · territorial_transfer · violence |

Three consequences worth naming:

- **`rout` and `withdrawal` are the two combat endings a chronicle most wants** — they carry *how* a fight ended rather than *who* won — and they are registered and **unwritable**. The only producer emits three tokens.
- **`:942` is a rival degree ladder in canon**, putting `graze` where Failure belongs. A Godot importer typing off this file builds an enum in which the failure case is a *light hit* — a wound where canon says a miss.
- **`graze` already means four things**, and the Godot skeleton contains the collision *internally*: `strike_module.gd:74` says `graze = partial`; `combat_config.gd:27` lists them as distinct. This is the sharpest port-time defect in the sweep.

**And `committee` — the only token in the tree naming a contest that produced a compromise rather than a winner, the outcome the design explicitly wanted — cannot cross a scale boundary.** The bridge collapses it to `Partial`; `scene.contest_resolved` has no such token. The deliberative outcome the system was built to produce is untellable outside the bout.

---

## §8 SCALE — the largest act in the world cannot be recorded

```
SCALES = ('personal', 'settlement', 'territory', 'peninsula')
```

Four, and **hard-enforced**: `keys.py:415` raises `KeyValidationError` on anything else. Against:

| Roster | n | Members |
|---|---|---|
| `keys.py:65` | **4** | personal · settlement · territory · peninsula |
| `scale_transitions_v30.md:28` | **5** | Object · Personal · Relational · Territorial · Structural |
| `operations.py:54` | **6** | Object · Personal · Relational · **Field** · Structural · **Foundational** |

Only `Personal` appears in all three. `Field` (Ob 5) and `Territorial` (Ob 4) are the same slot with two names *and* two numbers.

> **A Foundational-depth Weaving — Ob 13, TS 90, the ceiling of what a practitioner can attempt — cannot emit a Key.** It happens at a scale the substrate refuses to validate, so it cannot be witnessed, cannot cascade, cannot be remembered by an NPC, and cannot reach a chronicle. The largest thing in the world is the one thing the event system cannot record.

And one tier below that: **"territory" itself means 17 things, 37 things, or a newly-ruled intermediate tier**. `scale_hierarchy_v1.md` is RATIFIED by direct Jordan ruling and unexecuted; PP-726 says *"Territory = Settlement"*; `settlement_layer §1.1` says the 17 territories *become provinces*; and `registry.py:262` performs the collapse in one line, reading a key named `territory` into a field named `province_id`. **Under the ratified model there is now no name at all for T1–T17.**

---

## §9 PLACE — verified by loading the world

```
territories: 16 | T16 present: False
geography provinces: 17 | settlements: 37
type histogram: {'Town': 15, 'Village': 14, 'Seat': 2, 'Fortress': 2,
                 'City': 2, 'Fortress-City': 1, 'Cathedral-City': 1}
settlements whose province is NOT in world.territories: ['S-037']
```

**Three things fall straight out of that:**

1. **Schoenland is a place the world cannot address.** T16 is authored in the canonical geography, given a temperament, given a radiation band, and named as home by a registry character — and it is absent from `STARTING_OWNER`. S-037 is permanently orphaned. Any action, march or scene targeting T16 raises. And `game_state.py` carries **two different territory sets in one file** — `ALL_PLAYABLE_15` (15) and `STARTING_OWNER` (16).
2. **43% of Valoria has no type.** Village (14), Fortress-City and Cathedral-City are absent from the type tables that assign facility slots, Local Actor counts and radiation modifiers. **Fourteen villages — the most common kind of place in the setting — cannot host a rank-holder, cannot generate a named local, and cannot be described as feeling the Calamity.** Meanwhile Port, Cathedral, Mine and Outpost have **zero instances** on the map, and the Calamity table keys its "frontier falls first" rule to Outpost, naming three settlements that are a Village and two Towns.
3. **The memory vocabulary of a place has five rival lists.** Union 11, intersection 4. `Leverage` is in the code and in Goldenfurt and in *neither* design doc that enumerates the set. D3 is **RATIFIED** — *"keep the built five; re-express Compact as a `Debt` subtype"* — and was never propagated; the doc still calls Compact "a fifth family". And the scope conflict has teeth: Reputation is single-valued per settlement in code, while the grounded deck writes it **onto NPCs**, so thanking a merchant **silently erases the town's memory that its governor defended it.**

**The one town worked end-to-end cannot run.** Goldenfurt's spec authors `facility_tier=1, religious_building="Chapel", subnational={Guild,Church,RM,Niflhel}`. The loader reads only the geography YAML, so the loaded S-006 has `facility_tier=0, ap=2, religious_building='None', subnational={}`. **The vise the slice exists to demonstrate — "3 AP cannot serve all three" — is off by a third before a card is drawn**, and its Geneva-trap arc, gated on `religious_building == Chapel`, cannot fire.

---

## §10 VOICE — the precedence runs backwards from status

| | `narrative_voice_canon_v30.md` | Solmund corpus | `prose-writer/SKILL.md` |
|---|---|---|---|
| Status | **CANONICAL**, ED-1030 | PROVISIONAL / DRAFT | a skill |
| Claims | *"the single source for Valoria's narrative voice"* | — | — |
| Authors | **8 listed, 12 claimed** | **21 registers** | **12** |
| Cited by code | **nothing** | nothing | **the RATIFIED narrative engine** |

The two frameworks share **not one author name**. The CANONICAL one claims exclusivity and contains none of the setting's religious voice; the PROVISIONAL one contains all of it. The four authors the canon claims but does not list are exactly the four the skill adds — Lem, McCarthy, Le Carré, Beckett — so a writer following the canon's own pointer gets 8 of 12 and no notice that four are missing.

**And the document that will actually be executed to produce prose cites the wrong ones.** `narrative_engine_design_v2_churn.md` is RATIFIED and is `CURRENT.md`'s narrative-engine head. Its bake directives name the **skill's** 12-author table and the **PROVISIONAL** Solmund registers — under the axis name **Certainty**, renamed to Truth thirteen days after that doc was ratified.

Three compounding facts:

- **Truth-0 has no register at all.** §18's rows run 1-2 / 3 / 4 / 5 / 6+ on a **0–5** track. So the Edeyja pole — the character who has fully accepted Thread-truth against the Church, the most narratively distinctive position in the setting — falls off the bottom of every table, and the "6+" register is unreachable off the top.
- **Two Jordan-REJECTED sources are still assigned.** ibn Gabirol and Abulafia were excluded by editorial direction 2026-04-25; the master document still assigns them as the register for Graduation Texts and Practitioner Notation.
- **`CURRENT.md` has no `systems/world/` row**, so a session establishing currency by the book never sees any of this.

Meanwhile the four renderers that exist — a technical trace, a sports-commentator call, a bracketed chronicle, and second-person UI cards — cite **no voice spec at all**, and the only one that reaches players is authored in a "CDS voice" that appears in no voice document.

---

## §11 HONESTY — what was already tracked, and what the antagonist killed

### §11.1 Already registered before this sweep

The antagonist established that **seven flagship findings are already prioritised open work** in the live continuity surface:

| Finding | Where it was already filed |
|---|---|
| P2/P3 — the `'Loyalty'` Scar no-op | `HANDOFF_IN.md:864-866` — **Tier 0, NEXT ACTION #1, T0-1** |
| P1 — conviction-vocabulary reconciliation | `HANDOFF_IN.md:874-876` — **J-C, held for Jordan** |
| P8 — the two `armature_position` bases | `HANDOFF_IN.md:1203-1204` — **ED-IN-0073 L2**, remediation already specified |
| P9 — roster vs `npc_behavior` contradictions | **ED-IN-0073 L3/L4** |
| P4, P12, P13 | `HANDOFF_IN.md:3475`, `:1851`, `:1189` |

**And this session already wrote the rule it just broke.** `proposals/2026-08-19-…:229-236` closes with: *"Presenting tracked defects as discoveries inflates apparent yield. The method fix is one line: read `proposals/` and `audit/` before claiming a defect is new."* The producer repeated the named failure four days later. **The correction belongs here, at the top of the honesty section, not buried.**

**J-C's own framing also undercounts.** It reads *"4 substrate axes vs 9 character-sim names vs 8 NPE names."* The real span includes the canonical 13, the `names_index` 7, and the `complete_systems_reference` 7 — **five rosters, not three.**

### §11.2 Genuinely new, and worth Jordan's time

- **P6** — the Sanction rename collision: the collision database prescribes a fix that manufactures a new collision.
- **R5** — the fifth roster at `complete_systems_reference.md:23`, whose supersession banner is scoped only to combat. **This is where `names_index`'s 7 comes from.**
- **P10** — the `alias_registry` inverted table, now a one-line diagnosis and a mechanical fix.
- **§2.2** — `enforce: warn` on 112 of 113 entries as the root enforcement gap.
- **O4, O14, L2, L3, L7's D3 non-propagation, M6, M7.**

### §11.3 What the antagonist overturned — including the thing I most wanted attacked

| Claim | Verdict |
|---|---|
| **Resonant Style is a four-way** | **OVERTURNED.** The armature basis is a ratified, explicitly distinct concept. Merging would destroy it. **A narrower two-name conflict survives** |
| An `accord` read/write asymmetry | **OVERTURNED.** Assembled by matching the token "accord" across a registry key and a method name — two scales, two quantities. **The term-vs-concept error, committed inside a sweep for term-vs-concept errors** |
| `npc_behavior §2` uses *only* legacy labels | **FALSE.** 10 of 22 cited lines name canonical convictions; 14 cells carry deprecated labels, and the producer missed two of them |
| Both `worldview` consumers | **OVERTURNED.** Both cited lines are comments; the real consumer is a set intersection at `npe.py:344`. Conclusion survives, evidence did not |
| "Loyalty names five things" | **NOT ESTABLISHED.** Three solid, one weak, one unchecked |
| `symbolic_dimensions` does not exist | **FALSE** — I checked; it is a real field on `Key`. Had I accepted it, I would have retracted a correct claim in the master log |

Line numbers were wrong in roughly a third of the producer's citations. Every citation in this document has been re-derived.

---

## §12 COVERAGE

**Verified by me personally** (parse, read, or execution): the conviction scar gate and the 12-of-43 count; `names_index`'s 7 `conv.*` and 4 `ppt.*`; the `enforce` tier distribution; the `alias_registry` inverted table against its source; `complete_systems_reference` §1.1 and its banner scope; `SCALES` and `Key`'s field list; the `alias_registry` phantom genre/interaction values; `create_world` territory count, S-037's orphaning, and the settlement type histogram; the TN Monte Carlo; the `deprecated/` FORKED probe; the PP freeze vs `id_reservations`; `season.py`'s unconditional accounting; `mass_seizure`'s raw accord write; `treaty.py`'s never-lapse fallback; the `#4)` truncation.

**Producer-grade, antagonist-checked:** everything in §3–§5 and §9.

**Producer-grade, NOT antagonist-checked** — treat as a lower bound: §7 (outcomes), §8 (scale), §10 (voice), the place-and-polity rows of §1, and the entire supplement M. **Only the person-texture sweep received an antagonist**, and it overturned two of its claims and corrected a third of its citations. **The others should be assumed to carry a similar error rate.**

**Declared unread by the sweeps and still unread:** `settlement_adjacency_v30.md`, `march_layer_v30.md`, `faction_behavior_v30.md`, `faction_state_authoring_v30.md`, `factions_personal_v30.md`, ~46 of the 58 grounded cards, `systems/ui/`, most of the `audit/` corpus, `conviction_migration_roster_v30.md` (antagonist), `clock_registry_v30.md` (antagonist), and 45 of 46 registry entries at antagonist grade.

**The largest qualifier:** every count of the form "N rosters" is a **lower bound**. Five conviction rosters were found by six sweeps reading different parts of the tree; the fifth was found only because an antagonist checked a supersession banner's scope. There is no instrument that could tell us the count is complete, because — §2.1 — **no registry in this repo can express a set.**
