# 03 — Method, and this analysis's own corrections
## Status: process record, 2026-08-25

This file exists because the analysis makes a methodological claim — that adversarial
independence catches what effort does not — and a claim like that is worthless without the
record of it being tested on the analysis itself. **This analysis made four errors of its own.** All
four are here in full, with how each was caught — and the pattern in *how* they were caught is the
most useful thing in this file: not one was found by the producer re-reading its own work.

---

# CORRECTION 1 — the `Standing` retraction

*Caught by the structurally independent adversarial audit; verified by the orchestrator and retracted.*

## What I claimed
That `ED-SC-0014` (2026-07-08) **ratified the officer ladder's range to 0–10** and left it
"execution pending", so `faction_politics_v30.md`'s 8-rank ladder with gates at Std 4/6/7 is written
against a scale that does not exist in code.

## Why it is false
The ruling reads: *"Standing range collision ratified (BG faction track 0-10; **scope-tag the
cross-scale homonym with the contest kernel**, OPT-AV-12; FA co-sign); execution pending."*

That is not a range unification. **It is a ruling that "Standing" is a HOMONYM naming different
mechanisms at different scales, and that the senses must be tagged apart.** I read "ratified … 0-10"
and treated it as a verdict on *the* Standing. It is a verdict on *one* Standing.

There are **three distinct mechanisms**, verified at HEAD:

| # | Mechanism | Shape | Where | Executes? |
|---|---|---|---|---|
| 1 | **Contest ethos Standing** — a within-contest quantity, `START=5.0`, `build(deg)`/`strip(deg)` at 0.8 per degree, floor/ceiling clamped, feeds Readiness/leak and `FaceScale` | `float` 0.0–10.0 | `systems/social_contest/sim/contest/primitives.py:31-48` | **yes** |
| 2 | **`Faction.standing`** — a faction-scale reputation modifier, written ±1 by Crown initiatives and absolution, read straight into a dice pool: `pool = int(crown.I) + crown.standing` | `int = 0`, **unclamped** | `engine/autoload/game_state.py:129`; `crown_initiative.py:81,98,116,119`; `absolution.py:86` | **yes** |
| 3 | **Officer rank Standing 0–7** — the 8-rank ladder, sub-office ladders, gates at Std 4/6/7, Leadership Acquisition at Std 7 | integer rank 0–7 | `systems/factions/faction_politics_v30.md:6,1141` | **no — prose only** |

I cited (1) — a per-contest ethos float with `.build()`/`.strip()` — as evidence about (3), a rank
ladder. They share a word and nothing else: no shared state, no shared invariant, no shared failure
topology. **Under this run's own no-pattern-matching rule, that is a vocabulary collision and I
promoted it to a finding.** It is precisely the error I wrote the rule to catch in other people, and
it is the third correction this document has needed.

## What actually survives, stated conservatively
1. **"Standing" is a genuine three-sense homonym across three scales**, and the 2026-07-08 ruling to
   scope-tag it is **unexecuted**. That is a real ruled-but-unexecuted item — but the unexecuted work
   is *tagging*, not *rescaling*. R1 in `02_ruled_but_unexecuted.md` is rewritten to say so.
2. **The officer rank ladder (sense 3) executes nowhere.** This was my broader point and it stands
   independently — L7's count is 0 up paths and 0 down paths executing. It does not need the
   Standing-range argument, and it was never supported by it.
3. **A new, real defect surfaces from doing this properly.** `Faction.standing` is an **unclamped
   `int`**, incremented and decremented in at least four sites, and read **directly into a dice pool
   size** (`crown_initiative.py:81`). An unbounded accumulator feeding a pool is a live **NERS-R
   failure** — leverage is not in-band across the range because the range has no bound. L7 flagged
   it as unclamped against `clock_registry`'s 0–5; the pool read is what makes it mechanically
   dangerous rather than merely untidy. This finding is worth more than the one it replaces, and I
   would not have found it without being refuted.

## The methodological point, for the analysis itself
Two lanes, one adversarial audit and the orchestrator all touched `Standing`; **only the structurally
independent audit caught the error**, because it was the only reader that went to the class
definition rather than to the comment naming a range. The lesson is the one CLAUDE.md §10 already
states and this run has now demonstrated on itself: a critic that never saw the producer's reasoning
is worth more than more effort from the producer. Both of this document's earlier corrections came
the same way — from a subagent contradiction and from an incidental grep, never from re-reading.

**This retraction should appear in the published analysis, not be quietly absorbed.** A document
arguing that Valoria's central hazard is confusing a shared word for a shared mechanism has an
obligation to record that its own orchestrator did exactly that, and was caught by the adversarial
stage working as designed.

---

# CORRECTION 2 — the counter-case, and the narrowing it forced

*The pivotal question: is "built but unwritten" a pathology, or a normal mid-build state? I went looking for evidence against my own thesis and found some.*

## The counter-case is real, and it is strong
`engine/tests/test_pipeline_reach.py` is not a graveyard. It is a **disciplined, live burn-down
list** — `XFAIL_MANIFEST`, *"one row per still-unwired direction, each citing the OI row and the plan
location that schedules its closure. Every xfail in this file corresponds to exactly one manifest
row; **nothing here is a disguised pass**."*

And it burns down. Verbatim from the Wave-2 header (`:88-96`):
> *"**four rows retired this wave, each confirmed XPASS (strict) by running its test directly against
> the tree, not by inspection** — accord-echo-leg (OI-03), vertical-up-handoff (OI-06),
> territory-transfer-resolver (OI-04), world-settlements (OI-07). Their tests are now unconditional
> strict assertions … and their manifest rows are removed."*

Four unwired directions closed in one wave, each verified **by execution rather than by inspection** —
which is precisely the §0.2 discipline this repository has been trying to institutionalise. So
"nothing is wired and nobody is wiring it" is **false**, and any version of the thesis that implies it
is over-claimed. The orchestrator over-claimed it in the first draft.

## But the counter-case does not cover the two rows that matter most
The same Wave 2 that retired four rows did something different to two others (`:83-87`):

> *"`honest-deferral` rows are a **THIRD kind** … unlike `wave2`/`wave3`, these are **not scheduled to
> close in any future wave** — canon itself specifies no world-gen/season-tick trigger for the
> mechanism, so the deferral is the considered, **permanent-until-canon-changes** disposition, not a
> to-do."*

The two rows moved into that category are **`world-npcs` and `world-knots`** — i.e. exactly the two
that would put *people* in the world. And the header states it plainly: *"Wave 2 landed a considered
disposition, not a wire-up."*

**So the finding is not that the backlog is being ignored. It is that the population of the world with
persons was removed from the backlog by reclassification rather than closed by wiring** — on a stated
ground that is explicitly conditional: *permanent until canon changes*.

## Why that reclassification is the thing worth putting in front of Jordan
The stated blocker is *"canon itself specifies no world-gen/season-tick trigger."* That is a true
statement about canon and a **decidable** one — canon changes by ruling. Three things bear on it that
the reclassification does not appear to have weighed:

1. **A citable population already exists.** `references/npc_registry.yaml` holds 46 authored
   characters, each `status: canonical` with a `source` field, each carrying a `role` that is an
   office (King, Duke, Fourth Cardinal, Crown Minister, Chief Parliamentary Clerk, Warden-Chief…).
   OI-05's deferral is grounded in *"no world-gen initial count … to cite"*; forty-six citable,
   canonical persons is a count. **Nothing would be fabricated** — which is the exact value the
   deferral was protecting.
2. **The precedent is in the same commit that created the category.** `world-settlements` (OI-07) was
   retired in Wave 2 by writing `populate_from_geography` — loading authored settlements from the
   canonical geography file. Its docstring proves the manoeuvre is free:
   *"Deterministic: no RNG draw, so this cannot move any RNG-derived campaign golden."* The identical
   move is available for the cast, and for the same reason. Under CLAUDE.md's five-test ladder this
   is **test #4, answered by precedent** — not a `needs_jordan` item at all.
3. **The two rows were classified together but are not alike.** `world-knots` genuinely needs a rule
   (knot formation has prerequisites — Disposition, Bonds, TS — and a formation trigger nobody has
   specified). `world-npcs` needs a **loader**, and its data already exists. Bundling them under one
   disposition let the harder one's justification carry the easier one.

## The refined thesis — narrower, and load-bearing
Replace the first draft's *"the substrate is built and the writers are not"* with:

> **Valoria's wiring backlog is real, tracked and actively burning down. The exception is the
> personal scale: the one class of writer that would put persons into the world was reclassified as
> a permanent disposition rather than wired, on a canon-silence ground that an existing authored
> registry and an existing in-tree precedent both answer. Everything downstream of persons —
> officers, promotion and demotion, intra-faction rivalry, the personal↔strategic seam — is blocked
> behind that single reclassification.**

That is falsifiable, it is specific, it is fair to the work that has been done, and it converts
Jordan's three-part mandate into **one decision** rather than a design programme.

## Rows from the original ten-row table that this narrowing DISQUALIFIES
Being honest about which rows do not belong under the sharper claim:
- **`Settlement.legitimacy` / `.popular_support`** — an explicitly tracked schema stub with an owning
  ED (`ED-FA-0004`, Stratum-B), `registry.py:69-74`. Tracked work, not a silent absence. Belongs in
  the backlog narrative, not the pathology one.
- **`succeed_governor`, `Settlement.suspicion`** — downstream of the officer object existing at all.
  They are *consequences* of the population gap, not independent instances of it. Counting them as
  separate rows inflated the pattern.
- **`Standing`'s unexecuted 0–10 ruling** — a genuinely separate defect (an executed-pending ruling),
  and it stands on its own. It is not an instance of "built but unwritten"; it is "decided but not
  done". Keep it, reclassify it.
The rows that survive as one pattern: `npe.generate_npc` (0 callers, pinned), `npc_registry.yaml`
(0 loaders), `hidden_allegiance` (dropped write), `Settlement.add_tag` (0 callers). **Four, not ten**
— and all four are about *persons*, which is what makes them one pattern rather than a list.

## A vocabulary hazard found while doing this, worth one line
Inside this single file, **"strict" means two different things**: pytest's `xfail(strict=True)` (fail
the run if it passes) and the file's own phrase *"unconditional strict assertions"* (a normal passing
assertion, what a retired row becomes). Reading the manifest header's *"they stay xfail (never flip to
strict)"* against `:625`'s literal `xfail(strict=True)` looks like a contradiction and is not. I
nearly reported it as one. That is exactly the idempotency failure CLAUDE.md §4 legislates against —
a term whose meaning must be re-derived from context, in the one file whose job is to be unambiguous.

---


| Subsystem | Executable Python | Scale |
|---|---:|---|
| `systems/mass_battle/sim` | **11,612** | unit / battle |
| `engine/` (substrate, autoload, cross_scale, mc_v18) | **8,942** | spine |
| `systems/combat/combat_engine_v1` | **7,901** | personal |
| `systems/social_contest/sim` | **7,045** | personal |
| `systems/factions/sim` | **2,744** | faction / political |
| `systems/settlements/sim` | **1,012** | settlement / territory |

≈ **39,000 lines of executing engine code.** `combat_engine_v1` alone is 17 modules — weapon physics,
weapons (921 lines), traditions, capabilities, geometry, contact, a state graph, ability primitives,
a wrapper and a balance workbench. Lane L3 separately verified that its weapon-physics §§1–6 execute
with live consumers, that mass-battle formations (brace / ROLE_SPEC / kite / volley-density) execute
with a measured pike-beats-cavalry cycle, and that fighting withdrawal is built and defaulted ON.

**So the correct framing of this entire analysis is not "the game is not built".** It is:

> **Valoria has four working engines and no populated world to run them on.**

## The asymmetry is the finding, and it is stark
Rank the scales by executable size and the pattern is immediate:

- The three scales that resolve **events** — mass battle (11.6k), personal combat (7.9k), social
  contest (7.0k) — are heavily built.
- The two scales that hold **persons and their offices** — factions (2.7k) and settlements (1.0k) —
  are the thinnest in the tree. **Settlements is one-eleventh the size of mass battle.**

That is the same result the qualitative lanes reached, arrived at by counting lines instead of
reading docs, and it is independent evidence for it. Valoria has invested in *how a contest resolves*
and not in *who is contesting and what they lose*. Every one of Jordan's three mandate items —
officers, two-directional advancement, intra-faction competition — lives in the 3,756 lines at the
bottom of that table, and none of them executes.

## Why this matters for the recommendations
1. **The expensive work is done.** Resolvers are the hard, high-risk part of a design like this, and
   Valoria's are real, tested and tuned. What is missing is comparatively cheap: loaders, writers, and
   a persistent person object.
2. **It reframes the officer mandate as the highest-leverage work available**, not as new scope. The
   engines are waiting for actors; the actors are authored in a file nothing loads
   (`references/npc_registry.yaml`, 46 officeholders, 0 loaders).
3. **It predicts where the next defect will be.** Thin subsystems with rich prose heads are where
   design-vs-code divergence concentrates — and that is exactly where the run found `Standing`
   ratified-but-unexecuted, `add_tag` with zero callers, `legitimacy`/`popular_support` declared and
   never written, `suspicion` with no writers, and `Settlement.pressure` (Π) with no dynamics. All
   five are in the two thinnest rows.

**Falsifier:** the counts are `find <dir> -name '*.py' | xargs cat | wc -l`, so they include comments
and docstrings, and this tree comments unusually heavily. A comment-stripped count would shrink every
row, but the *ratios* — which is what the argument rests on — would have to change materially for the
conclusion to fail. Anyone re-running this should report ratios, not absolutes.

# CORRECTION 3 — the stale golden, and why it is the worst of the four

*Caught by Chapter 1's author while checking a figure I had supplied to everyone.*

## What happened
I instructed all five chapter writers, the index and the PR body: *"Do not propagate the retracted
~87% degenerate win-share. The live golden is `{Crown: 37.5, Church: 12.5, Hafenmark: 12.5,
Varfell: 37.5}`."*

That substitute is itself stale. It sits at `engine/tests/test_f7_smoke_oracle.py:75` inside a block
headed **"OLD (pre-OI-04, pre-transfer-motion) values, preserved for the before/after record"**. The
live constant is at `:267`:

```python
GOLDEN_WIN_SHARE = {'Crown': 62.5, 'Church': 25.0, 'Hafenmark': 0.0, 'Varfell': 12.5}
```

regenerated 2026-08-24 when the mass-battle engine was swapped (1,905 lines replaced by an
11,342-line ported engine).

## Why it is the worst of the four
The first two were reasoning failures. This is a **process failure inside the instruction warning
against that exact failure** — I handed writers a stale number in the same sentence telling them not
to propagate a stale number. Had Chapter 1's author not checked, four chapters would have carried it
*with a citation*, which is precisely how the ~87% figure reached five documents.

The rule that would have prevented it was already written down, forty lines from where I misread it,
by someone who had been burned by the same trap (`:264-265`):

> *"A golden test pins the LIVE constants; nothing pins the prose, so a fabricated history stays green
> forever and the next re-recorder reasons from it. Rule: a PREVIOUS line is read out of
> `git show <ref>:<file>`, never copied from the constant you are about to overwrite."*

A guard, earned, placed at the point of use, in the right file — and it still did not stop the next
reader, because prose beside a value enforces nothing. Under CLAUDE.md §0.05 that is the entire
lesson: **the annotation is reference; only the code is mechanism.** A preserved historical constant
sitting in a comment next to a live one is a trap no amount of labelling closes. The mechanism that
would close it is to make the live constant the only copy reachable without an explicit `git show`.

## A caveat that matters more than the number
None of these figures is a balance fact. The file states (`:264-265`) that n=2/seed-0 and n=8/seed-42
**"cannot distinguish a balance change from noise"**, and the n>=100 oracle its own line 8 demands
still does not exist. They are reproducibility pins. Using them as evidence about Valoria's balance
repeats the ~87% error in a new costume.

---

# CORRECTION 4 — "golden-safe by construction" is refuted, by experiment

I banked as verified that loading persons at world-gen cannot move a seeded golden, reasoning from
`populate_from_geography`'s docstring. Chapter 1's author tested it instead of reading it:

- The two guards that this analysis, five Fable lanes and the Opus adversarial audit all described as
  pinning the world's population **pin `generate_npc`'s call counter** (`world.npc_counter`), not
  `world.npcs`.
- Two NPCs loaded directly into `world.npcs` left **both guards green** at `npcs_generated = 0` —
  **and moved seed-42's winner from Crown to Hafenmark.**
- A control arm with `npe.simulate_npc_actions` neutered reproduced the baseline **byte-exact**,
  isolating the channel: `simulate_npc_actions` draws `world.rng` at
  `systems/overview/sim/accounting.py:139`.

Two consequences worse than the retracted claim. **A social-drift simulator is invoked roughly 400
times per golden batch (50 seasons x 8 campaigns) over an empty dict, and is one non-empty dict away
from consuming campaign entropy.**

⚠ *Precision owed to Chapter 5's author, who checked this rather than accepting my wording.* An
earlier version of this paragraph said the simulator "has been drawing from the campaign RNG" all
along. **It has not.** `npe.simulate_npc_actions` binds `rng` and then iterates
`for tid, npcs in store.items()` (`systems/world/sim/npe.py:353-368`) — with an empty store the loop
body never executes and **zero** draws occur. The hazard is *latent*, not active.

That distinction makes Chapter 1's experiment sharper rather than weaker: the guards look green today
precisely because nothing draws; the instant the world is populated, entropy consumption begins and
the seeded goldens move — which is exactly what the experiment observed. A dormant stochastic
consumer sitting behind an empty container is a worse failure mode than an active one, because
nothing about today's green suite predicts tomorrow's red one. And


**the guards go silent rather than break** — a loader that populates `world.npcs` without calling
`generate_npc` passes both. Failing to notice a change is strictly worse than failing on it, and it
is CLAUDE.md §0.1 pt 2 — *an assertion must be able to observe the failure it excludes* — violated by
guards written in that rule's own spirit.

## The pattern across all four
| # | Error | Caught by |
|---|---|---|
| 1 | `Standing` ratified 0–10 (a vocabulary collision promoted to a mechanism claim) | the structurally independent adversarial audit |
| 2 | Ten absences over-generalised into one pattern | the same audit, narrowing it to seven |
| 3 | A stale golden propagated inside a warning against stale goldens | a downstream writer checking a supplied figure |
| 4 | "Golden-safe by construction" | a downstream writer **running a controlled experiment** |

**None was caught by the producer re-reading its own work.** Two came from structural independence
and two from a downstream reader refusing to take a supplied claim on trust. Error 4 in particular
was invisible to six careful readers and fell out of one experiment with a control arm — which is
CLAUDE.md §0.1's measurement discipline vindicating itself, and the strongest argument in this
document for §0.2's rule that *done means it runs*.

---

---

# CORRECTION 5 — I overstated what the 46 authored records contain, and the fix improves the recommendation

*Caught by Chapter 2's author, who counted the fields instead of trusting my summary. Verified.*

## What I claimed
That `references/npc_registry.yaml` holds 46 authored officeholders *"each with stats, territory,
goals and weighted convictions"*, and I put that in the index and the pull-request body.

## What the file actually contains
Counted by parsing it (non-null values, 46 records):

| Field | Coverage | | Field | Coverage |
|---|---:|---|---|---:|
| `id`, `first_name`, `faction`, `role`, `status`, `convictions`, `source` | **46 / 46** | | `ts` | 10 / 46 |
| `last_name` | 44 / 46 | | `certainty` | 8 / 46 |
| `arc_trajectory` | 36 / 46 | | `territory` | **7 / 46** |
| `resonant_style` | 18 / 46 | | `title` | 7 / 46 |
| `goals`, `cultural_label` | 17 / 46 | | `birthplace` | 5 / 46 |
| `notes` | 15 / 46 | | `coherence` | 1 / 46 |
| | | | **`stats`** | **1 / 46** (NPC-001 only) |

**"Each with stats" was wrong by a factor of forty-six.** Exactly one record carries a stat block.
Territory is on seven, not all.

## Why this makes the recommendation better rather than worse
The error mattered because it inflated what a loader would deliver. Corrected, the picture is sharper
and it resolves a question the analysis had been treating as either/or.

**What all 46 records genuinely carry is identity, an office, a faction, a provenance, and a weighted
conviction vector** — `convictions: {primary: [{conviction, weight}, ...], cultural_label,
self_other_initial}`, present on every single one. That is precisely the VSG-shaped payload: a
weighted vector with a cultural conditioning label.

**What they do not carry is mechanical stats.** And the tree already contains the thing that produces
those: `npe.generate_npc`'s Tier-1 archetype seed, which derives the five axes from
`_ecology_weights(world, territory_id)` — the territory's own prosperity and accord.

So the right architecture is neither "load the registry" nor "run the generator". It is **both, in
order**:

> **Load authored identity, office, faction and conviction vector from the registry; derive the
> mechanical stats through the existing territory-conditioned generator.**

That composes the two existing pieces instead of choosing between them, it keeps every authored fact
citable (no fabrication — the constraint OI-05's deferral exists to protect), and it confines the
stochastic half to the fields nobody authored. It also splits the golden cost cleanly: the authored
half is deterministic; only the derived half touches `world.rng`, and Correction 4 already establishes
that the drift channel needs its own substream first.

**Sequence, therefore: RNG substream → authored-identity loader → stat derivation.** Three commits,
each independently verifiable, with the golden-moving step isolated in the last.

## A live defect found in the same file, by the same author
`references/npc_registry.yaml:835` and `:850` carry unquoted `#` characters inside a value:

```yaml
faction: Hafenmark (Inner Council #4)     # parses as 'Hafenmark (Inner Council'
faction: Varfell (Jarl Council #5)        # parses as 'Varfell (Jarl Council'
```

**YAML eats `#4)` and `#5)` as comments.** NPC-081 and NPC-082 therefore land in singleton faction
namespaces that match nothing. A two-character fix — quote the strings — that **must land before any
loader**, or those two officers silently join factions that do not exist.

This is the *same failure class* as the Gustav colon (`01_verified_defects.md` D5): a structural
character inside an unquoted YAML scalar, in a file nothing loads, undetected because nothing loads
it. Two instances in one 46-record file is not bad luck; it is what an unparsed register looks like.

And the truncated text is itself the finding: **`Inner Council #4` and `Jarl Council #5` are seat
numbers encoded in a free-text faction string.** The officer object is trying to exist inside a
`str`. That is the strongest single piece of evidence in this analysis that the object is missing —
the authors kept writing seats down because there was nowhere to put them.

---

# CORRECTION 6 — `temperaments.py` is executable, not executed, and I said executed

*Caught by Chapter 4's author. Verified.*

I claimed, in the front matter and in the orchestrator's own spine, that
`systems/settlements/sim/temperaments.py` is the one VSG slice that **executes** — pointing at its
five-typology ⟨α,β⟩ table (`:34-38`, carrying Goldenfurt's authored `"traditional": {alpha: 0.3,
beta: 0.7}`) and its strain-driven drift toward `outcomes-only` (`:124-131`).

The module is real and it runs when called. **Nothing calls it.** Grep across every `.py`: the only
occurrence outside the module itself is a docstring mention at
`systems/settlements/sim/registry.py:15`. There are **zero production callers and zero tests**.

Under CLAUDE.md §0.2 — *done means it runs, and something ran it* — that makes it **executable, not
executed**, and the distinction is the one this entire analysis is built on. I asserted the stronger
word about the single example I was using to prove the method is implementable. Chapter 4 also notes
its drift is one-directional (`if drift > 0`), which places it in the same accrual-without-restoration
class the chapter's own T-04 describes.

The corrected version is still good news for the argument, just weaker than I put it: **the slice is
written, correct and one call site away** — it is evidence the method is cheap to land, not evidence
that any of it is landed.

---

# CORRECTION 7 — the most dangerous one: a recommendation that would have overwritten a Jordan hold

*Caught by Chapter 3's author. Verified. This is the error that would have done real damage.*

## What I published
`02_ruled_but_unexecuted.md` row **R2** claimed Jordan's 2026-08-14 obstacle-derivation ruling was
**ruled and unexecuted**, and the register's summary recommended it as *"perhaps thirty lines of code
plus falsifiers"* — the second of its two headline actionable items.

## Why it is wrong, twice
**(a) The evidence was a stale comment.** My warrant was `engine/autoload/dice_engine.py:118-123`
asserting *"THAT DERIVATION IS IMPLEMENTED NOWHERE — every call site in the tree still passes a
hand-set Ob."* Under §0.05 that is prose, and it is **out of date**.
`tests/valoria/test_faction_obstacle_conventions.py` records the measurement, 2026-08-21:

> *"the M1 board records that derivation as 'wired NOWHERE'. **Measured 2026-08-21, that is FALSE:**
> of the three sites that roll against a target faction's score, **one already implements the ruling
> exactly, one implements it under a condition, and one contradicts it** — each citing its own canon."*

**(b) The work is not pending. It is deliberately suspended.** Same file:

> *"Jordan **suspended the work 2026-08-21** and flagged it for later systems work **rather than
> having a session reconcile three ratified numbers on its own authority.**"*

And a guard exists for precisely this: the test pins all three conventions so that none drifts while
the question is held — *"including a well-meaning 'let's just make them consistent'."*

**That is my recommendation, described in advance, by the guard built to stop it.** Had anyone acted
on R2, they would have overwritten a live Jordan hold, reconciled three ratified numbers on a
session's own authority, and broken the test protecting them.

## The lesson, at its narrowest
I built a register whose entire purpose is to catch claims that outran their evidence — decisions
recorded as done that the code does not obey — and populated one of its two headline rows from **a
comment**. Not a careless comment: one written by someone rigorous, in the correct file, about their
own function. It was simply older than the measurement that superseded it.

> **A comment is not a measurement — including a comment written by someone careful, in the right
> file, about their own code.** §0.05 is usually read as a rule about design documents. Its sharpest
> application is to the docstring three lines above the function you are citing.

The general form, and the reason this analysis keeps tripping on it: **prose ages silently and code
does not.** A stale comment produces no failing test, no diff, no signal of any kind. The only way to
catch one is to check the behaviour it describes — which is what Chapter 3's author did, and what I
did not.

## What replaced it
The row is struck rather than deleted, with the refutation in place, so that the next reader of this
register meets the correction rather than the claim. And CH3's parallel finding on the TN defect
(`01_verified_defects.md`) runs the same way but in the opposite direction: I said fixing `roll_pool`
would move the seeded goldens and cost a re-pin. Measured, it costs **nothing** — a TN-parameterised
face rule already exists at `systems/mass_battle/sim/resolution.py:36-42`, reproduces
`_CONTINUOUS_PARAMS` bit-exactly at 6/7/8, and is bit-identical at tn=7. Both goldens ran green under
an in-memory patch.

Twice, then, in the same chapter's review: I overstated a cost and understated a risk, and both were
settled by someone measuring instead of reading.
