# Five-lens repository assessment — structure, vocabulary, modularity, workflow

## Status: REFERENCE — observation with evidence; nothing ruled, nothing executed

## Date: 2026-08-14 · Lane: IN (cross-cutting) · ED-IN-0183

**Commissioned by Jordan**, 2026-08-13: a read-only assessment of *structural rigour*, *vocabulary
and formula standardization*, *modularity and injectability*, and *workflow compliance* — across the
repo and across the recent wave work (`a0810fe`..`bb45b88`).

**Method.** Five `valoria-critic` agents on Fable-5, Read/Grep/Glob only — no write tools, so
independence is structural rather than declared (CLAUDE.md §10). Four ran **concurrently and blind
to each other** on lenses A–D. A fifth received the four reports **as output, not reasoning**, and
was asked for throughlines, lessons and cull candidates. Per §10 the audit tier does not author;
this document is written by Opus from their reports.

⚠ **What none of them could do:** execute anything. No `pytest`, no validator run, no `git show`.
Every "this gate would fire" is read off source. Claims requiring execution are marked inferred and
are **not** load-bearing on any conclusion below.

---

## 0. The one-paragraph version

The repo's distinguishing property is that **it measures its own defects and pins them with
growth-fail ratchets** — an unusual and genuinely good property. Its distinguishing weakness is the
exact complement: **the ratchets freeze debt at its discovery level, and the designated authority
surfaces are the rotten ones.** Every §1 priority-order authority is validated by *metadata* (a
leading date, a path's existence) and none by *structure*, so the files the repo tells you to trust
first are the files least able to report their own corruption.

---

## 1. Throughlines, ranked by independent-lens convergence

### T1 — The designated authorities are the rotten surfaces (4 of 5 lenses)

`CURRENT.md:31` — the §1 priority-one currency index — is a single ~30,000-character line whose
reconcile-stamp chain has **~8 blocks duplicated verbatim** and a **broken chronology** (08-12 → …
→ 07-30 truncated mid-sentence → 08-10 → duplicate run → 07-30 resuming on line 32). The signature
of a mid-chain splice when the ED-IN-0151 stamp was inserted.

**This was found independently by three lenses that never saw each other** (A-F3, D-R1, and the
synthesis pass re-verifying). Independent rediscovery is the confidence signal §10 asks for; this is
the most reliable finding in the set.

The same class, elsewhere:
- `HANDOFF.md:47-49` — the **only** section the SessionStart banner reads — opens with a blocker
  resolved 2026-07-30 and contains nothing newer than July.
- `references/glossary.md:45` bans and mandates `CI` in one sentence, inside the file self-declared
  "canonical reference for all term expansions".
- CLAUDE.md §8 still lists supersession as a blocking gate after it moved to the never-fails tier;
  §9 routes to §5–§7, which do not exist.

**The common mechanism:** `currency_consistency_check` reads leading dates; `MEASURED-BY` requires a
path to *exist*, not to produce its number; `validate_ed_citations.py:545` checks one ID family.
**Metadata validation everywhere, structural validation nowhere.**

### T2 — Owner declared in prose, enforcement absent in tooling (4 of 5)

- **`TN_STANDARD = 7` has three live definitions and none in its owner** —
  `engine/autoload/sigma_leverage.py:79`, `systems/threadwork/sim/operations.py:46`,
  `tests/sim/v32-combat-balance/m1_dice_sigma_core.py:31`. `dice_engine.py` contains none. The
  committed remediation plan (`audit/2026-08-11-divergence-audit/02_remediation_plan.md:582`)
  prescribes `dice_engine.TN_STANDARD` — **a symbol that does not exist**. A plan citing its own
  uncreated target.
- **`dice_engine.roll_pool:68-69`** silently degrades to an unseeded `Random()` with no guard.
- **`tools/single_owner_check.py` is absent from `references/ci_checks_registry.yaml` entirely**
  while invoked at `valoria_local.py:242`. The registry that exists to define what a tool's verb
  means does not know the single-ownership checker exists — so CLAUDE.md §4's "every tool has a
  `role:` line" is false as written, **stated in the same commit that shipped the violation.**

§8's "every rule lives once" and §0.1 point 5's "if you cannot write the guard you have not
understood the pattern" are **both already written down and selectively applied**: morale writes got
their guard; RNG defaults, degree ladders, path bootstraps and stamp structure did not.

### T3 — Instrumentation outpaces remediation; ratchets freeze debt at discovery level (4 of 5)

`valoria_local.py:237-241` states the posture outright: single_owner_check "REDS ON DAY ONE by
design — 14 known bypasses are the finding." A ratchet that may fall and never rise **has no
mechanism that makes it fall.** Measured across the wave: duplicate-reader count unchanged at 14,
`_load` helper copies grew, bootstrap copies grew — inside commits themed on single ownership.

The 7-vs-9 attribute-roster conflict has been open since 2026-07-07 and is still live at
`descriptor_registry.yaml:48-52`, carrying `[ASSUMPTION] … Jordan veto`.

### T4 — The vocabulary failure reproduces inside its own fix (2 of 5 + tree)

One day after ED-IN-0179 settled `evacuate`/`retire`, **a file named `_archive` became the primary
allocation surface**: the "active" `editorial_ledger_in.jsonl` tops out at ED-IN-0159, and every
entry 0160–0182 exists only in `editorial_ledger_in_archive.jsonl:111-134`. CLAUDE.md §4 describes
the old state.

And `wave` — the word this session organised itself around — **fails both of Jordan's tests**: it
resolves to session-local numbering existing nowhere on disk. The proof is that explaining "Wave 3"
to the lenses required sending commit SHAs.

*(Severity softened by the synthesis pass — see Disagreement D4.)*

### T5 — The Jordan queue is the structural bottleneck behind the biggest duplications (5 of 5, named by none)

Every lens's worst duplication is **ruled-but-not-executable or awaiting-ruling**: the mass-battle
migration, the attribute roster, the `Faction` schema (ED-FA-0004), the §5–§7 disposition,
ED-IN-0163's landing-site paradox.

⚠ **And the mass-battle case sharpens T5 rather than illustrating it.** Jordan (2026-08-14): *"I've
ruled on mass battle like eighteen times."* He has — J2 is recorded correctly at
`systems/mass_battle/sim/__init__.py:1-11`. **Five lenses still reported it as an open canon
question**, because CURRENT.md narrates the J2-vs-keep-pin tension twice verbatim and prior audit
prose repeats "dual engines" without stating that the *canon* question is closed. So T5 has a second
half nobody named: **the queue is not only long, it is polluted with settled items that keep being
re-raised** — and re-raising a settled ruling is more expensive than leaving it unruled, because it
consumes the ruler's attention and teaches sessions the ruling did not stick.

**No session can consolidate these.** The fan-out keeps re-measuring them instead. The cheapest
single intervention available to this repo is **a batched ruling session, not another audit wave** —
and this assessment is itself an instance of the pattern it is naming.

### T6 — `tests/` is the largest ungoverned surface (3 of 5)

**159 `sys.path.insert` across 131 files** under `tests/`, while `conftest.py` does no path setup at
all. 18 files define a `_load*` helper; 34 hand-roll `importlib.util.spec_from_file_location`. A
1,650-line `_kernel_tests.py` lives *inside* the shipped contest package. Design vocabulary, tools
and registers all have registries; **tests have none.**

---

## 2. Lessons

**L1 — the highest-priority class: rules already written and still not followed.**
§0.1 point 5's guard rule is applied per *incident*, not per *pattern*. Falsifiable form: for each
named recurring pattern — bare `random.` call, new degree ladder, new `sys.path.insert`, new `_load`
helper, CURRENT.md stamp block — **either a test in `tests/valoria/` fails on a new instance, or the
pattern is unowned.** Today exactly one of those five has such a guard.

**L2 — a hand-reconciled authority needs a structural validator, not a date validator.**
CURRENT.md's stamp chain should parse as strictly-descending dates with unique ED-sets. It does not,
and no tool can see it. The same rule would have caught `glossary.md:45` and `HANDOFF.md:49`.

**L3 — a count is admissible only if a reader with `grep` reproduces it.**
Demonstrated in both directions this wave: the `armature` census (1,859 occurrences / 263 files) was
**reproduced exactly, in one grep**, by an independent agent. The 32-term / ~26,000-use census in
CLAUDE.md §4 **cannot be reproduced from the tree** — nine terms are listed, "23 more" are not, and
no script was committed. It is now baked in as a convention's motivation. §0.1 point 4 already
requires this and the irreproducible number shipped anyway.

**L4 — new: "archived / deprecated ≠ dead" is load-bearing in three unconnected places and named in
none.** `deprecated/archives/editorial*` (the citation universe), `audit/` (a parity oracle and the
fork-divergence harness, both pinned by shipped tests), `*_archive.jsonl` (the primary ID surface).
Rule for a cold session: **before culling anything under an archive-named path, grep `tests/` and
`tools/` for it** — the repo's own classifier does not do this for `audit/`.

**L5 — a ratchet needs a burn-down owner or it is a monument.**

---

## 3. Cull and consolidation candidates

Sorted by the repo's own rule (ED-IN-0163): *an absent or unused path is dead only if its SUBJECT
was retired, never merely because nothing calls it.*

### SAFE TO CULL
| What | Why | Risk |
|---|---|---|
| ~8 duplicate stamp blocks in `CURRENT.md:31` | Accidental splice copies; originals remain in the same line | Hand-editing the priority-1 authority — diff the stamp-ID sequence and land L2's structural check in the same commit |
| `'designs/'` in `SCAN_PREFIXES` (`validate_ed_citations.py:120`) | Subject retired 2026-07-19 — passes the ED-IN-0163 test; filters a tree that cannot be yielded | Near-zero, but this file's docstring records that touching walk scope starved the universe once; use its pre-change control |

### CONSOLIDATE
| What | Why | Risk |
|---|---|---|
| `TN_STANDARD` → `dice_engine.py` | 3 live defs, same value, owner has none; the committed plan already prescribes it | `tests/sim/v32-combat-balance/` is a frozen reference — repoint the live two, annotate the frozen copy |
| 8 of 11 degree ladders → `dice_engine.degree_from_net` | **Need no design ruling** | Exclude `faction_action.py:97` — 45% band divergence, needs a ruling |
| Test path bootstrap → `conftest.py` | 131 files, 159 copies | Scope to `tests/valoria/` + `engine/tests/`; leave frozen `tests/sim/` |
| 6 `restructure_ledger.md` parsers → `tools/pathres.py` | The consolidation pathres already falsely claims | Each migration ships its own expected-delta test |
| `patch_register_active.yaml:9-15` archive pointers | Point at `deprecated/archives/patches/*`, **verified non-existent** | Annotate `FORK:` rather than delete — the only remaining PP provenance trail |

### LOOKS DEAD BUT KEEP
- **`systems/mass_battle/sim/`** (incl. the 1,905-line god-module) — retired by J2, keep-pinned by
  ED-IN-0127/0128, and **still the engine the live campaign runs on**.

  ⚠ **CORRECTED 2026-08-14 (Jordan, in session). Every lens framed this as "dual engines, canon
  question open". THE CANON QUESTION IS SETTLED AND HAS BEEN SINCE 2026-08-03.** Jordan: *"I've
  ruled on mass battle like eighteen times. It's the one with a huge amount of code and the target
  of loads of commits, not the tiny shit one that kept being used in simulations with opposing
  military rolls."*

  **Measured, so no future session can mistake which is which:** `tests/sim/mass_battle/` is
  **11,269 lines across ~30 modules** (engine, geometry, perimeter, percell, contact, exchange,
  attrition, troop_types, equipment, validators, provenance) — the big one, the commit target,
  **canon**. `systems/mass_battle/sim/` is **2,385 lines**, of which `massbattle.py` is a single
  1,905-line god-module — the small one, retired.

  `systems/mass_battle/sim/__init__.py:1-11` already records J2 correctly. **The audits kept
  re-raising a settled question**, which is a direct cost of the framing in CURRENT.md and prior
  audit prose, not of any genuine ambiguity.

  **Migrating `faction_action.py` onto the canon engine needs two plain decisions, and neither is
  about mass battle:**
  1. **When a faction takes a strategic action, is "how well did it go" judged against how hard the
     action was, or against fixed numbers?** Canon (`dice_engine.degree_from_net:94-122`) scales to
     the difficulty — beat it by double for Overwhelming, meet it for Success, fall short but beat
     zero for Partial. `faction_action._degree:97-104` ignores difficulty: 3+ Overwhelming, 1–2
     Success, exactly 0 Partial, below Failure.
  2. **Does scraping exactly zero count as a partial success, or a failure?** Canon says failure.
     `faction_action` says partial. Same number, opposite outcome.

  (A third difference, not part of this call: `faction_action` rolls d6 counting 4+, while the
  canonical engine is d10. That is the separate `#1b` strategic-layer question.)

  ⚠ The source comment at `systems/mass_battle/sim/__init__.py:8-9` calls this "ruling the four
  `degree` band edges", and an earlier draft of this document repeated that phrase. **It does not
  mean anything in English** (Jordan, 2026-08-14) — it is exactly the coined-jargon failure §4
  legislates against, propagated by copying a source comment instead of translating it.

  Lens B measured the surrounding surface: **8 of 11 degree sites are mergeable with no decision at
  all**; only `faction_action.py:97` needs these two answers.
- **`audit/2026-06-03-contest-groundup/engine.py`** and **`audit/2026-08-13-.../fork_divergence.py`**
  — pinned by shipped tests. Evacuating `audit/` per the classifier **breaks a shipped test.** These
  need the promotion path that does not exist.
- **`registers/editorial_ledger_in.jsonl`** — looks superseded by its archive; it is the documented
  active surface. The fix is rotation semantics, not deletion.
- **`tools/valoria_rename.py`** — dead by census, and the designated executor of a ratified proposal.

### NEEDS A RULING
- **`systems/combat/sim/combat.py`** — called "a DEPRECATED third resolver still shipping", but it is
  **live-imported at `engine/cross_scale/scene_dispatch.py:273`**. Retiring it means repointing the
  scene-dispatch seam — a design call.
- **The PP citation family** — `checked_prefixes=('ED',)` validates no PP at all; the universe is
  evacuated; the active register's own pointers dangle. Restore, blanket-`FORK:`, or drop PP from the
  provenance grammar.
- **Ledger rotation semantics** (`_archive` as write surface) — directly in ED-IN-0179's lineage.
- **`godot/` disposition** — see M2.

---

## 4. Where the lenses disagreed — not smoothed

**D1 — a finding was OVERTURNED.** Lens A claimed "shipping gates reach into `audit/`" citing
`engine/tests/test_sigma_leverage_parity.py:12`. The synthesis pass read it: that file **no longer**
imports the audit oracle — it reads a committed golden table *specifically to remove that coupling*.
The claim is **overturned for that citation and upheld for `test_fork_divergence.py:33`**. The
finding survives on one leg, not two.

**D2 — B and D disagree about the §4 census, and both are right differently.** B treats it as
*understating* (it missed `armature`, the largest ungoverned coinage). D treats it as
*irreproducible*. Both hold: B's own counts reproduce exactly by grep; the §4 census does not.
**Do not cite "32 terms / ~26,000 uses" as measured.**

**D3 — the bootstrap counts conflict and the direction is the point.** A measured 152 occurrences /
126 files; the synthesis measured 159 / 131. Either drift or scope mismatch — **either way the count
rose**, which is consistent with A's own verdict against the wave.

**D4 — D's severity was overstated and is softened.** The `_archive` inversion is real
doc/semantics rot, but `validate_ed_citations.py:162-168` derives per-lane archives into the ED
universe *by construction*, and `id_reservations.yaml:234` correctly tracks the archive max. Soften
from "inversion" to **"misnamed primary surface, gate-coherent."**

**D5 — the grades are unanchored and should not be averaged.** A's B− sits atop a false acyclicity
claim and a corrupted priority-1 authority; B's C+ sits atop a genuinely working single-source
registry. **Rank the findings, not the letters.**

---

## 5. What all four lenses missed

**M1 — `workplans/workplan_v6_progress.yaml` is a month stale and its freshness check watches ghost
trees.** `as_of: 470aa09, 2026-07-16` — the board the SessionStart banner reads, untouched across
the entire audit-wave period. Its own anti-rot rule (`:8-12`) watches `designs/`, `registers/handoffs/`,
`canon/`, `sim/` — **two of those four were retired**, so the staleness detector is itself half-blind.
Rows still cite `sim/cross_scale/echo_transport.py`. This file exists because its predecessor
"killed `roadmap_state.yaml`" by rotting in exactly this way.

**M2 — `godot/` received zero examination from any lens**, despite being the port target that
justifies the entire engine/params apparatus. `id_reservations.yaml:244`: `GO: next_free: 1` —
**not one Godot ED has ever been allocated.** No `HANDOFF_GO.md`. And
`godot_architecture_specification.md:723` carries a literal unfilled template line —
`## Status: NOT STARTED / IN PROGRESS / COMPLETE` — sitting outside the `STATUS_HEAD_LINES = 80`
parse window the G8 consolidation just standardized, so the single Status owner cannot see the one
Status line in the port spec either way.

**M3 — nobody opened `registers/patch_register_active.yaml`** despite three lenses citing the
433/452 dangling-PP figure. It holds **6 active entries**; its header points at six archive files
that no longer exist; the oldest has sat `provisional` since 2026-04-14. The PP system is not merely
unvalidated — **its active register is a husk whose own pointers dangle.**

---

## 6. Verdict

| Dimension | Grade | The one thing holding it there |
|---|---|---|
| Structural rigour | **B−** | Two governing invariants in CLAUDE.md are false as written; the currency authority is corrupted |
| Vocabulary & formulae | **C+** | Design vocab has a real single source (B); process vocab is ungoverned (D); formulae have an owner nothing enforces (C−) |
| Modularity | **B−** | Seams exist in the right places |
| Injectability | **C+** | Every seam has a silent bypass and no guard fails on regression |
| Workflow compliance | **B** | Machine-enforced where it matters most; the perimeter is asserted in prose |

**On the wave work specifically: B+ for process compliance, and "instrumented the disease more than
it cured it" for effect.** Both are true. The §0.1 discipline in those commits is the best in the
tree — instruments committed, controls run, refutations recorded against the author's own claims —
and the underlying single-owner debt is untouched, with three new bootstrap copies and one new
load-bearing instrument in `audit/` added by commits themed on single ownership.

**The highest-leverage change is not a code change.** It is T5: a batched ruling session. Four of the
five largest duplications in this tree are blocked on a decision, not on effort.

**The second is one commit:** repair `CURRENT.md:31` and teach `currency_consistency_check` to fail
on a non-monotonic stamp chain. That closes the most-independently-rediscovered defect in the set and
retires a whole class of invisible rot.
