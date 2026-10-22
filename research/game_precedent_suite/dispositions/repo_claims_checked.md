# What the Valoria repo already says about the comparison-set games

Read-only scan of `/home/user/ttrpg`, 2026-10-22: case-sensitive `rg --hidden -g '!.git'` with word boundaries over the whole tree incl. `.designs/`
and `.audit/`; every match context read for the games below. Everything here is a **repo claim**, never a fact (CLAUDE.md §0.05: `research/` and
`proposals/` prose is reference only). Tags: `[UNV]` repo itself marks it [UNVERIFIED]/[MEMORY]/"leads"; `[SELF]` self-authored by an agent here;
`[UPLOAD]` rests on a document Jordan uploaded that is NOT committed (cannot be re-opened); `[M]` my memory; `[V]` I fetched it this session;
`[S]` search snippet only. "files a/b" = all files / authored docs (excluding `research/provenance/` harvest copies, `registers/`, `_session_provenance/`,
json/jsonl, tests). Counts are mentions, not study depth. Dropped as false positives: `Old World` in `research/pre_firearms_formations/*`
(Americas vs Europe), `Kingmaker's Moment` (canon arc, `proposals/2026-08-30-arc-reachability/01_arcs_01_18.md:491`), `Mordhau`/`Nemesis`-as-HEMA/lore,
`xcom` inside `EXCOMM_*`, lower-case verbs.

## 0. Provenance ceiling (applies to every row below)

- `research/00_INDEX.md:30-33`: Paradox/KOEI/Brigandine/Unicorn Overlord wikis returned 402/403, so "specific figures about games are leads; the durable
  findings are shapes"; strongest rows = Victoria 3 law enactment, Pax Pamir pricing, Burning Wheel *Duel of Wits*. `by_lane/README.md:15-17`: the lane
  files are an audit-design pass; "if this directory were deleted the game would behave identically."
- Four feeders: (1) companion `research/valoria_game_precedent_companion_v1*.md` (3 programs; "no precedent claim re-verified against source", `by_lane/PC:84`;
  downstream copies drop [UNVERIFIED] marks, `R4 K7`); (2) verb-coverage doc VCD `proposals/2026-10-03-verb-coverage-and-gap-fill.md` (7 detective games +
  CK3 + Romance of the Three Kingdoms; "many review sites returned HTTP 403", Paradox wiki Schemes/Council/Laws/Hooks pages "would not load", `:156-160`,
  `:4556-4568`; Lacuna/Tails Noir thin; some Disco Elysium and L.A. Noire rows "from memory"); (3) two uploaded surveys *Mechanics of Inquiry* (P1-P58)
  and *Narrative Churn* (F01-F84) plus six uploaded game docs (`13G` thirteen strategy games, `20G` twenty games, `TD` nine-title teardown `3cb2a6c8`...) - none committed
  (`VCD:99-133,171-190`; `by_lane/00_COMPARATIVE_ANALYSIS.md:305,677`); (4) verbs lexicon `proposals/2026-10-16-verbs/`, where nearly every game cell is `[MEMORY]`.
- Coverage the repo admits: settlement-governance rests on 4 games, conquest terms "almost entirely by Venice" (`companion_part5.md:229-245`); `20G`'s twenty titles leave
  Dwarf Fortress, RimWorld, Victoria, Frostpunk, Old World "unexamined" (`00_COMPARATIVE_ANALYSIS.md:305`); Mount & Blade and Heroes of Might and Magic "thin/absent".

## 1. Coverage of the comparison set

| game | files a/b | substantive files | depth |
|---|---|---|---|
| Crusader Kings III (+CK2) | 104/90 | VCD (78 lines), companion p5/p6, `by_lane/FA`, `NPC`, `WR` | deep (shapes + some numbers) |
| Total War (series) | 58/44 | `proposals/2026-09-25-squad-engagement-concept-v5.md` (27), `by_lane/MB` (21), PMM (10), companion p5 | deep on morale/autoresolve/governors |
| Mount & Blade (Warband/Bannerlord) | 52/46 | VCD (18), companion p1 §2.12, `by_lane/PC`/`FA` | medium; companion: "thinnest treatment" |
| Disco Elysium | 39/33 | VCD (20), `by_lane/FI` (9), proceedings relay A, `.designs` UI v4 | medium, partly [UNV] |
| Victoria 3 | 33/29 | `.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md`, companion p5/p6 | deep on ONE mechanism (law enactment) |
| Pentiment | 32/30 | VCD (28), `by_lane/FI` (13), `relay/G_EMERGENCE_PRECEDENT.md` (9), fieldwork proposal | medium-deep |
| Manor Lords | 21/19 | `by_lane/SE` (22), VCD (9) | medium (teardown upload) |
| Old World | 15/15 | companion p2/p5, `.audit/.../01...md:226,708`, `by_lane/NPC`/`FA` | one mechanism (ambitions) |
| Banished | 17/16 | `by_lane/SE` (22), settlements-factions-populations 02/05 | one family (pop/housing) |
| Suzerain | 17/16 | VCD (10), companion p5/p7, `by_lane/FA` | medium |
| Wildermyth | 16/13 | companion p1/p2/p5, THR ch1/ch5 | failure-shape only |
| Pathologic (2) | 13/12 | `player_agency_v30.md:59-63`, fieldwork proposal, `by_lane/FI` | thin (time-scarcity) |
| Frostpunk | 12/12 | governance-corpus-rebuild 02/03, `by_lane/SE`, verbs-14 | thin; "unexamined" |
| Battle Brothers | 11/10 | 2 lines each in 5 files | name-drop (fatigue, attributes) |
| Shadows of Doubt | 11/10 | VCD (52), `by_lane/FI` (15), verbs-12 (9) | deep in VCD (snippet-level) |
| Tropico | 11/11 | VCD (6), `by_lane/SE` (6), `WR` (5) | medium (upload) |
| L.A. Noire | 9/9 | VCD (30), `by_lane/IN`/`FI` | medium, partly [MEMORY] |
| Sunless Sea / Fallen London | 6/6 | proceedings relay A:194, B:827; VCD:1128 | name-drop (only "Fallen London" is analysed) |
| Griftlands | 5/5 | `by_lane/SC` (9), `.audit` SC sources 04 (4) + 03 (4) | one mechanism (negotiation) |
| Return of the Obra Dinn | 5/5 | VCD (6), fieldwork proposal (5), `by_lane/FI` (4) | one mechanism (batch confirmation) |
| Democracy 4 | 5/5 | `governance-corpus-rebuild/02-critique-and-precedents.md:281-299` | one idea [SELF] |
| Kingdom Come: Deliverance | 4/4 | fieldwork:103, `04_the_bout.md:117`, UI v4_1:1296 | name-drop |
| Field of Glory (ambiguous: tabletop or FoG II) | 4 | `by_lane/MB:150,166,210`, `multiunit_envelopment_plan.md:35` | name-drop (zone of control) |
| Patrician (III/IV/Port Royale lumped) | 4 | verbs-16 (5 lines, [MEMORY]) | name-drop |
| Hearts of Iron IV | 2 | VCD (7), verbs-17:69 | espionage only (survey) |
| Ultimate General | 2 | squad concept v5 (5), `by_lane/MB:145` | name-drop ("anchor") |
| Anno (1800/1404) | 2 | verbs-16:112,152, `verb_list.md:388` | name-drop [MEMORY] |
| The Sims 4 ("The Sims" only) | 2 | VCD:1125 | name-drop |
| Dragon Age (Inquisition not specified) | 2 | verbs-13:106,112, UI v4:2050 | name-drop [MEMORY] |
| Pathfinder: Kingmaker | 2 | verbs-17:73, `proposals/verb_list.md:449` ("Kingmaker hexes") | name-drop [MEMORY] |
| Kenshi | 1 | VCD:4615 ("not examined") | listed as unexamined |
| Baldur's Gate 3, Darkest Dungeon (I/II), Eternal Darkness, Don't Starve, Vampire: Bloodlines | 0 | -- | no hit under any spelling variant tried (`Baldur`, `Darkest`, `Eternal Dark`, `Starve`, `Masquerade`, `Bloodlines`) |

## 2. Claims per game (a/b/c: files, claims with file:line, disagreements)

**Crusader Kings III / CK2.** Claims: crown authority "four levels" gating what a liege may attempt (`companion_part5.md:37`; `.audit/.../01:220` tagged
`[T2 gamepressure guide; TV Tropes]`); vassal contracts trade extraction (Scutage +50% tax/-75% levy, March -50% tax/+20% levy, Palatinate -20% both,
`companion_part6.md:112`); levies "cost zero gold", men-at-arms "gold plus prestige", maintenance "even while unraised ... roughly triples once fielded"
(`part5.md:144`, `part6.md:110,114,116`); council-seat denial "flat -40 opinion" (`part5.md:81`; `FA:108` "numbers are leads"); unlanded courtiers leave "2%/month",
~6-7 parentless 16-year-olds spawn monthly, >24,000-character saves, two mods pull opposite ways (`part5.md:122`; `WR:98` "population figure community-derived");
one "tyrannical" contract change at a time, -15/-25 up, +5/+10 down (`part6.md:118`); CK2 apophenia "flagged by its own developer as not a mechanism" (`part5.md:213`);
CK2 truce break "-25 relations ... -5 diplomacy for 5 years" (`FA:121`, `[UPLOAD 13G, T1 CK2 wiki, patch-bound]`). VCD App. B rows 1-63 (`:4452-4519`) map ~60 CK3 acts
(hooks, secrets, schemes, blackmail, torture, banishment) from the Paradox "Interactions"/"Casus belli" pages + guides; blackmail/secret rules "from a pre-release
developer diary (2020), not re-verified under 1.20" (`VCD:182-184`); CK3 "torture", "banishment" `[UNV]` (`:4482,4484`); versions "1.19 Scribe (Apr 2026)", "1.20 Crozier" `[UNV]` (`:918,1263`).
Valoria declares CK3 vassal play a stance precedent (`.designs/.../player_agency_v30.md:40-46`). (c) No certain disagreement. Worth checking before reuse [M, not certain]: the
-40 council-denial reads like a CK2-era modifier filed under CK3; "plus prestige" for men-at-arms.

**Total War.** Governor "three times yes, twice no" across 20 years, "no convergent answer" (`part5.md:79`; `PMM:571`); occupy/sack/raze (`:100`); Shogun 2 ashigaru start
"-4 morale", Samurai behind building chains, "auto-culls units"; Medieval II "requires manual disbanding" (`:145-146`; PMM first got this wrong and self-corrected, `PMM:399-402`);
Three Kingdoms unit types gated by commander class, two-tier defeat (a general's death destroys his retinue only if the army also routs) (`:149,171`); Rome II agents consolidated
to three types (`PMM:269`); autoresolve "a different algorithm", calibration "never published, in twenty years", divergence "exploited in both directions" (`:185`; `by_lane/MB:156`);
lord aura = flat bonus, scale-blind (`:165`). `squad-engagement-concept-v5.md` cites Total War 27 times, always as an `[ASSUMPTION: ... basis: Total War ...]` anchor (morale states with recovery lag
`:182`, brace `:149`, shock cap `:116`, ammunition `:487`); the doc is CONCEPT, non-canonical, `[SELF]`. (c) Cannot confirm the "never published" claim either way.

**Mount & Blade (Warband/Bannerlord).** Companion calls it "the closest whole-game analogue, and the thinnest treatment" (`companion_v1.md:506-541`); "personal actor becomes irrelevant as N grows"
(fully fused, `part5.md:167`); same row elsewhere says layers "do not couple" - an unreconciled contradiction the repo itself notes (`by_lane/PC:89`, `R8 K13`). Declared stance precedent
(`player_agency_v30.md:53-57`). Churn-survey rows `[UPLOAD]`: Bannerlord traits drive AI but "it can be difficult to discern their role" (TaleWorlds, `VCD:986`); clans leaving the day they join
(`:1001`); executions start feuds via Honour/Mercy (`:1081`); influence-weighted kingdom votes (`:1082`, `FA:124` constants `[UNV]`, patch-variant); a mod's "Lords at -20 or lower will refuse" (`VCD:989`).

**Disco Elysium.** 24 skills under 4 attributes (Composure and Perception filed under Motorics, Volition/Authority/Empathy under Psyche; `proposals/2026-10-16-attributes-from-scratch_part5.md:183`) - matches
what I recall [M]. Shows modifiers and odds ("+1 ... 63%"), white checks retry when the world changes, red once, failure is content (`relay/A_FABLE_INTERROGATION.md:191`; written "from model knowledge with no
verification marks", `by_lane/SC:90`) - matches [M]. VCD rows G1-20..34 (pressing locks options, arrest, hanged man) with arrest `[UNV]` (`VCD:4481`). Used as the counter-example to "never show a number"
(`by_lane/SC:114,291`). Valoria's dialogue is called "DE's spiritual descendant" (`.designs/systems/ui/reference/valoria_ui_ux_v4.md:797`).

**Victoria 3.** All repo claims concern clout/legitimacy and law enactment (`.audit/.../01:212-217,396-404`; `part5.md:36,58`; `part6.md:39-64`): interest groups hold clout; legitimacy 0-100;
"below 25 ... cannot pass any law except one supported by an active movement"; enactment = multi-stage success vs stall chance; ruler stance +/-5% per step; "three setbacks ... fails, locking the law out
for two years"; 100 days base per stage, x2 governing-principle laws, x1.5 power-distribution/economic-system, legitimacy >90 -25%, 25-49 +50% - tagged `[T0 official wiki, Laws]`; counter-mobilisation
(half at once, 1%/week, revolution above 75% participation) tagged `[T2 namu.wiki; UNVERIFIED against current patch]`. The repo itself says the numbers are "tuned for a nation-state ... 1836-1936" and "borrowed at the wrong
scale" (`01:735`; `03_consolidation.md:37,596`). "Deep as a puddle" critic quote on legitimacy (`part5.md:36`). Also: single ownership "goods live in the market" (`02-critique:247`, `[SELF]`); "no numeric stats at all"
(`2026-08-15-character-and-faction-stats-and-progression.md:1554`). (c) See section 4, item 2: partly stale against the official 1.3 diary.

**Old World.** One claim, repeated in 8 docs: ambitions are victory conditions "generated by the current ruler's attitudes crossed with the influential families", "expire when the ruler dies"
(`.audit/.../01:226,708`; `companion_part2.md:138`; `part5.md:39`; `by_lane/NPC:138,302` "UNGROUNDED in cited evidence; convergent"). "Not surveyed" for failure (`part5.md:39`). (c) Section 4, item 3.

**Pentiment.** Finite days, cannot interview everyone, "you never learn whether you were right", accusation has consequences regardless (`fieldwork-architecture...md:119,136`, `[HIGH]`);
director said there "cannot be a right answer" (`VCD:669`); flags "unbounded count across the whole (~25 in-fiction year) game ... each read by exactly one later scene" (`relay/G_EMERGENCE_PRECEDENT.md:152`,
a targeted-search survey); VCD P1/P3/P23-25/P29 (`:768-796`) from snippets - "Acts II-III trial detail was not fetched" (`:158,4562`); `by_lane/FI:80` "[UNVERIFIED as to specific mechanics]", and FI notes the
same game carries two confidence grades in two docs (`FI:98`). Declared stance precedent (`player_agency_v30.md:63-67`).

**Shadows of Doubt.** Heaviest single-game table: prints/footage expire (`VCD:773`), generic prompts/payment/confrontation (`:777`), print lookup (`:779`), case board (`:784`), "beaten, you wake in hospital"
(`:795`), trespass = categorical crime (`:801`), consent search (`:802`), social credit "1 to start, 8 to retire" (`:803`), citizen routines/CCTV/tailing (`:1088-1096`). Sources: survey `[UPLOAD]` + store pages/snippets
(early access 24 Apr 2023, 1.0 26 Sep 2024, `VCD:291-298,4559`). The repo flags the survey as internally inconsistent on whether a wrong case submission is accepted (`VCD:913,4659` App. D s(1)). (c) None found.

**L.A. Noire.** Grades every interrogation answer vs a hidden reading (`VCD:669`); Truth/Doubt/Lie, one correct per question (`:774`); facial performance as evidence (`:782`); remaster's approach choices
(`:674`); Cole Phelps arrests "memory-sure" (`:1605`). Matches my memory [M] (note the 2017 remaster renamed the options Good Cop/Bad Cop/Accuse).

**Return of the Obra Dinn.** Confirms fates "only in sets of three, the last six in twos" (`VCD:669`); "a closed 60-person puzzle" (`fieldwork:92`, where Valoria rejects confirm-in-threes); frozen-moment record (`VCD:780`).
(c) Confirmed: 60 people, sets of three, last six in pairs [S Wikipedia/Film Stories snippet].

**Griftlands.** Negotiation as a second deckbuilder: core argument with resolve, Composure lost each round, Influence/Dominance, "Interrogation/Planted Evidence" (`.audit/.../sources/04_negotiation_and_persuasion.md:154-162`, T2 from wikis/PC Gamer,
`:543` tier floor); Klei replaced spend-and-roll persuasion ("a lot less fun than fighting") with cards, "documented eleven-turn deadlock" (`.audit/.../03_persuasion_documents_adjudication.md:86,126`); `by_lane/SC:104,128`:
warning answered for the old kernel, never carried to the new one. Details of Influence/Dominance decay not checked [M, uncertain].

**Suzerain.** Cabinet advising "in their own interest"; "resolution is largely branch selection ... not a system" (`part5.md:44,62,85`, from `13G`/`20G`); political capital as a spendable meter (`relay/A:192`); weighted vote, budget and
authority, two-body threshold, advisory legislature, decree (Rizia) (`VCD:804-816`); "fixed term ... an ending that is a judgment rather than a victory" `[U]` (`FA:126`).

**Manor Lords / Banished / Tropico / Frostpunk / Wildermyth / Pathologic / Battle Brothers.**
Manor Lords: family-as-atom, burgage plot, plot capacity gates **immigration** not births (`by_lane/SE:107`, vs ED-SE-0051 which said both games gate births - repo's own correction); approval-gated immigration, development perks "DOES NOT APPLY" (`VCD:1074-1077`); named with M&B as a stance precedent (`player_agency_v30.md:53`). Source: `TD` upload, "figures [ASSUMPTION 0.8.10x], breakpoints T2 [UNV]".
Banished: delayed cohort, housing vacancy gates births (`settlements-factions-populations/02:116,224,228,431`; `SE:105,117` check against `TD:284`); "food-limited attrition" judged only PARTLY right - Banished starves through lost labour (`SE:105`); age pyramid as a legibility exemplar (`emergent-narrative-primitives-v2/01_THE_TEN.md:62`). `research/` held zero Banished hits before the SE lane (`SE:17`).
Tropico: housing chosen once, never re-appraised (`VCD:998,1123`); die-hard->moderate diffusion `[SESSION]` (`:1124`); mutually exclusive approval (`03_PROPOSALS_POLITICS.md:161`); "shack-squatting" cited as cost of full simulation - repo notes **causation inverted** (`SE:108`, `TD:245`).
Frostpunk: law ratchet - "laws are permanent and each opens two further, mutually exclusive laws" (`02-critique-and-precedents.md:360`, `[SELF]`); Book of Laws as diegetic cross-linked record (`fieldwork:154`); food laws, workers `[MEMORY]` (`verbs-14:84,89`).
Wildermyth: hand-written per-personality variants "explicitly not procedural"; legacy binding; "Tale-Spin effect" with DF and Nemesis (`part5.md:210`, `part2.md:31,62`, `THR 08_ch5:57`); legacy characters across campaigns `[UNV]` (`VCD:1129`).
Pathologic 2: 12 days, more needs than hours, triage (`player_agency_v30.md:59-63`; `fieldwork:118`) - matches [M]. Battle Brothers: fatigue as precedent (`derived_stats_v30.md:126-128`, `[WRONG]` see section 4), "five combat properties reachable turn-based with one d100 roll" (`pr350-archive-recovery/evidence/LANE_C.md:84`), "attribute is a price, never a power" (`2026-08-15-...stats-and-progression.md:930`).

**Minor mentions.** Democracy 4: "the simulation is a signed, weighted, delayed graph" (`02-critique-and-precedents.md:281-299`, `[SELF]`, written against an upload, "no repository file was read"). Hearts of Iron IV: intel level a percentage per target and branch, cryptology, false intelligence
(La Resistance) (`VCD:820-822`, `[UPLOAD]` survey; "described from established knowledge" for some titles, `:171-178`) - matches [M]. Kingdom Come: NPC schedules make *when* you look a variable (`fieldwork:103`); duelling lineage list `[UNV]` (`04_the_bout.md:117`); Cuman interrogation, Epilogue trial as dialogue-as-investigation
(UI v4_1:1296). Sunless/Fallen London: qualities unlock storylets - "eligibility-by-stat, refused by name", "menaces accumulate" (`relay/A:194`; `VCD:1128`). Ultimate General: objective-zone timers (`squad-v5:521`, "anchor"). Field of Glory: zone of control + flank/rear modifiers (`multiunit_envelopment_plan.md:35`, one sentence). Others are single `[MEMORY]` lines (see section 1).

## 3. Games the repo leans on that are NOT in the comparison set (videogames first; counts a/b files = all/authored)

| game | files | what the repo uses it for (anchors) | ranking note |
|---|---|---|---|
| Romance of the Three Kingdoms (KOEI RTK I-XIV, + Nobunaga's Ambition) | 59/53 (217 lines) | declared precedent "officer mode" (`player_agency_v30.md:36`); personnel program; VCD's 2nd extraction (RTK XIV manual pp3100-6300); eight domestic commands, LOY recruiter tell <=70, order<25 blocks conscription (`part5.md:80,120,148`, `proposals/2026-10-16-troop-stock-design.md:670`) | #1; RTK XI/XII espionage "not retrieved", RoTK-8/Remake manuals only (`VCD:4566-4568`) |
| Dwarf Fortress | 38/32 | in-depth in churn survey (`VCD:4608`, 33 lines); emergence precedent (`relay/G:41-49`); residual-free demotion (`part5.md:89-93`); grudge flag, Legends, "Tale-Spin effect"; attribute-as-price (`stats:930`) | #2; wiki-sourced; "20G left it unexamined" |
| EU4 (Europa Universalis IV) | 36/31 | "estates = the canonical ignorable mechanic" (loyalty floor ~40), Loyalty-vs-Influence revocation gate (`THR 08_ch5:55`, `05_ch2:387`) | failure dossier P1 |
| Jagged Alliance 2 / 3 | 24/20 (118 lines) | five-layer morale, +/-25 pairwise opinion matrix, v1.13 audit tool, militia ~$75 vs regulars ~$440, town-loyalty charge, garrison (`part5.md:118,147,170`) | #4; JA2 v1.13 docs |
| RimWorld | 22/21 | mood = sum of thoughts, 5/20/35% break thresholds, storyteller cadence, fight outcomes +38/-22 opinion (`relay/G:51-59`, `VCD:4518`) | #5 (matches my memory [M] for thresholds) |
| Dominions (5/6 not distinguished) | 31/22 | commander-anchored rout "scale-blind" `[UNV player-community consensus]` (`part5.md:166`, `THR 08_ch5:62`) | failure pole; generic "Dominions" |
| Football Manager | 28/22 | fidelity ladder (instant ~ played) and formation/role model (`part5.md:184`; ruled doctrine `auto_manual_resolution_duality_v1.md`) | the repo's model of the "right" shape |
| Skyrim | 22/17 | "Skyrim Eight" guild-ladder dimensions in Valoria's own Standing design (`faction_politics_v30.md:6` as quoted at `THR 05_ch2:575`); Radiant AI (`VCD:986`) | own-design provenance |
| Imperator: Rome | 21/16 | launch Loyalty -20 on appointment, action-currency scrapped (`THR 08_ch5:54`; `part5.md:40`) | failure dossier |
| Nemesis system (Shadow of Mordor/War) | 22/19 | persistent encounter log; patent US 10,926,179 (`relay/G:73-80`, `VCD:185`) | |
| Caves of Qud / Ultima Ratio Regum | 18/18 | generate-then-rationalize; reify only when visited (`relay/G:61-71`) | |
| King of Dragon Pass / Six Ages | 20/17 | authored-branch selection by stored state (`relay/G:121`) | |
| Ace Attorney 18, Triangle Strategy 17, Brigandine 16, Unicorn Overlord 14, The Guild 2/3 12, Lacuna 11, Heroes of Might and Magic 10, XCOM 13, Shadow Empire 7, Stellaris 7, Esoteric Ebb 7, Medieval II/Shogun 2/Rome II 24 | -- | evidence rows (P8 accusation, hidden convictions, garrison, evidence decay, accrual-by-structure "not surveyed", fidelity ladder, admin strain, "EU/Stellaris" as labels) | single-purpose; HoMM and Stellaris are named gaps/labels |

Tabletop/board (list only, files all/authored): Burning Wheel 42/35 (*Duel of Wits*; `part5.md:197`: collapses to Point+Dismiss, 21-vs-11 `[UNV]`); Pax Pamir 19/18 (pricing, currency-as-score); Republic of Rome 21/18 (shared loss, agenda control); Kremlin 17/12; John Company 13/10; Blades in the Dark 13; Ars Magica 16; Twilight Struggle 3. "Diplomacy" and "Root" are too common as words to count.

## 4. Repo claims found wrong, stale, or contradicted (verified items marked)

1. **Battle Brothers fatigue (WRONG).** `.designs/systems/_architecture/reference/derived_stats_v30.md:126-128`: "Armour moves from base reduction to drain modifier (Battle Brothers precedent: armor adds to per-action fatigue cost, doesn't reduce
   max fatigue)". In BB, body armor and helmets carry a **Maximum Fatigue penalty** (e.g. "-10", "-5" per piece) [S: Nexus mod page 525 + Steam threads app 365360; confident from memory too]. The `.designs/` file is quarantined, not canon.
2. **Victoria 3 enactment numbers (STALE/VERSION-DEPENDENT).** Repo (`.audit/...01:215-216`, `part6.md:49-56`): 100-day stages, x2/x1.5, legitimacy <25 / >90 / 25-49, "failure locks out two years". Official 1.3 dev diary 80 [V
   https://www.paradoxinteractive.com/games/victoria-3/news/dev-diary-80-law-enactment-and-revolution-clock-in-13]: "Laws now need to progress through three phases", up to three setbacks then "automatically and irrevocably fail" (agrees), the **2-year cooldown applies to
   cancelling** an enactment (raised from 1), cancelling a movement-pushed law spikes Radicalism, +5% enactment chance per phase; it mentions no 100-day stage and no 25/90 legitimacy thresholds (so not confirmed, not refuted). Repo numbers predate 1.3; the Paradox wiki would not load for me either.
3. **Old World ambitions (INCOMPLETE).** Repo: ambitions "expire when the ruler dies". Designer Notes #11 [V https://www.designer-notes.com/?p=1748]: ambitions belong to the leader, but unfinished ones pass to successors as "legacies ... finishable for a limited time after
   the leader's death"; ambitions come from a tier-gated deck; **ten ambitions = victory**. A secondary review says they are generated from game events and characters' desires [S].
4. **Internal contradictions the repo already admits** (not outside-source errors): M&B "layers do not couple" vs "fully fused" (`by_lane/PC:89`); PMM non-payment null (`PMM:399-402` vs `:511`; `by_lane/SE:118`); ED-SE-0051 on Manor Lords/Banished (`SE:117`); Tropico causation inverted (`SE:108`); Shadows of Doubt survey (`VCD:913`).
5. **Not found wrong:** Obra Dinn confirmation rule [S]; Disco Elysium skill filing and white/red checks [M]; Pathologic 2's 12 days [M]; RimWorld 5/20/35 thresholds [M]; HoI4 intel-per-branch [M]; Vic3 "three setbacks" [V].

## 5. Method notes and limits

- Read in full: `research/00_INDEX.md`, `by_lane/README.md`, companion p5, VCD §1-§2, §6.1-6.2, App. B/C/D; read around matches in the other lane files, companion p1-p7, `relay/G`, squad concept v5, fieldwork proposal, SE lane. Not read in full: `proposals/2026-10-16-verbs/*`, `.designs/` UI v4, `.audit/` workings.
- Counts: raw `rg -c` (file counts "a") vs the filtered authored set ("b"); harvest copies under `research/provenance/` and ledger rows inflate "a" (CK3 104 vs 90). Only web checks run: sections 4.1-4.3 and Obra Dinn.
- Dominions edition, Total War title, Anno/Patrician edition and Field of Glory edition are mostly unspecified in the repo; I did not guess.
