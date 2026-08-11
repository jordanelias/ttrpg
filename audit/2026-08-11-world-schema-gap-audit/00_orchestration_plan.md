# World-Schema Gap Audit — orchestration plan

## Status: REFERENCE — method record for the ED-IN-0153 run. Ratifies nothing.

**Date:** 2026-08-11 · **Lane:** IN (cross-cutting) · **Base:** `63d4d0c` (ED-IN-0152)
**Instrument:** `.claude/wf_world_schema_gaps.js` (harness-synced, `tools/ci_wf_harness_check.py` green)

---

## 1. The question

Not *"is this system built?"* — that is already measured, by `references/ENGINE_ATLAS.md` §2
(declared vs executed), by the 15 `*_flow_skeleton_v1.md` §7 gap lists, and by the
`KEY_INDEX.md` / `CONTRACT_INDEX.md` review queues. Asking it again would rediscover known debt.

The question this run asks is one nothing in the corpus asks systematically:

> **What does the world model logically require that the *schema* cannot express?**

where the schema is exactly two authored surfaces —
`systems/_architecture/key_type_registry_v30.md` (55 key types) and
`references/module_contracts.yaml` (27 modules) — and everything in `references/` that renders them
is a generated **view**, not a source.

A blank cell in a generated view means *not declared*, which is not the same claim as *none*. The
distinction is the whole audit: an under-declaration is a filing question, a missing key type is a
design question, and an entity with no contract at all is a modelling question.

## 2. Why three passes and not one

The subject is decomposed along three orthogonal axes. Each pass sees the same tree and neither
sees the others' output. A gap reached by lanes from **different passes** is corroborated by
disjoint *method*, which is worth materially more than two lanes of one pass agreeing — the same
logic ED-IN-0152 applied retrospectively (grep-driven trace, then blind no-grep re-derivation),
applied here prospectively.

| Pass | Axis | Asks | Lanes |
|---|---|---|---|
| **A · Strata** | the entity ladder | per rung: what does canon say this rung *is*, and which of those facts has no key and no contract? | 4 |
| **B · Lenses** | 18 domain lenses | per lens, across every rung at once: what must the world remember, change, and announce? | 5 |
| **C · Config** | individuation / authoring | per entity class: what must be **authored** for an instance to be unique, consequential, and legible? | 3 |

**The ladder (A):** character → settlement → settlement faction & governance → territory/province →
provincial faction & governance → national faction & governance.

**The lenses (B):** beliefs and convictions · values and ethics · goals and ambitions · personal
history · social status · society (class, caste, culture) · demographics · religion · economics ·
military · invasion threats · geography · politics · geopolitics · diplomacy · world history ·
events · threadwork.

⚠ **Count corrected by second-pass adversarial review, 2026-08-11: that list enumerates EIGHTEEN, and this unit said 19 throughout.** The error is in the original decomposition, not the execution: Jordan's brief named 17 lenses, `history` was split into personal and world to make 18, and 19 was asserted without counting. Every downstream '19' inherited it — including this document's own table above, `03_discussion.md`, the workflow script's `meta.description`, and the ED-IN-0153 title. The coverage shortfall in `02` §4 item 1 is unaffected in substance (about 14 lenses visible in findings) but its denominator is 18.

**Pass C is a different class of question.** A and B ask what the engine must *remember and
announce*. C asks what must be *authored*. A world of 37 near-identical settlements and four
stat-block factions emits keys perfectly well and produces no narrative. Its three failure shapes
are named in the lane brief and each is a distinct gap kind:

1. **Flavour with no hook** — a distinguishing trait no system reads; two instances differ in prose
   and are identical in play.
2. **Hook with no variation** — a stat every instance carries at the same value; the mechanism
   exists and the individuation does not.
3. **Hardcoded singleton** — identity written as a named branch in code rather than as data on the
   instance, so a new instance cannot have it. This is **scripting drift** (CLAUDE.md §10) and is
   the failure mode this repo is most exposed to.

## 3. Agonist → antagonist

Per CLAUDE.md §10 the relay is **not a dialogue**: the twelve producer lanes are stateless, their
output is captured, and the critics are dispatched *with that output and not with the reasoning
behind it*. A critic that never read the producer's reasoning is a more independent check.

Independence is **structural, not declared**. Every critic stage routes through `hCritic()`, which
resolves `.claude/agents/valoria-critic.md` — `tools: Read, Grep, Glob`, no Write, no Edit, no Bash.
`tools/ci_wf_harness_check.py` fails any critic stage that omits it.

Findings are deduped by `hRediscover()` **before** the critics see them, so each critic is handed
corroboration groups rather than an arbitrary slice. Four clusters, disjoint by ladder rung, with
individuation and cross-rung findings in the fourth.

The critics are briefed on the three ways a claim of absence is most likely to be wrong *in this
corpus specifically*: the concept exists under another name in an adjacent subsystem; the producer
read a generated view instead of the authored source; or it is already filed (31 open ledger items
touch keys/contracts/schema, and most module rows carry their own `gap_notes`). An already-tracked
gap is a **soften**, not an uphold. They are also told to check the reverse failure — a proposal
that special-cases a named entity or grows a scale-local dialect is a defect in the *proposal* even
when the gap is real.

Every non-`uphold` verdict becomes a `run.dispute()` record built by `hVerdictDispute()`, so the
record carries its call site rather than silently defaulting every field.

## 4. Model tiering (CLAUDE.md §10)

| Stage | Tier | Why |
|---|---|---|
| A/B/C producer lanes (12) | `sonnet`, effort `high` | bounded reasoning against a fixed rubric over dispersed docs |
| Critics (4) | `opus`, effort `high` via `valoria-critic` | judgment under competing considerations; being wrong here is silent |
| Synthesis (1) | `opus`, effort `xhigh` | the stage that *gates* the result |

No `fable` stage: Jordan's 2026-07-28 ruling places `fable` on read-only audit / planner /
guardrail nodes and explicitly **not** on synthesis or artifact authorship, and this run's only
top-tier judgment node is the synthesis. Cache discipline (ED-IN-0087 fact 1): each pass fires one
lane and awaits its first token before fanning out the rest, because concurrent agents sharing a
prefix cannot read each other's cache.

## 5. Scope stops

- **The run edits nothing.** Its return value is the deliverable.
- **No renames.** The dotted-namespace nomenclature proposal was HELD for Jordan (ED-IN-0152) when
  this run was designed, and the constraint bound every lane. ⚠ **Updated at merge, 2026-08-11:**
  `main` has since landed `proposals/canonical_nomenclature_v1.md` (PR #301) — a **plan, PROPOSED
  only, ratifying nothing and renaming nothing**. The constraint therefore still holds exactly as
  stated, but the question is no longer only a held line item: read that proposal alongside this
  unit. Its headline is directly load-bearing on §5 of the gap register — the dotted namespace
  *already exists* in `names_index.yaml` (113 keys) and was never wired in, making this an
  **adoption** problem rather than a rename problem. It also independently reaches this audit's
  finding that Keys are the control group that works.
- **No scale-vocabulary unification.** Four vocabularies are unreconciled and HELD at ED-IN-0103
  fork 1. Lanes *record* the seam where they hit it; they do not resolve it.
- **No key type may actually be appended.** `key_type_registry_v30.md` §10 (RATIFIED 2026-07-07,
  ED-IN-0026) forbids appending a new type without a row in `references/rendering_dispositions.yaml`
  — **which does not exist**. Every `propose_key` row is therefore blocked on that file being
  created, and that blockage is itself a register row rather than an obstacle to route around.
- **Merging does not ratify.** Under ED-1094 a merge normally ratifies a PR's PROPOSED contents.
  This unit is called out as **held back** in full: the register is a set of observations against
  the tree, and dispositioning each row is per-lane design work.

## 6. Known limits of the instrument

- The `hRediscover` fuzzy key groups on *first cited file* + claim content words. Two lanes that
  reach one gap through different files will **not** group, so the rediscovery count is a floor,
  never a ceiling. It under-reports corroboration; it cannot over-report it.
- Report-only by ruling (Jordan, 2026-07-28): no signal aborts the run. A `stop_reason` other than
  `completed` in the returned summary means the reader should distrust *that part* of the run —
  it does not mean the run failed.
- A `null_result` signal on a lane means that lane returned zero findings. That is a real verdict
  and also an alarm; the lane's `coverage` and `clean` fields are what a reader uses to tell a
  clean surface from an unread one. The alarm ships paired with rediscovery ranking precisely so it
  never becomes pressure to manufacture findings.
- Three passes over one tree is not a proof of completeness. §7 of the findings document states
  what was not covered.

---

## 7. Correction — characters *are* NPCs (Jordan, in-session 2026-08-11)

**Valoria has no PC/NPC distinction.** The character entity is the `NPC` dataclass in
`systems/world/sim/npe.py`; there is no separate player-character schema because there is no
separate player-character *concept*.

This corrects a framing in this unit's pre-run grounding, which recorded *"no `Character` class
exists anywhere in the tree"*. That statement is **literally true and was verified** (`grep -rn
"^class .*Character" --include=*.py` returns zero hits) — but it is a claim about class *names* that
invited a false conclusion about the *model*: that a PC schema is missing. Nothing is missing on
that axis. The pattern is the one CLAUDE.md §0.1 names — a check that observes the wrong thing can
pass while the conclusion drawn from it is wrong.

**The measured gap survives the correction and sharpens under it.** Reading `NPC` as *the* character
type does not close anything; it relocates the finding:

- **No contract and no key family owns character identity.** All 27 modules in
  `references/module_contracts.yaml` treat `npc_id` / `actor_id` as an opaque foreign key. There is
  no owner, so there is no schema answer to *what a character is*.
- **Identity is recorded twice, at two scales, with no bridge.** `NPC.territory_id` binds a
  character at the *province* grain (`systems/world/sim/npe.py`), while `Settlement.npc_ids` binds
  at the settlement grain (`systems/settlements/sim/registry.py`). There is **no `settlement_id` on
  any character**, and nothing joins the two stores.
- The scene, conviction and belief systems key on a bare `actor_id` string, which is a *third*
  representation that joins to neither.

**The run is not invalidated by the correction.** Lane A1 was pointed at `npe.py` explicitly and
reached the character≡NPC framing on its own, without being told — its first finding is that no
module owns character/NPC identity, phrased in exactly those terms. That independent arrival is the
evidence the correction was to the *record* rather than to the *audit*. Where any later lane's
output rests on the superseded PC/NPC framing, this section governs and that lane's row is
re-stated in the findings register rather than carried forward.
