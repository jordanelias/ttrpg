# Architecture Map & Workplan — 2026-06-06

Consolidated in-repo (Wave 0 / W0.7) from the 2026-06-06 architecture-mapping session.
This folder is the canonical home for that work; the prior chat-side `/outputs` drafts
are superseded by what lands here.

## Contents
- **valoria_master_workplan.md** — THE capstone. Typed item register (Waves 0-4),
  lifecycle state-machine, wave-dependency graph, decision queue. Key amendments:
  - §8   engine-framing: core engine is attribute-AGNOSTIC; no single universal resolver
         (one kernel, three regimes: discrete-pool / continuous-Normal / d+sigma).
  - §8.1 Attribute Registry -> **Descriptor Registry** (W1.13): all quantified-qualitative
         descriptors, typed by KIND, companion to BOTH core and the Key substrate.
  - §8.2 the grounded **descriptor-candidate inventory** (what collates into the registry).

## Pending into this folder (continuation)
- valoria_system_hierarchy_map.md and valoria_system_wiring_analysis.md — to be RECONCILED
  to §8 (they carry pre-§8 "universal resolver" language) before being committed here.
- supersession_register entries for the superseded drafts.

## Status
Wave 0 executing (direct commits to main). See the workplan §1 register for per-item status.
Live decisions await Jordan: W2.1/W2.4/W2.5/W2.6/W2.8/W2.9 + the resonance-style enumeration read.
