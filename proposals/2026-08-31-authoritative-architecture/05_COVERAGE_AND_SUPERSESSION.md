# 05 · COVERAGE, SUPERSESSION, DUPLICATION, GAPS

## Status: PROPOSED (2026-08-31). The measurements in §1 were **taken by running commands over the
## working tree** and are reproducible; everything else here is judgment. `CLAUDE.md` §0.2 applies.

---

## §1 · COVERAGE, MEASURED

The current head opens with a confession: *"of 123 proposal documents over 200 lines, 108 are cited
nowhere."* **That figure is stale, and the truth is worse in the way that matters.**

| metric | the head's figure | **re-measured** |
|---|---|---|
| proposal documents > 200 lines | 123 | **133** |
| documents cited by the head's suite | ~15 | **30** |
| **uncited** | 108 | **103 — 77.4% by document count** |
| **uncited by LINE WEIGHT** | not stated | **67.7% — 51,111 of 75,453 lines** |
| `research/` coverage | not stated | **0%** |
| the two governing Jordan rulings (ED-IN-0200, ED-IN-0201) | not stated | **0 of 2 cited** |

**Why the numbers moved, and why both are true.** `01_ARCHITECTURE.md` in the working tree already
carries a self-correction section written *after* the confession, which answers the confession's five
bullets and finds nine more documents through a citation shorthand a filename-grep misses entirely.
**The head is better-read than its own warning says, and still reads under a third of the corpus.**

> **The number that matters: the head has accounted for under a quarter of the corpus's
> architectural content — and the unread remainder includes the only part that executes.**

**The mechanism of the failure, which is worth more than the number.** Every audit in that exercise —
two review rounds, five parallel runners, a 982-line keys audit — **was derivative-facing.** They
checked each other, so **agreement read as corroboration when it was correlated error with one root.**
That is precisely the failure the design's own corroboration rule exists to prevent, arriving in the
process that produced the design. **Citation count is not coverage.**

**What this suite did differently, and its own limit.** Six of the fourteen sweeps read *code and
registries* rather than proposals, and the five adjudicators were pointed at the tree rather than at
each other. That is why the ruling in `04` §1 could be made at all. **But this suite has not read the
other 103 documents either.** Its "there is no X" claims carry the same scope limit, and §5 names what
to read next.

---

## §2 · THE SUPERSESSION MAP

**Use this to know what to read and what to ignore.** Rows are ruled, not hedged.

### The design line, #337 → #344

| document | status | what survives |
|---|---|---|
| `research/valoria_systems_integration_master_v1.md` (+parts) | **ANCESTOR, uncited, still live** | **Proposal 4 — "stop iterating factions, iterate people" — is the direct ancestor of the Person/Office/Tenure model.** Never cited by the head |
| `research/valoria_game_precedent_companion_v1.md` (+parts) | **ANCESTOR, uncited** | the precedent patterns; the isolation risks it names are unanswered |
| `research/cross_scale_action_catalogue_v1.md` | **LIVE REFERENCE** | **the act catalogue.** It is the authority on what acts exist; the design's twelve-act table is a subset |
| `proposals/2026-08-28-greenfield-systems-suite/` (#339) | **ARCHIVED** by its own adversarial pass | its resolution mechanics survived intact into v2; its *scope* is what died |
| `proposals/2026-08-29-greenfield-systems-suite-v2/` (#340) | **THE CONTENT QUARRY — not superseded** | **world events, ambitions, the slate.** Its mechanisms are more worked than the head's abstractions |
| `proposals/2026-08-29-fable5-throughline-critique/` (#341) | **LIVE** | the nine throughlines are the spine everything downstream answers to |
| `proposals/2026-08-29-valoria-from-scratch/` (#342) | **LIVE, partly superseded** | `03_knowledge_telling_investigation.md` (980 lines) **owns the claim vocabulary and was never read by any prior pass** |
| `proposals/2026-08-31-ideal/10_SUPERSEDING.md` (#343) | **SUPERSEDED where `ARCH` §10 departs; source-of-truth elsewhere** | everything the head does not change |
| `proposals/2026-08-31-ideal-v2/` (#344) | **THE HEAD** | superseded by this suite only where `06_ADJUDICATIONS.md` rules against it |
| `proposals/2026-08-31-integration/` | **PARALLEL SYNTHESIS, uncross-cited** | a second, same-day effort that never cites the head. Read before trusting either as complete |

### The tree the design line never read

| document | status | why it matters |
|---|---|---|
| `systems/_architecture/key_substrate_v30.md` | **CANONICAL** | the pseudocode half of `04` §1's ruling |
| `systems/_architecture/propagation_spec_v1.md` | **CANONICAL** | the coarse spine the six-step loop refines |
| `systems/_architecture/holonic_container_doctrine_v1.md` | **CANONICAL** | the containment doctrine; in tension with "containment is an edge" |
| `systems/_architecture/scale_hierarchy_v1.md` | **RATIFIED** | already draws case-by-case the distinction `Tenure` generalizes |
| `systems/_architecture/governance_ripple_substrate_v1.md` | **REFERENCE / ANCESTOR** | the event deck's own governing spec; direction superseded by three later generations |
| `systems/settlements/governance_play_redesign_v1.md` | **REFERENCE / ANCESTOR** | its Part 3 NPC ambitions are richer than the head's bare `choose` |
| `godot/godot_conversion_strategy_v1.md` | **PROPOSED, governing, with open Jordan items** | `STRAT:213`'s autoload ruling is now forced |
| the four 2026-04-18 `godot/` docs | **STALE**, each says so | read for intent only |

---

## §3 · THE DUPLICATION REGISTER

**Independent convergence and re-invention are different findings and are separated here.** The first
is evidence a design is right; the second is evidence a process is broken.

### Independent convergence — the bankable results

| # | mechanism | converged where | weight |
|---|---|---|---|
| 1 | **Iterate people, not factions** | `research/` Proposal 4 · the throughline critique · the head's Person carrier · **Jordan's ED-IN-0201** | **the strongest result in the corpus.** Four routes, no citation between them |
| 2 | **The act economy — one act per person; an office's throughput is its establishment's** | `proposals/2026-08-30-fixes/02_the_act_economy.md` · the head's D-2 · Proposal 4's repair | **three independent derivations of the same conclusion** |
| 3 | Deferred-apply barriers with a write class spanning two phases | the head's write classes · **OF-7, running in `keys.py` since 2026-07-07** | design and code arrived separately |

### Re-invention — where the process failed

| # | mechanism | already designed at | state |
|---|---|---|---|
| 4 | the actorless event channel, incl. Altonian pressure | `…-v2/11_world_events.md` (715 lines) | **self-corrected** in the working tree |
| 5 | ambition's carrier with derived-at-read `progress` | `…-v2/09_ambitions_and_arcs.md` + part2 (1,065) | **self-corrected** |
| 6 | the claim source, the predicate vocabulary, `investigate` | `…/03_knowledge_telling_investigation.md` (980) | **the worst instance** — cited 3×, read 0×, which made it *look* covered. Cost: two FATAL errors and an invented verb standing where six shipped acts already were. Mostly corrected |
| 7 | **slate and salience — how anything is put in front of a decider** | `…-v2/10_the_slate_and_salience.md` + part2 (1,152) | **⚠ ACKNOWLEDGED UNREAD AND STILL UNREAD.** The least-closed hole in the head |
| 8 | Event / provenance / append-only log | **`engine/substrate/keys.py`, executing** | ruled in `04` §1: compose, never duplicate |

**Genuinely new, and it is the head's real contribution:** the four-carrier abstraction, the
`Tenure` unification of five separately-shaped existing mechanisms, and Jordan's Partition as a
schema column. **These have no precedent anywhere in the corpus.**

---

## §4 · THE GAP REGISTER

The head filed thirty gaps. Re-ruled, with additions.

### Closed — do not re-file these

| id | closed by |
|---|---|
| `relevance(c, q)` undefined | **defined in full** in the knowledge document; only `q`'s *producer* is open |
| the predicate vocabulary has no roster | **fourteen forms enumerated**, with a stated test for a fifteenth |
| an actor dying at MATTER after declaring an act | **cannot arise** — MATTER runs before DELIBERATE |
| the commitment ladder's licence column | closed by a merged edit the head had not re-read |
| `Profile`'s arithmetic | **defined** — presence, density and footprint all have formulas; only the record's field list is open |
| the `piety_track` owner ("three docs disagree") | **dissolved** — the contract layer already ships both scopes as separate modules |

### Open, and blocking

| id | what is missing | who it blocks |
|---|---|---|
| **G-01** | **the question `q`'s producer** — type, origin, lifetime | view assembly; salience; **and eviction, which is why "evict lowest salience" was uncomputable** |
| **G-13** | **`World`'s record** | every refusal is written against it. **The first thing a typed port must declare** |
| **G-14** | `Rung.matter`'s structure | four things are addressed by name inside an unstructured field |
| **G-12** | `Event`'s fields | resolved in principle by composing onto `Key`; the mapping is unwritten |
| **G-07** | `season_factor`'s distribution | `yield`, every season. **May already be answered by `11_world_events.md`'s rate bounds** |
| **G-05** | where the channel store lives | a minted person's plausible past |
| **G-06** | the cohort's construal spread | every cohort witnessing |
| **G-18/G-19/G-20** | establishment size; the empty judging set; the Coherence-0 officeholder | D-2's residue and two self-declared falsifiers |
| **G-23** | `Office.conferral` cycles — a cyclic path never reaches root and **silently excludes** the office | office clusters |
| **G-27/G-28** | the exchange form; re-denominating coercion into typed `stores` | every purchase; every retinue cost |

### Added by this reconciliation — gaps the head never filed

| id | what is missing | found by |
|---|---|---|
| **N-1** | **the Partition's membership test** — closed here by `01` §2.8's schema column, but the column itself is unwritten | this suite |
| **N-2** | **fixed-point representation** for `condition` and `stores` — specified in `03` §4, exported nowhere | the Godot lane |
| **N-3** | **the tenth attribute.** Jordan ruled ten; the registry ships nine and the tenth is unnamed. **Shipped Godot code already names `Recall` in ~19 places** | the registry and corpus lanes |
| **N-4** | **the NPE per-issue stance store** drifts every campaign and has no owner in the design | the registry lane |
| **N-5** | **no home for personal combat, social contest, threadwork or mass battle** in the twelve-act table | the execution lane |
| **N-6** | **`Faction.L` is written as a base descriptor at ~31 code sites and ratified as a derived, no-setter aggregate.** A live contradiction between canon and running code | the PR lanes |

---

## §5 · WHAT TO READ NEXT, RANKED BY EXPECTED CHANGE

1. **`…-v2/10_the_slate_and_salience.md` + part2 (1,152 lines)** — *how anything gets put in front of
   a decider.* The head has no answer and knows it. **Highest expected change of anything unread.**
2. **`…/03_knowledge_telling_investigation.md` (980 lines)** — owns the claim vocabulary, view
   assembly, corroboration, concealment. Partly absorbed; read it whole before touching WITNESS.
3. **`…-v2/11_world_events.md` (715 lines)** — the actorless channel with rate bounds. Likely closes
   G-07 outright.
4. **`systems/_architecture/key_substrate_v30.md`** — the pseudocode half of the substrate ruling; read
   before building `witness`.
5. **`research/valoria_systems_integration_master_v1.md`** — the uncited ancestor. Its corrections were
   never applied because it was never read.
6. **`…-v2/09_ambitions_and_arcs.md` + part2** — the ambition carrier, before anything gives a person
   a goal.
7. **`proposals/2026-08-31-integration/`** — the parallel synthesis nobody cross-cited.

> **An uncited ancestor is an unread ancestor, and the corrections it contains were not applied.** That
> is the whole cost of the coverage problem, stated as one sentence.
