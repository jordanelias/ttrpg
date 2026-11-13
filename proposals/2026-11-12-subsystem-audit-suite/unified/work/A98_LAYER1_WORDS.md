# A-98 · the retired words in Layer 1 (listed, not edited)

## Status: REFERENCE (a lane's list for the Layer 1 amendment lane; resolves nothing at runtime; not canon)

## Read at: the working tree, 2026-11-12, `grep -rniE` over `architecture/` for *talent, aptitude, prowess, trained score/rank, training, capability*. Lane: A-98 vocabulary sweep. `architecture/` was not edited (a parallel lane amends it under A-97).

**Result.** Layer 1 uses none of *talent*, *aptitude*, *prowess*, *trained score* or *training* (for a rank). It
uses **capability**, almost always as the identifier (`Person.capability`, the `capability` eligibility kind), which
A-98 keeps; the prose uses below are the only places where the word stands for *skill* in a sentence. Each is a
candidate for the Layer 1 lane's wording, not an edit this lane makes (Layer 1 is amended only by Jordan's
direction, A-97).

| file:line | text (abridged) | sense | what A-98's word would be |
|---|---|---|---|
| `architecture/meta/03_VERBS_AND_LOOPS.md:22` | heading "§A.2 · Eligibility is never capability" | a person's skill | "Eligibility is never a skill" (or keep, with `capability` in backticks as the field) |
| `architecture/meta/04_CODE_ARCHITECTURE.md:1062` | PART D row 33 "eligibility by capability, or a seat that gates or adds a bonus" | a person's skill | "eligibility by skill (`capability`) …"; the row's second half already writes the identifier in backticks |
| `architecture/meta/04_CODE_ARCHITECTURE.md:351`, `:490` | "`eligibility_kinds` has no `capability` member"; "**`capability` refused by name**" | identifier | none (identifier, kept) |
| `architecture/meta/04_CODE_ARCHITECTURE.md:234`; `holonic_ARCHITECTURE.md:324`, `:332`, `:345` | `Person := ( id, weight, capability, … )`; "§9.2 `capability` supplies dice and gates nothing" | identifier | none (identifier, kept); the rename to `skills` is the candidate v12 batch (glossary §H) |
| `architecture/holonic_ARCHITECTURE.md:433` | "`pool(act by remit) = capability of the dispatched establishment member(s)…`" (inside a code quote) | a person's skill score | "skill score" if the quotation is ever reworded; it is a quoted formula |
| `architecture/holonic_ARCHITECTURE.md:730`, `:1303`, `:1385` | "everything interior — `marks`, `capability`, …"; "plus capability, plus this new claim"; "claimants, capability, marks" | the field, in lists | "skills" in prose where the field is not meant |
| `architecture/ARCHITECTURE_V2.md:395`, `:445`, `:497`; `architecture/PLAN.md:723`, `:742`, `:1947` | "NEVER capability"; "capability gates no verb"; "never `capability`" | the eligibility kind (identifier) | none |
| `architecture/meta/01_AXIOMS.md:297`, `:1229`; `holonic_ARCHITECTURE.md:494`; `VOCABULARY.md:127` | "a capability the engine requires"; "Every capability survives"; "not a capability the…" | ordinary English (a power to do something; a provider role) | none: not the quantity A-98 names |
| `architecture/meta/01_AXIOMS.md:772`, `:844`, `:849`, `:862`, `:904` | "`weight`, `capability` (§D.1.1's fifth category)"; "`capability` supplies dice at RESOLVE" | identifier | none |

**Not checked:** *score* used bare in Layer 1 (A-98 (5) asks the suite never to write bare "score"; Layer 1's
uses were not swept, one round). `architecture/VOCABULARY.md` is a PROPOSED ballot and owns no term (glossary head).
