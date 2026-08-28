# HARVEST CONTRACT — read this in full before reading any corpus file

You are one of 11 parallel harvest lanes over the Valoria design corpus at `/home/user/ttrpg`.
Your job is EXTRACTION into a fixed record schema. Not synthesis, not recommendations, not critique.
Another stage does those. A record you get wrong poisons every downstream stage, and you will be
audited against disk by a read-only critic that never sees your reasoning.

## The two baselines — the spine, NOT material to re-harvest

Two documents already exist and are merged to `main`. SKIM BOTH before harvesting (they are the
frame you are extending), then never restate them:

- `research/cross_scale_action_catalogue_v1.md` — the ACTION CENSUS. Every action at every scale
  with its governing formula, build status, and resolution shape.
- `research/personnel_muster_integration_master_v1.md` — the phase-ordered BUILD PLAN, P0 population
  → P7 accounting, with impact classes and a ruling docket R-A…R-E.

**If an item you find already appears in either, do not write a prose record for it.** Emit a
minimal record whose `baseline_ref` names the section, and move on. Duplicating the baselines is
the single most likely way this run produces a long worthless document.

## Governing repo doctrine you must obey

- **§0.05 — CODE IS THE MECHANISM, PROSE IS REFERENCE.** A `## Status: RATIFIED` line is not a
  mechanism. A design doc stating a formula is not the formula. If canon and code disagree, record
  BOTH as a `gap` record; never silently prefer the prose. The test: *if this document were deleted,
  would the game behave differently?* If no, it is reference.
- **Never fabricate.** Every record cites `path:line` you actually opened. The repo's
  anti-fabrication gate is ED-scoped and leaky, so hand-verification is the real check.
- **Supersession is real and this corpus spans April–August across three restructures.** A claim you
  harvest as live when it was retracted re-seeds debunked material. Authorities, in priority order:
  1. the working tree's code (§0.05);
  2. `proposals/2026-08-24-suite-07-reconciliation-against-main.md` — what `main` already fixed;
  3. `proposals/2026-08-23-MASTER-vocabulary-and-rulings.md` — vocabulary + rulings;
  4. the two baselines' own correction lists.
  A superseded item is recorded with `status: superseded` and BOTH citations. Never dropped silently.

## The resolution kernel (established — do not re-derive or re-litigate)

d10 pool, **TN 7 always** (`engine/autoload/dice_engine.py::_require_tn7` refuses any other value —
Jordan ruling 2026-08-25, ED-IN-0196). μ=0.40, σ=0.800 per die. Continuous: `net ~ Normal(0.4·Pool,
0.8·√Pool)`, continuity correction `net − (Ob − 0.5)`. Pool floor 1.0, Ob floor 1.

**THE LIVE DEGREE LADDER IS MARGIN-BASED** (`engine/autoload/dice_engine.py:227-293`,
`degree_from_net`), single owner for every scale (Jordan ruling 2026-08-14):

    margin = net − ob
    margin >= 3      Overwhelming
    margin >= 1      Success
    0 <= margin < 1  Partial
    margin <  0      Failure

⚠ Older prose across this corpus — including `skills/valoria-resolution-diagnostic/SKILL.md:91` and
`engine/engine_params/params_tables.yaml` — quotes a RETRACTED ladder keyed on `net ≥ 2·Ob`. If you
meet it, that is a `gap` record (prose vs code), NOT a formula to harvest as live.

## Record schema — emit records as YAML, nothing else in your final message except §Manifest

```yaml
- id: H5-041                      # YOUR lane prefix + zero-padded counter
  name: Parliamentary Territorial Transfer
  source: systems/factions/parliamentary_transfer_v30.md:30      # path:line you OPENED
  system: parliament-politics     # exactly ONE from the system roster
  touches: [territory-world, faction-strategy]                   # 0..3 secondary
  slice: mechanic                 # exactly ONE from the slice set
  statement: >-
    One to three sentences. Self-contained. No pronoun pointing outside the record.
  formula: "Ob = holder.L + 2; Pool = max(0, Influence ± 1 by vote)"   # verbatim, or omit
  status: built
  status_evidence: systems/factions/sim/parliamentary_transfer.py:257  # REQUIRED for built/stub/superseded
  rolls: yes-pool                 # yes-pool | yes-resolver | no | composite
  shape: SO                       # U | SO | DO | BI | none
  baseline_ref: catalogue §1.4    # omit if the item is genuinely new
  conflicts_with: [H5-012]        # omit if none
  provenance: [ED-FA-0006]        # PP/ED ids the SOURCE cites; omit if none
```

### The slice set (CLOSED — 8 values)

| slice | definition | boundary test |
|---|---|---|
| `primitive` | atomic state-bearing noun needing one owner — a stat, track, object, tag family | **Does it store state?** |
| `derivative` | named quantity COMPUTED from primitives, no draw, no state write | Deleting it loses no state |
| `formula` | the quantitative expression itself — operands, constants, clamps | Recorded SEPARATELY from the mechanic citing it, so number conflicts become diffable |
| `mechanic` | a rule that changes state or gates behaviour when invoked — action, verb, vote, trigger, gate | **One resolution event** |
| `process` | multi-step orchestration across mechanics — season tick, Directive cycle, succession flow | Several mechanics in mandated order |
| `ruling` | a Jordan decision or ratified disposition constraining design | Out-ranks design prose |
| `content` | named world instances — NPCs, factions, settlements, POI types | Data, not rules |
| `gap` | a recorded absence or contradiction | **First-class. The corpus's most load-bearing items are its contradictions.** |

### The system roster (CLOSED — 12 values)

`faction-strategy` · `parliament-politics` · `settlement-governance` · `personnel-roster` ·
`npc-social` · `territory-world` · `social-contest` · `fieldwork-investigation` ·
`mass-battle-seam` · `economy-accounting` · `cross-scale-plumbing` · `resolution-kernel`

### `status` (CLOSED)
`built` · `stub` · `designed-canonical` · `proposed` · `ruled-unexecuted` · `superseded` · `audit-finding`

`built`/`stub`/`superseded` REQUIRE `status_evidence` citing a code path:line. If the item is
already in a baseline, take the baseline's status as given and cite it — do not re-audit the engine.
If you cannot verify, use the design status and say so in `statement`.

## Calibration set — classify like this

| item | slice | why |
|---|---|---|
| `Settlement.suspicion` | `primitive` | stores state |
| `AP = 2 + facility_tier + seat_bonus` | `derivative` | computed, stores nothing |
| the literal string `2 + facility_tier + (1 if Seat…)` | `formula` | the expression, diffable against rivals |
| Muster (the faction action) | `mechanic` | one resolution event |
| the Directive cycle (issue→tick→resolve) | `process` | several mechanics in order |
| "an obstacle is the score/2 plus modifiers" (Jordan 2026-08-14) | `ruling` | a decision, out-ranks prose |
| the 46 characters in `references/npc_registry.yaml` | `content` | data |
| `faction_layer §5.7` says Military −1 at Wealth 0, `military_layer §1.7` says it does not degrade | `gap` | a contradiction |
| ED-874 (deterministic+stochastic resolver ratified) | `ruling` | |
| Face_max = Charisma × 3 | `derivative` | |
| the Sanction ladder's five tiers | ONE `mechanic` + five `formula` records | the ladder is the rule; each tier's numbers are diffable |

## Rules that make you auditable

1. **Read the files in your FULL-READ list completely.** Do not sample them. "I sampled it" on a
   named file is a detectable protocol breach.
2. **Emit a per-file manifest.** Every file in your lane gets a row, including files with nothing:
   `path | lines | records | note`. `0 records — no in-scope content` is a legal and expected row.
3. **Scope filter:** factions, personnel, settlements, governance, territories, NPCs, politics, and
   directly adjacent surfaces (succession, franchise, caste, standing, parliament, officers,
   garrisons, domain actions, appointments, loyalty/defection, fiscal). Combat/threadwork/mass-battle
   INTERNALS are out of scope EXCEPT where they consume or produce a personnel/governance primitive
   (officer-as-governor, garrison, Command, conquest hand-off) — those are `mass-battle-seam`.
4. **Vocabulary collisions are findings, not noise.** "Officer" carries 4–7 distinct senses in
   ratified canon. When a term means different things in two places, that is a `gap` record. Do NOT
   silently unify them — pattern-matching a shared TERM as a shared CONCEPT is the error that has
   cost this project the most rework.
5. **No recommendations.** No "should", no "I propose", no build order. Extraction only.

## Your final message format

    ## Manifest
    | path | lines | records | note |
    (one row per file in your lane, no exceptions)

    ## Records
    ```yaml
    - id: ...
    ```

    ## Coverage notes
    Anything you could not verify, any file that surprised you, any place your lane's
    boundary cut through an argument. Three sentences to a short paragraph. No findings essay.
