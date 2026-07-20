# Fable Top-of-Stack Audit (v1) — docket + Phase-F reconciliation

## Status: FILED — 2026-07-14 · Lane: IN · ED-IN-0051 (audit layer; allocates no new ED)

**Scope.** Final audit node over the whole `2026-07-13-cross-scale-governance-grounding` docket
**and** its Phase-F three-skeptic reconciliation (`adversarial_review_v1.md`). Every load-bearing claim
was re-verified against the working tree and code directly (Read/Grep on `sim/`, `tools/sim_harness/`,
the ruling spine, indices, ledgers, and the four docket commits `4196723..9b1d16a`), not taken from the
docket's own assertions. This file edits nothing else; corrections are recommended, not applied.

---

## VERDICT: **SOUND-WITH-FIXES**

The docket's substance is genuinely strong — the best-evidenced synthesis artifact in the governance
thread. Every headline BROKEN/INERT/ORPHAN claim survives independent code verification; all six
Phase-F reclassifications are correct on the classification question; the struck citation and all four
evidence corrections are factually right; the decision queue's #1 is the corpus's own stated priority.
No CRITICAL finding. But four MAJOR defects — one substrate-fidelity overreach, one systematic
LIVE-status inflation (which Phase-F itself propagated), one set of false "correction applied" claims
inside the reconciliation, and a dropped needs_jordan item — must be fixed before this docket is safe
to use as a reference surface. None of them overturns a conclusion; all of them are exactly the class
of currency/evidence defect this repo treats as first-order.

---

## §1 · Per-dimension assessment

### D1 — North-star fulfillment: **STRONG, with one framing overreach** (8/10)

- **Every scale is grounded.** The §2 matrix covers individual → settlement → territory → province →
  national (Duchy+Country) → ruling-authority, one non-empty row each, every cell status-tagged and
  GAP-keyed. The Territory row is honestly all-DOCTRINE (verified: only `sim/territory/registry.py
  province_accord()` exists on that rung). Spot-checks of matrix cells all passed (Domain Echo LIVE via
  `parliamentary_bridge.py` ✓; Censure LIVE via `parliamentary_action.py` ✓; Suspicion DOCTRINE-ONLY per
  E11/D6 ✓; L/PS INERT ✓ — zero `.legitimacy`/`.popular_support` use sites anywhere in `sim/`).
- **Up/down/lateral/temporal are real and correctly evidenced.** Bottom-up: Order→Accord floor-mean is
  live code (`sim/territory/settlement.py:68-169`, `registry.py:124`). Top-down: the Two-Tier base case
  (`governance_type_registry_v1 §2.1`). Lateral: correctly flagged as scene-scale-only today
  (`key_echo_armature_v1 §2.3`; `governance_type_registry_v1 §4` says the same). Temporal: OF-3
  deferral accurately carried.
- **Skip-scale and bend-around are real as RULINGS but mis-bound to the armature** (MAJOR-1 below).
  `scale_hierarchy_v1 §5.2/§5.3` genuinely rules cross-scale claiming and the two chain-bypass
  authorities — the nexus behaviors exist in canon. But the docket's repeated equation "diagonal =
  skip-scale / outward = bend-around," presented as "grounded natively in the Key & Echo Armature's
  existing six directions" (README §North-star; `governance_grounding_v1` premise; registry legend), is
  a re-labeling the substrate does not support.
- **Collision-of-stresses (Cut D) is faithfully drawn as design and honestly gapped (E1/E2)** — but
  "LIVE channels… each exist and run" overstates code reality (MAJOR-2b): of the four named radiation
  systems, only MS and CI have writers in `sim/` (`ms_track.py`, `ci_track.py`); Π runs only in the
  `tools/sim_harness` PR#119 engine; **nothing in live code writes `clocks['Strain'|'Turmoil'|'PI']`**
  (writers exist only in the archived `designs/audit/2026-05-14-balance-audit/sim/mc_v4..v14` — likely
  the stale source of the "LIVE" memory).
- Net: the nexus premise is **substantially realized at the design plane and honestly gapped at the
  code plane**, except where the two labeled defects blur that line.

### D2 — Phase-F correctness: **THE GATE WORKED; verified sound, two soft spots** (8.5/10)

Re-verified each reclassification against the cited canon:

| Reclass | Verdict on the verdict | Decisive evidence (re-checked) |
|---|---|---|
| **A4 → CTC** | **Correct** | `propagation_spec_v1 §4.3` *does* author the convergence condition (strictly-contractive `decay()` ∧ D.6-disjoint — read directly); catalog conceded "no external precedent." Authoring, not import. |
| **C3-hardness → CTC** | **Correct — best catch in the gate** | `scale_hierarchy_v1 §3` verbatim: "noisy cascading throughline… **not deterministically**." The register's "hard top-down cascade" premise was a genuine misreading; the gate caught canon, not opinion. |
| **D2 → CTC** | **Classification defensible; its evidence line is wrong** | The `Revolt +1`/faction-elim `+2` feeder pattern is real (`peninsular_strain_v30 §4.1/§3.2`, read directly) — but the gate's "Turmoil/IP (**LIVE**…) already collapses realms" is false in code (no writers; MAJOR-2b). CTC survives on the *ruled prose* pattern; the wording must not. |
| **F3 → CTC (+sliver)** | **Correct** | §2.5a Mastership capital buy-in is RATIFIED (ED-FA-0022/0023 per CURRENT.md); `franchise_v30 §5.1` carries the caste-reform hook; only the *limpieza* temporal-forgery mechanic lacks a hook. |
| **H3 → CTC** | **Correct, cost-framing optimistic** | `propagation_spec_v1` §1 banner + **O.2 is literally titled "engine_clock module contract (retires doc:null/[ASSUMPTION])"** — verified. But "collation + a doc:null flip" understates: O.2's own banner gates the flip on ED-1051, and the `domain_actions` home (`governance_play_redesign_v1 §1.3`) is PROPOSED-not-ratified material, so the flip needs a ruling, not hygiene (the queue's Tier-3 placement absorbs this; the phrase doesn't). |
| **B5-ext → CTC** | **Correct** | `settlement_layer_v30` invokes "**The ROTK principle**" by name (city-state fallback included) and carries the Standing→governance-scope gate plus a Renown/Standing→Scope→"ROTK Parallel" table (line ~1019) — rank→scope coupling is built canon; blast-radius completes it. |
| **C4 → MIXED** | **Defensible but under-argued** | The gate never engaged `sim/personal/contest/wrapper.py`'s own note — "(Stage 4 Consensus is **largely promote-existing** per faction.py)" and the GAMES source "§10 BG-Vote / §7.2" — the strongest textual counter to "not derivable from the built games." A promote-existing path may exist; MIXED may be a mild over-correction. Flag for the C2/C4 author. |

Evidence corrections re-verified: **A1 ~87%** — `sim/tests/test_f7_smoke_oracle.py` docstring confirms
verbatim ("SMALL-N ARTIFACT… Do not tune to it"; golden 37.5/12.5/12.5/37.5; "the only restoration
path, parliamentary_transfer, is never called") ✓. **E3/E11** — `governance_consolidation_v1` confirms
E11 RULED-as-co-requisite (ED-IN-0047), not built ✓. **H1 3/5** — direct header reads confirm exactly:
`fractional_province_ownership`/`faction_succession_split`/`territory_temperaments` carry the
`## Status: CANONICAL` header over a PROVISIONAL body; `franchise` is DRAFT; `valoria_political_hierarchy`
has no `## Status:` line ✓. **E1 strike** — Court-and-Country absent from `research/games/` ✓, and the
catalog's own §4 EU4-disaster discard makes the self-contradiction real ✓; the Imperator Tyranny×AE
replacement is genuinely in G7 ✓. **P-01/12/14 removal** — `canon/02_canon_constraints.md` Violation
Tests are textually thread-op/Coherence-scoped ✓; the category-error finding is right. **Carthage
~700→~500** — the *lesson* (floor-not-zero) is untouched, but the correction itself is contestable:
~500 holds to Augustine (d. 430 CE), while Procopius attests spoken Punic into the 6th c., which makes
the original "~700" defensible too. Low stakes; note, don't relitigate.

**No surviving surface analogy found.** I independently re-checked the surviving imports (Mandate-of-
Heaven two-signal/zaiyi/Zhai Fangjin/devolution-to-warlordism; Bodin war/peace diagnostic; 1615 Kinchū
narabi; ROTK rank-scaled secession; Imperator Tyranny + power-base; millet fission; Cleisthenes
reaggregation; the seven-backfire taxonomy incl. the PNAS Inquisition study) — all are real cross-scale
*mechanisms*, correctly characterized, with the research files' "web-consensus, not hand-verified"
caveat properly attached to exact game constants.

### D3 — Corpus grounding & code claims: **headline claims all true; one-directional LIVE inflation** (7.5/10)

Verified TRUE against code: GAP-A1 (`propose_transfer` defined `parliamentary_transfer.py:101`, zero
callers repo-wide) · GAP-A2 (`compute_accord_echo` defined `domain_echo.py:128`, zero callers) · GAP-B1
(zero L/PS use sites in all of `sim/`; `lps_inert_check` exists at
`tools/sim_harness/adapters/pr119_governance/pr119_structural_gaps.py` — note it scans only 3 files,
but my repo-wide grep independently confirms the stronger claim) · GAP-C4 (`wrapper.py:209` consensus
STUB raising `NotImplementedError`) · ECHO_TRANSPORT default ON (`mc_v18.py:47-56`) · F1/H2 orphanhood
from CURRENT.md (grep-confirmed) · the §9 bonus Legitimacy-buffer collision (`peninsular_strain_v30`
§4.3 "Legitimacy −25" vs `designs/scene/derived_stats_v30.md:297` "Mandate × 20… 0–140" — a genuinely
new, correct find) · read-only compliance (the four docket commits touch only docket files +
`id_reservations.yaml` + `editorial_ledger_in.jsonl`; allocation hygiene correct, IN 51→52).

Found FALSE or inflated (all in the "more live than reality" direction — MAJOR-2, m3, m4 below):
the L/PS→Mandate "LIVE recompute"; Turmoil/Strain/IP "LIVE"; "§5.3 states bypass acts are free"
(silence cited as statement); H2's canonical_sources claim (3 of the 4 "orphans" ARE pinned there —
`canonical_sources.yaml:48,143,233` — and `insurgency_pipeline` is in `mechanics_index.yaml:826,844`;
the orphanhood is CURRENT.md-specific, exactly as H2's *title* says and its fix-text contradicts).
**No fabricated evidence found anywhere** — every formula quoted (Mandate `7T/(T+6)` K=6, ΔLegitimacy
λ-terms, Strictness clamp, National Influence clamp) matches its source verbatim.

### D4 — Cross-file coherence & completeness: **weakest dimension** (6.5/10)

The declared correction-layer pattern ("adversarial_review is authoritative where it conflicts") is
legitimate, but the reconciliation *overstates its own application* (MAJOR-3), the register's summary
arithmetic contradicts its own table (m1), two docs say "five cuts" over a four-cut graph (m2), F6/F7
exist only in queue/review while the register inventory and tally were never extended, and the
mode-domain is 6 values in the registry's own-synthesis row vs 8 in catalog/queue with no cross-note
(m8). Individually small; collectively they mean no single file can be read alone — which the banners
say, but the bodies punish.

### D5 — Decision-queue prioritization: **ranking right; two items fell off the truck** (8/10)

- **#1 L/PS wiring is correctly #1.** Not just the docket's judgment: `scale_hierarchy_v1 §6.4` ("the
  single highest-priority open item in the whole governance/generation thread") and CURRENT.md's
  Settlement/territory row say the same; it re-animates the largest dead-arc family (§5). A pure
  leverage×1/cost ordering could argue #2 first (two one-line call sites vs B1's real build — note B1
  is *not* mere connection: the §1.8 aggregation engine itself is unbuilt, `registry.py:63`'s own
  "Stratum-B work" comment), but leverage-first is defensible and matches the corpus.
- Tiering (unblock-spine → genuine-design-calls → unblocking-rulings → hygiene) is coherent; #17's
  hold on the elect-inward armature direction is exactly right.
- **Defects:** GAP-B3 is missing from the queue entirely, despite `pressure_key_registry_v1 §4`'s
  explicit "handed to … `decision_queue.md` as a `needs_jordan` item" — the three-formula collision
  (which meter feeds Parliament vs Domain Actions) is a real Jordan call D4 alone does not settle.
  GAP-B5 is likewise absent. #3 asks Jordan to "Confirm D4," which is already RULED (ED-IN-0046,
  2026-07-13) — frame as "execute D4 + rule the two valves." The stated formula
  "leverage × 1/cost × novelty" does not literally describe the ordering (Tier 1 is the *lowest*-novelty
  work); the real rule is leverage-dominant — say so.

---

## §2 · Ranked findings

### CRITICAL — none.

No fabricated evidence, no classification that would import a harmful mechanic, no canon violation, no
conclusion-overturning error. This is why the verdict is not MATERIAL-ISSUES.

### MAJOR

**MAJOR-1 · The "native six-direction grounding" re-purposes two armature directions that mean
something else.**
`key_echo_armature_v1 §2.4` defines **diagonal = provenance chains (`causes[]`)** ("causes[]-chained
cross-scale consequence," confirmed by `scale_transitions_v30 §12.1`'s direction table and
`key_substrate_v30.md:84`); **§2.5 defines outward = the rendering surface** (the RR/RG/UR sweep — what
the *player* sees). "Bend-around" appears nowhere in the corpus outside this docket. Yet README,
`governance_grounding_v1` (premise + Cut C), and the registry legend assert "diagonal = skip-scale /
outward = bend-around" as *existing* armature semantics. The underlying behaviors are genuinely ruled
(`scale_hierarchy_v1 §5.2/§5.3`) — the nexus is real — but the substrate binding is invented: bypass
acts and cross-scale claims currently have **no Key types at all** (the registry's own rows say "none
named"). *Fix:* reword the premise to "ruled in §5.2/§5.3, **needing new armature binding**" (diagonal
is at best *adjacent* via emergent `targets[]`/`scale_signature` spans; outward is not applicable);
keep the registry's Skip/Bend column but label it docket-schema, not armature vocabulary (its footnote
gestures at this; README/grounding do not). Missed by all three skeptics — the compliance/wiring lens
should have caught it.

**MAJOR-2 · LIVE-status inflation against the docket's own legend (one instance propagated into
Phase-F).**
(a) `governance_grounding_v1` labels the **L/PS→Mandate aggregation "LIVE recompute/LIVE aggregate"**
(Cut A bullet, Cut B arrow + first bullet, §2 matrix Settlement and National rows, §5 "Mandate
aggregates and re-reads LIVE (§1.8)"). No such code exists: `sim/territory/registry.py:60-65` marks
L/PS "declared but NEVER READ OR WRITTEN… Mandate aggregate is ED-FA-0004 **Stratum-B work**";
`faction_behavior_v30`'s own header says "no Mandate/PS… engine"; the bridge consumes `Faction.L` *as*
Mandate ("pre-LPS-1"), bypassing settlements — which the docket itself states two lines later. Only
Order→Accord is live on that rung. This contradicts the pressure-key registry's correct INERT rows and
the legend's own LIVE definition. (b) `pressure_key_registry_v1 §8` marks **Turmoil/Strain "LIVE" and
IP "LIVE (aggregation)"** — nothing in `sim/` or `tools/` writes `clocks['Strain'|'Turmoil'|'PI']`
(only MS and CI have writers; the sole Turmoil read is `victory.py:73`; writers exist only in the
archived 2026-05-14 `mc_v4..v14`). The same prose-ratified-but-unwired state earns L/PS "INERT" —
the taxonomy is applied inconsistently, always in the flattering direction. Phase-F then *repeated*
the error as D2's evidence ("Turmoil/IP (LIVE…) already collapses realms"). *Fix:* relabel (a) as
"formula ruled in canon; code aggregation unbuilt (inside B1's scope)" and (b) as ruled-prose/BG-live,
sim-unwired (D2's CTC classification survives on the ruled feeder pattern — only its wording changes);
re-check Cut D's "each exist and run" (MS/CI run; Π runs in the harness; Strain/Turmoil/IP do not).

**MAJOR-3 · The reconciliation claims corrections it did not apply.**
`adversarial_review_v1 §3` states the Carthage figure was "Corrected in
`research/theory/internal_polity_precedents_v1.md`" — **provably false**: commit 9b1d16a touches five
files, not that one, and "~700 yrs" still stands there (lines 142-143) and twice in the catalog
(§2 G2, §4). §2 says the P-01/12/14 citations were "**removed**" from B2/E1/E2/G2 — all four remain in
the catalog body (lines ~325/439/460/513), as do the struck Court-and-Country citation (GAP-E1 body)
and the debunked "~87%" line (GAP-A1 compliance, line ~64). The banner-supersession pattern is declared
and legitimate; *asserting application that didn't happen* is not — it is precisely the
claims-vs-working-tree failure mode this repo's anti-fabrication culture exists to catch. *Fix:* apply
the five body edits (Carthage ×3, catalog A1 ~87%, catalog E1 C&C, catalog P-citations ×4 — or reword
the review to "superseded by banner" where body edits are deliberately withheld).

**MAJOR-4 · The needs_jordan surface silently dropped GAP-B3 (and B5); the register was never extended
with F6/F7.**
`pressure_key_registry_v1 §4` (the docket's own centerpiece analysis of the three competing
political-power formulas) ends: "handed to `gap_register_v1.md` / **`decision_queue.md`** as a
`needs_jordan` item." The queue contains no B3 item — D4 retires Mandate-as-collapse-carrier but does
not adjudicate which surviving meter feeds which consumer (Parliament reads at least two of the three
across the corpus, per the registry's own write-up). B5 (rank=blast-radius) is likewise absent from the
queue even though reclassified-CTC peers (D2, C3, A4, H3) all received Tier-3 slots. And GAP-F6/F7
exist only in queue+review — `gap_register_v1.md`'s "every gap" inventory and Summary were never
extended. *Fix:* add B3 (Tier 3: "designate consumers per D4; retire `political_value()`") and B5
(Tier 3/4) rows; append F6/F7 rows to the register.

### MINOR

- **m1 ·** `gap_register_v1` Summary says "~24 gaps… 14 CTC · 8 GG · 2 Mixed"; its own table holds
  **28** IDs = **16 CTC · 10 GG · 2 Mixed**. The catalog's 16/12 and Phase-F's ~21/~6/1 both sum to 28;
  the register's summary is the outlier. Phase-F corrected the catalog's split but missed this. *Fix:*
  restate as 16/10/2 of 28 (30 with F6/F7).
- **m2 ·** README manifest and `gap_register_v1` intro say "**five** graph cuts"; `governance_grounding_v1 §1`
  is titled "The **four** cuts" (A–D). *Fix:* pick one (the §F/§G axes are explicitly not cuts).
- **m3 ·** D2's evidence "`doc:` bypass acts are free" / catalog "§5.3 **states** bypass acts are free" —
  `scale_hierarchy_v1 §5.3` (read in full) is *silent* on cost. Silence ≠ statement; it also changes the
  fix's character (additive, not canon-contradicting). *Fix:* "no cost is specified."
- **m4 ·** GAP-H2's fix ("add the four docs to … `canonical_sources.yaml`") is wrong for 3 of 4 —
  `insurgency_pipeline_v30`, `fractional_province_ownership`, `faction_succession_split` are already
  SHA-pinned there (and insurgency is in `mechanics_index`). Only `franchise_v30` is absent from all
  three indices. The real gap is CURRENT.md rows (+ the H1 header fixes). *Fix:* narrow the wiring text.
- **m5 ·** C4→MIXED never engaged `wrapper.py`'s own "Stage 4 Consensus is **largely promote-existing**
  per faction.py" source note — the strongest counter-evidence to "not derivable." Possible mild
  over-correction; resolve when C2/C4 is authored. Similarly, Carthage "~500" vs "~700" is a coin-flip
  on whether Procopius (6th c.) counts — the review presented a contestable figure as a correction.
- **m6 ·** Queue #3 asks Jordan to "Confirm D4" — D4 is already RULED (ED-IN-0046, 2026-07-13, per
  `governance_consolidation_v1`'s status line). Reframe as "execute D4; **rule the two relief-valves**."
- **m7 ·** "the **13** `domain_actions` verbs" (catalog H3, Phase-F H3) vs the 12 the grounding doc
  lists; `governance_play_redesign_v1 §1.3`'s base menu is 8 with staged additions (§1.1a/§1.3a/b) —
  the count is presentation-dependent; pick one and cite it. Also note the A1 "pure wiring" framing is
  slightly optimistic: the bridge's derived motions are generic two-pole stability motions; routing a
  *transfer* motion needs the CB-gated derivation authored (still CTC — all pieces exist).
- **m8 ·** The registry's own-synthesis mode-domain row is **6** values; catalog/queue recommend **8**.
  No file notes the supersession. *Fix:* one cross-note in the registry row.
- **m9 ·** Grounding §5: "legitimacy only ratchets up" — `faction_behavior_v30 §3.5`'s
  `−λ_violation×score` term does subtract on events; what's missing is *entropy absent events*. Wording.
- **m10 ·** A4 never engages `settlement_layer_v30 §1.8`'s own prior-art claim — "Stage-4 sim
  (2026-05-30): the coupled Mandate↔settlement system stays bounded 0–7 and **converges** over 30
  seasons" — a doc-asserted convergence result for the flagship loop instance (unreproducible today:
  `sim/` lacks the model). The convergence-artifact work (queue #11) should cite and reconcile it.

---

## §3 · What the three skeptics MISSED (explicitly)

All of MAJOR-1, MAJOR-2 (both halves — and Phase-F *repeated* 2b in its D2 evidence), MAJOR-4, and
m1–m4, m6–m10. MAJOR-3 is the reconciliation's *own* defect (false applied-correction claims). The
pattern: the skeptics audited the **catalog's classifications and precedents** rigorously and well, but
nobody re-audited the **graph doc's and registry's status labels against code**, the **queue against
the register's promises**, or the **review's own application claims against the tree**. The
classification/surface-analogy lenses performed excellently; the compliance-**wiring** lens
under-delivered on exactly the wiring half of its name.

**What the skeptics got right (all independently re-verified here):** the six reclassifications (C3's
canon-misreading catch and B5's ROTK-by-name evidence are model adversarial work), the C&C strike, the
auctoritas and anacyclosis downgrades (the dropped §6 caveat is real and was correctly restored), the
P-citation category error, the A1/E3/H1 evidence corrections, F6/F7's verification and re-homing, and
the honest intra-tier flag on elect-inward. The "~21 CTC · ~6 GG · 1 MIX" revised shape — the docket's
honest headline for Jordan — **survives this audit intact**, with the caveat that several "CTC"
cost-framings (B1, H3, A1) understate build/ratification work while remaining correct classifications.

## §4 · Confidence

**HIGH on every named finding** — each is pinned to a specific file/line or a repo-wide grep performed
in this audit (zero-caller checks, clock-writer checks, header reads, commit file-lists, formula
comparisons). **MODERATE-HIGH on completeness** — ~20 of the 65 registry rows were deep-verified
(including all rows the arguments lean on), 5 of ~30 arc IDs, and the precedent corpus was
spot-verified from domain knowledge rather than fresh web research (the research files' own
"web-consensus" caveat stands). A row-by-row registry re-verification could surface further m-class
status drift but is unlikely to move the verdict.

**Bottom line for Jordan:** trust the gap analysis, the classification shape, and the queue's Tier 1-2
— they are real and well-evidenced. Before citing this docket as a reference: apply the four MAJOR
fixes (reword the two direction equations; deflate the LIVE labels on L/PS→Mandate and
Turmoil/Strain/IP; actually apply or honestly re-scope Phase-F's claimed corrections; restore B3/B5 to
the queue and F6/F7 to the register). One editorial pass closes all of it — nothing structural.

---

_Fable-tier final audit, max effort, 2026-07-14. Read-only over canon; this file is the only artifact
written. Verification base: `sim/` + `tools/sim_harness/` greps; `test_f7_smoke_oracle.py`;
`scale_hierarchy_v1`; `key_echo_armature_v1` + `scale_transitions_v30 §12.1` + `key_substrate_v30`;
`propagation_spec_v1` §1/§3/§4; `holonic_container_doctrine_v1`; `governance_consolidation_v1`;
`governance_type_registry_v1`; `settlement_layer_v30`; `faction_behavior_v30`; `faction_politics_v30`;
`franchise_v30`; `insurgency_pipeline_v30` (`designs/world/`); `peninsular_strain_v30`;
`territory_temperaments_v30`; `valoria_political_hierarchy_v30`; `derived_stats_v30`;
`canon/02_canon_constraints.md`; `CURRENT.md`; `canonical_sources.yaml`; `mechanics_index.yaml`;
`id_reservations.yaml`; `editorial_ledger_in.jsonl`; docket commits 4196723, 159f80f, 7436dbe, 9b1d16a._
