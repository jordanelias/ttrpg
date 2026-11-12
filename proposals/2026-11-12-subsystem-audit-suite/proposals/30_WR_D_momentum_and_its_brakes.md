# WR-30-D — momentum and its brakes: how small things compound through persons and places, and what stops them running away or standing still

Reconciled: 2026-11-12, wave 3 (W3-3) — A-85: the two statements that no mechanism reads a strand, era or world count into a draw now name the one ruled exception (the unopposed-entry draw reads the realm's strife level, `U5d_FA_land_and_seats_pass_on_a_won_march.md` D6; `ED-IN-0352` (3)'s clause owed, not applied); D-U1-09: L12's brake "the steward's skill in the pool" reads as named levels on the place's draw; U3 B00 and T-3 (commit 2's LOOP ids come from the hole-register block B00 allocates, not "the next free id at build"; H-275 is CR-79's row, not free); U3 §6.1 (`test_narrative_dues.py` is absent on `main` and is written as the batch's first commit); batch (U3 B38). Tier already named.

## Status: PROPOSED

Lands in batch: B38 (narrative and regimes), after `23_STORY_A` and before `30_WR_E` (U3 §1 item 38); commit 1 inside `20_NARRATIVE_B`'s first commit (as this file says).
Depends on: see "Dependencies" below; commit 2's ids on B00's hole-register block.

Source: `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md` F-30-08 to F-30-11. Jordan, 2026-11-12: *"momentum mechanisms. cascade effects and compounding are real"*; A-80 (*"entrenchment still moves the world"*); A-81 (*"scenes NEVER generate stillness"*). Reference only (`CLAUDE.md` §0.05). Lane WR; owner files IN's and CHAR's.

Composes on, and restates none of: `20_NARRATIVE_A` to `E` (the five pulls), `16_PESSIMIST_CORE_a_refusal_is_remembered.md` (`refused_before`), `28_CORE_scene_access_A` to `C` (occupancy, appointments, the petition that waits; A-63, A-64), `23_STORY_A_what_a_roll_leaves.md` (a failure writes; the other party is named), `16_PESSIMIST_CORE_the_record_holds_what_changed.md`, `27_MB_E_what_an_army_carries_back.md` (A-69, A-78), `09_WR_B_weather_with_memory_and_the_year.md`, `06_FA_war_lives_in_seats_B.md`, `01_CORE_claim_fade_as_read.md`, `01_CORE_unmet_need_is_attended_first.md`, `02_CHAR_scar_cap_and_regard_unit.md`, `08_FI_02_rumour-that-travels.md`, `U5a_DICE_owed_edits.md` §4, plan positions CR-88, CR-98, CR-99.

## What it changes in `engine/season/` at runtime

| commit | change | hash |
|---|---|---|
| 1 | `person_q.dues_unmet` takes the estimate window and nets a renewed tie (an amendment to `20_NARRATIVE_B` edit 1, made before that edit ships live) | EQUAL while `dues_valence` is 0 |
| 2 | LOOP rows for nine feedback paths, each with sign, bound and switch, in `hole_register.yaml`; keys in `harness/loops.py` | EQUAL (register rows) |
| 3 | nothing else: every other mechanism here is carried by a proposal already on file, and this file orders them and states what each must leave behind | n/a |

No counter is added. No mechanism here reads a strand, an era or a count of the world into a pool, an obstacle or a draw (`ED-IN-0352` (3)); the one ruled exception, the unopposed-entry draw reading the realm's strife level (A-85, `U5d_FA_land_and_seats_pass_on_a_won_march.md` D6; the clause's text owed, not applied), is not this file's. Nothing fires.

## The problem, with evidence

- **Order carries nothing.** Adjacent strife codes against a shuffled-order control, seed 0, two seasons: `WN->WN` 9 against 8.23, `PT->PT` 7 against 6.25; none of the study's 16 links appears (audit §12, P-1). A world in which an act raised the odds of the next would show order above its shuffle.
- **The declared loops are asserted.** L1 to L4 carry signs "asserted and unmeasured" (`strife-00` §6); CR-98 will write them as rows. None describes compounding through a person's grievance, a house's succession, a side's membership, an army's losses or a place's stores.
- **The one measured feedback runs the wrong way.** A refused act is retried by the same person 41% of the time and refused again 328 times in 342, while an executed act is re-attempted 21% of the time (`16_PESSIMIST_CORE_a_refusal_is_remembered.md`, seed 0, three seasons): failure breeds repetition, not escalation or a change of means.
- **Stillness is measurable.** Seed 0, one season: 821 acts, 444 made and 377 refused; 59 refused acts left no change on any of their Events and no claim in any ledger (`research` 24, `surveil` 19, `interview` 14, `reconstruct` 2); a further 318 refused and 78 made acts left only the sighting claims of those who saw them, with no write to any other state (audit §12, P-2). Under A-81 the 59 are defects, and the 396 are scenes whose only trace is that someone watched.
- **A grievance, as proposed, cannot fade.** `20_NARRATIVE_B`'s `dues_unmet` counts each lapsed edge once, for ever ("Each edge once"); with oaths lapsing together every term the count only rises. A compounding term with no brake is the runaway the charge warns of.

## The resolution, decided

### 1. Where momentum lives

Momentum is a person's, a house's, an army's or a place's. It is never the world's score. It moves through five channels, all built or on file, and through nothing else:

| channel | what carries the momentum | where it enters | settles by |
|---|---|---|---|
| **what he holds for or against someone** | his claims of deeds; his dues unmet; his waiting; his kin's blood | `person_q.regard` (`:424`) → the stance term of `score_terms` (`decision/choose.py:193`) | his sampled choice (`_sample_order`, `:322`), then the act's draw |
| **what is on his table** | stamps: a vacancy, a prisoner, a matter, a stake of a strand he holds or lives within | `questions_for` (`world_q.py:4031`), `attention_key` (`:3857`) | which question he attends (NPC: the first; player: A-48) |
| **what he believes true and likely** | claims with confidence; believed odds; refusals remembered | `View.odds`, `odds_weight`, `refused_before`; `_credit` at the telling | the same |
| **material state** | stores, bodies, men under arms, condition of sites, who holds what | the pools and obstacles resolvers already compose from state | each resolver's draw |
| **the world's drawn motion** | the year's spell, shared under a parent rung for the year | `season_factor_of` and the spell term (`09_WR_B`) | MATTER's keyed draw |

"A grievance raises the odds of the next act" means: the candidate ranks higher in a sampled order. "A defection makes the next easier" means: the next man's opinion of his side is lower and the creed is on his table. Neither is a threshold and neither is certain.

### 2. The compounding paths, each with what the first event leaves, what it makes likelier, and its brake

Each row is a LOOP row of commit 2. Sign `+` compounds; the brakes are the `−` paths that bound it. "Leaves" is the durable write A-81 requires of the first step.

| loop | path | the first event leaves | makes likelier (the reading that moves) | brakes (each an owner that exists or is on file) | switch (control) |
|---|---|---|---|---|---|
| **L8 grievance** | a due unmet or a wrong → lower regard → an act against the one blamed → its refusal or loss, remembered → lower regard | a lapsed edge in his own tenures; a claim of the deed; a claim of the refusal (`a_refusal_is_remembered`) | `regard` falls: `dues_unmet`, `held_against`, `kept_waiting` | the estimate window (commit 1: a grievance is as old as memory); a renewed tie nets it (commit 1); redress at Success or better (`20_NARRATIVE_B`'s bands); `refused_before` lowers the same route's rank; `scene_budget` 5; an unmet need is attended first (`01_CORE_unmet_need_is_attended_first.md`) | `dues_valence` 0 |
| **L9 succession** | a death → a vacancy → a claim → a second claim → backers sworn → a march on the claim → a field | `tenure.closed` on the seat; a `succession.claimed`; a provisional hold (Partial, `14_VERBS_BINDING_C`) | the vacancy is a mandatory question for those who may claim (`30_WR_A` commit 3); a standing rival claim is a ground to march (A-74) | the set who may claim is finite (`may_claim`); a claim that lands Success closes the vacancy and the stamp; each living rival is a step against a claimant (`15_INSTITUTIONS_BYZANTINE_E`); war's own brakes (L11) | `era_mandatory_vacancy` off; the single-title `successions` |
| **L10 the side thins** | a member leaves a creed or head seat (A-46) → the side is who is left → the next member's opinion of it changes → the creed is on his table → he argues, stays or goes | `commitment.ended` on the creed; a claim of it in those who saw or were told | `opinion_of` (`world_q.py:3029`): its third mean is his regard for the head and the members whose deeds he holds, and the leaver is no longer among them | selection: those who stand for the creed keep a positive conviction term; the head's own acts (a grant, a strip under A-35, a purge); credit: the leaver's word is halved across a fault line (`_credit`). **Sign unmeasured**: if the leavers were disliked the mean rises and the loop is `−`; `30_WR_E` shape E-08 reads which | `stamp_own_side` off |
| **L11 victory** | a field won → the victor's deeds are held by more → regard and legitimacy rise → more commit to his war → a larger muster | `field.won`; `rung.seized`; the dead and the taken written (A-69) | `legitimacy` (`person_q.py:537`); the de facto share of committers (`06_FA_war_lives_in_seats_B`) | permanent losses (dead, captured, deserted: A-78) lower the next muster; fatigue carried on the one stamina ledger; numbers act through frontage, not dice (A-60); more land held is more larders in purview and more seats to fill; the loser's kin and sworn men hold the deed against him (L8) | the field's shipped scale (no `field.won` today) |
| **L12 dearth** | a hard year → stores fall → hunger → the cohort's heavy moves (petition, migrate, refuse, riot: A-56) → fields unworked or a granary burned → a lower yield | the yield taken; `stores.changed`; a `shortfall` claim | the year's spell is shared under the parent rung for the year (`09_WR_B`), so neighbours are short together; `stability` (`:566`) falls where shortfall is known | fewer eaters after a migration or a death; relief by `transfer` or `exchange`; the next year's draw; the steward's skill as named levels on the place's draw (A-54, D-U1-09) | `season_factor_draw` `()` |
| **L4 rumour** (declared by CR-98) | a telling believed → acted on → more to tell | a claim with a chain | in-regime tellers are credited more | credit halves across a fault line; each hop refracts; claims fade as read | `regime_gain` 0 |
| **L13 the door** | a petitioner kept waiting → the petition intensifies (a drawn, graded change: A-64) → he waits again, books, or goes elsewhere | `visitor.kept_waiting`; the petition's stage | `kept_waiting` lowers regard; the intensified matter outranks others on the bench's docket | an appointment (a commitment between two persons); precedence by rung orders access and gates nothing; determination closes it; the term fades as its claims fade | `waiting_valence` 0 |
| **L14 the held position** (A-80) | an attempt on an entrenched holder fails → the attempt is remembered by both → the attacker's route is discounted and his grievance stands → he takes another means; the holder answers | STORY-A's failure write; a claim of the refusal in the attacker; a claim of the attempt in the holder | for the attacker: `refused_before` on the failed route, so the other rows on the same referent rank above it; for the holder: `held_against` the attacker, `enemies_heard` | `scene_budget`; each alternative has its own draw; the holder's concession ends it | `refused_before`'s fixture at 0 reproduces today's retry loop |
| **L15 retry** (today's, perverse) | a refusal → the same act again | nothing he reads | nothing: it is repeated because nothing changed | removed by `a_refusal_is_remembered` | that fixture |

**Counter-pulls that bound every path** (each already an owner): loyalty and duty (`oblige`; CR-88's `duty_weight`); need (an unmet need is attended first); distance and the road (`16_PESSIMIST_WR_A_the_road_is_drawn.md`); ignorance (a death travels only by presence, trail and telling, A-33; notice is a draw, `18_DETERMINISM_notice_is_a_draw.md`); disbelief (credit); occupancy (a visited person is occupied, A-63); custody (A-23); the budget of five scenes; forgetting (D-48).

**What keeps the world from freezing** is A-81 and L14: a failure is never nothing, and a held position turns the loser toward another means.

### 3. What each scene outcome writes, and what that write is toward (A-81)

Every outcome of every scene leaves at least one durable change other than the budget debit. A *durable write* is a Receipt on a `write_matrix.yaml` cell whose `steps` include `RES` or `WIT`, other than the scene budget's own cell; a claim deposited in the actor's or a counterparty's ledger counts; a sighting in a bystander's ledger alone does not (the act must matter to someone in it). `[ASSUMPTION; medium; Jordan to correct; revert: any claim counts]`.

| outcome | the write (owner) | toward a strand | toward a regime | toward an era |
|---|---|---|---|---|
| Overwhelming, Success | the row's `writes:` at that degree | a move: it joins, turns or concludes | the deed is told and credited along the teller's lines | a turn, when it changes the head seat or a realm condition |
| Partial | a provisional or termed edge: a provisional hold (`14_VERBS_BINDING_C`), a promise with a term (`20_NARRATIVE_B`), a truce | the strand stays open on a named referent (the term) | told as a half-success: each camp holds its own version | `contested`, a truce, a regency: the era's conditions |
| Failure | the stake paid and the counterparty named as patient (`23_STORY_A`); `refused_before` reads the actor's own claim | the attempt is held against the actor by its patient, who is now a party | a lost argument across a fault line is a scar on the element pressed (`_scar_witnesses`), toward a crisis | a failed claim lowers the claimant's standing with those who saw it |
| refused at the fold (the world said no) | a firsthand claim of the refusal in the actor (184 of 226 already, PES-CORE); for the inquiry verbs `finding.none` deposited to the actor (`U5a_DICE_owed_edits.md` §4), which closes the 59 measured above | he turns to another means on the same matter (L14) | none | none |
| refused by a person (a petition denied, a challenge declined, an order defied) | the refusal is a deed of the refuser, held by the refused (`a_refusal_is_remembered`; A-81 (1)) | a move where its kind is one (`compliance.withheld` opens) | told | a head who refuses the realm's petitions spends legitimacy |
| kept waiting, an appointment missed, a petition unanswered | `visitor.kept_waiting`; the petition's intensified stage (`28_CORE_scene_access_C`) | pressure on the matter's strand; the lapse, when it comes, is a due unmet | none | none |
| a drawn field | both armies home at once (A-67, A-70); fatigue and losses written (A-69) | the strand stays open; the war continues | told by both sides as their own | the war stands |
| a mandatory scene passed over (NPC: cannot; player: not offered) | n/a: A-47 says it cannot be passed | | | |

### 4. Entrenchment produces (A-80)

A position that holds (A-79: an even argument carries one time in four) is a source of motion. What each entrenching thing leaves and opens:

| what holds | what its holding leaves (per failed attempt, by §3) | what the other party may do next (existing rows on the same referent) | what the holder does (his own occasions) |
|---|---|---|---|
| an argument that does not carry | a scar or a hardened stance in the one pressed; the arguer's claim of the loss | argue again on other ground (`02_CHAR_which_ground_moves_whom.md`), bring a document (`cite`), go to a bench (`petition`) | hold, counter-argue, concede a part |
| a bench that will not rule, or rules against | a petition that waits and intensifies (A-64); a determination against him | another forum: a superior by petition (A-22), an appeal on new grounds (A-39); a patron; forgery (`forge`); force (A-74: a march on a grievance) | recuse or be challenged (`15_INSTITUTIONS`), delay, grant |
| an incumbent in a seat | a refused claim, remembered; a provisional rival hold | a rival claim (`succeed`), a rival body (`establish`), `commit` to another, flight (`migrate`, `release`) | strip (A-35), grant, arrest, buy |
| a fortified town, an army that stands | a drawn field, losses and fatigue carried home | a siege, a raid, a treaty, a third power (`covenant`), cutting its larder | sortie, provision, parley, call an ally |
| a creed that keeps its members | an argument lost; the dissenter marked | leave quietly, leave and be seen, found a rival | discipline, concede, expel |
| a lord who does not pay | a due unmet in every sworn man | each of them: petition, release, swear elsewhere, withhold compliance | pay late (Partial: a new term), excuse, punish the first to complain |

No row needs a new mechanism. Each "may do next" is a verb row that already forms on the referent, made likelier by §2's readings; the gate that this happens is `30_WR_E`'s entrenched-world arm.

## Instructions to code

Tier: second (sonnet) for both commits; no judgment node. Land commit 1 inside `20_NARRATIVE_B`'s first commit (it changes that proposal's edit 1 before it ships).

**Commit 1 (EQUAL at `dues_valence` 0).** `engine/season/queries/person_q.py`.
1. `dues_unmet(p, x, window)` (signature of `20_NARRATIVE_B` edit 1, plus `window`, the argument `legitimacy` and `stability` take, `:537`, `:566`): count his own termed `oblige` edges that ended at or after their term **with `until` inside the window**, whose seat he believed `x` held then, **less** one for each such lapse that is followed by a newer `oblige` edge of his to the same seat that is live or ended by his own `release` (the tie was renewed). Never below 0.
2. `regard` (`:424-453`): the call site passes `fx.get("estimate_window_seasons")` (the fixture `storybar.estimates` already reads, `harness/storybar.py:270`), as the block that reads `scar_weight_shift` passes its own.
3. Tests, `engine/season/tests/test_narrative_dues.py` (the file `20_NARRATIVE_B` opens; if that proposal names another, that one; absent on `main`, written as the batch's first commit, U3 §6.1): `test_a_lapse_older_than_the_window_is_not_counted`, `test_a_renewed_tie_nets_the_lapse_before_it`, `test_two_lapses_and_one_renewal_count_one`, `test_the_count_is_never_negative`.
Ladder: step 4 (the window is `legitimacy`'s and `stability`'s; one methodology for one kind of estimate, NERS-S). `[ASSUMPTION; medium; Jordan to correct; revert: count every lapse, `20_NARRATIVE_B` as written]`.

**Commit 2 (EQUAL).** `engine/season/hole_register.yaml`, after CR-98's rows (so it lands after CR-98): nine rows `kind: "LOOP"`, ids from the hole-register block B00 allocates for B38 (U3 §1 item 1; T-3: H-275 is CR-79's row and the register runs past it, so no id is taken as max+1), one per row of §2 (L8 to L15, and L4's row gains the brake text if CR-98 left it out). Each row: `sign:` `+`; `default:` naming its bounds as §2's brakes column gives them, each bound a fixture or a function with its path; `switch:` the control fixture; `cite:` this file and the measured baseline (P-1's pair table; PES-CORE's 41% and 21% for L15; `unmeasured` where none exists, said so). `engine/season/harness/loops.py::DECLARED_CYCLES` (`:172-181`) gains one key per row, or the row is recorded unmapped with the reason, as CR-98 does. L10's row carries `sign: "+"` with the note "unmeasured; may read `-`; `30_WR_E` shape E-08 decides", which G13 admits (a sign and a bound are present).
Tests: `engine/season/tests/test_loops_instrument.py` (existing) passes; the falsifier is CR-98's: a planted copy of one row with `sign:` removed fails `register --check`.

## The gate (execution artifacts)

```sh
python -m engine.season.harness.register --check                      # G13 on the new rows
python -m engine.season.harness.loops                                 # declared against derived
python -m pytest engine/season/tests/test_narrative_dues.py engine/season/tests/test_loops_instrument.py -q
```

Expected: G13 passes; `loops` prints "amplifiers derived equal declared" or names the disagreement (recorded in the commit); the four dues tests pass. The behavioural gates for the paths themselves are `30_WR_E`'s (compounding against correspondence; the entrenched-world arm; the no-null-scene reading).

## The falsifier, and its control

- **Runaway.** In the on arm, any person's `regard` toward any other below the floor `02_CHAR_scar_cap_and_regard_unit.md` sets, or `dues_unmet` above the number of his termed edges inside the window: a brake is not braking.
- **Freeze.** In the entrenched-world arm, executed acts per person-season below half the free arm's, or a null-scene count above 0 after the carriers of §3 land (`30_WR_E` clause C8, C9).
- **Not compounding.** `30_WR_E`'s lift for a path within its control's seed spread: the path is declared and does nothing; its row is marked `inert` with the reading, and no gain is raised to force it (a gain is set by its own sweep, not to pass a gate).
- Control for each path: its switch at control, the same seeds.

## Dependencies

Commit 1: with `20_NARRATIVE_B`, after `20_NARRATIVE_C`. Commit 2: after CR-98. The paths need, in order of how much they unlock: `16_PESSIMIST_CORE_a_refusal_is_remembered.md` and `23_STORY_A` (L14, L15, §3); `20_NARRATIVE_B` and `C` (L8); `22_HAPPENINGS_A`, `B` and `14_VERBS_BINDING_C` (L9); `20_NARRATIVE_D` (L10); the MB batch and `27_MB_E` (L11); `09_WR_B` and `U5d_SE_cohort_heavy_moves_and_caste.md` (L12); `28_CORE_scene_access_C` (L13).

## Layer 1

AX-2 (`decision/` reads no World; a pull is person-side): kept, **STRUCTURAL**. `ED-IN-0352` (3) (no flow touches an obstacle, pool or draw): kept; every odds-setting reading here is a person's or a place's state (A-85's one exception is the entry draw's, not this file's). ID-16 (`01_AXIOMS.md:616-619`: every feedback path declared with a direction before an amplifier lands): **MECHANICAL**, and the reason commit 2 exists; G13 is its check. T-a: nothing stored, **STRUCTURAL**. §C.11 (hidden in existence, never in arithmetic): untouched.

## NERS reading

- **N.** Remove the brakes and `20_NARRATIVE_B` ships a term that only rises; remove the rows and five amplifiers land undeclared. Holds bottom-up (one lapse, one man), top-down (a realm that neither freezes nor runs away), laterally (the same window for grievance, legitimacy and stability), diagonally (a person's momentum against a place's).
- **R.** Strategy: a player can see that a man kept waiting, unpaid and refused is dangerous, and can pay, hear or renew. No player: a lord who does not pay makes his own rebellion. Complete: a person with no dues, no claims and no ties has no momentum and acts on pursuit alone.
- **S.** One window; one regard; brakes that are the same owners the rest of the game uses (budget, fade, need). It pauses nothing.
- **E, last.** One argument, one netting clause and nine register rows; everything else is order. High.

## Cost class

Edit (commit 1). Edit (commit 2). The carried mechanisms keep their own classes.
