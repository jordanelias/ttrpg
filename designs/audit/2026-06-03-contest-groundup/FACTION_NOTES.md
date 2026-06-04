# Faction-action testing — engine in the Parliamentary context

**Scope.** `faction.py` is an ADAPTER for exercising the contest engine against the shape of the
canonical Parliamentary action (`faction_layer_v30 §5`). It is **not** a canonical change — the faction
layer keeps its ratified resolution (§5.5 Rebuttal roll, §5.3 Mandate-weighted vote, §5.4 thresholds).
Mapping: proposer vs target argue before each faction-voter; each casts its Mandate-weighted vote for
whoever persuades it (Church adds ⌊CI/20⌋, §5.3); the motion passes at the venue threshold
(Censure/Majority 0.50, Outlawry/Supermajority 0.60). Levers: target rebuttal (its argue strength),
fixed-lean AI blocs (§5.8), institutional/public pressure on the body, and a documented case.

## Evidence calibration (tuning, 2026-06-03)
A weight sweep on a Mandate-2 petitioner's Outlawry found:
- **A hostile body is a wall evidence cannot climb** — 0.00 pass at *every* evidence weight (the votes
  aren't there; disposition dominates). Faithful and bounding.
- **Over-potency was specific to a persuadable body at full weight** — scale-1.0 evidence carried a weak
  petitioner to certainty (1.00). **Weak evidence is worse than none** (presenting feeble proof wastes
  the floor — a real gamble, since value is hidden).
- **Fix (adapter-level; engine's validated 1v1 evidence untouched):** `case(strength)` weights chosen so
  a *solid* case lifts a persuadable body ~+0.2 (0.54→0.77), a *strong* case →0.93 (carries, never
  certain), and nothing moves a hostile body off ~0.00. The supermajority keeps even a strong case short
  of certainty.

## Emergent findings (insight-first)
1. **Body disposition is the master variable.** A proposer who pitches to the room sweeps (matched
   style → 1.00); a mismatched one is crushed (→0.01). Faction politics = who is in the assembly and
   what moves them.
2. **Mandate carries routine motions; case + allies + style win the hard ones.** Faculty saturates fast
   for Censure (the proposer's own Mandate does the work); Outlawry/close bodies need persuasion.
3. **Graded rebuttal frontier** (proposer × target faculty, neutral body, Outlawry): a strong target
   defeats a weak proposer outright (f2 prop v f4+ target → 0.00); matched faculty hovers ~0.50; the
   surface is smooth, not a cliff. §5.5 rebuttal works decisively at the extremes.
4. **Levers act differentially at the swing** (balanced body, Censure ~0.5 baseline):
   - *Pressure* (institutional/public toward proposer) tilts the whole body — strongest lever (0.76→0.96).
   - *Style-match* is decisive — a proposer switching to an axis no voter wants (ethos into a logos/pathos
     body) crashes (0.76→0.24).
   - *Rebuttal* (stronger target) erodes the margin (0.76→0.67).
   - *Evidence helps only on its own axis* — logos-evidence does **not** swing pathos voters; it reinforces
     voters already won. Evidence is not a universal solvent.
5. **Diagnostic contrast.** Routing the motion through the engine makes the outcome a smooth, multi-factor
   function (faculty matchup × body × style × evidence-axis × rebuttal × pressure) the player can move —
   versus the bare 2D faction-stat roll (P≈0.26, one throw, no recourse) the resolution diagnostic flagged
   on pivotal/irreversible faction actions. This is the Lesson-3/4 correction demonstrated in context.
   A matched-faculty Outlawry near 0.50 is the *good* kind of close (aggregate of many voters + influenceable),
   not the diagnostic's fragile single-die binary.

## Boundaries / not yet modeled
- **Non-adversarial motions** (Subsidy, Treaty Ratification) have no target to rebut; the two-party model
  needs a different treatment (one-party persuasion vs the body's default, a per-voter ProofBar).
- **Voters are independent** — no coalition/bandwagon dynamics (`social_contest §9.2` has coalition structure).
- **Sacred Veto** modeled only as a fixed "no", not the canonical override-the-tally block.
- Specific canonical faction stats/dispositions (Crown/Church/Hafenmark/Varfell) not yet wired from canon.

## Wiring + build on PersuasionTrack (2026-06-03)
- **Banded votes (wire).** `band_of(share, threshold, margin)` adds canon's committee/referral outcome: a
  motion within ±0.06 of its §5.4 threshold is too close to decisively resolve → **committee**; clear of
  it → pass/fail. So a clear majority passes (strong Censure 98.8% pass), a genuine near-tie is referred,
  and a *solid case* lifts a weak Outlawry to the brink (share ~0.61 vs a 0.60 bar) → ~80% committee — the
  case earns a hearing, not an automatic pass. Respects §5.4 thresholds while supplying §10's committee zone.
- **Succession (build).** `succession()` resolves two leading claimants on the Persuasion Track into §7.2
  bands: **unified** (track ≥9/≤1), **decisive** (≥7/≤3 — single winner takes leadership), **split** (4-6 —
  faction split, majority share per §7.2.1: track 4→0.60, 5→0.55, 6→0.50). Emergent + faithful: matched
  claimants fracture the realm (91.5% split — Compromise is canon's designed major outcome), skill shifts it
  toward a clean takeover (f6v2 → 40% decisive, f7v1 → 56% decisive + 18.5% unified). Downstream split logic
  (stat division by ratio, Stability floor 3, territory/treaty split, schismatic identity by Conviction) is
  NOT modelled — `succession()` returns the engine verdict + ratio only.
- **Canon observation (not changed):** §7.2.1's ratio table is mildly counter-intuitive (track 4→60/40 more
  lopsided than track 6→50/50). Implemented literally; flagged for Jordan, not altered.

## Coalition pooling (§10 BG vote) — closes #4 (2026-06-03)
`coalition_vote(sides, lobby, scale)` implements canon §10: factions declare pro (Side A) / anti (Side B) /
abstain; each side's pool = sum of its Mandate; the pools clash and move the Persuasion Track (start 5 ±
lobby, ED-621 clamped), read in bands → pass / committee / fail. **This is the concrete proof of review
finding #4's resolution: a multi-faction coalition pools into ONE side on the two-party engine — no N-party
spine is needed.** Emergent + faithful: coalition size leans the vote, a bloc of small factions can edge a
strong lone power (5 vs 6 → leans fail), balanced coalitions are symmetric and committee-heavy, lobbying
tilts a dead heat toward passage, a high-Stability abstention raises the committee rate. A moderate Mandate
edge lands in committee on average — decisive passage needs clear dominance or lobbying/genre, which is
canon's §10 design. (Single pooled roll per side → BG-scale variance is intended; the per-voter `vote()` is
the finer/personal-scale resolution.)
