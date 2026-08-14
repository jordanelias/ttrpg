# Post-assessment remediation — the plan of record

## Status: RULED 2026-08-14 — §2's seven questions are ANSWERED; the tracks are part-executed

> ⚠ **§2 is a CLOSED agenda. Do not re-raise it.** Jordan answered all seven questions on
> 2026-08-14; the answers are recorded verbatim in `ED-IN-0185` and summarised in
> `registers/handoffs/HANDOFF_IN.md`. Q2 and Q3's band/dice halves are executed (ED-IN-0187),
> Q4's vocabulary is built (ED-IN-0188); Q1a, Q1b, Q4's sweep, Q5, Q6, Q7 are **ruled and
> awaiting execution**, and Q2's `score/2` obstacle derivation plus Q3's fractional *dice* are
> the two largest unexecuted pieces. This banner exists because this document's own finding
> T5 is that settled rulings get re-raised when the answer is not written where the question
> lives.

## Date: 2026-08-14 · Lane: IN (cross-cutting) · ED-IN-0185 · Companion to `00_findings.md`

**Read `00_findings.md` first.** Every step below cites a finding there; the evidence is not repeated.

**Method.** Decomposition by a read-only Fable-5 planner (CLAUDE.md §10 assigns planning to the top
tier), written up by Opus. The planner re-verified every load-bearing citation against disk and
**corrected one of my own**: the `Faction` port-blocking declaration is at
`engine/autoload/game_state.py:6-11`, not under `systems/factions/sim/` as the assessment's brief
said. Claims it could not check are marked **inferred** and each carries an executor-side
precondition, so the inference is tested before it is acted on.

---

## 0. Three rules, one of them new

The first two are inherited from `audit/2026-08-11-code-leanness/01_plan.md`:

- **Centralize to one definition.** Where copies agree, mechanically (delta = none). Where they
  disagree, rule the semantics first, then centralize with the variants as explicit named adapters.
- **Every change to a blocking gate ships its own expected-delta test**, with a pre-change control.

The third is new, and it exists because of finding **T3** — the repo's measured failure mode is
adding instruments instead of reducing debt:

> **A step may add a guard ONLY in the same commit as a burn-down of the thing it guards, and every
> ratchet it touches must leave with a *lower* pinned maximum than it entered with.**

Steps marked **[BURN]** reduce a ratcheted count. **If the [BURN] steps are skipped and the guard
steps land, this plan has failed by its own standard** — that is the falsifier for the plan as a
whole, not just for its parts.

**Column key:** `pre` precondition · `fals` the command or test the executor runs · `eff` S (<2h) /
M (half-day) / L (multi-session) · tier per §10.

---

## 1. Tracks

**Parallelism.** A and E both touch `CURRENT.md` and must serialize within IN. B touches
`engine/`+`systems/`, C touches `tools/`+`tests/valoria/`, D touches `tests/` — those three run
concurrently with A. The ruling agenda (§2) is one Jordan session, not a track.

### Track A — authority-surface repair. Highest leverage after the ruling session.

| # | step | pre · fals · eff · tier | mechanism at risk |
|---|---|---|---|
| **A1** | **[BURN]** Rewrite `HANDOFF.md:47-60` "Next actions" — drop the ✅-RESOLVED 2026-07-30 ID-freeze block (history to `HANDOFF_IN.md`), replace with actual open cross-cutting items. | none · banner shows nothing resolved before 2026-08-01; `grep "RESOLVED 2026-07-30" HANDOFF.md` → 0 · S · sonnet | The banner reads **only** this section. Over-trimming hides live cross-lane work — keep the lane table. |
| **A2** | **[BURN]** De-duplicate `CURRENT.md:31`: excise the ~8 verbatim-duplicated stamp blocks and repair the chronology at the ED-IN-0151 splice. **Same commit:** the structural check inside the *existing* `currency_consistency_check.py` — the stamp chain must parse as strictly-descending dates with unique ED-sets. | none · a test feeding the check a duplicated block and a date inversion, asserting both fire; line 31's char count roughly halves · M · **opus** | The file §1 says to trust first. A wrong excision silently loses a stamp that is some ruling's only registration — **J1/J2 register in this line.** Mitigation: byte-compare each excised block against its twin; anything non-identical is not a duplicate and stays. |
| **A3** | **[BURN]** The same dedupe removes the twice-verbatim J2 narration — the direct fix for **T5's pollution half**. Verify `CURRENT.md` states the mass-battle canon question as **settled** exactly once, pointing at `systems/mass_battle/sim/__init__.py:1-11`, with only the adapter open. | A2 · each concept appears once, marked settled · S (folds into A2) · opus | Re-raising a settled ruling costs Jordan's attention. **Transcription only — do not re-open J2's content.** |
| **A4** | Fix `references/glossary.md:45` — currently bans and mandates `CI` in one sentence. Rewrite to what ED-782 + ED-IN-0075 establish: `CI` = Church Influence clock only; `PT` (territory) and `Truth` (personal) written in full. | none · the sentence no longer both bans and mandates the token · S · sonnet | Self-declared canonical for expansions — a wrong rewrite propagates into 19 generated views. |
| **A5** | **[BURN]** Two factual row contradictions: (a) `:154` cites `engine/params/core.md` as live SoT while `:168` marks it EVACUATED — annotate per the SC-row precedent, do not silently repoint. (b) `:156` claims "Retires ED-921" while the ledger holds it open **and** the row's own baseline is pending that reconciliation. | A2 merged · `grep "Retires ED-921" CURRENT.md` → 0; ED-921 stays open · S · sonnet | ⚠ **inferred** — the ED-921 ledger line was not opened this pass. Executor greps all ledger files for a closing entry **before** editing. |
| **A6** | **Both branches of Jordan's CURRENT.md reduction, pre-built so the ruling executes same-day.** See §2 Q1 for the options and costs. **This step prepares only.** | A2 · per branch · S–M · **opus** for the cutover | The riskiest edit in the plan. Whichever branch: the cutover commit **must show the head-row table byte-identical** before/after. The reduction is of *narrative*, never of rows. |

### Track B — owner-in-code enforcement. The T2 burn-down.

| # | step | pre · fals · eff · tier | mechanism at risk |
|---|---|---|---|
| **B1** | **[BURN]** Create `TN_STANDARD = 7` in its owner `engine/autoload/dice_engine.py`; repoint `sigma_leverage.py:79` and `threadwork/sim/operations.py:46` (threadwork re-exports so its consumers stay byte-identical — the `obs_core` precedent). **Annotate, do not touch,** the frozen `tests/sim/v32-combat-balance/` copy. Also makes the remediation plan's dangling `dice_engine.TN_STANDARD` prescription true. | none · delta=none test on all three values; `grep "TN_STANDARD\s*="` outside owner+frozen → 0 · S · sonnet | ⚠ **inferred** that `dice_engine` imports nothing from `sigma_leverage` — circular-import risk between two autoload modules is the first thing to check. |
| **B2** | **[BURN]** Bare-RNG sweep, smallest slice: haiku enumerates live `roll_pool(`/`roll_net*(` calls under `engine/`+`systems/*/sim/` lacking `rng=`; sonnet threads them; **same commit** ships the sweep guard (template: `test_morale_write_sweep.py`). `roll_pool`'s signature does **not** change. | B1 · the sweep test plus `assert checked >= N` so an empty enumeration fails loud · M · haiku→sonnet | The seeded `sim-regression` job already depends on threaded rngs. **Do not extend into `tests/sim/mass_battle/`** — that convention is Q3's territory. |
| **B3** | Register `single_owner_check.py` in `ci_checks_registry.yaml` with a `role:` line. Closes "§4 false as written". | none · registry grep → 1 row with `role:` · S · **haiku** | None — additive. |
| **B4** | **[BURN]** Merge the **8 ruling-free degree sites** onto `dice_engine.degree_from_net`. Per-site delta=none. **Excluded:** `faction_action.py:97-104` (Q2) and frozen copies. | B1 · per-site delta tests; bypass count falls · M · sonnet, **escalate to opus** on any site whose bands are not literally identical — that site moves to Q2's list instead of merging | The **Ob-20 exception and the PP-232 Overwhelming floor** are the traps: a site omitting them is not equivalent even when common-case bands match. Equivalence argued per-branch, never by eyeball. ⚠ **inferred**: the 11-site list. |
| **B5** | After Q2: implement `faction_action._degree` as an explicit named adapter over the owner, citing the ruling. | Q2 ruled; B4 landed · seeded season before/after with a **published** delta · S–M · sonnet | The `net == 0` flip changes strategic outcomes. Publish it as a delta; do not slip it into a refactor (§0.1 point 4). |

### Track C — gate perimeter.

| # | step | pre · fals · eff · tier | mechanism at risk |
|---|---|---|---|
| **C1** | Annotate `patch_register_active.yaml:9-15` — the six `deprecated/archives/patches/*` pointers are verified non-existent. Add `FORK: c451bcb` per pointer. **Annotate rather than delete: it is the only remaining PP provenance trail.** | none · every pointer carries a ref · S · haiku | None — comments only. Do not touch the 6 active entries. |
| **C2** | Extend `validate_ed_citations` scope to `audit/` (**2,612 citations across 198 files currently unscanned**) **with the pre-change control its own docstring demands** — widened scan offline first, triage, then scope + triage + expected-delta test in one commit. Also delete dead `'designs/'` from `SCAN_PREFIXES:120`. | none · expected-delta test; a planted `ED-XX-9999` in a scratch audit file fails the gate · M · sonnet | **BLOCKING gate.** Real fabrications found in triage are findings to file, not reds to suppress — but they must be dispositioned before the scope lands, or CI reds on a pre-existing condition (the ED-IN-0112 lesson). |
| **C3** | Widen `broken_dependency_checker.extract_file_refs` to `engine/` **first only** — report-only delta, triage, then blocking; `registers/` in a second pass. `params/` and `audit/` deferred. | none (parallel with C2) · expected-delta test; a planted `engine/nonexistent.py` ref fails · M · sonnet | Longest-dir-prefix alias resolution must keep winning **before** the not-found verdict, or every historical `sim/`→`engine/` alias reds. |
| **C4** | PP validation — execute whichever arm **Q4** picks. Until then, nothing beyond C1. | Q4 ruled · per arm | **Deliberately no interim half-measure**: validating PP against a 19/452-coverage universe manufactures 433 reds against a HELD disposition. |

### Track D — `tests/` governance. Smallest slices only.

| # | step | pre · fals · eff · tier | mechanism at risk |
|---|---|---|---|
| **D1** | **[BURN]** Execute the leanness plan's own not-started **T5** (this plan does not fork it): one `conftest.py` path helper for `tests/valoria/` + `engine/tests/` — the ~39-block slice, **not** the 131-file corpus. **Same commit:** a sweep test failing on a new `sys.path.insert` in the governed trees, pinned at the post-burn count — *a ratchet born falling.* | none · `sys.path.insert` in governed trees → 0; both suites green; sweep red on a planted insert · M · sonnet | Some bootstraps mutate `sys.path` for **data** paths, not imports — those are not conftest-removable and must be found in the haiku enumeration, not discovered by a red suite. |
| **D2** | **[BURN]** After D1 proves the pattern: fold `_load*` helpers and hand-rolled `importlib` loads **within governed trees only**. Counts outside are recorded, not chased. | D1 green on main for a few days · `_load*` in governed trees → 0 · M · sonnet | Duck-typed doubles loaded by path are grep's blind spot — **assert on collected test count**, not just green. |
| **D3** | Relocate `_kernel_tests.py` (1,650 lines) out of the shipped contest package. | **hard pre:** grep proves zero runtime importers inside the package · suite green; package import graph unchanged · S · sonnet | If the kernel imports it for fixtures, the move breaks the shipped package. ⚠ **inferred** — hence the hard precondition. |

### Track E — boards, godot, vocabulary, design-doc corrections.

| # | step | pre · fals · eff · tier | mechanism at risk |
|---|---|---|---|
| **E1** | **[BURN]** Refresh `workplan_v6_progress.yaml` from lane handoffs + ledgers; bump `as_of` from `470aa09, 2026-07-16`; **repoint its anti-rot watch roster (`:8-12`) off the two retired trees** onto `systems/`, `engine/`, `workplans/`. | none · `workplan_status --check` clean; no retired path in the roster · M · sonnet | This surface class killed `roadmap_state.yaml` by rotting exactly this way. **The roster fix is what stops this being a one-shot refresh that rots again.** |
| **E2** | Replace the unfilled template at `godot_architecture_specification.md:723` with a true status **inside** the 80-line parse window. Lane activation is Q6. | none · the Status owner parses it · S · sonnet | Do not invent a status stronger than DRAFT — §5–§7 is held and this must not pre-empt it. |
| **E3** | **[BURN]** PC lane: correct `combat_reference_v1.md:218,347` — `WI = End+6` was superseded 2026-06-18 by `End + 4 + 0.4×Spirit`, MW cap 3. **This is a transcription defect, not an open design call**: the doc is explicitly subordinate to the engine and the supersession is already ruled. | **hard pre:** executor confirms the engine constant in `combat_engine_v1/config.py` · `grep "End+6"` → 0 live occurrences · S · sonnet | ⚠ If the engine implements End+6 the step inverts — hence the hard precondition. Flag in the PR body per §2's loud-exception rule. |
| **E4** | Piety-Track collision, smallest slice: **banner the two definition sites only**. The 419-ref sweep stays STAGED and gets sliced by subsystem later. | none (ED-IN-0075 exists) · both files carry the disambiguation banner · S now / **L** total · sonnet | **A partial rename is worse than a bannered non-rename.** Never sweep `deprecated/` or `audit/`. |
| **E5** | Define process vocabulary at its invocation sites (§4's both-places rule; **no renames — retrofit posture stands**): `armature` (≥4 live referents) and `disposition` (process sense vs the registered mechanic) get disambiguating glossary entries; **§4's headline `idempotent` is reworded to plain English** — it fails its own test. | none · entries exist and reach the generated views · S · sonnet (headline: **opus**, one paragraph) | Smallest possible CLAUDE.md diff; do not touch the worked example. ⚠ **inferred**: the `armature` referent list. |
| **E6** | Ledger cap/rotation — execute whichever arm **Q5** picks, and **update CLAUDE.md §3 in the same commit** (it describes the pre-overflow state). | Q5 ruled · per arm; `validate_ed_citations:162-168` must still derive the archive into the universe · S–M · sonnet | The archive derivation is what kept the misnamed surface gate-coherent. Any renaming arm moves that derivation in the same commit. |

### Sequencing — what unblocks the most

1. **The §2 ruling session.** It gates A6, B5, C4, E6 and dissolves the four largest duplications.
2. **In parallel, immediately, nothing gated:** A1, A2 (+A3), B1, B3, C1, E1, E2. **A2 retires the
   most-independently-rediscovered defect in the assessment.**
3. Then B2/B4, C2/C3, D1, A4/A5, E3/E4/E5. Then the ruled steps. D2 trails D1 deliberately.

---

## 2. The batched ruling agenda — one session

Finding **T5**: the cheapest intervention available is a batched ruling session, not another audit.
Each question is in plain English with its options and what each costs.

**Q1 — `CURRENT.md` reduction, two parts.**
(a) *The 37 KB history line*: **delete** (git keeps every version; reading history needs `git log`)
or **move to an archive file** (one more frozen file to keep people out of; readable without git)?
(b) *The head-per-subsystem table*: **generated by a script** (a new tool to maintain and gate; but
cannot silently rot) or **hand-written with an automatic shape check** (near-zero cost; catches
corruption like today's, but a wrong-yet-well-formed row still needs a human)?

**Q2 — Faction strategic actions, two small calls.** Only `faction_action.py:97` needs these; the
other 8 sites merge without a ruling.
1. Is "how well did it go" judged **against how hard the action was** (the personal-scale rule:
   beat it by double = overwhelming) or **against fixed numbers** (3+ overwhelming regardless)?
2. Does scraping **exactly zero** count as a **partial success** (current strategic code) or a
   **failure** (the personal-scale rule)?

**Q3 — Strategic dice.** Faction actions roll **d6, success on 4+**; everything else uses the
canonical d10. **Unify on d10** (a bounded rebalancing pass on faction action rates) or **keep d6 as
a declared strategic convention** (two dice systems forever, and the port carries both)?

**Q4 — The PP citation system.** 433 of 452 cited patch numbers point at registers moved off `main`;
the checker validates none. **(a) Restore** the archives from the fork (contradicts the evacuation);
**(b) blanket-mark** all PP as historical-resolves-at-fork and have the checker verify only that
format (small tooling change; PP becomes frozen vocabulary); **(c) drop PP** from the live grammar,
ED-only (cheapest, least reversible).

**Q5 — What happens when a ledger file gets too big?** It hit the cap three times in one session and
new entries now land in a file named `_archive`, which reads as "old". **(a)** numbered continuation
(`_2.jsonl`) with the full file frozen — names stay honest; **(b)** raise the cap for ledgers (they
are append-only records; the cap exists for prose); **(c)** keep the mechanics, rename the overflow
file. Each ~an hour. **The cost of not choosing is every future reader mis-sorting new from old.**

**Q6 — Godot lane: on or dormant?** No GO ED has ever been allocated, no `HANDOFF_GO.md` exists.
**Activate** (one small commit; the lane starts appearing in banners) or **declare dormant** (one
line, so its emptiness stops reading as neglect)? Related and bigger: the held §5–§7 restoration —
a yes/no would close 327 dangling section citations.

**Q7 — schedule, don't answer here.** The **7-vs-9 attribute roster** (open since 2026-07-07) and
the **`Faction` schema** (ED-FA-0004, self-declared port-blocking) are design workshops, not agenda
items. The ask is only: *put them on the calendar.*

---

## 3. Deliberately not planned, and why

- **Another audit, census or measurement wave.** The anti-goal, and T3's point. Every count this
  plan needs already exists. The only new instruments permitted are the guards welded to burn-downs.
- **The full 131-file bootstrap burn, and the frozen `tests/sim/` tree.** D1/D2 govern two trees
  only. Churning frozen references buys nothing and risks the parity oracles.
- **The full 419-ref Piety→Truth sweep.** Banners now; the sweep is real, ruled, and **L** — it gets
  its own sliced lane plan.
- **`module_contracts.yaml` as an enforced interface.** New machinery on unburned debt, and its
  consumer is the port, whose lane and pipeline sections are HELD.
- **RNG unification of the canon mass-battle engine** (~11k lines, no `rng` param anywhere).
  Threading through ~30 modules is **L**, and whether the port wants injection-everywhere is a
  porting-architecture call. B2 guards the *live campaign* surfaces; the canon engine waits.
- **`combat_engine_v1` repackaging.** Left non-package deliberately to preserve internal reaches;
  port-lane work behind Q6.
- **Any process-vocabulary rename.** §4's no-retrofit posture is explicit. E5 defines, never renames.
- **Re-planning what is already fixed**, and **re-opening anything J2 settled.**
- **The leanness plan's remaining steps (G4–G6, G10–G11, Track S, T2–T8).** That plan stands for its
  own scope; this one touches it where the assessment moved a priority (D1 = its T5) and otherwise
  defers rather than forking.

---

## 4. Verification ledger

**Verified on disk:** every `file:line` in a step's text except as marked below.

**Inferred — each carries an executor-side precondition or falsifier so the inference is checked
before it is acted on:** the ED-921 ledger line (A5); lens B's 11-site degree list (B4); the
`armature` referent enumeration (E5); `combat_engine_v1/config.py`'s WI implementation (E3);
`dice_engine`'s import graph (B1); `_kernel_tests.py`'s importer set (D3).

**Nothing in this plan was executed.** All falsifiers are for the executing session.
