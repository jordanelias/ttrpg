# F3 — Heresy Investigation Lifecycle Audit
## fieldwork_lifecycle_stress_01 sub-module F3

**Date:** 2026-05-10
**Mode:** A coverage + B (interaction chains)
**Scope:** Heresy Investigation (HI) → Excommunication Tribunal (ET) lifecycle, including extra-territorial jurisdiction (ED-670) and Church self-investigation exception (PP-349).
**Source authority:** social_contest_v30 §7.1 (ED-625); npc_behavior_v30 §2.13a (ED-670); PP-349.

This module supplements F2 Knot Lifecycle (commit `ddccbf9a`); F1 covered in R5; F4 follows.

---

## 1. Verification ledger entries

| ID | sim_variable | value | canonical_source | section | quoted_text |
|---|---|---|---|---|---|
| F3-L01 | hi_filing_prerequisites | CI ≥ 40, Church Mandate ≥ 4, Evidence Track ≥ 3 OR Obligation violation OR 2 prior Tribunal convictions | designs/scene/social_contest_v30.md | §7.1 | "Prerequisites: CI ≥ 40, Church Mandate ≥ 4, Evidence Track ≥ 3 on target from prior HI OR documented Obligation violation OR 2 prior Tribunal convictions." |
| F3-L02 | et_persuasion_track_start | Persuasion Track starts at 7 (Church near-decisive) | designs/scene/social_contest_v30.md | §7.1 | "Persuasion Track starts at **7** (Church near-decisive before Exchange 1 — institutional fait accompli)" |
| F3-L03 | et_no_corroboration | Accused gets no corroboration; Resistance halved | designs/scene/social_contest_v30.md | §7.1 | "No accused corroboration permitted" |
| F3-L04 | et_npc_consequences | CI +4; target Mandate −2; Certainty forced min(current, 2) | designs/scene/social_contest_v30.md | §7.1 | "Named NPC: CI +4; target Mandate −2; Certainty forced to min(current, 2); arc transition; all NPCs Disposition ≥ +1 to target check Certainty Ob 1 or lose Disposition −1." |
| F3-L05 | et_pc_consequences | Mandate −3; excluded from Parliamentary motions; Standing −2; Faith-companion Scar 1 | designs/scene/social_contest_v30.md | §7.1 | "Player Character: Faction Mandate −3; excluded from Parliamentary motions; Standing −2; Faith-conviction Companions make departure scene check (Scar 1)." |
| F3-L06 | act_of_contrition_revocation | Revocation requires Mandate ≥ 5, CI ≥ 50; result: Church Mandate −1, CI −1, lift | designs/scene/social_contest_v30.md | §7.1 | "Revocation — Act of Contrition:** Church declares (Mandate ≥ 5, CI ≥ 50 required). Target fulfils Obligation abjuring the violation. Result: Church Mandate −1, CI −1, Excommunication lifted." |
| F3-L07 | church_self_investigation_exception | Church doesn't file HI against own ordained acting in alignment | designs/scene/social_contest_v30.md | PP-349 | "**Church Self-Investigation Exception (PP-349):** The Church does not file Heresy Investigation against its own ordained members who are supporting Church interests." |
| F3-L08 | extra_territorial_jurisdiction | Heresy authority varies by territory controller per ED-670 | designs/npcs/npc_behavior_v30.md | §2.13a | "Church heresy designation operates differently inside vs outside Church-controlled territories:" |
| F3-L09 | hafenmark_sovereignty_block | Hafenmark blocks Church trials; extradition Ob 3 (Standing 0 only) | designs/npcs/npc_behavior_v30.md | §2.13a | "Hafenmark's Categorical Imperative framework treats Church heresy proceedings as extra-constitutional. Baralta will not permit Church trials on Hafenmark soil." |
| F3-L10 | parliamentary_stay_filing_prevention | Filing can be prevented while CI < 55 (Parliamentary Stay) | designs/scene/social_contest_v30.md | §7.1 | "*The correct strategic counter is preventing the filing, not defending at Tribunal. See §10.1 Parliamentary Stay. Filing can be prevented while CI < 55.*" |

---

## 2. Heresy lifecycle state machine

```
[No proceedings]
      │
      │ Inquisitor (rank ≥2) initiates HI
      │ (per faction_politics §2.3)
      ▼
[Heresy Investigation active]
      │   Evidence Track accumulates 0 → 1 → 2 → 3 → 4
      │
      │ At ET 3+ (and CI ≥ 40, Mandate ≥ 4), filing eligible
      │
      │ Parliamentary Stay (§10.1) can prevent filing if CI < 55
      │
      ▼
[Tribunal filed]   ◄── Church Self-Investigation Exception (PP-349)
      │                  blocks filing if target is ordained AND
      │                  acting in Church interests
      │
      │ Persuasion Track 7 (Church near-decisive)
      │ Exchange 1–3 (Inquisitor sets count)
      │ No corroboration; Resistance halved
      │
   ┌──┴──────────────────┐
   ▼                     ▼
[Excommunication]   [Acquittal — rare]
   │ Consequences fire (F3-L04 / F3-L05)
   │
   │ Act of Contrition path
   │ requires Mandate ≥ 5 AND CI ≥ 50
   ▼
[Revocation possible]
   │ Target fulfils Obligation abjuring violation
   │ Church Mandate −1, CI −1
   ▼
[Excommunication lifted]
   │
   ▼
[No proceedings] (cycle re-entrant)
```

**Extra-territorial wrinkle:** the entire pipeline gates on territory-controller per F3-L08. In Hafenmark (F3-L09), HI proceeds in absentia only — −2 Standing in Church territories but no mechanical effect in Hafenmark itself.

---

## 3. NERS at full grain — Heresy lifecycle (24 cells)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | F3-L01..L10 cover filing prerequisites, proceedings rules, consequences (NPC + PC), revocation, jurisdictional variation, self-investigation exception. Complete state machine. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Persuasion Track 7 start (F3-L02) implements "institutional fait accompli" mechanically. Exchange 1–3 cap (F3-L03) bounds duration. |
| Vertical | ✓ | ✓ | ✓ | ✓ | Personal-scale (named NPC F3-L04) and faction-scale consequences (Mandate −2, CI +3) both specified. |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Cross-system: HI couples to faction-politics (Inquisitor rank, faction Mandate), Conviction (Faith-companion Scar F3-L05), Standing track. Comprehensive. |
| Lateral | ✓ | ✓ | ✓ | ✓ | Lateral mechanics: Parliamentary Stay (F3-L10) is the strategic counter; Act of Contrition (F3-L06) is the revocation channel; extra-territorial jurisdiction (F3-L08, F3-L09) is the geographic gating. Three lateral channels for distinct strategic responses. |
| Horizontal | ⚠ | ✓ | ⚠ | ✓ | ⚠ N: PC consequence (F3-L05) is severe but fixed-magnitude; doesn't scale with Standing or campaign-stage. ⚠ R: Excommunicated PC has limited recovery options if Mandate < 5 sustained — may produce campaign deadlock for high-Faith-investment PCs. |

**Verdict:** 22/24 ✓, 2 ⚠ on Horizontal (PC severity scaling). Lifecycle is mature.

---

## 4. Mode B — Heresy interaction chains

### Chain 1: Filing → Persuasion Track 7 → consequences

Per F3-L01 prerequisites + F3-L02 Track-7 start: filing is hard to prevent (requires Parliamentary Stay before CI hits 55) and hard to defeat (Track 7 + halved Resistance). The strategic locus is filing-prevention, not Tribunal-defence per the canonical note "*The correct strategic counter is preventing the filing, not defending at Tribunal*" (F3-L10).

This is intentional design — Excommunication is meant to be a Sword of Damocles, not a recoverable contest. Players experience it as a structural threat to plan around, not a fair fight.

### Chain 2: Self-Investigation Exception → ordained PC immunity

PP-349 (F3-L07): the Church doesn't file HI against own ordained members supporting Church interests. An ordained PC (Conviction Faith primary, Standing in Church) is **structurally immune to internal Church HI** as long as they remain "in alignment with Church doctrine."

**Question:** what's the threshold for "in alignment"? Spec says "controversial methods" don't trigger investigation. So ordained PCs have wide latitude.

**However**, opposing factions can still file via PP-182 path (cross-reference). And the Church can investigate ordained members "actively working against Church interests" (specific examples: aiding the Restoration Movement, collaborating with Niflhel — though Niflhel is now dissolved per `npc_behavior §2.12 STRUCK`).

**Niflhel reference is now stale** post-2026-05-09 dissolution per G-L01. The PP-349 exception's specific example "collaborating with Niflhel" needs editorial review — should reference crime/underground networks per Jordan's 2026-05-09 decision (G-L03), not Niflhel.

### Chain 3: Extra-territorial jurisdiction → Hafenmark sovereignty block

Per F3-L08 + F3-L09: Hafenmark's Categorical Imperative framework blocks Church trials on Hafenmark soil. Church can:
- Request extradition (Diplomacy Ob 3; Hafenmark grants only if accused has Standing 0 in Hafenmark)
- Declare heretic in absentia (no Hafenmark mechanical effect; −2 Standing in Church territories)

This produces a **sanctuary mechanic**: PCs/NPCs threatened with Excommunication can flee to Hafenmark and operate from there. The −2 Church-Standing penalty is the cost; mechanical safety is the benefit.

### Chain 4: Act of Contrition revocation gate

Per F3-L06: revocation requires Church Mandate ≥ 5 AND CI ≥ 50. After the Excommunication itself reduces Church Mandate by some amount (the target's Mandate is −2 per F3-L04, but Church's own Mandate may not change directly), this can be hard to satisfy.

Specifically: if Church declares Excommunication when Mandate is exactly 5 and Mandate doesn't change as a result of the proceeding itself, revocation is technically possible. But the Mandate must stay ≥ 5 — any Mandate erosion (rival faction action, CI drift) would lock Excommunication permanent.

**Edge case:** can the Church revoke an Excommunication if Mandate drops below 5 mid-process? Per F3-L06, prerequisite is "Mandate ≥ 5 AND CI ≥ 50 required" — explicit prerequisite check. If Mandate drops below 5, revocation cannot fire. The Excommunication persists.

This produces a structural lock-in: high-CI Church campaigns can excommunicate widely, but if their Mandate drops, they cannot retract. Players counter by burning Mandate via faction actions targeting Church.

### Chain 5: PC consequence asymmetry vs NPC

F3-L04 (NPC) vs F3-L05 (PC) consequences:

| Effect | NPC | PC |
|---|---|---|
| Mandate | target Mandate −2 (their faction) | Faction Mandate −3 (their faction) |
| CI | +4 | (not specified — implicit Church benefit but unspecified for PC's faction) |
| Standing | not specified | Standing −2 |
| Certainty | forced to min(2) | not specified |
| Scar | Disposition cascade on +1 NPCs | Faith-Conviction Companions check Scar 1 |
| Politics | arc transition | excluded from Parliamentary motions |

**PC consequences hit harder on faction-coalition mechanics (Standing, Parliamentary motions) but lighter on Conviction/Certainty.** NPC consequences hit harder on individual interpretive state. Consistent with player-as-faction-leader design intent.

---

## 5. Mode D — Edge cases (compressed)

### Boundary
**EC-F3.B-01 [P3]:** Filing exactly at CI = 40 + Mandate = 4 + Evidence = 3. All thresholds met; filing eligible. Boundary canonically clean.

**EC-F3.B-02 [P2]:** Tribunal at exactly Persuasion Track 7 start; if Inquisitor sets Exchange count = 1 and the single exchange goes against Church, the Tribunal could resolve Acquittal at Track 5 or 6. Possible but rare (Track-7 start + halved-Resistance for accused makes successful defence unlikely).

### Cascade
**EC-F3.C-01 [P2]:** Excommunication of a faction leader (say, Almud as a King in Arc A Reformer) — per F3-L05, Faction Mandate −3 + Standing −2 + Parliamentary exclusion. For a King, this is a coronation crisis; succession may activate. Cascade into faction_succession_split mechanic.

### Regression
**EC-F3.R-01 [P3]:** Excommunicated PC seeks Act of Contrition; submits to Obligation. Church Mandate −1 on revocation could drop below 5 immediately, locking other Excommunications (cascade across cases). Strategic choice for Church: revoke or retain Excommunications based on Mandate cushion.

### Crunch cascade
**EC-F3.CR-01 [P3]:** Each NPC tracked for HI status, Evidence Track, Excommunication flag, jurisdictional state per current territory. Bookkeeping is non-trivial but bounded (per-NPC state).

### Ambiguity
**EC-F3.A-01 [P2 — STALE per Niflhel dissolution]:** Chain 2 surfaced this — PP-349's specific example "collaborating with Niflhel" is stale post-2026-05-09. Should be updated to reference crime/underground networks per Jordan's decision (G-L03). Surfaced finding, recommend follow-up PP.

**EC-F3.A-02 [P3]:** "Acting in alignment with Church doctrine" threshold (PP-349) — wide latitude. Game Master adjudication likely needed; bounded by faction_priority_tree behavior. Acceptable.

### Incoherence
**EC-F3.I-01 [P3]:** Hafenmark sovereignty block (F3-L09) creates safe-haven mechanic — narratively rich but mechanically asymmetric (Hafenmark non-Church PCs gain risk-free cover for Church-directed HI). Asymmetry is intentional per Categorical Imperative framing.

### Optimal play
**EC-F3.O-01 [P2]:** Players optimal: avoid Faith Conviction primary builds OR keep Mandate cushion ≥ 7 to absorb Excommunication consequences. High-Faith builds are "campaign-fragile" against Church campaigns — intentional, but produces meta-build pressure away from Faith primary in non-Church-aligned PCs.

---

## 6. Decision-shape findings

**Recommendation: F3.1 (preserve canonical Heresy Investigation lifecycle; one editorial follow-up: PP-349 stale Niflhel reference).**

**Rationale:**

1. **The lifecycle passes 22/24 NERS.** Two ⚠ on Horizontal (PC consequence severity scaling, recovery options) are intentional design — Excommunication is meant to be a sword-of-Damocles, not a fair fight (per F3-L10 strategic-counter framing).

2. **All canonical channels present and consistent.** Filing, proceedings, consequences, revocation, jurisdictional variation, self-investigation exception, sovereignty block — coherent state machine.

3. **One editorial defect surfaced (EC-F3.A-01):** PP-349's specific example "collaborating with Niflhel" is stale post-2026-05-09. Should be updated to reference crime/underground networks per Jordan's decision (G-L03 from setup_ignition_stress_01).

**Implementation:** No mechanical changes. PP-722 follow-up to update PP-349 example. (Authored separately to keep this stress test commit clean.)

---

## 7. Module status

| Item | Status |
|---|---|
| Canonical sources fetched at full depth (npc_behavior §2.13/§2.13a; social_contest §7.1; PP-349) | ✓ |
| Verification ledger (10 entries) | ✓ |
| Lifecycle state machine reconstructed | ✓ |
| NERS full-grain analysis (24 cells) | ✓ |
| Mode B chains (5) | ✓ |
| Mode D edge cases (8 across 7 categories) | ✓ |
| Decision-shape finding (F3.1 preserve canonical; PP-349 stale Niflhel example flagged) | ✓ |

**F3 Heresy Investigation lifecycle audit: verified.**

**Open follow-up:**

- `[GAP: PP-349 stale Niflhel example — should reference crime/underground networks per Jordan's 2026-05-09 decision G-L03. Class E editorial.]`
