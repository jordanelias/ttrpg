# Refutation notes — finding `gm-controls-npc-votes`

## Claim
faction_layer_v30 §5.8 "explicitly delegates NPC faction voting to a human GM, contradicting the
no-GM engine premise and Omega clause (c) autonomous world." Direction top-down, Omega, P1, NEW.

## Text check (verbatim, holds literally)
- `designs/provincial/faction_layer_v30.md` L490 §5.8: "GM controls NPC faction votes (Guilds,
  Niflhel, and any other NPC-only factions)." — string IS present.
- BUT the same §5.8 immediately supplies a **fully deterministic** "Guilds AI vote rule": always
  against Blockade/Combined/Outlawry, for Subsidy, else "votes for whichever outcome reduces the
  highest Mandate faction's power" + ED-752 settlement-broker ±1 shift. This is engine-resolvable.
- Niflhel is **STRUCK** (L494, CR-STRIKE-2026-04-19); it does not vote. So the only live seated
  NPC-only faction named has a deterministic rule. The engine autonomy clause is materially
  satisfied for the live case.
- Sibling residue in same doc: L345 "Players/GM declare", L362 "GM adjudicates" — i.e. this is
  systemic dual-mode authoring residue, not a bespoke delegation decision at §5.8.

## Mode context (refutes the "contradiction" framing)
faction_layer_v30 is an explicitly tri-mode spec (§8: BG / TTRPG / Hybrid). §8.2 TTRPG mode has a
GM by construction. "GM controls NPC votes" is *correct for TTRPG mode*; the no-GM mandate targets
the videogame/engine build. §5.8 already ships the engine path (Guilds AI rule) alongside the
TTRPG-mode GM framing. The finding reads a TTRPG-mode line as if it were the engine spec.

## Intent / safeguard evidence (the decisive part)
- `designs/architecture/videogame_mode_spec.md` §3 L171: "Each design doc should be audited for
  'GM' references and resolved per the above types during Godot extraction." §4 L185 discard table:
  "GM adjudication → Engine handles all resolution. NPC AI + authored content + deterministic
  rules." => the corpus KNOWS docs carry GM residue and has a **declared, canonical translation
  process** for exactly this. Safeguarded, not accidental-unhandled.
- `canon/editorial_ledger.jsonl` **ED-1061** (ratified 2026-07-01): fixed the identical "GM picks"
  Guilds defect at another site (params/contest.md Faction Boosts / social_contest §2 Step 3),
  explicitly calling it "a stale no-GM defect," CANON-LEADS-CODE-FOLLOWS, treated as a routine
  **prose scrub**, filed P2-class. This is the governing precedent for the defect CLASS. §5.8 is a
  sibling instance ED-1061's sweep did not reach — same class, same trivial fix.

## Tracking / novelty
- Not literally duplicate of an ED for this exact site. ED-752 touched §5.8 (Niflhel-strike
  propagation) but not the "GM controls" phrase. So this specific string is KNOWN-UNTRACKED.
- Novelty "NEW" is wrong: it is the ED-1061 defect class + covered by videogame_mode_spec §3's
  standing "audit each doc for GM references" instruction. Should cite ED-1061 as class ref.

## Severity re-judgment vs North Star
Does fixing it widen meaningful choice / emergence / legibility? No. The Guilds
competitive-commercial voting dynamic already exists and is deterministic; scrubbing the vestigial
sentence and porting the rule changes no player-facing decision space. Residual genuine gap: "any
other NPC-only factions" (Schoenland/Altonia, §8.1) lack an explicit vote rule — but whether they
even hold peninsular Parliamentary seats is unstated (they are external powers: invasion threat /
naval mediator), so this is thin debt, not a choice-collapsing defect. P1 is overstated. This is a
P3 terminology scrub already covered by an existing standing process + ratified precedent.

## Verdict
REFUTED as stated (the load-bearing "P1 Omega contradiction / NEW" framing collapses). The string
exists but: (a) engine autonomy is satisfied for the live faction via the deterministic Guilds AI
rule; (b) the residue is a known, **safeguarded** dual-mode artifact with a declared corpus-wide
translation process (videogame_mode_spec §3/§4) and a ratified class precedent (ED-1061); (c) it is
not NEW. Honest residual: a P3 prose-scrub / port item, not a defect that undermines the North Star.
Intent NOT-INTENDED (stale residue) but safeguarded-by-process.
