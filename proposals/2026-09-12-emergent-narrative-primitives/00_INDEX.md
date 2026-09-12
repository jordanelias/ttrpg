# Emergent-narrative primitives — four research documents, audited and curated

## Status: **PROPOSED (2026-09-12, ED-IN-0217). HELD BACK FROM RATIFICATION-ON-MERGE, IN FULL.**

⚠ **ED-1094 does NOT apply to this set, and the exception is stated here rather than assumed.**
Merging a PR normally ratifies its `PROPOSED` contents by default. **Nothing in these four files
ratifies on merge.** Every proposal is a design object for Jordan to accept, amend or refuse.
Landing this directory changes no `## Status:` line, no ledger row, no `CURRENT.md` row and no code.

---

## What this is

**Jordan, this session:** read four research documents in the context of each other and of the
repository as it stands; run an adversarial pessimistic **NERS** audit of each document's mechanics
and proposals; have **Fable 5.1, read-only**, use those findings to interrogate the game; then
identify and propose the most apt mechanics, curated for gameplay, emergence, applicability,
relevancy, immediate impact and implications going forward; and pass all of it to **Opus** to write
out in **agonist–antagonist** methodology with fidelity to findings.

**Read in this order:**

| file | what it holds |
|---|---|
| `00_INDEX.md` | this — the finding, the set in one table, what is **not** claimed |
| `01_THE_PASSES.md` | **Part A** — the three NERS passes: **21 false N-lines**, the mechanism Valoria already shipped and which broke, what Valoria **cannot adopt at any price**, where the documents are **wrong about a game like this one**, the minimum-viable machine scored against the tree, and **§7, the read-only interrogation's seven answers** |
| `02_PROPOSALS.md` | **Part B** — the curated set, each stated by an **agonist**, attacked by an **antagonist**, closed with its **residual**. Plus three measurements handed over, and the one thing to refuse |
| `03_PROVENANCE.md` | **Part C** — how it was produced, the execution artifacts pasted, **seven corrections** made to this session's own work and to the passes it commissioned, source tiers, and what could not be established |

---

## The finding, in one paragraph

**The repository does not lack these primitives. It has almost all of them as carriers, and nearly
none of them as producers.** Three independent NERS passes, run against three different documents,
converged on that sentence and produced **twenty-one false N-lines** between them: mixed success,
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
| **M1–M3** | Measurements handed over — the unreachable band · `standing_of` as `H-116` at a second site · two engines disagreeing about a sub-season timestep | — | — | no ruling; no one-object repair |
| **§R** | **The one thing to refuse** — salience-ranked memory | — | — | — |

**Nothing in this set adds a system.** Four of five proposals are a clause, an argument, an effect
body composing on an existing primitive, and a deletion. The remediation standard `skills/ners/SKILL.md`
sets — *"a few edits, most of them deletions, leaving the vocabulary shorter"* — is met, and where it
is not met the item is filed as a measurement rather than dressed as a repair.

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
```

**GRADE: `paper`** for every primitive and proposal in all four documents as a Valoria candidate —
nothing in them executes here. **The tree runs and is not yet a game.** The execution step that is
the whole difference is not a design: it is a producer, and `P1` is the smallest one that makes the
others reachable.
