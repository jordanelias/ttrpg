# Verbs, v2 — part 11: Part VI.3, social contest (SC)

## Status: PROPOSED (2026-10-17). Reference, not canon (`CLAUDE.md` §0.05): nothing here binds the game or is read by it. Merging ratifies nothing unless Jordan so rules. Static reading and static lookup only; no run.
## Parts, in reading order: [head](2026-10-16-verbs-01-thesis-and-persons.md) (§0, Part I Persons) · [`verbs-02`](2026-10-16-verbs-02-attributes.md) (Part II Attributes) · [`verbs-03`](2026-10-16-verbs-03-standards-roster-and-reconciliation.md) and [`verbs-04`](2026-10-16-verbs-04-critics-etymology-gaps-and-decisions.md) (Part III Verbs: standards, roster, reconciliation; critics, etymology audit, gap coverage, named mechanics, decisions) · [`verbs-05`](2026-10-16-verbs-05-what-verbs-do-to-the-world-1.md) and [`verbs-06`](2026-10-16-verbs-06-what-verbs-do-to-the-world-2.md) (Part IV What verbs do to the world) · [`verbs-07`](2026-10-16-verbs-07-roadmap-reliability-and-sources.md) (§5 Roadmap, §6 Reliability ledger, §7 Sources) · [`verbs-08`](2026-10-16-verbs-08-engine-findings-from-the-first-trial.md) (Part V: engine findings carried from the first-pass trial) · Part VI, the lexicon by subsystem: [`verbs-09`](2026-10-16-verbs-09-lexicon-personal-combat.md) PC · [`verbs-10`](2026-10-16-verbs-10-lexicon-mass-battle.md) MB · **this file** SC · [`verbs-12`](2026-10-16-verbs-12-lexicon-fieldwork-and-inquiry.md) FI · [`verbs-13`](2026-10-16-verbs-13-lexicon-threadwork.md) TW · [`verbs-14`](2026-10-16-verbs-14-lexicon-settlements-and-governance.md) GV · [`verbs-15`](2026-10-16-verbs-15-lexicon-faction-actions.md) FA · [`verbs-16`](2026-10-16-verbs-16-lexicon-economy-trade-and-craft.md) EC · [`verbs-17`](2026-10-16-verbs-17-lexicon-world-travel-and-survival.md) WT · [`verbs-18`](2026-10-16-verbs-18-lexicon-npc-life-and-persons.md) NP · Part VII, the verb gap register (the evidence behind Part VI's coverage tables): [`verbs-19`](2026-10-16-verbs-19-gap-register-pc-and-np.md) PC+NP · [`verbs-20`](2026-10-16-verbs-20-gap-register-mb-and-fa.md) MB+FA · [`verbs-21`](2026-10-16-verbs-21-gap-register-sc-and-gv.md) SC+GV · [`verbs-22`](2026-10-16-verbs-22-gap-register-fi-and-tw.md) FI+TW · [`verbs-23`](2026-10-16-verbs-23-gap-register-ec-and-wt.md) EC+WT.

**How to cite this Part.** The lane's own sections are numbered 3.1 to 3.9; cite them as `SC §3.n` (for example `SC §3.9` for its items for Jordan). Gap ids (`SC-G01` …) resolve in Part VII (`verbs-21`). Abbreviations such as `VT`, `VCD`, `v2-p3` are defined in the lane's opening paragraphs; `v2-p3`, `v2-p4`, `v2-p8` are the first-pass v2 parts as filed at `716c253`. Old file names such as `…synthesis_part8.md` or `_part8` in the body also mean those first-pass files; the suite was later renamed `2026-10-16-verbs-NN-…`. Mechanic ids (`M1`, `M-1`, `M-WT-1`) are this lane's own.

**Rulings that override this section** (`verbs-03` §III.5; where this section and the roster disagree, the roster governs):

- R-06: the rename `utter` → `declare` is **withdrawn**: `declare` is FA's seat-level row. `utter` stays; the candidate rename is `propound`.
- R-07: `interrogate` is SC's; FI's `interview` is the non-custodial row.
- R-10: `carry` → `lodge` is adopted in the rename batch.
- R-12: `construe` is GV's row.
- R-14: `forge` is FI's.
- R-24: "challenge a claim" is `dispute`.

---

# SC — social contest

Status: lane deliverable for the v2 Part III / Part V rewrite, 2026-10-16. Reference, not canon
(CLAUDE.md §0.05): nothing here is a mechanism; every engine fact is cited to the file that holds it.
Register rows SC-G01…SC-G59 (Part VII (`verbs-21`)). Abbreviations: VT = 
`engine/season/verb_table.yaml`, EI = `engine/season/loop/effects_information.py`, ARR =
`engine/season/arrangements.yaml`, RHET = `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md`,
COMP-1 = `research/valoria_game_precedent_companion_v1.md`, XSC = `research/cross_scale_action_catalogue_v1.md`,
v9-p5/v9-p6 = `workplans/valoria_master_workplan_v9_part5.md`/`_part6.md`, v2-p3/v2-p8 = the v2 synthesis parts.

**Result at a glance.** 7 suites; 10 hosts (`tell`, `persuade`, `declare`, `commit`, `petition`,
`lodge`, `convene`, `open_case`, `speak`, `determine`), of which 1 is a new row (`persuade`, the planned
`argue`) and 2 are shipped rows renamed (`utter` → `declare`, `carry` → `lodge`). Lexicon: 47 names —
24 FOLDED, 14 SHIPPED (incl. the two old names and `forge`, `construe`, `challenge`), 5 PARKED, 2
CULLED, 1 NEW, 1 PLANNED. Gaps: 59 of 59 dispositioned (36 closed by a verb — 10 needing no new
mechanic, 26 "once" a named mechanic of §3.7 exists; 9 PARKED; 10 OUT OF SCOPE; 2 STALE; 2 DISPUTED). One item for Jordan (J-C-6).

## 3.1 Subsystem mechanic

**What runs today.** Seven `social`-stratum rows and three `binding_decision` rows carry SC.
`tell` (VT:985) is contested on "a standing" against the hearer `to` and writes nothing; WITNESS deposits
the told claim, teller chained (VT:1015-1062). `utter` (VT:1267) mints an
immutable Proposition whose `mood` is the payload's, default `OUGHT`, plus the utterer's `hold`
(EI:857-891). `commit` (VT:128) opens a `commit` Tenure on a Proposition. `speak` (VT:924) has no
precondition, writes nothing and emits `speech.made`; WITNESS deposits it like any kind
(`hole_register.yaml:652`); no reader keys on it outside `harness/` (grep). `petition` (VT:805) mints a `petition` Record held by the petitioner,
`to` a Person, `from` a Rung. `carry` (VT:105) re-winds a held petition's stages and appends it to
`World.docket` (EI:300-). `construe` (VT:829) is graded `absent` and is not resolvable. `convene`
(VT:188) writes a `Date` with no holder; `open_case` (VT:780) mints a case file and a docket item by
`remit:determine`; `determine` (VT:222) opens the docketed arrangement's disposal Tenure (`oblige`,
`detain` or `ban`) on a Person, through a bench and a quorum. Data: seven arrangements, six speech
kinds (ARR:44-233); proofs `record, testimony, oath, confession` (`rosters.yaml:2095`).

**What it lacks.** A contest provider for `speak`/`determine` (SC-01 steps 12-15, v9-p6:22-); any
writer of `Person.pursuits` (`write_matrix.yaml:179-186`, H-62: "Part E carries no argument verb"); a
reader of speech kinds, proofs or genres; an arrangement for a computed case (EI:271-272: "NOT
DERIVED"); a dated sitting; a `Record` disposal — parliament and council dispose `Record` (ARR:122,
:144), which `DISPOSABLE_KINDS` excludes (`state/gate.py:254-257`), so no deliberative body decides
anything; and any way to say what one does not hold.

## 3.2 Convention floor

Status key: *shipped* = a verb row; *planned* = a workplan position; *designed* = v2 / VCD only;
*absent*.

| floor act | precedent | status |
|---|---|---|
| inform, gossip, spread news | XSC:642 §6.3 *Rumour* row; [MEMORY] Crusader Kings 3: secrets learned and spread by characters (the *Expose secret* interaction) | shipped (`tell`) |
| persuade (change someone's mind) | COMP-1:432-437 §2.10 (Burning Wheel Duel of Wits: Body of Argument, compromise); XSC:639, :641 §6.3 *Converse*, *Impress*; [MEMORY] Blades in the Dark *Sway* action (influence by guile, charm or argument); [MEMORY] Crusader Kings 3 *Sway* scheme (raises one character's opinion over time) | planned (`argue`, v9-p5:64 IN-12 step 9) |
| charm, flatter, praise | XSC:641 §6.3 *Impress* (Ob from the NPC's Cognition); VCD:674 §6.1 approach verbs; [MEMORY] Crusader Kings 3 *Sway* | designed (v2-p8:431, :438) |
| insult, disparage | VCD:674 §6.1 (insult among the approach verbs); COMP-1:436 (Burning Wheel *Incite* manoeuvre) | designed, parked (v2-p8:437) |
| threaten, intimidate | COMP-1:491-494 §2.11 (Diplomacy: every promise and threat is cheap talk); [MEMORY] Blades in the Dark *Command* action (intimidation); [MEMORY] Crusader Kings 3 *hooks* (a held secret used to force an interaction) | designed (v2-p8:430) |
| petition the ruler, ask redress | RHET:300-307 §8.1 (SC 8 petitions: complaints and requests; intercessors); XSC:553-558 §5.5 *Royal Audience*, *Personal Appeal* | shipped (`petition`) |
| accuse, lay a charge | RHET:289 §7.2 (*libellus*, the written complaint); COMP-1:474-476 §2.10 (Pentiment: accusation under an authority) | planned (v9-p5:68 step 5a, "the charge") |
| plead a case before a court | RHET:285-294 §7.2-7.3; COMP-1:432-456 §2.10 (Duel of Wits); XSC:491-501 §5.1 move menu | planned (SC-01 step 12, `speak`) |
| testify, give evidence | RHET:289 §7.2 (graded proof hierarchy); XSC:499 §5.1 *evidence* move | designed (v2-p8:434) |
| convene / hold a sitting | RHET:292-294 §7.3 (the venue is the engine: framing authority, order, decision rule); COMP-1:127-130 §2.2 (agenda control) | shipped (`convene`, thin) |
| judge, sentence | XSC:547-563 §5.5 (eight proceedings, each with an adjudicator) | shipped (`determine`) |
| vote, divide | RHET:279 §7.1 (*discessio*); COMP-1:111-130 §2.2 (Victoria 3 law enactment; division) | designed (v2-p8:435) |
| propose a motion | RHET:279 §7.1 (*relatio*: the presiding magistrate frames the question); COMP-1:127-128 | absent as a named act (an `utter` OUGHT exists, EI:884) |
| negotiate, bargain | COMP-1:491-502 §2.11 (Diplomacy, Pax Pamir positional pricing, Machiavelli bribery); RHET:313-325 §8.3-8.4; XSC:643 §6.3 *Negotiate* | designed (v2-p8:496, on FA's `covenant`) |
| arbitrate a dispute | XSC:555 §5.5 *Guild Arbitration* (panel adjudicator); ARR:94-106 `arbitration` row | shipped as an arrangement row |
| lie, deceive | COMP-1:458-464 §2.10 (Ace Attorney: a contradiction needs a lie to catch); COMP-1:491-494 (Diplomacy: the promise one breaks); [MEMORY] Blades in the Dark *Sway* includes lying | absent (gated on J-C-6) |

Not floor, kept only on NERS and precedent: confide, confess, counsel, warn/confront, swear (an oath
as proof), preach, mediate, adjourn, filibuster.

## 3.3 Suites

Seven suites. Fold test columns: **A** same actor? · **M** same subsystem mechanic (same effect body
and precondition)? · **P** differs only in a parameter or content? A fold passes on yes/yes/yes.

### Suite 1 — Telling (host `tell`)

What one person passes to another of what he holds. One row, one effect (WITNESS's told channel).

| folded act | A | M | P | the line |
|---|---|---|---|---|
| testify | y | y | y | `tell` whose `to` sits on the bench of a docketed matter; the told claim is the proof kind `testimony` (`rosters.yaml:2095`) |
| confess | y | y | y | `tell` whose subject is the teller's own deed; at a venue it is the proof `confession` |
| confide | y | y | y | `tell` under a visibility circle; the break is `confidence.broken` (VT:1013) |
| warn | y | y | y | `tell` to a person of a danger to him; content only |
| confront | y | y | y | `tell` with `to == subject` (VCD §6.8 reading, via SC-G41) |
| praise / flatter | y | y | y | `tell` of a favourable claim; *flatter* is the same content with `to == subject`. One content, two names a reader already uses |
| insult | y | y | y | `tell` of a disparaging claim to or about the hearer; `tell` already contests "a standing" (VT:1002), which is what an insult is about |
| counsel | y | y | y | `tell` whose subject is an OUGHT Proposition the teller holds (a course of action already declared, by him or anyone). v2's "`tell` + `utter`" (v2-p8:439) is a composition and fails A/M; this reading needs no second act inside counsel |
| deny / confirm a rumour | y | y | y | `tell` of the contrary or the same claim; no name is kept (the register's own refusal, SC-G40) |

- **World effect.** The hearer holds the told claim with the teller on its chain; a broken circle
  emits `confidence.broken`. `tell` writes nothing (VT:1003-1007; VT:1061, "deposits at WITNESS, not here").
  **Lacks:** a regard or slant reader (H-194, H-196), so praise, flattery and insult move nothing a
  person later reads; the teller's standing in the obstacle (SC-G21); a hearer competence carrier
  (SC-G22); a bench reader of told claims (proofs).
- **NERS.** **N** HOLDS, NARROWED, in all six directions: it is the only act that moves a claim a
  person holds *in memory* to another person (v2-p3:324 [carried, not re-run]); a document's terms
  also move, by `give` and the content deposit to a new holder (VT:160 note), so `tell`'s N-line is
  the unwritten claim — rumour, report, confidence; top-down (a lord briefs a reeve), bottom-up
  (a reeve reports), lateral (gossip), diagonal (a spy to a foreign head), vertical (news crossing a
  rung), horizontal (across factions). False-N attack: `issue` and `give` move a document's terms,
  not a remembered claim, and witnessing moves only co-located events; none carries a claim the
  hearer did not see and no document holds. **R** R-WORLD holds (rumour chains, broken confidences emerge unwatched); R-PLAYER is the
  core social choice, but its contents are *paper* until the valence reader exists. **S** one
  contest engine for every telling; defect: two readings of standing (SC-G21). **E** one row hosts
  nine named contents and adds no row: high ratio.
- **Precedent.** XSC:639-642 §6.3 (*Converse*, *Impress*, *Rumour*); [MEMORY] Crusader Kings 3
  secrets learned and exposed by characters.
- **Gaps closed:** SC-G17 (testimony half), SC-G40, SC-G41, SC-G42 (flatter, praise, insult,
  counsel), SC-G56, SC-G58. **Left open:** SC-G21, SC-G22 (§3.7).
- **Disposition.** `tell` **KEEP-AS-IS**, one REBUILD of a column: `beneficiary: subject` names the
  topic since T4 (SC-G58); take `to`, `give`'s precedent (VT:416) [CONFIDENCE: medium — flattery
  benefits the teller; `none` with a note is the alternative]. All nine contents **FOLD**.
  *Falsifier:* a second shipped row that moves a remembered (undocumented) claim between persons would make the N-line false.
- **Why `tell` carries no value cell.** `rosters.yaml:2612-2617` leaves `tell` uncelled *by design*:
  "testimony's moral weight is in WHAT is told", and telling is driven by regard. So the chooser picks
  praise over insult by the sign of regard, which is the right driver; this is why these contents
  need no own rows (contrast `lie`, Suite 7).

### Suite 2 — Persuasion (host `persuade`, the planned `argue` renamed)

Dyadic: one person changes what another *wants*. Planned at v9-p5:64 (IN-12 step 9, `argue`); writes
`Person.pursuits`, whose matrix row says it moves "by argument and consequence, never by evidence"
(`write_matrix.yaml:184`) and whose one missing producer is this act (`:186`, H-62).

| folded act | A | M | P | the line |
|---|---|---|---|---|
| argue (the name) | y | y | y | renamed, not folded: the same planned row. *Argue* names giving reasons; the row also takes appeals |
| manner `reason` | y | y | y | a `manner` operand: the obstacle reads the claims the hearer holds against the course; on success the hearer also holds the speaker's reasons (citable later) |
| manner `appeal` | y | y | y | the obstacle reads the hearer's regard for the speaker; on success pursuits move and no claim is deposited, so a later `reason` can undo it [ASSUMPTION: the two manners differ in what they leave, per COMP-1:449-451's rule that manoeuvres must differ in "what they change about the state", not in damage] |
| preach | y | y | n | the audience is a *set* of hearers, which no operand carries: **PARK**, trigger: a writer over a set of hearers (H-62); revival: an audience operand on `persuade` (v2-p8:436) |

- **World effect.** `pursuit.moved` on the hearer (`write_matrix.yaml:185`). **Lacks:** the row
  itself, the operand saying which weight moves and toward what (SC-G34), the manner operand.
- **NERS.** **N** HOLDS: cut it and `Person.pursuits` has no writer at all (H-62,
  `write_matrix.yaml:186`) and convictions move only by the scar crisis (`:195`), so nobody can talk
  anybody round; the convert, the turned envoy and the
  persuaded heir die. Directions: lateral (peer), top-down (lord and vassal), bottom-up (a
  counsellor and his king), diagonal (an envoy and a foreign noble); the vertical and horizontal
  reach run through SE-06's cohort pursuits (v9-p6:212). False-N attack: `tell` moves claims, and the
  matrix forbids evidence from moving pursuits, so `tell` cannot carry this. **R** R-WORLD: defections
  and conversions with no player present; R-PLAYER: the manner is a real choice only if the two
  manners leave different states (above). **S** same σ engine; one writer of the field, with crisis
  the only other. **E** one planned row, one rename, one park.
- **Precedent.** COMP-1:432-442 §2.10 (Duel of Wits binds public performance, not belief — which is
  why the public half is `speak`, Suite 6, and this dyadic half moves belief); RHET:353-355 §9.4
  (dyadic and public persuasion are different arts); [MEMORY] Blades in the Dark *Sway*; [MEMORY]
  Crusader Kings 3 *Sway* scheme.
- **Gaps closed:** SC-G34 (once the row lands), SC-G43 (parked), SC-G50 (answered: the split *is*
  dyadic `persuade` vs public `speak`, on RHET:355's own finding). **Left open:** none beyond the row.
- **Disposition.** **NEW ROW** (the planned position, renamed `persuade`; no hash has been moved by
  the name). *Falsifier:* a shipped row already writing `Person.pursuits` for a named hearer.

### Suite 3 — Declaration (host `declare`, the shipped `utter` renamed)

Putting a proposition on the record. `_eff_utter` (EI:857-891) mints an immutable Proposition with a
`mood` and the declarer's `hold`.

| folded act | A | M | P | the line |
|---|---|---|---|---|
| propose (a motion, a course) | y | y | y | mood `OUGHT` (the effect's default, EI:884). The motion a sitting votes on is this Proposition |
| allege (the public half of a charge) | y | y | y | mood `HOLDS`, `subject` the accused. The *complaint to a seat* is `petition` (Suite 5); this is the claim others may publicly `commit` to |
| threaten | y | y | y | mood `THREAT`, `subject` the threatened. Uncontested: a threat is cheap talk until someone acts on it |
| declare war (FA) | y | y | y | mood `WAR` (`queries/faction_q.py:216`); FA's preset, named here only because the rename absorbs it |

- **World effect.** A Proposition (`proposition.uttered`, renamed `proposition.declared` with the row)
  and the declarer's hold. **Lacks:** a mood source for a computed act — every computed declaration
  is a content-free OUGHT (SC-G36); an audience (a Proposition has no place, EI:870-871); a reader of a
  THREAT in the threatened person's choice; `at_war` is unread (v2-p8:342).
- **NERS.** **N** HOLDS: the only creator of a Proposition (VT:1277), which `commit` requires
  (VT:132-136; W3 also named `petition` and `issue`, whose cells have since changed). Cut it: no motion, no vote, no war, no cause to swear to. All six directions
  (a Proposition has no place, so it is indifferent to scale). **R** R-WORLD: declared wars and
  threats throw hooks; a threat with no reader is *paper*. **S** one mint, four moods; one mood-keyed
  alignment cell must serve WAR, the charge and THREAT (v2-p8:635, D-V6) — two ladders for one
  quantity otherwise. **E** one row, four named contents.
- **Threat: contest or cheap talk?** v2 asks whether a threat contests the addressee's nerve
  (v2-p8:664, SC call 5). Answered by precedent, not escalated: COMP-1:491-494 (Diplomacy: binding is
  "the expensive exception"; promises and threats are cheap talk), and ED-IN-0210 ruling 1 ("verbs are
  not fiats", quoted at VT:178): the threatened person bends by *his own* choice reading the threat's
  credibility (the threatener's standing, a force mustered), not by a roll that moves him. The reader
  is the missing mechanic (§3.7).
- **Precedent.** RHET:279 §7.1 (*relatio* frames the question); COMP-1:491-494 §2.11; [MEMORY]
  Blades in the Dark *Command*.
- **Gaps closed:** SC-G31 (the producer half), SC-G36 (once a mood source exists), SC-G42 (threaten).
- **Disposition.** `utter` **REBUILD**: rename to `declare` (L-13, §3.5); land the rename with the row's
  next hash move, K-24's precedent (VCD:2759, via SC-G07). Contents **FOLD**. *Falsifier:* a second
  creator of a Proposition.

### Suite 4 — Binding oneself (host `commit`, shared with FA and NP)

| folded act | A | M | P | the line |
|---|---|---|---|---|
| vote | y | y | y | the member's `commit` to the motion's Proposition at a sitting; the count is `determine`'s (SC-01 step 11, v9-p6:60) |
| swear (an oath) | y | y | y | `commit` to a HOLDS Proposition at a venue; the proof kind `oath` (`rosters.yaml:2095`) |

- **World effect.** A `commit` Tenure (`commitment.made`, VT:138-139); `release` ends it with
  `commitment.ended` (VT:853). **Lacks:** the `cardinality` count (`data/requires.py` raises on it,
  v9-p6:60); a reader of an oath as proof.
- **NERS.** **N** HOLDS (FA owns the war half; SC's half is the vote). **R** a division is the
  assembly's choice point; **S** one count for a bench vote and an election (`confer`'s `elected`
  basis, GV-G44) or S fails; **E** zero rows added.
- **Precedent.** RHET:279 §7.1 (*discessio*); COMP-1:111-130 §2.2; V-v2claims "vote → commit" upheld
  (*votum* 'vow').
- **Gaps closed:** SC-G25 (once the count exists), SC-G52 (swear half).
- **Disposition.** `commit` **KEEP-AS-IS** (owner flagged, §3.8); vote and swear **FOLD**.

### Suite 5 — Petition and complaint (hosts `petition`, `lodge`)

The seatless person's upward channel: ask a seat, accuse before it, and put the matter before a room.

| folded act | A | M | P | the line |
|---|---|---|---|---|
| accuse (lay a complaint) | y | y | y | `petition` whose `terms` name the accused; v9-p5:68 (step 5a, RS-23) already reads such a petition as "a computed charge". L petītiō is itself "an attack in words before a court" (L&S) |
| supplicate | y | y | y | the same act in a humble register: content only, and an ordinary synonym, so the name is **CULLED** |
| deny (the receiver's answer) | y | y | y | not a fold into `petition`: the receiver's `release` of the `hold` he received by `give` (v2-p8 §V.2.3; ED-IN-0210 Ruling 2's own word, VT:821). Owned by `release` |
| withdraw (the petitioner's) | y | y | y | the petitioner's `release` of his own petition `hold`. Owned by `release` |
| carry → `lodge` | — | — | — | not a fold: `lodge` is its own row (different effect: the docket append; actor: any holder) |

- **World effect.** `petition`: a `petition` Record held by the petitioner, `to` a Person, `from` a
  Rung (VT:805-827). `lodge`: the petition's stages re-wound and a docket item naming it (EI:300-).
  **Lacks:** a petition addressed to someone other than its subject — `to` and `subject` bind one
  referent (H-94; VT:821), so a complaint is addressed to the accused (SC-G03, SC-G05); the
  rank-indexed form and an intercessor's weight (SC-G06, SC-G16); an arrangement for a lodged matter
  (`_docket_item(<terms>, None, …)`); a public route for a denial after SC-01 step 13 (D-V3).
- **NERS.** `petition` **N** HOLDS: the only act by which a person without a seat asks anything of
  one; the bottom-up direction is the one most systems lack, and RHET:359 §9.5 tested that no such
  subsystem existed before it. v2's merge into `create_record` (v2-p3:329) loses the counterparty
  `to` and with it the receiver's `deny`. `lodge` **N** HOLDS: cut it and only a seat can docket
  (`open_case`'s remit); v2's "`give` to the docket" fails, since `give` needs a receiving *person*
  present (VT:413-419). **R** R-WORLD: a hearer whose regard for a killer moved files against him and
  the case reaches a docket unwatched (v9-p5:67, step 5's EXIT) — the subsystem's showcase hook;
  R-PLAYER: whom to petition and whose hand carries it (RHET:305: "*who carried the petition*
  shaped its success"). **S** S-UP fails today (H-94); one mint (`_mint_document`) serves petition,
  case file and writ. **E** two rows, five named acts, one cull.
- **Precedent.** RHET:300-311 §8.1-8.2 (SC 8 petitions: complaints and requests; supplique and
  remontrance); XSC:553, :558 §5.5 (*Royal Audience*, *Personal Appeal*).
- **Gaps closed:** SC-G04 (deny, withdraw), SC-G07 (rename), SC-G52 (supplication half); SC-G03,
  SC-G05, SC-G06 once their mechanics exist. **Left open:** the remontrance as a second instrument
  (RHET:311) — an institution's petition is a `petition` from a seat-holder; no second row is
  proposed until a reader distinguishes it.
- **Disposition.** `petition` **KEEP-AS-IS** (reverses v2's merge). `carry` **REBUILD**: rename
  `lodge`, kind `petition.lodged` (L-04: *carried* means *adopted*). accuse **FOLD**; supplicate
  **CULL**; deny, withdraw **FOLD** into `release` (owner outside SC). *Falsifiers:* `petition` — a
  computed `create_record` that reaches a receiver able to deny it; `lodge` — a seatless docketing by
  any other row.

### Suite 6 — The sitting (hosts `convene`, `open_case`, `speak`, `determine`)

The venue is the engine (RHET:294): who sets the sitting, how a matter reaches it, what is said, who
decides and what the decision writes.

| folded act | host | A | M | P | the line |
|---|---|---|---|---|---|
| adjourn | `convene` | y | y | y | a further `Date` for a matter already before the room; the chair is `convene`'s actor (`remit:convene`) |
| plead | `speak` | y | y | y | a party speaking at his own docket item; content kind |
| refute | `speak` | y | y | y | speech kind `cite_incompatible` (ARR:65) |
| concede | `speak` | y | y | y | speech kinds `concede_fact`, `concede_harm` (ARR:73, :77) |
| deny the fact | `speak` | y | y | y | speech kind `deny` (ARR:61), renamed `deny_fact` to pair with `concede_fact` and to free the verb `deny` for the petition (§3.5); the id is also `rosters.yaml: ladder_rungs`' (ARR:46-49), so both move |
| impugn | `speak` | y | y | y | speech kind `impugn_motive`, Partial by construction (ARR:69-72) |
| object (to the venue) | `speak` | y | y | y | a new speech kind for the translative stasis, "is this the right venue" (RHET:95): the challenge-as-objection |
| define | `speak` | y | y | y | a new speech kind for the definitional stasis ("granted the act, is it *this* crime?", RHET:93). With `object`, the four stases each have a kind; the ten-kind design's `construe` *as a speech kind* is this one, renamed so the word `construe` stays the GV verb |
| arbitrate | `determine` | y | y | y | `determine` under the `arbitration` row (ARR:94-106), whose disposal is a binding `oblige` (V-04) |
| vote | `commit` | — | — | — | Suite 4 |
| mediate | — | — | — | — | not arbitration (V-04): a non-binding go-between under `negotiation` (`disposal: mutual`), which is unseeded (ARR:24): **PARK**, trigger SC-04 seeds `negotiation` |
| negotiate | FA `covenant` | — | — | — | the offer of terms is FA's `covenant` (v2-p8:496); SC hosts only the `negotiation` sitting: **PARK** with mediate |
| interrogate | FI | — | — | — | questioning a person in custody; flagged to FI (§3.8) |
| filibuster | `speak` | y | y | n | needs a clock the provider lacks (SC-G48): **PARK**, trigger: a turn limit in the SC-01 provider |

- **World effect.** `convene`: `Date.due_at` with no holder, so dates fire vacant (VT:194;
  v9-p6:97). `open_case`: a case file and a docket item naming arrangement and petition, both `None`
  when computed (EI:243-272). `speak`: nothing today (VT:929). `determine`: the docketed row's
  disposal Tenure on a Person, matter removed (VT:253-254). **Lacks:** a Date holder (SC-G28); an
  arrangement for a computed case (SC-G01/G02); the contest provider, obstacle ceiling and prize
  (SC-01 steps 12-15; SC-G11, SC-G20); an `issue` (stasis rung) carried on the docket item, which
  speech kinds move and which persists between sittings (SC-G12, SC-G13, SC-G29); a reader of
  speech kinds and proofs (SC-G14, SC-G17); `Tenure.degree` (SC-03b, SC-G24); a `Record` disposal,
  without which the parliamentary and council rows can decide nothing (ARR:122, :144;
  `state/gate.py:255-257`).
- **NERS.** `determine` **N** HOLDS, NARROWED: the only writer of a disposal (`oblige`, `detain`, `ban`) *by a
  bench*; the warrant basis lets GV's planned `arrest` open a `detain` too (`state/gate.py:258-262`),
  so the N-line is judgment, not custody; cut it and no court binds anyone (top-down, vertical). `open_case` **N** HOLDS: the seat's
  own-motion route (RHET:290, the *inquisitio*) and the interval between charge and judgment others act
  in (v2-p3:328); false-N attack via `lodge` fails because `lodge` needs a petition someone filed.
  `convene` **N** HOLDS, NARROWED: the only writer of a sitting's time, but its dates fire vacant, so
  today nothing depends on it (*paper* until the fired-slot step, v9-p6:97-99). `speak` **N** today
  **FALSE** (writes nothing; a portrait), kept because pleading a case is floor and SC-01 step 12
  builds it contested on "a matter" (v9-p6:65). **R** R-WORLD: trials raised by petitions with no
  player (step 5's EXIT). R-PLAYER: the speech kind is the choice; COMP-1:444-456 warns that a menu
  differing only in damage collapses to two moves, so each kind must move a different state: `deny_fact`
  and `object` hold the `issue` rung, `define` moves it to the definitional rung, `cite_incompatible` raises the opponent's obstacle, `concede_*`
  caps the reachable band in exchange for a lower rung, `impugn_motive` is capped at Partial (ARR:72).
  [ASSUMPTION: these state differences — basis: the stasis ladder, RHET:88-99 and :351, read as a
  terrain the kinds move on.] **S** the sitting is where the season pauses for a proceeding: the
  provider resolves the exchanges inside one act and returns a margin (v9-p6:76), so no DELIBERATE
  nests inside RESOLVE (H-56's held half) and a matter that runs on is adjourned with its rung kept.
  S-UP fails today for every deliberative row (no Record disposal). **E** four hosts, ten folded names,
  one renamed speech kind, two added (`object`, `define`), no new row.
- **Precedent.** RHET:277-294 §7 (relatio, sententiae by rank, discessio; *libellus* →
  *litis contestatio* → proof → verdict); COMP-1:107-151 §2.2 (agenda control, recorded defeat);
  COMP-1:430-456 §2.10 (Duel of Wits; menu collapse); XSC:547-563 §5.5 (eight proceedings).
- **Gaps closed:** listed per row in §3.6.
- **Disposition.** `convene` **KEEP-AS-IS** (REBUILD only by the planned Date holder). `open_case`
  **KEEP-AS-IS**. `speak` **REBUILD** (SC-01 step 12; contents fold). `determine` **REBUILD**: add a
  `Record` disposal (§3.7). *Falsifiers:* `determine` — any other row opening a disposal Tenure;
  `open_case` — a seatless route that dockets without a petition; `speak` — if after SC-01 step 12
  `speak` still writes nothing, the KEEP was wrong.

### Suite 7 — Deception and the record (no host; `lie` parked, `forge` kept)

| act | form | the line |
|---|---|---|
| lie | **PARK** on J-C-6 | a `tell` whose said claim the teller does not hold. Mechanically a fold (A, M, P all yes); held as its own row only because the value term reads the verb alone (v2-p8 §V.2.1), so a lie folded into the uncelled `tell` would carry no moral weight. Revival: a row sharing `tell`'s cell and **emitting `tell`'s kinds** — never a `lie.*` kind, or every witness learns it was a lie, the leak L-11 found in `record.forged` |
| forge | **KEEP** (shipped, VT:330) | the documentary lie, which already ships. Its `forgery_quality` is read by nothing (SC-G39); the bench's proofs reader is where it must be read |
| construe | out of SC | interpreting a writ's terms is the receiver's answer to an order, GV's `comply` suite (VT:840: "the triple is now comply / evade / defy / construe"); ruled neutral, so it is **not** gated on J-C-6 (contra v2-p8:246) |
| suborn | FA | an inducement to an unlawful act (V-05); its perjury form waits on `lie` |

- **What SC needs if persons may lie** (J-C-6, D-V4): (1) the `lie` row above, its own alignment
  cells, `tell`'s kinds; (2) the said claim is made, not held — WITNESS deposits it in the hearer's
  ledger exactly as a told one; (3) something that can find it out: the bench's proofs reader
  weighing testimony against a held `record` or a `confession` (the mirror test, SC-G17),
  `interrogate`'s confession, and a contradiction a later teller tells. Without (3) a lie is
  undetectable and costs nothing. **The asymmetry today:** `forge` ships, so the world is already
  foolable by documents and not by speech — two answers to one question (S).
- **Precedent.** COMP-1:458-464 §2.10 (Ace Attorney: a contradiction needs a lie to catch);
  COMP-1:491-494 (Diplomacy: lying is the game).
- **Gaps closed:** SC-G37 and SC-G38 dispositioned (§3.6); SC-G39 once the proofs reader exists.

## 3.4 Lexicon table

Sources: **L&S** = Lewis & Short via `etym_tool.py ls`; **Wikt** = en.wiktionary via `etym_tool.py en`
/ `la` (it cites De Vaan's EDL, OED and others; quoted here as Wiktionary). A PIE root Wiktionary's
template dropped in the tool's output is marked `[UNVERIFIED]`. Germanic words are not routed
through Latin. Fit is ordinary current usage (ED-IN-0179), judged apart from the root.

| verb | suite | status | mechanic · world effect | etymology | fit | rename |
|---|---|---|---|---|---|---|
| `tell` | 1 | SHIPPED | contested on "a standing" vs `to`; told claim deposited at WITNESS with the teller chained; `news.told`, `confidence.broken` | ME *tellen* ← OE *tellan* ← PGmc *\*taljaną* ← *\*talą, \*talō* 'number, tale' ← PIE *\*del-* (o-grade *\*dol-*) [Wikt]. Germanic; no Latin path | FITS — to tell someone something is exactly the act | — |
| testify | 1 | FOLDED → `tell` | `tell` to a bench member at a docketed matter; proof `testimony` | ME *testifien* ← OF *testifier* ← L *testificor, -ārī, -ātus sum* (dep. 1) 'to bear witness, give evidence, attest, testify' [L&S] ← *testis* 'witness' ← *\*terstis* 'a third party standing' ← PIE *\*tréyes* + *\*steh₂-* [Wikt] | FITS — giving evidence before a tribunal | — |
| confess | 1 | FOLDED → `tell` | `tell` of one's own deed; proof `confession` | ME *confessen* ← AN/OF *confesser* ← L *cōnfessus*, pp. of *cōnfiteor, -ērī, cōnfessus sum* 'to acknowledge, confess, own, avow (a fact previously denied or doubted)' [L&S] ← *con-* + *fateor* ← PIE *\*bʰeh₂-* 'to speak' [Wikt la] (the stem *fat-* itself 'seemingly' from *\*bʰh₂-tó-s* or *\*bʰh₂-t-*) | FITS | — |
| confide | 1 | FOLDED → `tell` | `tell` under a visibility circle (G6) | early 17th c. ← Middle Scots *confide, confyde* ← L *cōnfīdō, -ere, cōnfīsus sum* 'to trust confidently in, rely upon' [L&S; Wikt for date] ← *fīdō* ← PIE *\*bʰeydʰ-* [Wikt]. 'Tell in confidence' is the English development [date UNVERIFIED] | FITS | — |
| warn | 1 | FOLDED → `tell` | `tell` of a danger to the hearer | ME *warnen* ← OE *warnian* ← PGmc *\*warnōną* ← PIE *\*wer-* [Wikt]. Germanic | FITS | — |
| confront | 1 | FOLDED → `tell` | `tell` with `to == subject` | MF *confronter* ← ML *confrontō* ← *con-* + *frōns* 'forehead, front' [Wikt]; ML sense [UNVERIFIED] | FITS | — |
| praise | 1 | FOLDED → `tell` | `tell` of a favourable claim; needs the slant/regard reader (H-196, H-194) | ME *praisen* ← OF *preisier* ← LL *pretiō* 'to prize' ← L *pretium* 'price, value' [Wikt] ← Proto-Italic *\*pretjom* ← *\*próti* ← PIE *\*per-* 'in front' [Wikt la]. Latin 'value' → English 'commend' | FITS | — |
| flatter | 1 | FOLDED → `tell` | as praise, `to == subject` | ME *flateren*, probably OE *floterian* 'flutter' (PGmc *\*flutrōną* ← PIE *\*plewd-*) conflated with ON *flaðra* 'fawn'; later associated with OF *flater* [Wikt]. Germanic, disputed | FITS (floor *charm*) | — |
| insult | 1 | FOLDED → `tell` | `tell` of a disparaging claim; same reader as praise | MF *insulter* or L *īnsultō, -āre, -āvī, -ātum* 'to leap at; (trop.) to scoff at, revile, abuse, taunt, insult' [L&S] ← *īnsiliō* ← *in-* + *saliō* 'leap' ← PIE *\*sel-* [Wikt] | FITS | — |
| counsel | 1 | FOLDED → `tell` | `tell` whose subject is an OUGHT Proposition the teller holds | ME *counseilen* ← OF *conseillier* ← L *cōnsilior, -ārī* 'to take counsel; (alicui) to give counsel, advise' [L&S] ← *cōnsilium*, of unknown origin: either *com-* + *calō* (PIE *\*kelh₁-*) or *cōnsulō* 'consider, deliberate' [L&S] (PIE *\*selh₁-*) [Wikt] | FITS | — |
| `persuade` | 2 | NEW (planned `argue`, renamed) | contested; writes the hearer's `Person.pursuits` (`pursuit.moved`); `manner` reason/appeal | directly (Wikt en: "From L *persuādeō*"; no French intermediate) ← L *persuādeō, -ēre, persuāsī, persuāsum* 'to bring over by talking, to convince of the truth of anything, to persuade' [L&S] ← *suādeō* 'to recommend, advise; urge' ← PIE causative of *\*sweh₂d-* 'sweet' [Wikt; 'make sweet' is the reconstructed causative, not an attested Latin sense — L-01 is right that it is no gloss] | FITS — the convention verb for the attempt in games | — (it *is* the rename) |
| argue | 2 | CULLED (renamed `persuade`) | — | ME *arguen* ← OF *arguer* ← L *arguō, -ere, -uī, -ūtum* 'to make clear, show, prove, declare; to accuse, charge with' [L&S] ← probably PIE *\*h₂erǵ-* 'bright, white' (disputed) [Wikt la] | STRAINED — names giving reasons (or quarrelling); the row also takes appeals | `persuade` |
| preach | 2 | PARKED (audience operand) | would be `persuade` over a set of hearers | ME *prechen* ← OF *preechier* ← L *praedicō, -āre, -āvī, -ātum* 'to cry in public, publish, proclaim' [L&S] ← *dīcō* ← PIE *\*deyḱ-* 'show' [Wikt] | FITS | — |
| `declare` | 3 | SHIPPED as `utter`, renamed | mints an immutable Proposition with a mood + the declarer's `hold` (EI:857-891) | ME *declaren* ← OF *declarer* ← L *dēclārō, -āre, -āvī, -ātum* 'to make clear, plain, evident; show, manifest, declare; (public law) to announce as elected' [L&S] ← *clārus* 'clear; loud, distinct' ← PIE *\*kelh₁-* 'call' [Wikt] | FITS — declare war, declare a fact, declare an intention | — (it *is* the rename) |
| utter | 3 | SHIPPED, rename proposed | as `declare` | ME *outren/utteren*, partly from ME *utter* 'outer' (OE *ūtera* ← *ūt*) and partly MDu *uteren* / MLG *üteren* 'make known' ← PIE *\*úd* 'out' [Wikt]. Germanic | STRAINED — "utter" is to voice a sound or word; legally, to pass a forged instrument (L-13); the row makes no sound and leaves a record | `declare` |
| propose | 3 | FOLDED → `declare` | mood OUGHT; the motion | ME *proposen* ← AN *proposer* ← L *prōpōnō, -ere, -posuī, -positum* 'to put forth, set before, display; to propose (a question for answer)' [L&S], conjugation altered by OF *poser* [Wikt] ← *pōnō* ← *\*po-sinō* 'put away' [Wikt] | FITS | — |
| allege | 3 | FOLDED → `declare` | mood HOLDS, subject the accused | ME *aleggen* ← OF *alleguer* / AN *aleger*: the form perhaps from OF *esligier* (ML ← L *ex* + *lītigō*), the meaning from L *allēgō, -āre, -āvī, -ātum* (*ad* + *lēgō*) [Wikt]; *allēgō* 'to send one away with a commission, despatch, depute' [L&S]; L&S *allēgo* (key *allego1*) II: 'To bring forward, to relate, recount, mention, adduce' (post-Aug.), the 'cite, adduce' sense the meaning comes from [L&S] | FITS | — |
| threaten | 3 | FOLDED → `declare` | mood THREAT, subject the threatened; needs a reader | ME *thretenen* ← OE *þrēatnian* (← *þrēat* + *-en*) ← PIE *\*trewd-* [Wikt]. Germanic | FITS | — |
| `commit` | 4 | SHIPPED (shared) | opens a `commit` Tenure on a Proposition | ME *committen* ← L *committō, -ere, -mīsī, -missum* 'to join, put together; to entrust; (se committere) to entrust oneself' [L&S] ← *mittō* ← likely PIE *\*mey-* 'exchange' [Wikt] | FITS — commit oneself to | — |
| vote | 4 | FOLDED → `commit` | a member's `commit` to the motion; counted by `determine` | ← L *vōtum* 'vow' ← *voveō, -ēre, vōvī, vōtum* 'to vow, promise solemnly' [L&S] ← PIE *\*h₁wegʷʰ-* [Wikt]; doublet of *vow* | FITS | — |
| swear | 4 | FOLDED → `commit` | `commit` to a HOLDS Proposition at a venue; proof `oath` | ME *sweren* ← OE *swerian* ← PGmc *\*swarjaną* ← PIE *\*swer-*; "the original sense in all Germanic languages is 'to take an oath'" [Wikt]. Germanic | FITS | — |
| `petition` | 5 | SHIPPED | mints a `petition` Record held by the petitioner, `to` a Person, `from` a Rung | ME ← OF *peticiun* ← L *petītiō, -ōnis* 'an attack, thrust; (trop.) an attack in words before a court; a request, petition (post-Aug.)' [L&S] ← *petō, -ere, -īvī, -ītum* 'to fall upon; seek; ask, request; (law) to sue for' [L&S] ← PIE *\*peth₂-* 'fly' [Wikt] | FITS | — |
| accuse | 5 | FOLDED → `petition` | `petition` whose `terms` name the accused (step 5a, RS-23) | ME *acusen* (c. 1300) ← OF *acuser* ← L *accūsō, -āre, -āvī, -ātum* 'to call one to account, make complaint against, reproach' [L&S] ← *ad* + *causa*, which is of unknown origin [Wikt] | FITS | — |
| supplicate | 5 | CULLED | — | late ME ← L *supplicātus*, pp. of *supplicō, -āre* 'to kneel down, pray or beg humbly, beseech' [L&S] ← *sub* + *plicō* ← PIE *\*pleḱ-* 'fold' [Wikt] | FITS, but a synonym of petition in a register | — |
| deny | 5 | FOLDED → `release` (owner outside SC) | the receiver's `release` of the petition `hold` he got by `give`; earns a `petition.denied` kind [proposed] | ME *denyen* ← OF *denoier* ← L *dēnegō, -āre, -āvī, -ātum* 'to deny a thing (very rare); far more freq. and class.: to reject, refuse a request' [L&S] ← *negō* ← *ne* ← PIE *\*ne* [Wikt] | FITS — "the petition was denied"; the classical sense is this one | — |
| withdraw | 5 | FOLDED → `release` (owner outside SC) | the petitioner's `release` of his own petition `hold` | ME *withdrawen* ← *with-* 'away, back' + *drawen* ← OE *dragan* ← PIE *\*dʰregʰ-* [Wikt]. Germanic | FITS | — |
| `lodge` | 5 | SHIPPED as `carry`, renamed | re-winds a held petition's stages; appends a docket item naming it (EI:300-) | ME *loggen* ← OF *logier* ← *loge* ← Frankish *\*laubja* (ML *laubia, lobia*) [Wikt]. Germanic through French; the 'lodge a complaint' sense is English [date UNVERIFIED] | FITS — one lodges a petition, a complaint, an appeal | — (it *is* the rename) |
| carry | 5 | SHIPPED, rename proposed | as `lodge`; emits `petition.carried` | ME *carien* ← AN *carier* ← L *carrus* 'wagon' ← Gaulish ← PIE *\*ḱers-* 'run' [Wikt] | MISFIT — transport; and "the petition was carried" means *adopted* (L-04) | `lodge` (`petition.lodged`) |
| `convene` | 6 | SHIPPED | writes `Date.due_at` and the convening condition (VT:194) | MF *convenir* ← L *conveniō, -īre, -vēnī, -ventum* 'to come together, meet together, assemble' [L&S] ← *veniō* ← PIE *\*gʷem-* 'come' [Wikt] | FITS | — |
| adjourn | 6 | FOLDED → `convene` | a further Date for a matter before the room; its rung kept | ME *ajournen* ← OF *ajorner*, from the phrase *a jor (nomé)* 'to an (appointed) day' [Wikt]; *jor* ← LL *diurnum* [Wikt fro *jor*] | FITS | — |
| `open_case` | 6 | SHIPPED | by `remit:determine`: a case file and a docket item (EI:228-296) | *open* ← OE *openian* ← adj. *open* ← PGmc *\*upanaz* ← PIE *\*upo* [Wikt]; *case* ← OF *cas* ← L *cāsus* 'a fall; event' ← *cadō, -ere, cecidī, cāsum* 'fall' ← Proto-Italic *\*kadō* ← PIE *\*ḱad-* (*\*ḱh₂d-*) 'to fall' [Wikt; LIV] | FITS — courts and constables open cases | — |
| `speak` | 6 | SHIPPED, REBUILD (SC-01 step 12) | today writes nothing; planned: contested on "a matter" at a docketed sitting, moving its `issue` rung | ME *speken* ← OE *specan*, an irregular alteration of *sprecan* ← PGmc *\*sprekaną* ← PIE *\*spreg-*; disputed (Hill sets up *\*bʰeh₂g-*) [Wikt]. Germanic | STRAINED today (no audience, no effect); FITS once it is speech to a sitting | — |
| plead | 6 | FOLDED → `speak` | a party's speech at his own docket item | ME *pleden* ← OF *plaidier* ← *plait* ← ML *placitum* 'opinion, determination; (a court, a suit)' ← L *placitum*, neut. pp. of *placeō* 'to please' [Wikt; L&S] | FITS | — |
| refute | 6 | FOLDED → `speak` | speech kind `cite_incompatible` | ← L *refūtō, -āre, -āvī, -ātum* 'to check, drive back; (trop.) to repel, oppose; refute' [L&S] ← *re-* + *\*fūtō*, disputed [Wikt] | FITS | — |
| concede | 6 | FOLDED → `speak` | speech kinds `concede_fact`, `concede_harm` | ME ← OF *conceder* ← L *concēdō, -ere, -cessī, -cessum* 'to go away, withdraw; to yield, grant, allow' [L&S] ← *cēdō*, derivation disputed [Wikt] | FITS | — |
| object | 6 | FOLDED → `speak` (new speech kind) | translative: the venue is wrong | ME *objecten* ← L *obiectus*, pp. of *obiciō, -ere, -iēcī, -iectum* 'to throw before, offer; to reproach, charge with' [L&S] ← *ob* + *iaciō* ← PIE *\*(H)yeh₁-* [Wikt] | FITS — "I object" | — |
| define | 6 | FOLDED → `speak` (new speech kind) | definitional: what the act is called | ME *definen* ← OF *definer*, var. of *definir* ← L *dēfīniō, -īre, -īvī, -ītum* 'to bound, set bounds to; to limit, terminate, define' [L&S] ← *dē* + *fīniō* ← *fīnis* 'end', origin disputed [Wikt] | FITS | — |
| `determine` | 6 | SHIPPED, REBUILD (Record disposal) | opens the docketed row's disposal Tenure on a Person by bench and quorum (VT:222-267) | ME *determinen* ← OF *determiner* ← L *dētermino, -āre, -āvī, -ātum* 'to enclose within boundaries, bound, limit; to fix, settle, determine' [L&S] ← *terminus* 'boundary' ← PIE *\*térmn̥* [Wikt la] | FITS — a court determines a case | — |
| arbitrate | 6 | FOLDED → `determine` | `determine` under `arbitration` (binding `oblige`) | ← L *arbitrātus*, pp. of *arbitror, -ārī, -ātus sum* 'to be a hearer, beholder; (judicial) to make a decision, give judgment' [L&S] ← *arbiter*, origin uncertain [Wikt] | FITS | — |
| mediate | 6 | PARKED (with `negotiation`) | a non-binding go-between; no disposal | verb 1538 [Wikt] ← LL *mediātus*, pp. of *mediō, -āre* 'to halve; to be in the middle' (post-class.) [L&S] ← *medius* ← PIE *\*médʰyos* 'between' [Wikt la] | FITS | — |
| negotiate | 6 | PARKED (SC side; FA hosts) | the offer of terms is FA's `covenant` | c. 1598 [Wikt] ← L *negōtiātus*, pp. of *negōtior, -ārī* 'to carry on business, trade, traffic' [L&S] ← *negōtium* ← *nec* + *ōtium* 'leisure' [Wikt]. The diplomatic sense is English | FITS | — |
| filibuster | 6 | PARKED (a clock) | a speech kind spending the sitting's clock | ← Sp. *filibustero* ← F *flibustier* ← Du. *vrijbuiter* 'freebooter' (*vrij* + *buit* + *-er*; *vrij* ← PIE *\*preyH-*), conflated with Du. *vlieboot* [Wikt]. Not Latin | FITS (legislative sense) | — |
| interrogate | 6 → FI | PLANNED (v9-p5:67) | questioning under custody; `confession.made` | ← L *interrogātus*, pp. of *interrogō, -āre* 'to ask, question, inquire, interrogate' [L&S] ← *rogō* 'ask' ← PIE *\*h₃reǵ-* 'stretch' [Wikt] | FITS | — |
| lie | 7 | PARKED (J-C-6) | `tell` of a claim not held; `tell`'s kinds; own cells | ME *lien* ← OE *lēogan* ← PGmc *\*leuganą* ← PIE *\*lewgʰ-* [Wikt]. Germanic | FITS | — |
| `forge` | 7 | SHIPPED | mints a Record on what the forger heard of; quality unread | ME *forgen* ← OF *forgier* ← L *fabricor, -ārī, -ātus sum* (also *fabricō, -āre*) 'to frame, forge, construct' [L&S] ← *fabrica* 'workshop' ← *faber* 'artisan', origin uncertain [Wikt la] (the verb path, per L-11) | FITS — forge a document | — |
| `construe` | 7 → GV | SHIPPED (`absent`) | the receiver's reading of a writ; writes nothing | ME *construen* ← LL *cōnstruō* (gramm. 'to connect grammatically', Priscian) ← L *cōnstruō, -ere, -strūxī, -strūctum* 'to heap together; to construct, build' [L&S] ← *struō* ← Proto-Italic *\*strowō* ← PIE *\*strew-*, cognate with *strew* [Wikt] | FITS — to construe a text is to interpret it | — |
| `challenge` | PC | SHIPPED | call to a duel; mints nothing today (VT:596-616) | ME *chalenge* ← OF *chalengier*, *chalonge* ← L *calumnia* 'trickery, false accusation' (*calumnior* 'to accuse falsely', L&S), origin uncertain [Wikt] | FITS for a duel; its old 'accuse' sense is not current | — |

## 3.5 Deduplication and culls

**Near-synonym groups and what was done.**

| group | ordinary-usage overlap | resolution |
|---|---|---|
| `speak` / `utter` (/ `tell`) | *speak* and *utter* are ordinary synonyms (L-13) | split by mechanic, then by word: `tell` = to one person, moves a claim; `speak` = to a sitting, contested, moves a matter; `utter` renamed **`declare`** = puts a Proposition on the record. `speak` keeps its name (plain, floor: "speak in the assembly"); `utter` is the one renamed because its word is the weaker fit (voicing a sound; passing a forged note) |
| `argue` / `persuade` / `preach` | *argue* = give reasons; *persuade* = bring someone round by any means; *preach* = to many | one row, named **`persuade`**; *argue* is not kept as a second name (its reason-only sense is the `manner: reason` value); `preach` parked as the many-hearer case |
| `petition` / `supplicate` / `accuse` / `plead` | *supplicate* and *petition* differ only in register; *plead* also means *beg* | `supplicate` **CULLED**; `accuse` is `petition` content (a complaint); `plead` is kept only in its court sense, under `speak` |
| `deny` (three senses) | deny a request; deny a fact; deny a rumour | the petition answer keeps **`deny`** — ED-IN-0210 Ruling 2's own word (VT:821) and *dēnegō*'s classical sense (L&S: "far more freq. … to reject, refuse a request"); the speech kind `deny` (ARR:61) is renamed **`deny_fact`**, pairing `concede_fact`; the rumour denial is unnamed `tell` content (SC-G40) |
| `praise` / `flatter` | flattery is praise aimed at the hearer | one content of `tell`, two names distinguished by `to == subject`; kept both because *flatter* is the floor act (*charm*) and *praise* is the third-party act. No row; one valence reader serves both |
| `mediate` / `arbitrate` | V-04: mediation is non-binding, arbitration binding | **applied**: `arbitrate` folds into `determine` under the `arbitration` row (binding `oblige`); `mediate` is **PARKED** with `negotiation`. v2's "mediate → `convene`" (v2-p8:440) also fails the fold test: `convene` sets a date and decides nothing |
| `convene` / `covenant` | V-19: both ← *conveniō* | **answered, kept apart**: in current use *convene* is to assemble, *covenant* to bind by agreement; no reader confuses them; a shared root is not evidence (L-01) |
| `object` / (`reject`) | both ← *iaciō* | only `object` is used (a speech kind); no collision |
| `challenge` / `accuse` | K-23's "what marks a petition as a challenge rather than an accusation" | `challenge` is PC's duel (VT:596); accusation is `petition` content; challenging *the venue* is the speech kind `object`. Three acts, three words |
| `testify` / `confess` / `swear` / `forge` | four ways evidence enters | they map one-to-one onto the shipped proofs roster `record, testimony, oath, confession` (`rosters.yaml:2095`): testimony and confession are `tell`, oath is `commit`, record is any Record (a forged one included). One reader (§3.7 M9) weighs all four |
| `lodge` / `give` / `carry` | handing a document on vs putting it before a room | `give` hands a petition to a person (an intercessor); `lodge` (ex-`carry`) puts it on the docket. Different effects, kept apart |
| `vote` / `swear` / `commit` | binding oneself | both fold into `commit`; L-02's proposed rename of `oblige` to *swear* would collide with the oath — recommend *pledge* there (§3.8) |

**Culls, with the fold test and the floor check.**

| culled | fold test (A/M/P) | what dies | floor check |
|---|---|---|---|
| `supplicate` (name) | y/y/y into `petition` | a register word | nothing a floor act needs dies: *petition the ruler* stays a shipped row |
| `argue` (name) | the same planned row | a second name for one act | *persuade* is the floor word and the host |
| `utter` (name) | the same shipped row | a strained word | the Proposition and every mood survive under `declare` |
| `carry` (name) | the same shipped row | a false friend (*carried* = adopted) | the seatless route to a docket survives as `lodge` |

**v2 dispositions reversed or changed here.** `petition` and `carry` "standing as filed" as merges into
`create_record` and `give` (v2-p3:329-330; v2-p8:248): **reversed** — each loses its counterparty or
its effect (Suite 5). V119 persuade → `argue`: **direction reversed** (the host is named `persuade`).
V129 insult PARK: **reversed to FOLD** — insult is floor, `tell` already contests a standing, and
`tell` is uncelled by design so a content needs no row (`rosters.yaml:2612-2617`); only the reader is
missing. V131 counsel "`tell` + `utter`": **re-targeted** to `tell` alone (a composition fails the fold
test). V132 mediate → `convene`: **reversed** (V-04). `construe` "held on J-C-6" (v2-p8:246):
**reversed** — it is interpretation, ruled neutral (VT:840), and leaves SC for GV. Upheld: V120 plead,
V121 threaten, V122 flatter, V124 refute, V125 concede, V126 testify, V127 vote, V128 preach (PARK),
V130 praise, V073 withdraw, V074 deny, V075 lie (PARK; one condition added: `tell`'s kinds).

**Critic findings on SC verbs.**

| id | finding | here |
|---|---|---|
| L-01 | root sense used as design intent | **applied**: no merge, gap or node here rests on a root. Partly answered on *persuade*: Wiktionary itself records "make sweet" as the reconstructed causative's literal sense; it is still no gloss, and the attested sense (L&S) is the one given |
| L-04 | `carry`'s `petition.carried` reads as *adopted* | **applied**: `lodge`, `petition.lodged` |
| L-11 | `record.forged` leaks the forgery to every witness | **applied** to `lie`'s revival form (emit `tell`'s kinds). The `forge` leak itself is FI/EC's to repair; flagged |
| L-12 | the earlier pass is stale (carry built; challenge, accept unjudged) | **applied**: `carry` read as built (VT:126); `challenge` judged (§3.4) |
| L-13 | `speak`/`utter` indistinguishable; *utter* has a legal false friend | **applied**, by renaming `utter` (not `speak`) — reason in the table above |
| L-16 | `open_case` "legal" root wrong | **applied**: *cāsus* 'a fall; event' |
| L-17 | `challenge` vs "Recognition Challenge" (silo rule) | **answered**: not an SC verb; flagged to PC |
| L-02 | `oblige` runs backwards; rename to *pledge*/*swear* | **answered** for SC's side: prefer *pledge*, since `swear` is SC's oath content |
| L-08 | `release` names vow-breaking; *renounce* | **answered**: `deny` and `withdraw` are the player-facing names; a rename of `release` does not touch them |
| V-04 | mediate is not arbitrate | **applied** |
| V-05 | bribe ≠ suborn; suborn's perjury waits on J-C-6 | **answered**: FA's; SC supplies only `lie` |
| V-12, V-14 | `construe` called "deceiver" against its ruled neutral sense | **applied** (Suite 7) |
| V-13 | `challenge` gloss drops "falsely" | **applied** (§3.4: *calumnia* 'false accusation') |
| V-19 | `convene` / `covenant` same root | **answered, kept** |
| V-21 | `speak` kept against the in-tree STRAINED verdict | **answered**: STRAINED today, FITS once rebuilt; the overlap the verdict named is resolved by renaming `utter` |
| V-03 | "each keeps a name" against the tally | SC side: `deny` and `withdraw` both keep names here; the count is the reconciliation (Part III §III.5)'s |

## 3.6 Gap coverage table

One disposition per row. "M*n*" is a mechanic in §3.7.

| gap id | closed by (verb / suite) | PARKED (trigger) | OUT OF SCOPE (why) | STALE (cite tree) | DISPUTED (why) |
|---|---|---|---|---|---|
| SC-G01 | `open_case` / `lodge` (Suite 6, 5) once M2 gives a computed case an arrangement. Half moved since the register: SC-03a gave the item its keys (EI:261-272), but a computed act still writes `None` | | | | |
| SC-G02 | | | | the docket item now names its arrangement and petition (EI:243-244, :261-270, SC-03a `c2f855d2`) and `determine` reads the row's `disposes:` (VT:254); `interrogate`'s read of the charge is FI's (§3.8). Residue carried by SC-G01 | |
| SC-G03 | `petition` once M3 separates `to` from `subject` (H-94, VT:821) | | | | |
| SC-G04 | `deny`, `withdraw` (presets of `release`, Suite 5) once M4 | | | | |
| SC-G05 | `petition` (accuse) once M3 | | | | |
| SC-G06 | | trigger: a reader that weighs the petition's form or carrier (the intercessor's standing at `lodge`, RHET:305); the remontrance waits on a reader that tells an institution's petition from a subject's | | | |
| SC-G07 | `lodge` (the rename, Suite 5) | | | | |
| SC-G08 | `lodge` (the seatless route) and `convene` once M1 (the sitting's holder is the chair who orders the docket) | | | | |
| SC-G09 | `determine` once M5: a decided or vetoed motion is minted as a Record either way, so a defeat persists and is citable (*senatus auctoritas*, COMP-1:131-133) | | | | |
| SC-G10 | `speak` (REBUILD) and the `utter` → `declare` rename (L-13) | | | | |
| SC-G11 | `speak` once M6 (SC-01 steps 12-15) | | | | |
| SC-G12 | `speak` once M7 (the `issue` rung on the docket item) | | | | |
| SC-G13 | `speak` once M7: `deny_fact`, `cite_incompatible` (refute), `define` (the ten-kind design's `construe` kind), `concede_*`, `object` cover the four stases | | | | |
| SC-G14 | `speak` once M8 | | | | |
| SC-G15 | `speak` once M8: genre is read from the arrangement row (who judges, what is decided, RHET:82), priced not refused per the 2026-09-06 ruling the register cites; no new carrier | | | | |
| SC-G16 | | trigger: an interposition carrier (an advocate speaking `for:` a party); v2's own park (v2-p8:429) | | | |
| SC-G17 | `tell` (testimony, confession), `commit` (oath), any Record (record) once M9 | | | | |
| SC-G18 | | trigger: M8 (the two D-6/D-7 speech kinds need a kind reader before they can be read; H-153, H-154) | | | |
| SC-G19 | | | the person attribute carrier (v2 Part II, "pool derived at read"); no verb changes | | |
| SC-G20 | `speak` once M6 (SC-01 step 14's obstacle ceiling, v9-p6:70) | | | | |
| SC-G21 | `tell` once M10 | | | | |
| SC-G22 | | | a hearer's competence is a person attribute (v2 Part II, J-T1/J-T2), not a verb | | |
| SC-G23 | | | the contest surface is presentation (what the port shows); no verb or row carries it. The rows feed it the band | | |
| SC-G24 | `determine` once SC-03b (contested `determine` writes `Tenure.degree`, v9-p6:128) | | | | |
| SC-G25 | `vote` (into `commit`) once M12 | | | | |
| SC-G26 | `speak` once M6: the provider resolves a sitting's exchanges inside one act and returns a margin (v9-p6:76), so no DELIBERATE nests inside RESOLVE; a matter that runs on is adjourned (`convene`) with its rung kept (M7). H-56's within-season half is already closed (`hole_register.yaml:652`, R-03) | | | | |
| SC-G27 | | | the `scale:` column's retirement is the table-wide item waiting on `Act.via` scope (VT:66-79), not a verb | | |
| SC-G28 | `convene` once M1 (the SC-01 fired-slot step, v9-p6:97) | | | | |
| SC-G29 | `convene` (adjourn) once M7 | | | | |
| SC-G30 | | | | | `determine.unheard` was struck and stays struck (VT:264); a determination with no speech is a default judgment, which is lawful; "hearing precedes judgment" is the stratum order (`speak` is `social`, `determine` `binding_decision`), and that is enough |
| SC-G31 | `declare` (propose) + `vote` + `determine` once M5 and M13 | | | | |
| SC-G32 | | trigger: SC-04 seeds `negotiation` (`disposal: mutual`) and FA's `covenant` carries goods keys (v2-p8 §V.2.2) | | | |
| SC-G33 | | | FA's `covenant` readers and `release`'s pricing of a broken vow | | |
| SC-G34 | `persuade` (NEW ROW, IN-12 step 9) once M16 names which weight moves | | | | |
| SC-G35 | | | the questioning act is FI's (`interview` under custody, or the planned `interrogate`); SC's half is M9 reading the confession | | |
| SC-G36 | `declare` once M13 | | | | |
| SC-G37 | | trigger: Jordan rules J-C-6 (§3.9); revival form in Suite 7 | | | |
| SC-G38 | | | `construe` is the receiver's answer to a writ (GV's `comply` suite, VT:840); its gap is D18, whose ledger is read | | |
| SC-G39 | `forge` once M9 weighs a Record's provenance and `forgery_quality` | | | | |
| SC-G40 | `tell` (the contrary claim as content; no name, as the source refused) | | | | |
| SC-G41 | `tell` (warn, confront) | | | | |
| SC-G42 | `tell` (praise, flatter, insult, counsel) once M14, and `declare` (threaten) once M15 | | | | |
| SC-G43 | | trigger: an audience operand on `persuade` (a writer over a set of hearers, H-62) | | | |
| SC-G44 | `determine` (arbitrate, under the seeded `arbitration` row); mediate parked with SC-G32 | | | | |
| SC-G45 | | trigger: SC-04 (the unseeded games, `standing_routes`; v9-p6:136); the dead keys (`appeal_basis`, `venue_min_rank`, …) gain readers there or are deleted | | | |
| SC-G46 | | | | `challenge` and `accept` ship as the duel (VT:596, :617) and the accusation is a `petition` (v9-p5:68, step 5a, RS-23) | |
| SC-G47 | | | GV's `pardon` / `release`; the second-person lever stays refused (D-5, VT:861) | | |
| SC-G48 | | trigger: a turn limit or clock in the SC-01 provider (filibuster spends it) | | | |
| SC-G49 | | trigger: a provider with staged ballots (first ballot, momentum); dropped as WEAK DEMAND at the source | | | |
| SC-G50 | `persuade` (dyadic) vs `speak` (public): two rows, two win conditions, on RHET:355's finding | | | | |
| SC-G51 | `speak` once M8: each kind moves a different state (Suite 6), and SC-01 step 15 measures menu dominance | | | | |
| SC-G52 | `petition` (supplication) and `commit` (swear); the composition contest (N19) stays dropped | | | | |
| SC-G53 | | | | | `tell` is uncelled **by design** (`rosters.yaml:2612-2617`: its weight is in what is told, and telling is driven by regard); `speak`'s cells are owed when SC-01 step 12 rebuilds it (M8); `give`, `march` are other lanes' |
| SC-G54 | | | what a `hold` costs is H-92's budget rule (EI:878-879), not a verb | | |
| SC-G55 | | | FA's `covenant` (truce, treaty, alliance) | | |
| SC-G56 | `tell` (confide): the mechanism ships (G6, VT:1013); only the fixture `telling_privacy` is 0 | | | | |
| SC-G57 | `speak`, with the exchange count as arrangement data (XSC:551-552 *Formal*/*Grand Contest*), once M6 | | | | |
| SC-G58 | `tell` (REBUILD of `beneficiary`, Suite 1) | | | | |
| SC-G59 | `open_case` + `lodge`: `remit:determine` stands because `own` would duplicate `lodge`, the seatless route (answered by architecture; EI:301-302) | | | | |

## 3.7 Mechanics this subsystem needs (named gaps)

| # | mechanic | what it must write or read | verbs that wait on it | already planned? |
|---|---|---|---|---|
| M1 | a convened Date has a holder | `Date.holder` at `_eff_convene`, so CALENDAR forms a docket slot (EI:243-246) | `convene`, adjourn, `open_case` (fills the slot), `speak` | yes: SC-01's fired-slot step (v9-p6:97) — its own [GAP]: who sets the holder |
| M2 | a computed case's arrangement | `DOCKET_ARRANGEMENT` derived from the seat exercised and the matter (a killing → `legal_trial`; a heresy → `tribunal`); no per-arrangement branch (SC-01's falsifier, v9-p6:27) | `open_case`, `lodge`, `determine` | no ("NOT DERIVED", EI:271-272) |
| M3 | a petition's addressee apart from its subject | a content operand so `to` and `subject` bind different referents (H-94) | `petition`, accuse | partly (IN-10's channel; "a Person term has no route", v9-p5:67) |
| M4 | a denial the petitioner learns | an earned kind `petition.denied` beside `tenure.closed` (v2-p8 §V.2.4's pattern) and a channel to the absent petitioner that survives SC-01 step 13 (D-V3) | `deny`, `withdraw` | no |
| M5 | a `Record` disposal | `determine` under a row disposing `Record` mints the measure (carried or defeated) through `_mint_document`; `DISPOSABLE_KINDS` admits it (`state/gate.py:255-257`) | `determine`, `vote`, propose; recorded defeat | no |
| M6 | the contest provider | SC-01 steps 12-15: `speak`'s typed cell, four bands, the obstacle ceiling, the prize repoint, a margin returned | `speak` and its eight speech kinds | yes (SC-01, BLK on B-N) |
| M7 | the matter's `issue` rung | a stasis position on the docket item, moved by speech kinds and kept between sittings | `speak`, `deny_fact`, `define`, `object`, adjourn | no (the ladder exists only as data, ARR:44-84) |
| M8 | a speech-kind reader | the provider reads the kind (and the arrangement's genre) to choose what state moves; alignment cells for `speak` | `speak`, filibuster | no |
| M9 | a proofs reader | the bench weighs `record`, `testimony`, `oath`, `confession` (`rosters.yaml:2095`), including a Record's `forgery_quality` | testify, confess, swear, `forge`; finding out a `lie` | no (roster loaded, unread) |
| M10 | one reading of standing in a telling | `tell`'s obstacle reads the teller's standing as well as the hearer's (`rank` reads 0 today, SC-G21) | `tell` and its contents | no |
| M12 | a count of commits | the `cardinality` form (`data/requires.py` raises on it), one count shared with `confer`'s `elected` basis (GV-G44) | `vote` | yes (SC-01 step 11, v9-p6:60) |
| M13 | a mood source for a computed declaration | the chooser forms `declare` with a mood (HOLDS, THREAT, WAR) from the question; one mood-keyed alignment cell (D-V6) | `declare`, allege, threaten | no |
| M14 | a valence reader | the regard arm (H-194) and the slant valence (H-196) read a told claim's sign | praise, flatter, insult | no (both dark) |
| M15 | a threat reader | a THREAT Proposition naming a person raises his question, weighted by the threatener's credibility (standing, a force mustered) | threaten | no |
| M16 | a pursuits operand | which weight of `Person.pursuits` moves, toward what (VCD §9.4 [GAP], via SC-G34) | `persuade` | partly (IN-12 step 9) |

(M11 was a hearer-competence carrier; it is the attribute part's, SC-G22, and is not listed.)

## 3.8 Cross-subsystem flags

| other lane | verb / fold | the collision or dependency |
|---|---|---|
| GV | `construe` | leaves SC: it is the third answer to a writ, beside `comply` and `evade / defy` (VT:840) |
| GV, NP | `deny`, `withdraw` (and GV's `abdicate`) | three named presets on one closer, `release`; if L-08's *renounce* rename lands, the presets keep their names |
| GV | `vote` | one count must serve a bench vote and `confer`'s `elected` basis (GV-G44); two counts would fail S |
| GV | `determine`'s `Record` disposal (M5) | a parliament's enacted Record and a seat's `issue`d writ are two creators of binding text; GV's `proclaim`/charter/edict must say which binds whom |
| GV | `determine` (`detain`, `ban`) | the openers SC writes; GV's `arrest`/`pardon` are their other opener and closer (GV-G10-G12) |
| GV | `open_case` | GV-G09's succession tribunal waits on the same M2 |
| FA | `declare` | the rename absorbs FA's `declare (war)` preset; FA's threat/war reader and SC's M15 should share D-V6's mood-keyed cell |
| FA | negotiate, mediate | FA's `covenant` is the offer of terms; SC hosts only the `negotiation` sitting (parked) |
| FA | suborn | its perjury form waits on SC's `lie` (V-05) |
| FA, NP | `commit` | owner to be named: SC uses it for vote and oath, FA for war and allegiance |
| GV, FA | L-02's rename of `oblige` | *swear* would collide with SC's oath (`swear` → `commit`); *pledge* does not |
| FI | interrogate | questioning under custody: FI may fold it into `interview` with a custody parameter (A, M, P plausibly all yes); SC needs only the confession as a proof (M9) |
| FI, EC | `forge` | `forgery_quality` must be read by FI's inquiries as well as SC's proofs reader; L-11's `record.forged` leak is theirs to repair |
| NP | `persuade` | writes `Person.pursuits`, NP's interior; preach (religious persuasion) parks on an audience operand |
| NP | praise, flatter, insult | M14's readers (H-194, H-196) are person-interior |
| PC | insult → `challenge` | an insult's slight is the natural trigger for a duel (v2-p8:437's revival trigger); PC's `challenge` should be able to read it |
| PC | `challenge` | L-17's silo rule (`references/action_vocabulary.yaml` "Recognition Challenge") |
| EC | `give` | an intercessor receives a petition by `give` before he `lodge`s it; `give`'s owner keeps the Record case |
| EC | `exchange`, bargain | SC-G32's trade half |

## 3.9 For Jordan

Tried first, and answered without escalation: H-56's held half (answered by the SC-01 provider's
shape, SC-G26); dyadic vs public persuasion (answered by RHET:355 and the two-row split, SC-G50);
whether a threat is a roll (answered by precedent, Suite 3); whether a parliament's decision writes
anything (answered by the authored data, ARR:122 `disposes: Record`, M5); `open_case`'s eligibility
(answered by architecture, SC-G59); the `deny` name (kept as Ruling 2's word; the speech kind
renamed instead).

1. **J-C-6 (v2's D-V4): may a person lie?** Not superseded (no later ruling), not irrelevant (`forge`
   ships), not answered by a design document (v2 leaves it "not the courts' call", v2-p8:633), and
   precedent cuts both ways. The two answers make different games: *yes* makes speech foolable and
   lets testimony, interrogation and the mirror test catch something; *no* keeps the world
   unfoolable by speech while it is already foolable by documents (`forge`, VT:330), which is two
   answers to one question (S). **Recommendation: yes**, built in this order so a lie is never free:
   the proofs reader (M9) first, then `lie` as a row sharing `tell`'s cell and emitting `tell`'s kinds
   (Suite 7). If *no*: `lie` is cut, and `forge`'s place in a world without spoken lies should be
   re-argued.
