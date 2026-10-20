# Verbs, v2 — part 09: Part VI.1, personal combat (PC)

## Status: PROPOSED (2026-10-17). Reference, not canon (`CLAUDE.md` §0.05): nothing here binds the game or is read by it. Merging ratifies nothing unless Jordan so rules. Static reading and static lookup only; no run.
## Parts, in reading order: [head](2026-10-16-verbs-01-thesis-and-persons.md) (§0, Part I Persons) · [`verbs-02`](2026-10-16-verbs-02-attributes.md) (Part II Attributes) · [`verbs-03`](2026-10-16-verbs-03-standards-roster-and-reconciliation.md) and [`verbs-04`](2026-10-16-verbs-04-critics-etymology-gaps-and-decisions.md) (Part III Verbs: standards, roster, reconciliation; critics, etymology audit, gap coverage, named mechanics, decisions) · [`verbs-05`](2026-10-16-verbs-05-what-verbs-do-to-the-world-1.md) and [`verbs-06`](2026-10-16-verbs-06-what-verbs-do-to-the-world-2.md) (Part IV What verbs do to the world) · [`verbs-07`](2026-10-16-verbs-07-roadmap-reliability-and-sources.md) (§5 Roadmap, §6 Reliability ledger, §7 Sources) · [`verbs-08`](2026-10-16-verbs-08-engine-findings-from-the-first-trial.md) (Part V: engine findings carried from the first-pass trial) · Part VI, the lexicon by subsystem: **this file** PC · [`verbs-10`](2026-10-16-verbs-10-lexicon-mass-battle.md) MB · [`verbs-11`](2026-10-16-verbs-11-lexicon-social-contest.md) SC · [`verbs-12`](2026-10-16-verbs-12-lexicon-fieldwork-and-inquiry.md) FI · [`verbs-13`](2026-10-16-verbs-13-lexicon-threadwork.md) TW · [`verbs-14`](2026-10-16-verbs-14-lexicon-settlements-and-governance.md) GV · [`verbs-15`](2026-10-16-verbs-15-lexicon-faction-actions.md) FA · [`verbs-16`](2026-10-16-verbs-16-lexicon-economy-trade-and-craft.md) EC · [`verbs-17`](2026-10-16-verbs-17-lexicon-world-travel-and-survival.md) WT · [`verbs-18`](2026-10-16-verbs-18-lexicon-npc-life-and-persons.md) NP · Part VII, the verb gap register (the evidence behind Part VI's coverage tables): [`verbs-19`](2026-10-16-verbs-19-gap-register-pc-and-np.md) PC+NP · [`verbs-20`](2026-10-16-verbs-20-gap-register-mb-and-fa.md) MB+FA · [`verbs-21`](2026-10-16-verbs-21-gap-register-sc-and-gv.md) SC+GV · [`verbs-22`](2026-10-16-verbs-22-gap-register-fi-and-tw.md) FI+TW · [`verbs-23`](2026-10-16-verbs-23-gap-register-ec-and-wt.md) EC+WT.

**How to cite this Part.** The lane's own sections are numbered 3.1 to 3.9; cite them as `PC §3.n` (for example `PC §3.9` for its items for Jordan). Gap ids (`PC-G01` …) resolve in Part VII (`verbs-19`). Abbreviations such as `VT`, `VCD`, `v2-p3` are defined in the lane's opening paragraphs; `v2-p3`, `v2-p4`, `v2-p8` are the first-pass v2 parts as filed at `716c253`. Old file names such as `…synthesis_part8.md` or `_part8` in the body also mean those first-pass files; the suite was later renamed `2026-10-16-verbs-NN-…`. Mechanic ids (`M1`, `M-1`, `M-WT-1`) are this lane's own.

**Rulings that override this section** (`verbs-03` §III.5; where this section and the roster disagree, the roster governs):

- R-15: `capture` here and GV's `arrest` are two keys on one custody-opening mechanic; GV owns the `detain` opener.
- R-24: `challenge` is the duel; SC's "challenge a claim" is `dispute`. `accept` stays PC's.
- R-25: `ambush` is a content of `fight` (persons); the MB half is parked.
- R-20: `guard` (a person's body) and TW's `ward` (a thread) are kept apart by object.

---

# PC — personal combat

Lane deliverable for the v2 rewrite (`proposals/2026-10-16-verbs/*.md`, Part III and Part V). Subsystem: PC. Gap register rows PC-G01..PC-G40 (Part VII (`verbs-19`)). Built 2026-10-16 from the working tree; no file in the repository was edited, nothing was run but greps and the etymology tool.

**Sources abbreviated.** `VT` = `engine/season/verb_table.yaml`. `EC` = `engine/season/loop/effects_combat.py`. `SW` = `engine/season/seam/wrappers/combat.py`. `WR` = `modules/combat/wrapper.py`. `PCL` = `research/by_lane/PC_personal_combat.md`. `VCD` = `proposals/2026-10-03-verb-coverage-and-gap-fill.md`. `v2-p3`/`v2-p8` = the v2 `_part3`/`_part8` files (first-pass). `XSC` = `research/cross_scale_action_catalogue_v1.md`. `ROS` = `engine/season/rosters.yaml`. Etymology: **Wikt** = en.wiktionary via `etym_tool.py en|la`; **L&S** = Lewis & Short via `etym_tool.py ls`. Every file:line below was opened this pass unless tagged `via PCL` (taken from the lane file's own table).

**The one finding that organises this lane.** Of the fifteen acts the brief lists as "v2 folds into `fight`", only six are acts a person chooses at the season scale (ambush, assassinate, shoot, rescue, champion, and guard in its ordinary sense of protecting a person), plus taking alive (capture), which the brief lists under its own head. The other ten names (strike, guard-as-posture, parry, dodge, feint, rush, grapple, disarm, disengage, interpose) are moves or outcomes **inside the scene `fight` resolves**, chosen by the engine for whichever party is defending or pressing in that exchange (`WR:255-262`, `:283-287`, `:435-450`, `:151-183`). They fail the fold test on its first clause: the party who parries is usually not the act's actor. They are not folded verbs and not culled verbs; they were never verbs. They are the scene's move vocabulary, and their home is IN-46 (the player inside a fight), not the verb table. §3.3 Suite D sets them out.

---

## 3.1 Subsystem mechanic

**Carriers written:** `Person.body`, `Person.exists`, and `Tenure.until` through `World.remove_person`'s cascade (`VT:556-559`; `EC:151-177`). **Rows:** `fight` (`VT:492`), `challenge` (`VT:596`), `accept` (`VT:617`). **Resolver:** `contests: "the body"` (`VT:502`, `:627`) routes to the provider `personal_combat` (`SW:179-253`), which builds `PersonalCombatInput` (two claimants, `end` derived from `body` bands only: `SW:130-151`) and calls `modules/combat/fight.py:31-69`; that constructs two `Combatant`s at class defaults and calls `wrapper.fight(A, B, rng=rng)` (`fight.py:52`) — the multi-turn SIM harness (`WR:504`). **Degree** is read off the *subject's* `wound_state` (`VT:561`): Felled / Wounded / Untouched. **Effect:** one function, `_eff_kill`, registered for `fight` and `accept` (`EC:34-36`), writing the subject only (`EC:105-107`). **Emits** `person.died` / `body.changed` / `contest.undecided`; refusals `kill.refused`, `accept.refused`. `challenge` writes nothing and emits `challenge.issued` (`VT:609-611`).

**Built in the module, unreached from the season:** commit depth with lunge (`WR:255-262`), three defence modes (`modules/combat/vocabulary.py:68-72`), a grab menu of six outcomes (`modules/combat/contact.py:54`; fired at `WR:435-450`), footwork disengage (`WR:151-183`), and a §11.4 Yield declaration (`WR:467-513`) that `fight.py:52` never passes.

**Lacks:** a write on the actor (M-PC-2); a challenge carrier and duel terms (PC-10a/b, unbuilt: `grep challenge_terms|duel.yielded` over `engine/`, `modules/` → 0 this pass); a custody write from a fight (`detain` opens only as `determine`'s disposal: `ROS:115-123`); an N-party input (`SW:207-216`); ranged arms; per-person inputs (`SW:34-39`); a weight bound (cohorts admitted); and kinds that tell a duel from an assault — `person.died`, `body.changed` and `contest.undecided` are each emitted by two rows, so `KIND_VERB` maps them to no verb (`engine/season/data/verbs.py:1231-1245`).

---

## 3.2 Convention floor

What a player of a medieval personal-scale strategy RPG expects personal combat to let a person do. "Shipped" = a verb row; "planned" = a workplan position; "designed" = v2/VCD only; "absent" = neither. Named games from memory are `[MEMORY]` and name the mechanic relied on.

| # | floor act | precedent | state today |
|---|---|---|---|
| F1 | **Attack a person** (open violence, possibly lethal) | Jordan 2026-09-02, `VT:504` ("that would trigger the personal combat scene"); `VCD:851` (§6.3 `fight` APPLIES); GURPS `[MEMORY]`: the Attack / All-Out Attack manoeuvres | **shipped** (`fight`) |
| F2 | **Challenge to a duel, and answer it** | Romance of the Three Kingdoms series `[MEMORY]`: officers' one-on-one duels, offered and refused; Mount & Blade: Warband `[MEMORY]`: a rival suitor challenges the player to a duel; historical wager of battle in English law, abolished 1819 after *Ashford v Thornton* `[MEMORY]`. In-tree: none (`PCL:227` GAP) | **shipped** (`challenge`, `accept`; grade `assumption`, `VT:614`, `:643`) |
| F3 | **Duel terms**: to first blood, until one yields, to the death | tournament *à plaisance* vs *à outrance*, and the 19th-century first-blood duel `[MEMORY]`; in-tree `PCL:348` (PC-10 terms `[ASSUMPTION; medium]`) | **planned** (PC-10a/b, unbuilt) |
| F4 | **Yield / surrender in a fight** | `WR:467-481` (§11.4 Yield: "what the opponent does with an unresisting man (execute, take prisoner, release) is the CALLER's disposition"); Mount & Blade `[MEMORY]`: a beaten lord is taken, not killed | **built-dark** in the module; no season producer (`fight.py:52`) |
| F5 | **Take a person alive** (capture, kidnap) | CK3 `[MEMORY]`: imprison interaction, capture of commanders in battle; Mount & Blade `[MEMORY]`: defeated lords become prisoners; in-tree `PCL:113` (CK3 imprison/ransom/execute row) | **absent** from combat; custody exists only by judgment (`detain`, `ROS:115-123`) |
| F6 | **Ransom / execute a captive** | CK3 `[MEMORY]`: ransom and execute prisoner interactions; `research/governance/political_hierarchy_standing.md:142` (forced suicide as negotiated execution) | ransom **designed** (FA V152, `v2-p8:495`); execute ruled not a verb, **Jordan's R-1** (`VCD:2648` K-10). Not PC's: §3.8 |
| F7 | **Assassinate** (covert, lethal, attribution in doubt) | *The Republic of Rome*'s assassinate action (`VCD:851`); CK3 `[MEMORY]`: the Murder hostile scheme, secret until discovered; `research/governance/conflicts_power_struggles.md:36` (Caesar), `:256-259` (Pazzi); `canon/03_canonical_timeline.md:116` (unattributed killing, as quoted in the register) | **designed** (v2 V106 KEEP WITH CONDITIONS, `v2-p8:399`) |
| F8 | **Ambush** (attack first, from cover) | `research/historical_concerns_action_catalogue_v1.md:231-234` (Chain 11, assassination-class intrigue); Blades in the Dark `[MEMORY]`: the engagement roll grants position for a surprise attack | **designed** (V105 MERGE, `v2-p8:398`) |
| F9 | **Ranged attack** (bow, crossbow, thrown) | Mount & Blade `[MEMORY]`: bows, crossbows, throwing weapons as a skill-and-kit axis; GURPS `[MEMORY]`: the Aim manoeuvre; Blades in the Dark `[MEMORY]`: the Hunt action ("shoot") | **absent**: no ranged weapon in `modules/combat` (`PCL:232`, `:367`) |
| F10 | **Flee a fight** | `XSC:389` (§4.1 separation reasons); `WR:151-183` (footwork withdrawal, pursued on a failed read); Burning Wheel `[MEMORY]`: Range and Cover's withdraw; GURPS `[MEMORY]`: Retreat as a defence option | **built** in the module, engine-chosen; no season choice (IN-46 `{engage, withdraw}` `[ASSUMPTION]`, via PCL:329) |
| F11 | **Protect another person** (bodyguard) | CK3 `[MEMORY]`: the Bodyguard court position, which guards the liege against hostile schemes; in-tree `PCL:328` (M-PC-3: "guards interposing") | **absent**; v2 reads it as `oblige` + presence (V095, `v2-p8:388`) |
| F12 | **Rescue a captive** | Mount & Blade `[MEMORY]`: freeing prisoners held by a defeated party; `VCD:4481` (App. B fam. 26, extraction ids) | **parked** (V084, `v2-p8:401`) |
| F13 | **Fight for another** (champion; a duel inside a battle) | Romance of the Three Kingdoms and Total War: Three Kingdoms `[MEMORY]`: hero duels during a battle that move the side's morale; `research/valoria_systems_integration_master_v1_part2.md:236` (General Duel, designed) | **parked** (V085, `v2-p8:402`); no duel→battle seam (`PCL:330`) |
| F14 | **Choose how to fight** (press, defend, grapple) in the moment | GURPS `[MEMORY]`: dodge, parry and block chosen per attack; Burning Wheel *Fight!* `[MEMORY]`: scripted volleys of strike, block, feint, disarm…; `XSC:407-417` (§4.3: commit depth and defence mode "engine-chosen; the injection point exists") | **built**, engine-chosen (no IN-46 build batch) |
| F15 | **Who fights matters** (skill, kit, tradition) | Mount & Blade `[MEMORY]`: weapon proficiencies and equipment decide melee; `PCL:326` (M-PC-1); `XSC:407-413` (weapon, armour, tradition BUILT pre-fight) | **built-dark**: every season fighter is at defaults (`SW:34-39`) |

**Placement rulings for the floor.** F1–F5, F7–F14 are PC's (the act resolves through the body contest or reads its result). F6 belongs to the custodian's seat (GV/SC: `detain`'s holder) and FA (ransom). Flight *before* a fight (a person leaving a place to avoid an enemy) is WT's `move`, not PC's. Raising and fielding troops is MB; a crowd is never a personal-combat party (§3.3 Suite A, K-PC-12).

---

## 3.3 Suites

**How a fold is carried here (architecture, not preference).** The value term reads the verb key alone: `align(c.verb, ax)` (`engine/season/decision/choose.py:149`), and a witness can map a kind to a verb only where one row emits it (`data/verbs.py:1231-1245`). So a folded act that passes the fold test takes one of two forms: (a) a **content** of the host (no key) where its precondition and moral weight are the host's; (b) a **named fold with its own key on the host's effect** where its precondition or its valuation must differ. The tree already has form (b): `@effect_for("fight")` and `@effect_for("accept")` on one function (`EC:34-35`), with different alignment cells (`ROS:2876`, `:2918-2923`, `:2986-2988`). Form (b) is not a new row of mechanism; it is a new key on the one mechanism. If a contents-aware value term lands (v2 D-V6, `v2-p8:105-108`), every form-(b) fold here drops to form (a).

**Fold test** (the lane brief §0 item 5): *same actor? · same subsystem mechanic? · parameter or content only?* Three yes = true equivalent.

### Suite A — Attack. Host: `fight`

**Members.** Host `fight` (shipped). Named folds with own key: `assassinate`, `capture`. Contents: `ambush`, `shoot`. Outcomes, not verbs: kill, wound (the Felled/Wounded bands), murder (a judgment on an outcome, `VCD:2133`).

| act | same actor? | same mechanic? | parameter/content only? | verdict |
|---|---|---|---|---|
| `assassinate` | yes: the attacker | yes: the body contest, `_eff_kill` | yes: aim *death* (yields refused), a held cover, first move, actor withheld from witnesses by the cover's degree | **true equivalent; own key** (its precondition — a held cover — and its valuation, treachery, differ from `fight`'s) |
| `capture` | yes | yes: the same scene | yes: aim *alive*; the Felled or yielded subject is taken into custody instead of written dead | **true equivalent; own key** (precondition: somewhere to hold him; valuation: taking is not killing) |
| `ambush` | yes | yes | yes: sets the first mover, today a coin flip (`first = A if rng.random()<0.5 else B`, `WR:514`) | **true equivalent; content** (orthogonal to aim: any of `fight`, `assassinate`, `capture` may be laid from ambush, so a key would multiply keys) |
| `shoot` | yes | yes, *once* a ranged weapon exists in the one resolver ("never a second resolver", `v2-p8:394`; Total War, `PCL:102`) | yes: the weapon in hand | **true equivalent; content (kit)**, inert until the mechanic exists |

**World effect.** Host today: Felled → `Person.body`, `Person.exists`, `Tenure.until` and `person.died`; Wounded → `Person.body`, `body.changed`; Untouched → nothing, `contest.undecided` (`VT:556-581`) — **on the subject only** (`EC:105-107`). Lacks: (1) the actor's outcome — the scene fells the actor in about half of mirror fights (205/400, via `PCL:327`), and if the subject is untouched the act reports `contest.undecided` (a false report); (2) a weight bound — a cohort subject is deleted whole by one Felled band (`EC:176`, via `PCL:334`); (3) an Event that says how it ended (yielded, fled, felled) and by what blow (K-PC-9); (4) a grudge on a surviving subject, which `march` writes and `fight` does not (`EC:181-193`; `PCL:113`); (5) per-person inputs (`SW:34-39`). `capture` adds a custody write (no carrier for a seatless captor: `detain` is "prisoner -> a seat", `ROS:115`). `assassinate`/`ambush` need FI's cover (`conceal` has no row: `grep 'verb: *"conceal"' VT` → 0).

**NERS.**
- **N.** `fight`: cut it and no person can harm another; it is the only row into `modules/combat` besides `accept` (`VT:502`, `:627`; `rosters.yaml:1170` "for EVERY verb contesting this prize (`fight` and `accept`)"). Six directions: bottom-up (the module's physics reaches the world only here), top-down (a death closes the dead man's tenures, `EC:176`), lateral (`march` is the mass sibling), diagonal (FI's cover feeds the attack), horizontal (SC's challenge), vertical (duel→battle: absent, so narrowed there). **HOLDS.** `assassinate`: cut it and a killing whose author the world cannot name is inexpressible, because every act-caused Event carries its actor (`loop/witness.py:588-592`); attacked as a false N-line via `ambush` (content): ambush moves the first blow, it does not withhold the actor, and the chooser cannot price treachery off a content (`choose.py:149`). **HOLDS, narrowed** to unattributed killing. `capture`: cut it and violence can only harm, never take; custody arises only from a seat's judgment (`ROS:115-123`), so field capture, kidnap, ransom (FA) and rescue lose their producer; attacked via GV's planned `arrest` (warrant-bound, `VCD:4112` K-53): it covers custody by a seat's writ, not by force without one. **HOLDS, narrowed.** `ambush`: cut it and surprise has no lever (the first blow stays a coin flip). **HOLDS, narrowed** (bottom-up only). `shoot`: **FALSE N today** (disqualifier 2: no ranged weapon to produce it); kept as a named content only because F9 is floor and the gap is the mechanic's (§3.7 M9).
- **R.** R-PLAYER: four aims with different costs — open attack, covert killing, taking alive, (with kit) attack at range. R-WORLD: NPC assassinations and kidnaps throw succession, ransom and rescue hooks with no player present. R-COMPLETE **fails today at three extremes**: the felled actor, the cohort subject, identical fighters.
- **S.** Methodology defect: `fight` follows the subject whoever lost, `march` follows the losing side (`EC:181-199`; PC-G10). Pause: fought at RESOLVE as a harness call (`WR:504`, "the GAME calls one engagement per turn"); no suspension (M-PC-4). Up/down: no duel↔battle seam (M-PC-5). Calculation: one scene, one effect for every key — consistent.
- **E** (last, as a ratio). One effect, three keys each justified by a precondition or a valuation the chooser must read, two key-less contents, and the nine scene moves kept out of the season vocabulary (Suite D). Nothing N or R found is lost; nothing is carried twice. **Holds.**

**Precedent.** §3.2 F1, F5, F7, F8, F9; Total War auto-resolve's one-resolver lesson (`PCL:102`); CK3 `[MEMORY]` Murder scheme (secret attempt; discovery is a separate roll) — the cover/attribution split here.

**Gaps closed.** PC-G01, G09, G10, G16, G32, G34, G35 (combat half); closed once a mechanic exists: G14, G15, G23, G29, G30, G40. **Open:** G11–G13 (parameters), G27 (substrate), G31 (deontological gate).

**Disposition.** `fight` **REBUILD** (row stands; effect writes both parties, weight bound, Event payload, refusal kind `kill.refused` → `fight.refused`, and the stale note at `VT:503`). `assassinate` **NEW ROW** (named fold, own key on `_eff_kill`). `capture` **NEW ROW** (named fold, own key). `ambush` **FOLD** (content). `shoot` **FOLD** (content; waits on M9). Falsifiers: `fight` — a second row routing `contests: "the body"` outside PC; `assassinate` — `conceal`'s witness read withholds attribution generically *and* D-V6 lands (then it is a content); `capture` — GV builds `arrest` on this same scene with a warrant content, making `capture` the warrant-less value of one key (§3.8 proposes exactly that merge, so this is the expected falsifier, not a remote one).

### Suite B — Duel. Hosts: `challenge` (the challenger's act) and `accept` (the challenged's act)

**Members.** `challenge` (shipped), `accept` (shipped; mechanically a named fold of `fight`). Contents: the **terms** (`first blood`, `yield`, `death`) and the **stakes** on the challenge; `champion` (a `for` content). Not acts: refusing (the challenge lapses unanswered), "duel" (the name of what resolves, `VT:593-594`).

| act | same actor? | same mechanic? | parameter/content only? | verdict |
|---|---|---|---|---|
| `accept` vs `fight` | yes: the acceptor attacks the challenger | yes: one effect registered twice (`EC:34-35`) | yes: answers a held challenge and fights under its terms | **true equivalent of `fight`; own key** (precondition: a challenge naming him; valuation differs, `ROS:2876`, `:2923`, `:2988`) |
| `accept` vs `challenge` | **no**: two persons | no: `challenge` writes a Record, contests nothing | — | **two rows**; folding one into the other is the "other actor's reply" composition the the lane brief forbids |
| `champion` | yes: the champion is the actor of his own `challenge` or `accept` | yes | yes: a `for` naming the principal whose stakes ride on the result | **true equivalent; content** of `challenge`/`accept` |
| terms (`first blood`, `yield`, `death`) | yes (the challenger sets them) | yes | yes: data on the Record the scene reads | **content** |
| refusing a challenge | the challenged | — | — | **not an act**: no `accept` before the Record lapses; the lapse is witnessed (K-PC-7's shape, withdrawn only for want of the Record, `PCL:552`) |
| K-23 (`petition` + `fight`) | no: composes SC's `petition` and the replier's `fight` | no | no | **not a fold**; struck (`VCD:3` status line: "K-23 … NOT ratified, struck by IN-08") and fails the no-workaround rule; the revert clause at `VT:592-593` is stale |

**World effect.** `challenge` today writes nothing (`VT:609-610`) and `accept` refuses only a dead challenger, so 12 of 12 executed `accept`s ran with no challenge behind them (`VT:629`). Rebuilt: `challenge` mints a Record of kind `challenge` held by the challenger, naming the challenged, the terms, the stakes and any `for` (PC-10b), emits `challenge.issued`, and lapses at a term as a witnessed `challenge.lapsed`; `accept` requires a live challenge naming the actor, closes it, fights under its terms (first blood stops the scene at the first wound; `yield` passes Yield declarations; `death` refuses them, `WR:467-478`), writes `fight`'s bands to both parties (M1), and emits one duel kind beside the band's kind so a witness can tell a duel from an assault (today `person.died` maps to no verb, `data/verbs.py:1231-1245`).

**NERS.**
- **N.** `challenge`: cut it and a fight can no longer be offered and refused before witnesses, so honour-binding violence and refusal-as-shame die (v2's own closest call, `v2-p3:198`); attacked via K-23: struck and a composition. **HOLDS.** `accept`: cut it (fold into `fight` as content) and the consenting duel is priced as an assault by the chooser and every witness (`choose.py:149`); **HOLDS, narrowed** to valuation and precondition — exactly the reason it is a key and not a separate mechanism. `champion`: **FALSE N today** (disqualifier 2: nothing reads a duel's result for a principal, `v2-p8:554`); kept as a named content (F13) at zero row cost.
- **R.** R-PLAYER: accepting bad odds or losing face (`ROS:2987-2988`: honour cells on both acts); terms let a duel be survivable (RS-25, "a duel doesn't have to be lethal", `v2-p8:551`). R-WORLD: NPC duels produce deaths, yielded captives and feuds unwatched. R-COMPLETE **fails today**: the pair runs without its link (0 of 12).
- **S.** One scene for duel and assault (one resolver). "Pauses correctly" only once the scene reads the terms (first blood is a stop rule the module lacks). Vertical: a challenge issued in a field is the duel-inside-a-battle (F13); MB reads the result.
- **E.** Two rows, one Record kind, terms and `for` as data, refusal as a lapse rather than a verb. **Holds.**

**Precedent.** §3.2 F2, F3, F13. In-tree research has none for duelling custom (`PCL:227`); the floor rests on `[MEMORY]` precedents and one Jordan reply ("3 accept", `VT:592`).

**Gaps closed.** PC-G03, G04, G05, G06, G07, G08 (the producer of a yield), G24, G25; parked: G36.

**Disposition.** `challenge` **REBUILD** (mint the Record; PC-10b). `accept` **REBUILD** (require the Record; emit a duel kind; name kept, STRAINED, §3.4). Terms, `champion`: **FOLD** (contents). Falsifiers: `challenge` — a run in which no `accept` ever reads a challenge Record even after PC-10b (the link is the N-line); `accept` — D-V6 lands (then `accept` becomes `fight` with an `answering` content).

### Suite C — Protection and rescue. Hosts: `guard`, `rescue` (both new)

| act | same actor? | same mechanic? | parameter/content only? | verdict |
|---|---|---|---|---|
| `guard` vs `fight` | no: the guard is not the attacker | no: a standing protective edge, read when another's fight opens | no | **own row** |
| `guard` vs `oblige` (v2 V095: `oblige` + presence) | yes | no: `oblige` binds the actor to a **seat** (`VT:762`, `referent_class: Office` `:765`); a ward may hold none | no; and v2's form composes two verbs (`oblige`, `move`) | **fails; own row** |
| `rescue` vs `fight` | yes | **no**: the prize is a captive's custody, not a body | no | **own row** |
| `rescue` vs `release` | no: `release` closes one's own edge; `detain` is outside its domain (`ROS:118-121`) | no | no | **own row** (v2 V084 reached the same refusal, `v2-p8:553`) |
| `interpose` | a third party, inside another's scene | the N-party scene | — | **scene move** (Suite D), not a verb |

**World effect.** `guard`: actor = the guard, subject = the ward (a person), co-located; writes a protective edge guard → ward (carrier: a Tenure kind `guard`, an eleventh on `ROS:124` [ASSUMPTION — no existing kind binds person to person with this reader; `tie` is unread and partnerless, NP-G01]); emits `guard.taken`; ends by the guard's `release` or death. Its readers, all unbuilt: the combat seam enters a co-located guard as a party when his ward is attacked (K-PC-5), `assassinate`'s cover read counts guards, IN-60's security Query. `rescue`: subject = a prisoner under a live `detain`, co-located; contests custody against the custodian's guards present (through the combat scene; uncontested if none); writes `Tenure.until` on the `detain` and relocates the prisoner with the rescuer (`_relocate`, `EC:11`); emits `prisoner.freed`; leaves the case Record and any `ban` alone.

**NERS.**
- **N.** `guard`: cut it and protection exists only as a seat's service (IN-60's planned Query over `oblige` + presence); a person cannot choose to protect someone who holds no seat, and the bodyguard who dies for his friend is inexpressible. Attacked as false via IN-60 (disqualifier 1): it covers seat-holders' guards only. **HOLDS, narrowed.** Without K-PC-5 the edge has no reader, so it ships with that loop or not at all. `rescue`: cut it and a detained person leaves only by his seat's own act; attacked via `fight` the gaoler then `move`: a composition, and a dead gaoler leaves the `detain` running to the seat (`v2-p8:553`). **HOLDS.**
- **R.** R-WORLD: rescues and guarded assassinations are the genre's set pieces; R-PLAYER: allocating protectors; choosing to free rather than ransom.
- **S.** Both enter the one scene (no second resolver); `rescue` reads GV's `detain` without writing GV's sentence.
- **E.** Two rows, one Tenure kind, and `interpose` costs nothing. The Tenure kind is the cost the meta-rule presumes failed; §3.9 item 1.

**Precedent.** §3.2 F11, F12; `PCL:328` (M-PC-3).

**Gaps closed.** PC-G17, G18 (once their mechanics exist).

**Disposition.** `guard` **NEW ROW** (built with K-PC-5; carrier to Jordan, §3.9). `rescue` **NEW ROW** (built once `capture` or GV's `arrest` produces live `detain` edges; v2's PARK trigger is subsumed by `capture` being the producer). Falsifiers: `guard` — IN-60 ships and a seatless ward is never attacked in a seeded corpus (the narrowed N-line would be empty); `rescue` — no run ever holds a live `detain` at a season's end after `capture` ships.

### Suite D — The scene's moves (not verbs). Host: none at the season scale; IN-46 exposes them

These are chosen inside `fight`'s resolution, by the engine today, for whichever party is pressing or defending in that exchange (roles flip each exchange, `WR:428`). Applying the fold test as the brief asks:

| name | engine site | chosen at the season scale? | same actor as the act's actor? | same mechanic? | parameter only? | verdict |
|---|---|---|---|---|---|---|
| strike | the exchange itself (`WR:292` attack σ; `outcome` event `:451`) | no | no: either party | yes | **no**: it *is* the mechanic's unit | **not an equivalent**: a synonym of the exchange. CULL the name |
| feint | low commit depth ("a feint (commit~2, full recovery) costs no tempo", `WR:262`) | no | no: the exchange's aggressor | yes | yes | **move**: one value of commit depth |
| rush → **lunge** | commit ≥ `LUNGE_COMMIT` becomes a lunge (`WR:259-260`) | no | no | yes | yes | **move**: the other pole of the same parameter; name `lunge` (the engine's and fencing's word) |
| parry, dodge | `DEFENCE_MODES = (parry, dodge, wind)` (`vocabulary.py:72`), picked by the read contest or at random (`WR:284-287`) | no | no: the exchange's defender | yes | yes | **moves**: values of one parameter |
| guard (posture) | stance lean / wariness skew on commit (`WR:255-258`) | no | no | yes | yes | **move**, unnamed (the engine's `stance_lean`); the word goes to Suite C's row, its ordinary sense |
| grapple | contact branch on an opening (`WR:429-450`; `contact.py:29`) | no | no | yes | yes (a branch) | **move** |
| disarm | drawn from `GRAB_OUTCOMES` (`contact.py:54`, `:57-62`) | no | — | yes | **no**: drawn, not chosen | **outcome**, like kill and wound |
| disengage / withdraw → **flee** | footwork withdrawal, attempted by `disengage_attempt_p`, pursued on a failed read (`WR:151-183`) | no (flight *before* a fight is WT's `move`) | no: either party | yes | yes | **move**; name `flee` (§3.5) |
| yield | §11.4 declaration (`WR:467-513`) | no in the scene; yes as a duel term (Suite B) | no: the yielder | yes | yes | **move and term** |
| interpose | none: two claimants only (`SW:207-216`) | no | no: a third party | needs the N-party scene | — | **move** of the N-party scene |

**World effect.** None writes the world; each changes the scene's draw and reaches the world only through the band and the Event (M12): a yielded or fled ending, and with `capture`'s aim a yielder taken. **The trace-kind mirror is stale:** `systems/combat/combat_engine_v1/state_graph.py:21-25`'s `TRACE_KINDS` lacks `disengage`, which `WR:178` and `:183` emit (PC-G21, confirmed).

**NERS.** **N** — cut the moves from the season vocabulary: nothing dies, because they were never there; cut them from the scene: the bout's physics dies. **False N-line found in v2:** its nine "MERGE into `fight`" verdicts (`v2-p8:387-396`) record folds that were never verbs; V-02 counts them as "upheld" merges, which inflates PC's tallies. **R** — reaches the player only through IN-46 (F14); until then the duel is a spectator engine (`PCL:120`). **S** — one resolver at three fidelities (Football Manager, `PCL:101`). **E** — removes about ten names from the season vocabulary at no loss.

**Precedent.** GURPS and Burning Wheel *Fight!* `[MEMORY]` (§3.2 F14); `XSC:407-417`.

**Gaps closed.** PC-G19, G20, G21, G22 (once IN-46 exists).

**Disposition.** All **CULLED as verbs**; retained as the scene's move vocabulary under IN-46: press (`feint` ↔ `lunge`), defend (`parry`, `dodge`, wind), `grapple`, `flee`, `yield`, `interpose`. `strike`, `rush`, `disengage`, `withdraw` as names: CULLED. `disarm`: an outcome. Falsifier: a seeded corpus in which a person's season choice (not the engine) sets a defence mode or commit depth *without* IN-46 — that would make one of these a season-scale act.

---

## 3.4 Lexicon table

Chains: **Wikt** = `etym_tool.py en|la` output this pass; **L&S** = `etym_tool.py ls`. Principal parts are from the Wikt Latin headword template or L&S. "Fit" is ordinary current usage (ED-IN-0179), separate from the chain; no design claim here rests on a root sense (L-01).

| verb | suite | status | mechanic and world effect (carrier written) | etymology chain (sources) | fit | rename |
|---|---|---|---|---|---|---|
| `fight` | A host | SHIPPED (REBUILD) | body contest via `personal_combat`; Felled → `Person.body`, `Person.exists`, `Tenure.until`, `person.died`; Wounded → `Person.body`, `body.changed`; Untouched → `contest.undecided` (`VT:556-581`); rebuilt to write both parties (M1) | ← ME *fighten* ← OE *feohtan* ← Proto-West-Germanic \**fehtan* ← PGmc \**fehtaną* ← PIE \**peḱ-* 'pluck' (Wikt). **Germanic; no Latin path.** L *pectō, pectere, pexī, pexum* 'to comb' (L&S) is a **cognate, not an ancestor** (Wikt lists it among cognates) | **FITS**: "fight someone" is the attempt, not the outcome — what Jordan's ruling asks (`VT:482-483`) | — |
| `challenge` | B host | SHIPPED (REBUILD) | today writes nothing, emits `challenge.issued` (`VT:609-611`); rebuilt: mints a `challenge` Record (terms, stakes, `for`), lapses witnessed | ← ME *chalenge*, palatalised variant of *kalange* ← OF *chalenge, chalonge* (Central French forms of Old Northern French *calenge*) ← L *calumnia* (Wikt); *calumnia, -ae* f. 'trickery, artifice, chicanery, cunning device … a false accusation, malicious charge' (L&S; Wikt la). PIE **disputed**: Wikt reports De Vaan's two proposals (from *calvor*; or from \**kelh₁-*). The sense 'call to fight' is English `[UNVERIFIED: century]` | **FITS** with a person as object ("challenge him to a duel"); "challenge a claim" is SC's sense, §3.8 | — |
| `accept` | B | SHIPPED (REBUILD) | named fold of `fight` (own key on `_eff_kill`); rebuilt: requires a held challenge naming the actor, fights under its terms, emits a duel kind | first attested about 1380 (Wikt) ← ME *accepten* ← OF *accepter* or directly L *acceptō, -āre, -āvī, -ātum* (1st conj.) 'to take, receive, accept' (*jugum acceptare*, 'to submit to the yoke', Sil.) (L&S), frequentative of *accipiō* ← *ad-* + *capiō, capere, cēpī, captum* 'take, capture, seize' ← PIE \**kap-* (Wikt; exact pre-form disputed, LIV vs Schrijver) | **STRAINED**: the most generic verb in the table (L-12); exact only once the row requires a challenge | keep; if another lane needs "accept" for terms, PC takes `take up` — §3.8 |
| `assassinate` | A | NEW (named fold, own key) | `fight`'s scene with aim *death* (yields refused), a held cover, first move, actor withheld from witnesses by the cover's degree (M6) | ← *assassin* + *-ate*, after MF *assassiner* (Wikt) ← F *assassin* / It *assassino* ← Arabic (two proposed sources: *asāsiyy*, *ḥashshāshīn*) (Wikt). **Not Latin at root**; ML *assassīnus* (alt. *asasīnus*) is attested (from Ar. *ḥaššāš* / *ḥaššāšīn*), but English comes from F *assassin* / It *assassino*, not through it (Wikt la, fr, it). No PIE | **STRAINED**: an achievement verb ("was assassinated" reports a death), so the row names its hoped-for outcome — the defect Jordan ruled against for kill/wound — but it is the convention's name for the attempt (*Republic of Rome*, `VCD:851`) | keep (floor name); no plain attempt-verb exists ("make an attempt on his life") |
| `capture` | A | NEW (named fold, own key) | `fight`'s scene with aim *alive*: a Felled or yielded subject is taken into custody (M5), `person.captured` `[ASSUMPTION: kind name]` | ← MF *capture* (noun) ← L *captūra* 'a taking, catching; capture; that which is taken' (Wikt la) ← *capiō, capere, cēpī, captum* ← PIE \**kap-* (Wikt). English verb formed from the noun `[UNVERIFIED: century]` | **FITS** ("captured the duke"); achievement aspect as `assassinate`, milder because failure leaves both standing | — |
| `ambush` | A | FOLDED (content) | sets the scene's first mover from a held cover (`WR:514` coin flip today) | ← ME *enbuschen* ← OF *enbuscier, anbuchier* ← *en-* (← L *in-*) + VL *boscus* ← Frankish \**busk* ← PGmc \**buskaz* 'bush' (Wikt). Latin only in the prefix; the root is Germanic | **FITS** (an attempt verb: "ambushed but beaten off") | — |
| `shoot` | A | FOLDED (content, kit) | a missile weapon in `fight`'s one resolver; inert until M9 | ← ME *scheten, schoten* ← OE *scēotan* ← PWGmc \**skeutan* ← PGmc \**skeutaną* ← PIE \**(s)kewd-* (Wikt). **Germanic; no Latin** | **FITS** | — |
| `champion` | B | FOLDED (content) | a `for` naming the principal on `challenge`/`accept`; inert until a stakes reader | ← ME *champioun* ← OF *champion* ← ML *campio* ← Frankish \**kampijō* ← PWGmc \**kamp*, itself a borrowing of L *campus* 'field' (Wikt). Latin at both ends, Germanic between. PIE: through L *campus* ← Proto-Italic \**kampos* ← \**kh₂émpos* ← \**kh₂em-* 'to bend' (traditional, uncertain; an alternative derivation is of substrate origin) (Wikt la) | **FITS** as a noun ("the king's champion"); as a verb today it means 'advocate' (STRAINED), so it names the content, not an act | — |
| `yield` | B, D | FOLDED (term + scene move) | duel term on the Record; in the scene a §11.4 declaration (`WR:467-513`); the yielder stands, the victor's aim decides custody or release | ← ME *yielden, ȝelden* ← OE *ġieldan* 'pay' ← PWGmc \**geldan* ← PGmc \**geldaną* ← PIE \**gʰeldʰ-* (Wikt). **Germanic; no Latin**. Sense 'pay, render' → 'give up, surrender' (Wikt senses) | **FITS** ("the knight yielded"); homonym of `Rung.yield` and the inquiry yield (V-20): kinds must be prefixed (`fight.yielded`) | — |
| `guard` | C | NEW | protective edge guard → ward (`Tenure` kind `guard`, §3.9), `guard.taken`; read by the N-party scene (M7) | ← late OF *guarder* / early MF *garder* (c. 14th century) ← Early Medieval Latin *wardō* ← Frankish \**wardēn* ← PGmc \**wardāną* (Wikt). **Germanic, entering through Medieval Latin** (as *seize*); doublet of *ward* (Wikt) | **FITS** ("guard the king") | — |
| `rescue` | C | NEW | closes a live `detain` by force and relocates the prisoner; `prisoner.freed` | ← ME *rescouen* ← OF *rescoure, rescorre* ← *re-* + L *excutiō, excutere, excussī, excussum* 'to shake out or off, to cast out, drive out' (L&S) ← *ex* + *quatiō* 'shake' (Wikt la). PIE: *quatiō* is disputed (LIV gives a PIE root; De Vaan argues it is possibly non-IE) (Wikt la) | **FITS** ("free from confinement", Wikt sense 2); achievement aspect as `capture` | — |
| `flee` | D | FOLDED (scene move) | footwork break-off (`WR:151-183`); ends the scene undecided with the fleer standing; Event says so (M12) | ← ME *flen* ← OE *flēon* ← PWGmc \**fleuhan* ← PGmc \**fleuhaną* ← PIE \**plewk-*, \**plew-* (Wikt). **Germanic** | **FITS** | replaces `disengage`/`withdraw` |
| `lunge` | D | FOLDED (scene move) | commit ≥ `LUNGE_COMMIT` (`WR:259-260`) | ← F *allonge* ← OF *alonge*, *alongier* ← VL \**allongāre* ← *ad* + LL *longāre* ← L *longus* 'long' ← Proto-Italic \**(d)longos* ← PIE \**dlongʰos* (Wikt) | **FITS** (fencing) | replaces `rush` |
| `feint` | D | FOLDED (scene move) | low commit depth (`WR:262`) | noun ← F *feinte* ← *feindre* ← OF *feindre, faindre* ← L *fingō, fingere, finxī, fictum* 'shape, fashion … feign, pretend' ← PIE \**dʰeyǵʰ-* (Wikt la). English verb from the noun (Wikt) | **FITS** | — |
| `parry` | D | FOLDED (scene move) | `DEF_PARRY` (`vocabulary.py:69-72`) | ← earlier *parree* ← ME \**parree* ← OF *paree* ← ML *parāta* ← L *parō, parāre, parāvī, parātum* 'arrange; prepare, provide' ← PIE \**perh₃-* (Wikt); alternatively from F *parez*, imperative of *parer* (Wikt). The sense 'ward off' is a Romance development `[UNVERIFIED: date]` | **FITS** | — |
| `dodge` | D | FOLDED (scene move) | `DEF_DODGE` | dialectal *dodge, dod* 'jog, jerk', origin **uncertain**, perhaps PGmc \**dud-* (Wikt). No Latin | **FITS** | — |
| `grapple` | D | FOLDED (scene move) | contact branch (`WR:429-450`) | ← ME \**grapplen* ← OE \**græpplian* 'seize' ← PGmc \**graipilōną* / \**grabbalōną* ← PIE \**gʰrebʰ-* 'take, seize'; influenced in some senses by *grapple* 'hook' (OF *grapil*) (Wikt). **Germanic** | **FITS** | — |
| `interpose` | C, D | FOLDED (scene move of the N-party scene) | a third party entering another's scene (M7) | ← MF *interposer* (influenced by *poser*) ← L *interpōnō, interpōnere, interposuī, interpositum* 'put between; insert; pledge' (Wikt la) ← *inter* + *pōnō*. Wikt's root template \**tḱey-* belongs to the second element: *pōnō* ← Proto-Italic \**pozinō* ← \**po* 'off' + \**sinō*, a nasal-infix present of \**tḱey-* (Wikt la) | **FITS** ("interposed himself") | — |
| `strike` | D | CULLED | the exchange itself | ← ME *stryken* ← OE *strīcan* ← PGmc \**strīkaną* ← PIE \**streyg-* (Wikt). **Germanic** | **STRAINED** as a verb row: names the bout's unit; collides with the labour strike | — |
| `rush` | D | CULLED | = lunge | **disputed** (ME *ruschen*): (1) OE *hrysċan* ← PWGmc \**hurskijan* ← PGmc \**hurskijaną* ← PIE \**ḱers-*; (2) OE \**rūscian* ← PGmc \**rūskōną* ← PIE \**(o)rewə-*; (3) per the OED, AN/OF *russer* ← VL \**refūsāre* ← L *refundō* (Wikt) | **STRAINED**: ordinary sense is 'hurry' | `lunge` |
| `disengage` | D | CULLED | = flee | ← MF *désengager* (*dis-* + *engager*) (Wikt) | **FITS** the move (the verb means to release or break contact, military use included; the module's own trace kind is `disengage`), so the name is culled only because `flee` is the plainer word for a person: the verb itself means to release or break contact, military use included ("how American forces might begin to disengage in Iraq", Wikt); the fencing sense, "a circular movement of the blade that avoids the opponent's parry" (Wikt), is the noun | `flee` |
| `withdraw` | D | CULLED | = flee | ME *with-* 'away, back' + *drawen* ← PIE \**dʰregʰ-* (Wikt). **Germanic** | FITS in English, but collides with SC's `withdraw` (a petition, `v2-p8:441`) and MB's (`v2-p8:206`) | `flee` |
| `disarm` | D | CULLED (outcome) | drawn grab outcome (`contact.py:54`) | ← ME *desarmen* ← AN *desarmer* ← OF *desarmer* (*des-* + *armer*) ← L *armō, armāre, armāvī, armātum* 'to furnish with weapons, arm' (L&S) ← *arma* ← PIE \**h₂er-* 'to fit, join' (Wikt) | FITS as an outcome; not chosen | — |
| `kill` | A | CULLED (outcome; RS-5, ED-IN-0288) | the Felled band | ← ME *killen, cullen*, **obscure**: OE \**cyllan* ← PGmc \**kwuljaną* ← PIE \**gʷelH-*; or a variant of OE *cwellan*; or Old Norse (Wikt). **Disputed** | outcome, not an act | — |
| `wound` | A | CULLED (outcome; RS-5, ED-IN-0288) | the Wounded band | verb ← ME *wunden* ← OE *wundian* ← PGmc \**wundōną*; noun ← PIE \**wen-* (Wikt). **Germanic** | outcome, not an act | — |
| duel | B | not a verb (`VT:593-594`) | the name of what resolves | ← ML *duellum* ← Old Latin *duellum*, which survived as a rare classical byform of *bellum* 'war' (L&S: "duellum, v. bellum") and was reinterpreted as 'combat of two' by association with *duo* (Wikt); possibly via MF *duel* | — | — |

**Count after assessment.** Rows: 3 shipped kept and rebuilt (`fight`, `challenge`, `accept`), 4 new (`assassinate`, `capture`, `guard`, `rescue`; the first two are keys on `fight`'s one effect). Named contents: 4 (`ambush`, `shoot`, `champion`, the terms). Scene moves under IN-46: 8 names (`feint`, `lunge`, `parry`, `dodge`, `grapple`, `flee`, `yield`, `interpose`). Culled names: 4 (`strike`, `rush`, `disengage`, `withdraw`); outcomes: 3 (`kill`, `wound`, `disarm`). v2's PC set was 3 rows + 16 items (`v2-p8:383-402`).

---

## 3.5 Deduplication and culls

| group (near-synonyms or one act) | what was done | fold test / floor check |
|---|---|---|
| `fight` · strike · (attack, assault) | `fight` kept; `strike` culled | strike: not chosen at the season scale, either party, it *is* the exchange (no parameter). Floor: F1 is `fight`'s |
| `feint` · `rush`/`lunge` | one parameter (commit depth), two named poles; `rush` culled for `lunge` | same mechanic, same parameter. Floor F14 keeps both poles as moves |
| `parry` · `dodge` · (wind) | one parameter (`DEFENCE_MODES`) | values of one tuple (`vocabulary.py:72`) |
| `disengage` · `withdraw` · `flee` · (retreat) | one move, named `flee` | `disengage` as a noun is a blade action in fencing; as a verb it means breaking contact (FITS; culled for the plainer `flee`); `withdraw` and `retreat` are SC's and MB's (`v2-p8:441`, `:416`). Floor F10 keeps it |
| `assassinate` · `ambush` · murder | `assassinate` a key; `ambush` a content; murder an outcome-judgment (`VCD:2133`) | ambush is orthogonal to aim (it can carry a capture); assassinate differs in valuation and withheld attribution. F7, F8 kept |
| `capture` · GV's `arrest` · `seize` (a person) · kidnap | `capture` a key here; **recommend** GV's `arrest` be a second key on the same mechanic with a warrant content (§3.8) | `seize` declines a person (`v2-p8:708-709`, citing `VT:911`); `arrest` and `capture` are one act (take a person by the body contest) differing in a content (the writ) and in valuation. Kidnap is the unlawful *judgment* on a capture, not a second act. F5 kept |
| `yield` · `surrender` · submit · concede | `yield` for a person in a fight; `surrender` stays MB's (a held Rung, `v2-p8:420`); `concede` is SC's | different objects (one's own body vs a place vs an argument) |
| `guard` · `ward` · protect · `interpose` | `guard` the row; `interpose` its scene move; `ward` is TW's | guard/ward are doublets of one Frankish verb (Wikt; V-19). TW's `ward` protects by Thread, so the objects differ; flagged §3.8 |
| `challenge` + `accept` · K-23 (`petition` + `fight`) | pair kept; K-23 dead | K-23 composes SC's verb with another actor's reply (fails the the lane brief's test) and is struck (`VCD:3`) |
| `accept` · `fight` | `accept` kept as a key on `fight`'s effect | true equivalent by the fold test; kept as a key for precondition and valuation (`ROS:2876`, `:2923`, `:2988`) |
| `champion` · proxy · second | `champion` a content | true equivalent of `accept`/`challenge` with `for` |
| kill · wound · disarm · execute | outcomes, not verbs | kill/wound ruled (RS-5, ED-IN-0288; `VT:478-485`); disarm drawn; execute is Jordan's R-1 (`VCD:2648`) and the custodian's, not PC's |

**Every cull, with its floor check.**
- **`strike`** — fails the fold test (no parameter; either party). Nothing a floor act needs dies: F1 is `fight`, F14 keeps press and defend as moves.
- **`rush`** — same parameter as `lunge`. F14 keeps the lunge.
- **`disengage`, `withdraw`** — one move, named `flee`. F10 keeps it.
- **`kill`, `wound`, `disarm`** — outcomes; F1's results are the bands. Nothing dies.

**Stale text this lane found (not edited; for whoever edits `VT`/`EC`).**
- `VT:503`: "⚠ THE SLASHED NAME SURVIVES THIS COMMIT AND IS SEPARATELY RULED WRONG … landed as `challenge` -> `accept` alone" — the rename landed (`VT:478`), so the first clause is false; the sentence should be cut to its last clause.
- `EC:61` ("which is why the table's row is `kill / wound`") and `EC:117` (the `Unspecified` message "`kill / wound` on …") name the retired row.
- `VT:592-593`'s revert ("the duel composes as #453 K-23 has it") names a design struck at `VCD:3`.
- `VCD:4108` prices `fight` at "sacred −0.3"; `ROS:2344` has `fight: null`, "struck by R-C4.1". Stale.
- `kill.refused` (`VT:585`): an event kind named after a non-verb. `fight.refused` fits; renaming moves `content_hash()` (declared, as the `kill / wound` → `fight` rename did, `VT:485-491`).

**Critic findings on this lane's verbs.**

| finding | verdict | reason |
|---|---|---|
| L-01 (root sense as design intent) | **applied** | no design claim here rests on a root: `champion`'s *campus*, `rescue`'s *quatiō* and `challenge`'s *calumnia* are recorded, not used |
| L-01 gloss: *fight* "close, tugging struggle" | **applied** | Wikt: OE *feohtan* already 'fight'; \**peḱ-* 'pluck'; L *pectō* 'comb' (L&S) is a cognate |
| L-01 / V-13 gloss: *challenge* "accuse publicly and stand by it" | **applied** | L&S *calumnia*: "trickery, artifice, chicanery … false accusation"; the gloss drops the falsehood |
| L-12 (`accept` generic; resolves a duel with no challenge) | **applied** | STRAINED; the row is rebuilt to require the challenge Record; the 0-of-12 measurement (`VT:629`) is the R-COMPLETE failure |
| L-17 (`challenge` vs "Recognition Challenge", `references/action_vocabulary.yaml:48`) | **answered** | that roster is `status: provisional` (per V-21); flagged to SC rather than renaming a shipped row |
| V-02 (REJECT→MERGE classed three ways; PC's strike…disengage counted as upheld merges) | **applied and widened** | they were never merges: Suite D shows each is a scene move or outcome, so PC's "10 upheld" includes nine items that are not verbs |
| V-13 (*fight* "close struggle") | **applied** | as L-01 |
| V-16 (ransom → `pardon` mislabels the captor's side) | **answered** | not PC's row; agreed `pardon` is the wrong word for a captor's paid release; PC supplies the producer (`capture`); §3.8 FA |
| V-19 (`guard`/`ward` doublets) | **answered** | Wikt confirms the doublet; kept apart by object (a person's body vs a Thread protection); §3.8 TW |
| V-20 (`yield` homonym with `Rung.yield` and the inquiry yield) | **applied** | `yield` kept (ordinary for a duel); event kinds prefixed (`fight.yielded`), never bare `yield`. The module's trace kind `"yield"` (`WR:507`) is internal and reaches no season kind today |
| prompt caution 3 (`kill/wound` in `fight`'s cell note) | **applied** | the `VT:503` sentence and `EC:61`, `:117` are stale (above) |

---

## 3.6 Gap coverage table

One disposition per row. "Closed by X once M*n*" names the mechanic in §3.7.

| gap | disposition | note |
|---|---|---|
| PC-G01 | **closed by** `fight` (Suite A: kill and wound are its bands) | the stale `VT:503` sentence and `EC:61`, `:117` listed in §3.5 for deletion |
| PC-G02 | **OUT OF SCOPE** (GV/SC) | `execute` is a disposal of custody by the custodian's seat; R-1 is Jordan's (`VCD:2648`); PC supplies custody's combat producer (`capture`); §3.8 |
| PC-G03 | **closed by** `accept` once M3 | `accept` requires the challenge Record |
| PC-G04 | **closed by** `challenge` once M3 | PC-10b's Record is the carrier |
| PC-G05 | **closed by** `challenge`/`accept` (Suite B) | K-23 struck (`VCD:3`) and a composition; the revert clause at `VT:592-593` is stale |
| PC-G06 | **closed by** `challenge`/`accept` (§3.2 F2, F3) | grounded on the convention floor by `[MEMORY]` precedent; the *in-tree* research gap (`PCL:227`) remains a research task, not a verb gap |
| PC-G07 | **closed by** `challenge` (terms content) once M3, M4 | first blood / until one yields / to the death mirror historical duelling categories `[MEMORY]` |
| PC-G08 | **closed by** `yield` (term and move) once M4 | the seam must pass a Yield declaration; `fight.py:52` passes none |
| PC-G09 | **closed by** `fight`/`accept` once M1 | standing actor's wounds answered, not escalated: Jordan's "the combat engine determines the result there. your code just has to accept the result" (`EC:4-6`) covers both parties' wound state, which the seam already lifts (`SW:230`) [CONFIDENCE: medium — `march`'s winner silence (`EC:183-185`) is the counter-precedent, and it is MB's ruling, not PC's] |
| PC-G10 | **closed by** `fight` once M1 | both rows then follow whoever lost |
| PC-G11 | **OUT OF SCOPE** (a band edge, not a verb) | H-98 owns it; the engine carries no source for a fourth band |
| PC-G12 | **OUT OF SCOPE** (seam return) | K-PC-3 cuts `winner`; no verb reads it |
| PC-G13 | **OUT OF SCOPE** (parameter) | Jordan tuning (`PCL:361`) |
| PC-G14 | **closed by** `fight` once M13 | per-person inputs; K-PC-1 is already Jordan's |
| PC-G15 | **closed by** `fight` once M13 | the combat reader of `capability` is M13's; `train` is NP's (§3.8) |
| PC-G16 | **closed by** `fight` (and every Suite A/B key) once M2 | weight bound; under troop-stock candidate A a raised troop is a store, not a person (`proposals/2026-10-16-troop-stock-design.md:55-59`), and the population "never fights" a field (`:174`), so no personal-combat party should be a cohort |
| PC-G17 | **closed by** `guard` (and the `interpose` move) once M7, M8 | |
| PC-G18 | **closed by** `rescue` once M5 | `capture` is the producer v2's PARK trigger waited for |
| PC-G19 | **closed by** the Suite D moves once M11 | IN-46 needs a build batch (`workplans/valoria_master_workplan_v9.md:271`: "no build batch") |
| PC-G20 | **closed by** the Suite D moves once M11 | |
| PC-G21 | **closed by** `flee` (move) once M11 | `TRACE_KINDS` drift confirmed (`state_graph.py:21-25` lacks `disengage`; `WR:178`, `:183` emit it) |
| PC-G22 | **closed by** `grapple` (move); `disarm` is an outcome | **the "not activated" premise is stale**: `WR:435-450` runs the grab menu in every closed engagement with an opening; its outcomes reach only poise and initiative |
| PC-G23 | **closed by** `shoot` once M9 | |
| PC-G24 | **closed by** `challenge` (a field context) once M7 and MB's battle pause | MB reads the result as a fraction of the side (`PCL:103`, Dominions / M&B); §3.8 |
| PC-G25 | **closed by** `champion` (content) once M3's stakes have a reader | |
| PC-G26 | **OUT OF SCOPE** (surface) | odds display; K-PC-11 was withdrawn (`PCL:550`) |
| PC-G27 | **OUT OF SCOPE** (substrate) | K-PC-8 is Jordan's |
| PC-G28 | **OUT OF SCOPE** (IN, H-206) | K-PC-10: a vacancy claim at WITNESS; PC's killings are its trigger, not its owner |
| PC-G29 | **closed by** `fight` once M12 | the band's Event carries how the fight ended |
| PC-G30 | **closed by** `fight`/`challenge`/`accept` once M10 | IN-59 (a), BLK on IN-60 (`v9.md:276`) |
| PC-G31 | **OUT OF SCOPE** (NP/IN chooser) | `refusal_axis` (H-146) gates any act; not a verb |
| PC-G32 | **closed by** `fight` once M15 | the surviving subject's grudge on `march`'s shape; kin and witnesses are NP/IN (IN-72) |
| PC-G33 | **DISPUTED** | FA's K-FA-1 gating `fight` on war is rejected for personal combat: a murder, a duel or a kidnap in peacetime is floor (F1, F2, F5, F7), and VCD rules "Does a march need a war? No" (`VCD:3325`, via register). The war gate is MB's question for `march` alone |
| PC-G34 | **closed by** `assassinate` (key) and `ambush` (content) once M6 | |
| PC-G35 | **closed by** `capture` once M5 | arrest, pardon, ransom, hostage are GV/FA; §3.8 |
| PC-G36 | **PARKED** (trigger: a `determine` disposal reads a duel's result) | the judicial duel binds a bench through SC/GV's reader; PC supplies the stakes on the Record |
| PC-G37 | **OUT OF SCOPE** (IN witness channel) | dropped by disqualifier 1: witnesses hold `person.died` (`PCL:368`) |
| PC-G38 | **OUT OF SCOPE** (parameter, NP moral layer) | H-128 |
| PC-G39 | **OUT OF SCOPE** (NP: `tend`) | the raiser of `body` is NP's; §3.8 |
| PC-G40 | **closed by** `fight` once M13 | the module's 53 weapons and 7 traditions decide nothing until a person carries kit |

Tally: closed 27 (of which 23 wait on a named mechanic) · PARKED 1 · OUT OF SCOPE 11 · STALE 0 (two premises found stale inside closed rows: G05's revert clause, G22's "not activated") · DISPUTED 1. Total 40.

---

## 3.7 Mechanics this subsystem needs (named gaps)

Ordered bottom-up: the ones that change no store first.

| id | mechanic | what it must write | verbs that wait on it |
|---|---|---|---|
| M1 | **Two-sided band write** (K-PC-2) | `_eff_kill` reads each party's own `wound_state` (already lifted, `SW:230`) and writes each party's band; a felled actor gets `person.died`; the false `contest.undecided` for a fight whose starter fell disappears. A second `Subject` on the existing `Change`; no new store or kind | `fight`, `accept`, `assassinate`, `capture` |
| M2 | **Weight bound** (K-PC-12) | refusal conjunct: neither party `is_cohort` (`state/carriers.py:716`); refused acts emit the row's refusal kind | every Suite A and B key |
| M14 | **Distinguishing kinds** | `accept` emits a duel kind beside its band kind (so `KIND_VERB` maps it); `kill.refused` → `fight.refused`; yield/flight endings as `fight.yielded` / `fight.fled` in the band's Event, never bare `yield` | `fight`, `accept`, `yield`, `flee` |
| M15 | **The surviving subject's grudge** | on Wounded/Untouched, a stance row of the subject against the actor, on `_eff_march`'s grudge shape (`EC:181-199`, via `PCL:113`) | `fight`, `assassinate`, `capture` |
| M3 | **The challenge Record** (PC-10b) | a Record of kind `challenge`: holder = challenger, naming the challenged, `terms`, `stakes`, optional `for`; closed by `accept`; lapses at a term with a witnessed kind (calendar lapse precedent, via `PCL:552`) | `challenge`, `accept`, `champion` |
| M4 | **Terms in the scene** (PC-10a) | the seam passes `yield_decl` (`WR:487`), today never passed (`fight.py:52`); a *first-blood* stop rule (the scene ends at the first wound gate) — the module has none, and the seam may not edit it (`SW:27-28`), so this is a `modules/combat` change | `accept`, `yield` |
| M12 | **The band's Event says how it ended** (K-PC-9) | payload: felled / yielded / fled / undecided, and the decisive blow; replaces returning the whole trace (`SW:252`) | every attack key; `flee`, `yield` |
| M10 | **Co-location** (IN-59 (a)) | a refusal clause: the parties share a place (range-aware once M9) | every Suite A/B/C row |
| M5 | **Custody from a fight** | under `capture`'s aim, a Felled or yielded subject is not removed: a `detain` opens. `detain` is "prisoner -> a seat" (`ROS:115`): a captor holding a seat detains to it; a **seatless captor has no carrier** (§3.9 item 2). GV owns `detain` | `capture`, `rescue`; FA's ransom |
| M6 | **Cover and first move** | a held cover (FI's `conceal`, no row today) sets `first` (`WR:514`, a coin flip) and, by the cover's degree, withholds the actor at WITNESS (`loop/witness.py:588-592` names the actor of every act-caused Event today) | `assassinate`, `ambush` |
| M7 | **The N-party scene** (K-PC-5) | a second outer loop over `engagement()` (`WR:47`), never a fork; parties > 2; guards and present companions enter; a battle reads a named duel as a fraction of the side | `guard`, `interpose`, contested `rescue`, `champion` in a field |
| M8 | **The guard edge** | a person → person protective Tenure (an eleventh kind, `ROS:124`); §3.9 item 1 | `guard` |
| M9 | **A ranged resolver inside `modules/combat`** | a missile weapon kind in the one resolver (never a second one), and range in M10 | `shoot` |
| M11 | **Engagement cadence** (IN-46 / K-PC-4) | a played person's fight at ENCOUNTER, one engagement per act, pausing for the moves | the Suite D moves |
| M13 | **Per-person inputs** (K-PC-1, Jordan's) | attributes, experience and kit reaching the `Combatant` (`fight.py:45`); one equipment model with MB | every attack key |

---

## 3.8 Cross-subsystem flags

| other lane | verb or fold | the collision or dependency |
|---|---|---|
| **GV / SC** | `arrest` (planned, IN-12 step 5) vs PC's `capture` | one act (take a person by the body contest, open `detain`) differing in a content (the writ) and a valuation. Recommend: one mechanic, two keys (`fight`/`accept`'s precedent, `EC:34-35`) — `arrest` the warrant-bearing key, `capture` the warrant-less one. Whichever lane hosts, the effect is single-owned |
| GV / SC | `detain`'s holder | M5 needs custody held by a seatless captor, or a ruling that only seat-holders capture (§3.9 item 2) |
| GV / SC | `execute` (R-1, Jordan's), release or pardon of a captive | the custodian's disposals; PC writes the custody, not its end. `seize` declines a person (`v2-p8:708-709`) |
| GV / SC | judicial duel (PC-G36) | a `determine` disposal that reads a duel's result through the challenge Record's `stakes` |
| **FA** | ransom (V152) | its producer is `capture`; `pardon` is the wrong word for a captor's paid release (V-16 agreed) |
| FA | war gate (K-FA-1, PC-G33) | PC rejects a war gate on `fight`: personal violence in peace is floor |
| **FI** | `conceal` | `assassinate` and `ambush` read a held cover; `conceal` has no row (grep of `VT`: none). Its degree-keyed cover break is FI's |
| **MB** | `ambush` of an army | a content of `march` (`v2-p8:398`); one name, two hosts, same meaning (first mover from cover) |
| MB | duel inside a battle (F13, PC-G24) | a `challenge` issued in a field; MB pauses and reads the result as a fraction of the side (K-PC-5/M-6) |
| MB | `march` writes losers only; PC's M1 writes both parties | the S-methodology asymmetry moves to MB: whether a winning side takes casualties is ED-IN-0279's, MB's |
| MB | `withdraw`, `retreat`, `surrender` | PC uses `flee` (a person leaving a fight) and `yield` (a person giving up); MB keeps `retreat`/`withdraw` (a force) and `surrender` (a Rung) |
| MB | troop stock | a personal fight never takes a cohort or a troop store as a party (M2); attacking a population is MB's/GV's |
| **NP** | `tend` (PC-G39), `train` (PC-G15), grudge and grievance (PC-G32; NP-G16, G18, G40) | `fight` lowers `body` and NP's `tend` raises it; M13 is where `train`'s `capability` would reach combat; the kin's and witnesses' grievance after a killing is NP/IN's (IN-72), the surviving subject's grudge is PC's (M15) |
| NP | `oblige` (L-02 rename to `pledge`) | if IN-60's Query stays on `oblige` + presence for seat guards, it shares readers with `guard`'s edge; one owner should read both |
| NP / GV | a prisoner's escape | the prisoner's own act against `detain` (Mount & Blade `[MEMORY]`: captive lords escape); not PC's, and not `rescue` (different actor) |
| **IN** | IN-46, IN-59 (a), IN-60, H-206 (K-PC-10), D-V6 | M11, M10, M7/M8's reader, the vacancy after a killing, and the contents-aware value term that would turn `accept`, `assassinate` and `capture` from keys into contents |
| **SC** | the word `challenge` | PC's row holds the duel sense; "challenge a claim/ruling" in SC should use `dispute`. "Recognition Challenge" (`references/action_vocabulary.yaml:48`, L-17) is a provisional roster's |
| SC / FA / NP | the word `accept` | PC's row resolves a duel. Another lane wanting "accept terms / an offer" should use `commit` or its own word; if it must be `accept`, PC renames to `take up` |
| **TW** | `ward` | doublet of `guard` (V-19); kept apart only while TW's `ward` protects by Thread and not a person's body |
| **EC / FI** | `yield` | `Rung.yield` and the inquiry yield share the English word; PC's kinds are prefixed (`fight.yielded`) |
| **WT** | flight before a fight | a person avoiding a known attacker uses `move`; PC's `flee` is inside the scene only |

---

## 3.9 For Jordan

Two items survive the five answers (superseded · irrelevant · design document · precedent · architecture).

1. **A guard edge: may any person choose to protect any person?** (a) `guard` is the guard's own act, writing an eleventh Tenure kind (guard → ward) that the N-party scene reads — protection is a personal choice, and a friend, a hired sword or a servant may guard someone with no seat. (b) v2's form: no act; IN-60's security Query reads `oblige` + presence, so only sworn service to a *seat* protects, and only seat-holders are protected. *Tried:* not superseded (IN-60 is BLK, `v9.md:277`); not irrelevant (F11 is floor); design documents split (v2 V095 says (b); the the lane brief's no-workaround rule reads (b) as a composition of `oblige` and `move`); precedent leans (b) (CK3 `[MEMORY]`: the Bodyguard is a court *appointment*, the liege's act); architecture leans (b) by the meta-rule (a new store is presumed failed) and (a) by single ownership (one edge both the scene and IN-60 read). Two games: protection as servitude vs as a bond anyone can form.
2. **Custody by a seatless captor.** `detain` is "prisoner -> a seat" (`ROS:115`, ratified as intent, ED-IN-0288). (a) Widen it to person-held custody, so brigands kidnap and a landless knight takes a prisoner for ransom (Mount & Blade `[MEMORY]`: bandits hold prisoners). (b) Only a seat-holder can `capture`; a seatless attacker can only harm. *Tried:* no ruling supersedes ED-IN-0288's shape; the floor (F5, F6) wants (a); the architecture is indifferent (`detain`'s readers — `move`/`migrate` decline, muster excludes — read the prisoner, not the holder), so the answer overwrites ratified intent and is Jordan's.

*Answered here rather than escalated:* the standing actor's wounds (PC-G09: "accept the result", `EC:4-6`; written, [CONFIDENCE: medium]); keeping `assassinate` as a name despite its achievement aspect (the floor's word, and the act is an attempt carried by bands); `accept` kept and STRAINED rather than renamed (no other lane holds the word yet); K-23's revert struck (`VCD:3`). Already Jordan's and not re-raised: K-PC-1 per-person inputs, K-PC-8 one substrate, R-1 `execute`, D-V6 contents-aware value term.

---

## Limits

- Nothing was run: no probe re-measured the 205/400 felled-actor rate, the 0-of-12 `accept` link or the 1-of-63 cohort party; those are the lane file's and the row notes' measurements.
- `[MEMORY]` precedents (CK3, Mount & Blade, Romance of the Three Kingdoms, Total War: Three Kingdoms, GURPS, Burning Wheel, Blades in the Dark, the English wager of battle) were not checked against any source.
- Not opened: `canon/03_canonical_timeline.md` (quoted through the register), the `.audit` HEMA files, `loop/calendar.py`, `queries/inputs.py`, `03_VERBS_AND_LOOPS.md`, v2 `_part2`/`_part5`/`_part6`/`_part7` (first-pass files).
- Whether `determine` opens live `detain` edges in a shipped run (`rescue`'s second producer) is unmeasured [CONFIDENCE: medium].
- Etymology gaps tagged inline: the century of *challenge*'s 'call to fight' sense and *capture*'s verbal use; the Medieval Latin stage of *assassin*; the date of *parry*'s 'ward off'; *disarm*'s Latin link; which element of *interpose* carries Wikt's root template.

