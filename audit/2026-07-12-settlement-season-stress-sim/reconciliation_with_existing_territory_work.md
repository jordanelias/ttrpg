# Reconciliation Addendum — the stress test vs the existing territory/settlement work

## Status: FILED — 2026-07-12 · Corrects and re-weights `stress_test_synthesis_v1.md` after reviewing the pre-existing body of settlement/territory work the sim's compressed kernel omitted.

**Why this exists.** The stress test ran on a kernel distilled by extraction agents from the PR#119
docs alone. It did **not** see four large pre-existing bodies of work on exactly this subsystem. When
those are read, several of the sim's findings turn out to be **already solved, already answered, or
testing an unimplemented formula** — while a handful of **genuinely new reconciliation items** surface
that the sim was not looking for. This addendum is the honest correction. It supersedes the un-annotated
parts of `stress_test_synthesis_v1.md §6` where they conflict.

## What already existed that the sim reinvented or ignored

| Body of work | What it is | Bearing on the sim |
|---|---|---|
| **`designs/territory/goldenfurt_slice/`** | A fully-authored, adversarially-verified governance vertical slice — one real Town (S-006 Goldenfurt), 6 NPCs + 3 minor actors, a 28-card deck across all 7 families, a sim build spec, and its own 32-finding verification pass (2026-06-23). | The sim invented 7 ungrounded settlements when a canonical, collision-wired one already existed. Goldenfurt's verification **already found and fixed** several of the sim's "discoveries." |
| **`sim/territory/` (built code)** | `registry.py` (the `Settlement` dataclass), `ledger.py`, `infrastructure.py`, `adjacency.py`, `temperaments.py` — S0–S1 **built and test-covered** (6 passing tests incl. 3-settlement aggregation). | The settlement schema, ledger family set, and aggregation the sim treated as undefined are **implemented**. |
| **`tests/sim/settlement_mgmt_stress_01/`** | A prior **500-seed × 120-season executable** settlement-management stress test — 13 modules, 403 tests, a 24-probe NERS grid. | A prior stress test of the same subsystem. Its 500-seed batch **independently corroborates the sim's single strongest finding.** |
| **`designs/audit/2026-06-22-territory-settlement-audit/` + `designs/territory/{march_layer,political_hierarchy,territory_temperaments,settlement_adjacency}_v30.md`** | The baseline audit (gaps G1–G3, type-taxonomy drift) + the province/march scale layer. | Two of the sim's "gaps" are **known, ledgered** baseline gaps; two others are **testing formulas the code doesn't implement.** |

---

## A. Sim findings CORRECTED — already solved or answered in existing work

1. **Π death-spiral / "no circuit-breaker" (sim §2 Pattern B, §5) — ALREADY FIXED.** Goldenfurt's
   verification finding **CG-1** caught the mis-signed Π term and replaced it with a **bidirectional
   restoring term** `sign(3−Π)·min(1,|3−Π|)` — anti-runaway above the band *and* anti-stall below it.
   The sim's death-spiral is the *pre-CG-1* behavior. The relief valve the sim recommends authoring
   already exists in the Goldenfurt `pressure.py` spec; it simply wasn't in the kernel.

2. **Recall/demotion death-spiral + "Suspicion→Recall threshold undefined" (sim §2 Pattern A/G, §3, §6#11) —
   ALREADY FIXED for the governance-redesign recall.** Goldenfurt's **G606** ("The Bailiff's Report")
   ships a **`Submit to audit` escape (always available, −2 suspicion), a Konrad-capped-+1/season advance,
   and a `Reputation:Just`-lowers-the-Ob recall contest** — precisely the "let successes retire failure
   Keys / make the Just path sustainable" fix the sim asks for. The suspicion increment is defined
   (+1 per Defy, capped +1/season), not undefined.

3. **§3.3c Seggio "no force/seizure resolver" (sim §3 CRITICAL, §6#1) — OVERSTATED; a removal path exists.**
   `infrastructure.py` implements a **`seizure_ob_modifier`** (Chapel 0 → Cathedral −2 → Church-Governor
   −2, stacking, capped −4), and `settlement_adjacency_v30 §2` + the mass-battle layer provide **Siege/
   Assault** as the removal mechanic for an entrenched holding; Goldenfurt's G603 states removal "needs a
   **Mass Battle / Mandate Challenge**." **Residual (real):** the softer **"Mandate Challenge"** path is a
   forward reference — `political_hierarchy §2.4` mentions a "Mandate-track" but defines no challenge
   procedure. So the finding shrinks from "terminal lock, no resolver" to "the *violent* removal exists;
   the *political* Mandate-Challenge removal is genuinely unspecified." Down-tiered CRITICAL → MEDIUM.

4. **Mandate saturation masks peripheral collapse (sim §2 Pattern H, §6#8) — TESTING AN UNIMPLEMENTED FORMULA.**
   The `Mandate = round(7T/(T+6))` formula the sim stress-tested is `settlement_layer §1.8` **prose that
   the code does not implement.** The built aggregation (`registry.py`/`settlement.py`) is **floor-average
   Order** (which *does* fall when a settlement's Order collapses) + **summed Prosperity**. Peripheral
   collapse is actually carried upward by **province fracturing** (`political_hierarchy §2.3`, a
   state-machine on faction-split settlements) — not by a Mandate number. The sim's conclusion ("the real
   cross-scale carrier is Standing/tags, not Mandate") is directionally right; the concrete carriers are
   floor-avg Order + province fracturing. Also note **L/PS are inert in code** (ED-FA-0004, port-blocking) —
   so the whole L/PS→Mandate machinery the seeds leaned on is not yet wired at all.

5. **"No character attribute block" (sim §3 HIGH) — misattributed.** Attributes (Cognition/Charisma/…)
   are a **personal-scale (PC) concern**, not settlement state; the `Settlement` schema is fully defined in
   `registry.py`. The real input-completeness gap is narrower: the seed/roster spec didn't bind PC pools —
   a test-harness gap, not a canon hole.

---

## B. Sim findings CORROBORATED — independently confirmed by existing work

1. **The tragic-downfall / negative-spiral-as-default (sim §2 Pattern A, §5) — CONFIRMED by the 500-seed batch.**
   `settlement_mgmt_stress_01`'s 500-seed × 120-season run found the *same* runaway-negative regime by a
   completely different method: IP/CI/Turmoil pinned near ceiling, **near-universal faction elimination
   (mean 3.6 of 4)**, Flourishing crowded out (3.7/seed vs 659 revolts/seed), Domain Echo firing max-depth
   100% of the time. Two independent methodologies converging on "the system is biased to death-spirals" is
   the strongest single result of this whole effort — and it is **not novel to the sim**; it was already
   observable in the 2026-05-14 batch. This raises the priority of a systemic positive-feedback / recovery
   path above any single-item fix.

2. **§1.3b Bind-the-Cells actor collision (sim §1, §3 HIGH) — CONFIRMED and SHARPENED.** The real shape is
   **three conflated "actor" granularities**: (a) `§4.5 Local Actors` = a *count per settlement type* (this
   is the "1–2" figure); (b) **named NPC dossiers** — Goldenfurt carries **9**, and `registry.py`'s
   `npc_ids` is **uncapped**; (c) the **5-household population cells** Bind-the-Cells requires, which
   *no layer models*. So the collision is real, but it is not an "actor cap" — it is a **missing
   population-granularity layer**, distinct from both the §4.5 count and the named-NPC list.

3. **Territory-scale governor AP economy undefined (sim §3 HIGH, §6#6) — CONFIRMED by the baseline audit.**
   `political_hierarchy §2.5` makes governance **explicitly per-settlement** ("a faction can have different
   Governors for different territories within the same province"); no multi-settlement AP aggregation
   exists; `march_layer` is an *army* budget, not a governor's. This is consistent with baseline audit
   **G1** (no registry → province aggregation "can never fire" — since partially closed by Goldenfurt's
   `registry.py`). Real, and already on the ledger.

---

## C. NEW reconciliation items the sim was not looking for (the genuine yield for the current proposals)

These are **not in `stress_test_synthesis_v1.md`** and are the highest-value output of reading the existing
work. They bear directly on whether the PR#119 provisional items are ratifiable as written.

1. **★ Ledger-family divergence: PR#119 `Compact` vs the built `Leverage`.** The built `ledger.py`
   `TAG_KINDS = {Precedent, Grudge, Debt, Reputation, Leverage}` — and Goldenfurt uses the same five.
   **PR#119 §1.3a introduces `Compact` as "the 5th family."** The implementation's 5th is **Leverage**, not
   Compact. So §1.3a either (a) adds a **6th** family, (b) **collides** with Leverage, or (c) should reuse an
   existing family. This is unflagged anywhere and **must be reconciled before §1.3a ratifies** — otherwise
   the port has two competing "5th ledger families." *(This is the single most actionable new find.)*

2. **★ §1.0d Performance Audit likely DUPLICATES Goldenfurt's already-designed recall.** The governance
   redesign already has a **suspicion → G606 recall with a Submit-to-audit escape**. PR#119 §1.0d adds a
   *second* accountability cascade (triplicate-ledger → Waiting Order → patron review → Demotion). The sim's
   confirmed-correct NERS **MERGE** verdict on §1.0d now has a concrete **merge target**: unify §1.0d onto
   the existing suspicion/recall signal rather than standing up a parallel cascade. The two paths the sim
   flagged as "divorced" are the faction-politics audit and *this* governance-redesign recall.

3. **Two event architectures, unreconciled.** `settlement_mgmt_stress_01` uses a **predicate-sweep** event
   model (events are pure functions of settlement state, co-firing, chaining via shared state — no deck);
   `governance_play_redesign`/Goldenfurt/the PR#119 grounded deck use a **stateful card deck** (Π-weighted
   draw, cooldowns, forced queue, `seeds:` chaining). These are two different engines for "what happens to a
   settlement each season." Ratifying deck content without deciding which architecture is canonical risks
   authoring into the losing one.

4. **Two action models, unreconciled.** The 500-seed framework has **no AP economy** (discrete predicate-gated
   handlers); governance-redesign/Goldenfurt use **AP = 2 + facility_tier (+1 Seat/Cathedral)**. Same fork.

5. **PR#119's faction-standing items rest on inert substrate.** §1.0b/c/d and the §1.8 Mandate feedback all
   read **L/PS**, which are **declared-but-inert in `sim/`** (ED-FA-0004, PORT-BLOCKING). These items can be
   ratified as design prose, but they have **no implementation substrate yet** — worth stating plainly so
   "ratified" is not mistaken for "implemented."

6. **Type-taxonomy drift underlies settlement typing.** Both the baseline audit (**H3**) and the 500-seed
   framework (**F1**, the structural root of 7 findings) flag that the canonical §1.2 8 types
   (Seat/City/Town/Fortress/Port/Cathedral/Mine/Outpost) diverge from the §2.1 registry's real 11
   (adds Village/Fortress-City/Cathedral-City), so downstream modules hit fallback logic. The seeds
   silently assumed clean types; this drift is a real, cross-confirmed infrastructure gap under everything.

---

## D. Net effect on the current proposals

- **Reprioritize.** The sim's top structural finding — the **negative-death-spiral bias** — is real and now
  *doubly* confirmed (agent-narrative + 500-seed batch). It stays #1, but the fix is largely **already
  designed** (Goldenfurt CG-1 Π restore + G606 recall escape) and just needs wiring, not authoring.
- **Demote** the deck-Crisis (§0.1), §1.3c-unreachable (§0.2), and §3.3c-terminal-lock (A.3) findings — all
  overstated by the compressed kernel.
- **Elevate the NEW items** in §C — especially **Compact-vs-Leverage** (blocks §1.3a) and **§1.0d-into-recall**
  (concretizes the confirmed MERGE) — as the real, previously-unseen reconciliation work.
- **Ground future runs in Goldenfurt.** Any re-run should seed from `goldenfurt_slice` (real cast + deck) and
  the built `registry.py`, not invented settlements — and should include the existing work in-kernel so it
  stops re-deriving solved problems.

**Bottom line for the question "what is missing from your proposal":** it was missing *the awareness that this
subsystem is already partly built and previously stress-tested.* Reading that work turns roughly a third of the
sim's findings into "already solved," corroborates its biggest one, and — more valuably — surfaces the
**Compact/Leverage** and **§1.0d/recall** reconciliations that the sim, blind to the existing code, could not
have seen.
