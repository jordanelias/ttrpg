# 21 · PROCEDURAL C — a past by simulation (the prologue), and cases as armed motives with true trails

## Status: PROPOSED (2026-11-12; Fable design lane; ratifies nothing; reference under CLAUDE.md §0.05)

Carries `audits/21_PROCEDURAL_GENERATION.md` §4.6, §4.7, §9, resolutions R-21-05, -06, -07, -08; plan
batches **PG-4** and **PG-5**. Depends on proposals A (switch, `pick`), B (the cast, relations, local
seats) and D (the card schema `family: case` rows use).

## 1. What changes in `engine/season/` at runtime

With `build_realm(prologue=0)` and no `case` cards (shipped): nothing.
With `prologue=N`: the built realm runs N seasons of the ordinary loop before it is returned; play starts
on a world whose ledgers, stances, seats and records were made by its persons' acts.
With case cards drawn: some persons start holding a goal row whose object is another person, a seat, a
record or a store, with a motive drawn from their own relations. Whether they act on it is their
chooser's. A deed of a kind listed in `rosters.yaml: covert_kinds` leaves a findable trail; the roster
gains, per kind, which channels the deed deposits to and how the trail's age raises an inquiry's obstacle.
After the prologue the build counts the committed deeds an investigator could reach and redraws a world
with too few. Nothing in play compares a conclusion with truth.

## 2. The problem, with evidence

- **No past.** 0 Events at build; every ledger holds only build-time claims (audit P3). A person's first
  season is the world's first.
- **A prologue is affordable and already leaves something.** Probe P2: two seasons, seeds 0 and 1: 28 s
  and 31 s; 37,646 and 34,194 Events; `record.forged` 31 and 34; `finding.made` 120 and 122; no death.
- **One trail kind, reachable only through a plant.** `rosters.yaml: covert_kinds.values:
  ["record.forged"]`; `epistemic.trail_of`'s own docstring: "REACHABLE ONLY THROUGH A PLANT… The seed-0
  realm reaches no trail by `research`". `D_T06.md` row 8: "nothing varies what a deed leaves behind";
  row 2: "Nothing at a place can be read by someone who was not there"; row 10: belief fades, "the
  world-side half (a trace that fades) does not exist".
- **No case generator, though the ruling for one exists.** FW §2.3 and its §11.1 correction: solvability
  is a "generation-time precondition + emergent erosion, never… a constraint maintained against the sim".
  `research/by_lane/FI_fieldwork_investigation.md:197`: "Solvability at generation | FW Q6 ruled; no
  generator… UNREACHED".
- **The precedent's method does not transfer whole.** Shadows of Doubt selects a killer by archetype and
  grades the detective's answer by exact match (audit §1.1). Valoria may not pick an outcome (T-b), may
  not special-case an entity (scripting drift), and has no verifier by axiom.

## 3. The resolution, decided

1. **The prologue is the real loop.** No coarse simulation, no invented Events. `build_realm(prologue=N)`
   runs what `harness/populated.py::run` runs. Ticks are not renumbered.
2. **Older history is tradition:** pedigree and charter Records and hearsay claims whose source is the
   Record (proposal B §4(h); the institution lanes' Roll). Labelled as tradition wherever rendered.
3. **A case seed arms a motive and nothing else.** It is a world card (`family: case`): a query that binds
   a doer and a wronged party from the drawn realm's own relations, a role-bound goal row on the doer, at
   most one seeded claim. No outcome, no date, no firing condition, no named person.
4. **The deed is the doer's act** through an ordinary verb, resolved by draw.
5. **The trail is what the deed kind leaves.** The Event log is the trace store. `covert_kinds` gains a
   leaving pattern and a fade per kind. No new carrier.
6. **Solvability is checked once**, after the prologue, by the generator; then the world erodes freely.
7. **No case object and no grade.** A case exists when a seat-holder's `open_case` opens it.

## 4. Exact edits

### PG-4 — the prologue

**(a) `engine/season/harness/populated.py::build_realm`** gains `prologue: int = 0`. When positive, after
the build completes: construct `SeasonDriver(w)` and the standard chooser (`P.chooser(w,
verbs=resolvable_verbs())`) and call `d.season(…)` `prologue` times, exactly as `run` does at `:2060-2065`
(extract those four lines into `_tick(w, seasons)` and call it from both, so there is one owner). Return
`w`. `worldgen.yaml: prologue_seasons` is the value the shipped build passes once the default flips; the
parameter stays explicit so a test can pass 0.

**(b) A world can be saved after its prologue** and loaded for play, so the cost is paid once per world.
The save form is the port's question (`11_GO_*`); in the oracle the harness may cache by
`(seed, table hash, prologue)` under the scratch directory, never in the tree.

**(c) `worldgen.possibility(w)`** gains post-prologue counts, all read from the built world: `seats_filled`
(local seats with a holder whose `tenure.opened` cites an act), `stance_moved` (persons whose stored
stance differs from build), `chains` (cross-person consequence chains of depth 3 or more, the CR-69
reading in `harness/storybar.py`, called, not copied), `covert_deeds`, `reachable_deeds` (below).

**(d) Sheet:** `--sheet --prologue N` prints a *history page* per settlement: the Events of story-bearing
kinds in order with their causes, who holds a claim of each, and which are tradition.

### PG-5 — case seeds, leaving patterns, fade, solvability

**(e) `engine/season/world_cards.yaml`** (the file proposal D creates) gains `family: case` rows. The card
schema is D's; a case row uses it as follows:

```yaml
- id: case_debt_past_term
  family: case
  source: "generated; no arc"
  eligible:                              # every clause is a build query over the drawn realm; all must bind
    doer:    {relation: debtor, toward: wronged, stance_at_most: -1}        # MOTIVE: owes, and resents it
    wronged: {relation: creditor}
    means:   {doer_holds_any: [record_access, office_with: [create_record, forge]]}
    opportunity: {shared: [settlement]}
  roles: {doer: by_query, wronged: by_query}
  goal_rows:
    - org: {role: doer}
      object: {kind: record, of: wronged, record_kind: debt}                 # the thing the deed would be done TO
      pursuits: {wealth: 0.5, liberty: 0.3, reputation: 0.2}
      stance: -1
  seed_claim: {holder: doer, subject: {role: wronged}, predicate: holds_record, value: debt}
  opens_with: forge                      # an existing verb the doer MAY choose; the card does not choose it
- id: case_rival_for_a_seat
  family: case
  eligible:
    doer:    {goal_toward_seat: contested, relation: rival, toward: wronged}
    wronged: {holds_seat: contested}
    means:   {doer_capability_at_least: {presence: 2}}
    opportunity: {shared: [institution, settlement]}
  roles: {doer: by_query, wronged: by_query}
  goal_rows:
    - org: {role: doer}
      object: {kind: seat_holders, seats: [{role_seat: contested}]}
      pursuits: {reputation: 0.5, honour: 0.3, stability: 0.2}
      stance: -1
  opens_with: lie                        # the false accusation: the case IS the lie
```

Further families as rows, each needing its verb to execute and emit: an embezzled levy (`seize` or
`requisition` under colour of office), a stolen relic or record (`seize`), a ruined store or well
(`sabotage`), a killing in a quarrel (`fight`; only once `F-PC-04` is repaired so a fight does not kill
with certainty), a broken oath concealed (`conceal`), smuggling past a toll, a hidden heir (a pedigree
withheld). The `eligible` clause vocabulary (`relation`, `stance_at_most`, `holds_seat`,
`goal_toward_seat`, `doer_holds_any`, `doer_capability_at_least`, `shared`) is a **closed set**, declared
in `rosters.yaml: card_clauses` and refused at import outside it; each clause is one existing query
(relations from proposal B, seats from `world_q`, capability from the one capability surface). The pursuit
names must be members of `data/pursuits.py::PURSUITS` (fifteen; the rows above use five of them), and the
loader that already parses goal rows (`data/goals.py::parse`) refuses any other.

`worldgen.yaml` gains:

```yaml
case_seeds_per_realm: 4          # drawn among the case cards whose `eligible` binds; pick weight = number of distinct bindings
bars:
  reachable_deeds: 1             # after the prologue; a world under it is redrawn
```

**(f) `engine/season/rosters.yaml: covert_kinds`** gains two sibling maps keyed by the kinds in `values`
(a key not in `values` is refused at import; a kind in `values` with no entry takes the defaults, which
are today's behaviour):

```yaml
covert_kinds:
  values: ["record.forged"]            # unchanged; each new member is one line once its verb emits the kind
  leaves:                              # NEW: which channels a deed of this kind deposits to (closed set, below)
    record.forged: [co_located, record_altered]
  fade:                                # NEW: obstacle added to an inquiry per season of the trail's age, and its cap
    record.forged: {per_season: 0, cap: 0}     # 0 ships: the control arm, today's behaviour
  channels: [co_located, record_altered, stores_changed, body_changed, site_changed, tenure_closed]
```

- `leaves` is read by `epistemic.trail_of` to decide *where* the trail lies: `record_altered` is today's
  behaviour (the trail is on the Record); `site_changed` puts the trail on the Site, which is what
  `examine` reads once it forms on Sites (`08_FI_07_shortest-playable-case.md` §2); `stores_changed` on
  the rung's stores (read by `research` of the rung's rolls); `body_changed` and `tenure_closed` on the
  person or seat written. One projection (`trail_of`), more members; no second trail reader.
- `fade` is read where the inquiry's obstacle is assembled (`seam/wrappers/fieldwork.py::fieldwork_input`):
  obstacle += `min(cap, per_season × (w.tick − e.emitted_at) // scenes_per_season)`. It is a named
  modifier on the task's difficulty, in the engine's obstacle unit; the inquiry's draw still decides, so
  an old trail can still be found and a fresh one missed. No trail is ever deleted.
- The intended members as the verb lanes land them, each one roster line plus its verb emitting:
  `store.sabotaged` `[site_changed, stores_changed]`; `holding.seized` `[stores_changed, co_located]`;
  `person.wounded` / `person.died` by a hand `[body_changed, co_located, site_changed]`;
  `oath.broken` `[tenure_closed]`. Kind names follow whatever the verb table emits; these are
  illustrative until those rows exist.

**(g) `engine/season/data/worldgen.py`:**

```python
def reachable_deeds(w) -> list[tuple[str, str]]:
    """(event id, seat id) pairs: a committed covert deed and an office that could reach it. STRUCTURAL,
    run once after the prologue, by the generator, which may read truth. Never called by a loop step."""
```

A deed `e` (an Event of a `covert_kinds` kind with a person as its hand) is reachable by seat `s` when all
hold: (1) `s`'s remit includes `open_case` or `determine` and its scope covers the rung `e` wrote;
(2) `s` has a holder; (3) there is a chain of length at most `max_chain` (table, default 3) in which each
link is something the engine can form today: the holder (or the next person in the chain) can form an
inquiry whose `trail_of` contains `e`, **or** can reach (same settlement or an acquaintance) a person who
holds a claim about `e` (`holds_trail`), ending at a claim whose `doer` names the hand (the field
`08_FI_06_testimony-names-a-hand.md` fills). The function calls `trail_of`, `holds_trail` and the
candidate former; it re-implements none of them. It returns pairs so the sheet can show which seat could
reach which deed.

**(h) The inquiry scenario** (audit §9): `harness/play_surface.py` gains a scenario constructor that
builds the realm with `variable=True, prologue=N`, takes a `(deed, seat)` pair from `reachable_deeds`,
and seats the player-proxy as that seat's holder (replacing the generated holder by a `confer` in the
last prologue season, an act, so the tenure is real). The proxy is told nothing of the deed. One code
path: the same build, the same loop, the same verbs.

## 5. Gate (the detective gate)

**PG-4.** Seeds 0–19, `prologue=4`: every world's story inventory (chain count and kinds histogram,
`harness/chronicle.py --chains`) is non-empty; mean pairwise similarity of chain signatures between worlds
is lower than between dice-only arms of one world; same seed twice gives an equal hash; at least one local
seat is filled by an act in every world (with proposal B).

**PG-5.** Seeds 0–19, `prologue=4`, case cards on:

- (a) **Committed by the doer, by choice.** In at least half the worlds at least one case card's goal ends
  in a covert deed Event whose causing act is the bound doer's; in *no* world is a covert deed emitted
  with any other cause (no generator writes a deed). In the worlds where the seed did not fire, the sheet
  shows the armed motive standing.
- (b) **An NPC investigates.** In at least one world in four, a seat-holder's own chooser forms
  `open_case` on a generated deed and the case reaches `determine` by its graded draw. Reported per world:
  who was named, and whether it was the hand (computed by the harness, never by the game). Wrong
  determinations are counted and shown; a result with none across 20 worlds is suspicious and is
  investigated as a missing spread.
- (c) **The player-proxy investigates through the real verbs.** In the scenario of (h), a lead-following
  proxy (it prefers a formable inquiry on the newest claim it holds about the matter) reaches a committed
  conclusion in at most `S` seasons. Printed: right, wrong, unsolved, over the 20 seeds, against two
  controls: a **uniform-random proxy** over the same formable candidates (the floor the lead-follower
  must beat) and a **seeds-off realm** (no case cards: the base rate of findable deeds).
- (d) **Erosion is real.** With `fade.per_season > 0`, the right rate falls as the proxy is seated later
  (season 4, 8, 12); with `fade` at 0 it does not. Both arms printed.
- (e) **Draws, not rules.** For one fixed world, re-running (c) under ten dice seeds gives more than one
  distinct conclusion.

If the FI and LACUNA proposals have not landed, **PG-5a** closes on (a) plus `reachable_deeds ≥ 1` in
every accepted world, and (b)–(e) wait, named as owed.

## 6. Falsifiers

- A covert deed whose cause is not a person's act: the generator scripted it.
- `reachable_deeds` positive in a world where the lead-following proxy never forms a single inquiry on the
  matter: the structural check is counting links the engine cannot form.
- The lead-follower no better than the random proxy: the trail does not guide; leads are not chaining.
- Right rate 100% in (c): there is no spread; a good position never loses (the standing rule's test).
- The same doer and wronged pair in most worlds: the eligibility queries bind too narrowly; the pool is a
  script.

## 7. NERS reading

- **N:** cut the prologue and the first season has no yesterday; cut case seeds and the fieldwork lane has
  forgeries only, by whoever happened to forge. Is the cut free? Partly: the loop already forges 31 to 34
  Records in two seasons with no seed at all. What the seed adds is *motive that a reader can find*: a
  deed done to a named creditor by his debtor, with the ground on record. Without it a found forgery
  explains nothing.
- **R:** the no-player half entire (wrongs are done and investigated with nobody watching); variety by
  pool and by binding; the player matters because a wrong conviction stands. Completeness: a world where
  no seed fires is still a world; a world with no reachable deed is redrawn, and after that nothing is
  guaranteed.
- **S:** the same verbs, the same draws, the same obstacle unit; one trail projection; the scenario
  enters from the season and writes back into it. One methodological seam to watch: `fade` must be a
  modifier on the obstacle like every other, not a second decay beside belief decay.
- **E, last:** one parameter, one function, two roster maps and card rows, against a realm with a past and
  wrongs that can be found. The expensive part is not here; it is the verbs and the hearing.

## 8. Cost and dependencies

PG-4: small build. Yield depends on `14_VERBS_*` and `09_WR_B_draws_not_thresholds.md` (verbs that
execute instead of refusing).
PG-5: design-first for the clause vocabulary, then small build. Needs: `08_FI_07_shortest-playable-case.md`
(`examine` forms), `08_FI_06_testimony-names-a-hand.md` (a claim names a doer),
`08_FI_05_evidence-interface_B.md` and `12_ARCS_cited_evidence.md` (evidence cited),
`19_LACUNA_conclusion_is_a_committed_assertion.md`, `19_LACUNA_verdict_ladder_and_reversal.md`,
`14_VERBS_PHYSICAL_A_custody_and_force.md`, `14_VERBS_PHYSICAL_C_looking.md`,
`14_VERBS_SOCIAL2_C_case_question_confession.md`, `03_PC_*` for a fight that can go either way, and
proposal D's card loader.
