# Verbs, v2 — part 15: Part VI.7, faction actions (FA)

## Status: PROPOSED (2026-10-17). Reference, not canon (`CLAUDE.md` §0.05): nothing here binds the game or is read by it. Merging ratifies nothing unless Jordan so rules. Static reading and static lookup only; no run.
## Parts, in reading order: [head](2026-10-16-verbs-01-thesis-and-persons.md) (§0, Part I Persons) · [`verbs-02`](2026-10-16-verbs-02-attributes.md) (Part II Attributes) · [`verbs-03`](2026-10-16-verbs-03-standards-roster-and-reconciliation.md) and [`verbs-04`](2026-10-16-verbs-04-critics-etymology-gaps-and-decisions.md) (Part III Verbs: standards, roster, reconciliation; critics, etymology audit, gap coverage, named mechanics, decisions) · [`verbs-05`](2026-10-16-verbs-05-what-verbs-do-to-the-world-1.md) and [`verbs-06`](2026-10-16-verbs-06-what-verbs-do-to-the-world-2.md) (Part IV What verbs do to the world) · [`verbs-07`](2026-10-16-verbs-07-roadmap-reliability-and-sources.md) (§5 Roadmap, §6 Reliability ledger, §7 Sources) · [`verbs-08`](2026-10-16-verbs-08-engine-findings-from-the-first-trial.md) (Part V: engine findings carried from the first-pass trial) · Part VI, the lexicon by subsystem: [`verbs-09`](2026-10-16-verbs-09-lexicon-personal-combat.md) PC · [`verbs-10`](2026-10-16-verbs-10-lexicon-mass-battle.md) MB · [`verbs-11`](2026-10-16-verbs-11-lexicon-social-contest.md) SC · [`verbs-12`](2026-10-16-verbs-12-lexicon-fieldwork-and-inquiry.md) FI · [`verbs-13`](2026-10-16-verbs-13-lexicon-threadwork.md) TW · [`verbs-14`](2026-10-16-verbs-14-lexicon-settlements-and-governance.md) GV · **this file** FA · [`verbs-16`](2026-10-16-verbs-16-lexicon-economy-trade-and-craft.md) EC · [`verbs-17`](2026-10-16-verbs-17-lexicon-world-travel-and-survival.md) WT · [`verbs-18`](2026-10-16-verbs-18-lexicon-npc-life-and-persons.md) NP · Part VII, the verb gap register (the evidence behind Part VI's coverage tables): [`verbs-19`](2026-10-16-verbs-19-gap-register-pc-and-np.md) PC+NP · [`verbs-20`](2026-10-16-verbs-20-gap-register-mb-and-fa.md) MB+FA · [`verbs-21`](2026-10-16-verbs-21-gap-register-sc-and-gv.md) SC+GV · [`verbs-22`](2026-10-16-verbs-22-gap-register-fi-and-tw.md) FI+TW · [`verbs-23`](2026-10-16-verbs-23-gap-register-ec-and-wt.md) EC+WT.

**How to cite this Part.** The lane's own sections are numbered 3.1 to 3.9; cite them as `FA §3.n` (for example `FA §3.9` for its items for Jordan). Gap ids (`FA-G01` …) resolve in Part VII (`verbs-20`). Abbreviations such as `VT`, `VCD`, `v2-p3` are defined in the lane's opening paragraphs; `v2-p3`, `v2-p4`, `v2-p8` are the first-pass v2 parts as filed at `716c253`. Old file names such as `…synthesis_part8.md` or `_part8` in the body also mean those first-pass files; the suite was later renamed `2026-10-16-verbs-NN-…`. Mechanic ids (`M1`, `M-1`, `M-WT-1`) are this lane's own.

**Rulings that override this section** (`verbs-03` §III.5; where this section and the roster disagree, the roster governs):

- R-01: `levy` is **MB's** row (FA's seat is the actor); FA's fold of `hire` into `recruit` is reversed (`hire` is EC's).
- R-05: the posting act is **`assign`**; the shipped documentless order keeps the name `dispatch` until Jordan rules (D-V7).
- R-06: `declare` stands as FA's own row; SC's rename is withdrawn.
- R-11: `succeed` is GV's row.
- R-17: ransom is a `covenant` content; the discharge on payment is `pardon`'s mechanic and its name is open.
- R-21: `turn` (FA, a content of `recruit`) and `suborn` (an aim, parked on J-C-6 as a content of FI's `bribe`) are different acts.

---

# FA — faction actions

Lane file for the per-subsystem verb rewrite. Read against the working tree of 2026-10-16 (main). Reference only (CLAUDE.md §0.05): nothing here is a mechanism; every "writes" names the carrier the code would have to write, and every carrier that does not exist is a named gap (§3.7).
Scope: every act a seat (or a person through a seat, `Act.via`) performs on another seat, its members or its territory. Under Layer 1 a faction never acts: "the actor is always the person holding the office" (`engine/season/rosters.yaml` `factions` note, opened). Gap register: Part VII (`verbs-20`), rows FA-G01…FA-G50 (MB rows skimmed for collisions).
Abbreviations: VT = `engine/season/verb_table.yaml`; RO = `engine/season/rosters.yaml`; VCD = `proposals/2026-10-03-verb-coverage-and-gap-fill.md`; p4/p8 = `proposals/2026-10-16-v2-person-troop-attribute-synthesis_part4.md` / `_part8.md`; TS1 = `proposals/2026-10-16-troop-stock-design.md`; XSC = `research/cross_scale_action_catalogue_v1.md`; FAL = `research/by_lane/FA_faction_actions.md`; L-nn / V-nn = the two critic reports. Etymology sources: **Wikt** = en.wiktionary via the lookup tool; **L&S** = Lewis & Short via the tool; `[UNVERIFIED]` = not checked with the tool.

---

## 3.1 Subsystem mechanic

**What FA has in the engine today** (each opened):
- **War** is a Query, not a flag: `queries/faction_q.py:219 at_war(w, a, b)` is True while any live `commit` points at a `WAR`-mood Proposition whose `{subject, value}` is the pair. Producers exist (`utter`, `commit`, VT:1267, VT:128) but no world-gen act utters WAR, and **nothing calls `at_war` outside its own tests** (grep of `at_war(` under `engine/` excluding `tests/`: the definition only).
- **Membership** is a live `commit` to the faction's creed Proposition (`queries/world_q.py:1152 members`, "THE WHOLE OF MEMBERSHIP AND THERE IS NO SECOND ROUTE"). **Service** is a live `oblige` to a seat (`faction_q.subordinates`, :199); the joiner opens it himself (VT:758, `eligibility: ["own"]`; RO `binds_bases`: "admission is the joiner's act").
- **The army** is `world_q.mustered` (:1257) = members ∩ present at the rung. It reads `commit` only: an obligee who is not a member is never mustered, and an ally never is.
- **Territory** is a `hold` Tenure on a Rung. `march` (VT:683, `remit:dispatch`) arrives on Won/Unopposed (IN-13); `seize` (VT:898, `remit:issue`) takes a Rung under occupation or a Record under warrant ("A SEAT is never seized"). `give` (VT:413) still takes a Record only, so cession has no row.
- **Orders**: `dispatch` (VT:268) writes `[]` and emits `order.given`; its only consumer is the witness channel `post_remit` (`epistemic.py:565`). `issue` (VT:441) mints a `dispensation` Record to an executor; `comply` (VT:144) answers it, writing nothing.
- **Upkeep**: `transfer` renews `oblige` terms paid through a seat (`loop/effects_economy.py:240 _renewals`). Nothing renews or lapses any inter-seat term.
- **Remit roster is closed**: `[issue, determine, confer, revoke, dispatch, convene]` (RO:303-311).

**What FA lacks:** a `covenant` row (VT has none); any reader of `at_war`; a public channel that survives SC-01 step 13 (p8:319-333); a seat-made declaration, proclamation, embargo or alliance reader; a recruiter's act; a troop-raising act (`levy` is designed in TS1 §3.1, not a row); runtime faction founding (the `factions` roster is read from `names_index.yaml`, RO `factions` note, so no faction can be born in play).

---

## 3.2 Convention floor

What a player of a faction/grand-strategy game expects a faction to do. Precedent games from memory are tagged `[MEMORY]` and name the mechanic relied on.

| floor act | precedent | state in tree |
|---|---|---|
| **recruit** persons into service (officers, retainers, agents) | RoTK series: the "Recruit" command persuades a free or captured officer to serve, success by the officer's loyalty/compatibility `[MEMORY]`; CK3 "Invite to Court" for knights/courtiers `[MEMORY]`; Root: each faction's "Recruit" action `[MEMORY]`; RTP Category F (`research/rise_to_power_roster_system_research_v1.md`, via register FA-G47) | **absent** as the recruiter's act (v2 V072 MERGE → `tell`, rejected by the user); the joiner's `oblige` is **shipped** (VT:758) |
| **raise troops** from one's land | Total War: recruit units at a settlement, drawing on its population/replenishment `[MEMORY]`; Mount & Blade: recruit from villages `[MEMORY]`; Birthright domain action "Muster Armies" `[MEMORY]`; XSC:106 "Muster" (BUILT in retired code); PW §1.3b (via register MB-G02) | **designed** (`levy`, TS1 §3.1:692-718, `remit:dispatch`) |
| **set assignments** (post an officer to a place or a task) | RoTK: assign officers to cities/posts and move them between cities `[MEMORY]`; CK3: councillor tasks per council seat `[MEMORY]`; Birthright "Lieutenant" action `[MEMORY]` | **shipped** in name only: `dispatch` writes nothing (VT:268-282); appointment to a seat is GV's `confer` (VT:168) |
| **hold territory** (take, keep, cede) | Total War, Civilization: capture a settlement, cede it in a peace deal `[MEMORY]`; EU4 peace terms "cede province" `[MEMORY]`; PW §4.1 (via register FA-G09) | taking **shipped** (`march` + `seize` Rung); ceding **planned** (`give` + Rung, B-R, v9 `verbs-05`:57 DEPS) |
| **declare war; make peace** | CK3/EU4 "Declare War" with casus belli, peace by negotiated terms `[MEMORY]`; Civilization "Declare War"/"Make Peace" `[MEMORY]`; Empires in Arms political phase (FAL:121-122, via 13G) | **designed** (v2 V091 preset of `utter`); the Query `at_war` **shipped**, unread |
| **treaty, alliance, truce, tribute, vassalage** | EU4/Total War diplomacy: alliance, non-aggression pact, military access, vassalise, tribute/payment demands `[MEMORY]`; CK2 truce with a priced breach (FAL:121, [CHECKED] there); XSC:135 "Treaty proposal" (STUB in retired code) | **planned** (`covenant`, IN-12 step 7; VCD §9.2:1755-1789) |
| **public announcement: edict, embargo, sanction** | Birthright "Decree" `[MEMORY]`; EU4 "Embargo" diplomatic action `[MEMORY]`; Civilization V "Denounce" `[MEMORY]`; XSC:152-160 Sanction ladder (Censure built, Embargo/Blockade/Outlawry NO) | **designed and deferred** (`proclaim`, VCD:2138, K-50) |
| **intrigue: plot, sabotage, subvert** | CK3 schemes with invited agents (murder, abduct, claim throne) `[MEMORY]`; RoTK VIII schemes that lower a rival's order (FAL:116); Birthright "Espionage" `[MEMORY]` | `sabotage` **planned** (IN-12 step 9); `conspire` **designed** (v2 composition) |
| **succession** to the head seat | CK3: the heir succeeds at death under succession law, claimants may contest `[MEMORY]`; HCC §2.1 (succession crisis acts) | **planned** (IN-61, `workplans/valoria_master_workplan_v9_part5.md:211`: `succeed` re-specified as the heir's own claim, RS-27/RS-29) |
| **ransom, hostages** | CK3 ransom of prisoners `[MEMORY]`; Mount & Blade ransom brokers `[MEMORY]`; RTP:360-364 F9 (via register) | **designed** (v2 V152 composition); `detain` Tenure kind **shipped** (RO `tenure_kinds`) |

Floor acts (kept regardless of NERS; only the build depth is open): recruit, levy, assign/dispatch, seize/cede, declare war and peace, covenant. Beyond the floor (earn by NERS): proclamation contents, conspiracy, sabotage, succession claim, ransom.

---

## 3.3 Suites

Nine suites. Each host is one row in the actor's voice; each fold is tested on three questions: **same actor? same mechanic? only a parameter or content differs?** A fold that needs another verb, another person's reply or several steps fails, and so does any v2 MERGE of that shape (user rule 5). The world effect names the carrier in the subsystem's own terms (§3.1).

### S1 · Covenant — binding agreements between seats · host `covenant`

**Host row (NEW ROW).** Actor: a seat-holder through his seat (`remit:issue`, VCD:1760, "via a seat only — an `own` alternative would let anyone mint a treaty"). Counterparty `to`: another seat's holder. The design changes VCD's row in one respect. **Acceptance is the second party's own `covenant` on the same instrument**, not a `commit`. Two grounds:
- English: "to covenant" is something both parties do (Wikt verb senses: "to enter into … a covenant", "to bind oneself in contract").
- The value term: §V.2.8 (p8:262-264) finds that `commit` is celled as a vow, "so a corrupt bargain reads as piety".

**World effect.**
- **First `covenant` (the offer).** It writes `Proposition.exists` (the terms, minted through `_eff_utter`'s one mint, VCD:2169-2171's shared-mint shape), `Record.exists` (a `dispensation` naming both parties, VCD:1766) and `Tenure.since` (the actor's own binding edge to the terms). It emits `covenant.offered`.
- **Second `covenant` on a held instrument (the seal).** The second party, holding the instrument (handed over by `give` or carried by an envoy, S5), writes his own edge and emits `covenant.sealed`. The instrument is **in force** while both edges are live. That is a Query, never a flag (`at_war`'s shape, `faction_q.py:219-251`).
- **Breach.** Breach is the breaker's own close of his edge through GV's closer (`release` today, VT:845; `commitment.ended` is already earned, VT:856), priced by one `deed:` cell (p8:154-172).
- **What it lacks** (§3.7): every reader. None of these exist yet: an in-force Query, a breach detector, alliance muster, truce ranking, a tribute due, a peace override on `at_war`, and successor binding (an edge is a person's, so a treaty lapses when its signer dies; whether the seat's next holder inherits it is unruled).

**Folded acts.**

| act | same actor? | same mechanic? | content only? | line |
|---|---|---|---|---|
| treaty | Y | Y | Y | the generic terms |
| peace (negotiated) | Y | Y | Y | terms naming a live war Proposition. Reader: `at_war` reads False for the pair while a later peace instrument between them is in force. Unilateral peace is the declarer's own release of his war edge (GV's closer, p8:136-146) |
| alliance | Y | Y | Y | terms "each musters with the other". Reader: `world_q.mustered` (:1257) also counts an in-force ally's members (FA-G07) |
| truce | Y | Y | Y | terms with a declared end (`Tenure.term`, `oblige`'s precedent, VT:775). Reader: breach priced above a treaty's, and the chooser ranks a march on a truce partner down. Not a refusal (VCD:2106-2108, direction 8) |
| tribute | Y | Y | Y | terms naming a recurring `kind`/`amount` due. Reader: the `_renewals` shape (`effects_economy.py:240`) over covenant dues. Needs the goods keys in `record_sourced_operands` (p8:111-132, RO:1708-1723). Content named `tribute`, not `due` (V-19) |
| cession (terms) | Y | Y | Y | terms naming a Rung one party will hand over. The handing-over is the holder's `give` + Rung (planned B-R), not this row |
| vassalage | Y | Y | Y | terms naming the lesser seat's subordination. Its performance is the vassal's own pledge (`oblige`, VT:758) |
| league | Y | Y | parameter | n > 2 parties, each sealing the same instrument; `to` is per act |
| ransom | Y (the captor offers) | Y | Y | terms "captive X freed against amount Y". Performed by the payer's `transfer` and the captor's discharge of the `detain` (GV's closer). V-16 applied: not `pardon` |
| hostage surety | Y | Y | Y | terms naming a person held in `detain` as surety. PARK until `detain` has a voluntary opener (FA-G30) |
| marriage alliance | Y | Y | Y | terms naming a marriage. PARK on NP's kin tie (K-NPC-6 / D-V2, p8:631) |

**Not folded.**
- `negotiate` (FA-G10) fails twice. It is several steps (offer, counter-offer), and its contested form needs a `negotiation` arrangement that is **not seeded**: `arrangements.yaml` rows are `arbitration`, `parliamentary_debate`, `council_of_state`, `legal_trial`, `tribunal`, `interrogation`, `inquisition_hearing`, and the file's header (:24) names `negotiation` only as a candidate. v2's form (p8:496) rests on a row that does not exist. In FA a negotiation is a series of `covenant` offers. A contested bargain is SC's to build (§3.8).
- `mediate` / `arbitrate` (V-04): the actor is a third party.
  - Arbitration is GV/SC's `convene` under `arbitration` (`arrangements.yaml:94`) plus `determine`.
  - Mediation is non-binding. **PARK**; trigger: a non-binding SC arrangement.
- `conspire`: concealed, many persons, not seats. It is S7.
- `surrender`: MB's preset of `give` under arms (p8:420).
- `betray`: V-09 applied. Betrayal is a witness judgement across acts; the breach that `covenant` prices is the breaker's open close.

**NERS.**
- **N:** floor. A cut kills every inter-seat agreement (peace, alliance, tribute, cession on terms). It is judged from all six directions:
  - top-down: the head's options;
  - bottom-up: persons who see a seal witness a seat's word;
  - vertical: vassalage;
  - diagonal: peace across a war;
  - lateral: seat to seat;
  - horizontal: EC's goods terms and SC's bargain.
  
  False N-line check: no ruled-in act supplies it. `utter` + `commit` gives a private promise with no counterparty, no seat gate and no in-force Query (VCD:1778-1780 already lists `covenant`'s conflict axes against `issue` and `petition`).
- **R:** strategic (whom to ally, what to concede). Narrative without a player: AI seats ally, pay tribute and break truces. Completeness at the extremes fails until two things are ruled: a signer's death, and a breach by a third person bound to neither edge.
- **S:** one method. The terms are a Proposition and the binding is the parties' own edges, the shape war and membership already use (one ladder). A breach goes through the one closer.
- **E (ratio):** one row carries eleven named contents. High against N and R. The cost is the reader list (§3.7).

**Precedent.** §3.2's diplomacy rows; FAL:121 (CK2 truce breach priced, [CHECKED] there); COMP1:487-502 (Diplomacy and Pax: cheap talk by default, binding the expensive exception, via register FA-G06).

**Gaps closed:** FA-G04, G05, G06, G07, G08, G09 (terms half), G10, G28, G48, G50 (the treaty-counting reader). **Open:** G30 (hostage, PARK), G43 (marriage, PARK).

**Disposition:** **NEW ROW** (`covenant`). Fold set as above. Falsifier: in a seeded season, two seat-holders' `covenant` acts on one instrument leave both edges live, and the in-force Query reads True. Control: one party alone leaves it False.

### S2 · Declaration — one seat's public stance toward another faction · host `declare`

**Host row (NEW ROW).** Actor: a seat-holder through his seat, `remit:dispatch` (the remit `march` uses, VT:687, so whoever may send the army may declare the war it fights) [ASSUMPTION: the war remit — basis: `march`'s eligibility; revert: `remit:issue`, VCD's `proclaim` row, VCD:2161]. Subject: the target faction's Proposition. Stratum `binding_decision`, so `_ch_chronicle` carries the event kind to everyone alive (`epistemic.py:546-572`, as p8:324 reads it).

**World effect.** It writes `Proposition.exists` (mood by content: `WAR` for war, `faction_q.WAR_MOOD`) and `Tenure.since` (the declarer's own edge). It emits `war.declared` (an earned kind per content, p8:154-168's mechanism).
- **Fixes against v2.** The row writes the declarer's edge in its own effect, so FA-G03's "computed `commit` ranked last" cannot leave "a war of one". The verb supplies `mood`, so FA-G02's computed-`OUGHT` problem does not arise.
- **The seat clause** (v2 FA call 5, p8:687) moves into the row's eligibility. `at_war` then counts only WAR Propositions a `declare` minted, so a private `utter` of mood WAR no longer makes a war [ASSUMPTION: the Proposition carries its minting act or `at_war` reads it from the log; neither is checked here].
- **What it lacks:** a reader of `at_war` (none, §3.1), and a public channel that survives SC-01 step 13 (p8:327-328, `workplans/valoria_master_workplan_v9_part6.md:68`, quoted at p8:327).

**Folded acts.**

| act | same actor? | same mechanic? | content only? | line |
|---|---|---|---|---|
| war | Y | Y | Y | mood `WAR`, subject and value the two factions (`at_war`'s match, `faction_q.py:244-250`). Built first; the row's alignment cells are war's |
| embargo / sanction | Y | Y | Y | mood naming a trade ban on the target faction. **PARK**; trigger: EC's ban-term reader (p8:113-126) and a ruling that a crossing earns a breach kind rather than a refusal |
| condemnation (an organization outlawed, heresy declared) | Y | Y | Y | a `HOLDS` Proposition naming the target's creed. **PARK** on the accusation reader (VCD:1481 row "Heresy declared") |
| `proclaim` (the name) | — | — | — | **culled as a name in FA.** Its VCD row's subject is a Rung in one's own purview (VCD:2164-2165), so it cannot mint a war (VCD:2188-2190), and an edict to one's own purview is governance. That act is GV's (§3.8) |

**Not folded.**
- `utter` (any person, `own`, `social`; VT:1267). It differs in actor class and stratum, and so v2's preset (p8:491) fails the fold test on the mechanic.
- Peace: S1, or the declarer's own release.
- Show of force: MB's `march` posture (MB-G50).

**NERS.**
- **N:** floor ("declare war" is in every grand-strategy game, §3.2). A cut leaves `at_war` with no lawful producer. Directions: top-down (the head opens a war), bottom-up (persons hear of it), vertical (the seat's members are at war), lateral (faction to faction), diagonal (war to march via M1), horizontal (peace through S1). False N-line: `utter`+`commit` can set `at_war` today (`faction_q.py:235-241`), but only privately and by anyone, so it does not provide the floor act.
- **R:** war as a dated, public, attributable act; AI seats declare without the player.
- **S:** the war is one Proposition, read by the one Query. It pauses correctly once the reader exists: peace is a covenant or a release, never a flag.
- **E:** one row, three contents, one built.

**Precedent.** §3.2 row 5; FAL:121-122 (Empires in Arms' fixed declaration step).

**Gaps closed:** FA-G01 (once a reader exists), G02, G03, G32 (publicity, once D-V3 picks the channel), G31 (FA half), G33 (PARK content). **Open:** which act `at_war` gates (MB-G15, CMP:140 X-7).

**Disposition:** **NEW ROW** (`declare`), war content first. **Reverses v2 V091's preset of `utter`.**
- Ground: the fold test (actor class and stratum differ). This follows D-V6's own "refuse" branch (p8:635: "refuse: `declare (war)` needs an own row") without waiting on the lever.
- Falsifier: a `declare` through a seat makes `at_war(a, b)` True and leaves a `war.declared` claim held by a non-co-located person in the same season. Control: a private `utter` of mood WAR leaves `at_war` False.

### S3 · Recruitment — taking persons into a seat's service · host `recruit`

**Host row (NEW ROW).** Actor: the recruiter, a seat-holder through his seat. Eligibility `remit:confer`, establish's precedent for a seat-structural act (VT:283-287) [ASSUMPTION; basis: `establish`; alternative: `hold:<office>`, the seat's own holder]. Counterparty `to`: the person recruited (a known person; a `ban` holder is refused, per RO `tenure_kinds` note: "`oblige` refuses a `ban` holder service").

**Contested.** ED-IN-0210 Ruling 1 (VT:22-24) asks for "a COUNTERPARTY, an OBSTACLE and a DEGREE".
- The obstacle is the recruit's own standing: his live `oblige`/`commit` to a rival seat or faction, his regard for the recruiter, and his opinion of the faction once IN-70 lands (`workplans/valoria_master_workplan_v9_part5.md` IN-70).
- The recruit's will enters as the obstacle the act is rolled against. **No reply act is needed**, which is what rule 5 asks.

**World effect.**
- On the winning band it writes `Tenure.since` + `Tenure.term`: the recruit's `oblige` to the exercised seat, the edge kind the joiner's `oblige` opens (VT:775). The upkeep and lapse are already built (`_renewals`).
- Precedent for one act opening an edge another person owns: `determine` "opens an `oblige` owned by the party it binds" (VT:861 `disposal_release_note`), and `confer` opens the conferee's `hold`.
- Emits `service.entered`; the losing band emits `recruit.declined`, a witnessed refusal.
- **What it lacks:** `mustered` reads members only (`world_q.py:1257-1275`), so a recruited obligee who is not a creed member never fights for the seat. This is a named MB/FA mechanic (§3.7 M3).

**Folded acts.**

| act | same actor? | same mechanic? | content only? | line |
|---|---|---|---|---|
| hire | Y (the employer) | Y | parameter: the term's upkeep | "paid service" is already the `oblige` term renewed by `transfer`. V-06 applied: hire is the employer's act, so it folds here, not into `oblige` |
| enlist / retain | Y | Y | Y | synonyms; no content difference; names only |
| turn (an enemy's man) | Y | Y | content: the recruit keeps his rival edge and the new edge is concealed | **PARK**; trigger: `conceal` (IN-12 step 10, FI) and the recipient-side reader (p8:271-276) |

**Not folded.**
- `oblige`: the joiner's own act, a different actor (L-02; rename to `pledge` proposed for GV/NP, §3.8).
- `confer`: fills a seat (GV).
- `levy`: troops (S4).
- Conversion to a creed: SC's persuasion.
- `suborn`: the name is culled (§3.5, V-05).

**NERS.**
- **N:** floor (the user names it). A cut leaves no recruiter's act, only v2's `tell` + reply, which the user rejected.
  - From the six directions: top-down (the head builds a following), bottom-up (persons are offered service and refuse), vertical (seat to person), lateral (poaching a rival's man), horizontal (SC's contest resolver, EC's wages), diagonal (a retinue mustered for a march, once M3 lands).
  - False N-line: the joiner's `oblige` exists, but no seat can initiate it, and its `formation_decline_note` (VT:778) measured 0 of 4,451 referents as a seat. No computed `oblige` forms.
- **R:** customisation of a faction's people; AI factions compete for persons.
- **S:** one edge kind for service, from either side; one upkeep ladder.
- **E:** one row with three named contents.

**Precedent.** §3.2 row 1 (RoTK Recruit; CK3 Invite to Court; Root's Recruit); RTP Category F (via register).

**Gaps closed:** FA-G47; FA-G27 (`suborn` half, PARK as `turn`). **Open:** M3 (muster reads service).

**Disposition:** **NEW ROW** (`recruit`). **Voids v2 V072 MERGE → `tell`.**
- Falsifier: a seeded `recruit` of a known, unattached person opens his `oblige` to the seat. Over seeds, a person with a live `oblige` to a rival seat declines more often than one with none (control: the same pair with the tie removed).
- If the degree distribution does not move with the tie, the obstacle is not reading the recruit.

### S4 · Raising troops — a seat raises men from its land · host `levy`

**Host row (NEW ROW; designed in TS1 §3.1:692-718).**
- Actor: a seat-holder through his seat, `remit:dispatch`. Subject: a settlement Rung in the seat's purview. Stratum `binding_decision`.
- Cell: `requisition`'s two conjuncts, purview `authority` and a `stores` threshold (TS1:705-709).

**World effect.** It writes `Rung.stores` in one `Change`: `recruits −n`, `troops_raw +n` (TS1:775-776). It emits `levy.raised`, with refusals `levy.unauthorized` (the seat) and `levy.refused` (the place). The force is MB's, the pool is GV/SE's settlement store, and the act is the seat's.
- **What it lacks** (§3.7 M4): the `recruits` matter kind, `recruit_ceiling`, its regrowth with a claim producer (TS1 §2.1-2.3), and the troop body (J-1). None exists in RO today: `grep -c recruits engine/season/rosters.yaml` returns 0.

**Folded acts.**

| act | same actor? | same mechanic? | content only? | line |
|---|---|---|---|---|
| conscript / draft | Y | Y | Y | synonyms; names only |
| raise (a levy) | Y | Y | Y | the gloss, not a second name |

**Not folded.**
- Hire mercenaries ("troops for coin"). TS1:806 refuses it because "it mints men from matter". **PARK**; trigger: a mercenary pool carrier (a stock held by a non-settlement). If built, it is a `recruit`-shaped contract with a company's head, not `levy`.
- `muster`: a Query (TS1:803).
- `disband`: MB's (TS1:805, PARK).
- The political cost of raising: PARK on Jordan's ask (TS1 §2.10).

**NERS.**
- **N:** floor. A cut leaves armies as summed body weight (MB-G01). Directions: top-down (the seat raises), bottom-up (the settlement's pool falls), vertical (rung to seat), lateral (rival seats draw on contested land), diagonal (raised men to a field), horizontal (the `stores` ladder shared with EC). False N-line: `requisition` cannot carry it (Jordan: "levy typically doesn't refer to goods/stores", TS1:28).
- **R:** where and when to raise is a strategic choice that drains a settlement.
- **S:** the same `stores` ladder as `requisition` and `transfer` (one quantity, one method).
- **E:** one row.

**Precedent.** §3.2 row 2; PW §1.3b; PMM M-6 (via register MB-G02).

**Gaps closed:** FA-G22 (the seat half; the force is MB's). **Open:** MB-G53's political cost (PARK).

**Disposition:** **NEW ROW** (`levy`).
- Name risk (L-03): old `levy.refused`/`levy.unauthorized` counts in `requirements.yaml`/`hole_register.yaml` name the store act. TS1:730-734 re-keys them first.
- Falsifier: TS1's exit — `recruits` falls by n and `troops_raw` rises by n on one rung in one fold.

### S5 · Orders and posting — the seat sends or posts a person under it · host `dispatch`

**Host row (REBUILD of VT:268-282).** Today it writes `[]`, emits `order.given`, and "names a person; their own choose decides" (VT:281). No decision reads `order.given`; its only consumer is a witness channel (`epistemic.py:565`).
- Rebuilt: the actor (a seat-holder, `remit:dispatch`) **posts a named obligee of the exercised seat to a place, with a task**.
- Refusal (`dispatch.refused`) when the named person has no live `oblige` to the seat. He is not the seat's to send; this is the test `_renewals` already asks (`effects_economy.py:240-265`).

**World effect.** It writes `Tenure.payload` on the obligee's live `oblige` edge (the posting: rung and task; `establish` already writes `Tenure.payload`, VT:291). For a posting elsewhere, it relocates him through `move`'s one body (`loop/effects_migration.py:91 _relocate(w, a, dest, mover)`, which already takes a mover other than the actor; the same re-homing `march` performs through a seat, VT:698-708). It emits `order.given`; the posting earns `posted`.
- His answer afterwards is his own: `comply`, or `evade / defy` (desertion is his `move` away).
- **What it lacks:** a reader of the posting, so that the obligee's question source carries his task (§3.7 M5).

**Folded acts.**

| act | same actor? | same mechanic? | content only? | line |
|---|---|---|---|---|
| assign / post (a standing duty where he is) | Y | Y | parameter: no relocation | the user's "set assignments" |
| send an envoy | Y | Y | content: the posted man carries the seat's covenant instrument | his latitude (Kautilya's three envoy types, RHET:226 via register) **PARKS** on the instrument's terms range (FA-G11) |
| garrison (post a man to a settlement's `garrison` Site) | Y | Y | content | the troop-stock garrison is MB's |

**Not folded.**
- `issue`: GV's; a `dispensation` Record to an executor, read through `comply` (VT:441-490). After the rebuild the two differ by write row: a posting on a service edge against a document. That answers FA-G14's collision.
- `march`: MB's.
- `confer`: GV's.

**NERS.**
- **N:** floor ("set assignments"). Directions: top-down (the head places his men), bottom-up (an obligee receives a task), vertical (seat to servant), lateral (an envoy to another seat), diagonal (a garrison posting feeds a field), horizontal (`move`'s body, `comply`'s answer). FA-01 pins five heads acting through it (`engine/season/tests/test_fa01_head_seats.py:56-59`, opened), and `march`'s eligibility is `remit:dispatch`. False N-line: `confer` makes a man the holder of a seat, not the bearer of a task; `issue` makes a document.
- **R:** officers placed where they matter; AI seats post agents.
- **S:** the same service edge as recruit and upkeep; posting reuses `move`'s body.
- **E:** one row, three contents.

**Precedent.** §3.2 row 3 (RoTK posting; CK3 council tasks; Birthright Lieutenant).

**Gaps closed:** FA-G11 (PARK half), G12, G13, G14. **Open:** M5 (the posting's reader).

**Disposition:** **REBUILD** (name kept). The name FITS once the row sends: the Wikt verb senses "to send (a person) away hastily" and "to send (a journalist) to a place in order to report". L-05's objection rests on the noun (a written message), and that objection holds only for the row as it stands, which sends nobody.
- Falsifier: a `dispatch` of an obligee to another rung leaves his `contain` at that rung and a posting payload on his `oblige` edge. Control: a `dispatch` naming a non-obligee emits `dispatch.refused` and moves nobody.

### S6 · Territory — taking and holding places · host `seize`

**Host row (KEEP-AS-IS, shipped VT:898-923).** Actor: a seat-holder through his seat (`remit:issue`). It takes a Record under warrant or a settlement under occupation, writing one hold closed and one opened (`Tenure.until`/`Tenure.since`) and emitting `record.seized` or `rung.seized`. "A SEAT is never seized" (p8:354, VT:911).

**Folded acts.**

| act | same actor? | same mechanic? | content only? | line |
|---|---|---|---|---|
| conquer / take (a town) | Y | Y | Y | names for the Rung half; no content difference |
| annex | ? | N | — | **not folded, PARK.** RO `conferral_bases` lists `annex` as a way to fill a seat and states "Which act fills an `elected` or an `annex` seat is not ruled" (RO:2001-2019). Owner GV (§3.8) |

**Not folded.**
- `cede`: the holder's consensual handover. That is `give` + Rung (planned B-R; `give` is SC/GV's row, VT:413), a different actor and stratum (`social`, consensual; VT:915 cited at p8:244). FOLD into `give` (§3.8).
- `raze`: MB.
- `claim` (a title): **CULLED** as a name. It collides with the `Claim` carrier and `claim.*` kinds (VCD:2125-2127), and no casus-belli reader exists ("A march needs no war", VCD:1749).
- Garrison: S5 / MB.

**NERS.**
- **N:** floor ("hold territory"). A cut leaves occupation that never changes title.
- **R/S:** one hold-transfer shape, shared with `give`.
- **E:** unchanged.

**Gaps closed:** FA-G38 (once the Church-appetite Query exists, §3.7). **Open:** FA-G41's annex (GV).

**Disposition:** **KEEP-AS-IS.** Falsifier: a computed `seize` of an occupied Rung executes and `rung.seized` is earned (IN-13's test; not re-run here).

### S7 · Intrigue — a plot against a seat · host `conspire`

**Host row (NEW ROW).** Actor: any person (`own`); plotting needs no seat. Counterparty `to`: a person invited into the plot.
- Contested: the obstacle is the invitee's loyalty to the target seat (his live `oblige`/`commit` to it) against the plotter's standing.
- The first `conspire` with no plot held mints the plot: `Proposition.exists`, mood `OUGHT`, its predicate naming the target seat, plus the plotter's own edge.
- Each later `conspire` on a held plot opens the invitee's edge to it on the winning band. Precedent for opening another's edge: S3. The consent is the degree [ASSUMPTION; basis: `determine`'s and `confer`'s openers; revert: the invitee's own `commit` as his reply, which rule 5 forbids for a floor act and which this act is not].

**World effect.** `Proposition.exists`, `Tenure.since`. It emits `plot.joined` on the winning band. On the losing band it emits `plot.refused`: the invitee now holds a claim against the plotter (he may denounce him; that petition is SC/GV's).
- **What it lacks:**
  - `conceal` (until it exists, co-located persons witness a plot; p8:303-317);
  - a reader that turns a plot's members toward its act (§3.7 M7).

**Folded acts.**

| act | same actor? | same mechanic? | content only? | line |
|---|---|---|---|---|
| plot / scheme | Y | Y | Y | names only |
| coup | Y | Y | Y | the plot's predicate names the head seat. Its execution is GV's `depose` (PARK, p8:485) or PC's `fight` with `conceal` |

**Not folded.**
- `bribe`: FI's own row (p8:456).
- `sabotage`: S8.

**NERS.**
- **N:** beyond the floor (§3.2 row 8 is a strong convention: CK3 schemes). A cut leaves no many-person covert act; `covenant` is seat-only and public (p8:359).
- **R:** narrative without a player — plots form among the discontented, and a refused invitation is drama.
- **S:** edges are the same kind as membership and war (one ladder).
- **E:** one row.

**Precedent.** §3.2 row 8; RTP:321-322 F1; HCC:42-45 §2.1 (via register FA-G26).

**Gaps closed:** FA-G26. **Open:** M7.

**Disposition:** **NEW ROW.** It voids v2 V150's composition (`utter` + each conspirator's `commit` + `conceal`), which fails rule 5 on other actors' replies and on several steps.
- Falsifier: a `conspire` on a held plot opens the invitee's edge on Won only. Over seeds, an invitee with a live `oblige` to the target seat refuses more often.

### S8 · Covert damage · host `sabotage`

**Row (PLANNED, IN-12 step 9; VCD:1865-1891).** Actor: any person (`own`/`presence:<site>`). It writes `Site.condition` negative by `_rise`'s mirror and emits `site.damaged`.
- FA's use is denying a rival's muster or works: RoTK VIII's schemes (FAL:116, thin); PMM M-5 (via register FA-G35).

**Folded acts.** None. Spy → FI's `surveil`, out of FA (§3.8). Poisoning a well or burning a granary: `sabotage` on a Site, content only.

**NERS.**
- **N:** "the only act that LOWERS `Site.condition`" (p4:215). The false N-line is VCD's own [DISAGREE] at :1886-1889: emptying a works' store stalls a works but lowers no built Site.
- **R:** cheap asymmetric harm.
- **S:** one formula with `restore`, opposite sign (K-09).
- **E:** fine.

**Gaps closed:** FA-G35. **Disposition:** **KEEP** (planned row stands). Falsifier: VCD:1883 (`Site.condition` falls with a computed `sabotage` among its causes).

### S9 · Succession and founding · host `succeed`

**Row (REBUILD, planned by IN-61, `workplans/valoria_master_workplan_v9_part5.md:211-216`).**
- Under RS-27/RS-29 (Jordan: "designated heir is not a verb but a status or title. the heir still has to claim their throne"), the actor is the **heir**, holder of the registered heir seat (`off_heir`). He claims the vacant throne.
- The act opens the throne's `hold` under the new conferral basis `inheritance`, which `confer` may not exercise (IN-61 WHAT).
- Today's row (VT:935-965: the holder designates, effect declined) is the reading IN-61 retires.

**World effect.** `Tenure.since` (the heir's `hold` on the throne; his `off_heir` hold closes). It emits a succession kind. Waiting on IN-61's own exit: "a death followed by the title-holder's `succeed` claim opening the throne's hold".

**Folded acts.**

| act | same actor? | same mechanic? | content only? | line |
|---|---|---|---|---|
| claim (the throne) | Y | Y | Y | the act itself; `claim` is not used as a name (S6) |
| contest (a rival's claim) | N | — | — | **not folded.** The rival's petition is docketed under SC-04's `succession` arrangement (`workplans/valoria_master_workplan_v9_part6.md:138`): GV/SC |

**Not folded.**
- `designate`: **CULLED.** It is the King's `confer` of the heir title (IN-61 WHAT; RS-27).
- `abdicate`: GV's seat resignation on `release` (p8:484; L-08 proposes `resign`).
- `depose`: GV PARK.
- `found` (a faction): **PARK.** No faction can be born at runtime; the `factions` roster is read from `names_index.yaml` (RO `factions` note, opened). Trigger: a runtime faction carrier (FA-G39, H-186). `found` already names Rung creation (VT:367), so a faction-founding row would be a second sense. Owner GV/FA (§3.8).
- `establish`: GV (an office).

**NERS.**
- **N:** floor (succession; §3.2 row 9). False N-line: `confer` cannot fill an `inheritance` seat by design (IN-61).
- **R:** succession crises without a player.
- **S:** one basis read at the gate.
- **E:** one row.

**Gaps closed:** FA-G15 (the name now FITS: the heir succeeds — Wikt "to replace or supplant someone … vis-à-vis an office"; L&S *succēdō*, "regno successit"), FA-G16 (once IN-61 lands).

**Disposition:** **REBUILD per IN-61.** This **reverses v2's CUT** (p4:148). v2 read RS-27 as "against `succeed` and `designate` as verbs" (p4:93). RS-27 retires designation only, and its second sentence ("the heir still has to claim their throne") makes the claim an act, which IN-61 gives to `succeed`. Falsifier: IN-61's own (a hold opened through `inheritance` for a non-heir → fail).

---

## 3.4 Lexicon table

Chains: English ← Middle English ← (Anglo-Norman / Old / Middle) French ← Latin lemma (principal parts; attested sense) ← PIE. Sources: Wikt = en.wiktionary English entry; Wikt-la = Wiktionary Latin entry; L&S = Lewis & Short; all three fetched with the tool. "←" links without a source tag carry the tag of the link before them. `[UNVERIFIED]` marks a link not checked with the tool. Fit is judged by current ordinary usage (ED-IN-0179), not by the root.

**Hosts**

| verb | suite | status | mechanic and world effect | etymology chain (sources) | fit | rename |
|---|---|---|---|---|---|---|
| `covenant` | S1 | NEW | a seat's offer or seal of terms. Writes `Proposition.exists`, `Record.exists` (dispensation) and the party's own edge; in force while both parties' edges are live | covenant ← ME *covenaunt* ← OF *covenant* (pres. ppl. of *covenir*) ← L *conveniēns*, pres. ppl. of *conveniō, -īre, convēnī, conventum* (Wikt). Wikt-la senses: "to convene, assemble … come together"; "to be agreed upon" ← *con-* + *veniō* ← PIE \*gʷem- 'come' (Wikt-la) | FITS: "to enter into, or promise something by, a covenant" (Wikt verb). Risk: a religious register in a setting with a Church (VCD:1757). It shares its root with `convene` (V-19): noted, no clash in use | — |
| `declare` | S2 | NEW | a seat's public stance toward another faction. Writes `Proposition.exists` (mood WAR first) and the declarer's own edge; `binding_decision`, so public | declare ← ME *declaren* ← OF *declarer* ← L *dēclārō, -āre, -āvī, -ātum* (Wikt; L&S): "to make clear, plain, evident … to show, manifest, declare"; L&S sense B, "in pub. law lang. … to announce any one in public session as elected to an office … to declare or proclaim publicly" (*declaratus rex Numa*, Liv. 1, 18) ← *dē-* + *clārus* ← PIE \*kelh₁- (Wikt-la *clārus*: \*kl̥h₁rós) | FITS: "to assert or announce formally, officially" (Wikt). "Declare war" is the idiom | — |
| `recruit` | S3 | NEW | the recruiter's contested offer of service. On Won writes the recruit's `oblige` (+ term) to the exercised seat | recruit ← F *recruter* ← F *recrue* 'new growth; levy' (pp. of OF *recreistre*) ← OF *re-* + *creistre* (Wikt fr) ← L *crēscō, -ere, crēvī, crētum* 'to rise, grow, increase' (Wikt-la; L&S); cf. L *recrēscō* "to grow again, to grow up or increase again" (L&S) ← PIE \*ḱreh₁- (\*ḱer- 'grow') (Wikt-la). The French→Latin step goes through OF, not directly from *recrēscō* | FITS: the ordinary verb for taking people into service or an army, in the recruiter's voice | — |
| `levy` | S4 | NEW (designed TS1) | a seat raises men: `Rung.stores` recruits → troops_raw | levy ← AN *leve* ← OF *levee* ← OF *lever* 'raise' (Wikt) ← L *levō, -āre, -āvī, -ātum* "to lift up, raise, elevate" (L&S *lĕvo*; Wikt-la), from *levis* 'light' ← PIE \*h₁lengʷʰ- (Wikt-la *levis*). Wikt gives the English source as *lēvō*; L&S and Wikt-la have *levō*/*lĕvo* in this sense | FITS: Wikt verb senses "to draft someone into military service"; "said of troops, to form into an army by enrollment, conscription". STRAINED only for its old store sense (L-03) | — |
| `dispatch` | S5 | REBUILD | post a named obligee to a place with a task. Writes `Tenure.payload` on his `oblige` and, for a posting elsewhere, his `contain` (via `_relocate`) | dispatch ← Sp. *despachar* and/or It. *dispacciare*; second element uncertain: VL \*pactāre / \*pactiāre or L *-pedicāre* ← *pedica* 'fetter' ← *pēs* 'foot' (Wikt); first attested 1517 (Tunstall). PIE via *pēs*: \*ped- [UNVERIFIED: the *pedica* path is one of three Wikt gives]. No secure Latin ancestor | FITS once the row sends: "to send (a person) away hastily", "to send (a journalist) to a place in order to report" (Wikt). MISFIT for the row as shipped (sends nobody; L-05). A minor second sense, "to make a speedy end of" (Wikt), is harmless in context | — (kept by ED-IN-0210; see §3.9) |
| `seize` | S6 | SHIPPED, KEEP | take a Record under warrant or a Rung under occupation; one hold closed, one opened | seize ← earlier *seise* ← ME *seisen, saisen* ← OF *seisir* ← early ML *sacio* (8th c.) ← Old Low Frankish \*sakjan ← PGmc \*sakjaną / \*sakaną (Wikt); "cognate to *sake* and L *sāgiō*" (Wikt), cognate, not ancestor. **Not a Latin word**: Medieval Latin carried it late, from Frankish | FITS: "to deliberately take hold of; to grab or capture" (Wikt) | — |
| `conspire` | S7 | NEW | draw a person into a plot against a seat; mints the plot Proposition and opens edges to it on Won | conspire ← ME *conspiren* ← OF *conspirer* ← L *cōnspīrō, -āre* (Wikt; Wikt-la head *1+.nopass*): "to plot or conspire"; "(music) to sound in unison" (Wikt-la) ← *con-* + *spīrō* 'breathe' ← PIE \*(s)peys- (uncertain: Wikt-la tags it `unc`; De Vaan's onomatopoeic suggestion is quoted there). L&S *conspiro1*: *cōnspīro, āvi, ātum*, 1, "to blow or breathe together, to sound together"; II.B.2 "In a bad sense, to plot together, to enter into a conspiracy, to conspire" (Caes. B. G. 3, 10). | FITS: "to secretly plot or make plans together" (Wikt) | — |
| `sabotage` | S8 | PLANNED, KEEP | lower a Site's condition | sabotage ← F *sabotage* ← F *saboter* ← F *sabot* 'clog' ← MF *savate* 'old shoe', of unknown origin (perhaps Turkic or Iranian) (Wikt fr). **No Latin path.** Wikt fr repeats the clog-throwing story; VCD:1866 marks it folk etymology [UNVERIFIED either way] | FITS: "to deliberately destroy or damage something in order to prevent it from being successful" (Wikt) | — |
| `succeed` | S9 | REBUILD (IN-61) | the heir claims the vacant throne; opens his `hold` on it under the `inheritance` basis | succeed ← OF *succeder* ← L *succēdō, -ere, -cessī, -cessum* (Wikt; L&S): L&S "to go below or under … to approach … to follow after, take the place of", with *qui regno successit* (Plin.), *in hujus locum filia regno successit* (Just.) ← *sub* + *cēdō* 'go, proceed' (Wikt-la *cēdō*: "further derivation disputed"); Wikt (*cede*) gives PIE \*ḱyesdʰ-: **disputed** | FITS for the heir's act: "to replace or supplant someone … vis-à-vis an office" (Wikt). STRAINED for the shipped row, where the holder designates (VCD:357) | — |

**Folded acts and named contents**

| verb | suite | status | mechanic and world effect | etymology chain (sources) | fit | rename |
|---|---|---|---|---|---|---|
| treaty | S1 | FOLDED (content) | generic terms of `covenant` | treaty ← ME *trete, tretee* ← AN *treté* / OF *traitié*, pp. of *traiter* ← L *tractō, -āre* 'to drag, haul; to handle, manage; to debate, discuss' (Wikt; frequentative of *trahō* 'draw') ← PIE uncertain (as `train`): \*dʰregʰ- is tentative; De Vaan proposes a non-IE \*trHgʰ-/\*trā̆gʰ- (Wikt la *trahō*) | FITS | — |
| peace | S1 | FOLDED (content) | terms naming a war; `at_war` reads False while in force | peace ← ME *pees* ← AN *peis*, OF *pais* ← L *pāx* ← PIE \*peh₂ḱ- 'fasten' (Wikt; related to *pacīscor*, *pangō*, and so to *pact*) | FITS | — |
| alliance (ally) | S1 | FOLDED (content) | terms read by `mustered` | ally ← ME *allien* ← AN/OF *alier* ← L *alligō / adligō, -āre* 'bind to' ← *ad-* + *ligō* ← PIE \*leyǵ- 'bind' (Wikt). The root is shared with `oblige` and `league` (V-19 class; no clash in use) | FITS | — |
| truce | S1 | FOLDED (content) | terms with a declared end; breach priced higher | truce ← ME *trewes*, pl. of *trewe* ← OE *trēowa*, *trēow* 'faith, pledge' ← PGmc \*trewwō (Wikt). **Germanic, no Latin path**; F *trêve* is a loan from Germanic (Wikt) | FITS | — |
| tribute | S1 | FOLDED (content) | terms naming a recurring due; renewal reader | tribute ← ME *tribut* (14th c.) ← MF *tribut* ← L *tribūtum*, pp. of *tribuō* 'assign, grant', usually from *tribus* (Wikt) ← PIE \*tréyes 'three' + either \*dʰeh₁- 'to put' (\*tri-dʰh₁-o- 'tripartite') or \*bʰuH- 'to become' (Wikt la *tribus*: either) | FITS: "a payment made by one nation to another in submission" (Wikt) | — (content not named `due`: V-19) |
| cession (cede) | S1 terms / `give` | FOLDED: terms into `covenant`; the handover into `give` (GV/SC) | the holder's `give` of a Rung | cede ← MF *ceder* ← OF *ceder* ← L *cēdō* ← PIE \*ḱyesdʰ- (Wikt; disputed per Wikt-la) | FITS | — |
| vassalage (vassal) | S1 | FOLDED (content) | terms; performed by the vassal's pledge | vassal ← ME/OF *vassal* ← ML *vassallus* ← *vassus* ← Gaulish \*wassos ← Proto-Celtic \*wastos (Wikt). **Celtic, not Latin at root** | FITS | — |
| league | S1 | FOLDED (parameter: n parties) | many parties seal one instrument | league ← ME *liege, ligg, lige* ← MF *ligue* ← It. *lega* ← *legare* ← L *ligō* 'bind' ← PIE \*leyǵ- (Wikt) | FITS | — |
| ransom | S1 | FOLDED (content) | terms: captive against amount; the payer's `transfer` and the captor's discharge perform it | ransom ← ME *raunsoun* ← OF *raençon* ← L *redēmptiō* (Wikt), from *redimō, -ere, -ēmī, -ēmptum* "to buy back, repurchase" (L&S) ← *red-* + *emō* ← PIE \*h₁em- 'to take, distribute' (Wikt la *emō*) | FITS: "money paid for the freeing of a hostage" (Wikt) | — |
| hostage (surety) | S1 | PARKED | terms naming a surety in `detain` | hostage ← ME *hostage, ostage* ← OF *hostage*: either *hoste* 'lodging' + *-age*, or VL \*obsidāticum ← L *obses* 'hostage' (Wikt; both given) | FITS | — |
| marriage alliance | S1 | PARKED (NP kin tie) | terms naming a marriage | marry ← ME *marien* ← AN *marïer* ← L *marītō, marītāre, marītāvī, marītātum* 'to give a husband to; to wed, marry' (L&S; post-Augustan, rare) ← *marītus* ← *mās*, possibly PIE \*méryos (Wikt: uncertain) (V-19 list) | FITS | — |
| war | S2 | FOLDED (content, built first) | mood `WAR` | war ← ME *werre* ← late OE *werre* ← AN/ONF *werre* ← ML *werra* ← Frankish \*werʀu 'confusion' ← PIE \*wers- (Wikt). **Germanic**, not Latin | FITS ("declare war") | — |
| embargo | S2 | PARKED (content) | trade-ban declaration; EC reader | embargo ← Sp. *embargar* ← LL \*imbarricāre ← L *in-* + VL \*barra (Wikt) | FITS: "a ban on trade with another country" (Wikt) | — |
| sanction | S2 | PARKED (synonym of embargo's coercive sense) | as embargo | sanction ← MF *sanction* ← L *sānctiō* (Wikt) ← *sanciō* + *-tiō* ← Proto-Italic \*sankiō ← PIE \*seh₂k- 'to sanctify, make a treaty' (Wikt la) | STRAINED: its first sense is approval (Wikt: "an approval, by an authority"), so it is contranymic | use `embargo` for the content |
| condemnation | S2 | PARKED (content) | a HOLDS Proposition naming a creed | condemn ← ME *condempnen* ← OF *condamner* ← L *condemnāre* ← *com-* + *damnāre* ← *damnum* (Wikt) | FITS: "to strongly criticise or denounce" (Wikt) | — |
| `proclaim` | S2 → GV | CULLED in FA (the act is GV's edict) | — | proclaim ← ME *proclamen* ← OF *proclamer* ← L *prōclāmō, -āre, -āvī, -ātum* "to call or cry out, to vociferate" (L&S) ← *prō-* + *clāmō* (Wikt), PIE \*kelh₁- (*clāmō* ← Proto-Italic \*klām- ← \*kl̥h₁m- ← \*kelh₁-; Wikt la) | FITS for an edict (GV) | — |
| hire | S3 | FOLDED (parameter: wages) | `recruit` with upkeep | hire ← ME *hire, huren* ← OE *hȳr* ← PWGmc \*hūʀiju ← PGmc \*hūzijaną ← PIE \*kewHs- (or another; Wikt). **Germanic, no Latin** | FITS (V-06: the employer's act) | — |
| enlist / retain | S3 | FOLDED (names) | — | enlist ← *en-* + *list* (Wikt); retain ← ME *reteinen* ← AN *reteiner* / *retenir*, OF *retenir* ← VL \*retinō ← L *retineō* (*re-* + *teneō*) ← PIE \*ten- (Wikt en *retain*) | FITS | — |
| turn (a man) | S3 | PARKED (content; `conceal`) | concealed `recruit` of a rival's obligee | turn ← ME *turnen* ← OE *turnian/tyrnan* (← PWGmc \*turnēn) and OF *torner*, both ← L *tornāre* 'turn on a lathe' ← *tornus* 'lathe' ← Gk τόρνος ← PIE \*terh₁- (Wikt en) | FITS ("turn an agent") | replaces `suborn` |
| `suborn` | S3 | CULLED (name) | — | suborn ← AN *suburner* / MF *suborner* ← L *subōrnō, -āre*: L&S I "to fit out, furnish, provide, equip"; II "with the idea of the preposition predom., to incite secretly, to instigate, suborn" (*falsum testem*, Cic. Rosc. Com. 17, 51) ← *sub-* + *ōrnō* ← PIE \*h₂er- (Wikt) | MISFIT for "turning an enemy's man": Wikt "to induce (someone) to commit an unlawful or malicious act, esp. perjury" (V-05) | `turn` (content of `recruit`); the unlawful-inducement sense is FI's `bribe` or a THREAT |
| conscript / draft | S4 | FOLDED (names) | — | conscript ← L *cōnscrīptus*, pp. of *cōnscrībō* 'enrol' (Wikt); L&S *conscrībo*: "to write together in a roll or list, to enrol", especially of the levying of troops (Caes. B. G. 1, 10); draft = a phonetic spelling of *draught* ← ME *draught* ← OE \*dreaht/\*dræht ← PWGmc \*drahti ← PGmc \*drahtuz ← PIE \*dʰregʰ- (Wikt en *draft*) | FITS | — |
| assign / post | S5 | FOLDED (parameter: no relocation) | posting payload only | assign ← ME *assignen* ← OF *assigner* ← L *assignō, -āre* ← *ad-* + *signō* (Wikt). Wikt-la: "to appoint to, assign, distribute, allot, allocate". PIE: \*sek- or \*sekʷ- (Wikt tags both: disputed) | FITS: "to appoint or select (someone) for some office" (Wikt) | — |
| envoy (send) | S5 | FOLDED (content) / latitude PARKED | the posted man carries an instrument | envoy ← F *envoyé*, pp. of *envoyer* 'send' (Wikt) ← OF *enveier* ← LL *inviō, inviāre* ← *via* (Wikt fr *envoyer*) | FITS | — |
| garrison (post a man) | S5 | FOLDED (content) | posting to a `garrison` Site | garrison ← ME *garisoun* ← OF *garison* ← *guarir* 'protect', of Germanic origin; PIE \*wer- per Wikt's root tag (Wikt). **Germanic via French**; the modern sense was influenced by *garnison* | FITS | — |
| conquer / take | S6 | FOLDED (names) | the Rung half of `seize` | conquer ← ME *conqueren* ← OF *conquerre* ← LL *conquaerō* ← *con-* + *quaerō* 'seek' (Wikt) | FITS | — |
| annex | S6 → GV | PARKED | fill an `annex` seat (unruled) | annex ← ME *annexen* ← OF *annexer* ← ML *annexāre*, frequentative of L *annectō* ← *ad* + *nectō* 'bind' (Wikt) | FITS: "to add something … especially territory; to incorporate" (Wikt) | — |
| claim | S6 | CULLED (name) | — | claim ← ME *claimen* ← OF *clamer* ← L *clāmō* ← PIE \*kelh₁- (imitative) (Wikt en) | collides with the `Claim` carrier (VCD:2125-2127) | — |
| plot / scheme | S7 | FOLDED (names) | — | plot 'secret plan' ← ME *plot* ← late OE *plot* 'patch of ground', of uncertain origin (Wikt); **Germanic or unknown**, reinforced in this sense by F *complot* (Wikt) | FITS | — |
| coup | S7 | FOLDED (content: target is the head seat) | — | coup ← F *coup* ← OF *coup* ← LL *colpus* ← L *colaphus* 'a blow' (Wikt), a Greek loan | FITS | — |
| designate | S9 | CULLED (RS-27) | the heir title is `confer`red | designate ← L *dēsignātus*, pp. of *dēsignō* "to mark out, trace out; to describe, designate, define" (L&S); root templates \*sek- and \*sekʷ- (Wikt la *signum*: either) | — | — |
| negotiate | (SC) | not FA | a series of `covenant` offers; the contested form is SC's | negotiate ← L *negōtiātus*, pp. of *negōtior* (deponent) ← *negōtium* ← *nec* + *ōtium* (Wikt), c. 1598 | FITS | — |
| mediate | (SC) | PARKED (not FA) | non-binding third party | mediate ← LL *mediātus*, pp. of *mediō* 'to be in the middle' ← *medius* (Wikt), verb 1538 | FITS for the parked act, MISFIT for v2's binding V132 (V-04) | — |
| arbitrate | (GV/SC) | not FA | `convene` under `arbitration` + `determine` | arbitrate ← L *arbitrātus*, pp. of *arbitror* (deponent) ← *arbiter* (Wikt) | FITS | — |

Row counts: 9 hosts (4 NEW, 1 NEW-as-designed, 2 REBUILD, 1 SHIPPED, 1 PLANNED); 33 folded, parked, culled or not-FA names.

---

## 3.5 Deduplication and culls

**Near-synonym groups and what was done**

| group | resolution | discriminator (reads/writes/emits, and ordinary sense) |
|---|---|---|
| `declare` · `proclaim` · `utter` · `issue` | four acts; `proclaim` leaves FA | `declare`: a seat, about another faction, `binding_decision` (public). `proclaim`: a seat, about a Rung in its own purview (VCD:2164), an edict (GV). `utter`: any person, `social` (co-located). `issue`: a Record to a named executor, answered by `comply` (VT:441-490) |
| `covenant` · `commit` · `oblige` · ally · league | three rows plus two contents | `covenant`: seat to seat, an instrument held by both. `commit`: a person to a Proposition. `oblige`: a person to a seat. Ally and league are covenant contents. Same root \*leyǵ- across `oblige`, ally and league, and *convenīre* across `covenant`/`convene` (V-19): no reader confuses them, because each is the plain word for its act |
| `recruit` · hire · enlist · retain · `oblige` · `confer` · `levy` | one host, three folded names | `recruit` writes the recruit's `oblige` on a won contest; hire differs by a wage parameter; enlist and retain are names. `oblige` is the joiner's own act (another actor). `confer` seats an office holder (GV). `levy` moves `Rung.stores` (troops) |
| `dispatch` · assign · post · send · order · `issue` | one host, two folded names | `dispatch` posts and, where needed, moves an obligee. Assign/post is the same act without the move. `order` was withdrawn as a name because `order:` is an arrangement key (VCD:482, K-24). `issue` is a document |
| `seize` · conquer · take · annex · `cede`/`give` | one host; annex PARK (GV); cede → `give` | `seize`: non-consensual, under warrant or occupation (`rung.seized`). `give`: consensual (`record.given`). Annex: a seat-filling basis with no act (RO:2001-2019) |
| `conspire` · plot · scheme · coup · concealed `covenant` | one host | v2's own finding (p8:359): `covenant` is seat-only, private and uncontested |
| `suborn` · `bribe` · turn | `suborn` culled; turn is a content of `recruit`; `bribe` stays FI's | V-05: suborn names the aim (an unlawful act), bribe the means (a payment) |
| `succeed` · designate · claim · inherit | one host; designate culled | RS-27: designation is `confer` of a title; the heir's act is the claim |
| negotiate · bargain · `covenant` | negotiate is not an FA row | a negotiation is several `covenant` offers. The contested bargain needs an unseeded `negotiation` arrangement (SC) |
| mediate · arbitrate | V-04 applied | arbitration is binding (`effects_information.py:380-384`, cited in V-04); mediation is not |
| embargo · sanction | `embargo` kept as the content name | "sanction" first means approval (Wikt) |
| tribute · due · debt | the content is named `tribute` | V-19: *dēbeō* gives both "due" and "debt" |

**Culls**

| culled | fold test result | floor check |
|---|---|---|
| `proclaim` (as an FA name) | not a fold: its subject class (Rung) and purview differ from `declare`'s (a faction). It moves to GV, not to death | nothing a floor act needs dies, because "declare war" lives in `declare` |
| `suborn` (name) | the act "turn an enemy's man" folds into `recruit` (same actor, same contest, content: concealed). The legal sense (procure perjury) is FI/SC's | recruit stands |
| `designate` | not an act: RS-27; it is `confer` of the heir title (IN-61) | succession lives in `succeed` |
| `claim` (name) | — | taking territory lives in `seize`; no casus-belli reader exists (VCD:1749) |
| `sanction` (name) | a synonym of the embargo content | embargo parked, not lost |
| v2 V072 recruit → `tell` + reply | fails rule 5 (another actor's reply) | replaced by `recruit` |
| v2 V091 declare → preset of `utter` | fails the mechanic test (actor class `own` vs seat; stratum `social` vs public) | replaced by `declare` |
| v2 V150 conspire → `utter` + commits + `conceal` | fails rule 5 (three verbs, others' replies) | replaced by `conspire` |
| v2 V152 ransom → `pardon` + `transfer` | fails rule 5 (two parties' acts composed). `pardon` names mercy (V-16) | replaced by the `covenant` ransom content |
| v2 V153 negotiate → `covenant` "hosted by SC's `negotiation`" | rests on an arrangement row that does not exist (`arrangements.yaml` ids, §3.3 S1) | the offer is `covenant`; the contest is SC's |
| v2 V151 suborn → `bribe` row | V-05: different act | turn (content of `recruit`), PARK |
| v2 first pass `succeed` CUT (p4:148) | reversed: RS-27 makes the claim an act | `succeed` per IN-61 |

Falsifier for each cull, in one clause:
- `proclaim`: an FA-scale proclamation whose subject is a faction rather than a Rung would show it as a duplicate of `declare`, not a GV act.
- `suborn`: a usage corpus in which "suborn" ordinarily means "recruit a double agent" would revive the name.
- `designate`: a Jordan ruling reversing RS-27.
- `claim`: a reader of a justified war (a casus belli) would need a word, and "claim" would then need a non-colliding replacement.

**Critics' findings on FA verbs**

| finding | disposition | reason |
|---|---|---|
| L-01 (root sense used as design) | **applied** | no merge, gap or node here rests on a root; every fit verdict cites a current-usage sense |
| L-02 (`oblige` runs the other way) | **applied** | no FA act folds into `oblige`. `recruit` writes the edge from the recruiter's side; the joiner's act keeps its own row. The rename to `pledge` is flagged to GV/NP (§3.8) |
| L-03 (`levy` reused) | **answered** | the troop sense is the ordinary one (Wikt). TS1:730-734's re-keying of old `levy.*` counts must land first |
| L-05 (`dispatch` documentless) | **answered** | the verb sense "send (a person)" fits a rebuilt row that sends. The defect was the empty write. Renaming is §3.9 item 2 |
| L-07 (`found`/`establish`) | **flagged** | GV's; FA adds only that a faction-founding sense of `found` would be a second meaning (S9) |
| L-08 (`release` as vow-break) | **flagged** | FA's breach and unilateral peace use GV's closer. L-08's `renounce` fits "renounce a treaty", which supports it |
| L-10 (`give`/`transfer`) | **consistent** | cession by `give` (a hold), tribute by `transfer` (stores) |
| L-12 (`seize` never judged) | **applied** | judged here: FITS (S6, §3.4) |
| L-18 (`remit:issue` gates many acts) | **noted** | `covenant` takes `remit:issue` (VCD's row) and `declare`/`levy` take `remit:dispatch`. The remit names read as "civil authority" and "military command"; a rename is GV/IN's |
| V-04 (mediate ≠ arbitrate) | **applied** | S1 "not folded" |
| V-05 (bribe ≠ suborn) | **applied** | `suborn` culled; turn into `recruit` |
| V-06 (hire/recruit asymmetry) | **applied** | hire folds into `recruit` (the employer's act) |
| V-09 (betray ≠ release) | **applied** | betrayal is a witness judgement; a covenant breach is an open renunciation |
| V-15 (`tax` rests on retired `evade / defy`) | **answered, flagged** | `tax` is GV's. FA's rebuilt `dispatch` also leans on `evade / defy` as the obligee's answer, so its retirement must be reversed before either lands (§3.8) |
| V-16 (ransom ≠ pardon) | **applied** | the captor's act is the discharge of a `detain` (GV's closer), not mercy |
| V-19 (`due`/`debt`; `convene`/`covenant`) | **applied / answered** | the tribute content is named `tribute`. `covenant`/`convene` are kept: different subsystems, different objects, both plain words |

---

## 3.6 Gap coverage table

One disposition per row. "closed by X once M-n" names a §3.7 mechanic.

| gap | disposition |
|---|---|
| FA-G01 | **closed by `declare`** (S2) once M1 (a reader of `at_war`) |
| FA-G02 | **closed by `declare`**: the verb supplies mood `WAR`, so a computed declaration never mints `OUGHT` |
| FA-G03 | **closed by `declare`**: its effect writes the declarer's own edge, so no separate computed `commit` is needed |
| FA-G04 | **closed by `covenant`** (NEW ROW, S1) |
| FA-G05 | **closed by `covenant`** (truce content) once M2 (in-force Query, breach detector, truce ranking) |
| FA-G06 | **closed by `covenant`** once M2 (breach priced by a `deed:` cell on the breaker's close) |
| FA-G07 | **closed by `covenant`** (alliance content) once M3 (`mustered` counts an in-force ally's members and a seat's obligees) |
| FA-G08 | **closed by `covenant`** (tribute content) once M2's dues reader and the goods keys (p8:111-132) |
| FA-G09 | **closed by `covenant`** (cession terms) once `give` + Rung exists (planned B-R; GV/SC row) |
| FA-G10 | **closed by `covenant`**: a negotiation is a series of offers. The contested form is SC's, on a `negotiation` arrangement not yet seeded |
| FA-G11 | **PARKED**; trigger: M5 (the posting reader) and a terms range on a covenant instrument (an envoy's latitude) |
| FA-G12 | **closed by `dispatch`** (REBUILD): the verb sense fits once the row sends (§3.4). The rename question is §3.9 item 2 |
| FA-G13 | **closed by `dispatch`** once M5 |
| FA-G14 | **closed by `dispatch`** (REBUILD): a posting on a service edge, against `issue`'s document. J-8 answered by precedent: `dispatch` is on the closed remit roster (RO:311) and gates `march` (VT:687) |
| FA-G15 | **closed by `succeed`** once IN-61 lands: the heir is the actor, so the name fits |
| FA-G16 | **closed by `succeed`** once IN-61 lands (its exit: the heir receives a question naming the vacant throne) |
| FA-G17 | **OUT OF SCOPE**: GV (fratricide law and partition as GV acts, the consulta as `convene`), EC (donative as `transfer`), MB (recall as disband). The oath is GV/NP's pledge. Named in §3.8 |
| FA-G18 | **OUT OF SCOPE**: GV (`confer` delegate hold, IN-48; p8:481) |
| FA-G19 | **OUT OF SCOPE**: GV (abdicate on GV's closer, p8:484; depose PARK, p8:485) |
| FA-G20 | **OUT OF SCOPE**: GV (revocation cost, H-100) |
| FA-G21 | **OUT OF SCOPE**: GV (H-91) |
| FA-G22 | **closed by `levy`** (S4; the seat's half) once M4 (troop stock). The force is MB's |
| FA-G23 | **OUT OF SCOPE**: GV (`requisition`, `comply`, `evade / defy`) |
| FA-G24 | **OUT OF SCOPE**: GV; FA depends on it (§3.8: `dispatch`'s answer) |
| FA-G25 | **OUT OF SCOPE**: GV (fiscal stance, tax farming) |
| FA-G26 | **closed by `conspire`** (NEW ROW, S7) once `conceal` (FI) and M7 |
| FA-G27 | **PARKED** as `turn`, a content of `recruit`; trigger: `conceal` and a recipient-side reader (p8:271-276). `bribe` is FI's row |
| FA-G28 | **closed by `covenant`** (ransom content) once the goods keys, GV's `detain` discharge and a capture producer exist |
| FA-G29 | **OUT OF SCOPE**: GV (arrest and pardon are law acts; v2 left them untried, p8:706-710) |
| FA-G30 | **PARKED**; trigger: a voluntary opener of `detain` (a party handing over a hostage) and the covenant surety reader |
| FA-G31 | **closed by `declare`** for declarations against a faction. The edict to one's own purview is GV's (§3.8) |
| FA-G32 | **closed by `declare`** (`binding_decision`) once M6 (a public channel that survives SC-01 step 13; D-V3) |
| FA-G33 | **PARKED** as `declare`'s embargo content; trigger: EC's ban-term reader |
| FA-G34 | **OUT OF SCOPE**: GV/SC (vote = `commit` counted by quorum, p8:435). Ratification of a treaty is the second party's `covenant` (S1); a subsidy is EC's `transfer` |
| FA-G35 | **closed by `sabotage`** (S8). Spy is FI's `surveil` |
| FA-G36 | **closed by `recruit`** once M8 (a recruited seat-holder's own obligees follow him: the bloc) |
| FA-G37 | **OUT OF SCOPE**: GV (the cells of `release`). FA consumes them for the covenant breach |
| FA-G38 | **closed by `seize`** once M9 (a Church appetite Query that ranks `seize` of land) |
| FA-G39 | **PARKED**; trigger: a runtime faction carrier (H-186 / IN-30). Today `factions` is read from `names_index.yaml` |
| FA-G40 | **OUT OF SCOPE**: GV (`found`, `establish`; a standing-corps Organization) |
| FA-G41 | **OUT OF SCOPE**: GV (partition, redistrict, intendant, capital). Annex is flagged in §3.8 |
| FA-G42 | **OUT OF SCOPE**: MB (show of force as a `march` posture, MB-G50) and EC (trade mandate) |
| FA-G43 | **PARKED**; trigger: NP's kin tie (K-NPC-6 / D-V2). Then a covenant marriage content |
| FA-G44 | **OUT OF SCOPE**: FI and the decision layer (a reader of `faction_sheet`) |
| FA-G45 | **OUT OF SCOPE**: GV (`determine` disposing `ban`; its closer) |
| FA-G46 | **OUT OF SCOPE**: quarantined prose hooks with no carrier; FAL:408 drops them. No verb implied |
| FA-G47 | **closed by `recruit`** (NEW ROW, S3) |
| FA-G48 | **STALE** as filed: the reader exists. `state/gate.py:359-360`, `purview_reaches`: "since v9 IN-40, when a seat sworn to this one brings it (the oblige clause)". The terms are now a `covenant` content (S1) |
| FA-G49 | **OUT OF SCOPE**: GV (`establish`; dissolve) |
| FA-G50 | **closed by `covenant`** once M2's in-force Query (GD-1's "treaties counting"). GD-2's mandatory muster pass is MB's |

Count (by hand, recounted): closed 25 · PARKED 6 · OUT OF SCOPE 18 · STALE 1 · DISPUTED 0 = 50.

---

## 3.7 Mechanics this subsystem needs (named gaps)

| id | mechanic | what it must write or read | verbs waiting |
|---|---|---|---|
| M1 | a reader of `at_war` | at minimum `march`'s ranking or target selection (p8:343). `at_war` counts only WAR Propositions a `declare` minted | `declare` (war) |
| M2 | covenant readers | an in-force Query (both parties' edges live). A breach detector: an act against the terms earns a breach kind on the breaker's close, priced by one `deed:` cell. A truce rank term. A dues renewal over covenant terms (`_renewals`' shape) on the goods keys `kind`/`amount` (RO:1708-1723). A peace override in `at_war`. A ruling on successor binding (§3.9) | `covenant` and all eleven contents |
| M3 | widened muster | `world_q.mustered` also counts (a) the exercised seat's obligees and (b) an in-force ally's members. Today it is members ∩ present (`world_q.py:1257-1275`) | `recruit`, the covenant alliance content; MB's field |
| M4 | troop stock | the `recruits` matter kind, `recruit_ceiling`, its regrowth with a `stores:recruits` claim producer, the troop body (J-1) (TS1 §2.1-2.4). None exists (`grep -c recruits rosters.yaml` = 0) | `levy` |
| M5 | posting reader | the posted obligee's question source carries his task (`Tenure.payload` on his `oblige`). His refusal is a resolvable `evade / defy`, split covert/open per VCD:334 | `dispatch` (assign, envoy, garrison) |
| M6 | a public channel past SC-01 step 13 | a declaring seat's act reaches every faction head in the season it happens (D-V3, p8:632) | `declare` |
| M7 | plot reader | a plot's members' choosers rank its act. A refused invitation leaves the invitee a claim against the plotter. Needs FI's `conceal` (IN-12 step 10) | `conspire`; turn (`recruit`) |
| M8 | bloc follows | when a seat-holder enters a rival's service, his own obligees' goals follow (FAL K-FA-10, via register FA-G36) | `recruit` (of a seat-holder) |
| M9 | Church appetite Query | land appetite rising with holdings ends in a seizure attempt (FAL K-FA-8, H-25, via register) | `seize` |
| M10 | social contest on an act's counterparty | `recruit`'s and `conspire`'s obstacle read from the counterparty's ties, regard and opinion (IN-70) through SC's contest resolver (`contest_subsystems`, RO:1127) | `recruit`, `conspire` |

---

## 3.8 Cross-subsystem flags

**GV** (FA hands these over; each was an unowned FA gap, decided here):
- **Moves to GV:**
  - **`proclaim`** (an edict to one's own purview, VCD:2161).
  - **Annex** (which act fills an `annex` seat, RO conferral_bases note).
  - **The faction-founding sense of `found`** (FA-G39 PARK; the trigger is runtime factions, so whoever builds that owns it).
  - **Succession-crisis acts** (FA-G17).
  - **Regency** (G18), **abdicate/depose** (G19), **revocation** (G20, G21), **extraction** (G23, G25), **law acts** (G29, G45), **`release`'s cells** (G37), **structure** (G40, G41, G49).
- **Kept in FA with a GV dependency:**
  - **`succeed`** (IN-61: lane "IN (FA SE)"; the head-seat claim is FA's, the `inheritance` basis is GV's gate).
  - **`seize`** (warrant seizure is GV's use of the same row).
- **GV's rows that FA consumes:**
  - `release` (breach, unilateral peace; L-08's `renounce` would fit both).
  - The `detain` discharge (ransom).
  - `evade / defy` reversed from its retirement into `comply` (V-15; `dispatch`'s answer needs it as much as `tax` does).
  - `oblige` renamed `pledge` (L-02). `recruit` writes the same edge from the other side, and vassalage is performed by it.
- **Collision:** `issue` and the rebuilt `dispatch` must stay apart by write row (document vs posting).

**SC:**
- A contested bargain needs a seeded `negotiation` arrangement (it is a candidate only, `arrangements.yaml:24`).
- `recruit` and `conspire` roll through SC's contest resolver (M10).
- `mediate` is parked as a non-binding arrangement; v2's "mediate" (V132) is arbitration (V-04).
- `give` + Rung (cession) is shared with GV.
- D-V3's channel is shared with `deny`.

**MB:**
- `levy` writes the troop stock MB fields (TS1).
- M3 widens MB's `mustered`.
- MB's own rows: show of force, garrison stock, recall/disband, `surrender` (MB's preset of `give`, which may carry `covenant` terms), GD-2's muster pass, and which act `at_war` gates (MB-G15).
- MB-G48 and V118 name `dispatch` as a carrier of field orders. After the rebuild `dispatch` posts persons; battle orders should ride `march`'s order of battle, not `dispatch`.

**EC:**
- Hire folds into `recruit` (EC lists `hire`, p8:269).
- `tribute` and `ransom` need the goods keys (§V.2.2).
- The embargo content waits on EC's ban-term reader (smuggle).
- Subsidy and donative are `transfer`.

**FI:**
- `conceal` gates `conspire` and turn.
- `bribe` stays FI's row.
- Spy is `surveil`.
- A reader of `faction_sheet` (FA-G44).

**NP:**
- The kin tie for the marriage content (FA-G43).
- Defection as a person's own acts, if NP keeps them.
- `oblige`/pledge, if NP rather than GV owns it.

---

## 3.9 For Jordan

Each item survived the five-step ladder (superseded, irrelevant, design document, precedent, architecture); each step tried is named.

1. **Does a treaty bind the signer or the seat?**
   - Edges are persons' (`commit`/`oblige` Tenures). So with no further rule a treaty lapses when either head dies, and every accession reopens diplomacy. That is the historically common game.
   - The alternative is an edge on the seat, which survives the holder. That is the stable-diplomacy game of EU4/Total War `[MEMORY]` and needs a new carrier.
   - Tried: no ruling or head covers it; VCD's row is silent; tree precedent (membership and war edges are personal) argues for lapse, and the architecture can do either. Two defensible games.
2. **`dispatch` as the host name, or `assign`?**
   - ED-IN-0210 kept `dispatch` (VCD:4055; rename withdrawn under K-24). The rebuild makes it fit ("send a person"), but the user's own phrase is "set assignments", and `assign` would name the standing-post case better.
   - Renaming overwrites a ruling and the remit act name `remit:dispatch` (RO:311; `march` VT:687; FA-01's pin). Recommendation: keep `dispatch` (it FITS once it sends), with assign as the folded content. Escalated only because the alternative overwrites a ruling.
3. **Who may declare war?**
   - Option one: any holder of a seat with `remit:dispatch` (this file's row; under `remit_default` that is every seated person).
   - Option two: the faction's head seat only. That needs a `requires` conjunct reading `faction_q.head`, which is None today (`faction_q.py:116-147`).
   - The two make materially different wars: marshals starting wars, against only rulers.
   - Tried: v2's seat clause (p8:337-338: "a person holding a seat of one of the two factions"), `march`'s remit precedent, and canon (none found).
4. **May a won contest open an edge the counterparty owns?**
   - `recruit` and `conspire` take the counterparty's consent as the contest's degree. A won `recruit` opens the recruit's `oblige`; a won `conspire` opens the invitee's edge to the plot.
   - Precedent exists: `confer` opens the conferee's `hold`, and `determine` opens an `oblige` owned by the party it binds (VT:861).
   - Against it: `dispatch`'s note "their own choose decides" (VT:281) states the autonomy reading for orders.
   - The user's rule 5 forbids the reply-act alternative for a floor verb, so the recommendation is to allow it. It is escalated because it may overwrite an autonomy axiom this file did not trace to its source [UNVERIFIED: whether a ratified axiom forbids it].

---

*Not done:* no test or tool run (none covers a scratchpad file). The `ls conspiro` fetch failed three times. Not opened, so not verified beyond the register's citation: PW, PMM, RTP, HCC, PGS, COMP1/2 and RHET lines (all "via register"); the ED ledgers.



