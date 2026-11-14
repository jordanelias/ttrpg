# SC · DICE — what has already been designed for proceedings and the social contest, collated against Jordan's rulings of 2026-11-14: in code, in workplan v12, or in neither

Written: 2026-11-14, the pass between stage 1 (the Opus interrogation of the code,
`2026-11-14-social-contest-attribute-interrogation.md`, in flight at this read: 32 lines) and stage 2 (a Fable redesign).
Read at the working tree of branch `exec/v12-b00-b03` on 2026-11-14 (HEAD `97dafad`). Read-only on code and plan: nothing
outside this file was edited. Jordan (2026-11-14): *"we have already designed much of this at different stages, so collate
all that is currently missing from code and the workplan that I identified and pass off to fable"*; and, relayed during
the pass: *"you may find fragments of this in proposals or .designs or .audits"*; *"we also have research and proposals
about the psychology of argumentation and persuasion"*; *"and I believe those even have been broken down into
primitives"*.

**Depends on:** stage 1 (the interrogation; its findings on the live roll are not repeated here); B01 and B01a .01–.04
(drawn attributes, `engine/season/harness/pairs.py`); the Spirit-group ruling (R5, not yet in
`references/descriptor_registry.yaml`).
**Lands in batch:** none (a collation; stage 2 decides the fold).

## Status: PROPOSED

Design input, reference under CLAUDE.md §0.05: it describes designs and code, it is not a mechanism. Every source under
`.designs/`, `.audit/` and `proposals/` is cited for INTENT only (CLAUDE.md §1: `.designs/` and `.audit/` are quarantined
reference, never authority; nothing may load them); where a `.designs/` banner names an original path it is given once,
at first citation. Lanes owning the files it reads: SC (`modules/social_contest/`, `systems/social_contest/`), IN
(`engine/season/`), DICE (`engine/dice_engine/`).

Markers: `[UNVERIFIED]` — a claim whose source was not opened in this pass (or opened only at its headings);
`[ASSUMPTION: … — basis]`. Line numbers are those read on 2026-11-14.

**Status vocabulary used in the inventory (one meaning each):**

| status | means |
|---|---|
| `LIVE` | executes in the season loop today: `modules/social_contest/roll.py`, `engine/season/**` |
| `KERNEL` | written as code in `systems/social_contest/sim/contest/` (the SC05 kernel), which the season loop does NOT reach: SC-05 measured it and kept the one roll (`modules/social_contest/roll.py:16-37`); its retirement is Jordan's (`SM-15`), and v12 retires it at B24.33 (`workplan_v12_part22_cont.md:83`). Code, not game. |
| `V12` | an item of workplan v12 (`proposals/2026-11-12-subsystem-audit-suite/master/workplan_v12/`) carries it; the handle is given |
| `BOTH` | `LIVE` and `V12` |
| `NONE` | designed somewhere, in neither the live code nor v12 (a `KERNEL`-only element counts as `NONE` for the game; the column says `KERNEL` so the code can be harvested) |

## 0. Jordan's rulings this collates against (abbreviated; verbatim in the interrogation's head and the coordinator's brief)

- **R1, the six roles.** Focus = staying on topic, not pulled into the irrelevant. Reason = constructing the argument,
  logical and evidentiary, able to account for the opponent's factual circumstances (resources, office, influence).
  Attunement = what will rattle the opponent, reading intent, reading the room, which kind of argument works on
  audience / adjudicator / opponent. Charisma = being listened to, compelling delivery. Grace = acting correctly for venue
  and occasion, being seen as respectable, remaining composed under difficulty. Will = keeping on arguing, self-belief,
  not getting rattled in the first place, the "x factor".
- **R2.** The subsystem uses all six in the manner specified.
- **R3.** Argue / speech / like verbs all call the social contest / proceedings subsystem: they all concern influencing
  people.
- **R4.** Proceedings have types set by what is at stake, which factions are involved, the venue, the adjudicators, the
  audience, how and what kind of arguments are presented and in what order, the verdict system; from heresy trial to
  parliamentary debate to private negotiation to rallying a crowd.
- **R5.** Spirit is its own attribute group: `attr.spirit.will` (renamed from `attr.mind.will`) and a new
  `attr.spirit.threadsensitivity`.
- **R6.** Dice are continuous (fractional dice and obstacles), no flat oppositions; tuning from curves over generated
  populations (`engine/season/harness/pairs.py`).
- **R7.** A duel is a restrained contest; a fight is pure combat (`unified/U1_GLOSSARY.md` rows).

## 1. What the live code is, in one paragraph (for the "in code?" column)

The one social roll the season loop runs is `modules/social_contest/roll.py::roll` (`:197-206`): `net = roll_net(pool) +
net_boost(leverage, pool)` against `ob = obstacle(inp)`. The obstacle (`:147-194`) is the task's `difficulty`
(`rosters.yaml: task_difficulty`) plus the opposing person's score halved, minus the room
(`reception_gain · reception + proof_step · proofs`, `:175`, only when the prize row says `heard_by: bench`), plus an
examined document's `forgery_quality`, capped by `obstacle_ceiling` (per-pool solved cap, `:65-86`). The pool is
`faculty(w, person, verb)` (`engine/season/seam/wrappers/sigma.py:225`, `pool.py`): one governing score per verb. The
leverage is `effort` only (`sigma.py:164`, `advantage_sources`). There is one draw per act: no exchanges, no proceeding
type, no adjudicator type, no audience, no venue parameter (the venue catalogue `engine/season/venues.yaml` is buildings
for seating people, `:64-119`, with no rhetorical property), no composure or rattle state, no topic. The SC05 kernel
(`systems/social_contest/sim/contest/`) holds most of the archived design as code, unreached.

## 2. Inventory

Columns: **element** | **origin · source** (origin labels: `JORDAN` a ruling; `RATIFIED` a design carrying a ratified
status in its own file; `PROPOSAL`; `AUDIT`; `IS` the instruction suite; `V11` a v11 workplan item; `CANON`;
`CODE-COMMENT`; `RESEARCH`) | **in code?** | **in v12? (handle)** | **status**.

### 2.A Proceeding types and their parameters (R4)

