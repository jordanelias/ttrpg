# Social contest: the three proposals, assessed and compared

## Status: PROPOSED (reference; resolves nothing, schedules nothing)

Compares `...-proposal-1-one-draw.md`, `...-proposal-2-staged-proceeding.md` and `...-proposal-3-authority-first.md`
(each with its own executive overview and flowchart) on the three criteria Jordan set: **NERS**, **emergent
narrative possibilities** and **compatibility with the season loop engine**. Each criterion was assessed by an
independent read-only assessor that read all three proposals and checked at least five citations per proposal against
the tree (the NERS assessor opened 18 to 22 per proposal). None could run code, so every claim that a pinned hash or
test moves is inferred from reading, and no proposal has been run against a season. Their corrections to the
proposals' own claims are in §4. Jordan's rulings R-1 to R-41 and S-1 to S-8 outrank everything here.

---

## 1. Executive overview of the set

The three proposals share one base, the corrected armature: a contest is a venue row, a matter and a series of acts;
each act is one draw (dice, an obstacle and a leverage term on one continuous scale); people then decide by their own
acts; the row says whose decision counts, who learns it and which other authority an appeal goes to. They differ on
three forks:

- **Proposal 1, one draw, one roster:** the smallest. A speech is one act priced by aptness; kinds are rows;
  authority is a key; reception moves out of the draw into the decider's own choice. Fewest objects.
- **Proposal 2, staged proceeding:** a contest is a staged procedure whose stage list is the row's data; each stage
  asks a different question; the matter's position lives on the case file, a Record that can be seized, forged or
  burnt. Most procedural fidelity; a forensic row costs about six closing acts and an adjournment a season.
- **Proposal 3, authority first:** an authority (the parties, the polity, the church) is a grouping of offices by
  faction, with a per-territory legitimacy index; adds a bench filtered by authority, a forum contest, custody as a
  warrant, an appeal to another authority and Venice's lay assessors. The most institutional politics; the most to
  build before any of it fires.

**The result in one sentence: Proposal 1 is the best base, Proposal 3 supplies the institutional parts Proposal 1
cannot carry, Proposal 2's one distinctive idea (the seizable case file) should wait, and all three are blocked by the
same dead core that no proposal repairs.**

## 2. Side by side

| | **P1 one draw** | **P2 staged** | **P3 authority first** |
|---|---|---|---|
| distinctive object | typed `Dice`/`Obstacle`/`Leverage` sub-records; a `weights:` column on the row | a `stages:` list per row (eight question kinds); position on `Record.stages` of the case file | `authority.by_faction` in `rosters.yaml`; a legitimacy index per territory; `assessors`; forum, warrant, appeal-closure |
| reception | leaves the draw; read in the decider's own choice (`person_q.regard`) | in the draw (the armature's) | in the draw (the armature's) |
| a stage or authority is | a row value | a classification (8 kinds), not a code object | a grouping of offices, not a code object |
| kinds served best | dyadic, negotiation, count (designs voiding on appeal, mutual and count in full) | adjudication and panel (K3, K5); collapses into P1 for K1 and K7 | contests over the forum; crown over church; appeal to another authority |
| **NERS** | **1st** (best elegance ratio; the only one that deletes more vocabulary than it adds) | 3rd (adds a roster and a transition inventory; its headline reward, the plea, is weakly dominated) | 2nd (real N-lines the others only assert; two dominance corridors) |
| **emergent narrative** | 3rd (world loop not closed; L ignores news; the forum is a race) | 2nd (lasting, overlapping incidents; a seizable case file) | **1st** (most conflict between independent actors; the only L driven by news) |
| **season-loop fit** | **1st** (removes a live Layer-1 breach; typed seam) | 2nd (smallest seam; best fit to existing carriers; keeps the breach) | 3rd (opens the cross-ledger question a second time; an authority read where the gate cannot take it; names the Crown in code) |
| ranks | 1, 3, 1 | 3, 2, 2 | 2, 1, 3 |
| new objects | fewest | a roster, a docket key, a Query, a transition | one mapping, five row keys, one index, five readers, three rows |
| first batch buildable | yes (deletions, then repointing nine dependants) | yes (deletions only; every building batch waits on its S0) | yes (deletions); C2 to C4 dead in computed play until C5 |
| its own admitted weakness | everything rides on the speech-to-judgment link; procedure is flattened | pace: an adjournment costs a season; R-24 strained (Q3) | every route unreachable from computed play until C5; the church cannot judge outside T9 without a schema change |

(Rank order in the last row is NERS, emergent narrative, season-loop.)

## 3. What the three assessments agree on

**All three proposals are paper.** No season has been run with any of them. Each assessor found the same dead core,
and it is the same one in all three:

1. **Computed play reaches no arrangement row.** A computed `open_case` docks every matter under arrangement `None`
   (`effects_information.py:319-325`), and a computed `carry` writes `None`.
2. **`determine` has executed 0 times in computed play** (audit §8); `arrest` was attempted 0 times.
3. **A speech does not reach its own judgment.** `decision/` has no disposition operand; the chooser scores pursuit
   fit, stance and urgency only and cannot read a World Query.
4. **A computed petition is addressed to the person it is about** (the H-94 limit), so no non-player can petition the
   King about someone else.
5. **Not acting emits no Event**, so a refusal or a decline is invisible to everyone: scenery.
6. **No capability is authored for any person**: the roll is 2D for nearly everyone.

None of the nine scenarios the proposals wrote runs from a world cause to a world consequence today. They differ in
how far along the chain they get, and in what they add afterwards; they do not differ in this.

## 4. Where the assessors overturned a proposal's own claim

**Shared by all three.**
- *Act admission belongs in `loop/resolve.py::_eligible` and `data/requires.py`, not `state/gate.py`.* The gate is the Tenure write gate; its refusal raises `NotYours` and kills the season, against 04's "a refusal emits, never raises" (`gate.py:173-177`; `resolve.py:103`; `04:761`). P2 names the right mechanism and files it under the gate.
- *`judging_set` and the gate's `may_determine` must be one test.* Filtering only the bench lets the gate admit a judge the bench excludes (`gate.py:735-737,251-254`).
- *`disposal_reach` has no WITNESS reader* and an Event carries no recipient (`04:1031`; `loop/witness.py`). No proposal lists a WITNESS change.
- *Deleting the kernel breaks a test none of them claims:* `engine/tests/test_sigma_leverage_parity.py:52` imports the kernel's `degree_extension` and calls it (`:221-582`). The parity *golden* does not move; the test file breaks at import (CI job `sim-regression`).
- *Renaming or deleting row keys moves tests none claims:* the four keys appear 44 times across three test files; `test_arrangements.py:31-34` pins exactly eight rows.
- *Church reach beyond T9 is a schema change, not content:* `offices.yaml` has no `scope` key; one anchor sets both `rung` and `scope_rung`.
- *Widening `contest()` with `row` and `via` raises `TypeError` in the combat and mass-battle providers* (`wrappers/combat.py:180-182`; `wrappers/mass_battle.py:243-245`): three adapters, not one.

**Proposal 1.** The crown-holds-the-arm route has no carrier (a church `detain` opens directly, `effects_information.py:606-607`). Its `void` appeal needs a gate closure basis it omits: a seat can close an edge only when it is the edge's object (`effects_governance.py:335-338,348`). R-11's many matters about one party cannot hold: the docket is keyed on the party and `open_case` refuses a second item on a docketed matter (`:341`). *Softened:* "only proposal that removes the cross-ledger read" is "only proposal whose text applies ED-SC-0040's closed option B".
**Proposal 2.** Its plea is the respondent's own act with no draw, and denial is weakly dominant wherever the accuser bears the burden (at 5D an act against an equal fails 61% under R-5's ÷ 2). Its forum-detour showcase is refused at `effects_information.py:341`. Its §9c says ED-SC-0040 stays open; its last row is closed. Its appeal has no voiding. Its golden count is low: S2 moves every computed roll.
**Proposal 3.** Case-opening reads purview from `Office.rung` (T9 for church seats), not `scope_rung`, so its scenarios 2 and 3 and its worked example A break before Q1 can help. "Its roll is Proposal 1's" is wrong: P3 keeps reception in the draw. It says `contest()` keeps its signature while passing `Act.via`. Its falsifier for "C2 to C4 do not move computed play" is `test_go07_canonical_digest.py:490`, the build-world hash, which cannot see a season. Its measured legitimacy figures are not reproducible from the scratchpad scripts (outputs not saved).

## 5. Recommendation

**Adopt Proposal 1 as the base, and take from the others only what its own N-line analysis shows it needs.**

- **From P1:** the typed input record; one loop of single-draw acts; kinds as rows; the count and the mutual row; reception moved to the decider's own choice if Jordan reads R-32's "audience" that way (§6, question 1).
- **From P3, as the institutional readers P1 lacks:** the authority grouping (`authority.by_faction`, which is cleaner than P1's map), the bench filtered by authority, **custody as a warrant**, and the **appellate closure basis**. These are the carriers for R-34 and R-35 that P1 only asserts. Defer the forum contest, `assessors` and the legitimacy index until the dead core fires.
- **From P2, later and narrowly:** the seizable case file for K3 and K5 only, where its N-line survives the assessors' cut; not the stage roster.
- **Reject:** P2's pleading stage as designed (dominated); P3's authority classification as an object (a false N-line against P1's key); P1's three-sub-record split only if Jordan prefers to keep the flat record (the NERS assessor holds it a representation argument, not an N-line).

This is a judgment across three assessments that rank the proposals 1-3-2, 3-2-1 and 1-2-3. P1 never ranks last except on emergent narrative, where all three are paper; P3 wins that criterion on what it would add *after* the core fires, which is exactly the "take later" part above.

## 6. The decisions that are Jordan's (merged and deduplicated)

1. **Is "audience" a draw modifier (R-32) or an input to the decider's own choice?** This is the one that separates P1 from P2 and P3, and it decides the ranking: if R-32 binds the draw, P1's distinctive departure fails and P3 ranks first on fit. (ED-SC-0040's closed row chose re-sourcing reception from commits; whether that places it in the draw or in the choice is open.)
2. The armature's six: **G1** the ceiling's value above the default (R-37); **G2** the Layer-1 §A.3 wording for office weight (blocks every proposal's weight column); **G3** count weights; **G4** equals (keep R-5's ÷ 2: 61% failure at 5D); **G5** what R-40's 5D counts; **G6** where circumstantial leverage sits.
3. **May the church judge realm-wide while acting only at T9** (P3 Q1)? Without it R-36's own example cannot occur.
4. **May the fold read an index built from residents' ledgers** (P3 Q2)? This is Layer-1 F8 reopened.
5. **What "a royal person is involved" means** (P3 Q3), and **where church appeals go** (the polity or the Holy See; P3 Q4).
6. **Does a hearing run within one season** unless a Partial adjourns it (P2 Q1), and **may seizing a case file bend a proceeding** (P2 Q2)? Only if P2's case file is taken up.
7. **Unwatched contests (R-24):** do non-player proceedings run every stage, or collapse (P2 Q3)? Collapse breaks the armature's same-draw-at-both-fidelities rule.

## 7. What the three proposals do not decide, and what should be built first

Because the dead core is common, the first real work is the same whichever proposal is adopted, and it is the work
that turns paper into something that fires (CLAUDE.md §0.2):

1. **Computed `open_case` names its row** (today `None` for every matter).
2. **A speech reaches a judgment:** a disposition operand on `determine`; a matter-specific term in the choice layer read from the judge's own interior; computed play actually reaching `determine`. (The armature's critic priced this as not small.)
3. **A petition can be addressed to someone other than its subject** (the H-94 limit).
4. **A person can decline and the world notices** (a witnessed Event for not acting), or the refusal is scenery.
5. **Capability is authored**, so the roll is not 2D for everyone.

Each is shared by all three proposals, each has an observable (a seeded test that flips from "refused" to "fired"), and
none needs a ruling beyond G1 to G6. They should be sequenced before any proposal-specific batch, and they are the
honest answer to "can it execute": today one kind does.

## 8. Limits

No assessor ran code; every "moves" and "fires" is by reading, the audit's section 8 counts, or measured notes in
`verb_table.yaml`. P3's legitimacy figures are unreproduced. The three assessors disagree on rank by criterion; this
document weighs them, and the weighting (NERS and fit over emergent narrative while every scenario is paper) is mine
`[CONFIDENCE: medium]`. The proposals' own text overran their 3,500-word brief (4,450 to 5,100 words).
