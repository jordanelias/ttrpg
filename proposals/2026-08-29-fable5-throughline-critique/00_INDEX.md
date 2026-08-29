# Fable 5 throughline critique — index, verdicts, and the one finding that organizes the rest

## Status: FILED (2026-08-29) — analysis, not a proposal. Nothing here ratifies on merge.
## Version: v1 · Lane: IN (cross-cutting: reads FA, SE, WR, MB, PC, SC, FI, GO)
## Method: nine read-only adversarial steelman critics (Fable 5, `.claude/agents/valoria-critic.md`
## — Read/Grep/Glob only, so independence is structural), one per throughline, plus an independent
## verification pass by the synthesising session against the working tree.
## Reads: `proposals/2026-08-29-greenfield-systems-suite-v2/` (PR #340, 18 files) ·
## `proposals/2026-08-28-greenfield-systems-suite/ARCHIVED.md` (v1) · PRs #336–#339 ·
## `proposals/2026-08-18-epistemic-propositions-and-provenance.md` (five Jordan rulings, §10) ·
## `engine/`, `systems/`, `references/` at `606089d`

**Reading order:** 00 Index → [01 T1–T3](01_findings_T1_T3.md) → [02 T4–T6](02_findings_T4_T6.md) →
[03 T7–T9](03_findings_T7_T9.md) → [04 Owner map, keying, modularization](04_keying_and_owner_map.md)
→ [05 Independent verification and method](05_independent_verification.md)

---

## 0. What this is

Nine throughlines were assigned this session. They are **not** the repository's earlier throughlines
corpus (`proposals/2026-08-25-throughlines-and-precedent/`, `references/throughlines_meta.md`,
`systems/_architecture/throughlines_complete.md`) and must not be read through it; that corpus is
prior, differently-scoped work. The nine are:

| # | throughline |
|---|---|
| **T1** | all actions in the game are performed by characters |
| **T2** | all characters have memories, feelings and beliefs that may change over time |
| **T3** | memories are fallible, people are biased, and there can be multiple perspectives on one event |
| **T4** | no one is omniscient |
| **T5** | granular actions, demands and choices radiate and aggregate **upwards** in scale — so individual resentment can coalesce into a revolt, or a town's demand can be filtered out as irrelevant one rung up |
| **T6** | large actions ripple **downwards** in scale — a blockade or a treaty gets expressed as individuals getting excited about opportunities |
| **T7** | events across scales, political occurrences, clocks and gates are the basis for what gets debated, negotiated and argued about |
| **T8** | the world always churns — the player is not necessary for it, though they can influence it |
| **T9** | field investigations are first-class (assigned as cross-cutting, explicitly required) |

Each was given to one Fable 5 critic with read-only tools, a steelman-first instruction, and a fixed
eight-section return. This document is the synthesis. **It proposes no deletions and no mechanism.**
Under `CLAUDE.md` §0.05 it is reference: delete it and the game behaves identically.

## 0.1 The scope limit, inherited and restated

The suite states its own (`00 §0.1`): a resolution-scoped audit cannot ask whether a design expresses
the game. **This critique inherits it and adds a second.** A critique of a design cannot tell you
whether the game is good; it can tell you whether the design can *express* the throughline it claims.
Every verdict below is of that second kind. Where a critic reached for a taste judgment it is marked.

---

## 1. Verdicts

| # | throughline | verdict | the one sentence |
|---|---|---|---|
| **T1** | actions by characters | **PARTIAL** | Structural across faction, settlement and personnel; leaks at both deliberate exceptions and fails outright at the battle seam, where the contract has the faction fighting |
| **T2** | memories, feelings, beliefs | **STRUCTURALLY BLOCKED** | The feeling leg works; the belief leg is a well-designed store with **no working writer at generation, none after it, and no strategic reader** |
| **T3** | fallibility, bias, perspectives | **STRUCTURALLY BLOCKED** | Objects are ruled and correct; every *producer* of a divergent account is absent, broken or blocked, so no two people can come to disagree about anything |
| **T4** | no one is omniscient | **PARTIAL** | The player-facing half is the strongest anti-narrator architecture in the tree; the NPC half does not exist, in the suite **or in shipped code** |
| **T5** | upward aggregation | **PARTIAL** | The elite chain (conviction → practice → divergence → bloc → schism) genuinely composes; the popular half is statically unreachable and the filtering half is done by the player-attention system, not the political ladder |
| **T6** | downward ripple | **PARTIAL** | Reaches post-holders and the player; for anyone holding no post the last hop is unfilled schema, and the population's stake is conceded in one line |
| **T7** | debate and negotiation | **PARTIAL** | The event→content chain is real and traceable; there is no debate mechanic, negotiation is designed nowhere, and the return edge is blocked on a filed fork |
| **T8** | the world churns | **PARTIAL** | True today of the pre-existing strategic loop only; every mechanism the suite adds is DOC-class, and the scoring instrument has a dead leg |
| **T9** | field investigations | **PARTIAL** | Load-bearing in exactly one document, whose reverse direction targets a deleted gauge, wrongly declares a registered Key type missing, and delegates to an FI substrate of typed no-ops |

**Zero SUPPORTED. Two STRUCTURALLY BLOCKED. Seven PARTIAL.** No critic returned ABSENT, which is
itself a result: v2 has an answer of some shape for every throughline, and the failures are almost
all *wiring and ownership*, not conception.

---

## 2. The finding that organizes the other eight

Three separate stubs in the shipped engine give the same reason for not running, and none of the nine
documents names it as the thing the suite exists to close.

> **The strategic `World` has no personal-scale actor layer, so every seam that needs a *person*
> resolves against a faction aggregate or does not resolve at all.**

Read, not matched:

| site | what it says |
|---|---|
| `engine/mc_v18.py:212-218` | knot formation gets no call because *"Prerequisites … are personal-scale actor fields (Disposition, Bonds, TS) that do not exist anywhere on the aggregate strategic World — the same 'context-derivation gap' the `scene_dispatch.py` module docstring already names for combat/contest actor derivation"* |
| `engine/cross_scale/combat_bridge.py:103-111` | the bridge derives **one** field per side, `history` from `faction.Mil`, and labels the `Combatant` with the **faction id** |
| `engine/cross_scale/scene_dispatch.py` | carries the same declared `"context-derivation gap"` reason string; no live trigger ever queues a `combat` scene |
| `engine/mc_v18.py:194-202` | NPC generation likewise deferred, honestly, for the same class of reason |

This single absence is why **T1** is false at the battle seam, why **T2**'s and **T3**'s belief layer
has no perceiver, why **T4**'s NPCs read world truth (there is no person whose knowledge could be
partial), and why **T9**'s investigations cannot be conducted. It is also the strongest argument
*for* the suite: `01`–`04` are precisely the person layer whose absence these stubs name. **The suite
builds the missing thing and never says so** — no document cites `mc_v18.py:212`, and `13`'s build
order motivates Phase 3 by dependency ordering rather than by the four honest deferrals it unblocks.

**Consequence for the handoff.** `13 §5` Phase 3 ("people and posts") is currently justified as *"population bounds what generation may produce"*. Its real justification is stronger and is measurable: it is the phase after which `form_knot`, `derive_parties` and `generate_npc` stop being honest deferrals. That is an execution artifact under `CLAUDE.md` §0.2, and it is the only one in the plan that converts four stubs at once.

---

## 3. The cross-cutting register — findings reached independently by two or more critics

`CLAUDE.md` §10 records independent rediscovery as the strongest available signal. These were reached
by critics who could not see each other's work.

| # | finding | found by | severity |
|---|---|---|---|
| **X-1** | **The credence ghost.** `08 §6.3` — the suite's only post-generation belief writer — deposits into `credence.<proposition>`, a gauge `02 §6.2` cut outright (`02:464`), citing a contract row that no longer exists and misquoting `02:521`'s "confidence" as "credence" | **T2, T3, T9** (three-way) | **BLOCKER** |
| **X-2** | **Belief is a store with no producer and no strategic consumer.** No working writer at generation (`npc_memory` unbuilt), none after it (X-1), no perception edge, and no action-selection function anywhere reads it | **T2** (writer), **T3** (perception), **T4** (consumer) | **BLOCKER** |
| **X-3** | **`legitimating.*` has no producer**, so `09 §6.4`'s `rising` — the suite's only mass actor — is statically unreachable, and the falsifier built for the identical v2 defect checks module names, not tag keys, so it cannot catch this one | **T1, T5** | **BLOCKER** |
| **X-4** | **Two objects named Exposure.** Canon's is per-territory, Cover-thresholded, reset each season and on leaving (`fieldwork_exposure.md:27-34,55-56`); the suite's is a person-scoped decaying gauge that survives reassignment (`01:520`). `00 §7.1`'s own rename rule was applied to `footing` and not here | **T4, T9** | **DEFECT** |
| **X-5** | **Two or three stores for "what an agent knows"** — `Holding`, the `information` gauge (which structurally cannot be false, and has no knower), and FI's reliability-tagged evidence | **T3, T4, T9** | **DEFECT** |
| **X-6** | **`09 §1.2`'s three-failure list is stale** — it reports allegiance has no edge kind with a magnitude, which `01`'s O-7 shipped | **T1, T2** | **wording** |
| **X-7** | **Q-5 is not closed locally.** `fm.posture`'s per-season `acceptance.support` deposit is the one declared exception, and it forms a posture→support→footing→posture-gate loop that appears in no loop table | **T5, T6** | **DEFECT** |
| **X-8** | **There is no community rung.** The throughline names character → community → settlement; the suite's ladder starts at settlement, and canon has a community level it does not read (`settlement_layer_v30.md:171`) | **T5**, echoed by **T6**'s residents concession | **GAP** |

---

## 4. The blocker register — what makes a throughline unreachable as written

Ordered by how cheaply each closes.

| # | blocker | throughlines | cost to close |
|---|---|---|---|
| **B-1** | X-1, the credence ghost | T2, T3, T9 | **an edit.** Retarget `08 §6.3` row 4 to a `Holding.confidence` deposit; delete the stale dependency note |
| **B-2** | X-3, `legitimating.*` unproduced | T1, T5 | **one row.** Name a depositor (`08`'s Defy or an `11` row) and register the Precedent key namespace |
| **B-3** | `08 §6.3` declares a registered Key type missing. `scene.investigation_resolved` **exists** (`key_type_registry_v30.md:881-897`) with `finding`, `subject_id` and the `witnesses` field `08` calls undefined | T9 | **a grep the suite's own `00 §9.2` correction box already mandates** |
| **B-4** | No decision function reads belief — in the suite **or** in `systems/factions/sim/faction_action.py:208-273` | T2, T3, T4 | **a design call**: wire the capped term `01 §3.4` already licenses, or strike `01 §4.3`'s "and beliefs" |
| **B-5** | No declaration path for bloc- or faction-owned projects, killing change C's schism → founding-claim → charter chain at step one | T1 | **a sentence** in `09 §11` and `06 §3.4` |
| **B-6** | The battle seam has the faction fighting, not a character | T1 | **re-specify** `12 §3.3`'s ctx contract to carry the commander post-holders |
| **B-7** | The emission budget. `11 §3.3` passes the tick-wide sum to `13`; `13` never received it. The cap **raises**, it does not clamp | T8 | **a table** in Phase 0. See §5 for the correction to its severity |
| **B-8** | P0-7, the Turmoil victory leg — and it is four dead clocks, not one | T8, and every "unmeasured" claim in the suite | already Phase 0 in `13`; the finding widens |

---

## 5. Where this critique corrects its own critics

Per `CLAUDE.md` §0.1, an agent result is not taken at face value. Four sharpenings, each read-verified
by the synthesising session and detailed in [05](05_independent_verification.md):

1. **B-7 is smaller than T8 framed it.** The 64-emission cap is live by default (`ECHO_TRANSPORT`
   defaults ON, Jordan 2026-07-08) and does raise rather than clamp — but the tree emits **164–229
   Keys per *campaign*** today (`engine_clock.py:47`), roughly 3–5 per season against a per-tick cap
   of 64, and the constant is explicitly *"CALLER-SUPPLIED … NOT canonical"* and tunable via
   `ECHO_EMISSIONS_PER_TICK_MAX` (`echo_transport.py:96-103`, ED-IN-0026). It is an **unowned
   reconciliation item**, not an architecture blocker.
2. **P0-7 is wider than the suite states.** No code writes *any* clock generically; `IP`, `PI`,
   `Strain` and `Turmoil` are all initialised and never written.
3. **`Key.causes` is stated backwards by P0-11.** Two of the three emitters pass `[]` **with comments
   explaining no upstream Key exists to cite**. It is a wiring gap, not an authoring lapse.
4. **The unbounded-gauge hole is two gauges.** `prac.tps` has *both* floor and ceiling null and is
   named nowhere in the suite.

T4 also corrected itself on request, downgrading "impossible" to "expressible but unwired" for
belief-reading advance terms. That correction is carried.

---

## 6. Curation — the consolidated verdict

**KEEP, and these are the suite's best work.** `04 §4.0`'s acceptance gate (the acted-upon as actor —
the same preference function read from the other side, so one object genuinely does two jobs) ·
`10 part 2 §6`'s three invariance properties with the per-candidate RNG substream, which is what makes
"the world is 100%" honest · `01 §3.1`'s `Holding` with the provenance/`support_refs` split, which
executes rulings P2 and P3 exactly · `06 §4.2`'s footing as one derivation evaluated at many nodes ·
`09 §5`'s verb-free obstruction · `12 §5.2`'s requirement that a motion's subject be a real tag ·
`13 §6`'s guard table, which correctly forbids guarding the suite's own prose.

**MERGE.** The two Exposures (X-4) · the two or three knowledge stores (X-5) · `11`'s `route_cut` tag
into `07 §7`'s yield or cut it as a tag with no reader · `11 §3.3` and `10 §1.3` into one tick-budget
table owned by `13` Phase 0 · the two investigation Key ids.

**CUT.** `08 §6.3`'s `credence` target (B-1) · `09:137-139`'s stale sentence (X-6) · `07:394`'s
`Memory` reference · `01 §3.1`'s "has an in-suite answer" phrasing for the hashing rule, which
oversells an open blocker that `13` P0-11 states accurately.

**RULE, at lane level and not Jordan's.** Name the `legitimating.*` producer · close `signal(s, world)`
into an enumerated list on `09 §3.1`'s pattern · add the bloc/faction declaration path · resolve
`08 §3`'s `fa.gate` residual · state whether the personal-scale scene layer is exempt from the verb
budget.

---

## 7. What genuinely needs Jordan

Nine critics were instructed that most questions do not survive `CLAUDE.md` §0's five tests. **Six
returned "none".** Three items survived, and one is already filed.

| # | question | why it survives | raised by |
|---|---|---|---|
| **J-1** | **May a false belief ever determine an NPC's action outright, or only bias weighting inside `RELATION_SHARE_MAX`?** | Ruling P3 made lies *representable* and is silent on *decisive*; `01 §3.4` and the ruled proposal pull opposite ways; no precedent exists because this is the tree's first belief-consuming selection architecture. Exploit-proof NPCs and deceivable NPCs are materially different games | T3 |
| **J-2** | **Is "community" a required rung** — do resident communities aggregate individual grudges into collective acceptance, or is the presence-gauge plus two-scalar flattening the intended model? | Canon's community level is live (`settlement_layer_v30.md:171`); the suite flattened it without arguing the flattening; the bloc precedent is elite-scoped by construction | T5, T6 |
| **J-3** | **May an off-board polity act through an actorless world-event row**, or must every agentive pressure trace to a character? | T1 as stated has no off-board carve-out; `09 §12` rejects weather-shaped agentive pressure for populations while root cause E demands an outside. The two options are a diplomacy layer versus a pressure dial | T1 |
| *(filed)* | **ED-SC-0002**, the Debate→Domain-Echo keying fork | Already open. It blocks T7's return edge; one ruling unblocks ED-SC-0007 and closes the AU-5 seam | T7 |
| *(filed)* | **ED-SC-0024/0026**, strict parity vs AI-played baseline | Already open. It decides whether player ignorance has any cost at all (T4) | T4 |

**J-1, J-2 and J-3 are the same question at three scales**: how much may a person's *interior* — what
they believe, what they resent, whether they are a person at all — determine an outcome, against how
much is settled by position. That is one design decision with three faces, and it is the decision this
suite has been circling since v1's root cause C.

---

## 8. What this critique did not do

- **No steelman pass for subtraction.** `references/throughlines_meta.md:233-238` requires an
  independent pass that steelmans an action *for* KEEP before any subtractive verdict is final. §6's
  CUT list is therefore **candidates, not dispositions** — the same hold PRs #337 and #339 carry.
- **No coverage of `03`, `07` or `12` at critic depth** in several lanes; each critic's coverage note
  records what it read, and those notes are preserved verbatim in `01`–`03`.
- **No campaign measurement.** Every gain in the suite is unmeasured and stays so; `tools/balance_oracle.py`
  is the instrument and **B-8 must close before any control run is trustworthy**.
- **No ledger row.** Per `CLAUDE.md` §0, the adversarial pass is a stage, not a deliverable. Three
  rows would qualify under `needs_jordan` (§7); they are surfaced here by location rather than
  appended, and whether they become rows is Jordan's call, not this document's.
