<!-- Repository State Armature (ED-IN-0077): this template mechanizes the ED-1094 discipline at the
     surface where it keeps failing. Fill the checklist; delete the guidance comments if you like. -->

## What & why
<!-- One or two sentences: the change and the need it addresses. -->

## Lane & IDs
- **Lane:** <!-- MB / PC / FI / SC / FA / WR / IN / GO / SE (or "cross-cutting IN") -->
- **IDs allocated:** <!-- ED-<LANE>-NNNN, PP-NNN — allocated from references/id_reservations.yaml (next_free, never max+1) -->

## ED-1094 checklist (merge ratifies PROPOSED contents by default)
- [ ] **Ratify-on-merge done in THIS PR:** any doc/doctrine/ledger entry this PR lands as `PROPOSED`/`provisional` has its `## Status:` line, ED `status`/`needs_jordan`, and `CURRENT.md` row flipped **in this same change** — not left for an unprompted follow-up.
- [ ] **Held-back items called out loudly ABOVE:** anything needing separate explicit sign-off beyond ordinary merge review is named prominently in this body as *held back* (never bundled silently into routine work).
- [ ] **Currency:** `CURRENT.md` / relevant index rows updated; no new drift introduced (`python tools/currency_consistency_check.py`).
- [ ] **Green locally:** `python tools/valoria_local.py --staged` and `python -m pytest tests/valoria -q` pass.

## Repository-state impact (optional)
<!-- If this PR moves a review_baseline.yaml ceiling or adds/retires an apparatus, note it:
     python tools/review_core.py --summary -->
