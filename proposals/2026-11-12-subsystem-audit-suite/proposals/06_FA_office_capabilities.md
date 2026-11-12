# FA-P6 — skill where governance uses it: skills for the contested governance verbs, a seat's skill, founding content as data

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-11) — the judge's capability is named `law`, not `judgment`: SC's `05_SC_hearing_capabilities.md` authors the same capability under that name, one thing takes one name, and `judgment` collides with the uses table's role `judgement`. `determine: law`, `interrogate: inquiry`, `arrest: arms` are the decided verb values (`unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §5), written on the verb row's `capability:` column; the definition row lives in `references/descriptor_registry.yaml: capabilities`.

Reconciled: 2026-11-12, U5d closure — folded **A-12** (a seat may carry a modifier) and **A-7** (two inputs to a roll). The sentence "a seat's vocation is never a prerequisite. It is a reason" stands for gating (A-11: capability gates nothing), and edit 3's `vocation:` key stands. Added by A-12: a seat row may also carry a modifier on the rolls made through it; this file does not author its number or home, which is `14_VERBS_BINDING_C_turnover.md`'s standing term and the institutions kit's (`15_INSTITUTIONS_SYNTHESIS_A_one_kit.md`), read by the one obstacle composer (`U5c_SC_one_obstacle_form.md`) so that regard and office are not counted twice. Edit 4's "the one reader" is therefore no longer the only reader of a seat's row. The pool's two inputs and the capability home are `U5a_capability_home_and_two_inputs.md`'s; edits 1–2 land on that home. The Layer 1 text for `04` §B.7 is owed by the ruling, not applied.

Reconciled: 2026-11-12, wave 3 (W3-3) — the body follows the two heads above. Applied: D-U1-07 and R3 §2 (edits 1–2, the interface paragraph, the gate and the falsifier move from `rosters.yaml: verb_capability` / `vocation_attribute` / `judgment` to the verb row's `capability:` column and `law`; this file adds no definition row, `law`'s is `05_SC_hearing_capabilities.md`'s); C3-C15 and R3 §1 Option A (edit 3's key is row data on the seat's `offices.yaml` row, read through `data.rosters.SEAT_ROW_BY_ID`; no `Office` field, no grant-payload stamp); C-16 and the glossary's *capability* row (the key is named `capability:`, not `vocation:`); D-U1-01 (a seat's modifier is the seat row's `modifier:` read by the `office` leverage source; the second head's "standing term" and "institutions kit" homes are superseded by it); 7b-2 (the regard reader is `person_q.regard(p, referent, fx)`, `person_q.py:424`, already imported by `decision/choose.py:44`; named tests); 7b-0 (tier); U3 (batch B04). U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "vocation" → "capability" in prose (glossary *capability*, OWNERS C-16). A-98 vocabulary lane (2026-11-12, A-98; ledger `unified/work/A98_SWEEP.md`): "capability" in prose → skill (25).

## Status: PROPOSED

Lands in batch: B04 (capability home), after `05_SC_hearing_capabilities.md` (the `law` definition row) and `U5a_capability_home_and_two_inputs.md` (the `capability:` column); it ships no skill content.
Depends on: `U5a_capability_home_and_two_inputs.md` (B04), `05_SC_hearing_capabilities.md` (B04); D-U1-01a's seat-row `modifier:` column lands separately (B05) and is not read here.

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (L-10) — the pool reader's owner is `seam/wrappers/pool.py::faculty` (`:78`), re-exported by `sigma.py:105`; one citation corrected. No edit of the proposal changed.

Source: `audits/06_FA_audit.md` §14, §15 (c), (d), F-FA-05; hole rows H-126, H-207 (the positional conferee).

## What it changes in `engine/season/` at runtime

1. `determine`, `interrogate` and `arrest` roll the actor's skill for a named skill instead of
   `pool_default` for everyone. With nobody holding the new skill and no attribute authored, each still
   rolls `pool_default`, so the rows ship hash EQUAL until content gives someone a rank in it (the state
   `argue` and `inquiry` shipped in at REM-30).
2. A seat's row may name the skill its post calls on. One reader uses it: the ranking of candidates for
   a `confer`. It gates nothing.
3. Three constants that say what a founded office is granted move from Python to `offices.yaml`. No
   behaviour changes.

It adds no skill system. The owner is the one decided by D-U1-07: a skill is defined at
`references/descriptor_registry.yaml: capabilities` (exported by `tools/export_descriptors.py` and read by
`engine/substrate/descriptors.py`), and the verb that tests it names it in its own row's `capability:`
column (`verb_table.yaml`, `U5a_capability_home_and_two_inputs.md`), read at the roll by
`seam/wrappers/pool.py` (`faculty`, `:78`, re-exported by `sigma.py:105`, for the pool; `score` for the
opposition, D-U1-02). `rosters.yaml: verb_capability` and `vocation_attribute` are deleted by CAP A2/A3.

## The problem (evidence)

- `rosters.yaml: verb_capability` (`:1498-1549`) has values for `tell`, `speak`, `argue`, `research`,
  `examine`, `surveil`, `fight`, `accept`, `capture`. It has none for `determine`, `interrogate` or
  `arrest`, which are contested (`contests: a proposition`, `a proposition`, `a standing`). `faculty` falls
  through to `pool_default` for a verb with no row, so a judge of thirty years and a clerk given the bench
  yesterday roll the same dice.
- `aperture 2 0` POOLS ROLLED (audit E-3): every pool the seam rolled was 2, with no two actors differing in
  any verb; no governance verb reached a roll.
- Whom a conferrer seats is positional: every `confer(seat, to=*)` candidate ties on score and the stable
  sort seats the lowest-id person he knows (H-207's cite, C2/C4). Nothing about the candidate or the post is
  read.
- `loop/predicates.py:255-257`: `FOUNDER_KEEPS = ("confer", "revoke")`, `FOUNDED_CONFERRAL = "appointed"`,
  `FOUNDED_REVOCATION = "rung_above_in_holdings"` are content, each already marked `[ASSUMPTION … Jordan to
  correct]`, sitting in code where a designer cannot reach them.

## The resolution, decided

Extend the one owner; state the interface; leave the names to Jordan. Ladder step 4: REM-30 landed
`argue` and `inquiry` rows "before their first writer" for exactly this reason, and CR-20 closed the
skill → attribute table both ways so a skill cannot be half-declared.

The ruled axiom is kept: "capability supplies dice and gates nothing" (`rosters.yaml: verb_capability`'s
own source line; A-11). So the skill a seat row names is never a prerequisite. It is a reason: something a conferrer may
weigh, in the one place the engine currently weighs nothing.

## Exact edits, by owner

**1. `engine/season/verb_table.yaml`, the `capability:` column** (the U5a column; values decided in
`unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §5). `determine: law`, `interrogate: inquiry`,
`arrest: arms`. `law` is a new row of `references/descriptor_registry.yaml: capabilities` authored by
`05_SC_hearing_capabilities.md`; this file adds no definition. Until `law`'s row lands, lane A's interim
value `determine: argue` (branch B01) stands, then becomes `law` (D-U1-07).

**2. (Withdrawn into edit 1.)** The former `vocation_attribute: judgment → attr.mind.acuity` row is not
made: the attribute a skill starts from is its definition row's `base` (C-05), owned by the SC file
that authors `law`. The question this edit carried (Reason, or Presence if a bench is read as carrying the
room) goes with it to that row.

**3. `engine/season/offices.yaml`, row data, not a `Seat` field (C3-C15).** A seat row may carry
`capability: <a member of descriptors.CAPABILITIES> | null` (the key named `capability:`, not `vocation:`,
C-16). Loader: `data/rosters.py::_load_offices` refuses a value that is not a defined skill, naming the
row. No `Office` field is added and nothing is stamped onto the `hold` grant: `04` §B.7's `Seat` tuple is
closed ("NEVER: … a modifier of any kind"; "a seat adds no verb and no modifier"), and the one reader (edit
4) reads the row through `data.rosters.SEAT_ROW_BY_ID[seat_id]["capability"]` (`data/rosters.py:196`;
`decision/` may import `data/`, `04:656`). No shipped row names one in the first commit. Candidate content,
for Jordan: the Royal Marshal, the Military Commander and the Military Jarl `arms`; the Cardinal of Justice
and the Senior Inquisitor `law` or `inquiry`; the Chief Parliamentary Clerk `copying`.

**4. The one reader: ranking the conferee.** `decision/choose.py`'s score for a `confer` candidate gains a
term over its `to` operand, through the existing terms table (`choose.score_terms`), never a branch on the
verb name:

- the conferrer's regard for `to`, read by `queries/person_q.py::regard(p, referent, fx)` (`:424`), the
  reader `decision/choose.py` already imports (`:44`) for its `regard` term;
- where the seat's row names a skill (edit 3), the candidate's skill in it **as the conferrer's
  own ledger holds it**: a new person-side read, `believed_capability(p, other, capability) -> int | None`,
  over `p`'s claims about `other`. No claim on `main` carries another person's skill, so this half
  ships as `None` for everyone and the term is regard alone; the interface is stated so the skill
  architecture (`U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §8) can supply the claim. INCOMPLETE at this
  half: its writer (a claim of another's skill) has no carrier in the suite.

A seat's own help on a roll made through it is not this term and not this file's: it is the seat row's
`modifier:` (D-U1-01a), read off `Act.via` by the `office` leverage source, and a seat above the actor's
stands against an act only as the obstacle term `rank_gap` (D-U1-01). The ranking term here reads no
modifier, so regard and office are not counted twice.

Weight: one fixture, `confer_fit_weight`, shipped `0.0` (the control: today's positional order) and swept
`{0.0, 0.5, 1.0}`; the flip to a non-zero value is its own declared mover, made on a reading.

**5. `engine/season/offices.yaml`, a `founding:` block beside `titles:`**: `keeps: [confer, revoke]`,
`conferral: appointed`, `revocation: rung_above_in_holdings`, each validated against its roster at load.
`loop/predicates.py` reads the three from `data/rosters.py` and loses the constants.

## The interface FA needs from the merged capability architecture

The merged architecture is decided (`unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md`; D-U1-07); what FA
relies on from it:

- `pool.py::faculty(person, verb) -> pool` and `pool.py::score` (the opposition operand, D-U1-02) remain the
  only readers of skill at a roll. FA calls neither directly; the contest seam does.
- A skill definition (`descriptor_registry.yaml: capabilities`) names its id, its `base` attribute,
  its kind and how it is gained (`grows_by`); the verbs that draw on it name it in their own rows. FA adds
  one optional reference to a skill, from a seat row.
- FA reads no attribute by name and holds no threshold on one.

## Gate (execution artifact)

New test file `engine/season/tests/test_fa_office_capabilities.py` (hand-built worlds, in the style of the
existing hand-built tests), names: `test_a_judge_with_the_capability_wins_more_often_over_200_seeds`,
`test_confer_fit_weight_zero_is_positional`, `test_a_seat_row_naming_an_undefined_capability_is_refused`.

- Hand-built, real fold: two judges, one holding `law: 5`, determine identical matters over 200 seeds;
  the Success share differs in the holder's favour. Control: both holding nothing, the shares are equal
  within the seed spread (measure both).
- `aperture 2 0` POOLS ROLLED prints a `determine` line once content gives one seat-holder the key, with
  "two actors at different pools: yes".
- With `confer_fit_weight` at `1.0` on a hand-built world with one vacancy and two known candidates the
  conferrer regards differently, the higher-regard candidate is seated; at `0.0` the lowest id is.

## Falsifier

- EQUAL at ship: `build_realm(0)` at build and at one and two seasons, with the three rows landed and no
  one holding `law`.
- Mutation: `faculty` ignoring the `determine` row's `capability:` cell reddens the two-judges gate.
- A verb row's `capability:` naming a skill with no definition row is refused at import (CAP's loader
  refusal, observed).

## What it does not do

No rank (CR-32), no duty (CR-88), no qualification that bars a seat, no faction statistic. It does not give
`march` a capability: the commander's input to a field is the mass-battle module's (cross-listed to MB).

## NERS reading

- **N.** Vertical: the same rule gives a hearth elder and a cardinal a judge's dice. Lateral: the conferee
  term is the first place another person's qualities bear on a governance choice. Without it every bench is
  identical and every appointment is alphabetical.
- **R.** Customization: a designer adds a skill as one definition row and points a seat row at it. Characters matter:
  who is seated changes how the seat's contested acts go.
- **S.** One methodology with every other contested verb; no second ladder for the same quantity.
- **E, last.** Three rows, one optional key, one score term behind a fixture at zero, three constants moved.

## Cost class

Small build; EQUAL at ship. The regard reader exists (`person_q.regard`); the authoring file is decided
(D-U1-07). Tier: `sonnet` (R3 7b-0; the placement choice of edit 3 was made once in U3, C3-C15).
