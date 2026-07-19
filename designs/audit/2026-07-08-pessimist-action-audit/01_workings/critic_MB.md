# Inverted Critic Pass — Lane MB (Mass Battle)

**Method:** independent Sonnet pass, read-only, judging as-if-built per the charter's cardinal rule
(`designs/audit/2026-07-08-pessimist-action-audit/00_grounding/00_charter.md`). Of the 13 dossier
rows, 12 are already KEEP; only one is condemned (REFINE). That one gets the full steelman; a
handful of KEEPs are spot-checked for over-generosity per instructions.

---

## Condemned action: Tactic: Concentration (§A.8) — isolated finding

**Dossier verdict under review:** REFINE — "reframe as terrain/mismatch-conditional rather than
general-purpose, don't cut the underlying doctrine."

### Steelman attempt

Read the source directly (`designs/provincial/mass_battle_v30.md` lines 478–500):

- The tactic table lists Concentration at **Ob 1 — the cheapest tactic in the menu**, tied only with
  Refused Flank. Every stronger/more-reliable tactic costs more (Envelopment 2, Feigned Retreat 3,
  Hammer & Anvil 3, Ambush 4). A menu that prices its narrowest-window tactic at the *lowest* Ob is
  already internalizing the win-rate risk the dossier's finding surfaces — this is Ω-d ("pays what it
  buys") working correctly, not failing. A cheap tactic that is usually weak and occasionally decisive
  is a completely standard risk/reward menu entry (a "long-shot, low-cost" pick), not a design flaw.
- The tactic's own named counter is **"Flanks exposed."** The simulation finding the dossier cites
  (PP-508/ED-358: split beats concentration by 9–45pp) is not new information about imbalance — it is
  the *measured effect of that counter actually working*. A "named counter" system, by construction,
  means the countered tactic loses when the counter is exploited. The very next row up in this same
  docket (Tactic Declaration §A.8 menu, overall — KEEP) praises this menu specifically *because*
  "every entry has a named counter... keeps every entry from being a free lunch." You cannot credit the
  menu for Concentration having a real, biting counter and then condemn Concentration for that counter
  actually biting. That is an internal inconsistency within the dossier's own two adjacent rows.
- The doc already states the two narrow windows where Concentration is correct (Command Ob 4-5 vs 2
  mismatch; Narrow Pass terrain forcing single engagement) **in one paragraph, already canonical**
  (ED-358 resolved, PROVISIONAL marker stripped per ED-767). That is a one-read-legible conditional
  ("split usually wins, except under X or Y") — Q-elegant is not actually failed here; the restatement
  already exists in the corpus and is exactly one sentence.
- Criterion mapping problem: the dossier invokes Ω-d ("every action pays what it buys," in reverse) to
  flag a *weak* tactic. But Ω-d as bound by the charter (§2: "non-dominance") polices tactics that are
  **too strong for free** — a strictly-best no-brainer. It does not, on its canonical text, license
  flagging a tactic for being *situationally weak*. Reading it "in reverse" to also catch underpowered
  picks is a criterion extension the charter's "bind only to the canonical vetting framework — no new
  criteria" (§2) does not authorize. A menu is expected and *desired* to contain some niche/specialist
  entries whose value is terrain- and matchup-gated — that is what rewards battlefield reading, and is
  the entire point of pairing Concentration with the doc's own guidance that "the primary counter to
  enemy splitting is... Narrow Pass terrain or Feigned Retreat to disengage and re-concentrate" (line
  499) — i.e. Concentration is designed to combo with Feigned Retreat and terrain choice, not to stand
  alone as a context-free pick.
- Q-robust's "three viable approaches" bar operates at the decision-node/menu level, not per-entry.
  With 6 named tactics, 5 of which the dossier itself already rates strong in general play, the bar is
  exceeded regardless of Concentration's narrower profile; a 6th, situational, cheap-to-take entry adds
  richness, it does not "undermine" the bar.

### Outcome

**OVERTURNED-TO-KEEP.** The underlying doctrine (mass-of-force, real historical precedent) was never
in question even in the dossier's own REFINE text — but on inspection the "trap pick" framing doesn't
survive: the low Ob cost already prices the risk, the win-rate deficit is the intended operation of the
tactic's own named counter (a property the dossier credits the parent menu for elsewhere), the
conditional-use guidance is already stated in one legible paragraph in canon, and the invoked criterion
(Ω-d in reverse) is not actually licensed by the charter's bind-only-to-canonical-criteria rule. Fold
this back into the parent "Tactic Declaration (§A.8 menu, overall)" KEEP as a single unified row; the
isolated finding does not stand as an independent subtractive verdict. (A genuinely trivial, non-verdict
polish note: the two-condition caveat currently lives in prose below the table, not inline in the table
itself — worth a one-line table-footnote for player-facing legibility, but that is a documentation nit,
not grounds for REFINE.)

---

## Spot-checks on KEEP verdicts (over-generosity check)

- **Offence/Defence Pool Split vs. Formation Declaration** — checked for duplicate coverage, since both
  are declared in the same Phase 1 (`mass_battle_v30.md` line 366–372) and both touch Offence/Defence
  balance. Confirmed genuinely distinct mechanically: Formation applies **fixed additive dice
  modifiers** tied to a discrete geometric/tactical choice with its own counter logic (Wedge beats
  Line, etc.), while Pool Split is a **continuous, secret, zero-sum reallocation of a shared Effective
  Pool** with no discrete counter-logic of its own. They stack meaningfully (e.g., Shield Wall's
  defensive lean can be partially offset by an offence-heavy secret split, or doubled down on) rather
  than duplicating one knob twice. Dossier's KEEP is not over-generous — upheld.
- **Sub-unit Assignment, Formation Declaration** — build_state_note fields correctly used only as
  routing metadata (ED-1090 cap reconciliation; ED-909 documentation residual), never as verdict
  evidence. No cardinal-rule violation found.
- **Tactic Card Play (Board Game layer)** — build_state_note explicitly documents the empty
  `FACTION_TACTIC_CARD_POOL_MODIFIERS` stub and explicitly disclaims it as a verdict input per the
  cardinal rule. Correctly calibrated; upheld.
- **Aftermath Choice** — build_state_note is scoped as "adjacent-lane awareness only (not a finding)"
  re: SE lane's settlement-governance action, correctly declining to make a cross-lane duplicate-
  coverage claim without visibility into SE's action set. Appropriately conservative; upheld.

**Cardinal-rule audit result:** no verdict in this dossier rests on build state as evidence. Every
`build_state_note` present is confined to routing metadata as the charter requires (§0, §4). No
corrections needed on that axis.

---

## Summary of changes

| Row | Dossier verdict | Critic outcome | Final verdict |
|---|---|---|---|
| Tactic: Concentration (isolated finding) | REFINE | OVERTURNED-TO-KEEP | KEEP (merged into parent menu row) |
| All other 12 rows | KEEP | UPHELD (spot-checked subset) | KEEP |

Net effect on the docket: **one fewer subtractive row.** This also narrows the `retires_downstream`
claim on the original Concentration row (Stratum E gauge-triage independent re-validation) — since
Concentration is not being reframed, that downstream narrowing does not occur; note this for the
verdict-rendering stage so the retires_downstream ledger isn't credited with work that no longer
happens.

