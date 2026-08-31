# JORDAN RULING, 2026-08-31 (this session) — THE ACT BUDGET IS ~5, NOT 1

**Verbatim:** *"please note for the ideal proposal that i expect a character to get ~5 playable scenes
per season, which may mean that they get ~5 actions."*

## WHAT IT OVERTURNS IN PR #350

The suite states the opposite twice, in bold, as a universal:

- `02_ONTOLOGY.md` §8.1 — *"One act per person or cohort per season, universally. No office, rank or
  holding changes it, ever."*
- `07_THE_PLAYER_AND_THE_PERSON.md` §4 — *"ONE ACT PER PERSON OR COHORT PER SEASON. UNIVERSALLY."*,
  headed *"the act economy — one act, universally, and why it is the whole political economy"*.

It is load-bearing in at least four further places:
- `05_WORLD_CHURN.md` §2.1 — the `wear` tax is priced in person-seasons *"drawn from the one-act budget"*.
- `06_EMERGENT_NARRATIVE.md` §8 row 19 — *"a season in which the interesting thing is what you did NOT
  get to"*, whose N-line is *"one act per person, universally"*.
- `07` §4 — `dispatch` costs BOTH parties an act and names ONE person; the Duke's leverage is that his
  one act moves other people's acts.
- `02` §8.1 / `07` §4 — *"One allowance: the act. One cap: items a sitting processes."*

## THE CONTRADICTION THIS RULING LANDS ON — ALREADY PRESENT, UNNOTICED BY THE SUITE

`06_EMERGENT_NARRATIVE.md` §4.5, the Slate funnel:

> *"Roughly 190–200 candidates resolve per season; 6 reach the slate; 4 are acted on. Over a 50-season
> campaign: ~9,750 candidates resolve, ~300 surface, ~200 are played."*

**300/50 = 6 surfaced per season. 200/50 = 4 acted on per season.** The attention layer was already
built on a ~4-act season while the act economy declared one, and no document in the suite reconciles
them. The adversarial pass found 16 MAJOR defects and did not find this one.

**So Jordan's ~5 does not import a foreign number into the design — it resolves an existing internal
collision, and it resolves it toward the number the Slate was already using.** 4 (Slate) → ~5 (ruled)
is a calibration; 1 (act economy) → ~5 is the overturn.

## WHAT SURVIVES THE CHANGE, AND WHAT DOES NOT

**Survives — the arguments were never about the number 1:**
- *Personal attention is scarce identically at every rung; institutional throughput scales with the
  establishment.* A Duke having ~5 scenes and a fisher having ~5 scenes preserves this exactly.
- *If the pool for an act by remit comes from the establishment, the act does too.*
- *An order is a telling; compliance is the hearer's own `choose`.* No loyalty stat.
- *The cohort exploit is priced rather than forbidden* — individuating buys people, not acts.
- Scarcity as the generator of politics — 5 scenes against ~200 resolving candidates is still a funnel
  of ~2.5%, and the surplus is still the point.

**Does not survive unamended:**
- `dispatch` costing both parties their WHOLE season. At a budget of 5 it costs each 1 of 5, which is a
  materially different political economy — a Duke can redirect up to five people by name per season, or
  spend his season doing one thing five times. **That fork is now a live design question the suite
  never had to ask.**
- The N-line of row 19 — *what you did not get to* — weakens at 5 and needs restating in terms of the
  candidate:act ratio (~200:5) rather than the allowance being 1.
- Every place the suite prices a cost in "the one-act budget" is off by 5×, including the `wear` :
  restoration ratio's political framing in `05` §2.1.
- **`seat_items` was deleted on the argument that it and `capacity(date)` are "one quantity seen from
  two sides" under "one allowance: the act".** With five allowances that identity is no longer obvious
  and the deletion needs re-argued — this is a deletion that may have to be reversed.

## THE OPEN QUESTION THE RULING ITSELF FLAGS

Jordan wrote *"~5 playable scenes per season, which **may** mean that they get ~5 actions"* — the
hedge is his. **Scene and act are not yet established as the same unit.** Three readings, materially
different:
1. **1 scene = 1 act.** Budget is 5 acts. Simplest; the Slate's 4-acted-on becomes 5.
2. **A scene CONTAINS acts.** 5 scenes, each admitting one or more acts — the act budget is then
   ≥5 and uncapped per scene, and `capacity` moves to the scene.
3. **A scene is the fidelity unit, an act the resolution unit.** 5 scenes are what the player is
   *asked to choose in*; NPC acts are not scene-bounded at all — which would reintroduce exactly the
   player-only mechanism `07` §1 forbids ("there is no player model").

**Reading 3 is the one to watch:** the suite's central refusal is that the player and the NPC run the
same function with the same budget. If "scene" is a player-side pacing unit and "act" is the universal
one, the two must be reconciled explicitly or the every-rung rule breaks.

**This is a Jordan question, and it survives all five of `CLAUDE.md` §3's tests** — it is not
superseded, not irrelevant, not answered by a design document (the suite says the opposite), not
answered by precedent, and the architecture does not force one reading over the others.

---

# ADDENDUM — THE PRIOR ART EXISTS, IS CANONICAL, AND IS RICHER THAN THE RULING
*(added after lane L reported; every figure verified against the snapshot primary)*

**`designs/architecture/player_agency_v30.md` §4–§6 — `## Status: CANONICAL — approved 2026-04-17`.**
Verified verbatim at `snapshot/designs/architecture/player_agency_v30.md:55`:

> *"The scene action budget as triage mechanism. The player has 3–5 scene actions per season. There are
> always more opportunities than actions. **Choosing is the gameplay** — not executing, but deciding what
> to attend to and what to let pass. Opportunities not pursued do not wait — they resolve through NPC AI
> and clock advancement without player input, often in ways the player would not have chosen."*

**Jordan's ~5 is the top rung of a ratified three-rung ladder.** Not a new number — the existing one.

| difficulty | scene actions / season | slate size |
|---|---|---|
| Hard | 3 | 7–9 |
| Normal | 4 | 5–7 |
| **Narrative** | **5** | **4–5** |

Modifiers (`player_agency_v30` §6.2, and §5.1's Standing ladder, verified at `:152` and `:154`):
`+1` at Standing 4–5 · `+2` at Standing 6–7 · `+1` in a Knotted NPC's territory ·
`−1` at Stamina 0 · `−1` at 2+ Wounds.

## THE THREE THINGS THIS SETTLES THAT THE RULING ALONE DID NOT

**1 · A SCENE IS A CONTAINER; THE ACT IS "PURSUE THIS OPPORTUNITY."** (§6.3) *One scene action = one
scene opportunity pursued. A scene contains 1–3 mechanical interactions.* An extended scene costs **2**.
So Jordan's hedge — *"which may mean ~5 actions"* — resolves as **reading 2 of the three I flagged**:
5 scenes, each admitting 1–3 interactions, at a variable cost of 1–2 scene actions. Not 5 atomic acts.

**2 · THE BUDGET WAS NEVER UNIVERSAL, AND THE ARCHIVE MADE THAT CHOICE DELIBERATELY.** Lane L's F-L-4:
NPC factions run **exactly one** action per season off a 7-level priority tree; individual named NPCs
have **no action budget at all** — they generate Scene Slate entries that cost **the player's** budget
(`npc_behavior_v30` §8.11, the "World→Player bridge"). **This is reading 3, the one I flagged as the
hazard, and the corpus took it.** It is precisely the player-only mechanism `07` §1 forbids.
**This is now a genuine fork for Jordan, not a detail:** either the shape's symmetry survives and the
archive's asymmetric economy is rejected, or the asymmetry is accepted and "there is no player model"
is false. Note also that Standing `+1`/`+2` means **rank changes the budget** — which PR #350 forbids
in terms (*"No office, rank or holding changes it, ever"*).

**3 · FIVE HAS ALREADY BEEN STRESS-TESTED AND IT SATURATED.** Lane L's F-L-5, test **R-39**
(`designs/audit/2026-04-28-political-dynamics-session/15_stress_tests_batch3.md`): at a Year-4 season
with **5** scene actions, mandatory content alone — 1 leader crisis + 1 heresy investigation + 3
Concern-driven NPC-Outreach scenes — consumes **the entire budget, leaving zero discretionary actions.**
Filed as a Robust/Smooth violation: *"NPCs always have the initiative — the player reacts rather than
directing their own political agenda."* The proposed fix was **a slate-generation policy change**
(demote Concern-Outreach to explicitly deferrable), **not a bigger budget.** ⚠ That patch sits in the
never-promoted "doc 12" chain; the mechanism it stress-tested (Outreach at Priority 3, capped 3/season)
*did* reach canon — so **the failure mode is live against canon while its fix is not.**

## WHAT ELSE THE ARCHIVE ALREADY BUILT AROUND THIS NUMBER

- **Witness Mode** (§4.2 Step 1) — when mandatory scenes exceed the budget the player picks which to
  attend; the rest resolve at **0 cost** via a Read/Appraise at Ob 1 (*not* auto-success), one narrative
  input, NPC-AI resolution, and explicitly **no Domain Echo and no Momentum/Coherence change.** A
  ready-made answer to "what happens when 5 isn't enough" that neither drops content nor inflates the budget.
- **One between-scene currency, by explicit decision** (`integration_proposal_v30`): Combat has
  Wounds/Stamina, Contest has Composure/Concentration, Thread has Coherence, Fieldwork has Exposure —
  each a *within*-scene resource — and *"the scene action budget handles the between-scene resource
  limit"* for all of them. A second between-scene resource was proposed and **rejected as double-penalising.**
- **The budget is fractal.** Inside an investigation scene the player has a *scene time budget of 3*
  over a 4–9 node graph, and the doc says outright it is *"not a new resource — it is the scene action
  budget expressed spatially."*
- **Companions do not consume it** (`integration_audit_v1/v2`) — *"the answer must be no"*; they assist
  within the scene's own time budget.
- **The budget was load-bearing on two other closed debts** — ED-545 (only 5 Zoom-In triggers) and
  ED-547 (fieldwork resource cost: *"scene action budget IS the fieldwork cost"*). Changing the number
  reopens both.
- **Season phase structure**, independently reconstructed by four documents: Briefing → Duty Assignment
  → Slate Generation → Personal Phase (the 3–5 actions) → Strategic Phase → Accounting → Aftermath.
  The budget applies to **exactly one phase**.

## REVISED BOTTOM LINE
PR #350's one-act economy is not merely contradicted by Jordan's ruling — **it is contradicted by a
CANONICAL 2026-04-17 design the suite never read**, which supplies the number, the slate that feeds it,
the modifier table, the overflow mechanism, the currency-layering rule, and a stress test showing where
it breaks. Under `CLAUDE.md` §0.05 that document is *reference*, not mechanism — but as reference it is
the best-developed answer in the corpus, and PR #350's `16` §4 admits the suite never read 138 of 162
documents. **This is one of them.**
