# Personal Combat — Execution Plan for a Fresh Session

**Status: WORK ORDER — ready to execute. Batches E0–E3 need NO decision from Jordan; E4+ are ⚖-blocked.**
**Date:** 2026-07-28 · **Lane:** PC · **Scope:** executing the remediation identified in the 2026-07-26 combat arc.

**What this is:** `combat_remediation_plan.md` says *what* and *why* and *in what order*. This says **how**, for
a session starting with zero context. It carries the exact targets, the guards to write, the acceptance checks,
and — most valuably — **the traps the authoring session actually hit** (§2), so they are paid for once.

**Prerequisite reading, in this order and no more:**
1. `combat_remediation_plan.md` §2 (traceability), §3 (⚖ split), §4 (why structural precedes behavioural)
2. `combat_defect_register.md` — §G (independent audit, F1–F10) and §H (structural, H1–H7)
3. This file

Do **not** read the value catalogue (26.6k tokens) up front. **Query it** — `python workbench/catalogue.py values`.

---

## §1 Bootstrap

```bash
cd /home/user/ttrpg
pip install numpy pyyaml pytest          # NOT preinstalled; balance.py needs numpy and fails hard without it
git fetch origin main && git checkout -B claude/<your-branch> origin/main
python -m pytest tests/valoria -q        # ~8 min. RECORD THE BASELINE before touching anything.
```

**Baseline, measured on `047b428` (2026-07-28): 894 passed / 21 skipped / 3 xfailed / 3 xpassed** in ~10 min.
For reference it was 877 at `2353b31` two days earlier — **main moves, so re-measure rather than trust this
line.** **A batch that changes this count without saying so in its commit message has failed its disclosure
obligation.**

Instruments, all in `systems/combat/combat_engine_v1/workbench/`:

| command | use |
|---|---|
| `python workbench/balance.py all 300` | weapon matchup · attribute parity · tradition field · C1 context |
| `python workbench/balance.py armour 200` | weapon × armour matrix — **`0.0` at heavy means ZERO DECIDED, not 0%** |
| `python workbench/armour_participation.py participation 200` | plate capability vs measured decided-rate |
| `python workbench/armour_participation.py --drift` | which reference cells moved |
| `python workbench/build_levers.py all 600` · `mirror 2000` | build levers · the fairness control |
| `python workbench/catalogue.py values\|coupling\|mechanics\|constants` | any per-weapon number |
| `python workbench/structure_scan.py` | ownership / hard-coding / organisation counts |

---

## §2 Traps — paid for once, by the authoring session

These are not hypotheticals. Every one cost real time.

1. **Return to the repo root before any file edit.** The edit-time naming-guard hook resolves
   `tools/hook_naming_guard.py` **relative to cwd**. If you `cd` into the engine directory and then Write/Edit,
   every edit fails with a confusing `can't open file .../combat_engine_v1/tools/hook_naming_guard.py`. Run
   engine commands with `cd ... && python ...` in a single Bash call, or `cd /home/user/ttrpg` before editing.
2. **`tools/valoria_local.py --staged` does NOT run pytest.** Local-green ≠ CI-green (CLAUDE.md §8). Run the
   suite **after** your change, not before.
3. **`tests/valoria/test_build_proposals.py` pins the proposals-doc count** (20 as of 2026-07-28, and it has
   moved twice this week). Adding *anything* to `proposals/` requires bumping the assert **and** appending a
   comment line. This plan's artifacts go in `audit/`, which is not pinned — keep it that way.
4. **`registers/handoffs/HANDOFF_PC.md` has a 20,000-token cap** and the authoring session blew through it
   **four times** by appending summaries. It is an index, not a log. **As of ED-IN-0086 it also has an owner:
   `tools/handoff_atomize.py`** — use it; do not hand-restructure.
5. **The engine-params JSON is nested.** `json.load(...)['sections']['cfg' | 'core']` — 201 + 25 = **226 params**.
   A naive top-level probe reports 5 keys and returns "not exported" for everything. The authoring session made
   exactly this mistake and nearly wrote the false negative into a plan.
6. **Line numbers drift.** The independent audit's line references were 20–30 lines off within two days.
   **This plan targets function names only.** Locate with `grep -n "^def <name>"`.
7. **After your PR merges, the branch must be restarted from main** (`git checkout -B <same-name> origin/main`)
   and pushed with `--force-with-lease`. A merged PR cannot carry follow-up work.
8. **`compliance_check.py` is a separate gate** from `valoria_local.py`. Run
   `python tools/compliance_check.py --check-only --repo-state .` and require **0 errors** (warnings are
   pre-existing; do not chase them, but do not *add* one).

---

## §3 Batch E0 — Vocabulary ownership *(prerequisite; no ⚖)*

**Addresses:** M15 (H1) + M12 (F10, H5). **Behaviour-preserving by construction — the guards are the deliverable.**

**Why first:** 279 vocabulary literals across 18 tokens with no owner, and the failure mode is **silent** —
`head == 'cut_thust'` is simply `False`, `HEAD_MODE.get(head, 'shear')` returns the default, nothing errors.
**Two already-confirmed defects have exactly this shape** (F6's unreachable authored mode, A7b's identity
flips). E1–E3 and especially E4/E5 all edit token-keyed branches; doing this first makes them safe.

### Targets
- **Owner:** `core.py` already holds `HEAD_MODE`, `DELIVERY`, `TIER2MAT`. Promote the *token sets* to explicit
  frozen collections there (e.g. `HEADS`, `DAMAGE_MODES`, `ARMOUR_TIERS`, `MATERIALS`) and derive the three
  existing dicts' keys from them, so the tables cannot disagree with the set.
- **Consumers:** every `== 'point'` / `in ('cut_thrust', ...)` comparison across `combat_systems.py`,
  `weapon_physics.py`, `core.py`, `contact.py`, `capabilities.py`, `wrapper.py`.
- **Dead surface (M12):** `combat_systems.can_choke` (zero callers), `config.CHOKE_GRIP_MIN` (zero readers, yet
  **exported to Godot** — third recurrence of a class ED-PC-0035 and ED-PC-0037 each cleaned),
  `weapon_physics.HEAVY_BLUNT_THRESHOLD`, `RHO_IRON`, `_A_HAFT`.

### Guards to ship (the point of the batch)
- **AST guard:** a bare vocabulary literal appears **only** in the owner module. Model it on the existing
  no-weapon-name-in-resolution scan, which already works.
- **CI guard:** every exported CFG key has ≥1 live reader. This is what stops the fourth recurrence.

### Acceptance
```bash
python workbench/structure_scan.py     # vocabulary literals outside owner -> 0 ; dead exported keys -> 0
python -m pytest tests/valoria -q      # unchanged from baseline
python tools/export_engine_params.py --check
```
**Godot export:** the JSON **shrinks** (dead keys removed). That is a disclosure, not a parity risk — say so in
the commit.

---

## §4 Batch E1 — Correctness, no balance intent *(no ⚖; highest value per unit of risk)*

**Addresses:** M5 (F5) + M4 (F4).

### E1a — M5, sign-blind ability channels · **the most urgent item in the whole plan**

**Targets** (`combat_systems.py`, by function): `bind_sigma` — the
`(leverage(agg) − leverage(def)) · eff_cw(agg,'leverage')/eff_cw(def,'leverage')` term; `reach_sigma` — the
`meas_w = eff_cw(defender,'measure')/eff_cw(aggressor,'measure')` term.

**Defect:** a factor > 1 amplifies a **negative** difference, so **investing in a lever makes its owner worse
whenever they are behind on the differential it multiplies.** Verified: a dagger with `staerke_schwaeche`
binding a poleaxe goes **−1.0562 → −1.1904**. Live for every invested build; invisible only because
`equipped=[]` by default.

**Direction:** scale **each side's own contribution**, or the resulting win-probability — never ratio-multiply
a signed difference. (Proposal §5.1 rule 5 states the contract.)

**Guard — parameterised, so new levers inherit it:** for every multiplicative lever, equip it on the
**disadvantaged** side and assert the term does not worsen.

**Reproduce before and after:**
```python
# from systems/combat/combat_engine_v1
import combat_systems as S, tradition as TR
from combatant import Combatant; from config import CFG
base=Combatant('x',weapon='dagger',tradition='german')
inv =Combatant('y',weapon='dagger',tradition='german',equipped={'staerke_schwaeche':1.0})
opp =Combatant('o',weapon='poleaxe')
S.bind_sigma(base,opp,CFG,TR), S.bind_sigma(inv,opp,CFG,TR)   # currently -1.0562, -1.1904
```

**Blast radius:** zero for default builds (`equipped=[]` ⇒ all factors 1.0 ⇒ byte-identical). **Verify that
claim** — it is the batch's safety argument.

### E1b — M4, unclamped capability in σ-path deficits

**Targets** (`combat_systems.py`): `reach_threat`, `represent_measure_p`. **Precedent to copy:** `core.py`'s
ED-PC-0039 clamp, which already states *"'cannot defeat the harness' is a floor at zero capability, not an
unbounded negative one"* — and was applied only in the damage knee.

**Defect:** both feed the raw, possibly-negative `adef_cap` (a pure cutter reads `ADEF_CUT = −0.9`, a
**σ-domain control constant**, not a capability magnitude) into a capability *deficit*. Measured at medium:
represent gate **0.0089 vs 0.207** clamped — **23×**.

**Note:** `armor_defeat_sigma` legitimately keeps the raw signed cap. Do not "fix" that one.

**Guard:** assert the deficit consumers agree on a clamped input.

**Blast radius:** moves cutter-polearms vs mail/plate. **Reference tables will move** — regenerate with
`armour_participation.py --update` and **commit the diff as the disclosure**.

---

## §5 Batch E2 — The zeroes *(no ⚖)*

**Addresses:** M1 (F1) + M9 (F6). Same root cause — a lever form returning 0 at `x = 0` — at two scales.
**Still two commits.**

### E2a — M1, staff percussion authority

**Target:** `weapon_physics.percussion_authority`. **Defect:** it uses **PoB_frac** (CoM offset) as the lever,
so a centre-gripped haft derives **exactly 0 authority regardless of mass**. Verified:
`perc_auth 0.000 / puncture 0.000 / adef_cap 0.000 / percussion_stagger (0.0, 0.0)`. Damage @none: staff **3**
vs mace **17**; staff-vs-arming @heavy **0 decided / 200 draws**.

**It contradicts `percussion_stagger`'s own docstring**, which cites the staff as the worked example of
ED-PC-0031's headline mechanic, and `config.py`'s "staff (p_auth ~4)" comment. **Fix the code and the two
comments; do not fix the comments alone.**

**Direction:** a tip-lever term for centre-balanced hafts — the per-element `|x|/Lt` form already exists in
`percussion_element_authority`.

**Guard:** **no roster weapon with mass > 0 derives 0 percussion authority**; pin the staff's stagger non-zero.

**Blast radius: roster-wide damage.** Both reference tables move. This is the largest change in E0–E3.

### E2b — M9, unreachable authored elements

**Target:** `weapon_physics.percussion_element_authority` — `∝ |x|/Lt`, so any element at `x = 0` is zeroed.
`hook_sword`'s authored crescent (`mode_elements[1]`, "a genuine strike alternative", JD-5) can **never** be
selected: `afforded_heads(hook_sword)` = `{curved_cut, point}` only. **Generalises to any guard-mounted
striking element** — a hand-guard punch has an arm's lever, not zero.

**Guard:** every **authored** `mode_element` is reachable by `afforded_heads` in at least one legal
configuration. This is the guard that would have caught it originally.

---

## §6 Batch E3 — The calibration break *(no ⚖)*

**Addresses:** M3 (F3) + M2 (F2).

### E3a — M3, poleaxe spike adef

`config.py`'s `ADEF_POINT` comment says it was *"set so the poleaxe spike adef ≈ its hammer."* Measured:
hammer **1.216**, spike **0.601**, `ADEF_THRESHOLD['heavy']` **0.72**. PC-5's `thrust_authority` (in `core`'s
`_transmit` gap-press term) halved the spike **after** that calibration, so at heavy
`armor_defeat_sigma = 1.7 · (0.601 − 0.72) = −0.20` — **plate shields against the poleaxe**, on the mode
`select_mode` picks at all four tiers.

**Guard:** `adef_cap(poleaxe, spike) ≥ ADEF_THRESHOLD['heavy']` — ED-1080's intent made **mechanical instead of
a prose claim**, which is why it silently broke.

**Sub-item, do NOT bundle:** the greedy comparator in `select_mode` never prices the adef consequence of its
choice, so a selection can forfeit ~1σ of exchange control invisibly. **That is E5/M7's, not E3's.**

### E3b — M2, thrust-arm heft

**Target:** `weapon_physics.heft` — the lever is chosen by the head **token**
(`THRUST_POB if head=='point' else max(0, PoB_frac)`), so a `cut_thrust` weapon resolving the **puncture** arm
still gets the **swing** moment. Ranseur: **2.515 vs 0.799** (3.1×); damage @none ranseur **26** vs spear **13**.
`weapon_physics` already concedes the bypass in a comment; the ED-PC-0027 fix was never extended.

**Direction:** split on the **resolved arm** (`sel_dmg == 'puncture'`), not the token. **This is exactly the
class E0 makes safe** — it is a token-keyed branch.

**Guard:** `heft(w, thrust-resolving) ≈ heft(w, 'point')` across all 19 `cut_thrust` weapons.

**Blast radius:** damage for 19 weapons. Reference tables move.

---

## §7 E4+ — blocked, do not start

| batch | items | blocked on |
|---|---|---|
| E4 | M6 native cut grading · M8 saturation flat-tops (M16 scoped in) | **⚖1** (re-anchor vs non-saturating form). **⚠ the register's original A7d sketch was a NO-OP** — `min(1, eff/0.70)` against a 0.71–1.33 population clamps everything to 1.0. Do not implement as first written. `MAX_TEMPO_PEN` additionally needs `r3_identity_golden.json` **hand-reproduced — no generator exists.** |
| E5 | M7 mode selection | **⚖7**; largest golden blast radius; interacts with E3 and E4 |
| E6 | M10 off-hand / shield | **⚖6**. Cheap entry: `core.COVERAGE_GAP['partial']` is fully plumbed with **no live caller** |
| E7 | M11 weapon data | partly ⚖ (sparr_axe mode, cinquedea purpose) |
| E8 | M13 build layer · M14 subsystems | proposal §9's blocking claim |
| E9 | M17 typing ⚖8 · M18 organisation | parallel; highest churn — schedule when no behavioural batch is in flight |

---

## §8 Per-commit protocol

Every commit, without exception:

1. **One concern.** The last two same-commit "while I'm here" fixes are why batches 4 and 5 both half-stood.
2. **A guard shipped.** ED-PC-0040: *if you cannot write the guard you have not understood the pattern.*
3. **Godot export impact stated** — which exported constants moved, whether the port consumes them
   (**it covers 1/27 modules**, so usually not), and whether parity debt widened.
4. **Golden diffs disclosed.** Regenerate deliberately; **the diff is the disclosure.** Never regenerate to turn
   a build green.
5. **Falsifier named** for every quantitative claim, with whether it ran and what it returned.
6. **`MEASURED-BY: <path>`** on any ledger entry stating measured numbers — blocking since ED-PC-0040.
7. **One ED per batch**, allocated at point of use from `references/id_reservations.yaml` (**read `next_free`,
   allocate, bump, co-commit — never max+1**). PC `next_free` was **41**; re-read it, it moves.
8. Commit format `[scope] description` citing the ED. Push `-u origin <branch>`, open a PR **ready for review**,
   fill the repo's PR template.

---

## §9 What NOT to do

- **Do not fix `main_gauche` / `paired_short` / `hook_sword` by buffing them.** They are measured in a
  configuration they were never used in (no off-hand slot). That is E6, not a balance change.
- **Do not re-tune off-plate reach.** Proven not reachable by lever — four were swept and every configuration
  that moved it broke `guisarme@heavy`. It needs a closed-phase model rework.
- **Do not touch the resolver** (ED-900/904) or `UPSET_FLOOR` (a tagged designer rule).
- **Do not bundle E3a's comparator sub-item into E3.**
- **Do not quote the armour matrix's heavy column** without cross-checking `armour_participation.py` — `0.0`
  means zero decided, and 38 of 53 weapons hit it.
- **Do not trust a comment.** This session found several contradicting the code on the same line.

---

## §10 Known inconsistencies a fresh session will hit

1. **CLAUDE.md §4 vs `tools/handoff_atomize.py`.** §4 was corrected on 2026-07-26 to retire index+infill as a
   **default** for long documents (sequential `_part2/_part3` at 15k). `handoff_atomize.py` (ED-IN-0086,
   2026-07-28) implements Jordan's **later** ruling that **handoffs specifically** are skeleton + infill, and
   its docstring cites "CLAUDE.md §4 co-filing" — text that no longer says that. **Both rulings are Jordan's
   and the scopes differ (handoffs vs design docs); only the citation is stale.** Do not "fix" either by
   reverting the other.
2. **`combat_balancing_methodology.md` §7** is a 2026-06-28 baseline and **every figure has moved.**
3. **`ability_armature.md` §2c/§7** still lists `seize` as live with `vorschlag`/`sen_no_sen`; `seize` is dead
   and both abilities were removed from `ABILITIES`. Its own "STATUS CORRECTION" banner is itself stale.

## §11 Escalate, do not decide

Eight ⚖ calls are Jordan's (remediation plan §3): M6's direction · armour's wearer-side cost · disposition's
intended shape · 38/53 plate participation · carry-context taxonomy and whether scene-tagging is commissioned ·
off-hand scope · the roster-wide thrust-lean · typed weapon records.

## §12 The blind spot this plan does not cover

**`wrapper.py` has never been audited** — its mutation ordering, RNG-draw sequencing and burst/latch state
machine were only spot-checked by the independent pass. **Stale `sel_*` carryover and draw-order divergence
would live exactly there, and no batch above covers them.** If a session has budget for one more independent
read-only audit, that is the target.

---

## §13 Orchestration — for a max-intensity Opus 5 session

The plan above is correct as a linear work order. This section is what raises its **intensity and intelligence**
without raising its risk. It is written for a session running Opus 5 at maximum effort with a real agent budget.

### 13.1 Tiering, under Jordan's §0.6 ruling

Jordan's 2026-07-28 ruling places **Fable on read-only audit / planner / orchestrator / guardrail — explicitly
NOT synthesis or authorship** (it supersedes CLAUDE.md §10's fable row). Apply it literally:

| stage | tier | why |
|---|---|---|
| the fix itself, reconciliation, judgment calls | **Opus 5 (the session)** | authorship — never delegated to Fable |
| **adversarial gate on each batch** | **Fable, read-only `agentType`** | "top tier on review, not authorship"; risk-identification and gating |
| mechanical sweeps (find every call site of a token; transcribe a table) | **Sonnet** | bounded, verifiable |
| extraction / counting | **Haiku** | deterministic |

**Independence must be structural, not promised.** Proposal P4 records that this repo's critic-independence was
"a display string; no script restricts critic tooling." Use an agent type whose toolset **excludes Edit/Write**
(`Plan` qualifies). A critic instructed to be read-only is not a read-only critic.

### 13.2 The guard-first inversion — the single largest intensity multiplier

The plan says each batch "ships a guard." That is not enough, and this repo already knows why: ED-PC-0040's
verdict was **"a gate that has never failed is decoration."** So invert the order:

1. **Write the guard first.**
2. **Prove it RED on unmodified `main`.** ← the step that makes the guard real
3. Implement the fix.
4. Prove it GREEN.
5. **Mutation-verify** (§13.3).

Without step 2 you cannot distinguish a guard that works from one that is vacuous, and a vacuous guard is worse
than none because it licenses the claim. **Every batch in E0–E3 should be executed in this order.**

### 13.3 Mutation-verify every guard

Each guard ships with **declared mutations that must make it fail, and must be named in its failure message.**
The pattern already exists in-repo: `tests/valoria/test_plate_participation_guard_is_not_blind`. This is what
caught a guard that watched one weapon out of a class of fourteen while the whole suite passed.

### 13.4 Serialization — measured, and the answer is counter-intuitive

**Worktree parallelism buys almost nothing here.** Measured:

| batch | moves a reference table? | parallel-safe? |
|---|---|---|
| **E0** | no — behaviour-preserving | **No.** It touches nearly every module, so it conflicts with everything. Run it **first and alone.** |
| **E1a** (M5) | **NO — verified** | **Yes.** The only independent batch. |
| E1b, E2a, E2b, E3a, E3b | **all move `combat_armour_reference.json`** | **No — strictly serial.** |

**The E1a verification** (run it yourself before trusting it): `eff_cw(c,'leverage')` and `eff_cw(c,'measure')`
return exactly `1.0` for every default build, and **neither `balance.py` nor `armour_participation.py` ever sets
`equipped`** — so the goldens are all default builds and an E1a rewrite cannot move one.

**Why the others cannot parallelise:** each must regenerate the reference table against its *predecessor's*
state. Two batches in separate worktrees produce two reference tables, neither of which is correct, and the
merge silently picks one. **Do not orchestrate parallel write lanes. Orchestrate parallel *verification*
instead** — many critics against one serialized diff.

### 13.5 ⚠ E1a is invisible to the standard harnesses

Corollary of the above, and a genuine trap: because `balance.py` and `armour_participation.py` never equip
anything, **they cannot see E1a at all** — before or after. Running them and observing "no change" proves
nothing.

**E1a's acceptance MUST use `workbench/build_levers.py`**, which is the only instrument that sets `equipped`.
Specifically `build_levers.py abilities 2000`, compared against the pre-fix run.

### 13.6 The adversarial gate, per batch

Per CLAUDE.md §10, agonist→antagonist is a **relay, not a dialogue**:

1. Producer (the session) implements and states its claim.
2. Dispatch a **Fable, read-only** critic with **only the diff and the claim** — *not* the reasoning that
   produced them. A critic that never saw the producer's reasoning is more independent, and for audits that is
   preferable rather than a limitation.
3. Reconcile in the orchestrator. **Record disagreements** — the external-practice review found "disagreements
   are not recorded" to be a standing gap in this repo's method.

### 13.7 N-of-M refutation for any claim that gates a batch

For a claim that decides whether a batch ships — "this is byte-identical", "this guard is not vacuous", "the
reference diff is intended" — dispatch **3 independent refuters, each prompted to REFUTE, defaulting to
refuted-if-uncertain.** Ship only if a majority cannot break it. Reserve this for gating claims; using it
everywhere is waste.

### 13.8 Measurement intensity

| purpose | n |
|---|---|
| a number that gates a decision | **≥ 2000** |
| exploratory / directional | 300–600 |
| the mirror control, before trusting **any** relative number | **2000**, all three loadouts |

The authoring session's ±4pp floor at n=600 was enough to establish *presence*; it is not enough to establish
*absence*, and several of these batches will want to claim absence.

### 13.9 Termination discipline

This repo's remediation history is **three consecutive half-stands** (batches 4, 5, 5.1). Therefore:

- **Cap each batch at 3 adversarial rounds.**
- **If the gate returns a half-stand twice on the same batch, STOP and escalate to Jordan** rather than
  attempting a third fix. Two failed corrections is the documented signal that the model of the problem is
  wrong, not the patch.
- Record a `stopReason` from a closed set — `completed` / `refuted` / `escalated` / `repetition` — **in the
  batch's summary headline**, not buried.

### 13.10 What NOT to orchestrate

- **Do not fan out E0's sweep.** It is a single AST pass over 24 files; one Sonnet does it, and N agents produce
  N inconsistent partial rewrites of the same vocabulary.
- **Do not delegate the fix to Fable.** §0.6 places it on review, not authorship.
- **Do not run a Workflow for E1a.** One function pair, one guard — orchestration overhead exceeds the work.

---
