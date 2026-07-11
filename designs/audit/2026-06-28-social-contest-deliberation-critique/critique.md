<!-- STATUS: AUDIT — analytic instrument output, not canon. Self-exempting (Class A analysis). -->
<!-- Investigation: critique of the social contest system as a DELIBERATIVE GAME, against the
     deliberation/politics-as-game + Renaissance-machination research corpus (6 source documents). -->
<!-- Method: 8-lens multi-agent critique (one analyst per theoretical lens) + adversarial verification
     of every finding against the live working tree (checking whether claimed gaps are filled elsewhere).
     46 agents, ~3.3M subagent tokens, 0 findings refuted. Raw verified findings: findings.json. -->

# Valoria — The Social Contest as a Deliberative Game: a configuration critique

**Date:** 2026-06-28 · **Scope:** `social_contest_v30` (spec + infill + params + extensions + sim) read as a *deliberative game*, against the research corpus, with validation from the live engine (Key bus, the two primitives, the conviction armature).

**Lens corpus (6 documents):** `deliberation-as-game-synthesis` (four senses of "game"; constitution-by-rules; commitment stores; validity-as-winning-strategy; fallacies-as-fouls; mixed-motive vs zero-sum) · `politics-as-deliberative-game` (Caillois's agôn/alea/mimicry/ilinx; where the contest sits relative to the decision; the meta-game over *which* game legitimates power) · the three `renaissance-*` installments (machination, mechanism design, capture/robust-action/*broglio*, the archival test).

---

## 0. Executive summary (plain language)

You asked for a critique of how the social contest is *configured*, with regions for improvement, worked **bottom-up and emergent with validation from the top down**.

The honest headline: **the contest is an excellent build of *one* game — the agôn (the rule-equalised merit-contest with a victor) — and the engine has already proven, in four places, that it can hold the other games too. The configuration debt is that the system collapses what the research treats as four distinct things a deliberative procedure can do, and four distinct families of play, onto the single agonistic Persuasion Track.** This is *under-configuration and seam-closure*, not a broken architecture — almost every fix below reuses primitives you already ship.

The research is unambiguous that "game" is not one thing. A deliberative procedure can **produce a winner** (agôn), **strike a bargain** (mixed-motive, positive-sum), **discern a truth** (inquiry), or **enact a unity** (consensus/acclamation) — and the interesting play lives *in the gaps between them*. Caillois sorts the same space into **agôn / alea (chance) / mimicry (performed legitimacy) / ilinx (the crowd-charge)**. Valoria runs everything through agôn: a 0–10 zero-sum bar, Composure-as-hit-points, strain-as-damage, Focus-defence-as-armour. Pragma-dialectics' sharpest finding is that pure-contest ("win at all costs") is the *degenerate* mode of deliberation — and it is the mode the track makes optimal.

**What is *not* configured yet, in descending leverage:**

1. **The adjudicator is a flat resistance number where your second engine primitive would make verdict-legitimacy *emerge*.** The adjudicator — the agent who *declares the outcome* — contributes only `avg-faction-Stability − 1` and one boost die. The engine already has a 13-Conviction × 4-axis **armature dot-product** ("meaning-for-an-observer") and already aims it at the *opponent* (Resonant Style targeting). It is pointed at the wrong party. This is **the central bottom-up violation**: macro verdict legitimacy is gated by a stat-average instead of emerging from argument-meets-judge's-conviction.

2. **The procedure itself is frozen at GM setup; the meta-game — capture, forum-shopping, the antechamber — is unmodeled.** The single most consequential historical variable ("under whose rules, before whom, in what genre") is removed from play. Disposition and Subversion exist in the engine but stop at the chamber door; the *broglio* (channeled-not-eliminated maneuver) and "fiat displaces contest to the antechamber" are absent. This is the **richest churn the system forgoes**.

3. **Bargaining is collapsed to a tug-of-war.** Parliament, "Private Negotiation," and the Compromise zone all resolve on the same zero-sum track — there is no axis on which both sides gain, no ZOPA, and the coalition Lead is answerable to a shared dice pool, not a faction **win-set** (Putnam's two-level game is structurally absent). The spec itself defers "Negotiation (ZOPA-style) — structurally different from the Persuasion Track, not designed."

4. **Three resolution families are missing or inert.** No **alea** (sortition/lot as an anti-capture device) anywhere; the system reaches for *inert non-results* ("referred to committee," "cold equilibrium" freeze) exactly where history reached for the lot. No unified **mimicry/acclamation** resolution mode. No **Type-3** procedure (consensus/unanimity with a holdout) — so the liberum-veto pathology class, the research's richest churn generator, is unreachable.

5. **The contest has no commitment store.** Across exchanges only *scalar attrition* persists (track, strain, Concentration, one transient Doubt Marker). The thing the research names as **the** granular substrate of argument — a ledger of conceded/committed propositions that makes later contradictions costly — does not exist. "Concede a Point" even *names* the canonical commitment move and does its opposite (a tempo bribe that records nothing). A contest is dice-margin attrition on a bar, not an exchange of commitments.

**None of this requires redesigning a mechanic.** The work is unification: point the existing armature at the adjudicator, lift the existing faction-split / Offer / Obligation tables into new modes, and **propagate ratified-but-stranded design** (see §5) into the live spec. Recommendations are ranked and tagged **free-win / structural / needs-your-call** in §6.

---

## 1. The meta-finding: one game superbly built, three games collapsed into it

> **A deliberative procedure can do four things — crown a winner, strike a bargain, discern a truth, enact a unity — and Caillois sorts the play into four families — agôn, alea, mimicry, ilinx. Valoria builds a mature *agôn* and routes the other three games and the other three families through it.**

The proof that this is *under-configuration, not incapacity* is that the engine already escapes the agôn in four places, all verified sound:

- **Wager Obligations** (§6.1) are a correctly-built *mixed-motive* instrument: the winner forgoes an immediate decisive outcome to extend present trust against a future verifiable condition — both parties prefer the cooperative path. The game-theoretic sense, done right.
- **Succession faction-split** (§7.2.1) is exemplary *pathology-as-churn*: a hung succession does not terminate, it **bifurcates the political map** and mints a new actor whose identity is read off the loser's Conviction via the armature. "The failure mode seeds the next arc," rendered mechanically.
- **Obligations + NPC-priority-tree binding** (§6.1) are a faithful "rule of recognition" output: a win **narrows the opponent's reachable action set** for a clock's duration and is remembered across generational succession. This is the robust-action payoff as a live game-state object.
- **Adjudicator-type → primary-attribute** (§3) cleanly maps Aristotle's three kinds of judge: Expert Judge tests Cognition, Crowd tests Charisma, No-adjudicator tests Attunement. The *kind* of venue reshapes *which* faculty the contest tests.

So the engine can hold bargains, generative pathology, durable commitment, and judge-sensitivity. It simply does each in *one* corner and runs the default path as pure agôn. Everything below is "do what §6.1/§7.2.1 already prove, everywhere it belongs."

**Where this meets your axiom.** Bottom-up-emergent + top-down validation is *satisfied for the agôn*: per-exchange sigma rolls accumulate on the track and emerge into a binding Obligation, validated top-down by the adjudicator threshold (Formal/Grand Contest is a clean Type-1 "the contest IS the deciding" engine). The debt is that the **substrate is too coarse** (it integrates dice margin, not a propositional record — §5 below) and the **top-down validator is a scalar, not an armature** (§2.1). Fix those two and the four-into-one collapse mostly dissolves, because the *meaning* layer (your second primitive) is what distinguishes bargain/truth/unity from victory.

---

## 2. Structural findings, ranked by leverage

Leverage shown is the **verifier-corrected** value (every finding was adversarially re-checked against the working tree; 0 of 38 were refuted, 9 were downgraded as overstated, 2 as already-handled). Full evidence with verbatim quotes is in `findings.json`.

### 2.1 — HIGH · The adjudicator should be an armature, not a number *(the central bottom-up violation)*

The adjudicator declares the verdict but, after type-selection, contributes only `resistance = avg-faction-Stability − 1` plus one `+1D` faction-boost die. The avg-Stability scalar answers *"how hard is this room to move"* but never *"what moves this room."* Meanwhile the engine **already runs** the exact primitive needed — the armature dot-product — and **already aims it at the opponent** (Resonant Style targeting maps Precedent/Suppression/Vision/Insinuation onto the target NPC's Conviction vulnerability, with `+1D` and effects on confirmed match). It is pointed at the party you *defeat*, not the party who *rules*.

- **`adjudicator FG-2` (high):** give each third-party adjudicator (Crowd, Expert Judge, Panel) an `armature_position` computed from its Convictions exactly like any NPC; at resolution, dot-product the chosen argument's style against it and convert alignment into a **resistance delta** (reusing the per-exchange erosion machinery — no new bucket). The `+1D` faction-boost becomes the *degenerate row* of this. The one real design task is a 4-style × 4-axis projection map (Class B, PP-674-vetted); gate it off when adjudicator == opponent (asymmetric proceedings) to avoid double-counting Resonant Style. Closes **SIM-DEBT-04** in the same pass.
- **`adjudicator FG-3` (medium):** generalize Resonant Style targeting's target set from `{opponent}` to `{opponent, adjudicator}` for Expert-Judge contests (where the adjudicator is a named NPC with a real Conviction). Extend the Overwhelming-Appraise reveal to surface the *judge's* primary Resonant Style; a confirmed match lowers effective resistance. **Appraising the judge** (not just the opponent) becomes a meaningful recon move — the recon-and-tailor loop the research says deliberation is.
- **`adjudicator FG-4` (medium):** add a **sanior-pars** move. A *decisive loser* currently has no in-system way to challenge a verdict's legitimacy — only to violate the Obligation (framed as breach, not as a quality-over-quantity claim). Let a decisive loser convert the Obligation clock into a **Legitimacy claim** seeded at the verdict margin, resolving via a follow-up contest before a *different* adjudicator armature (reuse §7.2 + §6.3 + the clock bucket). Constrain so it doesn't undo the deliberate finality §7.1 built for Church proceedings.
- **`adjudicator FG-5` (low, already-handled):** Panel is provisional (ED-137 → "use Expert Judge"). The groundup engine (`2026-06-03-contest-groundup`) **already has a built, validated Panel** (per-member aggregation, `deliberative_body_venue`, VoteAtClose with per-juror variance — the cross-judge split that is the whole point). This is a **propagation** task ("closes ED-137 for free"), not new design; resolve it on the sigma resolver (per-member fan-out), *not* the armature dot-product.

### 2.2 — HIGH · The procedure itself should be contestable *(the meta-game / capture / the antechamber)*

The deepest political act in the research is **choosing which game legitimates power** (Hart's rule of recognition). Valoria fixes adjudicator type, exchange count, genre-of-record, resistance, and boost at GM setup — "players merely learn the format." The single most consequential variable is removed from agency, and the displaced-venue maneuver (a private appeal going public) is *dropped on the floor* ("the current contest ends and a new contest begins").

- **`meta-game FG-1` (high):** add a **Procedure Contest** — one sigma-A exchange *before* Step 1 that sets a disputed setup parameter (genre-of-record and/or adjudicator type) toward the winner's preference, ties to the institution's default. Reuse the §10/§11 lobbying-offset precedent. Replace the automatic "private→public = new contest" reset with a player-triggerable **Venue Shift** that costs a forfeited first exchange — so forum-shopping has a price and generates capture/legitimacy churn. Make genre-of-record a recorded §2 Step 6 stake.
- **`meta-game FG-2` (medium):** **no adjudicator-capture lever.** Disposition (−5..+5) and the Subversion DA exist but never reach inside the contest — a council cultivated to +3 adjudicates identically to one at −3 (this is the verified-by-grep gap G-7). Bind adjudicator Disposition into the *existing resistance channel* (`floor(Disp/2)`, Lobby-Cap-bounded), and add an **Expose Capture** Appraise check that voids the bias and fires Reputation/Disposition fallout — capture made high-value *and fragile* (a capture exposed mid-contest is premium scandal churn). Pin to the ED-137 Panel stub for the recuse/seat case.
- **`meta-game FG-3` (medium):** **no robust-action / multivocality lever.** Every exchange forces full commitment (genre AND orientation) — maximal legibility, the posture robust action *avoids*. Add an **Equivocal** stance (3rd orientation): forfeit this exchange's movement, bank an actor-state token, and at post-contest declare alignment with the winning side (reuse the Wager deferred-resolution pattern; one per contest). Seeds the "ally who was never quite committed" / "speech everyone heard differently" arcs.
- **`meta-game FG-4` (medium, partly already-scattered):** the *broglio* is a `+1`-per-DA scalar capped to 4–6, BG-only. **Credit:** the Lobby Cap correctly models maneuver-as-advantage-not-fiat (Venice channeling, not eliminating). But the personal-scale vote-soliciting layer already exists *scattered* across UI/audit/proposal docs (W-02 lobbying scene; Parliamentary Intent H-5) and was never consolidated into the contest spec; coalition-poaching is the inverse of the existing coalition-collapse trigger. **Consolidate** those by reference; the one genuinely-novel piece worth building is the **displacement loop** — a fiat-advantaged win (Tribunal start-7, Royal Audience) opens an antechamber clock granting the loser a one-time future benefit ("fiat displaces, not eliminates").

### 2.3 — HIGH · Bargaining is collapsed to a tug-of-war *(mixed-motive / ZOPA / two-level games)*

Negotiation is the strictest game-theoretic game *and precisely not* zero-sum: parties cooperate to create a surplus and compete over its division. Parliaments are **supply-for-redress** bargains where both sides can gain. Valoria runs all of it — Formal/Grand, BG Vote, Hybrid, and the named "Private Negotiation" type — on the one 0–10 track where every unit A gains, B loses.

- **`mixed-motive FG-1` (high):** add a **Negotiation mode** as a parameterization of the existing contest, not a new engine. The sigma track sets each side's BATNA/reservation point; borrow the **Recruitment Offer table** (`npc_behavior §9.5 Step 3` — already a working integrative primitive, currently stranded in Recruitment) so a tabled Offer spends a faction-stat delta to lower the *other* side's Argue-Ob (widening ZOPA through the existing Ob channel). A deal in the overlap pays each side its split via the **§7.2.1 track-distance weighting** (60/40, 55/45, 50/50). No-deal falls back to the zero-sum track. Reuses sigma-A + Offer + Disposition + the §7.2.1 table + §6.1 Obligations — *zero new engine*.
- **`mixed-motive FG-2` (high):** **Putnam's two-level game is absent.** A coalition is just a summed Concentration pool + a rotating Lead; nothing the Lead concedes can be repudiated at home. Give each member a **win-set** (outcomes that don't contradict an active Belief or push Disposition below threshold) and run a cheap **ratification check** (sigma Instance-B) before the Obligation binds; a deal outside a member's win-set triggers the existing defection path or withdraws their pool share. Vaynard's Belief 3 ("I will not surrender my vote without [concession]") is a textbook win-set written into the fiction with *no mechanical home* — this gives it one. Pure churn engine (oversell-then-repudiate; the holdout backbencher).
- **`four-games FG-1` (medium):** the **Compromise zone is a "nobody won" default** — no Domain Echo, routed to a Chain re-match. **Generalize §7.2.1's split:** where stakes name >1 divisible axis, the 4–6 band becomes a proportional *trade* (genre-won attribution decides who keeps which axis), emitting a bilateral Obligation pair. (Verifier note: §7.2 Succession *already* does this where stakes are divisible, so this is "lift an existing mechanic," and Compromise is not uniformly inert — it carries Disposition/Scar state and a Scene-Slate crisis.)
- **`mixed-motive FG-3` (low):** **no Priest-Klein selection gate** — a hopeless case still runs the full contest. Add a one-roll **lopsidedness gate** (sigma Instance-B) at setup: if leverage gap exceeds a band, the contest doesn't open — the stronger side imposes / the weaker extracts one Obligation (reuse §6.1; *not* a non-existent "Offer table"). Relocates story to settlement/side-payment instead of burning table-time on a foregone conclusion.

### 2.4 — HIGH/MEDIUM · The missing resolution families *(alea, mimicry, Type-3, pathology-as-churn)*

- **`contest-locus FG-3` (high):** **no Type-3 procedure.** RM and the Wardens are explicitly *consensus* institutions and the Succession table even lists "RM: by consensus" — but "by consensus" is a label that collapses straight back into the Mandate-weighted sigma vote. There is no unanimity threshold, no single-actor **holdout/veto move inside a contest**, no sortition. Add a thin **Consensus Proceeding**: per-required-assenter flags resolved by sigma rolls; a lone holdout mints a "Holdout" Obligation clock + Scene-Slate entry (the liberum-veto pathology becomes the plot); an **anti-gaming antibody** (a frivolous block — armature dot-product below threshold — costs Mandate, mirroring the existing Sacred-Veto self-interest cost). This is the largest unreachable pathology class on the churn axiom.
- **`caillois FG-4` (medium, *low effort*):** **no alea/sortition anywhere** — the only randomness is intra-agôn dice noise. The system reaches for *inert non-results* exactly where history reached for the lot: BG "referred to committee" and chain-Deadlock "cold equilibrium" freeze. Replace both with a **weighted lot** (Mandate/Track-weighted — the doge pattern, not a coin flip), seeded per-Key-emission so it's replayable. Converts two inert sinks into churn ("the dice chose wrongly"; the leader nobody fully backs). Low effort — reuses the RNG already in `contest.py` and the existing seeding rule.
- **`caillois FG-3` (medium):** **no unified mimicry/acclamation resolution mode.** The "Crowd" adjudicator is just a Charisma attribute-swap inside the same agôn kernel, so a parliamentary acclamation and a tribunal verdict resolve by identical math. Add **ACCLAMATION** as a *pluggable win-condition* on the Crowd adjudicator (the 2026-06-03 audit's exact lever): one armature-dot-product pass over present adjudicator-NPCs weighted by Mandate/Disposition; supermajority → passes in one evaluation. A *failed* acclamation falls through to the standard track with a starting penalty — the "hollow acclamation" / pretender-and-usurper churn agôn cannot produce. (Verifier note: Varfell's Jarl-Assembly acclamation *already exists* in `faction_politics`; this unifies it as a resolution mode rather than inventing it.)
- **`caillois FG-2` (medium):** **succession is hard-coded agôn** where history shows alea/mimicry. Don't add a "mode selector"; add a **WeightedDraw win-condition** to the already-in-flight pluggable-win-condition work (groundup `modes.py`) so Crown/doge-type succession runs a shortened qualifying contest then a weighted lot among the top-2 — the anti-capture property (a strong claimant can't guarantee the throne → factions must hedge → churn). Varfell (acclamation) and Löwenritter (merit-agôn) keep their existing paths.
- **`contest-locus FG-4` (low, overstated):** the **cold-equilibrium terminator** is the single most anti-churn line in the spec (freezes Disposition *and* locks the topic 4 seasons). Re-point *that one line*: emit a standing Deadlock Obligation clock and let Disposition keep drifting, instead of freezing. (Verifier note: §6.3 is otherwise a churn-*generator*, and deadlock-as-engine already exists at Arc 18 / Edeyja Arc A — so this is one line, not a section rewrite.)
- **`caillois FG-5` (low):** **ilinx** (crowd-charge that *bypasses* weighing) is absent — Charisma-as-pool is still agôn (higher Charisma wins *more reliably*; ilinx is the surge that carries a *weak* case). Optional: a **Fervor clock** on Crowd contests that, at threshold, fires a one-shot Track jump toward the surging side (reuse the §9.4 Track-co-movement pattern; clock → Track, both canonical). The "room got carried away" consequence class.

### 2.5 — MEDIUM · The contest has no commitment store *(the granular substrate)*

The least-disputable correspondence in the research: real argument is a **move-and-commitment structure** with a running ledger of conceded propositions that legal moves alter, and validity/truth are *defined* as a winning strategy over that ledger. Macro-structure **emerges** from this granular substrate — it is precisely the bottom-up substrate your axiom calls for.

- **`commitment-store FG-1` (medium, *effort high*):** across exchanges the contest persists only scalar attrition (track, strain, Concentration, one transient Doubt Marker); argument *content* is consumed for dice bonuses and discarded. A side can argue Precedent in exchange 1 and Suppression of the same fact in exchange 3 with **zero friction** — nothing leaves a propositional trace, so contradiction-traps and forced retractions (the richest argumentative churn) are *structurally impossible*. Add a per-side append-only **Commitment Store** as a clock-class ledger the sigma resolver reads (the report already classes the track and Evidence Track as clocks — this is the same bucket). Two hooks via existing math: **CONTRADICTION** (arguing against your own committed entry → `−Xd` to your pool, channel-correct per PP-716; opponent who cites it gets the Recall `+2D`) and **CONCESSION** (writes the opponent's proposition into your store; thereafter unavailable to you, `+1D` to them when invoked). This is the engine-disciplined answer to the report's own Rec #4 "verify social_contest on the sigma kernel."
- **`commitment-store FG-2` (medium, rider on FG-1):** **"Concede a Point" is a hit-point bribe, not a recorded concession** — it uses the canonical commitment-store word for its functional opposite (the `+1D` rebound makes conceding an *attack*). If FG-1 lands, re-spec it to write the conceded proposition into both stores. If not, the zero-cost honesty fix is to **rename it** ("Yield Ground") so the system stops claiming the Walton-Krabbe primitive it doesn't implement.
- **`commitment-store FG-3` (low, overstated):** the **Doubt Marker is the embryo of a commitment store** collapsed to a singleton transient `−2`. Minimal version (no proposition-objects): allow >1 active marker, and surface unconsumed markers as durable residue (Suspicion Token / `−1` Disposition) instead of vanishing. (Verifier note: durable residue mostly *already* exists via Obligations/Scars/Suspicion Tokens — this is polish.)

### 2.6 — MEDIUM/LOW · Eristic has no cost; the fouls layer is thin

Pragma-dialectics: a fallacy is a **foul** (a rule-violating move penalized within the game), and the healthiest deliberation is treated *least* as a contest to win.

- **`fallacies FG-2` (high leverage, *low effort* — propagation):** **the named shady styles are pure-upside.** An Obscuring win places a Doubt Marker on the opponent at *no self-cost*; where the audience boosts Obscuring (Church) it is `+1D` plus a free debuff — eristic as optimal play, with no "caught-in-a-lie" seed. The fix is **already ratified and stranded**: propagate **CR5** (`2026-06-01-contest-redesign`, ratified-but-not-applied) — Indirect/Obscuring attacks opponent Face *with self-Face backfire on failure*, F7 self-gating. Low effort, high coherence payoff.
- **`fallacies FG-3` (medium, overstated):** **no foul-mirror for a fabricated citation** (Recall rewards a verified claim; nothing penalizes a fabricated one — logged P2 sim-debt), the genre-dodge is a no-strain CROSS, and the orphaned "Suspicion Token" (contest_extensions) collides with the Doubt Marker rename (ED-897). Two repairs: (1) terminology — fold "Suspicion Token" into the canonical Doubt Marker; (2) reuse the existing **Appraise** roll as a fabrication-detection channel (success voids the Recall `+2D` and lands a Doubt Marker on the citer), scoped to adjudicated proceedings per the §9.4b visibility-gate pattern.
- **`four-games FG-2/FG-3/FG-5` (low / already-handled):** the eristic-cost and "discern-a-truth" concerns are *mostly already handled* — **Belief Revision** (`npc_behavior §3.2`: decisive + correct Resonant Style + Belief engagement → the loser is *persuaded on the merits*) already provides the inquiry game, and the merit channel exists as a **reward gradient** (substance unlocks durable Scars/Belief-revision; nastiness unlocks only ephemeral Doubt Markers). The residue is narrow: close the `state.belief_revised` Key emission (ED-937 / workplan #32) so the conversion reaches the chronicle, and optionally apply the existing **Sincerity Gate** so an instrumental win can't fake a conversion. Editorial, not structural.

---

## 3. What is already right (credit — these are the model for the rest)

Eleven strengths verified sound. The five that matter most as *patterns to imitate*:

1. **Formal/Grand Contest is a clean Type-1 bottom-up-emergent engine** — per-exchange sigma rolls → track → Obligation, validated top-down by the threshold. Your axiom, satisfied.
2. **Obligations + NPC-priority-tree binding** — a win narrows the opponent's *reachable action set* and is remembered across generations. The robust-action payoff as a live clock. *This is the model for everything in §2.*
3. **Succession faction-split (§7.2.1)** — the one place a non-decisive outcome is *generative* (bifurcates the map, mints an armature-read actor). Proof pathology-as-churn is a *capability*, so its absence elsewhere is a *choice*.
4. **Wager Obligations** — a correctly-built mixed-motive / trust-extension instrument. Proof the engine is not intrinsically agonistic-only.
5. **Adjudicator-type → primary-attribute** — Aristotle's three judges, near-direct. (The honest caveat: it stops at *which faculty*, never *what content* moves the judge — which is exactly §2.1.)
6. **Appraise-first exchanges** — the correct *read* primitive (model the opponent/audience each exchange). The read half of a commitment-store dialogue exists; the recorded-commitment half it should be reading (§2.5) does not.

---

## 4. The throughline: two primitives, both under-used at the seam

Echoing the 2026-06-28 distillation report: the engine has exactly two universal primitives — the **sigma resolver** (will + advantage → outcome) and the **armature dot-product** (event → meaning-for-an-observer). The social contest is a mature consumer of the **first** and an almost-non-consumer of the **second**:

- The sigma resolver runs every exchange. Good. The gaps here are *what it reads* (a commitment store, §2.5) and *what win-condition it terminates on* (alea/acclamation/consensus/negotiation are all **pluggable win-conditions** on the same kernel — §2.3, §2.4).
- The armature dot-product runs against the *opponent* (Resonant Style) but **never against the adjudicator** (§2.1) — the contest's defining observer. Pointing it there is the single highest-leverage, most engine-disciplined move available, and it is what makes the four-into-one collapse dissolve: the *meaning* layer is what tells a bargain from a victory from a discerned truth.

Net: this critique is the same shape as the distillation report — **unification and seam-closure, not redesign.** The contest doesn't need new mechanics; it needs its two primitives pointed at the parties and outcomes they already imply.

---

## 5. Already designed, just stranded (propagate, don't invent)

A striking amount of the "fix" is **propagating ratified-but-unpropagated design** into the live spec. Verification surfaced four such bodies:

| Stranded design | Where | Closes |
|---|---|---|
| **CR5 self-Face backfire / F7 self-gating** (eristic cost) | `2026-06-01-contest-redesign/RATIFIED_2026-06-01.md` ("not yet applied") | `fallacies FG-2`; the eristic-has-no-cost gap |
| **Pluggable win-conditions** (TallyAtClose / VoteAtClose / GraceThreshold / ceremonial-acclamation) + **built Panel model** | `2026-06-03-contest-groundup/` (`modes.py`, `contract.py`) | `caillois FG-2/FG-3`, `adjudicator FG-5` (ED-137), Type-3 win-conditions |
| **`state.belief_revised` Key emission** from contest Belief Revision | `key_type_registry_v30 §899` stub (ED-937 / workplan #32) | `four-games FG-3` (inquiry reaches the chronicle) |
| **Sincerity Gate** (Spirit TN7 Ob1, `[INSTRUMENTAL]` tag) | `investigation_systems` / `fieldwork §5.3` | sincerity-guards the conversion and the foul layer |

Doing these is *coherence work*, not new design — and it should ride the existing CR1–CR7 / groundup propagation rather than landing as standalone bolt-ons.

---

## 6. Ranked recommendations

| # | Recommendation | Lens | Leverage | Effort | Tag |
|---|---|---|---|---|---|
| 1 | **Point the armature dot-product at the adjudicator** — adjudicator gets an `armature_position`; alignment → resistance delta; faction-boost becomes its degenerate row. Close SIM-DEBT-04. | adjudicator FG-2/3 | ★★★★★ | med | structural |
| 2 | **Make the procedure contestable** — Procedure Contest (genre/adjudicator) + Venue Shift + adjudicator-capture via Disposition→resistance with an Expose-Capture check. | meta-game FG-1/2 | ★★★★★ | med | structural |
| 3 | **Negotiation mode + coalition win-sets** — reuse the Recruitment Offer table + §7.2.1 split for ZOPA; give coalition members a ratification check (Putnam two-level). | mixed-motive FG-1/2 | ★★★★★ | med–high | structural |
| 4 | **Add the missing win-conditions** — sortition (weighted lot replacing the inert "committee"/"cold-equilibrium" sinks), acclamation, consensus/holdout — as pluggable terminations on the sigma kernel. | caillois FG-3/4, contest-locus FG-3 | ★★★★ | low–med | structural |
| 5 | **Add the in-contest commitment store** — append-only clock-class ledger; CONTRADICTION (`−Xd`) + CONCESSION hooks; re-spec "Concede a Point." | commitment-store FG-1/2 | ★★★★ | high | structural |
| 6 | **Propagate the stranded design** (§5): CR5 eristic backfire; groundup Panel + win-conditions; `belief_revised` Key; Sincerity Gate. | fallacies FG-2, adjudicator FG-5, four-games FG-3 | ★★★ | low | free-win |
| 7 | **Re-point the inert terminators at generation** — cold-equilibrium → Deadlock clock; sanior-pars verdict-contestation for decisive losers. | contest-locus FG-4, adjudicator FG-4 | ★★ | low–med | free-win |
| 8 | **Optional richness** — Equivocal/multivocality stance; Fervor/ilinx clock; Priest-Klein lopsidedness gate; antechamber displacement loop. | meta-game FG-3, caillois FG-5, mixed-motive FG-3, meta-game FG-4 | ★★ | med | needs-your-call |

**If you do only three:** #1 (the adjudicator armature — the central bottom-up fix), #4 (the missing win-conditions — turns inert sinks into churn for low effort), and #6 (propagate what's already ratified — nearly free coherence). Together they undo most of the four-into-one collapse without touching the agôn that already works.

---

## 7. Do-not-touch (load-bearing — preserve through any change)

- **The bidirectional Persuasion Track and the Appraise-first exchange** (distillation do-not-touch list): the right substrate for the *distributive* contest and the *read* primitive. The fixes above build **on** these, never replace them.
- **Obligations-as-clocks + NPC-priority-tree binding** (§6.1): the model for durable, emergent, churn-seeding output. Imitate it; don't dilute it.
- **The two-primitive discipline:** every fix here reuses the sigma resolver or the armature dot-product. Reject any "fix" that adds a parallel resolver — the corpus's own adversarial verdict is that the social and combat engines correctly *diverge at the resolution atom* (CROSS / Compromise / stall must survive); do **not** force "one resolver to rule both."
- **The deliberate finality of Church proceedings** (§7.1 "the counter is preventing the filing"): the sanior-pars and capture levers must be constrained so they don't dissolve the asymmetric-proceeding design intent.

---

## 8. Method, honesty, and provenance

- **Lenses:** 8 theoretical lenses (four-senses / commitment-store / Caillois-families / contest-locus-and-Type3 / meta-game-capture / adjudicator-armature / fallacies-as-fouls / mixed-motive-bargain), one analyst each, grounded in the 6-document research corpus and judged against the bottom-up-emergent + churn philosophy and engine discipline.
- **Verification:** every one of 38 raised findings was adversarially re-checked against the live working tree, with the verifier specifically tasked to find where a claimed gap is **already handled elsewhere** in the (large) corpus. Result: **0 refuted, 16 sound, 9 overstated (leverage reduced), 2 already-handled.** Leverage and improvements in this document are the *corrected* values. This is why several research-strong findings (eristic cost, inquiry, Panel) are demoted to "propagation/editorial" — the engine already does more than a first pass assumes.
- **Honest limits:** (a) this is a *design* critique, not an internal-consistency audit — for spec-vs-params-vs-sim contradictions, the intended instrument was `tools/observability/social_contest_audit.workflow.js`, retired 2026-07-11 (ED-IN-0033, never executed, stale paths post-contest-rebuild) to `deprecated/tools/observability/`; the SC lane's ratified Fable-5 subsystem audit (`designs/audit/2026-07-05-fable5-social-contest-audit/`) now covers this ground instead. (b) The research corpus is itself self-flagged as a graded, comparative claim ("X *is* a game" only in specific senses) — the four-senses taxonomy is a *generative lens*, not a natural kingdom; findings are weighted accordingly. (c) Improvements are proposed at design altitude; lever magnitudes (thresholds, deltas) are starting values for sim-validation, not canon.
- **Artifacts:** full verified findings with verbatim quotes and per-finding verdicts in `findings.json`; workflow script at `.claude/wf_social_contest_critique.js`.
