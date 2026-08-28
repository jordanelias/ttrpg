# Game Precedent Companion — Part 5: The Comparative Matrix

## Status: PROPOSED (2026-08-28) · reference under §0.05, not canon
## Version: v1.0 · Lane: IN (cross-cutting)
## Reads: Parts 1–4. **This part is the substrate they were written on top of.**

**Reading order:** [Part 1 · Corpus and Survey](valoria_game_precedent_companion_v1.md) → [Part 2 · Comparison, Complements, Synergies](valoria_game_precedent_companion_v1_part2.md) → [Part 3 · The Critique](valoria_game_precedent_companion_v1_part3.md) → [Part 4 · Reconcile and Unify](valoria_game_precedent_companion_v1_part4.md) → [Part 5 · The Matrix](valoria_game_precedent_companion_v1_part5.md)

Parts 1–4 argue. **This part does not argue.** For each Valoria system it lays the surveyed games
side by side on the *same* question, with Valoria as the last row, so the comparison can be inspected
rather than taken on trust.

**Three conventions, and the third one matters most.**

1. Each table asks one question of every game, so the cells are comparable rather than each game
   being described on its own terms.
2. **Valoria is always the last row**, in the same columns.
3. **`— not surveyed`** is a real and common cell. It means the corpus does not cover that game on
   that question, **not** that the game lacks the feature. Those cells are informative: they show
   where a conclusion in Parts 2–4 rests on three games rather than nine.

**Sourcing floor, restated because this part is where it bites hardest.** Fan wikis were bot-walled
across the research (Paradox, KOEI, Brigandine, Unicorn Overlord all returned 402/403), so the load-
bearing numbers below rest on guide sites, forum synthesis, `acoup.blog`, and the manuals that did
fetch — Koei Tecmo's *Awakening* and *RoTK 8 Remake*, Total War Academy, the JA2 v1.13 documentation.
Victoria 3's law arithmetic, Pax Pamir's pricing and Burning Wheel's *Duel of Wits* are the strongest
rows, taken from game files, a rulebook and a published rules text respectively. **Treat every number
as a lead; the durable findings are the shapes.**

---

## §12.1 The strategic actor — what a faction *is*, and how it acts

| Game | What the faction object holds | How it acts in a turn | What gives it an interior | Documented failure |
|---|---|---|---|---|
| **Victoria 3** | Interest groups holding **clout**; government is a subset of them, the rest are opposition. Legitimacy 0–100 derived principally from governing clout | Law enactment, plus IG pressure and movements | **Interest groups** — the faction is a coalition that can lose members | Below 25 legitimacy it can pass nothing except a law an active movement supports. Critics: *"deep as a puddle"* |
| **CK3** | Characters holding titles; vassals bound by **negotiable contracts**; **crown authority** at four levels gating what the liege may attempt at all | Character actions, schemes, council tasks | Vassals, court positions, councillors, family | *acoup*: personal-opinion bonuses paper over structural factors, so *"you can generally succeed at things kings wanted to do but were unable to pull off"* |
| **EU4** | Three **estates**, each with **Loyalty and Influence** tracked separately; revocation gated on Loyalty > Influence | Monarch points; estate interactions | Estates | The canonical *ignorable* mechanic — loyalty floor sat near 40 and nothing crossed it; players *"hardly even bother"* |
| **Old World** | A ruler with attitudes; **families** with their own desires; ambitions emitted from the intersection | Orders per turn; ambitions as victory conditions | Families, and mortality — outstanding ambitions go on a clock when the ruler dies | — not surveyed |
| **Imperator: Rome** | Governors carrying **Loyalty**, on an action-currency | Governor actions | Governors | Launch Loyalty dropped 20+ **on appointment alone** and bled regardless of play; Paradox scrapped the entire action-currency four months later |
| **Kremlin** *(board)* | You hold **influence over** politicians arranged in a pyramid; you never own them. Politicians age and die | Place influence; manoeuvre your man to the rostrum | The politicians, who are not yours | — |
| **John Company** *(board)* | Offices held by **different players**; most ventures need several offices to cooperate | Office actions; chairman election; a Parliament phase that changes the game's own rules | Distributed, complementary office powers | — |
| **Republic of Rome** *(board)* | Senate factions — **and the state itself**, which can lose | Proposals, votes, prosecutions | Factions plus a **shared-loss** condition | — |
| **Suzerain** | A cabinet of ministers who advise **in their own interest** | Choice under pressure | Interested advisors | Resolution is largely branch selection — the player chooses between authored futures rather than operating a system |
| **Mount & Blade** | Lords with fiefs and relations; kingdoms with policies | Party-level play, then kingdom decisions | Lords | — **thinly surveyed**; used in the corpus only as a comparator and a failure pole |
| **VALORIA** | Six scalars (`L Sta W I Mil intel`), a territory list, four turn-flags. `Faction.standing` outside the registry | **One `rng.random()`** against a prior re-weighted by three state signals | **Nothing.** Personality is `if faction.name == 'Crown'`; two of four factions have no branch | Swap Hafenmark and Varfell in the starting table and the campaign is unchanged |

**What the column reveals.** Eight of ten surveyed titles give a faction *parts* that can disagree —
estates, interest groups, vassals, families, offices, politicians. Valoria's has none, which is why
most of the genre's faction-scale vocabulary is untypeable here rather than merely unbuilt.

---

## §12.2 Deliberation — how a body converts talk into a decision

| Game | Is passing a measure an event or a process? | Who controls the agenda | Does a defeated motion leave anything? | Documented failure |
|---|---|---|---|---|
| **Victoria 3** | **A process.** Multi-stage; each stage a running success chance vs stall chance; **three setbacks fail it** and lock it out two years. 100-day base stage, ×2 for governing principles, ×1.5 for power-distribution; legitimacy >90 cuts 25%, 25–49 adds 50% | Government composition | No | **Attempting it mobilises the opposition** — participation in opposing movements rises on attempt, half at once and the rest weekly; past a threshold, revolution. *(Counter-mobilisation figures `[UNVERIFIED]` against current patch)* |
| **Republic of Rome** *(board)* | An event | The presiding official | No | — |
| **John Company** *(board)* | An event, in a dedicated phase | Chairman | No | — |
| **Die Macher** *(board)* | Positions and public opinion are **separate tracks**; the distance between them is what scores | — | — | — |
| **Suzerain** | An event | Scripted | — | Branch selection, not a system |
| **Roman Senate** *(historical — no surveyed game implements it)* | An event | ***relatio*** — the presiding magistrate states the question, and **the wording fixes which question the body is sitting at**. ***Discessio*** — with several motions live, the chair picks which to put and in what order | **Yes — *senatus auctoritas***: a motion that carried and was vetoed persists **with no force and full citability** | *Diem dicendo consumere* — talking until sunset kills the business |
| **Ming Grand Secretariat** *(historical)* | — | ***Piaoni*** — the drafter pastes a proposed rescript to the document, so the sovereign's choice is reduced to accept/reject/return | ***Fengbo*** — a sealed edict returned unpromulgated by the clerical layer | — |
| **VALORIA** | **An event, and a free one.** Per-side pool = Σ `int(L)` + genre/audience dice; a track from 5 moves by `max(0, net − resistance)`; ≥7 passes | **Nobody.** The bridge derives *who* proposes and *who* defends, never *what* | No | Fires **every season, unconditionally, at no cost**, on a motion with no subject (`motion_id = "parl_s7"`) |

**What the column reveals.** The single most-cited loan in the corpus — Victoria 3's enactment
process — has no analogue in any other surveyed game, and the three richest procedural mechanisms
(agenda framing, division order, recorded defeat) come from history because **no surveyed game has
them**. That is why Part 2 rates recorded defeat *"nearly free to implement"* and notes very few games
have it.

---

## §12.3 Settlement governance — the appointed governor

| Game | Is there an appointed governor? | What the player does at a settlement | Budget / scarcity | Documented failure |
|---|---|---|---|---|
| **Total War** | **Three times yes, twice no** — added, removed and re-added across twenty years for three different reasons | Construct buildings; set taxes; recruit | Turn time and money | ***"There is no convergent answer — a real, unsettled design tension, not a solved problem you are behind on"*** |
| **RoTK** | Yes — officers assigned to cities | **Eight domestic commands**, each keyed to one of four stats, flat **10 gold per officer** | Officer actions per turn | **Commerce, Cultivate and Conscript all drop Safety** — every gain costs elsewhere, arrived at independently of Valoria's verb design |
| **CK3** | Vassals rather than appointees; a **council** the player staffs | Build; grant and revoke; council tasks | Gold, prestige, piety | **Denying a powerful figure a council seat costs a flat −40 opinion** |
| **Victoria 3** | No — states, not governors | Build; set institutions | Bureaucracy, construction | — |
| **Heroes of Might and Magic** | — **not surveyed** | — | — | — |
| **Mount & Blade** | Fiefs with appointed companions | — **thinly surveyed** | — | — |
| **Suzerain** | No | Policy choice | Political capital | Branch selection |
| **VALORIA** | **Yes, in the schema, and nothing appoints one.** `governor_id` is `None` on all 37 after world-gen; its only writer `succeed_governor` has zero callers | **Nothing.** No verb menu exists; no Directive arrives; no card is drawn | `AP = 2 + facility_tier` — **computes correctly, zero readers**, and `facility_tier` is never raised by anything including the loader | *(see below)* |

**The row that inverts the table.** Dwarf Fortress's documented failure is that **demotion with no
residual reads consequence-free once survived** — a comeback that resets to zero is a reset button.
Valoria's `succeed_governor` calls `ledger_sweep`, and durable tags (`ttl=None`) **survive the
handover**, so a demoted governor's record outlives him. That is precisely the residual DF lacks,
built correctly, **with zero callers and no tag writer anywhere in the tree.**

---

## §12.4 Conquest — what happens when territory changes hands

| Game | At capture, the player… | Do local institutions survive? | Is there an occupation phase? |
|---|---|---|---|
| **Total War** | Chooses **occupy / sack / raze** | Partially (public order, corruption) | No |
| **CK3** | Takes the title; de jure drift over time | Vassals persist under contracts | No, but de jure claims mature slowly |
| **Victoria 3** | Incorporates or holds as unincorporated | Institutions are state-level | Incorporation is a state with different rules |
| **Mount & Blade** | Takes the fief; loyalty decays | — not surveyed | — not surveyed |
| **Venice** *(historical — the corpus's model)* | Negotiates a ***dedizione***: local statutes, tax exemptions, guild privileges and councils **formally preserved** in exchange for loyalty and appellate supremacy | **Yes, by treaty** — Vicenza kept a great council of 500, a minor council of 150, and a court that could impose death | Venice inserted **two rectors** (a *podestà* over civil justice, a *capitano* over military) and left the rest |
| **VALORIA** | **Ownership flips immediately**, loser takes `L −0.5` granular, garrison set | No model | **Designed and skipped.** A three-season transfer window with per-season costs to both sides and a free Resistance Check exists in canon; conquest does not touch it |

**What the column reveals.** The corpus's design instruction — *conquest should produce a
negotiation, not a colour change; what you leave standing determines what governing costs for the
rest of the game* — is grounded in history because **the surveyed games mostly do the colour change
too.** Valoria is not an outlier here; it is with the pack, and the pack is what the survey criticises.

---

## §12.5 People — loyalty, defection, and what the player is told

| Game | The loyalty model | Is the threshold visible? | Are the inputs visible? | Idleness cost | Population model |
|---|---|---|---|---|---|
| **Jagged Alliance 2** | Five-layer morale stack; **±25 pairwise opinion matrix**; event deltas; prejudice axes | **No** — hidden tolerance clock | **Not originally.** v1.13's fix shipped an audit tool **itemising every pairwise opinion by source** — it *exposed the models rather than changing them* | **Yes** — docks merc morale **and town loyalty** after three days without offensive action | Fixed hireable roster |
| **Jagged Alliance 3** | **All of the above compressed to:** *"liked squadmate present: +1 AP; disliked: −1 AP"* | No | Yes | — | Fixed roster |
| **RoTK** | Officer **LOY**, with a recruiter-side tell at **≤ 70** | Partly — the tell is the mechanic | Yes | **Yes** — officers want posts | Historical roster |
| **Three Kingdoms** | **Satisfaction** | No | Yes | **Yes** — idle characters lose satisfaction; *"give them something to do"* is the named top mitigation | Historical roster + generated |
| **CK3** | Opinion web, modified by **dread** | No | Partly — opaque dread interplay | **Yes** — unlanded courtiers leave at a base **2%/month** | **Ambient spawn** — ~6–7 parentless sixteen-year-olds monthly; late saves past **24,000 characters**; two community mods pulling in **opposite** directions; Paradox's fix throttled the low-value tail |
| **CK2** | Opinion | No | Partly | — | **Births plus scripted events, no ambient guest queue** — the corpus's recommended shape |
| **Triangle Strategy** | Three hidden conviction axes per character | **No** | Partly | — | Fixed roster |
| **Radiata Stories** | — | — | — | — | **175 NPCs as config rows** with a static 2–3 block schedule — *"pure spatial theatre"* gating fetch-quests, with **zero connection** to persuasion or office-holding |
| **VALORIA** | **None.** No Disposition field exists. Nearest relative is `affiliation_loyalty` (0–3), set at construction with **no mutator anywhere** — an NPC cannot change faction | n/a | n/a | **None.** An unassigned person is **inert, not restless** | **46 authored rows, zero runtime loaders.** `world.npcs` is empty in every seeded campaign; `generate_npc` is complete and has no call site |

**The two rules this table produced.** *(i)* **5/5 lanes hide the threshold and show the inputs** —
and 4/5 show that legibility is what separates a celebrated system from a resented one, decisively
JA2, whose social layer is loved and whose tactical math is resented **in the same game**. *(ii)*
**JA3, not JA2** — every lane recommended its own game's full apparatus, and JA3 is proof the feel
survives an enormous compression.

**And the structural finding the rows make visible:** every surveyed system is **primarily a
relationship model indexed by a roster.** Valoria authored the index — role, faction and convictions
on 46/46 — and none of the model: capability on 1/46, relationships on 0/46.

---

## §12.6 Recruitment and the cost of soldiers

| Game | Levy channel | Professional channel | What recruitment costs besides money | On non-payment |
|---|---|---|---|---|
| **CK3** | **Levies cost zero gold** to raise or hold — a standing entitlement drawn down, rationed **politically** (contract %, control, opinion) and **temporally** (muster travel time) | Men-at-arms cost gold **plus prestige**, carry maintenance **even while unraised**, and maintenance **roughly triples once fielded** | Vassal opinion | Men-at-arms desert |
| **Shogun 2** | **Ashigaru** — start at **−4 morale**, essentially no building requirements | **Samurai** — behind building chains | Honour | **Auto-culls units** |
| **Medieval II** | — | Retinue and buildings | — | **Requires manual disbanding** |
| **Jagged Alliance 2** | **Train militia ≈ $75/head** | **Buy regulars ≈ $440/head**, and **2× the daily upkeep** ($40–60 vs $20–30) | **Town loyalty per unit purchased** — 0.1 per regular, **0.15 per veteran**, charged **globally, not to the receiving sector** | — |
| **RoTK VIII** | Conscript, a domestic command | — | **City public order drops.** Below 50 order, conscription capacity and soldier income fall; **below 25 (revolt), conscription is unavailable entirely** | — |
| **Total War: Three Kingdoms** | — | **Unit types gated on the commander's class** — Strategists unlock ranged and siege; *"a mixed-archetype army is the intended way to access a full roster"* | — | — |
| **Heroes of Might and Magic** | — **not surveyed.** The shape the corpus lacks: accrual as a property of a **built structure in a place**, piling up whether or not you visit | — | — | — |
| **VALORIA** | **Does not exist as a distinct channel** | **`_try_muster`** — `pool = Mil + floor(W/2)`, `Ob 1`, no failure penalty | **Nothing.** No Accord cost, no order gate | **N/A — Wealth has no source.** Four write sites in the whole engine, all costs; and Muster's charge is scaled wrong at **0.01 Wealth** |

**What the column reveals.** 4/4 franchises separate the two economies; **every one resolves
non-payment somehow**; and 2/4 charge recruitment in consent as well as coin. Valoria's single Muster
is not an under-built levy — ED-FA-0009's grounding is Wallenstein, *a contractor paid regardless*,
which is the **professional** model. The action is correctly grounded and mis-labelled, with the levy
half absent and unnamed.

---

## §12.7 Mass battle, and what a person does to it

| Game | Army composition varies by… | Garrison is… | Commander's effect on the battle | Failure direction |
|---|---|---|---|---|
| **Total War** | Building chains, faction roster, general's class *(TK)* | **An assignment of the same pool** | **Lord aura** — a flat bonus | **Scale-blind**: dominates a small engagement, negligible in a large one |
| **Dominions** | Nation, recruitment sites | — | The army is **anchored to its commander** | **Scale-blind at the extreme**: *"the biggest army in the universe will rout if it is led by a single commander, and he is killed"* `[UNVERIFIED — community consensus]` |
| **Mount & Blade** | Party composition, upgrades | — | The player fights **in** the battle, in the same engine | **Fully fused**: consistent, and **the personal actor becomes irrelevant as N grows** |
| **Brigandine** | Knight + monsters under him | — | **Knights never die — they retreat.** What is permanently lost are monsters killed, **or stranded outside the knight's Rune Area when he withdraws** | — |
| **Unicorn Overlord** | Squad composition | **An assignment** | — | — |
| **Jagged Alliance 2** | Squad, gear, training | **An assignment** — and JA2's garrisons **can move offensively**, a major feature | Merc-level | — |
| **TW: Three Kingdoms** | Commander class | Assignment | **Two-tier defeat**: a general's death destroys his retinue **only if the whole army also routs** | — |
| **VALORIA** | **Nothing.** `_faction_to_unit` gives both sides one `Line` subunit, tier 2, position `(8,12)`, `advance_dir=1`, command 4, discipline 5, morale 5 — **only `power = round(Mil)` differs** | A **boolean**, written once on conquest, read once for +1 defence | `derive_command(charisma, cognition)` exists, is clamped, and its flag **defaults ON** — and the adapter sets neither attribute, so the campaign path falls back to the hardcoded 4 | **Both poles, live in the same sixteen lines**: `pc_incapacitated` applies flat regardless of size; `contested_figure_wounded` is a flat +0.15 Ob whose effect decays as `1/√N` |

**The null this table exists to make visible.** *"No precedent in this survey demonstrates a mechanism
whose personal-scale contribution is provably leverage-in-band from N=1 to N=1000+."* Every row is one
pole or the other. Well-funded teams tried.

---

## §12.8 Playing it out versus resolving it fast

| Game | Fast path | Is it the same engine? | Calibration target | Result |
|---|---|---|---|---|
| **Football Manager** | Instant result, or commentary | **Yes — three fidelities of one match engine**, and every fixture is **specific** | **Instant ≈ played** | The corpus's model of the shape that works |
| **Total War** | Autoresolve | **No — a different algorithm** | **Never published, in twenty years** | Divergence unsolved and **exploited in both directions**. The two dominant complaints are mirror images of one cause: it collapses a multi-dimensional space into a scalar |
| **XCOM** | Abstracted missions | The slate surfaces **specific** missions; you play the ones that matter | — | — |
| **Dominions / Mount & Blade** | **None** | n/a — consistency by never offering a second path | n/a | The corpus's *"don't build a second resolver at all"* is **the first option on the table, not a corner case** |
| **VALORIA** | The parliamentary bridge auto-resolves a vote | The played counterpart is the personal contest kernel | **Open** — the parity harness is the acceptance gate and does not exist | The vote is a **generic per-season roll, not the resolution of a specific motion from the slate** — which is the Total War shape, not the Football Manager one |

---

## §12.9 The resolver itself

| Game | Core resolution | Does the failure band survive competence growth? | Documented collapse |
|---|---|---|---|
| **Blades in the Dark** | Dice pool, best-die | **No** — P(fail) falls **50% → 1.6%** from N=1 to N=6, with no floor | *"Risky" degrades into "a formality"* |
| **Burning Wheel** *Duel of Wits* | Body of Argument; volleys of three; **simultaneous secret scripting**; seven manoeuvres; **compromise scaled to what winning cost** | — | Two: players converge on **Point and Dismiss**, and **Rebuttal is almost never used because too much beats it**; and at **21-vs-11** it degenerates to *"the bigger number wins fast"* |
| **Ace Attorney / Danganronpa** | Match a testimony statement to an evidence item | n/a | **One correct pair per round**; the space is pruned to 2–4 statements and 1–3 bullets. *A puzzle with one solution, not a debate* |
| **Victoria 3** | Faction arithmetic | — | Replaces argument content entirely |
| **VALORIA** | **d10 pool, TN 7 enforced by raise**; margin ladder single-owned and guarded | **Failure band: no.** 93% → 6% at fixed Ob 3. Scaling the obstacle fixes that band — **and the Partial band still collapses 0.320 → 0.093**, because its window is a fixed one-success width over a spread growing as √N | Not yet — **the manoeuvre set is unauthored**, so Valoria stands at the point *before* Burning Wheel's failure, knowing what causes it |

---

## §12.10 Expressing what the simulation knows

| Game | How interior state reaches the player | Scope |
|---|---|---|
| **Dwarf Fortress** | **Templated flavour text over a facet band** | Narrowed deliberately |
| **Nemesis system** | A **small closed trait vocabulary** plus a persistent encounter log | Narrowed deliberately |
| **Wildermyth** | **Hand-written per-personality variants** — explicitly *not procedural*, by its developers' own account | Narrowed deliberately |
| **Caves of Qud** | Abstract-then-reify | — |
| **Ultima Ratio Regum** | A culture stack | — |
| **CK2** | **Apophenia** — the player's own pattern-seeking over a rich substrate. Flagged **by its own developer as not a mechanism**; Paradox was exploring "emergence detection" because waiting for coincidence is a limitation, not a strategy | n/a |
| **VALORIA** | The Key substrate: typed, validated, append-only, with deferred-apply and honest `causes[]` | **Five Key types emitted, of 55 declared, from four call sites.** Thirteen subscribed callbacks, all typed no-ops |

**The field's own verdict, which binds every row.** Physics has graphics, so any reachable physical
state is visible at zero marginal authoring cost, and **no equivalent exists for mood, grudge, loyalty
or ambition** — named *"perhaps the hardest challenge we present"*. All three teams that hit it
converged on the same answer: **small tagged units recombined by matching.** Valoria's `ledger.py`
five families are exactly that shape, and have no writers.

---

## §12.11 Coverage, made visible

The point of `— not surveyed` cells. Games per Valoria system, in the corpus:

| Valoria system | Games with a substantive row | Thin or absent |
|---|---|---|
| Strategic actor | 9 | Mount & Blade (thin) |
| Deliberation | 5, and **the three richest mechanisms come from history because no game has them** | — |
| Settlement governance | 4 | **HoMM (absent)**, Mount & Blade (thin) |
| Conquest terms | 4, **and the model is historical** | Mount & Blade (thin) |
| People | 8 | — |
| Recruitment | 6 | **HoMM (absent)** |
| Mass battle + seam | 7 | — |
| Fidelity ladder | 4 | — |
| Resolver | 4 | — |
| Expression | 6 | — |

**Two conclusions in Parts 2–4 rest on thinner evidence than their phrasing suggests**, and this is
where to see it: the settlement-governance verdict draws on four games, one of which (Total War) is
the source of the *"no convergent answer"* null itself; and the conquest-terms model is carried almost
entirely by Venice rather than by any game. Both are stated more confidently elsewhere in this
companion than this table supports.
