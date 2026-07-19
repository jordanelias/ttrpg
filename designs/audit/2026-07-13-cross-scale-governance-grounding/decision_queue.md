# Decision Queue — Cross-Scale Governance (ranked `needs_jordan`)

## Status: FILED — 2026-07-13 · Lane: IN · ED-IN-0051

> **Superseded as a live surface (2026-07-15, ED-IN-0068).** The current ranked queue is
> [`designs/audit/2026-07-14-scale-chain-and-decision-surface-map/decision_queue_delta_v1.md`](../2026-07-14-scale-chain-and-decision-surface-map/decision_queue_delta_v1.md).
> The unified, always-fresh register of every open work item (this queue + the ledger +
> proposals + audit verdicts) is generated at [`tools/observability/PROPOSALS.md`](../../../tools/observability/PROPOSALS.md).
> This dated docket is retained for provenance only.

The ranked surface this docket hands to Jordan. Ordering = **leverage** (impact on the L/PS-pressure spine)
× **1/cost** × **novelty**. Classifications are the **Phase-F revised** ones (`adversarial_review_v1.md`):
**[CTC]** = COMPLETE-THE-CHAIN (execution on sound logic — mostly needs a *ruling to unblock*, not a design
call); **[GAP]** = GENUINE-GAP (a real design call, precedent-informed); **[MIX]** = mixed. Every fix is
detailed in `precedent_fix_catalog_v1.md` + `adversarial_review_v1.md`.

---

## Tier 1 — unblock the whole spine (do these first)

| # | Item | Class | The decision / action | Why it's #1 |
|---|---|---|---|---|
| **1** | **Wire L/PS (E5)** — GAP-B1 | [CTC] | Approve wiring L/PS from the *surrounding* logic (LPS-2e aggregation + `scale_hierarchy §4` consent-gate + deferred-apply boundary + Field/Gauge shape). **Do NOT import CK3.** | The single highest-priority open item in the whole governance thread (`scale_hierarchy §6`). L/PS is inert 100/100; **every** consent/fracturing/emergence arc is dark until this bites. Unblocks the most arcs per unit work. |
| **2** | **Wire `propose_transfer` + `compute_accord_echo`** — GAP-A1, A2 | [CTC] | Approve connecting the two zero-caller functions into the live season loop. | Pure wiring of built-but-uncalled code; ends the "lost territory is unrecoverable" structural defect (A1) and closes the political→spatial return path. Cheapest high-leverage fix in the set. |
| **3** | **Mandate collapse: ratify D4 + author the two relief-valves** — GAP-B2 | [GAP] (valves) + [CTC] (devolution=D4/A1/F5) | Confirm D4 (retire `round(7T/(T+K))` as collapse-carrier → floor-avg Order + fracturing + Standing Keys), and **rule the two Mandate-of-Heaven relief-valves**: (a) **scapegoat** — an appointee absorbs a legitimacy hit at the cost of *their* Standing (bend-around); (b) **self-reproach** — the ruler spends their *own* resource to arrest the slide. | Gives the L/PS spine a *downward* consequence (collapse), not just upward aggregation. The valves are the genuine, un-derivable import; the rest is D4 execution. |

## Tier 2 — the genuine new-mechanism surface (small, load-bearing)

| # | Item | Class | The decision | Precedent (verified REAL) |
|---|---|---|---|---|
| **4** | **Rank the two chain-bypass authorities** — GAP-D1 | [GAP] | Monarch + Parliament are both unconditional bypasses with **no precedence** (`scale_hierarchy §5.3`). Pick: **(a)** nest one inside the other (constitutional-monarchy / Tokugawa asymmetry), or **(b)** make Monarch-vs-Parliament collision a **named designed crisis mode**. | **Bodin** indivisible-sovereignty + war/peace diagnostic. The sharpest single finding; currently the most dangerous under-specification. |
| **5** | **Collision-of-stresses primitive + two-signal trigger** — GAP-E1, E2 | [GAP] | Approve a unified collision primitive requiring **two independently-arriving signals** (a material threshold **AND** an interpretive trigger) to resonate before it becomes a Mandate-tier event; a court social-contest scene adjudicates whether a disaster "counts." | **Mandate-of-Heaven** *zaiyi* two-channel resonance + DF mandate-clock + **Imperator Tyranny×Aggressive-Expansion** (⚠ *not* EU4 Court-and-Country — struck in Phase-F). |
| **6** | **Governance-mode FLAG taxonomy** — GAP-C2 (+ C1 split, C4 resolver) | [GAP] + [MIX] | Adopt the **8-value `governance_mode` FLAG domain** (AUTOCRATIC_FIAT / ROYAL_COURT_APPOINTMENT / OLIGARCHIC_COUNCIL / LANDHOLDER_FRANCHISE / DELIBERATIVE_ASSEMBLY / CONSENSUS_UNANIMITY / NEGOTIATED_ESTATES / MERITOCRATIC_BUREAUCRATIC), distinct from the manager-type enum; decide which are start-active vs latent. **Note:** 5/8 are corpus-native; the genuine build is sortition/consensus/negotiated + the **Consensus resolver** (3-state assent/stand-aside/holdout + antibody, C4). | Aristotle/Athens-sortition/Roman-*comitia*/consensus-polities (Haudenosaunee/Quaker/Gadaa/*shūrā*). |
| **7** | **Suppression as consequence-bearing + identity-migration** — GAP-G2 | [GAP] (taxonomy + migration) | Approve modeling cultural suppression via the **seven backfire mechanisms**, esp. the novel **identity-migration** hand-off (severe suppression converts a militarily-solvable problem into a militarily-*unsolvable* one → hands it from Conquest/mass-battle to Fieldwork/Investigation). Frame as never consequence-free. | Reconquista/*limpieza*/Morisco expulsion; Rome-vs-Jerusalem substrate-migration; ⚠ Carthage = floor-not-zero (no total erasure). ~4/7 backfires are chain-completions. |
| **8** | **Two missing resolution registers** — GAP-F6, F7 (re-homed from §3) | [GAP] | **F6 recognition-fission** — a *peaceful* negotiated-recognition insurgency-*formation* path (charter a sub-faction out of a diverged population); `insurgency_pipeline §4.1` has only a territorial-neglect trigger. **F7 reaggregation** — a Crown action that changes the allegiance *aggregation topology* (redraw the blocs), not the values. | Ottoman **millet** fission; **Cleisthenes** tribal reaggregation. Both verified REAL by the surface-analogy gate. |

## Tier 3 — rulings that unblock chain-completions

| # | Item | Class | The ruling needed |
|---|---|---|---|
| **9** | **ΔLegitimacy decay / OF-3 `decay()`** — GAP-B4 | [CTC] | Approve adding the deferred `decay()` term (mean-reversion) so legitimacy can *rot*, not only ratchet up. Precedent (Old-World cognomen-decay / EU4 Horde-Unity) is confirmatory; anacyclosis was downgraded to thematic. Enables decline-and-fall arcs. |
| **10** | **Author `engine_clock` + `domain_actions` home docs** — GAP-H3, A3 | [CTC] | Flip the two `doc:null` contracts using their already-authored homes (`propagation_spec §1` for `engine_clock`; `governance_play_redesign §1.3` for the 13 governor verbs). Unblocks the Territory tier + the governor decision-surface (the verbs that make L/PS bite). |
| **11** | **D.6 disjoint ruling + convergence proof** — GAP-A4 | [CTC] | Rule the down-`stat_deltas` / up-`aggregate` domains **disjoint** (per `propagation_spec §4.3`), enabling the contraction/termination proof. Closes the collision-oscillation risk. |
| **12** | **Cascade "hardness"** — GAP-C3 | [CTC] | Confirm the governance-type cascade is the *noisy, L/PS-gated* model `scale_hierarchy §3`/`§4` already describes (broadcast + local attenuation), **not** a hard identical-type cascade (which has no game precedent). Mostly a confirmation. |
| **13** | **Bypass metering** — GAP-D2 | [CTC] | Approve metering a chain-bypass as a new **Turmoil/IP feeder** (structurally identical to the built `Revolt +1`), drawing on the same fragility pool F5's fracture roll reads. Imperator-Tyranny is confirmatory. |

## Tier 4 — hygiene, slivers, and a flagged proposal

| # | Item | Class | Note |
|---|---|---|---|
| **14** | **Re-index the orphans + reconcile status headers** — GAP-F1, H1, H2 | [CTC] | Add `franchise_v30`, `fractional_province_ownership`, `insurgency_pipeline`, `faction_succession_split` to `CURRENT.md`; reconcile the 3 `## Status: CANONICAL`-vs-`PROVISIONAL`-body docs (H1 is 3, not 5). Pure currency-hygiene. |
| **15** | **Caste cross-scale cascade + circumvention** — GAP-F2, F4, F5, F3 | [CTC] (+F3 sliver [GAP]) | Wire caste-composition→franchise-suppression; adopt the orphaned Fragmentation-Check + Consolidation + two-stage split resolver; generalize the §2.5a wealth-buyout. **F3 genuine sliver:** the *limpieza* forged-genealogy temporal mechanic (only route lacking a corpus hook). |
| **16** | **Orthodoxy-as-nexus-axis** — GAP-G1 | [CTC] | Lift the built Church keys (CI/Piety/Excommunication) into an L/PS-parallel ideological-consent axis. |
| **17** | **"Elect-inward, account-back" propagation shape** ⚠ | [GAP], **held** | A proposed *new* armature direction (Venice Great Council→Senate→Ten). Verified REAL but **same-tier (intra-tier), not cross-scale**. Adding an armature direction is **fable/opus-gated PROPOSED-doc work** (`holonic_container_doctrine §4`) — **do not treat as ratified**; author separately if desired. |

---

**Recommended sequence:** Tier 1 (#1–3) unblocks the spine and should land first; Tier 2 (#4–8) is the
genuine design surface worth Jordan's direct calls; Tier 3 (#9–13) are rulings that free execution; Tier 4
is hygiene + one held proposal. Nothing here is executed by this docket — it indexes, classifies, and hands
off. Per CLAUDE.md §1, merging this docket's PR ratifies its *analysis* (FILED); the **fixes remain PROPOSED**
and each needs its own sign-off before authoring into canon.

---

### Addendum (Fable audit) — items to fold in

- **GAP-B3 · reconcile the three competing "faction political power" formulas** — [CTC]. franchise
  National-Influence · `political_value()` (§2.4, scalars TBD) · Mandate `round(7T/(T+K))`. Execute per **D4**'s
  ruling (one carrier). A currency/execution item, not a new design call — belongs at **Tier 3**; omitted from
  the table above, surfaced by the Fable audit.
- **GAP-B5 · rank = secession blast-radius** — [CTC, reclassified]. The disloyal actor's Standing rank sets the
  scope of what breaks away — a chain-completion of `settlement_layer §3` (the ROTK principle, cited by name) +
  `§3.2` rank→holding-scope gate + `§5.2` independence. Execution, not import. **Tier 3.**
- **Armature-binding** (Fable) — bind cross-scale claiming (`§5.2`) + chain-bypass (`§5.3`) onto an
  armature/substrate channel; currently RULED-but-unbound. [CTC]-to-author, **Tier 3**.
- **GAP-F6/F7** (millet recognition-fission / Cleisthenes reaggregation) are at **Tier 2 #8** and now also
  recorded in `gap_register_v1.md`.
