# VALORIA — Parliamentary Territory Transfer

## Status: CANONICAL — Pass 2h authoring 2026-05-17

## Scope: canonical specification for the Parliamentary Territory Transfer mechanic. Universal (available to all parliamentary factions). v12c balance-validated at N=1000 (Crown 24.7% / Church 28.6% / Hafenmark 24.2% / Varfell 22.5% with this mechanic active per `faction_balance_convergence_v12c_2026-05-14.md` §4.4).

## GD constraints: GD-1 binding (produces territorial control delta, not victory trigger); GD-3 binding (extra-parliamentary factions per GD-3 cannot initiate Parliamentary Transfer — their participation in the political surface excludes formal Parliamentary motions).

## Source authority:
- `designs/audit/2026-05-14-balance-audit/faction_balance_convergence_v12c_2026-05-14.md` §4.4 (mechanic spec) + §4.4.1 (CB sources) + §5 (balance validation)
- `designs/audit/2026-05-14-balance-audit/part13_integrated_balance_solution_2026-05-14.md` (prior iteration RC-v1)
- `designs/scene/social_contest_v30.md` §10 (Parliamentary Vote contest engine used for resolution)
- `canon/02_canon_constraints.md` §B GD-1, §B GD-3
- `tests/sim/v17-integration/m6_faction_actions.py` (sim implementation, v17 line)

## Sim module: `sim/provincial/parliamentary_transfer.py`

---

## §1. Mechanic Specification

### §1.1 Action properties

| Field | Value |
|---|---|
| **Available to** | All parliamentary factions (including emergent factions promoted to parliamentary status per GD-3; excludes extra-parliamentary factions) |
| **Frequency** | 1 per arc per faction |
| **Prerequisite** | Casus Belli against the territory holder (see §3) |
| **Pool** | Proposer Influence |
| **Ob** | Holder Legitimacy + `PARL_MAJORITY_OB_BONUS` (default 2) |
| **Cost** | Action slot + CB consumption (whether transfer succeeds or fails) |

### §1.2 Outcome table

| Degree | Effect |
|---|---|
| Overwhelming | Territory transfers from holder to proposer. Holder Legitimacy −1. Transferred territory Accord = 1. |
| Success | Territory transfers from holder to proposer. Transferred territory Accord = 1. |
| Partial | Transfer fails this attempt. Proposer **gains CB vs holder** (enables retry next arc; replaces the consumed CB). |
| Failure | Transfer fails. Proposer Stability −1. Holder Legitimacy **+1** (public sympathy from defeated coercion attempt). |

### §1.3 Protections

- **Last-territory protection.** Cannot strip a faction's last territory. If holder has only 1 territory remaining, Parliamentary Transfer against that territory is blocked at the action-declaration stage (not rolled).
- **GD-3 extra-parliamentary block.** Promoted-RM and other extra-parliamentary emergent factions cannot initiate Parliamentary Transfer. They may participate in the broader political surface (treaties, alliances, CB economy) but cannot make formal Parliamentary motions.
- **Self-transfer block.** Proposer cannot target their own territory.

---

## §2. Four Modes

Per v12c §4.4, Parliamentary Transfer has four narrative-mechanical modes. The mode is declared at action proposal and shapes both the CB-source check and the post-roll narrative articulation. Mechanically, all four use the same Pool / Ob / Outcome table from §1; modes differ in *which CB sources qualify* and *what narrative articulation fires* on success.

| Mode | CB sources accepted | Narrative articulation |
|---|---|---|
| **Adversarial** | Military CB; Adjacent instability CB; Einhir Revival Partial CB; prior-Transfer Partial CB | Hostile motion. Holder opposes; proposer presses through political coalition. |
| **Consensual** | Negotiated agreement CB (both factions hold reciprocal action history showing alignment) | Both parties agree; vote is procedural. Holder Legitimacy not damaged on Failure. |
| **Punishment** | Faction has prior fault: Excommunication-related CB; Conviction Scar accumulation; Treaty-violation CB | Motion frames transfer as consequence. Holder cannot claim public sympathy on Failure (no L+1 — instead Holder Standing −1). |
| **Appeasement** | Crisis-stability CB: Peninsular Strain >= severe; Insurgency emergence in holder territory; war-readiness threshold met | Motion frames transfer as crisis-defusing. Accord granted +2 instead of +1 on Success (the transfer is meant to defuse, not subjugate). |

[PROVISIONAL: mode-specific narrative articulation effects beyond CB source filtering are derived from v12c §4.4 framing but specific outcome adjustments per mode (Punishment "no L+1", Appeasement "+2 Accord") are Pass 2h interpretive additions, not balance-validated. Confirm or strike in Pass 2k.]

---

## §3. Casus Belli Sources

Per v12c §4.4.1. CB is consumed on use whether transfer succeeds or fails. CB sources:

| Source | Mechanism |
|---|---|
| **Crown constitutional restoration** | Auto-justified when Crown territories < 6 (starting count). Crown faction only. Refreshes per arc if condition holds. |
| **Adjacent instability** | At arc boundary: if a faction has a territory at Accord ≤ 1, adjacent faction holders gain CB against that faction. CB persists 1 arc. |
| **Einhir Revival Partial** | Varfell gains CB vs territory holder per Einhir Revival Partial outcome (per `einhir_revival_v30.md`, Pass 2d pending). |
| **Parliamentary Transfer Partial** | Proposer gains CB vs holder for retry next arc. |
| **Military Conquest action** | Various existing military actions generate CB per `mass_battle_v30` and `faction_canon_v30` canonical rules. |
| **Treaty-violation CB** | Treaty broken or violated by holder generates CB to wronged party (per `treaty_expiration_v30.md` Pass 2h). |
| **Excommunication-related CB** | Church Excommunication action against a faction generates Punishment-mode CB for any Church-allied parliamentary faction. |
| **Conviction Scar accumulation** | Holder reaches Conviction Scar count threshold (≥3 per `conviction_track_v30.md` §1) → all parliamentary factions gain Punishment-mode CB. |

CB tracking is faction-pair-scoped (each `(proposer, holder)` pair has its own CB ledger). Multiple CB sources can stack on the same pair; consumption decrements one source per Parliamentary Transfer attempt.

---

## §4. Resolution via Parliamentary Vote Contest

Per §10 of `social_contest_v30.md`, Parliamentary Transfer's roll is **wrapped in** a formal Parliamentary Vote contest, not resolved as a single Pool-vs-Ob roll.

**Procedure:**
1. Proposer declares Parliamentary Transfer with target territory + mode + CB-source citation.
2. Vote contest opens per `social_contest_v30 §10`. All parliamentary factions vote.
3. Voting blocs computed by faction Standing relative to proposer + holder.
4. Vote result modifies the Pool-vs-Ob roll:
   - Majority bloc favoring proposer: Pool +1D
   - Majority bloc favoring holder: Pool −1D
   - Split bloc (no clear majority): no modifier; roll as canonized in §1
5. Pool-vs-Ob roll resolved per `params/core.md` Continuous Engine + degree table
6. Outcome applied per §1.2
7. **Parliamentary Stay** per `social_contest_v30 §10.1` ED-631 may be invoked by any parliamentary faction post-vote, post-roll. Stay invocation suspends transfer pending external resolution (treaty, Crown intervention, Conviction Scar resolution); stay-lift mechanism per §10.1.

**Sim integration:** `sim/provincial/parliamentary_transfer.py` invokes `sim/personal/parliamentary_vote.py` for the vote contest before computing the Pool-vs-Ob roll modifier. Stay handling routes through `sim/personal/parliamentary_stay.py`.

[PROVISIONAL: vote-bloc Pool modifier (+1D / −1D / 0) is Pass 2h interpretive — derived from §10 vote-contest semantics but specific dice-pool deltas not in v12c §4.4 or §10 spec. Confirm or revise in Pass 2k.]

---

## §5. Balance Validation

Per v12c §5 at N=1000 with this mechanic active alongside Einhir Revival, Altonian Reinforcements, Restoration Movement PT decay, Treaty Expiration, and EA throttle every-arc:

| Faction | Win % | End Legitimacy (avg) | End Territories (avg) |
|---|---|---|---|
| Crown | 24.7% | 3.4 | 0.8 |
| Church | 28.6% | 4.8 | 0.5 |
| Hafenmark | 24.2% | 5.6 | 0.6 |
| Varfell | 22.5% | 2.3 | 1.0 |

All factions in 20-30% band. Mean deviation from 25% target: 7.2pp.

Parliamentary Transfer fires ~2-4 times per campaign on average. Crown initiates ~60% of all Transfer attempts (constitutional restoration CB is the most frequent CB source). Punishment mode is rare (~5% of attempts); Adversarial is dominant (~75%); Consensual ~15%; Appeasement ~5%.

**Without Parliamentary Transfer mechanic active:** Crown 55-90% win rate dominance (Hafenmark + Varfell lack territorial acquisition vector; Crown compounds via Treaty hegemony). Parliamentary Transfer is one of the three v12c territorial-vector additions (Einhir Revival, Altonian Reinforcements, Parliamentary Transfer) that distributed territorial access across factions.

**Sensitivity:** `PARL_MAJORITY_OB_BONUS` = 2 is the tested value. Increasing to 3 reduces all-faction Transfer success rate by ~40%; decreasing to 1 makes Crown over-dominant (Crown I=5 vs others' L=4-5 makes Ob trivially low). 2 is the canonical default.

---

## §6. Tier-of-Test Status

**Tier 0 (Jordan-directed, v12c balance-validated):** ✓ This mechanic is one of the three v12c territorial vectors validated at N=1000. Per `canon/mechanics_index.yaml` entry `parliamentary_transfer`, `test_status: validated_n1000_v12c`.

**Implementation pending:** `sim/provincial/parliamentary_transfer.py` is a Pass 2l armature stub. Pass 2h canonization unblocks implementation. Implementation must reproduce v12c balance at N=1000 to retain `validated_n1000_v12c` status.

---

## §7. Cross-references

### Canon

- `designs/scene/social_contest_v30.md` §10 (Parliamentary Vote contest engine)
- `designs/scene/social_contest_v30.md` §10.1 (Parliamentary Stay ED-631)
- `designs/audit/2026-05-14-balance-audit/faction_balance_convergence_v12c_2026-05-14.md` §4.4 + §4.4.1 + §5
- `designs/provincial/treaty_expiration_v30.md` (Pass 2h companion — Treaty-violation CB source)
- `designs/provincial/einhir_revival_v30.md` (Pass 2d pending — Einhir Revival Partial CB source)
- `canon/02_canon_constraints.md` §B GD-1 (no victory trigger), §B GD-3 (extra-parliamentary status block)

### Sim

- `sim/provincial/parliamentary_transfer.py` — primary module
- `sim/personal/parliamentary_vote.py` — invoked for vote contest
- `sim/personal/parliamentary_stay.py` — invoked for stay handling
- `sim/provincial/faction_action.py` — action dispatch routes Transfer through here

### Mechanics index

`canon/mechanics_index.yaml` → `mechanics.parliamentary_transfer` — `canon_authoring_target` field updated from "(Pass 2h, pending)" to canonized path in companion commit.

---

## §8. Forward-flag (Pass 2k editorial-ledger batch)

| ID | Description | Resolution required |
|---|---|---|
| **PARL-MODE-DRIFT-001** | §2 mode-specific narrative effects (Punishment "no L+1 on Failure"; Appeasement "+2 Accord on Success") are Pass 2h interpretive additions, not in v12c §4.4 source. | Jordan ratify or strike. |
| **PARL-VOTE-MODIFIER-001** | §4 vote-bloc Pool modifiers (+1D / −1D / 0) are Pass 2h interpretive. Not in v12c §4.4 or social_contest §10. | Jordan ratify, revise, or strike. |
| **PARL-PROTECTION-001** | §1.3 self-transfer block is Pass 2h derived (obvious case not in v12c). | Confirm. |

[FLAG: these are derivation choices made during Pass 2h. Each surfaces a sub-mechanic that v12c balance validation didn't isolate. Resolution feeds canonized text update at Pass 2k.]

---

## §9. Status Declaration

[STATUS: CANONICAL — Pass 2h 2026-05-17. v12c-validated mechanic core (Pool / Ob / Outcomes / CB sources / Mode taxonomy) is canonized. Derivation choices (mode-specific narrative effects, vote-bloc Pool modifier, self-transfer protection) are [PROVISIONAL] pending Pass 2k Jordan ratification.]

---

## §10. Changelog

- **v30 init (2026-05-17, Pass 2h):** Initial canonization. Consolidates v12c §4.4 + §4.4.1 + §5 specification into formal canon doc. Defines 4-mode taxonomy (Adversarial / Consensual / Punishment / Appeasement). Specifies CB source table (8 sources). Wires resolution through Parliamentary Vote contest per social_contest §10 with Parliamentary Stay per §10.1. Forward-flags 3 derivation items to Pass 2k editorial-ledger.
