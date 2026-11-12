# NARRATIVE-C — who holds what is something people know: the `held_by` claim, the holder behind a seat, and the oath that meets a new holder

Folded: 2026-11-12 by `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md`. Nothing here is deleted. `believed_holder` gains two readers. (1) **The person's era**: `person_q.era_known(p, head_seats)` (`30_WR_A_the_era_is_a_named_period.md` commit 2) is his newest `held_by` claim on the realm's head seat, with the conditions his own open realm-placed strands show; a man who has not heard of the death serves the old king, and his era is the old one. Before this file's commits 1 and 2 land that function returns `unknown`. (2) **The player's marker and recap** (`30_GO_F_the_plot_as_the_player_is_shown_it.md` surfaces 1 and 5) print the believed holder, how old the belief is, and a seat change apart from a death (A-33). This file's G3 (a new holder meets an old oath) is a link of cascade chain K-1 (`30_WR_E` §1) and of LOOP row L9 (`30_WR_D` §2).

Reconciled: 2026-11-12, U5d closure — folded **A-32** and **A-33**. Who holds a seat is learned by the seat's reach (realm-wide shipped, with presence, jurisdiction and telling built as the test arm, A-32), so edit 1's build-time `held_by` deposit and the later Event agree with the shipped reach. A holder's death is learned apart, by presence, trail and telling (A-33): a `held_by` claim may be stale because its holder is dead and the believer does not know it; this file's "the claim can be stale" covers it, and no edit corrects the belief on the death. Blame under an empty seat reads the believed holder (`U5d_STORY_owed_edits.md` §3).

Reconciled: 2026-11-12, wave 3 lane W3-5b (`unified/work/R5_READ.md` §1 rows who_holds_what (CONFORMS; the `_stance_arm` ordering AMBIGUOUS), §2 row edit 5 (`release` polarity; A-22, A-37), §7, 7b; `unified/U3_CONFLICT_LEDGER.md` C3-K3; `unified/U3_DEPENDENCY_ORDER.md` §1 item 38, §3.1). Changed: (1) edit 2's `[UNVERIFIED]` call site is resolved at the tree: `epistemic.py::claim_subjects` (`:185`) reads a `hold` through `_hold_tenure_ends` (`:167`, H-71, used at `:246` and in the sighting walk at `:1038`); the `held_by` deposit is added where those ends are produced; (2) edit 4 lands after the scar-cap Addendum's `regard_sign`/`beneficiary` term (B10; C3-K3) and adds `holder_gain` to the same `r` before the sign rule, one clamp, one `stance_scale`; its code used `_regard_of`, which does not exist in `decision/choose.py` (read here: the arm memoises `regard(p, subject, fx)` in `memo`), so the code now uses that memo; (3) edit 5's "stated limit" is decided at its owner (R5 §2): the Addendum's `regard_sign` column is `-1` on `release` and on any row that ends a tie to its subject, so `stance_polarity: declared` no longer makes a man likelier to leave a lord he honours; the row values are the CHAR lane's to write in that Addendum (listed); (4) tests named; (5) batch order: this file lands before `20_NARRATIVE_B_what_he_was_owed.md` inside B38 (NARR_B imports `believed_holder`; U3 §1 item 38 lists them the other way, corrected here); (6) tier.

Depends on: `02_CHAR_scar_cap_and_regard_unit.md` Addendum (B10; `_stance_arm`'s merged term and the `regard_sign` column); `18_DETERMINISM_notice_is_a_draw.md` (B11); `06_FA_seat_terms_and_turnover.md`, `06_FA_seat_terms_by_body_B.md` (B21) and `06_FA_war_lives_in_seats_B.md` (B23), which supply the changes of holder commit 2 deposits; `30_WR_A_the_era_is_a_named_period.md` and `30_GO_F_the_plot_as_the_player_is_shown_it.md` (B38) read `believed_holder` after it lands.
Lands in batch: B38 (lane WR), after `20_NARRATIVE_A_stands_for.md` and before `20_NARRATIVE_B_what_he_was_owed.md`; three commits, each a declared mover with its control.
Tier: sonnet / high.

## Status: PROPOSED

Source: `audits/20_NARRATIVE_CHURN.md` F-NARR-04 (nothing is aimed), F-NARR-05 (allegiance never moves),
§2 edges O3, O4, A3; hole register H-195 (`engine/season/hole_register.yaml:4415-4426`, grade `absent`,
trigger "the share of persons holding a `held_by` claim at or above 5 %"). Reference only (`CLAUDE.md`
§0.05). Not ratified by being written.

## What it changes in `engine/season/` at runtime

Three commits, each a declared mover with its control:

1. **At build**, every person whose home lies under a held seat holds one claim per such seat,
   `(seat, held_by, holder)`. A build-hash mover (a ledger is state).
2. **In play**, when a `hold` on a seat or a rung opens or closes, every ledger that receives that
   Event's deposit also receives `(seat or rung, held_by, the holder it now shows, or nobody)`. A mover
   in any season where such a hold changes (in the shipped realm: none in four seasons at three seeds,
   audit O3; it moves when FA's turnover proposals land, and in every forced arm).
3. **In choice**, the stance term of a candidate whose subject is a seat or a rung adds the person's
   regard for the holder he believes it has, at `holder_gain` (0 the control, EQUAL).

No verb, Event kind, carrier or world read from `decision/` is added.

## The problem, with evidence

- H-195, verbatim: "nobody holds stance about a rung; the role reading would regard the rung's HOLDER,
  and a person can know the holder only from their own `held_by` claim, which no ledger holds. So a
  grudge on faction F does not make F's enemies march on F-held rungs." Its measurement (0 of 80 persons)
  re-read at this HEAD: 0 claims with a `held_by` predicate in any ledger of `build_realm(0)` (audit
  E-N13); no depositor of the stem exists in `loop/` or `epistemic.py` (E-N12).
- WITNESS reads a `hold` edge as its two ends, so a conferral lands as `(holder, tenure.opened)` and
  `(seat, tenure.opened)`: two claims that share a tick and nothing else. `person_q.deeds_judged` says
  of the pair "which this module never reads as a pairing … so no claim a judge holds says the victim
  sat in that seat" (`person_q.py:121-126`).
- What marches are occasioned by (audit F-NARR-04, three seeds, four seasons): a sighting 45, a finding
  7, a refused transfer 4, a blocked road 2, of the 66 printed; marcher against the governing holder of
  the target by `commensurate`: the base rate.
- A sworn man's oath is to the *seat* (`_eff_oblige`; every one of 50 / 45 / 93 edges). It passes to
  the next holder with no act and no question, and his stance toward the seat has no person in it.
- CR-91 (ratified, B10-17b) will require a *ground* before a march is admitted. That is eligibility
  at RESOLVE. Nothing in it tells the chooser whom the march is against.

## The resolution, decided

**Who holds a seat or a rung is public knowledge within its reach, held as an ordinary claim, and it
can be stale.** Ladder: step 4 for the seeding (the builder already seeds ledgers: 42 of 83 persons hold
claims at build, audit E-N13; `known_persons` reads acquaintance from the holder's own claims, H-195's own cited
precedent), step 5 for the deposit (the Event already shows the holder to everyone it reaches; the
claim says in one row what its two rows imply) and for the operand (H-195 names the marker where it
goes). AX-7 is the point, not an obstacle: a man who has not heard of the succession still serves, and
resents, the dead king.

## Exact edits, by owner

**1. The realm builder (`engine/season/harness/populated.py::build_realm`, the one owner of the built
realm's ledgers).** After seats are filled and homes set: for every person `p` and every Office `o`
with a live holder `h` such that `p`'s home is within `o`'s purview (`state/gate.py::purview_reaches`,
the one owner of that walk) or `o` is a seat `p` is sworn to, mint one claim `(o.id, "held_by", h)`,
source and confidence as the builder's other seeded claims, `when = -1`. The same for the governing
hold of each rung on his home's ancestry (`world_q.governing_hold`). A switch `seed_holders: bool` on
`build_realm` (default on; off is the control and reproduces today's build hash).

**2. `engine/season/loop/witness.py`, the deposit, and `engine/season/epistemic.py::claim_subjects`'s
`hold` branch (the one place a `hold` is read as its ends, H-71).** Where an Event's changes open or
close a `hold` whose object is an Office or a Rung, each recipient of the Event's deposit also
receives `Claim(subject = the object, predicate = "held_by", value = the subject of the live hold
after the Event, or None)`, with the Event's own source, chain and confidence (so a told succession
is hearsay and can be disbelieved, and the notice draw of `18_DETERMINISM_notice_is_a_draw.md` governs
it like any other deed). Behind `Fixtures deposit_holder` (`off` control / `on`). Call site (read at
the tree): `claim_subjects` (`epistemic.py:185`) produces a `hold`'s ends through `_hold_tenure_ends`
(`:167`; called at `:246`, and at `:1038` in the sighting walk); the `held_by` claim is minted beside
those ends for each recipient, so the deposit and the sighting read one rule.

**3. `engine/season/queries/person_q.py` — new, beside `known_persons`.**

```python
def believed_holder(p: Person, x: str, at: Optional[int] = None) -> Optional[str]:
    """WHO `p` BELIEVES HOLDS the seat or rung `x`: the value of his newest `held_by` claim on `x`
    (by `(when, round)`, with `when <= at` when `at` is given), or `None` -- he has no belief, or
    believes it vacant. His ledger only (AX-2, AX-7): it may be wrong, and stays wrong until a
    claim lands."""
```

**4. `engine/season/decision/choose.py::_stance_arm`, at the `ABSENT: H-195 holder` marker
(`:82`, `:101-121`).** Landing order on this one function (C3-K3): the scar-cap Addendum's term
(`regard_sign(row) × regard(p, subject)` plus `regard(p, b)` for a beneficiary, B10, which also carries
`17_CENSUS_C1A_02` W4) first; this term after it, added to the same `r` before the sign rule, under one
clamp and one `stance_scale`. After `r` is formed:

```python
    hg = fx.get("holder_gain")
    if hg:
        h = believed_holder(p, subject)
        if h is not None and h != p.id:
            if h not in memo:
                memo[h] = regard(p, h, fx)                 # the same `regard`, memoised per subject
            r = r + hg * memo[h]
```

The sign rule that follows is untouched: on a contested row whose subject is its opponent the sum is
negated, so a man who hates the holder of a town scores `march` on that town higher, and one who
honours him lower. `holder_gain` ships 0 (control), swept 0 / 0.5 / 1, a `hole_register.yaml` row
replacing H-195's `absent` with `assumption`; `[ASSUMPTION; medium; Jordan to correct; revert: 0]`.

**5. Nothing is built for "the oath meets a new holder": it falls out.** A `held_by` claim that lands
on a seat a man is sworn to is a claim about his own tenure's object, which `attention_key` already
ranks at tier 1 (`world_q.py:3867-3868`, `own_purview`); the candidates on that seat then read his
regard for the new holder through edit 4. **The `release` sign, decided at its owner** (R5 §2): `release`
is an uncontested row, so under `stance_polarity: declared` it took `+regard`, which made a man
*likelier* to leave a lord he honours. The owner is the `regard_sign` column of
`02_CHAR_scar_cap_and_regard_unit.md`'s Addendum (how the act treats its subject): `release` and any row
that ends a tie to its subject carry `regard_sign: -1`, so the act reads regard for the tie's other end
with the opposite sign [ASSUMPTION: the column exists once that Addendum lands in B10 — basis: C1A_02's
head describes `regard_sign` as landing before W4]. The row values are written by the CHAR lane in that
Addendum (listed for it); A-37's imposed services are not this case (they end by pardon or term, not by
the bound man's `release`). Gate 4 reads `release` and reports the sign it finds.

## The gate that shows it worked (execution artifacts)

Tests: NEW `engine/season/tests/test_held_by.py`: `test_build_seeds_one_claim_per_seat_under_purview`
(gate 2), `test_seed_holders_false_reproduces_base_hash` (gate 1), `test_conferral_deposits_held_by_to_the_reach`
(commit 2), `test_far_person_keeps_the_old_holder_until_told` (gate 5, AX-7),
`test_holder_gain_ranks_march_on_a_hated_holders_rung_higher` (gate 3). Gates 4 and 6 are realm readings
printed in the commit body (seeds 0 to 2, four seasons), with `20_NARRATIVE_F`'s `--overlaps` (formerly `--crossings`) for G4.

1. Control: `seed_holders=False`, `deposit_holder off`, `holder_gain 0` reproduce the base hashes.
2. H-195's own trigger: the share of persons holding a `held_by` claim at build, by seed, is above 5 %
   (expected: every person under a held seat).
3. H-195's own falsifier, now observable: a planted person holding a grudge row on `p_x`, who believes
   `p_x` holds rung A and `p_y` rung B, ranks `march` on A above `march` on B at `holder_gain 1` and
   equal at 0, through `make_chooser`'s real ranking (the `march` half `test_told_by_channel.py -k g2`
   says is "not observable while H-195 holds").
4. Realm, seeds 0 to 2, four seasons, `holder_gain 1` against 0: among `march`, `petition`, `challenge`,
   `speak` and `release` acts whose subject is a seat or rung, the mean regard of the actor for its
   believed holder differs between arms by more than the control's seed spread for at least one verb;
   and the targets of marches spread over at least three believed holders at two seeds (not one name).
5. Staleness (AX-7): a planted conferral that a far person does not witness leaves his
   `believed_holder` at the old holder; a `tell` of it updates him at the told confidence.
6. `20_NARRATIVE_F` class G4 (a hostile act on a place whose believed holder the actor holds against)
   above zero at two seeds and above the control arm.

## The falsifier

- Gate 4 with no verb moved at `holder_gain 1`: regard for holders is flat (nobody holds anything
  against anybody who holds anything), which is a finding about `regard`'s inputs (CHAR F-CHAR-03, the
  interior does not move) and `20_NARRATIVE_B`'s reason to exist.
- Gate 5 failing (he knows at once): the deposit is fanning past its channel.
- The build hash moving with `seed_holders=False`: the switch is not a control.

## NERS reading

- **N.** Cut it and every act on a place or a seat is aimed at nobody: a rising has no enemy, an oath
  no lord, a succession is not news about a person. Top-down (the Crown as a person others regard),
  bottom-up (my reeve), vertical (the same claim at hearth and realm), lateral (CR-91's ground says a
  march is allowed; this says whom it is against), diagonal (`20_NARRATIVE_B` lays a lapse at this
  door), horizontal (two neighbours with different news hold different lords).
- **R.** The no-player half: a contested succession in which half the realm has not heard is drama the
  engine makes alone. Complete at the extremes: an unheld place reads nobody; a person with no claim
  reads today's term exactly.
- **S.** The claim is an ordinary claim (decays, is told, can be forged or denied); the term is
  `regard`, the one owner, at a gain with a control. No second knowledge system.
- **E, last.** A seeding step, one deposit rule, one reader, one term; it closes a hole the register
  has carried since 2026-10-09 and unblocks three of the crossings. High.

## Cost class

Small build (three commits). No design decision is open; the `release` polarity (edit 5) is decided at
its owner and its row values are the CHAR lane's.

## Dependency edges

- **Feeds:** `20_NARRATIVE_B` (`believed_holder`), `20_NARRATIVE_D` (the faction behind a holder),
  `20_NARRATIVE_F` (G4, G5).
- **FA:** `06_FA_seat_terms_and_turnover.md`, `06_FA_seat_terms_by_body_B.md`, `06_FA_war_lives_in_seats_B.md`
  supply the changes of holder that commit 2 deposits; CR-91 (the ground) and CR-88 (the duty decline,
  which asks whether a subject is "F's head or an F office-holder": person-side it can only know that
  through this claim).
- **INSTITUTIONS:** `15_INSTITUTIONS_BYZANTINE_A_dignities_and_the_roll.md` (the Roll, and founding
  deeds as claims on the seat) and `15_INSTITUTIONS_COLONIAL_D_accomplishment.md` (standing that passes
  down the seat): both read "who held this seat"; one `held_by` claim form should serve all three.
- **FI:** `08_FI_02_rumour-that-travels.md` carries the news; `18_DETERMINISM_notice_is_a_draw.md`
  decides who notices.
- **CHAR / VERBS-BINDING:** the `release` polarity (edit 5).
