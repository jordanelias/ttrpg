# Generational Transition Specification — Phase 2.11
# Date: 2026-04-18
# Location: Canonical in player_agency_v30 (proposed §11)

## Trigger
PC death OR Portrait Retirement (≥2 Convictions resolved, player chooses to retire).
Conviction Legacy fires (T8): one Conviction transforms and transfers to new character.

## Tracked Value Transition Behaviors

### PRESERVE (world state persists across generations)
- Evidence Tracks (knowledge persists in notes/records)
- All faction stats (Mandate, Wealth, Military, Influence, Stability)
- All derived values (Treasury, Legitimacy, Reputation, Discipline)
- All clocks (RS, TC, IP, PI, Strain, VTM, AER, Coup Counter)
- All settlement states (Prosperity/Defense/Order, governors, facilities)
- All NPC states (Disposition toward OTHER NPCs, Scars, Beliefs, arc position)
- Territory control, Accord, PT per territory
- Church infrastructure (4 axes per territory)
- RM Presence markers
- Card hands (faction Domain Action cards)

### TRANSFORM (modified inheritance)
- One Conviction: Legacy Conviction transfers as transformed version per T8
- Resources: floor(predecessor's Resources / 2) + new character's starting Resources (partial inheritance — wealth passes imperfectly through generations)

### RESET (new character starts fresh)
- Disposition toward PC: all NPCs reset to faction-default (new person, new relationships)
- Standing: reset to 0 (new character must prove themselves — Initiation Duty fires)
- Coherence: reset to 10 (new practitioner, untouched by Thread work)
- Thread Sensitivity: per new character's lifepath origin
- Certainty: per new character's lifepath origin
- Wounds: 0
- Stamina: full
- Momentum: 0
- Combat Reputation: 0 (nobody knows this person in combat)
- Exposure: 0 in all territories (nobody is watching this person yet)
- Skills: per new character lifepath (predecessor's skills die with them)
- Attributes: per new character lifepath

### BREAK (severed connections)
- All Knots: rupture (relational threads sever — Knotted NPCs receive Knot rupture strain per npc_behavior §5.0b)
- Companion relationships: departure scene for each companion (the companion was bonded to the person, not the player abstract). Companion returns to NPC pool at current Disposition toward faction.

### TRANSFER (institutional memory)
- Active Obligations: transfer to new character's faction (the institution remembers the commitment even if the individual doesn't). New character inherits obligation countdown and violation conditions.
- Renown: reset to 0, but predecessor's Renown ≥ 7 grants +1 starting Renown to successor (legacy reputation — "aren't you so-and-so's...?")

## Open Question Resolved
Resources = floor(predecessor / 2) + new character starting. Rationale: partial inheritance models imperfect wealth transfer (taxes, debts, distance, institutional claims on estate). A predecessor with Resources 6 bequeaths floor(6/2)=3 + new character's 1-2 starting = 4-5 total. Wealthy families provide advantage without eliminating the new character's economic challenge.

## Canon Compliance
- A12/C5: Knot rupture on death is metaphysically correct — the thread that was knotted no longer exists as a continuous being
- P-15: Coherence reset reflects new being-persistence layer — new consciousness, new rendering
- A10: New character must develop Thread sensitivity through confrontation, not inheritance (unless lifepath provides starting TS)
