# Social contest: how to orchestrate and unify

## Status: PROPOSED (reference; resolves nothing; adopts nothing; it is a draft for one adversarial pass)

Answers: how do we turn the identified, flattened, deduplicated primitives into one clean system, in the docs, the
data and the code. Built on `2026-10-30-social-contest-reconciliation-and-distillation.md` (the 13-item model),
`...-code-audit.md` (what the code does) and Jordan's rulings R-1 to R-41. CLAUDE.md governs the form: one active plan
per lane, a carve-out named by the plan, done means it runs (§0.2), the full suite once per batch (§0.4), no guard
for a guard (§0.1 pt 5).

## 1. The unifying device: one owner per fact, and the owner is data

The duplication in the corpus is one pattern repeated: the same fact held in several places under several names
(credibility as `Standing`, `Face`, ethos, reception, charisma; a decision as a ballot, a tally, a vote, a count).
The cure is the one the repo already uses: **a single owner that the code reads, and nothing else holds the fact**
(CLAUDE.md §0.05, the "term, roster, closed set" clause).

Proposal: **one roster of contest sources**, a data table the roll composes from, with one row per source:

| field | meaning |
|---|---|
| `source` | `capability.attribute`, `capability.title`, `capability.office`, `capability.faction`, `argument`, `evidence`, `leverage`, `standing`, `reception`, `proofs_against`, `opposition_score`, `authority_weight`, `world_state` |
| `side` | `pool` (what a party brings) or `obstacle` (what stands against it): **declared once**, which is the double-counting rule: a source cannot appear on both sides, and a fact has one source |
| `producer` | the one function that reads it from the world (a Query) |
| `venue_key` | the arrangement key that turns it on, off or reweights it for this contest type (R-31, R-33) |

Everything that is today a parameter fed a constant (`leverage=0.0`, `pool_default`, the unread keys) becomes a row
with a producer or is deleted. The roll composes `pool = Σ pool-side rows`, `obstacle = Σ obstacle-side rows`, one draw,
one ladder (R-5, R-6, R-22, R-40). This is the only new object proposed, and it **replaces** `_pool_of`,
`_opposition_of`, the room terms and the capability map; it adds no verb. `[ASSUMPTION; medium: that a roster is the
right form; the alternative is editing the three existing sites. The adversarial pass is asked to attack this first.]`

## 2. The order of work (bottom-up; deletion first)

Each batch ends in an **execution artifact** (§0.2): a test that runs the behaviour end to end, which is also the
acceptance for the kind it touches. No batch adds a guard.

| batch | what | ends when | needs Jordan |
|---|---|---|---|
| **B0: settle** | the double-counting rule (§1); the ceiling's value (R-37); Layer-1 §A.3 wording (R-31); the mechanism of "crown modulates church" (R-34); whether local legitimacy acts on the verdict or on bench availability and enforcement (R-36, with the inquisition cases) | four rulings recorded in the ledger as verbatim rows | **yes: the only batch that does** |
| **B1: delete the free cuts** | the kernel (18 files, 9 break: six tests, two JSON pointers, one contract row); the 12 unread arrangement keys that no ruling needs (`records_dissent`, `term_required`, `venue_min_rank`, `registers`, `verdict_reasons`, `stakes_grade`...) while **keeping** the keys the rulings require (`disposal`, `bench_basis`, `floor`, `order`, `proofs`, `interposed`, `appeal_basis`, `disposal_reach`, `quorum`); the dead code in audit B-6 to B-10; the stale contract row | the suite is green with fewer files; one `FORK:` row names each deletion | no |
| **B2: one engine** | the source roster; a continuous pool (remove the `int` cast at `sigma.py:131`); producers for capability (attribute, title, office, faction), argument, evidence and leverage; the new ceiling; Partial writes a docket matter | a probe that shows pool **varies by person** and a Partial leaves a docket matter; goldens re-recorded and **said so plainly** (§7) | no (after B0) |
| **B3: one action surface** | the venue row's `floor`, `order`, `proofs` and `interposed` gate which acts are admitted (in `state/gate.py`'s admission); the speech-kind roster becomes a field of `speak` with aptness priced (R-16) | the same actor is admitted to `speak` in one row and refused in another, by the row alone | no |
| **B4: authority** | `bench_basis` names an authority; offices tie to authorities by one spelling (`body` or `faction`, not both); a per-territory legitimacy Query over the persons present (S-7, S10.1); office weight (R-31, R-38) scaled by it | a heresy proceeding and a royal tribunal, same accused, different benches and weights, by data | the mechanism choice from B0 |
| **B5: deciders** | the count over `commit` edges as a Query that licenses or blocks the owner's act (R-29); a mutual row (negotiation) with agree or impasse; a bench of two or more | a council motion carries or fails by count; a negotiation ends in `commit` or impasse | no |
| **B6: reach and reaction** | disposal reach set by the row; witnessing at news speed; reasons to convene (a petition, a vacancy) producing sittings in computed play | a computed season forms a sitting for a reason the world supplied | no |
| **B7: the rest as rows** | seed the unseeded rows (negotiation, envoys, audience, appeal as a route, succession) from `research/social_contest_procedures/` | each row constructs and reaches the roll | no |

**Why this order.** Deletion first shrinks what every later batch must read. The engine (B2) comes before the action
surface (B3), because B3's gate needs a source to limit. Authority (B4) needs the roster. Deciders (B5) need the
admission gate. Reach (B6) needs a decider to disclose. Rows (B7) are data once all of that exists.

## 3. How to run it

- **One carve-out, named by the SC lane's plan** (CLAUDE.md §2): the batches above are its positions; the plan names them and schedules nothing. The superseded proposal text is retired in the same commit by deletion plus a `FORK:` row, not kept on disk.
- **`methodology-execute` per batch**: `valoria-author` builds each item cheaply; `methodology-close` runs once per batch; a closed batch is deleted from the plan and the next opens with a cleared window.
- **Model tiers** (§10): measurement on Haiku (counts, greps, the probe); wiring on Sonnet; the B0 judgments and each batch's verify stage on Opus; `fable` audits and does not author. Fan-out is sized to the batch: B1 is one producer, B3 and B4 each two lanes (the gate; the data) with a shared extract.
- **The agonist–antagonist relay is used at three nodes only:** the source roster (B0), the authority mechanism (B4), and the count (B5), each once, per CLAUDE.md §0's one-round rule.
- **The acceptance instrument is the existing kind of thing**: a test per kind that runs it (the K1 `tell`, the K3 trial, the K6 count). The probe built for this audit is a measurement, kept out of `tests/` until one of its lines becomes such a test.

## 4. What this deliberately does not do

- It builds nothing in B0. Four decisions are Jordan's; the rest follows from rulings already given.
- It does not mechanise the classical or modern persuasion theories. They fill the aptness table and name which sources exist; the engine's inputs are the roster's rows.
- It does not port. The Python is the oracle (CLAUDE.md §6); the port waits on its own gate.
- It does not re-open the kernel's retirement timing beyond B1; if Jordan wants it later, B1 shrinks by one item.
