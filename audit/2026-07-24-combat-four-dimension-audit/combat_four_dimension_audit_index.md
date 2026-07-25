# Combat Engine — Four-Dimension Read-Only Audit + Remediation (SKELETON)

**Author:** PC-lane audit node (CLAUDE.md §0/§10) · **Date:** 2026-07-24 · **EDs:** ED-PC-0034..
**Subject:** `systems/combat/combat_engine_v1/` at the post-ED-PC-0029..0033 head (PR #231 merged).
**Charter (Jordan):** four independent read-only audits — **fiat, orphans, conflicts, tuning/balance** — each
covering *all directions and conditionals*; then resolve every finding in priority order, batch by batch, with an
adversarial audit after each batch.
**Prose:** `combat_four_dimension_audit_infill.md` (co-filed; method, evidence, per-finding detail, verification).
**Status: IN PROGRESS** — Batches 1–5.2 landed (ED-PC-0034..0040); Batch 6 pending.

Every batch is adversarially reviewed after landing, and the record is deliberately unflattering: batches 1 and 2
returned **stands**, batch 3 **stands with follow-ups**, and batches 4, 5 **and 5.1** all returned **HALF-STANDS** —
each because a fix of mine introduced a *new* defect, or overstated its own reach, on the same code path (batch 4:
per-arm quality sourced from the whole weapon instead of the winning element; batch 5: a negative sigma-domain penalty
fed into a capability deficit, annihilating the cutter class; batch 5.1: a "restored" participation guard that watched
one weapon out of a class of fourteen, plus four factual claims in its own ledger entry and comments that measurement
contradicts). Each was corrected in a follow-up (4.1, ED-PC-0039, ED-PC-0040). Reviews have also caught me **moving a
goalpost** — a ceiling raise justified as "sampling noise" over a real +27pp regression — a **fabricated file entry**
in a ledger `files` array, and an **index that claimed clean reviews it had not had** (this file, corrected by
ED-PC-0040). That cadence is the only reason those are in the record rather than in the engine.

## Method (skeleton)

Four `fable`-tier read-only auditors, structurally independent (each blind to the others' reasoning and to the
author's), read-only tooling, ablation/sim evidence required. Every finding re-verified by hand against the code
before acceptance — the anti-fabrication gate is leaky (CLAUDE.md §7), so no unverified claim is carried.
Aggregate evidence: ~96k ablation fights (orphans), 61,200-fight full grid + 30,158 mirror fights (tuning),
full-file reads + provenance spot-checks against `registers/editorial_ledger_pc.jsonl` (fiat, conflicts).

## Finding roster → remediation batches

| # | Dim | Finding | Sev | Batch | Status |
|---|---|---|---|---|---|
| F1 | tuning | `represent_measure_p` reads stale/native `sel_head`+grip → crowd gate path-dependent | high | 1 | **DONE** |
| F2 | conflicts | `overcommit_exposure` "floored at 0" false; negative value suppresses riposte below base | high | 1 | **DONE** |
| F3 | fiat | `contact.grab_sigma` edge-hazard sign-flips for grab skill > 1 | med | 1 | **DONE** |
| F4 | — | tradition-lever texture instrument under-powered (n=60, knife-edge) | — | 1 | **DONE** |
| F5 | orphans | 6 unread CFG keys, leaking into the Godot-facing engine-params JSON | high | 2 | **DONE** |
| F6 | orphans | `CHOKE_BIND_K` — read lever multiplied by a hardcoded `0.0` at its only call site | high | 2 | **DONE** |
| F7 | orphans | `close` damage param threaded through ~12 sites, never read | high | 2 | **DONE** |
| F8 | orphans | 5 zero-caller functions; dead `Combatant.ready`; unreachable `QUAL`/`COVERAGE_GAP` `'partial'` | med | 2 | **DONE** |
| F9 | orphans | retired imposition machinery still wired (`PREFERRED`/`preferred`/`profile`) | med | 2 | **DONE** |
| F10 | conflicts | stale prose: poise `EFFECT_FLOOR`, facing-profile sign, "deliberately failing" tests that pass, phantom `disengage_prob`, `represent_p` magnitudes, `affords_halfsword` count, `TRUE_TIME_K` citation, `module_contracts` rows | med | 2 | **DONE** |
| F11 | fiat+conflicts | `percussion_stagger`: inline second quality ladder + bypasses the `sel_*` single-source contract | med | 3 | **DONE** |
| F12 | fiat | cut_thrust "versatile max" shear branch is dead (paid as thrust, read as swing) | high | 3 | **DONE** |
| F13 | fiat | Nachreisen pursuit strike resolves at a flat `−0.3` σ, bypassing the σ-assembly | med-high | 3 | **DONE** |
| F14 | fiat | `ATTACKER_BIAS=0.12` untagged/unledgered, duplicates the Vor system | high | 3→4 | **TAGGED**; removal moves to batch 4 (it compounds with F16) |
| F15 | fiat | `UPSET_FLOOR=0.05` post-hoc result inversion (designer rule — tag, do not silently remove) | high | 3 | **DONE** (tagged; retained as Jordan's rule) |
| F16 | tuning | deterministic first-actor race: a 1.5% tempo edge → 2:1 action monopoly; 20 g mass step swings 57↔42% | **structural** | 4 | **DONE** |
| F17 | tuning | `closed = gap ≤ 0.3` latch is a cliff (+9pp across 2 cm); reach curve saturates by gap 1.5 | **structural** | 4 | **DONE** |
| F18 | tuning | off-plate reach over-buff + identity erasure (26 weapons at 94±1; Jordan's ~0.75 target) | high | 4 | **OPEN** — structural precondition landed; the ~0.75 re-tune itself is NOT done (still ~0.94 off-plate) |
| F19 | tuning | plate damage path contradicts `adef_cap`: covert plate-killers (partisan/ranseur/guandao) | high | 5 | **PARTIAL** — inversion attenuated (partisan 11→3), but at equal capability head mass still orders penetration; a knee cannot express the principle |
| F20 | tuning | jian/tsurugi plate paradox (0.04 gap-cap grading → ~95% of decided) | high | 5 | **DONE** (capability-gated) |
| F21 | tuning | flat `ADEF_CUT=−0.90` cutter cliff (a gambeson makes a falchion an 8% weapon) | high | 6 | pending |
| F22 | tuning | roster gaps: sparr_axe horn, falchion point, greatsword/odachi half-sword; staff can't wound | med-high | 6 | pending |
| F23 | orphans | ability/`eff_cw` surface hollow: 5 of 8 channels are identity ×1.0 for every legal build | med | 6 | pending |
| F24 | conflicts | **selection contradicts damage**: `select_mode` picks a head that provably cannot wound — falchion 46/47 plate strikes select `point` for 0 damage every time; podao selects `point` (mean 0.00) over its own `curved_cut` (mean 2.40); every 2H sword flips to `blunt` at mail and lands ~3× less than the arming sword it faces | high | 6 | pending (found by the ED-PC-0039 review follow-through) |

**Cleared (checked, not findings):** no name-keyed weapon/tradition branches in live resolution; imposition gate is a
verified no-op; provenance spot-checks (ED-1041, ED-901, ED-PC-0002/0009/0022/0023/0027/0029..0033) all passed — **no
fabricated citation found**; wound-Ob / reach / armour-defeat / armour-fade sign conventions consistent across all
consumers; PEN_THR light-inertness and the represent-gate RNG-stream inertness hold exactly as documented; the
"Combat Pool defined three ways" hazard (CLAUDE.md §5) has collapsed to one quarantined stale surface.

## Batch ledger

| Batch | Scope | ED | Result |
|---|---|---|---|
| 1 | correctness bugs (F1–F4) | ED-PC-0034 | full suite green (686 passed, 1 xfailed) |
| 2 | dead code + stale prose (F5–F10) | ED-PC-0035 | behaviour-preserving; 686 passed, 1 xfailed; engine-params 202→194 keys |
| 3 | fiat retirement (F11–F15) + batch-1/2 review corrections | ED-PC-0036 | 122 new regression pins; golden regenerated (label field only, 17 cells) |
| 4 | structural thresholds (F16–F18) | ED-PC-0037 | 1H cohort spread compressed ~25–30%; mirrors clean at n=4000. Review: **half-stands** |
| 4.1 | review corrections | — | element-local sourcing; goalpost + fabricated-provenance corrections |
| 5 | plate damage ↔ adef_cap (F19–F20) | ED-PC-0038 | `adef_cap` moved to core as single owner. Review: **half-stands** |
| 5.1 | review corrections | ED-PC-0039 | capability clamped at ≥0; K swept; a one-weapon participation guard added. Review: **half-stands** |
| 5.2 | 0039 review corrections | ED-PC-0040 | roster-wide participation guard (mutation-verified); 4 false claims retracted; medium round trip + selection/damage disagreement measured |
| 6 | roster + cut grading (F21–F23, F24) | — | pending |

**Correction to this table (ED-PC-0040).** The 5.1 row previously read "cutter class restored; participation guard
restored" and this document previously said batches 1–3 all returned *stands*. Both were overclaims, and the ED-PC-0039
review caught them. The clamp *un-annihilated* the cutter class but did not restore it — it erased all grading *within*
the class (every pure cutter's capability floors to the same 0, so a bardiche and a shamshir now fail plate identically),
and it recovered only part of the medium-tier loss. The guard "restored" was one assertion on one weapon; the review
killed three other plate-defeaters simultaneously and the whole 806-test suite passed.

## Meta-review → enforcement (ED-PC-0040)

Three consecutive half-stands (batches 4, 5, 5.1) share **one cause**, and it is not subtle physics: quantitative
claims were written into ledger entries and code comments faster than they were measured, and the scripts that would
have falsified them were ad-hoc and thrown away. Every finding the reviews returned was reachable by a script that
takes two minutes to run. The measured shape of the problem: **31,000 characters** of ledger prose across
ED-PC-0034..0040, `config.py` at **74%** comment density, and batch 5.1 shipping **+27/−5 lines of code** wrapped in
~3,500 characters of claim.

The lessons are therefore converted into gates rather than into resolutions to be more careful. A resolution is what
failed three times.

| Lesson | Enforcement | Catches |
|---|---|---|
| Measurement must be a committed artifact, not scratch | **`workbench/armour_participation.py`** — the four views (`participation`, `strikes`, `tiers`, `--drift`) that produced every number in §5.2, in the repo and re-runnable | the whole class — a claim is now a *query*, not a recollection |
| A guard must be attacked before it is trusted | **`test_plate_participation_guard_is_not_blind`** — declared mutations that MUST make the participation guard fail, *and* must be named in its failure message | **S1**: a guard watching 1 of 14 while the class dies |
| Every rule lives once (CLAUDE.md §8) | the CI guard **imports** `capability()`/`_duel()` from the instrument instead of re-deriving them (the first draft inlined a copy — that duplication was itself the bug class) | guard and instrument drifting apart |
| Collateral tier damage must be visible | **`tests/valoria/data/combat_armour_reference.json`** + `test_combat_armour_reference.py` — full roster × all four tiers, drift gate at 0.15; regeneration is manual and *the diff is the disclosure* | **S3**: a plate fix silently moving mail by 23pp |
| A measured claim must name a re-runnable source | **`tools/ci_claim_provenance_check.py`** — blocking, CI job `claim-provenance-check` + local hook; a ledger entry stating measured numbers needs `MEASURED-BY: <path>` and the path must exist | **S2/S8**: "estoc → 0" about the roster's most decisive plate weapon |

Verified, not asserted: the drift gate was confirmed to **fire** on a real change (`PEN_DEFICIT_K` 6.0→2.0 → 13 cells
flagged by name), and all four declared mutations are caught by the participation guard. A gate that has never failed
is decoration.

**The limits, stated plainly.** The provenance gate checks that a source is *named and present*, not that a number is
*correct* — the same limit CLAUDE.md §7 records for the anti-fabrication gate; a reviewer still has to run the thing.
Its cutover is an **ID, not a date** (ED-PC-0040 forward), because every entry in the failing arc carries the same date
as the entry establishing the rule; the five grandfathered entries are corrected by retraction, not excused. And the
drift gate is defeated the moment someone regenerates the reference to turn a build green without reading the diff.

**What no gate here fixes:** the treadmill itself. F19 (damage vs capability), F24 (selection vs damage) and S4
(grading inside the cutter class) are one defect — three separate models of "what does this weapon do to this armour",
reconciled pairwise by patch. Each batch closes one pair and exposes the next. That is a design call for Jordan, not
something a validator can enforce.

## Known-open after batch 5.2 (carried, not hidden)

- **F5/F18 — the flagship principle is attenuated, not achieved.** At equal capability, head mass still orders
  penetration (partisan cap 0.176 out-damages spear cap 0.288 at every K). A magnitude *knee* cannot express
  "capability orders penetration" — that needs multiplicative gating. Batch-6 redesign.
- **Off-plate reach is still ~0.94**, not Jordan's ~0.75 target. Batch 4 removed the structural obstacle; the tuning
  pass was never performed.
- **Four-channel double-count.** The same armour-defeat deficit now enters `armor_defeat_sigma`, `reach_threat`,
  `represent_measure_p` and the penetration knee, with no recorded budget — against a repo rule that forbids exactly
  that.
- **34/51 weapons decide zero fights at plate.** Defensible under PC-5 and historically recognisable, but a large
  behavioural fact worth a design decision rather than an inheritance.
- **`PEN_DEFICIT_K` is exported to a Godot contract whose port has no penetration knee at all** — pre-existing
  parity red, now carrying a second orphan constant.
- **The ranseur is a surviving covert plate-killer** (ED-PC-0040). Capability 0.284 against a 0.72 threshold, yet it
  settles ~12% of its plate fights and wins ~100% of what it settles. The knee is a graded threshold multiplier, not a
  gate, so raw magnitude still buys through — the F19 residual, now named to a specific weapon. `guandao` (cap 0.127,
  mean 2.76/strike) and `partisan` (cap 0.171, 1.96) are the same class one rung lower.
- **The clamp erased grading *inside* the cutter class** (ED-PC-0040, from the 0039 review). Every pure cutter's
  capability floors to 0, so the knee treats a bardiche and a shamshir as failing plate identically. Correct as a
  *floor*, wrong as a *model*: F21's mass/keenness grading is what has to carry the difference.
- **Medium tier never round-tripped** (ED-PC-0040, measured — see infill §5.2). Against arming at mail, n=200:
  odachi 0.67→0.44→**0.26**, naginata 0.82→0.57→0.57, staff 0.21→0.09→0.09, podao 0.61→0.32→0.44,
  sparr_axe 0.36→0.07→0.22 across pre-0038 → 0038 → 0039. The 0039 clamp recovered part of the axe/podao loss, nothing
  of staff/naginata, and made the **odachi worse** — the grip/room threading lowered its realized capability. ED-PC-0038
  said mail was "a tier the fix was never meant to touch"; it touched it, permanently.
- **F24: mode selection and the damage path disagree** (ED-PC-0040). See the roster table above. This is the same
  defect class ED-PC-0038 set out to close, one layer up: 0038 reconciled *damage* with *capability*, but *selection*
  is still keyed on afforded effectiveness with no reference to whether the chosen head can wound the armour in front
  of it. Batch-6 head item; deliberately NOT patched in ED-PC-0040 (it is a `select_mode` change with golden-parity
  blast radius, and the last two same-commit "while I'm here" fixes are why batches 4 and 5 both half-stood).
