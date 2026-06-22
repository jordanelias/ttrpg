# Personal Combat — Consolidated Loose-Ends Register
**2026-06-19 · status: PROPOSED working master (Jordan-vetoable) · a synthesis over live sources, not a replacement**

`[SELF-AUTHORED — bias risk: consolidates the Claude-authored combat audit corpus + this session's D-A work. "Closed/wired" claims are SHA- or ledger-cited; system verdicts inherited from the source audits.]`
`[as_of: live HEAD after ED-1029 (40a3a321) + banner commit (2967f7ee), 2026-06-19. Sources: combat decision docket 2026-06-17 (RATIFIED, ED-1029); comprehensive_analysis_personal_combat 2026-06-09 (F1–F7); combat_reconciliation_plan 2026-06-16; ratification_and_deprecation_proposal 2026-06-02; editorial_ledger.jsonl.]`

Scope: **personal combat (`combat_engine_v1`) only.** Mass battle (including ED-811), fieldwork, and social contest are excluded.

## §1 — TRIAGED (directive 2026-06-19: "test §1 until it makes sense")
- **Wound model N + magnitude** — **SETTLED (tested).** N=4 (vs N=3: N=4 is exactly coherent — wounds fire at identical %-health-lost 44/75/94/100 across every build; N=3 drifts ~1% on rounding — and gives 4 graduated states vs 3, first wound at 44%). WI = round(2.5·End + 1.5·Str + 1.0·Spi) (your 5:3:2 ratio); Health = WI×4 (avg 76, tank 140); gates (2i−1)/4·WI consumed largest-first. Verified against your worked example (WI=16, N=4 → 28/48/60/64). **Lands coupled with the §4 attack/defense asymmetry fix** — N=4 allows up to −4D before felling, which deepens the −1D-per-wound mutual-stall; the asymmetry fix resolves it, so they co-land or the draw rate regresses. `[ASSUMPTION: weights at exact 5:3:2 per your ratio; magnitude (Health ~76) re-tunes via DMG_SCALE when D1 lands — bottom-up: verified gates/coherency; top-down: accelerating-collapse injury model. Jordan-vetoable.]`
- **ED-864** — scene-combat C4 direction + Contest! integration (6 records, 2026-05-17): design-*direction*, not a calibration — needs its own focused pass. (ledger ED-864)
- **D8 — new traditions** — **HELD (yours).** Creative-world authorship (the urumi rigidity axis etc.); no test authors a tradition's identity. Per the project-owner contract this stays parked for you, even under "test §1." (docket D8)
- *(moved out by the triage: **D2** → rides D1 (§2); **F7** → subsumed by D3 (§7); **ED-879** → mooted (§7).)*

## §2 — RATIFIED (ED-1029), IMPLEMENTATION PENDING (engineering + parity re-validation)
- **D1** continuous weapon-vs-armour transmission model replaces RESIST/DELIVERY/HEFT/ADEF — **re-bases this session's D-A damage reshape** (intent survives; coupling numbers + DMG_SCALE/~5-hit calibration recomputed). (docket D1)
- **D3** continuum degree + saturating quality replaces the 4-band degree + QUAL{.35/1.0/1.5} — supersedes the M-QUAL band model. (docket D3)
- **D4** composite pool recompute (experience / tradition / stamina / focus) — **A6 σ-leverage parity recal required first**. (docket D4)
- **D6** tradition representation → S3⊕S4 (abilities qualitative + channels as player-allocated affinity budget). (docket D6)
- **D7** ability schema (trigger / cost / prereq) + the ~55-ability library as the composable layer (library = your curated content). (docket D7)
- **D5** disposition-as-selection layer — **unbuilt**; scope-then-build. (docket D5; reconciliation #2)
- **D9 / F1 / ED-911** ranged + group (>2) + thread-in-combat have **no engine resolution** — build a path or declare a retained-canonical seam. *(The system NERS R-FAIL driver.)* (docket D9; comprehensive F1; ledger ED-911)

## §3 — MECHANICAL RESIDUALS (go — no decision needed)
- **M1** finish eff_cw routing — 5 residual channel_weight sites in wrapper.py (systems.py 18/18 done). (docket §C M1)
- **M2** drop the dead POOL_FLOOR branch (History≥1 ⇒ pool ≥7 > 5; floor never binds). *(Closes/moots ED-879 if the floor is truly dead.)* (docket §C M2)
- **M3** dead seize lever (vorschlag / sen_no_sen point at a baseline-dead cut lever) — recommend **retire** (micro-CANON, vetoable). (docket §C M3)
- **M4** wound-sweep re-confirm under the μ-shift (Class-A −1D not re-measured post-shift) — **overlaps this session's wound work**. (docket §C M4; comprehensive F5)
- **F3** annotate derived_stats §4.2 stamina cost-model with an engine-supersession note (doc-only; no behavioural surface). (comprehensive F3)
- **F5** ledger entry ratifying the 3 post-ED-904 commits (wound −1D wiring, deb405b944 — measured working). (comprehensive F5)
- **F6** doc-drift cleanup: README "canonical-candidate" line; r1 Class-C pool label (the ED-901/903 flip never landed in the subdoc); derived_stats. (comprehensive F6)

## §4 — THIS SESSION'S D-A WORK (post-06-17, to land)
- **New wound model** (Health=WI×N, graduated bunched gates, health-based felling) — supersedes ED-1021; pending §1 N+magnitude, then one commit (core DMG_SCALE + r2 + derived_stats §4.1 re-propagation + new ED).
- **Attack/defense wound asymmetry** — the ~50% multi-bout mutual-stall fix (defense degrades faster than offense; boxing land-vs-thrown decay, du Picq) — **not yet prototyped**.
- **D-A damage re-base** onto D1's gradient — the first implementation step of §2; gated on the D2 magnitude call (re-tuning twice otherwise).

## §5 — MAGNITUDE TUNING (post-ratification, non-blocking) — ratification_proposal §4
longsword-vs-spear (19 vs ~40 target) · longsword-vs-plate magnitude · A1 mail dials · feint-vs-elite-reader floor (~5%, slightly over-punished) · autonomous choke / lunge / feint decision policy (states wired, not engine-chosen).

## §6 — CARRIED OBSERVATIONS (not defects — feel questions)
sabre mirror draws ~80% (open feel question, 2026-06-06) · read-dominance Cog/History > physical (an A6 balance tune; the μ-shift *compressed* spans, didn't widen them) · wound −1D per-roll non-uniformity (peak −9.7pp at pool 5→4; intended and bounded).

## §7 — CLOSED / WIRED (recorded so they are not re-opened)
- combat_engine_v1 CANONICAL (ED-900); combat_v31/v32 DEPRECATED (ED-900); combat_v30 PARTIAL, lore retained; params/combat deprecated 06-04.
- Combat decision docket RATIFIED (ED-1029, 2026-06-19).
- **F4** μ-shift / effective_ob seam WIRED (ED-934, commit 15269f3c) — declared method now matches the implementation.
- **F2** eff_cw channel wiring 18/23 live (M1 finishes the last 5); channel-abilities (misura / atajo / Stärke-Schwäche) fire.
- P_auth (pob_frac / mass inputs) WIRED; atk_sig → Concentration WIRED (ED-934 / 15269f3c).
- **ED-870** PP-717 Agi×2 propagation — **mooted**: the engine pool is `max(5, History+6)` (ED-901), never Agi×2; the drifted docs (combat_v30 / params/combat) are deprecated. Verify-and-close.
- **F7** crit saturation (pool-12, 74% overwhelming) — **subsumed by D3**: the continuum + saturating quality replaces the 4-band model that produces the top-band saturation; resolved under D3, not a separate ED-906 bar.
- **ED-879** out-of-bounds × Pool-Floor-5 — **mooted (tested 2026-06-19)**: OOB feeds `atk_sig` (wrapper.py:139), not the pool; the floor (5) never binds (pool ≥ 7). No interaction exists; M2 removes the dead floor.

`[CONFIDENCE: high on structure, status, and authority (all source-cited); medium where the source itself flags it — F7-vs-D3 subsumption, ED-870/879 moot-pending-verify, and the comprehensive's 06-09 numbers pre-dating the μ-shift.]`
`[GAP: the F4 / P_auth / atk_sig "wired" claims are inherited from the docket §A SHA cites, not re-grepped this session.]`
