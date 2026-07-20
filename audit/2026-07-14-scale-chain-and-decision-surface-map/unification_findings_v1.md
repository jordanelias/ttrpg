# Holistic Unification — Cross-Artifact Adversarial Findings (v1)

## Status: FILED (holistic adversarial review) — 2026-07-14 · Lane: IN · ED-IN-0064

**What this is.** A refute-by-default antagonist pass over the *whole* governance deliverable set —
not within any single document, but ACROSS the three corpora — surfacing inconsistencies,
broken research→gameplay through-lines, and Mandate-of-Heaven adjacency that appear only when
A (research), B (vector audit), and C (chain/gap docket) are read together.

**Corpora reviewed.**
- **A — Research corpus:** `research/governance/{governance_modes, political_hierarchy_standing,
  conflicts_power_struggles}.md` (synthesis + consolidated design-hooks tables + per-civ hooks).
- **B — Vector audit:** `designs/audit/2026-07-14-governance-vector-audit/{02_weakness_register,
  structure_register}.md`.
- **C — Chain/gap docket:** `chain_map_v1`, `decision_surface_census_v1`,
  `churn_event_opportunity_map_v1`, `gap_register_v2`, `decision_queue_delta_v1`,
  `adversarial_review_v1` (all in this directory).

**Relationship to `adversarial_review_v1.md` (de-confliction — read this first).** That file is the
**per-artifact / corpus-C-internal** antagonist: it re-checked every C edge classification and count
against the `sim/` working tree and rendered SOUND_WITH_FIXES, with six findings (F-1 H2
"unconditional" overstatement; F-2 caller-count 5→4 self-contradiction; F-3 invariant-7 miscitation,
plus the fact that `keys.py:355-359` enforces the enum in code; F-4 recusatio/anacyclosis grounding
thinness; F-5 the ~4-5 bar; F-6 governor ~11-13 double-count). **This pass does not re-litigate any of
those.** Its charter is the seams *between* the corpora that a single-corpus pass structurally could
not see: research hooks that never reach the hand-off (A→C), census fills mis-sourced to the corpus
(C→A), vector-audit confidence caveats that don't travel into the docket (B→C), and one WIRED-status
contradiction *between two C files* that the per-artifact pass treated as five separate documents
rather than cross-checking against each other. Where a finding below touches something the review
already saw, that is stated explicitly and only the cross-artifact increment is claimed.

**Method.** Every load-bearing cross-corpus claim was re-checked against the working tree
(`key_substrate_v30.md` lines 57/122/447 read; `sim/` grepped for L/PS and scale usage; each research
citation in the census/queue grepped in `research/governance/`). Quotes below are verbatim.

**Headline.** The deliverable set is, as `adversarial_review_v1` found, unusually well-evidenced and
MoH-clean at the mechanic level. But the *unification* is weaker than any single artifact: **the
research→gameplay through-line is broken at four named hooks** (the user's core requirement), **two
C files give opposite ground-truth verdicts on the two most load-bearing edges**, **one census fill
is sourced to a research precedent the corpus does not contain**, and **the one center→periphery
legitimacy flow in the whole system is grounded on a loose analogy the corpus's own Roman verifier
warns against.** None is fatal; all are correctable in place before the DESIGN pass binds on the set
as a unified whole. Overall: **UNIFIES_WITH_FIXES.**

---

## Ranked cross-artifact defects

### X-1 · [contradiction · C↔C · HIGH] `churn_map` reports Mandate aggregation and cross-scale stamping as "verified WIRED"; `chain_map`/`gap_register` class the same two edges SPEC-ONLY / BROKEN.

**Artifacts.** `churn_event_opportunity_map_v1.md §2` vs `chain_map_v1.md §3` + `gap_register_v2.md
§0/§2` (all corpus C, all filed 2026-07-14 under ED-IN-0064).

**The conflict, quoted.**
- `churn_map §2 (EXISTS)`: *"**Mandate aggregation, already canon**: `settlement_layer §1.5` —
  Mandate = Σ settlement L/PS … Both **verified WIRED** in the ripple substrate's own self-audit
  (§13/§14.1)."* and *"**`scale_signature` on every Key**: `key_substrate_v30.md` §2.1 already stamps
  every state-change with `[personal | settlement | territory | peninsula]` … **verified WIRED
  (§13)**."*
- `chain_map §3` (same-day sibling): *"Settlement → Mandate → faction (§7) | §13 canon grade WIRED |
  **Sim-reality grade: SPEC-ONLY** | L/PS dead in `sim/` (`lps_inert_check` 100/100 red)"* and
  *"Cross-scale stamping (§7) | WIRED | **BROKEN above territory** … Scene echoes hardcode
  `["personal"]`."*
- `gap_register_v2 §2`: V3 **SPEC-ONLY**, NG-1 **BROKEN**.

**Why it's a cross-artifact defect (not caught by the per-artifact review).** The whole thesis of
`chain_map` is *"Canon-WIRED ≠ sim-WIRED — the synthesis table tracks both columns because they
disagree on 4 of 8 edges"* (§0.5). The `churn_map` inherits `governance_ripple_substrate §13`'s
canon-grade **without that correction** and files the two flagship gaps under **EXISTS**. A reader who
picks up the churn map alone concludes Mandate aggregation and cross-scale stamping already run;
the chain map and gap register headline them as the docket's two single biggest gaps (gap-ledger
ranks 1 and 2). `adversarial_review_v1` confirmed the chain-map side is *true* (L/PS 100/100 inert;
echo hardcodes `["personal"]`) but, scoping each C file independently, never flagged that the churn
map asserts the opposite. This is the sharpest "claim in one doc refuted by another" in the set.

**Reconciliation (one line).** Add a sim-reality column to `churn_map §2` and re-grade its two
"verified WIRED" EXISTS entries to **canon-WIRED / sim-INERT**, cross-citing `chain_map §3` — or
demote them from EXISTS to the GAP column, since by the set's own ground truth they are the two
biggest gaps, not accomplished plumbing.

---

### X-2 · [through-line break · A→C · HIGH] Four load-bearing research design-hooks are orphaned — present in corpus A, absent from every actionable C hand-off (gap register / decision queue / census).

**Artifacts.** `research/governance/{conflicts_power_struggles, governance_modes,
political_hierarchy_standing}.md` (hooks) vs `gap_register_v2.md` + `decision_queue_delta_v1.md` +
`decision_surface_census_v1.md`. This is the user's core requirement — "research informs gameplay,
edge by edge" — audited in the orphaned direction. Confirmed by grep: none of the following tokens
(`perpetuo`, `Ides`, `permanent-grant`, `dormant-but-live`, `Tetrarchy`, `impersonal charter`) appears
anywhere in the five actionable docket files (`Tetrarchy` appears **only** in `adversarial_review_v1`
prose, never as a gap/queue/census item).

**The orphaned hooks, quoted from A.**
1. **Permanent-grant / recall-cap removal as a distinguishable collision-trigger event type** —
   `conflicts §3` (Caesar *dictator perpetuo* → Ides) + hooks-table row: *"permanent-grant transition
   is a distinguishable event type … fires a collision check among the highest OLIGARCHIC_COUNCIL
   seats."* A vivid, buildable state-transition hook — dropped entirely.
2. **Dormant-but-live Crown consent-gate that never zeroes under eclipse** — `governance_modes`
   hooks-table row "Two co-resident authority tracks … dormant-but-live Crown," grounded explicitly
   **non-MoH** (*"Roman Senate reassertion"*). Absent from the decision queue's chain-bypass item (#4).
3. **Bind enforcement-layer loyalty to an impersonal charter-Key, never a seat-holder** — `conflicts
   §7` (Tetrarchy collapse) hooks-table row: *"gate army/enforcement loyalty to an impersonal
   charter-Key … or the structure reproduces single-claimant collapse."* This is doubly load-bearing
   because `governance_modes §4` **proposes the tetrarchy mechanism as a player-chosen anti-secession
   mitigation** — so corpus A carries the mechanism-to-offer but its documented failure-guard never
   reaches the hand-off. Offering the multi-seat power-share without its guard is a design landmine.
4. **Reaggregation can *add a new seat* rather than reverse** — `political_hierarchy_standing` hooks
   row (Palatinate 1623 *added* an Electoral seat). Only generic `rank = secession-blast-radius` is
   carried; the "adds-a-seat" resolution nuance is lost.

**Why it matters.** The docket's re-grounding pass (`gap_register §7`, `decision_queue §C`) *did*
harvest many `conflicts` hooks (Gracchi, Year of Four Emperors, Janissary+fatwa, 887-888, Venetian
ladder, recusatio, recognition-fission), so this is not wholesale neglect — it is four specific,
high-value, buildable hooks left on the table by the very pass that ingested the corpus. Each is a
live design lever the DESIGN pass will not see because it exists only in A.

**Reconciliation (one line).** Add a "harvested vs. deferred research hooks" ledger to
`decision_queue_delta` (or a Tier-2 collision/succession sub-item) that either absorbs these four or
records them as consciously deferred, so no live hook silently dies between corpus A and the hand-off.

---

### X-3 · [ungrounded fill · C→A · MEDIUM-HIGH] The census's bureaucrat menu cites a research precedent the corpus does not contain (Zhang Juzheng / *kaochengfa*).

**Artifacts.** `decision_surface_census_v1.md §2(d)` vs `research/governance/
political_hierarchy_standing.md`.

**The claim, quoted.** Census §2(d): *"**Zhang Juzheng's *kaochengfa* triplicate task-ledger**
(`political_hierarchy_standing.md` §1.0d precedent, already partly captured as `faction_politics_v30.md`
§1.0d *Patron-Sponsored Performance Audit*)."* The bureaucrat is the role the census calls *"the
research corpus's strongest suit,"* and this is one of its four grounding pillars.

**What the corpus contains.** Grep for `Zhang Juzheng|kaochengfa|Ming|Qing` across
`research/governance/` returns **zero hits in `political_hierarchy_standing.md`** (and none anywhere
except an unrelated `governance_modes.md` line). The corpus header is explicit — *"Covers 8
civilizations … Han/Three-Kingdoms China"* — and there is **no §1.0d** in that file (that is a
`faction_politics_v30` numbering scheme). *Kaochengfa* (1570s) and Zhang Juzheng are **Ming**, outside
the corpus's declared scope. The corpus's *actual* in-scope bureaucrat-audit precedents are Han **cha
ju** (`political_hierarchy_standing.md:411-416`; `governance_modes §1.5-1.6`), Roman *repetundae*,
Carolingian *missi*, Roman *transvectio* — all real, all correctly cited elsewhere in the same menu.

**Why it matters.** This is exactly the task-flagged defect "a census fill that cites no [valid]
research precedent." The fill is legitimately backed by a *design doc* (`faction_politics_v30 §1.0d`),
but attributing it to the *research corpus* fabricates a research→gameplay through-line that does not
exist — undercutting the census's own claim that the bureaucrat is corpus-grounded.

**Reconciliation (one line).** Drop the `political_hierarchy_standing.md` attribution for *kaochengfa*
(cite `faction_politics_v30 §1.0d` only), or swap the pillar to the in-corpus **cha ju** /
*repetundae* resolution-quality precedent the corpus actually supplies.

---

### X-4 · [MoH adjacency + surface-analogy · A↔C · MEDIUM] The Mandate→settlement-L/PS "distribute-down drift" is the one center→periphery legitimacy flow in the system, and it is grounded only on a loose Polybian-anacyclosis analogy — the exact "legitimacy from above" shape the corpus's Roman verifier warns against.

**Artifacts.** `chain_map_v1 V7` / `gap_register_v2 V7,§7` / `decision_queue_delta §C` (the drift +
its grounding) vs `research/governance/conflicts_power_struggles.md` (Roman verifier note + the whole
non-MoH re-grounding constraint).

**The mechanic, quoted.** `chain_map V7`: *"Mandate → settlement L/PS (mean-reverting drift) …
`ΔL_drift = sign(M_prev−L)·1` when `|M_prev−L|≥2`"* — i.e., a settlement's Legitimacy is pulled
±1/season **toward the national Mandate**. Structurally this is a top-down legitimacy transfer
(national → local).

**The constraint it brushes.** The corpus's Roman verifier note (quoted verbatim in `gap_register §7`
and `adversarial_review §2`): *"do not let the synthesizer re-narrate the Third-Century accumulator as
legitimacy 'draining from above' — the mechanism is army-loyalty fission, and the framing must stay
endogenous."* The entire re-grounding pass insists legitimacy is sourced **bottom-up** (settlement
consent aggregating up to Mandate), never top-down.

**The grounding gap.** `gap_register §7` / `decision_queue §C` justify the drift's decay term on
*"Polybian anacyclosis / regime-cycle as *confirmatory* grounding that a legitimacy which only ratchets
up is a modeling error."* But anacyclosis is a theory of regime-**form** cycling
(monarchy→tyranny→…), **not** of center→periphery legitimacy transfer. It supports "legitimacy should
decay, not only ratchet" — it does **not** support "the national Mandate pulls each settlement's
Legitimacy toward itself." That is a surface analogy. `adversarial_review §F-4` independently found the
anacyclosis *section-pointer* is wrong (it lives in Han §3.6 Dong Zhuo, not "synthesis"), compounding
the thinness. Notably, the **aggregate-UP** direction (settlement→Mandate) is impeccably grounded
throughout; only this **DOWN** direction — the MoH-shaped one — lacks a precedent showing the flow it
actually implements.

**Why it's a cross-artifact finding (not the review's MoH pass).** `adversarial_review §2` cleared the
*term* "Mandate" (correctly — it is Valoria's endogenous aggregate stat) and flagged the anacyclosis
*pointer*, but did **not** examine the drift's **direction** against the "no legitimacy from above"
rule. This is not a hard MoH *leak* (the drift is a bidirectional convergence device, not cosmic
favor) — but it is the single place in the whole set where a reviewer scanning for MoH-shaped flow
should slow down, and no artifact grounds it endogenously.

**Reconciliation (one line).** Re-ground the distribute-down drift on an **endogenous** mechanism
(settlements observing and conforming to the regime's demonstrated performance — a bottom-up
perception loop) and add a one-line note that it is a coupling/convergence device, not center-sourced
legitimacy, closing the MoH adjacency; re-cite anacyclosis to `research §3.6` per review F-4.

---

### X-5 · [taxonomy/scale consistency · A↔C · MEDIUM] The ratified scale hierarchy is stated at different cardinality across corpora (research 5-tier vs docket 6-level), and the docket's "4-of-6" enum headline conflates the non-ladder `peninsula` into the count while omitting `system_meta`.

**Artifacts.** `research/governance/governance_modes.md` synthesis vs `chain_map_v1 §0/§1` +
`gap_register_v2 NG-1` + `decision_queue_delta #10`; cross-checked against
`designs/architecture/key_substrate_v30.md`.

**The conflict, quoted.**
- Research (`governance_modes` synthesis, line 13): *"That maps directly onto Valoria's **ratified
  Country→Duchy→Province→Territory→Settlement hierarchy**"* — **five** tiers, no character/personal.
- Docket (`chain_map §1`, line 86): *"Ratified **6-level** hierarchy … character → settlement →
  territory → province → duchy → country"*; `gap_register NG-1`: *"ratified ladder is **6-level**
  (`doc:scale_hierarchy_v1 §1`)."*

Both call their structure "ratified." They disagree on cardinality (5 vs 6) and on whether
character/personal is a member. They are plausibly describing different objects (governance *tiers*
vs scale *bands*), but nothing in the set reconciles them — a reader cannot tell whether "the ratified
hierarchy" has five rungs or six.

**The compounding arithmetic error.** `chain_map §0.1` headlines *"The `scale_signature` enum is
**4-of-6**"* with the 4 = `{personal, settlement, territory, peninsula}`. But the chain map itself
notes `peninsula` is *"one world-layer, NOT province/duchy/country"* — i.e., **not a ladder rung** —
so it should not fill a ladder slot in a "of-6" count. And `key_substrate_v30.md:447` shows the doc's
own example stamping a **fifth** value, `scale_signature=['system_meta']`, which the "4-member enum"
framing omits. The honest count is *"3 of the 6 ladder rungs are nameable (personal/settlement/
territory); 3 are not (province/duchy/country); plus 2 non-ladder values (peninsula, system_meta)."*
The BROKEN-above-territory classification is correct and, per `adversarial_review §F-3`,
code-enforced (`keys.py:355-359`) — this is purely a headline-precision defect, not a status error.

**Reconciliation (one line).** State the ratified hierarchy's cardinality once, consistently, across
A and C (governance tiers = 5, scale bands = 6, if that is the intent), and rewrite the enum headline
as "3 of 6 ladder rungs nameable + peninsula/system_meta as non-ladder values," so the denominator
and the peninsula/`system_meta` handling are not silently conflated.

---

### X-6 · [grounding through-line · A↔C · MEDIUM] The 8-value `governance_mode` taxonomy is *used* consistently across all artifacts, but the decision-queue grounds it on an out-of-corpus precedent (Aristotle/Athens) while corpus A directly validates all eight — a missed re-grounding.

**Artifacts.** `governance_modes.md` synthesis + hooks table vs `decision_queue_delta_v1 #8`
(GAP-C2) + `gap_register_v2 §6`.

**Consistency confirmed (the good half).** All eight values — `AUTOCRATIC_FIAT`,
`OLIGARCHIC_COUNCIL`, `NEGOTIATED_ESTATES`, `LANDHOLDER_FRANCHISE`, `CONSENSUS_UNANIMITY`,
`DELIBERATIVE_ASSEMBLY`, `ROYAL_COURT_APPOINTMENT`, `MERITOCRATIC_BUREAUCRATIC` — are used identically
in the research synthesis, the census's per-role "mode-as-constraint-set" tables, `gap_register §6`
("the 8-value FLAG domain the census leans on throughout"), and `decision_queue #8`. No taxonomy
drift. (This resolves the task's scale-consistency check #4 in the affirmative for the mode taxonomy.)

**The through-line miss (the defect).** `decision_queue #8` grounds the adoption on *"Precedent:
Aristotle/Athens-sortition/Roman-comitia/consensus polities"* — of which only Roman-comitia is one of
the eight read civilizations; **Aristotle and Athens-sortition are not in corpus A** (Byzantine
omitted; no classical-Greek civ). Yet `governance_modes` synthesis (lines 12-14, 32-47) explicitly
says the eight-value taxonomy *"maps directly onto"* the read civilizations and supplies a working
instance of **all eight** (AUTOCRATIC_FIAT=Ottoman, OLIGARCHIC_COUNCIL=Divan/*intercessio*,
NEGOTIATED_ESTATES=Reichstag, LANDHOLDER_FRANCHISE=HRE-elective, CONSENSUS_UNANIMITY=conclave,
DELIBERATIVE_ASSEMBLY=Roman-comitia, ROYAL_COURT_APPOINTMENT=Carolingian,
MERITOCRATIC_BUREAUCRATIC=Roman-cursus/Han). GAP-C2 is a *carried* 2026-07-13 gap, so its
Aristotle/Athens grounding predates the corpus — the defect is that the pass ingested a fresh corpus
that richly validates the exact taxonomy and never re-pointed the item to it.

**Reconciliation (one line).** Re-ground `decision_queue #8` primarily on `governance_modes §synthesis`
(the eight in-corpus civ instances); keep Aristotle only as theory backdrop.

---

### X-7 · [definition drift · C↔C · MEDIUM] "Mandate" — the system's central stat — is defined three different ways across the docket, reproducing the CLAUDE.md §5 "defined three ways" anti-pattern.

**Artifacts.** `churn_map §2` vs `chain_map V3` / `module_contracts.yaml:604` vs `gap_register §A` /
`decision_queue #3` (D4).

**The three forms, quoted.**
- `churn_map §2`: *"Mandate = **Σ settlement L/PS**"* (raw sum).
- `chain_map V3` (citing `module_contracts.yaml:604`): *"Mandate=**clamp(round(7T/(T+6)),0,7)**"*
  (saturating transform).
- `decision_queue #3` / `gap_register §A` (D4): *"retire `round(7T/(T+K))` as collapse carrier →
  **floor-avg Order** + fracturing + Standing Keys."*

These may be reconcilable (raw sum vs saturating transform *of* the sum vs a PROPOSED replacement),
but **no single artifact states the reconciliation**, so a reader gets three definitions of the
system's load-bearing stat. This is precisely the hazard CLAUDE.md §5 records for Combat Pool
("defined three different ways"), now recurring for Mandate — and it is invisible unless the three C
files are read together (each is internally consistent).

**Reconciliation (one line).** State the canonical Mandate definition once (the aggregate transform),
mark "floor-avg Order" explicitly as the *proposed D4 replacement* with a cross-reference, and have
`churn_map` cite the transform, not the raw sum.

---

### X-8 · [provenance seam · B→C · LOW-MEDIUM] The docket consumes the vector audit's structural registers as authoritative inputs but never surfaces corpus B's own top-line confidence caveats.

**Artifacts.** `02_weakness_register.md` (corpus B) vs `chain_map §3.1` / `gap_register §5` (which
cite `audit:structure_register.md` throughout).

**The unsurfaced caveats, quoted from B.** `02_weakness_register.md`: *"Validation: **FAILED (1/3)**.
Confidence inherits from validation,"* and *"this L0 layer is a **CURATED slice** — 110 design docs =
**10.3% of** the 1071 `.md` under `designs/` … a green result here is NOT whole-repo coverage."* B
also headlines **Crown as the dominant cascade sink** (*"Crown — 189 chains terminate here"*) and a
notional-edge attractor (20 edges → Crown at cite-weight 183).

**The seam.** The docket cites B's **structure_register** (the deterministic, working-tree, "measures
does not gate" layer — appropriately the reliable one) for `doc:null` and dangling-emit inputs, and
largely does *not* lean on the FAILED-validation weakness_register — which is defensible discipline.
But it never *says* which B layer it trusts, so a reader cannot tell the structural-debt inputs come
from a curated 10% slice whose sibling layer failed its own validation. And B's single loudest
finding — Crown as the #1 cascade black-hole — is nowhere reflected in the docket's gap prioritization
(the chain-bypass item #4 touches Crown but not as a cascade sink).

**Reconciliation (one line).** Add one sentence to `chain_map §3.1` naming the B provenance
("structural inputs are from the deterministic `structure_register`, not the FAILED-validation
`weakness_register`; both are a curated ~10% `designs/` slice") and note the Crown-cascade-sink finding
as a watch item.

---

## What unifies cleanly (confirmed, not refuted)

- **MoH at the mechanic level is clean across all three corpora.** Consistent with
  `adversarial_review §2`: every MoH token in A and C is a "historical grounding only" / "do not port"
  tag; no MoH-shaped mechanic is proposed in any Valoria-mechanic column. X-4 is an *adjacency to
  scrutinize in the distribute-down direction*, not a leak.
- **The 8-value governance_mode taxonomy is used identically** in A, the census, `gap_register`, and
  `decision_queue` (X-6 is a grounding-citation miss, not a usage drift).
- **The core structural gaps are genuinely cross-consistent** where it counts: L/PS 100/100 inert,
  V2-as-the-one-live-vertical-aggregation, FI zero-dispatch, and the scale enum's BROKEN-above-territory
  status agree across `chain_map`, `gap_register`, the vector audit, and (per `adversarial_review`) the
  actual `sim/` tree.
- **The re-grounding harvested most of the `conflicts` corpus correctly** (Gracchi, YoFE,
  Janissary+fatwa, 887-888, Venetian ladder, recognition-fission) — X-2 is about four *specific*
  dropped hooks, not systemic neglect.

## Bottom line

The three corpora are individually strong and the docket's internal antagonist already hardened corpus
C. The failures are **at the seams**: the research→gameplay through-line drops four live hooks (X-2)
and mis-sources one census fill to the corpus (X-3); two C files contradict each other on the two most
load-bearing edges (X-1); the central stat is defined three ways (X-7); the one top-down legitimacy
flow is grounded on a loose analogy the corpus warns against (X-4); and the ratified-hierarchy
cardinality and the 8-mode grounding are stated inconsistently across A and C (X-5, X-6). All eight are
correctable in place and none overturns a headline gap or a THIN/OK verdict. Apply X-1 through X-3
before the DESIGN pass treats the set as a unified whole; X-4 through X-8 are reconciliations.
