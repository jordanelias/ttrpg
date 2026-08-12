# Code leanness — the merged consolidation plan (ED-IN-0159, companion)

## Status: REFERENCE — plan of record; PARTIALLY EXECUTED 2026-08-12 (ED-IN-0160..0165)

> **Execution state, so a resuming session does not re-do landed work.** `G7` DONE · `G8` DONE ·
> `G1` DONE · **`G2` HALF-DONE** — its five dead-scope retirements landed; its
> generator-retirement half is **NOT EXECUTABLE AS WRITTEN and needs Jordan** (the
> `deprecated/tools/` landing site it names was removed by the 2026-08-05 evacuation and is
> pinned as `evacuate` by `tests/valoria/test_evacuation_plan.py:98`, with `:166` forbidding any
> destination under `deprecated/`). **Not started:** G3, G4, G5, G6, G9, G10, G11, G12, G13,
> Track S, Track T (T1 landed early in #303). Nothing in this document is RULED; the execution
> record is `registers/editorial_ledger_in.jsonl` + `registers/handoffs/HANDOFF_IN.md`.

## Date: 2026-08-11 · Lane: IN (cross-cutting) · Companion to `00_code_leanness.md`

**Chunked out of the findings document** (Jordan, 2026-08-11: *"chunk the plan instead of cutting
content from plan"*), so the plan can grow without evidence being trimmed to fit a cap. The
`audit/**/*.md` cap is 30,000 tokens, owned by the single row in
`references/atomization_rules.yaml`.

**This is the plan of record.** It reconciles three sources into one ordered programme:

1. this session's consolidation sweep (ED-IN-0158) and code-leanness census (ED-IN-0159);
2. **PR #304**'s systems-architecture and divergence audits, including its 887-line
   `02_remediation_plan.md`;
3. Jordan's **centralization directive** of 2026-08-11 (findings §8) and its extension to the
   content layer — formulae, mechanics, values, names (§9).

**Read `00_code_leanness.md` first.** Every step below cites a finding there by section; the
evidence, the retractions and the measurements live in that document and are not repeated here.

**Two rules govern every step:**

- **Centralize to one definition.** Where copies agree, mechanically (delta = none). Where they
  disagree, rule the semantics first, then centralize with the variants as **explicit named
  adapters** — disagreement blocks *implicit* merging, never centralization (findings §8.2).
- **Every migration of a blocking gate ships its own expected-delta test** (CLAUDE.md §8, already
  ruled). This is why the programme is ~25 small changes and not one refactor.

---

## 1. The merged plan

**One plan, replacing both.** Three tracks. Steps within a track are ordered; **G** and **S** may run
concurrently in different lanes. Every step names the mechanism at risk, because "without sacrificing
mechanisms" is the binding constraint.

**Governing rule — REVISED by the 2026-08-11 centralization directive (§8).** The target is one
definition everywhere. Where copies **agree**, centralize mechanically (delta = none). Where copies
**disagree**, the disagreement blocks *implicit* merging, not centralization: rule the semantics
first, then centralize with the surviving variants expressed as **explicit** adapters over one owner.
Disagreement is a sequencing constraint, never a permanent exemption. See §8.

**Governing discipline (CLAUDE.md §8, already ruled):** every migration of a blocking gate ships with
its own expected-delta test. This is why the plan is ~20 small changes, not one refactor.

### Track G — gates and tooling (IN lane)

| # | step | depends on | mechanism at risk |
|---|---|---|---|
| **G1** | Excise `compliance_check.py`'s dead branch (`_lazy_import`, `check_all`, the interactive path); update `test_compliance_on_exceed_vocabulary.py:98-99` in the same commit | — | None — the live `--check-only` mode is inline |
| **G2** | **Dead-scope sweep as ONE pattern** (§1.6): retire `ci_co_file_checker` Rule 4, fix the three siblings, delete the `designs/` policy row, retire `atomizer`/`doc_index_gen`/`index_gen` to `deprecated/tools/` | G1 | Rule 4's co-change pressure — #304 argues three code-to-artifact gates now carry it. **The 37 `*_index.md` files are grandfathered (2026-07-26 ruling) — HELD, do not delete with the generator** |
| **G3** | Move the two always-exit-0 gates to `validators-report`; flip their registry `ci_job` rows **in the same commit**; prune the `valoria_hooks.py` ghosts (§1.10) | — | Split the commit and `broken_dependency_checker` reds |
| **G4** | Make `pathres` the owner: migrate the **four** parsers it names (§2.3); add #304's two-tier walk exclusions; fix the TREES roster 17 to 19 | — | `broken_dependency_checker`'s inclusion of `deprecated/` is **correct** — live ledger entries cite the ED archives, the anti-fabrication universe. The two-tier design preserves it deliberately |
| **G5** | **#304's C4 meta-guard** — a vitality check that every blocking validator's scope still matches something | G1, G2, G4 | None. If its first run reds on `review_core.py`, that is a finding |
| **G6** | Size caps, one sequence: adopt the policy cap and delete the stale duplicate block (`atomization_rules.yaml:231-232`), **then** merge the two gates | G2 | **The `.jsonl` caps and the local-tier coverage** (§1.8). The merged gate must carry both or coverage regresses |
| **G7** | The mechanical one-owner migrations — `REPO`, YAML load, `LANES`, `tokens()`, `ID_RE`, ledger read — each with an expected-delta test asserting **delta = none**; gates last | — | Any behaviour change here is a bug, not a delta |
| **G8** | **`STATUS_RE` to one owner.** The only intended behaviour change in Track G. Its test must name all 7 disputed docs **and assert both directions** (§1.3a) | G7 | A one-sided test lets the incompleteness census silently shrink |
| **G9** | Glob the syntax job **and** exclude that job from `invoked_by()` **in one commit**, with a test that a known-dead tool still reports orphaned | — | **Shipping the halves separately zeroes the orphan census** (§2.2; measured: basename-in-workflow goes 46/108 to 108/108) |
| **G10** | Repoint the provenance citations — **all 354 across 12 paths**, not just `params/core.md` — at `engine/engine_params/params_tables.yaml`; add a test that no live `.py` cites an evacuated path | after S1 (avoid double-touching lines #304's B1 rewrites) | None; the capture is byte-faithful |
| **G11** | Fix the 3 broken-anchor probes; wire `validate_ed_citations` locally; drop `systems/combat/sim` from `export_sim_params`'s `SCAN_DIRS` and regenerate (**unblocked**, §3.5); finish the `ci_names_consistency` migration | — | **Do not delete the deprecated resolver** — it is still the campaign default. Only its *export* presence goes |

### Track S — engine/systems correctness (#304's plan, adjudicated; FA/PC/MB/WR lanes)

Run in #304's own order (conventions and units before vocabularies): **A1** (pin the unpinned canon
ladder — precondition for everything), then **B1, B2, B3**, then **B7, B8**, then **B9**, **B10**,
**A2**, **A3, A4**, **A6**, **A8**, **A9**, **B5, B6**, **B11**.

Three adjudications applied:

- **B4 moves out of P0.** #304's sequencing table lists it as behaviour-preserving; its own body says
  "BLOCKED ON B0", and B0 is HELD. It goes behind the ruling.
- **The `altonian_reinforcements` conversion item is STRUCK** (§3.3). It is an accepted cross-session
  handoff with a passing guard; converting it is MB plan §12 I1's call, not this plan's.
- **Two items are added that neither plan had:** bind and guard the 4x faction-roster literal (§3.5),
  and disposition the forked degree ladder in `skills/valoria-dice-model/valoria_dice.py:45`.

### Track T — instruments

| # | step | depends on |
|---|---|---|
| **T1** | Land #304's **C6** fix (atlas probe under `tmp_path`; the no-test-writes-into-`systems/` guard) | — |
| **T2** | Promote the Class-A batteries into `tests/valoria/` as `xfail(strict)` citing an ED, marked slow | **T1 — mandatory.** They were written as free-standing scripts; promoting them into a `-n auto` suite without C6's guard reproduces the exact race C6 documents (6/6 repro on clean main) |
| **T3** | Promote Class B to a standing `tools/mechanism_census.py` — one owner over `flag_ablation` + `harness` + `interaction` + `reachability_sweep` | T2 |
| **T4** | **Run it.** Its output is an explicit input to the HELD rulings below | T3 |
| **T5** | One `conftest.py` path helper for the 32+7 bootstrap blocks; finish the `tests/valoria` same-fact analysis **via `test_register.json`**, not by hand | — |
| **T6** | Teach `dead_primitive_census.py` to exclude `stub_resolve` bodies (#304 8b); pair with G9's `invoked_by` fix — **same defect class, ship as one pattern fix** (§2.2) | G9 |
| **T7** | Pin or retire the forked resolution core (§1.13); coordinate with A3/A9 — same constant family | — |
| **T8** | Resume the `systems`/`engine` uncalled tracing **with string-path grepping** (§2.1) | T4 |

### Held for Jordan

#304's six (**#0** which `net`/`ob` convention is canonical — *blocks #1 and #2*; **#1** the
`faction_action` band shift and its `s == ob` dead zone; **#1b** the strategic layer resolving on
**d6 >= 4** rather than the canonical d10 engine; **#2** one owner for degree bands; **#7**
`standing`'s bounds; **#8** the 10 dead `infrastructure.py` constants), plus **the 37 grandfathered
`*_index.md` files** and **the `sim_harness` promote-or-retire call** (28 files).

**Recommendation: run T4 before ruling #1, #1b, #2 and #8.** The mechanism census prices exactly those
questions — how often the dead `s == ob` band actually fires in seeded campaigns, whether the 10
constants are behaviourally dead.

**On #7 specifically:** the leanness instinct — reuse the existing `contest.primitives.Standing` — is
**correctly refuted** by #304's B11: rebasing silently adds +5 to two dice pools and imports a
venue-local shape across scales. Its dedicated mutator is the mechanism-preserving answer. Keep that
reasoning; it is the clearest worked example of the mission's binding constraint.

### What this is worth

**Not a large file-count reduction.** Track G removes ~3 files; Track T *adds* an owner; the honest
ceiling is the `sim_harness` cluster plus whatever tracing confirms.

**It is a large edit-surface reduction** — the number of files you must touch to change one rule goes
53 to 1, 44 to 1, 8 to 1, 6 to 1, 5 to 1; adding a tenth lane goes from 8 edits to 1.

**And it closes four live defect classes**: seven documents whose status two tools cannot see; 354
constants citing an evacuated authority; dead scope in six blocking gates; and two dead-code censuses
that are both wrong in opposite directions.

---
