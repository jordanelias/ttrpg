# Fable Review — this session's outputs + PR #139, reviewed together (v1)

## Status: FILED — 2026-07-14 · ED-IN-0066 · run NOW at Jordan's instruction, before the plan is treated as final

> Direct Fable-tier review (not a delegated fan-out) of (a) the ED-IN-0064 docket + the remediation plan and
> (b) PR #139's observatory pass — with the findings applied to `remediation_plan_v1.md` in the same commit.
> Verdicts below; the plan's change-log is at the bottom. Where this review revises a classification, it wins
> over the earlier text it corrects.

---

## 1 · The headline ruling: **P5 as scheduled was NOT necessary — demoted to conditional**

Jordan asked "Is P5 necessary?" The honest answer, against my own evidence: **not now, and not as written.**

- **It contradicted a standing ruling.** The armature already ruled `decay()` **deferred to Stratum B+** ("when
  cross-tick convergence work actually starts") — and my own gap register classified GAP-DIR-5 as *"[deferral] —
  do NOT fix now."* Scheduling P5 was un-deferring a ruled deferral without a new trigger. D1 as written even
  asked Jordan to re-rule something already ruled — decision-queue noise.
- **Nothing gameplay-blocking depends on it.** The program's own DAG shows P5 feeding only P6. The findings'
  thesis (~10:1 CTC:GENUINE — "unbuilt wiring on sound logic") means the player-facing value is in P2–P4;
  P5.2's byte-exact migration is *behavior-neutral by construction* — pure internal unification.
- **The convergence risk is live only where D2 wires.** The one place D.6 double-count becomes real *now* is the
  accord-echo composition — and that is already covered by D2 + its exactly-once property test in P3. The
  Mandate↔L/PS loop is already sim-verified bounded/mean-reverting.
- **Its Fable-tiering violated §10's own rule.** "Fable is an upgrade trigger, never a default — promote only on
  evidence a cheaper tier failed." No cheaper tier has attempted Field/Gauge and failed.

**Necessary kernel retained:** the D2 composition rule (P1/P3), and `scale_hierarchy §6` territorial aggregation
when the Territory tier is wanted (FA/SE design work, not a unification primitive). **Everything else in P5 —
`fields.py`, census migration, general `decay()`, the convergence artifact — becomes P5† (conditional):
trigger = Stratum B opening or an explicit D1 opt-in; Opus-first, Fable only on demonstrated failure.**
Scorecard adjusted: temporal direction closes **by classification** (standing deferral), not by wiring.

## 2 · Verdicts on this session's outputs (the ED-IN-0064 docket + plan)

- **The findings substrate holds.** Every scorecard number survives #139's corrections (validation 1/3, doc:null
  9, `[ASSUMPTION]` 13, seams 20, dangling 4, zero-caller 3, `causes[]` 0, join 3/27 — none derived from the
  silently-capped displays #139 fixed; the orphans-87 figure was already flagged as inflated pending the
  `__init__` fix). The five prior adversarial passes did their job on *facts*.
- **The plan's defect was judgment, not facts** — the P5 scheduling above, plus: (i) **D-docket overload** — 16
  undifferentiated rulings is a poor next-steps interface; (ii) **P4's blanket "ground all 11 remaining
  [ASSUMPTION] markers"** is checkbox-ism — several are trivial infra where CLASSIFY is the honest disposition;
  (iii) the critical path was buried rather than led with. All three fixed in the plan (change-log below).
- **Known-stale displays in frozen artifacts:** the merged docket's register/HTML still show the pre-#139
  "52.7% pointer resolved" label and capped section lists. These are historical run outputs — left as history,
  superseded by the P6 rerun; an errata note now sits in the docket README.

## 3 · Verdicts on PR #139

- **Meter-1 (keyed vs matched) — correct and adopted, with one refinement.** 52.7% was mislabeled, but 21.8%
  *understates* health the same way 52.7% overstated it: the 17/55 matched-but-declined names are quantities the
  registry **deliberately declines to key** — that is a disposition, not debt. The honest NS2 meter is
  **three-band**: keyed 12/55 (21.8%) · declared-non-pointer 17/55 (30.9%) · **unresolved 26/55 (47.3%)**.
  Target = unresolved → 0 (each keyed or classified). The plan's scorecard now states it this way.
- **Obs-1/2/3 silent-cap fixes — the pass's best result** (the instrument violating its own "never a silent cap"
  rule was exactly the failure class to hunt). Confirmed none of this docket's headline numbers depended on the
  capped displays.
- **The paren-normalized cycle pass** — real fix; the Mandate↔Legitimacy feedback is now machine-visible
  (closes the narrow GAP-J2; the registry-key node identity remains the deeper P0 item).
- **`head_pointers.yaml` + `REPO_MAP.md` as highest-leverage unblocked action — endorsed** (adopted into P2;
  gives `G_generation` its first consumer; haiku-tier).
- **One overstatement not inherited:** #139's "NS3 cannot even *begin* until `scale_hierarchy §6` is authored" —
  §6 gates the *territorial-tier propagation*, not repo-legibility work (REPO_MAP/head_pointers proceed now).
  The plan binds §6 to the Territory-tier item only.

## 4 · What changed in `remediation_plan_v1.md` (this commit)

1. **"Jordan's 20-minute version" added at the top** — the ranked minimal ruling set: **D2** (accord-echo
   composition — unblocks P3's biggest wire), **D4** (structured-state — unblocks pointer closure), **D11**
   (Convictions doc — flips P2 validation), **D13** (handoff disposition), **D3** (transfer activation). Rule
   those five and every other track proceeds.
2. **The docket split into two classes.** **Class R (ratify-by-merge):** items executed in their phase PR with
   the recommendation as written; that PR's normal ED-1094 merge ratifies them (D7, D8, D9, D10, D15, D16).
   **Class E (explicit pick):** D1†, D2, D3, D4, D5, D6, D11, D12, D13, D14 — held back until picked. Jordan's
   load drops from 16 rulings to 10, of which 5 are the critical path.
3. **P5 → P5† (conditional)**, D1 → D1† (reframed: *confirm the standing Stratum-B deferral (default)* or opt
   in early), tiering Opus-first. Mermaid, sizing (~10–12 core PRs + 3 conditional), and the scorecard's
   temporal/directions rows adjusted (6/7 = the six spatial; temporal closed-by-classification).
4. **P4 tail reworded** — the two hubs grounded; the remaining 11 markers *dispositioned* (ground **or**
   classify per-module), not blanket-grounded.
5. **Three-band pointer meter** in the scorecard (21.8 / 30.9 / 47.3 → unresolved 0).
6. **Docket README errata** for the frozen pre-#139 displays.

*Net: the program's facts stand; its judgment layer is now consistent with the repo's own rulings, cheaper by
~4 PRs, and decidable in one short pass. That is what "run Fable now" was for.*
