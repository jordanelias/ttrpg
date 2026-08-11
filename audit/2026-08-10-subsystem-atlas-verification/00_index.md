# Subsystem atlas — verification corpus (2026-08-10, ED-IN-0152)

## Status: REFERENCE — working record; authors and ratifies nothing

The evidence behind the subsystem flow skeletons and the engine atlas. It is landed here because
the atlas cites it: a verification claim whose control lives only in a scratch directory is not a
control at all, and every count in the atlas's verification section resolves to a file below.

**Nothing here is canon.** These are the raw working papers of two tracing passes and their diffs,
recorded so the numbers can be checked rather than believed.

---

## Why two passes

The 15 flow skeletons (`systems/<x>/<x>_flow_skeleton_v1.md`) were produced by **grep-driven code
tracing**. That method has a characteristic blind spot: it finds what you thought to search for.
So a second pass re-derived the same subjects under an **inverted constraint** — no grep, no
pattern matching, files read whole, agents forbidden from opening the skeletons — and sourced from
the *declarative* surfaces instead of the code index.

The point was not redundancy. Two passes that share a method share its blind spots, and agreement
between them proves only that the method is consistent. Method-disjoint passes fail differently,
so where they agree the claim is corroborated, and where they disagree one of them is wrong in a
way the other could see.

**The prediction held.** The passes agreed on almost everything *reachability*-related and
disagreed mainly where a claim rested on a **registry** rather than on code. Grep tracing is
strong on "what calls what" and weak on "what was declared and never built"; reading the contracts
whole is the opposite.

---

## The files

| File | What it is |
|---|---|
| `contracts.md` | `references/module_contracts.yaml` read whole — all 27 modules, mapped to subsystem folders, with the internal contradictions found while reading |
| `indexes.md` | `mechanics_index.yaml` + `canonical_sources.yaml` + `CURRENT.md` read whole — per-subsystem heads, mechanic counts, code pointers, missing rows |
| `vector_audit.md` | The 2026-08-06 corpus vector audit's structural layer — import graph, cycles, cut-vertices, orphans, stub counts, execution-trace reachability, with a staleness verdict |
| `code_spine.md` | Whole-file read of the Key substrate, cross-scale layer, autoloads and the campaign driver |
| `code_personal.md` | Whole-file read of the combat resolver package and the characters modules |
| `code_strategic.md` | Whole-file read of the factions and settlements sims |
| `code_scene.md` | Whole-file read of the social-contest kernel and both mass-battle trees |
| `code_world.md` | Whole-file read of world, threadwork, fieldwork, and the four folders that hold no code |
| `DIFF_spine.md` · `DIFF_strategic.md` · `DIFF_scene.md` | The adjudicated diffs: every material claim bucketed CONFIRMED / MISSED / CONTRADICTED / SKELETON-ONLY / STALE-SOURCE, with each contradiction ruled against the code |
| `COMPARE_298_contradictions.md` | The shipped skeletons against PR #298's generated contract/key indexes — declared view vs as-built view |
| `COMPARE_298_integration.md` | Whether the two apparatus halves duplicate each other, and how they should relate |

---

## What it found

- **~168 claims independently rediscovered** across the 15 subsystems.
- **Three outright errors** in the shipped skeletons, all corrected: threadwork asserting a schema
  migration had not landed (it had, 2026-05-19, and the file contradicted its own §2); settlements'
  `Contracts:` header naming Python modules rather than contracts; factions labelling an
  unconditional branch a "fallback".
- **Four defects in PR #298's just-merged apparatus**, each verified before being touched and
  fixed under ED-IN-0152 — two key types reaching no review queue at all, a false "the contract
  side is simply unauthored" claim, a non-deterministic render, and a data error asserting IP is
  not a clocks key.

## What the second pass got WRONG

Recorded because a plausible-sounding claim is exactly what gets copied forward:

1. **`sigma_leverage` and `dice_engine` are NOT dead.** The agent that called them orphans had a
   scope that excluded combat; both are imported widely, several call sites reached from the
   season loop.
2. **`overview` IS present in the execution trace.** The agent read `by_subsystem_path` only and
   missed `by_contract`.

Neither survived adjudication, and both are named here so they are not resurrected from the raw
working papers by someone reading them without the diffs.
