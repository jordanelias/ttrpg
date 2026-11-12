# VERBS · SOCIAL1 — build-out of eleven `social` rows

## Status: REFERENCE (a verb build-out audit under `VERBS_BRIEF.md`; resolves nothing at runtime, CLAUDE.md §0.05)
Authored in part by Fable; completed by Opus after the Fable usage limit (2026-11-12).

## Read at: 84d2a02 (working tree; implementation lane A's duel-chain and obstacle edits not merged)

Work order: `VERBS_BRIEF.md`, FAMILY = SOCIAL1. Verbs (rows of `engine/season/verb_table.yaml`, stratum
`social`): `carry`, `argue`, `commit`, `comply`, `conceal`, `covenant`, `evade / defy`, `lie`, `forgive`,
`give`, `challenge`. The exact edits are in the four proposals named in §0.4; this file holds the premise,
the state today with its reading, the decided build-out, and the family's order. Cited, not redone:
`proposals/03_PC_duel_chain_reach.md` and `IMPLEMENTATION_BRIEF_A.md` (lane A: formation of `challenge`
and `accept`, the Record-kind formation rule, persons holding scores), `proposals/05_SC_obstacle_difficulty_and_modifiers_B.md`
(the obstacle as task difficulty plus named modifiers; called **SC-OB** below),
`proposals/02_CHAR_offer_what_can_be_done.md` (one person-side decline read off the row; **CHAR-OFFER**),
`proposals/02_CHAR_relations_have_a_ground.md` and `02_CHAR_which_ground_moves_whom.md`. The
contest-interrogation lane's `audits/13_SC_contest_interrogation.md` **did not exist** when this was
written (its scratch `runs/SC_INT/` holds only a census); where the brief says to cite it, SC-OB is cited.

## 0. Verdict and reading

### 0.1 Verdict

**One of the eleven works as its premise promises (`commit`); two execute and carry a consequence a later
reader takes up (`conceal`, `carry`); three execute but a large share of what they form is refused for a
reason the actor could have known (`argue`, `lie`, `give`); four are formed and always refused (`comply`,
`evade / defy`, `covenant`, `challenge`); one is formed almost never (`forgive`).** None is a stub: every
row has a typed cell, a refusal channel and (but for `comply`, `evade / defy`, `lie`) an effect body.

Three causes account for nearly every failure, and each has one owner:

1. **Wrong-kind formation** (`challenge`, `covenant`, `comply`, `evade / defy`, part of `carry`): the row
   forms on a referent of the wrong collection or Record sub-kind and the fold refuses `exists:<K>=0`.
   Lane A's Record-kind rule and a `referent_class` on `covenant` remove it (proposal A).
2. **Co-location the actor cannot read** (`argue`, `lie`, `give`, part of `challenge`): `with` is
   WORLD-ONLY (`data/requires.py: WORLD_ONLY_STEMS`; `ED-IN-0282` for the hearer), the person forms on
   everyone he knows (`person_q.known_persons`), and the refusal is never deposited, so he forms the
   same refused act next round. A person-side belief of who is with him, read off his own dated
   sightings, removes most of it without touching the world-only fold (proposal A).
3. **The document never reaches its addressee** (`comply`, `evade / defy`, `covenant`'s acceptance,
   `accept` downstream of `challenge`): writs and challenges are minted into the maker's hand
   (`ED-IN-0292` (1), RULED NO "for now"), and reach the addressee only by `give`, which is 0 executed in
   season 1 and 1 of 19 in two seasons. The delivery link is `give`'s (proposal B), and whether to reopen
   `ED-IN-0292` survives to Jordan (§D).

### 0.2 What this is read against

- HEAD `84d2a02`. Lane A (`IMPLEMENTATION_BRIEF_A.md`) was landing `03_PC_duel_chain_reach.md` and the
  obstacle work in a worktree; every figure here is the **baseline** that lane moves.
- **This lane's reading:** `python -m engine.season.harness.aperture 1 0` (realm and spine, seed 0, one
  season, `PYTHONHASHSEED=0`, control `content_hash EQUAL`), written by the Fable lane before its cut-off
  to `scratchpad/runs/VERBS_SOCIAL1/aperture_1_0.txt`. **Second reading, not re-run:** the PHYSICAL lane's
  `aperture 2 0` (two seasons) at `scratchpad/runs/VERBS_PHYSICAL/aperture_2_0.txt`, and its
  `corpus_run` (143 cases, seed 0) at `scratchpad/runs/VERBS_PHYSICAL/corpus_run.txt`, read at the line.
  Marked `[2s]` and `[corpus]` below. One seed is a reading of a trajectory, not a rate (CLAUDE.md §0.1
  pt 4); nothing below is a balance claim.

### 0.3 State today, one line per verb

`elig` = persons eligible (seated / unseated); `att / ex / ref` = acts attempted / executed / refused.
Realm arm; `[2s]` the two-season reading.

| verb | elig | formed | att / ex / ref (1s) | `[2s]` att / ex / ref | deciding read of the refusals `[2s]` | verdict |
|---|---|---|---|---|---|---|
| `carry` | 33 / 50 | 46 | 4 / 2 / 2 | 17 / 4 / 13 | `exists:petition=0` 9 · post-admission 4 | **executes**; a third refused on a wrong-kind Record or a matter already docketed |
| `argue` | 33 / 50 | 33 | 10 / 3 / 7 | 41 / 10 / 31 | `with=False` 31 | **executes; three quarters refused** on an absent hearer |
| `commit` | 33 / 50 | 43 | 37 / 37 / 0 | 65 / 65 / 0 | — | **works** |
| `comply` | 33 / 50 | 45 | 16 / 0 / 16 | 33 / 0 / 33 | `exists:dispensation=0` 33 | **forms but is refused**; writes nothing even when admitted |
| `conceal` | 33 / 50 | 83 | 11 / 11 / 0 | 23 / 23 / 0 | — | **executes**; the cover is read by attribution; unranked (no celled axis) |
| `covenant` | 18 / 0 | 18 | 3 / 0 / 3 | 10 / 0 / 10 | `exists:Proposition=0` 10 | **forms but is refused** |
| `evade / defy` | 33 / 50 | 45 | 1 / 0 / 1 | 5 / 0 / 5 | `exists:dispensation=0` 5 | **forms but is refused** |
| `lie` | 33 / 50 | 42 | 6 / 2 / 4 | 22 / 6 / 16 | `clause:hearer` 16 | **executes; three quarters refused**; no band writes |
| `forgive` | 33 / 50 | 2 | 0 / 0 / 0 | 0 / 0 / 0 | — | **formed almost never** (no grievance it can read) |
| `give` | 33 / 50 | 21 | 0 / 0 / 0 | 19 / 1 / 18 | `with=False` 17 · post-admission 1 | **almost unreachable** |
| `challenge` | 33 / 50 | 83 | 48 / 0 / 48 | 84 / 0 / 84 | `exists:Person=0` 65 · `with=False` 13 · `dispute=False` 6 | **forms but is refused** (lane A's target) |

Of the family's declared kinds, never emitted in the one-season reading: `commitment.refused`,
`compliance.given`, `compliance.withheld`, `confidence.broken`, `covenant.offered`, `challenge.issued`,
`stance.moved`, `forgive.refused`, `give.refused`, `record.given`. Emitted: `commitment.made` 37,
`cover.assumed` 11, `petition.carried` 2, `argument.won` 2, `argument.lost` 1, `pursuit.moved` 1,
`news.told` 2 (of `lie`'s), `news.untold` 4. Pools rolled: `argue` and `lie` at pool 2 for every actor
("two actors at different pools: no"). `[corpus]`: `argue` 947 resolved (Failure 660), `lie` 138 (Failure
110); `comply`, `covenant`, `evade / defy` are among the 13 verbs only ever refused; `forgive` among the 30
never attempted; `lie`'s bands do not differ in writes; `comply`, `evade / defy`, `lie` are in "emits and
writes nothing, untagged".

### 0.4 The proposals that carry the edits

| file | verbs | batch |
|---|---|---|
| `proposals/14_VERBS_SOCIAL1_A_formation.md` | `covenant`, `comply`, `evade / defy`, `carry` (kind); `argue`, `lie`, `give`, `challenge` (believed co-location) | S1-A |
| `proposals/14_VERBS_SOCIAL1_B_documents_and_obedience.md` | `give` (delivery), `comply`, `evade / defy`, `covenant` (in force) | S1-B |
| `proposals/14_VERBS_SOCIAL1_C_persuasion_and_deceit.md` | `argue`, `lie`, `conceal` | S1-C |
| `proposals/14_VERBS_SOCIAL1_D_grievance_and_settlement.md` | `forgive`, `challenge` (beyond lane A), `carry` (venue), `commit` | S1-D |

The per-verb sections follow, in the order of the work order. Each has the nine parts the brief orders.

### 0.5 Two shared rules this family introduces (each with one owner)

- **R-WITH, believed co-location.** `queries/person_q.py::believed_with(claims, other, now, window)`:
  True when the holder's newest FIRSTHAND claim that names `other` (a `seen` claim's `Seen.who`, or a deed
  claim whose subject is `other`, or a telling `other` gave him) has `when >= now - window`, window the
  fixture `with_belief_window` (proposed: one season's ticks; control: unbounded, which is today's
  formation). A firsthand claim is deposited by WITNESS only to persons present, so a recent one is the
  person's own evidence that `other` is where he is. Read in formation by CHAR-OFFER's one decline for
  every row whose cell carries a WORLD-ONLY `with` conjunct, from the conjunct's own `of:` operand; never
  by verb name. The fold's `with` stays WORLD-ONLY and unchanged (`ED-IN-0282` is not reopened): a man can
  still be wrong, and then the fold refuses him. Proposal A.
- **R-KIND, the Record sub-kind at formation.** Lane A's rule (`03_PC_duel_chain_reach.md` edit 4): a
  `referent_class: Record` row whose cell has `existence … kind: K` forms only on a Record of kind K. This
  family does not redo it; it names the rows it repairs here (`comply`, `evade / defy`, `carry`).

---

## 1. `carry` — put a held petition before the room

**1. Premise.** *A person who holds a petition carries it before the court that can hear it, so the matter
is docketed and will be decided.* Links: (a) a petition exists and he holds it; (b) a room exists whose
remit covers what the petition is about; (c) the matter is put on that room's docket; (d) a sitting hears
it and a determination binds; (e) the petitioner learns the outcome.

**2. State today.** Row `verb_table.yaml:108`: `own`; `referent_class: Record`; cell `existence kind:
petition` ∧ `held_by`; no roll; writes `Record.stages`, `DocketItem.*`; emits `petition.carried`; refusal
`carry.refused`. Effect `loop/effects_information.py::_eff_carry` (`:448`): rewinds the petition's stages
and appends `_docket_item(terms, None, pid)` — **no arrangement**, so link (b) is absent: the item names no
room's rule (`world_q.judging_set` gap, the docstring's own [ASSUMPTION]). Declines: not a petition; no
`terms`; already `docketed`; stages unchanged. Readers: `determine` (docket conjunct), `speak`
(`exists:DocketItem`), the strife roster (`petition.carried` joins a strand), `world_q.docketed_by`.
Reading: 1s 4 att / 2 ex / 2 ref (`exists:petition=0`); `[2s]` 17 / 4 / 13 (`exists:petition=0` 9,
post-admission 4: the matter was already docketed). `determine` in the same reading executes 0 (BINDING
§`determine`, refused on `docket`), so link (d) does not complete. **Verdict: executes; consequence reaches
the docket and stops there.**

**3. Build-out, decided.**
- *Formation:* R-KIND (petition only); and a person-side decline when his own ledger holds a claim that
  the matter is already docketed (`docket.formed` / `petition.carried` / `case.opened` claim whose
  docketed matter is the petition's `terms`, read by `world_q.docketed_by`'s person-side twin). The
  world-side `docketed` decline stays for a hand-built act.
- *Room:* the docket item names the arrangement row of the **venue whose purview contains the petition's
  matter at the actor's place** — the first `court`-kind venue up the actor's containment chain whose
  arrangement admits petitions (`arrangements.yaml`, an `admits_petition: true` key, default true on
  courts). One reader, `world_q.petition_venue(w, actor, matter)`. This closes the `None` arrangement
  [ASSUMPTION] in `_eff_carry`; `05_SC_arrangement_rows_that_bind.md` owns the arrangement row itself.
- *Roll:* none. Filing is a right of anyone holding a petition; the contest happens at `speak`/`determine`.
  A refusal is never a dead end: the petition stays held and can be given to someone with standing.
- *Effects:* unchanged writes, plus the arrangement on the item; emits `petition.carried`.
- *Appeal (the reopenable file, ARCS e5):* a petition whose matter has been determined may be carried to
  the **next venue up** (`petition_venue` walking past the venue that determined it). One rule: the
  reader skips venues whose docket already determined this matter.
- *Costs:* a scene. *Unlocks:* `speak` on the matter, `determine` by the bench. *Forecloses:* a second
  carry of the same matter to the same room.
- *Reason trail:* the docket item names petition, arrangement and venue; `petition.carried` is witnessed.

**4. Scales.** Person (the petitioner) → settlement or realm (the venue). An unseated person's only route
to a binding decision. NPC chooses through the one chooser on held petitions (`held_record_claims`).

**5. Tuning.** Venue (`arrangements.yaml`: `admits_petition`, the `standard:` of SC-OB); office (a seated
petitioner's standing enters at `speak`/`determine` as `reception`, not here); season (sittings,
`convene`'s dates).

**6. Exact edits.** Proposal D §1 (venue and appeal); proposal A §2 (R-KIND names `carry`).

**7. Gate and falsifier.** `aperture 2 s` (s = 0, 1): `carry` refusals `exists:petition=0` = 0; every
`petition.carried` docket item names a non-`None` arrangement; at least one carried matter reaches a
`determine` attempt (`matter.determined` or a `determine` refusal on any conjunct but `docket`). Planted
failure: delete the court venue's `admits_petition` and every carry declines, naming the venue reader.

**8. Cases.** M-SIT cases (ARCS §4 row 7: "a matter gets before a room on a date"); ARC-31 (Quaestio of
Baralta), ARC-21 (Excommunication) need a docketed matter heard; e5 cases (ARC-04, -06, -10) need appeal.

**9. NERS.** N: the only unseated route to a binding decision; removing it leaves petitioning inert. R: a
commoner's grievance can reach a court with nobody watching. S: one docket owner (`docketed`), one venue
reader. E, last: one reader and one row key against a docket that today names no room. **Cut test:**
merging into `petition` (file-and-carry in one act) loses the gap between holding and carrying in which a
petition can be given, seized or destroyed (M-REC); keep it.

---

## 2. `argue` — move a hearer toward one's position

**1. Premise.** *A person argues a position to someone present, and if he argues well the hearer comes
round, part way or wholly.* Links: (a) a position (Proposition) exists; (b) the hearer is present;
(c) a contest whose obstacle is the task plus the hearer's resistance; (d) the hearer's pursuits move by
degree; (e) the hearer's later choices differ.

**2. State today.** Row `:133`: `own`; `referent_class: Proposition`; cell `existence Proposition` ∧
`with` of `to`; `counterparty: to`; `contests: a proposition`; writes `Person.pursuits` at Overwhelming
and Success; emits `argument.won` at Partial too (with no write), `argument.lost` at Failure. Effect
`_eff_argue` (`:647`) through `person_q.argued_pursuits`. Reading: 1s 10 att / 3 ex / 7 ref (`with=False`
7); `[2s]` 41 / 10 / 31 (`with=False` 31); pool 2 for every actor; `[corpus]` 947 resolved, Failure 660,
Overwhelming 2. Obstacle today: `obstacle_default` 2 (nobody holds a score; F-SC-03). Reader of the
consequence: `choose`'s pursuit score (the hearer's later choices). **Verdict: executes; three in four
formed acts are dead ends on co-location; the roll does not differ by person; Partial claims a win and
changes nothing.**

**3. Build-out, decided.**
- *Formation:* R-WITH on `to`. The arguer forms on known persons he has firsthand seen this season.
- *Roll:* pool from `verb_capability: argue` (already a row). Obstacle per SC-OB: `difficulty: routine`,
  `opposition` = hearer's `argue` score × `opposition_rate`, `regard` = hearer's stance toward the arguer
  (no bench), `evidence` = the arguer's cited items for the Proposition, and in a sitting `reception`
  replaces `regard`. A **commitment term** (proposed new `obstacle_terms` member, `commitment`): a hearer
  holding a live `commit` to a Proposition contrary to the argued one adds `commitment_ob` (fixture,
  proposed 1.0, control 0) — affiliation tuning, read off his own tenures (`world_q`'s commit readers).
- *Effects by degree (graded, recoverable):* Overwhelming: pursuits shift × 2 `pursuit_shift`; Success: × 1;
  **Partial: × 0.5 and `Person.pursuits` is written** (today it writes nothing and still emits
  `argument.won` — a deed that did not happen; the row's Partial `writes:` gains `Person.pursuits`);
  Failure: nothing moves, and the hearer still gains the claim of the arguer's position (WITNESS's deposit
  of `argument.lost`, already firsthand to him) — a later `argue` may cite new evidence.
- *Costs:* a scene. *Forecloses:* nothing. *Reason trail:* SC-OB's `terms` on the Event.
- *Consequences:* `choose` (pursuit score), `covenant` (a moved hearer commits), `faction_q` (membership by
  commit), CHAR's `which_ground_moves_whom` (susceptibility — the hearer's cast row decides which grounds
  move him; this verb is its main caller).

**4. Scales.** Person to person; in a sitting, person to bench (the same verb with `reception`). A faction
argument is many person arguments; no faction-scale argue. NPC: one chooser, ranked by the Proposition's
alignment to the arguer's pursuits.

**5. Tuning.** Venue (`reception`, SC-OB), personality (`which_ground_moves_whom`: susceptibility on the
cast row), affiliation (`commitment` term), relationship (`regard`), evidence (`proof_step`), season (none).

**6. Exact edits.** Proposal A §1 (R-WITH); proposal C §1 (row, terms, Partial write).

**7. Gate and falsifier.** `aperture 2 s`: `argue` refusals `with=False` fall by at least half; pools
rolled differ across actors (after lane A's persons-hold-scores); a two-NPC hand-built fold with the
hearer committed to a contrary Proposition in one arm shows `commitment` in `terms` alone. Planted failure:
set `with_belief_window` unbounded and the refusal count returns.

**8. Cases.** ARC-31 (formal debate), ARC-21 (a formal challenge's argument), the e5 multi-tier verdict
cases; chooser demand c7 (ARCS §9).

**9. NERS.** N: the only verb that moves another's pursuits by persuasion. R: positions spread without a
player. S: one obstacle composition with `tell`, `lie`, `speak`. E, last: two data edits and one column
change against 31 of 41 wasted acts. **Cut test:** folding into `speak` loses the private, benchless
argument; keep.

---

## 3. `commit` — take a position as one's own

**1. Premise.** *A person commits himself to a cause or claim, and is thereafter counted as its adherent.*
Links: (a) the Proposition exists; (b) he binds himself; (c) others read him as committed; (d) he can
later release it.

**2. State today.** Row `:209`: `own`; `referent_class: Proposition`; cell `existence Proposition`; writes
`Tenure.since` (a `commit` Tenure, `_eff_commit` `:1252`); emits `commitment.made`; duplicate declined
person-side (`rosters.yaml: held_edge_declines`). Readers: `faction_q` (membership is a commit edge),
`world_q` (adherents, opinion), `predicates.py:176`, `release` (closes it). Reading: 1s 37 / 37 / 0;
`[2s]` 65 / 65 / 0. **Verdict: works.**

**3. Build-out, decided.** No change to formation, roll (none: a commitment is one's own) or effect. Two
consequences to wire, owned elsewhere and named here: `covenant` is in force when both parties hold a
`commit` to its terms (proposal B §3); `argue`'s `commitment` term reads it (proposal C). Costs: a scene;
forecloses nothing but is read by contrary arguments.

**4. Scales.** Person; aggregated to faction by `faction_q`. **5. Tuning.** Affiliation (which
Propositions are offered: those he utters or hears; `terms_sourced` for held documents). **6. Exact
edits.** None. **7. Gate.** The existing reading stands; regression: `commitment.made` count non-zero at
`aperture 1 0` after batches S1-A..D. **8. Cases.** CHAR §7 "loyalty to a cause" (Kreutz, Ehrenwall,
Torberg). **9. NERS.** Works; E high. **Cut test:** removing it removes faction membership by choice.

---

## 4. `comply` — do what the writ orders

**1. Premise.** *A person who receives a lawful order obeys it, and is then bound to the service it
names; the issuer and the room know he obeyed.* Links: (a) a writ addressed to him exists; (b) it reaches
him; (c) he chooses to obey; (d) obedience binds him (a service, a duty); (e) the issuer, and those who
see it, read the obedience.

**2. State today.** Row `:227`: `own`; `referent_class: Record`, `referent_named`; cell `existence kind:
dispensation` ∧ `own_ledger`; **no effect body; writes `[]`**; emits `compliance.given` (read by no code);
refusal `compliance.impossible`. Formation: `world_q.writs_held` (a writ on his own `hold` naming him);
writs are minted into the issuer's hand (`ED-IN-0292` (1)), so link (b) is `give` alone. Reading: 1s
16 / 0 / 16; `[2s]` 33 / 0 / 33, every refusal `exists:dispensation=0` (a held Record of another kind,
`record_subkind`); `[corpus]` only refused. **Verdict: forms but is refused; would write nothing if
admitted.**

**3. Build-out, decided.**
- *Formation:* R-KIND (dispensation only, lane A). The occasion: `writs_held` (unchanged).
- *Roll:* none. Obedience is the person's choice; whether he *can* perform the order is the order's own
  verb (a writ to `march` is obeyed by marching).
- *Effects (ungraded, but never a dead end):* `comply` **opens an `oblige` Tenure** from the complier to
  the issuing seat (`world_q.issuing_seat(w, rid)`: the `via` of the act that minted the Record, read
  through `state/attribution.py::causing_act` on its minting Event; `None` for a seatless mint, and then
  the `oblige` is not opened and only the hold closes — `[UNVERIFIED]` that every minting Event resolves
  to its act after a load), with
  `term` = the writ's own stages' last due tick (the order lasts as long as it says), `payload =
  {"writ": rid}`. This composes on `oblige`'s existing Tenure (`_eff_oblige`, `rosters.yaml` tenure kind
  `oblige`), so a complier is read by every reader of sworn service: `purview_reaches`' oblige clause,
  `establishment_of`, legitimacy. It also **closes his `hold` on the writ** — he has answered it, which
  removes the occasion (`writs_held` no longer stamps it) and ends the scene tax `writs_held`'s docstring
  records ("NO 'ALREADY ANSWERED' DECLINE").
- *Emits:* `compliance.given` (now with a write behind it), witnessed: the issuer's ledger gains a deed
  claim his pursuits judge (obedience to his own writ leans with his pursuits), so his `regard` of the
  complier rises through the existing `deeds_judged`.
- *Refusals:* `compliance.impossible` keeps only the hand-built case (the writ is gone, or not his).
- *Costs:* the `oblige` binds him; forecloses `evade / defy` on the same writ (the hold is closed).

**4. Scales.** Person → seat (settlement/realm office). The realm's obedience is the sum of compliances;
the strife roster reads defiance, and now the `oblige` edges read compliance.

**5. Tuning.** Office (issuing seat's legitimacy in the complier's eyes drives the choice through
`choose`'s legitimacy term), affiliation (a writ whose terms violate a held affiliation scores low:
`violated_affiliations`), relationship (`regard` of the issuer), season (the term).

**6. Exact edits.** Proposal B §2.

**7. Gate and falsifier.** A seeded realm with the writ delivered (proposal B's delivery occasion, or a
planted `give`): `compliance.given` > 0, each with an `oblige` edge whose payload names the writ; the
issuer's `regard` of the complier rises versus the control arm with the comply effect removed. Planted
failure: drop the hold closure and the same complier forms `comply` on the same writ next round.

**8. Cases.** ARCS M-SIT ("ruling separate from enforcement"); strife moves `RU` (refusal or inaction) need
its opposite to exist.

**9. NERS.** N: without it an order binds nobody (BINDING's `issue` verdict: "binds nobody"). R: obedience
becomes a record others weigh. S: composes on `oblige`; no new Tenure kind. E, last: one effect body on
existing kinds. **Cut test:** merging `comply` into `oblige` (oblige to the writ's seat) loses the writ
link — the obedience would not answer a particular order; keep the verb, share the Tenure.

---

## 5. `conceal` — act under a cover

**1. Premise.** *A person assumes a cover, so that what he does next is attributed to the cover and not to
him, until someone sees through it.* Links: (a) he makes a cover; (b) his later deeds are witnessed as the
cover's; (c) an inquirer can penetrate it, harder the better it was made; (d) once penetrated, the deeds
return to him.

**2. State today.** Row `:251`: `own`; `requires: —`; writes `Record.exists` (a `cover` Record keyed to
the actor, `_eff_conceal` `:292`); emits `cover.assumed`; no refusal. Reader: `state/attribution.py::
live_cover` / `anchor_of` (tier 1): every Event the actor causes while the cover lives is anchored on the
cover's id, so WITNESS deposits deed claims on the alias. Reading: 1s 11 / 11 / 0; `[2s]` 23 / 23 / 0.
`[corpus]`: `conceal` is in RANKING EXCLUDES (no celled axis), so its choice is broken by the draw, not
by any reason. Link (c): no inquiry reads a cover's quality (SC-OB's `subject` term names "a cover's
quality when FI lands one"). **Verdict: executes, and the consequence is read; it is chosen at random and
cannot be seen through by degree.**

**3. Build-out, decided.**
- *Formation and ranking:* the chooser ranks `conceal` by **what it would hide**: the largest
  `violated_affiliations` / `violated_pursuits` weight among the other acts the person forms in the same
  deliberation (a deed he expects others to judge against him). A celled axis is not invented; the score
  term is `choose`'s, read off his own candidates (person-side). Zero when he forms nothing judgeable, so
  he does not mask idly.
- *Roll:* an uncontested quality draw at mint: `quality` = the actor's `conceal` capability score
  (new `verb_capability` row `conceal: tradecraft`; ARCS §8 names tradecraft as an authored skill).
- *Effects:* the cover Record gains a `quality` content key (`rosters.yaml: record_kinds.cover`), read by
  the inquiries as SC-OB's `subject` term (`surveil`, `examine`, `research` on a deed claim anchored on a
  cover). A Success by an inquirer **unmasks**: the cover's stages close (`Record.stages` matured now) and
  WITNESS re-deposits the inquirer's copy with the actor as doer — owned by FI's inquiry effect, named
  here as the consumer. The cover otherwise lapses at its stages (existing).
- *Costs:* a scene. *Forecloses:* nothing.

**4. Scales.** Person; a faction's spy network is many covers. **5. Tuning.** Personality (tradecraft
capability), season (cover lifetime = `record_stages_default`), evidence (quality as `subject` term).

**6. Exact edits.** Proposal C §3. **7. Gate and falsifier.** Hand-built two-arm fold: an actor with a
cover of quality 6 and one of quality 0; one `surveil` against each anchored deed; the two Events'
`terms` differ in `subject` alone. Realm: `conceal` attempts correlate with a same-deliberation
judgeable act (≥ 0.8 of attempts) against the control (draw-ranked). Planted failure: drop the score
term and the correlation returns to chance.

**8. Cases.** ARC-09 N2 and ARC-30 N1 (a concealed identity undetectable to non-specialists), NPC-004
N6 (concealment kept up scene by scene), ARCS e6 (suppressing evidence changes a case).

**9. NERS.** N: the only route by which a deed is misattributed. R: the hidden actor, a story with nobody
watching. S: quality enters inquiry as SC-OB's existing `subject` term. E, last: one capability row, one
content key, one score term. **Cut test:** without it, every witnessed deed names its doer; keep.

---

## 6. `covenant` — bind two parties to terms

**1. Premise.** *Two parties agree terms, each binds himself to them, and the agreement is then in force
and read by what it governs (tribute, alliance, marriage).* Links: (a) terms (a Proposition) exist; (b)
one party offers the instrument; (c) it reaches the other; (d) the other accepts (commits); (e) in force
when both are committed; (f) its readers act on it; (g) breaking it is visible.

**2. State today.** Row `:300`: `remit:issue`; `beneficiary: to`; cell `existence Person` of `to` ∧
`existence Proposition` of `subject`; **no `referent_class`**; writes a `dispensation` Record
(`_eff_covenant` = `_eff_issue`, `:275`); emits `covenant.offered`; refusal `covenant.refused`. Link (c)
is `give`; (d) is `commit` via `terms_sourced`; (e) "a reading nothing performs yet" (the effect's own
docstring); (f) deferred. Reading: 1s 3 / 0 / 3; `[2s]` 10 / 0 / 10, every refusal
`exists:Proposition=0` (`collection`: the subject is no Proposition). **Verdict: forms but is refused;
links (e)–(g) unbuilt.**

**3. Build-out, decided.**
- *Formation:* `referent_class: Proposition` (`argue`'s and `commit`'s class; the rung-4 repair of
  `03_PC_duel_chain_reach.md`), and R-WITH is **not** applied (an instrument can be drawn up in absence;
  it travels by `give`).
- *Roll:* none to draw up. (Agreement is the counterparty's `commit`, his own choice.)
- *Effects:* as today; plus the in-force reader `world_q.covenant_in_force(w, rid) -> bool`: the
  Record's maker and its `to` each hold a live `commit` to its `terms`. One owner; readers: tribute
  (`_renewals`) and allied sides (`mustered`), both named deferred in the effect docstring and both
  owned by FA/MB — this proposal builds the reader and names them as consumers, and adds one reader of its
  own that needs no other lane: **`legitimacy`'s deed judgement** — a party who `release`s his commit to
  in-force terms emits `commitment.ended` on a covenant's terms, which WITNESS deposits as a deed claim
  the other party's pursuits judge (a broken covenant is a grievance, read by `holds_dispute`, i.e.
  grounds for `challenge`).
- *Delivery:* proposal B's addressed-document occasion for `give` (the instrument's `to`).
- *Costs:* the maker binds his seat's word. *Forecloses:* nothing; a second covenant on the same terms
  to the same party is declined person-side (`held_document_declines`' shape: he holds one already).

**4. Scales.** Seat to person (a lord's charter), seat to seat (a treaty: the counterparty is the other
seat's holder). A person-to-person oath without office is two `commit`s to one uttered Proposition; no
covenant is needed for it (`remit:issue` stays).

**5. Tuning.** Office (only `issue`-remit seats), affiliation (terms aligned with the counterparty's
pursuits make his `commit` likelier, through `choose`), relationship (`regard`), season (the instrument's
stages = its duration).

**6. Exact edits.** Proposal A §3 (class); proposal B §3 (in force, breach, decline).

**7. Gate and falsifier.** `aperture 2 s`: `covenant` refusals `exists:Proposition=0` = 0 and
`covenant.offered` > 0. Planted-delivery run: maker and addressee both commit → `covenant_in_force`
True; addressee releases → a deed claim in the maker's ledger and `holds_dispute(maker, addressee)` True.
Control: reverted class reproduces the pre-change refusals.

**8. Cases.** ARC cases on marriage and alliance contracts (CHAR §7 "sworn bond"); FA tribute.

**9. NERS.** N: the only consensual binding between parties. R: alliances form and break with nobody
watching, and a breach feeds the duel chain. S: no new kind (a dispensation), in-force read off two
`commit`s. E, last: one class line, one reader. **Cut test:** folding into `issue` loses the two-sided
acceptance; keep.

---

## 7. `evade / defy` — refuse the order

**1. Premise.** *A person who receives an order refuses it, openly or by evasion; the issuer learns of it
and may enforce.* Links: (a)–(b) as `comply`; (c) he refuses; (d) the refusal is visible to the issuer;
(e) it is grounds for enforcement (arrest, revocation); (f) it opens strife.

**2. State today.** Row `:457`: as `comply` (`requires: as comply`); writes `[]`; emits
`compliance.withheld` — **read by the strife roster** (`rosters.yaml:3388`, `opens:`) and by
`harness/strife_moves.yaml` (`RF`, `RU`). Reading: 1s 1 / 0 / 1; `[2s]` 5 / 0 / 5, every refusal
`exists:dispensation=0`. **Verdict: forms but is refused; the one reader exists.**

**3. Build-out, decided.**
- *Formation:* R-KIND (lane A).
- *Two faces, one row (the slash is kept):* the payload's `mode` ∈ `rosters.yaml: defiance_modes`
  `[evade, defy]` (choice-sourced, `choice_sourced` roster; `marshal`'s `role` shape). **defy**: the
  refusal is announced — `compliance.withheld` is witnessed by those present and **told** to the issuer
  (it opens strife). **evade**: an uncontested quiet non-performance — no Event names the defier until the
  writ's term matures, when MATTER emits `compliance.withheld` naming him (the writ's stages carry a
  `due` label `answer`). Evasion buys time and risks discovery; defiance is immediate and honest.
- *Effects:* both close his `hold` on the writ (the occasion is answered, as `comply`'s). `defy` writes
  his own `Person.stance` toward the issuing seat's holder (−1 valence, weight 1: he has set himself
  against him), so `forgive` and `regard` see it.
- *Consequences:* the issuer's ledger gains a deed claim (`compliance.withheld`) his pursuits score
  against the defier → `holds_dispute` (grounds for `challenge`), and is the occasion for `arrest` (PHYSICAL
  lane: a defiance claim is a warrant ground, `warrant_sourced`) and `revoke` (BINDING lane). Strife reads
  it unchanged.
- *Costs:* standing with the issuer. *Forecloses:* `comply` on that writ.

**4. Scales.** Person → seat; a settlement's mass defiance is many defy acts; the strife layer aggregates.

**5. Tuning.** Personality (pursuits violated by the writ's terms), affiliation (the issuer's faction vs
his own commit), office (issuer legitimacy), relationship (`regard`), season (the evasion's due tick).

**6. Exact edits.** Proposal B §2 (the shared obedience effect with `comply`).

**7. Gate and falsifier.** Planted-delivery run: one writ whose terms violate the addressee's pursuits;
he forms `evade / defy`; with `mode: defy` the issuer's ledger holds `compliance.withheld` in the same
season; with `mode: evade` only after the due tick; a strife strand opens in both. Planted failure: drop
the hold closure and the occasion repeats.

**8. Cases.** Strife moves RF (refusal or mutiny) and RU; ARCS "ruling separate from enforcement".

**9. NERS.** N: an order that cannot be refused is not an order; the strife opener depends on it.
R: rebellion with nobody watching. S: one obedience effect for both verbs. E, last: one payload roster,
one stance write. **Cut test:** merging `evade` and `defy` loses the time-versus-honesty choice; the
slash already merges them in one row, which is right — keep the row, give the payload two values.

---

## 8. `lie` — tell someone something false

**1. Premise.** *A person tells someone present a falsehood; if believed, the hearer holds it as true and
acts on it; if caught, the liar's standing with him falls.* Links: (a) the liar holds a fact he can falsify;
(b) the hearer is present; (c) a contest against the hearer's discernment and disposition; (d) believed:
the false claim lands at a confidence set by degree; (e) disbelieved: the hearer knows he was lied to;
(f) a later contradiction counts against the liar.

**2. State today.** Row `:534`: `own`; cell `own_ledger` of `subject` (`holds`) ∧ `with` of `to`
(`hearer`); `counterparty: to`; `contests: a standing`; writes `[]` at every band; emits `news.told` +
`confidence.broken` at Overwhelming/Success/Partial, `news.untold` at Failure; refusals `tell.refused` per
clause. Formation gated by `Fixtures.lie_offered` (shipped True) and `rosters.yaml: lie_verbs`; the
false value is `person_q.lie_said_of` (cells only; numbers moved one band step; booleans flipped), carried
on `payload["said"]` and deposited by WITNESS through the told channel; `decision/options.py::record`
counts a contradicted lie against the liar (H-183). Reading: 1s 6 / 2 / 4 (`clause:hearer` 4); `[2s]`
22 / 6 / 16 (`clause:hearer` 16); pool 2 everywhere; `[corpus]` 138 graded, Failure 110, "bands that
differ: False". **Verdict: executes; three in four formed acts are dead ends on co-location; every band
that is not Failure has the same consequence; Failure has none.**

**3. Build-out, decided.**
- *Formation:* R-WITH on `to` (the `hearer` conjunct).
- *Roll:* pool from `verb_capability` (new row `lie: deceit`; DICE's capability map is the owner).
  Obstacle per SC-OB: `difficulty: routine`; `opposition` = hearer's score on the **perceiving**
  capability (`verb_capability: lie` names the liar's key; the hearer's opposing key is the row's
  `opposed_by:` — a new column read by the one pool reader, `10_DICE_one_score_two_roles.md`'s `score()`,
  only where present); `regard` (hearer's stance to liar); a **contradiction term** (`contradiction_ob`,
  proposed 1.0, control 0) when the hearer holds the cell firsthand — read by the host, which may read the
  hearer's ledger because the host builds the counterparty's side (SC-OB "how an NPC-versus-NPC contest
  gets its obstacle").
- *Effects by degree (the told deposit already exists; the band now sets its confidence):*
  Overwhelming: deposited at the liar's own confidence; Success: −1; Partial: −2 (floor 1, believed but
  doubted); **Failure: nothing false is deposited, and the hearer gains a firsthand deed claim
  `deceit.exposed` naming the liar** (a new kind in the `lie` row's Failure `emits:`, in `EMITTED_KINDS`),
  judged by his pursuits (`deeds_judged`) → his regard of the liar falls, and it is grounds for a dispute.
  The confidence is a WITNESS-side read of the Event's band (`loop/witness.py`'s told deposit takes
  `confidence` from the Said; the band adjusts it, one owner: a `lie_confidence_by_band` fixture table).
- *Costs:* a scene; the risk of exposure (Failure is the most likely band today, 110 of 138).
- *Consequences:* the hearer's choices (a false cell drives `requires` reads in his formations); the
  liar's `record`; disputes (`holds_dispute`) and so `challenge`; FI (a told falsehood is evidence that
  can be contradicted).

**4. Scales.** Person to person; a faction's propaganda is many lies and tellings (the told channel
spreads a believed falsehood onward at the hearer's confidence — existing behaviour).

**5. Tuning.** Personality (deceit vs perception capabilities), relationship (`regard`), evidence
(`contradiction` term), venue (none: a lie in a sitting is `speak`'s), season (none).

**6. Exact edits.** Proposal A §1 (R-WITH); proposal C §2 (row, capability, terms, Failure deed,
confidence by band).

**7. Gate and falsifier.** Corpus run: "bands that differ" for `lie` becomes True; `aperture 2 s`:
`clause:hearer` refusals fall by at least half; a two-arm hand-built fold (hearer holds the cell
firsthand vs not) differs in `contradiction` alone; a Failure deposits `deceit.exposed` and
`stance_toward`-free `regard(hearer, liar)` falls versus a control with the Failure deposit removed.

**8. Cases.** M-INFO (ARCS §4 row 2: "reports that differ from what is held"); chooser demand c7 (29
cases); ARC-37 (a supply chain carrying a good under a false account).

**9. NERS.** N: the only route by which a person believes a falsehood on purpose. R: deceit spreads and
is caught without a player. S: one obstacle composition with `tell`/`argue`; one told channel. E, last:
a column, a fixture table and one deed kind against a verb whose four bands are three alike. **Cut
test:** folding into `tell` with a `false` flag would lose the separate formation gate (`lie_offered`)
and the distinct Failure consequence; keep.

---

## 9. `forgive` — let a grievance go

**1. Premise.** *A person forgives someone who wronged him; his grievance ends, he no longer seeks redress,
and the forgiven may learn of it.* Links: (a) he holds a grievance (a wrong he judges against the
other); (b) he chooses to forgive; (c) the grievance stops counting: no dispute, no challenge on it;
(d) his disposition toward the other recovers; (e) a new wrong can start a new grievance.

**2. State today.** Row `:573`: `own`; `requires: —`; writes `Person.stance` (removes rows `held_against`
— negative stance rows naming the referent; `_eff_forgive`, `loop/effects_combat.py:827`); emits
`stance.moved`; refusal `forgive.refused`; formation declined person-side unless `held_against` is non-empty
(`rosters.yaml: own_stance_declines`). **The grievance a person acts on is not a stance row**: `challenge`'s
`dispute` conjunct is `person_q.holds_dispute` over **deed claims** (`deeds_judged`), which `forgive` never
touches; stance rows are written only by `march` (a lost field) and seeded, and `march` fights 0 fields
(PHYSICAL §0.3). Reading: 1s formed 2, attempted 0; `[2s]` the same; `[corpus]` never attempted.
**Verdict: formed almost never; when executed it would not end the grievance that drives challenges.**

**3. Build-out, decided.**
- *What a grievance is:* one owner, `person_q.holds_dispute` (CR-88 re-points it to `grievance_against`;
  this build-out follows whichever is the owner at landing and adds nothing beside it).
- *Formation:* the person forms `forgive` on a referent when **either** `held_against` is non-empty **or**
  `holds_dispute` is True (the `own_stance_declines` reader widened to the one grievance owner; through
  CHAR-OFFER's one decline).
- *Roll:* none. Forgiveness is the forgiver's own act.
- *Effects:* removes the `held_against` rows (as today) **and writes a forgiveness mark**: a stance row
  `(referent, 0, 0, since=tick)` — zero valence and weight, so `stance_toward` and `held_against` are
  unchanged by it — which `attributed_deeds` reads to **skip the holder's deed claims about the referent
  whose `when` is at or before `since`**. One reader (`person_q.forgiven_since(p, referent)`), read by
  `attributed_deeds`, so `deeds_judged`, `holds_dispute`, `regard` and `world_q.reception` all see the
  same forgiveness. A new wrong (a deed after `since`) starts a new grievance. [ASSUMPTION: a fourth
  element on a stance row; K-49 says a row carries no KIND, and this carries a tick, not a kind; revert:
  a `Person.forgiven: dict[referent, tick]` field.]
- *Emits:* `stance.moved`; witnessed by those present, **told to the forgiven** when he is present (the
  Event names him as subject; WITNESS's firsthand deposit); his `deeds_judged` of the forgiver gains a
  deed that leans with mercy-weighted pursuits (`deed:stance.moved` cells, authored in `rosters.yaml`'s
  deed cells — an `assumption` row).
- *Ranking:* `choose` ranks it by the grievance's own magnitude against the forgiver's mercy/peace
  pursuit weights (existing alignment cells for `forgive`).
- *Costs:* gives up the grounds for `challenge`. *Forecloses:* `challenge` on that grievance (the dispute
  reads False), until a new deed.

**4. Scales.** Person; a lord's forgiveness of a rebel is the same act from a seated person, and composes
with BINDING's `pardon` (which releases a restraint) — two verbs, two objects: `pardon` ends a sentence,
`forgive` ends a grievance.

**5. Tuning.** Personality (mercy-leaning pursuits), relationship (`regard`, stance), season (deed age:
older grievances cost less to forgive, through `recent_claims`' window if CR-88 uses one).

**6. Exact edits.** Proposal D §2.

**7. Gate and falsifier.** Planted run: A holds a firsthand deed claim of B's judged against B
(`holds_dispute(A, B)` True); A forms and executes `forgive`; `holds_dispute(A, B)` is False after, and
A forms no `challenge` on B; a later planted deed by B makes it True again. Realm: `forgive` attempted > 0
over `aperture 2 s`. Planted failure: drop the `attributed_deeds` skip and the dispute survives the
forgiveness.

**8. Cases.** CHAR §7 (feud, rivalry); the duel chain's off-ramp (a dispute must be endable without a
duel, or every dispute ends in blood or never).

**9. NERS.** N: the only off-ramp from a grievance; without it disputes only end by a duel. R: reconciliation
with nobody watching. S: one grievance owner read by challenge and forgive alike. E, last: one widened
decline and one mark. **Cut test:** merging into `pardon` conflates a legal restraint with a private
wrong; keep.
