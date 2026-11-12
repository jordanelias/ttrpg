# DICE — adversarial steelman audit, addendum B

## Status: REFERENCE (an audit addendum; resolves nothing at runtime)

## Read at: 618ec4b (working tree; the first audit was read at 601e715)

Addendum to `10_DICE_audit.md`. It does not edit that file or its five proposals. It covers what that
audit reported as unread, closes H-152 by a run, corrects the first audit where a second reading or a
probe shows it wrong, and writes the capability → axiom → resolver input map as a proposal
(`../proposals/10_DICE_capability_axiom_map.md`). Finding numbers continue from `F-DICE-14`.

## 0. Verdict on the first audit

The first audit's verdict stands and is sharpened: the dice engine is sound and is fed a constant.
What the first audit did not see, because it had not read `derived_stats_v30.md` and its sources, is
that the constant is not only a missing content switch. The design's capability model (attribute
doubled plus History plus three, floor five; derived resources that drain; a wound as a fraction of an
obstacle) and the season's built model (the score is the pool; the opponent's score halved is the
obstacle; a modifier is a named sigma level) are two different sets of RPG axioms, each internally
coherent, and the tree runs three of them at once: the season's, personal combat's, and mass battle's.
The sections below state each, by code, and the proposal names one authoring surface over them.

(Sections 1 to 6 follow; this head was written before the reading finished, per the brief.)

<!-- S1-S2 -->

## 3. H-152 closed

**The row** (`engine/season/hole_register.yaml:3439`): a `total`-casualty-model march loss removes a
person with no `person.died` Event. Its own falsifier, *"TO BE WRITTEN"*: sweep
`field_casualty_model = "total"`, fold a real march to `Lost`, and show that no `person.died` Event names
the removed person.

**The code, read.** `loop/effects_combat.py::_eff_march` (`:451-680`). At `:618` `dies = model == "total"`;
at `:668-672` each loser is named to the gate as `death_subjects(w, pid, loser_earns, fields=fields)` when
`dies`, else as a plain `Subject.entity`; at `:676-679` the same for a winner the arm kills (CR-24).
`state/gate.py::death_subjects` (`:1819-1832`) names the dying person earning the band's kinds plus
`person.died`, and each seat he holds earning `tenure.closed`. `verb_table.yaml:1077`'s `emits_note`
records that `march`'s `Won` and `Lost` bands declare both kinds since CP-T02-01 / HR-1 and cites this
row. The row's `owner:` (*"no owner exists yet"*) and its closing sentence (*"THE MISSING `person.died`
EVENT THIS ROW NAMES IS UNCHANGED AND STILL OPEN"*, dated 2026-09-29) predate that build and were not
updated by it.

**The probe that decides it** (E-B01; `probe_h152.py`, seed 0, the realm at build). A real `march`
(`p_npc_033` through `off_spymaster`, Crown, two mustered, on `set_s_036`, Church of Solmund, six
mustered), folded by the real driver at RESOLVE and then ENCOUNTER, so the resolution is the mass-battle
provider's and not a hand-built one (the existing test,
`engine/season/tests/test_cp_t02_01_death_names_seats.py:238`, constructs its `Resolution`).

| arm | Event kinds emitted | removed from `w.persons` | named by a `person.died` Event |
|---|---|---|---|
| `total` | `march.declared`, `field.lost`, `person.died`, `tenure.closed` | 8 | the same 8 |
| `scaled_by_degree` (shipped; control) | `march.declared`, `field.lost` | 0 | 0 |
| `total`, with `death_subjects` replaced by a version that does not add `person.died` (mutation) | `march.declared`, `field.lost` | 8 | 0 |

The mutation arm reproduces the row's defect exactly (eight people gone, nothing in the log), so the
probe can observe the failure it excludes; the unmutated arm does not show it. **H-152 is closed** (by
CP-T02-01, `1ef8d273` and before). Action, a register edit for whoever closes this suite: the row's head
to CLOSED citing CP-T02-01 and this probe; `owner:` to `state/gate.py::death_subjects`. It never was a
dice-engine row; the dossier filed it here by a path rule on `effects.py`.

**A by-product, for the MB lane (not a dice finding).** Under `total` the same field removed all eight
people: the two losing attackers and the six winning defenders, because CR-24's rule (*"under `total`
only a winner who took a casualty dies"*, `:585-588`) reads the winning side's survivor ratio, and a
winning side that lost anyone has a ratio below 1 for every member. `_eff_march`'s docstring gives the
reason for the rule as avoiding the case that *"would annihilate both sides"* (`:466`); at the one
fixture measured, both sides are annihilated anyway. `total` is a control arm and not shipped, so this
costs nothing in play; it means the control re-runs *"fighting costs everyone everything"* where its
note says *"losing costs everything"*. Cross-listed, not adjudicated.
