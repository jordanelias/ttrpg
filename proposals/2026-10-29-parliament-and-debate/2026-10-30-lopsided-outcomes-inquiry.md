# Why the social-contest kernel's outcomes are lopsided

Reference, not a plan (CLAUDE.md §0.05, §0). It explains one finding of `2026-10-30-stress-test-report.md`; it
dies with the kernel it describes. The kernel (`systems/social_contest/sim/contest/`) is **evaluated, not
adopted** (SC-05); the live game code is `modules/social_contest/roll.py`, which this does not touch.

**Evidence.** `lopsided_mechanism.py` → `2026-10-30-stress-log-lopsided-mechanism.jsonl` (53 matchup cells +
a faculty table); `lopsided_levers.py` → `2026-10-30-stress-log-lopsided-levers.jsonl` (21 lever cells + 6
narrative cells). No chosen trial count: each cell sampled until its time slice ended and logged `n`.
Source read at `73fa88d0` = `origin/main` + the stress-test commit; kernel files identical to main.

**Terms.** *Faculty* is one integer per side (default 4, 1–7 tried), the kernel's "argue skill"; it is not a
named character attribute. *Gap* is `advA − advB` at the close. *Decided* means the verdict names a side.

## 1. What the first finding actually measured

The stress test reported the weaker side's share **of decided contests** (formal 0.04%, grand 0.06% …). Three
conditions sit under every such number:

- **Both sides played the logos-only policy.** It never builds standing or room, never presents evidence.
- **Sides were bare integers**: no evidence, default standing, no pressure, no armature.
- **Conditioning on "decided" hides the middle.** For faculty 1 v 4 in `formal_contest`: committee 85.3%,
  stronger side 14.7%, weaker side 0.02% (unconditional, same cell as the lever table).

## 2. The mechanism, in the order the numbers are made

1. **Faculty → degree is concave.** Mean reception degree by faculty 1…7: 1.06, 1.48, 1.83, 2.13, 2.31, 2.38,
   2.49. P(failure) is 40.0% at faculty 1 and 6.8% at faculty 4. Most of the spread is below 4.
2. **Persuasion is additive.** Gain per advance is about 2.6 × degree × resonance × readiness, so a faculty-1
   advance is half a faculty-4 advance (0.25 v 0.50 in formal; 0.39 v 0.78 in casual).
3. **Additive means more exchanges → more determinism.** Drift grows with n, noise with √n. Exchange-majority
   venue, faculty 1 v 4, weaker side's win share at 1, 2, 3, 5, 8 exchanges: 21.9%, 13.3%, 8.8%, 6.0%, 4.2%;
   equal sides stay at 50% throughout. So the longer, grander proceedings are the more predictable ones.
4. **The verdict bands are fixed gap sizes; the gain scale is not.** `PersuasionTrack` needs |gap| ≥ 1.33
   (start 5, scale 1.5) for a decisive verdict. Equal-sides gap sd and the threshold in sd units:

   | proceeding | gain/advance | gap sd | threshold in sd | equal sides decided |
   |---|---|---|---|---|
   | formal_contest (crowd) | 0.50 | 0.47 | 2.9 | 0.5% |
   | grand_contest (crowd) | 0.50 | 0.55 | 2.4 | 1.6% |
   | royal_audience (expert) | 0.97 | 0.91 | 1.5 | 15.1% |
   | church_tribunal, neutral start | 1.13 | 1.22 | 1.1 | 26.5% |

   How decisive a proceeding is comes from `resonance × readiness` (judge profile × appeal played), not from
   anything the proceeding declares. Changing only the appeal both sides play moves formal-contest equal-side
   decided share from 0.5% (logos) to 35.4% (pathos) and 36.3% (exploiter); grand 1.5% → 45.7%.
5. **Where it is decided, it is decided on the drift side.** Formal, faculty 1 v 4: the stronger side needs
   1.1 sd, the weaker side 3.9 sd. The "weaker share of decided" is a tail-versus-tail ratio, so it is near
   zero even though the weaker side is not "crushed" — it mostly gets a committee.
6. **`church_tribunal`'s seat asymmetry is the track start, nothing else.** Start 6.0 (canonical): A wins
   84.7% of decided contests at equal faculty. Start 5.0, everything else unchanged: 50.0% (95% interval
   48.6–51.4). A needs a gap of +0.67 (0.55 sd), B needs −2.0 (1.65 sd). Control: in the symmetric
   venues move order gives no edge (casual 4 v 4, A share 0.4995).
7. **The upset channels exist and act as a switch.** Faculty 1 (side A) v 4, A's share of **all** contests:

   | A is given | formal | royal | church |
   |---|---|---|---|
   | nothing | 0.02% | 0.6% | 1.9% |
   | standing 8 | 0.02% | 7.1% | 13.2% |
   | institutional pressure 1.0 | 1.7% | 9.6% | 20.9% |
   | one evidence item, weight 1 (control) | 0.03% | 1.2% | 5.0% |
   | one evidence item, weight 3 | 12.1% | 54.5% | 60.9% |
   | two evidence items, weight 3 | 82.2% | 99.9% | 99.3% |

   Evidence is deterministic, readiness-free and ignores faculty; at the 3.0 cap one item is worth about 1.5
   of gap, twice the whole faculty 1→4 drift. Weight 1 is the control for the policy change that
   accompanies evidence (`advocate`): it barely moves anything.

## 3. The narrative construction

*What story does each proceeding tell, and does the mechanism tell it?*

- **Single exchange (casual, personal appeal).** A brief clash decided by one roll each: weaker side 21.6%.
  The story and the mechanism agree: it is volatile.
- **Negotiation (up to 3 exchanges).** "Talking longer favours the skilled": 8.6%, and §2.3 shows that is the
  √n law, not a tuned value.
- **Crowd proceedings (formal, grand).** The story is oratory that moves a crowd. The crowd responds mostly
  to its own character (pathos-heavy, discipline 0.3), so a logos argument earns 0.5 per advance against 1.25
  for pathos. The only public cue, `venue_brief`, prints "rewards logos; favours past-ground argument"
  identically for formal, grand, royal and church. The "past-ground" is a tie-break (the three tense weights
  are equal for these venues), and the crowd's actual taste is hidden by design (the code comment says the
  judge's leaning is "learned through play"). A fixed-policy harness cannot learn, so what it measures is the
  cost of not learning.
- **Royal audience and church tribunal.** Their declared asymmetries are mostly not in the mechanism. The
  proceeding rows carry `roles` ("crown objects", "inquisitor proposes"), an exchange **minimum**, and a
  derived audience `resistance`. `dictionaries.PROCEEDINGS_TABLE` copies them for display and cross-checks,
  but resolution reads none of them (`resistance` is documented metadata-only at `wrapper.py:75`; no code
  reads `roles` or the minimum). Every proceeding plays A-first strict alternation, and every tribunal runs
  the maximum five exchanges although the flavor text says "the Inquisitor sets the length"
  (`dictionaries.py:546-550`).
  The authored story is a **two-part balance**: the tribunal's track "starts BIASED against the accused …
  whose resistance is halved to compensate", and the royal petitioner's "uphill fight is eased by HALVED
  resistance" (`dictionaries.py:539-540,547-548`). The code applies the bias (start 6) and not the
  compensation, so the 84:16 split is the biased half of a designed pair. (`wrapper.py:38-40` also says
  "halved" is "for the advantaged party", the opposite reading.)
- **Guild arbitration.** A bench of five names a side every time (no committee outcome; weaker 12.3%), while a
  crowd before the same two parties produces a compromise 85–99% of the time. The same dispute has two
  different outcome spaces depending on the room.

### The story-telling layer misreads the verdicts it is given

`narrative.summarize` was written and tested for winners `'a'`/`'b'`; the track proceedings return
`A_decisive`, `committee`, … (checked on 25,000–37,000 contests per proceeding):

- `render()` names the band as the winner: "committee took it by 15%", "B_decisive led from the opening".
- `classify` treats any non-`'a'` winner as side B, so seat decides the shape: with equal faculty (royal,
  A_decisive 1,818 v B_decisive 1,788) A's verdicts are 100% CLEAR_WIN and B's are 45% ROUT; A is never a rout.
- 43% of formal-contest committee outcomes (faculty 1 v 4: 11,011 of 25,551) are narrated "ROUT … never trailed".
- Every rendered line ends "on accumulated pressure": the decisive-appeal field is empty for band results,
  so the "what worked" signal that teaches a player never appears.

The live module does not call it; only the kernel's own tests do, with `'a'`/`'b'`. This is a flaw in an
evaluated kernel, stated because its output is what a player would read.

## 4. Verdict, and what is not shown

Lopsidedness here has five separable causes: (a) additive persuasion (intended-looking, and standard);
(b) gain scale unrelated to band size, which makes a proceeding's decisiveness accidental; (c) concave
faculty, a bare-skill harness and a fixed logos policy; (d) the tribunal's start offset geared up by a small
gap sd, with its designed compensation (halved resistance) unplumbed; (e) a narrator that cannot describe a band verdict. (a) and the tribunal's direction are plausibly
intended; (b), (c)'s harness conditions and (e) are not choices anyone made visible.

Not shown: any effect of armature or style (untested); sides built from the host `World` rather than
integers; both sides holding evidence; seat swaps beyond the earlier 4 v 1 cells; what the tribunal's split
would be with the halved-resistance compensation wired (that code does not exist, so it cannot be measured). Rates have `n` and 95% intervals in the logs;
the narrowest is formal equal-sides decided (n = 34 decided, interval 0.37–0.69).
