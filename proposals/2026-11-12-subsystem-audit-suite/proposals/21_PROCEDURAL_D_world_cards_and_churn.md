# 21 · PROCEDURAL D — one world-card schema for four families; churn from storms, openings and arrivals

Reconciled: 2026-11-12, U5d closure — folded **A-52**, **A-50** and **A-47**. §5 (the docket; held on D-3) is ruled B behind its test: the docket is read inside a seat-holder's `convene` only after PG-6's reading shows that cards read at build run dry (openings per season falling to zero in a long game); until that reading exists the docket is not built, and when it is, plan lines B10-18:183 and B10-19:95 are amended by the ruling. World cards may draw bounded starting state (A-50). A card never decides an outcome: where it arms a threshold it opens a mandatory scene (A-47).

Reconciled: 2026-11-12, wave 3 lane W3-5b (`unified/work/R5_READ.md` §1 row world_cards (PG-6 CONFORMS; (g) VIOLATES; docket and (g′) AMBIGUOUS), §2 row Status/§5 (A-52), §7, 7b; `unified/U3_CONFLICT_LEDGER.md` C3-L13; `unified/U3_DEPENDENCY_ORDER.md` §1 item 39, §3.1, §4.1 row 42). The body now follows the head. Changed: (1) the Status line and §5's heading say "RULED B behind a test (A-52)", not held on D-3; (2) (g) repeats `21_PROCEDURAL_B` (d)'s CENSUS violation and is rewritten as B (d) is: an arrival is minted with `exists` and `weight` (name and `born` from `generate_person`), with no lifepath, relations or claims written at CENSUS (C3-L13); (3) the docket's carrier when it is built is a Proposition or Record the seat-holder utters at `convene`, which the bound persons' choosers then meet as a classed referent (`propositions_heard`, CR-28, this file's own stamp precedent), never goal rows minted on other persons (no write basis admits a non-owner write of another person's goal); (g′) cannot mint goal rows at CENSUS for the same reason as (g) and, if built, takes the same carrier; (4) the variety instrument of the gate is a step that first writes `harness/variety.py` (defined by `02_P1_templates.md` §1, not in the tree); (5) tests named; (6) dependency, batch and tier lines.

Depends on: `21_PROCEDURAL_A_worldgen_tables_and_ground.md` and `21_PROCEDURAL_B_cast_and_seats.md` (B39; the realm cards bind to); `02_CHAR_goal_lean_on_its_own_question.md` and `12_ARCS_arcs_as_staged_goals.md` (B10); `14_VERBS_BINDING_B_sittings.md` (B32, `convene` for the docket); `01_CORE_case_setup_and_beats.md` and `12_ARCS_case_on_the_realm.md` (B39). `07_SE_ground_and_granaries.md` (B12) runs at its control until this file supplies A-50's bounded starting state (§4.1 row 42, LATER).
Lands in batch: B39 (lanes WR / FA), after `21_PROCEDURAL_C`; PG-6 one commit (hash-equal with empty pools), PG-7 (g) one commit with its test; the docket and (g′) are not built until PG-6's reading exists.
Tier: sonnet / high (PG-6, PG-7, `variety.py`); opus for the docket's carrier when it is built.

## Status: PROPOSED (2026-11-12; Fable design lane; ratifies nothing; reference under CLAUDE.md §0.05). §5 (the docket) is RULED B behind a test (A-52): built only after PG-6's reading shows cards read at build run dry; plan text B10-18:183 and B10-19:95 are amended then, by the ruling.

Carries `audits/21_PROCEDURAL_GENERATION.md` §4.8, §6 ("how an authored arc plugs in"), resolutions
R-21-01, -11; plan batches **PG-6** and **PG-7**. Builds on the ratified CL-OPEN design
(`proposals/2026-10-28-content-architecture-suite/02_P1_templates.md` §3, P1-B; ED-IN-0305) and on
`08_decks_and_template_in_engine_form.md` (the Tensions and Goldenfurt rows already rewritten into the
goals schema and executed there). It specifies the *one widening* of the world-generation schema that the
plan assigns to CL-OPEN's build (`workplans/valoria_master_workplan_v11.md:113`); it does not add a
second.

## 1. What changes in `engine/season/` at runtime

With `build_realm(cards=False)` or empty pools (shipped): nothing; hash EQUAL.
With cards on: at build, a few cards per family are drawn from pools by keyed draw; each drawn card binds
its roles to persons and seats of the drawn realm by query and mints its role-bound goal rows and at most
one seeded claim. Nothing is drawn in a season; no card carries a date, a firing condition or an outcome;
a card's story begins only if a bound person's own chooser picks the act.
With arrivals on (PG-7): a person individuated at CENSUS takes his name and birth season from
`generate_person`; nothing of his interior is written there (C3-L13).
With the docket on (RULED B behind a test, A-52; §5): a seat-holder's `convene` reads a few cards from the
seat's pool and utters them as Propositions or Records.

## 2. The problem, with evidence

- **Four receivers, none built, three held.** CL-EVENTS commits (3) and (4) (the Tensions receiver and six
  cards, "a world-generation draw"), CL-OPEN (set pieces: design RATIFIED, build HELD on `-10` M26), CR-80
  (the strife deck: HELD on CL-OPEN's build), and case seeds (proposal C). Each has been described with its
  own row shape (`workplans/valoria_master_workplan_v11_part12.md:14-16, :184`;
  `08_decks_and_template_in_engine_form.md` §1). `build_realm` has no `tensions=` or `cards=` parameter
  today (its signature, `harness/populated.py:1014-1016`).
- **Sameness is the stated reason for decks.** Jordan's original ask, as the content suite records it:
  "pure emergence tells similar stories"; "scripted hooks and sequences, never whole arcs".
- **Churn has no source after the build.** Six seasons at seeds 0 and 1: no ending, one death, three
  determinations in eleven thousand acts (`audits/09_WR_audit.md` §0). Build-time pools are finite.
- **A director is refused by axiom** (AX-1, T-c), and every pacing precedent uses one (audit §1.4, null N4).

## 3. The resolution, decided

1. **One schema, one loader, one draw.** A card is `id, family, source, eligible, attach, roles,
   goal_rows, seed_claim, opens_with, weight`. `family` is one of `tension | setpiece | strife | case`.
   The "may not be data" list of B10-18:183 is kept whole: no date, deadline, firing condition or outcome.
2. **Roles bind by query** over the drawn realm (proposals A and B), most important role first; a
   mandatory role that cannot bind means the card is not drawn in that world.
3. **Selection reads state, at build:** a card's draw weight is its authored `weight` times the number of
   distinct bindings its `eligible` finds (a card that fits this world in more ways is likelier). That is
   a state-dependent draw without a clock.
4. **Pool sizing is the ratified rule:** draw `k` per family from pools of at least `k²` eligible cards.
5. **Churn without a director** has three lawful sources: MATTER draws with memory (the WR lane's weather
   proposal; this kit supplies the per-realm climate profile, proposal A), drawn openings, and arrivals
   by demand. Succession needs nothing new once kin and contested seats exist (proposal B).
6. **Re-arming in play** by a docket inside `convene` is designed here and ruled B behind a test (A-52).

## 4. Exact edits

### PG-6 — the card receiver

**(a) New file `engine/season/world_cards.yaml`** (authored for play; ships with empty pools):

```yaml
meta: {authority: "AUTHORED FOR PLAY. Not canon. Read once by build_realm (engine/season/data/world_cards.py)."}
draw:                                # how many cards of each family a world draws at build
  tension: 1
  setpiece: 3
  strife: 2
  case: 4
cards: []                            # rows as below
```

A row:

```yaml
- id: setpiece_uncatalogued_lock          # unique
  family: setpiece
  source: "an arc, quoted by its id (illustrative row; the text is read by nothing)"   # the plan-text amendment P1-B names (`part12:276`)
  weight: 3                               # integer authoring weight
  attach: {building: scriptorium}         # OR {settlement_type: Town} OR {seat_post: <a post in the roster>}: a QUERY, never a rung id or a name
  eligible:                               # closed clause set (rosters.yaml: card_clauses); every clause must bind
    scholar:   {holds_seat_with_remit: research}
    inquisitor: {holds_seat_with_remit: determine, shared: [settlement]}
  roles: {scholar: mandatory, inquisitor: optional}
  goal_rows:                              # the goals.yaml row shape, with `org: {role: …}` in place of a seat or faction
    - org: {role: scholar}
      object: {kind: rung, rung: {role_home: scholar}}
      pursuits: {scholastics: 0.5, individuality: 0.3, liberty: 0.2}
  seed_claim: {holder: {role: scholar}, subject: {role_home: scholar}, predicate: holds_record, value: uncatalogued}
  opens_with: research                    # names an existing verb; refused at import if not in verb_table.yaml
```

A card in the `scenario` sense (one that names a faction, house or person, such as the six Tensions cards
as `08_decks…` §1 writes them) sets `scenario: true` and may then use `org: {faction: …}` or a named seat;
`04` PART D row 27a's scan treats exactly those rows as scenario declarations. Every other card is
refused at import if any field resolves to a proper noun.

**(b) `engine/season/rosters.yaml: card_clauses`** (new closed set; the vocabulary of `eligible` and
`attach`): `relation`, `toward`, `stance_at_most`, `holds_seat`, `holds_seat_with_remit`,
`goal_toward_seat`, `doer_holds_any`, `doer_capability_at_least`, `shared`, `seat_post`,
`settlement_type`, `building`, `faction_role`. Each maps to one existing query; a clause outside the set
is refused at import by name (the `_check_covert_kinds` idiom).

**(c) New module `engine/season/data/world_cards.py`:**

```python
@dataclass(frozen=True)
class Card: id: str; family: str; weight: int; attach: Mapping; eligible: Mapping; roles: Mapping
            goal_rows: tuple; seed_claim: Mapping | None; opens_with: str | None; scenario: bool
@dataclass(frozen=True)
class BoundCard: card: Card; binding: Mapping[str, str]        # role -> person id or seat id in the built world

def load(text: str | None = None) -> tuple[Card, ...]: ...                       # schema, clause set, verb names, pursuit names; each refusal names the row
def bindings(w, card: Card) -> tuple[Mapping[str, str], ...]: ...                # every way the card's roles bind in this world, sorted
def draw(w, cards: tuple[Card, ...], counts: Mapping[str, int], attempt: int = 0) -> tuple[BoundCard, ...]: ...
```

`draw`, per family in sorted order: the eligible cards are those with at least one binding; pick weight =
`card.weight × len(bindings)`; draw without replacement `counts[family]` times with
`worldgen.pick(w.world_seed, card.id, f"card:{family}")`-style keys (one key per candidate card: each card
gets a keyed score and the `k` best scores are taken, which is draw without replacement that does not
depend on pool order and does not move when an unrelated card is added); then pick one binding per drawn
card by `pick(seed, card.id, "card:binding")`.

**(d) `harness/populated.py::build_realm`** gains `cards: bool = False`. When true, after the cast, seats
and goals are seated and before the prologue: `world_cards.draw(…)`; each bound card's goal rows are
expanded (roles replaced by the bound ids) and passed through the existing `seed_goals` path
(`goals.rows_replaced` shows the route works: `08_decks…` §0 executed 27 of 27 such rows); the seed claim
is appended to the named holder's ledger as a firsthand claim. The drawn and bound cards are recorded on
the build report (`census`), never on a store a loop step reads.

**(e) The other three receivers land on this one:** CL-EVENTS commit (3)'s "Tensions receiver (registry,
loader, roster… build switch, shipped off)" is this loader with `family: tension` and commit (4)'s six
cards are six `scenario: true` rows (the 27 expanded rows of `08_decks…` §1, as written there, are the
content); CR-80's "world-build seeds per strife category" are `family: strife` rows whose `eligible`
names a strife category of `rosters.yaml: strife_kinds`' registry; CL-OPEN's set pieces are
`family: setpiece`. The `yield_scale` Tension (Feldmark Famine) is not a card under this schema: it is a
`worldgen.yaml: scenario` row on the climate profile (proposal A), which is where a matter fact belongs.

**(f) An authored arc** enters as one or more `setpiece` cards plus `goal_stages` rows
(`12_ARCS_arcs_as_staged_goals.md`): named roles pinned with `scenario: true`, open roles by query. The
corpus's per-case `setup:` blocks (`01_CORE_case_setup_and_beats.md`, `12_ARCS_case_on_the_realm.md`) map
onto `eligible` and `roles` one to one; that mapping is the route by which a provided case runs on the
realm instead of a template world.

### PG-7 — arrivals

**(g) `engine/season/loop/census.py`**: individuation takes the arrival's name and `born` from
`generate_person`, keyed by the demand (proposal B (d), as reconciled). That is the whole of PG-7's
unheld part. CENSUS writes `exists` and `weight` (and the person rung and `contain` edge), the cells
`04` §A.2 `:179` licenses it; the arrival's lifepath, deviation and relations are **not** written there
(inv. 5 `:497`; heritage is build-only, `:244`; C3-L13): he begins thin and gains pursuits by his own
first acts and claims by WITNESS. No card is read.

**(g′) RULED B behind the docket's test (A-52) — an arrival may bind a card.** With table probability `worldgen.yaml: arrival_card`
(per thousand; 0 ships), the arrival is offered to the realm's eligible-but-undrawn `strife` and
`setpiece` cards as a role candidate; if one now binds with the new person in a mandatory role, it is
bound and its goal rows minted, keyed by the demand Event. Under the axioms this is authored (AX-5's
resolution: "the demand is its author") and no clock is involved; but CENSUS is a step of the season
loop, so it is a card read by a loop step and falls under the same plan text (B10-18:183) as the docket.
It is therefore held with it, not slipped in beside it. **And its write is not lawful as drafted:** goal
rows minted on the arrival at CENSUS are interior cells (inv. 5, C3-L13). If built, the bound card reaches
the arrival as the docket's does: a Proposition or Record his chooser meets as a classed referent.

## 5. RULED B behind a test (A-52) — the docket (decision D-3, answered)

**What it would be.** A seat's pool: cards with `attach: {seat_post: …}` and `family: docket`. When the
seat's holder executes `convene` (a sitting, `14_VERBS_BINDING_B_sittings.md`), RESOLVE reads up to
`docket_size` cards from the pool whose `eligible` binds *now*, by keyed draw
(`H(seed, tick, seat_id, "docket")`), with **repeat suppression** (a card drawn at this seat has its
weight quartered for the rest of the world, the Wildermyth rule, stored nowhere: it is a query over the
seat's own past `convene` Events), and utters each as a Proposition or Record of the sitting (a petition
to hear, a dispute to settle, an audit to order, a vacancy to fill), which the bound persons' choosers
then meet as a classed referent through the stamp `propositions_heard` (CR-28). It mints no goal row on
another person: no write basis of `04` §C.2 admits a non-owner write of another person's goal (T-m is
`actor == subject`), so the conforming carrier is the utterance, and the business reaches each person as
something he has heard (R5 §1). No date, no outcome: the business exists; what the bench does with it is
the bench's.

**Why it is lawful under the axioms:** the draw is inside a person's act, so the clock is wound and has
handles (T-c: the convener can be bribed not to sit, the roll can be burned). A card still produces no
outcome (T-b).

**What it amends:** plan text B10-18:183 ("a card is a world-generation draw: read once at build, by no
step of the season loop") and B10-19:95 ("no dealing per season"), as `02_P1_templates.md` §3 records for
its variant B+. It does not need T-c reopened, because the card carries no term.

**The two options as games:** without it, institutions hold sittings with nothing new before them once
the build's openings are spent, and churn rests on weather, death and arrivals; with it, a court or a
chapter is a standing source of business scaled to how often it sits and to what the realm currently
holds. Recommended: build PG-6 first, read the openings-per-season curve past season 8, and decide on
that reading.

## 6. Gate

Tests: NEW `engine/season/tests/test_world_cards.py`: `test_empty_pools_reproduce_base_hash`,
`test_card_with_unbindable_role_is_not_drawn`, `test_adding_one_card_changes_draws_only_where_it_scores_into_top_k`,
`test_clause_outside_card_clauses_is_refused_by_name`, `test_non_scenario_card_with_a_proper_noun_is_refused`;
`engine/season/tests/test_census_generated_arrival.py` (proposal B's) covers (g).

**First step, the instrument:** the variety instrument is not in the tree. Write
`engine/season/harness/variety.py` as `02_P1_templates.md` §1 (line 75) defines it: run N world seeds for
S seasons, sign every cross-person chain of depth 3 or more as (verb sequence, actor role classes, subject
kind) keyed by role, reusing `harness/storybar.py::chains` (`:373`), and print the mean pairwise Jaccard
between worlds and the stock share (signatures present in at least half the worlds). Its own test, in
`test_world_cards.py`: `test_variety_of_one_world_twice_is_one_and_stock_share_one` (a world compared
with itself reads Jaccard 1).

- **PG-6.** Empty pools: hash EQUAL at seeds 0, 1, 2. With the 27 Tensions rows and a drafted set-piece
  pool: over 20 seeds the variety instrument (`harness/variety.py`, above: mean pairwise Jaccard of chain
  signatures; stock share) shows mean similarity lower than the cards-off arm by more than the dice-only
  spread, and the stock share not higher. Printed, because it is the known risk: the share of drawn cards
  whose `opens_with` verb was executed by a bound person within 4 seasons, per family. Stability: adding
  one card to a pool changes which cards are drawn in at most the worlds where the new card scores into
  the top `k`.
- **PG-7.** The `04` PART E row 9 acceptance case (a `dispatch` to a post nobody holds) individuates a
  person with a name and `born` (no lifepath, relations or claims written at CENSUS) who acts next
  season; the same demand under the same seed individuates the same person. (Held part: with `arrival_card` on, at least one arrival in 20 seeds × 8
  seasons binds a card, and the card's goal rows cite the demand in their provenance.)
- **Docket (if released).** Openings per season after season 8, docket on against off, same seeds: the off
  arm's curve and the on arm's are printed; the on arm does not fall to zero where the off arm does; the
  repeat rate of a card at one seat is under one in four.

## 7. Falsifiers

- Similarity does not fall, or the stock share rises: the cards are a stock story, not variety.
- Most drawn cards are never opened: the bundles bind to people whose choosers do not weigh them (the CHAR
  lane's finding about goals), and more cards will not help.
- A card whose bound person acts on it in every world in which it is drawn, with the same result: it is a
  script; check for an outcome smuggled into `goal_rows`.
- With the docket on, the same three cards at every sitting: the pool is too small for the seat's
  frequency (the `k²` rule applied to sittings, not builds).

## 8. NERS reading

- **N:** cut the schema and four positions each build a loader. Cut the cards and worlds differ only by
  ground and cast; whether that is enough is exactly what the variety instrument is for, and the cut may
  turn out nearly free if the generated cast alone lowers similarity. The proposal therefore gates on the
  cards-off arm *after* PG-2, not before it.
- **R:** authored hooks where authorship is wanted, cast on generated people; nothing happens unless
  someone acts. Incomplete at one extreme, and it says so: a long game spends its pools (D-3).
- **S:** one schema; the goal-row path that already executes; no clock; arrivals reuse individuation.
- **E, last:** one file, one loader, one closed clause set, against three held positions released onto a
  single receiver and a route for authored arcs onto generated context.

## 9. Cost and dependencies

PG-6: small build; after CL-EVENTS commits (3) and (4) are re-aimed at this receiver, CL-OPEN's release
(`-10` M26) and proposals A and B (the realm cards bind to). PG-7: small build after proposal B (d).
The docket: ruled B behind PG-6's reading (A-52); design-first for its Proposition carrier; needs
`14_VERBS_BINDING_B_sittings.md`.
Chooser dependency for the whole proposal: `02_CHAR_goal_lean_on_its_own_question.md` (a goal must
actually lean a choice, or no card is ever opened).
