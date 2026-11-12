# WR · Pointer and register text for files only the orchestrator edits

## Status: PROPOSED

The first WR audit (`audits/09_WR_audit.md` §6.2, R-11, R-12, R-20) and its addendum B
(`audits/09_WR_audit_addendum_B.md` §6, §2.3 F-WR-22, R-31) reach conclusions whose edits land in
`CURRENT.md`, `engine/season/requirements.yaml` and `engine/season/hole_register.yaml`. The lanes edit none
of them. This file states each edit as text, so the orchestrator applies it, rejects it, or hands it on,
without re-deriving it.

## What it changes in `engine/season/` at runtime

**Nothing.** `CURRENT.md` is a process surface; `requirements.yaml` is read by
`register --requirements` (a doc-derived count that declares itself so) and `hole_register.yaml` by the
corpus grader, not by the loop. No hash moves.

## The edits

### 1 · `CURRENT.md:36`, the narrative-engine row (first audit R-11; ladder step 1, ED-IN-0232)

The row names a design written on the Key substrate that ED-IN-0232 retired; its successor is the set of
readings the season loop's harness runs. `CURRENT.md` is a pointer index (no figure, no narrative).

Old:

```
| **Narrative engine** | `narrative_engine_design_v2_churn.md` — ED-IN-0011 | — |
```

New:

```
| **Narrative engine** | `engine/season/harness/` — `storybar.py`, `chronicle.py`, `strife.py`, `arc.py` (readings over the log, never carriers: ED-IN-0225); design intent `proposals/2026-11-04-strife-flows/00_MASTER.md` | ED-IN-0011 (history); ED-IN-0232 | `registers/handoffs/HANDOFF_WR.md` |
```

`narrative_engine_design_v2_churn.md` stays where it is, unreferenced by the row (§1: `CURRENT.md` names
quarantined documents by bare filename, and this one is no longer a head).

### 2 · `CURRENT.md:28`, the threadwork row (first audit R-12; ladder step 1, ED-WR-0010)

Old:

```
| **Threadwork** | `threadwork_v30.md` + `thread_horizontal_integration_spec.md` | ED-WR-0010 (last row); `registers/handoffs/HANDOFF_WR.md` |
```

New, until `modules/threadwork/` exists:

```
| **Threadwork** | `systems/threadwork/sim/` (the oracle; Coherence per ED-WR-0010); design intent `threadwork_v30.md` (Part 3 superseded), `threadwork_applications.md`, `thread_horizontal_integration_spec.md` | ED-WR-0010 (last row); `registers/handoffs/HANDOFF_WR.md` |
```

After the move (`09_WR_threadwork_module.md` edit 2 as amended by `09_WR_B_threadwork_session_and_practitioner.md`
edit 2), the code head becomes `modules/threadwork/`. `references/module_contracts.yaml:301-303`'s
`registry_system:` line and `sim_module:` re-point are the first lane's edit 2 and are not repeated.

### 3 · `engine/season/requirements.yaml:173-176`, the settlement scale's note (first audit R-20; measured)

The note says "in the realm only `restore` executes (cohorts mending their own settlement's fabric since
`24f`)". At HEAD `restore` is not attempted in three or six seasons at seed 0 (first audit E-07, E-08): it
forms only on a Site-classed referent, none arises while no fabric crosses a floor, and 248 of the realm's
322 Sites are wear-0 kinds that cannot cross one (addendum F-WR-21).

Old (the clause):

```
in the realm only `restore` executes (cohorts mending
      their own settlement's fabric since `24f`), while `found`, `build` and `work` are formed and
      refused because no computed act declares a works (`H-165`);
```

New:

```
none of the four executes in the shipped realm: `restore` forms only
      on a Site below a floor and no Site crosses one (wear-0 dwellings and garrisons; no wound, H-235/H-236),
      and `found`, `build` and `work` are formed and refused because no computed act declares a works
      (`H-165`);
```

The row's `status:` is not moved by this text; whether it should be is `register --requirements`'s reading
after the edit.

### 4 · `engine/season/hole_register.yaml`, one sentence appended to each named row's cite

Each sentence is dated and attributed, in the register's own style; no row is re-graded except where
said.

| row | append to `cite` | re-grade? |
|---|---|---|
| H-05 | "CLOSED IN CODE (2026-11-12 audit, WR addendum B §6): `harness/populated.py::build_realm` is the world-generation roster's producer; `build_realm(0)` holds 83 persons (first WR audit E-13)." | `grade` stays; the empty cite is filled |
| H-27 | "THE DEFAULT IS SUPERSEDED IN FORM (2026-11-12, WR addendum B §6): the leg is held as `Person.travel_leg` (`loop/matter.py:831-843`), not as a Tenure's subject; CP-T10-01 changes the leg's element to a tuple and must update this row." | no |
| H-159 | "OBSERVED (2026-11-12, WR addendum B §3.2): at the shipped `oblige_term` 4, `tenure.closed` reads 27 in season 5 at seeds 0 and 2 and is absent at seed 1, whose duties were taken a season later; 'NOT MEASURED' is out of date." | no |
| H-168 | "STALE (2026-11-12, first WR audit E-07, E-08): `migrate` executes 16 of 116 (seed 0, three seasons) and 36 of 217 (six seasons) in computed play." | SE re-reads |
| H-172 | "CLOSED IN EFFECT (2026-11-12, first WR audit S2): same-season cross-person answers 128, 160, 158 at seed 0, three seasons." | to `measured`, closed |
| H-209 | "MEASUREMENT NOT REPRODUCIBLE AT ITS SEED (2026-11-12, WR addendum B F-WR-22): seed 0 has no `person.died` in six seasons at HEAD; the mechanism claim is unfalsified. Re-measure at seed 2 (two deaths in six seasons) or under the illness arm, after the duel path executes." | no |
| H-225 | as H-209, with "its counts are of death claims at two seasons, seeds 0 to 2; at HEAD, two seasons, seeds 0 and 1 hold no death". | no |
| H-230 | "PREMISE NO LONGER OCCURS AT SEED 0 (2026-11-12, WR addendum B F-WR-22): the King `p_npc_020` does not die in season 1, nor anyone in six seasons; re-measure on a seed or arm in which an office-holder dies." | no |
| H-107 | only if its row still reads open: "CLOSED (G1b, plan position 4, 2026-09-26): `Event.subject` is deleted (`state/carriers.py:259-268`); its two senses read through `state/attribution.py::actor_of` and `anchor_of`." | to closed |

## The gate that shows it worked

```sh
python tools/currency_consistency_check.py
python tools/freshness_gate.py
python -m engine.season.harness.register --requirements
```

Passes when the two currency tools report no new defect for the two `CURRENT.md` rows (a bare filename
that resolves; a code path that exists), and `register --requirements` loads the edited note.

## The falsifier

A `CURRENT.md` row naming a path that does not exist at HEAD; a register sentence citing a number its named
run does not show.

## NERS reading

Not a design object; process text. **S** is the one criterion that bears: one head per subsystem, named
where a reader looks first.

## Cost class

Edit (text only).
