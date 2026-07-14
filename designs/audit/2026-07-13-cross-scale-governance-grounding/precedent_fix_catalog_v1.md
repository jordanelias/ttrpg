# Precedent Fix Catalog (v1) — Cross-Scale Governance

## Status: FILED (in progress) — 2026-07-13 · Lane: IN · ED-IN-0051

**Purpose.** The culminating synthesis of the `2026-07-13-cross-scale-governance-grounding` docket: one
**PROPOSED** fix per gap in `gap_register_v1.md` (GAP-A1..H3), drawn from that register's already-decided
two-tier classification, the graph (`governance_grounding_v1.md`), the key census
(`pressure_key_registry_v1.md`), and the three precedent files (`research/games/`, `research/theory/`).
This artifact **catalogs** fixes — it flips no `## Status:` line, wires no inert field, and edits no canon
doc (per the docket brief and CLAUDE.md §2). Currency resolved via `CURRENT.md` (2026-07-13):
`scale_hierarchy_v1` is the ratified hierarchy head; `governance_consolidation_v1` D1–D6 are RULED
(ED-IN-0046/0047); `key_echo_armature_v1` + `propagation_spec_v1` are the ratified substrate; `Field`/`Gauge`
(`governance_type_registry_v1 §4`) is PROPOSED-not-ratified.

**Binding method — classify BEFORE proposing (mirrors `gap_register_v1.md` exactly).**
- **[COMPLETE-THE-CHAIN]** — an unbuilt link in an otherwise-built chain; the fix is **derived from the
  logic of its surroundings** (ED-1050 doctrine). A precedent may appear **only as confirmatory**; no
  foreign mechanic is imported-and-modified.
- **[GENUINE-GAP]** — the surrounding logic does not determine the answer; **only here** is a precedent
  (game / political-theory / historical) cited by its **real cross-scale mechanism**, plus a Valoria-native
  adaptation. Every genuine-gap entry must (a) defend why no chain-completion was available and (b) pass a
  surface-analogy check (a REAL cross-scale mechanism, not a pattern-match).

**Phase-F adversarial gate.** Each **[GENUINE-GAP]** entry carries its Phase-F verdict inline: the
*why-no-chain-completion* defense (against an available chain-completion) and the *surface-analogy verdict*
(REAL vs pattern-match). Chain-completions carry an *is-the-gap-real / chain-completion-correct* verdict.
Tally: **16 [COMPLETE-THE-CHAIN]** (§1) · **12 [GENUINE-GAP]** (§2, incl. the genuine-gap halves of the two
Mixed gaps C3, B5). §3 synthesizes legitimacy/authority across scales; §4 records the cross-cutting rulings
and the explicit surface-analogy discards.

---

## §1 · [COMPLETE-THE-CHAIN] fixes — derived from surrounding logic

*Precedent is confirmatory only. No import. Format: issue → derives-from → wiring → confirmatory precedent →
compliance → verdict.*

### GAP-A1 · faction → named settlement/territory transfer BROKEN
- **Derives from:** `parliamentary_bridge.py` already runs the seasonal §10 vote each Accounting; the
  transfer resolver `parliamentary_transfer.propose_transfer` (CB-gated, vote-wrapped Influence-vs-Legitimacy
  roll) is **CODED-BUT-UNCALLED** (`test_f7_smoke_oracle.py`: "never called"). The won holding re-aggregates
  through the already-LIVE S→P recompute.
- **Wiring:** in `parliamentary_bridge.py`, route a resolved territorial-transfer motion's outcome into
  `propose_transfer` at the accounting boundary; the transferred settlement re-aggregates normally. Connect
  two existing endpoints — no new mechanic.
- **Confirmatory precedent:** CK3 Council named-target task / Stellaris planetary-governor override (G6) — an
  authority resolving directly onto one named node is standard. Confirmatory only.
- **Compliance:** GD-1 (transfer *advances toward* peninsular sovereignty, never triggers it) · holonic
  (Parliament is the ratified bend-around/outward authority, `scale_hierarchy §5.3`; obeys the scripting-drift
  guardrail — touch declared I/O only) · emergence (wires a resolver, scripts no outcome) · no-GM (vote +
  resolver resolve engine-side). Ends the F7 degenerate ~87% single-faction win.
- **Verdict:** gap real (test asserts zero callers); chain-completion correct — 100% adjacent built code.

### GAP-A2 · Accord echo aggregation BROKEN
- **Derives from:** `domain_echo.compute_accord_echo()` exists with **zero callers**; the Accounting boundary
  already invokes `echo_transport` for the faction-stat echo path (ED-SC-0006/0007). The aggregation math is
  written.
- **Wiring:** invoke `compute_accord_echo()` from the same Accounting boundary so settlement-locus scene
  conduct aggregates into Province/Territory Accord, feeding the already-LIVE Strain/IP downstream.
- **Confirmatory precedent:** DF "same variables read by multiple scales — don't invent a parallel ledger"
  (G8) — read existing Order/Accord, add no bookkeeping track. Confirmatory.
- **Compliance:** holonic (bottom-up accumulation, Domain-Echo-shaped, deferred-apply) · emergence (invoke
  existing function, no special-case) · no-GM.
- **Verdict:** gap real (zero callers, code-verified); chain-completion correct.

### GAP-A3 · Territory tier DOCTRINE-ONLY
- **Derives from:** exactly one live aggregation pattern (Order→Accord floor-mean; L/PS→Mandate). `scale_hierarchy
  §3` ruled Settlement→Territory→Province→Duchy→Country. Extend the one live pattern to the ruled tiers;
  `territory_temperaments §3` supplies the population-weighted `aggregate_fn` shape.
- **Wiring:** instantiate Territory as a scale instance with `aggregate_fn` = population-weighted / floor-mean
  and `propagate_fn` = cascade-with-noise (governance-type). **Blocked on `engine_clock` (GAP-H3)** for the
  temporal/ordering spine.
- **Confirmatory precedent:** CK3 de jure drift (G4) — a mid-tier claim lags control, doesn't teleport.
  Confirmatory.
- **Compliance:** holonic (one uniform container shape at the new scale — obeys the shape-divergence
  guardrail, no new dialect) · GD-3 (Territory secession feeds insurgency) · no-GM.
- **Verdict:** gap real (doctrine-only; code has only Settlement↔Province); chain-completion correct but
  **BLOCKED on H3** (engine_clock, itself a genuine gap).

### GAP-B1 · L/PS INERT (100/100) — the headline
- **Derives from:** all four pieces exist — aggregation (LPS-2e W-weighted mean → Mandate), consent-gate
  (`scale_hierarchy §4`), deferred-apply Accounting boundary (`echo_transport` LIVE), and the `Field`/`Gauge`
  shape (`governance_type_registry §4`). The `Settlement` dataclass already carries `legitimacy`/`popular_support`;
  nothing reads them. Cut B: the vote reads `Faction.L` directly, bypassing settlement grain.
- **Wiring:** make the consumers (Mandate, Public-Expectation Strictness, `compliance(L)`, the governance-cascade
  consent-gate) actually read/write the built L/PS fields; route the vote pool through the aggregate, not the
  raw `Faction.L`. **Do NOT import CK3** (gap-register instruction). This is E5 in `governance_consolidation_v1`.
- **Confirmatory precedent:** Vic3 legitimacy-loop, EU4 estate loyalty (band + drift), CK3 two-track opinion
  (noble Standing vs popular L/PS distinct), Frostpunk twin-gauge (L≠PS), FP2 Fervor (per-settlement, not one
  national scalar). All confirmatory.
- **Compliance:** holonic ("behaviour is bottom-up and emergent" — settlement acceptance produces the faction
  consequence) · GD-2 (L/PS-driven threat response) · GD-3 (defiant-governor → faction-emergence) · emergence
  (revolt/Recall arcs emerge from the local consent rule — the anti-scripting-drift exemplar: never write
  global state to force the outcome) · no-GM (engine adjudicates whether an imposed type sticks). Re-animates
  the entire governance-consent arc family.
- **Verdict:** gap real (`lps_inert_check` 100/100, named single highest-priority open item); chain-completion
  correct — DF "don't invent a parallel legitimacy ledger" is the doctrine backing.

### GAP-B3 · Three competing "faction political power" formulas
- **Derives from:** D4 (`governance_consolidation_v1`, RULED) already determines the direction — Mandate
  retired as collapse carrier, **kept** only as the renamed faction/parliamentary meter; `political_value()`
  flagged SUPERSEDED-PENDING-REWRITE (`scale_hierarchy §6`); franchise-weighted National Influence is the
  Domain-Action roll pool. One reconciliation determined by a ruling, not three independent gaps.
- **Wiring:** designate the surviving meters per D4 (renamed Mandate = parliamentary tally; National Influence =
  Domain-Action pool); execute the tracked `political_value()` retirement; state which consumer reads which;
  register the collision resolved.
- **Confirmatory precedent:** EU4 Estate Influence saturating cap (G2) — one saturating meter, not three.
  Confirmatory.
- **Compliance:** holonic (single shape — removes a shape-divergence instance) · no-GM.
- **Verdict:** gap real (three live incompatible formulas, key-registry §4); chain-completion correct —
  executes a ruled reconciliation (D4), imports nothing.

### GAP-B4 · ΔLegitimacy has NO decay term
- **Derives from:** OF-3 `decay()` is the corpus's own deferred substrate function every "NONE — GAP" key
  points to; the `Field` proposal makes `decay_fn` required; MS (hysteresis-and-falloff) and Π (homeostat
  clamp) are two working templates (`governance_type_registry §2.7/§4`). `faction_behavior §3.5` is additive-only
  with an uncapped `+λ×seasons_in_role`.
- **Wiring:** add a `−λ_decay·(L − baseline)` mean-reversion/entropy term sourced from the generic `decay_fn`,
  parameterized off the MS/Π templates. A chain-completion of the deferred substrate, not an import.
- **Confirmatory precedent:** Anacyclosis (Polybius, regime decay), Old World cognomen-decay (50%→…→10%), EU4
  Horde Unity (constant decay, feed-or-crisis). The theory doc states it outright: "precedent is *confirmatory*,
  the fix is a chain-completion."
- **Compliance:** holonic (the temporal/dissipation armature direction, already named) · emergence
  (decline-and-fall arcs emerge from entropy) · no-GM. Re-animates regime-cycle arcs (with B2).
- **Verdict:** gap real (explicitly flagged, no decay term); chain-completion correct — OF-3 is the corpus's
  own deferred function.

### GAP-C1 · Two senses of "governance type" CONFLATED
- **Derives from:** the manager-type enum is built and canon-enumerated (7-way {Church, Guilds, Ministry,
  Löwenritter, RM, Wardens, Niflhel}, `settlement_layer §3.3`); the *mode* taxonomy is the empty palette (C2).
  Split WHO governs (built FLAG) from HOW decisions are made (the decision-procedure).
- **Wiring:** in `scale_hierarchy §3` / `governance_type_registry §2.1`, formally separate `manager_type`
  (built) from `governance_mode` (C2's FLAG domain); the cascade imposes a manager-type; the mode governs the
  decision-procedure inside it.
- **Confirmatory precedent:** Mandate-of-Heaven "Legalism-under-Confucianism" form(ideology)-vs-function
  (admin-logic) split (legitimacy §1) — a real precedent that the imposed form doesn't guarantee the function
  beneath. Confirmatory.
- **Compliance:** holonic (removes a conflated key — clean shape) · no-GM.
- **Verdict:** gap real (`scale_hierarchy §3` mixes the two); chain-completion correct — split derives from the
  built manager enum; the mode *side* depends on C2 (genuine-gap).

### GAP-C4 · Mode ↔ deliberative-game binding; Consensus game STUB
- **Derives from:** each `governance_mode` selects its resolving contest-game (Agôn WIRED / Negotiation /
  Inquiry / Consensus STUB); `wrapper.py` GAMES already carries a `consensus` slot that raises
  `NotImplementedError`. The binding is derivable from the mode taxonomy; `internal_polity §A` gives the
  mode→game map directly.
- **Wiring:** build the declared Consensus stub (roster + Holdout clock + frivolous-block antibody + a 3-state
  assent/stand-aside/holdout per Quaker practice); wire each mode value to its resolver; some modes correctly
  resolve to **no game** (fiat = Directive FLAG).
- **Confirmatory precedent:** `internal_polity §A`'s mode→game bindings (Haudenosaunee/Quaker/Gadaa consensus)
  are the design reference for the stub's internals — this borders C2's genuine-gap import, so it is cited but
  held confirmatory: the *slot* and the *requirement* are corpus-native.
- **Compliance:** holonic (one of the four uniform contest-games, no new dialect) · emergence · no-GM (the
  Consensus game resolves engine-side).
- **Verdict:** gap real (STUB raises `NotImplementedError`); chain-completion correct for the **binding**
  (derivable) and for building a **declared** stub; its mode *domain* depends on C2.

### GAP-E3 · Collapse-is-a-dial (recovery/decay) partial
- **Derives from:** E11 (symmetric suspicion-reduction, ED-IN-0047) exists; E7 (systemic recovery) named;
  Goldenfurt's bidirectional Π restoring term `sign(3−Π)·min(1,|3−Π|)` (CG-1) is designed-not-ported
  (`governance_consolidation §3`). Generalize these existing counters into one anti-cascade dampener (part of
  the OF-3 `decay_fn` work).
- **Wiring:** lift E11's compliance-decay + Goldenfurt's Π restoring term into a substrate-level dampener; every
  collapse track gets a recovery counter.
- **Confirmatory precedent:** RimWorld anti-cascade dampener + DF 15-year tantrum-dampening (G7) — collapse is a
  DIAL, not a free byproduct; Tokugawa *murauke* (settlement-internal fiscal self-aggregation halts a collision
  at the settlement) confirms a bottom-up dampener. Confirmatory.
- **Compliance:** holonic (temporal dissipation) · emergence (recovery is tunable, not scripted) · no-GM.
- **Verdict:** gap real (E11 exists, not systematized); chain-completion correct. **Bundle note:**
  `governance_consolidation §6.7` — E1 must land bundled with E3+E7 (Phase P not greenlit for E1 alone).

### GAP-F1 · `franchise_v30` ORPHAN through every currency layer
- **Derives from:** the caste→territory→national-power cascade (Franchise 0–5) is fully specified in
  `franchise_v30` but absent from `CURRENT.md`, `canonical_sources.yaml`, `mechanics_index` and predates PP-726
  nomenclature. Re-index + reconcile. (H1/H2 are the currency-hygiene siblings.)
- **Wiring:** add `franchise_v30` to the `CURRENT.md` subsystem table + machine indices; reconcile Territory-tier
  nomenclature against PP-726's now-superseded "Territory = Settlement" (now Settlement→Territory→Province per
  `scale_hierarchy`); flip DRAFT→its true state (execution is the per-lane follow-on, not this docket).
- **Confirmatory precedent:** `internal_polity §B` — territory-as-unit-of-weight is historically well-founded
  (guild/borough charter holds the franchise; Roman century is the counting unit); ±1 reapportionment matches
  real weighted-bloc evolution. Confirmatory.
- **Compliance:** holonic (re-index into the one currency surface — no parallel index) · no-GM.
- **Verdict:** gap real (ORPHAN, code-verified absent); chain-completion correct — re-index a real, fully-specified
  mechanic.

### GAP-F2 · Caste cross-scale cascade under-wired
- **Derives from:** caste keys exist — composition VECTOR (`faction_politics §3.1`), rank-gate FLAG (§3.2) — plus
  the franchise caste-gradient (`franchise_v30 §5`). The cascade is unwired: settlement caste-composition →
  territory advancement → national franchise-suppression.
- **Wiring:** instantiate a caste-composition `aggregate_fn` (population-weighted, parallel to temperament) at
  settlement→territory→province; connect to the franchise Shift Triggers (§5.1).
- **Confirmatory precedent:** `internal_polity §B` — jati regional-inconsistency; sanskritization as the
  group-scale reclassification home for `franchise §5.1`'s open "Caste reform (TBD)". Confirmatory (the
  *circumvention* import is F3, genuine-gap, kept separate).
- **Compliance:** holonic (bottom-up aggregation of a demographic VECTOR — Jordan's "demographics" example) ·
  GD-3 (caste-suppression feeds intrapopulation conflict → insurgency) · no-GM.
- **Verdict:** gap real (personal-scale only); chain-completion correct — wire from existing caste keys +
  franchise gradient.

### GAP-F4 · Intrapopulation-conflict → fracturing under-integrated
- **Derives from:** `insurgency_pipeline_v30` (the **GD-3-canonical** spine) + `faction_succession_split_v30`
  exist but are ORPHAN-vs-CURRENT; the two-stage split resolver (dice = who-leads, gap G = whether-splits) is
  specified. Re-index; wire the fracturing engine under the causal-justification constraint (Jordan ruling on
  P11-vs-P2).
- **Wiring:** re-index the two docs into `CURRENT.md`; wire P11/P2 (allegiance vs owner) fracturing with in-world
  causal justification; adopt the two-stage split resolver. **Flag** the settlement-generator P11/P2 vs canon
  P-11/P-02 namespace collision (`internal_polity §B`) to the `governance_type_registry` owner.
- **Confirmatory precedent:** Machiavelli's two humors confirm the parliamentary-vent asymmetry
  (`insurgency_pipeline §5.2`) is sound. Confirmatory. (The *recognition-fission* and *reaggregation* resolution
  registers are genuine-gap adds — see §3 / F5.)
- **Compliance:** GD-3 (this **is** the revolt→insurgency→faction pipeline) · holonic (bottom-up emergence —
  "behaviour is bottom-up") · no-GM (engine emerges factions; no player consent, per GD-3).
- **Verdict:** gap real (ORPHAN vs CURRENT); chain-completion correct — wires the GD-3 spine; the
  causal-justification constraint is a real authoring gate.

### GAP-F5 · Fracture RESOLUTION absent
- **Derives from:** `fractional_province_ownership`'s Fragmentation Check (recurring hold/collapse roll) +
  Consolidation Domain Action are orphaned-but-real; `scale_hierarchy §5.2` rules independence-at-any-tier with
  no resolution roll. Adopt the orphaned mechanics; anchor dissolution on the RAND-grounded 4-path model
  (sponsor-withdrawal modal).
- **Wiring:** adopt the Fragmentation Check as the recurring resolution roll for an independence-eligible tier;
  wire Consolidation as the reversing Domain Action; ground dissolution modes on the RAND 4-path model.
- **Confirmatory precedent:** `internal_polity §B` — Dorr "failure of nerve" (5th flavor), Ciompi
  post-recognition reversal, "Concession Residue" sub-flag all **extend** the RAND base. Confirmatory here; the
  *new resolution registers* (millet recognition-fission, Cleisthenes reaggregation) are genuine-gap imports
  carried in §3.
- **Compliance:** GD-3 (fracture resolution feeds the insurgency→faction lifecycle) · holonic (bottom-up) · no-GM.
- **Verdict:** gap real (no resolution roll); chain-completion correct — adopt orphaned Fragmentation Check +
  Consolidation; genuine-gap resolution registers handled in §3.

### GAP-G1 · Orthodoxy↔heresy↔non-orthodoxy not a nexus axis
- **Derives from:** the Church keys (CI / Piety Track / Excommunication / Inquisition / Heresy-Lifecycle / RDT)
  exist; the PT×SW→CI aggregation is LIVE. Lift them into the registry as an **ideological-consent axis parallel
  to L/PS**: individual belief → settlement doctrinal composition → territory Piety → national CI.
- **Wiring:** register the belief→doctrinal-composition→PT→CI cascade as a parallel consent axis in the
  pressure-key registry (PT is already bottom-up-source-of-CI and top-down-target of CI's Ascendant band — a
  built collision shape).
- **Confirmatory precedent:** `internal_polity §C` — Investiture→Concordat "split a contested resource into two
  non-competing channels" (extends the T7 advowson finding). Confirmatory. (The **millet/dhimmi** non-orthodox
  *membrane* PT doesn't model is a genuine-gap sibling — reuse FA-8 Protected-Tributary's shape; carried in §3.)
- **Compliance:** holonic (a parallel axis, same shape as L/PS — reuse, not a new dialect) · no-GM. **Register
  nuance:** the axis models *institutional* consent (parallel to L/PS), **not** moral valence — consistent with
  the no-alignment principle (P-04's spirit); it never frames belief in the monstrosity/moral register (P-02/P-04).
- **Verdict:** gap real (keys exist, not integrated); chain-completion correct — lift existing Church keys into
  the registry.

### GAP-H1 · CANONICAL header vs PROVISIONAL/DRAFT body (5+ docs)
- **Derives from:** currency-hygiene across `franchise`, `fractional_province_ownership`,
  `faction_succession_split`, `territory_temperaments`, `valoria_political_hierarchy`. `CURRENT.md` + the
  merge-ratifies-by-default convention (ED-1094) are the authorities.
- **Wiring:** reconcile each doc's `## Status:` header against its body, resolving via `CURRENT.md`. **This docket
  does not flip status** (brief constraint) — it catalogs the reconciliation; execution is the per-lane follow-on.
- **Confirmatory precedent:** none (pure hygiene).
- **Compliance:** holonic (currency discipline — CLAUDE.md §1/§4, versioning≠currency) · no-GM (n/a).
- **Verdict:** gap real (header/body mismatch, doc-verified); chain-completion correct.

### GAP-H2 · Cited/pinned docs ORPHAN from CURRENT.md
- **Derives from:** `franchise`, `fractional_province_ownership`, `insurgency_pipeline`,
  `faction_succession_split` are relied-on but unindexed. Sibling of F1/F4's re-indexing.
- **Wiring:** add the four docs to the `CURRENT.md` subsystem table + `canonical_sources.yaml`.
- **Confirmatory precedent:** none.
- **Compliance:** holonic (single currency surface — no parallel ledger) · no-GM (n/a).
- **Verdict:** gap real (relied-on but unindexed, code-verified); chain-completion correct.

---

## §2 · [GENUINE-GAP] fixes — imported-and-adapted, adversarially defended

*Format: issue → precedent + real cross-scale mechanism → Valoria adaptation → why-no-chain-completion →
surface-analogy verdict (Phase-F) → compliance.*

### GAP-A4 · Cross-tick convergence UNPROVEN
- **Precedent + mechanism:** **no external precedent** — the termination artifact of the holonic doctrine
  (ED-1083 §4: aggregate-up/distribute-down **+ a convergence proof**). `propagation_spec §4` proves per-tick /
  per-cascade termination only (TERMINATION-ONLY); D.6 shows an up/down hop can double-count into a bounded
  oscillation. The needed "mechanism" is a formal contraction/over-damping condition, not a game import.
- **Valoria adaptation:** author the cross-tick convergence condition as a contraction on the
  aggregate-up∘distribute-down composite, using the OF-3 `decay_fn` as the damping term (strong enough to
  contract, not to over-damp), grounded on the D.6 disjointness rule (is the down-write disjoint from the
  up-read?). Ties to E1.
- **Why no chain-completion:** `propagation_spec §4` proves termination and *explicitly does not* extend to
  cross-tick convergence; the surrounding logic does not imply it. Holonic doctrine §1 names non-termination
  "the scariest runtime risk" and the highest-value unauthored canon.
- **Surface-analogy verdict:** **REAL / N/A** — a formal-mathematical gap, not a mechanism-analogy; the
  "precedent" is internal doctrine (ED-1083 §4). No surface-analogy risk.
- **Compliance:** holonic (this **is** the propagation-spec's deferred §4 convergence guarantee) · determinism
  (seeded replay) · no-GM. Fable/opus-tier authorship per CLAUDE.md §10.

### GAP-B2 · Mandate has no withdrawal/collapse path
- **Precedent + mechanism:** **Mandate of Heaven (*tianming*)** — the archetype. Collapse is a **conjunction of
  two independent signals** (material famine-signal + interpretive portent-signal, Dong Zhongshu's *zaiyi*),
  whose real output is a **cross-scale TRANSFER of power, not a stat flip** (the Han fell as suppression forced
  the center to devolve military authority to regional governors who never returned it → warlordism). Two
  mechanically-distinct relief valves: **(1) scapegoat-the-subordinate** — a bend-around routing the hit off the
  un-blamable apex onto a named appointee at the cost of *their* standing/office/life (Chancellor Zhai Fangjin's
  7 BCE suicide); **(2) ruler self-reproach** — a costly signal spending the *ruler's own* resource (Emperor
  Wen's edict). Contestable, not automatic (Xunzi: Heaven is "constant and amoral").
- **Valoria adaptation:** D4 already retires the `round(7T/(T+6))` carrier → floor-avg Order + province
  fracturing + Standing Keys. The genuine-gap layer is the **interpretive/withdrawal overlay**: a Mandate-collapse
  event fires on the **two-signal collision** (E2), outputs **power devolution** (national → province/territory,
  reusing the A1 transfer resolver + F5 fracture-resolution), and exposes the two valves as costed actions —
  scapegoat (a bend-around onto a named appointee, spending *their* Standing) and self-reproach (spending the
  ruler's own Mandate/Treasury). A court social-contest scene adjudicates whether the disaster "counts" (Xunzi
  contestability); a rival can *declare* a disaster a legitimacy-sign as a political move.
- **Why no chain-completion:** `settlement_layer §1.8` is monotone-saturating with no withdrawal term; D4 retires
  it but the surrounding logic yields only a lower floor-avg — the interpretive/withdrawal collision + devolution
  + valves are a mechanism the corpus never implied. The legitimacy doc is explicit: "whichever mechanic carries
  collapse needs an interpretive/portent layer, not just a lower floor-avg."
- **Surface-analogy verdict:** **REAL** — unusually strongly attested (founding-text *Shangshu* → Qing; named
  carriers: Censorate remonstrance, Zhai Fangjin). **FALSE-FRIEND FLAG:** it shares only the *name* with Valoria's
  `Mandate` stat — import the *structure* (two-signal + devolution + valves), never conflate with the formula.
- **Compliance:** P-14/P-01 (a Mandate crisis fires material + interpretive + actual consequence together — the
  two-signal collision **is** inseparability at governance scale) · GD-3 (devolution → new holders → emergence) ·
  holonic (top-down interpretive ∧ bottom-up material — the outward + accumulation directions) · no-GM (court
  scene + costed valves, never GM fiat). **§3 headline.**

### GAP-C2 · Governance-mode taxonomy under-specified
- **Precedent + mechanism:** **Aristotle regime types; Athens sortition; Roman *comitia*; consensus polities**
  (Haudenosaunee / Quaker / Gadaa / *shūrā*); Venice councils; Chinese examination. The real mechanism: a
  governance-**mode** is a decision-procedure FLAG that selects **which contest resolves a tier's business** —
  and some modes correctly resolve to *no game* (fiat = a Directive FLAG; the contest is displaced to
  Standing/Succession machinery).
- **Valoria adaptation:** the recommended **8-value `governance_mode` FLAG domain** (`internal_polity §A`),
  filling the empty palette in `governance_type_registry §2`:

  | value | resolves via | start-active vs latent |
  |---|---|---|
  | AUTOCRATIC_FIAT | none (Directive FLAG) | start-active (Crown default) |
  | ROYAL_COURT_APPOINTMENT | none (Directive per link; hostage-kin/Court-Attendance) | start-active |
  | OLIGARCHIC_COUNCIL | Agôn on a narrow peer roster (+ elect-inward sub-committee) | start-active |
  | LANDHOLDER_FRANCHISE | Agôn, weighted blocs, + early-termination-on-majority | start-active / reform-reachable |
  | DELIBERATIVE_ASSEMBLY | Agôn (mass) + sortition roster; Inquiry as retroactive legality | latent/emergent only |
  | CONSENSUS_UNANIMITY | Consensus mode (+ 3-state assent/stand-aside/holdout) | start-active (clan/tribal/religious) |
  | NEGOTIATED_ESTATES | Negotiation (BATNA/ZOPA + bound-mandate win-set) | start-active (Country/Duchy) |
  | MERITOCRATIC_BUREAUCRATIC | Inquiry-as-composition + anti-capture "no home-province posting" | latent (blocked on ED-FA-0018) |

  Property-class / sortition / acclamation are **PARAMETERS inside a mode**, not modes.
- **Why no chain-completion:** the corpus names the *slot* (a blank governance-mode row, this-registry's-own-
  synthesis) but no single canon doc enumerates the closed domain; the built manager-type enum answers WHO
  governs, not the decision-procedure. The taxonomy must be imported from regime-theory.
- **Surface-analogy verdict:** **REAL** — genuine decision-procedures with distinct cross-scale mechanics
  (sortition roster vs weighted bloc vs unanimity-holdout). Guard: modes are procedures, **not palette-swaps** —
  Machiavelli's *grandi/popolo* gives each a failure-mode signature (elite-satisfying → peer-coup risk;
  populace-satisfying → PS volatility). Solon→Cleisthenes is a real crisis-driven mode-flip.
- **Compliance:** holonic (a top-imposed FLAG selecting a bottom-up contest — "structure top-imposed, behaviour
  bottom-up" exactly) · GD-1 (modes are tactical leverage toward the one victory, never alternate win-paths) ·
  no-GM. **§3 covered.**

### GAP-C3-hardness · is the type cascade too HARD? (Mixed — hardness half)
- **Precedent + mechanism:** **CONVERGENT NEGATIVE FINDING** (Imperator / Stellaris / EU4 / ACOUP) — a top
  tier's government *type* forces a matching type onto the tier below in **none** of them. A hard, continuous,
  identical-type top-down cascade is genuinely NOVEL with no clean port. The nearest REAL precedent is **CK3
  Administrative — uniform broadcast + local attenuation**, which grounds the *does-it-stick* chain-completion
  (chain-completed by B1), confirmatory.
- **Valoria adaptation:** replace "force an identical type down" with CK3-Administrative **uniform broadcast +
  local L/PS attenuation**; model the cascade as the corpus's own *noisy-weighted* imposition where L/PS gates
  whether it sticks, not a hard identical-type copy. EU4 Republican Tradition (support runs out → the mode
  itself flips) and CK3 de jure drift (claims lag control) supply the softening. **Reconsider the hardness.**
- **Why no chain-completion (hardness half):** the surrounding logic (`scale_hierarchy §3`, a hard cascade gated
  by inert L/PS) is exactly what's in question — "how hard should it be" can't be derived from the doc asserting
  it's hard. The external negative finding is required to justify softening. *(The does-it-stick half **is** a
  chain-completion, resolved by B1 — this Mixed gap's chain half lives there.)*
- **Surface-analogy verdict:** **SURFACE-ANALOGY DISCARD** for the hard identical-type cascade — it must **not**
  be pattern-matched to any game's "government type" (none cascade). Model a floor/attenuation. CK3 Administrative
  is **REAL** for the does-it-stick half.
- **Compliance:** holonic ("structure top-imposed but attenuated bottom-up" **is** the CK3-Administrative shape,
  and the doctrine's own statement) · emergence (whether it sticks emerges from L/PS, not scripted) · no-GM.
  **§4 surface-warning.**

### GAP-D1 · Monarch + Parliament both bypass, UNRANKED
- **Precedent + mechanism:** **Bodin's indivisible sovereignty** — splitting law-giving power between ≥2 agents
  with no precedence is a category error producing anarchy "worse than the cruelest tyranny" (written amid the
  French Wars of Religion — the exact two-unlimited-sovereigns config `scale_hierarchy §5.3` creates).
  Diagnostic: sovereignty sits with whoever can bindingly declare war/peace without sign-off. Two real
  resolutions: **(1) nest one inside the other** (Tokugawa auctoritas/potestas; English constitutional monarchy —
  one closure point though two bodies act); **(2)** a **named designed crisis mode** (English Civil War).
- **Valoria adaptation:** surface both to Jordan (decision_queue). **(1) Nest:** borrow legitimacy once at the
  apex (Monarch = auctoritas/ratification), run an independent potestas chain beneath (Parliament/administration)
  that never re-touches the source, **asymmetric-and-enforced** (Tokugawa is safe *only because* one is coercive,
  one ratification-only-with-a-leash). **(2) Crisis mode:** the Monarch-vs-Parliament collision is a named
  constitutional-crisis arc, adjudicated by a Bodin war/peace test for where sovereignty really sits.
- **Why no chain-completion:** `scale_hierarchy §5.3` gives **both** an unconditional bypass with explicitly **no
  precedence** — the surrounding logic *contains* the contradiction and cannot resolve it. Ranking requires a
  sovereignty theory the corpus lacks.
- **Surface-analogy verdict:** **REAL** (sharpest actionable finding) — Bodin's theory exists precisely to forbid
  this configuration, dated to the crisis it caused; the war/peace test is a real diagnostic; the Tokugawa split
  is a co-signed, dated instrument (1615 Kinchū narabi). Not a pattern-match.
- **Compliance:** holonic (the outward/bend-around direction — ranking the two chain-exempt authorities makes it
  well-formed) · GD-1 (crisis mode is leverage, not a win-path) · no-GM (the crisis resolves by contest). **§3.**

### GAP-D2 · Bypass has no metered cost
- **Precedent + mechanism:** **Imperator Tyranny** — the ruler forces an action past the Senate (40–60% support)
  by **spending Tyranny, which feeds the same civil-war-fragility gauge**. The strongest metered-cost-bypass
  precedent: bypass carries a quantified cost against the secession-risk pool, never free. Cross-validated,
  load-bearing (G6).
- **Valoria adaptation:** meter each Monarch/Parliament bypass against the **same fragility/secession-risk pool**
  the intrapopulation-conflict/fracture system reads (Turmoil/IP + the F5 Fragmentation-Check inputs). A bypass
  raises fragility; enough bypasses cross the (size-scaling, per Imperator) secession threshold. Couples D2 to D1
  (a metered bypass is also a rankable one) and to the fracture engine (F4/F5).
- **Why no chain-completion:** `scale_hierarchy §5.3` states bypass acts are **free**; nothing in the surrounding
  logic supplies a cost — the cost model must be imported.
- **Surface-analogy verdict:** **REAL** — the genuine cross-scale coupling is that the cost feeds the *same* pool
  that resolves secession; not a pattern-match to a generic "action-point cost."
- **Compliance:** holonic (couples the outward/bend-around direction to the bottom-up fragility accumulation) ·
  GD-3 (bypass-driven fragility feeds insurgency) · no-GM. **§4 (bypass-metered ruling).**

### GAP-E1 · Collision primitive not unified
- **Precedent + mechanism:** **Mandate-of-Heaven two-signal resonance** + **Dwarf Fortress mandate-clock / EU4
  Court-and-Country** (a top-down obligation ∧ a bottom-up production-collapse colliding in the *same tick*) +
  **Frostpunk 2 Whiteout** (one authored event spikes 4+ gauges/scales in parallel). The real mechanism: a
  collision is the **resonance of an independent top-down signal and an independent bottom-up signal arriving
  together**, not one accumulator cascading.
- **Valoria adaptation:** unify MS distance-falloff + Calamity radiation + Peninsular Strain + Π homeostat into
  **one collision primitive**: a shock emits an independent top-down arm (Calamity/MS radiation, distance-banded)
  AND triggers a bottom-up arm (Π/Order collapse → Accord → Strain/IP); a Mandate-tier event fires only on the
  **resonance** of both arriving at intermediate scales in one Accounting. Hand-author specific
  Whiteout-style collision events on top. Resolve the D.6 double-count via the disjointness rule + OF-3 damping
  (ties to A4).
- **Why no chain-completion:** the four radiation systems exist with **no shared primitive**; true *parallel*
  collision (many scales hit independently in one tick) is a Valoria departure — the surrounding logic gives four
  separate systems, not their unification.
- **Surface-analogy verdict:** **REAL** for the two-signal resonance (Mandate-of-Heaven) and the authored
  multi-gauge event (FP2 Whiteout). **SURFACE-ANALOGY DISCARD:** EU4 disasters (accumulate-then-cascade through
  *one funnel*) are **not** true parallel collision — do not port them as the primitive. Build on
  MS/Calamity/Strain/Π.
- **Compliance:** P-01/P-14 (a collision firing top-down ∧ bottom-up in one tick **is** inseparability — the two
  arms are the co-moving auto-effects) · holonic (two armature directions composed) · no-GM (resonance detected
  engine-side). **§3/§4.**

### GAP-E2 · Collision needs two independent signals
- **Precedent + mechanism:** **Mandate-of-Heaven *zaiyi***: a legitimacy crisis is the **conjunction** of (a) an
  elite/court channel (an astronomical portent — *no geographic locus*, arriving top-down independently) and (b)
  an independent popular channel (regional suffering read from below). A bad harvest *alone* is a settlement
  problem; a portent *alone* is court ritual; the crisis is **both at once**. Contestable (Xunzi) — a court scene
  adjudicates whether it "counts."
- **Valoria adaptation:** a Mandate-tier event **requires** a material threshold (Order/Dearth/Π at a settlement)
  **AND** an independently-arriving interpretive trigger (portent / rumor / interdict — celestial, no locus,
  top-down). A court social-contest scene adjudicates whether the conjunction counts (Xunzi contestability); a
  rival can *declare* a disaster a legitimacy-sign as a costed political act. Implements E1's two-signal
  requirement at the event grain; pairs with B2 (the withdrawal output).
- **Why no chain-completion:** nothing in the corpus models a two-signal requirement — a famine is a lone
  settlement Order event; the interpretive channel does not exist. The surrounding logic cannot produce a
  conjunction it has no second term for.
- **Surface-analogy verdict:** **REAL** — the *zaiyi* two-channel structure is documented (Dong Zhongshu; Xunzi's
  naturalist counter). The genuine cross-scale mechanism is the **independence** of the arms (a portent with no
  geographic locus arrives independently of the material signal). Not a pattern-match.
- **Compliance:** P-01/P-14 (material + interpretive conjunction is co-movement across the actual + epistemic
  dimensions — governance-scale inseparability) · emergence (the crisis emerges from two independent local
  signals, not a scripted flag) · no-GM (the court scene adjudicates contestably; "declare it a sign" is a costed
  social-contest move, not GM fiat). **§3.**

### GAP-F3 · Caste circumvention general mechanism absent
- **Precedent + mechanism:** three historical routes (`internal_polity §B`): **wealth-buyout** (Solon/equestrian
  property threshold — a coexisting open-wealth axis beside closed-birth); **forged/purchased proof** (*limpieza
  de sangre* — gameable; forged/purchased proof was normal; temporal cross-scale — genealogy back in time);
  **group-scale cultural reclassification** (*sanskritization* — a settlement/territory multi-season process). The
  real mechanism: capital/social-collateral routes *around* a caste gate without removing it.
- **Valoria adaptation:** generalize the one existing instance (§2.5a Guild Entry/Mastership Forks) into a
  circumvention layer, each route at its correct scale: **(1) wealth-buyout** = a capital-gated bypass of a caste
  rank-gate (parallel to the Guild buy-in path); **(2) forged/purchased proof** = hang on the existing
  Conviction-Scar/exposure machinery (limpieza's temporal accrual matches Scar accumulation); **(3)
  sanskritization** = the group-scale home for `franchise §5.1`'s open "Caste reform (TBD)" — a
  settlement/territory reclassification, **not** the PC-scale mechanic. *devshirme*/*novus homo* are confirmations
  of built mechanics (citation-patches).
- **Why no chain-completion:** the corpus has **only** the sponsorship-Disposition-burn instance (§2.5a); the
  hard caste gate (§3.2) has no route around it. Circumvention must be imported.
- **Surface-analogy verdict:** **REAL** — *limpieza* is the closest total-system analog (post-conflict,
  ancestry-based, institutional, investigation-based, gameable); sanskritization is a genuine group-scale
  reclassification. Guard: three *distinct* routes at three *distinct* scales — not a flat "buy your way up."
- **Compliance:** holonic (each route at its correct scale — PC wealth, PC-temporal proof, settlement-scale
  reclassification — no shape divergence) · GD-3 (blocked circumvention → intrapopulation conflict) · no-GM.

### GAP-G2 · Cultural suppression/genocide as a costed consequence-bearing action
- **Precedent + mechanism:** the **backfire structure** — suppression backfires by **seven distinct, nameable
  mechanisms** (`internal_polity §C`): **(1) Resource/Treasury** (skilled-population flight — Huguenot exodus;
  1492/1609 expulsions); **(2) Legitimacy-contagion** (reputational hit with untouched third parties —
  Magdeburg/Rome sack); **(3) Quiet trust-decay** (corrodes cooperation for generations, *no revolt, no trigger*
  — PNAS Inquisition study → ambient Church-Attention-Pool decay); **(4) Identity-hardening/non-reintegration**
  (Chalcedonian schism; kakure kirishitan); **(5) Identity-migration** (converts a militarily-solvable problem
  into a militarily-**unsolvable** one — hands it from Conquest/mass-battle to Fieldwork/Investigation — *most
  novel*); **(6) Sponsor/insurgency** (Reformation/Camisards/Cathars → couple to the Insurgency Pipeline's
  existing sponsor mechanic, ED-881); **(7) No-off-ramp ratchet** (an uncorrectable-keyed track — ancestry/
  limpieza — must escalate to expulsion; a *belief* track must keep its recant off-ramp reachable).
- **Valoria adaptation:** a suppression Domain Action (conquest Storm/Sack fork + Entry-Terms "Impose
  Administration" exist) is **never consequence-free** — it fires a designer-selected subset of the seven
  mechanisms as cross-scale consequences: severe L/PS collapse + intrapopulation conflict + a durable
  resistance-identity feeding the insurgency pipeline (GD-3). **Toleration** is the lower-variance, deferred-cost
  alternative (Ottoman millet → 19th-c nationalism), built as a **variance/timing trade reusing FA-8
  Protected-Tributary's shape — not a good/evil dial.** Model **axis-capture** generally (Albigensian
  heresy-suppression as cover for Capetian annexation). **Interdict** = a collective/territory-grain sanction
  (vs single-target Excommunication).
- **Why no chain-completion:** the corpus has the suppression *action* (Storm/Sack, Impose Administration) but the
  cross-scale *consequence* (backlash → insurgency, the seven mechanisms) is under-wired — the surrounding logic
  delivers the action without its downstream cost. The backfire structure must be imported.
- **Surface-analogy verdict:** **REAL** — seven historically-grounded mechanisms with distinct cross-scale
  signatures (fiscal vs reputational vs identity vs military-to-investigation hand-off). **SURFACE-ANALOGY
  DISCARD: Rome vs Carthage "total erasure achieved" is historically FALSE** (Neo-Punic persisted ~700 yrs;
  salted-earth is apocryphal) — any mechanic implying suppression can *fully zero* a Conviction/identity track
  must be rejected: **model a floor, not a zero.**
- **Compliance:** P-01/P-12/P-14 (suppression produces tri-dimensional co-movement — actual population-flight,
  intelligibility resistance-identity, temporal durable-scar; P-12's drift-propagation shape fits
  identity-hardening across a population) · GD-3 (backfire is the pipeline's designed input) · GD-1 (tactical
  leverage, never a win-trigger) · no-GM (consequences fire as deterministic auto-effects, P-14). **Register
  nuance:** stays in the **political-consequence** register (a variance/timing trade), **non-moralizing** —
  consistent with the no-alignment principle (P-04's spirit), never framing a population as evil. **§3 (seven
  mechanisms) + §4 (Carthage discard).**

### GAP-H3 · `domain_actions` / `engine_clock` doc:null (strategic-turn + temporal home)
- **Precedent + mechanism:** **no external precedent** — an authoring task. `module_contracts.yaml` has 10/27
  `doc: null`, including `engine_clock` (the temporal spine) and `domain_actions` (the strategic-verb home). The
  surrounding logic does not *determine* a temporal-spine/strategic-verb contract; it must be authored.
- **Valoria adaptation:** author `engine_clock` (ordering/cadence — `propagation_spec_v1` supplies its candidate
  home per `CURRENT.md`) and `domain_actions` (the home for the governance verbs of A3). Unblocks A3 (Territory-
  tier coding + the uncoded governance-play layer) and A4 (convergence needs the clock's ordering).
- **Why no chain-completion:** a `doc: null` module has **no home design doc to derive from** — there is nothing
  adjacent to complete; the contract must be authored first. Holonic doctrine §1 calls this the highest-value
  unauthored canon.
- **Surface-analogy verdict:** **REAL / N/A** — an authoring task, no mechanism imported, no surface-analogy
  risk. (Internal "precedent": `propagation_spec_v1` is `engine_clock`'s candidate home.)
- **Compliance:** holonic (authors the temporal/ordering spine the whole propagation model needs — determinism,
  stable iteration order) · no-GM (the clock **is** the engine's resolution cadence). Fable/opus-tier per §10;
  blocks A3/A4.

### GAP-B5-extension · rank = secession blast-radius (Mixed — extension half)
- **Precedent + mechanism:** **KOEI ROTK rank-scaled secession** — a **Prefect** takes only their city
  independent; a **Viceroy** takes the whole **division**; a rival can *engineer* it via a "Collaborate" plot. The
  real mechanism: **the disloyal actor's Standing rank = the blast radius of the break-away**. Plus **Imperator
  power-base** (the same holdings/cohorts that empower an appointee *corrode their loyalty*, ~0.55/pt — capability
  is corrosive **by construction**) and the **size-scaling civil-war threshold** (25%→17%, shrinks with Tyranny —
  bigger realms structurally more fragile).
- **Valoria adaptation:** map the **built** Standing 0–7 ladder (Skyrim-Eight, `faction_politics_v30`) to secession
  blast-radius — a low-rank holder secedes with one settlement; a high-rank (Viceroy-equivalent) takes a whole
  province/division. Model capability-corrodes-loyalty: the forces that empower a governor also raise their
  secession potential (not independent axes). A rival faction-action can engineer a break (ROTK Collaborate →
  target the delegation chain). Ties to F5 (fracture resolution) + D2 (bypass fragility).
- **Why no chain-completion:** the ladder **exists** (that half **is** a chain-completion — it is built), but the
  rank→blast-radius **function** is absent; the surrounding logic gives a rank ladder and a secession event with
  no relation between them. That relation must be imported (ROTK).
- **Surface-analogy verdict:** **REAL** — ROTK rank-scaled secession is genuine (rank literally sets the
  seceding territory); Imperator capability-corrodes-loyalty is cross-validated, load-bearing. The rank is
  *causally* the blast radius, not a flavor label — not a pattern-match.
- **Compliance:** holonic (the ladder is top-imposed structure; the blast-radius is bottom-up behaviour — rank
  determines scope) · GD-3 (rank-scaled secession feeds the insurgency/faction lifecycle) · no-GM (secession
  resolves by the F5 fracture roll).

---

## §3 · Legitimacy & Authority across scales

The docket's legitimacy findings cohere into a single authority-across-scales picture. It is **not** one new
mechanic; it is the shape the precedents converge on for how legitimacy is aggregated, contested, transferred,
and lost.

**1 · The apex is a lease, and it collapses by resonance and devolves (B2/E2).** The Mandate-of-Heaven archetype
supplies the missing withdrawal layer as a **two-signal collision** (E2): a **material** signal (settlement
Order/Dearth/Π, bottom-up) and an **interpretive** signal (a portent/rumor/interdict — top-down, often
locus-less) must **resonate in one Accounting** for a Mandate-tier legitimacy crisis to fire. Its output is not a
floor-crossing but a **cross-scale power devolution** (national → province/territory, via the A1 transfer resolver
+ F5 fracture-resolution). Two costed relief valves route the crisis: **scapegoat-the-subordinate** (a bend-around
onto a named appointee, spending *their* Standing/office) and **ruler self-reproach** (spending the ruler's own
Mandate/Treasury). The verdict is **contestable** (Xunzi) — a court social-contest scene decides whether a
disaster "counts," and a rival can weaponize the *declaration* itself.

**2 · Two apex authorities need a ranking or a named crisis (D1).** Bodin's indivisible-sovereignty theory exists
to forbid exactly the two-unlimited-bypass configuration `scale_hierarchy §5.3` creates. Resolve either by
**nesting** (auctoritas at the apex, an independent potestas chain beneath — asymmetric-and-enforced, Tokugawa)
or by making the Monarch-vs-Parliament collision a **named constitutional-crisis mode**, adjudicated by Bodin's
war/peace test for where sovereignty really sits. This is the outward/bend-around direction made well-formed.

**3 · auctoritas/potestas → L vs Mandate.** The Roman/Tokugawa separation of *legitimacy* from *office-power*
maps Valoria's **L (consent/legitimacy)** against **Mandate/Military (potestas)** — the corpus's own L-vs-Mandate
split, historically grounded (Res Gestae 34.3; the 1615 Kinchū narabi). It licenses borrowing legitimacy once at
the apex and running an independent power chain beneath.

**4 · Legitimacy decays (B4).** Anacyclosis and cognomen-decay confirm that a legitimacy that only ratchets up is
a modeling error; the fix is the corpus's own deferred OF-3 `decay()` (a chain-completion), giving decline-and-fall
its entropy term.

**5 · The decision-procedure is its own FLAG (C2).** Legitimacy is exercised *through* a governance-mode — the
recommended 8-value `governance_mode` domain (§2, C2) — each selecting the contest that resolves its business, or
resolving to fiat. Modes carry Machiavellian failure-signatures (elite-satisfying → peer-coup; populace → PS
volatility), so which mode holds power shapes *how* it is lost.

**6 · Two missing resolution registers (F4/F5).** Beyond suppression and concession, two genuine-gap imports
complete fracture-resolution: **millet recognition-fission** — charter a new sub-faction out of a permanently-
diverged population (a *peaceful* insurgency-**formation** path the pipeline lacks; `insurgency_pipeline §4.1` has
only territorial-neglect) — and **Cleisthenes reaggregation** — a genuinely new 4th category that changes *how
allegiance aggregates* (redraw the blocs) rather than the values, a Crown action diluting a regional bloc
structurally. Nothing in the current stack touches aggregation *topology*.

**7 · Suppression is a costed, backfiring, non-moralizing action (G2).** The seven backfire mechanisms
(Resource/Treasury · Legitimacy-contagion · Quiet trust-decay · Identity-hardening · Identity-migration ·
Sponsor/insurgency · No-off-ramp ratchet) make cultural suppression a cross-scale consequence-bearing action,
never consequence-free; toleration is its lower-variance, deferred-cost twin (FA-8 shape). A belief track keeps a
reachable recant off-ramp; an ancestry-keyed track has none and must escalate — **but never to a zero (Carthage
discard, §4)**.

**8 · The propagation shape: elect-inward, account-back.** A new same-tier direction (`internal_polity §A`,
Venice Great Council → Senate → Ten): a body spins off a *narrower, time-boxed, more-empowered* committee
accountable back to its **same-tier** creator — distinct from top-down cascade and bottom-up aggregation, and
distinct from the CK3-Council superior's-fiat skip (power here flows from a *peer body's* delegation and must be
returned). Recommend adding it to `governance_type_registry §4` alongside propagation/dissemination/accumulation/
dissipation.

---

## §4 · Cross-cutting rulings + surface-analogy warnings

**Design rulings the precedents converge on** (the fix doctrine, drawn from `game_precedents §cross-cutting` +
the theory files):

1. **Does-it-stick = broadcast + local-attenuation** (CK3 Administrative), not a forced identical type — the hard
   type-cascade is Valoria-novel (C3).
2. **Capability corrodes loyalty** (Imperator power-base) and **rank = secession blast-radius** (ROTK) — the
   delegation chain's disloyalty math (B5).
3. **Fragility scales with size** (Imperator threshold 25%→17%) — big realms are structurally fragile; many quiet
   disloyalties are harmless until their combined weight crosses a scaling line (D2/F5).
4. **Bypass is metered against the same fragility pool** (Imperator Tyranny) — never a free Monarch/Parliament
   action (D2).
5. **Collapse is a dial** (RimWorld/DF dampening; Tokugawa *murauke*) — recovery/decay counters (E3/E7/E11) are
   *required*, not optional.
6. **Don't invent a parallel ledger** (DF: popularity *is* legitimacy, read off the existing graph) — the
   [COMPLETE-THE-CHAIN] principle behind A2/B1/F1/H2: read existing state, add no bookkeeping.
7. **Saturating aggregation is Valoria-original** — games use linear sum/ratio or a land-share cap; the
   `round(7T/(T+K))` shape has only partial precedent (EU4 influence cap). Design it fresh; do not import a
   linear model onto it.
8. **L and PS stay divergent** (Tropico/Frostpunk twin-gauge), **per-node, not one national scalar** (FP2
   Fervor) — the B1 wiring must keep the two axes genuinely divergent with distinct feeders/consequences.

**Explicit SURFACE-ANALOGY discards** (Phase-F rejections — a shared vocabulary is not a shared mechanism):

- **Carthage "total erasure achieved" = historically FALSE** (Neo-Punic persisted ~700 yrs; salted-earth is
  apocryphal). Any suppression/conquest mechanic implying a Conviction/identity track can be *fully zeroed* is
  **rejected — model a floor, not a zero** (G2).
- **Byzantine Blues/Greens ≠ caste.** They were caste/class-*orthogonal* — REAL for **cross-caste coalition
  formation**, a **misuse** if folded into the caste thread (F2/F3). Keep them out of the caste keys.
- **A hard identical-type cascade has no game precedent** — the convergent negative finding across
  Imperator/Stellaris/EU4/ACOUP: no game forces a matching government type down a tier. Do not pattern-match the
  cascade to any game's "government type"; treat the hardness as a Valoria-novel question and soften toward
  broadcast+attenuation (C3).
- **EU4 disasters ≠ parallel collision.** They accumulate-then-cascade through *one funnel*; true parallel
  collision (many scales hit independently in one tick) is a Valoria departure — do not port EU4's accumulator as
  the collision primitive (E1).
- **CK3 factions Discontent ratio is SURFACE for Valoria's Mandate math** — REAL for the aggregate-then-resolve
  *shape*, but its linear sum/ratio is not the saturating `round(7T/(T+K))`; import the shape, not the formula
  (B3, ruling 7 above).

---

_ED-IN-0051. PROPOSED fixes only — this catalog flips no `## Status:` line, wires no field, and edits no canon
doc (docket brief; CLAUDE.md §2). Pairs with `gap_register_v1.md` (classifications mirrored exactly),
`governance_grounding_v1.md` (graph), `pressure_key_registry_v1.md` (key census). Genuine-gap imports and the
D1/C3/E1/F4-F5/G2 authoring calls are handed to `decision_queue.md` as ranked `needs_jordan` items. Currency per
`CURRENT.md` 2026-07-13._
