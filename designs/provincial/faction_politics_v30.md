# VALORIA — Faction Politics Patch Register (EXPANDED)
## Date: 2026-04-16 (original audit); expanded 2026-04-17
## Status: CANONICAL (approved Jordan 2026-04-17, commit PP-660)
## Supersedes: faction_politics_patch_register_2026-04-16.md (original, 5-rank draft)
## [EDITORIAL: ED-634–ED-658 — 25 editorial items and 5 SIM-DEBT items raised by this register, tracked in canon/editorial_ledger.yaml.]
## Scope: Item 1 rank-ladder expansion to 8 ranks (Standing 0–7) with Skyrim-guild progression patterns; sub-office ladders (Löwenritter, Riskbreakers, Inquisitors, Templars, Guilds, Niflhel, RM-when-active); caste integration; CV≡PT terminology equivalence note; Baralta Crown Claim rank-ladder interaction; Ministry expansion to non-Crown factions; cross-faction parity; unified resolution of ED-POL-01 through ED-POL-14.
## Cross-references: player_agency_v30 (Standing §5, Renown §5.4, Duties §3), factions_ttrpg_v30 (8-faction roster §8.2–§8.9), worldbuilding_v30 (Four-Cardinal Church §3, Löwenritter arms §4, Guild structure §5, Parliament §6), npc_roster_v30 §14 (caste annotations), conviction_track_v30 (CV/WA), tc_political_redesign_v30 (PT/SW/TC milestones), baralta_crown_claim_v30 (Crown Succession Contest, Consecration Crisis), scale_transitions_v30, npc_behavior_v30 §7, settlement_layer_v30 §7.2.
## Patch ID: PP-660

> **Glossary note:** In this document, **TC** refers exclusively to the **Theocracy Counter** (Church institutional advancement clock, 0–100). Conviction Track is always written in full, never abbreviated as TC. (ED-756)

---

# PART 0 — AUDIT FINDINGS

This register v2 addresses eleven structural deficiencies in the original 2026-04-16 draft:

| # | Finding | Severity | Addressed in |
|---|---------|----------|--------------|
| A-01 | Rank depth of 5 is insufficient for the design goal of "governance-not-a-void" at mid-Standing. The original produces the same problem it diagnoses, one rank deeper. | P1 | Part 1 (8-position ladder per faction) |
| A-02 | No Skyrim-pattern progression gates (initiation, mentorship, specialization branch, hall access, equipment, rank-restricted dialogue, rival cohort, dismissal). Rank advancement reads as stat-tracking, not institutional belonging. | P1 | Part 1 (Skyrim Integration subsections) |
| A-03 | Sub-office coverage missing. Löwenritter, Riskbreakers, Inquisitors, Templars have Office Specifications (OFC-01–04) but no rank ladders. Guilds and Niflhel have no office or ladder at all. | P1 | Part 2 (seven sub-office ladders) |
| A-04 | Caste system (npc_roster_v30 §14) is described as "load-bearing for the entire NPC ecosystem" but absent from the patch register. Rank advancement, Formal Recognition, and inner-circle approval all intersect caste, and the original is silent on all three. | P1 | Part 3 (caste layer) |
| A-05 | `conviction_track_v30.md` line 16 violates the Solmund naming rule ("Galbadian Orthodoxy" pole). Propagation required across any downstream reference. | P1 | Part 4 (naming propagation) |
| A-06 | CV (Conviction Track) and PT (Piety Track) are the same per-territory stat under two names across two v30 documents. Plus SW (Spiritual Weight, fixed) was introduced in tc_political_redesign without explicit dissolution of CV. The register silently uses none of the three. | P1 | Part 4 (terminology reconciliation) |
| A-07 | TC as political legitimacy (floor(TC/20) bonus dice for Church, floor(TC/30) penalty for opposition) has no interaction with the Church rank ladder. A Prelate at TC 28 should not feel identical to a Prelate at TC 90. | P2 | Part 5 (TC × rank ladder) |
| A-08 | The Baralta Crown Claim mechanism (ED-408–411) terminates the Hafenmark faction (Option A merger) or fires PI-gated succession (Option B persistence). Neither outcome is reflected in the rank-ladder design — the register has no path from Hafenmark Chancellor to Crown Chancellor, nor a Hafenmark-under-institutional-successor ladder. | P1 | Part 6 (Baralta × rank interaction) |
| A-09 | Ministry system (MIN-01–06) is Crown-exclusive. The Church's four-cardinal apparatus, Hafenmark's parliamentary committee structure, and Varfell's Jarl councils have equivalent institutional functions with no mechanical scaffolding. | P2 | Part 7 (Ministry expansion) |
| A-10 | Generational shift is spec'd at "10 years game-time" (LIN-02 Condition B). At 4 seasons per year that is 40 seasons; typical campaign is ~S14–S20 per victory_v30 pacing. The mechanic is unreachable as written. | P1 | Part 8 (Generational shift fix) |
| A-11 | Cross-faction rank parity (BALANCE-POL-01) is flagged but not resolved. Without a parity table, Standing 5 Crown vs Standing 5 Varfell vs Standing 5 Hafenmark vs Standing 5 Church are simply assumed equivalent. | P1 | Part 9 (parity table) |

---

# PART 1 — SEVEN-RANK LADDER SPECIFICATION (Expanded FAC-01)

## §1.0 Ladder Architecture

Replace the 0–5 Standing track with an eight-position ladder (Standing 0 through Standing 7). Standing 0 is explicit pre-initiation status, not "no relationship." Standing 7 is the senior-most position short of leadership; Leadership itself is a discrete state (not a ninth Standing), reached via the succession mechanisms in Part 2 of the original register (SUC-01–03, LIN-01–04).

Each rank specifies eight mechanical dimensions (the **Skyrim Eight**):

1. **Title** — faction-specific vocabulary.
2. **Initiation Gate** — the condition that must be met to advance from the prior rank. Includes an **Initiation Duty** at Standing 0→1 (analogous to the "prove yourself" first quest in Skyrim guilds).
3. **Granted Access** — mechanical capability unlocks.
4. **Required Obligations** — ongoing duties while holding the rank.
5. **Hall Tier** — what Order/Cathedral/Assembly space the rank-holder may enter, reside in, or requisition. Mirrors the Cloud District / Jorrvaskr upper floor / Arcanaeum access gating in Skyrim.
6. **Livery & Equipment** — visible identifier; faction-provided gear or stipend. Mirrors the Thieves Guild armor set, College robes, Dark Brotherhood leathers.
7. **Mentor Relationship** — named NPC who trains, vouches for, or oversees the player at this rank. Training is a mechanical scene action: +1D on one specified roll per season while the mentor is alive and at Disposition ≥ 0.
8. **Demotion Trigger** — the specific condition that returns the player to the prior rank (or lower). Parallels Skyrim's "kicked out of the Thieves Guild" mechanic for violating the Shadow's rules.

Three cross-rank dimensions apply to all tiers:

- **Rival Cohort** — at Standing 2–4, a named NPC of the same rank competes for advancement. Their Disposition toward the player is independent of faction-leadership Disposition. A rival at Rival Standing 3 (see original SUC-02) triggers a pre-emption challenge.
- **Rank-Restricted Dialogue** — named NPCs above the player's Standing have **Minimum Engagement Scale** per NPC-02 of the original register. This is unchanged but now layered over the expanded ladder: an NPC at Standing 6 treats a Standing 2 as an unknown; Standing 4 as a familiar; Standing 6 as a peer.
- **Dismissal** — Standing can fall below 1. Dismissed members lose all rank privileges, cannot re-enter the faction in that role, and accumulate a **Dishonored** flag that persists across the campaign. Re-entry requires Extraordinary Circumstances (LIN-02 equivalent, faction-specific).

The Initiation Duty (Standing 0→1) is the single most important addition. In the original register a player simply "is" at Standing 1 by virtue of faction choice at character creation. Under this expansion, faction choice at character creation determines **eligibility** (the player is a Petitioner/Aspirant); the Initiation Duty is the first scene arc of the campaign and must be resolved before any Duty system (player_agency_v30 §3.2) activates for that faction. This creates the Skyrim "prove yourself" opening and, mechanically, gives the GM a guaranteed first-season scene arc for every faction-aligned player.

---

### §1.0a Demotion Magnitude (NEW — ED-776)

The Demotion Trigger column on each rank ladder specifies *what causes* demotion but not *by how much*. This section specifies magnitude rules.

**Default magnitude: one rank.** Most demotion triggers cause the player to drop one rank — Standing N → Standing (N−1). This applies to:
- Failure of Required Obligations at the current rank.
- Disposition decline with mentor or institutional supervisor.
- Procedural failure (e.g., 3 consecutive service failures, missing a Recognition Event timeline).
- Skill or attribute drift that no longer meets the rank's requirements.

**Severe magnitude: two or more ranks.** Triggers that explicitly involve institutional violation cause multi-rank demotion:
- Public scandal: drop 2 ranks, minimum Standing 1.
- Heresy Investigation that ends in Tribunal but not full Excommunication: drop 2 ranks; if rank 5+, drop to Standing 3 (lay status retained).
- Faction-faction defection that compromises ongoing Obligations: drop 3 ranks or to Standing 1, whichever is higher.

**Total magnitude: full dismissal (Standing 0 or below).** Triggers that constitute fundamental institutional rejection cause Dismissal per §1.0 (Dishonored flag, persistent across campaign):
- Excommunication (per social_contest §7.1): Standing drops to **−1** (Dismissed-with-Dishonor flag set; cannot re-enter faction in that branch). Note that −1 is below Standing 0; the player is treated as actively opposed by the faction.
- Treason / oath-breaking against the faction's central authority (Crown regicide, Hafenmark constitutional violation, Varfell jarl-oath breaking, Church doctrinal breaking).
- Permanent Conviction shift to opposing-framework Conviction (e.g., Crown member shifts to Autonomy primary): rank rolls to Standing 0 (the framework-alignment underpinning advancement is gone).
- Cardinal-rank-specific triggers (per §1.4 Standing 6 Demotion column): "arm-specific catastrophic event" — the magnitude is engineered such that a Cardinal demoted from Standing 6 falls to Standing 3 (Canon, retains lay status) UNLESS the catastrophic event involves Heresy or Treason, in which case full dismissal applies.

**Demotion vs Loss of Faction Membership:**

| Demotion Result | Faction Membership | Re-entry? |
|---|---|---|
| Drop to Standing ≥ 1 (any non-Dismissal demotion) | Retained | Re-advancement possible per Initiation Gates (must complete prerequisites again from current rank) |
| Drop to Standing 0 (e.g., from Standing 1 demotion) | Retained at lay/initiate level | Re-advancement requires completing Initiation Duty 0→1 again |
| Drop to Standing −1 (Dismissal) | **Forfeited** | Re-entry impossible in same branch; may petition different Cardinal/Jarl/Minister for separate-branch entry; Dishonored flag applies |

**Cross-rank demotion flow:** When demotion magnitude exceeds 1, the player does NOT pass through intermediate ranks — they fall directly to the destination rank. Mentor relationships from intermediate ranks are voided immediately. Hall Tier and Livery permissions clear and resync to the new rank within 1 season (a Cardinal demoted to Canon must vacate Cardinal-grade housing within 1 season; their Cardinal livery is recalled).

**Demotion appeal:** A demoted player at Standing ≥ 1 may file institutional appeal within 2 seasons of demotion. Resolution: faction-internal Conviction Track (Standard Contest), Adjudicator = supervising Standing-7 NPC or institutional body. Successful appeal reverses the demotion. Failed appeal makes the demotion permanent (no re-appeal in same campaign year). Appeals are unavailable for Standing 0 (Dismissal) demotions — these require Initiation re-attempt, not appeal.

[EDITORIAL: ED-776 — Demotion magnitude specified. Closes spec gap surfaced by stress-test 33: Demotion column gives triggers but not magnitudes. Default = one rank; severe (public scandal, Heresy non-excommunication, defection) = 2-3 ranks; total (excommunication, treason, framework abandonment, Cardinal catastrophic) = Standing −1 dismissal. Also specifies cross-rank flow (no intermediate-rank pass-through; mentor/livery/hall reset within 1 season) and appeal mechanism (2-season window, faction-internal Conviction Track, no appeal for Dismissal). Source: 2026-04-25 stress-test 33.]

---

## §1.1 CROWN RANK LADDER (Valorsmark Monarchy)

**Faction ethical framework:** Virtue Ethics (factions_ttrpg_v30 §8.2). Visible, public, virtuous actions are −1 Ob; covert or morally ambiguous are +1 Ob. This is a ladder where **being seen doing the right thing** matters more than the doing.

**Core institutional logic:** Deed-monarchy institutional memory (npc_roster §14, Almstedt). The Almqvist dynasty traces its legitimacy to the first Almqvist's documented deeds at kingdom-founding. Rank advancement in the Crown is structurally a re-enactment of that logic: each rank demands a deed that renews the founding principle, not merely accrued loyalty.

### Crown Ladder Table

| Standing | Title | Initiation Gate | Access | Obligations | Hall Tier | Livery | Mentor | Demotion |
|----------|-------|-----------------|--------|-------------|-----------|--------|--------|----------|
| **0** | **Petitioner** (Bittsteller) | Character creation + sponsorship by any Standing 3+ Crown NPC (requires one social scene, Disposition ≥ +1) | Public access to Crown court in Valorsplatz (T1); standing to petition for audience (no guaranteed response) | None formal. The Petitioner is *expected* to complete the Initiation Duty within 2 seasons or be ignored permanently. | None — lodging at own cost in Valorsplatz or traveling | Plain clothing, no insignia | Sponsor (TBD — typically a junior Löwenritter or a minor aristocrat) | Sponsor withdraws sponsorship (Disposition falls to −1); or 2 seasons pass without Initiation Duty attempt |
| **1** | **Retainer** (Hofmann) | **Initiation Duty:** "Carry the King's Word" — deliver a formal correspondence between Almud and a specified inner-circle NPC across at least one provincial boundary. Requires: successful fieldwork (Interview or Observe) in both origin and destination, and no Exposure event fires during the journey. | Faction safe passage in Crown territories; access to garrison quartermaster (1 supply requisition/season free) | Must answer Duty calls within 1 season | Retainer's Billet at Valorsplatz garrison (shared quarters, no privacy) | Crown tabard (public Crown identifier); sidearm permitted in civilian settlements | Royal Marshal's staff-serjeant (TBD — see ED-634 below) | Refusing a Duty without documented cause |
| **2** | **Crown Agent** (Kronagent) | Complete 2 Duties successfully (Success or Exceeding) at Standing 1; one must be in a province not the player's origin territory. | May conduct fieldwork in Crown name (+1D Interview in Crown territories); access to Crown couriers (1 information relay/season free) | Must maintain Disposition ≥ 0 with at least one Crown inner-circle NPC | Retainer's Billet retained; access to Crown archive reading room (Ob +0 for documentary Interview) | Embroidered tabard (rank visible); stipend 1 Wealth/year-arc | Mentor assigned: a named Standing 5 Crown NPC with overlapping domain specialty (combat, administration, or intelligence — see §1.1b) | Disposition −3 with any inner-circle NPC; or 3 consecutive Duty failures |
| **3** | **Banneret** (Bannerherr) | **Formal Recognition Event** (mandatory Zoom In — FAC-02): Almud (or designated officer) grants the player a Banner. The Banner is a physical object and a mechanical token — see §1.1c. Recognition can be withheld per FAC-02 conditions. Plus: demonstrated competence in one of the three Crown specialty branches (§1.1b). | May direct one NPC officer in tactical operations; may initiate a minor Domain Action on the faction's behalf (Ob +1; outcome must be reported within 1 season); Löwenritter Knight sub-ladder opens (OFC-01, Part 2) if the player branches into the military specialty | Must govern or garrison at least one settlement; must report directly to Almud at least once per year-arc (Audience scene) | Private chamber in Valorsplatz Cloister Wing; access to Cloister Wing meeting rooms (lets the player convene other Bannerets privately — key for coalition-building) | Banner (personal device on a Crown tabard); personal arms license (visible weapon in all civilian settlements, including Hafenmark); mount stipend | Mentor upgrades to a Standing 6+ NPC (a Seneschal or a senior Löwenritter Knight-Commander). Specialty-specific — see §1.1b. | Loss of assigned settlement without authorized withdrawal; or Banner formally revoked (requires a Crown social contest, Ob 3, triggered by misconduct) |
| **4** | **Crown Lieutenant** (Kronleutnant) | 2 completed Banneret-rank Duties at Success+, plus one **Public Deed** — a visible, witnessed action generating Renown +2 (per REN-03 in the original register). Virtue Ethics requires the deed be *public*. | +1 scene action from faction resources (per original FAC-03, revised framing); may direct 2 NPC officers; access to Crown war council meetings (observer, not voting); may initiate a Scene Slate Priority 2 entry at any Crown settlement (the player proposes fieldwork that gets treated as a Crown-sanctioned operation) | Active military or administrative Duty each season; must attend two court audiences per year-arc; must maintain Renown ≥ 3 (the Lieutenant's authority is visibly underwritten by reputation) | Lieutenant's Chamber (private apartment in Valorsplatz); may billet 2 personal retainers in the Cloister Wing; access to Crown stable | Lieutenant's star (heraldic mark added to Banner); may wear Crown Lieutenant livery at court (required for formal occasions) | Royal Marshal (Standing 7) directly mentors Crown Lieutenants in the military branch; Lord Treasurer mentors administrative; Spymaster mentors intelligence | Sustained Duty failure (2+ consecutive seasons); or Renown drops to ≤ 1 (the Virtue-Ethics link has broken) |
| **5** | **Seneschal** (Reichsseneschall) | 3 completed Lieutenant-rank Duties plus one **Recognized Deed** — an action the Church, Parliament, or a senior military commander publicly endorses (produces +1 Legitimizing Authority token toward Deed-Claim succession per LIN-01). | May speak in Crown's name in formal negotiations (below treaty scale); war council voting member; may convene Bannerets and Lieutenants under own authority (political coalition formation); may govern a province-adjacent settlement; inner-circle-adjacent (sees inner-circle deliberation but does not vote there) | Govern at least one province-adjacent settlement; maintain Disposition ≥ +1 with majority of inner circle; must pursue at least one arc-level objective registered with the Markamt | Seneschal's Suite in Valorsplatz (apartment with private entrance); may billet 4 retainers; access to Royal Library (sealed section); permanent chamber assigned in one other Crown province | Seneschal's chain (visible at all times in Crown territory); personal household banner (separate from the Banner — the household is now a recognized political unit); Crown-granted horse and full armor set | Inner-circle NPC (any of the five named — see §1.1d) directly mentors. Specialty branch now fully matured; cross-branch access possible at Ob +1. | Inner-circle majority turning against player (SUC-02); or two consecutive Duty failures at this scale |
| **6** | **Inner Prince / Prince of the Realm** (Reichsfürst) | Unanimous inner-circle confirmation (all 5 inner-circle NPCs at Disposition ≥ 0). Effectively: the inner circle has recognized the player as a member of their own rank. | Inner-circle voting member; may represent Crown in treaty negotiations; may initiate Ministry reforms (Part 7) in one Ministry per year-arc; authority to nominate Bannerets (Standing 3) for Recognition Events; access to all sealed Crown correspondence | Chair at minimum one Ministry; maintain inner-circle Disposition majority (3 of 5 ≥ 0); must remain in Valorsplatz for at least 2 of 4 seasons per year (the court cannot function without its princes); Crown Treaty actions require Prince approval (the player is one such approver) | Prince's Wing in Valorsplatz (separate building within castle precinct); personal armory; household of 8+ retainers | Prince's Coronet (visible in all public contexts); Crown heraldic variant (household banner now incorporates royal arms) | No mentor — the player is now mentored only by Almud directly, at Almud's discretion | Inner-circle majority withdraws (3 of 5 Dispositions fall below 0); or public act against Crown Virtue Ethics (covert action exposed with Renown damage ≥ −3) |
| **7** | **Crown-Adjacent** / **Regent-Designate** (Kronnah / Reichsverweser-designiert) | Succession Declaration Scene fires (SUC-03). The player has been formally named by Almud as the succession candidate OR has built a 3-of-5 inner-circle supermajority sufficient to defeat any rival at a Succession Contest. | Succession-eligible (full LIN-01 Bloodline-equivalent weight from position alone, plus Deed-Claim evidence as accumulated); may call one Extraordinary Audience with Almud per season; may issue Royal Decrees in Almud's name if Almud is Unavailable or In Crisis (with Legitimacy Token damage per POW-03); treaty-ratification vote in Crown's name (requires later Almud endorsement within 2 seasons or the decree fails retroactively) | Govern at minimum a province; maintain all inner-circle Dispositions ≥ 0; active succession preparation (Markamt registration of deed-claim per MIN-06); if Almud ages, must initiate regency preparation (scene arc) | Regent's Apartment in the Valorsplatz palace (not merely the castle precinct — inside the royal residence); full access to royal household; own retinue | Regent's circlet (visible mark of designation); Crown colors added to personal arms | Mentored only by Almud, co-equally with Torben (creates Torben-player tension — see §8 on generational shift) | Rival succession candidate wins an inner-circle supermajority; or player commits a Public Act repudiating Crown Virtue Ethics; or Torben reaches Generational Shift at Disposition ≤ 0 (§8) |

### §1.1b Crown Specialty Branches (Unlocks at Standing 3)

At Banneret rank, the player selects a specialty branch. The branch determines: the mentor assigned at Standing 4+, the Duty categories the player is offered, the Ministry they are positioned to chair at Standing 6, and which sub-office ladders (Part 2) are open to them.

| Branch | Ministry link | Sub-office opens | Primary mentor line | Secondary |
|--------|---------------|------------------|---------------------|-----------|
| **Martial** (Schwertzweig) | Kriegsamt (Ministry of War) | Löwenritter Knight ladder (Part 2, §2.1) | Royal Marshal → Löwenritter Grand Master | Knight-Commander of the player's garrison |
| **Administrative** (Stangzweig) | Haushalt (Finance) or Gerichtsamt (Justice) or Markamt (Lands) | None; advancement within Crown ranks only | Lord Treasurer → Lord Chief Justice | Chancellor of the Markamt |
| **Intelligence** (Schattenzweig) | Schattendienst (Intelligence) | Riskbreaker ladder (Part 2, §2.2); Niflhel transactional relationships (Part 2, §2.6) | Spymaster (TBD name) → Riskbreaker Commander | Senior Tribune of the Schattendienst |

Branch switching is possible but expensive: requires one completed Duty in the new branch at Standing ≥ 3, plus demotion to Standing 3 from whatever rank the player currently holds (branch identity is institutional — the Crown does not recognize a Lieutenant of uncertain specialty).

**Caste gating:** The Martial branch is functionally open to all castes but in practice dominated by northern and central Valorsplatz-adjacent Einhir heritage; the Intelligence branch is caste-neutral by necessity (Niflhel connections require Southern Einhir fluency); the Administrative branch has the strongest caste bias — see Part 3.

### §1.1c The Banner (Standing 3 Recognition Token)

The Banner is the first faction-token object in the ladder. Its function is Skyrim's "Guild Master's cape" analog — a visible identifier that signifies rank to any observer.

- **Mechanical:** +1D on all Crown-context Intimidate rolls; −1D on all Subterfuge rolls while visible (the Banner is the opposite of anonymity). The player may choose to display or conceal the Banner per scene. Concealment in a situation where Crown authority was invoked generates Exposure.
- **Narrative:** The Banner is inherited, commissioned, or granted. An inherited Banner carries a Legacy Attribute (a prior Banneret's deed is known to every NPC; roll on the Legacy table when the Banner is introduced). A newly commissioned Banner has the player's own deed stitched into it — a permanent record of the Initiation Duty + the Banneret Recognition Deed.
- **Revocation:** Formal revocation requires an Audience scene at Valorsplatz with at least one inner-circle NPC present. Revocation is a Scene Slate Priority 1 entry if the player's misconduct is known.

### §1.1d Crown Inner Circle — Named (resolves ED-POL-01)

The original register leaves four inner-circle NPCs unnamed. This proposal names them. All require Stance Triangle specification (Conviction / Resonant Style / Certainty) — provisional values below:

| Role | Proposed Name | Conviction | Resonant Style | Certainty | Notes |
|------|---------------|------------|----------------|-----------|-------|
| Royal Marshal | **Wilhelm Voss** | Order | Authority | 4 | Second-generation Valorsmark aristocrat; conservative; distrusts the Löwenritter because the Order answers to its own Grand Master, not to the Crown chain. Disposition toward Ehrenwall (Löwenritter Grand Master) starts at −1. |
| Lord Treasurer | **Annalie Reichard** | Precedent | Evidence | 5 | Mercantile family that married into aristocracy two generations ago. Distant cousin of Feldhaus (Guilds); formally distanced but the relationship is known. Disposition toward Baralta starts at +1 (constitutional procedure respected). |
| Spymaster (Schattendienst Minister) | **Kolbrun Thale** | Autonomy | Consequence | 3 | Background obscured; rumored Southern Einhir ancestry (unconfirmed). Operates at the edges of Crown propriety. Only inner-circle member with any Niflhel contacts. Disposition toward Haelgrund starts at −1 (Inquisitorial scrutiny has touched the Schattendienst twice). |
| Archbishop's Representative | **Father Gustav Linder** | Faith | Authority | 5 | Church Canon (Standing 3 in Church sub-ladder) seconded to Crown by Himlensendt. Reports to Himlensendt weekly. Disposition toward any visible Thread-practitioner player is structurally −2. |
| Captain of the Royal Guard / Löwenritter Liaison | **Theodor Kreutz** | Order | Authority | 4 | Knight-Commander of the Löwenritter, seconded to the Royal Guard. Answers to both Ehrenwall (Grand Master) and Almud. In a conflict between the two chains, his pre-designated allegiance is to Almud personally — but the Coup Counter increment is linked to *his* death or removal, not to Ehrenwall's, which is why Löwenritter coups target Almud through Kreutz first. |

**Torben Almqvist** remains the heir apparent; he is treated as inner-circle-adjacent (not a voting member until Generational Shift — see §8) but required for Clean Succession. His Conviction is **Continuity** (as original register) with Resonant Style **Evidence** (provisional — he has been taught by Almstedt, whose style is documentary).

---

## §1.2 HAFENMARK RANK LADDER (Constitutional Duchy)

**Faction ethical framework:** Categorical Imperative (factions_ttrpg_v30 §8.4). Actions based on legal precedent, constitutional authority, and established procedure are −1 Ob; ad hoc or precedent-breaking actions are +1 Ob. This is the ladder of **rules that must apply universally** — advancement requires the player to have demonstrated they will follow procedure even when it costs them personally.

**Core institutional logic:** Parliament is the adjudicating body. Rank advancement is *formal confirmation by legislative vote*. Unlike the Crown, where Almud's personal favor suffices, Hafenmark rank above Standing 2 is a matter of public record — a Burgher has been voted onto a Roll of Burghers that is physically maintained in the Gransol Parliamentary Archive.

### Hafenmark Ladder Table

| Standing | Title | Initiation Gate | Access | Obligations | Hall Tier | Livery | Mentor | Demotion |
|----------|-------|-----------------|--------|-------------|-----------|--------|--------|----------|
| **0** | **Petitioner** (Bittsteller) | Character creation + standing to petition Parliament (proof of residence in a Hafenmark territory for 1 year-arc; OR sponsorship by any Standing 3+ Burgher) | Parliamentary public gallery access during open sessions | None formal. The Petitioner is permitted to approach any Advocate for sponsorship. | None — lodging at own cost | Plain clothing, no insignia | Self-sourced (the Petitioner must *secure* a mentor as part of the Initiation Duty) | 3 seasons without Initiation attempt → eligibility revoked (must re-establish residence) |
| **1** | **Advocate** (Advokat) | **Initiation Duty:** "File the Petition" — the player must file a formal legal petition with Parliament that is accepted for consideration (not vote — consideration). This requires: one successful fieldwork action (documentary research, typically Interview at the Parliamentary Archive), one social scene with a sitting Burgher at Disposition ≥ 0, and the petition subject must be a genuine civic matter (land claim, trade dispute, constitutional question — not a personal vendetta). | Legal standing to petition Parliament; access to the public Archive; may attend Parliamentary sessions they are summoned to | Must attend any Parliamentary session they are summoned to; must maintain residence in a Hafenmark territory | Advocate's Bench in the Parliamentary outer hall (public seating reserved for licensed Advocates); access to Gransol library reading room | Advocate's sash (black with single stripe); legal satchel (mechanical: +1D on documentary Interview in Hafenmark courts) | Senior Advocate (TBD — a Standing 3 Burgher with open apprenticeship) | Failure to attend 2 summons; or loss of residence |
| **2** | **Burgher** (Vollbürger) | Complete 2 Advocate-rank Duties with Success+; pass a Burgher's Examination (a formal oral social contest, Ob 2, adjudicated by 3 sitting Burghers — the player must defend knowledge of Hafenmark constitutional doctrine). | May second Parliamentary motions; access to Guild commercial data (1 query/season free); may serve as legal counsel to a Hafenmark NPC (creates a formal Obligation) | Must maintain Wealth ≥ 1 personally or through faction resources (Burghers are expected to be self-sustaining); must testify honestly if subpoenaed by Parliament | Burgher's Chamber in the Parliament building (shared office with 4 other Burghers); rights to Commons-level dining hall | Burgher's cloak (navy, rank embroidery at collar); signet ring (Hafenmark watermark) | Assigned Mentor-Parliamentarian (Standing 4, named by examining committee) | Bankruptcy (Wealth 0 for 2 consecutive seasons); or procedural violation exposed in Parliament |
| **3** | **Alderman** (Ratsherr) | **Formal Recognition Event:** Parliamentary vote of admission to a local council seat. Requires: Burgher's petition to a specific council (city, town, or parish); 2/3 supermajority of existing council; no outstanding Obligations with rival factions. | Voting seat on local council (settlement Order +1D on Pacify in that settlement); may introduce minor Parliamentary petitions; access to all Hafenmark commercial intelligence; invited to committee (§7.2) | Must govern a City/Town settlement OR serve as standing legal advisor to one Hafenmark NPC; regular council attendance | Alderman's Office in the council hall of the governed settlement; permanent bench in Parliamentary Commons | Aldermanic robes for council sessions (ceremonial); stipend 2 Wealth/year-arc; desk in Gransol | Standing 5 Parliamentary chair; specialist branch mentor per §1.2b | Council vote of no confidence (2/3 against); or Conviction scandal exposed publicly (Renown −2 equivalent) |
| **4** | **Parliamentarian** (Parlamentsmitglied) | **Public Deed:** A specified Parliamentary intervention that passes (the player proposes and carries a motion — not merely votes on one). Plus: completion of 3 Aldermanic Duties at Success+. The Parliamentary intervention is a social contest against opposing parliamentary blocs (mass social contest — factions_ttrpg_v30 §8.11 rules apply). | Full Parliament voting seat; may introduce major motions (including Motion of No Confidence per worldbuilding_v30 §6.2); +1 scene action from Hafenmark resources; access to Baralta's private audiences (Availability State: In Session); may chair a Parliamentary Committee (see §7.2) | Must vote every active Parliament session (abstention costs Standing −1); must maintain public alignment with Hafenmark constitutional doctrine (CI framework actions); residence in Gransol at least 2 of 4 seasons per year-arc | Parliamentarian's Hall (private study in the Parliament building); may requisition committee meeting rooms; access to Baralta's correspondence on any matter the Parliamentarian has Committee chair for | Parliamentarian's mantle (navy with gold); personal arms on the mantle; Baralta-dependent stipend (paid in Crown-issued coin, symbolically important — Baralta draws on her own purse for her closest parliamentarians) | Baralta herself (specific scene type: "Baralta's Study" — annual audience for direction-setting); or a senior committee chair per branch | Public violation of constitutional doctrine; or coalition collapse (Disposition with 4+ other Parliamentarians dropping below 0 simultaneously) |
| **5** | **Parliamentary Chair** (Parlamentsvorsitzender) | 3 completed Parliamentarian-rank Duties; successful chairmanship of one major committee (committee passes 2 motions during player's tenure); plus **Recognized Deed** — a judicial or constitutional act endorsed by Baralta, by the Supreme Judiciary, OR by an outside legitimizing authority (the Crown, the Church, or the Guilds). | May chair Parliamentary session in Baralta's absence; member of the Hafenmark Inner Circle; authority to open formal treaty negotiations in Hafenmark's name (treaty ratification still requires Parliamentary majority); may speak at Parliament without recognition; Cabinet-equivalent access | Govern at least one Hafenmark province-level settlement; maintain Disposition ≥ 0 with majority of Inner Circle; manage at least one constitutional priority (see Parliament Committees §7.2) | Chair's Residence in Gransol (apartment in Baralta's own residence precinct); full library access including sealed constitutional archive | Chair's chain of office (visible in all public Hafenmark contexts); Supreme Judiciary consultation right (the player may request advisory opinion from any Justice) | Baralta directly; or the Senior Parliamentary Chair (Almstedt — a Standing 6 NPC per §1.2c) for deep-procedural matters | Coalition collapse (losing Parliamentary majority for 2 consecutive sessions); or public Motion of Censure succeeds |
| **6** | **Chancellor** (Kanzler) | Unanimous Inner Circle confirmation (all 4 Hafenmark IC NPCs at Disposition ≥ 0) — paralleling Crown §1.1, but here enacted as a formal Parliamentary vote of confirmation (not an informal inner-circle consensus). | May act in Baralta's name for operational matters (treaty negotiation, tax policy, ministerial assignment); succession-eligible per Hafenmark Option B (Parliamentary vote on vacancy); may initiate Sovereign Authority Doctrine (factions_ttrpg_v30 §8.4) with Baralta's approval | Must chair at minimum two Parliamentary Committees; govern a province; must maintain Parliament's ability to convene (if Parliament fails to convene for 2 consecutive sessions, Chancellor Standing falls to 5) | Chancellor's Tower — private building adjacent to Parliament (reserved historically for the Chancellor office); full court access; own household of 10+ | Chancellor's Gold Chain and official arms; use of Baralta's personal heraldic variant when acting in her name (with cost to Legitimacy Token per POW-03) | Baralta only; plus advisory access to the Lord Chief Justice of Hafenmark | Formal Parliamentary Censure passes (rare — requires 2/3 supermajority); or Baralta withdraws confidence (Disposition falls to −2) |
| **7** | **Prime Parliamentarian** / **Speaker-Regent** (Erster Parlamentarier / Sprecher-Verweser) | In Hafenmark, Standing 7 is specifically a *succession-prepared* state — the player has been publicly endorsed by Baralta AND by Parliament in a formal motion (not a vote, but a resolution of endorsement). This is the structural equivalent of the Crown's Regent-Designate, but channeled through legislative procedure. | Full succession-readiness; may chair Parliament in Baralta's place indefinitely; may negotiate treaties on Hafenmark's behalf without prior approval; equivalent to Crown Standing 7 at every operational level | Govern a province AND chair minimum two Parliamentary Committees; maintain public Parliamentary majority; active public engagement with Hafenmark constitutional priorities; if Baralta is aging or incapacitated, must initiate Parliamentary succession preparation | Speaker-Regent's Hall in the Parliament building (reserved for the office); own household of 15+; governance offices in all major Hafenmark settlements | Speaker-Regent's device (personal heraldic identification); Hafenmark state color (navy and gold) added to personal arms | Baralta co-equally with the Senior Parliamentary Chair | Rival succession candidate wins Parliamentary supermajority; or Baralta's Disposition falls to −2 (she formally revokes endorsement) |

### §1.2b Hafenmark Specialty Branches (Unlocks at Standing 3)

| Branch | Committee link | Sub-office opens | Primary mentor line |
|--------|----------------|------------------|---------------------|
| **Judicial** | Supreme Judiciary Committee | None (Hafenmark-internal only) | Senior Justice (Standing 6 NPC) |
| **Commercial** | Trade & Guild Relations Committee | Guilds ladder (Part 2, §2.5) opens — Hafenmark Parliamentarians in the Commercial branch are structurally eligible for parallel Guild advancement | Guild Comptroller (Standing 5 in Hafenmark Inner Circle; also holds Guild Master rank — see §2.5) |
| **Martial** | Defense Committee | Hafenmark Militia rank ladder (provisional — see ED-640 below) | Hafenmark Military Commander |

### §1.2c Hafenmark Inner Circle — Named (resolves ED-POL-01, partial)

| Role | Proposed Name | Conviction | Resonant Style | Certainty | Notes |
|------|---------------|------------|----------------|-----------|-------|
| Senior Parliamentary Chair | **Peder Almstedt** (canonical — npc_roster_v30 #8) | Precedent | Evidence | 4 | Already canonical. Deed-monarchy institutional memory; serves as senior chair by seniority. Is the single NPC who remembers the original Almqvist founding terms. |
| Guild Comptroller | **Annika Feldhaus** (canonical — npc_roster_v30 #7, but secondary role here) | Precedent | Consequence | 5 | Serves as Inner Circle liaison; holds dual rank (Master Merchant in Guilds — Part 2, §2.5). Caste alignment: commercially invested in caste maintenance. |
| Baralta's Legal Advisor | **Torvi Heljason** (new — ED-635) | Precedent | Authority | 4 | Senior constitutional scholar; sole advisor who may contradict Baralta in private without procedural consequence. Northern Einhir heritage. |
| Military Commander (Hafenmark) | **Olaf Geirson** (new — ED-636) | Order | Consequence | 4 | Veteran of the Hafenmark defensive tradition; Hafenmark has no offensive army, only border garrisons. He is more a logistician than a general. Caste-neutral; operates in a branch where practical competence dominates. |

---

## §1.3 VARFELL RANK LADDER (Jarl Confederacy)

**Faction ethical framework:** Consequentialist Pragmatism (factions_ttrpg_v30 §8.5). Actions with measurable seasonal outcomes are −1 Ob; actions with uncertain or long-term payoff are +1 Ob. This is the ladder where **demonstrable results win the argument** — advancement is by provable deed, not by procedural qualification. The Jarl Assembly can retroactively justify almost anything that worked.

**Core institutional logic:** Varfell is a confederation. Vaynard is "first among the Jarls" not a monarch. Rank advancement is therefore *horizontal* in one sense (you become a Jarl among Jarls) and *vertical* in another (seniority among Jarls). The Jarl Assembly's role is analogous to the Varangian Guard's role in Byzantine acclamation politics — the Assembly *creates* the legitimacy it affirms.

### Varfell Ladder Table

| Standing | Title | Initiation Gate | Access | Obligations | Hall Tier | Livery | Mentor | Demotion |
|----------|-------|-----------------|--------|-------------|-----------|--------|--------|----------|
| **0** | **Stranger** (Fremdling) | Character creation + presence in Varfell territory. No formal sponsorship required (Varfell is porous at the lowest level — a Stranger who is useful will be noticed). | Public hospitality at any Jarl's hearth for one night; no protection if the Stranger causes offense | None formal. The Stranger is expected to make themselves useful or depart within 2 seasons. | None — the Stranger sleeps where the Jarl permits | Stranger's dress (unmarked); arms carried openly are tolerated | No formal mentor; informally, any Huscarl who has noticed the Stranger | Offense to a Jarl; or 2 seasons without the Initiation Duty being attempted |
| **1** | **Huscarl** (Huskarl) | **Initiation Duty:** "Answer the Muster" — the player joins a Jarl's hearth-guard for one military operation (mass battle or escorted movement in hostile territory). Survival is sufficient; glory is exceeding. No resource cost; the Jarl provides arms and food. | Faction martial hospitality (lodging and food) in Varfell territories; right to carry arms in Varfell courts; bench at the Jarl's hearth | Must respond to muster call within 1 season | Space at the hearth (communal sleeping in the hall); common dining | Huscarl's band (wrist-wrapped cloth in the Jarl's colors); hand-axe or seax issued | The Jarl the player served (relationship is personal, not institutional) | Refusing muster without lawful impediment; or proven cowardice in battle |
| **2** | **Thane** (Thegn) | Complete 2 Huscarl-rank Duties at Success+; participate in at least one mass battle with Overwhelming or Success result (the combat outcome matters, not only the Duty outcome). | May lead a unit of 2 in mass battle; access to Varfell intelligence (Threat level, not details); may bring 3 armed retainers into Varfell settlements | Must maintain personal military contribution (participate in at least 1 military action per year-arc); annual presence at the Jarl's winter court | Thane's bench (named seat in the Jarl's hall); own chamber in the hall if present for more than one season | Thane's ring (gold or silver by the Jarl's wealth); long-axe or sword; embroidered cloak in the Jarl's colors | Senior Thane of the hearth (Standing 3+ named Thane) | 2 consecutive year-arcs without military contribution; or loss of ring in dishonor (gambling, theft, breach of hospitality) |
| **3** | **Lendmann** (Lendmann) | **Formal Recognition Event:** The Jarl grants the player a **Land-Grant** — a specific settlement or defined territory to govern. The grant is ceremonial (public), specific (one named settlement), and contractual (obligations defined). Plus: 3 completed Thane-rank Duties with at least one Exceeding. | Governs an assigned settlement with full local authority; may conscript local garrison; may invoke Varfell's name to requisition local resources | Must develop assigned settlement (Prosperity or Defense +1 within 2 year-arcs); must appear at the annual Jarl Assembly | Lendmann's Hall — private hall in the governed settlement; maintains own hearth and hearth-guard | Lendmann's torc (neck ring, rank-marker); household banner (distinct from Jarl's banner); horse | Jarl of the land (the specific Jarl who granted the land — always that one, regardless of internal Varfell politics) | Settlement Order falling to 0 for 2 consecutive seasons; or Jarl revokes the Land-Grant (requires public assembly consent; can be politically costly) |
| **4** | **Senior Lendmann / Hersir** (Hersir) | Successful defense of assigned settlement through 2 year-arcs; OR expansion of governance to include an adjacent settlement; OR **Public Deed** — a named mass battle victory under the player's command (not merely participation). | Leads multiple settlements or a defined march; may direct 3 NPC officers; may request Thread-related resources from Vaynard's Private Collection (Ob +2, via Senior Jarl sponsor); eligible for Varfell Colonist card actions (per tc_political_redesign §5.2) | Must govern march-level holding; must contribute Military ≥ 2 per year-arc at the Varfell level; must attend Jarl Assembly | Hersir's Great Hall; permanent retinue of 8+ retainers; local magistrate authority | Hersir's heavy torc; personal standard; war-mail gifted by the Jarl | Senior Jarl (a Standing 6 Jarl in the Jarl Assembly) | Mass military defeat (loss of battle with −2 margin+, per mass_battle_v30 §B.3); or loss of a settlement without authorized withdrawal |
| **5** | **Jarl** (Jarl) | Raised by an existing Jarl (who resigns or dies, vacating the seat) OR by unanimous agreement of the Senior Lendmänner of the region. Requires: completed 3 Hersir-rank Duties with at least one Recognized Deed (endorsed by another Jarl, by the Skald-Chief, or by Vaynard personally). | Controls a province or province-equivalent; Jarl Assembly seat with full voting rights; may conduct independent military operations with prior notice to Vaynard; +1 scene action from Varfell resources | Must attend the annual Jarl Assembly (once per year-arc — missed attendance without honorable cause is a Standing −1 event); must contribute Military ≥ 2 per year-arc; must uphold personal warranty (a Jarl's word is contract) | Jarl's Great Hall (often a fortress — the Jarl's residence and court); permanent retinue of 15+; rights to regional taxation | Jarl's Crown (heavy gold torc marked with province symbol); personal war-banner; Vaynard's confirmation gift (varies) | Vaynard directly for martial matters; the Skald-Chief for traditional disputes | Absent from Jarl Assembly without honorable cause; Military contribution falling to 0; or the assembly voting the Jarl out (rare — requires unanimity minus one) |
| **6** | **Senior Jarl** (Markherr) | Seniority by service: the player has been a Jarl for at least 4 year-arcs OR led Varfell forces in at least 2 successful campaigns. Plus: unanimous Jarl Assembly confirmation (all other senior Jarls at Disposition ≥ 0). | Chairs one of the five standing Jarl Assembly councils (see §7.4); speaks with acting authority on specialty matters (Martial, Resource, Cultural, Warden, Foreign); may convene regional mustering of multiple Jarls | Must chair at least one Assembly council; must manage regional Military ≥ 3; must attend all Assembly sessions | Senior Jarl's Seat — permanent place at the Jarl Assembly high table; Vaynard's confidence | Senior Jarl's broad-torc; province standard at Assembly | Vaynard only; plus (for cultural matters) the Skald-Chief | Loss of council chairmanship (Assembly vote); or military failure of a campaign the Senior Jarl commanded |
| **7** | **High Thane / Jarl-Regent** (Hochjarl) | Jarl Assembly elects the player as Vaynard's Regent (during Vaynard's absence or incapacity) OR as designated successor (Vaynard names the player at a public Assembly). Requires: majority support of the senior Jarls (3 of 5 at Disposition ≥ +1); personal performance in either a completed Varfell Deed (path B or C — see victory_v30 §3 and varfell_path_b_v30) or a Grand Contest victory (per the original register SUC-01 Varfell mechanic). | May convene Jarl Assembly in Vaynard's absence; succession-eligible (Varfell elective succession per SUC-01); speaks for Varfell in inter-faction negotiations; direct access to Vaynard's Private Collection (Ob +0 rather than +2) | Must hold Senior Jarl majority; maintain Military ≥ 4 in Varfell provinces; active pursuit of Varfell strategic priority (currently Path A, B, or C per Vaynard's campaign posture) | Jarl-Regent's Hall at Sigurdshelm (Vaynard's seat); access to Vaynard's private quarters; household of 20+ | Jarl-Regent's regalia — Vaynard's secondary torc (ceremonial); personal seal of state | Vaynard only | Loss of Jarl majority (Senior Jarls withdrawing support — SUC-03); or public military failure at campaign scale |


#### §1.3a Hochjarl Incapacity Assessment (ED-673)

The oral law provision referenced in Varfell succession — when a Hochjarl or Vaynard himself is deemed incapable of leadership — requires formal definition.

**Triggers (any one sufficient):**

| Trigger | Initiator | Evidence required |
|---|---|---|
| Physical incapacity | Any Senior Jarl | Witnessed injury or illness lasting ≥ 2 seasons; confirmed by at least 1 other Senior Jarl |
| Mental incapacity | Any Senior Jarl | 2 consecutive Assembly sessions where the assessed leader's orders are incoherent or contradicted within the same session; witnessed by majority of Assembly |
| Prolonged absence | Jarl Assembly automatic | Leader absent from Assembly for 3 consecutive sessions without designating a Regent |
| Conviction collapse | Player or NPC action | Leader's Certainty reaches 0 AND Conviction Scar count ≥ 3 (the leader's framework has disintegrated) |

**Process:**

1. **Invocation:** Any Senior Jarl declares Assessment at the Jarl Assembly. Costs the invoker Disposition −1 with the assessed leader (challenging leadership is personal).
2. **Deliberation:** All Senior Jarls vote. Majority (3 of 5) required to confirm incapacity. The assessed leader may speak in their own defense (Social Contest, Ob 2; Success: one Senior Jarl switches vote to oppose Assessment).
3. **Duration:** If Assessment passes, the assessed leader is removed from active leadership for a minimum of 2 seasons (recovery period). A Regent is appointed per Standing 7 succession rules.
4. **Outcomes:**

| After recovery period | Result |
|---|---|
| Leader recovers (injury heals, Certainty ≥ 1) | Reinstated automatically. Regent steps down. |
| Leader does not recover after 4 seasons | Permanent removal. Succession fires per SUC-01 Varfell elective process. |
| Leader dies during assessment | Immediate succession per SUC-01. |

**Vaynard-specific:** If Vaynard is assessed as incapacitated, the Hochjarl (if one exists) automatically becomes Regent. If no Hochjarl exists, the Senior Jarl with highest Military contribution becomes acting Regent until formal election.


### §1.3b Varfell Specialty Branches (Unlocks at Standing 3)

| Branch | Assembly Council | Sub-office opens | Primary mentor line |
|--------|------------------|------------------|---------------------|
| **Martial** | Council of the March | None (Varfell-internal) | Senior Jarl of the Eastern March |
| **Resource** | Council of the Highlands | None (Varfell-internal) | Senior Jarl of the Western Highlands |
| **Cultural** | Council of the Skald | Warden of the Thread ladder opens (Part 2, §2.7) if the player has Thread Sensitivity ≥ 30 AND WA ≥ +1 | Skald-Chief |
| **Warden** | Council of the Warden | Warden of the Thread ladder opens (Part 2, §2.7) — this is the canonical path via Edeyja sponsorship | Edeyja (Warden-Chief, npc_roster_v30 #1) |
| **Foreign** | Council of Voices (delegation/diplomacy) | None | Huscarl Captain (Vaynard's personal guard) |

### §1.3c Varfell Inner Circle — Named (resolves ED-POL-01, partial)

| Role | Proposed Name | Conviction | Resonant Style | Certainty | Notes |
|------|---------------|------------|----------------|-----------|-------|
| Senior Jarl of the Eastern March | **Thorvald Hann** (canonical heritage — referenced obliquely in prior registers) | Order | Authority | 5 | Largest Varfell military bloc; conservative, bloodline-focused succession advocate. Disposition toward Maret Uln starts at −1 (she represents elective-Einhir succession to him). |
| Senior Jarl of the Western Highlands | **Björn Holdar** (new — ED-637; renamed from initial "Björn Torben" to avoid collision with heir Torben Almqvist) | Precedent | Evidence | 4 | Controls resource-rich western fjords. Needs player cooperation for continued settlement development. Caste-neutral. |
| Skald-Chief | **Ingrid Stenskald** (new — ED-638; renamed from initial "Ingrid Ehrenwall" to avoid collision with canonical Löwenritter Grand Master Ehrenwall) | Continuity | Evidence | 5 | "Stenskald" = stone-skald; keeper of Varfell's oral law; validates claims. Hard requirement: any Deed-Claim succession in Varfell needs the Skald-Chief's endorsement (or the Skald-Chief's death, which creates a secondary succession crisis). |
| Vaynard's Huscarl Captain | **Maret Uln** (canonical — npc_roster_v30 #2) | Community | Evidence | 3 | She is already canonical as Varfell Practitioner / Succession Fallback. Promoting her to Huscarl Captain rather than a separate role resolves two issues: (a) it makes her mechanically proximate to Vaynard without requiring player investment; (b) her Southern Einhir solidarity (npc_roster §14) now has direct access to Vaynard's ear. |
| Warden Liaison | **Edeyja** (canonical — npc_roster_v30 #1; appears in Inner Circle only on Path B, WR ≥ 3) (PP-663: VTM reference replaced) | Warden | Evidence | 4 | Technically Warden-Chief (Southernmost), not Varfell. Becomes Inner Circle member if Vaynard has committed to Path B (Thread work). Her Conviction "Warden" is Varfell-specific — a Conviction tier above the standard 5 (see ED-641 below). |

---

## §1.4 CHURCH RANK LADDER (Church of Solmund)

**Faction ethical framework:** Divine Command (factions_ttrpg_v30 §8.3). Doctrine-aligned actions are −1 Ob; contradiction is +1 Ob; Thread-revealing actions are +2 Ob. This is the ladder where **what the institution teaches is true by definition** — advancement requires doctrinal coherence, not necessarily empirical truth.

**Core institutional logic:** The Church is organized under a **Four-Cardinal structure** (worldbuilding_v30 §3.1). Each Cardinal heads one Arm (Fortitude/Military, Justice/Judicial, Prudence/Economic, Temperance/Knowledge). This is the Church's equivalent of specialty branches — but because the Cardinals themselves are canonical NPCs (Jarnstal, Olafsson, Prudence [unnamed], Klapp), a Church player's specialty branch is *discipleship to a named Cardinal*. The mentor relationship is more binding in the Church than in any other faction.

**Critical:** the TC political legitimacy bonus (tc_political_redesign_v30 §3.2) interacts strongly with Church rank — see Part 5. Advancement above Standing 3 effectively requires the player to manage their Cardinal's institutional position as well as their own.

### Church Ladder Table

| Standing | Title | Initiation Gate | Access | Obligations | Hall Tier | Livery | Mentor | Demotion |
|----------|-------|-----------------|--------|-------------|-----------|--------|--------|----------|
| **0** | **Catechumen** (Katechumen) | Character creation + presence in a Church-controlled settlement for 1 season + successful first instruction (social scene, Ob 1, with any Standing 2+ Church NPC at Disposition ≥ 0). | Permission to attend public services; standing to petition for instruction | Observance of public rite; no formal Thread contact (any Thread Sensitivity ≥ 30 in a Catechumen is immediately suspect — automatic Exposure +1 in any Church-adjacent scene) | Lay lodging in a Cathedral settlement's cloister (modest cell, shared meals) | Plain white robe for public services; wooden devotional | Instructor-deacon (Standing 2) | Discovered Thread engagement; or persistent theological non-alignment |
| **1** | **Lay Confessor** (Laibeichtvater) | **Initiation Duty:** "Witness the Solmund Codex" — the player participates in a formal Codex reading (scene arc, requires travel to Himmelenger T9, social attendance, and one doctrinal Interview passed). | Church hospitality in Cathedral settlements; right to assist in public ceremony; access to Cathedral reading room (public texts only) | Must observe Church doctrine publicly; must report to Cathedral superior at least monthly | Shared chamber in Cathedral quarters | Lay Confessor's white robe with single stripe; plain cross | Deacon (Standing 2) of the assigned Cathedral | Public heresy; or Thread engagement |
| **2** | **Deacon** (Diakon) | Complete 2 Lay Confessor Duties with Success+; pass Scriptural Examination (oral Ob 2, adjudicated by a Canon). | May conduct minor Church services (raises PT/CV +1 in the serving territory during service — subject to ±1/season cap); access to Church correspondence network (1 free information relay/season) | Must serve a Cathedral settlement; must report Thread activity to Church superior | Private cell in the cloister of the serving Cathedral | Deacon's black robe with white collar; iron cross | Canon (Standing 3) | Failure to report Thread activity that is later discovered; or 3 consecutive service failures |
| **3** | **Canon** (Kanoniker) | **Formal Recognition Event:** Investiture by a Cardinal (not by Himlensendt directly — the Cardinal of the player's specialty branch performs the ceremony). Mandatory: 3 Deacon-rank Duties with Success+; at least one Thread reporting that led to Inquisitorial follow-up; doctrinal specialty declared (alignment to one of the Four Cardinals). | Church institutional authority in one territory (can sanction investigations within territory; +1D on Church-aligned fieldwork); access to sealed Church archives in the home Cathedral; Inquisitor sub-ladder opens (Part 2, §2.3) if player aligned to Justice; Templar sub-ladder opens (Part 2, §2.4) if aligned to Fortitude | Must adhere to theological positions of the assigned Cardinal (not just the Confessor — the Cardinal is the direct superior); must conduct regular pastoral work; must file quarterly reports to the assigned Cardinal | Canon's Chamber (private apartment in Cathedral quarters); access to the Canon-level refectory | Canon's black cassock with Cardinal-arm trim (Red for Fortitude/Templars, Blue for Justice/Inquisitors, Gold for Prudence/Economic, Green for Temperance/Knowledge); pectoral cross with Cardinal device | Assigned Cardinal (named NPC) | Theological contradiction (publicly contradicting the Cardinal's doctrine); or failure to conduct pastoral duties; or Thread Sensitivity reaching 30 without institutional sanction |
| **4** | **Bishop's Delegate** (Bischofslegat) | 3 completed Canon-rank Duties; plus one **Public Doctrinal Defense** — the player successfully defends a theological position in public (a form of Grand Debate, Ob 2, against a named Thread-curious opponent or a theological skeptic). Plus: Cardinal's personal endorsement. | May conduct ecclesiastical trials in own territory (Heresy Proceedings per OFC-03); may grant or withhold Church blessing (affects Mandate ±1 for the blessed/cursed faction); access to Himlensendt's private deliberations (Availability State: In Session + In Private Retreat); manages a Church Sekretum or Dicastery equivalent (see §7.3) | Must manage Church Attention Pool in assigned territories; must advise the Confessor on TC-sensitive matters; must chair a Sekretum | Bishop's Delegate Suite in the Cathedral (apartment with private devotional chapel); rights to consecrate minor structures | Delegate's purple-trim cassock; Episcopal ring (conferring Church administrative authority in ecclesiastical trials); Cardinal's arms embroidered on mantle | Cardinal directly; plus (for high-stakes matters) Himlensendt | Church Attention Pool reaching 5 in assigned territory without response; theological defection; or Cardinal withdraws endorsement (Disposition ≤ −1) |
| **5** | **Prelate** (Prälat) | Unanimous College of Prelates confirmation (all 5 Prelates at Disposition ≥ 0); plus one **Recognized Deed** — an action the Holy See endorses, or an Altonian Church acknowledgment (if AEA ≥ 3 per conviction_track_v30 §4.2). | Member of the College of Prelates; succession-eligible to Confessor; may cast deciding vote on Church policy questions; Mandate of the Church follows the Prelate's counsel when Confessor delegates; chairs a Cardinal-branch division; may initiate Cardinal Independence Checks (per worldbuilding_v30 §3.2) with institutional consequences | Must maintain theological alignment with majority of College; must actively manage TC in 2+ territories; must advise Confessor on succession-relevant matters; must consult at Holy See if summoned | Prelate's Palace in Himmelenger (T9) — separate residence within the Cathedral precinct; full household; private chapel; sealed-archive access | Prelate's scarlet cassock with full Cardinal arms; Prelate's crozier (authority symbol in public contexts); Cathedral keys (physical symbol of institutional control) | Himlensendt only (or, in Himlensendt's absence, the senior Prelate of the College) | College majority turning against player; theological breach causing schism within the College; or Conviction strain (personal faith crisis) at Certainty ≤ 1 — the Prelate's personal faith must be *functioning* for the rank to function |
| **6** | **Cardinal** (Kardinal) | Vacancy in one of the Four Cardinal seats (Fortitude, Justice, Prudence, Temperance) — this only happens when the incumbent Cardinal dies, is deposed, or is raised to Confessor. College of Prelates elects (2/3 supermajority). Requires: at least 4 year-arcs as Prelate; personal endorsement of the outgoing Cardinal (if alive) or of the current Confessor; no outstanding Grand Debates against the player. | Heads one of the Four Arms of the Church (Fortitude/Templars, Justice/Inquisitors, Prudence/Economic, Temperance/Knowledge); controls the arm's Military/Investigation/Wealth/Scholarly resources respectively; named character — triggers Named Character Event Cards specific to the Cardinal's arm (per worldbuilding_v30 §3.3) | Arm-specific — the Cardinal *is* the institutional embodiment of the arm. Jarnstal-analog must deploy Templars without excessive independence (watch Jarnstal Drift mechanic); Olafsson-analog must avoid Niflhel exposure; Prudence-analog must manage charities to avoid Prudence Crisis Event; Klapp-analog must manage Thread-adjacent text handling without institutional reveal. | Cardinal's Palace (Himmelenger or secondary Cathedral); full household; institutional resources of the Arm | Cardinal's red robes with full regalia; full insignia of the Arm (Templar cross for Fortitude, scales for Justice, balance for Prudence, open book for Temperance); Cardinal's ring | Himlensendt only | Arm-specific catastrophic event (Jarnstal Independence card, Olafsson Exposure card, Prudence Crisis card, Klapp Awakening card) if poorly managed; or College of Prelates Cardinal Independence Check failed at Ob 3; or public schism from the Confessor |
| **7** | **Confessor-Presumptive** (Bekennerpräsident-designiert) | The Confessor position opens (Himlensendt dies, is incapacitated, or has a Crisis of Faith) AND the player is either (a) the Cardinal with College of Prelates majority, or (b) unanimously elected by the College to succeed. This is a *pre-investiture* state. Formal Consecration (see §1.4c) elevates to actual Confessor. | Confessor-equivalent operational authority in Himlensendt's absence; may issue provisional pronouncements pending Consecration; administers the TC bonus-dice pool (floor(TC/20)) as Church's primary political operator | All Prelate and Cardinal obligations combined; pending Consecration must occur within 2 seasons or the position defaults to the next College-majority candidate | Confessor's Residence in Himmelenger (T9) — the single most secure location in the peninsula, the Cathedral's inner citadel | Confessor-Presumptive robes (gold-trimmed white); pending pallium (Consecration token); full Church arms | Holy See-equivalent counsel (off-stage — narrative only) | College rejects Consecration; or rival Cardinal assembles supermajority alternative; or Baralta Crown Claim fires concurrently, creating a Consecration Crisis (baralta_crown_claim_v30 §3) |

### §1.4b Church Specialty Branches (Cardinal Discipleship)

| Branch | Cardinal | Sub-office opens | Dicastery (see §7.3) |
|--------|----------|------------------|----------------------|
| **Fortitude / Military** | Jarnstal (canonical) | Templar ladder (Part 2, §2.4) | Dicastery for the Defense of the Faith |
| **Justice / Judicial** | Olafsson (canonical; also Haelgrund as Cardinal Justice alternate — npc_roster_v30 #4) | Inquisitor ladder (Part 2, §2.3) | Dicastery for Doctrinal Adjudication |
| **Prudence / Economic** | Aldric Tormann (canonical — npc_roster_v30 §13) | None (Church-internal commercial management) | Dicastery for Temporal Affairs |
| **Temperance / Knowledge** | Klapp (canonical) | Warden of the Thread-adjacent (rare — requires Klapp-specific sponsorship; see §2.7) | Dicastery for Doctrine and Archives |

### §1.4c Consecration

Consecration is the formal elevation of Confessor-Presumptive (Standing 7) to Confessor (Leadership). It requires:

1. **Holy See concurrence** (off-stage narrative check — Dispositional with the fictional Valorian Papacy; abstract at Valoria scale, but mechanically: GM-determined +1 Ob on the Consecration ceremony roll for each year-arc the Church's TC has been below 30 in the preceding 3 year-arcs).
2. **College of Prelates unanimity** (all 5 Prelates at Disposition ≥ 0 — rival Cardinals must have been co-opted or silenced).
3. **Consecration ceremony** (scene arc at Himmelenger T9 — mandatory Zoom In).

**Consecration under duress** (baralta_crown_claim_v30 §3): if the Hafenmark Crown Succession Contest is active and Baralta requires consecration, the ceremony is attempted even without Holy See concurrence — see Part 6.

---

## §1.5 Skyrim Integration Summary

The Skyrim Eight are applied consistently across all four primary factions. The table below shows cross-faction pattern:

| Skyrim element | Crown | Hafenmark | Varfell | Church |
|----------------|-------|-----------|---------|--------|
| Initiation Duty (Std 0→1) | Carry the King's Word | File the Petition | Answer the Muster | Witness the Solmund Codex |
| Specialty branch (Std 3) | Martial / Admin / Intel | Judicial / Commercial / Martial | Martial / Resource / Cultural / Warden / Foreign | Fortitude / Justice / Prudence / Temperance |
| Hall tier (lowest private quarters) | Std 3 Banneret's Cloister | Std 3 Alderman's Office | Std 2 Thane's Chamber | Std 3 Canon's Chamber |
| Leadership-adjacent hall | Std 6 Prince's Wing | Std 6 Chancellor's Tower | Std 7 Jarl-Regent's Hall | Std 6 Cardinal's Palace |
| Livery at lowest rank (Std 1) | Crown tabard | Advocate's sash | Huscarl's band | Lay Confessor's robe |
| Livery at highest rank (Std 7) | Regent's circlet + Crown-colors | Speaker-Regent's device + state-colors | Jarl-Regent's regalia + Vaynard's secondary torc | Confessor-Presumptive robes + pending pallium |
| Rank-gated trainer/mentor | Rank-appropriate NPC; always named; Disposition-dependent | Same | Same (plus cultural mentors — Skald-Chief) | Always a named Cardinal post-Std 3; Disposition + doctrinal alignment |
| Dismissal mechanism | Revoked Banner / inner-circle ouster | Censure / coalition collapse | Assembly vote / Jarl revocation | Heresy / theological defection |
| Rival cohort at Std 3 | Named Banneret rival | Named Alderman rival | Named Lendmann rival | Named Canon rival (within same Cardinal branch) |

Variance between factions reflects ethical framework: Crown rewards Virtue visibility; Hafenmark rewards procedural correctness; Varfell rewards demonstrated results; Church rewards doctrinal coherence. The **same** rank position (Standing 4, "Lieutenant-equivalent") thus carries different privileges and different costs in each.

---

# PART 2 — SUB-OFFICE RANK LADDERS

The original register specifies Office Specifications (OFC-01 through OFC-04) for Löwenritter, Riskbreaker, Inquisitor, and Templar — but without ranks. This Part builds the ladders and adds three more sub-office ladders: Guilds (per worldbuilding_v30 §5), Niflhel (per factions_ttrpg_v30 §8.7), and Wardens of the Thread (per Edeyja/Maret Uln mechanics).

**General rule:** A sub-office rank is *not* a primary-faction rank. Standing in a sub-office is tracked separately but interacts with the primary-faction ladder. For example: a Löwenritter Knight-Commander (sub-office Standing 5) retains Crown Standing in the Martial branch (typically Crown Standing 4–5). Branch advancement in one track does not automatically advance the other. The sub-office chain of command is *parallel*, not hierarchical-subordinate, to the primary chain — this is the Knight Templar historical model (the military order reports to its own Grand Master and ultimately to the Pope, not to the secular king, even while serving in the king's territory).

## §2.1 Löwenritter Knight Ladder

**Parent faction:** Crown (Martial branch). **Ethical framework:** Order-aligned; institutional.

**Core tension:** Lions' Table (military coordination), Royal Guard, and Knights of the Peace are all under the Löwenritter umbrella. The Grand Master (Ehrenwall) answers to the Crown at the faction level but to no one at the Order level. Crown authority attempts to direct the Order through the Royal Marshal (Voss) — but the Order's internal rank is determined by the Grand Master.

### Löwenritter Ladder

| Lr-Std | Title | Gate | Access | Obligations | Hall | Livery | Mentor | Demotion |
|--------|-------|------|--------|-------------|------|--------|--------|----------|
| 0 | Squire (Knappe) | Crown Martial branch Std 2 or sponsored (a current Knight vouches) | Hospitality at any Löwenritter-managed settlement (S-012, S-014) | Attend to a Knight; field service within 1 season | Squire's quarters at Ehrenfeld Citadel | Squire's mantle (white with single lion) | Assigned Knight | Disgrace, desertion |
| 1 | Knight (Ritter) | **Initiation Duty:** one successful escort mission OR one combat engagement with Success+; Squire has served ≥ 1 year-arc | Command of a squadron; Löwenritter-issued armor and horse | Garrison duty as assigned | Knight's chamber at Ehrenfeld or any Löwenritter settlement | Full Knight's arms (white tabard with Löwenritter lion, chainmail+plate) | Knight-Sergeant | Dishonor, refusing a lawful order from Grand Master's chain |
| 2 | Knight-Sergeant (Ritterfeldwebel) | 2 completed Knight-rank Duties at Success+; mass battle participation | Command of 3 squadrons; authority to detain in Löwenritter jurisdiction | Regular garrison assignment; quarterly report to Knight-Commander | Sergeant's billet | Sergeant's mantle with gold piping | Knight-Commander | Sustained garrison failure |
| 3 | Knight-Commander (Ritterkommandeur) | 3 Sergeant-rank Duties including one Overwhelming mass battle; Grand Master's personal endorsement | Commands a garrison or field company (up to 2 units per mass_battle_v30 §A); may initiate independent garrison action without Crown authorization (Löwenritter chain only) | Commands a specific garrison; maintains Order discipline; reports quarterly | Commander's Quarters (private rooms in the garrisoned Citadel) | Commander's mantle with silver trim; personal arms on shield | Preceptor (Standing 4) | Catastrophic garrison loss; or Grand Master's dismissal |
| 4 | Preceptor (Präzeptor) | Commands multiple garrisons or a regional command; 4 year-arcs as Knight-Commander minimum; unanimous Knight-Commander confirmation in region | Regional Löwenritter authority; may convene Knights within region | Management of regional Order assets; training responsibilities | Preceptor's Residence at a designated regional Citadel | Preceptor's full regalia | Grand Master or Riskbreaker Commander (only if Preceptor is Riskbreaker-aware) | Dismissal by Grand Master |
| 5 | Marshal of the Order (Ordensmarschall) | Grand Master's designation; one of 3 Marshal positions (Western, Eastern, Naval — Lions' Helm though naval is [NO MECHANICS] per worldbuilding §4.1); 6 year-arcs minimum as Preceptor | Coordinates Löwenritter operations across multiple regions; eligible to stand as Grand Master successor | Administration of Order strategic assets | Marshal's Hall at Ehrenfeld; seat at the Lions' Table | Marshal's full regalia with regional colors | Grand Master directly | Grand Master removal by full Lions' Table vote |
| 6 | Grand Master-Designate | Grand Master names successor OR 2 Marshals unanimously endorse; formal Lions' Table confirmation | Full operational control of Order in Grand Master's absence | Preparation for Grand Master accession | Grand Master's Wing of Ehrenfeld Citadel | Grand Master's arms with personal device | Grand Master (Ehrenwall canonically) | Lions' Table withdraws confirmation |
| 7 | **Grand Master** (Großmeister) | Accession on Grand Master vacancy (Ehrenwall's death, removal, or succession to Crown) | Full Löwenritter leadership; treaty-equivalent relations with other factions | All Order obligations | Ehrenwall's seat at Ehrenfeld | Grand Master's regalia | No mentor — is mentor to the Order | Coup Counter mechanisms (original factions_ttrpg_v30 §8.9); Crown repudiation |

**Riskbreaker Branch:** at Löwenritter Standing 3 (Knight-Commander), the player may be recruited into the Riskbreaker sub-ladder (§2.2 below). Recruitment is covert and invisible to the parent Order chain. A Riskbreaker retains their Knight-Commander rank publicly but operates on a separate Riskbreaker rank ladder privately.

---

## §2.2 Riskbreaker Ladder (Covert sub-ladder within Löwenritter)

**Parent:** Löwenritter (Std 3+ only; recruitment requires Knight-Commander rank minimum and covert Intel-aligned Conviction). **Ethical framework:** Hidden conviction: Valoria (nation as idea) — worldbuilding_v30 §4.2.

**Core principle:** Riskbreakers officially do not exist. Their ranks are maintained off-paper. Every advancement is a Shadow Renown event (original REN-03).

### Riskbreaker Ladder

| Rb-Std | Title | Gate | Access | Obligations | Hall | Livery | Mentor | Demotion |
|--------|-------|------|--------|-------------|------|--------|--------|----------|
| 0 | Candidate | Recruitment offered by Riskbreaker Commander or operative Riskbreaker; Conviction-check vs Valoria alignment (roll: Intel vs Ob 2, Overwhelming required) | Meeting with recruiter (single scene) | Confidentiality (breach = immediate termination) | None (meetings in-field) | None — Candidates wear Knight-Commander identity publicly | Riskbreaker Recruiter (TBD) | Confidentiality breach |
| 1 | Operative (Geheimagent) | **Initiation Duty:** one covert operation successfully completed (subterfuge action, no Exposure events, Ob 2) | Access to Riskbreaker communication network; 1 stash point established | Accept any mission; no refusals (Deniability Debt accrues on refusal) | Stash point (player-specified location) | None public; concealed Riskbreaker token on person | Operative-Senior (TBD) | Mission refusal × 2; or exposure that implicates the Order |
| 2 | Senior Operative | 3 completed Operative-rank missions including one Overwhelming | Squadron-coordination authority (can direct other Operatives covertly); may establish new stash points | Mission sequence continuity; may take apprentice Candidates | 2 stash points; safe-house access in any Löwenritter-garrisoned city | None (same as Op) | Squad-Leader | Catastrophic exposure |
| 3 | Squad-Leader (Truppführer) | 5 completed missions; has recruited and successfully apprenticed 1 Operative | Operational control of a 3-person Riskbreaker squad; may authorize assassinations within approved mission scope | Squad management; reports directly to Commander | Squad safe-house network | None public; squad identifier token | Riskbreaker Commander | Squad catastrophic failure |
| 4 | Field-Commander | 3 successful squad-led campaigns; endorsement by Riskbreaker Commander | Regional Riskbreaker operations; authority over multiple squads; may operate in cross-faction contexts | Regional operational integrity | Designated safe-house network | None | Riskbreaker Commander | Regional catastrophe |
| 5 | Deputy Commander | Commander's personal selection; 4 year-arcs minimum as Field-Commander | Operational authority in Commander's absence; sees all Riskbreaker strategic deployments | Preparation for Commander succession | Commander's inner office (Ehrenfeld subbasement, unofficially) | None | Riskbreaker Commander | Commander repudiation |
| 6 | **Riskbreaker Commander** | Commander succession (prior Commander eliminated, retired, or promoted to Löwenritter Grand Master) | Full Riskbreaker leadership; answers only to Grand Master; may veto Löwenritter operations via covert sabotage | All Riskbreaker strategic management | Private meeting rooms at Ehrenfeld | None | Grand Master (covert) | Grand Master dismissal or Riskbreaker Exposure Card trigger |

The Riskbreaker ladder tops at Standing 6 (not 7) because there is no rank above "Commander" — the Commander reports directly to the Grand Master. Promotion above would put the Riskbreaker on the Löwenritter Grand Master track, which is structurally possible but ends the covert career.

**Deniability Debt** (stage13 mechanic, retained) accumulates at all levels and is the Riskbreaker-specific demotion risk. See §2.2b below for full mechanical spec.

---

## §2.2b Shadow Renown and Deniability Debt — Mechanical Specs

[CANON 2026-04-19 — ED-632 / ED-633 resolved. Jordan-approved. Preserves existing Riskbreaker Exposure card thresholds (Debt 3/5) from worldbuilding_v30 §4.3. Specs parallel Renown (player_agency_v30 §5.4) for the covert track.]

### §2.2b.i Shadow Renown (0–10)

**Definition.** Shadow Renown measures the player's cross-faction personal significance accrued through covert actions. It is the Riskbreaker- and intelligence-community mirror of public Renown: every gain represents reputation earned inside informal networks that cannot be publicly cited. Shadow Renown and public Renown are separate tracks.

**Sources:**

| Source | Shadow Renown Gained | Condition |
|--------|----------------------|-----------|
| Covert mission (Operative+) succeeds | +1 | No Exposure event; target Disposition verifies completion |
| Covert assassination / sabotage success | +1 | Per §2.2 Riskbreaker mission ranks; cap once/target/season |
| Intelligence delivered to faction or patron | +1 | Verified actionable (changes an Ob or reveals a hidden NPC stat) |
| NPC recruited as Shadow Asset | +1 | Ongoing Knot with Disposition ≥ +2; target knows only the cover identity |
| Black-market trade closed at Overwhelming | +1 | Only counts for illicit goods or information; legitimate trade routes go through public Renown |
| Riskbreaker promotion event | +1 | Automatic; each Rb-Std advancement per §2.2 ladder |

**Cap:** +2 Shadow Renown per season maximum. Shadow Renown does not decay naturally.

**Effects:**

| Shadow Renown | Effect |
|---------------|--------|
| 3+ | Covert NPCs (spymasters, fences, informants, Riskbreaker peers) at neutral Disposition start at +1. |
| 5+ | +1D on Interrogate, Extort, and Black-Market-Contact actions. |
| 7+ | Independent covert Domain Action: pool = floor(Shadow Renown ÷ 2), resolved outside any faction's Mandate/Intel pool (Riskbreaker Commander authority). |
| 9+ | May initiate an Exposure Event against a target (trades Shadow Renown for Deniability Debt per §2.2b.ii; see exchange table). |

**Display and tracking.** Shadow Renown is a private subfield on the companion app (per ED-POL-04 resolution). It cannot be cited in public social contests (Grand Debate, Parliament, Ceremonial Scene) — citing converts the spend to public Renown at a 2:1 loss, and inflicts +1 Deniability Debt for each citation. Shadow Renown above the cap (10) spills into Deniability Debt at 1:1.

**Conversion — successful Exposure.** If a Shadow Renown action becomes public (Exposure Event resolves against the player), each +1 Shadow Renown earned from the now-public action converts to **−1 public Renown** (Infamy penalty) and +1 Deniability Debt. This is the risk profile that makes covert operation mechanically distinct from overt reputation-building.

### §2.2b.ii Deniability Debt (0–7, cap 7)

**Definition.** Deniability Debt is the Riskbreaker-specific tracked risk that the Order's covert operations leave traces. It accumulates from operational friction (evidence trails, partial successes, witness exposure) and discharges through cooling-off periods or dedicated counter-intelligence work.

**Accrual:**

| Trigger | Debt Gained |
|---------|-------------|
| Partial result on any Riskbreaker covert mission | +1 |
| Failure on any Riskbreaker covert mission | +2 |
| Evidence trail generated (Intel roll vs Ob 3 after the operation — failure creates evidence) | +1 |
| Witnessed by unintended non-asset NPC (GM discretion; typical trigger: ambient Standing 3+ NPC passing through operation zone) | +1 |
| Operation uses Löwenritter resources (Military stat, named knight, Lions' Helm asset) and is traced | +2 |
| Each Shadow Renown point that spills past cap 10 | +1 |

**Reduction:**

| Trigger | Debt Reduced |
|---------|--------------|
| One full season passes with no Riskbreaker operations of any kind | −1 (cooling off; does not apply if Debt ≥ 5) |
| Counter-intelligence operation succeeds (Intel vs Ob 3, once per season, Riskbreaker Squad-Leader or higher) | −1 |
| Riskbreaker Commander spends 1 Shadow Renown to purge records | −1 (once per campaign arc) |
| Parliamentary inquiry concluded in Riskbreaker favor (Grand Debate win at Debt 5 threshold) | Reset to 2 |

**Thresholds and effects:**

| Debt | Effect |
|------|--------|
| 0–1 | No effect. |
| 2 | +1 Ob on all Riskbreaker covert actions (operational caution tax). |
| 3 | **Riskbreaker Exposure card triggers** (per worldbuilding_v30 §4.3 Card: Riskbreaker Exposure). Crown Domain Actions against non-Crown factions +1 Ob. |
| 4 | Cooling-off reduction disabled (Debt sticks above 4). |
| 5 | **Parliamentary inquiry opens** — Grand Debate (Crown Influence + Mandate at stake per worldbuilding_v30 §4.3). |
| 6 | Riskbreaker operations require Commander personal approval. +2 Ob on Rb-Std 1–3 independent operations. |
| 7 (cap) | Riskbreaker Commander demotion mandatory at next Seasonal Accounting. All Rb-Std ranks demoted by 1. New Commander selected per §2.2 ladder succession rules. |

**Display and tracking.** Deniability Debt is a faction-level attribute on Löwenritter's companion-app card (per ED-POL-04). The Riskbreaker Commander and the sitting king (Almud or successor) can read it; other factions must probe via Intel actions (Ob 3) to sense the threshold band.

**Cross-references.** See §2.2 Riskbreaker Ladder for rank structure; worldbuilding_v30 §4.3 for the Riskbreaker Exposure card; player_agency_v30 §5.4 for the parallel public Renown spec.

---

## §2.3 Inquisitor Ladder (Church Justice branch sub-ladder)

**Parent:** Church (Justice branch — Canon Standing 3+ required). **Ethical framework:** Divine Command with institutional primacy; Conviction-aligned (Faith/Order).

**Core principle:** Inquisitors are investigators with theological authority. The ladder extends OFC-03 with rank-specific capabilities.

### Inquisitor Ladder

| Iq-Std | Title | Gate | Access | Obligations | Hall | Livery | Mentor | Demotion |
|--------|-------|------|--------|-------------|------|--------|--------|----------|
| 0 | Inquisitor's Scribe | Church Canon Std 3 + Justice branch alignment + Cardinal Justice sponsorship | Access to Inquisitorial files as clerk | Clerical duties; no investigation authority | Inquisitorial quarters (Cathedral subbasement) | Scribe's black robe | Senior Inquisitor | Cardinal revokes |
| 1 | Junior Inquisitor | **Initiation Duty:** successful theological examination of a named suspect (social contest, Ob 2, Faith/Order-aligned framework) | Full Inquisitor authority per OFC-03 (theological examinations in Church-presence territories); no Heresy Proceedings yet | Mandatory case reports to Senior Inquisitor; case closure within 3 seasons | Junior Inquisitor's cell in Cathedral | Black robe with silver cross | Senior Inquisitor | Heresy trial failure; or doctrinal contradiction exposed |
| 2 | Inquisitor | 3 successful Junior Inquisitor cases (closure + Cardinal approval) | May initiate Heresy Proceedings against non-leadership NPCs; access to Inquisitorial archives; +1D Interview in Church territories | Quarterly reports; case load management | Inquisitor's Chamber in Cathedral | Inquisitor's regalia (black and silver, inquisitorial cross) | Senior Inquisitor / Cardinal Justice | 2 Heresy trial failures; or archive mismanagement |
| 3 | Senior Inquisitor | 5 closed cases at Inquisitor rank; one case involved a Standing 4+ target | Regional Inquisitorial authority; may initiate Heresy Proceedings against Standing 4 targets with Cardinal authorization | Regional Inquisitorial administration | Senior Inquisitor's Quarters (private apartment) | Senior regalia with purple trim | Cardinal Justice | Overturned trial; or Niflhel exposure (Olafsson-style mechanic) |
| 4 | Inquisitor-General | Senior Inquisitor with 4 year-arcs minimum; unanimous Senior Inquisitor regional endorsement | Authority over the Inquisition apparatus in 2+ regions; manages Attention Pool strategically | Inquisition strategic planning | Inquisitor-General's Office in Himmelenger | General's regalia | Cardinal Justice (directly) | Cardinal dismissal |
| 5 | Grand Inquisitor | Cardinal Justice vacates (dies, promoted); College nominates | Cardinal-of-Justice-equivalent authority | Arm of Justice administration | Cardinal-grade housing | Cardinal's regalia | Himlensendt | Cardinal Independence Check failure; or Olafsson Exposure |

The Inquisitor ladder caps at Standing 5 because Standing 5 is the Cardinal Justice position — rank 5 IS the Cardinal. Above that is Confessor (Church Standing 7).

---

## §2.4 Templar Ladder (Church Fortitude branch sub-ladder)

**Parent:** Church (Fortitude branch — Canon Standing 3+ required). **Ethical framework:** Divine Command with martial focus; Conviction Faith-aligned; Jarnstal-inflected.

### Templar Ladder

| Tp-Std | Title | Gate | Access | Obligations | Hall | Livery | Mentor | Demotion |
|--------|-------|------|--------|-------------|------|--------|--------|----------|
| 0 | Templar Postulant | Church Canon Std 3 + Fortitude branch + Cardinal Fortitude sponsorship + martial aptitude (Combat ≥ equivalent of a Knight) | Templar cloister hospitality | Combat training; theological formation | Templar Barracks at Cathedral | Plain white mantle | Templar Sergeant | Combat failure; doctrinal error |
| 1 | Templar | **Initiation Duty:** one successful defensive action (per OFC-04, defensive only) | Full Templar authority per OFC-04 (ecclesiastical immunity, defensive ops) | Garrison duty; theological observance | Templar's cell in Cathedral barracks | Full Templar regalia (white with red cross) | Templar Sergeant | Offensive action violation; or faith crisis |
| 2 | Templar-Sergeant | 2 successful Templar-rank Duties; mass combat participation | Command of 3 Templar squadrons | Squad leadership; theological discipline | Sergeant's quarters | Sergeant regalia | Templar Commander | Sustained leadership failure |
| 3 | Templar Commander | 3 Sergeant-rank Duties; Overwhelming mass combat result; Cardinal Fortitude endorsement | Regional Templar command; garrisons at Cathedral settlements | Garrison management; theological defense | Commander's Quarters at assigned Cathedral | Commander's regalia (silver trim) | Master-Templar (Std 4) or Cardinal Fortitude | Cathedral loss; doctrinal defection |
| 4 | Master-Templar | Commands multi-Cathedral region; 4 year-arcs as Commander | Multi-region Templar command; Coordination with Cardinal | Strategic deployment; Church defense | Master's Residence at Himmelenger | Master's regalia | Cardinal Fortitude | Cardinal dismissal |
| 5 | Grand Master of the Temple | Cardinal Fortitude vacates; College nominates | Cardinal Fortitude-equivalent authority | Templar strategic administration | Cardinal-grade housing at Himmelenger | Cardinal regalia | Himlensendt | Cardinal Independence Check; Jarnstal Independence Card |

As with Inquisitor, Templar caps at Standing 5 (Cardinal-equivalent).

---

## §2.5 Guild Ladder (Hafenmark Commercial branch sub-ladder + independent Guild track)

**Parent:** Dual-parented. Hafenmark Commercial branch AND/OR Guilds as an independent faction (factions_ttrpg_v30 §8.6 — Guildmaster Council as collective leadership). **Ethical framework:** Moral Relativism.

**Core principle:** This is the most Skyrim-like sub-office structure — the Guild ladder resembles the Thieves Guild / Companions mix. A Guild member can rise in the Guilds entirely separately from Hafenmark politics (the "outside" track) or can do so through Hafenmark (the "institutional" track). The two tracks interact at Standing 3 (Free Master — worldbuilding_v30 §5.1) and above.

### Guild Ladder (Institutional track — Hafenmark-integrated)

| Gu-Std | Title | Gate | Access | Obligations | Hall | Livery | Mentor | Demotion |
|--------|-------|------|--------|-------------|------|--------|--------|----------|
| 0 | Apprentice | Accepted by a Guild Master in a trade (one scene arc, Ob 1 social) | Guild hospitality in trade territory | 3-year apprenticeship (Journeymen Years per worldbuilding_v30 §5.2) | Guild Hall apprentice quarters | Apprentice's leather tabard | Guild Master (assigned) | Desertion; theft from master |
| 1 | Journeyman | **Initiation Duty:** completion of formal apprenticeship (3+ territories worked over 2+ seasons — the Journeymen Years) | Guild Forum access; may practice trade in any Guild-territory | Trade practice; Guild dues | Journeyman's room at Guild Hall | Journeyman's mark (tool-symbol on tabard) | Guild Master (same master, now as peer-senior) | Craft fraud; Guild-rule violation |
| 2 | Free Master | 2 year-arcs as Journeyman; passes Masterpiece Examination (formal trial — scene arc, Ob 2) | Qualifies for Burgher status (Hafenmark Standing 2 integration path); may operate independent shop; may take Apprentices | Guild membership dues; Forum attendance | Free Master's workshop (personal property) | Master's insignia (guild-specific) | Senior Guild Master | Craft fraud; Guild expulsion |
| 3 | Guild Master | Elected by Free Masters in territory (Guild-specific vote); 4 year-arcs as Free Master | Controls local Guild Forum; voting member of the Guildmaster Council; qualifies for Burgher status (parallel Hafenmark Std 2) | Guild Forum chairing; Council attendance; trade regulation enforcement | Guild Master's Hall (local Guild headquarters) | Full Master's regalia; Guild-specific insignia | Senior Guild Master of the trade | Guild Schism event; local Forum revolt |
| 4 | Senior Guild Master | 4 year-arcs as Guild Master; leadership of multi-settlement Forum | Regional Guild authority; voting weight × 2 on Guildmaster Council | Regional Guild administration; integration with Hafenmark Parliamentary Commercial Committee | Senior Master's Residence | Senior regalia | Comptroller (Hafenmark Standing 5) | Multi-settlement Guild crisis |
| 5 | Comptroller-equivalent | Unanimous Senior Guild Master endorsement + Hafenmark Parliamentary confirmation | Seat on Guildmaster Council with chairing rights; direct Baralta access | Council strategic management; Hafenmark liaison | Comptroller's Office (Gransol) | Chain of office | Baralta; or outgoing Comptroller | Hafenmark Parliamentary censure; Guild Forum Revolt |
| 6 | Grand Guildmaster (if such exists — ED-642) | Unanimous Council; extraordinary circumstances only (the Council usually resists concentration) | Effectively leads Guilds-as-faction | All Council duties; Guild-Hafenmark relationship | N/A (itinerant; or Gransol) | Grand regalia | N/A | Council vote |

The Guildmaster Council leadership structure per factions_ttrpg_v30 §8.6 means Standing 6 is extraordinary and normally omitted — the Guilds are a *collective* leadership by design. This is different from the other factions and is a design feature, not a bug.

**Caste note:** Guild advancement is the most caste-open path in Valoria *at the lowest rank*. A Southern Einhir apprentice is not barred from apprenticeship. But the Masterpiece Examination (Std 1→2) is reviewed by a Free Master committee — and the committee can reject Einhir candidates on procedural grounds. Historically (per npc_roster §14) the Guilds economically benefit from Einhir caste suppression (Feldhaus AI analysis). So the Guilds are selectively open: a Southern Einhir can become Journeyman, can become Free Master with difficulty, and can almost never become Guild Master. See Part 3 for exact gating.

---

## §2.6 Niflhel Ladder (Shadow Network — not a playable faction in the ordinary sense)

**Parent:** Independent. **Ethical framework:** Amoral Consequentialism (factions_ttrpg_v30 §8.7). No Mandate, no Military. Four-arm decentralized structure: Dockworkers, Reckoners, Burned, Quiet.

**Core principle:** Niflhel does not have ranks in the formal sense. It has **standing** within the four arms, and each arm operates independently. A character can hold Reckoner Standing 4 and be a Dockworker Standing 1 simultaneously. This is not a ladder; it is four parallel informal reputations. We specify seven positions in each arm for rank-parity with other factions, but emphasize the informality.

### Niflhel Standings (per Arm)

**Dockworkers (smuggling, physical transit, waterfront):**
| Nf-Std | Title | Gate | Access |
|--------|-------|------|--------|
| 0 | Outsider | — | Hospitality if you pay |
| 1 | Runner | Known to a specific Dockworker; has served once | Minor fencing; hiding places |
| 2 | Dockhand | 2 successful runs | Full fencing network; safe movement |
| 3 | Foreman | 5 runs; leadership of small crew | Waterfront control in one settlement |
| 4 | Dockmaster | Multi-settlement waterfront control | Dockworkers' regional coordination |
| 5 | Dockslord | Endorsement by Dockworkers' council | Dockworkers arm leadership |
| 6 | Dockslord Senior | Hereditary or by force | Arm-level strategic decisions |
| 7 | — | (No formal position; the arm is leaderless at the top) | — |

**Reckoners (enforcement, debt, coercion):** analogous structure.
**Burned (infiltration, identity-theft, subterfuge):** analogous.
**Quiet (assassination, information suppression):** analogous; this is the Riskbreakers' main transactional counterpart.

**Cross-arm escalation:** Reaching Standing 4 in two arms simultaneously makes the character a **Broker** — an informal but recognized Niflhel coordinator. Brokers are rare (0–2 at any time peninsula-wide). Being a Broker provides +1D on all Niflhel-related Intel rolls but also generates Thread Tension +0.5 per season (per the Quiet Network long-term cost, generalized).

**Relationship to primary factions:** Niflhel standing *does not prevent* primary-faction Standing. But visible Niflhel association above Standing 2 in any arm makes Church Inquisitor attention a structural risk (the Attention Pool accumulates with visible Niflhel connections). Hafenmark Parliamentary ranks may be jeopardized (Motion of Censure grounds) if Niflhel Standing is exposed.

**Caste note:** Niflhel is the most caste-open institutional structure in the game. Southern Einhir are not excluded. This is why Spymaster Kolbrun Thale (Crown Inner Circle; rumored Southern Einhir heritage) can operate — she works through Niflhel contacts that would not accept a Feldhaus or an Almstedt.

---

## §2.7 Warden of the Thread Ladder

**Parent:** Varfell (Warden branch) primarily; Church Temperance branch secondarily (via Klapp sponsorship, rare); OR independent (if Renown 5+ and Edeyja sponsorship). **Ethical framework:** Warden Conviction (new — see ED-641 below).

**Core principle:** This is the only ladder where Thread Sensitivity is a hard gate. Ranks are not just political — they are tied to the character's Thread Sensitivity score, Knot count, and Warden's Accord.

### Warden Ladder

| Wd-Std | Title | Gate | Access | Obligations | Hall | Livery | Mentor | Demotion |
|--------|-------|------|--------|-------------|------|--------|--------|----------|
| 0 | Thread-Touched | Thread Sensitivity (TS) ≥ 15; awareness of the Thread (not practitioner yet) | Informal acknowledgment by practitioners | None formal | None — practitioners meet where safe | None | Any practitioner | Loss of TS (rare; possible via Forgetting Check failure) |
| 1 | Apprentice-Warden | **Initiation Duty:** TS ≥ 30; participate in one successful Thread-work action (Knot formed, or Community Weaving contribution) | Recognition by Warden-Chief (Edeyja); access to Warden safe-houses | Ongoing Thread-work; never report Thread activity to the Church | Warden safe-houses (itinerant — not a hall; it's a network) | No uniform — concealment is the norm | Edeyja or a Standing 3+ Warden | Church Inquisitorial exposure; or Forgetting Check catastrophic failure |
| 2 | Warden | 2 successful Thread operations; TS ≥ 40 | Full Warden hospitality network; may carry Thread-locked objects | Knot maintenance; practitioner protection | Safe-house network access | Discreet Warden-token (subtle, easily concealed) | Senior Warden | Exposure; or strain breakdown (Knot damage) |
| 3 | Senior Warden | TS ≥ 50; 4 successful operations; trained 1 Apprentice-Warden | Regional Warden coordination; access to Southernmost Expedition preparations | Regional practitioner network management | Regional safe-house (semi-permanent) | Warden-lock (Thread-anchored token) | Warden-Chief (Edeyja) | Catastrophic Knot failure; exposure of the network |
| 4 | Warden-Captain | TS ≥ 60; has completed Southernmost Expedition; endorsed by Warden-Chief | Authority over regional Warden assets | Strategic Warden coordination | Designated regional Warden-lock location | Senior Warden-lock | Warden-Chief | Chief withdraws endorsement |
| 5 | Warden-Senior (Council) | TS ≥ 70; 6 year-arcs minimum as Warden-Captain; Warden-Chief's council | Council-equivalent Warden leadership | Council attendance (rare — it convenes by need) | Itinerant council seat | Senior Warden-lock with personal variant | Warden-Chief Edeyja | Catastrophic personal Thread event |
| 6 | Warden-Chief Designate | Edeyja's personal successor designation | Edeyja-equivalent authority in her absence | Preparation for Chief accession | Southernmost approaches (with Edeyja) | — | Edeyja | Edeyja withdraws designation |
| 7 | **Warden-Chief** | Edeyja's death, incapacity, or retirement | Full Warden leadership | All Chief obligations | Southernmost-border residence | — | — | Successor succeeds by player's arrangement or crisis |

**Caste note:** The Warden ladder is structurally Southern Einhir-favorable. Higher baseline TS in Southern Einhir populations means the caste most stigmatized in the wider political system has easiest access to this ladder. This is not an accident; it is a design choice. The Wardens are, effectively, the resistance infrastructure for the caste system's victims — and the player who climbs this ladder encounters that dynamic directly.

---

# PART 3 — CASTE INTEGRATION LAYER

The caste system is load-bearing (npc_roster_v30 §14 — integrated from the deprecated caste-annotations file). This Part specifies how caste interacts with every rank ladder in Parts 1 and 2. The integration is deliberately asymmetric across factions, reflecting the structural-incentive argument in the deprecated file: the caste is reproduced through institutional design, not through individual intent.

## §3.1 Caste Definitions

Per npc_roster §14:
- **Northern Einhir** (Varfell highlands, Hafenmark, Crown heartland): unstigmatized; baseline low TS; full Church penetration; the "default" cultural position.
- **Central Einhir** (Valorsmark core, Hafenmark lowlands): unstigmatized; central cultural position.
- **Southern Einhir** (Southernmost-adjacent territories: T4 Grauwald, T6 Stillhelm, T13 Oastad; also distributed populations in the western fjords per Maret Uln's background): stigmatized; higher baseline TS; lower Church penetration; structurally excluded from post-war settlement. This is the caste that is economically-suppressed, culturally-pressured, and ethnically-targeted by Church enforcement.

The player character selects a caste background at character creation. The choice interacts with every faction ladder as specified below.

## §3.2 Caste × Rank Advancement

| Faction/Ladder | Northern Einhir | Central Einhir | Southern Einhir |
|----------------|-----------------|----------------|-----------------|
| **Crown** | Full access; Std 0→7 normal progression | Full access; Std 0→7 normal | **Gated:** Std 0→3 possible without modifiers; Std 3→4 requires Public Deed that mitigates caste (Exceeding-level, publicly witnessed); Std 5→6 requires Extraordinary Circumstances (a named inner-circle NPC sponsors despite caste — burns ~3 Disposition with a rival inner-circle NPC); Std 7 effectively closed unless bloodline-extinction or deed-claim conditions force acceptance |
| **Hafenmark** | Full access | Full access | **Moderate gate:** Std 0→2 fully open; Std 2→3 (Alderman council vote) requires +1 Ob on procedural grounds (Heljason can mitigate if Disposition ≥ +2); Std 4+ effectively caste-neutral once council confirmation achieved — Hafenmark's CI framework applies caste-neutral procedure once the procedural hurdle is cleared |
| **Varfell** | Full access | Full access | **Favored:** Std 0→2 identical; Std 3+ *preferential* if aligned with Maret Uln faction (Southern Einhir solidarity); Skald-Chief endorsement more easily obtained; Warden branch functionally open (highest TS in Southern Einhir populations) |
| **Church** | Full access in all branches | Full access in all branches | **Strongly gated:** Catechumen and Lay Confessor accessible but suspicious; Deacon requires unusual circumstances (Cardinal or Confessor personal sponsorship); Canon+ structurally difficult — a Southern Einhir Canon is a scandal. Exception: Temperance branch (Klapp) is caste-neutral in practice (Klapp's scholarly focus transcends caste politics). Inquisitor and Templar branches are structurally closed to Southern Einhir without extraordinary circumstances. |
| **Löwenritter** | Full access | Full access | **Moderate gate:** Squire and Knight accessible; Std 3 (Knight-Commander) requires Grand Master endorsement that Ehrenwall historically withholds from Southern Einhir |
| **Riskbreakers** | Full access | Full access | **Actually favored:** Southern Einhir's outsider status is a *covert asset* — Riskbreakers specifically recruit Southern Einhir because they can operate in Southern territories without triggering surveillance. |
| **Inquisitors** | Full access | Full access | Effectively closed (see Church above) |
| **Templars** | Full access | Full access | Effectively closed |
| **Guilds** | Full access | Full access | **Variable gate:** Apprentice and Journeyman accessible; Free Master's Examination bias against Southern Einhir (+1 Ob on procedural grounds, historically — Feldhaus's AI protects Guild caste profits); Guild Master typically closed except in marginal trades; Comptroller effectively closed. |
| **Niflhel** | Full access | Full access | **Favored:** Niflhel is caste-blind by necessity — the Dockworkers' waterfront operations and the Burned's covert identities both require Southern Einhir members. |
| **Warden of the Thread** | **Gated:** lower baseline TS makes the initiation threshold harder to reach | Slightly lower baseline | **Favored:** higher baseline TS; cultural familiarity; Edeyja's Warden network is structurally Southern Einhir-aligned |
| **Restoration Movement (when active)** | **Ideologically suspect** | Variable | **Ideologically favored** — the RM's base is Southern Einhir |

## §3.3 Caste as Renown Modifier

The Renown track (player_agency_v30 §5.4) acquires a caste-sensitivity layer:
- **Northern Einhir:** standard Renown rates.
- **Central Einhir:** standard rates.
- **Southern Einhir:** Renown gains from *public* actions in Northern/Central Einhir territories are halved (round down). Renown gains in Southern territories (T4, T6, T13, southern fjords) are standard. Renown gains from *covert* actions are unaffected (Shadow Renown is caste-independent — REN-03).

This encodes Gerik Strand's observation (npc_roster §14 #9): the system's incentives align against Southern Einhir advancement through visible public deed, driving them toward covert or alternative paths (Warden, Niflhel, RM).

## §3.4 Caste as Initiation Duty Modifier

Every Initiation Duty (Std 0→1) has a caste variant. The Duty objective is the same; the Ob and obstacles differ:

| Faction | Initiation Duty | Northern/Central Ob | Southern Einhir Ob | Southern modification |
|---------|-----------------|---------------------|-------------------|---------------------|
| Crown | Carry the King's Word | Ob 2 (standard fieldwork) | Ob 3 | Additional Exposure risk: the message-carrier is suspected of being an Einhir sympathizer |
| Hafenmark | File the Petition | Ob 2 | Ob 3 | Additional procedural hurdle: a Senior Advocate may object to the petition on grounds of Advocate qualification |
| Varfell | Answer the Muster | Ob 2 | Ob 2 (unchanged, possibly Ob 1 with Southern Einhir cultural kinship to a Jarl) | None negative; possibly favorable |
| Church | Witness the Solmund Codex | Ob 2 | Ob 3 | Additional theological scrutiny; presence of an Inquisitor observer likely |
| Löwenritter | First engagement | Ob 2 | Ob 2 (combat-neutral); advancement Ob later | No Initiation Duty modification; caste barriers arise at advancement |
| Guilds | Journeymen Years | Ob 2 | Ob 3 | Additional guild-gatekeeping at each territory transition |

## §3.5 Caste as Inner Circle Disposition Floor

Inner-circle NPCs (per §1 of each faction's ladder) begin with Dispositions toward the player reflecting caste. Default starting Dispositions (before any play) for Southern Einhir player characters:

| NPC | Faction | Default Disposition (Southern Einhir PC) |
|-----|---------|------------------------------------------|
| Almud | Crown | −1 |
| Voss (Royal Marshal) | Crown | −1 |
| Reichard (Lord Treasurer) | Crown | −1 |
| Thale (Spymaster) | Crown | 0 (caste-sympathetic due to own rumored heritage) |
| Linder (Archbishop's Rep) | Crown | −2 (doubly — Church structure + Crown-Church Archbishop role) |
| Kreutz (Royal Guard Captain) | Crown | −1 |
| Baralta | Hafenmark | 0 (CI framework ostensibly caste-neutral; institutional bias manifests procedurally, not personally) |
| Almstedt | Hafenmark | 0 (procedurally neutral, but deed-monarchy memory includes caste) |
| Feldhaus | Hafenmark/Guilds | −1 (structural caste-profit incentive) |
| Heljason | Hafenmark | 0 |
| Geirson | Hafenmark | 0 |
| Vaynard | Varfell | 0 (pragmatic) |
| Maret Uln | Varfell | +1 (solidarity) |
| Hann | Varfell | 0 |
| Torben (Sr Jarl West) | Varfell | 0 |
| Ehrenwall (Skald) | Varfell | 0 |
| Himlensendt | Church | −1 |
| Jarnstal (Cardinal Fort.) | Church | −1 (institutional) |
| Olafsson (Cardinal Justice) | Church | −2 (Inquisitorial alignment) |
| Tormann (Cardinal Prudence) | Church | −1 (extraction-benefit) |
| Klapp (Cardinal Temperance) | Church | 0 (scholar, caste-transcendent) |
| Edeyja | Warden | +1 |

Central Einhir start all values +1 from the Southern column; Northern Einhir start all values +2 (effectively standard-neutral or better).

## §3.6 Caste as Conviction Scar Risk

A player of any caste who publicly adopts a Conviction that is caste-transgressive (a Northern Einhir adopting Conviction: Community — the RM/Warden foundation, is caste-transgressive; a Southern Einhir adopting Conviction: Order — the Crown foundation, is caste-transgressive in a different way) faces an elevated Conviction Scar risk per npc_behavior_v30 §3.2. Scar risk increases the chance that a caste-transgressive Conviction cannot be completed without irreversible personal cost.

This is the mechanism by which Gerik Strand's "ideological ally" potential (npc_roster §14 #9) is expressed: Strand is Northern Einhir by background but adopts a Conviction that aligns with Southern Einhir or RM politics. The transgression is the source of his drama.

---

# PART 4 — TERMINOLOGY AND NAMING RECONCILIATION

## §4.1 Solmund Naming Violation — IMMEDIATE FIX REQUIRED

**Finding:** `designs/conviction_track/conviction_track_v30.md` line 16 states:

> "Poles: 0 = Einhir Restoration pole. 5 = Galbadian Orthodoxy pole."

**Violation:** Use of "Galbadian" violates the project naming rule ("Always Solmund, never Galbados").

**Fix applied (2026-04-17):** Replaced "Galbadian Orthodoxy" with "Solmund Orthodoxy" at conviction_track_v30.md line 16 as part of this propagation commit.

**Scope of remaining propagation:** Grep all designs/, references/, canon/ for "Galbadian" and "Galbados" and replace with Solmund equivalents where present. Known downstream references to check:
- conviction_track_v30 §1 (the line fixed in this commit, plus §5.1 Warden's Accord discussion)
- tc_political_redesign_v30 §§3.1, 3.2 (historical precedent discussion — uses "papal" language metaphorically; no direct violation, but confirm)
- Any CV/PT documentation that cites the poles

**Editorial item:** ED-643 (P1 APPLIED at line 16 — propagation-pending for any other occurrences).

## §4.2 CV / PT / SW Terminology Dissolution

**Finding:** Three separate terms are in simultaneous use for closely related per-territory stats:
- **Conviction (CV)** — conviction_track_v30 §1. Range 0–5. Changes seasonally. 0 = Einhir Restoration; 5 = Solmund Orthodoxy (corrected).
- **Piety Track (PT)** — tc_political_redesign_v30 §§1, 2.1. Treated as identical to CV in mechanical effect (Seizure Ob uses "max(0, 3 − PT)", identical to Seizure Ob in conviction_track_v30 §2.1).
- **Spiritual Weight (SW)** — tc_political_redesign_v30 §1. Range 0–5. Fixed (not dynamic). Weights PT yield and political pools. Not the same stat as CV/PT — this is a separate dimension.

**Assessment:** CV and PT are the same stat under two names. SW is a different stat that modifies CV/PT yield. Not a terminology conflict between SW and CV/PT — only between CV and PT.

**Reconciliation Decision (approved 2026-04-17):**

1. **CV and PT are the same stat under two names.** SW is a distinct fixed attribute. No terminology conflict between SW and CV/PT — only between CV and PT.

2. **Full rename deferred.** A complete rename (CV → PT, file rename `conviction_track_v30.md` → `piety_track_v30.md`, propagation across 489 lines of skeleton + 6,095 char infill + 40,000+ char propagation_map + canonical_sources.yaml + file_index) is a P2 cost-benefit decision that should be done in a dedicated cleanup pass, not bundled with this rank-ladder register.

3. **This register uses PT terminology** in all downstream mechanical discussion (Church rank ladder, TC × rank integration, caste layer). `conviction_track_v30.md` has been annotated with an equivalence note at §1 stating that CV ≡ PT mechanically and that PT is the preferred name in newer design docs.

4. **Retain SW as separate** (distinct fixed per-territory attribute).

5. **Retain Warden's Accord (WA)** as is — WA is a separate relationship track.

**New editorial item:** ED-644 (P1 DOCUMENTED — rename deferred) — CV ≡ PT equivalence documented in conviction_track_v30 §1; full rename queued for future cleanup pass.

## §4.3 T15 Name Reconciliation (Southernmost vs. Askeheim)

**Finding:** `conviction_track_v30.md §1.1` (line 39) refers to T15 as "Southernmost (Uncontrolled)". `tc_political_redesign_v30.md §1` (line 54) refers to T15 as "Askeheim". These are the same territory under two names.

**Assessment:** "Southernmost" is the geographic/directional name (used in Path B & C discussion and in setting_geography_v30 as the primary term). "Askeheim" appears to be a newer cultural/proper-noun name (perhaps Varfell linguistic? Altonian? Einhir?).

**Not resolved in this register.** This is flagged as:

**New editorial item:** ED-645 (P2) — T15 name reconciliation. Check geography_v30 for canonical choice. Recommend: use "Southernmost" for directional references and "Askeheim" for proper-name references; confirm which is canonical on the territory card.

## §4.4 Varfell vs. Valoria-Peninsula Naming

**Finding:** `worldbuilding_v30 §9.1` (the territory mapping table) has a collision between "Lore" names and "PP-199 map" names. E.g., T1 lore maps to "Varfell city" (Varfell duchy) while T1 on the map is Valorsplatz (Crown duchy). This appears to be a legacy of pre-v30 territory renumbering.

**Not resolved in this register.** Flagged as:

**New editorial item:** ED-646 (P2) — Cross-reference worldbuilding_v30 §9.1 lore-to-PP-199 mapping against the current canonical geography; confirm no NPC/rank/faction assignments are currently attached to stale names.

---

# PART 5 — TC × RANK LADDER INTEGRATION

The TC political legitimacy system (tc_political_redesign_v30 §3) grants Church floor(TC/20) bonus dice in political forums and imposes floor(TC/30) penalty on opposing factions. This interaction was not reflected in the original rank ladder. Per Finding A-07, a Prelate at TC 28 and a Prelate at TC 90 should have structurally different institutional positions.

## §5.1 Church Rank × TC (Primary integration)

The Church's expanded rank ladder (§1.4) acquires TC-dependent effects at Standing 3 and above:

| Church Standing | TC 0–39 effect | TC 40–64 effect (post-Assertive milestone) | TC 65–99 effect (post-Prominent/Dominant) | TC 100 effect (Unification) |
|-----------------|----------------|-------------------------------------------|------------------------------------------|-----------------------------|
| 3 Canon | Standard obligations | +1D Interview in Church territories (institutional weight rising) | +1D Interview in all territories (Church is institutionally dominant) | Canon authority extends to any territory regardless of faction control |
| 4 Bishop's Delegate | Standard | Ecclesiastical trials may be held in any territory where Church presence exists (not just Church-controlled); +1D Heresy Proceedings | Heresy Proceedings permitted against Standing 5+ rivals (normally restricted to 4-) | Bishop's Delegate may deputize Inquisitors for Unification Seizure support |
| 5 Prelate | Standard | +1D on all social contests at ceremonial scenes where Church has presence | +2D; Crown Treaty defenses targeting Church pay double-penalty | Prelate may speak with Confessor-equivalent authority for ceremonial purposes |
| 6 Cardinal | Standard for branch | +1D on Cardinal Independence Checks (resists Confessor countermanding) | +1D; arm-specific modifier (see §5.2) | Cardinal retains full arm authority even if the Confessor is contested |
| 7 Confessor-Presumptive | Standard | Named Character Event Cards for the Presumptive's arm fire at reduced cost | TC political legitimacy fully transfers to Presumptive during Confessor absence | Unification operations centered on Presumptive |

## §5.2 Arm-Specific TC Modifiers

At TC 55+ (Prominent milestone) each Cardinal Arm acquires a specialty TC-scaled benefit:

| Cardinal | TC 55+ modifier | TC 80+ modifier |
|----------|-----------------|-----------------|
| Jarnstal (Fortitude) | Templars may defend in non-Church territories without immunity forfeit | Templars may conduct offensive operations against explicitly-named heretical forces (expansion from OFC-04's strict defensive-only rule) |
| Olafsson (Justice) | Inquisitors may initiate proceedings against Standing 5 targets with Cardinal authorization | Inquisitors may initiate against Standing 6 targets (Parliament-level intervention becomes formally possible) |
| Prudence | Church charities may be imposed on territories where Prosperity ≤ 3 regardless of faction consent | Church may collect tithes directly from non-Church-controlled territories in ecclesiastical emergency |
| Klapp (Temperance) | Access to all institutional archives across factions, Church-sanctioned (rival factions +1 Ob to refuse) | Church may dictate doctrinal content of university curricula in all territories |

## §5.3 Non-Church Rank × TC (Secondary integration)

Non-Church factions experience TC as pressure on ranks that interact with the Church:

| Rank intersection | TC 40+ effect | TC 65+ effect | TC 100 effect |
|-------------------|--------------|----------------|----------------|
| Crown Prince (Std 6) / Crown Regent (Std 7) | Must consult Archbishop's Representative on TC-affecting decisions; inner-circle Disposition penalty for ignoring Linder | Linder's Disposition weight on inner-circle majority counts double | Linder may effectively veto Crown Regent actions with TC implications |
| Hafenmark Chancellor (Std 6) / Speaker-Regent (Std 7) | Baralta's Sovereign Authority Doctrine availability (unchanged, but more frequently needed) | Parliamentary floor(TC/30) penalty reaches −2; coalition maintenance harder | −3 penalty; Hafenmark effectively cannot pass any motion opposing Church without Extraordinary Parliamentary Manoeuvre |
| Varfell Senior Jarl (Std 6) / Jarl-Regent (Std 7) | No direct effect (Varfell operates outside Church institutional reach) | Skald-Chief's Cultural Reclamation actions +1 Ob (Church suppression visible at regional scale) | Vaynard's Thread operations increasingly constrained by Church scrutiny; Private Collection use generates Church Attention Pool +1 per use |

## §5.4 TC Milestones as Recognition-Event Modifiers

The Formal Recognition Events (§1.x Standing 3 — Banneret/Alderman/Lendmann/Canon) acquire TC dependencies:

- At TC 40+ (Church Assertive milestone), Crown Banneret and Hafenmark Alderman Recognition Events require Archbishop's Representative (Linder) concurrence (one-line approval scene, +1 Ob if opposed by Linder).
- At TC 65+ (Church Dominant), all non-Church Recognition Events require formal Church consultation (an Audience scene with a Cardinal). This is a structural Skyrim-parallel: as one faction dominates, the others must pay reputation cost to advance their own members — reflecting historical papal-approval dynamics.

---

# PART 6 — BARALTA CROWN CLAIM × RANK LADDER INTERACTION

The Baralta Crown Claim (baralta_crown_claim_v30) mechanic triggers Crown Succession Contest, Consecration Crisis, and potentially Hafenmark dissolution/persistence. This Part specifies how each outcome interacts with the expanded rank ladders.

## §6.1 Outcome A — Hafenmark Wins Succession Contest

**If Baralta takes Crown** (baralta_crown_claim_v30 §2):

### Rank-Ladder Cascades

**On Hafenmark:** Per Option B (ED-411), Hafenmark persists as NPC-controlled faction; Baralta's PP-487 succession mechanic fires for Hafenmark.

- **Hafenmark Standing 7 (Speaker-Regent) becomes Hafenmark Leadership candidate automatically.** If the player holds Hafenmark Std 7, they become eligible for Hafenmark Leadership — but at reduced scope (the new Hafenmark is a PI-gated institutional successor state, not the full pre-Baralta Hafenmark). The player's Std 7 rank transfers, but the faction they now lead has different stats (Mandate ≈ PI/2, Stability reduced).
- **Hafenmark Standing 5–6 (Chair, Chancellor) retain their ranks in the successor Hafenmark.** However: if Parliament fails to confirm the institutional successor (PP-487 PI < 4 condition), the faction fractures and all Hafenmark ranks become **dormant** (the factional structure no longer supports the rank). Dormant ranks are recoverable *if* a Rump Faction (original COUP-02) forms under one of the rank-holders.

**On Crown:** Baralta's inner circle composition conflicts with the existing Crown inner circle.

- Baralta becomes new Crown leader.
- The Crown inner circle (Voss, Reichard, Thale, Linder, Kreutz) remains in place institutionally, but each NPC re-evaluates loyalty. Default: Voss (Order) and Reichard (Precedent) accept with reluctance (+0 Disposition for non-deed-claim Crown leader = institutional duty binds); Thale (Autonomy) accepts pragmatically (+1); Linder (Faith) disposition drops based on Consecration outcome (see §6.2); Kreutz's (Order) disposition depends on Löwenritter coup posture.
- **Player Crown ranks are not automatically affected.** A player at Crown Std 5 (Seneschal) under Almud remains Seneschal under Baralta *if* the player's Disposition with Baralta is ≥ 0. If negative, the player is demoted to Std 3 (Banneret) within 1 season — Baralta does not retain senior officers loyal to the prior regime without personal affiliation.
- **Hafenmark ranks do NOT transfer to Crown ranks.** A Hafenmark Chancellor who held Hafenmark Std 6 does not automatically become Crown Std 6. They hold their Hafenmark rank (in the institutional-successor Hafenmark) and must earn Crown rank separately. An exception: if the player was Hafenmark Std 7 (Speaker-Regent) *and* had completed the Hafenmark-to-Crown Recognition ceremony (new mechanic — see §6.3), they carry a provisional Crown Std 5 (Seneschal-equivalent — Baralta's trusted advisor in Crown contexts).

## §6.2 Outcome B — Consecration Crisis

**Per baralta_crown_claim_v30 §3:**

- **Church Stability ≥ 4: Himlensendt Refuses Consecration.** Baralta rules unconsecrated.
  - **Church rank consequences:** Himlensendt's Std 7 (Confessor) position is politically strengthened (he exercised sovereign refusal). All Cardinals' positions hold. However, Linder (Archbishop's Rep at Crown inner circle) is in an impossible position — he cannot serve a Crown that the Confessor refuses to bless. He resigns (Standing → 0 effective; he returns to Church service). New Archbishop's Representative must be nominated by the College of Prelates — Standing 4+ Prelate eligible.
  - **Crown rank consequences:** Crown rank holders in the Martial and Administrative branches proceed as normal. The Church branch (if any — Crown NPCs with Church cross-rank are rare but possible) is constrained. Any Crown rank holder with Conviction Faith is forced to choose between personal faith and Crown loyalty; Conviction Scar risk elevated per npc_behavior §3.
  - **Hafenmark rank consequences:** Hafenmark rank holders in the institutional-successor state see −1 Disposition with the Church ally regardless of prior relationship; the Church's refusal is read as a Hafenmark insult.

- **Church Stability ≤ 3: Himlensendt Consecrates Under Duress.** Baralta takes Crown with full Mandate.
  - **Church rank consequences:** Himlensendt's position is severely weakened. Church Stability drops to 0 (anti-death-spiral floor). Standing 6 Cardinals retain rank but Cardinal Independence Checks become +1 Ob harder (they are viewed as collaborators). The College of Prelates may attempt to depose Himlensendt post-crisis (new scene arc: "The Consecration Aftermath" — requires two Prelates to initiate, College vote Ob 3).
  - **Cardinal Specialty Impact:** Jarnstal (Fortitude) may trigger Jarnstal Independence Card early (his view that Consecration under Duress is unconscionable). Olafsson (Justice) may initiate Heresy Proceedings against Himlensendt (unprecedented — requires 2 Prelates' concurrence). Prudence and Klapp less affected personally.
  - **Crown rank consequences:** Crown ranks proceed normally. Baralta is fully consecrated and inherits full Crown Mandate.
  - **Hafenmark rank consequences:** Institutional-successor Hafenmark begins with advantaged starting conditions (the Consecration victory increases Baralta's political weight).

## §6.3 Outcome C — Hafenmark Loses Contest

**If Löwenritter wins Crown Succession Contest (the original canonical route, PP-494/PP-194/Royal Deposition path):**

- **Löwenritter takes Crown.** The Löwenritter sub-office ladder (§2.1) becomes the Crown primary rank ladder; or a hybrid structure emerges where the Grand Master becomes King and the Löwenritter internal ranks reconfigure.
- **Hafenmark survives unless Baralta was eliminated in the contest.** Baralta alive + Hafenmark-lost-contest means Baralta reverts to pre-contest status with Stability −1 (overreach). The player's Hafenmark ranks are unaffected.
- **Church takes position based on Consecration stance.** If Church refused consecration for Löwenritter-Crown as well, Church Stability consequences apply as in §6.2.

**If Church wins Crown Succession Contest** (the Theocratic Regency path):
- **Theocratic regency forms.** The Church's rank ladder becomes the de facto Crown ladder. Church Standings acquire Crown-equivalent authority (the Cardinals become Ministers; Prelates become Seneschal-equivalent). This is a major institutional reconfiguration.
- **Secular ranks are suspended.** Crown, Hafenmark, and Varfell rank holders are not dismissed but their rank authority is subordinated to ecclesiastical rank authority. The Standing track on primary factions continues; the privileges associated with those Standings are reduced.

## §6.4 The Hafenmark-to-Crown Recognition Ceremony (New Mechanic — ED-647)

If Outcome A fires and the player holds Hafenmark Std 7 at the moment of Baralta's Crown Succession Contest victory, a new scene event fires: the **Hafenmark-to-Crown Recognition Ceremony.**

- **Trigger:** Succession Contest resolves with Hafenmark victory; player at Hafenmark Std 7.
- **Scene:** Formal presentation of the player by Baralta at Valorsplatz, acknowledging their institutional continuity.
- **Mechanical effect:** Player gains Crown Std 5 (Seneschal-equivalent) provisionally. The Crown inner circle evaluates immediately (first of 5 Dispositions): if majority accepts, the rank consolidates to permanent Crown Std 5. If majority rejects, the player's provisional rank falls to Crown Std 2 (Crown Agent equivalent), and their Hafenmark rank reverts to Chancellor (Std 6) in the institutional-successor Hafenmark.

This ceremony resolves the original register's gap — that the register had no mechanical path for a Hafenmark senior officer to transition into Crown service under Baralta.

---

# PART 7 — MINISTRY SYSTEM EXPANSION

The original register specified Ministries for Crown only (MIN-01 through MIN-06). Per Finding A-09, the Church, Hafenmark, and Varfell have equivalent institutional apparatus that need mechanical scaffolding for consistency.

## §7.1 Crown Ministries (Original — confirmed with additions)

The six Ministries remain as specified (Haushalt, Kriegsamt, Kirchenamt, Gerichtsamt, Schattendienst, Markamt). Added:

- **Hochschule** (Ministry of Universities/Knowledge) — proposed new Ministry. Overlaps with Klapp's Temperance dicastery (Church). Manages Crown-sanctioned universities and scholarly credentialing. Seasonal cost 1 Wealth. Competence effect: influences Renown decay mechanic (new) and Knowledge-skill check Ob in Crown territories. Minister TBD. [ED-648]

## §7.2 Hafenmark Parliamentary Committees

The original worldbuilding_v30 §6.1 mentions "Ministries" for the Crown governance structure. But Hafenmark's equivalent is the Parliamentary Committee — a committee is a permanent sub-body of Parliament with defined jurisdiction and staff. Unlike Crown Ministries (executive-branch), Hafenmark Committees are legislative-oversight bodies chaired by Parliamentarians (Std 4+).

### Proposed Committees

| Committee | Jurisdiction | Parliamentary Chair (Std 4+) | Cost |
|-----------|-------------|-----------------------------|------|
| **Supreme Judiciary Committee** | Constitutional interpretation; supervision of Rectorates | Judicial-branch Parliamentarian | 0 (self-funded) |
| **Trade & Guild Relations Committee** | Guild Forum oversight; commercial policy; Guild arbitration (worldbuilding §5.4) | Commercial-branch Parliamentarian; Comptroller ex officio | 1 Wealth/season |
| **Defense Committee** | Hafenmark military (defensive); border garrisons; relations with Löwenritter | Martial-branch Parliamentarian | 1 Wealth |
| **Foreign Affairs Committee** | Crown relations, Varfell relations, Altonian diplomacy | Senior Parliamentarian (typically Std 5+) | 1 Wealth |
| **Constitutional Review Committee** | Statutory codification; constitutional emendation proposals | Almstedt chairs permanently (Senior Parliamentary Chair) | 0 |
| **Internal Affairs Committee** | Civic administration; settlement Order management; Alderman oversight | Junior Parliamentarian (Std 4) | 1 Wealth |

### Competence and Corruption (Parallel to Crown Ministries)

Each Committee has Competence (0–3) and Corruption (0–3) tracks identical to Crown Ministries (MIN-02, MIN-03). Committees are funded from Parliamentary budget; unfunded Committees decay. Unlike Crown Ministries (where the Crown leader allocates), Hafenmark funding allocation is itself a Parliamentary vote — the coalition mechanics apply.

Player positions in Committees parallel Crown Ministry Positions (MIN-04): auditor, secretary, clerk. Access to Committee information is a Burgher-level privilege (Hafenmark Std 2+) and is one of the few ways a Standing 2 player can meaningfully influence national policy.

## §7.3 Church Dicasteries (Sekreta)

The Four-Cardinal structure provides the framework. Each Cardinal Arm manages a Dicastery (Byzantine-style Sekretum). These are executive bodies within the Church.

### Proposed Dicasteries

| Dicastery | Cardinal Arm | Function | Player access via |
|-----------|--------------|---------|-------------------|
| **Dicastery for the Defense of the Faith** | Fortitude (Jarnstal) | Templar deployment; monstrous-incursion response; enforcement | Templar ladder (§2.4) |
| **Dicastery for Doctrinal Adjudication** | Justice (Olafsson) | Inquisition management; Heresy Proceedings | Inquisitor ladder (§2.3) |
| **Dicastery for Temporal Affairs** | Prudence (Aldric Tormann — canonical per npc_roster_v30 §13) | Church wealth; tithe collection; charities; church land | Church Std 3 (Canon) in Prudence branch |
| **Dicastery for Doctrine and Archives** | Temperance (Klapp) | Theological scholarship; archive maintenance; university liaison | Church Std 3 (Canon) in Temperance branch |

Each Dicastery has Competence and Corruption tracks. Dicastery staffing is by Canon, Bishop's Delegate, and Prelate appointment; the Cardinal has chairmanship. A Confessor can rearrange Dicastery jurisdictions (radical act — Stability cost).

Dicastery competence directly interacts with the arm's Named Character Event Cards: low Competence Dicastery for Temporal Affairs makes Prudence Crisis more likely; low Competence Dicastery for Defense makes Jarnstal Independence more likely.

## §7.4 Varfell Jarl Assembly Councils

The Jarl Assembly (per §1.3 of this register, plus factions_ttrpg_v30 §8.5) has five standing Councils as the equivalent of Ministries. Each is chaired by a Senior Jarl (Std 6).

### Councils

| Council | Jurisdiction | Senior Jarl Chair |
|---------|-------------|-------------------|
| **Council of the March** | Eastern military frontier; Altonian invasion preparation | Thorvald Hann (canonical-proposed, §1.3c) |
| **Council of the Highlands** | Western resource territories; timber, metals, trade routes | Björn Holdar (proposed, resolved from initial "Björn Torben") |
| **Council of the Skald** | Cultural memory; Einhir oral tradition; lawspeaking | Ingrid Stenskald (proposed, Skald-Chief; resolved from initial "Ingrid Ehrenwall") |
| **Council of the Warden** | Thread-related matters (Path B context); Warden liaison (PP-663: Path C struck; VTM term dropped) | Maret Uln (proposed dual role) OR Edeyja when serving |
| **Council of Voices** | Diplomacy; Crown and Hafenmark relations; Schoenland border | Vaynard's Huscarl Captain (role function) |

Unlike Crown Ministries or Hafenmark Committees, the Councils are not permanently funded entities — they convene on need, often at the Jarl Assembly's annual meeting, and delegate to individual Jarls for implementation. There is no Seasonal Cost; instead, each Council has a **Readiness Track** (0–3) that declines without session and increases when the Council acts.

- Readiness 0: Council effectively inoperative; any matter in its jurisdiction defaults to Vaynard's personal decision.
- Readiness 3: Council fully operational; chair may authorize action in its jurisdiction without Vaynard's approval.

This reflects Varfell's confederate structure — institutional capacity is distributed, not centralized, and only coheres when the Assembly chooses to act.

---

# PART 8 — GENERATIONAL SHIFT FIX

Per Finding A-10, the "10 years game-time" specification for Torben's maturation (LIN-02 Condition B) is unreachable within typical campaign pacing (~S14–S20).

## §8.1 Revised Specification

**Replace:** "he matures after 10 years game-time" (original LIN-02 Condition B).

**With:** Torben's maturation is a **Generational Trigger Event** that fires on the first of the following conditions to be met:

1. **Campaign Elapsed Seasons ≥ 24** (6 year-arcs; reachable by S24 or later — extended campaigns only). This is the "literal age" path.
2. **Accumulated Generational Readiness ≥ 5.** Readiness accumulates through Torben-specific Duties completed (Protection Duties +1, Tutoring/Mentoring scenes +1, successful Crown stabilizing actions with Torben witnessing +1). Max +2 Readiness per year-arc. This is the "precocious maturation" path — Torben matures faster if the Crown has actively trained him.
3. **Crown Stability ≤ 1** fires mandatory Generational Trigger regardless of other conditions — the heir must step up in emergency. This is the "crisis maturation" path.
4. **Almud's death** fires Generational Trigger immediately — Torben may be a child but the institutional requirements overtake his personal readiness.

## §8.2 Disposition-Dependent Outcomes

At Generational Trigger, Torben's accumulated Disposition toward the player determines the outcome. Original register specifies three outcomes (ally/managed/adversary); expand to five:

| Disposition at Trigger | Outcome | Mechanical effect |
|-----------------------|---------|-------------------|
| +3 or higher | **Loyal Heir** | Torben formally renounces claim in favor of the player if the player is non-dynastic; or supports the player's regency indefinitely if Torben is still too young for full authority. Stability +1 on succession events. |
| +1 to +2 | **Cooperative Heir** | Torben supports the player as regent until he reaches full age (additional readiness accumulation required); renunciation possible but not automatic. Stability −0 on succession. |
| 0 | **Neutral Heir** | Torben asserts his claim independently; willing to coexist with the player as a rival but not necessarily hostile. Stability −1 on succession. |
| −1 to −2 | **Wary Heir** | Torben pursues his own claim actively; builds inner-circle support to displace the player. Player's Crown Std 6+ is under active challenge. Stability −2. |
| −3 or lower | **Hostile Heir** | Torben becomes a Rival candidate with full Rival Standing track (SUC-02 mechanic). Active contested succession. Stability −3. |

## §8.3 Torben's Readiness Track (new — paralleling player Standing)

Torben has an internal Readiness Track (0–10) tracked separately from his Disposition toward the player. Readiness measures Torben's personal preparation to rule. At Readiness ≥ 7, Torben exits "ward" status and becomes a fully active political actor with his own Duty cycle (treated as an NPC at Crown Std 5+).

**Readiness interaction with rank:** If Torben reaches Readiness 7 while the player holds Crown Std 7 (Regent-Designate), the player's rank is challenged. Torben formally asserts his claim. If Torben's Disposition to the player is ≥ +2, the player may remain as co-regent or advisor (preserving Std 7); otherwise, Std 7 is contested and must be resolved via SUC-03.

---

# PART 9 — CROSS-FACTION RANK PARITY

Per Finding A-11 and BALANCE-POL-01, the expanded rank ladders must be cross-faction balanced. The **same Standing number** should grant roughly equivalent mechanical weight across factions, while offering distinct flavor.

## §9.1 Parity Table (By Standing)

| Std | Crown (Kronleutnant / etc.) | Hafenmark | Varfell | Church | Löwenritter | Guild | Warden |
|-----|------------------------------|-----------|---------|--------|-------------|-------|--------|
| 0 | Petitioner | Petitioner | Stranger | Catechumen | Squire | Apprentice | Thread-Touched |
| 1 | Retainer | Advocate | Huscarl | Lay Confessor | Knight | Journeyman | Apprentice-Warden |
| 2 | Crown Agent | Burgher | Thane | Deacon | Knight-Sergeant | Free Master | Warden |
| 3 | Banneret | Alderman | Lendmann | Canon | Knight-Commander | Guild Master | Senior Warden |
| 4 | Lieutenant | Parliamentarian | Hersir | Bishop's Delegate | Preceptor | Senior Guild Master | Warden-Captain |
| 5 | Seneschal | Chair | Jarl | Prelate | Marshal | Comptroller | Warden-Senior |
| 6 | Prince | Chancellor | Senior Jarl | Cardinal | Grand Master-Designate | (collective — effectively omitted) | Warden-Chief Designate |
| 7 | Regent-Designate | Speaker-Regent | Jarl-Regent | Confessor-Presumptive | Grand Master | (omitted) | Warden-Chief |

## §9.2 Parity Audit — Mechanical Equivalence

Cross-faction mechanical weights at each Standing:

| Std | Scene Action bonus | Delegation capability | Political pool access | Hall tier | Typical Disposition floor |
|-----|---------------------|----------------------|---------------------|----------|-------------------------|
| 0 | 0 | None | None | None | 0 |
| 1 | 0 | None | Public gallery access | Shared quarters | +1 with one sponsor |
| 2 | 0 | 1 Task/season (informal) | Information-query access | Shared quarters | +1 with faction peer |
| 3 | +0; access to free specialty action | 1 NPC officer delegation | Council/committee observation | Private chamber | +1 with direct mentor |
| 4 | +1 | 2 NPC officers | Voting-member access | Private apartment | +2 with mentor; inner-circle proximity |
| 5 | +1 | Multi-officer; major Domain Action authority | Treaty-level standing | Suite | Inner circle majority +1 |
| 6 | +2 | Inner circle coordination | Council voting; Cabinet-equivalent | Wing / Tower / Palace | Inner circle unanimous ≥ 0 |
| 7 | +2; succession-eligible | Regent-equivalent authority | Leadership-equivalent in absence of leader | Residence in leader's precinct | Leader concurrence + inner circle majority |

Cross-faction variance: Varfell Std 5 (Jarl) is structurally more independent than Crown Std 5 (Seneschal) — a Jarl commands a province with genuine autonomy, whereas a Seneschal operates under Crown hierarchy. The variance is a *flavor* difference, not a mechanical-weight difference. Both grant equivalent scene-action bonus, delegation, and political pool access.

## §9.3 Parity Enforcement

Any new rank added to any ladder must pass a parity check:

1. Does the rank grant benefits at the same mechanical weight as the parity row?
2. Does the rank impose comparable obligations?
3. Is the Disposition requirement consistent?
4. Does the livery/hall tier match?

Deviations from parity must be explicitly justified in the rank's specification. Default assumption: cross-faction rank-at-same-Standing is equivalent.

---

# PART 10 — RESOLUTION OF EDITORIAL ITEMS

## §10.1 Original ED-POL-01 through ED-POL-14 Dispositions

| Original ED | Description | Resolution in this register |
|-------------|-------------|----------------------------|
| ED-POL-01 | Name inner circle NPCs | **Resolved (partial)** — Crown inner circle named (§1.1d); Hafenmark named (§1.2c); Varfell named (§1.3c). Church inner circle is the College of Prelates; 3 of 5 Prelates are canonical (Jarnstal, Olafsson, Klapp); 2 need naming (ED-649). |
| ED-POL-02 | Succession rivals with Stance Triangles | **Partial.** Torben's Triangle specified (§1.1d). Crown Cadet Claimant, Varfell Vaynard-protégé, Hafenmark alternative candidates still require naming — new ED-650. |
| ED-POL-03 | Torben generational clock | **Resolved** — Part 8 specification. |
| ED-POL-04 | Renown / Shadow Renown tracking burden | **Proposed resolution**: Shadow Renown tracked on companion app as separate subfield of Renown track; does not create additional burden. Confirm with companion_specification_v30. |
| ED-POL-05 | Ministry NPCs Stance Triangles | **Partial** — Schattendienst named (Thale); Markamt minister still needs explicit Triangle specification. Added to ED-651. |
| ED-POL-06 | Ministry competence decay sim | **Not resolved.** Pending SIM-DEBT. |
| ED-POL-07 | Figurehead Status mat format | **Flagged.** UI/UX decision; not this register's scope. |
| ED-POL-08 | Rank-advancement Recognition as Zoom In trigger | **Resolved** — Part 1's formal Recognition Events are mandatory Zoom In (FAC-02 retained). Zoom In trigger list requires update. |
| ED-POL-09 | Coup classification exclusivity | **Resolved in principle** — types can combine (a Palace Coup can trigger a Constitutional Crisis response). Specific mechanics deferred to faction_layer_v30 update. |
| ED-POL-10 | Ceremonial Scene category | **Resolved** — new Scene Slate entry category (per REN-02 + this register's ceremony framework). Update Scene Slate generation algorithm. |
| ED-POL-11 | Patronage vs. Knot distinction | **Maintained.** Patronage is political/institutional; Knot is spiritual/personal. Use in separate contexts; do not conflate. |
| ED-POL-12 | Availability State tracking | **Proposed resolution**: Scene Slate generator maintains Availability State as a companion-app-visible field per NPC. |
| ED-POL-13 | Legitimacy Token damage calibration | **Pending SIM-DEBT.** |
| ED-POL-14 | Templar ecclesiastical immunity enforcement | **Partial.** Enforcement mechanics specified (Church Attention Pool +1 per violation, Mandate cost). Fully defined outcomes pending simulation. |
| BALANCE-POL-01 | Cross-faction rank parity | **Resolved** — Part 9 parity table. |
| BALANCE-POL-02 | Ministry funding competition calibration | **Pending SIM-DEBT.** Simulation needed. |

## §10.2 New Editorial Items Raised

| New ED | Description | Priority |
|--------|-------------|----------|
| ED-634 | Crown inner circle name formalization (Voss, Reichard, Thale, Linder, Kreutz) — confirm names and Stance Triangles | P1 |
| ED-635 | Hafenmark Baralta's Legal Advisor: **Torvi Heljason** — confirm name and Triangle | P1 |
| ED-636 | Hafenmark Military Commander: **Olaf Geirson** — confirm name and Triangle | P1 |
| ED-637 | Varfell Senior Jarl of the Western Highlands: **Björn Holdar** (renamed from initial "Björn Torben" to avoid collision with heir Torben Almqvist) — confirm name and Triangle | P1 |
| ED-638 | Varfell Skald-Chief: **Ingrid Stenskald** (renamed from initial "Ingrid Ehrenwall" to avoid collision with canonical Löwenritter Grand Master Ehrenwall) — confirm name and Triangle | P1 |
| ED-639 | Church Cardinal Prudence: canonical name is **Aldric Tormann** (npc_roster_v30 §13). Register has been synced. Propagation: worldbuilding_v30 §3.1 stale entry updated in this commit; ED-NEW-06 closed. | P1 RESOLVED |
| ED-640 | Hafenmark Militia sub-rank ladder specification (equivalent to Löwenritter Knight but Hafenmark-internal; for Martial-branch Hafenmark Parliamentarians) | P2 |
| ED-641 | Warden Conviction formalization as 6th Conviction (alongside Faith/Order/Reason/Equity/Autonomy/Precedent/Continuity/Community — confirm total list and Warden's addition) | P2 |
| ED-642 | Guild Grand Guildmaster rank (Std 6) — confirm whether this rank exists or is omitted per collective-leadership design | P2 |
| ED-643 | **Solmund correction propagation** — conviction_track_v30 line 16 ("Galbadian Orthodoxy" → "Solmund Orthodoxy") applied in this commit. Grep/propagate to any other Galbadian references across designs/, references/, canon/. | P1 APPLIED (line 16) — propagation-pending |
| ED-644 | **CV ≡ PT terminology reconciliation** — Conviction (CV) in conviction_track_v30 and Piety (PT) in tc_political_redesign_v30 are the same per-territory stat. Full rename (CV → PT, file rename conviction_track_v30.md → piety_track_v30.md) is deferred pending cost-benefit review; this register adds an equivalence note to conviction_track_v30 §1 and uses PT terminology downstream. | P1 DOCUMENTED — rename deferred |
| ED-645 | T15 Southernmost / Askeheim reconciliation | P2 |
| ED-646 | worldbuilding_v30 §9.1 lore-to-map mapping audit | P2 |
| ED-647 | Hafenmark-to-Crown Recognition Ceremony (new mechanic) — formalize scene arc and mechanical effects | P2 |
| ED-648 | Crown Ministry of Universities (Hochschule) — proposed new Ministry; confirm inclusion | P2 |
| ED-649 | College of Prelates — 2 additional Prelates need naming (not Cardinal-rank — Standing 5 Prelates who sit on the College without heading an Arm) | P2 |
| ED-650 | Succession rivals need explicit naming and Stance Triangles: Crown Cadet, Varfell Vaynard-protégé, Hafenmark alternative candidate(s) | P2 |
| ED-651 | Markamt Minister — explicit name and Triangle | P2 |
| ED-652 | Rank dismissal (Std 1 → Std 0) — mechanical cost of re-entry; Dishonored flag persistence across campaign; handling in mode-transitions (TTRPG dismissed player cannot simply re-join the same faction without major scene arc) | P2 |
| ED-653 | Inherited Banner Legacy Attribute table (§1.1c); specific entries for Banners associated with deceased former Bannerets | P3 |
| ED-654 | Conviction Scar interaction with caste-transgressive Conviction — formalize the Scar rate modifier | P2 |
| ED-655 | Ministry Position and Committee Position — same mechanic across Crown/Hafenmark/Church/Varfell? Or faction-specific variants? Recommend uniform mechanic with faction-specific titles | P2 |
| ED-656 | Cross-rank advancement interaction: player holds Löwenritter sub-office rank AND Crown primary rank. Confirm Duty conflicts between the two parallel chains are handled via faction AI evaluation (NPC-03 delegation) | P2 |
| ED-657 | Rank restoration after dismissal: what paths exist, and what is the cost? | P2 |
| ED-658 | Warden Ladder integration with Path B victory mechanics (varfell_path_b_v30, PP-663 revised) — Warden rank does not grant automatic Path B progression, but Warden-Chief designation must interact with Path B Deed sequence | P2 |
| SIM-POL-R01 | Simulation: 7-rank progression pacing — validate that a player starting at Std 0 can reasonably reach Std 5 by S14 and Std 7 by S20 under normal play | P1 SIM-DEBT |
| SIM-POL-R02 | Simulation: caste modifier impact — confirm that Southern Einhir rank-advancement gates do not create unwinnable game states | P1 SIM-DEBT |
| SIM-POL-R03 | Simulation: Baralta Crown Claim × rank interaction — confirm the Hafenmark-to-Crown Recognition Ceremony does not create exploit paths for free Crown Std 5 | P2 SIM-DEBT |
| SIM-POL-R04 | Simulation: TC × rank interaction — confirm TC 100 Unification does not trivialize or over-constrain Church rank advancement | P2 SIM-DEBT |
| SIM-POL-R05 | Simulation: Generational Shift Disposition outcomes — confirm five-tier outcome table does not produce degenerate paths | P1 SIM-DEBT |

---

# PART 11 — PROPAGATION MAP

| File | Changes Required |
|------|-----------------|
| player_agency_v30.md | §5.1 rewrite: Standing 0–7 ladder (was 0–5). §5.2 rewrite: Leadership Acquisition at Std 7. §5.3 retained. §5.4 retained with caste modifier note. §6.2 Modifiers: Std 4 +1 action (retained); Std 6/7 +2 action (new). §3.3 Duty Types: expand to include Initiation Duty (new category). §3.4: Duty completion at Std 0 unlocks Std 1 (initial rank). |
| factions_ttrpg_v30.md | §8.2–8.9: add rank-ladder callouts with reference to this register. Do not duplicate ladders; reference. §8.11 Parliamentary Vote: no change but add note that Parliamentarian-rank actors (Std 4+) are the direct participants. |
| faction_layer_v30.md (board_game/) | §Stability Triggers: add rank-specific triggers — dismissal of a Std 4+ Crown officer is itself a Stability event. |
| settlement_layer_v30.md | §7.2 Succession: replace with SUC-01–04 mechanics; add Hall Tier as a settlement-level resource (a Crown-owned Valorsplatz has a Prince's Wing; an adjacent settlement has no Prince's Wing — this is an asset of the capital). |
| npc_behavior_v30.md | §1.2 Convictions: add Continuity (Torben), Community (Solvei/RM), Warden (Edeyja) to canon list if not already present. §3 Conviction Scar: add caste-transgressive modifier. §7 Faction AI priority trees: add Ministry Position consideration (Schattendienst, Markamt) for faction AI. |
| npc_roster_v30.md | §14 Caste Annotations: add subsection for rank-advancement caste gating (reflecting Part 3 of this register). Confirm integration of deprecated caste-annotations file. |
| worldbuilding_v30.md | §3.1 Four-Cardinal: add Cardinal Prudence name confirmation. §6.1 Governance: Committee structure (per §7.2 of this register). |
| **piety_track_v30.md** (renamed from conviction_track_v30.md) | Complete file rename + Solmund propagation + CV→PT rename |
| tc_political_redesign_v30.md | §3.2–3.4: add Church-rank × TC interaction (per §5 of this register). |
| baralta_crown_claim_v30.md | §6 Hafenmark-after-Baralta: explicit reference to the Hafenmark-to-Crown Recognition Ceremony (§6.4 this register). |
| scale_transitions_v30.md | §4.3.2: add Recognition Event to mandatory Zoom In trigger list (8 total now). |
| params_npc.md (when created) | Populate inner-circle and Cardinal NPCs with Stance Triangle specifications per §1.1d, §1.2c, §1.3c, §1.4b of this register. |
| New file: **rank_ladder_v1.md** | Full specification of all rank ladders (Part 1, 2 here) — may be large enough to warrant its own document. Alternative: keep inline in factions_ttrpg_v30 and player_agency_v30. |
| New file: **caste_integration_v1.md** | Part 3 of this register as a canonical doc. |
| New file: **ministry_system_v2.md** | Parts 7.1–7.4 of this register. Supersedes original register's ministry_system_v1. |
| canon/editorial_ledger.yaml | Add ED-634 through ED-658 (20 new items); update ED-POL-01–14 statuses. |
| tests/coverage_matrix.md | Add SIM-POL-R01 through SIM-POL-R05 as simulation debt. |
| canon/patch_register_active.yaml | Add FP-EXP-001 (this register). |

---

## Summary of Changes vs. Original Register

| Area | Original | This expansion |
|------|----------|---------------|
| Rank count per primary faction | 5 (Std 1–5) | 8 (Std 0–7) |
| Skyrim-pattern features | Absent | Explicit (Skyrim Eight per rank) |
| Sub-office ladders | 4 Office Specs, no ranks | 7 full ladders (Löwenritter, Riskbreakers, Inquisitors, Templars, Guilds, Niflhel, Wardens) |
| Caste integration | Absent | Explicit layer (Part 3) |
| TC × rank interaction | Absent | Explicit (Part 5) |
| Baralta Crown Claim × rank | Absent | Explicit (Part 6); new ceremony mechanic |
| Ministry system | Crown-only | Crown + Hafenmark Committees + Church Dicasteries + Varfell Councils |
| Generational shift | "10 years" (unreachable) | Four-trigger mechanic (Part 8) |
| Cross-faction parity | Flagged unresolved | Resolved (Part 9 table) |
| Editorial items | 14 | 14 (retained) + 20 new |
| Terminology issues | None flagged | Solmund propagation + CV→PT rename (Part 4) |
| Simulation debt | 3 items pending | 3 + 5 new (SIM-POL-R01–R05) |

---

*End of expanded register. All proposals flagged for Jordan review. No canon mutations performed; this is a proposal document in /mnt/user-data/outputs/ for downstream approval and propagation.*
