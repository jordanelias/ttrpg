# PC session retrospective + plan v3 — lessons, adversarial pass, revised work order

## Status: RATIFIED as findings (PR #273 merged 2026-07-30, `3005096`; ED-1094). Its **sequencing (§5) is SUPERSEDED** by `combat_completion_plan_v4.md` v4.1 — read that for the live work order; read this for the lessons and the adversarial pass that produced them.

Covers the 2026-07-29/30 PC session that landed **ED-PC-0048..0055** (E2b, E3a, E3b, A7a channel 1,
contact moment, close-unwieldiness derivation, curvature recovery, dead-code sweep). Written because
the session's most valuable output is not the eight batches — it is **what the eight batches proved
about which kinds of change move a field and which do not**, and neither original plan encodes that.

---

## §1 The one lesson that reorders the plan

**Three correct, absent physical mechanisms were built, mutation-verified, and moved the field by
nothing. One fiat-gate removal moved it immediately.**

| batch | what it was | field effect |
|---|---|---|
| ED-PC-0051 (A7a) | native edge quality was derived then discarded — 16 weapons coupled identically | cutters +2..+6 pp, **rapier untouched** |
| ED-PC-0052 (ch. 5) | the bind/parry/wind had **no mass or momentum term at all** | **flat** — rapier 75.6→75.3 across K 0→0.60 |
| ED-PC-0054 (ch. 2) | `curvature` had one runtime consumer, a cost; no recovery benefit existed | **flat** — corr(curvature, Δ) = **−0.003** |
| **ED-PC-0053** | `close_unwieldiness` was a **fiat gate**; every sword paid 0 | **rapier −6.8 pp, spread 40.1→32.5** |

The three that failed were each a genuine missing fact and each worth fixing on correctness grounds.
But as *balance* work they were mis-aimed, and the pattern is legible:

> **Adding a benefit to a weak thing is absorbed by the field. Removing a free ride from a dominant
> thing is not.** Look for missing COSTS on dominant quantities, not missing benefits on weak ones.

The corroborating measurement: **corr(overall length, civilian win%) = +0.850** (+0.742 excluding the
rapier itself). One quantity explains most of the field, and it had four benefit channels (measure,
approach stop-hit, true-time edge, arrest impulse) against **one** cost channel that was gated off for
every sword. That is the shape to hunt.

---

## §2 Lessons, each with the artifact that earned it

1. **Check pathway THROUGHPUT before building — necessary, not sufficient.** ED-PC-0052 went into
   `bind_sigma` (~1.2 evaluations/fight) and was structurally too thin to matter at any K. ED-PC-0054
   *did* check first and went into the recovery path (every committed attack) — and was still inert,
   because effect SIZE against the ~4 pp noise floor also has to clear. Throughput screens out the
   hopeless; it does not promise the rest.
2. **Unbounded inputs mis-scale; bounded ones cannot.** Three scaling terms in one session:
   `S_g` carries units → a linear differential was dimensionally incoherent; `I_g` spans ~1000× → a
   linear multiplier read guandao **48.9** against 2.10; `curvature` is dimensionless [0,1] → safe by
   construction. **The reusable guard is a range assertion on the multiplier**
   (`test_the_discount_is_bounded_by_construction`), which would have caught the first two.
3. **Pre-register the prediction.** ED-PC-0054's was written into the test docstring before measuring
   and **failed** (predicted +1..+3 pp; measured corr −0.003). Without it the noise was rationalisable.
4. **A guard you have not watched fail is not a guard — twice over.** Two of my own guards were
   decoration: one compared two *different* pairings so it passed with the term ablated (it never
   observed its own defect); one asserted a bound the mutant satisfied. Both were caught only by
   running the declared mutation.
5. **Detectors need controls too.** The dead-code sweep's first version reported **8 live functions as
   dead** by ignoring intra-module calls. Hand-checked before reporting; nothing acted on.
6. **Do not trust a prescription, even a recent one.** E2a's docstring, plan §5 and the E2a commit all
   specified a call signature for E2b that would have dropped percussion **19–37% on all 53 weapons**.
   Measured before consuming.
7. **Fiat hides inside things that look derived.** `max(0, reach_base − CLOSE_REACH_REF)` reads as a
   derivation. It is a threshold on a scale that includes the body offset `L0`, and the docstring
   claimed "pure morphology" while gating every sword to zero.
8. **Threshold cliffs create absurd sensitivities.** A **4 mm** margin (staff 1.176 m vs a 1.18 m
   implied threshold) decided whether a two-metre quarterstaff gathers its grip in a press.
9. **Corpus claims expire.** Falsified this session: proposal §12.1's "carry context removes the entire
   D1 dominance problem" (it *relocates* it — civilian spread 66.8 pp **exceeds** the battlefield's
   52.1); `geometry.py`'s "shamshir/pulwar/scimitar correctly collapse toward 0".
10. **Texture ≠ aggregate, and it cuts both ways.** ED-PC-0052 moved **122 of 212** armour-reference
    cells while leaving field ordering untouched. A term can be simultaneously live per-event and
    inert in aggregate — which is a reason to measure both, not a licence to claim the good one.

---

## §3 Adversarial pass on this session's own work

Genuine attacks, run rather than asserted. Four land.

### 3.1 ⚠ `CLOSE_ENGAGE_M = 0.45` is indistinguishable from a tuned value — MEASURED, and it is the worst finding here

ED-PC-0053's ledger entry states the constant is "deliberately NOT tuned to hit a balance target,
since doing so would reinstate the fiat this batch removes." I chose 0.45 on physical grounds (chest-
to-chest out to a forearm) **before** measuring the field, and never swept it. Swept now:

| `CLOSE_ENGAGE_M` | rapier | spread |
|---|---|---|
| 0.30 | 83.5% | 41.1 pp |
| **0.45 (shipped)** | **75.5%** | **35.1 pp** |
| 0.60 | 79.8% | 41.7 pp |
| 0.75 | 80.8% | 38.5 pp |

**The shipped value is the best of the four on both metrics.** The process was honest; the artifact
cannot demonstrate that, which is precisely §0.1 point 4's warning that absence of one failure mode is
not presence of correctness. Two consequences, and the second matters more:

- The response is **NON-MONOTONE**, which the mechanism's own logic does not predict. Lowering the
  measure to 0.30 makes *more* weapons pay — including the daggers, who lose their "free in the close"
  status — so it helps the rapier *relatively*. Coherent in hindsight, invisible beforehand.
- Therefore **0.45 is not safely "just physical."** The balance outcome is sensitive to it in a
  direction nobody would guess. It needs Jordan's eye, and the sensitivity table is the disclosure.

**Action:** filed as the top item of §5. Do not defend the value on physical grounds alone.

### 3.2 Every field number reported during the session was measured one batch behind

Each batch was measured against the tree *at that moment*, but they compound. The "current balance"
breakdown quoted rapier 73.5% / spread 32.5 pp — measured after ED-PC-0053 but before ED-PC-0054.
True current state, measured now:

**rapier 71.8% · spread 30.7 pp · sd 8.2 pp** (was reported as 73.5 / 32.5 / 8.3).

The direction of every conclusion survives; the numbers were stale. **Action:** any future balance
claim states the SHA it was measured at, as the golden fixtures already do.

### 3.3 Two situational levers shipped with their validating measurement never taken

ED-PC-0052 and ED-PC-0054 are both aggregate-inert and both were shipped citing the U10/ED-PC-0022
ruling that the correct instrument for a situational lever is **per-fight texture with outcome
preservation**, not aggregate winrate. **That texture measurement was not run for either.** Shipping on
a precedent while skipping the measurement the precedent names is a thinner argument than it reads as.
The instrument exists (`test_levers_add_texture_without_shifting_balance`). **Action:** §5 item 2.

### 3.4 I made two of the register's own structural items worse

- **M18 (god-module):** `combat_systems.py` was 76 fn / 944 LOC in the register; it is now **80 /
  1059**, three of those functions mine (`forward_extent`, `contact_moment_edge`, `wound_impairment`).
  Each was a correct single-owner extraction that landed where its callers were. Correct locally,
  regressive globally.
- **ED-PC-0050 introduced a new instance of the B1/F24 selection-vs-damage class** (`cut_thrust_arm`
  picks on coupling alone, so the chosen arm is no longer the max-damage arm). Disclosed and pinned,
  but it is new debt created by a correctness batch.

### 3.5 Attacks that did NOT land, recorded so they are not re-run

- *"The curvature benefits double-count."* No — `cut_factor` (edge presentation), `arrest_impulse`
  (braceability) and the recovery discount are three distinct facts, and the net is pinned.
- *"The moment term duplicates `leverage()`."* No — corr(leverage, log S_g) = **+0.109**, and within
  the ten civilian swords the two measures nearly invert.
- *"The engine is full of dead code."* No — an AST call-graph over engine + workbench + tests found
  **zero** unreferenced functions, **zero** CFG keys with no reader, **zero** test-only tunables.

---

## §4 Flagged this session, absent from both workplans

| # | item | why it is not covered |
|---|---|---|
| **N1** | `CLOSE_ENGAGE_M` sensitivity + non-monotonicity (§3.1) | the constant did not exist |
| **N2** | Texture measurement owed for ED-PC-0052 + ED-PC-0054 (§3.3) | those levers did not exist |
| **N3** | **`point_concentration` correlates −0.729 with `curvature`** across 42 bladed weapons — the tip data was authored *as* a function of curvature and `thrust_factor` penalises curvature *again*. shamshir pc **0.08**, below sparr_axe's 0.10 (an axe). In-roster template: **szabla, curv 0.30 / pc 0.60** | M11 covers "weapon-data integrity" but names `extent_m`, protrusion and roster gaps — **not** a systematic tip-data confound |
| **N4** | ED-PC-0054's effective size **rides on N3** ((1−pc) = 0.70..0.92 amplifies it) → must be re-measured once N3 lands | interaction did not exist |
| **N5** | **No layering/acyclicity guard.** "Module Shape" checks cross-*container* reach-ins only. Nothing stops `weapon_physics` importing `combat_systems` or a cycle forming | M18 is about size/organisation, not about *pinning* the dependency invariant |
| **N6** | `CLOSE_EFF_GAP_REF = 6.5` is now unanchored — its justification ("shares `CLOSE_REACH_REF`'s magnitude") died with that constant | new orphan created by ED-PC-0053 |
| **N7** | The **byte-exact MB digest gate is not environment-stable** — CI and local disagree on which of `unit_mode`/`cell_mode` drifts, symmetrically on main and on the PC branch | MB lane, surfaced incidentally |
| **N8** | Three lanes crossed the 50k ledger cap in one week; each archive cap is hand-added | IN lane, process |
| **N9** | Session-crosses-midnight ⇒ guaranteed `currency.stamps` regression on any `systems/`+`engine/` work | IN lane, process |

---

## §5 Revised work order

### What changes versus the originals

`combat_execution_plan.md` §7 orders E4→E9 by *defect severity*. `combat_remediation_plan.md` §8
orders R0→R9 by *prerequisite*. **Neither encodes §1's finding**, so both would send the next session
at E4 (M6/M8 — more grading and de-saturation, i.e. more *benefits*), which this session has shown is
the shape that does not move a field. Reordered by **expected effect on the thing actually wrong**.

| # | work | why here | blocked on |
|---|---|---|---|
| **1** | **Rule `CLOSE_ENGAGE_M`** (§3.1) — accept 0.45 with the sensitivity table on the record, or re-anchor | a shipped constant sits at a local balance optimum and cannot prove it wasn't tuned | **Jordan** |
| **2** | **Texture measurement for ED-PC-0052 + 0054** (N2) | pays the debt that justified shipping two inert levers; cheap, instrument exists | nothing |
| **3** | **E6 / M10 — off-hand + shield** | **the rapier's actual historical counterweight**, and it is a missing COST on the dominant thing (§1). `COVERAGE_GAP['partial']` is **fully plumbed with no caller** — confirmed independently this session. Also repairs the four false negatives (`main_gauche`/`paired_short`/`hook_sword`/`cinquedea`) that occupy the field's bottom tail | ⚖6 scope call |
| **4** | **N3 — the tip-data confound**, then re-measure N4 | a data defect underneath two shipped terms; has an in-roster template so the values are not invented | ⚖ on the values |
| **5** | **N5 — layering guard** | cheap, generated-from-code, pins an invariant nothing currently checks | Jordan (adds CI surface) |
| **6** | **E9 / M18** — split `combat_systems.py`; **do it before more behavioural batches**, not after | the original defers it to "when no behavioural batch is in flight" — that is *now*, and every batch since has grown it (§3.4) | ⚖8 (typing) |
| **7** | E4 / M6+M8, E5 / M7, E7 / M11 | unchanged in content, **demoted**: all are benefit-side or selection-side, and §1 predicts they will not move the field | ⚖1, ⚖7 |
| — | **Do NOT commission the closed-phase LEVERAGE/DAMAGE rework** | reach is ruled to the future **grid layer**, where it becomes positional range. Four levers were swept and every fix broke `guisarme@heavy` | Jordan's grid ruling |

### Process changes to fold into the next session

- **Every balance claim carries the SHA it was measured at** (§3.2).
- **Every new scaling term ships a range assertion on its multiplier** (§2.2) — the guard that would
  have caught both mis-scaled terms.
- **Pre-register the predicted effect before measuring** (§2.3); record the outcome either way.
- **Run every declared mutation.** Two of eight guards this session were decoration until one was run.
- **Prefer removing a free ride to adding a benefit** (§1) when the goal is balance rather than
  correctness — and say which of the two a batch is, up front.
