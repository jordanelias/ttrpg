# Emergent-narrative primitives — seven research documents, audited, curated, and plotted

## Status: **PROPOSED (2026-09-12, ED-IN-0217). HELD BACK FROM RATIFICATION-ON-MERGE, IN FULL.**

⚠ **ED-1094 does NOT apply to this set, and the exception is stated here rather than assumed.**
Merging a PR normally ratifies its `PROPOSED` contents by default. **Nothing in these seven files
ratifies on merge.** Every proposal is a design object for Jordan to accept, amend or refuse.
Landing this directory changes no `## Status:` line, no ledger row, no `CURRENT.md` row and no code.

---

## What this is

**The ask arrived in four instalments, and the set is structured the way the ask was.** Stated in
full because Parts D and E exist only because of instalments two through four:

1. *(four documents)* Read them in the context of each other and of the repository as it stands; run
   an adversarial pessimistic **NERS** audit of each document's mechanics and proposals; have
   **Fable 5.1, read-only**, use those findings to interrogate the game; then identify and propose the
   most apt mechanics, curated for gameplay, emergence, applicability, relevancy, immediate impact and
   implications going forward; and pass all of it to **Opus** to write out in **agonist–antagonist**
   methodology with fidelity to findings. → **Parts A, B, C**
2. *(three more documents)* *"I feel like you missed out on context… read these and perform some
   exercise then consolidate them with the original four."* → **Part D**
3. The documents fall into three groups — **management, strategy, emergence** — and each evaluates
   games against many axes: *"analyze the Valoria game across each axis, so we see what it does for
   each design quality/system/mechanic queried in the document suite."* → **Part E** §1–§6
4. At the granularity of *"the clusters/axes/sets of primitives/mechanics."* → **Part E** §7, the
   primitive ledger

**Read in this order:**

| file | what it holds |
|---|---|
| `00_INDEX.md` | this — the finding, the set in one table, what is **not** claimed |
| `01_THE_PASSES.md` | **Part A** — the three NERS passes on the first four documents: **27 false N-lines**, the mechanism Valoria already shipped and which broke, what Valoria **cannot adopt at any price**, where the documents are **wrong about a game like this one**, the minimum-viable machine scored against the tree, and **§7, the read-only interrogation's seven answers** |
| `02_PROPOSALS.md` | **Part B** — the curated set, each stated by an **agonist**, attacked by an **antagonist**, closed with its **residual**. Plus three measurements handed over, and the one thing to refuse |
| `03_PROVENANCE.md` | **Part C** — how it was produced, the execution artifacts pasted, the **corrections** made to this session's own work and to the passes it commissioned, source tiers, and what could not be established |
| `04_CONSOLIDATION.md` | **Part D** — the three later documents: which two are **earlier drafts** of documents already audited and which one is **new**, the cut run on its **six proposals** (0 adoptable, 1 a `[NULL:]`), the nine-item asymmetry map cut, and **all seven documents in one frame with a tally** |
| `05_VALORIA_PLOTTED.md` | **Part E** — **Valoria plotted on every axis the suite carries** (management 7+5 · strategy I–VII + 8 families · emergence's four sets, four control parameters, eight persistence types, scale ladder, fourteen requirements), then **§7, the primitive ledger**: all **76** catalogued mechanics scored in an eight-term vocabulary, with the counting rule that reproduces the tally |
| `06_VALORIA_UNPLOTTED.md` | **Part F** — **the ledger run backwards.** All **38 verbs** of the shipped grammar in families, each with a *derived* execution state, plus the 13 declared carriers an instrument reports as having no field. Names the three mechanics this tree runs that the suite has no vocabulary for, and the five verbs that are **built and never reached** |

---

## The finding, in one paragraph

**The repository does not lack these primitives. It has almost all of them as carriers, and nearly
none of them as producers.** Three independent NERS passes, run against three different documents,
converged on that sentence and produced **twenty-seven false N-lines** between them: mixed success,
stale information, the storylet, disposition-rewriting, delegation-as-character, the persistence
taxonomy, the opinion scalar, the action-point budget, the rule-bound automaton, punished
allegiance-switching, the ageing cohort — each is already an object in this tree, and each is
unwritten, unreached, or already ruled on with a date. Adopting one adds a second empty carrier
beside a first. **And the read-only interrogation then found the reason they stay empty, which no
pass had reached and which reorders everything:**

> **No question in the shipped grammar ever has another person as its referent — so no candidate
> ever has another person as its subject.**

Measured this session by instrumenting `opening_set` across the corpus: **177,170 candidates
formed; 17,400 carry a person id as their subject; every one of those is the asker naming
themselves; zero name anyone else.** A candidate takes its subject from its question
(`decision/options.py:93,102`), and no question source produces a person.

That single fact explains the three holes the tree has been carrying separately. `H-62`'s planned
producer, **`W-F`, would write stance rows onto a scorer whose `c.subject` is never another
actor — a producer with no consumer.** `tie / knot`'s missing effect is **not** the reach
bottleneck, because its Tenure binds to the act's subject, which is a question referent, which is
never a person. And the live scorer's second term, `stance_toward(p, c.subject)`, cannot fire toward
anybody — which is why, in the world the loop actually drives, **no person holds a post, no person
has a disposition, and no person has a competence**, simultaneously and for one reason.

---

## The set

| | proposal | size | waits on | what it moves |
|---|---|---|---|---|
| **P1** | **A person-referent route into DELIBERATE** — one clause at `queries/world_q.py:213` admitting a claim whose subject is a Person id | **one clause** | nothing | makes `W-F`'s consumer exist. `R-01`, `R-02` (`not_met`), `R-07`, `R-08` (`partial`) |
| **P2** | `tie / knot`'s **effect body, as two directed edges**, with its stale note corrected against ratified Layer 1 | one effect body; six re-records | **P1** | `R-05`; the relationship channel, and *"I have cut you off and you do not know it"* |
| **P3** | **The deposit stamps the act, not the channel** — one argument at `loop/witness.py:121` | **one argument** | nothing | hearsay becomes separable from testimony; breaks a measured `utter`-over-`tell` dominance |
| **P4** | **`UPSET_FLOOR` — let the seam accept `wound_state`** | a deletion | — | an attribution contradiction measured at **6.06%**. ⚠ **PC lane; observation only** |
| **P5** | **The warrant for `W-F`'s magnitudes** — narrowed to two directions, with one **design call** surfaced | prose | `W-F` | converts *invented* into *warranted*, and no further |
| **P6** | **A telling about a person deposits in the namespace `standing_of` already reads** — `tell`'s precondition reads the teller's claim and the deposit discards it. `epistemic.py:82-83` names this as `H-116`'s open other half: *"WITNESS depositing claims in that namespace — is not this item"* | one branch at the deposit + a second Observation; no new field, no roster change | nothing | gives `standing_of` its **producer** — it returns a constant for every person in every world today. `R-07` |
| **M1–M4** | Measurements handed over — the unreachable band · `standing_of` as `H-116` at a second site · two engines disagreeing about a sub-season timestep · `choice_temperature`'s disputed control arm | — | — | no ruling; no one-object repair |
| **§R** | **The one thing to refuse** — salience-ranked memory | — | — | — |

**Nothing in this set adds a system.** Five of six proposals are a clause, an argument, an effect
body composing on an existing primitive, a deletion, and a payload field read at one branch. The
remediation standard `skills/ners/SKILL.md` sets — *"a few edits, most of them deletions, leaving the
vocabulary shorter"* — is met, and where it is not met the item is filed as a measurement rather than
dressed as a repair.

**Belief-with-provenance is the shape the corpus finds rarest — 2 of 20 titles — and this tree has every
carrier for it and a producer for none.** `P1` makes a person formable-about; `P3` puts a **speaker** in a
claim's `source`; `P6` puts the **content of what was said** in its `predicate` and `value`.

⚠ **`P6` is the one with a consumer already written and already starved.** `standing_of`
(`decision/options.py:444-465`) pairs told-against-own claims **by predicate** over `person_predicates`,
and returns maximum gap for every person in every world because `witness.py` never stamps `told_by`, so
`paired == 0` **by construction**. `epistemic.py:82-83` names the missing half in its own words —
*"`H-116`'s other half — WITNESS depositing claims in that namespace — is not this item"* — and `P6` is
that half.

---

## What is NOT claimed, and whose it already is

This is the half that keeps the set honest, and two items in it were **withdrawn from this
document's own first draft** after checking.

- **`W-F` / `U5` — an outcome moves `Person.stance` — is already planned**, specified down to the
  YAML with guardrails, acceptance, falsifiers and control arms
  (`workplans/2026-09-09-r-execution-plan.md:1324`). This session identified it early as the
  highest-value move and **does not claim it.** What it proposes instead is the thing that plan
  declares it lacks, in its own words: *"The magnitudes are INVENTED and this row is what makes that
  lawful."*
- **`H-71`** (`remit:` evaluable person-side) and **`H-62`** are existing tier-0 register rows. One
  commissioned pass calls `H-71` *the single highest-value object in the tree*; Jordan's **R7** calls
  `H-62` *"unavoidable and first-rank."* Named here, not re-proposed.
- **The conviction-matrix re-centring is `ED-IN-0214`** and Jordan's. D1's quantified variety trap is
  independent corroboration and changes nothing about who answers it.
- **An earlier draft of this document proposed `tie / knot`'s effect as *the* reach channel.** The
  interrogation showed that is wrong. `P2` is demoted in place, and the demotion is left legible.
- **An earlier draft claimed the source stamp revives `standing_of`.** It does not — that function is
  starved on a second, larger axis. `P3` is cut in half and `M2` carries what remains.

**No new `needs_jordan` row is filed.** Two candidates were tested against `CLAUDE.md` §0's five
gates and closed (`03_PROVENANCE.md` §6). One genuinely open **design call** is surfaced inside `P5`
— *the sign of a `Failure` interior write* — and it attaches to a plan Jordan already owns rather
than opening a queue entry.

---

## What the documents are, and how far they are trusted

| | document | admitted as evidence for | refused as evidence for |
|---|---|---|---|
| **D0** | *Emergent Narrative in Games: A Research Compendium* | the field's shape; the fabula/syuzhet split | any constant |
| **D1** | *Emergent Narrative: Mechanical Specifications* | directions, couplings, the minimum-machine checklist | its `[TIER-FLOOR: T2]` community constants |
| **D2** | *Thirteen Strategy Games Across Seven Design Qualities* | primitive shapes and their tensions | its playability scores — **and its one-clock finding, which `01_` §5.1 shows is confounded on the document's own text** |
| **D3** | *Citizens, Settlements, Factions — Nine Titles* | primitive shapes; its directives as tests | any constant — **it disowns them itself**: *"a catalogue of folk models… not acceptable for any claim about a specific constant"* |

Every number the documents carry stays `[OPEN — Jordan tuning]`. `skills/ners/SKILL.md` §11: *"the
form is the audit's business; the values are not."*

---

## The instruments, run on this tree

```
register --requirements   met 1 · not_met 4 · partial 4
m1_acceptance --summary   NOT MET, 2 rows failing
corpus_run                11 of 38 verbs execute · 89 worlds → 25 distinct executed sets
                          degrees {Failure 386 · Partial 60 · Success 37 · Overwhelming 0}
opening_set instrumented  177,170 candidates · 17,400 self-subject · 0 other-person subject
build_world(0)            3 persons · 0 live `hold` tenures · stance [] · capability {} for all
[computed, exact]         pool 2 vs Ob 2 → 74% / 19% / 7% / 0%; max margin +2, band needs ≥3
matrix_rows_without_a_field()
                          13 declared rows with no field — 6 absent, 7 unmodelled
25 worlds driven, full spans   4,499 claims deposited, ALL `firsthand` · 0 `told_by` ·
                          standing_of == max gap for 75 of 75 persons
verb_table × EFFECTS      11 run · 5 foldable and never attempted · 2 always refused ·
                          20 with no effect body
```

**GRADE: `paper`** for every primitive and proposal in all seven documents as a Valoria candidate —
nothing in them executes here. **The tree runs and is not yet a game.** The execution step that is the
whole difference is not a design: it is a producer.

**And `P1` is reached three times, by three routes that did not see each other** — which is the
strongest single result in this set:

1. **Part A/B**, auditing the documents: no question source produces a person, so no candidate carries
   one as a subject (measured over 177,170 candidates).
2. **Part D §5**, from ratified canon: a `Tenure` is owned by its subject; Layer 1 requires a `hold`'s
   subject to be a **Person**; a computed act's subject is its question's referent. **So Layer 1 as
   ratified is unsatisfiable by the running grammar**, and `P1` is a conformance repair rather than a
   new idea.
3. **Part F §3.3**, from the other end: five verbs are **built, tested and never reached**, and three of
   the five — `confer`, `revoke`, `convene` — unreach because no question names a person.

Three independent routes to one clause is worth more than any of the six proposals taken alone.
