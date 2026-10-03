"""
systems/threadwork/sim/rendering.py — STRUCK at plan position 27 (WR-SCOPE remainder). No entry point.

This module held two `stubwire.stub_resolve` armature stubs (Pass 2l, OI-17): `apply_rs_strain` and
`check_calamity_threshold`. Position 27 had to WIRE each to a carrier the season architecture retains,
or STRIKE it with its reason. Both are struck, for the reasons below, and neither was wired into the
overview Mending Stability track (position 27's own constraint: that module was not a target; it stays, Jordan 2026-10-02: the
`systems/` folders are kept).

`apply_rs_strain(delta, source, world) -> RSState` — STRUCK: no carrier, at either reading.
  - As written, it moved the world-level Rendering Stability track (its declared dependency was
    `sim/peninsular/rs_track`, later `systems/overview/sim/rs_track.py`) — an overview clock plan
    position `29a` deleted (PR #450). The season has no analogue BY ARCHITECTURE:
    `engine/season/loop/census.py:37` says *"NO CLOCK GENERATES ANYTHING"*, and
    `engine/season/write_matrix.yaml:183` quotes the architecture's *"the three licensed clocks are
    exhaustive -- matter, bodies, and the confidence of a memory"*; no rendering or mending clock is
    among them.
  - Read as canon's reality-strain (`canon/philosophy/07_drift.md` §7.5 — the load a failed
    configuration can no longer bear lands on "its vicinity"), it would need a PLACE-side strain
    carrier. `engine/season/write_matrix.yaml` has none: its place-side rows (`Rung` stores, yield,
    envelope, dates, exists; `Site` condition, exists) carry matter, schedule and existence. The
    nearest, `(Site, condition)`, is a built works' material condition worn by the MATTER clock
    (`condition.worn`, DR-1), not the fabric of a vicinity. And the split of an operation's load
    between Coherence and the substrate is itself unruled (§7.5: "Posit, not derived ... Flagged
    2026-09-09; not resolved").
  - The one carrier the architecture does provide, `(Person, coherence)` (RES, `social: false`,
    written only by a seam Event — `engine/season/state/world.py`'s guard), is the PRACTITIONER's own
    configuration, and strain is by definition what does NOT land there (§7.5). It is also a matrix
    row with no carrier field — `engine/season/state/carriers.py`'s `Person` declares no `coherence`
    — and its `unproduced:` cell (H-47 / H-62) says no verb writes it. Wiring strain there would
    invert the function's meaning and add a writer the verb table does not license.

`check_calamity_threshold(world) -> CalamityState` — STRUCK: no carrier.
  - As written, it read the Rendering/Mending Stability bands down to the Rupture — the same deleted
    world tracks, and the same absence of a season analogue (`engine/season/loop/census.py:37`; the
    write matrix, above). The per-being crossing in `systems/threadwork/sim/coherence.py` is a
    different quantity, not this stub's subject.

The file is kept, holding only this record, because `registers/mechanics_index.yaml`'s
`rendering_stability` entry names it as `sim_module`.
"""
