# REFUTE — massbattle-general-duel-decap

**Finding claim:** A combat-optimised PC risk-free-decapitates any enemy army via repeated General
Duels; ED-898 removes downside, incapacitating the enemy general zeroes Command and floors the whole
army → "the general is the battle" becomes a dominant mass-layer bypass flattening all of Part A.
Cite: scale_transitions_v30 §3.7; mass_battle_v30 §A.1, §A.5 (ED-898), §A.6/PP-273. Criterion Ω,
diagonal, P1, NEW.

## What the text actually says (working-tree reads)

1. **§3.7 (scale_transitions_v30)** — Mass→Personal (General Duel): "Personal Action available at
   Phase 5 (Priority 8). Limit: 1 exchange per battle turn. General's Command Rating suspended while
   in personal combat (PP-232). Maximum 5 exchanges before forced disengage or incapacitation." The
   infill §3.7 is EMPTY (header only) — no elaboration.
2. **§A.5 (mass_battle_v30)** — "General in personal combat: suspends all Command effects.
   Re-establish command with Command check Ob 2 in Phase 1 of any subsequent turn." AND: "Mass battle
   pauses during personal combat (unilateral). If one general enters personal combat, mass battle
   holds at current state." Bilateral (PP-506): "If both generals enter personal combat simultaneously
   … mass battle does NOT freeze — both armies fight uncommanded: PP-273 floor (1D minimum per unit),
   Line formation, no tactics available … until each general re-establishes Command (Ob 2)."
3. **ED-898 (§A.5):** No mass-battle mechanic kills a player/named character; worst outcome =
   incapacitation and, if their side loses the field, capture. Two-stage: Stage 1 Command halved
   (floor, min 1), Morale floor suspended, stabilise Medicine Ob 2 (1-turn window); Stage 2 fires
   *start of following turn's Phase 5 if not stabilised* → Command 0, uncommanded.
4. **PP-273 (§A.6):** uncommanded units fight at 1D floor — weakened, NOT destroyed.

## Refutation — five load-bearing errors in the claim

**(a) No forcing mechanism — the target must consent.** Grepped mass_battle_v30, scale_transitions_v30,
and designs/scene/ for single-combat / challenge / "must accept" / force-general: NONE exists. A "duel"
requires BOTH generals to enter personal combat (bilateral, PP-506). A unilateral entry merely PAUSES
the whole battle (§A.5) — there is no opponent to strike, and the PC's own command is off. So a
command-dominant enemy general — the exact Command=7 case the axiom describes — simply declines
(never enters personal combat) and keeps commanding. "Decapitate ANY enemy army" is therefore false:
the mechanism is unavailable against an unwilling target.

**(b) Own-command suspension is symmetric.** §A.5: entering personal combat "suspends all Command
effects" for the PC too. In a bilateral duel BOTH armies drop to PP-273 1D floor / Line / no tactics.
The PC surrenders their own generalship advantage for the duel's duration (up to 5 turns). For a
combat-optimised PC-general who is *also* Command-strong, that is a large sacrifice — the opposite of
a free win. The bypass is not a one-sided lever; it neutralises both sides' Command simultaneously.

**(c) "Risk-free" conflates no-death with no-downside.** ED-898 removes DEATH, not consequence. The PC
must WIN the personal combat to incapacitate the enemy. Lose it and the PC is themselves
incapacitated and — if their side loses the field — CAPTURED, a world-layer event (ransom /
imprisonment / escape). Capture is a real, heavy downside. The finding's "removes all downside" is
unsupported by ED-898's own text (which frames capture as the worst outcome, deliberately kept in
play).

**(d) Not instant-zero.** Incapacitation ≠ Command 0. Stage 1 only *halves* Command (min 1); Stage 2
(Command 0) fires only the *following* turn's Phase 5 and only if the enemy fails to stabilise
(Medicine Ob 2, 1-turn save). So even a won duel yields a turn of halved-but-live command plus an
enemy save before any "floor."

**(e) Floored ≠ flattened.** At Command 0, units fight at 1D floor (PP-273) — degraded, still fighting;
rout/cascade must still resolve. And by ED-898's symmetry the PC cannot kill the enemy general either;
"capture-if-field-lost" requires the PC's side to actually win the field, which an
everyone-uncommanded duel does not guarantee.

## Intent evidence (DELIBERATE, safeguarded)

- **"The general is the battle" is an explicit design axiom** (§A.1: "Command asymmetry is
  intentional… The general is the battle"). Not an accident.
- **ED-898 is an explicit Jordan directive (2026-06-01)**; ledger entry confirms mechanical
  magnitudes/timing unchanged, "fictional outcome only," capture deliberately retained as worst case.
- **The general-in-personal-combat model is a stack of deliberate safeguards:** PP-232 command
  suspension, PP-506 bilateral uncommanding (ED-441 specifically closed the bilateral case), PP-273
  1D floor, 1 exchange/turn, max-5-exchanges cap, Ob-2 re-establish. This is an intentionally bounded
  sub-system, not an open exploit.

## Residual (thin, not the claimed P1)

There IS a small real design space: a LOW-Command / high-personal-combat PC-champion could profitably
trade little own-command to neutralise a Command-strong foe — BUT only if the foe consents, and the
foe with the command advantage is precisely the one who won't. Whether the enemy AI declines is engine
behaviour not written in the (empty) §3.7 infill — a minor spec/Godot gap, and arguably the intended
*legible* drama (a small faction's champion challenging a great general). Worth a designer glance; far
from a Ω-collapsing dominant strategy. Revised severity P3.

## Verdict
REFUTED. Intent DELIBERATE (safeguarded). Not tracked as a defect (nothing to track); the underlying
axiom + ED-898 are ratified canon. Revised severity P3 (thin consent/AI spec-gap residual only).
