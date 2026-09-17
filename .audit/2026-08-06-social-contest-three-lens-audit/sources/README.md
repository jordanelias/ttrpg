# Source documents — the five-document persuasion/political-mechanics series

## Status: SOURCE MATERIAL — verbatim, NOT canon, NOT ratified, NOT Valoria design text
## Preserved 2026-08-06 (ED-SC-0025) · Lane: SC

These are Jordan's uploaded research/design documents, copied here **verbatim and unmodified** so that
the citation spine of our filed work resolves. Nothing in this directory is Valoria canon; nothing here
may be cited as a ratified rule. They are the *inputs* our audit and proposals reason about.

## Why they are in the repo

`ED-SC-0017` flagged that `params/contest.md` is cited 97× across the kernel and no longer exists on
disk — the anti-fabrication gate's own citation spine, broken. While adjudicating documents 4 and 5, a
lens could not read the uploads at all and correctly reported that **we had begun filing EDs
(ED-SC-0021, ED-SC-0023, ED-SC-0024) that cite — and now retract against — documents with no on-disk
provenance.** That is the same failure mode, freshly created by us. Copying them here closes it.

## The series, in order

| File | Doc | What it is |
|---|---|---|
| `01_political_mechanics_primitives.md` | 1 | Research → 45 primitives (P1–P45) in seven families; four assembled scenes; self-audit (A1–A11) |
| `02_political_state_graphs.md` | 2 | Eight political systems as state graphs in the P-vocabulary, plus a **computed** interrogation (incidence matrix, tiers, Jaccard clusters, call graph, throughlines) |
| `02a_interrogate.py` | 2 | The script that produced document 2's overlap analysis |
| `03_consolidation.md` | 3 | The distillation: 45 primitives → **14 mechanisms + 31 configurations**; the four-resource economy; M2 Scope; three loops replacing eight graphs; the faction opposition model |
| `04_negotiation_and_persuasion.md` | 4 | The pivot from propositions to **minds**: story model, ELM routes, Cialdini, reactance/inoculation, anchoring, deliberation dynamics. Primitives N1–N11 |
| `05_persuasion_in_the_era_sources.md` | 5 | **Newest.** Corrects doc 4's A4 by finding the counterpart-facing Chinese tradition (Guiguzi, Han Feizi). Primitives N12–N20 |

## Three things a reader must know before citing any of this

1. **Document 4 retracts document 3's warrant × attack matrix as fabricated** — "invented rather than
   derived … formatted to look rigorous" (doc 4, opening). Our own Fork B (ED-SC-0021) and CIP-2
   endorsed that matrix before doc 4 was available. See `../03_persuasion_documents_adjudication.md`
   for the disposition.
2. **Document 5's own audit finding B1 puts a `[TIER-FLOOR: T2]` on its Chinese material** — the
   Guiguzi chapter list is a *publisher's table of contents*, the doctrinal claims come from a database
   summary, and the Han Feizi material from an encyclopedia rendering. Doc 5 says plainly that "every
   specific technique in N12–N16 rests on a paraphrase of a paraphrase." **These may be adopted as game
   design on their merits; they may NOT be cited as historically grounded in a ratified Valoria doc.**
   The one properly-T1 claim that survives regardless is Gentz's comparative thesis (European rhetoric
   is forum-facing; the Guiguzi is counterpart-facing).
3. **The series corrects itself each iteration**, and doc 5's own reviewer notes the pathology: doc 3
   distilled 45 → 14, then docs 4 and 5 added 20 more without re-running the separation rule. Our
   re-distillation (adjudication §4) recovers it: **20 N-primitives → 5 mechanisms.**

Everything else these documents contain is reasoned about, with dispositions, in
`../03_persuasion_documents_adjudication.md` and `proposals/social_contest_consolidation_integration_v1.md`.
