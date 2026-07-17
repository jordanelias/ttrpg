"""
sim.provincial — Mass battle + provincial-scale faction actions

Status: [PROVISIONAL — Pass 2l armature stub 2026-05-17]

Modules:
  (mass-battle modules massbattle/units/tactic_cards/altonian_reinforcements
   moved to systems/mass_battle/sim/ — P4 slice 9, ED-IN-0071)
  - crown_initiative: Royal Progress / Great Work / Coronation Renewal (Royal Progress iter pending Pass 2h)
  - excommunication: Church excommunication action (calls personal/tribunal)
  - absolution: Church absolution action
  - council_solmund: Church 1/arc convocation
  - charter_liberties: Hafenmark Charter of Liberties
  - varfell_mandate_action: Varfell Mandate-gain action (placeholder name per VARFELL-MANDATE-ACTION-001; mechanic pending Jordan ratification)
  - varfell_territorial_acquisition: Varfell territorial mechanic (placeholder name per VARFELL-TERRITORIAL-ACQUISITION-001; canon authoring pending contamination audit)
  - infrastructure_reclamation: Church infrastructure-backed reclamation (Pass 2f, pending audit)
  - home_sanctuary: Church T9 protection mechanic (Pass 2f, pending audit)
  - parliamentary_transfer: Universal CB-required territorial transfer (Pass 2h, calls parliamentary_vote)
  - mass_seizure: Church Mass Seizure (PP-411, Pass 2f reconciliation pending)
  - treaty: Crown treaties + expiration (Pass 2h)
  - faction_action: AI action dispatch — GD-2 mandatory pass + stochastic candidates
"""
