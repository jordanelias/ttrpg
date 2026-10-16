# Comparative analysis: how the ten lane evaluations interact

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · resolves nothing at runtime · no recommendation here enters a plan or ledger until Jordan so rules
## Date: 2026-10-16 · Lane: IN (cross-cutting) · read at HEAD `bd8105b`, code-equal to `5445e34` (`git diff --stat 5445e34 bd8105b -- engine modules systems workplans architecture references CURRENT.md` is empty)

**What this is.** Jordan asked for "a comparative analysis as its own section that weaves together and
reconciles how this work may interact", in a session meant "to identify all the missing areas of the game as
it exists in code/workplanv9". The ten lane files here each ran NERS and closed on recommendations. This file
does not restate them; it joins them: shared causes (C2), dependencies and collisions (C3), adjudication by a
stated rule (C4), shared evidence (C5), one register of missing areas (C6), one of Jordan's decisions (C7),
one set of recommendations (C8). Deleting it would change nothing the game does.

**Locators.** `[CHECKED path:line]` = opened by this pass. `[LANE <lane> <id>]` = relayed from a lane file or
its digest (where they disagreed, the lane file was opened and governs; C9). `[AUDIT <id>, <lines>]` = the
uploaded NERS audit `9d5d80bf` (the tracked `references/ners_audit_2026-10-14.md` differs only in its header
lines and two ED renders, [CHECKED `diff`]). `vt` = `engine/season/verb_table.yaml`; `req` =
`engine/season/requirements.yaml`; `p2`..`p8` = `workplans/valoria_master_workplan_v9_part2.md`..`_part8.md`;
`L1-01`, `L1-04` = `architecture/meta/01_AXIOMS.md`, `04_CODE_ARCHITECTURE.md`; `20G` = the uploaded *Twenty
Games, One Frame* (`6039edcc`). A lane row with no id of its own is written `<lane> <position>(H|B)`, HOLLOW or
BLOCKED.

---

## C0. VERDICT

**The ten lanes describe one game with one structural absence seen from ten sides: the season loop resolves
acts by persons who differ in what they want but not in what they hold, can do or know, so every seam where
one scale hands a magnitude to the next (a fight, a contest, an inquiry, a levy, a field army, the player's
view) is fed a default or nothing, and most missing areas are that seam left without a person-held carrier.**

| # | interaction (worst first) | joins | why it ranks here |
|---|---|---|---|
| 1 | **The troop chain.** Jordan's 2026-10-16 statements demand troops levied from settlements as their own resource, graded by equipment, experience and commander, assembled by factions into subunits with subformations. The tree sizes every season side as one `Line` of summed `Person.weight` at power 4, command 4 [CHECKED `modules/mass_battle/massbattle.py:170-232`]; the verb named `levy` moves `Rung.stores` to the seat's treasury [CHECKED vt:629-653; `loop/effects_governance.py:374-400`]; v9's IN-52 rests on the opposite premise, "`levy` moves stores, not troops", with LF-1..3 delegated "[ASSUMPTION; medium; Jordan to correct]" [CHECKED p4:137; p5:533]. | MB, SE, FA, NPC, IN, PC | Jordan's own demand, contradicted by the plan's premise; every army, commander, experience and conquest row waits on it (C3 D-1..D-6). |
| 2 | **The per-person source.** `Person.capability` is empty on 429 of 430 corpus persons [CHECKED req:1244-1247]; the combat seam builds `Combatant(a_id, end=a_end)` and nothing else [CHECKED `modules/combat/fight.py:45`]; H-200 (competence) has zero plan mentions [CHECKED grep of the eight plan files]; the source is J-13's remainder, J.2 rank 1 [CHECKED p5:514]. | PC, SC, MB, NPC, FI, IN, WR, GO | One unruled source starves the body, the contest, the commander, the witness and creation at once; R-09 cannot be met without it. |
| 3 | **Acts that carry no content.** Six inquiry rows write nothing [LANE FI T-FI-1; BASELINE B3]; an authored OUGHT's predicate is read by nothing (H-185, zero plan mentions [CHECKED]); every computed `utter` mints an OUGHT, so war is never uttered [LANE FA M-FA-1]. | FI, WR, IN, SC, FA, NPC, PC | The chronicle, the investigator's record, deception, war and ambition each need a predicate nobody writes. |
| 4 | **No player surface and no pause.** IN-46 and IN-47 have landed designs and "no build batch"; R-04, hence M1, "cannot read `met` until a build batch exists for IN-46 and IN-47" [CHECKED p4:32-36]. What the surface may show is split inside ratified Layer 1: "No state is hidden from the player" [CHECKED L1-01:301-302] against §C.11. | GO, IN, PC, MB, SC, FI, FA, SE, NPC, WR | One of two M1 blockers (the other is interaction 2's source: J-13's remainder "unblocks R-09's by-person conjunct, hence M1" [CHECKED p5:514]), and where nine lanes' SURFACE rows land. |
| 5 | **Population that only shrinks.** The named cast is closed "for now" (ED-WR-0011 [CHECKED `registers/editorial_ledger_wr_archive.jsonl`]); "the birth-side consumer of `capacity`" — "no position builds one" [CHECKED p8:134]; hunger, ageing, illness and weather ship at the control [BASELINE B5]. A levy drawn from cohorts (interaction 1 under J-C-2 (a) or (c)) and forcing switched on (WR K-WR-9) both draw down a population with no producer. | SE, WR, NPC, MB | Decides whether the troop chain and the forcing handles leave a world that runs for more than a few seasons. |

---

## C1. LANE COMPARISON MATRIX

**Rule.** Each cell is the lane's own finding, not a new reading: *research* and *precedent* grade what the
lane's §0 and §7 judged sound; *grounding* is what its running code rests on; *code reach* is the dominant
value of its throughline table; counts are its §8.1 (MISSING · HOLLOW/BLOCKED · PLANNED-UNBUILT/BUILT-DARK),
reconciled with the digest (SC's §8.4 has 17 rows, as its §8.1 says, not the digest's 14 [CHECKED
`SC_social_contest.md:354-415`]; SE's has 19 [CHECKED]). *Outrun* ranks how far evidence reaches beyond code
(1 = furthest).

| lane | research | precedent | running code rests on | code reach | v9 reach | NERS verdict | M · H/B · P-D | top recommendation | outrun |
|---|---|---|---|---|---|---|---|---|---|
| MB | large, self-authored from memory, unverified [LANE MB §0 #5] | moderate (13G, 20G) | cited constants; Jordan values | harness depth built-inert; one `Line` executes | IN-13; IN-52 (opposite); MB-07r J; MB-08 LEAVE | R-CHOICE, R-VARIETY, E-LEGIBILITY fail on the season path | 17 · 5 · 11 | K-MB-1 troop stock | 1 |
| SC | vendored study reaches the design; RHET unreached | excluded by scope ruling | the study's gate half; rulings | `tell` executes; gate hand-built only | SC-01..08; SC-05/06 HELD | a shape on four objects, not yet a game | 9 · 9 · 17 | K-SC-1 a case names its game | 2 |
| PC | thin: one unverified HEMA run | null for the bout | cited constants; rulings | depth executes; every season fight two default fighters | PC-10 B-Y; PC-06 B-S; PC-08 LEAVE | `fight` holds narrowed; actor's felling unwritten | 9 · 3 · 8 | K-PC-1 combat inputs | 3 |
| SE | written for a retired target [LANE SE §0 #1] | teardown in hand, partly contradicted [UPLOAD_CHECKS] | Layer 1 axioms; rulings | larder, wear, `transfer` execute; `levy`, `found`, `build`, `work` refused | IN-07, IN-28, IN-45, IN-49, SE-03/04/06 | scarcity never observed; S-DOWN fails today | 8 · 5 · 19 | K-SE-13 troop stock | 4 |
| FA | unauditable; Key-idiom hooks | judged against a retired driver | Layer 1; rulings | `dispatch` writes nothing; `head()`, `at_war` inert | B-X; IN-27; IN-30; IN-36; FA-07 LEAVE | "the code holds the discipline; canon does not" | 5 · 6 · 18 | K-FA-13 faction levies and composes | 5 |
| NPC | one weak file (RTP) | degrades downstream | rulings; measurements | ledger and pursuit cells execute; capacity, values, body dark | B-X; IN-61; IN-48 | "small because capacity and change were amputated" | 12 · 10 · 14 | K-NPC-1 one capacity source | 6 |
| WR | catalogue reaches no code | none for magic | its own metaphysics | threadwork runs only in its tests; forcing dark | IN-35, IN-06, WR-01, IN-37, IN-27 | Calamity implementable as wear only | 8 · 6 · 8 | K-WR-2 thread acts as verbs | 7 |
| FI | none historical | unattributed, self-graded | its own archived prose | six rows execute content-free | FI-01/02 B-O; FI-03 B-S | executes, yields nothing | 7 · 7 · 15 | K-FI-6 inquiry yield | 8 |
| IN | excluded by Layer 1's rule; 0 of 45 rows GROUNDED | weaker than its verdicts | Layer 1; measurement | loop executes; 17 of 45 verbs in the corpus pin | most positions | four false N-lines; S-UP fails | 14 · 10 · 30 | K-IN-1 capacity source | 9 |
| GO | none | almost none | engine reference; own audits | six constants bridged; parity Python-only | GO-01/05/06, PC-05 in B-Z | the shell is expressible, not implementable | 10 · 4 · 9 | K-GO-1 integer hash | 10 |
| **total** | | | | | | | **99 · 65 · 149** | | |

The ranking inverts code maturity: MB and SC hold the most cited evidence and the deepest built modules and
deliver least of it to the season; IN and GO hold almost no evidence and the most running code. The lanes
furthest ahead (MB, SE, FA) had already named an army levied from settlements (T-MB-5, T-SE-4, T-FA-16),
which the plan declined and Jordan's statements now demand; whether that army is costed in population the
statements leave open (J-C-2).

---

## C2. SHARED ROOT CAUSES

A cause enters when three or more lanes file different rows for it and one sentence explains them all.

| id | cause | rows covered, by lane | agree on code and plan? | NERS |
|---|---|---|---|---|
| RC-1 | **No per-person source of capacity:** no ruled source exists (J-13 remainder; K-2 "not ratified"), so each resolver reads a fixture default. | PC M-PC-1, M-PC-9, T-PC-9 · MB M-MB-3, M-MB-16, T-MB-15 · SC 8.3-a, M-SC-8, T-SC-2 · NPC M-NPC-1, -2, -13, H-NPC-1, B-NPC-4 · IN M-IN-1, M-IN-7, H-IN-2, H-IN-4, T-IN-1 · FI M-FI-3, T-FI-7 · WR authored `ts:` unread · GO M-GO-7 | Agree it is absent. Disagree on the carrier: new `Person.attributes` (audit G1; PC; GO) or existing `Person.capability` derived at read (NPC); Jordan's "it will be 10 attributes" (ED-IN-0185 Q7 [CHECKED p5:515]) decides toward the first (C4 X-14). FI also needs the actor's reading of his own act, from which the witness exempts him [CHECKED `loop/witness.py:490-497`]; IN calls that optional [LANE IN M-IN-7]. | R-VARIETY; S vertical |
| RC-2 | **No troop stock, and a misnamed levy:** the season force is summed `Person.weight` because troops have no carrier, and the verb named for raising them moves stores. | MB M-MB-1, -2, -6, -15, -16, -17, IN-52(H), T-MB-5, -19 · SE M-SE-9, H-SE-1, T-SE-4 · FA M-FA-10, T-FA-16 · NPC M-NPC-13 · IN M-IN-12, -13, H-IN-10, T-IN-14 · PC M-PC-12 | Agree on code and plan. Disagree on form, three ways: a rung stock coupled to population (MB K-MB-1: "a count per troop kind held on the rung", filled by moving headcount out of cohort `weight` [CHECKED `MB_mass_battle.md:715`]); a rung stock uncoupled from population (SE K-SE-13's first shape, a `matter_kinds` row "never a person"); troops as people, cohort weight committed to a faction (SE K-SE-13's second shape [CHECKED `SE_settlements_territory_economy.md:492`]; FA K-FA-13, "the population is the soldiery" [CHECKED `FA_faction_actions.md:571`]). SE, FA and IN K-IN-13 leave the choice to Jordan (C7 J-C-2). | R-CHOICE; R-VARIETY; S vertical |
| RC-3 | **Knowledge only by claim, with no deposit occasion:** AX-2 makes a claim the only route to knowing, and several facts a person must act on are never deposited. | SE M-SE-3 (H-195 holder) · PC M-PC-8, WR M-WR-9, NPC M-NPC-6 (H-206 vacancy) · SC M-SC-4, IN M-IN-8 (H-180, H-181) · NPC M-NPC-9 (H-191) · FA M-FA-4 · SC M-SC-7, IN M-IN-14, FI M-FI-2 (no claim can be held False) | Agree: H-195 and H-191 have zero plan mentions, H-206 one [CHECKED grep]. NPC dropped H-180, H-181, H-195 as covered elsewhere; a placement difference only. | S-DOWN; R-WORLD |
| RC-4 | **Acts carry no content:** verb rows record an event kind, not a predicate, and the instruments count the event, so content-free execution passes every exit. | FI M-FI-1, M-FI-6, FI-01 ×4(H), T-FI-1, -6 · WR T-WR-4, IN-37(H) · IN M-IN-9, T-IN-4 · SC M-SC-1, M-SC-5 · FA M-FA-1, T-FA-12 · NPC M-NPC-4, T-NPC-13 · PC M-PC-10 | Agree. FI counts six inquiry rows writing nothing, the audit "five investigation verbs" [AUDIT 498]: a scope difference (`thread_read`). | R-COMPLETE; N bottom-up |
| RC-5 | **No surface and no pause:** IN-46 and IN-47 have no build batch, and §C.11's `explain` has no position. | GO M-GO-4..-7, -9 · IN M-IN-2, -3, H-IN-3 · PC M-PC-4, -6 · MB M-MB-5, -10, IN-46(B) · SC M-SC-9 · FI M-FI-5 · FA M-FA-4 · NPC M-NPC-7 · WR chronicle | Agree on absence; disagree on what may be shown (C4 X-16). PC withdrew its odds surface (K-PC-11). | E-LEGIBILITY; S pause |
| RC-6 | **No births or growth:** the closed cast and the missing birth-side consumer leave every population carrier written only downward, and those writers ship dark. | SE M-SE-1, H-SE-3, T-SE-9, -10 · NPC M-NPC-3, T-NPC-5 · WR M-WR-8, T-WR-8 · IN §8.4-21, -25 · MB M-MB-14 | NPC dropped "births and new persons"; SE files births STRONG on RR-2. Different objects: new named persons against a cohort's weight (C4 X-4). | R-WORLD; R-COMPLETE |
| RC-7 | **War, endings, the top seat:** strategic outcomes are person-level Propositions with no producer for the mood that would start them, and GD-1 and GD-2 were never re-expressed after Layer 1. | FA M-FA-1, -3, IN-27(H), covenant(H), IN-30(H), FA-01 flip(H) · WR M-WR-6, IN-27(H) · MB M-MB-7, -8, -12 · SE H-SE-2, M-SE-4, M-SE-7 | Agree `at_war` has no game reader [CHECKED grep: definition and docstrings only]. Disagree on GD-2 (missing or struck) and GD-1's thresholds (C4 X-8, X-9). | R-WORLD; S lateral |
| RC-8 | **Offices not made or emptied by persons:** the chooser has no motive that produces `revoke` or `establish` (for `revoke`, by Jordan's ruling: H-207 (A), 2026-10-12, "a computed `revoke` is NOT driven" [CHECKED `engine/season/hole_register.yaml:4451`]), and delegation was reverted against Layer 1 §E.2.4. | IN M-IN-4, -5, H-IN-5, -7, -11 · FA IN-61(B), M-FA-2 · NPC B-NPC-1, -5, H-NPC-2 · SC 8.3-f · SE delegation | Same reading, different classes: IN MISSING, NPC BLOCKED, FA and SE PLANNED (IN-48, batch "unscheduled"). C7 J-C-10. | R-WORLD; R-CHOICE |
| RC-9 | **One ladder, several roads:** combat draws a continuous Normal with a logistic side-channel where the season, contest and field use discrete dice, and the field grades on its own three bands. | PC M-PC-7, T-PC-13 · MB M-MB-11 · IN T-IN-2 · GO M-GO-10 | Agree [AUDIT A3]; IN extends: odds non-monotone to c = 6, latent while capability is empty [LANE IN §9.1]. | S methodology |
| RC-10 | **Hash parity:** `content_hash` folds `repr()` and floats and draws come from CPython `random.Random`, where Layer 1 asks for the oracle's hash "in the integer domain" [CHECKED L1-04:1119]. | GO M-GO-1, -2, -3, -10, T-GO-3 · IN T-IN-2 · PC T-PC-13 | Agree on code; disagree on the contract (Layer 1 hash against the PROPOSED strategy's statistics). | S methodology |
| RC-11 | **Inert-at-ship controls:** a carrier ships at its control arm and no position owns the flip. | IN T-IN-3, §8.4-21..30 · NPC M-NPC-3, T-NPC-3, -5 · SE T-SE-9 · WR T-WR-8 · PC §8.4-d, f, g · MB loyalty→morale, `MB_SUPPORT_RANK_CAP` · FA T-FA-5 · SC `bench_quorum`, D-6/D-7 | Agree (BASELINE B5: 18 knobs). Disagree on repair: arm (WR), delete (IN, SC), arm or delete each (NPC). | R-WORLD; E-OVERHEAD |

**Order.** RC-1 and RC-2 are the two unruled sources; RC-4 is their consequence at the act (nothing personal
goes in, little is recorded); RC-3 and RC-5 are the same gap at the reader; RC-6..RC-8 are the world's motion
without producers; RC-9..RC-11 are methodology every other cause inherits. This matches the audit's causal
order [AUDIT 413-415] and adds RC-2, which post-dates it.

---

## C3. INTERACTION MAP

### C3 (a) Dependencies: X needs Y first

| id | X | needs first | reason |
|---|---|---|---|
| D-1 | composite army (MB M-MB-2, -17; FA M-FA-10) | troop stock by kind (K-MB-1, K-SE-13, K-IN-13) | `build_army` takes a count per subunit spec |
| D-2 | troop stock | J-C-2 (its form); J-C-1 only for the name of the act that raises it | the `levy` row writes `Rung.stores` [CHECKED vt:629-653]; five lanes file three carrier forms (C2 RC-2) |
| D-3 | the stock in the plan | IN-49 and IN-52 re-stated; IN-52's premise "`levy` moves stores, not troops" withdrawn | statement 5 contradicts that premise only; LF-1's ration bound re-applies to the stock (MB K-MB-6) unless a decision cuts it (X-19); LF-2 and LF-3 (the defender's nearest rung; `_eff_march`'s ration debit) are contradicted by no statement [CHECKED p4:137; p5:533] |
| D-4 | commander quality (MB M-MB-3; NPC M-NPC-13) | RC-1's source | `Officer` derives command from figures no person carries |
| D-5 | troop experience (K-MB-3) | the stock and fought fields (IN-13) | no realm field is fought (H-150) |
| D-6 | a field with any outcome but `Lost` (IN-13(H)) | a force scale (M-MB-1) | largest side 6, rout floor 80 [CHECKED `modules/mass_battle/config.py:117`] |
| D-7 | war (FA M-FA-1, K-FA-1) | a mood source for `utter`; the `attention_key` own-echo precondition | computed `utter` mints OUGHT only [LANE FA M-FA-1, req:901-904] |
| D-8 | `march` requiring war (K-MB-5) | D-7 | otherwise every inter-faction march refuses and IN-13's field is never fought |
| D-9 | insurgency forming a faction (K-FA-7; SE H-SE-2) | the own-echo precondition; IN-27 | IN-30 is BLK on IN-27 |
| D-10 | competence (K-FI-1; M-NPC-2; M-SC-8) | RC-1; for an inquiry, AX-7's layer (2) | an inquiry deposits to its actor, who is exempt [CHECKED `witness.py:490-497`] |
| D-11 | a confidently wrong finding (K-FI-7) | an inquiry yield (K-FI-6) and competence | a wrong value needs a value |
| D-12 | the concealer's score (K-FI-5) | a concealing act executing (`forge`, IN-45, BLK IN-10) | its own ladder condition |
| D-13 | a case heard under its game (K-SC-1) | IN-10's record-sourced operands | built and reverted at B-I; restorable [BASELINE B2.1] |
| D-14 | succession (IN-61) | vacancy by claim (H-206) and D-13 | IN-61 rests on the missing claim [LANE NPC M-NPC-6] |
| D-15 | a chronicle (IN-37; K-WR-11; K-NPC-11) | content in acts (RC-4); IN-47 batched | the render's input is thin [LANE WR T-WR-4] |
| D-16 | odds or a derivation shown | J-C-12 | the ruling decides what is admissible |
| D-17 | a played fight; a battle yielding to a duel; the port's seat | IN-46 batched | all extend IN-46's one call-out [CHECKED p4:34] |
| D-18 | thread acts (K-WR-2), Calamity from strain, TS seeding | a `(Person, coherence)` writer; IN-06 | K-3 types `thread_read` but names no writer |
| D-19 | forcing on (K-WR-9) | authored ages (M-WR-8); J-C-9 | `age_at_build` is 0; forcing alone only shrinks the realm |
| D-20 | a priced store act (K-SE-5) | `body_step` > 0 (J-6) | the price is the hunger left |
| D-21 | the taxed person's answer (K-FA-5) | IN-09 restored; the store act executing | `evade / defy` has no effect [LANE FA M-FA-5] |
| D-22 | terms of taking a place (K-SE-9) | `seize`; `held_by` claims (K-SE-2) | its falsifier reads stance toward a known holder |
| D-23 | hostility aimed at a place; IN-70 | `held_by` claims | `stance_term` reads a rung, not its holder (H-195) |
| D-24 | R-04 conjunct (3), hence M1 | IN-46, IN-47 batched; FA-01, IN-07, FI-01, SC-01 rows `in_loop` | [CHECKED p4:36; BASELINE B2] |
| D-25 | co-location for lethal acts (K-NPC-12; IN-59) | heads housed at their seats | five of six heads live off-seat [LANE NPC H-NPC-5] |
| D-26 | any person-varying pool (RC-1) | a monotone odds rule (K-IN-5) | the sawtooth is latent only while capability is empty |

### C3 (b) Collisions: one object, incompatible proposals

| id | object | side A | side B | the incompatibility |
|---|---|---|---|---|
| X-1 | chooser's `urgency` | IN K-IN-2: delete | v9 IN-62: `score_terms -> (pursuit, stance, urgency)`, "hash EQUAL" [CHECKED p5:255] | IN-62 keeps the slot K-IN-2 removes |
| X-2 | troops' carrier | a rung stock: MB K-MB-1 (per-kind count on the rung, coupled to population by lowering cohort weight); SE K-SE-13's `matter_kinds` shape (uncoupled) | troops as people: FA K-FA-13 (cohort weight into the muster; a weight writer); SE K-SE-13's second shape. IN K-IN-13 leaves all open; PC K-PC-12 (refuse cohort fights) binds every form | a coupled stock or persons make casualties population losses; an uncoupled stock does not |
| X-3 | a felled actor | PC K-PC-2: write it, on `march`'s precedent | `_eff_march` writes "ON THE LOSING SIDE ONLY ... silent on the winner" [CHECKED `loop/effects_combat.py:178-183`] | none for the felled actor; a standing winner's wounds unruled |
| X-4 | population over time | WR K-WR-9 (forcing on); MB K-MB-1, FA K-FA-13 (levies) | SE K-SE-1 (growth or fixed); ED-WR-0011 (cast "only shrinks") | three lanes write population down, one up, behind a ruling; a cohort's death is final [AUDIT A6] |
| X-5 | suspension sites | GO K-GO-3 (DELIBERATE, duel yield); MB K-MB-10, IN K-IN-6 (inside the 18-tick call) | IN-46: suspends at ENCOUNTER "and only at the engine call" [CHECKED p4:34] | each extends IN-46 beyond its design |
| X-6 | the closed `requires` grammar | FI: do not widen; "each added read is a refusal condition"; forms closed at seven; K-FI-6's Sites half needs an eighth [CHECKED `FI_fieldwork_investigation.md:374, :455-462`] | MB K-MB-5, FA K-FA-1, PC K-PC-12, NPC K-NPC-12 add conjuncts | not opposed in intent (those lanes want refusal), but one grammar; F.33 leaves `at_war` in a `requires` open |
| X-7 | the act war gates | MB K-MB-5: `march` | FA K-FA-1: `fight` | two acts for one gate |
| X-8 | GD-2 | MB M-MB-12, WR M-WR-6: MISSING | FA K-FA-6, IN K-IN-12: strike; WR K-WR-12: duty or retire | missing area against deletion |
| X-9 | GD-1 | FA K-FA-6: Query over seats; strike Accord and Stability | WR K-WR-10: stability from a seat-holder's estimate; Accord carried or dropped | strike against re-express; 15 or 17 territories [LANE SE §8.4] |
| X-10 | what Mending is | WR K-WR-3: the thread Mend; `restore` is fabric | v9 IN-35: "Mending as persons' acts (the `restore` arm)" [LANE WR §0 #9] | one verb for two acts |
| X-11 | the top seat | FA K-FA-3: offer resignation; replacement Jordan's | 2026-10-12 duchy ruling; SC-04 "awards, never unseats" | abdication fits; replacement does not |
| X-12 | closing a petition | SC K-SC-3: `destroy_record`, or a `deny` row | A-13 (`destroy_record` unformable); A-16 "No new closer rows", which applies Layer 1 row 14, "one `release` verb, eligibility `own`, generic over kind" [CHECKED L1-04:201; p5:355] | (a) blocked; (b) overwrites ratified Layer 1, not only the plan |
| X-13 | a delegate's early end | NPC K-NPC-8's falsifier: revoking the deputy ends his acts | FA K-FA-11: early dismissal Jordan's; SE K-SE-6: term only | NPC assumes what FA leaves open |
| X-14 | the capacity carrier | audit G1, PC K-PC-1, GO K-GO-8: new `Person.attributes` | NPC K-NPC-1: no new field; `Person.capability` | new field against existing |
| X-15 | the actor's own reading | FI K-FI-1 needs it | IN M-IN-7, audit G6: permitted, not owed; NPC dropped it | needed against optional |
| X-16 | what the player sees | GO K-GO-6 (cut the gloss), K-GO-7 (odds from held claims) | IN K-IN-9 (Jordan); SC K-SC-9 (band or not); PC withdrew odds | one Layer 1 conflict, three routes |
| X-17 | investigation's seam | FI-02, K-FI-9: its own role (SM-3) | FI-01 pins `modules/social_contest/roll.py`; K-FI-3 routes testimony through `tell` [LANE FI X] | own seam against the contest's roller and verb |
| X-18 | the dedup filter | audit G4: delete; §C.3 forbids it; Jordan's only if R-03 goes red [CHECKED `references/ners_audit_2026-10-14.md:433`] | IN K-IN-3: §C.2 against §C.3, plus a measured monoculture [LANE IN §10.7] | a conditional cut against a Layer 1 conflict |
| X-19 | IN-52's ration bound (LF-1) once troops are a stock | MB K-MB-6 (C8 R-C-25): bound fielded troops by the smaller of stock and ration; only LF-1's "does not create troops" half falls; LF-3 unchanged [CHECKED `MB_mass_battle.md:732`] | SE K-SE-13: cut "IN-52's stores-bound-troops feed (LF-1, and the `field_provisioning` arm with it)" [CHECKED `SE_settlements_territory_economy.md:492`] | keep the bound and re-point its input, against cut the bound and its arm |

### C3 (c) Amplifications

| id | fix | effect elsewhere | direction |
|---|---|---|---|
| AM-1 | capacity source (R-C-1) | wakes the sawtooth (D-26); makes PC's "no chooser term reads odds" live ("a defect once K-1 lands" [LANE PC §9 C3]); a varying pool nobody can see (RC-5) | bites |
| AM-2 | troop stock (R-C-2) | eases M-MB-1 and IN-13; under J-C-2 (a) or (c), makes M-SE-1 bite (a levy drains a population with no producer) | both |
| AM-3 | forcing on (R-C-32) | more deaths with H-206 open: vacancies nobody learns of; "five of six heads die in two seasons" already [LANE NPC B-NPC-1] | bites |
| AM-4 | a case names its game (R-C-17) | eases IN-61's tribunal and FI T-FI-3 (inquiry lands on proceedings) | eases |
| AM-5 | inquiry yield (R-C-23) | eases IN-37's thin input and SC-02's "investigation products" | eases |
| AM-6 | war utterable (R-C-12) | makes M-MB-1 and M-MB-14 bite: wars fought by 4/4 Lines that always lose and never kill | bites |
| AM-7 | co-location (R-C-13) | makes H-NPC-5 bite: the gate's premise is wrong in data | bites |
| AM-8 | store act renamed (R-C-10) | eases SE H-SE-1, IN M-IN-13 | eases |
| AM-9 | `held_by` claims (R-C-6) | eases war targeting, IN-70, terms of taking (R-C-33) | eases |
| AM-10 | dark person knobs armed (R-C-32) | values change unwatched with no surface (T-NPC-8) | bites |
| AM-11 | thread acts (R-C-18) | free self-Mending becomes strictly dominant at a playable seat (T-WR-9) | bites |
| AM-12 | integer hash, fixed-point draws (R-C-4, R-C-5) | goldens move once; every later hash-moving repair moves them again | ordering cost |

### C3 (d) Dependency order (C8 ids)

| layer | contents |
|---|---|
| L0 rulings | J-C-1, J-C-2, J-C-3, J-C-9, J-C-12 first; the rest as dependants arrive |
| L1 cuts and owners, no ruling | R-C-8, R-C-3 (owner half), R-C-4, R-C-5 |
| L2 carriers | R-C-1, R-C-2, R-C-6, R-C-7, R-C-9, R-C-29 |
| L3 verbs | R-C-10..R-C-22 |
| L4 mechanics, texture | R-C-23..R-C-28, R-C-30..R-C-36 |
| L5 surface | R-C-37..R-C-39 (R-C-37 may start at once: its designs exist) |
| L6 apparatus | R-C-40 |

---

## C4. RECONCILIATION

**The rule, by precedence:** (1) Jordan's statements and rulings (the later governs on the point it decides)
> (2) ratified Layer 1 > (3) `canon/` (P-01..P-15 and the GD constraints; below Layer 1 because Layer 1, ratified
later, admits nothing "under `canon/`, `systems/` or `research/`" as authority over it [CHECKED L1-01:1173-1175])
> (4) the v9 plan's recorded state (an entry over an index row where the plan contradicts itself) > (5)
measured behaviour in the tree > (6) proposals > (7) research, tier 3 (`engine/season/rosters.yaml:75-90`
[CHECKED]). "[ASSUMPTION; Jordan to correct]" keeps a plan answer at (4) but revertible alone (p8:193). A
Jordan ruling that adopts a document (as "adopt in full" adopts Layer 1) gives that document its own rank,
not (1); otherwise rank (2) would be empty. C6's demand ladder (D1..D6) grades how strongly an area is asked
for, not which source wins a conflict. Where nothing decides, the item goes to C7.

### C4.1 Collisions and disagreements

| item | rank | favours | why | C7 |
|---|---|---|---|---|
| X-1 `urgency` | (4) | IN-62 first, then K-IN-2 | a sequence: IN's §10.7 calls the slot loss "real but small" | — |
| X-2 troops' carrier | (1), partly | troops a resource distinct from goods, raised by the troop verb | statement 1: "troops levied from settlements as their own resource"; statement 5: `levy` is wrong for goods. "Their own resource" reads toward a rung-held carrier but decides neither that nor whether raising troops lowers cohort weight: all three forms stay open | J-C-2 |
| X-3 felled actor | (1) | PC | Jordan 2026-09-04, "your code just has to accept the result" [LANE PC M-PC-2]; ED-IN-0279 silent on the winner | J-C-4 |
| X-4 population | (1) | no new named persons; cohort weight may grow | ED-WR-0011 closes the NAMED cast "for now"; it does not reach a cohort's `weight`. Decide before forcing (D-19) | J-C-9 |
| X-5 suspension sites | (2), weakly | GO, as a specification latent until step 12 | "for a player character the player IS the decision procedure" [CHECKED L1-04:844-846] sits inside §C.11, the explanation contract, and specifies no pause; the hazard exists only once step 12 pools the map, and step 12 is unbuilt, "beside — an optimisation" [CHECKED L1-04:1118]; IN-47's development space already acts "into the chooser slot" [CHECKED p4:41]. GO's own row: "a specification, not a missing mechanism" [CHECKED `GO_godot_port.md:250`]. The battle's internal yield: nothing decides which acts interrupt | J-C-20 |
| X-6 `requires` grammar | (5) | conjuncts within the seven forms takeable; an eighth form Jordan's | forms closed, "a design change, not a table edit" [LANE FI §9 C3] | J-C-15 |
| X-7 war's gate | none | — | F.33 open | J-C-15 |
| X-8 GD-2 | (2) over (3) | the faction-level mandatory pass is superseded | Layer 1's AX-1 (only persons act) outranks canon's GD-2 (`canon/04_game_design_constraints.md:28` [CHECKED]: "Faction action-selection … runs a mandatory-actions pass") on the actor; not Jordan against Jordan. A holder's duty is undecided, and M-MB-12, M-WR-6 stay MISSING only under it | J-C-14 |
| X-9 GD-1 | (2) over (3), partly; (4) | an ending as a Query over persons' seats | IN-27 schedules one; an omniscient evaluator is "acceptable only as presentation" [LANE FA §9 C3]; the thresholds are a canon edit | J-C-13 |
| X-10 Mending | (4), then sequence | IN-35 today; WR once a thread Mend exists | both readings are tagged assumptions; the roster declines only "until a Mending can be told from mending a wall"; R-C-18 makes that distinction | — |
| X-11 top seat | (1) | abdication yes, replacement no | the 2026-10-12 ruling bars stripping; resigning by one's own `release` is not stripping | J-C-5 |
| X-12 petition | (1), then (2) | the closer is owed; its form must keep Layer 1 row 14 | ED-IN-0210 Ruling 2 names WITHDRAW and DENY [CHECKED `registers/archive/editorial_ledger_in_archive_pre-2026-09.yaml:2312-2316`], so a closer is owed; A-16 applies Layer 1 row 14, one generic `release` [CHECKED L1-04:201; p5:355], so a `deny` row overwrites ratified Layer 1. The address needs no new row. Which closer (`destroy_record`, or the holder's generic `release`) is open | J-C-7 |
| X-13 early dismissal | none | — | H-207 (A) and IN-31's ban cover neither a same-rung deputy | J-C-17 |
| X-14 capacity carrier | (1) | an attribute carrier of ten (audit G1, PC K-PC-1, GO K-GO-8); `capability` survives only as a reading derived from it | Jordan: "it will be 10 attributes" (2026-08-14 Q7, ED-IN-0185 [CHECKED p5:515; the ledger row]); v9's interim `capability` keyed by `verb_capability` (J-13 (iii), only key `copying` [CHECKED p5:514]) is not a ten-attribute carrier. Open: where the magnitudes come from (J-13's remainder) and the tenth attribute's name (J-9 D2) | J-C-3 |
| X-15 actor's own reading | (2) | not owed | AX-7 (2): self-understanding "may be wrong", a permission | J-C-3 |
| X-16 what is shown | (2) against (2) | — | the gloss and §C.11 conflict; decided regardless: `explain` takes no `World`, so shown odds are the actor's estimate [LANE GO §9 C2] | J-C-12 |
| X-17 investigation's seam | (1) | FI | SM-3 (P6:266) outranks the carried v8 line [LANE FI K-FI-9]; sharing the one roller is RC-9's single owner, not a seam | — |
| X-18 dedup filter | (2) against (2) | — | §C.2 and §C.3 conflict | J-C-16 |
| X-19 IN-52's ration bound | (4) | MB K-MB-6 (R-C-25): the bound stays, its input becomes the stock | LF-1 is a delegated plan answer, revertible by Jordan alone (p8:193); statement 5 withdraws only IN-52's premise that `levy` moves stores, and no statement reaches the ration bound, so SE's cut has no rank above (6) | — |
| `restore` executes? | (5) | refused | SE's run: 25 refused, 0 executed over two seasons [LANE SE §9]; `req:163-166` is stale | — |
| `march` in the realm | (5), not run | unreconciled | `req:675` "16/16" against `req:1124` "all 11 refused"; needs `aperture 4 0`; p2:178 [UNVERIFIED] | — (C9) |
| inquiry rows writing nothing | (5) | both | six rows (BASELINE B3); five if `thread_read` is threadwork | — |
| IN-14's state | (4), entry over index | the entry (B, B-J, MORE ROUNDS) | [CHECKED p4:25-27]; FA and IN both flagged it | — |
| delegation's class | definitional | — | IN-48 is STATE B in an "unscheduled" batch | J-C-10 |
| parity contract | (2) over (6) | hash equality in the integer domain | [CHECKED L1-04:1119]; GO itself takes the hash [LANE GO §9.5] | J-C-11 (version) |
| thread History term (audit G7) | (5); §0.05 | WR: a ruling | code reads `min(3, history + 3)` [CHECKED `systems/threadwork/sim/operations.py:246`]; the alternative rests on a comment and PP-624 has no `registers/` row [LANE WR §8.4] | J-C-23 |
| one substrate (audit G2d) | (1) | PC: a ruling | combat is exempt from the ladder's bands by ruling (T-PC-13); the choice moves every combat balance figure | J-C-18 |

### C4.2 The lanes against the uploaded NERS audit

Tested by IN's §10.7 (each item re-opened at `5445e34` [CHECKED `IN_infrastructure.md:1023-1052`]) for A2-A5,
A9, T3-T6, G1-G9, X1-X8, and by the other lanes' own cites for A1, A6-A8, T1, T2, R-WORLD. The audit assumed
v9 built; an unbuilt-but-planned row does not contradict it.

| audit | lanes' verdict | relation | cites |
|---|---|---|---|
| A1/T1 per-person difference | holds; reaches commanders, troops, competence, creation | agree, extend | MB M-MB-3; NPC M-NPC-13; FI M-FI-3; GO M-GO-7 |
| A2 callback player; gloss; dead path; empty hooks | holds | agree, extend (DELIBERATE pause; mass→personal; thread→mass) | IN §10.7; GO M-GO-4; MB M-MB-4; WR M-WR-3 |
| A3/T3 one ladder, several roads | holds; sawtooth to c = 6 | agree, extend | IN §9.1; PC M-PC-7; MB M-MB-11 |
| A4 (i)-(iv) inert terms, dark knobs | holds | agree | IN §10.7; NPC M-NPC-3 |
| A4 (v) no term reads odds, cost, capability | not a missing area | **diverge** (a defect once capacity lands, AM-1) | IN §8.5; NPC §8.5; PC §9 C3 |
| A4 datum (439 of 1,318) | not re-run | unverified | G9 unrun |
| A5 (a) dedup vs §C.3 | §C.2 against §C.3 | **diverge** in form | IN §10.7 |
| A5 S-UP petition | holds | agree | SC M-SC-2 |
| A5 R-CHOICE `levy` | holds, on the misnamed store act | **re-labelled** (statement 5) | IN M-IN-13; SE H-SE-1 |
| A6 `doc: null`; governance verbs; no births | holds | agree, extend (labour, exchange, adjacency) | SE M-SE-1, -2, -4, -5 |
| A7/T2 force unresolvable | holds | agree; **repair relocated** (the conversion moves from `_weighted_unit` to the levy) | MB M-MB-15; IN §10.7 G3 |
| A8 history term; post-crossing; free Mending; empty inquiries | holds; cost 0 at 16 cells, executed | agree, extend | WR M-WR-2, -4, -7; FI M-FI-1 |
| A9 AX-7 falsifier by its letter | holds; sites moved | agree, extend (X-15) | IN §10.7 |
| R-WORLD | holds | agree, extend (ages unauthored; drought stays in surplus) | WR M-WR-8; SE §9 |
| T2, T4, T5, T6 | hold (T2 narrowed; T5 one seed; T6 now 88,377 lines) | agree | MB T-MB-2; IN T-IN-3, -4, §10.7 |
| G1 capacity source | survives | agree; carrier decided toward attributes by ED-IN-0185 Q7 | X-14 |
| G2a, G2b, G2c (Jordan) | survive | agree | K-IN-5; K-MB-7; K-MB-8 |
| G2d one substrate, agent | Jordan | **diverge** | K-PC-8 |
| G3 weight→troop conversion | its site moves: K-MB-1 still needs "the men-per-weight scale `[OPEN — Jordan tuning]`" [CHECKED `MB_mass_battle.md:715`], applied at the levy instead of at `_weighted_unit` [CHECKED `references/ners_audit_2026-10-14.md:432`] | **relocated** | IN §10.7; K-MB-1 |
| G4 delete dedup | not a free cut | **narrowed**: the audit already routed a red R-03 to Jordan [CHECKED `references/ners_audit_2026-10-14.md:433`]; the lanes add the §C.2 conflict and a measured monoculture | K-IN-3 |
| G5 delete `urgency`, `benefits_me` | survives, after IN-62; ED-IN-0261 Jordan's | agree | K-IN-2; M-NPC-12 |
| G6 AX-7 sites; gloss | sites survive; gloss Jordan's | partly diverge | K-IN-9; K-GO-6 |
| G7 history term, agent | a ruling | **diverge** | K-WR-7 |
| G8 head rows | survives; one head sits in `.audit/`, outside `CURRENT.md:13`'s caveat | agree, extend | WR §0 #1 |
| G9; X1-X7; X8 | survive; X8 precondition unverified | agree | IN §10.7 |

**Overturned by the lanes:** G7 and G2d (ladder results), A4 (v) (as a missing area). **Relocated or
narrowed:** G3 (the conversion moves to the levy), G4 (the audit's own R-03 escalation, widened to a Layer 1
conflict), A5's `levy` finding (re-labelled). **Extended past the audit:** the troop chain, the DELIBERATE
pause (a specification, latent until step 12), labour, adjacency, authored ages, the actor's own reading.

---

## C5. CROSS-LANE EVIDENCE

### C5.1 Convergence, nulls and misapplied precedent

| pattern | lanes | independent? |
|---|---|---|
| persons differ in wants, not capacities | IN T-IN-1, PC T-PC-9, MB T-MB-15, SC T-SC-2, NPC T-NPC-4, FI T-FI-7 | **no**: one measurement (req:1244-1247) relayed six times — redundancy, not corroboration (CLAUDE.md §10) |
| built ahead of readers; controls shipped off | IN T-IN-3, NPC T-NPC-3/-5, SE T-SE-9, WR T-WR-8, FA T-FA-5, PC T-PC-7, GO T-GO-2 | **yes**: different knobs opened by each lane |
| a levy takes people, and their labour and future | MB T-MB-5, SE T-SE-4, IN T-IN-14, FA T-FA-16 | **yes**: history (FASE) and precedent (20G A3, Proposal F) agree; Jordan's statements agree that a levy raises troops, not goods, and leave its population cost open (J-C-2); the plan's premise is the outlier |
| acts record that, not what | IN T-IN-4, FI T-FI-1, NPC T-NPC-13, WR T-WR-4 | partly: rows independent; the 52-of-52 datum is one seed |
| one resolver, several fidelities | MB T-MB-3, PC T-PC-8, IN T-IN-5 | no: one precedent (Total War auto-resolve) |
| **null:** no precedent for the hand-off above the bout | MB T-MB-4, PC T-PC-15, IN T-IN-7 | sound; the built `Command=0` rout breaks the borrowed fraction rule [LANE MB §0 #8] |
| **null:** shape transfers, magnitude does not | FA T-FA-14, IN T-IN-8, MB §0 #3, PC T-PC-4, WR T-WR-6 | sound everywhere: every value is a fixture or `[OPEN — Jordan tuning]` |
| **null contradicted:** no NPC acts on knowingly false information (N-9) | FI T-FI-10, NPC T-NPC-15, IN T-IN-13 | all three contradict it: The Guild 2's fabricated evidence and slander (TD:191) |
| **null split:** allegiance never arrives late | IN T-IN-12, NPC T-NPC-2 (sound); FA T-FA-9 (over-claimed); SE T-SE-7 (unverified) | adjudicated: "recomputed instantly" over-claims (Tropico's diffusion, Guild 2's evidence, 20G A9); "no title schedules a lag on allegiance" holds inside the twenty (20G empty cell 3) |

| precedent | applied correctly | applied incorrectly |
|---|---|---|
| failure shape A (a mechanism tuned never to fire is absent) | MB T-MB-13 (`Won`); FA T-FA-5 (`head()`, `at_war`, `uncontrolled`, `levy`) | — |
| The Guild 3's agent layer switched off (TD:195, T1) | FA T-FA-5; NPC T-NPC-3; PC T-PC-7 | VCD's "at a popularity threshold" (relayed by IN, NPC) is not in the teardown [UPLOAD_CHECKS] |
| 20G A5, "specify the half-strength setting" | NPC T-NPC-3 | none, but all miss that the knobs HAVE intermediate arms (`scar_weight_shift` 0.5 / 1, BASELINE B5): half-strength exists in code, unchosen in data |
| Banished | SE: capacity gates births (TD:284) | SFP's "food-limited attrition" CONTRADICTED (TD:21); Tropico's causation inverted [UPLOAD_CHECKS] |
| du Picq | — | MB: the 15-30 % rout band is a Jordan value (ED-MB-0031) credited to du Picq [LANE MB §0 #7] |
| survey counts | — | COMP "six of eight" contradicted by its own table [LANE IN §7]; 13G counts inflated [LANE NPC §0 #8] |

**Tiers reaching code.** Across the ten lanes the one research finding with a code-read owner is H-100 (seat
provenance prices revocation), and its owner IN-31 keys cost on a different variable [LANE NPC H-NPC-2].
Historical research otherwise reaches code comments (MB, PC), one shipped-dark name (SE, Sen) or nothing (FA,
WR, FI, IN, GO); game precedent reaches `forgive` through VCD (NPC), IN-37 as an observer (WR) and nothing
else; two research-derived rosters were built and deleted unread (`rosters.yaml:86-90` [CHECKED]). Research
reaches the game by vocabulary, never magnitude (T-IN-8).

### C5.2 The Twenty Games frame against the lanes

**Corpus bound (the document's own):** twenty titles; Dwarf Fortress, RimWorld, the Victoria series,
Frostpunk and Old World unexamined; every empty-cell and novelty claim inherits it [CHECKED 20G:148, :446, :462].

| 20G axis | Valoria's own cell | empty in Valoria's design? |
|---|---|---|
| 1 population resolution | 46 named persons plus cohorts as one Person at `weight` (37) [CHECKED p5:517, J.2 row 4] | no, but cohorts never change size (RC-6) |
| 2 named-agent cardinality | 46, closed "for now" | no |
| 3 contested object | seats and allegiance; land (occupation planned, IN-13) | **labour and time empty** (SE M-SE-5; no ending) |
| 4 player position | embedded: the player is one person's decision procedure [CHECKED L1-04:844-846] | no |
| 5 control channel | rung 1; rung 3 (delegate) reverted; rung 4 (lobby a body) partly built, a court, not a vote: computed `open_case` and `determine` execute and dispose `oblige` [CHECKED `SC_social_contest.md:370`], the vote over commitments is blocked on J-4 [CHECKED `SC_social_contest.md:388`]; rung 2 (zone) absent | **2 and 3 empty today, 4 partly; 2 empty planned** |
| 6 coupling latency | belief carried by telling (4 of 1,270 claims [LANE NPC T-NPC-2]); scars accrue | **lagged cohort empty** |
| 7 durability | persistent, no ending (H-176) | ending empty until IN-27 |
| clock count; legibility | two clocks, auto-resolve only (T-MB-12); no legibility strategy | the second clock buys nothing a player touches (20G directive 6); **legibility empty** |

20G's four empty cells against Valoria: cell 1 (fine populace × scarce named agents) occupied in structure,
not in loop (no steward over a populace); cell 2 (labour contested between players) empty; cell 3 (lagged
allegiance) crossed in shape, thin in delivery; cell 4 (zone and delegate together) empty.

| 20G asymmetry | Valoria | lanes |
|---|---|---|
| A1 allegiance with a delay | **crossed in shape** (telling, regard at read); loyalty seed static | NPC T-NPC-1, -2; IN T-IN-12 |
| A2 zone plus delegate | **not crossed** | IN M-IN-5; NPC M-NPC-11; FA T-FA-15 |
| A3 conscription removes a cohort | **not crossed, refused by v9** (IN-52's premise; LF-1's "does not create troops" half); statements 1 and 5 withdraw that premise but leave A3's cell, a levy that removes a cohort, open (J-C-2); Proposal F ("The Levy", B+) needs births for its lag | MB M-MB-15; SE M-SE-9; FA M-FA-10; IN M-IN-12 |
| A4 relational victory | **partly** (IN-27's Query over seats; GD-1 unresolved) | FA T-FA-4, K-FA-6 |
| A5 graduated agent layer | **crossed in mechanism, not in data** | NPC T-NPC-3; IN T-IN-3 |
| A6 ephemerality with carry-over | not applicable (persistent); unaddressed | — |
| A7 dual-use political currency | **not crossed**; unaddressed | — |
| A8 scarce named agents over a many | **structure crossed**, loop not | NPC T-NPC-10; SE T-SE-6 |
| A9 belief with provenance | **crossed**, ahead of the twenty; deceit and fabrication absent | IN T-IN-13; FI T-FI-4 |

Valoria has crossed the epistemic asymmetries (A1, A9) the political corpus lacks and not the demographic ones
(A3, lagged cohort, labour) the settlement corpus supplies. Jordan's statements remove the plan's refusal of
A3 without choosing it: whether a levy costs population is left open (J-C-2).

---

## C6. CONSOLIDATED MISSING-AREAS REGISTER

**Count rule.** Every MISSING row and every HOLLOW or BLOCKED row of the lanes' §8.2-§8.3 enters once; rows
naming one game area merge whatever their lane or class. An unsuffixed id was filed MISSING; `(H)` HOLLOW,
`(B)` BLOCKED. *Demand* is the strongest merged: D1 THE NINE or a Jordan statement · D2 canon · D3 a ruling or
Layer 1 · D4 a hole row or the plan · D5 the audit · D6 research alone; S/M/W.

**Arithmetic.** MISSING 99 (MB 17, PC 9, FI 7, SC 9, FA 5, WR 8, IN 14, GO 10, SE 8, NPC 12) + HOLLOW/BLOCKED
65 (MB 5, PC 3, FI 7, SC 9, FA 6, WR 6, IN 10, GO 4, SE 5, NPC 10) = **164** lane rows → **84** consolidated
(persons 3, armies 15, settlements 6, factions 13, knowledge 10, proceedings 9, world 7, surface 6, port 8,
decision 7); 80 merged away; 30 rows join two or more lanes. Placements re-add to each lane's total (MB 22,
PC 12, FI 14, SC 18, FA 11, WR 14, IN 24, GO 14, SE 13, NPC 22).

### Persons and capacity

| id | area | merges | demand | code | v9 | NERS |
|---|---|---|---|---|---|---|
| C-PER-1 | per-person capacity (attributes, skill, kit) read by pool, `Combatant`, command | PC M-PC-1, M-PC-9(H) · IN M-IN-1, H-IN-2(H), H-IN-4(B) · NPC M-NPC-1, H-NPC-1(H), B-NPC-4(B) · SC 8.3-a(B) · FI FI-01 by person(B) | D1 R-09; statement 1 · S | empty on 429 of 430; `Combatant` takes `end` only | J-13 remainder; `train` writes `copying` only (B-Q) | R-VARIETY; S vertical |
| C-PER-2 | a reader's competence; the actor's reading of his own act | FI M-FI-3 · SC M-SC-8 · NPC M-NPC-2 · IN M-IN-7 | D3 AX-7 · S | competence fixed; actor exempt | none; H-200 zero mentions | R-VARIETY; R-COMPLETE |
| C-PER-3 | values and body changing in shipped play | NPC M-NPC-3, B-NPC-3(B) | D1 R-06 · S | built, shipped at control | none arms them | R-WORLD |

### Combat and armies

| id | area | merges | demand | code | v9 | NERS |
|---|---|---|---|---|---|---|
| C-ARM-1 | a season force scale clearing the rout floor | MB M-MB-1, IN-13(H), MB-07r(H/B) | D1 R-04, R-07; statement 3 · S | troops = weight (≤ 6) against floor 80 | none; IN-52 only lowers | R-COMPLETE; R-CHOICE |
| C-ARM-2 | a settlement's troop stock: levied, fielded, drawn down | MB M-MB-15, M-MB-6, IN-52(H) · SE M-SE-9 · FA M-FA-10 · IN M-IN-12, H-IN-10(H) | D1 statements 1, 4, 5 · S | no troop kind; cohorts have no `commit` | opposite reading (IN-49, IN-52 LF-1) | R-CHOICE; S vertical |
| C-ARM-3 | the store act under its own name, priced | IN M-IN-13 · SE H-SE-1(H) | D1 statement 5 · S | `levy` moves stores, unpriced | IN-49 under the wrong name | E-LEGIBILITY; R-CHOICE |
| C-ARM-4 | composition: subunits, kinds, subformations, chosen by the faction | MB M-MB-2, M-MB-17, J-19(B) | D1 statements 3, 4 · S | `build_army` harness-only | MB-08 LEAVE | R-VARIETY; R-CHOICE |
| C-ARM-5 | a commander whose person reaches the field | MB M-MB-3 · NPC M-NPC-13 | D1 statement 1 · S | `command=4`; `Officer` harness-only | U-4, K-6 LEAVE | R-PLAYER |
| C-ARM-6 | experience as troop quality | MB M-MB-16 | D1 statement 1 · S | absent | none | R-VARIETY |
| C-ARM-7 | a decision at the field | MB M-MB-5 | D1 R-04 · S | `resolve_field` takes no choice | none | R-CHOICE; S pause |
| C-ARM-8 | a battle that yields to a person (duel, champion, capture) | MB M-MB-4 · PC M-PC-5 · IN M-IN-6 | D5 A2; R-04 · M | one atomic 18-tick call | M-6 LEAVE | S vertical; S pause |
| C-ARM-9 | death in battle | MB M-MB-14 | D3 ED-IN-0279 · M | `max(1, …)` floor | none | R-WORLD |
| C-ARM-10 | the actor's own outcome written | PC M-PC-2 | D1 Jordan 2026-09-04 · S | lifted, never read | none | R-COMPLETE |
| C-ARM-11 | fights with more than two persons | PC M-PC-3 | D3 Layer 1 §E.2.1 · S | two claimants | PC-08, WS-7 LEAVE | S vertical |
| C-ARM-12 | a cohort fought as one body | PC M-PC-12 | D3 S9 · S | `weight` unread at the seam | none (H-49 zero mentions) | R-COMPLETE |
| C-ARM-13 | the occupier's consumption | MB M-MB-8 | D4 IN-13 · M | absent | none | R-COMPLETE |
| C-ARM-14 | the authored cast marches | MB M-MB-13 | D4 H-175 · M | never attempted in the corpus | none | R-WORLD |
| C-ARM-15 | an access gate whose premise holds | NPC H-NPC-5(H) | D4 IN-59 · M | heads off-seat | IN-59 (B-Y) | R-COMPLETE |

### Settlements, population and the economy

| id | area | merges | demand | code | v9 | NERS |
|---|---|---|---|---|---|---|
| C-SET-1 | births and growth | SE M-SE-1, H-SE-3(H) | D3 RR-2; D5 A6 · S | absent | none | R-WORLD; N |
| C-SET-2 | exchange between places; a trading act | SE M-SE-2 · SC M-SC-6 · FA FA-01 trade(B) | D1 R-05 · S | no `_eff_exchange` (reverted) | IN-33, no batch | R-VARIETY |
| C-SET-3 | adjacency | SE M-SE-4 | D2 GD-3 · S | parsed, read by nothing | none | S lateral |
| C-SET-4 | labour as a production input | SE M-SE-5 | D6 · W | yield ignores headcount | none | R-COMPLETE |
| C-SET-5 | terms of taking a place | SE M-SE-7 | D6 · W | absent | none | R-CHOICE |
| C-SET-6 | regional production | SE M-SE-8 | D6 · W | every site everywhere | none | R-VARIETY |

### Factions, war, treaty, succession and the ending

| id | area | merges | demand | code | v9 | NERS |
|---|---|---|---|---|---|---|
| C-FAC-1 | war as a state | FA M-FA-1 · MB M-MB-7 | D3 Layer 1 04:451; D1 IN-36 · S | `at_war` read by nothing | none | R-WORLD; S lateral |
| C-FAC-2 | forcing a top holder out | FA M-FA-3 | contested (D6 against a D1 ruling) | strippable by nobody | none | R-WORLD |
| C-FAC-3 | a change of sides priced as a deed, and its bloc | NPC M-NPC-5 · FA M-FA-8 | D4 H-205 · S | judged at `release` cells | none | R-CHOICE |
| C-FAC-4 | an ending reached by choices | FA IN-27(H/B) · WR IN-27(H/B) | D2 GD-1; H-176 · S | absent | IN-27 (B-U) | R-COMPLETE |
| C-FAC-5 | treaties that bind | FA covenant(H) | D2 GD-1 · M | unbuilt | IN-12 step 7, readers deferred | R-CHOICE |
| C-FAC-6 | insurgency forming a faction over contiguous ground | FA IN-30(H) · SE H-SE-2(H) | D2 GD-3 · S | `uncontrolled` report-only | IN-30: any caller exits | R-WORLD |
| C-FAC-7 | grand-strategy acts that do something | FA FA-01 flip(H) | D1 R-04 · S | `dispatch` writes nothing | FA-01 (B-V) | R-CHOICE |
| C-FAC-8 | succession | FA IN-61(B) · IN H-IN-5(B) · NPC B-NPC-1(B) · SC 8.3-f(H) | D1 RS-27 · S | `succeed` declined | IN-61 (B-R), blocked | R-WORLD |
| C-FAC-9 | delegation and regency | IN M-IN-5 · NPC B-NPC-5(B) | D1 Jordan 2026-09-03 · S | built, reverted | IN-48, unscheduled | R-CHOICE |
| C-FAC-10 | offices made and emptied by persons; their cost | IN M-IN-4, H-IN-7(B), H-IN-11(B) · NPC H-NPC-2(H) | D1 R-04 (1) · S | `revoke` hand-forced only | IN-31 exit against H-207 | R-WORLD |
| C-FAC-11 | a threatened holder's response (GD-2) | MB M-MB-12 · WR M-WR-6 | D2 GD-2 · S (form unruled) | absent | none | S methodology |
| C-FAC-12 | recruitment | NPC M-NPC-10 | D6 · W | own `commit` only | none | R-CHOICE |
| C-FAC-13 | usefulness breeds threat | NPC M-NPC-11 | D6 · W | absent | none | R-CHOICE |

### Knowledge, testimony, inquiry and findings

| id | area | merges | demand | code | v9 | NERS |
|---|---|---|---|---|---|---|
| C-KNO-1 | an inquiry that yields content; failure distinct from refusal | FI M-FI-1, FI-01 vs S-6(H), vs scales(H), vs R-05(H), vs Q1(H), SKIP scope(B) | D1 R-04 (3); D3 AX-7 · S | six rows write nothing | FI-01 grades a content-free kind | R-COMPLETE; N |
| C-KNO-2 | the honest misreading | FI M-FI-2 | D3 AX-2 · S | confidence moves, value never | none | R-WORLD |
| C-KNO-3 | the concealer's score as obstacle | FI M-FI-4 | D1 Jordan Q1 · M | default obstacle | none | R-CHOICE |
| C-KNO-4 | testimony from questioning | FI M-FI-6 | D1 Jordan Q4 · M | content-free | none | R-COMPLETE |
| C-KNO-5 | watching a person covertly | FI M-FI-7 | D4 · W | grammar cannot bind it | none | R-VARIETY |
| C-KNO-6 | an investigation role with a provider | FI FI-02(H) | D1 SM-3 · M | role, no provider | FI-02, FI-03 | N |
| C-KNO-7 | a spoken lie | SC M-SC-7 · IN M-IN-14 | D4 H-198 · M | `said_of` passes a held claim | G7 recorded only | R-COMPLETE |
| C-KNO-8 | credibility: intent kept, stake, rank | IN M-IN-8 · NPC M-NPC-9 · SC M-SC-4 | D1 R-07 · M | `rank_gain` dormant | none | R-WORLD |
| C-KNO-9 | who holds a place, knowable | SE M-SE-3 | D2 GD-1, GD-3 · S | 0 of 80 hold `held_by` | none | S diagonal |
| C-KNO-10 | a vacancy delivered by claim | PC M-PC-8 · WR M-WR-9 · NPC M-NPC-6 | D4 H-206 · M | edges deleted with the dead | none | S-DOWN |

### Contests and proceedings

| id | area | merges | demand | code | v9 | NERS |
|---|---|---|---|---|---|---|
| C-PRO-1 | the game a computed case is heard under | SC M-SC-1 | D1 R-04 · S | `DOCKET_ARRANGEMENT: None` | none (IN-10 reverted) | N; R-VARIETY |
| C-PRO-2 | a petition that rises; a receiver who may deny | SC M-SC-2, 8.3-g(H) | D3 ED-IN-0210 · S | addressed to its subject | contested (A-16) | S-UP |
| C-PRO-3 | the stasis issue ladder | SC M-SC-3 | D3 PS/04 · S | mislabelled | none | S methodology |
| C-PRO-4 | procedure before the vote; `carry` | SC M-SC-5 · IN H-IN-6(B) | D4 SC-07 · M | `carry` declined | IN-45; its gate amends Layer 1 | R-WORLD |
| C-PRO-5 | a compromise scaled to the loss | SC 8.3-b(H) | D1 R-05 · M | no disposal reader | SC-03b | R-COMPLETE |
| C-PRO-6 | arrangement data read in production | SC 8.3-c(H) | D4 · W | six keys unread | SC-08, exit met | E-OVERHEAD |
| C-PRO-7 | an obstacle ceiling that does not deprive | SC 8.3-d(H) | D1 Jordan 2026-09-06 · M | p = 0.0006 | SC-01 falsifier | R-COMPLETE |
| C-PRO-8 | a vote over commitments | SC 8.3-e(B) | D2 GD-3(b) · M | `commit` refused | SC-01 step 11; J-4 | R-CHOICE |
| C-PRO-9 | held: `scale:`, nested deliberation, common facts | SC 8.3-h(B), 8.3-i(B) · IN H-IN-8(B) | D1 2026-09-02 · M | `scale:` read by nothing | HELD | S pause |

### The world, threadwork and the crossing

| id | area | merges | demand | code | v9 | NERS |
|---|---|---|---|---|---|---|
| C-WLD-1 | thread operations as persons' acts | WR M-WR-1, IN-06(H), PC-06 K-3(H) | D3 #457 D1 · S | no verb; no `coherence` field | none builds it | N; S vertical |
| C-WLD-2 | what follows the crossing | WR M-WR-2 | D2 P-15 · S | no carrier | none | R-COMPLETE |
| C-WLD-3 | thread hand-offs to field and faction | WR M-WR-3 · MB M-MB-9 | D5 A2 · M | empty hook | none | S diagonal |
| C-WLD-4 | a cost on Mending oneself; Mending another | WR M-WR-4, M-WR-7 | D3 RULINGS C-1, E-1 · M | cost 0; not routed | none | R-CHOICE |
| C-WLD-5 | the Calamity coupled to acts | WR IN-35(H/B) | D1 #457 · S | wear only | IN-35, BLK IN-06 | N |
| C-WLD-6 | practitioner resilience | WR WR-01(B) | D4 · M | gain 0 | WR-01 | R-VARIETY |
| C-WLD-7 | authored ages | WR M-WR-8 | D3 #457 D2 · M | `age_at_build` 0 | none | R-WORLD |

### The player surface and pause

| id | area | merges | demand | code | v9 | NERS |
|---|---|---|---|---|---|---|
| C-SUR-1 | the playable fight | PC M-PC-4 · IN M-IN-2 · MB IN-46(B) | D1 R-04 c3 · S | callback only | IN-46, no batch | R-PLAYER; S pause |
| C-SUR-2 | creation, development, chronicle | GO M-GO-7 · IN H-IN-3(H) · NPC M-NPC-7 · WR IN-37(H) · PC M-PC-10(H) | D1 R-04 c3 · S | builder seats a cast entry; storybar measures | IN-47 no batch; IN-37 | E-LEGIBILITY |
| C-SUR-3 | `explain(p, v)` | IN M-IN-3 · GO M-GO-5 | D3 §C.11 · S | absent | none | E-LEGIBILITY |
| C-SUR-4 | odds shown | GO M-GO-6 · MB M-MB-10 · PC M-PC-6 | D5 A3 · M | `eff_ob` uncalled | none | E-LEGIBILITY |
| C-SUR-5 | the seat at DELIBERATE and the duel yield | GO M-GO-4 | D3 L1-04:844-846 · S | unspecified | none | S pause |
| C-SUR-6 | investigator, contest and faction views | FI M-FI-5 · SC M-SC-9 · FA M-FA-4 | D1 R-04 · M | carriers, no surface | none | E-LEGIBILITY |

### Parity, the resolution kernel and the port

| id | area | merges | demand | code | v9 | NERS |
|---|---|---|---|---|---|---|
| C-POR-1 | one die, one ladder | PC M-PC-7 · MB M-MB-11 | D3 Layer 1 03 · M | continuous Normal; three bands | none | S methodology |
| C-POR-2 | an integer state encoding | GO M-GO-1 | D3 L1-04:1119 · S | `repr()`, floats | none | S methodology |
| C-POR-3 | a portable draw primitive | GO M-GO-2 | D3 L1-04:916 · S | CPython Random | none | S methodology |
| C-POR-4 | port-readable fixtures | GO M-GO-3, GO-05(H/B) | D3 L1-04:913 · M | Python literal | GO-05 paths only | S vertical |
| C-POR-5 | fixed-point resolution | GO M-GO-10 | D3 L1-04:1119 · S | libm floats | none | S methodology |
| C-POR-6 | refusal as a typed value | GO M-GO-8 | D3 L1-04 · S | ~120 in-loop raises | none | R-COMPLETE |
| C-POR-7 | save by replay | GO M-GO-9 | D6 · W | none | none | R-COMPLETE |
| C-POR-8 | a version and a slice that runs | GO GO-01(H/B), GO-06(B), PC-05(H/B) · PC M-PC-11(B) | D3 step 13 · M | skeleton on an undefined base | B-Z; J-9 | N |

### The decision layer

| id | area | merges | demand | code | v9 | NERS |
|---|---|---|---|---|---|---|
| C-DEC-1 | what an ambition demands (OUGHT predicate) | NPC M-NPC-4 · IN M-IN-9 | D1 R-06 · S | read by nothing | none | R-COMPLETE |
| C-DEC-2 | self-interest weighting | NPC M-NPC-12 | D3 ED-IN-0261 · M | `benefits_me` uncalled [CHECKED] | none | R-VARIETY |
| C-DEC-3 | a damping bound on self-feeding loops | IN M-IN-11 | D4 H-25 · M | none | `forgive` (B-Q) | R-COMPLETE |
| C-DEC-4 | a controlled multi-season reading | IN M-IN-10 | CLAUDE.md §7 · M | `arms`: one mechanic | none | R |
| C-DEC-5 | R-05 owned by a position | IN H-IN-1(H) | D1 R-05 · S | relaxed exit | none | — |
| C-DEC-6 | cohorts with pursuits and spread | SE B-SE-1(B), B-SE-2(B) · NPC B-NPC-2(B) | D1 R-06 · M | pursuit term 0 | SE-06 ask-then; HELD | R-CHOICE |
| C-DEC-7 | loyalty and grievance that move choice | NPC H-NPC-3(H), H-NPC-4(H) | D1 R-07 · M | hash EQUAL at `legacy` | IN-58, IN-69, IN-70 | R-WORLD |

### PLANNED-UNBUILT and BUILT-DARK

149 lane rows (MB 11, PC 8, FI 15, SC 17, FA 18, WR 8, IN 30, GO 9, SE 19, NPC 14), unbuilt or unarmed but
not missing under the v9-built assumption, grouped by what builds or arms them (families, not a row merge):

| family | builds or arms it | lanes |
|---|---|---|
| IN-12's twelve verbs (seize … raze) | B-K, B-M, B-Q, B-R | IN, MB, PC, FI, SC, FA, SE, NPC |
| arrival, occupation, foreign march | IN-13, IN-36 | MB, FA, WR, NPC, IN |
| goals, salience, opinion, scar re-read, doctrine | IN-62..72, FA-04..06 (B-X) | FA, NPC, IN |
| proceedings core and tail; inquiry degree, role, counter-espionage, knots, `thread_read` | SC-01..08; FI-01..03; IN-32; PC-06 | SC, FI, WR, PC, NPC, IN |
| `forge`, `work`, `migrate`, `carry`, `found`, `build`; levied stores to the field | IN-45, IN-28, IN-49 (B-K); IN-52 (B-T; `field_provisioning` not in code) | FI, SE, SC, MB, FA, IN |
| legitimacy, ending, insurgency; Calamity; chronicle; character space | IN-23, IN-27, IN-30, IN-35, IN-37; IN-47 (no batch) | FA, SE, GO, WR, FI, NPC, IN |
| duel terms, access; delegation, revocation, succession; `exchange`, IN-09; overlays; act budget | PC-10, IN-59/60; IN-48, IN-31, IN-61; IN-33, IN-09; IN-38; IN-14 | PC, NPC, FA, SE, IN |
| dark knobs: forcing (5), person (8), field (2) | none, IN-65 (conditional), ED-IN-0296, MB-07r; values Jordan's | WR, SE, NPC, PC, SC, FI, MB, FA, IN |
| reader-less carriers (`urgency`, `benefits_me`, σ-leverage, `head()`, `at_war`, `faction_sheet`, `uncontrolled`, `proofs`, `View`, the combat trace, `eff_ob`, module traditions and weapons) | mostly none | all ten |
| the contest kernel's retirement; thread pricing and authored TS | SC-05 HELD; IN-06, K-3 | SC, WR |

---

## C7. DECISIONS FOR JORDAN

Every choice the lanes leave to Jordan, after §0's ladder and C4's rule removed those already decided (the
parity contract, the DELIBERATE seat, the investigation seam, GD-2's faction pass, the felled actor). Values
marked `[OPEN — Jordan tuning]` ride the decision whose form they fill.

| id | question | (a) | (b) | what each does | hinges | blocked until decided |
|---|---|---|---|---|---|---|
| J-C-1 | the store act's name (statement 5 rules `levy` wrong for it) | a new name, his; `levy` becomes the troop verb | — | the statement leaves only (a); the name is his | MB, SE, FA, IN | R-C-2, R-C-10; IN-49, IN-52, H-163 |
| J-C-2 | troops: persons or a stock | a levy lowers cohort weight and raises a stock by that headcount | a non-person troop kind, uncoupled from population | (a) war costs population (20G A3, Proposal F); (b) simpler, war costs no labour | MB, SE, FA, IN, NPC, PC | R-C-2, R-C-11, R-C-13 (cohort half); men-per-weight scale |
| J-C-3 | the capacity source, and J-13's reading | one stored source read by pool, `Combatant`, command, competence | identical capacities intended; withdraw the claim | (a) persons differ in what they can do, R-09 meetable; (b) a game of wants alone. Sub: new field or `capability` (X-14); the actor's own reading owed? (X-15) | PC, SC, MB, NPC, IN, FI, WR, GO | R-C-1; R-C-23 (competence); R-C-37 (attributes) |
| J-C-4 | a standing winner's wounds | written | not written (as `march` reads) | every fight costs both sides, or the winner walks away whole | PC | R-C-13's rest |
| J-C-5 | replacing a top holder | allowed | abdication only | (a) overwrites the 2026-10-12 ruling and SC-04 | FA, SC, NPC | R-C-30's replaced arm |
| J-C-6 | do persons lie | a lie is a deed claim a witness can hold False | no: close deception and intent-keeping | testimony and interrogation have something to catch, or G7, H-198, H-191 are cut | SC, IN, FI, NPC | R-C-35; R-C-14 |
| J-C-7 | how a petition closes | `destroy_record` (against A-13) | a `deny` row (against A-16) | both deliver Ruling 2; they leave different log entries | SC, IN | R-C-16's closer |
| J-C-8 | a failed or refused inquiry | error, and refusal witnessable | ignorance, refusal silent (SKIP) | a confidently wrong finding and a visible attempt, or today's silence (H-111 records both) | FI | R-C-23; FI-01's exit |
| J-C-9 | population | grows at CENSUS to `capacity` (RR-2) | fixed; delete `Rung.envelope` | a lagged population (20G axis 6), or a world that only shrinks under forcing | SE, WR, NPC, MB | R-C-9; R-C-32 |
| J-C-10 | what counts as MISSING | strict: no position | wide: no position that delivers (LEAVE, unscheduled, hollow exit) | counts, not the game; this file enters C6 rows wide and keeps the lanes' classes | all | the next count |
| J-C-11 | the Godot version (J-9); fixed-point table resolution | — | — | parity itself is decided (C4) | GO, PC | GO-01, GO-05, PC-05; R-C-5 |
| J-C-12 | what the player sees | AX-7's gloss: no state hidden | §C.11: the arithmetic the character holds | true odds admissible, or only the actor's estimate; and is a band shown | GO, IN, SC, MB | R-C-38 |
| J-C-13 | the ending | a Query over seats; GD-1's thresholds struck | GD-1 kept, re-expressed through persons | threshold against choice-only victory; 15 or 17 territories | FA, WR, SE | R-C-31; IN-27 |
| J-C-14 | GD-2's response | a duty on the threatened holder | retired | a person's question names the territory, or a canon row goes | MB, WR, FA, IN | C-FAC-11 |
| J-C-15 | war's gate | `march` requires `at_war` | `fight` is gated, or march freely | what a war licenses (F.33) | MB, FA | R-C-12's gate |
| J-C-16 | repetition in a season | §C.2: keep the dedup filter | §C.3: delete it, re-measure | overwrites Layer 1 either way | IN | the filter |
| J-C-17 | offices in computed play | `revoke`, `establish` execute through a general motive; a delegate may be dismissed early | DONE-test; term-end only | offices change hands by choice, or by test only | IN, FA, NPC, SE | R-C-19; IN-31's exit |
| J-C-18 | one substrate; the field's margin | all scales on the season's die and `degree_from_net` | combat and field keep theirs, stated in Layer 1 | one ladder (rewrites ED-IN-0279), or no balance moves | PC, MB, IN | R-C-3's substrate half |
| J-C-19 | death in battle | a lost field kills | wounds only | two games of war | MB | R-C-34 |
| J-C-20 | a commander's fate | a duel at ENCOUNTER | the side's fraction | which acts interrupt a battle | MB, PC, IN, GO | R-C-24 |
| J-C-21 | experience on a stock | one averaged grade | entries per grade | legibility against fidelity | MB | R-C-2 (experience) |
| J-C-22 | the crossing | removal from play | play as an altered being | P-15's consequence | WR | R-C-26 |
| J-C-23 | the thread History term (PP-624) | code: `min(3, history + 3)`, inert | `min(3, history) + 3` | whether History matters | WR | the term |
| J-C-24 | Coherence's elastic return | a licensed clock | a chosen rest | a fourth clock against an act | WR | `coherence.recover()` |
| J-C-25 | forcing values | his values (#457 D2; J-6) | — | unwatched seasons carry dearth and death, or not | WR, SE, NPC | R-C-32 |
| J-C-26 | kin | a tie the heir title reads | heir is a title only | dynastic against title game | NPC | IN-61 eligibility |
| J-C-27 | a creed after its head dies | binds the man (schism) | binds the seat (vacancy) | regicide splits or transfers | NPC | dead-referent state |
| J-C-28 | self-interest | build ED-IN-0261's weighting | delete `benefits_me` | persons who weigh self-interest, or not | NPC, IN | R-C-8 |
| J-C-29 | proceedings | disposal `degree` read as term length or release price | nested deliberation in RESOLVE: yes or no (H-56) | how hard a narrow win binds; whether contests react mid-fold | SC | R-C-28; SC-01 step 15 |
| J-C-30 | settlements | production authored by place | persisting dearth deposited every season (re-opens H-160 (3)) | interdependent towns; neglect known at the seat | SE | R-C-7; K-SE-7 |
| J-C-31 | played fidelity | the duel decision set (J-15); a player commanding a field | creation as an act or a selection | how much of a fight a player touches | PC, MB, IN | R-C-37 |

---

## C8. CONSOLIDATED KEY RECOMMENDATIONS

Forty, from the lanes' 112 live K-rows (MB 12, PC 9, FI 8, SC 12, FA 12, WR 12, IN 12, GO 11, SE 12, NPC 12).
Seven are rulings only and appear in C7, not here: K-IN-3, K-SC-12, K-WR-7, K-WR-8, K-NPC-4, K-NPC-6, K-SE-7.
*Ladder*: a takeable step, or Jordan with the C7 id. A row that adds names what it cuts. Rows within a group
follow C3 (d)'s layers; ids are handles.

**Top ten, and why this order.** R-C-2 (troop stock): Jordan's own demand, contradicted by the plan, six
lanes waiting. R-C-1 (capacity): the source whose absence starves most seams. R-C-3 (one die, monotone):
R-C-1 wakes the sawtooth. R-C-11 (order of battle): turns the stock into statement 4's subunits. R-C-37 (the
surface batch): M1 waits on it and its designs exist. R-C-23 (inquiry yield): content for the chronicle's
thinnest input. R-C-12 (war): the strategic layer has no conflict without it. R-C-8 (deletions): cheap,
shortens every later read. R-C-29 (vacancy by claim): unblocks succession. R-C-4 (integer hash): every golden
re-pin after it is the last of its kind.

### PRIMITIVES

| id | recommendation | merges | ladder | adds / cuts | depends | falsifier |
|---|---|---|---|---|---|---|
| R-C-8 | Delete what nothing reads: `urgency` (after IN-62), `benefits_me` (unless J-C-28 builds it), the survivor-ratio degree, the empty `rally_check` and `threadwork_check`, D-6/D-7 and three unread arrangement keys, the seam's `winner`, the skeleton's Key-type resources. | K-IN-2, K-MB-7, K-MB-11, K-SC-10, K-PC-3, K-GO-10; audit G2b, G5 | steps 2-3 | cuts only | X-1 order | seed-0 `content_hash` equal before and after each |
| R-C-3 | Put every per-die figure in one owner under an obstacle rule where a more capable equal pair never has worse odds; rule one substrate and the field's margin. | K-IN-5, K-PC-8, K-MB-8; G2a, G2c, G2d | owner step 4; rest Jordan (J-C-18) | cuts three literal owners, then a substrate or a Layer 1 sentence | — | the per-die pair defined once; odds monotone in capacity |
| R-C-4 | Fold state into `content_hash` through one integer encoder with declared field order; author the baseline fixtures in YAML; return refusals as a typed value in touched seams. | K-GO-1, K-GO-4, K-GO-5 | step 3-4 | an encoder, a Result type; cuts `repr()`, floats in `pursuits`, the Python literal head | — | an independent encoder prints the same seed-0 hash; a planted float is refused |
| R-C-5 | Own the draw primitive behind `H(seed, tick, subject, purpose)` and resolve draws in fixed point. | K-GO-2, K-GO-11 | step 3; resolution Jordan (J-C-11) | tables under one owner; cuts `random.Random`, libm calls | R-C-4 | a table-only implementation reproduces 10,000 seeded outcomes |
| R-C-1 | Rule one source of per-person capacity, stored once and derived at read by the pool, the `Combatant`, a commander's command and a witness's competence. | K-IN-1, K-NPC-1, K-PC-1, K-SC-2, K-FI-1, K-GO-8; G1 | Jordan (J-C-3) | four readers; cuts `pool_default`, `obstacle_default`, `competence = 1`, `command=4`, unread `stats`/`ts` | R-C-3 | persons differing only in capacity resolve differently; equal capacity reproduces today's hash |
| R-C-2 | Give each settlement a troop stock by kind, raised by `levy`, fielded by `march`, drawn down by loss, graded by equipment, experience and commander. | K-MB-1, K-MB-3, K-SE-13, K-FA-13, K-IN-13 | Jordan (J-C-1, -2, -21); direction is statement 1 | a count per kind, one write on `levy`; cuts `_weighted_unit`'s weight feed, `_SEASON_FORCE_POWER`, IN-52's stores bound | J-C-1, J-C-2 | a levy raises the stock by the headcount drawn; a lost field lowers the next levy; arm off keeps the hash |
| R-C-6 | Deposit a `held_by` claim when a seat over a place is conferred, revoked or vacated in a person's sight; let regard reach a place through its holder. | K-SE-2 | step 5 | a deposit occasion; cuts the ABSENT H-195 marker | — | after one season some persons hold `held_by` (0 of 80 today) |
| R-C-7 | Read adjacency from the parsed geography as one Query for contiguity, spread and distance. | K-SE-3, K-SE-10 (map production, Jordan) | step 3-4; production Jordan (J-C-30) | one Query, no state | — | two adjacent uncontrolled territories group; non-adjacent do not |
| R-C-9 | Give population one carrier, cohort `weight`, growing at CENSUS until `capacity` refuses or ruled fixed; let `work` scale with it. | K-SE-1, K-SE-8 | Jordan (J-C-9); `work` step 5 | one CENSUS term or none; cuts two of three population carriers | J-C-9 | over ten fed seasons a cohort's weight rises and stops at `capacity` |

### VERBS

| id | recommendation | merges | ladder | adds / cuts | depends | falsifier |
|---|---|---|---|---|---|---|
| R-C-10 | Give the store act its own name and row, price it by the hunger it leaves, and let the taxed person comply, evade or defy first. | K-SE-5, K-FA-5, K-IN-13 (name) | name Jordan (J-C-1); price 5; answer 3 | a rename; cuts the misnaming across IN-49, IN-52, H-163 | J-C-1; D-20, D-21 | after the rename `levy` writes no goods |
| R-C-11 | Let `march` carry an order of battle chosen by its seat and build every side through `build_army`, moved into `modules/mass_battle/`. | K-MB-2, K-MB-4, K-FA-13 | step 5 | one operand; cuts `_MVP_SUBUNIT_SHAPE`, the fixed `Line` | R-C-2 | equal stocks under different orders give different outcomes |
| R-C-12 | Let a person whose goal holds stance −1 toward a rival seat utter WAR, and let one act read `at_war`. | K-FA-1, K-MB-5 | producer 3; gate Jordan (J-C-15) | one payload read, one conjunct | own-echo precondition | seed 0 yields WAR with a live `commit` |
| R-C-13 | Write a felled actor as the subject is written; refuse fights with a cohort party until a cohort can be fought at weight; require co-location for lethal acts. | K-PC-2, K-PC-12, K-NPC-12 | 4; 5; 3; standing winner Jordan (J-C-4) | a second subject write, two conjuncts; cuts false `contest.undecided` and the remote kill | heads at seats (D-25) | a fight that fells its actor removes him; no death joins distant persons |
| R-C-14 | Let `interview` yield the questioned person's own `tell` about the matter. | K-FI-3 | step 4 | the matter as the Event's subject | J-C-6 for false replies | B, holding a claim about C, next tells A about C |
| R-C-15 | Let a concealer's score set the obstacle an inquiry into it faces. | K-FI-5 | step 3 | a branch in `_obstacle_of` | `forge` executing | forged and true Records differ by `forgery_quality`/2 |
| R-C-16 | Address a computed petition to the seat above its subject, and give the receiver a closer. | K-SC-3 | address 4; closer Jordan (J-C-7) | no verb for the address | — | a petition reaches a person above its subject |
| R-C-17 | Let a case's opener name its game from a writ he holds. | K-SC-1 | step 5, after IN-10 | one operand; cuts `UNDECLARED_DISPOSAL` as the computed path | IN-10 | ≥ 1 computed `determine` opens `detain`, `ban` or `succession` |
| R-C-18 | Make thread operations persons' acts writing Coherence through the seam; keep `restore` for fabric; seed authored TS once a writer exists. | K-WR-2, K-WR-3, K-WR-1 | step 3-4 | verb rows on `operations.py`; cuts the module's Coherence store, the empty hook, IN-35's restore reading | IN-06 | a working writes `(Person, coherence)`; rows deleted keep the hash |
| R-C-19 | Let a ruler delegate by a termed second seat, ended by term or `release`. | K-FA-11, K-SE-6, K-NPC-8, K-IN-4 | step 3; dismissal and computed `revoke` Jordan (J-C-17) | a seat row per delegation; cuts the reverted `delegate` kind | — | the deputy acts `via` the seat; after the term he refuses |
| R-C-20 | Give a broken vow its own deed; end a covenant party's `commit` when he breaches it. | K-NPC-5, K-FA-2 | step 3-4 | one cell pair, one reader | — | vow-break and `release` judged differently |
| R-C-21 | Publish an edict as an `issue`d Record to everyone in purview, not a `proclaim` verb. | K-FA-12 | step 4 | an addressee form; cuts `proclaim` | — | claims land in purview and nowhere else |
| R-C-22 | When `exchange` returns, let seat-holders trade stores through it; seed no `negotiation` before then. | K-SE-4, K-SC-11 | step 4-5 | a seat-treasury operand reading | IN-33 | complementary rungs trade, conserved |

### MECHANICS

| id | recommendation | merges | ladder | adds / cuts | depends | falsifier |
|---|---|---|---|---|---|---|
| R-C-29 | Keep a dead seat-holder's ended edges so witnesses name his office and the vacancy reaches every person who learns of it. | K-NPC-3, K-PC-10 | step 3/5 | cuts `World._departed` | — | after a regicide a non-conferrer holds a claim naming the office |
| R-C-23 | Give every inquiry a yield on the content-deposit model, starting with Records, without widening `requires_typed`; keep refusal apart from Failure; land the role only with a provider. | K-FI-6, K-FI-9, K-FI-7, K-FI-8 | Records 4; role 3/5; error and refusal Jordan (J-C-8) | a trigger on an existing deposit; cuts `research`'s empty yield | — | a Success `research` leaves the Record's content in the actor's ledger |
| R-C-24 | Let a battle stop at a phase boundary for a present person's act and resume, reading a duel only as a fraction of the side. | K-IN-6, K-MB-10, K-PC-5 | form 4; acts Jordan (J-C-20) | one yield point; cuts `Command=0` rout, M-6's LEAVE | R-C-37 | a field with a commanders' duel differs from one that forbids it |
| R-C-25 | Bound fielded troops by the smaller of the stock and the treasury's ration. | K-MB-6 | step 3 | IN-52's input becomes the stock | R-C-2 | a full stock with an empty treasury fields only the bound |
| R-C-26 | Feed the Calamity from thread strain; price Mending oneself in its Ob and route Mending another; give the crossing a consequence. | K-WR-4, K-WR-6, K-WR-5 | 3; crossing Jordan (J-C-22) | one input, one term, one branch; cuts `ms_track.py` | R-C-18 | Menders stabilize, workers destabilize, against a no-acts arm |
| R-C-27 | Let allegiance move with deeds done to oneself, intent kept be learnt, and a teller weigh by the hearer's claims about his seat. | K-NPC-7, K-NPC-10, K-SC-7 | step 5 | kinds in `PAIRED_KINDS`, a reconciliation, a `rank_gain` producer | — | a revoked man regards his head lower than a control |
| R-C-28 | Add the stasis `issue` ladder, a reader for a disposal's `degree` (or stop writing it), and a citable recorded defeat. | K-SC-4, K-SC-5, K-SC-8 | 3-5; reader Jordan (J-C-29) | four roster members, a reader; cuts the mislabel, `records_dissent` | SC-03b | `Partial` and `Success` disposals differ later |
| R-C-30 | Found an insurgent faction only on a creed with two commits; offer a top holder his resignation; make the highest seat-holder the head; let the Church's appetite rise with its holdings. | K-FA-7, K-FA-3, K-FA-4, K-FA-8 | 3; head and replacement Jordan (Layer 1 B.6.1; J-C-5) | cuts the `Tenure.degree` derivation, a third revocation basis, a planned Church Query | own-echo precondition | sustained `uncontrolled` yields a creed with ≥ 2 commits |
| R-C-31 | End the realm on a Query over seats held through acts; re-express or strike GD-1's terms and GD-2's pass. | K-FA-6, K-WR-10, K-WR-12, K-IN-12 (GD-2) | Jordan (J-C-13, -14) | cuts canon clauses | — | every hold the ending reads traces to an act in `w.log` |
| R-C-32 | Arm or delete every dark person and world knob; author ages and ship forcing at Jordan's values. | K-NPC-2, K-WR-9 | arm-or-delete 3; values Jordan (J-C-25) | cuts each knob not armed, with its hole row | R-C-9 | a four-season realm where weights and bodies move, the hash declared |
| R-C-33 | When `seize` lands, let the taker's terms be what he does with the place's seats. | K-SE-9 | step 5 | no terms object | R-C-6 | a confirmed and a revoked holder differ in stance toward the taker |

### TEXTURE

| id | recommendation | merges | ladder | adds / cuts | depends | falsifier |
|---|---|---|---|---|---|---|
| R-C-34 | Let a lost field kill and emit `person.died`. | K-MB-9 | Jordan (J-C-19) | one emission; cuts the `max(1, …)` floor | R-C-2 | a seeded field kills a named loser |
| R-C-35 | Let a teller speak a lie at `said_of`. | K-SC-6, K-IN-7 | Jordan (J-C-6) | one value rule; cuts ABSENT H-198 | — | a hearer holds a value the teller does not, not from `Partial` |
| R-C-36 | Read an ambition's predicate, so it is met or thwarted. | K-NPC-9; K-IN-2 (predicate) | step 5 | one reader, or the field's deletion | IN-66 | a met ambition stops raising its question |

### SURFACE

| id | recommendation | merges | ladder | adds / cuts | depends | falsifier |
|---|---|---|---|---|---|---|
| R-C-37 | Batch IN-46 and IN-47; seat the player at DELIBERATE and the duel yield, outside the pooled map; let creation write a cast entry; fight a played fight one engagement per act; save as seed plus acts. | K-IN-10, K-GO-3, K-GO-8, K-PC-4, K-GO-9 | 3-4; decision set and creation Jordan (J-C-31) | a batch, one exclusion clause; cuts the RESOLVE-time fight for played persons | — | AUTOMATED and PLAYABLE with the chooser's choices end at one hash |
| R-C-38 | Build `explain(p, v)` from the holder's claims as the one owner of every shown derivation; show odds only as the character believes them. | K-GO-6, K-GO-7, K-IN-9, K-SC-9, K-MB-12 | Jordan (J-C-12) | one function; cuts the losing Layer 1 sentence | J-C-12 | `explain` takes no `World`; different claims show different odds |
| R-C-39 | Render the chronicle and every view as projections of what the person holds, carrying each act's decisive content. | K-WR-11, K-NPC-11, K-FI-11, K-FA-9, K-SE-12, K-PC-9 | 3-5 | no store; one renderer; cuts the trace key and a second render path | R-C-23, R-C-37 | two persons read different chronicles; none shows an unwitnessed event |

### APPARATUS (IN only)

| id | recommendation | merges | ladder | adds / cuts | depends | falsifier |
|---|---|---|---|---|---|---|
| R-C-40 | Make `arms` sweep any knob over N seasons; untrack run output, fork-delete `params_tables.yaml`, re-point the dead CANONICAL path and AX-7's stale sites. | K-IN-11, K-IN-12; X1, X3, G6, G8 | steps 1-4 | two arguments; cuts about 87,000 tracked lines | — | a planted difference is detected over N seasons |

---

## C9. LIMITS AND METHOD

- **Opened by this pass** ([CHECKED]): every `[CHECKED]` locator above, plus the audit upload 405-508, 20G
  1-26, 77-152, 221-248, 349-377, 408-471, and `git diff --stat` from `5445e34` (the commits since are
  checkpoints of `research/by_lane/` only, including partial copies of this file).
- **Taken from the digests** ([LANE]): every other lane claim, including the §8.1 counts of MB, PC, FI, FA, WR,
  IN, GO and NPC (each digest quotes its lane's §8.1 line; not re-opened). Digest against lane file: SC's §8.4
  has 17 rows, not 14; SE's M-SE-8 is "folded" in its self-audit but still a §8.2 row, and is counted.
- **What the lanes could not check:** no lane ran `corpus_run`, `aperture 4 0`, `arms`, `soak` or a
  multi-season realm; most did not run `resolution-diagnostic`; the probes behind several findings (PC's 400-fight
  mirror and cohort probes, GO's float and cross-process hash probes, MB's 22-cell field probe, SE's three-arm
  probe) are uncommitted session artifacts; the critics were read-only, without Bash, and sampled 14-41 claims
  per lane; lanes were read at `d885abf`, `021fd96` or `5445e34`.
- **This pass:** ran no test and no instrument; spawned no subagents (one reader held the ten digests; the
  independence §10 buys belongs on a verdict critic, which is the orchestrator's call). The C6 merges and the
  C8 distillation are judgments: another reader could split C-ARM-2 or join C-SUR-3 and C-SUR-4.
- **Corpus bounds:** 20G's twenty titles (Dwarf Fortress, RimWorld, Victoria, Frostpunk, Old World unexamined);
  the churn survey (F01-F84), *Mechanics of Inquiry* (P1-P58), *A Tells B About C*, the earlier drafts of the
  teardown and surveys, and Unreality Suite documents 09-10 are in neither the repository nor the uploads
  [UPLOAD_CHECKS].
- **Not reconciled:** the `march` realm record (`req:675` against `req:1124`), which needs a run; the audit's
  candidate-formation datum (G9 unrun); whether a cohort could ever `commit`; whether statement 1's "as their
  own resource" means a non-person stock (carried as J-C-2 rather than decided).
