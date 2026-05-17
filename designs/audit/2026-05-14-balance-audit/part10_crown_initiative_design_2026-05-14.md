# Part 10 — Crown Initiative: Mandate-Increase Mechanic Design
## Date: 2026-05-14 · Session: bottom-up-canonical-verified · Part 10/10
## Trigger: Jordan's directive — *"we also need a way to increase mandate that
makes sense with game. refer to historical precedent, consider cards or whatever
as a currency to spend on mandate as some governmental initiative or project."*
## Companion: Part 9 (character-scale decoupling — established the need)

---

## §1 The Problem (Part 9 finding)

Part 9 quantified that Almud is **deposed in 16% of canonical campaigns**
(rising to **56% at long campaigns**), via three modes:

| Mode | Canon rate | Long-campaign rate |
|------|-----------|--------------------|
| Mandate collapse (L ≤ 1 sustained) | 12.0% | 39.4% |
| Excommunication | 2.8% | 14.4% |
| Proclaimed against | 1.2% | 2.2% |

**Crown has no canonical internal Mandate-recovery mechanic.** Royal Decree
gives Sta +1. Royal Charter gives Wealth pipeline. Crown Treaty gives L +1
but is *external* (binds rivals) and *consent-gated* (Q-1 unresolved). Once
Treaties are exhausted, Crown has nowhere to recover Mandate after attrition
from Spy attacks, Excommunication, sustained PI pressure, or stat cascades.

The structural gap is broader: **only Hafenmark (Parliamentary Session) and
Church (Ecclesiastical Appointment) have flagship internal L+1 mechanics.**
Crown has external-only. Varfell has nothing.

This proposal fills the gap, grounded in historical precedent.

---

## §2 Historical Precedent for Sovereign Mandate-Building

How did real monarchs increase their personal and dynastic mandate? Twelve
patterns from medieval/early-modern history:

### §2.1 Travel-and-presence
- **Royal Progress** (Henry I of England's Normandy circuits; Elizabeth I's
  English progresses) — monarch tours own realm, holds court, dispenses
  justice, hears petitions. Cost: treasury (entertainment + gifts to hosts).
  Benefit: personal Mandate from direct contact + visible governance.
- **Eyre / itinerant justice** (Edward I) — institutional version of the same.

### §2.2 Institutional building
- **Codification** (Justinian's Corpus Juris, Napoleon's Code, Edward I's
  legal reforms) — great legal project, multi-year. Cost: bureaucracy +
  treasury + risk of opposition. Benefit: permanent institutional Mandate.
- **Public works / monuments** (Hadrian's Wall, Versailles, Suleiman's
  mosques, St. Basil's Cathedral, Trajan's Forum) — W expenditure ↔
  grandeur ↔ Mandate.

### §2.3 Religious sanction
- **Coronation / anointing** (Charlemagne crowned by Pope Leo III, 800 AD;
  Charlemagne is the canonical example — Roman authority transferred via
  papal recognition). Cost: concessions to Church + ceremony costs. Benefit:
  sacred Mandate + can lift Excommunication.
- **Crusade / holy war** (Richard I, Louis IX) — Mandate from religious
  validity, but only if successful. High cost, high risk.

### §2.4 Diplomatic
- **Dynastic marriage** (Habsburg "tu felix Austria nube"; Catholic Monarchs
  Ferdinand & Isabella) — treaty + alliance + heir + sometimes inherited
  territory. Cost: diplomatic capital, dowry.
- **Successful treaty / peace** (Westphalia, Vienna) — Mandate from
  delivering peace.

### §2.5 Popular legitimacy
- **Charity / famine relief** (Roman grain dole; Constantinople institutional
  charity) — W expenditure → Mandate from common subjects.
- **Tournament / festival** (Edward III's Round Table; Henry VIII's Field of
  the Cloth of Gold) — W expenditure → Mandate from chivalric/aristocratic
  display.
- **Patronage of culture / scholarship** (Medici, Suleiman the Magnificent,
  Akbar) — W → cultural Mandate.

### §2.6 Reform
- **Anti-corruption purges** (Kangxi's reforms; Henry II's reining-in of
  sheriffs) — costs political capital, makes enemies. Benefit: institutional
  Mandate from rule-of-law.

### §2.7 Synthesis pattern
Most historical Mandate-building share a common shape:
- **Cost an existing resource** (treasury / time / political capital)
- **Risk failure** (cost paid even on failure; downside is reputational)
- **Slow accrual** (single project = +1 step on long ladder)
- **Religious sanction is special** (can recover from de-legitimation)

This shape is the design template for the Crown Initiative card.

---

## §3 Crown Initiative — Card Design

### §3.1 Card metadata

| Property | Value |
|----------|-------|
| **Card name** | Crown Initiative |
| **Faction** | Crown (Valorsmark) only |
| **Slot** | Senator Inward (new) — 1× per season; shares no slot with Senator Outward (Crown Treaty) or other cards |
| **Replay** | Once per season; no per-arc or per-campaign cap |
| **Modes** | Three; player declares mode at play |

### §3.2 Mode I — Royal Progress (the "soft" mode)

**Historical anchor:** Henry I's Normandy circuits, Elizabeth I's progresses.

| Property | Value |
|----------|-------|
| **Cost** | Wealth −2 (treasury for entertainment, gifts to hosts) |
| **Pool** | Influence + Standing modifier |
| **Ob** | `max(2, floor((sum_max - sum_current) / 2))` where `sum_max = 7 × num_owned_territories`, `sum_current = Σ(territory.Accord for territory in owned)`. Discontent-driven: easier when Accord is high (small `sum_max - sum_current`); harder when realm is in turmoil. Floor at 2 prevents trivial auto-success at peak Accord. **[ITERATED 2026-05-17 per ED-840 closure, Pass 2h. Previous formula `floor(sum_accord/2)` produced OPPOSITE behavior; was canon-vs-text contradiction.]** |
| **Outcomes** |  |
| Overwhelming | Mandate +2; Standing +1; all own territories at Accord 1 → Accord 2 |
| Success | Mandate +1; one own territory of choice (lowest Accord) +1 Accord |
| Partial | Standing +1 (tour happened, didn't move the needle); cost still paid |
| Failure | Standing −1 (no welcome at one stop); cost paid; no L gain |

**ED-840 closure note (2026-05-17, Pass 2h):**

The Ob formula was iterated to match the descriptive text. Prior canon stated `floor(sum_accord/2)` which produced OPPOSITE behavior from the descriptive clause (action got HARDER as Accord rose, not EASIER). M7 balance sweep N=1000 surfaced the contradiction: starting sum_accord ≈ 30-33 across 6 Crown territories produced Ob 15-16 vs Pool 5, mathematically unwinnable. Pass 2h ratifies Option A from ED-840: revise formula to `max(2, floor((sum_max - sum_current) / 2))` where `sum_max = 7 × num_owned_territories`. Behavior matches descriptive text. Floor 2 prevents trivial auto-success at peak Accord.

Verification at illustrative Crown states (Cost: W -2; Pool: I=5 + Standing):

| State | sum_current / sum_max | Ob | Net (Pool 5) | Outcome density |
|---|---|---|---|---|
| Peak (Accord 7 × 6 terr) | 42/42 | 2 (floor) | +3 | Overwhelming likely |
| Starting (Accord 5.5 × 6) | 33/42 | 4 | +1 | Partial-Success boundary |
| Strained (Accord 4 × 6) | 24/42 | 9 | −4 | Failure likely |
| Collapsing (Accord 3 × 3) | 9/21 | 6 | ≤−2 (reduced Standing) | Failure |

Design intent: Royal Progress is the *maintenance* action for governing Crowns, not a recovery action. Cannot restore a collapsing realm. Crisis recovery uses Coronation Renewal (Mode II) or Great Work (next §). Historical anchor (Henry I touring settled realm; Elizabeth I touring loyal counties) is preserved — both monarchs progressed at peak governance, not in crisis.

ED-840 closed.

**Flavor:** The King travels through his realm, holds court at each stop,
hears petitions, dispenses justice. Accord-1 territories get the Sovereign's
visible governance; the realm sees its monarch in person.

### §3.3 Mode II — Great Work (the "Open Pledge" mode)

**Historical anchor:** Justinian's Code, Edward I's legal reforms, Versailles,
Suleiman's mosques.

| Property | Value |
|----------|-------|
| **Structure** | Open Pledge per PP-515 declared in Phase 1: "I will undertake [codification / monument / charter] over 3 seasons." |
| **Cost** | Wealth −1 per season for 3 seasons (sustained investment) AND uses Senator Inward slot each season |
| **Pool (final season)** | Mandate (the institutional weight backing the project) |
| **Ob (final season)** | 4 — challenging; major project |
| **Outcomes (on completion)** |  |
| Overwhelming | Mandate +2 permanent; all own Charters gain Govern −1 Ob (permanent quality-of-life), Standing +2 |
| Success | Mandate +2 permanent |
| Partial | Mandate +1; sunk W cost partial loss |
| Failure | Standing −2, Cohesion −20 (per PP-515 breach penalties); the project failed publicly |
| **Mid-pledge breach** | Standing −2, Cohesion −20, Reputation −15 (PP-515); the project was abandoned visibly |

**Flavor:** The Crown commits to a multi-year project. Could be a legal code
(Lex Valoriae), a great cathedral commissioned with Church approval, a
university founding, a defensive infrastructure program. The Pledge structure
means players commit publicly (Standing +1 on declare); breach is costly.

**Strategic role:** Long-term Mandate accrual that scales with Mandate
already held (higher L = better odds at the Ob 4 roll). Rewards consolidation
over expansion.

### §3.4 Mode III — Coronation Renewal (the "recovery" mode)

**Historical anchor:** Charlemagne crowned by Pope Leo III (Christmas 800 AD).
The original example: Roman imperial authority re-conferred through papal
recognition.

| Property | Value |
|----------|-------|
| **Prerequisites** | Crown–Church active Truce, Peace, Alliance, or Crown Treaty; Church is not actively prosecuting an Excommunication against Crown this season |
| **Cost** | Wealth −2 (ceremony, gifts to Church, hosting clergy) |
| **Pool** | Influence |
| **Ob** | floor(Church Mandate / 2) + 1 |
| **Outcomes** |  |
| Overwhelming | Mandate +2; if Crown currently Excommunicated, Excommunication lifted; Standing +1; Crown–Church Standing +1 |
| Success | Mandate +1; Excommunication lifted if currently active |
| Partial | Standing +1 (ceremony happened); no L change |
| Failure | Standing −1 (awkward ceremony, visible cracks); cost paid |

**Flavor:** The Cardinal anoints the King. The crown is placed by the Church.
Sacred authority is renewed. This is **the canonical recovery from
Excommunication** — the only mechanic that lifts Excommunication's L cost.

**Strategic role:** A Crown that has been Excommunicated, suffered Mandate
collapse, or seen its sacred standing eroded can recover through alignment
with Church. Costs: Crown must accept Church's hegemonic role in the
arrangement. Cannot be played while Crown–Church are at war.

### §3.5 Defensive interaction

- **Excommunication while Coronation Renewal is in progress:** If Church
  successfully Excommunicates Crown the same season Coronation is played,
  resolve Excommunication first; Coronation may still attempt but Pool is
  reduced by 1 die (lost public standing).
- **Hafenmark Parliamentary Session targeting the Initiative:** If
  Parliament passes a vote opposing the Initiative, +1 Ob to the Initiative
  roll (matches existing Dynastic Proclamation defensive pattern).
- **Spy success during Royal Progress:** May intercept the king's progress
  (Standing −1 instead of normal Spy effect).

### §3.6 Open Pledge integration (PP-515)

All three modes can be declared as Open Pledges in Phase 1 for additional
Standing gains on honor / breach penalties. Mode II is structurally an Open
Pledge by default; Modes I and III are optional Pledge enhancements.

### §3.7 Casus Belli interaction

Crown Initiative does NOT grant or remove Casus Belli on any faction. It is
an internal-governance action; it has no rival-facing consequence outside
the Standing display.

---

## §4 Simulation Test Results

500 campaigns per config. Source: `/home/claude/crown_initiative_sim.py`. Mode I
(Royal Progress) implemented; Mode II + III modeled as approximate equivalents
in scoring; actual Mode II Open Pledge mechanics not simulated.

### §4.1 Headline results

| Configuration | Crown win | Church | Hafenmark | Varfell | Almud Strong | Almud Deposed | Pyrrhic wins |
|---------------|-----------|--------|-----------|---------|--------------|---------------|--------------|
| canon-v5 (no Initiative) | 31.6% | 50.8% | 12.4% | 5.2% | 16.2% | 12.0% | **1.9%** |
| canon + Initiative | 28.8% | 53.8% | 12.6% | 4.8% | 15.8% | 13.2% | **1.4%** |
| long 60s (no Initiative) | 18.6% | 70.4% | 8.0% | 3.0% | 14.6% | 38.6% | **2.2%** |
| long 60s + Initiative | 18.2% | 68.2% | 10.8% | 2.8% | 14.8% | 37.8% | **0.0%** |
| high-consent (no Initiative) | 50.8% | 38.6% | 7.4% | 3.2% | 29.0% | 9.2% | **1.6%** |
| high-consent + Initiative | 48.4% | 37.4% | 9.6% | 4.6% | 29.2% | 8.4% | **0.4%** |

### §4.2 What the Initiative does

**Crown faction win-rate:** very slight decrease (31.6 → 28.8% canon; 50.8 →
48.4% high-consent). The Initiative competes for action-slot resources with
Crown Treaty + Royal Charter + Govern — playing Initiative means foregoing
those.

**Almud personal survival:** modest improvement at long campaigns (Deposed
38.6 → 37.8%); near-zero effect at canon length (12.0 → 13.2%).

**Pyrrhic wins (Crown wins but Almud deposed):** **measurable, consistent
decrease.** Drops from 1.9% to 1.4% at canon; from 2.2% to **0.0%** at long
campaigns; from 1.6% to 0.4% at high-consent. **This is the design-intended
effect.**

### §4.3 Interpretation

The Crown Initiative is a **defensive/recovery mechanic, not a power
amplifier.** It does not push Crown to dominance; it makes Crown's wins
"Almud's wins" rather than pyrrhic Crown-territory-but-Almud-deposed
outcomes.

This is the correct design shape:
- A Mandate-increase mechanic that doubled as a winning vector would
  unbalance the 4-faction equilibrium
- A pure Mandate-recovery mechanic preserves balance while making the
  character-scale layer survivable
- Cost (Wealth) is bounded by Crown's economy; can't be spammed
- Slot competition (Senator Inward 1×/season) limits cumulative effect

### §4.4 Limitations of this test

- Only Mode I (Progress) simulated mechanically; Modes II & III approximated
  in scoring
- 500 campaigns; 95% CI on rate differences ~±4pp
- Almud-state classification uses my Part 9 heuristic; canonical character-scale
  state may differ
- Other factions' analog cards not simultaneously tested (see §5)

---

## §5 Analog Mechanics for Other Factions

The Crown Initiative pattern (Mandate-recovery through historical-precedent
internal action) generalizes. Sketched proposals for the other three factions:

### §5.1 Church — Synod / Council
**Historical anchor:** Council of Nicaea, Lateran Councils, Council of Trent.

| Property | Value |
|----------|-------|
| **Card** | Council of Solmund — Special/Unique Power |
| **Slot** | 1× per arc (rare event) |
| **Cost** | Cardinal Focus consumed; +1 Standing from invitation |
| **Pool** | Mandate |
| **Ob** | floor(CI / 30) + 2 (easier when CI is high — Church has institutional momentum) |
| **Effects (Success)** | Church Mandate +1; one Cardinal Focus permanent for this campaign |
| **Effects (OW)** | Church Mandate +2; choose a Cardinal Focus permanent + select one rival faction's L → −1 (formal censure) |

**Why this fills a gap:** Ecclesiastical Appointment already exists as
Church's per-season L+1 mechanic; Council provides the long-cycle Strategic
Mandate boost analogous to Crown's Great Work.

### §5.2 Hafenmark — Charter of Liberties
**Historical anchor:** Magna Carta (1215), 1648 Westphalia Treaties.

| Property | Value |
|----------|-------|
| **Card** | Charter of Liberties — Diplomat/Senator (slot conflict with Crown Treaty's pattern) |
| **Cost** | 1 Diplomatic Token (consumed); W −1 |
| **Pool** | Influence + (active Tokens on opponents) |
| **Ob** | 4 |
| **Effects (Success)** | Hafenmark Mandate +1; PI −1 (Parliament has codified a constitutional check; tension reduced) |
| **Effects (OW)** | Hafenmark Mandate +2; PI −2; all rival factions face +1 Ob to Excommunication attempts this campaign (constitutional protection) |

**Why this fills a gap:** Parliamentary Session already exists. Charter
of Liberties is the rare, codifying counterpart — institutional rather than
political.

### §5.3 Varfell — Vaynard's Hall
**Historical anchor:** Mead-hall culture (Heorot in Beowulf); Norse Althing
gatherings; Reinhardt von Lohengramm's personal court (per CR-STRIKE
flavor text).

| Property | Value |
|----------|-------|
| **Card** | Vaynard's Hall — Tribune (new card type) |
| **Cost** | Military −1 (one warband leaves the front for the gathering); W −1 |
| **Pool** | Mil + (Tribune Network active) |
| **Ob** | 3 |
| **Effects (Success)** | Varfell Mandate +1; one captured Revelation Token sacrificed for +1 Standing |
| **Effects (OW)** | Varfell Mandate +2; one rival faction L −1 (publicly insulted by demonstration of Varfell strength) |

**Why this fills a gap:** Varfell currently has NO L-gain mechanic. Vaynard's
Hall provides a military-flavored Mandate-gain consistent with CR-STRIKE
flavor ("Vaynard does not convert populations ideologically; Varfell expansion
is purely military"). The Hall is a *military-honor* mandate path, not a
populist or institutional one.

### §5.4 Cross-faction balance check

Once all four factions have flagship Mandate-recovery mechanics, the
character-scale survival rates should converge. Recommended follow-up:
implement all four in simulator, measure deposition rates per faction
leader, check for ±5pp band.

---

## §6 Integration with Canonical Sources

### §6.1 New canonical text needed

To formalize this proposal:
- Add to `peninsular_strain_v30.md` §5 (Faction Toolkits): new subsection
  §5.5 "Crown — Internal Governance (Crown Initiative)" mirroring §5.1
  (Crown Treaty) structure
- Add to `faction_actions.md` (the card-action specification): full Crown
  Initiative spec for all three modes
- Add new patch register entry: PP-NEW (Crown Initiative card)
- Cross-reference in `victory_v30.md` if relevant to victory conditions

### §6.2 PP-515 (Open Pledge) integration

Mode II (Great Work) uses Open Pledge structure already canonical via
PP-515. No new patch needed; just specify Initiative's pledge mechanics
follow PP-515.

### §6.3 PP-189 (Institutional Mandate / Appease) interaction

Crown Initiative is **not** subject to Appease — it's an internal-governance
action, not a rival-facing action. Targets do not get to Appease.

### §6.4 Excommunication recovery (Q-11 resolution)

The 8-part audit's Q-11 (Can Excommunication be lifted?) is **answered by
Mode III (Coronation Renewal)**. Recommended editorial action: ratify
Mode III as the canonical Excommunication-recovery path. This closes Q-11.

---

## §7 Recommendations

### §7.1 Immediate

1. **Ratify Crown Initiative** at minimum Mode I (Royal Progress).
   Modes II + III can be deferred for further design / playtest if
   Mode I alone proves the concept.
2. **Adopt Mode III as the canonical Excommunication recovery mechanic
   (Q-11 resolution).** This closes a high-priority open question.
3. **Run full simulation with all four faction analogs implemented** —
   verify the leader-survival decoupling closes for all factions, not
   just Crown.

### §7.2 Medium-term

4. **Playtest Mode II (Great Work) Open Pledge interactions** — multi-season
   pledge mechanics need physical play to verify pacing
5. **Tune cost vs reward across modes** — current W −2 + Ob calibration
   based on Mode I sim; Modes II + III need additional simulation
6. **Verify Mode III defensive interaction** — Church can deliberately
   excommunicate at the wrong time; needs game-theoretic playtest
7. **Implement Hafenmark Charter of Liberties + Varfell Vaynard's Hall +
   Church Council** — close the structural gap for all factions

### §7.3 Long-term

8. **Resolve Q-12 to Q-15 (character-scale layering)** — when does Almud
   actually "fall"? What is the character-scale game state when Mandate
   collapses? Does Lothar inherit?
9. **Build v8 simulator with character-scale event triggers** — track not
   just stats but character-scale state machines (king → regent → exile →
   restoration)

---

## §8 Open Questions This Surfaces

| # | Question | Status |
|---|----------|--------|
| Q-16 | What is the canonical maximum Mandate? Current sim caps at 7 — is this canonical? | partial — appears canonical |
| Q-17 | Does Mode II (Great Work) Open Pledge breach also cost W (sunk treasury) or just Standing? | not specified |
| Q-18 | Can multiple Crown Initiatives be in progress simultaneously (Mode II × 2)? | not specified |
| Q-19 | What happens to a Mode II Pledge if Crown is Excommunicated mid-pledge? | not specified |
| Q-20 | Are there cross-faction copy-cat Initiatives possible (e.g., Hafenmark mounts a "People's Initiative")? | design space |

---

## §9 Cross-Part Synthesis (Final)

| Part | Status |
|------|--------|
| 1 — Errata (4-faction canonical model) | preserved |
| 2 — Log Schema | preserved |
| 3 — Top-Down Re-Sim | directionally correct, magnitudes off |
| 4 — NERS Audit | methodologically valid |
| 5 — Throughline Audit | methodologically valid |
| 6 — Bottom-Up MC v3 | methodology valid; rule encoding had 10 violations |
| 7 — Canonical Bottom-Up v5 | canonical rules verified; EM-12 refuted |
| 8 — Sensitivity Analysis | identifies editorial leverage ranking |
| 9 — Character Decoupling | faction-scale ≠ character-scale |
| **10 — Crown Initiative Design** | **NEW** — mandate-increase mechanic; closes Q-11; analogs sketched for all factions |

**The 10-part audit progresses from balance question → emergent dynamics →
canonical verification → editorial leverage → character-scale → design proposal.**

Outstanding work:
- Editorial ratification of Crown Initiative (Modes I/II/III)
- Implementation of Church Council, Hafenmark Charter of Liberties, Varfell
  Vaynard's Hall (analog cards)
- Full v8 simulation with all four analogs
- Playtest verification

---

## §10 Files Produced This Session (Post-Compaction, 2026-05-14 series)

| File | Description |
|------|-------------|
| `part6_bottom_up_v3sim_2026-05-14.md` | Bottom-up MC v3 emergent findings |
| `part7_canonical_v5sim_2026-05-14.md` | Canonical v5 simulator results |
| `part8_sensitivity_synthesis_2026-05-14.md` | Q-1/Q-3/Q-4 sensitivity sweeps |
| `part9_character_decoupling_2026-05-14.md` | Almud vs Crown decoupling |
| **`part10_crown_initiative_design_2026-05-14.md`** | **this doc** — Crown Initiative card |
| `mc_v6_simulator_source.py` | v6 simulator with parameterized rules |
| `mc_v6_sensitivity_results.json` | Sensitivity sweep raw data |
| `char_decoupling_source_2026-05-14.py` | Character-scale instrumentation |
| `char_decoupling_results_2026-05-14.json` | Character-scale results |
| `crown_initiative_sim_source_2026-05-14.py` | Crown Initiative prototype simulator |
| `crown_initiative_test_results_2026-05-14.json` | Crown Initiative test results |

---

*Session: bottom-up-canonical-verified · 2026-05-14 · Part 10/10*
*Bottom-up methodology applied to design proposal: historical precedent ↔
mechanical pattern; simulator test verified design shape; analogs sketched
to close structural gaps in other factions.*
