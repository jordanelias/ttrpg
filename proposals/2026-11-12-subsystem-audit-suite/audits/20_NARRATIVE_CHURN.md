# NARRATIVE CHURN — eras, regimes and strife against allegiance, office, obligation, pursuit and conviction

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: d4ee8a4 (working tree)

Lane: narrative systems. Jordan, 2026-11-12: *"Fable to interrogate how eras, regimes, strife work
alongside faction allegiances, office duties, obligations and demands, pursuits and convictions, with the
goal to improve our emergent narrative basis to construct legible narratives and drive plot points
dynamically with compelling contributing worldly churn WITHOUT determinism."* Every reading below is a
dated reading of a command in §11 (`PYTHONHASHSEED=0`; seed and season count stated with it). Design
documents are cited for intent and vocabulary only (`CLAUDE.md` §0.05). The other lanes' audits and
proposals are cited, not redone; where this file repeats one of their numbers it says whose it is.

Vocabulary, as the tree uses it (so no reader takes a word in its ordinary political sense):

- **era**: the realm's one strife flow, a scope over every strife move under the realm rung
  (`queries/world_q.py::Era`, `_eras`; `strife-00` §4, R11). Not a calendar period.
- **regime**: Foucault's regime of truth (`strife-00` R13, R17), "an assemblage of institutions with
  commensurate dominant modes of understanding and behaving, not a political regime". In code it is one
  function and one fixture: `world_q.commensurate(w, a, b)` and `Fixtures regime_gain`.
- **strife**: an Event whose kind is in `rosters.yaml: strife_kinds` (`opens`, `joins`), linked into
  strands by `world_q._links`.
- **allegiance**: a live `commit` Tenure from a person to a faction's Proposition (`world_q.members`,
  `faction_of`) or to an organisation's goal (`goals.yaml`, `world_q.ambitions`).
- **office duty**: what a seat's holder may do (`offices.yaml: seats[].remit_acts`), and the `oblige`
  Tenure a person swears to a seat (`effects_governance._eff_oblige`). §1 shows these are the only two
  senses the code has.
- **obligation and demand**: `oblige` (with a `Term`), `petition`/`carry` (a Record, a docket item),
  `issue` (a writ: a `dispensation` Record), `comply` / `evade / defy`, `covenant`, `requisition`,
  `transfer`, `exchange`.
- **pursuit**: a weight on the canonical fifteen (`Person.pursuits`), projected to seven axes and dotted
  with a verb's alignment cells (`decision/choose.py::score_terms`).
- **conviction**: `Person.conviction`, an intensity 0 to 5 on each of five affiliations
  (`data/affiliations.py`); **scar**, a count per violated element (`loop/resolve.py::_scar_witnesses`).

## 0. Verdict

*(Written last; see the end of the file's build order in §11. Placed here.)*

VERDICT_PLACEHOLDER

## 1. The eleven things, as coded

One row per thing the direction names: its single owner, what the season loop reads of it, and what
reads it back. "Loop reader" means a step of `loop/` or a function `questions_for` or `choose` calls; a
harness or a test is not a loop reader.

| thing | owner (code reads this) | written by | loop reader | shipped state |
|---|---|---|---|---|
| season of the year | `world_q.season_of_year` (`:1169`): `tick % len(season_factor_draw)` | nothing (read off the tick) | `season_factor_of` → MATTER's yield | **no year exists**: `season_factor_draw = ()` (`data/fixtures.py:535`), so `season_of_year` is `None` every tick (E-N02) |
| calendar | `loop/calendar.py` (`Date.fired`, the docket) | `convene` (`date.scheduled`), CALENDAR | `sittings_before`, `docket_question` → a judge's question | live; fires sittings whose matters then lapse by clock (WR F-WR-13) |
| era | `world_q._eras`, `Era` (`:4929`, `:5233`) | nothing (recomputed from the log) | **none** (`world_q.py:4749-4752`: "NO CONSUMER IN THE LOOP") | one era per run, never concluded (E-N03) |
| ending | `rosters.yaml: endings` → `world_q.endings_reached` | nothing | the season summary only; halts nothing | `[]` in every run here; victory unreachable (WR F-WR-06) |
| regime | `world_q.commensurate` (`:5317`) over `data/affiliations.py::INCOMPATIBILITY`; `Fixtures regime_gain` 0.5 | nothing | `loop/witness.py::_credit` (`:240`), on a told claim's confidence, once, at deposit | live and **degenerate** (F-NARR-01) |
| strife | `rosters.yaml: strife_kinds`; `world_q.flows_in` (world), `flows_known` (person) | every verb whose row emits a move kind | `flow_stakes` → `questions_for` (the stamp, `stamp_flow_stakes` True) | live; reaches 0 to 28% of persons by seed (WR F-WR-07) |
| allegiance | `commit` Tenures; `world_q.members`, `faction_of`, `ambitions`; `goals.yaml` | `commit`, `release`; world-gen | `questions_for` Q4 (`need`), `attention_key` tiers 0 and 3 (salience), `opinion_referents` | live as attention; never changes hands (E-N05) |
| office duty | `offices.yaml: seats[]` (`remit_acts`, `conferral`, `revocation`, `obligees`); `state/gate.py` remit grant | `confer`, `succeed`, `revoke`, `establish`; world-gen | `Act.via`, `own_purview` (attention tier 1), `reach` | a **licence only**: no row says what a seat owes, to whom, or by when (F-NARR-03) |
| obligation | `oblige` Tenure + `Term` (`oblige_term` 4); the docket; writ Records | `oblige`, `transfer` (renews), MATTER (matures) | `establishment_of` → the obligee channel; `writs_held` → `comply` | terms mature unpaid by clock; `comply` never executes (E-N06) |
| demand | `petition` Record → `carry` → docket → `determine`; `issue` → writ; `requisition` | those verbs; MATTER lapses a docket item at `docket_lapse` 4 | `docket_question`, `sittings_before`, `matters_awaiting` | petitions accumulate and lapse (E-N06; WR F-WR-13; SC F-SC-01) |
| pursuit | `Person.pursuits`; `tables.alignment`; `decision/choose.py::score_terms` | `determine`/`argue` (`pursuit.moved`), scar shift (off) | the score's first term, every candidate | live; reads the verb only (CHAR F-CHAR-01) |
| conviction | `Person.conviction`; `tables.incompatible`, `tables.affiliation_engagement` | `conviction_after_crisis` (scar ≥ 3) | `crisis_weights` (the `doctrine` weight), `opinion_terms`, `heritage_regard`, `commensurate`; `confliction` damp (weight 0, off) | live in four small places; removing it changes nothing a story reading sees (E-N07) |
| scar | `Person.scar`; `loop/resolve.py::_scar_witnesses` | every witnessed act that violates a held element | `conviction_after_crisis`; `scar_weight_shift` (0, off) | runs away (CHAR F-CHAR-04); E-N05 |

**How a season joins them.** `calendar` → `matter` → five rounds of `deliberate → resolve → encounter →
witness` (`loop/driver.py::season`). The only place the eleven meet is `questions_for`
(`world_q.py:4031-4283`): a person's questions are (Q2) each new claim in his ledger whose subject his
`reach` covers, (Q4) one `need` per live `commit` to an OUGHT Proposition, the sitting and docket
questions, and then the standing occasions stamped on the first question as classed referents
(vacancies, seats named, writs held, places, matters awaiting, larders, holdings, propositions heard,
stage referents, the wounded, flow stakes). `attention_key` (`:3857`) orders them in five tiers. The
chooser then scores each candidate `(verb, referent)` as `pursuit + stance` (`choose.py:193-221`). So:

- allegiance, office and strife enter as **which referents a person is handed and in what order**;
- pursuit and (through `doctrine` and `regard`) conviction enter as **how a verb scores**;
- obligation enters as one referent class (`Record`, for `comply`) and one channel (the obligee's);
- era, the year and endings enter **nowhere**;
- regime enters one step earlier, as how firmly a told claim is held.

Nothing in that path asks *why* a referent matters to the person: a referent is a referent, whether it
is the lord who failed him or a granary he walked past. That is the subject of §3 and §5.
