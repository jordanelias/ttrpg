# Part A — the passes: what the audit found

## Status: **PROPOSED (2026-09-12, ED-IN-0217). HELD BACK FROM RATIFICATION-ON-MERGE, IN FULL.**

⚠⚠ **SUPERSEDED BY `proposals/2026-09-12-emergent-narrative-primitives-v2/` (same session, same
`ED-IN-0217`).** This set applied the wrong test: it disposed of mechanics on **architecture rules** and
**implementation facts** as though those refuse an idea, which they do not — and it never cited **`R2`**,
the ruling that makes every refusal *instrumental, not terminal* and requires each to be **argued** against
five terminal properties (`references/design_rulings_2026-09-06.md:37-50`). Its facts are largely sound and
its citations reproduce; **its verdicts do not follow from them.** Kept as the audit trail. Read
`…-v2/02_THE_RESCORE.md` for what changed and why, and `…-v2/01_THE_TEN.md` for the set that replaces this
one.


Companion to `00_INDEX.md`. This file carries the evidence; `02_PROPOSALS.md` carries what is
proposed on it. Nothing here ratifies on merge, closes a row, or moves a `CURRENT.md` row.

**What was audited.** Four uploaded research documents, as candidates for Valoria — not as
scholarship:

| | document | what it carries |
|---|---|---|
| **D0** | *Emergent Narrative in Games: A Research Compendium* | the survey — Areas 1–8, a 14-primitive taxonomy in four sets, five recommendations |
| **D1** | *Emergent Narrative: Mechanical Specifications* | the companion — Parts 0–IX, a six-item **minimum viable emergent-narrative machine**, and **fourteen numbered requirements** |
| **D2** | *Thirteen Strategy Games Across Seven Design Qualities* | 33 primitives in eight families (A1–H4), seven axes, five under-occupied regions, **six proposals** P1–P6, a playability rubric |
| **D3** | *Citizens, Settlements, Factions — Nine Titles* | a primitive catalogue in six families, **eight graded transferables**, **nine directives**, three absent couplings |

Three independent Opus NERS passes ran `skills/ners/SKILL.md` in full against the working tree, one
per document group (D0+D1, D2, D3). A structurally read-only Fable node then turned the findings on
the game (`02_PROPOSALS.md` §0 and `00_INDEX.md`). Every claim below was re-verified by hand before
being carried; four were **corrected or refuted**, and those are recorded in `03_PROVENANCE.md` §3
rather than quietly dropped.

---

## §1 · THE FINDING THE THREE PASSES CONVERGED ON, INDEPENDENTLY

> **Every store-shaped primitive in all four documents is already a carrier in Valoria's tree, and
> almost every one of them is unwritten. Adopting one adds a second empty carrier beside a first.**

The three passes reached this from three different documents and stated it three different ways.
It is the reason the proposal set in `02_` is five objects rather than fifty, and why four of the
five are a single cell, a single argument, a single effect body, or a deletion.

**The measurement that makes it concrete.** Run on this tree, 2026-09-12:

```
build_world(0):  persons 3 · live `hold` tenures 0
                 stance   {p_carin: [], p_bailiff: [], p_warden: []}
                 capability {p_carin: {}, p_bailiff: {}, p_warden: {}}
```

In the world the loop actually drives, **no person holds a post, no person has a disposition, and
no person has a competence.** Those are three different fields, with three different holes against
them, and they are empty simultaneously and for one reason.

At corpus scale the same shape, measured over 86 buildable worlds and 258 persons:

```
DISTINCT PERSON-SIDE ELIGIBILITY SETS: 1  (size 28)
persons holding a live `hold` Tenure:  0
BUDGET DISTRIBUTION (actions/person):  {5: 258}
```

**A faction head, a settlement governor and a person with no post are, in the code, the same seat.**
Under `skills/ners/SKILL.md` §6 that is not *one option dominates*; it is **one seat exists**, and
it is why `R-04` reads `not_met`.

And at the strategic scale, a seeded `engine/mc_v18.py` campaign runs to completion — `winner=Crown`,
season 50, 33 battles, 119 scenes, 180 keys — with:

```
npcs={} convictions={} beliefs={} knots={} practitioners={} comovement_deck.remaining=[]
governor_id=None legitimacy=0 popular_support=0 facility_tier=0 suspicion=0 stub_hits=100
```

The carriers are all there. Nothing fills them.

---

## §2 · THE FALSE N-LINES — the product of the pass

`skills/ners/SKILL.md` §3: a false N-line is *an object whose claimed lost possibility actually
survives the cut, because something already ruled in provides it.* The pass is graded on these.

**Twenty-seven, across the four documents.** Each row: the primitive · the possibility it claims ·
the Valoria object that already provides it · which of §3's five disqualifiers fired.

### 2.1 · From D0/D1 — emergent narrative

| # | primitive | claimed possibility | already provided by | disq. |
|---|---|---|---|---|
| 1 | **Mixed success** (I.2, req. 7) | a complication band as the modal outcome | `engine/autoload/dice_engine.py:227-300` `degree_from_net` — four bands off a margin, single owner by Jordan's 2026-08-14 ruling. `PARTIAL` is `0 ≤ margin < 1`, a real band | **1** |
| 2 | **Affliction History, +2 weight** (III.4, req. 5) | an agent's past rewrites its future distribution | `write_matrix.yaml:147-153` `(Person, axis_count)` emits `axis.incremented`; `:196-202` `(Person, scar)` emits `scar.taken`. **And the distribution is already `softmax(score/tau)`** over `project(p)` at `decision/choose.py:283-297` — a conviction move *is* a distribution rewrite | **1, 4** |
| 3 | **Stale information** (VII.6, req. 10) | an agent holds a belief the system knows is false | `queries/person_q.py:82-88` `LedgerReader.read` returns the stored value, most-recent-then-most-confident, never world truth; no match is `UNKNOWN`, never `False`. Rationale at `rosters.yaml:365-368` | **1** |
| 4 | **Values-vs-facets contradiction** (III.2) | desire and capacity conflict, and the conflict is data | `AX-3`, `architecture/meta/01_AXIOMS.md:111-115` — *"Evidence moves what is held true. Argument and consequence move what is held right."* Two fields, one carrier: `Person.convictions` vs `Person.ledger` | **1** |
| 5 | **The storylet** (V.1) | content + prerequisites + effects, graph emergent from state | `verb_table.yaml:10-11` — the fold, by name, across 38 rows, with a loader that refuses an unlisted `writes:` | **1** |
| 6 | **Delegation as character generation** (VII.5) | the delegate becomes a character by failing attributably | `AX-1` + `T-h` (`01_AXIOMS.md:71-74, 237`) — institutions act only by a named person; every delegate is already a `Person` running `choose` | **1** |
| 7 | **The persistence taxonomy** (VI.1) | eight kinds of state, each enabling a different story | seven of eight are already rows of `write_matrix.yaml` with emission names | **1, 2** |
| 8 | **The L4D four-state director** (IV.3) | reliable dramatic pacing over a simulation | **cut, with a name and a date** — held back at `narrative_engine_design_v1.md:119-124` fork 8, then **ratified subtract-only by Jordan 2026-07-05, ED-IN-0011**: the Light Function *"can never inject content, shape the RESOLUTION of any scene, accelerate a clock, or emit a pressure-bearing Key"* | **3** |
| 9 | **Visible clocks / beats** (IV.4–5, req. 9) | the player can see the drama's state | **cut** — the NOT-list's *"no arc labels ever surfacing (C2)"*, C2 lint on all lifecycle/salience state labels, and v2 §6's *"**never a meter** … no quantized horizon ever surfaces — no counts-remaining, no dates-certain"* (`:394-402`) | **3** |
| 10 | **Story sifting's surface** (V.4) | retrospective meaning; the world had a plot all along | **vetoed by Jordan** — *"the arc-recognition surface **Jordan vetoed** stays internal (C2)"* (`narrative_engine_design_v1.md:132-133`). A sifter that may not surface has no narrative product | **3** |
| 11 | **Meier's RNG massage** (II.5) | randomness reads as fate rather than noise | **already shipped** — `systems/combat/combat_engine_v1/config.py:295` `UPSET_FLOOR=0.05`, `[DESIGNER RULE — Jordan; ED-PC-0036]` — **and registered as a measured defect**, `H-119`. See §3 | **1, 3** |
| 12 | **The variety trap** (VIII.3) | expressive range is parameter space ∩ player discrimination | **already carried by name** — *"the three anti-oatmeal defenses"* (`narrative_engine_design_v1.md:49`), *"anti-oatmeal defense 1"* (`v2:96`), in a RATIFIED document | **3** |
| 13 | **PRD / pity timers** (II.2, II.4, req. 6) | bounded, legible waiting | **no producer, and the absence is a ruling** — every Valoria draw is keyed `H(seed, tick, subject, purpose)`, *"no counter, no service"* (`seam/wrappers/sigma.py`, `04` PART D row 35), because a stream would make every roll depend on the count of prior draws. **PRD requires a since-last-success counter on a stream** | **2** |

### 2.2 · From D2 — thirteen strategy games

| # | primitive | claimed possibility | already provided by | disq. |
|---|---|---|---|---|
| 14 | **A5 · vote as the resolution mechanism** | political opposition without a scripted antagonist | **it executes** — `systems/social_contest/sim/parliamentary_vote.py::run_parliamentary_vote` (d10 pool TN 7), `engine/cross_scale/parliamentary_bridge.py`, reached from `engine/mc_v18.py`, tested at `engine/tests/test_parliamentary_action.py`. Canon side gives Mandate-weighted votes, two thresholds, a Sacred Veto with cooldown, and **stated NPC agendas** — the thing D2 says Bannerlord lacks | **1** |
| 15 | **B1 · opinion as a modifier-stacked scalar** | every relationship in one comparable unit | `Person.stance` (`state/carriers.py:371`), read as §F2's second scoring term at `decision/choose.py:77-86`; gated `social: true` at `state/world.py:352-357`. **The store is there, the consumer is there, the gate is there. The missing thing is a verb** | **1, 2** |
| 16 | **H4 · rule-bound automaton opposition** | credible opposition with no risk of the layer being switched off | `AX-1` + `architecture/PLAN.md:438` — every character runs the same `choose`; a player-only mechanism is forbidden; `AX-2` denies everyone privileged access. **There is no separable opposition layer to switch off** | **1** |
| 17 | **G2 · character-selected ambitions** | AI characters behaving differently for stated reasons | a `commit` Tenure to an OUGHT Proposition, read by Q4 `need` every season — `requirements.yaml` R-06: *"that IS the ambition mechanism, and it is why Carin acts in a quiet season"* | **1** |
| 18 | **F1 · action-point budget** | forces triage and, at scale, forces delegation | `engine/season/decision/budget.py:17-60` — `base + office_bonus × live holds − body-band − travel-leg`, floor 1, `scene_budget = 5` | **1** |
| 19 | **C5 · contract personnel with expiry** | a pacing clock independent of the in-world calendar | **ruled, verbatim** — `T-n`, `01_AXIOMS.md:1138`: *"Some relations should not end at the holder's whim — a term of service, a wardship that lapses at majority. But an end condition nobody declared is **a clock nobody wound**, which `T-c` forbids. **So the opening act declares the terms**."* | **3** |
| 20 | **C1 · hard-capped named agents** | an anti-blobbing brake built into personnel | `AX-5` + demand-driven CENSUS (`01_AXIOMS.md:172-181`) — *the world may never individuate a person nobody's act demanded.* A **derived** cap, which is what R7 prefers to a stipulated one | **1** |
| 21 | **D3 · site selection as a durable decision** | map variation between playthroughs | `write_matrix.yaml:294-300` — `Rung.exists`, steps `[RES]`, emits `rung.founded`, **no producing verb**; `Site.exists` the same. The gap is R4's four unbuilt churn routes, not D3's | **2** |

### 2.3 · From D3 — nine titles

| # | primitive | claimed possibility | already provided by | disq. |
|---|---|---|---|---|
| 22 | **Punished loyalty-switching** (its top political transferable) | betrayal drama with no AI | `systems/factions/reference/faction_politics_v30.md:86-95` already rules it, harder — defection is graded **severe, 2–3 ranks** (ED-776), with no pass-through of intermediate ranks, **mentor relationships voided immediately**, Hall Tier and Livery cleared within a season, and a persistent **Dishonored** flag at Dismissal. CANONICAL, Jordan 2026-04-17. Re-proposed 2026-09-10 as P6 and graded `paper`. ⚠ **Reference, not mechanism** (§0.05) — no code reads this ladder | **1, 3** |
| 23 | **The ageing cohort** (its top demographic transferable) | boom, bust, and a story the player authored | `Rung.envelope` (`carriers.py:560`), its matrix row (`write_matrix.yaml:288-293`), the CENSUS step that owns it, and the full proposal at `proposals/2026-09-10-…/02_PROPOSALS_SUBSTRATE.md:142-254`, graded `paper` | **3** |
| 24 | **Work areas with caps / auto-allocation** | large populations shaped without micromanagement | **cut** at `proposals/2026-09-10-…/05_COLLISIONS_AND_RESIDUE.md:157-160` against `AX-1`: *"auto-allocation is nobody deciding"* | **3** |
| 25 | **Fiction wrapped around the hostile system** ("the best ratio in the catalogue") | change who the player blames, at near-zero cost | **no producer** — there is no authorless hostile quantity to wrap. `AX-5`'s three motions, and *"a quantity that advances on its own with no author is A SHADOW ACTOR"* | **2** |
| 26 | **Write the half-strength spec first** (Directive 5) | an autonomy setting that can be reduced rather than switched off | `fixtures.py:328` `fan_out_mode` swept `total / all_five / presence_only`; `fixtures.py:229` `choice_temperature` swept `0 / 0.1 / 0.25 / 0.5 / 1.0`; and `observers_for` **refuses an unrecognised mode** so a sweep can never silently read its control. This is `CLAUDE.md` §0.1 pt 4 as shipped code | **1** |
| 27 | **Skill → satisfaction → output** | a double-reinforcement advancement loop | fails **its own falsifier** before reaching Valoria — the document says it *"is a pure bonus with no opposing pressure, at which point correct play is obvious and the decision evaporates"* — and no satisfaction field exists | **5** |

**Twenty-seven free cuts, partitioned by which disqualifier fired.** Sixteen on **1** — the
carrier already exists, on an object that can also be contested, planted or refuted. Seven on
**3** — the cut was already made, by Jordan, with a date, and applied. Three on **2** — no producer,
so the possibility was never reachable. One on **5** — the residue is a flat bonus, and the object
was the wrapper. No row fires **4** alone.

---

## §3 · THE MECHANISM THE DOCUMENTS RECOMMEND, WHICH VALORIA SHIPPED, AND WHICH BROKE

This is the single most useful negative result of the pass, and it is worth its own section.

D1 §II.5 recommends Meier's *"unholy alliance between the player's suspension of disbelief and the
designer's willingness to defy both logic and the laws of maths"* as the mechanism that makes
randomness read as fate. **Valoria has it.** `systems/combat/combat_engine_v1/config.py:295`:

```python
UPSET_FLOOR=0.05,   # [DESIGNER RULE — Jordan; deliberate, NOT an emergent mechanic. Tagged ED-PC-0036.]
```

applied at `wrapper.py:493` — `if result!=0 and rng.random()<cfg['UPSET_FLOOR']: result = -result`.

The code's own comment concedes the consequence before any audit reached it: *"the one place the
engine deliberately OVERRIDES its own emergent outcome — the trace stream emits `engagement_end
felled=X` and then `fight_result winner=X`, **with no in-model event corresponding to the
reversal**."*

`H-119`, tier 1, grade **measured**: over 300 seeded fights **the reported winner is the FELLED
fighter in 6.06%**; cross-confirmed from an independent quantity, 28 of 595 losers are not at
health 0.

**And D1's own VII.2 is the test that condemns it.** *"A dwarf who does not haul the stone because
he is praying is a character. A unit that does not move because of pathfinding failure is a bug.
The identical mechanical event is narrative or defect depending entirely on whether the system can
account for the refusal in terms of the subordinate's own state."* Here the winner is the fighter
the model felled, and nothing in the model accounts for it.

**The two halves must be kept apart.** The *disposition* is Jordan's — the constant carries
`[DESIGNER RULE — Jordan]` and ED-PC-0036, and `H-119` says so. The *defect* is not a disposition:
two surfaces the same seam returns contradict each other on ~5% of decided fights, and `H-119`
records it as answerable **by precedent** rather than escalation — Jordan's 2026-09-04 ruling that
the combat engine determines the result and the caller accepts it. See `02_PROPOSALS.md` P4.

---

## §4 · WHAT A RATIFIED LINE REFUSES, AND ON WHAT GROUNDS

⚠ **This section previously read "WHAT VALORIA CANNOT ADOPT AT ANY PRICE" and asserted "these are not
cost judgments." Both claims were wrong, and the error has a shape worth naming, because it is the
easiest one to make in this repository.**

**Only Jordan can say *never*.** A ratified line does not close a question; it says **what would have
to change and who decides**. And `CLAUDE.md` §0.05 is explicit about the direction of authority: *"If
canon and code disagree, decide and then CHANGE THE CODE — never declare the prose authoritative."*
**A fact about how the tree is currently written is therefore not a refusal of anything.** It is a
price. Presenting it as a refusal rejects a mechanic for the convenience of the incumbent
implementation, which is the opposite of a design judgment.

**So every row below carries its GROUNDS — and the cut that matters is NOT "ruled versus unruled". It
is whether the commitment is about THE GAME or about THE CODE.** (RULED by Jordan, this session:
*"Even the design commitments are to be ignored if they are directly attached to code (eg no
aggregates on a query)."*)

| grounds | what it is | what it may do to a gameplay idea |
|---|---|---|
| **G — a commitment about THE GAME** | what the player experiences; whether a narrator exists; what is allowed to act; what the player is shown | **may refuse it.** This is a real design judgment, and it is still **Jordan's to revise** — citing one opens a conversation, it does not close one |
| **A — a commitment about ARCHITECTURE** | how state is **stored or computed**. R7/`L3`'s *"every aggregate is DERIVED, none is PUSHED"*; `carriers.py:579/586`; a `tie` on the lower id vs two edges; a comparator's signature | ⚠ **NOTHING. NO VETO AT ALL.** **A player cannot tell a field from a function.** Whether Approval ends up a stored number or a computed Query is settled *after* the gameplay question, and may never settle it |
| **I — an implementation fact** | *"nothing produces it"*, *"no code reads it"*, *"no step exists in which it could run"*, *"0 of N cases carry one"* | ⚠ **NOTHING.** Not a refusal — **a work estimate** |

⚠ **Two of the three grounds cannot refuse anything, and between them they were carrying most of this
suite's negative verdicts.** The single largest category in the seven documents — spendable political
currency and settlement/faction meters, and everything derived from them — was refused on **A**. That
refusal is **void**, and the family returns to be judged on what it does for the game. `§4.1` below
records what that reopens.

**Five rows in the previous version of this table were wrong.** Each is corrected in place and marked
⚠. **Every one of the five made the design look more closed than it is.**

| the primitive | grounds | the line, and what it actually refuses |
|---|---|---|
| **Any scheduler that makes the world act on a person** — MTTH as a hazard rate, the RimWorld storyteller, the L4D director, PbtA fronts, Façade's beat manager | **G** | **`AX-1`**, `01_AXIOMS.md:71-74` — *"**ONLY A PERSON ACTS.** No institution, no faction, no threshold, no clock, no container, and no engine is ever the subject of a decision."* And `00_THE_METHOD.md:79` — *"whose act makes this happen? ⚠ **nobody's** → **you have found a narrator. Remove it.**"* This refuses what the mechanic **does**, not how it is coded |
| ⚠⚠ **A spendable political currency, or any settlement/faction meter** — Approval, Resolve, Impatience, Hostility, legitimacy, unrest | **A** — ⚠ **NOT A REFUSAL** | **R7** (`design_rulings_2026-09-06.md:169`) — *"no magnitude carrier is admitted at any scale. **Every aggregate is DERIVED, none is PUSHED**"* — and `carriers.py:579/586` are **architecture**: they rule on where a number LIVES. ⚠ **This row has now been wrong twice, each time less wrong, and the second attempt is instructive.** It first refused the idea outright. It was then narrowed to *"refused as stored; the derived form is ruled in"* — still wrong, because that lets a storage rule shape a gameplay verdict. **The correct verdict is that R7 has nothing to say here.** Approval, Resolve, Impatience, Hostility, legitimacy and unrest are **live candidates to be judged on what they do to play**, and the field-or-function question is downstream of that decision, not upstream of it. **This is the largest reopening in the suite** — see `§4.1` |
| **A threshold that produces an outcome** — RimWorld's mental breaks, Darkest Dungeon's resolve check at 100, Imperator's tyranny tail | **G** (from `AX-1`) | **`T-b`**, `01_AXIOMS.md:284-287` — *"A threshold may change what can be chosen; it may never produce an outcome… a threshold that produced an outcome would be an actor."* **And the substitute ships:** a band crossing raises a **Question** (`queries/world_q.py:234-238`) and a person chooses. The axiom records **19 of 50** surveyed arcs wanting exactly that |
| ⚠ **Salience-ranked *memory retention*** — not salience-ranked selection generally | **G** on its reason; **A** on its enforcement | `07_DYNAMICS.md:182-184` — *"the correct bound is **who could have perceived this**, never **how important it is**… a narrator deciding what matters."* ⚠ **The previous row said "salience-ranked selection, ANYWHERE", and that is false of this tree.** Questions **are** ranked before a budget-bounded person answers them: across sources by `rosters.yaml`'s `question_sources` order, *whose own note calls that order **semantic***, and within a source by lexicographic order over content hashes — measured deciding `qs[0]` in **801 of 1,068 deliberations** (`queries/world_q.py:250-269`, `H-54`). What is refused is ranking **a memory** by importance. Ranking **a question** is shipped, and its within-source half is **undeclared**, which is a live hole rather than a design property |
| ⚠ **Scheduled decay or recovery of a social quantity** — mood drift, approval decay, relationship cooling | **I** — ⚠ **NOT A REFUSAL, and the claim was also FALSE** | ⚠ **The previous row read *"structural by phase membership — THERE IS NO STEP IN WHICH A RESTORING TIMER COULD RUN"*. There is such a step, and it executes.** MATTER matures act-declared stages at a later tick and writes `Record.matured` (`loop/matter.py:55-109`) — *"the only mechanism in the design by which one season's act reaches into a later one WITHOUT anybody acting again"*, and it **stops if the maker is gone**. So the honest statement is two-part: an **unauthored** drift is refused by `AX-5` (**G**), and an **act-declared** recovery is *licensed*, lawful, and merely **unbuilt for social quantities** — `Tenure` has no `term` field (`verb_table.yaml:421`). This row was the clearest case of an implementation fact wearing a refusal's clothes |
| ⚠ **An UNWOUND clock** — a hazard rate, a drift nobody set | **G** | **`AX-5`**, `01_AXIOMS.md:151-165`: three world motions — matter, bodies, the fading of memory. *"Nobody wound any of the three, and you cannot bribe silt."* ⚠ **The previous row said "a fourth clock of ANY KIND — a loss timer, an election clock, a Queen", and `T-c` licenses exactly those.** `T-c` (`:304-316`) states the consequence as the design's **best single property**: a wound clock can be *"bribed, delayed, burned, or killed."* **And the licensed form ships:** a `Date` written only by `convene` (`write_matrix.yaml:98`, `loop/effects.py:188`), firing at `loop/calendar.py:31`, raising a Q1 question at `world_q.py:196`. An election clock **with a nameable convener is admissible.** The axiom also flags that its list of three may be incomplete — `03_PROVENANCE.md` §3 |
| **Auto-allocating labour to zones** (D2's missing rung; D3's work areas) | **G** (from `AX-1`) | a zone that allocates persons is a container deciding a person's options. Already cut at `proposals/2026-09-10-…/05_COLLISIONS_AND_RESIDUE.md:157-160` |
| **Surfacing dramatic structure in the interface** — progress clocks, tension meters, act labels, countdowns (D1 req. 9) | **G** | the NOT-list (`narrative_engine_design_v1.md:117-121`), C2 lint, `v2:394-402` — *"**never a meter** … no quantized horizon ever surfaces."* **RATIFIED, ED-IN-0011.** Note this refuses a **readout**, not a mechanism: the quantity may exist as a Query and simply never be shown |
| **A director that shapes rather than rations** | **G** | held back for Jordan, then **ratified at subtract-only, ED-IN-0011** — and severed against its own reflexivity by fixture F8: *"if forecasting C raises P(C), the loop is live and the build fails"* |
| **A world-truth readout on the main view** (D3 Directive 2's second test) | **G** | `04_CODE_ARCHITECTURE.md:751` §C.11 — *"there is no referee, so the engine inherits the referee's SECOND job"* — and `:765`: *"**The engine owes the ARITHMETIC of what the character already holds, and nothing else.**"* R7: *"the player sees their character's **ESTIMATE**, never the true aggregate"* |
| **Any GM-arbitrated element** | **G** — the project's premise | `ARCHITECTURE_V2.md:94` refuses *"a GM / referee adjudicating"*, 3 cases; `CLAUDE.md`'s head: **there is no GM — the engine resolves everything.** This is why parts of the canonical prose layer cannot be lifted: several of their mechanisms name a GM as the resolver |

**Tally of the grounds: 9 G · 1 A · 1 I.** Nine rows are genuine design judgments about what a mechanic
does to the game, and Jordan may revise any of them. **Two rows refuse nothing** — and one of those two
was the ground for the corpus's single largest family.

---

### §4.1 · WHAT THE VOID DISPOSALS REOPEN

The two rows above that refuse nothing were not doing small work. **R7 was the stated ground for eight
further disposals in `05_VALORIA_PLOTTED.md` §7**, and those return with it:

| the mechanic | what it was disposed of with | what it is now |
|---|---|---|
| **Spendable political currency** (`A1`) | *"a stock is a magnitude carrier"* | **open.** To be judged on whether spending standing to move a decision is a good decision to give a player |
| **Approval slope with a punitive tail** (`A4`) | *"the slope is a stored aggregate"* | **open on the slope**; the *tail* stays refused on `T-b` (**G**) — a threshold may raise a Question, never produce an outcome |
| **Currency as the victory condition** (`A3`) | *"no score exists"* | **open.** The disposal was an `I` |
| **Dominance with a gap condition** (`E1`) | *"needs a score"* | **open** — and `standing_of` already computes a gap, so the shape is present |
| **Tile painting with severable supply** (`D1`) | *"a stored aggregate on a Rung"* | **open** |
| **The inverse-linked meter triangle** | *"three stored global meters… the tree's most comprehensive refusal"* | ⚠ **open, and it may be the corpus's strongest single offer.** The suite's own note calls it the documents' *"most sophisticated pressure design"*. Three quantities that move against each other is a **gameplay** proposition; where the three numbers live is not |
| **Twin-population tension** | *"two stored aggregates"* | **open** |
| **Threshold immigration on standing** | *"a settlement approval aggregate"* | **open on the standing**; the *threshold firing the migration* stays refused on `T-b` (**G**) |
| **Scheduled recovery of a social quantity** | *"no step exists in which a restoring timer could run"* | **open, and the claim was false** — MATTER matures act-declared stages (`loop/matter.py:55-109`) |

**Nine mechanics, reopened by correcting the grounds rather than by any new argument.** Each must now
win or lose on NERS, on emergent narrative, on the decision it gives a player, and on whether it can be
said in this design's vocabulary — which is the only test that was ever supposed to apply.

⚠ **One qualification that keeps two of the G rows honest.** The Churn Engine is a `.md`, and `grep`
for `light_function|stake_horizon|convergence_candidate|foreclosure_countdown` over every `.py` in the
tree returns **zero files**. Under §0.05 it is **reference for game mechanism**; what it binds as is
**agent instruction**, and a ruled refusal of a build is exactly that. So the director and
dramatic-structure rows bind *a session from building these*; they do not describe the game's code,
because there is no code. `AX-1`, `T-b` and the memory-comparator refusal are different in kind — they
are carried by axioms with theorems, by a comparator signature, and by a `Question` that executes.

**How to read this section, stated because two earlier versions invited the opposite.** A row marked
**G** is a place where adopting the mechanic means asking Jordan to revise a commitment about the game —
a real conversation, and sometimes one worth having. A row marked **A** or **I** is **not a refusal**:
the mechanic is open, and what looks like a wall is either a storage decision that comes later or an
estimate of work. **The only question this suite should ever have been asking is whether a mechanic
improves the game.** Where these tables reached for a ratified line instead, they were answering an
easier question.

---

## §5 · WHAT THE DOCUMENTS GOT WRONG ABOUT A GAME LIKE THIS ONE

Three findings that run the other way, and that a reader should have before trusting the documents'
own rankings.

**5.1 · D2's one-clock finding is a confounded measurement, and it fails on the document's own
text.** §5.4 reports single-clock proposals averaging 29.3 against two-clock at 24.7, and concludes
*"run one clock unless you can state what the second buys."* The arithmetic checks; the grouping
does not. **P6 states in bold that it cuts the tactical clock** — *"**The tactical clock is cut.**
Battles resolve by commitment and officer rating in one step… Single clock."* **P2 has no tactical
layer at all** — *"Monthly turns over roughly fifty years; one continuous hex continent."* The true
split is **one two-clock proposal against five one-clock proposals**, and that one — P5 — is ranked
**second at 29**, above every member of the other arm but P1. The finding inverts on its own n=1.
What actually separates the arms is C6, failure-mode exposure, for reasons the document states and
that have nothing to do with clocks. This is `CLAUDE.md` §0.1 pt 1 exactly — a result whose
*statistics* were attacked and whose *setup* was not.

**And the repaired version does bind Valoria, but not where it was aimed.** Valoria's scene/season
pair is not two clocks: `w.tick` advances **once** per season (`loop/driver.py:356-361`). One clock,
two granularities — and the second granularity was **bought with a measured control**, R-03's flip
to `met` on an execution, with the price reported and not netted off. What *is* a second clock is
invisible to the document's Axis VII: **`engine/mc_v18.py` runs a complete, independent second
season loop and `engine/season/` never imports it** (`requirements.yaml` R-04: *"the two are not
joined"*). That is not a strategic-plus-tactical split, which buys tactile drama. It is **two
implementations of the same object**, which buys nothing and costs §7.3's *calculations consistent
in methodology*. The second clock Valoria should be asked to justify is the second campaign
simulator.

**5.2 · D3's "named and not recommended" is inverted for this repo.** It grades
belief-with-provenance *"the most interesting primitive in the set and the one most likely to fail
in practice, because it puts the entire game state inside hidden beliefs."* In Valoria the game
state is **already** inside per-person beliefs by axiom (`AX-2`), the field already exists
(`Claim.source`), and **the consumer already exists and is starved** (`decision/options.py:443-464`).
Its stated mitigation — *"display the belief structure and make the uncertainty concern the accuracy
of the player's reading rather than the existence of the information"* — is `§C.11`'s explanation
contract, ruled. The primitive D3 ranks last is the one Valoria is closest to and gains most from.
See `02_PROPOSALS.md` P1.

**5.3 · D1 refutes its own Part II and does not propagate the refutation.** Part II files randomness
shaping under **Set A, the generative substrate**, and makes it requirement **#6** of the machine.
Then VIII.1 says: *"**Randomness shaping (A.5) has no effect without D.** …PRD, shuffle-bags, and
RNG massaging do nothing to the fabula — the same events occur, at the same long-run rates. They act
entirely on the player's **reading** of the sequence."* That is one fact pattern ruled two ways
(`SKILL.md` §4 C4), and the symptom of a missing evaluator: nothing in the taxonomy asks *whose
state does this change?* **Requirement #6 is in the wrong group of the fourteen**, and the document
says so itself. Scoped narrowly per §8: this strikes Part II's **set membership**, not Part II. The
settled member — that bounded waiting is legible — stands.

---

## §5A · TWO FINDINGS THE PASSES DID NOT PRODUCE, FOUND WHILE VERIFYING THEM

Both were found by checking a commissioned pass's citation rather than carrying it, and both bear
directly on `02_PROPOSALS.md`. Neither is a new object; both are measurements.

**5A.1 · `standing_of` is `H-116` at a second site, and it is starved on two axes, not one.**

`decision/options.py:412-434` — `agreement(told, own)` pairs claims **by predicate**, and only over
a roster: `own_by = {c.predicate: c for c in own if c.predicate in PERSON_PREDICATES}`.
`rosters.yaml:232-241` gives that roster as `[heritage, grade, church_standing, office, residence]`
— *"the five things `marks[]` records about a person."*

But `witness.py:133` mints `predicate = e.kind` — event kinds — and the `W-B` observation channel
mints `stores:<kind>`, `condition`, `contain.path:<to>`. **Neither deposit channel ever mints a
person predicate.** So `own_by` is empty in every run, `paired` is `0`, and `standing_of` returns
`condition_scale` — **whether or not anything is ever stamped `told_by`.** Verified: `PERSON_PREDICATES`
has exactly one consumer, and **nothing writes `Person.marks`** anywhere in `engine/season/`.

⚠ **This corrects an over-claim this session nearly made.** A source stamp at `witness.py:121` is
**necessary and not sufficient**; reviving `standing_of` needs three producers, not one. It is
reported here as a measurement and is **not proposed as a repair** (`02_PROPOSALS.md` P1 is scoped
accordingly).

**And the shape has a name and a precedent.** `epistemic.py:74-82` records the same defect class
already measured and already repaired at a different site:

> *"`H-116` then measured the consequence: over 4,800 deposited claims **the two vocabularies were
> DISJOINT** and zero claims were falsy, so clause 4 could not fire in any run and the candidate set
> was invariant with respect to everything that happened in the simulation. The predicate is
> **DERIVED from the form** now… so there is **one namespace** and the write side has a name to aim
> at."*

`standing_of` is that shape, unfixed. Under `CLAUDE.md` §0.1 pt 5 it is a **pattern defect**, and it
satisfies the predicate — it feeds `Sensation`, which feeds `choose`, so it is load-bearing on the
game and not on this repository's process. The repair direction is precedented; the repair is not
one object, and this set does not pretend otherwise.

**5A.2 · `verb_table.yaml:711` carries a rule that ratified Layer 1 supersedes.**

`04_CODE_ARCHITECTURE.md` §A.3 is titled *"Fifteen differences from the chain, each with its forcing
clause"*, with columns `the chain | this | forced by`. Row 9, at `:178`:

| # | the chain | this | forced by |
|---|---|---|---|
| 9 | `tie`/`knot` stored once on the lower id | **two directed edges**; strain is a Query | §E.1.3 |

`01_AXIOMS.md` §E.1.3 (`:1185-1200`) gives the argument, and it is the one a reader of D1 §VI.1
would reach for independently:

> *"They are stored once, on the lower-id endpoint, so under `AX-4` the **other** person owns nothing
> and by `T-m` cannot end a relation they are inside. **Whether you can walk away from a bond would
> depend on an id comparison**, which is not a thing the fiction can express."*
>
> *"The shape that satisfies both rules: **two directed edges, each owned by its subject.** A tie is
> a **regard**, and regard was never symmetric… It also buys the most interesting case for free:
> **I have cut you off and you do not know it**, which is `AX-2` at the level of relationships."*

**`engine/season/verb_table.yaml:711` still reads `requires_note: "stored once, on the lower id
(§15.1)"`.** It is not a misbehaving mechanism — nothing executes a note — but it is a superseded
instruction sitting exactly where whoever writes the effect will read it, and an effect written from
it would implement the rule Layer 1 corrected.

⚠ **And the finding is not that the asymmetry is a defect.** It was found, argued and ruled here
before this session; presenting it as new would be `SKILL.md` §3 disqualifier 3, and an earlier draft
of this document did so before the citation was checked. The ruled shape is also **what D1 §VI.1
describes** — *"Relationship | Dyadic scalar (often asymmetric)"* — so the document and the axiom
agree, and the ruling's stated yield, *"I have cut you off and you do not know it"*, is D1 §VII.6's
asymmetric-knowledge case arriving free and already ruled in.

---

## §6 · THE MINIMUM VIABLE MACHINE, SCORED AGAINST THE TREE

D1 §VIII.4's six items, scored first-hand:

| # | item | Valoria | at |
|---|---|---|---|
| 1 | ≥2 interacting rule systems whose interaction is not enumerable in advance | **yes** | `EFFECTS` × `requires_typed` × `witness` × `questions_for` |
| 2 | agents with modelled internal state that **explains** their behaviour | **no** | `H-62` — no verb writes any `Person` interior field |
| 3 | **compliance < 1.0 with the shortfall attributable to that state** | **half** | `decision/choose.py:111` yes; attributable **no** — R-08's own words |
| 4 | ≥1 channel of permanent state | **yes** | `Record`, `Tenure.until`, `World.log`, and death (`_eff_kill` deletes the Person) |
| 5 | randomness with memory on a frequently-observed event | **no, and refused** | keyed draws; no stream |
| 6 | a surfacing mechanism that **names causes** | **half** | `Event.causes[]` populated at every write; **no render exists** |

**Item 3 is D1's own nomination for the most-often-missing item, and it is the one Valoria misses.**
Two documents and one acceptance file, written apart, name the same absent object:

> D1 VII.2 — *"The design lever is therefore **compliance below 1.0, where the shortfall is
> explained by a modelled interiority**."*
>
> `engine/season/requirements.yaml` R-08 — *"A tie is now broken by the **DRAW, which is not the
> person** — it is the absence of a reason, not a reason of theirs. That is the whole of why this
> row does not go `met`."*

That convergence is the strongest independent corroboration this pass produced, and it is what
`02_PROPOSALS.md` is organized around.

---

## §7 · THE INTERROGATION — seven questions turned on the game

The three passes audited the documents. A structurally read-only node
(`.claude/agents/valoria-critic.md`: `tools: Read, Grep, Glob` — no Write, no Edit, no Bash) then
took their findings and interrogated Valoria with them. Its answers are carried into
`02_PROPOSALS.md`; what follows is the shape of each, with the residual that survived it.

**Q1 · Is the dead scorer the deficit, or a symptom?** **A symptom — and upstream is one hole that
was not any of the three named.** No question source produces a person as a referent, so no
candidate carries one as a subject, so `stance_toward` can never fire toward anybody. §0 of
`02_PROPOSALS.md` carries the chain and the measurement. **Verdict: two holes, not three and not
one** — the referent grammar (whose faces are the dead stance consumer, the reach bottleneck, and
`tie / knot`'s futility) and `H-71`, which is genuinely separate. *Residual, stated by the node
itself:* the claim was derived from the four question sources' code, not run; this session then ran
it, and it reads zero over 177,170 candidates.

**Q2 · Does the documents' evidence warrant `W-F`'s invented magnitudes?** **Direction is already
the tree's; magnitude is nobody's.** `AX-3`, `H-62`'s supplied shape and the ruled band order supply
the direction without the documents. Adopting the catalogue for magnitude imports what the catalogue
disowns. See `02_` P5, which is much smaller than its first draft as a result.

**Q3 · Is `U4`'s Gumbel sampler a defect under D1's attribution condition?** **No — it is a declared
stopgap**, and the repair is neither removal (which restores the alphabet) nor giving it a reason
(which would change §F2's ruled shape and is Jordan's). The repair is to land the second live term
so the draw's share shrinks, with the `tau = 0` control as the instrument. *Residual, and it is
sharp:* the tree's own docstring calls the keyed noise a **"TASTE… stable across a season"** — a
season-scoped per-candidate valence with no verb producer, re-drawn on the tick, which is
functionally the interior `H-62` refuses, and `AX-3` licenses a clock only to **remove**, never
revise.

**Q4 · Which second clock should Valoria be asked to justify?** **Neither the one a pass named.**
Under `T-c`'s own definition the scene round is not a clock — it advances nothing and `w.tick` moves
once. And `mc_v18` is not a second clock either; it is a second **owner** of one, and a second
**world**. `02_` M3 carries it, including the sharper form: the two engines disagree about whether a
sub-season timestep exists at all.

**Q5 · Which half of the band result is Jordan's?** The boundary, exactly: the **ladder** is his
ruling, the **values** are his tuning, and what is structural is that `Person.capability` has one
writer and it zeroes — *"a two-die cast should never overwhelm; the defect is that everyone is a
two-die cast."* `02_` M1.

**Q6 · Would any of these primitives make `NPC RUNS` or `ARC ENDS` computable?** **No.** `RUNS`
waits on authored `exercises:` rows and a real cast — content, which no primitive can author.
`ENDS` waits on contest results, binding decisions and ending predicates, and the binding-decision
half is blocked on `H-71`. **The one primitive that would flip `ENDS` for a named set — a threshold
that produces an outcome, reaching the eight `THRESHOLD` arcs in `ENDINGS_CLASSIFIED.yaml` — is
refused by `T-b`.** `W-F` makes neither bar computable; it makes outcomes richer inside cases the
bar cannot yet grade.

**Q7 · What should be refused, that a reader of these audits would take anyway?** **Salience-ranked
memory** — carried in full at `02_PROPOSALS.md` §R, including why it is seductive (the tree records
the symptom it appears to cure) and why forgetting is load-bearing fiction rather than a bug.

⚠ **The node recorded one limit on its own answers and it is material:** the four documents are not
in the working tree, so every claim it makes about *what the documents say* is carried at the
passes' report, while every claim it makes about *Valoria* is verified at `file:line`. Q2 and Q7 are
therefore answered against the tree's warrant inventory rather than against the documents' text.
