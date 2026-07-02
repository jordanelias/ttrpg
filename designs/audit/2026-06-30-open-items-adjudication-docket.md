## Status: CURRENT — adjudication docket (open, awaiting the Month work-overview & architecture session)

# Open items for adjudication — Month work-overview & architecture session

Decision docket carrying the open items from the 2026-06-30 ecosystem review
(`designs/audit/2026-06-30-ecosystem-adversarial-review.md`) that need Jordan's call before further
tooling/porting work proceeds. Each item states the **question**, the **context**, the **options**,
a **recommendation** (advisory only), and the **artifacts** it touches. Nothing here has been decided
or applied — that is this session's job.

Two of these (D1, D2) carry `needs_jordan` in the ledger; D3 is a *scope* decision that a prior pass
got wrong and reverted; D4/D5 are low-stakes go-aheads.

---

## D1 — Combat parity oracle (ED-1050) · `needs_jordan`

**Question.** What are the canonical `ADEF_THRESHOLD` values, and how do we make the port match the oracle?

**Context.** The Godot conversion's master validation gate is Key-log parity vs the Python oracle. But
module #1 already disagrees with its oracle:
- `designs/scene/combat_engine_v1/config.py:29` — `ADEF_THRESHOLD={'none':0.0,'light':0.70,'medium':0.45,'heavy':0.72}` (non-monotonic: medium < light).
- `designs/godot/skeleton/.../combat_config.gd:58` — hand-edited to monotonic `{light:0.45,medium:0.60,heavy:0.72}` with an inline `[AUDIT-FIX]` note that itself says *"a parity re-sweep is required before this ships."*

`config.py` is **Class-C — calibrated against the harness, not canon**, so choosing the corrected
values is a **balance re-calibration**, not a transcription fix. **Note (learned this session):** combat
coefficients are actively iterated in `designs/scene/combat_engine_v1/` — this must be resolved *through*
the combat work, not independently. A prior pass that tried to settle a combat value out-of-band was
rejected (see D3).

**Options.** (a) Re-sweep the harness, set the monotonic values in `config.py` (canon), regenerate the
`.tres`/`.gd` from it. (b) Defer until the scene-combat re-baseline (the channel-leverage residual in
HANDOFF) lands, then re-derive thresholds from the settled engine. (c) Freeze the port's combat slice
until (a)/(b).

**Recommendation.** (b) then (a): fold the threshold decision into the scene-combat re-baseline rather
than a standalone sweep; never let the port correct its oracle in-place — fix `config.py`, then re-export.

**Artifacts.** ED-1050; `combat_engine_v1/config.py`; `designs/godot/skeleton/.../combat_config.gd`.

---

## D2 — Godot module-contract gaps (ED-1051) · `needs_jordan`

**Question.** In what order do we author the missing module home-docs, and who ratifies the assumption-grade resolvers?

**Context.** `references/module_contracts.yaml`: **10 of 27 modules have `doc: null`** — including
`engine_clock`, the temporal/accounting spine every system hangs off — and **11 of 27 resolvers are
`[ASSUMPTION]`-grade**, i.e. the determinism *class itself* is unratified. For a no-GM engine, an
unratified resolver enum is an unspecified determinism guarantee. The port is blocked beyond the combat
slice until these are authored + ratified.

**Options.** (a) Author the `doc:null` modules in dependency order, `engine_clock` first; run
`valoria-module-adjudicator` to ratify each `[ASSUMPTION]` resolver before the port consumes it.
(b) Ratify only the near-term-needed subset (whatever the next Godot slice touches). (c) Defer all until
Gate-0 spine exists.

**Recommendation.** (a) starting with `engine_clock` — it is load-bearing for every downstream system;
authoring it unblocks the most.

**Artifacts.** ED-1051; `references/module_contracts.yaml`; `skills/valoria-module-adjudicator`;
Godot strategy doc `designs/audit/2026-06-10-godot-conversion-strategy/`.

---

## D3 — Typed engine-params direction (ED-1052) · scope decision

**Question.** Do we want a typed, Godot-ingestible params layer now — and if so, what is the scope boundary given combat values are in flux?

**Context.** Params live as prose markdown; `values_master.yaml` is auto-extracted, stale, and stores
formulas as free-text English. A prior pass built a typed layer + a CI round-trip gate (PR #37) and was
**reverted** — it overstepped by asserting an "authoritative" Combat Pool formula (`(Agility × 2) +
weapon History (points + 3)`, min 5, PP-615) that **subsequent combat work has firmly rejected**. Key
learning: the ledger's "collapse the Combat Pool triple-definition" sub-action is itself a **combat-work
decision**, not resolvable by picking the `core.md` PP-615 line. The pipeline *mechanism* (typed JSON +
round-trip gate) was sound; the *content judgment* was not the tooling pass's to make.

**Options.** (a) Green-light a typed layer scoped to **genuinely-settled, non-combat** core values only
(TN, Ob scale, momentum range, MS decay) — explicitly excluding anything the combat/derived-stat work
touches (Combat Pool, Health, Stamina, thresholds) until those settle. (b) Hold the typed layer entirely
until the combat re-baseline + derived-stat schema exit "IN FLUX." (c) Drop the typed-layer approach in
favor of a different ingestion design.

**Recommendation.** (b) or a tightly-fenced (a). The value of a typed layer is real for Godot, but it is
only safe over *settled* numbers; typing anything in flux re-creates exactly the drift it's meant to kill.
If (a): the scope fence must be Jordan-drawn, not tool-inferred.

**Artifacts.** ED-1052 (open); reverted PR #37 (recoverable from git history if the direction is
approved); `descriptor_registry.yaml` ("IN FLUX"); `references/values_master.yaml` (stale).

---

## D4 — Navigation / structural-debt residual (ED-1054) · go-ahead

**Question.** Approve the file relocations that finish the navigation cleanup?

**Context.** Partially done in PR #33 (banners, README defer, size-cap). Residual is mostly mechanical
but moves files: (i) relocate ~850KB of narrative markdown out of `tests/` (the
`emergent_arc_skeleton_test_*` batches, session audits — prose mislabeled as tests) to
`designs/audit/` or `archives/`; (ii) move the retired session-log/checkpoint files
(`session_log_*.md`, `session_logs/`, `handoffs/`, `canon/session_checkpoint.md`) under `deprecated/`;
(iii) regenerate the stale `sim/README.md`, `sim/CONVENTIONS.md`, and `tools/README.md`.

**Options.** (a) Approve all three as a cleanup pass. (b) Approve (i)+(iii), hold (ii) if any tooling
still reads those paths (checked: only `ci_register_size_check` lists a couple — de-register alongside).
(c) Leave as-is (banners already warn agents off).

**Recommendation.** (a) — all three are safe and directly reduce agent-navigation hazard; (ii) needs the
`ci_register_size_check` entries removed in the same commit.

**Artifacts.** ED-1054; `tests/*.md`; the retired session files; `sim/README.md`, `sim/CONVENTIONS.md`,
`tools/README.md`.

---

## D5 — Freshness pin refresh · go-ahead

**Question.** Re-pin the 12 stale `canonical_sha__` values and flip the freshness gate to blocking?

**Context.** ED-1053 (resolved) made `freshness_gate` verify pins against the working tree; it found
**119/131 fresh, 12 stale** and runs report-only (`continue-on-error`). The 12 stale pins are
content-drift on canonical docs (their working-tree blob SHA moved past the pin). `freshness_gate.py
--update` re-pins them from the working tree.

**Options.** (a) Run `--update`, review the 12 re-pins, commit, then drop `continue-on-error` so the gate
blocks future drift. (b) Refresh the pins but keep report-only. (c) Leave report-only indefinitely.

**Recommendation.** (a) — the whole point of the pins is a blocking integrity signal; report-only is a
temporary state. Quick, low-stakes; only needs a nod that re-pinning to current content is intended.

**Artifacts.** `references/canonical_sources.yaml` (12 pins); `.github/workflows/valoria-ci.yml`
(integrity job, freshness step).

---

## Not in this docket (already owned elsewhere)

- **Scene-combat channel-leverage residual** — design-laden, tracked in `HANDOFF.md` "Next actions"
  (effectiveness-functions calibration; Jordan-owned).
- **Mass-battle bottom-up re-architecture (ED-1043)** — its own gated roadmap
  (`designs/audit/2026-06-30-massbattle-bottomup/`).
