# NERS Audit — `combat_engine_v1` — RECONCILED MASTER

`[SELF-AUTHORED — bias risk]` Author built and ratified this engine (ED-900). This document **supersedes**
`ners_audit_combat_engine_v1.md` (the original audit) and folds in its adversarial critique, reconciled
against a fresh grounded investigation. Per the `<document_consolidation>` standing rule: collate →
reconcile-by-evidence → one working master. **Date:** 2026-06-04.

## WHAT THIS RECONCILES (collate)

1. **NERS audit v1** (`ners_audit_combat_engine_v1.md`) — verdict: not fully compliant; N partial-fail, R strong, S weak, E weak.
2. **Adversarial critique** of v1 (delivered inline) — charge: v1 is over-confident; ≥4 load-bearing claims rest on memory/partial checks; it fails its own "ground every claim" standard.
3. **Investigation** (this pass) — fresh reads resolving the contested claims.

`[READ: derived_stats_v30.md — Combat Pool = (Agility×2)+History+3 min5 (5–17D); Concentration = Focus×3; Stamina = (3×End)+(2×Spirit) RATIFIED S1]`
`[READ: r1_sigma_resolution.py docstring — Agi-independent pool DELIBERATE ("settled with Jordan, armature reset"); closes the Agi-dominance channel; Agi moved to the sigma-leverage channel (uniform impact); pool form labelled "Class C, NOT canonical"]`
`[READ: config.py — INIT_DECAY 0.75 / INIT_CAP 1.5 / INIT_GAIN_HIT 0.18 / INIT_LOSS_WOUNDED 0.28 / POISE_RECOVER 0.20 / POISE_FLOOR 0.5 / ATTACKER_BIAS 0.12 / UPSET_FLOOR 0.05 / OOB 2 / BURST_MAX 4]`
`[READ: r2_consequence_wounds.py + r8 WoundTracker — wound gates at interval WI; −1D/wound to Pools, NEVER Ob; felled at MW+1; overkill capped; MW cap PP-717 (End6/7→cap)]`
`[READ: combatant.py — bake() output stored to w['geo'] "for downstream wiring"; only top-level w['gap'] overridden/consumed]`
`[READ: core.py — RESIST/DELIVERY mode tables (blunt/point/cut × armour) drive the armour rotation, NOT the baked coeffs]`
`[READ: tradition.py + wrapper.py + systems.py — channel_weight() wired live at ~7 sites (initiative/reading/counter/poise-break/foot-measure); eff_cw() defined but unused (call sites still use channel_weight) → channel-ability levers inert "next pass"; ability_factor() live for counter_select]`
`[CONFIDENCE: high on the canon formulas, loop constants, wound model, and the staged-scaffolding reframe — all freshly read; medium on cross-system Smoothness (siblings not read this pass)]`

---

## RECONCILIATION LEDGER (the heart)

| # | v1 claim | Critique said | Investigation evidence | **Resolution** |
|---|---|---|---|---|
| 1 | **[S] Pool deviates from canon PP-615 `Agi×2+Hist+3`** (ranked #1, then called "not a defect") | "#1's anchor cited from memory; possibly ungrounded; and ranking a non-defect #1 is incoherent" | Canon **verified**: `(Agi×2)+History+3, min5` (derived_stats). Engine = `max(5,Hist+6)`, Agi-independent — **deliberate, "settled with Jordan"** (r1 docstring), to close the Agi-dominance channel. **But** r1 still labels the new pool "Class C, NOT canonical," and derived_stats still carries the OLD formula. | **SHARPENED → real defect.** Not "non-defect" (v1 wrong) and not "ungrounded" (critique resolved). The true defect is **un-propagated ratification**: ED-900 made the engine canonical but left canon-of-record (derived_stats Combat Pool) and the engine's own provenance label contradicting it. **Fixable by canon edit, not engine change.** This is now the #1 actionable finding. |
| 2 | **[N/E · medium] 4/5 baked geometry coefficients dead; engine over-engineered** | "'Verified' is overclaimed — the grep used one narrow pattern" | Definitive trace: `bake()` → `w['geo']` **"for downstream wiring"**; the armour rotation runs on core.py's own RESIST/DELIVERY mode tables, not the baked coeffs. So `thrust/cut/perc_conc/halfsword` **are** unconsumed — but **explicitly staged**, zero runtime cost (baked at import). Same for tradition channel-ability levers (eff_cw defined, call sites still use channel_weight → inert "next pass"). | **CONFIRMED-IN-SUBSTANCE but DOWNGRADED + REFRAMED.** The coefficients/levers are unconsumed (v1 right), but they are **deliberately staged scaffolding for documented planned wiring**, not accidental over-engineering (v1's "accidental" framing wrong; critique's "grep inadequate" right). Severity **medium → low**. Only `can_halfsword_thrust` is truly orphaned. |
| 3 | **[S · medium] Concentration `3·focus+spirit` ≠ canon §5.2 `Focus×3` — "NOT intended"** | (not specifically challenged) | Canon **verified** = `Focus×3` (derived_stats §5.2). Engine **adds** a `+spirit` term. No evidence found that the addition was deliberate-and-recorded. | **CONFIRMED, intent softened.** Real divergence (engine adds spirit). "NOT intended" overstates my knowledge → restate as **"divergence; intent unrecorded — either propagate the +spirit into canon or remove it."** |
| 4 | **[R] Robust STRONG; loops bounded** | "Asserted from memory; loop stability argued statically, not stress-proven" | Constants **freshly verified** (INIT_DECAY 0.75, INIT_CAP 1.5, POISE_RECOVER 0.20, POISE_FLOOR 0.5, UPSET_FLOOR 0.05). Matches v1. | **CONFIRMED + GROUNDED.** Robust STRONG stands, now on fresh reads. (Static argument noted as a residual — a dynamic loop-stress would fully close it; prior session battery showed no runaway.) |
| 5 | **Phase 4 loop enumeration** (initiative / poise / fatigue) | (not raised) | WoundTracker: −1D/wound to Pools **+** INIT_LOSS_WOUNDED 0.28 → a **wound → smaller pool + lost Vor → more hits → more wounds** loop the v1 audit **did not list**. | **NEW FINDING (completeness gap in v1).** The loop is **undamped within a fight** (wounds don't heal mid-fight) but **bounded** (felled at MW+1; pool penalty and Vor both capped). Per Lesson 5 (defect = undamped *and* unbounded) it **passes** — and the bound (felling) is the *intended* combat terminal (a wounded fighter should be losing; contrast faction collapse, where such a spiral is a defect). Adequate; should be on the record. |
| 6 | **[Phase 3b GAP] wound model not traced** | "Honesty about a gap ≠ closing it; load-bearing for R/S" | WoundTracker **read**: damage → wound gates at fixed interval WI; **−1D/wound, never Ob**; felled at MW+1; overkill capped. | **GAP CLOSED → strengthens R/S.** Health degrades via an **intended, uniform (−1D/wound), bounded** discrete-accumulator clock. No accidental cliff; uniform impact (Lesson 2 satisfied); bounded. NERS-clean. |
| 7 | **Necessary PARTIAL FAIL** (basis: dead apparatus + focus/spirit) | "Category error — focus/spirit are 'not redundant' by your own admission; weak ≠ unnecessary; padding" | Per #2: the "dead apparatus" is staged scaffolding, not redundant. focus/spirit clear 50 (effect, not redundant). | **OVERTURNED → upgrade to Necessary PASS (with notes).** v1 over-penalised N. Nothing in the engine is *redundant*; the only N/E cost is carried staged scaffolding (minor). |
| 8 | **"Compliant by orthogonality"** (P-/GD- constraints) | "Asserted, not demonstrated; engine has `spirit`; P-01/P-11/P-10 could bind if combat touches Threadwork" | Not re-investigated this pass (combat's metaphysical surface unread). | **OPEN — narrowed.** Restate as **"no applicable P-/GD- constraint found for ordinary embodied combat; thread-touching combat paths (if any) NOT checked."** Honest scope, not a green check. |
| 9 | `ATTACKER_BIAS` unexamined (critique scope-gap) | "A flat attacker advantage — over-rewarding first-mover?" | `ATTACKER_BIAS=0.12` confirmed; applied to the per-beat aggressor; symmetric over alternating exchanges (mirror = 49–50 holds). | **ADDRESSED — benign.** A small, bounded attacker-tempo term; symmetric over a fight; does not break the mirror. Not a defect. |
| 10 | `equipped`/`skills` unexamined (critique scope-gap) | "Never looked at them" | `equipped` wired (combatant/systems/tradition); `ability_factor` live for counter_select; `skills` minimal (combatant only). | **ADDRESSED.** Partially wired; the inert part is specifically the **channel-ability** levers (pending the eff_cw pass) — same staged-scaffolding bucket as #2. |
| 11 | σ-term sensitivity (critique scope-gap) | "v1 asserts each of ~20 terms is load-bearing without a term-level check" | Not done this pass. | **OPEN — honest gap.** A term-zeroing sensitivity study is the remaining deep analysis; not faked here. |
| 12 | Cross-system Smoothness ("inconsistent with dice-pool siblings") | "Built on the skill's *unvalidated* sibling hypotheses, not reads" | Only the **combat** pool canon verified; social/mass-battle resolution NOT read. | **SCOPED DOWN.** Restate the S finding as **"deviates from the canonical *Combat* pool (verified); broader sibling consistency not assessed."** |

`[CORRECTION: mid-investigation #1 — I told you "the dead-apparatus headline is likely wrong" on the strength of a substring grep. The definitive trace shows that grep was misleading (those `cut`/`thrust` hits are a separate mode-logic system). v1's finding #2 is substantively correct (the baked coeffs are unconsumed); the real correction is the *reframe* to staged-scaffolding, not an overturn.]`

---

## REVISED NERS VERDICT (post-reconciliation)

**Necessary — PASS (with notes).** *Upgraded from PARTIAL FAIL.* Nothing in the engine is redundant. The
resolution spine, σ-hub, bounded loops, reach/tempo/measure primitives, armour-mode rotation, and wound
clock all carry differentiated behaviour. The only N/E cost is **deliberately staged scaffolding** (the
baked `w['geo']` surface beyond `gap`, and the channel-ability levers awaiting the `eff_cw` pass) — carried
weight that does nothing yet but is documented planned work, at zero runtime cost. Note, not failure.

**Robust — STRONG (grounded).** Constants freshly verified. Every loop is damped+bounded **or**
undamped-but-bounded-by-the-intended-terminal: initiative (decay 0.75 + cap ±1.5), poise (recover 0.20 +
floor 0.5), fatigue (inter-turn recovery + burst cap + collapse), and the **newly-enumerated wound→pool→wound
spiral** (bounded by felling at MW+1, capped pool penalty, capped Vor-loss). The wound clock is uniform and
bounded. No one-shot (max hit 18 < health 40), 95% cap, moderate pools 6–12D. Residual: the `oob` step at
stamina 0 (a minor accidental cliff atop the smooth ramp); the loop-stability case is argued from constants,
not freshly stress-proven.

**Smooth — WEAK (sharpened; the fix is canon-side).** The real Smoothness defect is **un-propagated
ratification**: ED-900 made the engine canonical, but derived_stats still states the old Combat Pool
(`Agi×2+Hist+3`) and Concentration (`Focus×3`), and the engine's own r1 docstring still labels its pool
"Class C, NOT canonical." Canon-of-record therefore **contradicts the ratified engine** on two derived
quantities. Both are deliberate engine choices; the gap is that the ratification didn't carry the canon
edits. (Cross-system consistency with social/mass-battle was not assessed — see #12.)

**Elegant — WEAK→MODERATE (upgraded).** The staged scaffolding is a minor, intentional cost (not the
over-engineering v1 implied). The genuine Elegance items are the **~100+ Class-C constant count** (real
tuning/cognitive overhead, partly mitigated as invisible engine logic) and the **`disp`/Disposition naming
collision** (two concepts, one name — Jordan-kept, but confusing). The σ-hub itself is defensible.

---

## POST-RECONCILIATION FINDINGS (severity-ranked)

1. **[S · high · actionable] Un-propagated ratification.** Update `derived_stats_v30` Combat Pool + Concentration to match the ratified engine (or record the deviations as intentional), and relabel r1's pool form Class-A/canonical post-ED-900. *This is the one finding that became sharper, and it implicates the ratification itself.*
2. **[S · medium] Concentration `3·focus+spirit` vs canon `Focus×3`** — reconcile in one direction (subset of #1).
3. **[R · low] `oob` step-cliff** at stamina 0 — ramp it.
4. **[E/N · low] Staged scaffolding** (geometry `w['geo']` surface + channel-ability levers + the orphaned `can_halfsword_thrust`) — complete the wiring passes or prune if deferred.
5. **[R · low] Disposition aggression-tilt vs documented intent** (`disp1→7 = 47→54`) — `[INTENT UNDETERMINED]`, Jordan's call (carried from v1, empirically grounded, unchanged).
6. **[E · low] `disp`/Disposition naming collision** — Jordan-kept; standing confusion.
7. **[balance · Jordan] tradition spread** (german 52 ↔ spanish/chinese/filipino 60 vs none) and **focus/spirit per-point weakness** — design-intent calls (unchanged from v1).

**Open honest gaps (not closed this pass):** σ-term sensitivity study (#11); thread-touching combat
constraint check (#8); cross-system Smoothness vs social/mass-battle (#12).

---

## RECOMMENDATIONS (updated)

1. **Propagate the ratification (do first).** Edit `derived_stats_v30` so the canonical Combat Pool and
   Concentration match the ratified engine (or add an explicit "engine supersedes; deviation intentional"
   note + ledger entry), and flip r1's "Class C, NOT canonical" pool label to canonical. Closes the #1
   defect. *This is a canon edit — Jordan's structural call on whether canon adopts the engine's forms or
   records them as deviations.*
2. **Decide the scaffolding.** Either schedule the geometry-coefficient + `eff_cw` channel-lever wiring,
   or prune the unused bake/levers to restore Elegance. Removal is now genuinely low-risk (the resolution
   uses core.py's mode tables + `w['gap']`, not the staged surface — verified).
3. **Ramp the `oob` penalty** toward stamina 0 instead of a step (small, low-risk).
4. **Design-intent calls (Jordan):** disposition tradeoff-vs-reward; tradition parity; focus/spirit weight.
5. **If you want full closure:** run the σ-term sensitivity study and read the sibling resolvers before
   asserting cross-system (in)consistency.

---

## BOTTOM LINE

Reconciled against evidence, `combat_engine_v1` is in **better NERS shape than the original audit
concluded**. The investigation **upgraded Necessary to PASS** (the "dead apparatus" is deliberately staged,
not redundant), **strengthened Robust** (wound model is a clean bounded clock; loop constants verified;
one missed loop added and shown adequate), and **left Elegant only mildly weak**. The one finding that got
*sharper* is **Smoothness via un-propagated ratification** — and that is a consequence of the ED-900
ratification I performed, not an engine flaw: canon-of-record was never updated to match the engine it
declared canonical. The single highest-value action is the canon-propagation in Recommendation 1.

*This reconciled master is the working audit going forward; `ners_audit_combat_engine_v1.md` is superseded.*
