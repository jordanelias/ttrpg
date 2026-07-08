# Term Usage Sweep — Batch 4: Debate / Social Contest terms - resolve the Piety Track vs Persuasion Track question

# Batch 4 — Debate / Social Contest Terms: Full Findings

## Preliminary note on method

This batch's two headline questions (Piety Track vs Persuasion Track; the Interaction Type label set) turn out to be tightly linked and are addressed together below under Term 1 and Term 8 respectively. Both are, encouragingly, **already known to the project** — tracked in `canon/editorial_ledger.jsonl` and `handoffs/HANDOFF_SC.md` — but neither is resolved as of today (2026-07-08). I cite the live ledger entries verbatim rather than treating this as an original discovery, while still doing the full independent verification the batch asks for.

---

## 1. Piety Track / CT

### Home definition (as given)
`references/glossary.md` Part Three, line 86:
> `Piety Track | CT* | 0–10 | Debate position tracker. Side A wins at ≥ 7; Side B wins at ≤ 3. Compromise zone: 4–6. Canonical doc: designs/personal/conviction_track_v1.md (promoted PP-681).`

with a usage note at line 94: `**CT** is the preferred abbreviation for Piety Track. Even CT should not stand alone.`

### What the cited canonical doc actually contains
I read `designs/personal/conviction_track_v1.md` in full. It contains **no 0–10 tracker, no "Side A/Side B," no "Compromise zone."** It is titled "Valoria — Piety Track" (line 8) but its actual content (confirmed by direct read) is:
- §1 Conviction Taxonomy — a table of moral-belief axes (Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity, Community, Warden), lines 16–28.
- §2 Scar Accumulation and Conviction Effects — a per-Conviction 0/1/2/3+ Scar-count table driving NPC "Conviction crisis," lines 32–58.
- §3 Thread Operation → Conviction Scar Triggers, lines 64–87.
- §4 Cross-references, lines 91–107.

This is the **NPC/PC moral-belief Scar/crisis mechanic**, not a debate-position tracker. The file's own top banner (line 1) even flags it `[SUPERSEDED 2026-05-10 — PP-717]` for §1 (superseded by `designs/personal/conviction_taxonomy_v30.md`, PP-684's 13-Conviction set) while claiming `STATUS: CANONICAL` (line 5) for the rest. So the glossary's citation for "Piety Track" points at a file that is (a) about a completely different mechanic, and (b) itself partially superseded.

### What the actual 0–10 debate-position tracker is called in its own canonical home
I read `designs/scene/social_contest_v30.md` and `params/contest.md` in full, plus `sim/personal/contest/resolver.py`. The mechanic the glossary describes is real and is called **Persuasion Track** everywhere in its home documents:
- `designs/scene/social_contest_v30.md:89-93` (§2 Step 4): "**Step 4 — Set Persuasion Track:** Scale: 0–10. Side A wins at ≥ 7. Side B wins at ≤ 3. Compromise zone: 4–6."
- `designs/scene/social_contest_v30.md:276`: "Persuasion Track ≥ 7 = Side A wins; ≤ 3 = Side B wins; 4–6 = compromise."
- `params/contest.md:127-128`: "## Persuasion Track / Range: 0–10. Side A wins ≥ 7. Side B wins ≤ 3. Compromise zone: 4–6."
- `sim/personal/contest/resolver.py:79-93`, class `PersuasionTrack(WinCondition)`: "Canon's two-pole Persuasion Track... a 0-10 axis, neutral start 5... `>=9 A_total · >=7 A_decisive · 4-6 committee · <=3 B_decisive · <=1 B_total`."

Word-for-word, the glossary's thresholds (≥7 Side A, ≤3 Side B, 4–6 Compromise) are the Persuasion Track's thresholds, not anything found in `conviction_track_v1.md`.

### A third, genuinely distinct mechanic also called "Piety Track (PT)"
Separately, I found a **BG/faction-scale, per-territory, 0–5 stat**, also called "Piety Track," with abbreviation **PT** (not CT):
- `params/bg/tracks.md:139-159`: "## Starting Piety Track (PT) — PP-652 (provisional), peninsular_strain_v30.md §2.2" — per-territory starting values 0–5 ("Aligned/Restoration pole" framing).
- `params/bg/core.md:117-138`: "**Starting Piety Track (PT) values:**" — a different per-territory 0–5 table (Crown-side "PV" framing; note this table's header actually says "Starting PV," a further internal label wobble in the same file).
- `designs/provincial/clock_registry_v30.md:60`: `| Piety Track (PT) | 0–5 | Varies by territory | victory_architecture_v1.md §2. Oscillating: 0 = Restoration pole, 5 = Piety pole. |`
- `designs/provincial/victory_v30.md:111,165` (§0.4, §2 "Piety Track (PT)") and its co-files `victory_v30_index.md`, `victory_v30_infill.md`.
- `designs/provincial/ci_political_v30.md:36`: "SW is NOT the same as Piety Track (PT). PT is dynamic... SW is fixed."
- **Its actual canonical home**, per `references/canonical_sources.yaml:222-230` (`conviction_track:` block), is `designs/scene/conviction_track_v30.md` — a *different file* from `designs/personal/conviction_track_v1.md`, despite the near-identical filename. I confirmed by direct read: `designs/scene/conviction_track_v30.md:5,8,14`: "# Valoria BG — Piety Track & Church Victory Redesign... ## 1. Piety Track — Per-Territory Stat."

This 0–5 per-territory PT is mechanically unrelated to the 0–10 personal-scale debate tracker — different scale (world/BG vs. personal/scene), different range (0–5 vs 0–10), different semantics (Solmund-orthodoxy alignment of a territory vs. who is winning an argument).

### The registry itself is internally contradictory on top of this
`references/canonical_sources.yaml:222-230`'s `conviction_track:` entry sets `design_doc: designs/scene/conviction_track_v30.md`, but its own `canonical_status` field describes content — "§1 (9-Conviction set)... §2 Scar accumulation now per-Conviction (PP-718)... §3 Thread Operation triggers remain canonical" — that is **not in `conviction_track_v30.md` at all**; it is a description of `designs/personal/conviction_track_v1.md`'s §1/§2/§3 (Conviction Taxonomy / Scar Accumulation / Thread Operation Triggers, verified above). So the registry's own design_doc pointer and its own descriptive annotation refer to two different physical files.

### This exact collision is already tracked, and open, in the ledger
I did not have to discover this cold — it is filed:
- `canon/editorial_ledger.jsonl:335`, **ED-SC-0003** (filed 2026-07-05, from Fable 5 audit finding N-4b): *`"status": "open", "needs_jordan": true`* — `"resolve the 'Piety Track' name collision... One name, two referents, three docs: the 0-10 debate tracker is 'Piety Track' in scale_transitions_v30/npc_behavior_v30/glossary (glossary.md:84 points its canonical home at conviction_track_v1.md) but 'Persuasion Track' throughout social_contest_v30.md; params/bg/ separately uses 'Piety Track (PT)' for an unrelated per-territory BG stat... RATIFIED-AS-ACCEPTED by Jordan 2026-07-05... [as a backlog item; the fork itself has no stated default and stays needs_jordan]."`
- `canon/editorial_ledger.jsonl:174`, **ED-1006** (open since 2026-06-10, broader/older, overlapping but distinct per the audit's own cross-check in `designs/audit/2026-07-07-unaddressed-areas-audit/01_workings/refutations/gapclosure_G2.md:66`): flags a *"3-way piety/conviction_track name collision (substrate SS8.4 vs designs/personal/conviction_track_v1 vs designs/scene/conviction_track_v30)"* and separately that *"conviction_track_v1 header-CANONICAL but absent from canonical_sources (A8)"* — confirming `conviction_track_v1.md`'s own `CANONICAL` self-label (line 5 of that file) was never entered into `canonical_sources.yaml` at all.
- `canon/editorial_ledger.jsonl:188`, **ED-919** (open since 2026-06-11): *"Piety-Track wording where Conviction is meant"* — `designs/scene/fieldwork_v30.md` §2.3/§5.7 say "Piety Track offset" where `params/fieldwork.md` correctly says "Conviction offset"; explicitly states "the personal track is Conviction (CV); Piety/PT is the separate 0-5 territory stat." I found a further, uncatalogued instance of this exact same drift pattern at `designs/personal/knots_v30.md:166`: `"Witnessing Conviction Scar fire in Knot partner (Piety Track ≥ 3 Scar count)"` — again using "Piety Track" where "Conviction" (Scar count) is meant.
- `handoffs/HANDOFF_SC.md:100`: lists *"Piety/Persuasion tracker naming + canonical home"* as one of four items in the **P0 decision docket awaiting Jordan's picks**, i.e. as of today this is a live, open, named blocker in the project's own continuity file, not merely something I noticed.

### Fourth usage: "Piety Track" as a *loose synonym* for Persuasion Track in BG/faction param docs
Beyond the two genuinely distinct mechanics above, several files use "Piety Track" as an apparent unswept **old name** for the 0–10 personal debate tracker itself (same ≥7/≤3 thresholds, wrong scale-name):
- `params/scale_transitions.md:46,75`: "**Debate outcome → Domain Echo:** Piety Track ≥7 (winner) queues +1... ≤3 queues −1..." / "Debate Piety Track outcomes map to Domain Echo as follows:"
- `params/factions/npc_stance_triangles.md:66`: "Trigger: decisive Contest outcome (Piety Track ≥ 7 or ≤ 3)..."
- `params/factions/stats_1_7_scale.md:417`: "On Partial: Contest at Piety Track 5."
- `designs/npcs/npc_behavior_v30.md:394,465,657-721,1085` (many instances) — e.g. line 394: "A Contest produces decisive outcome (Piety Track ≥ 7 or ≤ 3)"; line 657: table header "Piety Track | Outcome."
- `designs/provincial/factions_personal_v30.md:63`: "On Partial: GM may call a Contest at Piety Track 5 (neutral)."
- `designs/provincial/faction_politics_v30.md:92,681`: faction-internal appeal "Piety Track (Standard Contest)"; a catastrophic-failure clause resetting "PC's Piety Track... to neutral (5/5/5)."

`references/silo_cohesion_analysis.md:4,39` explicitly documents this as a **known, in-progress rename**: *"Conviction Track split → Persuasion Track (contest) / Piety Track (territory)... 'Conviction Track' (89 files) Corpus-wide residual — Deprecated. Contest → Persuasion Track. Territory → Piety Track. Corpus sweep in progress."* So the corpus's own terminology-hygiene analysis confirms: the debate-tracker's *current* canonical name is Persuasion Track, "Piety Track" is reserved for the territory stat only, and the residual "Piety Track" appearances in `npc_behavior_v30.md` / `scale_transitions.md` / `npc_stance_triangles.md` / `faction_politics_v30.md` are acknowledged leftovers of an incomplete sweep, not competing canon.

### Divergence summary
| Referent | Range | Canonical home (best evidence) | Abbrev |
|---|---|---|---|
| Personal-scale debate-position tracker (glossary's actual described mechanic) | 0–10, ≥7/≤3/4-6 | `designs/scene/social_contest_v30.md` + `params/contest.md` + `resolver.py PersuasionTrack` | none (glossary wrongly assigns "CT") |
| BG per-territory Solmund-orthodoxy stat | 0–5 | `designs/scene/conviction_track_v30.md` §1 (per `canonical_sources.yaml`, itself internally contradictory — see above) | PT |
| NPC/PC moral-belief Scar/crisis system (what `conviction_track_v1.md` actually documents) | per-Conviction 0/1/2/3+ Scar counts | `designs/personal/conviction_track_v1.md` (self-labeled CANONICAL but absent from `canonical_sources.yaml` per ED-1006) | none formalized |

The glossary's single Part Three row conflates the first mechanic's *definition* with the third mechanic's *file citation*, while a fourth cluster of docs uses "Piety Track" as a residual synonym for the first mechanic. **This is a real, currently-open, four-way terminology tangle, not resolvable to a single clean answer from the corpus as it stands today** — Jordan's decision is pending per ED-SC-0003.

### Classification table

| Site (file:line) | Classification | Mechanism / evidence | Agrees with which canon? |
|---|---|---|---|
| `references/glossary.md:86` | UNCLEAR / NO CANONICAL SOURCE | States a formula matching Persuasion Track but cites `conviction_track_v1.md`, which contains no such mechanic | Formula agrees with Persuasion Track; citation does not |
| `designs/scene/social_contest_v30.md:89-93,276` | CANONICAL DEFINITION (of "Persuasion Track") | Home doc, ratified (CR3, `RATIFIED_2026-06-01.md`) | — |
| `params/contest.md:127-130` | CANONICAL DEFINITION (co-canonical param head) | Explicitly single-sourced from social_contest_v30 per file header | Agrees with social_contest_v30 |
| `sim/personal/contest/resolver.py:79-93` (`PersuasionTrack`) | CANONICAL DEFINITION (kernel implementation) | Implements the identical bands (`>=9/>=7/>3/>1`) | Agrees |
| `designs/scene/conviction_track_v30.md:14` | CANONICAL DEFINITION (of the *different* per-territory "Piety Track (PT)") | Home doc per `canonical_sources.yaml` | — |
| `references/canonical_sources.yaml:222-230` | UNCLEAR / NO CANONICAL SOURCE (self-contradictory) | `design_doc` field vs. `canonical_status` field describe two different physical files | N/A — internally inconsistent |
| `designs/personal/conviction_track_v1.md` (whole file) | CANONICAL DEFINITION (of the Conviction Scar/crisis system) but **not registered** | Self-labeled `STATUS: CANONICAL`; absent from `canonical_sources.yaml` per ED-1006 | N/A |
| `params/scale_transitions.md:46,75`; `params/factions/npc_stance_triangles.md:66`; `params/factions/stats_1_7_scale.md:417`; `designs/npcs/npc_behavior_v30.md` (many); `designs/provincial/factions_personal_v30.md:63`; `designs/provincial/faction_politics_v30.md:92,681` | HARDCODED DUPLICATE (stale name for Persuasion Track) | Independently restates "≥7/≤3" thresholds under the old name; acknowledged as unswept residue in `silo_cohesion_analysis.md:39` | Numerically agrees with Persuasion Track; name has already drifted |
| `designs/personal/knots_v30.md:166` | HARDCODED DUPLICATE (stale name for Conviction Scar count) | "Piety Track ≥ 3 Scar count" — should read "Conviction," per ED-919's pattern | Semantically wrong name for a Scar-count concept |
| `canon/editorial_ledger.jsonl:335` (ED-SC-0003), `:174` (ED-1006), `:188` (ED-919) | PULLED / REFERENCED (tracking entries, not definitions) | Ledger records citing the above sites as the collision's evidence | N/A |
| `handoffs/HANDOFF_SC.md:100` | PULLED / REFERENCED | Bare pointer to the open P0 docket | N/A |

No incidental-English exclusions were needed for this term — "piety"/"persuasion"/"conviction" as bare English words do not otherwise appear as false positives in the grep set I reviewed.

---

## 2. Persuasion Track

Folded into Term 1 above per the batch's framing. Summary: **Persuasion Track is the current, live, actively-developed canonical name** for the 0–10 personal-scale debate-position tracker (`social_contest_v30.md`, `params/contest.md`, `resolver.py PersuasionTrack`, `sim/personal/parliamentary_vote.py`, `sim/personal/tribunal.py`, `sim/personal/contest/faction.py` all use it consistently — I spot-checked `resolver.py` and `faction.py` directly). It is **not** the same mechanic as the glossary's citation target (`conviction_track_v1.md`), and it **is** the same mechanic the glossary's Part Three row is actually trying to describe (the numbers match exactly). Occurrences in `designs/scene/social_contest_v30.md` (dozens, e.g. lines 89,184,198,206,209,237,257,276,300,359,382,396,401,594,604,606) and `params/contest.md` (lines 90,110-112,127-130,133-190 area, 237,264,270) are internally consistent — I opened enough of them (quoted above) to confirm no drift between the two co-canonical files.

**Classification:** `social_contest_v30.md` = CANONICAL DEFINITION; `params/contest.md` = CANONICAL DEFINITION (co-canonical, single-sourced per its own header `<!-- sources: designs/contest/social_contest_v30.md -->`); `resolver.py PersuasionTrack` = CANONICAL DEFINITION (kernel); dozens of `tests/sim/*.md` and `designs/audit/*` occurrences = PULLED/REFERENCED (citing the above, not independently defining new numbers) — I sampled several (`tests/sim/sim_debt_03_04_contest_baselines.md`, `designs/audit/2026-07-01-contest-gate-a-packet/GATE_A_packet.md`) and found them quoting rather than restating the mechanic independently.

---

## 3. Concentration

### Home definition
`designs/scene/social_contest_v30.md:256`: "**Concentration = (3 × Focus) + (2 × Spirit).** Range 5–35... (Canonical per derived_stats_v30 §14.1: ED-901 (STRUCK Focus×3) + ED-902 (coefficients + Cognition→Focus engine fix) + ED-933 (params propagation)); supersedes the struck Focus × 3." Depletes 5/exchange, −5 more on loss.

`params/contest.md:140`: identical formula, `(3 × Focus) + (2 × Spirit)`, range 5–35, same ED citations.

`designs/scene/derived_stats_v30.md:147-160`: §5.2 "Concentration (action economy resource)" — same formula, explicitly noting it supersedes an even older `Focus + Recall` form and the interim `Focus × 3` form (ED-902, 2026-06-04).

### Exhaustive sweep and divergence
1. **Glossary is formula-free.** `references/glossary.md:87`: `Concentration | — | varies | Debate resource spent to sustain rhetorical positions.` No number at all — not wrong, just uninformative relative to the three prose sites above, which all agree.
2. **`sim/personal/contest/primitives.py:49-56`, class `Reserve`:** `MAX = 12  # [SEED]`, an *abstract per-move stamina pool* with costs `{"advance": 3, "hard": 5, "shift": 4, "support": 2, "pass": 0, "evidence": 3, "rebut": 3}`. This is explicitly **not** the same magnitude as the prose formula — the code's own comment says so directly (`primitives.py:99-103`): *"The kernel's Reserve is an ABSTRACT per-move stamina pool ([SEED] MAX=12, per-move COST) — it does not hard-code any attribute formula; the (3*Focus)+(2*Spirit) magnitude is the v30-surface value the wrapper/params carry, not a kernel literal."* I checked this claim against `sim/personal/contest/wrapper.py` directly: grepping for `Focus`/`Spirit`/`Concentration` in that file returns **only** comment-level naming references (lines 282,283,292-294 — e.g. `"three_trackers": {"fn":"TRACKERS", ..., "status":"WIRED"}`), never a numeric formula or a `(3*focus)+(2*spirit)` computation. So the code comment's claim that "wrapper.py... carries" the v30-surface magnitude is **not actually true of the code** — no file in `sim/personal/contest/` computes `(3×Focus)+(2×Spirit)` or converts it into `Reserve.MAX`. The bridge between the prose's 5–35 Concentration and the kernel's abstract 0–12 Reserve is asserted in commentary but not implemented anywhere I could find.
3. `references/mechanical_terms_index.md:96,610` gives the same formula-free description as the glossary ("Action-economy resource for sustained positions"), citing `contest, derived_stats §5.2` — a bare citation, not an independent number.

### Classification table
| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon? |
|---|---|---|---|
| `designs/scene/derived_stats_v30.md:147-160` | CANONICAL DEFINITION | Attribute-derivation home doc, explicit ED-901/902/933 chain | — |
| `designs/scene/social_contest_v30.md:226,256` | HARDCODED DUPLICATE | Independently restates `(3×Focus)+(2×Spirit)`, 5–35 | Agrees (currently) |
| `params/contest.md:140,153-156` | HARDCODED DUPLICATE | Independently restates same formula | Agrees (currently) |
| `references/glossary.md:87` | PULLED / REFERENCED (thin) | States no number ("varies"); not a competing definition | N/A — no number to disagree with |
| `references/mechanical_terms_index.md:96,610` | PULLED / REFERENCED | Bare citation "derived_stats §5.2," no independent number | N/A |
| `sim/personal/contest/primitives.py:49-56` (`Reserve`) | UNCLEAR / NO CANONICAL SOURCE for the bridge | Abstract `MAX=12 [SEED]`, explicitly disclaimed as a different, unconverted magnitude from the prose formula; the promised conversion in "wrapper.py" is not actually present | Does not use the same numbers as canon at all — not comparable, and nothing converts one to the other |
| `sim/personal/contest/wrapper.py:282-294` | PULLED / REFERENCED (name only) | `TRACKERS`/`MECHANICS` registry entries name "Concentration" as WIRED, but only bind the *name*, not the *formula*, to `Reserve` | Misleading if read as "the formula is implemented" — it names the tracker, nothing more |

I disambiguated ordinary-English "concentration"/"focus" (e.g. "concentration of forces" in mass-battle docs, general narrative prose) and excluded those; the sweep above covers only the game-mechanical Debate-resource sense.

---

## 4. Doubt Marker

### Home definition
`designs/scene/social_contest_v30.md:200,210-217`: placed when, in **CROSS**, "the side with larger movement used Obscuring" (line 200); more generally (§4 Step 4, the un-headed "Obscuring win" clause at lines 209-213): *"Persuasion Track does not move toward winner. Place a Doubt Marker on the opponent. Doubt Marker effect: opponent's next winning exchange has its margin reduced by 2... Only one Doubt Marker active at a time. New replaces old. Consumed on use."* Terminal-Doubt handling (ED-1060, still `OPEN DECISION FOR JORDAN` per line 214) is specified at lines 214-217.

`params/contest.md:114-125`: identical mechanic and identical ED-1060 open-decision framing.

### Divergence
`references/glossary.md:88`: `Doubt Marker | — | token | Applied on Obscuring loss in Diverge state.` This is **wrong on both counts** against current canon:
1. **Trigger direction**: canon places the marker on an Obscuring **win** (the side with the larger movement, i.e. the winner, used Obscuring), not on an Obscuring **loss**. Quote, `social_contest_v30.md:200`: "if the side with larger movement used Obscuring, place a Doubt Marker on the opponent" — the marker punishes the *loser of that exchange*, planted *by* the Obscuring winner, not applied *because of* a loss.
2. **State name**: "Diverge state" is the retired pre-v30 interaction type (see Term 8) — current canon fires this in **CROSS** (and, per the general Step 4 text, potentially any Obscuring win). `social_contest_v30.md:680` (§12, "Carried forward"): `ED-133 | Diverge state — superseded by CROSS. Confirm Diverge no longer needed. | P2` — an item still open, not closed, as of the current head.

`references/mechanical_terms_index.md:611` repeats the **identical stale wording**: `Doubt Marker | Token applied on Obscuring loss in Diverge state.` — the same error duplicated across two separate reference indices, suggesting one was copied from the other (or both from a common pre-v30 ancestor) without either being resynced against `social_contest_v30.md`.

### Classification table
| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon? |
|---|---|---|---|
| `designs/scene/social_contest_v30.md:200,209-217` | CANONICAL DEFINITION | Home doc | — |
| `params/contest.md:114-125` | HARDCODED DUPLICATE | Independently restates the full mechanic and the ED-1060 open item | Agrees |
| `designs/npcs/npc_behavior_v30.md` (per earlier "Piety Track" grep, co-located usages) | PULLED / REFERENCED | Cites Doubt Marker in context of Contest outcomes, doesn't redefine it | Consistent |
| `references/glossary.md:88` | HARDCODED DUPLICATE, **DRIFTED** | Independently restates trigger + state name | **Disagrees** — wrong trigger direction (loss vs win) and cites a retired state name (Diverge, superseded by CROSS per ED-133) |
| `references/mechanical_terms_index.md:611` | HARDCODED DUPLICATE, **DRIFTED** | Same wording as glossary, independently stated | **Disagrees**, identically to the glossary entry |
| `sim/personal/contest/dictionaries.py`, `resolver.py`, `rhetoric.py` | (see Term 8 — Doubt Marker's mechanical trigger is not yet wired into the CLASH/REINFORCE/CROSS resolution path; only the CR5 self-backfire half is wired, per `resolver.py:390-419`) | Code implements CR5's self-Face-backfire (`cr5_self_backfire`), not the Doubt-Marker-placement half | The Doubt Marker *rule* (prose) is undisputed; its *code* realization is a separate, honestly-flagged gap, not a numeric contradiction |

---

## 5. Composure (Debate context)

### Home definition and the critical currency fact
Composure's *base* formula is defined once, corpus-wide, in `params/core.md:160`: `Composure | Charisma × 3 | 3–21 | Social damage buffer before Rattled. Strain scaled ×3... (ED-694, replaces Cha+6)`.

**But inside the Debate/Contest system specifically, Composure was formally retired as of `RATIFIED_2026-06-01.md` CR3** and split into two trackers. Direct quotes from `designs/scene/social_contest_v30.md:231-239`:
> "**CR3 (RATIFIED 2026-06-01):** the single **Composure** buffer is **RETIRED as the social-contest tracker** and split into the two distinct trackers whose roles it conflated... The contest now carries **three** trackers: **Concentration** (stamina)... **Face** (contest-local ethos/standing)... **Persuasion Track** (merits clock, PRESERVED)."

`params/contest.md:132-133` states the identical retirement. The retirement is explicitly **scoped only to the contest tracker** — `social_contest_v30.md:509-513` ("RESOLVED — Composure-retirement blast radius... Gate A") states Jordan CONFIRMED "scoped-rename-only": Composure references in knots (`designs/personal/knots_v30.md` §4.2), combat, and conviction are **deliberately NOT touched**. I verified this directly: `params/core.md:160` (base attribute formula, unchanged, still says "Composure") and `designs/personal/knots_v30.md:56,124-127,166,186-188,197-198,201,213-220` (Knot-as-Composure-buffer mechanic, still live, still called Composure) both confirm Composure is alive and canonical **outside** the contest.

### Divergence — the glossary has not been updated for CR3 at all
This is the batch's specific ask (cross-check vs. Batch 2). Three separate glossary points are stale relative to the 2026-06-01/07-01 CR3 ratification:

1. `references/glossary.md:51` (Part One): `Composure | — | varies | Social endurance track. Used in Debate. Rattled at ≤ 2; concession forced at 0.` — This does not match **either** the pre-CR3 formula (`params/core.md:160`, Cha×3, 3–21, no "≤2"/"concession at 0" language at all) **or** the post-CR3 contest mechanic (`social_contest_v30.md:241-245`: Rattled fires at "strain ≥ Face," where Face's threshold is the Cha×3 value, not a flat "≤2"; there is no "concession forced at 0" rule anywhere in current canon — the closest analogues are "2 marks = socially incapacitated" (`params/contest.md:149`) and Concentration's separate "Spent" state at 0). This looks like a leftover from an even earlier design iteration that was never reconciled against either the ED-694 (Cha×3) or CR3 (Face split) revisions.
2. `references/glossary.md:89` (Part Three): `Composure | — | varies | Social endurance (see Part One). Also the damage track in Debate exchanges.` — Presents Composure as still being *the* live Debate exchange damage track. Per CR3, it is **not**: the live contest-local ethos/standing track is now named **Face**, and stamina is **Concentration**. The glossary Part Three has no "Face" entry at all (confirmed — grepped the whole file, zero hits for "Face" as a game term), so a reader relying on the glossary for the Debate system would not learn that Composure was retired from this role over a month before the glossary's own "last swept" date claims otherwise are even in play — the glossary's header says "content last swept 2026-04-30, PP-691" (line 3), which in fact **predates** CR3 (2026-06-01) entirely, so the staleness is dateable and expected, just never corrected since.
3. `references/glossary.md:244` (Part Twelve collision table): `COMP | Composure (Debate context) | Computation / Composition (general English) | Write "Composure" in game documents.` — This entry's own label, "Composure (Debate context)," is the thing CR3 renamed away from; it's a second, independent stale reference to the same retired role.

### Classification table
| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon? |
|---|---|---|---|
| `params/core.md:160` | CANONICAL DEFINITION (base attribute formula, unretired, corpus-wide) | Home doc for the Cha×3 formula | — |
| `designs/scene/social_contest_v30.md:231-260,485,509-513` | CANONICAL DEFINITION (of the CR3 *retirement*, scoped to contest) | Ratified decision doc + propagation | — |
| `params/contest.md:132-151` | HARDCODED DUPLICATE (of the CR3 retirement text) | Independently restates the three-tracker split and the Gate-A scoping note | Agrees |
| `designs/personal/knots_v30.md:56,124-220` | PULLED / REFERENCED + HARDCODED DUPLICATE mix | Cites "Knot-as-Composure-buffer" per `social_contest §4 Step 6`, but independently states its own point-costs (e.g. "Break Composure damage = 4," "2 Composure" for dissolution) | Consistent with the *pre-CR3, unretired* Composure that CR3 explicitly left untouched here |
| `references/glossary.md:51` (Part One) | HARDCODED DUPLICATE, **DRIFTED** (against both old and new canon) | Independently states "Rattled at ≤2; concession forced at 0" | Disagrees with both the ED-694 formula and the CR3 mechanic |
| `references/glossary.md:89` (Part Three) | HARDCODED DUPLICATE, **STALE** (pre-CR3) | States Composure is still "the damage track in Debate exchanges" | Disagrees with CR3 (Face now holds this role in-contest) |
| `references/glossary.md:244` (Part Twelve) | HARDCODED DUPLICATE, **STALE** (pre-CR3) | Labels the collision-table entry "Composure (Debate context)" | Same staleness as line 89 |

I excluded ordinary-English "composure"/"composition"/"computation" occurrences per the glossary's own COMP collision-table guidance (line 244) — those aren't game terms and I did not count them in the sweep above.

---

## 6. Genre

### Home definition
`designs/scene/social_contest_v30.md`, header block lines 16-17: "Three genres (Past/Present/Future) → two genres (Memory/Projection)" (PP-234). Current live definition, `§2 Step 2` (lines 41-58) and `§4 Step 2` (line 157): **Genre ∈ {Memory, Projection}**, now further gated by the CR4 Ciceronian-stasis mechanism (lines 48-61). `params/contest.md:27-31` gives the identical two-genre table with Temporal/Epistemic/Actualization Status columns.

### Divergence
`references/glossary.md:90`: `Genre | — | Past / Present / Future | Debate argument type selection each exchange.` This is the **pre-PP-234 three-genre system**, explicitly superseded — the same social_contest_v30.md file that the glossary is nominally describing states its own supersession in its header block (line 17, quoted above). The glossary's stated "last swept" date (2026-04-30, PP-691) is *after* PP-234 (dated 2026-04-04 per the doc header), so this isn't a case of the glossary predating the change — it's a case of the sweep missing this row entirely.

I also found a **third, older historical layer** still present in `designs/arcs/emergent_arcs_experimental.md` (lines 13,36,39,52,64,73,85,187,190), which uses genre labels like "Evidence genre," "Consequence genre" — an even earlier vocabulary from a "Debate redesign v1" predecessor system, confirming this file was never updated across at least two generations of the Genre taxonomy. This is a narrative-arc design doc, not update-tracked against social_contest_v30, so I flag it as a known-stale historical artifact rather than a live contradiction, but it does show three co-existing generations of "Genre" values in the corpus at once (Evidence/Consequence in old arcs docs; Past/Present/Future in the glossary; Memory/Projection in current canon).

### Classification table
| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon? |
|---|---|---|---|
| `designs/scene/social_contest_v30.md:16-17,41-58` | CANONICAL DEFINITION | Home doc, PP-234 restructure + CR4 update | — |
| `params/contest.md:27-31` | HARDCODED DUPLICATE | Independently restates Memory/Projection | Agrees |
| `references/glossary.md:90` | HARDCODED DUPLICATE, **DRIFTED** | States "Past/Present/Future" | Disagrees — describes the pre-PP-234 three-genre system, superseded since 2026-04-04 |
| `designs/arcs/emergent_arcs_experimental.md:13,36,39,52,64,73,85,187,190` | HARDCODED DUPLICATE, **DOUBLY STALE** | Uses "Evidence genre"/"Consequence genre," an even earlier vocabulary layer | Disagrees with both current canon and the glossary's (also-wrong) Past/Present/Future |
| `references/mechanical_terms_index.md` (not separately re-quoted; consistent with `Memory`/`Projection` where checked) | PULLED / REFERENCED | Cites `contest §4` for genre | Agrees where checked |

I excluded incidental English "genre" (there is essentially none in this corpus outside the game-mechanical sense — I checked and all hits were the Debate/arc mechanic, some just stale).

---

## 7. Orientation

### Home definition
`designs/scene/social_contest_v30.md:157` (§4 Step 2): "Each orator selects a genre (Memory or Projection) and an orientation (**Revealing** or **Obscuring**)." `params/contest.md:34-42` (Argument Styles table): Precedent=Memory+Revealing, Suppression=Memory+Obscuring, Vision=Projection+Revealing, Insinuation=Projection+Obscuring.

### Divergence — an in-file residual inside the params doc itself
`references/glossary.md:91`: `Orientation | — | Revealing / Obscuring | Debate stance selection each exchange.` — **This matches current canon.** No divergence here.

However, `params/contest.md` — the very file that correctly uses Revealing/Obscuring in its Argument Styles table (lines 34-42) and Faction Boosts table (lines 67-77) — **contradicts itself** at its own Exchange Structure section:
- `params/contest.md:98`: "Step 2 — Choose genre (Memory/Projection) + orientation (**Direct/Indirect**)."
- vs. `params/contest.md:114`: "[ED-897: **"Indirect"→"Obscuring"**, "Doubt Marker"→"Doubt Marker" to match social_contest §4.]" — i.e., the file's own inline editorial note documents that "Indirect" was the *old* label, renamed to "Obscuring" by ED-897, yet line 98 (a different section of the same file) was never updated to match.
- `params/contest.md:123`: "an Obscuring (**Indirect**) argue move" — the *current* CR5 text (added later, 2026-07-02 per its own citation) still uses "Indirect" parenthetically as a live gloss for Obscuring, showing the old label is still being actively used as a synonym in newly-added prose, not just left over from before ED-897.
- `params/contest.md:81`: an HTML comment records the same rename: `orientation Indirect/Direct → Obscuring/Revealing`.

So within a single file, three different vintages of the same axis's labels coexist: the canonical current pair (Revealing/Obscuring, used in the two main tables), an acknowledged-retired pair (Direct/Indirect, still literally present at line 98), and a hybrid gloss form ("Obscuring (Indirect)," line 123) that keeps the retired term alive as a bracketed alias in brand-new (2026-07-02) text.

### Classification table
| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon? |
|---|---|---|---|
| `designs/scene/social_contest_v30.md:157` and throughout §2-§9 | CANONICAL DEFINITION | Home doc | — |
| `params/contest.md:34-42,67-82` | HARDCODED DUPLICATE | Independently restates Revealing/Obscuring | Agrees |
| `references/glossary.md:91` | HARDCODED DUPLICATE | Independently restates Revealing/Obscuring | Agrees |
| `params/contest.md:98` | HARDCODED DUPLICATE, **DRIFTED (in-file, self-contradicting)** | States "orientation (Direct/Indirect)" | Disagrees with the file's own Argument Styles table 60 lines earlier, and with its own ED-897 rename note 16 lines later |
| `params/contest.md:123` | PULLED / REFERENCED (gloss, not a redefinition) | Uses "(Indirect)" as a bracketed alias for Obscuring in freshly-authored CR5 text | Not wrong per se, but perpetuates the retired label as if still current |

---

## 8. Interaction Type — the CLASH/AMPLIFY/CROSS/DIVERGE vs. CLASH/REINFORCE/CROSS/TIE question, resolved with exact citations

### Glossary side
`references/glossary.md:92`: `Interaction Type | — | CLASH / AMPLIFY / CROSS / DIVERGE | Determined by Genre + Orientation match between orators.`

`references/mechanical_terms_index.md` repeats the identical, wrong label set in three places:
- `:602`: `| **AMPLIFY** (interaction) | Same Genre, same Orientation. | contest §4 |`
- `:604`: `| **DIVERGE** (interaction) | Different Genre, same Orientation. | contest §4 |`
- `:611`: `| Doubt Marker | Token applied on Obscuring loss in Diverge state. |`
- `:1704`: `| Interaction Types (CLASH/AMPLIFY/CROSS/DIVERGE) | 4 | YES — §6.2 |`

### Code side (as the batch asked me to confirm precisely)
`sim/personal/contest/dictionaries.py:19,254-322`:
- Line 19 (module docstring): `4. INTERACTIONS_TABLE — InteractionType×4 (CLASH / REINFORCE / CROSS / TIE) derivation.`
- Lines 254-259 (comment block): 
  ```
  #   same genre, OPPOSITE orientation  -> CLASH     (social_contest_v30 §4: "same genre, opposite orientation")
  #   same genre, SAME orientation      -> REINFORCE (§4: "same genre, same orientation")
  #   DIFFERENT genres                  -> CROSS      (§4: "different genres"; orientation irrelevant)
  #   TIE is OVERLAID on any of the above when successes are equal (§4 Step 4 "TIE (equal
  ```
- Lines 284-305 (`INTERACTIONS_TABLE` dict): `key="clash", name="CLASH"`; `key="reinforce", name="REINFORCE"`; `key="cross", name="CROSS"`; `key="tie", name="TIE"`.
- Lines 309-322 (`def derive_interaction(style_a, style_b)`): returns `INTERACTIONS_TABLE["cross"]` for different genres, `INTERACTIONS_TABLE["reinforce"]` for same-genre/same-orientation, else `INTERACTIONS_TABLE["clash"]` for same-genre/opposite-orientation (TIE is handled separately as an overlay, per the comment at 257-259 and confirmed by `resolver.py`'s own separate TIE win-condition logic).

### Prose side confirms the code, not the glossary
`designs/scene/social_contest_v30.md:181,190,195,204` (§4 Step 4 section headers): `**CLASH**`, `**REINFORCE**`, `**CROSS**`, `**TIE**` — verbatim.
`params/contest.md:106-125` (`## Interaction Types (3 + TIE)` table + line 125 `Coalition Push` clarification): "The interaction types are CLASH / REINFORCE / CROSS / TIE."

**Confirmed, with file:line on both sides**: the prior audit's finding is correct. The glossary's `CLASH/AMPLIFY/CROSS/DIVERGE` does **not** match the current canonical set `CLASH/REINFORCE/CROSS/TIE` used identically by `social_contest_v30.md`, `params/contest.md`, and `sim/personal/contest/dictionaries.py`. This is not a subtle rename either — "AMPLIFY" and "REINFORCE" describe the *same condition* (same genre, same orientation) under two names, and "DIVERGE" and "TIE" are actually **different conditions**: DIVERGE (per `mechanical_terms_index.md:604`) was "different Genre, same Orientation" (a genre-based case, effectively absorbed into CROSS today since CROSS is now simply "any different genre" regardless of orientation), while TIE is an orthogonal, cross-cutting condition ("equal successes, **any** interaction type" — `social_contest_v30.md:204`) — TIE is not a replacement-name for DIVERGE at all, it's a structurally different axis (outcome-parity vs. genre/orientation-matching) that the glossary's row doesn't capture even conceptually.

### Historical confirmation this was a real, dated rename, not an original error
- `designs/scene/social_contest_v30.md:680` (§12 "Carried forward"): `ED-133 | Diverge state — superseded by CROSS. Confirm Diverge no longer needed. | P2` — an item still open, not closed.
- `tests/audit/editorial_resolution_pass.md:220-221`, `220`: "### ED-150: AMPLIFY Combined Pool Cap... Decision: AMPLIFY combined pool cap = highest individual contributor × 2" — confirms "AMPLIFY" was a real, once-canonical name for the same-genre/same-orientation case, later renamed to REINFORCE.
- `designs/audit/2026-06-03-contest-groundup/TERMINOLOGY.md:16`: `` `DIVERGE` canonical term this redesign replaced/omits `` — an explicit acknowledgment, in the groundup-engine design notes that became the current kernel, that DIVERGE was consciously dropped.
- Even the file's own header dating undercuts the glossary's excuse: `params/contest.md`'s stated `last_updated: 2026-04-04` already contains `REINFORCE` at line 44 ("Interaction type derived: same style = REINFORCE, same genre opposite orientation = CLASH, different genre = CROSS"), while the glossary's stated last full sweep is 2026-04-30 (PP-691, per its own header, line 3) — **after** that date. So the glossary was already behind the params doc's terminology at the moment of its own last claimed sweep; this is not a case of a subsequent rename outpacing an old-but-once-accurate glossary entry.

### Classification table
| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon? |
|---|---|---|---|
| `designs/scene/social_contest_v30.md:181,190,195,204,680` | CANONICAL DEFINITION | Home doc; ED-133 explicitly tracks DIVERGE's retirement (still open as a cleanup item) | — |
| `params/contest.md:44,106-125` | HARDCODED DUPLICATE | Independently restates CLASH/REINFORCE/CROSS/TIE | Agrees |
| `sim/personal/contest/dictionaries.py:19,254-322` | CANONICAL DEFINITION (kernel implementation) | `derive_interaction()` + `INTERACTIONS_TABLE`, with inline comments explicitly citing `social_contest_v30 §4` per row | Agrees |
| `references/glossary.md:92` | HARDCODED DUPLICATE, **DRIFTED** | Independently restates a 4-item set | **Disagrees** — CLASH/AMPLIFY/CROSS/DIVERGE vs. current CLASH/REINFORCE/CROSS/TIE |
| `references/mechanical_terms_index.md:602,604,611,1704` | HARDCODED DUPLICATE, **DRIFTED**, same wording as glossary | Independently restates the same stale 4-item set across four separate lines | **Disagrees**, identically to the glossary — likely shared origin or mutual copying, neither resynced |
| `designs/audit/2026-05-28-resolution-diagnostic/ners_verdict_social_contest.md:16` and `resolution_diagnostic_social_contest.md:25,193` | HARDCODED DUPLICATE, **triply stale** | Uses yet another, even older 5-type set: "CLASH/CROSS/COMPETITION/DIVERGENCE/AMPLIFY" | Disagrees with current canon on both count (5 vs 4) and labels |
| `designs/audit/2026-07-05-fable5-social-contest-audit/01_workings/critic.md:23` and `fable5_social_contest_audit_v1.md:121` | PULLED / REFERENCED (auditing the drift, not asserting it as canon) | Explicitly flags (finding **N-10, UPHELD**) that the 5-type taxonomy "does not exist in the rebuilt kernel" | Correctly identifies the divergence rather than perpetuating it |

---

## 9. Face

### Home definition
`designs/scene/social_contest_v30.md:236,249-254` and `params/contest.md:137,143-151`: **CR3** introduces Face as the contest-local ethos/standing tracker: *"Face_max = Charisma × 3, range 3–21 (the retired Composure magnitude, unchanged)... Face_current = round(Standing ÷ 10 × Face_max), where Standing is the unchanged kernel 0–10 ethos-built value."* Explicitly disambiguated: *"Face ≠ Disposition and Face ≠ Reputation... Disposition/Reputation are persistent cross-scene relationship stats; Face is a within-contest tracker that resets at contest end."*

Code home: `sim/personal/contest/primitives.py:105-108` (`Face = Standing` — a bare alias, not a subclass) and `:132-149` (class `FaceScale`, `face_max`/`face_current` static methods implementing the exact formula above). `sim/personal/contest/resolver.py:220-234` (`_Side.face`/`face_max()`/`face_current()` accessors).

### Divergence / honesty gaps (self-disclosed, not contradictions)
The corpus is unusually explicit that Face is only **partially** wired: `social_contest_v30.md:245,253-254,503-506` and `params/contest.md:143-146` all state, in near-identical language, that the strain→Rattled consumption channel and the general CLASH/REINFORCE strain-vs-Face mechanic remain **spec-only**, not implemented — only the narrow CR5 self-backfire path (`resolver.py:404-419`, `c.face.strip_points(backfire)`) actually calls a strip method on Face today. I count this as an honestly-flagged gap rather than a drift, since prose and code agree on exactly what is and isn't wired.

**No glossary entry exists for Face at all** — I grepped the entire glossary file for "Face" as a capitalized game term and found zero hits. Given the glossary's own stated authority ("this file is the canonical reference for all term expansions project-wide," line 4) and maintenance rule ("Update in the same commit as any file that introduces or retires a term," line 5/277), this is a real gap: a CR3-ratified (2026-06-01), actively-implemented tracker with no glossary presence over a month later.

### Classification table
| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon? |
|---|---|---|---|
| `designs/scene/social_contest_v30.md:236,249-254` | CANONICAL DEFINITION | Ratified CR3/Gate-A doc | — |
| `params/contest.md:137,143-151` | HARDCODED DUPLICATE | Independently restates the combo formula | Agrees |
| `sim/personal/contest/primitives.py:105-149` | CANONICAL DEFINITION (kernel) | `Face = Standing` alias + `FaceScale` derived accessor, cited by name from the prose docs | Agrees |
| `sim/personal/contest/resolver.py:220-234,404-419` | PULLED / REFERENCED (imports `FaceScale` from primitives) | `from .primitives import (..., FaceScale)` at resolver.py:17 | Agrees |
| `references/glossary.md` | UNCLEAR / NO CANONICAL SOURCE — **no entry at all** | N/A | N/A |

---

## 10. Stasis

### Home definition
`sim/personal/contest/primitives.py:11-25`, class `Stasis`: six-rung Ciceronian ladder — `FACT, DEFINITION, QUALITY, JURISDICTION, CONSEQUENCE, FEASIBILITY` — plus a `TENSE` mapping and `stronger_than`/`relevant` helpers. `designs/scene/social_contest_v30.md:48-61` (§2 Step 2, "CR4 — the primary genre is TERRAIN-DERIVED, not GM-fiat") gives the prose table mapping "Classical stasis" to "Kernel ground" to "Primary genre," citing `sim/personal/contest/primitives.py Stasis` directly. `params/contest.md:65` restates the CR4 rule identically.

### Sweep and disambiguation
All game-mechanical occurrences I found (`social_contest_v30.md` §2/§7/§8, `params/contest.md` §Genre and Orientation Bonus Dice / §Proceeding Types, `resolver.py Venue.start_ground`, `armature.py`) are consistent with the primitives.py ladder — I opened several (`social_contest_v30.md:48-61,97-106,196,384,497-498`; `params/contest.md:65,190,196`) and found no numeric or structural divergence; all describe the same six-rung ladder and the same CR4 reachability fix (Church Tribunal alone opens at FACT instead of the QUALITY default).

I explicitly **excluded as incidental English** several non-mechanical hits: `designs/world/solmund_v30.md:32,36` and `designs/world/solmund_master_document.md:242,246` ("ontological stasis," a lore description of Solmund's absence of temporal depth — cosmology prose, not the Ciceronian-stasis game mechanic); `designs/audit/2026-06-29-combat-corpus-recovery/weapon-typologies-differential-reference.md:30,119` ("commitment and stasis," a martial-arts/HEMA research term about held postures); and multiple `designs/audit/*workplan*.md` uses of "stasis window" meaning a simulation period with no state change (a balance-testing term, not the rhetoric mechanic). None of these are competing definitions of the game term; they are a different word-sense.

**No glossary entry exists for Stasis** (grepped the whole file, zero hits) — the same gap as Face.

### Classification table
| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon? |
|---|---|---|---|
| `sim/personal/contest/primitives.py:11-25` | CANONICAL DEFINITION (kernel) | Home implementation | — |
| `designs/scene/social_contest_v30.md:48-61,384,497-501` | HARDCODED DUPLICATE (prose restatement, explicitly cross-cited to the kernel) | Independently states the table but names `primitives.py Stasis` as its source | Agrees |
| `params/contest.md:65,190,196` | HARDCODED DUPLICATE | Same relationship | Agrees |
| `references/glossary.md` | UNCLEAR / NO CANONICAL SOURCE — no entry | N/A | N/A |
| `designs/world/solmund_v30.md:32,36` etc. | EXCLUDED — incidental English ("ontological stasis," unrelated cosmology term) | N/A | N/A |

---

## 11. Adjudicator Armature

### Home definition
`designs/scene/social_contest_v30.md:171-177` (§4 Step 3, "The Adjudicator Armature (Stage 3 / Gate C; ED-1062)"): a hidden four-axis vector (`Evidence, Consequence, Authority, Insinuation`) carried by every adjudicator, entering resolution as "a continuous δσ-leverage shift... not a bonus die." `params/contest.md:164` (CR4/CR5/Armature section) restates identically. Code: `sim/personal/contest/armature.py` (`ArmaturePosition`, `STYLE_AXIS`, `style_axis_dsigma`, `ArmatureConfig`), consumed in `resolver.py:246-256,383-386` (`Bout.armature`, `dsigma_bonus = self.armature.dsigma(side, self.adj)`).

### Important context: "armature" is a corpus-wide reused pattern, not a fresh coinage
This term is deliberately built on a pre-existing general mechanism, not floating free: `designs/architecture/key_substrate_v30.md:99,142-153` documents a general "Conviction armature"/`armature_position` dot-product pattern (NPC-behavior-level), and `skills/valoria-module-adjudicator/SKILL.md:25` contains an explicit **naming-collision guard**: *"'armature' is a canonical term (Conviction armature, `armature_position`, Faction Meta-Armature — key_substrate §8.2). This instrument is therefore the adjudicator, never 'the armature.'"* `social_contest_v30.md:174` itself states three of the Adjudicator Armature's four axes (Evidence, Consequence, Authority) **are** "the canonical Resonant-Style vulnerability map (npc_behavior_v30.md §1.3)" reused, with only the fourth (Insinuation) a deliberate new addition — so this is an explicit, well-documented specialization of an existing corpus-wide pattern, not an independent or colliding coinage.

### Divergence
None found in the mechanical description itself across the sites I checked (`social_contest_v30.md:171-177,500-501`; `params/contest.md:164`; `armature.py`; `resolver.py`) — all consistent. **The only gap is that, like Face and Stasis, "Adjudicator Armature" has no glossary entry** (zero hits grepping the whole file for "Armature"), despite being a Gate-C-ratified (2026-07-02), currently-implemented mechanic.

### Classification table
| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon? |
|---|---|---|---|
| `designs/scene/social_contest_v30.md:171-177,500-501` | CANONICAL DEFINITION | Ratified Gate-C doc | — |
| `params/contest.md:164` | HARDCODED DUPLICATE | Independently restates | Agrees |
| `sim/personal/contest/armature.py` | CANONICAL DEFINITION (kernel) | Implements `ArmaturePosition`/`STYLE_AXIS`/`ArmatureConfig` | Agrees |
| `sim/personal/contest/resolver.py:246-256,383-386` | PULLED / REFERENCED | `from .rhetoric import ...`; consumes `self.armature.dsigma(...)` | Agrees |
| `designs/architecture/key_substrate_v30.md:99,142-153` | PULLED / REFERENCED (the more general pattern this specializes) | Cross-cited by name in `social_contest_v30.md:174` | Consistent, explicitly a shared-pattern relationship, not a collision |
| `references/glossary.md` | UNCLEAR / NO CANONICAL SOURCE — no entry | N/A | N/A |

---

## 12. Standing (the value underlying Face)

### Home definition (contest-kernel sense)
`sim/personal/contest/primitives.py:31-47`, class `Standing`: `LO, HI, START = 0.0, 10.0, 5.0`; `build()`/`strip()`/`strip_points()` methods; explicitly documented (line 68-69 in the CR3 comment block) as "contest-local ethos/standing (TRANSIENT)... built by ethos moves; feeds Readiness+leak." `Face = Standing` (line 108) — Face is a bare alias of this class, not a different value.

### A second, unrelated "Standing" exists at the corpus/design level
`references/glossary.md:110` (Part Four, Faction Stats): `Standing | — | Reputation track. Range 0–10 (exception to 1–7 scale). No in-game benefit above 7; 10 is cosmetic maximum.` This is a **persistent** faction/NPC reputation attribute, used as an eligibility gate in unrelated systems: `social_contest_v30.md:390` ("Eligible claimants: Any NPC or PC at Standing ≥ 5 in the affected faction" — Succession Contest); `designs/provincial/faction_politics_v30.md` (Heresy Investigation targeting, "rank ≥ 3 may target Standing 4+ NPCs/PCs" per my earlier read of `social_contest_v30.md §7.3`); `references/mechanical_terms_index.md:185,1166` (same 0–10 reputation definition).

### Are these the same primitive or two different things sharing a name?
They are **two different things**. The persistent faction Standing is never reset; it gates long-lived eligibility (Succession Contest claimants, Heresy Investigation targets). The kernel's contest Standing is explicitly **transient** — `primitives.py:68` labels its role "(TRANSIENT)"; `social_contest_v30.md:239,244` states "Face recovery: full restore at scene change" and "Face is a within-contest tracker that resets at contest end." A `Contestant` is built with `standing_start=Standing.START` (a parameterizable float defaulting to 5.0, `primitives.py:182`; `resolver.py:182`) — so in principle a real character's persistent Standing *could* seed a Bout's starting ethos value, but nothing in the code or prose I found actually performs that hand-off; the kernel's Standing is purely a per-bout working value that "feeds Readiness + leak" internally and is discarded/reset afterward. Post-contest consequences in `social_contest_v30.md:292` ("Disposition change with all witnesses; Reputation shift (GM-set magnitude)") name **Disposition** and **Reputation**, not Standing, as the persistent write-back — reinforcing that the kernel's Standing is not understood, even by its own home doc, as the same value as the persistent faction attribute.

### Is this collision tracked anywhere?
`references/name_collision_database.yaml:139` lists `Standing # faction attribute (also Key type — exempt)` under §2 Faction Attributes — but this exemption is about "Standing" also being a formal **Key type** in the Key-substrate architecture, a different overlap than the one identified here. I found **no ledger entry, no name_collision_database row, and no mechanical_terms_index note** addressing the specific fact that `sim/personal/contest/primitives.py`'s `Standing` class (transient, contest-local, feeds Face) shares its exact name with the corpus's persistent faction/NPC reputation attribute (glossary Part Four, `references/mechanical_terms_index.md:185`). This appears to be a genuine, previously **unflagged** naming collision — distinct from, though thematically adjacent to, the tracked Piety/Persuasion/Conviction tangle in Term 1.

### Classification table
| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon? |
|---|---|---|---|
| `sim/personal/contest/primitives.py:31-47,68-69,105-108` | CANONICAL DEFINITION (contest-kernel "Standing," transient, underlies Face) | Home implementation | — |
| `sim/personal/contest/resolver.py:182,204-234` | PULLED / REFERENCED | `from .primitives import (Stasis, Appeal, Standing, ...)` (resolver.py:15); constructs `_Side.standing = Standing(spec.standing_start)` | Agrees |
| `sim/personal/contest/faction.py:8,44-45,100-101` | PULLED / REFERENCED | `from .primitives import (..., Standing, ...)`; uses `Standing.START` as a default seed value | Agrees |
| `designs/scene/social_contest_v30.md:236,249-254` (Face/CR3 discussion) | CANONICAL DEFINITION (prose side of the same transient value, named "Face") | Explicitly cites `primitives.py Standing` | Agrees |
| `references/glossary.md:110` (Part Four) | CANONICAL DEFINITION (of the *unrelated* persistent faction-reputation "Standing") | Home glossary entry, distinct concept | N/A — not the same referent |
| `references/mechanical_terms_index.md:185,1166` | HARDCODED DUPLICATE (of the persistent faction attribute) | Independently restates the 0–10 reputation definition | Agrees with the persistent (glossary) sense; not comparable to the kernel sense |
| `designs/scene/social_contest_v30.md:390` (Succession Contest eligibility) | PULLED / REFERENCED (of the persistent sense) | "Standing ≥ 5 in the affected faction" — an eligibility gate using the persistent attribute, in the *same file* that also documents the unrelated transient kernel Standing | Internally the file uses both senses of "Standing" without disambiguating them explicitly, though context makes each occurrence's sense inferable |
| `references/name_collision_database.yaml:139` | UNCLEAR / NO CANONICAL SOURCE (addresses a different overlap) | Exempts "Standing" from Key-type collision checking, not from this specific transient-vs-persistent naming overlap | N/A — does not cover the collision identified here |

No incidental-English exclusions were needed here beyond the ordinary sense of "standing" in unrelated prose (e.g., "standing army," "long-standing"), which I did not count as hits in the game-mechanical sweep above.

---

## Cross-cutting observation (raw material, not synthesis)

Every divergence found in this batch traces back to one of two mechanisms: (1) the glossary's Part Three appears not to have been resynced since at least PP-234 (2026-04-04) despite a later claimed full sweep (2026-04-30, PP-691), and definitely not since CR3 (2026-06-01) or CR4/CR5/Armature (2026-07-02); and (2) `references/mechanical_terms_index.md` independently duplicates several of the *exact same* stale readings as the glossary (Doubt Marker's "Diverge state" wording verbatim; the AMPLIFY/DIVERGE interaction-type set), suggesting the two reference indices were built from a shared or mutually-copied source and neither has been independently reconciled against the current `social_contest_v30.md`/`params/contest.md`/kernel triad since. The Piety/Persuasion/Conviction three-way (Term 1) is the one item in this batch already carrying its own open ledger ID (ED-SC-0003) and an explicit "awaiting Jordan" status in `handoffs/HANDOFF_SC.md:100`; the Standing/Face naming overlap (Term 12) and the three glossary gaps for Face/Stasis/Adjudicator Armature (Terms 9-11) do not appear to have been filed anywhere as far as I could find.
