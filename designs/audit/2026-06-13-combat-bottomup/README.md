# Combat bottom-up deliverables — 2026-06-13 (PROVISIONAL)

**status: PROVISIONAL · PROPOSED, Jordan-vetoable · no ED IDs assigned · not bootstrapped-to-HEAD for ratification**

Bottom-up combat work from the 2026-06-13 session. Each artifact carries its own honesty block and
decision surface; nothing here is ratified, and the canonical `combat_engine_v1` is unchanged.

| File | Role |
|---|---|
| `combat_residuals_pob_f5_findings_2026-06-13.md` | J-33 residuals: F5 wound-penalty (keep canonical −1D; redirect optional) + PoB → percussion authority (`P_auth` derived; the "redundant" verdict retracted) |
| `combat_puncture_and_topdown_inventory_2026-06-13.md` | puncture model (head-shape splits puncture from percussion) + the top-down inventory of the engine (the weapon-vs-armour damage stack) |
| `combat_tradition_state_graph_gates_2026-06-13.md` | tradition system from flat σ-tuning → state-graph imposition gates (tradition success routes the exchange into its preferred node) |
| `percussion_authority.py` | derivation module: `P_auth` (percussion), `puncture_pressure`, `first_moment` (M₁ control-cost), `armour_defeat_mode` — self-test green |
| `tradition_gate.py` | illustrative gate-contest sketch + per-tradition node map — self-test green; NOT wired/balance-validated |

**Provisional means:** snapshot of in-progress design/audit, subject to revision (the tradition gate is
under adversarial review + reconciliation as of this commit; the weapon physics is being stress-tested).
Commit-grade adoption requires a bootstrapped re-pin, the named Jordan decisions, and ratification.
