# Governance Consolidation (v1) — the reconciled proposal head

## Status: D1–D5 RATIFIED (2026-07-13, ED-IN-0046) — 2026-07-12 · Lane: IN (cross-cutting; SE, FA, GO) · Opus 4.8 max-effort consolidation. §6 decisions D1–D5 are RULED (each accepted as stated below, per their own "(rec: yes)"); the Phase-4 execution plan and §2 item dispositions are downstream of that ruling and still track their own authoring status. **D6 (the G606 recall-clock wiring fork, filed by `designs/architecture/ners_vsg_reconciliation_v1.md`) is a SEPARATE, still-open decision — not resolved by this ruling.**

**What this is.** The single consolidated head for this session's governance proposal arc, reconciled
against the **pre-existing built substrate** the earlier work was blind to. It collates six streams into
one decision surface and one execution order:

1. the comparative-governance **44 proposals** (`designs/audit/2026-07-09-comparative-governance-research/`) → **12 authored** into canon as PROPOSED (PR #119);
2. the **governance-ripple substrate** (`designs/architecture/governance_ripple_substrate_v1.md`);
3. the **58-card grounded deck** (`designs/audit/2026-07-11-grounded-event-card-deck/`);
4. the **pessimist NERS audit** (`designs/audit/2026-07-11-comparative-governance-pessimist-ners-audit/`);
5. the **7-seed settlement-season stress test** + its verification layer (`designs/audit/2026-07-12-settlement-season-stress-sim/`);
6. the **reconciliation** against `goldenfurt_slice`, the **built `sim/territory/` code**, the **500-seed `settlement_mgmt_stress_01`** framework, and the **2026-06-22 baseline audit** + march/hierarchy layer.

**The one-paragraph verdict.** The *resolution substrate is sound and earned ratification* — both a
qualitative 7-seed sweep and a prior 500-seed batch confirm it produces coherent arcs, and both confirm
the same failure: **the system is biased toward negative death-spirals.** But that failure is *already
largely designed-away* in `goldenfurt_slice` (a bidirectional Π valve and a survivable recall), just not
ported. What genuinely blocks ratification is not balance — it is **five unreconciled architecture
divergences** (§1) between the PR#119 prose and the built code, none of which the earlier work could see.
Resolve those five, port two already-designed fixes, and the twelve items sort cleanly into ratify /
refine / merge (§2).

---

## §1 · The five reconciliation decisions (these gate everything)

Each is a real fork between what PR#119 authored (prose) and what `sim/territory/` implements (code). Each
has a recommended resolution; each is a Jordan call (§6). **Nothing downstream is safe to ratify until
these are ruled** — otherwise the port inherits two competing definitions of the same thing.

### D1 · Event architecture — card-deck vs predicate-sweep → **RECOMMEND: card-deck is canonical for play; predicate-sweep is the batch oracle.**
Two engines model "what happens to a settlement each season." The **stateful card deck** (`governance_play_redesign §2`, Goldenfurt, the grounded deck) — Π-weighted draw, cooldowns, a forced queue, `seeds:` chaining — is the **player-facing** engine; it carries authored drama and the churn invariant (every card moves the world). The **predicate-sweep** (`settlement_mgmt_stress_01` M6) — events as pure functions of state, co-firing, chaining only through shared state — is a **headless batch** model good for 500-seed regression, bad for authored narrative. They are not rivals; they serve different masters. **Resolution:** the deck is canonical for the game; the predicate-sweep is retained as the balance-regression harness; the two are kept in sync by a small overlap map (Famine/Revolt/Raid/Flourishing appear in both — assert the deck card and the predicate event write the same state deltas).

### D2 · Action model — AP economy vs predicate-gated handlers → **RECOMMEND: AP economy is canonical.**
`governance_play_redesign` and the built `registry.py` both use **`AP = 2 + facility_tier (+1 Seat/Cathedral)`** as the player's scarcity lever (the whole "the vise: 3 AP cannot serve all three needs" tension depends on it). The 500-seed framework's un-metered discrete handlers are the batch approximation. **Resolution:** AP is canonical for play; the batch harness may keep un-metered handlers (it is measuring the world, not playing it). This is already the built reality — the decision is just to state it and stop the settlement_mgmt handler model from being read as the action contract.

### D3 · Ledger families — PR#119 `Compact` vs the built `Leverage` → **RECOMMEND: keep the built five; re-express Compact as a recurring, fixed-term `Debt` subtype (do NOT add a 6th family).**
The built `ledger.py` is `TAG_KINDS = {Precedent, Grudge, Debt, Reputation, Leverage}`; Goldenfurt uses the same five. PR#119 §1.3a calls **Compact** "the 5th family" — but the implementation's 5th is **Leverage**, and the two are semantically distinct (Leverage = a player-held hook; Compact = a negotiated fixed-term extraction figure that fires *every season of its term*). So Compact is **not** Leverage, and it is **not** a free slot. Its distinguishing machinery — *fires every season for N seasons, then lapses* — is exactly a **`Debt` with a term and a recurrence** (Debt already = a fired-when-due obligation; the built `LedgerTag` already carries `ttl`/`created_season`). **Resolution:** model Compact as `Debt(key="compact:<quota>", ttl=term, recurs=True)` — reusing built machinery, honoring the "additive to existing machinery, no new primitive" discipline — rather than minting a 6th family. If Jordan judges Compact deserves first-class status, add it as a real 6th `TAG_KIND` in `ledger.py` **and** update Goldenfurt + the built code in the same stroke. Either way, **§1.3a cannot ratify until this is chosen** — today it silently claims a slot that is taken.

### D4 · Cross-scale carrier — the §1.8 Mandate formula vs the built aggregation → **RECOMMEND: retire §1.8 `round(7T/(T+6))` as the collapse carrier; designate floor-avg Order + province fracturing + Standing/tag Keys.**
The `Mandate = round(7T/(T+6))` formula the stress test found "masks peripheral collapse" is **`settlement_layer §1.8` prose the code never implements**; and its inputs (L/PS) are **declared-but-inert in `sim/`** (the `Settlement` dataclass carries `legitimacy`/`popular_support` but nothing in `sim/` reads or writes them — a known port-blocking gap, tracked open in the FA lane). The built aggregation is **floor-average Order** (which *does* drop when a settlement collapses) + **summed Prosperity**, and the real "a peripheral settlement fell" signal is **province fracturing** (`political_hierarchy §2.3`). **Resolution:** stop asking a saturating Mandate scalar to carry cross-scale collapse; the carriers are floor-avg Order + province fracturing + the Standing/resolution_quality Keys (as the substrate already routes). Keep a "Mandate" **only** as the faction/parliamentary meter (the `settlement_mgmt` M12 CI-driven one) and **rename** to end the two-Mandates collision. This also means the §1.8 L/PS→Mandate feedback loop is **design-only until L/PS is wired** — state that so "ratified" is not read as "working."

### D5 · Accountability — §1.0d Performance Audit vs Goldenfurt's suspicion→recall → **RECOMMEND: merge §1.0d onto the one suspicion/recall signal (this IS the confirmed NERS MERGE).**
The governance redesign already has a complete accountability spine: **suspicion accrues** (per Defy, capped +1/season) → at threshold **G606 "The Bailiff's Report"** fires a **Recall scene** with a **`Submit to audit` escape** (always available, −2 suspicion) and a `Reputation:Just`-lowered Ob. PR#119 §1.0d bolts on a *second* cascade (triplicate-ledger → Waiting Order → patron review → Demotion). The stress test's NERS **MERGE** verdict on §1.0d is confirmed, and now has a concrete target: **§1.0d becomes a *modifier* on the existing suspicion/recall signal** — a Standing-6+ patron toggles a stricter suspicion→review cadence and a faster-promotion upside — **not a parallel demotion engine.** One signal, one recall scene, one escape.

---

## §2 · The twelve PR#119 items — consolidated dispositions

Each item's stress-test verdict, the reconciliation, and the consolidated call. "RATIFY" = ordinary-merge
ratifiable once D1–D5 are ruled; "RECONCILE-FIRST" = blocked on a §1 decision; "REFINE" = small authored
fix then ratify; "MERGE" = fold into an existing system.

| Item | Stress verdict | Reconciliation | Consolidated disposition |
|---|---|---|---|
| **§1.0b Recognition Fork** | STRAIN | granter decision-rule + orphaned-New-Grant fate undefined | **REFINE-THEN-RATIFY** (two small edges) |
| **§1.0c Court Attendance + Hostage-Kin** | HOLD (under-tested) | sound; no collision found | **RATIFY** |
| **§1.0d Performance Audit** | MERGE (NERS-confirmed) | duplicates Goldenfurt suspicion→recall (**D5**) | **MERGE into the suspicion/recall spine** |
| **§2.5a Guild entry/mastership forks** | HOLD | the "missing Gu-Std2→3 rung" was a kernel artifact — §2.5 authors the full ladder | **RATIFY** |
| **§1.1a Clerk Capacity** | STRAIN | CC-scaling, Corruption→Intrigue increment, defection-severance undefined; harvest VEN-FA-2 accounting (not its AP source) | **REFINE-THEN-RATIFY** |
| **§1.3a Locked Extraction / Compact** | BREAK (failure-mode) | Compact/Leverage collision (**D3**); no subsistence floor; protective variant Π-gated-out | **RECONCILE-FIRST (D3) + REFINE** (add subsistence-floor clamp; ungate the protective Compact at crisis Π) |
| **§1.3b Bind the Cells** | MERGE (NERS-confirmed) | the collision is a **missing population-granularity layer**, not an actor cap (settlements hold unbounded named NPCs; §4.5 "1–2" is a *count-per-type*, distinct again) | **REFINE-THEN-RATIFY**: reframe cells over an explicit household/population layer, or scope Collective-Liability to named-actor factions; fix the §4.5 cross-reference |
| **§1.3c Ordenanza Ratification** | HOLD (was BREAK) | Amend/Ratify/Reject resolves when actor qualified; only a sub-threshold-presentment fallback is missing | **RATIFY** (+ tiny fallback-resolver edge) |
| **§3.3b Za Patron-Lapse** | HOLD (cleanest) | end-to-end clean; interaction with §3.3c is the only friction | **RATIFY** |
| **§3.3c Seggio Council** | BREAK → MEDIUM | violent removal exists (Siege + `seizure_ob_modifier`); only the soft **Mandate-Challenge** path is genuinely undefined; the §3.3b×§3.3c asymmetry is real | **REFINE-THEN-RATIFY**: define the Mandate-Challenge (§3-E2); state the asymmetry resolution |
| **Governance-ripple substrate** | HOLD (spine) | §5 mis-scores a *sanctioned* Defy as Duty-failure (verify vs §5 text) | **RATIFY** (+ verify the one scoring edge) |
| **58-card grounded deck** | STRAIN (was BREAK) | "Crisis band empty" was a kernel artifact; Crisis cards resolve via `d_sigma`; per-branch delta tables are uneven | **RATIFY the architecture; polish** the uneven delta tables |

**Net:** of twelve, **five RATIFY as-is** (1.0c, 2.5a, 1.3c, 3.3b, substrate, deck-architecture), **four
REFINE-THEN-RATIFY** (1.0b, 1.1a, 3.3c, 1.3b), **one RECONCILE-FIRST** (1.3a on D3), **one MERGE** (1.0d on
D5). *Not one requires reversal* — the compressed-kernel alarms that suggested otherwise were artifacts.

---

## §3 · Extensions & improvements (wire what's designed; author the true gaps)

Ordered by leverage. E1 is the single highest-value move and is **already designed** — it only needs porting.

- **E1 · Port Goldenfurt's death-spiral fixes (highest leverage, already designed).** Both stress harnesses
  confirm a negative-spiral bias; Goldenfurt already fixes its two engines: (a) the **bidirectional Π
  restoring term** `sign(3−Π)·min(1,|3−Π|)` (CG-1) — anti-runaway *and* anti-stall; (b) the **survivable
  recall** (G606 `Submit to audit` escape + suspicion cap +1/season + `Reputation:Just`-lowered Ob). Porting
  these into the shared engine de-fangs Pattern A/B/G at once. *No new design — a port.*
- **E2 · Author the Mandate-Challenge** — the *political* (non-violent) removal of an entrenched/irrevocable
  privilege (§3.3c Seggio, §3.3b-lapsed charter, entrenched Church infra). Violent removal already exists
  (Siege + `seizure_ob_modifier`); this is the one genuine §3.3c residual. Scope it as a bounded
  Parliament/Mandate-track contest, not the "unbuilt emergence pipeline" IT-3 was cut against — the
  down-scoped IT-3 (Sforza Gambit) is the reinstatement candidate here.
- **E3 · Subsistence-floor clamp on extraction (§1.3a)** — turns the deterministic below-subsistence strip
  into a bounded floor; define the below-subsistence terminal state (depopulation / Prosperity floor).
- **E4 · Resolve Compact (D3) and the population-granularity layer (§1.3b).** These are authoring decisions
  gated on §1; once ruled, both are small.
- **E5 · Wire L/PS (the port-blocking inert-fields gap).** Every faction-standing item (§1.0b/c/d) and the
  Mandate feedback read L/PS, which is declared-but-inert in `sim/` (an open FA-lane item). Until wired, these
  items are ratified-as-prose only.
- **E6 · Close the type-taxonomy drift** (baseline audit **H3** + 500-seed **F1**, cross-confirmed): add
  Village / Fortress-City / Cathedral-City to §1.2 so downstream modules stop hitting fallback logic. This
  sits under everything and is a known, ledgered gap.
- **E7 · Add a systemic recovery / positive-feedback path.** Both harnesses show negative events crowd out
  Flourishing (500-seed: 3.7 vs 659/seed). Beyond E1's valves, the world needs a way for *good* governance
  to compound (a Flourishing→Prosperity→Opportunity loop), or the only stable attractor is collapse. This is
  the highest-leverage *balance* intervention and is currently no one's item.

---

## §4 · Dependency-ordered execution plan

```
Phase R (Reconcile — Jordan rules §6):  D1 D2 D3 D4 D5           ── unblocks everything
        │
Phase P (Port the designed fixes):       E1 (Π valve + recall escape)   ── highest leverage, no new design
        │
Phase A (Ratify the clean five):         1.0c · 2.5a · 1.3c · 3.3b · substrate · deck-arch
        │
Phase B (Refine-then-ratify):            1.0b · 1.1a · 3.3c(+E2) · 1.3b(+E4 pop-layer)
        │
Phase C (Reconcile-gated):               1.3a (needs D3) + E3 subsistence floor ;  1.0d MERGE (needs D5)
        │
Phase D (Author the true gaps):          E2 Mandate-Challenge · E5 wire L/PS · E6 type-taxonomy · E7 recovery loop
```

Phases A–C are ordinary-merge ratifiable once R + their gates clear. Phase D is genuine new authoring.

---

## §5 · Grounding & validation protocol (so this stops recurring)

- **Seed from canon, not invention.** Future runs seed from **`goldenfurt_slice`** (real 9-actor cast + 28-card
  deck) and the built **`sim/territory/registry.py`**, never from hand-invented settlements. The stress test's
  weakest seam was ungrounded seeds.
- **Two harnesses, two jobs.** The **card-deck** drives authored churn traces (does a season *play* well); the
  **500-seed predicate-sweep** is the balance-regression oracle (is the *distribution* healthy). Neither
  replaces the other. Wire a seeded smoke assertion (CLAUDE.md §7) before trusting either.
- **Carry the existing work in-kernel.** Any agent-driven sim must include `goldenfurt_slice` + the built
  schema + the baseline audit in its kernel, or it will re-derive solved problems (as this session's first
  pass did).
- **Odds from code, not estimate.** Roll odds come from `valoria_dice.py` / `sigma_leverage.p_success` (the
  ground-truth tables already computed), not agent arithmetic — and the **d_sigma legible-vs-engine
  divergence** (deck's +10%/pt vs the continuous CDF) is itself an open reconciliation.

---

## §6 · The explicit ask (decisions for Jordan) — RULED 2026-07-13

**Ruling basis:** Jordan's "ratify commit all" instruction (2026-07-13), applied to the scoped tier laid
out in reply (D1–D5 plus the six items §2 already called a clean, no-open-sub-question RATIFY) and left
unobjected, followed by the review-and-merge of PR #129 (`designs/architecture/ners_vsg_reconciliation_v1.md`,
which restates and relies on D1–D5) — per CLAUDE.md §2's merge-ratifies-by-default convention (ED-1094).
Items with no stated recommendation anywhere in this doc were explicitly NOT resolved by that instruction
(precedent: the pre-existing faction-count gap, "no default exists — deliberately NOT resolved by a prior ratify-all" — see B1 below).

1. **D1 RULED YES** — card-deck canonical for play, predicate-sweep is the batch oracle.
2. **D2 RULED YES** — AP economy canonical, handlers are the batch approximation (already the built reality).
3. **D3 RULED** — Compact models as a recurring fixed-term `Debt` subtype
   (`Debt(key="compact:<quota>", ttl=term, recurs=True)`), **not** a 6th `ledger.TAG_KINDS` family.
   **Unblocks §1.3a** (still needs E3's subsistence-floor clamp authored before §1.3a itself ratifies).
4. **D4 RULED YES** — retire §1.8's Mandate formula as the collapse carrier (floor-avg Order + province
   fracturing + Standing/resolution_quality Keys instead); rename the faction "Mandate" meter to end the
   two-Mandates collision.
5. **D5 RULED YES** — §1.0d merges into the suspicion/recall spine as a Standing-6+ modifier, not a
   parallel cascade: one signal, one recall scene (G606), one escape (`Submit to audit`, −2 suspicion).
   **The spine's WIRING — does suspicion advance every non-compliant season, or only on a specific
   card draw (`ners_vsg_reconciliation_v1.md` D6) — is NOT ruled by this and stays open**; the merge
   cannot be authored into `faction_politics_v30.md` until D6 is answered.
6. **RATIFIED** — the six items §2 called a clean "RATIFY" with no open sub-question: §1.0c
   (ED-FA-0020), §2.5a mastership + entry forks (ED-FA-0022/0023), §1.3c (ED-SE-0023), §3.3b
   (ED-SE-0021). (The governance-ripple substrate and the 58-card grounded-deck architecture items in
   §2's table are **not** touched here — no ED citation was available to update them accurately in this
   pass; they remain as governance_consolidation_v1 §2 already described them.)
7. **NOT ruled — Phase P greenlight.** `ners_vsg_reconciliation_v1.md §3` supersedes this ask: four
   independent measurements (500-seed isolated test, 1500-trial integrated campaign, the event-deck
   engine, two prior methodologies) show the unaugmented Π term does not de-fang the runaway pattern
   alone — Phase P as originally scoped (E1 alone) should not be greenlit; E1+E3+E7 need to land as one
   bundled port. This is a build/engineering task, not a ratification, and remains tracked in the
   reconciliation doc's workplan.

**Still genuinely open (no recommendation exists anywhere to accept, not resolved by "ratify all"):** D6
(G606 wiring), B1 (faction count 4–8, `ED-FA-0001`), B2 (S-006's identity), B12 (the Territory-naming
collision) — all per `ners_vsg_reconciliation_v1.md §5`. Also explicitly held back: Part 41's
Territory-scale content (Relay Tier/Beacon Network), per that same document's loud-exception flag.
