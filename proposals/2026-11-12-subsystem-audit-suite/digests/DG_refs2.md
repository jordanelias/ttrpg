# Digest refs2

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane refs2: `references/` registries and ledgers (nine files). Read in full by the digest lane on 2026-11-12. Entries in assignment order. The first entry (the restructure ledger) is written last because it is 704 KB; a placeholder stands until it is filled.

### references/restructure_ledger.md
- **What it is:** PLACEHOLDER (to be filled once the ledger is fully read).
- **Status:** pending.
- **Bears on:** PROCESS.
- **Content that matters:** pending.
- **Conflicts / stale:** pending.
- **Open items:** pending.

### references/scope_vocabulary.md
- **What it is:** process reference, written 2026-05-31 (Lane B, roadmap 5.8 / decision D6), corrected 2026-08-01 (ED-IN-0119); a register of the three scope/type vocabularies (commit scopes, session scopes, task types) and the union of them.
- **Status:** "unified-vocabulary established (D6, partial — single source + drift guard done; the ~10 reduction is proposed, not executed)" (:2). Reading: historical; only the COMMIT row is live, and its advertised drift guard does not exist (see Conflicts).
- **Bears on:** PROCESS.
- **Content that matters:**
  - Commit scopes are the only live axis: editorial, patch, simulation, compilation, infrastructure, skill, cleanup, godot, phase, fix, bugfix, design (12), authority `CLAUDE.md` §2 (:12). This matches CLAUDE.md §2 as read today.
  - Session scopes (`github_ops.SESSION_SCOPES`, 7) and task types (`valoria_hooks.TASK_REQUIRED_FILES`, 10) were retired with the orchestrator; kept as "historical record, not live vocabularies" (:16).
  - The 17-member "union" (:25-33) and a proposed reduction to ~10 (:37-43) are both inert: a union over two dead vocabularies.
  - Migration discipline says change `CLAUDE.md` §2 and this doc in the same commit and re-run the test (:45-48).
- **Conflicts / stale:** Names `tests/valoria/test_scope_vocabulary.py` as the drift guard (:3, :48). That file does not exist (`ls tests/valoria` shows only `test_front_fixer_scope.py` and `test_vocab_store.py`; grep of `tests/`, `tools/`, `.githooks/`, `.github/` for `scope_vocabulary` returns nothing). The ED-IN-0119 correction at :4 retired the earlier `tests/hooks/` test, and the replacement it promises was either never written or since removed. So the sentence "the test enforces it" (:7) is false today. `valoria_hooks` (no module in the tree) and `github_ops` are retired. The 17-set and the "reduction to ~10" are dead decisions. [Related ledger rows, `restructure_ledger.md`, also mention this file.]
- **Open items:** D6 reduction "REQUIRES JORDAN DECISION" (:37) but the vocabularies it would reduce are gone; the row answers itself as irrelevant (CLAUDE.md §0 ladder step 2).

### references/silo_overlap_matrix.yaml
- **What it is:** data file (YAML), extracted 2026-05-10 from `references/mechanical_terms_index.md` §2; a list of 55 terms that appear in two or more vocabulary silos, each with a keep/rename verdict.
- **Status:** `disposition: "RATIFIED 2026-07-08 (ED-IN-0029 docket, OPT-AV-14): permanent historical snapshot, no live regeneration path."` (:4). Reading: historical, deliberately frozen.
- **Bears on:** PROCESS, CHAR (attribute words), FA, WR.
- **Content that matters:**
  - Shape: `entries[]` with `word`, `silos_where_it_appears`, `verdict_+_rationale` (:8-202). `total_entries: 55` (:6) but the list has about 62 rows including duplicates (Pool appears twice, Standing twice, the 'Conviction Track' row struck out twice) and stray header rows ("Word / Silos / Problem" at :48, "Attribute word (§1) / Used as mechanic in / Verdict" at :89, :114, :146, "Word / Silos / Note" at :167): the count is wrong and header rows were ingested as data.
  - Verdicts rename: Conviction Track to Piety Track (territory) and Persuasion Track (contest) (:23-26); Pressure Point type "Authority" to "Sanction" (:57-62); mass-combat Strength to Size (PP-232) (:92-95); "Cardinal" structural frame recommended renamed "Four-Virtue Structure" (:51-56).
  - Core-attribute inputs named: Strength, Agility, Endurance, Presence, Cognition, Spirit, Attunement as stat-to-pool drivers (:92-113) (seven names; the 9-attribute roster in `descriptor_registry.yaml` is the live one, see `vocab_history.md` alias note).
  - Recommends collapsing "Mandate Pool" to `faction_pool`/`political_pool` (:117-122).
- **Conflicts / stale:** `Key` and "Standing change Key type" (:45-47, :143-145) refer to the retired Key substrate (ED-IN-0232). "Thread Pool", "Domain Echo", "Knot" are listed as keep; Domain Echo and Knot may not exist as engine terms [UNVERIFIED]. The only code mention of this file is a comment in `skills/valoria-vector-audit/scripts/vector_audit.py:1131` (calls it a frozen snapshot); nothing loads it at runtime. `vocab_history.md` confirms it was left whole as ratified frozen data.
- **Open items:** none that anything tracks; the "recommend rename" verdicts (Cardinal, Mandate Pool) are unactioned recommendations in a frozen file.

### references/synonym_registry.yaml
- **What it is:** generated data (YAML) from `tools/vocab_store.py --build` over `references/definitions/vocab_source.yaml` (key `registers.synonym_registry`); 20 canonical-vs-alias rows extracted 2026-05-10.
- **Status:** header "GENERATED ... DO NOT EDIT BY HAND (ED-IN-0078, Phase 3 vocab fold)" (:1-2). Reading: live as a generated view of the vocabulary store, read by the naming checks as an exempt file; its content is old.
- **Bears on:** PROCESS, WR (names), MB (stat names), FA.
- **Content that matters:**
  - Readers: `tools/vocab_store.py:43` (builds it), `tools/ci_naming_check.py:104` and `tools/validate_ed_citations.py:108` (both exempt it from scanning because it lists legacy synonyms by design). No engine reader.
  - Mass-combat stats: Size (was Strength), Power (was Combat Power/CP), Discipline (was Cohesion), Command (was Command Rating) (:17-32). CP is locked to Character Points (ED-136).
  - World clock: Mending Stability (MS) canonical, Rendering Stability (RS) retained only in canon/02 annotations (:9-12); Church Influence (CI) over Theocracy Counter (TC) (:13-16).
  - 13 Convictions (PP-684) replace Categorical Imperative/Virtue/Faith/Scholastic/Equity/Honor/Reason/Continuity (:58-62).
  - Piety Track (PT) is the single per-territory orthodoxy track, range 0-5, same as Conviction Track CT/CV (ED-644) (:79-87).
  - "Engine Setup / Resolution" over "GM Setup / Resolution" (:63-66).
- **Conflicts / stale:** Two rows canonicalise **Key** ("Substrate event-record, canonical **Key**", PP-687) and "Memory entry" (:33-40): the Key substrate is RETIRED (ED-IN-0232), so these rows now canonicalise a deleted concept. Rows :84-87 are struck-through (a resolved duplication) and are carried as data inside a generated file. "Mass Seizure ... CI ≥ 60" (:88-91) is a number from prose-era design; no code owner named here [UNVERIFIED against `engine/season/`]. `total_entries: 20` but 21 rows are present counting the struck row.
- **Open items:** none.

### references/throughlines_meta.md
- **What it is:** design/process reference (SKELETON), PP-672 (2026-04-19) with PP-674 tier N added; the "Valoria Throughlines Framework — Canonical Vetting Guide": a tiered rubric (N, Ω, Μ, М, Τ, Q, Μ̄) for vetting proposals.
- **Status:** no Status line; comment headers cite PP-672/PP-674/ED-717 (:1-6). Reading: live as reference for vetting; its enforcement claims are partly stale.
- **Bears on:** PROCESS, WR, FA (М-4 institutional postures), GO (Μ̄ translation).
- **Content that matters:**
  - Tier order N (necessity, Renaissance-leadership grounding) → Ω (intent: cross-scale consequence, personal transformation, autonomous agents, non-dominance) → Μ (4 modes α pressure, β agent composition, γ substrate ontology, δ cross-scale) → М (11 meta-throughlines) → Τ (25 throughlines per `throughlines_complete.md`) → Q (robust/smooth/elegant) (:22-141).
  - Authority: Jordan owns N, Ω, Μ; Claude flags N/Ω failure and never rejects unilaterally (:14, :39, :55, :292-300).
  - Scope classes A-E decide which tiers run (:183-189). Failure Lexicon of 15 terms (:155-173). Test battery: pass PP-666 settlement adjacency, Hafenmark food vulnerability; fail 10-season peace treaty, caravan minigame, Standing-7 boost, reskinned Hafenmark (:244-248).
  - §8.2-A subtractive verdict ladder KEEP→REFINE→DISTILL→MERGE→PRUNE→CUT, judged "as-if-built, never by build state" (:201-238, ED-IN-0027).
  - Q-robust includes "dramatic legibility": a designer can read game state and say whose position is at risk, what each actor wants, what happens if no one acts (:122).
- **Conflicts / stale:** Enforcement is described as `valoria_hooks.vetting_gate` (:16, :275); `valoria_hooks` no longer exists. The live port is `tools/ci_vetting_check.py` (entries with id < PP-674 grandfathered). "Strategic clock is real-time" (:148) conflicts with the season-loop design (seasonal ticks, no real-time clock) [UNVERIFIED but CLAUDE.md and the season loop are turn-based]. "41 throughlines" (:78) vs "25" (§4 :106): both counts appear; infill says 40 of 41. "Applies to work after adoption" with grandfathering (:12) so older canon is exempt. Dual vocabulary with CLAUDE.md §0.06 NERS: this is an earlier, different quality rubric (Q-robust/smooth/elegant) and the two coexist; no cross-reference. Test battery and cited `designs/audit/2026-07-08-pessimist-action-audit/` (:238) point to the dissolved `designs/` tree.
- **Open items:** Μ̄ section assumes Godot features (shaders, real-time clock, single save); never reconciled with the season-loop mapping (`04` §C.12).

### references/throughlines_meta_infill.md
- **What it is:** design/process reference (INFILL companion), PP-672/674/676 (2026-04-19 to 2026-04-29), ED-IN-0027 (2026-07-08); rationale, the full T→М tag table, М-7..М-11 specs, worked examples, failure-lexicon definitions, N-tier and enforcement detail.
- **Status:** no Status line; "Do not use for vetting reference; use skeleton only" (:3). Reading: live as reference only; declared load-on-demand.
- **Bears on:** PROCESS, WR, FA, CHAR (Truth/TS arc), GO.
- **Content that matters:**
  - Full T→М table T-01..T-41 (T-10 struck, T-15a/b/c added) with "load-bearing systems" column (:73-118); coverage line says primary distribution М-3: 14, М-4: 11, but the skeleton (`throughlines_meta.md:102`) quotes a different distribution (М-3: 4, М-4: 8): the two documents disagree on the counts.
  - Ω rationale: the four clauses specialise "a positive feedback loop between player decisions and mechanics that produces emergent narratives" to Valoria (:14-22).
  - Μ-γ vs Μ-δ test: a mechanic can satisfy one and violate the other (settlement Order that does not feed province Accord) (:48-56).
  - N tier: Valoria's subject is Renaissance-Italian political leadership; ten load-bearing dynamics listed (succession, excommunication, condottiere loyalty, grain politics, parliamentary blocs, assassination, financial ruin, territorial loss, Thread/heresy politics) (:445-460). N judgment belongs to Jordan alone (:479-483).
  - Worked examples: PP-666 settlement adjacency (passes), 10-season peace treaty (fails Ω-d, Ω-c), reskinned Hafenmark parliament (fails М-4) (:233-343).
  - Enforcement: `vetting:` block with class A-E, necessity, omega, mu, m_ratings, q (:522-543); a `design_proposal` task type requiring this file be loaded (:545-547).
  - §7-A: subtractive-audit rationale; in the 2026-07-08 run the inverted-critic gate "overturned 2 of 37 candidates" (:404).
- **Conflicts / stale:** `valoria_hooks.vetting_gate`, `TASK_REQUIRED_FILES` and `pre_commit_gate` (:512, :547) are retired (see scope_vocabulary). Section numbering is out of order (§3.4-§3.8 precede §3.2; §3.1 table then §3.4). "Current: 6 patterns" (:427) vs 11 М elsewhere. Cites `audit/lane-a/rigorous_audit_synthesis_s1_s7_v3_1.md` (:187), a path under the dissolved `audit/`. :428 ends in a dangling sentence fragment ("involving them defaults to 'undefined baseline'"). Settlement-Order floor-average rule cited as `settlement_layer §1.3` ED-SETT-03 (:54) [UNVERIFIED]. The "single save per campaign, real-time strategic clock" Godot rules (:353-354) are design intent, not mechanism.
- **Open items:** whether a 7th М for temporal recursion is needed (:427); retroactive canon audit left "probably after engine_v4 smoke-test" (:429), a smoke-test that no longer exists by that name.

### references/throughlines_meta_solmund_appendix.md
- **What it is:** provisional appendix (2026-04-25, Stage 4 follow-up), five Solmund throughlines T-A..T-E plus implementation priorities, extracted from `atoms_pending/2026-04-25/_consolidated/02_solmund_cultural_guide.md` PART 8, plus an audit-resolution table and nine open editorial items.
- **Status:** "[PROVISIONAL ... Pending Jordan integration into canonical throughlines_meta_infill.md table format]" (:1). Reading: unresolved since April; orphan (nothing reads it).
- **Bears on:** WR, FA (Church), CHAR (Truth, SA), FI (Seam Texts), GO.
- **Content that matters:**
  - Five placeholder throughlines: perceptual prophylaxis as literary engine; seam texts as mechanical objects (comprehension-gated by TS via P-08); double-consciousness spiral (one Mending effect read three ways by three factions); Baralta as accidental prophylaxis cracker; the Solmund repetition (miracle→institutional capture→suppression of practice) (:29-39).
  - Implementation priorities: 10-15 Seam Texts as POI content in T2 Kronmark, T9 Himmelenger, T14 Ehrenfeld; Truth baselines by controlling faction (Church 5, Varfell 3-4, Crown 4, Hafenmark 4) (:45-49); Seam Text comprehension gate as annotation layer at TS ≥ 30 in Godot (:57).
  - Proposed mechanics unratified: Miracle Investigation Ob = floor(controller SA / 2) + 1 (:78); Miraculous Event trigger; Accord +1; Proximity Rating -1; Cognition vs Ob = Truth (:90-100).
  - Nine open editorial items with the decision needed and what each blocks (:90-100).
- **Conflicts / stale:** the infill (:568-572) says the appendix is awaiting integration; the table `T-NN` sequence in the infill has since reached T-41, so numbers are unassigned. Content is "PROVISIONAL... No existing canonical files modified" (:104) yet the Truth-baseline and SA-gated numbers are hard numbers in prose, not in a registry code reads (CLAUDE.md §0.05). "Truth 6+ qualification" and "SA stat" are attribute names that may not match the current 9-attribute roster [UNVERIFIED].
- **Open items:** all nine editorial items at :90-100 are open; no later document in the tree appears to have answered them [UNVERIFIED beyond a grep for the file name].

### references/vocab_history.md
- **What it is:** process history file (2026-10-06, B-X), the supplement holding dated narrative moved out of the vocabulary-register YAML comments.
- **Status:** "Reference only: no code consumes it as a fact (CLAUDE.md §0.05)" (:4). Reading: live reference; accurate description of the family.
- **Bears on:** PROCESS, CHAR (attribute roster note).
- **Content that matters:**
  - The YAMLs are state, this file is history; new dated narrative goes here, not into YAML comments (:3, :31-32).
  - `alias_registry.yaml` and `censured_vocabulary.yaml` are generated from `references/definitions/vocab_source.yaml` `view_headers:` by `tools/vocab_store.py --build`; `proper_noun_registry.yaml` and `action_vocabulary.yaml` are hand-authored (:14-18).
  - Warning dated 2026-09-16 that `tools/valoria_collator.py` DOES NOT EXIST; the alias registry's checks are a specification only; live readers are `ci_naming_check.py` and `validate_ed_citations.py`, neither of which performs them; nothing under `engine/` or `systems/` reads the alias registry at runtime (:49-59).
  - The 7-vs-9 core-attribute split (ED-IN-0025): only the nine in `descriptor_registry.yaml` are live (read at runtime behind a blocking `--check`); the alias registry's seven are enforced by nothing (:55-59).
  - `faction x` is a test faction (RULED 2026-09-18) so `governance_spine.py`'s generic spine can seat offices; `office_faction` refuses an office naming neither a body nor a faction (:93-99). Church canonical name is "Church of Solmund" (RULED 2026-09-13) (:105-109).
  - `action_vocabulary.yaml` is a PROVISIONAL hand-list of domain-action verbs; the `domain_actions` home is unbuilt (doc: null, port_rank 8, resolver d_sigma) (:119-129).
- **Conflicts / stale:** `name_collision_database.yaml`, `deprecated_terms_registry.yaml`, `silo_overlap_matrix.yaml` left whole (:20-29). Domain-action statement (:124) predates the verb table and `engine/season/verb_table.yaml`; whether "doc: null" still holds is [UNVERIFIED].
- **Open items:** ED-IN-0025 (7-vs-9 core attributes) is called open at :56-59; this digest did not check whether a later ruling closed it (the 2026-11-05 attribute-rulings proposals likely supersede it) [UNVERIFIED].

### references/what_valoria_is_and_what_runs.md
- **What it is:** orientation/measurement reference, 2026-09-05, IN lane, ED-IN-0202; measured against `main` at `9ebd148`; one-pass description of the game, nine required systems vs measured state, eight false self-claims, the held-back architecture chain.
- **Status:** "REFERENCE. Not canon, not a proposal, nothing ratifies on merge" (:3). Reading: historical (2026-09-05); the header itself says code wins and this file is stale; a large part of it describes the since-deleted campaign driver and Key substrate.
- **Bears on:** CORE, CHAR, MB, PC, SC, FA, SE, FI, WR, DICE, GO.
- **Content that matters:**
  - Epistemic contract: the engine owes "the arithmetic of what your character already holds, and nothing about the world they do not"; hidden actors are hidden in existence, never arithmetic (:30-33, citing `04_CODE_ARCHITECTURE.md` §C.11).
  - Dice: d10 pool, TN 7 always (`_require_tn7`, ED-IN-0196); die rule 1=-1, 2-6=0, 7-9=+1, 10=+2; margin ladder `<0` Failure, `0≤m<1` Partial, `1≤m<3` Success, `m≥3` Overwhelming; continuous mode Normal(0.40N, 0.800√N); sigma-leverage soft-cap `1.5·tanh(x/1.5)`; a `BandExtension` can only veto an Overwhelming (:81-92).
  - Jordan's nine-system framing quoted verbatim (:98-108); measured state table per system: overview/scenes/arcs "designed, essentially unbuilt"; one faction scale acts; personnel nothing runs; settlements state executes but nothing founds or builds ("the world only decays"); mass battle strongest (51×51 field, 18 ticks/turn, Lanchester volleys, du Picq rout 15-30%, facing octagon); social contest 1 of 4 GAMES rows built; duel is a 16-state graph with 53 weapons and armour-defeat thresholds none 0 / light .30 / medium .45 / heavy .72, no grid or squad layer; fieldwork stubs (the six investigation acts declare no contest); generation exists and never fires, `capability` has no season writer so nobody improves (:110-120).
  - Eight false self-claims (:137-146): no mandatory pass in `faction_take_action` (GD-2); `world.clocks['Turmoil']` never written so GD-1's Political Stability clause is vacuously true; insurgency pipeline and NPC population engine pinned at zero; `degree_from_net` docstring's "every call site hand-set Ob" false (`crown_initiative.coronation_renewal_ob`); MB "cell is the primitive" is a directive not accomplished state (stamina per column, discipline per subunit); four MB flags (`PC_CELL_MORALE`, `PC_CELL_DAMAGE`, `PC_CLOSE_RANKS`, `PC_FRICTION_CEV`) claimed "default OFF" but default ON; seven (not six) faction-unique actions unbuilt including `altonian_reinforcements.py` raising `NotImplementedError`; `requires_typed:` half-closes F.24.
  - The 2,403-forks "nothing changed" baseline is RETRACTED (H-117: INERT-BY-CONSTRUCTION; every arm 3,204 = 801 no-live-window + 2,403 inert + 0 genuine) (:172-181); "NPC RUNS=0 / ARC ENDS=0" is false, the instrument prints NOT-COMPUTABLE (:183-186). Re-measured 2026-09-10: 143 cases, 54 UNREPRESENTABLE (faction 44, world 10), 10 of 37 verbs executed, 16 distinct executed sets over 89 worlds, R3 22/30 NPC and 34/59 ARC (:191-200).
  - Architecture chain (holonic → executable → meta → social-contest branches) is PROPOSED and held back; six axioms; "keep the physics, replace the spine" (:214-282); five open choices (:301-309).
- **Conflicts / stale:** Everything about "the Key substrate (log, invariants, content hash, deferred-apply boundary)" as a keeper (:272-274), `KeyLog.content_hash()` (:209), and `engine/cross_scale/articulation.py` "13 Key callbacks" (:112) is stale: Key substrate RETIRED (ED-IN-0232). The campaign driver (`engine/autoload/victory.py`, `systems/world/sim`, `engine/tests/test_f7_smoke_oracle.py`) is deleted at `28-iii` per its own correction (:150); `tools/balance_oracle.py` (:332) is RETIRED (CLAUDE.md §7); `python engine/season/corpus_run.py` moved to `python -m engine.season.harness.corpus_run`. §3 row 5 and 6 (MB flags) were not re-verified here [UNVERIFIED]; a lane should grep `modules/mass_battle/config.py`. The "nine of 27 module contracts with doc: null" count (:112) predates later work. The table "Overview ... essentially unbuilt" predates `engine/season/` growth (scenes, `gaps.py`, harness).
- **Open items:** the five chain questions (:301-309: faction stat block vs AX-4, Accord/PT as fields, which clocks survive AX-5, four games vs venue rows plus `settle()`, who authors occasions) are framed as facts about the chain; whether later rulings answered them is for the FA, SC, WR lanes. `FORK:c451bcb` unfollowable in a shallow clone (:319-322).

## Cross-subsystem leads

PENDING (written after the ledger is read).

## Likely stale or superseded

PENDING.

## Items that could change an audit finding

PENDING.
