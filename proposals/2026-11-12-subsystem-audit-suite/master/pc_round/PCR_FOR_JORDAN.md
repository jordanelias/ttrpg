# PC round — for Jordan

## Status: REFERENCE (the A-101 round lane's register for Jordan; form of `unified/DECISIONS_FOR_JORDAN.md`; resolves nothing at runtime, CLAUDE.md §0.05)

## Read at: the working tree of 2026-11-12. Lane: `master/pc_round/` (A-101).

**No question survives the five-step ladder.** Every choice the round needed was answered by your own words
(A-101 and its two clarifications: the 4–10 seconds caps the exchanges roughly; boxing and fencing are the model),
by your earlier combat rulings written in the engine, or by the engine as built. They are listed below so you can
reverse any of them with one line; each says what the game does under the suite's reading. The full reasoning is
`PC_ROUND_SPEC.md` §2.

## Taken by the ladder (reversible on your word)

| # | what was decided | how it plays | basis | to reverse |
|---|---|---|---|---|
| 1 | **Initiative does not carry between rounds**; it starts even at every round. (`DECISIONS_ANSWERED.md` A-101's summary lists initiative among what carries; your quoted words name nothing, and your 2026-06-05 cut in the engine, "initiatives start even", stands.) | Separating resets who holds the upper hand, as a fencing halt resets right of way; what pressing leaves behind is the opponent's lost poise and stamina, which do carry | ladder 1 (your 2026-06-05 cut) and 4 (fencing, boxing) | "initiative carries": the round's state gains it, and every fight's numbers move |
| 2 | **A round has at most four exchanges** (the engine's existing cap). One exchange is one attack and the defence against it; either fighter may attack next | Most rounds end in one or two exchanges, when an attack is parried or avoided cleanly; a fighter who lands keeps pressing (a combination) until a clean defence or the fourth exchange | your indicator (4–10 s ≈ one to four exchanges at an estimated 1–2 s each plus closing and separating); the probe (`PC_ROUND_SPEC.md` §1.1) | name another cap (3 or 5 are the sensible neighbours) |
| 3 | **A landed hit does not end the round; a clean defence does** (boxing's combination, fencing's phrase that ends on a parry) | As above | your own design of 2026-06-03, written in the engine ("a faster fighter can land several hits in a single turn") | "a hit ends the round" (pure fencing): rounds get shorter and more numerous |
| 4 | **A clean disengagement or a re-opened measure ends the round** (today the engine lets the fighters part and close again inside one round) | A spear or staff that breaks away from a sword at close quarters ends the round; both get the between-round breather, and the next round begins apart. About 4–5% of rounds where reach differs; none in even-reach fights | A-101: "then disengage/create distance again" | "keep the second closing inside one round" |
| 5 | **No seconds are counted anywhere.** Fatigue is spent per attack and recovered per separation, as the engine does now; a duel inside a battle does not advance the battle's clock | A player never sees a duration; a narrator may say "a few seconds" | your clarification ("not absolute but an indicator") | — |
| 6 | **The season's own "round" is renamed in prose to a "lap"** (one pass in which everyone deliberates, acts and is witnessed, several per season), so "round" means only the fight's | Nothing in play changes; the code's `Claim.round` keeps its name until a rename batch, if v12 takes it | the word test (one word, one meaning); your A-101 claims "round" | name another word for the season's pass |
