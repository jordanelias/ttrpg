# Churn / Event-Opportunity Map — Where Narrative Friction Can Occur, and the Gaps

## Status: FILED (analysis) — 2026-07-14 · Lane: IN · ED-IN-0064

**What this is.** A governance-docket map of the three sources of dramatic friction Valoria's
no-GM engine must generate on its own — (1) character desires/needs/events/choices, (2) evolving
geopolitics & faction relationships, (3) randomized/unexpected events (event decks) — cross-walked
against what actually EXISTS in the working tree today, where the OPPORTUNITY sits for each, and
the concrete GAP blocking production use. It also traces how a single event resolution is meant to
feed the ripple-substrate loop into Standing/FI/SC/FA and re-weight the deck for the next season.

**What this is not.** Not a new design, not a ruling, not a fix. An orientation map for whoever
picks up event-deck/churn work next — every claim below cites its source doc, and every "does not
exist yet" is checked against the working tree, not asserted from memory (CLAUDE.md's working-tree
rule).

**Sources read for this map:**
- `designs/audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md` — RATIFIED
  Churn Engine v2 (Jordan, ED-IN-0011), Stage 0–5 sequencing (§8), forks §10.
- `designs/territory/goldenfurt_slice/event_deck.md` — the 28-card worked deck, S-006 Goldenfurt,
  draw rule `1 + ⌊Π/3⌋`.
- `designs/territory/governance_play_redesign_v1.md` — PROPOSAL (drafted 2026-06-22); §2 event
  deck, §3.1–3.4 the NPC ambition engine, Part 4 the two-stroke churn loop.
- `designs/architecture/governance_ripple_substrate_v1.md` — PROPOSED (2026-07-11, not yet
  Jordan-ratified); §4 event generation reads state, §5 the standing bridge, §6 the three ripples,
  §8 arc feedback, §13 self-audit against its own primitive test.
- Cross-checked against `designs/audit/2026-07-13-cross-scale-governance-grounding/gap_register_v1.md`
  and `governance_grounding_v1.md` for the corrected win-share/territory finding (below).

---

## §0 · The three friction sources, at a glance

| Source | Canonical home | Status | One-line verdict |
|---|---|---|---|
| **1. Character** (desires/needs/events/choices) | `governance_play_redesign_v1.md` §3 (NPC ambition engine) + `narrative_engine_design_v2_churn.md` §4/§6 (character rung of the render) | PROPOSAL + RATIFIED-design-not-yet-built | Best-specified surface in the whole docket (per-NPC dossier, four conflict surfaces from one NPC); **not ticking** — no Accounting-cascade hook exists |
| **2. Geopolitics & faction relationships** | `governance_ripple_substrate_v1.md` §5–§8 (standing bridge, ripples, cross-scale aggregation) | PROPOSED, self-graded mixed (§13) | The wiring diagram is honest about its own gaps — 5 of 8 loop edges WIRED, 2 HOOK-NEEDED, 1 AT-RISK; the sim's actual territorial-transfer code is broken independent of any design doc |
| **3. Randomized/unexpected events** (event decks) | `governance_play_redesign_v1.md` §2 (schema, Π homeostat) + `goldenfurt_slice/event_deck.md` (28-card worked example) | Design PROPOSAL; implementation **absent** | One hand-authored slice deck proves the shape works; zero deck engine code, zero module contract, zero production wiring |

All three sources are meant to compose over the **same five primitives** named in
`governance_ripple_substrate_v1.md` §9: Key emission, Ledger tag, Disposition, Π, and
Standing/`consolidation_progress`. That is the single most load-bearing fact in this map — none of
the three friction sources is a separate content pipeline; each is a subscriber to (or writer of)
these five fields. Where a proposed connection is NOT a genuine read/write dependency over one of
the five, §9 calls it pattern-matching and requires it be cut — the ripple-substrate doc itself
found and flagged one such case in its own text (§6.2, below).

---

## §1 · Source 1 — Character desires, needs, events, and choices

### EXISTS

- **The NPC ambition dossier** (`governance_play_redesign_v1.md` §3.1): every significant NPC gets
  `convictions`, `ambition{goal, method, timeline, progress}`, `ethic` (α/β), `leverage{wants,
  fears, secret}`, `relationships` (Knots, PP-724), and `trajectory` (how they act when unwatched —
  shifts method if blocked, seeks a rival patron if Disposition < −2, escalates if a Conviction is
  violated). This is genuinely rich: the worked Hedda Vorn dossier (§3.4) generates four distinct
  conflict surfaces — a Petition, a Friction, an Intrigue, and an Ambition card — from one NPC
  specification (§3.4's own claim, and it checks out against the goldenfurt deck's G501–G606,
  G303 cluster, which are all keyed to the same Hedda/Orsk/Tomas/Konrad/Wessel dossier set).
- **Settlement Needs** (§1.5): emitted independently of the Directive, deck-driven, and *designed
  to conflict* with whatever the Directive demands — "the drama is that the Directive and the Needs
  routinely conflict, and your AP can't serve both." This is the vise mechanism, and it is the
  single clearest EXISTS in the whole map: the goldenfurt deck's G201 (levy) vs G101 (only-sons
  petition) trace (§0 in `event_deck.md`) is a fully worked instance.
- **The ambition engine tick** (§3.2): "each Accounting, every significant NPC advances their
  ambition by 1... unless the player or another actor intervened." When `progress` hits threshold
  the NPC fires an Ambition card (G601–G606 in the worked deck).
- **Character-rung render** (`narrative_engine_design_v2_churn.md` §6): intent-grammar dialogue
  (concerns/projects emit `request/demand/warn/confide/accuse/deflect`), bound to
  topic=stake/relationship=Bond·Standing·npc_memory/voice=slow-variable overlays — players choose
  intents, never sentences; deterministic anti-repetition per NPC. The churn engine's Light
  Function (§4) is explicitly the mechanism that decides which character-scale threads get
  attention (tie-proximity is "a permanent weight term; the seedling grows where the protagonist
  stands" — invariant iii).
- **Conflict-maximizing authoring discipline** (§3.3): orthogonal Convictions within a settlement,
  overlapping ambitions (two NPCs want the same office), cross-cutting Knots, and ethic spread are
  named authoring rules, not incidental flavor — they are how the deck's 28 cards manage to
  interlock (Hedda vs Orsk is exactly "overlapping ambitions forcing the governor to be kingmaker").

### OPPORTUNITY

- **Character-scale friction is the cheapest to render and the most diegetically real** per the
  churn engine's own cost model (`narrative_engine_design_v2_churn.md` §6): "the bulk renders are
  behavioral... NPCs and factions acting on their own diegetic expectations... zero prose cost."
  Character desire/need friction does not wait on the forecast (Layer A/B) or the Light Function's
  render budget to *exist* — only to be narrated. That means Source 1 is the one friction source
  that can be load-bearing even before Stage 2.5 (forecast) or Stage 3 (detect) land in the churn
  engine's staging (§8).
- **The dossier's `trajectory` field is the anticipation engine's actual substrate**: churn v2's
  hard rule that forecast objects are actor-invisible (R-AI, §3/§4/§7) means NPCs must anticipate
  via diegetic heuristics over observable state — the `trajectory` schema in
  `governance_play_redesign_v1.md` §3.1 is precisely that heuristic layer, already specified,
  already the right shape. Wiring the ambition tick into the Accounting cascade is therefore not
  just a Source-1 fix — it is the concrete implementation of churn v2's R-AI conformance rule.
- **Four-conflict-surfaces-per-NPC (§3.4) is a force multiplier for authoring economy**: the
  combinatorial-census logic in `narrative_engine_design_v2_churn.md` §6 (specificity from binding
  at instantiation) applies exactly here — one well-specified NPC dossier, bound to one settlement's
  state vector, is individually meaningful without being individually authored per event.

### GAP

- **No Accounting-cascade hook.** `governance_play_redesign_v1.md` §5.2 lists "NPC ambition tick in
  the Accounting cascade" as sequence step 4 of 5 — after the settlement registry (step 1), Ledger
  tags as persistent state (step 2), and the event-deck engine itself (step 3). None of steps 1–4
  are built. The dossier schema (§3.1) is fully specified prose; the code that advances
  `ambition.progress` every season does not exist.
- **Blocked on the same registry gap as everything else in this doc**: `governance_play_redesign_v1.md`
  §5.2 states plainly "this redesign cannot fire until the audit's G1 is closed: there is no
  settlement registry (`settlement.py` is 1:1 territory→settlement)." Character-scale friction is
  gated on the same missing substrate as the deck and the geopolitics loop — it is not an
  independent build.
- **The forecast-severance discipline (R-AI) cuts a door the Light Function otherwise wants**:
  churn v2 (`narrative_engine_design_v2_churn.md` §4) states the Light Function's forecast-mass and
  imminence terms may never leak into NPC behavior. This is correct design discipline, but it means
  a promising-looking future (`stake_horizon`, `convergence_candidate`) can never be used to make an
  NPC's ambition timeline *smarter* — NPCs stay heuristic-only by design, permanently, which bounds
  how sophisticated Source-1 friction can ever get without a second, parallel (and currently
  unspecified) "diegetic foresight" system.
- **The commitment/precedent stores that would make character choices persistently exploitable
  don't exist yet**: `narrative_engine_design_v2_churn.md` §5 flags `precedent{...}` and
  `commitment{...}` as "requir[ing] new SC-lane-owned stores that exist nowhere yet" — so an NPC's
  hypocrisy (praising the levy, then being caught profiting from it) is authored as flavor in the
  worked deck (e.g., G505's "her earlier public praise... is now a citable contradiction") but has
  no engine-level store backing it outside that one hand-written card.

---

## §2 · Source 2 — Evolving geopolitics and faction relationships

### EXISTS

- **The Directive** (`governance_play_redesign_v1.md` §1.4): the dual-authority engine — Comply /
  Bargain / Defy, with suspicion accumulation gating a Recall scene or the governor's own
  faction-emergence path (Stage 2→3). This is the up-tier half of the vise and is fully specified.
- **Standing / Demotion Magnitude** (`faction_politics_v30.md` §1.0a, read by
  `governance_ripple_substrate_v1.md` §5): fires on "sustained Duty failure" already, in canon.
- **Mandate aggregation — canon-designed but sim-INERT**: `settlement_layer §1.8` defines Mandate =
  `clamp(round(7·T/(T+6)),0,7)` over settlement L/PS (Treasury = Σ Prosperity×10, `derived_stats §8.1`),
  but per-settlement L/PS is **100/100 inert** — the live loop runs on the scalar `Faction.L` placeholder.
  So it is WIRED in canon/self-audit (§13/§14.1) but **not in `sim/`**: sim-WIRED ≠ canon-WIRED (see `chain_map_v1.md §3`).
- **`scale_signature` on every Key — canon-WIRED but sim-BROKEN above territory**: `key_substrate_v30.md`
  §2.1 stamps `[personal | settlement | territory | peninsula]` — only **4 of the 6** ratified bands (no
  province/duchy/country), and the echo hardcodes `["personal"]`. Above territory the cross-scale plumbing
  is a schema field the substrate cannot populate; §13's WIRED grade is canon-only.
- **The five new settlement levers** (`governance_ripple_substrate_v1.md` §2): StockLevel,
  Assessment tag, Capital-Posture, Consent-Rule, route/corridor Precedent — each passes the "does it
  change what KIND of decision the settlement presents" test, giving settlement types (granary-town
  vs. trade-chokepoint-port vs. garrison-fortress) genuine mechanical identity rather than reskinned
  meters. Status: proposed, gated on open ruling R-1 (in scope, or is identity purely the
  subnational-faction roster?).
- **The worked cross-scale trace** (§5.5, "one famine walked around the entire loop"): individual
  (Aldric's power_base) → settlement (Kronmark's Π/Prosperity) → territory (unbuilt, skipped) →
  faction (Mandate bleed → defensive posture) → peninsula (the Cooling flag correlating the shock
  across multiple settlements) → back down into every governor's response burden. This is the
  clearest existing illustration of how one settlement-scale event becomes a regional power shift
  "no single governor caused."

### OPPORTUNITY

- **The resolution-quality primitive (§5) is the single connective tissue the whole geopolitics
  layer needs**: a computed field on the emitted Key —
  `resolution_quality = w_d·(delivered−demanded)_Directive + w_n·(delivered−demanded)_Need` — read
  by Standing (demotion/promotion), by FI (concealment inventory), by SC (contest predicate), and by
  FA (via Mandate). One arithmetic field, four downstream consumers, zero per-event hand-authoring
  once it exists (§6.4: "authoring an event authors all three ripples at once").
- **The positional/power_base vector (§3) makes "modes of governance" mechanical rather than
  flavor**: the same event, same response, produces a different standing outcome depending on
  whether the governor is patronage-seated (answers up, high `w_d`) or elected (answers down, high
  `w_n`). This is the one genuinely new contribution the ripple substrate adds over
  `governance_play_redesign_v1.md`'s existing Directive/Needs vise.
- **Cross-scale aggregation is bidirectional already in canon** (§7): Mandate feeds back into
  settlement L/PS, so a peninsula-scale shock pushes down into every settlement's Π simultaneously,
  which pushes into individual response burdens, which push back up through resolution Keys into
  Mandate. A faction losing or gaining ground is meant to be the *emergent sum* of many governors'
  locally-rational choices, never an authored strategic-layer event.
- **Territory as connective-tissue scale (R-3, open ruling)**: the substrate names Territory as
  "the one genuine architectural gap" and proposes authoring it as shared-AP-pool + route-network +
  Key-aggregation, explicitly *not* as "a bigger settlement" — this is flagged as the
  highest-leverage architectural ruling in the entire spec (§7, §11).

### GAP

- **Two of eight loop edges are HOOK-NEEDED, one is AT-RISK — by the spec's own self-audit (§13),
  not an external critique**:
  - **§5 event→standing** is HOOK-NEEDED: `faction_politics §1.0a`'s Demotion Triggers read real
    state, but *none reads a per-event resolution signal today* — it needs one authored trigger
    clause, not more research.
  - **§6.2 event→Parliament/SC** is **AT-RISK**: the spec itself admits it asserted "opening Ob from
    the Key magnitude" as a dependency that **canon does not have** — `social_contest_v30 §6`'s
    "Define stakes" step has no hook that reads an external Key. This is flagged in the source doc
    as "the one edge that would fail this spec's own §9 test" — i.e., pattern-matching, not a
    primitive. It must be earned (author a `stakes.source_key` input) or explicitly weakened to "a
    motion may cite the Key" before any downstream design leans on it.
  - **§8 arc feedback→deck re-weight** is HOOK-NEEDED: tag-modifiers on card weight are canon
    (`weight: base + Π-scaling + tag-modifiers`), but resolution Keys writing those modifiers is not
    yet a written convention.
- **Faction count is unreconciled 4–8 across four docs** (`narrative_engine_design_v2_churn.md` §2,
  §10 fork 10; filed as ED-FA-0001) — this "blocks any faction-scope bank/binding table," i.e. it
  blocks exactly the kind of per-faction render/idiom content geopolitical friction needs to read
  as distinct factions rather than a generic label.
- **Territory scale is architecturally unbuilt**, not merely under-specified — `game_state.World`
  is confirmed 1:1 territory→settlement (no registry), so there is no code-level place for the
  "connective tissue" R-3 proposes to live yet.
- **The real, code-level defect underneath the geopolitics loop is territorial transfer being
  BROKEN, not a win-share balance problem.** The previously-circulated "~87% single-faction
  win-share" claim (CLAUDE.md §7's own phrasing) is a **debunked small-N artifact**: per
  `sim/tests/test_f7_smoke_oracle.py`'s own docstring, that figure came from one unguarded
  `run_batch(8, seed=42)` call and the lesson recorded is *"no balance claim without an oracle +
  n ≥ 100"* (`designs/audit/2026-07-12-simulation-test-harness-methodology/simulation_test_harness_methodology_v1.md`
  lines 92–94). The corrected, larger-N golden distribution is 37.5/12.5/12.5/37.5 (ECHO_TRANSPORT).
  **The actual structural defect, verified by
  `designs/audit/2026-07-13-cross-scale-governance-grounding/gap_register_v1.md` GAP-A1 and
  `governance_grounding_v1.md` (lines 303–309), is that `parliamentary_transfer.py` is never called
  from the live loop** — `parliamentary_bridge.py` already fires the seasonal vote, but its output is
  never connected to the existing transfer resolver. The practical consequence: **factions can never
  regain lost territory** — a parliamentary vote to transfer a settlement resolves (Persuasion Track
  passes, Standing changes) but nothing actually moves, so territorial control is a one-way ratchet
  in the live sim regardless of political outcome. This is classified COMPLETE-THE-CHAIN (not
  GENUINE-GAP) — the fix is wiring an existing output to an existing resolver, no new code, no
  import needed — but until it lands, **any geopolitical-friction design that assumes territory can
  change hands and later change back (contested borders, reconquest, a faction's fortunes
  reversing) has no code-level ground to stand on.** This is a materially different, and cheaper,
  problem than "the sim is imbalanced," and conflating the two (as the pre-correction "~87%" framing
  did) risks someone spending balance-tuning effort on a wiring bug.

---

## §3 · Source 3 — Randomized / unexpected events (event decks)

### EXISTS

- **A fully worked, 28-card starter deck** (`goldenfurt_slice/event_deck.md`, S-006 Goldenfurt):
  Petition (3) · Friction (5) · Opportunity (3) · Crisis (4) · Intrigue (5) · Ambition (6) · Thread
  (2). Spine cards carry full schema (triggers, weight, cooldown, npc_refs, the_ask, responses,
  `seeds`/`follow_on` chains); the remaining cards are specified compactly but completely. The deck
  demonstrably self-satisfies its own churn rule: "every card has ≥1 response that emits a `Π`
  delta, and every player-action response writes ≥1 Ledger tag" — verified by the file's own
  in-line fix annotations (e.g. G201's `verify fix deck-F1/CG-6`, G204's `v1.1 fix deck-F3/sim-F6`)
  showing this invariant was actually checked and cards patched to satisfy it.
- **The Π pressure homeostat** (`governance_play_redesign_v1.md` §2.1): `Π_next = clamp(Π +
  Σunserved-Needs + Σactive-Grudges + ΣNPC-ambitions-in-motion + external_shock −
  Σplayer-releases, 0, 10)`, banded 0–2 Opportunity/Ambition, 3–7 dramatic, 8–10 Crisis. Guarantees
  anti-stall and anti-runaway.
- **The card schema** (§2.2) and **draw rule** (§2.4): `1 + ⌊Π/3⌋` cards per season, trigger-filtered,
  weighted, cooldown/exclusion-deduplicated, chaining via `follow_on`.
- **A worked two-season churn trace** (`event_deck.md`'s closing section, and independently
  `governance_play_redesign_v1.md` §4.4): both documents trace the *identical* Goldenfurt scenario
  (G201/G101 levy-vs-petition vise → G303/G502 second-order draws) end to end, showing the loop
  actually closes on paper.
- **The deck named as the canonical replacement for hard-coded content**: §2.4 states "the deck is
  the canonical home for the §4.3 settlement events, generalized from 8 hard-coded rows into an
  open, stateful, GM-/sim-authorable card set."

### OPPORTUNITY

- **The deck is designed to scale**: target 60–100 base cards + chains across 7 families
  (`governance_play_redesign_v1.md` §5.3); the 28-card Goldenfurt slice is roughly a third of that,
  proving the authoring grammar (trigger-predicate × weight × response-tree × `seeds`) generalizes
  across settlement types without becoming generic — each settlement's own state vector, temperament,
  and NPC roster particularizes the same card templates (the "anti-oatmeal defense" logic
  `narrative_engine_design_v2_churn.md` §2 names explicitly for arc templates applies identically
  here).
- **New triggers landed 2026-07-09 from the comparative-governance-research docket** (Clerk
  Corruption → Intrigue, Collective Liability → "Cell Revolt" Crisis, Guild ordenanza → Petition,
  patron-standing loss → "Patron's Rivals Move" Intrigue) show the deck's trigger-predicate grammar
  is already absorbing new content cleanly (`governance_play_redesign_v1.md` §2.3) — the deck format
  itself is not the bottleneck.
- **The event-deck draw has been run through the resolution diagnostic and passed 4 of 5 properties**
  (`governance_ripple_substrate_v1.md` §14.2): legible-band odds (PASS/PARTIAL), uniform leverage
  (PASS, exempt from the √N trap since it's a no-pool weighted-table draw), graded/recoverable
  (PASS, resolves through `d_sigma`'s FAIL_FLOOR .97), and right-engine (PASS, correctly tagged
  `[NEW ENGINE — surface for canon ratification]`). This means the deck-draw mechanism itself is
  mechanically sound and close to ratifiable — it is a *build* gap, not a *design-soundness* gap.

### GAP

- **No event_deck module contract exists.** `governance_ripple_substrate_v1.md` §14.1 maps the
  event draw explicitly as **"NEW ENGINE"** — the weighted-event table is *not in the fixed resolver
  enum* (`module_contracts.yaml`) at all. Per `references/module_contracts.yaml`'s own discipline
  (cross-doc edges surfaced as findings, never silently normalized), this is listed at §14.3 item 4
  as one of the contract deltas still to be authored and Jordan-ratified — nothing has been edited
  into `module_contracts.yaml` yet.
- **No production wiring.** `governance_play_redesign_v1.md` §5.2's build sequence puts "event-deck
  engine — card store + predicate evaluator + Π homeostat" at step 3 of 5, strictly after the
  settlement registry (step 1, **not built** — G1) and Ledger tags as persistent state (step 2,
  **not built**). The 28-card Goldenfurt deck is prose in a markdown file; there is no card-store
  code, no predicate evaluator, no live Π tracker anywhere in the working tree. The entire deck
  layer is currently a design artifact, not a runnable system.
- **One unresolved ratification blocker on the draw mechanism itself**: the resolution diagnostic's
  one finding (§14.2, P-iii) is that the Π band thresholds are **discrete cliffs** — Π 7→8 flips the
  draw from Intrigue-band to Crisis-band with no transition, "a continuous input crossing a discrete
  boundary that jumps the outcome class." This is named as open ruling **R-4** in
  `governance_ripple_substrate_v1.md` §11: intended dramatic threshold, or softened with a
  transition band (7–8 draws from both, Crisis-weighted)? Nothing else about the draw mechanism is
  blocked, but this one Jordan call gates the draw engine's ratification.
- **The debunked "~87% win-share" must not be read as a deck-design problem.** As detailed in §2's
  GAP above, that figure was a small-N sampling artifact of a single unguarded 8-seed batch, now
  superseded by a corrected larger-N golden distribution and fixed by `test_f7_smoke_oracle.py`. The
  actual structural defect it was standing in for — `parliamentary_transfer.py` never being called,
  making territorial control a one-way ratchet — is a **geopolitics/faction-relationship** defect
  (Source 2), not an event-deck defect; it lives in the transfer-resolver wiring, not in card
  triggers, weights, or the Π homeostat. Anyone picking up "fix the deck's balance problem" should
  redirect to GAP-A1 (§2) instead — there is no deck-balance problem on record, only a build gap
  (this section) and a transfer-wiring bug (§2).
- **Every card in the eventual production deck additionally owes three compliance artifacts before
  it is implementable** (`governance_ripple_substrate_v1.md` §14.4): its owning module + resolver
  from the fixed enum, registry-valid Key types for everything it emits/consumes (with any gap
  surfaced as a finding, never silently invented), and — for any draw-resolved branch — a
  resolution-diagnostic P-i…P-v verdict. None of the 28 Goldenfurt cards has been run through this
  pass yet; §14.4 calls this "a design sketch, not an implementable mechanic" until it is.

---

## §4 · How one event feeds the ripple-substrate loop (the cross-cutting trace)

This is the mechanism all three sources are meant to share, per
`governance_ripple_substrate_v1.md`'s core loop diagram (§1) and worked example (§5.5):

```
EVENT fires (deck draw, Π-gated, trigger-predicate-filtered)
   → hits a SETTLEMENT OPERATION via a typed lever (§2: Prosperity/Order/Defense/StockLevel/…)
   → creates a RESPONSE BURDEN on the governing character: three distinct pressure vectors
       (upward — the governed; downward — the Directive/patron; positional — power_base, §3)
   → the RESPONSE is shaped by GOVERNANCE MODE (which verbs are affordable given power_base)
   → the OUTCOME emits a Key carrying a resolution_quality signal (§5) — the arithmetic gap
       between what the Directive/Need demanded and what the season's stat deltas delivered
   → that Key updates the responder's STANDING (advance/demote, via faction_politics §1.0a
       Demotion Magnitude — HOOK-NEEDED, needs one authored trigger clause)
   → the SAME Key ripples to three subscribers:
       - FI (§6.1, WIRED): a negative signal raises the concealment inventory Investigate reads
       - SC/Parliament (§6.2, AT-RISK): intended as a contest predicate/opening-Ob input;
         canon has no such hook today — must be authored or explicitly weakened
       - FA (§6.3, WIRED via Mandate): rolls into Mandate = Σ settlement L/PS, gating
         domain-action windows (expansion/Muster vs. defensive Consolidate/Suppress)
   → these AGGREGATE across scale (§7): individual → settlement → [territory, UNBUILT] →
       faction → peninsula, bidirectionally (a peninsula shock pushes back down into every
       settlement's Π, closing the loop across scale as well as across time)
   → a resolved chain RE-WEIGHTS THE DECK (§8, HOOK-NEEDED): tag-modifiers on future card
       weight are canon machinery already; resolution Keys writing those modifiers is the
       one still-missing convention — once written, this is the mechanism by which an
       emergent arc is "the trace the loop leaves," never authored as a plot.
```

**The honest state of this loop, in one line** (echoing the source doc's own §13 headline): the
spine — event→settlement→Mandate→faction, cross-scale stamping, and the FI ripple — is WIRED on
current canon; the standing bridge and the arc-feedback re-weight are each one authored clause away
(HOOK-NEEDED); and exactly one edge, event→Parliament/SC, is currently AT-RISK of being the kind of
resemblance-not-dependency pattern-matching the substrate's own §9 test exists to catch. None of
this loop is implemented in code yet — every arc above describes what should compose once the
settlement registry, Ledger-tag store, and deck engine (all three: §5.2's build sequence, unbuilt)
exist.

---

## §5 · Consolidated gap register (priority order for anyone picking this up)

| # | Gap | Blocks | Class | Fix-direction |
|---|---|---|---|---|
| 1 | No settlement registry (`game_state.World` is 1:1 territory→settlement) | All three friction sources; the entire ripple loop | GENUINE build gap | `governance_play_redesign_v1.md` §5.2 step 1 — prerequisite for everything else in this map |
| 2 | `parliamentary_transfer.py` never called from the live loop | Source 2 (geopolitics) — territory is a one-way ratchet | COMPLETE-THE-CHAIN (code exists, just needs wiring) | Connect `parliamentary_bridge.py`'s seasonal-vote output to the existing transfer resolver — GAP-A1, `gap_register_v1.md` |
| 3 | No event_deck module contract; not in the resolver enum | Source 3 — the deck can't be ratified as a canonical engine | Ratification-pending | Author the contract entry per `module_contracts.yaml`'s discipline; resolve open ruling R-4 (Π band-cliff, §14.2) first |
| 4 | No event-deck engine code (card store, predicate evaluator, live Π tracker) | Source 3 — the 28-card deck is prose, not a running system | GENUINE build gap | `governance_play_redesign_v1.md` §5.2 step 3 |
| 5 | Ambition-tick not in the Accounting cascade | Source 1 — NPC ambitions don't actually advance without the player | GENUINE build gap | §5.2 step 4 |
| 6 | §5 standing bridge is HOOK-NEEDED, not wired | Source 2 — event outcomes don't yet move Standing | One authored clause | Add a `faction_politics §1.0a` trigger clause reading the resolution_quality Key |
| 7 | §6.2 event→Parliament is AT-RISK (self-flagged pattern-matching) | Source 2 — SC/Parliament ripple has no real hook | Must be earned or weakened | Author `stakes.source_key` consumes-edge on `social_contest`, or downgrade the claim to "may cite" |
| 8 | §8 arc-feedback deck re-weight is HOOK-NEEDED | All three — emergent-arc fuel doesn't yet write back to the deck | One authored convention | Resolution Keys write a tag-modifier delta on future draws |
| 9 | Faction count unreconciled 4–8 across four docs (fork 10, ED-FA-0001) | Source 2 — blocks any faction-scope bank/binding table | Open ruling, filed | Needs Jordan's count ruling |
| 10 | Territory scale architecturally unbuilt (R-3) | Source 2 — the connective-tissue scale between settlement and faction | Open ruling, highest-leverage per the source doc | Author Territory as shared-AP-pool + routes + Key-aggregation, not "a bigger settlement" |

---

## §6 · Crosswalk / citations

Executes no ED on its own; this is an orientation map over already-filed work. Cites: ED-IN-0011
(Churn Engine v2 ratification), the `governance_play_redesign_v1.md` PROPOSAL (unratified),
`governance_ripple_substrate_v1.md` PROPOSED (unratified, self-audited §13), ED-IN-0051
(`gap_register_v1.md`, GAP-A1 territorial-transfer finding), and the corrected win-share finding in
`designs/audit/2026-07-13-cross-scale-governance-grounding/governance_grounding_v1.md`. No new
rulings are made here; §5's priority table is a reading aid, not a sequencing decision — the actual
build sequence remains `governance_play_redesign_v1.md` §5.2's, gated as stated throughout.
