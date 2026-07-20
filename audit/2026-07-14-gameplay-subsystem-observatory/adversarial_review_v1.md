# Adversarial Review + Directional Verification (v1)

## Status: FILED — 2026-07-14 · ED-IN-0064

Two independent read-only gates ran against the synthesis (`subsystem_synthesis_v1.md`) and gap register
(`gap_register_v1.md`), each a relay (the critic saw the *output*, not the synthesizer's reasoning; both had
read-only intent). This file is the **authoritative correction layer** — where it conflicts with the synthesis or
register, this file wins, and the per-file top banners point here.

---

## Gate 1 — Adversarial critic (refute-by-default). Verdict: **SOUND-WITH-FIXES**

The instrument faithfully reports the machine ground truth (every count + citation spot-checked resolves),
correctly screens the ED-MB-0010 fabrication, and `scale_transitions §12` fully supports the seam classification.
**No fabricated numbers.** Confirmed: 9 doc:null (raw grep 10 counts one prose string, not a field), 13
`[ASSUMPTION]` (raw grep 14 counts the header comment), in-13/in-12 hubs, 52.7 % pointer, validation FAILED 1/3
(p1 54.75<89.5, p2 cv 999), 4 dangling-emits, cross-scale-fraction 0.512, "20 !A6 type-edges" (= 20 per-type tags
on 9 mermaid module-pair edges; the red overlay's "19" is the top-down-only subset). ED-MB-0010 exists
(`canon/editorial_ledger_mb.jsonl:10`) and exactly describes the fabrication.

**Two reclassifications applied (GENUINE → COMPLETE-THE-CHAIN):**

1. **GAP-F1 `MS`-owner.** The gap is real *at the contract layer* (no `module_contracts.yaml` module declares MS
   ownership — confirmed; `peninsular_strain`'s contract state lists only Turmoil/IP). But the fix is **fully
   determined by existing built logic**, so it is CTC, not GENUINE — no imported precedent is needed:
   - `params/core.md` §MS Baseline Decay (**PP-255**): canonical MS mechanic (−1/in-game-year, floor 0, ceil 100).
   - `sim/peninsular/ms_track.py` **writes** `world.clocks['MS']` (`apply_ms_baseline_decay`).
   - `sim/peninsular/accounting.py` **wires** it into the Year-End cascade — **MS is already ticked in the sim**,
     on the peninsular spine.
   - `designs/world/ms_trajectory_v1.md` is a dedicated MS design doc; a prior audit already drafted the exact
     contract fix (`env.ms_delta` + a `substrate_state`/peninsular module owning MS at Accounting).
   - *Self-disconfirming evidence the synthesis had in hand:* it cites `sim.peninsular.ms_track` in
     `peninsular_strain`'s "Shape" but never connected it to GAP-F1. **Fix: wire the existing decay into a contract
     owner** — mechanical, not a design invention.

2. **engine_clock (GAP-A3 GENUINE sub-case) → CTC.** `designs/architecture/propagation_spec_v1.md` is **CANONICAL
   (ratified 2026-07-02)**; its **§O.2 is titled "engine_clock module contract (retires doc:null/[ASSUMPTION])"**
   with §1 formalizing ordering/determinism grounded in the already-implemented `season.py`/`accounting.py`. The
   home doc exists, is canonical, carries a drafted contract; only the `module_contracts.yaml` pointer-flip pends
   **ED-1051** (administrative). CTC. *Nuance:* propagation_spec itself flags the tick-scoped scheduler /
   `cascade_depth` as "genuinely new apparatus" — a sliver is new, but the temporal-spine core is ruled canon,
   already coded.

**Softer flags (confidence overstated, not hard-reclassified):**
- **GAP-A1 `domain_actions` home** — defensible GENUINE but **leans CTC**: `ED-FA-0002` says the playable verbs
  already exist, *fragmented* across `params/bg/core.md`, `params/bg/faction_actions.md`, and the faction_layer
  resolver math. Authoring the home = **consolidation of existing canon** + the (genuinely new) strategic-turn
  *structure*. Kept GENUINE-leaning-CTC.
- **GAP-C4 `env.crisis` consumer** — appropriately hedged; **leans CTC**: `peninsular_strain_v30 §2.6` defines
  Crisis/Collapse as settlement Order/Accord penalties → points at `settlement_layer` as the *determined*
  consumer. The "candidate" hedge stands.

**Minor slip corrected:** the synthesis dated ED-IN-0016 "2026-07-08"; the ledger entry is **2026-07-05**.

**Net effect on the thesis:** *strengthened.* "The missing architecture is overwhelmingly unbuilt wiring on sound
logic" is *more* true — MS and engine_clock are more CTC than first claimed. The true GENUINE-mechanism surface is
**at most `domain_actions` (leaning CTC) + `env.crisis` (hedged)** — not four items.

---

## Gate 2 — Six-directional coverage ("double check in all directions"). Verdict: **partially correct, materially incomplete as stated**

The `!A6`-as-annotation-debt claim is **correct for the two DOWN directions** the synthesis enumerates (top-down,
down-diagonal): the substrate mechanism (`Target` + `stat_deltas` + `scale_signature` + deferred apply) genuinely
exists and is *exercised* by `echo_transport`; the 8 §12.4 seams are real sparse-`targets[]` debt. **But the "all
six directions" framing hid genuine execution gaps the seam count does not touch.**

### Directional matrix (16 subsystems × 6 directions)
COVERED = wired/live · A-DEBT = `!A6`/sparse-targets/uncalled (exemption class) · ABSENT = no edge · the zero-Key
trio is ABSENT in every direction.

| Subsystem | bottom-up | lateral | vertical-up | diagonal | top-down | down-diag |
|---|---|---|---|---|---|---|
| personal_combat | A-DEBT | COVERED | A-DEBT | ABSENT | COVERED | ABSENT |
| social_contest | COVERED | COVERED | COVERED-decl | ABSENT | ABSENT | ABSENT |
| mass_battle | COVERED | COVERED | COVERED-decl | ABSENT | ABSENT | ABSENT |
| threadwork | A-DEBT | COVERED | A-DEBT | **A-DEBT** | ABSENT | ABSENT |
| fieldwork_knots | COVERED | COVERED | COVERED-decl | ABSENT | ABSENT | ABSENT |
| domain_actions | ABSENT | COVERED | ABSENT | ABSENT | A-DEBT | A-DEBT |
| faction_state | ABSENT | COVERED | ABSENT | ABSENT | COVERED | COVERED |
| faction_politics | ABSENT | COVERED | ABSENT | ABSENT | A-DEBT | A-DEBT |
| ci_political | ABSENT | **ABSENT** | ABSENT | ABSENT | ABSENT | ABSENT |
| territorial_piety | ABSENT | **ABSENT** | ABSENT | ABSENT | ABSENT | ABSENT |
| settlement_layer | COVERED | COVERED | COVERED | ABSENT | A-DEBT | A-DEBT/COV |
| peninsular_strain | ABSENT | ABSENT | ABSENT | ABSENT | COVERED+A-DEBT | A-DEBT |
| npc_behavior | COVERED | COVERED | COVERED | ABSENT | COVERED | COVERED |
| piety_track | COVERED | COVERED | COVERED | ABSENT | A-DEBT | A-DEBT |
| miraculous_event | COVERED | COVERED | COVERED | ABSENT | COVERED | ABSENT |
| victory | ABSENT | **ABSENT** | ABSENT | ABSENT | ABSENT | ABSENT |

### Seam reconciliation — 8 of 9 machine `!A6` seams == §12.4 exactly
The 9th, **`scene_slate → piety_track`**, is **NOT in §12.4** and is a **scale-signature mislabel, not a genuine
down-seam**: the four types (`scene.dialogue/insult/threat/witness`) carry `default_scale_signature: [personal]`
and `piety_track` is `[personal]` — no cross-band delivery occurs. The identical bundle `scene_slate → npc_behavior`
is drawn *solid* precisely because `npc_behavior` declares `scales:[personal,scene]` while `piety_track` omits
`scene`. **Fix = scale-vocabulary reconciliation (WS2) / add `scene` to piety_track's `scales:`**, not `targets[]`
population. The "20 / 19 / 15" published counts all reconcile as the same set sliced three ways.

### GENUINE directional gaps (uncalled/deferred — beyond annotation-debt) — NEW findings
- **GAP-DIR-1 · DIAGONAL has zero executable instances.** `causes[]` is the diagonal channel (§12.1); the
  substrate *supports* it (`sim/substrate/keys.py`) but **no emit site in `sim/` ever populates it** (grep `causes=`
  across `sim/**` finds only the def/serialize/validate in keys.py). The named exemplar §5.6 Thread Echo
  (`domain_echo.compute_thread_echo`) has **zero callers**. The armature concedes it verbatim: *"The diagonal
  direction has zero executable or exemplified instances"* (`key_echo_armature_v1.md:41`). Stronger than
  annotation-debt — the direction is **unreached**, not sparsely-targeted.
- **GAP-DIR-2 · bottom-up Accord echo (§5.5) built-but-uncalled.** `domain_echo.compute_accord_echo` has **zero
  callers**; `echo_transport` invokes only `compute_domain_echo`. **Reproduces governance GAP-A2.** (A live *static*
  Accord recompute stands in; the event-driven echo is dead.)
- **GAP-DIR-3 · distribute-down territory transfer built-but-uncalled.** `parliamentary_transfer.propose_transfer`
  has **no live caller**; `parliamentary_bridge` wires the Mandate-penalty vote, not the transfer resolver.
  **Reproduces governance GAP-A1.**
- **GAP-DIR-4 · §3 handoff dispatcher orphaned; §3.3 an empty stub.** `handoff_rules.py` implements all eight
  handoffs but is an **import-orphan** (no live caller); **§3.3 Personal→Scene is an empty canon stub**
  (`scale_transitions_v30.md:51` header, no body).
- **GAP-DIR-5 · temporal (the 7th direction) `decay()` un-shipped.** The armature lists a 7th **temporal**
  direction (§2.6). Cadence/ordering is partially wired (`TickScheduler`, `accounting_boundary`); the general
  **`decay()` term is an explicit deferral** ("substrate ships WITHOUT decay… deferred to Stratum B+",
  `key_echo_armature_v1.md`). **Reproduces governance GAP-B4/A4** (ΔLegitimacy no-decay; cross-tick convergence
  unproven).

### Up-direction verdict
- **Domain Echo §5.2 core: WIRED + CALLED.** `ECHO_TRANSPORT` is **default ON** (mc_v18, Jordan 2026-07-08,
  *post-dating* the 2026-07-13 docket). Caveat: the live firing path is the **faction-scale** parliamentary vote +
  **synthetic** emergency-council (parties from aggregate faction stats); the **true personal-actor→faction** path
  still **defers** on the context-derivation bridge (`scene_dispatch` — "combat, and any future contest… defer").
- §5.5 Accord / §5.6 Thread echo: **DOCTRINE-ONLY** (uncalled). The 8 handoffs: **DOCTRINE-ONLY dispatcher** (orphaned).

### Bottom line
Only **lateral** and the **bottom-up Domain-Echo core (§5.2)** are genuinely live end-to-end. Everything else is
either **annotation-debt** (the down-seams — correctly), **doctrine-only** (diagonal, handoff dispatcher,
Accord/Thread echo), or a **ruled deferral** (temporal decay). The synthesis's directional claim was too generous:
it is corrected in `subsystem_synthesis_v1.md` §8 (Directional coverage) and the five GAP-DIR entries are added to
`gap_register_v1.md` category D.

---

## Reconciliation applied to the synthesis + register
1. GAP-F1 (MS) and engine_clock (GAP-A3) → **COMPLETE-THE-CHAIN** (with the existing-code evidence above).
2. Summary/§5 "genuine-mechanism surface" revised: the true GENUINE surface is `domain_actions` (leaning CTC) +
   `env.crisis` (hedged) + the **directional** genuine gaps (GAP-DIR-1 diagonal-unreached, GAP-DIR-5 temporal-decay),
   which are uncalled/deferred rather than sparse-targets.
3. New **§8 Directional coverage** + a directional Mermaid cut added to the synthesis; **GAP-DIR-1..5** added to the
   register; the 9th seam reclassified as a scale mislabel (not a down-seam).
4. ED-IN-0016 date corrected to 2026-07-05.
5. All still HELD-BACK (ED-1094); still leads-not-verdicts (L0 gate FAILED 1/3).
