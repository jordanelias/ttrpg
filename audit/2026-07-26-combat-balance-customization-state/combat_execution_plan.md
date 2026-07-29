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
- **Dead surface (M12) — CORRECTED (review R-2):** `config.CHOKE_GRIP_MIN` (the **only** dead CFG key of 201,
  yet **exported to Godot** — third recurrence of a class ED-PC-0035 and ED-PC-0037 each cleaned),
  `weapon_physics.HEAVY_BLUNT_THRESHOLD`, `RHO_IRON`, `_A_HAFT`.
  **⚠ `combat_systems.can_choke` was on this list and MUST NOT BE DELETED.** It is called at
  `tests/valoria/test_combat_units_refactor.py:118` and pinned per-weapon in `r3_identity_golden.json` — the
  fixture with **no generator**. Deleting it breaks a 1e-9 identity golden inside a batch sold as
  behaviour-preserving. The claim came from `structure_scan.py`, whose caller sweep did not search `tests/`;
  **the scanner is fixed and the corrected count is ZERO zero-caller functions.**

### Guards to ship (the point of the batch)
- **AST guard:** a bare vocabulary literal appears **only** in the owner module. Model it on the existing
  no-weapon-name-in-resolution scan, which already works.
- **CI guard:** every exported CFG key has ≥1 live reader. This is what stops the fourth recurrence.

### Acceptance — CORRECTED (review R-6)

**⚠ `structure_scan.py` cannot print the stated acceptance today.** Its `[D]` section counts *all* vocabulary
literals across 14 engine + 11 workbench modules with **no owner concept**, and it has **no dead-exported-keys
check at all**. Extending the scanner is **unstated work inside E0** — budget it, or the acceptance is
unmeasurable. Note also that the count cannot reach 0 unless the sweep rewrites the 11 workbench tools too,
which contradicts §3's own six-module consumer list. **Decide the scope explicitly.**

**⚠ Do NOT mechanically derive the three dicts' keys from one set (R-6b).** `DELIVERY` **deliberately** lacks
`'cut_thrust'` — ED-PC-0037 deleted that dead entry from the Godot contract. Keyset-equality **resurrects it**,
reversing a ledgered cleanup and re-widening the export. `TIER2MAT`'s keys are armour tiers, not heads: they are
**different vocabularies** and must stay separate sets.

**⚠ `workbench/armour_participation.py:67` calls `adef_cap(..., 'edge')`** — a token in no set, falling through
to `ADEF_CUT`. The AST guard will flag it, and "fixing" it changes the participation capability convention that
**E1b and E3a acceptance depend on**. Leave it, and whitelist it explicitly with a comment.

```bash
python workbench/structure_scan.py     # after extending it: literals outside owner -> 0 ; dead exported keys -> 0
python -m pytest tests/valoria -q      # unchanged from baseline (894 at 047b428)
python tools/export_engine_params.py --check
```
**Godot export:** the JSON **shrinks** (dead keys removed). That is a disclosure, not a parity risk — say so in
the commit.

---

## §3a Ordering and blast radius — corrections from the adversarial review

**Serialization (review R-9, and §1–§12 never stated it).** `E1b, E2a, E2b, E3a, E3b` **all regenerate the
single `tests/valoria/data/combat_armour_reference.json`** and are therefore **strictly serial** — each diff
must be taken on its predecessor's baseline. `E0` conflicts with everything (24+ files). **`E1a` is the only
independent batch.**

**E2 before E3 is load-bearing, not incidental (R-9).** A non-gated tip-lever term in E2a moves
`bec_de_corbin` (PoB 0.122), `lucerne_hammer` (0.133) and potentially the poleaxe hammer (0.206) — so E3a's
"spike ≈ hammer" target **shifts under E2a**. Do not reorder them.

**The E0-first justification was over-claimed (R-9).** §3 says "E1–E3 all edit token-keyed branches." False for
half: `E1a` (`bind_sigma`/`reach_sigma`) and `E1b` (`reach_threat`/`represent_measure_p`) contain **no
token-keyed edits** — pure arithmetic and a clamp. The genuine beneficiaries are **E3b, E4, E5**. E0 remains a
sensible first batch, but **no shared-baseline conflict forces it**: if E0 stalls, **E1a can land
independently**, and the remediation plan's own §8 says "if only one batch runs, run R1."

**Golden blast radius is larger than §5 states (review R-3).** Three committed fixtures pin
`percussion_authority` **directly** — `r3_identity_golden.json` (1e-9, plus `puncture_pressure`),
`golden_heft_percussion_snapshot.json` (1e-6), and `golden_element_parity.json` (1e-9, and it also pins the
`afforded_heads` token map **and `select_mode` across all four tiers**). **E2a breaks all three at minimum on
the staff rows; E2b breaks element-parity's affordance/selection pins**, and if the lever-form change touches
`percussion_element_authority` generally it moves every 2H sword's Mordhau value as well. **`r3_identity_golden.json`
has no generator and must be hand-reproduced.** Budget E2 accordingly — it is the most expensive batch in E0–E3,
not E4.

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

**Direction — NARROWED (review R-4).** The original offered two options; **"scale each side's own
contribution" is NOT safe here and fails this batch's own guard.** `leverage()` is signed and **14 of 51
weapons are negative** (rapier −0.0792, bear_spear −0.0611, falchion −0.0576, szabla −0.0436, stiletto −0.0330,
voulge −0.0317, …), so scaling a negative own-contribution by a factor > 1 makes the invested owner *worse* —
the exact defect being fixed. For the plan's canonical pair (dagger + `staerke_schwaeche` vs poleaxe) own-side
scaling gives −0.6734 against a −0.6708 base: **red on the guard.**

**Use the win-probability form** (modulate the resulting probability/magnitude, which is positive by
construction), **or** state explicitly how negative own-contributions are handled. Do **not** reach for
"clamp `leverage` at 0 inside `bind_sigma`" as an escape — it changes default-build behaviour and destroys the
batch's byte-identity safety argument. (Proposal §5.1 rule 5 states the contract.)

**Guard — parameterised, so new levers inherit it:** for every multiplicative lever, equip it on the
**disadvantaged** side and assert the term does not worsen.

**⚠ The guard is VACUOUS unless the tradition-access gate is respected (review R-7).** An equipped technique
outside the fighter's known kit is inert (`ability_primitives._invested`, ED-PC-0028). Verified: `misura` on a
default-tradition fighter moves `reach_sigma` **not at all** — so the guard would pass on today's broken code.
Set the tradition: `misura`→`italian`, `staerke_schwaeche`→`german`, `atajo`→`spanish`. With
`tradition='italian'` the breakage appears (−1.025 → −1.1787).

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

**Guard — with a concrete RED-ON-MAIN pin (review R-11.3).** "Assert the consumers agree" is an
implementation-consistency check with no stated failing form, so it could ship green on broken code. Pin the
numbers instead, using a pure cutter against mail (`bardiche`, raw `adef_cap` **−0.9000**):

| quantity | on main (broken) | must become |
|---|---|---|
| `reach_threat(bardiche, medium)` | **0.5275** | the `max(0, cap)` prediction (**0.843**) |
| `represent_measure_p(bardiche, medium)` | **0.0089** | the `max(0, cap)` prediction (**0.207**, a 23× move) |

Both are red on main today — verified. Assert against the clamped-cap prediction, not against a hard-coded
constant, so the guard survives a legitimate recalibration of the surrounding terms.

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

**Direction — and E2a/E2b MUST AGREE ON ONE FORM (review R-11.4).** E2a needs a tip-lever term for
centre-balanced hafts. **Do not copy `percussion_element_authority`'s `|x|/Lt` verbatim — that is the very form
E2b declares defective**, because it returns 0 for any element at `x = 0`. Copying it would propagate the bug
from the element scale to the weapon scale.

**Both batches want the same underlying quantity: a STRIKE-POINT lever** — the distance from the hand to where
the weapon actually strikes — not a CoM offset (E2a's current bug) and not a bare `|x|` about the haft origin
(E2b's current bug). **Design the shared form once, in E2a, and have E2b consume it.** If the two batches ship
different lever forms, one of them is wrong.

**Guard — SCOPED (adversarial review R-1; the original was unimplementable):** **no BLUNT-NATIVE weapon derives
0 percussion authority.** The original read "no roster weapon with mass > 0", which goes red on **37 of 51
weapons, 36 of them correct by design** — `reversed_grip_percussion` returns 0.0 for every 1H weapon and every
hafted non-blunt head, with historical grounding in its own docstring. Scoped to blunt-native, **only the staff
fails** (mace 8.0, poleaxe 7.484, bec 6.363, lucerne 6.539, goedendag 8.0, staff **0.0**). Also pin the staff's
stagger against a **band** (config's own "staff p_auth ~4"), not merely non-zero — an epsilon would satisfy
non-zero.

**Blast radius: roster-wide damage.** Both reference tables move. This is the largest change in E0–E3.

### E2b — M9, unreachable authored elements

**Target:** `weapon_physics.percussion_element_authority` — `∝ |x|/Lt`, so any element at `x = 0` is zeroed.
`hook_sword`'s authored crescent (`mode_elements[1]`, "a genuine strike alternative", JD-5) can **never** be
selected: `afforded_heads(hook_sword)` = `{curved_cut, point}` only. **Generalises to any guard-mounted
striking element** — a hand-guard punch has an arm's lever, not zero.

**Guard — PER-TOKEN, not per-element (review R-11.1):** every authored `mode_element`'s **head token** must
appear in `afforded_heads` for at least one legal configuration.

**It must NOT be written per-element.** `afforded_heads` returns a token→best-element map, so when a weapon
carries two elements sharing a token only one wins the union — correctly. **Four weapons do this:**
`poleaxe` (blunt + point + point), `bec_de_corbin` (blunt + point + point), `lucerne_hammer` (blunt + blunt +
point), `kama_yari` (point + curved_cut + curved_cut). A per-element guard flags all four as broken; a
per-token guard flags **only hook_sword**, which is the actual defect.

---

## §6 Batch E3 — The calibration break *(no ⚖)*

**Addresses:** M3 (F3) + M2 (F2).

### E3a — M3, poleaxe spike adef

`config.py`'s `ADEF_POINT` comment says it was *"set so the poleaxe spike adef ≈ its hammer."* Measured:
hammer **1.216**, spike **0.601**, `ADEF_THRESHOLD['heavy']` **0.72**. PC-5's `thrust_authority` (in `core`'s
`_transmit` gap-press term) halved the spike **after** that calibration, so at heavy
`armor_defeat_sigma = 1.7 · (0.601 − 0.72) = −0.20` — **plate shields against the poleaxe**, on the mode
`select_mode` picks at all four tiers.

**Direction — ADDED (review R-5: this batch shipped without one).** Two candidates differ by an order of
magnitude in blast radius, and the plan must not leave the choice to a zero-context session:
- **Re-anchoring `ADEF_POINT` 1.2 → ≥1.44** clears the guard (0.7217) but raises `armor_defeat_sigma` for
  **every selected-point weapon at every armoured tier** — a de facto roster-wide balance change inside a batch
  labelled "no ⚖", and a config change tripping the Godot export gate. **This is ⚖ territory; escalate rather
  than take it.**
- **Exempting the blunt-composite spike from `tauth`** is the surgical option, but needs a native-blunt +
  selected-point branch that also reaches bec_de_corbin / lucerne_hammer / goedendag spikes. **Prefer this, and
  state the three collateral weapons in the commit.**

**Guard — STRENGTHENED (review R-5):** pin **spike ≈ hammer** (the actual ED-1080 contract; hammer measures
1.2162), not merely `≥ ADEF_THRESHOLD['heavy']` = 0.72. The weak form passes a fix that clears the threshold
while still contradicting the calibration it claims to restore. Making it mechanical instead of a prose claim
is why it silently broke.

**Sub-item, do NOT bundle:** the greedy comparator in `select_mode` never prices the adef consequence of its
choice, so a selection can forfeit ~1σ of exchange control invisibly. **That is E5/M7's, not E3's.**

### E3b — M2, thrust-arm heft

**Target:** `weapon_physics.heft` — the lever is chosen by the head **token**
(`THRUST_POB if head=='point' else max(0, PoB_frac)`), so a `cut_thrust` weapon resolving the **puncture** arm
still gets the **swing** moment. Ranseur: **2.515 vs 0.799** (3.1×); damage @none ranseur **26** vs spear **13**.
`weapon_physics` already concedes the bypass in a comment; the ED-PC-0027 fix was never extended.

**Direction:** split on the **resolved arm** (`sel_dmg == 'puncture'`), not the token. **This is exactly the
class E0 makes safe** — it is a token-keyed branch.

**Guard — needs BOTH sides (review R-8):** `heft(w, thrust-resolving) ≈ heft(w, 'point')` **and** the
complementary pin `heft(w, shear-resolving) ≈ native swing heft`. The one-sided form is red on main (ranseur
2.5151 vs 0.7992 ✓) but **passes a wrong fix that pays the thrust lever on both arms.**

**Disclose, do not discover:** `core.cut_thrust_arm` picks the arm on **coupling alone**. Once impact differs by
arm, the chosen arm is no longer the max-damage arm for some weapons — a fresh instance of the B1/F24
"selection contradicts damage" class, introduced by a correctness batch and interacting with ⚖7/E5. Ranseur
resolves `puncture` even at `none`, so this is live at every tier. **State it in the commit as an expected
consequence.**

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

## §14 Adversarial review record (Fable, read-only, 2026-07-28)

An independent `fable`-tier reviewer with a **write-excluded toolset** scored §1–§12 against live code. It was
told to treat every claim as motivated, because the plan was written by an agent reviewing its own session's
work. **Eleven findings; five would have caused a wrong result.** All corrections are folded in above, at
source, rather than appended.

| # | finding | disposition |
|---|---|---|
| **R-1** | E2a's guard ("no weapon with mass > 0 derives 0 authority") goes red on **37 of 51 weapons, 36 correct by design** — `reversed_grip_percussion` returns 0 for every 1H and hafted non-blunt head. Unimplementable; invites roster-wide over-reach. | **Fixed** — scoped to blunt-native (only the staff fails). ✅ re-verified by me |
| **R-2** | `can_choke` is **not dead** — called at `test_combat_units_refactor.py:118`, pinned in `r3_identity_golden.json` (**no generator**). Deleting it breaks a 1e-9 golden inside a "behaviour-preserving" batch. **Second false positive from the same scope bug.** | **Fixed** — removed from the dead list; **`structure_scan.py`'s sweep now includes `tests/`**; corrected count is **0** zero-caller functions; register §H5 corrected at source. ✅ re-verified |
| **R-3** | Golden blast radius understated: **three** fixtures pin `percussion_authority` directly, and element-parity also pins `afforded_heads` **and `select_mode` at all four tiers**. The hand-reproduce cost lands in **E2a, not E4**. | **Fixed** — §3a states it; E2 re-labelled the most expensive batch in E0–E3 |
| **R-4** | E1a's own direction backfires: `leverage()` is signed and **14 of 51 weapons are negative**, so "scale each side's own contribution" makes an invested owner worse — **red on this batch's own guard**. | **Fixed** — direction narrowed to the win-probability form; the clamp escape is explicitly forbidden. ✅ re-verified |
| **R-5** | E3a shipped **no direction**, and the two candidates differ by an order of magnitude; the guard (`≥0.72`) is far weaker than the contract it claims to mechanize (**spike ≈ hammer**, 1.2162). | **Fixed** — direction added, `ADEF_POINT` re-anchor marked ⚖, guard strengthened to spike ≈ hammer |
| **R-6** | E0's acceptance is **not measurable by the named instrument** (no owner concept, no dead-key check); mechanical keyset-derivation would **resurrect `DELIVERY['cut_thrust']`**, reversing ED-PC-0037; `adef_cap(...,'edge')` will trip the new guard. | **Fixed** — all three stated in E0's acceptance with explicit instructions |
| **R-7** | E1a's guard is **vacuous unless the tradition gate is set** — `misura` on a default-tradition fighter moves nothing, so the guard would pass on broken code. | **Fixed** — tradition mapping added to the guard spec |
| **R-8** | E3b's guard is one-sided (passes a wrong fix paying the thrust lever on both arms), and the fix creates a **new selection-vs-damage disagreement** (B1/F24 class) that the plan did not disclose. | **Fixed** — complementary pin added; the consequence is now a disclosed expectation |
| **R-9** | The E0-first justification over-claims — E1a/E1b contain **no token-keyed edits**. True constraint is E0 before E3b/E4/E5. Also: the **serialization constraint was never stated**, and **E2-before-E3 is load-bearing** (E2a moves the hammer E3a targets). | **Fixed** — §3a |
| **R-10** | The verified/carried distinction eroded: E1b/E2b/E3b numbers presented as flat fact without the "carried at auditor's confidence" marker. **All three happen to be true** — the reviewer re-ran them — but the framing was not honest to its sources. | **Accepted.** F2/F4/F6 are now independently verified; the plan no longer needs the marker, but the lapse is recorded |
| **R-11** | Four specification defects: E2b guard ambiguity (per-token vs per-element), the staff-stagger pin gameable by an epsilon, M4's guard has no stated red-on-main form, and E2a directs copying the very lever form E2b declares defective. | **ALL FOUR FIXED.** E2b guard is now per-**token**, with the four duplicate-token weapons (poleaxe, bec_de_corbin, lucerne_hammer, kama_yari) named as the reason a per-element form would be wrong — verified. Stagger pinned to a band. M4's guard carries a concrete red-on-main pin (bardiche vs medium: `reach_threat` **0.5275**, `represent_measure_p` **0.0089**, both verified) asserted against the clamped-cap prediction rather than a constant. E2a/E2b are now required to share **one strike-point lever form**, with an explicit warning not to copy the defective `\|x\|/Lt`. |

**Found SOUND and not to be re-litigated:** every headline number in E1–E3 reproduces exactly on live code
(bind_sigma −1.0562→−1.1904; staff 0.0/0.0/0.0 and stagger (0,0); hook_sword affordance and its uniqueness in
the roster; poleaxe 1.2162/0.6013/0.72 with the spike selected at all four tiers; ranseur 2.5151/0.7992;
represent gate 23.3×). Also sound: E1b's "do not fix `armor_defeat_sigma`" note; E0's factual base (279
literals, `CHOKE_GRIP_MIN` the only dead CFG key, the 226-param nesting); every §2 trap; E1a's byte-identity
argument; §12's blind-spot claim; and the §7 A7d NO-OP note — **the reviewer hunted for further no-ops among
all E0–E3 directions and found only R-4's conditional backfire.**

**Not reached:** §13 (it post-dates the review — two of its gaps, serialization and E1a's instrument, duplicate
R-9 and R-7, which is corroboration); the simulation-sweep numbers (38/53, F7/F8 band counts); the Godot port's
actual consumption of `CHOKE_GRIP_MIN`; and `wrapper.py`'s ordering/RNG audit, which §12 already flags.

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
