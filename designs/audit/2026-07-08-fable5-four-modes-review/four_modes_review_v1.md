# Design Review — The Four Deliberative Modes of the Social Contest
## Agôn · Negotiation · Inquiry · Consensus: what each brings, how each connects, and whether all four earn their budget

## Status: FILED (informational review) — 2026-07-08. Advisory only; no ledger action taken by this
## document itself. Its recommendation (re-scope Inquiry as a composition rather than a fourth
## from-scratch engine) is not yet an ED — fold into the Stage-4 entry-criteria decision when Stage 4
## is next scoped (see `handoffs/HANDOFF_SC.md`).

**Date:** 2026-07-08 · **Reviewer:** Fable 5 (read-only) · **Lane:** SC
**Sources of record:** `designs/scene/social_contest_v30.md`, `params/contest.md`, `sim/personal/contest/` (esp. `wrapper.py`, `resolver.py`, `faction.py`), `designs/audit/2026-06-28-social-contest-deliberation-critique/critique.md`, `designs/audit/2026-07-05-fable5-social-contest-audit/`, `designs/audit/2026-07-01-contest-player-interaction/player_interaction_walkthrough_v1.md`, `handoffs/HANDOFF_SC.md`, `canon/editorial_ledger.jsonl` (ED-SC-0002..0011, ED-IN-0028), `CURRENT.md:37`.

---

## 0. Where the four modes actually live today

The router is `sim/personal/contest/wrapper.py:206-215` (`GAMES` dict): **`agon` is WIRED** — the promoted kernel `Bout` on the Persuasion-Track path; **`consensus` / `negotiation` / `inquiry` are registered STUB rows** that raise `NotImplementedError` (mirrored in `MECHANICS` at `wrapper.py:336-338`). The four-game shape was not in the original v30 spec — it was authored by the 2026-06-28 deliberation critique (`critique.md §0-§1`): a deliberative procedure can *crown a winner, strike a bargain, discern a truth, or enact a unity*, and Valoria had built only the first. The staged rebuild adopted that as Stage 4 (`HANDOFF_SC.md:9-12`), and the 2026-07-05 Fable-5 audit then resequenced Stage 4 **after** a P0 decision docket and a P1 consequence spine (`fable5_social_contest_audit_v1.md §6`, ratified 2026-07-05).

State as of today (2026-07-08, verified against the ledger and `CURRENT.md:37`):

- **ED-SC-0006 (P1 spine part 1) is EXECUTED** — `scene_dispatch` now routes the one live campaign trigger (Stability Crisis → Emergency Council, as `guild_arbitration`) to the promoted kernel; the campaign regression asserts ≥1 resolved contest (`editorial_ledger.jsonl` ED-SC-0006, dated 2026-07-08). The kernel is no longer dead-in-campaign.
- **ED-IN-0028** built the echo-transport plumbing (un-orphans `domain_echo.py`) but it is deliberately **inert** — no contest sets an echo context yet.
- **ED-SC-0007 (outcome → world) is still open**, blocked at spec level on **ED-SC-0002** (the §5.4 band-keyed vs §6 genre-keyed Domain-Echo conflict, a Jordan fork).
- **The P0 docket ED-SC-0002..0005 still awaits Jordan's four picks** (echo keying; Piety/Persuasion tracker naming; kernel Argue-pool formula; Recall/Corroborate/Prep/Findings stack cap).
- **P3-lite (human-plays-Agôn harness) has not been built** — no interactive harness exists anywhere in `sim/` or `tools/` (repo grep), and no human has yet played even the one wired game.
- **Stage 4 entry criteria (ED-SC-0009)** — Face/Rattled strain channel, §9.3-9.4b thread hooks — are open; ED-SC-0005 (stack cap) and ED-SC-0010 (Chronicle focalization) are additional entry gates per `HANDOFF_SC.md:108-110`.

So the honest frame for this review: one mode is a mature engine that no human has played; three modes are one-line registry rows whose design exists only in an audit critique, a UI-divergence sketch, and (for Consensus) an adapter module.

---

## 1. AGÔN — the adversarial persuasion-track contest

### 1.1 What it is specified to do

The fullest spec in the corpus, and the only one with a running implementation:

- **Setup** (`social_contest_v30.md §2`): 8 canonical proceedings (`§2` Step 5 table, lines 97-106; `params/contest.md:184-196`) fix exchange count, role structure, resistance modifier, adjudicator type, and starting stasis. Four adjudicator types (Expert Judge / Crowd / No-adjudicator / Panel) rotate the Argue pool's primary attribute (Cognition/Charisma/Attunement; `§3:119-128`), with Panel resolved by weighted-by-standing `VoteAtClose` ballot (ED-1057/1059; `params/contest.md:215-247`; `resolver.py:97-146`).
- **Exchange loop** (`§4`): Appraise (4-band information ladder, `§4:144-154`) → Style pick (Precedent/Suppression/Vision/Insinuation = genre × orientation, `params/contest.md:34-57`) → Argue on the δσ sigma-leverage substrate (CR2; `params/contest.md:158-165`) → CLASH/REINFORCE/CROSS/TIE resolution moving a 0-10 Persuasion Track against audience resistance (`§4:179-217`).
- **Rhetorical depth wired at Gate C (ED-1062):** CR4 stasis-derived primary genre (`§2:48-60`), CR5's two-sided Obscuring bet (Doubt Marker + self-Face backfire, `§4:214-223`), and the adjudicator armature — a hidden 4-axis conviction vector the chosen Style dot-products against, entering as continuous δσ leverage and revealed only partially through Appraise (`§4:171-177`).
- **Three trackers** (CR3, `§4 Step 6:229-259`): Concentration (stamina), Face (contest-local standing, Charisma×3 ceiling × Standing position), Persuasion Track (merits).
- **Termination and consequence** (`§6`): banded resolution (Total/Decisive/Compromise), Domain Echo (`§6:287-292`), binding Obligations incl. Wager Obligations (`§6.1:296-344`), Chain Contests from Compromise (`§6.3:354-369`).

### 1.2 What it distinctly brings

Agôn is the **zero-sum merit contest with a third-party audience** — the game where "who won the room" is the whole question. Its distinct decision space, which none of the other three replicate: the *bet-under-uncertainty against a hidden judge* (armature + Appraise partial-reveal — the prior audit's Q-elegant PASS, `fable5_social_contest_audit_v1.md §2`), the two-sided Obscuring gamble (CR5), and resource-triaged escalation across a fixed exchange budget. The 2026-06-28 critique's own verdict stands: "an excellent build of *one* game" (`critique.md §0`).

Its two real liabilities are not design but experience: **~13 per-decision consults per exchange against a 3-4 personal-scene ceiling** (audit N-7, UPHELD), and **zero human play-testing**. Everything validated about Agôn has been validated engine-against-itself.

### 1.3 How it connects

- **Upstream (built):** the 8 proceedings are the trigger taxonomy; since 2026-07-08 one live campaign path exists (Stability Crisis → Emergency Council → `guild_arbitration`, ED-SC-0006). Every other proceeding is reachable only by direct API call — no scene generator or player-initiated path selects them yet.
- **Downstream (mostly gap):** §6's consequence surface (Domain Echo, Obligations, Chain Contests, Conviction Scars, Belief revision) is well-specified prose with **no wired transport**: ED-SC-0007 is open, blocked on the ED-SC-0002 keying fork; Obligations-as-clocks and the NPC-priority-tree binding have no kernel emitter; the `Chronicle` narrative record is consumed by nothing (audit N-8a). The prior audit's headline — "no outcome changes the world" — is now half-fixed (reachability yes, echo no).

**Verdict on Agôn:** earning its budget as the flagship; the binding risks are the consult-count and the untested interaction model, both of which P3-lite exists to measure and neither of which is closed.

---

## 2. NEGOTIATION — the mixed-motive bargain

### 2.1 What is actually specified

The thinnest paper trail of the four, and the spec itself says so: v30 §12 lists *"Negotiation compromise resolution (ZOPA-style) — identified as structurally different from Persuasion Track, not designed"* (`social_contest_v30.md:688`). The wrapper's GAMES row marks it **author-new** (`wrapper.py:211-212`). What design exists:

- **The critique's blueprint** (`critique.md §2.3`, mixed-motive FG-1/FG-2, ★★★★★): a *parameterization of the existing contest, not a new engine* — the sigma track sets each side's BATNA/reservation point; the stranded **Recruitment Offer table** (`npc_behavior §9.5 Step 3`) becomes the integrative move (spend a faction-stat delta to lower the other side's Argue-Ob, widening the ZOPA); a deal in the overlap pays out via the **§7.2.1 track-distance split weights** (60/40, 55/45, 50/50); no-deal falls back to the zero-sum track. FG-2 adds **coalition win-sets + ratification checks** (Putnam's two-level game): a Lead's concession outside a member's win-set triggers repudiation/defection.
- **The interaction shape** (`player_interaction_walkthrough_v1.md §4:143-145`): a **two-sided offer panel** — BATNA brackets, a live ZOPA overlay — "a bargaining table, not a tug-of-war bar."
- **Existing near-misses to be superseded/absorbed:** the *Private Negotiation* proceeding (1-3 exchanges, no adjudicator, optional tracker, exchange-majority `TallyAtClose`; `params/contest.md:193`) — currently an Agôn skin, exactly the collapse the critique diagnosed ("Bargaining is collapsed to a tug-of-war," `critique.md §0` item 3).

### 2.2 What it distinctly brings

**The only positive-sum decision space in the entire social layer.** Every currently expressible social outcome is win/lose/compromise-as-deferral; Negotiation is the one mode where both sides can *gain*, where making a concession is a move rather than damage, and where the interesting question is surplus *division*, not victory. Three genuinely new player verbs with no Agôn equivalent: **table an offer** (spend a resource to enlarge the deal space), **hold at your BATNA** (walk-away as leverage), and — via win-sets — **negotiate with your own coalition** at the same time as the opponent. The two-level game also gives Beliefs their first hard mechanical home (Vaynard's Belief 3 is a textbook win-set "written into the fiction with no mechanical home," `critique.md §2.3`).

**Overlap check:** low. This is the mode most structurally distinct from Agôn — the spec's own §12 deferral says as much. The one redundancy hazard is doing it *badly*: if Negotiation ships as "Persuasion Track + a deal-split at the end," it is a venue skin and confirms KT-1. The BATNA/offer/ZOPA loop is the distinctness; the split table alone is not.

### 2.3 How it connects

- **Upstream:** Private Negotiation and Personal Appeal proceedings; treaty/diplomacy and Recruitment scenes (the Offer table's current home); any two-party stakes with a divisible axis. None of these routes exist in dispatch.
- **Downstream:** bilateral Obligation pairs (§6.1 already supports the output shape); faction stat deltas via the Offer spend; the §7.2.1 split machinery (already in code — `faction.py succession()` returns the exact 60/40-55/45-50/50 ratios).
- **Gap status:** everything player-facing is unbuilt; the consequence plumbing it needs (Obligations-as-clocks, echo transport) is the same P1 gap as Agôn's. Notably its *ingredients* mostly exist — Offer table, split weights, Disposition, Ob channel — the critique's "zero new engine" claim held up under its adversarial verification.

**Verdict:** the strongest earn of the three unbuilt modes — it adds a game-theoretic family the system cannot express at all today. Also the largest genuine authoring job (the offer economy and win-set derivation are real design work, and the AI policy for an NPC negotiator is a new problem class — `policy.py` currently ships argue-styles, not offer strategies).

---

## 3. INQUIRY — the truth-discernment proceeding

### 3.1 What is actually specified

The wrapper cites "social_contest_v30 §7 Church Tribunal / Inquisition (author-new)" (`wrapper.py:213-214`) — but read closely, **§7 specifies an asymmetric Agôn, not an inquiry**: Church Tribunal is Inquisitor-proposes, biased track start 6, halved accused-resistance, Expert Judge, resolving on the same Persuasion Track (`§7:376-384`). The genuinely inquiry-shaped material is scattered:

- **CR4's conjectural stasis** (ED-1062): Church Tribunal is the one proceeding opening on FACT — "did X happen?" (`§2:60`, `§7:384`) — the question-shape of an inquiry, wired as a genre-bonus condition, not a distinct resolution logic.
- **The Heresy Investigation lifecycle** (`§7.3:427-475`): a genuinely investigative multi-season *procedure* (Evidence Track thresholds, interrogation phases, 8 closure conditions) — but its per-scene resolution is again the standard track.
- **Kernel substrate:** `ProofBar` (`resolver.py:65-71`) — challenger must clear an absolute evidence bar or lose — is the natural inquiry win-condition, already implemented, currently unused by any proceeding. Evidence enters via `Dossier`/`EvidenceItem` (live, capped at `EVIDENCE_CAP`, `resolver.py:42`).
- **The interaction shape** (`walkthrough §4:146-147`): a **belief-alignment meter per contested proposition** — "closer to a shared whiteboard than a contest track — the 'win' condition is convergence, not domination."
- **Crucially, the critique itself demoted the inquiry gap**: four-games FG-2/3/5 are tagged *"low / already-handled — Belief Revision (`npc_behavior §3.2`: decisive + correct Resonant Style + Belief engagement → the loser is persuaded on the merits) already provides the inquiry game… The residue is narrow"* (`critique.md §2.6`) — an ED-937 Key emission and an optional Sincerity Gate. **Editorial, not structural.**

### 3.2 What it distinctly brings — and the honest problem

In principle: a mode where the opponent is not the enemy — the *unknown* is — and where evidence accumulation, not rhetorical force, decides. The FI lane makes this attractive: the master workplan explicitly names field investigation as "the evidence supply chain for the claim-grammar interface (trails → evidence → argument → precedent → new stakes)" (`valoria_master_workplan_v6.md:203-205`), and Inquiry would be that chain's terminal venue.

In practice, **Inquiry has the weakest standalone case of the four**, on the corpus's own evidence:

1. Its cited canonical home (§7) is an Agôn variant; nothing in canon specifies a convergence-resolution logic.
2. The critique that invented the four-game frame concluded the truth-discernment function is *already mostly delivered* by Belief Revision + the Evidence Track + the merit-reward gradient.
3. The walkthrough's per-proposition alignment meter presupposes propositions as first-class objects — which is the **commitment store** (`critique.md §2.5`, tagged effort-HIGH and deliberately not scheduled). Without a propositional substrate, "Inquiry" degenerates to Agôn-with-a-ProofBar-and-a-different-meter — precisely a venue skin, the KT-1 failure mode built brand-new.

### 3.3 How it connects

- **Upstream:** Church Tribunal / Excommunication Tribunal (§7.1) / Heresy Investigation verdict phases; FI-lane Evidence Track findings (F-TRANS-11 already bridges Findings → contest dice, `§9.1:532`).
- **Downstream:** verdicts (acquittal/escalation per §7.3), Belief revision on NPCs, Conviction Scars — all doc-only channels today (audit D2 Ω(b): "no outcome persists onto a character in code").
- **Gap status:** the largest spec gap of the four — Negotiation at least has a ratified blueprint paragraph with named mechanisms; Inquiry has a flavor sentence, an unused win-condition class, and a dependency on an unbuilt high-effort substrate.

**Verdict:** does **not** currently earn a fourth engine-game slot. Recommend re-scoping (see §6).

---

## 4. CONSENSUS — assent, holdout, and the unity-enactment

### 4.1 What is actually specified

The best code coverage of the three stubs — Gate 0's finding was "Consensus mostly promote-existing" (`HANDOFF_SC.md:22-23`), and it holds up:

- **Canon:** §10 BG Parliamentary Vote (Mandate-pooled sides, lobby-capped start, pass/committee/fail bands; `social_contest_v30.md:575-597`), §7.2 Succession Contest (institutional-body adjudication, Compromise → track-weighted **faction split**, `§7.2:386-423`), and the §5.3-5.5 faction-layer motion machinery.
- **Code (`sim/personal/contest/faction.py` — self-described "ADAPTER (not canon)"):** `vote()`/`rate()` (per-faction Mandate+CI-weighted ballots, each voter persuaded via its own armature-carrying `Bout`, ~lines 44-77); `band_of()`/`rate_banded()` (the committee band); `succession()` (full §7.2.1 outcome ladder incl. split ratios, ~86-113); `coalition_vote()` (§10 pooled coalitions with abstention damping, ~121-143). Plus `VoteAtClose` per-member ballots with weighted aggregation (`resolver.py:97-146`) and `GraceThreshold` (`resolver.py:72-77`).
- **The genuinely NEW piece — the critique's Type-3 procedure** (`contest-locus FG-3`, HIGH; `critique.md §2.4`): a **unanimity/holdout game**. Per-required-assenter flags resolved by sigma rolls; a lone holdout mints a "Holdout" Obligation clock + Scene-Slate entry (the *liberum veto* pathology becomes plot, not deadlock); a **frivolous-block antibody** (armature dot-product below threshold → Mandate cost) prevents stall-spam. The source-research trilogy (`2026-06-28.../source-research/`, which Stage-4 agonists are directed to read raw, `HANDOFF_SC.md:77-85`) supplies the liberum-veto-as-self-undermining-equilibrium grounding.
- **Interaction shape** (`walkthrough §4:148-150`): a **per-assenter roster** — a row per NPC/faction flipping undecided → assenting, a visible holdout counter, the frivolous-block cost shown live.

### 4.2 What it distinctly brings

Two things no other mode has:

1. **N-party structure.** Agôn, Negotiation, and Inquiry are all two-pole (coalitions pool onto two sides — `coalition_vote()` demonstrates this deliberately). Consensus is the only mode where the *target is plural*: you persuade a roster one member at a time, and the decision-relevant read is "who is still holding out and why."
2. **The veto/holdout pathology class** — the critique's "largest unreachable pathology class on the churn axiom." Canon already *names* consensus institutions (RM "by consensus," the Wardens; the §7.2 Succession table) but resolves them as Mandate-weighted votes — a label with no mechanic. Without Consensus, a single stubborn assenter can never be the story.

**Overlap check:** moderate but manageable. The per-assenter *persuasion* step is literally an Agôn micro-bout per voter (that is how `faction.py._one_vote()` already does it) — and that is fine: the *game* is the roster-level structure (whom to spend exchanges on, when a holdout is worth the antibody bet), not the per-voter roll. The KT-1 risk is real only if Consensus ships as `rate_banded()` with a UI — i.e., a batch vote with no sequential player agency. The holdout clock + antibody + per-assenter targeting are what make it a fourth game rather than §10 re-skinned.

### 4.3 How it connects

- **Upstream:** Succession Contests (leader removal at Accounting), Parliamentary motions/Stays (§10.1), RM/Warden internal decisions, treaty ratification. The §10/§11 BG↔personal hybrid path is specified in canon.
- **Downstream:** the *richest* consequence surface of the four, and much of it already coded at adapter level: faction splits (§7.2.1 ratios in `succession()`), Mandate penalties (`parliamentary_vote.py` writes them — though `mc_v18` never calls it; audit dossier C, still true per ED-SC-0007's scope note), committee referrals, Holdout Obligation clocks (new).
- **Gap status:** promotion + the holdout/antibody design + player-agency shaping. `faction.py`'s own docstring ("ADAPTER (not canon)") flags the canonization step honestly. Cheapest of the three by a wide margin.

**Verdict:** earns its slot, and is the correct **first** Stage-4 build — highest existing coverage, lowest engine risk, unlocks a canonically-promised institution class.

---

## 5. The KT-1 critique — "one game wearing eight venue skins": confirmed, with a sharper boundary

KT-1 (`finding_status.md:13`) and the critique's meta-finding (`critique.md §1`) are **confirmed on my own read of the specs** — for the *current* system. The 8 proceedings differ in exchange count, role symmetry, resistance, adjudicator attribute, track start, and (post-CR4) one starting stasis — every one of them is parameter variation on the identical Appraise→Style→Argue→Track loop. Private Negotiation is a bargain resolved as a tug-of-war; Church Tribunal is an inquiry resolved as a biased tug-of-war; Guild Arbitration's Panel changes only the terminal read. That is precisely one game in eight costumes.

But the finding cuts *both ways* for Stage 4, and this is the review's central caution:

- **The refutation-in-principle is already in the kernel.** `resolver.py` carries five pluggable win-conditions (ThresholdRace / TallyAtClose / ProofBar / GraceThreshold / VoteAtClose, lines 50-146). The engine was deliberately built so that new games are new terminations + new move surfaces on the same σ-substrate — the critique's own "do-not-touch" list demands exactly this reuse (`critique.md §7`).
- **The trap is that a win-condition swap is NOT a game.** The distinctness test each Stage-4 game must pass: *does it change the player's decision space, or only the termination read?* Negotiation passes clearly (offers, BATNA, win-sets — new verbs). Consensus passes if and only if the roster/holdout layer gives sequential targeting agency (new target structure). **Inquiry, as currently sourced, fails the test** — its only specified differences are a ProofBar and a meter label, unless the commitment-store substrate exists to make propositions playable.
- The walkthrough's §4 exists precisely because the team saw this risk ("each game's interaction shape should look and feel different, **or they are not four games**," `walkthrough:140`). That sentence should be treated as the Stage-4 acceptance criterion, applied *mechanically* and not just visually.

Worth noting what the four modes correctly do NOT include: the critique's alea (WeightedLot) and mimicry (Acclamation) families were recommended as **pluggable win-conditions on existing games**, not as fifth and sixth games (`critique.md §2.4`) — the four-game roster is already the right cut of the space; the question is only whether all four are games.

---

## 6. Overall verdict

### Are all four earning their design budget?

| Mode | Earn | Basis | Recommendation |
|---|---|---|---|
| **Agôn** | **Yes — flagship** | Only built mode; corpus-best legibility discipline; genuinely novel armature bet | Do not extend further until a human has played it (P3-lite). Its open risks are UX (N-7 13-consult load) and the ED-SC-0004 pool-formula fork, not design. |
| **Negotiation** | **Yes — strongest new addition** | The only positive-sum decision space in the social layer; ratified blueprint (mixed-motive FG-1/2) with mostly-existing ingredients | Build second. Hold the line on BATNA/offer/ZOPA as the core loop — a track-plus-split-table version is a skin, not a game. Budget for the NPC offer-policy AI as real new work. |
| **Consensus** | **Yes — cheapest earn** | N-party structure + holdout/veto pathology, both unreachable today; `faction.py`/`VoteAtClose`/§7.2/§10 cover most of it | Build first. The new design surface is narrow and well-specified: holdout clock, frivolous-block antibody, per-assenter targeting agency. Canonize the `faction.py` adapter as part of the same pass. |
| **Inquiry** | **Not as scoped** | Cited canon home (§7) is an asymmetric Agôn; the critique itself found truth-discernment "mostly already handled" (Belief Revision + Evidence Track); the convergence meter presupposes the unbuilt, effort-high commitment store | **Re-scope rather than cut**: (a) short term, deliver "inquiry" as a *composition* — Church Tribunal/Heresy proceedings + ProofBar win-condition + Evidence-Track integration + the ED-937 `belief_revised` Key + Sincerity Gate (all cheap, mostly propagation); (b) revisit Inquiry as a first-class fourth game only when/if the commitment store or the FI claim-grammar (workplan v6's v2-§5 requirements input) gives it a propositional substrate. Do not author a fourth interaction shape that is Agôn with a different meter — that would manufacture the exact KT-1 pathology Stage 4 exists to fix. |

Net: **3½ of 4 earn.** The four-way taxonomy is analytically right (it comes straight from the deliberation research), but taxonomic completeness is not a build order. Shipping "Negotiation + Consensus + Inquiry-as-composition" delivers all four *deliberative functions* while building only two new interaction shapes.

### Sequencing risk — the actual one

The ratified sequencing (P0 → P1 ∥ P3-lite → Stage 4 → calibration) is correct and is **not yet satisfied**:

1. **The P0 docket is the live blocker, and it is Jordan's.** ED-SC-0002..0005 are all open/`needs_jordan`. Two of them bite Stage 4 directly: ED-SC-0004 (which Argue-pool formula is canon — building three new games on an undecided pool formula multiplies rework across every one of them) and ED-SC-0005 (the +8D bonus stack must be capped in prose *before* Stage 4 wires those channels and makes the hazard live). ED-SC-0002 blocks the echo half of the spine.
2. **The consequence spine is half-landed.** Reachability is done (ED-SC-0006, 2026-07-08 — a real and recent win); echo transport is plumbed but inert (ED-IN-0028); ED-SC-0007 waits on the ED-SC-0002 fork. Until it lands, a Stage-4 game would still be a game whose outcome changes nothing — the prior audit's core objection, still half-true.
3. **P3-lite has not happened, and it is unblocked.** No harness exists; no human has played Agôn; the 13-consult overrun (N-7) is unmeasured. Building three new interaction shapes on an interaction model that has never met a player is the single largest identified risk in this program — the prior audit's independent critic tried to defeat this argument and could not (`fable5_social_contest_audit_v1.md §6`). The per-mode UI divergences of §4 of the walkthrough (offer panel, alignment whiteboard, assenter roster) are *hypotheses about what players can parse*, and right now there is zero empirical data about whether they can parse even the simplest of the four.
4. **Stage-4 entry criteria (ED-SC-0009/0010) are open**: the Face/Rattled strain channel (the CR3 triangle still runs on two legs), the §9.3-9.4b thread hooks (P-14 fails at kernel depth), and Chronicle focalization (P-03) — each is cheaper to land before the shape-count multiplies by four.

**Recommended next actions, in order:** (1) Jordan rules the P0 docket — four picks, no build; (2) land ED-SC-0007 + the P3-lite Agôn harness in parallel; (3) run one human through Agôn and let the consult-load data set the interaction budget for Stage 4; (4) enter Stage 4 as **Consensus → Negotiation → Inquiry-as-composition**, each gated on the walkthrough-§4 distinctness criterion applied mechanically ("new decision space, not new termination read"). That order delivers the four-game promise at roughly two-thirds of its nominal build cost, with each new mode landing on a system that a campaign can reach, that echoes into the world, and that a human has actually played.
