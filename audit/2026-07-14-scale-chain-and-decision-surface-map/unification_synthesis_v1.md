# Holistic Unification — Governing Synthesis (v1)

## Status: FILED (unification synthesis) — 2026-07-14 · Lane: IN · ED-IN-0064

**What this is.** The capstone that gates the 2026-07-14 governance deliverable set. It reconciles the
whole set — **A** the research corpus (`research/governance/{governance_modes,
political_hierarchy_standing, conflicts_power_struggles}.md`), **B** the vector audit
(`2026-07-14-governance-vector-audit/`), **C** the chain/gap docket (this directory's five maps), and
the two antagonist passes over them (`adversarial_review_v1` = corpus-C-internal, findings **F-1..F-6**;
`unification_findings_v1` = cross-corpus seams, findings **X-1..X-8**) — into **one governing picture
and one prioritized fix-list**. Every X- and F- finding is resolved explicitly (§4 ledger, §5 fixes).

**How the two antagonist passes relate (do not double-count).** `adversarial_review_v1` re-checked
corpus C *against the `sim/` working tree and cited docs* and returned SOUND_WITH_FIXES; it hardened C
internally (caller counts, firing frequency, citation precision) but scoped each C file independently.
`unification_findings_v1` then read A+B+C *together* and returned UNIFIES_WITH_FIXES, surfacing the
**seams between** corpora that a single-corpus pass structurally could not see. This synthesis binds
both: the F-findings are C-hardening, the X-findings are cross-corpus reconciliation, and none overturns
a headline gap, a THIN/OK verdict, or the ranked queue. **All fixes land in corpus-C docket files** —
the research corpus A and vector audit B are the ground truth being *correctly re-cited*, not edited.

**The binding constraint holds set-wide.** Mandate of Heaven is **not** a proposed Valoria mechanic
anywhere in A, B, or C. `adversarial_review §2` verified this clean at the mechanic level; the one place
a reviewer should slow down (the distribute-down drift, X-4) is an *adjacency to close*, not a leak.

---

## 1 · The research → gameplay through-line (character ↔ country, all non-MoH)

The three research documents are not three topics; they are the three faces of **one bidirectional
ripple** between the personal scale (a character resolving a scene) and the country scale (a polity's
legitimacy, mode, and collisions). The videogame's no-GM engine runs that ripple over the five
primitives the churn map names (`key_substrate` Key emission, Ledger tag, Disposition, Π,
Standing/`consolidation_progress`). Read as a single narrative:

**The atomic signal is resolution quality, and it flows UP.** Every governed event is a vise — a
Directive from above colliding with settlement Needs from below (`governance_play_redesign §1.4/§1.5`).
When a character resolves it, the outcome emits a Key carrying `resolution_quality = w_d·(delivered −
demanded)_Directive + w_n·(delivered − demanded)_Need` (`governance_ripple_substrate §5`). This single
arithmetic gap is the **hierarchy research's** central find made mechanical: *rank is a display-aggregate
over a debasable currency, not ground truth* (`political_hierarchy_standing` framing) — so the
resolution-quality signal advances or demotes **Standing** via the delivered-vs-demanded bridge (Roman
*lex repetundae*, Carolingian *missi*, HRE *Reichsexekution*, Han *cha ju*/impeachment, Japanese
*honryō-andō*), aggregates into settlement **L/PS**, and rolls up through territory → **faction
Mandate** → peninsula. This is **the explicit non-MoH legitimacy source the brief requires**: legitimacy
is *earned performance observed and rewarded*, never cosmic favor.

**The country scale constrains what flows back DOWN.** At the top, the **modes research** supplies the
`governance_mode` taxonomy — eight values that are each a *constraint-set on the legal response*, not a
costume (an `OLIGARCHIC_COUNCIL` seat cannot emit a Directive a peer vetoed; an `AUTOCRATIC_FIAT` seat
runs inside a parallel legitimacy order that can block it). Mode decides *which verbs are even
affordable* at each tier — it is the "thinness multiplier" the census runs its verdicts against. And the
**conflicts research** supplies the events that fire when the aggregated pressure resonates: the
**two-signal collision primitive** (a material-strain Key AND an independent legitimating-authority Key
must co-fire — Janissary+fatwa, Gracchi land-crisis+re-election-read-as-kingship — a bare grievance
fizzles), the **relief-valves** that bleed pressure short of collapse (scapegoat ladder, ritual
self-reproach), **suppression-backfire** (a "solved" unrest becomes a dormant lower-threshold grievance
handed to the investigation track), **recognition-fission → reaggregation**, and **rank = secession
blast-radius**. Collapse *disperses back down* as a national → province/territory devolution, never MoH
warlordism.

**The circuit, in one sentence.** *Personal-scale resolution quality aggregates up into country-scale
Standing/Legitimacy/Mandate; country-scale mode and collision constrain and discharge back down into
personal-scale affordances and events* — one loop, over five shared primitives, grounded end-to-end in
eight civilizations' endogenous political mechanics with Mandate of Heaven left as history only.

**The through-line has four breaks (X-2) — the four orphaned hooks.** The re-grounding pass harvested
most of the corpus (Gracchi, Year of Four Emperors, Janissary+fatwa, 887-888, Venetian ladder,
recusatio, recognition-fission), but **four live, buildable hooks reached corpus A and died before the
hand-off** — confirmed absent from every actionable C file:

| # | Orphaned hook | Corpus-A home | Where in the circuit it belongs |
|---|---|---|---|
| a | **Permanent-grant / recall-cap removal as a distinguishable collision-trigger event type** (Caesar *dictator perpetuo* → Ides) — "fires a collision check among the highest OLIGARCHIC_COUNCIL seats" | `conflicts` hooks row (§3) | The collision primitive (queue #5) — a named event *sub-type* |
| b | **Dormant-but-live Crown consent-gate that never zeroes under eclipse**, snapping back on a two-signal collision (grounded **non-MoH** on Roman Senate reassertion) | `governance_modes` hooks row (§4-adjacent) | Chain-bypass ranking (queue #4) |
| c | **Bind army/enforcement loyalty to an impersonal charter-Key, never a seat-holder** — the **Tetrarchy failure-guard** | `conflicts §7` + hooks row | **Must accompany the tetrarchy mechanic** — see below |
| d | **Reaggregation can *add a new seat* rather than reverse** (Palatinate 1623 added an Electoral seat) | `political_hierarchy_standing` hooks row | Devolution output (queue #3) / succession |

Hook (c) is the sharpest instance and the reason X-2 is HIGH, not housekeeping. **The corpus itself
pairs the mechanic with its guard and the hand-off carries neither.** `governance_modes §4` explicitly
*offers* the Tetrarchy as a player-chosen anti-secession mitigation: *"the Tetrarchy itself is a template
for deliberate multi-seat power-sharing installed as an anti-civil-war mechanism … a designed
alternative to single-heir succession that Valoria's Duchy/Country tier could offer as a player-chosen
mitigation against secession risk, at the cost of creating exactly the four-way collision it was meant
to prevent (see conflicts_md, Tetrarchy collapse)."* And `conflicts §7` supplies the mandatory guard,
naming §4 by hand: *"a critical cautionary design hook for the 'Tetrarchy as anti-secession mechanism'
hook proposed in modes_md §4 — … it must gate legion/army-equivalent loyalty to the structure itself
(not to any one seat-holder) or the mechanic will reliably reproduce exactly the single-claimant
collapse it was built to prevent — a strong argument for tying army loyalty checks to an impersonal
charter-Key rather than a named seat-holder Key."* Offering the multi-seat power-share **without** its
charter-Key enforcement guard is a design landmine the corpus already flagged (Go-Tairō fracture,
Tetrarchy 306-324). The fix (§5) carries **both halves as one inseparable Tier-2 item**.

---

## 2 · The unified cross-scale + cross-subsystem picture (the boundary stated once)

The chain map's two axes, the #136 L/PS spec, and the ripple-substrate loop describe **one machine**.
Vertically (V1-V9), occurrences **aggregate up** (scene → settlement L/PS → Mandate → peninsula) and
**disperse down** (Mandate → settlement drift; peninsula Cooling → settlement Π). Horizontally (H1-H6),
a faction/domain action **cascades across** FA → SC (Censure) and is *meant* to reach FI
(field-investigation) — the horizontal analogue of the vertical axis. The #136 spec (`lps_wiring_v1.md`)
is the **designed-but-uncoded** closed form for the whole settlement→Mandate→settlement loop; the
ripple-substrate loop (`governance_ripple_substrate §1/§5.5`) is the **narrative trace** the same edges
leave. They agree on the mechanism and disagree only on *grade*.

**The single correct grading rule (resolves X-1).** **Canon-WIRED ≠ sim-WIRED.** A doc's self-audit can
verify a design is *specified* (canon grade) while the running `sim/` tree does *not execute* it
(sim-reality grade). The chain map is right to track both columns because they disagree on 4 of 8 edges;
the churn map inherited only the canon column and mis-filed two flagship gaps as accomplished plumbing.
**Grade every edge on the sim-reality column; the canon column is the design target, not the running
truth.** Applying that rule once, across the whole set:

| Edge (chain-map key) | Canon grade | **Sim-reality grade (governs)** | Evidence |
|---|---|---|---|
| **V2** settlement Order → province Accord | WIRED | **WIRED** — the one genuinely live vertical aggregation | `registry.py:124-130` floor-mean over real members |
| **H1** faction-action → domain/mgmt action | WIRED | **WIRED** (live strategic loop; resolver `domain_actions` is `doc:null`) | `mc_v18.py:89-97` → `faction_action.py:176-241` |
| **H2** domain action → SC (Censure) | WIRED | **WIRED but conditional/probabilistic** (F-1: ~30% neutral unique slot, quadruple-gated — **not** "unconditional/every season") | `faction_action.py:176-269`; `parliamentary_action.py:136` |
| **V5** faction → peninsula (correlated shock) | WIRED | **WIRED** (contract) | `module_contracts.yaml:64-66,509-518` |
| **V1 · V3 · V7** scene → L/PS → Mandate → L/PS drift | WIRED (§13) | **SPEC-ONLY** — #136 designed, **0 `sim/`**; L/PS **100/100 inert**; live vote on scalar `Faction.L` placeholder | `lps_wiring_v1 §4/§5`; `parliamentary_vote.py:168` PRE-LPS-1 |
| **V4** territory → province → duchy → country | WIRED | **BROKEN** — enum is 4-of-6; `keys.py:355-359` actively rejects the missing bands | `keys.py:62`; blocked on NG-1 + `engine_clock` |
| **V8 · H2′ · H3** char/domain scene → faction (Domain Echo) | WIRED | **INERT under flag** — fires only if `world.echo_scheduler` attached (default OFF); echo hardcodes `scale_signature=["personal"]` | `echo_transport.py`; `mc_v18.py:109-113` |
| **V9** combat scene → faction | WIRED | **BROKEN (double)** — dangling emit + combat path always-defers | `structure_register.md:18-19`; `scene_dispatch.py:137-145` |
| **V6 · standing-bridge · arc-feedback** | WIRED | **HOOK-NEEDED** — one authored clause each | `governance_ripple_substrate §13` self-audit |
| **H4 · H5 · H6** any → field-investigation | DOCTRINE-ONLY / BROKEN | **BROKEN** — FI has **zero live dispatch**; `investigation.py`/`fieldwork.py` are import-orphans | `scene_dispatch.py:129-215` (no FI branch) |
| **§6.2** event → Parliament/SC | AT-RISK | **AT-RISK** — no `stakes.source_key` consume-edge; resemblance-not-dependency by the spec's own §9 test | `module_contracts.yaml:513` |

**So X-1 resolves thus:** the churn map's two "verified WIRED" EXISTS entries are **canon-WIRED /
sim-not-WIRED** — Mandate aggregation is **sim-INERT** (runs on the scalar `Faction.L` placeholder, L/PS
100/100 dead), and `scale_signature` stamping is **sim-BROKEN above territory** (4-of-6 enum; echo
hardcodes `["personal"]`). By the set's own ground truth these are the docket's **two biggest gaps**
(gap-ledger ranks 1 and 2), not accomplished plumbing.

**Mandate is one stat with one canonical definition (resolves X-7).** The three forms in the docket are
not three definitions: the canonical Mandate is the **saturating aggregate transform**
`clamp(round(7T/(T+6)),0,7)` over the settlement-L/PS aggregate (`module_contracts.yaml:604`); the churn
map's *"Σ settlement L/PS"* is informal shorthand for that transform's **input**; and *"floor-avg Order
+ fracturing + Standing Keys"* is the **PROPOSED D4 replacement** of the collapse-carrier, pending
sign-off — a future, not a present, definition. Stated once, the CLAUDE.md §5 "defined three ways"
anti-pattern dissolves.

**Scale cardinality is one structure counted two ways (resolves X-5).** Research names **5 governance
tiers** (Country→Duchy→Province→Territory→Settlement); the docket names a **6-level scale ladder** that
adds character/personal as the base band. Same structure, different denominator, both correctly
"ratified." And the enum headline should read honestly: **3 of 6 ladder rungs are nameable**
(personal/settlement/territory), 3 are not (province/duchy/country, all BROKEN above territory), **plus 2
non-ladder values** (peninsula, `system_meta`) — the "4-of-6" framing silently promoted the non-ladder
`peninsula` into a rung and omitted `system_meta`.

**Provenance of the structural inputs (resolves X-8).** The docket's structural claims come from the
vector audit's **deterministic, working-tree `structure_register`** (the "measures, does not gate"
layer) — appropriately the reliable one — **not** the `weakness_register`, which **FAILED its own
validation (1/3)**; and **both** are a curated **~10.3% slice** (110 of 1071 `.md` under `designs/`), so
a green structural result is *not* whole-repo coverage. Corpus B's single loudest finding — **Crown as
the #1 cascade sink (189 chains terminate there)** — is a standing **watch item** the gap prioritization
should name.

---

## 3 · The single ranked MoH-free design surface handed to Jordan (Tier 1-4)

This is `decision_queue_delta_v1`'s ranked queue **with the cross-corpus fixes folded in** — X-2's four
orphaned hooks absorbed into their items (▲), and X-6's in-corpus re-grounding applied (◇). Classes:
**[CTC]** complete-the-chain (execution on sound logic) · **[GAP]** genuine precedent-informed design
call. Nothing here executes; each fix stays PROPOSED, needing its own sign-off (CLAUDE.md §1).

**Tier 1 — unblock the whole spine (do first)**
1. **Approve the #136 L/PS impl PR** (B1+A2+B4+A4-artifact) — [CTC]. Code `lps_wiring_v1 §5` into `sim/`
   (new `sim/territory/legitimacy.py`; rewire `parliamentary_bridge`/Treasury/AP to read the aggregate,
   not scalar `Faction.L`). Turns 4 chain-map edges from canon-WIRED/sim-INERT to agreeing at once —
   the single highest-leverage action.
2. **Wire `propose_transfer` to the seasonal vote** (GAP-A1) — [CTC]. Ends the one-way-ratchet defect
   (territory can never be regained); no new code. *(The "~87% win-share" it was conflated with is a
   debunked small-N artifact; corrected golden dist 37.5/12.5/12.5/37.5.)*
3. **Mandate collapse + two relief-valves — RE-GROUNDED** (GAP-B2) — [GAP]+[CTC]. Confirm D4 (retire
   `round(7T/(T+K))` as collapse carrier → floor-avg Order + fracturing + Standing Keys); rule the two
   valves on **non-MoH** precedent (scapegoat ladder; ritual self-reproach). ▲ **Devolution output adds
   the reaggregation-topology nuance (hook d): reaggregation may *add a new seat*, not only reverse**
   (Palatinate 1623). ◇ Re-ground the V7 distribute-down drift **endogenously** (settlements conform to
   demonstrated regime performance — a bottom-up perception/convergence device, not center-sourced
   legitimacy), closing the X-4 MoH-adjacency.

**Tier 2 — the genuine new-mechanism / new-verb surface (Jordan's direct calls)**
4. **Rank the two chain-bypass authorities** (GAP-D1) — [GAP]. Monarch + Parliament bypass with no
   precedence; add a **third bypass-adjacent authority** (standing ideological/juridical seat — Ottoman
   Şeyhülislam) + an **ad-hoc emergent** non-chartered bypass (Roman SCU). ▲ **Add hook (b): the
   dormant-but-live Crown consent-gate that never zeroes under eclipse** and snaps back on a two-signal
   collision (non-MoH, Roman Senate reassertion).
5. **Collision-of-stresses two-signal primitive — RE-GROUNDED** (GAP-E1/E2) — [GAP]. Two independently
   arriving signals (material threshold AND independent legitimating trigger) must resonate; a bare
   grievance fizzles. ▲ **Add hook (a): permanent-grant / recall-cap removal as a distinguishable
   collision-trigger event type** (Caesar *perpetuo* → Ides) firing a collision check among the highest
   OLIGARCHIC_COUNCIL seats.
   **5b. Tetrarchy multi-seat power-share — MECHANIC + MANDATORY FAILURE-GUARD (hook c)** — [GAP]. Offer
   the tetrarchy-style deliberate multi-seat power-share as a player-chosen anti-secession mitigation
   (`governance_modes §4`) **bound inseparably to its charter-Key enforcement guard** (`conflicts §7`):
   gate army/enforcement loyalty to an **impersonal charter-Key, never a seat-holder Key**, or it
   reproduces single-claimant collapse. **Never surface the mechanic without the guard** — the corpus
   flags the unguarded version as a landmine (Go-Tairō, Tetrarchy 306-324).
6. **Author the thin decision-surface verb sets** (NG-4) — [GAP]. Council (~5), bureaucrat (~5),
   Parliament-body (~4); guard: each verb must emit a down-tier Key or it is decorative false depth.
   *(Bureaucrat menu re-grounded on **in-corpus Han cha ju / hejue audit**, not the out-of-scope Ming
   kaochengfa — X-3.)*
7. **Parliament's ruled-reach verb + armature binding** (NG-5) — [GAP]+[CTC]. A `Reichsexekution`-shaped
   Domain Action emitting a coercive Key onto a named province/territory/settlement.
8. **Governance-mode FLAG taxonomy** (GAP-C2) — [GAP]. Adopt the 8-value `governance_mode` domain. ◇
   **Re-grounded on `governance_modes §synthesis` — all eight values instanced in-corpus** (X-6):
   AUTOCRATIC_FIAT=Ottoman · OLIGARCHIC_COUNCIL=Divan/*intercessio* · NEGOTIATED_ESTATES=Reichstag ·
   LANDHOLDER_FRANCHISE=HRE-elective · CONSENSUS_UNANIMITY=conclave · DELIBERATIVE_ASSEMBLY=Roman-comitia
   · ROYAL_COURT_APPOINTMENT=Carolingian · MERITOCRATIC_BUREAUCRATIC=Roman-cursus/Han. Aristotle/Athens =
   theory backdrop only.
9. **Suppression-backfire + identity-migration** (GAP-G2) — [GAP]. Seven backfire mechanisms; convert a
   militarily-solvable problem into a Fieldwork/Investigation one; model a floor, not a zero.

**Tier 3 — rulings + authoring that unblock chain-completions**
10. **Extend `scale_signature` to 6-of-6** (NG-1) — [CTC]+sliver. Add province/duchy/country; rule
    `peninsula`'s relation to the ladder (WS2). Unblocks V4 + everything above territory.
11. **Add the Field-Investigation dispatch branch** (NG-2) — [CTC]. One `scene_type` branch importing
    the orphan resolvers. Unblocks H4/H5/H6.
12. **Author `engine_clock` + `domain_actions` home docs** (VA-1) — [GAP]. The two load-bearing
    `doc:null` contracts of 9.
13. **Wire the combat bottom-up echo** (V9/VA-2) — [CTC].
14. **Turn ECHO_TRANSPORT on by default** (V8/H2′/H3) — [CTC].
15. **`stakes.source_key` predicate — earn or weaken** (§6.2/§3 AT-RISK edge) — [GAP].
16. **Carried Tier-3 rulings** (C3, D2, B3, B5) — [CTC].

**Tier 4 — hygiene, slivers, held proposals**
17-20. Repair `id_reservations.yaml` duplicate-IN-key (NG-6); register the 4 unregistered-canonical
heads + resolve `combat_v30` currency-drift (VA-3/VA-4); re-index orphans + repoint stale pointers
(VA-5); carried Tier-4 (elect-inward armature stays fable/opus-gated PROPOSED).

---

## 4 · Reconciliation Ledger (every finding resolved)

| Finding | Corrected position | Doc(s) to edit |
|---|---|---|
| **X-1** [C↔C · HIGH] churn_map reports Mandate aggregation + `scale_signature` stamping "verified WIRED"; chain_map/gap_register class them SPEC-ONLY/BROKEN | **sim-WIRED ≠ canon-WIRED.** Both are canon-WIRED but **sim-INERT** (Mandate: scalar `Faction.L` placeholder, L/PS 100/100 inert) / **sim-BROKEN above territory** (enum 4-of-6; echo hardcodes `["personal"]`). chain_map/gap_register grade governs. | `churn_event_opportunity_map_v1.md §2` (EXISTS) |
| **X-2** [A→C · HIGH] four load-bearing research hooks orphaned before the hand-off | Carry all four into the queue: (a) permanent-grant event type → #5; (b) dormant Crown gate → #4; **(c) Tetrarchy charter-Key guard → new #5b, inseparable from the tetrarchy mechanic `governance_modes §4` offers**; (d) reaggregation-adds-a-seat → #3. | `decision_queue_delta_v1.md` (Tier 2 items + new §D harvested/deferred ledger) |
| **X-3** [C→A · MED-HIGH] census cites *kaochengfa* to `political_hierarchy_standing §1.0d` — a §-number that file lacks, for a **Ming** precedent outside the 8-civ corpus | Drop the research-corpus attribution; the mechanic is a **design-doc** fill (`faction_politics_v30 §1.0d`). Re-anchor the *research* pillar to the genuinely in-corpus **Han cha ju / hejue audit** (`political_hierarchy_standing` §2.2/§2.3, Han section). | `decision_surface_census_v1.md §2(d)` (line 162) + §7 (lines 441-442) |
| **X-4** [A↔C · MED] distribute-down drift = the one center→periphery legitimacy flow, grounded on a loose Polybian-anacyclosis analogy the Roman verifier warns against | Re-ground **endogenously**: settlements observe and conform to the regime's *demonstrated performance* (bottom-up perception loop); label the drift a **coupling/convergence device (mean-reversion between aggregate and parts), not center-sourced legitimacy** — closes the MoH adjacency. Anacyclosis stays **confirmatory-only** ("legitimacy should decay, not only ratchet"), re-cited to `research §3.6`. | `gap_register_v2.md §7` + `decision_queue_delta_v1.md §C` |
| **X-5** [A↔C · MED] scale cardinality stated 5 (A) vs 6 (C); "4-of-6" enum conflates non-ladder `peninsula`, omits `system_meta` | Governance **tiers = 5**; scale **bands = 6** (adds personal). Enum honestly = **"3 of 6 ladder rungs nameable (personal/settlement/territory) + peninsula/`system_meta` as non-ladder values."** BROKEN-above-territory unchanged. | `chain_map_v1.md §0.1` + `§1` |
| **X-6** [A↔C · MED] 8-value taxonomy grounded on out-of-corpus Aristotle/Athens while corpus A instances all eight | Re-ground primarily on `governance_modes §synthesis` (eight in-corpus civ instances, listed in #8); keep Aristotle as theory backdrop only. | `decision_queue_delta_v1.md #8` (line 52) |
| **X-7** [C↔C · MED] "Mandate" defined three ways | Canonical = saturating transform `clamp(round(7T/(T+6)),0,7)` over the L/PS aggregate (`module_contracts.yaml:604`); "Σ settlement L/PS" = informal input shorthand; "floor-avg Order" = **PROPOSED D4 replacement** (cross-ref), not a live third definition. | `churn_event_opportunity_map_v1.md §2` (cite transform) + one-line note in `gap_register_v2.md §A` / `decision_queue_delta #3` |
| **X-8** [B→C · LOW-MED] docket consumes B's registers but never surfaces B's confidence caveats | Name the provenance: inputs from the **deterministic `structure_register`**, not the FAILED-validation (1/3) `weakness_register`; both a **curated ~10.3% `designs/` slice**. Add **Crown-as-#1-cascade-sink (189 chains)** as a watch item. | `chain_map_v1.md §3.1` + `gap_register_v2.md §5` |
| **F-1** [CONFIRMED] H2 Censure labeled "unconditional / every season" | **WIRED but conditional/probabilistic** — reached via the ~30% (neutral, state-reweighted) unique slot, gated on parliamentary-eligibility + specific-unique-fallthrough + GD-3/§5.4 proposer-minimum. The substantive "orphan-mutator retired" correction **stands**. Drop "UNCONDITIONAL" from the caller-graph edge. | `chain_map_v1.md §0.4/§2.1/§2.2` + `gap_register_v2.md §3 (H2)` |
| **F-2** [CONFIRMED] `run_parliamentary_vote` caller count wrong + self-contradictory (§0.4 3+2 vs §2.2 2+3) | **4 call sites = 2 live** (propose_censure — conditional; parliamentary_bridge — flag-gated) **+ 2 orphan** (parliamentary_transfer, parliamentary_stay). The emergency-council path is **not** a caller (it calls `sim.personal.contest`) — drop it from the count. | `chain_map_v1.md §0.4` + `§2.2` |
| **F-3** [CONFIRMED, self-strengthening] scale-canonicity rejection cited to doc "invariant 7," which lacks it | Invariant 7 reads only *"`scale_signature` non-empty."* The canonicity rejection is **code-enforced** — re-cite to `code:keys.py:355-359` (raises `KeyValidationError`, enforcing the §2.1 enum); strike "members must match the canonical set" from the paraphrase. BROKEN classification unchanged (in fact strengthened). | `chain_map_v1.md §1.1` + `gap_register_v2.md NG-1` (line 53) |
| **F-4** [PLAUSIBLE] recusatio (self-reproach) is hooks-table-only, no Roman body §; anacyclosis mis-pointed to "synthesis" | Cite recusatio to the hooks-table row "Ritual self-abasement" and **flag it wants a dedicated body paragraph before grounding a ratified mechanic** (do not represent as body-attested). Re-cite anacyclosis to `research §3.6` (Dong Zhuo). Neither affects the MoH binding. | `gap_register_v2.md §7` + `decision_queue_delta_v1.md §C` |
| **F-5** [PLAUSIBLE] census ~4-5 bar sits *at* the 3-5 scene budget, but "surplus is the point" needs the menu to *exceed* it | State the fills' ~4-5 as a **floor, not a target** (or raise the authored target to ≥6 where practical). Verdicts unaffected — the bar is self-flagged "deliberately soft." | `decision_surface_census_v1.md §0` (+ fill-count phrasings) |
| **F-6** [PLAUSIBLE] governor "~11-13" double-counts method sub-choices as standalone verbs | Defensible standalone count ≈**10** (8 core + Retain Clerks + Bind the Cells + 3 Directive responses; Survey / Negotiate Quota / Ordenanza are method-branches of existing verbs). **OK verdict robust regardless.** *(Task named F-1..F-5; F-6 folded for completeness.)* | `decision_surface_census_v1.md §3(b)` (line 215) |

**Confirmed unified cleanly (not refuted, no edit):** MoH is clean at the mechanic level across A/B/C
(`adversarial_review §2`); the 8-value taxonomy is *used* identically everywhere (X-6 is a citation
miss, not usage drift); the core structural gaps (L/PS 100/100 inert, V2 the one live vertical
aggregation, FI zero-dispatch, BROKEN-above-territory) agree across chain_map, gap_register, the vector
audit, and the actual `sim/` tree; and the re-grounding harvested most of the `conflicts` corpus
correctly (X-2 is four specific drops, not systemic neglect).

---

## 5 · Prioritized FIX-LIST (file + exact change, for the orchestrator to apply)

Ordering: **HIGH** = apply before the DESIGN pass binds on the set as a unified whole (the two
antagonist passes' pre-DESIGN gates: X-1/X-2/X-3 + F-1/F-2/F-3). **MED** = reconciliations. **LOW** =
provenance/hygiene. All edits are to corpus-**C** docket files; A and B are not edited.

### HIGH

**H-1 · `churn_event_opportunity_map_v1.md` §2 (EXISTS, lines ~139-144) — resolves X-1 + X-7.**
Re-grade the two "verified WIRED" entries to canon-vs-sim.
- Replace the **Mandate-aggregation** bullet ("*…Mandate = Σ settlement L/PS… Both verified WIRED in the
  ripple substrate's own self-audit (§13/§14.1).*") with a bullet that keeps the canon citation **and
  adds the sim-reality grade**: canon-WIRED but **sim-INERT** — L/PS is 100/100 inert and the live vote
  runs on the scalar `Faction.L` placeholder (`parliamentary_vote.py:168`, PRE-LPS-1/PORT-BLOCKING), not
  a real Σ; the canonical Mandate is the transform `clamp(round(7T/(T+6)),0,7)` (`module_contracts.yaml:604`),
  of which "Σ settlement L/PS" is informal input shorthand, and "floor-avg Order" is the PROPOSED D4
  replacement (X-7). Cross-cite `chain_map §3` + `gap_register V3/NG-3`.
- Replace the **`scale_signature`** bullet ("*…already stamps every state-change with [personal |
  settlement | territory | peninsula]… verified WIRED (§13).*") with: canon-WIRED but **sim-BROKEN above
  territory** — the enum is 4-of-6 (`keys.py:62`), `keys.py:355-359` actively rejects
  province/duchy/country, and the echo path hardcodes `scale_signature=["personal"]`
  (`echo_transport.py`). Cross-cite `chain_map §3` + `gap_register NG-1/V4`.
- Simplest form: move both bullets out of **EXISTS** into a new "**canon-designed / sim-not-yet**"
  sub-bucket, since by the set's ground truth they are the docket's two biggest gaps.

**H-2 · `decision_queue_delta_v1.md` — resolves X-2 (four orphaned hooks; Tetrarchy is the headline).**
- **Tier 2 #5b (new):** add "**Tetrarchy multi-seat power-share — mechanic + mandatory failure-guard**
  [GAP]": offer the deliberate multi-seat power-share as a player-chosen anti-secession mitigation
  (`governance_modes §4`) **bound inseparably to** the charter-Key enforcement guard (`conflicts §7` +
  hooks row): gate army/enforcement loyalty to an *impersonal charter-Key, never a seat-holder Key*, or
  it reproduces single-claimant collapse (Go-Tairō, Tetrarchy 306-324). **Never offer the mechanic
  without the guard.**
- **Tier 2 #4:** append hook (b) — the **dormant-but-live Crown consent-gate that never zeroes under
  eclipse**, snapping back on a two-signal collision (non-MoH: Roman Senate reassertion,
  `governance_modes` hooks row).
- **Tier 2 #5:** append hook (a) — **permanent-grant / recall-cap removal as a distinguishable
  collision-trigger event type** (Caesar *perpetuo* → Ides, `conflicts §3` hooks row), firing a
  collision check among the highest OLIGARCHIC_COUNCIL seats.
- **Tier 1 #3 (devolution):** append hook (d) — **reaggregation may add a new seat, not only reverse**
  (Palatinate 1623 added an Electoral seat, `political_hierarchy_standing` hooks row).
- Add a short **"§D · Harvested vs. deferred research hooks"** ledger recording all four as
  now-absorbed, so no live hook silently dies between corpus A and the hand-off.

**H-3 · `decision_surface_census_v1.md` §2(d) line 162 — resolves X-3.**
- Replace: `**Zhang Juzheng's *kaochengfa* triplicate task-ledger** (`political_hierarchy_standing.md`
  §1.0d precedent, already partly captured as `faction_politics_v30.md` §1.0d *Patron-Sponsored
  Performance Audit*):`
- With: `**Han censorial performance-audit** (in-corpus: `political_hierarchy_standing.md` §2.3 *hejue*
  impeachment / §2.2 *cha ju* recommendation-audit, Han section — the corpus's resolution-quality →
  standing precedent; the *kaochengfa* triplicate task-ledger it echoes is a **design-doc** capture,
  `faction_politics_v30.md` §1.0d *Patron-Sponsored Performance Audit*, not the research corpus):`
- Also fix §7 (lines 441-442): change "*drawn straight from the Kamakura honryō-andō/shin-on and Zhang
  Juzheng kaochengfa research*" → "*drawn from the Kamakura honryō-andō/shin-on research and the
  faction_politics_v30 §1.0d kaochengfa-modeled Performance Audit*" (attribute the Ming item to the
  design doc, not the 8-civ research corpus).

**H-4 · `chain_map_v1.md` §0.4 / §2.1 (H2 row) / §2.2 + `gap_register_v2.md` §3 (H2) — resolves F-1.**
- Relabel H2 from "**unconditional / every season**" to "**WIRED but conditional/probabilistic** —
  reached via the ~30% (neutral, state-reweighted) unique slot, gated on parliamentary-eligibility +
  specific-unique-fallthrough + GD-3/§5.4 proposer-minimum."
- In the §2.2 caller-graph, change the edge `PC ==>|UNCONDITIONAL — WIRED| RPV` to `PC ==>|CONDITIONAL
  ~30%, gated — WIRED| RPV`.
- Keep the "orphan-mutator retired" substantive correction. In `gap_register §3 H2`, change
  "unconditional, applies §5.4/§10 penalties" and "mutates live state every season" to the conditional
  framing.

**H-5 · `chain_map_v1.md` §0.4 + §2.2 — resolves F-2.**
Reconcile both to a single count: "**4 call sites: 2 live** (propose_censure — conditional;
parliamentary_bridge — flag-gated) **+ 2 orphan** (parliamentary_transfer, parliamentary_stay)." Delete
the emergency-council path from the caller count (it calls `sim.personal.contest`, not
`run_parliamentary_vote`); §0.4's "3 live/near-live + 2 orphan" and §2.2's "5 call sites: 2 + 3" both
become 2+2.

**H-6 · `chain_map_v1.md` §1.1 + `gap_register_v2.md` NG-1 (line 53) — resolves F-3.**
Re-cite the scale-canonicity rejection to `code:keys.py:355-359` (raises `KeyValidationError`, enforcing
the §2.1 enum), **not** doc invariant 7; strike "members must match the canonical set" from the
invariant-7 paraphrase (invariant 7 = "`scale_signature` non-empty" only). In NG-1, replace
"`audit:key_substrate_v30 §12 invariant 7` rejects non-canonical members" with "`code:keys.py:355-359`
raises `KeyValidationError` on non-canonical members (enforcing the §2.1 enum)." BROKEN unchanged.

### MED

**M-1 · `gap_register_v2.md` §7 + `decision_queue_delta_v1.md` §C — resolves X-4 (+ F-4 anacyclosis).**
Re-ground the V7 Mandate→settlement-L/PS drift on an **endogenous bottom-up perception loop**
(settlements conform to the regime's demonstrated performance) and add one line: *the drift is a
coupling/convergence device (mean-reversion between the aggregate and its parts), not center-sourced
legitimacy* — closing the "legitimacy from above" adjacency. Re-cite Polybian anacyclosis to
`research §3.6` (Dong Zhuo), and keep it **confirmatory-only** (supports "legitimacy should decay," not
"the national Mandate pulls each settlement's Legitimacy toward itself").

**M-2 · `gap_register_v2.md` §7 + `decision_queue_delta_v1.md` §C — resolves F-4 (recusatio).**
Cite recusatio/self-reproach to the `research` hooks-table row "Ritual self-abasement" and flag that the
valve **wants a dedicated Roman body paragraph before it grounds a ratified mechanic** — do not present
it as body-attested (currently a single hooks-table line).

**M-3 · `chain_map_v1.md` §0.1 + §1 — resolves X-5.**
Rewrite the "`scale_signature` enum is 4-of-6" headline to "**3 of 6 ladder rungs nameable
(personal/settlement/territory); 3 not (province/duchy/country, BROKEN above territory); + 2 non-ladder
values (peninsula, `system_meta`)**." Add a one-line note: the research corpus's 5-tier
Country→Duchy→Province→Territory→Settlement names governance *tiers*; the docket's 6-level ladder adds
character/personal as the base *scale band* — same structure, both ratified.

**M-4 · `decision_queue_delta_v1.md` #8 (line 52) — resolves X-6.**
Change the precedent cell from "Aristotle/Athens-sortition/Roman-comitia/consensus polities" to
"`governance_modes §synthesis` — all eight values instanced in-corpus (AUTOCRATIC_FIAT=Ottoman,
OLIGARCHIC_COUNCIL=Divan/*intercessio*, NEGOTIATED_ESTATES=Reichstag, LANDHOLDER_FRANCHISE=HRE-elective,
CONSENSUS_UNANIMITY=conclave, DELIBERATIVE_ASSEMBLY=Roman-comitia, ROYAL_COURT_APPOINTMENT=Carolingian,
MERITOCRATIC_BUREAUCRATIC=Roman-cursus/Han); Aristotle/Athens as theory backdrop only."

**M-5 · `gap_register_v2.md` §A + `decision_queue_delta_v1.md` #3 — resolves X-7 (pairs with H-1).**
State once: canonical Mandate = the saturating transform `clamp(round(7T/(T+6)),0,7)` over the
settlement-L/PS aggregate (`module_contracts.yaml:604`); mark "floor-avg Order + fracturing + Standing
Keys" explicitly as the **PROPOSED D4 replacement**, cross-referenced, not a competing live definition.

**M-6 · `decision_surface_census_v1.md` §0 (+ fill-count phrasings) — resolves F-5.**
State the ~4-5 bar as a **floor, not a target**: since "the surplus is the point" requires the menu to
*exceed* the 3-5 budget, authored fills should aim ≥6 where practical; the ~4-5 council/bureaucrat/
Parliament fills are the *minimum* to clear false-choice, not the design target. Verdicts unchanged.

### LOW

**L-1 · `chain_map_v1.md` §3.1 + `gap_register_v2.md` §5 — resolves X-8.**
Add one sentence: "structural inputs are from the deterministic, working-tree `structure_register` (not
the FAILED-validation `weakness_register`); both are a curated ~10.3% slice (110/1071) of `designs/`, so
a green structural result is not whole-repo coverage." Add **Crown as #1 cascade sink (189 chains
terminate there)** as a named watch item in the gap prioritization.

**L-2 · `decision_surface_census_v1.md` §3(b) (line 215) — resolves F-6.**
Change "~11-13 (8 core verbs + ~5 expansions + 3 Directive responses)" to "**≈10 standalone** (8 core
verbs + Retain Clerks + Bind the Cells + 3 Directive responses; Survey / Negotiate Quota / Ordenanza are
method-branches of existing verbs, not standalone)." OK verdict robust regardless.

---

## Bottom line

Read as a whole, the set tells one coherent story — **personal-scale resolution quality aggregates up
into country-scale Standing/Legitimacy/Mandate; country-scale mode and collision constrain and discharge
back down** — grounded end-to-end in eight civilizations' endogenous mechanics, with Mandate of Heaven
left as history only and the binding satisfied. The failures were all **at the seams**, and all are
correctable in place: the running engine is far behind the paper (only V2, H1, and a conditional H2 are
genuinely sim-live; the entire Mandate loop is SPEC-ONLY via #136, the scale axis is BROKEN above
territory, and FI has zero dispatch), so **grade every edge on the sim-reality column** and code #136 +
the scale enum + the FI branch to make the two columns agree. Apply the six HIGH fixes (X-1/X-2/X-3 +
F-1/F-2/F-3) before the DESIGN pass binds — above all, **never let the Tetrarchy mechanic reach a player
without its charter-Key enforcement guard** — and the seven MED/LOW reconciliations tidy the rest.
Nothing here executes; the analysis is FILED, each fix stays PROPOSED per CLAUDE.md §1.
