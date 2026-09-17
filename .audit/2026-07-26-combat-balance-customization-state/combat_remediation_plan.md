# Personal Combat — Comprehensive Remediation Plan (v2, plan of record)

**Status: PLAN — PROPOSED. Nothing executed. Items marked ⚖ are HELD FOR JORDAN.**
**Date:** 2026-07-26 · **Lane:** PC · **Subject:** `systems/combat/combat_engine_v1/`

**Supersedes v1** (same path, 2026-07-26 earlier), which covered only the behavioural findings. v2 adds the
structural axis (§H) and — the substantive change — **re-sequences on the discovery that part of the structural
debt is on the critical path for the behavioural fixes, not parallel to it** (§4).

**Scope: every combat issue raised in this arc.** §2's traceability matrix accounts for all of them, so
"comprehensive" is checkable rather than asserted.

**No engine constant is changed by this document.**

---

## §1 Sources being consolidated

| source | IDs |
|---|---|
| Balance-state report | D1–D8 (= register C1–C8) |
| Defect register §A–§F | A1–A7b · B1–B13 · D-gaps · E1–E5 |
| Independent `fable` audit §G | F1–F10 |
| Structural scan §H | H1–H7 |
| Plan's own adversarial passes | X1–X6 · Y1–Y5 |
| Proposal increments | I-1…I-8 |

---

## §2 Traceability — every ID lands somewhere

Merged into **18 items**. Nothing is dropped; items that are *deliberately* out of scope say so.

| item | absorbs | one-line statement |
|---|---|---|
| **M1** staff percussion | F1, A4-staff | `percussion_authority` uses CoM offset as lever → centre-gripped haft derives **exactly 0**, regardless of mass |
| **M2** thrust-arm heft | F2, A5-ranseur | `heft` keys on head *token*, so 19 `cut_thrust` weapons are paid the **swing** moment on their **thrust** arm |
| **M3** poleaxe spike adef | F3, B5/F19 | PC-5's `thrust_authority` broke ED-1080's "spike ≈ hammer"; **plate shields against the poleaxe** |
| **M4** unclamped cap in deficits | F4, 2 of B6's 4 channels | `reach_threat` / `represent_measure_p` feed raw negative `adef_cap` into a capability deficit |
| **M5** sign-blind ability ratios | F5 | multiplicative levers ratio-multiply a **signed** difference → investment backfires when behind |
| **M6** native cut ungraded | A7a, A3, B2/F21 | `core.coupling` ignores `eff` for native cut tokens → **16 weapons couple identically regardless of edge** |
| **M7** mode-selection pathologies | A7b, B1/F24, M3's comparator sub-item | picks heads that cannot wound; flips identity on a 2.2% margin; never prices the adef consequence |
| **M8** saturation flat-tops | F7, F8/B9, B10, B11 | derived orderings computed then discarded: parry 36/53 identical, tempo 38/53 clipped |
| **M9** unreachable authored content | F6, A1-hook_sword | `percussion_element_authority ∝ \|x\|/Lt` zeroes any guard-mounted element |
| **M10** off-hand absence | A6, A2, A1-partial | no shield/buckler/targe, no off-hand slot; 3 weapons measured in a configuration never used |
| **M11** weapon-data integrity | F9, B3/F22, A4-sparr_axe, A5-jian/tsurugi, A1-cinquedea | `extent_m` inconsistent in-class; 13 records protrude past `head_len`; roster gaps |
| **M12** dead surface + doc drift | F10, H5, E1–E3, B12, B13 | dead keys exported to Godot (3rd recurrence); comments contradicting adjacent code; 2 stale docs |
| **M13** build layer | C1–C8 / D1–D8 | weapon dominance, free armour, monotone disposition, inert focus/tradition/abilities, no tactical layer |
| **M14** absent subsystems | carry context, ED-911 multi-combatant, chargen economy, terrain | design-scale gaps, not defects |
| **M15** vocabulary hard-coding | **H1** | **279 literals over 18 tokens**; no owner for the token set; failure mode is **silent** |
| **M16** numeric hard-coding | **H2** | **127 inline literals, 33 distinct**, against `config.py`'s own "one place" contract |
| **M17** typing / procedural shape | **H3** | 2 classes in ~3,700 LOC; weapons are unvalidated dicts — the root cause of M15 |
| **M18** module organisation | **H4, H6, H7** | `combat_systems.py` god-module (76 fn / 944 LOC); 28 path hacks; comment density 4%→74% |

**Explicitly OUT of scope, with reasons** — so the matrix is honest rather than complete-looking:

| id | why not here |
|---|---|
| **B8** off-plate reach ~0.94 | proven **not reachable by lever** (4 swept; every fix breaks `guisarme@heavy`). Needs a closed-phase model rework — its own project. |
| **B7** 38/53 zero plate participation | ⚖4, a design call, not a defect |
| **E4** `values_master.yaml` stale | quarantined repo-wide (CLAUDE.md §5); not PC-lane |
| **E5** `UPSET_FLOOR` compression | tagged designer rule (ED-PC-0036); retained deliberately |
| `wrapper.py` ordering/RNG/latch | **never audited** — see §9, the largest known blind spot |

---

## §3 Defect vs design call

Mixing these turns a remediation pass into an unratified balance change.

**DEFECTS — the code contradicts its own stated contract. No design input required.**
M1 · M2 · M3 · M4 · M5 · M9 · M11 (protrusions only) · M12 · M15 · M16 · M18

**⚖ DESIGN CALLS — Jordan's. The plan must not pre-empt them.**

| # | call | why it is not mine |
|---|---|---|
| ⚖1 | **M6 direction** — re-anchor `CUT_AUTH_REF` (coupled to the incidental-cut path) or adopt a non-saturating form | either buffs keen curved swords and nerfs dull ones — a balance change |
| ⚖2 | **M13/D2** — should armour cost the wearer, and in which channel | mass/tempo/stamina/mobility all plausible, all absent |
| ⚖3 | **M13/D3** — is disposition a genuine trade, or is aggression simply good | code and its own comment disagree |
| ⚖4 | **B7** — is 38/53 non-participation at plate correct | "defensible and historically recognisable" (ED-PC-0040) |
| ⚖5 | **M14 carry context** — scene taxonomy; is scene-tagging commissioned (X2) | cross-lane; makes balance conditional on a content mix |
| ⚖6 | **M10 scope** — is the off-hand in scope for personal combat, at what priority | subsystem-scale |
| ⚖7 | **M7** — is the roster-wide thrust-lean wanted at all | open since ED-PC-0027/0028; A7b is that question answered as data |
| ⚖8 | **M17** — adopt a typed weapon record, or keep untyped dicts with a guard | the primitive principle wants data-driven; typing is a real architectural commitment |

---

## §4 The sequencing insight that shapes v2

**Part of the structural debt is a prerequisite for the behavioural fixes, not a parallel cleanup.**

- **M15 (vocabulary) before M6, M7, M9.** All three modify **token-keyed branches** — `head=='point'`,
  `HEAD_MODE.get(...)`, element affordance by token. With 279 unowned literals, every such edit risks a silent
  miss, and the two defects already confirmed to have that shape (**F6**, **A7b**) are the proof. Doing M15
  first makes the three highest-blast-radius behavioural fixes both safer and cheaper.
- **M16 (numerics) is scoped *into* M8, not before it.** `defense_affinities` holds **23 inline literals** and
  is the same function F7 shows floor-pinning 36/53 weapons' parry to 0.4. Those band edges *are* the magic
  numbers. Fixing M8 without naming them means re-tuning invisible constants.
- **M12 pairs with M15.** Both need the same new CI guard shape (a check that every exported/declared symbol
  has a live consumer). Building it once serves both.

Everything else in §H (M17, M18) is genuinely parallel and can wait.

---

## §5 Batches

### R0 — Vocabulary ownership *(new in v2; prerequisite)*

**M15 + M12.** One owner for the token set — a frozen registry the `HEAD_MODE`/`DELIVERY`/`TIER2MAT` tables and
every comparison derive from — plus deletion of the dead surface.

| guard shipped | catches |
|---|---|
| AST check: a bare vocabulary literal appears **only** in the owner module | the silent-typo class (F6, A7b shape) |
| CI check: every exported CFG key has ≥1 live reader | `CHOKE_GRIP_MIN` — **3rd recurrence** of a class ED-PC-0035 and ED-PC-0037 each cleaned |

Behaviour-preserving by construction; the guard is the deliverable. **Godot export:** removes dead keys, so the
JSON shrinks — a disclosure, not a parity risk.

### R1 — Correctness, no balance intent *(no ⚖; highest value per unit of risk)*

**M5 + M4.**

- **M5** — stop ratio-multiplying signed differences in `bind_sigma` / `reach_sigma`.
  *Guard:* a **parameterised** test that equips each multiplicative lever on the **disadvantaged** side and
  asserts the term does not worsen, so new levers inherit it.
- **M4** — apply ED-PC-0039's `max(0, cap)` at both σ-path deficit sites.
  *Guard:* assert all deficit consumers agree on a clamped input.

**M5 is the single most urgent item in the plan:** it is live for every invested build and currently makes the
investment system *punish* investment. It is invisible only because `equipped=[]` by default.

### R2 — The zeroes *(things that should work and do nothing at all)*

- **M1** — give the authority lever a tip-lever term for centre-balanced hafts (the per-element `|x|/Lt` form
  already exists). *Guard:* **no roster weapon with mass > 0 derives 0 percussion authority**; pin the staff's
  stagger non-zero, since its own docstring cites it as ED-PC-0031's worked example.
- **M9** — same lever-form defect one layer down. *Guard:* every **authored** `mode_element` is reachable by
  `afforded_heads` in at least one legal configuration.

Same root cause at two scales, **still two commits** — M1 moves damage roster-wide, M9 only un-hides a mode.

### R3 — The calibration break

- **M3** — re-anchor `ADEF_POINT` or exempt the blunt-composite spike from `tauth`; **verify the claim, not the
  comment**. *Guard:* `adef_cap(poleaxe, spike) ≥ ADEF_THRESHOLD['heavy']` — ED-1080's intent made mechanical.
- **M2** — split the heft lever on the **resolved arm** (`sel_dmg=='puncture'`), not the token.
  *Guard:* `heft(w, thrust-resolving) ≈ heft(w, 'point')` across all 19 `cut_thrust` weapons.

**Where the reference tables start moving.** Every commit regenerates `combat_armour_reference.json` with the
diff as the required disclosure.

### R4 — Grading ⚖1 · ⚖7

**M6** (needs ⚖1) and **M8 + M16-scoped-in**. Both restore an ordering the engine already computes and discards.
M8's `MAX_TEMPO_PEN` fix has a known shape (surgical over-cap tail) and a known cost: `r3_identity_golden.json`
must be **hand-reproduced — no generator exists.**

### R5 — Mode selection ⚖7

**M7.** Largest golden blast radius; interacts with R3 and R4. **Deliberately last among resolution batches.**

### R6 — Structure ⚖6

**M10.** Cheap entry: `core.COVERAGE_GAP['partial']` is fully plumbed and **has no live caller** — the shield's
damage hook exists and is merely unreachable. Proposal §13 is the spec. Note this is a **damage-path** change
(equipment physics, legitimately — not a character modulator), so it needs its own calibration.

### R7 — Weapon data ⚖ partly

**M11.** Protrusions and `extent_m` consistency are defects; sparr_axe's missing armour-defeating mode and
cinquedea's purpose are content/design.

### R8 — Build layer and subsystems

**M13**, **M14**, and the proposal's increment ladder (I-1…I-8). **Gated by the proposal's §9 blocking claim: a
modulation layer built before weapon dominance is resolved will measure as inert, exactly as the ability layer
already did.** Note I-1…I-4 are themselves independent of that blocker.

### R9 — Organisation *(parallel, no dependency)*

**M18** (split `combat_systems.py` along the container doctrine; comment-density floor) and **M17** ⚖8.
Lowest urgency, highest churn — schedule when no behavioural batch is in flight, because it moves code that
every other batch edits.

---

## §6 Rules binding every batch

Each is a lesson this lane already paid for.

1. **One concern per commit.** The last two same-commit "while I'm here" fixes are why batches 4 and 5 both
   half-stood.
2. **Ship a guard.** ED-PC-0040: *if you cannot write the guard you have not understood the pattern.*
3. **State the Godot export impact.** All **226 params** are exported (201 `cfg` + 25 `core`), so every batch
   touching `config.py`/`core.py` trips the blocking round-trip gate. The gate checks JSON-matches-config, **not**
   that the port implements the constant — record widened parity debt in the same commit.
4. **Disclose golden diffs.** Regenerate deliberately; **the diff is the disclosure.** Never regenerate to turn
   a build green.
5. **Name the falsifier** for every quantitative claim, and say whether it was run and what it returned.
6. **`MEASURED-BY:`** on any ledger entry stating measured numbers (blocking since ED-PC-0040).
7. **One ED per batch**, allocated at point of use. PC `next_free = 41` — recorded, **not reserved**.

---

## §7 Verification strategy

| batch | primary instrument | acceptance |
|---|---|---|
| R0 | `workbench/structure_scan.py` | vocabulary literals outside the owner → **0**; dead exported keys → **0** |
| R1 | new lever-sign test | no lever worsens its owner's term on the disadvantaged side |
| R2 | `workbench/catalogue.py` | no mass > 0 weapon at 0 authority; every authored mode reachable |
| R3 | `workbench/armour_participation.py` + reference drift | poleaxe spike clears threshold; heft parity across 19 weapons |
| R4–R5 | `workbench/balance.py` + texture test | ordering visible; §8-band aggregate; texture floor met |
| R6–R7 | armour reference + `build_levers.py` | within bands; A2's three weapons re-measured *in configuration* |
| R8 | `build_levers.py` + `context_weighted_field` | per proposal §8 |

**Standing caveat:** `pytest tests/valoria` (877) and the 290 combat tests are **shipping gates, not belief
gates** — the fable audit found F1–F6 all present with the suite green. Every guard above exists because the
current suite cannot see these.

---

## §8 Recommended order, and what to do first

**R0 → R1 → R2 → R3** are all defect-only, need no ⚖, and are independently valuable. **If only one batch
runs, run R1** — M5 alone is making investment backfire. **If two, R0 then R1**, because R0 makes everything
after it safer.

R4 onward is either ⚖-blocked or golden-heavy and should not start until R0–R3 have landed and the reference
tables have settled.

---

## §9 Honest state of the evidence

- **Verified by me with a falsifier:** M1, M3, M5 (re-run against the fable audit's claims), M6/A7a, M15, M16,
  the M12 export facts, and the carriability bands.
- **Carried at the auditor's confidence, not re-run:** M2, M4, M9, M11's `extent_m` spread, M8/F7's band counts.
- **One correction already made to my own work:** the register's original A7d fix sketch was a **no-op**
  (`min(1, eff/0.70)` against a 0.71–1.33 population) — caught during increment planning and amended at source.
- **One scan false positive**, checked and discarded (`WoundTracker` zero-caller).
- **Largest blind spot: `wrapper.py`'s mutation ordering, RNG-draw sequencing, and burst/latch state machine.**
  The fable pass spot-checked only. Stale `sel_*` carryover and draw-order divergence would live there, and
  **no batch in this plan covers them.** That is the strongest candidate for the next independent audit.
