# Architecture reconciliation — trace logs (2026-08-31)

## Status: **PROVENANCE ONLY. Nothing here is a design ruling, and nothing ratifies on merge.**
## `CLAUDE.md` §0.2 applies: **done means it runs, and none of the design these logs trace runs.**
## `CLAUDE.md` §0.05 applies: these are **reference**. No behaviour is correct because a row here says so.

These are the raw trace logs behind a Jordan-directed reconciliation of the code architecture across
PRs **#337–#344**. They are session work under `CLAUDE.md` §0's first carve-out — *"work is this
session's work if Jordan asked for it this session"* — and they are filed here rather than under
`audit/`, which §0 retires as a category.

**They are a SECONDARY SOURCE.** Every log was produced by an agent reading the tree; each carries its
own verification section marking claims VERIFIED-TRUE / VERIFIED-FALSE / UNVERIFIED. Where a log and
the working tree disagree, **the working tree wins** (`CLAUDE.md` §2).

---

## `pr_logs/` — one per pull request, tracing code-architecture content

| log | PR | merge | what the PR landed |
|---|---|---|---|
| `PR337.md` | #337 | `d73b5d3` | systems integration master + game precedent companion (6 parts, FILED reference) |
| `PR338.md` | #338 | `6760ffc` | the precedent matrix, the slice decomposition, the critique, the unified imports |
| `PR339.md` | #339 | `ef12ab1` | greenfield systems suite — eight systems on four primitives (**ARCHIVED same day**) |
| `PR340.md` | #340 | `606089d` | greenfield suite v2 — archive v1 after the adversarial critique, and rebuild |
| `PR341.md` | #341 | `920de97` | Fable 5 throughline critique — nine read-only adversarial passes over v2 |
| `PR342.md` | #342 | `57739a2` | Valoria from scratch — a suite built on the nine throughlines, audited |
| `PR343.md` | #343 | `72ab03b` | coverage, arc reachability, adversarial integration, the superseding document |
| `PR344.md` | #344 | `f129ca7` | adversarial review of #343 — the architecture is right, the vocabulary incomplete |

Each log carries: the commit history · an exhaustive ARCHITECTURE LOG table (keys, classes/types,
nodes/Godot constructs, containers/registries, modules/subsystems, function signatures, loop/phase
ordering, ownership, determinism, params/constants, invariants/refusals, claims-about-the-repo) ·
the named vocabulary introduced · claims about existing repo code with verification verdicts ·
Godot-specific content quoted · duplication/overlap signals · and the gaps the PR itself declares.

## `repo_logs/` — six repository sweeps, establishing what the tree actually contains

| log | lane | the question it answers |
|---|---|---|
| `R1_engine.md` | `engine/` | what architecture actually **executes** today |
| `R2_systems.md` | `systems/` | what the design source of truth already owns, and what the proposal re-invents |
| `R3_godot.md` | `godot/` + contracts | the port, the module contracts, and the **4.3-versus-4.6 evidence** |
| `R4_registries.md` | `references/`, `registers/`, `canon/` | the registries, the vocabulary, the ledgers, the open rulings |
| `R5_corpus_coverage.md` | `proposals/` | the **coverage measurement re-run**, and the uncited corpus mined |
| `R6_execution.md` | `research/`, `tests/`, `tools/`, `workplans/`, CI | what runs, what is pinned, and what the M1 board really says |

---

## Findings that were independently rediscovered by two or more lanes

Per `CLAUDE.md` §10's rank-by-independent-rediscovery, these are the bankable ones:

1. **Nothing in the #337–#344 design line executes.** `Person`, `Rung`, `Office`, `Site`, `Tenure`,
   `Query`, `Act`, `Event` and `Claim` are absent from `engine/` and `systems/` as named identifiers
   (R1, R6). `tools/m1_acceptance.py --summary` reports M1 at **0/7 junctures**, verdict NOT MET (R6).
2. **The running campaign resolves with zero people in it.** `world.npcs` is empty in every seeded
   campaign, `generate_npc` has no call site, and the population guards watch `world.npc_counter`,
   which only `generate_npc` increments — so a direct NPC loader is invisible to every existing check
   (PR337, PR338, R6).
3. **Two open Jordan rulings — ED-IN-0200 (centralized hierarchical key/module contracts) and
   ED-IN-0201 (the personnel precondition) — land 3–4 days before this design line and are cited by
   none of it** (PR338, R4).
4. **The coverage confession in `proposals/2026-08-31-ideal-v2/00_INDEX.md` is itself stale.** Its
   123/108 figures re-measure to **133 documents >200 lines, 30 cited, 103 uncited — 67.7% of the
   corpus uncited by line weight** (R5). Both are true of their own moment.
5. **Godot F-1, F-2 and F-3 are already remediated in the design; F-4 is not.** The `additive`
   order-independence claim still conflates clamp order with IEEE float summation order at
   `01_ARCHITECTURE.md:445-449` and `02_THE_SEASON_LOOP.md:570-573`, with no fixed-point fix (R3).
6. **The 84-error compile ratchet has only ever been measured under Godot 4.3.** Nobody has run 4.6
   against `valoria-game`, and the one artifact that positively asserted 4.6 no longer exists on
   `main` (R3).

## One conflict these logs do NOT settle, and that the adjudication stage exists to rule

**R1 and R2 reached opposite verdicts on whether this architecture already exists in code.** R1: *zero
design objects have a matching first-class type in `engine/`; this is greenfield, not a refactor.*
R2: *the Event/StateChange/witness/Claim/Query cluster is already canonical and executable as the Key
substrate.* Both cited code. The distinction is probably **named identifier versus functional
equivalent** — but that is a hypothesis, not the ruling, and it determines whether the authoritative
architecture is a greenfield build or a refactor onto `engine/substrate/`.
