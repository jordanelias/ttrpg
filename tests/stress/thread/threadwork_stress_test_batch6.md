# THREADWORK STRESS TEST — BATCH 6
## Session: d8b924fb834a398c | Date: 2026-04-16 | Effort: MAX
## No repeats from Batches 1–5.
## New lens this batch: every finding evaluated against robust / elegant / smooth definitions.
##
## ROBUST = strategic thinking + customization + creative variety + world impact + emergent without player
## SMOOTH = clean integration, no friction, good transitions between systems, clean zoom in/out
## ELEGANT = logically simple, clear approach, no unnecessary overhead

---

# 1. THREE-AXIS OB SYSTEM — ELEGANT FAILURE AT THE TABLE

## 1.1 Per-Operation Lookup Cost [ELEGANT — FAILS]

The three-axis Ob system (PP-622/PP-623): Total Ob = Depth Ob + Breadth Ob + Distance Ob. Each axis requires a table lookup:
- Depth: 6-row Fibonacci table (Object/Personal/Relational/Field/Structural/Foundational)
- Breadth: 5-row table (Single/Small group/Formation/Battlefield/Regional)
- Distance: 4-row table (Contact/Near/Distant/Far)

**Three table lookups per Thread operation, every operation, every contact window.** In a combat scene where the practitioner has Focus 4 (3 operations): 9 table lookups for Ob construction alone — before rolling a single die.

Compared to: Combat pool construction (one formula, pre-calculated on character sheet). Social contest Argue pool (one attribute × 2 + History). Fieldwork pool (same formula).

**[ELEGANT — FAILS]** Three-axis Ob is the most cognitively expensive pool construction in the game. It violates the elegant definition: "no unnecessary overhead." The overhead IS necessary (the three axes capture meaningful dimensionality) but the lookup mechanism creates table-juggling at exactly the moments requiring the most tactical focus (combat, contested Thread ops, mass battle).

**Mitigation check:** Practitioners would pre-calculate common operation profiles (e.g., "my standard Relational Single Contact Weave = Ob 3+0+0 = 3, always"). Only novel configurations (new breadth, new distance, unfamiliar depth) require full lookup. Pre-calculation on the character sheet reduces per-session overhead significantly. This is an elegant *mitigation* of an inelegant system — acceptable but should be flagged as a UX design debt.

**Required:** Character sheet section for "pre-calculated Thread operation profiles" listing player's most common operations with total Ob pre-summed. This converts the three-lookup problem into a one-lookup problem for prepared practitioners.

## 1.2 Mending Depth Ob as Separate Column — Overhead Without Value [ELEGANT — FAILS]

params_threadwork Depth table has a separate "Mending Ob" column (Depth Ob − 1 for each tier). Foundational: Ob 13 standard, Ob 12 for Mending. Field: Ob 5 standard, Ob 4 Mending.

**The Mending Ob column is just "Depth Ob minus 1."** It adds a column and increases table reading time without conveying information not already captured by the rule "Mending Depth Ob = Depth Ob − 1." The column is a computation result, not a rule. At the Foundational tier, the note "−1 reduction remains but the base is 13" requires reading the column AND the footnote AND the rule to understand why Ob 12 instead of 12.

**[ELEGANT — FAILS]** Remove the separate Mending Ob column. Replace with a single-line rule: "Mending Ob = standard three-axis total − 1 (Mending works with substrate's self-repair tendency)." This is the existing rule, cleanly restated. The column is reference material that creates a false impression the Mending Ob is independently derived rather than derived from the standard.

---

# 2. THREAD-READ → EVIDENCE TRACK — SMOOTH INTERACTION BUT ROBUST CONCERN

## 2.1 Thread-Read Dumps Evidence at Maximum Fieldwork Bonus [SMOOTH — OK; ROBUST — CONCERN]

Fieldwork_v30 (from available text): Thread operations contribute to Evidence Track advances:
- Pulling (standard): +2 (Success), +3 (Overwhelming)
- Past-Oriented Pulling: +2 (Success), +3 (Overwhelming)
- Locking: +1 preservation; +2 if resistance reveals structure
- Dissolution: +2 if concealment destroyed; +1 from Gap topology
- Mending: contribution noted (text truncated)

Thread-Read specifically: "the only fieldwork action that constitutes a Thread operation." As a Leap (TS ≥ 30, Spirit-primary pool), Thread-Read produces evidence at Thread-operation rates.

**Smooth check:** Does Thread-Read integrate cleanly with the Evidence Track? Apparently yes — the fieldwork doc explicitly defines Thread operation evidence contributions. The handoff between Thread-Read (personal operation) and Evidence Track (investigation system) is designed, not accidental. **[SMOOTH — OK]**

**Robust concern:** Pulling at Personal scale on a target's memory: +2 Evidence (Success). A POP: +3 Evidence (Overwhelming). A non-Thread investigator using standard investigation: how many successes for +2 Evidence? If non-Thread investigation produces +1 Evidence per Overwhelming: **Thread operations are roughly 2–3× more efficient at generating Evidence than mundane investigation.**

A practitioner investigator can short-circuit the Evidence Track by performing a series of Thread operations (each advancing Evidence 2–3 points) rather than methodical fieldwork investigation. The Evidence Track thresholds (3/5/8) can be reached in 1–3 Thread operations rather than the multi-scene investigation arc they're designed to require.

**[ROBUST — CONCERN]** Thread-Read as investigation tool may be too efficient at Evidence generation. If the goal is for investigation to be a multi-session arc (rich, varied, methodical), Thread-Read that produces +3 Evidence per Overwhelming compresses this into a single contact window. **Mitigation:** Thread-Read evidence should be gated: "Thread-Read evidence advances the Evidence Track only for questions at Depth ≥ 4 (Liminal) — questions inaccessible to mundane investigation. For Depth 1–3 questions, Thread-Read provides flavor but no Evidence Track advance; mundane investigation governs." This preserves Thread-Read's unique value (accessing Depth 4–5 evidence) while keeping Depth 1–3 investigation as fieldwork's domain.

---

# 3. LEAP PRIORITY 5 + MULTI-ENGAGEMENT — SMOOTH FAILURE

## 3.1 Practitioner Leaping While Multi-Engaged Has No Pool Split Resolution [SMOOTH — FAILS]

Combat: "Priority 5 — Leap (Thread — full-round). Only reactive defence available during Leap round."

PP-274 (Multi-engagement): "Target declares one Offence/Defence split; both attackers roll against same Defence allocation."

**Combined scenario:** The practitioner is engaged by two opponents. At Priority 5, they declare Leap. "Only reactive defence available during Leap round." Their entire pool is committed to defence — they cannot allocate Offence. But PP-274 says the target declares ONE Offence/Defence split, and both attackers roll against the same Defence allocation.

If the practitioner must commit 0 to Offence (full defence, Leap constraint): they allocate all pool dice to Defence. Both attackers roll against this full Defence. This is correct. But "full-round action" language implies the Leap itself consumes the entire action — the practitioner has no pool available for Defence either.

**The conflict:** Is the Leap round's "reactive defence only" meaning:
(a) The practitioner can still allocate pool dice to Defence normally, but cannot Offend — they split 0/N?
(b) The practitioner has no pool at all during the Leap round (the Leap is the action) and can only apply passive defensive bonuses (armour, position)?

**[SMOOTH — FAILS]** The Leap round combat sequence is undefined for multi-engaged practitioners. Option (a) is implied but not stated. Option (b) makes the Leap round catastrophically dangerous (no defence pool at all). Given PP-274's "target declares one Offence/Defence split," the practitioner under Leap must still have a Defence allocation. But the Leap round costs the full-round action. Ruling required: "During the Leap round, the practitioner allocates their full pool to Defence (0 Offence). Attackers roll against this full Defence allocation per PP-274."

## 3.2 Fibonacci Group Bonus vs Practitioner in Thread Contact [SMOOTH — FAILS]

Combat: Fibonacci Group Bonus applies to Offence dice only, based on attacker count. During Thread contact (rounds 2+), the practitioner cannot take offensive action — they can only take reactive defence. They have effectively 0 Offence pool allocation.

An attacking group of 3 opponents receives +2 Offence bonus dice (Fibonacci 3 = +2). But the bonus applies to "Offence dice only." If the practitioner in Thread contact is defending with full pool (0 Offence, all Defence): the Fibonacci bonus is functionally uncapped vs. the practitioner — their Defence pool is fixed at whatever they have, and each attacker gets the group bonus against it.

**In multi-attacker vs Thread-active practitioner scenarios: the practitioner is increasingly disadvantaged as attacker count grows.** A group of 4–5 attackers (Fibonacci +3) all rolling against the practitioner's full-pool Defence allocation, with no risk of Offence return, is effectively a death trap for any practitioner attempting sustained Thread operations in multi-attacker combat.

**[SMOOTH — OK, thematically]** This is intended — Thread contact in melee is dangerous. The mechanical interaction (Fibonacci bonus unchecked by practitioner Offence) is a smooth expression of the design intent. Surface as an explicit tactical note: "Thread contact in multi-attacker scenarios is tactically suicidal. Practitioners should ensure personal safety before Leaping."

---

# 4. DISSOLUTION RESIDUE TRACKING — ELEGANT FAILURE

## 4.1 Residue Requires Four Separate Tracking Values [ELEGANT — FAILS]

Per Dissolution Residue rules, a practitioner with accumulated Residue must track:
1. **Potency rating** (1–5): how many bonus dice the Residue grants.
2. **Source count** (for +1 Ob per prior use depletion): each use of the same Residue source degrades it.
3. **Coherence cap exemption status**: Residue use is a distinct Coherence event not subject to the §3.2 cap — must track separately from operation Coherence cost.
4. **Volatile dice behavior**: these dice explode on 9–10, requiring separate resolution from the standard pool.

**During an actual play moment:** The practitioner decides to use Residue. They must: look up current Potency (1), calculate +1 Ob per prior use this source (2), roll the volatile dice separately and apply explosion rule (4), then calculate Coherence cost as: operation Coherence + Residue Coherence as two separate cap-status items (3). This is four distinct mechanical actions layered on top of an already multi-step operation resolution.

**[ELEGANT — FAILS]** Dissolution Residue has the highest per-use overhead of any resource in the game. Mitigation: pre-print a Residue card with: current Potency, uses-remaining before depletion, and a checkbox for "used this contact window." This reduces to two lookups (Potency, use count) and one check. But the volatile dice (explode on 9–10) still require separate resolution — this cannot be simplified without changing the mechanic.

**Proposed simplification:** Remove volatile dice explosion. Instead: "Residue bonus dice succeed on 7+ AND chain on any 9 or 10 (instead of normal 10-only chain)." This gives the same flavor (Residue dice are more volatile/powerful) without requiring separate die resolution. The chaining behavior is part of the existing dice system; it doesn't add new overhead.

---

# 5. DOMAIN ECHO CHAIN — SMOOTH UNDER PRESSURE

## 5.1 Is Domain Echo Clean at Every Step? [SMOOTH — PARTIALLY FAILS]

Scale Transitions §3.4 (Scene → Faction / Domain Echo): a personal-scale action that meets "Sufficient Scope" thresholds echoes into faction-layer consequences. Threshold (§7): companion presence +1, Knot-sharing with faction-level NPC, investigation Finding naming faction leader.

**The Domain Echo chain for Thread operations:**
Personal Thread operation → sufficient scope met → Domain Action equivalent fires → Faction stat change.

What IS the Domain Action equivalent of a Relational Weave on provincial institutional bonds? The Domain Action system has: Govern, Trade, Fortify, Recruit, Suppress, Investigate, Deploy, Negotiate, Parliament, Coerce, Subvert. None of these map cleanly to "Weave relational bonds." The Weave's consequence at faction level is undefined.

**[SMOOTH — PARTIALLY FAILS]** The Thread → Domain Echo handoff has a category gap. Thread operations don't map to existing Domain Action categories. A Relational Weave that achieves sufficient scope should produce a faction consequence — but what? Proposed mapping table:
| Thread Operation | Faction-Level Domain Echo |
|---|---|
| Weaving (provincial loyalty) | Equivalent to Govern Success in that territory (Accord +0, but next Govern Ob −1 this season) |
| Pulling (institutional bonds) | Equivalent to Suppress Failure consequence (Stability −1 to affected faction) |
| Locking (configuration) | Equivalent to Fortify Success (specific to whatever was Locked) |
| Dissolution | Equivalent to Coerce Success OR Subvert Success (GM assigns based on target) |
| Mending | Equivalent to Govern Overwhelming in RS-damaged territory |
| POP | Unique — no Domain Action equivalent; create new category |

Without this mapping, Domain Echo for Thread operations requires GM judgment every time rather than a defined procedure. This is unnecessary overhead for what should be a clean zoom-out moment.

---

# 6. BELIEF CO-AUTHORSHIP AT COHERENCE 2 — UNMODELED HISTORY CONSEQUENCE

## 6.1 GM-Written Beliefs Still Reference Player-Selected Histories [ELEGANT — CONFLICT]

Coherence 2 (Fractured): "Belief Co-Authorship begins. Game Master presents the practitioner's shifting perceptual framework as the character's internal voice. Player must rewrite each Belief to reflect the framework in which the categories that structure consciousness are loosening."

Beliefs govern History bonus dice. Each History is tied to a specific domain (Einhir Architecture, Sword Fighting, Court Intrigue). When the GM co-authors the Beliefs at Coherence 2, they are rewriting the practitioner's Beliefs — but the History dice are still the player's, tied to their learned domains.

**Potential conflict:** A GM rewrites Belief 2 from "I must protect Vaynard's Archive" to "Knowledge flows through me but belongs to no one — I am its conduit." The player's History "Einhir Scholar" now applies to a Belief about universal knowledge conduit. Does the GM's rewrite of the Belief change which History applies? The History is a trained skill (accumulated experience), not a Belief-contingent resource. The Belief Co-Authorship should not affect History dice eligibility.

**But the Fragmented band also states:** "−1D to all Recall-based rolls." Recall governs how many points a History can hold (History points cap = Recall score). At Fragmented, Recall is reduced — meaning the practitioner's effective History pool is reduced. At Coherence 4, Recall −1D: the practitioner's per-History-roll performance drops, but their History capacity (Recall score as a stat, not a roll) is unchanged.

**[ELEGANT — CONFLICT]** The Fragmented band applies −1D to "Recall-based rolls." Is using History in a Thread operation a "Recall-based roll"? History is not the same as Recall — Recall is the mental stat that governs memory; History is the skill system. If Recall-based rolls include "any roll that uses History bonus dice" (because History IS recalled experience), then −1D applies to ALL Thread operation rolls (which use History). This would make the Fragmented band significantly more punishing than stated (−1D to all social AND all Thread ops, not just social and Recall-specific rolls).

**Required ruling:** "Recall-based rolls = rolls where the primary mechanic involves accessing stored knowledge (Recall attribute × 2 + History). Thread operations use Spirit, not Recall, as primary — they are NOT Recall-based rolls. −1D at Fragmented/Fractured applies to social rolls (Attunement, Cognition, Charisma primary) and explicit Recall-primary rolls, not Thread operations." Without this ruling, the Fragmented band's −1D cascades into Thread pools, making already-expensive Coherence loss significantly worse.

---

# 7. NPC PRACTITIONERS OPERATING WITHOUT PLAYER — ROBUST STRESS TEST

## 7.1 Can Thread Create Emergent Compelling Play Without Player Involvement? [ROBUST — PARTIAL]

Robust definition: "able to provide emergent and compelling play without player involvement." For Thread, this means: NPC practitioners operating autonomously should produce interesting world-state changes that the player discovers, not scripted events.

**NPC practitioner AI decision tree (inferred from available docs):** NPC Thread operations are governed by:
- NPC Stance Triangle (Conviction, Resonant Style) — determines operational goals
- Faction priority tree (Mandate → Influence → Military etc.) — determines urgency
- RS awareness (Batch 3: Church is structurally blind to RS; other factions are RS-visible with Investigate Thread orders)

**Where NPC Thread decision-making is undefined:**
1. When does an NPC practitioner choose to Leap? No decision threshold stated.
2. What scale does an NPC practitioner target? No priority given for Object vs Relational vs Structural.
3. How does an NPC weigh RS cost vs political gain? Undefined.
4. When does an NPC practitioner stop using Thread (to recover Coherence)? No recovery-threshold defined.

**[ROBUST — PARTIAL]** Without NPC Thread decision rules, autonomous NPC Thread operations are entirely GM improvisation — not emergent system behavior. A Varfell NPC practitioner who accumulates Coherence damage across several seasons has no defined behavior for when to begin Coherence recovery vs. continuing to operate. This means Thread's emergent play depends entirely on GM judgment, not mechanical output. Thread passes the robust test for *player-initiated* emergent play (the interaction effects are rich) but fails for *autonomous* emergent play (NPC practitioners have no AI spec).

**Required:** NPC practitioner decision rules (analogous to NPC governor AI in settlement spec §3.2). Proposed:
| NPC Coherence | Behavior |
|---|---|
| 10–7 (Stable/Dissonant) | Operate freely per Conviction priority |
| 6–5 (Dissonant-low) | Limit to Object/Personal scale operations; avoid FR |
| 4–3 (Fragmented) | Emergency operations only (direct threat to NPC or faction survival) |
| 2–1 (Fractured/Severed) | No voluntary Thread operations; seek Anchoring Scenes |
| 0 (Rendering Crisis) | GM takes character; faction must address crisis or lose practitioner |

---

# 8. CONCENTRATION TRACK — THREAD INTERACTION UNDEFINED

## 8.1 The Concentration Track Has No Thread Rules [GAP — OMISSION]

Clock registry: "Concentration | 2–14 | Focus + Recall | params_contest.md §Concentration."

Concentration is a social contest resource — the mental endurance for prolonged argument. It parallels Composure (social damage buffer) but for concentration/attention resources. Focus + Recall as its base suggests it is the practitioner's extended-attention capacity.

**Thread interaction:** Focus governs Contact Rounds in Thread operations. Recall governs History capacity. Both stats feed Concentration. A practitioner in Thread contact is spending their Focus resource on Thread engagement. Are they simultaneously spending Concentration on a social contest occurring in the same scene?

**Specific scenario:** A practitioner is in Thread contact (using Focus) while a social contest is happening in the same scene (using Concentration). Can a practitioner simultaneously maintain Thread contact AND participate in a social contest? The rules prohibit Offence in combat during Thread contact but say nothing about social contest participation.

**[GAP]** Concentration drain from simultaneous Thread contact has no ruling. If the practitioner can participate in a social contest during Thread contact (spending Concentration) while also performing Thread operations (spending Contact Rounds): the practitioner effectively multi-tasks between the social and Thread layers. This may be intended (Thread can prime social outcomes per Batch 3 §7.3), but the action economy is undefined.

**Required ruling:** "A practitioner in Thread contact may not participate as an active orator in a social contest during the same round (their full action is Thread contact). They may, however, provide Corroboration as a Helper orator (since Corroboration requires presence, not active participation). Concentration drain does not apply during Thread contact rounds."

---

# 9. LOCK ON A CLOSED GAP SITE — SUBSTRATE ARCHITECTURE EXPLOIT

## 9.1 Locking Substrate After Successful Mending [EXPLOIT — NOVEL]

After a successful Mending (Gap closes, RS +1 to +2), the substrate in that area is freshly repaired — its self-repair tendency has been assisted and the configuration is settled. The Mended area is "more than normally actualized" in the sense that it has been actively restored.

A practitioner could, immediately following a successful Mending, Lock the freshly-repaired substrate configuration:
- Target: the Mended area's substrate coherence — its resistance to future Gap formation.
- Ob: Field scale (the Mended area = a coherent local zone), Breadth 1 (Small group — the Mended configuration), Distance 0 = Ob 5+0+0 = **Ob 5, TN 8** (Restricted Operation).
- Success: the Mended substrate is Locked — it cannot become less coherent (unable to become a Gap again).

**Intended effect:** The Lock prevents Gap re-formation at the Mended site. A site that repeatedly forms Gaps (high-traffic Thread territory, Calamity-adjacent zone) would normally re-Gap after Mending. With a Lock: the substrate coherence is frozen at its post-Mending state — it cannot re-become a Gap.

**But:** Lock on Mended substrate — chronic RS drift from Season 2: −1 RS/season. The Lock that prevents Gap re-formation costs ongoing RS drain. Trade-off: Gap persistence cost (−4 RS/season per active Gap) vs Lock drift cost (−1 RS/season). If the site would otherwise re-Gap after one season: the Lock saves 3 RS/season in prevented Gap drain at the cost of 1 RS/season Lock drift = **net RS +2/season** at sites with reliable Gap re-formation rates.

**[EMERGENT+]** Locking a Mended substrate is net-positive RS if the site would otherwise re-Gap within 2 seasons. At high-Thread-traffic territories and Calamity-adjacent zones: re-Gap rates are presumably high. A practitioner-defender who Mends AND Locks key sites converts the endgame RS economics. This is elegant design emerging from two existing mechanics.

**[GAP]** Can the substrate itself (post-Mending) be treated as a Thread configuration for Lock purposes? The Lock rules target configurations "unable to become" — the Mended substrate's inability to become a Gap IS the Lock's intended effect. Ruling required: "The post-Mending substrate coherence of a Mended zone can be targeted by Lock (Restricted Operation, Field scale minimum). Success freezes the substrate's self-repair state, preventing Gap re-formation at that site. Chronic RS drift applies as standard Lock."

---

# 10. WHAT HAPPENS TO A LOCK WHEN THE PRACTITIONER DIES?

## 10.1 Lock Persistence After Practitioner Death Is Undefined [GAP — CRITICAL FOR PLOT]

Lock rules define reversal ("Pull at Ob = original practitioner's TS ÷ 10 − 2") and the Einhir framework for Permanent Locks. Both cases assume the original practitioner exists and can be referenced.

**If the original practitioner dies before their Lock is Pulled:** The Lock was tied to that practitioner's intentionality — their specific Thread configuration of "this thing shall not become." Does the Lock:

(a) **Persist indefinitely** — the intentionality is now frozen without its source, like a spell outlasting its caster. The Lock becomes de facto Permanent (no practitioner to reference for Pull Ob calculation).

(b) **Dissolve immediately** — the intentionality that sustained the Lock is gone. The locked configuration releases; RS gains +1 per season the Lock persisted (max +5, as with normal Lock release).

(c) **Unravel slowly** — the Lock degrades over 1d3 seasons without its intentional source, producing a Partial Lock effect during degradation (volatile configuration, unstable).

**[GAP — CRITICAL]** The answer determines whether "assassinate the enemy practitioner who placed our Lock" is a viable RS restoration strategy. Under (a): assassination leaves the Lock permanent, making it worse. Under (b): assassination dissolves the Lock instantly and restores RS — this is the highest-value assassination in the game. Under (c): assassination produces a transitional instability period.

**Design recommendation:** Option (c) provides the most interesting gameplay. "When a practitioner who has placed an active Lock dies, the Lock degrades over 1d3 seasons. During degradation: the locked configuration oscillates (Shifting Object risk) and becomes targetable by Pull at Ob 1 (degrading intentionality offers minimal resistance). If Pulled during degradation: RS restoration applies. If not Pulled: the Lock collapses into Permanent state (the unresolved intentionality crystallizes into substrate adaptation without its source)." This gives assassination a clean narrative consequence while preserving the "Permanent Lock = endgame problem" design.

---

# 11. KNOT WITH A THREADCUT BEING — METAPHYSICAL PARADOX

## 11.1 Can an Organic Practitioner Form a Knot With a Threadcut Being? [GAP — CRITICAL METAPHYSICS]

PP-632: "Knots are being-with (Mitsein), not Thread operations. Any character. TS not required."

Threadcut beings are defined as: having their own originary intentionality, no Coherence track (they don't render — they exist in the originary state continuously), and continuous self-rendering as their mode of existence.

Knots constitute "being-with" — the relational ontological bond between two entities. A Knot with a threadcut being would be: a Mitsein bond between an organic practitioner (who renders, who has Coherence) and an entity that exists in the originary state (no rendering, no Coherence). This is a bond across two ontological modes: rendered and originary.

**Theoretical consequences:**
- **Solidarity attacks** require an active Knot with the NPC. A Solidarity attack through a Knot with a threadcut being would require: the organic practitioner leveraging their ontological bond with a non-rendering entity to persuade another party. Philosophically: appealing to your relationship with something that exists outside the rendered world.
- **Knot-mediated remote Thread-Read** (TS 30+, +1 strain/use): using the Knot to access the threadcut being's direct substrate perception remotely. This is potentially accessing Thread information without performing a Leap — because the threadcut being never stopped perceiving at Thread-depth.
- **Anchoring Scene** (Bonds TN7 Ob2, +1 Coherence): Can a threadcut being anchor a practitioner's Coherence recovery? The Anchoring is "relational anchoring." A threadcut being IS a relational anchor of a profound kind — they exist continuously in the originary state that the practitioner is trying to stabilize their rendering around. Their presence as Knot-partner for Anchoring might be MORE effective than an organic partner's.
- **Knot-mediated remote Thread-Read causing +1 threadcut being self-maintenance strain per use** (PP-632 threadcut mechanic): Using the Knot connection actively drains the threadcut being's self-maintenance stability.

**[GAP — CRITICAL METAPHYSICS]** No rule addresses Knot formation with threadcut beings. Given that "any character" can form Knots (PP-632: "TS not required"), threadcut beings should be Knot-eligible. But the metaphysical consequences are unique and potentially profound — remote substrate access through the Knot connection, Anchoring at unprecedented depth, and the threadcut being's self-maintenance drain from Knot use.

**Required ruling:** "Organic characters may form Knots with threadcut beings. Formation follows standard rules (Connect action, Disposition ≥ +3 threshold). Knot-mediated Thread-Read via this Knot operates as for any Knot partner (TS ≥ 30 organic required; +1 Rendering Strain on the threadcut being per use in place of the standard strain). Anchoring Scenes with a threadcut being as partner: Ob 1 instead of Ob 2 (the threadcut being's continuous originary state provides stronger relational grounding). The threadcut being's participation in Anchoring Scenes adds +1 Rendering Strain per Anchoring (external engagement = self-maintenance cost)."

---

# 12. POP ON SOMEONE'S FIRST LEAP MEMORY

## 12.1 Can You Temporally Displace the Event of Thread Awakening? [EXPLOIT — METAPHYSICAL]

A Past-Oriented Pull can target any past relational or experiential configuration. The First Leap Event is a specific historical moment — the practitioner's first Thread contact, their rendering suspended for the first time.

**A practitioner with TS 30+ could POP the target's First Leap Event:**
- Recency (if it happened in the last season): Ob 4, TN 8.
- 3–5 seasons past: Ob 5, TN 8.

On Success: the First Leap Event's configuration is opened — displaced. Temporal Disjunction fires. The target's memories of their First Leap are intact, but the configuration's actualization is opened.

**What does "opening" a First Leap Event mean?** The First Leap Event is described as an "Event Scene" — it is the moment when Thread Sensitivity reached the Stirring threshold and the practitioner first suspended rendering. If the POP succeeds on this event:

- The First Leap's consequences (TS permanently at 30+, Approach Training tag established, Thread contact as a possibility) — are these consequences of the Thread configuration (which is now opened) or consequences of the TS stat itself (which is biological/developmental)?

**[GAP — METAPHYSICAL]** If the First Leap's relational configuration can be Pulled: the moment of awakening is "opened," rendered less actualized. Does this mean: the practitioner retains TS 30+ (their perceptual depth is biological) but their Approach Training tag is un-established (the relational memory of how to Leap is disrupted)? This would result in: a TS 30+ character with Thread Sensitivity but no Approach Training — they can perceive Thread but cannot Leap until they re-establish the Approach (re-experiencing the path to rendering-suspension).

This is a viable and philosophically coherent ruling. The TS (perceptual depth) is one thing; the Approach Training tag (the learned ability to surrender rendering) is another. A POP on the First Leap Event could strip the Approach Training tag without reducing TS — creating a practitioner who perceives everything but cannot act.

**[EXPLOIT — DARK]** Stripping an enemy practitioner's Approach Training tag via POP renders them unable to Leap without removing their TS. They retain all Thread perception (they can see everything, Diagnose freely during contact they can no longer initiate, use Thread-Read only if they somehow achieve contact by other means). This is a precision incapacitation that doesn't require killing or Dissolving the practitioner — just denying their operational capability. Required ruling on whether this is possible.

---

# 13. THE FORGETTING BOUNDARY "ROUND" — SMOOTH FAILURE IN NON-COMBAT CONTEXT

## 13.1 Companion Carrying Uses Rounds in an Exploration Context [SMOOTH — FAILS]

PP-279 companion carrying: "Each companion: −2 Coherence/round (cumulative)." A "round" is defined in combat (one exchange of action declarations). In Southernmost exploration, there are no combat rounds — exploration uses scenes and time units.

**Fieldwork uses "time units" (turns of fieldwork action), not rounds.** A scene in exploration is not a round. The Forgetting boundary crossing, as an exploration action, occurs within a scene — not within combat rounds. Yet the Coherence drain is stated in rounds.

**[SMOOTH — FAILS]** The companion carrying rule uses a time unit ("round") that doesn't exist in the context where the rule applies (Southernmost exploration). This is a friction point: at the table, the player asks "how long is a round during the Forgetting crossing?" and there is no answer.

**Required:** Define the Forgetting crossing time unit. Proposed: "The Forgetting boundary crossing is measured in crossing intervals (each crossing interval = one Contact Round of the practitioner's Focus duration, since the Forgetting crossing IS a Thread contact window). At Focus 5: 5 crossing intervals. Coherence −2 per companion per crossing interval." This maps the companion carrying rule directly onto the existing Thread contact duration mechanic — the Focus already times the crossing.

---

# 14. MENDING YOUR OWN FAILED DISSOLUTION — TEMPORAL COHERENCE

## 14.1 Can You Mend a Gap You Just Created? [SMOOTH — OK; EMERGENT+]

Dissolution Partial or Failure creates a Gap or Shifting Object. A practitioner who fails a Dissolution: "Full Gap tears open. RS −8. Monstrous Incursion immediately. Practitioner Incapacitated."

If the practitioner is Incapacitated: they can't Mend. But a companion practitioner (or another party member with TS 50+) in the same scene could immediately attempt Mending of the fresh Gap (Micro-Gap or Standard Gap depending on Dissolution outcome and Partial vs Failure).

**Mending a same-scene Gap (Dissolution Partial created a Shifting Object):** Mending Ob 2 (Shifting Object, Micro-Gap level). With the Mending Overwhelming co-movement card effect: the freshly-created instability settles. RS cost: Dissolution Partial RS −6, then Mending Overwhelming RS +2 net. Net RS impact: −4 (instead of −6 if the Shifting Object persisted to Accounting).

**Can the same practitioner Mend their own Dissolution's aftermath in the same contact window?** Sequential operations in one contact window: the Dissolution is Op 1 (failed = ejected from contact). Ejection ends the contact window. The practitioner cannot Mend in the same contact window.

But they can RE-Leap (new contact window, next scene): Ob 2 (TS 50+), pool full again, target the Shifting Object they created. This is the "undo your own mistake" pattern — costly (two Leaps, two Coherence events) but mechanically valid.

**[SMOOTH — OK]** The mechanic is coherent: Dissolution failure ejects (can't Mend in same window), but re-Leap next scene to Mend is valid. The cost is appropriately punishing (double Leap, double Coherence, whatever RS damage already occurred). No design change needed — but surface as a tactical note for practitioners: "A failed Dissolution creates a Shifting Object or Gap that you are responsible for Mending. Plan for a second contact window in the same scene or next scene to address the aftermath."

---

# 15. CERTAINTY TRACK AS THREAD-SENSITIVITY GATE

## 15.1 Certainty Decline = Thread Eligibility Advance — Smooth Zoom From Personal to System [SMOOTH — EMERGENT+]

Clock registry: "Certainty | 0–5 | Varies | Oscillating: 5 = Solmund orthodoxy, 0 = Thread acceptance."

Certainty decline (toward 0) moves the character toward Thread acceptance. At some Certainty threshold, TS can develop (the character's consciousness becomes receptive to Thread-level perception). This is the mechanism by which non-practitioners become practitioners through play.

**The smooth zoom:** Certainty is a personal track (character sheet). Thread Sensitivity is a personal stat. RS is the world track. AP is a territory track. TC is a global faction track. A character whose Certainty declines through play experience:
- Gains Thread eligibility (TS can develop → character becomes practitioner)
- As practitioner: performs Thread operations → generates AP in territory (Batch 5 §7)
- AP → Church Inquisitor deployment → TC advances
- TC → Church political power grows → faction dynamics shift
- Faction dynamics → Accord changes → Victory condition pressure changes
- Victory condition pressure → player strategic choices → more Thread operations
- Thread operations → RS drain → RS threshold effects → more Certainty-challenging events

**[SMOOTH — EMERGENT+]** This is a complete smooth zoom chain: individual Certainty decline → character Thread development → territory AP → faction TC → peninsular politics → world RS → individual encounter pressure → individual Certainty decline (loop closes). Every level of the zoom is mechanically connected to every other level through defined rules. This is the system working as designed.

**Surface explicitly as a design validation:** The Certainty-to-Thread-to-AP-to-TC-to-Victory-to-RS-to-Certainty feedback chain is the smoothest macro-loop in the game. It should be documented as such because it answers the question "why is Certainty an interesting track?" — because it connects individual character development to world-scale consequences through six mechanically-defined steps.

---

# 16. WARDEN HARVEST BG ORDER — WHAT IS IT?

## 16.1 PP-630 Adds "ED-NEW Harvest" to Fieldwork — Warden Harvest [GAP]

Fieldwork_v30 header: "PP-628 (canon guard), PP-630 (three-axis Ob, Warden Emergence fix, **ED-NEW harvest**)." This "harvest" in PP-630 is a Warden-specific fieldwork action distinct from Niflhel's BG Harvest order (Batch 5 §18).

Warden Harvest in fieldwork context: the Wardens harvest something during Southernmost expeditions. Given:
- Wardens operate at S-033 Askeheim.
- WC advances from Forgetting Check success.
- Mending produces "Dissolution residue forms at Mending site" (Co-Movement card 18: Niflhel harvests).
- Wardens perform sustained Mending at Askeheim.

**The Warden Harvest is likely:** Harvesting substrate information, Thread configurations, or Einhir-related resources from Askeheim during Mending work. Not Dissolution Residue (that's Niflhel). More likely: "Harvesting" stable Thread configurations from the Foundational gap network — the Einhir technique analogs that the Wardens have preserved through practice.

**Mechanically:** The Warden Harvest fieldwork action may produce: Einhir Text equivalents (enabling Einhir framework access without Sigurdshalm), WR/WC advancement bonus, or RS restoration materials that can be deployed outside Askeheim.

**[GAP]** The Warden Harvest action is referenced but undefined in all available documents. If it produces Einhir Text equivalents: it creates an alternate path to Einhir framework access that doesn't require Sigurdshalm control (solving the Batch 3 §5.1 Sigurdshalm chokepoint problem). This is a significant design gap that affects both the Sigurdshalm strategic value analysis and the endgame Thread capability calculus.

---

# 17. SIMULTANEOUS RUPTURE CAP + THREAD — PP-633 UNDER PRESSURE

## 17.1 Simultaneous Knot Ruptures from Opposing Operations [EMERGENT+]

PP-633: "Multiple Knots rupturing same scene → total Composure damage capped at floor(Composure×0.75), min = highest single-tier cost. Non-Composure effects uncapped."

A practitioner whose opponent wins a FR (Lock/Dissolution) Opposing Operation receives: +2 Ob next Thread op, 4 Composure damage, +1 Wound (if winner Dissolved). If this practitioner has three Close Knots with NPCs present in the scene, and the Dissolution tears through them: do the three Knots rupture simultaneously?

**The Dissolution of a practitioner (targeting their personal Thread configuration at Personal scale) doesn't directly target their Knots.** Knots are Mitsein bonds, not Thread configurations of the practitioner (ruling pending per Batch 5 §15). So Dissolution of the practitioner ≠ automatic Knot rupture.

**But:** The +1 Wound from FR Opposing (winner Dissolved): Wound disruption during contact triggers Spirit check TN7 Ob1. If the practitioner fails: rendering reasserts, contact drops. But they were in contact for the Opposing Operation — after the operation resolves, they're out of contact regardless. The Wound itself (from FR Opposing loss) doesn't trigger Knot ruptures.

**Where PP-633 is relevant for Thread:** A mass battle scene where three Thread operations fire simultaneously and all three fail catastrophically (Gap formations, Dissolution failures): each failed Dissolution Failure incapacitates its practitioner. If those practitioners had Close Knots with player characters: three simultaneous Knot Loss events (incapacitated → forced departure → Loss consequence). PP-633 caps the Composure damage but "non-Composure effects uncapped" — three simultaneous Coherence −1 (Loss) events ARE uncapped. Player character goes from Coherence 7 to Coherence 4 (Fragmented) in one mass battle scene.

**[EMERGENT+]** A catastrophic mass battle with multiple practitioner casualties produces uncapped Coherence drain on player characters through simultaneous Knot Loss events. PP-633's partial protection (Composure cap) does not shield against the Coherence cost. A player character with three Knotted practitioner NPCs who all die in the same battle goes directly to Fragmented. This is devastating and warrants an explicit design note.

---

# 18. VISIBILITY CONCEALMENT ROLL — ELEGANT OUTLIER

## 18.1 Thread Concealment Uses Cognition-Only — Inconsistent Pool Construction [ELEGANT — FAILS]

Threadwork §2.3: "Concealing from Thread Sensitivity 30+ observers: Roll Cognition only (no History), TN7, Ob = observer's Thread Sensitivity ÷ 30 (round up)."

Every other Thread-adjacent roll uses: Primary Attribute × 2 + History. The concealment roll uses: Cognition alone (single attribute, no doubling, no History). This is the only non-standard pool construction in the Thread system.

**Why Cognition only?** The infill would explain this. The skeleton offers no rationale. Mechanically: Cognition at attribute 1–7, average 3. Pool = 3D vs Ob 1 (TS 30–49 observer) through Ob 3 (TS 70+ observer) through Ob 4 (TS 100 observer). At Cognition 3, Ob 3: 3D TN7 → P(≥3) ≈ 22%. At Cognition 5, Ob 3: 5D TN7 → P(≥3) ≈ 47%. Concealment is unreliable against TS 70+ observers even at high Cognition.

**[ELEGANT — FAILS]** The concealment roll is an outlier in pool construction, creating a special-case rule that players must remember specifically for this action. It also has no History bonus — which means a practitioner who has spent months concealing Thread work in Church territories has no experiential History to draw on. The skill learned through concealment practice is mechanically invisible.

**Proposed fix:** "Thread concealment: Cognition + Thread-relevant History (specifically: any History related to deception, covert operations, or Thread practice concealment). TN7, Ob = observer TS ÷ 30 (round up)." This aligns concealment with every other fieldwork action (Cognition + History) and rewards practiced concealment. The Ob remains unchanged — observers with TS 70+ are still very hard to deceive.

---

# SUMMARY TABLE — BATCH 6

| Item | Finding | Lens | Severity | Action Required |
|------|---------|------|----------|----------------|
| Three-axis Ob | 3 table lookups per operation; highest overhead in game | **ELEGANT — FAILS** | Moderate | Pre-calculation character sheet section for common op profiles |
| Mending Ob column | Separate column = "Depth Ob −1" redundantly tabulated | **ELEGANT — FAILS** | Low | Remove column; replace with one-line rule |
| Thread-Read vs Evidence Track | Thread ops produce 2–3× more Evidence than mundane investigation; compresses investigation arc | **ROBUST — CONCERN** | High | Gate Thread-Read Evidence to Depth ≥ 4 questions only |
| Leap Priority 5 + multi-engaged | "Reactive defence only" during Leap round = full pool to Defence, but undefined vs multi-attacker | **SMOOTH — FAILS** | Moderate | Rule: full pool to Defence (0 Offence), standard PP-274 resolution |
| Fibonacci bonus vs Thread contact | Group attackers get uncapped bonus vs defenceless Thread-active practitioner | **SMOOTH — OK (thematic)** | Low | Surface as tactical note: Thread contact in melee = tactically suicidal |
| Dissolution Residue tracking | 4 separate tracking values; volatile dice require separate resolution | **ELEGANT — FAILS** | Moderate | Simplify: remove volatile dice explosion; use chain-on-9-or-10 instead |
| Domain Echo + Thread ops | Thread operations don't map to existing Domain Action categories; Echo handoff requires GM improvisation | **SMOOTH — PARTIALLY FAILS** | High | Define Thread → Domain Action mapping table |
| Belief Co-Authorship + Recall | Is "Recall-based rolls" at Fragmented applicable to Thread pools? Potentially cascades −1D to all Thread ops | **ELEGANT — CONFLICT** | High | Rule: Thread ops are Spirit-primary, NOT Recall-based; Fragmented −1D does not apply |
| NPC practitioner AI | No Thread decision tree for NPC practitioners; autonomous Thread play is fully GM-improvised | **ROBUST — PARTIAL** | High | Define NPC Thread Coherence decision table |
| Concentration track | No Thread interaction defined; Focus stat feeds Concentration but Contact Round spending is undefined | **SMOOTH — GAP** | Moderate | Rule: Thread contact precludes active orator participation; Corroboration only |
| Lock on Mended substrate | Mend → immediately Lock = prevents Gap re-formation; net RS +2/season vs re-Gap cost | **ELEGANT — EMERGENT+** | Low | Surface as design note; rule: post-Mending substrate is Lock-eligible |
| Lock after practitioner death | Lock persistence after practitioner death is undefined; assassination value is unknown | **SMOOTH — GAP — CRITICAL** | Critical | Rule proposed: Lock degrades over 1d3 seasons → Pulling at Ob 1 during degradation; else crystallizes Permanent |
| Knot with threadcut being | "Any character" Knots = threadcut being eligible; metaphysical consequences profound and undefined | **ROBUST — GAP — CRITICAL** | Critical | Full ruling proposed: Ob 1 Anchoring; +1 Rendering Strain per Knot use on being |
| POP on First Leap Event | Past-Oriented Pull on practitioner's Thread awakening memory may strip Approach Training tag | **ROBUST — EXPLOIT** | High | Ruling: POP Success on First Leap → Approach Training tag suspended; re-establishment required |
| Forgetting "round" in exploration | Companion carrying Coherence −2/round uses undefined time unit in non-combat context | **SMOOTH — FAILS** | Moderate | Map crossing intervals to Contact Rounds (Focus duration = crossing length) |
| Mending own Dissolution aftermath | Re-Leap next scene to Mend your own failure: valid but costs double Leap | **SMOOTH — OK** | Low | Surface as tactical note for practitioners |
| Certainty → Thread → AP → TC → RS loop | Complete six-level smooth zoom chain: personal development → world RS → personal | **SMOOTH — EMERGENT+** | Low | Document as design validation; answer to "why is Certainty interesting?" |
| Warden Harvest | PP-630 references Warden Harvest fieldwork action; completely undefined | **ROBUST — GAP** | High | Fetch params_board_game §WC; define Harvest; assess impact on Sigurdshalm chokepoint |
| PP-633 + simultaneous Knot Loss | Three simultaneous Knot Loss events from mass battle practitioner casualties → uncapped Coherence −3 in one scene | **SMOOTH — EMERGENT+** | Moderate | Design note: mass battle practitioner casualties produce uncapped Coherence drain on player Knot partners |
| Concealment roll outlier | Cognition-only (no ×2, no History) = only non-standard pool construction in Thread system | **ELEGANT — FAILS** | Low | Fix: Cognition + concealment History (align with standard fieldwork pool) |

---

## NEW CRITICAL ITEMS FROM BATCH 6

21. **Lock after practitioner death** — the most plot-relevant gap found across all six batches. Assassination of the enemy practitioner who placed a Lock is a viable strategy only if the Lock dissolves on their death. If it crystallizes into Permanent, assassination makes things worse. This uncertainty makes every "assassinate the enemy practitioner" decision potentially catastrophic.

22. **Knot with threadcut being** — metaphysically profound, mechanically undefined. A Knot with a threadcut being bypasses the Leap requirement for remote Thread-Read access (the being already exists at Thread-depth; the Knot provides a connection). Anchoring through a threadcut being Knot is mechanically superior to organic Anchoring. Both interactions are unruled.

23. **NPC practitioner AI decision tree** — Thread creates emergent autonomous play only if NPC practitioners have defined decision rules. Without these, Thread's "robust" emergent play depends entirely on GM skill, not mechanical structure. The settlement governor AI gets a defined priority tree (§3.2); NPC practitioners need the equivalent.

24. **Domain Echo for Thread operations** — the Thread → faction-consequence handoff requires GM improvisation every time. A mapping table converts this from creative burden to procedural lookup, supporting the smooth zoom-out that scale transitions are designed to provide.

25. **Recall-based rolls at Fragmented** — whether Thread pools count as Recall-based determines whether the Fragmented band penalizes Thread ops by an additional −1D. The ruling has significant impact on practitioner viability in the Fragmented Coherence band.

---

*End of document. Session d8b924fb834a398c.*
