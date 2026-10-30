# ED-IN-0305 phase 5 — the missed behaviours of phases 1–4, how each is resolved, and the menu and presets that ride on them

## Status: PROPOSED (design reference; the code is the mechanism, CLAUDE.md §0.05)

Phases 1–4 (battle-side order of battle, recruiting rule, `army` Record and four verbs, the battle reading the record,
territory march/occupy/seize) closed with `methodology-close`. That close, and the session's own measurements, left a
list of behaviours the plan asks for that the built chain does not yet deliver. This is the list, the resolution of each
by the order CLAUDE.md §0 sets (precedent, then what the architecture wants; nothing here is a live design fork), and what
phase 5 builds. Every number is an ASSUMPTION Jordan may correct.

## 1. The missed behaviours and their resolutions

| # | Missed behaviour (evidence) | Resolution |
|---|---|---|
| M1 | **The shipped realm cannot field a surviving army.** A cohort is weight 2; `under_arms_cap(2)` = 20 troops; the engine routs a unit under 100 (`Unit.recalc_size`, `BLOCK_SIZE` 100) and a subunit under 80. Measured on `build_realm(0)`: the Crown holds 30 weight, Hafenmark and Varfell 20, the Church 2. | **Raise the scale and field the whole levy.** `TROOPS_PER_WEIGHT` 100 → 300 (one weight is a hamlet of three hundred; the engine's own tiers run 100–800). The Crown can then raise 900, a mid faction 600, the Church 60 (a garrison, which routs, and should). See M2 for why the whole levy can reach one field. |
| M2 | **An army's troops only fought if their cohort stood at the field**, but a cohort IS a place's population and does not march: with one cohort per town the biggest field was 20 troops. | **An army is where its commander is.** An army Record's troops all take the field when its holder (the commander) is present at the place (mustered there); otherwise that side fights as it always did. Cohorts stay home; their bodies carry the losses. (Replaces phase 3's "cohort present" rule.) |
| M3 | **`recruit` is unreachable in a built realm.** It demanded the cohort be `commit`ted to the faction; the realm seats cohorts with no commit. | A cohort may be raised by the faction that **governs where it lives** (`holder_faction_of` of its residence) as well as by one it is committed to. |
| M4 | **A cohort can be raised into two armies** (the cap is per army). | The cap counts what a cohort has already given **across every army** (`world_q.raised_from`). |
| M5 | **`move` onto a territory occupies it** (presence is occupation), so a lone member walks onto a defended territory and seizes it with no field. | A territory is an **arrival-only** place (`rosters.yaml: arrival_only_kinds`): `move` and `migrate` decline it. Only a won or unopposed `march` puts people there. |
| M6 | **An army parked on a territory cannot march again** (no settlement in its home chain, so no origin). | `sides_of` takes the nearest `march_target_kinds` rung in the home chain as the origin, and a territory musters the people **standing at it** (`world_q.standing_at`), not its whole subtree. |
| M7 | **Every territory field is a walled assault** (`fortification_of` averages the subtree's garrisons; any value above 0 is WALLS and overrides terrain). | Walls belong to a settlement. A field fought AT a territory has `fort_level` 0, so the territory's own terrain applies. |
| M8 | **An army side is provisioned, and the treasury debited, by the whole mustered weight**, though the battle ignores it. | The ration is billed on the weight of the cohorts the army drew its troops from. |
| M9 | **An army cannot shrink**: no way to disband a subformation or discharge troops, so a wrong type takes a slot for good and the cap counts it forever (NERS R: a mechanism that breaks at its extremes). | Two verbs, `disband_unit` (the subformation's troops return to the trained pool) and `discharge_troops` (trained troops return home). |
| M10 | Untagged assumptions (fall-back point read as a fraction of own strength; troop-type morale presets overridden by the side's morale; stat mirrors "provisional"). | Tagged `[ASSUMPTION; medium; Jordan to correct]` at the site, with the revert. |
| M11 | Winners are never depleted (the casualty ruling writes the loser only); casualties are uniform across a cohort's subformations. | **Not changed — RULED** (Jordan, 2026-09, clause (b): *casualties only on the losing side*). Recorded so it is not rediscovered as a defect. |

## 2. What phase 5 itself builds

**The military menu (headless).** `engine/season/harness/military_menu.py`: `menu(w, actor)` lists, for the faction the actor
is committed to, every legal army act with its bounds (mint if none; per cohort and troop type the most that may be raised;
types and roles that may be formed; assignments; orders; disband; discharge), plus **advisories** (a subformation under 80
troops routs at the first check, an army under 100 routs at once). `act_for(...)` builds the `Act`; `callback(select)`
returns a `dispatching_chooser` callback (`harness/play_surface.py`) so a client's choices ride the real fold. It adds no
rule: every refusal is the verb's own.

**Preset orders of battle (AI factions).** A pure plan in the module (`modules/mass_battle/troop_types/presets.py`, reached
by the composition row `mass_battle.army_preset`): given what a faction can raise (per type, from its cohorts and sites)
it returns the commands that mint-fill-organise an army — a battle line of the best heavy foot it can train, missile troops
behind, horse on the flanks, levy filling the rest — and the engine side (`harness/army_presets.py`) turns them into acts
for the faction's leader. Deterministic (no draw). It ships **OFF** (`Fixtures.army_presets`, default `False`), the
`field_provisioning` precedent, so no seeded run moves; its falsifiers run on hand-built worlds. The AI general planner
(who marches where) stays MB-08's.

## 3. Out of scope, named

H-166 (who may take UNHELD land). A Godot screen. Winner depletion (M11). The legacy headcount path's
`effective_size / size_max` quirk (its goldens would move).
