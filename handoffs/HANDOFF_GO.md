# Handoff — GO (Godot)

Lane-scoped continuity for the `GO` (godot conversion) lane, per the `ED-<LANE>-NNNN` namespace
(`ED-IN-0001`) and `CLAUDE.md` §3's session-lane-scoping convention. Root `HANDOFF.md` is the
index; see it for cross-lane/global items.

No dedicated session work tracked directly under this lane as of the 2026-07-02 HANDOFF split
(the one concrete Godot artifact shipped so far — `tools/export_engine_params.py` — is filed
under `handoffs/HANDOFF_IN.md`'s ED-1052 item, since it's a typed-params/tooling deliverable,
not a port-implementation one). Governing spec: `designs/audit/2026-06-10-godot-conversion-strategy/
godot_conversion_strategy_v1.md` — status PROPOSED (Jordan-vetoable throughout), with an open
8-item register and unexecuted Gate-0 preconditions (KeyStore v2, base classes, RNG service).
See `CLAUDE.md` §6 for the full state-of-the-bridge summary before starting any "implementation"
task here — the skeleton is illustrative, not buildable (covers 1/27 modules, doesn't compile).

## Pending

(none.)

## Decisions

(none logged under this lane split.)

## Next actions

- **The strategy doc's 8-item open register** (`designs/audit/2026-06-10-godot-conversion-strategy/`)
  — downward Key delivery (ED-1006), Python end-state, faction-stat inversion, Key runtime
  form (needs K8), autoload ruling, first module target, D6 Church 4/4-vs-5/5, standing
  dockets. All unruled as of 2026-07-01. Also tracked at `decision_queue.md` item 10.
- **Gate-0 preconditions** — KeyStore v2 (valoria-game frozen since 05-04), spine base
  classes, RNG service, K8 performance verdict. None executed. Also tracked at
  `decision_queue.md` item 11.
