# FA-P6 — capability where governance uses it: vocations for the contested governance verbs, a seat's vocation, founding content as data

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-11) — the judge's capability is named `law`, not `judgment`: SC's `05_SC_hearing_capabilities.md` authors the same capability under that name, one thing takes one name, and `judgment` collides with the uses table's role `judgement`. `determine: law`, `interrogate: inquiry`, `arrest: arms` are the decided verb values (`unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §5), written on the verb row's `capability:` column; the definition row lives in `references/descriptor_registry.yaml: capabilities`.

Reconciled: 2026-11-12, U5d closure — folded **A-12** (a seat may carry a modifier) and **A-7** (two inputs to a roll). The sentence "a seat's vocation is never a prerequisite. It is a reason" stands for gating (A-11: capability gates nothing), and edit 3's `vocation:` key stands. Added by A-12: a seat row may also carry a modifier on the rolls made through it; this file does not author its number or home, which is `14_VERBS_BINDING_C_turnover.md`'s standing term and the institutions kit's (`15_INSTITUTIONS_SYNTHESIS_A_one_kit.md`), read by the one obstacle composer (`U5c_SC_one_obstacle_form.md`) so that regard and office are not counted twice. Edit 4's "the one reader" is therefore no longer the only reader of a seat's row. The pool's two inputs and the capability home are `U5a_capability_home_and_two_inputs.md`'s; edits 1–2 land on that home. The Layer 1 text for `04` §B.7 is owed by the ruling, not applied.

## Status: PROPOSED

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (L-10) — the pool reader's owner is `seam/wrappers/pool.py::faculty` (`:78`), re-exported by `sigma.py:105`; one citation corrected. No edit of the proposal changed.

Source: `audits/06_FA_audit.md` §14, §15 (c), (d), F-FA-05; hole rows H-126, H-207 (the positional conferee).

## What it changes in `engine/season/` at runtime

1. `determine`, `interrogate` and `arrest` roll the actor's capability for a named vocation instead of
   `pool_default` for everyone. With nobody holding the new key and no attribute authored, each still rolls
   `pool_default`, so the rows ship hash EQUAL until content gives someone the key (the state `argue` and
   `inquiry` shipped in at REM-30).
2. A seat's row may name the vocation its post calls on. One reader uses it: the ranking of candidates for a
   `confer`. It gates nothing.
3. Three constants that say what a founded office is granted move from Python to `offices.yaml`. No
   behaviour changes.

It adds no capability system. The owner already exists and is extended: `rosters.yaml: verb_capability`
(verb → vocation) and `vocation_attribute` (vocation → one of the ten registry attributes), read by
`seam/wrappers/pool.py::faculty` (`:78`; `sigma.py:105` re-exports it).

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
vocation → attribute table both ways so a vocation cannot be half-declared.

The ruled axiom is kept: "capability supplies dice and gates nothing" (`rosters.yaml: verb_capability`'s
own source line). So a seat's vocation is never a prerequisite. It is a reason: something a conferrer may
weigh, in the one place the engine currently weighs nothing.

## Exact edits, by owner

**1. `engine/season/rosters.yaml: verb_capability.values`.**
`interrogate: "inquiry"` (the existing vocation: questioning is an inquiry; its attribute row exists).
`arrest: "arms"` (the existing vocation `capture` uses; an arrest contested is a taking of the body).
`determine: "judgment"` (a new vocation).

**2. `engine/season/rosters.yaml: vocation_attribute`.** `judgment` → `attr.mind.acuity` (Reason), the
attribute `inquiry` already starts from: weighing a matter is of a kind with finding one out
`[ASSUMPTION; medium; Jordan to correct; revert: drop the `determine` row and this one together; the loader
refuses either alone]`. The competitor, the cheap swap: Presence, if a bench is read as carrying the room.

**3. `engine/season/offices.yaml`.** A seat row may carry `vocation: <a `data/verbs.py::VOCATIONS` member>
| null`. Loader: `data/rosters.py::_load_offices` refuses a value that is no vocation, naming the row.
`Office` gains `vocation: Optional[str] = None`, stamped onto the `hold` grant by `World._grant_remit`
beside `remit_acts` and `seat_rung` (the same untyped payload convention CR-32 uses for `post`), so a
person-side reader has it with no `World`. No shipped row names one in the first commit. Candidate content,
for Jordan: the Royal Marshal, the Military Commander and the Military Jarl `arms`; the Cardinal of Justice
and the Senior Inquisitor `judgment` or `inquiry`; the Chief Parliamentary Clerk `copying`.

**4. The one reader: ranking the conferee.** `decision/choose.py`'s score for a `confer` candidate gains a
term over its `to` operand, through the existing terms table (`choose.score_terms`), never a branch on the
verb name:

- the conferrer's regard for `to`, read by CHAR's existing person-side regard reader (the same one `tell`'s
  hearer choice uses) [UNVERIFIED: its name and signature; the holistic stage fixes the interface];
- where the seat's grant carries a vocation, the candidate's capability in it **as the conferrer's own
  ledger holds it**: a new person-side read, `believed_capability(p, other, vocation) -> int | None`, over
  `p`'s claims about `other`. If CHAR's audit finds that no claim today carries another person's capability,
  this half ships as `None` for everyone and the term is regard alone; the interface is stated so the
  merged architecture can supply the claim.

Weight: one fixture, `confer_fit_weight`, shipped `0.0` (the control: today's positional order) and swept
`{0.0, 0.5, 1.0}`; the flip to a non-zero value is its own declared mover, made on a reading.

**5. `engine/season/offices.yaml`, a `founding:` block beside `titles:`**: `keeps: [confer, revoke]`,
`conferral: appointed`, `revocation: rung_above_in_holdings`, each validated against its roster at load.
`loop/predicates.py` reads the three from `data/rosters.py` and loses the constants.

## The interface FA needs from the merged capability architecture

- `faculty(person, verb) -> pool` and its opposition twin remain the only readers of capability at a roll.
  FA calls neither directly; the contest seam does.
- A capability definition must name: its key (the vocation), the attribute its pool starts from, the verbs
  that draw on it, and how it is gained (`train`, practice, a lifepath). FA adds one optional reference to a
  key, from a seat.
- FA reads no attribute by name and holds no threshold on one.
- If the merged file replaces `verb_capability` and `vocation_attribute` with one table, FA's three rows
  and the seat's `vocation:` reference move with it unchanged.

## Gate (execution artifact)

- Hand-built, real fold: two judges, one holding `judgment: 5`, determine identical matters over 200 seeds;
  the Success share differs in the holder's favour. Control: both holding nothing, the shares are equal
  within the seed spread (measure both).
- `aperture 2 0` POOLS ROLLED prints a `determine` line once content gives one seat-holder the key, with
  "two actors at different pools: yes".
- With `confer_fit_weight` at `1.0` on a hand-built world with one vacancy and two known candidates the
  conferrer regards differently, the higher-regard candidate is seated; at `0.0` the lowest id is.

## Falsifier

- EQUAL at ship: `build_realm(0)` at build and at one and two seasons, with the three rows landed and no
  one holding `judgment`.
- Mutation: `faculty` ignoring the `determine` row reddens the two-judges gate.
- A row for `judgment` in `verb_capability` with no `vocation_attribute` row is refused at import (the
  existing check, observed).

## What it does not do

No rank (CR-32), no duty (CR-88), no qualification that bars a seat, no faction statistic. It does not give
`march` a capability: the commander's input to a field is the mass-battle module's (cross-listed to MB).

## NERS reading

- **N.** Vertical: the same rule gives a hearth elder and a cardinal a judge's dice. Lateral: the conferee
  term is the first place another person's qualities bear on a governance choice. Without it every bench is
  identical and every appointment is alphabetical.
- **R.** Customization: a designer adds a vocation as two rows and points a seat at it. Characters matter:
  who is seated changes how the seat's contested acts go.
- **S.** One methodology with every other contested verb; no second ladder for the same quantity.
- **E, last.** Three rows, one optional key, one score term behind a fixture at zero, three constants moved.

## Cost class

Small build; EQUAL at ship. Depends on CHAR for the regard reader and on the holistic stage for the merged
authoring file.
