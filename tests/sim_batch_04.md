# VALORIA SIMULATION BATCH 04
## 30 Stress Tests — Manoeuvres, Mass Combat, Gaps, Forgetting, Generic Factions, Knight Templar
**Executed:** 2026-03-27 | **Model:** Sonnet 4.6 | **Skill:** valoria-simulator

---

## Priority targets this batch
- M-044 Combat Manoeuvres (§8.6 now scanned — full isolation possible)
- M-045 Mass Combat disposition table (deeper simulation)
- M-023 Collective Thread Ops (formal cells)
- M-024 Shifting Objects (formal cells)
- M-025 Gaps (formal cells)
- M-029 Forgetting (§6.1 now scanned — full isolation)
- Crown, Church, Varfell, Hafenmark, Schoenland generic character tests
- Knight Templar archetype
- Damage formula correction (§8.1 confirms Power + weapon damage bonus + excess successes)
- Mass combat Thread ops TT cap (×3 flat, cap +15 — new finding from §8.3)

---

## TEST B4-001 — Combat Manoeuvres: Full Isolation
**Coverage:** M-044 | TTRPG | PRES | — | Crown, Löwenritter | Ehrenwall | Löwenritter Knight
**Mode A — Isolation**

All manoeuvres use Combat History pool, resolve at Priority 3A (before standard attacks).

### Manoeuvre Table (confirmed from §8.1)

| Manoeuvre | Versus | Effect |
|-----------|--------|--------|
| Defend! | Agility | Hold at bay; deny target's move action next round |
| Disarm | Agility vs Agility | Target drops weapon |
| Trip | Agility vs Agility | Target prone: −2D attack, attacks vs prone +2D, double cost to stand |
| Tie Up | Power | Lock weapons; no damage either this round |
| Rescue | Endurance | Redirect melee / Priority 4+ attack from ally to self |
| Reorient | Cognition | Manipulate positioning; establish or deny reach advantage |
| Withdraw | Agility | Sacrifice offence; re-establish reach advantage |

**Ob for each manoeuvre:** Not explicitly stated as a fixed Ob — "Versus" column specifies what the defender rolls, not an Ob. Resolution is attacker's Combat History pool vs defender's specified pool (opposed roll: higher net wins).

### Disarm probability analysis
Attacker: Ehrenwall (Combat History pool 12D, using Combat History vs Agility). Wait — "Disarm: Agility vs Agility." Both sides use Agility for Disarm, not Combat History. The manoeuvre column says "all use Combat History pool" in the header, but individual Versus entries override. Need to confirm: does "Combat History pool" in the header mean the *attacker* always uses Combat History, while the *defender* uses the listed stat?

**[FLAG: Manoeuvre resolution ambiguity — header says "all use Combat History pool" but Versus column lists specific defender stats (Agility, Power, Endurance, Cognition). Confirm: attacker always uses Combat History; defender uses listed stat.]**

**Assuming confirmed: attacker uses Combat History pool, defender uses listed stat.**

Ehrenwall (Combat History 12D) Disarms Crown Soldier (Agility 3):
- Ehrenwall: 12D TN7, expected net ≈ 4.0
- Soldier: 3D TN7, expected net ≈ 1.0
- P(Ehrenwall net > Soldier net) ≈ 85%. Disarm reliable for skilled character vs weak defender.

Trip vs strong defender (Agility 5):
- Ehrenwall 12D vs defender 5D. P(12D net > 5D net) ≈ 78%.
- Trip effect: defender prone → −2D attack, attacks vs prone +2D, double cost to stand. Very strong follow-up.

Rescue (Endurance as defender stat):
- Attacker redirects an attack onto themselves. No opposed roll vs the original attacker — it's a self-declaration. Endurance check determines the Rescue's stability? Or is Endurance just the pool size for determining reach and timing? Text is sparse.

**[FLAG: Rescue mechanic incomplete — "Endurance" listed as Versus, but Rescue is self-targeted (redirect attack onto yourself). What is Endurance checked against?]**

**F96** — Manoeuvre resolution uses attacker's Combat History pool vs defender's listed stat — but this is inferred, not explicit. If both sides use listed stats, a high-Agility low-Combat character could win Disarm against a high-Combat low-Agility fighter despite inferior overall combat ability. P2 — clarification needed.

**F97** — Rescue mechanic incomplete. Endurance as "Versus" for a self-redirect doesn't map to opposed roll logic. P2.

**F98** — Priority 3A sequencing: Manoeuvres resolve *before* attacks within Priority 3. A successful Trip renders the target prone before attacks resolve. Attacks against the now-prone defender gain +2D. This means a manoeuvre+attack combination (declared simultaneously, manoeuvre resolves first) is a strong two-step. No restriction found on declaring both a manoeuvre and an attack in the same round. P3 — intentional design (tactical depth).

---

## TEST B4-002 — Combat Manoeuvres: Interaction Chain
**Coverage:** M-044 | TTRPG | PRES | — | Crown, Löwenritter | Ehrenwall | Löwenritter Knight
**Mode B — Interaction**

### Trip → Attack combo

Round 1: Ehrenwall declares Trip + Attack.
- Phase 1 (Priority 3A): Trip resolves. Defender prone? 78% chance.
- Phase 3 (Priority 3, attacks): If prone, Ehrenwall's attack gains +2D.

Ehrenwall attack with +2D: 12D + 2D = 14D. Expected net ≈ 4.6. Damage: Power + weapon +2 + 4.6 excess − armour.

Vs heavy armour (DR 3): Power 3 + weapon +2 + 4.6 − 3 = 6.6 expected damage. Vs Health 10: 60% of max Health in one round.

**Defend! denial effect:** Opponent denied move action next round. In zone-based combat, denying movement means the opponent cannot change zones. Useful to pin a character in an unfavourable zone.

**Reorient → reach denial:** A short-weapon character Reorients to deny the long-weapon opponent's reach advantage before closing. This makes Reorient a prerequisite for Close manoeuvre in some fights.

**F99** — Trip+Attack two-step is a dominant tactical choice for high-pool characters: ~78% prone guarantee with +2D attack bonus creates a near-certain heavy damage round. Only counter: opponent declares Defend! (which denies move but doesn't prevent being Tripped, as both resolve at Priority 3A). No explicit counter-manoeuvre to Trip found. P2 — possible dominant strategy.

---

## TEST B4-003 — Mass Combat: Disposition Table Full Simulation
**Coverage:** M-045 | TTRPG/BG | PRES | FSTAT | Löwenritter, Crown vs Church Templars | Ehrenwall | Löwenritter Knight
**Mode C — Scenario**

### Unit Setup

**Löwenritter Heavy Infantry (veteran):**
Martial 4+1vet=5, Endurance 4, Cohesion 4. Health=10. Commander: Ehrenwall (Cog 5, Pres 4).
Attack pool: Martial 5 + Cog 5 = 10D. TN5.

**Knights Templar:**
Martial 5, Endurance 5, Cohesion 6. Health=11. Immune to Brutal morale effects. +1D Cohesion vs Thread events.

### State: Battle Start
```
Löwenritter: Health 10, Martial 5, End 4, Coh 4
Templars: Health 11, Martial 5, End 5, Coh 6
TT 44 | TC 38
```

**Mass combat TN: 5** (confirmed — all mass combat rolls TN5).

Expected net per die at TN5: P(die≥5)=0.6. Expected net ≈ 0.5 per die (0.6 − 0.1 for 1s + chain).

### Round 1: Both Offensive

Disposition Interaction: Offensive vs Offensive → Ob 1, +2D each.
Löwenritter: (5+5+2)=12D TN5. Expected net ≈ 6.0.
Templars: (5+est.Cog4+2)=11D TN5. Expected net ≈ 5.5.

Both hit (Ob 1 near-certain at 12D). Damage = Power (est.3 for Heavy Infantry) + weapon +2 + excess − armour.
Excess Löwenritter: 6.0 − Templar defence. But mass combat doesn't use split pools — one roll for attack, one for defence? Or is damage just net successes above Ob?

**[FLAG: Mass combat damage calculation ambiguous. §8.3 disposition table shows Ob and pool modifier for attack. Damage formula not restated for mass combat. Does "excess attack successes" apply, or is there a flat damage value per success?]**

**F100** — Mass combat damage formula not specified in §8.3. Personal combat uses Power + weapon + excess − armour. Mass combat mentions Health and damage conceptually but no explicit formula found in scanned §8.3. P1 — combat cannot be resolved without this.

### Round 1: Löwenritter Offensive, Templars Defensive

Löwenritter (Offensive) vs Templars (Defensive): Ob 2, +2D.
Löwenritter: 12D TN5. Expected net ≈ 6.0. P(≥2 net) ≈ 99%. Hits reliably.

Templars (Defensive) vs Löwenritter (Offensive): Ob 1, ±0.
Templars: 9D TN5. Expected net ≈ 4.5. Hits reliably too.

**Formation Break check (Health → 0):** At moderate damage rates (~3/round), Löwenritter reaches 0 Health in ~3 rounds → Formation Break → Cohesion check (Ob2, 4D TN5). P(4D TN5 ≥2 net) ≈ 76%. P(route) ≈ 24%.

**F101** — Defensive disposition does not prevent being hit — it only raises attacker's Ob to 2. Both sides in a battle can deal damage simultaneously regardless of disposition. A Defensive unit that fails its attack (Ob 2) simply didn't deal damage that round while the attacker did. Asymmetric attrition — the Offensive unit deals damage reliably; the Defensive unit deals damage ~76% of turns. This creates a "Defensive is correct choice vs equal opponent" incentive. P3 — intentional asymmetry.

---

## TEST B4-004 — Mass Combat: TT Cap Discovery
**Coverage:** M-045, M-046 | TTRPG/HYB | CROSS | TT, ThS, FSTAT | Revolution, Crown | — | Practitioner
**Mode B — Interaction**

### Thread Operations in Mass Combat (§8.3 confirmed)

TT multiplier: **×3 flat** (replaces scale-based). TT gain from any single mass combat Thread op **capped at +15**.

**Significance:** A Relational-scale Weaving normally generates +3 TT × ×2 multiplier = +6 TT. In mass combat context: +3 TT × ×3 = +9 TT. Under cap (15). OK.

A Territorial-scale FR Dissolution (if attempted in mass combat): normal TT +8 (Failure degree) × ×3 = +24 TT. **Cap applies: +15 max.** Excess → narrative consequence.

**B2-029 correction:** Test B2-029 used scale-based TT multiplier for Thread ops in mass combat. Correct multiplier is ×3 flat per §8.3. All mass combat Thread op TT calculations in B2 should use ×3 not scale-based.

**F102** — TT cap in mass combat (+15) prevents worst-case Thread op cascades during battle. Without cap: a failed Territorial FR Dissolution in mass combat could generate +24 TT in one round, potentially crossing a threshold mid-battle. Cap converts excess to narrative. Clean safety valve. P3 — intentional.

**F103** — ThS cost in mass combat: does the ×3 flat TT multiplier affect ThS? ThS cost is from the temporal auto-effect of Thread operations, not directly from TT gain. ThS should still use normal per-operation costs regardless of mass combat context. Not confirmed in §8.3 text. P2 — ThS cost in mass combat context unconfirmed.

---

## TEST B4-005 — Collective Thread Operations: Formal Isolation
**Coverage:** M-023 | TTRPG | PRES | TT, ThS, CERT | Revolution | — | — | Practitioner
**Mode A — Isolation**

### Collective Op Structure (§5.14)

Anchor: highest TS practitioner. Rolls full operation pool.
Helpers: each contributes floor(Cognition ÷ 2) bonus dice.
Constraints: helpers cannot Fork; anchor cannot Fork when anchoring; Conflicting Beliefs → helper dice cannot chain on 10.

### Pool Construction — 3-Practitioner Collective

Anchor (TS 55, Attunement 5, History 6): 11D base.
Helper 1 (Cog 5): floor(5÷2) = +2D.
Helper 2 (Cog 4): floor(4÷2) = +2D.
Total: 15D. TN7. Ob3 (Relational scale).

P(15D TN7 ≥3 net) ≈ 99.9%.

### Lattice Fracture (helper drops contact)

If Helper 1's contact drops mid-operation: remove 2D → pool becomes 13D. 
Check: "If total pool drops below half the Anchor's solo pool: +1 Ob." Half of 11D = 5.5D. 13D > 5.5D — no fracture penalty. Pool must drop below 5.5D total before fracture fires.

If both helpers drop: pool = 11D (anchor solo). Still above 5.5D. Fracture never fires in a 3-person collective if anchor is present. Fracture requires a larger collective where helper withdrawal significantly depletes the pool.

**F104** — Lattice fracture condition fires only in large collectives: for a 3-person collective, helpers would need to abandon and anchor's solo pool still exceeds fracture threshold. Fracture becomes relevant at 6+ practitioner collectives where helper withdrawal could drop pool below half-anchor. For typical play (3–4 practitioners), fracture is a near-dead rule. P3 — intended for large ritual operations.

### Stunt in Collective Operations
"Anchor's auto-successes replace rolled dice; helpers' contributed dice do not apply to a Stunt."

This means: Stunt disables the collective pool advantage. A Stunt in a collective operation is equivalent to the anchor acting solo. Effectively: Stunt is anti-synergistic with collective ops.

**F105** — Stunt anti-synergy with collective ops: using Stunt removes all helper contribution, reducing collective pool to anchor solo. Players must choose: collective reliability (all pool) or dramatic solo (Stunt auto-successes). Intentional — Stunt is a personal narrative moment, not a group effort. P3.

---

## TEST B4-006 — Shifting Objects: Creation and Deterioration
**Coverage:** M-024 | TTRPG | CROSS | TT, ThS, CERT | — | — | — | Practitioner
**Mode A — Isolation**

### Shifting Object Mechanics (§5.13)

**Trigger:** Object in territory where multiple Thread ops performed, OR TT above 40 for 2+ seasons.

**Certainty cost:** −1 on first witnessing (Spirit check TN7 Ob1 to resist).

**Deterioration:** Worsens to Gap within 1d3 seasons without intervention. Dissolution residue forms at edges each season it persists.

**Stabilisation:** Weaving (Object scale, Ob2) arrests deterioration. Overwhelming restores full actualisation.

### Deterioration Timeline

Season 1: Shifting Object forms.
Season 2 (50% chance — 1d3 seasons, so 1/3 chance it became Gap in Season 1, 1/3 in Season 2, 1/3 in Season 3):
- Expected time to Gap: 2 seasons.
- Each season persisting: dissolution residue accumulates at edges.

### Stabilisation probability

Pool: Attunement 5 + History 6 = 11D. TN7. Ob2.
P(11D TN7 ≥2 net) ≈ 99%. Stabilisation is routine for competent practitioners. The challenge is knowing the Shifting Object exists and reaching it.

**TT-based spontaneous formation (TT 40–59 Elevated state):** "Shifting Objects spontaneous" — no Ob or roll specified for spontaneous formation. Rate? Frequency? Not defined.

**F106** — Shifting Object spontaneous formation rate at TT 40+ not defined. §7.1 states Shifting Objects become possible at TT 40–59, but no per-season chance, no pool, no procedure. GMs must improvise frequency. P2.

---

## TEST B4-007 — Gaps: Full Lifecycle
**Coverage:** M-025 | TTRPG | CROSS | TT, ThS, CERT | — | — | — | Practitioner
**Mode A + D — Isolation + Edge Cases**

### Gap Formation Sources

1. Shifting Object deteriorates (1d3 seasons).
2. FR Dissolution Failure at Personal+ scale.
3. FR Dissolution Failure against monstrous entity.
4. Existing Gap proximity + TT accumulation: existing Gaps generate TT +4/season, raising probability of secondary Gaps.
5. Past-Oriented Pulling against Threadcut being: auto-produces Gap.

### Gap Escalation Table

| Gap Age | Scale | Closure Ob |
|---------|-------|------------|
| Micro-Gap (same scene) | Personal | 3 |
| Standard (1 session old) | Relational | 5 |
| Entrenched (1+ seasons) | Territorial | 6 |
| Catastrophic (3+ seasons) | Structural | 7; requires Einhir ritual framework |

**Gap lifecycle math:**

If players fail to close a Standard Gap before next session:
- Gap age → Entrenched. Closure Ob: 5 → 6. TT cost of closure: 0 (closure reduces TT by reducing Gap's TT +4/season contribution, but the Closure operation itself generates TT from the FR Dissolution used to close it).

**Gap × Monstrous Incursion interaction:**
Each scene near a Gap: 1d10 roll, 1–2 = Mode 1 incursion. P(incursion) = 20% per scene.

With 3 scenes near a Gap per session: P(at least one incursion) = 1 − (0.80)³ = 1 − 0.51 = 49% per session.

**F107** — Gaps near session-active locations almost guarantee incursions within 2–3 sessions (49%/session → >75% by session 2). Players have strong incentive to close Gaps immediately. Correct pressure. P3.

**F108** — Multiple Gaps compound incursion probability multiplicatively. Two active Gaps in the same territory: 20% + 20% − 4% = 36% per scene. Three Gaps: ~49% per scene. At TT 80+ (full entity + Shifting Objects in adjacent territories), multiple Gap formation could create near-certain incursion pressure every scene. P2 — threshold interaction creates runaway incursion states.

---

## TEST B4-008 — The Forgetting: Full Isolation
**Coverage:** M-029 | TTRPG | PRES | CERT, TS | — | — | Maret Uln | Practitioner, Non-TS Scholar
**Mode A — Isolation**

### Forgetting Check (§6.1 confirmed)

Roll: Cognition + Memory. TN8.

| Exposure | Ob |
|----------|----|
| Boundary < 1hr | 1 |
| Interior 1–4hr | 2 |
| Deep interior 4hr+ | 3 |
| Einhir core sites | 4 |

TS bonus: TS ÷ 20 (rounded down) as bonus dice.

**Non-practitioner (Cog 4, Mem 3, TS 0):** Pool 7D. TN8. Ob2 (Interior).
P(die≥8) = 0.3. Expected net ≈ 1.4. P(≥2 net, 7D TN8) ≈ 29%.
Likely outcome: **Partial** (emotional impressions only).

**Practitioner (Cog 4, Mem 3, TS 55):** TS bonus = floor(55÷20) = +2D. Pool 9D. TN8. Ob2.
P(9D TN8 ≥2 net) ≈ 46%. Better odds, but still below 50% for Interior.

**Maret Uln (practitioner-level TS, est. TS 60, Cog 5, Mem 4):** TS bonus +3D. Pool 12D. TN8. Ob2.
P(12D TN8 ≥2 net): Expected net ≈ 2.4. P(≥2) ≈ 60%.
P(Overwhelming ≥4 net): ≈ 28%. On Overwhelming at TS 40+: full retention including ontological understanding.

### Testimony Ob penalty

Non-practitioners using Southernmost knowledge in Appeals/Debates: +1 Ob (Boundary), +2 Ob (Interior), +3 Ob (Deep/Core). The penalty *decreases credibility at lower exposure* — those with more exposure are more credible despite more Forgetting, because emotional weight reads as conviction.

**F109** — Forgetting check at TN8 with Cognition+Memory pool is mechanically harder than standard checks (TN7). This is correct — Forgetting is a structural limitation of rendering, not a skill failure. But it creates a near-certainty of information loss for non-practitioner expeditions even with good stats. A party sending non-practitioner scouts loses operational intelligence routinely. P3 — intentional.

**F110** — TS bonus to Forgetting check (+1D per 20 TS) is modest even for Resonant practitioners (TS 90–100: +4D bonus). At Deep Interior Ob3 TN8 with 11D pool: P(≥3 net) ≈ 33%. Even the most sensitive practitioners struggle to retain full knowledge from deep Southernmost exposure. P3 — intentional.

---

## TEST B4-009 — Crown Generic Character: Full Domain Action Suite
**Coverage:** M-034, M-035 | TTRPG/BG | PRES | FSTAT, TT, TC | Crown | — | Faction Leader
**Mode C — Scenario**

### Crown Starting Stats
Mandate 5, Influence 5, Wealth 4, Military 4, Stability 4.

**Ethical Framework: Virtue Ethics.** Public/virtuous actions −1 Ob. Covert/expedient +1 Ob.

### Domain Action: Royal Decree (once/season)
Roll: Mandate 5D TN7 vs Ob2. P(≥2 net) ≈ 66%. On success: one faction attribute change takes effect immediately rather than at seasonal accounting.

**Military Muster:**
Roll: Military 4D TN7 vs Ob set by Prosperity of territory (Prosperity 5 → Ob2; field: Ob1 for Feldmark −1 Ob). 4D TN7 P(≥2 net) ≈ 59%.

**Govern (uncontrolled territory):**
Roll: Mandate 5D vs Ob3 (neutral territory). −1 Ob if Virtue Ethics aligned (open governance). Ob2. P(5D TN7 ≥2 net) ≈ 84%.

**Seasonal Accounting:**
Stability check. Quiet season: Ob1. 4D TN7. P(≥1 net) ≈ 87%. Crown stable under normal conditions.
One active threat (Ob2): P(4D ≥2 net) ≈ 59%. Crown starts failing Stability checks under sustained pressure.

**F111** — Crown Stability fragile under multiple simultaneous threats. At Ob3 (2 concurrent threats): P(4D TN7 ≥3 net) ≈ 35%. P(fail 65%). Expected trajectory under active conflict: Stability 4→3 in 2 seasons. Stability 3→2 in further 2 seasons. Then anti-death-spiral floor engages at Stability 2 (F83 applies — Ob4 floor accelerates collapse). P2 — links to F83 P1 finding.

---

## TEST B4-010 — Church Generic Character: Mandate + TC Pressure
**Coverage:** M-034, M-035 | TTRPG/BG | PRES | FSTAT, TC, IP | Church | Himlensendt | Faction Leader
**Mode C — Scenario**

### Church Starting Stats
Mandate 5, Influence 6, Wealth 5, Military 4, Stability 5.

Ethical Framework: Divine Command. Actions aligned with doctrine −1 Ob. Non-doctrinal +1 Ob.

**Heresy Investigation (Domain Action):**
Pool: Influence 6D (or Church Reach 7D per §13.6 — ambiguity). TN7. Ob3. Against practitioner defense Ob2.
P(6D TN7 ≥3 net) ≈ 45%. Church builds files slowly without player obstruction.

**Church Mandate reaches 6–7:**
At Mandate 7 (theoretical): TC passive drift +1/season per §7.5.
Mandate 5 (start): below 7 threshold. No TC passive drift from Mandate alone.

**Seasonal Accounting:**
Church Stability 5. Quiet season Ob1: P(5D ≥1 net) ≈ 97%. Most stable at rest.

**Stability brake on TC:**
"When Church Stability falls to 5 or below at seasonal accounting, TC generation ceases that season regardless of Church Mandate."

Wait — Church Stability *starts* at 5. Per this rule, TC generation would *cease immediately at game start* because Church Stability is already at or below 5.

**F112** — Church Stability TC brake fires at Stability ≤5, but Church starts at Stability 5. This means TC generation is suppressed at game start and would only resume if Church Stability somehow *rises above 5*, which requires Overwhelming Stability checks. As written, the TC brake condition permanently suppresses TC generation unless Church Stability reaches 6+. This contradicts the TC's intended role as a climbing pressure. Either: (a) the threshold should be ≤4 or ≤3, or (b) the brake condition is inverted (should fire when Stability *drops to 5 or below*, meaning it's a late-game suppressor when Church is weakened, but starting at 5 means the "Cardinals competing publicly suppresses momentum" narrative only applies when Stability falls *from* a higher level — which it never starts at). **P1.**

---

## TEST B4-011 — Varfell Generic Character: Private Collection + Domain Actions
**Coverage:** M-034, M-035 | TTRPG/BG | PRES | FSTAT, TC, TS | Varfell, Church | Vaynard | Faction Leader
**Mode C — Scenario**

### Varfell Starting Stats
Mandate 4, Influence 4, Wealth 4, Military 4, Stability 4.

Ethical Framework: not confirmed in scanned §8.5. Assuming consequentialist (Vaynard's conviction is Reason — truth as instrument).

**Private Collection (Eisengrund T9 only):**
Access to Originary Locks, rare Einhir texts. Vaynard can offer these for Thread education (TK4). The Collection grants faction-specific advantages in Eisengrund only.

**Domain Action: Southernmost Research (Varfell specialty):**
Varfell Awareness 2 (starting). Research arc: Maret Uln leads expedition. If Maret Uln in Southernmost (unavailable for Council actions), Varfell loses an officer action.

**Succession leverage:** Vaynard refuses succession ratification without Southernmost access terms. This is a Domain Action denial — blocking Crown succession ratification. Mechanically: Vaynard has a veto on succession ratification. No Ob specified for this veto; it's a narrative-political hold, not a dice mechanic.

**F113** — Succession ratification veto mechanic undefined. Vaynard "refuses succession ratification" — what happens mechanically if Crown attempts to ratify anyway? IP implications (delayed ratification → IP +2)? No resolution procedure found. P2.

---

## TEST B4-012 — Hafenmark Generic Character: Maritime Trade + Sovereign Authority
**Coverage:** M-034, M-035 | TTRPG/BG | PRES | FSTAT, TC | Hafenmark, Church | Baralta | Faction Leader
**Mode C — Scenario**

### Hafenmark Starting Stats
Mandate 4, Influence 4, Wealth 5, Military 3, Stability 4.

Ethical Framework: from §13.3 Baralta — "structured, hierarchical, institutional authority." Closest to Deontological (rule-following).

**Maritime Trade (Hafenmark specialty):**
Sternhaven (T7) Trade Hub: all Trade orders +1D. Hafenmark's primary economic engine.

**Domain Action: Trade in Sternhaven:**
Pool: Wealth 5D + 1D (Trade Hub bonus) = 6D. TN7. Ob = target faction Wealth ÷ 2 = Guilds Wealth 6 ÷ 2 = Ob3.
P(6D TN7 ≥3 net) ≈ 45%. Moderate success rate.

**Seasonal Accounting:** Stability 4, quiet: P(4D ≥1) ≈ 87%. Hafenmark stable.

**Schoenland sea route interaction:**
Hafenmark controls Sternhaven (T7) adjacent to Schoenland (T15) by sea. If IP 75+: sea route severed. Hafenmark loses Trade Hub functionality. Wealth directly threatened.

**F114** — Hafenmark's economic identity is IP-vulnerable. At IP 75+, Sternhaven's sea route severs. Hafenmark Wealth drops. All characters with Resources tied to Hafenmark/Sternhaven lose 1D permanent (territory threatened). Hafenmark has strong incentive to resist IP escalation — but no unique IP-reduction mechanic. Baralta's Sovereign Authority reduces TC, not IP. P3 — intentional faction incentive alignment.

---

## TEST B4-013 — Schoenland Generic: Spoiler Actor Mechanics
**Coverage:** M-034, M-035 | BG | CROSS | IP, FSTAT | Crown, Altonian, Hafenmark | — | Faction Leader
**Mode C — BG Scenario**

### Schoenland (§8.10 — not fully scanned)

"Schoenland is not a faction — it is a spoiler actor." (§8.1 note).

Known mechanics:
- Altonian Trade: +1 Wealth/season to any faction with Trade order here while route is open.
- Altonian spies: Intelligence orders here reveal results to Altonia.
- At IP 75+: Altonian vanguard deploys here.

**Schoenland trade alliance:** −2 IP/year. Available if players secure it.

**Spoiler actor mechanics:** Schoenland has no faction stats, no Domain Actions, no Stability checks. It is a terrain feature with mechanical properties.

**F115** — Schoenland-as-spoiler-actor has no formal mechanical interaction framework. It generates benefits (Trade) and threats (spies, vanguard) but no roll procedure for "securing Schoenland trade alliance." What does this Domain Action look like? Who is the counterparty? Altonian Merchant Consortium? The Duke holding Schoenland? No procedure. P2.

---

## TEST B4-014 — Knight Templar Archetype: CE and Thread Exposure
**Coverage:** M-049, M-026 | TTRPG | CROSS | CE, TC, CERT | Church | Himlensendt | Knight Templar
**Mode C — Scenario**

### Knight Templar Profile

Stats: Martial 5, Endurance 5, Cohesion 6. Immune to Brutal morale effects. +1D Cohesion vs Thread events. Church asset; not muster-raised.

**Thread exposure mechanics:**
Templars assigned to Monstrous Incursion suppression accumulate CE on Inquisitor table. Unlike Inquisitors, they have no institutional trajectory framework for managing it.

**CE accumulation in incursion suppression:**
- Witnessing Thread operation: CE +2
- Monstrous entity encounter: CE +2
- Handling Originary Lock/residue: CE +2

Typical incursion mission (1 session): encounter Mode 1 entity + handle residue = CE +2 + CE +1 (residue handling) = CE 3.

**At CE 3:** TS growth check. For Templars — no essentialist Ob modifier specified (Inquisitors get Ob+1 from essentialist formation; Templars may or may not). Assume Ob1 (standard).

Cog 3 (estimated): 3D TN7 Ob1. P(≥1 net) ≈ 73%. Templar develops TS after one serious incursion.

**No institutional framework:** The Church has no suppression protocol for Templars developing TS. Templar CE crises are described as "personal, sudden, and unmanaged."

**F116** — Knight Templar CE pathway is unmanaged: Templars develop TS from combat exposure with no institutional support structure. Unlike Inquisitors (3 trajectories) or practitioners (trained framework), a Templar who develops TS has no defined resolution path. The character enters a narrative crisis with no mechanical procedure. P2.

**F117** — Templar Cohesion 6 + Thread immunity creates a paradox: Templars are mechanically best suited to fighting Thread entities (+1D Cohesion vs Thread events; Brutal immunity) but accumulate CE fastest from doing so, and have no framework for the resulting sensitivity. The faction most capable of suppressing Thread manifestations is also the faction most likely to inadvertently create practitioners who will challenge Church doctrine. Intentional — correct. P3.

---

## TEST B4-015 — Damage Formula Correction: Power Stat
**Coverage:** M-042 | TTRPG | PRES | — | — | — | — | Generic
**Mode A — Correction**

### B2-023 correction

B2-023 used "Weapon Bonus" as the base damage component. §8.1 confirms:

**Damage = Power + weapon damage bonus + excess attack successes − armour (minimum 0)**

Power is a character attribute (not weapon stat). Weapon damage bonus is Light +0, Medium +1, Heavy +2.

This changes the B2-023 analysis: a character with Power 4 wielding a Medium weapon deals 4 + 1 + excess − armour. Prior B2-023 used only "Weapon Bonus ~3" without Power. The corrected formula is more character-stat-dependent.

**Revised scenarios:**

| Power | Weapon | Armour | Expected Excess | Expected Damage |
|-------|--------|--------|-----------------|-----------------|
| 3 | Medium (+1) | 0 | 1.3 | 5.3 |
| 3 | Medium (+1) | 2 | 1.3 | 3.3 |
| 5 | Heavy (+2) | 0 | 1.3 | 8.3 |
| 5 | Heavy (+2) | 3 | 1.3 | 5.3 |
| 2 | Light (+0) | 0 | 1.3 | 3.3 |

**F118** — Power attribute is the dominant damage factor, not weapon choice. Power 5 heavy weapon vs Power 2 light weapon = 5 damage difference at 0 excess. Weapon bonus adds at most +2. Skill (pool size) determines excess successes. This creates three independent damage vectors: Power (character stat), weapon (equipment), skill (pool hits). Each contributes meaningfully. P3 — well-designed damage structure.

**Also confirmed: Exploding damage** — damage die showing 10: re-roll. Failure: +1. Success: +2 and re-roll. This was not in the original B2 analysis. Adds variance to damage, not covered in B2.

**F119** — Exploding damage rule not previously simulated. High-Power characters hitting with heavy weapons have non-trivial probability of exploding damage chains. Not captured in batch B2 expected-value calculations. P2 — affects damage ceiling calculations.

---

## TEST B4-016 — Initiative: Ob 2 Correction
**Coverage:** M-039 | TTRPG | PRES | — | — | — | — | Generic
**Mode A — Correction**

### B2-022 correction

B2-022 stated initiative as "Agility TN7 Ob1." §8.1 confirms: **Initiative = Agility dice, Ob2. Higher net wins.** TN unspecified for initiative — likely TN7 (standard) but only Ob is confirmed as 2.

**Corrected initiative probabilities:**

Ehrenwall Agility 5 vs Soldier Agility 3, TN7 Ob2:
- Ehrenwall P(≥2 net, 5D) ≈ 59%.
- Soldier P(≥2 net, 3D) ≈ 30%.
- P(Ehrenwall wins outright: both succeed, Ehrenwall higher) + P(Ehrenwall succeeds, Soldier fails) ≈ ...

Ehrenwall net: P(≥2) ≈ 59%, expected net ≈ 1.6.
Soldier net: P(≥2) ≈ 30%, expected net ≈ 1.0.

P(Ehrenwall wins initiative) ≈ 65% (not 97% as B2-022 stated with Ob1). B2-022 significantly overestimated initiative win rate.

**F120** — B2-022 initiative calculation error: used Ob1 when Ob is 2. Corrected P(skilled fighter wins initiative) ≈ 65%, not 97%. Initiative advantage exists but is not dominant — roughly 2:1 odds for a skilled character, not near-certain. P2 — prior simulation results affected.

---

## TEST B4-017 — Siege: Multi-Season Extended Action
**Coverage:** M-045 | BG/HYB | FUT | FSTAT | Löwenritter, Crown | Ehrenwall | Faction Leader
**Mode A — Isolation**

### Siege Mechanics (§8.4 — header confirmed)

"Sieges are multi-season extended actions. Siege may only be declared against Fortification 2+ territory. Fortification 0–1 = direct assault."

"Siege declaration: attacking force Military ≥ defender's garrison Military."

**[FLAG: §8.4 full procedure not scanned beyond opening paragraph. Proceeding from known context and §7.2 territory properties.]**

**Ehrenfeld (T5) siege scenario:**
Fortification 4 (max for Ehrenfeld). Garrison: Löwenritter Military 5.
Attacker needs Military ≥ 5 to declare siege.

Church Military 4 — cannot declare siege against Ehrenfeld. Crown Military 4 — cannot. Need Military 5+ = only Löwenritter itself or a coalition.

**F121** — Ehrenfeld is mechanically unsiegeable by any single faction at starting stats. Only Löwenritter (Military 5) meets the declaration threshold against itself. Coalition required for any external faction to besiege Ehrenfeld. Fortification 4 bonus (+1D per level to defence = +4D) makes any siege roll very difficult. Intentional — Löwenritter fortress as near-impregnable. P3.

---

## TEST B4-018 — Ambush Rules: Detection and Initiative
**Coverage:** M-039, M-040 | TTRPG | PRES | — | Crown, Niflhel | — | Riskbreaker, Inquisitor
**Mode B — Interaction**

### Ambush Mechanics (§8.1 confirmed)

Ob = ambusher's Tactics History + environment modifier (Ob 1–3). Defender's highest-Cognition character detects. On failure: attackers get one free Priority 2 round and initiative. On success: Agility vs Agility; defender's bonus successes from detection apply.

**Niflhel Riskbreaker ambushes a Crown Investigator:**

Ambush Ob: Tactics History (est. 3pts → pool not used, Ob3 = Tactics + env modifier). Wait — "Ob = ambusher's Tactics History + environment modifier." This makes Ob scale with the ambusher's skill, not a fixed number. Higher-skilled ambusher = harder to detect.

**[FLAG: Ambush detection uses Ob = ambusher's Tactics History + environment modifier. This is unusual — Ob scales with attacker's skill, not a fixed difficulty. Confirms attacker's skill directly sets detection difficulty. Verify this is the intended mechanic and not "pool = Tactics History + environment dice".]**

Tactics History 3pts: Ob = 3 + 1 (urban environment) = Ob4 for detection check.
Crown Investigator Cognition 3: 3D TN7 Ob4. P(≥4 net, 3D) ≈ 4%. Ambush nearly undetectable by low-Cognition character.

**F122** — Ambush detection Ob scales with ambusher skill, making high-Tactics Riskbreakers near-undetectable by low-Cognition targets. Ob4+ against 3D pool = <5% detection rate. Intended asymmetry. P3.

---

## TEST B4-019 — Thread Locked Objects: Resistance and Forensics
**Coverage:** M-017, M-054 | TTRPG | PAST | TS, ThS | Varfell, Church | Vaynard, Klapp | Practitioner
**Mode B — Interaction**

### Intentional Lock Resistance

Ob = creating practitioner's TS ÷ 10 (round up).
TS 62 practitioner → Ob7 to Pull against.

Vaynard's Private Collection: Originary Locks (cannot be Pulled, Woven, or subjected to standard FR). TS 50+ required to handle intentionally.

**Practitioner forensics on Intentional Lock (TS 50+, full scene):**
Reveals: approximate TS of creator (±10), whether placed under duress or calmly, rough date (within a decade).

**Klapp (TS 41) attempts forensics:** Below TS 50 requirement. Cannot perform intentional investigation of a Lock. Passive perception: at TS 30–49 tier, Klapp passively perceives dissolution residue at touch distance and Originary Locks when touched. He feels something but cannot investigate it.

**Originary Lock handling by TS 50+ practitioner:**
+10 TS immediately. Spirit check TN8, Ob = Wounds + 1. Fail: 2 Wounds (armour doesn't apply).

**Cascading benefit:** Klapp (TS 41) guided by a TS 50+ practitioner to handle an Originary Lock → TS 41 + 10 = 51. Threshold crossed: now Attuned. Subsequent forensics become available.

**F123** — Originary Lock TS threshold creates a "key that unlocks itself" dynamic: handling an Originary Lock at TS 41 (sub-threshold for intentional investigation) produces enough TS gain to immediately push past the 50 threshold. The Lock grants the capacity to investigate the Lock. This is thematically correct but creates a potential exploit: repeatedly exposing sub-threshold practitioners to Originary Locks for fast TS advancement. Each handling: +10 TS, Spirit check Ob1, P(fail, 0 Wounds) ≈ 30% → 2 Wounds. Risk exists but is manageable. P2 — TS advancement exploit via Originary Locks possible for determined players.

---

## TEST B4-020 — Social Systems: Reading Exchange + Debate Combo
**Coverage:** M-007, M-037 | TTRPG | PRES | COMP, CERT | Crown, Church | Almud, Himlensendt | Faction Leader
**Mode C — Scenario**

### Reading Exchange before Grand Debate

Reading Exchange: Attunement + History, TN7. First round of social contact only. Pre-Debate.

Almud (Attunement est. 4, "Political Observation" History 2pts = pool 4+5=9D) reads Himlensendt before debate.

P(Overwhelming, 9D TN7): P(≥2×Ob1=2 net) ≈ 90%.

**Overwhelming result:** "GM describes opponent's emotional state, tells, and assessment confidence in detail. +1D on the first two formal Exchanges in the same scene."

**Grand Debate bonus:** +1D on exchanges 1 and 2.

Almud base debate pool: Cognition 5 + "Political Rhetoric" History (est. 3pts+3) = 11D.
With Reading bonus: 12D exchanges 1–2, 11D exchanges 3–5.

**F124** — Reading Exchange provides substantial advantage when combined with high Attunement. Almud's Attunement gives near-guaranteed Overwhelming Reading, which then boots Debate exchanges. This synergy rewards Attunement investment beyond its Thread-perception role. P3 — intentional multi-use of Attunement stat.

---

## TEST B4-021 — Advancement: Test Track vs CP Interaction
**Coverage:** M-003, M-004 | TTRPG | PAST | — | — | — | — | Generic
**Mode A — Isolation**

### Test Track Advancement (§10.1)

Tested History advances automatically — increments after each successful roll with that History in a challenging situation. No CP cost.

### CP Menu rates
Attribute +1: current score × 3 CP. Score 4→5 = 12 CP. Score 5→6 = 15 CP. Score 6→7 = 18 CP.

**Session CP generation (average):** ~3–4 CP from Belief engagement.

**Time to max attribute (7):** Starting at 4: (12+15+18) = 45 CP. At 3 CP/session: 15 sessions. At 4 CP/session: 11 sessions.

**Test Track cap:** History cap = Memory score. Memory max 7. If Memory is not advanced, History cap is limited.

**Attribute advancement constraint on History:** History pool = Attribute + (History pts + 3). If Attribute is low, advancing History points has diminishing returns vs advancing the Attribute.

**F125** — CP optimization creates History vs Attribute tradeoff. For a social character (Presence 4, Circles History 3): advancing Presence 4→5 (12 CP) gives +1D to all social rolls. Advancing Circles History 3→4 via CP (3 CP) gives +1D only to Circles. CP efficiency favors History advancement until the pool construction formula equalizes. At typical Attribute 4 + History 6 = 10D: next Attribute point costs 12 CP for +1D on all rolls of that Attribute. Next History point costs 3 CP for +1D on one roll type. History is 4× more CP-efficient. Attribute advancement is primarily for derived stats (Health, Composure, Certainty max). P3 — intentional differentiation.

---

## TEST B4-022 — Faction Stats: Seasonal Cap Mechanics
**Coverage:** M-034, M-038 | TTRPG/BG/HYB | CROSS | FSTAT | All | — | Faction Leader
**Mode A — Isolation**

### Seasonal Cap: ±2 per stat per season

All sources combined. Domain Actions, Domain Echoes, direct events, seasonal accounting — all count toward ±2 cap per stat per season.

**Stress test: Church over-performing season**

Church events in one season:
- Heresy conviction of prominent figure: TC +2 (not a stat change — TC event, not faction stat)
- Domain Echo from won Grand Debate: Church Influence +1
- Seasonal accounting: Church Mandate +0 (no Overwhelming Stability)
- Royal Investigators blocked: Church Intel target not applicable
- Himlensendt's personal Domain Action (Heresy Investigation): Church Influence +1

Total Church Influence change: +1 + +1 = +2. At cap. One more source would be voided.

**If TC interaction would raise Church Mandate:** Say Baralta loses and TC rises → Church Mandate boost. But Mandate change from TC events vs faction stat changes — are these the same or different? TC changes (the shared track) are separate from faction stat (Mandate) changes? 

**[FLAG: TC value changes vs Church Mandate changes — clarify whether TC rising constitutes a Church faction stat change capped at ±2, or whether TC is an independent track uncapped. From §7.1-7.3: TC is an independent world track like TT and IP. Church Mandate is a faction stat. They interact but are separate numbers. Cap applies to faction stats (Mandate, etc.), not to the TC track itself.]**

**F126** — TC track is not capped by the ±2 seasonal faction stat rule. TC can rise multiple points per season from multiple sources simultaneously (passive drift, cross-clock effects, Church actions). Only faction stats are capped. TC is effectively uncapped per season. At worst-case: passive drift +1, TT>60 link +2, TC>40+IP>45 link +1, Church Mandate passive +1, Baralta Mandate drops +1 = TC +6 in one season. Confirmed intentional by the cascade design of the clock system. P3.

---

## TEST B4-023 — Löwenritter Coup: Martial Law Mechanics
**Coverage:** M-035 | TTRPG/HYB | PRES | FSTAT, TC, IP | Löwenritter, Crown | Ehrenwall | Löwenritter Knight
**Mode C — Scenario**

Post-coup scenario. Ehrenwall controls Valorsplatz. Martial Law declared.

**Martial Law (Ehrenfeld −1 Ob for Löwenritter ops, confirmed from T5 territory property).** Does Martial Law extend this −1 Ob to all Löwenritter-controlled territories post-coup?

**[FLAG: Martial Law mechanics not located in scanned text beyond T5 Fortification property. §8.9 Löwenritter section not scanned. What does post-coup Martial Law do mechanically — faction stats change? All Domain Actions at −1 Ob? Enforced Stability cap on other factions?]**

**F127** — Martial Law post-coup mechanics not in scanned text. §8.9 presumably contains Löwenritter unique actions including Martial Law declaration. Gap. P2.

---

## TEST B4-024 — Schoenland Unique Properties: IP Interaction
**Coverage:** M-032 | BG/HYB | FUT | IP, FSTAT | Crown, Altonian | — | Faction Leader
**Mode B — Interaction**

### Schoenland Trade Alliance securing procedure

"Schoenland active trade alliance: −2 IP/year." Procedure: not in §8.10 (not scanned). Known from T15: "Altonian Trade: +1 Wealth/season to any faction with Trade order here while route is open."

**IP 75+:** "Altonian vanguard deploys here." Schoenland T15 becomes a military deployment zone. Sea route severs. Trade order impossible. IP reduction via Schoenland becomes unavailable precisely when most needed.

**Window for alliance:** IP must be addressed before 75. At passive drift (+1 IP/season) + TT>45 effect (+1–2 IP/season): IP 20 → 75 takes approximately 15–25 seasons baseline. Realistic window before Schoenland becomes militarised: ~15 seasons at moderate escalation. Ample time if players prioritise.

**F128** — Schoenland IP reduction window is generous under moderate escalation but closes irreversibly at IP 75. Players who ignore IP until mid-campaign may find the easiest reduction mechanism (Schoenland trade) already lost. Intentional long-term consequence. P3.

---

## TEST B4-025 — Beliefs: CP Ceiling Calculation
**Coverage:** M-004 | TTRPG | CROSS | CERT | — | — | — | Generic
**Mode D — Edge Cases**

### Maximum CP generation per session

3 Beliefs, each active in scene (+1) + each challenged (+1) = 6 CP theoretical max per session.
Additional: Belief achieved (+2) + rewritten; Belief genuinely revised (+2).

In a highly focused session: 3 beliefs active and challenged + 1 achieved = 6 + 2 = 8 CP.

### CP ceiling hit

Attribute 7 (max): cannot advance further. History cap = Memory (max 7). All Histories at cap: no History advancement. New History 5 CP: possible until all Histories at cap. Inspiration: cap = Spirit. CP eventually has no target.

**What happens to excess CP?** No text found specifying CP overflow behavior. Once all advancement options are maxed, CP has no sink. Late-campaign characters potentially accumulate CP with nothing to spend.

**F129** — Late-campaign CP sink absent. Fully-advanced characters continue generating CP from Belief engagement with no expenditure target. Renown (§10.5) is described as a narrative permission system, not a CP sink. P2 — no late-game CP expenditure mechanic.

---

## TEST B4-026 — Resources: Territory Loss Cascade
**Coverage:** M-012, M-034 | BG/HYB | CROSS | FSTAT | Guilds, Crown | — | Faction Leader
**Mode C — Scenario**

### Territory Conquest → Resources Degradation

If Crown conquers Feldmark (T11, Guilds-controlled):
- All Guilds characters with Resources tied to Feldmark: −1D permanent Resources.
- Guilds faction Wealth: −1 (territory Prosperity lost from Guilds accounting).

If Guilds also loses Grauwald (T8):
- −1D permanent again for affected characters.
- Guilds Wealth: −1 again.

Starting Guilds Wealth 6D. After 2 territory losses: Wealth 4D. Domain Action Ob targets are now harder to reach.

**Characters with Resources in both territories: −2D permanent.** Starting pool Presence 4 + History 6 = 10D → 8D. Degraded but functional.

**F130** — Territory loss cascade hits personal Resources and faction Wealth simultaneously. Characters embedded in conquered territories face both personal degradation and faction weakening — double-hit. This creates strong incentive for characters to defend their economic territories personally. P3 — intentional.

---

## TEST B4-027 — Hybrid Mode: BG Orders vs TTRPG Domain Echo Same Season
**Coverage:** M-048, M-038 | HYB | CROSS | FSTAT, TT, TC | Crown, Church | Almud | Faction Leader
**Mode C — Scenario**

### Hybrid Season Structure (§12.3)

Strategic Phase (BG orders) + Personal Phase (TTRPG scenes). Seasonal cap shared: ±2 per stat.

**Conflict scenario:**

Strategic Phase: Crown places Govern order in Sudwald (T12). Crown Military 4D vs Ob2. Success: Crown Influence +1 in Sudwald.

Personal Phase: Almud debates Himlensendt (Grand Debate) and wins. Domain Echo: Church Influence −1 (equivalent: Crown Influence +1 via Consequence Style argument persuading Parliament).

Same stat (Crown Influence) affected twice in same season. Cap = ±2. Total: +1 (Govern) + +1 (Debate Echo) = +2. Exactly at cap. One more source would be voided.

**Player visibility:** Do players know they're approaching the cap mid-season? In BG mode, Strategic Phase resolves before Personal Phase. So after Strategic Phase, players know Crown Influence +1. In Personal Phase: they know the cap allows +1 more. Transparent if players track.

**F131** — Hybrid seasonal cap is tractable when players track it actively. The +2 cap across both phases creates genuine strategic resource allocation: do we spend our cap in Strategic Phase (reliable BG roll) or Personal Phase (narrative TTRPG scene)? Correct design tension. P3.

---

## TEST B4-028 — Ceiral Ritual: Procedure and Stakes
**Coverage:** M-055 (related) | TTRPG | PAST | TT, ThS, CERT, TC | Revolution, Church | Maret Uln | Practitioner
**Mode C — Scenario**

### Ceiral Ritual (§6.5 — partially scanned)

Maret Uln's Belief: "I will reconstruct the Ceiral Ritual before the Inquisitors find the text."

Awareness 5+ required (−2 Ob otherwise). Revolution Awareness 3 at start. Requires +2 Awareness before attempting without penalty.

"Ceiral Ritual attempted without Awareness 5+: +2 Ob."

**Scale of ritual:** Not fully scanned. From Community Weaving context: likely a large-scale collective Thread operation. Relational+ scale. Requires Einhir text access.

**TC implications:** If the Ceiral Ritual succeeds: likely TC event (public revelation of Thread knowledge). Per §7.2: "Player characters use Thread abilities in Church-observed contexts: TC +1 per event." A Ceiral Ritual performed publicly or observed by Church: TC +1 minimum, possibly much more if it constitutes a "heresy conviction" or large-scale Thread event.

**F132** — Ceiral Ritual success likely generates significant TC. A ritual explicitly associated with the Einhir (pre-Church) tradition, performed by the Revolution: theological threat to Church authority. If observed: TC spike probable. Players must choose between advancing the Ceiral Ritual and managing TC. P3 — intentional dilemma.

---

## TEST B4-029 — NPC: Maret Uln Unique Mechanics
**Coverage:** M-015, M-019, M-027 | TTRPG | CROSS | CERT, ThS, TS | Varfell, Revolution | Maret Uln | Practitioner
**Mode C — Scenario**

### Maret Uln Profile (§13.4)

TS: Unknown; practitioner-level (confirmed). Starting Loyalty to Varfell: 4. Pursuing Ceiral Ritual reconstruction.

**Unique mechanics:**
1. Southernmost access (Varfell connection)
2. Ceiral Ritual knowledge (Einhir text pursuit)
3. Revolution-adjacent (dual loyalty pressure)

**Loyalty 4 to Varfell:** Borderline. If Vaynard uses Maret as tool, Loyalty may drop. If Revolution secures Maret's loyalty: Varfell loses its best Southernmost asset.

**Dual faction pull (no mechanic specified):** No formal loyalty clock for Maret (unlike Torben). Loyalty is narrative, tracked by GM judgment, not a numbered track.

**F133** — Maret Uln has no formal loyalty track. Torben has a named TLK (Torben Loyalty Clock) but Maret Uln's Loyalty "4 to Varfell" is a narrative number with no per-season drain, no threshold mechanics, no recruitment procedure beyond player influence. Given Maret's importance as the only confirmed Ceiral Ritual practitioner, this is a significant NPC without mechanical definition. P2.

---

## TEST B4-030 — Full Edge Case: Simultaneous Catastrophes
**Coverage:** M-030, M-031, M-032, M-033 | HYB | CROSS | TT, TC, IP, ThS, CERT, FSTAT | All | Multiple | Multiple Archetypes
**Mode D — Edge Case Discovery (Catastrophe State)**

### Catastrophe State: All Clocks Above Midpoint + ThS Crisis

Starting from B3-030 Season 7 projection:
```
TT 64 | TC 36 | IP 35 | ThS 0
```

**ThS 0 — World Crisis:** Campaign event. Practitioners must resolve disjunction narratively or withdraw. What does ThS Crisis mean for the *world*? If ThS is world-level, Crisis should have world-level effects beyond individual practitioner consequences. No world-level ThS Crisis consequence specified in §5.9. Only practitioner-level (character must resolve or withdraw). This confirms F57 — the world track has no world-level terminal effect.

**TT 64 effects:** TC +2/season, IP +2/season. Full Monstrous entities active. Thread ops +1 Ob (from ThS Fractured state — but wait, if ThS is world, +1 Ob applies to all practitioners, not just the one with Fractured state).

**Simultaneous Season 7 events:**
1. ThS Crisis fires (campaign event)
2. IP 35 → crosses 30+ (already past — Torben tutoring demand active)
3. TT 64 drives TC to 38 (approaching 40 Ultimatum threshold)
4. Fractured ThS: all practitioners +1 Ob on Thread ops worldwide

**F134** — ThS world Crisis has no defined world-level mechanical consequence. The Fractured state gives +1 Ob to Thread ops, and Severed gives dissociative episodes — these are stated as per-practitioner. But if ThS is world-level, "the world is Fractured" should mean something beyond individual practitioners experiencing it. The world-track framing lacks any world-scale consequence text. Confirms F57 as structural contradiction, not just language. P1 — affirms existing finding.

**Stacking penalties at Season 7:**
- All practitioners: +1 Ob Thread ops (ThS Fractured world state, if world-level)
- TT>60: All Thread ops already more expensive by 2× TT gain
- Gap incursions: ~49%/session near any Gap
- ThS Crisis: campaign event requiring narrative resolution

**F135** — No defined ceiling on simultaneous penalty stacking. At Season 7, a practitioner attempting a Relational Weaving faces: Ob3 (base) + Fraying (if applicable) + ThS world Fractured (+1 Ob) + active Wounds (+1 per Wound) + near a Gap (+1 Ob). Potential Ob 7+ for a routine Relational Weaving. Ob cap is 10 (§1.3). Stack is bounded by cap. P3 — intentional; the Ob cap prevents absolute impossibility.

---

## FINDINGS SUMMARY — BATCH 04

### P1 Findings (2)
| # | Mechanic | Issue |
|---|----------|-------|
| F100 | M-045 Mass Combat | Damage formula not specified in §8.3 |
| F112 | M-034 Church | Church Stability TC brake fires at ≤5 but Church starts at 5 — permanently suppresses TC generation at game start |

F134 affirms existing F57 (ThS world Crisis has no world-level consequence).

### P2 Findings (17)
F96, F97, F99, F103, F106, F108, F111, F113, F115, F116, F119, F120, F123, F127, F129, F133

### P3 Findings (intentional)
F98, F101, F102, F104, F105, F107, F109, F110, F114, F117, F118, F121, F122, F124, F125, F126, F128, F130, F131, F132, F135

---

## Coverage Dimension Log — Batch 04

| Test ID | Mechanics | Mode | Temporal | Tracks | Factions | NPCs | Archetypes |
|---------|-----------|------|----------|--------|----------|------|------------|
| B4-001 | M-044 | TTRPG | PRES | — | Crown, Löwenritter | Ehrenwall | Löwenritter Knight |
| B4-002 | M-044 | TTRPG | PRES | — | Crown, Löwenritter | Ehrenwall | Löwenritter Knight |
| B4-003 | M-045 | TTRPG/BG | PRES | FSTAT | Löwenritter, Church | Ehrenwall | Löwenritter Knight, Knight Templar |
| B4-004 | M-045, M-046 | TTRPG/HYB | CROSS | TT, ThS | Revolution, Crown | — | Practitioner |
| B4-005 | M-023 | TTRPG | PRES | TT, ThS | Revolution | — | Practitioner |
| B4-006 | M-024 | TTRPG | CROSS | TT, ThS, CERT | — | — | Practitioner |
| B4-007 | M-025 | TTRPG | CROSS | TT, ThS, CERT | — | — | Practitioner |
| B4-008 | M-029 | TTRPG | PRES | CERT, TS | — | Maret Uln | Practitioner, Non-TS Scholar |
| B4-009 | M-034, M-035 | TTRPG/BG | PRES | FSTAT, TT, TC | Crown | — | Faction Leader |
| B4-010 | M-034, M-035 | TTRPG/BG | PRES | FSTAT, TC, IP | Church | Himlensendt | Faction Leader |
| B4-011 | M-034, M-035 | TTRPG/BG | PRES | FSTAT, TC, TS | Varfell, Church | Vaynard | Faction Leader |
| B4-012 | M-034, M-035 | TTRPG/BG | PRES | FSTAT, TC | Hafenmark, Church | Baralta | Faction Leader |
| B4-013 | M-034, M-035 | BG | CROSS | IP, FSTAT | Schoenland, Crown | — | Faction Leader |
| B4-014 | M-049, M-026 | TTRPG | CROSS | CE, TC, CERT | Church | Himlensendt | Knight Templar |
| B4-015 | M-042 | TTRPG | PRES | — | — | — | Generic |
| B4-016 | M-039 | TTRPG | PRES | — | — | — | Generic |
| B4-017 | M-045 | BG/HYB | FUT | FSTAT | Löwenritter, Crown | Ehrenwall | Faction Leader |
| B4-018 | M-039, M-040 | TTRPG | PRES | — | Crown, Niflhel | — | Riskbreaker, Inquisitor |
| B4-019 | M-017, M-054 | TTRPG | PAST | TS, ThS | Varfell, Church | Vaynard, Klapp | Practitioner |
| B4-020 | M-007, M-037 | TTRPG | PRES | COMP, CERT | Crown, Church | Almud, Himlensendt | Faction Leader |
| B4-021 | M-003, M-004 | TTRPG | PAST | — | — | — | Generic |
| B4-022 | M-034, M-038 | TTRPG/BG/HYB | CROSS | FSTAT | All | — | Faction Leader |
| B4-023 | M-035 | TTRPG/HYB | PRES | FSTAT, TC, IP | Löwenritter, Crown | Ehrenwall | Löwenritter Knight |
| B4-024 | M-032 | BG/HYB | FUT | IP, FSTAT | Crown, Altonian | — | Faction Leader |
| B4-025 | M-004 | TTRPG | CROSS | CERT | — | — | Generic |
| B4-026 | M-012, M-034 | BG/HYB | CROSS | FSTAT | Guilds, Crown | — | Faction Leader |
| B4-027 | M-048, M-038 | HYB | CROSS | FSTAT, TT, TC | Crown, Church | Almud | Faction Leader |
| B4-028 | M-055 | TTRPG | PAST | TT, ThS, TC | Revolution, Church | Maret Uln | Practitioner |
| B4-029 | M-015, M-019, M-027 | TTRPG | CROSS | CERT, ThS, TS | Varfell, Revolution | Maret Uln | Practitioner |
| B4-030 | M-030,031,032,033 | HYB | CROSS | TT,TC,IP,ThS,CERT | All | Multiple | Multiple |

---
*End sim_batch_04.md*
