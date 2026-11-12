# SC-P7 — the social roll's capability inputs as data: complete the capability rows, one generic advantage source

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-02) — its `trait_advantages` source is not a second leverage source: it is read as the `edge` rows of the one `capability` source (`U5c_SC_one_obstacle_form.md` §3), whose home is the one `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` names. Edits 3 and 4 (a judge whom evidence moves more or less) stand, on the leverage channel.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.4 row SC-P7, §7; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-07, ledger C-04, C-09, C-12; `unified/U1_GLOSSARY.md` *capability* (not "vocation"); `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §1–§3, §5). SUPERSEDED in part: edits 1–3 are removed from the body and replaced by a pointer table (U1 decides them: `lie` → `deception` on the `capability:` column; `interrogate` → `inquiry` on the column; `trait_advantages` → `edge` rows of `capability_uses` at the `social_roll` site). Edit 4 stands and is completed: a trait is a capability row (kind `trait`, U1 §2), so the believed trait is read under the existing `CAPABILITY_CLAIM` prefix (`seam/wrappers/sigma.py:238`, `"capability:"`) and no `trait:` prefix or roster row is added. The check is restated on the uses table; lands-it and tier added. The "vocation" wording is replaced by "capability" in new text. The ED-IN-0350/A-26 opposition (`/2`) is A-79's `opposed_ob` on the trained score (D-U1-02). U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "Ob" → "obstacle" in prose (glossary *obstacle*); "faculty" → "capability"; "vocation" → "capability" (glossary *faculty*, *capability*).

**Lands in batch:** B04 (edit 4 with U1 §11 U1-A; the `edge` reader it feeds is U1-B in B05). **Depends on:** `01_CORE_capability_authoring_surface.md` (the column, B04); `02_CHAR_capability_uses_table.md` (the table, B04); `02_CHAR_which_ground_moves_whom.md` (the first trait rows, B24).

## Status: PROPOSED (edit 4 only; edits 1–3 superseded by U1)

Source: `audits/05_SC_audit.md` §14. It extends the existing owner (`engine/season/rosters.yaml`:
`verb_capability`, `vocation_attribute`, `vocation_opposed_by`, `advantage_sources`); it adds no
second capability system and no field to the module.

## What it changes in `engine/season/` at runtime

Edits 1 and 2 are data rows: `lie` and `interrogate` start drawing on a capability where they roll the
bare default today. In the shipped realm nobody holds a key or an attribute (`aperture 2 0`: pools
`[2]` for every actor; `build_realm(cast_attributes=False)`), so the hash is unchanged until a cast
row carries one. Edit 3 lets a trait become an advantage on the social roll by a roster row, with no
Python function per trait; with no such row authored it is inert.

## The problem (evidence)

1. **Sibling verbs draw differently.** `rosters.yaml: verb_capability` maps `tell → copying` and has
   no row for `lie`, which contests the same prize against the same hearer (`verb_table.yaml`: both
   `contests: "a standing"`, `counterparty: to`). `interrogate` (contested, `a proposition`) has none
   while the three graded inquiries map to `inquiry`. `determine` and `arrest` have none. A verb with
   no row rolls `pool_default` for every person (`seam/wrappers/pool.py::faculty`) and opposes at
   `obstacle_default` for every subject (`sigma.py::_opposition_of`).
2. **A trait cannot reach the roll without code.** `seam/wrappers/sigma.py::ADVANTAGE_SOURCES` binds
   each `advantage_sources` member to a Python function and refuses a member with none (`:151-157`).
   The one member is `effort`. So "a jurist is harder to move by an ad hoc plea" (NPC-071, core) or
   "unmoved by rhetoric, moved by evidence" (NPC-001, core) needs an engine edit per trait.
3. **Four rules of composition are constants in code:** the pool is `max(attribute, key)`
   (`pool.py:94-100`); the opposition is `max(key, opposing attribute)` (`sigma.py:133-136`); the
   obstacle is `opposition / 2.0` (`modules/social_contest/roll.py:141`); an absent key is
   `pool_default` while a held `0` is zero dice (`pool.py:97-99`), so a person trained to 1 rolls
   fewer dice than one untrained.

## The resolution, decided

- Rows 1–2 by sibling precedent (ladder step 4). `determine` and `arrest` are NOT decided here: which
  capability judges and which resists arrest is CR-92's design (B10-19, *the social attributes acting on
  others*), answered by plan (step 3).
- A trait reaches the roll through ONE generic member of the existing advantage door, defined in
  data (step 5: the door exists and is closed; a per-trait function is the scale-local dialect §10
  forbids).
- The `max` rules and the absent/held asymmetry are stated as the subsystem's interface in audit §14
  for the holistic stage; they belong to the pool reader's owner (CHAR/CORE) and are not re-decided in
  an SC file. The `/2` is SC-P5's.

## Exact edits, by owner

**Edits 1–3 are superseded** (U1, D-U1-07); what replaces each:

| edit | as first written | decided form | owner |
|---|---|---|---|
| 1 | `verb_capability: lie: copying` | `capability: deception` on the row that resolves a lie (`capability: none` with a note until `deception`'s definition row lands, `05_SC_hearing_capabilities.md`) | `verb_table.yaml` column (U1 §5) |
| 2 | `verb_capability: interrogate: inquiry` | `capability: inquiry` on `interrogate`'s row | `verb_table.yaml` column (U1 §5) |
| 3 | roster `trait_advantages`, source `trait`, `_trait_levels` | `edge` rows of `rosters.yaml: tables.capability_uses` at site `social_roll`, `side: actor` or `subject`, `when` keys, `level` a `LEVEL_SIGMA` name; summed by the `capability` leverage source's one reader (`advantage_sigma`, signed two-list form, ADV Edit A) | U1 §3; OBS §3 |

The first-written text of edit 3 is kept below for the record only (superseded):

   ```yaml
   trait_advantages:
     source: "SC-P7: a held trait as a named level on the social roll, by declaration"
     note: >-
       Each row: `trait` (an id the character surface defines), `side` (actor | subject), `when`
       (optional; keys closed against `verb_table` verbs, `arrangements.yaml: speech_kinds` ids,
       `proofs` and `genres`), `level` (a `sigma_leverage.LEVEL_SIGMA` name). `side: actor` adds the
       level to the actor's leverage; `side: subject` counts it AGAINST him, through the `defender`
       list `sigma_leverage.levels_to_net_sigma(aggressor, defender)` already subtracts (today
       `advantage_sigma` passes the aggressor list only). Refused at import: an unknown level, an
       unknown `when` key or value.
     values: []
   ```

   and `advantage_sources.values: [effort, trait]`. `seam/wrappers/sigma.py::ADVANTAGE_SOURCES`
   gains ONE function, `_trait_levels(fx, operands)`, which reads the rows whose `when` matches the
   act's operands and whose `trait` the named side holds. The side's traits arrive in `operands`
   (`{"effort": e, "actor_traits": (...), "subject_traits": (...)}`), filled by `contest_input` from
   the person record through whatever reader the character surface names (interface, audit §14 (c)).
   `modules/social_contest/roll.py` is unchanged: it already applies `leverage` as `net_boost`.
4. `engine/season/seam/wrappers/sigma.py::believed_input` — the believer's own traits are his to
   know; the subject's are `None` unless he holds a claim of them under the existing `CAPABILITY_CLAIM`
   rule (`sigma.py:238`, prefix `"capability:"` + the trait's capability id, value 0 or 1), since a trait
   is a capability row of kind `trait` (U1 §2): no new prefix and no roster row. Unknown → `None`, never
   a guess. The `edge` rows on the subject's side are evaluated against the believed value in the
   believed input and against the held value in the true input.

## Gate (execution artifact)

`engine/season/tests/test_sc01_provider.py` (exists): with one planted `capability_uses` row
(`{use: social_roll, role: edge, key: <a planted trait id>, side: subject, against: true, when: {plea: impugn_motive}, level: moderate}`) and a
subject holding the trait, `sigma.odds_of` for a `speak` carrying that plea differs from the same
`speak` with another plea, and equals it when the row is removed. `build_realm(0)` hashes equal with
the roster empty.

## Falsifier

A row naming a trait nobody holds changes no odds anywhere (run the realm with the planted row:
hash equal). A row with `level: "enormous"` refuses at import. Edit 4: a believer holding no
`capability:<trait>` claim of the subject reads `None` for it (named test
`test_sc01_provider.py::test_believed_input_reads_a_trait_only_from_a_held_claim`). If the planted row changes odds for a
verb its `when` does not name, the match is wrong.

## NERS reading

- **N**: lateral — combat already reads attributes into thresholds; the social roll's only lever
  beyond the pool is `effort`. Top-down — the provided characters are specified by exactly such
  traits (NPC-001, NPC-071).
- **R**: customisation of characters by data; anticipation by third parties (a known trait is a
  claim).
- **S**: one advantage door, one level vocabulary (`LEVEL_SIGMA`), no flat bonus and no obstacle edit.
- **E**: one roster, one function, two data rows.

## Cost class

Edits 1–3: superseded (carried by U1's batches). Edit 4: edit, after the character surface names its
trait carrier (done: U1 §2's `trait` kind).

**Lands it.** B04, an SC `valoria-author` session on `sonnet` (`high`) inside the capability batch, closed by
its `methodology-close` once. **Hash movers.** None (no trait row authored; control: the batch's base tree).
