# The character decision layer — one precedence, three bands

## Status: **PROPOSED (2026-09-18). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Authority: **none claimed.** Supersedes nothing. Takes no position inside `proposals/2026-09-17-governance-and-behaviour/` or r2.
## Lane: `IN` · no ED id allocated · `references/id_reservations.yaml` untouched
## Grade under `CLAUDE.md` §0.2: **`paper`** for §3–§7. §2 and §6 are **`measured`** — every number names the command that takes it.
## Reads: `CLAUDE.md` §0.05 (code is mechanism), §0.06 (NERS), `skills/ners/SKILL.md` (method).
## Beside it: `../2026-09-18-conviction-basis-worksheet.yaml` (Jordan's open choices) · `../2026-09-18-conviction-basis-probe.py` (the instrument)

> ⚠ **THIS FILE IS A QUEUE BY CONSTRUCTION AND DOES NOT CLAIM §0'S EXEMPTION.** §7 creates work for a
> future session. That is what a proposal is; the exemption is for a verdict about something that
> already exists, and this is not that.

---

## §0 · What this reconciles

Four documents arrived across one session, each superseding the last in part, none citing this
repository. Three rulings arrived from Jordan in the same session. One structurally read-only NERS
pass attacked the result. This file is the single coherent shape they converge on, with every
collision against the tree named rather than smoothed.

| source | what it contributed | what did not survive |
|---|---|---|
| `character-decision-frameworks.md` | four architectures; the composite; the build order | its build order, corrected twice by its own successors |
| `character-model-term-index.md` | **the class test** — FIELD / READOUT / STRUCTURE / DISPOSED | its three-axis roster (`warrant`/`facing`/`purity`), which is a *third* axis set |
| `character-model-adjudication.md` | twelve self-defects; the evaluation order; `D8`'s two-stage split | `D1`'s integrity formula, retracted by its own author |
| `decision-procedure-docket.md` | **the procedure**: ordered tests returning EXCLUDE / DECIDE / PASS | its name (taken — §2.4); its one-act return; its fixed generation order |

**The single claim this file makes that none of the four makes:** *Valoria already runs a precedence.
It is global rather than per-person, and it runs over occasions rather than over acts.* Everything
below follows from taking that seriously.

---

## §1 · The fixed points — ruled, not proposed

Three rulings from Jordan, 2026-09-18, **recorded in commit messages only; none is in a ledger yet.**

**R1 — `conviction` is reserved for RELIGIOUS AFFILIATION AND INTENSITY.** A vector over affiliations;
confliction **derived** from an incompatibility relation, never stored. Reaffirms `STR-6`
(`RULINGS.yaml:1371`, ED-IN-0245). Verbatim, 2026-09-17: *"reserve 'conviction' for religious
affiliations and their intensities so that you can have someone who is devoutly Solmund but also
believes in Threadwork and therefore experiences religious confliction."*

**R2 — `Truth` IS NOW `Conviction`.** ED-IN-0075's 0–5 pole (Solmund-orthodoxy ↔ Thread-truth,
`CURRENT.md:31`, ruled *"DISTINCT and unchanged"*) is absorbed. MEASURED: `Truth` has no
implementation — 10 mentions under `engine/season/`, every one narrative prose in `cases/*.yaml`, no
field, no reader. **Owes a successor row AT ED-IN-0075**, not only a new row; PR #413 caught exactly
this trap with ED-IN-0210.

**R3 — best design wins.** Verbatim: *"reconcile or replace. best design wins."* The incumbent gets no
default; migration cost is a price to state, never an argument.

**And two ratified constraints that bind everything below.** `R7`
(`adjudication_register.yaml:223-228`): the projection is a **linear map** from the weight vector, so
two persons with identical weights are identical on every projected axis, necessarily — *any quantity
that must vary at fixed weights cannot be a projected axis.* `AX-2` (`01_AXIOMS.md`): no view of world
truth inside a decision; a `View` carries claims and raises on anything else.

---

## §2 · The vocabulary — one word, one object

### 2.1 Three bases, and why they are three rather than one

| basis | holds | reaches behaviour by | escapes `R7`? |
|---|---|---|---|
| **conviction** (R1/R2) | a vector over religious affiliations, with intensities | confliction derived from an `incompatible` relation | n/a — not projected |
| **⟨moral basis⟩** — name is Jordan's (§9) | N weights over a roster | projection onto axes, then `align(verb, axis)` | **no** — bound by `R7` |
| **bearing** | the axis values **directly on the Person** | consulted inside a test; no projection | **yes**, and that is its whole reason |

`adjudication_register.yaml:201` records Jordan making this split himself: *"these four are
value-frames (what is right), the seven are bearing."* `R7` is why it is forced rather than tidy —
a rigid man and a fluid man holding the same principles is **structurally impossible** as a projected
axis and **free** as a held one.

### 2.2 The class test, which is the term index's real contribution

Every folk term is one of four things, and mixing them is what produces unbuildable specs:

- **FIELD** — names a quantity it multiplies, a threshold it sets, or a set it filters. *Stored.*
- **READOUT** — computable only after the fact. *Never stored; storing it throws away what generated it.*
- **STRUCTURE** — a property of how fields relate, not a value any field takes.
- **DISPOSED** — duplicate, category error, or a property of the question rather than the person.

Applied to Jordan's twelve concepts of 2026-09-18, this **collapses** rather than grows the basis:

| class | terms | resolves to |
|---|---|---|
| FIELD | rigidity · flexibility · means-before-ends · ends-justify-means · pragmatism | **one field: `bend_price`** — high, low, ∞ (a gate), a readout over the vector, and low-plus-stable-goals |
| FIELD | fluidity | **`drift_rate`** — its own field, explicitly *not* rigidity's opposite |
| FIELD | indirect · direct | **two** fields: speech convention (a culture prior) and `means_directness` |
| READOUT | humble · grandstanding | the integrity delta read backwards — `social_weight` made visible |
| READOUT | insecure · secure | claimed-vs-perceived distance — **already computed** by `standing_of` (`options.py:443-464`) |

⚠ **A first pass of this session read all twelve as five bipolar held axes. That was wrong and is
retracted** — they are not the same kind of thing, and five of them are one field seen from
different angles.

### 2.3 What `cost` was for, and why it is not needed

`synthesis.md` §1.3 justifies exactly one minus sign: *"Valoria resolves by drawing, so a term that
moves the obstacle and a term that moves the preference are different objects. `cost` belongs on the
Ob; `pull` belongs on the pool."* **Both halves survive the cut** (§4, F1).

### 2.4 ⚠ `docket` IS TAKEN. The procedure needs another name.

`w.docket` is the **world's** register of matters — `DocketItem`s with dates, feeding Q1 `date_due`
(`harness/corpus_run.py:325`, `probes.py:1366`). A `Person.docket` holding an ordered list of tests
would be one word on two objects, which is the exact failure `STR-5`/`STR-6` spent their length on for
`temperament`, `piety` and `belief`. **The read-only pass's own steelman proposed `Person.docket`
without noticing.**

MEASURED, live code and both registries: `constitutive` 0/0 · `precedence` used in this repo's prose
already in precisely this sense (*"a precedence list"*, `harness/populated.py:148`; *"the
source-precedence ruling"*, `hole_register.yaml:1664`) and registered **nowhere**. §4's cold-reader
test passes on it. **This file uses `precedence`; the name is Jordan's to confirm (§9).**

---

## §3 · The architecture — three bands

```
CONSTITUTIVE   opening_set clauses 1-4                 discrete · arithmetic-free · SHIPS TODAY
PRECEDENCE     an ORDERED tuple of tests, per person   EXCLUDE / DECIDE / PASS
RESIDUAL       the draw                                _sample_order, Plackett-Luce at tau
```

### 3.1 The claim that makes this small

**Valoria already runs a precedence.** `world_q.questions_for` produces occasions from four ordered
sources (`QUESTION_SOURCES = date_due · claim_landed · band_crossed · need`), and
`aggregate_questions` under the shipped `first` rule takes the head — which `H-54` records as having
*"silently ruled that A DATE ALWAYS BEATS A NEED, which decides what every NPC does first"*
(`deliberate.py:103-107`).

That is an authored test order. It is **global** where this proposal makes it **per-person**, and it
runs over **occasions** where this proposal moves DECIDE down to **acts**. So the change is not
*replace the sum with a procedure*; it is:

1. make the order per-person,
2. move DECIDE from occasion-selection to act-selection,
3. keep the draw as the residual.

### 3.2 The six decisive tests, and their carriers — all shipped

Each test is `(p, view, live) -> (verdict, subset)`. **Person-side only; no `World` argument** — `AX-2`,
and `test_choose_receives_no_world` already pins the property.

| test | asks | carrier that exists today |
|---|---|---|
| **Obligation** | does a duty name exactly one act? | Q1 `date_due` off `w.docket` (`world_q.py:561-568`) |
| **Threat** | is a stake under threat past the ruin line? | Q3 `band_crossed` + Q2 `claim_landed` on owned tenures; body bands via `budget.py:73` |
| **Conviction** | does a salient religious affiliation discriminate? | R1's vector — **does not exist** (§5) |
| **Principle** | does a salient moral weight discriminate? | the existing `Σ axis_w · align` (`choose.py:359-360`), used as a **local** currency against a bend threshold, never summed with anything else |
| **Standing** | who sees, and does the reading differ? | `stance_toward` (`choose.py:134-143`) + `standing_of` (`options.py:443-464`) |
| **Habit** | what did he do last time? | own firsthand ledger claims — ⚠ **CROSS-SEASON ONLY** (§3.4) |

### 3.3 The output is an ORDER, not one act

The docket document's `decide()` returns one act. `pack_scenes(p, ranked, n_scenes, …)` takes a
**ranked list** and `n_scenes` is a **cost budget**: `take()` spends it across the ranking and an
extended scene costs 2 against a plain one's 1. S26.3 (*the person triages*) and U2 (the budget is
the season remainder) both assume an ordering the person chooses what to leave undone within.

**Repair:** DECIDE the head, remove it, re-run until `live` empties or the budget is spent; hand the
list to `pack_scenes` unchanged. This is `_drop_what_was_already_done`'s loop (`deliberate.py:278-341`)
moved one level down.

### 3.4 ⚠ Habit collides with R-03 within a season

`_drop_what_was_already_done` **removes** what was already realised, and `_realised` resets per season
(`driver.py:354-355`). So *"what did he do last time"* as a DECIDE inside one season would re-choose
what the driver has just removed. **Habit is lawful cross-season only**, and this proposal scopes it so.

### 3.5 The residual is the DRAW, never a fixed generation order

The docket document requires *"fixed generation order [D4]"*. **That is `H-96`'s retracted defect by
name** — the triage *"decided, for most candidates, BY ALPHABETICAL ORDER OF THE VERB'S NAME"*,
measured by running one mechanism under two names: the early-sorting name executed in **18** corpus
cases and displaced 71 acts, the late-sorting one in **5** and displaced **2**. Same world, same seed.
The fix was to **sample** the order (Plackett-Luce via Gumbel, `choose.py:170-319`), and this proposal
keeps it. **A free cut whose proposed replacement is worse.**

⚠ **And this is not the contradiction it appears to be.** `H-96`'s order was the order of
**candidates**, decided by an arbitrary lexicographic property of a verb's name — meaningless. The
precedence is the order of **tests**, authored per person — meaningful. The tree removed meaningless
order-dependence; this adds meaningful order-dependence.

### 3.6 The empty set emits

A decisive EXCLUDE that empties `live` is a **dilemma**, and the null act **emits an event kind**
(precedent, and it is stronger than a bare one: `resolve.py:161`, `:208`, `:270` each emit
`row.emits_on_refusal or ("act.refused",)` — refusal-emission is **already a declared verb-table
column**, so a dilemma kind is a data edit rather than new machinery). The source document's null act accrues
residue and emits nothing, which is silence beating refusal — a dominance the `ners` skill names.

⚠ **The line that must change its mind is `choose.py:347-350`, not `questions.py:29`.** The latter is
the *no-occasion* case and is correct under either design; the conflation is that a question with no
surviving candidate returns the same empty list as no question at all.

---

## §4 · What this deletes, and why each cut is free

The `ners` skill grades a pass on **cuts that turn out to be free** — a claimed-necessary element whose
lost possibility survives, because something else already provides it.

**F1 — `cost(c) = demand · (1 − courage)`. FREE.** Its justification is the Ob/pool split (§2.3), and
both halves survive: the obstacle is already a RESOLVE-side quantity — `resolve.py:388` refuses at
`Ob > 2 × Pool` under S27.4, and that same block records that ***"the computed chooser never sets"***
`Act.obstacle` — while putting `pull` on the pool contradicts a ratified ruling verbatim at
`options.py:141`: ***"capability supplies dice and GATES NOTHING"*** (#353 §9.2).
⚠ **This is the finding that decides §7's shape.** The sum's central justification is not load-bearing.

**F2 — `Σ press · serves`. HALF-FREE.** Q4 `need` already makes a live commitment the *occasion*
(`world_q.py:608-616`), and the precedence supplies its priority for free. `press` as a magnitude has no
producer. ⚠ `serves` — *which verb advances this commitment* — is absent in **both** designs. Shared gap,
not a false N-line.

**F3 — `urgency`. FREE.** Dead by construction (`choose.py:146-167`, `H-73`). Already known.

**F4 — Δ ≥ 0.294 as a general method rule. DELETED, AND THIS SESSION MISUSED IT.** The floor is
`P(inversion) = 1/(1+e^{Δ/τ})` where `_sample_order` keys on `score(c)/τ + g` **per candidate within one
person's list** (`choose.py:317`). It governs two of *that person's* candidates swapping. It says nothing
about two different people, who never share a sort — and `RULINGS.yaml:1176-1179` warns of exactly that:
***"a builder who applies the 0.294 floor uniformly will apply it to a quantity that never enters the
sort."*** It survives for within-one-sort questions and for nothing else.

**F5 — the global sum. DELETED**, on F1–F3 rather than on age (R3). Every term relocates into one test.

---

## §5 · What this needs that does not exist

Ranked by cost. Nothing here is scheduled by this file; §7 is.

1. **The four excluders of the constitutive band** — scope, `purity ≥ 2`, lexical exclusions, taboo
   gates. MEASURED 0/0/0/0 across live code, both registries, `.designs/` and `proposals/`. Without
   them the aperture cannot narrow, and §6's constant is the consequence.
2. **`Person.precedence`** — an ordered tuple, and a **sixth** interior row with no producer beside the
   five `01_THE_BUILD_ORDER.md:1031` already names. It fails the same disqualifier `convictions` fails.
3. **R1's affiliation roster and `incompatible` relation** — neither exists; `church_standing` is one
   string in a claim-predicate values list (`rosters.yaml:312`) that nothing reads.
4. **A reason on `Event`** — `carriers.py:92-98` has no field for it, so a deciding-test name reaches
   the player's trace and not other persons' ledgers unless it rides the event KIND.
5. **`choose` looping to an order** (§3.3).
6. **A narrower aperture** (§6).

---

## §6 · The measurements that constrain this

Instrument: `../2026-09-18-conviction-basis-probe.py`, control-paired, its control assertion proven to
fire by substitution under `--prove-control`.

| measured on `build_realm(0)` | figure |
|---|---|
| candidates per person | **min 28 · median 28 · max 28** |
| distinct verbs per person | **28 for all 46** |
| distinct subjects per person | **1 for all 46** |
| persons excluded to an empty set | **0** |
| distinct conviction vectors → distinct first acts | **41 → 6** (uniform control: → 1) |
| distinct full rankings, live vs control | **41 vs 2**; rank disagreement 0.2882 vs 0.0000 |
| effective directions in the live 13×4 | **1.849** of 4 (candidate basis 2.199) |
| `ALIGNMENT` | 52 cells · 31 of 38 verbs · 17 negative |
| verbs with no moral weight at all | 7, including **`speak` and `tell`** |

**⚠⚠ THE APERTURE IS A CONSTANT FUNCTION OF THE PERSON.** Neither `opening_set` clause 2
(`eligibility`) nor clause 4 (known-false from the person's own claims) discriminates between anybody
on this world. Every difference between two people's behaviour comes from the score, or from which
single subject they were handed. **The stage this proposal puts first is, with respect to the person,
currently a no-op** — which is why §5 item 1 ranks highest.

**What a dilemma costs:** the set empties **per question**, and the referent set is **one**. Prohibition
must beat **28 verbs toward one target** — *everything I could do to my brother is either forbidden by
my oath or beneath me.* A pointed question makes a dilemma cheap; a broad verb repertoire makes it
impossible. **The dilemma rate is a property of the question and the verb breadth, not of the
procedure**, and 28 is the number to beat.

**Three of the six tests fire zero times today.** Q1 and Q3 measured 0 questions on a populated season;
`stance` has 0 rows. So Obligation, Threat and Standing PASS for everyone until the aperture work lands.

**Retracted in this session, and carried here so they are not re-derived:** the 0.294 floor applied
across persons (F4); the integrity formula, circular at its source and with no comparison arm here since
the social term is measurably zero; `means-before-ends ↔ ends-justify-means` as one axis; `pragmatism` as
a duplicate of `Utility`; `values` as the free name for the moral basis (`values:` is the generic YAML key
holding a roster's members, 28 times in `rosters.yaml`).

---

## §7 · Build order

Each step is executable and observable before the next. The ordering follows the correction **all three
successor documents converged on independently**: the cheapest and most visible stages come before any
arithmetic exists.

| # | step | why here | artifact |
|---|---|---|---|
| 1 | **The reason on the trace** | `trace_log` records actor/verb/budget only; every legibility mechanism downstream consumes a *reason*. Cheapest thing in the file. | a deciding-test name per act in `TRACE` |
| 2 | **Split the two empties** at `choose.py:347-350` | no-occasion and excluded-to-empty currently return the same `[]` | a census separating them |
| 3 | **The constitutive band's excluders** | §6 — the aperture is a constant; nothing downstream discriminates until this does | scope · `purity≥2` · lexical · taboo, as data |
| 4 | **`Person.precedence` + the test roster** | the order is the character; `require_member` like `question_sources` | `rosters.yaml` roster + one held field |
| 5 | **Three tests with live carriers** — Principle, Standing, Habit | they can fire today; the other three cannot (§6) | `(p, view, live) -> (verdict, subset)` |
| 6 | **The loop to an order** (§3.3) | `pack_scenes` is unchanged; only `choose` changes shape | one loop in `choose` |
| 7 | **The emitting null act** (§3.6) | a dilemma that emits nothing is silence beating refusal | one event kind |
| 8 | **R1's affiliation roster + `incompatible`** | Conviction test acquires a carrier | `rosters.yaml` + `descriptor_registry.yaml` |
| 9 | **Obligation and Threat** | they have carriers but no occasions until the aperture work lands | after phases 1–3 of the r2 order |

**`6f` is not on this list.** `01_THE_BUILD_ORDER.md:1032` specifies it as *"the score function itself —
`pull(c) − cost(c)`"*, and F1 removes the reason that function was shaped that way. Nothing is deleted,
because nothing was built: `6f` has zero lines in the tree.

---

## §8 · What would show this wrong

- **§3.1's claim fails** if `aggregate_questions`'s ordering turns out not to be a test order — if the
  four question sources are not comparable to the six tests, the tree is not already a precedence and
  this proposal is a bigger change than it says.
- **F1 fails** if any reading of `synthesis.md` §1.3 makes `cost` reach something other than the
  obstacle. Then the sum's minus sign is load-bearing after all and §7 is mis-shaped.
- **§3.3's repair fails** if the loop changes which scenes pack — the falsifier is a corpus run whose
  `pack_scenes` output is compared against today's for an unchanged chooser.
- **§6's constant is the whole of §5 item 1's argument.** If the aperture is *not* constant on a world
  other than `build_realm(0)`, item 1 drops in rank. One command settles it: the probe's arm 3 on
  another seed.
- **The precedence is decoration** if, once built, the six tests produce the same act order as the score
  on the same world. That is a runnable comparison and it is the honest replacement for the Δ ≥ 0.294
  floor F4 deletes.

**Not claimed:** that the six tests are the right six; that the three bases are complete; that any
magnitude here is right. This is the smallest shape that holds the four documents, the three rulings and
the measurements at once.

---

## §9 · What is still Jordan's

Nothing below has an engineering answer, and §0's five-step gate was run on each.

1. **Sum, precedence, or neither** — `docket_verdict` in the worksheet. This file argues for the
   precedence on F1–F5; the argument is refusable.
2. **The name of the procedure** — `docket` is taken (§2.4). `precedence` is this file's candidate.
3. **The name of the moral basis** — `conviction` has gone to religion. `principles` measured free.
4. **The third axis set** — `warrant`/`facing`/`purity` against the four ruled on 2026-09-17. Its
   definitions are in `conviction_projection_vnext.yaml`, which exists in neither the repo nor the
   uploads; and `purity`'s weighted-**max** aggregation would change `data/convictions.to_axes` — the
   single owner of convictions→axes — rather than adding a column.
5. **The affiliation roster, its 10 incompatibility pairs, and the intensity scale** (R1/R2).
6. **The 13×N cells themselves**, rows and columns both open under `STR-2`.
