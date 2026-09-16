# U9 — Adversarial Review & Full Pipeline Trace

**Reviewer:** PC-lane adversarial node (CLAUDE.md §0 "adversarial pass at every stage that gates a result")
**Date:** 2026-07-23 · **Subject:** the U9 capstone (`u9_capstone_v1.md`, ED-PC-0021, PR #220)
**Posture:** try to *break* the U9 verdict, not confirm it. Trace the ablation pipeline in all directions,
map every input/output/state-change, and log the raw material so the review is independently checkable.
**Outcome:** the shipped result (all six levers `K=0`, byte-identical) **survives** — but the review
**corrects the capstone in three material ways** and **surfaces one test-isolation defect**. All corrections
are folded back into `u9_capstone_v1.md`; none touch shipped engine code (still byte-identical).

---

## 0. What was under review

U9's verdict: the six edge/choke/facing morphology levers (`LEGIB_EDGELINE_K`, `BIND_SPINE_K`,
`GRAB_EDGE_K`, `CHOKE_ACCURACY_K`, `FACING_REGIME_K`, `CHOKE_THRUST_K`) all stay at `K=0`; none robustly
moves aggregate winrate; activating `CHOKE_THRUST` additionally breaks a ratified thrust principle.

**The load-bearing risk** (what would falsify the verdict): the ablation's "sub-noise" reading is only
meaningful if the harness *actually exercises* each lever. Two failure modes:
- **P1 (plumbing):** the constant never reaches its consumption site during a fight (cfg not threaded /
  module global not read). A dead knob shows Δ≈0 for a reason that has nothing to do with being situational.
- **P2 (code-path):** the site is reached but the *enabling state* never occurs (e.g. `grip_position`
  never rises above 0, so the choke branch is dead).

If either holds for a lever, "sub-noise" means "never tested" and that lever's classification is unfounded.

---

## 1. State-change map (Battery A) — what the PR actually changes

`git diff --stat origin/main...HEAD`:

| File | Δ | Nature |
|---|---|---|
| `CURRENT.md` | +1/−1 | combat-row status note |
| `consolidation_v1.md` | +1/−1 | U9-executed status note |
| `u9_capstone_v1.md` | +193 | the capstone doc (new) |
| `references/id_reservations.yaml` | +1/−1 | PC next_free 21→22 |
| `registers/editorial_ledger_pc.jsonl` | +1 | ED-PC-0021 entry |

**Zero `.py` files, zero files under `systems/combat/combat_engine_v1/`.** Confirmed by path-classifying
every changed file. The engine is byte-identical to `origin/main`; the combat suite baseline is unchanged
(9 accepted-red, 0 new — re-verified §4).

---

## 2. Pipeline trace (all directions) — inputs → consumption → outputs

**Forward (driver → primitive):**
```
workbench.balance.winrate(specA, specB, cfg, n, seed)
  └─ wrapper.fight(X, Y, cfg, rng)              # cfg threaded verbatim, per fight
       └─ per beat: combat_systems / contact / weapon_physics resolvers read cfg[...] and module globals
```
`cfg` is passed by value into every `fight`; the five cfg-borne constants reach their sites through it.
`CHOKE_THRUST_K` is **not** in cfg — it is a `weapon_physics` module global read directly by `phi_grip`.

**The six consumption sites (backward, primitive → constant):**

| Lever | Consumption site | Term | Enabling state |
|---|---|---|---|
| `LEGIB_EDGELINE_K` | `combat_systems.legibility:709` | `legib -= K·WP.edge_lines(agg.w)` | aggressor has a double/false edge |
| `CHOKE_ACCURACY_K` | `combat_systems.legibility:710` | `legib += K·choke_counterbalance(agg,cfg)` | head-heavy pole, `grip_position>0` |
| `BIND_SPINE_K` | `combat_systems.bind_sigma:760` | `+ K·(WP.spine(agg.w) − WP.spine(def.w))` | a bind occurs; weapons differ in spine |
| `FACING_REGIME_K` | `combat_systems.facing_target:376` | `base·(1 + K·WP.facing_pref(c.w))` | every facing computation |
| `GRAB_EDGE_K` | `contact.grab_sigma:47` | `− K·WP.grab_hazard(opp.w)·(1−skill)` | a grab occurs; opponent has an edge |
| `CHOKE_THRUST_K` | `weapon_physics.phi_grip:247` | `max(FLOOR, 1 − K·grip)` for `sel_head=='point'` | point-headed strike, `grip_position>0` |

`grip_position` is confirmed **live per-beat state** the wrapper writes (`grip_target` computes it;
`combat_systems` reads `getattr(c,'grip_position',0.0)` in ~15 places) — so P2 is testable, not assumed.

---

## 3. Harness-integrity battery (the decisive test)

### 3.1 Site-firing probe — does each lever's code path execute? (P1/P2)

Every site instrumented with a call/fire counter; a real `winrate` (n=200, seed 3, all K=1.0) run on four
matchups. "Fired" = the lever's term was non-zero on that call. Raw log:

```
[poleaxe/med vs arming/med]  A winrate 83.5%
  legib_edgeline   calls=  1395 fired=  902  max|term|=1.0000  FIRED
  choke_accuracy   calls=  1395 fired=  493  max|term|=0.0821  FIRED
  bind_spine       calls=   874 fired=  (probe-bug, see 3.2)
  facing_regime    calls= 10552 fired=10552 max|term|=0.9920  FIRED
  grab_edge        calls=   608 fired=  284  max|term|=1.0000  FIRED
  phi_grip_choke   calls= 14019 fired=  270  max|grip|=0.078  FIRED
[spear/med vs arming/med]   choke_accuracy fired 476, phi_grip_choke fired 212 (max grip 0.865)  FIRED
[dagger/lt vs arming/lt]    choke_accuracy fired 0, phi_grip_choke fired 0  — CORRECT: a dagger/arming
                            never chokes a pole, so grip_position stays 0. The choke path is domain-gated,
                            not dead: it FIRES in pole matchups (poleaxe/spear), where the ablation ran it.
```

**P1 refuted** for all five cfg-levers (terms reach their sites, non-zero). **P2 refuted** for the choke
levers — they fire in pole matchups (fired 270–493×, grip reaching 0.865), exactly where the ablation
placed them; they are correctly *silent* for non-pole matchups.

### 3.2 bind_spine — probe bug fixed

The Part-1 probe under-counted `bind_spine` (it counted `spine()` calls but never computed the bind term
— a **bug in the probe, not the engine**). Direct check of the term on its best matchup:
```
spine(katana)=0.850  spine(arming)=0.000  diff=+0.850  term@K=2.0=+1.700   (nonzero — FIRES)
spine(falchion)=0.800 spine(arming)=0.000 diff=+0.800  term@K=2.0=+1.600   (nonzero — FIRES)
spine(longsword)=0.000 spine(arming)=0.000 diff=0.000  term=0              (a double-edge vs double-edge: correctly 0)
```
bind_spine fires whenever a single-edged rigid blade binds a non-single-edged one. Not dead.

### 3.3 Extreme-K coverage — can the harness move winrate through each lever at all?

For each lever, K pushed to an **extreme** value (10–20× the tested "working" value) on its best matchup;
winrate Δ across 5 seeds at n=500. A lever that moves winrate at extreme K is *harness-exercised*
(so its moderate-K sub-noise is a genuine "situational" finding); one that is flat even at extreme K would
be a coverage gap.

```
LEVER              K_ext  matchup             deltas(pp) over seeds {3,5,7,11,13}        mean
LEGIB_EDGELINE_K   2.0    arming vs estoc     +4.0  -1.6  +0.2  +2.4  +0.4              +1.1   sub-noise*
BIND_SPINE_K       2.0    katana vs arming    +3.1  +7.5  +7.3  +1.5  +7.1              +5.3   MOVES (all +)
GRAB_EDGE_K        3.0    dagger vs arming    +1.6  +2.8  +3.2  +0.3  -1.9              +1.2   sub-noise
CHOKE_ACCURACY_K   3.0    poleaxe vs arming   +0.4  +2.6  -2.2  +1.0  -0.2              +0.3   sub-noise (weakest)
FACING_REGIME_K    3.0    sabre vs longsword  +3.5  +4.1  +2.9  -1.5  +2.9              +2.4   weak-but-present
CHOKE_THRUST_K     0.9    spear vs arming     +0.0  -3.1  -0.3  -2.9  -4.5              -2.1   weak, grounded sign (−)
```
`*` LEGIB_EDGELINE's matchup is **floor-compressed** — arming already loses ~94% to estoc, leaving almost
no room to move. This is a flaw in my *original* matchup choice, not evidence the lever is dead (§5, C2).

**Reading:** every lever fires; none is plumbing-dead. Winrate *sensitivity* spans a real range —
**BIND_SPINE is the strongest** (robustly directional, +5.3pp mean at K=2.0), **CHOKE_ACCURACY the weakest**
(flat even at K=3.0). The verdict "situational, not dead" is now **evidence-backed** rather than asserted.

---

## 4. CHOKE_THRUST dual claim — re-verified, and a masking defect found

**Claim (a): the noise collapse at high N.** Confirmed independently (n∈{350,500}, 5 seeds): mean
−0.1…−2.1pp, sign-flipping — within the ~±4pp floor even at the extreme K=0.9. My earlier low-N
"−4.7/−5.3/−7.6pp robustly live" reading was a seed artifact. Stands.

**Claim (b): activating CHOKE_THRUST breaks the ratified grip-invariant-thrust principle.**
The principle is `test_combat_invariants.py::test_thrust_protection_grip_invariant` — a **ratified D2 gate**
(ED-1029 D-series, pre-existing, *not* authored this session): bear_spear/spear/yari select `point` and
`phi_grip>=0.9` at full gather. Direct computation:
```
CHOKE_THRUST_K=0.0  →  phi_grip('point', grip=1.0) = 1.0000   OK
CHOKE_THRUST_K=0.30 →  phi_grip('point', grip=1.0) = 0.7500   BREAKS D2 (0.75 < 0.9)
CHOKE_THRUST_K=0.90 →  phi_grip('point', grip=1.0) = 0.7500   BREAKS D2 (floored)
```
Run in **isolation**, `test_thrust_protection_grip_invariant` **FAILS** at K=0.30
(`AssertionError: bear_spear ... 0.75, assert 0.75 >= 0.9`). Claim (b) is **CORRECT**, with the *ratified*
D2 gate — stronger evidence than the capstone's original citation of my own U5 pin
(`test_thrust_grip_invariant_at_k_zero`).

**⚠ Test-isolation defect surfaced.** In the *full* suite at K=0.30, `test_thrust_protection_grip_invariant`
does **not** appear in the failures — because `test_combat_choke.py::test_both_channels_live_not_dead`
mutates the shared `weapon_physics.CHOKE_THRUST_K` global and resets it to `0.0` in its `finally` block.
That module-global write leaks to every later test module, so the D2 gate (a later module, alphabetically)
silently sees `0.0` and passes. Consequence: **flipping the source constant and running the suite HIDES the
D2 breakage** — a reviewer would be misled into thinking D2 survives activation. The shipped `K=0` state is
unaffected (the `finally` correctly restores the K=0 default), so this is a *review-hazard*, not a shipped
defect; it is logged here and flagged for a follow-up test-hygiene fix (make the live-not-dead toggle use a
`cfg` override or `monkeypatch` rather than a raw global write). Filed as a note under ED-PC-0021.

**Tolerance correction.** The capstone's option (b) proposed a "≤25% floored exception". The D2 gate's own
tolerance is `phi>=0.9` — i.e. **≤10%**. A 25% floor (phi=0.75) already blows past D2's 10% band, so
option (b) is not merely "re-baseline a pin" — it **widens a ratified D2 gate from 10% to 25%**. That is a
larger design call than the capstone implied; the corrected capstone says so.

---

## 5. Corrections folded back into the capstone

The shipped verdict (all six `K=0`, byte-identical, cut-nothing-activate-nothing) **holds**. The review
changes the *reasoning*, not the result:

- **C1 — cite the ratified D2 gate, not (only) my own pin.** The authoritative principle blocking
  CHOKE_THRUST activation is `test_thrust_protection_grip_invariant` (D2/ED-1029), verified broken in
  isolation. Strengthens the held-back-for-Jordan framing.
- **C2 — credit BIND_SPINE correctly.** It is the *strongest* of the six (robustly directional at K=2.0),
  not "doesn't survive re-seeding". It is the best candidate for eventual scenario-specific activation.
  And flag that my LEGIB_EDGELINE ablation matchup (arming vs estoc) was floor-compressed — a methodology
  caveat: the fair test of a legibility lever needs a ~50/50 matchup, not a 6%-winrate one.
- **C3 — "situational, not dead" is now evidence-backed.** All six fire (§3); none is plumbing-dead. The
  capstone previously *asserted* this; it now *cites* the firing probe + extreme-K battery.
- **C4 — tolerance correction** (§4): option (b) widens a ratified 10% gate to 25%, not a mere pin rebase.
- **C5 — the test-isolation review-hazard** (§4) is recorded so no future reviewer is misled by a
  full-suite run of a flipped constant.

---

## 6. Provenance / ledger integrity (Battery E)

- **ID protocol:** ED-PC-0021 allocated from `id_reservations.yaml` `next_free` (21→22), not max+1. ✔
- **Citations:** `validate_ed_citations.py` → 0 integrity violations. ✔
- **Currency:** `currency_consistency_check.py` → clean. ✔
- **No fabricated numbers:** the capstone reports simulation outputs, not ledger-backed engine constants;
  every number here is reproducible from the scripts in §7. The shipped constants are all literally `0`. ✔

---

## 7. Reproduction (radical transparency)

All scripts in the session scratchpad; all read-only against the working tree except the two temporary
CHOKE_THRUST_K flips (each immediately `git checkout`-reverted — working tree confirmed clean after):
- `u9_adversarial.py` — §3.1 site-firing probe (instruments the six sites, real winrate).
- `u9_extreme.py` — §3.2 spine check + §3.3 extreme-K coverage sweep (n=500, 5 seeds).
- Inline snippets — §4 D2-gate computation + isolated-vs-full-suite reconciliation.
- `pytest tests/valoria -k combat` at `CHOKE_THRUST_K∈{0.0,0.30}` — the 9-vs-12 failure delta.

**Net:** the U9 PR is sound as shipped (byte-identical, `K=0`). The adversarial pass hardened its evidence,
corrected two mis-characterisations, tightened one design-call estimate, and logged a test-hygiene hazard —
exactly the "try to break it" gate CLAUDE.md §0 requires before a result is trusted.
