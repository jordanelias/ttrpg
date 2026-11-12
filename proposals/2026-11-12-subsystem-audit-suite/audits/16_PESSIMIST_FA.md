# FA — pessimist audit: NERS, premise and emergent narrative, of factions, governance, offices, war and diplomacy

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: 2eba83c (working tree)

Scope: `engine/season/loop/effects_governance.py`, `queries/faction_q.py`, `offices.yaml`,
`governance_spine.yaml`, `arrangements.yaml`, `data/affiliations.py`, the governance verbs, the
institutions fixed points (royalty by noble conquest; nobility by deed) and five premise sentences of rule.
The FA lane's audit and addendum (`audits/06_FA_audit.md`, `06_FA_audit_addendum_B.md`), the binding-verbs
lane (`14_VERBS_BINDING.md`), the four institutions lanes (`15_INSTITUTIONS_*`) and the game-level pessimist
(`16_PESSIMIST_GAME.md`) are cited, not redone. Everything measured here is new work unless a lane is named.
All runs `PYTHONHASHSEED=0`; scripts and outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/PES_FA/`.
`[UNVERIFIED]` marks what was not checked. Nothing here is the reason a behaviour is correct (`CLAUDE.md`
§0.05).

**§0 (verdict) is written last and placed first; if this file ends before §0 is filled, the lane was
interrupted and the sections below are the partial record.**

## 0. Verdict

*(placeholder: replaced when the runs of §1 to §3 are in; see the note above)*

## 2. Premise audit

Method: `skills/premise-check/SKILL.md`, SLICE scope (the orchestrator named the sentences). The ordinary
account **O** below was written before any FA code file, registry or note was opened by this lane.
**Declared contamination:** the FA lane's audit §0 to §6 and addendum §B0 to §B2 had been read, so O is not
blind to the lanes' findings; it is blind to the code. O is written from the words and from genre
convention, and where a cell says what a player would expect, the lanes' findings were not used to lower the
expectation.

### 2.0 The ordinary account (O), written first

**P1. "A decree binds those under the seat."**

| link | plain sentence | O: what a player expects (a run could contradict each) |
|---|---|---|
| P1.1 | a seat exists and someone sits in it | only the sitter can decree through it; a stranger, a former holder and an empty seat are refused, visibly (E1) |
| P1.2 | the sitter issues a decree | one event, with an author, a seat, a time and **content** (what is ordered, of whom) (E2) |
| P1.3 | "those under the seat" | a definite set: the persons and seats below this seat's rung in its own ladder, not persons under another seat, not the issuer (E3). A count's decree reaches his county, not the realm |
| P1.4 | the decree reaches them | each addressee learns of it, with its content, at a pace the calendar allows; distance may delay it (E6) |
| P1.5 | "binds" | each addressee is thereafter under an obligation he can keep or break: obeying does the thing ordered; **breaking it is possible and costs something the issuer can see** (E4, E5). Under the standing rule, whether a given addressee obeys goes by his own choice and a draw, never by fiat |
| P1.6 | the world changes | the ordered thing happens where obeyed (stores move, a man is installed, a levy is raised) and does not where defied (E4 zero: no decree, no change) |
| P1.7 | it ends | revocation, expiry, the issuer's death or loss of the seat: the decree lapses or passes to the successor, one or the other, by a stated rule (E7) |
| P1.8 | neighbours | a stronger seat's decree outranks a weaker one's on the same matter; `revoke` undoes `issue` (E11) |

**P2. "A vacant seat is filled."**

| link | plain sentence | O |
|---|---|---|
| P2.1 | a seat falls vacant | by death, resignation, removal or term; the vacancy is an event others can learn of (E2, E10) |
| P2.2 | someone has the right to fill it | by the seat's rule: an heir inherits, a superior appoints, a body elects; a seat with no rule says so (E1) |
| P2.3 | that someone acts | **within a season or two**: a vacancy is the most urgent thing on a ruler's desk in any strategy game; an empty throne for years is a crisis, not a default (E6, [GENRE]) |
| P2.4 | candidates | more than one eligible person may exist; who gets it depends on standing, favour and a contest, and can go either way (standing rule) |
| P2.5 | the new holder holds | he has the seat's powers the day he sits; the old holder's do not linger (E7, E8) |
| P2.6 | a vacancy that is not filled costs | the seat's work stops: its decrees, its court, its levy (E12: a seat whose emptiness changes nothing is dead) |
| P2.7 | bounds | a seat with no eligible person; a realm with every seat empty; the last member of a body (E9) |

**P3. "A war is declared and fought."**

| link | plain sentence | O |
|---|---|---|
| P3.1 | someone with standing declares | a ruler or a body with war powers, not a clerk; the declaration names an enemy and (genre) a cause (E1) |
| P3.2 | the declaration is known | both sides learn they are at war; third parties can learn it (E10) |
| P3.3 | being at war changes what is allowed | hostile acts against the enemy become licit that were not in peace (E4); allies are called |
| P3.4 | forces are raised and sent | by those with authority over men and stores; raising costs (E8) |
| P3.5 | battles are fought | where armies meet; outcome by a draw weighted by strength, ground and command (standing rule) |
| P3.6 | battle results move the war | land, fortresses, prisoners, or the will to continue (E4). A battle that changes nothing but a casualty list is half a war |
| P3.7 | the war ends | by treaty, surrender, exhaustion or conquest; someone has the standing to end it; the end has terms (E6, E7) |
| P3.8 | zero case | no declaration, no war: attacking in peace is a distinct, worse act (E4 zero, E11) |

**P4. "A faction is the sum of its persons' acts."**

| link | plain sentence | O |
|---|---|---|
| P4.1 | a faction has members | a definite set of persons, each a member by his own standing act, each able to leave (E3) |
| P4.2 | "the sum" | what the faction has (land, men, money, seats, reputation) is the total of what its members have; what it did is the total of what they did. Nothing is credited to the faction that no member did (E8) |
| P4.3 | the sum responds to its terms | a member's gain is the faction's gain; a member leaving or dying lowers the sum; a faction of zero members is nothing (E4, E9) |
| P4.4 | others read the sum | other persons treat the faction as strong or weak, friend or enemy, by that sum; and the sum they see is what they could know, not the true total (E10) |
| P4.5 | the faction "acts" only through persons | a faction's war, policy or betrayal is traceable to named persons' acts; two members can pull opposite ways and the faction then shows a split, not an average (E2, [GENRE]: factions in strategy games have a stance) |
| P4.6 | a faction rises and falls | over a campaign the sums change rank; a faction can be destroyed or founded (E6, E9) |

**P5. "An officeholder who fails his duty is called to account."**

| link | plain sentence | O |
|---|---|---|
| P5.1 | an office has a duty | something definite the holder is expected to do or keep (hold court, pay the levy, obey orders, keep the peace), knowable from the office (E3) |
| P5.2 | the holder fails it | a failure is an observable fact about what he did or did not do in a period (E2) |
| P5.3 | someone notices | a superior, a body or the governed learn of the failure; an unobserved failure goes unpunished (non-omniscience) (E10) |
| P5.4 | "called to account" | a proceeding: summons, hearing, a finding that can go either way (standing rule), in a venue with standing over him (E1, E2) |
| P5.5 | a consequence | reprimand, fine, removal, ban, by degree; proportionate to the failure (E4) |
| P5.6 | the diligent are not punished | an officer who does his duty is not called; the difference between the two is visible (E4 zero) |
| P5.7 | who guards the guard | the top seat's failure is answerable by someone or explicitly by no one (E9) |

**P6 (institutions fixed point, Jordan 2026-11-12). "Royalty is by noble conquest: the first king had the
greatest accomplishment in the secession war, then the first Duke of Hafenmark, then the first Duke of
Varfell; nobility is by deed."**

| link | plain sentence | O |
|---|---|---|
| P6.1 | a secession war happened | the world records it: a dated event with participants (E2) |
| P6.2 | accomplishments in it are ranked | three ranked deeds, each attributed to a founder: king first, Hafenmark second, Varfell third (E3, E4 ordered levels give ordered results) |
| P6.3 | rank follows the deed | the crown and the two duchies exist *because of* those deeds; the present holders' standing descends from them and a person in the world can say so (E10) |
| P6.4 | nobility is by deed | a new great deed can ennoble; a house with no deeds for generations is weaker in legitimacy than one with fresh ones; rank is contestable by accomplishment (E4, E11) |
| P6.5 | heirs | what passes to an heir is the seat and a claim on the founder's standing, which he must keep up or lose (E7) |
| P6.6 | the order matters | Hafenmark outranks Varfell by the founding order in some observable way (precedence, the claim to the crown if the royal line fails) (E4) |

