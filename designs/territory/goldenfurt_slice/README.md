# Goldenfurt Governance Vertical Slice (v1)

**What this is:** a single, interlocking worked example of the governance redesign (`../governance_play_redesign_v1.md`), built end-to-end around one real Town — **S-006 Goldenfurt**, a Crown breadbasket river-town in Kronmark province. Three artifacts that must fit together:

| Artifact | What it delivers |
|----------|------------------|
| [npc_cast.md](npc_cast.md) | 6 collision-wired NPC dossiers + 3 minor actors — the deck's fuel and initiative |
| [event_deck.md](event_deck.md) | a 28-card pressure-driven deck across all 7 families — the world's moves |
| [sim_build_spec.md](sim_build_spec.md) | an implementable plan to run it (registry, ledger, deck engine, ambition tick, Directive generator) |

**Status:** PROPOSAL, 2026-06-23. Authored directly (the authoring workflow died three times on session/rate/spend limits); the **adversarial verification workflow did run on rerun** — see [verification_findings.md](verification_findings.md), with its clear bug-fixes folded into this commit.

---

## Why Goldenfurt

A grain town on a tolled river ford maximizes collision with a clean Crown-as-Provincial-Authority frame: the Guild wants the toll, the Ministry wants the levy, the Church wants the souls, the RM keeps the old rites in the hamlets, and Niflhel smuggles under all of it. Famine, war-levy, tithe, hoarding, and smuggling are *organic* here, not bolted on.

```
            CROWN  ── Directive (Extract/Tax/Suppress/Host) ──►  YOU (Governor)
              ▲                                                    │
   suspicion / report (Konrad G06)                    AP verbs · Ledger tags
              │                                                    ▼
        ◄──────────────  GOLDENFURT  ──────────────►  Guild(Orsk) · Church(Wessel)
        Hedda(law) · Tomas(river) · Greta(RM)          each pulling its own way
```

## How the three artifacts interlock

- Each **NPC** (`npc_cast`) has a `fires_card` → an **Ambition card** (`event_deck` G601–G606) and an *autonomous advance* the **ambition tick** (`sim_build_spec §6`) runs each Accounting.
- Each **deck card** references NPCs by the fixed ids and writes **Ledger tags** the **registry** (`sim_build_spec §1–2`) persists.
- The **Directive generator** (`sim_build_spec §4`) issues the mandatory world→player move that the Friction cards (G201–G205) dramatize.
- The **Π homeostat** (`sim_build_spec §5`) decides how many cards draw and biases families by pressure — the engine that keeps the town in the dramatic band.

## A full season at Goldenfurt (the loop in one page)

> **You are the newly-assigned Governor. AP = 3 (Town, FacilityTier 1). Π = 4.**
>
> **WORLD → PLAYER (season opens):**
> - Π recomputes; the deck draws `1 + ⌊4/3⌋ = 2` cards.
> - The Crown's Directive arrives via Bailiff Ems: **Extract** a war-levy → `EVT-G201`.
> - Deck draws `EVT-G101` ("Only Sons" — Mertha's boy is taken) and `EVT-G103` (Sister Aldith begs famine relief).
> - NPC ambitions tick: Orsk +1 (grain leverage), Wessel +1 (Order is low).
>
> **THE VISE:** the Directive (extract grain & men) directly contradicts two Needs (don't conscript the widow's son; feed the town). 3 AP cannot serve all three.
>
> **PLAYER → WORLD (your turn):**
> - **Directive:** you `Defy/Divert` the levy → suspicion +1, **Konrad +1 → G606**, PS +1, Hedda +2, `Reputation:Just`.
> - **1 AP `Hold Court`** for Mertha → `Precedent:only-sons-exempt`, Garrison −1, Π −2.
> - **2 AP `Sponsor`** modest relief → Treasury −, Order +1, PS +1, `Debt:relief-expected-next-year`.
> - Your personal scene actions go to your own arc.
>
> **ACCOUNTING:** Prosperity → Crown Treasury; Order → Kronmark Accord (floor-avg); Local-Actor Dispositions update; suspicion logged; ambition ticks applied; Π settles to ~2.
>
> **NEXT SEASON the world answers:** suspicion notched → the Directive escalates ("restore the levy or face audit"); grateful Hedda's bid advances → `EVT-G303` (alliance) draws; Orsk reads weakness → `EVT-G502` (his whisper to Konrad) draws. Your S1 choices *are* S2's deck.

That is the churn: you never had a turn the world didn't act on, and the world never had a turn your choices didn't shape.

---

## Coherence self-check (the verifier pass, done by hand)

| Check | Result |
|-------|--------|
| Every deck `npc_ref` resolves to a real dossier | ✅ all refs ∈ {G01–G06, LA-G01–G03} |
| Every NPC `fires_card` exists in the deck | ✅ G601–G606 present, one per NPC, each resolving by relationship/state |
| Sim registry models every field the deck/dossiers use | ✅ stats, L/PS, facility_tier→AP, suspicion, Π, subnational footholds, ledger kinds (Precedent/Grudge/Debt/Reputation/Leverage), NPC ambition progress all in `Settlement`/`LedgerTag`/ambition runtime |
| All 7 card families present | ✅ Petition 3 · Friction 5 · Opportunity 3 · Crisis 4 · Intrigue 5 · Ambition 6 · Thread 2 |
| Churn invariant — every card can change the world; every NPC acts autonomously | ⚠ **verified on the 7 spine cards; the 21 compact rows assert but don't show the Π-delta+Ledger triple** (G604/G605 lacked it). See [verification_findings.md](verification_findings.md) CG-4/CG-5. |
| Directive (comply/bargain/defy) wired into Frictions | ✅ G201 (Extract), G202 (Tax), G203 (Suppress), G205 (Host); Geneva trap in G204 |

**Adversarial verification ran (2026-06-23)** — a 4-lens skeptic pass surfaced **32 findings (15 high)**. The clear bugs and missing fields are fixed in this commit; the design-revision items are tracked. Full record: **[verification_findings.md](verification_findings.md)**. Headlines:
- Fixed ✅ — mis-signed Π homeostat term (pinned toward 0, not 3); 7 deck-referenced fields the sim spec never modeled (directive, religious_building, church_attention, faction-emergence, treasury, open_needs); G201's zero-Π-delta vise; the suspicion track being purely reactive; the README overclaim above.
- Fixed in **v1.1** (this branch) — the G606 recall death-spiral (a `Submit to audit` escape + Konrad capped +1/season), the G204 Geneva vise (a secular `Keep Order: Consent` relief; Decline Π-neutral), G602/G604/G605 payoff-for-play forks, Tomas reachability (the Old Brun lever), and Greta's neglect-escalation.
- Still ⏳ — predicate-grammar history triggers (sim-F4), the empty Wessel/Greta collision card (npc-F4), decorative-Knot wiring (npc-F5), ethic mechanization (npc-F6), and numeric tuning (AP curve, Π band, suspicion→recall threshold) pending the §9 sim sweep.

## Build status / what's next

**S0–S1 are now built** (this branch): `sim/territory/registry.py` (the Settlement registry — closes audit gap **G1**) + `sim/territory/ledger.py` (durable Ledger tags), `World.settlements`, and a registry-backed path in `settlement.py` so the §1.3 multi-settlement province floor-average finally fires over real members. Covered by `tests/sim/territory_registry/test_registry_ledger.py` (6 tests, passing: AP economy, ledger-survives-succession, single-valued Reputation, 3-settlement aggregation, registry-backed derived values, and the legacy 1:1 fallback intact).

Next, in order: **S2** governance verbs + AP economy · **S3** Directive generator + comply/bargain/defy · **S4** deck engine + Π homeostat · **S5** NPC ambition tick · **S6** the Goldenfurt content pack. The acceptance test remains the two-season churn trace reproducing end-to-end in the sim.
- Deferred ⏳ v1.1 — the G606 recall death-spiral, the G204 Geneva vise (no acceptable out), G602/G605 lacking payoff-for-play, Tomas being unreachable in a well-governed town, and Greta not escalating on neglect.
- Still open — `Thread` family is thin (2 cards); numeric tuning (AP curve, Π band, suspicion→recall threshold) is unvalidated pending the §9 sim sweep.

## Build status / what's next

This slice is **content + spec only**; none of it runs until `sim_build_spec §7 S0` (the settlement registry, audit gap G1) lands. Recommended order: build S0–S1 (registry + ledger), port the Goldenfurt content to the `content/` YAMLs, then S2–S6. The acceptance test is the two-season trace above reproducing in the sim.
