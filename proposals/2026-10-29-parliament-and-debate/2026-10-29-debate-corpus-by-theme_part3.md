# Debate, persuasion and social-contest corpus — sorted by theme (part 3: themes G, H, I, K)

## Status: **REFERENCE (2026-10-29).** Continues `2026-10-29-debate-corpus-by-theme.md`, whose status, scope note, counts, lane coverage and reading key apply here.

---

## G · Outcome, binding and enforcement — 59 entries (CODED 4, RATIFIED 4, INTENT 14, PROPOSED 7, ARCHIVED 13, NOTCODED 1, RESEARCH 3, HISTORICAL 12, GAME 1)


### G / CODED

- **CD-038** `CODED` — issue: a seat with remit 'issue' mints a dispensation (a writ) Record addressed to executors; comply: a person whose ledger holds a claim of the writ's terms records compliance. \[verb rows issue (:596) and comply (:221); effect effects_information.py:221\] `engine/season/verb_table.yaml:596` · hook: verb issue; verb comply; Record dispensation · conf H
  - Promulgation is minting a document; compliance is a claim-gated Event with writes []. Non-compliance (evade/defy) and construal (construe, 'absent', D18) are weak: construe is graded 'absent'.

- **GV-049** `CODED` (+H) — Revocation basis: a seat may be stripped only by the holder of a seat on the rung directly above, in the same faction; a second value requires the seat's rung to be in the revoker's holdings. \[code: roster plus REVOCATION_RULES in state/gate.py, refused at import if they disagree; ED-IN-0256 ruling (3)\] `engine/season/rosters.yaml:2324` · hook: may_revoke; REVOCATION_RULES · conf H
  - Verbatim ruling 'rung above of same faction' replaced purview-based rules. rung_above_in_holdings (Jordan 2026-10-12) lets Hafenmark and Varfell duchy heads be stripped by the monarch only if the duchy is in the monarch's holdings; as built no duchy is, so nobody can. Seat with no declared basis is revocable by nobody.

- **GV-050** `CODED` (+J,I) — Revoking an appointed seat opens a permanent ban on the ex-holder; revoking an elected or annex seat costs nothing; a confer that displaces an incumbent costs nothing. \[code: REVOCATION_DISPOSAL dict, Jordan 2026-10-21 (B-Q answering IN-31 design)\] `engine/season/state/gate.py:590` · hook: revoke -> ban tenure; revocation_disposal · conf H
  - Mapping is total over conferral bases plus None, checked at import. The ban carries no term and no effect closes it except the man's death (pardon is a separate verb). Encodes that dismissal of an appointee is punitive while an electorate's removal is not.

- **PR-098** `CODED` (+B) — release is CODED (eligibility own, writes Tenure.until, domain hold/commit/oblige/succeed/tie/knot) and ABSORBS repudiate: repudiate's row was deleted as a second closer of one edge, so a vow-break is witnessed as commitment.ended through release. \[code at verb_table.yaml:1051 (v9 IN-11); repudiate CUT\] `engine/season/verb_table.yaml:1051` · hook: release; commitment.ended; deed_valence · conf H
  - Contradicts the proceedings docs that still say repudiate closes a commit and the treaty/party mechanics ('repudiate T-m'). requires_typed none because the grammar lacks an any combinator. Vow-break priced at release's alignment cells via KIND_VERB; no deed:commitment.ended cell authored.


### G / RATIFIED

- **CD-063** `RATIFIED` (+D,I) — Planned: the throne may be stripped by joint_concurrence: a Parliamentary determine (monarch as party) minting a resolution, plus the Holy See's own revoke while holding it. \[plan position CR-37, B10-17; unbuilt; closes 'depose'\] `workplans/valoria_master_workplan_v10_part4.md:391` · hook: revoke; joint_concurrence; resolution · conf H
  - A third revocation_bases value and a closed concurring_bodies roster [Holy See]. No ban opens; the deposed King keeps his duchy seat. Motive supplied by CP-T09-09 'legitimacy'. No computed route until an operand channel names arrangement and petition (H-80).

- **GV-030** `RATIFIED` (+B,M) — Governance-type cascade: each tier's authority sets governance type of the tier below, a noisy bidirectional throughline modulated by settlement consent (Legitimacy / Popular Support). \[RATIFIED Jordan 2026-07-13 (archived doc)\] `.designs/systems/settlements/reference/scale_hierarchy_v1.md:49` · hook: L/PS as consent modulator on cascade · conf H
  - Duke sets provincial type; province sets territorial; territory sets settlement. Consent gate: ruling faction can impose, but keeping effective power depends on what settlements accept (L/PS). Doc notes L/PS was inert in sim at the time (E5) and wiring it is a precondition for the hierarchy mattering.

- **GV-033** `RATIFIED` (+B,F) — Worked appointment chain: King appoints provincial governors from his royal court; governors oversee, coordinate and vet appointed settlement councils; independent provincial factions sit outside that chain. \[RATIFIED Jordan 2026-07-13 (archived doc)\] `.designs/systems/settlements/reference/scale_hierarchy_v1.md:146` · hook: appointed governor / settlement council · conf H
  - 'Vet' means the higher authority reviews settlement-level decisions (bidirectional cascade). Example provincial factions: anti-caste Einhir faction, farming collective, not part of the Crown's appointment chain. Councils at settlement level are appointed bodies under governors.

- **OP-107** `RATIFIED` (+E,I) — Inherited casus belli: when a war's declarer dies the inheritor gains standing in a peace negotiation, not an automatic exit, so the ending stays contestable. \[Jordan ruling in design_rulings_2026-09-06.md:30-35 as quoted by a PROPOSED doc; closes Layer-1 F.32 (row unswept)\] `proposals/2026-09-12-emergent-narrative-primitives-v2/01_THE_TEN.md:485` · hook: F.32; succession of a war Proposition · conf M
  - Same doc: a war with a reason that is a Record others can be told about, forgeable or destroyable, expresses casus belli as a legal gate in declared vocabulary; and Jordan's ruling that the world must churn (R4).


### G / INTENT

- **GV-063** `INTENT` (+H) — Revocation bases as conjunct sets: purview alone (ordinary seats), purview plus holdings (duchy titles), or none (nobody may empty it; ends by death, resignation, succession). \[RATIFIED AS INTENT ED-IN-0235; revocation set later replaced by ED-IN-0256 rung-above-same-faction\] `proposals/2026-09-17-governance-and-holdings-r2/03_SEATS_AND_CONTENT.md:387` · hook: revocation conjuncts reaches, in_holdings · conf H
  - Jordan 2026-09-02: a Duke can revoke office under his purview; a King can revoke a Duke only if the duchy is in his holdings. 19 seats purview, 3 holdings, 7 none. Reaches defined once as descendants of the seat's rung. The holdings idea survives in code as rung_above_in_holdings.

- **GV-064** `INTENT` (+B,C) — Principle RR-P: the act is inviolate, reception is not: a draw may decide what HAPPENS but never what you MEANT; the world's churn is in how others receive and act on a player's choices. \[RATIFIED AS INTENT ED-IN-0234 (RR-P ruled by Jordan per RULINGS.yaml)\] `proposals/2026-09-17-governance-and-holdings-r2/02_THE_WRIT_AND_THE_WORD.md:192` · hook: Act.payload vs Claim · conf H
  - Jordan verbatim on sanctity of choices. Three boundaries: narrowing the option set is legitimate; failure is not corruption; reassigning intent is forbidden. Home in code: Act.payload against Claim. Binds all subsystems, including debate outcomes: a speech's content is not rewritten by a roll.

- **GV-065** `INTENT` (+J,B) — Authority descends by two people-borne channels, no broadcast: the Writ (a dispensation Record, issued and carried verbatim by give) and the Word (told_by claim spread by tell, lossy at Partial); compliance is the executor's own act. \[RATIFIED AS INTENT ED-IN-0234; absorbed where built; nothing executes (paper)\] `proposals/2026-09-17-governance-and-holdings-r2/02_THE_WRIT_AND_THE_WORD.md:367` · hook: issue; give; tell; Record kind dispensation · conf H
  - Writ content is immutable by absence of a producer: you do not amend a writ, you issue another and the executor holds two claims (agreement scores told-against-own). A writ that changes hands transfers its clock. Speed is not an axis (Jordan); differences are fidelity, addressing, evidence. 69 record.created events per season carry nothing (kind text, no subject_matter).

- **GV-101** `INTENT` (+B,M) — Placeless offices still have remit by class: a Cardinal may have no lands but jurisdiction over all Temples housing Knights Templars; a cluster seat gets a NOMINAL rung and its remit resolves against the class of thing its faction assigns. \[RULED by Jordan 2026-09-17 in session (RR-B, limb B-7 narrowed); record is a proposals ruling ledger, not code\] `proposals/2026-09-17-governance-and-behaviour/RULINGS.yaml:1690` · hook: Office.scope?; purview by class; reaches = contain_ascends · conf H
  - Ruled neither 'every seat gets a rung' nor pure null. Same ruling: B-8 narrowed to descendants only (drop the same-rung disjunct, which would license a same-rung coup); B-2 refused (who confers a seat is politics and the by-seat operand stays); B-1 keeps scope? as carrier of placeless jurisdiction.

- **GV-102** `INTENT` (+M,C) — H-71: a seated person must be able to know their own remit (person_side_eligible reads the holder's own Tenure payload) AND be understood by others for being seated; the second half, how others come to know or contest someone's remit, is explicitly not closed. \[CAT-6 ruled arm 2 (Tenure payload) by Jordan 2026-09-17; OTHERS half of H-71 left OPEN\] `proposals/2026-09-17-governance-and-behaviour/RULINGS.yaml:575` · hook: Tenure.payload; person_side_eligible · conf M
  - Jordan's 2026-09-16 design pressure quoted in the register. Arm 4 (a commission Record carrying a claim) was refused in the end. So public recognition of an office-holder's authority has no mechanism: a legibility gap for any debate about whether an officer was entitled to act.

- **PR-009** `INTENT` (+D) — Every verdict is appealable; an appeal is a proceeding whose matter is the disposition of a prior one before a bench whose remit reaches the first. Depth cap is declared by the opening act, never a default. \[00 PROPOSED; AX-6; seam.contest already takes depth/max_depth and returns Refusal(depth_cap) per the doc\] `proposals/2026-09-05-proceedings-subsystem/00_DERIVATION.md:231` · hook: seam.contest depth/max_depth; determine; release; repudiate · conf H
  - Closing paths: finding -> later determine; censure/excommunication -> T-o revocation via Act.via; imposed oblige -> release by the swearer; treaty -> repudiate by each committer separately. Exhaustion of appeals is a game mechanic. Default cap would be a fabricated constant (H-87).

- **PR-016** `INTENT` (+H) — A determination opens the disposal Tenure on its SUBJECT via the seat's conferral basis; determine.writes becomes degree-keyed (Tenure.since + Tenure.degree); the subject may release what the finding opened. \[21 RATIFIED AS INTENT (v9); C-1 supersedes 04_VERBS B.2 'UNCHANGED' note\] `proposals/2026-09-05-proceedings-subsystem/21_RECONCILIATION.md:158` · hook: determine; Tenure.since/degree; Act.via; release; disposes key · conf H
  - Mirrors confer. disposes: key finally gets a reader: load check that each arrangement row's disposes kind appears in ID-14 opener map for determine (or parties' oblige when disposal mutual). Write gate needs a conferral-via clause; confer matches none of four gate exceptions today. A convict can discharge his own penance, public and priced by reception.

- **PR-020** `INTENT` (+H) — A disposal's reach has three values: room (co_located, today), body (post_remit, free once determine emits disposal), and <rung kind> (needs a new channel keyed on disposal emission and the row's disposal_reach); chronicle channel matches nobody and is deleted. \[21 C-6 ruled (over-corrects PART F of 20_STRESS_TESTS)\] `proposals/2026-09-05-proceedings-subsystem/21_RECONCILIATION.md:285` · hook: disposal_reach key; co_located; post_remit; chronicle · conf M
  - disposal_reach splits reach of a ruling from reach of the arguing. Argument emissions deposit identically at room and realm; the disposal's do not. Same emission reaches differently by a data value.

- **PR-030** `INTENT` (+J) — Who witnessed the arguing (floor) and who learns the ruling (disposal_reach: room / body / rung kind) are orthogonal. A disposal is what reaches beyond the people who made it; announcement is a property of the disposal, not an act. \[03 B.7 Jordan ruling 2026-09-06; ratified as intent; 21 C-6 says the <rung kind> channel is not yet built\] `proposals/2026-09-05-proceedings-subsystem/03_PARAMETERS.md:249` · hook: disposal_reach key; witness scope of disposal emission · conf H
  - Jordan: closed parliament outcomes announce to the world as the parliament's decision, giving state change and propagation. Excommunication decided floor:closed, proclaimed to realm. Without reach, those compelled by a levy could not petition or make common cause.

- **PR-040** `INTENT` (+H) — GAME excommunication deliberation: bench disposal, closed floor, interposed procedure+ceremony, rank order, disposes a Tenure that severs a commit, reach realm. No subject_absent key: the subject simply did not travel. \[03 E.2 game row 7; ratified as intent\] `proposals/2026-09-05-proceedings-subsystem/03_PARAMETERS.md:648` · hook: arrangement row excommunication; commit severance; rank · conf H
  - Ceremony settles relative standing before a word but cannot absorb a substantive concession, so it buys the body authority and the absentee nothing. Severed commit is closable (T-m/AX-6); restoration is a later proceeding, not a mercy. Eligibility for every seat the body confers goes with it.

- **PR-044** `INTENT` (+D) — GAME appeal to higher authority: the only row that is a nested sibling, not a peer: matter is a prior finding, bench whose remit reaches the first, interposed document, order written_only, disposes closure of the prior tenure. \[03 E.2 game row 11; ratified as intent\] `proposals/2026-09-05-proceedings-subsystem/03_PARAMETERS.md:706` · hook: arrangement row appeal; seam depth; written_only order · conf H
  - seam.contest carries depth/max_depth and typed Refusal at cap. written_only models the Arabic telhis: counsel removed from face-to-face exchange so neither party is seen to yield; cost is losing the exchange where unshared information would have pooled.

- **PR-047** `INTENT` (+L) — Structure refuses: (1) disposal with no author (lot, self-executing ordeal; recovered as two games: physical contest then a bench that reads claims); (2) a shared transcript / common knowledge of verdict; (3) a proceeding that advances because time passed. \[03 F.2 three refusals; ratified as intent; AX-1/AX-2/AX-5 are the breaking axioms\] `proposals/2026-09-05-proceedings-subsystem/03_PARAMETERS.md:784` · hook: none (refusal register) · conf H
  - Costs: Athenian allotment/sortition, ordeal as law understood it, any UI showing the verdict as fact. Gains: verdicts can be denied, misreported, believed by wrong people. Honest residue: player wants to know what court decided and cannot be told. If sortition wanted, AX-1 must be broken deliberately.

- **PR-055** `INTENT` (+B) — release (eligibility own, writes Tenure.until, generic over tenure kinds minus contain) lets a person discharge their own tenure - resign an office, discharge a surety - and is also step 14: 'close, leaving the other party a way down' = releasing something you could have held them to. \[04 B.5; release absent from live verb table; 21 PHASE 2 step 8\] `proposals/2026-09-05-proceedings-subsystem/04_VERBS.md:638` · hook: release verb; Tenure.until · conf H
  - Needed for AX-6 and ID-14: what an act can open an act must be able to close. Currently hold closable only by revoke so a person cannot resign. 21 C-1: a convict can release his own penance - public and priced, accepted by ruling; D-5/ED-SC-0035 refuses a creditor-side closer.

- **PR-073** `INTENT` (+H,L) — Governing test for any game: (1) what in the world does it change - a disposal must write a thing somebody can lose (holding, seat, duty, life, document, bond); (2) why is each person in the room - because of what they hold, not a slot; (3, added) who learns it happened - disposal_reach. \[14 PART E Jordan ruling 2026-09-06 'ABOUT the world and enacted by characters OF the world'; binding on every row\] `proposals/2026-09-05-proceedings-subsystem/14_THE_WORLD_IN_THE_ROOM.md:237` · hook: disposes key; Record; create_record/carry/destroy_record/forge/comply/defy · conf H
  - Run over twelve rows: interrogation (disposes standing) and public debate (disposal none) FAIL question 1. Parliament/council/audience disposes Record (dispensation as a document carried, burned, defied) not 'issue'. Forbidden: disposal that writes only a Query; stakes internal to the proceeding (points, debate score); cast declared by arrangement; matter with no referent; outcome nobody can be told about.


### G / PROPOSED

- **CD-103** `PROPOSED` (+H,D) — Result tiers: T1 opinion (needs three builds), T2 the record (a held unexecuted resolution), T3a concurrence (owner's act needs a held resolution), T3b obligation (held). \[PROPOSED (2026-10-29), design only, CR-38's design file; HELD BACK from the merge default: its section 12 calls; sec 6\] `proposals/2026-10-29-parliament-and-debate/2026-10-29-parliament-and-debate.md:126` · hook: resolution Record; give; confer; revoke; issue · conf H
  - The assembly never acts on the world: it mints a document and a seat that already has power acts. Land and asset transfer enter at T3a, needing a data-owner discriminator (give has no via; warrant_sourced would gate every give). T3b: declining becomes a breach; held for Jordan.

- **GV-073** `PROPOSED` (+D,I) — Crown Policy instrument (emergency, session, taxation, trade, martial) is declared by the Crown, can be interrupted by a Hafenmark Parliamentary Manoeuvre, then needs Ministry countersignature to be in force. \[PROPOSAL 2026-09-03\] `proposals/2026-09-03-governance-corpus-rebuild/annex-b-state-graphs.md:602` · hook: w.crown_policy; PI band · conf H
  - Availability depends on Crown Mandate and PI band (Mandate>=4 at PI<=10, >=5 at PI>=11; unavailable at PI>=15 where Royal Decree is lost). Emergency Powers cost PI -1 per season held, Crown actions -2 difficulty, Nomination suspended. Ministry aggregate L<2 raises difficulty; 0 makes it unavailable. Check/balance among three institutions.

- **GV-084** `PROPOSED` (+C,M) — P7: a dispensation (order from above) is a Record whose terms are a typed roster; compliance is a per-executor contest, suspicion is the issuer's own ledger, recall is revoke. \[PROPOSED 2026-09-10, HELD BACK IN FULL (writ half later INTENT in r2 02)\] `proposals/2026-09-10-settlements-factions-populations/03_PROPOSALS_POLITICS.md:274` · hook: issue; comply/evade/refract; dispensation Record · conf M
  - Overturns a written refusal that typed the subject of comply as a dispensation. Goldenfurt Directive becomes issue once nine typed terms exist. Executor may comply, evade/defy or refract. Basis for a top-down order being received differently by each recipient.

- **OP-037** `PROPOSED` (+D,L) — Named mechanics a social-contest verb set needs: Date holder, derived arrangement for a computed case, petition addressee distinct from subject, Record disposal, contest provider, issue rung on the docket. \[PROPOSED named gaps M1-M16\] `proposals/2026-10-16-verbs/2026-10-16-verbs-11-lexicon-social-contest.md:527` · hook: rosters.yaml; state/gate.py DISPOSABLE_KINDS · conf H
  - Speech-kind reader, proofs reader, standing in telling, vote count, mood source, valence and threat readers, pursuits operand. Several marked 'no (roster loaded, unread)': proofs (record, testimony, oath, confession) exist in rosters.yaml:2095 with no reader. One vote count must serve both a bench vote and confer's 'elected' basis (GV-G44) or S fails.

- **OP-047** `PROPOSED` (+B) — `declare` is a seat-holder's public stance act (remit:dispatch) minting a Proposition whose mood by content is WAR (embargo, condemnation parked), broadcast by the binding_decision chronicle to everyone alive. \[PROPOSED verbs v2 FA suite S2\] `proposals/2026-10-16-verbs/2026-10-16-verbs-15-lexicon-faction-actions.md:124` · hook: verb declare/utter; at_war; war.declared · conf H
  - Proclaim is culled as a name in FA. Fixes 'a war of one' by writing the declarer's own edge. A private utter of mood WAR would no longer make a war. Lacks a reader of at_war and a public channel that survives the SC-01 step-13 change. Edict to one's own purview is governance (GV).

- **OP-058** `PROPOSED` (+F,I) — `declare`: a seat-holder mints a WAR Proposition plus his own commit; at_war counts only declare-minted WAR Propositions; a grievance occasion (a wound by a faction's doer) stamps that creed for every person. \[PROPOSED CP-T09-02\] `proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-09-factions-war-diplomacy.md:157` · hook: declare; at_war; war.declared; opinion_referents · conf H
  - A coalition is several declarations on one grievance. A killing starts no war until H-209 (dead victim's claim never asked about) closes. Unbuilt: world-tension meter, phased play. War ends when no committer is left.

- **OP-065** `PROPOSED` (+H) — Both outcomes bind: the winner concedes in proportion to the rung he ended on, concession = (final rung - 1)/4. \[PROPOSED\] `proposals/2026-08-29-valoria-from-scratch/08_argument.md:211` · hook: rider clause; dispensation issuance (doc 06) · conf H
  - The motion carries and the venue issues a rider scaling the thing allocated (rung 3: half the stake deferred; rung 4: carries in name only). Reads final rung not descent count so route cannot be gamed. Without it losing costs nothing extra and the dominant play is to open at rung 1 always.


### G / ARCHIVED

- **GV-010** `ARCHIVED` (+I,D) — Parliamentary Sanction ladder: Censure, Embargo, Blockade, Combined, Outlawry as one action at ascending severity, each with proposer minimum, vote bar, penalty and duration. \[ARCHIVED-NOT-CANON; reframing ED-FA-0006\] `.designs/systems/factions/reference/faction_layer_v30.md:463` · hook: sanction tier parameters · conf H
  - Censure Mandate2/majority: Stab-1 Mand-1. Embargo Mandate3: Wealth-1/season. Blockade Mil3: Wealth-2. Combined: supermajority. Outlawry Mandate5/supermajority: Mandate-2 Stab-2, CB to all, permanent until petitioned by target with Mandate>=3. Embargo/Blockade renew annually or lapse.

- **GV-011** `ARCHIVED` (+D,H) — Constructive motions: Subsidy, War Authorisation, Treaty Ratification, Recognition Challenge, Succession Endorsement, each with own object and vote bar. \[ARCHIVED-NOT-CANON\] `.designs/systems/factions/reference/faction_layer_v30.md:463` · hook: motion types; succession recognition · conf H
  - War Authorisation (Mil2, majority): first advance vs target is free and creates CB for 1 season. Recognition Challenge (Mandate4, supermajority): target loses 1 TCV from victory calc. Succession Endorsement (Mandate3, majority): endorsed NPC becomes recognised heir, succession Ob -1; rescind by supermajority.

- **GV-012** `ARCHIVED` (+I) — Target Rebuttal: the faction named in a Censure or Outlawry motion may spend an action to roll a Mandate-based defence that reduces or negates the penalties. \[ARCHIVED-NOT-CANON\] `.designs/systems/factions/reference/faction_layer_v30.md:455` · hook: rebuttal resolver on motion · conf H
  - Resolver M = Mandate-2 (Censure) or Mandate-3 (Outlawry). Failure: vote proceeds. Partial: Stability cost halved. Success: Stability negated, Mandate cost halved. Overwhelming: both negated, proposer Mandate -1 and target Stability +1.

- **GV-027** `ARCHIVED` (+H,J) — Court Attendance and Hostage-Kin: absentee governors at Standing 4+ must attend court yearly or accrue Suspicion at double rate; a kin hostage held at capital eases demotion triggers. \[ARCHIVED-NOT-CANON; RATIFIED per ED-FA-0020 (2026-07-13), then archived\] `.designs/systems/factions/reference/faction_politics_v30.md:123` · hook: suspicion field; court attendance scene · conf H
  - Sankin-kotai grounding. Court attendance costs 1 AP + Treasury. Hostage-kin is a named Knot NPC at the capital; makes a legible capture target; skipping attendance with a hostage held auto-escalates Suspicion. Composes with governance_play_redesign Suspicion field.

- **GV-028** `ARCHIVED` (+J) — Demotion magnitude and appeal: default one rank, severe two or three, total dismissal at Standing -1; demoted player may appeal within 2 seasons via the faction's internal Piety Track contest. \[ARCHIVED-NOT-CANON; ED-776\] `.designs/systems/factions/reference/faction_politics_v30.md:69` · hook: demotion magnitude; appeal contest · conf H
  - Excommunication, treason, framework abandonment give Standing -1 and Dishonored flag, no re-entry in that branch. Appeal adjudicated by a supervising Standing-7 NPC or institutional body; failure is permanent that year. No appeal for Dismissal.

- **GV-036** `ARCHIVED` (+B,M) — The Directive: each season the Provincial Authority issues one typed order (Extract, Tax, Suppress, Install, Host, Cede) and the governor must Comply, Bargain (social contest as petitioner), or Defy. \[ARCHIVED; PROPOSAL 2026-06-22 (Directive dual-authority parts ratified via ED-IN-0046 per consolidation doc)\] `.designs/systems/settlements/reference/governance_play_redesign_v1.md:119` · hook: directive/response; suspicion track · conf H
  - Defy accrues a suspicion track +1; threshold triggers Recall scene (social contest to justify), audit, or replacement. A governor who repeatedly defends the settlement against its own faction walks toward faction-emergence. Directive vs settlement Needs routinely conflict; AP cannot serve both.

- **GV-037** `ARCHIVED` (+J,F) — Ledger of Consequence: governance choices write durable tags (Precedent, Grudge, Debt, Reputation, Compact) that bias later rolls, events and NPC behaviour, and survive succession. \[ARCHIVED; PROPOSAL; D3 of consolidation keeps built five families\] `.designs/systems/settlements/reference/governance_play_redesign_v1.md:139` · hook: settlement ledger tags · conf H
  - Precedent: rulings bias related events +-1 Ob. Grudge: wronged actor's hostile weight up. Debt fires when due (sponsorships, Treat favours). Reputation: Just/Harsh/Generous/Weak/Hated modifies starting Disposition. Compact (fixed-term extraction deal) was reconciled to a Debt subtype in consolidation D3.

- **GV-042** `ARCHIVED` (+H,L) — Consolidation rulings: card-deck events canonical for play, AP economy canonical, ledger keeps five families, suspicion accrual cumulative per Defy-season with a symmetric suspicion-reduction counter (E11) required. \[ARCHIVED; D1-D6 RATIFIED 2026-07-13 (ED-IN-0046, ED-IN-0047) per its own header; Key-substrate content later retired ED-IN-0232\] `.designs/systems/_architecture/reference/governance_consolidation_v1.md:11` · hook: mandate-challenge (undefined); suspicion counter · conf M
  - Also E2: author a Mandate-Challenge as a bounded Parliament/Mandate-track contest for non-violent removal of entrenched privilege (Seggio, lapsed charter, Church infra); E1 port Goldenfurt death-spiral fixes. Mandate formula round(7T/(T+6)) retired as collapse carrier. Ratification claims here are prose, not code.

- **GV-046** `ARCHIVED` (+H,F) — Institutional bodies per faction scaffolded as ministries: Crown Ministries, Hafenmark committees, Church Dicasteries (chaired by Cardinal), Varfell Councils, each with Competence and Corruption or Readiness tracks. \[ARCHIVED; PROPOSED expansion of ministries\] `.designs/systems/factions/reference/faction_politics_v30.md:932` · hook: institutional body tracks · conf M
  - Church Dicastery staffing by appointment (Canon, Bishop's Delegate, Prelate), Cardinal chairs; a Confessor can rearrange jurisdictions at a Stability cost. Low dicastery Competence raises odds of named Event Cards (Prudence Crisis, Jarnstal Independence). Differing institutional logic by faction ethic (Virtue, Categorical Imperative, Utility).

- **HP-082** `ARCHIVED` (+I,E) — Sanction ladder in five tiers: Censure, Embargo, Blockade, Combined, Outlawry, each with proposer minimum, vote threshold, target effect and proposer cost. \[retired design (ED-FA-0006); catalogue says only Censure was built\] `research/cross_scale_action_catalogue_v1.md:152` · hook: none (retired) · conf H
  - Outlawry needs Mandate 5 and a supermajority, gives Mandate -2, Sta -2 and a casus belli to all, permanent until petitioned. Constructive motions (Subsidy, War Authorisation, Treaty Ratification, Recognition Challenge, Succession Endorsement) all unbuilt.

- **OP-010** `ARCHIVED` — A Decisive win in a Formal or Grand Contest produces a binding Obligation: the winner names one achievable, verifiable commitment the loser must honour for a fixed duration. \[ARCHIVED; ED-619\] `.designs/systems/social_contest/reference/social_contest_v30.md:314` · hook: clock_registry (named in doc) · conf H
  - Duration: Formal 2 seasons (violation Mandate -1, Reputation shift, Fatigue), Grand 4 seasons (Mandate -2, Stability -1, +2 Ob next DA), Royal Audience 2, Church Tribunal until revoked. Settlement-targeted variants use settlement stats as the verification condition. Tracked as clocks.

- **OP-014** `ARCHIVED` (+B,I) — Heresy Investigation lifecycle: Initiation (1 season), Investigation Proper (2-4 seasons, one asymmetric Interrogation per season), Verdict (Acquittal / Insufficient Evidence / Tribunal Recommended). \[ARCHIVED; ED-772\] `.designs/systems/social_contest/reference/social_contest_v30.md:449` · hook: Mandatory Zoom-In (scale_transitions 4.3.2 per doc) · conf H
  - Eight closure conditions: Inquisitor death/demotion/reassignment, target death/defection/faction protection, acquittal, faction conversion. Parliamentary Stay suspends one season. Total nominal 4-6 seasons. Only one active investigation per target per Cardinal Justice jurisdiction.

- **OP-015** `ARCHIVED` (+H) — Excommunication Tribunal: Church-initiated asymmetric proceeding with track starting at 7, no accused corroboration, 1-3 exchanges; success sanctions by target type; revocation via Act of Contrition. \[ARCHIVED; ED-625\] `.designs/systems/social_contest/reference/social_contest_v30.md:632` · conf H
  - Prerequisites CI>=40, Church Mandate>=4, evidence. Named NPC: CI+4, target Mandate-2, Truth forced low. PC: faction Mandate-3, excluded from Parliamentary motions, Standing-2. Faction: Mandate-2.


### G / NOTCODED

- **CD-010** `NOTCODED` (+H) — Appeal, term-bounded disposals, interposed intermediaries (person/office/document/procedure/ceremony/pair) and the reach of a disposal are declared but unenforced. \[keys term_required, appeal_basis, interposed, disposal_reach, bench_basis loaded; no reader\] `engine/season/loop/effects_information.py:597` · hook: arrangement appeal_basis/interposed/disposal_reach/term_required · conf H
  - effects_information.py:597 says term_required 'has no reader yet'. detain and ban open with no term. bench_basis is the constant BENCH_BASIS 'determine' in gate.py:243, not read from the row, because every seeded row says determine.


### G / RESEARCH

- **HP-063** `RESEARCH` (+I) — P21 Return-Unsigned (fengbo 1384, fenghuan, kecan): clerical layer refuses to transmit an edict sealed rather than promulgate it. \[SOURCE MATERIAL, not canon; self-authored upload with T0/T1/T2 evidence tiers (per research/by_lane/SC_social_contest.md)\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:415` · conf M
  - A low-ranking power over a high-ranking actor and career-threatening; pair with a personal risk roll rather than a plain veto. T1 chinaknowledge.

- **HP-066** `RESEARCH` (+J) — P29-P31 information: inspection circuits (missi, Venetian Sindici Inquisitori ~30-person cortege, Ming censors), sealed channel versus open accusation, rumour and reputation drift. \[SOURCE MATERIAL, not canon; self-authored upload with T0/T1/T2 evidence tiers (per research/by_lane/SC_social_contest.md)\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:465` · conf M
  - Inspection has separate informational and theatrical legitimacy effects. Open accusation is costly but builds Standing if vindicated; sealed is safe and deniable. Venetian ambassador reported straight to the Ten from 1480 (T2).

- **HP-067** `RESEARCH` (+I) — P34 Detection Rate and Graduated Sanction: two coupled dials; stability is as sensitive to certainty of detection as severity of sanction. \[SOURCE MATERIAL, not canon; self-authored upload with T0/T1/T2 evidence tiers (per research/by_lane/SC_social_contest.md)\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:496` · conf M
  - From Ostrom design principles 4 and 5 (T1). A savage-but-rare-monitoring regime should be visibly less stable than frequent inspection with light fines.


### G / HISTORICAL

- **CL-040** `HISTORICAL` (+B,C) — Remontrance escalation ladder: Parlement remonstrates, king issues lettre de jussion, Parlement files remontrances itératives, king imposes lit de justice. Remontrance = opposition affirming the authority it opposes (appel comme d'abus). \[RESEARCH; French scholarship, conf high\] `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:493` · conf H
  - Right of sovereign courts to contest an edict before registration, a legitimated pre-enactment check. Distinct instrument from the supplique (subject asks grace). Doc recommends building the appeal system as TWO mechanics (line 359). Also evocation: jurisdiction more than justice decides (corroborates translative = Stay).

- **CL-067** `HISTORICAL` (+B,C) — Supplication as a binding performance (Koziol): public self-abasement in fixed language and gesture costs the supplicant and costs the recipient MORE to refuse, since public refusal damages his claim to rule by grace. Binds the powerful with no enforcement. \[SOURCE MATERIAL; T1 Koziol 1992 (reviewed AHR, JEH), single-region caveat\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/05_persuasion_in_the_era_sources.md:79` · conf M
  - Doc N17: third resolution beside argue and trade ('perform'). Form varies by region/community and shifted from hierarchical distance toward equality across 10th-12th c. Own audit B6: no failure state; wrong form should fail and humiliate. Distinct from the research-doc petition corpus (CL-039).

- **CL-068** `HISTORICAL` (+J,I) — Kishomon self-cursing oath: statement plus anathema clause naming deities; talismanic paper, split in half between parties, held/mediated by local collectives; the form escalates (plain, talisman, seal, blood) as trust falls, so the prevailing form reads world trust. \[SOURCE MATERIAL; T1 kishomon corpus; Ogino inference T2, contested (CONFLICT line 302)\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/05_persuasion_in_the_era_sources.md:94` · conf M
  - Doc N18; replaces flat 'costly signal' bond. Audit B7: needs a world-trust state that no system defines; B9: blood-signature inflation rests on one scholar's reading, criticised by Okouchi.

- **HP-002** `HISTORICAL` (+J) — Roman Senate had no legislative power yet its senatus consulta and auctoritas (collective standing opinion) throttled provincial, war and finance decisions. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:107` · hook: L/PS consent gate (proposed) · conf M
  - Soft power constraining hard power. Repo hook: a non-binding council whose L/PS-weighted opinion makes a Monarch-tier act cost Legitimacy/Popular-Support to execute. Senate grew c.300 to 600 (Sulla) to 900 (Caesar).

- **HP-006** `HISTORICAL` (+B) — Capitularies: royal clause-lists issued after deliberation with magnates, read aloud by counts/missi; assembly input, royal-command output. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:154` · hook: none (Key substrate retired) · conf M
  - Admonitio Generalis 789 (82 clauses), Capitulare de Villis, Quierzy 877 (conceded heritable counties). A hybrid DELIBERATIVE_ASSEMBLY input with AUTOCRATIC_FIAT output; repo maps it to a Directive-vs-Need gap per province.

- **HP-007** `HISTORICAL` (+J) — Missi dominici: paired lay magnate plus bishop/abbot sent from outside the circuit, hearing placita, taking oaths, able to depose or refer. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:158` · hook: Standing demotion trigger (proposed) · conf M
  - Anti-collusion by design; regularised 802, re-regularised under Louis the Pious c.825, eroded 850s-860s. Repo hook: demotion needs two independent audit channels (material + interpretive) to concur.

- **HP-009** `HISTORICAL` — General oath of fidelity from all free adult males (792/793 and elaborate 802), administered by missi, listing duties. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:170` · hook: L/PS gate (proposed) · conf M
  - Verifier flags the 789 attribution as unverified. Repo hook: a population-wide oath Key feeding Legitimacy directly, bypassing the noble Standing ladder as a Monarch-tier reservoir.

- **HP-024** `HISTORICAL` (+J) — Promissione Ducale: each doge swore an oath lengthened by the Correttori to close the last doge's abuses; Inquisitori sopra il Doge defunto audited his term and fined the estate. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:325` · hook: resolution-quality to standing bridge (proposed) · conf H
  - Oath at accession, reconciliation at exit; doge could not receive envoys or write abroad privately and had no veto. Repo hook: appointment and exit events carry the same promise payload; a bad gap narrows the successor.

- **HP-027** `HISTORICAL` (+J) — Avogadori di Comun: three legality guardians who could suspend or annul any act of any body, even the Great Council, if procedurally improper. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:349` · hook: legality auditor (proposed) · conf H
  - Also verified patrician birth entries. Repo hook: an independent auditor emitting a retroactive null of an improperly obtained standing gain, closing the gap where procedural fraud games the arithmetic.

- **HP-029** `HISTORICAL` (+M) — Myth of Venice: St Mark civic religion, Sposalizio del Mare, and Contarini's 1543 mixed-constitution theory (monarchy, aristocracy, democracy) after Polybius. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:357` · hook: L/PS legitimacy source (proposed) · conf H
  - Repo uses Contarini/Polybius, not Mandate of Heaven, as the cited grounding for why mixed hybrids resist collapse. Legitimacy from correct procedure.

- **HP-038** `HISTORICAL` (+I) — Four generative conflict mechanisms: succession vacuum, autonomy-equals-secession, displacement grievance, channel starvation; plus relief valves (Venetian graduated removal ladder, Ottoman grand-vizier scapegoat) versus Rome's valve-less third century. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/conflicts_power_struggles.md:20` · hook: relief valve / scapegoat (proposed) · conf H
  - Venice: soft rebuke, forced co-signature, deposition, with a procurator sinecure absorbing blame. Repo hook: intermediate consequences bleed pressure before all-or-nothing revolt.

- **HP-041** `HISTORICAL` (+I) — Reichsacht (imperial ban): offender loses protection, fiefs and standing; Henry the Lion banned 1180 and duchies split; Reichsexekution authorised by the Diet to enforce. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/political_hierarchy_standing.md:238` · hook: Demotion Magnitude (proposed) · conf M
  - Diet's collective capacity as the closest analog to recall. Repo hook: gap between delivered and demanded peace licenses escalation from individual penalty to collective enforcement.


### G / GAME

- **HP-060** `GAME` (+I) — P18 Enactment Clock: passing a measure becomes a process of N timed stages with running success and stall chances; setbacks accumulate to failure and a lockout; attempting mobilizes the opposition. \[SOURCE MATERIAL, not canon; self-authored upload with T0/T1/T2 evidence tiers (per research/by_lane/SC_social_contest.md)\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:397` · hook: none (no enactment clock exists per SC evaluation) · conf M
  - From Victoria 3 law enactment (T0 wiki): three-setback failure, two-year lockout, 100-day stage, legitimacy modifiers; counter-mobilization marked UNVERIFIED against current patch. Odds must be visible.



## H · Transfers of land, office and asset — 33 entries (CODED 5, RATIFIED 1, INTENT 1, PROPOSED 6, ARCHIVED 13, NOTCODED 1, RESEARCH 1, HISTORICAL 5)


### H / CODED

- **CD-039** `CODED` (+G) — give: a holder hands a Record or a Rung (cession) to a present receiver, closing his hold and opening the receiver's. The consensual route for title to move. \[verb row give, verb_table.yaml:571; effect effects_information.py:795\] `engine/season/verb_table.yaml:571` · hook: verb give; Tenure hold; rung.ceded · conf H
  - Rung cession executes 0 times in computed play (H-229): no person forms a gift of a rung he holds, because no question source names a held rung. Land and office change hands in practice only via confer/revoke or seizure.

- **CD-040** `CODED` (+F) — seize: a seat with remit 'issue' whose purview reaches the subject takes a Record or settlement from its holder (record.seized, rung.seized): confiscation by seat authority. \[verb row seize, verb_table.yaml:1151; effect effects_information.py:904\] `engine/season/verb_table.yaml:1151` · hook: verb seize; remit issue · conf M
  - Graded 'assumption'. Needs no bench, no hearing, no petition: confiscation and quo warranto are NOT routed through determine or any arrangement.

- **CD-041** `CODED` (+G,D) — confer fills a vacant office for a living person (one holder per object); revoke closes a hold by a seat directly above in the same faction; an appointed revocation also opens a permanent ban. \[verb rows confer (:261), revoke (:1090); effects_governance.py:59, :260\] `engine/season/verb_table.yaml:261` · hook: verb confer; verb revoke; REVOCATION_DISPOSAL · conf H
  - Authority is the seat exercised (via), not the person. REVOCATION_DISPOSAL (Jordan, IN-31): appointed -> ban; elected/annex/None -> nothing. Removal of an official is possible by a superior; removal BY a vote of an assembly is not.

- **GV-048** `CODED` (+G,B) — A seat is filled by exactly one of three conferral bases: appointed, elected, annex. Closed set (open:false); a fourth is a design change. \[code: roster read by Office.__post_init__ and state/gate.py; source ED-IN-0256 ruling (2), Jordan 2026-09-18\] `engine/season/rosters.yaml:2304` · hook: Office.conferral; has_conferral_basis; may_fill · conf H
  - Verbatim ruling 'appointed, elected, annex'. Membership only is enforced: confer admits all three; no election or annexation verb exists, and the mapping from basis to act is unruled. Replaces the older confer/determine/succeed set. Heredity (succession) is deliberately not a conferral value; hereditary seats carry conferral null.

- **GV-051** `CODED` (+B,M) — Authored seat table: each seat has rung anchor, body or faction, remit_acts, conferral, revocation, holder case id, obligees; King holds [issue, determine, confer, revoke, convene], hereditary so conferral null. \[code: 31 authored seats read by build_realm; 14 of 29 original have revocation null by Jordan ruling 2026-10-11\] `engine/season/offices.yaml:181` · hook: seat remit_acts; obligees (oblige tenure) · conf H
  - Remit acts are a closed roster (issue, determine, confer, revoke, dispatch, convene). Cardinals, Senior Inquisitor, Archbishop's Rep and Grand Master are revocation null (cannot be stripped in built realm). Grand Master's oath makes the Lowenritter a Crown subfaction; her release is the Split. Hereditary succession left null as a flagged judgment call.


### H / RATIFIED

- **GV-098** `RATIFIED` (+B) — Settlement of the Secession: the Crown is first among equals, not absolute sovereign; Hafenmark retains parliamentary traditions; Varfell territorial independence; ducal authority cannot be unilaterally overridden. \[canon/ foundations timeline (canon world truth)\] `canon/03_canonical_timeline.md:88` · hook: none (world truth) · conf H
  - Deed-monarchy stabilises into hereditary within a generation; deed-presumption is rebuttable and enforced by the Coup Counter and Motion of No Confidence. Cognatic senior succession. Ducal families earned status by wartime deeds. Underwrites why Parliament has no monopoly in the ruler (H-90).


### H / INTENT

- **GV-062** `INTENT` (+D,G) — Conferral bases first drawn as confer (a superior names), determine (a body/electorate decides at a sitting), succeed (designated heir): three ways a seat is filled. \[RATIFIED AS INTENT ED-IN-0235 (its confer/determine/succeed set was superseded by Jordan's ED-IN-0256 appointed/elected/annex)\] `proposals/2026-09-17-governance-and-holdings-r2/03_SEATS_AND_CONTENT.md:342` · hook: Seat.conferral; determine at a Date · conf H
  - Seats: 6 succeed (crown, heir, regent), 8 determine (Jarl council seats, commune rep, Guild comptroller, Confessor, Duke of Varfell), 15 confer. 'determine' seats filled by a sitting at a fired Date, not by confer. Warrant (consecration) was refused as a fourth basis; widen the door instead. Later replaced in code by appointed/elected/annex.


### H / PROPOSED

- **GV-071** `PROPOSED` (+E,A) — Casus belli as ledger entries (holder, target, source, mode class, expires = created+3 seasons) with predicate-defined sources: adjacent instability, crown restoration, consensual (mutual regard >=2), appeasement (Turmoil>=7 or insurgency), punishment (excommunication, treaty violation, scars>=3). \[PROPOSAL 2026-09-03; predicates marked as new defaults (diamond)\] `proposals/2026-09-03-governance-corpus-rebuild/annex-b-state-graphs.md:605` · hook: rel.cb ledger; D-09.05/06 · conf H
  - Eleven CB sources including trespass, seizure attempt, pledge breach. Transfer protections: holder not on last province, target not proposer's, proposer parliamentary, a CB with matching mode exists, not used this arc. Lifetime of 3 seasons is a default, not source.

- **GV-076** `PROPOSED` (+D,G) — Motion pipeline: declared (Senator-class, extra-parliamentary excluded) > vote > majority > kernel check where the motion has one (Transfer, Censure, Outlawry, Embargo) > Stay may be invoked by any parliamentary polity > suspended until a treaty, Crown Session or arc end. \[PROPOSAL\] `proposals/2026-09-03-governance-corpus-rebuild/annex-b-state-graphs.md:625` · hook: motion pipeline PL-09.03; stay · conf H
  - Censure: proposer Influence vs holder aggregate L; success L -1. Outlawry: same vs +2, L -2. Embargo: Wealth -2/season for an arc. Transfer outcomes set Order pin 1 (2 for Appeasement). A Stay is thus a procedural hold, not a verdict.

- **GV-077** `PROPOSED` (+D,F) — Succession contest as state machine: leader loss opens a contest (unless a sole heir with Disposition>=+3, Standing>=4); contenders by rank, blood, office or backing; Stage 1 decides leader, Stage 2 decides fragmentation by gap G (>=3 unified, 2 fractious, <=1 split). \[PROPOSAL\] `proposals/2026-09-03-governance-corpus-rebuild/annex-b-state-graphs.md:86` · hook: PL-10.01/10.02 succession; regency · conf H
  - No contender gives regency; three empty contests collapse the faction. Split divides provinces by nearness to contender, units by Disposition+Discipline. Baralta Stake Claim +2 strength; Consecration Crisis decided by Church Stability. Reunification by treaty needs both Mandate>=3. Collapse (Stability 0) feeds insurgency.

- **GV-097** `PROPOSED` (+G,B) — Folded governance verbs: appoint, designate, elect, steward, rotate fold onto confer; dismiss onto revoke; amend onto establish; resign/abdicate/abandon onto release; annex onto seize's Rung half; elect waits on a count reader (M-COUNT). \[PROPOSED lexicon (verbs proposal 14)\] `proposals/2026-10-16-verbs/2026-10-16-verbs-14-lexicon-settlements-and-governance.md:133` · hook: confer/revoke/release folds; M-COUNT · conf H
  - Voters' act is social contest's vote = their own commit (V127); the chair only seats the winner. Completeness gap flagged: top seat cannot be emptied against its holder and an elected seat has no count. Termed seats make regency and term limits.

- **OP-049** `PROPOSED` (+B) — Succession: Jordan's rule that a designated heir is a status or title, not a verb, and the heir must still claim the throne. \[PROPOSED/planned (IN-61, RS-27/RS-29, Jordan quote); verb_table succeed currently effect declined\] `proposals/2026-10-16-verbs/2026-10-16-verbs-15-lexicon-faction-actions.md:355` · hook: verb succeed; off_heir; conferral basis inheritance; arrangements succession · conf H
  - `succeed` becomes the heir's own claim opening the throne's hold under a new `inheritance` conferral basis. designate is culled (it is the king's confer of the heir title). A rival's contest is docketed under an SC-04 `succession` arrangement (unseeded, no hold-disposal site yet). Today's row has the holder designate with effect declined.

- **OP-108** `PROPOSED` (+B,D) — Three and only three ways a seat is filled: confer (a superior names the holder), determine (a body decides at a fired Date: council, assembly, chapter or electorate), succeed. \[PROPOSED r2 (2026-09-17), cites ARCH section B.7 and AX ID-14\] `proposals/2026-09-17-governance-and-holdings-r2/03_SEATS_AND_CONTENT.md:354` · hook: conferral bases; determine; succeed · conf H
  - (the designated heir claims it, own-eligible with no remit); a fourth (warrant, for consecration) was refused because consecration is determine by a judging set outside the seat's containment path. At that time determine had no effect body (grade absent). Seats filled by a process are refused by confer outright.


### H / ARCHIVED

- **GV-001** `ARCHIVED` (+D) — Parliamentary Territory Transfer: a faction with a casus belli moves a territory from holder to proposer by parliamentary vote plus Influence-vs-Legitimacy roll, once per arc. \[ARCHIVED-NOT-CANON; was 'CANONICAL Pass 2h 2026-05-17'; derivation choices marked PROVISIONAL\] `.designs/systems/factions/reference/parliamentary_transfer_v30.md:28` · hook: territory transfer; cb ledger (proposer,holder) · conf H
  - Pool = proposer Influence; Ob = holder Legitimacy + PARL_MAJORITY_OB_BONUS (2). Frequency 1/arc/faction; CB consumed win or lose. Outcomes: Overwhelming/Success transfer (Accord set to 1; OW also holder Legitimacy -1); Partial yields new CB for retry; Failure costs proposer Stability -1 and gives holder Legitimacy +1.

- **GV-002** `ARCHIVED` (+I) — Transfer protections: last-territory protection, extra-parliamentary factions may not move motions, no self-transfer; blocked at declaration, not rolled. \[ARCHIVED-NOT-CANON; PARL-PROTECTION-001 provisional\] `.designs/systems/factions/reference/parliamentary_transfer_v30.md:50` · hook: declaration gate · conf H
  - Cannot strip a faction's last territory (holder with 1 territory is blocked at action-declaration). GD-3: emergent extra-parliamentary factions (e.g. promoted RM) may join treaties/CB economy but not make formal parliamentary motions. Self-transfer block was a Pass 2h derived addition.

- **GV-003** `ARCHIVED` (+E,G) — Four transfer modes (Adversarial, Consensual, Punishment, Appeasement) share one roll table but differ in which casus belli qualify and in outcome riders. \[ARCHIVED-NOT-CANON; mode-specific effects PROVISIONAL (PARL-MODE-DRIFT-001)\] `.designs/systems/factions/reference/parliamentary_transfer_v30.md:58` · hook: transfer mode declared at proposal · conf H
  - Adversarial: military/adjacent-instability CB, holder opposes. Consensual: negotiated agreement CB, no holder Legitimacy loss on failure. Punishment: excommunication/Conviction Scar/treaty-violation CB; holder gets no L+1 on failure, Standing -1 instead. Appeasement: crisis-stability CB; Accord +2 on success. Sim mix ~75% adversarial, 15% consensual, 5%/5%.

- **GV-004** `ARCHIVED` (+A,G) — Eight casus belli sources feed Parliamentary Transfer, tracked per (proposer,holder) pair, stacking, one consumed per attempt. \[ARCHIVED-NOT-CANON\] `.designs/systems/factions/reference/parliamentary_transfer_v30.md:73` · hook: cb ledger per faction pair · conf H
  - Sources: Crown constitutional restoration (Crown territories <6), adjacent instability (Accord<=1 neighbour, persists 1 arc), Einhir Revival Partial, prior Transfer Partial, Military Conquest, treaty violation, excommunication, Conviction Scar count >=3 (all parliamentary factions get Punishment CB). CB consumed on use.

- **GV-026** `ARCHIVED` (+G,E) — Recognition fork: granting authority chooses honryoando (confirm existing holding, rank unlock withheld, demotion triggers ease) or shin'on (full new grant), as a graduated stonewalling lever. \[ARCHIVED-NOT-CANON; PROPOSED ED-FA-0019\] `.designs/systems/factions/reference/faction_politics_v30.md:106` · hook: recognition event: confirm vs new-grant · conf H
  - Kamakura grounding. Confirm fires the ceremony but withholds mechanical unlock; two Confirms in a row for a qualified candidate is a legible political signal (player may petition, cultivate rival patron, or Defy). Applies to Standing-3 Recognition Events and Standing-5 Recognized Deeds on all four ladders.

- **GV-034** `ARCHIVED` (+F) — Faction political value (for parliamentary influence and Mandate inputs) = sum of territory values + unification bonus for fully owned provinces, rewarding consolidation. \[ARCHIVED; PROVISIONAL PP-726, formula marked TBD; sections superseded by scale_hierarchy_v1\] `.designs/systems/settlements/reference/valoria_political_hierarchy_v30.md:90` · hook: political_value(faction) · conf H
  - Structure canonical, numbers TBD. Territory value from settlement type plus Prosperity/Defense/Order. Two of three territories gets no bonus; the third triggers it. Implies parliamentary disadvantage for fractured holdings. Governor assigned per settlement by controlling faction (Standing 3+ NPCs and PCs eligible).

- **GV-035** `ARCHIVED` (+D,F) — Franchise 0-5 per territory is its parliamentary weight; faction National Influence is the Franchise-weighted average of its per-territory influence, recalculated at Accounting. \[ARCHIVED; was DRAFT awaiting Jordan review\] `.designs/systems/factions/reference/franchise_v30.md:30` · hook: franchise stat; national_influence · conf H
  - Territory Influence = +2 controller +infrastructure(0-3) +1 NPC +1 governor, clamp 7. National = clamp(round(sum(TI x franchise)/sum(franchise)),1,7). Crown holds 49% of Franchise, Varfell 13% (caste stigma). Shift triggers +-1: 4 seasons stable (+1), revolt (-1), Church seizure (-1), Lowenritter coup (-1).

- **GV-039** `ARCHIVED` (+G,J) — Charters, prescription and Quo Warranto: a granted charter is a durable tag that survives succession; revocation Ob rises with age; revoking an old charter requires a public Quo Warranto contest. \[ARCHIVED; mixed PROPOSED (ED-SE-0010) and RATIFIED (ED-SE-0021, 2026-07-13) sub-sections\] `.designs/systems/settlements/reference/settlement_layer_v30.md:597` · hook: charter tag; revocation Ob; patron lapse · conf H
  - Ob = base revoke (subnational Influence/2) + floor(age_seasons/8). Over ~16 seasons triggers public contest with peninsula-wide chilling effect (-1). Za model (ratified): charter may carry a patron whose standing backs it; if patron falls below threshold privileges lapse automatically at Accounting with a prior warning card.

- **GV-040** `ARCHIVED` (+G,J) — Entry Terms at control transfer: new controller chooses Confirm Privileges (keeps charters, L seeds 3, tax capped) or Impose Administration (strips tags, L seeds 1, Order -1). \[ARCHIVED; PROPOSED ED-SE-0011\] `.designs/systems/settlements/reference/settlement_layer_v30.md:969` · hook: transfer fork; L seed · conf H
  - Joyeuse Entree / Henry I coronation charter grounding versus Olson roving bandit. Seeds L rather than incrementing. Transfer (faction changes) is governed here; succession (same faction, new leader) by s1.8b; never both on one settlement in one season.

- **GV-044** `ARCHIVED` (+E,M) — Treaty Expiration: each active Crown Treaty rolls to lapse at every arc boundary (default 0.90), forcing continual re-binding via Senator Outward at Wealth -2. \[ARCHIVED; was CANONICAL Pass 2h; violation sub-section PROVISIONAL\] `.designs/systems/factions/reference/treaty_expiration_v30.md:15` · hook: treaty lapse roll; violation cb · conf H
  - Lapse is peaceful: no CB, no Standing delta. Violation (attack, external CB support, Parliamentary Transfer vs treaty partner) voids the treaty, grants wronged party CB, violator Standing -2, wronged +1. Memoryless independent rolls. Roman foedera / coronation oath renewal as anchors. Author flags 90% as narratively extreme.

- **GV-079** `ARCHIVED` (+D,I) — Hochjarl Incapacity Assessment: any Senior Jarl declares it at the Assembly (costing Disposition -1 with the leader); all Senior Jarls vote, 3 of 5 confirms; a Regent serves at least 2 seasons; no recovery after 4 seasons means permanent removal and elective succession. \[ARCHIVED; was CANONICAL (ED-673)\] `.designs/systems/factions/reference/faction_politics_v30.md:270` · hook: assessment vote; regency · conf H
  - Triggers: physical (2 seasons), mental (2 sessions of incoherent orders), prolonged absence (3 sessions without Regent), conviction collapse (Truth 0 and 3 Scars). Accused may defend in a Social Contest Ob 2 (success flips one vote). Gives regency/delegation a procedure: Hochjarl or highest-Military Senior Jarl acts as Regent.

- **GV-106** `ARCHIVED` (+G,D) — Quo Warranto: revoking a charter older than about 16 seasons is a public scene (a social contest) with a peninsula-wide chilling effect, scaled by prescription so privilege hardens into right with age. \[ARCHIVED; PROPOSED ED-SE-0010\] `.designs/systems/settlements/reference/settlement_layer_v30.md:597` · hook: charter tag; quo warranto scene · conf H
  - Edward I quo warranto 1278-94 and London charter forfeiture 1683 as grounding. Revocation Ob adds floor(age/8). Seggio privileges are exempt from quo warranto and the standard grant/revoke action (inherit, marry, or seize only). Charters survive succession.

- **OP-013** `ARCHIVED` (+B) — Succession Contest: on removal of a faction leader a Grand Contest opens at next Accounting among claimants with Standing >=5; an institutional body (per-faction) adjudicates. \[ARCHIVED; ED-665 closure\] `.designs/systems/social_contest/reference/social_contest_v30.md:408` · hook: Succession; faction leadership · conf H
  - Adjudicators: Crown inner circle by Disposition majority, Hafenmark Parliament Mandate-weighted, Varfell Jarl Assembly by quorum, Church College of Cardinals, Lowenritter Knight-Commanders by seniority, Guilds Council Favour-weighted. Track length 3-7 by contested-ness. Decisive = single leader; Compromise = faction split; Total Victory = unified plus Wager power.


### H / NOTCODED

- **GV-085** `NOTCODED` (+D,L) — CR-34: a vote at a sitting counts live commits; determine on a 'declared' disposal row needs at least quorum bench members with a live commit to an OUGHT naming the party and the disposal kind (ED-SC-0034 C-7, H-161). \[workplan v10 position CR-34, STATE BUILD; arrangement rows carry no 'disposal: declared' (grepped arrangements.yaml: only header text)\] `workplans/valoria_master_workplan_v10_part4.md:352` · hook: determine quorum conjunct; judging_set; commit tally · conf H
  - Loyal-creed hazard closed: a commit to a faction creed whose subject is the leader does not count as a vote against him. Excommunication_deliberation becomes the first declared row, quorum 2 (swept 1-3). parliamentary_debate NOT flipped because it disposes a Record and _eff_determine declines Records. This is the planned parliamentary 'count'.


### H / RESEARCH

- **HP-069** `RESEARCH` (+E,G) — P36 Charter of Submission: negotiated terms of incorporation specifying which local institutions survive, are suspended, and what the centre may extract. \[SOURCE MATERIAL, not canon; self-authored upload with T0/T1/T2 evidence tiers (per research/by_lane/SC_social_contest.md)\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:508` · hook: charter/conquest terms · conf M
  - Venetian mainland: Vicenza kept a council of 500, 150, 40, eight deputati and a consolato; Venice inserted only two rectors. Conquest should produce a negotiation, not a colour change.


### H / HISTORICAL

- **HP-005** `HISTORICAL` (+G) — Augustus 27/23 BC: monarchic power built by accreting nominally separate Senate-granted powers (tribunicia potestas, imperium maius) while performing republican forms. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:118` · hook: Monarch bypass / L/PS (proposed) · conf M
  - Legitimacy framed as auctoritas, not title. Repo hooks: Monarch bypass reachable by accreting grants, each a loggable reversible event; Monarch pays ongoing L/PS upkeep to keep assemblies as ceremonial shells and spikes a penalty if it drops them.

- **HP-019** `HISTORICAL` (+E) — Milan: Gian Galeazzo Visconti bought the ducal title from Emperor Wenceslaus for ~100,000 florins (1395), converting signoria into hereditary duchy. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:282` · hook: ROYAL_COURT_APPOINTMENT (proposed) · conf M
  - Purchased legitimacy from a nominal suzerain. Repo hook: Monarch bypass sells a Duchy-tier title for a lump sum, instantly re-tagging governance_mode and unlocking heredity.

- **HP-023** `HISTORICAL` (+D) — Venetian Serrata 28 Feb 1297: Great Council membership frozen to recent members and descendants, new entry via an annual lottery of ~40; Libro d'Oro formalised 1506. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:334` · hook: governance_mode migration (proposed) · conf H
  - One dated charter act turned an open commune into a closed patriciate. Repo hook: mode migration legislated and observable, entry gate switching from open application to closed lineage plus lottery.

- **HP-046** `HISTORICAL` (+G) — Entry charters: Joyeuse Entree of Brabant 1356 conditioned recognition on sworn confirmation of privileges; coronation charters (Henry I 1100) preceded Magna Carta; towns paid for confirmation. \[FILED 2026-07-08 research, not canon; docket items ED-FA/ED-SE cite it as provenance\] `research/fa_se_historical_precedent_research_v1.md:138` · hook: conquest terms (proposed) · conf M
  - A conqueror who confirms buys cheap legitimacy at the cost of constrained extraction; one who imposes buys full extraction and a resentful base. Siege honors of war versus storm and sack (Magdeburg 1631).

- **HP-104** `HISTORICAL` (+E,G) — Venetian dedizione: subject cities negotiated pacts, keeping statutes, tax exemptions, guild privileges and councils in exchange for loyalty and appellate supremacy; the companion's load-bearing loan for conquest as negotiation. \[PROPOSED 2026-08-28 reference under 0.05, not canon\] `research/valoria_game_precedent_companion_v1_part5.md:104` · hook: charter/conquest terms (proposed) · conf M
  - Companion also flags its own claim as stated more confidently elsewhere than the source supports. Pairs with split command (podesta civil, capitano military).



## I · Disorder and failure modes — 28 entries (CODED 2, INTENT 2, PROPOSED 5, ARCHIVED 2, NOTCODED 4, RESEARCH 3, HISTORICAL 9, GAME 1)


### I / CODED

- **CD-045** `CODED` (+F) — The revolt query: territories at or under a rung that no faction holds (held by none, or by more than one faction, counts as unheld). \[code at world_q.py:2030 uncontrolled (24h P5)\] `engine/season/queries/world_q.py:2030` · hook: uncontrolled; holder_faction_of · conf M
  - The oracle insurgency pipeline was retired; this is its season-native stand-in. Reads holder_faction_of; no petition, vote or unrest accumulation drives it.

- **CD-093** `CODED` (+K) — Bout classifier labels each contest as an arc (ROUT, CLEAR_WIN, NAIL_BITER, REVERSAL, COLLAPSE, DEADLOCK, SPLIT_DECISION) with a turning point and decisive factor. \[kernel, NOT adopted (SC-05, ED-SC-0033); runs only in its own tests; narrative.py shapes\] `systems/social_contest/sim/contest/narrative.py:1` · hook: none (kernel); classify; Chronicle · conf H
  - A legibility and narrative-clarity layer: thresholds NAIL 0.06, CLOSE 0.12, ROUT 0.30 are eyeballed [SEED]. Nothing in engine/season consumes it; the live engine's analogue is the Event stream and the Chronicle channel.


### I / INTENT

- **PR-039** `INTENT` (+G) — GAME inquisition hearing: interrogation with a bench; term_required false with closed floor and bench = authored indefiniteness; interposed office, procedure, document; verdicts withheld; reach body. \[03 E.2 game row 6; ratified as intent\] `proposals/2026-09-05-proceedings-subsystem/03_PARAMETERS.md:632` · hook: arrangement row inquisition; term_required key · conf H
  - AX-6 says nothing permanent without an author: an indefinite hearing is lawful and contestable, and whoever set it can be reached - which is what makes the row playable not a trap. Flagged as an architecture/fiction agreement to check not celebrate.

- **PR-109** `INTENT` (+G) — Contumacy and incapacity are the same state in the design, but in canon and common law defiance of a summons IS the finding; O-14 (18) proposes four degrees of presence (go, send advocate, letter, nothing) plus defying a summons. \[20 F-20 as a finding; whether contumacy was built not checked\] `proposals/2026-09-05-proceedings-subsystem/20_STRESS_TESTS.md:436` · hook: Tenure.term; summons; evade/defy · conf M
  - Needs a summons return day: Tenure.term is now CODED (engine/season/state/carriers.py:107, term: Optional[Term]); F-20 in 20_STRESS_TESTS. Whether contumacy is implemented as a finding was not checked.


### I / PROPOSED

- **CD-100** `PROPOSED` (+D) — Nothing ends a motion today: a below-quorum determine is a refusal retried every round. The design adds a MATTER step that lapses it and witnesses matter.lapsed. \[PROPOSED (2026-10-29), design only, CR-38's design file; HELD BACK from the merge default: its section 12 calls; sec 2 and B-7\] `proposals/2026-10-29-parliament-and-debate/2026-10-29-parliament-and-debate.md:59` · hook: MATTER; matter.lapsed (new); term_required · conf H
  - A re-tabling is a fresh Proposition with no commits (Propositions are immutable). term_required is the unread key that would carry this. Deadlock is therefore invisible in the engine today; the proposal makes lapse the defined end.

- **CD-104** `PROPOSED` (+D) — A carried motion can fail on the declarant's dice: determine on a declared row is still a contested act rolling against the default obstacle after the vote passed. \[PROPOSED (2026-10-29), design only, CR-38's design file; HELD BACK from the merge default: its section 12 calls; sec 6 inherited defect B-10\] `proposals/2026-10-29-parliament-and-debate/2026-10-29-parliament-and-debate.md:137` · hook: determine; contests a proposition · conf H
  - Either the declared arm resolves without the roll or an unlucky declaration is accepted as content. Jordan's call 4. A played session would feel it first.

- **GV-074** `PROPOSED` (+D,G) — PI (Parliament Index, 0-20, start 7) is a meter with bands: Non-functional, Degraded, Standard, Full, Ascendant, Supreme, and 20 triggers Royal Deposition into a succession contest with the Crown excluded. \[PROPOSAL; bands 11-20 marked as new defaults\] `proposals/2026-09-03-governance-corpus-rebuild/annex-b-state-graphs.md:499` · hook: w.PI clock; deposition at 20 · conf M
  - At PI<=2 no Manoeuvre and Crown rules by decree; 3-4 Manoeuvre +2 difficulty; 15-19 No-Confidence needs no Church concurrence. Gains: Manoeuvre +1, Crown Session +1, Legislative Record +1, Ministry posture +1; losses: Emergency Powers -1, Church seizure -1, Coup -3; cap +2/season. A health meter for the assembly's functioning.

- **GV-075** `PROPOSED` (+G,H) — Motion of No Confidence against the Crown: a normal vote with Crown as holder; if passed, the Confessor concurs iff Church regard toward Crown <=-1 or CI>=65; concurrence opens a succession contest with Crown excluded; refusal gives CI +3, MS -2. \[PROPOSAL; concurrence predicate marked new default\] `proposals/2026-09-03-governance-corpus-rebuild/annex-b-state-graphs.md:615` · hook: no_confidence motion; deposition · conf M
  - Royal Deposition separately triggers when PI>=5, Church Mandate>=5, Crown Mandate<=1 and two or more factions hold regard<=-2 toward Crown, or PI=20. Nomination agenda: at Year-End, Hafenmark picks Law, Guilds or Logothetes if a Manoeuvre succeeded and no emergency; Crown confirms at Mandate>=3.

- **PR-078** `PROPOSED` (+J,B) — Silence is priced by the room: under a calling order, being reached and returning nothing raises your own obstacle (base_Ob += PASS_STEP x passes) with no act/Event/write; only counted by the provider's own loop over attendees. Charge only where a lawful act existed and was not taken. \[17 D.9 P9 WOUNDED; 'the one mechanism that survived its attack'; not adopted into 21 PHASE list; needs three fixes\] `proposals/2026-09-05-proceedings-subsystem/17_PLAYABILITY.md:537` · hook: order key; provider loop; PASS_STEP · conf M
  - Fixes: falsifier on order scripted not rank (P-08 unbuildable); carve-out for free/written_only from arrangement data; charge only when candidate set non-empty. Flaw: 'formed no candidate' and 'took none' are the same observation, and passes would be the first outcome-moving quantity reconstructible by nobody. Precedent: Dogs give; Liudprand.


### I / ARCHIVED

- **GV-006** `ARCHIVED` (+G,D) — Parliamentary Stay: any parliamentary faction may, post-vote and post-roll, invoke a Stay that suspends a transfer pending external resolution (treaty, Crown intervention, Scar resolution). \[ARCHIVED-NOT-CANON; Stay cited as social_contest_v30 s10.1 ED-631\] `.designs/systems/factions/reference/parliamentary_transfer_v30.md:106` · hook: stay on enacted outcome · conf M
  - Stay-lift mechanism defined in social_contest_v30 s10.1 (not read here). Handled by sim/personal/parliamentary_stay.py (sim stub path cited, not opened). A procedural suspension device distinct from the vote itself.

- **OP-020** `ARCHIVED` (+B) — Chamber Violence: violence in the contest chamber is an immediate forfeit by the violent party; monster incursion or external catastrophe postpones instead; proceeding resumes next scene if both survive. \[ARCHIVED; ED-897\] `.designs/systems/social_contest/reference/social_contest_v30_infill.md:57` · conf H
  - Renamed from 'Forced Unmask' to avoid name collision. Also at infill: two Rattled marks = socially incapacitated (cannot take part in formal social scenes); a Knot can absorb Face strain at +1 strain per use to the Knot.


### I / NOTCODED

- **CD-070** `NOTCODED` (+D) — A matter docketed before any sitting fires is never called to one: open_case appends a dateless item and determine's docket conjunct admits it with no sitting. \[hole H-163 limit 2 and test_sc01_the_bar.py:1 docstring\] `engine/season/hole_register.yaml:3706` · hook: open_case; determine docket conjunct · conf H
  - Lifting this ordering is a design choice not taken. It means a bench can dispose of a person at any time, sitting or not. determine's quorum and bench still apply.

- **CD-071** `NOTCODED` (+G) — No succession arrangement row and no hold disposal: a rival's petition cannot be docketed and determined over a vacant throne; a judge cannot open a hold on a seat he does not exercise. \[hole H-217 (measured 2026-10-17); owner CR-35\] `engine/season/hole_register.yaml:4646` · hook: determine; hold; succession · conf H
  - Adding hold to disposable kinds made 4 tests red. Vacant throne goes to first valid claim (IN-61). A tribunal can restrain a person (ban, detain, oblige) but cannot award or strip land or office.

- **GV-088** `NOTCODED` (+G,H) — CR-37: the throne may be stripped only by joint concurrence: a Parliamentary vote (determine under parliamentary_debate, monarch as opposing party) minting a resolution, and the Holy See's own revoke through its seat; a revocation basis 'joint_concurrence' with concurring_bodies [Holy See]. \[workplan v10 position CR-37, STATE BUILD; depends on CR-36; M8 corrected by Jordan's 2026-10-26 request\] `workplans/valoria_master_workplan_v10_part4.md:391` · hook: joint_concurrence; resolution; depose closed · conf H
  - No ban opens; the deposed King keeps off_duke_valorsmark until death or release; the heir's claim then executes. Revoking actor must HOLD a live resolution naming seat and holder, minted through a different seat. Motive from Royal Deposition conjunction. Church thus has structural veto over regime change. No computed route until H-80 closes.

- **HP-106** `NOTCODED` (+D,L) — The liberum-veto-style holdout: the report found no unanimity/holdout/veto structure anywhere in the old code; committee and cold-equilibrium were inert sinks where it belonged. \[FILED 2026-07-08 advisory review; old sim/ tree, now retired\] `.audit/2026-07-08-contest-settlement-faction-interface/interface_report_v1.md:308` · conf M
  - Succession by consensus resolved as a two-leader Persuasion-Track contest. Gate C packet (line 354) draws the liberum-veto lesson: maximal individual leverage plus zero uncertainty gives capture, so appraisal reveal should be partial. The Sejm/liberum veto appears only as a passing name here, in the interface report, and in a list at fa_se_historical_precedent_research_v1.md:75,77; no source describes the Sejm's procedure.


### I / RESEARCH

- **CL-050** `RESEARCH` (+C) — Route-forcing creates a dominant strategy: a high-standing player should always rush, complicate and fatigue the body ('make them stupid, then charm them'); the counter is that peripheral change decays, which the doc states but never uses. \[SOURCE MATERIAL self-audit finding A6\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/04_negotiation_and_persuasion.md:484` · conf M
  - Doc 4's own audit says the Floor system should not be written until A6 is answered (line 532). Related N3 vs N5 may be the same receptivity field twice (A9).

- **HP-059** `RESEARCH` (+B) — P17 Clock Consumption (diem dicendo consumere): a speaker spends remaining session time to stop business being reached; each such action uses a slot. \[SOURCE MATERIAL, not canon; self-authored upload with T0/T1/T2 evidence tiers (per research/by_lane/SC_social_contest.md)\] `.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md:391` · conf M
  - Requires sessions to be a scarce container with fixed slots; otherwise obstruction is impossible.

- **OP-086** `RESEARCH` (+G,H) — Parliament may raise a Motion of No Confidence (Influence vs Crown Mandate) that the Confessor concurs with or refuses; concurrence deposes the Crown, refusal strengthens the Church. \[RESEARCH recovered-archive finding (worldbuilding_v30 6.2-6.3, 'New Mechanic - All Modes', no supersession marker)\] `proposals/2026-08-31-pr350-archive-recovery/evidence/LANE_F.md:124` · hook: Constitutional Crisis event; Crown Mandate · conf M
  - Concurrence: Crown Mandate to 1, Stability -3, succession chain. Refusal: Church Influence +3, Thread Tension +2. Church holds structural veto over regime change. Unclosed seam: settlement-level Defy raises national Suspicion with no stated link to this mechanic.


### I / HISTORICAL

- **HP-016** `HISTORICAL` (+F) — Parte Guelfa ammonizione: a chartered party body barred suspected Ghibellines or magnates from office without trial on suspicion alone. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:265` · hook: Standing demotion (proposed) · conf M
  - Repo hook: a faction holding a disqualify-without-trial Directive that bypasses the normal performance-based demotion bridge, a more abusable lever.

- **HP-020** `HISTORICAL` (+H,F) — Golden Ambrosian Republic 1447-50 hired Francesco Sforza, who turned the contract army on the employer, starved Milan, became duke (Lodi 1454). \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:285` · hook: military power_base (proposed) · conf M
  - Repo hook: a hired mercenary faction whose unpaid wages and unclear post-war status flip contractor into usurper when the employer has no armed force of its own.

- **HP-021** `HISTORICAL` (+E) — Genoa: doge (1339) as neutral arbiter with no independent coercive base, repeatedly toppled by alberghi; sovereignty repeatedly handed to foreign protectors; Doria 1528 closed list of 28 alberghi. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:290` · hook: Monarch bypass escape valve (proposed) · conf M
  - Repo hook: a neutral office without enforcement is capturable by faction militia; voluntary subordination to an external tier as a crisis escape valve.

- **HP-026** `HISTORICAL` (+G,J) — Council of Ten (1310 emergency, permanent 1334/1355) with Zonta augmentation; Inquisitori di Stato (1539); Bocche di Leone anonymous denunciation slots; secret proceedings, final verdicts. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/governance_modes.md:346` · hook: none (proposed) · conf M
  - Bypassed the ordinary judiciary for state-security cases. Repo hook: rank sets secession blast-radius; low-rank informer betrayal stays local.

- **HP-033** `HISTORICAL` (+G) — Tiberius Gracchus 133 BC bypassed the Senate to the plebeian assembly, deposed fellow tribune Octavius by mass vote, sought re-election and was clubbed to death. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/conflicts_power_struggles.md:105` · hook: collision-of-stresses (proposed) · conf M
  - Constitutional dubiousness of the lever being fought over. Senate read re-election as kingship: a material land-crisis signal plus an independent interpretive trigger.

- **HP-034** `HISTORICAL` (+D) — Two-signal resonance: revolt or deposition fires only when accumulated material strain meets an independent legitimating trigger; a bare grievance fizzles. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/conflicts_power_struggles.md:26` · hook: collision-of-stresses primitive (proposed) · conf H
  - Examples cited: Janissary revolt plus fatwa, Gracchi, Onin, Venice Agnadello. Repo grounds this on non-MoH precedent only.

- **HP-035** `HISTORICAL` (+H) — Pazzi conspiracy 1478: informal Medici primacy had no office to contest, so rivals went outside the system; channel starvation turns grievance into assassination. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/conflicts_power_struggles.md:257` · hook: emergent friction (proposed) · conf M
  - Also the Ides of March (no legal recall of a dictator perpetuo) and Honno-ji. Repo hook: absent contest channel raises violent-exit probability.

- **HP-036** `HISTORICAL` (+H) — Agnadello 14 May 1509: defeat plus Terraferma cities' prior consent deficit toward Venetian rectors collapsed the mainland empire; Venice's councils survived and recovered it. \[RESEARCH (ED-IN-0064; design hooks are proposals, not ratified)\] `research/governance/conflicts_power_struggles.md:313` · hook: collision-of-stresses (proposed) · conf M
  - Each signal alone survivable; only the collision cascades. Repo hook: military Key plus a separately computed consent-deficit Key.

- **HP-101** `HISTORICAL` (+J) — Day of the Dupes 1630: a private decision to dismiss an advisor is a reversible rumour until ratified; an audience race decides and early public committers are exposed. \[FILED 2026-07-11, PROPOSAL; unverified per SC evaluation\] `research/rise_to_power_roster_system_research_v1.md:467` · hook: none (proposed) · conf L
  - Rewarded variable is speed of access after the vulnerable moment, not accumulated support. Proposed Premature Commitment tag. Companion to Thermidor (denunciation pipeline running out turns the purger on the body, resolved by a procedural vote).


### I / GAME

- **HP-102** `GAME` (+A) — EU4 estates as the canonical ignorable mechanic: tuned so failure is never reached; a mechanism engineered not to fire is indistinguishable from none. \[PROPOSED 2026-08-28 reference under 0.05, not canon\] `research/valoria_game_precedent_companion_v1.md:142` · conf H
  - The same file says Valoria's old parliamentary bridge had the mirror defect, firing every season with a subjectless motion; the bridge file is no longer in the tree (engine/cross_scale and parliamentary_bridge are absent).



## K · Emergent narrative and churn — 121 entries (CODED 16, RATIFIED 8, INTENT 3, PROPOSED 28, ARCHIVED 2, NOTCODED 10, RESEARCH 2, GAME 9, NARRLIT 43)


### K / CODED

- **NL-042** `CODED` (+J,M) — reception: how the bench receives a speaker = sum over each seated member's OWN ledger of the speaker's attributed deeds, weighted by confidence and the member's own projected pursuits; a called bluff erases dominance-route deeds. \[code at engine/season/queries/world_q.py:581-639 (reception) and :641 (proofs)\] `engine/season/queries/world_q.py:581` · hook: world_q.reception, person_q.attributed_deeds; speak/argue contest input · conf H
  - Opened. Bench = judging_set(w, venue). Valence uses person_q.deed_term (existing alignment table, arm 1; H-215 notes the dedicated regard table was never authored). Same room, different bench, different reception. This is the 'one change' of proceedings doc 15 Part C. ED-SC-0040 row: Layer-1 F8 reading dispute, closed as option B re-sourcing from commits (row says code change owed).

- **NL-053** `CODED` (+F,J) — Fan-out is no longer total: the shipped witness arm is all_five channels, so two ledgers can differ (measured 3 differing pairs vs 0 under total at build_world(0)); secrets, rumour and hidden profiles become possible. \[code at engine/season/data/fixtures.py:386 (fan_out_mode='all_five'); rationale :305-345; requirements.yaml R-07 :1317\] `engine/season/data/fixtures.py:386` · hook: fan_out_mode; epistemic.py CHANNEL_PREDICATES · conf H
  - Mechanism 1 of NL-052 now present. Comment records deposits 649 (total) -> 60 (all_five). But rosters.yaml:950 warns only three of five channels can admit anyone in a drivable world (chronicle matches nobody, post_remit needs an obligee). Falsifier: test_r7_two_persons_hold_different_things.

- **NL-054** `CODED` (+F,J) — Attribution and hearsay exist: a paired deed names its doer through the sighting's seen.who; a told copy carries no seen and names nobody; claims source 'told_by' record hearsay with a chain. \[code at engine/season/queries/person_q.py:141-170 (attributed_deeds, deed_term, suffered_deeds) and decision/options.py:1346 (told_by claims)\] `engine/season/queries/person_q.py:141` · hook: person_q.attributed_deeds; Claim.chain/source · conf M
  - Mechanisms 2 and 3 of NL-052 are present in part: 'Aldric said' needs seen.who or a telling chain. Narration proposal measured 1,270 told_by claims of 11,929, only 4 by an actual telling (chain non-empty), 1,266 by public-record channels, so telling-transport is rare in play.

- **NL-055** `CODED` (+M,F) — Convictions move by consequence: at scar threshold 3 the crisis folds, destroys or (not built) restabilises a held affiliation, written once through the gate by an act's outcome; engine rolls nothing. \[code at engine/season/loop/resolve.py:674 (_conviction_crisis) and queries/person_q.py:815; data/fixtures.py:727 scar_weight_shift=0 (shipped control)\] `engine/season/loop/resolve.py:674` · hook: Person.conviction, Person.scar · conf M
  - Mechanism 6 of NL-052. Only the affiliation crisis writes (Person, conviction); RESTABILISE branch is NOT BUILT. The projected-axes shift (scar_weight_shift) ships at 0, the control arm, so scars do not yet bend decision weights by default. Judges can harden only via scarred affiliations.

- **NL-056** `CODED` (+I,F) — Pressure crossing: a person's standing gap crossing a band emits one record; the only consequence is that person's own later choice, via a question about the people who told. \[code at engine/season/loop/matter.py:187 (_standing_crossings) and queries/world_q.py:2786 (standing_crossed)\] `engine/season/loop/matter.py:187` · hook: standing_band_floors; Question source claim_landed · conf H
  - Mechanism 8 of NL-052, built (v9 SC-02 22b step 23). Writes nothing (step falsifier: a crossing must raise a question, not a write). Band floors from fixtures standing_band_floors; empty tuple is the control arm. Gives 'the person who breaks, at somebody, on their own initiative' a carrier.

- **NL-057** `CODED` (+A,M) — A standing ambition (live commit to an OUGHT proposition) raises a 'need' question every season, so a quiet-season person with an ambition still forms a candidate and initiates something. \[code at engine/season/queries/world_q.py:2262 (ambitions), :2811 (questions_for Q4 'need'); thrust register: need scenes 24-28% of scenes\] `engine/season/queries/world_q.py:2285` · hook: questions_for Q4 need; ambitions; goal_referents · conf H
  - Half of mechanism 4 of NL-052: the question fires. Thrust-layer register measures need scenes at 149-174 of 606-642 per seed, goal-Proposition scenes only 7.1-8.5%; narration proposal measured need taken in 51 of 803 deliberations because claim_landed sorts first. Starved by ordering, not absent.

- **NL-063** `CODED` (+J,M) — Regard is computed at read from stored stance + judged deeds + told valence (gains 0.5, [ASSUMPTION]); two hearers regard one doer differently by what each was told and judged. Writes no stance. \[code at engine/season/queries/person_q.py:393 (regard); requirements.yaml R-07 :1317 records a measurement (3270 of 11449 pairs differ beyond stance)\] `engine/season/queries/person_q.py:393` · hook: person_q.regard; options.teller_weight · conf H
  - Memory feeds decision: regard enters choose's stance term and teller_weight. R-07 stays 'partial': feelings/attitudes have only stance as a field; no stance writer reached by a death or witnessed claim in the measured run. Falsifier test_told_by_channel::test_r07_realm_regard_differs_between_hearers_by_claim_not_stance_alone.

- **NL-071** `CODED` (+J) — Instrument chronicle: picks the deepest cross-person chain of acts over a finished log (ties to first logged; walk back by depth-1 antecedent) and prints it root-first with 'answers <n>' lines; writes nothing to the World. \[code at engine/season/harness/chronicle.py:1-60 (instrument; wired into no gate; test_in37_chronicle.py asserts hash/log/writes unchanged)\] `engine/season/harness/chronicle.py:1` · hook: harness/storybar.py read(); CLI python -m engine.season.harness.chronicle · conf H
  - Observer, not a carrier (ED-IN-0225): no arc, story or thread carrier exists; nothing ranked by salience inside the loop. --executed-only variant cuts refused acts. This is the repo's only story-sifting analogue; a pure depth rule, no query language (cf. Felt NL-020).

- **NL-072** `CODED` (+J) — Story-bar: per season, share of acts with another person's act among their antecedents and the distribution of cross-person chain depth, per forcing arm; classes cross > own > world > none. \[code at engine/season/harness/storybar.py:1-60 (M2 instrument, IN-19); reports raw readings, grades nothing, wired into no gate\] `engine/season/harness/storybar.py:1` · hook: SeasonDriver.act_of; harness · conf H
  - Narration doc measured shipped storybar understated cross-person causation (cross 9.5%) vs occasion-restored reading 23.8% (depth max 7), pending IN-50. The only metric of 'drama between persons' in the tree; forcing arms: only 'off' exists, no forcing source built yet (docstring).

- **NL-073** `CODED` (+A,J) — ARC(p,a) reader: an act by p on a thrust, plus two distinct Receipts (one self-field write, one world-field write) both caused by it, with a refusal null; deaths counted apart. \[code at engine/season/harness/arc.py:1-25 (CL-THRUST B0.1, G-28); instrument only, read by nothing in the game\] `engine/season/harness/arc.py:1` · hook: Receipts; harness only · conf H
  - Rosters of self/world (kind, field) pairs exist because every witnessed act deposits a claim, so any Receipt would count moved-and-was-seen as an arc. Arc test gets a shuffled-causes null. Reports, grades nothing, moves no hash.

- **NL-082** `CODED` (+J) — How 50 legacy arcs close, classified blind from their ends_when strings: DECIDER 20, ROLL 9, THRESHOLD 8, NEVER 10, UNCLEAR 3; 19 of 50 forced_by_threshold. \[data read at runtime by engine/season/harness/corpus_run.py:75 (instrument); header: an AGENT CLASSIFICATION OF PROSE, not an execution\] `engine/season/ENDINGS_CLASSIFIED.yaml:1` · hook: harness/corpus_run.py ENDINGS · conf H
  - Independently reproduces the executed A2 core-blocker count of 8. Plan (part6:216) later reports 48 classified arcs: 18 unforced DECIDER/ROLL, 11 forced, 8 THRESHOLD, 9 NEVER, 2 UNCLEAR. An arc ended by 'the vote resolves' (ARC-R18) is DECIDER. Weakest evidence class in the suite.

- **NL-085** `CODED` (+C,M) — argue: on Overwhelming or Success it moves the hearer's Person.pursuits and emits argument.won and pursuit.moved; Partial emits argument.won only; Failure emits argument.lost; refusal argument.refused. \[code at engine/season/verb_table.yaml:131-166 (verb argue) and loop/effects_information.py::_eff_argue; grade assumption\] `engine/season/verb_table.yaml:131` · hook: argue verb; Person.pursuits; argument.* events · conf H
  - A persuasion consequence that ripples: the changed pursuits alter the hearer's later scores. Contest is sigma_leverage via social_contest (interim). Requires the argued thing be an uttered Proposition and hearer 'with' the arguer. Dyadic, not a sitting.

- **NL-086** `CODED` (+B,J) — speak at a docketed matter contests 'a matter' and writes nothing at any degree; it only emits matter.carried / matter.advanced / matter.held / matter.turned (refusal speech.unheard), which witnesses turn into claims. \[code at engine/season/verb_table.yaml:1177-1204 (verb speak); grade assumption\] `engine/season/verb_table.yaml:1177` · hook: speak; matter.* events; docket · conf H
  - A sitting's speech leaves a record only through witnessed events and claims, not a stored result. The turn of a matter is a fact in ledgers: the hook source for later retelling. Stage: SC-01 fired-slot step.

- **NL-087** `CODED` (+A,B) — A fired date puts a sitting before a judge only if his own ledger holds the date.fired claim from the firing tick; hearsay of a firing is not admitted. \[code at engine/season/queries/world_q.py:283-316 (sittings_before) with loop/calendar.py:28 and verb convene (verb_table.yaml:281)\] `engine/season/queries/world_q.py:283` · hook: calendar; date.fired; judging_set · conf H
  - Convening is by calendar: convene writes Date.due_at, CALENDAR fires it, a docket item forms; nothing is decided by the firing. One convene is a standing court (open_slots re-opens). Epistemic gate on convening is itself a hook: absence of a bench member has a cause.

- **NL-090** `CODED` (+F,J) — tell needs the teller to hold a claim and the hearer to be with him; Success/Partial emit news.told and confidence.broken, Failure news.untold. Rumour transport is a verb. \[code at engine/season/verb_table.yaml:1278-1305 (verb tell); grade per row\] `engine/season/verb_table.yaml:1278` · hook: tell verb; Claim.chain; news.* events · conf H
  - Telling is the only transport that makes hearsay (18_FINDINGS.md:486: 'the channel matches nobody. Telling is the only transport'). Narration proposal measured only 11 news.told in a two-season run. Gossip/recap channel that Aylett requires for off-stage events (NL-006).

- **NL-110** `CODED` (+J,A) — R-01: a decision propagates to other persons; R3 cross-person propagation measured 46/46 NPC and 96/97 ARC cases over the 143-case corpus (later superseded in-row to 97/97 ARC, NPC 46/46). \[engine/season/requirements.yaml:199 R-01 'decisions must propagate' status met; the NINE's status strings are DOC-DERIVED but this row cites a measurement with an executable measure:\] `engine/season/requirements.yaml:199` · hook: python -m engine.season.harness.register --requirements; wd_acceptance · conf M
  - R-02 (:545) decisions affect subsequent decisions: met on a printed 43.03% reconvergence at the 2x3 acceptance point (below 96%, so forks reach later deliberations). R-03 (:699) scene-by-scene tick met. These are the executed basis for 'drama ripples'; they say nothing about debate-specific ripple.


### K / RATIFIED

- **NL-031** `RATIFIED` (+A,I) — The world happens to the player and the player happens to the world; every decision must generate churn that seeds continuing or new emergent narrative. Suspect any inert, unreachable or one-directional mechanic. \[Jordan principle per memory note (2026-06-23, 'core design axiom'); not an ED row I opened\] `C:/Users/Jordan/.claude/projects/C--Github-ttrpg/memory/world-player-churn.md:10` · hook: none (design lens over every verb row) · conf H
  - Audit lens: outcome rows with 'cost paid, no effect', actions that can never fire, or world-acts-on-player-only are defects. For debate: a sitting whose result changes nothing the world can react to is inert (cf. NL-047 ABOUT-the-world ruling). Origin: 2026-06-22 faction-action audit.

- **NL-032** `RATIFIED` (+M,D) — Persons differ in risk appetite and in decision horizon: short = this season or next, medium = three to four seasons, long = five or more. Boldness and patience are wanted traits, not excluded. \[Jordan ruling per memory note, 2026-10-29; recorded as ED-IN-0304 per the note (ledger row not opened)\] `C:/Users/Jordan/.claude/projects/C--Github-ttrpg/memory/persons-differ-in-risk-and-horizon.md:8` · hook: decision/choose.py score terms (not yet) · conf H
  - Reverses the earlier 'out' call. Feeds the churn principle: differing appetites generate divergent choices and so divergent votes and offers. Build waits on v10 CR-17 (believed odds weight the alignment term, B10-09).

- **NL-034** `RATIFIED` (+J) — 'All directions' is a general method: trace a mechanic by several routes and perspectives, and name any route with no carrier as a finding. Not NERS-specific. \[Jordan principle per memory note (2026-10-28 correction)\] `C:/Users/Jordan/.claude/projects/C--Github-ttrpg/memory/all-directions-means-routes-and-perspectives.md:11` · conf H
  - Not NERS-specific. Applied first to the emergent-narrative corpus. For a debate system the method asks which route from a sitting's outcome to a later decision, a later telling, or a later vote has no carrier.

- **NL-037** `RATIFIED` (+J,A) — Narrative holonomy: exactly one beat stream; a character's story, household season, faction campaign and world chronicle are projections of it at different scale and focalizer; aggregate-up and distribute-down. \[Header: RATIFIED Jordan 2026-07-05 (PR #78, ED-IN-0011); lives under hidden .audit/; built on the Key substrate RETIRED by ED-IN-0232 (CLAUDE.md s0)\] `.audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md:46` · conf M
  - Churn v2 s1. Candidacy universal, selection scoped. Applied to a parliament: a sitting is one beat that must read coherently as a member's story, a faction paragraph and a chronicle line. No beat-stream carrier exists in engine/season (ED-IN-0225, arcs have no carrier).

- **NL-040** `RATIFIED` (+M,I) — Reflexivity severance: forecast must not steer actors; casting reads realized state only; NPCs anticipate by diegetic heuristics over observable state; fixture F8 tests that forecasting convergence C does not raise realized P(C). \[Ratified design (ED-IN-0011); structural analogue CODED: choose receives no World (requirements.yaml:1317 R-07)\] `.audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md:264` · hook: decision/choose.py (View, no World) · conf M
  - Guards the loop forecast -> actors move toward forecast -> rubber-banding. In code the equivalent is that a person's choice sees only his own ledger View (R-07), so a drama manager cannot leak to agents. Relevant to any debate pacing/steering layer.

- **NL-044** `RATIFIED` (+J,A) — Anti-slop theorem: slop is unbound, consequence-free, unlimited content; forbid it by binding (actors with wants, stakes with history), consequence (one ledger), scarcity (light budget), memory (precedent, callbacks), range (any-seed regression). \[Ratified design (ED-IN-0011); only 4 of 5 checks operative per its own text (ERA instrument unbuilt)\] `.audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md:405` · conf M
  - A five-property checklist for any generated sitting text: does each rendered event name actors-with-wants and cite causes, change the ledger, compete for limited attention, call back to precedent, and vary across seeds. Expressive Range Analysis named as bake gate but unbuilt.

- **NL-045** `RATIFIED` (+J) — Shade semantics: unlit is not deleted; shaded branches keep churning; re-light renders the catch-up as a designed beat, always focalized through a chronicler or a diegetic carrier (returning agent, gossip, document, witness). \[Ratified design (ED-IN-0011); no catch-up renderer in engine/\] `.audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md:254` · conf M
  - 'The letters from Hafenmark, a year unread.' Never placeless present-tense narration of the unwitnessed (P-08). Answers Aylett's off-stage question (NL-006) for a parliament that sat while the player was elsewhere.

- **NL-046** `RATIFIED` (+J) — Render without a runtime LLM: grammar x lexicon with state binding slots; authored bake ~1,200-2,700 units (230-450 under fallback); only ~10-30 distinct prose beats rendered per season; cost O(attention budget), not O(world). \[Ratified design (ED-IN-0011); fork 6 (Certainty gating) needs Jordan; nothing built\] `.audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md:338` · conf M
  - Proven no-LLM lineage cited: CK3 event text, Dwarf Fortress histories, RimWorld tales. Most narrative is behavioural (NPCs acting on diegetic expectations), costing zero prose. Plots project forward as anticipation, never a promise or a meter.


### K / INTENT

- **NL-078** `INTENT` (+A,M) — Jordan licence 2026-08-18: narrative hooks and sequences may be scripted, entire arcs may not. ED-IN-0225: an arc has no carrier. A ladder is a sequence read from the person's own ledger. \[v10 plan decision M20 NARROWED (v10 head Status: RATIFIED on merge, ED-1094, ED-IN-0299); marked [ASSUMPTION; medium; Jordan to correct]\] `workplans/valoria_master_workplan_v10_part6.md:167` · hook: goals.yaml goal_stages (v10); no arc carrier · conf M
  - Quote of licence from proposals/2026-08-18-fieldwork-architecture-and-nonadversarial-play.md:618 (via plan). Sequence/arc boundary is Jordan's line. ED-IN-0225 itself is in an archive fragment I could not retrieve by id; text taken from the plan's quotation.

- **NL-079** `INTENT` (+A,I) — Something that happens without the player: a six-card Tensions deck is the first receiver, read once at build and shipped off; Goldenfurt 28 cards and 11 named cards not receivable; arcs never runtime data. \[v10 second decision round item 2, TAKEN (delegated), [ASSUMPTION; medium; Jordan to correct]\] `workplans/valoria_master_workplan_v10_part6.md:216` · hook: CL-EVENTS; registry/loader (not built) · conf M
  - CL-EVENTS commits: FORCE-WEATHER per territory and the Tensions receiver (B10-18). B6.n draws only from unforced or hooked classes of ENDINGS_CLASSIFIED.yaml. Switch stays off in v10. Jordan's 45 cards = 6 + 28 + 11.

- **NL-081** `INTENT` (+I,G) — T-b: a threshold or hazard may not produce an act or outcome; a band crossing may only raise a Question for a named person (form F5 OCCASION). \[v10 second decision round item 5, TAKEN, [ASSUMPTION; medium]; RF-2 supersedes Jordan's 2026-08-18 endorsement of a guaranteed fire\] `workplans/valoria_master_workplan_v10_part6.md:224` · hook: loop/matter.py crossings; Question · conf M
  - Five lawful forms F1 estimate, F2 own-ledger conjunct, F3 structural conjunct, F4 pool term, F5 occasion. The coup counter's fire and Royal Deposition 'fires' refused as superseded. Eight refusals bind how a drama-by-threshold (crisis, crossing) can be built.


### K / PROPOSED

- **GV-078** `PROPOSED` (+H,F) — Faction emergence from below: Cell > Organisation (2+ settlements) > Movement > National (4+ settlements over 2 provinces) > Hegemon; insurgency pipeline can promote to a parliamentary faction if mean Piety >=3, so new voices enter the assembly without player action. \[PROPOSAL\] `proposals/2026-09-03-governance-corpus-rebuild/annex-b-state-graphs.md:86` · hook: polity status; parliamentary flag · conf H
  - Promoted faction requires L>=3, 2+ provinces, mean Accord>=4 for two seasons. Four dissolution paths: military, sponsor loss, amnesty (contested), persist. Parliamentary status = national and not extra-parliamentary (D-06.01). Churn: assembly membership changes with the simulated world.

- **NL-043** `PROPOSED` (+C,M) — As first specified the proceeding is a flowchart: every obstacle input is mine or printed on the room. Hidden information that enters no outcome is decorative; the fix is an obstacle that depends on what the room holds. \[PROPOSED, held back in full (file Status); Jordan question 2026-09-06 quoted; its Part C remedy is now in code (NL-042)\] `proposals/2026-09-05-proceedings-subsystem/15_WHY_IT_IS_A_GAME.md:18` · hook: world_q.reception (implemented) · conf H
  - Five game conditions: non-computable optimum (inputs hidden AND load-bearing), irreversible commitment before uncertainty resolves (have it: the descent), cost outside the current frame, incommensurable goods, other minds reasoning about you. Anti-solver is also an anti-flat-log requirement.

- **NL-047** `PROPOSED` (+J,A) — Jordan: proceedings must be ABOUT the world and enacted by characters OF the world. Test: what in the world does a game change; why is each person in the room; (added) who learns it happened. \[Jordan ruling 2026-09-06 quoted in a file marked PROPOSED, held back (only README, 21, 04 of the directory were flipped to INTENT by ED-SC-0039)\] `proposals/2026-09-05-proceedings-subsystem/14_THE_WORLD_IN_THE_ROOM.md:239` · hook: disposes (arrangements.yaml), Record/Tenure writes · conf H
  - Forbids a disposal that writes only a Query, stakes internal to the room (points, momentum, debate score), a cast set by the arrangement, a matter with no referent, an outcome nobody can be told of. Answers NERS N attack: proceedings are the only route by which holdings change hands without force.

- **NL-048** `PROPOSED` (+A,J) — Eight nouns reach a proceeding by existing carriers: events->witness->claims, facts as Claims, pressures as Sensation, clocks as Date, issues as Proposition, concerns as Question, demands as petition, impositions as levy/oblige/Tenure. \[PROPOSED, held back (14 Status); carriers cited exist in code per its own table\] `proposals/2026-09-05-proceedings-subsystem/14_THE_WORLD_IN_THE_ROOM.md:123` · hook: questions_for, calendar date.fired, open_case · conf M
  - B.1: a proceeding cannot be raised by a fact; facts raise questions, questions raise candidates, a person must then act (AX-1), so a world where nobody convenes anything has no proceedings however bad things get. Flagged as a play question, not an oversight.

- **NL-049** `PROPOSED` (+J,M) — Belief->decision edge: claim read by belief_contradicts is live and aimed at a namespace, but the witness deposit into that namespace was unbuilt; so no belief reached a choice. Retraction corrected an earlier 'measured-severed' claim. \[PROPOSED (2026-09-05/06); its severance measurement was RETRACTED in the file (:188); corrected state: reader live, write side unbuilt\] `proposals/2026-09-05-proceedings-subsystem/14_THE_WORLD_IN_THE_ROOM.md:177` · hook: decision/options.py belief_contradicts; epistemic.py deposits · conf M
  - Later code: requirements.yaml R-02 (:545) records divergence of later decisions; at the 2x3 acceptance point reconvergence is 942/2189 = 43.03% (below 96%), so a decision does reach later ones (actor arm). The row's earlier 'closed by a theorem / ~4%' reading is superseded in-file.

- **NL-051** `PROPOSED` (+A,J) — A public debate is not a twelfth game but the degenerate case: a speak finding no bench deposits claims into every ledger present and disposes of nothing. \[PROPOSED, held back (14 Status)\] `proposals/2026-09-05-proceedings-subsystem/14_THE_WORLD_IN_THE_ROOM.md:321` · hook: speak verb; claim deposit at witness · conf M
  - Cost admitted: loses the answer to 'why attend a debate'; replacement is 'you attend to put claims into ledgers', worth a scene only when the room holds people whose beliefs matter. Epideictic genre has no ladder and disposes standing only (rejected as a disposal).

- **NL-052** `PROPOSED` (+F,M) — A story rather than a log needs a DIFFERENCE between two ledgers that a third act exploits, and a WANT that makes someone initiate. Eight mechanisms listed; the doc counted six of eight absent. \[PROPOSED, held back (18 Status, 2026-09-06); several of its eight mechanisms have since changed state in code (NL-053..058)\] `proposals/2026-09-05-proceedings-subsystem/18_FINDINGS.md:415` · hook: see NL-053..058 · conf H
  - List: (1) fan-out not total, (2) attribution, (3) told_by from transport, (4) unmet-want term, (5) reception reads ledgers, (6) conviction moves by consequence, (7) summons with a return day, (8) pressure crossings. 'The design documents describe items 2, 3 and 5 as though present; the code disagrees' - true then, stale now.

- **NL-059** `PROPOSED` (+E,B) — What is distinct play in each proceeding variant: negotiation offer ladder, envoy rope, arbitration game-before-the-game, trial advocacy, council hidden profile, embassy seating, appeal depth cap; interrogation, inquisition and council had no distinct play as coded. \[PROPOSED, held back (18, 2026-09-06); 'council hidden profile real only if fan-out is off total' - fan-out is now all_five (NL-053)\] `proposals/2026-09-05-proceedings-subsystem/18_FINDINGS.md:453` · hook: arrangements.yaml rows · conf M
  - Verdict then: three rows no distinct play, two distinct only through transport, trial distinctness is attribution. Parliamentary debate distinct play: which of many to address, no ladder; dissent has no reader (records_dissent, see NL-050). Table is a status snapshot to re-check.

- **NL-064** `PROPOSED` (+J) — Two texts must not be merged: an omniscient instrument chronicle for designers and a focalized journal bounded by one person's claims, the only text a player may read before choosing. \[PROPOSED, held back; merge does not ratify (file header :3); grade paper; one seed two seasons\] `proposals/2026-10-13-narration-mechanisms.md:88` · hook: harness/chronicle.py; person_q explain shape (planned) · conf H
  - Grounds: player coupling (salience-ranked memory reaching one seat), hidden actors (explain has no World param), leaked knowledge (144 date.scheduled claims carry only stratum). who/why printed only per channel supplied_by (rosters.yaml:948-963), read at runtime. NM-W1 and NM-W5.

- **NL-065** `PROPOSED` (+A,J) — Narration can start as an instrument over today's log. First obstacle is candidate formation: 439 of 1,318 acts (33.3%) pick a subject that exists as another kind; 929 of 1,318 acts refused, blocked or null (70.5%). \[PROPOSED (see NL-064); measurements [MEASURED] on one seed, two seasons, tree e6b706d\] `proposals/2026-10-13-narration-mechanisms.md:23` · hook: decision/options.py opening_set; REFUSAL_KINDS data/verbs.py:1073 · conf M
  - Refused: need-triggered injection and scripted beats, argued on five properties (dynamic, capable, flexible, emergent, persistent). Decision round later took the typing dispute as M19 (a), H-156. Measured: 19.45 questions per deliberation, 686 took claim_landed, 51 need, 66 none.

- **NL-066** `PROPOSED` (+A,I) — Explicit not-done list: no storyline object steering the sim, no arc labels in fragments, no forecast/countdown/meter, no stored salience field, no render-to-world write, no per-season occasion emitter, no runtime LLM, no per-entity branches. \[PROPOSED (narration s3.4 ground table); grounds cite ratified texts ED-IN-0011, ED-IN-0225, charter C2, T-b\] `proposals/2026-10-13-narration-mechanisms.md:177` · hook: none (negative constraints) · conf H
  - Salience quote: bound memory by importance and you have built salience-ranked memory, the actor the design exists to refuse (architecture 07_DYNAMICS.md:184-186). Starvation is detected outside the sim as a group-by over storybar rows, never as a trigger.

- **NL-067** `PROPOSED` (+A,J) — Render selection ranked lexicographically, not by a product: executed acts with effect and tellings first, then executed without effect, then refusals with in-world reason, then kind-mismatched attempts; ties by cross-person depth; anti-repetition by (template, binding-class). \[PROPOSED; NM-W1 scheduled B10-19 in workplans/valoria_master_workplan_v10_part12.md:177\] `proposals/2026-10-13-narration-mechanisms.md:228` · hook: harness/chronicle.py (extension) · conf M
  - Precedent test is discrete: same (kind, subject-class, degree). Most of 388 own refusals are probably retries (all 79 migrate refusals are 'path'), so repetition suppression is first-order. Sifting analogue (NL-020..022) done by plain ranking, not statistics.

- **NL-068** `PROPOSED` (+A,I) — Occasion ladder replaces an event deck: rung 1 existing carriers (standing need question, faction-creed ambitions, petitions addressed with 'to', staged Records maturing at MATTER); rung 2 authored boot-time rows; rung 3 per-season emitter refused. \[PROPOSED; NM-W8 scheduled B10-19 (part12:184); rung 3 refused\] `proposals/2026-10-13-narration-mechanisms.md:312` · hook: questions_for; Record.stages term.matured; build_realm boot rows · conf M
  - Rows must not key on seat age (every hold tenure minted with since 0, so cards would fire in one synchronized pulse). Measure need starvation under one_per_source first. Authored content would be Jordan's (forcing-churn s7 decision 3).

- **NL-069** `PROPOSED` (+J,C) — Telling rules: a claim is told with its source and chain; documentary content named from the content:<kind> predicate; staleness told 'as of' its season; two held contradicting claims both told with sources, never reconciled by the render. \[PROPOSED (narration s3.3 epistemic rules)\] `proposals/2026-10-13-narration-mechanisms.md:165` · hook: Claim.when/source/chain; ledger cap · conf M
  - Eviction (ledger cap 200, data/fixtures.py:196) emits no Event, so an evicted antecedent is told from a per-season snapshot or not at all. Gives a recount of a contested sitting each member's own version without a referee.

- **NL-070** `PROPOSED` (+J,M) — Chroniclers: lexicon voice on a person-focalized selection (a), a diegetic chronicler person admitted by the public-record chronicle channel whose W4 record others can read (b), or persons with ledgers (c, engine change). \[PROPOSED; no chronicler exists in engine/season (narration L-3); options (a)-(c) undecided\] `proposals/2026-10-13-narration-mechanisms.md:122` · hook: rosters.yaml chronicle channel; Record kinds · conf M
  - No option recommended; (b) cheapest once W4 content-bearing record kind and W5 journal exist; staleness and partiality come free from the channels the chronicler holds. Fits retelling-as-artifact (Eladhari, NL-014).

- **NL-074** `PROPOSED` (+M,A) — A thrust is a standing OUGHT (an ambition) plus a typed ladder of stages whose completion is a world query; it changes only which question a person answers. No arc object. \[PROPOSED, held back in full (v2); PARTLY RULED via v10 CL-THRUST, M20, M21, ED-IN-0301 (workplans v10 part6)\] `proposals/2026-10-25-thrust-layer/00_THRUST_LAYER_DESIGN.md:16` · hook: goals.yaml; goal_referents; need question · conf H
  - M20 decision: stages only add referents to the person's own need question; closing, successor and deal struck; R3' and stage deadline excluded unless Jordan amends T-c. Ten thrust axes (e.g. political_authority, faction_standing, overthrow_church). Nothing stores 'person is on stage 3'.

- **NL-075** `PROPOSED` (+I,A) — The substrate refuses most acts: 76.2% of 7,402 attempts refused (2 seasons), 76.8% of 16,116 (4 seasons); closers rarely execute. \[PROPOSED, held back; [engine] figures on shipped realm seeds 0-4, scratch probes; B10-02 later landed instruments\] `proposals/2026-10-25-thrust-layer/02_MAJOR_TAKEAWAYS.md:51` · hook: determine, confer; REFUSAL_KINDS · conf M
  - Dependency order: fix instruments and alignment first (T8, T1), then formation (H-156), then death consequences, ladders last. Bears on any debate: a sitting's closing verbs (determine, confer) execute rarely, so drama has no outcome to react to.

- **NL-076** `PROPOSED` (+I,D) — Do not build: lookahead-biased choice (about 270x run time; arc rate minus null -0.08), blind scripts (violate world constraints in 96% of runs), forcing directors (arcs only by dictating a death in 99% of passing runs). \[PROPOSED, held back; [toy] evidence from an abstract world (24 actors, 6 places, 24 seasons), low confidence\] `proposals/2026-10-25-thrust-layer/02_MAJOR_TAKEAWAYS.md:249` · hook: decision/choose.py; loop/matter.py · conf M
  - Engine side: chooser has three terms and no outcome-probability term; no Arc/Story/Plot/Thread class (0 hits); MATTER crossing emits and writes nothing. Argues against a drama manager steering votes or speeches.

- **NL-077** `PROPOSED` (+M,F) — Arc shape needed a goal ladder and a closure form together; a motive layer raised share of events with a lasting motive from 0.43 (bottom-up) to 0.80 (hybrid) in the toy. \[PROPOSED, held back; [toy] arc rate minus shuffled null: bottom-up -0.056, ladder -0.020, ladder + threshold-raised tribunal +0.010 (interval includes 0)\] `proposals/2026-10-25-thrust-layer/02_MAJOR_TAKEAWAYS.md:149` · hook: open_case, determine, oblige, covenant · conf M
  - Closure forms are lawful actor-decided ones: a docket matter a judge determines, a bound peace, a succession, a dice-decided contest. Critics found the first arc test vacuous (T8). Treat as hypotheses; none confirmed in the engine.

- **NL-091** `PROPOSED` (+J,C) — A content-bearing record kind with one key 'says' (a Said), minted by create_record through an own_ledger conjunct, so a document can carry what was said and be read by a second person. \[PROPOSED; NM-W4 scheduled B10-19 (workplans v10 part12:180); held until built with a test\] `proposals/2026-10-13-narration-mechanisms.md:269` · hook: create_record; Record kinds; research verb · conf M
  - Today 112 of 120 Records are 'text' with subject_matter None; 8 content-bearing. Content reaches a second person only when they come to hold the Record; give executed 0 of 24, research 14 of 84. Candidate carrier for a minute-book or speech record (journal artifact, NL-070).

- **NL-092** `PROPOSED` (+J,A) — Scale lines: settlement lines from actorless MATTER events grouped per season; faction lines through faction_q.resolve (faction_sheet Records go stale, giving staleness and contradiction free); cohort lines through the weight>1 key. \[PROPOSED; NM-W7 scheduled B10-19 (part12:183)\] `proposals/2026-10-13-narration-mechanisms.md:304` · hook: loop/matter.py; faction_q.resolve; Person.weight · conf M
  - Vertical rule proposed by the writer: a person's act renders on the person's page and is never folded into a settlement aggregate; settlement lines carry actorless events only. NERS found no prior rule for when a person beat yields to an aggregate. Gaps named: march field outcome untested (8 declared, 0 field.*).

- **NL-093** `PROPOSED` (+J,M) — The client reads a per-person projection (that person's view, own claims, events witnessed), never a World, and renders the season as the character's journal of belief; a falsely held claim appears as held, not corrected. \[PROPOSED; play-surface S-2/S-3 in proposals/2026-09-30-character-and-play-surface/03_play_surface.md:76-77 (PROPOSED, design-only)\] `proposals/2026-10-13-narration-mechanisms.md:114` · hook: query projection (planned); harness/play_surface.py · conf M
  - Test: the projection for p contains no claim p does not hold (plant a claim in another ledger). Narration doc cites PC-06 as ratified intent; I opened only the play-surface file, which is PROPOSED. Defines what a player sees of a parliament they did not attend.

- **NL-111** `PROPOSED` (+A,D) — With attribution, told_by, non-total fan-out and the unmet-want term, twelve characters already generate first-order drama: the wrong person blamed, the want pursued into the wrong room, the rumour believed by the bench. \[PROPOSED, held back (18); claim that items 1-4 'cost one roster member, one deposit line, one sweep arm and one score term'\] `proposals/2026-09-05-proceedings-subsystem/18_FINDINGS.md:429` · hook: fan_out_mode; told_by; need question · conf M
  - Items 1-3 are now present in code (NL-053/054); item 4 missing (NL-058). Whether the first-order drama in fact appears has not been measured in a sitting; chronicle/storybar exist to look (NL-071/072). Build order step 5: author the speech-kind roster (still absent).

- **OP-051** `PROPOSED` (+D) — Genre-loop audit of social contest against dialogue/court RPGs (Disco Elysium, Griftlands, BG3, Kingdom Come, Ace Attorney, Suzerain): ten play opportunities graded AFFORDED/PARTLY/ABSENT with run evidence per seed. \[PROPOSED (grade paper, nothing executes); lane IN; ED-1094 loud exception, held back for Jordan\] `proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-05-social-contest.md:22` · hook: verbs tell, argue, petition, carry, speak, determine · conf H
  - Findings: tell runs; argue never executes in computed play (every computed argue refused on exists:Proposition); petition runs (14/7/11), carry tests-only; speak runs but writes nothing (seed 0: three Failures); determine runs at seed 1 only (one Partial); win-a-chamber ABSENT in the season; deceive ABSENT. 'Build a case' and 'plead and lose forward' are the emptiest.

- **OP-056** `PROPOSED` (+C) — agon_harness is the repo's one human-played social contest: the player plays Side A of a named proceeding (default formal_contest, 3 exchanges) against a kernel policy. \[PROPOSED description; the human-played harness is oracle only\] `proposals/2026-10-22-system-description/2026-10-22-system-description-06-t05-social-contest.md:8` · hook: agon_harness.py (tests-only) · conf H
  - Choosing a move kind each exchange then a Style (4) and Appeal (3), with the tracker printed after each exchange. About 9 prompts over 3 exchanges; verdict varies because the harness does not seed random. Imported by no .py file, so the season cannot reach it. Gives the closest picture of a player-facing exchange loop in the repo.

- **OP-072** `PROPOSED` (+H,I) — The Baralta Crown Claim composes without a script: a 5-article Crown Succession Contest where the Church's consent is custody-held. \[PROPOSED\] `proposals/2026-08-29-valoria-from-scratch/08_argument.md:521` · hook: Crown Succession Contest; record custody · conf H
  - So if the Church's own succession is contested no ground reaches G4 and the sitting closes CARRIED-WITHOUT-FORCE, leaving a record, F2 hazards and a heavier pattern. Altonia destroyed records so descent grounds bottom out at G0 for all. A consecration crisis emerges from two contested successions meeting article 3; nothing authored.

- **OP-073** `PROPOSED` (+C,M) — NPCs argue from what they believe: case assembly ranks the ledger by recency x confidence x relevance x stance weight (motivated reasoning for free). \[PROPOSED\] `proposals/2026-08-29-valoria-from-scratch/08_argument.md:543` · hook: choose(person, view); salience budget K · conf H
  - The opening rung is picked by believed gap in decisive grade, and a planted false claim sends an NPC to a doomed rung. Manoeuvre priority list (strike provenance, press on record collision, plead, descend, yield, press weakest). Planting a claim that the witness is dead is a complete political operation.

- **OP-109** `PROPOSED` (+H,I) — Measured emergent state in the governance run: the King (p_npc_020) dies in the first season (tick 0) in all three seeds. \[PROPOSED description; measurements from an uncommitted round-3 probe at 51d7b05\] `proposals/2026-10-22-system-description/2026-10-22-system-description-09-t08-settlements-governance-economy.md:107` · hook: off_king; off_duke_valorsmark; confer · conf M
  - His and the Duke of Valorsmark's seats are null-conferral and vacant from tick 0 and can never refill; 8, 7 and 10 seats are vacated by season 2 and the only refill is a self-conferral. With the Duke's seat vacant no seat can revoke.


### K / ARCHIVED

- **GV-103** `ARCHIVED` (+F,A) — Two-stroke churn: the world always acts on the player (mandatory Directive, deck draws at least one card each season driven by pressure Pi) and the player's every verb emits a world-delta that conditions next season's draw; a Pi homeostat keeps settlements in a dramatic band. \[ARCHIVED; PROPOSAL 2026-06-22 (settlement churn engine)\] `.designs/systems/settlements/reference/governance_play_redesign_v1.md:276` · hook: event deck; Pi homeostat; NPC ambition engine · conf H
  - Deck draws 1+floor(Pi/3) cards; families Petition, Friction, Opportunity, Crisis, Intrigue, Ambition, Thread; ignored petitions escalate to crises; NPC ambitions (e.g. a magistrate seeking a parliamentary seat) act without the player and offer alliances. A solved settlement offers rather than threatens.

- **OP-012** `ARCHIVED` (+A,I) — Chain Contests: a Compromise (track 4-6) defers tension into a next-season Scene Slate entry whose contest starts at the prior final track position, carrying Scars and Dispositions. \[ARCHIVED; ED-582/ED-896\] `.designs/systems/social_contest/reference/social_contest_v30.md:376` · hook: Scene Slate (player_agency 4.2 per doc) · conf H
  - Two consecutive zero-movement exchanges = Deadlock (third ends as Compromise); max chain length 3, after which a permanent cold equilibrium freezes Disposition and bars the topic for 4 seasons. Per-exchange resistance erosion makes the old Deadlock resistance drop redundant.


### K / NOTCODED

- **NL-033** `NOTCODED` (+M,D) — The chooser's score has exactly three terms (pursuit, stance, urgency); there is no risk term and no time-horizon term, so persons cannot differ in boldness or patience at HEAD. \[code at engine/season/decision/choose.py:130-146 (score_terms)\] `engine/season/decision/choose.py:130` · hook: decision/choose.py::score_terms · conf H
  - Opened score_terms: returns (damp*pursuit sum, stance_term, urgency); urgency is identical for every candidate. requirements.yaml R-08 (:1381) adds that ties break alphabetically by verb, so no inclination breaks a tie. Thrust takeaways (02_MAJOR_TAKEAWAYS.md:249 area) say no term reads an outcome probability.

- **NL-038** `NOTCODED` (+A,I) — Forward probability field: each Accounting computes stake_horizon and convergence_candidate by analytic Layer A plus a seeded ensemble Layer B; forecast objects are actor-invisible and feed render depth only. \[Ratified design (ED-IN-0011); grep of engine/ and modules/ for stake_horizon, forecast_mass, foreclosure_countdown, Light Function returns zero files\] `.audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md:112` · hook: none (absent) · conf M
  - Unbuilt: no forecast, horizon or countdown carrier. The design itself gates Layer B on ~19 stubs, event deck, scene-EV flag; 'M1 ships Layer A alone'. Narration proposal s3.4 (:177) separately refuses 'a forecast, countdown or meter'. Mismatch to flag: ratified v2 vs proposed refusal.

- **NL-039** `NOTCODED` (+J,A) — Light Function: pruning is authorship. It rations among candidates the churn produced, never injects content or shapes resolution; scored by meaningfulness x forecast mass x imminence x inertia; four coherence invariants. \[Ratified design (ED-IN-0011, fork-8 default); no Light Function in engine/ (grep zero); nearest code is the outside-the-sim observer harness/chronicle.py\] `.audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md:190` · hook: none (absent) · conf M
  - Invariants: proximate causal connectivity, light-inertia with anti-strobe floor, player-rooting, liveness (a lit stake may be deferred but not silently foreclosed). Weight set is 'Jordan's narrative voice' as versioned data. Narration proposal (2026-10-13 s3.4) refuses a stored salience field inside the sim.

- **NL-041** `NOTCODED` (+J,C) — Claim grammar: a parliamentary argument is a typed claim over ledger objects; evidence weight from witness count, chain strength, recency, asserter standing; bluster for unbound claims; citable precedent store; commitment store exposing hypocrisy. \[Ratified design (ED-IN-0011) as a REQUIREMENTS INPUT; its own text says four contest sub-systems 'none of which exist today'; grep for bluster/commitment store/precedent store finds no engine code\] `.audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md:286` · hook: social_contest sigma input (absent); world_q.proofs partial · conf M
  - Proposes evidence-weight delta-sigma family, bluster move class, precedent store with Recall rewire, commitment store. Stasis grounds FACT/DEFINITION/QUALITY/JURISDICTION are the SC lane's vocabulary. Partly succeeded by world_q.reception/proofs (NL-043). Key-based text, Keys retired.

- **NL-050** `NOTCODED` (+J,G) — Announcing a binding decision to the world: arrangements declare disposal_reach (room/body/realm/settlement) and records_dissent, validated at load, but no loop code consumes them. \[code at engine/season/data/arrangements.py:75,200-228 loads disposal_reach and records_dissent; grep finds no reader outside the loader and tests\] `engine/season/arrangements.yaml:135` · hook: arrangements.yaml disposal_reach; witness channel 'chronicle' · conf M
  - Doc 14 E.1a says disposal_reach 'closes' who-learns-it-happened; at HEAD only the registry value and a loader test exist. rosters.yaml:963 states the chronicle (public-record) channel 'matches nobody' in a drivable world. So a parliament's decision reaching the realm is registry-only.

- **NL-058** `NOTCODED` (+M,A) — The unmet-want term (direction of initiation) is absent: the need question fires but nothing scores a person toward an unmet want or damps it with a habituation clause. \[Design O-3 (PROPOSED, 18_FINDINGS); grep for unmet_want/unmet-want/habituation in engine/season finds nothing\] `proposals/2026-09-05-proceedings-subsystem/18_FINDINGS.md:423` · hook: decision/choose.py; questions_for ordering (attention_key) · conf M
  - Choose score terms are pursuit, stance, urgency only (NL-033). Narration W8 and thrust-layer R3' propose attention ordering instead; M20/M21 excluded R3' (stage deadline) at the default. Open: who attends first when claim_landed and need compete.

- **NL-080** `NOTCODED` (+I,A) — Exogenous drama is off: the season's yield factor is the bare constant unless season_factor_draw is set; forcing-churn found no drought, calamity or empire anywhere in the code, so no outside pressure reaches a sitting by default. \[code at engine/season/loop/matter.py:453-455 ('season_factor_draw empty (the shipped control)'); proposals/2026-10-04-forcing-churn-and-the-story-bar.md:59-67 (RATIFIED AS INTENT, ED-IN-0287)\] `engine/season/loop/matter.py:453` · hook: season_factor_draw; fixtures.season_factor · conf M
  - Forcing-churn lists nine intents (weather, empire, Calamity, Schoenland outside; ageing; four internal). Plan schedules hunger and now FORCE-WEATHER (CL-EVENTS commit 1, B10-05). Without outside forcing a legislature has no crisis to convene on unless an act makes one.

- **NL-083** `NOTCODED` (+I,G) — No ending is shown reachable in computed play: the vocabulary (peninsular_sovereignty, theocracy) and the reporting step exist, but seed 0 two seasons reports endings == [] and no verb opens a hold on any territory. \[hole H-176 (grade absent) in engine/season/hole_register.yaml; endings_reached Query built (world_q.py:2084), rosters.yaml:2564 endings rows\] `engine/season/hole_register.yaml:3968` · hook: world_q.endings_reached; SeasonDriver.season endings · conf H
  - A realm cannot END as opposed to run out of seasons. Plan v10 item 4 (part6:~232) reschedules purview-licensed seizure to make peninsular_sovereignty reachable. Relevant: arc/ending machinery cannot yet give a legislature a terminal stake.

- **NL-084** `NOTCODED` (+M,C) — Non-rational choice does not exist: the chooser takes the top-ranked candidate deterministically (ties alphabetical by verb) and only 2-7 of 22 candidates carry a nonzero conviction score; persons never decline the optimum. \[requirements.yaml R-08 (status partial); status strings are DOC-DERIVED for THE NINE (CLAUDE.md s0.2)\] `engine/season/requirements.yaml:1381` · hook: decision/choose.py make_chooser · conf H
  - Non-omniscience holds structurally (R-07). R-06 (characters robustly built) and R-07 (memories, attitudes) are partial. A debate where every member plays the argmax of a thin score produces uniform votes, not hooks. Related: NL-033.

- **PR-085** `NOTCODED` (+A) — Emergent narrative: what makes a story rather than a log is a DIFFERENCE between two ledgers that a third person's act exploits plus a WANT that makes someone initiate. Eight mechanisms listed (fan-out not total, attribution, told_by transport, unmet-want, reception reads ledgers, conviction moves, summons return day, pressure crossings); six of eight did not exist at writing. \[18 PART I per doc (code not opened by me); 21 PHASE 1 step 2 (fan-out) executed since\] `proposals/2026-09-05-proceedings-subsystem/18_FINDINGS.md:407` · hook: fan-out; deposit; Question sources · conf M
  - Items 1-4 cost one roster member, one deposit line, one sweep arm, one score term and yield first-order drama (wrong person blamed, want pursued into wrong room, rumour believed by bench). Precedent failure modes: undifferentiated NPCs, memory that never surfaces (live), cosmetic memory (true), legibility collapse at scale (unaddressed; Dwarf Fortress), no causal chain (avoided), escalation with no terminus (avoided).


### K / RESEARCH

- **OP-085** `RESEARCH` (+H,I) — Finding: the mechanics that make governance feel alive and generate emergent narrative are intermediate branch points (3-season Occupation window resist/cede/recapture, 3-phase treaty negotiation positioning/concession/ratification. \[RESEARCH recovered-archive finding F-A-14 (PR #350), single source\] `proposals/2026-08-31-pr350-archive-recovery/evidence/LANE_A.md:115` · hook: faction_layer sections 2, 3.3, 5 (old) · conf M
  - Ten parliamentary motion types) and every implementation generation skipped them for terminal state transitions. Ten motion types named: Censure, Embargo, Blockade, Outlawry, Subsidy and others. Two irreconciled parliamentary vote models: Mandate-weighted vote vs Persuasion-Track dice contest. In the current suite review COMPARE_1: venue/docket/Motion generate the form, vote = judging set at a venue under a decision rule.

- **OP-094** `RESEARCH` (+C,M) — Player-facing exchange flow with the principle that every number the resolver uses is visible before commitment: a framing screen, then per exchange Appraise, four Style cards, a named interaction type, two persistent bars. \[RESEARCH draft working document 2026-07-01 (seed for Stage 6 Player Interaction Model); not canon\] `.audit/2026-07-01-contest-player-interaction/player_interaction_walkthrough_v1.md:1` · hook: Contest Framing screen; Persuasion Track meter · conf H
  - Framing screen: venue, adjudicator, pool, stakes both ways, track and bands, banked Appraise hints. Interaction types named: Direct Clash, Mutual Reinforcement, Talking Past Each Other, Deadlocked. Resolution screen enumerates every consequence; Scar cue kept subtle.


### K / GAME

- **NL-060** `GAME` (+M,F) — Ranked shared mechanisms across CK, DF, RimWorld, Nemesis, Qud, KoDP: typed persistent relationship records; memory that gates eligibility; threshold escalation with shared causes; identity-embedded memory; computed utility vs authored branch selection. \[REFERENCE (relay stage G, sonnet, external material, tabletop entries unverified); no design decision\] `proposals/2026-09-05-proceedings-subsystem/relay/G_EMERGENCE_PRECEDENT.md:113` · conf M
  - Rank 2 'memory that gates ELIGIBILITY, not just flavor' is called most load-bearing. CK3 opinion is a stack of named modifiers with decay; hooks are single-use or persistent. Correlated independent thresholds read as an authored uprising (many vassals joining one faction).

- **NL-061** `GAME` (+I,J) — Failure modes of shipped emergence systems: undifferentiated NPCs, memory that never surfaces, decorrelated events, escalation with no terminus, legibility collapse at scale, cosmetic memory, authored branches mistaken for simulation. \[REFERENCE (relay G)\] `proposals/2026-09-05-proceedings-subsystem/relay/G_EMERGENCE_PRECEDENT.md:125` · conf M
  - 18_FINDINGS.md:438 scores this design: memory never surfaces = live risk (RimWorld's exact failure); cosmetic memory currently true; legibility collapse unaddressed ('nothing here curates'); escalation terminus and causal chain avoided by construction.

- **NL-062** `GAME` (+J,M) — The single mechanism that keeps retained memory from sitting inert is coupling the read to a specific decision-evaluation point (scheme availability, encounter scheduler, scene gate), not an ambient scan; RimWorld surfaces memory only into mood. \[REFERENCE (relay G); finding reframes P-42 per the relay header\] `proposals/2026-09-05-proceedings-subsystem/relay/G_EMERGENCE_PRECEDENT.md:137` · hook: person_q.regard; choose score · conf M
  - Contrast: CK hooks appear in the scheme panel; Nemesis schedules a vendetta orc's reappearance; KoDP/Pentiment flags are wired to known later scenes. Pentiment/Qud bounded by authored content. Rule for a parliament: a recorded defeat must be read inside a later vote or speech decision.

- **NL-088** `GAME` (+J,M) — Prom Week / Comme il Faut negative lesson: thousands of small summed weights give diffuse causality, so no single legible reason survives for any outcome; the suite calls Valoria's convictions matrix 'a smaller Prom Week'. \[unratified comparative analysis (suite-05 Status); external claims tagged by evidence grade; its Key-substrate proposals are retired\] `proposals/2026-08-23-suite-05-precedent-and-proposals.md:43` · hook: conviction axes; choose score · conf M
  - Prescription: contingent unlocking (scripted hooks that gate content) rather than more summed axes. Also: Talk of the Town belief and fallibility; per-character sifting patterns bias interpretation; salience-based storylets. Research dir marks Comme il Faut/Ensemble as named-not-read (08_not_read.md:51).

- **NL-089** `GAME` (+M,F) — Primitives P33 disposition rewrite from experience (events rewrite the weights that drive later choices) and P38 state-keyed director (the game picks the next threat or story from current state, scaling or suppressing). \[FILED reference, tier 3 (suite README Status); cross-reading of about 70 games, tags carried per claim\] `research/game_precedent_suite/THROUGHLINES.md:49` · conf M
  - Both tied to Valoria capability ids (L1 L4 M3 for P33; L4 L5 M2 for P38). Suite README: 866 disposition rows, none passes the five-step test alone; LACKS rows are reference only. Games with a political/narrative tutorial: KoDP and Six Ages (T16), Nemesis and Pax Pamir (T15), Griftlands and Disco Elysium (T05).

- **NL-094** `GAME` (+J,F) — Nemesis system: unlimited per-orc memory while the orc lives, evicted by death; the strongest active-surfacing design - the system schedules a nemesis orc to reappear in a relevant encounter instead of leaving recurrence to chance. \[REFERENCE (relay G, external, sonnet)\] `proposals/2026-09-05-proceedings-subsystem/relay/G_EMERGENCE_PRECEDENT.md:73` · conf M
  - Contrast with RimWorld's ambient mood sum (memory expires before it matters). Scars/names/taunts embed memory on the entity itself, costing no query. Applied to a legislature: a wronged member scheduled to reappear on the relevant motion.

- **NL-095** `GAME` (+M,D) — King of Dragon Pass: seven named council seats hold characters with personality and cult; advice only fires if a council member actually worships that god; rare bonus interjections prioritized when 2-3 members share a trait. \[REFERENCE (relay G, external); flagged as mechanically shallowest system in the set\] `proposals/2026-09-05-proceedings-subsystem/relay/G_EMERGENCE_PRECEDENT.md:83` · conf M
  - Advisors gate and flavour a fixed pool of pre-written lines: authored selection gated by simulated seat composition, not independent reasoning. Memorable by naming and recurrence. The relay flags it leans almost entirely on authored branching, least on emergent mechanism.

- **NL-096** `GAME` (+F,M) — Crusader Kings: opinion is a stack of named, decaying modifiers; typed hooks and secrets; the AI is a utility scorer over traits x opinion x stress x hooks. \[REFERENCE (relay G, external)\] `proposals/2026-09-05-proceedings-subsystem/relay/G_EMERGENCE_PRECEDENT.md:31` · hook: person_q.regard (analogue) · conf M
  - Memorable events upgrade a decaying modifier into a durable flag or create a secret whose discovery is a future event. The scheme panel shows only the causally relevant subset of the stack at the decision. Escalation: many vassals crossing one low-opinion threshold join a faction together.

- **PR-091** `GAME` (+M) — Burning Wheel: three concrete Beliefs and three Instincts per character; the GM is obliged to challenge Beliefs and advancement currency (Artha) is paid for testing a Belief - a human-run utility function. Ars Magica: troupe play plus abstracted seasons let decades of unplayed history accumulate (covenant feuds, Tribunal politics). \[relay G, lower confidence (tabletop entries not freshly verified)\] `proposals/2026-09-05-proceedings-subsystem/relay/G_EMERGENCE_PRECEDENT.md:105` · conf L
  - Belief->test->revision is the story record; Instinct as IF-trigger-THEN-behaviour is a guaranteed-surfacing format. Ars Magica's mechanism is long unplayed time-skips resolved by light systems under a consistent shared setting.


### K / NARRLIT

- **NL-001** `NARRLIT` (+D,C) — Emergence (few rules, large variation, strategies) versus progression (serial designer-delivered challenges); Juul places storytelling ambition in progression, not emergence. \[FILED reference, tier-3 research (00_README Status); T04 Juul 2002, P (full)\] `research/emergent_narrative_literature/01_foundations_narrative_vs_play.md:13` · conf H
  - Test T04.Q1: name the walkthrough vs strategy guide for story-bearing content. A sitting whose only reachable outcomes follow one authored order is progression dressed as emergence. Test T04.Q4: two sessions converging on one shape because of the goal = dominant-strategy collapse. Asks of a debate system: which outcomes derive from rules vs scripted beats.

- **NL-002** `NARRLIT` (+J) — A retelling of a play session keeps existents and events but loses the dynamic system; detailed recounts of moves are dull. Games run in present tense, narrative needs a determined past. \[FILED reference; T06 Juul 2001, P (full)\] `research/emergent_narrative_literature/01_foundations_narrative_vs_play.md:46` · conf H
  - Test T06.Q1: does the retelling say what is lost, or pose as the experience? Test T06.Q2: at the moment the player can act, is any story element presented as already fixed? Bears on a minutes/record of a debate: it is a retelling, valid only after the player cannot act. Corrected claim: Juul says nothing about chronicle prose.

- **NL-003** `NARRLIT` (+A) — The Aleph myth: story fragments cannot be freely permuted because they are bound by presupposition, causality and temporal order; a reader assembles one picture over many sessions. \[FILED reference; T07 M.-L. Ryan 2001, P (full)\] `research/emergent_narrative_literature/01_foundations_narrative_vs_play.md:77` · conf H
  - Apparatus B5 (T07.Q2): can two world states that follow one choice be reconciled coherently? Warns against an agenda/event deck of modular fragments that yields permutations without coherence. Holodeck myth: first-person tragic plots are undesirable, so playable characters drift to flat problem-solvers.

- **NL-004** `NARRLIT` (+J) — Four narrative-architecture modes: evoked, enacted, embedded, emergent. Designers are narrative architects; spaces hold narrative possibility rather than stories. \[FILED reference; T05 Jenkins 2004, P (full)\] `research/emergent_narrative_literature/01_foundations_narrative_vs_play.md:105` · conf H
  - Apparatus A1/C6/H5: for each intended story say which mode carries it; an emergent mode needs conflicting drives, legible objects and consequence traces (T05.Q3, T05.Q4). Debate application: a chamber that leaves visible traces (recorded defeats, broken oaths) is an embedded/indexical carrier.

- **NL-005** `NARRLIT` (+F,M) — Build characters bottom-up from drives and behaviours so plot-level narrative emerges from their interaction; no pre-given plot. Specify characters, relationships, conflicting aims, constraints. \[FILED reference; T01 Aylett 1999, P (full)\] `research/emergent_narrative_literature/01_foundations_narrative_vs_play.md:137` · conf H
  - Needs enough dynamic events outside characters' control and a rich behaviour set; paper itself says narrative may fail to emerge and no rate is measured (T01.Q2: log the rate of recognisable arcs). Football/improvisation analogies. Maps to a parliament of persons with conflicting interests and exogenous crises.

- **NL-006** `NARRLIT` (+J,M) — Social presence: persistent, remembering agents that reward and penalise the user's role behaviour; no restart; off-stage events reach the user by gossip or recap; storification is per-viewer. \[FILED reference; T11 Aylett 2000, P (full)\] `research/emergent_narrative_literature/02_interactive_drama_and_agency.md:14` · conf H
  - Tests T11.Q1-Q4 (apparatus H1-H3): what story state survives undo/reload; viewpoint named per telling; off-stage events both simulated and reported; NPCs change later behaviour toward the user. Direct question for an assembly: do members remember how the player voted and spoke.

- **NL-007** `NARRLIT` (+I,B) — Tabletop GM as a real-time director: places five encounter types (descriptive, social, information-gathering, problem-solving, combat), intervenes on stall, unexpected branch, role misread, skipped content; only part of the GM role is computable. \[FILED reference; T12 Louchart & Aylett 2003, P (full)\] `research/emergent_narrative_literature/02_interactive_drama_and_agency.md:47` · conf H
  - Signs of impasse are easy to categorise; sensing and acting on player satisfaction is much harder; GM leans on out-of-character talk. Base is ONE GM (McBriar), no build. Apparatus F1/F2 (T12.Q1-Q4): name the intervention types and triggers; say which GM functions are dropped. Relevant: no-GM engine must chair, call, and break deadlocks.

- **NL-008** `NARRLIT` (+A,I) — Facade drama manager sequences author-annotated beats (preconditions, effects on story state) toward a target Aristotelian tension arc; weighted random draw among highest-priority beats scored by slope-mismatch to the arc. \[FILED reference; T03a Mateas & Stern 2003, P (full)\] `research/emergent_narrative_literature/02_interactive_drama_and_agency.md:78` · conf H
  - Score = 1/e^(slope mismatch) times weight. Authors admit architecture not generator, heavy hand authoring. Tests F3/F4: explicit tension variable, and an alarm when no beat qualifies (empty candidate set or growing error). A debate-pacing analogue: agenda items as beats with tension effects.

- **NL-009** `NARRLIT` (+C) — Local agency (immediate visible reaction within a beat) versus global agency (interaction history shaping later beats); Facade bought local agency at the expense of global, 27 beats, ~25% of content seen per run. \[FILED reference; T03a/T03b Mateas & Stern, P (full)\] `research/emergent_narrative_literature/02_interactive_drama_and_agency.md:83` · conf H
  - Test G4 (T03b.Q2, T03a.Q3): share of sampled player acts that get a specific immediate response, a generic one, or none; do acts shape the arc as well as the moment. Player interaction recast as abstract social games scored by hidden numeric state and expressed in performance (02:109) - structurally a persuasion contest.

- **NL-010** `NARRLIT` (+C) — Agency occurs when the actions a player wants are among the actions the computational model supports (material affordances) and the story gives reasons to prefer them (formal constraints). \[FILED reference; T08 Wardrip-Fruin et al. 2009 and T02 Mateas 2001, P (full)\] `research/emergent_narrative_literature/02_interactive_drama_and_agency.md:141` · conf H
  - Apparatus G1-G3: at each decision point list what the world affords and what reasons the story gives; does the surface correspond to something in the model; does a failed plan leave something to do. A speech or vote verb with no model behind it is false agency.

- **NL-012** `NARRLIT` (+I) — Experience manager balances story coherence against agency, projecting trajectories and intervening through non-player characters; space organised by authorial intent, character autonomy, player modelling. \[FILED reference; E16 Riedl & Bulitko 2013, P (full)\] `research/emergent_narrative_literature/02_interactive_drama_and_agency.md:201` · conf H
  - Apparatus F6: what happens when the planned continuation is made impossible (boundary problem), and is the criterion for a good trajectory written down. Claim that AI widens expressive range without reducing agency is asserted not tested.

- **NL-013** `NARRLIT` (+J) — Tale-Spin effect: the most interesting operations of a simulation (planning, inference, lying) are almost never visible in its output; a simulation of human behaviour is an authored fiction. \[FILED reference; T13 Wardrip-Fruin 2008, P (full)\] `research/emergent_narrative_literature/02_interactive_drama_and_agency.md:231` · conf H
  - Apparatus E1-E4: what fraction of significant internal events reach the player; Eliza test (trace the three most impressive outputs); every depicted trait must correspond to an input of the decision process. Pointed at a deliberation model: hidden belief updates the player never sees are overbuild.

- **NL-014** `NARRLIT` (+J) — Players' re-tellings form a fourth narrative layer above architecture, design and discourse; occurrence of retellings is a blunt indicator of design success and an instrument for critique. \[FILED reference; E01 Eladhari 2018, P (full)\] `research/emergent_narrative_literature/03_retelling_and_the_concordia_cluster.md:13` · conf H
  - Apparatus L2/L3: control retelling frequency for community size; locate each retold event in code, story or discourse layer; D6 asks whether the system itself retells faithfully with nameable viewpoint. Argues a system's output is judged by what players choose to tell.

- **NL-015** `NARRLIT` — A significant subset of retellings are critical, mocking incoherent output; retelling volume is not a marker of quality. Classify retellings by stance. \[FILED reference; E02 Sych 2020, P (full); the 2023 thesis is UNREAD (08_not_read.md:17)\] `research/emergent_narrative_literature/03_retelling_and_the_concordia_cluster.md:45` · conf H
  - Apparatus L1 (E02.Q1/Q2/Q4): classify celebratory/neutral/ironic/critical; report in-joke retellings separately; record disposition of each incoherent output. Corrected: tellability, Heidegger dial, MENU NEW GAME+ are not in the 2020 paper. Disagrees with Eladhari (07_apparatus.md:190).

- **NL-016** `NARRLIT` (+J,A) — Retellings as human-centred evaluation: output should give underdetermined evocative hooks and modelled characters so players extrapolate beyond logged events. \[FILED reference; E11 Kreminski, Samuel, Melcer & Wardrip-Fruin 2019, P (full)\] `research/emergent_narrative_literature/03_retelling_and_the_concordia_cluster.md:80` · conf H
  - Apparatus C10 (E11.Q1/Q2) and E7 (E11.Q3 ablation: with a subsystem disabled, are stories measurably harder to tell). Sample was small (20 per game coded). Hook design principle: a debate result should leave open questions rather than fully specify motive.

- **NL-017** `NARRLIT` (+M,F) — Polti's 36 dramatic situations as a mid-level authoring heuristic: roles with conflicting aims, abstract enough not to over-determine, likely tellable because rare and high-stakes. \[FILED reference; E04 Lessard & Pare-Chouinard 2022, P (full)\] `research/emergent_narrative_literature/03_retelling_and_the_concordia_cluster.md:112` · conf H
  - Apparatus C2/B4/D7 (E04.Q1-Q4): name target situations, show each reachable, report frequency; same situation across different causal histories and casts; can a stranger find a tellable account in a time budget. Candidate named situations for a parliament: rivalry of kinsmen, conflict with a superior, self-sacrifice for the law.

- **NL-018** `NARRLIT` (+M,A) — Tension space: model characters as sets of ideal worldviews over a shared fact-space; plot distance between worldviews across all world states to compute conflict potential at design time, before any run. \[FILED reference; E05 Kybartas, Verbrugge & Lessard 2020, P (full)\] `research/emergent_narrative_literature/03_retelling_and_the_concordia_cluster.md:142` · conf H
  - Apparatus C3 (E05.Q1-Q3), L4: distinguish reachable conflict from merely existing; class each action's effect on pairs of ideals; encode design goals as checkable properties. Measures structural conflict potential, not story quality. Close analogue of persons-with-convictions feeding a debate.

- **NL-019** `NARRLIT` (+M) — Interactive emergent narrative bundles two purposes: the player participating as a character, and the player authoring stories with the system as partner. Separate them when designing and judging. \[FILED reference; E07 Kreminski & Mateas 2021, P (full)\] `research/emergent_narrative_literature/03_retelling_and_the_concordia_cluster.md:172` · conf H
  - Apparatus A2/L5: which user role is served (spectator, participant, author); misapplied authority across roles. A parliament sim where the player is a member differs from one where the player curates a chronicle.

- **NL-020** `NARRLIT` (+J) — Story sifting: author-written patterns as queries over a database of past events (variables, attribute, temporal and negative constraints) coupled to a rules simulation; a deliberate caricature, not validated. \[FILED reference; E08 Felt (Kreminski, Dickinson, Wardrip-Fruin 2019), P (full)\] `research/emergent_narrative_literature/04_sifting_curation_and_simulation.md:13` · conf H
  - Apparatus D2 (E08.Q1-Q3): can a designer ask a new question of the event record without new code; can a pattern match interleaved events and an ABSENT event; can a non-match be debugged. A recorded-defeat/betrayal pattern over a proceedings record is the debate use.

- **NL-021** `NARRLIT` (+J) — Incremental sifting: patterns temporally staged so each new event advances, forks or kills tracked partial matches; recognises a microstory while still unfolding, permitting foreshadowing and live commentary. \[FILED reference; E09 Winnow (Kreminski, Dickinson, Mateas 2021), P (full)\] `research/emergent_narrative_literature/04_sifting_curation_and_simulation.md:49` · conf H
  - Apparatus D3 (E09.Q1-Q4): recognition while open, bound on in-progress candidates, stated temporal scope per constraint, sifter runs without modifying the generator. Sitting-in-progress detection (a coalition forming across motions) is the debate analogue.

- **NL-022** `NARRLIT` (+J) — Rank pattern matches by mean frequency of a match's properties among matches of the same pattern; lowest preferred (statistically rare = interesting). 15 pairs, three raters, 38/45 agreement. \[FILED reference; E10 Select the Unexpected (Kreminski et al. 2022), P (full)\] `research/emergent_narrative_literature/04_sifting_curation_and_simulation.md:81` · conf H
  - Apparatus D4 (E10.Q1/Q2/Q4): better than random in a blind comparison, measured against matches of the same pattern, discounting rarity the world's own rules expect (correlated-unlikelihood false positives). A way to choose which of many sittings to surface or recount.

- **NL-023** `NARRLIT` (+J) — Generate-then-rationalise: pick events at random, apply them to an entity's shared state, then give each a cause afterwards from that state; coherence from shared state and apophenia, not simulated causation. \[FILED reference; E15 Grinblat & Bucklew 2017 (Caves of Qud), P (full)\] `research/emergent_narrative_literature/04_sifting_curation_and_simulation.md:112` · conf H
  - Apparatus B2 (E15.Q2): is a stated cause a recorded fact, a state-derived rationalisation, or invented? Label which. Warning for any narration layer that explains a vote or decision after the fact. Corrected: 40k words is the whole corpus; 8-of-17 sultan structure not in paper.

- **NL-024** `NARRLIT` (+J) — Emergent narrative resembles nonfiction: events actually happened in a simulation; raw output rarely has story structure; remedy is curation (human or second system) rather than steering the simulation with a drama manager. \[FILED reference; E12bcd Short (2019) reporting J. Ryan's thesis, tag S (secondary); Ryan's thesis unread (08_not_read.md:18)\] `research/emergent_narrative_literature/04_sifting_curation_and_simulation.md:177` · conf M
  - Apparatus D1/D5: is there an explicit stage that selects, orders and frames events with a stated criterion; can the engine name the finite prior conditions that enabled a major outcome as a stored record. Short doubts curation alone separates good from bad generators; no hard line against drama management.

- **NL-025** `NARRLIT` (+M,J) — Stories come from apophenia: few, named, long-remembered characters, a handful of labels and numbers, plain display, much left undefined; not from deep simulation or an AI overseer. \[FILED reference; G13 Rock Paper Shotgun on Sylvester (RimWorld), tag S\] `research/emergent_narrative_literature/04_sifting_curation_and_simulation.md:211` · conf M
  - Apparatus C8 (G13.Q1/Q2): are the entities players should care about few and persistent enough to remember, with readable labels carrying small consequences. For a parliament: a small named bench of recurring members rather than anonymous aggregates.

- **NL-026** `NARRLIT` (+I) — The Simulation Dream fails: players neither want nor can perceive that much simulation. Use a simplified observable simulation, small cast, and an event generator shaped to hurt without finishing the colony. \[FILED reference; G14 Game Developer on Sylvester, tag S\] `research/emergent_narrative_literature/04_sifting_curation_and_simulation.md:242` · conf M
  - Apparatus F5 (G14.Q3/G13.Q4): does the event generator damp severity when a run goes badly, and is that disclosed (rubber-banding). Conflict with Wardrip-Fruin: both converge on perceivability, differ on remedy (07_apparatus.md:192).

- **NL-027** `NARRLIT` (+I,A) — AI Director: per-player intensity estimate (damage, incapacitation, nearby deaths, decaying) drives a state machine Build Up / Sustain Peak 3-5 s / Peak Fade / Relax 30-45 s; adjusts frequency of peaks, not difficulty. \[FILED reference; G10 Booth 2009 (Left 4 Dead), P (full), slides only\] `research/emergent_narrative_literature/06_engagement_space_and_craft.md:161` · conf H
  - Apparatus F3-F5 (G10.Q1-Q4): explicit tension variable with named inputs, decay and thresholds; designed low-pressure phase after a peak; frequency vs difficulty stated; proxy validated (slides call it crude, no outcome data). Numbers are the game's tuning, not general constants.

- **NL-028** `NARRLIT` (+A) — A storylet = content + prerequisites + effects on named world state; small recombinable unit; system picks what fits; most narrative structures expressible; branching time cave wastes the approach. \[FILED reference; G11 Short 2019 storylets, P (full)\] `research/emergent_narrative_literature/05_procedural_generation_and_choice_structure.md:176` · conf H
  - Apparatus J2 (G11.Q1-Q4): unit stateable as content+prereq+effect; add one without editing others; gating by route; play performance can change the state storylets test. Natural carrier for agenda items / petitions gated on grievance state.

- **NL-029** `NARRLIT` (+A) — Alternatives to branching: quality-based (player picks among unlocked), salience-based (system picks best-fitting), waypoint (system paths back to authored beats). Salience-based and waypoint are Short's coinages. \[FILED reference; G07 Short 2016 Beyond Branching, P (full)\] `research/emergent_narrative_literature/05_procedural_generation_and_choice_structure.md:143` · conf H
  - Apparatus F7 (G07.Q3): if the system selects scenes from world state, is there a source of dramatic shape outside the selection (else accidental ending, dead or dominant content). J4: who maintains progression state, the engine or the author by hand.

- **NL-035** `NARRLIT` (+J) — NOT READ: Sych 2023 thesis (blocked), J. Ryan 2018 thesis (bot wall; only Short's reading), Tanenbaum 2009, Tracery, Evans & Short Versu (paywall), Sengers, Murray, Salen & Zimmerman. \[FILED reference; 08_not_read.md lists every blocked or unread candidate\] `research/emergent_narrative_literature/08_not_read.md:17` · conf H
  - Also unread talks: Ingold, Ruskin fuzzy dialog, Levine Narrative Legos, Sylvester, Keenan, Hoge/de Plater Nemesis. Named, not attempted: Comme il Faut, Ensemble, Prom Week-type social sim, PaSSAGE, Riedl & Young, Szilas IDtension, Green & Brock transportation. Claims about Disco Elysium, CK, Wildermyth, Nemesis in earlier notes were not re-verified (08:54).

- **NL-036** `NARRLIT` (+J) — Apparatus applied to a design with nothing running: gates fired on no user role, undeclared hybrid, no tension variable, no starvation alarm; every rater/player/ablation row was inapplicable; apparatus silent on five needs. \[FILED reference; first application of the apparatus to PR #506 thrust-layer design (one critic reading)\] `research/emergent_narrative_literature/00_README.md:13` · conf M
  - Silent on: whether a pacing clock is wound by an act, what share of agents' acts the world refuses (~76% in the design's register; no source measures an execution rate), belief vs world truth for progress, false-positive null for arc detectors, periodic stagger. Scored APPLIES 0, N-A 27, UNTESTED 11, CONTRADICTS 2 against five modules.

- **NL-097** `NARRLIT` (+I,B) — Where a design has no GM, name the GM functions and what carries each: intervention types and triggers, tension variable, starvation alarm, low-pressure phase, frequency vs difficulty. \[FILED reference; Gate F of the 75-row apparatus (evidence mostly doc/trace)\] `research/emergent_narrative_literature/07_apparatus.md:94` · conf M
  - Rows F1-F7 draw on T12 Louchart, T03a Facade, G10 Booth, E16 Riedl, G07 Short. Valoria has no GM by rule (CLAUDE.md): chair, convener, deadlock-breaker, pacer are the functions a sitting would need to carry in code or drop on the record.

- **NL-098** `NARRLIT` (+J) — Can the engine name, for a major outcome, the finite prior conditions that enabled it as a stored record (D5)? Does one situation arise through different histories across seeds (B4)? \[FILED reference; apparatus rows D5, B4, B2\] `research/emergent_narrative_literature/07_apparatus.md:76` · hook: Event.causes; harness/storybar.py · conf M
  - Sources: E12 Short on Ryan (S), E04 Lessard, E15 Qud, E17 Adams. Repo analogue: every Event carries causes[]; storybar/chronicle read the chain (NL-071/072); no stored 'enabling set' beyond causes. A vote's recorded cause chain answers D5.

- **NL-099** `NARRLIT` (+I) — Should anything steer the story? Facade and Riedl & Bulitko: a manager sequences content to a target. Ryan (via Short, S): curate instead. Aylett: script no plot. \[FILED reference; 'Where the sources disagree' table\] `research/emergent_narrative_literature/07_apparatus.md:188` · conf H
  - Other splits in the same table: where a game's story lives (Juul vs Aylett vs Ryan), whether a retelling proves success (Eladhari vs Sych), how much simulation should show (Wardrip-Fruin vs Sylvester/Adams), whether narrative is a mechanic (Koster vs Mateas vs Hocking), whether replayability justifies generation (Juul vs Smith/Compton).

- **NL-100** `NARRLIT` (+G,D) — Ludonarrative dissonance (title only in the post): ludic and narrative contracts send opposite messages about what to do, undercutting both. \[FILED reference; G06 Hocking 2007, P (full) (archive copy)\] `research/emergent_narrative_literature/06_engagement_space_and_craft.md:132` · conf H
  - Apparatus K3 (G06.Q1-Q4): forced-choice override, commentary on the player consistent with what they were shown, a moral choice with different mechanical payoffs. For a parliament: if the text calls a vote binding while the code lets the outcome go unenforced (NL-050), the two contracts conflict.

- **NL-101** `NARRLIT` (+C) — Narrative is not a mechanic but a form of feedback about how the player's input is going; a game whose systems are outweighed by narrative feedback is a weak design even if a good experience. \[FILED reference; G12 Koster 2012, P (full)\] `research/emergent_narrative_literature/06_engagement_space_and_craft.md:191` · conf H
  - Apparatus K4 (G12.Q2-Q4): authored content consumed per hour, whether the system generates new problems without new content, whether feedback is proportionate to the problem solved. Opposes Mateas (story as formal constraint giving reasons to act). Argues a debate result should be feedback on the mechanics, not a substitute for them.

- **NL-104** `NARRLIT` (+J,H) — Indexical storytelling: story built from traces (signs physically connected to past events) left in game space; reading and leaving traces is tied to how the player acts. \[FILED reference; G04 Fernandez-Vara 2011 and G05 Carson 2000, P (full)\] `research/emergent_narrative_literature/06_engagement_space_and_craft.md:73` · hook: Record, forge, destroy_record, carry · conf M
  - Apparatus H5 (G04.Q1-Q4, G05.Q3): history leaves readable traces that point to a recoverable cause, change what the player or an agent does next, persist, and can be read by non-player agents. Candidate traces for a parliament: a Record, a seal, a stripped seat, a burned decree.

- **NL-107** `NARRLIT` (+J,A) — What fraction of authored content does one run reach? Do two sessions from the same start give players something to compare? Facade reaches about 25% per run; low variance kills comparison; author satisfaction is not reception. \[FILED reference; apparatus row I7 (T03a.Q4, T03b.Q4, E01.Q3, E15.Q4)\] `research/emergent_narrative_literature/07_apparatus.md:147` · conf M
  - Volume mistaken for variety. For a deck of agenda items or events: report per-run coverage (items fired / items authored) and whether two seeds from one start diverge enough to retell differently.

- **NL-108** `NARRLIT` (+J) — If a player misses any one element, is the essential information delivered elsewhere (H4)? Do traces point to a recoverable cause and get read by non-player agents (H5)? \[FILED reference; apparatus rows H4, H5, H3, E6\] `research/emergent_narrative_literature/07_apparatus.md:131` · hook: claim channels (rosters.yaml witness_channels) · conf M
  - Sources T05, G04, G05, T11, G13, G14, T03b. Single-point information loss in non-linear play is the failure caught by H4. A decree that only one attendee heard fails it unless a channel (tell, document, public record) re-delivers.

- **NL-109** `NARRLIT` (+A) — No source here tests directly whether authored narration crowds out player-made stories; nearest are the sandbox-without-hooks test (T05.Q3) and the event-generator damping test (G13.Q4, secondary). \[FILED reference; crosswalk row N12, marked WEAKLY SUPPORTED\] `research/emergent_narrative_literature/07_apparatus.md:213` · conf M
  - The survey cited Jenkins quoting Lynch for N12. Matters for a debate layer that adds authored speech text or event cards: displacement of emergent story by authored story is untested in the literature read.

- **PR-088** `NARRLIT` (+M,J) — Crusader Kings: per-pair opinion STACK of named modifiers each with source, magnitude and own decay; relation flags (rival/lover/nemesis) separate from the number; hooks (weak single-use, strong persistent); typed secrets with a known-by list; stress and break points; characters act by a utility scorer weighted by traits. \[relay G, sonnet research pass, REFERENCE status (external material; nothing a design decision; web-verified except tabletop entries)\] `proposals/2026-09-05-proceedings-subsystem/relay/G_EMERGENCE_PRECEDENT.md:31` · hook: none (reference for claim/opinion model) · conf M
  - Retained events write a history entry, upgrade a decaying modifier into a durable flag, or create a Secret whose discovery is a future event. Escalation by correlated independent thresholds (many vassals joining one faction). Anti-log: pop-ups quote only the causally relevant modifiers.

- **PR-089** `NARRLIT` (+M) — RimWorld: mood = sum of independent memory 'thoughts' each with decay; a storyteller director schedules incidents from wealth, population and days since last (Cassandra/Phoebe/Randy); mood crossing trait-scaled thresholds (5% extreme/20% major/35% minor default) triggers a mental break whose flavor is trait-weighted. \[relay G; reference\] `proposals/2026-09-05-proceedings-subsystem/relay/G_EMERGENCE_PRECEDENT.md:51` · conf M
  - Memory feeds mood only and never gates an action - the one surveyed system where players report memories that should matter quietly expiring. Permanent exceptions promoted out of decay (ex-lover tag, scars). Breaks spawn witnessed-break thoughts in bystanders (chaining).

- **PR-090** `NARRLIT` (+J,M) — Shadow of Mordor Nemesis: per-orc per-relationship records of specific encounters written onto the orc's identity (scars, name, taunts); outcome-keyed state machine (orc beats player -> levels up, promoted); a beaten orc is actively re-queued to reappear; escalation monotonic with no release valve. \[relay G; reference\] `proposals/2026-09-05-proceedings-subsystem/relay/G_EMERGENCE_PRECEDENT.md:73` · conf M
  - Mechanically shallower (scripted transitions) but narratively strong via active re-surfacing and identity-embedded memory. Eviction by death not time.

- **PR-092** `NARRLIT` (+L) — Ranked common mechanisms across seven systems: (1) typed persistent relationship records not a scalar (6/8); (2) memory that gates ELIGIBILITY not just flavour; (3) escalation by threshold crossing with shared causes; (4) identity-embedded memory over separate log; (5) fork between computed utility and authored branch selection. \[relay G ranked table; feeds 18 PART B/I\] `proposals/2026-09-05-proceedings-subsystem/relay/G_EMERGENCE_PRECEDENT.md:113` · hook: none (informs P-42, claim eligibility) · conf M
  - Failure modes: undifferentiated NPCs, memory that never surfaces, decorrelated event stream, escalation with no terminus (caps: DF clamps 0-100, RimWorld timers, CK single-use hooks), legibility collapse at scale, cosmetic memory, mistaking authored-branch systems for simulated. Generalizing lesson: couple the memory read to a specific decision-evaluation point, not an ambient scan.


