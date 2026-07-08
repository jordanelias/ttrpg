# Board Game + Dice/Resolution Core — Findings (adversarially verified)

**Canonical heads:** `params/board_game.md` + `params/bg/*` (Board Game); `params/core.md`
(Dice/resolution core).

## 1. Tracker inventory

**`params/board_game.md` is a broken index** — confirmed exhaustively: all 18 links point to
`references/params_bg_*.md` paths that don't exist anywhere in the repo; the actual files live at
`params/bg/*.md` under a different naming scheme entirely. Every link in the CURRENT.md-designated
canonical head for Board Game is dead. **"Quasi-binomial"** (CURRENT.md's own term for the
resolver) appears nowhere else in the corpus — confirmed by full repo grep, one hit total
(`CURRENT.md:56` itself).

**Combat Pool has five textually distinct definitions in the live corpus**, confirmed verbatim by
independent re-check of every citation:
1. `params/core.md:161` — `max(5, History+6)`, Agility-independent, current canonical.
2. `combat_engine_v1/core.py:27-32` — matches (1) exactly.
3. `module_contracts.yaml:811` — matches (1) exactly.
4. `references/values_master.yaml:213` — `(Agility×2)+History+3`, the struck legacy form, filed
   under a phantom nonexistent source file.
5. `references/values_master.yaml:1151` — a second, differently-worded stale extraction of the
   same struck form.
6. `params/core.md:252` — an **in-file propagation miss inside the canonical head itself**: this
   line (in the same file as the correct definition, ~90 lines below it) still asserts "Fieldwork
   Pool... matching Combat Pool... construction," which stopped being true when line 161 was
   updated.

Only (4) and (5) are quarantined registry rot (with a genuine, specific quarantine banner that
does its job if a reader opens the file); (6) is a live, uncorrected propagation miss in the
canonical prose doc itself. Argue/Contest Pool and Mass-Battle's "Effective Combat Pool" are each
their own separately-maintained sibling formulas (not further Combat Pool inconsistencies, though
Contest's is self-aware and flags the divergence explicitly in its own doc, `social_contest_v30.
md:490`).

**Derived-stat schema is genuinely IN FLUX**: `references/descriptor_registry.yaml` (9 attributes,
3 groups, marked IN FLUX) folds Spirit→Will and Cognition→Acuity relative to `params/core.md`'s
canonical 10-attribute/4-group table — and the registry's alias mechanism, which exists
specifically to prevent exactly this kind of drift-related breakage, **drops Recall entirely**
(confirmed by critic re-check: `Recall`/`retention` appears nowhere in the registry, not as a key
or an alias) — a concrete instance of the alias design failing to cover a load-bearing attribute
that sets the per-History point cap and drives Fieldwork actions.

## 2. Interaction chain map

- The continuous σ-resolution engine feeds personal combat, Contest, Fieldwork, Thread, and Mass
  Battle "by construction," but `params/core.md:78` itself admits faction-scale pools sit at the
  small-pool boundary and would benefit from a dedicated sanity-check that was never run (partly
  mitigated for the sub-5D combat band by an existing continuity correction, but the
  faction-specific case remains unrun).
- The Obstacle Scale caps its exception band at Ob 20 in the general table but at **Ob 10 in the
  parallel Board Game Degree Table** — a live, self-flagged inconsistency (`[FLAGGED FOR REVIEW:
  ED-142-R]`), open.
- `combat_engine_v1`'s fixed `DECISIVE_OB=3` runs parallel to, and disconnected from, the general
  1–20 Obstacle Scale. **Correction on severity:** the producer originally framed this as
  contravening the holonic doctrine's "no scale-local dialect" guardrail; the critic pass found
  this mischaracterizes a **ratified, parity-tested resolver design** (`module_contracts.yaml:
  811` documents "base Ob 3 FIXED" as intentional, cited to ED-900/904/1085) as a doctrine
  violation. The real, narrower finding: it's functionally validated but not legible from the
  shared substrate doc alone — a legibility gap, not a governance breach.

## 3. Cascade check — the exporter gap (the strongest finding in this lane)

`references/engine_params/combat_engine_v1.json` is the CI-round-trip-checked generated export
meant to be the single source of truth the Godot port regenerates from, never hand-transcribes.
**Confirmed: the exporter (`tools/export_engine_params.py:53-58`) only imports `config.py`.**
`POOL_FLOOR`, `BASE_POOL`, and `resolution_pool()` are defined in the sibling module `core.py`,
which the exporter never touches — confirmed by grepping the generated JSON for these names
(zero hits). **Consequence: Combat Pool — the value this entire lane's audit centers on — is not
covered by the single-source-of-truth pipeline CLAUDE.md §5/§6 hold up as the successor
discipline.** A Godot implementer following "regenerate from JSON, never hand-transcribe" would
find no Pool formula there at all and would be forced back into hand-transcription — precisely
the ED-1050 failure mode the exporter was built to prevent.

## 4. Cognitive load

Resolving a single standard check requires 5–6 distinct sub-decisions/lookups in sequence:
attribute selection (ambiguous between the 9- and 10-attribute rosters), History-bonus lookup
capped by Recall, a TN judgment call (not a fixed constant), Ob assembly (discrete 6-band or
continuous fractional sum, or combat's own separate fixed-Ob+wound-Ob model), pool resolution
(discrete dice or continuous Normal-approximation — distinct arithmetic paths), Momentum
interaction (auto-successes cancellable by a rolled 1), and Degree banding with two different
exception thresholds depending on context (Ob 20 general vs. Ob 10 in Board Game). This is a
multi-table lookup chain, not a single-step roll.

## 5. Legibility gaps (severity per critic-corrected verdict)

- **P1 — Combat Pool multiply-defined**, and the one typed-export mechanism meant to prevent
  exactly this kind of drift doesn't actually cover this value (see §3).
- **P1 — `params/board_game.md` index is entirely broken** — every link 404s against the actual
  `params/bg/*` structure; this is the CURRENT.md-designated canonical head for the Board Game
  row.
- **P2 — Derived-stat schema (9-attribute IN-FLUX registry vs. 10-attribute canonical prose) IN
  FLUX**, with a genuine, previously-unflagged gap: the alias mechanism drops Recall entirely,
  undermining its own stated purpose.
- **P2 (mitigated) — `values_master.yaml`'s stale Combat Pool entries are genuinely
  quarantine-bannered** — risk is real only for a reader who bypasses the banner.
- **P2 — BG Degree Table's Ob-10 vs. core's Ob-20 exception** — already self-flagged in-file, open
  ED-142-R.
- **P2 (corrected framing) — `combat_engine_v1`'s fixed-Ob resolver dialect is a legibility gap,
  not a doctrine violation** (see §2 correction above) — functionally sound, just undocumented
  against the shared substrate doc.
- **P3 — "quasi-binomial" terminology drift**, unattested anywhere else in the corpus.

**Could a player predict their own pool size without cross-referencing ≥3 documents? No** —
confirmed: needs `params/core.md` (formula + Recall-cap rule), a separate Histories list, and, on
any secondary-source sanity-check, a real chance of landing on one of the two stale Agility-based
formulas still sitting in `values_master.yaml`.
