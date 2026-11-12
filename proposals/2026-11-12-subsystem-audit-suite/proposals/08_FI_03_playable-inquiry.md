# 08 · FI · 03 — A playable inquiry: a scenario, products for the empty inquiries, a conclusion, a check, an end

## Status: PROPOSED (design-first: §3 and §4 need a design pass before code; §1, §2 and §6 are edits)

Carries audit `audits/08_FI_audit.md` F-FI-03, F-FI-04 and resolutions R-07, R-08, R-27. Sits on top of
B10-14 as written (CR-94, CP-T06-09, -01, -03, -04, -02, -07, -05) and changes none of its positions.

## What this changes in `engine/season/` at runtime

Nothing until §2 lands. §1 is a harness scenario and a rendering (no engine change). §2 gives three inquiry
rows a product and lets a graded inquiry deposit what it examined. §3 lets an investigator state a
conclusion as a Proposition he holds and act on it through verbs that exist. §4 makes a contradicted teller
a question. §5 names the end conditions as predicates over existing state. No verifier, no truth flag, no
case object, no new resolver, no contest seam (SM-3 and the 2026-08-18 Q5 ruling stand).

## The problem, with evidence

`modules/fieldwork/find.py` is a band-to-terms lookup. In `build_realm(0..2)`, one season: `record.forged`
16 / 19 / 17, found deposits 0 / 0 / 0; `reconstruct` folded 47 / 45 / 54, `interview` 19 / 8 / 19,
`thread_read` 2 / 1 / 0, each depositing only "a finding was made"; `examine` folded 0. In the 143-case
corpus (`corpus_run`, seed 0): `examine` and `thread_read` never attempted, `forge` and `survey` only
refused, and the instrument's own line lists `interview`, `reconstruct`, `thread_read`, `lie`, `interrogate`
under *EMITS AND WRITES NOTHING … untagged*. Nothing can check a told claim (H-271); a caught liar loses
nothing (F-FI-04). 26 corpus cases carry a CORE need about an investigation reaching a conclusion; NPC-004
needs a confident wrong one.

## 1. The scenario (edit; harness only)

- **`engine/season/harness/scenarios.py`** (a harness module, beside `probes.py`): `trail_world(...)` moved
  out of `engine/season/tests/test_fi03_trail.py:95` unchanged, the test importing it. A second builder,
  `inquiry_world(seed)`: one settlement; a forger who has forged a sheet and handed it on; a holder acting on
  it; a witness to the handover who was not at the forging; an investigator with a seat that may
  `open_case`; a bench. Built from `build_realm`'s own primitives; no authored outcome.
- **Entry:** `harness/play_surface.py::dispatching_chooser(auto, {investigator: callback})`: the
  investigator is the player-proxy, everyone else the shipped chooser. One code path: the same
  `SeasonDriver.season`.
- **Legibility:** a rendering of `decision/sheet.py::chronicle(p)` in the play surface: per subject, what he
  holds, from whom (`chain`), how sure (`confidence`), how old (`when`). A read; no state.

## 2. Products for the empty inquiries, and checking (build)

One new **column** on `verb_table.yaml`, `observes:` — a list of typed reads in the existing `requires`
grammar that do **not** gate, evaluated by the fold's `WorldReader` when the act's band is `Partial` or
better, and attached to the act's Event as `Observation`s. Nothing else is new: `loop/witness.py`'s second
deposit already turns an Event's observations into firsthand cell claims for the actor
(`observation_deposit_mode: actor`), in the vocabulary clause 4 and `record` read.

| row | `observes:` (what a success teaches the inquirer, firsthand) |
|---|---|
| `examine` (a Site) | the site's `condition`; the `stores` of the rung it stands in |
| `surveil` (a Rung) | who is `with` the place is world-only and stays so; the rung's `stores`; `held_by` of the rung |
| `research` (a Record) | `held_by` of the Record; the Record's `content:` as a holder would read it, **without** taking the hold |
| `interview` | CP-T06-05 as planned: the questioned person answers by his own `tell` or `lie`; no `observes:` |
| `thread_read` | T07's (B10-15): the live `knot`/`tie` edges of the subject, as a `seen`-shaped claim; named, not designed here |

**Checking a telling is investigating.** Once an inquirer holds a firsthand cell on something he was told
about, `decision/options.py::record` has its pair and the teller's word is re-graded on every claim he ever
passed on (CAT-3, graded at read). No verification verb is added (H-271 closes by composition).
CP-T06-04 (a refused or failed inquiry teaches its actor his reads) is the same deposit for the gating
reads; this column is its non-gating half.

## 3. A conclusion (design-first)

`reconstruct` becomes the act that states what the investigator believes happened (R-27):
- **Value space** (K-37's missing piece): the persons his own ledger names as the doer of a deed he holds a
  claim of — `queries/person_q.py::deed_doer`, which already pairs a deed claim with its sighting.
- **Product:** an uttered Proposition, mood `HOLDS`, about the deed's patient or the Record, naming that
  doer, with the maker's `hold` (`_eff_utter`'s body and `_makers_hold`, the one owner). Graded through the
  existing `graded_inquiries` route: `Failure` utters nothing; `Partial` utters it without the hand.
- **If his ledger is wrong, the conclusion is wrong, and nothing tells him.** A borrowed name (CP-T06-07), a
  lie or a drifted report is enough. This is NPC-004's need with no truth flag anywhere.
- **Acting on it:** `petition` whose `terms` names the accused, `carry`, `determine` — the route
  `_eff_carry`'s docstring already describes (*"an accusation petition's `terms` names the accused"*).
  What makes a petition form from a held conclusion is `rosters.yaml: terms_sourced`' existing mechanism
  (a held document or Proposition supplying `terms`); the design pass decides the row.
- **The world answers later:** a HOLDS Proposition contradicted by a later firsthand or found claim naming
  another doer is the pair `record` scores for tellers; the design pass decides whether the same pairing
  scores the concluder (the plan's home for the price is CR-83).

## 4. A caught liar is a question (design-first, small)

`queries/world_q.py::standing_crossed` already raises one `claim_landed` question *"about the people who
told"* when a person's standing crosses a band. Its sibling: when `record(p, teller)` is below neutral and
the contradicting firsthand claim landed since `p` last deliberated, one question whose referent is the
teller and whose `about` is that claim. No new deposit, no new source, no new Event kind. The hearer's
candidates on the liar then form by the ordinary rows (`tell` others, `petition`, `challenge`, `forgive`).
What it costs the liar beyond that is CR-83's.

## 5. End conditions (edit; an instrument reads them, nothing stores them)

The scenario ends when the first holds: the accused is determined (a live disposal edge of his on the
bench's seat); the forger is out of the investigator's reach (`world_q.reach`); the investigator holds a
conclusion and his season budget is spent; four seasons pass. An `aperture` line per inquiry verb (formed /
refused / found) and one scenario summary line (which ending, at which tick, was the conclusion's named
doer the Event's actor).

## 6. Cover quality (edit, with CP-T06-07)

A cover is a Record; `Record.forgery_quality` already has one writer and one reader (the examination's
obstacle). `_eff_conceal` writes the same field through `_mint_document` (CR-94's value once it lands), so
a `surveil` against a covered deed is harder against a better cover. No second quality field.

## Gates (execution artifacts)

- §1: `inquiry_world(s)` runs four seasons headless at seeds 0–19 with the shipped chooser in the
  investigator's seat; every run ends by a §5 predicate.
- §2: at seeds 0–2, a hearer's `record` of a liar reads 1.0 before his `examine`/`surveil` and below 1.0
  after; control: the same season with `observes:` empty reads 1.0 throughout.
- §3: over the 20 seeds at least one run ends with a conclusion naming someone who is not the Event's actor,
  and at least one with the actor named; `reconstruct` deposits a Proposition in more than zero of its
  folded acts (today zero of 47 / 45 / 54).
- §4: a question whose referent is the liar exists in the round after the contradiction; control: no
  contradiction, no question.

## Falsifiers

- Every one of the 20 runs names the true actor: then nothing in the scenario can mislead, and the wrong
  conclusion is still unrepresented.
- `observes:` makes clause 4 decline more acts the world would admit (stale firsthand cells): read the
  `world says True` share of declines before and after (today 1 / 2 / 1 of 461 / 445 / 485).

## NERS reading

N: the investigation scale is one of the seven the requirements file names and reads `in_loop: False`;
without a conclusion the scale has no outcome. Top-down (R-05), bottom-up (rows gain a column, not a
resolver), lateral (SC's bench hears the accusation; CHAR's `record` prices it), diagonal (a player's
conclusion and an NPC's are one Proposition). R: creativity in approach (three independent routes:
document, place, testimony), a wrong answer that matters, and the no-player half (NPC investigators reach
conclusions and accuse). S: one roll owner, one ladder, one mint, one deposit rule; *pauses correctly* to be
tested when a multi-act scene exists. E, last: one column, one retyped row, one question sibling, against a
scale that today does nothing.

## Cost class

§1, §5, §6: edit. §2: small build. §3, §4: design-first, then small builds. Lanes: FI; SC (the bench);
CHAR (CR-83); T07 (`thread_read`).
