# CHAR — one table for where a capability enters a person's choice

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-08) — adopted as `rosters.yaml: tables.capability_uses` with the `role` column (`unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §3); `form` is implied by `role`. A `key` may also be a capability id from `descriptor_registry.yaml: capabilities` or the selectors `verb` / `verb.base`.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.2 row 2, §2 row 2, §7, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` ledger C-06, C-07, C-08, C-14, C-23; `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §3, §8, §11 U1-A steps 4–5). The body now follows the head: the yaml sample carries U1 §3's columns (`use, role, key, side, when, level, per, against, gain`; `role` replaces `form`, which it implies: `judgement` is `about_mid`, `gate` is `at_least`); `capability_use_sites` is U1 §3's map from a site to its one reader; the bullet "It does not absorb `vocation_attribute`" is deleted (U1 §1 deletes that roster; the governing attribute is the definition row's `base`); `test_k3_thread_sensitivity.py`'s name is verified (`engine/season/tests/test_k3_thread_sensitivity.py` exists); named tests, lands-it and tier added. `capability_factor` / `capability_admits` stand (U1 §8 adopts them).

**Lands in batch:** B04 (U1 §11 U1-A steps 4–5). **Depends on:** `01_CORE_capability_authoring_surface.md` Edits 1–4 (B04, first); B02 (the pin file).

## Status: PROPOSED

Written by the CHAR audit lane (`audits/02_CHAR_audit.md` §14). Ratifies nothing. Reference under
`CLAUDE.md` §0.05. It extends the existing owners and adds no capability system.

## What this changes in `engine/season/` at runtime

Nothing at the shipped values. Two attribute names that are literals inside modules today move to rows
of one roster table that the same modules read; a third row is added for the temper hook
(`02_CHAR_resolve_and_temper.md`), shipped at gain 0. The one-season hash of `build_realm(0)` is EQUAL.

## The problem, with evidence

The tree already owns the definition of a capability in two places that code reads:

| fact | owner (code reads it) |
|---|---|
| what an attribute is: key, name, aliases, scale 1–7 | `references/descriptor_registry.yaml: attributes` → `engine/substrate/descriptors.py` (`ATTRIBUTES`, `attribute_key`, `ATTRIBUTE_FLOOR`, `ATTRIBUTE_CEILING`) |
| which vocation a verb draws on | `engine/season/rosters.yaml: verb_capability` (`data/verbs.py::VERB_CAPABILITY`, `VOCATIONS`) |
| which attribute a vocation's pool starts from, and which opposes it | `rosters.yaml: vocation_attribute` (`VOCATION_ATTRIBUTE`, `VOCATION_OPPOSED_BY`) |
| which vocations a lifepath grants | `rosters.yaml: lifepaths`, `tables.lifepath_templates` |
| what a character holds | `references/npc_registry.yaml` rows: `stats:`, `lifepath:`, `ts:`, `heritage:` → `data/cast.py` |

Those rows are reached by one reader, `seam/wrappers/pool.py::faculty`, and a new vocation is already a
data edit (the loader refuses a vocation with no attribute row). The decision layer breaks the pattern
in three places:

1. `decision/options.py:1627` — `COMPETENCE_ATTRIBUTE = attribute_key("Attunement")`. Which attribute
   grades a told claim is a string in a module.
2. `queries/person_q.py::OwnStateReader` — `thread_sensitivity` is its own `Person` field with its own
   two hard-wired stems and an import-time `SystemExit` if `OWN_STATE_STEMS` grows
   (`person_q.py:1145-1148`). The registry calls the same thing `prac.thread_sensitivity`; nothing in
   the decision layer reads it by that key.
3. Every planned use (CR-93: Focus on the temperature, Reason on the forecast, an aptitude on
   uncontested candidates; CR-92: Grace, Presence, Attunement on others) would, built in the shape of
   (1), add one more named constant per use.

So "which capability feeds which choice" cannot be answered from data: `faculty`'s half can, the
decision layer's half is in function bodies.

## The resolution, decided

One roster table lists every place a capability changes an outcome, a person's own choice among them
(U1 §3: the one table, closed both ways). Ladder step 4: `vocation_attribute` was the precedent (a closed
table, both ways, refused at import); it is itself deleted by U1 §1, its `base`/`opposed_by` facts moving
to the definition row.

```yaml
# engine/season/rosters.yaml
capability_roles: {values: [dice, addend, opposes, edge, circumstance, resource, threshold, rate, judgement, gate]}
capability_use_sites:          # a map: site -> its one reader (U1 §3 amendment 7)
  told_claim_credit: decision/options.py::competence
  choice_temper:     decision/choose.py::temper
  own_state_gate:    queries/person_q.py::OwnStateReader (capability_admits)
tables:
  capability_uses:
    # EVERY PLACE A CAPABILITY CHANGES AN OUTCOME. One row per use. `use` is a member of
    # `capability_use_sites`. `role` is a `capability_roles` member; for the choice-side rows `judgement`
    # (a factor about the scale's mid-point, the form `options.competence` has) and `gate` (against a
    # fixture; Thread Sensitivity only, A-11). `key` is a capability id, a registry key (an attribute or a
    # practitioner stat) or the selectors `verb` / `verb.base`. `side` is whose sheet is read. `gain` names
    # the Fixture that scales it.
    rows:
      - {use: told_claim_credit, role: judgement, key: attr.social.attunement,  side: actor, gain: competence_gain}
      - {use: choice_temper,     role: judgement, key: attr.mind.focus,         side: actor, gain: temper_gain}
      - {use: own_state_gate,    role: gate,      key: prac.thread_sensitivity, side: actor, gain: thread_sensitivity_gate}
```

- **Closed both ways**: a `use` that no reader registers is refused at import, and a reader whose `use`
  has no row reads "no capability" (a factor of exactly 1, or UNKNOWN for a gate), never a default. The
  loader also refuses an unknown site, role or key, a field the role does not take, and a `gate` row on any
  key but `prac.thread_sensitivity` or at any site but `own_state_gate` / `told_retain` (U1 §11 U1-A step 4).
- **The factor forms are a closed set of two**, each implemented once in `engine/substrate/` beside the
  attribute scale: `about_mid(value, floor, ceiling, gain)` (role `judgement`) and `at_least(value,
  threshold)` (role `gate`). A third form is a code change and a design decision, which is the right
  price for a new axiom.
- **`Person.thread_sensitivity` stays a field** (its write-matrix row and its `ts:` loader are
  untouched); the row only names it by its registry key so the gate is listed with the other uses.
- The other sites and roles (`social_roll`, `fight`, `field`, `task`, `notice`, …; `dice`, `edge`, …) are
  U1 §3's and land with their readers (U1 §11 U1-A step 4, U1-E); this proposal carries the three
  choice-side rows.

**The interface the decision layer needs from the merged authoring surface** (for the holistic stage):

```
capability_factor(p: PersonInterior, use: str, fx) -> float | None     # about_mid uses; None = none held
capability_admits(p: PersonInterior, use: str, fx) -> bool | UNKNOWN    # at_least uses
View.odds(act, bands) -> float | None                                   # pools, opposition: never read directly
```

and nothing else: no attribute name, no scale constant and no pool arithmetic under `decision/`.

## The exact edits, by owner

1. `engine/season/rosters.yaml` — `capability_roles`, the map `capability_use_sites` and the table above.
2. `engine/season/data/rosters.py` — `_load_capability_uses`, on the retired `_load_vocation_attribute`'s
   shape (every `key` resolved through `substrate.descriptors`, every `gain` a registered Fixture, the
   refusals listed above).
3. `engine/substrate/descriptors.py` — `about_mid` and `at_least` beside `ATTRIBUTE_FLOOR` /
   `ATTRIBUTE_CEILING`; `scale_of(key)` returning `(floor, ceiling)` for an attribute or a practitioner
   stat.
4. `engine/season/decision/options.py::competence` — reads its key and role from the table; the
   module-level `COMPETENCE_ATTRIBUTE`, `COMPETENCE_MID` and the `assert` are deleted.
5. `engine/season/queries/person_q.py::OwnStateReader` — the gate's key and threshold fixture come from
   the row; the two stems stay (they are the grammar's).

## Gate, falsifier

- Hash EQUAL at seeds 0–2 (`build_realm`, one season).
- `engine/season/tests/test_cr19_competence_gain.py` and `engine/season/tests/test_k3_thread_sensitivity.py`
  (both exist) stay green unedited.
- Named tests (new, in `engine/season/tests/test_u1_capability_surface.py`, U1 §11 U1-A):
  `test_a_gate_row_on_another_capability_is_refused`, `test_a_use_with_no_registered_reader_is_refused`,
  `test_repointing_told_claim_credit_moves_the_factor_with_no_decision_edit` (the falsifier below, as a test).
- The B04 pin (`build_realm` hashes) is the working tree's reading before B01; re-read on the batch's base
  (C3-N27).
- Falsifier: re-point the `told_claim_credit` row at `attr.mind.perception` in a test's rebound table
  and a hand-built hearer's refracted confidence follows Perception and ignores Attunement, with no
  edit under `decision/`.

## NERS reading (§0.06)

- **N.** Without it each new use is a constant in a module, and Jordan cannot answer "what does Focus
  do" without reading Python. With it the question is one `grep` of one table.
- **R.** Customization of characters by data; a designer can move a use to another attribute and see
  the game respond. Complete: a use with no row is refused or reads nothing, never a silent default.
- **S.** One method for every capability factor in a choice (`about_mid`), consistent with the pool's
  table one row over.
- **E (last, as a ratio).** One table and two substrate functions against one constant per use,
  indefinitely.

## Cost class

Edit. Lands before or with CR-93's first build, so that build adds rows and no constants.

**Lands it.** The B04 batch (U1 §11 U1-A steps 4–5), an IN `valoria-author` session on `sonnet` (`high`),
closed by the batch's `methodology-close` once. **Hash movers.** None (control: the batch's base tree).
