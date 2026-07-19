# VALORIA — Settlement Governance Play Redesign (v1 proposal)

**Status:** PROPOSAL — drafted 2026-06-22. Extends/replaces `settlement_layer_v30 §3.2` player-facing loop; adds the event-deck and NPC-ambition substrate behind PART 4.
**Problem it solves:** As written, a player-governor's mechanically-distinct verbs are four stat-pumps (`Develop`/`Fortify`/`Pacify`/`Administer`). The governance *politics* (dual authority, subnational bargaining, capacity pressure, L/PS→Mandate, fracturing) is held one tier up, at the faction/Provincial-Authority layer. The settlement-as-scene-generator (PART 4) is reactive texture, not a player decision-surface. Net: governing collapses toward "roll one die a season and watch numbers" unless a GM carries it.
**Goal:** Make governing *choosing under constraint*; make the settlement an emergent-narrative engine; and enforce a closed world↔player churn so neither side is ever static.

---

## Part 0 — Design pillars

| # | Pillar | Consequence for the spec |
|---|--------|--------------------------|
| **P1** | Governing is choosing under constraint, not maintaining stats. | Every verb costs a bounded resource (Administration Points) and carries a political side-effect. No free stat-pumps. |
| **P2** | The settlement is a **pressure-driven** scene engine. | Events are the world's *moves*, drawn from current state — not random flavor. |
| **P3** | NPCs have **ambitions and act autonomously**. | The world moves whether or not the player does. NPCs are the deck's fuel and its initiative. |
| **P4** | The **two-stroke churn**. | World→player and player→world alternate and *condition each other*. The loop is closed and guaranteed to turn every season. |
| **P5** | The world **remembers**. | Choices persist as Precedent / Grudge / Debt / Reputation tags that bias future rolls, events, and NPC behavior. |

---

## Part 1 — The Governor's Turn (replaces `§3.2`)

### §1.1 Action economy

A player-governor's season has three layers, resolved in order:

1. **The Directive** (mandatory) — the Provincial Authority's order for the settlement this season. The governor must respond (§1.4).
2. **Governance Phase** — the governor spends **Administration Points (AP)** on governance verbs (§1.3).
3. **Personal Phase** — the player's normal scene actions, unchanged (their own arc).

**Administration Points:** `AP = 2 + FacilityTier_s` (the §1.8 built-infrastructure tier, 0–3) → 2–5 AP/season. Standing 5 governors (Seat/Cathedral) get +1. AP do not carry over. **This is the core constraint: you cannot do everything the settlement needs in one season — you must prioritize, and what you neglect festers (P5, feeds the deck).**

### §1.1a Clerk Capacity — the second, opaque AP source (NEW — ED-SE-0022, 2026-07-09)

**Status: PROPOSED.** A second, orthogonal AP source alongside the `FacilityTier` formula above — the only AP source in the doc that is not visible/transparent up front. Provenance: `designs/audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md` §Step 3 CHN-3.

**Grounding.** The Ming–Qing county magistrate (*zhixián*): a single ranked official governing tens of thousands, backed by unranked private secretaries (*muyou*, personally paid, no state budget line) and clerks/runners (*shúlì*/*yázì*) who did the bulk of actual paperwork — and who were structurally prone to corruption, since the magistrate had no state apparatus to supervise them directly (T'ung-tsu Ch'ü, *Local Government in China Under the Ch'ing*, 1962).

**Mechanic.** New verb **Retain Clerks** (1 AP + `W −1`/season, auto-succeeds, no roll): grants +1 effective AP per point of Clerk Capacity (CC, 0–3 per settlement), uncapped by `FacilityTier`. Each CC point also silently increments a hidden **Clerk Corruption** counter, raising the draw-weight of a new Intrigue-family trigger (a clerk skimming a Levy, selling access, or extorting a Local Actor in the governor's name — §2.3). The counter is discoverable only via `Investigate` (§1.3), never surfaced up front the way every other AP source is. Dismissing clerks (1 AP) stops future accrual but does not undo Grudge/Reputation already generated.

**Status:** promote-ready — self-contained addition to the AP formula plus one new verb, hooking entirely into the existing Intrigue card family and Ledger tag machinery; the only opaque-liability AP source against a doc where every other is transparent.

### §1.2 What replaces "one free governance action"

The old "one mandatory free governance action" is removed. Instead the governor has an **AP budget over a richer verb menu**, so the seasonal decision is *allocation*, not *single-pick*. Companion-governors get a fixed 2 AP (down from a free action) per `settlement_bridge_unification C-04`.

### §1.3 The governance verbs

Each verb: AP cost · roll (existing engine, continuous Ob) · primary effect · **the tradeoff** · **what it churns** (the world-delta it emits, P4/P5).

| Verb | AP | Roll | Effect | Tradeoff (the politics) | Churns (world-delta) |
|------|----|------|--------|--------------------------|----------------------|
| **Develop** | 2 | Cognition + Wealth-history vs Ob ⌊Prosperity/2⌋+1 | Prosperity +1 | Choose funding: **Treasury** (needs Directive room / PA approval) · **Guild charter** (+1 Prosperity faster, Guild Influence +1 in settlement — a standing claimant) · **Corvée** (Order −1, populace strained) | Raises settlement Weight; empowers whichever patron you chose (Precedent tag) |
| **Fortify** | 2 | Military + history vs Ob ⌊Defense/2⌋+1 | Defense +1 | **Garrison** (Löwenritter dependence ↑) · **Militia** (PS +1, but Defense brittle, armed populace = future leverage) · **Walls** (Treasury, slow) | Shifts who holds the swords here; militia seeds future faction-emergence recruits |
| **Keep Order** | 1–2 | varies by method | Order +1 | **Consent** (Charisma, 2 AP, slow, PS +1) · **Force** (Military, 1 AP, fast, PS −1, Local-Actor Disposition −1, rebound risk) · **Clergy** (invite Parish services, 1 AP, Order +1 *and* Church infra creeps in — the Geneva trap, §1.6) | Force seeds Grudge tags + radicalization; Clergy seeds Church-capture vector |
| **Hold Court** | 1 | Charisma/Cognition + Governance-history vs Ob set by dispute | Adjudicate a Local-Actor dispute (a scene). Pick a side. | Ruling for one party raises their Disposition, lowers the other's; sets a **Precedent** (binds future rulings, +1/−1 Ob on related events) | The settlement brings you the conflict (world→player); your ruling realigns local actors (player→world) |
| **Sponsor** | 1–2 | auto / Wealth | Fund festival / market / shrine / guild-hall → durable +1 to a stat + Disposition | Empowers a subnational faction or sets a recurring **expectation** (a Debt tag: skip it next year → Disposition −2) | Creates durable goodwill *and* a durable obligation |
| **Treat** | 1 | Influence + history vs subnational leader (social contest §7) | Strike a *minor* side-deal with a subnational faction (intel, labor, a favor) | Bounded: major grants (management rights, privileges) still need PA ratification → escalate via **Petition**. Each deal is a chit the faction will later call in | Builds a leverage web you're now entangled in |
| **Levy** | 1 | auto | Extract troops / Treasury / intel for the faction (often *to satisfy the Directive*) | L/PS −1 and/or Order −1 in the settlement. The dual-authority extraction tension made literal | Satisfies up-tier, strains down-tier — the squeeze |
| **Investigate** | 1–2 | Cognition + relevant history vs concealment | Surface a covert actor (Niflhel/RM), a secret, a broker | On discovery, **choose**: expose (faction credit, local fear) · expel (removes asset + risk) · co-opt (gain the asset, share its risk) · shelter (its loyalty, your exposure) | Each choice recruits or makes an enemy with its own ambition |

Plus the always-available **Petition / Defy** response to the Directive (§1.4), which costs 0 AP but spends political capital.

**Design note:** the verbs are deliberately *not* orthogonal stat-pumps. `Develop`/`Fortify`/`Keep Order` each force a *method* choice that hands power to a different faction, so optimizing the number costs you politically. That is the EU4-estate / Shadow-Empire principal-agent friction ported down to the player's tier.

**Reconciliation notes (ED-SE-0005, 2026-07-08 — ratified pessimist-action audit, ED-IN-0027).** These refine the verbs above without changing the menu; they bind when this proposal is staged (OPT-16):

- **Investigate — DISTILL.** The concealment *roll* (Cognition + history vs a hidden actor's concealment) is **not respecified here**: it invokes the existing **fieldwork Investigation resolver** (`investigation_systems_v30` Observe/Surveil/Reconstruct). What this verb authors is the settlement-specific **four-way post-discovery disposition** (expose · expel · co-opt · shelter) — that is the genuinely new, load-bearing content; the detection engine is reused, not duplicated. (Shrinks the §5.2 build sequence — one fewer bespoke roll-resolver to author.)
- **Treat — REFINE (chit call-in trigger, previously unspecified).** A Treat side-deal stores its **chit as a Debt-family tag** (§1.6 Ledger of Consequence · *Debt*) on the counterparty. It is **called in when a Friction card that references it fires** (§2.3 Card families · *Friction* ← "Treat chits"), on the same "fires when due" cadence the Debt tag already uses for sponsorship expectations — i.e. at the counterparty's next Friction surfacing, not a free-floating adjudication (this is a no-GM engine). This closes the Q-smooth gap the audit flagged: the trigger is now enumerated, not implicit.
- **Sponsor** is the single canonical patronage verb: it absorbs the retired `player_agency_v30 §9` free "Sponsor settlement event" (Order +1, no downside). Only the **Debt**-bearing form survives, removing the dominant-strategy duplication.
- **Administer** (dropped from `settlement_layer_v30 §3.2`'s four-verb menu) is formally folded, not silently omitted: its information half → **Investigate**, its maintenance half → the "governance action not spent on growth this season" state. No standalone Administer verb is reintroduced.

### §1.3a Locked Extraction Figures — Survey and Encabezamiento (NEW — ED-SE-0018/ED-SE-0019, 2026-07-09)

**Status: PROPOSED.** Two proposals landed as one shared substrate per the judged synthesis recommendation (comparative-governance-research docket §3 S-5): both lock an extraction figure that then decouples from live Prosperity, letting the governor (or the settlement) eat the resulting gap. One locked-figure read-path, two acquisition triggers. Provenance: same docket, §Step 3 SE-JP2, HAB-5.

**The shared substrate.** A settlement may carry a durable **Assessment** tag: `assessed_base`, a locked Prosperity figure. While an Assessment tag is active, `faction_layer_v30` §5.9's Fiscal Stance yield formula and any Levy/Extract Directive target read off `assessed_base`, not live Prosperity. A settlement that has grown since its last Assessment is under-taxed (a legible surplus the governor can exploit or quietly hide); one that has declined is over-taxed relative to real capacity.

**Trigger A — Survey (unilateral).** New verb **Survey** (2 AP, Cognition + Governance-history vs Ob ⌊Prosperity/2⌋+1, ~8-season cooldown). On success, writes/refreshes the Assessment tag at the current Prosperity. *Grounding:* Toyotomi Hideyoshi's *Taikō Kenchi* cadastral survey (1582–1598) — the *koku*/*kokudaka* rating fixed a domain's assessed size, and with it its lord's stipend tier and military-service quota, off one periodically-resurveyed number, never continuously tracked (Wikipedia, "Koku"). **New failure mode:** an Extract/Tax Directive (§1.4) against a stale-high Assessment strips a since-declined settlement below subsistence purely from administrative neglect — Scott's extraction-invariance-detonates-revolt logic (already cited at `settlement_layer_v30` §4.3a), triggered here by *inaction* rather than policy.

**Trigger B — Encabezamiento (negotiated).** New method under the existing `Levy` verb (§1.3), parallel to how `Develop`/`Fortify`/`Keep Order` already force a method choice: **Negotiate Quota** (2 AP, Charisma/Cognition + history vs the settlement's Local Actors as a mass social contest, `social_contest_v30` §7). On success, converts the settlement's per-season variable Levy into a fixed multi-season **Compact** — a new **fifth Ledger-of-Consequence tag family** (§1.6), alongside Precedent/Grudge/Debt/Reputation, locking a Treasury/troop figure for 4–6 seasons. During the term the Extract Directive auto-resolves via the Compact at 0 AP and no further Order/PS penalty, but the figure does not rise even if Prosperity does. In exchange, Local Actors gain standing to bring one Petition per Compact term that the governor must `Hold Court` on to keep the Compact intact; refusing breaks it immediately (reverts to normal Levy, writes a Grudge, blocks renegotiation for 2 seasons). Renewal at term-end is a fresh Negotiate Quota roll, harder if settlement Reputation is Weak/Hated. *Grounding:* the Cortes of Castile's *encabezamiento*, formalized 1534 for the *alcabala* — eighteen chartered cities (Burgos, Toledo, Sevilla, etc.) negotiating fixed ~6-year tax quotas in exchange for redress of grievances (*peticiones*), the crown's key fiscal lever through the 1575 crisis (Chamley; Britannica, "Cortes"; *Hispania*, CSIC).

**Status:** both promote-ready — Survey wraps a periodic-refresh discipline around the already-PROPOSED §5.9 formula without changing its shape; Encabezamiento is a bounded alternative resolution path reusing the existing mass-social-contest resolver. Neither changes any faction roster.

### §1.3b Bind the Cells — Goningumi collective liability (NEW — ED-SE-0020, 2026-07-09)

**Status: PROPOSED.** A new method under the `Keep Order` verb (§1.3), alongside Consent/Force/Clergy. Provenance: same docket, §Step 3 SE-JP1.

**Grounding.** Hideyoshi's 1597 edict (five households for samurai, ten for urban commoners), generalized under the Tokugawa into five-household *goningumi* units: collective tax and crime liability with a reporting group leader answering to the local magistrate (Britannica, "Gonin-gumi").

**Mechanic.** **Bind the Cells** (1 AP — cheaper than Force, and unlike Force carries no PS penalty): partitions the settlement's Local Actors (§4.5) into fixed five-household cells, each with a Group Leader who reports to the governor; Order +1 on success. Once bound, any single member's infraction auto-stamps a durable **Collective Liability** Ledger tag (a Grudge-family variant, §1.6) on the *whole* cell — Disposition −1 to every member, not just the offender — instead of requiring per-actor `Investigate` spend to find the culprit. Stacking three Collective Liability tags on one cell auto-seeds a new Crisis-family card, **"Cell Revolt"** (§2.3). Unbinding costs its own 1-AP verb plus Order −1. The tradeoff: cheap, distributed enforcement against a compounding collective-punishment failure mode disproportionate to the original infraction.

**Status:** promote-ready — adds one new Keep Order method and one new Ledger tag variant inside a doc already at PROPOSED status; reuses existing AP/Disposition/card machinery, forks no faction's identity.

### §1.3c Ordenanza Ratification — guild self-regulation vs. civic check

**Status: PROPOSED (NEW — ED-SE-0023, 2026-07-09).** A new resolution branch under the `Hold Court` verb (§1.3). Cross-references `faction_politics_v30` §2.5 Guild Ladder (Guild Master obligations). Provenance: same docket, §Step 3 HAB-7.

**Grounding.** Spanish *gremios* (craft guilds): guild-authored *ordenanzas* — entry standards, price floors, output quotas, quality rules — required municipal or royal sanction to be enforceable, with continuing municipal inspection to check the guild's own self-interest (Encyclopedia.com, "Guilds (Gremios)"; Academia.edu, "Guild Authorities in Late Medieval Spain").

**Mechanic.** When a settlement's Guild Master (`faction_politics_v30` §2.5, Gu-Std 3+) autonomously writes a new internal *ordenanza* (an ambition-engine action, §3.2), it does not take effect automatically: it generates a Petition-family card, **"Guild seeks Ordenanza sanction"** (§2.3). `Hold Court` gains three resolution branches:

- **Ratify** — the ordenanza's effect applies (e.g., faster Prosperity growth under `Develop`'s Guild-charter funding option), but Guild Influence in the settlement +1 — a standing claimant.
- **Reject** — Guild Master Disposition −2, a Grudge tag, no Prosperity bonus, no Influence creep.
- **Amend** — Charisma/Cognition vs the Guild Master, Ob 2. Success: half the bonus, no Influence gain. Failure: treated as Reject, but at only −1 Disposition.

An ordenanza's entry-standard clause can encode caste exclusion per the existing §2.5 caste note (Masterpiece Examination committees rejecting Einhir candidates); **Ratifying such a clause locks the exclusion in as settlement policy** with no separate roll — no current mechanic otherwise lets a governor unilaterally undo a sanctioned ordenanza short of a fresh Investigate-then-Hold-Court chain.

**Status:** promote-ready — new Hold Court sub-case using only existing verbs, Ledger/Influence mechanics, and the already-ratified Guild ladder's stated Guild Master obligations; no new faction roster action or track.

### §1.4 The Directive — the dual-authority engine

Each season the Provincial Authority issues **one Directive** to the settlement (the controlling faction's AI, or the GM, per the faction priority tree). Typed examples:

- **Extract** ("raise a war-levy of N troops"), **Tax** ("impose the harvest tithe"), **Suppress** ("shut down the RM circle"), **Install** ("seat this Bishop-Governor"), **Host** ("quarter an allied ambassador in a Wing"), **Cede** ("transfer the Fortress to Löwenritter").

The governor must respond — **this is the recurring forced choice the old design asserted but never gave the player a button for** (`§3.1` "when they disagree, tension generates gameplay"):

| Response | Cost | Up-tier effect | Down-tier effect |
|----------|------|----------------|-------------------|
| **Comply** | — | Faction Standing +, trust + | Often strains the settlement (the Directive usually conflicts with a Need, §1.5) |
| **Bargain** | social contest vs PA (§7, you as petitioner) | Soften terms on success; mild suspicion | Partial strain |
| **Defy / Divert** | — | Standing-debt (FAC-02), **suspicion track +1**; at threshold → recall, audit, or replacement | Protects the settlement; Local-Actor Disposition +, PS + |

Suspicion accumulating to a threshold triggers a **Recall scene** (you're summoned to justify yourself — a social contest) or, if you've built enough local L/PS, the seed of *your own* faction-emergence (§6.2): the governor who repeatedly defends the settlement against its own faction is walking the Stage-2→3 path.

### §1.5 Settlement Needs — the other jaw of the vise

Independently of the Directive, the settlement emits **Needs** from its state (deck-driven, §2): low Order → a petition for justice; famine → relief demand; a Guild → a charter request; a flourishing settlement → an ambition to expand. The drama is that **the Directive and the Needs routinely conflict, and your AP can't serve both.** Comply with the Extract Directive *and* meet the famine-relief Need? You don't have the AP or the Treasury. Choose — and the unserved side becomes next season's escalation.

### §1.6 The Ledger of Consequence (P5)

Every governance choice writes a durable per-settlement tag the world remembers:

- **Precedent** — a ruling/policy that biases related events (±1 Ob, opens/closes deck cards).
- **Grudge** — an actor/faction wronged; raises their hostile-action weight, seeds Intrigue cards.
- **Debt** — an obligation (a sponsorship expectation, a called-in Treat favor); fires when due.
- **Reputation** — the settlement's read on the governor (Just / Harsh / Generous / Weak / Hated), modifying Local-Actor starting Disposition and event tone.
- **Compact** (NEW — ED-SE-0019, 2026-07-09; §1.3a) — a fifth family: a negotiated, fixed-term extraction agreement (Encabezamiento) locking a Treasury/troop figure for its term and granting the counterparty a bounded Petition right. Distinct from Debt (which fires once, when called in): a Compact fires *every season of its term* until renewal or breach.

Tags persist across the governor's tenure and **survive succession** (the next governor inherits the settlement's memory), which is what makes player→world stick.

---

## Part 2 — The Event Deck (the settlement-as-scene-generator)

The deck is the **world's move-generator**. It is pressure-driven and stateful, not a random table.

### §2.1 Pressure model

Each settlement carries a **Pressure** scalar `Π` (0–10), the homeostat that keeps the churn in the dramatic band:

```
Π_next = clamp( Π + Σ(unserved Needs) + Σ(active Grudges) + Σ(NPC ambitions in motion)
                  + external_shock − Σ(player releases this season), 0, 10 )
```

- **Π low (0–2):** the deck draws Opportunity/Ambition cards (the world offers, tempts, recruits) — quiet seasons still *move*.
- **Π mid (3–7):** the dramatic band — Petitions, Frictions, Intrigues.
- **Π high (8–10):** Crisis cards escalate (revolt, schism, assassination, defection). Sustained high Π forces a breaking event.

The homeostat guarantees **anti-stall** (Π never sits at 0 — Opportunity/Ambition cards inject motion) and **anti-runaway** (player releases and resolved crises bleed Π back down). The world is never quiet and never an unsurvivable spiral.

### §2.2 Card schema

```yaml
card:
  id: EVT-Sxxx
  family: Petition | Friction | Opportunity | Crisis | Intrigue | Ambition | Thread
  triggers:                      # state predicates — ALL must hold
    - settlement.Order <= 2
    - settlement.has_subnational(RM)
    - actor.<Conviction>.threatened
  weight: base + Π-scaling + tag-modifiers
  cooldown: 2                    # seasons before it can recur
  excludes: [EVT-Syyy]           # mutually exclusive chains
  the_ask:                       # what the world demands of the governor
    summary: "The miller's son was conscripted; the Magistrate petitions for his release."
    pressure_if_ignored: +2
  responses:                     # the player's verbs, with consequences
    - verb: Hold Court (rule for)   -> Magistrate.Disp +1, Garrison.Disp -1, Precedent: "conscription-exempts-only-sons", Π -2
    - verb: Comply with Levy        -> PS -1, Magistrate.Disp -2, Grudge(Magistrate), Π +1, seeds EVT-S101 (son radicalizes)
    - verb: Bargain (PA)            -> social contest; partial
    - ignore                        -> Π +2, Grudge(Magistrate), Reputation -> "Weak"
  follow_on:                     # what this seeds (the chains)
    - on Grudge(Magistrate): unlock EVT-S140 "Magistrate backs a rival"
```

### §2.3 Card families

| Family | The world is… | Seeded by |
|--------|---------------|-----------|
| **Petition** | …asking you to adjudicate | Local-Actor Convictions + Needs |
| **Friction** | …forcing a dual-authority / subnational clash | Directive ↔ Need conflict; Treat chits |
| **Opportunity** | …offering (festival, windfall, recruit, alliance) | High stats, low Π, NPC goodwill |
| **Crisis** | …breaking (famine, raid, revolt, plague, schism) | High Π, stat floors, external shock |
| **Intrigue** | …scheming behind your back (blackmail, assassination, covert actor) | Grudges, covert factions, NPC ambitions |
| **Ambition** | …an NPC making *their* move (claiming, betraying, rising) | The NPC ambition engine (Part 3) |
| **Thread** | …manifesting the metaphysical (RS bleed, Calamity edge) | Thread Proximity, RS thresholds |

**New triggers landed 2026-07-09 (comparative-governance-research docket — see §1.1a/§1.3a/§1.3b/§1.3c above for the full specification of each):** *Intrigue* — "Clerk skims/sells access/extorts" (seeded by Clerk Corruption, §1.1a); *Crisis* — "Cell Revolt" (seeded by 3 stacked Collective Liability tags, §1.3b); *Petition* — "Guild seeks Ordenanza sanction" (seeded by a Guild Master's autonomous ordenanza, §1.3c). A fourth, **"Patron's Rivals Move"** (Intrigue), is seeded by a Guild's backing patron losing standing — specified at `settlement_layer_v30` §3.3b, not here, since the patron-standing state it reads lives in the settlement's subnational-faction record rather than this deck's own state.

### §2.4 Drawing

Each season: draw **`1 + ⌊Π/3⌋` cards** (1 at peace, up to 4 in crisis), filtered by trigger predicates, weighted, de-duplicated against cooldowns/exclusions. Cards chain (a `follow_on` seeds next season's deck), escalate (ignored Petitions become Crises), and resolve (player verbs apply consequences and release Π). **The deck is the canonical home for the §4.3 settlement events, generalized from 8 hard-coded rows into an open, stateful, GM-/sim-authorable card set.**

---

## Part 3 — NPC specification (the conflict-maximizing schema)

NPCs are the deck's fuel and its initiative. To **maximize opportunities for conflict/interaction**, every significant settlement NPC (Local Actors §4.5, subnational officers, the governor's own court) is specified for *agency*, not just attitude.

### §3.1 The dossier schema

```yaml
npc:
  identity: name (culture-derived), role, faction/none, settlement
  convictions: [1-2]             # core drives (existing canon). What they will NOT compromise.
  ambition:                      # NEW — what they are actively trying to achieve
    goal: "become Magistrate of S-017"
    method: lawful | factional | violent | covert   # ties to ethic
    timeline: seasons-to-act     # they act on this whether or not the player engages
    progress: 0-5                # advances autonomously each season (§3.3)
  ethic: alpha/beta              # the temperament α/β axis (outcomes vs conduct) — already canon
  loyalty: faction + Disposition(governor) + Disposition(others via Knots)
  leverage:                      # the hooks — what makes them playable
    wants: [...]                 # what you can offer
    fears: [...]                 # what you can threaten
    secret: "..."               # what Investigation can surface
  relationships: Knots (PP-724)  # allies, rivals, kin, debts — the relational graph
  trajectory:                    # NEW — how they act when the player isn't looking
    if ambition blocked: -> shifts method (lawful -> factional -> violent/covert)
    if Disposition < -2: -> seeks a rival patron / defects / sabotages
    if Conviction violated by governor: -> Grudge, escalates
```

The two additions that make NPCs *churn the world* are **`ambition`** (they want something and pursue it) and **`trajectory`** (they act on it autonomously, and re-plan when thwarted).

### §3.2 The ambition engine (the world's initiative)

Each Accounting, every significant NPC **advances their ambition by 1** (or more, if conditions favor) unless the player or another actor intervened. When `progress` hits its threshold, the NPC **acts** — emitting an Ambition card (they claim the office, betray the patron, call in a Knot, expose a secret). This is the `sim_npc_as_player` principle made load-bearing: **the settlement's NPCs are playing their own game on the same clock as the player.** The player who ignores the ambitious Magistrate doesn't get a frozen NPC — they get a Magistrate who, three seasons later, has the votes to challenge them.

### §3.3 Speccing for maximum friction

Author NPC sets so their drives *collide*:

- **Orthogonal Convictions** within a settlement (the Priest's "souls before law" vs the Magistrate's "law before mercy") guarantee that any ruling (`Hold Court`) pleases one and wrongs the other.
- **Overlapping ambitions** (two NPCs want the same office/charter) force the governor to be kingmaker — and make an enemy by choosing.
- **Cross-cutting Knots** (the Guildmaster is the rival Magistrate's brother-in-law) mean local moves ripple through the relational graph.
- **Ethic spread** (α-outcomes pragmatists vs β-conduct principled) ensures the same crisis reads as opportunity to some and betrayal to others.

### §3.4 Example dossier (abbrev.)

```yaml
npc: Hedda Vorn — Magistrate of S-017 (no faction)
convictions: ["the law is the only shield the weak have"]
ambition: { goal: "win the Gransol parliamentary seat", method: lawful->factional, timeline: 4, progress: 1 }
ethic: beta (conduct-weighted)
leverage: { wants: ["a fair grain court"], fears: ["her brother's smuggling exposed"], secret: "her brother runs the dock black market" }
relationships: Knots[ rival: Guildmaster Orsk; kin: smuggler brother Tomas ]
trajectory: { if blocked: petitions louder -> backs a rival faction; if Conviction violated: leads the unrest }
```

This single NPC can generate: a Petition (grain justice), a Friction (her vs Orsk), an Intrigue (the brother's black market — surface via Investigate, then leverage or expose), and an Ambition card (her parliamentary bid) — four conflict surfaces from one well-specified person.

---

## Part 4 — The churn engine (world ↔ player)

The unifying mechanism: **a two-stroke loop where each stroke writes the preconditions of the other.** Neither side is ever static; the loop is *guaranteed to turn* every season.

### §4.1 The guarantee

- **The world always acts on the player:** the Directive is mandatory, and the deck draws `≥1` card every season (Π never sits at 0; §2.1). The player can never have a "nothing happens" turn.
- **The player always acts on the world:** every governance verb emits a world-delta (a stat, a Disposition, a Ledger tag; §1.3). The player can never act without changing the pressure field that drives next season's draw.

### §4.2 World → player stroke (the world's turn)

Resolved at season open: Π recomputes → the deck draws → NPCs advance ambitions → the Provincial Authority issues the Directive → rivals/subnationals maneuver. The player is handed demands, opportunities, and crises *that are responses to last season's deltas.*

### §4.3 Player → world stroke (the player's turn)

The player spends AP on verbs, responds to the Directive, and plays the scenes. Each choice mutates: settlement stats, NPC Dispositions **and ambitions** (advanced or thwarted), faction alignments, and the Ledger. These mutations become the trigger predicates and weights for next season's world-stroke.

### §4.4 Worked two-season example (the loop closing)

> **S1, world→player:** Π=4. Directive: *Extract* a war-levy. Deck draws a Petition (the Magistrate asks to spare only-sons). The vise: comply with the levy *or* honor the petition.
> **S1, player→world:** You `Defy/Divert` the levy partially and `Hold Court` for the Magistrate. → Standing-debt +1, suspicion +1 (up-tier); Magistrate.Disp +2, PS +1, Precedent "only-sons exempt", Reputation→"Just" (down-tier). Π −2.
> **S2, world→player:** The deltas *are* the new world. Suspicion crossed a notch → Directive escalates: *"restore the levy or be audited."* The grateful Magistrate's ambition (parliamentary seat) advanced → she offers you an alliance (Opportunity card). The Garrison commander you stiffed has a new Grudge → Intrigue card: he leaks your defiance to a Crown rival.
> **S2, player→world:** You accept the Magistrate's alliance (now you have a parliamentary proxy — Stage-2→3 faction-emergence progress) but it deepens your break with the Crown… and so on.

Every move the player made became a move the world made back, and vice versa — **they churn each other.**

### §4.5 Homeostasis (keeping the churn alive)

The Π homeostat (§2.1) is the anti-flatline / anti-death-spiral governor: it injects Opportunity/Ambition cards when quiet and bleeds off when the player resolves crises, keeping the settlement in the dramatic band indefinitely. A settlement the player has "solved" doesn't go quiet — its low Π surfaces *ambition* and *opportunity* cards, i.e., the world starts offering rather than threatening, but it never stops moving.

---

## Part 5 — Integration & open questions

### §5.1 Hooks into existing canon (build on, don't reinvent)

- **Convictions, Disposition, social contest §7, Domain Actions, Accounting** — reused directly as the resolution + consequence substrate.
- **Knots / relational graph (PP-724)** — the NPC `relationships` field *is* this graph; ambitions ripple through it.
- **Temperament α/β** — the NPC `ethic` field; already canon at territory grain, now applied at NPC grain.
- **L/PS → Mandate (§1.8)** — governance verbs and Directive responses are the per-settlement L/PS drivers the §1.8 model needs but doesn't currently source from player action.
- **`sim_npc_as_player`** — the ambition engine (§3.2) is the settlement-scale instance of this existing principle.
- **NPC priority trees (npc_behavior §8.2)** — the Provincial-Authority Directive generator and NPC trajectory both read from these.

### §5.2 What the sim needs first (gated by the audit)

This redesign **cannot fire** until the audit's `G1` is closed: there is no settlement registry (`settlement.py` is 1:1 territory→settlement). Sequence:
1. **Settlement registry** in `game_state.World` (audit G1) — prerequisite for everything here.
2. **Ledger tags** as persistent per-settlement state (§1.6).
3. **Event-deck engine** — card store + predicate evaluator + Π homeostat (§2).
4. **NPC ambition tick** in the Accounting cascade (§3.2).
5. **Directive generator** off the faction priority tree (§1.4).

### §5.3 Open balance questions

- AP curve (2–5) vs verb costs — is the squeeze tight enough to force real triage without paralysis?
- Π weights — tuning the homeostat band so quiet settlements *offer* without going dull and hot settlements escalate without unsurvivable spirals.
- Suspicion→recall thresholds vs faction-emergence thresholds — the defiant governor should feel the knife-edge between "promoted" and "purged."
- Deck authorship load — how many cards constitute a "robust" deck (target: ~8–12 per family × settlement-type modifiers ≈ 60–100 base cards + chains)? GM-authorable vs sim-generated split.

---

## Part 6 — Summary: what the player ACTUALLY does now

Each season as governor, you:
1. **Answer the Directive** — comply, bargain, or defy your own faction (a real, consequential fork).
2. **Spend 2–5 AP** across a menu of 8 verbs that each force a *method* choice handing power to a different faction — you cannot optimize the numbers without paying politically.
3. **Play the scenes the settlement throws at you** — petitions, frictions, intrigues, and ambitious NPCs making their own moves, all drawn from the settlement's current pressure-state.
4. **Watch your choices become the world's next moves** — every action writes a Ledger tag and shifts an NPC's ambition, which *is* next season's deck.

Governing is no longer four stat-pumps. It is the continuous, two-sided negotiation between a faction above you, a populace below you, and a cast of NPCs pursuing their own ends on the same clock you are — each of you, every season, churning the other.
