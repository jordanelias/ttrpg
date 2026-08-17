# Weekly code review — commits `d36498f`..`f2fc307` (2026-08-10 .. 2026-08-16)

## Status: REFERENCE — observation with evidence; nothing ruled, nothing executed

## Date: 2026-08-17 · Lane: IN (cross-cutting) · ED-IN-0194

> ⚠ **SUPERSEDED IN FOUR PLACES by `01_consolidation.md` (same date).** Three Fable-5 read-only
> critics audited this document; all eleven findings and five throughlines were CONFIRMED against the
> tree, but four things here are wrong or missing and the corrections are marked inline below as
> `[CORRECTED — see 01_consolidation.md §1.x]`. **The headline number of TL-1 is one of them.**
> Read `01_consolidation.md` for those four, for findings F12–F19, and for the consolidated
> outstanding-item register. Nothing here is deleted — a corrected claim is left visible with its
> correction, per this repo's standing convention.

**Scope.** The fifteen commits merged to `main` in the review window, plus a full instrument sweep
over the tree at `f2fc307`: the v3 vector audit (L1), the structure audit (G_code + L2), and every
`tools/` check that concerns code shape, contracts, wiring, provenance and currency.

**Method, stated so the confidence is readable.** Unlike the 2026-08-14 five-lens assessment, this
pass **executed everything it reports**. Both blocking test suites were run to completion, every
validator was run from the working tree, and both audits were run fresh into
`audit/2026-08-17-weekly-review/`. Where a finding restates one the five-lens assessment made on
2026-08-14, it was **re-verified at HEAD** rather than carried forward — three of them have not
moved, and that is itself the finding. Nothing below is inferred from source-reading alone.

⚠ **What this pass did NOT do:** it did not run `mc_v18` campaigns (no CI job does), did not exercise
the Godot skeleton (non-compilable, §6), and did not assess design content except where an
instrument's output pointed at it. `PP-NNN` provenance was not hand-verified — §0's standing caveat
that 433 of 452 cited PP numbers resolve to no register on `main` is unchanged and untouched here.

---

## 0. The one-paragraph version

**The week's shipping quality is high and the week's debt direction is wrong.** Both suites are
green, every blocking gate passes, and the single highest-leverage act available to this repo — a
batched ruling session — actually happened and closed a ten-item agenda in one sitting. But the two
debt signals the scope ratchet exists to watch **regressed by 122 and 62** across the same week, four
registers never received the ruling that was the week's centrepiece, and the pattern-level repair
that §0.1 point 5 demands was applied to the two instances the last assessment named and not to the
class. The apparatus is now finding defects faster than the tree is burning them down, and it is
finding them well: five of the ten findings below were surfaced by an instrument, not by reading.

---

## 1. Verification results (all executed at `f2fc307`)

| Gate | Result |
|---|---|
| `pytest tests/valoria` | **1933 passed**, 23 skipped, 15 xfailed, 0 failed (478s) |
| `pytest engine/tests` | **2051 passed**, 5 xfailed, 0 failed (185s) |
| `tools/valoria_local.py --all` | blocking gates pass; 1 report-only fail (`scope_ratchet`) |
| `tools/review_core.py --summary` | **AMBER** · 0 blocking · 0 regressions · 2 report-only · 0 errors (11 signals) |
| `freshness_gate` | 109/109 FRESH, 0 stale, 0 no-SHA |
| `broken_dependency_checker` | no broken links |
| `wiring_map_check` | 27/27 modules · 8/8 adapters · all tags resolve |
| `ci_gate_coverage` | HEAD up to date with `origin/main`; local green matches merge result |
| `ci_claude_workflow_paths` | 169 referenced · 168 live · 1 aliased · **0 dead** |
| `ci_claim_provenance_check` | every quantitative ledger entry names an instrument that exists |
| `ci_pp_frozen_check` | archive pointers name the fork; no PP above the PP-726 ceiling |
| `export_engine_params` / `export_key_types` / `export_sim_params` | round-trips OK (55 key types) |
| `compliance_check --check-only` | 61 warnings, **0 errors** |
| Vector audit v3 (L1) | **VALIDATED (2/3)** — P2 pass (CV 0.382), P3 pass (mean cite-degree 51.6), P1 fail |
| Structure audit | 273 code modules · 419 import edges · 3 cycles · 20 cut-vertices · 27 L2 modules · 103 wiring edges · **0 phantom producers** · 1 real dangling emit · 9 `doc: null` |
| Contract↔code join (OI-54) | **13 joined · 13 declared-none · 0 unresolvable** · 1 undeclared (see F3) |

Everything that gates a merge is green. Everything below is under the gates.

---

## 2. Throughlines

Ranked by how much independent evidence converged on them, per §10's rediscovery rule.

### TL-1 — Instrumentation outpaced remediation again, and now there is a week of evidence for it

The five-lens assessment called this T3 from a snapshot on 2026-08-14. A week of commits makes it
measurable. The window added **+82,021 / −15,588 lines across 283 files**, and the great majority of
that is apparatus: contract and key indexes (#298), flow skeletons and the engine atlas (#299), the

> ⚠ **[CORRECTED — see `01_consolidation.md` §1.1]. "The great majority is apparatus" is FALSE, and
> it was the one load-bearing number here with no instrument behind it** — a critic named it as the
> claim to bet against, correctly, on §0.1-point-4 grounds. Measured over the same range: **53.8% of
> the churn is machine-generated artifacts**, 14.1% is `systems/` + `engine/`, 12.2% is `audit/`
> prose, and hand-authored apparatus (`tools/` + `skills/` + `tests/`) is **11.9%** — less than
> design got. `references/glossary/glossary.json` alone is **44.5% of the entire week's diff**,
> rewritten in 8 of 15 commits. The corrected finding is sharper: **the diffstat is nearly
> meaningless as a measure of work here, because half of it is one generated file being rewritten.**
> TL-1's actual thesis — the ratchet regressed while the window shipped — survives, and is
> corroborated by two earlier non-self measurements (173/60 on 2026-08-11; +115/+56 in a prior
> handoff entry).
world-schema and Python-architecture censuses (#300/#304), the consolidation sweeps (#303/#305/#306),
five new guard tests and `single_owner_check` (#307/#310), the CURRENT.md stamp-structure guard
(#313). Over exactly the same window:

```
ed.stale                198   ceiling  76   REGRESSED +122
ed.needs_jordan_stale    83   ceiling  21   REGRESSED  +62
```

246 open ED entries; 114 need Jordan. `scope_ratchet` is the one report-only signal that fails, and
it fails in the direction that matters. The instruments are good — five of this document's ten
findings came out of one of them — but **the burn-down owner L5 asked for still does not exist**, and
a ratchet with no owner is a monument.

### TL-2 — The adversarial pass is now this repo's most productive defect finder, and it keeps finding the same defect

Every substantive commit this week carries refuted-own-claims in its message, and they are load-bearing
rather than decorative: #306 refuted three of its own claims before commit; #307 found seven defects
in its own first two commits; #311's two read-only critics found a **ninth and tenth** degree ladder
the census had never enrolled, a second blocking suite the author had never run (six failures, all
his), a recurrence guard that would have caught only 4 of the 11 ladders it claimed to guard, and two
vacuous assertions; #315 retracted two of its own numbers.

> ⚠ **[CORRECTED — see `01_consolidation.md` §1.3]. The "ninth ladder" story is misattributed, and I
> passed the tree's own wrong lesson along.** Both "newly found" ladders were already on `main`, as
> rows **#2 and #4 of 8** in `audit/2026-08-11-systems-python-architecture-audit/00_findings.md:184-194`,
> merged three days earlier. The filed lesson ("an audit instrument's ROSTER is a claim about the
> tree") points at instrument blindness; the actual defect was that a later instrument in the same
> window never read the earlier one's committed output. Both are worth keeping — the filed one is
> currently the only one, and it is the wrong half.

The recurring shape underneath them is one thing, and it now has a name in the tree:

> **CHECK THE GATE THAT GATES THE THING.** (`ED-IN-0187`, `HANDOFF_IN.md`)

It appeared twice in a single commit — `pytest tests/valoria` green while `engine/tests` had six
failures, and then `test_mass_battle_byte_exact.py` green while the actual gate
(`ci_golden_modes_check.py`, a separate blocking job that does not run locally) was red. Both times
**a green from a neighbouring instrument was read as a refutation.** This is the same failure §0.1
point 2 describes at assertion scale, one level up: an instrument must be able to observe the failure
it is being cited to exclude.

### TL-3 — Ruling throughput is the binding constraint, proven in both directions in one week

The five-lens assessment's T5 said the cheapest available intervention was a batched ruling session
rather than another audit wave. On 2026-08-14 that session happened, and it worked: ten calls ruled
in one sitting, the degree ladder unified under a single owner, the strategic d6/4+ dice system
deleted, `CONQUEST_MIN_MIL` deleted. That is the highest-leverage act of the week by a wide margin.

And then the constraint reasserted itself immediately. Of the ten rulings, **four executed, one
part-built, five not started.** The two sites HELD in `test_degree_ladder_single_owner.py::HELD` were
**ruled the very next day** (2026-08-15 — Jordan: *"systems should not need different degree bands"*)
and are still unexecuted at HEAD; both remain asserted to STILL DIVERGE, which is correct today and
becomes a stale exemption the moment either lands. The ruling's own propagation is owed (F5). The
queue is not merely long — **rulings are being produced faster than they are propagated into the
registers that carry them**, which is the mechanism by which settled rulings get re-raised (T5's
second half).

### TL-4 — The named authority surfaces were repaired; the pattern was not

#313 did the thing the last assessment asked for on the two worst instances: CURRENT.md went
81,415 → 16,755 bytes with its spliced stamp chain deleted, HANDOFF.md's "Next actions" was rewritten
off a July blocker resolved on 07-30, and — the part that counts — a **structural** validator
(`check_current_stamp_structure`) now fails on a repeated stamp body or a chronology that climbs.
That closes T1 and L2 for CURRENT.md properly: a metadata check was replaced by a structural one.

One level down, the same class is untouched. Five workplan pointers declare `liveness: LIVE` and name
targets that do not exist (F2). The SessionStart banner prints a tool path that does not exist (F1).
CLAUDE.md §8 still lists a gate in the blocking tier that the registry records as never-failing (F7).
`glossary.md:45` still bans and mandates `CI` in one sentence (F6c). §0.1 point 5's rule is explicit
that the unit of repair is the pattern; this week it was applied to the two instances that were named.

### TL-5 — Design work re-based itself on measurement, and produced the first design-level finding

#304 measured nine degree implementations rather than arguing about them. #315 went further and is
worth singling out: **every number in it was produced by running the engine at HEAD**, not transcribed
from the 2026-07-26 balance audit — and the re-measurement showed the audit's *ranking* survived
while its *values* moved (history +19.4pp → +14.9pp). That is §0.1 point 4 applied correctly, in the
unfavourable direction, to the author's own source.

It also produced the week's only finding that is about the game rather than the repository:

> Valoria has a complete, numerate engine for characters and factions getting **worse**, and no
> engine for them getting **better**.

Supported by a run falsifier: threadwork's `_actor_pool` returns 12 for History 0, 3 and 7 alike, so
History has zero marginal value in every Thread operation. The apparatus finally paid out in its
intended currency.

---

## 3. Findings

Numbered F1–F11, each verified by execution this session. Severity is my judgement; none is blocking
today, though F11 is close to becoming so.

### F1 — `review_core.py` fabricates the tool path for any signal that does not live in `tools/`

`tools/review_core.py:136` builds the displayed source as `"tools/" + chk["argv"][0].split("/")[-1]`.
Two of the eleven signals (`stubs.count`, `contracts.join`) are served by
`skills/valoria-vector-audit/scripts/structure_audit.py`, so both are reported as
**`tools/structure_audit.py` — a path that does not exist**:

```
[fail] stubs.count 24/25 (tools/structure_audit.py)
```

That line is what the SessionStart banner shows and what the dashboard's Repository-state card
carries. A reader following the pointer finds nothing. This is precisely CLAUDE.md §4's
define-it-at-the-call-site rule failing at the call site: the banner is where the next session meets
this signal first. Fix is one line (use `argv[0]` verbatim).

### F2 — Half the live workplan pointers name targets that do not exist

`ci_workplan_pointer_check` reports **5 violations of 10 pointers**, all self-declared `liveness: LIVE`:

| Pointer | Missing target |
|---|---|
| `POINTER_2026-07-17_character_decision_L1_L2.md` | `audit/2026-07-17-character-decision-adversarial-audit/01_remediation_L1_L2.md` |
| `POINTER_2026-07-17_character_decision_program.md` | `…/03_remediation_program.md` |
| `POINTER_2026-07-29_centralization_single_owner.md` | `audit/2026-07-29-centralization-single-owner/01_orchestration_plan_v1.md` |
| `POINTER_2026-07-29_code_shape_execution_ledger.md` | `audit/2026-07-29-code-shape-open-items/04_execution_ledger.md` |
| `POINTER_2026-07-29_code_shape_open_items.md` | `audit/2026-07-29-code-shape-open-items/01_orchestration_plan_v1.md` |

All three directories were removed in the 2026-08-05 evacuation. **Two of them are the plans of record
for the single-owner and code-shape programs that this week's work executes against** — `OI-54`,
`stubs.count` and `contracts.join` all cite `01_orchestration_plan_v1.md` in live comments. The gate
is report-only, so CI is green.

⚠ **Compounding:** the tool prints `[workplan-pointers] 10 pointer file(s), 10 target(s) resolved.`
*above* the five violations. `checked` counts attempts, not successes
(`ci_workplan_pointer_check.py:133`), so the summary line a skimming reader sees asserts the opposite
of the detail below it. Two fixes, and the summary line is the more important one.

### F3 — Two governing surfaces disagree about whether `mass_battle`'s undeclared `sim_module` is a regression

`structure_audit.py:790` writes, unconditionally, into every generated register:

> `undeclared` should always read 0 now that all 27 modules carry the field (a nonzero value here is
> itself a regression, not a pre-existing gap).

It reads **1**. And `references/module_contracts.yaml:566` withholds that field deliberately, with a
documented reason:

> `sim_module: DELIBERATELY NOT ADDED HERE (OI-54, ED-IN-0097, W4)` — MB owns these rows per the
> plan's shared-file single-writer table; the join lane does not touch MB's rows even to add a field.

Both are defensible; they cannot both be read. A cold session reading the register concludes a
regression shipped; a cold session reading the contract concludes the register is wrong. The lane-hold
is the true state, so the generated prose should be conditional on the disclosed-hold list rather than
asserting a clean tree it does not have. (The lead is already recorded: `mechanics_index.yaml` carries
`mass_battle -> systems/mass_battle/sim/massbattle.py`.)

### F4 — One malformed contract field is generating findings in two independent instruments

`references/module_contracts.yaml:749` and `:757` embed prose annotations inside identifier strings:

```yaml
- output: "faction Mandate (cross-module → faction_state)"
- output: "faction Treasury income (cross-module → faction_state)"
```

Those exact two strings are:

- 2 of the 21 `ci_quantity_vocabulary_check` **UNRESOLVED** stat identifiers,
- 2 of the 4 vector-audit **Mode-H multi-graph isolates** (cite 0, tl 0, mu 0, pp 0 — structurally
  disconnected in all four graphs), and
- 2 of the 10 vector-audit **Mode-E sparse-context tokens** (0 paragraphs, cite-degree 0).

Three findings, two instruments that share no code, one root cause: the annotation belongs in a
comment or a `note:` field, not inside the identifier. This is the cheapest repair named in this
document and it retires six rows of instrument output. The remaining Mode-H isolates —
`Active Inquisition` and `Counter-Intelligence` — are genuinely canonical tokens with zero structural
connection anywhere, and are a real gap rather than a formatting artefact.

### F5 — The week's centrepiece ruling has not propagated to any of the four registers that owe it

`HANDOFF_IN.md` names the propagation owed by ED-IN-0187 and says explicitly that **no new tool is
needed** — `ci_supersession_check` already reads `files_to_recheck`; what is missing is the data.
Measured at HEAD, `ED-IN-0187` appears **zero times** in all four:

- `registers/supersession_register.yaml` (owes the PP-232 floor, the Ob-20 exception, the 2×Ob bar)
- `CURRENT.md`'s Dice / resolution row
- `references/propagation_map.md`
- `registers/mechanics_index.yaml`

The consequence is visible in this session's own run: `ci_supersession_check` reported clean against
25 entries, **none of which know the degree ladder moved**. A green from a register that was never
told is TL-2's failure shape, expressed as data rather than as a test run.

### F6 — Three defects the five-lens assessment named on 2026-08-14 are unchanged at HEAD

Re-verified individually, not carried forward:

**(a) `TN_STANDARD` still has no owner, and the plan still prescribes a symbol that does not exist.**
Live module-scope definitions at `engine/autoload/sigma_leverage.py:87` and
`systems/threadwork/sim/operations.py:47`, plus the deliberately-frozen
`tests/sim/v32-combat-balance/m1_dice_sigma_core.py:31`. `dice_engine.py` contains none — and
`dice_engine.roll_pool` hardcodes `tn: int = 7` as a **fourth** de-facto definition of the same
number. `audit/2026-08-11-divergence-audit/02_remediation_plan.md:582` prescribes
`dice_engine.TN_STANDARD`, which still does not exist. The plan cites its own uncreated target.

**(b) `tools/single_owner_check.py` is still absent from `references/ci_checks_registry.yaml`** while
`valoria_local.py:242` invokes it. CLAUDE.md §4 names that registry as one of the two places a process
term must be defined ("every tool has a `role:` line … it is machine-read, so it cannot silently rot")
— so that claim remains false, for the checker whose entire subject is single ownership.

**(c) `references/glossary.md:45` still bans and mandates `CI` in one sentence:** "**`CI` is no longer
used** … Use `CI` for the Church clock". Inside the file self-declared canonical for term expansions.

### F7 — CLAUDE.md §8 places a never-failing gate in the authoritative tier

`CLAUDE.md:401` lists supersession among CI's blocking gates. `references/ci_checks_registry.yaml:245`
records `ci_job: validators-report` with the note that *"every return in `main()` is 0 and `:66` says
so explicitly, so it could never gate"* — moved 2026-08-12 by G3, ED-IN-0159 §1.9. The registry is the
machine-read owner and it is right; the governing document is three days stale on its own §8, which is
the section that tells the next session which gates are unbypassable.

### F8 — Both declared degree-ladder HOLDs were ruled on 2026-08-15 and are unexecuted

`tests/valoria/test_degree_ladder_single_owner.py::HELD` carries both rulings verbatim
(`combat_engine_v1/core.py` MIGRATES once the defender-derived Ob lands; `sigma_leverage.degree`
MIGRATES with pool-awareness re-expressed as an injected extension). The guard is behaving exactly as
designed — both are asserted to STILL DIVERGE, so resolving either fails the file and forces the
update. Two notes for whoever picks it up:

- The **sequence is fixed and is the opposite of the obvious one**: derive Ob from the defender
  (score/2 + modifiers) *first*, then apply the owner's ladder. Migrating the bands against the fixed
  Ob is wasted work, and the file says so.
- **The score/2 derivation is wired nowhere**, and `roll_net_continuous` still does
  `int(round(pool))` — so the fractional-dice half of the ruling is not implemented either. Both
  halves gate both holds.

Recorded but unpropagated design consequence: **181/600 cells moved Partial → Failure (30.2%)**,
scaling with Ob, and three consumer tables pay differently for those bands. Instrument:
`audit/2026-08-14-degree-reband-consumer-cost/reband_delta.py`.

### F9 — Six of seven refresh families are stale, one severely

```
vector-audit        STALE  drift=1372  last refresh 9845f4f (2026-07-28)
decisions-digest    STALE  drift= 102  last refresh ed7d0fd (2026-08-11)
proposals-register  STALE  drift=  55  last refresh ed7d0fd (2026-08-11)
graph-lexicon       STALE  drift=  51  last refresh 55a1703 (2026-08-08)
mechanics-index     STALE  drift=  44  last refresh 85bf491 (2026-08-13)
apparatus-registry  STALE  drift=   7  last refresh 85bf491 (2026-08-13)
glossary            fresh  drift=   0
```

The tracked `tools/observability/audit_findings.json` has not been refreshed in twenty days across
1,372 in-scope changes, so the Incompleteness Ledger's **Missing** face — the dashboard surface whose
entire doctrine is *surface, never cull* — is reporting a July tree. This run produced a current
findings feed at `audit/2026-08-17-weekly-review/vector_audit/audit_findings.json`; it is deliberately
**not** written over the tracked artifact here, because that regeneration belongs to
`audit-refresh.yml` and its owning tools, not to a review pass.

⚠ Related display nit: `review_core`'s `audit.staleness` signal reads **pass** while the tool it runs
reports six stale families. It is tier `info` and `audit_staleness.py` exits 0 unconditionally
(`:320`), so nothing is being hidden — the SessionStart banner surfaces the staleness lines
separately — but "pass" next to a six-way stale report is the wrong word in the one place a reader
skims.

### F10 — `structure_audit`'s console total does not match the register it writes

Console: `0 phantom-producer, 3 dangling-emit, 9 doc:null`. Register: `dangling-emits=1`. Both are
correct — the console prints all findings, the register prints `real_dangling` (non-notional) only
(`structure_audit.py:690`) — but the console number is the one a session reads first and it disagrees
with the artifact by 3×. Label the console line as including notional modules.

**The one real dangling emit is worth its own note:** `env.crisis` is emitted by `peninsular_strain`
*and* `scenario_authoring` and consumed by nobody. It is independently reported by `m1_acceptance`
("2 unconsumed by name") and by `systems/overview/_identifier_census.yaml:660`. Three instruments, one
gap — not new, and not closed.

### F11 — `editorial_ledger_in.jsonl` has ~1,100 tokens of headroom under a **blocking** cap

> ⛔ **[UPDATED LATER THE SAME DAY — this finding came due during the session that filed it.]**
> Filing `01_consolidation.md`'s ledger entry **hit the cap**: `50,048 / 50,000`, commit refused. The
> entry was cut back twice to fit. **The file now stands at 49,892 with 108 tokens of headroom** —
> less than any entry anyone will write. Q5 is not "not started," it is **overdue**, and the next IN
> session is blocked before it starts. See `01_consolidation.md` §4 Q-D for the ruling actually
> needed, which is not "chunk it" but *which file new entries land in afterwards*.

Found by filing this review's own ED entry, which is the only reason it was found: the IN ledger sat
at **48,217 / 50,000 tokens (96%)** before this commit and **48,892 (98%)** after, and
`ci_register_size_check` is a blocking CI gate. Roughly **one more entry of the size sessions
actually write** exhausts it — the first draft of ED-IN-0194 alone consumed 1,070 of the 1,783
tokens available, and had to be cut back to fit.

This is not a new problem, it is a **not-started ruling coming due**: `ED-IN-0185 Q5 (ledger
chunking)` was ruled on 2026-08-14 and is listed among the five items "NOT STARTED". Three other
registers are also over 85% (`module_contracts.yaml` 87%, `editorial_ledger_in_archive.jsonl` 88%,
`tests/coverage_matrix.md` 94%). The gate is doing its job by warning early; the warning has now been
standing long enough that the next routine session is likely to meet it as a hard failure instead.

⚠ Note the interaction with F4/T4 from the five-lens assessment: the **archive** file is already the
larger of the two (131,302 tokens) and the pre-cutover convention makes `_archive` the primary
allocation surface for 0160–0182. Chunking needs to decide which file new entries land in, not only
how the old ones are split.

---

## 4. Structural state of the code (measured, for the record)

**Import graph:** 273 modules, 419 edges, **3 cycles** (`massbattle ↔ units`; the six-module
`social_contest.sim.contest` package cycle; the five-module `tests.sim.mass_battle` cycle), 20
cut-vertices. The top cut-vertices are the expected spine — `engine.autoload.game_state` (in 10,
out 11), `engine.cross_scale.scene_dispatch`, `engine.mc_v18` — plus `tools.sim_harness.adapters`
(in 1, out 17), which is the prototype cluster CLAUDE.md §3 already flags as 28 of the 36 zero-caller
modules.

**Contract layer:** 27 modules, 103 wiring edges, 2 L2 cycles, cross-scale fraction 0.511. **9 modules
still carry `doc: null`** — `audit`, `domain_actions`, `engine_clock`, `game_director`, `npc_memory`,
`scenario_authoring`, `scene_slate`, `scene_timer`, `settlement_economy`. This is unchanged and is
still the §6 porting blocker: `engine_clock`, the temporal spine, has no home design doc, and
`domain_actions` is simultaneously a Mode-A hub in 3 of 4 graphs (cite 141, pp 12) — **the most-cited
module in the corpus with no document**. `HANDOFF_FA.md`'s open ED-FA-0002 (author the
`domain_actions` home) is the right next M1 juncture and the banner already surfaces it.

**Vector audit topology:** 217 design docs (38.1% of 570 `.md`), 268 tokens, 13,839 cite edges. Four
hubs are top-quintile in **all four** graphs — Mass Battle, Peninsular Strain, Settlement Layer,
Threadwork — which is the change-impact ranking to consult before touching any of them. Mode F
(throughline orphans) is **empty**, which is a genuine improvement worth recording. Mode G still
carries three struck terms in circulation: **Game Master** (68 uses / 18 docs — in a repo whose first
line of CLAUDE.md is "there is no GM"), **Coup Counter** (46 / 19), **Cultural Reformation** (24 / 10).

> ⚠ **[CORRECTED — see `01_consolidation.md` §1.4]. Four categories present in this run's own output
> and not reported here:** **Mode B was omitted entirely and without disclosure** — 28
> implied-but-missing pairs, two of which link the 4/4 hubs named just above (`Mass Battle ↔
> Settlement Layer`, `Faction Layer ↔ Mass Battle`, metadata-linked, zero citations); **two canonical
> Key types at 0 paragraphs / cite-degree 0** (`mechanical.scene_exited`, `mechanical.scene_skipped`)
> while the other four members of that exact class are discussed below; **63 import orphans and 91
> unverified CLI entries** dropped from the scorecard quotation; and `_kernel_tests` as a top import
> hub (in 0, out 16) — a test module inside the shipped package.

⚠ Mode D tripped its traversal cap on 55,175 calls; its 237 cascade sinks are leads, not findings.
P1 (foundation-periphery) FAILED — foundation cite-mean 59.75 against a corpus median of 75.5, i.e.
the docs designated foundational are *less* central than the median document. The audit publishes at
2/3 as designed, but P1 has now failed on consecutive runs and deserves a look on its own.

---

## 5. What I would do next, in order

1. **F5 — propagate ED-IN-0187 into the four registers.** No new tool, no ruling, ~30 minutes, and it
   is the difference between a ruling that stuck and one that will be re-raised.
2. **F2 — resolve the five dead workplan pointers.** Each is `LIVE`, two are the plans of record for
   in-flight work, and the fix is a `FORK:` annotation (the convention already exists) rather than a
   deletion. Fix the summary line in the same commit.
3. **F4 — split the two annotated identifiers in `module_contracts.yaml`.** One-line data fix; retires
   six instrument rows across two independent tools.
4. **F1, F10, F3, F7, F6b/c — the pointer-and-label class.** All small, all in the "a claim about a
   surface that the surface contradicts" family, and worth doing as **one** commit so the pattern is
   repaired rather than five instances.
5. **F11 — execute ED-IN-0185 Q5 (ledger chunking) before the cap is hit, not after.** ~1,100 tokens
   of headroom on a blocking gate is roughly one entry. This is the only finding here with a deadline
   set by someone other than us.
6. **Assign the ratchet a burn-down owner (L5, still open).** `ed.stale` at 198 against a ceiling of
   76 is the number that decides whether the next month's audits are worth running.
7. **F8 — sequence the Ob derivation.** It gates both holds and the fractional-dice half of the
   ruling; nothing else in the degree work can proceed around it.

---

## 6. What this pass could not establish

- **PP provenance.** *[CORRECTED — see `01_consolidation.md` §1.2: **531 of 537** is the current
  measurement (ED-IN-0190, 2026-08-14, 537 distinct PP ids across 318 live files, 6 resolving). The
  433/452 figure below was copied from `CLAUDE.md:34`, which is stale; two uncontrolled numbers for
  one quantity now circulate, which is §0.1 point 4 in the governing document itself.]*
  433 of 452 cited `PP-NNN` numbers resolve to no register on `main`, and
  `validate_ed_citations.py` is ED-scoped by design (ED-IN-0190, frozen as historical). Every PP
  citation encountered here was taken on trust.
- **Balance behaviour.** No CI job runs full `mc_v18` campaigns; §7's gap is unchanged. The seeded
  regression suite (`engine/tests`, 2051 green) covers determinism and parity, not balance.
- **Whether the three import cycles matter.** They were measured, not diagnosed. `massbattle ↔ units`
  is in the tree Jordan ruled non-canon (J2), so it may be moot rather than fixable.
- **`godot/`.** Untouched by every instrument run here, as it was by four of the five lenses on
  2026-08-14. The GO lane activated on 2026-08-14 (ED-GO-0001) and has one handoff entry; nothing in
  this window exercised it.
