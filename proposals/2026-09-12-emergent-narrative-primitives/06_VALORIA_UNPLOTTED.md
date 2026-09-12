# Part F — the ledger run backwards: Valoria's own mechanics, scored against the suite

## Status: **PROPOSED (2026-09-12, ED-IN-0217). HELD BACK FROM RATIFICATION-ON-MERGE, IN FULL.**

⚠⚠ **SUPERSEDED BY `proposals/2026-09-12-emergent-narrative-primitives-v2/` (same session, same
`ED-IN-0217`).** This set applied the wrong test: it disposed of mechanics on **architecture rules** and
**implementation facts** as though those refuse an idea, which they do not — and it never cited **`R2`**,
the ruling that makes every refusal *instrumental, not terminal* and requires each to be **argued** against
five terminal properties (`references/design_rulings_2026-09-06.md:37-50`). Its facts are largely sound and
its citations reproduce; **its verdicts do not follow from them.** Kept as the audit trail. Read
`…-v2/02_THE_RESCORE.md` for what changed and why, and `…-v2/01_THE_TEN.md` for the set that replaces this
one.


Part E scores **the suite's catalogue against Valoria** — 76 primitives, mostly refused. That direction
cannot see a mechanic this tree runs that no catalogued primitive names, and there are several. This
part runs the ledger the other way: **every verb in the shipped grammar, and every declared carrier,
scored against whether the suite has a vocabulary for it at all.**

**Why the reverse direction is the more useful half.** A catalogue of refusals says what the game is
not. The suite's axes were built to discriminate among thirty-three shipped games, so a mechanic those
games do not have is invisible to them — and that is exactly where a design's own contribution lives.

**The roster is authoritative and complete, not assembled.** `engine/season/verb_table.yaml` carries
**38 verbs**, and `engine/season/requirements.yaml:301-305` measures their execution:

```
11 of 38 verbs execute in the corpus
   create_record · interview · move · reconstruct · release · research
   speak · surveil · tell · transfer · utter
20 carry no predicate and no effect
 5 are foldable but never attempted   — the governance verbs (H-71)
 2 are attempted and always refused   — work, examine: no question these worlds raise
                                        refers to a Site
```

**Four execution states, and each is DERIVED rather than asserted** — from three columns that can be
cross-tabulated: `eligibility` in `verb_table.yaml`, membership of `EFFECTS` in `loop/effects.py`, and
the eleven names above.

| state | how it is derived | count |
|---|---|---|
| **RUNS** | named in the eleven | **11** |
| **FOLDABLE, NEVER ATTEMPTED** | has an `EFFECTS` body; not in the eleven; not refused at `requires` | **5** — `confer` `convene` `revoke` (each `remit:`-gated) · `destroy_record` (`H-75`) · `kill / wound` (the third gate) |
| **ATTEMPTED, ALWAYS REFUSED** | a candidate forms and `requires` refuses it every time | **2** — `work`, `examine`, both `presence:<site>` |
| **NO EFFECT BODY** | no `EFFECTS` entry, and it writes something it never writes | **20** |

11 + 5 + 2 + 20 = 38. ⚠ **Eleven verbs have `EFFECTS` bodies and six of the eleven that RUN do not** —
`speak`, `tell`, `interview`, `research`, `surveil`, `reconstruct` pass the gate
`effected = not row.writes or v in EFFECTS` (`loop/driver.py:99`) **by writing nothing**. Their whole
effect is the emitted event and the claims the witness layer then deposits, which is why Part B `P6`'s
site is the deposit and not a write matrix.

---

## §1 · THE THIRTY-EIGHT VERBS, IN FAMILIES

### 1.1 · Investigation — ⭐ **the family the suite has no axis for, and a third of what runs**

| verb | state | |
|---|---|---|
| `interview` | **RUNS** | |
| `research` | **RUNS** | |
| `surveil` | **RUNS** | |
| `reconstruct` | **RUNS** | |
| `examine` | **ATTEMPTED, ALWAYS REFUSED** | no question refers to a Site |
| `thread_read` | **NO EFFECT BODY** | `presence:<site>`-gated |

**Four of the eleven executing verbs are investigation acts.** No axis in the seven documents scores
*finding out* as a mechanic: the strategy corpus scores information as **fog of war** (a visibility
state) and the emergence corpus as **knowledge propagation** (who learns what, when). Neither scores
**an act whose purpose is to learn** — a deliberate expenditure of a bounded budget on acquiring a
claim. The management corpus's nearest neighbour is a research tree, which is a technology unlock and
not an epistemic act.

⚠ **This is the single largest gap in the suite's coverage of this tree, and it is a gap in the
suite.** Valoria's most-executing family is one thirty-three games gave the suite no reason to name.
The `resolution-diagnostic` and field-investigation (`FI`) lanes exist for it; the research corpus does
not reach it.

### 1.2 · Speech and information transport

| verb | state | |
|---|---|---|
| `utter` | **RUNS** | puts a Proposition in the world |
| `speak` | **RUNS** | seeds the claim `tell` then needs (`epistemic.py:156-160`) |
| `tell` | **RUNS** | contests *a standing*; resolves at a measured 21% |
| `refract` | **NO EFFECT BODY** | ⭐ **distortion in transit** — declared, unbuilt |
| `dispatch` | **NO EFFECT BODY** | `remit:dispatch` — the carried message |

**Partly covered, and the uncovered part is the interesting one.** The emergence corpus scores
propagation; `refract` is *distortion* in transit, which the suite raises only as a directive
(*"news should degrade"*) and never as a primitive with a carrier. Valoria declares the verb and does
not build it — and Part B `P6` is the adjacent finding: what travels today carries neither content nor
attenuation, so `refract` would have nothing to distort.

### 1.3 · Dockets, petitions and sittings — the S-UP demand channel

| verb | state | |
|---|---|---|
| `petition` | **NO EFFECT BODY** | `own` |
| `carry` | **NO EFFECT BODY** | `own` |
| `convene` | ⭐ **FOLDABLE, NEVER ATTEMPTED** — `_eff_convene` is registered and writes a `Date` | `remit:convene` |
| `determine` | **NO EFFECT BODY** | `remit:determine`; `grade: absent`; `judging_set` **raises** |
| `open_case` | **NO EFFECT BODY** | `remit:determine` |

**The chain is half-built and the built half is the lawful half.** `convene` puts a `Date` on the
calendar; CALENDAR fires it and forms a `DocketItem`; Q1 raises `date_due`; and `effects.py:181-182`
states the discipline — *"`convene` puts a date on the calendar and stops, which is `L5`: a clock may
not produce an outcome."* **What the sitting then decides is `H-32`/`W7` and is not built.**

The suite scores councils and assemblies as **an influence-priced vote** (a body with a scalar) or **a
bloc-dominance check**. Valoria's shape is neither: a scheduled occasion that **raises a question for
whoever holds standing**, and a person then chooses. **The suite has no cell for a deliberative body
that decides nothing.**

### 1.4 · Edicts and compliance — the S-DOWN channel

| verb | state | |
|---|---|---|
| `issue` | **NO EFFECT BODY** | `remit:issue`; writes `Dispensation.exists` |
| `comply` | **NO EFFECT BODY** | `own` |
| `evade / defy` | **NO EFFECT BODY** | `own` |
| `oblige` | **NO EFFECT BODY** | `own` |
| `repudiate` | **NO EFFECT BODY** | `own` |

**Wholly unbuilt, and the family the management corpus is richest in.** Every one of the nine titles
scores a policy or edict layer; Valoria declares five verbs for it and folds none. This is the
management corpus's core and this tree's largest declared-and-silent surface.

### 1.5 · Office, appointment and succession

| verb | state | |
|---|---|---|
| `confer` | ⭐ **FOLDABLE, NEVER ATTEMPTED** | `remit:confer`; `_eff_confer` opens a `hold` and closes the prior holder's |
| `revoke` | ⭐ **FOLDABLE, NEVER ATTEMPTED** | `remit:revoke`; the mirror of `confer` |
| `release` | **RUNS** | `own`; the generic closer, `grade: ruled`, domain = six tenure kinds |
| `establish` | **NO EFFECT BODY** | `remit:confer`; founds an `Office` |
| `succeed` | **NO EFFECT BODY** | `own`; `heir.designated` |
| `restore` | **NO EFFECT BODY** | `own`, `presence:<site>` |
| `commit` | **NO EFFECT BODY** | `own`; Q4's only question source; a standing ambition |
| `tie / knot` | **NO EFFECT BODY** | `own`; `grade: ruled` — Part B `P2` |

⚠ **`confer` and `revoke` are the sharpest single fact in this part.** Both have **working effect
bodies**. Neither is ever attempted, because `remit:` is unevaluable person-side (`H-71`) — and because
a `hold`'s subject must be a Person (ratified Layer 1, `04_CODE_ARCHITECTURE.md:181` row 12) while no
question produces one (Part B `P1`). **The appointment machinery is written, tested and unreachable**,
which is why *0 live `hold` tenures across 86 worlds* is not a thin fixture. The suite universally
scores delegation as *a named agent you appoint*; Valoria can appoint and never does.

**Succession** appears in the suite as inheritance of statistics or of a title. Valoria declares
`succeed` with `heir.designated` — **designation by an act**, not transmission by a rule — which is the
`AX-1`-shaped version and which the suite does not carry as a distinct primitive.

### 1.6 · Matter, labour and exchange

| verb | state | |
|---|---|---|
| `transfer` | **RUNS** | measured 21 of 723 refused |
| `move` | **RUNS** | 650 execute, 73 blocked; `budget` charges per leg |
| `create_record` | **RUNS** | writes stages that **mature at a later season** |
| `destroy_record` | **FOLDABLE, NEVER ATTEMPTED** | `hold:<record>`, `presence`; `H-75`: *cannot fire for any actor* |
| `work` | **ATTEMPTED, ALWAYS REFUSED** | `presence:<site>` — no question refers to a Site |
| `levy` | **NO EFFECT BODY** | `remit:issue`, `presence:<rung>` — taxation |
| `exchange` | **NO EFFECT BODY** | `own` — trade |
| `forge` | **NO EFFECT BODY** | `own`; declares `Record.forgery_quality` and never writes it |
| `kill / wound` | **FOLDABLE, NEVER ATTEMPTED** | `own`; excluded by the third gate — a contested verb whose `subject` cannot bind (`H-80`) |

**Taxation, markets and prices are declared and unbuilt**, and they are the strategy corpus's most
heavily scored family. `work` is the tree's only production act and no question reaches a Site — the
same grammar gap as `P1`, one object over.

### 1.7 · The act-wound clock — ⭐ **produced, and the suite has no primitive for it**

Not a verb: a **step**. MATTER matures act-declared stages at a later tick and writes `Record.matured`
(`loop/matter.py:55-109`). Its own comment: *"the only mechanism in the design by which one season's act
reaches into a later one WITHOUT anybody acting again"* — and it **stops if the maker is gone**.

The suite scores delayed consequence as a **timer** (a clock the world runs) or a **cohort lag** (a
demographic pipeline). This is neither: **an act that ripens, and dies with its author.** It is the
lawful form `T-c` promised — a clock with handles, because it has a maker who can be bribed, delayed,
burned or killed. **No title in thirty-three carries it, so no axis scores it.**

---

## §2 · THE CARRIERS, FROM THE INSTRUMENT

`matrix_rows_without_a_field()` (`state/carriers.py:591-624`) exists to report a write-matrix row that
names something the model does not have. Run on this tree, 2026-09-12:

```
$ python -c "from engine.season.state.carriers import matrix_rows_without_a_field as f; print(f())"

absent      (Office, remit) · (Person, axis_count) · (Person, claim_ledger)
            (Person, coherence) · (Person, scar) · (Proposition, *)
unmodelled  (Act[], returned) · (ConveningCondition, attached) · (Date, due_at)
            (Date, fired) · (Dispensation, exists) · (DocketItem, matter) · (Petition, exists)
```

**Thirteen declared rows with no field behind them, and the two categories mean different things.**

- **`absent`** — the carrier class exists and the field does not. `(Person, scar)` and
  `(Person, axis_count)` are the two persistence types Part E §3.3 scores **matrix-only**: the
  irreversible flag and the rewritten distribution, the suite's two most-cited emergence carriers, each
  a row naming nothing.
- **`unmodelled`** — the carrier class itself is not modelled. **Five of the seven are the docket and
  edict family**: `Petition`, `Dispensation`, `DocketItem`, `ConveningCondition`, and `Date` — which is
  *a dict rather than a class*, as `effects.py:178` says of itself: *"⚠ A DATE IS A DICT HERE, not a
  class."*

⚠ **So §1.3 and §1.4's silence is deeper than a missing effect body.** The verbs have no predicate
**and** their carriers are unmodelled. The governance layer is declared at the matrix and absent at the
model, which is a different and larger state than `tie / knot`'s — a `ruled` verb over a `Tenure` that
exists.

---

## §3 · WHAT THE REVERSE DIRECTION SHOWS

**3.1 · Three mechanics this tree runs that the suite has no vocabulary for.** Each is *produced*, and
each is invisible to Part E because no catalogued primitive names it:

| | the mechanic | what the suite scores instead |
|---|---|---|
| **1** | **the investigative act** — spending a bounded budget to acquire a claim | fog of war (a state) · knowledge propagation (a diffusion) · a research tree (an unlock) |
| **2** | **the act-wound clock** — a stage that ripens later and dies with its author | a timer the world runs · a demographic lag |
| **3** | **the deliberative occasion that decides nothing** — a scheduled date that raises a question for whoever holds standing | an influence-priced vote · a bloc-dominance check |

**3.2 · And the mirror: the suite's richest family is this tree's emptiest.** Policy and edicts —
`issue · comply · evade / defy · oblige · repudiate` — score in all nine management titles and fold
zero times here. Taxation and markets, the strategy corpus's most-scored family, are two declared verbs
with no predicate. **What Valoria runs and what the corpus scores are close to disjoint**, in both
directions, and Part E could only see one of them.

**3.3 · The execution profile, and the five verbs in the middle are the ones worth reading.** Of 38:
**11 run**, **20 have no effect body**, **2 are attempted and always refused**, and **5 are FOLDABLE AND
NEVER ATTEMPTED** — code written, tested and never reached:

| verb | why it never folds |
|---|---|
| `confer` | `remit:` unevaluable person-side (`H-71`) **and** a `hold` needs a Person subject no question supplies |
| `revoke` | the same, as `confer`'s mirror |
| `convene` | `remit:convene` — so the docket chain's built half is gated at its entrance |
| `destroy_record` | `H-75`: *cannot fire for any actor* |
| `kill / wound` | the third gate — a contested verb whose `subject` operand cannot bind (`H-80`) |

**Three of the five unreach for one reason: a question grammar that names no person.** Add the two
always-refused verbs, which unreach because it names no Site, and **seven of the 38 are blocked at the
grammar rather than at the code.** That is more verbs than the whole proposal set touches, and it is
the clearest statement available of why `P1` is ordered first.

**3.4 · Which restates Part B's ordering from a third direction.** Part A reached `P1` by auditing
documents; Part D reached it through ratified Layer 1's `hold` rule; this part reaches it by asking why
built code never runs. **Three independent routes to one clause is the strongest result in this set**,
and it is stronger than any one proposal in the set taken alone.

---

## §4 · WHAT THIS PART DOES NOT ESTABLISH

- **The family groupings are this part's**, not the tree's. `verb_table.yaml` carries a `stratum:`
  column; these families are cut for comparison against the suite's own categories and do not always
  follow it. The **roster** and the **execution states** are the tree's.
- **"The suite has no vocabulary for X" is a claim about seven documents**, not about game design. It
  means no axis, cluster or primitive in them scores X — checkable against the pinned sources
  (`04_CONSOLIDATION.md` §1), not from this repository.
- **No figure here was re-measured.** The 11-of-38 split and the per-verb counts are
  `requirements.yaml`'s and `verb_table.yaml`'s own; the carrier listing is an instrument run pasted
  above.
- **`grade:` is not execution.** Several verbs graded `ruled` do not fold, and one that runs (`move`) is
  graded `assumption`. Where the two disagree this part reports the execution state.
