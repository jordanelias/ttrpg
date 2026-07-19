# 2026-06-10 — Deprecation Map

**Contents:** `deprecation_map.md` — the legible map of every artifact this session filed as superseded/deprecated, with its current canonical replacement, status (full / PARTIAL), reason, and authority.

**What it guarantees:** a cold session pulls up the **current** master workplan (**v3**) and the **ratified** combat resolver (`designs/scene/combat_engine_v1/`), never a superseded workplan or the combat-v32 proposal lineage.

**Enforcement (not just a list):** the map is the readable companion to the hook-enforced `canon/supersession_register.yaml`, which `valoria_hooks.supersession_check()` reads to warn on any commit touching a superseded path. This session extended that register from 8 → 17 entries (workplans → v3; combat-v31/v32 proposals + the v32 NERS verdict → `combat_engine_v1`; the two Godot-framing docs → the conversion strategy; combat_v30 recorded as PARTIAL — lore retained, do not full-deprecate). Read-path banners are in place on both superseded workplans and the v32 verdict; the proposals' in-file banners + relocation to `deprecated/proposals/` are routed to master-v3 LB-13. See §5 of the map for the full model + the one residual (wiring the register into bootstrap fetch) that makes the commit-path warn fire on every session.
