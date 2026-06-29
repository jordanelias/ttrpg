# VALORIA — Faction Politics Throughline Resolutions v1
## Date: 2026-04-17 | PP-661 | ED-659
## Status: CANONICAL (approved Jordan 2026-04-17)
## Scope: Resolve 10 second-order integration questions raised by PP-660 faction politics rank-ladder expansion.
## Supersedes: none (new document)
## Cross-references: faction_politics_expanded_v1 (primary source), player_agency_v30 §3/§5/§7, settlement_layer_v30 §1, npc_behavior_v30 (new §11), baralta_crown_claim_v30 (new §7), threadwork_v30 (ED-629 stress test open), coverage_matrix.

---

# §0 — AUDIT ORIGIN

PP-660 committed a comprehensive faction politics rank-ladder expansion (Standing 0–7, sub-office ladders, caste integration, Ministry expansion, Generational Shift fix). Post-commit audit identified 10 second-order integration questions that the register opened but did not close. This document addresses each with canonical resolution.

| # | Throughline | Resolution locus | New ED |
|---|-------------|------------------|--------|
| 1 | Caste starting-state opacity — no onboarding signal for caste × faction viability | player_agency §7.1 + this doc §1 | ED-659 (batch) |
| 2 | Duty system contradicts Std 0 Initiation Duty — §3.2 auto-generates Duty; §3.4 says 0–5 range | player_agency §3.2, §3.4 | ED-659 (batch) |
| 3 | CI × Warden asymmetry — Warden ladder not covered by CI interaction; no rank ladder for RM-when-active | this doc §3, §4 (amends faction_politics §2.7 + adds RM stub) | ED-659 (batch) |
| 4 | Generational × Coup × IP clock convergence — Torben maturation interacts unspecified with 3 other clocks | baralta_crown_claim §7 (new section) | ED-659 (batch) |
| 5 | NPC roster capacity — ~35 NPCs now load-bearing; companion app limits unverified | npc_behavior §11 (new section) | ED-659 (batch) |
| 6 | Hall Tier is flavor text — no settlement_layer mechanical hook | settlement_layer §1.4 (new section) | ED-659 (batch) |
| 7 | Warden × Thread stress test (ED-629) open P0 integration | this doc §3.3 cross-reference note | — (flag only) |
| 8 | ED-NEW-06 lineage — confirmed archived as ED-475 (2026-04-12) | no action | — (closed) |
| 9 | SIM-POL-R01–R05 discoverability — debt invisible outside register | coverage_matrix.md append (this commit) | — (discoverability) |
| 10 | Register-split opportunity — Part 1-2 (spec), Part 3 (philosophy), Part 5-7 (contract) | Future-split marker in faction_politics §0 | — (future) |

---

# §1 — CASTE STARTING-STATE ONBOARDING (Throughline 1)

## §1.1 The Problem

PP-660 Part 3 made caste load-bearing: Northern/Central/Southern Einhir affect advancement gating, Renown rates, Initiation Duty Ob, Inner Circle Disposition floors, and Conviction Scar risk. A player who picks "Southern Einhir + Crown + Martial branch" at character creation is choosing a structurally harder game than the same player picking "Northern Einhir + Crown + Martial branch." Without an onboarding signal, this asymmetry is invisible at the decision moment.

This is not a flaw to remove — Valoria's caste system exists precisely because oppression is structural and invisible to those not subject to it. **But informed consent at character creation is a design requirement.**

## §1.2 Resolution: Viability Matrix at Character Creation

player_agency §7.1 is revised to add:

1. **Caste selection step** (currently implicit via "faction alignment" step; now explicit).
2. **Viability Matrix display** — a 4-faction × 3-caste × 3-branch grid shown to the player before final selection.
3. **"Recommended pairing" advisory** — non-binding, surface-level flag indicating which caste-faction-branch combinations play at baseline, elevated, or reduced difficulty.
4. **"Why this matters" narrative note** — one-paragraph explanation that caste is a structural game element, not cosmetic, and that a reduced-difficulty pairing is not an "easy mode" but a different game.

## §1.3 Viability Matrix (canonical)

**Legend:** ★★★ Favored — structural tailwinds (e.g., lower Ob at rank gates, preferential inner-circle Disposition). ★★ Standard — default progression rules. ★ Gated — structural headwinds (higher Ob, Disposition penalties, rank ceilings). ✕ Closed — effectively impossible without Extraordinary Circumstances per LIN-02.

| Faction × Branch | Northern Einhir | Central Einhir | Southern Einhir |
|------------------|-----------------|----------------|-----------------|
| Crown — Martial | ★★★ | ★★ | ★ (Std 4+ gated) |
| Crown — Administrative | ★★★ | ★★ | ✕ (Std 5+ effectively closed) |
| Crown — Intelligence | ★★ | ★★ | ★★ (caste-neutral by necessity) |
| Hafenmark — Judicial | ★★ | ★★★ | ★ (procedural +1 Ob at Std 2→3) |
| Hafenmark — Commercial | ★★ | ★★★ | ★ (Guild-caste-profit structural) |
| Hafenmark — Martial | ★★ | ★★ | ★★ (caste-neutral) |
| Varfell — Martial | ★★ | ★★ | ★★★ (Maret Uln solidarity at Std 3+) |
| Varfell — Resource | ★★ | ★★ | ★★ (caste-neutral) |
| Varfell — Cultural | ★ | ★★ | ★★★ (Skald-Chief endorsement easier) |
| Varfell — Warden | ★ (lower baseline TS) | ★★ | ★★★ (higher baseline TS) |
| Varfell — Foreign | ★★ | ★★ | ★★ |
| Church — Fortitude | ★★★ | ★★ | ✕ (Templars structurally closed) |
| Church — Justice | ★★★ | ★★ | ✕ (Inquisitors structurally closed) |
| Church — Prudence | ★★ | ★★ | ★ (extraction-target tension) |
| Church — Temperance | ★★ | ★★★ | ★★ (Klapp scholar caste-transcendent) |
| Löwenritter (sub-office) | ★★ | ★★ | ★ (Std 3+ Ehrenwall endorsement-gated) |
| Riskbreakers (sub-office) | ★★ | ★★ | ★★★ (outsider status = covert asset) |
| Guilds (sub-office) | ★★ | ★★★ | ★ (Masterpiece Examination bias) |
| Niflhel (informal) | ★★ | ★★ | ★★★ (caste-blind by necessity) |
| Wardens (sub-office) | ★ (TS threshold harder) | ★★ | ★★★ (TS baseline favor) |

## §1.4 Character Creation Flow (revised)

Step order for character creation (additive to existing steps):

1. Write 3 Convictions (existing, player_agency §2.2).
2. Choose caste background (new): Northern / Central / Southern Einhir.
3. Display Viability Matrix filtered to the chosen caste.
4. Choose faction alignment (or independent) — with matrix visible.
5. If faction chosen at Standing ≥ 3 branch: choose specialty branch (existing from PP-660, but elevated in importance).
6. Starting Standing = 0 (Petitioner) for faction members; independent remains independent. *(Change from prior §7.1 which derived Standing = 1 — see §2 below.)*
7. Display Initiation Duty preview for the chosen faction-branch-caste combination.

## §1.5 "Why this matters" narrative text (canonical, display verbatim to players)

> Valoria's caste system is not a difficulty setting. It is a structural feature of the peninsula's politics. A Southern Einhir character facing the Crown is not playing a harder version of the same game — they are playing a different game, one where covert paths (Riskbreakers, Niflhel, Wardens) are structurally open while overt institutional advancement is structurally difficult. A Northern Einhir character facing Varfell's Cultural branch faces the mirror challenge.
>
> If this is your first Valoria campaign, a Standard (★★) or Favored (★★★) pairing is recommended. A Gated (★) or Closed (✕) pairing is a deliberate thematic commitment, not a mistake. Both produce valid stories.

---

# §2 — STANDING 0 INITIATION DUTY × DUTY SYSTEM RECONCILIATION (Throughline 2)

## §2.1 The Problem

player_agency §3.2 says "each season the player's faction leader assigns one Duty." player_agency §3.4 says "Success: Standing +1 (faction-specific track, 0–5)." Both are now contradictory with PP-660's 0–7 ladder and Initiation Duty gate at Standing 0.

## §2.2 Resolution: §3.2 Carve-Out + §3.4 Range Update

**§3.2 revised generation logic:**

Add new paragraph after existing generation rules: *"Duty assignment requires Standing ≥ 1. At Standing 0 (Petitioner), the player receives the **Initiation Duty** only — a faction-specific scene arc (faction_politics_expanded_v1 §1) that must be completed before standard Duty generation begins. The Initiation Duty is not drawn from the faction AI priority stack; it is a fixed narrative gate. Successful completion transitions the player to Standing 1 and activates the Duty system as defined below."*

**§3.4 revised ladder references:**

Replace: *"Standing +1 (faction-specific track, 0–5). High Standing unlocks: ... authority to issue sub-commands to NPC officers (Standing 4), candidacy for faction leadership succession (Standing 5)."*

With: *"Standing +1 (faction-specific track, 0–7 per faction_politics_expanded_v1 §1). Rank thresholds unlock: Standing 2 (faction intelligence access), Standing 3 (council observation, specialty branch selection, Formal Recognition Event), Standing 4 (NPC officer sub-commands, +1 scene action), Standing 5 (treaty-level standing, inner-circle adjacency), Standing 6 (inner-circle voting, +2 scene actions), Standing 7 (succession-eligible, Regent-Designate authority)."*

**§3.4 failure condition revised:** *"Below Standing 0 is not possible — Standing 0 is the minimum institutional state (Petitioner). A player who fails the Initiation Duty remains at Standing 0 until they complete it or declare for a different faction. A player who fails a Duty at Standing 1+ drops by 1 step but cannot fall below Standing 1 (once initiated, the rank is floor-protected unless explicitly dismissed — see ED-647 for dismissal mechanics)."*

---

# §3 — CI × WARDEN ASYMMETRY + RM-WHEN-ACTIVE LADDER (Throughline 3)

## §3.1 The Problem

PP-660 §5.1 specifies CI × Church rank. PP-660 §5.3 specifies CI × non-Church rank (Crown Prince, Hafenmark Chancellor, Varfell Senior Jarl). But the Warden sub-ladder was not included in either table. The Warden is neither Church-allied nor Church-opposed — it is Church-**hidden**. As CI rises, Church scrutiny rises, and Warden operations become more dangerous without a specified mechanical cost.

Secondly: PP-660 §2 names the Restoration Movement as a potential sub-office target ("RM-when-active"), but the ladder was not built because RM emergence is conditional (conviction_track_v30 §5.2). A player who participates in RM founding (ED-620) lacks a specified progression path within the movement.

## §3.2 Resolution: Warden × CI Pressure Scale

**Add to faction_politics_expanded_v1 §5 (CI × Rank Ladder Integration) via this document's propagation:**

| Warden Standing | CI 0–39 | CI 40–54 | CI 55–79 (Prominent+) | CI 80–99 (Ascendant) | CI 100 (Unification) |
|-----------------|---------|----------|----------------------|---------------------|---------------------|
| 0–2 (Thread-Touched through Warden) | Standard | Standard | +1 Ob on visible Warden-network contact in Church-presence territories | +2 Ob; safe-house exposure risk | Warden Ladder effectively goes underground; no Formal Recognition Events possible |
| 3+ (Senior Warden through Chief) | Standard | +1 Ob Southernmost Expedition planning (Church monitoring rises) | +2 Ob; Warden-Captain cannot conduct Recognition Events in Cathedral settlements | +3 Ob; Warden-Senior convocations require covert location (no fixed seat) | Warden-Chief position becomes literal hiding — Edeyja's successor cannot be publicly identified |

This is the mirror of the Church bonus curve: as Church political legitimacy rises, the Warden's practical operating margin narrows. Mechanically this ties the Warden ladder's health to a game-state clock already tracked, rather than requiring a new clock.

## §3.3 ED-629 Thread Stress Cross-Reference

ED-629 (2026-04-17) raised 28 P0 blockers on Thread system integration, including horizontal integration across social/companion/fieldwork boundaries. The Warden ladder adds a new integration surface (rank × TS thresholds) that is affected by those findings but does not block on them.

**Canonical note:** The Warden Ladder (faction_politics_expanded_v1 §2.7) is committed as-designed. If ED-629 resolution produces substrate-level changes to TS, Knot, or Thread operation rules, the Warden ladder will require a confirmatory audit. This is flagged as a dependency, not a blocking conflict.

## §3.4 Resolution: RM-When-Active Ladder (Stub)

Per conviction_track_v30 §5.2, the Restoration Movement emerges as an active faction when WA ≤ −2 AND ≥ 3 territories at CV ≤ 1 AND MS ≤ 50. Once emerged, the RM is a latent-faction-promoted-to-active mechanic. A player participating in its founding (ED-620) or serving within it post-emergence requires a ladder analogous to the 7 other faction ladders.

The RM ladder is **a stub here** because the movement's institutional architecture is deliberately thin — RM rejects institutional hierarchy as ethical principle (Equity Social Contract, factions_ttrpg_v30 §8.8). A formal rank ladder reproducing Crown-style gradation would violate the movement's design premise.

**Stub spec (for future extension):**

| RM-Std | Title | Gate | Access |
|--------|-------|------|--------|
| 0 | Sympathizer | RM has emerged (not yet founded) OR Disposition ≥ +1 with a named RM NPC | Informal network introduction |
| 1 | Comrade | RM active; participate in one Community Weaving OR Grassroots Organising action | Network access, hospitality in RM-presence territories |
| 2 | Organizer | 2 completed actions; trained 1 Sympathizer | Local cell coordination; speaks in cell decisions |
| 3 | Cell-Leader | 4 completed actions; recognized by Vossen or local elder | Regional cell authority; may initiate Resist Seizure |
| 4 | Movement-Voice | 6 actions; speaks at movement-wide council (informal convocation); known regionally | Cross-regional coordination; may speak for RM at neutral forums |
| 5 | Elder-Recognized | Endorsed by named Elder (Solvei Kaldring per worldbuilding_v30 §8 or equivalent Southern Einhir elder) | Acts as Elder's hand; may carry the movement's answer to a faction's formal proposal |
| 6 | — | (No formal rank; movement rejects hierarchy above this) | — |
| 7 | — | — | — |

Ladders above Std 5 are omitted by design. This is the same pattern as Guild collective-leadership (PP-660 §2.5), applied for ideological rather than structural reasons. Full specification deferred: **ED-659 (batch)** logs this as an active track pending RM emergence in a campaign.

---

# §4 — GENERATIONAL × COUP × IP CLOCK CONVERGENCE (Throughline 4, ED-659)

## §4.1 The Problem

PP-660 Part 8 revised Torben's maturation from "10 years game-time" to a 4-trigger Generational Shift. Three existing clocks now interact with it in ways the expansion did not specify:

1. **Coup Counter** (factions_ttrpg_v30 §8.9, npc_behavior §8.7): Löwenritter Coup fires at Counter 3. Torben Loyalty ≤ 3 increments the Counter.
2. **IP (Institutional Pressure)** (npc_behavior §7.8): Altonian invasion preparation at IP ≥ 60, Vanguard mobilization at IP ≥ 75.
3. **Baralta Crown Claim** (baralta_crown_claim_v30): If Hafenmark wins Succession Contest while Torben is mature AND disloyal to player, Torben is a rival claimant to *Baralta*, not merely the Löwenritter.

A mature-but-disloyal Torben mid-campaign produces game states the original pacing never contemplated. This requires explicit spec.

## §4.2 Resolution: Three-Clock Interaction Table

New section added to `designs/mechanics/baralta_crown_claim_v30.md §7` (see companion propagation in this commit):

### §4.2.1 Generational Shift × Coup Counter

**Rule:** When Generational Shift fires (any trigger), evaluate Torben's Disposition to the player and his Loyalty to the Altonian influence vector:

| Shift Trigger | Torben Disposition to player | Torben Loyalty vector | Coup Counter effect |
|---------------|-----------------------------|-----------------------|---------------------|
| Campaign Seasons ≥ 24 (natural maturation) | Any | ≥ 4 (Crown-aligned) | No effect |
| Campaign Seasons ≥ 24 | Any | ≤ 3 (Altonian) | +1 (standard per factions §8.9) |
| Readiness ≥ 5 (precocious) | ≥ +1 | Any | No Coup Counter effect; Loyalty transfers stabilize |
| Readiness ≥ 5 | ≤ 0 | Any | +1 (Torben as rival rather than successor) |
| Crown Stability ≤ 1 (emergency) | Any | Any | +1 automatic (institutional panic) — separate from Loyalty-vector increment |
| Almud death | Any | Any | Immediate Succession Declaration Scene; no automatic Coup Counter effect (Succession resolution takes precedence) |

**Interpretation:** The Crown Stability ≤ 1 trigger is the most dangerous path. It fires Coup Counter +1 in *addition* to any Loyalty-based increment, because the institutional frame is itself in crisis. If the Counter was at 2 when this trigger fires, Coup fires immediately.

### §4.2.2 Generational Shift × IP

**Rule:** At Generational Shift, if IP ≥ 60 (Altonian Preparation active):

- Torben's Loyalty threshold drops from ≤ 3 to ≤ 4 for Altonian-alignment attribution. Rising Altonian pressure makes mid-loyalty Torben legible as a defection risk.
- If IP ≥ 75 (Vanguard active) AND Torben Disposition to player ≤ 0: Torben becomes a formal Altonian contact point. Altonia may use him diplomatically (per npc_behavior §7.8 Vanguard tree). This is not automatic Coup — it is an additional scene category (Torben diplomatic intervention scenes become part of the Scene Slate at Priority 2).

### §4.2.3 Generational Shift × Baralta Crown Claim

**Rule:** Three scenarios based on sequence:

**Scenario A — Generational Shift fires before Baralta Crown Claim triggers:**
- Torben is already mature at the moment Hafenmark wins Succession Contest.
- Baralta inherits a Crown whose hereditary heir is an adult with potential opposing claim.
- **Consequence:** Baralta's Consecration path (§3 of baralta spec) takes a Disposition penalty. Add +1 Ob to Consecration ceremony roll if Torben Disposition to Baralta ≤ 0. Torben may be formally exiled by Baralta (requires Parliament concurrence — a +1 Ob scene arc), or may become a rival claimant creating de facto civil war at reduced scale (per COUP-02 Contested Coup mechanics).

**Scenario B — Baralta Crown Claim fires before Generational Shift:**
- Baralta holds Crown while Torben is still a ward.
- Standard Option A (merger) or Option B (institutional successor) applies per baralta §5.
- At subsequent Generational Shift: Torben matures under Baralta's regency, producing a political actor raised by the woman who displaced his bloodline. Torben's Disposition to Baralta is a new variable (default 0, modified by ward-relationship scenes). At Disposition ≤ −2, Torben becomes rival claimant to Baralta's Crown after his Generational Shift — effectively a delayed Scenario A.

**Scenario C — Generational Shift and Baralta Crown Claim fire concurrently** (same Accounting):
- Contested Crown Succession Contest. Both Hafenmark and Torben stake claim. Löwenritter may stake third claim if Coup Counter ≥ 2.
- Resolution: standard Crown Succession Contest rules (baralta §2) with Torben added as a fourth possible claimant. Torben's pool = Mandate + Bloodline Legitimacy bonus (+2D as Bloodline claim tier 1 per LIN-01).
- If Torben wins: Crown remains under Bloodline claim; Hafenmark's Succession Contest attempt fails; Baralta reverts to pre-contest status with Stability −1 (overreach per §2 failure clause). Löwenritter Coup Counter +1 if Counter was not already ≥ 2 (Ehrenwall views the contest as institutional failure).

## §4.3 Sequencing Rules

When multiple clocks would fire in the same Accounting step:

1. **Succession takes precedence** — Almud death → Succession Declaration Scene fires first, pauses other clock resolutions until the succession is declared (within 1 season).
2. **Coup Counter resolution next** — if the Counter reaches 3 during this Accounting (via Generational Shift increment or other), the Coup fires after Succession is declared but before IP effects apply.
3. **IP effects apply last** — the peninsula's political state post-succession-and-coup is what Altonia reacts to.

This sequence preserves narrative coherence: the peninsula has a succession or coup event, the aftermath shapes Altonian calculation, Altonia responds accordingly.

---

# §5 — NAMED NPC ROSTER CAPACITY (Throughline 5, ED-659)

## §5.1 The Problem

PP-660 added 9 named NPCs to the inner circles (5 Crown + 2 Hafenmark + 2 Varfell). Combined with 13 canonical roster NPCs + 4 Cardinals + Jarls and incidental figures named elsewhere (Elder Solvei Kaldring, Schoenland factor, Altonian Doux Laskaris, etc.), the peninsula's "must-track" named-NPC count reaches approximately 35.

Companion specification v30 caps *active companions* at 2. This is a different metric — roster tracking is about **awareness and state-continuity**, not personal-scale participation. But no existing doc formalizes roster capacity or degradation paths at capacity overflow.

## §5.2 Resolution: npc_behavior_v30 §11 (new section)

Add to `designs/systems/npc_behavior_v30.md`:

### §11 — Named NPC Roster Tracking Capacity

#### §11.1 Tiers

Every named NPC is classified into one of three tiers at any moment:

| Tier | Tracking Required | Scene Eligibility | Storage |
|------|-------------------|-------------------|---------|
| **Active** | Disposition per PC, Availability State, active-Duty reference, Scar count, current-season action flag | All scene types | Companion app primary surface |
| **Passive** | Disposition per PC (stable), Availability State | Ceremonial scenes, Scene Slate Priority 3+ only | Companion app secondary surface |
| **Background** | Identity only (name, faction, canonical role) | Reference only; appears in generated text | Game Master memory / roster reference |

#### §11.2 Capacity

The peninsula supports approximately **35 named NPCs at Active tier** at any time. This is the soft cap based on companion-app tracking plus Game Master narrative load. When a 36th NPC becomes Active (typically via entering inner circle, Companion acquisition, or player-initiated arc), one Active NPC is demoted to Passive.

#### §11.3 Demotion Triggers (in priority order)

1. **Off-screen duration:** Active NPC has had no scene appearance, Duty assignment, or Disposition shift for ≥ 4 seasons.
2. **Low Disposition inertia:** Disposition has been −1 to +1 and unchanged for ≥ 4 seasons with no active Duty thread.
3. **Faction removal:** NPC's faction has collapsed, been eliminated, or formally dismissed the NPC.
4. **Player-declared:** Player signals no interest (e.g., "I'm not engaging with Lord Treasurer this arc"). Game Master may demote.

Demotion is reversible. A Passive NPC returns to Active when: player scene directly engages them, their Disposition shifts by ≥ 2, or their faction priority tree selects them for a named action.

#### §11.4 Background Tier

Background NPCs exist only as canonical references. They have no tracked state. If a scene requires them (e.g., a Background senator casts a vote in Parliament), their behavior defaults to their faction AI tendency. They cannot be Companion, cannot hold rank-ladder position for the player to interact with personally.

**Promotion from Background to Passive:** Requires a named Priority 1 Scene Slate entry that brings them into interactive presence. Game Master authority.

#### §11.5 Inner-Circle NPCs

Per PP-660 Parts 1–2, the inner-circle NPCs (Crown 5, Hafenmark 4, Varfell 5, Church 5) are **structurally Active** — they cannot be demoted below Passive while their faction is in play. If one is deposed, killed, or exiled from their role, they are replaced by the faction's succession rules (§§5–6 PP-660) and the replacement enters Active tier.

#### §11.6 Companion App Display

The companion app's NPC surface displays:
- **Active tier:** Full state panel per NPC (Disposition, Availability, active Duty, Scar count, next-expected-action).
- **Passive tier:** Compact panel (name, faction, last-known Disposition, faction role).
- **Background tier:** Searchable directory only, no state panel.

Total capacity at these display weights is approximately 35 Active + 30 Passive + unlimited Background.

---

# §6 — HALL TIER SETTLEMENT INTEGRATION (Throughline 6, ED-659)

## §6.1 The Problem

PP-660 Parts 1–2 specify Hall Tiers per rank (Retainer's Billet, Banneret's Cloister Wing, Seneschal's Suite, Prince's Wing, Regent's Apartment, etc.). These are physical locations within specific settlements. But `designs/systems/settlement_layer_v30.md` has no concept of "institutional apartments within a settlement" — its stats (P/D/O) track territory-level function, not political residency. Hall Tier was committed as flavor with no mechanical hook.

## §6.2 Resolution: settlement_layer §1.4 (new subsection)

Add to `designs/systems/settlement_layer_v30.md` after §1.3 (Settlement Stats):

### §1.4 Institutional Facility Tiers

Each Seat-type and certain City-type settlements offer a bounded number of **Institutional Facility slots** that the faction controlling the settlement can allocate to rank-holders (per faction_politics_expanded_v1 §1 Hall Tier specification). Facility slots are a finite settlement resource; when full, new rank-holders at the corresponding tier receive "pending" status until a slot opens.

#### §1.4.1 Facility Slot Capacity by Settlement Type

| Settlement Type | Wing Slots (Std 6+) | Suite Slots (Std 5) | Chamber Slots (Std 3–4) | Billet Slots (Std 1–2) |
|-----------------|--------------------|--------------------|--------------------------|-------------------------|
| Seat | 3 | 5 | 8 | unlimited (shared quarters) |
| City | 1 | 3 | 5 | unlimited |
| Town | 0 | 1 | 3 | unlimited |
| Fortress | 0 | 1 | 4 (military chambers) | unlimited |
| Cathedral | 1 (Prelate's Palace) | 3 (Bishop's Suites) | 5 (Canon's Chambers) | unlimited (cloister) |
| Port | 0 | 1 | 3 | unlimited |
| Mine | 0 | 0 | 1 | unlimited |
| Outpost | 0 | 0 | 1 | unlimited |

#### §1.4.2 Allocation Rules

- Slots are allocated by the settlement's controlling authority (usually the province faction).
- At Seat settlements, the faction leader has automatic occupation of one Wing (counted against the 3 cap). Inner circle NPCs occupy additional Wings per rank.
- Player advancement to Std 6+ requires an available Wing slot. If none is available, the player's advancement is "pending" — mechanically equivalent to FAC-02 "standing debt" per PP-660 §1.0.
- Wing occupancy is durable: an NPC or player holding a Wing retains it across seasons until death, succession, exile, or formal transfer.

#### §1.4.3 Capacity Pressure as Political Mechanic

At full capacity, rank advancement becomes politically charged. If Valorsplatz Palace (S-001) has 3 Wings occupied (Almud + 2 inner circle) and the player reaches Std 6 as a fourth claimant, one of three things must happen:

1. An existing Wing-holder must depart (through Generational Shift, death, exile, or political transition).
2. The settlement's Wing capacity must be expanded (a Domain Action: **Expand Institutional Capacity**, Wealth −3, scene action at the settlement, +1 Wing added to that Seat. Cap: +1 Wing per settlement per decade).
3. The player's Std 6 advancement is deferred as "Prince-in-Waiting" — a provisional rank with Std 6 privileges but without Wing residency. Provisional rank is unstable: each season without Wing, player must make a social contest (Disposition pool vs Ob 2) to maintain inner-circle standing. Failure reverts to Std 5.

This is the Skyrim-parallel where guild-hall capacity is gated; it's also the Byzantine-parallel where imperial suite assignment was itself a political resource.

#### §1.4.4 Cross-Faction Wing Allocation

At Seat settlements of composite control (e.g., Valorsplatz Cathedral S-003 is Church-controlled within Crown territory T1), Wing slots belong to the settlement's controller (Church in S-003's case), not the province's controller. This means Church-controlled Seats can host Prelates and Cardinals regardless of Crown occupation of the province's primary Seat.

Cross-faction Wings are a diplomatic concession mechanic — a faction may permanently cede a Wing in its Seat to an allied faction as part of a treaty. This is used historically for ambassadorial residences.

---

# §7 — SIM-POL DISCOVERABILITY (Throughline 9)

## §7.1 The Problem

PP-660 raised SIM-POL-R01 through R05 as simulation debt. These were deferred per Jordan instruction. But the debt lives only inside faction_politics_expanded_v1 §10.2 — invisible to anyone reading `tests/coverage_matrix.md` (the canonical debt register).

## §7.2 Resolution

Append to `tests/coverage_matrix.md` a new section documenting the 5 SIM-POL items with DEFERRED status. Maintains discoverability without implying active work. See this commit's coverage_matrix.md update.

---

# §8 — REGISTER SPLIT FUTURE-MARKER (Throughline 10)

## §8.1 The Problem

faction_politics_expanded_v1 does three distinct jobs: mechanical spec (Parts 1–2), design philosophy (Part 3), integration contract (Parts 5–7). At 944 lines CANONICAL, future edits are cumbersome.

## §8.2 Resolution

Add a future-split marker to faction_politics_expanded_v1 §0 (via this document's propagation note, not an edit to the register itself — the register is CANONICAL and stable):

Proposed future decomposition (deferred, not scheduled):
- `designs/systems/rank_ladder_v1.md` — Parts 1–2 (faction ladders + sub-office ladders)
- `designs/systems/caste_integration_v1.md` — Part 3 (caste layer)
- `designs/systems/faction_politics_expanded_v1.md` retained — Parts 0, 4–11 (audit, terminology, integration contracts, ED tracking, propagation map)

Trigger for split: when faction_politics_expanded_v1 next requires a patch larger than 20% of its current size, split at that time.

---

# §9 — DOCUMENT STATUS AND PROPAGATION

This document is CANONICAL effective 2026-04-17 via PP-661. It resolves the 10 throughline findings from the PP-660 post-audit. It does not supersede faction_politics_expanded_v1 — it extends it.

## §9.1 Files Modified by This Commit

| File | Modification |
|------|-------------|
| `designs/systems/throughline_resolutions_v1.md` | New — this document |
| `designs/systems/player_agency_v30.md` | §3.2 Standing 0 carve-out; §3.4 range 0–7 + failure clause; §7.1 caste step + Viability Matrix + narrative note |
| `designs/systems/settlement_layer_v30.md` | §1.4 Institutional Facility Tiers (new subsection) |
| `designs/systems/npc_behavior_v30.md` | §11 Named NPC Roster Tracking Capacity (new section) |
| `designs/mechanics/baralta_crown_claim_v30.md` | §7 Generational Shift × Coup Counter × IP × Crown Claim Interaction (new section) |
| `canon/editorial_ledger.yaml` | Add ED-659 (batch), ED-659, ED-659, ED-659 |
| `canon/patch_register_active.yaml` | Add PP-661 |
| `references/canonical_sources.yaml` | Add throughline_resolutions entry |
| `references/propagation_map.md` | Add PP-661 section |
| `references/file_index.md` | Add throughline_resolutions row |
| `references/file_index_summary.md` | Add canonical listing |
| `tests/coverage_matrix.md` | Append SIM-POL-R01 through R05 as DEFERRED |

## §9.2 Editorial Items Raised

| ED | Description | Priority |
|----|-------------|----------|
| ED-659 (batch) | Throughline resolutions batch: TL-1 (caste onboarding), TL-2 (Std 0 Duty carve-out), TL-3 (Warden × CI + RM stub), TL-9 (SIM discoverability), TL-10 (future-split marker). Applied in PP-661. | P1 — APPLIED |
| ED-659 (batch) | Generational × Coup × IP × Baralta convergence (TL-4). Three-clock interaction table applied to baralta §7. | P1 — APPLIED |
| ED-659 (batch) | NPC roster tracking capacity (TL-5). npc_behavior §11 applied. | P1 — APPLIED |
| ED-659 (batch) | Hall Tier settlement integration (TL-6). settlement_layer §1.4 applied. | P1 — APPLIED |

## §9.3 Open Dependencies

- **ED-629** (Thread stress test): Warden ladder integration depends on this resolution. Post-ED-629, confirmatory audit of faction_politics_expanded_v1 §2.7 required.
- **ED-647** (provisional, pending) (Rank dismissal mechanics): partially resolved by §2 above (failure-clause revision); full mechanical spec still pending.
- **SIM-POL-R01–R05**: deferred per 2026-04-17 instruction. Coverage_matrix entry created for discoverability.

---

*End of throughline resolutions v1. All modifications applied atomically in PP-661.*
