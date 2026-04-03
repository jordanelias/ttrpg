# Valoria Session Log — Updated

```yaml
session_id: 2026-04-02T_CANONICAL_SOURCE_INTEGRATION
phase: SESSION CLOSED
status: COMPLETE

## CANONICAL SOURCE PROVIDED
User provided original pre-project institutional documents. Key extractions:

### Church of Solmund structure (PP-194)
Holy See + Four Cardinals: Fortitude (Templars), Justice (Inquisitors), Prudence (Tithes/Charities), Temperance (Universities/Observatories).
Each Cardinal has BG mechanical role. Cardinal schism trigger at Church Stability = 2.
Church levy rule: Crown may raise 2/3 Church levies once/Year-End (Church Military −1, Crown Military +1 for 1 season).
Excommunication penance mechanic: Wealth −1/season (3 seasons) + one Senator Outward/season toward Church.

### Löwenritter structure (PP-194)
Lions' Table (military), Lions' Helm (naval), Riskbreakers (covert sub-unit), Civic Arm (Knights of Peace + Royal Investigators).
CORRECTION: Riskbreakers are a Löwenritter sub-unit, NOT an independent NPC faction.
Pre-coup: Riskbreakers fire under Löwenritter NPC AI Priority Tree.
Post-coup: Riskbreakers become Löwenritter player resource (1 free Priority action/season).

### Ministry canonical identity (PP-194)
Multiple ministries: Law, Guilds, Logothetes, Granaries, Pure Water.
Ministers nominated by Parliament, confirmed by Monarch.
Ministry of Guilds directly protects Guilds NPC from Economic Leverage when Ministry Mandate ≥ 2.
Parliament Nomination mechanic added (once/Year-End, three agenda options).

### Parliament Deposition mechanic (PP-194)
Canonical source: Parliament can depose Monarch if Holy See AND Imperial Court deem unfit.
BG mechanic: PI ≥ 5 + Church Mandate ≥ 5 + Crown Mandate ≤ 1 + 2+ Standing against Crown = deposition trigger.

### Guilds confirmed as Ministry of Guilds client
Guilds = economic NPC monitored by Ministry of Guilds. Trade protections linked to Ministry Mandate.

## CRITICAL OPEN ITEM — ED-107 (P1 BLOCKER)
Canonical source establishes duchy boundaries that DIFFER from v04 BG map:
- Hafenmark: Gransol (T2, duchy capital), Eidursjo (T8), Spartfell (T4)
- Varfell: Varfell (T9), Sigurdshalm (T10), Halvardshelm (T11), Oastad (T12)
- Crown/Valorsmark: Valorsplatz (T1), Lowenskyst (T7), Himmelenger (T3), Arnesheld (T5), Stillhelm (T13)
- Himmelenger is Crown territory with Church cathedral presence — NOT Church-controlled

If canonical: Guilds NPC and Niflhel NPC lose starting territorial positions.
Major balance implication. USER DECISION REQUIRED before map reassignment.

## WHAT WAS NOT APPLIED (awaiting ED-107 decision)
- Territory starting control corrections
- Faction capital corrections (Hafenmark capital = Gransol T2, not Hafenvalor T6)
- Himmelenger as Crown territory

## Gate: PASS 22/22

## Commits
31d6a80: PP-194 + ED-107

next_session_start:
  priority_1: "Run freshness_gate.py check first."
  priority_2: "ED-107 decision: does BG map use canonical duchy geography or gameplay abstraction? Answer determines whether T2/T4/T7/T8/T10/T11/T12 reassignments apply."
  priority_3: "If canonical map: full territory reassignment pass required (affects starting positions, faction VCs, opening strategies, all adjacency-based mechanics)."
  priority_4: "BAL-BG-02: balance analysis with corrected values."
```
