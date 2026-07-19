# Part 40 — NPC Roster / Officer / Advancement System

> **Status: PROPOSED / provisional.** This part integrates the rise-to-influence research pass
> (`designs/audit/2026-07-11-rise-to-power-roster-system-research/rise_to_power_roster_system_research_v1.md`,
> FILED 2026-07-11, lane IN cross-cutting FA/SE/PC/MB). The §3 system-design proposal, the §4
> cross-references, and the §5 rulings are all PROPOSAL-grade and Jordan-vetoable; nothing here is
> ratified canon. It is preserved here in full fidelity as the design source for a follow-up
> authoring pass, layered on the settlement-scale **ambition engine** (`governance_play_redesign_v1.md`
> §3.1–3.4) and the player-facing **Standing ladder** (`faction_politics_v30.md`).

This part specifies the **roster / officer / advancement layer** — the system by which non-player
characters *gain, maintain, and lose standing and consolidate power*, sitting on top of the NPC
ambition engine and the shared Standing ladder. It answers: how does an NPC actually rise to durable
influence, what does that rise cost, and how does it come apart?

---

## 40.1 Framing — the eight general mechanisms

The historical record (Rome, Byzantium, the Islamic empires, China, Japan, Renaissance Italy,
early-modern France/England, the modern bureaucratic and revolutionary states) converges on a
**small, recurring set of power-acquisition mechanisms**, and — critically — **each mechanism carries
its own characteristic downfall shape baked into the same structure that produced the rise.** This
symmetry is the design gift: it maps directly onto Valoria's **Ω-d non-dominance principle** ("every
action pays what it buys").

There are **eight general mechanisms.** Every one of the ~96 historical cases catalogued below is an
instance, hybrid, or edge-case of these:

| # | Mechanism | One-line shape | Characteristic downfall |
|---|---|---|---|
| **M1** | **Patronage chains (clientelism)** | Run obligation in both directions at once — sponsor upward, accumulate clients downward | Collapses **top-down**: when the upward patron falls, the whole client base decays/purges |
| **M2** | **Credentialed merit** | Pass an objective competence gate + a discretionary sponsor gate; the sponsor bond persists | Structurally capped for the un-tutored; reversible by **rewriting the credential criteria** |
| **M3** | **Kinship / marriage alliance** | Marry into (or supply consorts to) the ruling line; power rides the blood-tie, not the office | **Generational flip** or demographic lapse — one bad marriage or Disposition-flip voids decades of setup |
| **M4** | **Court proximity / favoritism** | Informal Royal-Intimacy outperforms formal Standing (the *valido*/favorite) | **Binary, not graduated** — loss of intimacy or the patron's death is total and often violent |
| **M5** | **Bureaucratic chokepoint control** | Sit on the routing path (correspondence, seals, adjudication, access) without holding a vested office | Undone by a **single bypass channel** or by succession (authority-by-proxy has no transferability) |
| **M6** | **Purchased office (venality)** | Buy the rank, or the toll-post athwart it, with Treasury | **No loyalty reserve** — purchased legitimacy evaporates the instant a rival offers what money can't buy |
| **M7** | **Armed retinue / military power-base** | Build a personal, self-loyal force outside the formal ladder | **Coalition purge** or **subordinate-flip** — the ruler routes *around* the strength rather than matching it |
| **M8** | **Ideological / moral authority** | Accumulate Standing-independent legitimacy (prophetic, jurisprudential, credentialing-body) | Cannot be bought or demoted — only **outcompeted in its own currency**, or purged by covert violence |

Two cross-cutting truths run through all eight:

1. **Power routinely detaches from formal rank.** Michinaga ruled through Minister of the Left, not
   the throne; Cosimo governed Florence holding no permanent office; Heshen stacked unremarkable posts
   into a monopoly. The design consequence: **the advancement system cannot be modeled as "climb the
   Standing ladder" alone** — it needs Standing-independent influence tracks (Disposition-as-Standing,
   `moral_authority`, `renown`, `shadow_standing`, custody-of-Mandate) that *feed* the ladder or
   *substitute* for it.
2. **Consolidation is self-limiting by construction.** Every rise writes a legible vulnerability — a
   Grudge pool, a patron dependency, a bypass channel, a purchased-legitimacy flag, an Upstart tag, a
   "purchased" provenance. This is not a bolt-on; it is the *same field* the rise reads. This is the
   exact shape Valoria wants.

---

## 40.2 The concrete system-design proposal (research §3)

The point of the exercise: six decisions, each with a clear recommendation and reasoning. Preserved
in full below. All recommendations are **PROPOSED**.

### 40.2.1 Relationship to the settlement-scale ambition engine → one engine, two scale-bindings (§3.1)

**Recommendation (PROPOSED): neither a bolt-on replacement nor a literal reuse of the settlement-bound
instance. Adopt the ambition engine's *field grammar* (`goal / method / timeline / progress /
trajectory`, autonomous Accounting-advance + threshold card) as a shared substrate, and instantiate a
distinct court/faction-scale *profile* of it.**

Reasoning:

- **Reuse the grammar, not the instance.** ~40 of the ~96 catalogued entries are explicitly described
  as "extends the settlement-scale ambition engine upward" and map 1:1 onto
  `goal/method/timeline/progress/trajectory` (F5 Sforza is the textbook case: contract → marriage →
  vacancy → seizure with *only a trajectory shift as new logic*). Building a *separate* system would
  violate the ED-1083 §2 anti-shape-divergence rule ("never grow a scale-local interface dialect").
  The card menu, the autonomous tick, the trajectory-replanning branch — all port directly.
- **But decouple the scale-binding.** The settlement instance is "gated on an unbuilt settlement
  registry." The court/faction instance is gated on the **Standing ladder and the Knots graph, both of
  which already exist.** I10 (malikane) makes this precise: the family-scale Entrenchment counter
  "needs only Accounting-cadence ticking plus the existing Knots graph, so it is NOT gated on the
  unbuilt settlement registry the way the base per-NPC ambition engine is." **This is the key unlock:
  the court-scale roster layer can ship without waiting on the settlement registry.**
- **Three scale profiles, one engine.** (i) settlement-local (existing, registry-gated); (ii)
  court/faction (this proposal, ladder-gated); (iii) lineage/clan (a genuine new scope — C5 Wang Mang,
  I10 malikane — that outlives any single NPC's `progress` and is the single biggest structural ask;
  see §40.5). The engine's Accounting-cascade tick runs over all three; only the *entity it ticks on*
  and the *gate it checks* differ.

**Concretely: a shared `ConsolidationEngine` with a `scale_binding` field ∈ {settlement, court,
lineage}.** The settlement binding stays blocked; the court binding is the deliverable; the lineage
binding is Jordan-gated.

### 40.2.2 Interaction with the player-facing Standing ladder → shared rank space + off-ladder auxiliary meters (§3.2)

**Recommendation (PROPOSED): NPCs climb the SAME Standing ladder the player does — shared rank space,
so an NPC and the player can compete for the same seat. The parallel/shadow tracks the research
repeatedly demands (`moral_authority`, `renown`, `shadow_standing`, `service_rank`, Dignity,
custody-bonus) are modeled as EXPLICIT off-ladder auxiliary meters that *feed into or force
ratification onto* the one shared ladder — never as a duplicate ladder.**

Reasoning:

- **The whole research shows rise is contested against incumbents.** Rival Cohort (§1.0), the vacancy
  auctions (F1, I1), the succession contests, the coalition purges — all presuppose NPCs and the
  player compete in one rank space. A parallel NPC-only ladder would make "denounce a rival,"
  "contest a vacancy," and "an NPC out-climbs you for the seat you wanted" incoherent.
- **Avoids parallel-track proliferation, which the corpus has already flagged as a problem.** BYZ-2
  (Purchased Dignity) was *cut* precisely to avoid "a third parallel wealth-shortcut track" (I3), and
  needs_jordan item 3 explicitly asks "how many parallel status/power tracks does the game want." A
  shared ladder + a *bounded, named* set of auxiliary meters is the disciplined answer.
- **The auxiliary meters are real and unavoidable — but they are meters, not ladders.** Power
  routinely detaches from rank (Michinaga/H1, Cosimo/H6, Heshen/H7). The clean model:
  `shadow_standing` (F8), `moral_authority` (J2), `renown` (J6), `service_rank` (F9),
  `mandate.custody_bonus` (F7), sticky `Dignity` (BYZ-1) are **scalar auxiliary scores that (a) can
  *substitute* for Standing in specific gated checks, and (b) can *force ratification* onto the shared
  ladder at a threshold** (Yoritomo's sei-i taishōgun grant, F8). They are not a second seat-space;
  they are pressure on the one seat-space.

**The tradeoff (named):** shared rank space means **an NPC can, in principle, contest — and win — a
seat the player currently holds.** This is the sharpest "every action pays what it buys" stakes
question in the whole design, and it needs a Jordan ruling (see §40.5). The alternative (parallel
track) *avoids* this tension but at the cost of making NPC advancement narratively inert — NPCs would
rise in a sandbox the player never actually competes in, which defeats the purpose. **Recommend:
shared ladder, and treat "can an NPC depose the player at a held rank" as a policy toggle, not an
architectural fork** — the architecture supports it either way; only a `player_seats_are_contestable`
flag differs.

### 40.2.3 NPC sheet extension (§3.3)

Reuse aggressively; flag only genuinely-new fields. The existing NPC sheet already carries
`ambition{goal, method, timeline, progress}`, `trajectory`, `Standing`, `Disposition`, the Stance
Triangle (Conviction / Ethical Framework / Resonant Style), and edges on the relationships/Knots graph
(PP-724). The roster layer adds the following.

**Reused as-is:** `ambition.*`, `trajectory`, `Standing`, `Disposition`, Knots graph,
Ledger-of-Consequence tags (Precedent / Grudge / Debt / Reputation), Mandate.

**New relational edges (on the Knots graph, not new subsystems):**

- `patron_id` + a `bound` flag (E1 Conduit; distinguishes derivative from independent ambition) — with
  edge subtypes: `upward_patron` (A1), `sponsor_bond` (bidirectional, B2), `favor_bond`
  (`revocable_by=ruler_only`, B4), `kul_bond`/`fictive_bond` (A4/E6), `cohort_bond`/`cohort_id`/
  `lineage_id` (B5/A9/J10), `successor_designate` (A5), `web_id` (D5), `shadow_deputy` (G5).
- `clients_sponsored` — aggregate weighted list/count (E8 — the one field that cannot be modeled as an
  ambition variant; the compounding sponsorship base).
- `client.patron_loyalty` **and** `client.crown_loyalty` (two-axis, F6 — the assassination vector).

**New scalar fields (the bounded auxiliary-meter set — deliberately capped per §40.2.2):**

- `power_base` enum ∈ **{patronage, merit, kinship, bureaucratic, military, purchased, ideological}** —
  *the organizing field of the whole system.* It is the single most load-bearing addition: it (a)
  types the climb driver (§40.2.4), (b) types the downfall shape (§40.2.5), and (c) gates whether a
  Dismissal is enforceable (H8 — `favor-dependent` vs `independent`).
- `consolidation_progress` (0–5) + `consolidation_trajectory` — **reuse `ambition.progress`/
  `trajectory` directly**; no new field, just the court-scale binding.
- `standing_source` ∈ {earned, patron-granted, purchased, sponsored} (C4/B6/I-series — provenance for
  the legitimacy/appeal logic).
- `independent_power_base` (raw non-Standing power, G6/G8 — gates coalition-purge and
  scapegoat-transfer).
- `succession_eligible` (bool, C3) / `succession_immune` (bool, G7/BYZ-8) — the "consort-advisor
  ceiling" and its inverse.
- `invested_status` ∈ {invested, uninvested, contested} (J1).
- `access_monopoly` (tier, G1) / `gatekeeper` (bool, A6) — chokepoint control.
- `moral_authority` (0–5, J2) / `renown` (peninsula-scoped aggregate, J6) / `shadow_standing` (0–7,
  F8) / `service_rank` (0–5, F9) — the Standing-substitute meters.
- `office_vested` (bool, E2) / `heritable` + `droit_annuel_due` (I3) — venality/tenure.
- `expected_tenure` (A2) — seat time-boxing.
- `concurrent_roles: []` (H7 — for the plural-advisor stack).

**New Ledger-tag capabilities (extend the family, don't add families where avoidable):**

- `trigger_condition: succession` metadata (G4 — dormant tags that activate on a specific Key).
- a `transfer` operation on Reputation tags (G8 — scapegoat reassignment).
- a `hidden`/`concealed` visibility flag (H7 — embezzlement Debt invisible until an `audit_exposed`
  reveal).
- self-reinforcing "Culpability Debt" chain semantics (G5).
- *Genuinely new families, use sparingly:* lineage-scoped "Kinship Precedent" (C2), "Endogamous Lock"
  (C7). Everything else scopes existing Debt/Grudge/Precedent/Reputation with a `patron_id`/
  `lineage_id`.

**New Key types (all siblings of `standing_change`/`officer_deaths` in `key_type_registry_v30.md`):**
the research proposes many; the *minimum viable set* for the court binding is:

- `npc_standing_climb_attempt` (B1, records sponsor + waiver),
- `patron_succession_transfer` / `state.patron_succession` (A5/F4),
- `state.succession_vacancy` (F1 — the **shared cross-entry vacancy primitive**, reused by F1/F5/I1),
- `access.correspondence_filtered` (H2 — the in-transit-interception primitive, reused by all
  chokepoint entries),
- `coalition_purge` (G6 — the joint-ambition primitive).

The rest layer on later.

### 40.2.4 The core autonomous loop (§3.4)

Mirroring the ambition engine's autonomous-advance-plus-threshold-card pattern, at each **Accounting**:

**1. Advance `consolidation_progress` by a `power_base`-typed driver** (this is the elegance of the
`power_base` field — one loop, seven drivers):

| `power_base` | Driver | Note |
|---|---|---|
| `patronage` | `+f(clientele_breadth, upward_patron Disposition)` (A1) | frozen if the upward patron stalls |
| `merit` | `+1` if the two-stage credential gate + tutoring-investment is cleared (B2) | capped otherwise |
| `kinship` | advances on marriage/betrothal/heir-birth Keys (A8/H1) | pays a recurring rank-independent bonus once the tie holds |
| `bureaucratic` | `+f(Keys successfully filtered/routed)` (E1/H2) | resets to 0 if the patron falls |
| `military` | `+f(retinue.leverage/autonomy, self-financing Keys)` (F1/F6) | spent at a vacancy |
| `purchased` | instant on Treasury spend (I-series) | writes `purchased_legitimacy`/Exposure |
| `ideological` | `+f(aggregate scene.witness/gossip)` feeding `moral_authority`/`renown` (J2/J6) | no ladder entry needed |

**2. At threshold, fire an "Ascendancy card"** (the court-scale rename of the Ambition card) with a
`power_base`-appropriate menu, extending the existing three (**claim office** / **betray patron** /
**expose secret**) with:

- **install successor** (A2),
- **capture the gate** (A3),
- **cohort capture** (A9),
- **convert to asset** (E7),
- **press a banked claim** (C1),
- **force ratification** (F8),
- **purge predecessor** (G5),
- **seize Mandate custody** (F7).

**3. Emit through the Key substrate** (`key_substrate_v30.md` — every state-change is a Key), so the
roster layer is fully legible to faction_layer / npc_behavior / articulation.

**Player-facing verbs/decisions this creates** (the reason the system is *fun*, not just
simulationist):

- **Sponsor a client** — spend Mandate/Access to advance an NPC's climb (buys `clients_sponsored`,
  incurs the top-down-collapse liability).
- **Denounce a rival** — weaponize the Demotion system (H4 — false-accusation risk).
- **Marry into a house** — C-series (banks a contingent claim, C1).
- **Buy an office / buy heritability** — I-series (instant rank, no loyalty reserve).
- **Co-sign or withhold investiture** — J1 (the cross-ladder veto).
- **Expose a chokepoint-holder** — Investigate verb (H7/I2 — the bypass/audit).
- **Reassess an Upstart grant** — D10 (the no-drama succession check).
- **Convene a coalition** — G6 (the only way to touch an over-threshold patron, E8).

### 40.2.5 The downfall / limiting mechanic — Ω-d non-dominance (§3.5)

**Recommendation (PROPOSED): the `power_base` field IS the limiting mechanic.** Consolidation is
self-limiting because *the same field that types the rise types the exploitable vulnerability* — this
is the historical record's gift, and it is exactly Valoria's principle. Concretely, each `power_base`
writes a legible, rival-exploitable liability:

| `power_base` | Rise driver | The bill it pays (legible vulnerability) |
|---|---|---|
| **patronage** | breadth of clients | **top-down collapse** — patron falls → `clientele_breadth` decays / cohort auto-purges (A1, A9, CHN-8) |
| **merit** | credential gate | **criteria rewrite** — a faction flip re-tests you out (B3); wealth-cap if un-tutored |
| **kinship** | blood-tie | **generational flip / demographic lapse** — one Disposition-flip or missed marriage voids decades (A8, C2, C5) |
| **bureaucratic** | routing chokepoint | **single bypass channel** or succession — proxy authority has zero transferability (G1, G4, H7) |
| **military** | personal force | **coalition purge** or **subordinate-flip** — the ruler routes around your strength (F3, F6, G6) |
| **purchased** | Treasury | **no loyalty reserve** — `purchased_legitimacy` suppresses the Coup Counter buffer (I1); prestige-devaluation Grudge (I8) |
| **ideological** | moral authority | **counter-authority in the same currency** — only a rival ruling on the same Renown track, or covert violence (J2, J6, J4) |

The unifying engine primitive underneath all seven: **every consolidation move writes a Ledger tag
(Grudge/Debt/Precedent) that (a) is legible to rivals and (b) makes a rival coalition progressively
*affordable*.** Below a threshold, ordinary Rival Cohort / no-confidence handles the NPC; above it,
only a higher-cost `coalition_purge` (G6/E8) can — which is precisely why real over-mighty subjects
survived until a crisis made the coalition worth its cost. This gives the exact shape Valoria wants:
**power is never dominant; it is *expensive to unwind*, and the cost is paid by whoever waited too
long.**

Two implementation notes:

1. The `independent_power_base` field is the master switch on *whether* a downfall is enforceable at
   all (H8 — a favor-dependent NPC's Dismissal always sticks; an independent one's does not).
2. The vulnerability must be *readable by the player* (via Investigate) — an illegible vulnerability
   isn't a mechanic, it's a coin-flip.

### 40.2.6 Naming — resolve the "officer" collision explicitly (§3.6)

**Recommendation (PROPOSED): name the system the "Ascendancy" layer; name the tracked NPC role a
"Retainer" (bound client) / "Patron" (sponsor) / "Advisor" (chokepoint/court role); and reserve
"officer" exclusively for the mass-battle auto-generated unit commander, with an inline
naming-collision callout carried in the design doc itself (not just the audit).**

Justification:

- **"Officer" is unavailable** — it is owned by `mass_battle_v30.md`/`faction_layer_v30.md`'s
  auto-generated unit-commander, and the `officer_deaths` Key type already means that. The collision
  is real and repeated: **~20 of the ~96 entries flag it** (every military-retinue entry F1–F10, the
  household/consort/prefect entries B4/C3/D2, the bureaucratic entries E3/E8/H7, and — loudest — I7
  British commission-purchase and F10 Yuan Shikai, where the historical subject matter *is* an officer
  corps). A single NPC can legitimately hold *both* a court rank and (separately) a mass-battle officer
  role; the fields must never collide.
- **"Ascendancy" for the system** because it names the *arc* (the consolidation-progress meter), spans
  all eight mechanisms without privileging one (unlike "Court," which excludes settlement brokers /
  military retinues / ideological figures), and has zero corpus collision.
- **"Retainer / Patron / Advisor" for the roles** because these are already the corpus's dominant
  vocabulary — the research overwhelmingly reaches for "patron," "client," "retinue," "household,"
  "advisor," "conduit," "favorite/valido," none of which touch "officer." "Retainer" is the single
  clean replacement for the tempting "officer" (it reads as a bound-to-a-house individual, exactly the
  M7 shape, without any military-command connotation). For the specific sub-roles the research names
  distinctly, keep them: **Conduit** (E, chokepoint-without-office), **Favorite/Valido** (D, per
  HAB-2), **Gatekeeper** (CHN-7, shared primitive), **Sanctioning Prelate** (J5), **Anointed
  Successor** (A2).
- **Carry the callout inline at F10's mechanic definition** (the research's own recommendation) — the
  highest-collision surface deserves a callout at the point of definition, not buried in an audit.

---

## 40.3 The ten research categories, distilled to their concrete mechanics

The full catalogue is ~96 entries across ten categories. Each entry contributes a named mechanic, a
set of new/reused fields and Keys, a characteristic failure dynamic, and (where relevant) a
naming-collision flag. Preserved below at full fidelity — every field name, Key type, and mechanic
name is load-bearing for implementation.

### 40.3.1 Category A — Patronage networks & clientelism (M1 spine)

*Rise via running clientela in both directions; fall from the top down. The strongest argument that
the ambition engine's sponsorship-gate (Standing 0→1) should generalize to every rung.*

| Entry | Mechanic | New fields / Keys | Failure dynamic | Naming |
|---|---|---|---|---|
| **A1** Roman clientela & cursus honorum | **Patronage Web Breadth** — rank climb gated on both directions of clientela: `upward_patron` edge (sponsor gates next-rank Initiation Gate) + derived `clientele_breadth` (weighted count of lower-tier NPCs at Disposition ≥+1 + Debt bond), feeding Rival Cohort tiebreak | `upward_patron` edge; `clientele_breadth` aggregation query (no new storage) | Top-down collapse: if `upward_patron` demoted/dies, advancement freezes, `clientele_breadth` decays; larger-breadth rival wins vacancy tiebreak even vs the player | clean |
| **A2** Cardinal-nephew system | **Anointed Successor** — `ambition.goal='install successor'` for term-limited Standing-6/7 NPCs; sponsors a protégé into a Standing 3–4 slot early, waiving the Initiation Gate at a Reputation cost, timeline pinned to patron's tenure | `expected_tenure` field; Key `patronage_installation`; scoped Debt tag | Each bypass accrues faction-wide "Nepotism debt"; at threshold a **Reform Backlash** card fires a simultaneous Demotion wave on all kin/protégé-tagged seats | **not "officer"; not "cardinal-nephew" (Cardinal = Church Standing-6 title). Use "Anointed Successor"/"Protégé Seat"** |
| **A3** Cosimo de' Medici "robust action" | **Gate Capture** — `ambition.method='capture the gate, not the seat'`; target control of the Initiation Gate / Formal Recognition adjudication (rides FA-JP2 Recognition Fork as shadow-adjudicator). Success measured by `Cross-Faction Reach` | `Cross-Faction Reach` derived stat (distinct faction ladders where NPC holds Disposition ≥+1) | A narrow ideologically-coherent low-Reach rival forces a public Investigate/expose, converting scattered ties into one legible scandal → mass Grudge + multi-faction purge | clean |
| **A4** Köprülü household (kapı) | **Household Roster** — patron gains `household_roster` (protégés sponsored into Standing 1–2 outside credentialing, each with a `kul_bond` scoping tag on their Debt Ledger). One Exceeding-tier Duty success unlocks a one-time `household_succession_grant` (designated member inherits Standing-6+ seat, bypassing Rival Cohort) | `household_roster`; `kul_bond`; `household_succession_grant` | Rival households scale up Rival Cohort for the same 5–7 vacancies; leadership periodically triggers CHN-8 (Institutional Purge, Bloc) against a whole `kul_bond` cohort when Disposition flips | **flag** — a household member also holding mustered-unit command uses mass-battle "officer" for that separate function; political rank must be "household member"/"retinue" |
| **A5** Zeng→Li→Yuan / Huai Army clique | **Successor Designate** — `successor_designate` pointer; on patron death/retirement/demotion an accumulated `parallel_asset_pool` (garrisons, revenue Domain Actions, Treasury ties built outside faction allocation) transfers wholesale to the successor instead of reverting to the institution | `successor_designate`; `parallel_asset_pool`; Key `patron_succession_transfer` | Each hand-off compounds successor power AND raises leadership Suspicion toward the lineage; unchecked, the final successor thresholds into "claim office" → full Succession Contest (Yuan Shikai endgame) | **flag** — mustered-troop commanders in the pool *are* mass-battle officers; inheritance chain is "retinue lineage"/"power-base transfer" |
| **A6** William Cecil (Burghley) | **Chokepoint Seat** — `gatekeeper` boolean on named Standing-6+ Access-column slots (e.g. Lord Treasurer): a mandatory routing point; any lower NPC's sponsorship-requiring ambition first resolves a sub-check against the holder's Disposition, who may extract a Debt-tag toll convertible to Reputation/Wealth | `gatekeeper` boolean | Procedural, not favor-based: does **not** auto-lapse on the holder's fall; **heritable** (kin-tagged Standing-5+ heir inherits at reduced toll). Sustained tolls build a faction Grudge pool → rival fires an Ordenanza-Sanction Petition (HAB-7) to strip the flag | "Routing Office" too close lexically → use "Chokepoint Seat"/"Routing Seat" |
| **A7** Tammany Hall / Plunkitt | **Patronage Broker** — inverts A1: a low-Standing NPC accumulates many small Disposition+Debt ties with the *background populace*, feeding the settlement Π/Suspicion homeostat. Aggregate populace-loyalty becomes a deliverable "bloc" traded upward for discretionary Access refilling gift-giving capacity — a closed loop | `bloc_delivered` counter; settlement-linked discretionary-Access pool | Collapses systemically: strip discretionary-Access from the feeding Ministry seat (civil-service reform) → every downstream broker's `bloc_delivered` decays and progress freezes across the board | "broker" already names a covert Investigate archetype → use "Patronage Broker" |
| **A8** Fujiwara regency marriage-politics (sekkan) | **Kin Placement** — `ambition.goal='kin placement'` targeting a marriage/kinship tie into the *still-forming* `heir_household` of a seated Leadership-track NPC; `ambition.timeline` spans multiple Accountings beyond patron tenure, re-parenting to the placed kin once marriage/birth Keys fire | `heir_household` link; multi-generational timeline persistence/re-parenting; Key `kin_placement` | Rival kin-branches compete all-or-nothing at the placement step (no graduated demotion). If the placed heir later Disposition-flips (a Generational Shift), the whole 15–20-season investment voids at the last step | clean |
| **A9** Brezhnev's "Dnepropetrovsk mafia" / nomenklatura | **Cohort Capture** — `ambition.goal='cohort capture'`; a patron forms a `cohort_id` grouping same-era peers (mutual high Disposition). On reaching a `gatekeeper` seat with FA-JP2 authority, resolves **Confirm** (never New-Grant-to-outsiders) for every member across seasons, mass-promoting the bloc | `cohort_id` | Cohort-wide top-down lapse: the moment the patron falls, every `cohort_id` member takes automatic Demotion-1 within 1 season (CHN-8 bloc purge) — authority has no independent life | avoid "registry" (false dependency on unbuilt settlement registry) → "Cohort Roster"/"Cohort Tag" |

### 40.3.2 Category B — Merit & credentialing (M2 spine)

*Rise via a two-stage gate (objective competence + discretionary sponsor); fall via credential-criteria
rewrite or a structural wealth cap. The sponsor bond persists as a lever long after the exam.*

| Entry | Mechanic | New fields / Keys | Failure dynamic | Naming |
|---|---|---|---|---|
| **B1** Roman cursus / novus homo (Cicero, Marius) | **Sponsored Ladder Climb + Crisis Waiver** — progress converts to a Standing grant only if a Standing-5+ NPC spends Mandate to sponsor (`patron_bond`); a **Crisis Key** grants a one-time waiver skipping the inter-rank cooldown | `patron_bond` (sponsor id + Mandate) Knots edge; `crisis_waiver` flag (once); Key `npc_standing_climb_attempt` → emits `standing_change` | Reuses Rival Cohort; no-patron NPCs advance slower. Repeated waiver-climbs (Marius's seven consulships) accrue faction Grudge from leapfrogged incumbents → higher civil-war-scale event probability | clean |
| **B2** Chinese Imperial Examination (jinshi, zuozhu/mensheng bond) | **Two-Stage Credential Gate with Sponsor Bond** — (1) objective competence check vs Attribute/Conviction, then (2) a discretionary Examiner NPC who can waive/fast-track/fail-anyway. Passing emits a permanent **bidirectional** sponsor bond | `sponsor_bond` bidirectional Debt edge; Key `credential_pass` (records objective result + whether override invoked) | Un-tutored NPCs structurally capped: model stage (1) as requiring a Treasury-backed "tutoring investment" spend (the wealth gate). Counter-reform is B3 | clean ("Examiner" ≠ "officer") |
| **B3** Song exam reform (anonymous grading; Wang Anshi vs Sima Guang) | **Credential Criteria Rewrite** — a high-Standing actor spends Mandate to rewrite which Attribute/Ethical Framework/Resonant Style a gate's check tests, and/or toggle `anonymize_gate` (suppresses B2 override). Faction-scoped | `credential_criteria`; `anonymize_gate`; Key `credential_reform` | Faction flip reverses it (Sima Guang counter-`credential_reform`); composes with §1.0a Demotion: NPCs whose Conviction no longer matches the reverted criteria take automatic rollback to Standing 0 | clean |
| **B4** Ottoman devshirme/kul (Pargalı Ibrahim Pasha) | **Household Favor Track (unilateral, revocable)** — parallel track for NPCs recruited outside Standing/birth (origin flag); every rank above a threshold requires an active `favor_bond` held with the ruler — asymmetric, unilaterally revocable. On revocation → §1.0a "Dismissal" (Standing −1, assets Forfeited, Dishonored) | `favor_bond` edge `revocable_by=ruler_only`; Key `favor_revocation` (collapses Standing in one step, bypassing graduated demotion) | The mechanism *is* the failure — no independent base; a rival's Grudge/Reputation attack on ruler-Disposition directly fires `favor_revocation` | **flag** — reflexively called "Household Officer" → use "Household Advisor"/"First Retinue" |
| **B5** Mamluk pipeline → sovereignty (Baybars) | **Cohort Bond + Ceiling Contest** — trained-together NPCs share a horizontal `cohort_bond`; a qualifying crisis Key makes the topmost rank contestable regardless of current Standing (jump into the discrete Leadership state) | `cohort_id`; many-to-many `cohort_bond` edge; Key `cohort_formation`; Ceiling Contest reuses SUC-01–03 | The bond that enables the rise is the coup risk: high-Standing `cohort_bond` NPCs carry elevated "betray patron" card probability scaled by cohort size/cohesion — the loyal pipeline is the likeliest usurpation source | **flag** — avoid `officer_cohort` → `retinue_cohort`/"brotherhood" |
| **B6** Napoleon — "carrière ouverte aux talents" (Grandes Écoles, Légion d'Honneur) | **Dual-Track Advancement (Talent vs Favor)** — two parallel Standing-grant channels; every grant records which. Sustained Favor-Track overuse accrues faction Reputation/Grudge eroding Talent-Track legitimacy | `advancement_track` enum {talent, favor}; Key `advancement_grant` (superset of `standing_change` + provenance) | Legitimacy erosion, not a rival: Favor-Track appointees are mechanically brittle ("public scandal: drop 2 ranks" applies at double magnitude) | clean *(sourcing caveat — see §40.5)* |
| **B7** Northcote–Trevelyan (1854) / ICS open exam | **Gate Conversion (patron-discretion → open-exam)** — a reformer spends Mandate to flip a tier's Initiation Gate from patron-controlled to open-exam (objective only), stripping specific NPCs/blocs of the gating lever | `gate_mode` enum {patron_discretion, open_exam}; Key `gate_conversion` | ~16-year delay → multi-cycle conversion: sustained Mandate spend; opposed patrons spend to stall; losing Mandate dominance mid-conversion reverts `gate_mode` | clean |
| **B8** Prussian civil service (Referendar/Assessor) | **Reform-in-Progress transitional state** — a third layer on B7: `legacy_bypass_open` boolean, true even while `gate_mode=open_exam` (formal exam exists but a legacy purchase/favor bypass persists until a ruler spends a `bypass_closure` action) | `legacy_bypass_open`; Keys `gate_conversion` then `bypass_closure` (the gap between them *is* the transition) | While open, bypass-promoted NPCs inherit B6's favor-track fragility AND accrue faction Suspicion for "reform not yet real" — forcing eventual closure or indefinite legitimacy bleed | clean |
| **B9** Meiji Higher Civil Service Exam (1887) | **Founding Cohort Dilution** — composes B5's `cohort_bond` (a founding faction whose early NPCs share a founding-cohort advantage) with B7's `gate_conversion`, faction-wide, to open a parallel exam track non-cohort NPCs can climb without the founding bond | purely compositional (B5 + B7); `gate_conversion` gated on a "consolidation secure" predicate (Π-homeostat stability) | Reuses B5's double-edge: founders losing their advantage is a thwarted-ambition "betray patron" event — the dilution reform *is* the founding-generation rebellion trigger | **flag** — militarized founding-cohort member's political rank kept distinct from mass-battle "officer" |

### 40.3.3 Category C — Marriage alliances & kinship networks (M3 spine)

*Rise via blood-tie to the ruling line; fall via generational flip, demographic lapse, or the permanent
"consort-advisor ceiling." Most stresses the multi-generational / lineage-scope gap.*

| Entry | Mechanic | New fields / Keys | Failure dynamic | Naming |
|---|---|---|---|---|
| **C1** Habsburg marriage diplomacy (Maximilian I) | **Contingent Claim Banking** — `ambition.method='dynastic'`; a claim on a *currently-occupied* seat that advances via a marriage Key + the holder's line surviving; "if target line's heir dies without issue → claim auto-resolves (fires 'press the claim')." Sits dormant for game-years | `ambition.contingent_on` (watched external Key predicate); Key `marriage_contract_banked` → auto-fires on `standing_change` (death/exile no-heir) or new `line_extinguished` | Contested only *at resolution*: a rival with independent military/diplomatic weight gets "contest the banked claim" the instant the vacancy fires; sticking is gated on Rival Cohort standing + military leverage, not the marriage | clean |
| **C2** Fujiwara regency (sekkan seiji) | **Generational Consort-Supply Precedent** — a **lineage-scoped** Ledger tag family, "Kinship Precedent"; each successive daughter-marriage into the ruling house increments its weight; at threshold the lineage head gains an informal regency track modeled on **HAB-2 (Valido)** | lineage-level "Kinship Precedent" tag (existing families are NPC/faction-scoped, not lineage-scoped); no new Key beyond `standing_change` recording `decided_by=monarch` | Rival cousins → Rival Cohort scoped to the lineage's internal succession-of-supplier. Precedent zeroes if the lineage fails to place a daughter with the *reigning* monarch for a generation (auto-decay if no marriage Key within N Accountings — demographic, not violent) | clean |
| **C3** Ottoman damat (imperial son-in-law) | **Consort-Advisor Ceiling** — `succession_eligible` hard-set **false** on marriage into the ruling house for a capable-but-ineligible subordinate, paired with a Standing fast-track (skip Initiation Gates up to Standing 7/senior-advisor). The flag is **permanent and unremovable** | `succession_eligible` (bool, permanent-false); Key `consort_bond_formed`. **Overlaps BYZ-8 — consolidate** | The bond's Disposition anchor can flip without misconduct — a Demotion firing purely off patron-Disposition collapse, instantly dropping Standing even though `succession_eligible` was never the failure point | **YES** — a spouse-bound chief administrator is exactly "officer" → use "advisor"/"consort-advisor" |
| **C4** Woodville affinity cascade (England 1464–83) | **Patron-Granted Standing Cascade** — per-NPC `standing_source` (earned \| patron-granted), set when advancement bypasses gates on one patron's favor, applied to a *cluster* simultaneously, all pointing to the same `patron_id` | `standing_source`; `patron_id` linkage; Key `patronage_cascade_voided` (patron_id, affected_npc_ids[]) — child of `standing_change` on the patron's death/exile → every patron-granted client takes an immediate §1.0a Demotion | The cascade *is* the failure — no rival action required; a zero-earned-Duty cluster cascades harder. A rival gets only an opportunistic "press the purge" card once it fires | clean |
| **C5** Wang Mang & the Han consort clan (waiqi) | **Consort-Clan Leverage (multi-generational)** — a genuinely new **clan/lineage object** accumulating `dynastic_leverage` across reigns (increments whenever a member's daughter is/remains consort to the *reigning* monarch); feeds a clan-head's ambition ("convert regency into Leadership") | clan-scale `dynastic_leverage` — **requires promoting the Accounting-cascade tick to a clan/lineage entity above the single NPC (the biggest structural ask)**; Key `regency_established`; final seizure extends `coup_attempted` with a new `usurpation` outcome | Rival consort clans → Rival Cohort at clan scale. The final usurpation checks Conviction/Disposition via the Stance Triangle — a clan head whose Conviction drifted from generations-built reputation backfires even at maximal leverage | clean |
| **C6** Mongol quda under Genghis Khan | **Marriage-Tribute Obligation (conquest-alternative)** — a new entry on the Required Obligations column for subject factions: elevated baseline Disposition + partial-autonomy retention in exchange for a perpetual wife-supply Obligation | reuses Obligation/Disposition/Standing; Key `marriage_alliance_formed` (faction scale) | (1) resistance instead draws worse-treatment (**shared with C10's Rajput contrast**); (2) generational lapse of "perpetual" supply → auto tie-lapse if no marriageable daughter within N Accountings (modeled on CHN-9 auto-lapse) | clean |
| **C7** Rothschild endogamy | **Endogamous Lock** — a Ledger tag across a faction's internal branches: while active, reduces the Suspicion field's growth rate for members and lowers external Investigate "co-opt" success, at the cost of shrinking the branch's external marriage-market pool | "Endogamous Lock" tag (faction-branch-scoped, boolean-plus-strength); Key `endogamy_pact_formed` (formation only) | Opportunity cost, no external rival needed — a locked branch can't also run external alliance expansion (C1/C6/C10). A forced out-marriage breaks the tag and pays out suppressed leak-risk at once as a Suspicion spike | clean |
| **C8** Romanos I Lekapenos (basileopator → co-emperor) | **Staged Co-Leadership Climb** — a staged trajectory (marital tie → intermediate honorific → co-Leadership) requiring a **new intermediate state** between Standing 7 and the binary Leadership state; "if unopposed N seasons → advance," chaining three stages | `co_leadership` state (Leadership-adjacent, non-exclusive — a genuine gap; Part 2 has no partial/shared-rule concept); Key `co_leadership_claimed`, or extend `coup_attempted` with a fourth "co-opted" outcome | A "Legitimate Heir Living" tag on the true-line NPC makes "restore the true heir" an available goal; success strips `co_leadership` from the usurper's line **including children already promoted** (944/945 double reversal) | clean |
| **C9** Akbar's Rajput marriage-alliance policy | **Dynastic Marriage Entry + Resistance Cost** — a new `standing_change` trigger `dynastic_marriage`: an allied ruler's kin gain immediate mid-rank Standing (e.g. 3) in the dominant ladder on marriage, skipping gates, while keeping their own separate throne (dual-track membership). Paired with a "Resistance Cost" tag on holdouts | additive trigger-enum extension; one "Resistance Cost" tag (**structurally identical to C6 — author once**) | (1) the shared C6 Resistance Cost; (2) integrated kin hit the C3 damat ceiling — high in administration, blocked from throne-succession → a long-blocked ambition shifts violent/covert | clean |
| **C10** Venetian patrician endogamy & the Libro d'Oro | **Registered-Lineage Eligibility Gate** — a categorical block: `marriage_registered` (bool) gating **all** advancement above Standing 0 for a closed-oligarchy archetype; unregistered marriages produce permanently-ineligible descendants. Paired with an inheritable "Registered Lineage" Precedent-family tag | `marriage_registered`; closed-eligibility registry object; inheritable-Precedent propagation; Key `marriage_registered`. **Speculative pending a Venice-style faction being authored** | (1) bribery targeting registry gatekeepers (Investigate co-opt); (2) over-transaction backlash — a Grudge tag accrues against houses manipulating dowries/registration → "reform/audit the registry" can strip status retroactively | clean |

### 40.3.4 Category D — Court favorites & power behind the throne (M4 spine)

*The richest vein for HAB-2 (Valido). Rise via Royal-Intimacy outperforming Standing; fall binary and
often violent. Several entries directly answer HAB-2's open needs_jordan questions.*

| Entry | Mechanic | New fields / Keys | Failure dynamic | Naming |
|---|---|---|---|---|
| **D1** Rasputin & the Romanov inner circle | **Proxy-Intimacy Favorite + Regency Window** — extends **HAB-2**: the Favorite's Royal-Intimacy is scored against a *consort*, not the ruler; a "Regency Window" state (ruler absent, consort holds interim authority) multiplies the Favorite's Patronage-Web reach while open | "Regency Window" state (open/closed, opened_by, `authority_delegate=consort_id`); or `interim_authority_delegate` payload on `state.succession` | HAB-2 binary collapse **plus legitimacy contagion**: Grudge accrues against the *consort*; excluded Standing-5+ nobles execute the Favorite outside any formal process (assassination); the regime's own legitimacy collapses shortly after | clean |
| **D2** Sejanus, Praetorian Prefect under Tiberius | **Access-Gatekeeper Prefect** — a named inner-circle office-holder doubling as the **CHN-7 Chancellery Gatekeeper** plus a physical-isolation clause: the ruler relocated remote, the Gatekeeper controls the Access channel itself (who may petition), not just message content | `isolated_residence` bool on the ruler (gates whether CHN-7 substitution is total); new Key only for the downfall | A **bypass channel**: a single trusted freedman with a pre-isolation tie delivers unfiltered info once → HAB-2-style Total collapse from a single bypass. Model as a one-shot Investigate/Knot action for pre-isolation-tie NPCs firing `standing_change` (exile, total), no appeal | **flag** — "Prefect" commanding the Guard ≈ mass-battle unit-commander "officer"; if he also commands a mustered Guard unit, that officer is a distinct auto-generated record |
| **D3** Wei Zhongxian & the Eastern Depot | **Reign-Bound Cohort Purge** — a surveillance bloc patron-bound to the current reign: reuse CHN-9's patron-bound lapse scaled from chain to persecuting cohort, paired with **CHN-8 (Bloc)** as the successor's demotion mechanism | none — CHN-9 + CHN-8 composed and chained off `state.succession` | Succession-triggered instant total reversal: power was authority-by-proxy on one ruler; the successor was structurally outside the network (Disposition defaults hostile). Fast and total | clean ("Eastern-Depot cohort"/"secret-police bloc") |
| **D4** Zhao Gao & the forged succession edict | **Seal/Mandate Custody Forgery + Compelled Loyalty Test** — during the vacancy window between a ruler's death and `state.succession` resolving, whoever holds physical custody of the Mandate token can **fabricate** the succession Key's contents via covert Deception, contested only by an NPC with independent knowledge of the true will. Paired with a "Compelled Public Loyalty Test" scene-verb (every Standing-3+ NPC publicly declares Disposition; hesitation → immediate Total demotion) | `state.succession` payload `fabricated`/`discovered` bools; scene-verb "Demand Public Loyalty Test" | Delayed cascading discovery: the forgery holds while uncontested; eventual Investigate/purge-survivor discovery retroactively flips legitimacy → mass Grudge + `coup_attempted` from the true heir's allies | clean ("Seal Custody"/"Regent-Forger") |
| **D5** Nur Jahan's shadow administration | **Kin-Distributed Favorite Web** — extends **HAB-2's Patronage Web** from a single client roster to an explicit multi-NPC family bloc (each member independently climbs with an Ob discount while the founder's Royal Intimacy holds), bound by **Knot-relationships (FA-JP4)**. When members' Knots point at *different* heir-claimants, the Web has an internal fault line | `web_id` grouping multiple NPCs (HAB-2 implies a single Favorite + amorphous clients) | **Internal fracture**, not external defeat: at the ruler's death, members resolve competing Knot-loyalties; the founder (weakest own claim) loses control as the strongest-Knotted member backs the winner → confinement/demotion | clean |
| **D6** Madame de Pompadour as unofficial minister | **Institutionalized Favorite (Web decoupled from Intimacy)** — **directly answers HAB-2's needs_jordan Q3** ("does the binary collapse ever soften?"): once a Favorite's Web contains 2+ clients independently at Standing 5+ through her sponsorship, the Web graduates to "Institutionalized"; influence is scored against aggregate senior-client Disposition, and HAB-2's binary collapse no longer applies | `web_institutionalized` (threshold-triggered bool) | Slower partial purge: rivals accrue Grudge but can't trigger collapse once Institutionalized; only at the Favorite's death does a CHN-8-style purge open against surviving clients, and it's graduated (Standing-5+ clients survive on earned rank) | clean |
| **D7** George Villiers, Duke of Buckingham | **Heir-Banked Favorite Transfer (HAB-2 × HRE-2)** — applies **HRE-2 Chapter Capture** (pre-vacancy banking under timing uncertainty) to the Favorite track: proactively cultivate Disposition/Standing credit with the *heir apparent* before succession. If banked heir-Disposition clears threshold when `state.succession` fires, the Web survives without §1.0a's succession-demotion check | `heir_banked_disposition` (or reuse HRE-2's "seats owed" banking) | Surviving one succession neutralizes institutional collapse but **not** the accumulated personal Grudge pool — downfall shifts to a scene-level impeachment Contest, then assassination keyed off Grudge. **Banked heir-Disposition protects the Web/Office, not the person** | clean |
| **D8** Kösem Sultan & the Valide Sultan system | **Contested Regency Slot, resolved via Gatekeeper realignment** — a single-occupancy cross-reign-persistent **Dignity** (BYZ-1) contested by *two* claimants simultaneously, resolved through a third-party **CHN-7 Gatekeeper** rather than a direct Contest: whoever holds the Gatekeeper's Disposition controls Access to the minor-heir | "Contested Slot" relationship (two ids racing for one single-occupancy row); composes BYZ-1 + CHN-7 | The Gatekeeper **survives the coup** and keeps the chokepoint under the new patron — a distinctive non-resolution: the loser is eliminated but the systemic risk persists, setting the identical failure to recur | "Gatekeeper" shared with CHN-7 **by design** — author once, not twice |
| **D9** Basil Lekapenos, the eunuch parakoimomenos | **Multi-Reign Oath-Bound Administrator + Personal-Rule-Assumption demotion** — **the direct real-world precedent for BYZ-8**; adds multi-reign persistence (he served five). Each survived reign-transition stacks a capped "Institutional Indispensability" bonus; a new Demotion Trigger **"Personal Rule Assumption"** lets the ruler unilaterally revoke the Office at *zero* Coup Counter cost once they cross a majority/independence threshold | capped `reigns_survived` counter; optional new `state.standing_change.trigger` value. **Duplicate coverage of BYZ-8 — contribute as amendments** | Distinctively **non-violent** — the adult ruler exercising ordinary authority once the regency need lapses; the renounced dynastic claim removes retaliation capacity | clean ("parakoimomenos"/"Oath-Bound Administrator") |
| **D10** Yanagisawa Yoshiyasu & the sobayōnin office | **Lineage-Bypass Grant (Upstart Favorite) + reign-transition reassessment** — **institutional**, not purely personal: the ruler grants rank above caste/lineage (skipping the Initiation Gate lineage prerequisite), reusing **IT-8's Upstart tag**. Downfall orderly: at the next `state.succession`, the new ruler's own advisor gets a one-shot "Reassess Upstart Grant" stripping the Office half of BYZ-1's split (Dignity/domain may persist), no Contest | scene-verb "Reassess Upstart Grant" (new ruler's advisor only, Upstart-tagged holders, season after succession); extends IT-8 to the general ladder; composes with BYZ-1 | Ordinary graduated demotion — because the grant was *visibly* Upstart (durable tag), no Grudge/Contest needed; the Reassess is a designed no-drama check. The opposite pole from D3's violent purge | **flag** — "sobayōnin" ≈ "the Shogun's attendant," most likely mistranslated as "officer" → "Steward"/"Chamberlain"/"Sobayōnin" |

### 40.3.5 Category E — Bureaucratic / institutional capture (M5 spine)

*Rise via sitting on the routing path without a vested office (the "Conduit"); fall via bypass,
succession, or the patron's fall. Proposes a unifying "Conduit" role most other chokepoint entries
reference. (Category E has 8 entries; E1–E8 are the full set.)*

| Entry | Mechanic | New fields / Keys | Failure dynamic | Naming |
|---|---|---|---|---|
| **E1** Roman imperial freedman secretaries (Pallas, Narcissus) | **Conduit role + patron-bound ambition** — a role-tag **"Conduit"** on any NPC regardless of Standing: no vested office, sits on the routing path between a patron (or ruling player) and everyone else. `ambition.method` locked to "lawful→factional"; `ambition.goal` explicitly *advancing a named patron's faction*. Patron-Disposition soft-multiplies progress; the moment the patron stalls/is thwarted/loses a succession card, progress force-resets toward 0 and trajectory flips violent/covert or terminates | `patron_id` + "bound" flag (no concept today of one NPC's progress being derivatively contingent on another's ambition outcome) — **the clearest load-bearing case for extending the ambition engine upward** | Two Conduits bound to *rival* patrons: whichever patron wins the succession card first triggers the other Conduit's forced-reset + near-term removal, fired as an automatic Key | clean — "Conduit," not "secretary-officer" |
| **E2** Venality of office & the Paulette (droit annuel) | **Office vesting (Standing tenure modifier)** — an NPC/player at Standing ≥1 in an office-bearing slot may pay a recurring Treasury cost (renewed each Accounting) to flip the slot's tenure from "revocable" to "vested." A vested rank is immune to the *default* one-rank Demotion — losable only via Severe/Total triggers | `office_vested` bool + recurring-Debt renewal check; §1.0a Demotion-Magnitude modifier, no new Key | The *grantor* loses control, not the holder: model vested-office NPCs as contributing to the unserved-Needs term of the Π homeostat whenever a Directive touches their prerogatives — a standing structural veto bloc (the Fronde) | clean |
| **E3** Richelieu's intendants | **Shadow appointment (overlay agent)** — a faction leader spends an action to install an at-will-revocable "Intendant" into a territory held by a vested-office NPC (E2); it doesn't replace the holder's rank — it intercepts and supersedes that domain's Directive-resolution and petition routing, fully revocable, no vesting available | Key `mechanical.shadow_appointment` (patron_id, agent_id, overlaid_actor_id, domain_id, revocable=true) | Hard dependency: the instant the appointing patron falls, the Key auto-expires and the Intendant collapses via Total Dismissal, no appeal. Displaced vested holders accrue a Grudge against the *patron*, feeding Π | **explicit flag** — do NOT name "officer" → "Intendant"/"Crown Agent"/"Enforcer" |
| **E4** Thomas Cromwell as Principal Secretary | **Documentary strike (weaponized Conduit action)** — a Conduit with high enough progress spends it to file a "documentary strike": manufactures apparent-sovereign authorization for its own initiative and directly triggers a Severe Demotion (§1.0a "public scandal") against a target who did not transgress | Key `mechanical.documentary_strike` (instigator_id, target_id, apparent_authorization, actual_authorization, framing) | Valid only while the Conduit retains patron favor (Disposition ≥ 0); the instant favor lapses, an *identical* strike becomes trivially available against them, auto-succeeding (they hold no vested Standing — Cromwell's attainder) | clean — reuses "Conduit" |
| **E5** Ottoman Kızlar Ağası (Chief Harem Eunuch) | **Access-gate role with independent endowment income** — a Conduit variant restricted to ladder-ineligible NPCs; controls a literal access chokepoint (any Social Contest with the gated principal must clear the gate-holder's Disposition). Uniquely converts access-leverage into an independent Treasury/endowment income that persists even if the gate closes | `gate_target_id`; `access_threshold`; an endowment/ward asset (**needs a territory-layer income hook not fully specified — flag before implementation**) | Bound to the faction's succession like the Roman Conduits → Total Dismissal auto-fired on the patron losing a succession contest, **but** the endowment is NOT auto-stripped; it becomes a contestable asset the new regime must reassign | clean if "Gatekeeper"/"Warden"; avoid "Chief Officer" |
| **E6** Wei Zhongxian & the vermilion rescript process | **Borrowed mandate (disengaged-ruler escalation) + fictive-bond client cascade** — when the principal enters a modeled "disengaged" state, a bound Conduit may escalate to autonomously emitting Directive-equivalent Keys *as if authored by the principal*, then rapidly seed satellite clients via a `fictive_bond` flag (each client's Standing entirely parented to the Conduit, bypassing the Initiation Gate) | `disengaged` flag on the principal; `fictive_bond` bool on clients; Key `mechanical.borrowed_mandate` | Totality and speed: the succession Key flips every `fictive_bond` client to Total Dismissal within a single Accounting tick, bypassing the §1.0a two-season appeal (never real standing) | clean — "Conduit"/"borrowed mandate" |
| **E7** Papal Cardinal-Nephew (Scipione Borghese under Paul V) | **Calendar-bound kin-gatekeeper with extraction-biased ambition** — a Conduit selected by kinship whose `ambition.timeline` is *computed as a cap* from the patron's expected remaining tenure; the short horizon biases `ambition.method` toward **"extractive"** (rapid asset conversion) and unlocks a 4th Ambition-card outcome: **"convert to asset"** (locks in extracted wealth/leverage permanently) | `ambition.method='extractive'` enum value; card outcome "convert to asset" | Rival curial families → Rival Cohort. On the patron's death, locked "convert to asset" gains are NOT clawed back, but the gate role reverts to Standing 0 — **the extraction, not the office, survives** | clean — "kin-gatekeeper"/"Conduit" |
| **E8** Soviet Nomenklatura & the Orgraspredotdel | **Patronage ledger (compounding sponsorship chokepoint)** — a genuinely new NPC-level stat: an NPC accumulates a running list of others whose Initiation Gate they personally sponsored (each client a Debt tag toward the sponsor). It **compounds** — each appointment increases the sponsor's durable support base for any future Standing-contest/Ambition-card vote, independent of the sponsor's own rank | `clients_sponsored` (list/weighted count); Key `mechanical.patronage_appointment` — **the one entry that cannot be modeled as a Conduit/ambition variant** | Rivals *miss the threshold* until reversal is impossible: below a `clients_sponsored` threshold a normal contest works; above it, no single card can touch them, requiring a higher-cost `mechanical.purge_cascade` demanding a rival supermajority coalition (why Lenin's Testament went unactioned) | **explicit flag** — natural label "personnel officer"/"chief of staff" → "Patron"/"Sponsor"/"Patronage Ledger" |

### 40.3.6 Category F — Rise to power via military retinues (M7 spine)

*Rise via a personal self-loyal armed force outside the ladder; fall via coalition purge,
subordinate-flip, or fragmentation-on-death. **Highest naming-collision density in the corpus** — nearly
every entry flags "officer."*

| Entry | Mechanic | New fields / Keys | Failure dynamic | Naming |
|---|---|---|---|---|
| **F1** Roman Praetorian Guard — the 193 CE throne auction | **Retinue Veto Threshold + Donativum bid-war** — a hidden `retinue.leverage` (0–5) sub-field on the ambition block, rising when the ruler relies on the guard to survive a crisis, *spent* at a succession vacancy. If leverage ≥ 3 the guard (a collective NPC) auto-resolves a kingmaker event — each claimant's bid becomes a Standing-contest where leverage adds a flat modifier to whichever offers the higher one-time Debt payout (the donativum), resolved by comparing Debt-tag magnitude | `retinue.leverage`; guard as a collective NPC at court scale; Key `state.succession_vacancy` (payload `guard_leverage`, optional `donativum_bids`) | Only way to zero leverage: a claimant who wins by military conquest (`scene.battle_concluded`) *without* bidding resets leverage to 0 and reassigns the muster; bidding then reneging is itself a Grudge generator | "guard"/"retinue" avoids it, **but** the mass-battle `officer_deaths` field is a plausible trigger — read in the mass-battle unit-commander sense, not the court-level collective |
| **F2** Carolingian Mayors of the Palace (Pepin, Charles Martel) | **Household Office Capture + Hereditary Lock-in** — a subordinate household post with patronage-grant power sets `ambition.goal='make office hereditary'`; each grant increments progress AND writes a Precedent tag scoped to the *office* ("this office grants to kin"). At progress 5 the office flips crown-appointed → hereditary-within-family | mutable `succession_rule` on the office/post record (offices are currently static slots); Key `state.office_hereditary_lock`. **HRE-2 territory** | Not reversal but **external legitimation required** — the hereditary-lock Key can't itself trigger a dynasty-replacement without a second independent Key from a legitimating faction (Church Standing actor); absent it, a stable hereditary-but-subordinate sub-dynasty | clean — "household office"/"patronage grant"; "Mayor of the Palace" as flavor safe |
| **F3** Ottoman Janissary Corps — tool to kingmaker | **Corps Ossification** — a corps built to bypass nobles starts `ambition.goal='serve the crown'` but accrues `corps.entrenchment` (0–5), rising passively every un-rotated Accounting and faster if economic Debt tags exceed a threshold. At 5 its ambition auto-flips (goal "veto reformist rulers," method violent) and gains standing veto: any ruler action reducing corps privilege auto-generates an Intrigue/Ambition contest | `corps.entrenchment` — **a genuinely new institution-level drift layer**; the corps occupies a Standing slot as an institutional actor; Key `state.corps_entrenchment_shift` | Only violent replacement (1826 Auspicious Incident): at entrenchment 5 the *only* card resolution is "build a rival corps from zero, then a single decisive `scene.battle_concluded`" — no lawful/social branch. The institution forecloses non-violent branches for opponents | **high risk** — "corps member"/"retinue trooper," never "officer" |
| **F4** Mamluk slave-soldier households → Sultanate | **Patron-Client Household (ustadh/mamluk)** — a bounded patron-client pair: a patron's ambition spends "recruit client" to create subordinates whose Standing is entirely derivative (`bond.patron_id`). On the patron's death, the *client* (not a biological heir) inherits accrued Standing/tags and a fresh recruitment cycle begins — blocking any bloodline past one generation | `bond.patron_id`/`bond.client_ids`; a "derivative Standing" flag (evaporates on patron death unless a client inherits); Key `state.patron_succession`. **BYZ-8-adjacent anti-dynasty rule** | The *opposite* of most entries — stability came from blocking hereditary calcification. Rival *households* fight for the citadel seat; the winner ascends and rivals keep their bonds intact; the base perpetually renews via recruitment | clean — "patron"/"client"/"household"; avoid "officer" for client-NPCs |
| **F5** Francesco Sforza — condotta to crown (Milan) | **Contracted Retinue → Dynastic Marriage Claim conversion** — a mercenary-captain's ambition ("best contract terms") unlocks, on a Standing threshold via contract fulfillment, a goal-branch "marry into the patron house" (existing "if blocked, shift method" logic applied on *success*), writing a latent Precedent tag ("this marriage was a political payment") until the patron line fails | none — clean reuse of ambition/trajectory + Standing + Precedent; the "vacancy" trigger is F1's `state.succession_vacancy` (**evidence it should be a shared cross-entry primitive**) | A countervailing patron-side branch: "if client retinue-strength exceeds my Standing lead by N, attempt to void the marriage-claim Precedent" — a recurring social-contest tug-of-war until the vacancy fires | clean — "contracted captain"/"condotta retinue" (never the field name) |
| **F6** Wallenstein's self-financed imperial army | **Self-Financed Retinue Autonomy + Subordinate-Turned-Assassin** — `retinue.autonomy` (0–5, distinct from F1's political `retinue.leverage` — tracks *financial* independence). High autonomy raises Standing fast but writes a rival Grudge proportional to it. Sub-commanders accrue their own `client.crown_loyalty` **separate from** `client.patron_loyalty` — the latent assassination vector | `retinue.autonomy`; a second loyalty axis on bonds; Key `state.retinue_autonomy_shift` | The sovereign turns the general's own senior subordinates against him — model dismissal as the crown spending Debt/patronage on clients' `crown_loyalty` to flip one into an assassination-trajectory. **The one entry where the resolution routes *around* the power-base's strength** | **high risk** — subordinates literally "officers" in every source → "retinue client"/"sub-commander" |
| **F7** Cao Cao — "support the Son of Heaven" | **Legitimacy Hostage** — an NPC who physically controls a Mandate-bearing figure *without* deposing them gains `mandate.custody_bonus`: a flat Standing-equivalent bonus on any contest invoking the captive Mandate, multiplying *effective* Standing for legitimacy-gated actions while base Standing is untouched | `mandate.custody_bonus` + `custodian_id` distinct from `holder_id` (**the sharpest genuine architectural gap** — Mandate must become separable-from-possession); Key `state.mandate_custody_change` | A race, not a stable state: after a Mandate-vacancy Key, a limited window opens for any sufficient-Standing rival to attempt custody-seizure; once closed the card despawns. Failure is *permanent forfeiture of a legitimacy chokepoint*, with deferred consequences (Cao Pi's usurpation a generation later) | clean — "custody"/"Mandate-holder" |
| **F8** Minamoto no Yoritomo & the gokenin → Kamakura Shogunate | **Parallel Vassal-Band + Dual Legitimacy (shadow Standing)** — an NPC builds a personal vassal-band (F4 bonds) via direct land-for-service, accruing a **`shadow_standing` (0–7)** parallel track from vassal-grant Keys. When it exceeds formal Standing by a threshold, the NPC spends a card to force the formal holder to **ratify** the shadow structure — converting shadow appointments to legal offices in one stroke (the sei-i taishōgun grant) while the sovereign keeps their Standing-7 seat: dual legitimacy, not replacement | `shadow_standing` — an off-ladder accumulation track that can force ratification; Key `state.shadow_standing_ratified` | Purge-your-own-lieutenant (Yoshitsune): a client whose independent Standing (personal battlefield success) grows faster than `bond.patron_loyalty`; once it exceeds a threshold vs the patron's `shadow_standing`, the patron's trajectory gains "purge or lose the client to a rival power base" | clean — "vassal-band"/"client"; "shugo"/"jito" as flavor safe |
| **F9** The Mongol Keshig — hostage-and-training pipeline | **Hostage-Cohort Pipeline (inverted-status recruitment)** — a ruler demands subordinate Standing-holders send an heir into household service (a `bond` patron_id=ruler on the heir + a Debt tag against the household). The heir's Standing resets to a service-track baseline overriding birth-Standing while in the corps — a **`service_rank` (0–5)** inverted prestige ladder. On graduation, alumni are preferentially assigned admin/command slots, converting `service_rank` into fast-tracked Standing | `service_rank`; a `compulsory` bool on the bond; Keys `state.hostage_service_commenced`/`state.service_graduation` | No clean historical reversal — structural: if the ruler stops rotating fresh cohorts, alumni calcify into an old-boys' bloc (their own `bond.client_ids` growing from patronage), converging on F3's `corps.entrenchment` — the pipeline becomes the hereditary interest it was designed to prevent | clean — "keshig"/"hostage-cohort"; graduates commanding mustered units become mass-battle "officers" at that point — a boundary to document, not collide on |
| **F10** Yuan Shikai & the Beiyang Army — to the presidency | **Academy-Patronage Network + Fragmentation-on-Death cascade** — a recruitment/training privilege creates many bonded clients at once: `network.scale` (recursive bonded-client count) grows via training Keys. At a threshold AND a state-crisis Key only this force can resolve (a "monopoly moment"), ambition auto-unlocks an "extract the throne" branch with compressed timeline. On the NPC's death, `network.scale` **fragments** — each top-tier client spins off as an independent Standing-holder (a Warlord-Era field) | `network.scale` (recursive — F4's simple bond doesn't model nesting/fragmentation); Key `state.crisis_leverage_extraction`; reuse `state.patron_succession` generalized to fire recursively | Fragmentation-on-death *is* the failure — no rival needed; on the top patron's death the cascade fires unconditionally, converting one Standing-7 holder into N mid-Standing rivals, **none holding a legitimacy chokepoint** (contrast F7) | **highest risk of all** — Duan Qirui/Feng Guozhang collide hardest → "client"/"network member"/"protégé"; **the design doc should carry an inline naming-collision callout at this mechanic's definition** |

### 40.3.7 Category G — Downfall, purges & succession

*The mirror image of rise. Specifies the failure side of M4/M5/M7/M8 in detail and introduces several
genuinely-new primitives: dormant/conditional tags, the joint Coalition object, self-reinforcing
Culpability chains.*

| Entry | Mechanic | New fields / Keys | Failure dynamic | Naming |
|---|---|---|---|---|
| **G1** The Fall of Sejanus | **Chokepoint Access flag with Bypass-Key revocation** — an advisor bound to a specific ruler holds a tiered `access_monopoly` (all orders/info route through them). While held, Standing climbs faster than any Rival Cohort contest (rivals can't even be *seen* forming). The moment the ruler issues an order through ANY other channel, the flag flips off in one Key and Demotion jumps straight to **Total** | `access_monopoly` (bool/tier, bound to a ruler id); Key `chokepoint_bypass` | The bypass works because a designated alternate advisor has been secretly advancing their *own* ambition ("become the new channel") — invisible precisely *because* the chokepoint-holder's monopoly blinds them. Dramatic irony enforced structurally | clean — "Chokepoint Advisor"/"Access-holder" |
| **G2** The Fall of Thomas Cromwell | **Brokered-Outcome Ledger tag + appeal-bypass Demotion** — when an advisor brokers the ruler's marriage/alliance, tag the outcome "Brokered-Outcome." If the resulting ruler↔brokered-party Disposition delta is negative, it converts to a Grudge scaled to the damage, feeding §1.0a's Severe tier AND **disabling the normal 2-season appeal window** (attainder — no trial) | "appeal-bypass" boolean on a Demotion trigger | The rival wins not by attacking the broker but by having a substitute intimate already positioned (a niece); the Ambition card is *pre-advanced* (near-threshold), so succession reads instant, not contested | clean |
| **G3** Ottoman Kul System & execution of Grand Viziers | **legitimacy_ceiling classification + escheat-on-Total-Demotion** — a structural type `legitimacy_ceiling` ('capped' vs 'dynasty-eligible') gates a trade: a capped advisor climbs faster (reduced/waived Rival Cohort, can't found a rival dynasty) but ANY Demotion resolves at **Total** with zero appeal AND fires an **escheat** Key reverting accumulated Wealth to the patron | `legitimacy_ceiling`; escheat transfer; Key `escheat_purge`. **Strongly overlaps CHN-9 — build as a variant** | Rivals accumulate Grudge as the favorite's wealth grows; at threshold the ruler auto-fires Total + escheat as a "harvest" — a Π-homeostat-style accumulator specific to this favorite | "Grand Vizier" ≈ a command role → "capped patron-advisor"/"kul-bound advisor" |
| **G4** Wei Zhongxian & the Ming eunuch faction | **Succession-triggered dormant-tag cascade** — reuses `access_monopoly` (G1) but the revocation trigger is a **succession Key**: all NPCs whose monopoly binds to the outgoing ruler auto-suffer Total Demotion within a window UNLESS they *also* hold independently-earned transferable Standing. Simultaneously, dormant rival Grudge/Precedent tags activate en masse as justification | `trigger_condition: succession` metadata on Ledger tags (a tag sits inert until a specific Key fires — a genuinely new capability); Key `succession_purge_cascade` | The incoming ruler's first Accounting fires the cascade — the holder's power has zero transferability, so the new ruler has every incentive to destroy the predecessor's chokepoint-holder. No external coalition needed | clean; avoid "eunuch official" → "palace advisor"/"chokepoint-holder" |
| **G5** Yagoda–Yezhov–Beria NKVD succession | **purge_predecessor ambition goal + self-reinforcing Culpability Debt chain** — a new goal subtype **`purge_predecessor`** (dismantle the current enforcement-holder's client network on the ruler's behalf). On installing at the vacated slot, the successor accrues a **Culpability Debt** tag (compromising knowledge), which seeds the *next* successor's `purge_predecessor` — a self-perpetuating chain, each link's Culpability higher, shortening that holder's own Demotion clock | `purge_predecessor` goal; Culpability Debt (in the Debt family); `shadow_deputy` Knot subtype (successor pre-embedded, advancing in secret); Key `predecessor_purge` | The chain doesn't self-terminate — each purger becomes the next target with an *accelerating* Demotion clock, until the ruler breaks the pattern or is removed. An escalating-magnitude spiral | "NKVD chief"/"security chief" close → "enforcer-patron"/"security-retinue head" (`officer_deaths` = mass-battle) |
| **G6** The Night of the Long Knives | **independent_power_base threshold + joint Coalition Purge object** — `independent_power_base` (raw retinue/influence not on the ladder); when it exceeds a threshold relative to the faction's institutional strength, auto-generate a temporary **multi-NPC Coalition object** — several rivals, each with pre-existing Grudge/Debt, bound into a single joint Ambition/Intrigue card with a shared trigger and uneven shared payoff. Resolution retroactively writes a Precedent tag justifying the purge | `independent_power_base`; **the Coalition object itself** (ambitions today are strictly per-NPC — **the clearest new-mechanic requirement in the downfall set**); Key `coalition_purge` | Uneven post-purge reward (one member gets an SS-style autonomy bump) can seed the *next* chokepoint-favorite recursively — a recursive setup hook, not a clean resolution | **direct collision** — the target (a paramilitary commander) is exactly the "officer" shape → "Warband Patron"/"Retinue-Captain", with mass-battle *reading* (not duplicating) `independent_power_base` |
| **G7** Basil Lekapenos (downfall view) | **succession_immune continuity flag + ruler-side rule_without_regent ambition** — `succession_immune` marks an NPC legally barred from ever holding Leadership; the *inverse* of G4's cascade: their Standing/Disposition explicitly **survive** the succession Key intact. Their fall is triggered by the *new ruler's own* ambition — goal **`rule_without_regent`** climbing with the ruler's maturation, firing a *moderate* (not total) Demotion (exile, no Dishonored) | `succession_immune`; `rule_without_regent`. **Strong overlap with BYZ-1 and BYZ-8 — consolidate** | No external rival — the "rival" is the ruler's own ambition clock; a soft, near-inevitable, gentle/exile-grade fall (cross-reign continuity becomes evidence of scheming once the regent is no longer needed) | clean — "Grand Chamberlain"/"court patron" |
| **G8** Cesare Borgia & execution of Remirro de Orco | **Reputation-tag transfer via scapegoat execution** — mostly reuse: a settlement's negative Suspicion/Disposition toward an enforcer accumulates normally. The new piece: a ruler-initiated **Public Execution Key** that (a) transfers accumulated negative Reputation from ruler onto a one-time write-off on the enforcer, flipping the ruler positive, and (b) sets the enforcer's Demotion to **Total instantly, bypassing the trajectory-consult step** | a "transfer" operation on the Reputation family; instant-Total-bypass-trajectory mode; Key `scapegoat_execution` | The transfer only works if the enforcer had zero `independent_power_base` (G6) — an enforcer with their own base can't be cleanly scapegoated; attempting it fails and generates a new Grudge against the ruler ("botched scapegoat") | tempting "enforcement officer" → "enforcer"/"instrument-advisor" |
| **G9** Robespierre & the Thermidorian Reaction | **denunciation_pipeline exhaustion → procedural Coalition Purge** — a purger against a deliberative body tracks a `denunciation_pipeline` (a pool of named Grudge-tagged targets consumed one/Accounting). When it runs out, the purger's trajectory branches into an ambiguous body-wide threat, and *that* branch auto-generates a **Coalition Purge (reusing G6)** among the body's own membership, resolved via `resolution_method: procedural-vote` (only aggregate Disposition-turn-hostile needed, no Treasury/troops, within a single Accounting) | only the `procedural-vote` value on the G6 Coalition object. **Crown Standing-6 (Inner Prince) already specifies "inner-circle majority withdraws (3 of 5 Dispositions fall below 0)" — Robespierre's CPS seat maps onto that row** | The purger is safe only while the pipeline has *other* visible targets; forced to threaten the body itself, the same uncertainty flips into a fast procedural coalition — speed (single Accounting, no army) differentiates it from G6 | clean — CPS seat maps to an existing Standing-6/7 row |

### 40.3.8 Category H — Rival factions & court bureaucracy (cross-cuts M1/M4/M5)

*Emphasizes the contested, multi-actor texture — how a rise is fought over, and how selection mechanisms
themselves get captured.*

| Entry | Mechanic | New fields / Keys | Failure dynamic | Naming |
|---|---|---|---|---|
| **H1** Fujiwara Regency Marriage Politics (Michinaga) | **Kinship Claim (bloodline chokepoint investment)** — an ambition targeting "become kin to the ruler's line" (method lawful) advancing via a multi-season Petition/Opportunity chain (courtship→dowry→betrothal→heir-birth). On threshold "install heir"/"claim regency" fires — but the reward is **not an office; it's a standing Ledger entry that keeps paying out every Accounting** as long as the kin-tie holds (Michinaga ruling via Minister of the Left) | a "Kin-of-Ruler" value under the Precedent family that persists across office changes and grants a recurring rank-independent influence bonus | A structural ceiling, not a rival — works only while the ruler *needs* the kin-tie; the ruler's own trajectory eventually offers an insei-style bypass ("rule directly, retired") that permanently zeroes ALL Kin-of-Ruler tags in that court | clean |
| **H2** Claudius's Freedman Secretariat (Pallas, Narcissus) | **Correspondence Advisor / Access Chokepoint** — a low-Standing household servant is the ruler's Correspondence Advisor; all Petition/Intrigue Keys route through them before the ruler's queue. Ambition advances by filtering/redirecting Keys (approving allies, suppressing accusers), converting no formal rank into de facto influence | Key `access.correspondence_filtered` (child, cause=the intercepted Key, payload {advisor_id, disposition: approved\|suppressed\|surfaced}) — the ambition engine has no mechanism for intercepting *other* Keys in transit; follows the `officer_deaths → standing_change` child-Key precedent | Two rival advisors each backing a different successor-designate → on succession, an automatic "patron_death → client purge" cascade: the loser's Reputation/Debt flip sign, forced Demotion within one season, no appeal; the winner gets a short decaying reprieve | **flag** — "ab epistulis"/"a rationibus" read as bureau-chief "officers" → "Correspondence Advisor"/"Household Advisor" |
| **H3** Ottoman Valide Sultan ("Sultanate of Women," Kösem) | **Contested Hereditary Slot (matrilineal reassignment)** — a Standing-6/7 "Valide"-equivalent bound not to an individual but to whichever NPC is mother/grandmother of the current ruler (per the Knots graph). On a ruler-succession Key it auto-reassigns via a relationship query rather than the Initiation Gate — but the incumbent isn't auto-displaced, so the slot **supports simultaneous rival claimants** until a Disposition/client-network contest resolves it | a "succession-bound" rank property (auto-recompute eligible claimants on succession); doesn't need the settlement ambition engine | The coup as a Disposition-network flip: the incumbent's own Confidant-level client betrays her once the rival's network crosses a Disposition threshold, while a *third* bloc stays loyal (a factional split); the coup requires the rival's controlled-Disposition sum to exceed the incumbent's by a margin | clean for "Valide" slot; the loyal client ("Chief Black Eunuch") → "Household Advisor"/"Chamberlain" |
| **H4** Wei Zhongxian's eunuch faction vs the Donglin Academy | **Patron-Bound Purge Ambition** — a Court Advisor's ambition (goal "purge rival ideological faction," method lawful→violent) advances by **weaponizing the existing Demotion Magnitude system** — manufacturing false-accusation Keys forcing Severe/Total demotions on targets who did nothing under normal rules | `patron_bound: true` flag on the ambition object + a `standing_change.forced` (or `cause: false_accusation`) variant so appeal mechanics differ for a fabricated trigger — the one entry mapping onto an *already-built* resolver (Demotion) being *abused* | The `patron_bound` flag *is* the failure — on the patron's death, a short countdown, then the successor's own trajectory reverses every forced demotion and applies Total Dismissal to the advisor, no appeal. Self-terminating on succession | "Directorate of Ceremonial" reads as "officer" → "Court Advisor"/"Palace Advisor" |
| **H5** Thomas Cromwell's patronage rise & faction fall | **Indispensable Processor + Attainder Bypass** — an advisor's ambition (goal "become indispensable at processing the ruler's transactions"; method administrative) advances by resolving Mandate/Petition Keys, each success writing Reputation/Debt tags on beneficiary clients (a Knots patronage network). Destruction bypasses the normal appeal path | an "Attainder Bypass" sub-case on §1.0a's Total tier that explicitly **skips the 2-season appeal** (no trial, resolved in one scene when a rival feeds the ruler a personal grievance) | The processor has no hereditary/institutional floor — a rival uses the *same* marriage-introduction lever to manufacture a personal-grievance Intrigue Key triggering Attainder Bypass in one scene. **Years of positive Ledger tags provide zero defense** | clean — "Privy Seal"/"Chief Advisor" |
| **H6** Cosimo de' Medici's shadow patronage rule | **Slate Control (selection-mechanism capture)** — rather than climbing, this ambition (goal "capture the appointment/selection mechanism itself"; method lawful→covert) targets the resolver that generates candidate slates (the Provincial Authority Directive generator, or a settlement's Rival Cohort pre-emption roll) — on payoff, a hidden `selection_bias` weighting so a formally-neutral process reliably outputs the faction's people, *without holding the office* | `selection_bias` on whatever resolver generates candidate slates — **the one pattern fitting neither the ambition payoff types (claim/betray/expose) nor the ladder advancement types**; needs a new hook in the Directive-generation logic or Rival Cohort assignment, gated behind ambition progress | Symmetric and reversible — whoever holds `selection_bias` can have it seized by a rival the moment they're structurally vulnerable (Albizzi's 1433 exile of Cosimo, reversed a year later using the identical lever). A single ownership pointer flipped in one Coup Key | clean; the captured body ("accoppiatori") → "Selectors"/"the Slate" |
| **H7** Heshen's monopoly on access under Qianlong | **Plural Advisor Stacking** — one NPC accumulates MULTIPLE concurrent advisor roles (info gatekeeper + fiscal controller + appointment-vetter), each unremarkable but combining into a monopoly, plus a **decaying-ruler-attention multiplier** (illicit-gain rate scales with the ruler's Disposition/attention decline) | (1) `concurrent_roles: []` array (the engine is single-goal today); (2) a **hidden visibility flag** on Debt/Grudge tags (embezzlement concealed until an `audit_exposed` reveal Key) | The growth multiplier inverts at succession — the new ruler was structurally excluded from the access network, so on succession auto-fire `audit_exposed`, converting hidden Debt to public Grudge/Reputation overnight → Total Dismissal. The concealment provides zero defense once the succession Key flips visibility | **explicit flag** — "Grand Minister"/"Chief Officer" collides hardest → "Plural Advisor"/"Court Patron" |
| **H8** Shah Abbas I's Ghulam counter-faction vs the Qizilbash | **Power-Base Tagging (dependent-client counter-faction)** — a *ruler-initiated* counter-mechanic: when a bloc derives power from an independent base (land/hereditary office/tribe), the ruler's ambition seeds and promotes a rival cohort explicitly tagged as having **no independent base** (only personal favor), filling the same slots. Their total dependency is the design intent (they can't credibly defect) | `power_base` field {independent \| favor-dependent} — nothing today distinguishes whether a Dismissal actually removes power or just a title; consumed by the §1.0a Demotion resolver (gates whether a Dismissal is *enforceable*) | Generational drift — `power_base` slowly drifts favor-dependent → independent over successions as the cohort accumulates its own client networks; a periodic recheck nudges it independent, so a *second* counter-faction eventually becomes necessary. The fix decays into the problem it solved | clean — "ghulam" = "Retinue"/"Household Client" |
| **H9** The Day of the Dupes — Richelieu vs Marie de Médicis | **Unwitnessed Promise / Audience Race** — a ruler's private unwitnessed decision to dismiss an advisor is modeled NOT as an immediate Demotion Key but as a **rumor-stage Intrigue card — reversible until ratified.** During a short **Commitment Window**, the threatened advisor can contest a race for the next physical audience (a Speed/social contest) to reverse it. Any OTHER NPC who publicly commits Disposition to the rumored winner during the window gets flagged | a "Premature Commitment"/"Exposed" tag (under Grudge); a scene-level "Commitment Window" timer; a new scene-trigger: rumor card → Commitment Window → contested Audience-Race → real `state.standing_change` only at window close | The rival's failure IS the mechanic — they read the rumor as ratified and publicly commit before the race resolves; when the incumbent wins, every committer gets "Premature Commitment" and becomes a valid purge target (Marillac's arrest, Marie's exile). The rewarded variable is **speed-of-access after the vulnerable moment** | clean |

### 40.3.9 Category I — Venality of office (M6 spine)

*Rise via purchase — of rank, heritability, toll-posts, or plural holds; fall via no-loyalty-reserve,
prestige devaluation, or reform under crisis. Directly implicates the needs_jordan "how many parallel
wealth-tracks" question (BYZ-2 was cut for exactly this).*

| Entry | Mechanic | New fields / Keys | Failure dynamic | Naming |
|---|---|---|---|---|
| **I1** Auction of the Roman throne — Didius Julianus | **Garrison Auction — kingmaker bidding for vacant Leadership** — when Leadership vacates non-institutionally while a Standing-6+ NPC commands the core Retinue, open a Crisis card: two+ Standing-5+ NPCs (or the player) bid Treasury in escalating rounds directly to the Retinue-commander; highest bid wins instant elevation same-Accounting, bypassing Initiation Gate/Deeds | `purchased_legitimacy` boolean on the Leadership-holder (suppresses the accrued-loyalty buffer against Coup Counter); reuses `standing_change` via `cause="garrison_auction"`; a **third** succession path alongside institutional (SUC-01–03) and dynastic (LIN-01–04). **Distinct from HAB-2 — do NOT merge** | `purchased_legitimacy` means the next Standing-5+ Retinue-commander with *genuine* Disposition ≥0 among the rank-and-file gets an auto-favored Coup Counter roll within ~2 Accountings (Severus's march) | do not call the armed body's members "officers" → "Retinue"/"Guard cadre"/"Retinue-commanding NPC" |
| **I2** Verres's Sicilian governorship | **Extraction-Debt Ledger tag + delayed Exposure Key** — an NPC who buys office starts with a hidden Debt tag sized to the bribe; resolving Obligations by converting the office's extractive verbs (Levy/Tax) to personal Treasury pays it down but increments a paired hidden **Exposure** counter. If a rival/player spends an Investigate within a post-term audit window, roll against Exposure → exposure Key → Severe Demotion + clawback | a paired hidden `Exposure` counter (distinct from Debt face value); extends **HRE-4 Borrow**; pairs the audit window with **SE-7's Residencia**; Key `state.extraction_exposed` (child `state.standing_change`) | A timing race, not guaranteed escape — success is proportional to the rival's *actual prosecution investment* (Cicero's 50-day evidence tour), not automatic detection. Absent a willing rival, the Debt resolves clean | clean |
| **I3** The Paulette — hereditary venality in France | **Droit Annuel — heritable-rank upkeep fee** — a purchased rank gains an optional `heritable` flag, bought for an ongoing per-Accounting Treasury fee. While current, the holder's death passes the rank to a named heir bypassing the Initiation Gate; a missed payment lapses heritability (grace period) back to non-heritable | `heritable: bool` + `droit_annuel_due` cost field; heir pointer reuses the Knots graph. **The exact concern BYZ-2 Purchased Dignity was CUT for (needs_jordan item 3) — more surgical than BYZ-2** | Institutional: a faction-scoped Precedent tag increments per heritable transfer; at threshold any leader attempt to claw back heritable ranks (HAB-6 Crush the Estates) suffers an escalating Legitimacy/Coup-Counter penalty — the robe-class becomes a check the leader created and can't freely undo (the Fronde) | clean |
| **I4** Renaissance papal venal offices | **Chokepoint Seat — purchased toll-post** — an NPC buys a newly-manufactured, purely-administrative Seat sitting athwart a named Key-emission pathway (e.g. all Petitions routed through Hold Court). Every other actor's action through that pathway pays a toll (AP/Treasury) credited to the Seat-holder before resolving | the Chokepoint Seat as a lightweight purchasable entity (pinned to a pathway, owner pointer, toll rate); Key `state.toll_extraction`. **No item in the 44 covers this — genuinely new gap** (HAB-7 is petitioner-initiated friction, not a passive toll on unrelated actors) | Maximally vulnerable to legislative removal once visible — each `toll_extraction` increments a faction-wide Reform Pressure counter (reuse the Π homeostat); at threshold a Crisis card offers the leader a one-time "Abolish the Seat" (no refund, permanent Grudge) | not "chokepoint officer" → "Seat"/"Toll-Post" |
| **I5** Albrecht of Brandenburg's purchase of Mainz | **Patron-Financed Plural Hold** — an NPC holds Standing in a SECOND faction/ladder simultaneously if a Financier (reuse HRE-4) fronts the dispensation cost, creating a Debt-Service Obligation tag that **biases the indebted NPC's trajectory** toward whichever move maximizes Treasury flow to the Financier — even against their own stated `ambition.goal` | a `debt_service_priority` weight on trajectory; **holding Standing in two ladders at once may need a multiplicity flag if the schema assumes single-faction Standing per NPC — the biggest new-field risk in the batch**; extends **HRE-4 Borrow** with pluralism | A **contagion** failure, not merit — if the Financier's own Standing/solvency collapses independently, the Debt-Service tag converts instantly to a Demotion-Magnitude-2 (Severe) on the indebted NPC regardless of conduct (the Fuggers' exposure) | the compelled downstream action (indulgence-drive equivalent) → a "Mandate," not an "officer directive" |
| **I6** Venice's sale of nobility (case nuove) | **Emergency Rank Buy-In** — during a Treasury-shortfall Crisis, leadership may open a one-time, non-recurring option to sell direct entry into a normally-closed tier for a large lump payment, bypassing the Initiation Gate. Distinct from I3 (single crisis-triggered lateral admission, not recurring heritability) | none structurally — reuses `standing_change` + a persistent, never-fully-decaying "New-Money"/"Case-Nuove" Reputation sub-tag modulating Disposition against legacy-rank NPCs; settlement/faction-scale sibling of **FA-JP2 Recognition fork** | Social, not institutional — legacy-rank Disposition toward case-nuove NPCs starts at a permanent floor penalty unless the buyer completes a marriage-alliance Knot with a legacy family; absent that, legally equal but mechanically excluded from inner-circle Mandate assignments (a *designed* exclusion) | clean |
| **I7** Purchase of commissions in the British Army | **Retinue-Command Purchase Schedule + Rank Sale** — a formal faction-published price schedule for purchasing INTO a Standing rank carrying **retinue-command authority**, scaled by the specific warband's prestige tier. Paired with a secondary-market Rank Sale — an existing holder sells their slot to a chosen buyer (subject to Standing-6+ approval) instead of it opening on death | a per-Retinue prestige-tier price modifier; a `rank_sale` transaction record; Key `state.rank_sale` (buyer, seller, price, approving authority — two-party, unlike `standing_change`); reform hooks the HAB-6 ladder-amendment lever | Reform requires two conjoined preconditions: (1) a legitimizing Crisis Key (a battlefield disaster making incompetence-cost visible) + (2) a Leadership-only prerogative override rewriting the Schedule *without* normal council ratification, at a one-time Legitimacy cost (Gladstone's Royal Warrant bypassing the Lords) | **LOUDEST FLAG IN THE CORPUS** — literally buying military command rank. Never "commission"/"officer"/"commanding officer" → "Retinue-Command rank"/"warband command slot"/"muster-command Standing." Cross-reference `mass_battle_v30`: the purchased Standing *qualifies its holder to be ASSIGNED a Retinue*; it is NOT the auto-generated in-battle commander role |
| **I8** Qing juanna sale of titles/offices | **Juanna Track — floating-rate purchase promotion** — a second, purchase-based path running alongside **CHN-2's Imperial Examination Ladder**. The Treasury cost of a rank-jump floats each Accounting via a formula off the faction's fiscal-pressure state (reuse the Π homeostat retargeted at deficit) | a computed `juanna_rate` (a formula, not a new resource). **The explicit missing "purchase" half of the CHN-2 decision (needs_jordan item 3) — present as CHN-2's paired purchase answer, not standalone.** Writes an existing Grudge tag applied *collectively* to the exam cohort per juanna promotion (reusing CHN-9 Kaochengfa's pattern) | Prestige-devaluation, not individual collapse — each juanna promotion increments the collective exam-cohort Grudge; at a faction-wide threshold, exam-track Obligation tolerance tightens + a faction Legitimacy penalty to future Directives | any purchase-track title must reuse existing Standing-N vocabulary, not invent a "purchased officer" title |
| **I9** Spanish Habsburg sale of colonial offices (beneficio de oficios) | **Distance-Discounted Office Price + Self-Audit Capture** — extends **SE-7 Residencia/Visita**: (a) purchase price scales inversely with distance from the capital while the same distance penalizes the Residencia detection roll; (b) a buyer may spend extra Treasury to seat an allied NPC on the reviewing tribunal (Self-Audit Capture), further reducing detection | `distance_price_modifier`/`distance_audit_penalty` (formulas over existing distance data); tribunal-ally link reuses Knots; a sixth instrument on the S-2 Governor-Oversight Toolkit | Madrid's own check was corruptible — Self-Audit Capture only shifts probability. A rival with sufficient Investigate can surface the *captured-tribunal arrangement itself* as a second-order exposure Key, triggering a **compounded** Demotion (extraction + capture = separate triggers). Each layer of capture is itself discoverable | clean |
| **I10** Ottoman malikane lifetime tax-farm auctions | **Lifetime Grant Auction + De-Facto-Heritability Entrenchment Race** — a short-leash annually-re-auctioned revenue-claim (reuse **BYZ-7 Pronoia**) converts, via a large upfront payment, to a lifetime grant. The state never formally grants heritability (distinct from I3), but each Accounting the holder's *family* accrues an **Entrenchment** tick (0–5 progress pattern at family/lineage scale) via patronage/marriage. Reclaiming before threshold is clean; after, it fires a Rebellion-risk Crisis card | a family/lineage-scoped Entrenchment counter (nothing tracks multi-generational accrual) + the before/after-threshold reclaim branch; extends BYZ-7. **The clearest candidate for extending the ambition engine UPWARD — but needs only Accounting-cadence ticking + the Knots graph, so NOT gated on the unbuilt settlement registry** | The center's reclaim window is the mechanic — intervention cost rises monotonically with Entrenchment while local leverage rises in lockstep, so delay past threshold converts every future reclaim from administrative to military/Crisis. Early intervention still wins cleanly | clean |

### 40.3.10 Category J — Religious / ideological authority (M8 spine)

*Rise via Standing-independent legitimacy — prophetic, jurisprudential, credentialing-body, cross-ladder
co-signature. Fall only by counter-authority in the same currency, or covert violence. Most directly
demands the peninsula-scale aggregation gap.*

| Entry | Mechanic | New fields / Keys | Failure dynamic | Naming |
|---|---|---|---|---|
| **J1** Investiture Controversy — Gregory VII vs Henry IV | **Investiture Gate (cross-ladder co-signature)** — any secular promotion at Court-Attendance tier (Standing 4+) or any Standing 6–7 succession requires a **co-sign Key from a qualifying religious-ladder NPC (Church Standing 5+)** before resolving. Withheld → `invested_status = Uninvested`: subordinate loyalty tags flagged breakable, each subordinate's trajectory gains an "oath released → back a rival" branch. Granting later retroactively clears it | `invested_status` {invested \| uninvested \| contested}; `co_signer_id`/`co_sign_status` payload on succession/standing_change; Key `state.investiture_ruling`. **Complements BYZ-1** (adds a co-signature gate *between* two ladders) | Decades of back-and-forth — model Uninvested with a renewal/decay cycle and give the secular ruler an antipope counter-lever: sponsor a rival claimant up the *same* religious ladder for a competing co-sign, splitting the religious ladder into two legitimacy-granting tracks | clean |
| **J2** Savonarola's theocratic interregnum | **Prophetic Mandate (zero-Standing moral-authority track)** — an NPC can hold Standing 0 on every ladder yet run a full ambition (goal "set the moral-political agenda," method preaching) whose progress is driven by accumulated public `scene.witness`/`scene.gossip` Keys crossing a threshold, converting into a Standing-independent **`moral_authority` (0–5)** that substitutes for Standing in Hold Court agenda-setting branches | `moral_authority` (decoupled from Standing) + a rule that court-scene gates accept it as an alternate qualifying score | Fragile with no office to entrench — two *both-required* levers: (1) an EXTERNAL rival religious Standing-holder emits a delegitimizing (excommunication-style) Key zeroing `moral_authority`; (2) a DOMESTIC secular Rival Cohort supplies the actual removal. Neither alone suffices | clean |
| **J3** Cardinal Cisneros | **Cross-ladder ambition chaining into emergency succession** — `ambition.goal` extended to name a **chain of intermediate offices across a DIFFERENT faction's ladder** before a secular target (e.g. "become Regent," chain [confessor → Church Standing 3 → Cardinal]); the terminal step fires only when a `state.succession` opens with `succession_mode=emergency` and checks the NPC's independent revenue + coercive access (their religious rank) rather than prior secular Standing | `ambition.goal` needs a `ladder_chain` list (cross-faction) — **the least-new-mechanics entry** | Cisneros did NOT fall — a durable **standing tension**: nobility Grudge accrues at an elevated rate but **cannot be bought off** through the normal favor-economy (the power base is orthogonal to secular patronage). Model these Grudge tags as **non-negotiable**, never forcing a Demotion | clean |
| **J4** Rasputin (ideological view) | **Backchannel Confidant (Disposition-as-Standing substitute)** — a Standing-0 NPC gains a formal advisory **veto** over others' ambition/appointment resolutions, gated purely on an extreme Disposition with one inner-circle NPC (originating from a private-crisis scene emitting a `meta.miraculous_event` Key). That single high-Disposition relationship reads, in specific court-decision resolutions, as if it were a Standing rank | not a field — a rule flag on specific court-decision resolvers permitting Disposition-with-inner-circle to substitute for Standing; add an OR-branch on appointment Keys | No formal removal exists for a Standing-0 actor — Demotion Magnitude has no purchase. The only lever for rivals is escalating directly from a Grudge tag to a covert/violent DA (`da.covert_betrayal`) — assassination, not dismissal | **explicit flag** — "Confidant"/"Backchannel Advisor," never "officer" |
| **J5** Ottoman Şeyhülislam deposition fatwas | **Sanctioning Prelate (required co-signer on coup)** — the top rank of a religious ladder holds a unique capability: any `state.coup_attempted` against the sitting secular leader must carry a `sanctioned=true` flag sourced from this NPC to have any chance of `outcome=success`; without it the coup auto-fails regardless of military Standing/troops. The office is appointive and revocable by the ruler it may be asked to depose (a Patron relationship, reusing **CHN-9**) | `sanctioned` (bool) + `sanctioning_npc_id` payload on `coup_attempted`; reads `moral_authority` (J2) if the Prelate cultivated an independent preacher base | Double bind — the ruler can pre-emptively dismiss the Prelate before a hostile fatwa (patron-bound lapse). The check on that counter-move is the Prelate's independent `moral_authority`: dismissal succeeds automatically only below a threshold; above it, dismissal itself triggers a destabilization event | mild caution — avoid "Court Officer" → "Sanctioning Prelate" |
| **J6** Tobacco Protest fatwa & the Shia marja'iyya | **Jurisprudential Renown (peninsula-scale non-appointive prestige ladder)** — a wholly separate track from the 0–7 Standing ladder: a scholarly NPC accrues **`renown`**, peninsula-scoped and aggregated across MANY settlements' teaching/doctrine scenes (summed `scene.witness`/`scene.gossip` from settlements the NPC never administers). Nobody can appoint or revoke onto this track — only peer jurisprudential contest. At high Renown the NPC can emit a policy-override ruling superseding a standing Directive at mass/peninsula scale | `renown` (peninsula-scoped aggregate) — **the entry that most directly demands extending the settlement-scale ambition engine to a peninsula-wide aggregate**; Key `state.doctrinal_ruling` (scale_signature [peninsula], persistent; payload ruling_npc_id, renown_at_issue, target_policy_id, compliance_magnitude) | Cannot be co-opted by office or bought off — only outcompeted in its own currency. The only check on a `doctrinal_ruling` is a rival on the SAME Renown track issuing a counter-ruling, resolved as a Standard/Social Contest between the two Renown scores | clean |
| **J7** The Fifth Dalai Lama & the Ganden Phodrang | **Institutional-Search succession + Patron-Client legitimation exchange** — (a) `state.succession` gains `succession_mode=institutional_search` where `new_leader_id` is chosen by the religious establishment (a Desi/regent), who can **artificially DELAY** emitting the Key past the incumbent's actual death (a concealment window). (b) A patron-client Key (modeled on `da.diplomatic_alliance`) exchanges an external faction's military force for the religious leader's legitimation, converting the religious Standing-7 leader into the discrete Leadership state | `institutional_search` enum value + a `concealment_duration` payload; a new `da.diplomatic_alliance` instance | The concealment window is the fragility — give it a decay clock. If a rival/foreign patron obtains a `scene.witness`/`scene.gossip` Key exposing the concealment before the preferred candidate is ready, `succession_mode` retroactively flips to `contested`, applying a legitimacy penalty and opening a Rival Cohort challenge | clean — "Regent"/"Desi" |
| **J8** Calvin's Consistory in Geneva | **Discipline Board — externally-sourced civic-eligibility gate** — a standing body (one religious NPC + co-opted lay Standing-holders) controls a boolean `civic_eligible` flag on OTHER NPCs and the player. Losing it zeroes ability to hold/advance ANY secular Standing rank regardless of secular progress — the gate is **external to the ladder it constrains** | `civic_eligible` cross-cutting flag (checked by any secular 0→1 advancement) + a `gate_authority_id` payload on `standing_change`; proposes a general **"Cross-Ladder Gate" primitive shared with J1 and J9** | The Board has no independent coercive power — durability depends entirely on packing the secular council with sympathizers. A periodic Gate Renewal check keyed to the sympathetic/hostile fraction of secular Standing-holders; a hostile majority can legislate the gate away | mild — avoid "officers of the Consistory" → "elders"/"lay wardens" |
| **J9** Church-membership franchise gate in Massachusetts Bay | **Franchise Prerequisite — hard-coded cross-ladder rule** — the more extreme, non-discretionary sibling of J8: instead of a capture-maintained flag, a faction's Standing 0→1 Initiation Gate *definition itself* is authored to require a specific Standing threshold on a DIFFERENT faction's ladder as a formal rule (a design-table change, not a runtime Key) | a `franchise_prerequisite_ladder`/`franchise_prerequisite_rank` column on rank-ladder tables — **needs a design-doc-level table change, not just a runtime mechanic** | Challenged from WITHIN the gating religious ladder — a rival theological track allies with a high-secular-Standing sympathizer; the orthodox gate-holders must win a secular leadership election (J8's council-packing) to expel the challenger before the franchise rule comes under threat | clean |
| **J10** Donglin Academy vs the eunuch Wei Zhongxian | **Lineage-tagged ambition clustering vs Backchannel-plus-covert-apparatus purge** — (a) NPCs sharing a `lineage_id` tag (teacher-student/exam-cohort ties, on the Knots graph) get a coordination bonus — when multiple lineage-tagged NPCs' ambitions target correlated appointments, each advances faster. (b) The rival pattern is J4's Confidant PLUS an existing covert-faction apparatus (Niflhel/RM per the Investigate verb) issuing a MASS purge — many `da.covert_betrayal` + Standing-drops against the entire cluster at once | `lineage_id` (denotes shared-credential coordination, not personal Disposition) + a batch/cascading Demotion wrapper Key firing N child `standing_change` against every `lineage_id` member (analogous to the `officer_deaths → standing_change` fan-out); Key `state.faction_purge` (payload faction_id, target_lineage_id, cause) | Wei's own power is precarious — entirely Confidant-pattern (J4), no formal office. On `state.succession`, the Confidant relationship does NOT transfer — an automatic re-roll/decay of the Disposition-substitute veto on any succession event (Wei's apparatus collapsed within months of Tianqi's death) | **explicit flag** — the coercive apparatus (Eastern-Depot analog) must not be an "officer corps" → "covert apparatus"/"Niflhel-analog retinue" |

---

## 40.4 Cross-reference against the 44 comparative-governance proposals (research §4)

For each proposal this research touches: **ABSORB** (the general mechanic subsumes it as an instance),
**EXTEND** (this research adds a refinement to author alongside it), or **TENSION** (a conflict, with
resolution). Feeds the in-flight pessimist-NERS audit of the 44. All **PROPOSED**.

| Proposal | Verdict | Detail |
|---|---|---|
| **HAB-2 (Valido)** | **EXTEND (heavily) — land it** | The single most-referenced proposal (D1, D5, D6, D7, C2). Supplies three concrete amendments: **proxy-intimacy + Regency Window** (D1), **multi-member Patronage Web with intra-Web fracture** (`web_id`, D5), **the `web_institutionalized` escape valve answering needs_jordan Q3** (D6), and **heir-banking succession insurance via HRE-2** (D7). C2 feeds a marriage-supply on-ramp. HAB-2 becomes the canonical `power_base=patronage/favor` instance |
| **CHN-9 (Kaochengfa)** | **ABSORB as a core primitive** | The patron-bound auto-lapse (landed ED-FA-0021) is the reusable engine for M1's top-down collapse. Referenced by D3, D4, G3, H4, J5, A9. G3 (kul escheat) and D3 (reign-bound cohort) are CHN-9 *variants*, not parallel systems |
| **FA-JP2 (Recognition fork)** | **EXTEND** | A3 (Gate Capture) and A9 (Cohort Capture) ride FA-JP2's Confirm/New-Grant adjudication as a *shadow-adjudicator layer*; I6 (case nuove) is a settlement-scale sibling. Extend FA-JP2 with a "who adjudicates the fork" capture surface |
| **HRE-2 (Chapter Capture)** | **ABSORB as the banking primitive** | Pre-vacancy investment under timing uncertainty. F2 (Carolingian hereditary lock) is HRE-2 territory; D7 makes HRE-2 the template for a Favorite's succession insurance; C1 and I10 are the same banking shape |
| **BYZ-1 (Office/Dignity split)** | **ABSORB as substrate** | The sticky-Dignity-vs-revocable-Office split is the substrate many entries need: D8, D10, G7, J1. Land BYZ-1 as the two-track rank substrate; the auxiliary meters plug into its Dignity half |
| **BYZ-8 (Oath-Bound Administrator)** | **ABSORB — this research supplies its implementation surface** | D9 (Basil Lekapenos) is BYZ-8's *direct real-world precedent* (multi-reign persistence + Personal-Rule-Assumption demotion). C3 (`succession_eligible=false`) and G7 (`succession_immune` + `rule_without_regent`) are BYZ-8's mechanical core. F4 is BYZ-8-adjacent. **Consolidate C3/D9/G7 into BYZ-8** |
| **CHN-2 (Imperial Examination Ladder)** | **EXTEND — supply the missing purchase half** | B2/B3 author its merit mechanics; I8 (juanna) is **the explicit missing "purchase" half of the CHN-2 needs_jordan decision** — present together. A4 (Köprülü) is a rival funnel competing for 1–2 vacancies |
| **CHN-7 (Chancellery Gatekeeper)** | **ABSORB — author once as a shared primitive** | D2, D8, H2/H3 all converge on it. D8 explicitly flags CHN-7 and D8's Gatekeeper should be one primitive. The `access_monopoly`/`gatekeeper` fields ARE CHN-7 generalized |
| **CHN-8 (Institutional Purge, Bloc)** | **ABSORB — reuse verbatim for the failure side** | A4, A9, D3 name CHN-8 as the mass-demotion mechanism for a patron-bound cohort. It is the `coalition_purge`/bloc-fan-out failure primitive |
| **IT-8 (Upstart tag)** | **EXTEND** | D10 extends IT-8 (landed ED-FA-0022) from Guild-mastership to the general ladder as the `standing_source=upstart` provenance marker |
| **FA-JP4 (Knot / hostage-kin)** | **ABSORB as substrate** | D5's Web binding and F9's compulsory-hostage bond ride FA-JP4's Knot machinery (landed ED-FA-0020). The `bond.*` edges are FA-JP4 extended |
| **HRE-4 (Borrow)** | **EXTEND** | I2 (Verres) makes debt self-financed through the office's own extraction; I5 (Albrecht) adds pluralism. Both author alongside HRE-4 |
| **BYZ-7 (Pronoia)** | **EXTEND** | I10 (malikane) is BYZ-7's lifetime-tenure auctioned variant; shares fixed-term-lock substrate with HAB-5/SE-JP2 |
| **SE-7 (Residencia/Visita)** | **EXTEND** | I2 pairs the audit window with it; I9 (distance-discount + self-audit capture) is a sixth instrument on the S-2 Governor-Oversight Toolkit |
| **HAB-6 (Crush the Estates)** | **ABSORB as the reform lever** | I3 and I7 both hook HAB-6's irreversible ladder-gate-rewrite lever for their reform paths |
| **HAB-7 (Ordenanza Ratification)** | **ABSORB** | A3 and A6's strip-the-chokepoint petitions ride HAB-7's petitioner-initiated friction pattern |

**TENSION — one real one, and its resolution:** the recurring pressure toward **parallel-track
proliferation.** BYZ-2 was cut for adding a third wealth-track; I3 (Paulette), I8 (juanna), and the
D-series favorite tracks all risk re-introducing the same sprawl, and needs_jordan item 3 ("how many
parallel status/power tracks") is unresolved. **Resolution: §40.2.2's "one shared ladder + a bounded,
named set of auxiliary meters" is the disciplined answer.** The auxiliary meters (`moral_authority`,
`renown`, `shadow_standing`, `service_rank`, `Dignity`, `custody_bonus`) are *not* parallel ladders —
they are scalar pressures on the one shared ladder that either substitute-in at specific gates or force
ratification at a threshold. This lets HAB-2, BYZ-1, and the venality tracks all coexist as *typed
auxiliary meters* rather than competing seat-spaces.

**One clean non-merge to preserve:** I1 (Garrison Auction) is a *one-shot vacancy auction*, explicitly
**distinct from HAB-2's sustained track** — do NOT fold it into the HAB-2/BYZ-1 parallel-track
decision. And I4 (purchased toll-post Chokepoint Seat) is flagged as a **genuinely new gap not covered
by any of the 44** — closest analog HAB-7 is petitioner-initiated friction, not a passive toll on
unrelated actors.

---

## 40.5 Open decisions — what needs a Jordan ruling (research §5)

### 40.5.1 The one design-taste ruling (not a research question)

- **Can an NPC actually DEPOSE or SUPERSEDE the player at a rank the player holds?** §40.2.2 recommends
  shared rank space, which *architecturally permits* this. It is the sharpest "every action pays what
  it buys" stakes question in the design: if the answer is *no*, NPC advancement is partly a sandbox
  the player watches; if *yes*, the player's own consolidation writes the same legible vulnerability
  every NPC's does (the purest expression of Ω-d non-dominance). **The architecture supports both via a
  single `player_seats_are_contestable` toggle — this needs Jordan's taste, not more historical
  cases.** *Research inclination:* yes, but gated behind the *coalition* threshold (E8/G6), so the
  player is only deposable when they have over-consolidated past the point where ordinary challenges
  bind — making the fall *earned and legible*, never a coin-flip.

### 40.5.2 Genuine architectural gaps (new mechanics, not reskins) — flag before building

1. **Lineage/clan-scope objects above the NPC lifespan.** C5 (Wang Mang, `dynastic_leverage` across
   five reigns) and I10 (family `Entrenchment`) need an entity the Accounting-cascade tick operates on
   *above* a single NPC — "the single biggest structural ask of this batch." Recommend the
   `scale_binding=lineage` profile (§40.2.1), which I10 shows is *not* registry-gated. But whether
   Valoria wants clan-scale actors at all is a scope call.
2. **The joint / Coalition ambition structure.** G6/G9 need a multi-NPC joint ambition object —
   "ambitions today are strictly per-NPC; this is the clearest new-mechanic requirement." E8's
   `purge_cascade` supermajority coalition is the same primitive. Genuinely new and load-bearing for
   the entire downfall side.
3. **Peninsula-scale aggregation** (`renown`, J6) — the exact gap named in the system context.
   `state.doctrinal_ruling` needs to sum `scene.witness`/`scene.gossip` across settlements an NPC never
   administers.
4. **Mandate separable-from-possession** (F7, `custodian_id` ≠ `holder_id`) — "the sharpest genuine
   architectural gap of the ten."
5. **In-transit Key interception** (H2, `access.correspondence_filtered`) — the engine has no
   mechanism for one NPC intercepting *other* NPCs' Keys before they resolve; every chokepoint entry
   needs it.
6. **Dormant/conditional tags** (G4, `trigger_condition: succession`) and **hidden-visibility tags**
   (H7) — genuinely new tag-family capabilities.
7. **A co_leadership / partial-Leadership state** (C8) and **mutable office `succession_rule`** (F2) —
   Part 2's succession model currently treats Leadership as binary and offices as static slots.

### 40.5.3 Thin spots / fact-check caveats (do not over-trust)

- **B6 (Napoleon / Légion d'Honneur):** the Cambridge Core article title/existence are confirmed, but
  the "carrière ouverte aux talents" attribution and the specific meritocracy quote were **not
  independently re-verified verbatim** — treat the Dual-Track mechanic as sound but the exact sourcing
  as advisory.
- **B7 (Northcote–Trevelyan):** the Queen Victoria hostility quote and 1855/1870 timeline were
  confirmed via general historical search, not a primary document — the ~16-year multi-cycle-conversion
  timing is a reasonable model, not a hard citation.
- **B8 (Prussian Referendar):** the 1755/1770 exam dates come from multiple secondary sources via
  general search — fine for a game mechanic, thin for a claim of precision.
- **A1 (Cicero patronus):** cited to an Edinburgh PhD thesis (Avesani) plus encyclopedic sources — the
  mechanic is well-grounded but leans on tertiary framing.
- **F9 (Mongol keshig):** flagged in the research as having **no clean historical reversal within the
  paradigm period** — its downfall mechanic ("slow-burn calcification into F3's `corps.entrenchment`")
  is an *inferred* extrapolation, not an attested event. The least empirically anchored failure dynamic
  in the corpus.
- **C10 / I6 (Venice) and J-series closed-oligarchy gates** are flagged **speculative pending a
  Venice-style faction actually being authored** — do not build the `marriage_registered` registry
  object until that faction exists.

### 40.5.4 What is settled and what remains

- The research pass appears to have **already fact-culled** — every surviving entry carries a real
  citation, and the two "existence confirmed, quote not verbatim" flags (B6, B7) are self-disclosed.
  No entries survived on fabricated sourcing.
- **No entry supplies a settlement-registry substitute** — the registry that gates the
  *settlement-scale* ambition engine remains unbuilt; while §40.2.1/I10 show the *court and lineage*
  bindings can ship without it, the settlement binding is still blocked. That is an infrastructure
  dependency, not a research gap.
- **What needs no more research:** the eight mechanisms (M1–M8) are saturated — 96 cases converge
  cleanly onto them, and every one maps onto reused engine fields plus a small enumerated set of new
  ones. Both the rise side and the failure side are thoroughly specified. **The remaining work is
  design-taste rulings and architecture decisions (§40.2, §40.5.1–2, the deposition toggle), not
  further historical distillation.**

### 40.5.5 Continuity routing

PROPOSAL-status; routes to `handoffs/HANDOFF_FA.md` (faction actions), cross-linking
`HANDOFF_PC.md`/`HANDOFF_MB.md` for the naming-collision boundary with mass-battle. Load-bearing
follow-ups:

1. **Jordan ruling:** the `player_seats_are_contestable` toggle (§40.5.1) and needs_jordan item 3
   (parallel-track count — §40.4 offers the resolution).
2. **ID allocation:** if this lands, allocate lane-tagged `ED-FA-NNNN` items per §40.2.3's new
   fields/Keys (read `references/id_reservations.yaml` `next_free`, allocate, bump, co-commit — never
   max+1).
3. **Author the naming callout inline** at the F10 (Yuan Shikai) and I7 (commission-purchase) mechanic
   definitions, per the research's own recommendation — not only in the audit.
4. **Feed the pessimist-NERS audit** of the 44 with §40.4's ABSORB/EXTEND/TENSION verdicts, especially
   the parallel-track-proliferation TENSION and its resolution.
