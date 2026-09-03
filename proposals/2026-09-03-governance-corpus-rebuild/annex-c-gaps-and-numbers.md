# Annex C — Gaps, unresolved rules, and the verbatim number inventory

> An independent second reading of the same 33 documents, asking only: where does this corpus fail to
> be executable? Section 2 (U-01…U-30) is the one that matters for building — each entry quotes the
> rule and names the **specific missing decision**, not "needs more detail". These are the questions
> the design in Annex B answers. Section 1 catalogues collisions (decided in Part III of the main
> document); section 4 is 362 verbatim numeric constants, thresholds and formulas, preserved because
> a paraphrase destroys them.

---

# B — Independent read: where the governance corpus contradicts itself, and where a no-GM engine cannot execute it

Reader B. Corpus: the 33 `.md` files in `scratchpad/gov/` (810,408 bytes), read in full, nothing else. No repository, no other analyst's output.

Conventions. Citations are `filename › heading` (a `§` number where the document has one; a line number where a location has no heading). Quotations are verbatim, including the corpus's own arithmetic. IDs are stable: `X-` contradictions, `U-` underspecification, `R-` dangling references, `N-` numbers. Where a number carries different values in different places, the `N-` row points at the `X-` row.

**Reading order used.** Small files first (`generational_transition_v30`, `clocks`, `southernmost`, `phases`, `parliament`, `territory_temperaments_v30`, `tracks`, `fractional_province_ownership_v30`, `ci_seizure`), then the mid-size specs (`treaty_expiration_v30`, `settlement_adjacency_v30`, `parliamentary_transfer_v30`, `baralta_crown_claim_v30 (1)`, `ministry`, `faction_succession_split_v30`, `march_layer_v30`, `campaign_architecture_v30`, `worldbuilding_v30 (1)`, `institutions`, `conflict_architecture_proposal`, `valoria_political_hierarchy_v30`, `core (1)`, `governance_play_redesign_v1`, `insurgency_pipeline_v30`, `ci_political_v30`, `geography`, `faction_behavior_v30`, `stats_1_7_scale (1)`, `early_game_ignition_analysis`), then the four large ones (`player_agency_v30 (3)`, `strategic_layer_v30`, `settlement_layer_v30 (1)`, `faction_politics_v30`).

**Null results, stated as such.** Two documents contain no *internal* contradiction that I could find: `treaty_expiration_v30.md` (its three forward-flags are self-declared derivations, not contradictions) and `territory_temperaments_v30.md` (one arithmetic slip in §3, recorded at X-59, and a status-header clash shared with six other files, X-33). Every other document either contradicts another document or contradicts itself.

---

## 1. Contradictions

Ranked by build consequence. **Tier A** = a formula, threshold, resolution method, victory condition or data table that the engine must evaluate every season and that has two incompatible definitions. **Tier B** = a rule or entity with two incompatible definitions that affects a subsystem. **Tier C** = naming, status and bookkeeping clashes that would confuse an implementer but not change resolution.

### Tier A — formulas, thresholds, victory, resolution

**X-01 · What wins the game.**
- `core (1).md › (header comment, line 10)`: "Per GD-1 the SOLE victory condition for all factions is Peninsular Sovereignty (control 11+ of 15 territories) — no faction-specific or non-military victory path exists."
- `ci_political_v30.md › §2.2 CI 100 — Theocracy Unification Attempt`: "Peninsular Sovereignty (control 11/15 territories sustained 2 seasons, treaties counting) is the **sole** victory condition for all factions".
- `insurgency_pipeline_v30.md › §7 GD-3 Sim Enforcement Boundaries`: "can WIN via peninsular_sovereignty (the sole victory path) once they hold 11+ territories sustained 2 seasons."
- `campaign_architecture_v30.md › §1.3 CI=100 — Mass Seizure Declaration`: "The Church still needs all 15 territories at Accord ≥ 2 for Peninsular Sovereignty."
- `settlement_layer_v30 (1).md › §8.1 Changes to Existing Systems`: "Universal victory still requires Accord ≥ 2 in all provinces."
- `parliament.md › PP-189 Final Corrections`: "Church primary victory threshold: CI ≥ 65 (P-32 reduced from 70)".
- `institutions.md › Löwenritter — Reconstitution`: "PI = 0 is a permanent lock on Regency primary victory (PI ≥ 4 required)."
- `ci_political_v30.md › §6.2 Faction-Specific Priorities`: "HF victory needs PI ≥ 5 which is the starting value".
- `geography.md › Varfell Territorial Expansion Constraint`: "The Intelligence Hegemony victory path requires TCV ≥ 10 + VTM ≥ 3 + 2 rival stats revealed." and `› Varfell Path B — Southernmost Dominion`: "TCV held ≥ 8 … Control T4 (Grauwald) AND T13 (Oastad) … VTM ≥ 3 … WR ≥ 2".
- `strategic_layer_v30.md › I-06`: "5 Presence markers in 5 non-adjacent territories, held 2 consecutive seasons + Mending Stability ≥ 50."
- `phases.md › Phase 5 Seasonal Accounting`: "12. Victory condition check. Any faction meeting all its victory conditions for 2 consecutive Accounting steps declares victory. … Co-victory pairings checked simultaneously (§4)."
- **Decision:** whether the victory predicate is 11-of-15 or all-15-at-Accord≥2; whether "treaties counting" is part of it; and whether every faction-specific victory (CI ≥ 65, PI ≥ 4/5, Path B, Intelligence Hegemony, Restoration MS ≥ 50, co-victory pairings) is struck or is an "approach" — `faction_behavior_v30.md › §3.1` says "faction-specific tracks in victory_v30 §3 are *approaches*, not win triggers", but `phases.md` still checks them as conditions.

**X-02 · The degree table (how a roll becomes an outcome).**
- `core (1).md › Degree Table (PP-179 + PP-249)`: "≥ 2× Ob AND ≥ 3 | Overwhelming … ≥ Ob | Success … 0 < net < Ob | Partial … ≤ 0 | Failure … ED-031 (Ob+1 surplus) is SUPERSEDED by PP-179 (2×Ob). PP-179 is canonical."
- `strategic_layer_v30.md › CORRECTION 3 — Degree Table Update`: "Ob + 1 or more | **Overwhelming** … = Ob | **Success** … Ob − 1 | **Partial** … 0 | **Failure**". (A net of 1 against Ob 3 has no row at all in this table.)
- The worked examples in `strategic_layer_v30.md › Cascade Test 1`–`4` and `Scenario A–C` all use the Ob+1 rule ("Ob 1, surplus 2 = **Overwhelming.**").
- **Decision:** which degree ladder is canonical for dice checks, and whether the Ob-10 exception ("Overwhelming unavailable. Partial requires net ≥ 5", `core (1).md`) survives.

**X-03 · Target number.**
- `core (1).md › Dice System (v05 correction)`: "d10 pool. TN 7 (standard). … 7–9 | +1 success … 10 | +2 successes … 1 | −1 success".
- `baralta_crown_claim_v30 (1).md › §2 Contest Mechanics`: "rolls their pool vs Ob 3 (TN 7)".
- `southernmost.md › Forgetting Check`: "Pool: Cognition + Recall. TN 8." and its probability table is computed "(7D base, TN8)".
- **Decision:** one TN, or an explicit per-check TN field.

**X-04 · Resolution method for faction Domain Actions.**
- `stats_1_7_scale (1).md › Domain Action Resolution (deterministic+stochastic) — CANONICAL`: "**This is the canonical resolution method for faction Domain Actions and bare-stat faction checks.** It supersedes the bare-stat-pool-vs-Ob dice approach … P_success(M) = clamp(0.50 + 0.10·M, 0.05, 0.90)".
- Every other document states faction checks as dice pools versus Ob: e.g. `core (1).md › Standard Action Ob Reference`, `ci_seizure.md › Church Mass Seizure` ("**Pool:** Influence + floor(CI / 15)"), `parliament.md › L Suppression` ("adds +2D to the suppression pool"), `ministry.md › Ministry NPC AI Priority Tree` ("roll Ministry L (3D) vs Ob 1"), `fractional_province_ownership_v30.md › §2.6` ("Roll 5d10 vs Ob 3"), `institutions.md › Löwenritter — Reconstitution` ("Roll: L vs Ob 3"). `ci_political_v30.md › §4.2` and `faction_succession_split_v30.md › §2.2` have been rewritten to the resolver; the rest have not.
- **Decision:** which checks are "bare-stat faction checks" governed by the resolver and which remain dice; and the stat-to-`difficulty` table for every action (the resolver gives only five examples).

**X-05 · Church Seizure Ob — six formulas.**
- `ci_seizure.md › Seizure Ob`: "Ob = 10 − PT − infrastructure modifiers (floor 1)." (also `campaign_architecture_v30.md › §1.2`, `ci_political_v30.md › §7.6`, `settlement_layer_v30 (1).md › §1.5`).
- `stats_1_7_scale (1).md › Church — CI 60 Territorial Seizure`: "Roll: Influence + floor(CI/15) vs Ob = 7 − PT (AUTHORITATIVE per faction_layer §2.7; supersedes the stale L-based formula)."
- `faction_politics_v30.md › §4.2 CV / PT / SW Terminology Dissolution`: "Seizure Ob uses "max(0, 3 − PT)", identical to Seizure Ob in conviction_track_v30 §2.1".
- `parliament.md › PP-189 Final Corrections`: "CI 75 seizure: Church L vs Ob = Fort + 1 (PP-192/PP-421)". Against `ci_seizure.md › Church Mass Seizure`: "**Fort Level:** Fort Level does NOT modify Seizure Ob."
- `strategic_layer_v30.md › P-23`: "Church Church Influence 80+ triggers seizure at next Accounting. Territory roll: Church Military vs Defender Military, Ob 2."
- `strategic_layer_v30.md › Cascade Test 4`: "Church Mandate vs Ob 3 (contested territory) or Ob 2 (allied/neutral)."
- Internal to `ci_seizure.md › Church Mass Seizure`: the table "5 (Piety) | 2 … 0 (Restoration) | 7" cannot be produced by "10 − PT" (which gives 5 and 10), and the same section says "PT 5 with full infra = Ob 1".
- **Decision:** one formula; whether infrastructure modifiers sum per settlement or per territory; whether Fort applies.

**X-06 · When Church seizure fires, and what gates it.**
- `ci_seizure.md › Church Mass Seizure (one-shot)`: "**Available:** CI ≥ 60. Declaration probability per season: P = ((CI−60)/40)^3.3 … One attempt only." Gate: "Church L ≥ 4 required to attempt seizure."
- `campaign_architecture_v30.md › §1.3`: "When CI reaches 100: every territory with at least one settlement containing a Church building (Chapel+) is targeted for simultaneous Seizure."
- `ci_political_v30.md › §2.1`: "Gated by Church Mandate >= 4"; `› §6.2`: "Church Seizure when CI ≥ 40 and prominent territories have PT ≥ 3."
- `stats_1_7_scale (1).md › Church — CI 60 Territorial Seizure`: "Trigger: Church Influence (CI) reaches 60. Fires once per territory."
- `parliament.md › Parliament Integrity (PI) Scale`: "Church territorial seizure (−1)" and "CI +2 (does not apply when CI is frozen at 75 — PP-560)"; `clocks.md › Church Influence (CI) Effects`: "70–74 | … Territorial Seizure protocol pending"; `ministry.md`: "**Ministry and Church Seizure (CI 75)**"; `geography.md › What "No Faction Control" Means in BG`: "CI 75 Church Territorial Seizure does not target T15."
- `strategic_layer_v30.md › P-23`: "Church Influence 80+ triggers seizure".
- **Decision:** deterministic-at-100, probabilistic-from-60, or threshold-at-75/80; one-shot versus once-per-territory; L-gate versus Mandate-gate (these are different quantities after X-10).

**X-07 · CI ceiling: 100 or frozen at 75.**
- `ci_seizure.md › CI Generation — Seasonal`: "CI runs to 100 (no freeze)." `ci_political_v30.md › §0`: "CI 75 freeze (PP-421): superseded; CI runs to 100". `core (1).md › Starting Values`: "0–100 (no freeze)".
- `parliament.md › Parliament Integrity (PI) Scale`: "CI +2 (does not apply when CI is frozen at 75 — PP-560)."
- `settlement_layer_v30 (1).md › §7.1`: "CI caps at 75 (phase transition), so the real question is: when does 75 fire?"
- `ci_seizure.md › Church Mass Seizure`: "**Mandatory Assert post-CI 75:** Suspended. Assert optional only once CI caps."
- `clocks.md › Church Influence (CI) Effects` stops at "70–74".
- **Decision:** ceiling value; whether any 75-threshold effect survives.

**X-08 · Battle → MS / IP / Turmoil.**
- `campaign_architecture_v30.md › §3.1 Mass Battle MS Loss — ×3 Multiplier Struck`: "Standard Mass Battle: −1 MS per battle, regardless of scale or outcome".
- `clocks.md › Battle Consequences`: "All battles on Valorian soil: MS −1 (MS −2 for Campaign/War scale). Each season with inter-faction battle: IP +2. Each season with inter-faction battle: Turmoil +1." Same in `strategic_layer_v30.md › PP-647` and `tracks.md › Turmoil`.
- `ci_political_v30.md › §4.4`: "**Battles → MS −1 per battle.** Each season in which at least one inter-faction battle occurred: MS −1 immediately at Accounting. Campaign/War scale: MS −2." (per battle and per season in one paragraph) and "**~~Battles → IP +2 per season: STRUCK by ED-743 (2026-04-29).~~**" and "~~Direct battle-occurrence trigger STRUCK by ED-743~~" for Turmoil — while `ci_political_v30.md › §0` and `› §7.5` in the same file keep "Battle → MS −1, IP +2 per season with inter-faction battle".
- `phases.md › Phase 5 Seasonal Accounting`: "4e. **Battle consequence accounting:** IP +2 if inter-faction battle occurred this season."
- `settlement_adjacency_v30.md › §2.3`: "Strain +1: applied peninsula-wide (unchanged)" (per battle).
- **Decision:** per-battle vs per-season; scale multiplier or flat; whether IP and Turmoil advance from battles at all after ED-743.

**X-09 · Turmoil decay condition.**
- `tracks.md › Turmoil (Global, 0–10)`: "**Decay:** −1 per peaceful season (no battles, no revolts)." Same in `core (1).md › Starting Values` ("Decays −1/peaceful season").
- `phases.md › Phase 5 Seasonal Accounting`: "4d. **Turmoil update:** (i) Strain −1 (min 0) if ALL territories at Accord ≥ 2 this season (no territory-instability — per peninsular_strain §4.2, ED-797 correction; supersedes prior "no battles AND no Revolts" condition)."
- **Decision:** which predicate; the superseded one is still printed as live in two files.

**X-10 · What Mandate is.**
- `tracks.md › (header comment)` and `core (1).md › (comment before Faction Starting Stats)`: "Mandate = round(0.5 × Legitimacy + 0.5 × Popular_Support)" with faction-level L and PS.
- `faction_behavior_v30.md › §4 Mandate (REVISED by LPS-2e)`: "Mandate is **not** transitional and is **not** derived from faction-level L/PS (which do not exist — L/PS are per-settlement)… `Mandate(faction) = clamp(round(7 · T / (T + K)), 0, 7), T = Σ_s W_s·(0.5·L_s + 0.5·PS_s)/7, K = 6`". Same in `settlement_layer_v30 (1).md › §1.8`.
- Dozens of rules still treat Mandate as a primitive that is incremented: `faction_succession_split_v30.md › §2.3` "Stability −1, Mandate −1"; `strategic_layer_v30.md › P-20` "Faction Mandate cannot exceed 7"; `strategic_layer_v30.md › §9.9` "faction loses 1 Stability, 1 Mandate"; `ci_political_v30.md › §4.1` "Govern Overwhelming in own capital | +1"; `baralta_crown_claim_v30 (1).md › §3` "Crown Mandate inherited by Hafenmark at −2".
- **Decision:** whether Mandate is state or derived; if derived, every "Mandate ±N" rule must be re-expressed as a settlement L/PS change or deleted.

**X-11 · The faction stat schema (5, 6 or 7 stats).**
- `stats_1_7_scale (1).md › Stats (1–7 scale)`: "**Faction stats (6): Mandate / Influence / Wealth / Military / Intel / Stability.**"
- `core (1).md › Faction Starting Stats (v04 B5)` columns: "Legitimacy | Popular_Support | Influence | Wealth | Military | Intel | Stability" with the comment "canonical 7-stat schema (ED-787)".
- `settlement_layer_v30 (1).md › §6.2 Stage 4`: "full faction stat sheet (Mandate, Influence, Wealth, Military, Stability)".
- `stats_1_7_scale (1).md › Crown Covert Actions (PP-236)`: "Crown has NO Intel stat." versus the same file's `› Starting Stats` "Crown … Int 3".
- **Decision:** the stat list the engine stores; whether Crown has Intel.

**X-12 · Crown and Löwenritter Military.**
- `core (1).md › Faction Starting Stats`: Crown Military "5"; comment: "Crown Military here=5 CONFLICTS with stats_1_7_scale.md=4 (direction undetermined). See ED-869."
- `stats_1_7_scale (1).md › Starting Stats`: Crown Mil "5/6" with comment "prior value 4 struck per ED-869 / Jordan 2026-05-31".
- `geography.md › Varfell Territorial Expansion Constraint`: "Varfell 4+4+4+4+4 = 20 points (vs Crown 22, Church 25, Hafenmark 20)" — 22 is only reachable with Crown Military 4 (5+5+4+4+4); with 5 it is 23. Same "Crown | 22" in `strategic_layer_v30.md › Starting Stat Assessment`.
- Löwenritter: `core (1).md › Faction Starting Stats` "Löwenritter (Split) | 3 | 3 | 2 | 3 | 5 | 3 | 5"; `conflict_architecture_proposal.md › Graduated Löwenritter Autonomy` "Löwenritter = separate faction (M3/I2/W3/Mil6/Stab5)"; `core (1).md › Split row` "(L3/PS3/Inf2/W3/Mil5/Stab5)"; `stats_1_7_scale (1).md` "Löwenritter | — | — | 3 | 3 | 2/3 | — | — | 5/6 | 3 | 5/4"; `strategic_layer_v30.md › Starting Stat Assessment` "Löwenritter | 19 | Military 6".
- **Decision:** one integer per stat; the slash values "5/6", "2/3", "5/4" are not values.

**X-13 · Varfell starting Mandate / Wealth.**
- `core (1).md › CORRECTIONS`: "Varfell L 4, PS 4 … Wealth 4."; `stats_1_7_scale (1).md › Note`: "The table is authoritative; this note now matches."
- `strategic_layer_v30.md › G-10`: "**Recommendation:** Keep Varfell at Mandate 3, Wealth 3 for the board game." and `› Starting Stat Assessment`: "Varfell | 18 | … | Mandate 3, Wealth 3".
- **Decision:** 3 or 4.

**X-14 · The Löwenritter coup model: graduated stages vs a counter.**
- `core (1).md › Löwenritter Graduated Autonomy (replaces Coup Counter)`: "Loyal→Restless→Autonomous→Split … Replaces binary Coup Counter." Same in `conflict_architecture_proposal.md › Graduated Löwenritter Autonomy`, `campaign_architecture_v30.md › §5.3`, `worldbuilding_v30 (1).md › §4.3` ("fires when Autonomy track reaches Split stage, not on a single count-threshold trigger").
- `stats_1_7_scale (1).md › Löwenritter — Martial Law / Coup Trigger`: "Löwenritter action is triggered by Graduated Autonomy reaching 4. **Graduated Autonomy increments (+1 each):** … Counter never decrements. Fires at next seasonal accounting once at 4. (PP-577: threshold unified to 4…)".
- `baralta_crown_claim_v30 (1).md › §1 The Gap`: "Löwenritter Autonomy 4 → coup fires (PP-194)"; `› §7.4 Sequencing Rules`: "if Counter reaches 3, Coup fires"; `› §7.1`: "If Counter was at 2 when this trigger fires, Coup fires immediately."
- `institutions.md › Parliament Deposition Mechanic`: "Löwenritter Coup Counter immediately set to 4 (coup fires next season)."
- `core (1).md › Löwenritter Graduated Autonomy` also appends a fifth row "| **Coup** | Löwenritter loses faith in monarch AND has candidate … | T14 under Löwenritter. Crown faction SUSPENDED." after "Split", so the same table has both a four-stage and a five-state model.
- **Decision:** stages or counter; 3 or 4; whether "Coup" is a fifth state.

**X-15 · VTM: struck, but still load-bearing.**
- `tracks.md › VTM — STRUCK (PP-663, 2026-04-19)`: "Vaynard Thread Mastery track removed as faction-level stat."
- Live uses: `phases.md › Phase 5` "9b. … AND VTM ≥ 4"; `generational_transition_v30.md › PRESERVE` "All clocks (MS, CI, IP, PI, Strain, VTM, …)"; `parliament.md › Institutional Mandate Uphold/Appease` "VTM for Varfell"; `geography.md › Expedition Procedure` "VTM ≥ 2: −1 Ob … VTM +1 (Varfell only, if VTM ≥ 2)"; `geography.md › Varfell Path B` "VTM ≥ 3"; `campaign_architecture_v30.md › §4.1` "Varfell: knows (VTM track)"; `player_agency_v30 (3).md › §3.3` "Mend Gap, restore MS, or advance VTM"; `ci_political_v30.md › §6.2` "Military expansion only when VTM ≥ 2".
- **Decision:** each surviving VTM predicate needs a replacement (or deletion); `geography.md` also says "Restoration Weaver with Presence in T6: −1 Ob" and the Path-B table's VTM row has no substitute.

**X-16 · Territory numbering — three incompatible maps.**
- `geography.md › Territory Table`: "T1 | Valorsplatz | Crown … T3 | Lowenskyst … T9 | Himmelenger | Church … T10 | Spartfell | Hafenmark … T13 | Oastad … T14 | Ehrenfeld". Matched by `territory_temperaments_v30.md`, `tracks.md`, `core (1).md`, `ci_political_v30.md`.
- `worldbuilding_v30 (1).md › §9.1 Lore-to-Map Alignment` (column headed "PP-199 Territory"): "Valorsplatz | T12 … Lowenskyst | T8 … Himmelenger | T14 … Ehrenfeld | T9 … Stillhelm | T13 … Gransol | T5 … Rendstad | T6 … Spartfell | T7 … Varfell city | T1 … Sigurdshelm | T2 … Halvardshelm | T3 … Oastad | T4 Grauwald". `› §3.3`: "within 1 territory of T3 (Himmelstift/Himmelenger)".
- `campaign_architecture_v30.md › §5.3`: "Doux Alexios Laskaris of T11/T12 Altonian provinces" and "Crown Mandate +1 in T16-T17 region" (Löwenritter regions) — on the geography map T11/T12 are Varfell, T16 is Schoenland, T17 is Hafenmark.
- `strategic_layer_v30.md › Cascade Test 4`: "T6 (Hafenmark) … T9 (Varfell) … T14 (Restoration)"; `› Scenario C`: "Löwenritter March T5→T4 … T4 has Fort 2" (geography: T4 Fort 0).
- `institutions.md › Structure`: "Löwenritter Helm can deny T10 sea access to Schoenland" (T10 Spartfell is an inland border castle; the sea edge is T1↔T16).
- `valoria_political_hierarchy_v30.md › §4`: "T1..T17 nomenclature deprecated".
- **Decision:** confirm the geography numbering and retire the other two; every T-number in `worldbuilding_v30 §9.1`, `campaign_architecture §5.3`, `strategic_layer` examples and `institutions` has to be remapped by hand.

**X-17 · Where Parliament sits (Ministry mechanics).**
- `ministry.md › Ministry Tokens`: "Starts with AP-tokens in T14 (Ehrenfeld), T2 (Kronmark), T5 (Feldmark), T1 (Valorsplatz). … (PP-204 corrected.)" and `› Ministry Stabilisation`: "AP-token in T1 (Valorsplatz, Parliament seat)".
- `ministry.md › Ministry NPC AI Priority Tree` and every rule after it: "Ministry plays Consul Inward (Govern) in T13", "T13 has no Ministry AP-token", "If Ministry has AP-token in T13: Hafenmark Parliamentary Manoeuvre Ob −1", "Church seizes T13 with AP-token present", "AP-tokens in T13 and T12 are removed". T13 is Oastad (Varfell).
- **Decision:** replace T13→T1 (and T12→?) throughout, or accept that the Ministry's engine runs in Varfell's southern fjords.

**X-18 · The settlement registry (36 vs 37; S-IDs reassigned).**
- `settlement_layer_v30 (1).md › §1.1`: "Settlement | S-001 to S-036 | 36"; `› §4.5`: "Total: ~45–50 across 36 settlements"; `settlement_adjacency_v30.md › §1.2`: "(36 settlements) … 49 edges"; `march_layer_v30.md › §8.1`: "36 settlement nodes + 26 adjacency edges".
- `settlement_layer_v30 (1).md › PART 2`: "**35 settlements across 14 provinces in 3 duchies** … canonical adjacency-graph total to **37 settlements**"; `valoria_political_hierarchy_v30.md › (header)`: "the 56-edge canonical march-route graph".
- Old S-IDs remain live in rules after the renumbering: `conflict_architecture_proposal.md › Starting Friction Points` "S003 Valorsplatz Cathedral … S017 Market Quarter … S014 Barracks … S029 Lodge … S032 Shrine"; `phases.md › Game Setup` "S014 Barracks"; `fractional_province_ownership_v30.md › §3` "S-017 Gransol Market Quarter"; `settlement_layer_v30 (1).md › §4.1` "S-015 Gransol Parliament … S-017 Gransol Market Quarter", `› §5.1` "Lowenskyst Fortress (S-006, Defense 4)", `› §6.3` "S-015 Gransol Parliament … S-010 Stillhelm … S-003 Valorsplatz Cathedral … S-023 through S-025"; `faction_politics_v30.md › §2.1` "Löwenritter-managed settlement (S-012, S-014)". Under the new registry `› §2.1`, S-012 = Stillhelm, S-014 = Ehrenfeld, S-015 = Nordhain, S-017 = Holzbrück, S-029 = Geirsvik, S-032 = Brynjard, S-006 = Goldenfurt, S-010 = Erntehof.
- **Decision:** one registry; every S-ID in a rule re-pointed. `settlement_layer §2.3` says the migration is "lazy"; the engine cannot be lazy.

**X-19 · Province count and settlements-per-province.**
- `settlement_layer_v30 (1).md › §1.1`: "Province | T1–T17 | 17"; `geography.md`: "17 territories".
- `valoria_political_hierarchy_v30.md › §2.1`: "14 provinces total in the duchy hierarchy = 35 settlements" plus three special cases; same file `› §1.1`: "each province is comprised of 1–3 territories (settlements)" and `› §2.1`: "**The minimum is 2 — every province in the Kingdom must have at least two settlements**".
- **Decision:** 17 nodes or 14+3; "1–3" or "2–3".

**X-20 · How far an army moves in a season.**
- `settlement_adjacency_v30.md › §1.3 Army Movement`: "**Intra-province:** traverse 1 edge per season" and, four lines later, "Per season, an army may move up to **Military ÷ 2 edges** (round down, minimum 1)."
- `march_layer_v30.md › §1 March Budget`: "march_budget_pixels = Military × 100 × cavalry_modifier … × skirmish_modifier" with "Cost per traversed segment: `distance_px × terrain_cost_multiplier`".
- `core (1).md › Standard Action Ob Reference`: "March (Legionary Outward) | No roll | Contested entry = Battle"; `strategic_layer_v30.md › P-21`: "March (Legionary Outward) | 2 | +1 in T8 (Difficult terrain)".
- **Decision:** edges-per-season, Military÷2, or pixel budget; roll or no roll.

**X-21 · Accord range vs the insurgency promotion threshold.**
- `tracks.md › Accord (Per-Territory, 0–3)`, `core (1).md`, `geography.md`: Accord is 0–3.
- `insurgency_pipeline_v30.md › §5.1 Promotion trigger`: "**Accord ≥ 4** averaged across held territories (population acceptance)". Unreachable. The same file's `› §4.2` gives "Legitimacy | 1.0 | Float" and `› §6.2` "Legitimacy < 1.0" while `core (1).md › Stat Ceilings and Floors` has Legitimacy "0 | 7" integer.
- **Decision:** the promotion predicate; integer or float Legitimacy.

**X-22 · Standing range and leadership thresholds.**
- `faction_politics_v30.md › §1.0`: "Replace the 0–5 Standing track with an eight-position ladder (Standing 0 through Standing 7)"; `player_agency_v30 (3).md › §5.1`: "The Standing ladder runs 0–7".
- `player_agency_v30 (3).md › §5.4`: "Standing (0–5) measures the player's relationship with one faction"; `› §8`: "Standing track (0–5) … Standing 5 enables succession or leadership challenge."; `settlement_layer_v30 (1).md › §6.1`: "The existing Standing track (0–5 per faction)"; `› §3.2`: "5 (Successor)"; `strategic_layer_v30.md › P-15`: "Standing: Cannot exceed 5."
- `player_agency_v30 (3).md › §5.2`: "a Standing 4+ character can call a leadership challenge at any time" vs `› §8` "Standing 5 enables … leadership challenge" vs `› §5.1` Standing 7 "can initiate a leadership challenge OR succeed on leader vacancy."
- **Decision:** 0–7 everywhere; the challenge threshold.

**X-23 · What a successor character inherits.**
- `generational_transition_v30.md › RESET / TRANSFER`: "Disposition toward PC: all NPCs reset to faction-default"; "All Knots: rupture"; "Renown: reset to 0, but predecessor's Renown ≥ 7 grants +1 starting Renown"; "Resources: floor(predecessor's Resources / 2) + new character's starting Resources".
- `player_agency_v30 (3).md › §10 Conviction Legacy`: "Renown inherited: floor(predecessor ÷ 2). Dispositions: predecessor's allies (+3) start at +1; enemies (−2) start at −1; others at 0. Knotted NPCs: Knot does not transfer but +1D on first Connect (Knot scar)." `settlement_layer_v30 (1).md › §7.2`: "inheriting Renown ÷ 2 (round down)". `campaign_architecture_v30.md › §7.4`: Mentorship "Skills at 60%, Founded Org membership, 1 Close Knot (Disposition −2)" vs `generational_transition` "Skills: per new character lifepath (predecessor's skills die with them)".
- **Decision:** one inheritance table (the generational spec says it is "Canonical in player_agency_v30 (proposed §11)", but §11 there says something else).

**X-24 · The Church building model and the seizure-modifier cap.**
- `campaign_architecture_v30.md › §1.1`: per-settlement "None / Chapel (+0.5 PT/season) / Church (+1 PT/season) / Cathedral (+2 PT/season, +0.5 to adjacent)" with Seizure mods "0 / 0 / −1 / −2", Templar −1, Inquisitor −1, Governor −2; `› §1.2`: "Maximum per-settlement Seizure Ob modifier: −6".
- `settlement_layer_v30 (1).md › §1.5`: same axes but "Cap: −4 per settlement (campaign_architecture_v1 refinement)."
- `institutions.md › Parish / Cathedral System — Church (ED-319 RESOLVED)`: per-territory "Parish: 2 sequential successful Consul Inward actions + 1 Wealth. Effect: PT floor raised to 1 … Cathedral: 3 more … + 2 additional Wealth. Effect: PT floor 2 + Church Prominence +1 … Max 1 Parish or Cathedral per territory."
- **Decision:** settlement axes or territory Parish/Cathedral; −6 or −4.

**X-25 · Crown Treaty difficulty.**
- `core (1).md › Standard Action Ob Reference`: "Formal Crown Treaty (Senator Outward) | floor(target L / 2) + 1".
- `treaty_expiration_v30.md › §2`: "**Ob** | Target faction Sta (lower-stability targets are receptive)"; "**Pool** | Influence + Standing modifier".
- `stats_1_7_scale (1).md › Domain Action Resolution`: "Positioning (contested): M = own Influence − target Influence … Ratification: M = Mandate − 2".
- **Decision:** one.

**X-26 · Reconstitution difficulty.**
- `institutions.md › Löwenritter — Reconstitution`: "Roll: L vs Ob 3." `stats_1_7_scale (1).md`: "Reconstitute: M = Influence − 6 (legacy Ob 4 → difficulty 6)." `strategic_layer_v30.md › §9.10`: "reconstitute the faction via Influence Domain Actions (Ob 4, multi-season)".
- **Decision:** pool (L or Influence) and difficulty (3 or 4→6).

**X-27 · CI passive and Suppress.**
- `stats_1_7_scale (1).md › CI Passive Advance (PP-402)`: "advances by **+1 per season** from institutional momentum, regardless of Church action."
- `ci_seizure.md › CI Generation`: "1. **Conditional Passive (§3.2):** CI +1 only if Church L > controlling faction L in ≥ 2 territories."; `ci_political_v30.md › §0`: "CI passive | PP-402 unconditional +1 | Conditional passive".
- `settlement_layer_v30 (1).md › §7.1`: "Passive +1/season if Church Mandate ≥ 3 (existing conditional)."
- Suppress Ob: `stats_1_7_scale (1).md`: "Ob = floor(Church L / 2) + 1 ÷ 2 (round up, min 1)" vs `ci_seizure.md`: "L vs Ob = floor(Church L / 2) + 1" vs `stats_1_7_scale (1).md › Domain Action Resolution` "Suppress — M = Mandate − (Church-L difficulty)".
- **Decision:** three passives, three Suppress forms.

**X-28 · Community Weaving / Organising — pool and Ob.**
- `core (1).md › Standard Action Ob Reference`: "Community Organising (Restoration) | 2 | Pool: 1D base + 1D per adjacent territory with RM Presence marker" and "Community Weaving (Restoration) | (100−MS)÷20 round up min 1 | −1 per Presence marker".
- `insurgency_pipeline_v30.md › §3.3`: "Community Weaving | Influence vs Ob = Thread Tension ÷ 20 (round up, min 1). Requires TS 30+ practitioner affiliated."
- `stats_1_7_scale (1).md › Restoration Movement — Community Weaving [SUPERSEDED by PP-616]`: "PP-616 unifies all Thread operations under a single pool formula: `(Spirit × 2) + History + TPS` … removes the Domain Action framing".
- `campaign_architecture_v30.md › §2.2`: ""Community Organizing" for RM is political organizing, NOT a Thread operation … Uses social stats (Charisma, Attunement), not Thread stats (Spirit)". `strategic_layer_v30.md › G-06`: "Ob = ceil((100−MS)/20) min 1".
- **Decision:** whether the RM action is a Thread operation; its pool; its Ob (MS-based or TT-based — and whether TT ≡ 100−MS, see X-32).

**X-29 · Province Value per territory — three tables.**
- `core (1).md › Starting Piety Track (PT) values` (column actually headed "Starting PV"): T2 2, T4 2, T5 2, T10 3, T16 1, T17 2; "Total: 40. Jordan-confirmed 2026-04-23."
- `ci_political_v30.md › §1` PV column: "T2 | Kronmark | 1 … T4 | Grauwald | 1 … T5 | Feldmark | 1 … T10 | Spartfell | 1 … T16 | Schoenland | — … T17 | Halvarshelm | 1" (sums to 33).
- `geography.md › Starting Control`: "Crown … Starting TCV 12; Hafenmark … 6; Varfell … 6; Church … 5". The core table gives Crown 16 / Hafenmark 10 / Varfell 8; the ci_political table gives 14 / 7 / 7. Neither yields 12/6/6. `early_game_ignition_analysis.md › §1`: "Crown holds 14 PV".
- **Decision:** one PV table.

**X-30 · The Forgetting Check.**
- `southernmost.md › Forgetting Check`: "Pool: Cognition + Recall. TN 8. TS bonus: TS ÷ 20 (round down) … Boundary zone < 1 hour | 1 … Einhir core sites | 4".
- `geography.md › Expedition Procedure`: "Roll: Champion pool (TS ÷ 10, rounded down, min 1D, max 3D) vs Ob 3 … 3. **Forgetting Check (on entry into T15):** Same pool vs Ob 2."
- `strategic_layer_v30.md › G-06`: "Influence + 1D per Presence marker in T13 (Restoration) OR Intelligence stat (Varfell) OR Wealth ÷ 2 rounded up (other factions) … Ob 1 (floor applies)."
- **Decision:** one check (or a declared scale split, which none of the three states).

**X-31 · IP thresholds and starting value.**
- `core (1).md › Starting Values`: "IP | 20 | 0–100 | IP 75 = Altonian Vanguard appears. IP 80+ = sustained Vanguard presence … IP ≥ 100 = Altonia regularly invades"; `geography.md › T16`: "IP ≥ 75: Vanguard deploys"; `› NW Pass`: "Fires at IP ≥ 90"; `march_layer_v30.md › §6.3`: "IP ≥ 75 → Altonian sea route opens".
- `campaign_architecture_v30.md › §5.1`: "**Phase 1 (IP reaches 100):** First mountain pass … **Phase 2 (IP sustained 85+ for 3 seasons after Phase 1):** Second corridor through Schoenland … **Phase 3 (IP sustained 80+ …):** Third corridor northwest."
- `conflict_architecture_proposal.md › What's Cut`: "IP starts at 0".
- `strategic_layer_v30.md › Scenario C`: "AER 3 raises threshold to 80" (AER is removed per `tracks.md`).
- **Decision:** start 0 or 20; the escalation ladder (75/90/100 or 100/85/80); whether Schoenland and the NW pass are corridors 2 and 3 or fire at 75/90.

**X-32 · Same abbreviation, two clocks; same clock, three names.**
- `IP`: "Invasion Pressure" (`core (1).md`, `clocks.md`, `geography.md`) vs "Institutional Pressure" (`stats_1_7_scale (1).md › Clock Starting Values`, `strategic_layer_v30.md › G-11` and `Scenario C`, `baralta_crown_claim_v30 (1).md › §7.2`, `worldbuilding_v30 (1).md › §3.6`).
- `PI`: "Parliament Integrity" (`parliament.md`, `core (1).md`) vs "Public Instability" (`stats_1_7_scale (1).md › PP-255` "PI ≥ 8: revolt check … PI = 10: GM narrative uprising event"; `› ED-174` "At PI ≥ 8").
- `MS` / `RS` / `TT`: `worldbuilding_v30 (1).md › (footer)` "TC→CI + RS→MS abbreviation disambiguation"; yet `phases.md › Phase 5` "RS baseline drift", `tracks.md › Turmoil` "RS −1/season additional" (`core (1).md` has "MS −1/season additional" in the same row); `southernmost.md` runs entirely on "Thread Tension" ("Thread Tension ≥ 40", "TT 50 … Cracking begins") with no stated relation to MS; `strategic_layer_v30.md › §9.8` lists "Thread operation clock changes (MS, TT)" as two clocks.
- **Decision:** one glossary; whether TT is 100−MS or a separate clock.

**X-33 · Documents that are PROVISIONAL and CANONICAL at once.**
- `territory_temperaments_v30.md`: "STATUS: PROVISIONAL" (comment) and "## Status: CANONICAL". `fractional_province_ownership_v30.md`: "## Status: CANONICAL" then "**Status:** PROVISIONAL". `settlement_adjacency_v30.md`, `faction_succession_split_v30.md`, `march_layer_v30.md`: identical pattern. `faction_behavior_v30.md`: "[CANONICAL: 2026-05-01 …]" / "STATUS: PROVISIONAL" / "## Status: CANONICAL" / "**Status:** PROVISIONAL" / "**End spec. PROVISIONAL pending ratification.**". `valoria_political_hierarchy_v30.md`: "Class A canonical foundational document" / "**Status:** PROVISIONAL." `faction_politics_v30.md`: "## Status: CANONICAL (approved Jordan 2026-04-17, commit PP-660)" and last line "this is a proposal document in /mnt/user-data/outputs/ for downstream approval".
- **Decision:** which header binds; this matters because X-05/X-06/X-24 pit "canonical" files against each other.

### Tier B — rules and entities with two definitions

**X-34 · Tensions Deck size and draw.** `early_game_ignition_analysis.md › (header)`: "Tensions Deck rescoped to 6 external bilateral cards, draw 2 (was 8 mixed cards)"; `conflict_architecture_proposal.md › Tensions Deck (Rescoped)`: "6 cards, draw 1 at game start"; `phases.md › Game Setup`: "Draw 1 card from 6". Decision: draw 1 or 2 (the superseding note misdescribes the superseder).

**X-35 · Royal Deposition predicate.** `baralta_crown_claim_v30 (1).md › §1`: "Royal Deposition (PI ≥ 5 + Church Mandate ≥ 5 + Crown Mandate ≤ 1 + 2 Standing tokens)"; `institutions.md › Parliament Deposition Mechanic`: "PI ≥ 5 (Parliament functional), Church L ≥ 5 (Holy See has standing), Crown L ≤ 1 (Monarch deemed unfit), AND at least 2 other player factions have active Standing tokens against Crown." After X-10, Mandate and L are different quantities. Decision: which.

**X-36 · Does the Restoration Movement have stats.** `core (1).md › Faction Starting Stats`: "Restoration Movement | — … No faction stats. Operates via Presence markers and Community Weaving only. (PP-460)"; `insurgency_pipeline_v30.md › §3.2 Latent RM characteristics`: "Mandate | Count of territories with PT ≤ 1 (min 2, max 5) … Influence | 4 … Wealth | 1 … Military | 0 … Stability | 3"; `strategic_layer_v30.md › Scenario B`: "complete stats (Mandate 2, Influence 4, Wealth 2, Stability 3)"; `› Starting Stat Assessment`: "Restoration | 11 | Influence 4 | Military 0, Mandate 2". Decision: statless or the Latent-RM sheet.

**X-37 · Ethical Framework modifiers — struck and live.** `core (1).md › ~~Ethical Framework Modifiers~~`: "SUPERSEDED 2026-05-01 (PP-686 v2)"; `stats_1_7_scale (1).md`: "Retained below struck … do not implement"; `faction_behavior_v30.md › §3.7` replaces them. But `faction_politics_v30.md › §1.1`: "**Faction ethical framework:** Virtue … Visible, public, virtuous actions are −1 Ob; covert or morally ambiguous are +1 Ob."; `› §1.2` "Categorical Imperative … −1 Ob; … +1 Ob"; `› §1.3` "Utility-driven Pragmatism … −1 Ob … +1 Ob"; `› §1.4` "Faith … Thread-revealing actions are +2 Ob." `strategic_layer_v30.md › Cascade Test 1`: "doctrine-aligned −1 Ob". Decision: strike from `faction_politics` too.

**X-38 · Niflhel — dissolved and live.** `conflict_architecture_proposal.md › Niflhel Dissolution`: "Strike Niflhel as a faction." (also `core (1).md`, `ministry.md`, `stats_1_7_scale (1).md`). Live: `faction_politics_v30.md › §2.6 Niflhel Ladder` (full four-arm ladder, "Brokers … Thread Tension +0.5 per season"); `settlement_layer_v30 (1).md › §3.3` "Niflhel | Any (covert) | … Intel-gathering at +1D", `› §4.2`, `› §4.6` "Niflhel supply nodes"; `geography.md › T12`: "Niflhel Black Market: Trade +1 Ob, Niflhel Covert −1 Ob"; `governance_play_redesign_v1.md › §1.3` "Surface a covert actor (Niflhel/RM)"; `player_agency_v30 (3).md › §7.1` advisory text "covert paths (Riskbreakers, Niflhel, Wardens)"; `faction_politics_v30.md › §3.2` "Niflhel | … Favored". Decision: delete or reinstate.

**X-39 · AER — removed and live.** `tracks.md`: "[REMOVED 2026-05-04] AER … track removed." `strategic_layer_v30.md › Scenario C` still resolves on AER ("AER 3 raises threshold to 80 … AER −2"); `faction_politics_v30.md › §1.4 Standing 5`: "an Altonian Church acknowledgment (if AEA ≥ 3 per conviction_track_v30 §4.2)" (AEA is defined nowhere). Decision: replacement for the Vanguard-threshold and Prelate-deed hooks.

**X-40 · Battle Ob / defender bonus.** `ci_seizure.md › Battle Ob Formula`: "**Battle Ob = floor(defender Military / 2) + 1.** Attacker rolls: Military pool vs Ob." `strategic_layer_v30.md › P-16`: "Both sides roll simultaneously. Compare net successes." `geography.md › Fortification Combat Rule`: "defending faction adds Fort level as bonus dice". `settlement_adjacency_v30.md › §2.2`: "Fortress | +Fort Level to Defender Ob". `clocks.md › Altonian Vanguard`: "automatic Battle (defender Military vs Ob 3)"; `tracks.md › Accord 0`: "Popular Uprising (Military vs Ob 2)". `settlement_layer_v30 (1).md › §5.2`: "effective Defense = settlement Defense + garrison Discipline". Decision: one battle-entry resolution; Fort as dice, as Ob, or as Defense.

**X-41 · Ministry roster and the two "Ministry Collapse" rules.** `institutions.md › Ministry — Canonical Identity`: "Ministry of Law, Ministry of Guilds, Ministry of Logothetes, Ministry of Granaries, Ministry of Pure Water." `faction_politics_v30.md › §7.1`: "The six Ministries remain as specified (Haushalt, Kriegsamt, Kirchenamt, Gerichtsamt, Schattendienst, Markamt)." `ministry.md › Ministry Collapse (L 0)`: "Ministry ceases NPC actions for 2 seasons." `worldbuilding_v30 (1).md › Card: Ministry Collapse`: "Trigger: Crown Stability drops to 2 or below." Decision: one roster; rename one of the two mechanics.

**X-42 · Ministry L thresholds (internal).** `ministry.md › Ministry and Crown Policy`: "If Ministry L < 2 …: Crown Policy actions cost +1 Ob … If Ministry L = 0: Crown Policy actions unavailable"; `› Ministry and PI Track — Summary`: "Ministry L ≤ 1 | Crown Policy unavailable". At L = 1 these disagree. Decision: which.

**X-43 · Cardinal challenge / schism trigger.** `institutions.md › Four Cardinals`: "When Church Stability drops below 3, one Cardinal may challenge the Confessor"; `› Cardinal schism trigger`: "If Church Stability = 2 AND any faction played a Senator action targeting Church this season: one Cardinal (random or GM discretion) challenges"; `tracks.md › TD 2`: "Cardinal of Fortitude schism risk when Church Stability < 3"; `early_game_ignition_analysis.md › §9 item 4`: "When Church Stability ≤ 3 (note: lower bar than current ≤ 2 schism trigger)". Decision: threshold and whether a Senator action is required.

**X-44 · Territory Prosperity range.** `strategic_layer_v30.md › P-22`: "Each territory has a Prosperity value (0–5)"; `settlement_layer_v30 (1).md › §1.3`: settlement "Prosperity/Defense/Order, 0–5"; `geography.md › Territory Table`: "T1 | Valorsplatz | Crown ★ | 2 | 6". Decision: cap or T1's value; also whether territory Prosperity is its own track or the settlement sum (`settlement_layer §1.3`: "Each point of settlement Prosperity adds to the province's Prosperity pool" — T8's settlements sum to 6 in `fractional_province §3` while `geography` lists T8 Pros 5).

**X-45 · Treasury derivation.** `settlement_layer_v30 (1).md › §1.3`: "Prosperity | Local Economy | Prosperity × 50 | Gold income contribution to faction Treasury"; `› §1.8`: "faction Treasury income = `Σ settlement Prosperity × 10`, derived_stats §8.1"; `› §4.3`: "Mine type + Prosperity 3+ | Resource surplus. Province Treasury +50/season". Decision: ×10 or ×50.

**X-46 · Fractional PV rounding.** `fractional_province_ownership_v30.md › §2.2`: "(rounded to 1 decimal)"; `› §5`: "**PV share rounding:** currently 2-decimal." Decision.

**X-47 · Parliamentary Transfer Accord on success.** `parliamentary_transfer_v30.md › §1.2`: "Transferred territory Accord = 1."; `› §2 Appeasement`: "Accord granted +2 instead of +1 on Success". Decision: set-to or add-to.

**X-48 · Deniability Debt cooling-off threshold.** `faction_politics_v30.md › §2.2b.ii Reduction`: "−1 (cooling off; does not apply if Debt ≥ 5)"; `› Thresholds`: "4 | Cooling-off reduction disabled (Debt sticks above 4)." At Debt 4 these disagree.

**X-49 · Torben Readiness threshold.** `faction_politics_v30.md › §8.1`: "**Accumulated Generational Readiness ≥ 5.**" fires the trigger; `› §8.3`: "At Readiness ≥ 7, Torben exits "ward" status"; `baralta_crown_claim_v30 (1).md › §7.1`: "Readiness ≥ 5 (precocious)". Decision: 5 or 7, or two tracks.

**X-50 · Warden Recognition range and the +1D Thread bonus.** `core (1).md › Starting Values`: "Warden Recognition (WR) | 0 | 0–3"; `geography.md › Varfell Path B`: "**WR track (0–4):** … WR 3: Wardens actively cooperate (+1D Thread ops peninsula-wide) … WR 4: Edeyja has made substantive contact"; `core (1).md › Warden Cooperation (WC) Effects`: "≥ 1 | +1D to all Thread operations peninsula-wide." Decision: WR 0–3 or 0–4; which track carries the +1D.

**X-51 · Excommunication Ob.** `tracks.md › Church Excommunication Ob Cap (PP-180)`: "Ob = floor(target L / 2) + 1."; `stats_1_7_scale (1).md › Church — Excommunication`: "contested (faction leader): M = Mandate − target Mandate; non-leader: M = Mandate − 2".

**X-52 · Political pool against the Church.** `ci_seizure.md › Faction Political Pool`: "**Non-Church (anti-Church motions):** Political pool = L − floor(CI/30)."; `ci_political_v30.md › §3.4`: "**max(0, Mandate − ⌊CI/30⌋)** votes — floored at 0". L vs Mandate; floor vs none.

**X-53 · Public Instability accrual.** `stats_1_7_scale (1).md › PP-237`: "Hybrid increases: +1 per season Revolution Agitation resolves (any degree); +1 per season IP increases while CI > 40. Hybrid decreases: −1 per season Crown or Guilds completes successful social Domain Action"; `› PP-255`: "Accrual: +1/season any faction PS < 3 at accounting. Recovery: −1/season zero hostile Stability-targeting DAs." Two accrual rules for one clock.

**X-54 · Löwenritter autonomy increments.** `stats_1_7_scale (1).md › Löwenritter — Martial Law`: "+1 each: Church Influence reaches 40 while Crown took no action …; Torben's loyalty reaches 3–2 or lower; Crown loses 2+ territories in one season without a military response"; `core (1).md › Graduated Autonomy` stage triggers: "Crown Stability ≤ 3, OR no military action 4+ seasons, OR Crown loses a province". Different predicates for the same track.

**X-55 · Hafenmark's coast and the Altonian passes.** `geography.md › Geographic Trade Notes`: "Hafenmark is fully landlocked"; `territory_temperaments_v30.md › T8`: "constitutional capital + west-sea trade + Schoenland route"; `settlement_adjacency_v30.md › §1.2`: "Gransol Harbor (S-016)"; `settlement_layer_v30 (1).md › §2.2`: "Gransol Harbor district | Lake-harbor district | … (Gransol is on a lake — landlocked Switzerland-like province)". Passes: `geography.md › Altonian Mountain Passes`: "NE Pass | T10 (Spartfell) … NW Pass | T3 (Lowenskyst)"; `territory_temperaments_v30.md`: "T3 | Lowenskyst … NE Altonian-pass garrison" and "T10 | Spartfell … NW Altonian-pass garrison". Decision: which pass is where; sea or lake at Gransol.

**X-56 · Season structure.** `phases.md`: Phase 4 (seven priority tiers) then "Phase 5 Seasonal Accounting … 13-step sequence"; `player_agency_v30 (3).md › §7.2`: "Phase 1a — Duty Assignment. Phase 1b — Scene Slate Generation. Phase 1c — Personal Phase. Phase 2 — Strategic Phase. Phase 3 — Accounting."; `strategic_layer_v30.md › §9.1`: "Phase sequence: Personal → Strategic → Cascade" with "§9.8 Cascade Sequence — 5 Steps"; `conflict_architecture_proposal.md › The Three Scales`: "**Resolution order each season:** Settlement → Province → Peninsula." Step 11: `phases.md`: "11. [DISSOLVED — Hollow Victory totals no longer tracked…]" vs `ministry.md`: "fires at Accounting Step 11, before Hollow Victory totals" vs `phases.md › Year-End`: "6. Hollow Victory totals announced publicly." Decision: one season skeleton.

**X-57 · Piety Yield "PT tier" and CI cap.** Not a contradiction but an inconsistency in the yield examples: `ci_political_v30.md › §1`: "T9 (SW 5, PT 5): yield = 1.0 × (5/5) = 1.0 … T8 (SW 3, PT 3): yield = 0.25 × (3/5)"; `ci_seizure.md`: "CI += Σ(PT tier × SW/5) per prominent territory, floored." The "PT tier" map (PT 5 → 1.0, PT 3 → 0.25) is defined only by example — see U-03. Listed here because `settlement_layer_v30 (1).md › §7.1` models CI as "+1/season" flat, contradicting the yield model.

**X-58 · Parliamentary Transfer balance arithmetic.** `parliamentary_transfer_v30.md › §5`: "Crown | 24.7% … Church | 28.6% … Hafenmark | 24.2% … Varfell | 22.5% … Mean deviation from 25% target: 7.2pp." The four deviations (0.3, 3.6, 0.8, 2.5) average 1.8pp. `treaty_expiration_v30.md › §5`: "all configs within 7-10pp deviation at N=1000" — a different quantity under the same wording. Consequence: a build that gates on "7.2pp" reproduces a number that the printed data do not produce.

**X-59 · Temperament aggregates.** `territory_temperaments_v30.md › §3`: "Crown | T1, T2, T3, T5, T6, T14 | … | α≈0.50, β≈0.50" — the six listed α values (0.7, 0.3, 0.5, 0.3, 0.9, 0.5) average 0.533; "Hafenmark | T7, T8, T10, T17 | … | α≈0.55, β≈0.45" — the four listed values (0.3, 0.7, 0.5, 0.5) average 0.50. Low consequence (the table is authoritative and the summary is derived), but an implementer copying the summary gets the wrong seed.

**X-60 · Conviction taxonomy.** `faction_behavior_v30.md › §3.3.1`: 13 Convictions "Virtue, Authority, Honor, Faith, Warden, Scholastic, Precedent, Order, Utility, Liberty, Equity, Community, Identity" (PP-684). `faction_politics_v30.md › §10.2 ED-641`: "Warden Conviction formalization as 6th Conviction (alongside Faith/Order/Reason/Equity/Autonomy/Precedent/Continuity/Community — confirm total list" — eight names listed as a "6th" addition, and inner-circle NPCs carry "Autonomy" and "Continuity", which are not in the 13. `faction_politics_v30.md › §1.0a`: "Crown member shifts to Autonomy primary". Decision: the vector space `cascade_fidelity` is computed in.

**X-61 · Mass Seizure "Church Prominent" naming.** `ci_political_v30.md › §2.1 CI 55`: "*(Renamed from "Church Prominent" 2026-04-29 — "Church Prominent" is reserved for the CI generation prerequisite in military_layer_v30 §3.2…)*" vs `faction_politics_v30.md › §5.2`: "At CI 55+ (Prominent milestone)". Name reused after reservation.

**X-62 · Seizure "one-shot" vs "one seizure attempt per season".** `ci_seizure.md › Seizure Constraints`: "One seizure attempt per season." vs the same file's "One attempt only." / "One-time event."

### Tier C — names, IDs, bookkeeping

**X-63 · RM leader / contact names.** `worldbuilding_v30 (1).md › §8`: "**Proposed: Elder Solvei Kaldring**"; `stats_1_7_scale (1).md › Restoration Movement — Named NPCs (ED-005 resolved)`: "1. **MARET VOSSEN** — Primary contact"; `stats_1_7_scale (1).md › ED-005 Resolution (PP-286)`: "Primary NPC contact: **Yrsa Vossen** (confirmed existing)"; `campaign_architecture_v30.md › §2.3`, `faction_succession_split_v30.md › §3`: "Yrsa Vossen". "Maret" is also Maret Uln (Varfell). Decision: one name per person.

**X-64 · Other name pairs.** Baralta "Inga | Inge" (`worldbuilding_v30 (1).md › §2`); "Himlensendt" (`core`, `faction_politics`) vs "Himmensendt" (`strategic_layer_v30.md › Scenario A`); "Almud" vs "Almund" (`valoria_political_hierarchy_v30.md › §1.1`: "**Almund** (Almud)"); "Halvardshelm" (T11, Varfell) vs "Halvarshelm" (T17, Hafenmark) — one letter apart; "Dienton Vaynard" superseded by "Magnus Vaynard" (`worldbuilding §2`) but the succession example says "Duke Magnus Vaynard" while `core (1).md` Conviction table says "Varfell (Vaynard)"; Torben the heir vs "Torben (Sr Jarl West)" in `faction_politics_v30.md › §3.5` (renamed to Björn Holdar in `› §1.3c`) and "Ehrenwall (Skald)" there (renamed Ingrid Stenskald); "Confessor (Cardinal of Faith)" (`valoria_political_hierarchy_v30.md › §1.2`) vs the four Cardinals Fortitude/Justice/Prudence/Temperance (`institutions.md`, `worldbuilding`).

**X-65 · Patch/editorial ID collisions.** PP-494: "Torben Loyalty transfers to Löwenritter (PP-494)" (`baralta_crown_claim_v30 (1).md › §1`) vs "Graduated Seizure PP-494" (`ci_seizure.md`). ED-781: "replaces the prior Coup Counter (ED-781)" (`conflict_architecture_proposal.md › Assessment`) vs "ED-781 | Phase 4 stress tests" (`march_layer_v30.md › §9`). PP-244: "Scene→Mass Transition Modifiers — Hybrid (PP-244)" and "PP-244 — PC excommunication succession" (`stats_1_7_scale (1).md`). PP-246: "Ethical Framework Modifiers — Löwenritter (PP-246)" and "PP-246 — DA→Contest escalation" (same file). "CI = Church Influence (… renamed from Church Influence per ED-782)" (`faction_politics_v30.md › Glossary note`) — a rename from itself.

**X-66 · Duplicated sections with drift risk.** Whole sections appear twice inside `ministry.md`, `institutions.md`, `tracks.md` (RDT/TD), `ci_seizure.md` (Mass Seizure), `geography.md` (SW, roads, passes, Southernmost Access), `core (1).md` (Playable Factions). Today the copies match; any single-copy edit produces a contradiction with no marker. Recorded so a build de-duplicates before parsing.

**X-67 · `parliament.md` cross-references its own missing sections.** "Effects table: §PI Thresholds above. (PP-553)" — there is no such section in the file; "[Full Policy table in faction card section]" — none in the corpus.

---

## 2. Underspecification — rules a machine cannot execute

Each entry quotes the rule and names the missing decision. Ordered roughly by how much of the engine waits on it. "No-GM holes" (the corpus delegating to a referee) are collected at U-01 because every one of them is the same missing decision: *who decides, by what predicate*.

**U-01 · Explicit referee delegations in a no-GM engine.**
- `parliament.md › Open Pledge System (PP-515)`: "**Forced breach exemption:** Pledge honoured if breach results directly from responding to another faction's military action in the pledged territory, provided the pledging faction's card was not yet played when the threat arose. GM adjudicates." — Missing: the predicate for "results directly from responding to".
- `institutions.md › Cardinal schism trigger`: "one Cardinal (random or GM discretion) challenges the Confessor." — Missing: the selection rule (uniform random? weighted by arm?).
- `worldbuilding_v30 (1).md › §3.2`: "**Jarnstal Drift (0–3, Game Master-tracked, private)**"; `› §4.2`: "Game Master rolls Riskbreaker Intel vs Ob 2." — Missing: who "orders" a Riskbreaker to act against the conviction; what makes an order conviction-violating.
- `strategic_layer_v30.md › P-12`: "one additional immediate consequence (Game Master discretion: −1 Standing, −1 Stability, or one stat degradation)" (struck later in the same file — but the strike is itself contradicted at X-02).
- `strategic_layer_v30.md › §9.3`: "if the Game Master judges a consequence is simple enough to track inline … they may apply it immediately"; `› §9.4`: "the Game Master sequences them by dramatic logic (most consequential first). No strict mechanical priority."; `› §9.5`: "The Game Master determines this at the Cascade phase ledger"; `› §9.12`: "tied to the Player Character's TTRPG Belief arc by the Game Master"; `› §9.13`: "the Game Master may grant limited access". — Missing: every ordering and gating predicate in the Hybrid cascade.
- `geography.md › Champion TS Values`: "On success: TS gains initial awareness (GM sets value, likely 10-15 Stirring range)". — Missing: the value.
- `baralta_crown_claim_v30 (1).md › §3 Override`: "If Himlensendt has experienced the originary Lock encounter before the Succession Contest fires: GM discretion." — Missing: the outcome function of Himlensendt's "personal faith state".
- `faction_politics_v30.md › §2.2b.ii`: "Witnessed by unintended non-asset NPC (GM discretion; typical trigger: ambient Standing 3+ NPC passing through operation zone)"; `› §1.4c`: "GM-determined +1 Ob on the Consecration ceremony roll for each year-arc the Church's CI has been below 30". — Missing: witness probability; the Consecration roll itself (pool, base Ob).
- `player_agency_v30 (3).md › §4.2 Witness Mode`: "one sentence, GM may incorporate or reject; videogame: pre-scripted dialogue branch tagged to player Conviction" — the videogame branch is stated but the tag-to-branch mapping is not.
- `stats_1_7_scale (1).md › PP-244`: "replacement designated (Influence DA Ob 2 or GM succession)"; `› PP-255`: "PI = 10: GM narrative uprising event." — Missing: the automatic succession rule; the uprising's mechanical effect.
- `governance_play_redesign_v1.md › §1.4`: "(the controlling faction's AI, or the GM, per the faction priority tree)"; `› §2.4`: "GM-/sim-authorable card set"; `› §5.3`: "GM-authorable vs sim-generated split."
- `player_agency_v30 (3).md › §7.1`: "the player may only *indicate* intent for GM use."

**U-02 · The settlement pressure homeostat has undefined terms.** `governance_play_redesign_v1.md › §2.1`: "Π_next = clamp( Π + Σ(unserved Needs) + Σ(active Grudges) + Σ(NPC ambitions in motion) + external_shock − Σ(player releases this season), 0, 10 )". Missing: the unit of a Need, a Grudge, an ambition "in motion"; the source and range of `external_shock`; what counts as a "release" (the card example gives "Π −2" per response, but the verbs table gives none). Also `› §1.4`: "**suspicion track +1**; at threshold → recall, audit, or replacement" — the threshold and the choice among the three outcomes are unstated. `› §1.1`: "Standing 5 governors (Seat/Cathedral) get +1" AP — Standing 6–7 governors unaddressed.

**U-03 · Piety Yield's "PT tier".** `ci_seizure.md › CI Generation`: "CI += Σ(PT tier × SW/5) per prominent territory, floored." `ci_political_v30.md › §1`: "T9 (SW 5, PT 5): yield = 1.0 × (5/5) = 1.0 … T8 (SW 3, PT 3): yield = 0.25 × (3/5) = 0.15". Missing: the tier value for PT 0, 1, 2, 4; whether "floored" floors the sum or each term (at the printed values every non-T9 term floors to 0, making the whole Piety Yield mechanic inert outside Himmelenger — which the corpus's own "(negligible)" note half-admits).

**U-04 · Seizure "infrastructure modifiers" and Prominence.** `ci_seizure.md › Seizure Ob`: "Ob = 10 − PT − infrastructure modifiers (floor 1). See victory_v30 §3.2 for infrastructure table." The table is not in the corpus (R-01); `campaign_architecture §1.1` gives per-settlement modifiers but `ci_seizure` treats seizure per territory, and no rule says how per-settlement modifiers combine into a territory Ob (sum? max?). "Prominence assessed at seizure declaration" — `phases.md 4b` says Prominence is "Updated every Accounting"; which snapshot applies to a mid-season declaration is unstated.

**U-05 · The Domain Action Resolver's difficulty table.** `stats_1_7_scale (1).md › Domain Action Resolution`: "difficulty = the contested target's relevant stat (contested actions), OR a fixed action-difficulty rating (non-contested actions). Legacy Ob mapping: an action previously "vs Ob O" has difficulty D = max(1, (O−1)·2)." Missing: for each Domain Action, which stat is "relevant" and which actions are "contested" (five examples given, ~30 actions in `core (1).md › Standard Action Ob Reference` and `stats › Unique Actions`). The mapping D = max(1,(O−1)·2) applied to `core`'s Govern "floor(Prosperity / 2) + 1" yields a Prosperity-dependent difficulty no document tabulates. `› Unique Actions`: "Hafenmark Sovereign Authority Doctrine — bare Mandate vs Ob 4 — is the same class but was not in the ratified four; pending decision."

**U-06 · Fragmentation Check, Secession and Consolidation.** `fractional_province_ownership_v30.md › §3`: "Roll 5d10 vs Ob 3. Roughly Success rate." (no probability). `› §2.6`: Secession makes a settlement "a de facto independent subnational holding" — no stat sheet, governor, or Accord rule for it. `› §2.3`: "If non-Seat settlements cluster north of Seat: "Northern [Province]"" — requires settlement coordinates, which exist in no corpus document (they are cited to `valoria_geography_v30.yaml`, R-05). `› §2.4`: "Default on non-response: Resist" — "non-response" has no timeout for an AI controller.

**U-07 · Succession Contest inputs.** `faction_succession_split_v30.md › §2.2`: "Blood claim (named canonical heir per `npc_character_analyses_v30`)" (R-13); "Tie in strength: faction's dominant stat decides which is "top1"" — "dominant stat" undefined; `› §2.3`: "~60% of assets … ~40%" then `› §2.4` gives exact 60/40/70/30 — the tilde values are not rules; `› §2.4`: "Loyalty = (Commander Disposition toward contender) + (unit Discipline)" — unit Discipline is defined only in the absent `military_layer_v30` (R-04); "Ties: unit disbands." `› §2.1`: "Multiple claimants of comparable Standing" — "comparable" undefined. `› §6`: "resolve in descending pre-loss Mandate order" for simultaneous successions is the only ordering rule and it reads a derived stat (X-10).

**U-08 · Treaty pool.** `treaty_expiration_v30.md › §2`: "**Pool** | Influence + Standing modifier" — "Standing" is a per-player faction rank (0–7) in `player_agency`, a faction-pair token in `parliament.md` ("+1 Standing", "Standing tokens") and a Renown-like value in `treaty_expiration §3` ("Standing −2 (public reputation damage)"). Missing: which Standing, and its modifier table.

**U-09 · Parliamentary Transfer vote mechanics and CB predicates.** `parliamentary_transfer_v30.md › §4`: "Voting blocs computed by faction Standing relative to proposer + holder … Split bloc (no clear majority): no modifier" — no bloc algorithm, no majority definition (`ci_political §3.4` says votes are "Mandate + ⌊CI/20⌋" tallies; this file says blocs). `› §3`: "Negotiated agreement CB (both factions hold reciprocal action history showing alignment)" — no predicate; "Crisis-stability CB: Peninsular Strain >= severe" — Strain bands are "Peace/Tension/Fracture/Crisis/Collapse" (`tracks.md`), none is "severe"; "war-readiness threshold met" — undefined; "Conviction Scar count threshold (≥3 per `conviction_track_v30` §1)" (R-09). `› §1.3`: "Cannot strip a faction's last territory" — "territory" here vs settlement/province after X-18/X-19.

**U-10 · Insurgency pipeline constants and stats.** `insurgency_pipeline_v30.md › §2`: "If Varfell adjacent AND Varfell I ≥ `EINHIR_I_GATE`" — `EINHIR_I_GATE` has no value anywhere. `› §4.2`: "Military | Variable | Determined by source territory state at formation" — no function. `› §6.2`: "Acceptance is a contested resolution (parent Mandate vs Insurgency Resolve …)" — "Resolve" is not a stat in any schema; "P(sponsor-loss/season) is the key tuning value … set so that aggregate defeat remains modal" — no value; "a faction backing it via an informal alliance" — no informal-alliance mechanic exists in the corpus. `› §3.3`: "Resist Seizure | Influence vs Church Influence | … RM adds +1 Ob to Church seizure roll. Passive — does not consume RM action." — a roll is named, then the effect is declared unconditional. `› §5.4`: "Their Convictions are set by emergence conditions … [PROVISIONAL: Conviction-derivation algorithm not specified]".

**U-11 · March layer data and edge rules.** `march_layer_v30.md › §1`: "Cost per traversed segment: `distance_px × terrain_cost_multiplier` per `valoria_geography_v30.yaml :: terrain_cost_matrix`" — the matrix, `distance_px`, `vision_range` factor tables, `bridges`, `gates`, `radiation_bands` all live in a YAML not in the corpus (R-05); without them §1–§3 cannot evaluate. `› §1.3`: "beyond a finite supply radius (default 8 settlements …) accumulate Attrition strain at +1 per season per 4 settlements over budget" — "over budget" of what; "Attrition strain converts to Size loss at season Accounting at 1:1 ratio" — Size undefined in corpus. `› §5.4`: "(b) IP −2 to the trespassing faction" — IP is a single global clock; a per-faction IP does not exist. `› §3.3`: "Counter-recon does not reveal scouting attempts to the defender automatically — only on contested-roll success" — the contested roll is not specified. `› §6`: "§6.1 Fleet composition / §6.2 Naval combat resolution / …" are empty headings, while `settlement_adjacency_v30.md › §1.1` has "Coastal | 1 (requires naval)" and `› §2.2` "Port | Defender gains +1D if naval reinforcements available" — both predicates depend on the empty section.

**U-12 · Settlement layer: starting values and undefined stats.** `settlement_layer_v30 (1).md › PART 9 ED-SETT-01`: "Settlement starting Prosperity/Defense/Order values need simulation. **DEFERRED** … Values stand PROVISIONAL." — no document in the corpus gives a starting Prosperity/Defense/Order for any of the 35–37 settlements, yet Accord (`§1.3`), Treasury (`§1.8`), Weight W (`§1.8`) and Mandate (X-10) all derive from them. `› §3.3`: "RM | … CV −1 potential per season" and "Only available in territories with PT ≤ 2" — CV is declared ≡ PT in `faction_politics §4.2`, but "potential" has no rule. `› §4.7`: "Settlement Wealth +0.5 … Settlement Accord −0.5" — settlements have neither a Wealth nor an Accord stat (they have Prosperity/Defense/Order; Accord is provincial). `› §4.9`: "Any settlement with Thread Proximity ≤ 2" — Proximity is a territory attribute (`geography.md`); "RS −0.5 per harvest per season" — fractional MS with no rounding rule. `› §3.2`: "Pacify | Charisma + local History | floor((3 − Order) + 1), min 1" — at Order 4–5 the formula goes negative before the floor, so Pacify at high Order is Ob 1 (probably intended, unstated). `› §4.3`: "Order decay −1 (Order is more stable)" — no baseline Order decay rate is defined anywhere. `› §7.1`: "Political Stability | 0 start, +1 per violence event | Unchanged | Cumulative. Self-regulating via victory gate (≤ 6)." — a clock named nowhere else, with an undefined "violence event" and an undefined "victory gate".

**U-13 · Player-agency generation predicates.** `player_agency_v30 (3).md › §3.2`: "assigns one Duty to the player character based on the highest-priority unaddressed need that matches the player's capabilities" — no capability-match function. `› §3.4`: "**Exceeding:** Completing the Duty AND producing additional value (discovered a conspiracy, turned an enemy NPC, generated Casus Belli)" — an open list, not a predicate. `› §4.2 Step 5`: "NPC's priority tree fired an action this season that could benefit from player involvement" — no predicate. `› §9`: "Trade action (Cognition + History, Ob varies by settlement Trade stat, in Port/City)" — settlements have no Trade stat. `› §2.3`: "Sufficient Scope" and "Domain Echo" are used throughout but defined only in `scale_transitions_v30` (R-11).

**U-14 · Faction behaviour architecture — unspecified functions.** `faction_behavior_v30.md › §3.4`: "`attributed_mission_outcome(faction)` ∈ `[-1, +1]`: aggregated `da_outcome.*` Key stream" — aggregation unspecified; "`γ × (random shock; events)`" — distribution unspecified; `› §3.7`: "`cascade_alignment_modifier(da, faction.aggregate_effective_convictions)` # -1, 0, +1" — no mapping from a DA to a 13-vector alignment; "`sign(da.cascade_alignment_with_role) × strictness(faction) × {1, 2}` # +1 if action is ±1 from role expectation, +2 if ±2 deviation" — the distance metric is undefined; `› §5.1`: "L crosses threshold (e.g., L < 2 = "collapse zone") | `state.coup_attempted` (probabilistically)" — no probability; `› §3.4.1`: "Faction effective temperament = population-weighted average" — no population data (`territory_temperaments §3`: "Population weighting deferred (uniform-weighted approximation here…)"); `› §3.4.2`: `territory.temperament_drift` accumulates but no rule converts drift into new α/β.

**U-15 · Clock-effect tables with holes.** `parliament.md › Parliament Integrity (PI) Scale`: range "0–20" but bands only for "8–10", "5–7", "3–4", "≤ 2"; `core (1).md`: "Auto-resolves at PI ≥ 20 (Crown elimination)". Missing: 11–19. `core (1).md › Starting Values` has a row with no name: "| | 2 | 0–5 | Near IP clock. |". `clocks.md › Altonian Vanguard`: "[EDITORIAL: authorial review required — Vanguard faction identity, advance route, and elimination conditions]". `clocks.md › Cascade Depth Cap`: "Maximum 3 immediate mechanical effects per card play resolution step. Additional effects queue to next Accounting." — which three apply first is unstated; `strategic_layer_v30.md › Cascade Test 2`: "Confirm that clock changes count against the 3-effect cap."

**U-16 · Southernmost.** `southernmost.md › Southernmost Awareness`: "Scale: 0–7 (or 0–10 for research-intensive factions). Starting values: see params_factions_ttrpg.md." — which factions; starting values absent (R-15). `› [NAME-PENDING: ED-048] Ritual`: the central ritual has no name and requires "ED-048 Text in possession" — an object defined nowhere. `› Zone Hazard Table`: "Inner (Oscillating) | Monstrous entity | Combat | varies". `› Ritual Failure`: "Mode 3 entity at primary site" — undefined. `› Crisis Timeline`: "TT 50 sustained 3 seasons without stabilising Weave" — TT's relation to MS (X-32).

**U-17 · Phases and events.** `phases.md › Game Setup`: "Sub-roll for target (Lenneth/Torben/Almud)" — no distribution; `conflict_architecture_proposal.md › Royal Assassination`: "(exact season randomized within S8–S12 window)" — no distribution. `phases.md › Phase 5`: "8. Check threshold events: draw one Event Card per threshold crossed." — the event deck is undefined; "8b. Milestone Bonus check.", "9. Warden Emergence check.", "10. Warden Cooperation check." — none defined in the corpus.

**U-18 · Mechanics referenced everywhere, defined nowhere in the corpus.** Each is load-bearing: **Emergency Powers** (`parliament.md` "Crown Emergency Powers (−1)", `ministry.md`, `institutions.md`); **Parliamentary Manoeuvre** (Ob given in `core`, procedure absent); **Heresy Investigation** (`institutions`, `stats`, `worldbuilding` — no roll, no outcome table); **Church Attention Pool thresholds** ("resolve threshold responses", `phases.md`; `tracks.md` gives Inquisitor thresholds only); **Casus Belli** standard duration/use ("Casus Belli (standard, 3 seasons)" in `parliament.md`, consumed "per parliamentary_transfer §3", generated per "faction_layer §3.5" — R-03); **Standing tokens**, **Deed tokens**, **Diplomatic Token** (`core (1).md › Dynastic Proclamation`, `faction_succession_split §2.2`); **Hollow Victory** (dissolved and live, X-56); **Popular Will / PW** (`conflict_architecture_proposal.md`: "RM PW advances"; `early_game` T7); **Warden's Accord (WA)** (`insurgency §3.1` "WA ≤ −2"; defined in `conviction_track_v30 §5.1`, R-09); **Thread Debt tokens** (`phases.md 6`); **Guild Favour** (`stats › Economic Leverage` "Guild Favour ≥ 5 … (1–7 territory track)"; `institutions` "Church has Favour ≥ 3" — a Church Favour track exists nowhere); **Scene Slate "Priority" numbering** is defined in `player_agency` but `settlement_layer §4.3` feeds "Priority 4 (Territorial)" and `§4.5` "Priority 5" — consistent, fine; **Momentum / Stunt** (`player_agency §2.3`); **Coherence** range (`generational_transition` "reset to 10", never bounded); **lifepaths** ("per new character's lifepath origin").

**U-19 · Ministry priority tree.** `ministry.md › Priority 5 (default)`: "Consul Inward in highest-Prosperity uncontested territory with AP-token" — "uncontested" undefined; `› Corrupt Ministry Failure`: "Riskbreaker Priority 6 now includes the corrupting faction's territory" — Riskbreaker priority tree absent; `› Ministry Collapse`: "all Hafenmark Deed 3 (Parliamentary Consolidation) checks suspended" — Deed 3 undefined.

**U-20 · Tracks.** `tracks.md › RDT`: "Advances: Reformed Settlement event = +1 (max once per arc). Requires: …" — what fires a "Reformed Settlement event" is never stated (the `strategic_layer › Cascade Test 2` narrative has Church choose "Resist, Accommodate, or Ignore" with no rule). `› Accord`: "Non-military acquisition → Accord 2+" — 2 or 3. `› TD 2`: "schism risk" — risk of what, at what probability.

**U-21 · Campaign architecture.** `campaign_architecture_v30.md › §1.1 Axis 4`: "Removal: Mass Battle, Mandate Challenge (Ob 6+), or RM community action OW." — pool for "Mandate Challenge" unstated. `› §3.2a`: "Each consecutive threadwork operation in the same scene reduces the pool by a Fibonacci amount. Op 1 = full pool, op 2 = −1D, op 3 = −2D, op 4 = −4D, op 5 = −7D, op 6 = −12D." — the increments are 1,1,2,3,5; op 7 (−20D?) is unstated. `› §4.3`: "renowned character performs threadwork publicly" — Renown threshold unstated. `› §5.1`: "One border territory under Active Invasion" — which; "Underground Network activates" — undefined; `› §6.2 Path E`: "Declare Mending Sanctuaries. Enforce with Thread capability." — no mechanic; `› §6.3`: "Governance stat = average Spirit of active Menders." — which stat this replaces.

**U-22 · Conflict architecture.** `conflict_architecture_proposal.md › Church Expansion`: "Accord in the settlement adjusts by PT alignment (high PT territory: population accepts; low PT: population resists)" — no numbers, and settlements have Order not Accord. `› Royal Assassination`: "Retrieval requires military deployment to T4 (Varfell territory) to establish an extraction route." — Elske is in Altonia (`campaign_architecture §5.3`); no route rule. `› Starting Friction Points`: "Every Accounting, Crown runs a fragmentation check (Influence 5 vs Ob 3)" — consistent with `fractional §2.6` only if T1 has exactly one non-Seat-held settlement, which under the new registry (`settlement_layer §2.1`: Valorsplatz province = Valorsplatz, Auerheim, Königsbrück; the Cathedral is now a district) it does not.

**U-23 · Baralta claim.** `baralta_crown_claim_v30 (1).md › §7.3`: "+1 Ob to Consecration ceremony roll if Torben Disposition to Baralta ≤ 0" — `§3` resolves Consecration by a Stability threshold, not a roll. `› §5`: presents "Option A" and "Option B" as open, while `› §6` records "ED-411 | … Option B … Decision made, flagged for review". `› §2`: "Church | … | CI ≥ 40 (theocratic threshold — Church only claims if already dominant)" — the contest pool "Mandate + Influence" is a derived-stat read (X-10).

**U-24 · Faction politics.** `faction_politics_v30.md › §1.1c`: "roll on the Legacy table when the Banner is introduced" — table absent (ED-653). `› §3.6.2 Failure`: "PC's Piety Track resets to neutral (5/5/5)" — PT is a 0–5 territory stat; a PC has none. `› §3.6.2 Partial`: "Any Standing earned through transgressive Conviction work converts to half value" — no ledger of "earned through". `› §6.1`: "Mandate ≈ PI/2" for the successor Hafenmark — not a rule. `› §7.2`: "Competence (0–3) and Corruption (0–3) tracks identical to Crown Ministries (MIN-02, MIN-03)" — MIN-02/03 absent (R-20). `› §1.3 Standing 7`: "majority support of the senior Jarls (3 of 5 at Disposition ≥ +1)" — `› §1.3c` names four Senior Jarls plus a conditional Edeyja; the five are not fixed. `› §2.2 Candidate`: "Conviction-check vs Valoria alignment (roll: Intel vs Ob 2, Overwhelming required)" — under X-02 "Overwhelming" at Ob 2 needs net ≥ 4 (PP-179) or ≥ 3 (Ob+1).

**U-25 · Worldbuilding cards without complete triggers/effects.** `worldbuilding_v30 (1).md › Card: Prudence Crisis`: effect "Church Mandate −1 in each territory where Prosperity ≤ 3" but no trigger in §3.3; the §10 table gives trigger "Church Wealth ≤ 2". `› Card: Guild Schism`: §5.3 gives trigger and counter-play only; §10 adds "Wealth −1, Influence −1 for 1 season. One territory Guild Favour → 0." `› Card: Ministry Collapse` §10: "One Ministry ceases function for 1 season" — which one. `› §6.2 Motion of No Confidence`: "Succession: Torben if available and loyal" — loyalty threshold unstated; "Parliamentary Vote | Influence vs Crown Mandate (existing §8.11)" (R-15).

**U-26 · Institutions.** `institutions.md › Prudence (Tithes)`: "+0.5 Wealth/season from tithed territories (rounds down at Year-End). Territories where Church has Favour ≥ 3 contribute" — per territory or total; Church Favour undefined. `› Church Levies`: "Two-thirds can be raised by the King" (prose) vs "Crown gains Military +1 … Church Military −1" (rule) — fine as a rule, but "Church cannot refuse if Crown L ≥ 4" implies a refusal roll below L 4 that is not given.

**U-27 · Strategic layer residue.** `strategic_layer_v30.md › §9.2`: "Own faction: exact values visible. Intel stat: always hidden from all players regardless of ownership." — a faction cannot see its own Intel; `› §9.7`: "Resource expenditure threshold: 2× rolled net successes" — resources of what unit; `› G-11`: the IP advancement table is truncated mid-row ("Torben complied (sent to Altonia) | −3/season while"); `› P-21` is truncated ("−1 with"); `› I-03`, `› I-09`, `› G-05` have headings and no body.

**U-28 · Political hierarchy.** `valoria_political_hierarchy_v30.md › §2.4`: "Specific scalar values are TBD pending balance pass; the structure is canonical here, the numbers are not." `› §5`: "specific event triggers and reunification thresholds not yet specified." Both are the mechanism `fractional_province_ownership` already defines differently (fractional names "Greater/Lesser/Northern…", hierarchy names "northern/southern or western/eastern" and "merge back … when all sub-provinces … return to common faction-alignment" with no Consolidation action). Decision: which fracturing model.

**U-29 · Southernmost expedition vs settlement gates.** `geography.md › Expedition Procedure`: staged from T6 with a Champion "TS ≥ 30"; `march_layer_v30.md › §7.3`: "Gate edges are also the only land-route into T15 … Holding a gate confers +1 IP per season (strategic chokepoint value)." — "holding" a gate (a sub-feature with no siege target, `settlement_layer §2.2`) has no control rule; and +1 IP for holding a southern gate against a northern invader is unexplained.

**U-30 · Generational transition.** `generational_transition_v30.md`: "Coherence: reset to 10" (range never stated); "Thread Sensitivity: per new character's lifepath origin" (no lifepaths in corpus); "Companion returns to NPC pool at current Disposition toward faction" (companion Disposition-toward-faction is not a tracked value in `player_agency`).

---

## 3. Dangling references

Every citation to a document, section, path or identifier that is not in the 33-file corpus, grouped by target. **LB** = load-bearing (a rule in the corpus cannot be evaluated without the target). **PROV** = provenance/history only. Where a corpus file is plausibly the cited document under another name, that is said explicitly and the citation is *not* counted as dangling.

**Near-matches (not dangling, but the name differs).** `params/core.md` (cited by `parliamentary_transfer §4`) ≈ `core (1).md`; `tc_political_redesign_v30` (cited by `ci_seizure`, `geography`, `faction_politics`) ≈ `ci_political_v30.md` (whose own header names its infill `tc_political_redesign_v30_infill.md`); `faction_politics_expanded_v1.md` (cited by `player_agency`, `baralta_crown_claim`, `settlement_layer`) ≈ `faction_politics_v30.md` ("Faction Politics Patch Register (EXPANDED)"); `board_game_v30` ≈ `strategic_layer_v30.md` (its header: "renamed from designs/board_game/valoria_bg_v05_simulation_and_patches.md"); `params/bg/core.md`, `params/bg/tracks.md` ≈ `core (1).md`, `tracks.md`; `params_southernmost.md` ≈ `southernmost.md`; `geography_v30.md` is cited by `geography.md` as its own source ("Canonical geography applied … per geography_v30.md") — the corpus file is a derived table, the cited narrative is absent (so the *narrative* is dangling, R-05, while the table is here).

**R-01 · `victory_v30.md` (§0.4, §1, §3, §3.1, §3.2, §3.4, §3.5 Phase 2, §5, §7).** LB. Cited by `ci_seizure.md` ("See victory_v30 §3.2 for infrastructure table", "Per victory_v30.md §7"), `phases.md` (step 12 "See designs/board_game/victory_v30.md §3 for all faction conditions"), `core (1).md`, `ci_political_v30.md`, `geography.md` ("TCV from victory_v30.md §1"), `campaign_architecture_v30.md`, `faction_succession_split_v30.md` ("victory §3.5 Phase 2"), `fractional_province_ownership_v30.md`, `faction_behavior_v30.md`. The seizure infrastructure table, the TCV table and the per-faction victory conditions live only there (X-01, X-05).

**R-02 · `peninsular_strain_v30.md` / `peninsular_strain_v1.md` (§1, §2, §2.1, §2.2, §2.3–2.4, §2.5, §3, §3.2, §4, §4.1, §4.2, §5.3, §6.2, §6.4).** LB. Cited by `clocks.md`, `tracks.md`, `phases.md` ("per peninsular_strain §4.2, ED-797"), `core (1).md`, `geography.md`, `ci_political_v30.md` ("IP now advances from Accord-based territory-count thresholds at Accounting (peninsular_strain_v30 §3.2)"), `strategic_layer_v30.md`, `campaign_architecture_v30.md`, `fractional_province_ownership_v30.md`, `faction_succession_split_v30.md` ("peninsular_strain §2.5 RM exception"), `insurgency_pipeline_v30.md`, `settlement_layer_v30 (1).md`. After ED-743 the only stated IP advancement rule is in this absent document (X-08).

**R-03 · `faction_layer_v30.md` (§1.3, §1.4, §1.5, §2, §2.7, §3, §3.3, §3.5, §5, §5.3, §5.5, "Triggers 1–5", "War Doctrine").** LB. Cited by `ci_political_v30.md` ("Parliament votes by Mandate (§5.3 faction_layer_v30)", "Stability: Governed exclusively by Triggers 1–5"), `stats_1_7_scale (1).md` ("AUTHORITATIVE per faction_layer §2.7"), `fractional_province_ownership_v30.md`, `settlement_adjacency_v30.md`, `march_layer_v30.md` ("Casus Belli check per faction_layer_v30 §3 War Doctrine"), `faction_succession_split_v30.md` ("Collapse Exit Procedure", "treaty … requires both at Mandate ≥ 3"), `insurgency_pipeline_v30.md`, `settlement_layer_v30 (1).md`. The Parliament vote tally, Stability triggers, occupation and collapse procedures are all there.

**R-04 · `military_layer_v30` (§1.7, §3, §3.2–§3.8) and `mass_battle_v30` (§A, §A.4, §A.5, §A.9, §A.11, §B.3, §D.1, §E.1, Part B, Part E).** LB. Cited by `ci_seizure.md` (the whole seasonal CI procedure is "per military_layer_v30 §3"), `ci_political_v30.md`, `settlement_adjacency_v30.md`, `march_layer_v30.md`, `settlement_layer_v30 (1).md` ("garrison's stats (from military_layer_v30)"), `faction_politics_v30.md` ("−2 margin+, per mass_battle_v30 §B.3"), `player_agency_v30 (3).md`, `parliamentary_transfer_v30.md`, `insurgency_pipeline_v30.md`. Unit Discipline, Size, Manoeuvre Phase and battle resolution are defined only there (X-40).

**R-05 · `designs/territory/valoria_geography_v30.yaml` (`:: adjacency`, `:: settlement_adjacency`, `:: terrain_cost_matrix`, `:: vision_range`, `:: radiation_bands`, `:: gates`, `:: bridges`, `:: starting_pros`, `.settlements`, `scale_anchors :: strategic_to_tactical_zoom`) and `designs/world/geography_v30.md` + infill, `setting_geography_v30`, `designs/world/settlement_adjacency_map.yaml` (superseded), `designs/audit/2026-04-30-geography-audit/` (00, 01 PP-707, 04 PP-709).** LB for the march layer and settlement adjacency (every edge, cost and coordinate); PROV for the audit. Cited by `march_layer_v30.md`, `settlement_adjacency_v30.md`, `territory_temperaments_v30.md`, `valoria_political_hierarchy_v30.md`, `settlement_layer_v30 (1).md`.

**R-06 · `calamity_radiation_v30.md` (`designs/setting/…`, `designs/world/…`; "Simplified BG Lookup Table", "Node Distance Map + Radiation Matrix", "§Forgetting", "band table").** LB for `march_layer §2.4/§7`, `player_agency §4.2 Step 2b` ("per calamity_radiation_v30"); `clocks.md` reproduces the MS×Proximity table so that part is executable.

**R-07 · `threadwork_v30` (§2.3, §2.6, §5.2, §5.6), `params_threadwork` (§Coherence), `params/threadwork.md` PP-616, `ms_budget.md` (§2.2).** LB: PP-616's pool "(Spirit × 2) + History + TPS" is the declared canonical Community Organizing pool (X-28) and lives only there; `settlement_layer §4.9` gates discovery on "RS visibility thresholds (threadwork_v30 §5.6)". Cited by `stats_1_7_scale (1).md`, `campaign_architecture_v30.md`, `worldbuilding_v30 (1).md`, `march_layer_v30.md`, `strategic_layer_v30.md`, `tracks.md` ("per threadwork_v30").

**R-08 · `social_contest_v30.md` (§6.4, §7, §7.1, §10, §10.1 ED-631).** LB: the Parliamentary Vote contest engine and Parliamentary Stay that `parliamentary_transfer_v30 §4` "is **wrapped in**"; Excommunication Tribunal (`insurgency §4.3`); "asymmetric … petitioner" contest (`settlement_layer §3.3`, `governance_play §1.3`).

**R-09 · `conviction_track_v30.md` (line 16, §1, §1.1, §2.1, §4.2, §5, §5.1–§5.4; future `piety_track_v30.md`).** LB: Latent RM stage (`insurgency §3` is "Per conviction_track §5"), Warden's Accord (WA), Cultural Reclamation ("Influence vs Ob 2, target-territory Piety -1", `core (1).md` header), Conviction Scar threshold, "Seizure Ob … max(0, 3 − PT)" (X-05). Cited by `core (1).md`, `insurgency_pipeline_v30.md`, `parliamentary_transfer_v30.md`, `faction_politics_v30.md`.

**R-10 · `npc_behavior_v30` (§1.2, §1.3, §3, §3.2, §3.3, §3.4 "line 447", §5.0b, §5.2, §7, §7.8, §8.2), `npc_roster_v30` (§11, §13, §14 and "#1, #2, #4, #7, #8, #9"), `npc_character_analyses_v30` (§2), `npc_relational_graph` (§6), `character_canon Part B`, `migration_roster`, `params_npc.md` ("when created"), `edeyja_npc.md`.** LB: every NPC priority tree (Church, Ministry "AI tree", Riskbreaker "Priority 6", Löwenritter), Conviction Scar accumulation, Knot rupture strain, the canonical heir list. Cited by `generational_transition_v30.md`, `baralta_crown_claim_v30 (1).md`, `campaign_architecture_v30.md`, `player_agency_v30 (3).md`, `settlement_layer_v30 (1).md`, `governance_play_redesign_v1.md`, `faction_succession_split_v30.md`, `faction_politics_v30.md`, `valoria_political_hierarchy_v30.md`, `geography.md`.

**R-11 · `scale_transitions_v30` (§3, §4.3.2, §5, §7 "bullet 5"), `hybrid_gaps_v30.md`, `videogame_mode_spec`.** LB: Domain Echo ("Success +1, Overwhelming +2, cap ±2"), "Sufficient Scope", mandatory Zoom-In trigger list. Cited by `stats_1_7_scale (1).md`, `faction_behavior_v30.md`, `player_agency_v30 (3).md`, `ci_political_v30.md`, `faction_politics_v30.md`, `strategic_layer_v30.md`, `campaign_architecture_v30.md`.

**R-12 · `factions_ttrpg_v30` (§8.2–§8.9, §8.11), `stage6_factions.md` (§8.4–§8.9), `stage6 §8.8`, `stage13` (§13.6), `params_factions_ttrpg.md`, `params/factions.md`, `params/factions_personal.md`, `factions_personal_v30` (§8.1), `faction_state_authoring` (§6, §8), `faction_canon_v30` (§3.4, §5), `params/factions/stats_1_7_scale.md` (≈ corpus `stats_1_7_scale (1).md`).** LB: "§8.11 Parliamentary Vote" (`worldbuilding §6.2`, `faction_politics`), the unextracted unique actions ("Hafenmark, Varfell, Guilds, Löwenritter unique actions not extracted", `stats › Unique Actions`), Southernmost Awareness starting values, Deniability Debt "tracked per stage13", Patience Protocol, Coup Counter "§8.9". Cited by `southernmost.md`, `stats_1_7_scale (1).md`, `treaty_expiration_v30.md`, `faction_behavior_v30.md`, `faction_politics_v30.md`, `baralta_crown_claim_v30 (1).md`, `worldbuilding_v30 (1).md`.

**R-13 · `fieldwork_v30` (§3.3, §4.1), `fieldwork_design_v1.md` (§8.1), `fieldwork_lifecycle_stress_01 F-L06`.** LB: Evidence Track thresholds (Duty "Investigate" success, Renown, Niflhel/Knot discovery "Evidence Track threshold 3/5"), Depth Axis, Survey POI rules (`core (1).md › Survey`). Cited by `player_agency_v30 (3).md`, `settlement_layer_v30 (1).md`, `core (1).md`, `march_layer_v30.md`.

**R-14 · `derived_stats_v1` (§3, §4, §8.1, §8.3), `derived_stats_v30`.** LB: Treasury (`settlement_layer §1.3/§1.8`, "Treasury −300", "+50/season"), Legitimacy meter "= Mandate × 20", Renown governance penalties (`player_agency §5.4`).

**R-15 · `params_board_game.md`, `params/bg/npcs_special` (§Patience Protocol), `params/bg/tensions_deck.md`, `params/bg/royal_assassination.md`, `board_game_v30_infill.md`, `canonical_timeline.md` / `canon/03_canonical_timeline.md` (L16, D-2).** LB for the Tensions Deck cards and assassination sub-roll (`phases.md › Game Setup` cites both); PROV otherwise. `stats_1_7_scale (1).md › PP-577`: "per params_board_game canonical".

**R-16 · `canon/02_canon_constraints.md` §B GD-1, GD-2, GD-3.** LB: GD-1 is the victory rule (X-01), GD-3 is the insurgency pipeline's authority ("(a)–(e)" clauses quoted but the clause text is absent), GD-2 "mandatory threat response" (`insurgency §7.2`) is not defined in the corpus. Cited by `treaty_expiration_v30.md`, `parliamentary_transfer_v30.md`, `insurgency_pipeline_v30.md`, `ci_political_v30.md`, `core (1).md`.

**R-17 · `designs/audit/2026-05-14-balance-audit/faction_balance_convergence_v12c_2026-05-14.md` (§4.2, §4.4, §4.4.1, §4.5, §5, §6.5, §7, §8.3), `part10_crown_initiative_design_2026-05-14.md` (§3.4 Mode III), `part13_integrated_balance_solution_2026-05-14.md` (RC-v1), `handoff_2026-05-15_v15.md` (HR-10), `restoration_movement_v30.md` (Pass 2d pending), `einhir_revival_v30.md` (Pass 2d pending), `varfell_path_b_v30`, `2026-04-24 audit`, `2026-04-25 stress-test 33/46`, `gap_resolution_2026-04-19.md`, `improvement_avenues_2026-05-10`, `historical_precedents_analysis.md` (§1, §1.4, §3, §3.4, §4.3), `references/historical/precedents_analysis.md`, `precedents_warfare.md`, `ners_historical_precedent_matrix.md` (entries 2, 4), `insurgency_dissolution_proposal.md`, `domain_action_resolver_spec.md`, `2026-05-01-stage-10-validation/05_ED-755_resolutions.md`, `2026-04-30-architecture-session/03_PP-686_proposal.md`, `05_PP-686_simulation_evaluation.md`, `06_PP-686_sim_v2_evaluation.md`, "artifact 04 P3-4", "artifact 06 §1.3", "audit Problem 03", "audit Q2/Q5", "audit G1", "Finding A-07/A-09/A-10/A-11", "PR-14 Finding 7".** PROV (validation and rationale), except that the Senator Outward re-binding action (`treaty_expiration §2`: "Per part10 … consult part10 directly if Pass 2h amendments change this") and the v12c "world-level RM PT decay" parameters are stated to be *derived from* these and the corpus copies may be stale.

**R-18 · Sim and test paths: `sim/provincial/treaty.py`, `sim/provincial/parliamentary_transfer.py`, `sim/provincial/crown_initiative.py`, `sim/provincial/faction_action.py`, `sim/peninsular/accounting.py`, `sim/personal/parliamentary_vote.py`, `sim/personal/parliamentary_stay.py`, `sim/world/insurgency_pipeline.py`, `sim/world/restoration_movement.py`, `sim/autoload/victory.py`, `sim_insurgency_dissolution.py`, `settlement.py`, `game_state.World`, `tests/sim/v17-integration/m6_faction_actions.py`, `tests/coverage_matrix.md`, `engine_v4 Phase 1–5`, commits `65b918a2`, `297f892`, `13b8f30`, `bb5e293`, `3cb5207`, `fe367105`, `c2effdd`, `801b97c5`.** PROV.

**R-19 · Registries: `references/canonical_sources.yaml`, `references/params_southernmost_history.md` ("to be created"), `references/glossary.md`, `references/alias_registry.yaml`, `canon/mechanics_index.yaml` (`treaty_expiration`, `parliamentary_transfer`, `insurgency_pipeline`), `canon/supersession_register.yaml`, `canon/editorial_ledger.yaml`, `canon/patch_register_active.yaml`, `propagation_map`, `file_index`, `settlement_layer_v30 §2.2 migration table` (present), `_lps_structural_redesign_2026-05-30` ledger, `clock_registry_v30` (§3), `clocks_v30`, `companion_specification_v30`, `settlement_bridge_unification` (C-01, C-04), `throughline_resolutions_v1` (§1.3 viability matrix, §2), `throughline_specifications` (§T3.3), `throughlines_meta` (§8.2), `key_substrate_v30.md`, `key_type_registry_v30.md` (§3), `conviction_taxonomy_v30.md` / PP-684 (§2, §3.1, §4, §5), `conviction_axis_matrix_v30.md`, PP-687 (§4, §4.1, §7.1), `knots_v30.md` (§5), `solmund_cultural_guide_consolidated.md` (§12, §22.1), `worldbuilding_v30_infill.md`, `worldbuilding_integration_v2.md`, `baralta_crown_claim_v30_infill.md`, `tc_political_redesign_v30_infill.md`, `UI v4 §7.4`, PP-688 "Tier 1", `rank_ladder_v1.md`, `caste_integration_v1.md`, `ministry_system_v1/v2.md`.** Mostly PROV. LB exceptions: the viability matrix (`player_agency §7.1` displays it at character creation), the 13-Conviction taxonomy and Self-Other axis (`faction_behavior §3.4` reads PP-684 §3.1), the Key type registry (`faction_behavior §3.1` reads PP-687 `da_outcome` subtypes), Knot strain (`march_layer §3.4`), companion governor rule C-04.

**R-20 · Register identifiers with no text in corpus: OFC-01–OFC-04, SUC-01–SUC-03, LIN-01/LIN-02, MIN-01–MIN-06, FAC-01–FAC-03, REN-02/REN-03, NPC-02/NPC-03, POW-03, COUP-02, ED-POL-01–14, BALANCE-POL-01/02, FRAC-01/FRAC-03, FSS-1/FSS-F2, LPS-1/LPS-2e, CC-4, ER-1, NERS-N/E, M-1–M-11 / T-08–T-25 / Μ-α..δ (vetting), G-075–G-095, A-01–A-11, B2/B3/B4/B5/B6/B7/B8/B11/B14 (v04 sections), P-07–P-32 (bg patches), v04/v05, "stage7", "Stage 10", "Pass 2d/2h/2i/2k/2l", "Session A/B/C", ED-048 "[NAME-PENDING]", "Q2/Q5", "Tier 0", "Class A/B", "S1–S20" (seasons, fine).** LB where a rule points at them for its mechanics: SUC-01–03 (`player_agency §5.2`, `faction_politics §1.3`), LIN-01 (Bloodline claim "+2D"), POW-03 (Legitimacy Token damage), MIN-02/03 (Competence/Corruption), OFC-03/04 (Inquisitor/Templar authority), FAC-02 (Recognition withheld conditions), REN-03 (Public Deed Renown), P-07 (Patience Protocol cap), PP-182 (Thread co-movement protocol, cited by `phases.md` and `core (1).md`), PP-491, PP-430 ("Focused" Cardinal), PP-487 (Hafenmark PI-gated succession), PP-460 (RM statless rule), PP-616, PP-663, PP-686/PP-687/PP-684.

**R-21 · Patch/editorial IDs.** Roughly 190 distinct `PP-NNN` and 150 distinct `ED-…` identifiers are cited; none resolves to text in the corpus. PROV in general. Three are load-bearing by construction: `PP-TBD` (used as the authority for the three-scale model in `phases.md`, the bishop appointment in `ci_seizure.md`, secession candidates in `fractional §2.6`, and the whole `player_agency` proposal — "PP-TBD" cannot be resolved), `PP-[NEXT]` (`southernmost.md › Combined TT Reduction Cap`), and `ED-NEW-01…10` (`worldbuilding_v30 (1).md`, unnumbered placeholders). The ID collisions are at X-65.

**R-22 · Philosophical foundations P-01…P-15 (P-01, P-03, P-08, P-12, P-13, P-15) and "A10/A12/C5" (`generational_transition › Canon Compliance`).** PROV.

**R-23 · Deprecated directory paths.** `designs/mechanics/baralta_crown_claim_mechanic.md`, `designs/worldbuilding/worldbuilding_integration_v3.md`, `designs/board_game/valoria_bg_v05_simulation_and_patches.md`, `designs/setting/southernmost_v30.md`, `/mnt/user-data/outputs/` (`faction_politics` final line). PROV — rename trails.

**Dangling *inside* the corpus (a document citing its own missing section).** `parliament.md`: "§PI Thresholds above", "[Full Policy table in faction card section]", "§Casus Belli" (cited by `ci_seizure.md` "(See §Casus Belli.)"), "§Victory Conditions above … TCV table" (`ci_seizure.md`); `settlement_layer_v30 (1).md`: "§1.4 … per faction_politics_expanded_v1 §1 Hall Tier" (near-match), "§2.1 … starting values shown in B2" (`strategic_layer P-22`), "§9 PENDING" (`settlement_layer §1.8` refers to a §9 Population item; PART 9 is Open Items and has no such row); `strategic_layer_v30.md`: "See Section Two, P-13", "PATCH P-28: See below" (nothing follows), "PATCH P-16 … See below" (present), "§9.9/§9.10/§9.11" (present); `march_layer_v30.md § 6` empty subsections; `worldbuilding_v30 (1).md` §3.4, §4.4, §7.2, §7.3 are headings with no body ("## 3.4 Church Taxation (Simple Rule — All Modes)" followed by nothing).

---

## 4. Numbers

Every numeric constant, threshold, band edge, cap, floor, coefficient, cost and probability, verbatim, per document. Columns: id · value (verbatim) · `file › heading` · what it governs · cross-reference where the same quantity carries another value elsewhere. Values are not normalised (½ stays "½", "0.5" stays "0.5", "≥ 2×Ob" stays as written).

### 4.1 `core (1).md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-001 | "control 11+ of 15 territories" | header comment (line 10) | victory | X-01 |
| N-002 | "Influence vs Ob 2, target-territory Piety -1" | header comment | Cultural Reclamation | R-09 |
| N-003 | "2–5 players", "5 players only" | FACTION ASSIGNMENT | board-game residue | U-18 |
| N-004 | "d10 pool. TN 7 (standard)"; "1 … −1 success"; "7–9 … +1"; "10 … +2 successes" | Dice System | dice | X-03 |
| N-005 | "Ob minimum: 1" | Dice System | Ob floor | — |
| N-006 | "≥ 2× Ob AND ≥ 3 → Overwhelming"; "≥ Ob → Success"; "0 < net < Ob → Partial"; "≤ 0 → Failure"; "Ob 10 exception: … Partial requires net ≥ 5" | Degree Table | degrees | X-02 |
| N-007 | MS "72", "0–100" | Starting Values | MS start | stats: TTRPG 60 |
| N-008 | CI "**28**", "0–100 (no freeze)", "CI 60 = Mass Seizure available", "CI 100 = cap" | Starting Values | CI | X-06, X-07 |
| N-009 | IP "20", "0–100", "IP 75 = Altonian Vanguard appears", "IP 80+", "IP ≥ 100 = Altonia regularly invades" | Starting Values | IP | X-31 |
| N-010 | PI "**7**", "0–20", "Auto-resolves at PI ≥ 20 (Crown elimination)" | Starting Values | PI | U-15 |
| N-011 | unnamed row "2", "0–5", "Near IP clock" | Starting Values | ? | U-15 |
| N-012 | Torben Loyalty "**7**", "0–7"; contest "Ob = current Torben Loyalty ÷ 2"; "PP-498 start 3 superseded" | Starting Values | Torben | early_game T1 "starts at 3" (superseded) |
| N-013 | Elske Loyalty "4", "0–7" | Starting Values | Elske | — |
| N-014 | Restless "Crown Stability ≤ 3, OR no military action 4+ seasons"; Autonomous "Crown Stability ≤ 2 … 4+ seasons Restless"; "PI −1"; Split "4+ seasons Autonomous", "(L3/PS3/Inf2/W3/Mil5/Stab5)", "PI −3", "Crown Military drops to 2", "PV drops by 3"; "Crown Military = 2" post-Coup | Löwenritter Graduated Autonomy | autonomy | X-12, X-14, X-54 |
| N-015 | WC "0", "0–3"; WR "0", "0–3", "WR ≥ 2 required to advance" | Starting Values | Warden tracks | X-50 |
| N-016 | Turmoil "0", "0–10"; "+1/season", "+2", "+1"; "−1/peaceful season" | Starting Values | Turmoil | X-08, X-09 |
| N-017 | Accord 0–3; "Defender +1D"; "Govern Ob +1"; "Military vs Ob 2"; capitals "3", home "2" | Accord | Accord | X-40 |
| N-018 | PV: T1 5, T2 2, T3 3, T4 2, T5 2, T6 1, T7 1, T8 4, T9 5, T10 3, T11 1, T12 4, T13 1, T14 3, T15 0, T16 1, T17 2; "Total: 40" | Starting Piety Track (PT) values [sic — column is PV] | PV | X-29 |
| N-019 | Turmoil bands "0–2 … 3–4 … Ob 1 … 5–6 … 7–8 … Ob 2 … 9–10 … cap 2 … Ob 3 … MS −1/season" | Turmoil Threshold Effects | Turmoil | tracks: "RS −1" |
| N-020 | WC "≥ 1 +1D"; "≥ 2 MS decay … −0.5"; "3 MS +2/season" | WC Effects | WC | X-50 |
| N-021 | Crown 5/5/5/4/5/3/4; Church 5/5/6/5/4/4/5; Hafenmark 4/4/4/5/3/3/4; Varfell 4/4/4/4/4/4/4; Löwenritter 3/3/2/3/5/3/5; Guilds 3/3/4/6/2/4/5 (L/PS/Inf/W/Mil/Intel/Stab) | Faction Starting Stats | stats | X-11, X-12, X-13 |
| N-022 | "Range [0, 7]"; RM/Löwenritter "Legitimacy = Popular_Support = 0" | L+PS Starting Values | L/PS | X-10 |
| N-023 | "Political Vacuum for 1 season" | Faction Elimination | elimination | — |
| N-024 | floors/ceilings: L 0/7, PS 0/7, Influence 1/7, Wealth 0/7, Military 0/7, Stability 0/7 | Stat Ceilings and Floors | stats | strategic P-20 |
| N-025 | Muster "2", "−1 T12 garrison"; March "No roll"; Govern "floor(Prosperity / 2) + 1", "−1 own capital"; Trade same "+1 IP≥30; +1 T2"; Diplomacy vs NPC "floor(NPC Stability / 2) + 1"; Crown Treaty "floor(target L / 2) + 1"; Thread Op "Ob 2 base"; Investigate "2", "+2 Ob … Inquisitor"; Spy "floor(target Intel / 2) + 1"; Survey "(5 − Proximity Rating) + 1, min 1", "Askeheim (PR 0) → Ob 6; Lowenskyst (PR 5) → Ob 1", Remnant "Ob −1 ×2 seasons"; Parliamentary Manoeuvre "floor(opponent Influence / 2) + 1"; Community Organising "2", "1D base + 1D per adjacent"; Community Weaving "(100−MS)÷20 round up min 1", "−1 per Presence marker"; Dynastic Proclamation "floor(target Stability / 2) + 1", "M ≥ 4", "+1 Ob if PT ≤ 1"; Martial Governance "floor(Prosperity / 2) + 2", "Accord +1 (cap 2)"; Fortify "Fort level + 1"; "All Obs: floor 1" | Standard Action Ob Reference | action Obs | X-20, X-25, X-28; strategic P-21 |
| N-026 | "Ob_modifier = clamp(Ob_modifier, -2, +2)", "(was ±3 …)" | Ethical Framework (superseded) | DA Ob | X-37 |
| N-027 | hands: Crown "2× Legionary, 1× Consul, 1× Senator, 1× Prefect, 1× Recess"; Church "2× Senator …"; Hafenmark "2× Consul …"; Varfell "2× Tribune …"; Restoration "1× Pontifex, 2× Praetor, 1× Senator, 1× Tribune, 1× Recess" vs "RM hand: 2× Praetor …, 1× Pontifex …, 1× Recess" | Batch Card Hand | cards | internal (two RM hands) |

### 4.2 `clocks.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-028 | Proximity "0–5"; MS bands "100–80 / 79–60 / 59–40 / 39–20 / 19–1"; "+1 Ob non-Thread"; "+2 Ob"; "Shifting Objects (1d10: 1–2)"; "Gaps (1d10: 1–2)"; "(1d10: 1)"; "(1d3)"; "(1d10: 1–4)" | MS Effects | radiation | R-06 |
| N-029 | "Critical (19–1): all Thread operations +1 Ob worldwide; … Stability checks … Ob 1 (failure: Mandate −1)"; "MS 0 = Rupture" | MS Effects | MS | — |
| N-030 | "Southernmost Surge (one-time, MS ≤ 10): … within Proximity 2 … one band worse for one season" | MS Effects | surge | — |
| N-031 | CI "Below 30 / 30–49 −1 Ob in Church-held / 50–69 −1 Ob everywhere, +1 Ob, Mandatory Assert/Suppress / 70–74 seizure pending" | CI Effects | CI bands | X-07 |
| N-032 | IP "Below 30 +1D / 30–59 +1 Ob, +1D Intel / 60–74 +2 Ob, Proxy at T4: +1D" | IP Effects | IP bands | X-31 |
| N-033 | "MS −1 (MS −2 for Campaign/War scale)"; "IP +2"; "Turmoil +1"; "Strain +2"; "Strain +1" | Battle Consequences | battle | X-08 |
| N-034 | Vanguard "Military 5 equivalent; Size 3"; "2 consecutive seasons"; route "T10→T3→T2→T1"; "Ob 3"; "−1 Stability/season" | Altonian Vanguard | Vanguard | X-16 (route), X-40 |
| N-035 | "Maximum 3 immediate mechanical effects" | Cascade Depth Cap | cascade | U-15 |

### 4.3 `tracks.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-036 | "Mandate = round(0.5 × Legitimacy + 0.5 × Popular_Support)" | header comment | Mandate | X-10 |
| N-037 | "2 Wealth cost. Ob 2"; "+1D Trade"; "Guild Favour +1"; "Stability −1" | Trade Network Investment | trade | — |
| N-038 | RDT "0–5"; TD "0–5" | RDT/TD | tracks | — |
| N-039 | "Ob = floor(target L / 2) + 1" | Excommunication Ob Cap | excommunication | X-51 |
| N-040 | "2 existing markers + Partial Mend = Thread Wound" | Partial Mend | thread | — |
| N-041 | "Per-territory ceiling: 10"; "First Inquisitor at AP ≥ 3. Second … AP ≥ 6"; "Max 2"; "AP −2" | Church Attention Pool | AP | — |
| N-042 | RDT advance requires "M ≥ 3 AND PI ≥ 4"; RDT 4 "−1 CI/season while Hafenmark L ≥ 3 (was ≥ 4)"; RDT 5 "+2 L", "−2 Ob", "+1 Ob"; TD 1 "+1 Wealth"; TD 2 "Stability < 3"; TD 3 "PI +1"; TD 4 "Ob +2" | RDT/TD tables | tracks | X-43; stats "Baralta L ≥ 4" |
| N-043 | Accord table (as N-017); "TCV counts only at Accord ≥ 2"; "Military conquest → Accord 1. Non-military acquisition → Accord 2+" | Accord | Accord | U-20 |
| N-044 | Turmoil "+1 … +2 … +1"; "−1 per peaceful season"; "−1 per diplomatic resolution (max 1/season)"; bands with "RS −1/season" | Turmoil | Turmoil | X-09, X-32 |
| N-045 | PT: T1 3, T2 3, T3 3, T4 2, T5 3, T6 1, T7 3, T8 3, T9 5, T10 3, T11 2, T12 2, T13 1, T14 3, T15 0, T17 3 (T16 absent) | Starting Piety Track | PT | — |

### 4.4 `parliament.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-046 | PI "0–20", "Starts at **7**"; bands "8–10 … L ≥ 4 / 5–7 / 3–4 +1 Ob, Decree Ob … 1 / ≤ 2 … CI +2" | PI Scale | PI | U-15 |
| N-047 | "Emergency Powers (−1), Church territorial seizure (−1), Löwenritter coup (−3)"; recover "+1", "+1" | PI Scale | PI | — |
| N-048 | Crown Policy "L ≥ 4"; "cannot repeat 2 seasons" | Crown Policy Instrument | policy | strategic PP-036 "Mandate ≥ 4" |
| N-049 | Govern OW "L +1 (max once/season, max to faction starting L)" | Mandate Recovery | recovery | — |
| N-050 | "Ob = floor(target L / 2) + 1"; coalition "+2D" per extra faction, "4+ … +6D (cap)"; "Pool floor: 1D" | L Suppression | suppression | — |
| N-051 | Appease "L −1"; NPC "L ≥ 4 AND Stability ≤ 3" | Uphold/Appease | mandate | strategic "Mandate ≥ 4" |
| N-052 | "CI starting value: 28 (PP-188 had set it to 22)"; "CI ≥ 65 (P-32 reduced from 70)"; "Ob = Fort + 1" | PP-189 Final Corrections | CI | X-01, X-05 |
| N-053 | Pledge "+1 Standing"; breach "Stability −1 + Casus Belli (standard, 3 seasons)"; "1 active Pledge"; Closed "PI −1" | Open Pledge | pledges | — |
| N-054 | "Crown Stability −2, Crown L −1"; "Cascade Depth Cap of 3" | Treaty Betrayal Cascade | betrayal | — |

### 4.5 `phases.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-055 | "5 provinces … (T1, T8, T14, T4, T13)"; "Draw 1 card from 6" | Game Setup | setup | X-34 |
| N-056 | priority tiers 1–7; "descending Stability order. Ties: simultaneous" | Phase 4 Resolution Priority | ordering | strategic I-07 (3+ ties alphabetical) |
| N-057 | "≥2 attribute loss … Ob = loss magnitude"; "RS baseline drift (−1 at Year-End/Winter only)"; 4c "Accord +1 (cap 2)" after "2 consecutive seasons"; "Ob 2"; 4d "Strain −1 (min 0)"; 4e "IP +2"; 6 "RS −1/token", "−0.5"; 12 "2 consecutive Accounting steps"; 13 "every 4th season" | Phase 5 | accounting | X-08, X-09 |
| N-058 | Year-End "RS baseline drift −1"; Löwenritter "Prosperity −1"; Torben "Crown PI ≥ 5 →+1; … L 2+ consecutive seasons →+1; Löwenritter PI ≥ 3 … →+1" | Year-End Accounting | year-end | X-56 |

### 4.6 `ci_seizure.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-059 | "Starting CI: 28. CI runs to 100" | CI Generation | CI | X-07 |
| N-060 | "CI +1 only if Church L > controlling faction L in ≥ 2 territories"; "CI += Σ(PT tier × SW/5)"; "CI +1 per 2 Wealth, cap 2/season"; "+1 CI per territory with Church military unit AND Church Prominence"; Assert "Influence vs Ob 2"; Suppress "L vs Ob = floor(Church L / 2) + 1"; "While Baralta L ≥ 4, CI −1/season" | CI Generation | CI | X-27, U-03 |
| N-061 | "±3 per season from player-initiated Domain Actions. ±5 per season from all sources" | CI seasonal cap | CI cap | — |
| N-062 | "Church: … L + floor(CI/20)"; "Non-Church (anti-Church motions): … L − floor(CI/30)" | Faction Political Pool | votes | X-52 |
| N-063 | "CI ≥ 60"; "P = ((CI−60)/40)^3.3 — 1% at CI 70, 10% at CI 80, 39% at CI 90, 100% at CI 100" (verified: 0.0103 / 0.1015 / 0.387 / 1.0) | Church Mass Seizure | seizure | X-06 |
| N-064 | "Ob = 10 − PT − infrastructure modifiers (floor 1)"; "Church L ≥ 4" | Seizure Ob | seizure | X-05 |
| N-065 | "PT +1"; "One seizure attempt per season"; "Cannot target T15 … or T16" | Seizure Results/Constraints | seizure | X-62 |
| N-066 | "Pool: Influence + floor(CI / 15). At CI 60: 10D. At CI 100: 12D"; table "5 → 2, 4 → 6, 3 → 7, 2 → 8, 1 → 9, 0 → 7"; "PT 5 with full infra = Ob 1. PT 0 no infra = Ob 10"; "Stability −1"; "CI < 50 … CI ≥ 50 … Intel ≥ 3" | Church Mass Seizure (one-shot) | seizure | X-05 |
| N-067 | "**Battle Ob = floor(defender Military / 2) + 1.**"; "Military ≥ 2× defending faction Military → Stability −1"; "Min 1" | Battle Ob Formula | battle | X-40 |
| N-068 | "Cap: 2 territory transfers per seizure event"; "Previously set to 4" | CI 75 Seizure (PP-421) | seizure | X-06 |

### 4.7 `ci_political_v30.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-069 | CI ceiling "75" → "100 (no freeze; Mass Seizure one-shot at CI >= 60)" | §0 | CI | X-07 |
| N-070 | PV column T1 5, T2 1, T3 3, T4 1, T5 1, T6 1, T7 1, T8 4, T9 5, T10 1, T11 1, T12 4, T13 1, T14 3, T15 0, T16 —, T17 1; SW 2,2,2,1,2,1,2,3,5,2,1,2,1,3,0,1,2 "**Total SW … 32**" | §1 | PV, SW | X-29 |
| N-071 | "SW factor = SW/5"; "T9 … yield = 1.0 × (5/5) = 1.0"; "T8 … 0.25 × (3/5) = 0.15"; "Σ(SW of Prominent territories) / 5 bonus dice"; "+1 die" in high-SW | §1 | Piety Yield | U-03 |
| N-072 | milestones "28 / 40 +1D / 55 Ob +1 / 65 extra action slot / 80 Seizure Ob −1, PT +1 … unless Warden Cooperation ≥ 2 / 100" | §2.1 | CI | X-61 |
| N-073 | "Church Mandate >= 4"; "loses 3 territories … OR Church Mandate drops to 3 or below"; struck "≥ 10 territories … 2 consecutive Year-Ends"; "11/15 … sustained 2 seasons" | §2.1–§2.2 | seizure/victory | X-01, X-06 |
| N-074 | "±5 CI per season … ±3 from player Domain Actions" | §2.4 | cap | — |
| N-075 | "⌊CI/20⌋" (+1 at 28, +2 at 40, +3 at 60, +4 at 80, +5 at 100); "FLOOR 0.05 / CAP 0.90"; "floor(CI/30)" "0–29 0 / 30–59 −1 / 60–89 −2 / 90+ −3", "floored at 0" | §3.2–§3.4 | political weight | X-52 |
| N-076 | "seasonal cap (±2 per stat per season)"; Mandate paths "+1 … −1 … +1 (OW) … −1 … −2 … −1 … −1 … +1"; Wealth "+1 … −1 per occupied territory … −2/season … −1/season Discipline … +1/year"; Military "−1 … −1"; Influence "+1 … +1" | §4.1 | stat economy | X-10 |
| N-077 | Govern "M = Mandate − difficulty, difficulty = max(1, (Ob−1)·2), Ob = floor(Prosperity/2)+1 (−1 Ob in own capital)"; "Stability −1 if Prosperity was 0"; "Accord +1 … (max 3)" | §4.2 | Govern | U-05 |
| N-078 | Trade "M = Wealth − difficulty … (+1 Ob at IP≥30; +1 Ob at T2)"; OW "Wealth +2 (capped … +2)" | §4.3 | Trade | — |
| N-079 | Turmoil "+2 … +1"; "−1 per peaceful season"; battles "MS −1 … Campaign/War scale: MS −2"; IP +2 "STRUCK by ED-743" | §4.4 | clocks | X-08 |
| N-080 | cooldowns "Legionary 1 / Consul 1 / Senator 1 / Pontifex 2 / Tribune 1 / Prefect 2 / Diplomat 1 / Colonist 2 / Recess 0" | §5.3 | cards | — |
| N-081 | AI "Stability ≤ 1 or territory count = 1"; "Stability ≤ 2 OR Wealth ≤ 1 OR Mandate ≤ 2"; "CI ≥ 55"; Crown "Mandate ≥ 4 and PV ≥ 10"; "PI ≥ 10"; Hafenmark "CI ≥ 40", "Wealth < 4", "Mandate < 4", "PI ≥ 5"; Church "CI < 60", "CI ≥ 40 … PT ≥ 3", "Accord 3"; Varfell "VTM ≥ 2", "territory count ≤ 3" | §6 | AI | X-01, X-06, X-15 |
| N-082 | "T9 … 1.0 CI/season at SW 5, PT 5 counts against the ±5/season CI cap" | §7.1 | cap | — |
| N-083 | "Church (Mandate 5 + 5 bonus = 10D, against Ob 2)"; "effective votes = 5−3 = 2" | §7.2 | worked check | — |
| N-084 | "P = ((CI−60)/40)^3.3 — 1% … 10% … 39% … 100%"; "Ob = 10 − PT − infrastructure (floor 1)" | §7.6 | seizure | X-05, X-06 |

### 4.8 `geography.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-085 | Fort: T1 2, T2 1, T3 3 ("max 4"), T4 0, T5 0, T6 0, T7 0, T8 1, T9 2, T10 2, T11 0, T12 1, T13 0, T14 3 ("max 4"), T15 0, T16 1, T17 0; Pros: 6, 4, 3, 3, 5, 2, 4, 5, 5, 3, 5, 3, 3, 4, 1, 5, 3; Proximity: T4 3, T5 2, T6 1, T12 2, T13 1, T14 3, T15 0, T16 4, T17 5 | Territory Table | map | X-44; strategic Scenario C "T4 has Fort 2" |
| N-086 | "+1 Pros/season uncontested" (T5, T11); "Muster +1D" (T8); "CI +1/season Church controls" (T9); "−1 Ob" (T9, T12, T13, T14); "Trade +1 Ob" (T12) | Territory Table | specials | X-27 |
| N-087 | SW table (= N-070) "**Total 32**"; "SW ≥ 3 territories" +1D | Spiritual Weight | SW | — |
| N-088 | Starting Accord per T (capitals 3, home 2) | Starting Accord | Accord | — |
| N-089 | "Crown … 6 … 12"; "Hafenmark … 4 … 6"; "Varfell … 4 … 6"; "Church … 1 … 5" | Starting Control | TCV | X-29 |
| N-090 | adjacency lists (26 undirected edges, verified) | Adjacency | graph | march_layer "26 edges" |
| N-091 | Proximity classes "0: T15 / 1: T6, T13 / 2: T5, T12 / 3: T1, T14, T4, T11 / 4: T2, T16, T9, T7, T10 / 5: T3, T8, T17" | Proximity Ratings | radiation | consistent with N-085 |
| N-092 | passes "NE Pass T10 … NW Pass T3 … Fires at IP ≥ 90" | Altonian Mountain Passes | IP | X-31, X-55 |
| N-093 | "TS ≥ 30 … at least 1 full season"; "(TS ÷ 10, rounded down, min 1D, max 3D) vs Ob 3"; "−1 Ob"; "VTM ≥ 2: −1 Ob"; Forgetting "Same pool vs Ob 2"; "Cooperation +1"; "VTM +1"; Edeyja "TS < 30 … 30–39 … 40+"; "TS 75–80 scale" | Southernmost Access System | expedition | X-15, X-30 |
| N-094 | Vaynard "30 (at VTM 3)", "40"; "VTM 3 achieved ~S7–9"; "VTM 4 ~S10–12"; Almud "0", "Spirit Ob 1", "10-15 Stirring", "Certainty −1", "CI +1", "CI +2"; Restoration Weaver "18" | Champion TS Values | champions | X-15 |
| N-095 | "Tribune Sabotage, Ob = Fort level"; "Fort 3 (Ehrenfeld) = defender rolls Military + 3D" | Varfell Territorial Expansion Constraint | fort | X-40 |
| N-096 | "TCV ≥ 10 + VTM ≥ 3 + 2 rival stats revealed"; "Varfell 4+4+4+4+4 = 20 points (vs Crown 22, Church 25, Hafenmark 20)" | Varfell Territorial Expansion Constraint | victory/stats | X-01, X-12 |
| N-097 | Path B "TCV held ≥ 8", "VTM ≥ 3", "WR ≥ 2"; WR "0–4"; "WR −2"; "3+ seasons … WR −1" | Varfell Path B | Path B | X-01, X-50 |

### 4.9 `territory_temperaments_v30.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-098 | pragmatic 0.7/0.3; traditional 0.3/0.7; balanced 0.5/0.5; principled 0.2/0.8; outcomes-only 0.9/0.1 | §1 | temperament | faction_behavior §3.4.1 (same) |
| N-099 | per-T assignments (T1 pragmatic … T17 balanced) | §2 | temperament | — |
| N-100 | "Crown … α≈0.50, β≈0.50"; "Church … α=0.20"; "Hafenmark … α≈0.55"; "Varfell … α≈0.50" | §3 | aggregates | X-59 |
| N-101 | "temperament_drift + 0.1 × strain_delta, -1, +1" | §4 | drift | U-14 |

### 4.10 `southernmost.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-102 | "TN 8"; "TS ÷ 20 (round down)"; Ob "1 / 2 / 3 / 4" by exposure ("< 1 hour", "1–4 hours", "4+ hours"); "TS 40+"; testimony "+1 / +2 / +3"; probabilities "76% / 0% / 24% … 27% / 49% / 24%" | Forgetting Check | forgetting | X-03, X-30 |
| N-103 | Awareness "0–7 (or 0–10 …)"; "Awareness 5+ → +2 Ob" | Southernmost Awareness | awareness | U-16 |
| N-104 | "Thread Tension ≥ 40"; "TS 30+"; "History, Ob 3"; "Resources: Ob 3"; "(1+ unit)" | Expedition Prerequisites | expedition | X-32 |
| N-105 | seasons "1 … Ob 1 / 2 … Three zones / 3 … TS 50+ auto; below TS 50: Ob 3 / 4+ … Ob 3" | Expedition Procedure | expedition | — |
| N-106 | hazards "Ob 2 … 1 Wound/character"; "Gap open, TT +2"; "Ob 2/round … Certainty −1"; "Contact duration halved" | Zone Hazard Table | hazards | — |
| N-107 | Ritual "Awareness 5+ (else +2 Ob); lead TS 60+; 2 participants TS 20+; 1 season prep"; "Ob 5"; "+1D (max +4D)"; "TT −10 / −6, 5 seasons / −3, Ob −1 permanent / +8"; "18D 80% 42% / 20D 87% 53% / 22D 92% 63%" | Ritual | ritual | — |
| N-108 | "Awareness 8+"; "TS 50+"; "Ob 4"; "Ob 3. −1D"; "TT −2 … Awareness +1 / TT −1 … CD +1 / TT +1 … CD +2"; "After 4-5 successful seasons" | Extraordinary Repair Weaving | repair | — |
| N-109 | "max −5 per season" (was "up to −12") | Combined TT Reduction Cap | cap | — |
| N-110 | "TT 50"; "3 seasons"; "TT +1/season"; "3+ seasons"; "TT +2/season"; Stabilising Weave "Ob 3, TS 40+" | Crisis Timeline | crisis | X-32 |

### 4.11 `generational_transition_v30.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-111 | "≥2 Convictions resolved"; "floor(predecessor's Resources / 2) + new character's starting Resources"; example "floor(6/2)=3 + … 1-2 … = 4-5" | Trigger / TRANSFORM | inheritance | X-23 |
| N-112 | "Standing: reset to 0"; "Coherence: reset to 10"; "Wounds: 0"; "Momentum: 0"; "Combat Reputation: 0"; "Exposure: 0" | RESET | reset | U-30 |
| N-113 | "Renown: reset to 0, but predecessor's Renown ≥ 7 grants +1" | TRANSFER | Renown | X-23 |

### 4.12 `fractional_province_ownership_v30.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-114 | "≥ 1 settlement … NOT the nominal province controller" | §2.1 | trigger | — |
| N-115 | "(settlement Prosperity / sum …) × province base PV"; "base PV 4 … 3/2/1 … 2/1.33/0.67 … (rounded to 1 decimal)"; FRAC-01 "floor(base PV / settlement count), remainder to Seat", "Accord forced to 0" | §2.2 | PV | X-46 |
| N-116 | "≥ 75% of a province's PV"; "Ob = remaining non-faction-held PV share × 2 (round up)"; Submit "Order −2"; "within 1 season" | §2.4 | consolidation | — |
| N-117 | Fragmentation "Pool: Seat-holding faction's Influence; Ob: 2 + (number of non-Seat-held settlements)"; OW "4 seasons"; Partial "Order drops −1" | §2.6 | fragmentation | conflict "Influence 5 vs Ob 3" |
| N-118 | "3.33/4.0 = 83%"; "(0.67 × 2) = 1.33 → round up to Ob 2"; "Roll 5d10 vs Ob 3" | §3 | worked | U-06 |
| N-119 | "currently 2-decimal" | §5 | rounding | X-46 |

### 4.13 `settlement_adjacency_v30.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-120 | Road "1"; River "1", "Attacker −1D"; Mountain Pass "2", "−1D"; Coastal "1 (requires naval)"; Thread-Witnessed "0" | §1.1 | edges | — |
| N-121 | "(36 settlements)"; "49 edges: 19 intra-province, 26 inter-province, 4 thread-witnessed"; "26 territory-adjacency edges"; hubs S-001, S-015, S-026, S-023; overrides S-002, S-011, S-034, S-031, S-016, S-021, S-007, S-004, S-024, S-017, S-008; thread edges S-003↔S-023, S-011↔S-033, S-026↔S-025, S-029↔S-032 | §1.2 | graph | X-18 |
| N-122 | "traverse 1 edge per season"; "**Military ÷ 2 edges** (round down, minimum 1)" | §1.3 | movement | X-20 |
| N-123 | Fortress "+Fort Level to Defender Ob"; Seat "+1 Defender Discipline"; Port "+1D"; Coastal "loses Fort-level bonus" | §2.2 | battle | X-40 |
| N-124 | "MS −1 to −2"; "Strain +1"; "IP +2"; "Order −1"; "Prosperity −1 on … Partial or worse" | §2.3 | consequences | X-08 |
| N-125 | Siege "Order −1/season until Order = 0" | §2.4 | siege | — |

### 4.14 `march_layer_v30.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-126 | "march_budget_pixels = Military × 100 × cavalry_modifier (1.5 if Cav ≥ 50% …) × skirmish_modifier (1.3 …)"; "capped at 1.7× total"; "1.5 × 1.3 = 1.95, capped at 1.7×" | §1–§1.2 | movement | X-20 |
| N-127 | "default 8 settlements"; "+1 per season per 4 settlements over budget"; "1:1 ratio (rounded down)" | §1.3 | attrition | U-11 |
| N-128 | "within +20% cost"; "Size ≥ 1"; "season Q4 and Q1"; "radiation band ≥ 4" | §2.3–§2.4 | routing | — |
| N-129 | "Base 240 px"; "Ob 3"; "half the march budget"; "2 hops"; "Intel investment ≥ 3 … +1 Ob … 1 hop"; "TS ≥ 50"; "+1 Knot strain" | §3 | vision | — |
| N-130 | "26 edges across 17 provinces"; gate "attacker −1D"; mountain_pass "attacker −1D" | §4 | edges | X-19 |
| N-131 | "+1 attrition per bypassed hostile settlement" | §4.3 | bypass | — |
| N-132 | "Casus Belli +1"; "IP −2 to the trespassing faction" | §5.4 | crossing | U-11 |
| N-133 | "IP ≥ 75 → Altonian sea route opens" | §6.3 | naval | X-31 |
| N-134 | "TS ≥ 30 individual gating"; gates "attacker −1D"; "+1 IP per season" for holding a gate | §7 | calamity | U-29 |
| N-135 | "17 province polygons + 36 settlement nodes + 26 adjacency edges"; "1920×2880 ÷ 32 = 60×90 hex grid"; "4×"; "36×36 settlement pairs (≤ 630 unordered pairs)"; "Godot 4.6" | §8 | implementation | X-18 |

### 4.15 `valoria_political_hierarchy_v30.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-136 | "Duchy (3 …)"; "Six provinces … Four provinces … Four provinces"; "1–3 per province"; "The minimum is 2"; "7 provinces at 3 settlements and 7 at 2 (14 provinces total … = 35 settlements)"; "Himmelenger at 5 connections"; "Schoenland at 1"; "56-edge" | §1–§2.2 | hierarchy | X-18, X-19 |
| N-137 | "political_value(faction) = Σ … territory_value + Σ … province_unification_bonus" (scalars "TBD") | §2.4 | PV | U-28 |
| N-138 | "Standing 3+ NPCs" governors; "S-001..S-037"; "30+ sub-features"; "22 of the 36 … 14 … 21 new" (settlement_layer §2.3) | §2.5, §4 | registry | — |

### 4.16 `settlement_layer_v30 (1).md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-139 | "T1–T17 | 17"; "S-001 to S-036 | 36"; "1–3 settlements" | §1.1 | map | X-18, X-19 |
| N-140 | "Prosperity × 50"; "Defense × 20 + Fort Level × 30"; "Order × 20"; stats "0–5"; "Order 0 = local revolt. Order 3+ = stable"; "floor((4+2+1)/3) = floor(2.33) = 2" | §1.3 | derived | X-45 |
| N-141 | slots: Seat 3/5/8; City 1/3/5; Town 0/1/3; Fortress 0/1/4; Cathedral 1/3/5; Port 0/1/3; Mine 0/0/1; Outpost 0/0/1 ("Wing Std 6+ / Suite Std 5 / Chamber Std 3–4 / Billet Std 1–2"); "Treasury −300", "+1 Wing … per decade"; "Ob 2" | §1.4 | facilities | — |
| N-142 | "+0.5 PT/season … +1 PT/season … +2 PT/season, +0.5"; "+1 CI/season"; "(+1 Ob, costs 1 CI)"; "Mandate Challenge (Ob 6+)"; mods "−0, −1, −2, −1, −1, −2"; "Cap: −4 per settlement" | §1.5 | Church axes | X-24 |
| N-143 | Chapel "+0.5 Order/season"; Church "+1 Order"; Cathedral "+1 Order … decay −1" | §1.6 | parish | — |
| N-144 | Pastoral Assumption "Ob 1"; revoke "Ob = Church Influence ÷ 2, Order −1, Disposition −2" | §1.7 | governor | — |
| N-145 | L, PS "0–7"; "W_s = base(Type) + Prosperity_s + FacilityTier_s"; base "Seat 3, City 3, Cathedral 3, Town 2, Fortress 2, Port 2, Village 1, Mine 1, Outpost 1"; "W=1 → … W=11"; "q_s = 0.5·L_s + 0.5·PS_s"; "T = Σ_s W_s · (q_s / 7)"; "Mandate = clamp( round( 7 · T / (T + K) ), 0, 7 ), … K = 6"; "Σ settlement Prosperity × 10"; feedback "≥1 below … L +1 … ≥1 above … PS −1 … ±1 per settlement per season"; "sim: Mandate 5"; "Mandate × 20"; "Reputation ×15, Discipline ×10, Treasury ×100" | §1.8 | Mandate | X-10, X-45 |
| N-146 | "35 settlements across 14 provinces in 3 duchies"; "37 settlements"; "Valorsmark 6 provinces (15 settlements), Hafenmark 4 (10), Varfell 4 (10)" | PART 2 | registry | X-18 |
| N-147 | governor eligibility "0–2 … 3 … Town or Outpost … 4 … City, Fortress, or Mine … 5 … Seat or Cathedral"; Develop "floor(Prosperity/2) + 1"; Fortify "floor(Defense/2) + 1"; Pacify "floor((3 − Order) + 1), min 1"; Administer "2"; NPC governors "Order ≥ 2" | §3.2 | governance | X-22, U-12 |
| N-148 | Church "+1 Piety Influence"; Guilds "+1 Trade"; Ministry "Order decay −1"; Löwenritter "Defense +1"; RM "CV −1 … PT ≤ 2"; Wardens "1 band earlier"; Niflhel "+1D", "Evidence Track threshold 3"; RM cells "≥ 3 settlements … +1 Ob"; grant "Ob 1"; revoke "Ob = … Influence ÷ 2, round up", "Order −1", "Disposition −2" | §3.3 | subnational | X-38 |
| N-149 | "1 scene per province traversed"; "Depth 3" | §4.1 | travel | — |
| N-150 | events: "Prosperity 0 … Order −1"; "Order 5 + Prosperity 4+ … +1 Disposition"; RM transition "−1 Order for 2 seasons, … +0.5/season; PT −1"; "PT drops 0.5"; "4-season"; Consensus Delay "+1 season", "1 Mandate + … 1 Presence marker"; "Prosperity 3+ … +50/season"; Fortress "Defense pool vs Ob 2" | §4.3 | events | — |
| N-151 | "Cap: ±1 per settlement stat per season"; ops table (Order/Prosperity/Defense ±1) | §4.4 | thread ops | — |
| N-152 | Local Actors "1–2"; counts "Seat 2, City 2, Town 1, Fortress 1, Port 2, Cathedral 1, Mine 1, Outpost 0 … ~45–50 across 36"; Disposition "+1 … 0"; drivers "+1 / −1 / +1 / −2 / +2 / reset to 0 / +1"; recruitment "+3" | §4.5 | NPCs | — |
| N-153 | black market "Order ≤ 1"; "Order ≥ 3"; "Wealth +0.5"; "Accord −0.5"; brokers "Prosperity ≥ 3 … Stability ≤ 2"; exploitation "Proximity ≤ 2"; "RS −0.5 per harvest"; "Wealth +1" | §4.7–§4.9 | Niflhel residue | U-12 |
| N-154 | Assault "Military vs Defense + garrison"; Siege "Military ≥ Defense", "Order −1"; Bypass "Military > Defense by 2+", "Military vs Ob 1 … −1 Discipline"; "Order ≥ 3 may resist"; Fortress "exceeds … by 3+"; "Lowenskyst Fortress (S-006, Defense 4) requires Military 7+" | §5.1 | invasion | X-18 |
| N-155 | "effective Defense = settlement Defense + garrison Discipline"; "Defense 0 … auto-captured" | §5.2 | defense | X-40 |
| N-156 | ladder "0–2 / 3–4 … 3 / 5–6 … 4 … up to 3 settlements / 7–8 … 4–5 / 9–10 … 5"; "Standing track (0–5 …) and Renown track (0–10 …)" | §6.1 | stature | X-22 |
| N-157 | "2 → 3 | Control 2+ settlements. Renown 5+. … 2 NPC officers with Disposition +3"; "3 → 4 | 4+ settlements across 2+ provinces. Renown 7+. … Influence pool = Renown ÷ 2, Ob 3 … 1 province Seat"; "4 → 5 | 2+ province Seats. Renown 9+" | §6.2 | emergence | — |
| N-158 | founded faction "L 2, PS 3, I floor(Renown ÷ 2), W 2 + (# settlements − 1) capped at 5, Mil 1, Int 2, Sta 3" | §6.2 ED-790 | founded stats | — |
| N-159 | collapse "Order ≥ 3 + governor Disposition ≥ +3"; "Standing 4+"; Hafenmark city-state "Influence 4, Wealth 3, Stability 3" | §6.3 | collapse | — |
| N-160 | "13–15 year game"; "20–30 years"; MS "−1/year … 72 → 0 in 72 years; 30-year game = MS ~42"; CI "Passive +1/season if Church Mandate ≥ 3 … CI caps at 75 … ~47 seasons (~12 years)"; IP "+1/season baseline → +1/2 seasons … 100 in 80 seasons … 100 in 160 seasons … 30-year game: IP ~80"; "Political Stability | 0 start, +1 per violence event … (≤ 6)" | §7.1 | clocks | X-07, X-27, U-12 |
| N-161 | Generational Shift "0–10"; "+1 per 5 years"; "Threshold 2 (Year 10) … −1"; "TS ≥ 50 are exempt"; "Threshold 4 (Year 20) … −2"; "Threshold 6 (Year 30) … −3" | §7.1 | generational | — |
| N-162 | "Order −1 per season until a governor is assigned"; protégé "Disposition +4 and Standing 4+"; "Renown ÷ 2 (round down)" | §7.2 | succession | X-23 |
| N-163 | "2–4 POIs"; Depth "0 … 3+" | §4.6 | POIs | — |
| N-164 | ED-SETT-02 "Ob 2 standard / 3 recovery / 4 crisis"; ED-SETT-03 "Seat getting +1 weight"; ED-SETT-04 "Siege duration 4 seasons for Order 4"; ED-SETT-06 "Stability ≤ 2" | PART 9 | open items | U-12 |

### 4.17 `conflict_architecture_proposal.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-165 | "5+ seasons" (peninsula lag) | The Three Scales | pacing | — |
| N-166 | "(Influence 5 vs Ob 3)"; "Prosperity 5, highest non-capital"; "Fort 3, five-way hub" | Starting Friction Points | fragmentation | U-22 |
| N-167 | Bishop appointment "Church building ≥ tier 2 … no governor OR … Disposition toward Church ≥ +2 … Influence vs Ob 1"; "CI 60+"; "15 seasons"; "+0.5 from Parish Social Services" | Church Expansion | appointment | X-06 |
| N-168 | autonomy table "Counter ≥ 4 → instant" (replaced); Restless "Crown Stability ≤ 3 … 4+ seasons … +1 Ob … Ob +1"; Autonomous "≤ 2 … below 0 … 4+ seasons … PI −1"; Split "4+ seasons … (M3/I2/W3/Mil6/Stab5). PI −3 … PV drops by 3 … Fort 3 + Mil 6"; reversible "raising Stability above 3" | Graduated Löwenritter Autonomy | autonomy | X-12, X-14 |
| N-169 | "One assassination … S8+"; "S1–S7"; "S8–S12 window" | Royal Assassination as Fuse | assassination | U-17 |
| N-170 | black markets "Order ≤ 1 or no governor … Wealth +0.5 … Accord −0.5 … Order ≥ 3"; "Proximity ≤ 2" | Niflhel Dissolution | residue | X-38 |
| N-171 | "6 cards, draw 1"; "S8+"; "(was) 8–10 cards, draw 2"; "IP starts at 0" | Tensions Deck / What's Cut | deck, IP | X-31, X-34 |

### 4.18 `campaign_architecture_v30.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-172 | axes (= N-142 values) "Maximum per-settlement Seizure Ob modifier: −6"; "Base Seizure Ob = 10 − PT − infrastructure modifiers (floor 1)" | §1.1–§1.2 | seizure | X-05, X-24 |
| N-173 | "CI reaches 100"; "1 Emergency Session season"; "all 15 territories at Accord ≥ 2"; "Accord 1 … or Accord 2 (if PT ≥ 3)" | §1.3 | mass seizure | X-01, X-06 |
| N-174 | "−1 MS per battle"; "MS ≤ 10 … Stability Check (Ob 3) … −1 MS (max −2/battle)"; "Three battles per season = −3 MS" | §3.1 | MS | X-08 |
| N-175 | Coherence costs "0 / 0 / 1 / 1 per test / 2 per test / 1–2 (by scale) / 2 per test" | §3.2 | Coherence | — |
| N-176 | fatigue "op 2 = −1D, op 3 = −2D, op 4 = −4D, op 5 = −7D, op 6 = −12D"; "+2 Ob" per scene | §3.2a | fatigue | U-21 |
| N-177 | Mending "1–2 +1/+2; 3–4 +1/+3; 5 +2/+4; 6 (Edeyja) +2/+5 … (MS ≤ 5)" | §3.3 | Mending | — |
| N-178 | "MS ~72"; visibility bands "100–80 … 19–1" | §4 | revelation | N-028 |
| N-179 | "Phase 1 (IP reaches 100)"; "+1 Ob"; "Phase 2 (IP sustained 85+ for 3 seasons …) … (Mandate 2, Military 4, Stability 3)"; "Phase 3 (IP sustained 80+ for 3 more seasons) … Mandate 3, Military 5, Stability 4 … +2 Ob"; retreats "IP < 85 … IP < 75 … IP < 60" | §5.1 | invasion | X-31 |
| N-180 | "Two consecutive Overwhelming … IP resets to 60. Cannot rise above 80 for 10 seasons"; "Elske Loyalty ≥ 6 + Social Contest … (Ob 4) + IP < 80 → IP drops to 40. Overwhelming: IP to 20 + Non-Aggression Pact 20 seasons"; "Underground Network Mandate 3 + … Accord 0 … → IP resets to 30" | §5.2 | repulsion | — |
| N-181 | Loyal "Crown Mandate +1 in T16-T17"; "Crown Stability ≤ 1" | §5.3 | Elske | X-16 |
| N-182 | Wardens "~8–15 Einhir"; "WR 3+"; "MS ≤ 20" | §6 | Wardens | — |
| N-183 | "≥ 2 of 3 starting Convictions"; "(3 arcs)"; Fulfilled "≥2 scene actions"; Failed "≥1"; Transformed "≥1" | §7.1–§7.3 | retirement | — |
| N-184 | Mentorship "Skills at 60% … 1 Close Knot (Disposition −2) … Disposition ≥ +3"; Thread Legacy "WR at half (rounded down) … WR ≥ 2" | §7.4 | lineage | X-23 |

### 4.19 `treaty_expiration_v30.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-185 | "N=1000"; "55-90% win-rate" | Scope | balance | — |
| N-186 | "(4 seasons per arc)"; "end of season 4, 8, 12, …"; "`TREATY_LAPSE_RATE` ∈ [0.90, 0.95] (canonical default: **0.90**)"; "roll < TREATY_LAPSE_RATE" | §1.1 | lapse | — |
| N-187 | Senator Outward "1 per season"; "Wealth −2"; "Influence + Standing modifier"; "Target faction Sta"; "Standing +1"; "CB-blocking effect for 1 arc"; "Standing −1"; "3 Treaties … 3 season-actions per arc" | §2 | re-binding | X-25, U-08 |
| N-188 | violation "Standing −2"; "Standing +1" | §3 | violation | — |
| N-189 | "Crown 24.7% / Church 28.6% / Hafenmark 24.2% / Varfell 22.5%"; "+0.05 → Crown −1pp"; "0.90, 0.92, 0.95 … within 7-10pp" | §5 | balance | X-58 |

### 4.20 `parliamentary_transfer_v30.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-190 | "1 per arc per faction"; "Holder Legitimacy + `PARL_MAJORITY_OB_BONUS` (default 2)"; OW "Holder Legitimacy −1 … Accord = 1"; Success "Accord = 1"; Failure "Stability −1 … Legitimacy **+1**" | §1.1–§1.2 | transfer | X-47 |
| N-191 | "only 1 territory remaining" | §1.3 | protection | U-09 |
| N-192 | Appeasement "Accord granted +2 instead of +1"; "Peninsular Strain >= severe" | §2 | modes | X-47, U-09 |
| N-193 | "Crown territories < 6"; "Accord ≤ 1 … CB persists 1 arc"; "Conviction Scar … (≥3 …)" | §3 | CB | — |
| N-194 | "Pool +1D … Pool −1D … no modifier" | §4 | vote | U-09 |
| N-195 | "24.7% … 3.4 … 0.8; 28.6% … 4.8 … 0.5; 24.2% … 5.6 … 0.6; 22.5% … 2.3 … 1.0"; "20-30% band"; "7.2pp"; "~2-4 times per campaign"; "~60% … ~5% … ~75% … ~15% … ~5%"; "3 … ~40% … 1 … Crown I=5 vs others' L=4-5" | §5 | balance | X-58 |

### 4.21 `insurgency_pipeline_v30.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-196 | "`RM_BASE_STRENGTH` 1; `RM_GROWTH_PER_ARC` 1; `RM_PT_DECAY_CHANCE` 0.35; `RM_VARFELL_COOPTION_BONUS` 0.1"; "min(0.8, 0.35 × (1 + 1 × (arc − 1)))"; "(capped at 0.9)"; "PT − 1" | §2 | PT decay | U-10 |
| N-197 | "WA ≤ −2"; "At least 3 territories have PT ≤ 1"; "MS ≤ 50" | §3.1 | Latent RM | — |
| N-198 | Latent RM "Mandate … (min 2, max 5) … Influence 4 … Wealth 1 … Military 0 … Stability 3"; "+1 Ob" | §3.2 | RM stats | X-36 |
| N-199 | "Thread Tension ÷ 20 (round up, min 1) … TS 30+"; "MS +2, PT −1 / MS +1, PT −1 / … / Stability −1, MS −1"; Grassroots "Ob 2 … PT ≤ 2 … caps at Mandate 5"; Resist "+1 Ob" | §3.3 | RM actions | X-28 |
| N-200 | "2+ contiguous territories at Uncontrolled status, sustained 2 consecutive seasons" | §4.1 | formation | — |
| N-201 | "Legitimacy 1.0 Float"; "Influence … 2-3"; "Stability … 2"; "Wealth 0-1" | §4.2 | insurgency stats | X-21 |
| N-202 | "L ≥ 3"; "2+ territories"; "Accord ≥ 4 averaged"; "2 consecutive seasons"; "PT < 3 … PT ≥ 3" | §5 | promotion | X-21 |
| N-203 | suppression "WA ≥ 0"; "PT ≥ 2"; "Stability reaches 0"; dissolution "Legitimacy < 1.0 AND territorial count < 2"; "−0.5/season" | §6 | de-escalation | X-21 |
| N-204 | "11+ territories sustained 2 seasons" | §7 | victory | X-01 |

### 4.22 `faction_succession_split_v30.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-205 | "ransom paid within 2 seasons"; "Disposition ≥ +3"; "Standing ≥ 4" | §2–§2.1 | trigger | — |
| N-206 | "Standing ≥ 3"; strengths "Mandate + Influence / Influence + … / backer's Influence + own Standing" | §2.2 | contest | X-10 |
| N-207 | "G ≥ 3 … UNIFIED … Stability −1, Mandate −1"; "G = 2 … Disposition ≥ 0"; "G ≤ 1 … SPLIT … ~60% … ~40%"; "3 consecutive Accountings" | §2.3 | outcomes | U-07 |
| N-208 | "60% (round down) … 40%"; "70% … 30%"; "Stability … current − 1 … Splinter: 2" | §2.4 | split | — |
| N-209 | "50% of frozen parent values"; "Mandate ≥ 3" (re-merge) | §2.5 | splinter | — |
| N-210 | example "Season 12"; "Mandate 3 + Influence 4 = 7"; "Influence 4 + Intelligence 5 = 9"; "RM Influence 3 + Standing 2 = 5"; "7d10 vs Ob 3 → 3"; "9d10 … 4"; "5d10 … 1"; "60% of Vaynard's 5 = 3 … 40% = 2"; "70% of 4 = 2 … 30% = 1"; "Ob −1" | §3 | worked | X-11 (Intelligence 5 vs Intel 4) |
| N-211 | RM stages "2+ settlements … 4+ settlements across 2+ provinces OR … 1+ provincial Seat … 2+ provinces"; Settlement Emergence "Order = 0 … PT ≤ 1 … Disposition … ≥ +3"; "once per province per 4 seasons" | §4 | RM emergence | — |

### 4.23 `baralta_crown_claim_v30 (1).md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-212 | "Löwenritter Autonomy 4 → coup"; "(PI ≥ 5 + Church Mandate ≥ 5 + Crown Mandate ≤ 1 + 2 Standing tokens)" | §1 | deposition | X-14, X-35 |
| N-213 | "Mandate 0 + Loyalty 0"; "Mandate ≥ 3"; Löwenritter "Military 5 + Stability … Autonomy ≥ 3"; Hafenmark "Mandate + Influence … Mandate ≥ 4"; Church "CI ≥ 40"; "Ob 3 (TN 7)"; Church wins "CI +10 … Stability check Ob 2" | §2 | contest | X-03 |
| N-214 | Stake Claim "Crown Mandate ≤ 2 AND PI ≥ 5"; "(4 + 4 = 8D at game start)"; "Ob: Crown Mandate + 1 (minimum Ob 2)"; "+2D"; "Stability −1 … 2 seasons" | §2 Baralta Claim Precondition | claim | — |
| N-215 | "Church Stability ≥ 4 … CI +3 … −2 … 3 consecutive seasons … below 3 … +0.5/season"; "Church Stability ≤ 3 … CI −5 … Stability −3 … floor 0" | §3 | consecration | faction_politics §6.2 "drops to 0" |
| N-216 | "Church Stability 5 (game start value)"; "Season 3-4"; "35-40 range, drops to 30-35"; "Season 8-10"; "Season 14+" | §4 | scenarios | — |
| N-217 | "Wealth 5 (highest non-Guilds)"; "PI ≥ 4 … PI < 4"; "Standing 7 … Crown Standing 5 … Crown Std 2 … Chancellor (Std 6)"; "Disposition ≥ 0 … demoted to Std 3 within 1 season" | §5 | succession | — |
| N-218 | "Campaign Seasons ≥ 24"; "≥ 4 (Crown-aligned) … ≤ 3 (Altonian)"; "Readiness ≥ 5"; "≥ +1 … ≤ 0"; "Crown Stability ≤ 1 … +1 automatic"; "Counter was at 2 … fires"; "IP ≥ 60 … ≤ 3 to ≤ 4"; "IP ≥ 75 … Disposition ≤ 0 … Priority 2"; "+1 Ob"; "Disposition ≤ −2"; "Löwenritter Autonomy ≥ 2"; "+2D … LIN-01"; "Stability −1"; "Counter reaches 3, Coup fires"; "within 1 season" | §7 | generational | X-14, X-49 |

### 4.24 `ministry.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-219 | "L 3 / Influence 4 / Wealth 2 / Military 0 / Stability 5" | Ministry Stats | stats | — |
| N-220 | AP-tokens "T14, T2, T5, T1"; "Accounting Step 11"; "reduced by 1"; "PI +1" (Legislative Record); "L < 2 … +1 Ob; L = 0 … unavailable"; seizure "Ob +1"; "1 season"; Manoeuvre "Ob −1 / +1"; coup "Ministry L −2. PI −3"; "1/season" | Parliament Connection | Ministry | X-17, X-42, X-56 |
| N-221 | tree "PI ≤ 3 … (3D) vs Ob 1 … PI +1"; "L 3D vs Ob 1"; "delayed 1 season"; "Crown L ≥ 4 AND PI < 5 … PI +1" | Priority Tree | AI | X-17 |
| N-222 | Corrupt "Ob = floor(Ministry L / 2) + 1"; "−1 Ob"; "Stability −1"; Collapse "L 0 … 2 seasons"; exit "Ob 2 … L returns to 1" | Compromise and Corruption | corruption | — |
| N-223 | summary "L ≥ 2 … L ≤ 1 | Crown Policy unavailable" | Summary | — | X-42 |
| N-224 | Guilds CP-tokens "T11, T8, T3, T1, T9" | Guilds CP-Token Starting Positions | tokens | — |

### 4.25 `institutions.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-225 | "Stability drops below 3"; Templars "Stability ≥ 2 … ≤ 1"; "+0.5 Wealth/season … Favour ≥ 3"; "Church Stability = 2 AND … Senator action" | Four Cardinals | Church | X-43, U-26 |
| N-226 | levies "Two-thirds"; "Military +1 … Church Military −1"; "Crown L ≥ 4" | Church Levies | levies | — |
| N-227 | penance "Wealth −1 per season … (3 seasons)" | Excommunication — Canonical Procedure | excommunication | — |
| N-228 | "deny T10 sea access … at IP < 75"; "March Ob −1"; "once per season" (cancel Intel) | Löwenritter — Structure | Löwenritter | X-16 |
| N-229 | Reconstitution "PI = 0 … L vs Ob 3 … Once per season"; "PI restored to 2 / 1 / 0 Stability −1 / … Church L +1"; "PI ≥ 4 required" | Reconstitution | PI | X-01, X-26 |
| N-230 | "Influence (4) … L (3)"; Guilds "L ≥ 2 … +1 Ob … L ≤ 1 … +1"; nomination "Ministry L +1 … +1 … Wealth +1 … 1 Wealth … −1 Ob … Influence +1"; "Crown L ≥ 3 … L < 3: roll L vs Ob 2" | Ministry — Canonical Identity | Ministry | — |
| N-231 | deposition "PI ≥ 5 … Church L ≥ 5 … Crown L ≤ 1 … 2 other player factions"; "Senator Inward, Ob 3"; "Coup Counter immediately set to 4" | Parliament Deposition | deposition | X-14, X-35 |
| N-232 | Parish "2 sequential … + 1 Wealth … PT floor … 1"; Cathedral "3 more … (5 total …) + 2 additional Wealth … PT floor 2 + … Prominence +1"; "Max 1 … per territory. Max 1 upgrade attempt per territory per arc" | Parish / Cathedral System | Church buildings | X-24 |

### 4.26 `worldbuilding_v30 (1).md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-233 | "Ob 3 … Stability −1"; Jarnstal Drift "0–3 … At 3 … Stability −2, … CI +2"; Klapp "Stability −1, CI +1 … −1D" | §3.2 | Cardinals | — |
| N-234 | cards: Jarnstal "Stability −2. CI +2 … 1 Influence + 1 Stability … once per game"; Olafsson "Stability −2, CI −3 … 2 seasons … +1 Ob … 1 Stability"; Klapp "within 1 territory of T3 … CI ≥ 30"; Prudence "Prosperity ≤ 3 … +1 Influence … 1 Wealth" | §3.3 | cards | X-16, U-25 |
| N-235 | Penance "1 season … Mandate +1"; Grand Debate "5 exchanges"; Banishment "Ob 4" | §3.5 | reversal | — |
| N-236 | "IP 50 … (IP −3, CI +2)" | §3.6 | Almaic Kyriakos | — |
| N-237 | Seam Texts "TS 30+ … TS 0–29" | §3.7 | POIs | — |
| N-238 | Riskbreaker "Intel vs Ob 2"; Exposure "Debt reaches 3 … +1 Ob … Debt 5"; Mutiny "Military drops to 2 or below" | §4 | Löwenritter | — |
| N-239 | Journeymen "3+ territories … 2+ seasons … +1D"; Schism "Stability … 2 or below … 1 Influence … +1 … +1 … 1 season"; Forum Revolt "Stability ≤ 3 … Wealth +1 … +1D" | §5 | Guilds | — |
| N-240 | deposal "Crown Mandate → 1, Stability −3 … IP +10 … +2 Ob"; refusal "CI +3, … TT +2"; Constitutional Crisis "Mandate drops to 1 OR … 3+ territories"; Ministry Collapse "Stability … 2 or below … Wealth −1 … +1 … −1 Prosperity … 1 Influence" | §6 | governance | X-41 |
| N-241 | Kaldring "Age Late 60s; TS 22; Composure 9 (Presence 4 + 5); Histories (3), (2), (2); Circles Ob 2 south, Ob 4 elsewhere; TS 22 < 30 threshold" | §8 | NPC | X-63 |
| N-242 | §9.1 T-numbers (Valorsplatz T12 … Oastad T4) | §9.1 | map | X-16 |
| N-243 | §10 table: "Debt 3/5"; "Jarnstal Counter reaches 3"; "Church Wealth ≤ 2"; "Military ≤ 2"; "Stability ≤ 2 … Wealth −1, Influence −1 … Favour → 0"; "Stability ≤ 3"; "Mandate ≤ 1 OR … 3+"; "Stability ≤ 2 … 1 season" | §10 | cards | U-25 |

### 4.27 `stats_1_7_scale (1).md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-244 | "Faction stats (6)"; "±2 per stat per season (TTRPG)" | Stats | schema | X-11 |
| N-245 | Crown "5 5 5 5 5 4 4 5/6 3 4"; Church "5 5 5 5 6 5 5 4 4 5"; Hafenmark "4 4 4 4 4 5 5 3 3 4"; Varfell "4 4 4 4 4 4 4 4 4 4"; Guilds "3 3 3 3 4 6 6 2 4 5"; Löwenritter "— — 3 3 2/3 — — 5/6 3 5/4"; Intel "3 / 4 / 3 / 4 / 3 / 4" | Starting Stats | stats | X-11, X-12 |
| N-246 | "Spy Ob = floor(target Intel / 2) + 1"; "Intel ≥ 4 … Intel vs Ob 3" | Mechanical roles for Intel | intel | — |
| N-247 | CI "0 / 28"; MS "60 / 72"; Institutional Pressure "20 / 20"; Public Instability "— / 5" | Clock Starting Values | clocks | N-007, X-32 |
| N-248 | "difficulty = … relevant stat … OR fixed"; "D = max(1, (O−1)·2)"; "P_success(M) = clamp(0.50 + 0.10·M, 0.05, 0.90)"; "P_overwhelming(M) = clamp(0.50 + 0.10·M − 0.35, 0, 0.55)"; "P_atleast_partial = clamp(0.50 + 0.10·M + 0.20, P_success, 0.97)"; "BASE 0.50 … SLOPE 0.10 … FLOOR 0.05 … CAP 0.90 … M ∈ [−4, +4]"; "Success +1, Overwhelming +2, cap ±2" | Domain Action Resolution | resolver | X-04, U-05 |
| N-249 | "Assert: M = Influence − 2"; "Reconstitute: M = Influence − 6 (legacy Ob 4 → difficulty 6)"; "Suppress — M = Mandate − (Church-L difficulty)"; "Positioning … own Influence − target Influence"; "Ratification: M = Mandate − 2"; "Guarantor … +1 M"; "Overwhelming +2 / Success +1 / Partial 0 / Failure −1"; "+⌊CI/20⌋"; "M = Stability − loss_magnitude"; "Royal Decree M = Mandate − 2"; "Excommunication … M = Mandate − target Mandate … M = Mandate − 2"; "Private Collection M = Intel − 2"; "Economic Leverage … M = Wealth − target Wealth"; "bare Mandate vs Ob 4" | Governed checks | resolver | X-26, X-51 |
| N-250 | legacy "Ob = floor(relevant stat / 2) + 1"; "TN 7" | Domain Action Rules (TTRPG) | legacy | — |
| N-251 | "+1 per season"; Assert "+2 total"; Suppress "Ob = floor(Church L / 2) + 1 ÷ 2 (round up, min 1)"; "once per season by one faction" | CI Passive Advance (PP-402) | CI | X-27 |
| N-252 | "−1 Stability" on Failure | PP-403 | stability | — |
| N-253 | Leadership Deviation Obs "Crown: 2 | Church: 3 | Hafenmark: 2 | Varfell: 2 | Guilds: 2 | Restoration Movement: 2 | Löwenritter: 2" | Leadership Deviation | stability | — |
| N-254 | Seizure "Influence + floor(CI/15) vs Ob = 7 − PT"; "+2 Ob"; "Mandate −1"; "one season" | CI 60 Territorial Seizure | seizure | X-05, X-06 |
| N-255 | "Mending Stability ≤ 10 adds +1" | NPC Trigger Conditions | triggers | — |
| N-256 | Royal Decree "Consecutive seasons: difficulty +2/season (legacy +1 Ob)"; "One faction stat ±1" | Crown — Royal Decree | decree | — |
| N-257 | Sovereign Authority "Mandate vs Ob 4. Once per campaign arc"; OW "CI −3 … +1D"; Success "CI −2 … Ob 4"; Partial "CI −1 … +1"; Failure "CI +1 … L −1"; "L ≥ 4 … −1/season … CI +4" | Hafenmark — Sovereign Authority Doctrine | unique | — |
| N-258 | Private Collection "+2D"; "+1D vs Varfell for 1 season; Thread Tension +1"; "+1 to Vaynard's hidden TS … At Thread Sensitivity 14+ … Spirit check TN 7 Ob 1"; "TK +1 … Certainty −1" | Varfell — The Private Collection | unique | — |
| N-259 | Economic Leverage "Guild Favour ≥ 5 … (1–7 territory track)"; "1 Wealth + 1 Prosperity / 1 Wealth for 1 season / Guild Favour −1" | Guilds — Economic Leverage | unique | — |
| N-260 | Community Weaving (superseded) "Thread Tension ÷ 20 (round up) … TS 30+ … −2 / −1 / … −1 / … +1"; PP-195 (superseded) "TN 7, Ob 3 … MS +2 / +1 / +0 / +0 PS −1" | Restoration Movement — Community Weaving | RM | X-28 |
| N-261 | "Graduated Autonomy reaching 4"; "Church Influence reaches 40"; "3–2 or lower"; "2+ territories"; Martial Law "TN 7, Ob 2"; removal "Ob = Löwenritter Military ÷ 2, round up, min Ob 3 … below 40" | Löwenritter — Martial Law / Coup Trigger | coup | X-14, X-54 |
| N-262 | "+1 L/season … +1 PS/season … Stability ≥ 2" | Mandate Recovery | recovery | — |
| N-263 | "Wealth above 5 … +1D … (max +2D …)" | Hafenmark Wealth Sink | wealth | — |
| N-264 | "Military −1 … Cap: −2 per season"; "±2/season … starting value +1" | Military Stat Change / Seasonal Cap | military | — |
| N-265 | "L ≥ 4" (Institutional Mandate); "+1D on one Domain Action per season" (PC embedding) | Institutional Mandate / PC Faction Embedding | mandate | — |
| N-266 | "MS=0 AND IP≥80" | Simultaneous Catastrophe Rule | ordering | — |
| N-267 | "Church Influence ≥ 40 … +1 Ob … below 40" | Reformed Settlement Standing Effect | RDT | — |
| N-268 | Vossen "TS 0, Charisma 5+, Circles 3+" | Restoration Movement — Named NPCs | NPC | X-63 |
| N-269 | Crown covert "+1 Ob" | PP-236 | covert | X-11 |
| N-270 | Public Instability "0–10 … 5 … +1 … +1 … CI > 40 … −1 … Threshold 8 … Threshold 10" | PP-237 | clock | X-53 |
| N-271 | Scene→Mass "−1 Ob / no modifier / +1 Ob / +2 Ob" | PP-244 | hybrid | — |
| N-272 | "±2 cap applied at accounting" | PP-242 | cap | — |
| N-273 | "Contest at Piety Track 5" | PP-246 | contest | U-23 |
| N-274 | "±5/season … ±3 DA sub-cap" | PP-254 | CI cap | — |
| N-275 | "Range 0–10. Start 5. … PS < 3 … PI ≥ 8 … Stability ≤ 3 … Ob 2 … PS −1 … PI = 10"; "Stability +1 … PI increase cap +2/season" | PP-255 / ED-174 / PP-281 | Public Instability | X-32, X-53 |

### 4.28 `faction_behavior_v30.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-276 | "institutional_culture: <-0.2..+0.2>"; "cascade_fidelity: <-1..+1>"; "strictness: <0..1>"; "mandate: <0..7> … K=6" | §2 | schema | X-10 |
| N-277 | mission_alignment "−1 / +1 / 0"; "≥4 consecutive seasons" | §3.1 | mission | — |
| N-278 | orphan "α = 1.0"; "magnitude < 0.1"; "effective = α × personal + (1 − α) × supervisor"; "α_base 0.4; α_seniority -0.2 to +0.4 (Standing 1: -0.2; Standing 7: +0.4); α_institution -0.2 to +0.2 (Hafenmark = -0.2 …; Crown = 0; Restoration = +0.1; Lowenritter = -0.1)"; "drift_coef = 0.6"; "leader.scars >= 3" | §3.2 | cascade | — |
| N-279 | role templates: sovereign "0.30, 0.30, 0.20, 0.10, 0.10"; ecclesiastical "0.40, 0.20, 0.20, 0.10, 0.10"; mercantile-procedural "0.35, 0.25, 0.20, 0.10, 0.10"; intelligence-diplomatic "0.30, 0.30, 0.20, 0.10, 0.10"; reformist "0.30, 0.25, 0.20, 0.15, 0.10"; military-order "0.30, 0.25, 0.15, 0.15, 0.15"; "Range [-1, +1]" | §3.3 | expectation | X-60 |
| N-280 | "ΔPopular_Support = α × attributed + β × fidelity × gate + γ × shock"; "attributed_outcome = raw_outcome × (1 − 0.5 × max(0, leader.self_other_orientation))"; "gate ∈ {0.5, 1.0}"; "α + β = 1"; "γ … default 0.5"; "0.1 × strain_delta, -1, +1" | §3.4 | PS | U-14 |
| N-281 | "λ_continuity = 0.05, λ_procedural = 0.3, λ_expectation = 0.1, λ_violation = 0.6"; events "+1 / +1 / +0.5 / +1 / +0.5"; violations "+1 / +1 / +2 / +1 (magnitude == 3) / +0.5/season (≥4 consecutive seasons)" | §3.5 | Legitimacy | — |
| N-282 | "strictness = clamp(base_strictness + 0.5 × (L/7) − 0.3 × (PS/7), 0, 1) … base_strictness = 0.4"; table "0.4 / 0.7 / 0.2 / 0.4" | §3.6 | strictness | — |
| N-283 | "sign × strictness × {1, 2}"; "clamp(Ob_modifier, -2, +2) … (was ±3)"; "≥0.5 rounds to ±1; ≥1.5 rounds to ±2" | §3.7 | DA Ob | X-37 |
| N-284 | "L < 2 = collapse zone"; "λ_violation × 0.5/season" | §3.9, §5.1 | edge cases | U-14 |
| N-285 | "Mandate = clamp(round(7 · T / (T + K)), 0, 7) … K = 6" | §4 | Mandate | X-10 |

### 4.29 `player_agency_v30 (3).md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-286 | "14 combat actions, 6 fieldwork actions, 7 Thread operations, 4 contest styles"; "3–5 scene actions per season" | §0, §1.5 | inventory | — |
| N-287 | "Three strains on one Conviction"; "Three Convictions"; "+1 Momentum"; "+2 Momentum"; states "+2 / +1 / +2 / No"; "≥ 2 scene actions"; "at least 2 of 3" | §2 | Convictions | — |
| N-288 | "Standing ≥ 1"; "Standing 2 … 3 … 4 (+1 scene action) … 5 … 6 (+2 scene actions) … 7"; "Standing −1, floor-protected above Standing 1"; "Standing +2" | §3 | Duties | X-22 |
| N-289 | "3–5 per season"; "1 scene action per province traversed"; mandatory list of 4; ordering 1–8; Witness "Ob 1"; Step 2 "within 2 adjacencies … Accord ≤ 1 … Scar count ≥ 2 … Disposition ≥ +1 / ≥ +2"; 2b "MS ≤ 20 … Max 1"; Step 3 "1–2"; Step 4 "~25 … Maximum 3"; Step 5 "≥ +2 … ≤ −2 … Disposition −1, +1 Exposure"; Step 6 "1–2 … MS ≤ 60"; Step 7 "1" | §4.2 | Scene Slate | — |
| N-290 | "Normal: 5–7 … 4 scene actions"; "Hard: 7–9 … 3"; "Narrative: 4–5 … 5" | §4.3, §6.1 | budget | — |
| N-291 | unpursued "Standing −1"; "Disposition −1 if … ≥ +3"; "Disposition −1 … +1 Exposure" | §4.5 | consequences | — |
| N-292 | ladder "0 … 7"; "Standing 5–6 … SUC-01 through SUC-03"; "Standing 4+ … leadership challenge … Standing drops to 2, Disposition … −4" | §5.1–§5.2 | stature | X-22 |
| N-293 | "Standing (0–5) … Renown (0–10)"; sources "+1" ×8; "Cap: +2 Renown per season"; "Renown −1 (cap: −2/season)"; "Standing ≥ 3"; effects "3+ … +1 / 5+ +1D / 7+ floor(Renown ÷ 2) / 9+" | §5.4 | Renown | X-22, X-23 |
| N-294 | modifiers "Standing 4–5 +1; 6–7 +2; Knot +1; Stamina 0 −1; 2+ Wounds −1"; "1–3 mechanical interactions"; "2 scene actions" | §6 | budget | faction_politics §9.2 (same) |
| N-295 | "4-faction × 3-caste"; "Starting Standing = 0" | §7.1 | creation | — |
| N-296 | Resources "0–5. Cap: 5"; starting "2 / 3 / 2 / 2 / 1 / 1"; sources "+1/season at Standing 2+, +2 at Standing 4+ … +1/season per settlement with Prosperity ≥ 3 … +1 to +3 … +1 … +1"; uses "1 / 1 / 2 / 2 / 3 / 1 / 3" | §9 | Resources | N-111 |
| N-297 | "Renown inherited: floor(predecessor ÷ 2)"; "allies (+3) start at +1; enemies (−2) start at −1"; "+1D on first Connect" | §10 | legacy | X-23 |
| N-298 | "Skills at 60% … 1 Close Knot (Disposition −2) … Disposition ≥ +3"; "WR at half (rounded down) … WR ≥ 2 … Evidence Track threshold 3" | §11 | lineage | X-23 |

### 4.30 `faction_politics_v30.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-299 | "0–100" CI; "eight-position ladder (Standing 0 through Standing 7)"; "Standing 2–4" rival; "+1D on one specified roll per season … Disposition ≥ 0" | Glossary, §1.0 | ladder | X-22 |
| N-300 | demotion "one rank"; "drop 2 ranks, minimum Standing 1"; "drop 2 ranks; if rank 5+, drop to Standing 3"; "drop 3 ranks or to Standing 1"; "Standing drops to **−1**"; "within 1 season"; appeal "within 2 seasons" | §1.0a | demotion | — |
| N-301 | Crown ladder: Std 0 "Disposition ≥ +1 … within 2 seasons"; Std 1 "1 supply requisition/season"; Std 2 "2 Duties … 1 information relay/season … stipend 1 Wealth/year-arc … Disposition −3 … 3 consecutive"; Std 3 "Ob +1 … 1 season … once per year-arc … Ob 3"; Std 4 "2 … Renown +2 … +1 scene action … 2 NPC officers … two court audiences … Renown ≥ 3 … 2 personal retainers … 2+ consecutive … Renown … ≤ 1"; Std 5 "3 … +1 Legitimizing Authority token … 4 retainers … Ob +1 … two consecutive"; Std 6 "all 5 … ≥ 0 … one Ministry per year-arc … 3 of 5 ≥ 0 … 2 of 4 seasons … 8+ retainers … 3 of 5 … below 0 … Renown damage ≥ −3"; Std 7 "3-of-5 … within 2 seasons … Disposition ≤ 0" | §1.1 | Crown ladder | — |
| N-302 | Banner "+1D … Intimidate; −1D … Subterfuge"; branch switch "demotion to Standing 3"; inner circle Certainty "4 / 5 / 3 / 5 / 4"; Dispositions "−1 / +1 / −1 / −2" | §1.1b–§1.1d | Crown | — |
| N-303 | Hafenmark ladder: Std 0 "1 year-arc … 3 seasons"; Std 1 "2 summons"; Std 2 "2 … Ob 2 … 3 sitting Burghers … 1 query/season … Wealth ≥ 1 … 4 other Burghers … Wealth 0 for 2 consecutive seasons"; Std 3 "2/3 supermajority … +1D on Pacify … 2 Wealth/year-arc … 2/3 … Renown −2"; Std 4 "3 … +1 scene action … Standing −1 … 2 of 4 seasons … 4+ other Parliamentarians"; Std 5 "3 … 2 motions … 2 consecutive sessions"; Std 6 "all 4 … two Parliamentary Committees … 2 consecutive sessions … falls to 5 … 10+ … 2/3 … −2"; Std 7 "15+ … −2" | §1.2 | Hafenmark ladder | — |
| N-304 | Varfell ladder: Std 0 "one night … 2 seasons"; Std 1 "within 1 season"; Std 2 "2 … unit of 2 … 3 armed retainers … 1 military action per year-arc … 2 consecutive year-arcs"; Std 3 "3 … Exceeding … +1 within 2 year-arcs … 0 for 2 consecutive seasons"; Std 4 "2 year-arcs … 3 NPC officers … Ob +2 … Military ≥ 2 … 8+ … −2 margin+"; Std 5 "3 … +1 scene action … Standing −1 … Military ≥ 2 … 15+ … unanimity minus one"; Std 6 "4 year-arcs OR … 2 successful campaigns … Military ≥ 3"; Std 7 "3 of 5 at Disposition ≥ +1 … Ob +0 … Military ≥ 4 … 20+" | §1.3 | Varfell ladder | U-24 |
| N-305 | incapacity "≥ 2 seasons … 1 other Senior Jarl"; "2 consecutive Assembly sessions"; "3 consecutive sessions"; "Certainty reaches 0 AND … Scar count ≥ 3"; "Disposition −1"; "3 of 5 … Ob 2"; "minimum of 2 seasons"; "4 seasons" | §1.3a | incapacity | — |
| N-306 | Warden branch "TS ≥ 30 AND WA ≥ +1"; inner circle Certainty "5 / 4 / 5 / 3 / 4"; Edeyja "WR ≥ 3" | §1.3b–§1.3c | Varfell | X-50 |
| N-307 | Church ladder: Std 0 "1 season … Ob 1 … Disposition ≥ 0 … TS ≥ 30 … Exposure +1"; Std 1 "monthly"; Std 2 "2 … Ob 2 … PT/CV +1 … ±1/season cap … 1 free … 3 consecutive"; Std 3 "3 … TS … 30"; Std 4 "3 … Ob 2 … Mandate ±1 … Attention Pool reaching 5 … Disposition ≤ −1"; Std 5 "all 5 Prelates … AEA ≥ 3 … 2+ territories … Certainty ≤ 1"; Std 6 "2/3 supermajority … 4 year-arcs … Ob 3"; Std 7 "within 2 seasons … floor(CI/20)" | §1.4 | Church ladder | X-39 |
| N-308 | Consecration "+1 Ob … each year-arc … CI … below 30 in the preceding 3 year-arcs"; "all 5 Prelates at Disposition ≥ 0" | §1.4c | consecration | U-01 |
| N-309 | Löwenritter ladder "(S-012, S-014)"; "≥ 1 year-arc"; "2 … 3 squadrons"; "3 … up to 2 units"; "4 year-arcs"; "one of 3 Marshal positions … 6 year-arcs"; "2 Marshals" | §2.1 | Löwenritter | X-18 |
| N-310 | Riskbreaker "Intel vs Ob 2, Overwhelming required"; "Ob 2"; "3 completed … one Overwhelming"; "2 stash points"; "5 completed … 1 Operative … 3-person"; "3 successful"; "4 year-arcs"; "Mission refusal × 2" | §2.2 | Riskbreakers | — |
| N-311 | Shadow Renown "(0–10)"; sources "+1" ×6; "cap once/target/season"; "+2 … per season"; effects "3+ / 5+ / 7+ floor(Shadow Renown ÷ 2) / 9+"; "2:1 loss"; "+1 Deniability Debt"; "above the cap (10) … 1:1"; conversion "−1 public Renown … +1" | §2.2b.i | Shadow Renown | — |
| N-312 | Deniability Debt "(0–7, cap 7)"; accrual "+1 / +2 / +1 (Intel roll vs Ob 3) / +1 / +2 / +1"; reduction "−1 (… does not apply if Debt ≥ 5) / −1 (Intel vs Ob 3, once per season) / −1 (once per campaign arc) / Reset to 2"; thresholds "0–1 / 2 +1 Ob / 3 … +1 Ob / 4 … disabled / 5 … inquiry / 6 … +2 Ob on Rb-Std 1–3 / 7 … demoted by 1"; probe "Ob 3" | §2.2b.ii | Debt | X-48 |
| N-313 | Inquisitor "Std 3 … Ob 2 … within 3 seasons … 3 … +1D … 5 … Standing 4+ … 4 year-arcs … caps at Standing 5"; Templar "3 squadrons … 2 … 3 … 4 year-arcs … Standing 5"; Guild "Ob 1 … 3-year … 3+ territories … 2+ seasons … 2 year-arcs … Ob 2 … 4 year-arcs … voting weight × 2 … Standing 6"; Niflhel "2 successful runs … 5 runs … Standing 4 in two arms … 0–2 … +1D … Thread Tension +0.5 per season … above Standing 2"; Warden "TS ≥ 15 / ≥ 30 / 2 … ≥ 40 / ≥ 50 … 4 … 1 / ≥ 60 / ≥ 70 … 6 year-arcs / 7" | §2.3–§2.7 | sub-ladders | X-38 |
| N-314 | caste gates "Std 3→4 … Std 5→6 … ~3 Disposition"; "+1 Ob"; "halved (round down)"; Initiation Obs "2 / 3" ×6 (Varfell "2 … possibly Ob 1"); Disposition floors table (−2 … +1); "Central … +1 … Northern … +2" | §3.2–§3.5 | caste | — |
| N-315 | "at least one NPC at Standing ≥ 2 … or 3+ NPCs"; "TN 7 Ob 1 … Ob 2"; "1-season … 2 seasons"; "margin reduced by 2 … minimum 0"; "3+ … 4 consecutive seasons"; "Spirit pool, TN 7, Ob 3"; "Renown +1 … −1"; "half value"; "(5/5/5)"; "drops 1 rank"; "2 seasons" | §3.6 | caste-transgressive | U-24 |
| N-316 | "CV … Range 0–5"; "max(0, 3 − PT)"; "SW … Range 0–5"; "489 lines … 6,095 char … 40,000+ char" | §4.2 | terminology | X-05 |
| N-317 | CI×rank bands "0–39 / 40–64 / 65–99 / 100"; "+1D … +1D … +1D … +2D … double-penalty … +1D"; "CI 55+ … CI 80+"; "Prosperity ≤ 3"; "floor(CI/30) … −2 … −3"; "CI 40+ … +1 Ob … CI 65+" | §5 | CI×rank | X-61 |
| N-318 | "Mandate ≈ PI/2"; "PP-487 PI < 4"; Dispositions "+0 … +1"; "≥ 0 … Std 3 … within 1 season"; "Church Stability drops to 0"; "+1 Ob harder"; "two Prelates … College vote Ob 3"; "2 Prelates' concurrence"; ceremony "Crown Std 5 … first of 5 Dispositions … Crown Std 2 … Chancellor (Std 6)" | §6 | Baralta×rank | N-215 |
| N-319 | Hochschule "Seasonal cost 1 Wealth"; committees "0 / 1 Wealth/season / 1 Wealth / 1 Wealth / 0 / 1 Wealth"; "Competence (0–3) and Corruption (0–3)"; "Hafenmark Std 2+"; councils "Readiness Track (0–3) … 0 … 3" | §7 | ministries | X-41 |
| N-320 | "10 years … 40 seasons … ~S14–S20"; triggers "≥ 24 (6 year-arcs) … Readiness ≥ 5 … Max +2 Readiness per year-arc … Crown Stability ≤ 1 … Almud's death"; outcomes "+3 … Stability +1 / +1 to +2 … −0 / 0 … −1 / −1 to −2 … −2 / −3 … −3"; "Readiness Track (0–10) … Readiness ≥ 7 … Crown Std 5+ … Std 7 … ≥ +2" | §8 | generational | X-49 |
| N-321 | parity "Std 4 +1 / Std 5 +1 / Std 6 +2 / Std 7 +2"; "1 Task/season … 1 NPC officer … 2 NPC officers" | §9.2 | parity | N-294 |
| N-322 | "3 of 5 Prelates are canonical … 2 need naming"; "25 editorial items and 5 SIM-DEBT"; "Std 5 by S14 and Std 7 by S20" | §10 | editorial | — |

### 4.31 `governance_play_redesign_v1.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-323 | "AP = 2 + FacilityTier_s … 0–3 → 2–5 AP/season … Standing 5 … +1"; "Companion-governors … 2 AP" | §1.1–§1.2 | AP | — |
| N-324 | verbs "Develop 2 … ⌊Prosperity/2⌋+1 … Prosperity +1"; "Fortify 2 … ⌊Defense/2⌋+1 … Defense +1"; "Keep Order 1–2 … Consent 2 AP … PS +1 … Force 1 AP … PS −1 … Disposition −1 … Clergy 1 AP … Order +1"; "Hold Court 1 … +1/−1 Ob"; "Sponsor 1–2 … +1 … Disposition −2"; "Treat 1"; "Levy 1 … −1 … −1"; "Investigate 1–2"; "Petition / Defy … 0 AP" | §1.3 | verbs | N-147 |
| N-325 | Directive responses "Standing +, trust +"; "suspicion track +1" | §1.4 | directive | U-02 |
| N-326 | Precedent "±1 Ob" | §1.6 | ledger | — |
| N-327 | "Π (0–10)"; formula (U-02); bands "0–2 / 3–7 / 8–10"; draw "1 + ⌊Π/3⌋ … (1 … up to 4)"; card "cooldown: 2 … pressure_if_ignored: +2 … Π −2 … PS -1 … Disp -2 … Π +1 … Π +2" | §2 | deck | U-02 |
| N-328 | dossier "convictions: [1-2] … progress: 0-5 … timeline: 4, progress: 1 … Disposition < -2"; "advances their ambition by 1" | §3 | NPCs | — |
| N-329 | example "Π=4 … Standing-debt +1, suspicion +1 … Disp +2, PS +1 … Π −2" | §4.4 | worked | — |
| N-330 | "~8–12 per family … ≈ 60–100 base cards" | §5.3 | authoring | — |

### 4.32 `strategic_layer_v30.md`

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-331 | Uphold/Appease "Mandate ≥ 4 … Mandate −1 … Mandate ≥ 4 AND Stability ≤ 3" | Institutional Mandate | mandate | N-051 (L) |
| N-332 | "7-10 = success; 10 = bonus success; 1 = remove one success"; "Ob minimum = 1" | Transition Document / CORRECTION 1–2 | dice | N-004 |
| N-333 | "P-15: … Standing: Cannot exceed 5"; "P-14: … Reputation: Cannot exceed 5" | CORRECTION 1 | caps | X-22 |
| N-334 | probability table "2 0.80 ~58% ~22% ~5% / 3 1.20 ~74% ~40% ~15% / 4 1.60 ~85% ~56% ~27% / 5 2.00 ~91% ~69% ~42% / 6 2.40 ~95% ~80% ~57% / 7 2.80 ~97% ~88% ~69%"; "P(success-or-bonus)=0.40, P(subtraction)=0.10, P(neutral)=0.50"; "56-69% … 60-74% … 74-97% … 15-42%" | Probability summary | dice | — |
| N-335 | "P-29: … +1 Mending Stability per successful Weave … (max +2/season …) … TS ≥ 20"; "P-23: … 80+ … Ob 2 … maximum 2 territory transfers per seizure event per faction"; "P-18: … cannot exceed current Military stat" | CORRECTION 2 | misc | X-05, X-06 |
| N-336 | "Ob = ceil((100−MS)/20) min 1, −1 per Presence marker … At MS 72 (start): Ob 2"; Policy Instrument "Mandate ≥ 4"; P-21 "Muster 2 … −1 in T2 … −1 in T11; March 2 … +1 in T8; Govern 2 … −1 in own capital" | CORRECTION 2 | Obs | X-20, X-28 |
| N-337 | degree table "Ob + 1 … = Ob … Ob − 1 … 0 … Negative" | CORRECTION 3 | degrees | X-02 |
| N-338 | "P-12: … more 1s than … 7–10 … Critical Failure" (later "struck") | I-01 | dice | X-02 |
| N-339 | "P-15: Mandate drops to 0 … freeze"; "P-20: … cannot exceed 7 … floor is 0" | I-04 | collapse | X-10 |
| N-340 | "PP-034 … Discipline −1"; "PP-647 … MS −1 (Campaign/War scale: MS −2) … IP +2, Turmoil +1 … Accord → 1 … Accord −1" | I-05 | battle | X-08 |
| N-341 | "Mending Stability ≥ 50"; "starts at 72" | I-06 | RM victory | X-01 |
| N-342 | "P-18: … alphabetical faction order" | I-07 | ties | N-056 |
| N-343 | "P-22: … Prosperity value (0–5) … Prosperity ≥ 3 generates +1 Wealth" | G-02 | Prosperity | X-44 |
| N-344 | G-06 Forgetting "Influence + 1D per Presence marker in T13 … Ob 1 … OR Intelligence stat … OR Wealth ÷ 2 rounded up"; "Thread Sensitivity ÷ 10" | G-06 | forgetting | X-30 |
| N-345 | "pool of 4 at Ob 1 = ~85%" | G-08 | RM | — |
| N-346 | "standard Muster = Ob 2 … Military 4 vs Ob 2" | G-09 | Muster | — |
| N-347 | "Mandate 3, Wealth 3 … Mandate 4, Wealth 4" | G-10 | Varfell | X-13 |
| N-348 | G-11 "0 … +1 … −3/season while" (truncated); "Church Influence > 60 → Institutional Pressure +1/season" | G-11 | IP | U-27 |
| N-349 | Cascade Test 1 "Season 7, Church Influence 36 … Base Ob 2 − 1 − 1 = Ob 1 … 5d10 … 3 net … Attention Pool ≥ 3 … +0.5 … AER +1 … 76→80"; Test 2 "RDT 5, Season 12 … +3 … 52 + 1 … + 3 = 56 … RDT 6 … Appease count … 2 … 3 − 1 = 2 … Path A requires 3"; Test 3 "MS 38 … −1 Ob … Ob 1 … 4d10 … +1 … −3 … 37 … +2"; Test 4 "CI 80 … Ob 3 … Ob 2 … 5 territories … CI +2 … Public Instability −1"; "P-25: 1 personal Wound = Coherence Rating −1 (minimum … 1)" | PART FIVE | worked | X-16, X-39 |
| N-350 | Scenario A "Season 9 … CI 38, MS 48 … +1D … 0 Wealth … CI +1 … Ob 2 … 4d10 … CI −1 … Ob 2 … Stability −1. AER −1. CI −2 … Renown −1 … +1 (now 2) … CI −2 … Stability −1 … Cooperation 2 instead of 3"; Scenario B "Season 14 … Player Character 6 … 6 consecutive seasons … Mandate 3, Military 4, VTM 4 … VTM maximum (7) … +2D … Ob 2 … +1D … −1 Ob = Ob 1 … 5d10 … (Mandate 2, Influence 4, Wealth 2, Stability 3) … +1D … 2 seasons"; Scenario C "Season 11, IP 68 … threshold 75; AER 3 … 80 … Loyalty 4 … Loyalty 1 … Public Instability 4 … Ob 2 … Wealth 5 vs Ob 2 + 1 = Ob 3 … Military 6 vs Ob 2 … 6d10 … Loyalty +1 (now 5) … < 60 … 70 … 5 more seasons (10 points … +2/season) … 72 … 74 … 76 … Military 6 vs Vanguard Military 5, Discipline 5 … +2D … 8 dice … Fort 2: +2D … 7 dice … Discipline −2 … 6 net vs 2 net … −5 … 76 → 71 … AER −1 … CI = 55" | PART SIX | worked | X-15, X-16, X-36, X-39 |
| N-351 | "−1/year baseline … 20-season game … ~5 points" | PART SEVEN | MS | — |
| N-352 | "Starting Church Influence 22. Target Church Influence 70. Gap: 48"; "+1/season"; "+1/season from Season ~14+"; "+0.5–1.5/season"; "Mandate ≥ 4 passive: −1/season … ~1/season … ~2/season … Season 35–45"; "+0.5" | PART EIGHT | pace | N-052 (28/65) |
| N-353 | "Crown 22 … Wealth only 4; Church 25 … Influence 6; Hafenmark 20 … Military 3; Varfell 18 … Mandate 3, Wealth 3; Restoration 11 … Military 0, Mandate 2; Löwenritter 19 … Military 6, Influence 2, Mandate 3" | Starting Stat Assessment | stats | X-12, X-13, X-36 |
| N-354 | "90–150 minutes"; "1 real-world session per in-game season" | §9.1 | hybrid | — |
| N-355 | fog "In ruins 1 / Poor 2–3 / Good 4–5 / Excellent 6–7" | §9.2 | fog | — |
| N-356 | "2× rolled net successes … Wealth −1"; "(2×−1 variant … rejected)" | §9.7 | resources | U-27 |
| N-357 | "5 Steps"; "loses 1 Stability, 1 Mandate"; "Ob 4, multi-season"; "1 directive per season"; "MS < 30" | §9.8–§9.15 | hybrid | X-26 |

### 4.33 `early_game_ignition_analysis.md` (SUPERSEDED per its own header; listed for provenance)

| id | value | heading | governs | xref |
|---|---|---|---|---|
| N-358 | "CI grows at +5/season. MS decays at −1 per battle"; "Crown holds 14 PV" | §1 | (superseded) | X-29 |
| N-359 | "Military 6 (post-coup)"; "3 tokens per year"; "30% abort rate"; "Torben starts at Loyalty 7" | §2 | (superseded) | X-12 |
| N-360 | "8 Tension Cards … 2 are drawn"; cards: T1 "Loyalty starts at 3 … Coup Counter +1 at S4"; T2 "Prosperity drops to 2 (from 5) … +1D … 4 seasons"; T3 "AER −1 … Mandate −1"; T4 "within 3 seasons, Coup Counter +1 … Accord −1"; T5 "Stability −2 … within 4 seasons"; T6 "by Season 8, or IP +10 … Loyalty drops to 1 … +1 CI"; T7 "Accord … drops by 1 … RM Popular Will +1 … +1D … 4 seasons … CI +1"; T8 "Mandate check (Ob 1) at S2 … Coup Counter +1 … +0.5"; "28 possible combinations"; "3–4 seasons" | §4.1 | (superseded) | X-34 |
| N-361 | Niflhel "3 consecutive seasons … +2 or −2"; Löwenritter "4 consecutive seasons AND Coup Counter < 3 … +0.5 … Strain +1 … 2 seasons" | §4.2–§4.3 | (superseded) | X-38 |
| N-362 | "C(8,2) = 28"; "12 cards … C(12,2)=66"; "S4, S8, S12"; "Stability ≤ 3 … ≤ 2" | §6–§9 | (superseded) | — |

---

## 5. Summary

**Counts.** Contradictions: **67** (X-01…X-67; Tier A 33, Tier B 29, Tier C 5 — X-63…X-67, with X-66 recording a structural risk rather than a present clash). Underspecification: **30** entries (U-01…U-30), of which U-01 bundles 14 distinct referee delegations and U-18 bundles 15 undefined-but-cited mechanics. Dangling references: **23** target groups (R-01…R-23) plus a within-corpus set; roughly 190 `PP-` and 150 `ED-` identifiers, ~60 named documents/paths, and ~40 register codes resolve to nothing in the corpus. Numbers: **362** rows (N-001…N-362), 41 of which cross-reference a contradiction.

**Ten highest-consequence findings.**
1. X-01 — "control 11+ of 15 territories" (GD-1) vs "all 15 territories at Accord ≥ 2" vs five surviving faction-specific victory conditions: the engine has no single win predicate.
2. X-04/X-02/X-03 — faction checks are simultaneously "deterministic+stochastic resolver … canonical" and d10 pools, with two degree ladders (2×Ob-and-≥3 vs Ob+1) and two TNs (7, 8).
3. X-05/X-06/X-07 — Church seizure has six Ob formulas, three triggers (CI 60 probabilistic, CI 100 deterministic, CI 75/80 threshold) and a ceiling that is both 100 and frozen at 75.
4. X-10 — Mandate is both a stored faction stat that rules decrement and a derived saturating aggregate `clamp(round(7·T/(T+K)))` of per-settlement L/PS; every "Mandate ±N" rule is unevaluable under the latter.
5. X-08/X-09 — battle → MS/IP/Turmoil is per-battle and per-season, scale-flat and scale-doubled, and IP/Turmoil-from-battle is both struck (ED-743) and live in the Accounting steps; Turmoil decay has two predicates.
6. X-16/X-17/X-18 — three incompatible territory numberings, the Ministry running in T13 instead of T1, and a settlement registry that renumbered S-IDs while rules still cite the old ones (S-014 Barracks is now S-014 Ehrenfeld; S-015 Parliament is now S-015 Nordhain).
7. X-29 — three PV tables (total 40 vs 33; Crown 16 vs 14 vs 12) under a PV-based victory condition.
8. X-11/X-12 — the stat schema is 5, 6 or 7 stats; Crown Military is 4, 5 or "5/6"; Löwenritter Military 5 or 6; Crown both has and has no Intel.
9. U-12 — no document gives starting Prosperity/Defense/Order for any settlement, yet Accord, Treasury, settlement Weight and (after X-10) Mandate all derive from them; and R-01…R-05 — the seizure infrastructure table, the Parliament tally, the battle engine and every march-layer cost live in absent files.
10. X-14/X-15/X-38 — the Coup Counter, VTM and Niflhel are each struck in one place and load-bearing in five others (autonomy threshold 3 vs 4 vs stages; expedition/Path-B gates on VTM; a full Niflhel ladder and settlement rules).

Output file: `/tmp/claude-0/-home-user-ttrpg/1d0e9e01-2d37-533d-88c0-943d2e937e83/scratchpad/out/B_independent_contradictions.md`
