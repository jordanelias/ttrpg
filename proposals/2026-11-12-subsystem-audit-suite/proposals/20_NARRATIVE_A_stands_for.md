# NARRATIVE-A — a person holds what he stands for: one reading of conviction for the regime, for strain and for fault lines

## Status: PROPOSED

Source: `audits/20_NARRATIVE_CHURN.md` F-NARR-01 (the regime is a constant), §2 edges R1, R2, V3, S4;
evidence E-N01, E-N04. Reference only (`CLAUDE.md` §0.05). Not ratified by being written.

## What it changes in `engine/season/` at runtime

With the new fixture at its control (`held_reading: any`, shipped in the first commit) nothing moves and
every hash is EQUAL. At `held_reading: stands` (the second commit, a **declared hash mover** for every
world in which a told claim lands between two persons holding convictions, which is every realm season):

1. `world_q.commensurate(w, a, b)` reads each person's affiliations *stood for* in place of affiliations
   *held above zero*. Its three values then all occur in the built realm (measured below), where today
   one value covers 1,031 of the 1,035 pairs it is ever asked about.
2. `loop/witness.py::_credit` therefore raises some told claims, lowers some and leaves most alone, in
   place of halving nearly every told claim between two cast members.
3. `world_q.incompatible_span` (a reading; the strife harness and CR-97 print it) discriminates.
4. `person_q.confliction` counts a strained pair only where the person stands for both; it is damped
   out of the score today (`confliction_weight` 0) so this moves nothing until that arm is flipped.

No carrier, verb, Event kind or roster member is added. `Person.conviction` is unchanged.

## The problem, with evidence

`ED-IN-0293 (2)` (ruled; enforced by `data/cast.py::conviction_of`, `:245-263`): *every NPC holds a
conviction concerning Einhir, Altonia and the Church*. So each of the 46 cast members carries an
intensity on at least three affiliations, most of them low. `build_realm(0)` (E-N01):

- intensities over all 148 holdings: `{0: 7, 1: 90, 2: 23, 3: 7, 4: 7, 5: 14}`;
- held-sets above zero: `altonian_civics + einhir_restoration + solmund_orthodoxy` 32 persons, the same
  plus `thread_truth` 6, five other sets 8;
- `tables.incompatible` is `true` for `einhir_restoration × solmund_orthodoxy`, `inner_tradition ×
  solmund_orthodoxy`, `solmund_orthodoxy × thread_truth`.

Three readers read that intensity three ways:

| reader | reading of an intensity `v` on 0 to 5 | where |
|---|---|---|
| `person_q.conviction_stand` (and `heritage_regard` on it) | signed, centred on the midpoint: `(v − 2.5) / 2.5`; 1 reads −0.6, **against** | `queries/person_q.py:456-466` |
| `person_q.opinion_terms`, `religious_intensity` | a fraction of the ceiling, `v / 5` | `:618-620`, `:819-826` |
| `world_q._held` (→ `commensurate`, `incompatible_span`), `person_q.confliction`, `person_q._held` (→ `broken_by`, the scar writer) | **held if `v > 0`** | `world_q.py:5339-5341`; `person_q.py:778-793`, `:764-767` |

The third reading makes a person who stands against the Restoration at intensity 1 a *holder* of
`einhir_restoration`, and so incompatible with every holder of `solmund_orthodoxy`, himself included.
Read on `build_realm(0)`:

| | held above zero (today) | stood for (`v ≥ 3`) |
|---|---|---|
| pairs of convinced persons at −1 / 0 / +1 | **1,031 / 0 / 4** | **130 / 779 / 126** |
| persons whose own set holds an incompatible pair | 41 of 46 | 0 of 46 |
| distinct sets | 7 | 6 (20 persons stand for none) |
| `P(incompatible_span)` over 6 random persons (300 draws) | 0.95 | not yet run (gate 3) |

and, at `v ≥ 3`, the sets fall along the factions the cast was authored into: Church of Solmund 7 of 7
`solmund_orthodoxy`; Restoration Movement 4 of 4 and Varfell 5 of 5 `einhir_restoration`; Altonia 3 of 3
`altonian_civics`; Guilds and Hafenmark none; **Valorsmark split** (8 none, 2 `solmund_orthodoxy`, 1
`einhir_restoration`); Löwenritter split (2 none, 1 `thread_truth`, 1 `solmund_orthodoxy`). The fault
lines Jordan authored are in the data. The reader erases them.

What that costs in play (E-N04, four seasons, seeds 0 to 2): every told claim a cast member holds from
another cast member at the end of the run reads `commensurate = −1`; none reads 0 or +1 between two
convinced persons. `regime_gain` 0.5 is therefore one flat discount on hearsay inside the cast, the
strife design's L4 ("in-regime tellers credited more", `strife-00` §6) has no in-regime teller to
credit, and `incompatible_span` prints `True` for every strand with two convinced parties, which is the
base rate and not a reading. `tests/test_strife_credit.py:216-241` asserts that `commensurate` is
*called* at the live value; it cannot observe that it returns one value (`CLAUDE.md` §0.1 pt 2).

## The resolution, decided

**A person holds an affiliation, for every boolean question the engine asks, when he stands for it:
when `conviction_stand(p, a) > 0`, that is, when its intensity is above the scale's midpoint.**

Ladder: step 4 (precedent). `conviction_stand` is the signed reading IN-63 already ruled for a stored
zero ("a considered rejection … reads −1") and `heritage_regard` already composes on it; the boolean
readers were written before the rule that every NPC carries a position on three concerns, and were
correct while a key meant a holding. Step 5 for the form: one function, one owner, the other readers
routed through it, behind a fixture so the flip is a declared mover with a control. The midpoint is not
a new number: it is `(AFFILIATION_FLOOR + AFFILIATION_CEILING) / 2`, read from the leaf
(`engine/substrate/descriptors.py:144-145`).

Two things this does **not** decide. The graded readers (`opinion_terms`, `religious_intensity`) stay
as they are: they ask "how much", not "whether". And a *rejection* (a stored intensity below the
midpoint) is not made a holding of some opposite affiliation: no table says what the opposite of
`altonian_civics` is.

## Exact edits, by owner

**1. `engine/season/queries/person_q.py` — the single owner.** New, beside `conviction_stand`:

```python
def stands_for(p: Person, reading: str = "stands") -> frozenset:
    """THE AFFILIATIONS `p` HOLDS, for every yes/no question (is he commensurate with another, does
    his own set strain, can this act scar him): `stands` -- those he stands for,
    `conviction_stand(p, a) > 0` (an intensity above the scale's midpoint); `any` -- the CONTROL,
    every key stored above zero, the reading before this function. One owner; `world_q._held`,
    `confliction` and `_held(p.conviction, ...)` ask it. Person-side, no World (AX-2)."""
```

`reading` is a member of a new closed roster `held_readings: [any, stands]` (`rosters.yaml`, beside
`stance_polarities`), refused if unrostered (`require_member`, the `_stance_arm` precedent).

**2. `engine/season/data/fixtures.py`.** `held_reading="any"` with a NUMBER-free `[JUSTIFIED: …]` line
naming a new `hole_register.yaml` row (kind `RULING`, grade `assumption`, H-275's shape): *swept `any`
(control, the tree before this item) / `stands` (live)*, `[ASSUMPTION; medium; Jordan to correct;
revert: set it back to `any`]`.

**3. `engine/season/queries/world_q.py::_held`** (`:5339-5341`).

Old:
```python
def _held(w: World, pid: str) -> set:
    """A person's HELD affiliations: an intensity above 0."""
    return {k for k, v in (w.persons[pid].conviction or {}).items() if v > 0}
```
New:
```python
def _held(w: World, pid: str) -> set:
    """A person's HELD affiliations: `person_q.stands_for`, at `Fixtures held_reading`."""
    return set(stands_for(w.persons[pid], w.fixtures.get("held_reading")))
```
`commensurate`'s and `incompatible_span`'s bodies do not change. `commensurate`'s docstring line "HELD
affiliations (an intensity above 0, `person_q`'s reading)" is replaced by the pointer.

**4. `engine/season/queries/person_q.py::confliction`** takes the reading as an argument its one caller
passes (`decision/choose.py::deliberation_memo` already holds `fx`): the sum runs over the incompatible
pairs both of whose members are in `stands_for(p, reading)`. At `any` it is today's sum exactly.

**5. Not edited here: the scar writer.** `person_q._held(p.conviction, violated)` (`:764`, through
`broken_by`) is the same boolean, and CHAR's `02_CHAR_scar_is_a_wound.md` fixture 1 (`scar_hold:
primary`, "affiliations held at intensity 3 or more of 5") proposes the same threshold for it. **One
owner for both:** that proposal's `primary` arm, for affiliations, should call `stands_for` and not
restate `>= 3`. Listed for the CHAR lane; no second rule is written here.

**6. `engine/season/tests/test_strife_credit.py`.** One test added, on `build_realm(0)` with no season
run: at `stands`, `{commensurate(w, a, b) for every pair of convinced persons} == {-1, 0, 1}`, and at
`any` the same set is asserted to be what it is today (`{-1, 1}`), so the test names the defect it
excludes. `test_the_realm_reaches_commensurate…` is kept.

## The gate that shows it worked (execution artifacts)

1. `build_realm(0).content_hash()` and the one- and two-season pins EQUAL at `any` (commit 1).
2. At `stands`, seeds 0 to 2, three seasons, `PYTHONHASHSEED=0`: told claims held at the end, grouped by
   `commensurate(hearer, last teller)`, show **all three signs with a non-zero count at two seeds or
   more**, and the mean confidence orders `−1 < 0 < +1`. Control arm `regime_gain 0`: the three means
   are equal within rounding. (The probe is `narr_probe.py`'s REGIME line, audit §11 E-N04.)
3. `incompatible_span` over the run's strands against the same-size random-party control: the two
   differ at some seed (today both read `True` / 0.95).
4. The strife guard (`strife-00` §6; CR-99's function once built) over `any` against `stands`: every
   terminal code reached at `any` is reached at `stands`, and no code's share rises by more than the
   `any` arm's seed spread. If the guard is BLIND (fewer than two terminal codes at `any`), say so and
   read it at four seasons (the plan's risk 8).
5. The WR story bar (`09_WR_story_instruments_that_can_fail.md`): `--arms off off` still EQUAL.

## The falsifier

- Gate 2 with one sign only at `stands`: the realm's tellers and hearers do not cross a fault line, and
  the fix is in who speaks to whom (FI's `08_FI_02_rumour-that-travels.md`), not here.
- Gate 2 with three signs and equal means at `regime_gain 0.5`: `_credit` is not reached.
- Gate 4 failing: the credit term concentrates endings once it discriminates, which is L4 hardening
  (`strife-00` §6); then `stands` does not ship and `regime_gain` is re-swept under it.

## NERS reading

- **N.** Cut the change and the regime stays a constant: R13 ("an assemblage of institutions with
  commensurate dominant modes of understanding") has no two assemblages to tell apart, CR-79's term
  cannot do what it was ratified for, and every later position that reads `commensurate` (CR-97's span
  column, the strife guard's S5 arm) measures a base rate. Top-down (the era's regimes), bottom-up (one
  hearer weighing one teller), lateral (CHAR's scar reads the same boolean) and diagonal (FA: a split
  faction is visible as one) all turn on it.
- **R.** No player is involved. Completeness: a person standing for nothing reads 0 with everyone
  (`commensurate`'s existing rule); a world with no convictions is the control.
- **S.** This *removes* a second ladder for one quantity. Costs stated: the credit stays frozen at
  deposit (R14), so a person whose conviction later moves does not re-grade what he heard.
- **E, last.** One function, one fixture, one roster, three call sites; against a ratified mechanism
  that is inert as built. High.

## Cost class

Edit. One session with its sweep. Depends on nothing; `02_CHAR_scar_is_a_wound.md` should land after
it or adopt its function.

## Dependency edges

- **CHAR** `02_CHAR_scar_is_a_wound.md` (fixture 1): same threshold, must share the owner (edit 5).
- **WR** `09_WR_strand_conclusion.md`, `09_WR_story_instruments_that_can_fail.md`: gate 4 and 5 read
  their instruments; no edit collides (`world_q._held` is not touched by either).
- **Plan** CR-97 (its strands block prints `incompatible-span`), CR-99 (the guard function), CR-107
  (cohort convictions, authored per cohort row: the same reading applies to a cohort's vector).
- **FI** `08_FI_02_rumour-that-travels.md`: supplies the told claims gate 2 counts.
