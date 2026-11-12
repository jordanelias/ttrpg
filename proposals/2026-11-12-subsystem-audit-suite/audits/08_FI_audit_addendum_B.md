# FI — adversarial steelman audit, addendum B (the full design set, the detective precedent, the evidence interface)

## Status: REFERENCE (an audit addendum; resolves nothing at runtime)

## Read at: ad07a9a (working tree)

Addendum to `audits/08_FI_audit.md` (§0–§17, findings F-FI-01 to F-FI-10, resolutions R-01 to R-33). It does
not repeat that file; it completes the reading that file reports as not done, corrects it where the full
reading shows it wrong, and adds what the full design set, the precedent corpus and the surviving audits
warrant. Finding numbers continue at F-FI-11; resolution numbers continue at R-34. `PYTHONHASHSEED=0` on every
run; scratch output is under the session scratchpad, `runs/FI_B/`. Sections are appended as the reading
completes (brief, "write early"); §B1 is the reading record and is filled in as each item is finished.

## B1. What was read

**Read first, so as not to repeat:** `AUDIT_BRIEF.md` (in full); `audits/08_FI_audit.md` (§0–§17, in full);
`proposals/08_FI_01` to `08_FI_05` (in full); `dossiers/08_FI.md` (in full); `audits/12_ARCS_adjudication.md`
(in full: at this reading it is a 15-line stub whose verdict line reads *"written at the end of the pass …
this line is replaced"*; it adjudicates nothing yet, so no arc dependency is taken from it).

**The fieldwork design set, `.designs/systems/fieldwork/reference/` (19 files, 284 KB; ARCHIVED-NOT-CANON):**

| file | how read | what it is |
|---|---|---|
| `fieldwork_v30.md` (916 lines) and `fieldwork_v30_infill.md` | in full | one document in two parts (skeleton and prose): §1 Depth Axis, §2 pool and transitions, §3 exploration, §4 investigation, §5 socializing and knots, §6 exposure, §7–§12 |
| `investigation_systems_v30.md` (474 lines) | in full | the four "investigation systems": NPC Population Engine, Investigation Interface (scene graph, Case Board), Dialogue Lattice, Response Resolution Matrix |
| `knots_v30.md` (377 lines) | in full | the unified Knot synthesis (formation, five use-sites, strain, break, rupture) |
| `fieldwork_investigation.md`, `fieldwork_socializing.md`, `fieldwork_exploration.md`, `fieldwork_exposure.md`, `fieldwork_godot.md`, `fieldwork_bg_v30.md` (+infill), `fieldwork_hybrid_v30.md` (+infill) | in full, by line difference against the parent and its infill (every line not byte-identical to a parent line was read; the rest is the parent, read above) | atomized copies of the parent's §3–§6, §8–§10, made 2026-04-13 and since drifted (§B2, F-FI-16) |
| `fieldwork_rationale.md`, `fieldwork_editorial.md`, `fieldwork_summary.md` | in full | §13 rationale; §12 open items and the PP-632 redesign note; the §11 table |
| `fieldwork_flow_skeleton_v1.md` | in full (the last long table row was cut by the display at 1,300 characters; its subject, `apply_knot_loss` applying two of four consequence fields, was read) | a traced call structure of `systems/fieldwork/sim/` at `6545067`: three source files, two of which no longer exist |
| `fieldwork_v30_index.md`, `investigation_systems_v30_index.md` | in full | generated heading maps; no content |

