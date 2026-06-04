# Appeal Modulation — design proposal (F1 fix + context/adjudicator)

**Status: PROPOSAL** (mechanical/systemic tier — Jordan-vetoable). Implemented and tested locally; **not committed**. Recommend audit + stress before ratifying.

## What
An appeal's effect on the verdict is no longer flat. A successful appeal moves the verdict by
`MERIT_SCALE · deg · resonance · readiness`:
- **Resonance** — how much *this* proof moves *this* adjudicator *here*:
  `effective_weight = (1−leak)·role_weight[appeal] + leak·character_weight[appeal]`.
  - **role_weight** comes from the **mode** (the discursive context's demand): forensic leans logos, deliberative leans pathos.
  - **character_weight** is the **adjudicator's** disposition over the three proofs.
  - **leak** is how far the adjudicator drifts from role toward character: it rises as **discipline** is low *and* as you **build ethos** (rapport draws them off the role's guard). So the role↔character contradiction is navigable — build ethos to unlock a sympathetic character beneath a hostile role.
- **Readiness** (the F1 fix) — built standing (ethos) and room (pathos) make your appeals land; floor < 1, so raw logos-spam stays weak and you must build before you close.

## Why (grounding)
- **Top-down (corpus):** the genres privilege different proofs (logos in court, pathos in the assembly, ethos in appeal); the regime determines which genre is load-bearing; the adjudicator is a person whose character can sit in tension with what the office requires. This model is the mechanical form of those claims.
- **Bottom-up (sim):** the stress test showed logos-spam strictly dominant because appeals were inert. The modulation removes the universal dominant strategy.

## Results (probe + 31/31 tests)
- **Symmetry preserved** — identical contestants ~50/50.
- **Context modulates** — logos beats pathos in the forensic venue (0.97); pathos beats logos in the deliberative venue (0.98). Same matchup, flipped by context.
- **Adjudicator modulates** — in the same forensic venue, logos wins before a by-the-book logos judge (0.97) but loses to pathos before a pathos-character judge (0.98).
- **Role↔character tension navigable** — the exploiter (build ethos → unlock character → press pathos) beats logos-spam against a high-tension judge (0.97) but loses against a low-tension judge with no contradiction (0.98).
- **F1 fixed** — build-then-close now beats logos-spam (0.59–0.73), where it was 0.000.
- Defeat-conditions intact; contests resolve.

## The authored boundary (important)
I built the **mechanical frame** for adjudicator modulation: `character_weights`, `discipline`, the role↔character `tension`, and how they enter resonance. The **specific adjudicators** — their actual virtues, ethical frameworks, style, and the particular nature of each role's contradiction — are **authored, Jordan's**. The profiles in the tests (by-the-book judge, pathos judge) are illustrative `[SEED]`s, not canonical characters. Richer modelling (e.g. virtue/consequentialist/deontological frameworks responding to argument *content*, not just the three proofs) is an authored design extension on top of this frame, for Jordan to drive.

## Open tuning (feel calls)
- Matched-appeal decisiveness is high (~97% — wrong-appeal-for-the-room rarely wins). Softenable via reception variance or flatter resonance weights if a more forgiving feel is wanted.
- The `[SEED]`s (MERIT_SCALE 2.6, threshold 5, budget 8, readiness floor 0.35, leak unlock 0.5, role/character profiles) are a working point, not a tuned optimum.

## Recommended next steps
Audit the added mechanism for NERS-N/E (is resonance+readiness necessary and elegant, or over-built?), stress-test the modulation at extremes, then ratify + commit if it holds — the same cycle the corrected core went through.
